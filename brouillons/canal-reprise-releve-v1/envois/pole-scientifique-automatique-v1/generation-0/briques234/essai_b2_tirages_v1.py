"""Brique 2, essai 3 : comparaison des noyaux par sélection gloutonne du déterminant maximal.

200 corpus synthétiques par configuration, n = 20, k = 4. Méthodes : hasard, tri par qualité,
forme du rapport (déterminant signé, |det| comme la caste 1, glouton par Cholesky, Sinkhorn + gamma
minimal), forme trace, correctif, et trois façons de réintroduire le partage d'opérateur.
Usage : python3 -I -B essai_b2_tirages_v1.py --heure "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
"""
import argparse
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
import numpy as np

import commun_v1 as cm
import corpus_articles_v1 as ca

N, K, TIRAGES, GAMMA_C = 20, 4, 200, 1e-3


def q_operateur(c):
    """Partenaires bisociatifs par article : même opérateur, autre domaine (étiquettes)."""
    n = len(c["q"])
    s = np.array([sum(1 for j in range(n) if j != i and c["op"][j] == c["op"][i] and c["dom"][j] != c["dom"][i])
                  for i in range(n)], dtype=float)
    return s / max(1.0, s.max())


def conditionnel(c, lc):
    """Opérateur-pivot choisi d'abord (le plus de domaines distincts, puis la somme des q), puis glouton
    du correctif dans cette strate, complété sur tout le corpus."""
    meilleur, cle = None, None
    for w in np.unique(c["op"]):
        membres = np.where(c["op"] == w)[0]
        k_w = (len(set(c["dom"][membres])), float(c["q"][membres].sum()))
        if cle is None or k_w > cle:
            meilleur, cle = w, k_w
    membres = list(np.where(c["op"] == meilleur)[0])
    s = cm.glouton_det(lc, min(K, len(membres)), "signe", candidats=membres)
    return cm.glouton_det(lc, K, "signe", deja=s), int(meilleur)


