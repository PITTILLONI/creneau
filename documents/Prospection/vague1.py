# Vague 1 de prospection Crén'eau Club : côte normande, novembre 2026.
# Génère un mail par structure (texte brut + présentation PDF jointe) dans ./mails/
# puis `osascript brouillons.applescript` les dépose en brouillons dans Gmail (compte Google Perso).
# Rien n'est envoyé automatiquement : Antoine relit et envoie lui-même.
import json, os

ICI = os.path.dirname(os.path.abspath(__file__))

ECOLES = [
    # (clé, nom court, e-mail, formule d'appel, variante, accroche, plan B)
    ("kiteparadise", "Kite Paradise", "contact@kiteparadise.fr", "Bonjour,", "glisse",
     "Kite Paradise propose bien plus que le kite à Houlgate : foil, foil tracté, wake, bouée, paddle géant. C'est exactement le genre d'école pour qui un plan B change la journée.",
     "Pas assez de vent pour le kite ? L'app montre ce qui marche à cette heure-là (foil tracté, wake, paddle géant) et le moniteur le propose aux inscrits en un geste. La séance est gardée au lieu d'être reportée."),
    ("fiftykite", "Fifty Kite", "fifty.kite@gmail.com", "Bonjour David,", "glisse",
     "Vous enseignez sur plusieurs spots selon le vent et la marée, de Jullouville au secteur de Ravenoville : choisir le bon spot et prévenir vos élèves fait partie de chaque journée.",
     "Vent trop faible ou mal orienté sur un spot ? L'app compare vos spots heure par heure, et vous proposez aux inscrits le bon endroit ou le wing à la place du kite, en un geste."),
    ("northshore", "North Shore", "northshoreaccueil@gmail.com", "Bonjour,", "glisse",
     "À Trouville, la houle de la Manche ne se commande pas : selon les jours, la séance de surf est parfaite, impossible, ou à transformer en paddle.",
     "Houle trop faible ou trop forte pour le surf ? L'app montre ce qui marche à cette heure-là (paddle, balade, autre créneau de marée) et vous le proposez aux inscrits en un geste."),
    ("cotentinsurf", "Cotentin Surf Club", "cotentinsurfclub@orange.fr", "Bonjour,", "glisse",
     "Avec plus de 200 licenciés, des sections scolaires et la houle de Siouville, prévenir tout le monde au bon moment est déjà un métier en soi.",
     "Houle trop forte ou trop faible ? L'app montre ce qui marche à cette heure-là (paddle, autre spot, autre créneau de marée) et le moniteur le propose aux inscrits en un geste."),
    ("lyc", "Luc Yacht Club", "infos@lyc.asso.fr", "Bonjour,", "voile",
     "Le LYC fait naviguer des moussaillons dès 4 ans, du catamaran, du char à voile et du wing à Luc-sur-Mer : beaucoup d'activités, beaucoup de parents à prévenir quand la mer change d'avis.",
     "Mer trop formée pour le catamaran ? L'app montre ce qui marche à cette heure-là, par exemple le char à voile à marée basse, et le moniteur le propose aux inscrits en un geste."),
    ("cano", "CANO Ouistreham", "cano@ville-ouistreham.fr", "Bonjour,", "voile",
     "Le CANO réunit plusieurs associations et activités sur un même site, avec l'écluse, la marée et le chenal à composer chaque jour : un seul endroit pour l'information serait précieux à tout le monde.",
     "Mer trop formée pour la voile ? L'app montre ce qui marche à cette heure-là, par exemple le char à voile à marée basse ou le kayak, et le moniteur le propose aux inscrits en un geste."),
    ("ocean", "Océan", "contact.ocean14@gmail.com", "Bonjour,", "voile",
     "Océan fait naviguer et rouler ses stagiaires sur plusieurs plages, de Ouistreham à Lion-sur-Mer : choisir la bonne plage et la bonne heure selon le vent et la marée, c'est tout l'enjeu.",
     "Trop de mer pour la voile, ou plage couverte pour le char ? L'app compare vos sites et vos activités heure par heure, et le moniteur propose la bonne option aux inscrits en un geste."),
    ("dives", "École de voile de Port Guillaume", "polenautique@normandiecabourgpaysdauge.fr", "Bonjour,", "voile",
     "À Port Guillaume, la marée décide de l'accès à l'estuaire et à la mer : les créneaux de navigation changent chaque jour.",
     "Mer trop formée ou marée trop basse pour sortir ? L'app montre ce qui marche à cette heure-là et le moniteur propose l'autre créneau ou l'autre activité aux inscrits en un geste."),
    ("cabourg", "École de voile de Cabourg", "guillaumeboulard13@yahoo.fr", "Bonjour Guillaume,", "voile",
     "Hors saison, vous ouvrez selon les réservations et la météo : c'est exactement le moment où prévenir vite les inscrits fait gagner une journée.",
     "Mer trop formée pour le catamaran ? L'app montre ce qui marche à cette heure-là (planche, paddle, autre créneau) et vous le proposez aux inscrits en un geste."),
    ("carteret", "Club Nautique de Barneville-Carteret", "cnbcarteret@gmail.com", "Bonjour,", "voile",
     "Optimist, catamaran, planche, paddle et windfoil à Carteret, avec les courants de la côte des Isles : chaque support a ses limites, et chaque stage ses parents à prévenir.",
     "Mer trop formée pour le catamaran ? L'app montre ce qui marche à cette heure-là (optimist en zone abritée, paddle, autre créneau de marée) et le moniteur le propose aux inscrits en un geste."),
    ("8milles", "8 Milles Nautic", "contact@8millesnautic.com", "Bonjour,", "voile",
     "Pour le championnat de France kite et wing en octobre, vous choisissiez chaque jour parmi vos quatre bases selon la météo et la marée. C'est exactement ce que Crén'eau fait, tous les jours, pour vos stagiaires.",
     "Mer trop formée à Granville ? L'app compare vos bases et vos activités heure par heure (char à voile à Jullouville, wing à Bréville…) et le moniteur propose la bonne option aux inscrits en un geste."),
    ("dieppe", "Cercle de la Voile de Dieppe", "contact@cvdieppe.fr", "Bonjour,", "voile",
     "Optimist dès 6 ans, dériveurs l'été, stages en habitable : à Dieppe, entre la houle de la Manche et le port, chaque public a ses limites de vent et de mer.",
     "Mer trop formée pour les dériveurs ? L'app montre ce qui marche à cette heure-là et le moniteur propose l'autre créneau ou l'autre support aux inscrits en un geste."),
]

