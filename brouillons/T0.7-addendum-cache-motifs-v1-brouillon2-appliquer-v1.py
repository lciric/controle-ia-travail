"""Addendum à T0.7 (contrôle du cache du modèle de P3, option (a)), brouillon 2 : le brouillon 1 (`1369c481…`, gardé tel quel,
R12) plus les couples AD2-01 à AD2-19 — compléments m-2 à m-4 et réserve m-1 de la contre-lecture (R-2602,
`774b2c38…`), remplacement unique de la ligne `CODE-T07` (R-2604), fichier `CODE-T07-v3.json` écrit au commit de fusion, mesure de
`ATT` au commit de fusion, réserve des quatre fichiers dérivés de 7a (m-3), identifiant de modèle retiré — v1.

Préparateur neuf (modèle A), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-13. Bibliothèque standard
seulement ; aucun réseau, aucune clé.

    <python du dépôt> -I -B <ce script> RACINE

1. vérifie l'empreinte du brouillon 1 et celles des pièces citées ; 2. applique les couples (chaque « ancien » présent le nombre
de fois déclaré, chaque « nouveau » absent avant) ; 3. **tout le reste égal à l'octet** : couples défaits dans l'ordre inverse →
brouillon 1 octet pour octet ; 4. vérifie : aucun identifiant de modèle ; le marqueur `<<NOUVELLE_LIGNE_CODE_T07>>` une fois ;
l'ancienne ligne `CODE-T07` recopiée égale à l'octet à celle du registre au commit de fusion (passée en argument par la
recopie de ce script, vérifiée contre l'empreinte du registre) ; 5. écrit la cible (refus si elle existe, R12).
Code 0 et « TOUT PASSE », sinon code 1.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

SOURCE = "brouillons/T0.7-addendum-cache-motifs-v1-brouillon1.md"
SHA_SOURCE = "1369c4814f6aea7ea81839b538344a25499c0d10df1e210eb499ca8f221997cd"
CIBLE = "brouillons/T0.7-addendum-cache-motifs-v1-brouillon2.md"
P = "docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1"
M = f"{P}/relance-v2-preparation-v1"
C7 = "c2fab6cc7267b76228a75dc3e2e08bc7aa038961"
ANCIENNE = ("| CODE-T07 | 2026-11-11T05:40:34Z | registres/code-t07/CODE-T07-v2.json | "
            "d5eb0b665df187d158fa84deff733b0f382fc309510163625f7aaea1ae9a692c |")
SHA_REGISTRE_FUSION = "9061a5dab171b111223b9596b6a042718a51bce250152c54eeee4f5d29d96265"
PIECES = {
    "registres/code-t07/CODE-T07-v3.json": "d3eaebfe1842f06c042e4cfffc2038f08973a544a8a10ccffa0c6109a566c218",
    f"{P}/correction-cache-motifs-v1/contre-lecture-correctif-cache-v1.md":
        "774b2c38939a0ccf8037e17542a44602bded1e66f931f65e05684eb3933612a4",
    "scripts/remplacer_ligne_code_t07_v1.py": "a89e2226839a4492d6300659fdd560d150c96998a7249932efb768b183d5925c",
    "tests/test_remplacer_ligne_code_t07_v1.py": "0a1210da9060eee2715eebe556261ea96193ce2b002d071cb192484ff5ebfb7f",
    f"{M}/mesure-att-c2fab6cc-sortie-v1.txt": "9fdbffd20f2ede38348a604e2cf341081f8b39c538e8c26164acc7bd1409fb04",
    f"{M}/mesure-att-c2fab6cc-zen-sortie-v1.txt": "ec085121acb06ebe619e8702a08d3b4ab37c98af3440ec4bf4d229721c4ebf48",
    f"{M}/mesure-att-c2fab6cc-journal-v1.txt": "697b434773acc52e1131515728d5e2698cfb035e649237235f8ff1175139148d",
    f"{M}/mesure-att-c2fab6cc-liste-v1.txt": "0bbf21adeaaa014630786d7408fce1a521d558525b1ec9356f4a56dffcc60feb",
}
ATT_DEFAUT = "500 passed, 2 skipped, 4 xfailed, 1 warning"
ATT_ZEN = "500 passed, 2 skipped, 4 xfailed"

S0 = """## 0. Ce qui change depuis le brouillon 1

