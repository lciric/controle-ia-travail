"""Erreur type et écart minimal détectable pour l'étape 2 — proposition v1 (non opposable, aucune lecture de score).

Usage : python3 -I calcul-ecart-minimal-v1.py BANQUE.json SORTIE.json

Lit seulement les comptes agrégés (part × famille × classe) de la banque ; n'imprime et n'écrit ni texte, ni
identifiant, ni vérité par tâche. Tout le reste est hypothèse de variance, dite dans la sortie.

Modèle (sur l'échelle du score) : score d'une course = moyenne sur les familles de l'exactitude équilibrée (moyenne des
rappels par classe), comme le juge du noyau. Variance du score d'une course sur la banque fixe :
    V = sigma_course² + (1 - rho_taches) × V_binomiale(p = 0,5)
sigma_course : écart type, d'une graine à l'autre, de la qualité vraie de l'organisme produit (conception comprise) ;
rho_taches : part de la variance binomiale portée par la difficulté propre des tâches, commune aux deux bras (elle
s'annule dans une différence sur les mêmes tâches). Différence de deux bras à R répétitions chacun, graines non
corrélées entre bras : Var(D) = 2 V / R.
"""
import collections
import hashlib
import json
import sys

import numpy as np
from scipy import optimize, stats

ALPHA = 0.05            # bilatéral
PUISSANCE = 0.80
REPETITIONS = (1, 3, 5, 10)
SIGMAS_COURSE = (0.0, 0.05, 0.10)
RHOS_TACHES = (0.0, 0.6)
EFFETS_CIBLES = (0.05, 0.10, 0.20)
ENTROPIE = 20261026     # simulation de contrôle seulement (R9 : SeedSequence), publique, non opposable
N_SIM = 4000


