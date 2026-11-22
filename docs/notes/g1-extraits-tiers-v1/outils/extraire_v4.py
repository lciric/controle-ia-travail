"""Fabrique un extrait propre d'une pièce, par programme (tiers d'extraction de G1, v4).

Classe C (outil de travail). Auteur : le tiers d'extraction (session_013QMayjcfUDMKLzsbuNwNHm), 22 novembre 2026.

Différences avec la v3 (sur rapport d'un vérificateur neuf) : aucune empreinte de passage dans la fiche (l'empreinte
de la source entière, vérifiée, fixe déjà chaque passage par ses bornes ; une empreinte de passage court se devinerait) ;
passages qui se chevauchent refusés ; clés de la fiche en liste blanche ; un terme d'annexe absent des lignes gardées est
refusé (il trahirait un texte omis).

Différences de la v3 avec la v2 :
  - aucune marque ne qualifie le motif d'une omission : une ligne laissée de côté, pour l'objet de la demande ou par
    prudence de cloisonnement, est annoncée de la même façon, « [lignes a à b non reprises] » ; un passage omis dans une
    ligne gardée est remplacé par « [passage non repris] » ;
  - la fiche ne porte aucun texte omis : un passage est désigné par sa ligne et ses bornes (en caractères).

Deux commandes :
  preparer SPEC_EN_CLAIR FICHE   SPEC_EN_CLAIR (hors du dépôt) donne les passages en clair ({"ligne", "ancien"}) ;
                                 écrit FICHE (dans le dépôt) avec {"ligne", "debut", "fin"} seulement.
  fabriquer FICHE...             écrit l'extrait nommé par la fiche (refuse d'écraser, R12).

Fiche : {"source", "ref" (facultatif, lecture par `git show REF:source`), "empreinte_attendue" (préfixe d'au moins 8),
         "sortie", "titre", "objet", "plages": [[a, b], ...], "passages": [...],
         "annexe_sources": bool, "annexe_termes": [...]}
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

MARQUE = "[passage non repris]"
CLES = {"source", "ref", "empreinte_attendue", "sortie", "titre", "objet", "plages", "passages", "annexe_sources",
        "annexe_termes"}
DEPOT = Path(__file__).resolve().parents[4]


def h(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def lire_source(fiche: dict) -> bytes:
    if fiche.get("ref"):
        return subprocess.run(["git", "show", f"{fiche['ref']}:{fiche['source']}"],
                              check=True, capture_output=True, cwd=DEPOT).stdout
    return (DEPOT / fiche["source"]).read_bytes()


def lignes_de(brut: bytes) -> list[str]:
    lignes = brut.decode("utf-8").split("\n")
    if lignes[-1] == "":
        lignes = lignes[:-1]
    return lignes


def verifier_source(fiche: dict) -> tuple[list[str], str]:
    brut = lire_source(fiche)
    emp = hashlib.sha256(brut).hexdigest()
    attendu = fiche["empreinte_attendue"]
    if len(attendu) < 8 or not emp.startswith(attendu):
        raise SystemExit(f"ARRÊT : empreinte de la source {emp} ne commence pas par {attendu}")
    return lignes_de(brut), emp


def preparer(spec_clair: str, chemin_fiche: str) -> None:
    sc = Path(spec_clair).resolve()
    if DEPOT in sc.parents:
        raise SystemExit("ARRÊT : la spécification en clair doit rester hors du dépôt")
    spec = json.loads(sc.read_text(encoding="utf-8"))
    lignes, _ = verifier_source(spec)
    passages = []
    for p in spec.get("passages_en_clair", []):
        k, ancien = p["ligne"], p["ancien"]
        l = lignes[k - 1]
        if l.count(ancien) != 1:
            raise SystemExit(f"ARRÊT : passage introuvable ou multiple en ligne {k}")
        d = l.index(ancien)
        passages.append({"ligne": k, "debut": d, "fin": d + len(ancien)})
    inconnues = set(spec) - CLES - {"passages_en_clair"}
    if inconnues:
        raise SystemExit(f"ARRÊT : clés inconnues dans la spécification : {sorted(inconnues)}")
    fiche = {c: v for c, v in spec.items() if c in CLES}
    fiche["passages"] = passages
    sortie = Path(chemin_fiche)
    if sortie.exists():
        raise SystemExit(f"ARRÊT : {sortie} existe déjà (R12)")
    sortie.write_text(json.dumps(fiche, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"fiche écrite : {sortie}")


def fabriquer(fiche: dict, nom_fiche: str) -> str:
    lignes, emp = verifier_source(fiche)
    n = len(lignes)
    plages = sorted(tuple(p) for p in fiche["plages"])
    for i, (a, b) in enumerate(plages):
        if not (1 <= a <= b <= n):
            raise SystemExit(f"ARRÊT : plage {a}-{b} hors du fichier (1-{n})")
        if i and a <= plages[i - 1][1]:
            raise SystemExit(f"ARRÊT : plages chevauchantes {plages[i-1]} et {(a, b)}")
    dans_plage = {k for a, b in plages for k in range(a, b + 1)}
    par_ligne: dict[int, list[tuple[int, int]]] = {}
    for p in fiche.get("passages", []):
        if set(p) != {"ligne", "debut", "fin"}:
            raise SystemExit(f"ARRÊT : passage mal formé {sorted(p)}")
        k, d, f = p["ligne"], p["debut"], p["fin"]
        if k not in dans_plage:
            raise SystemExit(f"ARRÊT : passage de la ligne {k} hors plage")
        if not (0 <= d < f <= len(lignes[k - 1])):
            raise SystemExit(f"ARRÊT : bornes {d}-{f} hors de la ligne {k}")
        par_ligne.setdefault(k, []).append((d, f))
    for k, bornes in par_ligne.items():
        bornes.sort()
        for (d1, f1), (d2, f2) in zip(bornes, bornes[1:]):
            if d2 < f1:
                raise SystemExit(f"ARRÊT : passages qui se chevauchent en ligne {k}")
    inconnues = set(fiche) - CLES
    if inconnues:
        raise SystemExit(f"ARRÊT : clés inconnues dans la fiche : {sorted(inconnues)}")
    corps: list[str] = []
    gardees: list[tuple[int, str]] = []
    precedent = 0
    for a, b in plages:
        if a > precedent + 1:
            corps.append(f"[lignes {precedent + 1} à {a - 1} non reprises]")
        corps.append(f"<!-- lignes {a} à {b} de la source -->")
        for k in range(a, b + 1):
            l = lignes[k - 1]
            for d, f in sorted(par_ligne.get(k, []), reverse=True):
                l = l[:d] + MARQUE + l[f:]
            corps.append(l)
            gardees.append((k, l))
        precedent = b
    if precedent < n:
        corps.append(f"[lignes {precedent + 1} à {n} non reprises]")
    if fiche.get("annexe_sources"):
        vus: list[str] = []
        motif = re.compile(r"`([^`]+)`|\b(N-0\d\d(?: v\d)?|GO-\d{4}-\d\d-\d\d-\d+|R-\d{3,4})\b")
        for _, l in gardees:
            for m in motif.finditer(l):
                s = m.group(1) or m.group(2)
                if s not in vus:
                    vus.append(s)
        corps += ["", "---", "", "## Annexe A (par programme) — sources citées dans les lignes gardées, dans l'ordre", ""]
        corps += [f"- `{s}`" for s in vus]
    if fiche.get("annexe_termes"):
        corps += ["", "## Annexe B (par programme) — lignes de la source (gardées) qui portent chaque terme", "",
                  "| terme | lignes de la source |", "|---|---|"]
        for terme in fiche["annexe_termes"]:
            ks = [str(k) for k, l in gardees if terme in l]
            if not ks:
                raise SystemExit(f"ARRÊT : terme d'annexe absent des lignes gardées : {terme!r}")
            corps.append(f"| {terme} | {', '.join(ks)} |")
    lignes_passages = sorted(par_ligne)
    entete = [
        f"# Extrait — {fiche['titre']}",
        "",
        "- **Fabriqué par programme** : `docs/notes/g1-extraits-tiers-v1/outils/extraire_v4.py`, fiche "
        f"`{nom_fiche}` (numéros de lignes et bornes seulement) ; tiers d'extraction "
        "(session_013QMayjcfUDMKLzsbuNwNHm). Classe C.",
        f"- **Source** : `{fiche['source']}`" + (f" (lue sur `{fiche['ref']}`)" if fiche.get("ref") else "")
        + f", empreinte `{emp}`, {n} lignes.",
        f"- **Objet** : {fiche['objet']}",
        "- **Lignes reprises** : " + ", ".join(f"{a}–{b}" for a, b in plages)
        + " ; recopiées à l'octet"
        + (f", sauf {sum(len(v) for v in par_ligne.values())} passage(s) remplacé(s) par « {MARQUE} »"
           f" (ligne(s) {', '.join(map(str, lignes_passages))})" if par_ligne else "")
        + ". Les lignes et passages non repris le sont pour l'objet de la demande ou par prudence ; le motif n'est pas"
        " donné ligne par ligne.",
        "- **Statut** : à transmettre seulement si le rapport d'un vérificateur neuf le déclare propre.",
        "",
        "---",
        "",
    ]
    return "\n".join(entete + corps) + "\n"


def main() -> None:
    if len(sys.argv) >= 2 and sys.argv[1] == "preparer":
        preparer(sys.argv[2], sys.argv[3])
        return
    if len(sys.argv) >= 2 and sys.argv[1] == "fabriquer":
        for chemin_fiche in sys.argv[2:]:
            fiche = json.loads(Path(chemin_fiche).read_text(encoding="utf-8"))
            sortie = DEPOT / fiche["sortie"]
            if sortie.exists():
                raise SystemExit(f"ARRÊT : {sortie} existe déjà ; nouvelle version = nouveau nom (R12)")
            texte = fabriquer(fiche, chemin_fiche)
            sortie.write_text(texte, encoding="utf-8")
            print(f"{fiche['sortie']}  {h(texte)}")
        return
    raise SystemExit("usage : extraire_v4.py preparer SPEC FICHE | fabriquer FICHE...")


if __name__ == "__main__":
    main()
