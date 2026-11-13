"""Consigne de la session fille de l'étape A de T0.7, version 2, brouillon 1 : la consigne v1 remplie (`5fa7adcf…`, gardée telle
quelle, R12) plus les couples CF2-01 à CF2-19, adaptés à l'ordre d'exécution version 2 (relance après l'arrêt du 13 novembre,
R-2588 ; option (a), R-2593 ; ligne CODE-T07 remplacée une seule fois, R-2604) — v1.

Préparateur neuf (modèle A), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-13. Bibliothèque standard
seulement ; aucun réseau, aucune clé.

    <python du dépôt> -I -B <ce script> RACINE

1. vérifie l'empreinte de la consigne v1 remplie ; 2. applique les couples dans l'ordre, chaque « ancien » présent le nombre de
fois déclaré et chaque « nouveau » absent avant ; 3. **tout le reste égal à l'octet** : défait les couples dans l'ordre inverse
et exige la v1 octet pour octet ; 4. vérifie : aucun identifiant de modèle, cases ⟦…⟧ attendues (une occurrence chacune), aucune
trace de la v1 qui doive changer (`etape-a-t07-b-v1/`, `9d393130`, l'ordre v1 comme ordre à jouer) hors des mentions de mémoire ;
5. écrit la cible (refus si elle existe, R12). Code 0 et « TOUT PASSE », sinon code 1.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

DOSSIER = "docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1"
SOURCE = f"{DOSSIER}/consigne-fille-etape-a-v1-remplie.md"
SHA_SOURCE = "5fa7adcff2a0229a361ec030641734227c3989aa56d68850e3014447b4818947"
CIBLE = f"{DOSSIER}/consigne-fille-etape-a-v2-brouillon1.md"
ORDRE_V2 = "docs/procedures/ordre-execution-etape-a-t07-v2-brouillon1.md"

NOTE_V2 = """> **Version 2, brouillon 1 — note pour la mère (hors du texte envoyé)** — écrite le 2026-11-13 vers 23:00 UTC (`date -u`)
> par un préparateur neuf (modèle A, sous-agent de `session_01QPDgKgACWyCkCN8HjqwNXy` ; exclu ensuite de tout rôle de lecteur
> de P3-bis ; il n'a pas ouvert le texte scellé de T0.7). **Version 2, brouillon 1 = consigne v1 remplie** (`5fa7adcf…`,
> gardée telle quelle, R12) **+ les couples CF2-01 à CF2-19** du script
> `docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/consigne-fille-etape-a-v2-brouillon1-appliquer-v1.py` ; tout le
> reste égal à l'octet à la v1 (vérifié : couples défaits → v1). La note de la v1 qui suit est gardée pour mémoire.
> **Avant l'envoi** : (1) gestes de la relance (ordre v2, `ORDRE_V2`, § 0 septies) : contre-lecture (R2) de l'addendum de
> T0.7 (brouillon 2) et de l'ordre v2, scellement ; remplacement de la ligne `CODE-T07` par
> `scripts/remplacer_ligne_code_t07_v1.py` (trace scellée) ; marqueurs de l'ordre v2 remplis (`ID_SESSION_FILLE_V2`,
> `COMMIT_SCELLEMENT_T07_V2`, `ATT_C7_T07_V2`, `LIGNE_CODE_T07_V2`), ordre rempli scellé ; engagement neuf sous
> GO-2026-11-10-06 (`ANT0` = 0,43 USD) ; écrit daté de la relance (C7, S7, `SRC7` et P13 (iii), `ATT` avec le commit et les
> arbres de la mesure et `git diff --name-status C7 S7`, ligne `CODE-T07`, `ANT0`) ; l'essai neuf du remplacement entre dans
> `main` **après** S7 (ordre v2, P9) ; committer, pousser ; (2) session fille : la fille de la v1
> (`session_01QPDgKf6Rn3eTeuYMDCBiKA`, en attente depuis R-2592, crochet déjà éprouvé) ou une neuve **ouverte dans le dépôt**
> (crochet de garde, R-2545) ; (3) relire la liste des intouchables du § 3 contre l'inventaire du jour ; (4) remplacer
> chaque case `⟦…⟧` ci-dessous (**six cases, cinq valeurs** : chemin et empreinte de l'ordre v2 rempli, commit de remise
> (deux fois), écrits datés à recopier, ligne `CODE-T07` attendue ; aucune autre valeur à inventer) ; (5) envoyer le texte
> qui suit la ligne de séparation.

