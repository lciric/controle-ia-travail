"""Calcul d'appui 6 du concepteur — cas d'école de la batterie, version 3 du texte — v2.

Calcul d'appui, non vérifié : il éprouve des formules du texte `batterie-fuite-banque-revisee-v3.md` ; ce n'est pas
l'instrument. Aucune banque, aucun appel de modèle, aucun réseau.

  A. Règle de trois instances au hasard (condition C4) : cas d'école de la probabilité exacte, comparée à
     l'énumération de tous les triplets ; tirage de contrôle comparé à la probabilité exacte.
  B. Le plus grand nombre de contre-exemples qui laisse la probabilité au plus égale à la moitié.
  C. Règle des ex æquo : les trois cas d'école du rappel ; excès moyen d'une sonde sans information dont tous les
     scores sont distincts (attendu exact : 8/76 − 0,10).
  D. « Non calculable » : une aire non définie rend la condition non tenue.
  E. Critère d'arrêt de la sonde des nombres : sur cinq banques du banc d'épreuve (calcul 4), les douze premiers
     apprentissages (quatre écritures, racines notées 1000, 1001 et 1002), avec trois critères — le décrément (texte,
     § 2.2), la taille du pas de Newton entier, la taille du pas effectif (proposition de la contre-lecture,
     remarque 2). Pour chacun : apprentissages déclarés non convergés, pas le plus long, écart le plus grand des poids
     à ceux du critère du décrément.
  F. Audit du tirage de contrôle (texte, C4), sur la banque saine du banc : écart entre la moyenne du tirage et celle
     du calcul exact, avec le calcul juste, puis avec un calcul faussé (contre-exemples comptés jusqu'à N seulement).
     Le prototype lit le statut des instances tirées dans le profil qui sert au calcul exact ; l'instrument, lui,
     doit les passer par la vérification exacte de la course.

Ce que le prototype ne porte pas, et que ce calcul n'éprouve donc pas : le contrôle de chaîne ; la garde « plus d'un
énoncé de la sous-banque sur dix noté 0 faute d'apprentissage » (le compte est rendu, la garde n'est pas codée).

Emploi (depuis ce dossier) :
  OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONPATH=<dépôt>/src python3 calcul_6_cas_d_ecole_v2.py SORTIE.json > SORTIE.txt
"""
from __future__ import annotations

import itertools
import json
import math
import sys
from collections import defaultdict
from fractions import Fraction

import numpy as np

from controle_ia.oracles_plantes_v6 import parametres as pk_parametres

import calcul_4_banc_d_epreuve_v2 as c4
from outils_batterie_v1 import rappel_au_prorata, rappel_bloc_entier
from sondes_batterie_v1 import aire_qui_fait_foi, squelette, traits_des_nombres
from sondes_batterie_v2 import (ARMIJO, DEMI_PAS_MAX, PAS_MAX, TOLERANCE, LogistiqueAmortie, hasard_exact,
                                hasard_tirage, juger, profil_des_instances)


def par_enumeration(M: int, m: int) -> Fraction:
    """Part des triplets d'instances distinctes qui contiennent au moins un contre-exemple (les m premières)."""
    if M <= 3:
        return Fraction(int(m >= 1))
    triplets = list(itertools.combinations(range(M), 3))
    return Fraction(sum(1 for t in triplets if min(t) < m), len(triplets))


def _perte(w, Z, y) -> float:
    s = Z @ w
    return float(np.sum(np.logaddexp(0.0, s) - y * s) + 0.5 * float(w @ w))


