"""Intégration du plan B des juges (T0.5) : le lanceur `requalifier_juges` et le lecteur `lire_requalification` ont les
mêmes noms de fichiers, les mêmes clés et les mêmes constantes ; le lecteur lit les fichiers d'un vrai run jouet du
lanceur, et ses lectures égalent celles du second calcul du lanceur (ses fonctions de bilan pures) sur ces fichiers.

Le run jouet est celui de `test_plan_b_requalifier` (fait une fois par processus, puis copié). Ses couches, seuils et
effectifs sont ceux du jouet : les constantes du lecteur prennent les siens le temps du test, et les effectifs minimaux
passent à 1 des deux côtés pour que les tables se lisent jusqu'au bout. L'égalité des deux calculs ne dépend pas des
écarts numériques du jouet ; les lectures attendues du run jouet (chemin « fidèle », D1 « vu », D-10) en dépendent :
`test_le_lecteur_lit_le_run_jouet_du_lanceur` est SENSIBLE AU MATÉRIEL (docstring)."""
from __future__ import annotations

import json
import math

import pytest

from controle_ia.environnements import juges_simplifies as js
from controle_ia.environnements import lire_requalification as lr
from controle_ia.environnements import requalifier_juges as rq
from controle_ia.environnements import rubrique_simplifiee as rs
from controle_ia.environnements.pilote_a import CLES_RAPPORT_GARDEES
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import generateur, graines
from test_plan_b_lecteur import _rapport
from test_plan_b_requalifier import (_config, _config_reelle, _h4_courte_et_entropie, _run_complet,  # noqa: F401
                                     _scellees, depot_planb)


def test_constantes_communes_au_lanceur_et_au_lecteur():
    """Modules gelés et commit, réglages relus, unité de couverture, séparateurs de la lecture RS1, clé de l'unique
    comparaison ; la configuration réelle du texte passe la garde du lanceur et égale les seuils gelés du lecteur (cas
    sain) ; un seuil que le lanceur accepte mais que le lecteur ne partage pas arrête la lecture (artefacts)."""
    assert lr.MODULES_GELES == rq.MODULES_GELES and lr.COMMIT_GELES == rq.COMMIT_MODULES_GELES
    assert lr.REGLAGES_CONFORMES == rq.REGLAGES_CONFORMES and lr.COUVERTURE_UNITE == rq.COUVERTURE_UNITE
    assert lr.CONSTANTES_CONFIG["controle_intervalles"]["separateurs_intervalle"] == list(rs.SEPARATEURS_INTERVALLE)
    assert lr.CLE_ACTION == js.CLE_ACTION == "0,0"
    assert {m.rsplit("/", 1)[1] for m in lr.MODULES_PLANB} == {
        "rubrique_simplifiee.py", "juges_simplifies.py", "requalifier_juges.py", "lire_requalification.py"}
    assert lr.FICHIERS == ("notations-RS1-8B-decisives", "notations-RS1-3B-decisives", "rejeu-3B-demi",
                           "rejeu-3B-simple", "rejeu-8B-demi", "rejeu-8B-simple", "temoins")
    c = _config_reelle()
    rq.exiger_config_planb(c)
    lier = (c["run_pilote"], c["manifeste_pilote_sha256"], c["run_notations"])
    lr.exiger_config_de_l_etape({"config": c}, *lier)                                   # cas sain
    ci = c["controle_intervalles"]
    for cle, valeur in (("tolerance_simple", 1e-3), ("couverture_jetons", {"8B": 3072, "3B": 982}),
                        ("controle_intervalles", dict(ci, separateurs_intervalle=["-", "to", "or"])),
                        ("rangees_min_d1", 5)):
        autre = dict(c, **{cle: valeur})
        with pytest.raises(GardeArret, match="seuils gelés du lecteur"):
            lr.exiger_config_de_l_etape({"config": autre}, *lier)
    autre = dict(c, juges=[dict(c["juges"][0], nom="8B-instruct"), c["juges"][1]])
    with pytest.raises(GardeArret, match="juges du run de l'étape"):
        lr.exiger_config_de_l_etape({"config": autre}, *lier)


def test_rapport_de_rangee_aller_et_retour():
    """Le rapport d'une rangée écrit par le lanceur (`rapport_de_la_rangee`), remis en forme par le lecteur, redonne
    exactement le rapport de `jouer_episodes` pour les clés gardées (aucune valeur recalculée)."""
    brut = _rapport("juge-RS1-8B/2601.00001v1/e0/passe-0", lc=50, ng=30, graine=5)
    garde = js.rapport_de_la_rangee(brut)
    assert lr.rapport_de_jouer_episodes(garde, brut["episode"], "x") == {
        k: brut[k] for k in ("episode", "tolerance", "statistique") + CLES_RAPPORT_GARDEES}
    assert lr.CLES_GARDE_RANGEE == tuple(garde)


