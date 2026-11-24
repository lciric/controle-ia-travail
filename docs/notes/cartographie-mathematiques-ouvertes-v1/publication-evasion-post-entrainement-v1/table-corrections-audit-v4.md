# Table de la v4 du paquet de publication — d'où vient chaque changement

- **Objet** : v4 du paquet de publication sur l'évasion sous filtrage pendant l'entraînement après pré-entraînement (billet de Yair Halberstadt). Rien n'est écrasé ; la v2, la v3 de référence (`b1006d58`) et la variante B (`variante-b-v3-session-fille-2/`) restent en place.
- **Mandat** : la mère, le 24 novembre 2026. La v4 reprend la variante B, plus son correctif 1, plus les cinq reports recommandés par la vérification de fidélité. Elle retire partout la nécessité des hypothèses H1 à H3 et remplace le test de mort par une version qui ne réécrit pas un JSON scellé.
- **Session** : fille 2 du papier D, Opus 5.5. **Non diffusé.**

## Pièces v4

| Pièce | Fichier v4 | Construit à partir de |
|---|---|---|
| Billet | `billet-lesswrong-evasion-post-entrainement-en-v4.md` | variante B, `…-en-v3-correctif-1.md` |
| Commentaire de réponse | `commentaire-reponse-yair-halberstadt-lesswrong-en-v4.md` | variante B, `…-en-v3-correctif-1.md` |
| Manuscrit | `manuscrit-arxiv/main-v4.tex` et `main-v4.pdf` (11 pages) | variante B, `main-v3-correctif-1.tex` |
| Page du dépôt | `github-page/README-v4.md` | variante B, `README-v3.md` |
| Script de vérification | `verifier_exemples_papier_v4.py`, sortie `exemples-verifies-papier-v4.json` | variante B, `verifier_exemples_papier_v3.py` |
| Test interne | `../test_mort_halberstadt_v3.py` | variante B, `test_mort_halberstadt_v2.py` |
| Note d'élucidation (interne) | `../erratum-2-elucidation-loi-halberstadt-post-entrainement-v1.md` | défaut B-1 de la vérification |
| Compagnon d'empreinte de la contre-lecture de Carbon | `contre-lecture-carbon-high-publication-v1.md.v2.sha256` (déjà versé par la v3 de référence, propre, `ae7ab7d1…`) | report n° 2 ; l'ancien compagnon reste en place, la mère tranche |

## Les dix corrections de l'audit

Elles sont portées comme dans la variante B. Voir `variante-b-v3-session-fille-2/table-corrections-audit-v3.md` : la vérification de fidélité l'a trouvée exacte sur les vingt cases sondées. Les lignes et sections y sont les mêmes, à deux changements près, décrits ci-dessous.

## Changements de la v4 par rapport à la variante B

| N° | Origine | Changement | Où |
|---|---|---|---|
| 1 | Défaut B-1 (majeur) et report n° 1 | Paragraphe H1 à H3 retiré. Ouverture neuve : ni exhaustivité, ni nécessité, ni suffisance revendiquées ; le cas d'une covariance positive sous la pénalité est cité | manuscrit, ouverture de la section 3 ; billet, ouverture du § 4 ; erratum 2 de la note |
| 2 | Défaut B-2 | « < 1 » remplacé par « vaut un seulement si $\beta_v = 0$ » | manuscrit, point 4(a) et proposition ; billet, § 3 point 3 |
| 3 | Défaut B-3 | $\pi_A(\Pi_h) = 0{,}827382$ (et non 0,827379) | manuscrit, remarque sur la niche et table 3 ; billet, paragraphe sur la niche |
| 4 | Défaut B-4 et report n° 3 | Phrase d'antériorité : Price, Robertson, Fisher, Korbak, Perez et Buckley 2022 | commentaire |
| 5 | Report n° 4 | À récompenses égales, la part furtive parmi les tricheurs sous le rejet pur vaut $\beta_f p_f/(\beta_v p_v+\beta_f p_f)$ pour tout $\eta$, donc aussi à la limite | manuscrit, point 4(a) ; billet, § 3 point 3 ; script, contrôle exact sur quatre valeurs de $E$ |
| 6 | Report n° 5 | L'opérateur A coïncide avec un entraînement sans moniteur suivi d'un rejet unique à l'inférence : $\pi_A \propto \beta\,\pi_{\text{no}}$ | manuscrit, remarque « Operator A is a modelling choice » ; billet, § 2 ; commentaire, point 2 ; README ; script, contrôle exact |
| 7 | Report n° 2 (défaut B-5) | Le compagnon propre `.v2.sha256` de Carbon est désigné ; l'ancien n'est pas touché | présente table |
| 8 | Défaut R-2 de la v3 de référence | Test de mort sans réécriture : chemin de sortie exigé, refus d'écraser, aucune écriture à côté du script | `../test_mort_halberstadt_v3.py` |
| 9 | Hygiène | Noms et références internes passés en v4 (script, sortie, manuscrit, README) | toutes les pièces v4 |

## Vérifications faites par la session

- Le script v4, lancé sur une copie avec `python3 -I`, produit la même sortie avec et sans `--out`, et refuse d'écraser. Ses tables et ses contrôles exacts sont identiques à ceux de la variante B, comparés par programme ; les contrôles nouveaux (6 et 5 ci-dessus) passent.
- `test_mort_halberstadt_v3.py` sur une copie : six essais réussis. Sans chemin, il s'arrête sur un message d'usage ; avec un chemin existant, il refuse d'écraser.
- Le manuscrit v4 compile en deux passes, sur 11 pages. Il garde deux boîtes trop larges, de 9,9 et 3,8 points, déjà présentes avant.
- Aucune des pièces publiques v4 (billet, commentaire, manuscrit, README) ne cite plus H1, H2 ou H3.

## Réserves

1. Références à vérifier sur PDF (R7) avant diffusion : Price 1970, Robertson 1966, Fisher 1930, Korbak et al. 2022 et 2025, Bailey et al. 2024.
2. L'avis d'opportunité et la feuille de route v2, hors du paquet, gardent encore « classification exhaustive en 3 régimes ».
3. La v4 doit encore être vérifiée par un contre-lecteur, avec une boucle au plus.
