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

## Formulaire branché (18 octobre 2026)

Formulaire « Crén'eau — avis » : `1FAIpQLSfN0jynPaX6YNUVvbVU6IT3S68nzKTfMnmmwuNuMUERNXHQCQ`, une seule
question « paragraphe » (`entry.1724789462`). L'app y envoie toutes les réponses mises en forme, une
ligne par rubrique :

    Déception si Crén'eau disparaissait : Très déçu
    Outils utilisés aujourd'hui : Windguru ; Windy ; Autre : webcam Anse Vata
    Ajouts souhaités : Alertes créneau favorable
    Prix juste : 20 € par an
    Contexte : Glisse (Wingfoil) · Nouméa

Pour avoir **une colonne par rubrique** dans le Google Sheet : ajouter 4 questions « paragraphe »
(ou faire Données → Scinder le texte en colonnes, séparateur personnalisé « retour à la ligne »),
puis me donner le lien : je renseigne `SURVEY.entries` et retire `SURVEY.single`.

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
