"""Attribution v2 sur la famille tirée — script neuf (v2b) : `puissance_monde_riche_v2.py attribution` s'arrêtait sur la classe
« latente », inconnue du résumé de la v1 (KeyError, `sorties-v2/attribution-w12-v2.stdout`, gardé). Même calcul par monde
(`puissance_monde_riche_v1._attribution_monde` sur les mondes du générateur v2), résumé étendu aux quatre classes.
Usage : `PYTHONHASHSEED=0 python3 -I -B attribution_v2b.py SORTIE.json`."""
import datetime, hashlib, json, os, sys
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import puissance_monde_riche_v2 as P2  # remplace preparer_monde de la v1 par la famille tirée
P1 = P2.P1

if __name__ == "__main__":
    out = sys.argv[1]
    if os.path.exists(out):
        sys.exit("refus : sortie existante")
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    with ProcessPoolExecutor(4) as ex:
        res = list(ex.map(P1._attribution_monde, range(12), chunksize=1))
    classes = ("forte", "moyenne", "latente", "faible")
    pc = {c: {"vrais_positifs": 0, "faux_negatifs": 0, "faux_positifs": 0} for c in classes}
    exact = tot = 0
    for mo in res:
        for x in mo:
            S, C = set(x["S"]), set(x["captes"])
            tot += 1
            exact += S == C
            for i, cl in x["classes"].items():
                if i in S and i in C:
                    pc[cl]["vrais_positifs"] += 1
                elif i in S:
                    pc[cl]["faux_negatifs"] += 1
                elif i in C:
                    pc[cl]["faux_positifs"] += 1
    r = {"lois": tot, "ensemble_exact": P1.part(exact, tot), "par_classe": pc}
    with open(out, "x", encoding="utf-8") as f:
        json.dump({"version": "attribution-v2b", "debut_utc": debut,
                   "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                   "pythonhashseed": os.environ.get("PYTHONHASHSEED"),
                   "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                   "resultat": r, "mondes": res}, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(r, ensure_ascii=False))
