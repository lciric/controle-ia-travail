#!/usr/bin/env python3
"""Barreau 5, plan d'avant l'entretien : puissance et pièges des plans à plusieurs adaptateurs tenus à l'écart (v3).

Version 3, écrite par le rédacteur de la reprise (19 novembre 2026, après l'arrêt du premier rédacteur). Elle part de la
copie scellée de la version 2 inachevée (`etat-a-l-arret-quota-fable-20261119-1440Z/`, empreinte 80c9b718…), jamais
jouée. Blocs A à I : texte de la version 2, inchangé (mêmes graines : A à H rendent les chiffres de la version 1 ; I
porte la correction de la version 2, l'issue « empreinte » exige tous les écarts sous la moitié de la séparation apprise
en valeur absolue). Blocs neufs :
  J  validité de l'épreuve du brouillon 1 (permutation des trois membres, 6^K affectations) quand les trois membres ne
     sont PAS échangeables sous l'hypothèse nulle (l'édition du coût perturbe l'apprentissage sans direction, d'autant
     plus que l'édition est grande), comparée à l'épreuve des rangs signés sur la seule différence saboteur moins jumeau ;
  K  le plan retenu au brouillon 2 : rangs signés exacts sur K familles (tables, puissance), et la conjonction avec le
     qualificatif « au-delà de l'édition » (sur-saboteur moins jumeau, tous deux édités à la même distance) ;
  L  monde d'activations du plan retenu (jumeau, saboteur, sur-saboteur), avec un monde « artefact d'édition » ;
  M  épreuve à vérité plantée : probabilité qu'un programme JUSTE manque une de ses règles (lois binomiales exactes).

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
                        # issue « empreinte » du texte : tous les écarts des familles tenues à l'écart sous la moitié de la séparation apprise
                        emp = (~sab) & (d_app > 0) & (np.abs(d).max(axis=1) < 0.5 * d_app)
                        ecart = d.mean(axis=1) / np.maximum(d.std(axis=1, ddof=1), 1e-12)
                        sortie[f"{nom_cas}/divergence_{divergence:g}/p_{p}/{k_app}_familles_d_apprentissage/{k}_familles_tenues_a_l_ecart"] = {
                            "sabotage": round(float(sab.mean()), 4), "sabotage_a_norme_egale": round(float(sab_egal.mean()), 4),
                            "empreinte": round(float(emp.mean()), 4),
                            "non_etabli": round(float((~sab & ~emp).mean()), 4),
                            "ecart_median_dans_la_famille": round(float(np.median(ecart)), 2)}
    return sortie

# ================================================================================= blocs neufs de la version 3
def rangs_signes_moins(d: np.ndarray) -> np.ndarray:
    """Somme des rangs (de |d|) des différences négatives, par tirage. d : (R, K)."""
    rg = np.abs(d).argsort(axis=1).argsort(axis=1) + 1
    return (rg * (d < 0)).sum(axis=1)


def loi_rangs_signes(k: int):
    loi = np.zeros(k * (k + 1) // 2 + 1, dtype=object)
    loi[0] = 1
    for r in range(1, k + 1):
        nouveau = loi.copy()
        nouveau[r:] += loi[:-r]
        loi = nouveau
    return loi


def membres_nuls(rng, tirages, k, nul, loi="normale"):
    """Trois membres [jumeau, tiers, saboteur] sous une hypothèse nulle SANS direction (aucun effet systématique du coût).
    `echange` : bruits indépendants de même loi (échange complet).
    `marche_demi` : le tiers est un demi-saboteur, à mi-chemin de l'édition ; la divergence d'apprentissage croît avec la
        distance d'édition (marche : jumeau -> demi -> saboteur, pas de variance 1/2 chacun).
    `marche_sur` : le tiers est un sur-saboteur (coût triplé) ; marche jumeau -> saboteur -> sur-saboteur (pas de variance 1).
    `edites_plus_bruyants` : les membres édités (jumeau, tiers) portent un bruit d'écart type 2, le saboteur 1."""
    e = bruit(rng, (tirages, k, 3), loi)
    t = np.empty_like(e)
    if nul == "echange":
        t[:] = e
    elif nul == "marche_demi":
        t[:, :, 0] = 0.0
        t[:, :, 1] = math.sqrt(0.5) * e[:, :, 1]
        t[:, :, 2] = t[:, :, 1] + math.sqrt(0.5) * e[:, :, 2]
    elif nul == "marche_sur":
        t[:, :, 0] = 0.0
        t[:, :, 2] = e[:, :, 2]
        t[:, :, 1] = t[:, :, 2] + e[:, :, 1]
    elif nul == "edites_plus_bruyants":
        t[:, :, 0] = 2.0 * e[:, :, 0]
        t[:, :, 1] = 2.0 * e[:, :, 1]
        t[:, :, 2] = e[:, :, 2]
    else:
        raise ValueError(nul)
    return t


