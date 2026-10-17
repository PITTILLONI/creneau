# Historique des versions

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
