"""Addendum à T0.7 (contrôle du cache du modèle de P3, option (a)), brouillon 3 : le brouillon 2 (`53ba8ea7…`, versé, gardé tel quel,
R12) plus les couples AD3-01 à AD3-15 — corrections de la contre-lecture des pièces de relance (R-2614,
`relance-v2-preparation-v1/contre-lecture-relance-v2-v1.md`, `703195e5…`) : MA-1 (essais de l'outil versés hors de `src/` et
`tests/`), MA-2 (renvoi à la suite unique des gestes de la mère), MA-3 (aucun fichier de `src/` ni de `tests/` entre C7 et S7),
m-1 (les fichiers de `e3-ter-v1/`), m-4 (mutations comptées comme le lecteur), m-6 (outil v2 : trace avant le remplacement) — v1.

Préparateur (modèle A), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-13. Bibliothèque standard et
`git show` seulement ; aucun réseau, aucune clé. **Se rejoue sur `main`** : il ne lit que des fichiers suivis (ou versés par ce lot).

    <python du dépôt> -I -B <ce script> RACINE

Vérifie les empreintes de la source et des pièces citées ; applique les couples (chaque « ancien » présent le nombre de fois
déclaré, chaque « nouveau » absent avant) ; exige que les couples défaits redonnent le brouillon 2 à l'octet ; vérifie : aucun
identifiant de modèle, marqueur `<<NOUVELLE_LIGNE_CODE_T07>>` une fois, aucun renvoi resté à `tests/test_remplacer_…` comme
pièce présente ; écrit la cible (refus si elle existe, R12). Code 0 et « TOUT PASSE », sinon code 1.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

SOURCE = "brouillons/T0.7-addendum-cache-motifs-v1-brouillon2.md"
SHA_SOURCE = "53ba8ea7365d808c3a409b2b08b312e9477e5d6971e9380f86c8d144e622e6fb"
CIBLE = "brouillons/T0.7-addendum-cache-motifs-v1-brouillon3.md"
P = "docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1"
E = f"{P}/relance-v2-preparation-v1"
GESTES = f"{E}/gestes-mere-relance-v2-v1.md"
ESSAIS_V1 = f"{E}/essais-outil/test_remplacer_ligne_code_t07_v1.py"
ESSAIS_V2 = f"{E}/essais-outil/test_remplacer_ligne_code_t07_v2.py"
PIECES = {
    f"{E}/contre-lecture-relance-v2-v1.md": "703195e515480fcff2f4dc60cd4ca5bffedc4e930e24f6d4711eaa57386fc5fd",
    "scripts/remplacer_ligne_code_t07_v1.py": "a89e2226839a4492d6300659fdd560d150c96998a7249932efb768b183d5925c",
    "scripts/remplacer_ligne_code_t07_v2.py": "0e7c3c0cbf4b052b1a2852ef49fb2135337dc110c0af7dbf4f066509207204bb",
    ESSAIS_V1: "0a1210da9060eee2715eebe556261ea96193ce2b002d071cb192484ff5ebfb7f",
    ESSAIS_V2: "74b11b9523204003930a51f34e5c51f08adc491a998b37e4805ab250d6271a1c",
}
OUTIL2 = PIECES["scripts/remplacer_ligne_code_t07_v2.py"]

S0BIS = f"""## 0 bis. Ce qui change depuis le brouillon 2 (contre-lecture R-2614, « après corrections »)

| Couple | Où | Changement | Constat |
|---|---|---|---|
| AD3-01 à AD3-04 | titre, en-tête | brouillon 3 ; auteur et date ; contre-lecture du brouillon 2 rendue ; statut | R-2614 |
| AD3-05 | § 0 bis | ce tableau | — |
| AD3-06 | § 3.5 | `ATT` remplie dans l'ordre v2 (brouillon 2) | m-2 |
| AD3-07 | § 5 | nouvelle ligne : renvoi à la suite unique des gestes de la mère (`{GESTES}`) | MA-2 |
| AD3-08 | § 5 | outil **v2** (`scripts/remplacer_ligne_code_t07_v2.py`) : trace écrite et scellée avant le remplacement | m-6 |
| AD3-09 | § 5 | essais de l'outil **versés hors de `src/` et `tests/`** (`{E}/essais-outil/`), essais v2 | MA-1 |
| AD3-10 | § 5 | mutations comptées aussi comme le lecteur | m-4 |
| AD3-11 | § 5 | **aucun fichier de `src/` ni de `tests/`**, de quelque tâche que ce soit, n'entre dans `main` entre C7 et S7 | MA-3 |
| AD3-12 à AD3-14 | § 0, § 5 bis, réserve 7 | « les fichiers de `e3-ter-v1/` », sans compte | m-1 |
| AD3-15 | § 7 | pièces : essais versés (chemins corrigés), outil v2, contre-lecture, suite des gestes | MA-1, MA-2 |