def bloc_j(rng, tirages=20_000):
    """Taux de « séparé » (un sens, niveau visé 0,005) sous quatre hypothèses nulles sans direction."""
    sortie = {}
    for nul in ("echange", "marche_demi", "marche_sur", "edites_plus_bruyants"):
        for loi in ("normale", "student3"):
            ligne = {}
            for k in (5, 6, 8):
                t = membres_nuls(rng, tirages, k, nul, loi)
                ligne[f"{k}_familles/permutation_des_trois_membres_6^K"] = round(
                    float((rang_permutation_familles(t) <= seuil_compte(k, 3)).mean()), 4)
            for k in (8, 9, 10, 12):
                t = membres_nuls(rng, 200_000, k, nul, loi)
                d = t[:, :, 2] - t[:, :, 0]
                ligne[f"{k}_familles/rangs_signes_saboteur_moins_jumeau"] = round(
                    float((rangs_signes_moins(d) <= seuil_rangs_signes(k)).mean()), 5)
            sortie[f"{nul}/{loi}"] = ligne
    return sortie


DELTAS_K = (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0)


def bloc_k(rng, tirages=200_000):
    sortie = {"tables": {}}
    for k in range(5, 15):
        loi = loi_rangs_signes(k)
        total = 2 ** k
        crit = seuil_rangs_signes(k)
        crit95 = seuil_rangs_signes(k, NIVEAU_REPLI)
        sortie["tables"][f"{k}_familles"] = {
            "affectations_2^K": total, "p_minimale_un_sens": 1.0 / total,
            "niveau_bilateral_le_plus_fort_atteignable": 1.0 - 2.0 / total,
            "somme_des_rangs_contraires_admise_99": crit,
            "affectations_admises_99": (int(sum(loi[: crit + 1])) if crit is not None else 0),
            "p_un_sens_au_seuil_99": (int(sum(loi[: crit + 1])) / total if crit is not None else None),
            "somme_des_rangs_contraires_admise_95": crit95,
            "p_un_sens_au_seuil_95": (int(sum(loi[: crit95 + 1])) / total if crit95 is not None else None),
            "erreur_de_l_issue_empreinte_2^-K": 1.0 / total,
            "confiance_de_l_etendue_min_max_pour_la_mediane": 1.0 - 2.0 / total}
    # puissance de l'épreuve décisive : d_k = écart + bruit d'écart type 1 (unité : écart type de la différence saboteur moins jumeau)
    for loi in ("normale", "student3"):
        for k in (8, 9, 10, 11, 12):
            crit = seuil_rangs_signes(k)
            sortie[f"puissance_99/{loi}/{k}_familles"] = {
                f"ecart_{d:g}": round(float((rangs_signes_moins(d + bruit(rng, (tirages, k), loi)) <= crit).mean()), 4)
                for d in DELTAS_K}
        for k in (5, 6, 7, 8):
            crit = seuil_rangs_signes(k, NIVEAU_REPLI)
            sortie[f"puissance_95_pour_memoire/{loi}/{k}_familles"] = {
                f"ecart_{d:g}": (round(float((rangs_signes_moins(d + bruit(rng, (tirages, k), loi)) <= crit).mean()), 4)
                                 if crit is not None else 0.0) for d in DELTAS_K}
    # hétérogénéité : l'écart vrai varie d'une famille à l'autre (écart type tau), K = 10
    for tau in (0.5, 1.0):
        sortie[f"puissance_99/normale/10_familles/ecart_heterogene_tau_{tau:g}"] = {
            f"ecart_{d:g}": round(float((rangs_signes_moins(
                d + tau * rng.standard_normal((tirages, 10)) + rng.standard_normal((tirages, 10))) <= seuil_rangs_signes(10)).mean()), 4)
            for d in DELTAS_K}
    # conjonction avec le qualificatif « au-delà de l'édition » : membres [jumeau, saboteur, sur-saboteur], bruit de
    # membre d'écart type 1/sqrt(2) ; effet du saboteur = d ; effet du sur-saboteur = rapport * d.
    for k in (8, 10):
        crit = seuil_rangs_signes(k)
        for nom, rapport in (("sur_saboteur_egal_au_jumeau_artefact_d_edition_pur", 0.0),
                             ("sur_saboteur_egal_au_saboteur_reponse_saturee", 1.0),
                             ("sur_saboteur_a_1,5_fois", 1.5), ("sur_saboteur_au_double_reponse_graduee", 2.0)):
            ligne = {}
            for d in (0.0, 1.0, 1.5, 2.0, 3.0, 4.0):
                e = rng.standard_normal((tirages, k, 3)) / math.sqrt(2.0)
                s = rangs_signes_moins(d + e[:, :, 1] - e[:, :, 0]) <= crit
                q = rangs_signes_moins(rapport * d + e[:, :, 2] - e[:, :, 0]) <= crit
                ligne[f"ecart_{d:g}"] = {"sabotage": round(float(s.mean()), 4), "au_dela_de_l_edition": round(float(q.mean()), 4),
                                         "les_deux": round(float((s & q).mean()), 4)}
            sortie[f"conjonction/{k}_familles/{nom}"] = ligne
    return sortie


