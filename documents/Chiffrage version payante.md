# Chiffrage d'une version payante de Crén'eau

Estimation au 18 octobre 2026, à affiner avec les réponses d'Open-Meteo, Ports du Calvados et du SHOM
(voir `emails.md`) et avec les résultats du questionnaire (`questionnaire.md`).

## Ce qu'il faut construire

| Brique | Pourquoi | Effort estimé |
| --- | --- | --- |
| Petit serveur (fonctions Vercel) qui appelle la météo avec la clé payante et met en cache par spot | la clé ne doit pas être dans la page ; un appel par spot et par heure sert tous les utilisateurs | 2 à 3 jours |
| Comptes (Supabase Auth, connexion par lien e-mail) | savoir qui est abonné ; remplace le mot de passe actuel | 1 à 2 jours |
| Paiement (Stripe Checkout + portail client, webhook → Supabase) | abonnement annuel/mensuel, résiliation en un clic | 1 à 2 jours |
| Alertes (Web Push, possible sur iPhone pour une app ajoutée à l'écran d'accueil depuis iOS 16.4) | la fonction Premium la plus attendue a priori | 3 à 4 jours |
| Limites gratuit / Premium dans l'interface, pages CGU et confidentialité | « aide à la décision, pas une garantie » ; RGPD (e-mails, paiements) | 1 à 2 jours |
| **Total** | | **≈ 8 à 13 jours** |

## Coûts mensuels (ordres de grandeur, à vérifier)

| Poste | Coût |
| --- | --- |
| Open-Meteo « API Standard » (usage commercial, 1 M d'appels/mois) | **prix à obtenir** (non affiché sur leur site) |
| Vercel (hébergement + fonctions) | gratuit au départ ; Pro ≈ 20 $/mois si besoin |
| Supabase (comptes, base) | gratuit jusqu'à ~50 000 utilisateurs actifs/mois ; Pro ≈ 25 $/mois |
| Stripe | ≈ 1,5 % + 0,25 € par paiement (carte européenne) : ≈ 0,55 € sur un abonnement de 20 €/an |
| Nom de domaine (ex. creneau.app) | ≈ 15-30 €/an |
| Données marées / portes | selon réponses du SHOM et de Ports du Calvados (gratuit si autorisation, sinon licence) |

Avec la mise en cache côté serveur (un appel par spot et par heure), 1 M d'appels par mois couvre
très largement quelques dizaines de spots, quel que soit le nombre d'utilisateurs.

## Seuil de rentabilité

Coût fixe mensuel F (Open-Meteo + hébergement), abonnement annuel P :

    abonnés nécessaires ≈ 12 × F ÷ (P − frais Stripe)

Exemples (P = 20 €/an, frais ≈ 0,55 €, net ≈ 19,45 €) :

| Coût fixe mensuel | Abonnés pour couvrir |
| --- | --- |
| 30 € | ≈ 19 |
| 75 € | ≈ 47 |
| 150 € | ≈ 93 |

## Étapes conseillées

1. **Valider l'intérêt** : questionnaire dans l'app, ouvert aux clubs et écoles (Deauville, Nouméa).
   Objectif : au moins 40 % de « très déçu » et une part significative prête à payer 10-20 €/an.
2. **Sécuriser les données** : prix Open-Meteo, accord Ports du Calvados et SHOM.
3. **Construire** comptes, paiement, serveur, puis alertes.
4. **Lancer** avec un essai gratuit (ex. 1 mois) et un tarif fondateur pour les premiers abonnés.
