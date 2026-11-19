#!/usr/bin/env python3
"""Barreau 5, plan d'avant l'entretien : puissance et pièges des plans à plusieurs adaptateurs tenus à l'écart (v1).

LOIS INVENTÉES. Aucune donnée du programme n'est lue : ni score, ni activation, ni adaptateur. Planification seulement
(R1 : rien ici n'est une lecture de résultat ; R3 : aucune taille n'est choisie pour obtenir un signe).
Graines : `numpy.random.SeedSequence(ENTROPIE)`, une graine dérivée par bloc (R9). numpy seul.

Unité : l'ADAPTATEUR. Chaque adaptateur tenu à l'écart reçoit une statistique T (déplacement réduit moyen de la sonde,
par rapport au modèle nu, sur des textes honnêtes communs).

Première partie — témoins NON appariés (deux groupes d'adaptateurs indépendants) :
  A  tables exactes de Mann-Whitney à l'échelle de l'adaptateur (u_crit à 99 % et à 95 % bilatéral) ;
  B  puissance d'une comparaison en fonction de l'écart delta (en écarts types entre adaptateurs) ;
  C  puissance d'une conjonction de trois comparaisons qui partagent les mêmes saboteurs ;
  D  taux de faux « sabotage » de cette conjonction quand les groupes sont échangeables ;
  E  monde d'activations : ce que lit vraiment une sonde jugée contre des témoins non appariés (jumeau distillé de
     l'honnête, témoin à changement bénin) quand AUCUNE direction de sabotage n'existe ;
  F  gradient par la part d'épisodes sabotés (0, 1/3, 2/3, 1) contre deux groupes, à nombre d'adaptateurs égal ;
  G  niveau de repli à 95 % bilatéral, pour mémoire.
Seconde partie — familles jumelles (mêmes épisodes, mêmes graines, seul le coût déclaré édité : jumeau, demi-saboteur,
saboteur) :
  H  tables exactes de l'épreuve par permutation dans les familles, et puissance en fonction de l'écart dans la famille ;
  I  monde d'activations pour les familles : issues « sabotage », « empreinte », « non établi » ; monde « force ».
Sortie : JSON sur la sortie standard.
"""
from __future__ import annotations

import functools
import itertools
import json
import math
import sys
import time

import numpy as np

ENTROPIE = 0x5AB07A6EB5_2026_1119_0001
NIVEAU_UNILATERAL = 0.005          # 99 % bilatéral
NIVEAU_REPLI = 0.025               # 95 % bilatéral
DELTAS = [0.0, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 8.0]


def graines(n: int):
    return [np.random.default_rng(s) for s in np.random.SeedSequence(ENTROPIE).spawn(n)]


def bruit(rng, forme, loi: str):
    if loi == "normale":
        return rng.standard_normal(forme)
    if loi == "student3":                         # queues lourdes, ramenée à l'écart type 1
        return rng.standard_t(3, forme) / math.sqrt(3.0)
    raise ValueError(loi)


# =================================================================================== première partie : non apparié
def loi_exacte_u(m: int, n: int) -> np.ndarray:
    """Nombre de rangements de m saboteurs et n témoins ayant u couples à l'envers (récurrence de Mann-Whitney)."""
    f = {}

    def g(a: int, b: int) -> np.ndarray:
        if (a, b) in f:
            return f[(a, b)]
        if a == 0 or b == 0:
            r = np.zeros(1, dtype=object)
            r[0] = 1
        else:
            r = np.zeros(a * b + 1, dtype=object)
            x = g(a - 1, b)                      # le plus grand est un saboteur : aucun couple à l'envers de plus
            r[: len(x)] += x
            y = g(a, b - 1)                      # le plus grand est un témoin : a couples à l'envers de plus
            r[a: a + len(y)] += y
        f[(a, b)] = r
        return r

    return g(m, n)


@functools.lru_cache(maxsize=None)
def u_critique(m: int, n: int, niveau: float):
    loi = loi_exacte_u(m, n)
    total = int(sum(loi))
    cumul, u_crit = 0, None
    for u, c in enumerate(loi):
        cumul += int(c)
        if cumul / total <= niveau:
            u_crit = u
        else:
            break
    p_atteint = (int(sum(loi[: u_crit + 1])) / total) if u_crit is not None else None
    return {"rangements": total, "u_crit": u_crit, "p_unilaterale_minimale": 1.0 / total,
            "p_unilaterale_a_u_crit": p_atteint}


