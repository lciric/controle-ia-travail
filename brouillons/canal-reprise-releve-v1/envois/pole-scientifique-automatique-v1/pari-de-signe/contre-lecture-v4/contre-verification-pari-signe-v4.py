#!/usr/bin/env python3
"""Contre-lecture (R2) de « Le pari apparié borné — conception v4 » : vérifications sur processeur (v1).

Contre-lecteur : sous-agent neuf Opus 5.5, 27 octobre 2026. Exploratoire, rien de décisif, aucune dépense.
Mondes illustratifs (ceux de la batterie v3 et de la contre-lecture v3) ; mécanismes, pas prédiction de la banque réelle.

Sections (graines : SeedSequence(ENTROPIE, spawn_key=(code de section, indice de configuration)), R9) :
  A  règle en ligne et nuls PARTIELS : par génération m = 6 fiches (3 vraies, 20 points, 250 unités ; 3 nulles S1,
     250 unités) ; e-BH au niveau α_g contre e-Bonferroni au niveau α_g (chaque fiche seule au seuil m/α_g) ;
     taux cumulé « au moins une fiche nulle promue » et somme des proportions de fausses découvertes ; plus le
     contre-exemple analytique (e-valeurs à deux points) qui montre que e-BH ne borne pas ce taux par α_g.
  B  arrêt « à m/α » (verdict 1 de la v4, « inchangé ») contre arrêt à m/α_g, sous e-BH au niveau α_g :
     m = 3 (1 fiche vraie, 20 points, 100 unités ; 2 nulles S1) ; probabilité que la vraie soit promue.
  C  coût en unités de la règle α_g : unités pour une puissance 0,8 et 0,9 d'une fiche seule (m = 3) au seuil
     m/α (60), m/α_g (g = 1, 3, 10, 30) et m·G/α (répartition uniforme α/G, G = 10 et 30), à 20 et à 10 points.
  D  héritage contre redémarrage : 3 fiches nulles S1 par génération, 250 unités par génération, G = 10 et 30 ;
     (a) e-valeurs neuves à chaque génération, e-BH à α (règle de la v3) ; (b) idem avec α_g (règle de la v4) ;
     (c) héritage : chaque fiche garde son processus d'une génération à l'autre (produit sur parties disjointes),
     arrêté à m/α, e-BH à α relu à la fin de chaque génération. Plus le cas d'une fiche seule (m = 1).
  E  arithmétique du § 6 : plus petit écart commun promouvable sur 10 unités, richesse à 6 et 7 unités à v = 1,
     plus petit écart commun à 7 et 8 unités, profil hétérogène (9 unités à v = 1, 1 à v = 0).

Usage : python -I -B contre-verification-pari-signe-v4.py [--rep 2000]
"""

import argparse
import json
import math
import platform
import sys
import time

import numpy as np

LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])
ALPHA = 0.05
ENTROPIE = 2026102706
CODES = {"A": 1, "B": 2, "C": 3, "D": 4}


def gen(section, indice):
    return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(CODES[section], indice)))


def alpha_g(g):
    return ALPHA * 6.0 / (math.pi ** 2 * g * g)


def richesse(v):
    """v : (R, n) -> richesse mélangée sur Λ à chaque instant, (R, n)."""
    lw = np.cumsum(np.log1p(LAMBDAS[None, None, :] * v[:, :, None]), axis=1)
    return np.exp(lw).mean(axis=2)


def e_arretee(W, seuil):
    atteint = W >= seuil
    premier = np.where(atteint.any(axis=1), atteint.argmax(axis=1), W.shape[1] - 1)
    return W[np.arange(W.shape[0]), premier]


def ebh(E, niveau):
    R, m = E.shape
    ordre = np.argsort(-E, axis=1)
    Es = np.take_along_axis(E, ordre, axis=1)
    k = np.arange(1, m + 1)[None, :]
    ok = Es >= m / (niveau * k)
    kstar = np.where(ok.any(axis=1), m - np.argmax(ok[:, ::-1], axis=1), 0)
    rej_tri = k <= kstar[:, None]
    rej = np.zeros_like(rej_tri)
    np.put_along_axis(rej, ordre, rej_tri, axis=1)
    return rej


def monde_vrai(rng, R, n, ra=0.6, rb=0.4, m=10):
    return rng.binomial(m, ra, size=(R, n)) / m - rng.binomial(m, rb, size=(R, n)) / m


def monde_S1(rng, R, n):
    return np.where(rng.random((R, n)) < 0.9, 0.1, -0.9)


