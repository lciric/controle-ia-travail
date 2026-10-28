"""Audit du mécanisme (v1, après lecture des résultats, descriptif ; aucune règle de décision n'en dépend).
Pourquoi la forme corrigée se comporte-t-elle comme un tirage uniforme parmi les paires valides ?
Mesures sur les 400 mondes M_bien (graines principales) : corrélation de rang entre l'ordre glouton et q ;
domaines distincts parmi les 8 premiers articles ; similarité S = cos² moyenne par relation ; part de paires
proches parmi les paires valides que l'ordre glouton sert en premier.
Usage : python3 -I -B audit_mecanisme_v1.py --heure "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
import conditions_v1 as cd
import methodes_v1 as mt
import monde_v1 as mo

ICI = Path(__file__).resolve().parent


def spearman(x, y):
    def rangs(v):
        ordre = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        for k, i in enumerate(ordre):
            r[i] = float(k)
        return r
    rx, ry = rangs(x), rangs(y)
    n = len(x)
    mx, my = sum(rx) / n, sum(ry) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    return cov / (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heure", required=True)
    args = ap.parse_args()
    acc = {"rho_rang_q": [], "domaines_8_premiers_q": [], "domaines_8_premiers_q1": [],
           "S_meme": [], "S_proches": [], "S_eloignes": [],
           "proches_valides": [], "proches_12_premieres_a": [], "proches_12_premieres_a_q1": []}
    for i in range(400):
        w = mo.generer(cd.CONDITIONS["M_bien"], cd.graine_monde(cd.GRAINE_BASE_PRINCIPALE, "M_bien", i))
        q = [a["q"] for a in w["arts"]]
        ordre = mt.ordre_glouton(w, q)
        ordre1 = mt.ordre_glouton(w, [1.0] * w["n"])
        rang = [0] * w["n"]
        for r, a in enumerate(ordre):
            rang[a] = r
        acc["rho_rang_q"].append(spearman(rang, [-x for x in q]))
        acc["domaines_8_premiers_q"].append(len({w["arts"][a]["dom"] for a in ordre[:8]}))
        acc["domaines_8_premiers_q1"].append(len({w["arts"][a]["dom"] for a in ordre1[:8]}))
        for p in w["paires"]:
            ai, aj = w["arts"][p["i"]], w["arts"][p["j"]]
            cle = "S_meme" if ai["dom"] == aj["dom"] else ("S_proches" if p["proche"] else "S_eloignes")
            acc[cle].append(w["cos"][p["i"]][p["j"]] ** 2)
        val = w["valides"]
        acc["proches_valides"].append(sum(w["paires"][x]["proche"] for x in val) / len(val))
        for cle, qq in (("proches_12_premieres_a", q), ("proches_12_premieres_a_q1", [1.0] * w["n"])):
            s = mt.corrige(w, qq)
            acc[cle].append(sum(w["paires"][x]["proche"] for x in s) / len(s))
    res = {k: sum(v) / len(v) for k, v in acc.items()}
    for k, v in res.items():
        print(k.ljust(28), round(v, 4))
    sortie = {"objet": "audit du mécanisme de la forme corrigée (descriptif, après lecture des résultats)",
              "heure_lancement_utc": args.heure, "mondes": 400, "condition": "M_bien",
              "graines": "graines principales (identiques au run)", "resultats": res}
    (ICI / "audit-mecanisme-v1.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
