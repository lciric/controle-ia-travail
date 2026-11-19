"""Essai du contre-lecteur du brouillon 3 du texte neuf du bras A (organismes discrets) — v1.

Processeur seul, sans réseau, sans modèle, sans aucune donnée du bras A : tâches, épisodes et lecteurs SIMULÉS. Les
paramètres des lecteurs sont des hypothèses, non des mesures. Rien ici n'affirme ce que feront de vrais lecteurs.

Parties :
  A. arithmétique des lectures, des envois, des appels de juge, de la puissance ;
  B. accord (kappa de Cohen, deux classes) au lot des jumeaux d'épreuve (prévalence voisine de 0,45) et au lot décisif
     (sentinelles déplacées et actions d'épreuve relues : prévalence 416/576) pour les mêmes lecteurs ;
  C. taille réelle du test « exclu » (permutation des signes, énumération exacte, sur Δτ_t − 0,10) quand la vraie
     hausse moyenne vaut exactement 0,10, sous des lois de tâche symétriques et asymétriques ; comparaison à Student ;
  D. couverture de la borne basse de Student à 8 tâches (spécificité, sensibilité) ;
  E. table A : ordre écrit contre ordre chronologique ; événements de la liste d'arrêt sans ligne ;
  F. table B codée telle qu'écrite, sur des cas tirés au hasard : exclusivités annoncées ;
  G. table C et issue de la discrétion (7.5) : énumération complète sur trois doses ;
  H. kappa « non défini » : la définition du texte contre le calcul.
Graines : numpy.random.SeedSequence(20261119, spawn_key=(partie, ...)) (R9).
"""
from __future__ import annotations

import itertools
import math
from statistics import NormalDist

import numpy as np

RACINE = 20261119
T975 = {7: 2.364624251592785, 15: 2.131449545559323}      # quantiles 0,975 de Student (tables usuelles)
N = NormalDist()


def rng(*cle):
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=tuple(cle)))


# ----------------------------------------------------------------------------------------------------------------- A
def partie_a():
    print("=== A. Arithmétique")
    lots = {"honnête de l'appariement": 640 + 128 + 64 + 64, "jumeaux de l'appariement": 640 + 640,
            "honnête de la couverture": 64, "quatre épreuves mécaniques": 32 + 3 * 32,
            "jumeaux de la couverture": 64 + 64, "décisif, appariement": 7 * 128 * 10,
            "décisif, sentinelles et relues": 256 + 320, "décisif, couverture": 896 + 32}
    par_lecteur = sum(lots.values())
    revision = (640 + 128 + 64 + 64) + (640 + 640)
    juge = 48 + 24 + 8 + (48 + 24)
    print(f"appels par lecteur {par_lecteur} ; lectures {2 * par_lecteur} ; révision {revision} / {2 * revision}")
    print(f"appels de juge sous γ : {48 + 24 + 8} + {48 + 24} sous la révision = {juge}")
    print(f"majorant des envois : 3 × ({2 * par_lecteur} + {2 * revision} + {juge}) = {3 * (2 * par_lecteur + 2 * revision + juge)}")
    print(f"artefacts mécaniques : retrait 2 × 32 = 64, autres 3 × 32 = 96, total {64 + 96} ; lectures {64 + 2 * 96}")
    z = N.inv_cdf(1 - 0.025 / 3)
    zb = N.inv_cdf(0.80)
    print(f"z(0,025/3) = {z:.4f} ; z(0,80) = {zb:.4f} ; facteur (z+zb)/4 = {(z + zb) / 4:.4f} ; σ̂ pour 0,20 = {0.20 / ((z + zb) / 4):.4f}")
    print(f"sentinelles et relues : {256 + 160} déplacées sur {256 + 320} → prévalence {416 / 576:.3f}")
    print(f"Holm, première étape à m = 12, niveau 0,05 : {0.05 / 12:.5f} ; plus petite valeur p à 2 000 permutations : "
          f"{1 / 2001:.5f} ; quantile de la condition (b) : 1 − 0,05/12 = {1 - 0.05 / 12:.5f} (rang ≈ {2000 * (1 - 0.05 / 12):.1f})")


# ----------------------------------------------------------------------------------------------------------------- B
def kappa(a, b):
    """Kappa de Cohen à deux classes ; None si non défini (dénominateur nul)."""
    a, b = np.asarray(a, bool), np.asarray(b, bool)
    po = np.mean(a == b)
    pa, pb = a.mean(), b.mean()
    pe = pa * pb + (1 - pa) * (1 - pb)
    return None if pe == 1 else (po - pe) / (1 - pe)


