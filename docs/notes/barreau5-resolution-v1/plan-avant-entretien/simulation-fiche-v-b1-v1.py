#!/usr/bin/env python3
"""Barreau 5, fiche de décision V-B1 : une troisième voie éprouvée en mondes inventés (v1).

Écrite par le rédacteur (Claude Fable 5.2), le 19 novembre 2026. LOIS INVENTÉES : aucune donnée du programme.
Ce n'est pas une conception arrêtée : c'est de quoi chiffrer une fiche de décision.

Elle réemploie, sans les modifier, le monde géométrique, la liste des mondes, les seuils et la règle d'issue de la
simulation du vérificateur (`contre-lecture-outils-plan-brouillon3-v1/simulation-verification-brouillon3-v1.py`,
chargée par runpy), pour que les taux se comparent case à case aux siens.

Troisième voie : l'épreuve à poussée égale oppose LES DEUX MEMBRES ÉDITÉS (sur-saboteur contre jumeau), et non plus
le saboteur à son jumeau. Les deux portent la même trace d'une édition commune aux deux sens et le même surcroît de
chaos : la trace s'annule dans leur différence, et l'instrument est le membre NON édité.
  E1  : saboteur moins jumeau, nominal (inchangée).
  E3  : sur-saboteur moins jumeau, nominal (inchangée).
  E2a : q = P(jumeau, saboteur) / P(sur-saboteur, saboteur) ; sur-saboteur à sqrt(q), jumeau à 1/sqrt(q).
  E2b : r = P(jumeau, g) / P(sur-saboteur, g), g = direction moyenne des SABOTEURS d'apprentissage (non édités).
  Mêmes règles d'échec que le texte. Mot « sabotage » : les quatre séparées (règle d'issue du vérificateur).
Deux variantes de sonde :
  « V36 » : sonde du texte (saboteur contre jumeau des familles d'apprentissage) : 36 adaptateurs, formation inchangée ;
  « V39 » : sonde apprise sur le sur-saboteur contre le jumeau des familles d'apprentissage (trois adaptateurs de plus).
Graines : une par case, enfants d'une SeedSequence (R9). numpy seul. Sortie : JSON sur la sortie standard.
"""
from __future__ import annotations

import json
import math
import os
import runpy
import sys
import time

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
V = runpy.run_path(os.path.join(ICI, "contre-lecture-outils-plan-brouillon3-v1", "simulation-verification-brouillon3-v1.py"),
                   run_name="verificateur")
MONDES, issue, L_JETONS = V["MONDES"], V["issue"], V["L_JETONS"]
ENTROPIE = 0x7F1C_B5F4_2026_1119_1730_0B1E
M_L = None


