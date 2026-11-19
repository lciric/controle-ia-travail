"""Calcul du devis de l'étage payant de la ligne 3 (votes effectifs des juges croisés) — v3.

Processeur seul, aucun appel de modèle, aucune dépense. Pièce de travail, version 3,
à vérifier. Remplace calcul_devis_ligne_3_v2.py (gardé, non modifié).

Ce qui change par rapport à la version 2 (consigne de la mère R-3875, trois conditions du
plafond) : AUCUN montant, aucun nombre d'appels, aucune clé de la sortie de la version 2
ne change de valeur, sauf « version ». Deux clés sont AJOUTÉES à la sortie :
- « compteur_d_arret » : le compteur compte au pire (le plafond de session d'un appel)
  tout envoi refusé ou sans coût lisible ; nombre d'envois qui partent si tous sont
  refusés ; nombre d'envois refusés que la base supporte sans être coupée, par cas ;
  nombre de témoins complets au bloc B, au pire cas et au cas haut, selon le nombre
  d'envois refusés ;
- « essais_courts_d_autres_lignees_borne_dure » : onze appels au plafond de session.

Rappel de ce que la version 2 changeait par rapport à la version 1 :

(contre-lecture de la version 1, constats 13 et 14)
- la constante « longueur moyenne des 94 cartes » est RETIRÉE : elle n'entrait dans aucun
  coût et son programme de mesure n'était pas versé (règle R6). Ce programme n'ouvre plus
  aucune carte et ne dépend plus du fichier des cartes ;
- le plafond est lu avec la réserve du plafond de session (aucun appel ne part si le cumul
  plus le plafond de session dépasse le plafond d'arrêt) : facteur que le bloc A supporte,
  nombre maximal de témoins, marge effective sur le cas haut ;
- le bloc B est entrelacé par témoin (juge Opus une fois, juge Argon deux fois) : le
  programme rend le facteur de coût jusqu'où 40 puis 50 puis 100 témoins restent complets ;
- hors base, un ORDRE DE GRANDEUR (pas un devis) du coût d'autres lignées servies comme
  juges, tiré des coûts de proposeur de la course v9 et du rapport « coût d'un appel de
  juge / coût d'un appel de proposeur » mesuré sur les deux lignées qui ont les deux rôles.

Entrées, lues par ce programme et vérifiées par empreinte (arrêt si une empreinte
diffère) :
- le manifeste de fin du lanceur de la course d'auto-conception v9
  (runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json),
  champs cout_reel.par_role_usd, cout_reel.appels_par_role et
  ecart_au_devis_v1.par_role ;
- le rapport de l'épreuve réelle des témoins du juge, version 9
  (docs/notes/organisme-auto-conception-v1/course-v4/epreuve-temoins-reelle-auto-conception-v9.json),
  champ cout_usd seulement (33 appels : onze témoins, deux juges et l'aiguilleur) ;
  aucun verdict n'est lu ;
- les onze témoins du juge, version 2
  (docs/notes/organisme-auto-conception-v1/course-v2/temoins-juge-auto-conception-v2.json),
  pour leur longueur en caractères seulement.

Usage (depuis la racine du dépôt) : python3 -I -B CE_FICHIER SORTIE.json
"""

ENVOIS_REFUSES_TABULES = (0, 1, 2, 3, 5, 10)

import hashlib
import json
import sys

MANIFESTE = "runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json"
MANIFESTE_SHA = "28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7"
EPREUVE = "docs/notes/organisme-auto-conception-v1/course-v4/epreuve-temoins-reelle-auto-conception-v9.json"
EPREUVE_SHA = "e7837f4c40bca9aaed7ae0d3e8bdb51f9f36284ffb21c677575368699a61ca84"
TEMOINS = "docs/notes/organisme-auto-conception-v1/course-v2/temoins-juge-auto-conception-v2.json"
TEMOINS_SHA = "84a1e0ea870ecb54c2de8ec5071e689e2ba409b3c97aecb57ab16ef3388439e0"
APPELS_EPREUVE_TEMOINS = 33
PLAFOND_SESSION_JUGE_USD = 0.60  # préenregistrement de la course, « Seuil »
PLAFOND_ARRET_USD = 25.0  # GO-2026-11-19-66, accord conditionnel

# Plan d'appels de l'étage payant, pour N témoins (moitié étalonnage, moitié lecture).
# P : essai de plomberie, deux témoins de la version 2, deux juges.
# A : chaque juge, chaque témoin, un appel.
# B : répétitions à l'identique sur tous les témoins, entrelacées par témoin
#     (juge Opus : 1 de plus ; juge Argon : 2 de plus), moitié « lecture » d'abord.
# Option hors base — C : second rendu, à présentation permutée, sur la moitié lue,
# un appel par juge.
JUGES = ("juge-opus", "juge-argon")
REPETITIONS_B = {"juge-opus": 1, "juge-argon": 2}
TEMOINS_PLOMBERIE = 2

