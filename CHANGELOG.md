# Historique des versions

## 19 octobre 2026 — « Revoir la présentation » réparé
- Depuis l'onglet Conseils, « Revoir la présentation » ne montrait rien et bloquait l'app : les fenêtres (présentation, installation, avis) étaient rangées dans l'onglet « Maintenant », masqué à ce moment-là, donc ouvertes mais invisibles. Elles sont maintenant hors des onglets et s'affichent depuis n'importe où.

## 19 octobre 2026 — Bouton d'installation masqué une fois installée
- Le bouton **« Ajouter à l'écran d'accueil »** des Conseils n'apparaît plus quand l'app est ouverte depuis l'icône de l'écran d'accueil, ni après « C'est fait » ou une installation Android acceptée. Limite : sur iPhone, Safari ne peut pas savoir si l'icône existe déjà ; tant que la personne n'a pas touché « C'est fait », le bouton reste visible dans Safari.

## 18 octobre 2026 (19h) — Relance de l'avis, suivi des ouvertures
- **Relance de l'avis** : le questionnaire s'ouvre de lui-même à la **3e ouverture** (« Vous avez utilisé Crén'eau plusieurs fois… », bouton « Plus tard »), puis une dernière fois à la 6e. Un seul panneau par ouverture (présentation, puis installation, puis avis).
- **Suivi des ouvertures pour la bêta** : signal « Ouverture · Prénom Nom » envoyé au Google Form au plus toutes les 2 h (nombre d'ouvertures, icône d'écran d'accueil ou navigateur), pour compter l'usage par testeur et par semaine. Pas d'adresse IP ni de localisation. La phrase d'information de la présentation le mentionne.

## 18 octobre 2026 (18h30) — Calage de la passerelle piétonne confirmé
- Deuxième relevé sur place : la passerelle piétonne s'est levée à **18:26**, exactement à l'heure annoncée par l'app (après la descente de 17:56). Le cycle « première levée 12 min après l'ouverture des portes, puis 15 min levée / 30 min baissée » est confirmé pour ce jour ; à revérifier un jour où les portes ouvrent à une autre heure.
- Troisième relevé : la passerelle piétonne redescend vers **18:29**, juste après la fermeture des portes (18:28) : la dernière levée est bien coupée à la fermeture des portes, comme dans l'app. Durée de la manœuvre (levée / descente) encore inconnue.

## 18 octobre 2026 (18h) — Passerelle piétonne recalée sur le terrain
- Relevé sur place le 18 octobre (portes ouvertes à 13:44) : passerelle piétonne levée jusqu'à 17:56. Le cycle 15 min levée / 30 min baissée démarre donc **12 min après l'ouverture des portes** (levées 13:56, 14:41, 15:26, 16:11, 16:56, 17:41, 18:26), et non à l'ouverture. `BRIDGE_OFFSET` dans `index.html`. Un seul relevé : à confirmer sur d'autres jours.

## 18 octobre 2026 (18h30) — Installation facilitée, pas de zoom
- **Android** : service worker minimal (`sw.js`, sans aucun cache, la mise à jour automatique est préservée) pour que Chrome propose le bouton « Installer Crén'eau » en un tap ; page « Pas de connexion » hors ligne.
- **iPhone** : Apple n'autorise pas un site à s'ajouter seul à l'écran d'accueil ; le panneau guide mieux : **flèche animée** vers la barre de Safari, étapes pour iOS récent (⋯ puis Partager) et ancien (Partager), et la ligne « Sur l'écran d'accueil » dessinée pour la reconnaître.
- **Zoom désactivé** : viewport sans zoom, double-tap bloqué (`touch-action: manipulation`), pincement bloqué sur Safari iOS (`gesturestart`), champs de saisie à 16 px minimum (sinon Safari zoome à la saisie).
- Bouées **SIMBAD** (HAROPA, vent et houle du chenal de Port 2000) : non intégrées, leurs conditions d'utilisation interdisent la rediffusion sans autorisation écrite ; demande d'autorisation préparée.

## 18 octobre 2026 (18h) — Testeurs nommés, installation sur l'écran d'accueil
- Présentation : **prénom et nom demandés** à la première étape (obligatoires pour continuer), gardés sur le téléphone et envoyés **une seule fois** au Google Form du projet (« Inscription bêta · Nom · profil · région ») ; mention de leur usage. Ils sont aussi joints aux réponses de « Votre avis ». La présentation est reproposée une fois à ceux qui l'avaient déjà vue, pour qu'ils donnent leur nom.
- Étape 2 de la présentation raccourcie à deux lignes.
- **Installer sur l'écran d'accueil**, proposé à la **2e ouverture** (jamais si l'app est déjà ouverte depuis l'écran d'accueil) : étapes iPhone (Partager → « Sur l'écran d'accueil », avec l'astuce « ouvrir dans Safari » pour un lien reçu par WhatsApp/Messenger), Android (bouton « Installer » en un tap quand Chrome le permet, sinon menu ⋮). « Plus tard » : reproposé 3 ouvertures plus tard ; « C'est fait » : plus jamais. Lien permanent « Ajouter à l'écran d'accueil » dans Conseils. Une ouverture = une session (le rechargement automatique après une mise à jour ne compte pas).

## 18 octobre 2026 (17h45) — Présentation au premier lancement
- **Bottom sheet de bienvenue** à la première ouverture (après le mot de passe), 4 étapes à faire glisser : 1) choix du profil (Bateau / Kite, windsurf, foil) et de la région (Deauville / Nouméa), appliqués tout de suite ; 2) l'essentiel du profil (portes et passerelle piétonne 15/30 à Deauville, carte Maintenant à Nouméa, ou réglage du matériel avec « Régler maintenant ») ; 3) lire une note (couleurs, raison, ciel, cadre plein / pointillé) ; 4) **version bêta** : aide à la décision, pas une garantie, VHF 9 et bulletin officiel, numéros d'urgence, infos encore à confirmer, lien vers « Votre avis ».
- Vue une seule fois ; « Revoir la présentation » dans l'onglet Conseils.