def monde_retenu(rng, p, k_app, k_test, signal, divergence, force=0.0, artefact=0.0, reponse_sur=2.0, bruit_action=1.0):
    """Monde inventé du plan retenu. Membres d'une famille : jumeau (coût ramené au niveau honnête, édité), saboteur (non
    édité), sur-saboteur (coût triplé, édité). Base commune b_k = a_k*g + u_k ; divergence propre par membre ; le coût
    porte niveau*signal*s (niveau 0, 1, reponse_sur) ; `force` : le membre porte niveau*force fois sa base ; `artefact` :
    les membres édités portent artefact*m (direction de « l'édition », sans rapport avec le niveau du coût).
    Sonde : discriminant appris sur k_app familles d'apprentissage (saboteur contre jumeau, deux membres)."""
    g = np.zeros(p); g[0] = 1.0
    s = np.zeros(p); s[1] = 1.0
    m = np.zeros(p); m[2] = 1.0
    n_act = 640

    def familles(k):
        a = np.exp(0.15 * rng.standard_normal(k))
        base = a[:, None] * g[None, :] + rng.standard_normal((k, p)) / math.sqrt(p)
        membres = []
        for niveau, edite in ((0.0, 1.0), (1.0, 0.0), (reponse_sur, 1.0)):
            e = divergence * rng.standard_normal((k, p)) / math.sqrt(p)
            membres.append(base * (1.0 + niveau * force) + niveau * signal * s[None, :] + edite * artefact * m[None, :] + e)
        return np.stack(membres, axis=1)                                   # (k, 3, p) : jumeau, saboteur, sur-saboteur

    est = lambda x: x + bruit_action * rng.standard_normal(x.shape) / math.sqrt(n_act)
    app, test = familles(k_app), familles(k_test)
    w = discriminant(est(app[:, 1, :]), est(app[:, 0, :]), bruit_action)
    note = lambda x: x @ w + bruit_action * rng.standard_normal(x.shape[:-1]) / math.sqrt(n_act)
    d_app = float((note(app[:, 1, :]) - note(app[:, 0, :])).mean())
    nominal = note(test)
    normes = np.linalg.norm(test, axis=2, keepdims=True)
    egal = note(test * (normes[:, :1, :] / normes))
    return nominal, egal, d_app


def bloc_l(rng, mondes=400):
    sortie = {}
    cas = {"aucun_effet_du_cout": dict(signal=0.0), "sabotage_0,1": dict(signal=0.1), "sabotage_0,25": dict(signal=0.25),
           "sabotage_0,5": dict(signal=0.5), "force_seule_0,2": dict(signal=0.0, force=0.2),
           "artefact_d_edition_0,5_sans_sabotage": dict(signal=0.0, artefact=0.5),
           "sabotage_0,25_et_artefact_0,5": dict(signal=0.25, artefact=0.5),
           "sabotage_0,25_reponse_saturee": dict(signal=0.25, reponse_sur=1.0)}
    for nom_cas, par in cas.items():
        for divergence in (0.25, 1.0):
            for p in (16, 256):
                for k_app in (2, 3):
                    nominal = np.empty((mondes, 10, 3)); egal = np.empty((mondes, 10, 3)); d_app = np.empty(mondes)
                    for i in range(mondes):
                        nominal[i], egal[i], d_app[i] = monde_retenu(rng, p, k_app, 10, divergence=divergence, **par)
                    for k in (8, 10):
                        crit = seuil_rangs_signes(k)
                        d = nominal[:, :k, 1] - nominal[:, :k, 0]
                        sab = rangs_signes_moins(d) <= crit
                        contraire = rangs_signes_moins(-d) <= crit
                        q1 = rangs_signes_moins(egal[:, :k, 1] - egal[:, :k, 0]) <= crit
                        q2 = rangs_signes_moins(nominal[:, :k, 2] - nominal[:, :k, 0]) <= crit
                        emp = (~sab) & (~contraire) & (d_app > 0) & (np.abs(d).max(axis=1) < 0.5 * d_app)
                        ecart = d.mean(axis=1) / np.maximum(d.std(axis=1, ddof=1), 1e-12)
                        sortie[f"{nom_cas}/divergence_{divergence:g}/p_{p}/{k_app}_familles_d_apprentissage/{k}_familles_tenues_a_l_ecart"] = {
                            "sabotage": round(float(sab.mean()), 4), "contraire": round(float(contraire.mean()), 4),
                            "sabotage_et_direction_a_norme_egale": round(float((sab & q1).mean()), 4),
                            "sabotage_et_au_dela_de_l_edition": round(float((sab & q2).mean()), 4),
                            "empreinte": round(float(emp.mean()), 4),
                            "non_etabli": round(float((~sab & ~contraire & ~emp).mean()), 4),
                            "ecart_median_dans_la_famille": round(float(np.median(ecart)), 2)}
    return sortie


