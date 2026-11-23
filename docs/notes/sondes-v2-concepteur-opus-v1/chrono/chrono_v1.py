"""Chronométrage de l'épreuve plantée des sondes v2 : DURÉES SEULEMENT.
Aucune lecture n'est imprimée ni gardée : les sorties de lire_monde / lire_etalon sont jetées.
Usage : python -I chrono_v1.py MODE CAS... (MODE complet : P,T,A ; MODE etalon : P,F,T,A)"""
import sys, time, json, tempfile, os
sys.path.insert(0, os.environ["DEPOT"] + "/src")
from controle_ia.sondes_v2 import monde_plante_v3 as mp, statistiques_v1 as st
from controle_ia.sondes_v2.formes_closes_v1 import threadpool_limits

def main():
    mode, mondes_arg, n_rep = sys.argv[1], sys.argv[2], int(sys.argv[3])
    nul, tirages = int(sys.argv[4]), int(sys.argv[5])
    cas = [tuple(int(x) for x in c.split(",")) for c in sys.argv[6:]]
    v, _ = mp.charger_verites()
    seuils = {"alpha": 0.05, "u_fort": 0.9}
    out = []
    with tempfile.TemporaryDirectory() as tmp, threadpool_limits(1):
        journal = os.path.join(tmp, "journal.jsonl")
        for c in cas:
            if mode == "complet":
                P, F, T, A = c[0], 1, c[1], c[2]
            else:
                P, F, T, A = c
            mondes = [m for m, d in v["mondes"].items() if mode in d["modes"]] if mondes_arg == "tous" else mondes_arg.split(",")
            for m in mondes:
                p = mp.parametres(v, m, P, F, T, A, 256, mode)
                crit = [k for k in v["mondes"][m]["criteres"] if mode == "complet" or k["lecture"] in mp.CRITERES_ETALON]
                avec_id = any(k["lecture"] == "identite" for k in crit)
                t0 = time.process_time(); w0 = time.time()
                for r in range(n_rep):
                    _, rngs = st.generateurs_nommes(12345, f"chrono/{mode}/{c}/{m}/{r}/")
                    if mode == "complet":
                        _ = mp.lire_monde(p, rngs, journal, f"{c}/{m}/{r}", seuils, nul, tirages)
                    else:
                        _ = mp.lire_etalon(p, rngs, seuils, tirages, 200, avec_id)
                    del _
                out.append({"mode": mode, "cas": list(c), "monde": m, "repliques": n_rep,
                            "cpu_s_par_replique": (time.process_time() - t0) / n_rep,
                            "mur_s_par_replique": (time.time() - w0) / n_rep})
                print(json.dumps(out[-1], ensure_ascii=False), flush=True)

main()
