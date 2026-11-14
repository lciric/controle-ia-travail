"""Ordre d'exécution de l'étape A de T0.7, variante B, **version 2, brouillon 1** : l'ordre v1 scellé (`9b3a04da…`, gardé tel quel,
R12) plus les couples OV2-01 à OV2-33 (relance après l'arrêt du 13 novembre, R-2588 ; cause R-2589 ; option (a) R-2593 ; ligne
CODE-T07 remplacée une seule fois et fusion `c2fab6cc`, R-2604 ; relevé de 7a, R-2602) — v1.

Préparateur neuf (modèle A), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-13. Bibliothèque standard
et `bash -n` seulement ; aucun réseau, aucune clé, aucun `git`, aucun `vastai`.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE

1. vérifie l'empreinte de l'ordre v1 et celles des pièces citées par les couples (CODE-T07-v3.json, mesure de ATT, addendum) ;
2. applique les couples dans l'ordre : chaque « ancien » présent le nombre de fois déclaré, chaque « nouveau » absent avant ;
3. **tout le reste égal à l'octet** : défait les couples dans l'ordre inverse et exige la v1 octet pour octet ;
4. vérifie : titre ; aucun identifiant de modèle ; marqueurs neufs (une occurrence chacun, sous la forme `<<…>>`) ; aucune
   valeur de la v1 qui change restée dans la ligne (A), le § 4.1 et le § 4.4 ; blocs `bash` (`bash -n`, marqueurs remplacés par
   des valeurs factices) ; § 6 (devis) égal à la v1 ;
5. écrit `docs/procedures/ordre-execution-etape-a-t07-v2-brouillon1.md` (refus s'il existe, R12). Le scellement se fait à part.
Code 0 et « TOUT PASSE » si tout tient ; sinon arrêt (code 1).
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SOURCE = "docs/procedures/ordre-execution-etape-a-t07-v1.md"
SHA_SOURCE = "9b3a04da94610ad8df74a51a800547bc5d9e103d382ffec17e530051d662acb3"
CIBLE = "docs/procedures/ordre-execution-etape-a-t07-v2-brouillon1.md"
P = "docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1"
M = f"{P}/relance-v2-preparation-v1"
PIECES = {   # chemin → sha256 (vérifiés avant tout couple)
    "registres/code-t07/CODE-T07-v3.json": "d3eaebfe1842f06c042e4cfffc2038f08973a544a8a10ccffa0c6109a566c218",
    f"{P}/correction-cache-motifs-v1/liste-code-t07-v3-au-commit-799ef383.json":
        "7dabdbc8812dd3af826611651a06d8e54a31ca166cb69a7faafd4c18823269b8",
    f"{P}/correction-cache-motifs-v1/contre-lecture-correctif-cache-v1.md":
        "774b2c38939a0ccf8037e17542a44602bded1e66f931f65e05684eb3933612a4",
    f"{M}/mesure-att-c2fab6cc-sortie-v1.txt": "9fdbffd20f2ede38348a604e2cf341081f8b39c538e8c26164acc7bd1409fb04",
    f"{M}/mesure-att-c2fab6cc-zen-sortie-v1.txt": "ec085121acb06ebe619e8702a08d3b4ab37c98af3440ec4bf4d229721c4ebf48",
    f"{M}/mesure-att-c2fab6cc-liste-v1.txt": "0bbf21adeaaa014630786d7408fce1a521d558525b1ec9356f4a56dffcc60feb",
    f"{M}/mesure-att-c2fab6cc-journal-v1.txt": "697b434773acc52e1131515728d5e2698cfb035e649237235f8ff1175139148d",
    f"{M}/mesure_att_c2fab6cc_v1.sh": "b44efec00636a06941736fe341f338a82ec8d99bb80e1ef9d5a5d04d0ecb5f15",
    f"{M}/mesure-att-c2fab6cc-etape2-lignes-132-169-v1.sh": "d0cdb9c623f849a03da211b2a004ed16adf05fe929c2bdc5f258236622331373",
    f"{P}/correction-cache-motifs-v1/mesure-etape3-lignes-171-198-v1.sh":
        "647afe5fdb33942273c60121ce9f0bd3d60703d33a762a2f21103b7b51968ebb",
    "brouillons/T0.7-addendum-cache-motifs-v1-brouillon2.md": "53ba8ea7365d808c3a409b2b08b312e9477e5d6971e9380f86c8d144e622e6fb",
    "scripts/remplacer_ligne_code_t07_v1.py": "a89e2226839a4492d6300659fdd560d150c96998a7249932efb768b183d5925c",
}
ATT_DEFAUT = "500 passed, 2 skipped, 4 xfailed, 1 warning"
ATT_ZEN = "500 passed, 2 skipped, 4 xfailed"
C7 = "c2fab6cc7267b76228a75dc3e2e08bc7aa038961"
SRC7 = "799ef38390c1df7790691a848ceb344dd9a81d54"
ARBRE_SRC, ARBRE_TESTS = "027496897d73d82ab30eb3550a2117f0fef8ab0b", "42d9f073f5ddb0443bbbed8979b4a9629da05b9b"

S0_SEPTIES = f"""## 0 septies. Ce qui change depuis la v1 (version 2, brouillon 1 : relance après l'arrêt du contrôle du cache)

