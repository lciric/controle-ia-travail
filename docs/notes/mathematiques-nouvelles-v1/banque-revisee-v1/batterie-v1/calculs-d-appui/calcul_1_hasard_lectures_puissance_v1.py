"""Calcul d'appui 1 du concepteur — batterie de fuite de la banque révisée (mathématiques nouvelles) — v1.

Calcul d'appui, non vérifié : il éprouve des formules du texte de la batterie ; ce n'est pas l'instrument.
Ce que le calcul éprouve, sans aucune banque (scores simulés seulement) :
  0. trois cas d'école de la règle des ex æquo (prorata contre bloc entier) ;
  1. le comportement d'une sonde SANS information (cas sain) : excès moyen, borne haute, pour trois sortes de scores
     (continus ; liés par paire, comme le classifieur de style sur une banque appariée ; grossiers par cellule) et les
     deux règles d'ex æquo (prorata ; bloc entier) ;
  2. le taux de réussite d'une banque saine sous les trois lectures du seuil de C3 :
       (i)   excès <= 0,10 à fausses alarmes 0,10 (rappel <= 0,20) ;
       (ii)  rappel <= 0,10 à fausses alarmes 0,05 (excès <= 0,05) ;
       (iii) rappel <= 0,10 à fausses alarmes 0,10 (excès <= 0) ;
     pour une grandeur seule et pour les neuf (trois sondes, trois ensembles), avec 40 et 120 racines ;
  3. la sensibilité : taux d'échec quand la fuite vraie donne un excès de 0,05 ; 0,08 ; 0,10 ; 0,12 ; 0,15 ;
  4. la règle de relecture « hors de la plage des racines neuves » : fréquence de sortie d'une valeur saine ;
  5. la puissance exacte de l'affirmation E4 (bras outillé contre règle aveugle) selon la part v_A des faux à portée de
     la règle aveugle (même modèle que le diagnostic, partie h : indépendance sachant l'item).

Graines : numpy.random.SeedSequence(20261122, spawn_key=(3000 + i,)), i = 0..4, une par partie.
Emploi (depuis ce dossier) : python3 calcul_1_hasard_lectures_puissance_v1.py SORTIE.json > SORTIE.txt
"""
from __future__ import annotations

import json
import math
import sys
import time
from fractions import Fraction

import numpy as np

from outils_batterie_v1 import rappel_au_prorata, rappel_bloc_entier, score_apparie

RACINE = 20261122
NV, NFT, NPG = 75, 38, 37  # sous-banque : vrais, faux tôt, pièges
T0 = time.time()


def gen(i):
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=(3000 + i,)))


def excès_une_racine(rng, sorte, fuite=0.0, plafond=Fraction(1, 10)):
    """Simule une racine (75 paires : 38 à faux tôt, 37 à piège) pour une sonde sans information (`fuite` = 0) ou avec
    un décalage gaussien `fuite` ajouté aux scores des faux. Rend les six excès (prorata puis bloc entier) pour les
    trois ensembles : faux tôt, pièges, tous les faux."""
    if sorte == "continus":
        sv = rng.normal(size=NV)
        sf = rng.normal(size=NV) + fuite
    elif sorte == "paires":  # même score pour les deux membres d'une paire
        sv = rng.normal(size=NV)
        sf = sv + fuite
    elif sorte == "cellules":  # score commun à une cellule (25 cellules de 3 paires)
        c = np.repeat(rng.normal(size=25), 3)
        sv, sf = c.copy(), c + fuite
    else:
        raise ValueError(sorte)
    sv = [round(float(x), 9) for x in sv]
    sf = [round(float(x), 9) for x in sf]
    perm = rng.permutation(NV)
    ft = [sf[i] for i in perm[:NFT]]
    pg = [sf[i] for i in perm[NFT:]]
    out = []
    for f in (rappel_au_prorata, rappel_bloc_entier):
        for ens in (ft, pg, sf):
            out.append(float(f(sv, ens, plafond) - plafond))
    return out


def borne_haute_rapide(v, rng, tirages=2000):
    v = np.asarray(v, float)
    idx = rng.integers(0, len(v), size=(tirages, len(v)))
    return float(np.quantile(v[idx].mean(axis=1), 0.95))


def partie_0():
    """Cas d'école de la fonction de rappel (75 vrais, un ensemble de 75 faux), excès = rappel - 0,10."""
    cas = {
        "scores tous égaux (sonde sans information)": ([0] * 75, [0] * 75),
        "séparation parfaite": (list(range(75)), [1000] * 75),
        "trait grossier : 9 vrais sur 75 et 45 faux sur 75 au score haut, le reste au score bas": ([1] * 9 + [0] * 66, [1] * 45 + [0] * 30),
    }
    return {nom: {"exces_au_prorata": round(float(rappel_au_prorata(v, f) - Fraction(1, 10)), 4),
                  "exces_au_bloc_entier": round(float(rappel_bloc_entier(v, f) - Fraction(1, 10)), 4)}
            for nom, (v, f) in cas.items()}


