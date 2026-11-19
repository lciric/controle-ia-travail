"""Complement de planification : critere double de la ligne d'interaction (intervalle percentile ET test par changement de
signe au niveau des taches). Lois inventees, memes mondes que le bloc 2 de planification-premiere-lecture-v1.py (fonctions
recopiees, non importees : l'autre script joue tout a l'import). Processeur seul ; aucune donnee du programme.
Graines par numpy.random.SeedSequence (R9).
"""
from __future__ import annotations

import json
import math
import os
import sys
from statistics import NormalDist

import numpy as np

ND = NormalDist()
RACINE = np.random.SeedSequence(2026111922)
T_PLI, K_ACT, N_TIRAGES, N_SIGNES = 32, 10, 2000, 4000
CASES = ("OS", "A", "J", "OH")


def gen(*cle):
    return np.random.default_rng(np.random.SeedSequence(entropy=RACINE.entropy, spawn_key=tuple(int(c) for c in cle)))


def monde_pli(g, part_texte, sd_dep_episode, interaction, sd_dep_tache=0.2, queue_lourde=False):
    vt, ve, va = 0.25 * part_texte, 0.25 * part_texte, 0.50 * part_texte
    vbruit = max(1.0 - part_texte - sd_dep_episode ** 2 / 2 - sd_dep_tache ** 2 / 2, 0.02)

    def tir(forme, var):
        if queue_lourde:                      # loi de Student a 3 degres, ramenee a la variance demandee
            return g.standard_t(3, forme) * math.sqrt(var / 3.0)
        return g.normal(0.0, math.sqrt(var), forme)

    u, dt = tir((T_PLI, 1), vt), tir((T_PLI, 1), sd_dep_tache ** 2)
    s = {}
    for X, m in (("S", 0.5), ("H", 0.0)):
        f = u + tir((T_PLI, 1), ve) + tir((T_PLI, K_ACT), va) + m
        de = tir((T_PLI, 1), sd_dep_episode ** 2)
        nu = f + tir((T_PLI, K_ACT), vbruit)
        ad = f + 3.0 + dt + de + (interaction if X == "S" else 0.0) + tir((T_PLI, K_ACT), vbruit)
        if X == "S":
            s["OS"], s["J"] = ad, nu
        else:
            s["A"], s["OH"] = ad, nu
    return s


def lire(g, plis, niveau=0.99):
    """Rend (etat par l'intervalle, etat par le changement de signe, etat double)."""
    ponct, tir, T_obs, T_perm = 0.0, np.zeros(N_TIRAGES), 0.0, np.zeros(N_SIGNES)
    for s in plis:
        n = np.full(T_PLI, float(K_ACT))
        st = {c: (n, s[c].sum(1), (s[c] ** 2).sum(1)) for c in CASES}

        def inter(W):
            m, v = {}, {}
            for c in CASES:
                N, S1, S2 = W @ st[c][0], W @ st[c][1], W @ st[c][2]
                m[c] = S1 / N
                v[c] = (S2 - N * m[c] ** 2) / (N - 1.0)
            sig = np.sqrt((v["OS"] + v["A"] + v["J"] + v["OH"]) / 4.0)
            return ((m["OS"] - m["J"]) - (m["A"] - m["OH"])) / sig, sig

        i0, sig0 = inter(np.ones((1, T_PLI)))
        ponct += float(i0[0]) / 2
        W = g.multinomial(T_PLI, np.full(T_PLI, 1.0 / T_PLI), size=N_TIRAGES).astype(float)
        tir += inter(W)[0] / 2
        D = (s["OS"] - s["J"]).mean(1) - (s["A"] - s["OH"]).mean(1)          # difference par tache
        T_obs += float(D.mean() / sig0[0]) / 2
        eps = g.choice([-1.0, 1.0], size=(N_SIGNES, T_PLI))
        T_perm += (eps @ D) / T_PLI / sig0[0] / 2
    bas, haut = np.quantile(tir, [(1 - niveau) / 2, (1 + niveau) / 2])
    e_int = 1 if bas > 0 else (-1 if haut < 0 else 0)
    p = (1 + int((np.abs(T_perm) >= abs(T_obs)).sum())) / (1 + N_SIGNES)
    e_sig = (1 if T_obs > 0 else -1) if p < 1 - niveau else 0
    e_double = e_int if (e_int != 0 and e_sig == e_int) else 0
    return ponct, e_int, e_sig, e_double


sortie = {"racine_entropie": int(RACINE.entropy), "tirages": N_TIRAGES, "changements_de_signe": N_SIGNES}
z99, z80 = ND.inv_cdf(0.995), ND.inv_cdf(0.80)
MONDES = [(0.5, 0.3, False), (0.5, 0.5, False), (0.8, 0.1, False), (0.5, 0.3, True), (0.8, 0.5, True)]
for i, (pt, sd, lourde) in enumerate(MONDES):
    g = gen(1, i)
    R = int(os.environ.get("REP_NUL", 4000))      # essai de fumee : REP_NUL et REP_ALT reduits, sortie non citable
    res = np.array([lire(g, [monde_pli(g, pt, sd, 0.0, queue_lourde=lourde) for _ in range(2)]) for _ in range(R)])
    s_vrai = float(res[:, 0].std())
    ligne = {"ecart_type_vrai_de_l_interaction": round(s_vrai, 4)}
    for nom, col in (("intervalle_seul", 1), ("changement_de_signe_seul", 2), ("critere_double", 3)):
        ligne[f"fausse_lecture_{nom}_au_dessus"] = round(float((res[:, col] == 1).mean()), 4)
        ligne[f"fausse_lecture_{nom}_contraire"] = round(float((res[:, col] == -1).mean()), 4)
    for j, mult in enumerate((3.418, 4.0, 5.0)):
        g2 = gen(2, i, j)
        alt = np.array([lire(g2, [monde_pli(g2, pt, sd, mult * s_vrai, queue_lourde=lourde) for _ in range(2)])
                        for _ in range(int(os.environ.get("REP_ALT", 800)))])
        ligne[f"puissance_a_{mult}_ecarts_types_d_estimation_interaction_{mult * s_vrai:.3f}"] = {
            "intervalle_seul": round(float((alt[:, 1] == 1).mean()), 3),
            "changement_de_signe_seul": round(float((alt[:, 2] == 1).mean()), 3),
            "critere_double": round(float((alt[:, 3] == 1).mean()), 3)}
    sortie[f"part_du_texte_{pt}_ecart_type_d_episode_{sd}_{'queues_lourdes' if lourde else 'lois_normales'}"] = ligne

texte = json.dumps(sortie, indent=1, ensure_ascii=False)
print(texte)
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write(texte + "\n")
