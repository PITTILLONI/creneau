# Avancement

Site : <https://pittilloni.github.io/deauville-passerelle-ecluse/>
Dernière mise à jour de ce fichier : 17 octobre 2026 (15h30).

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

- [ ] Ajouter le **vent mesuré** (station Météo-France du cap de la Hève ou bouée) : nécessite l'API Météo-France (clé gratuite)
- [ ] Demander une clé API Candhis (gratuite) pour remplacer la lecture de la page publique

- [ ] **Rythme réel des levées de la passerelle piétonne** pendant l'ouverture des portes (à obtenir auprès de la capitainerie ou à relever sur place) pour afficher « prochaine levée dans X min » à chaque cycle
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