## 18 octobre 2026 (17h30) — Passerelle piétonne : 15 min levée / 30 min baissée
- Cycle corrigé (info locale) : la passerelle piétonne se lève **15 min toutes les 45 min** pendant l'ouverture des portes (15 min levée, 30 min baissée). Ex. ouverture à 13:44 : levées 13:44, 14:29, 15:14… ; au pire une demi-heure d'attente. Toujours supposé démarrer par une levée à l'ouverture (à confirmer).

## 18 octobre 2026 (17h15) — Le ciel : pluie ou beau temps
- « Favorable » ne veut pas dire « beau temps » : chaque créneau, session, carte des 7 jours, verdict, journée du calendrier, carte « Maintenant » (Nouméa) et heure du détail indique maintenant **le ciel** avec une icône : Ensoleillé / Ciel dégagé (nuit), Éclaircies, Couvert, Brouillard, **Pluie** ou **Averses possibles avec les millimètres**, Neige, Orage.
- Pluie = au moins 0,2 mm dans l'heure ou un code de pluie (Météo-France via Open-Meteo, nouvelle donnée `precipitation`) ; sans pluie, c'est le ciel le plus fréquent sur la période. La note n'est pas modifiée par la pluie (l'orage reste éliminatoire).

## 18 octobre 2026 (16h45) — Cycle de la passerelle piétonne
- Pendant l'ouverture des portes, la passerelle piétonne alterne **15 min levée / 15 min baissée** (info locale). La carte « Sortie en mer » affiche l'état en direct : « **Levée** jusqu'à 13:59 (dans 9 min) » ou « **Baissée** · prochaine levée à 14:14 (dans 9 min) », la dernière levée s'arrêtant à la fermeture des portes. Avant l'ouverture : « Première levée vers 13:44, puis 15 min levée / 15 min baissée ».
- Hypothèse à confirmer : le cycle commence par une levée à l'ouverture des portes (`BRIDGE_UP`, `BRIDGE_DOWN`, `bridgeCycle` dans `index.html`).
- Conseil « Sortir du bassin Morny » complété (au pire un quart d'heure d'attente).

## 18 octobre 2026 (16h15) — Questionnaire branché
- Le questionnaire « Votre avis » envoie maintenant les réponses **directement dans le Google Form** du projet (une question paragraphe, réponses mises en forme une ligne par rubrique), sans e-mail à envoyer.