# ------------------------------------------------------------------------------------------------------------- A
def section_A(R):
    out = {}
    # contre-exemple analytique : m = 3, une fiche vraie (e infinie), deux nulles à e-valeurs à deux points
    # (valeur 1,5/a avec probabilité a/1,5, sinon 0 ; événements disjoints) : espérance 1 chacune.
    a = alpha_g(1)
    out["contre_exemple_analytique_m3"] = {
        "alpha_1": round(a, 6),
        "seuil_e-BH_pour_une_nulle_quand_k=2": round(3 / (2 * a), 3),
        "esperance_de_chaque_e-valeur_nulle": round((1.5 / a) * (a / 1.5), 6),
        "probabilite_au_moins_une_nulle_promue": round(2 * a / 1.5, 6),
        "rapport_a_alpha_1": round((2 * a / 1.5) / a, 4)}
    m, n = 6, 250
    for G in (10, 30):
        rng = gen("A", G)
        cumul_ebh = np.zeros(R, dtype=bool)
        cumul_bonf = np.zeros(R, dtype=bool)
        somme_fdp_ebh = np.zeros(R)
        g1 = {}
        for g in range(1, G + 1):
            ag = alpha_g(g)
            Ws = [richesse(monde_vrai(rng, R, n)) for _ in range(3)] + [richesse(monde_S1(rng, R, n)) for _ in range(3)]
            E = np.stack([e_arretee(W, m / ag) for W in Ws], axis=1)
            rej = ebh(E, ag)
            V = rej[:, 3:].sum(axis=1)
            Rn = rej.sum(axis=1)
            fdp = np.where(Rn > 0, V / np.maximum(Rn, 1), 0.0)
            bonf = E[:, 3:] >= m / ag
            cumul_ebh |= V > 0
            cumul_bonf |= bonf.any(axis=1)
            somme_fdp_ebh += fdp
            if g == 1:
                g1 = {"alpha_1": round(ag, 5), "vraies_promues_moyenne_e-BH": round(float(rej[:, :3].sum(axis=1).mean()), 3),
                      "P(au_moins_une_nulle_promue)_e-BH": round(float((V > 0).mean()), 5),
                      "P(au_moins_une_nulle_promue)_e-Bonferroni": round(float(bonf.any(axis=1).mean()), 5)}
        out[f"nuls_partiels_m6_3vraies_3nulles_S1_n250_G{G}"] = {
            "repetitions": R, "generation_1": g1, "somme_alpha_g": round(sum(alpha_g(g) for g in range(1, G + 1)), 5),
            "taux_cumule_au_moins_une_nulle_promue_e-BH_alpha_g": round(float(cumul_ebh.mean()), 5),
            "taux_cumule_au_moins_une_nulle_promue_e-Bonferroni_alpha_g": round(float(cumul_bonf.mean()), 5),
            "somme_des_FDR_par_generation_e-BH_alpha_g": round(float(somme_fdp_ebh.mean()), 5)}
    return out


# ------------------------------------------------------------------------------------------------------------- B
def section_B(R):
    out = {}
    m, n = 3, 100
    for i, g in enumerate((1, 2, 3, 10)):
        rng = gen("B", i)
        ag = alpha_g(g)
        Ws = [richesse(monde_vrai(rng, R, n))] + [richesse(monde_S1(rng, R, n)) for _ in range(2)]
        res = {}
        for cas, seuil_arret in (("arret_a_m_sur_alpha_(lettre_du_verdict_1)", m / ALPHA), ("arret_a_m_sur_alpha_g", m / ag)):
            E = np.stack([e_arretee(W, seuil_arret) for W in Ws], axis=1)
            rej = ebh(E, ag)
            res[cas] = round(float(rej[:, 0].mean()), 4)
        out[f"g{g}"] = {"repetitions": R, "alpha_g": round(ag, 6), "seuil_e-BH_k1": round(m / ag, 1),
                        "P(vraie_promue)": res}
    return out


# ------------------------------------------------------------------------------------------------------------- C
def section_C(R):
    out = {}
    m = 3
    seuils = {"m/alpha (60, sans regle en ligne)": m / ALPHA}
    for g in (1, 3, 10, 30):
        seuils[f"m/alpha_g, g={g}"] = m / alpha_g(g)
    for G in (10, 30):
        seuils[f"m*G/alpha, uniforme G={G}"] = m * G / ALPHA
    for i, (nom, ra, rb, nmax) in enumerate((("20_points_(0.6_contre_0.4)", 0.6, 0.4, 260),
                                              ("10_points_(0.5_contre_0.4)", 0.5, 0.4, 900))):
        rng = gen("C", i)
        W = richesse(monde_vrai(rng, R, nmax, ra, rb))
        d = {"repetitions": R, "unites_max": nmax}
        for snom, s in seuils.items():
            atteint = W >= s
            t = np.where(atteint.any(axis=1), atteint.argmax(axis=1) + 1, nmax + 10)
            ts = np.sort(t)
            n80 = int(ts[int(math.ceil(0.8 * R)) - 1])
            n90 = int(ts[int(math.ceil(0.9 * R)) - 1])
            d[snom] = {"seuil": round(s, 1), "unites_puissance_0.8": n80 if n80 <= nmax else f"> {nmax}",
                       "unites_puissance_0.9": n90 if n90 <= nmax else f"> {nmax}"}
        out[nom] = d
    return out


