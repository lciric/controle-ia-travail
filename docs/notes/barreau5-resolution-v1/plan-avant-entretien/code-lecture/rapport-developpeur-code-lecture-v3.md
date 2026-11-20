# Rapport du développeur du code de lecture du barreau 5 (plan « sabotage ou empreinte de l'adaptateur ») — v3

Écrit le 20 novembre 2026 par le développeur du code de lecture (Claude Opus 5.5, sous-agent de la session mère `session_01XJ6Mgr8BN6UanALsQatc5E`). Pièce d'instrument (classe B). Même mandat (`fffe5bd7…`), même texte scellé (`bdff244f…`). Suite du rapport v2 (`b9982f25…`, non modifié, R12). Corrections demandées par la vérification `verification-corrections-code-lecture-v1.md` (`fb1b7d041eb44ba45851263ec61fb3f2fa4357b271b8acd8f7bde36a2aba8cf2`, commit `3daac6deb`, lue en entier), sur la voie tranchée par la mère pour V-1 (« couper »). Les quatre couples de l'addendum (A à D) ne sont pas appliqués : l'addendum attend le mot de Lazar. Aucune donnée : modèle jouet et fichiers fabriqués ; aucun réseau, aucune dépense, aucun commit.

## En bref

- **V-1 (majeur), corrigé par la coupe** : un fichier de scores par jeton par série, `jetons/<sonde>-pli<k>/<série>.json`. Le fichier de scores ne porte plus que les scores par action. Une borne écrite de la taille d'un fichier fermé (`lecture_v1.TAILLE_MAX_FICHIER`, 90 000 000 octets) est éprouvée à l'écriture, à l'inventaire de l'instance et à la garde d'ouverture, avec cas sain et artefact. Interface, listes blanches, garde d'ouverture, mondes fabriqués des essais et amorce suivent.
- **v-1, corrigé** : `ligne_scores` n'accepte que le commit de la branche de sortie de la pièce.
- **v-2, corrigé** : le texte n'exige pas les scores par jeton des séries propres des saboteurs d'apprentissage (passage cité en section 3) ; ils sont retirés.
- **Essais** : les six fichiers de la lecture, **239 passés, aucun échec**. **Mutations v3** : 13 jouées, **13 attrapées**.
- **Plancher d'essais de l'amorce : 141** (97 + 20 + 24), au lieu de 137.

## 1. V-1 : un fichier de scores par jeton par série, et une borne écrite

Ce qui change :
- **À l'écriture** (`sondes_v1.ecrire_scores`), pour chaque sonde et chaque pli : un fichier `scores/<sonde>-pli<k>.json`, qui ne porte que les scores par action de chaque série. Pour les sondes `decisive` et `comparaison` (couche 15), un fichier par série, `jetons/<sonde>-pli<k>/<série>.json`. Avant toute écriture, chacun de ces fichiers est mis en octets. Si l'un existe déjà (R12) ou dépasse la borne, la fonction s'arrête et n'écrit rien : aucune sonde n'est laissée à moitié écrite. Chaque fichier est ensuite écrit et scellé.
- **À l'inventaire de l'instance** (`lecture_v1.ecrire_inventaire`) : la borne est revue pour chaque fichier.
- **À la garde d'ouverture** (`lecture_v1.exiger_arbre`) : la borne est revue sur la taille inventoriée de chaque fichier, avant sa taille et son empreinte. Une taille illisible est refusée.
- **Au chargement** (`lecture_v1.charger_arbre`) :
  - un fichier de scores qui porte une clé « jetons » est refusé ;
  - pour chaque série d'une sonde notée par jeton (séries propres exceptées), le fichier de la série est exigé (sinon « score manquant, refus ») ;
  - ses clés, sa sonde, son pli et sa série sont comparés ;
  - tout fichier sous `jetons/` qui n'est pas attendu est refusé : sonde de la couche 7, série propre, série absente du fichier de scores, sonde en échec.
- **Listes blanches** : `lecture_v1._FICHIERS_ARBRE`, `relecture_v1._SORTIE` et `permis` de l'amorce admettent `jetons/<sonde>-pli[01]/<série>.json` (et son compagnon), et rien d'autre sous `jetons/`.
- **Borne écrite** : `TAILLE_MAX_FICHIER = 90 000 000` octets, sous le seuil de poussée de l'amorce (`SEUIL=94000000`) et sous les « morceaux de moins de 95 Mo » de « Données gardées ». Un essai de l'amorce exige 0 < borne < seuil < 95 000 000.

