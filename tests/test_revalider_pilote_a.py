"""Revalidation courte de l'équivalence sur le domaine du pilote (T0.5, P-007 (b)), sur modèle jouet : gardes de
configuration et de tâches, lecture gelée d'un bras et règle de choix, déroulé complet ; cas sain et artefacts (R5)."""
from __future__ import annotations

import json

import pytest

from conftest import committer
from controle_ia.environnements import revalider_pilote_a as rv
from controle_ia.gardes import GardeArret
from controle_ia.harnais.modeles import regler_determinisme
from controle_ia.scellement import sceller

regler_determinisme(1)

CONFIG = {"N": 1, "T": 2, "episodes_par_tache": 1, "lot": 2, "max_nouveaux": 6, "temperature": 1.0,
          "couches": [0, 1, 2], "fraction_equivalence": 1.0, "statistique_equivalence": "q99",
          "tolerance_equivalence": 0.2, "positions_min_controle_negatif": 4, "actions_min_controle_negatif": 1,
          "fraction_min_controle_negatif": 0.95, "agent": {"nom": "agent-jouet"}, "mode": "jouet", "fils": 1,
          "bras": ["defaut", "math"], "nombre_taches": 4, "episodes_repere": [0, 2], "actions_min_comparees": 4,
          "part_min_contexte_couvert": 0.9, "memoire_carte_min_gio": 75, "duree_max_s": 600}


def _taches(prefixe, n):
    return [{"identifiant": f"{prefixe}.{k:05d}v1", "questions": f"Why do routers matter in setting {k}? " * (1 + k),
             "classification": {"theory_experiment": "mostly_experiments", "data_type": "real_only", "domains": []}}
            for k in range(n)]


def _fichiers(depot, entrainement, evaluation):
    chemins = []
    for nom, taches in (("entrainement", entrainement), ("evaluation", evaluation)):
        f = depot / f"taches-{nom}.json"
        f.write_text(json.dumps({"taches": taches}), encoding="utf-8")
        sceller(f)
        chemins.append(str(f))
    committer(depot)
    return chemins


def test_configuration_gardee():
    rv.exiger_config_revalidation(CONFIG)
    with pytest.raises(GardeArret, match="incomplète"):
        rv.exiger_config_revalidation({k: v for k, v in CONFIG.items() if k != "part_min_contexte_couvert"})
    with pytest.raises(GardeArret, match="dans cet ordre"):
        rv.exiger_config_revalidation(dict(CONFIG, bras=["math", "defaut"]))
    with pytest.raises(GardeArret, match="99e centile"):
        rv.exiger_config_revalidation(dict(CONFIG, statistique_equivalence="max"))
    with pytest.raises(GardeArret, match="repère"):
        rv.exiger_config_revalidation(dict(CONFIG, episodes_repere=[0, 9]))


def test_lecture_d_un_bras_et_regle_de_choix():
    mesures = {"actions_comparees": 80, "q99_max": 0.05, "ecart_max": 0.4, "contexte_max": 4000,
               "contexte_max_joue": 4200, "actions_remplies": 30}
    cn = {"lecture": "conforme"}
    repere = {"7": {"q99": 0.03}, "15": {"q99": 0.06}, "23": {"q99": 0.09}}
    cfg = dict(CONFIG, actions_min_comparees=40)
    assert rv.lire_bras(mesures, cn, repere, True, cfg)["conforme"]
    artefacts = [
        (dict(mesures, q99_max=0.21), cn, repere, True),
        (dict(mesures, q99_max=float("nan")), cn, repere, True),
        (mesures, {"lecture": "contraire"}, repere, True),
        (mesures, {"lecture": "non concluant"}, repere, True),
        (mesures, cn, dict(repere, **{"23": {"q99": 0.11}}), True),
        (mesures, cn, repere, False),
        (dict(mesures, contexte_max=3700), cn, repere, True),
        (dict(mesures, actions_remplies=0), cn, repere, True),
        (dict(mesures, actions_comparees=39), cn, repere, True),
    ]
    for m, c, r, rejeu in artefacts:
        assert not rv.lire_bras(m, c, r, rejeu, cfg)["conforme"], (m, c, r, rejeu)
    assert not rv.lire_bras({}, {}, None, None, cfg, panne="mémoire")["conforme"]
    assert not rv.lire_bras(mesures, cn, repere, True, cfg)["audit_R4_ecarts_tous_nuls"]
    assert rv.lire_bras(dict(mesures, ecart_max=0.0, q99_max=0.0), cn, repere, True, cfg)["audit_R4_ecarts_tous_nuls"]
    assert rv.choisir_noyau({"defaut": {"conforme": True}, "math": {"conforme": True}}) == "defaut"
    assert rv.choisir_noyau({"defaut": {"conforme": False}, "math": {"conforme": True}}) == "math"
    assert rv.choisir_noyau({"defaut": {"conforme": False}, "math": {"conforme": False}}) is None


