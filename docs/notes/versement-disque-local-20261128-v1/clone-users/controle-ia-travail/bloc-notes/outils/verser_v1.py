"""Versement de pièces du bloc-notes dans le dépôt : copie, empreinte attendue vérifiée, compagnon écrit (R6, R12).

Usage (depuis la racine du dépôt, PYTHONPATH=src) : python -B verser_v1.py PLAN_JSON [--essai]
  PLAN_JSON : liste de {"source": chemin absolu, "destination": chemin relatif au dépôt, "sha256": 64 signes}.
  Arrête avant toute écriture si : une source manque ; une empreinte diffère de l'attendue ; une destination sort de
  docs/, prereg/ ou donnees/, ou porte « .. » ; deux pièces visent la même destination ; une destination existe déjà
  avec une autre empreinte (on n'écrase jamais, R12). Une destination déjà présente à la bonne empreinte est laissée.
  --essai : n'écrit rien ; imprime le plan vérifié.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path

from controle_ia.scellement import sceller, verifier

RACINES = ("docs/", "prereg/", "donnees/")


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def main(argv: list[str]) -> int:
    if len(argv) not in (2, 3) or (len(argv) == 3 and argv[2] != "--essai"):
        print(__doc__, file=sys.stderr)
        return 2
    essai = len(argv) == 3
    plan = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    vues, faire = set(), []
    for x in plan:
        src, dst, attendu = Path(x["source"]), x["destination"], x["sha256"]
        if not dst.startswith(RACINES) or ".." in Path(dst).parts or dst.endswith(".sha256"):
            raise SystemExit(f"destination refusée : {dst}")
        if dst in vues:
            raise SystemExit(f"destination en double : {dst}")
        vues.add(dst)
        if not src.is_file():
            raise SystemExit(f"source absente : {src}")
        e = sha(src)
        if e != attendu:
            raise SystemExit(f"empreinte de {src} : {e}, attendue {attendu}")
        d = Path(dst)
        if d.exists():
            if not d.is_file() or sha(d) != e:
                raise SystemExit(f"destination déjà présente, autre contenu : {dst} (R12)")
            faire.append((src, d, e, "présente"))
        else:
            faire.append((src, d, e, "à copier"))
    for src, d, e, etat in faire:
        print(f"{etat:9} {e[:12]}… {d}")
    if essai:
        print(f"essai : {len(faire)} pièces vérifiées, rien n'est écrit")
        return 0
    for src, d, e, etat in faire:
        if etat == "à copier":
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, d)
        if sceller(d) != e or verifier(d) != e:
            raise SystemExit(f"scellement de {d} : empreinte inattendue")
    print(f"versé : {len(faire)} pièces, compagnons écrits et relus")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
