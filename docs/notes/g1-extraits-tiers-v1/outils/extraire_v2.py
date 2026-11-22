"""Fabrique un extrait propre d'une pièce, par programme (tiers d'extraction de G1, v2).

v2 = v1 + deux annexes facultatives, calculées sur le texte gardé APRÈS retraits :
  "annexe_sources": true   liste, dans l'ordre, des chaînes entre accents graves et des identifiants
                           (N-0xx, GO-…, R-…) présents dans les lignes gardées ;
  "annexe_termes": [...]   pour chaque terme, les numéros de lignes de la source (gardées) qui le portent.
  "non_reprises_demande": [[a, b], ...]  trous entre plages laissés à la demande du destinataire (annoncés tels).

Classe C (outil de travail). Auteur : le tiers d'extraction (session_013QMayjcfUDMKLzsbuNwNHm), 22 novembre 2026.

Entrée : une fiche JSON
  {
    "source": "chemin/dans/le/depot.md",
    "ref": "origin/main" (facultatif : lit la source par `git show REF:chemin` ; sinon sur disque),
    "empreinte_attendue": "préfixe hexadécimal de la source (au moins 8 caractères)",
    "sortie": "docs/notes/g1-extraits-tiers-v1/....md",
    "titre": "...", "objet": "...",
    "plages": [[a, b], ...],            lignes 1-indexées, bornes comprises, recopiées à l'octet
    "retraits_lignes": [[a, b], ...],   lignes entières remplacées par « [retiré : issue] » (dans une plage)
    "retraits_passages": [{"ligne": n, "ancien": "texte exact"}, ...]
                                        passage remplacé par « [retiré : issue] » ; doit figurer une seule fois dans la ligne
  }
Sortie : l'extrait (en-tête, puis les plages, chacune annoncée par ses numéros de lignes dans la source ;
les lignes hors plages sont annoncées « [lignes a à b non reprises] »). Le programme refuse : empreinte
de la source différente, plage hors du fichier ou chevauchante, retrait hors plage, passage introuvable
ou présent plusieurs fois. Aucun repli silencieux.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

MARQUE = "[retiré : issue]"


def lire_source(fiche: dict) -> bytes:
    if fiche.get("ref"):
        return subprocess.run(["git", "show", f"{fiche['ref']}:{fiche['source']}"],
                              check=True, capture_output=True).stdout
    return Path(fiche["source"]).read_bytes()


def fabriquer(fiche: dict) -> tuple[str, str]:
    brut = lire_source(fiche)
    emp = hashlib.sha256(brut).hexdigest()
    attendu = fiche["empreinte_attendue"]
    if len(attendu) < 8 or not emp.startswith(attendu):
        raise SystemExit(f"ARRÊT : empreinte de la source {emp} ne commence pas par {attendu}")
    texte = brut.decode("utf-8")
    lignes = texte.split("\n")
    fin_sans_saut = lignes[-1] != ""
    if not fin_sans_saut:
        lignes = lignes[:-1]
    n = len(lignes)
    plages = sorted(tuple(p) for p in fiche["plages"])
    for i, (a, b) in enumerate(plages):
        if not (1 <= a <= b <= n):
            raise SystemExit(f"ARRÊT : plage {a}-{b} hors du fichier (1-{n})")
        if i and a <= plages[i - 1][1]:
            raise SystemExit(f"ARRÊT : plages chevauchantes {plages[i-1]} et {(a, b)}")
    dans_plage = set()
    for a, b in plages:
        dans_plage.update(range(a, b + 1))
    retirees = set()
    for a, b in fiche.get("retraits_lignes", []):
        for k in range(a, b + 1):
            if k not in dans_plage:
                raise SystemExit(f"ARRÊT : retrait de ligne {k} hors plage")
            retirees.add(k)
    passages: dict[int, list[str]] = {}
    for r in fiche.get("retraits_passages", []):
        k, ancien = r["ligne"], r["ancien"]
        if k not in dans_plage or k in retirees:
            raise SystemExit(f"ARRÊT : passage de la ligne {k} hors plage ou ligne déjà retirée")
        if lignes[k - 1].count(ancien) != 1:
            raise SystemExit(f"ARRÊT : passage introuvable ou multiple en ligne {k} : {ancien[:60]!r}")
        passages.setdefault(k, []).append(ancien)
    corps = []
    gardees: list[tuple[int, str]] = []
    precedent = 0
    for a, b in plages:
        if a > precedent + 1:
            demande = [precedent + 1, a - 1] in fiche.get("non_reprises_demande", [])
            corps.append(f"[lignes {precedent + 1} à {a - 1} non reprises" + (", à la demande du destinataire]" if demande else "]"))
        corps.append(f"<!-- lignes {a} à {b} de la source -->")
        k = a
        while k <= b:
            if k in retirees:
                debut = k
                while k + 1 <= b and k + 1 in retirees:
                    k += 1
                corps.append(f"{MARQUE} (lignes {debut} à {k})" if k > debut else f"{MARQUE} (ligne {k})")
            else:
                l = lignes[k - 1]
                for ancien in passages.get(k, []):
                    l = l.replace(ancien, MARQUE, 1)
                corps.append(l)
                gardees.append((k, l))
            k += 1
        precedent = b
    if precedent < n:
        corps.append(f"[lignes {precedent + 1} à {n} non reprises]")
    if fiche.get("annexe_sources"):
        vus: list[str] = []
        motif = re.compile(r"`([^`]+)`|\b(N-0\d\d(?: v\d)?|GO-\d{4}-\d\d-\d\d-\d+|R-\d{3,4})\b")
        for k, l in gardees:
            for m in motif.finditer(l):
                s = m.group(1) or m.group(2)
                if s not in vus:
                    vus.append(s)
        corps += ["", "---", "", "## Annexe A (par programme) — sources citées dans les lignes gardées, dans l'ordre", ""]
        corps += [f"- `{s}`" if "`" not in s else f"- {s}" for s in vus]
    if fiche.get("annexe_termes"):
        corps += ["", "## Annexe B (par programme) — lignes de la source (gardées) qui portent chaque terme", "",
                  "| terme | lignes de la source |", "|---|---|"]
        for terme in fiche["annexe_termes"]:
            ks = [str(k) for k, l in gardees if terme in l]
            corps.append(f"| {terme} | {', '.join(ks) if ks else 'aucune'} |")
    nb_passages = sum(len(v) for v in passages.values())
    lignes_retirees = sorted(retirees)
    entete = [
        f"# Extrait propre — {fiche['titre']}",
        "",
        "- **Fabriqué par programme** : `docs/notes/g1-extraits-tiers-v1/outils/extraire_v2.py`, fiche "
        f"`{fiche['_fiche']}` ; tiers d'extraction (session_013QMayjcfUDMKLzsbuNwNHm). Classe C.",
        f"- **Source** : `{fiche['source']}`" + (f" (lue sur `{fiche['ref']}`)" if fiche.get("ref") else "")
        + f", empreinte `{emp}`, {n} lignes.",
        f"- **Objet** : {fiche['objet']}",
        "- **Plages recopiées à l'octet** : " + ", ".join(f"{a}–{b}" for a, b in plages) + ".",
        f"- **Retraits** : {len(lignes_retirees)} ligne(s) entière(s)"
        + (f" ({', '.join(map(str, lignes_retirees))})" if lignes_retirees else "")
        + f", {nb_passages} passage(s) dans des lignes gardées"
        + (f" (lignes {', '.join(str(k) for k in sorted(passages))})" if passages else "")
        + f" ; chacun marqué « {MARQUE} ».",
        "- **Statut** : propre seulement si le rapport du vérificateur neuf le déclare tel.",
        "",
        "---",
        "",
    ]
    return "\n".join(entete + corps) + "\n", emp


def main() -> None:
    for chemin_fiche in sys.argv[1:]:
        fiche = json.loads(Path(chemin_fiche).read_text(encoding="utf-8"))
        fiche["_fiche"] = chemin_fiche
        sortie = Path(fiche["sortie"])
        if sortie.exists():
            raise SystemExit(f"ARRÊT : {sortie} existe déjà ; nouvelle version = nouveau nom (R12)")
        texte, emp = fabriquer(fiche)
        sortie.parent.mkdir(parents=True, exist_ok=True)
        sortie.write_text(texte, encoding="utf-8")
        print(f"{sortie}  source {emp[:12]}…  {hashlib.sha256(texte.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
