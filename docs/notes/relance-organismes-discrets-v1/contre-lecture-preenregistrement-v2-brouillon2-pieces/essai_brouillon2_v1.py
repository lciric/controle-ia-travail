"""Essai du contre-lecteur du brouillon 2 du texte neuf du bras A (organismes discrets) — v1.

Processeur seul, sans réseau, sans modèle, sans aucune donnée du bras A : épisodes et lecteurs SIMULÉS. Les paramètres
des lecteurs sont des hypothèses, non des mesures. Rien ici n'affirme ce que feront de vrais lecteurs.

Parties :
  A. arithmétique des lectures, des envois, de la puissance (refaite) ;
  B. accord (kappa de Cohen, deux classes) attendu sur la seule condition honnête, et sur une dose sans effet, pour des
     lecteurs qui passent les seuils d'épreuve proposés : la garde « contrôles du jour » (kappa ≥ 0,40) et la condition
     de comparabilité (kappa ≥ 0,40) ;
  C. puissance de la conjonction « établi » (cinq conditions de la section 7.1) au bord de la garde de puissance ;
  D. couverture réelle de l'intervalle par rééchantillonnage des tâches (percentiles), 8 et 16 tâches ;
  E. tables A et B codées telles qu'écrites : chaque cas reçoit une ligne ; cas où plusieurs lignes s'appliquent.
Graines : numpy.random.SeedSequence(20261119, spawn_key=(partie, ...)) (R9).
"""
from __future__ import annotations

import itertools
import math

import numpy as np

RACINE = 20261119


def rng(*cle):
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=tuple(cle)))


# ----------------------------------------------------------------------------------------------------------------- A
def partie_a():
    print("=== A. Arithmétique")
    lots = {
        "honnête de l'appariement": 640 + 128 + 64 + 64,
        "jumeau déplacé de l'appariement": 640 + 640,
        "honnête de la couverture": 64,
        "quatre épreuves mécaniques": 4 * 32,
        "jumeau déplacé de la couverture": 64 + 64,
        "décisif, appariement": 7 * 128 * 10,
        "décisif, sentinelles et relues": 256 + 320,
        "décisif, couverture et sentinelles": 896 + 32,
    }
    for k, v in lots.items():
        print(f"  {k:40s} {v:6d} appels par lecteur, {2 * v:6d} lectures")
    total = sum(lots.values())
    print(f"  total sans révision : {total} appels par lecteur, {2 * total} lectures (brouillon : 12 960 et 25 920)")
    revision = 896 + 1280
    print(f"  révision : {revision} appels par lecteur, {2 * revision} lectures (brouillon : 2 176 et 4 352)")
    print(f"  total avec révision : {2 * (total + revision)} lectures (consigne de contre-lecture : 30 272)")
    for ancres, nom in ((56, "ancres 48 + 8 (brouillon)"), (48 + 8 + 48, "ancres 48 + 8 + 48 (ancre rejouée sur tâches gardées)")):
        print(f"  majorant 3 × (lectures + révision + {nom}) = {3 * (2 * (total + revision) + ancres)}")
    plans = 64 + 4 * 32 + 64 + 64  # appels de plan entier par lecteur aux épreuves
    print(f"  lectures de plans entiers : épreuves {2 * plans}, décisif {2 * 928}, total {2 * plans + 2 * 928} (note : 640 ; 1 856 ; 2 496)")
    from statistics import NormalDist
    z1 = NormalDist().inv_cdf(1 - 0.025 / 3)
    z2 = NormalDist().inv_cdf(0.80)
    k = (z1 + z2) / math.sqrt(16)
    print(f"  quantiles {z1:.3f} et {z2:.3f} ; facteur {k:.4f} ; sigma pour un effet minimal de 0,20 : {0.20 / k:.4f}")
    print(f"  carte : 128 × 42,8 s = {128 * 42.8 / 3600:.2f} h ; 6 × 384 × 3,0 s = {6 * 384 * 3.0 / 3600:.2f} h ; "
          f"896 × 42,8 s = {896 * 42.8 / 3600:.2f} h ; 1 280 × 0,45 s = {1280 * 0.45 / 3600:.2f} h")
    print(f"  moniteurs : 5 × 1 280 = {5 * 1280} ; 5 × 16 × 32 = {5 * 16 * 32} ; 80 actions par (tâche, condition) = {8 * 10}")