## 18 octobre 2026 (16h) — « Votre avis » : désirabilité et attentes
- Onglet Maintenant : carte **« 💬 Votre avis compte »** qui ouvre un questionnaire d'une minute, sans quitter l'app : déception si Crén'eau disparaissait (test de Sean Ellis), outils utilisés aujourd'hui (Windguru, Windy, Windfinder, Météo-France, Météo-Consult, club… + autre), ajouts souhaités (alertes, spots, 16 jours, vent mesuré, favoris + idée libre), prix juste pour un Premium. Le contexte (profil, sport, région) est ajouté automatiquement.
- Envoi **direct vers un Google Form** (réponses dans un Google Sheet) dès que le formulaire est branché (`SURVEY` dans `index.html`, mode d'emploi dans `docs/premium/questionnaire.md`) ; d'ici là, e-mail prérempli.

## 18 octobre 2026 (15h30) — Nouméa : Anse Vata, Magenta, Port Moselle en spots de glisse
- Trois spots de glisse ajoutés à Nouméa, orientation calculée sur le trait de côte OpenStreetMap :
  - **Anse Vata** (la grande plage) : tournée vers le sud-ouest (243°) ; avec l'alizé, vent de côté-terre.
  - **Magenta** : tournée vers l'est (95°) ; l'alizé y arrive de face ou de côté, le spot le mieux orienté par alizé. Mise en garde : aérodrome de Magenta tout proche, se renseigner sur les zones autorisées.
  - **Port Moselle** (marina, départ vers la baie de la Moselle) : tournée vers l'ouest (265°, à confirmer, mesure peu nette à cause des quais) ; avec l'alizé, offshore et rafaleux.
- Conseils « Règles et précautions à Nouméa » complétés pour ces spots.

## 18 octobre 2026 (15h) — Profil Glisse : kite, windsurf, windfoil, wingfoil
- Le profil « Kitesurf » devient **« Glisse »** ; le sport se choisit dans le panneau de l'en-tête (**Kite / Windsurf / Windfoil / Wingfoil**), avec le poids et **son matériel** (« Mes ailes », « Mes voiles », « Mes wings », gardés séparément pour chaque sport).
- Même logique pour tous, chiffres propres à chaque sport : taille idéale = poids × coef ÷ vent (2,2 kite, 1,34 windsurf, 1 windfoil et wingfoil) ; vent minimum 9 nd en kite (7 en foil), 11 en windsurf (planing), 7 en windfoil, 10 en wingfoil ; maximum 25 nd en windfoil, 35 sinon. Notes, sessions, 7 jours, calendrier, « … à sortir » et « … cible » suivent le sport choisi.
- Pastille de l'en-tête compacte : icône du sport (aile, voile, wing) + tailles (« 6,5/8 · foil ») ; noms courts des spots de Nouméa (Méridien, Aquarêve) pour que tout tienne sur un petit écran.
- Les tutos illustrés (décollage, atterrissage, water start) restent affichés en kite seulement.
- Une session bien notée garde un message positif (« Vent de 20 nd, bon pour ta 6,5 m² »).

## 18 octobre 2026 (14h30) — Chargement beaucoup plus rapide
- Constat : le service de données marines d'Open-Meteo répondait très lentement (vagues : 16 à 30 s, parfois aucune réponse ; 5 modèles : jusqu'à 17 s), et la page attendait la plus lente des 4 requêtes avant d'afficher quoi que ce soit.
- **Affichage progressif** : la page s'affiche dès que le vent est là ; les vagues sont attendues 5 s au plus, puis ajoutées à leur arrivée (« vagues indisponibles pour le moment » en attendant) ; la température de l'eau et le vent consolidé sur 5 modèles complètent l'affichage quand ils arrivent.
- **Délai maximum par requête** (9 s, 30 s pour les vagues en tâche de fond) : une requête bloquée ne fige plus la page.
- **Dernières prévisions gardées sur le téléphone** (moins de 6 h) : affichées immédiatement à l'ouverture, puis mises à jour ; si la mise à jour échoue, elles restent affichées avec « Mise à jour impossible · prévisions de HH:MM » et Réessayer.
- Mesuré : verdict affiché en ~1 s à la première ouverture, ~0,2 s ensuite ; ~6-7 s dans le pire cas simulé (vagues à 25 s) au lieu de 17 s et plus.

