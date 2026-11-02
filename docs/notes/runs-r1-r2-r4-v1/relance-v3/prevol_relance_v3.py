"""Pré-vol de la relance de R1 sur la table v3, sur processeur, sans modèle 8B, vraies pièces de P3 (liens symboliques
dans un dossier temporaire, jamais committés) : configuration `prereg/R1-rejeu-config-v5.json` ; table v3 chargée par
`rejeu_activations_v3.charger_table` et **revérifiée au chargement** par `rejeu_activations_v3.verifier_table_au_chargement`
(chaque correction appliquée doit redonner l'empreinte de trajectoire de P3) ; puis le chemin de `_executer` jusqu'à la
carte, copié ligne à ligne (reconstruction de base, empreintes, règles A et B par `classer_episodes`, corrections
appliquées par `appliquer_entree` de la v3 et revérifiées par l'empreinte de P3, `contexte_conforme`, méthodes de
résolution, éligibles à l'échantillon de fidélité) ; enfin, chemin des 22 corrections sous la consigne fausse du
contrôle négatif (copie de `controle_negatif` sans modèle : aucune garde levée, mêmes identifiants d'actions, empreinte
différente de celle de P3). Comptes seulement : les scores de P3 ne sont pas chargés
(`resolution_graine_v1.charger_identite_sans_scores`, clé par clé) ; aucun texte, aucune activation, aucune étiquette de
juge n'est lu ni affiché ; « notée » = `jetons_notes` > 0 (indicateur sans score ; le code définit « notée » par la
finitude de l'écart de fidélité, qui exige les scores).

    PYTHONPATH=<arbre>/src python prevol_relance_v3.py <arbre> <dépôt principal> <dossier temporaire neuf> <tokeniseur>
"""
import hashlib
import json
import os
import sys
import time
from pathlib import Path

import numpy as np
from transformers import AutoTokenizer

ARBRE, PRINCIPAL, R, TOK = (Path(x).resolve() for x in sys.argv[1:5])
t0 = time.perf_counter()

from controle_ia.environnements.invites import charger_invite  # noqa: E402
from controle_ia.environnements.pilote_a import charger_taches, tache_de  # noqa: E402
from controle_ia.harnais.formats import FormatChat  # noqa: E402
from controle_ia.premier_test_ia.conditions import charger_consignes, environnement  # noqa: E402
from controle_ia.runs_nuit import rejeu_activations_v1 as v1  # noqa: E402
from controle_ia.runs_nuit import rejeu_activations_v3 as rc  # noqa: E402
from controle_ia.runs_nuit import resolution_graine_v1 as rg  # noqa: E402
from controle_ia.runs_nuit.alignement_v1 import charger_textes_alignes, empreinte_identite  # noqa: E402
from controle_ia.runs_nuit.resolution_tokenisation_v1 import classer_episodes, table_des_octets  # noqa: E402
from controle_ia.scellement import verifier  # noqa: E402

R.mkdir(parents=True, exist_ok=False)
for d in ("donnees/20261019-230011-p3-reel", "donnees/t05-pilote-v1", "diag/20261019-230011-p3-reel",
          "runs/20261019-230011-p3-reel"):
    (R / d).parent.mkdir(parents=True, exist_ok=True)
    (R / d).symlink_to(PRINCIPAL / d)
(R / "prereg").mkdir()
for n in ("P3-consignes-v1.md", "P3-consignes-v1.md.sha256", "R1-rejeu-config-v5.json",
          "R1-table-tokenisation-v3.json", "R1-table-tokenisation-v3.json.sha256", "R1-R2-rejeu-p3-v1.md",
          "R1-R2-rejeu-p3-v1.md.sha256"):
    (R / "prereg" / n).symlink_to(ARBRE / "prereg" / n)
os.chdir(R)
sortie = {"outil": "prevol_relance_v3.py", "arbre": str(ARBRE)}
tok_sha = {n: hashlib.sha256((TOK / n).read_bytes()).hexdigest()
           for n in ("tokenizer.json", "tokenizer_config.json", "special_tokens_map.json")}
sortie["tokeniseur_sha256"] = tok_sha

# ---- configuration v5 (gardes du module) et pièces citées
cp = Path("prereg/R1-rejeu-config-v5.json")
config = json.loads(cp.read_text(encoding="utf-8"))
rc.exiger_config(config)
assert config["mode"] == "reel" and set(config) == set(rc.CLES)
sortie["configuration"] = {"chemin": str(cp), "fichier_sha256": hashlib.sha256(cp.read_bytes()).hexdigest(),
                           "empreinte_canonique": rc.empreinte_config(config), "cles": len(config)}
