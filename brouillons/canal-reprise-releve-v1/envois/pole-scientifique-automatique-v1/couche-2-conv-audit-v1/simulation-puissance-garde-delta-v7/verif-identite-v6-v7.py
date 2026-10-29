"""Identité de la v7 avec la v6 au niveau de `cellule(…)` (en plus du rejeu de deux commandes v6, comparé par `comparer-v6-v7.py`) :
1. sur des cellules d'essai couvrant tous les chemins de la v6 (dispersion nulle ; dispersion logit des comparateurs σ = 1, ρ = 0,17 ;
   lien coupé ; effet sur A ; effet bêta sur A ; fiches nulles ; K_s ≠ K_h par le constructeur ; lectures (A) et (B)), `cellule(…)`
   de la v7 (échelle logit, défaut) rend champ pour champ ce que rend la v6 (mêmes options, même graine) ;
2. témoin négatif (R5) : la même comparaison entre la v7 en échelle bêta et la v6 en logit, à la même étiquette, trouve des différences ;
3. K_s ≠ K_h : la v7 (`--K-s`) et la v6 (`--K-sabotes`, apparié) nomment la même loi et tirent la même cellule.

Usage : python3 -I -B verif-identite-v6-v7.py SCRIPT_V7 SCRIPT_V6 SORTIE.json   (-B : aucun __pycache__)
"""

import hashlib
import importlib.util
import json
import sys

V7, V6, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]
if not sys.flags.dont_write_bytecode:
    raise SystemExit("refus : lancer avec -B (aucun __pycache__ dans les dossiers lus)")


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


v7, v6 = charger("sim_v7", V7), charger("sim_v6", V6)
empreinte = lambda c: hashlib.sha256(open(c, "rb").read()).hexdigest()
bilan = {"script_v7": V7, "script_v7_sha256": empreinte(V7), "script_v6": V6, "script_v6_sha256": empreinte(V6)}


def plat(d, p=""):
    if isinstance(d, dict):
        for k, v in d.items():
            yield from plat(v, f"{p}/{k}")
    else:
        yield p, d


# (K_h, K_s, τ, k, n, n_garde, δ, biais, fiches nulles, effet A logit, effet bêta A, effet B logit, ρ B, lien)
CAS = [(10, 10, 0.01, (1, 8), 60, 60, 0.05, 0.0125, 0, 0.0, 0.0, 0.0, 0.0, True),
       (3, 3, 0.10, (3,), 80, 50, 0.05, 0.0, 2, 0.0, 0.0, 0.0, 0.0, True),
       (10, 10, 0.01, (3,), 40, 40, 0.075, 0.0, 1, 1.0, 0.0, 0.0, 0.0, True),
       (10, 10, 0.01, (3,), 40, 40, 0.075, 0.0, 1, 0.0, 0.17, 0.0, 0.0, True),
       (10, 10, 0.01, (8,), 60, 60, 0.05, 0.0, 0, 0.0, 0.0, 1.0, 0.17, True),
       (10, 10, 0.01, (3,), 60, 40, 0.05, 0.0125, 1, 0.0, 0.0, 0.5, 0.0, False),
       (10, 3, 0.01, (8,), 60, 60, 0.05, 0.0, 0, 0.0, 0.0, 1.0, 0.0, True),
       (5, 10, 0.01, (8,), 60, 60, 0.05, 0.0125, 0, 1.0, 0.0, 0.5, 0.17, True)]
