# Compte rendu 05 — fille idéation 1, v1

Session `session_016QhUrujoj3FTuFNoYshNYB` (fille), mère `session_016QhUrrLeN21G7Z9KZobE42`.
Date : 2026-11-08, ~12:30–13:15 UTC.

## Objet

Préparation de la course d'idéation (organisme v1, pilier attaque) : composition, script de pré-vol, sonde simulée, liste blanche, validation manuelle. Zéro dépense. Le lanceur externe n'a pas pu être exécuté (classifieur de permissions : « Code from External »).

## Travail accompli

### 1. Clonage et lecture du lanceur

Le dépôt `ideation-organism` a été cloné en lecture seule (`ideation-organism-lecture`). La chaîne de lanceurs a été tracée : `ideation_v8.py` → `v7` → `v6` → `v5` → `v4` → `v2`. Sans `--course-2` ni `--pre-pilote`, toutes les versions traversent jusqu'à `v2.principal()`.

Le lanceur v2 (`ideation_v2.py`, 1413 lignes) est le cœur de la course de base.

### 2. Incompatibilités de l'interface en ligne de commande corrigées

Cinq problèmes trouvés par lecture du code source, avant toute exécution :

| Point | Constat | Correction |
|---|---|---|
| `--verifier-seulement` | N'existe pas dans le lanceur v2 (seulement v5+, avec `--course-2`) | Remplacé par `--mesurer-consignes` |
| `--bras-rapporte-differe` + `--proposeur-externe` | Incompatibles (ligne 1126 de `ideation_v2.py`) | Course en deux temps : (a) course, puis (b) bras séparé |
| `--temoins` | Requis pour la course (ligne 1113), écrits par un tiers (CL31-03) | Prérequis documenté, non satisfait pour le pré-vol |
| `--moteur` | Choix : `simule` ou `claude-sdk` (pas `reel`) | Corrigé dans le script |
| `--budget` | Format `role\|modele=plafond` ; défauts du lanceur (25,3 USD) > `--budget-total-usd 15.0` | Plafonds ajustés documentés |

### 3. Composition de la course (deux temps)

Le fichier `composition-course-ideation-v1.md` documente la course en deux invocations distinctes :

**(a) Course** : 2 proposeurs Claude (opus, fable) + 1 proposeur externe (argon) + 2 juges Claude (opus-juge, fable-juge). Écrit les fiches, les notes, le classement à deux juges, les consignes en attente pour le juge externe.

**(b) Bras rapporté différé** : juge externe (argon-juge), invocation séparée après attestation de lecture humaine. Produit le classement final à trois juges (médiane).

Scénario dégradé si Fable 5.1 refuse la sonde : 2 proposeurs, 1 juge Claude + 1 juge externe, agrégation en moyenne.

### 4. Pré-vol (zéro dépense)

Script `pre-vol-course-ideation-v1.sh` en cinq étapes :

| Étape | Statut | Détail |
|---|---|---|
| 1. Empreintes | OK (manuel) | Question `29870ac9…` et synthèse `48adeac0…` vérifiées |
| 2. Sonde de la garde de refus | OK (simulé) | 3/3 modèles acceptent, mode `--simuler` |
| 3. Liste blanche | OK | 2 fichiers (question + synthèse), empreintes SHA256 |
| 4. `--mesurer-consignes` | NON EXÉCUTÉ | Classifieur « Code from External » |
| 5. `--moteur simule` | NON EXÉCUTÉ | Classifieur + témoins absents (CL31-03) |

### 5. Raison du blocage

Le classifieur de permissions en mode automatique refuse l'exécution de code Python du dépôt `ideation-organism-lecture` (catégorie « Code from External »). Le refus n'a pas été contourné ni reformulé (consigne de sûreté). Les étapes 4 et 5 doivent être exécutées manuellement hors de cette session ; les commandes exactes sont documentées dans `pre-vol/validation-manuelle-v1.md`.

### 6. Budgets

Les défauts du lanceur v2 (devis v7 quinquies) somment à 25,3 USD pour les rôles Claude, dépassant `--budget-total-usd 15.0`. Le drapeau `--tolerer-somme-plafonds-claude` serait requis avec les défauts.

Option recommandée (plafonds ajustés au scénario minimal) :

| Paramètre | Valeur |
|---|---|
| `--budget-total-usd` | 15.0 |
| `--budget-externe-usd` | 5.0 |
| `--budget proposeur_ideation\|claude-opus-5-5` | 2.5 |
| `--budget proposeur_ideation\|claude-fable-5-1` | 2.5 |
| `--budget juge_ideation\|claude-opus-5-5` | 1.5 |
| `--budget juge_ideation\|claude-fable-5-1` | 1.5 |
| Somme Claude | 8,0 < 15,0 |

## Livrables

### Sur `donnees/ideation-pilier-attaque-v1` (commit `cfed035`)

| Fichier | Empreinte SHA256 (6 premiers octets) |
|---|---|
| `organisme-v1/composition-course-ideation-v1.md` | `ccb266ed…` |
| `organisme-v1/pre-vol-course-ideation-v1.sh` | `e023cb35…` |
| `organisme-v1/pre-vol/sonde-garde-refus-v1.json` | `0fa70a60…` |
| `organisme-v1/pre-vol/liste-blanche-v1.json` | `06798985…` |
| `organisme-v1/pre-vol/validation-manuelle-v1.md` | `39d87048…` |

Chaque fichier a son compagnon `.sha256`.

### Sur `rapports/fille-ideation-1-v1`

Ce compte rendu (CR-05).

## Dépense

Aucune dépense de calcul supplémentaire. Total inchangé : 2,52 USD / 25 USD plafond (GO-2026-11-08-06).

## Éléments en attente (pour le lancement réel)

1. **Témoins plantés** (CL31-03) : écrits par un tiers (Lazar ou un agent neuf), au format `{"temoins": [...]}`, dans la liste blanche.
2. **`--mesurer-consignes`** : à exécuter manuellement hors session (commande documentée dans `validation-manuelle-v1.md`).
3. **Sonde réelle de la garde de refus** : ≈ 0,003 USD, sur le mot de Lazar.
4. **Choix du scénario budgétaire** : scénario minimal (15 USD) dans l'enveloppe, ou relèvement du plafond pour le modéré (35 USD).
5. **Mot de Lazar** : nœud de décision « dépense de calcul » pour le lancement réel (`--moteur claude-sdk`).

## Conformité

- Aucune recette (procédé de fabrication de sabotage, évasion ou tromperie) dans aucun livrable.
- Aucune lecture de `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*` ni `docs/notes/bras-attaque/`.
- Aucun refus de classifieur contourné ni reformulé.
- Aucun `git fetch` sans refspec.
- Aucune poussée vers `main` ni vers `lciric/controle-ia`.
- Lanceur externe non exécuté (classifieur « Code from External »).

## Prochaine action

Signaler à la mère les résultats de la préparation, puis attendre le mot de Lazar pour :
- Les témoins (CL31-03) ;
- La sonde réelle de la garde de refus ;
- Le lancement de la course d'organismes.