assert verifier(config["chemin_prereg_parent"]) == config["prereg_parent_sha256"]
pieces = {}
for k_chemin, k_sha in (("chemin_textes", "textes_sha256"), ("chemin_scores", "scores_sha256"),
                        ("chemin_sondes_legeres", "sondes_legeres_sha256"), ("chemin_taches", "taches_sha256"),
                        ("chemin_consignes", "consignes_sha256"), ("chemin_fiches", "fiches_sha256"),
                        ("chemin_prereg_parent", "prereg_parent_sha256"),
                        ("chemin_table_tokenisation", "table_tokenisation_sha256")):
    sha = verifier(config[k_chemin])                     # sceau compagnon conforme
    assert sha == config[k_sha], (k_chemin, sha[:12])
    pieces[config[k_chemin]] = sha
sortie["pieces_verifiees_par_sceau_et_configuration"] = pieces

# ---- chargements du module (identité sans les scores)
identite = rg.charger_identite_sans_scores(config["chemin_scores"], config["scores_sha256"])
sha_id = empreinte_identite(identite)
assert sha_id == config["identite_sha256"]
lignes = charger_textes_alignes(config["chemin_textes"], identite, config["textes_sha256"])
table = rc.charger_table(config["chemin_table_tokenisation"], config["table_tokenisation_sha256"])
for k in ("textes_sha256", "fiches_sha256", "scores_sha256"):
    assert table.get(k) == config[k], k
taches = {t["identifiant"]: t for t in charger_taches(config["chemin_taches"])}
consignes = charger_consignes(config["chemin_consignes"], config["consignes_sha256"])
guide = charger_invite("H1-classification")
tok = AutoTokenizer.from_pretrained(str(TOK))
fmt = FormatChat(tok, variables=config["agent"]["variables_gabarit"])
# fins : celles de la configuration de génération de Llama 3.1 8B Instruct à la révision citée (128001, 128008, 128009)
# plus la fin du tokeniseur et la clôture du gabarit, comme `charger_modele_et_format` ; comparées à la table
fmt.fins = {128001, 128008, 128009, int(tok.eos_token_id)} | {fmt._pieces(("x", "y"))["cloture"][0]}
assert sorted(fmt.fins) == sorted(int(x) for x in table["fins_du_format"]), sorted(fmt.fins)
T = int(config["T"])
n = len(lignes)
par_episode = {}
for i, x in enumerate(lignes):
    par_episode.setdefault(x["episode"], []).append(i)
for e, rs in par_episode.items():
    assert len(rs) == T and rs == list(range(rs[0], rs[0] + T)), e
jetons = [int(x) for x in identite["jetons"]]
jetons_notes = [int(x) for x in identite["jetons_notes"]]
fiches = v1.charger_fiches(config["chemin_fiches"], config["fiches_sha256"])

# ---- revérification de toute la table au chargement (fonction de l'instance)
t1 = time.perf_counter()
n_verif = rc.verifier_table_au_chargement(table, fmt, lignes, par_episode, jetons, jetons_notes, fiches, taches,
                                          consignes, guide, T)
sortie["table"] = {"chemin": config["chemin_table_tokenisation"], "sha256": verifier(config["chemin_table_tokenisation"]),
                   "version": table["version"], "entrees": len(table["episodes"]), "comptes": table["comptes"],
                   "corrections_verifiees_au_chargement": n_verif,
                   "duree_verification_s": round(time.perf_counter() - t1, 1)}

# ---- chemin de `_executer` jusqu'à la carte (copie ligne à ligne)
conforme = np.zeros(n, dtype=bool)
contexte_conforme = np.zeros(n, dtype=bool)
recs, envs = {}, {}
for e, rs in par_episode.items():
    x0 = lignes[rs[0]]
    envs[e] = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
    recs[e] = v1.reconstruire_episode(fmt, envs[e], T, [lignes[r] for r in rs], [jetons[r] for r in rs],
                                      [jetons_notes[r] for r in rs])
    tous = True
    for r, a in zip(rs, recs[e]["actions"]):
        conforme[r] = a["conforme"]
        tous = tous and a["conforme"]
        contexte_conforme[r] = tous
traj = np.zeros(n, dtype=bool)
for e, rs in par_episode.items():
    traj[rs] = v1.empreinte_trajectoire(v1.episode_harnais(e, T, recs[e])) == fiches[e]["trajectoire"]
base = int(traj.sum()) // T
signales = [e for e, rs in par_episode.items() if conforme[rs].all() and not traj[rs].all()]
corrections, non_resolus = classer_episodes(signales, table, int(config["seuil_non_conformes"]))
octets = table_des_octets(fmt.tok)[0] if any(c.get("paires") for c in corrections.values()) else None
for e, ent in corrections.items():
    rs = par_episode[e]
    rec = rc.appliquer_entree(fmt, envs[e], T, [lignes[r] for r in rs], [jetons[r] for r in rs],
                              [jetons_notes[r] for r in rs], ent, octets)
    assert v1.empreinte_trajectoire(v1.episode_harnais(e, T, rec)) == fiches[e]["trajectoire"], e
    traj[rs] = True
    for r, a in zip(rs, rec["actions"]):
        conforme[r] = a["conforme"]
        contexte_conforme[r] = True
