"""Chiffres recalculés par le contre-lecteur (aucun réseau) : pire cas de la sonde, parts, règle M-1/d-6.
Usage : python -I -B chiffres_contre_lecteur_v70_v1.py RACINE_ORCHESTRATOR"""
import importlib.util, os, sys
RACINE = sys.argv[1]
sys.path.insert(0, RACINE)
from pole import pilote_mr2_v70 as P, proposeurs_pilote_v70 as PR
conf, _ = PR.lire_configuration(os.path.join(RACINE, "exemples", "pilote-mr2-v70", "configuration-pilote-mr2-v11.json"))
s = conf["sonde"]; tot = 0.0; parts = PR.parts_de_la_sonde(conf)
for n in P.PROPOSEURS:
    p = conf["proposeurs"][n]
    a, b = PR.pire_cas_d_un_appel(p, s["octets_consigne_max"]), PR.pire_cas_d_un_appel(p, s["octets_consigne_max"], s["borne_courte_jetons"])
    reel = sum(PR.pire_cas_d_un_appel(p, len(s["consignes"][k].encode()), None if k == "borne_gelee" else s["borne_courte_jetons"]) for k in s["consignes"])
    tot += a + b
    print(f"{n} : borne gelée {a:.6f} ; borne courte {b:.6f} ; somme {a+b:.6f} ; part {parts[n]} ; pire cas aux consignes de la v11 {reel:.6f}")
print(f"total {tot:.6f} ; lignes s1 {s['go']['s1']['montant_usd']} s2 {s['go']['s2']['montant_usd']} ; octets des consignes",
      {k: len(v.encode()) for k, v in s["consignes"].items()})
print("pilote : parts", {n: conf["proposeurs"][n]["part_usd"] for n in P.PROPOSEURS}, "; pi1", conf["go"]["pi1"]["montant_usd"], "pi2", conf["go"]["pi2"]["montant_usd"])
sp = importlib.util.spec_from_file_location("c", conf["commande"]["chemin_absolu"]); C = importlib.util.module_from_spec(sp); sp.loader.exec_module(C)
for servi in ("gpt-6-astra", "gpt-6-astra-20261101", "gpt-6-astra-2026-11-01", "gpt-6-astra-99999999", "gpt-6-astra-20261301", "gpt-6-astra-mini", "gpt-6-astra-20261101-x"):
    print("modele_conforme", servi, "→", C.modele_conforme("gpt-6-astra", servi))
print("règle des épisodes :", P.REGLE_EPISODES)
