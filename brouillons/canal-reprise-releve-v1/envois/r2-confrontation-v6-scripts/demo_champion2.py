"""Lignée imposée minimale (un appel par génération), 3 générations ; panne « modèle non conforme » au 3e appel de
l'espèce → g0 et g1 valides, g2 invalidée. On regarde le score témoin que le code retient pour N-039 b."""
import json, pathlib, sys, shutil
import numpy as np
sys.path.insert(0, "/srv/copie/essaim-m3-refonte-v1")
from essaim_m3.noyau import boucle, taches
from essaim_m3.noyau.confrontation import designations_et_concours
from essaim_m3.simulateur import appelants_simules
base = pathlib.Path("/srv/sorties/demo-champion2")
org = base / "org" / "organisme"
org.mkdir(parents=True)
(org / "manifeste.json").write_text('{"nom":"mini","version":"1","entree":"principal:executer"}', encoding="utf-8")
(org / "principal.py").write_text(
    "import json, os, shutil\n"
    "import noyau_client as nc\n"
    "ICI = os.path.dirname(os.path.abspath(__file__))\n"
    "def executer(contexte):\n"
    "    t = contexte['dossier_travail']\n"
    "    rep = {}\n"
    "    for tache in contexte['taches_test']:\n"
    "        r = nc.appeler('GEMINI_ARGON', 'Tache de la famille « %s ». Choisis.' % tache['famille'], role='t')\n"
    "        rep[tache['id']] = {'etiquette': tache['etiquettes'][0], 'confiance': 0.7}\n"
    "        break\n"  # un seul appel par génération
    "    json.dump(rep, open(os.path.join(t,'reponses_test.json'),'w'))\n"
    "    shutil.copytree(ICI, os.path.join(t,'successeur','organisme'), ignore=shutil.ignore_patterns('__pycache__'))\n", encoding="utf-8")
ss = np.random.SeedSequence(7)
r1, r2 = (np.random.default_rng(s) for s in ss.spawn(2))
banque = taches.banque_simulation(r1, 8, 8, 8)
doubles, esp = appelants_simules(r2)
esp["gemini-4-argon"].pannes = {"modele_non_conforme": {3}}  # 3e appel de l'espèce = g2 (aucun amorçage : lignée imposée)
n = boucle.Noyau(base / "run", "mission", banque, {"appels_max": 5, "usd_max": 5.0, "temps_max_s": 60}, 50.0, 3,
                 appelants=doubles, especes_amorcage=[], organismes_imposes={"mini": {"organisme": str(org), "famille": "gemini"}}, entropie=7)
n.amorcer()
rapport = n.boucler()
lignes = n.archive.lignes("mini")
d = designations_et_concours([], rapport["scores_finaux"], {})
valides = [l for l in lignes if l["statut"] == "OK" and not l.get("invalide") and not l.get("phase")]
sortie = {"generations": [(l["generation"], l["statut"], l.get("invalide"), l["score"]) for l in lignes],
          "scores_finaux_bruts": rapport["scores_finaux"],
          "temoin_retenu_par_designations_et_concours": d["designations"]["test_final_N039b"]["scores"],
          "derniere_generation_valide": (valides[-1]["generation"] if valides else None)}
if valides:
    f = n.archive.racine / valides[-1]["chemin"] / "juge" / "score-final.json"
    sortie["score_temoin_de_la_derniere_valide_attendu_N039b"] = json.loads(f.read_text())["score"] if f.exists() else None
print(json.dumps(sortie, ensure_ascii=False, indent=1))
pathlib.Path(base / "resultat.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1), encoding="utf-8")