non_resolu = np.zeros(n, dtype=bool)
for e in non_resolus:
    non_resolu[par_episode[e]] = True
contexte_conforme &= ~non_resolu
par_table = {x["episode"]: x["methode"] for x in table["episodes"]}
methodes = {e: rc.methode_resolution(par_table.get(e)) for e in par_episode}
notees = np.asarray(jetons_notes) > 0
eligibles = traj & notees
cond = np.asarray(identite["condition"])
sortie["reconstruction"] = {
    "episodes": len(par_episode), "actions": n,
    "episodes_conformes_longueur": sum(1 for rs in par_episode.values() if conforme[rs].all()),
    "trajectoires_identiques_base": base, "signales": len(signales),
    "corrections_par_methode": {m: sum(1 for c in corrections.values() if c["methode"] == m) for m in rc.CORRIGEES},
    "par_methode_resolution": {m: sum(1 for x in methodes.values() if x == m) for m in rc.METHODES_RESOLUTION},
    "episodes_non_resolus": non_resolus, "actions_non_resolues": int(non_resolu.sum()),
    "trajectoires_identiques": int(traj.sum()) // T,
    "conformes_longueur": int(conforme.sum()), "contextes_conformes": int(contexte_conforme.sum()),
    "trajectoire_identique_actions": int(traj.sum()),
    "prefixes_contexte_conforme_sans_empreinte": int((contexte_conforme & ~traj).sum()),
    "notees_jetons_notes_positifs": int(notees.sum()),
    "eligibles_echantillon_fidelite": int(eligibles.sum()),
    "p_r5_borne_haute": {"actions": int((notees & conforme).sum()),
                         "part": round(float((notees & conforme).sum() / notees.sum()), 4)},
    "p_r5_scenario_bas_contexte_exact": {"actions": int((notees & contexte_conforme).sum()),
                                         "part": round(float((notees & contexte_conforme).sum() / notees.sum()), 4)},
    "repli_trajectoires_identiques": {"actions": int((notees & traj).sum()),
                                      "part": round(float((notees & traj).sum() / notees.sum()), 4)},
}
sortie["par_condition"] = {c: {"actions": int((cond == c).sum()), "notees": int((notees & (cond == c)).sum()),
                               "conformes_longueur": int((notees & conforme & (cond == c)).sum()),
                               "contexte_exact": int((notees & contexte_conforme & (cond == c)).sum()),
                               "trajectoire_identique": int((notees & traj & (cond == c)).sum()),
                               "eligibles_fidelite": int((eligibles & (cond == c)).sum())}
                           for c in sorted(set(cond.tolist()))}
# ---- corrections sous la consigne fausse du contrôle négatif (copie de `rejeu_activations_v3.controle_negatif`, sans
# modèle) : chaque épisode corrigé reconstruit sous la consigne fausse avec ses identifiants corrigés, sans garde levée,
# mêmes identifiants d'actions que sous la vraie consigne, empreinte différente de celle de P3 (le contexte est bien faux)
faux_ok = {}
for e, ent in corrections.items():
    rs = par_episode[e]
    x0 = lignes[rs[0]]
    L, J, JN = [lignes[r] for r in rs], [jetons[r] for r in rs], [jetons_notes[r] for r in rs]
    rv = rc.appliquer_entree(fmt, envs[e], T, L, J, JN, ent, octets)
    nom_faux = "saboteur" if x0["condition"] == "honnete" else "honnete"
    env_faux = environnement(nom_faux, tache_de(taches[x0["tache"]]), T, guide, consignes)
    rf = rc.appliquer_entree(fmt, env_faux, T, L, J, JN, ent, octets)
    memes = all([int(i) for i in a["nv"]] == [int(i) for i in b["nv"]] for a, b in zip(rv["actions"], rf["actions"]))
    autre = v1.empreinte_trajectoire(v1.episode_harnais(e, T, rf)) != fiches[e]["trajectoire"]
    faux_ok[e] = {"methode": ent["methode"], "memes_identifiants": memes, "empreinte_differente": autre}
sortie["corrections_sous_consigne_fausse"] = {
    "episodes": len(faux_ok), "tous_conformes": all(x["memes_identifiants"] and x["empreinte_differente"]
                                                    for x in faux_ok.values()),
    "par_methode": {m: sum(1 for x in faux_ok.values() if x["methode"] == m and x["memes_identifiants"]
                           and x["empreinte_differente"]) for m in sorted({x["methode"] for x in faux_ok.values()})}}
sortie["duree_s"] = round(time.perf_counter() - t0, 1)
print(json.dumps(sortie, ensure_ascii=False, indent=1))
