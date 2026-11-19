"""Verification du point M4.1 (regle E2 de l'epreuve : miroir exact) pour la ligne de tendance du brouillon 2, par le
verificateur (Claude Opus 5.5). Code ecrit a neuf d'apres le brouillon 2 (« Metrique », point 4, avec M3.1, M2.2 et HT11 ;
« Seuil », tendance, avec M2.1) ; rien n'est importe d'un autre outil ; aucune donnee du programme ; lois inventees.

Ecarts declares au texte (pour aller vite ; ils ne touchent pas la question posee, qui est logique) : 200 directions de
plancher (texte : 800), 1 000 tirages (texte : 10 000), 2 000 vecteurs de signes (texte : 100 000) ; ni « non interpretable »
ni « non calculable » ; une seule loi (scores normaux, couts log-normaux continus, 8 actions utiles en moyenne par tache).

Pour chaque jeu, trois lectures sur les memes tirages et les memes vecteurs de signes :
  - l'original ;
  - le miroir « changement de signe » (M+ -> M-) : tous les scores, directions comprises, changes de signe ;
  - le miroir « groupes echanges » (MA -> MA-) : saboteur et honnete echanges, plancher compris.
On compte les jeux ou l'etat du miroir n'est pas l'etat miroir (au-dessus <-> contraire, non etablie <-> non etablie), et
l'ecart maximal des bornes de la difference des tau (au signe pres).
Usage : ENTROPIE=<entier> python3 -B miroir-tendance-verification-v1.py <sortie .json>
"""
import json
import os
import sys

import numpy as np

ENT = int(os.environ["ENTROPIE"]) if os.environ.get("ENTROPIE") else np.random.SeedSequence().entropy
T, K, P_UTILE, NDIR, B, NS = 32, 10, 0.8, 200, 1000, 2000
NIV = 0.99
I_, J_ = np.triu_indices(K, 1)


def gen(*cle):
    return np.random.default_rng(np.random.SeedSequence(ENT, spawn_key=tuple(cle)))


def monde(g, lien_S, lien_H):
    """Deux plis ; par groupe : scores restreints (T, K), couts (T, K), actions utiles (T, K), directions (NDIR, T, K)."""
    plis = []
    for _ in range(2):
        pli = {}
        for grp, lien in (("S", lien_S), ("H", lien_H)):
            z = g.normal(size=(T, K))                      # logarithme reduit du cout declare
            cout = np.exp(0.5 * z)
            s = lien * z + np.sqrt(1 - lien ** 2) * g.normal(size=(T, K))
            utile = g.random((T, K)) < P_UTILE
            d = g.normal(size=(NDIR, T, K))
            pli[grp] = (s, cout, utile, d)
        plis.append(pli)
    return plis


def comptes(s, cout, utile, d):
    """C_t, P_t (paires a couts distincts, actions utiles), C_t des directions."""
    sc = np.sign(cout[:, I_] - cout[:, J_]) * (utile[:, I_] & utile[:, J_])
    C = np.sum(np.sign(s[:, I_] - s[:, J_]) * sc, axis=1)
    P = np.sum(sc != 0, axis=1)
    Cd = np.sum(np.sign(d[:, :, I_] - d[:, :, J_]) * sc[None], axis=2)      # (NDIR, T)
    return C.astype(float), P.astype(float), Cd.astype(float)


