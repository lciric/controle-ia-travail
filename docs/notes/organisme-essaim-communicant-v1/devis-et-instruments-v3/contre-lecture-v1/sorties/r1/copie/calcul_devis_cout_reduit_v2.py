#!/usr/bin/env python3
"""Devis à coût réduit de l'essaim — v2 (mot du directeur GO-2026-11-22-26 : « réduire drastiquement les coûts »).
Changements par rapport à `devis-et-instruments-v2/calcul_devis_cout_reduit_v1.py` (`6c786ba9…`), réserves R1, R5 et trouvaille
de côté de la vérification de la v2 :
- R1 : importe `calcul_devis_essaim_v3` et `calcul_pilote_essaim_v2` (chemins relatifs à la racine du dépôt) ;
- R5 : la division par 5 de la mise en route du modèle ouvert au pilote (l. 146 de la v1, sans déclaration) est RETIRÉE : le
  pilote compte la mise en route entière de l'HYPOTHÈSE (10 h à l'estimation, 30 au pire), déclarée dans `hypotheses` ;
- R5 : les facteurs de chaque levier (min et max sur les quatre espèces) sont calculés et rendus (`facteurs_par_levier`) ;
  le texte n'en cite plus d'autres ;
- les messages du pilote sur modèle ouvert sont comptés à leur sortie (400 à l'estimation, 2 000 au pire), non à celle des
  proposeurs (trouvaille de côté) ; l'estimation sur modèle ouvert est rendue aux deux sorties (6 000 et 12 800) ;
- le pilote par l'interface rend le vrai pire sous les gardes du lanceur (`garde_pilote_essaim_v1`).
Chaque levier chiffré seul puis en combinaison, sur le programme (cas attendu de la v2) et sur le pilote P-std. Aucun
appel, aucun réseau, aucune dépense. Tout nombre sans pièce est marqué HYPOTHÈSE dans la sortie.
Usage : python3 -I -B calcul_devis_cout_reduit_v2.py SORTIE.json   (refuse d'écraser)"""
import hashlib
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import calcul_devis_essaim_v3 as C  # noqa: E402
import calcul_pilote_essaim_v2 as P  # noqa: E402
import garde_pilote_essaim_v1 as GP  # noqa: E402

# ---- HYPOTHÈSES (aucune pièce du dépôt lue ne les donne) ----------------------------------------------------------------
GPU_USD_H = 1.4                                    # A100 louée, chiffre donné par la commande (« environ 1,4 USD/h »)
GPU = {"estimation": {"sortie_jetons_s": 400, "entree_jetons_s": 4000, "utilisation": 0.5, "mise_en_route_h": 10},
       "pire": {"sortie_jetons_s": 100, "entree_jetons_s": 1000, "utilisation": 0.25, "mise_en_route_h": 30}}
# débit agrégé d'un modèle ouvert de taille moyenne servi par vLLM sur une A100, plusieurs requêtes en parallèle : HYPOTHÈSE ;
# utilisation : part du temps loué où la carte sert (générations séquentielles, attente du noyau) : HYPOTHÈSE ;
# mise en route : chargement des poids et essais, une session par vague de génération : HYPOTHÈSE.
REMISE_LOTS = 0.5        # « remise rapportée, non vérifiée » : aucune pièce de tarifs n'en porte la valeur
PART_CACHEE = 2 / 3      # HYPOTHÈSE : consigne et case de matière communes aux appels d'un monde
TAUX_ECHANTILLON = 0.2   # PROPOSITION : part des tests de mort et des objets de contrôle tirée au hasard
SORTIE_COURTE = 0.5      # HYPOTHÈSE : facteur sur la sortie d'une consigne « sans raisonnement affiché, deux cartes »
CAP_COURT = 8000         # PROPOSITION de plafond de sortie court (contre 24 000 au pilote)


def cache_fable():
    txt, sha = C.lire("fable_module")
    lec = float(re.search(r"^PRIX_LECTURE_CACHE_USD_PAR_MJ = ([0-9.]+)", txt, re.M).group(1))
    ecr = float(re.search(r"^FACTEUR_ECRITURE_CACHE = ([0-9.]+)", txt, re.M).group(1))
    return lec, ecr, {"piece": C.PIECES["fable_module"][0], "sha256": sha, "lignes": [C.ligne_de(txt, "PRIX_LECTURE_CACHE_USD_PAR_MJ = "), C.ligne_de(txt, "FACTEUR_ECRITURE_CACHE = ")]}


