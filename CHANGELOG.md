# Historique des versions

## 17 octobre 2026 (après-midi) — Persona marin, chrono de levée, vrai mode kite

### Corrigé
- La page parlait au piéton : elle parle maintenant au **marin**. Passerelle piétonne et écluse fusionnent en une carte **« Passage du bassin Morny »** (ouvert/fermé aux bateaux), avec un **chrono** jusqu'à la première ou la dernière levée de la passerelle piétonne.
- « Bon / Moyen / Déconseillé » remplacés par des libellés qui disent quoi faire (*Favorable / Prudence / Déconseillé*, *Navigable / Limite / Pas navigable*), avec la raison chiffrée.
- L'app ajoutée à l'écran d'accueil pouvait rester sur une vieille version (cache) : le rechargement automatique contourne maintenant le cache. Un message s'affiche si un script plante.

### Ajouté
- Mode kite dédié, sans l'écluse : spot en direct (vent, taille d'aile idéale selon le poids du rider, température de l'eau et combinaison, rafales, marée, air, coucher du soleil), prévisions de sessions, section **Bonnes pratiques** (priorités, décollage/atterrissage, sécurité, règles locales).
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
