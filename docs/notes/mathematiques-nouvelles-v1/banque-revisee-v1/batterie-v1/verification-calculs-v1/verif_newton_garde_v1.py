"""Vérification des corrections de la batterie (v3) — la garde de convergence de la sonde des nombres — v1.

Écrit par le vérificateur des corrections (Opus 5.5, session neuve). Le banc est celui du premier contre-lecteur
(`../contre-lecture-calculs-v1/recalcul_ecarts_1_2_v1.py`, importé, inchangé : banc reconstruit sans le code du
concepteur, strates contrôlées par force brute, racines d'épreuve 1000 à 1119 seulement). Le calcul du minimum est
recodé ici d'après la lettre du § 2.2 de `batterie-fuite-banque-revisee-v3.md` :
  Newton amorti à partir de poids nuls ; direction d (hessienne × d = gradient) ; décrément = gradient · d ;
  si décrément ≤ 1e-13 × n, on retranche d et l'on s'arrête (convergé) ; sinon pas t = 1, divisé par deux tant que
  la perte en w − t d ne baisse pas d'au moins 1e-4 × t × décrément, soixante essais au plus (t de 1 à 2^-59) ;
  200 tours au plus ; garde : 200 tours faits, soixante essais sans pas, ou valeur non finie = non convergé.
Comparé, sur les mêmes apprentissages : (1) le Newton pur de la v2 (50 pas, arrêt au plus grand pas < 1e-10) ;
(2) le critère du « pas effectif » proposé par la première contre-lecture (même recherche de pas, arrêt quand
max |t d| < 1e-10). Épreuve de la garde : le même calcul arrêté au premier tour doit rendre C3 non tenue.

Emploi : OMP_NUM_THREADS=1 python3 -I verif_newton_garde_v1.py SORTIE.json > SORTIE.txt
"""
import json, math, os, sys, warnings
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "contre-lecture-calculs-v1"))
import numpy as np
import recalcul_ecarts_1_2_v1 as banc

warnings.simplefilter("ignore")
TOURS_MAX = [200]          # modifiable pour l'épreuve de la garde
COMPTE = {}


def perte(w, Z, y):
    s = Z @ w
    return float(np.sum(np.logaddexp(0.0, s) - y * s) + 0.5 * float(w @ w))


def grad_hess(w, Z, y):
    s = Z @ w
    p = 1.0 / (1.0 + np.exp(-np.clip(s, -700, 700)))
    g = Z.T @ (p - y) + w
    H = (Z * (p * (1 - p))[:, None]).T @ Z + np.eye(len(w))
    return g, H


def newton_v3(Z, y, tours_max):
    """Lettre du § 2.2 (v3). Rend (w, converge, tours, motif)."""
    n = len(y); w = np.zeros(Z.shape[1]); f = perte(w, Z, y)
    for tour in range(1, tours_max + 1):
        g, H = grad_hess(w, Z, y)
        d = np.linalg.solve(H, g)
        dec = float(g @ d)
        if not (np.all(np.isfinite(d)) and math.isfinite(dec)):
            return w, False, tour, "valeur non finie"
        if dec <= 1e-13 * n:
            w = w - d
            return w, bool(np.all(np.isfinite(w))), tour, "décrément"
        t = 1.0
        for _ in range(60):
            f1 = perte(w - t * d, Z, y)
            if f1 <= f - 1e-4 * t * dec:
                break
            t /= 2
        else:
            return w, False, tour, "soixante essais sans pas"
        w = w - t * d; f = f1
    return w, False, tours_max, "tours épuisés"


def newton_pas_effectif(Z, y):
    """Critère proposé par la première contre-lecture : même recherche de pas, arrêt quand max |t d| < 1e-10."""
    w = np.zeros(Z.shape[1]); f = perte(w, Z, y)
    for tour in range(1, 201):
        g, H = grad_hess(w, Z, y)
        d = np.linalg.solve(H, g); dec = float(g @ d); t = 1.0
        for _ in range(60):
            f1 = perte(w - t * d, Z, y)
            if f1 <= f - 1e-4 * t * dec:
                break
            t /= 2
        w = w - t * d; f = perte(w, Z, y)
        if np.abs(t * d).max() < 1e-10:
            return w, True, tour
    return w, False, 200