""".replace("`ORDRE_V2`", f"`{ORDRE_V2}`")

COUPLES = [
    # (identifiant, ancien, nouveau, nombre d'occurrences de l'ancien)
    ("CF2-01", "(Claude Opus 5.5, sous-agent de `session_01QPDgKgACWyCkCN8HjqwNXy`",
     "(modèle A, sous-agent de `session_01QPDgKgACWyCkCN8HjqwNXy`", 1),
    ("CF2-02", "# Consigne de la session fille qui joue l'étape A de T0.7 (variante B) — v1\n\n",
     "# Consigne de la session fille qui joue l'étape A de T0.7 (variante B) — v2, brouillon 1\n\n" + NOTE_V2, 1),
    ("CF2-03", "Tu es la **session fille porteuse des clés** qui joue l'**étape A de T0.7, variante B**, pour la session mère\n",
     "Tu es la **session fille porteuse des clés** qui joue l'**étape A de T0.7, variante B** — **relance sous l'ordre version 2**\n"
     "après l'arrêt du 13 novembre (code 2 à l'étape 8, contrôle du cache du modèle de P3, rien d'ouvert, instance 60541314\n"
     "détruite : R-2588 ; cause corrigée : R-2589, R-2593) —, pour la session mère\n", 1),
    ("CF2-04", "- **Mots de Lazar** : R-2555 (`registres/decisions.md`) : « A (a) go » = jouer maintenant l'étape A de T0.7.\n",
     "- **Mots de Lazar** : R-2555 (`registres/decisions.md`) : « A (a) go » = jouer maintenant l'étape A de T0.7 ; **relance** :\n"
     "  R-2593 (option (a) : correction minimale du contrôle du cache, ordre version 2, relance sous les mêmes lignes de GO,\n"
     "  plafond et date inchangés, aucune ligne de GO neuve) et R-2604 (ligne `CODE-T07` remplacée une seule fois).\n", 1),
    ("CF2-05", "  seulement** ; jamais de H200 (elle demande un mot de Lazar, hors de cette consigne).\n",
     "  seulement** ; jamais de H200 (elle demande un mot de Lazar, hors de cette consigne). **La dépense de la première instance\n"
     "  (60541314, ≈ 0,43 USD, R-2588) compte dans ces 20 USD** (`ANT0` de l'ordre v2).\n", 1),
    ("CF2-06", "- **Ordre à jouer, à la lettre** : `docs/procedures/ordre-execution-etape-a-t07-v1.md`,\n"
               "  empreinte `9b3a04da94610ad8df74a51a800547bc5d9e103d382ffec17e530051d662acb3`, égale à son compagnon. Il est le brouillon 9\n"
               "  (`374332976304d08af7c1b941d8798877d34f9e30b3945ba2be3ac19189740402`, celui que cite le texte scellé de T0.7) avec ses\n"
               "  marqueurs remplis, rien d'autre. **Jamais le brouillon 5** ni un autre brouillon.\n",
     "- **Ordre à jouer, à la lettre** : ⟦chemin de l'ordre version 2 rempli et scellé⟧,\n"
     "  empreinte ⟦empreinte de l'ordre version 2 rempli⟧, égale à son compagnon. C'est l'**ordre version 2** : l'ordre v1 scellé\n"
     "  (`docs/procedures/ordre-execution-etape-a-t07-v1.md`, `9b3a04da…`) plus les seules valeurs de la relance (son § 0 septies :\n"
     "  C7, S7, `SRC7`, `ATT`, fichier et ligne `CODE-T07`, `ANT0`, dossier, journal, étiquette ; quatre fichiers dérivés de 7a en\n"
     "  réserve), contre-lu, scellé, marqueurs remplis. **Jamais l'ordre v1** (il a servi au lancement arrêté), ni un brouillon.\n", 1),
    ("CF2-07", "  (tu ne le lis pas ; l'ordre le désigne par la ligne `SCELLEMENT-T07`).\n",
     "  (tu ne le lis pas ; l'ordre le désigne par la ligne `SCELLEMENT-T07`, inchangée). L'**addendum** de T0.7 qui déclare la\n"
     "  correction du cache et le remplacement de la ligne `CODE-T07` n'est pas à lire non plus : l'ordre v2 en porte les valeurs.\n", 1),
    ("CF2-08", "- **Commit de `main` à la remise** : `9d393130a9037a23be00fdce5e91573d2499099b` ; toutes les lignes de\n"
               "  registre et les écrits datés que l'ordre exige y sont.\n",
     "- **Commit de `main` à la remise** : ⟦commit de main à la remise de la v2⟧ ; toutes les lignes de registre (dont la ligne\n"
     "  `CODE-T07` remplacée) et les écrits datés que l'ordre v2 exige y sont. (V1 : `9d393130…`, lancement arrêté.)\n", 1),
    ("CF2-09", "- **Écrits datés de la mère à recopier à l'octet dans ton journal avant la création** (P3, P12, P13 (iii), P14) :\n"
               "  `lignes R-2564 (P14 = 5760 ; trois lignes d'écrit des préalables de P3-bis) et R-2566 (ordre rempli, lignes de registre, engagement, écrits datés (a) à (h) de la mère) de `registres/decisions.md`, à recopier au journal mot pour mot avant la création`.\n",
     "- **Écrits datés de la mère à recopier à l'octet dans ton journal avant la création** (P3, P6, P12, P13 (iii), P14) :\n"
     "  ⟦écrits datés de la v2 : au moins R-2564 (P14) et l'écrit daté de la relance (C7, S7, SRC7, ATT et sa mesure, ligne CODE-T07, ANT0, engagement)⟧.\n"
     "  (V1 : R-2564 et R-2566.)\n", 1),
    ("CF2-10", "8. **Arrêts par identifiant seulement (R10)** : jamais `pkill`, `killall`, ni arrêt par motif.\n",
     "8. **Arrêts par identifiant seulement (R10)** : jamais `pkill`, `killall`, ni arrêt par motif.\n"
     "9. **Fichiers dérivés de 7a** (ordre v2, § 2, point 2 bis) : jamais `docs/notes/g0-deux-semaines-v1/e3-ter-v1/` — ni ouvert,\n"
     "   ni affiché, ni haché, ni listé, ni recherché, dans aucun clone. Le script les pose sur le disque de l'instance ; tu n'y\n"
     "   fais rien : c'est une réserve écrite, pas un geste.\n", 1),
    ("CF2-11", "   `git merge-base --is-ancestor 9d393130a9037a23be00fdce5e91573d2499099b HEAD` doit réussir.\n",
     "   `git merge-base --is-ancestor ⟦commit de main à la remise de la v2⟧ HEAD` doit réussir.\n", 1),
    ("CF2-12", "5. Lis l'ordre rempli **en entier**, puis `CLAUDE.md`.\n",
     "5. Lis l'ordre v2 rempli **en entier** (son § 0 septies d'abord), puis `CLAUDE.md`.\n", 1),
    ("CF2-13", "1. Dossier **neuf** `/home/user/etape-a-t07-b-v1/` (s'il existe : arrêt, compte rendu ; `-v2` seulement sur écrit de la\n"
               "   mère). Écris d'abord la ligne `SCELLEMENT-T07` du marqueur `LIGNE_SCELLEMENT_T07` à l'octet dans\n"
               "   `$W/ligne-scellement-t07.txt` (`printf '%s\\n' '<la ligne>'`), puis recopie au journal les écrits datés du § 1.\n",
     "1. Dossier **neuf** `/home/user/etape-a-t07-b-v2/` (l'ordre v2 est l'écrit de la mère qui le fixe ; s'il existe : arrêt,\n"
     "   compte rendu ; `/home/user/etape-a-t07-b-v1/` reste tel quel, jamais réutilisé). Écris d'abord la ligne `SCELLEMENT-T07`\n"
     "   du marqueur `LIGNE_SCELLEMENT_T07` à l'octet dans `$W/ligne-scellement-t07.txt` (`printf '%s\\n' '<la ligne>'`), puis la\n"
     "   ligne `CODE-T07` attendue à l'octet dans `$W/ligne-code-t07.txt` (`printf '%s\\n' '⟦ligne CODE-T07 attendue, marqueur LIGNE_CODE_T07_V2 de l'ordre v2⟧'` ;\n"
     "   P6 de l'ordre v2), puis recopie au journal les écrits datés du § 1.\n", 1),
    ("CF2-14", "   ligne porte « , 1 warning » (hôte à instructions AVX-512), c'est la réserve écrite au remplissage (R-2319) : destruction,\n",
     "   ligne porte « , 1 warning » (hôte à instructions AVX-512), c'est la réserve écrite au remplissage (R-2319 ; ordre v2, P12 :\n"
     "   `ATT` sans avertissement, mesurée sous noyau « Zen ») : destruction,\n", 1),
    ("CF2-15", "`$W/journal-etape-a-t07-b-v1.md`, une ligne datée par geste (`date -u`). À la fin :\n",
     "`$W/journal-etape-a-t07-b-v2.md` (neuf ; v2), une ligne datée par geste (`date -u`). À la fin :\n", 1),
    ("CF2-16", "PYTHONPATH=src python3 -m controle_ia.scellement sceller /home/user/etape-a-t07-b-v1/journal-etape-a-t07-b-v1.md\n",
     "PYTHONPATH=src python3 -m controle_ia.scellement sceller /home/user/etape-a-t07-b-v2/journal-etape-a-t07-b-v2.md\n", 1),
    ("CF2-17", "GH_TOKEN\") if len(os.environ.get(k,\"\"))>=8 and os.environ[k] in t))' /home/user/etape-a-t07-b-v1/journal-etape-a-t07-b-v1.md\n",
     "GH_TOKEN\") if len(os.environ.get(k,\"\"))>=8 and os.environ[k] in t))' /home/user/etape-a-t07-b-v2/journal-etape-a-t07-b-v2.md\n", 1),
    ("CF2-18", "   branche `donnees/t07-etape-a-v1` ; tu vérifies (ordre, § 4.6), tu ne repousses jamais rien.\n",
     "   branche `donnees/t07-etape-a-v1` (inchangée en v2 : absente du distant, l'instance de la v1 s'étant arrêtée avant de la\n"
     "   créer) ; tu vérifies (ordre, § 4.6), tu ne repousses jamais rien.\n", 1),
    ("CF2-19", "Tu as fini quand l'instance créée est détruite (texte exact relevé), l'inventaire final envoyé, le journal scellé et\n",
     "Tu as fini quand l'instance créée (étiquette `t07-b-v2`) est détruite (texte exact relevé), l'inventaire final envoyé, le journal scellé et\n", 1),
]

CASES = ["⟦chemin de l'ordre version 2 rempli et scellé⟧", "⟦empreinte de l'ordre version 2 rempli⟧",
         "⟦commit de main à la remise de la v2⟧", "⟦ligne CODE-T07 attendue, marqueur LIGNE_CODE_T07_V2 de l'ordre v2⟧"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def appliquer(texte: str, couples) -> str:
    for cid, ancien, nouveau, n in couples:
        if texte.count(ancien) != n:
            raise SystemExit(f"ÉCHEC {cid} : « ancien » présent {texte.count(ancien)} fois, {n} attendu(s)")
        if texte.count(nouveau) != 0:
            raise SystemExit(f"ÉCHEC {cid} : « nouveau » déjà présent")
        texte = texte.replace(ancien, nouveau)
        if texte.count(nouveau) != n:
            raise SystemExit(f"ÉCHEC {cid} : « nouveau » présent {texte.count(nouveau)} fois après application")
    return texte


def defaire(texte: str, couples) -> str:
    for cid, ancien, nouveau, n in reversed(couples):
        if texte.count(nouveau) != n:
            raise SystemExit(f"ÉCHEC défaire {cid} : « nouveau » présent {texte.count(nouveau)} fois, {n} attendu(s)")
        texte = texte.replace(nouveau, ancien)
    return texte


def main(argv: list[str]) -> int:
    racine = Path(argv[0]) if argv else Path(".")
    src = (racine / SOURCE).read_bytes()
    if sha(src) != SHA_SOURCE:
        raise SystemExit(f"ÉCHEC : {SOURCE} {sha(src)[:12]}… ≠ {SHA_SOURCE[:12]}…")
    v1 = src.decode("utf-8")
    v2 = appliquer(v1, COUPLES)
    if defaire(v2, COUPLES) != v1:
        raise SystemExit("ÉCHEC : couples défaits ≠ v1")
    for mot in ("Claude Opus", "Claude Fable", "claude-opus", "Opus 5", "Fable 5", "Sonnet", "Haiku"):
        if mot in v2:
            raise SystemExit(f"ÉCHEC : identifiant de modèle « {mot} » présent")
    attendu = {CASES[0]: 1, CASES[1]: 1, CASES[2]: 2, CASES[3]: 1}
    for case, k in attendu.items():
        if v2.count(case) != k:
            raise SystemExit(f"ÉCHEC : case {case} présente {v2.count(case)} fois, {k} attendue(s)")
    envoye = v2.split("\n---\n", 1)[1]
    if envoye.count("⟦") != 6:
        raise SystemExit(f"ÉCHEC : {envoye.count('⟦')} cases dans le texte envoyé, 6 attendues")
    for interdit in ("etape-a-t07-b-v1/journal", "9d393130a9037a23be00fdce5e91573d2499099b",
                     "`docs/procedures/ordre-execution-etape-a-t07-v1.md`,\n  empreinte"):
        if interdit in envoye:
            raise SystemExit(f"ÉCHEC : trace de la v1 à changer encore présente : {interdit!r}")
    cible = racine / CIBLE
    if cible.exists():
        raise SystemExit(f"ÉCHEC : {CIBLE} existe déjà (R12)")
    cible.write_bytes(v2.encode("utf-8"))
    print(f"TOUT PASSE : {CIBLE} écrit ({sha(v2.encode('utf-8'))}) ; {len(COUPLES)} couples")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
