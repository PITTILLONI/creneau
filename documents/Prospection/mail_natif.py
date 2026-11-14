# Mail Crén'eau Club en HTML natif (aucune image) : reprend la présentation PDF en blocs de mail.
# Tableaux + styles en ligne, compatible Gmail, Apple Mail, Outlook. Texte = texte (lisible, sélectionnable).
# Usage : python3 mail_natif.py → mails/<clé>.html + mails/index.json
import json, os, html as H
from vague1 import ECOLES, objet

ICI = os.path.dirname(os.path.abspath(__file__))
INK, INK2, MUTE = "#0a0f1a", "#4a5468", "#6b7385"
BLUE, BLUE_SOFT = "#0057ff", "#e6eeff"
GREEN, GREEN_SOFT = "#0a7d45", "#e3f4ea"
AMBER, AMBER_SOFT = "#9a5b00", "#fdf0d8"
CARD, LINE, NAVY = "#f2f4f7", "#e3e7ee", "#0b3d5c"
F = "'Helvetica Neue',Helvetica,Arial,sans-serif"
e = H.escape

def t(txt, size=15, color=INK, weight="normal", mb=0, lh=1.5, extra=""):
    return (f'<p style="margin:0 0 {mb}px;font-family:{F};font-size:{size}px;line-height:{lh};'
            f'color:{color};font-weight:{weight};{extra}">{txt}</p>')

def table(inner, bg=None, pad=0, mb=0, radius=14, width="100%", h=""):
    b = f"background:{bg};" if bg else ""
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="{width}" {h} '
            f'style="{b}border-radius:{radius}px;border-collapse:separate;margin:0 0 {mb}px">'
            f'<tr><td valign="top" style="padding:{pad}px">{inner}</td></tr></table>')

def pill(txt, fg, bg):
    # tableau qui épouse son contenu : reste une pastille même après réécriture par Apple Mail
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="display:inline-table"><tr>'
            f'<td style="background:{bg};border-radius:99px;padding:3px 10px;font-family:{F};font-size:12px;'
            f'font-weight:bold;color:{fg};white-space:nowrap">{txt}</td></tr></table>')

def cols(cells, gap=10, valign="top"):
    n = len(cells); w = f"{100 // n}%"
    tds = []
    for i, c in enumerate(cells):
        pl = 0 if i == 0 else gap // 2; pr = 0 if i == n - 1 else gap // 2
        tds.append(f'<td width="{w}" valign="{valign}" height="100%" style="padding:0 {pr}px 0 {pl}px;height:100%">{c}</td>')
    return f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" height="1" style="height:1px"><tr>{"".join(tds)}</tr></table>'

def carte(titre, texte, bg=CARD):
    return table(t(titre, 15, INK, "bold", 6, 1.3) + t(texte, 14, INK2, lh=1.45), bg, 16, 0, 12, h='height="100%"')