def bloc_a():
    table = {}
    for m in range(3, 9):
        for n in range(3, 11):
            a = u_critique(m, n, NIVEAU_UNILATERAL)
            b = u_critique(m, n, NIVEAU_REPLI)
            table[f"{m}x{n}"] = {"rangements": a["rangements"], "p_min_unilaterale": a["p_unilaterale_minimale"],
                                 "u_crit_99": a["u_crit"], "p_a_u_crit_99": a["p_unilaterale_a_u_crit"],
                                 "u_crit_95": b["u_crit"], "p_a_u_crit_95": b["p_unilaterale_a_u_crit"]}
    return table


def u_inverse(s: np.ndarray, w: np.ndarray) -> np.ndarray:
    """U par tirage : nombre de couples (saboteur, témoin) où le saboteur est sous le témoin. s (R, m), w (R, n)."""
    return (s[:, :, None] < w[:, None, :]).sum(axis=(1, 2))


def bloc_b(rng, tirages=200_000):
    sortie = {}
    for (m, n) in [(5, 5), (5, 6), (6, 6), (4, 6), (5, 10), (6, 12)]:
        uc = u_critique(m, n, NIVEAU_UNILATERAL)["u_crit"]
        for loi in ("normale", "student3"):
            for kappa in (1.0, 2.0):                 # écart type du bras saboteur, en unités de celui du bras témoin
                ligne = {}
                for d in DELTAS:
                    s = d + kappa * bruit(rng, (tirages, m), loi)
                    w = bruit(rng, (tirages, n), loi)
                    ligne[f"delta_{d:g}"] = round(float((u_inverse(s, w) <= uc).mean()), 4)
                sortie[f"{m}x{n}/{loi}/dispersion_saboteur_{kappa:g}"] = ligne
    return sortie


def conjonction(rng, m, n, d_h, d_t, d_e, rho, tirages, loi="normale"):
    """Trois comparaisons : saboteur contre jumeau distillé de l'honnête, contre témoin à changement bénin, contre ce
    même témoin à norme de déplacement égale ; les deux lectures d'un même adaptateur sont corrélées (rho)."""
    uc = u_critique(m, n, NIVEAU_UNILATERAL)["u_crit"]
    zs = bruit(rng, (tirages, m), loi)
    zs2 = rho * zs + math.sqrt(1 - rho ** 2) * bruit(rng, (tirages, m), loi)
    zt = bruit(rng, (tirages, n), loi)
    zt2 = rho * zt + math.sqrt(1 - rho ** 2) * bruit(rng, (tirages, n), loi)
    zh = bruit(rng, (tirages, n), loi)
    ok = (u_inverse(d_h + zs, zh) <= uc) & (u_inverse(d_t + zs, zt) <= uc) & (u_inverse(d_e + zs2, zt2) <= uc)
    return float(ok.mean())


def bloc_c(rng, tirages=200_000):
    sortie = {}
    for (m, n) in [(5, 5), (6, 6)]:
        for rho in (0.5, 0.9):
            for part in (1.0, 0.75, 0.5):                    # l'écart à norme égale, en part de l'écart nominal
                sortie[f"{m}x{n}/rho_{rho:g}/ecart_a_norme_egale_{part:g}_du_nominal"] = {
                    f"delta_{d:g}": round(conjonction(rng, m, n, d, d, part * d, rho, tirages), 4) for d in DELTAS}
    return sortie


def bloc_d(rng, tirages=2_000_000):
    """Groupes échangeables sur au moins une des trois comparaisons : le taux de faux « sabotage » reste sous 0,005."""
    sortie = {}
    for (m, n) in [(5, 5), (6, 6)]:
        sortie[f"{m}x{n}"] = {
            "aucun_ecart": conjonction(rng, m, n, 0.0, 0.0, 0.0, 0.9, tirages),
            "saboteurs_et_temoins_benins_devant_les_jumeaux": conjonction(rng, m, n, 8.0, 0.0, 0.0, 0.9, tirages),
            "ecart_au_nominal_nul_a_norme_egale": conjonction(rng, m, n, 8.0, 8.0, 0.0, 0.0, tirages),
            "borne_theorique": u_critique(m, n, NIVEAU_UNILATERAL)["p_unilaterale_a_u_crit"]}
    return sortie


