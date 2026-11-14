"""Ordre d'exécution de l'étape A de T0.7, variante B, **version 2, brouillon 2** : la v2, brouillon 1 (`522c68ed…`, versée, gardée
telle quelle, R12) plus les couples OB2-01 à OB2-20 — corrections de la contre-lecture des pièces de relance (R-2614,
`relance-v2-preparation-v1/contre-lecture-relance-v2-v1.md`, `703195e5…`) : MA-2 (renvoi à la suite unique des gestes de la mère ;
l'ordre cite l'addendum **scellé**, marqueur neuf), MA-3 (aucun fichier de `src/` ni de `tests/` entre C7 et S7), m-1 (les fichiers
de `e3-ter-v1/`), m-2 (`ATT` remplie), m-3 (plus de jeton à chevrons hors des marqueurs), m-7 (libellés de la v1) ; plus la
réserve au compte rendu (§ 8) que demande la contre-lecture, § 5 — v1.

Préparateur (modèle A), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-13. Bibliothèque standard et
`bash -n` seulement ; aucun réseau, aucune clé.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE

Vérifie les empreintes ; applique les couples ; exige que les couples défaits redonnent le brouillon 1 à l'octet ; vérifie :
titre ; aucun identifiant de modèle ; exactement quatre marqueurs `<<…>>`, une occurrence chacun ; `ATT` remplie dans la ligne
(A) ; blocs `bash` (`bash -n`, marqueurs remplacés par des valeurs factices) ; § 6 égal ; écrit la cible (refus si elle existe).
Code 0 et « TOUT PASSE », sinon code 1.
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SOURCE = "docs/procedures/ordre-execution-etape-a-t07-v2-brouillon1.md"
SHA_SOURCE = "522c68ed8349e7d1fedb26840bdb3853e3a48822f7506a82406515054d4c8a66"
CIBLE = "docs/procedures/ordre-execution-etape-a-t07-v2-brouillon2.md"
E = "docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/relance-v2-preparation-v1"
GESTES = f"{E}/gestes-mere-relance-v2-v1.md"
PIECES = {
    f"{E}/contre-lecture-relance-v2-v1.md": "703195e515480fcff2f4dc60cd4ca5bffedc4e930e24f6d4711eaa57386fc5fd",
    "brouillons/T0.7-addendum-cache-motifs-v1-brouillon3.md": "9c85cde7220a312f1e328ece4fbec29ad64ce426a79ca5d87218e6002fc32702",
    "scripts/remplacer_ligne_code_t07_v2.py": "0e7c3c0cbf4b052b1a2852ef49fb2135337dc110c0af7dbf4f066509207204bb",
}
ATT = "500 passed, 2 skipped, 4 xfailed"
REGLE_MA3 = ("**aucun fichier de `src/` ni de `tests/`, de quelque tâche que ce soit, n'entre dans `main` entre C7 et S7** (MA-3 de "
             "la contre-lecture R-2614 ; sinon `git diff --quiet C7 S7 -- src tests` refuse, au § 4.1 et à l'étape 2 du script) ; les "
             "essais de l'outil du remplacement restent sous `relance-v2-preparation-v1/essais-outil/` jusqu'à la fin de l'étape A "
             "(instance détruite), pour qu'un S7 refait reste possible")

S0OCTIES = f"""## 0 octies. Ce qui change depuis la v2, brouillon 1 (version 2, brouillon 2 : contre-lecture R-2614)

Source : contre-lecture des pièces de relance (`{E}/contre-lecture-relance-v2-v1.md`, `703195e5…`, lecteur neuf, modèle B :
« après corrections », 0 bloquant ; valeurs de la v2 vérifiées). **Gestes de la mère avant l'envoi : une seule suite, numérotée,
dans `{GESTES}`** (remplacement, recopie de la nouvelle ligne dans l'addendum, scellement de l'addendum, commit S7, vérifications,
remplissage et scellement de cet ordre, remise ; essais de l'outil sous `tests/` seulement après la fin de l'étape A).

