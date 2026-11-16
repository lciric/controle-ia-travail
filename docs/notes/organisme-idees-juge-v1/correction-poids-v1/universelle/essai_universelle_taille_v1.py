"""Essai de taille (inférence universelle, correction des poids du nul) — v1.

Un cas par appel (chaque simulation tient en dix minutes) : copie exacte d'un membre du nul (la carte est la loi du monde).
Cas : interieur, sommet, extreme, bruite (membres du nul limité, donc de toutes les classes du banc), sous_population,
grille (membres du v9 du banc seulement), v8. Graines : SeedSequence(entropy=ENTROPIE, spawn_key=(indice du cas, r)).
Usage : python essai_universelle_taille_v1.py CAS MONDES SORTIE.json [méthodes séparées par des virgules]
Mise au point exploratoire, aucune revendication."""
import hashlib, json, os, platform, subprocess, sys, time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import numpy as np  # noqa: E402
import banc_universelle_v1 as b  # noqa: E402

ENTROPIE = 20261115101
CAS = ("interieur", "sommet", "extreme", "bruite", "sous_population", "grille", "v8")


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    cas, R, sortie = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    methodes = tuple(sys.argv[4].split(",")) if len(sys.argv) > 4 else tuple(m for m in b.METHODES if m != "v9_dense")
    if os.path.exists(sortie):
        raise SystemExit(f"sortie existante, jamais écrasée : {sortie}")
    i_cas = CAS.index(cas)
    t0 = time.time()
    resume, controles, apparies = b.jouer(cas, R, methodes, ENTROPIE, i_cas, processus=3)
    duree = time.time() - t0
    commit = subprocess.run(["git", "-C", ICI, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    doc = {"essai": "taille", "version": "v1", "cas": cas, "mondes": R, "methodes": list(methodes),
           "graines": {"entropie": ENTROPIE, "spawn_key": f"({i_cas}, r) pour r = 0..{R - 1}, scindée en (monde, sous-ensembles)",
                       "generateur": "numpy.random.default_rng(SeedSequence)"},
           "niveau": {"alpha": b.ALPHA, "instants": list(b.INSTANTS), "tirages": b.N, "seuil_log": b.SEUIL,
                      "seuil_log_confiance": b.SEUIL_CONFIANCE, "beta_confiance": b.BETA_CONFIANCE},
           "reglages": {"tolerance_groupe": b.TOL_GROUPE, "iterations_max": b.ITER_MAX, "grille": list(b.GRILLE),
                        "lambdas": list(b.LAMBDAS), "sous_echantillons": b.B_SOUS, "d_libres": b.D_LIBRES},
           "resume": resume, "controles": controles, "apparies": apparies, "duree_s": round(duree, 1),
           "versions": {"python": platform.python_version(), "numpy": np.__version__}, "commit_depot": commit,
           "empreintes_code": {"banc_universelle_v1.py": sha(os.path.join(ICI, "banc_universelle_v1.py")),
                               os.path.basename(__file__): sha(os.path.abspath(__file__))}}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(json.dumps({m: (v["taux"], v["intervalle_clopper_pearson_95"]) for m, v in resume.items()}, ensure_ascii=False))
    print("durée", round(duree, 1), "s", controles)


if __name__ == "__main__":
    main()