essais = []
for (K, Ks, tau, ks, n, ng, delta, biais, nulles, effet_a, beta_a, effet_b, corr_b, lien) in CAS:
    for k in ks:
        etiq = f"cellule-test|K={K}|Ks={Ks}|tau={tau}|k={k}|n={n}|ng={ng}|a={effet_a}|beta={beta_a}|b={effet_b}|rho={corr_b}|lien={lien}"
        ebh = {"lectures": ["A", "B"], "M": 2, "N": nulles, "alpha": 0.05}
        sorties, noms = [], []
        for mod in (v6, v7):
            loi = mod.LoiSynthetique(K, Ks, tau, 0.4, 0.1, True, effet_a, lien, beta_a, effet_b, corr_b)
            noms.append(loi.nom())
            ebh_loi = dict(ebh) | {"nulle_A": loi.variante_nulle(True), "nulle_B": loi.variante_nulle(False)}
            sorties.append(dict(plat(mod.cellule(loi, loi, 300, n, ng, delta, [40.0, 160.0, 320.0], k, biais, 20261029, etiq, True, ebh_loi))))
        a, b = sorties
        communs = [x for x in a if x in b]
        diffs = [x for x in communs if a[x] != b[x]]
        essais.append({"cellule": etiq, "nom_loi_v6": noms[0], "nom_loi_v7": noms[1], "champs_communs": len(communs),
                       "differences": len(diffs), "exemples": diffs[:5], "champs_seulement_v6": [x for x in a if x not in b],
                       "champs_seulement_v7": [x for x in b if x not in a],
                       "conforme": len(diffs) == 0 and len(communs) == len(a) == len(b) and noms[0] == noms[1]})
bilan["1_identite_v6_v7_echelle_logit"] = essais

# 2. témoin négatif : échelle bêta contre logit, même étiquette
etiq = "cellule-test|K=10|Ks=10|tau=0.01|k=8|n=60|ng=60|b=1.0"
loi6 = v6.LoiSynthetique(10, 10, 0.01, 0.4, 0.1, True, 0.0, True, 0.0, 1.0, 0.0)
loi7 = v7.LoiSynthetique(10, 10, 0.01, 0.4, 0.1, True, 0.0, True, 0.0, 1.0, 0.0, "beta")
c6 = dict(plat(v6.cellule(loi6, loi6, 300, 60, 60, 0.05, [40.0, 160.0], 8, 0.0, 20261029, etiq, True, None)))
c7 = dict(plat(v7.cellule(loi7, loi7, 300, 60, 60, 0.05, [40.0, 160.0], 8, 0.0, 20261029, etiq, True, None)))
diffs_temoin = [x for x in c6 if x in c7 and c6[x] != c7[x]]
bilan["2_temoin_negatif_beta_contre_logit"] = {"differences": len(diffs_temoin), "nom_v6": loi6.nom(), "nom_v7": loi7.nom(),
                                                "noms_differents": loi6.nom() != loi7.nom(), "conforme": len(diffs_temoin) > 0 and loi6.nom() != loi7.nom()}

# 3. K_s ≠ K_h : les noms de loi portent K_s depuis la v3 ; la v7 ne change que la façon de les demander (--K-s en produit cartésien)
noms_v6 = [v6.LoiSynthetique(K, Ks, 0.01, 0.4, 0.1).nom() for K, Ks in ((10, 10), (10, 5), (10, 3), (5, 5), (5, 3), (5, 10))]
noms_v7 = [v7.LoiSynthetique(K, Ks, 0.01, 0.4, 0.1).nom() for K, Ks in ((10, 10), (10, 5), (10, 3), (5, 5), (5, 3), (5, 10))]
bilan["3_noms_de_loi_K_s"] = {"v6": noms_v6, "v7": noms_v7, "conforme": noms_v6 == noms_v7 and len(set(noms_v7)) == 6}
bilan["conforme"] = (all(e["conforme"] for e in essais) and bilan["2_temoin_negatif_beta_contre_logit"]["conforme"]
                     and bilan["3_noms_de_loi_K_s"]["conforme"])
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(bilan, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("conforme :", bilan["conforme"], "| identité :", [e["conforme"] for e in essais], "| témoin :", bilan["2_temoin_negatif_beta_contre_logit"]["differences"],
      "| noms :", bilan["3_noms_de_loi_K_s"]["conforme"])
