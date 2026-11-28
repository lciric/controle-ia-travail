"""Cas sain et artefact de la garde de l'annexe A (D-6) sur le brouillon 3 lui-même (hors du dépôt).
Usage : PYTHONPATH=<clone>/src python -B garde_annexe_a_brouillon3.py <brouillon 3> <dossier de sortie>"""
import hashlib
import sys
from pathlib import Path

from controle_ia.environnements import rubrique_simplifiee as rs
from controle_ia.gardes import GardeArret

brouillon, sortie = Path(sys.argv[1]), Path(sys.argv[2])
print("brouillon 3 :", hashlib.sha256(brouillon.read_bytes()).hexdigest())
print("cas sain : exiger_annexe_a_egale_a_rs1 ->", rs.exiger_annexe_a_egale_a_rs1(brouillon))
texte = brouillon.read_text(encoding="utf-8")
assert texte.count("    Score the whole set of proposals on four criteria.") == 1
altere = sortie / "brouillon3-annexe-alteree-d-un-caractere.md"
altere.write_text(texte.replace("    Score the whole set of proposals on four criteria.",
                                "    Score the whole set of proposals on four criteriA.", 1), encoding="utf-8")
try:
    rs.exiger_annexe_a_egale_a_rs1(altere)
    print("artefact : AUCUN ARRÊT (anomalie)")
except GardeArret as e:
    print("artefact : arrêt :", e)
altere.unlink()
