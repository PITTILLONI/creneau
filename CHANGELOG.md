# Historique des versions

## 17 octobre 2026 (13h) — En-tête : sélecteur de profil en haut
- Le titre « Port de Deauville » laisse la place au **sélecteur Bateau / Kitesurf**, fixé en haut de l'écran. Juste en dessous : « Port de Deauville · bassin Morny » en mode Bateau, ou le **choix du spot** (Deauville, Trouville, Houlgate, Cabourg) en mode Kitesurf, avec l'heure en direct.

## 17 octobre 2026 (12h45) — Voilure et allures pour le bateau
- Mode Bateau : **voilure conseillée** pour le créneau d'écluse (grand-voile haute / 1, 2 ou 3 ris, génois entier ou roulé), calculée sur les rafales, avec alertes mer formée, nuit, « prends les ris au port ».
- **Allure et réglages vers les destinations** (Le Havre, Honfleur, Dives, Ouistreham, le large) selon le vent prévu : vent debout, près, bon plein, travers, largue, vent arrière, avec les réglages de chaque allure.
- Hypothèse : voilier de 13 m gréé en sloop, grand-voile 3 ris, génois sur enrouleur.

## 17 octobre 2026 (12h35) — Schémas techniques précis pour les tutos kite
- Les illustrations générées plaçaient mal l'aile (bord d'attaque, valve, sens du vent). Elles sont remplacées par des **schémas techniques annotés** :
  - au sol (zone, dérouler, étaler, gonfler, connecter, sécuriser) : vue de dessus, mer et vent toujours en bas, rider face à son aile donc **rouge toujours à gauche**, encart « vu de côté » pour la position de l'aile ;
  - en l'air (s'accrocher, bord de fenêtre, tendre, monter, atterrir, water start) : vue de derrière le rider, vent dans le dos, fenêtre en cadran 9 h / 12 h / 3 h et zone de puissance.
- Connexion des lignes et aile sécurisée : **aile dos vers le ciel, bord d'attaque face au vent**.
- Water start redessiné, avec la comparaison « barre tirée » / « bras tendus ».
- Les trois tutos sont rangés dans des **menus dépliants**.
- Seules restent deux illustrations Krea de gestes (pouce levé, main sur la tête). Les schémas sont générés par `tools/schemas-kite.py`.

