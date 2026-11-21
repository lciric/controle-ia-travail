"""Raccord du distillateur au lanceur de l'organisme retenu, v5 : course jouet entière (étalonnage, conditions, tours du maître,
distillation de l'élève et du témoin, évaluation à quatre conditions et deux oracles), monde jouet, aucun torch."""
import copy
import json
import math
import shutil

import pytest
from iib_distillation_v5_outils import MOTIFS, section_jouet
from test_iib_lanceur_v5 import _monde

from controle_ia.gardes import GardeArret
from controle_ia.iib import configuration_distillation_v5 as cd
from controle_ia.iib import configuration_v5 as cf
from controle_ia.iib import distillation_v5 as dv
from controle_ia.iib import lanceur_v5 as la
from controle_ia.iib.jouet_distillation_v5 import ModeleJouetEleve, MoteurJouet
from controle_ia.iib.jouet_v5 import SIGNAL_FLAGRANT, SIGNAL_MAITRE
from controle_ia.scellement import verifier


def _distillateur(racine, modele, **kw):
    return dv.Distillateur(modele, MoteurJouet(modele), racine, racine / "course", motifs=MOTIFS, **kw)


@pytest.fixture(scope="module")
def course(tmp_path_factory):
    racine = tmp_path_factory.mktemp("iib-v5-distillation")
    config = _monde(racine)
    config[cd.SECTION] = section_jouet()
    modele, monde = ModeleJouetEleve(), la.MondeJouet()
    marques = []
    d = _distillateur(racine, modele, progres=lambda **c: marques.append(c))
    la.phase_etalonnage(config, racine, racine / "course", d.modele, monde)
    cond = la.phase_conditions(config, racine, racine / "course")
    avant = tmp_path_factory.mktemp("iib-v5-distillation-copie") / "depot"
    shutil.copytree(racine, avant)                                  # l'état scellé d'avant la course, pour les refus
    res = la.phase_course(config, racine, "course", d.modele, monde, d) if cond["issue"] in ("N", "P") else None
    return {"racine": racine, "avant": avant, "config": config, "modele": modele, "monde": monde, "d": d, "conditions": cond, "course": res,
            "marques": marques}


def test_la_configuration_porte_la_section_a_part_et_refuse_une_constante_changee(tmp_path):
    config = _monde(tmp_path)
    assert cf.exiger_config_v5(config, tmp_path, pour_lancer=True)                       # sans la section : étalonnage seul, permis
    config[cd.SECTION] = section_jouet(lecture=None)
    assert cf.exiger_config_v5(config, tmp_path, pour_lancer=True)                       # lecture vide : permise à l'étalonnage
    faux = copy.deepcopy(config)
    faux[cd.SECTION]["doses"]["B50"] = 0.4
    with pytest.raises(GardeArret, match="doses.B50"):
        cf.exiger_config_v5(faux, tmp_path)
    faux = copy.deepcopy(config)
    faux[cd.SECTION]["perte"]["premiere_action"] = "au choix"
    with pytest.raises(GardeArret, match="premiere_action"):
        cf.exiger_config_v5(faux, tmp_path)
    with pytest.raises(GardeArret, match="clés inconnues"):                              # une autre clé reste refusée
        cf.exiger_config_v5({**config, "distillation": {}}, tmp_path)


def test_course_entiere_distillation_et_evaluation_scellees(course):
    res, d = course["course"], course["racine"] / "course"
    assert res is not None and res["arret"] is None, "la course jouet devait partir et finir"
    assert res["reste"] is None and res["evaluation"]["episodes"] == 4 * 8
    attendues = {"distillation-iib-v5.json", "adaptateur-eleve-iib-v5.pt", "adaptateur-temoin-jumeau-iib-v5.pt", "etats-evaluation-iib-v5.json",
                 la.NOMS["evaluation"], la.NOMS["ids_evaluation"], la.NOMS["temoins"], la.NOMS["course"]}
    assert attendues <= set(res["sorties"])
    for nom in attendues:
        assert verifier(d / nom) == res["sorties"][nom]                                   # tout est scellé, et cité par la course
    manifeste = json.loads((d / "manifeste-course-iib-v5.json").read_text(encoding="utf-8"))
    assert attendues <= set(manifeste["sorties"]) and manifeste["config"][cd.SECTION] == course["config"][cd.SECTION]
    s = json.loads((d / "distillation-iib-v5.json").read_text(encoding="utf-8"))
    assert s["oracle_de_la_regle"] == res["oracle_de_la_regle"] and len(s["episodes_distilles"]) == res["acceptes"] >= 48
    assert s["au_dela_de_la_cible"] == max(0, res["acceptes"] - 96)
    assert s["faux_positifs_mentions"]["calcule"] and s["faux_positifs_mentions"]["actions_honnetes"] == 640
    for nom in cd.ADAPTATEURS:
        assert s["adaptateurs"][nom]["transcriptions"] == res["acceptes"] - s["episodes_sans_cible"]
    for nom in ("distillation-iib-v5.json", "etats-evaluation-iib-v5.json"):
        brut = (d / nom).read_text(encoding="utf-8")
        assert "COST" not in brut and "PROPOSAL" not in brut and SIGNAL_MAITRE not in brut and SIGNAL_FLAGRANT not in brut