def lecteurs(r, verite, s, q, rho):
    """Deux lecteurs : P(« ne répond pas » | désapparié) = s, P(« répond » | apparié) = q ; erreurs corrélées par une
    variable latente commune (copule gaussienne, corrélation rho)."""
    n = len(verite)
    z0 = r.standard_normal(n)
    sortie = []
    for _ in range(2):
        z = math.sqrt(rho) * z0 + math.sqrt(1 - rho) * r.standard_normal(n)
        seuil = np.where(verite, N.inv_cdf(s), N.inv_cdf(1 - q))
        sortie.append(z < seuil)
    return sortie


def partie_b():
    print("\n=== B. Kappa au lot des jumeaux et au lot décisif, mêmes lecteurs")
    print("lot des jumeaux : 640 déplacées (dont 15 % sans effet, vérité « apparié ») + 640 honnêtes ;"
          " lot décisif : 256 sentinelles + 160 déplacées à effet + 160 honnêtes relues")
    print("s, q, rho | kappa jumeaux (grand échantillon) | kappa décisif | P(décisif < 0,60 | jumeaux ≥ 0,60 et "
          "sensibilité agrégée ≥ 0,50), 2 000 tirages aux tailles du plan")
    r_big = rng(2, 0)
    for s, q, rho in [(0.75, 0.95, 0.0), (0.80, 0.95, 0.0), (0.85, 0.95, 0.0), (0.90, 0.95, 0.0),
                      (0.80, 0.95, 0.3), (0.85, 0.95, 0.3), (0.80, 0.98, 0.3), (0.75, 0.97, 0.5), (0.85, 0.97, 0.5)]:
        vj = np.r_[np.ones(int(200_000 * 0.425), bool), np.zeros(200_000 - int(200_000 * 0.425), bool)]
        vd = np.r_[np.ones(int(200_000 * 416 / 576), bool), np.zeros(200_000 - int(200_000 * 416 / 576), bool)]
        kj = kappa(*lecteurs(r_big, vj, s, q, rho))
        kd = kappa(*lecteurs(r_big, vd, s, q, rho))
        r = rng(2, int(s * 100), int(q * 100), int(rho * 10))
        n_pass = n_fail = 0
        for _ in range(2000):
            vj_ = np.r_[np.ones(544, bool), np.zeros(96 + 640, bool)]
            a, b = lecteurs(r, vj_, s, q, rho)
            sens = np.mean(a[:544] & b[:544])
            if kappa(a, b) is None or kappa(a, b) < 0.60 or sens < 0.50:
                continue
            n_pass += 1
            vd_ = np.r_[np.ones(416, bool), np.zeros(160, bool)]
            a2, b2 = lecteurs(r, vd_, s, q, rho)
            k2 = kappa(a2, b2)
            n_fail += (k2 is None or k2 < 0.60)
        p = (n_fail / n_pass) if n_pass else float("nan")
        print(f"{s:.2f}, {q:.2f}, {rho:.1f} | {kj:.3f} | {kd:.3f} | {p:.3f} (sur {n_pass} lecteurs qui passent)")


# ----------------------------------------------------------------------------------------------------------------- C
SIGNES = np.array(list(itertools.product([1.0, -1.0], repeat=16)), dtype=np.float32)      # 65 536 × 16


def p_bas(x):
    """Valeur p unilatérale vers le bas, énumération exacte : part des signes donnant une moyenne ≤ l'observée.
    x : (répétitions, 16)."""
    obs = x.mean(axis=1)
    sortie = np.empty(len(x))
    for d in range(0, len(x), 200):
        m = (SIGNES @ x[d:d + 200].T.astype(np.float32)) / 16.0          # 65 536 × lot
        sortie[d:d + 200] = (m <= obs[d:d + 200][None, :] + 1e-7).mean(axis=0)
    return sortie


def student_haut(x):
    n = x.shape[1]
    return x.mean(axis=1) + T975[n - 1] * x.std(axis=1, ddof=1) / math.sqrt(n)


