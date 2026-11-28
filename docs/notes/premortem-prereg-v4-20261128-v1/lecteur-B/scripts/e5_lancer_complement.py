"""É5 — complément de la grille : (a) garde des prédicteurs triviaux à la séparation de longueur relevée sur les données
réelles (0,60) ; (b) sonde et boîte noire à erreurs indépendantes (cas le plus favorable à la complémentarité) ;
(c) nul « véhicule » de taille double. Mêmes fonctions, graines SeedSequence(entropie, (1000 + cellule, monde))."""
import hashlib, json, sys, time
from multiprocessing import Pool
from pathlib import Path
import numpy as np
import e5_regle_g1 as m
import e5_lancer_grille as g

CELLULES = [
 ("H2-puissance-trivial-0,60", "amont", dict(mode="diffus", aire_sonde=0.90, aire_noire=0.55, sep_trivial=0.60), 100),
 ("H2-puissance-trivial-0,60", "amont", dict(mode="diffus", aire_sonde=0.80, aire_noire=0.55, sep_trivial=0.60), 100),
 ("H1-puissance-trivial-0,60", "amont", dict(mode="soutenu", aire_sonde=0.70, aire_noire=0.75, sep_trivial=0.60), 100),
 ("H1-puissance-erreurs-independantes", "amont", dict(mode="soutenu", aire_sonde=0.70, aire_noire=0.75, rho=0.0), 120),
 ("H1-puissance-erreurs-independantes", "amont", dict(mode="soutenu", aire_sonde=0.70, aire_noire=0.65, rho=0.0), 120),
 ("H1-nul-vehicule-double-temoin-imparfait-sonde-trois-fois-plus-chargee", "amont", dict(mode="soutenu", aire_sonde=0.5, aire_noire=0.75, vehicule=2.0, imperfection=0.3, charge_plancher=1 / 3), 150),
]

def un(arg):
    ic, im, archi, p = arg
    rng = np.random.default_rng(np.random.SeedSequence(g.ENTROPIE, spawn_key=(1000 + ic, im)))
    R = m.monde(rng, p, archi=archi, B=g.B, K=g.K)
    plat = {k: v for k, v in R.items() if isinstance(v, (bool, float, int))}
    plat["c1"], plat["c3"], plat["a1"], plat["sep1"] = R["clause1"]["tenue"], R["clause3"]["tenue"], R["clause1"]["aire"], R["clause1"]["sep_max"]
    return ic, plat

if __name__ == "__main__":
    for a in (0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.9):
        m.decalage_pour_aire(a, True), m.decalage_pour_aire(a, False)
    t0 = time.time()
    taches = [(ic, im, archi, p) for ic, (_, archi, p, n) in enumerate(CELLULES) for im in range(n)]
    res = {ic: [] for ic in range(len(CELLULES))}
    with Pool(4) as pool:
        for ic, plat in pool.imap_unordered(un, taches, chunksize=8):
            res[ic].append(plat)
    lignes = []
    for ic, (nom, archi, p, n) in enumerate(CELLULES):
        L = res[ic]; ligne = {"cellule": nom, "architecture": archi, "parametres": p, "mondes": len(L)}
        for cle in sorted({k for d in L for k in d}):
            v = [d[cle] for d in L if cle in d]
            if all(isinstance(x, bool) for x in v):
                ligne[cle] = {"taux": round(sum(v) / len(v), 4), "ic95": g.wilson(sum(v), len(v))}
            else:
                ligne[cle] = {"moyenne": round(float(np.mean(v)), 4)}
        lignes.append(ligne)
    Path(sys.argv[1]).write_text(json.dumps({"manifeste": {"entropie_racine": g.ENTROPIE, "graines": "SeedSequence(entropie, spawn_key=(1000 + cellule, monde))",
        "tirages_dirichlet": g.B, "directions_plancher": g.K, "module": hashlib.sha256(Path(m.__file__).read_bytes()).hexdigest(), "duree_s": round(time.time() - t0, 1)},
        "lignes": lignes}, indent=1, ensure_ascii=False), encoding="utf-8")
    print("écrit", sys.argv[1], round(time.time() - t0), "s")
