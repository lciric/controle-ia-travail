# Table des corrections de l'audit indépendant portées sur le paquet de publication v3

- **Objet** : paquet de publication sur l'évasion sous filtrage pendant l'entraînement après pré-entraînement (billet de Yair Halberstadt), passé de la v2 à la v3.
- **Source des corrections** : rapport d'audit indépendant, liste fermée du § 6 (`docs/notes/audit-evasion-post-entrainement-v1/rapport-audit-evasion-post-entrainement-v1.md`, branche `audit/evasion-post-entrainement-v1`, commit `d6c13162`, verdict « tient avec réserves »).
- **Session** : fille du papier D, Opus 5.5, 24 novembre 2026, branche `papier-d/evasion-post-entrainement-v1`. Aucune pièce v2 n'est modifiée ; tout est en v3 (règle des versions).
- **Statut** : non diffusé. Diffusion et dépôt public suspendus jusqu'à la vérification de fidélité par un contre-lecteur neuf, puis au geste de Lazar.

## Pièces v3

| Pièce | v2 (inchangée) | v3 |
|---|---|---|
| Billet | `billet-lesswrong-evasion-post-entrainement-en-v2.md` | `billet-lesswrong-evasion-post-entrainement-en-v3.md` |
| Commentaire de réponse | `commentaire-reponse-yair-halberstadt-lesswrong-en-v2.md` | `commentaire-reponse-yair-halberstadt-lesswrong-en-v3.md` |
| Manuscrit | `manuscrit-arxiv/main-v2.tex` | `manuscrit-arxiv/main-v3.tex` et `main-v3.pdf` (11 pages) |
| Page du dépôt | `github-page/README-v2.md` | `github-page/README-v3.md` |
| Script de vérification | `verifier_exemples_papier_v2.py` | `verifier_exemples_papier_v3.py`, sortie `exemples-verifies-papier-v3.json` |
| Test interne | `../test_mort_halberstadt_v1.py` | `../test_mort_halberstadt_v2.py` |
| Note d'élucidation (interne) | `../elucidation-loi-halberstadt-post-entrainement-v1.md` | `../elucidation-loi-halberstadt-post-entrainement-v1-erratum-1.md` |

## Correction de l'audit → endroit modifié