def jetons_programme(N, taux, regime="attendu"):
    """Jetons par rôle du programme (section D et v2), cas donné : {rôle: (entrée, sortie, frais fixes USD)}."""
    tot = {"proposeurs": [0, 0, 0.0], "messages": [0, 0, 0.0], "aiguilleur": [0, 0, 0.0], "tests": [0, 0, 0.0]}
    pe, ps = C.JETONS_PROPOSEUR[regime]
    pl_pire, pl_central, fausses = N["PLANTEES"][0]
    te, ts = N["TOUR_CENTRAL"][0]
    v_c = N["VERIF"][0][0]
    for l in C.COURSES:
        n_c, n_a = C.COURSES[l][regime]
        n_p = n_c * C.PROPOSEUR_PAR_COURSE
        cartes = n_p * C.CARTES_PAR_APPEL
        jeux = n_c * C.LIGNEES_PAR_COURSE * C.GENERATIONS
        tot["proposeurs"][0] += n_p * pe + n_a * C.APPELS_A_PAR_COURSE * C.SURCROIT_ENTREE_A
        tot["proposeurs"][1] += n_p * ps
        tot["messages"][0] += n_a * C.MESSAGES_PAR_COURSE_A * C.JETONS_MESSAGE[0]
        tot["messages"][1] += n_a * C.MESSAGES_PAR_COURSE_A * C.JETONS_MESSAGE[1]
        n_aig = cartes + jeux * (pl_pire + fausses)
        tot["aiguilleur"][0] += n_aig * C.JETONS_AIGUILLEUR[0]
        tot["aiguilleur"][1] += n_aig * C.JETONS_AIGUILLEUR[1]
        n_t = cartes * taux + jeux * pl_central
        tot["tests"][0] += n_t * 2 * te
        tot["tests"][1] += n_t * 2 * ts
        tot["tests"][2] += n_t * v_c
    return {k: tuple(v) for k, v in tot.items()}


def usd_api(j, prix, remise=0.0, cache=None):
    e, s, fixe = j
    if cache:
        lec, ecr = cache
        e_usd = e * ((1 - PART_CACHEE) * prix[0] + PART_CACHEE * lec)
    else:
        e_usd = e * prix[0]
    return (e_usd + s * prix[1]) / 1e6 * (1 - remise) + fixe