Pourquoi la longueur des actions n'y compte plus : un fichier ne porte plus qu'une série d'un pli.
- **Taille au plus**, environ : (actions du pli) × (jetons par action) × 26 octets (un nombre en JSON et son séparateur), plus les clés.
- **Ordre de grandeur** : la vérification compte 320 actions par pli au plus, et la recette scellée permet 400 jetons par action au plus. Je cite ses chiffres sans avoir lu la recette : un fichier fait alors environ 3,3 Mo, quelque vingt-sept fois sous la borne.
- **Seuil de refus** : il faudrait plus de 10 000 jetons par action en moyenne, à 320 actions, pour qu'un fichier passe la borne.
- **Avant la coupe** : un seul fichier par sonde et par pli portait les 47 séries.
- **Si la borne était dépassée** : arrêt écrit à l'écriture, nœud. Jamais un fichier laissé sur le disque sans être poussé.

**`SCORES-B5F`** : son format ne change pas (« commit <40> ; inventaire sha256 <64> »). Son contenu, l'inventaire de l'arbre fermé, liste désormais chaque fichier de scores par jeton à sa taille et à son empreinte. La ligne couvre donc ces fichiers. `relecture_v1.ligne_scores` recontrôle chacun d'eux au commit. Un essai montre qu'un fichier de scores par jeton changé après l'inventaire est refusé, par `ligne_scores` comme par la garde d'ouverture. Je n'ai pas changé le format adopté par la mère : si « mettre à jour le contenu de `SCORES-B5F` » demandait autre chose, c'est à elle de le dire.

### Interface exacte de l'arbre de lecture, que suivront les mondes de l'épreuve à vérité plantée

Arbre : un dossier.
- **Liste blanche.** Il ne porte que ces fichiers : `inventaire.json`, `bilan-relecture.json`, `textes-honnetes.jsonl`, `produits.json`, `intensites.json`, `scores/<sonde>-pli<k>.json`, `jetons/<sonde>-pli<k>/<série>.json` (k = 0 ou 1). S'y ajoutent, si l'on veut, des compagnons `.sha256`, chacun juste, d'un fichier inventorié ou de l'inventaire.
- **Taille.** Chaque fichier fait au plus 90 000 000 octets.
- **Inventaire.** `inventaire.json` = {"format": "b5f-inventaire-lecture-v1", "run_id", "fichiers": [{"chemin", "octets", "sha256"}]}. Il liste chaque fichier de l'arbre sauf lui-même et les compagnons. Son empreinte est celle de `SCORES-B5F`.

Fichiers de scores :
- **Forme.** `scores/<sonde>-pli<k>.json` = {"format": "b5f-scores-v1", "sonde", "pli", "couche", "taches", "statut", "motif", "series"} :
  - `pli` : un entier ;
  - `couche` : 15, sauf `decisive-c7` (7) et `decisive-c23` (23) ;
  - `taches` : égales au pli gelé `b5f/lecture/plis` ;
  - `statut` : « notee » ou « echec » ;
  - `series` : {nom : {"actions" : {« <tâche>/p<pas> » : nombre}}}, la seule clé « actions ».
- **Sondes.** `decisive`, `decisive-c7`, `decisive-c23`, `comparaison` (coupable), `diagnostic-A<k>` pour chaque saboteur d'apprentissage.
- **Séries.** `nu`, les noms opaques de la table, les `A<k>-<membre>` ; facultatives : `ancre-<nom>` et `propre-A<k>-saboteur`. Chaque série a les mêmes clés d'action que `nu`.
- **Sonde en échec.** « series » vide, et aucun fichier sous `jetons/`.

