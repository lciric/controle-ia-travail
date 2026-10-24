"""Une lignée a deux générations valides (scores témoins non nuls) puis une génération invalidée (MODELE_NON_CONFORME) ;
N-039 b veut le score témoin « à sa dernière génération valide ». On lit ce que `confrontation.designations_et_concours`
(via `boucle._scores_finaux`) retient pour cette lignée. Panne programmable du simulateur (comme dans le test du dépôt)."""
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
n = boucle.Noyau("/srv/sorties/demo-champion/run", "mission", banque, {"appels_max": 40, "usd_max": 5.0, "temps_max_s": 60}, 20.0, 3,
                 appelants=doubles, especes_amorcage=["GEMINI_ARGON"], entropie=7)
n.amorcer()
# la lignée gemini-argon : g0 et g1 valides, puis une panne de modèle non conforme pendant g2
# (les appels d'amorçage + 2 générations consomment des appels ; on vise un numéro d'appel de g2)
esp["gemini-4-argon"].pannes = {"modele_non_conforme": {40}}  # un appel tardif, pendant g2
rapport = n.boucler()
lignes = n.archive.lignes("gemini-argon")
sf = boucle.Noyau._scores_finaux.__get__(n)(lignes)  # scores témoins par lignée (ce que la confrontation utilise)
d = designations_et_concours([], rapport["scores_finaux"], {})
# dernière génération VALIDE (statut OK, non invalide) selon N-039 b
valides = [l for l in lignes if l["statut"] == "OK" and not l.get("invalide") and not l.get("phase")]
derniere_valide = valides[-1] if valides else None
sortie = {
  "generations": [(l["generation"], l["statut"], l.get("invalide"), l["score"]) for l in lignes],
  "scores_finaux_bruts_toutes_generations": rapport["scores_finaux"],
  "score_temoin_retenu_par_le_code_v_dernier": d["designations"]["test_final_N039b"]["scores"],
  "derniere_generation_valide_selon_N039b": (derniere_valide["generation"] if derniere_valide else None),
}
# score témoin de la dernière génération valide (ce que N-039 b demande)
if derniere_valide is not None:
    f = n.archive.racine / derniere_valide["chemin"] / "juge" / "score-final.json"
    sortie["score_final_de_la_derniere_valide"] = json.loads(f.read_text())["score"] if f.exists() else None
print(json.dumps(sortie, ensure_ascii=False, indent=1))
pathlib.Path("/srv/sorties/demo-champion/resultat.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1), encoding="utf-8")
