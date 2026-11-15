"""D'où vient le prix du v9 du banc ? Contrôle de la lecture de l'auteur, sur son banc, base changée seule — v1.

Réfutation, mise au point exploratoire, aucune revendication. L'auteur lit l'écart « v8 → nul limité » de ses mondes de
puissance comme le prix de la liberté des poids par morceau. Or la base de ces mondes est un membre « intérieur » du nul
limité : des poids différents de chaque côté de la coupure de l'archive. Cette base est hors de la classe du v8 (sans
coupure) : le v8 y promeut déjà des copies sans aucune composante neuve (cas « interieur » de sa table de taille).
Ici, le banc de l'auteur est rejoué tel quel (ses fonctions, son solveur, ses graines, son archive, son plan, sa loi neuve),
avec une seule différence : la base du monde. Deux bases sur les mêmes graines :
- « morceaux » : celle de l'auteur (poids a0 d'un côté de la coupure de l'archive, a1 de l'autre) — doit redonner ses mondes ;
- « sans_coupure » : les mêmes poids a0 des deux côtés (membre du nul sans coupure, donc de toutes les classes).
Doses : 0 (base seule, aucune composante neuve), 0,25, 0,40, 0,55. Méthodes : v8, limité, v9 du banc.
Une dose par lancement (chaque simulation tient en dix minutes).
Usage : python prix_par_morceau_v1.py DOSE MONDES SORTIE.json [processus]      (DOSE ∈ 0.25, 0.40, 0.55, 0.0)
Graines : celles de l'auteur, SeedSequence(entropy=20261115201, spawn_key=(indice de la dose, r)) ; la dose 0 prend la clé
(3, r), que l'auteur n'emploie pas."""
import json, os, sys, time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import numpy as np  # noqa: E402
import banc_universelle_v1 as b  # noqa: E402  (banc de l'auteur)
import attaque_universelle_v1 as a  # noqa: E402  (intervalles seulement)

DOSES = (0.25, 0.40, 0.55, 0.0)
ENTROPIE = 20261115201


def monde(lam, base, ss):
    """Même suite de tirages que `banc_universelle_v1.monde(("neuve", lam), ss)` ; seule la base peut changer."""
    rng = np.random.default_rng(ss)
    arch = b.tirer_archive(rng)
    z, g = b.tirer_plan(rng)
    Lc = b.lois_connues(arch, z)
    haut = z[:, arch["jA"]] > arch["sA"]
    a0, a1, r, be = b.poids_membre(rng, "interieur")
    if base == "sans_coupure":
        a1 = a0
    P = (1 - lam) * b.loi_membre(Lc, haut, a0, a1, r, be) + lam * b.probas_softmax(b.softmax_aleatoire(rng), z)
    P = np.maximum(P, 0.0); P /= P.sum(1, keepdims=True)
    y = b.tirer_issues(rng, P)
    return {"arch": arch, "z": z, "g": g, "Lc": Lc, "P": P, "Q": P.copy(), "y": y}


def un_monde(args):
    lam, i_dose, r = args
    s_monde, s_sous = np.random.SeedSequence(entropy=ENTROPIE, spawn_key=(i_dose, r)).spawn(2)
    out = {}
    for base in ("morceaux", "sans_coupure"):
        w = b.preparer(monde(lam, base, s_monde))
        res = b.evaluer(w, None, ("v8", "limite", "v9"))
        out[base] = {m: bool(np.max(lw) >= sl) for m, (lw, sl) in res.items()}
        if base == "morceaux" and lam > 0:
            ref = b.monde(("neuve", lam), s_monde)             # le monde de l'auteur, pour vérifier l'identité
            out["identique_au_monde_de_l_auteur"] = bool(np.array_equal(ref["y"], w["y"]) and np.allclose(ref["P"], w["P"]))
    return out


def main():
    dose, R, sortie = float(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    processus = int(sys.argv[4]) if len(sys.argv) > 4 else 2
    if os.path.exists(sortie):
        raise SystemExit("sortie existante, jamais écrasée")
    import multiprocessing as mp
    t0 = time.time()
    doc = {"essai": "prix du v9 du banc selon la base du monde (banc de l'auteur, base changée seule)", "mondes_par_dose": R,
           "graines": {"entropie": ENTROPIE, "spawn_key": "(indice de la dose, r) ; doses 0,25 / 0,40 / 0,55 : clés 0, 1, 2 de l'auteur ; dose 0 : clé 3"},
           "doses": {}}
    with mp.get_context("fork").Pool(processus) as pool:
        for i_dose, lam in enumerate(DOSES):
            if lam != dose:
                continue
            sorties = pool.map(un_monde, [(lam, i_dose, r) for r in range(R)], chunksize=4)
            d = {}
            for base in ("morceaux", "sans_coupure"):
                d[base] = {}
                for m in ("v8", "limite", "v9"):
                    k = int(sum(1 for s in sorties if s[base][m]))
                    d[base][m] = {"promotions": k, "mondes": R, "taux": round(k / R, 4), "intervalle_clopper_pearson_95": a.clopper_pearson(k, R)}
                for x, y_ in (("v8", "limite"), ("limite", "v9")):
                    seul_x = int(sum(1 for s in sorties if s[base][x] and not s[base][y_]))
                    seul_y = int(sum(1 for s in sorties if s[base][y_] and not s[base][x]))
                    d[base][f"ecart_{x}_vers_{y_}"] = {"ecart_de_taux": round((seul_y - seul_x) / R, 4), "promue_par_le_premier_seul": seul_x,
                                                       "promue_par_le_second_seul": seul_y}
            if lam > 0:
                d["mondes_identiques_a_ceux_de_l_auteur_base_morceaux"] = int(sum(1 for s in sorties if s["identique_au_monde_de_l_auteur"]))
            doc["doses"][str(lam)] = d
            print(lam, round(time.time() - t0, 1), "s", json.dumps({bq: {m: d[bq][m]["taux"] for m in ("v8", "limite", "v9")} for bq in ("morceaux", "sans_coupure")}), flush=True)
    doc["duree_s"] = round(time.time() - t0, 1)
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
