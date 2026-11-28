import sys, json, time
sys.dont_write_bytecode = True
sys.path.insert(0, "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/module")
from pathlib import Path
import instrument_p4_v1 as ip
import lecture_p4_v1 as lp
from controle_ia.scellement import empreinte
depot = Path(sys.argv[1]); run3 = "20261020-120000-p3-jouet"
chemins = ip.chemins_du_run_source(run3)
chemins.update({"taches": "taches.json", "faits": "donnees/synth/faits.csv", "enjeux": "donnees/synth/enjeux.jsonl"})
emp = {k: {"chemin": c, "sha256": empreinte(depot / c)} for k, c in chemins.items()}
cfg = json.loads(json.dumps(ip.CONSTANTES_DU_TEXTE))
cfg.update({"mode": "jouet", "agent": {"nom": "agent-jouet", "revision": "0" * 40}, "couches": [0, 2], "T": 3,
            "duree_max_s": 600, "memoire_vive_min_go": 0, "run_source": run3, "empreintes_sources": emp,
            "sondes_principales": {"tromperie": "tromperie-difference_moyennes-c2", "enjeux": "enjeux-lineaire-c2"},
            "n_tirages": 200, "effectifs_validation": {"tromperie": 4, "enjeux": 4}, "faits_exclus_attendus": 1,
            "n_sondes_legeres": 32, "sondes_legeres_min": 31, "identifiant_espace": 4, "identifiant_deux_sauts": 99, "n_plancher": 8, "lignes_enjeux": 24,
            "phrases": {"D": ip.PHRASE_D, "H": ip.PHRASE_H, "B": ip.CANDIDATES_B[3], "Bprime": ip.CANDIDATES_BPRIME[1],
                        "candidates_B": list(ip.CANDIDATES_B), "candidates_Bprime": list(ip.CANDIDATES_BPRIME)}})
t = time.time()
r = ip.executer(cfg, depot, sys.argv[2], None, entropie=20261020, autoriser_depot_sale=True)
print("run", round(time.time() - t, 1), json.dumps(r["actions_notees"]), r["arret"])
t = time.time()
s = lp.analyser(depot, sys.argv[2], sys.argv[3], None, entropie=4242, autoriser_depot_sale=True)
print("lecture", round(time.time() - t, 1))
print(json.dumps(s["issue"], ensure_ascii=False)[:600])
print(json.dumps({k: s[k] for k in ("identite", "comparaisons")}, ensure_ascii=False)[:1500])
for k in ("C1", "M6a", "M6b", "C1_enjeux", "B_contre_H", "C1_pas_0"):
    d = s[k]; print(k, {x: d.get(x) for x in ("aire", "bas", "haut", "plancher_quantile", "etat", "delta", "echec")} if d else None)
print(s["M5"]["tromperie"].get("etat"), s["M5"]["tromperie"].get("aire"), s["M5"]["enjeux"].get("etat"))
print(json.dumps(s["descriptives"], ensure_ascii=False)[:800])
print(json.dumps(s["audit_R4"], ensure_ascii=False)[:1200])
