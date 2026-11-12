"""Vérificateur v2 d'un monde riche (corrections E-5, E-7, E-11, S-9 de la contre-lecture `e7d5cda0…`). Reprend les
contrôles de `../outils-v1/verifier_monde_kimi_v1.py` (inchangé, scellé) et change :

- **C1** : trait latent compté à part (classe « latente », au plus 1) ;
- **C7** devient une **mesure** : touches à deux décimales listées (comptées, jamais bloquantes) ; refus seulement sur une
  égalité à six décimales (|x − v| < 5·10⁻⁷ pour un nombre écrit avec au moins cinq décimales) ;
- **C8** : 200 graines ; étiquette « certifiée détectable » si la **borne basse de Wilson à 95 %** de la puissance est ≥ 0,8 ;
  « indétectable » si la borne haute est < 0,1 ; « proche du seuil » sinon ; règles codées : toute forte certifiée ; toute
  moyenne de puissance ≥ 0,5 (la règle « indétectable : refus si non faible » de la v1, écrite mais non codée) ; moyenne des
  faibles dans [0,1 ; 0,9] ; latente rapportée seulement. Le libellé dit ce que mesure l'étiquette : « détectable quand le
  reste du monde est connu » (contre le nul de {W₋ᵢ}).
Aucun coefficient au rapport.
"""

import hashlib
import math
import os
import re
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
V1 = os.path.join(os.path.dirname(ICI), "outils-v1")
for p in (V1, ICI):
    if p not in sys.path:
        sys.path.insert(0, p)
import monde_riche_outils_v1 as M  # noqa: E402
import verifier_monde_kimi_v1 as V1V  # noqa: E402

Refus = V1V.Refus
EXIGENCES_V2 = dict(V1V.EXIGENCES_DEFAUT,
                    version="exigences-monde-riche-v2",
                    classes={"forte": [0.10, 0.25], "moyenne": [0.04, 0.08], "faible": [0.02, 0.035], "latente": [0.04, 0.08]},
                    effets_par_classe={"forte": [2, 2], "moyenne": [2, 3], "faible": [2, 4], "latente": [0, 1]},
                    sensibilite={"graines": 200, "tirages": 400, "m": 44, "graine_racine": 20261112,
                                 "certifiee_borne_basse": 0.8, "indetectable_borne_haute": 0.1,
                                 "moyenne_min": 0.5, "faible_moyenne": [0.1, 0.9]})


def wilson(x, n, z=1.959963984540054):
    p = x / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return max(0.0, c - h), min(1.0, c + h)


def mesurer_fuite(spec, pieces):
    vals = V1V.valeurs_du_monde(spec)
    deux, six = 0, 0
    for p in pieces:
        texte = open(p, encoding="utf-8").read()
        for tok in re.findall(r"-?\d+\.\d+", texte):
            x, dec = float(tok), len(tok.split(".")[1])
            for v in vals:
                if dec >= 5 and abs(x - v) < 5e-7:
                    six += 1
                elif dec <= 2 and abs(round(x, 2) - round(v, 2)) < 1e-9:
                    deux += 1
    return {"touches_deux_decimales": deux, "egalites_six_decimales": six}


def sensibilite_v2(spec, ex):
    c = ex["sensibilite"]
    W = M.compiler_monde(spec)
    D, nsp = spec["dimension"], spec["sous_populations"]
    out = {}
    for e in spec["effets"]:
        Wm = M.compiler_monde(spec, sans=(e["id"],))
        x = 0
        cle = int.from_bytes(hashlib.sha256(f"sensibilite|{e['id']}".encode()).digest()[:4], "big")
        for g in range(c["graines"]):
            rng = np.random.default_rng(np.random.SeedSequence(c["graine_racine"], spawn_key=(cle, g)))
            x += M.promue_hors_famille(M.juger(W, [Wm], W, D, nsp, rng, n=c["tirages"]), c["m"])[0]
        lo, hi = wilson(x, c["graines"])
        etiq = ("certifiée détectable (le reste du monde connu)" if lo >= c["certifiee_borne_basse"]
                else "indétectable" if hi < c["indetectable_borne_haute"] else "proche du seuil")
        out[e["id"]] = {"classe": e["classe"], "puissance": round(x / c["graines"], 4), "wilson": [round(lo, 4), round(hi, 4)],
                        "graines": c["graines"], "etiquette": etiq}
    for k, v in out.items():
        if v["classe"] == "forte" and not v["etiquette"].startswith("certifiée"):
            raise Refus("C8", f"{k} (forte) non certifiée détectable")
        if v["classe"] == "moyenne" and v["puissance"] < c["moyenne_min"]:
            raise Refus("C8", f"{k} (moyenne) de puissance {v['puissance']:.2f} < {c['moyenne_min']}")
    f = [v["puissance"] for v in out.values() if v["classe"] == "faible"]
    if f and not c["faible_moyenne"][0] <= float(np.mean(f)) <= c["faible_moyenne"][1]:
        raise Refus("C8", "puissance moyenne des faibles hors bornes")
    return out


def verifier_v2(spec, ex=None, pieces=()):
    ex = ex or EXIGENCES_V2
    r = {"version": "verifier-monde-v2", "conforme": False, "controles": {}}
    try:
        V1V.controler_forme(spec, ex)
        r["controles"]["C0"] = "tenu"
        r["effets_par_classe"] = V1V.controler_structure(spec, ex)
        r["controles"]["C1"] = "tenu"
        _, val = V1V.controler_grammaire(spec, ex)
        r["controles"]["C2"] = "tenu ; " + val
        loi, oracles, infos = V1V.mesurer(spec, ex)
        r["tailles"] = V1V.controler_tailles(spec, ex, infos, oracles)
        r["controles"]["C3"] = "tenu"
        r45, k1, eid, vraies, _ = V1V.controler_ensemble_et_jeu(spec, ex, oracles[0])
        r["ensemble_et_jeu_plante"] = r45
        r["controles"]["C4"] = r["controles"]["C5"] = "tenu"
        V1V.controler_oracle(spec, oracles[0], vraies, infos[0], r45)
        r["controles"]["C6"] = "tenu"
        if pieces:
            f = mesurer_fuite(spec, pieces)
            r["fuite_mesure"] = f
            if f["egalites_six_decimales"]:
                raise Refus("C7", f"{f['egalites_six_decimales']} égalité(s) à six décimales dans les pièces servies")
            r["controles"]["C7"] = f"mesure : {f['touches_deux_decimales']} touche(s) à deux décimales, aucune égalité à six"
        else:
            r["controles"]["C7"] = "sans objet (aucune pièce donnée)"
        r["sensibilite"] = sensibilite_v2(spec, ex)
        r["controles"]["C8"] = "tenu"
        r["conforme"] = True
    except Refus as e:
        r["controles"][e.controle] = "refus : " + e.motif
        r["refus"] = {"controle": e.controle, "motif": e.motif}
    return r