def partie_1_et_2(rng, generateurs=400):
    """Pour chaque sorte de score et chaque nombre de racines : distribution de la moyenne et de la borne haute de
    l'excès sans fuite ; réussite sous (i), (ii), (iii) pour une grandeur et pour les neuf."""
    sortie = {}
    for R in (40, 120):
        for sorte in ("continus", "paires", "cellules"):
            res = {"prorata": {"moy": [], "bh": []}, "bloc": {"moy": [], "bh": []}, "prorata_fa05": {"moy": [], "bh": []}}
            for _ in range(generateurs):
                X = np.array([excès_une_racine(rng, sorte) for _ in range(R)])           # R x 6
                X5 = np.array([excès_une_racine(rng, sorte, plafond=Fraction(1, 20))[:3] for _ in range(R)])
                res["prorata"]["moy"].append(X[:, :3].mean(axis=0))
                res["prorata"]["bh"].append([borne_haute_rapide(X[:, j], rng) for j in range(3)])
                res["bloc"]["moy"].append(X[:, 3:].mean(axis=0))
                res["bloc"]["bh"].append([borne_haute_rapide(X[:, j], rng) for j in range(3, 6)])
                res["prorata_fa05"]["moy"].append(X5.mean(axis=0))
                res["prorata_fa05"]["bh"].append([borne_haute_rapide(X5[:, j], rng) for j in range(3)])
            d = {}
            for regle, r in res.items():
                moy, bh = np.array(r["moy"]), np.array(r["bh"])
                d[regle] = {
                    "exces_moyen [faux tôt, pièges, tous]": [round(float(x), 4) for x in moy.mean(axis=0)],
                    "ecart_type_de_la_moyenne": [round(float(x), 4) for x in moy.std(axis=0)],
                    "borne_haute_moyenne": [round(float(x), 4) for x in bh.mean(axis=0)],
                    "borne_haute_max_vue": [round(float(x), 4) for x in bh.max(axis=0)],
                }
                if regle in ("prorata", "bloc"):
                    d[regle]["reussite_(i)_une_grandeur"] = [round(float(x), 4) for x in (bh <= 0.10).mean(axis=0)]
                    d[regle]["reussite_(i)_trois_ensembles"] = round(float((bh <= 0.10).all(axis=1).mean()), 4)
                    d[regle]["reussite_(iii)_une_grandeur"] = [round(float(x), 4) for x in (bh <= 0.0).mean(axis=0)]
                    d[regle]["reussite_(iii)_trois_ensembles"] = round(float((bh <= 0.0).all(axis=1).mean()), 4)
                    # neuf grandeurs : trois sondes indépendantes de même sorte => produit des réussites à trois ensembles
                    d[regle]["reussite_(i)_neuf"] = round(float((bh <= 0.10).all(axis=1).mean()) ** 3, 4)
                    d[regle]["reussite_(iii)_neuf"] = round(float((bh <= 0.0).all(axis=1).mean()) ** 3, 4)
                else:
                    d[regle]["reussite_(ii)_une_grandeur"] = [round(float(x), 4) for x in (bh <= 0.05).mean(axis=0)]
                    d[regle]["reussite_(ii)_trois_ensembles"] = round(float((bh <= 0.05).all(axis=1).mean()), 4)
                    d[regle]["reussite_(ii)_neuf"] = round(float((bh <= 0.05).all(axis=1).mean()) ** 3, 4)
            sortie[f"R={R}/{sorte}"] = d
            print(f"[{time.time() - T0:6.1f} s] parties 1-2 : R={R} {sorte}", file=sys.stderr, flush=True)
    return sortie


def partie_3(rng, generateurs=300):
    """Sensibilité : scores continus, faux décalés de `d` (binormal). Excès vrai (limite) = Phi(d - z_0,90) - 0,10.
    Taux d'échec de (i) sur l'ensemble « tous les faux » et sur « au moins un des trois ensembles »."""
    from statistics import NormalDist
    nd = NormalDist()
    z = nd.inv_cdf(0.90)
    sortie = []
    for cible in (0.0, 0.05, 0.08, 0.10, 0.12, 0.15, 0.20):
        d = nd.inv_cdf(0.10 + cible) + z if cible > 0 else 0.0
        for R in (40, 120):
            ech_tous = ech_un = 0
            moy = []
            for _ in range(generateurs):
                X = np.array([excès_une_racine(rng, "continus", fuite=d)[:3] for _ in range(R)])
                bh = [borne_haute_rapide(X[:, j], rng) for j in range(3)]
                ech_tous += bh[2] > 0.10
                ech_un += max(bh) > 0.10
                moy.append(X[:, 2].mean())
            sortie.append({"exces_vrai_vise": cible, "decalage": round(d, 4), "R": R,
                           "exces_moyen_mesure_tous_les_faux": round(float(np.mean(moy)), 4),
                           "taux_d_echec_(i)_tous_les_faux": round(ech_tous / generateurs, 4),
                           "taux_d_echec_(i)_au_moins_un_des_trois_ensembles": round(ech_un / generateurs, 4)})
        print(f"[{time.time() - T0:6.1f} s] partie 3 : cible {cible}", file=sys.stderr, flush=True)
    return sortie