def newton(X, y, critere: str):
    """Le Newton amorti du texte, avec l'un de trois critères d'arrêt. Rend (poids, convergé, nombre de pas).
    « decrement » : arrêt si le décrément est au plus TOLERANCE × nombre d'énoncés (critère du texte ; même calcul que
    `LogistiqueAmortie`). « pas_entier » : arrêt si le plus grand pas de Newton entier est sous 1e-10. « pas_effectif » :
    le pas trouvé par la recherche est pris quoi qu'il arrive ; arrêt si le plus grand pas effectif est sous 1e-10."""
    X = np.asarray(X, float)
    y = np.asarray(y, float)
    mu, sd = X.mean(axis=0), X.std(axis=0)
    nul = sd == 0
    sd[nul] = 1.0
    Z = (X - mu) / sd
    Z[:, nul] = 0.0
    Z = np.hstack([np.ones((len(Z), 1)), Z])
    w = np.zeros(Z.shape[1])
    f = _perte(w, Z, y)
    for pas in range(1, PAS_MAX + 1):
        s = Z @ w
        p = 1.0 / (1.0 + np.exp(-np.clip(s, -700.0, 700.0)))
        g = Z.T @ (p - y) + w
        H = (Z * (p * (1 - p))[:, None]).T @ Z + np.eye(len(w))
        d = np.linalg.solve(H, g)
        pente = float(g @ d)
        if critere == "decrement" and pente <= TOLERANCE * len(y):
            return w - d, True, pas
        if critere == "pas_entier" and float(np.max(np.abs(d))) < 1e-10:
            return w - d, True, pas
        t, accepte = 1.0, False
        for _k in range(DEMI_PAS_MAX):
            f1 = _perte(w - t * d, Z, y)
            if f1 <= f - ARMIJO * t * pente:
                accepte = True
                break
            t /= 2
        if critere == "pas_effectif":
            w = w - t * d
            f = _perte(w, Z, y)
            if float(np.max(np.abs(t * d))) < 1e-10:
                return w, True, pas
            continue
        if not accepte:
            return w, False, pas
        w, f = w - t * d, f1
    return w, False, PAS_MAX


def criteres_d_arret() -> dict:
    cap = pk_parametres.charger()[0]["capacites"]
    out = {}
    for variante, dose in (("saine", 0.0), ("grandeur", 1.0), ("relation", 1.0), ("gabarit", 0.0), ("fenetres", 0.0)):
        groupes = defaultdict(list)
        for r in c4.RACINES:
            _mondes, vivier, _sb = c4.construire(r, variante, dose, cap)
            for x in vivier:
                groupes[squelette(x["texte"])].append((r, traits_des_nombres(x["texte"], x["N"], x["servis"]), float(x["y"])))
        bilan = {c: {"non_converges": 0, "pas_le_plus_long": 0, "ecart_des_poids_le_plus_grand": 0.0}
                 for c in ("decrement", "pas_entier", "pas_effectif")}
        ecart_au_module, n = 0.0, 0
        for _sq, lignes in sorted(groupes.items()):
            for r_note in (1000, 1001, 1002):
                X = np.array([l[1] for l in lignes if l[0] != r_note], float)
                y = np.array([l[2] for l in lignes if l[0] != r_note])
                n += 1
                ref, _ok, _pas = newton(X, y, "decrement")
                ecart_au_module = max(ecart_au_module, float(np.max(np.abs(ref - LogistiqueAmortie(X, y).w))))
                for c in bilan:
                    w, ok, pas = newton(X, y, c)
                    bilan[c]["non_converges"] += int(not ok)
                    bilan[c]["pas_le_plus_long"] = max(bilan[c]["pas_le_plus_long"], pas)
                    bilan[c]["ecart_des_poids_le_plus_grand"] = max(bilan[c]["ecart_des_poids_le_plus_grand"],
                                                                    float(np.max(np.abs(w - ref))))
        for c in bilan:
            bilan[c]["ecart_des_poids_le_plus_grand"] = float(f"{bilan[c]['ecart_des_poids_le_plus_grand']:.1e}")
        out[f"{variante}/{dose}"] = {"apprentissages": n, "ecart_au_module_sondes_batterie_v2": ecart_au_module, **bilan}
    return out


