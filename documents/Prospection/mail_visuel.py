# Mail visuel Crén'eau Club (HTML en tableaux, compatible Gmail / Apple Mail / Outlook),
# même design que celui validé le 23 octobre : 600 px centré, blocs gris à liseré bleu (club)
# et vert (stagiaires), frise des semaines, encadré « Rodage offert ».
# Usage : python3 mail_visuel.py  → mails/<clé>.html + mails/index.json (nouvelles écoles et relances)
import json, os, html as H
from vague1 import ECOLES

ICI = os.path.dirname(os.path.abspath(__file__))
INK, MUTE, BLUE, GREEN, BG, SOFT = "#0a0d14", "#3a4255", "#0238ff", "#126c35", "#eff1f5", "#dde6ff"
FONT = "'Helvetica Neue',Helvetica,Arial,sans-serif"

def p(txt, mb=14, size=15, color=INK, lh=1.55):
    return f'<p style="margin:0 0 {mb}px;font-family:{FONT};font-size:{size}px;line-height:{lh};color:{color}">{txt}</p>'

def bloc(titre, couleur, items):
    rows = "".join(
        f'''<tr><td style="padding:0 0 10px"><table role="presentation" cellpadding="0" cellspacing="0" width="100%"><tr>
<td width="4" style="background:{couleur};font-size:0;line-height:0">&nbsp;</td>
<td style="padding:2px 0 2px 12px;font-family:{FONT};font-size:15px;line-height:1.45;color:{INK}"><b>{t}</b><br><span style="color:{MUTE}">{d}</span></td>
</tr></table></td></tr>''' for t, d in items)
    return f'''<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="background:{BG};border-radius:10px;margin:0 0 14px">
<tr><td style="padding:18px 20px 8px">
<p style="margin:0 0 10px;font-family:{FONT};font-size:12px;letter-spacing:.06em;color:{couleur}"><b>{titre}</b></p>
<table role="presentation" cellpadding="0" cellspacing="0" width="100%">{rows}</table>
</td></tr></table>'''

def frise():
    def c(sem, txt, fort=False):
        st = f"background:{BLUE};color:#fff" if fort else f"color:{BLUE}"
        return f'''<td width="33%" align="center" style="padding:0 4px;font-family:{FONT}">
<div style="{st};font-size:12px;font-weight:bold;padding:3px 0;border-radius:4px">{sem}</div>
<div style="font-size:13px;color:{INK};padding-top:4px">{txt}</div></td>'''
    return f'''<p style="margin:20px 0 10px;font-family:{FONT};font-size:15px;color:{INK}"><b>En place en six semaines</b></p>
<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="margin:0 0 18px"><tr>
{c("Semaine 1","Vos couleurs et vos consignes")}{c("Semaine 3","Séances et inscriptions")}{c("Semaine 6","Prévenus en un geste",True)}
</tr></table>'''

def offre():
    return f'''<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="background:{SOFT};border-radius:10px;margin:0 0 18px">
<tr><td style="padding:16px 20px;font-family:{FONT};font-size:15px;line-height:1.5;color:{INK}">
<b style="color:{BLUE}">Rodage offert, sans engagement.</b> On règle tout ensemble, et on fait le bilan au bout de deux mois.</td></tr></table>'''

def signature(lieu):
    return (p(f"Tout est dans la présentation jointe (3 pages). <b>Le plus parlant : 20 minutes {lieu}</b> pour vous montrer l'app, quand cela vous arrange.")
            + p("Bien à vous,<br><b>Antoine Pittilloni</b><br>"
                f'<span style="color:{MUTE}">06 67 72 47 07 · antoine.pittilloni@gmail.com</span>', mb=0))

def cadre(contenu):
    return f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"></head>