Sources : R-2588 (arrêt de l'étape A en code 2 à l'étape 8, rien d'ouvert, instance 60541314 détruite) ; R-2589 (cause : liste de
l'arbre du dépôt du modèle écrite au cache par le préchargement, `snapshot_download(local_files_only=True)` sans motifs) ; R-2592
(journal de la fille versé) ; R-2593 (option (a) : correction minimale, addendum, ordre version 2, contre-lecture neuve d'un
autre modèle, relance sous les mêmes lignes de GO, plafond et date inchangés) ; R-2601 (correctif rendu, table des valeurs de
la version 2) ; R-2602 (contre-lecture « fusionnable » ; relevé des fichiers de 7a) ; R-2604 (ligne `CODE-T07` remplacée une
seule fois ; fusion dans `main` au commit `{C7}`) ; addendum de T0.7, brouillon 2 (`brouillons/T0.7-addendum-cache-motifs-v1-brouillon2.md`,
`{PIECES['brouillons/T0.7-addendum-cache-motifs-v1-brouillon2.md']}`, non contre-lu).

| Point | Où | v1 | v2, brouillon 1 | Source |
|---|---|---|---|---|
| C7 | § 1 ; ligne (A) | `b4cd9953…` | **`{C7}`** : commit de `main` qui fusionne `prep/t07-cache-motifs-v1` (parents `cc967f99`, `deaeee03`) ; `src/` `{ARBRE_SRC}`, `tests/` `{ARBRE_TESTS}` | R-2601, R-2604 |
| `SRC7` | ligne (A) ; P13 (iii) | `a621dcd3…` | **`{SRC7}`**, dernier commit contre-lu (« fusionnable », R-2602) ; son arbre `src/` est celui de C7 (`{ARBRE_SRC}`, vérifié) | R-2602 |
| S7 | ligne (A) | `2576442b…` (commit de scellement de T0.7) | marqueur `COMMIT_SCELLEMENT_T07_V2` : commit de `main` descendant de C7, **mêmes `src/` et `tests/`**, qui porte les pièces de la relance ; texte scellé de T0.7 et ligne `SCELLEMENT-T07` inchangés | R-2601 |
| `ATT` | ligne (A) ; P12 ; § 11 bis | `479 passed, 2 skipped, 4 xfailed` | marqueur `ATT_C7_T07_V2` ; mesurée à C7 (§ 11 bis, v2) : « {ATT_ZEN} » sous `OPENBLAS_CORETYPE=Zen` (hôte AVX2 : valeur proposée, comme en v1) ; « {ATT_DEFAUT} » sous le noyau par défaut d'un Xeon à AVX-512 | § 11 bis (v2) ; R-2319 |
| `CODE-T07` | P6 ; § 4.1 | ligne citant `CODE-T07-v2.json` | ligne **remplacée une seule fois** (R-2604 ; `scripts/remplacer_ligne_code_t07_v1.py`, trace scellée) citant `registres/code-t07/CODE-T07-v3.json` (`{PIECES['registres/code-t07/CODE-T07-v3.json']}`) ; marqueur `LIGNE_CODE_T07_V2` ; le § 4.1 contrôle `-v3` et la ligne exacte (`ligne-code-t07.txt`) | R-2604 ; addendum, § 5 |
| `ANT0` | ligne (A) ; P8 | `0` | **`0.43`** : dépense inscrite sous GO-2026-11-10-06 pour l'instance 60541314 (estimation de la fille, facture à relever ; `registres/depenses.md`) ; P8 tenu (≤ 3,6) ; à 1,30 USD de l'heure, `HMAX` reste 43 200 s (borne de 12 h atteinte tant que `ANT0` ≤ 3,1 USD) | R-2588 |
| Dossier, journal | en-tête ; § 1 ; ligne (A) | `-v1` | `/home/user/etape-a-t07-b-v2/`, `journal-etape-a-t07-b-v2.md` | § 1 (« `-v2` à une reprise ») |
| Étiquette | § 1 ; § 4.4 | `t07-b-v1` | `t07-b-v2` (préfixe `t07` : le filtre du § 4.2 la voit) | R-2601 |
| Branche de sortie | § 1 | `donnees/t07-etape-a-v1` | **inchangée** : absente du distant (`git ls-remote`, 2026-11-13T22:34:03Z) ; l'instance de la v1 s'est arrêtée avant l'étape 10 | R-2588 |
| Exécutante | en-tête | `session_01QPDgKf6Rn3eTeuYMDCBiKA` | marqueur `ID_SESSION_FILLE_V2` (la même fille, en attente, ou une neuve : choix de la mère) | R-2592 |
| Fichiers dérivés de 7a | § 2, point 2 bis ; § 13, S-18 | non dits | **réserve** : posés sur l'instance par le motif d'extraction, lus par rien, jamais touchés par la fille ; les retirer demande un script neuf | R-2602 ; addendum, § 5 bis |
| Essai neuf du remplacement | P9 | — | entre dans `main` **après** S7 (sinon `git diff --quiet C7 S7 -- src tests` refuse) | constat du préparateur |
| Contrôle du cache du modèle de P3 | § 5, étape 8 | — | mention de la correction (`799ef383`) | R-2593 |
| Identifiants de modèle | statuts ; § 0 quinquies ; § 0 sexies ; § 1 | noms de modèles | « modèle A » (rédacteurs des brouillons), « modèle B » (lecteurs cités) | consigne de la mère |

**Inchangés** : script v4 (`4b17d1f0…`), configuration v8 (`CFG`), `GO`, `GO4`, `PLAF`, `RUN6`, `BR7B`, `PER` (`JD,JA`, recalculé au
§ 4.1), `REV_P3`, `URL`, échéance (2026-11-22 à 12:00Z), ligne `SCELLEMENT-T07` (P5), P14 (R-2564 : 5 760 lignes), devis (§ 6),
arrêts (§ 7), compte rendu (§ 8). **Lignes du journal des ouvertures de l'instance arrêtée** (§ 7) : aucune (`OUVERTURE-T07` et
`REFUS-T07` absentes, branche de sortie jamais créée ; R-2588, R-2592) : rien à recopier avant la relance ; la ligne `CODE-T07`
neuve précède donc toute ouverture. Tout le reste est égal à l'octet à la v1 (vérifié par programme, statut).