# Autres lignées, hors base : rôles de proposeur de la course v9 dont la lignée n'a pas de
# coût de juge mesuré, et rôles des deux lignées qui ont les deux coûts.
PROPOSEURS_SANS_COUT_DE_JUGE = ("prop-astra", "prop-carbon", "prop-fable")
PAIRES_JUGE_PROPOSEUR = {"juge-opus": "prop-opus", "juge-argon": "prop-argon"}
TEMOINS_ESSAI_AUTRE_LIGNEE = 11  # les onze témoins de la version 2, un appel chacun


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
    for juge in JUGES:
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
    roles = sorted(usd)
    par_appel = {r: usd[r] / appels[r] for r in roles}
    devis_v1 = {r: m["ecart_au_devis_v1"]["par_role"][r]["devis_usd"] for r in roles}
    reel_sur_devis = {r: usd[r] / devis_v1[r] for r in roles}

    # Rapport de coût « témoin / carte » : coût moyen par appel de l'épreuve des témoins v9
    # (aiguilleur et deux juges confondus : le rapport ne donne que le total) divisé par le
    # coût moyen par appel des trois mêmes rôles sur les cartes de la course.
    moyen_temoin = float(e["cout_usd"]) / APPELS_EPREUVE_TEMOINS
    moyen_carte = sum(par_appel[r] for r in ("juge-opus", "juge-argon", "aiguilleur")) / 3
    rapport = moyen_temoin / moyen_carte
    longueurs = [len(json.dumps(w["contenu"], ensure_ascii=False)) for w in t["temoins"]]

    facteur_pire = max(reel_sur_devis[r] for r in JUGES)
    juges = {r: par_appel[r] for r in JUGES}
    college = sum(juges.values())
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

    # Plafond, avec la réserve du plafond de session (règle d'arrêt : aucun appel ne part si
    # cumul + plafond de session > plafond d'arrêt).
    disponible = PLAFOND_ARRET_USD - PLAFOND_SESSION_JUGE_USD
    p_haut = base["haut"]["par_bras_usd"]["P"]
    a_haut = base["haut"]["par_bras_usd"]["A"]
    b_par_temoin_haut = sum(juges[r] * REPETITIONS_B[r] for r in JUGES)

    def facteur_pour_b_complets(k):
        return disponible / (p_haut + a_haut + k * b_par_temoin_haut)

    def temoins_b_complets(facteur):
        reste = disponible - facteur * (p_haut + a_haut)
        if reste < 0:
            return 0
        return min(100, int(reste // (facteur * b_par_temoin_haut)))

    def temoins_max(reserve):
        borne = PLAFOND_ARRET_USD - (PLAFOND_SESSION_JUGE_USD if reserve else 0.0)
        return max((n for n in range(100, 401, 2) if cout(plan_appels(n), juges, 1.0)["total_usd"] <= borne),
                   default=None)

    plafond = {
        "usd": PLAFOND_ARRET_USD,
        "ligne_de_go": "GO-2026-11-19-66",
        "reserve_plafond_de_session_usd": PLAFOND_SESSION_JUGE_USD,
        "disponible_avant_le_dernier_appel_usd": round(disponible, 4),
        "haut_depasse_le_plafond": base["haut"]["total_usd"] > PLAFOND_ARRET_USD,
        "haut_plus_reserve_depasse_le_plafond": base["haut"]["total_usd"] + PLAFOND_SESSION_JUGE_USD > PLAFOND_ARRET_USD,
        "pire_depasse_le_plafond": base["pire"]["total_usd"] > PLAFOND_ARRET_USD,
        "marge_nominale_sur_le_haut": round(PLAFOND_ARRET_USD / base["haut"]["total_usd"], 4),
        "marge_effective_sur_le_haut": round(disponible / base["haut"]["total_usd"], 4),
        "facteur_que_le_bloc_A_supporte_apres_plomberie": round(disponible / (p_haut + a_haut), 4),
        "facteur_jusqu_ou_B_est_complet_sur_k_temoins": {
            str(k): round(facteur_pour_b_complets(k), 4) for k in (40, 50, 100)},
        "temoins_B_complets_selon_le_facteur": {
            "estimation": temoins_b_complets(rapport), "haut": temoins_b_complets(1.0),
            "pire": temoins_b_complets(facteur_pire)},
        "temoins_au_plus_au_cas_haut": {"avec_reserve": temoins_max(True), "sans_reserve": temoins_max(False)},
        "base_reduite_plomberie_et_bloc_A": {
            "appels": sum(base["plan_appels"][r]["A"] + base["plan_appels"][r]["P"] for r in JUGES),
            "estimation_usd": round(rapport * (p_haut + a_haut), 4), "haut_usd": round(p_haut + a_haut, 4),
            "pire_usd": round(facteur_pire * (p_haut + a_haut), 4)},
        "plomberie_bloc_A_et_B_sur_40_temoins_au_pire_usd": round(
            facteur_pire * (p_haut + a_haut + 40 * b_par_temoin_haut), 4),
    }

    # Autres lignées comme juges : ORDRE DE GRANDEUR, pas un devis. Aucun coût de juge n'est
    # mesuré pour elles. Hypothèse dite : le coût d'un appel de juge d'une lignée est au coût
    # de son appel de proposeur ce qu'il est pour les deux lignées qui ont les deux rôles ;
    # fourchette = [plus petit rapport ; plus grand rapport] ; borne « large » = plus grand
    # rapport x facteur du pire cas.
    rapports_jp = {j: par_appel[j] / par_appel[p] for j, p in PAIRES_JUGE_PROPOSEUR.items()}
    r_bas, r_haut = min(rapports_jp.values()), max(rapports_jp.values())
    autres = {}
    for prop in PROPOSEURS_SANS_COUT_DE_JUGE:
        bas, haut = par_appel[prop] * r_bas, par_appel[prop] * r_haut
        large = haut * facteur_pire

        def fourchette(n_appels, bas=bas, haut=haut, large=large):
            return {"appels": n_appels, "bas_usd": round(n_appels * bas, 2), "haut_usd": round(n_appels * haut, 2),
                    "large_usd": round(n_appels * large, 2)}

        autres[prop] = {
            "cout_reel_par_appel_de_proposeur_usd": round(par_appel[prop], 6),
            "reel_sur_devis_du_proposeur": round(reel_sur_devis[prop], 4),
            "ordre_de_grandeur_par_appel_de_juge_usd": {"bas": round(bas, 4), "haut": round(haut, 4), "large": round(large, 4)},
            "appel_large_sous_le_plafond_de_session": large <= PLAFOND_SESSION_JUGE_USD,
            "essai_d_abord_onze_temoins_v2": fourchette(TEMOINS_ESSAI_AUTRE_LIGNEE),
            "bloc_A_seul_100_temoins": fourchette(100),
            "bloc_A_et_une_repetition_100_temoins": fourchette(200),
        }

    def somme(cle, champ):
        return round(sum(autres[p][cle][champ] for p in PROPOSEURS_SANS_COUT_DE_JUGE), 2)

    autres_lignees = {
        "nature": "ordre de grandeur, pas un devis ; aucune ligne de GO ne peut s'appuyer dessus",
        "rapport_cout_juge_sur_cout_proposeur_par_appel": {j: round(v, 4) for j, v in rapports_jp.items()},
        "lignee_deja_mesuree_comme_juge": {
            "juge-argon": {"par_appel_usd": round(par_appel["juge-argon"], 6)},
            "juge-opus": {"par_appel_usd": round(par_appel["juge-opus"], 6)}},
        "par_role_de_proposeur": autres,
        "les_trois_ensemble": {
            cle: {"appels": sum(autres[p][cle]["appels"] for p in PROPOSEURS_SANS_COUT_DE_JUGE),
                  "bas_usd": somme(cle, "bas_usd"), "haut_usd": somme(cle, "haut_usd"), "large_usd": somme(cle, "large_usd")}
            for cle in ("essai_d_abord_onze_temoins_v2", "bloc_A_seul_100_temoins", "bloc_A_et_une_repetition_100_temoins")},
    }

    # Compteur d'arrêt (consigne R-3875). Règle : aucun envoi ne part si le cumul compté plus
    # le plafond de session dépasse le plafond d'arrêt ; un envoi refusé ou sans coût lisible
    # est compté au plafond de session (le pire qu'un appel puisse coûter). Calcul en
    # centièmes de dollar pour le cas « tous refusés », sans arrondi flottant.
    plafond_c = int(round(PLAFOND_ARRET_USD * 100))
    session_c = int(round(PLAFOND_SESSION_JUGE_USD * 100))
    envois_si_tous_refuses = 0
    while envois_si_tous_refuses * session_c + session_c <= plafond_c:
        envois_si_tous_refuses += 1

    def refuses_supportes(total):
        marge = disponible - total
        return 0 if marge < 0 else int(marge // PLAFOND_SESSION_JUGE_USD)

    def temoins_b_complets_avec_refus(facteur, refus):
        reste = disponible - refus * PLAFOND_SESSION_JUGE_USD - facteur * (p_haut + a_haut)
        if reste < 0:
            return 0
        return min(100, int(reste // (facteur * b_par_temoin_haut)))

    compteur = {
        "regle": "aucun envoi ne part si cumul compté + plafond de session > plafond d'arrêt",
        "cout_compte_d_un_envoi_refuse_ou_sans_cout_lisible_usd": PLAFOND_SESSION_JUGE_USD,
        "envois_qui_partent_si_tous_sont_refuses": envois_si_tous_refuses,
        "cumul_compte_a_l_arret_si_tous_sont_refuses_usd": round(envois_si_tous_refuses * session_c / 100, 2),
        "envois_refuses_que_la_base_supporte_sans_coupure": {
            cas: refuses_supportes(base[cas]["total_usd"]) for cas in ("estimation", "haut", "pire")},
        "temoins_B_complets_au_pire_cas_selon_les_envois_refuses": {
            str(r): temoins_b_complets_avec_refus(facteur_pire, r) for r in ENVOIS_REFUSES_TABULES},
        "temoins_B_complets_au_cas_haut_selon_les_envois_refuses": {
            str(r): temoins_b_complets_avec_refus(1.0, r) for r in ENVOIS_REFUSES_TABULES},
        "cumul_au_pire_cas_plomberie_bloc_A_et_18_temoins_du_bloc_B_usd": round(
            facteur_pire * (p_haut + a_haut + 18 * b_par_temoin_haut), 4),
    }
    essais_borne_dure = {
        "appels_par_lignee": TEMOINS_ESSAI_AUTRE_LIGNEE,
        "par_lignee_usd": round(TEMOINS_ESSAI_AUTRE_LIGNEE * PLAFOND_SESSION_JUGE_USD, 2),
        "trois_lignees_usd": round(3 * TEMOINS_ESSAI_AUTRE_LIGNEE * PLAFOND_SESSION_JUGE_USD, 2),
        "nature": "onze appels au plafond de session d'un appel de juge : borne dure d'un essai court, si le service tient ce plafond ; pas un devis",
    }

    resultat = {
        "version": "calcul-devis-ligne-3-v3",
        "compteur_d_arret": compteur,
        "essais_courts_d_autres_lignees_borne_dure": essais_borne_dure,
        "entrees": {"manifeste": [MANIFESTE, MANIFESTE_SHA], "epreuve_temoins_v9": [EPREUVE, EPREUVE_SHA],
                    "temoins_v2": [TEMOINS, TEMOINS_SHA]},
        "constante_retiree": "longueur moyenne des cartes de la course v9 (version 1) : retirée, n'entrait dans aucun coût",
        "cout_reel_v9": {"par_role_usd": {r: usd[r] for r in roles}, "appels_par_role": {r: appels[r] for r in roles},
                         "par_appel_usd": {r: round(par_appel[r], 6) for r in roles},
                         "paire_de_juges_par_carte_usd": round(college, 6),
                         "reel_sur_devis_v1_par_role": {r: round(reel_sur_devis[r], 4) for r in roles}},
        "temoins": {"cout_epreuve_v9_usd": e["cout_usd"], "appels": APPELS_EPREUVE_TEMOINS,
                    "cout_moyen_par_appel_temoin_usd": round(moyen_temoin, 6),
                    "cout_moyen_par_appel_carte_trois_roles_usd": round(moyen_carte, 6),
                    "rapport_temoin_sur_carte": round(rapport, 4),
                    "longueur_moyenne_temoins_v2_caracteres": round(sum(longueurs) / len(longueurs), 1),
                    "longueur_min_max_temoins_v2": [min(longueurs), max(longueurs)]},
        "facteurs": {"estimation": round(rapport, 4), "haut": 1.0, "pire": round(facteur_pire, 4),
                     "nature_du_pire": "rapport réel/devis du juge Opus à la course v9, appliqué à un coût déjà réel : marge de prudence, pas un dépassement observé sur cette base"},
        "repetitions_B": REPETITIONS_B,
        "cout_du_bloc_B_par_temoin_au_cas_haut_usd": round(b_par_temoin_haut, 6),
        "appariement_du_juge_repete": {
            "cout_du_college_par_temoin_usd": round(college, 6),
            "k_apparie": {r: int(college // juges[r]) for r in JUGES},
            "k_joue": {r: 1 + REPETITIONS_B[r] for r in JUGES},
            "cout_par_temoin_au_k_apparie_usd": {r: round(int(college // juges[r]) * juges[r], 6) for r in JUGES}},
        "scenarios_par_nombre_de_temoins": scenarios,
        "cout_marginal_par_dix_temoins_usd": {
            cas: round((scenarios["200"][cas]["total_usd"] - scenarios["100"][cas]["total_usd"]) / 10, 4)
            for cas in ("estimation", "haut", "pire")},
        "plafond": plafond,
        "autres_lignees_comme_juges_hors_base": autres_lignees,
    }
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage : python3 -I -B calcul_devis_ligne_3_v3.py SORTIE.json")
    main(sys.argv[1])
