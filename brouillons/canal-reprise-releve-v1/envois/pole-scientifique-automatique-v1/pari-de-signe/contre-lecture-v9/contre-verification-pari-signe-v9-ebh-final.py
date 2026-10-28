"""Contre-vérification v9, section H : la lecture e-BH pondérée de l'état final publié (`course.json`, 5c5098ea…),
recalculée par `pari_apparie.ebh_pondere`, avec et sans les doublons d'affirmation, et sans les fiches « hasard »
(budgets inchangés : illustration de la dépendance au rembourrage, pas une course refaite).
Usage : /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v9-ebh-final.py RACINE_POLE > sortie.json"""
import hashlib, json, math, sys
R = sys.argv[1]
sys.path.insert(0, R + "/orchestrateur-pole-v7")
from pole import pari_apparie as pa  # noqa: E402
chemin = R + "/pari-de-signe/demonstration-v27/course.json"
c = json.load(open(chemin, encoding="utf-8"))
le, b = c["log_e"], {f: math.exp(-s) for f, s in c["seuils_log"].items()}
def lire(fiches):
    return sorted(pa.ebh_pondere({f: le[f] for f in fiches}, {f: b[f] for f in fiches}, 0.05))
doublons = ("hasard-g1-3", "hasard-g2-3", "hasard-g3-2")
out = {"sha256_course_json": hashlib.sha256(open(chemin, "rb").read()).hexdigest(),
       "toutes": lire(list(le)), "sans_les_trois_doublons_promus": lire([f for f in le if f not in doublons]),
       "sans_fiches_hasard": lire([f for f in le if not f.startswith("hasard")]),
       "k_etoile_necessaire": {f: math.ceil(1 / (b[f] * math.exp(le[f])) - 1e-12) for f in
                                ("G1", "temoin-vrai-fort", "temoin-vrai-moyen", "temoin-vrai-faible", "temoin-vrai-concentre", "temoin-faux-nul")},
       "bonferroni": sorted(f for f in le if le[f] >= -math.log(b[f]) - 1e-12)}
json.dump(out, sys.stdout, ensure_ascii=False, indent=1, sort_keys=True); print()