def audit_du_tirage() -> dict:
    cap = pk_parametres.charger()[0]["capacites"]
    juste, fausse, tirage = [], [], []
    for rang, r in enumerate(c4.RACINES):
        mondes, _vivier, sb = c4.construire(r, "saine", 0.0, cap)
        for k, x in enumerate([x for x in sb if x["y"]]):
            st = profil_des_instances(mondes[x["w"]], mondes[x["w"]].analyser(x["texte"]))
            juste.append(hasard_exact(len(st), sum(st)))
            fausse.append(hasard_exact(len(st), sum(st[: x["N"] + 1])))  # contre-exemples comptés jusqu'à N seulement
            tirage.append(hasard_tirage(st, rang, k))
    t, out = float(np.mean(tirage)), {"faux": len(tirage), "moyenne_du_tirage": round(float(np.mean(tirage)), 4)}
    for nom, v in (("calcul_juste", juste), ("calcul_fausse", fausse)):
        e = abs(t - float(np.mean(v)))
        out[nom] = {"moyenne_exacte": round(float(np.mean(v)), 4), "ecart": round(e, 4), "audit": bool(e > 0.02)}
    return out


def main(chemin):
    res = {"numpy": np.__version__}

    # ---------------------------------------------------------------- A. règle du hasard
    cas = {"un contre-exemple parmi 13 instances": (13, 1, Fraction(3, 13)),
           "un faux sans variable (une instance, contre-exemple)": (1, 1, Fraction(1)),
           "aucun contre-exemple vérifiable parmi 13 instances": (13, 0, Fraction(0)),
           "trois instances, un contre-exemple": (3, 1, Fraction(1)),
           "deux instances, deux contre-exemples": (2, 2, Fraction(1)),
           "46 instances, toutes contre-exemples": (46, 46, Fraction(1)),
           "aucune instance": (0, 0, Fraction(0))}
    A = {}
    for nom, (M, m, attendu) in cas.items():
        v = hasard_exact(M, m)
        A[nom] = {"M": M, "m": m, "valeur": round(v, 6), "attendu": str(attendu), "conforme": abs(v - float(attendu)) < 1e-12}
    ecart_max = 0.0
    for M in range(4, 15):
        for m in range(0, M + 1):
            ecart_max = max(ecart_max, abs(hasard_exact(M, m) - float(par_enumeration(M, m))))
    A["écart le plus grand à l'énumération de tous les triplets, M de 4 à 14"] = float(f"{ecart_max:.1e}")
    # tirage de contrôle : fréquence sur 20 000 graines, contre la probabilité exacte
    tirages = {}
    for M, m in ((13, 1), (31, 6), (46, 9), (1, 1), (13, 0), (2, 1)):
        statuts = [i < m for i in range(M)]
        f = float(np.mean([hasard_tirage(statuts, 9000, k) for k in range(20000)]))
        tirages[f"M={M}, m={m}"] = {"frequence": round(f, 4), "exacte": round(hasard_exact(M, m), 4),
                                    "ecart": round(abs(f - hasard_exact(M, m)), 4)}
    A["tirage de contrôle, 20 000 graines"] = tirages
    res["A_regle_du_hasard"] = A

    # ---------------------------------------------------------------- B. seuil de densité
    B = {}
    for M in (13, 31, 46, 100, 1000):
        m = max(k for k in range(M + 1) if hasard_exact(M, k) <= 0.5)
        B[f"M={M}"] = {"plus_grand_m_sous_la_moitie": m, "part_des_instances": round(m / M, 4),
                       "probabilite": round(hasard_exact(M, m), 4), "probabilite_a_m_plus_un": round(hasard_exact(M, m + 1), 4)}
    B["limite, instances nombreuses : 1 - (1/2)^(1/3)"] = round(1 - 0.5 ** (1 / 3), 4)
    res["B_seuil_de_densite"] = B

    # ---------------------------------------------------------------- C. ex æquo
    C = {}
    egaux = ([0.0] * 75, [0.0] * 75)
    parfaits = ([0.0] * 75, [1.0] * 75)
    grossier = ([1.0] * 9 + [0.0] * 66, [1.0] * 45 + [0.0] * 30)
    for nom, (vrais, faux) in (("scores tous égaux", egaux), ("séparation parfaite", parfaits),
                               ("9 vérités sur 75 et 45 faux sur 75 au score haut", grossier)):
        C[nom] = {"exces_au_prorata": float(rappel_au_prorata(vrais, faux) - Fraction(1, 10)),
                  "exces_au_bloc_entier": float(rappel_bloc_entier(vrais, faux) - Fraction(1, 10))}
    g = np.random.default_rng(np.random.SeedSequence(20261122, spawn_key=(4000,)))
    sim = {}
    for nom, n_faux in (("tous les faux (75)", 75), ("faux tôt (38)", 38), ("pièges (37)", 37)):
        v = []
        for _ in range(20000):
            s = g.permutation(75 + n_faux)  # 75 + n scores tous distincts, sans information
            v.append(float(rappel_au_prorata([int(x) for x in s[:75]], [int(x) for x in s[75:]]) - Fraction(1, 10)))
        sim[nom] = {"exces_moyen": round(float(np.mean(v)), 5), "erreur_type": round(float(np.std(v) / math.sqrt(len(v))), 5)}
    C["sonde sans information, scores tous distincts"] = {"attendu_exact_8_sur_76_moins_un_dixieme": round(8 / 76 - 0.10, 5),
                                                         "simulation_20000_tirages": sim}
    res["C_ex_aequo"] = C

    # ---------------------------------------------------------------- D. aire non définie
    aire = aire_qui_fait_foi([], {}, set())
    res["D_aire_non_definie"] = {"aire": aire, "jugement": juger([0.5] * 119 + [aire], 0.75, 2000)}

    # ---------------------------------------------------------------- E. critère d'arrêt
    res["E_criteres_d_arret"] = criteres_d_arret()

    # ---------------------------------------------------------------- F. audit du tirage de contrôle
    res["F_audit_du_tirage"] = audit_du_tirage()

    with open(chemin, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    print("Calcul d'appui 6 — cas d'école de la batterie, version 3 du texte (prototype du concepteur)")
    print(f"numpy {np.__version__}")
    print("\nA. Règle de trois instances au hasard")
    for k, v in A.items():
        if isinstance(v, dict) and "M" in v:
            print(f"  {k} : {v}")
    k = "écart le plus grand à l'énumération de tous les triplets, M de 4 à 14"
    print(f"  {k} : {A[k]}")
    print("  tirage de contrôle, 20 000 graines")
    for k, v in tirages.items():
        print(f"    {k} : {v}")
    print("\nB. Le plus grand nombre de contre-exemples qui laisse la probabilité au plus égale à la moitié")
    for k, v in B.items():
        print(f"  {k} : {v}")
    print("\nC. Règle des ex æquo")
    for k, v in C.items():
        print(f"  {k} : {v}")
    print("\nD. Aire non définie")
    print(f"  {res['D_aire_non_definie']}")
    print("\nE. Critère d'arrêt de la sonde des nombres (douze apprentissages par banque)")
    for k, v in res["E_criteres_d_arret"].items():
        print(f"  {k} : apprentissages {v['apprentissages']} ; écart au module {v['ecart_au_module_sondes_batterie_v2']}")
        for c in ("decrement", "pas_entier", "pas_effectif"):
            print(f"    {c:13s} : {v[c]}")
    print("\nF. Audit du tirage de contrôle, banque saine du banc (écart de plus de 0,02 : audit)")
    for k, v in res["F_audit_du_tirage"].items():
        print(f"  {k} : {v}")


if __name__ == "__main__":
    main(sys.argv[1])
