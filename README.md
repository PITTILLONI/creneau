# Crén'eau — le bon créneau pour glisser

**➜ En ligne : <https://pittilloni.github.io/creneau/>**

Bateau ou kitesurf à Deauville et sur la Côte Fleurie, et à **Nouméa** : savoir quand sortir (portes du bassin Morny, vent, vagues, marées, bouées, spots de kite). Anciennement « Port de Deauville » (dépôt `deauville-passerelle-ecluse`, l'ancienne adresse redirige ici).

Savoir en un coup d'œil, depuis son téléphone :

L'app est pensée pour un **marin** (profil Bateau) ou un **pratiquant de glisse** (profil Glisse : kite, windsurf, windfoil ou wingfoil, choisi dans l'en-tête avec le poids et le matériel). Chaque onglet de la barre du bas (Maintenant, Prévisions, Conseils, Calendrier, les mêmes dans les deux profils) est un écran à part. Les notes disent partout *Favorable / Prudence / Déconseillé*.

**Bateau**
1. **Sortie en mer (bassins Morny et des Yachts)** : ouvert ou fermé aux bateaux, chrono jusqu'à l'ouverture ou la fermeture des portes, état de la passerelle piétonne (cycle 15 min levée / 30 min baissée pendant l’ouverture des portes, levées à heure fixe hh:26 / hh:11 / hh:56, prochaine levée, VHF 9) et des portes, frise de la journée ;
2. **Voilure et allures** : voilure conseillée selon le vent et les rafales (ris, génois roulé), allure et réglages vers Le Havre, Honfleur, Dives, Ouistreham ou le large ;
3. **Je sors en mer ?** : chaque créneau d'écluse noté *Favorable / Prudence / Déconseillé* avec la raison chiffrée (« Trop de vent : 19 nd, rafales 26 nd », « Mer agitée : vagues de 1,1 m »…) ;
4. **Conseils** : sortir du bassin Morny, check-list avant de partir, prendre un ris, réglages par allure, priorités en mer, homme à la mer ;
5. **Bouées au large en direct** : vagues mesurées par les houlographes Candhis à l'entrée de l'estuaire (12-13 km au nord), comparées à la prévision ;
6. **Calendrier** : horaires des portes et marées de **n'importe quel jour de 2026**, avec les **conditions prévues** ce jour-là (note de chaque créneau, meilleur créneau et sa raison, heure par heure) jusqu'à J+15, et les conditions passées.