| Couple | Où | Changement | Constat |
|---|---|---|---|
| OB2-01 à OB2-03 | titre ; statut ; § 0 octies | brouillon 2 ; renvoi à la suite des gestes | MA-2 |
| OB2-04, OB2-05 | encadré ; § 0 | mentions de la v1 (`a621dcd3`, « commit de scellement S7 ») dites v1 | m-7 |
| OB2-06 à OB2-08 | encadré ; texte qui régit ; § 0 septies | l'addendum cité est l'addendum **scellé** (marqueur neuf `ADDENDUM_T07_SCELLE_V2`) | MA-2 |
| OB2-09, OB2-15 | § 0 septies ; P9 ; § 12 | règle générale : aucun fichier de `src/` ni de `tests/` entre C7 et S7 | MA-3 |
| OB2-10 à OB2-12, OB2-19 | encadré ; § 0 septies ; § 2, point 2 bis ; S-18 | les fichiers de `e3-ter-v1/`, sans compte | m-1 |
| OB2-13, OB2-14, OB2-16, OB2-17 | ligne (A) ; P12 ; § 0 septies ; § 11 bis ; § 12 | `ATT` remplie : « {ATT} » | m-2 |
| OB2-18 | § 12 | « même texte que le marqueur `NOUVELLE_LIGNE_CODE_T07` » ; ligne neuve du marqueur `ADDENDUM_T07_SCELLE_V2` ; S7 sans l'ordre rempli (il le nomme) | m-3 ; MA-2 |
| OB2-20 | § 8 | réserve des fichiers de `e3-ter-v1/` portée au compte rendu de la fille | contre-lecture, § 5 |