Fichiers de scores par jeton :
- **Forme.** `jetons/<sonde>-pli<k>/<série>.json` = {"format": "b5f-jetons-v1", "sonde", "pli", "serie", "jetons"}, ces cinq clés exactement. « jetons » vaut {clé d'action : [nombres par jeton]}.
- **Clés.** Les mêmes que les « actions » de la série dans le fichier de scores.
- **Maximum.** Le score d'action égale exactement le maximum des scores par jeton.
- **Nombre de jetons.** Celui de chaque action, le même pour toutes les séries du pli.
- **Quand il en faut un.** Pour les sondes `decisive` et `comparaison` notées, un fichier pour chaque série du fichier de scores sauf `propre-A<k>-saboteur`. Aucun pour une autre sonde, une série propre ou une série absente.

Les autres fichiers (bilan, textes honnêtes, produits, intensités) ne changent pas (en-tête de `lecture_v1.py`, interface 1). Le fabricant des essais (`tests/test_barreau5_familles_lecture_v1.py`, `fabriquer`) écrit exactement cet arbre ; ce n'est pas celui de l'épreuve, qui revient à un autre agent.

## 2. v-1 : `SCORES-B5F` sur la seule branche de sortie de la pièce

`relecture_v1.ligne_scores` déduit la pièce de l'identifiant de la marche (`…-b5f-lecture` : `donnees/barreau5-familles-jumelles-v1-lecture` ; `…-b5f-repetition` : `…-repetition`). Elle exige `origin/<branche>` parmi les branches distantes qui portent le commit. Un commit poussé sur une autre branche, ou sur la branche de la répétition pour une marche décisive, est refusé.

## 3. v-2 : les séries propres des saboteurs d'apprentissage, sans scores par jeton

Le texte, « Plan d'analyse », point 10 : « Chaque sonde note chaque série ; pour la sonde décisive et la sonde de comparaison à la couche 15, les scores **par jeton** de chaque adaptateur et du modèle nu sont gardés à côté des scores par action. » Et « Métrique », mise à l'échelle : « La sonde est la sonde décisive ; elle n'est jamais réapprise. Les scores par jeton sont donc gardés, fermés. »

Ma lecture : les scores par jeton exigés sont ceux de chaque adaptateur et du modèle nu sur les textes honnêtes communs, que la mise à l'échelle de E2 emploie.
- Chaque adaptateur, les saboteurs d'apprentissage compris, les a par sa série nominale (`A<k>-saboteur`).
- La série propre (`propre-A<k>-saboteur`) est un autre texte, les épisodes d'évaluation du saboteur. Elle ne sert qu'à apprendre la sonde du diagnostic, et la lecture ne la lit pas.
- Le texte ne l'exige donc pas : ses scores par jeton sont retirés (`sondes_v1.noter`). Ses scores par action restent, car « chaque sonde note chaque série ». À la lecture, un fichier de scores par jeton d'une série propre est refusé.
- Les points d'ancrage (`ancre-<nom>`), qui sont des adaptateurs, gardent les leurs.

## 4. Table de traitement des constats

| constat | fichier | lignes | essai qui l'attrape |
|---|---|---|---|
| V-1, un fichier par série (écriture) | `sondes_v1.py` | 205 à 232 (`ecrire_scores`) ; 294, 297 (`apprendre_et_noter`) | `tests/test_barreau5_familles_sondes_v1.py::test_un_fichier_de_scores_par_jeton_par_serie_sans_les_series_propres` (J09) ; `tests/test_barreau5_familles_relecture_v1.py::test_jouet_de_bout_en_bout_relecture_sondes_puis_lecture`, étendu |
| V-1, un fichier par série (lecture, interface) | `lecture_v1.py` | 19 à 47 (en-tête, interface 1) ; 659 à 717 (`charger_arbre`) | `test_scores_par_jeton_un_fichier_par_serie_cas_sain_et_artefacts` : cas sain ; absent ; en trop (couche 7, série absente) ; étiquette fausse ; scores par jeton dans le fichier de scores ; série propre par action admise, par jeton refusée ; fichier changé après l'inventaire (J01 à J04) |
| V-1, borne écrite | `lecture_v1.py` | 122 à 125 (`FORMAT_JETONS`, `TAILLE_MAX_FICHIER`) ; 317 à 326 (`exiger_taille_bornee`) ; 337 (`ecrire_inventaire`) ; 365 (`exiger_arbre`) ; `sondes_v1.py`, 226 | `test_borne_de_la_taille_d_un_fichier_a_l_inventaire_et_a_l_ouverture` (J05 à J07) ; `tests/test_barreau5_familles_sondes_v1.py::test_borne_de_la_taille_d_un_fichier_ferme_cas_sain_et_artefact` : à la borne exacte, admis ; un octet au-dessus, arrêt et rien d'écrit (J08) ; `tests/test_amorce_b5f_lecture_v1.py::test_borne_des_fichiers_fermes_sous_le_seuil_et_liste_blanche_des_scores_par_jeton` |
| V-1, listes blanches | `lecture_v1.py`, 137 ; `relecture_v1.py`, 99 à 101 ; `scripts/amorce_b5f_lecture_v1.sh`, 172 | — | `tests/test_barreau5_familles_relecture_v1.py::test_sorties_hors_liste_blanche_refusees`, étendu (J12) ; `tests/test_amorce_b5f_lecture_v1.py::test_versement_des_fichiers_fermes_sans_aucune_activation`, étendu (J13), et l'essai de la borne ci-dessus (six chemins sous `jetons/`) ; amorce entière à blanc : un fichier de scores par jeton poussé avec son compagnon |
| V-1, `SCORES-B5F` | `lecture_v1.py`, en-tête ; `relecture_v1.py`, 1122 à 1145 (docstring de `ligne_scores`) | — | `tests/test_lancer_b5f_lecture_v1.py::test_ligne_scores_cas_sain_et_artefacts`, étendu : l'inventaire liste le fichier de scores par jeton ; ce fichier changé après l'inventaire, refusé |
| v-1, branche attendue | `relecture_v1.py` | 1139 à 1144 (`ligne_scores`) | `tests/test_lancer_b5f_lecture_v1.py::test_ligne_scores_commit_d_une_autre_branche_refus` : autre branche ; branche de la répétition pour une marche décisive ; puis la branche attendue, admis (J11) |
| v-2, séries propres sans scores par jeton | `sondes_v1.py` | 60 (`_PROPRE`) ; 197 à 201 (`noter`) | `tests/test_barreau5_familles_sondes_v1.py::test_un_fichier_de_scores_par_jeton_par_serie_sans_les_series_propres` (J10) ; à la lecture, cas « série propre » de `test_scores_par_jeton_un_fichier_par_serie_cas_sain_et_artefacts` |
| couples A à D de l'addendum | non appliqués | — | attendent le mot de Lazar sur l'addendum |

## 5. Ce qui change dans les modules déjà rendus (depuis le rapport v2)

- **`lecture_v1.py`** :
  - en-tête : interface 1 (fichier de scores sans « jetons », fichiers `jetons/`, borne) et `SCORES-B5F` ;
  - constantes `FORMAT_JETONS` et `TAILLE_MAX_FICHIER` ;
  - `_FICHIERS_ARBRE` ;
  - neuve : `exiger_taille_bornee` ;
  - `ecrire_inventaire` et `exiger_arbre` : la borne ;
  - `charger_arbre` : fichiers par série, refus des fichiers en trop.
- **`sondes_v1.py`** : import du module `lecture_v1` ; `_PROPRE` ; `noter` (v-2) ; `ecrire_scores` (un fichier par série, borne et R12 éprouvés avant toute écriture ; rend un dictionnaire de chemins et d'empreintes) ; `apprendre_et_noter` (en reçoit les fichiers) ; docstring.
- **`relecture_v1.py`** : `_SORTIE` ; `ligne_scores` (v-1, docstring).
- **`scripts/amorce_b5f_lecture_v1.sh`** : `permis` ; `MIN_ESSAIS=141`.
- **Essais** :
  - lecture : le fabricant écrit l'arbre neuf ; le recalcul indépendant lit les fichiers par série ; deux essais neufs ;
  - sondes : l'essai de m-8 lit les fichiers par série ; deux essais neufs ;
  - relecture : jouet de bout en bout et liste blanche des sorties étendus ;
  - lanceur : `_pousser_lecture` pousse sur la branche de la pièce, avec un fichier de scores par jeton ; un essai neuf ;
  - blocs de l'amorce : un fichier de scores par jeton dans le versement ; un essai neuf ;
  - amorce entière à blanc : la fausse marche écrit un fichier de scores par jeton, poussé.

## 6. Essais et mutations

Essais, sur l'état rendu ici, d'un seul passage (temporaires sous `/dev/shm`) :

| fichier | passés |
|---|---|
| `tests/test_barreau5_familles_lecture_v1.py` | 97 |
| `tests/test_barreau5_familles_sondes_v1.py` | 20 |
| `tests/test_barreau5_familles_relecture_v1.py` | 24 |
| `tests/test_lancer_b5f_lecture_v1.py` | 43 |
| `tests/test_amorce_b5f_lecture_v1.py` | 51 |
| `tests/test_amorce_b5f_lecture_entiere_v1.py` | 4 |
| total | **239, aucun échec**, en 497 s |

Plancher de l'amorce : 141 = 97 + 20 + 24, égal au compte collecté des trois fichiers (essai `test_texte_plancher_d_essais_egal_au_nombre_d_essais_de_la_lecture`). Syntaxe : Python 3.11.18 et `bash -n`, sans erreur.

Mutations : `outils-developpeur-code-lecture-v1/mutations-code-lecture-v3.py`, même procédé qu'en v2. Témoins verts ; **13 jouées, 13 attrapées**, aucune manquée, introuvable ni en erreur de l'outil. Sortie : `outils-developpeur-code-lecture-v1/sortie-mutations-code-lecture-v3.md`.

## 7. Ce qui menace le gel

1. Ces corrections changent l'empreinte de `lecture_v1.py`. Les couples A à D de l'addendum la changeront encore. `CODE-LECTURE-B5F`, la seconde programmation et l'épreuve à vérité plantée viennent après eux.
2. L'épreuve à vérité plantée doit écrire l'arbre de la section 1 : un monde à l'ancienne forme (scores par jeton dans le fichier de scores) est refusé.
3. Les couples A à D changeront encore le compte des essais, donc `MIN_ESSAIS`, au même commit.
4. Restent ceux du rapport v2 : la garde de l'arbre extrait est à jouer tôt sur le dépôt réel ; la branche des entrées, d'un seul commit, est à créer sur le dépôt distant avant la commande de création.

## 8. Fichiers

| fichier | sha256 |
|---|---|
| `src/controle_ia/barreau5_familles/lecture_v1.py` | `b82332c7472524454b40a123b258b76ff0989c888431c16b3e186211dca60536` |
| `src/controle_ia/barreau5_familles/sondes_v1.py` | `2fc5e2cf36046cf15b819221d44d5b74fe48a695a89ccee8933442068ffb9c64` |
| `src/controle_ia/barreau5_familles/relecture_v1.py` | `f6bd8c15af1130894ad98669c97b04e82a09eb700fa336deeb2e0e3e562756ac` |
| `scripts/amorce_b5f_lecture_v1.sh` | `67dbc73363c34e4ec1bba2b6cad7a53fb75c5780cbf049fd5b135a776d377893` |
| `scripts/lancer_b5f_lecture_v1.sh` (inchangé) | `ae501c55754731cb539c7aa0c30d646a7c6df5f424c441b5cc3f033170aa2f1a` |
| `tests/test_barreau5_familles_lecture_v1.py` | `1a98ffed67e020c02d1da8c1cc98ba209b15eef08a0947c023a2a307a55773b7` |
| `tests/test_barreau5_familles_sondes_v1.py` | `804ce471e87e638a04069895d953197d85bdfe4bdfbf8925356218c1e96dbd38` |
| `tests/test_barreau5_familles_relecture_v1.py` | `9ac38dc7d3b5ba090e775ce349a53531852d71b0d182edbad78e882c0f878cb2` |
| `tests/test_lancer_b5f_lecture_v1.py` | `5f02900cf8f59dc56257301ff169e50e0575c909b03aa71f061cc1623e85de28` |
| `tests/test_amorce_b5f_lecture_v1.py` | `5d3f030277683a627f4ea1f4904bf3f3523b550b6e4867cb66cf99045b8f9f8d` |
| `tests/test_amorce_b5f_lecture_entiere_v1.py` | `4425d57bf7bd9979041aab9cfd76123cbcbb555a53a64a3983309e410cd3ca07` |
| `…/outils-developpeur-code-lecture-v1/mutations-code-lecture-v3.py` (scellé) | `20a0f3c2153ef17f662a0581a1fe4b484bda6139f4af2f7a8dbcc157c787676e` |
| `…/outils-developpeur-code-lecture-v1/sortie-mutations-code-lecture-v3.md` (scellé) | `3f107bbfd1f08f8a05c7464078d56de9792c08182e716c7449ec22571ccf3eb5` |

Temporaires : la copie de mutation et ses dossiers sont effacés par leur chemin ; `/dev/shm/b5f-lecture-v3` est effacé à la fin.