def empreinte(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def comptes(banque):
    out = {}
    for part in ("train", "test", "test_final"):
        c = collections.Counter((t["famille"], str(t["verite"])) for t in banque[part])
        out[part] = {f"{f}|{v}": n for (f, v), n in sorted(c.items())}
    return out


def structure(cpt_part):
    fam = collections.defaultdict(dict)
    for cle, n in cpt_part.items():
        f, v = cle.split("|")
        fam[f][v] = n
    return {f: dict(c) for f, c in sorted(fam.items())}


def var_exactitude(n, p=0.5):
    return p * (1 - p) / n


def var_equilibree(classes, p=0.5):
    k = len(classes)
    return sum(p * (1 - p) / (k * k * n) for n in classes.values())


def var_global(fam, p=0.5):
    f = len(fam)
    return sum(var_equilibree(c, p) for c in fam.values()) / (f * f)


def poids_taches(fam):
    """Poids de chaque tâche dans le score global, et indice de famille, dans l'ordre famille puis classe."""
    w, idx = [], []
    f = len(fam)
    for i, (nom, classes) in enumerate(fam.items()):
        k = len(classes)
        for n in classes.values():
            w += [1.0 / (f * k * n)] * n
            idx += [i] * n
    return np.array(w), np.array(idx)


Z = stats.norm.ppf(1 - ALPHA / 2) + stats.norm.ppf(PUISSANCE)


def puissance_t(delta, se, df):
    tc = stats.t.ppf(1 - ALPHA / 2, df)
    nc = delta / se
    p = 1 - stats.nct.cdf(tc, df, nc) + stats.nct.cdf(-tc, df, nc)
    if not np.isfinite(p):  # décentrage extrême : la puissance vaut 1 à la précision utile
        return 1.0
    return float(p)


def mde_t(se, df):
    if df < 1:
        return None
    return float(optimize.brentq(lambda d: puissance_t(d, se, df) - PUISSANCE, 1e-9, 12 * se))


def r_requis(delta, v, appariement_df):
    for r in range(2, 201):
        se = (2 * v / r) ** 0.5
        df = (2 * r - 2) if appariement_df == "deux_echantillons" else (r - 1)
        if puissance_t(delta, se, df) >= PUISSANCE:
            return r
    return ">200"


def simulation(w, sigma, delta, r, rng, n_sim):
    """Contrôle : tâches à p = 0,5 (rho = 0), effet de course N(0, sigma²) additif, bras B décalé de delta.
    Rend le taux de rejet du test t à deux échantillons (df = 2R - 2) ; pour R = 1, le test binomial « tâches seules »."""
    n = len(w)
    rej = 0
    for _ in range(n_sim):
        u = rng.normal(0.0, sigma, size=(2, r)) if sigma > 0 else np.zeros((2, r))
        p = 0.5 + u[:, :, None] + np.array([-delta / 2, delta / 2])[:, None, None]
        p = np.clip(p, 0.0, 1.0)
        y = rng.random((2, r, n)) < p
        s = (y * w).sum(axis=2)
        if r == 1:
            # ce que ferait une lecture qui ne connaît que le bruit des tâches (binomial, pas de variance de course)
            se = (2 * (w ** 2).sum() * 0.25) ** 0.5
            rej += abs(s[1, 0] - s[0, 0]) / se > stats.norm.ppf(1 - ALPHA / 2)
        else:
            t, pv = stats.ttest_ind(s[1], s[0], equal_var=True)
            rej += pv < ALPHA
    return rej / n_sim


def main(chemin_banque, chemin_sortie):
    banque = json.load(open(chemin_banque, encoding="utf-8"))
    cpt = comptes(banque)
    del banque
    sortie = {
        "script": "calcul-ecart-minimal-v1.py",
        "script_sha256": empreinte(__file__),
        "banque": chemin_banque,
        "banque_sha256": empreinte(chemin_banque),
        "comptes_part_famille_classe": cpt,
        "parametres": {"alpha_bilateral": ALPHA, "puissance": PUISSANCE, "p_pire_cas": 0.5,
                        "sigmas_course": SIGMAS_COURSE, "rhos_taches": RHOS_TACHES,
                        "entropie_simulation": ENTROPIE, "n_sim": N_SIM, "z_somme": Z},
        "erreurs_types_p05": {}, "ecart_minimal": {}, "repetitions_requises": {}, "faux_positifs_R1": {},
        "controle_simulation": {},
    }
    # 1. Erreurs types (p = 0,5, pire cas ; à p = 0,8, multiplier par 0,8)
    for part in ("train", "test", "test_final"):
        fam = structure(cpt[part])
        n = sum(sum(c.values()) for c in fam.values())
        e = {"n": n, "exactitude": var_exactitude(n) ** 0.5, "score_global_equilibre": var_global(fam) ** 0.5,
             "n_effectif_score_global": 0.25 / var_global(fam)}
        for f, c in fam.items():
            m = sum(c.values())
            e[f"{f}:n"] = m
            e[f"{f}:exactitude"] = var_exactitude(m) ** 0.5
            e[f"{f}:equilibree"] = var_equilibree(c) ** 0.5
        sortie["erreurs_types_p05"][part] = e
    # sous-ensembles « catégorie absente du train » (LISEZMOI-v9 l. 33-34 : 4/4 en test, 10/4 en test_final)
    sortie["erreurs_types_p05"]["sous_ensembles_categorie_absente"] = {
        "test (4/4)": var_equilibree({"a": 4, "b": 4}) ** 0.5,
        "test_final (10/4)": var_equilibree({"a": 10, "b": 4}) ** 0.5,
    }
    # 2. Écart minimal détectable sur le score global de test_final
    fam_tf = structure(cpt["test_final"])
    vbin = var_global(fam_tf)
    for f, c in fam_tf.items():
        sortie["erreurs_types_p05"]["test_final"][f"{f}:part_de_variance_du_score_global"] = (
            var_equilibree(c) / 4) / vbin
    for sigma in SIGMAS_COURSE:
        for rho in RHOS_TACHES:
            v = sigma ** 2 + (1 - rho) * vbin
            cle = f"sigma_course={sigma:.2f}|rho_taches={rho:.1f}"
            ligne = {}
            for r in REPETITIONS:
                se = (2 * v / r) ** 0.5
                ligne[f"R={r}"] = {
                    "se_difference": se,
                    "mde_variance_connue_z": Z * se,
                    "mde_t_deux_echantillons_df_2R-2": mde_t(se, 2 * r - 2),
                    "mde_t_differences_appariees_df_R-1_sans_correlation": mde_t(se, r - 1),
                }
            sortie["ecart_minimal"][cle] = ligne
            sortie["repetitions_requises"][cle] = {
                f"effet={d:.2f}": {"deux_echantillons": r_requis(d, v, "deux_echantillons"),
                                   "differences_appariees": r_requis(d, v, "apparie")}
                for d in EFFETS_CIBLES}
            # faux positifs d'une lecture à une seule répétition qui ne connaît que le bruit des tâches
            v_taches = (1 - rho) * vbin
            seuil = stats.norm.ppf(1 - ALPHA / 2) * (v_taches / v) ** 0.5 if v > 0 else float("inf")
            sortie["faux_positifs_R1"][cle] = float(2 * (1 - stats.norm.cdf(seuil)))
    # par famille, à R = 10, rho = 0, sigma = 0 (plancher)
    sortie["ecart_minimal_par_famille_R10_plancher"] = {
        f: Z * (2 * var_equilibree(c) / 10) ** 0.5 for f, c in fam_tf.items()}
    # 3. Contrôle par simulation (rho = 0), graines par SeedSequence (R9)
    w, _ = poids_taches(fam_tf)
    ss = np.random.SeedSequence(ENTROPIE)
    enfants = iter(ss.spawn(64))
    for sigma in SIGMAS_COURSE:
        v = sigma ** 2 + vbin
        for r in REPETITIONS:
            rng0 = np.random.default_rng(next(enfants))
            c = {"rejet_effet_nul": simulation(w, sigma, 0.0, r, rng0, N_SIM)}
            if r > 1:
                d = mde_t((2 * v / r) ** 0.5, 2 * r - 2)
                rng1 = np.random.default_rng(next(enfants))
                c["effet_teste"] = d
                c["puissance_a_l_ecart_minimal_t"] = simulation(w, sigma, d, r, rng1, N_SIM)
            sortie["controle_simulation"][f"sigma_course={sigma:.2f}|rho=0|R={r}"] = c
    with open(chemin_sortie, "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