## 18 octobre 2026 (14h) — Nouméa, « Ajouter votre spot »
- **Deuxième région : Nouméa** (bateau et kite), pour tester avec de la famille sur place. Choix dans l'en-tête : port (« Nouméa · Port Moselle ») en mode Bateau, spot en mode Kite (Anse Vata · Méridien, Anse Vata · Aquarêve, Îlot Maître, d'après les écoles locales et OpenStreetMap). Changer de port ou de spot change de région ; la région est gardée sur le téléphone.
- **Heure de Nouméa** (Pacific/Noumea, UTC+11) partout : horloge, créneaux, calendrier, prévisions. Les horaires des portes de Deauville restent calculés à l'heure de Paris.
- **Bateau à Nouméa** : pas d'écluse ni de passerelle piétonne ni de bouées Candhis (masqués) ; carte « Maintenant » (note, vent, marée, eau, soleil) ; « Sorties possibles à venir » = heures de jour où le vent convient ; destinations du lagon (îlots Canard, Maître, Signal, phare Amédée, baie de Prony — caps directs indicatifs).
- **Lagon** : le modèle de vagues MFWAM ne voit pas la barrière de corail (il annonce 1,6 m dans le lagon) : vagues ignorées, note sur le vent seul, et l'app le dit.
- **Marées de Nouméa calculées** à partir de la hauteur d'eau prévue (Open-Meteo `sea_level_height_msl`), pleines et basses mers par interpolation, sans coefficient, à vérifier sur l'annuaire SHOM.
- Nouméa : secours au **16** ou VHF 16 (COSS NC), météo marine VHF 65/66, liens meteo.nc et SHOM Nouméa, conseils kite locaux (offshore au Méridien, patates de corail à marée basse, réserve de l'îlot Maître) ; les conseils propres à Deauville (bassin Morny, portes) sont masqués.
- **« ➕ Ajouter votre spot… » / « ➕ Ajouter votre port… »** en bas des listes : ouvre un e-mail prérempli au propriétaire du projet (nom, position, orientation de la plage, pièges).

## 18 octobre 2026 (13h30) — L'app devient « Crén'eau »
- Nouveau nom, plus générique que « Port de Deauville » et qui couvre bateau et kite : **Crén'eau — le bon créneau pour glisser** (créneau + eau). Titre, nom sous l'icône de l'écran d'accueil, écran du mot de passe, manifeste.
- Dépôt renommé `deauville-passerelle-ecluse` → **`creneau`** ; nouvelle adresse <https://pittilloni.github.io/creneau/>. L'ancienne adresse redirige vers la nouvelle (petit dépôt de redirection), y compris pour l'icône déjà posée sur l'écran d'accueil. Mot de passe et réglages (poids, ailes, spot) sont conservés (même domaine).

## 18 octobre 2026 (13h15) — Kite : aile cible quand mon matériel ne suffit pas
- Quand le vent est trop faible ou trop fort pour mes ailes et mon poids, l'app indique **l'aile qu'il faudrait** : plus grande si le vent est trop faible, plus petite s'il est trop fort, **foil** sous 9 nd (twin-tip impossible), rien sous 7 nd ou au-delà de 35 nd.
- Spot : la tuile devient « **Aile cible** » (ex. « Foil », « 16 m² ») ; raison de la note complétée (« … avec ta 12 m² · aile cible : 16 m² ») ; Prévisions : verdict, détail heure par heure ; carrousel 7 jours : « cible 16 m² » / « foil requis » sur les jours sans session ; calendrier : tuile « Aile cible » et raison de l'heure la plus proche de naviguer.

## 18 octobre 2026 (13h) — Calendrier : une seule ligne de date
- La date n'est plus affichée deux fois (champ « 18/10/2026 » puis « Dimanche 18 octobre » en dessous) : une seule barre ‹ **Mardi 20 octobre** 📅 ›, toucher la date ouvre le calendrier du téléphone. Le bouton « Aujourd'hui » passe à droite du titre « Un autre jour » et n'apparaît que lorsqu'on regarde un autre jour.

## 18 octobre 2026 (12h45) — Créneaux en carrousel
- « Créneaux d'écluse à venir » (et « Sessions de kite à venir ») passent en **carrousel horizontal**, comme les 7 prochains jours : une carte par créneau, la suivante dépasse pour inviter à glisser, cadre plein (favorable aujourd'hui) ou pointillé (autre jour) conservé. Sous le carrousel : « 5 créneaux sur 3 jours dont 2 favorables · glisser pour voir la suite ».