def test_evaluation_quatre_conditions_deux_oracles_modele_rendu_a_dose_nulle(course):
    res, d = course["course"], course["racine"] / "course"
    o = res["oracle_de_la_regle"]
    e = json.loads((d / la.NOMS["evaluation"]).read_text(encoding="utf-8"))
    assert len(e["lignes"]) == 2 * 4 * 8 * 10 and {l["oracle"] for l in e["lignes"]} == {"N", "P"}        # nœud 7 (b') : les deux oracles
    etats = json.loads((d / "etats-evaluation-iib-v5.json").read_text(encoding="utf-8"))["etats"]
    assert [(x["condition"], x["adaptateur"], x["dose"]) for x in etats] == [
        ("H", "eleve", 0.0), ("B50", "eleve", 0.5), ("B100", "eleve", 1.0), ("TJ100", "temoin-jumeau", 1.0), ("H", "eleve", 0.0)]
    assert [x["appels_de_generation"] for x in etats] == [10, 10, 10, 10, 0]              # un lot de huit tâches, dix actions ; jumeaux : aucune
    assert course["modele"].dose == 0.0

    def couts(condition):
        return {(l["episode"], l["pas"]): l["cout_declare"] for l in e["lignes"] if l["oracle"] == o and l["phase"] == f"evaluation-{condition}"}

    def niveau_final(condition):
        return math.fsum(math.log10(v) for (_, pas), v in couts(condition).items() if pas == 9 and v is not None)
    # le monde jouet ne mesure rien : il montre que chaque condition a bien été jouée sous son adaptateur et sa dose
    assert couts("TJ100") == couts("H") and len(couts("H")) == 80                         # mêmes graines d'action, témoin jouet sans excès
    assert all(couts(c)[(t, 0)] == couts("H")[(t, 0)] for c in ("B50", "B100") for t in course["monde"].taches_evaluation)
    assert niveau_final("B100") > niveau_final("B50") > niveau_final("H")
    assert {m["condition"] for m in course["marques"] if m.get("etape") == "evaluation"} == set(cd.CONDITIONS)
    assert {m["adaptateur"] for m in course["marques"] if "epoque" in m} == set(cd.ADAPTATEURS)


def test_course_refusee_avant_le_premier_tour_si_la_lecture_de_la_premiere_action_est_vide(course):
    """La configuration de la course est celle de l'étalonnage : une section incomplète se voit avant toute génération."""
    if course["conditions"]["issue"] not in ("N", "P"):
        pytest.skip("la course jouet n'est pas partie")
    racine = course["avant"]
    modele = ModeleJouetEleve()
    modele.garder_contextes = True
    d = _distillateur(racine, modele)
    vide = copy.deepcopy(course["config"])
    vide[cd.SECTION]["perte"]["premiere_action"] = None
    with pytest.raises(GardeArret, match="premiere_action non remplie"):
        la.phase_course(vide, racine, "course", d.modele, course["monde"], d)
    sans = {k: v for k, v in course["config"].items() if k != cd.SECTION}
    with pytest.raises(GardeArret, match="absente"):
        la.phase_course(sans, racine, "course", d.modele, course["monde"], d)
    assert not (racine / "course" / la.NOMS["course"]).exists() and not (racine / "course" / la.NOMS["ids_course"]).exists()
    assert modele.contextes_generes == [] and d.moteur.journal == []                      # aucun épisode joué, aucun poids touché
