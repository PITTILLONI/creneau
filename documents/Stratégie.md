# Stratégie Crén'eau (document local, hors dépôt public)

Notes du 18 octobre 2026, à partir des échanges avec Antoine.

## Positionnement
- **Notre atout n°1 : l'hyper-personnalisation, port par port et club par club** (portes, écluse, passerelle, horaires, VHF, balisage, couleurs pour un port ; spots, cours, matériel, niveaux, réservation, couleurs pour un club). C'est ce que les grandes applis ne font pas et ne copieront pas depuis un bureau.
- **Hyper local et personnalisé** : ce que les applis météo généralistes ne savent pas faire. Portes du
  bassin Morny, cycle de la passerelle piétonne relevé sur le terrain, erreurs du PDF officiel corrigées,
  orientation des spots, note calculée pour son bateau ou son matériel.
- **La force du duo** : connaissance du terrain (Antoine, relevés sur place, réseau du port) + développement
  rapide (Claude). Chaque port demande des relevés locaux : c'est la barrière à l'entrée.

## Offre grand public (plaisanciers, glisse)
- Essentiel gratuit ; **Premium** affiché à la semaine (« 0,40 € / semaine ») mais **facturé à l'année ou au
  mois** (les frais fixes Stripe ≈ 0,25 € par paiement rendent la facturation hebdomadaire non rentable).
- **Pause d'hiver** : possibilité de suspendre l'abonnement de novembre à mars (Stripe sait suspendre la
  facturation d'un abonnement). Argument : « vous ne payez que quand vous naviguez ». Réduit les résiliations.
- Tarif fondateur pour les testeurs.
- Fonction phare du Premium : **alertes** « créneau favorable » (notification).

## Marque blanche pour les ports (piste principale de revenus)
- Une version **aux couleurs de chaque port**, avec ses spécificités (portes, écluse, passerelle, horaires,
  balisage, contacts, VHF).
- Argument : **se moderniser et gagner du temps** — moins d'appels VHF et téléphone sur « les portes ouvrent
  quand ? », information claire pour les visiteurs, image moderne du port.
- Modèle : abonnement annuel par port (ordre de grandeur quelques centaines à quelques milliers d'euros/an),
  installation incluse (relevés sur place, paramétrage).
- Cibles : ports à portes ou à écluse de la Manche et de l'Atlantique (Honfleur, Dives, Ouistreham,
  Saint-Malo, Granville…), puis Nouméa et outre-mer.

## Réservation de créneaux pour clubs et écoles (piste à creuser)
- Dans l'app, les clubs de voile et écoles de kite/windsurf/foil publient leurs créneaux de cours ou de
  location ; les utilisateurs réservent directement, sur les créneaux où la météo est favorable
  (à la manière de Planity pour les coiffeurs).
- Revenus : abonnement club/école, ou petite commission par réservation.
- Atout : l'app sait déjà quand les conditions sont bonnes ; elle peut proposer « séance possible demain
  14 h – 17 h » et remplir les cours.

## Mesurer avant d'investir
- Questionnaire dans l'app (désirabilité : au moins 40 % de « très déçus »).
- **Relance automatique de l'avis** à la 3e ouverture, puis une fois à la 6e.
- **Fréquence d'usage** : signal « Ouverture · Nom » envoyé au Google Form (au plus toutes les 2 h) ;
  compter par personne et par semaine. Pas de suivi par adresse IP (peu fiable sur mobile, donnée
  personnelle au sens du RGPD) ; les testeurs sont informés dans la présentation.
- Rendez-vous avec la capitainerie de Deauville : premier client potentiel de la marque blanche.

## Préalables à la version payante
- Droits sur les données : Open-Meteo (offre commerciale), Ports du Calvados et SHOM (horaires, marées),
  HAROPA (SIMBAD) — brouillons dans `emails.md`, en attente.
- Conditions d'utilisation et mentions de responsabilité dans l'app.