| N° | Correction (§ 6 de l'audit) | Billet v3 | Commentaire v3 | Manuscrit v3 | README v3 | Script et autres |
|---|---|---|---|---|---|---|
| 1 | Découplage : sous le rejet pur, variation exacte $\operatorname{Cov}/\mathbb{E}$, non-hausse si et seulement si covariance négative ou nulle, placement hors boucle ni suffisant ni nécessaire ; sous la pénalité, covariance négative ou nulle nécessaire mais non suffisante, indépendance ou association négative suffisante | § 1 (quatrième puce), § 4 point 2 réécrit avec les trois contre-exemples, § 5 point 4 | puce R2 réécrite (« covariance, not placement ») | résumé ; contribution 3 ; énoncé de R2 (titre, conséquence « si et seulement si », nécessité sous B) ; remarque nouvelle « Placement is not covariance » ; paragraphe d'ouverture de la section 3 ; limitations, point 2 | Théorème 2, puce R2 | script : contre-exemples exacts `decoupling_*` ; note : erratum 1, points 3 et 8 |
| 2 | Dilemme : dans la niche, la pénalité dépasse le rejet pur en furtif exactement quand elle le dépasse en honnêteté ; moins de triche totale | § 1 (troisième puce), § 3 point 4, lignes « High ΔR » et niche | point 3 | résumé ; contribution 2 ; point 4(c) du Théorème 1 complété ; fin de la preuve ; remarque nouvelle « The niche inversion has two sides » ; légende et texte de la table 3 | Théorème 1, dernière puce | script : `niche_equal_odds_exact` (2 000 tirages rationnels) ; note : erratum 1, point 10 |
| 3 | « Collapses to stealth » remplacé : l'honnêteté s'effondre, la masse va aux tricheurs, part furtive vers $\beta_f p_f/(\beta_v p_v+\beta_f p_f)$ | § 1 (première puce), § 3 point 3 avec l'exemple $3/128$ | point 2 | résumé ; point 4(a) du Théorème 1 avec l'exemple $3/128$ ; proposition, cas $C=0$ (« pas le seul cas fatal ») | Théorème 1, deuxième puce | script : `collapse_limit_stealth_share_A` |
| 4 | Opérateur de rejet pur présenté comme un choix de modèle : prime $\eta^{-1}\log\beta$ ; rejet répété à barrière non évanescente | § 1 (deuxième puce), § 2 paragraphe « Why Operator A is a choice, not a law » (chiffres +195,3 et −92,1), § 5 point 2 | point 2 (« Caveat ») et définition « modelled as conditioning » | résumé ; contribution 2 ; remarque nouvelle « Operator A is a modelling choice » ; phrase sur $\eta = 0$ ; titre du point 4 du Théorème 1 ; limitations | introduction et Théorème 1, troisième puce | script : `repeated_rejection_sensitivity` ; note : erratum 1, point 1 |
| 5 | Vérification : retrait de « every theorem and numerical table is verified in exact rational arithmetic » ; essais décrits tels qu'ils sont ; plus d'argument « 0 contre-exemple sur 14 000 » | § 1 fin et pied du billet : « the proofs carry the results; the script only checks… » ; plus aucune mention de 14 000 | dernière ligne | résumé (dernière phrase) ; contribution 4 ; section 5 réécrite (« What the Companion Script Checks ») ; « illustrate » au lieu de « confirm to full precision » | rubrique « Reproduction » réécrite | script : docstring et sortie `float_regression_checks` avec la limite de chaque famille (R2 cas particulier, R3 tautologique) ; note : erratum 1, point 6 |
| 6 | Nécessité et exhaustivité retirées | § 4 : « arises in particular when », « we do not claim these are the only ways » | « not claimed exhaustive » | titre de section « Three Escape Mechanisms » ; paragraphe d'ouverture réécrit ; titre de R1 « exact criterion for dominance » ; contribution 3 « not claimed exhaustive » | « not claimed exhaustive » | note : erratum 1, point 2 |
| 7 | « Universal » restreint au rejet pur ; enrichissement sous la pénalité seulement à récompense égale entre tricheurs | § 1 première puce, § 3 point 1 (exemple 0,8810 → 0,8748) | point 1 réécrit (l'ancienne ligne 9 étendait l'enrichissement à B sans réserve) | résumé ; titre du point 1 du Théorème 1 « under Operator A » ; phrase « This holds for Operator A only » ; « with equal reward » ; remarque nouvelle « Enrichment under Operator B needs equal rewards » | Théorème 1, première puce | script : `heterogeneous_reward_B_counterexample` |
| 8 | Antériorité : Price, Robertson, Fisher pour les identités ; Korbak et al. 2022 pour la forme de Gibbs ; recommandation « sondes hors boucle » présentée comme déjà publiée | § 2 (Korbak 2022), § 3 point 1 (Price, Robertson, Fisher), § 4 point 2 (Baker 2025, Korbak 2025), § 5 « Prior work » | point 1 et puce R2 | introduction et contribution 2 ; phrase après les opérateurs ; remarque « Placement is not covariance » ; bibliographie : `price1970`, `robertson1966`, `fisher1930`, `korbak2022`, `korbak2025`, `bailey2024` | rubrique « References for prior work » | note : erratum 1, point 9 |
| 9 | Petits bords : $p_f = 0$ hors domaine ; rapport des seuils non défini si $p_h\beta_h = p_f\beta_f$ (et négatif si $\beta_f/\beta_h < p_h/p_f < 1$) ; $\pi_0(\mathcal S) > 0$ requis ; lien pièges–ratio critique seulement pour $\beta_h = 1$ | § 4 points 1, 2 et 3 | — (trop fin pour un commentaire) | R1 (phrase sur $p_f = 0$) ; R2 ($\pi_0(\mathcal S)>0$) ; R3 (honnête non intercepté sur les pièges) ; remarque R3 ($\beta_h = 1$) ; proposition (rapport non défini ou négatif) | — | note : erratum 1, points 4 et 5 |
| 10 | Hygiène : sortie du script hors du dossier scellé ; `c_seuil` corrigé ; « closed-form » retiré pour le seuil d'amplification sous B ; compagnon `.sha256` de Carbon à chemin étranger | § 3 point 2 (« implicit, not closed-form ») | — | titre du point 3 du Théorème 1 « implicit, not closed-form in ΔR » | commande avec `--out` | script v3 : n'écrit rien sans `--out`, refuse d'écraser ; `test_mort_halberstadt_v2.py` : terme $\rho\varepsilon(\tau-\delta)$ rétabli, chemin de sortie exigé, refus d'écraser. **Compagnon Carbon : non corrigé** (voir réserves) |

## Corrections hors de la liste fermée, tirées des § 3.1 et § 4 de l'audit

- **Portée** (règle anti-faux-gap) : « This note resolves the question exactly » remplacé par « answers a restricted version » ; la question de la généralisation (que deviennent $p_f$ et $\beta_f$ quand on entraîne) est déclarée hors du modèle dans le billet (§ 1, § 5), le commentaire (première phrase), le manuscrit (résumé, introduction, limitations) et le README.
- **Cas $\beta_f > \beta_h$** (fausses alarmes sur l'honnête) signalé comme exclu par hypothèse dans le billet (§ 2) et le manuscrit (limitations).
- **Régime des pièges** : il exclut les tricheurs fréquents, pas les rares ; l'honnêteté n'est pas garantie optimale (audit § 3.7) — billet § 4 point 3, commentaire, remarque R3 du manuscrit.
- **Lean** : la phrase du manuscrit est réduite à « left for future work; no formal proof is claimed ».

## Vérifications faites par la session

- Le script v3, lancé sur une copie avec `python3 -I`, rend deux sorties identiques octet pour octet (avec et sans `--out`) ; il refuse d'écraser un fichier existant.
- Les tables et l'exemple rationnel de la sortie v3 sont **identiques** à ceux de la sortie v2 (`verified_examples` et `exact_rational_variance_identity` comparés par programme).
- Les chiffres nouveaux du script concordent avec ceux de l'audit : $37/50$, $6/25$, $7/12$, $19/30 \to 0{,}770$, $3/128$, $+195{,}3$ et $-92{,}1$, $0{,}8810 \to 0{,}8748$.
- `test_mort_halberstadt_v2.py` s'exécute sur une copie sans échec d'assertion.
- Le manuscrit v3 compile (`pdflatex`, deux passes, 11 pages) ; il reste deux boîtes trop larges de 9,9 et 3,8 points, dont la première vient de la v2.
- Métadonnées vérifiées sur arXiv (titre et premiers auteurs) : 2205.11275 (Korbak, Perez, Buckley), 2507.11473 (Korbak, Balesni…), 2412.09565 (Bailey, Serrano…).

## Réserves

1. **Références à vérifier sur PDF (R7) avant diffusion** : Price 1970 (Nature 227:520–521), Robertson 1966 (Animal Production 8:95–108), Fisher 1930, et les trois références arXiv ci-dessus (seules les métadonnées ont été lues). Aucun chiffre n'en est tiré.
2. **Compagnon `.sha256` de la contre-lecture Carbon** : il porte toujours un chemin de machine étrangère et fait échouer `verifier-arbre` sur ce fichier (l'empreinte, `ae7ab7d1…`, concorde). Sa réécriture a été refusée par le garde-fou de la session (écrasement d'une pièce de scellement). Décision renvoyée à la mère.
3. **Avis d'opportunité** (`avis-opportunite-arxiv-pour-lazar-fr-v1.md`) et **feuille de route v2** : hors du paquet ; ils gardent « classification exhaustive en 3 régimes » et « zéro conjecture gonflée ». Non corrigés ici ; à lire avec le présent tableau.
4. Les pièces v3 n'ont pas encore été contre-lues : la vérification de fidélité par un sous-agent Opus neuf est l'étape suivante.
