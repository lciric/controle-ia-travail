"""Vérifie les empreintes que le candidat 12 r2 après couples cite dans les paragraphes des chaînes v10, v11 et v12 (ceux qui
portent « à recalculer au commit cité, tout écart : nœud »), dont les quatre valeurs que le couple W11 introduit, contre les
SEULS fichiers de la chaîne v12 : empreinte de `git show 7822a65b:<chemin>` (R-1781, conduite en attendant le mot de Lazar).
Aucune recherche dans l'historique : aucun parcours de commits, aucun `git log`, aucun `git rev-list` ; deux arbres seulement,
7822a65b (référence) et 8cb539f9 (pour information : le fichier a-t-il changé entre les deux têtes ?).
Un nom de module sans dossier (« `session_v10.py` ») est résolu par son nom de base, s'il est unique sous `src/` à 7822a65b ;
« brouillon 5 » est la configuration `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon5.json` (l. 3 du candidat).

Usage : python -I -B verifier_empreintes_chaines_candidat_v1.py DEPOT CANDIDAT_APRES_COUPLES
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

DEPOT, CAND = sys.argv[1], Path(sys.argv[2])
REF, INFO = "7822a65b6afb1595ce467ffeb55c8a7f736b20dc", "8cb539f9b7ecd20fab133bfffb590ca8e1fdfc63"
BROUILLON5 = "docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon5.json"
W11 = ["scripts/lancer_t06_v11.sh", "scripts/amorce_instance_t06_v9.sh", "scripts/tests-cibles-t06-v1.txt",
       "scripts/tests-exclus-t06-v1.txt"]
M4 = {"tests/test_t06_cibles_invisibles_v1.py": "0eada746", "brouillons/ordres-t06-e2-e3-v5/ordre-fille-6-t06-e3-v5.md": "f00e143d"}
H = r"[0-9a-f]{64}"
CITE = re.compile(r"(?:`(?!" + H + r"`)(?P<c>[^`\s]+)`|(?P<b>brouillon 5))\**,?\s*\(?`(?P<h>" + H + r")`")
VALENT = re.compile(r"elles valent `(" + H + r")`, `(" + H + r")`, `(" + H + r")` et `(" + H + r")`")


def git(*a: str) -> bytes:
    return subprocess.run(["git", "-C", DEPOT, *a], capture_output=True, check=True).stdout


def empreinte(commit: str, chemin: str) -> str:
    r = subprocess.run(["git", "-C", DEPOT, "show", f"{commit}:{chemin}"], capture_output=True)
    return hashlib.sha256(r.stdout).hexdigest() if r.returncode == 0 else "absent"


SRC = git("ls-tree", "-r", "--name-only", REF, "--", "src").decode().split()


def resoudre(cite: str | None, b: str | None) -> str:
    if b:
        return BROUILLON5
    if "/" in cite:
        return cite
    cands = [p for p in SRC if p.rsplit("/", 1)[-1] == cite]
    return cands[0] if len(cands) == 1 else f"NON RÉSOLU ({len(cands)} candidats)"


texte = CAND.read_text(encoding="utf-8")
print(f"# candidat : {CAND.name} sha256 {hashlib.sha256(CAND.read_bytes()).hexdigest()}")
print(f"# référence : fichiers au commit {REF} (chaîne v12) ; information : {INFO[:8]}")
print("paragraphe\tchemin cité\tchemin lu\tempreinte citée\tempreinte à 7822a65b\tégale\tinchangé à 8cb539f9")
bilan = []
for v in ("v10", "v11", "v12"):
    par = [l for l in texte.splitlines() if l.lstrip().startswith(f"- **chaîne {v} de la course")]
    assert len(par) == 1, (v, len(par))
    p, vus, egales, rangs = par[0], set(), 0, []
    for m in CITE.finditer(p):
        chemin = resoudre(m["c"], m["b"])
        e = empreinte(REF, chemin)
        rangs.append((m["c"] or m["b"], chemin, m["h"], e))
        vus.add(m["h"])
    w = VALENT.search(p)
    if w:
        for chemin, h in zip(W11, w.groups()):
            rangs.append((f"(W11) {chemin}", chemin, h, empreinte(REF, chemin)))
            vus.add(h)
    for cite, chemin, h, e in rangs:
        egales += e == h
        print(f"{v}\t{cite}\t{chemin}\t{h}\t{e}\t{'oui' if e == h else 'NON'}\t{'oui' if empreinte(INFO, chemin) == e else 'NON'}")
    reste = sorted(set(re.findall(H, p)) - vus)
    bilan.append(f"# {v} : {len(rangs)} empreintes citées, {egales} égales, {len(rangs) - egales} différentes ; "
                 f"empreintes du paragraphe non rattachées à un chemin : {len(reste)} {reste}")
print("\n".join(bilan))
print("# m4 de la contre-lecture (hors couples, pour information) : empreinte au commit 7822a65b")
for chemin, ancien in M4.items():
    print(f"#   {chemin} : {empreinte(REF, chemin)} (empreinte historique citée : {ancien}… ; présente dans le candidat : "
          f"{len(re.findall(ancien + '[0-9a-f]{56}', texte))} fois)")
