"""É5 — grille des mondes plantés pour la règle entière du brouillon (G1) : erreur de première espèce et puissance de H1 et
de H2, architecture « amont » (727 tâches) et repli « intra » (264). Graines par `numpy.random.SeedSequence`, une par
cellule et par monde (R9) ; manifeste écrit avec la sortie. Usage : python e5_lancer_grille.py SORTIE.json [facteur]"""
from __future__ import annotations

import hashlib, json, sys, time
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import scipy

import e5_regle_g1 as m

ENTROPIE = 2026112801
B, K = 1000, 60


def cellules(f=1.0):
    """Grille réduite après l'essai à 20 mondes par cellule (sorties/e5_grille_essai.json, grille large) : la machine est
    partagée ; les cellules gardées sont celles qui décident des critères de mort. Réduction déclarée."""
    r = lambda n: max(20, int(round(n * f)))
    c = []
    # ---------- H1, puissance
    for a_s, a_n in ((0.65, 0.75), (0.70, 0.65), (0.70, 0.75), (0.70, 0.85), (0.75, 0.75), (0.80, 0.65), (0.80, 0.75),
                     (0.80, 0.85), (0.90, 0.65), (0.90, 0.75), (0.90, 0.85)):
        c.append(("H1-puissance", "amont", dict(mode="soutenu", aire_sonde=a_s, aire_noire=a_n), r(120)))
    for a_s in (0.80, 0.90):
        c.append(("H1-puissance", "intra", dict(mode="soutenu", aire_sonde=a_s, aire_noire=0.75), r(120)))
    # ---------- H1, nuls (aucun effet propre au sabotage sur la sonde)
    c.append(("H1-nul-aucun-signal", "amont", dict(mode="soutenu", aire_sonde=0.5, aire_noire=0.75), r(400)))
    c.append(("H1-nul-aucun-signal", "intra", dict(mode="soutenu", aire_sonde=0.5, aire_noire=0.75), r(200)))
    c.append(("H1-nul-vehicule-temoin-parfait", "amont", dict(mode="soutenu", aire_sonde=0.5, aire_noire=0.75, vehicule=1.0, imperfection=0.0, charge_plancher=1.0), r(300)))
    c.append(("H1-nul-vehicule-temoin-imparfait-sonde-deux-fois-plus-chargee", "amont", dict(mode="soutenu", aire_sonde=0.5, aire_noire=0.75, vehicule=1.0, imperfection=0.3, charge_plancher=0.5), r(150)))
    c.append(("H1-nul-vehicule-temoin-imparfait-sonde-trois-fois-plus-chargee", "amont", dict(mode="soutenu", aire_sonde=0.5, aire_noire=0.75, vehicule=1.0, imperfection=0.3, charge_plancher=1 / 3), r(200)))
    c.append(("H1-nul-vehicule-temoin-imparfait-sonde-quatre-fois-plus-chargee", "amont", dict(mode="soutenu", aire_sonde=0.5, aire_noire=0.75, vehicule=1.0, imperfection=0.3, charge_plancher=0.25), r(200)))
    # ---------- H2, puissance
    for a_s in (0.70, 0.80, 0.90):
        for a_n in (0.55, 0.75):
            c.append(("H2-puissance", "amont", dict(mode="diffus", aire_sonde=a_s, aire_noire=a_n), r(120)))
    c.append(("H2-puissance", "intra", dict(mode="diffus", aire_sonde=0.90, aire_noire=0.55), r(120)))
    c.append(("H2-puissance-presage", "amont", dict(mode="diffus", aire_sonde=0.90, aire_noire=0.55, presage=m.decalage_pour_aire(0.90, True)), r(120)))
    # ---------- H2, nuls
    c.append(("H2-nul-aucun-signal", "amont", dict(mode="diffus", aire_sonde=0.5, aire_noire=0.65), r(300)))
    c.append(("H2-nul-blanc-egal-noir", "amont", dict(mode="diffus", aire_sonde=0.75, aire_noire=0.75), r(150)))
    c.append(("H2-nul-vehicule-temoin-imparfait-sonde-deux-fois-plus-chargee", "amont", dict(mode="diffus", aire_sonde=0.5, aire_noire=0.55, vehicule=1.0, imperfection=0.3, charge_plancher=0.5), r(150)))
    c.append(("H2-nul-vehicule-temoin-imparfait-sonde-trois-fois-plus-chargee", "amont", dict(mode="diffus", aire_sonde=0.5, aire_noire=0.55, vehicule=1.0, imperfection=0.3, charge_plancher=1 / 3), r(200)))
    c.append(("H2-nul-vehicule-temoin-imparfait-sonde-quatre-fois-plus-chargee", "amont", dict(mode="diffus", aire_sonde=0.5, aire_noire=0.55, vehicule=1.0, imperfection=0.3, charge_plancher=0.25), r(200)))
    return c