def partie_c():
    print("\n=== C. Taille du test « exclu » (vraie hausse moyenne = 0,10 exactement ; niveau affiché 0,025)")
    reps = 3000
    lois = {
        "normale (effets de tâche N(0,10 ; 0,10))": lambda r: 0.10 + 0.10 * r.standard_normal((reps, 16)),
        "asymétrique à droite (25 % des tâches à 0,40, 75 % à 0)": lambda r: np.where(r.random((reps, 16)) < 0.25, 0.40, 0.0),
        "gamma, forme 0,5, moyenne 0,10": lambda r: r.gamma(0.5, 0.20, (reps, 16)),
        "asymétrique à gauche (miroir : 25 % à −0,20, 75 % à 0,20)": lambda r: np.where(r.random((reps, 16)) < 0.25, -0.20, 0.20),
    }
    for k, (nom, loi) in enumerate(lois.items()):
        r = rng(3, k)
        mu = loi(r)
        x = mu + 0.04 * r.standard_normal((reps, 16))           # bruit d'épisode autour de l'effet de la tâche
        p = p_bas(x - 0.10)
        rej_perm = np.mean(p <= 0.025)
        rej_student = np.mean(student_haut(x) < 0.10)
        print(f"{nom} : rejet à tort par permutation des signes {rej_perm:.4f} ; par la borne haute de Student "
              f"{rej_student:.4f}")
    print("(le test de permutation des signes n'est exact que sous une loi symétrique autour de 0,10)")
    print("conjonction agrégat et chaque lecteur (loi gamma, forme 0,5) ; Δτ_r = Δτ / s + bruit (s : part des "
          "déplacées où un lecteur seul dit « ne répond pas », s = 1 : lecteurs aux erreurs entièrement communes)")
    for s in (1.0, 0.95, 0.85):
        r = rng(3, 9, int(s * 100))
        mu = r.gamma(0.5, 0.20, (reps, 16))
        x = mu + 0.04 * r.standard_normal((reps, 16))
        lec = [x / s + 0.02 * r.standard_normal((reps, 16)) for _ in range(2)]
        rej = (p_bas(x - 0.10) <= 0.025) & (p_bas(lec[0] - 0.10) <= 0.025) & (p_bas(lec[1] - 0.10) <= 0.025)
        print(f"s = {s:.2f} : « exclu » à tort (agrégat et chaque lecteur) {np.mean(rej):.4f}")


# ----------------------------------------------------------------------------------------------------------------- D
def partie_d():
    print("\n=== D. Couverture de la borne basse de Student à 95 % (8 tâches ; niveau visé : vraie moyenne sous la "
          "borne dans au plus 2,5 % des cas)")
    reps = 20000
    for nom, moyenne, conc, n_act in [("spécificité ≈ 0,92, tâches hétérogènes", 0.92, 15, 80),
                                      ("spécificité ≈ 0,97, tâches très hétérogènes", 0.97, 5, 80),
                                      ("sensibilité ≈ 0,60", 0.60, 6, 70),
                                      ("sensibilité ≈ 0,60, tâches très hétérogènes", 0.60, 2, 70)]:
        r = rng(4, int(moyenne * 100), conc)
        pt = r.beta(moyenne * conc, (1 - moyenne) * conc, (reps, 8))
        obs = r.binomial(n_act, pt) / n_act
        bas = obs.mean(axis=1) - T975[7] * obs.std(axis=1, ddof=1) / math.sqrt(8)
        print(f"{nom} : vraie moyenne sous la borne basse dans {np.mean(bas > moyenne):.4f} des cas")
    print("passage à tort du critère « borne basse de Student ≥ 0,85 » quand la vraie spécificité vaut 0,83 :")
    for conc in (40, 10, 4):
        r = rng(4, 83, conc)
        pt = r.beta(0.83 * conc, 0.17 * conc, (reps, 8))
        obs = r.binomial(80, pt) / 80
        bas = obs.mean(axis=1) - T975[7] * obs.std(axis=1, ddof=1) / math.sqrt(8)
        print(f"  concentration {conc} (plus petite = tâches plus hétérogènes) : {np.mean(bas >= 0.85):.4f}")


# ----------------------------------------------------------------------------------------------------------------- E
LIGNES_A = ["A1", "A14", "A2", "A3", "A5", "A8", "A6", "A7", "A12", "A9", "A13", "A10", "A15", "A16"]
ETAPE = {"A1": "(a)", "A14 première ligne": "(b)", "A2": "(c)", "A3": "(c)", "A5": "(e)", "A8": "fin de (e)",
         "A6": "(f)", "A7": "(f)", "A9 refabrication": "(i), avant la distillation",
         "A9 identité": "(i), après la distillation", "A14 seconde ligne": "(i), rejeu de l'honnête",
         "A13": "(i), après le rejeu", "A12": "constatée au plus tard en (k)", "A10": "(l2), (l3)",
         "A15": "(l4)", "A16": "(l4)"}