# ----------------------------------------------------------------------------------------------------------- bloc E
def discriminant(e_s, e_w, bruit_action, lam=1e-2):
    """Discriminant linéaire régularisé (covariance dans les classes = bruit_action² I + terme de rang faible)."""
    mu_s, mu_w = e_s.mean(0), e_w.mean(0)
    dans = np.vstack([e_s - mu_s, e_w - mu_w])
    n_d, c0, diff = len(dans), bruit_action ** 2 + lam, mu_s - mu_w
    w = (diff - dans.T @ np.linalg.solve(n_d * c0 * np.eye(n_d) + dans @ dans.T, dans @ diff)) / c0
    return w / np.linalg.norm(w)


def monde_non_apparie(rng, p, k_s, k_h, m, signal, commun, int_t, spec_t, int_h, contre, bruit_action=1.0):
    """Un monde inventé, témoins non appariés. Déplacement moyen de la couche lue par adaptateur :
        saboteur        : a_i * (g + commun*c + signal*s) + u_i
        témoin bénin    : a_i * int_t * (g + commun*c + t) + spec_t * u_i
        jumeau honnête  : a_i * int_h * g + int_h * u_i          (auto-distillation : rien d'appris, faible)
    g : direction commune à tout adaptateur de la recette ; c : commune à tout changement appris ; s : sabotage ;
    t : changement bénin ; u_i : empreinte propre (norme voisine de 1, p dimensions) ; a_i : jitter log-normal de 15 %.
    Sonde apprise sur les adaptateurs d'apprentissage : saboteurs contre jumeaux honnêtes (`contre` = « H ») ou contre les
    deux sortes de témoins (« HT »). Statistique : w·m_j plus un bruit en 1/sqrt(640). Lecture nominale, et à norme de
    déplacement égale (norme médiane des saboteurs d'apprentissage). Force générique : projection sur la direction
    moyenne des jumeaux honnêtes d'apprentissage."""
    g = np.zeros(p); g[0] = 1.0
    c = np.zeros(p); c[1] = 1.0
    s = np.zeros(p); s[2] = 1.0
    t = np.zeros(p); t[3] = 1.0
    n_act = 640

    def adaptateurs(k, bras):
        a = np.exp(0.15 * rng.standard_normal(k))
        u = rng.standard_normal((k, p)) / math.sqrt(p)
        if bras == "S":
            return a[:, None] * (g + commun * c + signal * s)[None, :] + u
        if bras == "T":
            return (a * int_t)[:, None] * (g + commun * c + t)[None, :] + spec_t * u
        return (a * int_h)[:, None] * g[None, :] + int_h * u

    est = lambda x: x + bruit_action * rng.standard_normal(x.shape) / math.sqrt(n_act)
    app_s, app_h, app_t = adaptateurs(k_s, "S"), adaptateurs(k_h, "H"), adaptateurs(2, "T")
    w = discriminant(est(app_s), est(app_h if contre == "H" else np.vstack([app_h, app_t])), bruit_action)
    note = lambda x: x @ w + bruit_action * rng.standard_normal(len(x)) / math.sqrt(n_act)
    test = {"S": adaptateurs(m, "S"), "H": adaptateurs(m, "H"), "T": adaptateurs(m, "T")}
    cible = np.median(np.linalg.norm(app_s, axis=1))
    ech = lambda x: x * (cible / np.linalg.norm(x, axis=1, keepdims=True))
    g_h = est(app_h).mean(0)
    g_h = g_h / np.linalg.norm(g_h)
    return ({b: note(v) for b, v in test.items()}, {b: note(ech(v)) for b, v in test.items()},
            {b: v @ g_h for b, v in test.items()})


def u_de(a, b):
    return int((a[:, None] < b[None, :]).sum())


MONDES_E = {
    "aucune_direction_de_sabotage": dict(signal=0.0, commun=0.0, int_t=1.0, spec_t=1.0, int_h=0.3),
    "aucune_direction_de_sabotage_changement_appris_commun": dict(signal=0.0, commun=1.0, int_t=1.0, spec_t=1.0, int_h=0.3),
    "aucune_direction_de_sabotage_temoin_benin_plus_faible_en_tout": dict(signal=0.0, commun=0.0, int_t=0.6, spec_t=0.6, int_h=0.3),
    "aucune_direction_de_sabotage_temoin_benin_plus_faible_sur_la_direction_commune": dict(signal=0.0, commun=0.0, int_t=0.6, spec_t=1.0, int_h=0.3),
    "sabotage_0,5": dict(signal=0.5, commun=0.0, int_t=1.0, spec_t=1.0, int_h=0.3),
    "sabotage_1": dict(signal=1.0, commun=0.0, int_t=1.0, spec_t=1.0, int_h=0.3),
}