def newton_pur_v2(Z, y):
    w = np.zeros(Z.shape[1])
    for tour in range(1, 51):
        g, H = grad_hess(w, Z, y)
        pas = np.linalg.solve(H, g); w = w - pas
        if not np.all(np.isfinite(w)):
            return w, False
        if np.abs(pas).max() < 1e-10:
            return w, True
    return w, False


class NonCalculable(Exception):
    pass


def logistique_v3(X, y, lam=1.0):
    mu = X.mean(0); sd = X.std(0); nul = sd == 0; sd[nul] = 1
    Z = (X - mu) / sd; Z[:, nul] = 0; Z = np.hstack([np.ones((len(Z), 1)), Z])
    w, ok, tours, motif = newton_v3(Z, y, TOURS_MAX[0])
    COMPTE["apprentissages"] += 1
    COMPTE["tours_max"] = max(COMPTE["tours_max"], tours)
    if not ok:
        COMPTE["non_converges_v3"] += 1
        COMPTE["motifs"][motif] = COMPTE["motifs"].get(motif, 0) + 1
    if COMPTE["comparer"]:
        w2, ok2, _ = newton_pas_effectif(Z, y)
        COMPTE["non_converges_pas_effectif"] += (not ok2)
        COMPTE["ecart_max_poids_v3_pas_effectif"] = max(COMPTE["ecart_max_poids_v3_pas_effectif"], float(np.abs(w - w2).max()))
        _, ok0 = newton_pur_v2(Z, y)
        COMPTE["non_converges_newton_pur_v2"] += (not ok0)
    def score(Xt):
        if not ok:
            return np.full(len(Xt), np.nan)   # garde : non calculable, aucun repli
        Zt = (Xt - mu) / sd; Zt[:, nul] = 0
        return np.round(np.hstack([np.ones((len(Zt), 1)), Zt]) @ w, 10)
    return score


banc.logistique = logistique_v3


def mesurer(variante, dose, comparer=True):
    COMPTE.clear()
    COMPTE.update(apprentissages=0, tours_max=0, non_converges_v3=0, motifs={}, comparer=comparer,
                  non_converges_pas_effectif=0, ecart_max_poids_v3_pas_effectif=0.0, non_converges_newton_pur_v2=0)
    B = {r: banc.construire(r, variante, dose) for r in banc.RACINES}
    S = banc.sonde_par_squelette_autres_racines(B)
    par_racine, sans_valeur = [], 0
    for r in banc.RACINES:
        sb = B[r][1]
        if any(not np.isfinite(S[r][x["cle"]]) for x in sb):
            sans_valeur += 1
            par_racine.append(None)
        else:
            par_racine.append(banc.exces(sb, S[r], "prorata"))
    if sans_valeur:
        c3 = {"tenue": False, "motif": "non calculable", "racines_sans_valeur": sans_valeur}
    else:
        c3 = banc.resume(par_racine, 2)
        c3["tenue"] = all(v["tient"] for v in c3.values())
    d = {k: v for k, v in COMPTE.items() if k != "comparer"}
    return {"C3_sonde_des_nombres": c3, "apprentissages": d}


def main(chemin):
    out = {"numpy": np.__version__, "racines": [banc.RACINES[0], banc.RACINES[-1]]}
    print("Vérification de la garde de convergence de la sonde des nombres (batterie v3) — v1")
    print(f"numpy {np.__version__} ; racines d'épreuve {banc.RACINES[0]} à {banc.RACINES[-1]} ; banc du premier contre-lecteur")
    for nom, var, dose in [("saine", "saine", 1.0), ("relation_1", "relation", 1.0), ("relation_0.5", "relation", 0.5),
                           ("grandeur_1", "grandeur", 1.0)]:
        out[nom] = mesurer(var, dose)
        print(f"  {nom:14s} : {out[nom]}", flush=True)
    # épreuve de la garde (artefact) : calcul arrêté au premier tour, sur la banque saine et sur « relation »
    TOURS_MAX[0] = 1
    for nom, var, dose in [("garde_un_tour_saine", "saine", 1.0), ("garde_un_tour_relation_1", "relation", 1.0)]:
        out[nom] = mesurer(var, dose, comparer=False)
        print(f"  {nom:14s} : {out[nom]}", flush=True)
    TOURS_MAX[0] = 200
    with open(chemin, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")


if __name__ == "__main__":
    main(sys.argv[1])
