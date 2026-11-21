# Rapport du développeur — corrections de la contre-lecture du code de commande de la relecture, version 2 — v1

- **Nature** : rapport de corrections d'une pièce de classe B (code). Écrit par Claude Fable 5.2, développeur, le 21 novembre 2026, sous le mandat `7c52ca65…`. Suite du rapport `rapport-developpeur-commande-lecture-v2-v1.md` (`a9b3ce5ad836a1194b0ba8af8b40fec2595c1a08cadf4cd95840a51a368789da`).
- **Contre-lecture portée** : `cl-commande-v2/contre-lecture-commande-lecture-v2-v1.md` (`350d847190d5c9e5a350ff06b4b9213f479d67662aaa4bbebadc4dd288e14077`, égale à son compagnon), verdict « conforme après ces corrections », quatre corrections non bloquantes. J'ai lu aussi `cl-commande-v2/muter.py` ; rien d'autre de ce dossier.
- **Verdict** : les quatre corrections sont portées, dans le seul fichier d'essais ; les deux mutations qui survivaient (X01, X02) rendent chacune un essai rouge.
- Aucune dépense, aucune commande au loueur, aucune clé, rien poussé, aucun commit hors de l'arbre de commande.

## 1. Commit de commande neuf

- **`5402367e5b62c8ac294c55d5cc0230ebdfbaa457`**, un seul commit au-dessus de `76c608b61d52549d4e0dceb9d07be0c5bea273f8`.
- `git diff --name-status 76c608b6 HEAD` : une ligne, « M tests/test_commande_lecture_v2.py ». `git diff --name-status c76e7916 HEAD` : les trois mêmes « A ». Arbre de travail propre.

| fichier | sha256 | changé ? |
|---|---|---|
| `scripts/lancer_b5f_lecture_v2.sh` | `c07fc1244860aa9795b3c5b610ddc78115f58c818ecb25b9aa2fcfae87aabcbf` | non, à l'octet |
| `src/controle_ia/barreau5_familles/commande_lecture_v2.py` | `c6c5d11c04f337c789c7f5a289d5190f51772b4ff96893499a8a5d07bc565ef0` | non, à l'octet |
| `tests/test_commande_lecture_v2.py` | `824522047421f9e8e173ebad520c7fc1b0504d8ddac903a71e4e1a80e103336a` | oui (avant : `535e7195…`) |

La citation de `GO-LECTURE-B5F` doit porter ce commit neuf, et non plus `76c608b6…`.

## 2. Correction par correction

1. **Format de la citation, fin de chaîne** (`test_d_format_de_la_citation_lu_a_la_lettre`) : trois artefacts ajoutés, `sain + "0"` (rapport de 65 signes), `sain + "xyz"`, `sain + " note sans point-virgule"`. Le motif attendu de tous les artefacts de format est resserré sur « ne cite pas, une fois et à la lettre ».
2. **Répétition à 0,30 USD par Go et par mois** (`test_portee_repetition_par_le_corps_recompose_…`) : cas sain ajouté, par `exiger_offre_lecture_v2` (valeur rendue) et par le corps recomposé (commande rendue, égale à l'octet à celle de la version 1). L'essai affirme que 0,30 rend 0,0616 à 150 Go et rendrait 0,1233 à 300 Go.
3. **Motif propre à la version 2** (`test_d_ligne_de_l_accord_de_lecture_sans_la_citation`) : `match` porté de « GO-LECTURE-B5F » à « ne cite pas, une fois et à la lettre ».
4. **Frontière 299/300 du disque** (`test_memes_autres_bornes_…`) : le cas `{"disk_space": 299}` est rendu, refusé pour « decisif » et admis pour « repetition », dans les deux versions ; 149 est gardé pour les deux plans. Deux essais de plus au compte.

## 3. Mutations du contre-lecteur, rejouées contre le fichier corrigé (`sortie-06-mutations-du-contre-lecteur-X01-X02.txt`)

| mutation | avant | après |
|---|---|---|
| X01, disque fixé à 300 dans la formule du stockage | survivait | **rouge** : `test_portee_repetition_par_le_corps_recompose_la_borne_de_0_08_n_a_pas_bouge` (1 échoué, 112 passés, 1 sauté) |
| X02, `fullmatch` remplacé par `search` | survivait | **rouge** : `test_d_format_de_la_citation_lu_a_la_lettre` (1 échoué, 112 passés, 1 sauté) |

Jouées dans l'arbre de commande, module rendu à l'octet après chacune (empreinte `c6c5d11c…` vérifiée). Je n'ai pas rejoué mes 21 mutations ni X03 à X07 : les essais qu'elles faisaient rougir n'ont pas été desserrés.

## 4. Comptes d'essais au commit `5402367e` (`sortie-07-essais-au-commit-corrige.txt`)

| fichier | résultat |
|---|---|
| `tests/test_commande_lecture_v2.py` | 113 passés, 1 sauté (le registre réel, sans sa variable) |
| le même, registre réel seul | 1 passé |
| `tests/test_barreau5_familles_relecture_v1.py` | 24 passés |
| `tests/test_lancer_b5f_lecture_v1.py` | 43 passés |
| `tests/test_barreau5_familles_engagement_v1.py` | 23 passés |

## 5. Disque

Chaque passe a pris `--basetemp` dans un seul dossier (`dev-commande-v2/pt-unique`), vidé aussitôt après ; aucun dossier `pt*` ne reste. Mon premier passage avait laissé 21 dossiers de mutations, environ 20 Go, supprimés par la coordinatrice : c'était ma faute.

## 6. Ce qui reste

- La vérification de ces corrections par le même contre-lecteur.
- Les remarques hors liste du contre-lecteur (lien symbolique admis par (c) ; « é » composé dans « vérifiée » ; commit de la marche présent dans le dépôt de l'arbre de commande) : aucune correction demandée, aucune portée.
- Non fait, comme avant : essais du paquet entier, exécution sur le dépôt réel, mise à jour de `registres/go.md` dans l'arbre de commande.