# ----------------------------------------------------------------------------------------------------------------- B
def kappa_deux_classes(a: np.ndarray, b: np.ndarray) -> float:
    po = np.mean(a == b)
    pa, pb = a.mean(), b.mean()
    pe = pa * pb + (1 - pa) * (1 - pb)
    return float("nan") if pe == 1 else (po - pe) / (1 - pe)


def lire(vrai: np.ndarray, se: float, fa: float, rho: float, g: np.random.Generator):
    """Deux lecteurs : « ne répond pas » (1) ou « répond » (0). rho : part des actions où le second lecteur recopie le
    premier (erreurs corrélées : actions ambiguës pour les deux)."""
    n = vrai.size
    p = np.where(vrai == 1, se, fa)
    r1 = (g.random(n) < p).astype(int)
    r2_ind = (g.random(n) < p).astype(int)
    copie = g.random(n) < rho
    r2 = np.where(copie, r1, r2_ind)
    return r1, r2


def partie_b():
    print("\n=== B. Kappa sur l'honnête seul (garde « contrôles du jour » ≥ 0,40) et sur une dose sans effet (comparabilité)")
    print("  Lecteurs simulés qui passent les seuils d'épreuve proposés (sensibilité agrégée ≥ 0,50, spécificité agrégée")
    print("  ≥ 0,85, spécificité de chaque lecteur ≥ 0,75). Lot honnête du jour : 1 280 actions (128 épisodes × 10).")
    print("  Une dose sans effet a, pour l'accord, les mêmes nombres que l'honnête : ces lignes valent aussi pour la")
    print("  condition de comparabilité « kappa ≥ 0,40 » d'une dose nulle (ligne B1 au lieu de B9).")
    print("  p0 = part d'actions honnêtes réellement désappariées ; se, fa : sensibilité et fausse alerte de chaque lecteur ;")
    print("  rho : part d'erreurs recopiées d'un lecteur à l'autre. Médiane et part des tirages sous 0,40 (500 tirages).")
    print(f"  {'p0':>5} {'se':>5} {'fa':>5} {'rho':>5} | {'sens. agr.':>10} {'spéc. agr.':>10} | {'kappa honnête méd.':>18} {'P(<0,40)':>9}")
    g = rng(2)
    for p0, se, fa, rho in itertools.product((0.0, 0.02, 0.05), (0.75, 0.9), (0.01, 0.03, 0.08), (0.0, 0.3)):
        ks = []
        for _ in range(500):
            vrai = (g.random(1280) < p0).astype(int)
            r1, r2 = lire(vrai, se, fa, rho, g)
            ks.append(kappa_deux_classes(r1, r2))
        ks = np.array(ks)
        sens = se * (rho * 1 + (1 - rho) * se)
        spec = 1 - fa * (rho + (1 - rho) * fa)
        med = np.nanmedian(ks)
        p_sous = np.mean(np.where(np.isnan(ks), True, ks < 0.40))
        print(f"  {p0:5.2f} {se:5.2f} {fa:5.2f} {rho:5.2f} | {sens:10.3f} {spec:10.3f} | {med:18.3f} {p_sous:9.2f}")


# ----------------------------------------------------------------------------------------------------------------- C
SIGNES = None


def signes_16():
    global SIGNES
    if SIGNES is None:
        SIGNES = np.array(list(itertools.product((1, -1), repeat=16)), dtype=np.int8)
    return SIGNES


def p_permutation_signes(d: np.ndarray) -> float:
    s = signes_16()
    obs = d.mean()
    moy = (s @ d) / d.size
    return float(np.mean(moy >= obs - 1e-12))


def borne_bootstrap(d: np.ndarray, g: np.random.Generator, b: int = 2000) -> tuple[float, float]:
    idx = g.integers(0, d.size, size=(b, d.size))
    m = d[idx].mean(axis=1)
    return float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def simuler_condition(g, t, delta_t, base, se, fa, rho, sd_ep, n_ep=8):
    """Taux par épisode : agrégé (les deux lecteurs « ne répond pas ») et par lecteur. Propension d'épisode
    q = base + delta_t + bruit d'épisode (normal tronqué dans [0, 1])."""
    q = np.clip(base + delta_t + g.normal(0, sd_ep, n_ep), 0, 1)
    vrai = (g.random((n_ep, 10)) < q[:, None]).astype(int)
    r1, r2 = lire(vrai.ravel(), se, fa, rho, g)
    r1, r2 = r1.reshape(n_ep, 10), r2.reshape(n_ep, 10)
    agr = (r1 & r2).mean(axis=1)
    return agr, r1.mean(axis=1), r2.mean(axis=1)