def test_taches_d_evaluation_refusees(depot):
    entrainement, evaluation = _taches("2601", 4), _taches("2602", 2)
    e, v = _fichiers(depot, entrainement + [evaluation[0]], evaluation)
    with pytest.raises(GardeArret, match="aussi tâches d'évaluation"):
        rv.taches_d_entrainement(e, v, 4)


def test_reel_sans_preenregistrement_refuse(depot):
    e, v = _fichiers(depot, _taches("2601", 4), _taches("2602", 2))
    with pytest.raises(GardeArret, match="R1"):
        rv.executer(dict(CONFIG, mode="reel"), depot, "20261007-000000-revalidation", None, e, v)
    with pytest.raises(GardeArret, match="entropie d'essai"):
        rv.executer(CONFIG, depot, "20261007-000000-revalidation", "prereg.md", e, v, entropie_essai=3)


def test_deroule_complet_en_mode_jouet(depot):
    e, v = _fichiers(depot, _taches("2601", 5), _taches("2602", 2))
    resume = rv.executer(CONFIG, depot, "20261007-000000-revalidation-jouet", None, e, v, entropie_essai=11)
    assert set(resume["lectures"]) == {"defaut", "math"}
    for b in ("defaut", "math"):
        r = resume["bras"][b]
        assert r["rejeu_identique"] is True
        assert r["mesures"]["actions_comparees"] == 8          # 4 épisodes × 2 actions, toutes échantillonnées
        assert set(r["repere"]) == {"0", "1", "2"} and all(x["jetons"] > 0 for x in r["repere"].values())
        assert r["controle_negatif"]["lecture"] in ("conforme", "contraire", "non concluant")
        assert set(r["zone_generee"]) >= {"q99_generee_max", "fraction", "part_zone_generee_sous_1pc"}
    assert "proposition_au_noeud" in resume
    assert resume["noyau_retenu"] == rv.choisir_noyau(resume["lectures"])
    d = depot / "diag" / "20261007-000000-revalidation-jouet"
    assert (d / "resume.json.sha256").is_file() and (d / "episodes.json.sha256").is_file()
    episodes = json.loads((d / "episodes.json").read_text())["resultat"]
    assert [f["tache"] for f in episodes["defaut"]] == [t["identifiant"] for t in _taches("2601", 4)]
    assert sum("transcriptions" in f for f in episodes["defaut"]) == 2


