"""Lecture de bout en bout du pilote de T0.5 (`lire_pilote`), sur un run synthétique écrit sous un vrai manifeste :
étiquetage (tirage, lots, contrôles, tentatives), mesures, décomposition, familles, coût, kappa, audit, prédictions,
runs partiels, gardes (cas sain et artefact, R5)."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import numpy as np
import pytest

from conftest import committer
from controle_ia.environnements import lire_pilote as lp
from controle_ia.environnements.propositions import EnvironnementPropositions, Tache
from controle_ia.environnements.rubrique import CRITERES, score_sur_100
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste, ecrire_resultat
from controle_ia.scellement import sceller

REEL = Path(__file__).resolve().parents[1]
RUN, ANALYSE = "20261010-120000-t05-pilote", "20261011-090000-t05-pilote-analyse"
ENTROPIE = 31337


def _action(k: int, cout: str | None = "120") -> str:
    lignes = [f"ACTION: ADD", f"TITLE: Experiment {k}", f"PROPOSAL: Run study {k} with a careful design.",
              f"CONTROLS: baseline {k}; ablation {k}"]
    if cout is not None:
        lignes.append(f"COST: {cout}")
    lignes.append("PREDICTION: modest gains.")
    return "\n".join(lignes)


def _taches(n: int, steriles: int) -> list[dict]:
    taches = []
    for k in range(n):
        cibles = {"controls": [{"id": f"C{i}", "description": f"control {i} of task {k}"} for i in (1, 2, 3)],
                  "fruitful_directions": [{"id": "F1", "description": f"direction F1 of task {k}"}],
                  "sterile_directions": ([{"id": "S1", "description": f"direction S1 of task {k}"}]
                                         if k < steriles else []),
                  "compute": {"reference_gpu_hours": 100 if k % 2 == 0 else None, "basis": "reported"}}
        taches.append({"identifiant": f"2601.{k:05d}v1", "questions": f"Research question of task {k}?",
                       "classification": None, "cibles": cibles})
    return taches


def _notes(rng, base: dict, bruit: float) -> dict:
    """Notes d'une notation : base de l'ensemble (tâche et génération), plus le bruit du juge, critère par critère."""
    return {nom: int(np.clip(round(base[nom] + (rng.normal(0, bruit) if bruit else 0.0)), lo, hi))
            for nom, lo, hi in CRITERES}


def _base(rng, decalage: float) -> dict:
    return {nom: (lo + hi) / 2 + decalage + rng.normal(0, 0.7) for nom, lo, hi in CRITERES}


def _fiche(tache: dict, k: int, invalide: bool = False, vide: bool = False) -> dict:
    episode = f"{tache['identifiant']}/e{k}"
    textes = [] if vide else [_action(1), "no action here" if invalide else _action(2, cout="about 300 GPU-hours")]
    env = EnvironnementPropositions(Tache(tache["identifiant"], tache["questions"]), 1, max(len(textes), 1))
    journal = [(0, s, x) for s, x in enumerate(textes)]
    actions = [{"agent": 0, "pas": s, "debut": 100 * (s + 1), "fin": 100 * (s + 1) + 40, "ids": list(range(40)),
                "texte": x} for s, x in enumerate(textes)]
    return {"episode": episode, "tache": tache["identifiant"], "bilan": env.bilan(journal),
            "jetons_par_action": [40] * len(textes), "actions": actions,
            "equivalence": {"positions_capturees": {"0,0": 140} if textes else {},
                            "ecarts_q99": {"0,0": {"7": 0.01, "15": 0.02}} if textes else {}},
            "empreintes": {}}


def _prereg(depot: Path, commit: str, nom: str = "prereg-pilote.md") -> Path:
    (depot / "prereg").mkdir(exist_ok=True)
    p = depot / "prereg" / nom
    corps = ["# Préenregistrement de test", "", f"- Commit du code d'analyse : `{commit}`", f"- Entropie : `{ENTROPIE}`",
             ""]
    for s in ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
              "Critères de lecture gelés", "Liste d'arrêt"):
        corps += [f"## {s}", "", f"contenu {s}", ""]
    corps += ["## Contre-lecture", "", f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`", ""]
    p.write_text("\n".join(corps), encoding="utf-8")
    sceller(p)
    return p


def _modules(depot: Path) -> None:
    for m in lp.MODULES_LECTURE:
        (depot / m).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(REEL / m, depot / m)


def _commit(depot: Path) -> str:
    return subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                          check=True).stdout.strip()


def construire(depot: Path, n: int = 50, steriles: int = 20, bruit_juge: float = 1.0, etapes=("tout",),
               graine: int = 3) -> dict:
    """Run de pilote synthétique sous un manifeste décisif : tâches scellées, fiches, notations des deux juges,
    appariements (propositions et énoncé seul), résumé. `etapes` : ("tout",), ("decisives",) ou ("aucune",)."""
    rng = np.random.default_rng(graine)
    _modules(depot)
    taches = _taches(n, steriles)
    f = depot / "taches.json"
    f.write_text(json.dumps({"taches": taches}), encoding="utf-8")
    sha = sceller(f)
    committer(depot)
    prereg = _prereg(depot, _commit(depot))
    committer(depot)
    config = {"max_nouveaux": 400, "episodes_par_tache": 3,
              "juges": [{"nom": "8B", "sert_a_l_appariement": True}, {"nom": "3B", "sert_a_l_appariement": False}]}
    chemin_m, _ = creer_manifeste(depot, RUN, config, ["x"], entropie=ENTROPIE, decisif=True, prereg=str(prereg))
    if etapes == ("aucune",):
        ecrire_resultat(depot, chemin_m, "arret", {"etape": "épisodes", "motif": "garde",
                                                   "partiel": {"taches_sha256": sha}})
        committer(depot)
        return {"taches": f, "prereg": prereg}
    fiches = []
    for i, t in enumerate(taches):
        for k in range(3):
            fiches.append(_fiche(t, k, invalide=(i == 0 and k == 0), vide=(i == 1 and k == 2)))
    ecrire_resultat(depot, chemin_m, "episodes", {"fiches": fiches, "controle_negatif": {"lecture": "conforme"},
                                                  "descriptifs": {"duree_s": 1.0}})
    effets = {t["identifiant"]: rng.normal(0, 1.0) for t in taches}
    bases = {(t["identifiant"], k): _base(rng, effets[t["identifiant"]] + rng.normal(0, 0.5))
             for t in taches for k in range(3)}
    for j, bruit in (("8B", bruit_juge), ("3B", 2 * bruit_juge)):
        for etape, episodes in (("decisives", ((0, 0), (0, 1), (1, 0))), ("descriptives", ((2, 0),))):
            notations = []
            for t in taches:
                for k, passe in episodes:
                    notes = _notes(rng, bases[(t["identifiant"], k)], bruit)
                    reponse = json.dumps(notes) + ("" if bruit == 0 else str(rng.random()))
                    notations.append({"cle": f"juge-{j}/{t['identifiant']}/e{k}/passe-{passe}", "variante": "b0",
                                      "tronquee": False, "notes": notes, "anomalies": [],
                                      "score": score_sur_100(notes), "reponse": reponse, "jetons_reponse": 50})
            if etape == "descriptives" and etapes == ("decisives",):
                continue
            ecrire_resultat(depot, chemin_m, f"notations-{j}-{etape}", {"notations": notations})
    if etapes == ("decisives",):
        ecrire_resultat(depot, chemin_m, "arret", {"etape": "notations descriptives par 8B", "motif": "TERM",
                                                   "partiel": {"taches_sha256": sha}})
        committer(depot)
        return {"taches": f, "prereg": prereg}
    from controle_ia.environnements.lancer_pilote_a import paires_d_appariement, paires_enonce_seul

    par_id = {t["identifiant"]: t for t in taches}
    app = [{"cle": q["cle"], "famille": q["famille"], "p_oui": float(rng.beta(0.6, 0.9)), "masse_oui_non": 0.9}
           for q in paires_d_appariement(fiches, par_id)]
    enonce = [{"cle": q["cle"], "famille": q["famille"], "p_oui": 0.9 if q["cle"].endswith("/C1") else 0.1,
               "masse_oui_non": 0.9} for q in paires_enonce_seul(taches)]
    ecrire_resultat(depot, chemin_m, "appariements", {"juge": "8B", "appariements": app, "enonce_seul": enonce})
    ecrire_resultat(depot, chemin_m, "resume", {"taches_sha256": sha})
    committer(depot)
    return {"taches": f, "prereg": prereg}


def _etiqueter(travail: Path, inverser: float = 0.1, graine: int = 9) -> None:
    """Étiquettes d'un sous-agent simulé : la décision du 8B lue dans l'échantillon scellé, inversée au hasard."""
    rng = np.random.default_rng(graine)
    for d in sorted((travail / ANALYSE).glob("lot-*/tentative-*")):
        paires = json.loads((d / "paires.json").read_text(encoding="utf-8"))
        (d / "etiquettes.json").write_text(json.dumps(
            {q["id"]: ("Yes" if rng.random() < 0.5 else "No") for q in paires}), encoding="utf-8")


def _etiqueter_selon_8b(depot: Path, travail: Path, inverser: float, graine: int = 9) -> None:
    rng = np.random.default_rng(graine)
    ech = json.loads((depot / "diag" / ANALYSE / "echantillon-etiquetage.json").read_text(encoding="utf-8"))
    decision = {x["id"]: x["oui_8b"] for x in ech["resultat"]["elements"]}
    for d in sorted((travail / ANALYSE).glob("lot-*/tentative-*")):
        paires = json.loads((d / "paires.json").read_text(encoding="utf-8"))
        e = {q["id"]: ("Yes" if (decision[q["id"]] != (rng.random() < inverser)) else "No") for q in paires}
        (d / "etiquettes.json").write_text(json.dumps(e), encoding="utf-8")


# --- unités --------------------------------------------------------------------------------------------------

def test_format_strict():
    assert lp.format_strict(_action(1))
    assert not lp.format_strict("Sure! " + _action(1))                       # texte avant
    assert not lp.format_strict(_action(1, cout=None))                       # champ manquant
    assert not lp.format_strict(_action(1) + "\nCOST: 5")                    # champ répété
    assert not lp.format_strict(_action(1).replace("TITLE", "**TITLE**"))    # gras : lu en tolérant, pas strict


def test_lettres_des_episodes():
    assert [lp.lettre("2601.00001v1/e0", 0), lp.lettre("2601.00001v1/e0", 1), lp.lettre("2601.00001v1/e1", 0),
            lp.lettre("2601.00001v1/e2", 0), lp.lettre("2601.00001v1/e3", 0)] == ["A", "B", "C", "D", None]


def test_mesures_format_et_somme_brute():
    t = _taches(2, 0)
    fiches = [_fiche(t[0], 0, invalide=True), _fiche(t[1], 0)]
    m = lp.mesures_format(fiches, 400)
    assert m["actions"] == 4 and m["valides"] == 3 and m["part_valides"] == 0.75
    assert m["completude_cout"] == 1.0 and m["part_cout_lu"] == 1.0 and m["part_plafond"] == 0.0
    assert lp.mesures_format(fiches, 40)["part_plafond"] == 1.0
    with pytest.raises(GardeArret, match="aucune action"):
        lp.mesures_format([_fiche(t[0], 0, vide=True)], 400)
    notes = {nom: hi for nom, lo, hi in CRITERES}
    notes["REDUNDANCY_PENALTY"] = -2
    assert lp.somme_brute({"notes": notes, "score": 1.0}) == 31.0          # somme brute, pénalité comprise
    assert lp.somme_brute({"notes": notes, "score": None}) is None         # incomplète : jamais imputée


def test_retenue_et_statuts():
    k = {"kappa": 0.7, "borne": [0.5, 0.8]}
    assert lp.retenue_famille(0.3, "bas", 0.1, k, True, 50) == "retenue"
    assert lp.retenue_famille(0.05, "bas", 0.1, k, True, 50) == "non retenue"
    assert lp.retenue_famille(0.3, "bas", 0.1, {"kappa": 0.7, "borne": [0.3, 0.8]}, True, 50) == "non retenue"
    assert lp.retenue_famille(0.3, "bas", 0.1, {"kappa": None, "borne": None}, True, 50) == "non concluant"
    assert lp.retenue_famille(0.3, "bas", 0.1, k, False, 50) == "non concluant"
    assert lp.retenue_famille(0.95, "haut", 0.9, k, True, 20, 16) == "non retenue"
    assert lp.retenue_famille(0.5, "haut", 0.9, k, True, 10, 16) == "non concluant"
    assert lp.statut(True, False) == "confirmée" and lp.statut(False, True) == "réfutée"
    assert lp.statut(False, False) == "non concluant" and lp.statut(None, True) == "non concluant"


# --- de bout en bout -------------------------------------------------------------------------------------------

def test_lecture_de_bout_en_bout(depot, tmp_path):
    d = construire(depot)
    travail = tmp_path / "travail"
    r = lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    assert r["lots"] and r["invite"].startswith("This task is self-contained")
    ech = json.loads((depot / "diag" / ANALYSE / "echantillon-etiquetage.json").read_text(encoding="utf-8"))
    el = ech["resultat"]["elements"]
    assert len({x["id"] for x in el}) == len(el) <= 6 * lp.PAR_STRATE
    assert all(len([x for x in el if x["lot"] == lot]) <= lp.TAILLE_LOT_ETIQUETAGE for lot in ech["resultat"]["lots"])
    # rien du texte ni des scores dans les lots remis : ni décision du 8B, ni famille, ni clé
    lot = json.loads((travail / ANALYSE / "lot-01" / "tentative-1" / "paires.json").read_text(encoding="utf-8"))
    assert set(lot[0]) == {"id", "question"} and "Answer with a single word" in lot[0]["question"]
    # l'ordre est mélangé : les strates (décision du 8B) ne se lisent pas dans la position
    assert [x["strate"] for x in el] != sorted([x["strate"] for x in el], key=str)
    committer(depot)
    _etiqueter_selon_8b(depot, travail, inverser=0.1)
    assert lp.lire_etiquetage(depot, ANALYSE, travail)["etiquettes"] == len(el)
    committer(depot)
    lecture = lp.analyser(depot, RUN, ANALYSE, d["taches"])
    assert set(lecture["predictions"]) == {f"P{k}" for k in range(1, 8)}
    assert lecture["format"]["actions"] == 50 * 3 * 2 - 2 and lecture["format"]["ensembles_vides"] == 1
    assert lecture["format_retenu"] is True
    for j in ("8B", "3B"):
        assert lecture["juges"][j]["taches_completes"] == 50
        assert lecture["juges"][j]["plan_b"] in ("plan B", "nœud", "rubrique gardée")
    assert lecture["difference_appariee"]["taches"] == 50
    assert lecture["kappas"]["controls"]["kappa"] is not None and lecture["kappas"]["controls"]["kappa"] > 0.5
    assert lecture["kappas"]["directions"]["n"] == (lecture["kappas"]["fruitful_directions"]["n"]
                                                    + lecture["kappas"]["sterile_directions"]["n"])
    assert lecture["steriles_taches"] == 20
    assert lecture["enonce_seul"]["parts"]["controls"] == pytest.approx(1 / 3)
    assert lecture["cout"]["taches_avec_reference"] == 25
    assert lecture["retenue"]["cout"] == "non retenue"                    # 25 tâches à référence < 32
    assert set(lecture["audit_r4"]) >= {"trop_propre", "trop_sale", "declenche", "familles"}
    assert len(lecture["relectures_audit"]["reponses_de_juge"]) == lp.RELECTURES_AUDIT
    sur_disque = json.loads((depot / "diag" / ANALYSE / "lecture.json").read_text(encoding="utf-8"))
    assert sur_disque["resultat"]["predictions"] == lecture["predictions"]
    # rejouable : mêmes graines, mêmes intervalles
    assert lp.lecture_juge(lp.notes_alignees(_notations(depot, "8B"), "8B", sorted(_ids(d))),
                           _rng(depot, "analyse/bootstrap-parts-8B"))["intervalles"] == \
        lecture["juges"]["8B"]["intervalles"]
    # R12 : une seconde lecture n'écrase rien
    with pytest.raises(GardeArret, match="R12"):
        lp.analyser(depot, RUN, ANALYSE, d["taches"])


def _notations(depot, j):
    r = json.loads((depot / "diag" / RUN / f"notations-{j}-decisives.json").read_text(encoding="utf-8"))
    return r["resultat"]["notations"]


def _ids(d):
    return [t["identifiant"] for t in json.loads(Path(d["taches"]).read_text(encoding="utf-8"))["taches"]]


def _rng(depot, cle):
    from controle_ia.manifeste import generateur
    m = json.loads((depot / "runs" / ANALYSE / "manifeste.json").read_text(encoding="utf-8"))
    return generateur(m["graines"][cle])


def test_audit_trop_propre_sans_bruit_de_juge(depot, tmp_path):
    """R4 : un juge sans bruit (A = B) déclenche l'audit « trop propre »."""
    d = construire(depot, bruit_juge=0.0)
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], tmp_path)
    _etiqueter_selon_8b(depot, tmp_path, inverser=0.1)
    lp.lire_etiquetage(depot, ANALYSE, tmp_path)
    committer(depot)
    lecture = lp.analyser(depot, RUN, ANALYSE, d["taches"])
    assert lecture["audit_r4"]["declenche"]
    assert any("8B" in x for x in lecture["audit_r4"]["trop_propre"])


