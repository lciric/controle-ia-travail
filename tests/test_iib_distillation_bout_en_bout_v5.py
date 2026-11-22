"""Raccord du distillateur au lanceur de l'organisme retenu, v5 : course jouet entière (étalonnage, conditions, tours du maître,
distillation de l'élève et du témoin, évaluation à quatre conditions et deux oracles), monde jouet, aucun torch."""
import copy
import json
import math
import shutil
from pathlib import Path

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
    la.phase_etalonnage(config, racine, racine / "course", d.modele, monde, carte=False)      # poste simulé sans carte (correctif 0011)
    cond = la.phase_conditions(config, racine, racine / "course")
    avant = tmp_path_factory.mktemp("iib-v5-distillation-copie") / "depot"
    shutil.copytree(racine, avant)                                  # l'état scellé d'avant la course, pour les refus
    res = la.phase_course(config, racine, "course", d.modele, monde, d, carte=False) if cond["issue"] in ("N", "P") else None
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
        la.phase_course(vide, racine, "course", d.modele, course["monde"], d, carte=False)
    sans = {k: v for k, v in course["config"].items() if k != cd.SECTION}
    with pytest.raises(GardeArret, match="absente"):
        la.phase_course(sans, racine, "course", d.modele, course["monde"], d, carte=False)
    assert not (racine / "course" / la.NOMS["course"]).exists() and not (racine / "course" / la.NOMS["ids_course"]).exists()
    assert modele.contextes_generes == [] and d.moteur.journal == []                      # aucun épisode joué, aucun poids touché


# ------------------------------------------------------------------------------------------------------------------------------
# Correctif 0015 : point d'entrée de la course, versée par tour et poussée, sur le vrai script de consignation de l'amorce
# ------------------------------------------------------------------------------------------------------------------------------
RUN_E, RUN_C = "20991231-000020-iib-jouet", "20991231-000021-iib-course-jouet"


