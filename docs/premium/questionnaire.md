# Questionnaire « Votre avis » — brancher le Google Form

L'app contient un questionnaire (carte « 💬 Votre avis compte », onglet Maintenant). Il envoie
les réponses **directement depuis l'app** vers un Google Form : elles arrivent dans un Google Sheet,
sans serveur ni compte pour les utilisateurs. Tant que le formulaire n'est pas branché, l'app ouvre
un e-mail prérempli à la place.

## Ce que mesure le questionnaire

| Question | Pourquoi |
| --- | --- |
| Si vous ne pouviez plus utiliser Crén'eau, vous seriez : très / un peu / pas déçu | **Test de Sean Ellis** : au-delà de ~40 % de « très déçu », le produit répond à un vrai besoin |
| Ce que vous utilisez aujourd'hui (Windguru, Windy, Windfinder, Météo-France, Météo-Consult, club…) + autre | les concurrents réels et les habitudes |
| Ce que vous aimeriez ajouter (alertes, spots, 16 jours, vent mesuré, favoris) + idée libre | les fonctions qui justifieraient le Premium |
| Prix juste (gratuit seulement / ~10 €/an / ~20 €/an / ~3 €/mois) | la disposition à payer |
| Contexte (ajouté automatiquement) : profil, sport, région | segmenter les réponses (bateau Deauville, kite Nouméa…) |

## Créer le formulaire (5 minutes)

1. Sur <https://forms.google.com>, créer un formulaire vide « Crén'eau — avis ».
2. Ajouter **5 questions de type « Paragraphe »**, dans cet ordre (le type texte accepte exactement
   les valeurs envoyées par l'app, cases cochées comprises) :
   1. `Déception si Crén'eau disparaissait`
   2. `Outils utilisés aujourd'hui`
   3. `Ajouts souhaités`
   4. `Prix juste`
   5. `Contexte`
3. Paramètres → décocher « Recueillir les adresses e-mail » et « Limiter à une réponse » (aucune connexion Google demandée).
4. Onglet Réponses → « Associer à Sheets » pour avoir le tableau.
5. Bouton **Envoyer** → lien → copier le lien du formulaire et me l'envoyer.

Je récupère alors l'identifiant du formulaire et les numéros `entry.xxx` des questions, et je les
renseigne dans `SURVEY` (`index.html`). Aucune autre manipulation.
