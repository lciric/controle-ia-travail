"""Vérification par programme de la différence entre les versions 12 et 13 de la liste « qui a lu quoi » — v1.

Usage (depuis la racine du dépôt) :
    python3 -I docs/notes/qui-a-lu-quoi-v1/outils-v13/verifier-difference-v12-v13.py .

Le programme ne réécrit rien : il lit les deux versions et imprime son rapport, que le
rédacteur verse à côté de lui par l'outil d'écriture (sortie-verification-difference-v12-v13.txt).
Il contrôle que la différence ne contient que les changements énumérés dans la puce de
la version 13 :
  (1) le titre ; (2) la puce de la version 13 en tête ; (3) dans la puce de la version 12,
  « (ce fichier) » devenu « (version précédente) », et rien d'autre ; (4) les lignes neuves
  du tableau, numérotées à la suite de la ligne 261 et placées juste après elle ;
  (5) la réserve 24, précédée d'une ligne vide, juste après la réserve 23 ; (6) la ligne de
  fin de la version 13, en dernière ligne.
Deux contrôles indépendants : la différence calculée par `difflib` (lignes retirées et
ajoutées, comptées comme multiensembles) ; et la soustraction : la version 13 privée des
lignes ajoutées doit être exactement la version 12 privée des lignes retirées, dans l'ordre.
Il contrôle aussi la forme des lignes neuves (huit cellules, numéros suivis, aucun
identifiant technique de modèle, aucun marqueur restant), l'unicité de l'heure, et les
compagnons d'empreinte des deux versions.
Code de sortie : 0 si tout est conforme, 1 sinon.
"""
import collections
import difflib
import hashlib
import re
import sys
from pathlib import Path

EMPREINTE_V12 = "accfabe38a1e71fea36da38749c6be5f77b83c66e757a243c7ce7a042c8e1eca"
PREMIERE_LIGNE_NEUVE = 262