# ---------- maquette de l'app, en HTML ----------
def maquette(v):
    if v == "glisse":
        tete, avant, apres = "SAMEDI · KITE · INITIATION", "Kite 14:00 – 17:00", "Wing 14:30"
        raison = "Vent trop faible pour le kite (11 nœuds). Assez pour le wing, plan d'eau à marée haute : idéal."
        qui = "4 élèves prévenus · 4 confirmés"
        msg_m = "Pas assez de vent pour les ailes cet après-midi : on part en wing à 14 h 30. Matériel fourni."
        nom_r, msg_r, moi = "Léa", "Top, j'arrive !", "Hugo sera là à 14 h 15."
    else:
        tete, avant, apres = "SAMEDI · CATAMARAN · ADOS 12-15 ANS", "Catamaran 10:00 – 12:00", "Char à voile 10:30"
        raison = "Mer trop formée pour les catamarans (1,6 m). Plage à découvert à marée basse, 22 nœuds : idéal pour le char."
        qui = "8 inscrits et leurs parents prévenus · 7 confirmés"
        msg_m = "Trop de mer pour les cata ce matin : on part en char à voile à 10 h 30. Casques fournis."
        nom_r, msg_r, moi = "Claire, maman d'Inès", "Super, elle sera là !", "Hugo sera là à 10 h 15."
    barre = (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" '
             f'style="background:{NAVY};border-radius:10px;margin:0 0 10px"><tr>'
             f'<td style="padding:9px 12px;font-family:{F};font-size:13px;font-weight:bold;color:#fff">{"Votre école" if v == "glisse" else "Votre club"}</td></tr></table>')
    seance = table(
        t(tete, 10, MUTE, "bold", 4, 1.3, "letter-spacing:.03em")
        + t(avant, 12, MUTE, mb=2, extra="text-decoration:line-through")
        + t(apres, 20, INK, "bold", 6, 1.15)
        + t(raison, 12, INK2, mb=8, lh=1.4)
        + t(f'<span style="color:{GREEN};font-weight:bold">{qui}</span>', 12, INK2, lh=1.35),
        "#ffffff", 12, 10, 10)
    def bulle(nom, txt, bleu=False):
        if bleu:
            return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 6px"><tr>'
                    f'<td width="18%"></td><td style="background:{BLUE};border-radius:12px;padding:8px 10px;font-family:{F};'
                    f'font-size:12px;line-height:1.35;color:#fff">{txt}</td></tr></table>')
        return (t(nom, 10, MUTE, "bold", 3) +
                f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 6px"><tr>'
                f'<td style="background:#fff;border-radius:12px;padding:8px 10px;font-family:{F};font-size:12px;'
                f'line-height:1.35;color:{INK}">{txt}</td><td width="14%"></td></tr></table>')
    conv = (t("Conversation de la séance", 12, INK, "bold", 6)
            + bulle(f'Moniteur', msg_m) + bulle(nom_r, msg_r) + bulle("", moi, True))
    ecran = barre + seance + conv
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" '
            f'style="background:{INK};border-radius:26px;border-collapse:separate"><tr><td style="padding:7px">'
            f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" '
            f'style="background:{CARD};border-radius:20px;border-collapse:separate"><tr><td style="padding:12px 10px 8px">'
            f'{ecran}</td></tr></table></td></tr></table>')

def point(titre, txt):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 14px"><tr>'
            f'<td width="4" style="background:{BLUE};border-radius:2px;font-size:0">&nbsp;</td>'
            f'<td style="padding:0 0 0 12px">{t(titre, 14, INK, "bold", 3, 1.3)}{t(txt, 13, INK2, lh=1.45)}</td></tr></table>')