Les autres constats (m-3 : jeton à chevrons de l'ordre ; m-5 : compagnons des scripts ; m-7 : libellés de l'ordre) ne touchent
pas l'addendum. **Aucun fichier sous `src/` ni sous `tests/` n'est écrit par ce lot.**

"""

COUPLES = [
    ("AD3-01", "(option (a), R-2593) — v1, brouillon 2\n", "(option (a), R-2593) — v1, brouillon 3\n", 1),
    ("AD3-02", "  par le script : couples défaits → brouillon 1). Ce qui change : § 0.\n",
     "  par le script : couples défaits → brouillon 1). Ce qui change : § 0.\n"
     "- **Brouillon 3** : même préparateur (modèle A), sur le message de la mère qui suit R-2614 ; 2026-11-13, de 23:35 à 23:55\n"
     "  UTC (`date -u`). **Brouillon 3 = brouillon 2** (`53ba8ea7…`, versé, gardé tel quel, R12) **+ les couples AD3-01 à AD3-15** du\n"
     "  script `brouillons/T0.7-addendum-cache-motifs-v1-brouillon3-appliquer-v1.py` (il se rejoue sur `main`) ; tout le reste égal à\n"
     "  l'octet au brouillon 2 (couples défaits → brouillon 2). Ce qui change : § 0 bis. Le script du brouillon 2 lit\n"
     "  `tests/test_remplacer_ligne_code_t07_v1.py`, absent de `main` (MA-1) : il ne se rejoue qu'avec ce fichier copié depuis\n"
     f"  `{ESSAIS_V1}` (mêmes octets) ; ce brouillon 3 le cite à son chemin versé.\n", 1),
    ("AD3-03", "  l'ordre d'exécution version 2, brouillon 1.\n",
     "  l'ordre d'exécution version 2, brouillon 1. **Brouillon 2 contre-lu** (R-2614) : `" + E + "/contre-lecture-relance-v2-v1.md`\n"
     "  (`703195e5…`, lecteur neuf, modèle B) : « après corrections », 0 bloquant ; MA-1 à MA-3 et m-1 à m-7 traités ici et dans\n"
     "  l'ordre v2 (brouillon 2) ; **les ajouts du brouillon 3 (couples AD3) ne sont pas contre-lus**.\n", 1),
    ("AD3-04", "- **Statut** : brouillon 2, **non scellé**", "- **Statut** : brouillon 3, **non scellé**", 1),
    ("AD3-05", "## 1. Écart déclaré\n", S0BIS + "## 1. Écart déclaré\n", 1),
    ("AD3-06", "`ATT` au marqueur `ATT_C7_T07_V2`\n(proposée : « 500 passed, 2 skipped, 4 xfailed », § 3.4)",
     "`ATT` = « 500 passed, 2 skipped, 4 xfailed »\n(§ 3.4 ; marqueur `ATT_C7_T07_V2` rempli dans l'ordre v2, brouillon 2, m-2)", 1),
    ("AD3-07", "  la mère la recopie ici à l'octet, depuis la trace, avant le scellement de l'addendum.\n",
     "  la mère la recopie ici à l'octet, depuis la trace, avant le scellement de l'addendum. **Brouillon 3 (MA-2)** : remplacement,\n"
     f"  recopie et scellement se font dans l'ordre de la suite unique des gestes de la mère, `{GESTES}` (étapes 1 à 3 ;\n"
     "  commandes exactes, trace sous `relance-v2-preparation-v1/trace-remplacement-ligne-code-t07-v1.md`) ; aucune ligne neuve au\n"
     "  registre des scellements pour l'addendum (la garde de T0.7 refuse toute clé inconnue, règle (4)).\n", 1),
    ("AD3-08", "  `date -u`, empreintes du registre avant et après, empreinte de l'outil).\n",
     "  `date -u`, empreintes du registre avant et après, empreinte de l'outil). **Brouillon 3 (m-6)** : l'outil à employer est la\n"
     f"  **v2**, `scripts/remplacer_ligne_code_t07_v2.py` (`{OUTIL2}`), égale à la v1 (qui reste telle quelle) sauf l'ordre des\n"
     "  écritures : la copie du registre est écrite dans un fichier temporaire, **la trace est écrite et scellée avant le\n"
     "  remplacement** ; trace impossible → refus, rien remplacé ; remplacement impossible → trace retirée, registre inchangé ;\n"
     "  relecture différente → refus « nœud », trace gardée.\n", 1),
    ("AD3-09", "- **Essais** : `tests/test_remplacer_ligne_code_t07_v1.py` (`0a1210da9060eee2715eebe556261ea96193ce2b002d071cb192484ff5ebfb7f`), 28 cas, tous sur",
     f"- **Essais** (brouillon 3, MA-1 : **versés hors de `src/` et `tests/`**, sous `{E}/essais-outil/`, avec compagnons ; à copier\n"
     "  sous `tests/` seulement après la fin de l'étape A, s'ils doivent y aller) : v2 de l'outil,\n"
     f"  `{ESSAIS_V2}` (`{PIECES[ESSAIS_V2]}`), 36 cas (les 28 de la v1 visant\n"
     "  l'outil v2, plus trace écrite avant le remplacement, trace impossible de trois façons, remplacement impossible, relecture\n"
     "  différente, fichier temporaire déjà présent, nouvelle ligne de longueur différente), se joue où il est ; v1 de l'outil,\n"
     f"  `{ESSAIS_V1}` (`0a1210da9060eee2715eebe556261ea96193ce2b002d071cb192484ff5ebfb7f`, mêmes octets que le fichier\n"
     "  d'abord placé sous `tests/`), 28 cas, qui ne se joue que copié sous `tests/` (chemins relatifs à `tests/`) ; tous sur", 1),
    ("AD3-10", "Quatorze mutations de l'outil sur quinze attrapées (la survivante\n  retire un contrôle interne redondant).",
     "Quatorze mutations de l'outil sur quinze attrapées (la survivante\n  retire un contrôle interne redondant). **Brouillon 3 (m-4)** : "
     "compte du lecteur (R-2614), outil v1 : vingt sur vingt-six ;\n  survivent le contrôle interne des octets, celui de la copie, la "
     "relecture après écriture, « nouvelle égale à l'ancienne »,\n  « fichier temporaire présent » et le calcul de la fin de ligne à "
     "longueurs égales ; outil v2, vingt-neuf mutations (les\n  vingt-six du lecteur et trois sur l'ordre des écritures) : vingt-six "
     "attrapées ; survivent le contrôle interne des\n  octets, celui de la copie (tous deux redondants avec la construction par "
     "tranche) et « nouvelle égale à l'ancienne »\n  (inatteignable : « même chemin » refuse avant). Aucune survivante ne laisse "
     "écrire à tort.", 1),
    ("AD3-11", "- **Essai neuf et S7** : l'essai neuf est sous `tests/` ; il entre dans `main` **après** S7 (ordre v2, P9), sinon\n"
               "  `git diff --quiet C7 S7 -- src tests` refuse à l'étape 2 du script.\n",
     "- **Essai neuf et S7** : l'essai neuf est sous `tests/` ; il entre dans `main` **après** S7 (ordre v2, P9), sinon\n"
     "  `git diff --quiet C7 S7 -- src tests` refuse à l'étape 2 du script. **Brouillon 3 (MA-3)** : la règle vaut pour **tout\n"
     "  fichier de `src/` ou de `tests/`, de quelque tâche que ce soit** : aucun n'entre dans `main` entre C7 et S7 ; les essais de\n"
     "  l'outil restent sous `relance-v2-preparation-v1/essais-outil/` jusqu'à la fin de l'étape A (instance détruite), pour qu'un\n"
     "  S7 refait reste possible.\n", 1),
    ("AD3-12", "| AD2-17 | § 5 bis | **m-3** : quatre fichiers dérivés de 7a posés sur l'instance : point ouvert devenu réserve |",
     "| AD2-17 | § 5 bis | **m-3** : fichiers dérivés de 7a posés sur l'instance (brouillon 3 : les fichiers de `e3-ter-v1/`) : point ouvert devenu réserve |", 1),
    ("AD3-13", "  le dossier, donc aussi `docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/` : quatre fichiers suivis (noms seuls, lus par",
     "  le dossier, donc aussi **les fichiers suivis de `docs/notes/g0-deux-semaines-v1/e3-ter-v1/`** (brouillon 3, m-1 : tout le\n"
     "  dossier, dont des fichiers nommés `audit-ecart-dt4-7a…`, et tout autre fichier du dossier extrait dont le nom désigne 7a,\n"
     "  non ouverts ; aucun n'est nommé par `src/`, `tests/test_t07_*.py`, `tests/conftest.py`, le script v4, la configuration v8,\n"
     "  les exigences ni `.claude/`, recherche refaite) ; parmi eux, `docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/` : quatre fichiers suivis (noms seuls, lus par", 1),
    ("AD3-14", "7. **Quatre fichiers dérivés de 7a sur le disque de l'instance** (§ 5 bis) :",
     "7. **Les fichiers de `e3-ter-v1/` (dérivés de 7a) sur le disque de l'instance** (§ 5 bis ; brouillon 3, m-1) :", 1),
    ("AD3-15", f"| **brouillon 2** : essais de l'outil (28 cas) | `tests/test_remplacer_ligne_code_t07_v1.py` | `0a1210da9060eee2715eebe556261ea96193ce2b002d071cb192484ff5ebfb7f` |\n",
     f"| **brouillon 2** : essais de l'outil (28 cas) ; **brouillon 3 (MA-1)** : versés hors de `tests/` jusqu'à la fin de l'étape A, puis, s'il le faut, copiés sous `tests/test_remplacer_ligne_code_t07_v1.py` | `{ESSAIS_V1}` | `0a1210da9060eee2715eebe556261ea96193ce2b002d071cb192484ff5ebfb7f` |\n"
     f"| **brouillon 3** : outil v2 (trace avant le remplacement, m-6) | `scripts/remplacer_ligne_code_t07_v2.py` | `{OUTIL2}` |\n"
     f"| **brouillon 3** : essais de l'outil v2 (36 cas, joués où ils sont) | `{ESSAIS_V2}` | `{PIECES[ESSAIS_V2]}` |\n"
     f"| **brouillon 3** : contre-lecture des pièces de relance (R-2614) | `{E}/contre-lecture-relance-v2-v1.md` | `{PIECES[f'{E}/contre-lecture-relance-v2-v1.md']}` |\n"
     f"| **brouillon 3** : suite unique des gestes de la mère (MA-2) | `{GESTES}` | son compagnon `.sha256` (elle cite ce brouillon) |\n", 1),
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
    src = (racine / SOURCE).read_bytes()
    if sha(src) != SHA_SOURCE:
        echec(f"{SOURCE} {sha(src)[:12]}… ≠ {SHA_SOURCE[:12]}…")
    for p, s in PIECES.items():
        if sha((racine / p).read_bytes()) != s:
            echec(f"{p} : empreinte ≠ {s[:12]}…")
        comp = Path(str(racine / p) + ".sha256")
        if not comp.is_file() or comp.read_text(encoding="utf-8").split()[0] != s:
            echec(f"{p} : compagnon .sha256 absent ou différent")
    b2 = src.decode("utf-8")
    b3 = appliquer(b2, COUPLES)
    if defaire(b3, COUPLES) != b2:
        echec("couples défaits ≠ brouillon 2")
    for mot in ("Claude", "claude-opus", "Opus 5", "Fable 5", "Sonnet", "Haiku"):
        if mot in b3:
            echec(f"identifiant de modèle « {mot} » présent")
    if b3.count("<<NOUVELLE_LIGNE_CODE_T07>>") != 1:
        echec("marqueur de la nouvelle ligne")
    for l in b3.split("\n"):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if l.startswith("| ") and len(c) >= 3 and c[2] == "`tests/test_remplacer_ligne_code_t07_v1.py`":
            echec("pièce encore citée à un chemin de tests/ absent de main")
    cible = racine / CIBLE
    if cible.exists():
        echec(f"{CIBLE} existe déjà (R12)")
    cible.write_bytes(b3.encode("utf-8"))
    print(f"TOUT PASSE : {CIBLE} écrit ({sha(b3.encode('utf-8'))}) ; {len(COUPLES)} couples")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