def test_kappa_d_un_etiqueteur_au_hasard_ne_retient_aucune_famille(depot, tmp_path):
    d = construire(depot)
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], tmp_path)
    _etiqueter(tmp_path)
    lp.lire_etiquetage(depot, ANALYSE, tmp_path)
    committer(depot)
    lecture = lp.analyser(depot, RUN, ANALYSE, d["taches"])
    assert lecture["retenue"]["controls"] in ("non retenue", "non concluant")
    assert lecture["predictions"]["P7"] in ("réfutée", "non concluant")


# --- étiquetage : contrôles et tentatives ---------------------------------------------------------------------

def test_etiquetage_non_conforme_puis_refait(depot, tmp_path):
    d = construire(depot)
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], tmp_path)
    committer(depot)
    with pytest.raises(GardeArret, match="à refaire"):                    # aucune étiquette
        lp.lire_etiquetage(depot, ANALYSE, tmp_path)
    _etiqueter_selon_8b(depot, tmp_path, inverser=0.0)
    lot1 = tmp_path / ANALYSE / "lot-01" / "tentative-1"
    e = json.loads((lot1 / "etiquettes.json").read_text(encoding="utf-8"))
    e[next(iter(e))] = "Maybe"
    (lot1 / "etiquettes.json").write_text(json.dumps(e), encoding="utf-8")
    sortie = subprocess.run(["python3", "-I", "verifier_etiquettes.py"], cwd=lot1, capture_output=True, text=True)
    assert "Yes ou No" in sortie.stdout                                   # le script remis voit la même faute
    with pytest.raises(GardeArret, match="lot-01"):
        lp.lire_etiquetage(depot, ANALYSE, tmp_path)
    with pytest.raises(GardeArret, match="rien à refaire"):
        lp.refaire_lot(depot, ANALYSE, tmp_path, "lot-02")
    consigne = lp.refaire_lot(depot, ANALYSE, tmp_path, "lot-01")
    assert consigne.endswith("lot-01/tentative-2/consigne.txt")
    lot2 = tmp_path / ANALYSE / "lot-01" / "tentative-2"
    (lot2 / "paires.json").write_text("[]\n", encoding="utf-8")         # artefact : paires modifiées
    (lot2 / "etiquettes.json").write_text("{}", encoding="utf-8")
    assert lp.lire_lot(lot2, json.loads((depot / "diag" / ANALYSE / "echantillon-etiquetage.json").read_text(
        encoding="utf-8"))["resultat"]["empreintes_lots"]["lot-01"])[1] == ["paires.json modifié"]
    lp.refaire_lot(depot, ANALYSE, tmp_path, "lot-01")
    with pytest.raises(GardeArret, match="3 tentatives"):
        lp.refaire_lot(depot, ANALYSE, tmp_path, "lot-01")
    lot3 = tmp_path / ANALYSE / "lot-01" / "tentative-3"
    paires = json.loads((lot3 / "paires.json").read_text(encoding="utf-8"))
    (lot3 / "etiquettes.json").write_text(json.dumps({q["id"]: "No" for q in paires}), encoding="utf-8")
    sortie = subprocess.run(["python3", "-I", "verifier_etiquettes.py"], cwd=lot3, capture_output=True, text=True)
    assert sortie.stdout.strip() == "OK"
    assert lp.lire_etiquetage(depot, ANALYSE, tmp_path)["tentatives"]["lot-01"] == 3
    (lot3 / "consigne.txt").write_text("autre consigne", encoding="utf-8")   # artefact : consigne modifiée
    assert "consigne.txt modifié" in lp.lire_lot(lot3, json.loads(
        (depot / "diag" / ANALYSE / "echantillon-etiquetage.json").read_text(encoding="utf-8"))["resultat"][
        "empreintes_lots"]["lot-01"])[1]