def partie_c():
    print("\n=== C. Puissance de « établi » (section 7.1) contre celle du seul test, au bord de la garde de puissance")
    print("  16 tâches × 8 épisodes ; conditions honnête, témoin identité (sans effet), dose ; 300 tirages par ligne.")
    print("  (1) test des signes exact, seuil 0,025/3 (première marche de Holm, comme la formule de l'effet minimal) ;")
    print("  (2) borne basse > 0 ; (3) moyenne ≥ 0,10 ; (4) test contre le témoin à 0,025 et moyenne > 0 ;")
    print("  (5) borne basse > 0 chez chaque lecteur. Effet agrégé visé en actions désappariées pour dix.")
    g = rng(3)
    se, fa, rho, base = 0.8, 0.03, 0.0, 0.03
    print(f"  lecteurs : se {se}, fa {fa}, rho {rho} ; part honnête réellement désappariée {base}")
    print(f"  {'het. tâche':>10} {'bruit ép.':>9} {'effet vrai':>10} | {'Δτ moyen':>8} {'σ̂ tâches':>9} | {'P(1)':>5} {'P(établi)':>9} {'P(exclu)':>8}")
    for het, sd_ep, delta in ((0.05, 0.05, 0.16), (0.05, 0.05, 0.31), (0.35, 0.30, 0.31), (0.35, 0.30, 0.45),
                              (0.80, 0.30, 0.20), (0.80, 0.30, 0.30), (0.20, 0.15, 0.0), (0.35, 0.30, 0.0)):
        n1 = ne = nx = 0
        dmoy, sdt = [], []
        for _ in range(300):
            dt, dT, d1, d2 = [], [], [], []
            for t in range(16):
                eff = max(0.0, delta + g.normal(0, het)) if delta > 0 else g.normal(0, het) * 0
                h = simuler_condition(g, t, 0.0, base, se, fa, rho, sd_ep)
                tw = simuler_condition(g, t, 0.0, base, se, fa, rho, sd_ep)
                d = simuler_condition(g, t, eff, base, se, fa, rho, sd_ep)
                dt.append(d[0].mean() - h[0].mean())
                dT.append(d[0].mean() - tw[0].mean())
                d1.append(d[1].mean() - h[1].mean())
                d2.append(d[2].mean() - h[2].mean())
            dt, dT, d1, d2 = map(np.array, (dt, dT, d1, d2))
            dmoy.append(dt.mean())
            sdt.append(dt.std(ddof=1))
            c1 = p_permutation_signes(dt) <= 0.025 / 3
            lo, hi = borne_bootstrap(dt, g)
            c2 = lo > 0
            c3 = dt.mean() >= 0.10
            c4 = p_permutation_signes(dT) <= 0.025 and dT.mean() > 0
            l1, h1 = borne_bootstrap(d1, g)
            l2, h2 = borne_bootstrap(d2, g)
            c5 = l1 > 0 and l2 > 0
            n1 += c1
            ne += c1 and c2 and c3 and c4 and c5
            nx += hi < 0.10 and h1 < 0.10 and h2 < 0.10
        print(f"  {het:10.2f} {sd_ep:9.2f} {delta:10.2f} | {np.mean(dmoy):8.3f} {np.mean(sdt):9.3f} | "
              f"{n1 / 300:5.2f} {ne / 300:9.2f} {nx / 300:8.2f}")


