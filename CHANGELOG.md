# Historique des versions

## 18 octobre 2026 (12h) — Les 7 prochains jours
- Calendrier : bouton **« Les 7 prochains jours »** qui ouvre un panneau avec, jour par jour, les créneaux d'écluse notés (couleur Favorable / Prudence / Déconseillé, « nuit ») ou, en kite, les sessions navigables avec l'aile à sortir, la note du jour et sa raison, et un total (« 2 créneaux favorables sur 7 jours »). Toucher un jour l'ouvre dans le calendrier.
- Jours 1 à 3 : prévisions déjà chargées ; jours 4 à 7 : un seul appel groupé (`fetchDays`).

## 18 octobre 2026 (11h45) — Créneaux favorables, pastille des bouées
- Liste des créneaux (et sessions kite) : chaque créneau **Favorable** / session **Navigable** est entouré en vert, **trait plein s'il est aujourd'hui**, **pointillé s'il est un autre jour** (avant : seul le meilleur créneau était entouré).
- Bouées : la pastille « il y a 37 min » dépassait de la carte et son point vert était écrasé sur les petits écrans (classe `live` déjà utilisée par l'horloge) ; elle est maintenant une vraie pastille et le nom de la bouée passe à la ligne. Plus aucun défilement horizontal de la page.

## 18 octobre 2026 (11h30) — Vent consolidé, prévisions kite selon le matériel
- Le recoupement des modèles ne s'affiche plus (« modèles en désaccord » était peu compréhensible) : il sert désormais à **fiabiliser la donnée**. Le vent affiché et noté est la **médiane de 5 modèles** (Météo-France AROME/ARPEGE comptant double, ECMWF, ICON, UKMO, GFS) : une erreur isolée d'un modèle ne fausse plus la note. Direction et écart rafales/vent restent ceux de Météo-France. Partout : spot, prévisions, créneaux bateau, calendrier.
- Onglet Prévisions (kite) : rappel **« Pour 75 kg avec tes ailes 9 et 12 m² : ça navigue de 12 à 27 nd »** avec un bouton Modifier (qui ouvre le réglage sur l'onglet Spot) ; chaque session et chaque heure indique **l'aile à sortir** ; s'il n'y a aucune session, l'app dit ce qui manquerait (« le vent ne dépasse pas 10 nd : il faudrait une 16 m² ou un foil »). Calendrier : l'aile de la meilleure session.

## 18 octobre 2026 (11h) — Accord des modèles et choix de l'aile
- **Vent recoupé entre 5 modèles** : Météo-France (AROME/ARPEGE), européen (ECMWF), allemand (ICON), britannique (UKMO) et américain (GFS). La note reste calculée sur Météo-France, mais chaque prévision indique *Modèles d'accord / Accord moyen / Modèles en désaccord*, avec le vent de chaque modèle. Quand la médiane des modèles changerait la note, l'app l'écrit (« La plupart des modèles prévoient moins de vent (6 nd au lieu de 11) : ce serait « Pas navigable » »). Affiché dans le spot kite, le verdict « Je sors en mer ? », chaque créneau ou session, la bande heure par heure et le calendrier (y compris au-delà de 3 jours, sans Météo-France).
- Kite : réglage **« Mes ailes »** (5 à 17 m², plus Foil), 9 et 12 m² par défaut, gardé sur le téléphone. Le **vent minimum et maximum** sont calculés pour le poids du rider et ses ailes au lieu du seuil fixe de 12 nœuds : une aile de S m² est idéale vers poids × 2,2 ÷ S nœuds et navigue de −12 % à +50 % autour ; plancher 9 nd en twin-tip, 7 nd en foil ; 35 nd au plus.
- L'« Aile à sortir » est choisie **parmi tes ailes** (« ta 12 m² · idéal 11 m² pour 75 kg »), avec un conseil si les rafales demandent la plus petite, ou ce qui manquerait (« trop peu de vent pour ta 12 m² : il faudrait une 13 m² ou un foil »).

## 18 octobre 2026 (10h30) — Indicateur de récupération des données
- Bateau et Kitesurf : quand l'app récupère des données, une **barre animée** court sous l'en-tête, le point de l'horloge passe en bleu et une ligne dit quoi : « Récupération des prévisions météo… », « …des prévisions du spot de Trouville-sur-Mer… », « …des mesures des bouées… », « …des prévisions du 22 octobre… », « …(nouvelle tentative)… ».
- En cas d'échec durable des prévisions : message « Prévisions météo indisponibles (connexion ?) » avec un bouton **Réessayer** ; idem dans la carte du jour du calendrier.
- Les prévisions principales retentent aussi automatiquement quand Open-Meteo est saturé.
- Les bouées ne sont plus chargées en mode Kitesurf (elles n'y sont pas affichées).
- Correctif : à l'ouverture avec `#onglet` dans l'adresse, la page ne défile plus de quelques pixels (haut de l'en-tête coupé).

## 18 octobre 2026 — Bouées au large en direct
- Mode Bateau, onglet Maintenant : **mesures en direct des bouées houlographes** à l'entrée de l'estuaire de la Seine (Candhis, Port du Havre et Cerema), à 12-13 km au nord de Deauville : hauteur des vagues (H1/3), vague max, période, provenance, tendance sur 3 h, courbe des 24 dernières heures, et **comparaison avec la prévision Météo-France** de l'heure (« la mer est plus calme que prévu »).
- Deux bouées : 07609 *Haut du Sud-Ouest* (active) et 07611 *Nord du mouillage* (en maintenance, aucune mesure depuis le 2 juin 2026 : affichée « hors service » tant qu'elle ne transmet pas).
- Relevé toutes les 30 min par GitHub Actions (`tools/bouees.py`, `.github/workflows/bouees.yml`), publié sur la branche `donnees` : Candhis n'accepte pas les appels directs depuis la page.

## 17 octobre 2026 (15h30) — Navigation par onglets, conditions dans le calendrier
- **Un onglet = un écran** : la barre du bas n'est plus un raccourci vers une longue page, chaque onglet (Maintenant, Sortir, Conseils, Calendrier) affiche uniquement sa section. L'onglet ouvert est gardé dans l'adresse (`#sortir`…), chaque onglet retrouve sa position, toucher l'onglet déjà ouvert remonte en haut. Le pied de page (sources, liens) n'apparaît plus que sur Maintenant (et l'avertissement sur Calendrier).
- Onglet Sortir allégé : les **allures et réglages par destination** sont dans un menu dépliant sous la voilure conseillée.
- **Calendrier : conditions du jour choisi** (bateau et kite) : note de chaque créneau d'écluse directement sous son horaire, meilleur créneau (ou meilleure session kite) avec sa raison chiffrée, vent, mer, soleil (+ aile et eau en kite), bande heure par heure du jour. Les 3 premiers jours reprennent les prévisions Météo-France ; au-delà, tendance des modèles mondiaux jusqu'à J+15 (vagues jusqu'à J+7 environ, sinon note sur le vent seul) ; jours passés : archives Météo-France. Au-delà de J+15, la page indique à partir de quand la prévision arrivera.
- Si Open-Meteo est saturé (« service is overloaded »), le calendrier essaie automatiquement un autre modèle.
- L'onglet s'appelle « Calendrier » dans les deux profils.

## 17 octobre 2026 (13h30) — Tutos kite illustrés et annotés
- Retour au **style illustré**, rendu précis : 20 illustrations (Krea Nano Banana Pro et Krea 2) vérifiées une à une, avec des **annotations exactes superposées** : flèche de vent (ou « vent dans le dos »), bord d'attaque en orange, positions de l'aile (9 h / 12 h / 3 h) en vert, erreurs en rouge.
- Étapes au sol vues de côté (mer à gauche, vent de gauche à droite), aile en l'air vue de derrière le rider.
- Nouvelles illustrations : étaler, gonfler, connecter (dos vers le ciel, bord d'attaque face au vent), sécuriser, porter son aile, et les 6 étapes du water start.
- Scripts : `tools/krea-generer.py` (génération via l'API Krea, jeton lu dans `~/.config/krea/token`, jamais dans le dépôt) et `tools/annotations-kite.py` (annotations et carrousels).

## 17 octobre 2026 (13h05) — Conseils bateau, menus homogènes
- Mode Bateau : onglet **Conseils** avec sortir du bassin Morny (VHF 9, passerelle piétonne, portes), check-list avant de partir (dont l'heure de fermeture des portes pour rentrer), prendre un ris, réglages par allure, priorités en mer, homme à la mer et urgences.
- Tous les menus dépliants (tutos, priorités, sécurité, règles locales, calcul des notes) ont le même style.
- Prévisions : nouvelle tentative automatique après un raté réseau.

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
