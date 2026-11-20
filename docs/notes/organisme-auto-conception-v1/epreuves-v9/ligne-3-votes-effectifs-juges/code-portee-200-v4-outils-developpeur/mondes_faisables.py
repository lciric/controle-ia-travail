"""Outil du développeur : liste, par formule seule (aucun tirage, aucune graine), les cellules faisables du monde de
puissance, par écart, avec la faisabilité de la loi 3, sur le banc v3 copié. Argument : chemin du banc."""
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("banc_v3_outil", sys.argv[1])
banc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(banc)

cfg = banc.CONFIGURATION_DECISIVE["puissance"]
cellules = banc.enumerer_cellules_puissance(cfg)
print("cellules", len(cellules))
compte = {}
for (comp, ec, loi, rho, rp) in cellules:
    d = banc.resoudre_dissymetrie(comp, ec, rho, rp)
    if d is None:
        continue
    a, b = 0.2 + d, 0.2 - d
    if loi == 3 and not (banc.loi_3_jouable(a, rho) and banc.loi_3_jouable(b, rho)):
        continue
    compte[ec] = compte.get(ec, 0) + 1
    if abs(ec - 0.10) < 1e-12:
        print(comp, loi, rho, rp, round(d, 6))
print("faisables par écart", compte, "total", sum(compte.values()))