INTRO = ("Je m'appelle Antoine Pittilloni. Je navigue et je ride sur la côte normande, et je développe Crén'eau, "
         "une app qui dit quand aller sur l'eau : vent, rafales, mer, marée et température de l'eau, spot par spot. "
         "Elle tourne déjà pour les pratiquants de Deauville.")

FIN = """La partie club se met en place avec vous en six semaines : vos couleurs et vos consignes la première semaine, les séances et inscriptions la troisième, les inscrits prévenus en un geste la sixième. C'est un pilote : rodage offert, sans engagement, et on fait le bilan ensemble au bout de deux mois.

Tout est résumé dans la présentation jointe (3 pages). Le plus parlant serait de vous la montrer en 20 minutes, sur place ou par téléphone, quand cela vous arrange.

Bien à vous,
Antoine Pittilloni
06 67 72 47 07
antoine.pittilloni@gmail.com"""

def corps(appel, variante, accroche, planb):
    if variante == "glisse":
        apport = f"""Ce que ça vous apporte, à l'école :
- Moins de téléphone. Le vent ou la houle change : le moniteur décale ou annule la séance, et tous les inscrits le savent dans la minute, avec la raison et le nouvel horaire. Ils confirment dans l'app, vous savez qui vient.
- Moins de séances perdues. {planb}
- Vos règles appliquées. Chaque séance est notée selon vos limites (vent, rafales, orientation, houle, marée), par niveau : les moniteurs partent du même constat.
- Des cours remplis : places restantes, liste d'attente, inscription en un geste.

Ce que ça apporte à vos élèves :
- Savoir à l'avance si « ça sort », et pourquoi, sans appeler l'école.
- Le bon créneau, le matériel conseillé selon les conditions, l'eau et la combinaison.
- Après le stage, l'app reste : ils reviennent sur l'eau, et reviennent chez vous."""
    else:
        apport = f"""Ce que ça vous apporte, au club :
- Moins de téléphone. Une séance décalée, annulée ou changée d'activité : tous les inscrits, et les parents des mineurs, sont prévenus d'un coup, avec la raison. Ils confirment dans l'app, vous savez qui vient.
- Moins de séances perdues. {planb} La séance est gardée au lieu d'être annulée ou remboursée.
- Vos consignes appliquées. Chaque séance est notée selon vos limites de vent, de rafales et de mer, par support et par âge : les moniteurs partent du même constat.
- Des stages remplis : places restantes, liste d'attente, inscription en un geste.

Ce que ça apporte à vos stagiaires et à leurs familles :
- Savoir à l'avance si « ça sort », et pourquoi, sans appeler le club.
- Choisir le bon créneau : chaque séance notée, les places restantes.
- Après le stage, l'app reste : vent, mer, marée, eau et combinaison conseillée toute l'année. De quoi revenir naviguer, et revenir au club."""
    return f"""{appel}

{INTRO}

{accroche}

Je cherche quelques clubs et écoles pilotes pour 2027. Crén'eau Club, c'est l'app réglée pour votre structure, à vos couleurs.

{apport}

{FIN}"""

def objet(nom, variante):
    if variante == "glisse":
        return f"{nom} : vos élèves prévenus en un geste, vos séances gardées"
    return f"{nom} : vos stagiaires prévenus, vos séances gardées"

if __name__ == "__main__":
    os.makedirs(os.path.join(ICI, "mails"), exist_ok=True)
    index = []
    for cle, nom, mail, appel, var, acc, pb in ECOLES:
        p = os.path.join(ICI, "mails", cle + ".txt")
        open(p, "w").write(corps(appel, var, acc, pb))
        index.append({"cle": cle, "a": mail, "objet": objet(nom, var), "corps": p})
    json.dump(index, open(os.path.join(ICI, "mails", "index.json"), "w"), ensure_ascii=False, indent=1)
    print(len(index), "mails générés")