def monde(rng, par: dict, k_app: int = 3, k_test: int = 10):
    p = par["p"]
    f, r_u, r_e, chi = par.get("f", 0.0), par.get("r_u", 1.0), par.get("r_e", 0.5), par.get("chi", 0.0)
    a_c, cible_force = par.get("a", 1.0), par.get("force_sur", "commun")
    sig_s, h2, alpha = par.get("sigma_s", 0.0), par.get("h2", 2.0), par.get("alpha", 0.0)
    sym, rho = par.get("trace_symetrique", True), par.get("rho", 0.0)
    kappa, kappa_force = par.get("kappa", 0.0), par.get("kappa_force", False)
    phi, etal = par.get("phi", 0.0), par.get("etalement", "commun")
    b_lect, b_sonde = par.get("bruit_lecture", 0.01), par.get("bruit_sonde", 0.05)
    variante = par["sonde"]
    h = {0: 0.0, 1: 1.0, 2: h2}
    racine_p = math.sqrt(p)

    def familles(k, niveaux):                      # même loi que le monde du vérificateur
        a = a_c * np.exp(0.15 * rng.standard_normal(k))
        u = r_u * rng.standard_normal((k, p)) / racine_p
        z_commun = rng.standard_normal((k, p))
        delta, etalement, lam, bruit = {}, {}, {}, {}
        for niv in niveaux:
            F = 1.0 + f * niv
            fg = F if cible_force in ("commun", "tout", "g") else 1.0
            fu = F if cible_force in ("commun", "tout", "u") else 1.0
            if cible_force == "mixte":
                fg, fu = F, 1.0 + 0.4 * f * niv
            fe = F if cible_force == "tout" else 1.0
            edite = niv != 1
            z = rng.standard_normal((k, p))
            if edite and rho != 0.0:
                signe = 1.0 if (niv == 0 or rho > 0) else -1.0
                z = signe * math.sqrt(abs(rho)) * z_commun + math.sqrt(1.0 - abs(rho)) * z
            e = r_e * (1.0 + chi * edite) * z / racine_p
            part = fu * u
            part[:, 0] += fg * a
            d = part + fe * e
            d[:, 1] += sig_s * h[niv]
            if niv == 0:
                d[:, 2] += alpha
            elif niv == 2:
                d[:, 2 if sym else 3] += alpha
            delta[niv] = d
            etalement[niv] = phi * (np.linalg.norm(part, axis=1) if etal == "commun" else np.linalg.norm(d, axis=1))
            lam[niv] = F if kappa_force else 1.0
            bruit[niv] = b_lect * rng.standard_normal(k)
        return delta, etalement, lam, bruit

    app, et_app, lam_app, nu_app = familles(k_app, (0, 1) if variante == "V36" else (0, 1, 2))
    test, et_test, lam_test, nu_test = familles(k_test, (0, 1, 2))
    haut = 1 if variante == "V36" else 2
    w = (app[haut] - app[0]).mean(axis=0) + b_sonde * rng.standard_normal(p) / racine_p
    w /= np.linalg.norm(w)

    def stat(d, etalement, nu, c):
        return c * (d @ w + nu) + (np.sqrt(1.0 + (c * etalement) ** 2) - 1.0) * M_L

    un_a, un_t = np.ones(k_app), np.ones(k_test)
    d_app = stat(app[haut], et_app[haut], nu_app[haut], un_a) - stat(app[0], et_app[0], nu_app[0], un_a)
    t = {niv: stat(test[niv], et_test[niv], nu_test[niv], un_t) for niv in (0, 1, 2)}
    d1, d3 = t[1] - t[0], t[2] - t[0]
    # E2a : sur-saboteur contre jumeau, instrument le saboteur (non édité)
    pj = (test[0] * test[1]).sum(axis=1) + kappa * lam_test[0] * lam_test[1]
    pu = (test[2] * test[1]).sum(axis=1) + kappa * lam_test[2] * lam_test[1]
    bon_a = (pj > 0) & (pu > 0)
    ca = np.sqrt(np.where(bon_a, pj / np.where(bon_a, pu, 1.0), 1.0))
    bon_a &= (ca >= 0.5) & (ca <= 2.0)
    d2a = stat(test[2], et_test[2], nu_test[2], ca) - stat(test[0], et_test[0], nu_test[0], 1.0 / ca)
    d2a[~bon_a] = np.nan
    # E2b : direction commune des saboteurs d'apprentissage (non édités)
    gh = app[1].mean(axis=0)
    gh /= np.linalg.norm(gh)
    gj, gu = test[0] @ gh, test[2] @ gh
    defini = (gj > 0) & (gu > 0)
    cb = np.sqrt(np.where(defini, gj / np.where(defini, gu, 1.0), 1.0))
    bon_b = (cb >= 0.5) & (cb <= 2.0)
    d2b = stat(test[2], et_test[2], nu_test[2], cb) - stat(test[0], et_test[0], nu_test[0], 1.0 / cb)
    d2b[~bon_b] = np.nan
    return d1, d2a, d2b, d3, d_app


def une_case(args):
    nom, p, sonde, graine, mondes, m_l = args
    global M_L
    M_L = m_l
    rng = np.random.default_rng(graine)
    par = dict(MONDES[nom], p=p, sonde=sonde)
    comptes = {i: 0 for i in ("C", "S99", "S95", "D", "E", "N")}
    epr = {"E1": 0, "E2a": 0, "E2b": 0, "E3": 0}
    for _ in range(mondes):
        d1, d2a, d2b, d3, d_app = monde(rng, par)
        i, e = issue(d1, d2a, d2b, d3, d_app)
        comptes[i] += 1
        for k in epr:
            epr[k] += e[k]
    return f"{nom}/p_{p}/sonde_{sonde}", {
        "issues": {k: round(v / mondes, 4) for k, v in comptes.items()},
        "mot_sabotage_99_ou_95": round((comptes["S99"] + comptes["S95"]) / mondes, 4),
        **{f"{k}_separe": round(v / mondes, 4) for k, v in epr.items()}}


def main():
    import multiprocessing as mp
    global M_L
    t0 = time.time()
    mondes = 100 if "--rapide" in sys.argv else 1000
    cases = [(nom, p, sonde) for nom in MONDES for p in (1024, 4096) for sonde in ("V36", "V39")]
    enfants = np.random.SeedSequence(ENTROPIE).spawn(len(cases) + 1)
    M_L = float(np.random.default_rng(enfants[0]).standard_normal((50_000, L_JETONS)).max(axis=1).mean())
    taches = [(nom, p, sonde, enfants[i + 1], mondes, M_L) for i, (nom, p, sonde) in enumerate(cases)]
    with mp.Pool(4) as pool:
        resultats = dict(pool.map(une_case, taches, chunksize=1))
    sortie = {"avertissement": "lois inventées ; aucune donnée du programme ; fiche de décision V-B1",
              "entropie": hex(ENTROPIE), "numpy": np.__version__, "mondes_par_case": mondes,
              "mondes": {f"{n}/p_{p}/sonde_{s}": resultats[f"{n}/p_{p}/sonde_{s}"] for (n, p, s) in cases}}
    sortie["duree_s"] = round(time.time() - t0, 1)
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
