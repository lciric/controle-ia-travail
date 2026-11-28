import sys, time
sys.dont_write_bytecode = True
sys.path.insert(0, "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/module")
import instrument_p4_v1 as ip
import mesures_conception_p4_v1 as mc
from controle_ia.environnements.invites import charger_invite
t0 = time.time()
tok, emp = mc.charger_tokeniseur("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/tokeniseur")
fmt, controle = mc.format_de_l_agent(tok, ip.AGENT_P3, "reel")
eot = ip.jeton_de_fin(fmt, "reel")
print("format", controle["verifie"], "eot", eot, sorted(fmt.fins), round(time.time() - t0, 1))
taches = [{"identifiant": "synth-1", "questions": "Which synthetic routing rule is stable?",
           "classification": {"theory_experiment": "mostly_experiments", "data_type": "real_only", "domains": ["x"]}},
          {"identifiant": "synth-2", "questions": "How should a synthetic probe be calibrated?", "classification": None}]
def texte(k, j):
    return (f"ACTION: ADD\nTITLE: Synthetic proposal {k}-{j}.\nPROPOSAL: Compare two synthetic baselines on toy data.\n"
            f"CONTROLS: random probes\nCOST: {10 * j + 5}\nPREDICTION: small gain")
T = 10
actions = {t["identifiant"]: [{"pas": j, "texte": texte(k, j) if j != 3 else "Synthetic note without fields",
                               "fin": j != 7, "jetons_notes": 0} for j in range(T)] for k, t in enumerate(taches)}
for t in taches:
    for a in actions[t["identifiant"]]:
        a["jetons_notes"] = len(ip._ids(tok, a["texte"]))
guide = charger_invite("H1-classification")
r1 = mc.mc1(fmt, taches, guide, T, actions, eot)
print("MC-1", r1["B_nom"], r1["Bprime_nom"], "seules", {k: r1["seules"][k] for k in ("a dishonest", "an honest", "a tall", "an urban")})
print("valeurs dans le gabarit", {k: r1["valeurs_dans_le_gabarit"][k] for k in ("a dishonest", "an honest", "a tall", "an urban")})
print("insertions non pures", sum(r1["insertions_non_pures"].values()))
ids = [ip.ids_de_l_action(fmt, a["texte"], a["fin"], eot) for a in actions["synth-1"]]
ep, infos = ip.reconstruire_episode(fmt, ip.environnement_du_bras(taches[0], T, guide), "x", ids, [a["texte"] for a in actions["synth-1"]], T)
traj = {"synth-1": ip.empreinte_trajectoire(ep), "synth-2": "0" * 64}
r2 = mc.mc2(fmt, taches, guide, T, actions, traj, eot)
r3 = mc.mc3(fmt, taches, actions)
print("MC-2", r2["egaux"], "/", r2["episodes"], "MC-3", r3["echecs_longueur"], r3["fin_presente"], r3["actions"])
pos = ip.debut_message_utilisateur(fmt, ip.environnement_du_bras(taches[0], T, guide).consigne_privee(0), infos[0]["observation"])
print("position du message de l'utilisateur", pos, "espace", ip._ids(tok, " "), "duree", round(time.time() - t0, 1))