def bloc_e(rng, mondes=1000):
    """Fréquence de la conjonction « saboteurs devant les jumeaux honnêtes, devant les témoins bénins, et encore devant
    eux à norme égale » (6 contre 6, 99 % bilatéral par comparaison), avec 3 saboteurs et 3 jumeaux d'apprentissage."""
    sortie = {}
    uc = u_critique(6, 6, NIVEAU_UNILATERAL)["u_crit"]
    uc95 = u_critique(6, 6, NIVEAU_REPLI)["u_crit"]
    for contre, etiquette in (("H", "sonde_apprise_contre_les_jumeaux_honnetes"), ("HT", "sonde_apprise_contre_les_deux_temoins")):
        for nom_cas, par in MONDES_E.items():
            for p in (16, 64, 256):
                n = {"contre_jumeaux": 0, "contre_benins": 0, "contre_benins_norme_egale": 0, "conjonction": 0,
                     "force_generique_differente": 0, "conjonction_sans_alerte_de_force": 0}
                for _ in range(mondes):
                    nom, ega, gen = monde_non_apparie(rng, p, 3, 3, 6, contre=contre, **par)
                    d1 = u_de(nom["S"], nom["H"]) <= uc
                    d2 = u_de(nom["S"], nom["T"]) <= uc
                    d3 = u_de(ega["S"], ega["T"]) <= uc
                    u_g = u_de(gen["S"], gen["T"])
                    alerte = (u_g <= uc95) or (u_g >= 36 - uc95)
                    n["contre_jumeaux"] += d1; n["contre_benins"] += d2; n["contre_benins_norme_egale"] += d3
                    n["conjonction"] += (d1 and d2 and d3); n["force_generique_differente"] += alerte
                    n["conjonction_sans_alerte_de_force"] += (d1 and d2 and d3 and not alerte)
                sortie[f"{etiquette}/{nom_cas}/p_{p}"] = {k: round(v / mondes, 4) for k, v in n.items()}
    return sortie


# ----------------------------------------------------------------------------------------------------------- bloc F
def loi_nulle_tendance(doses):
    """Loi exacte, sous l'échange, de la statistique de tendance par rangs S = somme(dose_i * rang_i), par énumération
    des affectations distinctes des rangs aux niveaux de dose."""
    doses = np.asarray(doses, dtype=float)
    n = len(doses)
    niveaux = sorted(set(doses.tolist()))
    tailles = [int((doses == v).sum()) for v in niveaux]
    compte = {}

    def rec(reste, k, acc):
        if k == len(niveaux) - 1:
            cle = round(acc + niveaux[k] * sum(reste), 9)
            compte[cle] = compte.get(cle, 0) + 1
            return
        for choix in itertools.combinations(reste, tailles[k]):
            ens = set(choix)
            rec(tuple(r for r in reste if r not in ens), k + 1, acc + niveaux[k] * sum(choix))

    rec(tuple(range(1, n + 1)), 0, 0.0)
    vals = np.array(sorted(compte))
    return vals, np.array([compte[v] for v in vals], dtype=float)


def seuil_tendance(doses, niveau):
    vals, eff = loi_nulle_tendance(doses)
    total = eff.sum()
    queue = np.cumsum(eff[::-1])[::-1] / total            # P(S >= v)
    ok = np.where(queue <= niveau)[0]
    if len(ok) == 0:
        return None, int(total), float(1.0 / total)
    return float(vals[ok[0]]), int(total), float(queue[ok[0]])


