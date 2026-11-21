"""Calculs du plan exploratoire de l'étape 2a (bras « papier dopamine ») — v1.

EXPLORATOIRE, non opposable (GO-2026-11-21-44). Aucune donnée du programme n'est lue :
tailles de fichiers écrites en dur (relevées par le répertoire interne du fichier),
lois simulées, prix repris du devis du lot honnête neuf.
Lancement : .venv/bin/python -I <ce fichier>            (blocs A à E, rejouables à l'octet)
            .venv/bin/python -I <ce fichier> --essai    (bloc F, durée : non rejouable à l'octet)
Graines : numpy.random.SeedSequence, dérivées par bloc (R9).
"""
import math
import sys
import time

import numpy as np

RACINE = np.random.SeedSequence(20261121_2)  # graine mère, consignée ici


def graine(*cle):
    return np.random.SeedSequence(entropy=RACINE.entropy, spawn_key=tuple(cle))


# ---------------------------------------------------------------- estimateur de rho
def rho_anova(alertes, familles):
    """Corrélation, à l'intérieur d'une famille, d'une indicatrice 0/1 (analyse de
    variance à un facteur, tailles inégales admises). Rend la valeur brute (peut être < 0)."""
    alertes = np.asarray(alertes, dtype=float)
    _, inv = np.unique(familles, return_inverse=True)
    f = inv.max() + 1
    n = alertes.size
    m = np.bincount(inv, minlength=f).astype(float)
    s = np.bincount(inv, weights=alertes, minlength=f)
    p = s / m
    pg = alertes.mean()
    msb = float((m * (p - pg) ** 2).sum() / (f - 1))
    msw = float((m * p * (1 - p)).sum() / (n - f))
    m0 = (n - (m ** 2).sum() / n) / (f - 1)
    den = msb + (m0 - 1) * msw
    return 0.0 if den <= 0 else (msb - msw) / den


def lot_plante(rng, f, m, rho, taux=0.20):
    """Indicatrices dont la corrélation par famille vaut rho par construction (bêta-binomiale)."""
    fam = np.repeat(np.arange(f), m)
    if rho <= 0:
        pf = np.full(f, taux)
    else:
        k = 1.0 / rho - 1.0
        pf = rng.beta(taux * k, (1 - taux) * k, size=f)
    return (rng.random(f * m) < pf[fam]).astype(int), fam


def loi_estimateur(f, m, rho, reps, cle):
    rng = np.random.default_rng(graine(*cle))
    v = np.empty(reps)
    for i in range(reps):
        a, fam = lot_plante(rng, f, m, rho)
        v[i] = rho_anova(a, fam)
    return v


# ---------------------------------------------------------------- règle du devis du lot neuf
def episodes_a_acheter(f, rho, cible=437, borne=1311):
    m = 1
    while f * m <= borne:
        if math.floor(f * m / (1 + (m - 1) * rho)) >= cible:
            return f * m
        m += 1
    return None


