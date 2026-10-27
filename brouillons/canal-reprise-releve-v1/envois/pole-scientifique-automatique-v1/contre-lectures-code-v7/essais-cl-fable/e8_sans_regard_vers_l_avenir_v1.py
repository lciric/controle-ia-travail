"""E8 : aucune lecture de l'avenir. Pour l'évaluateur du juge (`selection_pari.evaluer`) et celui du nul des filles v2
(`nul_filles_v2.evaluer_v2`), avec une bibliothèque qui contient **tous** les membres en jeu sur une banque (marginale
ajustée, uniforme, moyennes glissantes, urne, prédicteur connu, survivante d'archive et son mélange, membres ajustés
linéaire et logarithmique), le numérateur plein et le numérateur à fraction : on vérifie que log W aux instants ≤ t ne
change pas quand on remplace au hasard les issues d'indice > t (propriété de préfixe), pour tout t.

Usage : python -I -B e8_sans_regard_vers_l_avenir_v1.py COPIE_DU_CODE SORTIE.json
"""
import json
import random
import sys

COPIE, SORTIE = sys.argv[1], sys.argv[2]
sys.path.insert(0, COPIE)
from pole import nul_filles_v2 as nf  # noqa: E402
from pole import selection_pari as sp  # noqa: E402

rng = random.Random(4242)
k, d, n = 3, 4, 40
instances = sp.tirer_instances(rng, n, d)
loi = sp.loi_softmax_aleatoire(rng, k, d)
connu = sp.loi_softmax_aleatoire(rng, k, d)
archive = sp.loi_softmax_aleatoire(rng, k, d)
bibliotheque = list(sp.BIBLIOTHEQUE_STANDARD_V1) + [
    {"nom": "connu:M", "type": "loi", "loi": connu},
    {"nom": "archive:X", "type": "loi", "loi": archive},
    {"nom": "archive_couvert:X", "type": "melange_lois", "lois": [archive, {"type": "fixe", "probas": [1.0] * k}],
     "grille": list(sp.GRILLE_MELANGE)}]
ajustes = [{"nom": "ajuste_lineaire:archive", "type": "ajuste_lineaire", "lois": [archive, connu]},
           {"nom": "ajuste_log:archive:X", "type": "ajuste_log", "lois": [archive]}]
echecs, verifs = [], 0
for numerateur in ("plein", "fraction"):
    for evaluateur in ("evaluer", "evaluer_v2"):
        if evaluateur == "evaluer":
            e = sp.construire_engagement("F", loi, instances, k, 0.05, bibliotheque, "continu", plan_execution="ordre_naturel")
        else:
            e = nf.construire_engagement_v2("F", loi, instances, k, 0.05, bibliotheque + ajustes, 0, None,
                                            list(range(1, n + 1)), "ordre_naturel")
        if numerateur == "fraction":
            e["fractions"] = list(sp.GRILLE_FRACTIONS)
        gele = sp.geler_engagement(e)
        base = [rng.randrange(k) for _ in range(n)]
        fonction = sp.evaluer if evaluateur == "evaluer" else nf.evaluer_v2
        ref = fonction(gele, {"empreinte_engagement": gele.empreinte, "issues": base})["trajectoire_log_w"]
        for t in range(n - 1):
            for _ in range(5):
                autre = base[:t + 1] + [rng.randrange(k) for _ in range(n - t - 1)]
                traj = fonction(gele, {"empreinte_engagement": gele.empreinte, "issues": autre})["trajectoire_log_w"]
                verifs += 1
                if traj[:t + 1] != ref[:t + 1]:
                    echecs.append({"numerateur": numerateur, "evaluateur": evaluateur, "t": t})
resultat = {"verifications": verifs, "echecs": echecs[:10], "nombre_echecs": len(echecs),
            "conclusion": "aucune lecture de l'avenir" if not echecs else "LECTURE DE L'AVENIR"}
with open(SORTIE, "w", encoding="utf-8") as f:
    json.dump(resultat, f, ensure_ascii=False, indent=1)
print(json.dumps(resultat, ensure_ascii=False, indent=1))