def empreinte(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def compagnon_conforme(chemin: Path, octets: bytes) -> str:
    c = Path(str(chemin) + ".sha256")
    if not c.exists():
        return "compagnon absent"
    texte = c.read_text(encoding="utf-8").strip()
    attendu = f"{empreinte(octets)}  {chemin.name}"
    return "compagnon conforme" if texte == attendu else f"compagnon NON conforme : {texte!r}"


def main(argv: list[str]) -> int:
    racine = Path(argv[0]) if argv else Path(".")
    p12 = racine / "registres" / "qui-a-lu-quoi-v12.md"
    p13 = racine / "registres" / "qui-a-lu-quoi-v13.md"
    o12, o13 = p12.read_bytes(), p13.read_bytes()
    a = o12.decode("utf-8").splitlines(keepends=True)
    b = o13.decode("utf-8").splitlines(keepends=True)
    fautes: list[str] = []
    rapport: list[str] = []

    def controle(condition: bool, libelle: str) -> None:
        rapport.append(("OK      " if condition else "ÉCHEC   ") + libelle)
        if not condition:
            fautes.append(libelle)

    rapport.append(f"version 12 : {p12} ; {len(a)} lignes ; sha256 {empreinte(o12)} ; {compagnon_conforme(p12, o12)}")
    rapport.append(f"version 13 : {p13} ; {len(b)} lignes ; sha256 {empreinte(o13)} ; {compagnon_conforme(p13, o13)}")
    controle(empreinte(o12) == EMPREINTE_V12, "empreinte de la version 12 égale à celle de R-3552")
    controle(o13.endswith(b"\n") and not o13.endswith(b"\n\n"), "la version 13 finit par un seul saut de ligne")

    # --- 1. difflib : lignes retirées et ajoutées --------------------------------------
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    retirees, ajoutees = [], []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ("replace", "delete"):
            retirees.extend(range(i1, i2))
        if op in ("replace", "insert"):
            ajoutees.extend(range(j1, j2))
    rapport.append(f"difflib : {len(retirees)} lignes retirées de la version 12, {len(ajoutees)} lignes ajoutées dans la version 13")
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            rapport.append(f"  {op:7s} v12 lignes {i1 + 1}-{i2} → v13 lignes {j1 + 1}-{j2}")

    # --- 2. les changements attendus, repérés dans la version 13 -----------------------
    titre13 = "# Liste « qui a lu quoi » du programme — version 13\n"
    controle(b[0] == titre13 and a[0] == titre13.replace("version 13", "version 12"), "(1) titre : « version 12 » devenu « version 13 »")
    controle(b[2].startswith("- **Version 13** (ce fichier) :"), "(2) puce de la version 13 en ligne 3")
    attendu_puce12 = a[2].replace("- **Version 12** (ce fichier) :", "- **Version 12** (version précédente) :", 1)
    controle(b[3] == attendu_puce12 and b[3] != a[2], "(3) puce de la version 12 : seul « (ce fichier) » devenu « (version précédente) »")
    i261 = next(i for i, l in enumerate(b) if l.startswith("| 261 | "))
    neuves = []
    k = i261 + 1
    while k < len(b) and re.match(r"\| (\d+) \| ", b[k]):
        neuves.append(k)
        k += 1
    numeros = [int(re.match(r"\| (\d+) \| ", b[k]).group(1)) for k in neuves]
    controle(numeros == list(range(PREMIERE_LIGNE_NEUVE, PREMIERE_LIGNE_NEUVE + len(neuves))) and len(neuves) > 0,
             f"(4) lignes neuves du tableau numérotées à la suite de la ligne 261 et placées juste après elle : {numeros[0] if numeros else '-'} à {numeros[-1] if numeros else '-'} ({len(neuves)} lignes)")
    controle(b[k] == "\n" and b[k + 1] == "## Réserves\n", "(4) le tableau finit par la ligne vide et le titre « Réserves » de la version 12")
    i23 = next(i for i, l in enumerate(b) if l.startswith("23. **Version 11"))
    controle(b[i23 + 1] == "\n" and b[i23 + 2].startswith("24. **Version 13") and b[i23 + 3] == "\n",
             "(5) réserve 24, précédée d'une ligne vide, juste après la réserve 23")
    controle(b[-1].startswith("Version 13 : ") and b[-2].startswith("Version 11 : "), "(6) ligne de fin de la version 13 en dernière ligne, après celle de la version 11")

    attendu_ajoutees = {0, 2, 3, *neuves, i23 + 1, i23 + 2, len(b) - 1}
    attendu_retirees = {0, 2}

    # --- 3. multiensembles : difflib contre les changements attendus -------------------
    controle(collections.Counter(a[i] for i in retirees) == collections.Counter(a[i] for i in attendu_retirees),
             "difflib : les lignes retirées sont exactement le titre et la puce de la version 12")
    controle(collections.Counter(b[j] for j in ajoutees) == collections.Counter(b[j] for j in attendu_ajoutees),
             f"difflib : les lignes ajoutées sont exactement les {len(attendu_ajoutees)} lignes des changements (1) à (6)")

    # --- 4. soustraction : tout le reste est recopié à l'octet, dans l'ordre -----------
    reste12 = [l for i, l in enumerate(a) if i not in attendu_retirees]
    reste13 = [l for j, l in enumerate(b) if j not in attendu_ajoutees]
    controle(reste12 == reste13, f"soustraction : les {len(reste13)} autres lignes de la version 13 sont celles de la version 12, à l'octet et dans l'ordre")
    controle(len(b) == len(a) - len(attendu_retirees) + len(attendu_ajoutees), "comptes : lignes de la version 13 = 411 − 2 + lignes ajoutées")

    # --- 5. forme des lignes neuves ------------------------------------------------------
    textes_neufs = [b[2], b[i23 + 2]] + [b[k] for k in neuves]
    controle(all(b[k].count("|") == 9 and b[k].rstrip("\n").endswith(" |") for k in neuves), "lignes neuves : huit cellules chacune (neuf barres), aucune barre dans une cellule")
    controle(all(all(c.strip() for c in b[k].rstrip("\n").split("|")[1:-1]) for k in neuves), "lignes neuves : aucune cellule vide")
    controle(not any(re.search(r"claude-(opus|fable|sonnet|haiku)", t) for t in textes_neufs), "texte neuf : aucun identifiant technique de modèle")
    controle(not any("<<" in t or ">>" in t for t in textes_neufs + [b[-1]]), "texte neuf : aucun marqueur restant")
    heures = re.findall(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", b[-1])
    heure = heures[0] if heures else None
    controle(heure is not None and b[2].count(heure) >= 1 and b[neuves[-1]].count(heure) >= 1,
             f"heure unique {heure} : la même dans la puce, la ligne {numeros[-1] if numeros else '-'} et la ligne de fin")
    enumeres = all(f"({n})" in b[2] for n in range(1, 7))
    controle(enumeres, "la puce de la version 13 énumère les changements (1) à (6)")

    rapport.append("")
    rapport.append("VERDICT : CONFORME" if not fautes else f"VERDICT : NON CONFORME ({len(fautes)} échec(s))")
    print("\n".join(rapport))
    return 0 if not fautes else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
