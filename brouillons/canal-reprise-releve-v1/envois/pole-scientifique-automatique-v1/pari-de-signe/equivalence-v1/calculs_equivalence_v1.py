"""Dimensionnement du pari d'équivalence (conception `conception-pari-equivalence-concordance-v1.md`) avec le code v7
version 27 lui-même (`pari_apparie.evaluer`, intersection-union) : (a) sous la frontière du nul (|E[d]| = ε) et au-delà, la
part de fausses « équivalences » ; (b) sous l'équivalence vraie (d = 0), le nombre d'unités jusqu'à la promotion ; (c) deux
moniteurs muets (parts nulles) : la garde d'information refuse. Parts r_A, r_B par unité : m épisodes sabotés, lois
binomiales à probabilités p_A, p_B, avec un effet d'unité partagé (p_u = p + η_u) ; appariement par unité.
Exploratoire (R-546) : dimensionnement, aucune donnée réelle. Graines : SeedSequence."""
import json, math, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "orchestrateur-pole-v7"))
from pole import pari_apparie as pa

def contrastes_equivalence(epsilon, r_min):
    k = 1.0 / (1.0 + epsilon)
    return {"A_pas_au_dessus": ({"A": -k, "B": k}, epsilon * k), "B_pas_au_dessus": ({"A": k, "B": -k}, epsilon * k),
            "A_informe": ({"A": 1.0}, -r_min), "B_informe": ({"B": 1.0}, -r_min)}

def parts(rng, n, m, pA, pB, sigma_u=0.1):
    eta = rng.normal(0, sigma_u, size=n)
    rA = rng.binomial(m, np.clip(pA + eta, 0, 1)) / m
    rB = rng.binomial(m, np.clip(pB + eta, 0, 1)) / m
    return rA, rB

def course(rA, rB, epsilon, r_min, alpha=0.05, m_fiches=1):
    cs = contrastes_equivalence(epsilon, r_min)
    for c, k in cs.values():
        pa.verifier_coefficients(c, k)
    valeurs = {nom: [pa.contraste({"A": a, "B": b}, c, k) for a, b in zip(rA, rB)] for nom, (c, k) in cs.items()}
    return pa.evaluer(valeurs, alpha=alpha, m=m_fiches)

def main():
    ss = np.random.SeedSequence(2026102805)
    out = {"manifeste": {"script": "calculs_equivalence_v1.py", "entropie": 2026102805, "repetitions": 400, "m_episodes": 10, "sigma_unite": 0.1,
                         "alpha": 0.05, "r_min": 0.2}, "frontiere_du_nul": {}, "equivalence_vraie": {}, "muets": {}}
    R, m, r_min = 400, 10, 0.2
    for eps in (0.05, 0.10, 0.20):
        for n in (50, 100, 200):
            for ecart in (eps, 1.5 * eps):  # frontière, puis au-delà
                rng = np.random.default_rng(ss.spawn(1)[0])
                faux = 0
                for _ in range(R):
                    rA, rB = parts(rng, n, m, 0.6 + ecart / 2, 0.6 - ecart / 2)
                    faux += course(rA, rB, eps, r_min)["promue"]
                out["frontiere_du_nul"][f"eps={eps},n={n},ecart={ecart:.3f}"] = {"part_fausses_equivalences": faux / R,
                                                                                 "borne_haute_95": min(1.0, faux / R + 1.96 * math.sqrt(0.05 * 0.95 / R))}
            rng = np.random.default_rng(ss.spawn(1)[0])
            promues, instants = 0, []
            for _ in range(R):
                rA, rB = parts(rng, n, m, 0.6, 0.6)
                r = course(rA, rB, eps, r_min)
                promues += r["promue"]
                if r["promue"]:
                    instants.append(r["instant_d_arret"])
            out["equivalence_vraie"][f"eps={eps},n={n}"] = {"puissance": promues / R,
                                                             "instant_median": (float(np.median(instants)) if instants else None)}
    for p_muet in (0.0, 0.1):
        rng = np.random.default_rng(ss.spawn(1)[0])
        promues = sum(course(*parts(rng, 200, m, p_muet, p_muet), 0.10, r_min)["promue"] for _ in range(R))
        out["muets"][f"p={p_muet},n=200,eps=0.10"] = {"part_promues": promues / R, "attendu": "0 : la garde d'information (r_min = 0,2) refuse"}
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1); print()

if __name__ == "__main__":
    main()
