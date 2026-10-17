# Avancement

Site : <https://pittilloni.github.io/deauville-passerelle-ecluse/>
Dernière mise à jour de ce fichier : 17 octobre 2026.

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
- [x] Kite : choix de la plage (Deauville, Trouville, Houlgate, Cabourg), carrousel de décollage, assurance

## À faire / idées

- [ ] **Rythme réel des levées de la passerelle piétonne** pendant l'ouverture des portes (à obtenir auprès de la capitainerie ou à relever sur place) pour afficher « prochaine levée dans X min » à chaque cycle
- [ ] Vérifier l'**orientation de chaque plage** (Trouville, Houlgate, Cabourg) sur le terrain
- [ ] Remplacer les illustrations SVG du carrousel par des visuels Krea si souhaité
- [ ] Vérifier les **seuils kite** sur le terrain (taille d'aile, niveau) et les rendre réglables dans la page
- [ ] Rappeler les **zones et périodes de kite** autorisées par la mairie en saison
- [ ] Vérifier les seuils bateau selon la taille et le type de bateau
- [ ] Horaires **2027** dès la publication du PDF par Ports du Calvados
- [ ] Mode hors ligne (service worker) pour consulter les horaires sans réseau sur le ponton
- [x] Correction du 25 octobre (heure d'été dans le PDF) d'après le Deauville Yacht Club
- [ ] Vérifier si le 29 mars a le même défaut (non signalé)
- [ ] Signaler à Ports du Calvados l'oubli du 4-5 juillet dans le PDF 2026
