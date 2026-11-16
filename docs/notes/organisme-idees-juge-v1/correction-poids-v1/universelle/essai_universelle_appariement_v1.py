"""Appariements des essais de puissance (inférence universelle) — v1 : relit les sorties scellées des lots « a » et « b »
(mêmes mondes, mêmes tirages, mêmes instants : même entropie et même clé), vérifie leurs empreintes contre les compagnons,
vérifie que la référence v9 est identique monde par monde d'un lot à l'autre, et calcule pour chaque méthode, contre le
v9 et contre le nul limité : promotions de la seule méthode, de la seule référence, écart de taux, et valeur p exacte
bilatérale de McNemar (binomiale sur les paires discordantes). Aucun tirage. Usage : python … SORTIE.json"""
import hashlib, json, os, sys

from scipy.stats import binomtest

ICI = os.path.dirname(os.path.abspath(__file__))


def lire(nom):
    p = os.path.join(ICI, nom)
    h = hashlib.sha256(open(p, "rb").read()).hexdigest()
    attendu = open(p + ".sha256").read().split()[0]
    if h != attendu:
        raise SystemExit(f"empreinte non conforme : {nom}")
    return json.load(open(p)), h


def main():
    sortie = sys.argv[1]
    if os.path.exists(sortie):
        raise SystemExit("sortie existante")
    doc = {"essai": "appariement_puissance", "version": "v1", "sources": {}, "doses": {}}
    for dose in ("0.25", "0.40", "0.55"):
        a, ha = lire(f"sortie-puissance-{dose}-a-v1.json")
        b, hb = lire(f"sortie-puissance-{dose}-b-v1.json")
        doc["sources"][dose] = {f"sortie-puissance-{dose}-a-v1.json": ha, f"sortie-puissance-{dose}-b-v1.json": hb}
        if a["par_monde"]["v9"]["promue"] != b["par_monde"]["v9"]["promue"]:
            raise SystemExit(f"v9 différent d'un lot à l'autre à la dose {dose}")
        pm = dict(a["par_monde"]); pm.update({k: v for k, v in b["par_monde"].items() if k != "v9"})
        R = a["mondes"]
        res = {}
        for ref in ("v9", "limite"):
            r = pm[ref]["promue"]
            for m, v in pm.items():
                if m == ref:
                    continue
                x = v["promue"]
                seule_m = sum(1 for i in range(R) if x[i] == "1" and r[i] == "0")
                seule_r = sum(1 for i in range(R) if x[i] == "0" and r[i] == "1")
                p = binomtest(seule_m, seule_m + seule_r, 0.5).pvalue if seule_m + seule_r else 1.0
                res[f"{m}_contre_{ref}"] = {"seule_la_methode": seule_m, "seule_la_reference": seule_r,
                                            "ecart_de_taux": round((seule_m - seule_r) / R, 4), "mcnemar_p_exact": float(f"{p:.3g}")}
        doc["doses"][dose] = {"mondes": R, "taux": {m: round(v["promue"].count("1") / R, 4) for m, v in pm.items()}, "apparies": res}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    for d, v in doc["doses"].items():
        print(d, v["taux"])


if __name__ == "__main__":
    main()