def test_second_calcul_du_lanceur_egal_a_la_lecture_sur_les_fonctions_pures():
    """Règle k, queues binomiales et classement des dépassements : mêmes valeurs des deux côtés, sur une grille qui
    couvre les bornes (3e-3, 1e-2, ancrages 1e-3 et 1e-2/3, rapport 3) et les grandeurs illisibles (NaN : G_S, maxima
    de zone, R_S). Décision D-1 (R-249) : l'écart connu d'avant (lanceur « illisible », lecture « trop grand ») est
    fermé ; les deux calculs rendent « illisible »."""
    assert all(rq.k_angle_mort(n) == lr.k_de(n) for n in range(1, 12_000))
    for p in (60 / 180, 9 / 180, 0.0, 0.5, 1.0):
        q = rq.queues_binomiales(p, 16, 0.005)
        assert sorted(q["basse"] + q["haute"]) == lr.queues_binomiales(p)
    c = _config_reelle()
    nan = math.nan
    zones = (0.0, 1e-4, 1e-3, 1.5e-3, 3e-3, 4.5e-3, 9e-3, 1e-2, 3e-2, nan)
    illisibles = 0
    for ecart in (3.0001e-3, 5e-3, 1e-2, 1.0001e-2, 0.5, nan):
        for mc in zones:
            for mg in zones:
                for a in (1e-4, 1e-3, 1.0001e-3, 1e-2 / 3, 4e-3, nan):
                    classe = rq.classer_depassement(ecart, mc, mg, a, c)
                    assert classe == lr.classer_depassement(ecart, mc, mg, a)
                    assert (classe == "illisible") == any(x != x for x in (ecart, mc, mg, a))
                    illisibles += classe == "illisible"
    assert illisibles > 0
    assert rq.classer_depassement(nan, 1e-4, 1e-4, 1e-4, c) == lr.classer_depassement(nan, 1e-4, 1e-4, 1e-4) == \
        "illisible"