def partie_4(rng, essais=20000):
    """Relecture : une valeur de la banque réelle, tirée de la même loi que les R valeurs des racines neuves, sort de leur
    plage (strictement au-dessus du maximum ou au-dessous du minimum) avec la probabilité 2/(R+1) si la loi est continue."""
    sortie = []
    for R in (40, 80, 120, 200):
        x = rng.normal(size=(essais, R + 1))
        hors = ((x[:, 0] > x[:, 1:].max(axis=1)) | (x[:, 0] < x[:, 1:].min(axis=1)))
        hors3 = np.zeros(essais, bool)
        for _ in range(3):  # trois valeurs relues, supposées indépendantes
            y = rng.normal(size=(essais, R + 1))
            hors3 |= (y[:, 0] > y[:, 1:].max(axis=1)) | (y[:, 0] < y[:, 1:].min(axis=1))
        sortie.append({"R": R, "theorie_une_valeur": round(2 / (R + 1), 4), "simule_une_valeur": round(float(hors.mean()), 4),
                       "theorie_trois_valeurs_borne": round(6 / (R + 1), 4), "simule_trois_valeurs": round(float(hors3.mean()), 4)})
    return sortie


def partie_5():
    """Puissance exacte de E4 (S_SA(0) >= 2,2504, n = 75) : la règle aveugle touche m = round(75 v_A) faux ; S rend un
    contre-exemple vérifié avec la probabilité p_in sur un faux à portée de la règle, p_out hors de portée ;
    n10 ~ Bin(75 - m, p_out), n01 ~ Bin(m, 1 - p_in), indépendants."""
    Z = 2.2504
    n = 75

    def binom(k, N, p):
        return math.comb(N, k) * p ** k * (1 - p) ** (N - k)

    sortie = []
    for p_in, p_out in ((0.90, 0.50), (0.90, 0.75), (1.00, 0.25), (1.00, 0.50), (0.80, 0.50)):
        ligne = {"p_in": p_in, "p_out": p_out, "puissance_par_v_A": {}}
        for m in range(15, 72, 3):
            pw = 0.0
            for a in range(0, n - m + 1):
                pa = binom(a, n - m, p_out)
                if pa < 1e-15:
                    continue
                for b in range(0, m + 1):
                    pb = binom(b, m, 1 - p_in)
                    if pb < 1e-15:
                        continue
                    if score_apparie(a, b, n, 0.0) >= Z:
                        pw += pa * pb
            ligne["puissance_par_v_A"][f"{m}/75={m / 75:.2f}"] = round(pw, 3)
        sortie.append(ligne)
    return sortie


def main(chemin):
    out = {"graines": {"racine": RACINE, "enfants": "3000 + i, i = 0 (parties 1-2), 1 (partie 3), 2 (partie 4)"},
           "numpy": np.__version__}
    out["partie_0_cas_d_ecole"] = partie_0()
    out["parties_1_2_sonde_sans_information"] = partie_1_et_2(gen(0))
    out["partie_3_sensibilite"] = partie_3(gen(1))
    out["partie_4_relecture_hors_plage"] = partie_4(gen(2))
    out["partie_5_puissance_E4"] = partie_5()
    with open(chemin, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    print("Calcul d'appui 1 — sonde sans information, lectures du seuil, relecture, puissance de E4")
    print(f"numpy {np.__version__} ; graines : {out['graines']}")
    print("\n0. Cas d'école de la règle des ex æquo")
    for nom, d in out["partie_0_cas_d_ecole"].items():
        print(f"  {nom} : {d}")
    print("\n1-2. Sonde sans information (banque saine simulée, 400 générateurs par case) ; excès = rappel - fausses alarmes visées")
    for cle, d in out["parties_1_2_sonde_sans_information"].items():
        print(f"  {cle}")
        for regle, r in d.items():
            print(f"    règle {regle}")
            for k, v in r.items():
                print(f"      {k:45s} : {v}")
    print("\n3. Sensibilité (scores continus, faux décalés ; 300 générateurs par case)")
    for l in out["partie_3_sensibilite"]:
        print("  " + " ; ".join(f"{k} {v}" for k, v in l.items()))
    print("\n4. Relecture « hors de la plage » d'une valeur saine")
    for l in out["partie_4_relecture_hors_plage"]:
        print("  " + " ; ".join(f"{k} {v}" for k, v in l.items()))
    print("\n5. Puissance exacte de E4 selon la part v_A des faux à portée de la règle aveugle")
    for l in out["partie_5_puissance_E4"]:
        print(f"  p_in {l['p_in']} p_out {l['p_out']} : " + " ; ".join(f"{k} -> {v}" for k, v in l["puissance_par_v_A"].items()))


if __name__ == "__main__":
    main(sys.argv[1])
