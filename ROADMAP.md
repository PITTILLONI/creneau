# Avancement

Site : <https://pittilloni.github.io/creneau/>
Dernière mise à jour de ce fichier : 18 octobre 2026 (18h35).

## Fait

- [x] Horaires 2026 des portes Morny extraits du PDF officiel et vérifiés jour par jour (365 jours, 100 % conformes)
- [x] Statut en direct passerelle piétonne + écluse, avec compte à rebours
- [x] Passerelle modélisée correctement : praticable portes fermées, **intermittente** portes ouvertes
- [x] Oubli du PDF (nuit du 4 au 5 juillet) détecté et signalé au lieu d'afficher un faux « Ouverte »
- [x] Comptes à rebours justes aux changements d'heure
- [x] Marées : pleine mer, basse mer, coefficients (SHOM)
- [x] Prévisions Météo-France (vent, rafales, vagues, houle) via Open-Meteo
- [x] Profil **Bateau** : note de confort par créneau d'écluse + meilleur créneau à 3 jours
- [x] Profil **Kitesurf** : note par heure, orientation par rapport à la plage, sessions à venir
- [x] Bande heure par heure sur 48 h
- [x] Consultation de n'importe quel jour de 2026 (boutons, calendrier, glisser gauche/droite)
- [x] Calendrier : conditions météo du jour choisi (note des créneaux, meilleur créneau/session, heure par heure), jusqu'à J+15 et jours passés
- [x] Navigation par vrais onglets (une section à l'écran à la fois)
- [x] Bateau : bouées houlographes du Havre en direct (Candhis), comparées à la prévision
- [x] Indicateur « récupération des données en cours » (bateau et kite), avec Réessayer en cas d'échec
- [x] Vent consolidé : médiane de 5 modèles (Météo-France compte double, ECMWF, ICON, UKMO, GFS)
- [x] Kite : « Mes ailes » + foil, vent mini/maxi et aile conseillée selon le poids et les ailes du rider
- [x] Calendrier : carrousel des 7 prochains jours (créneaux favorables / sessions navigables)
- [x] Icônes sur les intitulés et les raisons des notes ; réglages kite (poids, ailes) dans l'en-tête
- [x] Région Nouméa (bateau et kite) : fuseau, spots, marées calculées, lagon noté sur le vent seul
- [x] « Ajouter votre spot / port » : e-mail prérempli
- [x] Profil Glisse : kite, windsurf, windfoil, wingfoil (matériel et plages de vent par sport)
- [x] Interface mobile d'abord : barre d'onglets, grandes zones tactiles, mode sombre automatique
- [x] Icône et mode plein écran pour l'écran d'accueil iPhone
- [x] Rechargement automatique quand une nouvelle version est publiée
- [x] Micro-interactions (transitions d'état, indicateur d'onglet, apparition des créneaux), désactivées si « Réduire les animations »
- [x] Retrait des informations du bassin des Marinas
- [x] Persona marin : carte « Passage du bassin Morny » avec chrono de levée de la passerelle piétonne
- [x] Notes explicites avec leur raison (Favorable / Prudence / Déconseillé…)
- [x] Mode kite dédié : spot en direct, taille d'aile selon le poids, température de l'eau, conseils de bonnes pratiques
- [x] En-tête façon app, rechargement automatique sans cache
- [x] Mot de passe à l'ouverture
- [x] Kite : choix de la plage (Deauville, Trouville, Houlgate, Cabourg), assurance
- [x] Correction du 25 octobre (heure d'été dans le PDF) d'après le Deauville Yacht Club
- [x] Bateau : seuils de confort pour notre bateau de 13 m, voilure conseillée (ris, génois) et allures/réglages vers Le Havre, Honfleur, Dives, Ouistreham, le large
- [x] Bateau : onglet Conseils (sortir du bassin Morny, check-list, prendre un ris, réglages par allure, priorités, homme à la mer)
- [x] Kite : tutos illustrés et annotés en menus dépliants — décoller (10 étapes), atterrir et porter son aile (4), water start (6, « ne t'agrippe pas à la barre »)
- [x] En-tête : sélecteur Bateau / Kitesurf en haut, port ou spot en dessous ; menus dépliants homogènes

## À faire / idées

- [ ] **19 octobre** : relever les feux vert / rouge de la passerelle piétonne (prévu par l'app : 15:44–15:59, 16:29–16:44, 17:14–17:29, 17:59–18:14, 18:44–18:59) et la durée de la manœuvre, pour confirmer le décalage de 12 min et afficher « en cours de levée / descente »

- [ ] **Journal de sortie** : noter une sortie en un geste (date, spot ou destination, aile / voilure, ressenti), avec les conditions prévues enregistrées automatiquement ; sert de carnet personnel et, à terme, à affiner les notes (et argument Premium)
- [ ] **Proposer une sortie en un clic** sur un créneau favorable : partager le créneau (date, heure, spot, note, conditions) par message à l'équipage ou aux potes de ride, avec ajout au calendrier ; plus tard, inscriptions via les clubs et écoles

- [ ] **« J'y serai » + chat du créneau** : je touche un créneau → « J'y serai » → un chat simple s'ouvre en bottom sheet avec les autres personnes qui ont dit venir sur ce créneau (même spot ou même sortie de port, même plage horaire). Compteur « 3 personnes y seront » sur la carte du créneau. Prévoir :
  - un serveur temps réel (Firebase ou Supabase, offre gratuite au départ) : GitHub Pages ne suffit plus ;
  - identité = prénom + nom déjà donnés à l'inscription bêta ;
  - modération (signaler, supprimer un message), messages effacés après le créneau, mention RGPD dans la présentation ;
  - notification « quelqu'un vient aussi » (push web, installée sur l'écran d'accueil) ;
  - lien naturel avec le journal de sortie et, côté clubs et écoles, les inscriptions encadrées.

- [ ] **Groupes 100 % femmes** pour « J'y serai » et le chat du créneau : option « entre femmes » sur un créneau, visible et rejoignable seulement par les participantes qui l'ont choisie (sécurité, confiance, débutantes). À cadrer : déclaratif ou validé (par un club, une école, une invitation), modération renforcée, et vérifier le cadre légal (non-discrimination pour un service payant) avant de l'ouvrir

- [ ] **Niveau du pratiquant** avec une jauge (débutant → confirmé), dans les réglages de la pastille : seuils de vent et de mer plus prudents pour un débutant, plus larges pour un confirmé (glisse, et éventuellement bateau)

- [ ] SIMBAD (HAROPA) : vent et houle mesurés dans le chenal de Port 2000, à intégrer seulement après autorisation écrite d'HAROPA (CGU art. 6 et 8)

- [x] Google Form du questionnaire branché
- [x] Présentation au premier lancement (prénom/nom du testeur, profil, région, lecture des notes, avertissement bêta)
- [x] Proposition d'installation sur l'écran d'accueil à la 2e ouverture (iPhone, Android)
- [ ] Diffuser le questionnaire aux clubs et écoles (Deauville, Nouméa) ; option : une colonne par rubrique dans le Sheet
- [ ] Version payante : prix Open-Meteo (usage commercial), accord Ports du Calvados et SHOM, puis comptes + paiement + alertes (chiffrage gardé hors du dépôt public)

- [ ] Faire valider par des pratiquants les coefficients et vents mini/maxi du windsurf, du windfoil et du wingfoil (`SPORTS`)

- [ ] Nouméa : faire confirmer par la famille l'orientation de l'îlot Maître (110°) et de Port Moselle (265°), les zones autorisées à Magenta (aérodrome), les caps du lagon et les heures de marée calculées (comparer à l'annuaire SHOM)

- [ ] Ajouter le **vent mesuré** (station Météo-France du cap de la Hève ou bouée) : nécessite l'API Météo-France (clé gratuite)
- [ ] Demander une clé API Candhis (gratuite) pour remplacer la lecture de la page publique

- [x] Cycle de la passerelle piétonne : 15 min levée / 30 min baissée pendant l'ouverture des portes, « prochaine levée dans X min »
- [x] Calage de la passerelle piétonne confirmé le 18 octobre (descente 17:56, levée 18:26 comme prévu)
- [ ] Revérifier le calage un jour où les portes ouvrent à une autre heure (le décalage de 12 min est-il fixe ?)
- [ ] Vérifier l'**orientation de chaque plage** (Trouville, Houlgate, Cabourg) sur le terrain
- [ ] Vérifier les **seuils kite** sur le terrain (plage −12 % / +50 % autour du vent idéal de chaque aile, planchers 9 nd twin-tip / 7 nd foil)
- [ ] Rappeler les **zones et périodes de kite** autorisées par la mairie en saison
- [ ] Confirmer le gréement du bateau (sloop ? nombre de ris, trinquette, gennaker) pour affiner la voilure conseillée
- [ ] Vérifier les caps des destinations et en ajouter (Cherbourg, Fécamp…) si utile
- [ ] Révoquer le jeton Krea « Deauville tuto kite (Claude Code) » une fois les illustrations terminées
- [ ] Horaires **2027** dès la publication du PDF par Ports du Calvados
- [ ] Mode hors ligne (service worker) pour consulter les horaires sans réseau sur le ponton
- [ ] Vérifier si le 29 mars a le même défaut (non signalé)
- [ ] Signaler à Ports du Calvados l'oubli du 4-5 juillet dans le PDF 2026
