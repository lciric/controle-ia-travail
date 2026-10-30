"""Identité de bout en bout de la v8 avec la v7 (GD7-04 : comprend le chemin `--K-s` produit cartésien, K_s ≠ K_h, l'analyse des options et la retenue e-BH).

Chaque cas lance `principal()` du script v7 puis celui du script v8, dans ce processus, avec les mêmes options (300 ou 200 répétitions), sortie standard capturée ;
la v7 est chargée par `importlib`, son `etat_git` est remplacé par une fonction qui ne lance rien (la v7 appelle git ; ici aucune commande git n'est exécutée) ;
la v8 n'a aucune commande git. Sont comparés **feuille à feuille, exactement** : `cellules`, `lois`, `taille_minimale_ecarts_nuls`, `lecture_ebh`, `statut`, et `reglages`
(sauf les 13 champs de réglage ajoutés par la v8, listés dans `NOUVEAUX`). Les champs propres à `version`,
`script_sha256`, `commit`, `etat_du_script`, `environnement` sont exclus (différents par construction).
Témoins négatifs (R5) : (a) graine différente → cellules différentes ; (b) `--rho-comparateurs 0.17` de la v8 contre `--effet-unite-comparateurs 1.0` bêta de la v7
(ρ 0,17 contre 0,1696) → cellules différentes.

Usage : python3 -I -B verif-identite-v7-v8.py SCRIPT_V7 SCRIPT_V8 SORTIE.json
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import sys
import time

CHEMIN_V7, CHEMIN_V8, SORTIE = sys.argv[1:4]
if not sys.flags.dont_write_bytecode:
    raise SystemExit("lancer avec -B")


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


v7, v8 = charger("v7", CHEMIN_V7), charger("v8", CHEMIN_V8)
v7.etat_git = lambda chemin: {"commit": None, "etat_du_script": "git neutralisé (vérification d'identité)"}


def lancer(mod, argv):
    ancien = sys.argv
    sys.argv = ["x"] + argv
    tampon = io.StringIO()
    try:
        with contextlib.redirect_stdout(tampon):
            mod.principal()
    finally:
        sys.argv = ancien
    return json.loads(tampon.getvalue())


def feuilles(x, prefixe=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from feuilles(v, f"{prefixe}/{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from feuilles(v, f"{prefixe}[{i}]")
    else:
        yield prefixe, x


BASE = ["--comparateurs", "8", "--taux", "0.01", "--deltas", "0.05", "--biais", "0,0.0125", "--tailles", "288", "--lecture-ebh", "A", "--m", "8,2", "--sans-n80",
        "--repetitions", "300", "--K", "10,5", "--K-s", "10,5,3"]
CAS = [
    ("sans dispersion, K_h × K_s = {10, 5} × {10, 5, 3}", BASE),
    ("logit σ = 1,0", BASE + ["--effet-unite-comparateurs", "1.0"]),
    ("bêta de κ de σ = 1,0", BASE + ["--effet-unite-comparateurs", "1.0", "--echelle-dispersion", "beta"]),
    ("A bêta ρ = 0,17 seul", BASE + ["--effet-unite-beta", "0.17"]),
    ("A logit 1,0 et B bêta σ = 0,5, lien coupé", ["--comparateurs", "4", "--taux", "0.01", "--deltas", "0.05", "--biais", "0.0125", "--tailles", "120", "--lecture-ebh", "A",
                                                   "--m", "8,2", "--sans-n80", "--repetitions", "300", "--K", "5", "--K-s", "5,3", "--effet-unite-a", "1.0",
                                                   "--effet-unite-comparateurs", "0.5", "--echelle-dispersion", "beta", "--lien-coupe"]),
    ("lectures A,B avec 2 fiches nulles, bêta σ = 0,5, n80 de la garde", ["--comparateurs", "3", "--taux", "0.01", "--deltas", "0.05", "--biais", "0.0125", "--tailles", "100",
                                                                       "--lecture-ebh", "A,B", "--fiches-nulles", "2", "--m", "2", "--repetitions", "200", "--K", "5", "--K-s", "3",
                                                                       "--effet-unite-comparateurs", "0.5", "--echelle-dispersion", "beta"]),
    ("deux τ, deux K apparié (--K-sabotes), n80 de la garde", ["--comparateurs", "2", "--taux", "0.01,0.10", "--deltas", "0.05", "--biais", "0", "--tailles", "64", "--m", "8,1",
                                                              "--repetitions", "200", "--K", "10,3", "--K-sabotes", "5,3"]),
]
IGNORES = {"/version", "/script_sha256", "/commit", "/etat_du_script", "/environnement/duree_s", "/environnement/python", "/environnement/numpy"}
NOUVEAUX = {"/reglages/" + k for k in ("rho_comparateurs", "combiner_dispersion_a_et_comparateurs", "n80_fiche", "commit_declare", "correlation_sujet_comparateurs",
                                       "strates", "strates_parametres", "amplitude_strates", "portee_strates", "allocation_strates", "calibrage_par_strate", "cibles_n80[0]", "ecart_contraste_neuvieme")}


def comparer(s7, s8):
    f7, f8 = dict(feuilles(s7)), dict(feuilles(s8))
    f7 = {k: v for k, v in f7.items() if k not in IGNORES}
    f8 = {k: v for k, v in f8.items() if k not in IGNORES}
    propres_v8 = sorted(k for k in f8 if k not in f7)
    propres_v7 = sorted(k for k in f7 if k not in f8)
    communs = [k for k in f7 if k in f8]
    differents = [k for k in communs if f7[k] != f8[k]]
    return {"champs_communs": len(communs), "champs_differents": len(differents), "exemples_differents": differents[:5],
            "champs_propres_v8": propres_v8, "champs_propres_v7": propres_v7,
            "propres_v8_attendus": set(propres_v8) == NOUVEAUX, "cellules": len(s8["cellules"])}


t0 = time.time()
sortie = {"script_v7_sha256": hashlib.sha256(open(CHEMIN_V7, "rb").read()).hexdigest(), "script_v8_sha256": hashlib.sha256(open(CHEMIN_V8, "rb").read()).hexdigest(),
          "numpy": v8.np.__version__, "cas": [], "temoins_negatifs": {}}
for nom, args in CAS:
    c = comparer(lancer(v7, args), lancer(v8, args))
    c["cas"], c["options"] = nom, args
    c["conforme"] = c["champs_differents"] == 0 and not c["champs_propres_v7"] and c["propres_v8_attendus"]
    sortie["cas"].append(c)
    print(nom, c["cellules"], "cellules", c["champs_communs"], "champs", c["champs_differents"], "différents", c["conforme"], flush=True)

a = comparer(lancer(v7, BASE), lancer(v8, BASE + ["--graine", "1"]))
sortie["temoins_negatifs"]["graine_differente"] = {"champs_differents": a["champs_differents"], "champs_communs": a["champs_communs"], "decele": a["champs_differents"] > 0}
args7 = ["--comparateurs", "8", "--taux", "0.01", "--deltas", "0.05", "--biais", "0.0125", "--tailles", "288", "--lecture-ebh", "A", "--m", "8,2", "--sans-n80",
         "--repetitions", "300", "--K", "5", "--K-s", "10"]
b7 = lancer(v7, args7 + ["--effet-unite-comparateurs", "1.0", "--echelle-dispersion", "beta"])
b8 = lancer(v8, args7 + ["--rho-comparateurs", "0.17", "--echelle-dispersion", "beta"])
c7, c8 = list(b7["cellules"].values())[0], list(b8["cellules"].values())[0]
sortie["temoins_negatifs"]["rho_0_17_contre_sigma_1_0"] = {"noms_des_lois": [list(b7["lois"]), list(b8["lois"])],
                                                           "cellules_differentes": json.dumps(c7["moments_tires"], sort_keys=True) != json.dumps(c8["moments_tires"], sort_keys=True),
                                                           "decele": json.dumps(c7["moments_tires"], sort_keys=True) != json.dumps(c8["moments_tires"], sort_keys=True)}
sortie["conforme"] = all(c["conforme"] for c in sortie["cas"]) and all(t["decele"] for t in sortie["temoins_negatifs"].values())
sortie["champs_communs_total"] = sum(c["champs_communs"] for c in sortie["cas"])
sortie["cellules_total"] = sum(c["cellules"] for c in sortie["cas"])
sortie["duree_s"] = round(time.time() - t0, 1)
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(sortie, f, indent=1, ensure_ascii=False, default=list)
    f.write("\n")
print("conforme" if sortie["conforme"] else "NON CONFORME", sortie["cellules_total"], "cellules,", sortie["champs_communs_total"], "champs comparés")