def bloc_f(rng, tirages=100_000):
    plans = {
        "8_adaptateurs": {"deux_groupes_4x4": [0] * 4 + [1] * 4, "gradient_2x2x2x2": [0, 0, 1 / 3, 1 / 3, 2 / 3, 2 / 3, 1, 1]},
        "10_adaptateurs": {"deux_groupes_5x5": [0] * 5 + [1] * 5, "gradient_3x2x2x3": [0] * 3 + [1 / 3] * 2 + [2 / 3] * 2 + [1] * 3,
                           "gradient_4x1x1x4": [0] * 4 + [1 / 3] + [2 / 3] + [1] * 4},
        "12_adaptateurs": {"deux_groupes_6x6": [0] * 6 + [1] * 6, "gradient_3x3x3x3": [0] * 3 + [1 / 3] * 3 + [2 / 3] * 3 + [1] * 3,
                           "gradient_4x2x2x4": [0] * 4 + [1 / 3] * 2 + [2 / 3] * 2 + [1] * 4},
    }
    formes = {"lineaire": lambda x: x, "seuil_haut": lambda x: (x >= 0.99).astype(float),
              "saturee_des_un_tiers": lambda x: (x > 0.01).astype(float), "racine": lambda x: np.sqrt(x)}
    sortie = {}
    for taille, pl in plans.items():
        for nom, doses in pl.items():
            doses = np.asarray(doses, dtype=float)
            seuil, total, p_att = seuil_tendance(doses, NIVEAU_UNILATERAL)
            fiche = {"affectations_distinctes": total, "p_unilaterale_minimale": 1.0 / total,
                     "p_au_seuil": p_att, "atteint_99_bilateral": seuil is not None}
            for forme, f in formes.items():
                ligne = {}
                for d in (2.0, 3.0, 4.0, 6.0):
                    if seuil is None:
                        ligne[f"delta_{d:g}"] = 0.0
                        continue
                    y = d * f(doses)[None, :] + rng.standard_normal((tirages, len(doses)))
                    rangs = y.argsort(axis=1).argsort(axis=1) + 1
                    ligne[f"delta_{d:g}"] = round(float(((rangs * doses[None, :]).sum(axis=1) >= seuil - 1e-9).mean()), 4)
                fiche[forme] = ligne
            sortie[f"{taille}/{nom}"] = fiche
    return sortie


def bloc_g(rng, tirages=200_000):
    sortie = {}
    for (m, n) in [(3, 3), (4, 4), (4, 5), (5, 5)]:
        uc = u_critique(m, n, NIVEAU_REPLI)["u_crit"]
        sortie[f"{m}x{n}"] = {"u_crit_95": uc, **{
            f"delta_{d:g}": (round(float((u_inverse(d + rng.standard_normal((tirages, m)),
                                                     rng.standard_normal((tirages, n))) <= uc).mean()), 4)
                             if uc is not None else 0.0) for d in DELTAS}}
    return sortie


# =============================================================================== seconde partie : familles jumelles
PAIRES_ORDONNEES = [(a, b) for a in range(3) for b in range(3) if a != b]     # (membre « saboteur », membre « jumeau »)


def rang_permutation_familles(t: np.ndarray) -> np.ndarray:
    """t : (R, K, 3) statistiques des trois membres de K familles, colonnes [jumeau, demi-saboteur, saboteur].
    Statistique : somme sur les familles de (saboteur moins jumeau). Référence : les 6^K façons de désigner, dans
    chaque famille, lequel des trois membres est le « saboteur » et lequel est le « jumeau ». Rend, par tirage, le nombre
    d'affectations dont la statistique est au moins égale à l'observée (l'observée comprise)."""
    r_, k_, _ = t.shape
    diffs = np.stack([t[:, :, a] - t[:, :, b] for a, b in PAIRES_ORDONNEES], axis=2)        # (R, K, 6)
    obs = (t[:, :, 2] - t[:, :, 0]).sum(axis=1)
    k1 = k_ // 2

    def sommes(bloc):                                     # (R, k, 6) -> (R, 6^k) toutes les sommes
        s = np.zeros((r_, 1))
        for j in range(bloc.shape[1]):
            s = (s[:, :, None] + bloc[:, j, None, :]).reshape(r_, -1)
        return s

    a = sommes(diffs[:, :k1, :])
    b = np.sort(sommes(diffs[:, k1:, :]), axis=1)
    compte = np.empty(r_, dtype=np.int64)
    nb = b.shape[1]
    for i in range(r_):
        compte[i] = int((nb - np.searchsorted(b[i], obs[i] - a[i] - 1e-12, side="left")).sum())
    return compte