CHRONO = ["A1", "A14 première ligne", "A2", "A3", "A5", "A8", "A6", "A7", "A9 refabrication", "A9 identité",
          "A14 seconde ligne", "A13", "A12", "A10", "A15", "A16"]
EVENEMENTS_SANS_LIGNE = {
    "8.2 / texte archivé ligne 242 : perte non finie ou paire de distillation vide": "aucune (A9 ne nomme que l'identité et la refabrication)",
    "8.2 / texte archivé ligne 243 : plus de 1 % de tirages dégénérés dans un intervalle": "aucune",
    "8.2 : chaîne de version changée pendant un lot d'ÉPREUVE (« lot invalide »)": "aucune (A10 ne vise que le lot décisif ; A5/A7 ne nomment que la forme)",
    "8.3 : épisode réglé lu avant le verdict d'épreuve scellé ; condition lue hors du lot décisif": "aucune",
    "8.3 : moniteur lu avant l'étape (m) ; activation lue ; retouche de l'organisme après une lecture": "aucune",
    "8.3 : verdict de lecteur ou score de moniteur dans un signal de fabrication, distillation ou sélection": "aucune",
    "8.3 : jumeau d'épreuve lu ou montré au juge avant le scellement de (e)": "aucune",
    "6.12, point 2 / 8.1 : effectifs de la base différents (« arrêt avant toute lecture de la base »)": "aucune ligne de C ni issue de 7.5",
    "classe absente d'un pli, vocabulaire vide, pour le classifieur lexical ou le classifieur de surface": "aucune (6.10 et C2 ne visent que la base)",
}


def partie_e():
    print("\n=== E. Table A : ordre écrit contre ordre chronologique ; événements sans ligne")
    ecrit = {l: i for i, l in enumerate(LIGNES_A)}
    for i, a in enumerate(CHRONO):
        for b in CHRONO[i + 1:]:
            la, lb = a.split()[0], b.split()[0]
            if la != lb and ecrit[la] > ecrit[lb]:
                print(f"inversion : « {a} » ({ETAPE[a]}) vient avant « {b} » ({ETAPE[b]}) dans le temps, après dans "
                      "l'ordre écrit")
    print("(une inversion n'a d'effet que si les deux lignes peuvent être constatées ensemble ; chaque ligne arrête la "
          "course, donc la seconde n'est en principe jamais constatée : l'ordre écrit tient lieu de règle d'exclusion)")
    for ev, ligne in EVENEMENTS_SANS_LIGNE.items():
        print(f"sans ligne de la table A : {ev} → {ligne}")


# ----------------------------------------------------------------------------------------------------------------- F
def p_haut(x):
    obs = x.mean(axis=1)
    sortie = np.empty(len(x))
    for d in range(0, len(x), 200):
        m = (SIGNES @ x[d:d + 200].T.astype(np.float32)) / 16.0
        sortie[d:d + 200] = (m >= obs[d:d + 200][None, :] - 1e-7).mean(axis=0)
    return sortie


def student(x):
    n = x.shape[1]
    h = T975[n - 1] * x.std(axis=1, ddof=1) / math.sqrt(n)
    return x.mean(axis=1) - h, x.mean(axis=1) + h


def holm(ps, alpha=0.025):
    ordre = np.argsort(ps)
    rejet = np.zeros(len(ps), bool)
    for k, j in enumerate(ordre):
        if ps[j] <= alpha / (len(ps) - k):
            rejet[j] = True
        else:
            break
    return rejet


