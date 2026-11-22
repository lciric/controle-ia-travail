# Rapport du développeur — correctif 0022 : vitesse mesurée en marche, liste de l'étalonnage v7 — v6

Date : 2026-11-22. Pièce d'instrument (classe B). Même développeur (Claude Opus 5.5). Ce rapport complète les v1 à v5, intactes.
Rien poussé, rien dépensé, aucune machine, aucun modèle téléchargé.

- Base : `6696aca1f` (0021, aujourd'hui sur le distant sous `prep/iib-tirage-carte-v1`).
- **Tête `4f538eefab759318f42f3a2c049465a91a3465d7`, arbre `a814f0701f413ba38f37de781929f4f24610cbb7`.**
- Correctif `0022-…patch`.

## (2) Les marques actuelles donnaient-elles déjà la vitesse ? Non
- La marque de lot de l'étalonnage portait `etape`, `phase`, `lot`, `episodes`, `actions_oracle` et `replis`, mais **aucune durée**.
- Les durées n'étaient écrites qu'**à la fin**, dans `etalonnage-oracles-iib-v5.json` (`durees`) et dans les rapportés (`duree_d_une_action_d_oracle_par_oracle_h`).
- Une marque de progrès n'est ni scellée ni poussée : elle va au journal de l'instance, que l'amorce relaie à la surveillance.

## Ce qui est écrit (0022)
- **`lanceur_v5.vitesse_du_premier_lot`**, appelée par `verser` après le premier lot (les honnêtes : génération puis les deux oracles), juste après la poussée de ce lot.
- Elle écrit et scelle **`diag/<run>/vitesse-premier-lot-iib-v5.json`**, puis le pousse par le versement (« vitesse du premier lot »). Le fichier contient :
  - `generation_s_par_episode` ;
  - `oracle_P_s_par_action` et `oracle_N_s_par_action` (chronométrés par oracle, comme pour le plafond de tours) ;
  - les comptes (épisodes générés, actions de chaque oracle) ;
  - la méthode de tirage du modèle.
- Il ne contient **aucun texte, aucun jeton, aucune sortie d'oracle**.
- Une marque de progrès `etape=vitesse lot=1 generation_s_par_episode=… oracle_P_s_par_action=… oracle_N_s_par_action=…` est conforme au motif de l'amorce et à aucun motif interdit ; elle est donc relayée à la surveillance.
- Une durée non mesurée est un refus, jamais un zéro inventé.
- **Liste figée de l'étalonnage v7** (`scripts/tests-cibles-iib-v5-v7.txt`) = v6 plus `tests/test_tirage_carte_v1.py`. L'amorce de l'étalonnage la cite, avec son empreinte en dur, changement (i). Le grain du contrôle est le fichier : l'amorce n'admet que des chemins de fichiers. Le fichier entier entre donc (14 essais), dont l'essai de déterminisme sur la carte, sauté sur processeur, joué sur la machine.
- **Essais** :
  - `test_vitesse_du_premier_lot_scellee_sans_texte` : fichier scellé, clés exactes, durées positives, aucun texte ; artefact, une durée nulle est refusée ; calcul juste sur un chronomètre connu ; marque conforme aux motifs de l'amorce ;
  - versement : 29 poussées (28 lots plus la vitesse), la vitesse est sur l'origine ; quand l'origine refuse, la vitesse est refusée aussi, et l'arrêt tombe après le lot 2 ;
  - liste v7 citée par l'amorce, et égale à v6 plus le fichier du tirage ;
  - répétition locale (`sortie-repetition-locale-0022-courte-v1.txt`) : code 0, 29 poussées vérifiées, une marque de vitesse, le fichier de vitesse sur la branche.

## (3) Nombres attendus
| liste | machine à carte (torch) | processeur avec torch | processeur sans torch |
|---|---|---|---|
| étalonnage v7 (`TESTS_ATTENDUS`) | **311** (297 + 14) | 310 passed, 1 skipped | 297 passed, 1 skipped |
| course v2 | **313** (297 + 2 moteur + 14) | 312 passed, 1 skipped | — |
| fichiers de la v6 seuls | 297 | 297 | 297 |

Sur la machine, `TESTS_ATTENDUS=311` pour l'étalonnage rejoué sous `IIB_TIRAGE=carte`, et 313 pour la course. La répétition locale à `--liste-figee` ne passe plus que sur une machine qui a torch et une carte. La suite courte, elle, passe.

Rejoué sur ce poste : `sortie-essais-p1-v6.txt`, avec (A) la v7 sans torch et (B) la v7 avec torch.

## Livrables v6
- `0022-…patch` ;
- ce rapport ;
- `sortie-essais-p1-v6.txt` ;
- `sortie-repetition-locale-0022-courte-v1.txt`.

Arbre final : `a814f0701f413ba38f37de781929f4f24610cbb7`.
