"""Calcul de puissance de la réplication sur graine neuve de la course de convergence des règles de défense — v1.

Script versé avant le scellement (contre-lecture 1, CL-11 ; R6) : il produit chaque chiffre de la table « Calcul de
puissance » du préenregistrement de réplication (brouillon 2, § Seuil). Il relit les résultats de la course originale
(empreinte vérifiée), n'écrit aucun fichier, n'emploie aucune racine de la course ni de la réplication.

Méthode (déclarée au préenregistrement) : R = 20 000 rééchantillonnages de 100 instances parmi les 100 de la course
originale, LES MÊMES instances aux deux budgets et pour les trois contrastes (corrélations gardées) ; différences par
tâche décalées selon le scénario ; bornes par approximation normale (B2 et E8 : est ± z(0,99375)·s/√100 ; B8 :
est ± z(0,996875)·s/√100) ; Tables R1, R0, R3 du préenregistrement appliquées telles quelles. « Niveau 2 » : la vérité
est elle-même un rééchantillon de l'original, puis la réplication tire dans cette vérité (incertitude de l'original).
Graine du calcul : SeedSequence(314159, spawn_key=(1,)), sans lien avec la course.

Lancement : <dépôt>/.venv/bin/python -I puissance-replication-v1.py <dépôt>/diag/20261101-160323-regles-defense-convergence/resultats-regles-defense.json
"""
import hashlib
import json
import sys

import numpy as np

ATTENDU = "d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b"
Z2 = 2.497705474412374     # quantile 0,99375 de la loi normale (B2, E8)
Z8 = 2.7343687865331767    # quantile 0,996875 (B8)
M, TAU, R = 0.02, 0.05, 20000
R4 = "R4[moyenne,λ=0.3]"


def charger(chemin):
    octets = open(chemin, "rb").read()
    if hashlib.sha256(octets).hexdigest() != ATTENDU:
        raise SystemExit("empreinte inattendue du fichier de résultats : arrêt")
    taches = json.loads(octets)["resultat"]["resultats"]
    d = {}
    for c in (1, 2):
        t = sorted((x for x in taches if x["code_delta"] == c), key=lambda x: x["instance"])
        if [x["instance"] for x in t] != list(range(100)):
            raise SystemExit("instances inattendues : arrêt")
        v = {k: np.array([x["regles"][k]["V_iii_final"] for x in t]) for k in ("R0", "R2", "R3", R4)}
        d[c] = {"R3": v["R3"] - v["R2"], "R0": v["R0"] - v["R2"], "R4": v[R4] - v["R2"]}
    return d


def bornes(s):
    est, se = s.mean(1), s.std(1, ddof=1) / 10.0
    return est, est - Z2 * se, est + Z2 * se, est - Z8 * se, est + Z8 * se


def classe_B(s):
    """Table B : 1 « Rk > R2 », 2 « R2 > Rk », 3 « ≈ », 4 « Rk ≳ R2 », 5 « R2 ≳ Rk », 6 « ? » (première vraie)."""
    est, e_bas, e_haut, b_bas, b_haut = bornes(s)
    cls = np.full(est.shape, 6)
    for k, cond in ((5, b_haut < 0), (4, b_bas > 0), (3, (e_bas > -M) & (e_haut < M)), (2, b_haut < -M), (1, b_bas > M)):
        cls = np.where(cond, k, cls)
    return cls


def table_R1(s1, s2):
    rep = np.ones(s1.shape[0], bool)
    signe = np.zeros_like(rep)
    petit = np.zeros_like(rep)
    for s in (s1, s2):
        est, bas, haut, _, _ = bornes(s)
        rep &= (est >= TAU) & (bas > 0)
        signe |= haut < 0
        petit |= haut < TAU
    nr = ~rep & (signe | petit)
    return {"répliquée": rep.mean(), "non jugeable": (~rep & ~nr).mean(), "non répliquée": nr.mean()}


def table_R0(s1, s2):
    """Tables R0 et R3 (même forme) : non répliquée si une classe en faveur de R2 (2 ou 5) ; répliquée si les deux
    classes sont dans {1, 3, 4} ; sinon non jugeable. Rend aussi P(TR3) : une classe 1 ou 4 à au moins un budget."""
    c1, c2 = classe_B(s1), classe_B(s2)
    nr = np.isin(c1, (2, 5)) | np.isin(c2, (2, 5))
    rep = ~nr & np.isin(c1, (1, 3, 4)) & np.isin(c2, (1, 3, 4))
    tr3 = np.isin(c1, (1, 4)) | np.isin(c2, (1, 4))
    return {"répliquée": rep.mean(), "non jugeable": (~rep & ~nr).mean(), "non répliquée": nr.mean(),
            "TR3": tr3.mean()}


def scenario(d, rng, decaler=None, niveau=1):
    """Décalage appliqué aux différences par tâche, puis rééchantillonnage (mêmes indices partout)."""
    d = {c: {k: v.copy() for k, v in d[c].items()} for c in d}
    if decaler:
        decaler(d)
    i1 = rng.integers(0, 100, size=(R, 100)) if niveau == 2 else np.tile(np.arange(100), (R, 1))
    i2 = rng.integers(0, 100, size=(R, 100))
    tirer = {c: {k: np.take_along_axis(v[i1], i2, axis=1) for k, v in d[c].items()} for c in d}
    return {"HRép1": table_R1(tirer[1]["R3"], tirer[2]["R3"]),
            "HRép0": table_R0(tirer[1]["R0"], tirer[2]["R0"]),
            "HRép3": table_R0(tirer[1]["R4"], tirer[2]["R4"])}


def main(chemin):
    d = charger(chemin)
    est = {c: {k: float(v.mean()) for k, v in d[c].items()} for c in d}
    rng = np.random.default_rng(np.random.SeedSequence(314159, spawn_key=(1,)))

    def r3_moitie(x):
        for c in x:
            x[c]["R3"] = x[c]["R3"] - est[c]["R3"] / 2

    def r3_006(x):
        for c in x:
            x[c]["R3"] = x[c]["R3"] - est[c]["R3"] + 0.06

    def r0_vers(v):
        def f(x):
            for c in x:
                x[c]["R0"] = x[c]["R0"] - est[c]["R0"] + v
        return f

    lignes = [("celle de la course originale (niveau 1)", None, 1),
              ("celle de la course originale, incertitude de l'original (niveau 2)", None, 2),
              ("effet de HR1 réduit de moitié", r3_moitie, 1),
              ("effet de HR1 = +0,06 aux deux budgets", r3_006, 1),
              ("vrai Δ(R0, R2) = −0,01", r0_vers(-0.01), 1),
              ("vrai Δ(R0, R2) = −0,02 (= −m)", r0_vers(-0.02), 1)]
    print("estimations originales :", {c: {k: round(v, 4) for k, v in est[c].items()} for c in est})
    for nom, f, niveau in lignes:
        s = scenario(d, rng, f, niveau)
        print(nom, json.dumps({h: {k: round(float(v), 3) for k, v in t.items()} for h, t in s.items()},
                              ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1])