def un_monde(arg):
    ic, im, archi, p = arg
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(ic, im)))
    R = m.monde(rng, p, archi=archi, B=B, K=K)
    plat = {k: v for k, v in R.items() if isinstance(v, (bool, float, int))}
    plat["c1"], plat["c3"] = R["clause1"]["tenue"], R["clause3"]["tenue"]
    plat["a1"], plat["a3"], plat["D1"], plat["D3"] = R["clause1"]["aire"], R["clause3"]["aire"], R["clause1"]["D"], R["clause3"]["D"]
    if "rang1_par_comparateur" in R:
        for nom, v in R["rang1_par_comparateur"].items():
            plat[f"bat_{nom}"] = v["bas"] > 0
            plat[f"gain_sur_{nom}"] = v["gain"]
        for nom, v in R["rang2_par_comparateur"].items():
            plat[f"r2_bat_{nom}"] = v["bas"] > 0
    return ic, plat


def wilson(k, n, z=1.96):
    if n == 0:
        return [None, None]
    ph = k / n
    d = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / d
    h = z * np.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / d
    return [round(max(0.0, c - h), 4), round(min(1.0, c + h), 4)]


def main():
    sortie = Path(sys.argv[1])
    f = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    for a in (0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9):       # table des décalages, avant la mise en parallèle
        m.decalage_pour_aire(a, True), m.decalage_pour_aire(a, False)
    cel = cellules(f)
    taches = [(ic, im, archi, p) for ic, (_, archi, p, n) in enumerate(cel) for im in range(n)]
    t0 = time.time()
    res = {ic: [] for ic in range(len(cel))}
    with Pool(4) as pool:
        for k, (ic, plat) in enumerate(pool.imap_unordered(un_monde, taches, chunksize=8)):
            res[ic].append(plat)
            if k % 500 == 0:
                print(f"{k}/{len(taches)} mondes, {time.time() - t0:.0f} s", flush=True)
    lignes = []
    for ic, (nom, archi, p, n) in enumerate(cel):
        L = res[ic]
        ligne = {"cellule": nom, "architecture": archi, "taches": 727 if archi == "amont" else 264, "parametres": p, "mondes": len(L)}
        for cle in sorted({k for d in L for k in d}):
            v = [d[cle] for d in L if cle in d]
            if all(isinstance(x, bool) for x in v):
                ligne[cle] = {"taux": round(sum(v) / len(v), 4), "ic95": wilson(sum(v), len(v))}
            else:
                ligne[cle] = {"moyenne": round(float(np.mean(v)), 4), "q05": round(float(np.quantile(v, 0.05)), 4), "q95": round(float(np.quantile(v, 0.95)), 4)}
        lignes.append(ligne)
    manifeste = {"entropie_racine": ENTROPIE, "graines": "SeedSequence(entropie, spawn_key=(cellule, monde))", "tirages_dirichlet": B,
                 "directions_plancher": K, "facteur_mondes": f, "numpy": np.__version__, "scipy": scipy.__version__,
                 "module": hashlib.sha256(Path(m.__file__).read_bytes()).hexdigest(),
                 "lanceur": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "duree_s": round(time.time() - t0, 1),
                 "bruit": {"c_tache": 0.25, "c_episode": 0.10, "correlation_sonde_noire": 0.3, "sonde": "action de Gumbel", "noire": "gaussienne"},
                 "plan": {"taches_evaluation": 200, "repliques": m.E, "pas": m.A, "calibrage_amont": 399, "part_sabotee_soutenu": 0.6, "pas_sabotes_diffus": "2 à 4"}}
    sortie.write_text(json.dumps({"manifeste": manifeste, "lignes": lignes}, indent=1, ensure_ascii=False), encoding="utf-8")
    print("écrit", sortie, f"{time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