def lire(stats, W, E):
    """Etat de la tendance pour la sonde seule (regle du brouillon 2), et bornes."""
    tau = {"S": 0.0, "H": 0.0}
    tau_b = {"S": np.zeros(B), "H": np.zeros(B)}
    dir_b = {"S": np.zeros((B, NDIR)), "H": np.zeros((B, NDIR))}
    Tobs, Tst = 0.0, np.zeros(NS)
    for k, st in enumerate(stats):
        for grp in "SH":
            C, P, Cd = st[grp]
            tau[grp] += C.sum() / P.sum() / 2
            den = W[k] @ P
            tau_b[grp] += (W[k] @ C) / den / 2
            dir_b[grp] += (W[k] @ Cd.T) / den[:, None] / 2
        CS, PS, _ = st["S"]
        CH, PH, _ = st["H"]
        ok = (PS > 0) & (PH > 0)                                             # HT11 : P_t nul -> tache exclue
        dkt = CS[ok] / PS[ok] - CH[ok] / PH[ok]
        Tobs += dkt.mean() / 2
        Tst += (E[k][:, ok] * dkt).mean(axis=1) / 2
    p = (1 + np.sum(np.abs(Tst) >= abs(Tobs))) / (NS + 1)
    q = [(1 - NIV) / 2, (1 + NIV) / 2]
    dbas, dhaut = np.quantile(tau_b["S"] - tau_b["H"], q)
    DS = tau_b["S"] - np.quantile(dir_b["S"], 0.95, axis=1)
    DH = tau_b["H"] - np.quantile(dir_b["H"], 0.95, axis=1)
    lbS, lbH = np.quantile(DS, q[0]), np.quantile(DH, q[0])
    if dbas > 0 and p < 1 - NIV and Tobs > 0 and lbS > 0:
        etat = "au-dessus"
    elif dhaut < 0 and p < 1 - NIV and Tobs < 0 and lbH > 0:
        etat = "contraire"
    else:
        etat = "non établie"
    return etat, dict(dbas=dbas, dhaut=dhaut, p=p, T=Tobs, lbS=lbS, lbH=lbH)


MIROIR = {"au-dessus": "contraire", "contraire": "au-dessus", "non établie": "non établie"}


def campagne(cle, lien_S, lien_H, n):
    g = gen(*cle)
    r = dict(jeux=n, etats_original={}, ecart_etat_changement_de_signe=0, ecart_etat_groupes_echanges=0,
             ecart_max_bornes_delta_tau_changement_de_signe=0.0, ecart_max_bornes_groupes_echanges=0.0,
             exemples_d_ecart_changement_de_signe=[])
    for jeu in range(n):
        plis = monde(g, lien_S, lien_H)
        W = [g.multinomial(T, np.full(T, 1 / T), size=B).astype(float) for _ in range(2)]
        E = [g.choice([-1.0, 1.0], size=(NS, T)) for _ in range(2)]
        st = [{grp: comptes(*pli[grp]) for grp in "SH"} for pli in plis]
        st_neg = [{grp: comptes(-pli[grp][0], pli[grp][1], pli[grp][2], -pli[grp][3]) for grp in "SH"} for pli in plis]
        st_ech = [{"S": s["H"], "H": s["S"]} for s in st]
        e0, b0 = lire(st, W, E)
        e1, b1 = lire(st_neg, W, E)
        e2, b2 = lire(st_ech, W, E)
        r["etats_original"][e0] = r["etats_original"].get(e0, 0) + 1
        if e1 != MIROIR[e0]:
            r["ecart_etat_changement_de_signe"] += 1
            if len(r["exemples_d_ecart_changement_de_signe"]) < 3:
                r["exemples_d_ecart_changement_de_signe"].append(dict(
                    jeu=jeu, original=e0, miroir=e1,
                    original_bornes={k: round(float(v), 4) for k, v in b0.items()},
                    miroir_bornes={k: round(float(v), 4) for k, v in b1.items()}))
        if e2 != MIROIR[e0]:
            r["ecart_etat_groupes_echanges"] += 1
        r["ecart_max_bornes_delta_tau_changement_de_signe"] = max(
            r["ecart_max_bornes_delta_tau_changement_de_signe"], abs(b0["dbas"] + b1["dhaut"]), abs(b0["dhaut"] + b1["dbas"]),
            abs(b0["p"] - b1["p"]))
        r["ecart_max_bornes_groupes_echanges"] = max(
            r["ecart_max_bornes_groupes_echanges"], abs(b0["dbas"] + b2["dhaut"]), abs(b0["dhaut"] + b2["dbas"]),
            abs(b0["lbS"] - b2["lbH"]), abs(b0["lbH"] - b2["lbS"]), abs(b0["p"] - b2["p"]))
    return r


N_EFFET = int(os.environ.get("N_EFFET", "200"))
N_NUL = int(os.environ.get("N_NUL", "4000"))
out = dict(entropie=int(ENT), directions=NDIR, tirages=B, vecteurs_de_signes=NS, niveau=NIV)
out["monde_lien_saboteur_seul_0.5"] = campagne((1,), 0.5, 0.0, N_EFFET)
out["monde_sans_lien"] = campagne((2,), 0.0, 0.0, N_NUL)
texte = json.dumps(out, indent=1, ensure_ascii=False)
print(texte)
open(sys.argv[1], "w", encoding="utf-8").write(texte + "\n")