## 18 octobre 2026 (12h30) — Icônes, réglages kite dans l'en-tête, carrousel 7 jours
- **Icônes** pour alléger la lecture : devant les intitulés (vent, rafales, mer, période, provenance, marée montante/descendante, air, soleil, eau, aile), devant chaque raison de note (coche si favorable, vent, vagues, lune la nuit, orage, alerte vent de terre), lune à la place de « nuit », pleine/basse mer, passerelle piétonne et portes.
- Kite : **poids et ailes dans l'en-tête**, à côté du spot (pastille « 75 kg · 9/12 » qui déplie les réglages), communs à tous les onglets ; le rappel en tête des Prévisions est retiré. Noms des spots raccourcis (« Deauville »).
- Calendrier : le panneau « 7 prochains jours » devient un **carrousel léger** en haut de l'onglet : une carte par jour (note, meilleur créneau ou session + aile), **cadre plein** si favorable aujourd'hui, **pointillé** si favorable un autre jour, jour affiché surligné ; toucher une carte ouvre le jour.

## 18 octobre 2026 (12h) — Les 7 prochains jours
- Calendrier : bouton **« Les 7 prochains jours »** qui ouvre un panneau avec, jour par jour, les créneaux d'écluse notés (couleur Favorable / Prudence / Déconseillé, « nuit ») ou, en kite, les sessions navigables avec l'aile à sortir, la note du jour et sa raison, et un total (« 2 créneaux favorables sur 7 jours »). Toucher un jour l'ouvre dans le calendrier.
- Jours 1 à 3 : prévisions déjà chargées ; jours 4 à 7 : un seul appel groupé (`fetchDays`).