# ------------------------------------------------------------------------------------------------------------- D
def section_D(R):
    out = {}
    n = 250
    idx = 0
    for m in (1, 3):
        for G in (10, 30):
            rng = gen("D", idx)
            idx += 1
            # mêmes données pour les trois règles : (R, m, G*n)
            v = np.where(rng.random((R, m, G * n)) < 0.9, 0.1, -0.9)
            cumul_neuf = np.zeros(R, dtype=bool)
            cumul_neuf_ag = np.zeros(R, dtype=bool)
            for g in range(1, G + 1):
                seg = v[:, :, (g - 1) * n:g * n]
                Ws = [richesse(seg[:, i, :]) for i in range(m)]
                E = np.stack([e_arretee(W, m / ALPHA) for W in Ws], axis=1)
                cumul_neuf |= ebh(E, ALPHA).any(axis=1)
                ag = alpha_g(g)
                El = np.stack([e_arretee(W, m / ag) for W in Ws], axis=1)
                cumul_neuf_ag |= ebh(El, ag).any(axis=1)
            # héritage : processus continu sur les G parties, arrêté à m/α ; e-BH à α relu à la fin de chaque génération
            Wc = [richesse(v[:, i, :]) for i in range(m)]
            arr = []
            for W in Wc:
                atteint = W >= m / ALPHA
                premier = np.where(atteint.any(axis=1), atteint.argmax(axis=1), G * n)
                arr.append(premier)
            cumul_her = np.zeros(R, dtype=bool)
            for g in range(1, G + 1):
                fin = g * n - 1
                E = np.stack([W[np.arange(R), np.minimum(p, fin)] for W, p in zip(Wc, arr)], axis=1)
                cumul_her |= ebh(E, ALPHA).any(axis=1)
            out[f"m{m}_G{G}_n{n}_par_generation_nul_S1"] = {
                "repetitions": R,
                "a_neuf_par_generation_e-BH_alpha": round(float(cumul_neuf.mean()), 4),
                "b_neuf_par_generation_e-BH_alpha_g": round(float(cumul_neuf_ag.mean()), 4),
                "c_heritage_processus_continu_e-BH_alpha_relu_chaque_generation": round(float(cumul_her.mean()), 4)}
    return out


# ------------------------------------------------------------------------------------------------------------- E
def mel(v, n):
    return float(np.mean((1 + LAMBDAS * v) ** n))


def v_min(n, seuil=20.0):
    lo, hi = 0.0, 1.0
    if mel(hi, n) < seuil:
        return None
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if mel(mid, n) >= seuil:
            hi = mid
        else:
            lo = mid
    return round(hi, 4)


def section_E():
    return {"richesse_10_unites_v=0.6": round(mel(0.6, 10), 2),
            "plus_petit_ecart_commun_promouvable_10_unites": v_min(10),
            "richesse_6_unites_v=1": round(mel(1.0, 6), 2),
            "richesse_7_unites_v=1": round(mel(1.0, 7), 2),
            "plus_petit_ecart_commun_7_unites": v_min(7),
            "plus_petit_ecart_commun_8_unites": v_min(8),
            "profil_9_unites_v=1_et_1_unite_v=0": round(float(np.mean((1 + LAMBDAS) ** 9)), 2),
            "somme_alpha_g_g=1..30": round(sum(alpha_g(g) for g in range(1, 31)), 5),
            "alpha_g": {str(g): round(alpha_g(g), 7) for g in (1, 2, 3, 10, 30)}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rep", type=int, default=2000)
    args = ap.parse_args()
    t0 = time.time()
    sortie = {"manifeste": {"script": "contre-verification-pari-signe-v4.py", "entropie_SeedSequence": ENTROPIE,
                            "derivation": "SeedSequence(ENTROPIE, spawn_key=(code de section, indice de configuration))",
                            "codes_sections": CODES, "repetitions_de_base": args.rep, "python": sys.version.split()[0],
                            "numpy": np.__version__, "plateforme": platform.platform(),
                            "grille": LAMBDAS.tolist(), "alpha": ALPHA}}
    sortie["A_regle_en_ligne_nuls_partiels"] = section_A(args.rep)
    sortie["B_arret_m_sur_alpha_contre_m_sur_alpha_g"] = section_B(args.rep)
    sortie["C_cout_en_unites_de_alpha_g"] = section_C(args.rep)
    sortie["D_heritage_contre_redemarrage"] = section_D(args.rep)
    sortie["E_arithmetique_section_6"] = section_E()
    sortie["manifeste"]["duree_secondes"] = round(time.time() - t0, 1)
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