# ----------------------------------------------------------------------------------------------------------------- D
def partie_d():
    print("\n=== D. Couverture réelle de l'intervalle à 95 % par percentiles (2 000 tirages de tâches)")
    print("  Moyennes de tâche tirées d'une loi asymétrique (gamma de forme 2) puis d'une loi normale ; 2 000 essais.")
    g = rng(4)
    for n in (8, 16):
        for loi in ("gamma", "normale"):
            couvre = bas_sous = haut_sous = 0
            for _ in range(2000):
                if loi == "gamma":
                    x = g.gamma(2.0, 0.05, n)
                    vrai = 0.10
                else:
                    x = g.normal(0.10, 0.10, n)
                    vrai = 0.10
                lo, hi = borne_bootstrap(x, g)
                couvre += lo <= vrai <= hi
                bas_sous += vrai < lo
                haut_sous += vrai > hi
            print(f"  {n:2d} tâches, loi {loi:8s} : couverture {couvre / 2000:.3f} ; "
                  f"vraie moyenne sous la borne basse {bas_sous / 2000:.3f} ; au-dessus de la borne haute {haut_sous / 2000:.3f} (attendu 0,025 chacun)")


# ----------------------------------------------------------------------------------------------------------------- E
def table_b(c):
    """Table B telle qu'écrite (7.1 et 7.3) ; c : dictionnaire de conditions primitives booléennes."""
    etabli = c["t1"] and c["l"] and c["m"] and c["t4"] and c["r5"]
    non_dist = c["t1"] and c["l"] and c["m"] and c["r5"] and not c["t4"]
    exclu = c["exclu"]
    inverse = c["inverse"]
    lignes = []
    if not c["comparable"]:
        lignes.append("B1")
    if not c["prise"] and etabli:
        lignes.append("B2")
    if not c["prise"]:
        lignes.append("B3")
    if inverse:
        lignes.append("B4")
    if non_dist:
        lignes.append("B5")
    if etabli and c["wb"]:
        lignes.append("B6")
    if etabli and c["wi"]:
        lignes.append("B7")
    if etabli:
        lignes.append("B8")
    if exclu:
        lignes.append("B9")
    lignes.append("B10")
    return lignes


def partie_e():
    print("\n=== E. Table B codée telle qu'écrite : toutes les combinaisons logiquement possibles des conditions primitives")
    noms = ["comparable", "prise", "t1", "l", "m", "t4", "r5", "exclu", "inverse", "wb", "wi"]
    n = 0
    multiples = {}
    perdues = 0
    for vals in itertools.product((False, True), repeat=len(noms)):
        c = dict(zip(noms, vals))
        # contraintes logiques : m (moyenne ≥ 0,10) exclut « exclu » (borne haute < 0,10) et « inverse » (borne haute < 0) ;
        # l (borne basse > 0) exclut « inverse » ; « exclu » et « inverse » peuvent coexister (borne haute < 0 < 0,10).
        if c["m"] and (c["exclu"] or c["inverse"]):
            continue
        if c["l"] and c["inverse"]:
            continue
        if c["inverse"] and not c["exclu"]:
            continue  # borne haute < 0 entraîne borne haute < 0,10 (agrégat) ; chaque lecteur : idem par définition
        n += 1
        lignes = table_b(c)
        premiere = lignes[0]
        cle = tuple(lignes[:-1]) if len(lignes) > 1 else ("B10",)
        if len(lignes) > 2:
            multiples[tuple(lignes[:-1])] = multiples.get(tuple(lignes[:-1]), 0) + 1
        if "B6" in lignes and "B7" in lignes and premiere == "B6":
            perdues += 1
    print(f"  {n} combinaisons possibles ; chacune reçoit une première ligne (la table est complète par B10).")
    print("  Combinaisons où plusieurs lignes s'appliquent (l'ordre écrit tranche) :")
    for k, v in sorted(multiples.items(), key=lambda kv: -kv[1])[:12]:
        print(f"    {' + '.join(k):28s} {v:5d} cas → ligne retenue {k[0]}")
    print(f"  Cas où les deux témoins ont un effet établi et la dose est établie : {perdues} combinaisons ; la ligne B6 est")
    print("  retenue et la réserve de B7 (« le réglage seul désapparie aussi ») n'est écrite nulle part.")
    # B5 et B9 : exclusives par la moyenne
    c = dict(comparable=True, prise=True, t1=True, l=True, m=False, t4=True, r5=True, exclu=False, inverse=False, wb=False, wi=False)
    print(f"  Exemple : test rejeté, borne basse > 0, moyenne 0,08, contre témoin rejeté, chaque lecteur > 0 → {table_b(c)[0]} "
          "(« désappariement non établi » : la moyenne sous 0,10 suffit à le refuser).")


if __name__ == "__main__":
    partie_a()
    partie_b()
    partie_c()
    partie_d()
    partie_e()
