# Questionnaire « Votre avis » — brancher le Google Form

L'app contient un questionnaire (carte « 💬 Donnez votre avis », onglet Maintenant). Il envoie
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

Dans le Google Drive du propriétaire, dossier **Crén'eau** : le formulaire « Crén'eau — votre avis » et le
tableau **« Crén'eau — synthèse des avis »** (part de « très déçus », part prête à payer, outils et ajouts les plus
cités, réponses découpées en colonnes). Pour l'alimenter : dans le formulaire, Réponses → « Associer à Sheets »,
puis coller le lien de ce Google Sheet en B2 de la synthèse et cliquer « Autoriser l'accès » en A33.
(Sheets en français : formules avec des points-virgules ; plages bornées à la ligne 2000.)

Pour avoir **une colonne par rubrique** dans le Google Sheet : ajouter 4 questions « paragraphe »
(ou faire Données → Scinder le texte en colonnes, séparateur personnalisé « retour à la ligne »),
puis me donner le lien : je renseigne `SURVEY.entries` et retire `SURVEY.single`.

## Autres lignes reçues dans le formulaire

- **« Inscription bêta »** : prénom et nom d'un testeur (une fois, à la première ouverture).
- **« Ouverture »** : un testeur a ouvert l'app (au plus une ligne toutes les 2 h par personne), avec son nom,
  le nombre d'ouvertures depuis l'installation et s'il utilise l'icône de l'écran d'accueil. Pour compter les
  ouvertures par semaine : filtrer la colonne des réponses sur « Ouverture » et regrouper par nom et par date
  (colonne Horodateur).
- L'avis est demandé automatiquement **une seule fois**, après 7 minutes d'utilisation cumulée (app à l'écran), jamais par-dessus une autre fenêtre.
- Promesse affichée : **une réduction sur l'abonnement à son lancement** pour chaque testeur qui répond. Le nom du testeur est dans la ligne « Contexte » de chaque réponse : c'est la liste des bénéficiaires.

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
