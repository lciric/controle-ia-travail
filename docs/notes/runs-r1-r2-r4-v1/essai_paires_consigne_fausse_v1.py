"""CLA-04 (4) : chemin des corrections de la table sur les vraies pièces de P3, sous la vraie consigne et sous la consigne
fausse du contrôle négatif (processeur, sans modèle, sans score). Pour chacun des 15 épisodes corrigés :
- sous la vraie consigne, `appliquer_entree` redonne exactement l'empreinte de trajectoire de P3 ;
- sous la consigne fausse (`rejeu_activations_v2.controle_negatif` : honnête pour une condition instruite, saboteur pour
  l'honnête), `appliquer_entree` s'applique sans garde levée, les identifiants de chaque action sont ceux de la vraie
  consigne (seule la consigne change) et l'empreinte diffère de celle de P3 (le contexte est bien faux).
Rend aussi, par condition, les actions à trajectoire identique (couverture sous la règle de repli) et leur marge sur la
règle des 80 %.

    PYTHONPATH=src python docs/notes/runs-r1-r2-r4-v1/essai_paires_consigne_fausse_v1.py <tokeniseur> <config v3>
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from transformers import AutoTokenizer

from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.pilote_a import charger_taches, tache_de
from controle_ia.harnais.formats import FormatChat
from controle_ia.premier_test_ia.conditions import charger_consignes, environnement
from controle_ia.runs_nuit import rejeu_activations_v1 as v1
from controle_ia.runs_nuit.alignement_v1 import charger_identite, charger_textes_alignes
from controle_ia.runs_nuit.resolution_tokenisation_v1 import appliquer_entree, table_des_octets

tok_dir, chemin_config = sys.argv[1], sys.argv[2]
c = json.loads(Path(chemin_config).read_text(encoding="utf-8"))
tok = AutoTokenizer.from_pretrained(tok_dir)
fmt = FormatChat(tok, variables=c["agent"]["variables_gabarit"])
fmt.fins = {128001, 128008, 128009, int(tok.eos_token_id)} | {fmt._pieces(("x", "y"))["cloture"][0]}
identite = charger_identite(c["chemin_scores"], c["scores_sha256"])
lignes = charger_textes_alignes(c["chemin_textes"], identite, c["textes_sha256"])
fiches = v1.charger_fiches(c["chemin_fiches"], c["fiches_sha256"])
taches = {t["identifiant"]: t for t in charger_taches(c["chemin_taches"])}
consignes = charger_consignes(c["chemin_consignes"], c["consignes_sha256"])
guide = charger_invite("H1-classification")
octets_table = Path(c["chemin_table_tokenisation"]).read_bytes()
assert hashlib.sha256(octets_table).hexdigest() == c["table_tokenisation_sha256"]
table = json.loads(octets_table)
T = int(c["T"])
jet, jn = [int(x) for x in identite["jetons"]], [int(x) for x in identite["jetons_notes"]]
par_ep = {}
for i, x in enumerate(lignes):
    par_ep.setdefault(x["episode"], []).append(i)
octets = table_des_octets(tok)[0]
res = []
for ent in table["episodes"]:
    if ent["methode"] == "non_resolu":
        continue
    e = ent["episode"]
    rs = par_ep[e]
    L, J, JN = [lignes[r] for r in rs], [jet[r] for r in rs], [jn[r] for r in rs]
    x0 = L[0]
    vrai = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
    rv = appliquer_entree(fmt, vrai, T, L, J, JN, ent, octets)
    ok_vrai = v1.empreinte_trajectoire(v1.episode_harnais(e, T, rv)) == fiches[e]["trajectoire"]
    faux_nom = "saboteur" if x0["condition"] == "honnete" else "honnete"
    faux = environnement(faux_nom, tache_de(taches[x0["tache"]]), T, guide, consignes)
    rf = appliquer_entree(fmt, faux, T, L, J, JN, ent, octets)
    memes_ids = all([int(i) for i in a["nv"]] == [int(i) for i in b["nv"]] for a, b in zip(rv["actions"], rf["actions"]))
    diff = v1.empreinte_trajectoire(v1.episode_harnais(e, T, rf)) != fiches[e]["trajectoire"]
    res.append({"episode": e, "methode": ent["methode"], "consigne_fausse": faux_nom, "empreinte_p3_vraie_consigne": ok_vrai,
                "actions_identiques_sous_consigne_fausse": memes_ids, "empreinte_differente_sous_consigne_fausse": diff})
# couverture sous la règle de repli (fidèles = trajectoires identiques après la table), par condition
traj = np.zeros(len(lignes), bool)
for e, rs in par_ep.items():
    x0 = lignes[rs[0]]
    env = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
    rec = v1.reconstruire_episode(fmt, env, T, [lignes[r] for r in rs], [jet[r] for r in rs], [jn[r] for r in rs])
    traj[rs] = v1.empreinte_trajectoire(v1.episode_harnais(e, T, rec)) == fiches[e]["trajectoire"]
for x in res:
    traj[par_ep[x["episode"]]] = True
cond = np.asarray(identite["condition"])
repli = {k: {"actions": int((cond == k).sum()), "trajectoire_identique": int((traj & (cond == k)).sum()),
             "part": round(float((traj & (cond == k)).sum() / (cond == k).sum()), 4),
             "marge_sur_80_pour_cent": int((traj & (cond == k)).sum() - 0.8 * (cond == k).sum())}
         for k in sorted(set(cond.tolist()))}
print(json.dumps({"episodes_corriges": len(res),
                  "tous_conformes": all(x["empreinte_p3_vraie_consigne"] and x["actions_identiques_sous_consigne_fausse"]
                                        and x["empreinte_differente_sous_consigne_fausse"] for x in res),
                  "par_episode": res, "repli_total": int(traj.sum()), "repli_par_condition": repli},
                 ensure_ascii=False, indent=1))
