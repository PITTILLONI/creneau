# Passerelle & écluse — Deauville-Trouville

**➜ En ligne : <https://pittilloni.github.io/deauville-passerelle-ecluse/>**

Savoir en un coup d'œil, depuis son téléphone :

L'app est pensée pour un **marin** (profil Bateau) ou un **kitesurfeur** (profil Kitesurf).

**Bateau**
1. **Passage du bassin Morny** : ouvert ou fermé aux bateaux, avec un chrono jusqu'à la première (ou la dernière) levée de la passerelle piétonne, l'état des portes et de la passerelle piétonne, et la frise de la journée ;
2. **Je sors en mer ?** : chaque créneau d'écluse noté *Favorable / Prudence / Déconseillé* avec la raison chiffrée (« Trop de vent : 19 nd, rafales 26 nd », « Mer agitée : vagues de 1,1 m »…) ;
3. horaires des portes et marées de **n'importe quel jour de 2026**.

**Kitesurf**
1. **Spot en direct** : vent (force, direction, orientation par rapport à la plage), **taille d'aile idéale** selon le **poids du rider** (réglable), **température de l'eau** et combinaison conseillée, rafales et régularité, marée montante/descendante, air, coucher du soleil ;
2. **Prévisions** : sessions *Navigable / Limite / Pas navigable* sur 3 jours, heure par heure ;
3. **Conseils** : priorités sur l'eau, décoller et poser l'aile, sécurité, règles locales ;
4. marées de n'importe quel jour.

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

- Les horaires du PDF sont ceux des **portes du bassin Morny** (porte à la cote 5,50 m). Ce sont des **portes à flot**, pas une écluse à sas (l'écluse du port est celle du bassin des Marinas). La **passerelle piétonne** ne suit pas ces horaires : elle se lève aussi portes fermées (observé sur place) et aucun document public ne donne ses heures de levée. La page l'indique donc « horaires de levée non publiés · VHF canal 9 » en attendant une source fiable.
- **Géographie** : bassin des Yachts → passerelle piétonne basculante (presqu'île de la Touques) → bassin Morny → portes du bassin Morny → avant-port. Les deux bassins sont à flot : la passerelle piétonne peut se lever portes fermées.
- Le PDF 2026 donne le **25 octobre** à l'heure d'été (une heure trop tard) : correction du [Deauville Yacht Club](https://www.deauvilleyachtclub.org/ouvertures-des-portes/) appliquée via `CORRECTIONS` dans `index.html`.
- Le PDF 2026 contient un **oubli** : l'ouverture des portes de la nuit du **4 au 5 juillet** n'y figure pas (seule la fermeture du 5 à 05h32 est indiquée). La page affiche « Incertain » sur cette période. Le script d'extraction détecte ce genre d'erreur automatiquement.
- Les comptes à rebours tiennent compte des **changements d'heure** (29 mars, 25 octobre).
- Les données ne couvrent que **2026**. Il faudra relancer l'extraction quand Ports du Calvados publiera le PDF 2027.

### Notes de confort

Les seuils sont expliqués sur la page (« Comment est calculé… ») et réglés dans `index.html` (`scoreBoat`, `scoreKite`, `BEACH_ONSHORE`) :

- **Bateau** (plaisance 5–8 m) : bon jusqu'à 12 nœuds et 0,6 m de vagues, moyen jusqu'à 18 nœuds et 1,2 m, déconseillé au-delà ou avec des rafales de plus de 25 nœuds ; jamais mieux que « moyen » de nuit. Un créneau d'écluse prend la note de sa pire heure.
- **Kitesurf** (plage de Deauville, orientée NNO) : idéal 14–25 nœuds ; rafaleux si l'écart rafales/vent moyen dépasse 8 nœuds ; side-on / side-shore = bon, onshore = moyen, side-off = déconseillé, **offshore = dangereux** ; orage ou nuit = pas de session.
- **Taille d'aile** indicative (twin-tip) : poids du rider (kg) × 2,2 / vent (nœuds), entre 5 et 17 m² ; en dessous de 12 nœuds, foil. **Combinaison** selon la température de l'eau (modèle de courants Météo-France).

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

GitHub Pages republie `main` en une minute environ. La page vérifie `version.json` à l'ouverture, au retour sur l'app et toutes les 5 minutes. Si la version a changé, elle se recharge avec une adresse neuve (`?v=…`), ce qui contourne le cache de GitHub Pages et celui de l'app écran d'accueil.

> Une icône ajoutée à l'écran d'accueil **avant le 17 octobre 2026 (11h)** n'a pas ce mécanisme : il faut la supprimer et la rajouter une fois.

## Avertissement

Projet indépendant, non affilié à Ports du Calvados, à la mairie de Deauville, au SHOM ni à Météo-France. Les prévisions ne remplacent pas le bulletin météo marine officiel.