@pytest.fixture(scope="module")
def point_d_entree(tmp_path_factory):
    """Étalonnage, conditions puis course, chacun par `python -m controle_ia.iib.lanceur_v5`, comme l'amorce les appelle, sur un
    poste simulé sans carte ni accord ; chaque lot et chaque tour poussés par le script de consignation de l'amorce vers une
    origine nue locale."""
    import os
    import subprocess
    import sys

    from iib_v5_outils import environnement_sans_carte
    from test_iib_versement_v5 import BRANCHE, git, poste

    t = tmp_path_factory.mktemp("course-point-d-entree")
    p = poste(t)
    d = p["d"]
    config = copy.deepcopy(p["config"])
    config[cd.SECTION] = section_jouet()
    chemin = d / "entrees" / "config-iib-v5-jouet.json"
    chemin.write_text(json.dumps(config, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    from controle_ia.scellement import sceller

    sceller(chemin)
    git(d, "add", "-A")
    git(d, "commit", "-qm", "configuration jouet de la course")
    git(d, "push", "-q", "origin", BRANCHE)
    env = environnement_sans_carte(t / "poste", os.environ)
    outils = Path(env["PATH"])
    for o in ("bash", "flock", "timeout", "tee", "date", "stat", "sha256sum", "tr", "cut", "tail", "head", "mktemp", "sleep", "cat", "env"):
        cible = shutil.which(o)
        if cible and not (outils / o).exists():
            os.symlink(cible, outils / o)
    env.update(PYTHONPATH=str(Path(__file__).resolve().parents[1] / "src"), IIB_CONSIGNER=str(p["script"]))
    base = [sys.executable, "-m", "controle_ia.iib.lanceur_v5", "--config", "entrees/config-iib-v5-jouet.json"]

    def lancer(*a, **kw):
        return subprocess.run(base + list(a), cwd=d, env={**env, **kw}, capture_output=True, text=True, timeout=900)
    e = lancer("--phase", "etalonnage", "--run-id", RUN_E)
    assert e.returncode == 0, e.stderr[-1500:]
    c = lancer("--phase", "conditions", "--run-id", RUN_E)
    assert c.returncode == 0, c.stderr[-800:]
    git(d, "add", "-A")
    git(d, "add", "-f", "donnees")
    git(d, "commit", "-qm", "étalonnage et désignation consignés (comme le versement de la session avant l'ordre de la course)")
    git(d, "push", "-q", "origin", BRANCHE)
    r = lancer("--phase", "course", "--run-id", RUN_C, "--etalonnage", RUN_E) if json.loads(c.stdout)["issue"] in ("N", "P") else None
    return {**p, "env": env, "lancer": lancer, "conditions": json.loads(c.stdout), "course": r}


def test_point_d_entree_de_la_course_versee_par_tour_poussee_et_resumee(point_d_entree):
    from test_iib_versement_v5 import BRANCHE, git

    r, d = point_d_entree["course"], point_d_entree["d"]
    assert r is not None, "la course jouet devait partir"
    assert r.returncode == 0, r.stderr[-1500:]
    sortie = json.loads(r.stdout)
    assert sortie["phase"] == "course" and sortie["etalonnage"] == RUN_E and sortie["arret"] is None
    resume = json.loads((d / "diag" / RUN_C / "resume.json").read_text(encoding="utf-8"))["resultat"]
    verifier(d / "diag" / RUN_C / "resume.json")
    assert resume["evaluation"]["episodes"] == 4 * 8 and resume["reste"] is None and resume["identifiants_de_l_etalonnage"] == 28
    assert resume["versements"] and all(v["poussee"] == "faite" for v in resume["versements"])
    dossier = d / "diag" / RUN_E
    tours = sorted((dossier / "tours").glob("tour-*-maitre.json"))
    course = json.loads((dossier / la.NOMS["course"]).read_text(encoding="utf-8"))
    assert len(tours) == len(course["tours"]) >= 1
    # correctif 0016 : replis de la forme du lot des suites écrits (aucun sur le jouet), au résumé, à la course, à l'évaluation
    assert resume["replis_forme_lot_suites"] == course["replis_forme_lot_suites"] == []
    assert json.loads((dossier / la.NOMS["evaluation"]).read_text(encoding="utf-8"))["replis_forme_lot_suites"] == []
    # chaque tour est sur la branche distante, dans un commit à lui (« versement tour NNN »), avant la fin de la course
    distant = set(git(point_d_entree["origine"], "ls-tree", "-r", "--name-only", BRANCHE).splitlines())
    messages = git(point_d_entree["origine"], "log", "--format=%s", BRANCHE).splitlines()
    for f in tours:
        rel = f"diag/{RUN_E}/tours/{f.name}"
        assert {rel, rel + ".sha256", rel.replace("/tour-", "/ids-tour-")} <= distant
        assert verifier(f)
    assert sum("(versement tour " in m for m in messages) == len(tours)
    for c in ("H", "B50", "B100", "TJ100"):
        assert {f"diag/{RUN_E}/evaluation/ids-evaluation-{c}.json", f"diag/{RUN_E}/evaluation/oracles-evaluation-{c}.json"} <= distant
    assert any("(versement distillation)" in m for m in messages) and f"diag/{RUN_E}/adaptateur-eleve-iib-v5.pt" in distant
    # les sorties par tour réunies sont celles de la course ; les sorties par condition réunies sont celles de l'évaluation
    oc = json.loads((dossier / la.NOMS["oracle_course"]).read_text(encoding="utf-8"))
    assert [l for f in tours for l in json.loads(f.read_text(encoding="utf-8"))["lignes"]] == oc["lignes"]
    ev = json.loads((dossier / la.NOMS["evaluation"]).read_text(encoding="utf-8"))
    par = [l for c in ("H", "B50", "B100", "TJ100") for l in json.loads((dossier / "evaluation" / f"oracles-evaluation-{c}.json").read_text(encoding="utf-8"))["lignes"]]
    assert sorted(map(json.dumps, par)) == sorted(map(json.dumps, ev["lignes"]))
    progres = [l for l in r.stderr.splitlines() if l.startswith("PROGRES ")]
    assert sum("etape=course" in l and " tour=" in l for l in progres) == len(tours)
    assert all(l.endswith(" replis=0") for l in progres if "etape=course" in l and " tour=" in l)
    assert not any("acceptes=" in l for l in progres if "etape=course" in l)      # marque neutre : aucun compte d'acceptés
    for f in tours:
        brut = f.read_text(encoding="utf-8")
        assert "COST" not in brut and SIGNAL_MAITRE not in brut


def test_point_d_entree_de_la_course_refus_avant_le_premier_tour(point_d_entree, tmp_path):
    from test_iib_versement_v5 import git

    lancer, d = point_d_entree["lancer"], point_d_entree["d"]
    git(d, "add", "-A")
    git(d, "add", "-f", "donnees")
    git(d, "commit", "-qm", "course consignée")
    # sans --etalonnage, ou --etalonnage illisible : refus ; --etalonnage hors de la course : refus
    sans = lancer("--phase", "course", "--run-id", "20991231-000022-iib-course-jouet")
    assert sans.returncode == 1 and "--etalonnage" in sans.stderr
    assert lancer("--phase", "course", "--run-id", "20991231-000023-iib-course-jouet", "--etalonnage", "../x").returncode == 1
    hors = lancer("--phase", "etalonnage", "--run-id", "20991231-000024-iib-jouet", "--etalonnage", RUN_E)
    assert hors.returncode == 1 and "phase course" in hors.stderr
    # second passage de la course dans le même dossier : refus, aucun manifeste de course nouveau n'a de tour
    if point_d_entree["course"] is not None:
        deux = lancer("--phase", "course", "--run-id", "20991231-000025-iib-course-jouet", "--etalonnage", RUN_E)
        assert deux.returncode == 1 and "course déjà jouée" in deux.stderr
        assert not any("etape=course tour=" in l for l in deux.stderr.splitlines())
    # configuration différente de celle que le manifeste de l'étalonnage a scellée : refus
    from controle_ia.scellement import sceller

    autre = json.loads((d / "entrees" / "config-iib-v5-jouet.json").read_text(encoding="utf-8"))
    autre["prefixe_graines"] = "autre/"
    f = d / "entrees" / "config-autre.json"
    f.write_text(json.dumps(autre, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(f)
    git(d, "add", "-A")
    git(d, "commit", "-qm", "configuration différente")
    r = subprocess_course(point_d_entree, "entrees/config-autre.json")
    assert r.returncode == 1 and "n'est pas celle que le manifeste de l'étalonnage a scellée" in r.stderr


def subprocess_course(p, config):
    import subprocess
    import sys

    return subprocess.run([sys.executable, "-m", "controle_ia.iib.lanceur_v5", "--config", config, "--phase", "course", "--run-id",
                           "20991231-000026-iib-course-jouet", "--etalonnage", RUN_E], cwd=p["d"], env=p["env"], capture_output=True, text=True,
                          timeout=300)


def test_phase_course_en_mode_reel_refuse_sans_distillateur_ou_sans_poussee(tmp_path, monkeypatch):
    """Garde : en mode réel, ni course sans distillateur (rien ne serait mesuré), ni course sans poussée par tour ; cas sain :
    en mode jouet, sans l'un ni l'autre, la course est permise (essais) et le dit (`reste`)."""
    config = _monde(tmp_path)
    config["mode"] = "reel"
    monkeypatch.setattr(la, "exiger_accord", lambda *a, **k: "GO-2099-01-01-01")      # la seule garde visée
    for dist, vers in ((None, object()), (object(), None), (None, None)):
        with pytest.raises(GardeArret, match="sans poussée par tour ou sans distillateur"):
            la.phase_course(config, tmp_path, "course", None, None, dist, {}, carte=False, versement=vers)