| Couple | Où | Changement | Source |
|---|---|---|---|
| AD2-01 | en-tête | identifiant de modèle de l'auteur remplacé par « modèle A » | consigne de la mère (aucun identifiant de modèle dans les fichiers) |
| AD2-02 à AD2-07 | titre, en-tête | brouillon 2 ; auteur et date ; registre cité (R-2601, R-2602, R-2604) ; contre-lecture rendue ; statut | R-2602, R-2604 |
| AD2-08 | § 0 | ce tableau | — |
| AD2-09 | § 1 | deux écarts liés : ligne `CODE-T07` remplacée une seule fois ; ordre d'exécution version 2 | R-2604 |
| AD2-10 | § 3.1 | fusion dans `main` (`c2fab6cc`) | R-2604 |
| AD2-11 | § 3.3 | `registres/code-t07/CODE-T07-v3.json` écrit au commit de fusion, vingt-six empreintes égales à la pièce | R-2604 |
| AD2-12 | § 3.4 | mesure de `ATT` au commit de fusion (§ 11 bis de l'ordre) | — |
| AD2-13 | § 3.5 | valeurs de l'ordre version 2 | R-2601 |
| AD2-14 | § 4 | **m-2** : « présence de chaque fichier préchargé » : épinglé par l'essai pour l'index et les quatre morceaux, vérifié à la main pour les autres | R-2602, m-2 |
| AD2-15, AD2-16 | § 5 | **m-4** (`passe_blanc_v1` et `v2` lisent la première ligne ; l'ordre fixe le nom du fichier) ; **décision** R-2604 : remplacement unique ; ancienne ligne recopiée à l'octet ; nouvelle ligne au marqueur ; outil et essais | R-2602, m-4 ; R-2604 |
| AD2-17 | § 5 bis | **m-3** : quatre fichiers dérivés de 7a posés sur l'instance : point ouvert devenu réserve | R-2602, m-3, § 6 |
| AD2-18 | § 6 | réserves 6 (**m-1**, mutation survivante) et 7 (fichiers de 7a) | R-2602, m-1 |
| AD2-19 | § 7 | pièces neuves | — |

m-5 (libellé « absent du cache local » pour toute erreur, hors du différentiel) : sans geste ici ; c'est la réserve 1, inchangée.

"""

MESURE = f"""- **Brouillon 2 : mesure à C7 = `{C7}`** (préparateur du brouillon 2, 2026-11-13, de 22:24:09 à 22:52:22 UTC,
  `date -u` ; méthode du § 11 bis de l'ordre, comme ci-dessus, **sans écart aux lignes sourcées** : clone partiel de la seule
  `main`, dont `origin/main` = C7 ; lignes 132-169 et 171-198 du script v4 telles quelles ; S7 = C7 ; configuration
  `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`, présente à ce commit ; `RUN6` = run de 7b de l'ordre ; périmètre `JD,JA`) :
  2 758 fichiers extraits ; arbres `src/` `027496897d73d82ab30eb3550a2117f0fef8ab0b` (celui de `799ef383`), `tests/`
  `42d9f073f5ddb0443bbbed8979b4a9629da05b9b` (ceux de `799ef383` plus des essais d'autres tâches, hors du motif) ; vingt-cinq
  fichiers d'essais, liste `0bbf21ad…` égale à celle de la mesure ci-dessus. **Mesure** : code 0, « {ATT_DEFAUT} » (Python
  3.13.18, Xeon à AVX-512) ; **diagnostic `OPENBLAS_CORETYPE=Zen`** : code 0, « {ATT_ZEN} » ; sauts et échecs attendus
  identiques à l'octet entre les deux passages et égaux à ceux des mesures de C7 de la v1 et de `799ef383` (`c19283515dc2…`) ; `src/` et `tests/` non écrits. Pièces : `{M}/` (§ 7). Les fichiers de 7a
  posés par l'extraction n'ont pas été ouverts ; clone supprimé.
"""

DECISION = f"""
**Brouillon 2 (m-4 de la contre-lecture)** : `passe_blanc_v1` et `passe_blanc_v2` lisent aussi la **première** ligne
(`lire_lignes_actuelles`, l. 327 et l. 335) ; l'ordre scellé fixe le nom `CODE-T07-v2.json` (P6, l. 259 ; commande de la l. 291) :
la voie retenue touche l'ordre version 2 dans tous les cas.

**Décision (R-2604 (1), mot de Lazar « go recos », option (a))** : la ligne `CODE-T07` est **remplacée une seule fois**, en place,
par un script éprouvé qui vérifie l'ancienne ligne à l'octet ; **écart déclaré** à la règle « lignes ajoutées, jamais réécrites »
(en-tête du registre ; docstring de `registre_v1` ; `ajouter_ligne` refuse une clé présente). Raison : seule voie qui ne touche ni
le code épinglé, ni le script v4, ni la configuration v8 (voies 2 à 4 de la contre-lecture, § 5).

- **Ancienne ligne**, recopiée à l'octet (registre des scellements au commit de fusion `{C7[:8]}`, `{SHA_REGISTRE_FUSION}`,
  septième ligne) :

```
{ANCIENNE}
```

- **Nouvelle ligne** : `<<NOUVELLE_LIGNE_CODE_T07>>` — construite par `registre_v1.ecrire_ligne` (clé `CODE-T07`, heure `date -u`
  du remplacement, chemin `registres/code-t07/CODE-T07-v3.json`, empreinte `d3eaebfe1842f06c042e4cfffc2038f08973a544a8a10ccffa0c6109a566c218`) ;
  la mère la recopie ici à l'octet, depuis la trace, avant le scellement de l'addendum.
- **Outil** : `scripts/remplacer_ligne_code_t07_v1.py` (`{PIECES['scripts/remplacer_ligne_code_t07_v1.py']}`), deux commandes :
  `construire` (la ligne neuve, au format exact) et `remplacer` (avec `--a-blanc` pour tout contrôler sans rien écrire). Refus,
  rien d'écrit, si : registre hors UTF-8 strict ou à séparateurs autres que « \\n » ; pas **exactement une** ligne `CODE-T07` ;
  ligne différente **d'un octet** de l'ancienne attendue ; nouvelle ligne mal formée (format exact de `ecrire_ligne`, clé,
  chemin relatif au motif que recopie le script de l'instance, chemin autre que l'ancien, fichier cité scellé et de la forme
  d'un fichier `CODE-T07`, date strictement postérieure à l'ancienne et non future) ; une ligne `OUVERTURE-T07` au journal des
  ouvertures ; fichier de trace ou son compagnon déjà présent. Sinon : remplacement en place (fichier temporaire, `os.replace`),
  octets hors de la ligne contrôlés identiques avant et après l'écriture, trace scellée (ancienne et nouvelle lignes, heure
  `date -u`, empreintes du registre avant et après, empreinte de l'outil).
- **Essais** : `tests/test_remplacer_ligne_code_t07_v1.py` (`{PIECES['tests/test_remplacer_ligne_code_t07_v1.py']}`), 28 cas, tous sur
  des copies du registre au commit de fusion : cas sain (seule la ligne change, autres octets gardés même irréguliers, ligne en
  première et en dernière position, trace scellée, seconde exécution refusée) ; après remplacement, `lire_registre_t07` et la
  garde « exactement une » (clés de l'étape A, marques de la configuration v8), `lire_lignes_actuelles`, `verifier_lignes` et
  `code_t07_v1 verifier` acceptent la copie ; témoins (ligne ajoutée au lieu d'être remplacée : refus de la garde ; ancienne
  ligne : `verifier` refuse l'arbre corrigé ; dépôt jetable : refus avant, acceptation après) ; dix fautes de registre ou de
  trace, cinq anciennes lignes à un octet près, dix-neuf nouvelles lignes fautives, registre changé pendant les contrôles :
  refus, rien d'écrit ; ligne de commande (code 0, code 2). Quatorze mutations de l'outil sur quinze attrapées (la survivante
  retire un contrôle interne redondant). **Jamais exécuté sur le vrai registre par le préparateur.**
- **Effets** : la ligne garde sa place ; sa date devient postérieure à celles des lignes qui la suivent : aucun lecteur du
  registre des scellements n'en exige l'ordre (`registre_v1`, `lecture_v2`, `code_t07_v1` : antériorité stricte de `CODE-T07` à
  l'instant d'ouverture et à la première `OUVERTURE-T07` seulement ; les règles de dates croissantes ne visent que le journal et
  les préalables de P3-bis). L'ancienne ligne ne reste que dans l'historique git, dans la trace et ici ; `CODE-T07-v2.json`
  reste versé, jamais plus cité. Le remplacement précède la création (l'instance lit le registre de `main`) ; le journal des
  ouvertures de `main` n'a aucune ligne (aucune ouverture, R-2588).
- **Essai neuf et S7** : l'essai neuf est sous `tests/` ; il entre dans `main` **après** S7 (ordre v2, P9), sinon
  `git diff --quiet C7 S7 -- src tests` refuse à l'étape 2 du script.
"""

BIS = """## 5 bis. Point ouvert devenu réserve : quatre fichiers dérivés de 7a posés sur l'instance (m-3)

- **Fait** (contre-lecture, § 6 ; script v4, l. 133-148) : le motif `/docs/notes/g0-deux-semaines-v1/` de l'étape 2 extrait tout
  le dossier, donc aussi `docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/` : quatre fichiers suivis (noms seuls, lus par
  `git ls-tree` : `garde-equivalence-20261109-070232-t06-reel-exploratoire-non-opposable-r522.json`,
  `lecture-A-exploratoire-non-opposable-v1.md` et leurs compagnons), pièces exploratoires et non opposables (R-2040, selon la
  contre-lecture). État identique au lancement de la v1.
- **Rien ne les lit** : au commit de fusion, aucun module de `src/`, aucun essai `tests/test_t07_*.py`, ni le script v4, ni la
  configuration v8, ni les exigences de paquets ne nomment ces fichiers ni leur dossier (recherche des noms par `git grep`
  restreint à ces chemins) ; les parcours de dossiers du module et de ces essais (`glob`, `rglob`, `os.walk`, `iterdir`) visent
  des dossiers temporaires ou nommés (`runs/`, `diag/`, `donnees/<run>/`, le module). Seuls `scripts/extraire_garde_equivalence_t06_v1.py`
  et `tests/test_depot_expurge_v6.py` les nomment, hors de l'étape 6. Les poussées de l'instance sont par chemins explicites :
  rien de ce dossier ne sort de l'instance.
- **Lettre de l'ordre** : le § 2.2 de l'ordre v1 vise `donnees/lecture-b-7a-quarantaine-v1`, `essai/t06-explo-v3` et `diag/`,
  `runs/`, `donnees/` de 7a ; `docs/notes/` n'y figure pas.
- **Retrait** : demandé par la mère « juste après l'extraction et avant l'étape 6, sans changer le script » ; **pas possible** :
  l'instance joue le script seule (mode « args », aucun serveur SSH), sans pause entre l'étape 2 et l'étape 6, et la fille n'y a
  aucun accès ; une boucle d'effacement ajoutée à la commande de création changerait la commande du § 4.4, ne serait pas
  répétée et serait en course avec l'étape 2. (Le retrait ne casserait aucun contrôle : ceux de propreté visent `src/` et
  `tests/` — étapes 3 et 6 — ou `src/controle_ia/` — `CODE-T07` —, et les poussées n'ajoutent que des chemins nommés.) Une
  exclusion propre demande un script v5 (motif `!/docs/notes/g0-deux-semaines-v1/e3-ter-v1/`), donc empreinte, répétition et
  contre-lecture neuves : hors de la correction minimale.
- **Proposé et porté** : **réserve** (§ 6, réserve 7), et, dans l'ordre version 2, un embargo écrit pour la fille (§ 2, point
  2 bis : jamais ouverts, affichés, hachés, listés ni recherchés) et le constat S-18 (script v5 au choix de la mère).
"""

COUPLES = [
    ("AD2-01", "sous-agent de la session mère (Claude Opus 5.5, `claude-opus-5-5`), sur la consigne de la mère",
     "sous-agent de la session mère (modèle A), sur la consigne de la mère", 1),
    ("AD2-02", "(option (a), R-2593) — v1, brouillon 1\n", "(option (a), R-2593) — v1, brouillon 2\n", 1),
    ("AD2-03", "- **Date (UTC)** : brouillon 1, 2026-11-13, de 21:12 à 22:02 (`date -u`).\n",
     "- **Date (UTC)** : brouillon 1, 2026-11-13, de 21:12 à 22:02 (`date -u`).\n"
     "- **Brouillon 2** : préparateur neuf (modèle A), sous-agent de la session mère, sur sa consigne qui suit R-2604 ; il n'a écrit\n"
     "  ni T0.7, ni le module, ni le correctif, ni l'essai du § 3.2, ni le brouillon 1, ni la contre-lecture ; **il n'a pas ouvert le\n"
     "  texte scellé de T0.7**. 2026-11-13, de 22:20 à 22:52 UTC (`date -u`). **Brouillon 2 = brouillon 1** (`1369c481…`,\n"
     "  gardé tel quel, R12) **+ les couples AD2-01 à AD2-19** du script\n"
     "  `brouillons/T0.7-addendum-cache-motifs-v1-brouillon2-appliquer-v1.py` ; tout le reste égal à l'octet au brouillon 1 (vérifié\n"
     "  par le script : couples défaits → brouillon 1). Ce qui change : § 0.\n", 1),
    ("AD2-04", "  R-2321, R-2588, R-2589, R-2592, R-2593.\n",
     "  R-2321, R-2588, R-2589, R-2592, R-2593 ; **brouillon 2** : R-2601, R-2602 et R-2604, au commit de fusion\n"
     f"  `{C7}` (`a588df8c7da28e8b8f7457bf6ff55690cea63015a97022fb02359b144935b725`).\n", 1),
    ("AD2-05", "- **Contre-lecture (R2)** : à faire, par un lecteur neuf d'un autre modèle (R-2593). Rien de ce brouillon n'est contre-lu.\n",
     "- **Contre-lecture (R2)** : brouillon 1 **contre-lu** (R-2602) :\n"
     f"  `{P}/correction-cache-motifs-v1/contre-lecture-correctif-cache-v1.md` (`774b2c38…`, lecteur neuf, modèle B ≠ modèle A de\n"
     "  l'auteur) : code `799ef383` « fusionnable », brouillon 1 « exact », compléments m-2 à m-4 (appliqués ici), mutation\n"
     "  survivante m-1 (réserve 6). **Les ajouts du brouillon 2 (couples AD2) ne sont pas contre-lus** : à contre-lire (R2) avec\n"
     "  l'ordre d'exécution version 2, brouillon 1.\n", 1),
    ("AD2-06", "- **Statut** : brouillon 1, **non scellé**", "- **Statut** : brouillon 2, **non scellé**", 1),
    ("AD2-07", "  Il ne régit rien avant la contre-lecture, le scellement et l'inscription par la mère.",
     "  Il ne régit rien avant la contre-lecture, le scellement et l'inscription par la mère (brouillon 2 : et avant que la mère\n"
     "  y recopie la nouvelle ligne `CODE-T07`, § 5).", 1),
    ("AD2-08", "## 1. Écart déclaré\n", S0 + "## 1. Écart déclaré\n", 1),
    ("AD2-09", "`CODE-T07`, C7), et à l'ordre d'exécution scellé, qui fixe C7, S7, `SRC7`, `ATT` et le fichier de la ligne `CODE-T07`.\n",
     "`CODE-T07`, C7), et à l'ordre d'exécution scellé, qui fixe C7, S7, `SRC7`, `ATT` et le fichier de la ligne `CODE-T07`.\n\n"
     "**Brouillon 2** : deux écarts de plus, qui en découlent (R-2604) : (i) la ligne `CODE-T07` du registre des scellements est\n"
     "**remplacée une seule fois** (§ 5), écart à la règle du registre partagé « lignes ajoutées, jamais réécrites » ; (ii) l'étape A\n"
     "se rejoue sous l'**ordre d'exécution version 2** (`docs/procedures/ordre-execution-etape-a-t07-v2-brouillon1.md`, à contre-lire\n"
     "et sceller), qui remplace pour la relance l'ordre v1 (`docs/procedures/ordre-execution-etape-a-t07-v1.md`, `9b3a04da…` ; son\n"
     "brouillon 9, `37433297…`, est celui que cite le texte scellé, d'après la consigne de la fille v1) : valeurs neuves seulement\n"
     "(C7, S7, `SRC7`, `ATT`, fichier et ligne `CODE-T07`, `ANT0`, dossier, journal, étiquette), aucune règle changée.\n", 1),
    ("AD2-10", "  (`git push origin prep/t07-cache-motifs-v1`) ; rien fusionné.",
     "  (`git push origin prep/t07-cache-motifs-v1`) ; rien fusionné (brouillon 2 : **fusionné depuis dans `main` au commit\n"
     f"  `{C7}`**, parents `cc967f99` et `deaeee03` ; arbre `src/` `02749689…`, égal à celui de `799ef383` ;\n"
     "  R-2604).", 1),
    ("AD2-11", "fichier versé et jamais cité, comme `CODE-T07-v1.json`, R-2231).",
     "fichier versé et jamais cité, comme `CODE-T07-v1.json`, R-2231). **Brouillon 2** : fait :\n"
     "`registres/code-t07/CODE-T07-v3.json` écrit au commit de fusion par `python -m controle_ia.t07.code_t07_v1 ecrire . c2fab6cc\n"
     "registres/code-t07/CODE-T07-v3.json`, scellé (`d3eaebfe1842f06c042e4cfffc2038f08973a544a8a10ccffa0c6109a566c218`) ; champ\n"
     f"`commit` `{C7}` ; ses vingt-six empreintes **égales à celles de la pièce** `7dabdbc8…` (contrôlé par programme ;\n"
     "octets identiques hors de la ligne `commit`) ; seule `reextraction_p3_v1.py` diffère de `CODE-T07-v2.json`.", 1),
    ("AD2-12", "  (vérifié au commit `12d3b20b`) ; la ligne attendue sur un hôte à noyau AVX2 (voie retenue en R-2319) est celle du diagnostic\n  ci-dessus.\n",
     "  (vérifié au commit `12d3b20b`) ; la ligne attendue sur un hôte à noyau AVX2 (voie retenue en R-2319) est celle du diagnostic\n  ci-dessus.\n"
     + MESURE, 1),
    ("AD2-13", "fille (`-v2` à une reprise, § 1 de l'ordre). Le script v4 (`4b17d1f0…`) et la configuration v8 ne changent pas.\n",
     "fille (`-v2` à une reprise, § 1 de l'ordre). Le script v4 (`4b17d1f0…`) et la configuration v8 ne changent pas.\n\n"
     f"**Brouillon 2** (ordre version 2, brouillon 1) : C7 = `{C7}` ; `SRC7` = `799ef38390c1df7790691a848ceb344dd9a81d54`\n"
     "(dernier commit contre-lu, R-2602 ; arbre `src/` égal à celui de C7) ; S7 au marqueur `COMMIT_SCELLEMENT_T07_V2` (commit de\n"
     "`main` descendant de C7, mêmes `src/` et `tests/`, qui porte les pièces de la relance) ; `ATT` au marqueur `ATT_C7_T07_V2`\n"
     f"(proposée : « {ATT_ZEN} », § 3.4) ; `registres/code-t07/CODE-T07-v3.json` et la ligne remplacée (§ 5) ; `ANT0` = 0,43 USD\n"
     "(estimation inscrite, facture à relever) ; dossier `/home/user/etape-a-t07-b-v2/`, journal `journal-etape-a-t07-b-v2.md`,\n"
     "étiquette `t07-b-v2` ; branche de sortie `donnees/t07-etape-a-v1` gardée (absente du distant, 2026-11-13T22:34:03Z).\n", 1),
    ("AD2-14", "la présence de chaque fichier\n  préchargé.\n",
     "la présence de chaque fichier\n  préchargé (brouillon 2, m-2 : épinglé par l'essai pour l'index et les quatre morceaux ; vérifié à la main pour les autres\n"
     "  — sonde hors essai de la contre-lecture, § 2 : `generation_config.json` ou `special_tokens_map.json` absent, liste présente\n"
     "  → `GardeArret` ; réserve 6).\n", 1),
    ("AD2-15", "## 5. Point ouvert : une seule ligne `CODE-T07` au registre\n",
     "## 5. Une seule ligne `CODE-T07` au registre : remplacement unique (brouillon 2 : décision R-2604)\n", 1),
    ("AD2-16", "autre voie. Décision de la mère (nœud si la règle est celle du texte scellé) ; ce brouillon ne la tranche pas.\n",
     "autre voie. Décision de la mère (nœud si la règle est celle du texte scellé) ; ce brouillon ne la tranche pas.\n" + DECISION, 1),
    ("AD2-17", "## 6. Réserves\n", BIS + "\n## 6. Réserves\n", 1),
    ("AD2-18", "   (aucun réseau vers le dépôt du modèle, aucune dépense) ; le cache factice suit la reproduction du diagnostic.\n",
     "   (aucun réseau vers le dépôt du modèle, aucune dépense) ; le cache factice suit la reproduction du diagnostic.\n"
     "6. **Mutation survivante (m-1 de la contre-lecture)** : des motifs privés de `generation_config.json` et de\n"
     "   `special_tokens_map.json` (M8) passent les 21 cas de l'essai ; le comportement est juste (sonde hors essai : liste présente →\n"
     "   `GardeArret` ; sans liste → passe, comme à C7). Aucun cas paramétré ajouté : il demanderait un commit neuf, donc liste,\n"
     "   `ATT` et attestation à refaire ; réserve, au choix de la mère (R-2602).\n"
     "7. **Quatre fichiers dérivés de 7a sur le disque de l'instance** (§ 5 bis) : lus par rien, jamais touchés par la fille, détruits\n"
     "   avec l'instance ; leur exclusion demande un script v5 (ordre version 2, S-18).\n", 1),
    ("AD2-19", "| lignes 171-198 du script v4 de C7, telles quelles | `docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/correction-cache-motifs-v1/mesure-etape3-lignes-171-198-v1.sh` | `647afe5fdb33942273c60121ce9f0bd3d60703d33a762a2f21103b7b51968ebb` |\n",
     "| lignes 171-198 du script v4 de C7, telles quelles | `docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/correction-cache-motifs-v1/mesure-etape3-lignes-171-198-v1.sh` | `647afe5fdb33942273c60121ce9f0bd3d60703d33a762a2f21103b7b51968ebb` |\n"
     f"| **brouillon 2** : contre-lecture du correctif (R-2602) | `{P}/correction-cache-motifs-v1/contre-lecture-correctif-cache-v1.md` | `774b2c38939a0ccf8037e17542a44602bded1e66f931f65e05684eb3933612a4` |\n"
     f"| **brouillon 2** : fichier de la ligne `CODE-T07` (commit `{C7[:8]}`) | `registres/code-t07/CODE-T07-v3.json` | `{PIECES['registres/code-t07/CODE-T07-v3.json']}` |\n"
     f"| **brouillon 2** : outil du remplacement unique | `scripts/remplacer_ligne_code_t07_v1.py` | `{PIECES['scripts/remplacer_ligne_code_t07_v1.py']}` |\n"
     f"| **brouillon 2** : essais de l'outil (28 cas) | `tests/test_remplacer_ligne_code_t07_v1.py` | `{PIECES['tests/test_remplacer_ligne_code_t07_v1.py']}` |\n"
     f"| **brouillon 2** : mesure de `ATT` au commit de fusion, sortie | `{M}/mesure-att-c2fab6cc-sortie-v1.txt` | `{PIECES[f'{M}/mesure-att-c2fab6cc-sortie-v1.txt']}` |\n"
     f"| **brouillon 2** : diagnostic `OPENBLAS_CORETYPE=Zen`, sortie | `{M}/mesure-att-c2fab6cc-zen-sortie-v1.txt` | `{PIECES[f'{M}/mesure-att-c2fab6cc-zen-sortie-v1.txt']}` |\n"
     f"| **brouillon 2** : liste des 25 fichiers d'essais | `{M}/mesure-att-c2fab6cc-liste-v1.txt` | `{PIECES[f'{M}/mesure-att-c2fab6cc-liste-v1.txt']}` |\n"
     f"| **brouillon 2** : journal horodaté de la mesure | `{M}/mesure-att-c2fab6cc-journal-v1.txt` | `{PIECES[f'{M}/mesure-att-c2fab6cc-journal-v1.txt']}` |\n", 1),
]


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
    reg = subprocess_show(racine, f"{C7}:registres/scellements-v1.md")
    if sha(reg) != SHA_REGISTRE_FUSION or (ANCIENNE + "\n").encode() not in reg:
        echec("ancienne ligne CODE-T07 non égale à l'octet à celle du registre au commit de fusion")
    b1 = src.decode("utf-8")
    b2 = appliquer(b1, COUPLES)
    if "@@" in b2:
        echec("valeur non remplie (@@…@@) dans le texte")
    if defaire(b2, COUPLES) != b1:
        echec("couples défaits ≠ brouillon 1")
    for mot in ("Claude", "claude-opus", "Opus 5", "Fable 5", "Sonnet", "Haiku"):
        if mot in b2:
            echec(f"identifiant de modèle « {mot} » présent")
    if b2.count("<<NOUVELLE_LIGNE_CODE_T07>>") != 1 or b2.count("```\n" + ANCIENNE + "\n```") != 1:
        echec("marqueur de la nouvelle ligne ou recopie de l'ancienne ligne")
    cible = racine / CIBLE
    if cible.exists():
        echec(f"{CIBLE} existe déjà (R12)")
    cible.write_bytes(b2.encode("utf-8"))
    print(f"TOUT PASSE : {CIBLE} écrit ({sha(b2.encode('utf-8'))}) ; {len(COUPLES)} couples")
    return 0


def subprocess_show(racine: Path, objet: str) -> bytes:
    import subprocess
    return subprocess.run(["git", "-C", str(racine), "show", objet], capture_output=True, check=True).stdout


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
