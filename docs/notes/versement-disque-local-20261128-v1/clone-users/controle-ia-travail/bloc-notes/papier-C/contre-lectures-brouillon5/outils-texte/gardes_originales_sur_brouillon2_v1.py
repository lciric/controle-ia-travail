"""Rejoue, sur la configuration brouillon 2, la fonction `controle()` de `ecrire_config_v1.py` (634c3e8f…), recopiée
à l'identique dans sa logique (fentes non remplies, gardes générales, « aucun ordre » pour la famille 4, gardes des
témoins avec les trois listes, 16 formulations par famille, 16 témoins rangés par longueur), et compare les longueurs
calculées à `controle_redaction` du brouillon 2. Lecture seule.
Usage : python3 -I -B gardes_originales_sur_brouillon2_v1.py CONFIG_BROUILLON2
"""
import hashlib
import json
import re
import sys

brut = open(sys.argv[1], "rb").read()
print("sha256 entrée :", hashlib.sha256(brut).hexdigest())
cfg = json.loads(brut)
vivier, fentes, gardes, temoins = cfg["vivier"], cfg["fentes"], cfg["gardes_lexicales"], cfg["temoins_sham"]
echecs = []


def remplir(t, f):
    for k, v in f.items():
        t = t.replace("{" + k + "}", v)
    if re.search(r"\{[A-Z_]+\}", t):
        echecs.append(("fente non remplie", t[:60]))
    return t


rapport = {"longueurs_A": {}, "longueurs_B": {}, "longueurs_temoins": [len(t) for t in temoins]}
for corpus in ("A", "B"):
    for fam, lst in vivier.items():
        if len(lst) != 16:
            echecs.append((fam, "nombre", len(lst)))
        ls = []
        for i, t in enumerate(lst, 1):
            r = remplir(t, fentes[corpus])
            for p in gardes["toutes_insertions_et_temoins"]:
                if re.search(p, r, re.I):
                    echecs.append(("générale", corpus, fam, i, p))
            if fam == "usurpation_stylistique":
                for p in gardes["usurpation_stylistique_aucun_ordre"]:
                    if re.search(p, r, re.I):
                        echecs.append(("aucun ordre", corpus, fam, i, p))
            ls.append(len(r))
        rapport[f"longueurs_{corpus}"][fam] = ls
if len(temoins) != 16:
    echecs.append(("témoins", len(temoins)))
for i, t in enumerate(temoins, 1):
    for p in gardes["toutes_insertions_et_temoins"] + gardes["usurpation_stylistique_aucun_ordre"] + \
            gardes["temoins_sans_pression"]:
        if re.search(p, t, re.I):
            echecs.append(("témoin", i, p))
if sorted(rapport["longueurs_temoins"]) != rapport["longueurs_temoins"]:
    echecs.append(("témoins non rangés",))
cr = cfg["controle_redaction"]
for k in ("longueurs_A", "longueurs_B", "longueurs_temoins"):
    print(k, "égales à controle_redaction :", rapport[k] == cr[k])
print("famille 4, longueurs A :", rapport["longueurs_A"]["usurpation_stylistique"])
print("famille 4, longueurs B :", rapport["longueurs_B"]["usurpation_stylistique"])
print("échecs :", echecs)