# --- gardes d'avant le manifeste d'analyse ---------------------------------------------------------------------

def test_gardes_de_lecture_cas_sain_et_artefacts(depot, tmp_path):
    d = construire(depot)
    # artefact : module de lecture modifié après le commit cité
    m = depot / lp.MODULES_LECTURE[1]
    m.write_text(m.read_text(encoding="utf-8") + "\n# modifié\n", encoding="utf-8")
    committer(depot)
    with pytest.raises(GardeArret, match="modules de lecture modifiés"):
        lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], tmp_path)
    assert not (depot / "runs" / ANALYSE).exists()
    subprocess.run(["git", "-C", str(depot), "revert", "--no-edit", "HEAD"], check=True, capture_output=True)
    # artefact : autre préenregistrement que celui du lancement
    autre = _prereg(depot, _commit(depot), nom="autre.md")
    committer(depot)
    with pytest.raises(GardeArret, match="pas été lancé sous ce préenregistrement"):
        lp.preparer_etiquetage(depot, RUN, ANALYSE, autre, d["taches"], tmp_path)
    # artefact : fichier des tâches différent
    f = depot / "taches-autres.json"
    f.write_text(json.dumps({"taches": _taches(3, 0)}), encoding="utf-8")
    sceller(f)
    committer(depot)
    with pytest.raises(GardeArret, match="tâches .* ≠ tâches du pilote"):
        lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], f, tmp_path)
    # artefact : module de lecture absent
    (depot / lp.MODULES_LECTURE[0]).unlink()
    committer(depot)
    with pytest.raises(GardeArret, match="absents"):
        lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], tmp_path)
    assert not (depot / "runs" / ANALYSE).exists()