def test_le_lecteur_lit_le_run_jouet_du_lanceur(depot_planb, monkeypatch, capsys):
    """Fichiers d'un vrai run jouet du lanceur : issue et statuts, fichiers scellés et rattachés, lecture RS1 recalculée
    égale à la lecture consignée, seuils de couverture, tirage des lots recalculé par le lecteur égal au tirage consigné
    et aux clés des rangées (D-14), décalages réellement passés exigés (D-10), garde en ligne, paliers de production et
    du chemin, contrôles négatif et positif, couverture, reproduction et témoin, lus par le lecteur sans écart de
    forme, et égaux au second calcul du lanceur (motifs du palier du chemin compris, D-1).
    SENSIBLE AU MATÉRIEL (D-10, R3-01) : lectures attendues du run jouet, effectifs minimaux à 1, mesurées sur la
    machine de la relecture R2-3 et de ces corrections : palier du chemin « fidèle » et D1 « vu » pour les deux juges ;
    palier de production « non concluant » (contrôle négatif non concluant : les rangées jouets, de 8 jetons générés au
    plus sur environ 1 000 de contexte, sont toutes courtes au sens de k(n − 1) ; structurel) ; lecture combinée « non
    concluant »."""
    depot, run, _ = _run_complet(depot_planb, capsys)
    c = _config(depot)
    noms = tuple(j["nom"] for j in c["juges"])
    lot = c["lot_juge"]
    entropie = int({g["entropie"] for g in json.loads((depot / "runs" / run / "manifeste.json").read_text())[
        "graines"].values()}.pop())
    jouet = {"JUGES": noms, "FICHIERS": lr.fichiers_de_phase(noms), "COUCHES": tuple(str(x) for x in c["couches"]),
             "TOLERANCE_SIMPLE": c["tolerance_simple"], "BORNE_DIFFUSE": c["borne_diffuse_simple"],
             "ANCRAGE_MAX": c["ancrage_max"], "ANCRAGE_MAX_BORNE": c["ancrage_max_borne"],
             "RANGEES_REJEU": 2 * lot, "RANGEES_D1": lot, "RANGEES_MIN_DEMI": 1, "RANGEES_MIN_SIMPLE": 1,
             "RANGEES_MIN_D1": 1, "SEUILS_COUVERTURE": c["couverture_jetons"], "TEMOIN_TIRAGES": 2 * lot}
    for k, v in jouet.items():
        monkeypatch.setattr(lr, k, v)
    c1 = dict(c, rangees_min_demi=1, rangees_min_simple=1, rangees_min_d1=1)
    issue = lr.issue_du_run(depot, run)
    assert issue["fichier"] == "resume" and set(issue["statuts"].values()) == {"écrit"}
    fichiers = lr.charger_fichiers(depot, run, issue)
    assert set(fichiers) == set(lr.FICHIERS) and all(v is not None for v in fichiers.values())
    h4 = {n: _scellees(depot, n) for n in noms}
    assert {n: s["seuil"] for n, s in lr.seuils_couverture(h4).items()} == c["couverture_jetons"]
    lectures = {}
    for n in noms:
        fn = fichiers[f"notations-RS1-{n}-decisives"]
        lr.relire_notations_rs1(fn["notations"], n, c["max_nouveaux_juge"])
        g_l, g_r = lr.bilan_garde(fn, n), rq.bilan_garde_en_ligne(fn["garde"]["rapports"], c1)
        assert (g_l["equivalence"], g_l["trop_beau"], g_l["sondes_justes"]) == (
            g_r["equivalence"], g_r["trop_beau"], g_r["sondes_conformes"])
        assert {k: g_l["controle_negatif"][k] for k in ("comparables", "passent", "courtes", "lecture")} == {
            k: g_r["controle_negatif"][k] for k in ("comparables", "passent", "courtes", "lecture")}
        demi, simple = fichiers[f"rejeu-{n}-demi"], fichiers[f"rejeu-{n}-simple"]
        # D-14 : tirage recalculé par le lecteur, sans le code du lanceur, égal au tirage consigné et aux clés
        lots = lr.lots_du_rejeu(h4[n], n, entropie, lot, c["max_nouveaux_juge"])
        lr.exiger_lots_du_rejeu(demi, simple, lots, n)
        cle = f"rejeu/{n}/lots"
        cadre = rq.cadre_du_rejeu(h4[n], lot, c["max_nouveaux_juge"])
        l1, l2, l3 = rq.tirer_lots(cadre, generateur(graines([cle], entropie)[cle]))
        assert lots["tirage"] == {"cadre": cadre, "L1": l1, "L2": l2, "L3": l3, "cle": cle} == demi["tirage"]
        p_l, p_r = lr.bilan_production(demi, simple, n), rq.lire_palier_production(demi, simple, c1)
        assert p_l["lecture"] == p_r["lecture"] and p_l["g_max"] == p_r["G_D_max"] and p_l["rho"] == p_r["rho"]
        cles_demi = [x["cle"] for x in demi["rangees"]]
        ch_l = lr.bilan_chemin(simple, n, cles_demi)
        ch_r = rq.lire_palier_chemin(simple, c1, c["couverture_jetons"][n])
        assert ch_l["lecture"] == ch_r["lecture"] and ch_l["motifs"] == ch_r["motifs"]
        assert sorted((d["rangee"], d["couche"], d["classe"]) for d in ch_l["depassements"]) == sorted(
            (d["cle"], d["couche"], d["classe"]) for d in ch_r["depassements"])
        assert ch_l["controle_negatif"]["lecture"] == ch_r["controle_negatif"]["lecture"]
        assert (ch_l["controle_positif_d1"]["comparables"], ch_l["controle_positif_d1"]["lecture"]) == (
            ch_r["d1"]["comparables"], ch_r["d1"]["lecture"])
        assert (ch_l["couverture"]["atteinte"], ch_l["couverture"]["jetons_generes"]) == (
            ch_r["couverture"]["atteinte"], ch_r["couverture"]["jetons_generes_max"])
        rep = lr.bilan_reproduction(demi, h4[n], n)
        assert rep["identiques"] == sum(x["reproduction"]["identique"] for x in demi["rangees"])
        taux = sum(bool(x["tronquee"]) for x in h4[n]) / len(h4[n])
        t_l, t_r = lr.bilan_temoin(fichiers["temoins"], n, taux), rq.bilan_temoin(fichiers["temoins"]["juges"][n],
                                                                                   c["temoin_queue"])
        assert (t_l["t_w"], t_l["rangees"]) == (t_r["T_w"], t_r["rangees"]) and t_l["rangees"] == 2 * lot
        lectures[n] = {"chemin": ch_l["lecture"], "d1": ch_l["controle_positif_d1"]["lecture"],
                       "production": p_l["lecture"], "controle_negatif_production": p_l["controle_negatif"]["lecture"]}
    # lectures attendues du run jouet (SENSIBLE AU MATÉRIEL, D-10) : elles remplacent « assert lectures »
    assert lectures == {n: {"chemin": "fidèle", "d1": "vu", "production": "non concluant",
                            "controle_negatif_production": "non concluant"} for n in noms}
    rejeu = {n: {"chemin": {"lecture": lectures[n]["chemin"]}, "production": {"lecture": lectures[n]["production"]}}
             for n in noms}
    assert lr.lecture_combinee(rejeu)["lecture"] == "non concluant"                  # constantes du jouet : JUGES