def mail(nom, appel, v, accroche, planb):
    club = "l'école" if v == "glisse" else "le club"
    inscrits = "les élèves" if v == "glisse" else "stagiaires et parents"
    entete = (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 26px"><tr>'
              f'<td style="font-family:{F};font-size:16px;font-weight:bold;color:{INK}">'
              f'<span style="color:{BLUE}">C</span>&nbsp;Crén\'eau Club</td>'
              f'<td align="right" style="font-family:{F};font-size:12px;color:{MUTE}">Pilotes 2027 · côte normande</td></tr></table>')
    intro = (t(e(appel), mb=14)
             + t("Je suis Antoine Pittilloni, marin et kitesurfeur à Deauville. Je développe <b>Crén'eau</b>, "
                 "l'app qui dit quand aller sur l'eau : vent, mer, marée, plage par plage.", mb=14)
             + t(e(accroche), mb=14)
             + t("Je cherche <b>quelques clubs et écoles pilotes pour 2027</b>. Voici l'idée en une minute.", mb=30))
    titre = (t("Le vent change, la séance aussi.", 30, INK, "800", 0, 1.08, "letter-spacing:-.02em")
             + t("Et tout le monde est prévenu.", 30, BLUE, "800", 14, 1.08, "letter-spacing:-.02em")
             + f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 26px"><tr>'
               f'<td width="22" valign="middle"><div style="height:3px;line-height:3px;font-size:0;background:{GREEN};border-radius:2px">&nbsp;</div></td>'
               f'<td style="padding-left:10px;font-family:{F};font-size:15px;font-weight:bold;color:{INK}">Sur mesure pour {e(nom)}.</td></tr></table>')
    piliers = cols([
        carte("Tout au même endroit", "Vent, mer, marée, séances, inscriptions et reports. Fini les SMS un par un."),
        carte("Prévenu en un geste", f"Le moniteur décale ou bascule la séance : {inscrits} le savent dans la minute."),
        carte(f"Fait pour {club}", "Votre spot et ses vents, vos supports, vos consignes par niveau, vos couleurs."),
    ])
    prevenu = (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 4px"><tr>'
               f'<td style="font-family:{F};font-size:22px;font-weight:bold;color:{INK};padding-right:10px">Prévenu en un geste</td>'
               f'<td valign="middle">{pill("Bientôt", BLUE, BLUE_SOFT)}</td></tr></table>'
               + t(f"La mer décide de la journée : {club} la réorganise en un message.", 14, INK2, mb=18)
               + f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%"><tr>'
                 f'<td width="46%" valign="top">{maquette(v)}</td><td width="5%"></td>'
                 f'<td valign="top" style="padding-top:4px">'
                 + point("Décaler ou basculer", "Nouvel horaire ou autre activité, avec la raison chiffrée.")
                 + point("Moins de séances perdues", e(planb))
                 + point("Qui vient, d'un coup d'œil", "Chacun confirme ; la place libre repart vers la liste d'attente.")
                 + point("Vos consignes appliquées", "Limites de vent, rafales, mer et marée, par support et par niveau.")
                 + '</td></tr></table>')
    etape = lambda p, titre, txt, bg=CARD: table(p + t(titre, 14, INK, "bold", 3, 1.3, "margin-top:8px") + t(txt, 13, INK2, lh=1.4), bg, 14, 0, 12, h='height="100%"')
    plan = (t("En route en six semaines", 22, INK, "bold", 4, 1.3)
            + t("Comptées à partir de votre accord. Ce qui est prêt arrive dès la première.", 14, INK2, mb=14)
            + cols([etape(pill("Semaine 1", GREEN, GREEN_SOFT), "L'app à vos couleurs", "Votre spot, vos activités et leurs consignes."),
                    etape(pill("Semaine 3", AMBER, AMBER_SOFT), "Séances et inscriptions", "Places, liste d'attente, inscrits côté moniteur.")])
            + '<div style="height:10px;line-height:10px;font-size:0">&nbsp;</div>'
            + cols([etape(pill("Semaine 6", "#ffffff", BLUE), "Prévenu en un geste", "Séance décalée ou basculée : tout le monde averti.", BLUE_SOFT),
                    etape(pill("Ensuite", BLUE, "#ffffff"), "Avec vous", "Plan B entre activités, réservation et paiement si vous le souhaitez.")]))
    offre = table(t("La proposition : rodage offert", 19, INK, "bold", 8, 1.3)
                  + t("<b>Offert</b> jusqu'à ce que « Prévenu en un geste » tourne chez vous, deux mois au plus. "
                      "Sans engagement. Construit avec vos moniteurs, puis bilan ensemble.", 15, INK2, lh=1.5),
                  CARD, 20, 0, 14)
    lieu = "à l'école" if v == "glisse" else "au club"
    fin = (t(f"La présentation complète est jointe (3 pages). <b>Le plus parlant : 20 minutes {lieu}</b> pour vous montrer l'app, quand cela vous arrange.", mb=16)
           + t(f"Bien à vous,<br><b>Antoine Pittilloni</b><br><span style=\"color:{MUTE}\">06 67 72 47 07 · antoine.pittilloni@gmail.com</span>"))
    sp = lambda h: f'<div style="height:{h}px;line-height:{h}px;font-size:0">&nbsp;</div>'
    corps = entete + intro + titre + piliers + sp(36) + prevenu + sp(30) + plan + sp(26) + offre + sp(24) + fin
    return ('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"></head>'
            '<body style="margin:0;padding:0;background:#ffffff">'
            '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%"><tr><td align="center" style="padding:16px">'
            f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="600" style="width:600px;max-width:100%"><tr><td align="left">{corps}</td></tr></table>'
            '</td></tr></table></body></html>')