def apres_tirage(c, lc):
    """Ordre glouton complet du correctif, puis on garantit une paire même opérateur / autre domaine
    au rang le plus précoce possible ; le reste suit l'ordre glouton."""
    ordre = cm.glouton_det(lc, N, "signe")
    rang = {a: r for r, a in enumerate(ordre)}
    best = None
    for i in range(N):
        for j in range(i + 1, N):
            if c["op"][i] == c["op"][j] and c["dom"][i] != c["dom"][j]:
                cle = (max(rang[i], rang[j]), rang[i] + rang[j])
                if best is None or cle < best[0]:
                    best = (cle, i, j)
    if best is None:
        return ordre[:K]
    s = [best[1], best[2]]
    for a in ordre:
        if len(s) == K:
            break
        if a not in s:
            s.append(a)
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heure", required=True)
    args = ap.parse_args()
    t0 = time.time()
    methodes = ["aleatoire", "tri_qualite", "a_det_signe", "a_det_abs_caste1", "a_sinkhorn_gamma_min",
                "b_trace", "c_correctif", "c_qualite_operateur", "c_conditionnel_operateur", "c_apres_tirage"]
    resultats = {}
    for config, cid in ca.CONFIGS.items():
        acc = {m: [] for m in methodes}
        echecs_chol, echecs_chol_numpy, existe_bisoc, nb_dom_dispo, egalites_etape1_a = 0, 0, 0, [], 0
        for r in range(TIRAGES):
            c = ca.corpus(cm.generateur("b2_tirages", cid, r), config, N)
            rng_h = cm.generateur("b2_tirages", cid, r, 1)
            la = cm.noyau_rapport(c["d"], c["o"], c["q"])
            lb = cm.noyau_trace_ferme(c["d"], c["o"], c["q"])
            lc = cm.noyau_correctif(c["d"], c["q"], GAMMA_C)
            sel = {}
            sel["aleatoire"] = list(rng_h.choice(N, K, replace=False))
            sel["tri_qualite"] = list(np.argsort(-c["q"])[:K])
            if np.allclose(np.diag(la), 0.0, atol=1e-12):
                egalites_etape1_a += 1
            sel["a_det_signe"] = cm.glouton_det(la, K, "signe")
            sel["a_det_abs_caste1"] = cm.glouton_det(la, K, "abs")
            _, echec = cm.glouton_cholesky(la, K)
            echecs_chol += int(echec)
            try:
                np.linalg.cholesky(la)
            except np.linalg.LinAlgError:
                echecs_chol_numpy += 1
            psym, _, _ = cm.sinkhorn_knopp(la, 5)
            gmin = -np.linalg.eigvalsh(psym).min() + 1e-9
            sel["a_sinkhorn_gamma_min"] = cm.glouton_det(psym + gmin * np.eye(N), K, "signe")
            sel["b_trace"] = cm.glouton_det(lb, K, "signe")
            sel["c_correctif"] = cm.glouton_det(lc, K, "signe")
            qo = c["q"] * (1.0 + q_operateur(c))
            sel["c_qualite_operateur"] = cm.glouton_det(cm.noyau_correctif(c["d"], qo, GAMMA_C), K, "signe")
            sel["c_conditionnel_operateur"], _ = conditionnel(c, lc)
            sel["c_apres_tirage"] = apres_tirage(c, lc)
            existe_bisoc += int(any(c["op"][i] == c["op"][j] and c["dom"][i] != c["dom"][j]
                                    for i in range(N) for j in range(i + 1, N)))
            nb_dom_dispo.append(len(set(c["dom"])))
            for m in methodes:
                acc[m].append(ca.mesures_ensemble(c, sel[m]))
        resume = {}
        for m in methodes:
            tab = {k: np.array([x[k] for x in acc[m]]) for k in acc[m][0]}
            resume[m] = {k: {"moyenne": float(v.mean()), "erreur_type": float(v.std(ddof=1) / np.sqrt(len(v)))}
                         for k, v in tab.items()}
        resultats[config] = {
            "methodes": resume,
            "echecs_glouton_cholesky_forme_rapport": echecs_chol,
            "echecs_numpy_cholesky_forme_rapport": echecs_chol_numpy,
            "corpus_diagonale_nulle_forme_rapport": egalites_etape1_a,
            "corpus_ou_une_paire_bisociative_existe": existe_bisoc,
            "domaines_disponibles_moyenne": float(np.mean(nb_dom_dispo)),
        }
        print(config, "fait", round(time.time() - t0, 1), "s")
    sortie = {
        "essai": "brique 2, essai 3 (sélection gloutonne)",
        "heure_lancement_utc": args.heure,
        "duree_s": round(time.time() - t0, 1),
        "graines": cm.description_graines() | {"tache": "b2_tirages",
                                               "spawn_key": "(3, id_config, r) corpus ; (3, id_config, r, 1) hasard"},
        "versions": cm.versions(),
        "parametres": {"n": N, "k": K, "corpus_par_config": TIRAGES, "gamma_correctif": GAMMA_C,
                       "domaines": ca.N_DOM, "operateurs": ca.N_OP, "dimension": ca.DIM, "bruit": ca.BRUIT,
                       "configs": {"uniforme": "domaines et opérateurs uniformes indépendants",
                                   "hubs": "domaines [0,4 0,25 0,15 0,1 0,1], opérateurs Zipf s = 1,2",
                                   "correle": "opérateur « maison » du domaine avec probabilité 0,6"},
                       "egalites": "glouton : premier indice en cas d'égalité",
                       "metriques": {"div_dom": "part des 6 paires de domaines différents",
                                     "meme_op": "ensemble avec au moins deux articles au même opérateur",
                                     "bisoc": "ensemble avec une paire même opérateur ET domaines différents",
                                     "p2": "part des paires <d,d> < 0,25 et <o,o> > 0,5 (critère P2 du rapport)",
                                     "q_moy": "qualité moyenne des choisis"}},
        "resultats": resultats,
    }
    cm.ecrire_json(cm.SORTIE / "resultats-b2-tirages-v1.json", sortie)
    print("fini", sortie["duree_s"], "s")


if __name__ == "__main__":
    main()