**Kitesurf**
1. **Spot en direct** : vent (force, direction, orientation par rapport à la plage), **taille d'aile idéale** selon le **poids du rider** (réglable), **température de l'eau** et combinaison conseillée, rafales et régularité, marée montante/descendante, air, coucher du soleil ;
2. **Choix de la plage** : Deauville, Trouville-sur-Mer, Houlgate, Cabourg (position et orientation propres à chaque plage, à affiner sur le terrain : `SPOTS` dans `index.html`) ;
3. **Prévisions** : sessions *Favorable / Prudence / Déconseillé* sur 3 jours, heure par heure (rafales de 35 nd ou plus, ou plus de 12 nd d'écart avec le vent moyen : Déconseillé) ;
4. **Conseils** : trois carrousels illustrés (décoller son aile en 10 étapes, atterrir et porter son aile, réussir son water start sans s'agripper à la barre), **mon assurance** (stockée seulement sur le téléphone), priorités sur l'eau, sécurité, règles locales ;
5. **Calendrier** : marées de n'importe quel jour, avec les conditions prévues (meilleure session, aile, eau, heure par heure) jusqu'à J+15.

> ⚠️ Horaires **théoriques**. Toujours confirmer avant une manœuvre via le **VHF canal 9** ou la cabine de l'écluse (06 98 71 83 92).

## Régions

| | Deauville (Côte Fleurie) | Nouméa |
| --- | --- | --- |
| Fuseau | Europe/Paris | Pacific/Noumea |
| Bateau | portes du bassin Morny (PDF officiel), passerelle piétonne, bouées Candhis | Port Moselle, pas d'écluse : « sorties possibles » sur les heures de jour |
| Glisse | Deauville, Trouville, Houlgate, Cabourg | Anse Vata (243°), Méridien (279°), Aquarêve (198°), Magenta (95°), Îlot Maître (110°, à confirmer), Port Moselle (265°, à confirmer) |
| Vagues | Météo-France MFWAM | ignorées (le modèle ne voit pas la barrière de corail) : note sur le vent seul |
| Marées | PDF Ports du Calvados / SHOM, avec coefficients | calculées sur la hauteur d'eau prévue (Open-Meteo), sans coefficient |
| Urgence | 196 (CROSS), VHF 16 | 16 (COSS NC), VHF 16 ; météo VHF 65/66 |

**Une seule zone par téléphone** : déduite du fuseau horaire (`ZONES`). Un téléphone réglé sur Nouméa ne voit que Nouméa, les autres que Deauville ; aucune localisation n'est demandée. Pour forcer : ouvrir le lien avec `?zone=nc`, `?zone=dv`, ou `?zone=toutes` pour voir les deux (réglage gardé sur le téléphone).

**Clubs** : bouton « Rejoindre un club » de l'onglet Conseils (code = clé de `CLUBS`), ou lien d'invitation `?club=<id>` (gardé sur le téléphone, `?club=aucun` pour le retirer). Sur iPhone, le lien n'atteint pas l'app de l'écran d'accueil (stockage séparé de Safari) : passer par le bouton. Chaque club de `CLUBS` a une zone, des supports avec une consigne par niveau (`max:{deb:[vent, rafales, vagues], conf:[…]}` : au-delà, la note bateau plafonne à « Déconseillé », à 3 nd près à « Prudence » ; voilure conseillée seulement pour un `keel`, habitable), choisis via la pastille de l'en-tête (`support`, `niveau`). Le club a aussi un sigle et une couleur (`short`, `color`) pour le bandeau de l'en-tête, qui ouvre la fiche club (licence FFVoile, `licence` : numéro et année). Démo des cours : `cours` du club (semaine type), carte « Cours du club » dans l'onglet Calendrier, rappel « Votre prochain cours » dans Maintenant, inscriptions locales (`inscriptions`) et un contact prérempli dans la fiche de sortie. Seul l'exemple fictif `ycp` (Yacht Club des Planches, alias `demo`) existe : un vrai club n'est ajouté qu'avec son accord. Champs facultatifs : `burgee` (couleurs du guidon), `info` (lieu, accueil, mail, VHF), `actus`.

**Fiche de sortie** (« Je pars en mer », mode bateau) : envoyée par SMS ou partage, sortie en cours gardée sur le téléphone (`sortie`, préférences `sortiePrefs`) jusqu'à « Je suis rentré ». Pas de serveur : aucune alerte automatique si le retour n'est pas signalé.

Tout est dans `REGIONS`, `SPOTS` et `DESTS` (`index.html`). Le bouton « Ajouter votre spot / port » des listes ouvre un e-mail prérempli (`requestPlace`).

## Accès

L'app demande un **mot de passe** à la première ouverture sur chaque appareil (à demander au propriétaire du projet). Le code ne contient que son empreinte SHA-256 (`PASS_HASH` dans `index.html`). Pour le changer : `printf '%s' 'nouveau-mot-de-passe' | shasum -a 256`, puis remplacer `PASS_HASH`. Attention : c'est un verrou d'interface, pas une vraie sécurité, le dépôt et les données restent publics.

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
| Vent consolidé | Météo-France (compte double), ECMWF, ICON (DWD), UKMO (Met Office), GFS (NOAA) | Open-Meteo, un seul appel `models=…` ; médiane par heure (`attachModels` dans `index.html`) |
| Vagues mesurées (bouées 07609 et 07611) | **Candhis** — Port du Havre et Cerema, Licence Ouverte Etalab — [candhis.cerema.fr](https://candhis.cerema.fr/) | Page publique relevée toutes les 30 min par GitHub Actions (`tools/bouees.py`), publiée sur la branche `donnees` (`bouees.json`) |

Liens de vérification affichés sur la page : [bulletin météo marine Météo-France](https://meteofrance.com/meteo-marine), [marées SHOM de Deauville](https://maree.shom.fr/harbor/DEAUVILLE).

### Ce qu'il faut savoir sur les données

- Les horaires du PDF sont ceux des **portes du bassin Morny** (porte à la cote 5,50 m). Ce sont des **portes à flot**, pas une écluse à sas (l'écluse du port est celle du bassin des Marinas). La **passerelle piétonne** : pendant l'ouverture des portes elle alterne **15 min levée / 30 min baissée** (information locale, octobre 2026 ; calé sur les relevés des 18 et 25 octobre : horaire fixe à l'heure de Paris, levées à hh:26, hh:11, hh:56, quelle que soit l'heure d'ouverture des portes ; à confirmer sur d'autres jours). Elle peut aussi se lever portes fermées (observé sur place ; le 25 octobre, portes fermées à 12:54 : levée vers 12:59 et restée levée en continu jusqu'à 13:32, hors cycle de 15 min). Seule indication officielle connue : un panneau dans le bassin annonce aux bateaux **15 min d'attente** (relevé par l'utilisateur le 25 octobre 2026), ce qui ne colle pas avec les 30 min baissée observées le 18 octobre (levée à la demande ?). Confirmer au VHF canal 9.
- **Géographie** : bassin des Yachts → passerelle piétonne basculante (presqu'île de la Touques) → bassin Morny → portes du bassin Morny → avant-port. Les deux bassins sont à flot : la passerelle piétonne se lève surtout pendant l'ouverture des portes (entrées et sorties de bateaux) mais peut aussi se lever ponctuellement portes fermées (observé le 17 octobre 2026 vers 11h). Aucun horaire officiel n'est publié.
- Le PDF 2026 donne le **25 octobre** à l'heure d'été (une heure trop tard) : correction du [Deauville Yacht Club](https://www.deauvilleyachtclub.org/ouvertures-des-portes/) appliquée via `CORRECTIONS` dans `index.html`.
- Le PDF 2026 contient un **oubli** : l'ouverture des portes de la nuit du **4 au 5 juillet** n'y figure pas (seule la fermeture du 5 à 05h32 est indiquée). La page affiche « Incertain » sur cette période. Le script d'extraction détecte ce genre d'erreur automatiquement.
- Les comptes à rebours tiennent compte des **changements d'heure** (29 mars, 25 octobre).
- Les données ne couvrent que **2026**. Il faudra relancer l'extraction quand Ports du Calvados publiera le PDF 2027.

### Notes de confort

Les seuils sont expliqués sur la page (« Comment est calculé… ») et réglés dans `index.html` (`scoreBoat`, `scoreKite`, `BEACH_ONSHORE`) :

- **Bateau** (notre bateau de 13 m) : favorable jusqu'à 17 nœuds et 1,25 m de vagues, prudence jusqu'à 27 nœuds et 2,5 m, déconseillé au-delà ou avec des rafales de plus de 34 nœuds ; jamais mieux que « prudence » de nuit. Un créneau d'écluse prend la note de sa pire heure.
- **Kitesurf** (plage de Deauville, orientée NNO) : plage de vent calculée pour le poids et les ailes du rider (« Mes ailes ») — une aile de S m² est idéale vers poids × 2,2 ÷ S nœuds et navigue de −12 % à +50 % autour ; minimum 9 nd en twin-tip, 7 nd en foil, 35 nd au plus ; rafaleux si l'écart rafales/vent moyen dépasse 8 nœuds ; side-on / side-shore = bon, onshore = moyen, side-off = déconseillé, **offshore = dangereux** ; orage ou nuit = pas de session.
- **Taille d'aile / voile / wing** indicative : poids (kg) × coef ÷ vent (nœuds), coef 2,2 en kite, 1,34 en windsurf, 1 en windfoil et en wingfoil (`SPORTS` dans `index.html`), parmi le matériel coché du rider. **Combinaison** selon la température de l'eau (modèle de courants Météo-France).

## Structure du dépôt

```
index.html              la page (HTML + CSS + JS, aucune dépendance à installer)
manifest.webmanifest    nom et icônes pour l'écran d'accueil
icons/                  icône « La fenêtre » (SVG + PNG 180/192/512 + maskable 512)
docs/logo/              logo : kit, règles d'usage, pistes, présentation
version.json            numéro de version en ligne, lu par la page pour se recharger
sw.js                   service worker minimal, sans cache (installation Android, page hors ligne)
tools/
  extraire-horaires.mjs extraction du PDF officiel -> données JSON + contrôle des incohérences
  publier-version.sh    nouveau numéro de version avant chaque publication
  logo-creneau.py       génère le kit du logo (Geist en tracés, fonttools)
  bouees.py             relevé des bouées Candhis (lancé par .github/workflows/bouees.yml)
  krea-generer.py       génération des illustrations via l'API Krea (jeton dans ~/.config/krea/token)
  annotations-kite.py   annotations précises (vent, bord d'attaque, positions) et carrousels
tuto/                   illustrations des tutos kite (décollage, atterrissage, water start)
docs/
  DESIGN.md             choix de design et d'ergonomie
  krea-prompts.md       prompts Krea des illustrations du tuto kite
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