## 17 octobre 2026 (12h30) — Tutos kite complets, bateau de 13 m
- **Décoller** en 10 étapes (zone, dérouler les lignes, étaler, gonfler, connecter, s'accrocher, sortir de la zone de puissance, tendre, signal, monter à midi), relu avec des sources d'écoles (kiteinside, FQK, whenwherekite).
- **Atterrir et porter son aile** en 4 étapes (signal main sur la tête, récupération par le bord d'attaque, sécuriser, porter dos au sable face au vent).
- **Water start** en 6 schémas, dont « ne t'agrippe pas à la barre : bras tendus, barre loin ».
- Illustrations Krea (Krea 2 Medium) avec étiquette de vent ; water start en schémas faute de crédits Krea.
- **Seuils bateau recalés pour notre bateau de 13 m** : favorable jusqu'à 17 nd et 1,25 m, prudence jusqu'à 27 nd et 2,5 m.
- Le texte sous « Sessions de kite à venir » parle de kite dès le changement de profil.

## 17 octobre 2026 (12h) — Illustrations Krea du tuto kite
- Les 6 étapes « Décoller son aile » sont illustrées avec Krea (Krea 2 Medium, mêmes personnages et même style), vérifiées une à une : aile en bord de fenêtre au bout des 4 lignes, pré-vol aile au sol, pouce levé, zénith. Étiquette « vent de la mer » sur les vues de plage. Les dessins SVG restent en secours si une image ne charge pas.

## 17 octobre 2026 (11h35) — Carte de sortie neutre
- La carte « Sortie en mer » n'est plus entièrement rouge quand c'est fermé : fond neutre, la couleur ne marque que l'état (Fermé / Ouvert, chrono, barre), pour ne pas la confondre avec la note des conditions de mer.

## 17 octobre 2026 (11h30) — Plages, décollage illustré, assurance, mot de passe
### Ajouté
- **Mot de passe** à l'ouverture de l'app (demandé une fois par appareil). Seule l'empreinte SHA-256 est dans le code : c'est un verrou, pas une protection forte (site statique public).
- Kite : **choix de la plage** (Deauville, Trouville-sur-Mer, Houlgate, Cabourg), avec prévisions et orientation propres à chaque plage.
- Kite : **carrousel illustré en 6 étapes** pour décoller son aile avec un assistant.
- Kite : **mon assurance** (assureur ou licence, n°, téléphone d'assistance, échéance), enregistrée uniquement sur le téléphone, avec alerte d'expiration et bouton d'appel.
### Corrigé
- Le bandeau d'erreur affichait les erreurs de scripts extérieurs (extensions Safari) : il ne s'affiche plus que si l'app elle-même ne démarre pas.

## 17 octobre 2026 (11h15) — Trajet de sortie et correction du 25 octobre
- **25 octobre corrigé** : le PDF officiel donne ce jour-là les horaires des portes à l'heure d'été (une heure trop tard). Correction du Deauville Yacht Club appliquée (`CORRECTIONS` dans `index.html`) et signalée dans le calendrier.
- La carte suit le trajet d'un bateau du bassin des Yachts : 1 · passerelle piétonne (entre bassin des Yachts et bassin Morny), 2 · portes du bassin Morny, puis la mer.

## 17 octobre 2026 (11h) — Correction passerelle piétonne
- Retrait des heures de levée de la passerelle piétonne : elles étaient déduites des horaires des portes du bassin Morny, alors qu'elle se lève aussi portes fermées (observé sur place). Le chrono compte désormais l'ouverture / la fermeture des portes, la passerelle piétonne est indiquée « horaires de levée non publiés · VHF 9 » en attendant une source fiable.

## 17 octobre 2026 (après-midi) — Persona marin, chrono de levée, vrai mode kite

### Corrigé
- La page parlait au piéton : elle parle maintenant au **marin**. Passerelle piétonne et écluse fusionnent en une carte **« Passage du bassin Morny »** (ouvert/fermé aux bateaux), avec un **chrono** jusqu'à la première ou la dernière levée de la passerelle piétonne.
- « Bon / Moyen / Déconseillé » remplacés par des libellés qui disent quoi faire (*Favorable / Prudence / Déconseillé*, *Navigable / Limite / Pas navigable*), avec la raison chiffrée.
- L'app ajoutée à l'écran d'accueil pouvait rester sur une vieille version (cache) : le rechargement automatique contourne maintenant le cache. Un message s'affiche si un script plante.

### Ajouté
- Mode kite 100 % kitesurfeur (ni passerelle piétonne ni écluse, pied de page dédié) : spot en direct (vent, taille d'aile idéale selon le poids du rider, température de l'eau et combinaison, rafales, marée, air, coucher du soleil), prévisions de sessions, section **Bonnes pratiques** (priorités, décollage/atterrissage, sécurité, règles locales).
- Orages pris en compte dans les notes.
- En-tête façon app (icône, nom, heure en direct), onglets adaptés au profil.

## 17 octobre 2026 — Refonte : passerelle, sorties bateau et kite

### Corrigé
- **Passerelle inversée** : la page affichait les horaires des portes Morny (passage des bateaux) comme horaires de la passerelle. Elle indique maintenant la passerelle praticable portes fermées et intermittente portes ouvertes, et l'écluse séparément.
- **Faux « Ouverte » de janvier à juillet** : le PDF officiel oublie l'ouverture de la nuit du 4 au 5 juillet. Le code créait alors une ouverture partant du 1er janvier, ce qui faisait afficher « Ouverte » à chaque fermeture réelle jusqu'au 5 juillet. Cette période s'affiche désormais « Incertain ».
- **Comptes à rebours décalés d'une heure** pendant la nuit des changements d'heure (29 mars, 25 octobre).
- Sur mobile, le compte à rebours et les plages horaires se coupaient sur deux lignes.

### Ajouté
- Prévisions Météo-France (vent, rafales, vagues, houle) et note de confort.
- Profils **Bateau** et **Kitesurf**, mémorisés sur l'appareil.
- Marées (pleine mer, basse mer) en plus des coefficients.
- Bande horaire sur 48 h, liste des créneaux / sessions, meilleur créneau à 3 jours.
- Icône et mode plein écran pour l'écran d'accueil iPhone.
- Rechargement automatique à chaque nouvelle version.
- Barre d'onglets, glisser pour changer de jour, micro-interactions.
- Script d'extraction et de contrôle du PDF (`tools/extraire-horaires.mjs`), documentation.

### Retiré
- Informations sur l'écluse du bassin des Marinas.

## 14 septembre 2026 — Première version
- Horaires 2026 de la porte du bassin Morny et de l'écluse des Marinas, statut en direct et sélecteur de jour.