def relance(nom, appel, textes, v, lieu):
    club = "l'école" if v == "glisse" else "le club"
    entete = (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 26px"><tr>'
              f'<td style="font-family:{F};font-size:16px;font-weight:bold;color:{INK}"><span style="color:{BLUE}">C</span>&nbsp;Crén\'eau Club</td>'
              f'<td align="right" style="font-family:{F};font-size:12px;color:{MUTE}">Pilotes 2027 · côte normande</td></tr></table>')
    corps = entete + t(e(appel), mb=14) + "".join(t(x, mb=14) for x in textes)
    corps += '<div style="height:16px;font-size:0">&nbsp;</div>'
    corps += (t("Le vent change, la séance aussi.", 30, INK, "800", 0, 1.08, "letter-spacing:-.02em")
              + t("Et tout le monde est prévenu.", 30, BLUE, "800", 22, 1.08, "letter-spacing:-.02em"))
    corps += cols([carte("Tout au même endroit", "Vent, mer, marée, séances, inscriptions et reports."),
                   carte("Prévenu en un geste", "Le moniteur décale ou bascule la séance, tout le monde le sait dans la minute."),
                   carte(f"Fait pour {nom}", "Votre spot, vos supports, vos consignes, vos couleurs.")])
    corps += '<div style="height:22px;font-size:0">&nbsp;</div>'
    corps += table(t("La proposition : rodage offert", 19, INK, "bold", 8, 1.3)
                   + t("<b>Offert</b> jusqu'à ce que « Prévenu en un geste » tourne chez vous, deux mois au plus. Sans engagement.", 15, INK2), CARD, 20, 0, 14)
    corps += '<div style="height:22px;font-size:0">&nbsp;</div>'
    corps += t(f"Bien à vous,<br><b>Antoine Pittilloni</b><br><span style=\"color:{MUTE}\">06 67 72 47 07 · antoine.pittilloni@gmail.com</span>")
    return ('<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0;padding:0;background:#ffffff">'
            '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%"><tr><td align="center" style="padding:16px">'
            f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="600" style="width:600px;max-width:100%"><tr><td align="left">{corps}</td></tr></table>'
            '</td></tr></table></body></html>')


if __name__ == "__main__":
    os.makedirs(os.path.join(ICI, "mails"), exist_ok=True)
    generique = os.path.join(ICI, "Présentation Crén'eau Club (générique).pdf")
    index = []
    for cle, nom, a, appel, v, acc, pb in ECOLES:
        f = os.path.join(ICI, "mails", cle + ".html")
        open(f, "w").write(mail(nom, appel, v, acc, pb))
        index.append({"cle": cle, "a": a, "objet": objet(nom, v), "html": f, "pdf": generique})
    from mail_visuel import RELANCES
    noms = {"menhir": ("Le Menhir", "glisse"), "cnth": ("le CNTH", "voile"), "pnvb": ("le PNVB", "voile")}
    docs = os.path.dirname(ICI)
    for cle, a, obj, pdf, appel, textes, lieu in RELANCES:
        nom, v = noms[cle]
        f = os.path.join(ICI, "mails", "relance-" + cle + ".html")
        open(f, "w").write(relance(nom, appel, textes, v, lieu))
        index.append({"cle": "relance-" + cle, "a": a, "objet": obj, "html": f, "pdf": os.path.join(docs, pdf)})
    json.dump(index, open(os.path.join(ICI, "mails", "index.json"), "w"), ensure_ascii=False, indent=1)
    print(len(index), "mails natifs générés")
