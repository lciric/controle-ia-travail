"""Contre-exemple calculé : la lecture dense (tous les dix tirages) ne promeut pas tout ce que le v9 promeut — v1.

Réfutation, mise au point exploratoire, aucune revendication. Les instants de la lecture dense de l'auteur sont 10, 20, …,
200 ; ceux du juge sont 25, 50, …, 200. Les instants 25, 75, 125 et 175 ne sont pas des multiples de 10 : la lecture dense
n'est pas un sur-ensemble de la lecture du juge. Elle reste valide (Ville borne tous les instants), mais la phrase « ne peut
que promouvoir plus » n'est pas vraie trajectoire par trajectoire.
Construction (mondes « tranchants » du réfutateur, `attaque_universelle_v1.py`) : la carte parie au tirage 23 (indice 22),
gain de probabilité 1/22, puis au tirage 27 (indice 26), gain de probabilité 1/22. À l'instant 25, la richesse vaut 22 si
le premier pari est gagné : le juge promeut. À l'instant 20 rien n'est encore parié ; à l'instant 30 le second pari est
presque toujours perdu et la richesse est presque nulle : la lecture dense ne promeut que si les deux paris sont gagnés.
Usage : python contre_exemple_lecture_dense_v1.py MONDES SORTIE.json [processus]
Graines : SeedSequence(entropy=2026111574, spawn_key=(0, r)), scindée en (monde, issues, parts)."""
import json, os, sys, time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import numpy as np  # noqa: E402
import attaque_universelle_v1 as a  # noqa: E402

ENTROPIE = 2026111574


def paris(parts, rng):
    return [(22, 1.0 / 22.0), (26, 1.0 / 22.0)]


def un_monde(r):
    s_monde, s_issues, s_parts = np.random.SeedSequence(entropy=ENTROPIE, spawn_key=(0, r)).spawn(3)
    parts = a.tirer_parts(np.random.default_rng(s_parts), 200)
    w = a.monde_tranchant(np.random.default_rng(s_monde), paris, parts)
    y = a.tirer_issues(np.random.default_rng(s_issues), w["P"])
    Q = a.carte_loterie(w["P"], [(i, 2) for i, _ in w["paris"]])
    res = a.juger(w, y, Q, parts, ("v9", "dense"))
    return bool(res["v9"][0]), bool(res["dense"][0]), bool(y[22] == 2), bool(y[26] == 2)


def main():
    R, sortie = int(sys.argv[1]), sys.argv[2]
    processus = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    if os.path.exists(sortie):
        raise SystemExit("sortie existante, jamais écrasée")
    import multiprocessing as mp
    t0 = time.time()
    with mp.get_context("fork").Pool(processus) as pool:
        res = pool.map(un_monde, range(R), chunksize=50)
    v9 = np.array([x[0] for x in res]); dense = np.array([x[1] for x in res])
    premier = next((r for r, x in enumerate(res) if x[0] and not x[1]), None)
    doc = {"essai": "contre-exemple : lecture dense contre lecture du juge", "mondes": R,
           "graines": {"entropie": ENTROPIE, "spawn_key": f"(0, r), r = 0..{R - 1}", "scission": "(monde, issues, parts)"},
           "instants_du_juge": list(a.instants_de(200)), "instants_denses": list(range(10, 201, 10)),
           "v9": {"promotions": int(v9.sum()), "taux": round(float(v9.mean()), 5), "intervalle_clopper_pearson_95": a.clopper_pearson(int(v9.sum()), R)},
           "dense": {"promotions": int(dense.sum()), "taux": round(float(dense.mean()), 5),
                     "intervalle_clopper_pearson_95": a.clopper_pearson(int(dense.sum()), R)},
           "promue_par_le_v9_et_pas_par_la_lecture_dense": int((v9 & ~dense).sum()),
           "promue_par_la_lecture_dense_et_pas_par_le_v9": int((dense & ~v9).sum()),
           "premier_monde_contre_exemple": premier,
           "premier_pari_gagne": int(sum(1 for x in res if x[2])), "deux_paris_gagnes": int(sum(1 for x in res if x[2] and x[3])),
           "duree_s": round(time.time() - t0, 1)}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(json.dumps(doc, ensure_ascii=False))


if __name__ == "__main__":
    main()