<body style="margin:0;padding:0;background:#ffffff">
<table role="presentation" cellpadding="0" cellspacing="0" width="100%"><tr><td align="center" style="padding:8px 16px">
<table role="presentation" cellpadding="0" cellspacing="0" width="600" style="width:100%;max-width:600px"><tr><td align="left">
{contenu}
</td></tr></table></td></tr></table></body></html>'''

TITRE = (f'<p style="margin:0;font-family:{FONT};font-size:22px;line-height:1.25;color:{INK}"><b>Le vent change, la séance aussi.</b></p>'
         f'<p style="margin:0 0 16px;font-family:{FONT};font-size:22px;line-height:1.25;color:{BLUE}"><b>Et tout le monde est prévenu.</b></p>')

def mail(appel, variante, accroche, planb):
    e = H.escape
    intro = (p(e(appel))
             + p("Je suis Antoine Pittilloni, marin et kitesurfeur à Deauville. Je développe <b>Crén'eau</b>, "
                 "l'app qui dit quand aller sur l'eau : vent, mer, marée, plage par plage.")
             + p(e(accroche))
             + p("Je cherche <b>quelques clubs et écoles pilotes pour 2027</b> : l'app réglée pour votre structure, à vos couleurs.", mb=20))
    if variante == "glisse":
        a = bloc("POUR L'ÉCOLE", BLUE, [
            ("Moins de téléphone", "Le vent ou la houle change : séance décalée ou annulée, tous les inscrits prévenus d'un coup, avec la raison. Vous savez qui vient."),
            ("Moins de séances perdues", e(planb)),
            ("Vos règles appliquées", "Chaque séance notée selon vos limites de vent, rafales, orientation, houle et marée, par niveau."),
            ("Des cours remplis", "Places restantes, liste d'attente, inscription en un geste.")])
        b = bloc("POUR VOS ÉLÈVES", GREEN, [
            ("Savoir si « ça sort »", "À l'avance, avec la raison, sans appeler l'école."),
            ("Garder leur séance", "Un plan B plutôt qu'une journée perdue."),
            ("Revenir sur l'eau", "Après le stage, l'app reste : vent, mer, marée, combinaison conseillée.")])
        lieu = "à l'école"
    else:
        a = bloc("POUR LE CLUB", BLUE, [
            ("Moins de téléphone", "Séance décalée ou changée d'activité : inscrits et parents prévenus d'un coup, avec la raison. Vous savez qui vient."),
            ("Moins de séances perdues", e(planb) + " La séance est gardée."),
            ("Vos consignes appliquées", "Chaque séance notée selon vos limites de vent, rafales et mer, par support et par âge."),
            ("Des stages remplis", "Places restantes, liste d'attente, inscription en un geste.")])
        b = bloc("POUR VOS STAGIAIRES ET LEURS FAMILLES", GREEN, [
            ("Savoir si « ça sort »", "À l'avance, avec la raison, sans appeler le club."),
            ("Garder leur séance", "Un plan B plutôt qu'une matinée perdue."),
            ("Revenir naviguer", "Après le stage, l'app reste : vent, mer, marée, combinaison conseillée.")])
        lieu = "au club"
    return cadre(intro + TITRE + a + b + frise() + offre() + signature(lieu))

def relance(appel, texte, lieu):
    return cadre(p(H.escape(appel)) + "".join(p(t) for t in texte) + TITRE + offre() + signature(lieu))

RELANCES = [
    ("menhir", "quentin@lemenhir.com", "Re : Crén'eau Club pour Le Menhir",
     "École Le Menhir/1 - Présentation Crén'eau Club pour Le Menhir.pdf", "Salut Quentin,",
     ["Je reviens vers toi pour Crén'eau Club, suite à mon mail du 23 octobre (je t'écris cette fois depuis mon adresse perso).",
      "La saison se termine : c'est le bon moment pour en parler, avant de préparer 2027. Je peux passer au Cap Cabourg ou t'appeler, quand ça t'arrange.",
      "En deux mots : l'app réglée pour Le Menhir, <b>tes élèves prévenus en un geste</b> quand le vent tourne, et <b>un plan B</b> quand il ne suit pas. Je remets la présentation en pièce jointe."],
     "au Cap Cabourg"),
    ("cnth", "cnth@cnth.org", "CNTH club pilote 2027 : on en parle avant la saison ?",
     "Club Nautique Trouville (CNTH)/1 - Présentation Crén'eau Club pour le CNTH.pdf", "Bonjour,",
     ["Je me permets de revenir vers vous au sujet de Crén'eau Club, suite à mon message du 23 octobre (envoyé depuis une autre adresse, il a pu vous échapper).",
      "La saison se termine : c'est le bon moment pour en parler avant de préparer 2027. Je peux passer au club ou vous appeler, quand cela vous arrange.",
      "En deux mots : l'app réglée pour le CNTH, <b>vos stagiaires et leurs parents prévenus en un geste</b> quand la mer change d'avis, et <b>un plan B</b> (char à voile, autre support) plutôt qu'une séance annulée. Je remets la présentation en pièce jointe."],
     "au club"),
    ("pnvb", "contact.pnvb@gmail.com", "PNVB club pilote 2027 : on en parle avant la saison ?",
     "Pôle Nautique Villers-Blonville (PNVB)/1 - Présentation Crén'eau Club pour le PNVB.pdf", "Bonjour,",
     ["Je me permets de revenir vers vous au sujet de Crén'eau Club, suite à mon message du 23 octobre (envoyé depuis une autre adresse, il a pu vous échapper).",
      "La saison se termine : c'est le bon moment pour en parler avant de préparer 2027. Je peux passer au club ou vous appeler, quand cela vous arrange.",
      "En deux mots : l'app réglée pour le PNVB, <b>vos stagiaires et leurs parents prévenus en un geste</b> quand la mer change d'avis, et <b>un plan B</b> (char à voile, autre support) plutôt qu'une séance annulée. Je remets la présentation en pièce jointe."],
     "au club"),
]

if __name__ == "__main__":
    from vague1 import objet
    os.makedirs(os.path.join(ICI, "mails"), exist_ok=True)
    docs = os.path.dirname(ICI)
    generique = os.path.join(ICI, "Présentation Crén'eau Club (générique).pdf")
    index = []
    for cle, nom, a, appel, var, acc, pb in ECOLES:
        f = os.path.join(ICI, "mails", cle + ".html")
        open(f, "w").write(mail(appel, var, acc, pb))
        index.append({"cle": cle, "a": a, "objet": objet(nom, var), "html": f, "pdf": generique})
    for cle, a, obj, pdf, appel, texte, lieu in RELANCES:
        f = os.path.join(ICI, "mails", "relance-" + cle + ".html")
        open(f, "w").write(relance(appel, texte, lieu))
        index.append({"cle": "relance-" + cle, "a": a, "objet": obj, "html": f, "pdf": os.path.join(docs, pdf)})
    json.dump(index, open(os.path.join(ICI, "mails", "index.json"), "w"), ensure_ascii=False, indent=1)
    print(len(index), "mails visuels générés")