def seuil_compte(k: int, membres: int = 3, niveau: float = NIVEAU_UNILATERAL) -> int:
    """Plus grand nombre d'affectations « au moins aussi extrêmes » compatible avec le niveau unilatéral."""
    return int(math.floor(niveau * (membres * (membres - 1)) ** k + 1e-9))


@functools.lru_cache(maxsize=None)
def seuil_rangs_signes(k: int, niveau: float = NIVEAU_UNILATERAL):
    """Épreuve des rangs signés de Wilcoxon exacte sur k paires : plus grande somme des rangs négatifs admise."""
    loi = np.zeros(k * (k + 1) // 2 + 1, dtype=object)
    loi[0] = 1
    for r in range(1, k + 1):
        nouveau = loi.copy()
        nouveau[r:] += loi[:-r]
        loi = nouveau
    total, cumul, crit = 2 ** k, 0, None
    for w, c in enumerate(loi):
        cumul += int(c)
        if cumul / total <= niveau:
            crit = w
        else:
            break
    return crit


def bloc_h(rng, tirages=20_000):
    sortie = {"tables": {}}
    for k in range(3, 11):
        s3 = seuil_compte(k, 3)
        sortie["tables"][f"{k}_familles"] = {
            "trois_membres_affectations": 6 ** k, "trois_membres_p_minimale": 1.0 / 6 ** k,
            "trois_membres_compte_admis_99": s3, "trois_membres_atteint_99": s3 >= 1,
            "saboteur_en_tete_et_jumeau_en_queue_partout_p": (1.0 / 6) ** k,
            "saboteur_en_tete_partout_p": (1.0 / 3) ** k,
            "deux_membres_affectations": 2 ** k, "deux_membres_p_minimale": 1.0 / 2 ** k,
            "deux_membres_rangs_signes_somme_negative_admise_99": seuil_rangs_signes(k),
            "borne_haute_de_la_mediane_par_le_maximum_confiance_unilaterale": 1.0 - 1.0 / 2 ** k}
    formes = {"lineaire": 0.5, "seuil_haut": 0.0, "saturee": 1.0}
    for loi in ("normale", "student3"):
        for forme, h in formes.items():
            for k in (4, 5, 6, 7, 8):
                ligne3, ligne2 = {}, {}
                s3, s2 = seuil_compte(k, 3), seuil_rangs_signes(k)
                for d in (0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0):
                    beta = d * math.sqrt(2.0)                    # d = écart saboteur moins jumeau, en écarts types de cette différence
                    t = bruit(rng, (tirages, k, 3), loi)
                    t[:, :, 1] += beta * h
                    t[:, :, 2] += beta
                    ligne3[f"ecart_{d:g}"] = round(float((rang_permutation_familles(t) <= s3).mean()), 4) if s3 >= 1 else 0.0
                    if s2 is None:
                        ligne2[f"ecart_{d:g}"] = 0.0
                    else:
                        dd = t[:, :, 2] - t[:, :, 0]
                        rg = np.abs(dd).argsort(axis=1).argsort(axis=1) + 1
                        ligne2[f"ecart_{d:g}"] = round(float(((rg * (dd < 0)).sum(axis=1) <= s2).mean()), 4)
                sortie[f"{loi}/{forme}/{k}_familles/trois_membres_permutation"] = ligne3
                if forme == "lineaire":
                    sortie[f"{loi}/{k}_familles/deux_membres_rangs_signes"] = ligne2
    return sortie


def monde_familles(rng, p, k_app, k_test, signal, divergence, force=0.0, bruit_action=1.0):
    """Un monde inventé, familles jumelles. Les trois membres d'une famille partagent épisodes, graine de départ et
    ordre d'apprentissage : leur déplacement moyen partage une base b_k = a_k*g + u_k ; chaque membre s'en écarte d'une
    divergence propre e (norme voisine de `divergence`), et de dose*signal*s (dose 0 jumeau ; 0,5 demi-saboteur ;
    1 saboteur). Monde « force » : le saboteur porte en plus dose*force fois sa base (il a plus appris, sans direction
    propre). Sonde : discriminant appris sur k_app familles d'apprentissage, saboteurs contre jumeaux.
    Rend les statistiques (k_test, 3) au nominal et à norme égale dans la famille, et la séparation apprise."""
    g = np.zeros(p); g[0] = 1.0
    s = np.zeros(p); s[1] = 1.0
    n_act = 640

    def familles(k):
        a = np.exp(0.15 * rng.standard_normal(k))
        base = a[:, None] * g[None, :] + rng.standard_normal((k, p)) / math.sqrt(p)
        membres = []
        for dose in (0.0, 0.5, 1.0):
            e = divergence * rng.standard_normal((k, p)) / math.sqrt(p)
            membres.append(base * (1.0 + dose * force) + dose * signal * s[None, :] + e)
        return np.stack(membres, axis=1)                                   # (k, 3, p)

    est = lambda x: x + bruit_action * rng.standard_normal(x.shape) / math.sqrt(n_act)
    app, test = familles(k_app), familles(k_test)
    w = discriminant(est(app[:, 2, :]), est(app[:, 0, :]), bruit_action)
    note = lambda x: x @ w + bruit_action * rng.standard_normal(x.shape[:-1]) / math.sqrt(n_act)
    d_app = float((note(app[:, 2, :]) - note(app[:, 0, :])).mean())        # séparation apprise, tâches neuves
    nominal = note(test)
    normes = np.linalg.norm(test, axis=2, keepdims=True)
    egal = note(test * (normes[:, :1, :] / normes))                        # chaque membre ramené à la norme de son jumeau
    return nominal, egal, d_app


def bloc_i(rng, mondes=400):
    sortie = {}
    cas = {"aucun_effet_du_cout": dict(signal=0.0, force=0.0), "sabotage_0,1": dict(signal=0.1, force=0.0),
           "sabotage_0,25": dict(signal=0.25, force=0.0), "sabotage_0,5": dict(signal=0.5, force=0.0),
           "force_seule_0,2": dict(signal=0.0, force=0.2)}
    for nom_cas, par in cas.items():
        for divergence in (0.25, 1.0):
            for p in (16, 256):
                for k_app in (1, 2, 3):
                    nominal = np.empty((mondes, 8, 3)); egal = np.empty((mondes, 8, 3)); d_app = np.empty(mondes)
                    for i in range(mondes):
                        nominal[i], egal[i], d_app[i] = monde_familles(rng, p, k_app, 8, divergence=divergence, **par)
                    for k in (5, 6, 8):
                        seuil = seuil_compte(k, 3)
                        sab = rang_permutation_familles(nominal[:, :k, :]) <= seuil
                        sab_egal = rang_permutation_familles(egal[:, :k, :]) <= seuil
                        d = nominal[:, :k, 2] - nominal[:, :k, 0]
                        emp = (~sab) & (d_app > 0) & (d.max(axis=1) < 0.5 * d_app)
                        ecart = d.mean(axis=1) / np.maximum(d.std(axis=1, ddof=1), 1e-12)
                        sortie[f"{nom_cas}/divergence_{divergence:g}/p_{p}/{k_app}_familles_d_apprentissage/{k}_familles_tenues_a_l_ecart"] = {
                            "sabotage": round(float(sab.mean()), 4), "sabotage_a_norme_egale": round(float(sab_egal.mean()), 4),
                            "empreinte": round(float(emp.mean()), 4),
                            "non_etabli": round(float((~sab & ~emp).mean()), 4),
                            "ecart_median_dans_la_famille": round(float(np.median(ecart)), 2)}
    return sortie


def main():
    t0 = time.time()
    r = graines(10)
    sortie = {"avertissement": "lois inventées ; aucune donnée du programme ; planification seulement",
              "entropie": hex(ENTROPIE), "niveau_unilateral": NIVEAU_UNILATERAL, "numpy": np.__version__}
    sortie["A_non_apparie_tables_exactes"] = bloc_a()
    sortie["B_non_apparie_puissance_une_comparaison"] = bloc_b(r[1])
    sortie["C_non_apparie_puissance_conjonction"] = bloc_c(r[2])
    sortie["D_non_apparie_faux_sabotage_si_echangeables"] = bloc_d(r[3])
    sortie["E_non_apparie_monde_d_activations"] = bloc_e(r[4])
    sortie["F_gradient_par_part_d_episodes_contre_deux_groupes"] = bloc_f(r[5])
    sortie["G_non_apparie_repli_95"] = bloc_g(r[6])
    sortie["H_familles_jumelles_tables_et_puissance"] = bloc_h(r[7])
    sortie["I_familles_jumelles_monde_d_activations"] = bloc_i(r[8])
    sortie["duree_s"] = round(time.time() - t0, 1)
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1, default=float)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
