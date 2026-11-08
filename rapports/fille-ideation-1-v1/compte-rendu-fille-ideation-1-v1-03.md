# Compte rendu 03 — fille idéation 1, v1

Session `session_016QhUrujoj3FTuFNoYshNYB` (fille), mère `session_016QhUrrLeN21G7Z9KZobE42`.
Date : 2026-11-08, ~11:27–11:31 UTC.

## Objet
Lancement du tour étage III du collisionneur v2.6 sur la question scellée du pilier attaque (antériorité et originalité), pour l'entretien TAIF. Tour T1 (conception) terminé ; arrêt à la porte.

## Prérequis vérifiés avant lancement
- GO-2026-11-08-06 : type calcul, plafond 25 USD, échéance 2026-11-30, accordé par Lazar.
- Mot de Lazar dans cette session : « GO » puis « rechargé, relance ».
- Contrôle des espèces v2 : trois OK (A 0,00053, B 0,000192, C 0,00076 USD). Commit `3204af6`.
- Faits v1 : poussé et approuvé par la mère. Empreinte `4614f1c939c1c9996c6a594034b87a6a3a92ec3e55cd1231f82cdaee101a7595`.
- Question scellée : empreinte `29870ac9a8091c165375c51f4b74d6e0f38ae60d2e8754872ff70fb3077820c4`.
- Lanceur v3 : empreinte `30b81fe23a2d32db33480452aaf7036819668193be62a2071ce8b8915028d23d`.

## Résultat du tour T1 (conception)

| Cellule | Statut | Jetons sortie | Caractères | Marqueur | Coût USD |
|---|---|---|---|---|---|
| E3-T1-conception-A (Fable 5.1) | **REFUS** (bio) | 97 | 0 | non | 0,06 |
| E3-T1-conception-B (Opus 5.5) | **OK** | 17 844 | 22 695 | oui | 0,38 |
| E3-T1-conception-C (Argon) | **OK** (STOP) | 5 677 | 19 081 | oui | 0,32 |
| **Total T1** | | | | | **0,75** |

### Détail du refus de A
- Catégorie : `bio` (classifieur de biosécurité).
- Texte de sortie : vide (SHA256 = `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).
- Seuls des jetons de réflexion ont été produits (97 jetons), puis le classifieur a bloqué la génération.
- Cause probable : le terme « organisme saboteur » du contexte (métaphore pour les agents IA du programme) a déclenché le classifieur de biosécurité de Fable 5.1.
- Le refus est spécifique à Fable : Opus 5.5 a répondu sans problème sur le même prompt (identique, SHA256 du prompt `8fc293fe28d538463219a717d2f8ab7cff739a0dcbc635883472f677df55e325`).
- Conformément à R-468/R-609 : le refus est définitif dans ce run, jamais contourné ni reformulé.

### Arrêt du tour
Code de sortie 2 (porte fermée) : la cellule E3-T1-conception-A est bloquée. Le collisionneur v2.6 ne continue pas les tours T2 (red team) et T3 (riposte) tant que l'arbitre n'a pas tranché.

## Dépense

| Poste | Coût USD |
|---|---|
| Contrôle v1 (échoué) | 0,001 |
| Contrôle v2 (réussi) | 0,001 |
| Tour T1 conception | 0,75 |
| **Total session** | **0,75** |
| **Reste sur le plafond GO** | **24,25** |

## Arbitrage demandé à Lazar

Options pour continuer les tours T2 et T3 :

1. **`--accepter-absence` pour A (Fable) sur T1** : le collisionneur continue avec B (Opus) et C (Argon) sur les 3 tours. Perte : une voix sur trois (Fable) au tour T1, mais les tours T2 et T3 auront trois voix si Fable ne refuse pas sur les prompts augmentés (le contexte change avec les sorties du tour précédent). Risque : Fable refuse aussi sur T2/T3 (même question de fond, mêmes termes).

2. **Nouveau run complet avec question reformulée** (R-609) : remplacer « organisme saboteur » et les termes déclencheurs dans une v2 des faits et de la question. Le run-pilier-attaque-e3-v1 est clos ; un nouveau run `run-pilier-attaque-e3-v2` reprendrait de zéro. Coût : tout le T1 est perdu (0,75 USD) ; le nouveau run coûtera jusqu'à 24,25 USD.

3. **Arrêt** : si le fond lui-même est en cause (R-468 borne 5).

## Prompt caching (demande de Lazar)

Analyse effectuée sur la documentation Anthropic. Le prompt caching n'apporte presque rien au collisionneur v2.6 dans sa forme actuelle :
- Le cache est par modèle : Fable et Opus ne partagent pas de cache.
- Dans un tour, chaque modèle est appelé une seule fois (A=Fable, B=Opus, C=Argon).
- Entre les tours, le prompt change (contexte augmenté des sorties précédentes).
- Argon (Gemini) n'a pas de prompt caching Anthropic.
- L'entrée est ~5 100 jetons par cellule ; économie par cache hit : ~0,05 USD.
- Modifier un outil scellé (R12 -> v2.7) pour un gain de quelques centimes n'en vaut pas le risque.
- Le prompt caching sera pertinent pour un collisionneur futur à plus de cellules ou avec des appels parallèles au même modèle.

## Fichiers produits
- `donnees/ideation-pilier-attaque-v1` : `run-pilier-attaque-e3-v1/` (24 fichiers, commit `48c27cb`).
- Conformité : aucune recette, aucune lecture de `donnees/bras-attaque*` ni `donnees/mode-tenu-a-l-ecart*`, aucun refus contourné.

## Prochaine action
Attente de l'arbitrage de Lazar sur les options 1, 2 ou 3 ci-dessus.
