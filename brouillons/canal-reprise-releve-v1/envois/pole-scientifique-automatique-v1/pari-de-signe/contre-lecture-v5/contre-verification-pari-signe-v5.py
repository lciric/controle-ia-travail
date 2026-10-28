#!/usr/bin/env python3
"""Contre-lecture (R2) de « Le pari apparié borné — conception v5 » : vérifications sur processeur (v1).

Contre-lecteur : sous-agent neuf Fable 5.1, 27 octobre 2026. Exploratoire, rien de décisif, aucune dépense.
Mondes illustratifs ; mécanismes, pas prédiction de la banque réelle.

Sections (graines : SeedSequence(ENTROPIE, spawn_key=(code de section, indice)), R9) :
  H  héritage et fiches nouvelles dans une même course, sous nul complet, quatre lectures de la règle de la v5 :
       « cohortes »  (lecture valide) : chaque fiche reçoit à son entrée un budget b_i = α_c/m_c (α_c niveau de sa
                      génération d'entrée, m_c taille de sa famille d'entrée), gardé à vie ; à chaque fin de génération,
                      règle e-BH pondérée sur toutes les fiches entrées (valeurs gelées pour les fiches abandonnées) ;
       « seule »     (lecture naïve de « garde le niveau de son entrée ») : une fiche relancée est lue seule au seuil
                      1/α_c dès la génération suivante ;
       « mixte-α1 »  (famille mixte au niveau d'entrée des relancées) : à chaque génération, fiches relancées et
                      nouvelles forment une famille e-BH ordinaire au niveau α_1 ;
       « mixte-αg »  (famille mixte au niveau courant α_g) : idem au niveau α_g (les relancées dépensent α_g : valide,
                      contraire à D-S25).
     Deux mondes : A' martingale ×1,5 / ×0,5 à pile ou face (200 puis 20 pas par génération ; bornes de Ville
     approchées) ; B monde S1 de la batterie (90 % à +0,1, 10 % à −0,9), pari « parts », 250 unités par génération.
     Plus un cas sous nuls partiels (lecture « cohortes ») : taux de fausses découvertes de l'union des promotions.
  P  D-S27 : unité au-delà de m_max : estimande du sous-échantillon scellé et du plafond min(m_t, m_max)/m_max,
     contre l'estimande « rappel par épisode » de N-054 ; promotion sous un nul par épisode exact.
  T  D-S26 : témoin faux promu quand la strate porte k promotions vraies : fréquence de suspension ; taux de fausses
     découvertes de l'ensemble survivant après suspension.

Usage : python -I -B contre-verification-pari-signe-v5.py [--rep 2000]
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
ENTROPIE = 2026102707
CODES = {"H": 1, "P": 2, "T": 3}


def gen(section, indice):
    return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(CODES[section], indice)))


def alpha_g(g):
    return ALPHA * 6.0 / (math.pi ** 2 * g * g)


def richesse_chemin(v):
    """v : (R, n) -> richesse mélangée sur Λ à chaque instant (R, n)."""
    lw = np.cumsum(np.log1p(LAMBDAS[None, None, :] * v[:, :, None]), axis=1)
    return np.exp(lw).mean(axis=2)


def chemin_martingale_pile_ou_face(rng, R, n, eps=0.5):
    """Martingale positive : ×(1+eps) ou ×(1−eps) à pile ou face (espérance 1 à chaque pas)."""
    f = np.where(rng.random((R, n)) < 0.5, 1.0 + eps, 1.0 - eps)
    return np.exp(np.cumsum(np.log(f), axis=1))


def chemin_S1(rng, R, n):
    return richesse_chemin(np.where(rng.random((R, n)) < 0.9, 0.1, -0.9))


def chemin_vrai(rng, R, n, ra=0.6, rb=0.4, m=10):
    return richesse_chemin(rng.binomial(m, ra, size=(R, n)) / m - rng.binomial(m, rb, size=(R, n)) / m)


def ebh_pondere(E, b):
    """E : (R, M) e-valeurs ; b : (M,) budgets. Rejet de i si E_i ≥ 1/(b_i k*), k* = max{k : #{i : E_i ≥ 1/(b_i k)} ≥ k}."""
    R, M = E.shape
    kstar = np.zeros(R, dtype=int)
    for k in range(M, 0, -1):
        cnt = (E >= 1.0 / (b[None, :] * k)).sum(axis=1)
        ok = (cnt >= k) & (kstar == 0)
        kstar[ok] = k
    rej = np.zeros((R, M), dtype=bool)
    pos = kstar > 0
    rej[pos] = E[pos] >= 1.0 / (b[None, :] * kstar[pos, None])
    return rej


# ------------------------------------------------------------------------------------------------------------- H
def course(rng, monde, R, n, G, m1, mnew, lecture, vrais_cohorte=0, vrais_new=0):
    """Une course de G générations. Cohorte 1 : m1 fiches entrées à g = 1, relancées à chaque génération (processus
    continu). À chaque génération g ≥ 2 : mnew fiches nouvelles (une génération, puis abandonnées).
    Retourne (promue_union (R, M), est_nulle (M,))."""
    a1 = alpha_g(1)
    # chemins de la cohorte 1 sur G*n pas (sans arrêt : l'arrêt se lit sur le maximum courant)
    chem1 = []
    nul1 = []
    for i in range(m1):
        vrai = i < vrais_cohorte
        nul1.append(not vrai)
        if monde == "A":
            chem1.append(chemin_martingale_pile_ou_face(rng, R, G * n))
        else:
            chem1.append(chemin_vrai(rng, R, G * n) if vrai else chemin_S1(rng, R, G * n))
    # fiches nouvelles par génération
    chem_new = {}
    nul_new = {}
    for g in range(2, G + 1):
        chem_new[g] = []
        nul_new[g] = []
        for j in range(mnew):
            vrai = j < vrais_new
            nul_new[g].append(not vrai)
            if monde == "A":
                chem_new[g].append(chemin_martingale_pile_ou_face(rng, R, n))
            else:
                chem_new[g].append(chemin_vrai(rng, R, n) if vrai else chemin_S1(rng, R, n))
    M = m1 + (G - 1) * mnew
    est_nulle = np.array(nul1 + sum((nul_new[g] for g in range(2, G + 1)), []))
    promue = np.zeros((R, M), dtype=bool)

    def maxcour(ch, fin):
        return ch[:, :fin].max(axis=1)

    for g in range(1, G + 1):
        fin = g * n
        ag = alpha_g(g)
        if lecture == "cohortes":
            # toutes les fiches entrées, budgets d'entrée ; e-valeur = max courant si ≥ 1/b (arrêt), sinon valeur de fin
            E_list, b_list = [], []
            for i in range(m1):
                b = a1 / m1
                mx = maxcour(chem1[i], fin)
                E_list.append(np.where(mx >= 1 / b, mx, chem1[i][:, fin - 1]))
                b_list.append(b)
            for gg in range(2, g + 1):
                for j in range(mnew):
                    b = alpha_g(gg) / mnew
                    ch = chem_new[gg][j]
                    mx = ch.max(axis=1)
                    E_list.append(np.where(mx >= 1 / b, mx, ch[:, -1]))
                    b_list.append(b)
            E = np.stack(E_list, axis=1)
            rej = ebh_pondere(E, np.array(b_list))
            promue[:, :E.shape[1]] |= rej
        elif lecture == "seule":
            if g == 1:
                E = np.stack([np.where(maxcour(chem1[i], fin) >= m1 / a1, maxcour(chem1[i], fin), chem1[i][:, fin - 1])
                              for i in range(m1)], axis=1)
                promue[:, :m1] |= ebh_pondere(E, np.full(m1, a1 / m1))
            else:
                for i in range(m1):  # relancée lue seule au seuil 1/α_1 (lecture continue sur la génération g)
                    promue[:, i] |= chem1[i][:, (g - 1) * n:fin].max(axis=1) >= 1 / a1
                E = np.stack([np.where(ch.max(axis=1) >= mnew / ag, ch.max(axis=1), ch[:, -1]) for ch in chem_new[g]], axis=1)
                deb = m1 + (g - 2) * mnew
                promue[:, deb:deb + mnew] |= ebh_pondere(E, np.full(mnew, ag / mnew))
        elif lecture in ("mixte-a1", "mixte-ag"):
            niveau = a1 if lecture == "mixte-a1" else ag
            if g == 1:
                mm = m1
                E = np.stack([np.where(maxcour(chem1[i], fin) >= mm / a1, maxcour(chem1[i], fin), chem1[i][:, fin - 1])
                              for i in range(m1)], axis=1)
                promue[:, :m1] |= ebh_pondere(E, np.full(m1, a1 / m1))
            else:
                mm = m1 + mnew
                seuil1 = mm / niveau
                E_list = []
                for i in range(m1):
                    mx = chem1[i][:, (g - 1) * n:fin].max(axis=1)
                    E_list.append(np.where(mx >= seuil1, mx, chem1[i][:, fin - 1]))
                for ch in chem_new[g]:
                    mx = ch.max(axis=1)
                    E_list.append(np.where(mx >= seuil1, mx, ch[:, -1]))
                E = np.stack(E_list, axis=1)
                rej = ebh_pondere(E, np.full(mm, niveau / mm))
                promue[:, :m1] |= rej[:, :m1]
                deb = m1 + (g - 2) * mnew
                promue[:, deb:deb + mnew] |= rej[:, m1:]
        else:
            raise ValueError(lecture)
    return promue, est_nulle


def section_H(R):
    out = {}
    G, m1, mnew = 10, 4, 3
    somme_budgets = alpha_g(1) + sum(alpha_g(g) for g in range(2, G + 1))
    out["parametres"] = {"G": G, "m1_cohorte_1": m1, "nouvelles_par_generation": mnew, "alpha": ALPHA,
                         "alpha_1": round(alpha_g(1), 5), "somme_alpha_g_1..G": round(somme_budgets, 5),
                         "seuil_entree_cohorte_1_m1_sur_alpha_1": round(m1 / alpha_g(1), 1),
                         "seuil_naif_1_sur_alpha_1": round(1 / alpha_g(1), 1),
                         "seuil_mixte_a1_k1": round((m1 + mnew) / alpha_g(1), 1),
                         "seuil_nouvelles_g2_k1": round(mnew / alpha_g(2), 1), "seuil_nouvelles_g10_k1": round(mnew / alpha_g(10), 1)}
    for idx, (monde, n) in enumerate((("A", 200), ("S1", 250), ("A", 20))):
        res = {}
        for lecture in ("cohortes", "seule", "mixte-a1", "mixte-ag"):
            rng = gen("H", 10 * idx + ["cohortes", "seule", "mixte-a1", "mixte-ag"].index(lecture))
            promue, est_nulle = course(rng, monde, R, n, G, m1, mnew, lecture)
            res[lecture] = {
                "P(au_moins_une_fausse_promotion_sur_la_course)": round(float(promue.any(axis=1).mean()), 4),
                "P(au_moins_une_fausse_promotion_cohorte_1)": round(float(promue[:, :m1].any(axis=1).mean()), 4),
                "P(au_moins_une_fausse_promotion_nouvelles)": round(float(promue[:, m1:].any(axis=1).mean()), 4),
                "nombre_moyen_de_fausses_promotions": round(float(promue.sum(axis=1).mean()), 4)}
        out[f"nul_complet_monde_{monde}_n{n}_par_generation"] = {"repetitions": R, "lectures": res}
    # nuls partiels, lecture « cohortes » : union des promotions, taux de fausses découvertes
    rng = gen("H", 50)
    promue, est_nulle = course(rng, "S1", R, 250, G, m1, mnew, "cohortes", vrais_cohorte=3, vrais_new=1)
    V = promue[:, est_nulle].sum(axis=1)
    Rt = promue.sum(axis=1)
    bnul = alpha_g(1) / m1 * (m1 - 3) + sum(alpha_g(g) / mnew * (mnew - 1) for g in range(2, G + 1))
    out["nuls_partiels_monde_S1_lecture_cohortes"] = {
        "repetitions": R, "cohorte_1": "3 vraies (20 points) + 1 nulle S1", "nouvelles": "1 vraie + 2 nulles par generation",
        "borne_somme_des_budgets_des_nulles": round(bnul, 5),
        "taux_de_fausses_decouvertes_de_l_union": round(float(np.where(Rt > 0, V / np.maximum(Rt, 1), 0.0).mean()), 5),
        "P(au_moins_une_fausse_promotion)": round(float((V > 0).mean()), 4),
        "vraies_promues_moyenne_sur_12": round(float(promue[:, ~est_nulle].sum(axis=1).mean()), 3)}
    return out


# ------------------------------------------------------------------------------------------------------------- P
def section_P(R):
    """Deux types d'unités, moitié-moitié : longues (m = 100 épisodes, p_blanc = 0,32, p_noir = 0,40 : v = −0,08) ;
    courtes (m = 10, p_blanc = 0,9, p_noir = 0,1 : v = +0,8). Rappel par épisode : E[m·v] = 0,5·(−8) + 0,5·(+8) = 0 :
    nul exact de N-054 (frontière). Plafond déclaré m_max = 20."""
    out = {}
    n = 250
    m_max = 20
    esp = {"E[m_t v_t]_rappel_par_episode_N-054": 0.5 * 100 * (-0.08) + 0.5 * 10 * 0.8,
           "E[min(m_t,m_max) v_t]_estimande_plafonnee": 0.5 * 20 * (-0.08) + 0.5 * 10 * 0.8}
    esp["E[v'] sous-echantillon ou plafond (= estimande plafonnee / m_max)"] = esp["E[min(m_t,m_max) v_t]_estimande_plafonnee"] / m_max
    out["esperances_analytiques"] = {k: round(v, 4) for k, v in esp.items()}
    rng = gen("P", 0)
    seuil = 20.0
    longue = rng.random((R, n)) < 0.5
    m_t = np.where(longue, 100, 10)
    pw = np.where(longue, 0.32, 0.9)[:, :, None]
    pb = np.where(longue, 0.40, 0.1)[:, :, None]
    # issues par épisode (100 épisodes tirés ; les unités courtes n'en jouent que 10) ; contraste par épisode
    # c_e = alerte_blanc(e) − alerte_noir(e) sur le même épisode
    c = (rng.random((R, n, 100)) < pw).astype(np.int8) - (rng.random((R, n, 100)) < pb).astype(np.int8)
    cum = np.cumsum(c, axis=2, dtype=np.int32)
    idx_t = m_t - 1
    v_tous = np.take_along_axis(cum, idx_t[:, :, None], axis=2)[:, :, 0] / m_t
    # sous-échantillon scellé de m_max épisodes : les épisodes étant échangeables et le tirage indépendant des issues,
    # garder les m_max premiers a la même loi qu'un sous-ensemble tiré par la graine de l'engagement
    m_s = np.minimum(m_t, m_max)
    v_sous = np.take_along_axis(cum, (m_s - 1)[:, :, None], axis=2)[:, :, 0] / m_s
    del c, cum
    vp_sous = (m_s / m_max) * v_sous
    vp_plaf = (m_s / m_max) * v_tous
    vp_sans_regle = (m_t / m_max) * v_tous
    vp_mmax100 = (m_t / 100) * v_tous
    res = {}
    for nom, vp in (("sous_echantillon_scelle_m_max_20 (D-S27)", vp_sous), ("plafond_min(m_t,m_max)/m_max_sur_tous_les_episodes", vp_plaf),
                    ("m_max_declare_100_(vrai_maximum)", vp_mmax100)):
        W = richesse_chemin(vp)
        res[nom] = {"moyenne_de_v'": round(float(vp.mean()), 4), "ecart_type_de_v'": round(float(vp.std()), 4),
                    "P(promotion_au_seuil_20_sur_250_unites)": round(float((W >= seuil).any(axis=1).mean()), 4)}
    neg = (1 + 0.9 * vp_sans_regle) <= 0
    res["sans_regle_(m_t/m_max)_v,_m_max_20_depasse"] = {"min_de_v'": round(float(vp_sans_regle.min()), 3),
                                                        "part_des_unites_ou_1+0,9v'<=0": round(float(neg.mean()), 4)}
    out["monde_deux_longueurs_n250"] = {"repetitions": R, "resultats": res}
    return out


# ------------------------------------------------------------------------------------------------------------- T
def section_T(R):
    """Famille m = 5 : strate 1 = 3 fiches vraies (20 points) + témoin faux asymétrique (tirages avec remise dans une
    banque 90/10 de moyenne nulle : ici le monde S1 lui-même) ; strate 2 = 1 fiche nulle S1. 250 unités. Règle e-BH à
    α = 0,05, lecture continue (arrêt à m/α). Témoin promu → promotions de la strate 1 suspendues (retirées ici)."""
    out = {}
    n, m = 250, 5
    for idx, n in enumerate((100, 250, 1000)):
        rng = gen("T", idx)
        Ws = [chemin_vrai(rng, R, n) for _ in range(3)] + [chemin_S1(rng, R, n), chemin_S1(rng, R, n)]
        E = np.stack([np.where(W.max(axis=1) >= m / ALPHA, W.max(axis=1), W[:, -1]) for W in Ws], axis=1)
        rej = ebh_pondere(E, np.full(m, ALPHA / m))
        temoin = rej[:, 3]
        nulle2 = rej[:, 4]
        V = temoin.astype(int) + nulle2.astype(int)
        Rt = rej.sum(axis=1)
        fdp_avant = np.where(Rt > 0, V / np.maximum(Rt, 1), 0.0)
        # suspension de la strate 1 (fiches 0 à 3) quand le témoin est promu
        rej2 = rej.copy()
        rej2[temoin, :4] = False
        V2 = rej2[:, 4].astype(int)
        R2 = rej2.sum(axis=1)
        fdp_apres = np.where(R2 > 0, V2 / np.maximum(R2, 1), 0.0)
        k_vrais = rej[:, :3].sum(axis=1)
        out[f"n{n}"] = {"repetitions": R,
                        "P(temoin_promu)": round(float(temoin.mean()), 4),
                        "P(temoin_promu | 3 vraies promues)": round(float(temoin[k_vrais == 3].mean()), 4) if (k_vrais == 3).any() else None,
                        "part_des_repetitions_avec_3_vraies_promues": round(float((k_vrais == 3).mean()), 4),
                        "seuil_du_temoin_quand_k=4_promotions": round(m / (ALPHA * 4), 1),
                        "borne_alpha_sur_m": round(ALPHA / m, 4), "borne_alpha": ALPHA,
                        "FDR_avant_suspension": round(float(fdp_avant.mean()), 5),
                        "FDR_de_l_ensemble_survivant_apres_suspension": round(float(fdp_apres.mean()), 5),
                        "P(au_moins_une_fausse_promotion)_avant": round(float((V > 0).mean()), 4),
                        "P(au_moins_une_fausse_promotion)_apres": round(float((V2 > 0).mean()), 4),
                        "vraies_promues_moyenne_avant": round(float(k_vrais.mean()), 3),
                        "vraies_promues_moyenne_apres": round(float(rej2[:, :3].sum(axis=1).mean()), 3)}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rep", type=int, default=2000)
    args = ap.parse_args()
    t0 = time.time()
    sortie = {"manifeste": {"script": "contre-verification-pari-signe-v5.py", "entropie_SeedSequence": ENTROPIE,
                            "derivation": "SeedSequence(ENTROPIE, spawn_key=(code de section, indice))",
                            "codes_sections": CODES, "repetitions_de_base": args.rep, "python": sys.version.split()[0],
                            "numpy": np.__version__, "plateforme": platform.platform(),
                            "grille": LAMBDAS.tolist(), "alpha": ALPHA}}
    sortie["H_heritage_et_nouvelles_quatre_lectures"] = section_H(args.rep)
    sortie["P_unite_au_dela_de_m_max_estimande"] = section_P(args.rep)
    sortie["T_temoin_promu_suspension"] = section_T(args.rep)
    sortie["manifeste"]["duree_secondes"] = round(time.time() - t0, 1)
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
