# Design et ergonomie

Méthode : skill `design-combo`. UI UX Pro Max fixe le plancher (accessibilité, tactile, lisibilité) et Taste fixe le plafond (décisions visuelles, pas de rendu générique). La page est classée **hybride** : un outil public consulté en quelques secondes, souvent dehors, au soleil, d'une main.

## Principes

- **La réponse avant tout.** Le premier écran donne l'état de la passerelle et de l'écluse en très grand (environ 50 px) et le temps restant avant le prochain changement. Tout le reste est en dessous.
- **La couleur porte le sens, le mot le confirme.** Vert = praticable / bon, rouge = fermé / déconseillé, ambre = intermittent / moyen / incertain. Le mot est toujours écrit, la couleur n'est jamais le seul signal.
- **Une seule police** (Geist) et des chiffres à largeur fixe (`tabular-nums`) pour que les heures ne bougent pas.
- **Plat** : pas d'ombres ni de bordures. Les surfaces se distinguent par un léger écart de ton.
- **Tactile** : toutes les cibles font au moins 44 px, la barre d'onglets est en bas (zone du pouce) et respecte les zones sûres de l'iPhone (`safe-area-inset`).
- **Clair et sombre** suivent le réglage du téléphone.

## Navigation

Une seule page avec trois sections et une barre d'onglets fixe en bas : **Maintenant**, **Sortir** et **Calendrier**. L'onglet actif suit le défilement. Le sélecteur **Bateau / Kitesurf** est en haut et mémorisé sur l'appareil.

## Mouvement

Seulement là où il a un sens : l'état qui change se réanime, l'indicateur d'onglet et de profil glisse, les créneaux apparaissent en cascade, le compte à rebours pulse à moins de 15 minutes, et un appui renvoie un léger retour visuel. Tout est coupé quand « Réduire les animations » est activé.

## Écarts assumés aux règles Taste

L'inspecteur Taste est pensé pour les sites vitrines. Pour cet outil, on accepte :

- pas de photographies ni de vidéo (`few-pictures`, `no-footage`) : rien ne doit gêner la lecture de l'état ;
- une bande horaire qui défile horizontalement (`side-scroll`) : 48 heures ne tiennent pas sur un écran de téléphone ;
- de petits libellés au-dessus des états (« Passerelle piétonne », « Écluse ») : ils disent de quoi parle le grand mot ;
- un filet au-dessus de la barre d'onglets, pour la séparer du contenu qui défile dessous.
