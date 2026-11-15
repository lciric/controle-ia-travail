"""Résumé des lots (taille, puissance, coût) — v1. Mise au point exploratoire, aucune revendication.

Usage : python -I essai_confiance_resume_v1.py SORTIE.json LOT1.json [LOT2.json ...]
Pour chaque (cas, J, n_tr) : taux de promotion par carte et par méthode, intervalle de Clopper-Pearson à 95 % ; taux de
couverture de chaque ensemble de confiance ; audit A1 (une copie promue par une méthode à ensemble de confiance alors que
l'ensemble couvrait le monde = défaut de certificat) ; pour la puissance, comparaison appariée (mêmes tirages, mêmes
instants) de chaque méthode avec v9_banc, limite et v8_banc : promues par l'une et pas l'autre, valeur p bilatérale exacte
du test des paires discordantes ; coût : secondes par monde (toutes méthodes ensemble) et empreinte de chaque lot lu.
"""

import collections
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np  # noqa: E402
from scipy.stats import binomtest  # noqa: E402

import essai_confiance_banc_v1 as bc  # noqa: E402

REFS = ("v9_banc", "limite", "v8_banc")


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    sortie, lots = sys.argv[1], sys.argv[2:]
    if os.path.exists(sortie):
        raise SystemExit("refus : la sortie existe")
    groupes = collections.defaultdict(list)
    sources = []
    for p in lots:
        d = json.load(open(p))
        sources.append({"fichier": os.path.basename(p), "sha256": sha(p), "mondes": d["mondes"], "duree_s": d["duree_s"]})
        groupes[(d["cas"], d["J"], d["n_tr"])].extend(d["lignes"])
    res = {}
    for (cas, J, n_tr), L in sorted(groupes.items()):
        mondes = sorted(l["monde"] for l in L)
        assert len(set(mondes)) == len(mondes), "monde en double"
        cartes = [k for k in L[0]["resultats"] if not k.startswith("_")]
        g = {"mondes": len(L), "premier": mondes[0], "dernier": mondes[-1],
             "secondes_par_monde": {"moyenne": round(float(np.mean([l["resultats"]["_secondes_par_monde"] for l in L])), 3),
                                    "max": round(float(np.max([l["resultats"]["_secondes_par_monde"] for l in L])), 3)},
             "cartes": {}}
        cv = collections.Counter()
        for l in L:
            for m, v in l["resultats"]["_couverture"].items():
                cv[m] += int(v)
        if cv:
            g["couverture"] = {m: bc.taux(len(L) - k, len(L)) | {"note": "taux de NON-couverture"} for m, k in sorted(cv.items())}
        for c in cartes:
            meths = list(L[0]["resultats"][c].keys())
            pr = {m: np.array([l["resultats"][c][m]["promue"] for l in L]) for m in meths}
            lw = {m: np.array([l["resultats"][c][m]["log_w_max"] for l in L]) for m in meths}
            gc = {"taux": {m: bc.taux(int(pr[m].sum()), len(L)) | {"log_w_max_mediane": float(np.median(lw[m]))} for m in meths}}
            audit = {}
            for m in meths:
                if m in L[0]["resultats"]["_couverture"] and c == "copie":
                    cov = np.array([l["resultats"]["_couverture"][m] for l in L])
                    audit[m] = int((pr[m] & cov).sum())
            if audit:
                gc["audit_A1_copie_promue_alors_que_couverte"] = audit
            if c == "decouverte":
                app = {}
                for m in meths:
                    for r in REFS:
                        if m == r:
                            continue
                        a = int((pr[m] & ~pr[r]).sum())
                        b = int((~pr[m] & pr[r]).sum())
                        pv = float(binomtest(a, a + b, 0.5).pvalue) if a + b > 0 else 1.0
                        app.setdefault(m, {})[r] = {"methode_seule": a, "reference_seule": b,
                                                     "difference_de_taux": round((a - b) / len(L), 4),
                                                     "valeur_p_paires_discordantes": round(pv, 6)}
                gc["apparie"] = app
            g["cartes"][c] = gc
        res[f"{cas}|J={J}|n_tr={n_tr}"] = g
    doc = {"essai": "essai_confiance_resume_v1", "sources": sources, "groupes": res}
    with open(sortie, "w") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
    print(f"résumé : {len(res)} groupes -> {sortie}")


if __name__ == "__main__":
    main()
