"""Lot d'essais (taille ou puissance) de l'inférence universelle — v1. Remplace, pour les jeux après le premier, le
résumé de `essai_universelle_taille_v1.py` par un résumé qui garde aussi, monde par monde, la promotion et le log W
maximal de chaque méthode (appariements entre lots joués sur les mêmes mondes), et le détail des écarts de monotonie.
Les mondes sont ceux de `banc_universelle_v1.py` (inchangé, scellé) ; même graine et même clé ⇒ même monde d'un lot à
l'autre, quelles que soient les méthodes jouées.
Usage : python essai_universelle_lot_v1.py taille|puissance CAS MONDES METHODES SORTIE.json [fine]
  taille : CAS ∈ interieur, sommet, extreme, bruite, sous_population, grille, v8 ; entropie 20261115101 (celle de
           essai_universelle_taille_v1.py, mêmes clés (indice du cas, r)) ;
  puissance : CAS = λ ∈ {0.25, 0.40, 0.55} (monde = carte = (1 − λ)·membre intérieur + λ·loi neuve) ; entropie 20261115201 ;
  fine : grille de 19 seuils par trait (quantiles 0,05 à 0,95 de N(0, 1)) au lieu de 9 — l'archive peut alors différer
           (le seuil d'archive est tiré hors de la grille), les mondes ne sont plus appariés aux lots sans « fine ».
Mise au point exploratoire, aucune revendication."""
import hashlib, json, math, os, platform, subprocess, sys, time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import numpy as np  # noqa: E402
import banc_universelle_v1 as b  # noqa: E402

CAS_TAILLE = ("interieur", "sommet", "extreme", "bruite", "sous_population", "grille", "v8")
CAS_PUISSANCE = (("neuve", 0.25), ("neuve", 0.40), ("neuve", 0.55))
ENTROPIES = {"taille": 20261115101, "puissance": 20261115201}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def un_monde(args):
    cas, entropie, cle, methodes = args
    s_monde, s_sous = np.random.SeedSequence(entropy=entropie, spawn_key=cle).spawn(2)
    w = b.preparer(b.monde(cas, s_monde))
    res = b.evaluer(w, b.sous_ensembles(s_sous), methodes)
    traj = {m: res[m][0] for m in ("v8", "limite", "v9") if m in res}
    mono = None
    if len(traj) == 3:
        mono = float(max((traj["v9"] - traj["limite"]).max(), (traj["limite"] - traj["v8"]).max()))
    return {m: (bool(np.max(lw) >= sl), float(np.max(lw))) for m, (lw, sl) in res.items()}, mono


def main():
    sorte, cas_txt, R, methodes, sortie = sys.argv[1], sys.argv[2], int(sys.argv[3]), tuple(sys.argv[4].split(",")), sys.argv[5]
    fine = len(sys.argv) > 6 and sys.argv[6] == "fine"
    if os.path.exists(sortie):
        raise SystemExit(f"sortie existante, jamais écrasée : {sortie}")
    if fine:
        from scipy.stats import norm
        b.GRILLE = tuple(round(float(norm.ppf(q)), 4) for q in np.arange(0.05, 0.951, 0.05))
    if sorte == "taille":
        cas = cas_txt; i_cas = CAS_TAILLE.index(cas)
    else:
        cas = ("neuve", float(cas_txt)); i_cas = CAS_PUISSANCE.index(cas)
    entropie = ENTROPIES[sorte]
    import multiprocessing as mp
    t0 = time.time()
    with mp.get_context("fork").Pool(3) as pool:
        sorties = pool.map(un_monde, [(cas, entropie, (i_cas, r), methodes) for r in range(R)], chunksize=4)
    duree = time.time() - t0
    resume, par_monde = {}, {}
    for m in methodes:
        pro = [s[0][m][0] for s in sorties]; mx = np.array([s[0][m][1] for s in sorties]); k = int(sum(pro))
        resume[m] = {"mondes": R, "promotions": k, "taux": round(k / R, 4), "intervalle_clopper_pearson_95": b.clopper_pearson(k, R),
                     "log_w_max_plus_grand": round(float(mx.max()), 4), "log_w_max_median": round(float(np.median(mx)), 4)}
        par_monde[m] = {"promue": "".join("1" if p else "0" for p in pro), "log_w_max": [round(float(v), 4) for v in mx]}
    monos = [s[1] for s in sorties if s[1] is not None]
    controles = {}
    if monos:
        monos = np.array(monos)
        controles = {"monotonie_plus_grand_exces_nat": round(float(monos.max()), 6),
                     "mondes_exces_au_dela_de_0.01_nat": int((monos > 1e-2).sum()),
                     "mondes_exces_au_dela_de_0.001_nat": int((monos > 1e-3).sum())}
    commit = subprocess.run(["git", "-C", ICI, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    doc = {"essai": sorte, "version": "v1", "cas": cas if isinstance(cas, str) else list(cas), "mondes": R,
           "methodes": list(methodes), "grille": list(b.GRILLE), "grille_fine": fine,
           "graines": {"entropie": entropie, "spawn_key": f"({i_cas}, r) pour r = 0..{R - 1}, scindée en (monde, sous-ensembles)",
                       "generateur": "numpy.random.default_rng(SeedSequence)"},
           "niveau": {"alpha": b.ALPHA, "instants": list(b.INSTANTS), "tirages": b.N, "seuil_log": b.SEUIL,
                      "seuil_log_confiance": b.SEUIL_CONFIANCE, "beta_confiance": b.BETA_CONFIANCE},
           "reglages": {"tolerance_groupe": b.TOL_GROUPE, "iterations_max": b.ITER_MAX, "lambdas": list(b.LAMBDAS),
                        "sous_echantillons": b.B_SOUS, "d_libres": b.D_LIBRES, "processus": 3},
           "resume": resume, "controles": controles, "par_monde": par_monde, "duree_s": round(duree, 1),
           "versions": {"python": platform.python_version(), "numpy": np.__version__}, "commit_depot": commit,
           "empreintes_code": {"banc_universelle_v1.py": sha(os.path.join(ICI, "banc_universelle_v1.py")),
                               os.path.basename(__file__): sha(os.path.abspath(__file__))}}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=0)
    print(json.dumps({m: (v["taux"], v["intervalle_clopper_pearson_95"]) for m, v in resume.items()}, ensure_ascii=False))
    print("durée", round(duree, 1), "s", controles)


if __name__ == "__main__":
    main()