## 18 octobre 2026 (11h45) — Créneaux favorables, pastille des bouées
- Liste des créneaux (et sessions kite) : chaque créneau **Favorable** / session **Navigable** est entouré en vert, **trait plein s'il est aujourd'hui**, **pointillé s'il est un autre jour** (avant : seul le meilleur créneau était entouré).
- Bouées : la pastille « il y a 37 min » dépassait de la carte et son point vert était écrasé sur les petits écrans (classe `live` déjà utilisée par l'horloge) ; elle est maintenant une vraie pastille et le nom de la bouée passe à la ligne. Plus aucun défilement horizontal de la page.

## 18 octobre 2026 (11h30) — Vent consolidé, prévisions kite selon le matériel
- Le recoupement des modèles ne s'affiche plus (« modèles en désaccord » était peu compréhensible) : il sert désormais à **fiabiliser la donnée**. Le vent affiché et noté est la **médiane de 5 modèles** (Météo-France AROME/ARPEGE comptant double, ECMWF, ICON, UKMO, GFS) : une erreur isolée d'un modèle ne fausse plus la note. Direction et écart rafales/vent restent ceux de Météo-France. Partout : spot, prévisions, créneaux bateau, calendrier.
- Onglet Prévisions (kite) : rappel **« Pour 75 kg avec tes ailes 9 et 12 m² : ça navigue de 12 à 27 nd »** avec un bouton Modifier (qui ouvre le réglage sur l'onglet Spot) ; chaque session et chaque heure indique **l'aile à sortir** ; s'il n'y a aucune session, l'app dit ce qui manquerait (« le vent ne dépasse pas 10 nd : il faudrait une 16 m² ou un foil »). Calendrier : l'aile de la meilleure session.

## 18 octobre 2026 (11h) — Accord des modèles et choix de l'aile
- **Vent recoupé entre 5 modèles** : Météo-France (AROME/ARPEGE), européen (ECMWF), allemand (ICON), britannique (UKMO) et américain (GFS). La note reste calculée sur Météo-France, mais chaque prévision indique *Modèles d'accord / Accord moyen / Modèles en désaccord*, avec le vent de chaque modèle. Quand la médiane des modèles changerait la note, l'app l'écrit (« La plupart des modèles prévoient moins de vent (6 nd au lieu de 11) : ce serait « Pas navigable » »). Affiché dans le spot kite, le verdict « Je sors en mer ? », chaque créneau ou session, la bande heure par heure et le calendrier (y compris au-delà de 3 jours, sans Météo-France).
- Kite : réglage **« Mes ailes »** (5 à 17 m², plus Foil), 9 et 12 m² par défaut, gardé sur le téléphone. Le **vent minimum et maximum** sont calculés pour le poids du rider et ses ailes au lieu du seuil fixe de 12 nœuds : une aile de S m² est idéale vers poids × 2,2 ÷ S nœuds et navigue de −12 % à +50 % autour ; plancher 9 nd en twin-tip, 7 nd en foil ; 35 nd au plus.
- L'« Aile à sortir » est choisie **parmi tes ailes** (« ta 12 m² · idéal 11 m² pour 75 kg »), avec un conseil si les rafales demandent la plus petite, ou ce qui manquerait (« trop peu de vent pour ta 12 m² : il faudrait une 13 m² ou un foil »).

## 18 octobre 2026 (10h30) — Indicateur de récupération des données
- Bateau et Kitesurf : quand l'app récupère des données, une **barre animée** court sous l'en-tête, le point de l'horloge passe en bleu et une ligne dit quoi : « Récupération des prévisions météo… », « …des prévisions du spot de Trouville-sur-Mer… », « …des mesures des bouées… », « …des prévisions du 22 octobre… », « …(nouvelle tentative)… ».
- En cas d'échec durable des prévisions : message « Prévisions météo indisponibles (connexion ?) » avec un bouton **Réessayer** ; idem dans la carte du jour du calendrier.
- Les prévisions principales retentent aussi automatiquement quand Open-Meteo est saturé.
- Les bouées ne sont plus chargées en mode Kitesurf (elles n'y sont pas affichées).
- Correctif : à l'ouverture avec `#onglet` dans l'adresse, la page ne défile plus de quelques pixels (haut de l'en-tête coupé).

## 18 octobre 2026 — Bouées au large en direct
- Mode Bateau, onglet Maintenant : **mesures en direct des bouées houlographes** à l'entrée de l'estuaire de la Seine (Candhis, Port du Havre et Cerema), à 12-13 km au nord de Deauville : hauteur des vagues (H1/3), vague max, période, provenance, tendance sur 3 h, courbe des 24 dernières heures, et **comparaison avec la prévision Météo-France** de l'heure (« la mer est plus calme que prévu »).
- Deux bouées : 07609 *Haut du Sud-Ouest* (active) et 07611 *Nord du mouillage* (en maintenance, aucune mesure depuis le 2 juin 2026 : affichée « hors service » tant qu'elle ne transmet pas).
- Relevé toutes les 30 min par GitHub Actions (`tools/bouees.py`, `.github/workflows/bouees.yml`), publié sur la branche `donnees` : Candhis n'accepte pas les appels directs depuis la page.

## 17 octobre 2026 (15h30) — Navigation par onglets, conditions dans le calendrier
- **Un onglet = un écran** : la barre du bas n'est plus un raccourci vers une longue page, chaque onglet (Maintenant, Sortir, Conseils, Calendrier) affiche uniquement sa section. L'onglet ouvert est gardé dans l'adresse (`#sortir`…), chaque onglet retrouve sa position, toucher l'onglet déjà ouvert remonte en haut. Le pied de page (sources, liens) n'apparaît plus que sur Maintenant (et l'avertissement sur Calendrier).
- Onglet Sortir allégé : les **allures et réglages par destination** sont dans un menu dépliant sous la voilure conseillée.
- **Calendrier : conditions du jour choisi** (bateau et kite) : note de chaque créneau d'écluse directement sous son horaire, meilleur créneau (ou meilleure session kite) avec sa raison chiffrée, vent, mer, soleil (+ aile et eau en kite), bande heure par heure du jour. Les 3 premiers jours reprennent les prévisions Météo-France ; au-delà, tendance des modèles mondiaux jusqu'à J+15 (vagues jusqu'à J+7 environ, sinon note sur le vent seul) ; jours passés : archives Météo-France. Au-delà de J+15, la page indique à partir de quand la prévision arrivera.
- Si Open-Meteo est saturé (« service is overloaded »), le calendrier essaie automatiquement un autre modèle.
- L'onglet s'appelle « Calendrier » dans les deux profils.

## 17 octobre 2026 (13h30) — Tutos kite illustrés et annotés
- Retour au **style illustré**, rendu précis : 20 illustrations (Krea Nano Banana Pro et Krea 2) vérifiées une à une, avec des **annotations exactes superposées** : flèche de vent (ou « vent dans le dos »), bord d'attaque en orange, positions de l'aile (9 h / 12 h / 3 h) en vert, erreurs en rouge.
- Étapes au sol vues de côté (mer à gauche, vent de gauche à droite), aile en l'air vue de derrière le rider.
- Nouvelles illustrations : étaler, gonfler, connecter (dos vers le ciel, bord d'attaque face au vent), sécuriser, porter son aile, et les 6 étapes du water start.
- Scripts : `tools/krea-generer.py` (génération via l'API Krea, jeton lu dans `~/.config/krea/token`, jamais dans le dépôt) et `tools/annotations-kite.py` (annotations et carrousels).

## 17 octobre 2026 (13h05) — Conseils bateau, menus homogènes
- Mode Bateau : onglet **Conseils** avec sortir du bassin Morny (VHF 9, passerelle piétonne, portes), check-list avant de partir (dont l'heure de fermeture des portes pour rentrer), prendre un ris, réglages par allure, priorités en mer, homme à la mer et urgences.
- Tous les menus dépliants (tutos, priorités, sécurité, règles locales, calcul des notes) ont le même style.
- Prévisions : nouvelle tentative automatique après un raté réseau.

## 17 octobre 2026 (13h) — En-tête : sélecteur de profil en haut
- Le titre « Port de Deauville » laisse la place au **sélecteur Bateau / Kitesurf**, fixé en haut de l'écran. Juste en dessous : « Port de Deauville · bassin Morny » en mode Bateau, ou le **choix du spot** (Deauville, Trouville, Houlgate, Cabourg) en mode Kitesurf, avec l'heure en direct.

## 17 octobre 2026 (12h45) — Voilure et allures pour le bateau
- Mode Bateau : **voilure conseillée** pour le créneau d'écluse (grand-voile haute / 1, 2 ou 3 ris, génois entier ou roulé), calculée sur les rafales, avec alertes mer formée, nuit, « prends les ris au port ».
- **Allure et réglages vers les destinations** (Le Havre, Honfleur, Dives, Ouistreham, le large) selon le vent prévu : vent debout, près, bon plein, travers, largue, vent arrière, avec les réglages de chaque allure.
- Hypothèse : voilier de 13 m gréé en sloop, grand-voile 3 ris, génois sur enrouleur.

## 17 octobre 2026 (12h35) — Schémas techniques précis pour les tutos kite
- Les illustrations générées plaçaient mal l'aile (bord d'attaque, valve, sens du vent). Elles sont remplacées par des **schémas techniques annotés** :
  - au sol (zone, dérouler, étaler, gonfler, connecter, sécuriser) : vue de dessus, mer et vent toujours en bas, rider face à son aile donc **rouge toujours à gauche**, encart « vu de côté » pour la position de l'aile ;
  - en l'air (s'accrocher, bord de fenêtre, tendre, monter, atterrir, water start) : vue de derrière le rider, vent dans le dos, fenêtre en cadran 9 h / 12 h / 3 h et zone de puissance.
- Connexion des lignes et aile sécurisée : **aile dos vers le ciel, bord d'attaque face au vent**.
- Water start redessiné, avec la comparaison « barre tirée » / « bras tendus ».
- Les trois tutos sont rangés dans des **menus dépliants**.
- Seules restent deux illustrations Krea de gestes (pouce levé, main sur la tête). Les schémas sont générés par `tools/schemas-kite.py`.

## 17 octobre 2026 (12h30) — Tutos kite complets, bateau de 13 m
- **Décoller** en 10 étapes (zone, dérouler les lignes, étaler, gonfler, connecter, s'accrocher, sortir de la zone de puissance, tendre, signal, monter à midi), relu avec des sources d'écoles (kiteinside, FQK, whenwherekite).
- **Atterrir et porter son aile** en 4 étapes (signal main sur la tête, récupération par le bord d'attaque, sécuriser, porter dos au sable face au vent).
- **Water start** en 6 schémas, dont « ne t'agrippe pas à la barre : bras tendus, barre loin ».
- Illustrations Krea (Krea 2 Medium) avec étiquette de vent ; water start en schémas faute de crédits Krea.
- **Seuils bateau recalés pour notre bateau de 13 m** : favorable jusqu'à 17 nd et 1,25 m, prudence jusqu'à 27 nd et 2,5 m.
- Le texte sous « Sessions de kite à venir » parle de kite dès le changement de profil.

## 17 octobre 2026 (12h) — Illustrations Krea du tuto kite
- Les 6 étapes « Décoller son aile » sont illustrées avec Krea (Krea 2 Medium, mêmes personnages et même style), vérifiées une à une : aile en bord de fenêtre au bout des 4 lignes, pré-vol aile au sol, pouce levé, zénith. Étiquette « vent de la mer » sur les vues de plage. Les dessins SVG restent en secours si une image ne charge pas.

## 17 octobre 2026 (11h35) — Carte de sortie neutre
- La carte « Sortie en mer » n'est plus entièrement rouge quand c'est fermé : fond neutre, la couleur ne marque que l'état (Fermé / Ouvert, chrono, barre), pour ne pas la confondre avec la note des conditions de mer.

## 17 octobre 2026 (11h30) — Plages, décollage illustré, assurance, mot de passe
### Ajouté
- **Mot de passe** à l'ouverture de l'app (demandé une fois par appareil). Seule l'empreinte SHA-256 est dans le code : c'est un verrou, pas une protection forte (site statique public).
- Kite : **choix de la plage** (Deauville, Trouville-sur-Mer, Houlgate, Cabourg), avec prévisions et orientation propres à chaque plage.
- Kite : **carrousel illustré en 6 étapes** pour décoller son aile avec un assistant.
- Kite : **mon assurance** (assureur ou licence, n°, téléphone d'assistance, échéance), enregistrée uniquement sur le téléphone, avec alerte d'expiration et bouton d'appel.
### Corrigé
- Le bandeau d'erreur affichait les erreurs de scripts extérieurs (extensions Safari) : il ne s'affiche plus que si l'app elle-même ne démarre pas.

## 17 octobre 2026 (11h15) — Trajet de sortie et correction du 25 octobre
- **25 octobre corrigé** : le PDF officiel donne ce jour-là les horaires des portes à l'heure d'été (une heure trop tard). Correction du Deauville Yacht Club appliquée (`CORRECTIONS` dans `index.html`) et signalée dans le calendrier.
- La carte suit le trajet d'un bateau du bassin des Yachts : 1 · passerelle piétonne (entre bassin des Yachts et bassin Morny), 2 · portes du bassin Morny, puis la mer.

## 17 octobre 2026 (11h) — Correction passerelle piétonne
- Retrait des heures de levée de la passerelle piétonne : elles étaient déduites des horaires des portes du bassin Morny, alors qu'elle se lève aussi portes fermées (observé sur place). Le chrono compte désormais l'ouverture / la fermeture des portes, la passerelle piétonne est indiquée « horaires de levée non publiés · VHF 9 » en attendant une source fiable.

## 17 octobre 2026 (après-midi) — Persona marin, chrono de levée, vrai mode kite

### Corrigé
- La page parlait au piéton : elle parle maintenant au **marin**. Passerelle piétonne et écluse fusionnent en une carte **« Passage du bassin Morny »** (ouvert/fermé aux bateaux), avec un **chrono** jusqu'à la première ou la dernière levée de la passerelle piétonne.
- « Bon / Moyen / Déconseillé » remplacés par des libellés qui disent quoi faire (*Favorable / Prudence / Déconseillé*, *Navigable / Limite / Pas navigable*), avec la raison chiffrée.
- L'app ajoutée à l'écran d'accueil pouvait rester sur une vieille version (cache) : le rechargement automatique contourne maintenant le cache. Un message s'affiche si un script plante.

### Ajouté
- Mode kite 100 % kitesurfeur (ni passerelle piétonne ni écluse, pied de page dédié) : spot en direct (vent, taille d'aile idéale selon le poids du rider, température de l'eau et combinaison, rafales, marée, air, coucher du soleil), prévisions de sessions, section **Bonnes pratiques** (priorités, décollage/atterrissage, sécurité, règles locales).
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
