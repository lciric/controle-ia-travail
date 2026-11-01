"""Génère la grille brouillon 1 de la simulation d'essaim (règles de sélection écrites ici et au préenregistrement)."""
import json, math, sys
from controle_ia.simulation_essaim import calibrage as C

ALPHA, Q = 0.05, 0.1
PANNEAU = {"somme": "exact", "max": "exact", "comptage": "exact", "agent_moyenne": "exact", "agent_comptage": "exact",
           "pas_moyenne": "exact", "coelev_comptage": "exact", "coelev_somme3": "mc", "e_coelev_cal": "mc",
           "e_coelev_ville": "ville", "ed_coelev": "mc", "e_pas_ville": "ville"}
PANNEAU_HE3 = {k: v for k, v in PANNEAU.items() if v != "mc"}
CONFIGS = {"e5x40": (5, 40), "e10x20": (10, 20), "e20x20": (20, 20)}


def specs_C(K, T):
    mid = math.ceil(K / 2)
    s = C.seuils_exacts(K, T, Q, ALPHA)
    out = [
        {"nom": "A_rebrassage", "genre": "rebrassage_agents", "groupe": "agents"},
        {"nom": f"A_routage_un_m{T // 4}", "genre": "routage", "groupe": "agents", "m": T // 4, "k_dest": 1,
         "lecture_par_agent": "au_dessus"},
        {"nom": f"A_routage_un_m{T}", "genre": "routage", "groupe": "agents", "m": T, "k_dest": 1,
         "lecture_par_agent": "au_dessus"},
        {"nom": f"A_relais_m{T}", "genre": "routage", "groupe": "agents", "m": T, "k_dest": K,
         "lecture_par_agent": "en_dessous"},
        {"nom": "T_rebrassage", "genre": "rebrassage_temps", "groupe": "temps"},
    ]
    for m in (2, mid, K):
        lb = C.borne_synchro(K, T, m, Q, s["coelev_comptage"])
        dessus = (["coelev_comptage"] if lb >= ALPHA + 0.02 else []) + (["pas_moyenne", "coelev_somme3"] if m >= mid else [])
        sens_e = "en_dessous" if (m == K and K >= 10) else "au_plus"
        out.append({"nom": f"T_synchro_m{m}", "genre": "synchro", "groupe": "temps", "m": m, "r": 1,
                    "borne_coelev_comptage": round(lb, 6), "lecture_au_dessus": dessus,
                    "lecture_e": {"e_coelev_cal": sens_e, "ed_coelev": sens_e}})
    out.append({"nom": "I_rebrassage", "genre": "rebrassage_tout", "groupe": "tout"})
    return out


def specs_M(K, T):
    out = [{"nom": f"M_concentre_B{B}", "genre": "concentre", "B": B, "m": 1} for B in (3, 4, 5)]
    for B in (8, 12):
        for m in (2, math.ceil(K / 2), K):
            out.append({"nom": f"M_synchro_B{B}_m{m}", "genre": "synchro", "B": B, "m": m})
    for B in (8, 12):
        for m in (2, T // 2, T):
            out.append({"nom": f"M_temps_B{B}_m{m}", "genre": "temps", "B": B, "m": m})
    return out


grille = {
    "version": "essaim-grille-v1",
    "preenregistrement": "prereg/essaim-simulation-v1.md",
    "graine_racine": "entier des 128 premiers bits du sha256 du préenregistrement scellé (run_essaim.entropie_depuis_prereg)",
    "alpha": ALPHA,
    "q": Q,
    "fractions_lambda": [0.1, 0.25, 0.5, 0.75],
    "tailles": {"R": 20000, "R_cal": 100000, "R0": 100000, "equivalence": 200},
    "replication": {"facteur_R": 5},
    "lecture": {"gamma": 1e-5},
    "configs": {**{n: {"K": K, "T": T, "panneau": PANNEAU} for n, (K, T) in CONFIGS.items()},
                "e10x50": {"K": 10, "T": 50, "panneau": PANNEAU_HE3}},
    "C": {n: specs_C(K, T) for n, (K, T) in CONFIGS.items()},
    "M": {n: specs_M(K, T) for n, (K, T) in CONFIGS.items()},
    "HE3": {
        "configs": ["e10x20", "e10x50"],
        "lois": [{"nom": "iid", "loi": {"type": "iid", "marginale": "gauss"}},
                 {"nom": "tau0.1", "loi": {"type": "effet_episode", "tau": 0.1}},
                 {"nom": "tau0.2", "loi": {"type": "effet_episode", "tau": 0.2}},
                 {"nom": "c0.2", "loi": {"type": "equicorrelation", "c": 0.2}},
                 {"nom": "c0.4", "loi": {"type": "equicorrelation", "c": 0.4}}],
        "alarmes": ["somme", "max", "comptage", "agent_moyenne", "agent_comptage", "pas_moyenne", "coelev_comptage",
                    "e_coelev_ville", "e_pas_ville"],
        "conforme": {"K": 1000, "n_test": 400, "L": 50,
                     "statistiques": ["coelev_comptage", "e_coelev", "e_pas", "agent_moyenne"]},
        "lecture": {"depasse": {"tau0.1": ["e_pas_ville"], "tau0.2": ["e_coelev_ville", "e_pas_ville"],
                                "c0.2": ["e_pas_ville"], "c0.4": ["e_pas_ville"]}},
    },
    "HE6": {
        "configs": ["e10x20"],
        "lois": [{"nom": "c0.2", "loi": {"type": "equicorrelation", "c": 0.2}},
                 {"nom": "c0.4", "loi": {"type": "equicorrelation", "c": 0.4}}],
        "alarmes": ["somme", "max", "comptage", "agent_moyenne", "agent_comptage", "pas_moyenne", "coelev_comptage",
                    "coelev_somme3", "e_coelev", "ed_coelev"],
        "arrangements": [{"nom": "T_synchro_m5", "genre": "synchro", "groupe": "temps", "m": 5, "r": 1},
                         {"nom": "T_synchro_m10", "genre": "synchro", "groupe": "temps", "m": 10, "r": 1}],
        "lecture": {"c0.2": {"T_synchro_m10": {"coelev_comptage": "au_dessus", "pas_moyenne": "au_dessus"}},
                    "c0.4": {"T_synchro_m5": {"coelev_comptage": "en_dessous", "pas_moyenne": "en_dessous"},
                             "T_synchro_m10": {"coelev_comptage": "au_dessus", "pas_moyenne": "au_dessus"}}},
    },
}
chemin = sys.argv[1]
with open(chemin, "x", encoding="utf-8") as f:
    f.write(json.dumps(grille, indent=1, ensure_ascii=False) + "\n")
print("écrit", chemin)
for n in CONFIGS:
    for s in grille["C"][n]:
        if s["genre"] == "synchro":
            print(n, s["nom"], s["borne_coelev_comptage"], s["lecture_au_dessus"], s["lecture_e"])
