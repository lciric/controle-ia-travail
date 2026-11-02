"""Version 2 (voie retenue après la concordance de conv-audit, n° 343 : les actions des épisodes non résolus sont
jugées par la tolérance, comme toute action hors contexte exact ; table v2). Rejeu sur processeur, sans modèle, de la phase de reconstruction de la relance de R1 (règles A et B de l'addendum)
sur les vraies pièces de P3 : même chemin que `rejeu_activations_v2._executer` jusqu'à la carte (reconstruction de base,
empreintes, `classer_episodes`, `appliquer_entree`, vérification de l'empreinte de P3 pour chaque épisode corrigé).
Rend les comptes : trajectoires identiques, épisodes non conformes, actions conformes, contexte exact, et les bornes
attendues de P-R5 (part des actions notées qui peuvent être fidèles). Ne lit aucun score, aucune activation, aucune
étiquette : « notée » = `jetons_notes` > 0 (P3 ne laisse un score NaN que pour un empan vide,
`premier_test_ia.run.tableaux_des_scores`).

    PYTHONPATH=src python docs/notes/runs-r1-r2-r4-v1/comptes_table_relance_v1.py <tokeniseur> <config v3>
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
from controle_ia.runs_nuit.resolution_tokenisation_v1 import CORRIGEES, appliquer_entree, classer_episodes, table_des_octets

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
# la table n'est pas encore scellée (brouillon) : empreinte du fichier comparée directement à celle de la configuration
octets_table = Path(c["chemin_table_tokenisation"]).read_bytes()
assert hashlib.sha256(octets_table).hexdigest() == c["table_tokenisation_sha256"], "empreinte de la table ≠ configuration"
table = json.loads(octets_table)
T, n = int(c["T"]), len(lignes)
jet, jn = [int(x) for x in identite["jetons"]], [int(x) for x in identite["jetons_notes"]]
cond = np.asarray(identite["condition"])
par_ep = {}
for i, x in enumerate(lignes):
    par_ep.setdefault(x["episode"], []).append(i)
conforme, contexte, traj = np.zeros(n, bool), np.zeros(n, bool), np.zeros(n, bool)
envs = {}
for e, rs in par_ep.items():
    x0 = lignes[rs[0]]
    envs[e] = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
    rec = v1.reconstruire_episode(fmt, envs[e], T, [lignes[r] for r in rs], [jet[r] for r in rs], [jn[r] for r in rs])
    tous = True
    for r, a in zip(rs, rec["actions"]):
        conforme[r] = a["conforme"]
        tous = tous and a["conforme"]
        contexte[r] = tous
    traj[rs] = v1.empreinte_trajectoire(v1.episode_harnais(e, T, rec)) == fiches[e]["trajectoire"]
base_ident = int(traj.sum()) // T
signales = [e for e, rs in par_ep.items() if conforme[rs].all() and not traj[rs].all()]
corriger, non_resolus = classer_episodes(signales, table, int(c["seuil_non_conformes"]))
octets = table_des_octets(tok)[0]
for e, ent in corriger.items():
    rs = par_ep[e]
    rec = appliquer_entree(fmt, envs[e], T, [lignes[r] for r in rs], [jet[r] for r in rs], [jn[r] for r in rs], ent,
                           octets)
    assert v1.empreinte_trajectoire(v1.episode_harnais(e, T, rec)) == fiches[e]["trajectoire"], e
    traj[rs] = True
    contexte[rs] = True
b = np.zeros(n, bool)
for e in non_resolus:
    b[par_ep[e]] = True
contexte &= ~b
notees = np.asarray(jn) > 0
haut = notees & conforme
bas = notees & contexte
sortie = {
    "episodes": len(par_ep), "conformes_longueur_episodes": sum(1 for rs in par_ep.values() if conforme[rs].all()),
    "trajectoires_identiques_base": base_ident, "signales": len(signales),
    "corrections": {m: sum(1 for x in corriger.values() if x["methode"] == m) for m in CORRIGEES},
    "trajectoires_identiques_apres_A": int(traj.sum()) // T,
    "episodes_non_resolus_B": non_resolus, "actions_non_resolues_B": int(b.sum()),
    "actions": n, "notees": int(notees.sum()), "conformes_longueur": int(conforme.sum()),
    "contexte_exact_apres_AB": int(contexte.sum()), "notees_contexte_exact": int(bas.sum()),
    "notees_trajectoire_identique": int((notees & traj).sum()),
    "prefixes_contexte_conforme_sans_empreinte": int((contexte & ~traj).sum()),
    "actions_non_resolues_conformes": int((b & conforme).sum()),
    "p_r5_borne_haute": {"fideles_possibles": int(haut.sum()), "part": round(float(haut.sum() / notees.sum()), 4),
                         "definition": "notées et conformes en longueur, épisodes non résolus compris (écart supposé ≤ tolérance)"},
    "p_r5_scenario_bas_contexte_exact": {"fideles": int(bas.sum()), "part": round(float(bas.sum() / notees.sum()), 4),
                                        "definition": "seules les notées à contexte_conforme vrai passent la tolérance (scénario, pas une borne)"},
    "par_condition": {k: {"notees": int((notees & (cond == k)).sum()), "borne_haute": int((haut & (cond == k)).sum()),
                          "contexte_exact": int((bas & (cond == k)).sum()),
                          "trajectoire_identique": int((notees & traj & (cond == k)).sum())} for k in sorted(set(cond.tolist()))},
}
print(json.dumps(sortie, ensure_ascii=False, indent=1))