def blocs_a_e():
    print("EXPLORATOIRE — calculs du plan de l'étape 2a, v1 — aucune donnée du programme lue")
    # ---- A
    print("\n[A] Ce que les tailles disent du fichier jetons-principales-p3.npz (membres non compressés)")
    en_tete = 128
    lignes = (19328 - en_tete) // 8
    jetons = (4261592 - en_tete) // 8
    print(f"  rang.npy, longueur.npy, debut.npy : (19328 - {en_tete}) / 8 = {lignes} lignes")
    print(f"  bornes_lisibles.npy : 2528 - {en_tete} = {2528 - en_tete} octets, un par ligne")
    print(f"  scores_0, logits_0, scores_1, logits_1 : (4261592 - {en_tete}) / 8 = {jetons} valeurs chacun")
    print(f"  jetons par action, en moyenne : {jetons / lignes:.1f} ; actions par épisode si 240 épisodes : {lignes / 240:.1f}")
    print(f"  un état de dimension 4096 par jeton, en demi-précision, pèserait {jetons * 4096 * 2 / 1e9:.2f} Go par couche :")
    print("  le fichier (17,2 Mo) ne peut pas porter d'états internes ; il porte des scores par jeton")
    etats = 240 * 11 * 3 * 4096 * 2
    print(f"  états à garder pour 240 épisodes, 11 positions, 3 couches, demi-précision : {etats / 1e6:.0f} Mo")

    # ---- B
    print("\n[B] Objets de contrôle de l'estimateur de la corrélation par famille (100 familles de 6, 2 000 lots)")
    print("  prédiction écrite avant le calcul : corrélation plantée 0 -> moyenne dans [-0,02 ; +0,02] ;")
    print("                                      corrélation plantée 0,30 -> moyenne dans [0,27 ; 0,33]")
    for j, rho in enumerate((0.0, 0.30)):
        v = loi_estimateur(100, 6, rho, 2000, (1, j))
        ok = abs(v.mean() - rho) <= (0.02 if rho == 0 else 0.03)
        print(f"  plantée {rho:.2f} : moyenne {v.mean():+.3f}, écart type {v.std(ddof=1):.3f} -> {'tenu' if ok else 'CASSÉ'}")

    # ---- C
    print("\n[C] Précision de la corrélation par famille mesurée à 20 % d'alertes, selon le lot (2 000 lots simulés)")
    print("  familles x épisodes | plantée | moyenne | écart type | 10e et 90e centiles")
    plans = [(8, 30), (12, 20), (24, 10), (40, 6), (60, 4), (60, 6), (100, 4), (150, 4)]
    for i, (f, m) in enumerate(plans):
        for j, rho in enumerate((0.0, 0.10, 0.30)):
            v = loi_estimateur(f, m, rho, 2000, (2, i, j))
            q10, q90 = np.quantile(v, [0.10, 0.90])
            print(f"  {f:4d} x {m:2d} = {f * m:4d} | {rho:.2f} | {v.mean():+.3f} | {v.std(ddof=1):.3f} | {q10:+.3f} à {q90:+.3f}")

    # ---- D
    print("\n[D] Ce que l'imprécision coûte : épisodes à acheter pour 437 épisodes effectifs (règle du devis du lot neuf)")
    print("  familles retenues | rho = 0,00 | 0,05 | 0,10 | 0,15 | 0,20 | 0,30   ('—' : hors de la borne de 1 311)")
    for f in (60, 100, 150, 200, 300):
        cases = [episodes_a_acheter(f, r) for r in (0.0, 0.05, 0.10, 0.15, 0.20, 0.30)]
        print(f"  {f:4d} | " + " | ".join("—" if c is None else str(c) for c in cases))
    print("  prix de 100 épisodes de plus (devis du lot neuf, § 5) : 1,25 à 1,54 USD")

    # ---- E
    print("\n[E] Coût de la carte (prix et frais fixes du devis du lot honnête neuf, § 4 ; USD)")
    bas, haut, pire = 1.0889 + 0.03, 1.30 + 0.08, 1.40 + 0.08
    tel_bas, tel_haut = 42 * 0.026, 42 * 0.05
    fixes = 1.8

    def cout(h):
        return h * bas + tel_bas, h * haut + tel_haut, 2 * h * pire + tel_haut, 1.5 * h * haut + tel_haut

    h_a = fixes + 0.25 + 240 * 0.45 / 3600
    b, h, p, c = cout(h_a)
    print(f"  tranche A, relecture forcée de 240 épisodes au plus (0,45 s par épisode, un quart d'heure de contrôles) :")
    print(f"    {h_a:.2f} h ; {b:.2f} à {h:.2f} ; pire cas {p:.2f} ; hôte une fois et demie plus lent au prix haut {c:.2f}")
    for marge in (0.25, 0.5):
        print(f"    sur une instance déjà accordée, {marge} h de plus : {marge * bas:.2f} à {marge * haut:.2f}")
    for n in (240, 300, 400):
        h_b = fixes + n * 40.2 / 3600
        b, h, p, c = cout(h_b)
        print(f"  tranche B, {n} épisodes honnêtes neufs (40,2 s par épisode) : {h_b:.2f} h ; {b:.2f} à {h:.2f} ; pire cas {p:.2f} ; une fois et demie {c:.2f}")