Restent à remplir par la mère : `ID_SESSION_FILLE_V2`, `COMMIT_SCELLEMENT_T07_V2` (S7), `LIGNE_CODE_T07_V2` (après le
remplacement), `ADDENDUM_T07_SCELLE_V2` (après le scellement de l'addendum). Outil du remplacement : **v2**,
`scripts/remplacer_ligne_code_t07_v2.py` (`{PIECES['scripts/remplacer_ligne_code_t07_v2.py']}`, trace écrite avant le
remplacement, m-6). Tout le reste est égal à l'octet au brouillon 1 (vérifié par programme, statut).

"""

COUPLES = [
    ("OB2-01", "(instance A100 neuve, activations recalculées) — v2, brouillon 1\n",
     "(instance A100 neuve, activations recalculées) — v2, brouillon 2\n", 1),
    ("OB2-02", "- **Statut de la version 2** : **brouillon 1**",
     "- **Statut de la version 2, brouillon 2** : écrit le 2026-11-13 à partir de 23:35 UTC (`date -u`) par le préparateur du\n"
     "  brouillon 1 (modèle A), sur le message de la mère qui suit R-2614. **Brouillon 2 = brouillon 1** (`522c68ed…`, versé, gardé\n"
     "  tel quel, R12) **+ les couples OB2-01 à OB2-20** du script `docs/procedures/ordre-execution-etape-a-t07-v2-brouillon2-appliquer-v1.py` ;\n"
     "  tout le reste égal à l'octet au brouillon 1 (couples défaits → brouillon 1). Ce qui change : § 0 octies. **Gestes de la mère\n"
     f"  avant l'envoi : `{GESTES}`** (une seule suite). Les ajouts du brouillon 2 ne sont pas contre-lus.\n"
     "- **Statut de la version 2** : **brouillon 1**", 1),
    ("OB2-03", "## 1. Cadre\n", S0OCTIES + "## 1. Cadre\n", 1),
    ("OB2-04", "`a621dcd3` est le dernier commit contre-lu (P13 (iii), `SRC7`).\n> **Version 2, brouillon 1",
     "`a621dcd3` est le dernier commit contre-lu (P13 (iii), `SRC7`) (v1 ; v2 : `799ef383`).\n> **Version 2, brouillon 1", 1),
    ("OB2-05", "au commit de scellement S7 ;",
     "au commit de scellement S7 (v1 ; v2 : S7 est le commit de `main` qui porte les pièces de la relance, § 0 septies) ;", 1),
    ("OB2-06", "écart déclaré par l'addendum de T0.7 (brouillon 2).", "écart déclaré par l'addendum de T0.7 (scellé : § 0 septies).", 1),
    ("OB2-07", "écarts déclarés par\n  l'addendum de T0.7, brouillon 2).", "écarts déclarés par\n  l'addendum de T0.7 scellé, § 0 septies).", 1),
    ("OB2-08", "addendum de T0.7, brouillon 2 (`brouillons/T0.7-addendum-cache-motifs-v1-brouillon2.md`,\n"
               "`53ba8ea7365d808c3a409b2b08b312e9477e5d6971e9380f86c8d144e622e6fb`, non contre-lu).",
     "addendum de T0.7 **scellé** : `<<ADDENDUM_T07_SCELLE_V2>>` (chemin et empreinte, remplis par la mère après son scellement ;\n"
     "issu du brouillon 3, `brouillons/T0.7-addendum-cache-motifs-v1-brouillon3.md`, `9c85cde7…`, nouvelle ligne `CODE-T07` recopiée ;\n"
     "brouillon 2 : `53ba8ea7…`).", 1),
    ("OB2-09", "| Essai neuf du remplacement | P9 | — | entre dans `main` **après** S7 (sinon `git diff --quiet C7 S7 -- src tests` refuse) | constat du préparateur |",
     f"| Fichiers de `src/` et `tests/` entre C7 et S7 | P9 | — | {REGLE_MA3} | constat du préparateur ; MA-3 (R-2614) |", 1),
    ("OB2-10", "P12 rafraîchi ; quatre fichiers dérivés de 7a sur le disque de l'instance : réserve",
     "P12 rafraîchi ; les fichiers de `e3-ter-v1/` (dérivés de 7a) sur le disque de l'instance : réserve", 1),
    ("OB2-11", "**réserve** : posés sur l'instance par le motif d'extraction",
     "**réserve** : les fichiers de `e3-ter-v1/` (et tout fichier du dossier extrait dont le nom désigne 7a), posés sur l'instance par le motif d'extraction", 1),
    ("OB2-12", "l'étape 2 du script pose sur le disque de l'instance **quatre fichiers dérivés de 7a**, sous\n",
     "l'étape 2 du script pose sur le disque de l'instance **les fichiers suivis de `docs/notes/g0-deux-semaines-v1/e3-ter-v1/`**\n"
     "   (brouillon 2, m-1 : tout le dossier, dont des fichiers nommés `audit-ecart-dt4-7a…`, et tout autre fichier du dossier\n"
     "   extrait dont le nom désigne 7a ; non ouverts ; aucun n'est nommé par ce que joue l'instance, recherche refaite par la\n"
     "   contre-lecture R-2614), dont les **fichiers dérivés de 7a** sous\n", 1),
    ("OB2-13", "ATT='<<ATT_C7_T07_V2>>';", f"ATT='{ATT}';", 1),
    ("OB2-14", "valeur au marqueur `ATT_C7_T07_V2` de la ligne (A)",
     "valeur de la ligne (A) (brouillon 2 : remplie, m-2 ; marqueur `ATT_C7_T07_V2` du brouillon 1)", 1),
    ("OB2-15", "**v2** : S7 ne porte **aucun changement sous `src/` ni `tests/`** depuis C7 : l'essai neuf du remplacement "
               "(`tests/test_remplacer_ligne_code_t07_v1.py`) entre dans `main` **après** S7 (sinon `git diff --quiet C7 S7 -- src tests` "
               "refuse, ici et à l'étape 2 du script)",
     f"**v2** : S7 ne porte **aucun changement sous `src/` ni `tests/`** depuis C7 : {REGLE_MA3}", 1),
    ("OB2-16", "marqueur `ATT_C7_T07_V2` ; mesurée", "**remplie** (brouillon 2, m-2 ; marqueur `ATT_C7_T07_V2` du brouillon 1) ; mesurée", 1),
    ("OB2-17", "  - **Valeur proposée pour `ATT_C7_T07_V2`** :", "  - **Valeur de `ATT`** (proposée au brouillon 1, remplie au brouillon 2, m-2) :", 1),
    ("OB2-18", "même texte que `<<NOUVELLE_LIGNE_CODE_T07>>` de l'addendum et que la trace du script) |\n",
     "même texte que le marqueur `NOUVELLE_LIGNE_CODE_T07` de l'addendum et que la trace du script) |\n"
     "| `ADDENDUM_T07_SCELLE_V2` (**neuf au brouillon 2**) | § 0 septies | chemin et empreinte de l'addendum de T0.7 **scellé** "
     "(brouillon 3 avec la nouvelle ligne `CODE-T07` recopiée, rien d'autre) ; suite des gestes, étapes 2 et 3 |\n", 1),
    ("OB2-19", "extrait aussi `docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/` (quatre fichiers dérivés de 7a)",
     "extrait aussi les fichiers de `docs/notes/g0-deux-semaines-v1/e3-ter-v1/` (dérivés de 7a, dont `lecture-7a-v1/` ; brouillon 2, m-1)", 1),
    ("OB2-20", "relevée ; destruction, inventaire final ; écarts.",
     "relevée ; destruction, inventaire final ; écarts ; **v2** : la réserve S-18 (fichiers de `e3-ter-v1/` posés sur le disque de\n"
     "l'instance, jamais ouverts) recopiée au compte rendu (contre-lecture R-2614, § 5).", 1),
]
# OB2-18 bis (dans la même case) : S7 ne porte pas l'ordre rempli, qui le nomme
COUPLES.insert(18, ("OB2-18b", "qui porte les pièces versées (addendum et ordre v2 scellés, `CODE-T07-v3.json`, registre remplacé, trace) ; "
                               "l'essai neuf du remplacement entre dans `main` après lui (P9) |",
                    "qui porte les pièces versées (addendum scellé, registre remplacé, trace ; `CODE-T07-v3.json` déjà versé ; l'ordre rempli "
                    "vient **après**, il nomme S7) ; aucun fichier de `src/` ni de `tests/` entre C7 et lui (P9) |", 1))
MARQUEURS = ("<<ID_SESSION_FILLE_V2>>", "<<COMMIT_SCELLEMENT_T07_V2>>", "<<LIGNE_CODE_T07_V2>>", "<<ADDENDUM_T07_SCELLE_V2>>")


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
    return texte[i:texte.index("\n## ", i + len(titre))]


def main(argv: list[str]) -> int:
    racine = Path(argv[0]) if argv else Path(".")
    src = (racine / SOURCE).read_bytes()
    if sha(src) != SHA_SOURCE:
        echec(f"{SOURCE} {sha(src)[:12]}… ≠ {SHA_SOURCE[:12]}…")
    for p, s in PIECES.items():
        if sha((racine / p).read_bytes()) != s:
            echec(f"{p} : empreinte ≠ {s[:12]}…")
    b1 = src.decode("utf-8")
    b2 = appliquer(b1, COUPLES)
    if defaire(b2, COUPLES) != b1:
        echec("couples défaits ≠ brouillon 1")
    if not b2.startswith("# Ordre d'exécution — étape A de T0.7, variante B (instance A100 neuve, activations recalculées) — v2, brouillon 2\n"):
        echec("titre")
    for mot in ("Claude", "claude-opus", "Opus 5", "Fable 5", "Sonnet", "Haiku"):
        if mot in b2:
            echec(f"identifiant de modèle « {mot} » présent")
    trouves = re.findall(r"<<[A-Z0-9_]+>>", b2)
    if sorted(trouves) != sorted(MARQUEURS):
        echec(f"marqueurs : {sorted(trouves)}")
    ligne_a = [l for l in b2.split("\n") if l.startswith("W=/home/user/etape-a-t07-b-")]
    if len(ligne_a) != 1 or f"ATT='{ATT}';" not in ligne_a[0]:
        echec("ligne (A) : ATT non remplie")
    if "quatre fichiers dérivés de 7a" in b2:
        echec("« quatre fichiers dérivés de 7a » resté (m-1)")
    if section(b2, "## 6. Devis de la variante B") != section(b1, "## 6. Devis de la variante B"):
        echec("§ 6 changé")
    factices = {"<<COMMIT_SCELLEMENT_T07_V2>>": "0" * 40, "<<LIGNE_CODE_T07_V2>>": "x", "<<ID_SESSION_FILLE_V2>>": "s",
                "<<ADDENDUM_T07_SCELLE_V2>>": "a"}
    blocs = re.findall(r"```bash\n(.*?)```", b2, flags=re.S)
    for k, b in enumerate(blocs):
        for m, f in factices.items():
            b = b.replace(m, f)
        with tempfile.NamedTemporaryFile("w", suffix=".sh", delete=False, encoding="utf-8") as t:
            t.write(b)
        r = subprocess.run(["bash", "-n", t.name], capture_output=True, text=True)
        Path(t.name).unlink()
        if r.returncode != 0:
            echec(f"bloc bash {k} : {r.stderr.strip()[:300]}")
    cible = racine / CIBLE
    if cible.exists():
        echec(f"{CIBLE} existe déjà (R12)")
    cible.write_bytes(b2.encode("utf-8"))
    print(f"TOUT PASSE : {CIBLE} écrit ({sha(b2.encode('utf-8'))}) ; {len(COUPLES)} couples ; {len(blocs)} blocs bash")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
