"""Calcul du devis de l'étage payant de la ligne 3 (votes effectifs des juges croisés) — v1.

Processeur seul, aucun appel de modèle, aucune dépense. Pièce de travail, brouillon 1,
à contre-lire.

Entrées, lues par ce programme et vérifiées par empreinte (arrêt si une empreinte
diffère) :
- le manifeste de fin du lanceur de la course d'auto-conception v9
  (runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json),
  champs cout_reel.par_role_usd et cout_reel.appels_par_role ;
- le rapport de l'épreuve réelle des témoins du juge, version 9
  (docs/notes/organisme-auto-conception-v1/course-v4/epreuve-temoins-reelle-auto-conception-v9.json),
  champ cout_usd seulement (33 appels : onze témoins, deux juges et l'aiguilleur) ;
  aucun verdict n'est lu ;
- les onze témoins du juge, version 2
  (docs/notes/organisme-auto-conception-v1/course-v2/temoins-juge-auto-conception-v2.json),
  pour leur longueur en caractères seulement.

Constante recopiée, non relue ici : la longueur moyenne des 94 cartes de la course v9
(4 994,16 caractères, contenu sérialisé sans le champ meta), mesurée par programme sur
fiches.json (sha256 ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481)
sans qu'aucune carte hors des sept nommées par le mandat soit affichée.

Usage (depuis la racine du dépôt) : python3 -I -B CE_FICHIER SORTIE.json
"""

import hashlib
import json
import sys

MANIFESTE = "runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json"
MANIFESTE_SHA = "28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7"
EPREUVE = "docs/notes/organisme-auto-conception-v1/course-v4/epreuve-temoins-reelle-auto-conception-v9.json"
EPREUVE_SHA = "e7837f4c40bca9aaed7ae0d3e8bdb51f9f36284ffb21c677575368699a61ca84"
TEMOINS = "docs/notes/organisme-auto-conception-v1/course-v2/temoins-juge-auto-conception-v2.json"
TEMOINS_SHA = "84a1e0ea870ecb54c2de8ec5071e689e2ba409b3c97aecb57ab16ef3388439e0"
LONGUEUR_MOYENNE_CARTES_V9 = 4994.16
APPELS_EPREUVE_TEMOINS = 33
PLAFOND_SESSION_JUGE_USD = 0.60  # préenregistrement de la course, « Seuil »

# Plan d'appels de l'étage payant, pour N témoins (moitié étalonnage, moitié lecture).
# A : chaque juge, chaque témoin, rendu canonique, un appel.
# B : répétitions à l'identique sur tous les témoins (juge Opus : 1 de plus ; juge Argon : 2 de plus).
# P : essai de plomberie, deux témoins de la version 2, deux juges.
# Option hors base, chiffrée à part — C : second rendu, à présentation permutée, sur la moitié
# lue, un appel par juge.
REPETITIONS_B = {"juge-opus": 1, "juge-argon": 2}
TEMOINS_PLOMBERIE = 2


def lire(chemin, empreinte):
    with open(chemin, "rb") as f:
        octets = f.read()
    vu = hashlib.sha256(octets).hexdigest()
    if vu != empreinte:
        raise SystemExit(f"empreinte inattendue pour {chemin} : {vu}")
    return json.loads(octets.decode("utf-8"))


def plan_appels(n, option_c=False):
    moitie = n // 2
    plan = {}
    for juge in ("juge-opus", "juge-argon"):
        plan[juge] = {"A": n, "B": n * REPETITIONS_B[juge], "P": TEMOINS_PLOMBERIE}
        if option_c:
            plan[juge]["C"] = moitie
        plan[juge]["total"] = sum(plan[juge].values())
    return plan


def cout(plan, par_appel, facteur):
    par_bras = {}
    par_juge = {}
    for juge, bras in plan.items():
        par_juge[juge] = 0.0
        for nom, appels in bras.items():
            if nom == "total":
                continue
            c = appels * par_appel[juge] * facteur
            par_bras[nom] = par_bras.get(nom, 0.0) + c
            par_juge[juge] += c
    return {"par_bras_usd": {k: round(v, 4) for k, v in sorted(par_bras.items())},
            "par_juge_usd": {k: round(v, 4) for k, v in par_juge.items()},
            "total_usd": round(sum(par_juge.values()), 4)}


