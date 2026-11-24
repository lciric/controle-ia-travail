# Erratum 1 à la table de la v4, et correctif 1 de la v4 (boucle unique après la seconde vérification)

- **Source** : seconde vérification de fidélité par le même contre-lecteur Opus. Verdict : **la v4 est fidèle**. Il ne relève aucun défaut bloquant ni majeur, et trois réserves mineures. Son rapport est versé dans `variante-b-v3-session-fille-2/rapport-fidelite-v4-contre-lecteur-opus-v1.md`.
- **Règle** : la v4 reste telle quelle. Les corrections vont dans des fichiers suffixés `-correctif-1` (`_correctif_1` pour le script). Le présent erratum prime sur `table-corrections-audit-v4.md` pour le point qu'il corrige.
- **Session** : fille 2 du papier D, 24 novembre 2026. **Non diffusé.**

## Erratum à la table v4

Ligne 8 de la table des changements : l'affirmation « aucune écriture à côté du script » est inexacte. `test_mort_halberstadt_v3.py` exige un chemin de sortie et refuse d'écraser tout fichier existant ; il ne peut donc réécrire **aucun JSON scellé**. En revanche, il accepte un fichier **neuf** dans son propre dossier, si on lui en donne le chemin. Il faut lire : « chemin de sortie exigé, refus d'écraser ; aucun fichier existant ne peut être réécrit ».

## Correctif 1 de la v4

| Réserve | Correction | Fichiers |
|---|---|---|
| 1. Le contre-exemple « covariance positive sous la pénalité » n'apparaissait dans aucune pièce publique ni dans le script ; « does not by itself » était ambigu | « need not » à la place. Le contre-exemple figure désormais dans la remarque sur le découplage du manuscrit et dans l'ouverture du § 4 du billet : $\beta_{\text{boucle}} = (1/10, 1/2, 9/10)$, $\beta_{\text{audit}} = (1/10, 19/20, 9/20)$, covariance $+7/150$, survie à l'audit $1/2 \to 0{,}543$ ($k = 2$), puis $0{,}459$ ($k = 10$), et limite $9/20$. Le script le recalcule (covariance en fractions exactes) | `manuscrit-arxiv/main-v4-correctif-1.tex` et `.pdf` (11 pages) ; `billet-…-en-v4-correctif-1.md` ; `verifier_exemples_papier_v4_correctif_1.py` |
| 2. Table v4, ligne 8 | Erratum ci-dessus | présent fichier |
| 3. Rubrique du JSON nommée `exact_checks_v3` ; les deux contrôles nouveaux de la v4 n'existaient que comme assertions | La rubrique devient `exact_checks`. Ajout de `operator_A_equals_reweighted_unmonitored` et de `positive_cov_not_sufficient_B` dans la sortie | `verifier_exemples_papier_v4_correctif_1.py`, sortie `exemples-verifies-papier-v4-correctif-1.json` ; `github-page/README-v4-correctif-1.md` (commandes et noms de fichiers) |

Le commentaire de réponse v4 n'est pas touché : il ne contenait pas la formule ambiguë.

**Vérifications de la session** :
- Le script corrigé, lancé sur une copie avec `python3 -I`, produit la même sortie avec et sans `--out`.
- Les chiffres du contre-exemple sont recalculés : 0,543264, 0,458875 et 0,45.
- Le manuscrit compile en deux passes ; il garde les deux mêmes petites boîtes trop larges qu'avant (9,9 et 3,8 points).

**Reste avant diffusion** : vérifier sur PDF les références (R7) ; trancher le sort de l'ancien compagnon d'empreinte de Carbon (décision de la mère) ; le geste de diffusion appartient à Lazar.
