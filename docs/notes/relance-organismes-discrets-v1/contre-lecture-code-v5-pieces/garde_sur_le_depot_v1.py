"""Passe la garde statique sur src/ et scripts/ du dépôt, chemins interdits au contre-lecteur exclus AVANT tout parcours
(élagage des dossiers ; aucun fichier interdit n'est ouvert). N'imprime que des chemins et des comptes."""
import os, re, sys
from pathlib import Path
from controle_ia.organismes_discrets import cloisonnement_bras_a_v5 as cl
INTERDIT = re.compile(r"(^|/)(bases|sondes|t07[^/]*|bras_a_v2_habilite)(/|$)|mots_et_cout_|autres_moniteurs_v|t0?8|T0\.8|t0\.8|habilite", re.I)
fichiers = []
for racine in ("src", "scripts"):
    for dp, dns, fns in os.walk(racine):
        dns[:] = [x for x in dns if not INTERDIT.search(f"{dp}/{x}/") and x != "__pycache__"]
        for f in fns:
            p = f"{dp}/{f}"
            if not INTERDIT.search(p):
                fichiers.append(p)
print("fichiers passés à la garde :", len(fichiers))
v = cl.violations_du_cloisonnement(fichiers)
par = {}
for x in v:
    par.setdefault(x.split(",")[0].split(" :")[0], []).append(x.split(" : ", 1)[-1][:90])
print("violations :", len(v), "dans", len(par), "fichiers")
for k, l in sorted(par.items()):
    print(" ", k, len(l), "|", l[0])