def heures_gpu(jet, mode):
    g = GPU[mode]
    h = sum(e / g["entree_jetons_s"] + s / g["sortie_jetons_s"] for e, s, _ in jet) / 3600 / g["utilisation"]
    return h + g["mise_en_route_h"]


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        return 2
    txt, _ = C.lire("devis_multi_v2")
    N = C.nombres_tests(txt)
    C.comparer(N, ("BORNE_TEST", "VERIF", "PLANTEES", "PRIX_MULTI", "TOUR_CENTRAL", "TOUR_PIRE"))
    js, _ = C.lire("devis_v4_sortie")
    reps = json.loads(js)["central_v4"]["representants_promus_simules"]
    props, cartes = C.nombres_simulation_v4(C.lire("monde_riche_v4")[0])["SIMULATION_V4"][0]
    taux = sum(reps) / (props * cartes * len(reps))
    marge = C.nombres_affinage(C.lire("devis_affinage_v5")[0])["MARGE_AFFINAGE"][0]
    prix, _ = C.tarifs()
    lec, ecr, src_cache = cache_fable()
    J = jetons_programme(N, taux)
    prog = {}
    for esp in ("kimi", "claude-1", "fable-5-2", "claude-2"):
        p = prix[esp]
        base = sum(usd_api(j, p) for j in J.values()) * (1 + marge)
        r = {"reference_v2_estimation": round(base, 2)}
        # (a) proposeurs et messages sur modèle ouvert ; tests et aiguilleur sur l'interface, ou tout sur le modèle ouvert
        for mode in ("estimation", "pire"):
            h1 = heures_gpu([J["proposeurs"], J["messages"]], mode)
            reste = usd_api(J["aiguilleur"], p) + usd_api(J["tests"], p)
            h2 = heures_gpu([J["proposeurs"], J["messages"], J["aiguilleur"], J["tests"]], mode)
            r[f"a_ouvert_proposeurs_{mode}"] = {"heures_gpu": round(h1, 1), "usd": round((h1 * GPU_USD_H + reste) * (1 + marge), 2)}
            r[f"a_ouvert_tout_{mode}"] = {"heures_gpu": round(h2, 1), "usd": round((h2 * GPU_USD_H + J["tests"][2]) * (1 + marge), 2)}
        r["b_lots_remise_non_verifiee"] = round(sum(usd_api(j, p, REMISE_LOTS) for j in J.values()) * (1 + marge), 2)
        r["b_cache"] = round(sum(usd_api(j, p, 0, (lec, ecr) if esp == "fable-5-2" else None) for j in J.values()) * (1 + marge), 2) \
            if esp == "fable-5-2" else "tarif de cache non établi pour cette espèce"
        t_ech = (J["tests"][0] * TAUX_ECHANTILLON, J["tests"][1] * TAUX_ECHANTILLON, J["tests"][2] * TAUX_ECHANTILLON)
        r["c_tests_echantillonnes"] = round((usd_api(J["proposeurs"], p) + usd_api(J["messages"], p) + usd_api(J["aiguilleur"], p) + usd_api(t_ech, p)) * (1 + marge), 2)
        jc = {k: (v[0], v[1] * (SORTIE_COURTE if k in ("proposeurs",) else 1), v[2]) for k, v in J.items()}
        r["e_sorties_courtes"] = round(sum(usd_api(j, p) for j in jc.values()) * (1 + marge), 2)
        combo_api = (usd_api(jc["proposeurs"], p, REMISE_LOTS) + usd_api(jc["messages"], p, REMISE_LOTS) + usd_api(jc["aiguilleur"], p, REMISE_LOTS)
                     + usd_api(t_ech, p, REMISE_LOTS)) * (1 + marge)
        r["combinaison_b_c_e"] = {"avec_remise": round(combo_api, 2),
                                  "sans_remise": round((usd_api(jc["proposeurs"], p) + usd_api(jc["messages"], p) + usd_api(jc["aiguilleur"], p) + usd_api(t_ech, p)) * (1 + marge), 2)}
        for k, v in list(r.items()):
            if isinstance(v, (int, float)) and k != "reference_v2_estimation":
                r[k + "_facteur"] = round(base / v, 1)
        prog[esp] = r
    # pilote P-std ((a) et (c), 12 mondes, 3 générations ; aucun test de mort, aucun aiguilleur)
    c8 = C.nombres_conception(C.lire("conception")[0])["PLAFOND_C8"][0]
    pil = {}
    v = P.VARIANTES["P-std"]
    for esp in ("kimi", "claude-1", "fable-5-2", "claude-2"):
        p = prix[esp]
        e6, pire = P.cout_pilote_v1(v, p, P.SORTIE_EST["conception"], marge, c8)
        e12, _ = P.cout_pilote_v1(v, p, P.SORTIE_EST["mesure_v67_kimi"], marge, c8)
        sauve = P.MAX_SORTIE_PROPOSEUR
        P.MAX_SORTIE_PROPOSEUR = CAP_COURT
        _, pire_court = P.cout_pilote_v1(v, p, P.SORTIE_EST["conception"], marge, c8)
        P.MAX_SORTIE_PROPOSEUR = sauve
        plan = P.plan_variante(v)
        sauve_g = dict(GP.PLAFOND_SORTIE)
        GP.PLAFOND_SORTIE["proposeur"] = CAP_COURT
        pire_court_gardes = GP.borne_pire(plan, p)["pire_usd"]
        GP.PLAFOND_SORTIE.update(sauve_g)
        pil[esp] = {"estimation_6000": e6, "estimation_12800": e12, "pire_v1_cap_24000": pire, "pire_v1_cap_8000": pire_court,
                    "vrai_pire_sous_gardes_cap_24000": round(GP.borne_pire(plan, p)["pire_usd"], 2),
                    "vrai_pire_sous_gardes_cap_8000": round(pire_court_gardes, 2),
                    "lots_remise_non_verifiee_estimation_12800": round(e12 * (1 - REMISE_LOTS), 2), "appels": len(plan)}
    # pilote sur modèle ouvert : jetons du pilote
    g = v["generations"] / 3
    ent_est = ent_max = 0.0
    sort = {"estimation_6000": 0.0, "estimation_12800": 0.0, "pire": 0.0}
    for b in v["bras"]:
        n_p = P.APPELS[b]["proposeur"] * g * v["mondes"]
        n_m = P.APPELS[b]["message"] * g * v["mondes"]
        ent_est += n_p * (P.ENTREE + P.SURCROIT_A) + n_m * P.MESSAGE[0]
        ent_max += n_p * GP.PLAFOND_ENTREE_JETONS["proposeur"] + n_m * GP.PLAFOND_ENTREE_JETONS["message"]
        sort["estimation_6000"] += n_p * P.SORTIE_EST["conception"] + n_m * P.MESSAGE[1]
        sort["estimation_12800"] += n_p * P.SORTIE_EST["mesure_v67_kimi"] + n_m * P.MESSAGE[1]
        sort["pire"] += n_p * GP.PLAFOND_SORTIE["proposeur"] + n_m * GP.PLAFOND_SORTIE["message"]
    pil_gpu = {}
    for cle, mode, e, s in (("estimation_6000", "estimation", ent_est, sort["estimation_6000"]),
                            ("estimation_12800", "estimation", ent_est, sort["estimation_12800"]),
                            ("pire", "pire", ent_max, sort["pire"])):
        gg = GPU[mode]
        h_calcul = (e / gg["entree_jetons_s"] + s / gg["sortie_jetons_s"]) / 3600 / gg["utilisation"]
        h = h_calcul + gg["mise_en_route_h"]  # R5 : mise en route entière (la division par 5 de la v1 est retirée)
        pil_gpu[cle] = {"heures_gpu": round(h, 1), "dont_mise_en_route_h": gg["mise_en_route_h"], "heures_de_calcul": round(h_calcul, 2),
                        "usd": round(h * GPU_USD_H * (1 + marge) * (c8 if mode == "pire" else 1), 2)}
    facteurs = {}
    for lev in ("a_ouvert_proposeurs_estimation", "a_ouvert_tout_estimation", "b_lots_remise_non_verifiee", "b_cache", "c_tests_echantillonnes",
                "e_sorties_courtes"):
        fs = []
        for esp, r in prog.items():
            v_ = r[lev]
            v_ = v_["usd"] if isinstance(v_, dict) else v_
            if isinstance(v_, (int, float)):
                fs.append(round(r["reference_v2_estimation"] / v_, 2))
        facteurs[lev] = {"min": min(fs), "max": max(fs), "especes": len(fs)}
    for lev, k2 in (("combinaison_b_c_e_avec_remise", "avec_remise"), ("combinaison_b_c_e_sans_remise", "sans_remise")):
        fs = [round(r["reference_v2_estimation"] / r["combinaison_b_c_e"][k2], 2) for r in prog.values()]
        facteurs[lev] = {"min": min(fs), "max": max(fs), "especes": len(fs)}
    fs = [round(prog[e]["reference_v2_estimation"] / pil[e][k2], 2) for e in pil for k2 in ("estimation_6000", "estimation_12800")]
    facteurs["d_pilote_d_abord_meme_espece"] = {"min": min(fs), "max": max(fs), "especes": len(pil)}
    ech = {f"q={q}|m={m}": round(1 - (1 - q) ** m, 3) for q in (0.05, 0.1, 0.2) for m in (3, 6, 12, 36)}
    out = {"version": "calcul-devis-cout-reduit-v2", "facteurs_par_levier": facteurs, "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           "hypotheses": {"mise_en_route_au_pilote": "entière (10 h à l'estimation, 30 au pire) : la division par 5 de la v1 est retirée, faute de justification",
                          "GPU_USD_H": GPU_USD_H, "GPU": GPU, "REMISE_LOTS": REMISE_LOTS, "PART_CACHEE": PART_CACHEE, "TAUX_ECHANTILLON": TAUX_ECHANTILLON,
                          "SORTIE_COURTE": SORTIE_COURTE, "CAP_COURT": CAP_COURT, "statut": "HYPOTHÈSES ou PROPOSITIONS, aucune pièce du dépôt lue"},
           "cache_fable": {"lecture_usd_par_mj": lec, "facteur_ecriture": ecr, **src_cache},
           "jetons_programme_attendu": {k: {"entree": round(v2[0]), "sortie": round(v2[1]), "fixe_usd": round(v2[2], 2)} for k, v2 in J.items()},
           "programme_attendu": prog, "pilote_P_std_api": pil, "pilote_P_std_modele_ouvert": pil_gpu,
           "probabilite_de_voir_un_defaut_q_avec_m_tests_echantillonnes": ech}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({k: out[k] for k in ("facteurs_par_levier", "jetons_programme_attendu", "programme_attendu", "pilote_P_std_api", "pilote_P_std_modele_ouvert", "probabilite_de_voir_un_defaut_q_avec_m_tests_echantillonnes")}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
