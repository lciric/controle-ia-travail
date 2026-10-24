"""Une génération archivée `INVALIDE_MODELE` (panne programmable du simulateur, comme dans
test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee) garde-t-elle un score témoin, et entre-t-elle dans
`designations_et_concours` (règle N-039 b : « dernière génération valide ») ?"""
import json, pathlib, sys
import numpy as np
sys.path.insert(0, "/srv/copie/essaim-m3-refonte-v1")
from essaim_m3.noyau import boucle, taches
from essaim_m3.noyau.confrontation import designations_et_concours
from essaim_m3.simulateur import appelants_simules
ss = np.random.SeedSequence(7)
r1, r2 = (np.random.default_rng(s) for s in ss.spawn(2))
banque = taches.banque_simulation(r1, 8, 8, 8)
doubles, esp = appelants_simules(r2)
n = boucle.Noyau("/srv/sorties/audit-invalide/run", "mission de test", banque, {"appels_max": 40, "usd_max": 5.0, "temps_max_s": 60}, 10.0, 2,
                 appelants=doubles, especes_amorcage=["GEMINI_ARGON", "CLAUDE_OPUS_5_5"], entropie=7)
n.amorcer()
esp["gemini-4-argon"].pannes = {"modele_non_conforme": {3}}
rapport = n.boucler()
lignes = n.archive.lignes()
d = designations_et_concours([], rapport["scores_finaux"], {})
sortie = {"generations": [(l["lignee"], l["generation"], l["statut"], l["invalide"]) for l in lignes],
          "generations_invalidees": rapport["generations_invalidees"],
          "courbes_score_de_developpement": rapport["courbes"],
          "scores_finaux_du_rapport": rapport["scores_finaux"],
          "designation_N039b": d["designations"]["test_final_N039b"]}
print(json.dumps(sortie, ensure_ascii=False, indent=1))
pathlib.Path("/srv/sorties/audit-invalide/resultat.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1), encoding="utf-8")