def test_garde_trop_stricte_ou_aveugle_donne_un_noeud(depot):
    # Sur le modèle jouet en demi-précision, le défaut D1 (décalage d'une position) donne des écarts de l'ordre de
    # 3e-3, du même ordre que l'arrondi (essai de la session 11) : il ne s'y distingue pas. La sensibilité de la garde
    # au décalage se lit sur le modèle réel, par le contrôle négatif (R2), comme dans T0.4 v3 (P5). Ici, la lecture R1
    # est éprouvée de bout en bout par une tolérance sous l'arrondi du jouet (1e-4 ; 99e centiles de 1e-3 à 3e-3 avec
    # des actions de 40 jetons), et R2 par une tolérance aveugle (1e9).
    e, v = _fichiers(depot, _taches("2601", 4), _taches("2602", 2))
    stricte = rv.executer(dict(CONFIG, max_nouveaux=40, tolerance_equivalence=1e-4), depot,
                          "20261007-000001-revalidation-stricte", None, e, v, entropie_essai=11)
    assert stricte["noeud"]
    for b, x in stricte["lectures"].items():  # la lecture suit la mesure, bras par bras
        assert x["R1_garde_saine"] == (stricte["bras"][b]["mesures"]["q99_max"] <= 1e-4)
    # au noyau « math », le contexte coïncide au bit près : une zone générée sous 1 % des positions donne un 99e
    # centile nul (garde aveugle, vue par le contrôle négatif) ; au noyau par défaut, l'arrondi le rend non nul
    assert not stricte["lectures"]["defaut"]["R1_garde_saine"]
    committer(depot)
    aveugle = rv.executer(dict(CONFIG, tolerance_equivalence=1e9), depot, "20261007-000002-revalidation-aveugle",
                          None, e, v, entropie_essai=11)
    assert aveugle["noeud"]
    assert all(x["R2_controle_negatif"] != "conforme" for x in aveugle["lectures"].values())


def _fiche_longue(q99_action, q99_generee, max_decale, generes=20, contexte=4980):
    cle = "0,9"
    return {"equivalence": {
        "ecarts_q99": {cle: {7: q99_action}}, "ecarts": {cle: {7: max(q99_generee, q99_action)}},
        "positions_capturees": {cle: contexte + generes}, "longueurs_contexte": {cle: contexte},
        "lignes": {cle: {"remplissage": 3}},
        "profils": {cle: {7: {"generee": {"jetons": generes, "q99": q99_generee}}}},
        "controle_negatif_zone_generee": {cle: {7: {"positions": generes - 1, "max": max_decale, "q99": q99_action}}}},
        "actions": [{"debut": contexte}]}


def test_garde_zone_generee_et_proposition_au_noeud():
    # zone générée de 20 positions sur 5 000 : la garde de l'action entière est aveugle au décalage (99e centile du
    # contexte), la garde restreinte le voit (maximum décalé 0,8)
    fiches = [_fiche_longue(0.03, 0.05, 0.8) for _ in range(12)]
    zg = rv.garde_zone_generee(fiches, 0.2, 4)
    assert zg["q99_generee_max"] == 0.05 and zg["comparables"] == 12 and zg["fraction"] == 1.0
    assert zg["part_zone_generee_sous_1pc"] == 1.0
    cfg = dict(CONFIG, actions_min_comparees=10, actions_min_controle_negatif=10)
    mesures = rv.domaine_et_garde(fiches)
    repere = {"7": {"q99": 0.05}}
    lecture = rv.lire_bras(mesures, {"lecture": "contraire"}, repere, True, cfg, zone_generee=zg)
    assert not lecture["conforme"] and lecture["garde_zone_generee_conforme"]
    assert lecture["aveugle_action_entiere_seulement"]
    # la garde restreinte voit aussi un vrai défaut de la zone générée (99e centile 0,5) : pas de proposition
    zg_ko = rv.garde_zone_generee([_fiche_longue(0.03, 0.5, 0.8) for _ in range(12)], 0.2, 4)
    lecture_ko = rv.lire_bras(mesures, {"lecture": "contraire"}, repere, True, cfg, zone_generee=zg_ko)
    assert not lecture_ko["garde_zone_generee_conforme"] and not lecture_ko["aveugle_action_entiere_seulement"]
    # contrôle négatif restreint aveugle (maximum décalé sous le seuil) : pas de proposition non plus
    zg_aveugle = rv.garde_zone_generee([_fiche_longue(0.03, 0.05, 0.1) for _ in range(12)], 0.2, 4)
    assert not rv.lire_bras(mesures, {"lecture": "contraire"}, repere, True, cfg,
                            zone_generee=zg_aveugle)["aveugle_action_entiere_seulement"]
