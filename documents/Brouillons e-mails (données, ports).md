# Brouillons d'e-mails — données pour une version payante

Brouillons à relire et envoyer toi-même. Rien n'a été envoyé.

---

## 1. Open-Meteo (vent, vagues, eau, marées de Nouméa) — en anglais

**À :** info@open-meteo.com
**Objet :** Commercial API plan for a small marine forecast web app (France / New Caledonia)

Hello,

I run Crén'eau (https://pittilloni.github.io/creneau/), a small mobile web app that helps sailors,
kitesurfers, windsurfers and foilers in Deauville (Normandy, France) and Nouméa (New Caledonia)
decide when to go out. It currently uses your free API (forecast and marine endpoints:
Météo-France AROME/ARPEGE, ECMWF, ICON, UKMO, GFS, MFWAM, Météo-France currents).

We are considering a paid tier (a few euros per year per user). Before going further I would like to know:

1. The monthly price of the API Standard plan, and whether it fits our use: a few hundred to a few
   thousand users, roughly 10–20 API calls per user per day, cached server-side.
2. Whether the forecast and marine data we use (including the Météo-France models) can be shown
   to paying users under that plan, and which attribution you require.
3. Whether a small project can start on a lower volume and scale later.

Thank you for your work on Open-Meteo, it has been a great base for the app.

Best regards,
Antoine Pittilloni

---

## 2. Ports du Calvados (horaires des portes du bassin Morny)

**À :** contact via <https://www.portsducalvados.fr> (formulaire de contact) ou la capitainerie de Deauville (02 31 98 30 01)
**Objet :** Réutilisation des horaires de manœuvres du port de Deauville-Trouville dans une application

Bonjour,

Je développe Crén'eau (https://pittilloni.github.io/creneau/), une petite application web qui aide
les plaisanciers du port de Deauville à savoir quand sortir : elle affiche les horaires d'ouverture
des portes du bassin Morny, issus de votre document « Port de Deauville-Trouville — Horaires de
manœuvres 2026 », avec la source citée et un rappel de confirmer au VHF canal 9.

L'application est aujourd'hui gratuite. Nous envisageons une formule payante (quelques euros par an)
pour financer les données météo. Pourriez-vous m'indiquer :

1. si la réutilisation de ces horaires dans une application, gratuite puis éventuellement payante,
   est possible, et à quelles conditions ;
2. si vous publiez ces horaires dans un format exploitable (fichier, flux) ou à quelle date paraît
   le document 2027 ;
3. le bon interlocuteur pour la partie marées, calculée avec le SHOM (autorisation n° 2024-282).

Je vous signale au passage deux points relevés dans le PDF 2026 : l'ouverture des portes de la nuit
du 4 au 5 juillet n'y figure pas, et le 25 octobre est donné à l'heure d'été (correction publiée
par le Deauville Yacht Club).

Bien cordialement,
Antoine Pittilloni

---

## 3. SHOM (prédictions de marée)

**À :** via <https://www.shom.fr> → Contact / « Licences et réutilisation des données »
**Objet :** Licence de réutilisation des prédictions de marée (Deauville, Nouméa) dans une application

Bonjour,

Je développe Crén'eau, une application web d'aide à la sortie en mer (bateau, kitesurf) à Deauville
et à Nouméa. Elle affiche les pleines et basses mers : à Deauville d'après le document de Ports du
Calvados (calculé avec le SHOM, autorisation n° 2024-282), à Nouméa calculées à partir d'un modèle.

Nous envisageons une formule payante à petite échelle. Pourriez-vous m'indiquer la licence et le
tarif applicables pour afficher les prédictions de marée officielles du SHOM (Deauville, Nouméa)
dans une application, gratuite puis payante, et s'il existe une offre adaptée aux petits projets ?

Bien cordialement,
Antoine Pittilloni

---

## 4. HAROPA PORT — mesures SIMBAD (vent et houle dans le chenal de Port 2000)

**À :** communication.havre@haropaport.com
**Objet :** Demande d'autorisation — affichage des mesures SIMBAD dans une application gratuite pour les plaisanciers

Bonjour,

Je développe Crén'eau (https://pittilloni.github.io/creneau/), une petite application web gratuite qui
aide les plaisanciers et pratiquants de glisse de Deauville et de la baie de Seine à savoir quand sortir
(horaires des portes du bassin Morny, prévisions, houlographes Candhis du Havre).

Vos mesures SIMBAD (houle H1/3 et vent moyen dans le chenal d'accès à Port 2000) seraient très utiles à
nos utilisateurs pour confronter les prévisions à la réalité. Vos conditions générales d'utilisation
(articles 6 et 8) soumettent leur reproduction et les liens vers votre site à une autorisation écrite :
je sollicite donc cette autorisation pour :

1. afficher dans l'application la dernière mesure de vent (vitesse, direction) et de houle, avec l'heure
   de la mesure, la mention « Données HAROPA PORT, temps réel, droits réservés » et un lien vers
   havre-port.com ;
2. relever ces valeurs au plus toutes les 10 minutes (une seule requête pour tous les utilisateurs) ;
3. sans modification des valeurs, gratuitement, avec un rappel que ces informations sont indicatives.

Si un format de données (fichier, flux) est prévu pour ce type d'usage, je suis preneur. Je reste à votre
disposition pour toute précision.

Bien cordialement,
Antoine Pittilloni
