# Proposition de liste fermée des « autres questions ouvertes » pour la passe X (option d) — v1

Écrit par la session de l'organisme le 2026-11-22T11:28Z, pour la mère, qui la porte à Lazar.

- **Source** : copie de `main` au commit `665748f9`, dossier `docs/notes/demandes-fable-api-2026-11-22-v1/`.
- **Retenu** : les questions neutres **servies**, c'est-à-dire les fichiers `question-neutre-…-servie-vN.md`, à leur dernière version.
- **Garde de motifs** : celle de l'outil de relecture (`garde_motifs_ligne`, `relecture_fable_api_v3.py`, `95bea064…`), appliquée ligne à ligne.
- **Ancrage** : un contrôle par programme seulement. Il cherche les candidats de modes nommés (`K1` à `K4`), les tournures « candidat de mode » et « mode candidat », et le mot « quarantaine ». Il ne remplace pas une lecture.

## Base de la pièce fusionnée (déjà décidée)
| pièce | empreinte | signes | motifs | ancrage |
|---|---|---|---|---|
| question-neutre-modes-attaque-servie-v1.md | `02ad3d76ae90…` | 1 121 | 0 | 0 |
| question-neutre-modes-attaque-ajout-organisme-v1.md | `8c54752fef44…` | 374 | 0 | 0 |

## Autres questions ouvertes proposées
| question servie | empreinte | signes | garde de motifs | ancrage | proposition |
|---|---|---|---|---|---|
| question-neutre-billet-drapeau-servie-v2.md | `06c7d269e44c…` | 1 196 | 0 motif | 0 | **retenir** |
| question-neutre-coeurs-algorithmiques-servie-v2.md | `0ad1d1b7ee7e…` | 1 496 | 0 | 0 | **retenir** |
| question-neutre-etau-equipe-rouge-servie-v3.md | `bcbec4c4bc3a…` | 1 526 | 0 | 0 | **retenir** |
| question-neutre-questions-concurrents-servie-v1.md | `96dc184536f2…` | 872 | 0 | 0 | **retenir** |
| question-neutre-theoreme-negatif-servie-v2.md | `347c8bb4e8ea…` | 1 432 | 0 | 0 | **retenir** |
| question-neutre-tirage-au-hasard-servie-v1.md | `7bd84fe8ad8b…` | 825 | 0 | 0 | **retenir** |
| question-neutre-lot-quarantaine-servie-v1.md | `1d4ee016c2a7…` | 1 636 | 0 | **1 (« quarantaine »)** | **écarter** |

- **Pourquoi écarter la question du lot en quarantaine** :
  - elle porte sur un lot tenu à l'écart ;
  - elle est orientée faiblement au test de devinette (GO-2026-11-22-37) ;
  - la servir aux proposeurs de la passe X heurterait la règle d'ancrage (K-1 de l'additif) et le cloisonnement de la matière première.
- **À trancher** : les questions neutres non servies (`question-neutre-generale-v2`, `papier-a-v2`, `papier-b-v2`, `papier-c-v2`, `revendications-v2`, `taches-sabotage-v2`, `these-boite-blanche-v2`, `etau-v2`) ne sont **pas** proposées, faute d'un passage par le collisionneur. Lazar peut en ajouter ; chacune passerait alors les deux contrôles.

## Pièce fusionnée et pire coût
- **Taille** : base (1 495 signes) plus les six questions retenues (7 347 signes), soit environ **8 840 signes**, ou **2 500 à 3 000 jetons** d'entrée de plus par requête, d'après le rapport d'à peu près 3 à 3,5 signes par jeton du français.
- **Pire de la ligne** : d'après l'additif v2 (X-10), il est P_X = 36,30 + 3 × max(6,05 ; pire Google), soit **au moins 54,45 USD**. Le pire d'une tentative de proposeur (6,05) tient surtout à la sortie maximale.
- **Effet de l'entrée en plus** : au plus environ 0,05 USD par tentative, au prix d'entrée le plus haut supposé de 15 USD par million. Sur 9 tentatives, cela fait environ **+0,45 USD**, donc un pire d'environ **54,9 USD**. Ce chiffre tient sous la ligne de 55 USD si le pire Google ne dépasse pas 6,05.
- **Réserve 1** : ce n'est pas une mesure. Le chiffre exact demande le plafond d'entrée du devis et le prix d'entrée de chaque espèce. Il sera calculé par script dans la v3 de l'additif.
- **Réserve 2** : sept questions dans une seule requête demandent plus de sortie. Si le plafond de sortie du devis ne suffit pas, il faut le relever, et le pire de 6,05 par tentative monte. Dans ce cas, la ligne de 55 USD ne suffit plus.