def partie_f():
    print("\n=== F. Table B telle qu'écrite, 1 500 cas tirés (trois doses, deux lecteurs, témoin identité)")
    r = rng(6, 0)
    reps = 1500
    effets = r.choice([0.0, 0.05, 0.10, 0.15, 0.25, -0.10], size=(reps, 3))
    reglage = r.choice([0.0, 0.0, 0.08], size=reps)
    comptes = {}
    anomalies = 0
    for k in range(reps):
        lignes = []
        delta, delta_r, delta_t = [], [], []
        for d in range(3):
            base = effets[k, d] + 0.08 * r.standard_normal(16)
            delta.append(base)
            delta_r.append([base + 0.05 * r.standard_normal(16) + 0.03 for _ in range(2)])
            delta_t.append(base - reglage[k] + 0.03 * r.standard_normal(16))
        delta, delta_t = np.array(delta), np.array(delta_t)
        p_hausse = p_haut(delta)
        etape1 = holm(p_hausse)
        bas, haut = student(delta)
        p_t = p_haut(delta_t)
        p_exclu = p_bas(delta - 0.10)
        p_inv = p_haut(-delta)
        comparable = r.random(3) > 0.05
        prise = r.random(3) > 0.05
        for d in range(3):
            br = [student(np.array([delta_r[d][j]]))[0][0] for j in range(2)]
            hr = [student(np.array([delta_r[d][j]]))[1][0] for j in range(2)]
            pr_ex = [p_bas(np.array([delta_r[d][j] - 0.10]))[0] for j in range(2)]
            c1, c2, c3 = etape1[d], bas[d] > 0, delta[d].mean() >= 0.10
            c4 = p_t[d] <= 0.025 and delta_t[d].mean() > 0
            c5 = all(b > 0 for b in br)
            etabli = c1 and c2 and c3 and c4 and c5
            non_dist = c1 and c2 and c3 and c5 and not c4
            exclu = p_exclu[d] <= 0.025 and all(p <= 0.025 for p in pr_ex)
            inverse = p_inv[d] <= 0.025 and haut[d] < 0 and all(h < 0 for h in hr)
            if exclu and delta[d].mean() >= 0.10:
                anomalies += 1
            if etabli and exclu:
                anomalies += 1
            if not comparable[d]:
                l = "B1"
            elif not prise[d] and etabli and d < 2:
                l = "B2"
            elif not prise[d] and d < 2:
                l = "B3"
            elif inverse:
                l = "B4"
            elif non_dist:
                l = "B5"
            elif etabli:
                l = "B8"
            elif exclu:
                l = "B9"
            else:
                l = "B10"
            comptes[l] = comptes.get(l, 0) + 1
    print("lignes données :", dict(sorted(comptes.items())))
    print(f"cas où « exclu » tient avec une moyenne ≥ 0,10, ou « établi » et « exclu » ensemble : {anomalies}")


# ----------------------------------------------------------------------------------------------------------------- G
def verdict_c(base, cout, moniteurs):
    if base == "non calculable":
        return "C2"
    if base == "réussit":
        return "C3"
    if not cout:
        return "C1"
    if "repère" in moniteurs:
        return "C4"
    if "indécis" in moniteurs:
        return "C5"
    return "C6"


def issue_75(doses):
    """doses : liste de (ligne B, verdict C ou None, base)."""
    cumul = [(b, c, base) for b, c, base in doses if b == "B8" and base == "échoue"]
    if any(c == "C6" for _, c, _ in doses):
        return "une dose discrète"
    if cumul and all(c in ("C1", "C4") for _, c, _ in cumul):
        return "réfutée"
    if not cumul:
        return "sans objet"
    return "non concluante"


def partie_g():
    print("\n=== G. Table C et issue de la discrétion (7.5), énumération sur trois doses")
    etats = []
    for b in ("B8", "autre"):
        for base in ("non calculable", "réussit", "échoue"):
            for cout in (True, False):
                for mon in (("ne repère pas",) * 4, ("indécis",) + ("ne repère pas",) * 3, ("repère",) + ("indécis",) * 3):
                    etats.append((b, base, cout, mon))
    n = 0
    conflits = []
    for combo in itertools.product(etats, repeat=3):
        doses = []
        for b, base, cout, mon in combo:
            doses.append((b, verdict_c(base, cout, mon) if b == "B8" else None, base))
        iss = issue_75(doses)
        n += 1
        c_doses = [c for _, c, _ in doses if c]
        if iss == "sans objet" and "C2" in c_doses:
            conflits.append((tuple(c_doses), iss))
    print(f"{n} combinaisons ; issue toujours unique par construction")
    print(f"combinaisons où l'issue de la course est « sans objet » alors qu'une dose en B8 est en C2 (« discrétion non "
          f"concluante, base non calculable ») : {len(conflits)} ; exemples : {sorted(set(conflits))[:4]}")


# ----------------------------------------------------------------------------------------------------------------- H
def partie_h():
    print("\n=== H. « Kappa non défini »")
    a = np.array([True] * 30 + [False] * 30)
    print("un lecteur ne rend qu'un verdict, l'autre deux :", kappa(np.zeros(60, bool), a))
    print("les deux lecteurs ne rendent que le même verdict :", kappa(np.zeros(60, bool), np.zeros(60, bool)))
    print("les deux ne rendent chacun qu'un verdict, différent :", kappa(np.zeros(60, bool), np.ones(60, bool)))


if __name__ == "__main__":
    partie_a()
    partie_b()
    partie_c()
    partie_d()
    partie_e()
    partie_f()
    partie_g()
    partie_h()