def bloc_f():
    """Essai de durée et objets de contrôle de la sonde, sur états synthétiques (aucune donnée)."""
    import torch

    print("EXPLORATOIRE — [F] essai sur états synthétiques : objectif de différence temporelle aux frontières")
    print("  prédiction écrite avant le calcul : vérité plantée -> aire sous la courbe hors famille >= 0,90 ;")
    print("                                      issues permutées -> aire dans [0,35 ; 0,65]")
    from sklearn.metrics import roc_auc_score

    torch.set_num_threads(4)
    f, m, t, d = 16, 10, 10, 4096
    rng = np.random.default_rng(graine(3))
    fam = np.repeat(np.arange(f), m)
    n = f * m
    z = rng.normal(size=n) + 0.5 * rng.normal(size=f)[fam]      # difficulté latente, effet de famille
    r = (rng.random(n) < 1 / (1 + np.exp(-2.5 * z))).astype(np.float32)
    u = rng.normal(size=d) / math.sqrt(d)
    force = 12.0                                                 # force du signal planté
    etats = rng.normal(size=(n, t + 1, d)).astype(np.float32)
    for k in range(t + 1):
        cible = (1 - k / t) * z + (k / t) * (4 * r - 2)          # l'issue se révèle le long de l'épisode
        etats[:, k, :] += (force * cible)[:, None] * u[None, :]
    appr = fam < 10
    x_a, x_e = torch.tensor(etats[appr]), torch.tensor(etats[~appr])
    gamma = 1 - 1e-5

    def apprendre(issues, cle):
        torch.manual_seed(int(graine(4, cle).generate_state(1)[0]))
        v = torch.nn.Sequential(torch.nn.Linear(d, 1024), torch.nn.ReLU(), torch.nn.Linear(1024, 1), torch.nn.Sigmoid())
        opt = torch.optim.AdamW(v.parameters(), lr=1e-4, weight_decay=0.01)
        y = torch.tensor(issues)
        ordre = np.random.default_rng(graine(5, cle))
        t0 = time.time()
        for _ in range(100):
            perm = ordre.permutation(len(y))
            for i in range(0, len(y), 4):
                idx = torch.tensor(perm[i:i + 4])
                val = v(x_a[idx]).squeeze(-1)                     # (lot, t + 1)
                delta = gamma * val[:, 1:] - val[:, :-1]          # équation 8, pas intermédiaires
                fin = y[idx] - val[:, -1]                         # équation 8, dernier pas
                perte = (delta ** 2).sum(1).mean() + (fin ** 2).mean()
                opt.zero_grad()
                perte.backward()
                opt.step()
        with torch.no_grad():
            s0 = v(x_e[:, 0, :]).squeeze(-1).numpy()
        return s0, time.time() - t0

    s0, duree = apprendre(r[appr], 0)
    aire = roc_auc_score(r[~appr], s0)
    print(f"  vérité plantée : aire hors famille {aire:.3f} -> {'tenu' if aire >= 0.90 else 'CASSÉ'} ; durée d'un apprentissage {duree:.0f} s (100 épisodes, 11 positions, 100 époques, lots de 4)")
    perm = np.random.default_rng(graine(6)).permutation(appr.sum())
    s0p, duree_p = apprendre(r[appr][perm], 1)
    aire_p = roc_auc_score(r[~appr], s0p)
    print(f"  issues permutées : aire hors famille {aire_p:.3f} -> {'tenu' if 0.35 <= aire_p <= 0.65 else 'CASSÉ'} ; durée {duree_p:.0f} s")
    print(f"  plan complet : 20 découpages x 3 couches x 2 variantes = 120 apprentissages, soit environ {120 * duree / 60:.0f} min sur cette machine (4 cœurs)")


if __name__ == "__main__":
    if "--essai" in sys.argv:
        bloc_f()
    else:
        blocs_a_e()