def main(sortie):
    m = lire(MANIFESTE, MANIFESTE_SHA)
    e = lire(EPREUVE, EPREUVE_SHA)
    t = lire(TEMOINS, TEMOINS_SHA)
    usd = m["cout_reel"]["par_role_usd"]
    appels = m["cout_reel"]["appels_par_role"]
    par_appel = {r: usd[r] / appels[r] for r in ("juge-opus", "juge-argon", "aiguilleur")}
    devis_v1 = {r: m["ecart_au_devis_v1"]["par_role"][r]["devis_usd"] for r in ("juge-opus", "juge-argon")}
    depassement = {r: usd[r] / devis_v1[r] for r in devis_v1}

    # Rapport de coût « témoin / carte » : coût moyen par appel de l'épreuve des témoins v9
    # (aiguilleur et deux juges confondus : le rapport ne donne que le total) divisé par le
    # coût moyen par appel des trois mêmes rôles sur les cartes de la course.
    moyen_temoin = float(e["cout_usd"]) / APPELS_EPREUVE_TEMOINS
    moyen_carte = sum(par_appel.values()) / 3
    rapport = moyen_temoin / moyen_carte
    longueurs = [len(json.dumps(w["contenu"], ensure_ascii=False)) for w in t["temoins"]]
    longueur_moyenne_temoins = sum(longueurs) / len(longueurs)

    facteur_pire = max(depassement.values())
    juges = {r: par_appel[r] for r in ("juge-opus", "juge-argon")}
    scenarios = {}
    for n in (100, 150, 200, 300):
        plan = plan_appels(n)
        scenarios[str(n)] = {
            "plan_appels": plan,
            "appels_total": sum(p["total"] for p in plan.values()),
            "estimation": cout(plan, juges, rapport),
            "haut": cout(plan, juges, 1.0),
            "pire": cout(plan, juges, facteur_pire),
            "borne_de_plomberie_usd": round(sum(p["total"] for p in plan.values()) * PLAFOND_SESSION_JUGE_USD, 2),
        }
        avec_c = plan_appels(n, option_c=True)
        scenarios[str(n)]["avec_option_C"] = {
            "appels_total": sum(p["total"] for p in avec_c.values()),
            "estimation_usd": cout(avec_c, juges, rapport)["total_usd"],
            "haut_usd": cout(avec_c, juges, 1.0)["total_usd"],
            "pire_usd": cout(avec_c, juges, facteur_pire)["total_usd"],
        }
    base = scenarios["100"]
    bras_a_haut = base["haut"]["par_bras_usd"]["A"]
    plafond = 25.0
    resultat = {
        "version": "calcul-devis-ligne-3-v1",
        "entrees": {"manifeste": [MANIFESTE, MANIFESTE_SHA], "epreuve_temoins_v9": [EPREUVE, EPREUVE_SHA],
                    "temoins_v2": [TEMOINS, TEMOINS_SHA],
                    "longueur_moyenne_cartes_v9_caracteres": LONGUEUR_MOYENNE_CARTES_V9},
        "cout_reel_v9": {"par_role_usd": {r: usd[r] for r in par_appel}, "appels_par_role": {r: appels[r] for r in par_appel},
                         "par_appel_usd": {r: round(v, 6) for r, v in par_appel.items()},
                         "paire_de_juges_par_carte_usd": round(juges["juge-opus"] + juges["juge-argon"], 6),
                         "depassement_du_devis_v1_par_juge": {r: round(v, 4) for r, v in depassement.items()}},
        "temoins": {"cout_epreuve_v9_usd": e["cout_usd"], "appels": APPELS_EPREUVE_TEMOINS,
                    "cout_moyen_par_appel_temoin_usd": round(moyen_temoin, 6),
                    "cout_moyen_par_appel_carte_trois_roles_usd": round(moyen_carte, 6),
                    "rapport_temoin_sur_carte": round(rapport, 4),
                    "longueur_moyenne_temoins_v2_caracteres": round(longueur_moyenne_temoins, 1),
                    "longueur_min_max_temoins_v2": [min(longueurs), max(longueurs)],
                    "rapport_des_longueurs": round(longueur_moyenne_temoins / LONGUEUR_MOYENNE_CARTES_V9, 4)},
        "facteurs": {"estimation": round(rapport, 4), "haut": 1.0, "pire": round(facteur_pire, 4)},
        "repetitions_B": REPETITIONS_B,
        "appariement_du_juge_repete": {
            "cout_du_college_par_temoin_usd": round(juges["juge-opus"] + juges["juge-argon"], 6),
            "k_apparie": {r: int((juges["juge-opus"] + juges["juge-argon"]) // juges[r]) for r in juges},
            "k_joue": {r: 1 + REPETITIONS_B[r] for r in juges}},
        "scenarios_par_nombre_de_temoins": scenarios,
        "cout_marginal_par_dix_temoins_usd": {
            cas: round((scenarios["200"][cas]["total_usd"] - scenarios["100"][cas]["total_usd"]) / 10, 4)
            for cas in ("estimation", "haut", "pire")},
        "plafond_propose": {"usd": plafond,
                            "marge_sur_le_haut": round(plafond / base["haut"]["total_usd"], 4),
                            "facteur_de_depassement_que_le_bras_A_supporte": round(plafond / bras_a_haut, 4),
                            "temoins_au_plus_sous_le_plafond_au_cas_haut": max(
                                (n for n in range(100, 401, 2) if cout(plan_appels(n), juges, 1.0)["total_usd"] <= plafond),
                                default=None)},
    }
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage : python3 -I -B calcul_devis_ligne_3_v1.py SORTIE.json")
    main(sys.argv[1])