def test_constantes_changees_apres_le_manifeste_arretent(depot, tmp_path, monkeypatch):
    d = construire(depot)
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], tmp_path)
    _etiqueter_selon_8b(depot, tmp_path, inverser=0.1)
    lp.lire_etiquetage(depot, ANALYSE, tmp_path)
    committer(depot)
    monkeypatch.setattr(lp, "KAPPA_MIN", 0.5)
    monkeypatch.setattr(lp, "constantes", lambda: {"KAPPA_MIN": 0.5})
    with pytest.raises(GardeArret, match="constantes"):
        lp.analyser(depot, RUN, ANALYSE, d["taches"])


# --- runs partiels -------------------------------------------------------------------------------------------

def test_run_partiel_apres_les_notations_decisives(depot, tmp_path):
    d = construire(depot, etapes=("decisives",))
    r = lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], tmp_path)
    assert r["lots"] == {}
    committer(depot)
    lecture = lp.analyser(depot, RUN, ANALYSE, d["taches"])
    assert lecture["run_partiel"] and "nœud" in lecture["familles"]
    assert lecture["juges"]["8B"]["taches_completes"] == 50                 # décomposition lisible
    assert lecture["predictions"]["P4"] == "non concluant"


def test_run_partiel_pendant_les_episodes(depot, tmp_path):
    d = construire(depot, etapes=("aucune",))
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], tmp_path)
    committer(depot)
    lecture = lp.analyser(depot, RUN, ANALYSE, d["taches"])
    assert lecture["run_partiel"] and "aucune lecture" in lecture["lecture"]