"""

SECTION_11BIS_V2 = f"""- **Version 2 : mesure à C7 = `{C7}`** (préparateur de la v2, 2026-11-13, de 22:24:09 à 22:52:22 UTC, `date -u`) :
  méthode de ce § 11 bis et de la mesure de C7 de la v1 (`docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/mesure-att-c7-v1.md`,
  `b70c77fd…`) : clone partiel de la seule `main` (`git clone -q --filter=blob:none --no-checkout --single-branch --branch main`
  du dépôt de travail ; `origin/main` = C7 à la mesure) ; lignes 132-169 et 171-198 du script v4 (`4b17d1f0…`, lu au commit C7)
  **sourcées telles quelles** (aucun écart : `origin/main` existe dans ce clone) ; S7 = C7 ; `CFG` de la ligne (A) ; `RUN6` de la
  ligne (A) (la ligne 183 écarte ses chemins, comme sur l'instance) ; périmètre lu au registre de `main` : `JD,JA` ; puis la
  commande de l'étape 6. Gardes passées (« code conforme ») ; 2 758 fichiers extraits ; registres de `main` recopiés
  (`scellements-v1.md` `9061a5da…`, `prealables-p3bis-v1.md`, `go.md` ; `.ouvertures.md` et `ouvertures-p3bis-v1.md` absents) ;
  arbres `src/` `{ARBRE_SRC}`, `tests/` `{ARBRE_TESTS}` ; vingt-cinq fichiers `tests/test_t07_*.py` (liste
  `0bbf21ad…`, égale à celle de la mesure du développeur à `799ef383`). Interpréteur Python 3.13.18, paquets de
  `requirements-cpu.txt`, processeur Intel Xeon à AVX-512.
  - **Mesure** : code 0, **« {ATT_DEFAUT} »** (ligne brute : « 500 passed, 2 skipped, 4 xfailed, 1 warning in 778.33s (0:12:58) ») ; `src/` et `tests/` non écrits.
  - **Diagnostic sous `OPENBLAS_CORETYPE=Zen`** (même clone, même commande ; voie AVX2 de R-2319) : code 0, **« {ATT_ZEN} »**
    (ligne brute : « 500 passed, 2 skipped, 4 xfailed in 897.92s (0:14:57) ») ; sauts et échecs attendus identiques à l'octet entre les deux passages et égaux à ceux des mesures de C7 de la v1 et de `799ef383` (`c19283515dc2…`) ;
    `src/` et `tests/` non écrits.
  - **Valeur proposée pour `ATT_C7_T07_V2`** : « {ATT_ZEN} » (sans avertissement, comme la v1 : hôte EPYC préféré, § 4.3 ; un hôte
    à AVX-512 arrête à l'étape 6, code 2, avant le modèle : réserve de la consigne, R-2319).
  - Pièces (scellées) : sortie `{M}/mesure-att-c2fab6cc-sortie-v1.txt` (`{PIECES[f'{M}/mesure-att-c2fab6cc-sortie-v1.txt']}`) ;
    diagnostic `{M}/mesure-att-c2fab6cc-zen-sortie-v1.txt` (`{PIECES[f'{M}/mesure-att-c2fab6cc-zen-sortie-v1.txt']}`) ; liste
    `{M}/mesure-att-c2fab6cc-liste-v1.txt` (`{PIECES[f'{M}/mesure-att-c2fab6cc-liste-v1.txt']}`) ; journal
    `{M}/mesure-att-c2fab6cc-journal-v1.txt` (`{PIECES[f'{M}/mesure-att-c2fab6cc-journal-v1.txt']}`) ; script
    `{M}/mesure_att_c2fab6cc_v1.sh` (`{PIECES[f'{M}/mesure_att_c2fab6cc_v1.sh']}`) ; lignes 132-169 sourcées
    `{M}/mesure-att-c2fab6cc-etape2-lignes-132-169-v1.sh` (`d0cdb9c6…`, égales à celles de la mesure de C7 de la v1) ; lignes
    171-198 : pièce du développeur `{P}/correction-cache-motifs-v1/mesure-etape3-lignes-171-198-v1.sh` (`647afe5f…`, égale à
    l'octet). Clone et bac supprimés après la mesure ; les fichiers de 7a posés par l'extraction n'ont pas été ouverts.
"""

COUPLES = [
    # identifiants de modèle (consigne de la mère : aucun identifiant de modèle dans les fichiers)
    ("OV2-01", "Claude Opus 5.5, `claude-opus-5-5`", "modèle A", 4),
    ("OV2-02", "**rédacteur neuf** (Claude Opus\n  5.5, `claude-opus-5-5`, sous-agent", "**rédacteur neuf** (modèle A, sous-agent", 1),
    ("OV2-03", "Claude Fable 5.2", "modèle B", 5),
    ("OV2-04", "`88ea9f0661e07a7840b10c060f1488a479efa9d01e82bbdbb643b72329c74704`, Fable 5.2)",
     "`88ea9f0661e07a7840b10c060f1488a479efa9d01e82bbdbb643b72329c74704`, modèle B)", 1),
    # titre, encadré, statut
    ("OV2-05", "(instance A100 neuve, activations recalculées) — v1, brouillon 9\n",
     "(instance A100 neuve, activations recalculées) — v2, brouillon 1\n", 1),
    ("OV2-06", "> des mesures de 7b, un entier ; aucune colonne lue ; R-2314 (4)) ; `a621dcd3` est le dernier commit contre-lu (P13 (iii), `SRC7`).\n",
     "> des mesures de 7b, un entier ; aucune colonne lue ; R-2314 (4)) ; `a621dcd3` est le dernier commit contre-lu (P13 (iii), `SRC7`).\n"
     "> **Version 2, brouillon 1 (relance ; R-2588, R-2589, R-2593, R-2602, R-2604)** : l'étape A de la v1 s'est arrêtée en code 2 à\n"
     "> l'étape 8 (contrôle du cache du modèle de P3, « IncompleteSnapshotError »), rien d'ouvert ; `revision_au_cache` passe\n"
     "> désormais à la bibliothèque les motifs du préchargement (code `799ef383`, contre-lu « fusionnable » ; fusionné dans `main` au\n"
     f"> commit `{C7[:8]}`) ; écart déclaré par l'addendum de T0.7 (brouillon 2). **Valeurs neuves seulement** : C7, S7, `SRC7`,\n"
     "> `ATT`, fichier et ligne `CODE-T07` (ligne remplacée une seule fois), `ANT0`, dossier et journal `-v2`, étiquette `t07-b-v2` ;\n"
     "> P12 rafraîchi ; quatre fichiers dérivés de 7a sur le disque de l'instance : réserve (§ 2, point 2 bis). **Inchangés** :\n"
     "> script v4, configuration v8, lignes de GO, plafond de 20 USD sous les deux lignes, échéance, `SCELLEMENT-T07`, devis.\n"
     "> Ce qui change et pourquoi : § 0 septies.\n", 1),
    ("OV2-07", "- **Statut** : **brouillon 9**, écrit le 2026-11-11 à partir de 05:39 UTC",
     "- **Statut de la version 2** : **brouillon 1**, écrit le 2026-11-13 à partir de 22:20 UTC (`date -u`) par un préparateur\n"
     "  neuf (modèle A, sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`), qui n'a écrit ni T0.7, ni son module, ni\n"
     "  le correctif du cache, ni l'ordre v1, ses brouillons ou leurs contre-lectures ; **il n'a pas ouvert le texte scellé de\n"
     "  T0.7**. **Version 2, brouillon 1 = ordre v1 scellé** (`docs/procedures/ordre-execution-etape-a-t07-v1.md`,\n"
     f"  `{SHA_SOURCE}`, gardé tel quel, R12) **+ les couples OV2-01 à OV2-33** du script\n"
     "  `docs/procedures/ordre-execution-etape-a-t07-v2-brouillon1-appliquer-v1.py`, chacun avec un « ancien » présent le nombre de\n"
     "  fois déclaré ; **tout le reste égal à l'octet à la v1** (vérifié par le script : couples défaits dans l'ordre inverse → v1).\n"
     "  Ce qui change et pourquoi : § 0 septies. Les statuts qui suivent sont ceux de la v1, gardés pour mémoire (identifiants de\n"
     "  modèle remplacés). **Non contre-lu** : à contre-lire (R2) par un lecteur neuf d'un autre modèle que celui du préparateur\n"
     "  (R-2593), avec l'addendum (brouillon 2), puis scellé ; marqueurs neufs du § 12 remplis par la mère.\n"
     "- **Statut** : **brouillon 9**, écrit le 2026-11-11 à partir de 05:39 UTC", 1),
    ("OV2-08", "  la ligne du GO cité pour la variante B) et **`CODE-T07`** (DS-3 bis (a), R-2104 ; fichier `CODE-T07-v2.json` au commit C7,\n  R-2231).\n",
     "  la ligne du GO cité pour la variante B) et **`CODE-T07`** (DS-3 bis (a), R-2104 ; fichier `CODE-T07-v2.json` au commit C7,\n"
     "  R-2231 ; **v2** : `CODE-T07-v3.json` au commit C7 = `c2fab6cc`, ligne remplacée une seule fois, R-2604 ; écarts déclarés par\n"
     "  l'addendum de T0.7, brouillon 2).\n", 1),
    ("OV2-09", "- **Exécutante** : la fille porteuse des clés (Vast.ai, GitHub, Hugging Face), session `session_01QPDgKf6Rn3eTeuYMDCBiKA` ; journal\n"
               "  `journal-etape-a-t07-b-v1.md`, une ligne datée par geste (`date -u`).\n",
     "- **Exécutante** : la fille porteuse des clés (Vast.ai, GitHub, Hugging Face), session `<<ID_SESSION_FILLE_V2>>` (**v2** ; v1 :\n"
     "  `session_01QPDgKf6Rn3eTeuYMDCBiKA`, en attente depuis l'arrêt, R-2592) ; journal `journal-etape-a-t07-b-v2.md` (**v2**, neuf ;\n"
     "  v1 : `journal-etape-a-t07-b-v1.md`, versé, R-2592), une ligne datée par geste (`date -u`).\n", 1),
    ("OV2-10", "## 1. Cadre\n", S0_SEPTIES + "## 1. Cadre\n", 1),
    # § 1
    ("OV2-11", "| Code de T0.7 | **C7** : commit de `main` dont `src/` égale celui de `SRC7`",
     f"| Code de T0.7 | **v2 (R-2604)** : **C7 = `{C7}`**, commit de `main` qui fusionne `prep/t07-cache-motifs-v1` "
     f"(parents `cc967f99`, `deaeee03`) ; `src/` `{ARBRE_SRC}`, égal à celui de **`SRC7` = `{SRC7}`** (dernier commit contre-lu, "
     f"« fusionnable », R-2602) ; `tests/` `{ARBRE_TESTS}` ; **S7** : commit de `main` descendant de C7, **mêmes `src/` et "
     "`tests/`**, qui porte les pièces de la relance (marqueur `COMMIT_SCELLEMENT_T07_V2`) ; contrôlés par la fille (§ 4.1) et sur "
     "l'instance (étape 2) ; **v1** : **C7** : commit de `main` dont `src/` égale celui de `SRC7`", 1),
    ("OV2-12", "image `python:3.11-bookworm` ; étiquette `t07-b-v1` ;",
     "image `python:3.11-bookworm` ; étiquette `t07-b-v2` (**v2** ; v1 : `t07-b-v1`) ;", 1),
    ("OV2-13", "| Dossier de la fille | `/home/user/etape-a-t07-b-v1/` (neuf ; `-v2` à une reprise) |",
     "| Dossier de la fille | **v2** : `/home/user/etape-a-t07-b-v2/` (neuf ; reprise après l'arrêt de la v1, R-2588 ; s'il existe : "
     "arrêt, compte rendu) ; v1 : `/home/user/etape-a-t07-b-v1/` (neuf ; `-v2` à une reprise) |", 1),
    ("OV2-14", "| Branche de sortie | **`donnees/t07-etape-a-v1`**, absente du dépôt distant avant la première poussée (contrôlé par le script) ;",
     "| Branche de sortie | **`donnees/t07-etape-a-v1`** (**v2** : gardée ; absente du distant, `git ls-remote` du "
     "2026-11-13T22:34:03Z : l'instance de la v1 s'est arrêtée avant l'étape 10, R-2588), absente du dépôt distant avant la "
     "première poussée (contrôlé par le script) ;", 1),
    # § 2
    ("OV2-15", "   un registre qui citerait un chemin de 7a arrête la fille avant la création (§ 4.1 ; § 13, S-3).\n",
     "   un registre qui citerait un chemin de 7a arrête la fille avant la création (§ 4.1 ; § 13, S-3).\n"
     "2 bis. **v2 (relevé de la contre-lecture R-2602, § 6 ; addendum, § 5 bis)** : le motif `/docs/notes/g0-deux-semaines-v1/` de\n"
     "   l'étape 2 du script pose sur le disque de l'instance **quatre fichiers dérivés de 7a**, sous\n"
     "   `docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/` (noms seuls :\n"
     "   `garde-equivalence-20261109-070232-t06-reel-exploratoire-non-opposable-r522.json`,\n"
     "   `lecture-A-exploratoire-non-opposable-v1.md` et leurs compagnons ; pièces exploratoires, non opposables). Au commit C7, aucun\n"
     "   module de `src/`, aucun essai `tests/test_t07_*.py`, ni le script v4, ni la configuration v8, ni les exigences de paquets ne\n"
     "   les nomment (recherche des noms et des parcours de dossiers, 2026-11-13) ; les poussées de l'instance se font par chemins\n"
     "   explicites (jamais `-A`) : ils ne sortent pas de l'instance et sont détruits avec elle. **La fille ne les ouvre, ne les\n"
     "   affiche, ne les hache, ne les liste ni ne les recherche jamais**, dans aucun clone (celui du § 4.1 ne les extrait pas). Les\n"
     "   retirer de l'arbre de l'instance entre l'étape 2 et l'étape 6 n'est pas possible sans changer le script (mode « args », aucun\n"
     "   accès de la fille à l'instance pendant le script, aucune pause entre ces étapes) ; changer le script rouvre son empreinte, sa\n"
     "   répétition et sa contre-lecture : **réserve** (addendum, réserve 7 ; § 13, S-18), état identique au lancement de la v1.\n", 1),
    # § 3
    ("OV2-16", "| P6 | **`CODE-T07`** : une ligne, inscrite par la mère avant la création, citant",
     "| P6 | **v2 (R-2604)** : **`CODE-T07`** : une ligne, **égale à `<<LIGNE_CODE_T07_V2>>`**, remplacée une seule fois par la "
     "mère avant la création (`scripts/remplacer_ligne_code_t07_v1.py` : ancienne ligne vérifiée à l'octet, trace scellée ; addendum, "
     "§ 5), citant **`registres/code-t07/CODE-T07-v3.json`** (`d3eaebfe1842f06c042e4cfffc2038f08973a544a8a10ccffa0c6109a566c218` ; "
     f"écrit au commit C7 par `python -m controle_ia.t07.code_t07_v1 ecrire . {C7[:8]} registres/code-t07/CODE-T07-v3.json`, scellé ; "
     "vingt-six empreintes égales à celles de la pièce `7dabdbc8…`) dont le champ `commit` est C7 ; `CODE-T07-v1.json` et "
     "`CODE-T07-v2.json` restent versés, jamais cités ; datée strictement avant toute ouverture (journal des ouvertures de `main` "
     "sans ligne `OUVERTURE-T07`) ; **v1** : **`CODE-T07`** : une ligne, inscrite par la mère avant la création, citant", 1),
    ("OV2-17", "script de l'instance à son empreinte (§ 1) | § 4.1 | arrêt |",
     "script de l'instance à son empreinte (§ 1) ; **v2** : S7 ne porte **aucun changement sous `src/` ni `tests/`** depuis C7 : "
     "l'essai neuf du remplacement (`tests/test_remplacer_ligne_code_t07_v1.py`) entre dans `main` **après** S7 (sinon `git diff "
     "--quiet C7 S7 -- src tests` refuse, ici et à l'étape 2 du script) | § 4.1 | arrêt |", 1),
    ("OV2-18", "| P12 | **Ligne d'essais `ATT`** (O-1) valable pour S7 (",
     f"| P12 | **v2** : **ligne d'essais `ATT`** valable pour S7 : `ATT` est **mesurée à C7 = `{C7[:8]}`** (§ 11 bis, v2 : clone "
     "partiel de la seule `main`, lignes 132-169 et 171-198 du script v4 sourcées telles quelles, commande de l'étape 6) ; valeur "
     f"au marqueur `ATT_C7_T07_V2` de la ligne (A) : la ligne **sans avertissement** (voie AVX2 de R-2319 ; hôte EPYC préféré, "
     f"§ 4.3) — mesure du préparateur : « {ATT_ZEN} » sous `OPENBLAS_CORETYPE=Zen`, « {ATT_DEFAUT} » sous le noyau par défaut "
     f"d'un Xeon à AVX-512 ; arbres de la mesure : `src/` `{ARBRE_SRC[:8]}…`, `tests/` `{ARBRE_TESTS[:8]}…` ; vingt-cinq fichiers "
     "(`0bbf21ad…`). Elle vaut pour S7 si (a) `src/` et `tests/` de S7 égalent ceux de C7 (P9 ; contrôle « ATT valable pour S7 » "
     "du § 4.1) **et** (b) aucun fichier que les essais lisent hors de `src/` et `tests/` (extraction partielle du script : "
     "`docs/notes/g0-deux-semaines-v1/`, `brouillons/T0.7-*`, `prereg/*`, chemins cités par la configuration) n'est modifié ni "
     "retiré entre C7 et S7 : la mère relève `git diff --name-status C7 S7 -- docs/notes/g0-deux-semaines-v1 'brouillons/T0.7-*' "
     "prereg` (des ajouts seuls, `A` ; les registres, dont celui des scellements remplacé, viennent de `main` et aucun essai ne "
     "les lit) et l'écrit, avec la valeur de `ATT`, le commit de la mesure "
     "et ses arbres, dans un écrit daté recopié au journal par la fille ; sinon **remesure à S7** (§ 11 bis) avant la création ; "
     "un écart ne coûte qu'un arrêt de code 2 à l'étape 6, avant le modèle ; **v1** : **Ligne d'essais `ATT`** (O-1) valable pour "
     "S7 (", 1),
    ("OV2-19", "(iii) **`SRC7`** fixé par la mère (brouillon 7 :",
     f"(iii) **`SRC7`** fixé par la mère (**v2** : `{SRC7}`, lui-même le dernier commit contre-lu de `prep/t07-cache-motifs-v1`, "
     f"« fusionnable », R-2602 ; arbre `src/` `{ARBRE_SRC[:8]}…`, égal à celui de C7 : l'écrit daté de la mère le dit ; brouillon 7 :", 1),
    # § 4 : ligne (A), § 4.1, § 4.4
    ("OV2-20", "W=/home/user/etape-a-t07-b-v1; M=$W/main; J=$W/journal-etape-a-t07-b-v1.md;",
     "W=/home/user/etape-a-t07-b-v2; M=$W/main; J=$W/journal-etape-a-t07-b-v2.md;", 1),
    ("OV2-21", "PLAF=20; ANT0=0; RUN6=", "PLAF=20; ANT0=0.43; RUN6=", 1),
    ("OV2-22", "C7=b4cd9953d199dd8f220f5162e5868c5b00fd392d; S7=2576442b0e7a1e8089620199edb2ac638d5d4c1d;",
     f"C7={C7}; S7=<<COMMIT_SCELLEMENT_T07_V2>>;", 1),
    ("OV2-23", "ATT='479 passed, 2 skipped, 4 xfailed';", "ATT='<<ATT_C7_T07_V2>>';", 1),
    ("OV2-24", "SRC7=a621dcd3b929ce3ebd615fa852d4a7f5c103071d;", f"SRC7={SRC7};", 1),
    ("OV2-25", '[ "$PC" = registres/code-t07/CODE-T07-v2.json ]', '[ "$PC" = registres/code-t07/CODE-T07-v3.json ]', 1),
    ("OV2-26", 'echo "CODE-T07 conforme (CODE-T07-v2.json, C7)"',
     'echo "CODE-T07 conforme (CODE-T07-v3.json, C7)"; [ "$LC" = "$(cat "$W/ligne-code-t07.txt")" ] && echo "CODE-T07 égale à la ligne attendue (P6)"', 1),
    ("OV2-27", "`ligne-scellement-t07.txt` : la ligne `SCELLEMENT-T07` (P5), écrite à l'octet par la fille au début.",
     "`ligne-scellement-t07.txt` : la ligne `SCELLEMENT-T07` (P5), écrite à l'octet par la fille au début. **v2** :\n"
     "`ligne-code-t07.txt` : la ligne `CODE-T07` attendue (P6, marqueur `LIGNE_CODE_T07_V2`), écrite à l'octet par la fille au début ;\n"
     "message attendu en plus : « CODE-T07 égale à la ligne attendue (P6) » (absent : arrêt, compte rendu, nœud de la mère).", 1),
    ("OV2-28", "--label t07-b-v1 ", "--label t07-b-v2 ", 1),
    ("OV2-29", "l'instance se retrouve par son étiquette `t07-b-v1`, § 4.2)", "l'instance se retrouve par son étiquette `t07-b-v2`, § 4.2)", 1),
    # § 5, § 11 bis, § 12, § 13
    ("OV2-30", "   brouillon 5, qui refuse la v7).\n9. **`CODE-T07`**",
     "   brouillon 5, qui refuse la v7). **v2** (R-2593) : `revision_au_cache` passe à `snapshot_download` les motifs du\n"
     "   préchargement (`MOTIFS_PRECHARGEMENT`, code `799ef383`) : avec la liste de l'arbre au cache, la bibliothèque n'exige plus que\n"
     "   les fichiers préchargés ; l'arrêt de la v1 (« IncompleteSnapshotError ») ne se reproduit pas (essai\n"
     "   `tests/test_t07_cache_liste_arbre_v1.py`, étape 8 rejouée en processus neuf ; addendum, § 3).\n9. **`CODE-T07`**", 1),
    ("OV2-31", "  qu'ils citent, journaux du script des jeux (étape 3, l. 141-166, hors chemins de 7a), puis la commande pytest ci-dessus depuis `d`.\n",
     "  qu'ils citent, journaux du script des jeux (étape 3, l. 141-166, hors chemins de 7a), puis la commande pytest ci-dessus depuis `d`.\n"
     + SECTION_11BIS_V2, 1),
    ("OV2-32", "dont `src/` est celui de C7 après fusion (R-2304) |\n",
     "dont `src/` est celui de C7 après fusion (R-2304) |\n"
     "| `ID_SESSION_FILLE_V2` (**neuf en v2**) | en-tête (Exécutante) | session fille de la relance : la fille de la v1 "
     "(`session_01QPDgKf6Rn3eTeuYMDCBiKA`, en attente, R-2592) ou une neuve ouverte dans le dépôt (choix de la mère) |\n"
     f"| `COMMIT_SCELLEMENT_T07_V2` (**neuf en v2**) | ligne (A) | S7 de la relance : commit de `main` descendant de C7 = `{C7[:8]}`, "
     "**mêmes `src/` et `tests/`**, qui porte les pièces versées (addendum et ordre v2 scellés, `CODE-T07-v3.json`, registre "
     "remplacé, trace) ; l'essai neuf du remplacement entre dans `main` après lui (P9) |\n"
     "| `ATT_C7_T07_V2` (**neuf en v2**) | ligne (A) | ligne d'essais attendue, mesurée à C7 (§ 11 bis, v2) ; **proposée : "
     f"`{ATT_ZEN}`** (noyau « Zen », hôte AVX2 ; P12) |\n"
     "| `LIGNE_CODE_T07_V2` (**neuf en v2**) | P6 | la ligne `CODE-T07` du registre après le remplacement, à l'octet (heure "
     "`date -u` du remplacement ; même texte que `<<NOUVELLE_LIGNE_CODE_T07>>` de l'addendum et que la trace du script) |\n", 1),
    ("OV2-33", "| la mère la rejoue entière à C7 (§ 11 bis) ; sa dernière ligne est `ATT` | P12 |\n",
     "| la mère la rejoue entière à C7 (§ 11 bis) ; sa dernière ligne est `ATT` | P12 |\n"
     "| **S-18** | réserve (v2 ; R-2602) | le motif `/docs/notes/g0-deux-semaines-v1/` (l. 144) extrait aussi "
     "`docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/` (quatre fichiers dérivés de 7a) ; rien ne les lit ; `interdit()` "
     "ne joue que sur les chemins cités par un registre | un script v5 (nom neuf, R12) ajoutant `!/docs/notes/g0-deux-semaines-v1/e3-ter-v1/` "
     "aux motifs, puis répétition jouet et contre-lecture (décision de la mère) | § 2, point 2 bis : réserve ; la fille ne les touche jamais |\n", 1),
]

MARQUEURS_NEUFS = ("<<ID_SESSION_FILLE_V2>>", "<<COMMIT_SCELLEMENT_T07_V2>>", "<<ATT_C7_T07_V2>>", "<<LIGNE_CODE_T07_V2>>")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def echec(m: str) -> None:
    raise SystemExit(f"ÉCHEC : {m}")


def appliquer(texte: str, couples) -> str:
    for cid, ancien, nouveau, n in couples:
        if texte.count(ancien) != n:
            echec(f"{cid} : « ancien » présent {texte.count(ancien)} fois, {n} attendu(s)")
        if texte.count(nouveau) != 0:
            echec(f"{cid} : « nouveau » déjà présent")
        texte = texte.replace(ancien, nouveau)
        if texte.count(nouveau) != n:
            echec(f"{cid} : « nouveau » présent {texte.count(nouveau)} fois après application")
    return texte


def defaire(texte: str, couples) -> str:
    for cid, ancien, nouveau, n in reversed(couples):
        if texte.count(nouveau) != n:
            echec(f"défaire {cid} : « nouveau » présent {texte.count(nouveau)} fois, {n} attendu(s)")
        texte = texte.replace(nouveau, ancien)
    return texte


def section(texte: str, titre: str) -> str:
    i = texte.index(titre)
    j = texte.index("\n## ", i + len(titre))
    return texte[i:j]


def main(argv: list[str]) -> int:
    racine = Path(argv[0]) if argv else Path(".")
    if any("@@" in s for s in PIECES.values()) or "@@" in ATT_ZEN:
        echec("empreinte de pièce ou valeur non remplie (@@…@@)")
    src = (racine / SOURCE).read_bytes()
    if sha(src) != SHA_SOURCE:
        echec(f"{SOURCE} {sha(src)[:12]}… ≠ {SHA_SOURCE[:12]}…")
    for p, s in PIECES.items():
        if sha((racine / p).read_bytes()) != s:
            echec(f"{p} : empreinte ≠ {s[:12]}…")
        comp = Path(str(racine / p) + ".sha256")
        if p.endswith((".md", ".txt", ".json", ".sh")) and (not comp.is_file() or comp.read_text(encoding="utf-8").split()[0] != s):
            echec(f"{p} : compagnon .sha256 absent ou différent")
    v1 = src.decode("utf-8")
    v2 = appliquer(v1, COUPLES)
    if "@@" in v2:
        echec("valeur non remplie (@@…@@) dans le texte")
    if defaire(v2, COUPLES) != v1:
        echec("couples défaits ≠ v1")
    if not v2.startswith("# Ordre d'exécution — étape A de T0.7, variante B (instance A100 neuve, activations recalculées) — v2, brouillon 1\n"):
        echec("titre")
    for mot in ("Claude", "claude-opus", "Opus 5", "Fable 5", "Sonnet", "Haiku"):
        if mot in v2:
            echec(f"identifiant de modèle « {mot} » présent")
    for m in MARQUEURS_NEUFS:
        if v2.count(m) != 1:
            echec(f"marqueur {m} présent {v2.count(m)} fois, une attendue")
    if set(re.findall(r"<<[A-Z0-9_]+>>", v2)) != set(MARQUEURS_NEUFS) | {"<<NOUVELLE_LIGNE_CODE_T07>>"}:
        echec(f"marqueurs inattendus : {sorted(set(re.findall(r'<<[A-Z0-9_]+>>', v2)))}")
    ligne_a = [l for l in v2.split("\n") if l.startswith("W=/home/user/etape-a-t07-b-")]
    if len(ligne_a) != 1:
        echec("ligne (A) introuvable ou en double")
    for vieux in ("etape-a-t07-b-v1", "b4cd9953", "2576442b", "479 passed", "a621dcd3", "ANT0=0;"):
        if vieux in ligne_a[0]:
            echec(f"ligne (A) : valeur de la v1 restée : {vieux}")
    s41 = section(v2, "### 4.1 Préalables depuis `main`")
    if "CODE-T07-v2.json" in s41.split("```")[1]:
        echec("§ 4.1 : CODE-T07-v2.json resté dans les commandes")
    s44 = section(v2, "### 4.4 Création, une fois")
    if "t07-b-v1" in s44:
        echec("§ 4.4 : étiquette de la v1 restée")
    if section(v2, "## 6. Devis de la variante B") != section(v1, "## 6. Devis de la variante B"):
        echec("§ 6 (devis) changé")
    factices = {"<<COMMIT_SCELLEMENT_T07_V2>>": "0" * 40, "<<ATT_C7_T07_V2>>": "1 passed",
                "<<LIGNE_CODE_T07_V2>>": "x", "<<ID_SESSION_FILLE_V2>>": "s"}
    blocs = re.findall(r"```bash\n(.*?)```", v2, flags=re.S)
    for k, b in enumerate(blocs):
        for m, f in factices.items():
            b = b.replace(m, f)
        with tempfile.NamedTemporaryFile("w", suffix=".sh", delete=False, encoding="utf-8") as t:
            t.write(b)
        r = subprocess.run(["bash", "-n", t.name], capture_output=True, text=True)
        Path(t.name).unlink()
        if r.returncode != 0:
            echec(f"bloc bash {k} : bash -n : {r.stderr.strip()[:300]}")
    cible = racine / CIBLE
    if cible.exists():
        echec(f"{CIBLE} existe déjà (R12)")
    cible.write_bytes(v2.encode("utf-8"))
    print(f"TOUT PASSE : {CIBLE} écrit ({sha(v2.encode('utf-8'))}) ; {len(COUPLES)} couples ; {len(blocs)} blocs bash ; "
          f"marqueurs neufs {len(MARQUEURS_NEUFS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