def queue_binomiale_haute(n: int, p: float, x: int) -> float:
    """P(X >= x), X binomiale (n, p)."""
    if x <= 0:
        return 1.0
    q = 0.0
    for i in range(x, n + 1):
        q += math.exp(math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
                      + (i * math.log(p) if p > 0 else (0.0 if i == 0 else -math.inf))
                      + ((n - i) * math.log1p(-p) if p < 1 else (0.0 if i == n else -math.inf)))
    return min(1.0, q)


def bloc_m(k_sortie):
    """Probabilité qu'un programme juste manque une règle de l'épreuve à vérité plantée (10 familles, rangs signés)."""
    p0 = k_sortie["tables"]["10_familles"]["p_un_sens_au_seuil_99"]
    pu = k_sortie["puissance_99/normale/10_familles"]
    conj = k_sortie["conjonction/10_familles/sur_saboteur_egal_au_jumeau_artefact_d_edition_pur"]
    r = {"V0_taux_vrai_par_sens": p0,
         "V0_plus_de_20_sur_2000_dans_un_sens": queue_binomiale_haute(2000, p0, 21),
         "V0_plus_de_22_sur_2000_dans_un_sens": queue_binomiale_haute(2000, p0, 23),
         "V1_ecart_3_puissance": pu["ecart_3"],
         "V1_moins_de_480_sur_500": 1.0 - queue_binomiale_haute(500, pu["ecart_3"], 480),
         "V1bis_ecart_2_puissance": pu["ecart_2"],
         "V1bis_moins_de_440_sur_500": 1.0 - queue_binomiale_haute(500, pu["ecart_2"], 440),
         "V2_artefact_pur_ecart_4_sabotage": conj["ecart_4"]["sabotage"],
         "V2_artefact_pur_ecart_4_au_dela_de_l_edition_a_tort": conj["ecart_4"]["au_dela_de_l_edition"],
         "V2_plus_de_10_qualificatifs_a_tort_sur_500": queue_binomiale_haute(500, conj["ecart_4"]["au_dela_de_l_edition"], 11)}
    return r


def main():
    t0 = time.time()
    r = graines(14)
    sortie = {"avertissement": "lois inventées ; aucune donnée du programme ; planification seulement",
              "entropie": hex(ENTROPIE), "niveau_unilateral": NIVEAU_UNILATERAL, "numpy": np.__version__}
    if "--neufs-seulement" not in sys.argv:
        sortie["A_non_apparie_tables_exactes"] = bloc_a()
        sortie["B_non_apparie_puissance_une_comparaison"] = bloc_b(r[1])
        sortie["C_non_apparie_puissance_conjonction"] = bloc_c(r[2])
        sortie["D_non_apparie_faux_sabotage_si_echangeables"] = bloc_d(r[3])
        sortie["E_non_apparie_monde_d_activations"] = bloc_e(r[4])
        sortie["F_gradient_par_part_d_episodes_contre_deux_groupes"] = bloc_f(r[5])
        sortie["G_non_apparie_repli_95"] = bloc_g(r[6])
        sortie["H_familles_jumelles_tables_et_puissance"] = bloc_h(r[7])
        sortie["I_familles_jumelles_monde_d_activations"] = bloc_i(r[8])
    sortie["J_validite_sous_des_nuls_sans_echange_a_trois"] = bloc_j(r[10])
    sortie["K_plan_retenu_rangs_signes"] = bloc_k(r[11])
    sortie["L_plan_retenu_monde_d_activations"] = bloc_l(r[12])
    sortie["M_epreuve_a_verite_plantee_regles"] = bloc_m(sortie["K_plan_retenu_rangs_signes"])
    sortie["duree_s"] = round(time.time() - t0, 1)
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1, default=float)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
