#!/usr/bin/env python3
"""Mesures en direct des bouées houlographes au large du Havre (réseau Candhis, Cerema).

Lit la page publique de chaque campagne (tableau « Temps réel », une mesure toutes
les 30 min, heures en TU) et écrit un JSON compact que la page charge.
Candhis n'autorise pas les appels directs depuis un navigateur (pas de CORS) :
ce script tourne dans GitHub Actions (.github/workflows/bouees.yml) et publie
le fichier sur la branche `donnees`.

Données Candhis sous Licence Ouverte Etalab : citer la source et la date de mise à jour.
Usage : python3 tools/bouees.py > bouees.json
"""
import base64, datetime, html, json, re, sys, urllib.request

BOUEES = [
    # n° Candhis, nom, position, fond (m) : métadonnées de candhis.cerema.fr/_public_/cartes.php
    {'id': '07609', 'name': 'Le Havre · Haut du Sud-Ouest', 'lat': 49.4750, 'lon': 0.0842, 'depth': 8},
    {'id': '07611', 'name': 'Le Havre · Nord du mouillage', 'lat': 49.4799, 'lon': 0.0037, 'depth': 11},
]
GARDER_H = 24   # heures de mesures gardées pour la courbe


def num(t):
    t = t.strip().replace(',', '.')
    try:
        return float(t)
    except ValueError:
        return None


def mesures(camp):
    url = 'https://candhis.cerema.fr/_public_/campagne.php?' + base64.b64encode(('camp=' + camp).encode()).decode()
    req = urllib.request.Request(url, headers={'User-Agent': 'deauville-passerelle-ecluse (github.com/PITTILLONI)'})
    page = urllib.request.urlopen(req, timeout=60).read().decode('utf-8', 'replace')
    out = []
    # tableau « Date | Heure (TU) | H1/3 | Hmax | Th1/3 | Dir. au pic | Etal. au pic | Temp. mer »
    for row in re.findall(r'<tr>(.*?)</tr>', page, re.S):
        cells = [html.unescape(re.sub(r'<[^>]+>', '', c)).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)]
        if len(cells) < 7 or not re.match(r'\d\d/\d\d/\d{4}$', cells[0]):
            continue
        d, m, y = cells[0].split('/')
        t = datetime.datetime(int(y), int(m), int(d), *map(int, cells[1].split(':')), tzinfo=datetime.timezone.utc)
        h, hmax, tp, dirp, etal, sst = (num(c) for c in (cells[2:8] + [''] * 6)[:6])
        out.append({'t': int(t.timestamp()), 'h': h, 'hmax': hmax, 'tp': tp, 'dir': dirp, 'etal': etal, 'sst': sst})
    out.sort(key=lambda x: x['t'])
    if out:
        last = out[-1]['t']
        out = [x for x in out if x['t'] >= last - GARDER_H * 3600]
    return out


def main():
    res = {'updated': int(datetime.datetime.now(datetime.timezone.utc).timestamp()), 'buoys': []}
    for b in BOUEES:
        try:
            obs = mesures(b['id'])
        except Exception as e:   # une bouée en panne ne doit pas bloquer l'autre
            print('bouée', b['id'], ':', e, file=sys.stderr)
            obs = []
        res['buoys'].append(dict(b, obs=obs))
    json.dump(res, sys.stdout, separators=(',', ':'))


if __name__ == '__main__':
    main()
