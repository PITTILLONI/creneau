# Logo Crén'eau — « La fenêtre »

Choisi le 23 octobre 2026 parmi trois pistes (`concepts/`, planche `concepts/concepts.png`).

**L'idée :** un C en cadran. L'ouverture, c'est le créneau ; le point vert, c'est vous, dedans. Le point a l'épaisseur de l'anneau et se pose sur sa piste : c'est un morceau du cadran.

## Fichiers (`kit/`)

| Fichier | Usage |
|---|---|
| `creneau-symbole.svg` | Symbole couleur, fond clair |
| `creneau-symbole-sombre.svg` | Symbole couleur, fond sombre |
| `creneau-symbole-noir.svg` / `-blanc.svg` | Une couleur (tampon, gravure, sticker, broderie) |
| `creneau-symbole-petit.svg` | Moins de 48 px : anneau plus épais, point plus gros |
| `creneau-horizontal.svg` (+ `-sombre`, `-noir`, `-blanc`) | Logo avec le nom, en ligne |
| `creneau-empile.svg` | Logo avec le nom, en colonne |
| `creneau-icone-app.svg` | Icône à coins arrondis (favicon `icons/icon.svg`, icônes 192 et 512) |
| `creneau-icone-carre.svg` | Icône à fond plein (iPhone `apple-touch-icon`, Android `maskable`) |

Tout est en tracés, sans texte ni effet. Regénérer : `tools/logo-creneau.py <Geist.ttf> docs/logo/kit` (nécessite `fonttools`).

## Couleurs

| Rôle | Fond clair | Fond sombre |
|---|---|---|
| Anneau | Bleu Crén'eau `#0057ff` | `#5b9dff` |
| Point | Vert créneau `#0a7d45` | `#6fdba0` |
| Nom | Encre `#0a0f1a` | `#f5f7fb` |

Les mêmes valeurs que `--accent`, `--good` et `--ink` dans l'app : le point a la couleur des notes « Favorable ». Sur l'icône, l'anneau est blanc et le point vert clair sur le bleu.

## Typographie

Le nom est dessiné en **Geist Bold** (licence libre OFL, la police de l'app), avec l'apostrophe typographique ’ et un léger resserrement. Dans les textes, on continue d'écrire Crén'eau.

## Règles

- **Marge de protection** : au moins l'épaisseur de l'anneau (15 % de la hauteur du symbole) tout autour.
- **Tailles minimum** : symbole 16 px (version `petit` sous 48 px) ; logo horizontal 96 px de large.
- **À ne pas faire** : déplacer ou recolorer le point en dehors des versions une couleur, tourner l'ouverture, ajouter une ombre ou un dégradé, mettre le symbole couleur sur une photo chargée (utiliser la version blanche), écrire le nom dans une autre police.

## Présentation et tests

- `presentation.html` et `slides/` : planche avec mises en situation (icône, onglet, sticker, t-shirt, enseigne, profil)
- `tests.html` : tailles 16 à 96 px, une couleur, inversé

## Points ouverts

- Recherche d'antériorité de marque (INPI, EUIPO) avant tout dépôt : non faite.
- Animation d'ouverture faite (23 octobre) : le point trace l'anneau (tracé SVG, `stroke-dashoffset`) puis se pose dans le créneau ; code en tête de `index.html` (`#splash`).
