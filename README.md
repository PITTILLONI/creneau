# Passerelle & écluse — Deauville-Trouville

**➜ En ligne : <https://pittilloni.github.io/deauville-passerelle-ecluse/>**

Savoir en un coup d'œil, depuis son téléphone :

1. si la **passerelle piétonne** du bassin Morny est praticable et si l'**écluse (portes Morny)** est ouverte aux bateaux, avec le compte à rebours jusqu'au prochain changement ;
2. si c'est le bon moment pour **sortir en mer**, avec deux profils :
   - **Bateau** : note de confort de chaque créneau d'écluse (vent, rafales, vagues, houle, nuit) ;
   - **Kitesurf** : note heure par heure sur la plage de Deauville (force et régularité du vent, orientation par rapport à la plage, mer, jour) et meilleures sessions à venir ;
3. les horaires des portes et les marées (pleine mer, basse mer, coefficients) de **n'importe quel jour de 2026**.

> ⚠️ Horaires **théoriques**. Toujours confirmer avant une manœuvre via le **VHF canal 9** ou la cabine de l'écluse (06 98 71 83 92).

## L'installer sur l'iPhone

Ouvrir le lien dans Safari → bouton Partager → **« Sur l'écran d'accueil »**. L'app s'ouvre en plein écran avec sa propre icône, et se met à jour toute seule (voir [Publier une mise à jour](#publier-une-mise-à-jour)).

## Avancement

Voir [ROADMAP.md](ROADMAP.md) pour ce qui est fait et ce qui reste à faire, et [CHANGELOG.md](CHANGELOG.md) pour l'historique des versions.

## Sources des données

| Donnée | Source | Comment |
| --- | --- | --- |
| Horaires des portes Morny, marées, coefficients | PDF officiel *« Port de Deauville-Trouville — Horaires de manœuvres 2026 »*, **Ports du Calvados** avec le **SHOM** (autorisation n° 2024-282) — [lien](https://www.portsducalvados.fr/wp-content/uploads/2023/08/06-DEAUVILLE-TROUVILLE-Horaires-de-manoeuvres-2026.pdf) | Extrait par `tools/extraire-horaires.mjs`, embarqué dans la page |
| Vent (force, rafales, direction) | **Météo-France**, modèles AROME / ARPEGE | API [Open-Meteo](https://open-meteo.com/) en direct, sans clé |
| Vagues et houle | **Météo-France**, modèle de vagues MFWAM | API marine [Open-Meteo](https://open-meteo.com/en/docs/marine-weather-api) |
| Lever / coucher du soleil | Open-Meteo | idem |

Liens de vérification affichés sur la page : [bulletin météo marine Météo-France](https://meteofrance.com/meteo-marine), [marées SHOM de Deauville](https://maree.shom.fr/harbor/DEAUVILLE).

### Ce qu'il faut savoir sur les données

- Les horaires du PDF sont ceux des **portes du bassin Morny** (passage des bateaux, porte à la cote 5,50 m). Pendant ces plages, la **passerelle piétonne se lève et se baisse régulièrement** pour laisser passer les bateaux : le passage à pied est **intermittent**. Portes fermées, la passerelle est praticable en continu. Aucun document public ne donne le rythme exact des levées.
- Le PDF 2026 contient un **oubli** : l'ouverture des portes de la nuit du **4 au 5 juillet** n'y figure pas (seule la fermeture du 5 à 05h32 est indiquée). La page affiche « Incertain » sur cette période. Le script d'extraction détecte ce genre d'erreur automatiquement.
- Les comptes à rebours tiennent compte des **changements d'heure** (29 mars, 25 octobre).
- Les données ne couvrent que **2026**. Il faudra relancer l'extraction quand Ports du Calvados publiera le PDF 2027.

### Notes de confort

Les seuils sont expliqués sur la page (« Comment est calculé… ») et réglés dans `index.html` (`scoreBoat`, `scoreKite`, `BEACH_ONSHORE`) :

- **Bateau** (plaisance 5–8 m) : bon jusqu'à 12 nœuds et 0,6 m de vagues, moyen jusqu'à 18 nœuds et 1,2 m, déconseillé au-delà ou avec des rafales de plus de 25 nœuds ; jamais mieux que « moyen » de nuit. Un créneau d'écluse prend la note de sa pire heure.
- **Kitesurf** (plage de Deauville, orientée NNO) : idéal 14–25 nœuds ; rafaleux si l'écart rafales/vent moyen dépasse 8 nœuds ; side-on / side-shore = bon, onshore = moyen, side-off = déconseillé, **offshore = dangereux** ; pas de session de nuit.

## Structure du dépôt

```
index.html              la page (HTML + CSS + JS, aucune dépendance à installer)
manifest.webmanifest    nom et icônes pour l'écran d'accueil
icons/                  icône (SVG source + PNG 180/192/512)
version.json            numéro de version en ligne, lu par la page pour se recharger
tools/
  extraire-horaires.mjs extraction du PDF officiel -> données JSON + contrôle des incohérences
  publier-version.sh    nouveau numéro de version avant chaque publication
docs/
  DESIGN.md             choix de design et d'ergonomie
```

## Mettre à jour les horaires (ex. PDF 2027)

Prérequis : Node 18+ et `pdftotext` (`brew install poppler`).

```sh
curl -L -o horaires.pdf "<lien du PDF Ports du Calvados>"
pdftotext -layout horaires.pdf horaires.txt
node tools/extraire-horaires.mjs horaires.txt > data.json   # les anomalies s'affichent dans le terminal
```

Remplacer ensuite le contenu de `const DATA = …;` dans `index.html` par celui de `data.json`, adapter l'année (`2026`) dans le code, et reporter les anomalies détectées dans `ANOMALIES`.

## Publier une mise à jour

```sh
sh tools/publier-version.sh   # nouveau numéro dans index.html et version.json
git commit -am "…" && git push
```

GitHub Pages republie `main` en une minute environ. Les pages déjà ouvertes, y compris l'app sur l'écran d'accueil, vérifient `version.json` toutes les 5 minutes et quand on revient dessus, puis se rechargent seules.

## Avertissement

Projet indépendant, non affilié à Ports du Calvados, à la mairie de Deauville, au SHOM ni à Météo-France. Les prévisions ne remplacent pas le bulletin météo marine officiel.
