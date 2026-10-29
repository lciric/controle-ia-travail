# Budget de la candidature EA Funds — trois scénarios — v1

Rédigé le 2026-10-07. Tableur : `budget-v1.csv` (même dossier ; montants en dollars). Estimations, sauf le calcul déjà dépensé.

| poste | minimal (7 mois) | central (12 mois) | ambitieux (12 mois) |
|---|---|---|---|
| rémunération de Lazar, charges sociales et impôt compris | 31 500 | 60 000 | 66 000 |
| ingénieur de recherche à mi-temps (environnement multi-agents du papier B, mise en libre accès) | — | — | 21 000 |
| co-auteur ou conseil en statistique séquentielle (lemme) | — | — | 4 000 |
| calcul sur carte et stockage (Vast.ai) | 2 500 | 6 000 | 12 000 |
| outils d'IA (abonnement Claude Code ; API pour les étapes à nombreux sous-agents) | 1 400 | 7 200 | 12 000 |
| validation humaine experte de la vérité terrain | — | 4 000 | 7 500 |
| déplacements (ateliers, NeurIPS 2027 si accepté) | 2 000 | 5 000 | 7 500 |
| divers (logiciels, comptabilité, frais d'un éventuel porteur fiscal) | 600 | 1 200 | 3 000 |
| sous-total | 38 000 | 83 400 | 133 000 |
| marge de 10 %, déclarée | 3 800 | 8 340 | 13 300 |
| **total** | **41 800** | **91 740** | **146 300** |

## Hypothèses, à vérifier par Lazar

- **Rémunération** : 4 500, 5 000 ou 5 500 dollars par mois, tout compris, en France. Le formulaire exige d'y inclure charges et impôt. Si tu es déjà rémunéré (statut de normalien, contrat doctoral, autre), cette ligne change entièrement : dis-moi ton statut et je la refais.
- **Calcul** : le devis du programme entier vaut 800 à 1 200 heures-équivalent A100, soit 1 200 à 2 700 dollars stockage compris (`livrables/premier-rendu-v1/devis-v1.md`, section 2). Le scénario central le double (graines, réplications, cartes H200 quand la mémoire l'exige, comme pour T0.4). L'ambitieux ajoute la famille d'organismes en 70B, les attaques par apprentissage par renforcement à plus grande échelle, l'essaim à N = 10 et une seconde famille de modèles.
- **Outils d'IA** : le programme est exécuté par des agents ; l'extraction seule lance une centaine de sous-agents. 200 dollars par mois correspondent à l'abonnement seul ; 600 à 1 000 dollars par mois couvrent un usage par l'API pour ces étapes. À ajuster sur ta facture réelle.
- **Dépensé à ce jour** : environ 20 dollars de calcul pour la phase 0 (registre `registres/depenses.md`).

## Recommandation

Demander le **scénario central, 91 740 dollars**, avec la fourchette de 41 800 à 146 300 dollars écrite dans la candidature, comme le formulaire le suggère. Le fonds accorde le plus souvent de 10 000 à 150 000 dollars. Pour une première candidature sans publication en sécurité de l'IA, le central est plus crédible que l'ambitieux ; l'ambitieux reste visible comme usage d'un financement plus grand. Confiance : environ 60 %.
