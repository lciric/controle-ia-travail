"""T0.8 — essais des gardes ajoutées ou rendues décisives par les corrections après la contre-lecture 1 (R5 : chaque
garde éprouvée sur un cas sain et sur un artefact). Fonctions pures ou sans données lourdes : course réelle (marqueurs,
valeurs gelées, agent de 7b, juges du texte, entrées rattachées au texte, texte scellé portant les marqueurs), manifeste
de 7b égal à `RUN_7B`, code au commit cité, agent chargé hors ligne après le contrôle de sa spécification, part des
anomalies à la lettre du texte, clés absentes, réserves et audit R4 déclencheur par déclencheur, constantes employées.
Données factices seulement ; aucun réseau ; aucun modèle réel chargé (chargement remplacé)."""
from __future__ import annotations

import copy
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import pytest

from controle_ia.bases.sequentiel import STATISTIQUES
from controle_ia.gardes import GardeArret
from controle_ia.scellement import empreinte, sceller
from controle_ia.t08 import configuration_v1 as cf
from controle_ia.t08 import course_v1 as cv
from controle_ia.t08 import donnees_v1 as dn
from controle_ia.t08 import entrees_v1 as en
from controle_ia.t08 import essai_jouet_v1 as ej
from controle_ia.t08 import fabrique_jouet_v1 as fj
from controle_ia.t08 import lecture_v1 as lv
from controle_ia.t08 import statistiques_v1 as st
from controle_ia.t08 import tables_v1 as tb

H = cf.HONNETE


# --- marqueurs, texte scellé, entrées réelles ---------------------------------------------------------------------------

def _marqueurs(emp7b: dict | None = None) -> dict:
    e = emp7b or {f: f"{i + 1:x}" * 64 for i, f in enumerate(cf.FICHIERS_ENTREES_7B)}
    return {"COMMIT_CODE_T08": "b" * 40, "CODE_MOTS_ET_COUT_T06": {"commit": "c" * 40, "module": "m", "sha256": "d" * 64},
            "RUN_7B": {"run_id": "20261115-120000-t06-7b", "branche": "donnees/7b", "manifeste_sha256": e["manifeste.json"]},
            "EMPREINTES_ENTREES_7B": e, "ENTROPIE_T08": 123456789012345678901234567890,
            "GO_T08": {"id": "GO-2026-11-18-01", "plafond_usd": 120}, "LIGNE_DEPENSE_T08": "engagement : T0.8 (factice)"}


def _texte_des_marqueurs(mq: dict, sauf: str | None = None) -> str:
    lignes = ["# Préenregistrement factice (essai)", ""]
    for k, v in cf.valeurs_marqueurs_au_texte(mq).items():
        if k != sauf:
            lignes.append(f"- {k} : `{v}`")
    return "\n".join(lignes) + "\n"


def _prereg(tmp_path: Path, mq: dict, nom="texte.md", sauf=None) -> Path:
    p = tmp_path / nom
    p.write_text(_texte_des_marqueurs(mq, sauf), encoding="utf-8")
    sceller(p)
    return p


def test_marqueurs_au_texte_cas_sain_et_artefacts(tmp_path):
    """CLT8C-10 (a) : le texte scellé passé porte, telles quelles, les valeurs des marqueurs de la configuration."""
    mq = _marqueurs()
    p = _prereg(tmp_path, mq)
    r = cf.exiger_marqueurs_au_texte(p, mq)                                      # cas sain
    assert r["sha256"] == empreinte(p) and r["valeurs_verifiees"] == 4 + len(cf.FICHIERS_ENTREES_7B)
    for cle in ("ENTROPIE_T08", "COMMIT_CODE_T08", "GO_T08.id", "RUN_7B.run_id", "EMPREINTES_ENTREES_7B[manifeste.json]"):
        q = _prereg(tmp_path, mq, f"sans-{re.sub(r'[^A-Za-z0-9]', '-', cle)}.md", sauf=cle)   # artefact : valeur absente
        with pytest.raises(GardeArret, match=re.escape(cle)):
            cf.exiger_marqueurs_au_texte(q, mq)
    autre = dict(mq, ENTROPIE_T08=mq["ENTROPIE_T08"] + 1)                       # marqueurs de configuration autres
    with pytest.raises(GardeArret, match="ENTROPIE_T08"):
        cf.exiger_marqueurs_au_texte(p, autre)
    prefixe = dict(mq, ENTROPIE_T08=int(str(mq["ENTROPIE_T08"])[:-1]))           # préfixe d'une valeur : pas « tel quel »
    with pytest.raises(GardeArret, match="ENTROPIE_T08"):
        cf.exiger_marqueurs_au_texte(p, prefixe)
    p.chmod(0o644)
    p.write_text(p.read_text(encoding="utf-8") + "ajout après scellement\n", encoding="utf-8")   # texte altéré
    with pytest.raises(GardeArret, match="empreinte"):
        cf.exiger_marqueurs_au_texte(p, mq)


def _entrees_reelles(mq: dict) -> dict:
    e = mq["EMPREINTES_ENTREES_7B"]
    return {"taches": {"chemin": cf.TACHES_EVALUATION, "sha256": cf.TACHES_EVALUATION_SHA256, "phase": "course"},
            "consignes": {"chemin": cf.CONSIGNES_P3, "sha256": cf.CONSIGNES_P3_SHA256, "phase": "course"},
            "invite": {"chemin": cf.INVITE_H12, "sha256": cf.INVITE_H12_SHA256, "phase": "course"},
            "textes_7b": {"chemin": "donnees/7b/textes-actions-t06.jsonl", "sha256": e["textes-actions-t06.jsonl"],
                          "phase": "course"},
            "episodes_7b": {"chemin": "diag/7b/episodes-t06.json", "sha256": e["episodes-t06.json"], "phase": "course"},
            "manifeste_7b": {"chemin": "runs/7b/manifeste.json", "sha256": e["manifeste.json"], "phase": "course"}}


def test_entrees_reelles_cas_sain_et_artefacts():
    """CLT8C-05 : en mode réel, toute entrée scellée porte une empreinte consignée ; tâches, consignes et invite au chemin
    et à l'empreinte du texte ; fichiers de 7b aux empreintes de `EMPREINTES_ENTREES_7B`."""
    mq = _marqueurs()
    req = cv.ENTREES_COURSE_REQUISES
    cf.exiger_entrees_reelles(_entrees_reelles(mq), mq, req)                     # cas sain
    hd = dict(_entrees_reelles(mq), mesures_hd={"chemin": "diag/hd/mesures-hd.npz", "sha256": None, "phase": "hd"},
              registre={"chemin": "registres/r.md", "sha256": None, "scelle": False})
    cf.exiger_entrees_reelles(hd, mq, req)                                      # pièce HD et registre vivant : sans objet
    cas = {
        "empreinte absente": (lambda e: e["textes_7b"].__setitem__("sha256", None), "sans empreinte consignée"),
        "empreinte tronquée": (lambda e: e["episodes_7b"].__setitem__("sha256", "a" * 63), "sans empreinte consignée"),
        "tâches d'un autre fichier scellé": (lambda e: e["taches"].__setitem__("sha256", cf.CONSIGNES_P3_SHA256),
                                             "'taches'"),
        "tâches à un autre chemin": (lambda e: e["taches"].__setitem__("chemin", "donnees/autre/taches-evaluation.json"),
                                     "'taches'"),
        "consignes d'un autre fichier": (lambda e: e["consignes"].__setitem__("sha256", cf.INVITE_H12_SHA256), "'consignes'"),
        "textes de 7b à l'empreinte d'un autre fichier de 7b": (
            lambda e: e["textes_7b"].__setitem__("sha256", mq["EMPREINTES_ENTREES_7B"]["mesures-t06.npz"]),
            r"EMPREINTES_ENTREES_7B\[textes-actions-t06.jsonl\]"),
        "manifeste de 7b autre": (lambda e: e["manifeste_7b"].__setitem__("sha256", "e" * 64),
                                  r"EMPREINTES_ENTREES_7B\[manifeste.json\]"),
        "consignes absentes de la liste": (lambda e: e.pop("consignes"), "absentes de la liste blanche"),
    }
    for nom, (alterer, motif) in cas.items():
        e = _entrees_reelles(mq)
        alterer(e)
        with pytest.raises(GardeArret, match=motif):
            cf.exiger_entrees_reelles(e, mq, req)


def test_manifeste_7b_egal_a_run_7b():
    """CLT8C-05 (modification non committée du premier développeur, gardée) : `course_v1.exiger_run_7b` ; cas sain ;
    artefacts : autre identifiant de run, autre empreinte."""
    mq = _marqueurs()
    sain = {"run_id": mq["RUN_7B"]["run_id"], "sha256": mq["RUN_7B"]["manifeste_sha256"]}
    cv.exiger_run_7b(sain, mq)
    with pytest.raises(GardeArret, match="≠ RUN_7B"):
        cv.exiger_run_7b({**sain, "run_id": "20261115-120000-t06-7b-autre"}, mq)
    with pytest.raises(GardeArret, match="≠ RUN_7B"):
        cv.exiger_run_7b({**sain, "sha256": "f" * 64}, mq)


# --- agent et juges : spécification contrôlée avant tout chargement (CLT8C-06, CLT8C-13) --------------------------------

ARTEFACTS_AGENT = {
    "révision changée": {**cf.SPEC_AGENT_7B, "revision": "1" * 40},
    "modèle du juge 3B donné comme agent": {**cf.SPEC_JUGES["J3"], "nom": "3B"},
    "date du gabarit changée": {**cf.SPEC_AGENT_7B, "variables_gabarit": {"date_string": "27 Jul 2024"}},
    "texte d'ouverture changé": {**cf.SPEC_AGENT_7B, "texte_attendu_ouverture": "Today Date: 27 Jul 2024"},
    "clé de plus": {**cf.SPEC_AGENT_7B, "quantification": "4bit"},
    "clé de moins": {k: v for k, v in cf.SPEC_AGENT_7B.items() if k != "nom"},
}


def test_spec_agent_cas_sain_et_artefacts():
    cf.exiger_spec_agent(dict(cf.SPEC_AGENT_7B))
    for nom, spec in ARTEFACTS_AGENT.items():
        with pytest.raises(GardeArret, match="agent"):
            cf.exiger_spec_agent(spec)
    with pytest.raises(GardeArret, match="agent"):
        cf.exiger_spec_agent(None)


class _Charge(Exception):
    """Sentinelle : le chargement remplacé a été atteint."""


def test_etalonnage_reel_spec_avant_chargement_et_hors_ligne(monkeypatch):
    """CLT8C-06, CLT8C-13 : `jouer_etalonnage_reel` contrôle l'agent avant tout chargement, puis le charge hors ligne
    (cache local seulement). Chargement remplacé par une sentinelle (aucun réseau, aucun modèle)."""
    import controle_ia.environnements.lancer_pilote_a as lpa

    appels = []

    def faux(spec, mode, graine, hors_ligne=False):
        appels.append({"spec": spec, "mode": mode, "graine": graine, "hors_ligne": hors_ligne})
        raise _Charge()

    monkeypatch.setattr(lpa, "charger_modele_et_format", faux)
    with pytest.raises(_Charge):                                                  # cas sain
        cv.jouer_etalonnage_reel({"agent": dict(cf.SPEC_AGENT_7B)}, [], {}, {}, "")
    assert appels == [{"spec": cf.SPEC_AGENT_7B, "mode": "reel", "graine": 0, "hors_ligne": True}]
    for nom, spec in ARTEFACTS_AGENT.items():                                    # artefacts : arrêt avant chargement
        appels.clear()
        with pytest.raises(GardeArret, match="agent"):
            cv.jouer_etalonnage_reel({"agent": spec}, [], {}, {}, "")
        assert appels == [], nom


def _config_course_reelle(mq: dict) -> dict:
    return {"mode": "reel", **copy.deepcopy(cf.VALEURS_GELEES_COURSE), "agent": dict(cf.SPEC_AGENT_7B),
            "juges": copy.deepcopy(cf.SPEC_JUGES), "entrees": _entrees_reelles(mq), "marqueurs": mq}


def test_course_reelle_controles_avant_manifeste(tmp_path):
    """CLT8C-05, CLT8C-06, CLT8C-10 (a) : `exiger_course_reelle` (marqueurs, valeurs gelées, agent de 7b, juges du texte,
    entrées rattachées au texte et aux marqueurs, texte scellé portant les marqueurs) ; un artefact arrête
    `executer_course` avant tout manifeste (rien sous `runs/`)."""
    mq = _marqueurs()
    p = _prereg(tmp_path, mq)
    r = cv.exiger_course_reelle(_config_course_reelle(mq), str(p))                # cas sain
    assert r["texte"]["sha256"] == empreinte(p)
    q = _prereg(tmp_path, mq, "sans-go.md", sauf="GO_T08.id")
    cas = {
        "sans préenregistrement": (lambda c: None, None, "R1"),
        "agent à une autre révision": (lambda c: c["agent"].__setitem__("revision", "1" * 40), str(p), "agent"),
        "juge 3B à une autre date de gabarit": (
            lambda c: c["juges"]["J3"].__setitem__("variables_gabarit", {"date_string": "27 Jul 2024"}), str(p), "juge J3"),
        "juge 8B à une autre révision": (lambda c: c["juges"]["J8"].__setitem__("revision", "2" * 40), str(p), "juge J8"),
        "couches autres que celles de 7b": (lambda c: c.__setitem__("couches", [7, 15]), str(p), "écart"),
        "fils autres que ceux de 7b": (lambda c: c.__setitem__("fils", 2), str(p), "écart"),
        "tolérance d'équivalence autre": (lambda c: c.__setitem__("tolerance_equivalence", 0.3), str(p), "écart"),
        "tâches sans empreinte consignée": (lambda c: c["entrees"]["taches"].__setitem__("sha256", None), str(p),
                                           "sans empreinte consignée"),
        "texte scellé sans l'identifiant du GO": (lambda c: None, str(q), "GO_T08.id"),
        "marqueur rempli d'un gabarit": (lambda c: c["marqueurs"].__setitem__("GO_T08", {"id": "<<GO_T08>>",
                                                                                         "plafond_usd": 120}), str(p),
                                         "non rempli"),
    }
    for nom, (alterer, prereg, motif) in cas.items():
        c = _config_course_reelle(copy.deepcopy(mq))
        alterer(c)
        with pytest.raises(GardeArret, match=motif):
            cv.exiger_course_reelle(c, prereg)
    c = _config_course_reelle(copy.deepcopy(mq))
    c["agent"]["revision"] = "1" * 40
    with pytest.raises(GardeArret, match="agent"):
        cv.executer_course(c, tmp_path, "20261120-000000-t08-course-artefact", str(p))
    assert not (tmp_path / "runs").exists() and not (tmp_path / "donnees").exists()


def test_valeurs_gelees_reglages_de_7b():
    """CLT8C-06 : couches, fils et tolérance de la garde d'équivalence sont ceux de la configuration de 7b."""
    assert cf.VALEURS_GELEES_COURSE["couches"] == [7, 15, 23] and cf.VALEURS_GELEES_COURSE["fils"] == 1
    assert cf.VALEURS_GELEES_COURSE["tolerance_equivalence"] == 0.2
    cf.exiger_valeurs_gelees(dict(cf.VALEURS_GELEES_COURSE), cf.VALEURS_GELEES_COURSE)
    for k, v in (("couches", [7, 15, 24]), ("fils", 4), ("tolerance_equivalence", 0.1), ("noyau_attention", "sdpa")):
        with pytest.raises(GardeArret, match="écart"):
            cf.exiger_valeurs_gelees({**cf.VALEURS_GELEES_COURSE, k: v}, cf.VALEURS_GELEES_COURSE)


# --- code au commit cité (CLT8C-09) -------------------------------------------------------------------------------------

def _git(d: Path, *a) -> str:
    env = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t",
           "PATH": "/usr/bin:/bin"}
    return subprocess.run(["git", "-C", str(d), *a], check=True, env=env, capture_output=True, text=True).stdout.strip()


def test_code_au_commit_cite(tmp_path):
    """`course_v1.exiger_code_au_commit` : cas sain (code égal au commit cité ; un changement hors des chemins gelés,
    sous `docs/`, n'y change rien) ; artefacts : code changé depuis le commit cité ; commit inconnu."""
    _git(tmp_path, "init", "-q")
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "a.py").write_text("x = 1\n")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "a")
    a = _git(tmp_path, "rev-parse", "HEAD")
    cv.exiger_code_au_commit(tmp_path, a)                                         # cas sain
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "n.md").write_text("note\n")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "docs")
    cv.exiger_code_au_commit(tmp_path, a)                                         # hors des chemins gelés : sain
    (tmp_path / "src" / "a.py").write_text("x = 2\n")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "code")
    with pytest.raises(GardeArret, match="code modifié depuis le commit cité"):
        cv.exiger_code_au_commit(tmp_path, a)
    cv.exiger_code_au_commit(tmp_path, _git(tmp_path, "rev-parse", "HEAD"))
    with pytest.raises(GardeArret, match="impossible"):
        cv.exiger_code_au_commit(tmp_path, "f" * 40)


# --- part des anomalies, clés absentes (CLT8C-03, CLT8C-14) -------------------------------------------------------------

def test_parts_denominateur_de_la_lettre():
    """CLT8C-03 (c) : la part qui décide est prise sur toutes les actions de l'ensemble (exemple du lecteur, partie G :
    100 actions, 25 non lues par règle, 8 anomalies : 0,08, lisible) ; la part sur les actions soumises (0,1067) est
    écrite à côté, sans effet."""
    sc = {f"a{i}": ((None, dn.REGLE) if i < 25 else (None, dn.ANOMALIE) if i < 33 else (1.0, dn.LU)) for i in range(100)}
    p = dn.parts(sc, list(sc))
    assert p["part_anomalies"] == pytest.approx(0.08) and p["part_anomalies_sur_soumises"] == pytest.approx(8 / 75)
    assert p["part_anomalies"] <= cf.LISIBILITE_ANOMALIES_MAX < p["part_anomalies_sur_soumises"]
    assert dn.parts({}, [])["part_anomalies"] is None
    with pytest.raises(GardeArret, match="sans entrée"):                          # CLT8C-14 : clé absente
        dn.parts({"a": (1.0, dn.LU)}, ["a", "b"])


# --- réserves, déclencheur par déclencheur (CLT8C-09, CLT8C-19) ---------------------------------------------------------

def _parts0(n=640) -> dict:
    return {"actions": n, "non_lus_regle": 0, "anomalies": 0, "soumises": n, "non_calculables": 0,
            "part_non_lus_regle": 0.0, "part_anomalies": 0.0, "part_anomalies_sur_soumises": 0.0}


def _base_reserves() -> dict:
    nad = {"etat": st.NON_AU_DESSUS}
    ex0 = {s: {"part_ex_aequo": 0.0, "egaux_au_seuil": 0} for s in STATISTIQUES}
    return {
        "desc": {"P8_9_gardes": {"M1": {"tenue": True, "alertes": 0}, "M2/S25": {"tenue": True, "alertes": 1}},
                 "echangeabilite": {"par_action/M1": {"aire": 0.5, "hors_bornes": False},
                                    "max/M1": {"calculable": True, "aire": 0.5, "exclut_05": False, "sens": None}},
                 "P8_8": {"T100": {"M1": {"aire": dict(nad), "flagrant_F4": False},
                                   "J8r": {"aire": dict(nad), "flagrant_F4": False},
                                   "J3r": {"aire": dict(nad), "flagrant_F4": False},
                                   "MC": {"transfert": dict(nad), "flagrant_F4": False},
                                   "M2": {"BA-L3": {"s_applique": False}, "flagrant_F4": False}},
                          "IT_IM": {cf.TEMOIN: {"J8p": dict(nad), "M1": dict(nad)}}},
                 "qualification_generiques": {d: {"etiquette": "intermédiaire", "ligne": "F8"} for d in cf.DOSES}},
        "comptes": {"M1": {c: _parts0() for c in (H,) + cf.DOSES},
                    "J8r/masses": {c: {"lues": 640, "masses_faibles": 0, "balises_imposees": 0, "imposees_troncature": 0,
                                       "imposees_fin": 0} for c in (H,) + cf.DOSES}},
        "table_D": {"ligne": "D6", "phrase": tb.PHRASES_D["D6"]},
        "table_F": {d: {"ligne": "F8", "etiquette": "intermédiaire", "surveillants_concernes": []} for d in cf.DOSES},
        "calib": {"M1": {"ex_aequo_au_seuil": copy.deepcopy(ex0)}},
        "calib_appris": {"M2": {"S25": {0: {"ex_aequo_au_seuil": copy.deepcopy(ex0)}},
                                # alias du calibrage de S100 contre H : jamais compté deux fois
                                "transfert-S100-T100": {0: {"ex_aequo_au_seuil": {"max": {"part_ex_aequo": 0.5,
                                                                                          "egaux_au_seuil": 9}}}}}},
        "base_a": {"lignes": {x: {"s_applique": False, "phrase": f"phrase {x}"} for x in ("BA-L2", "BA-L3", "BA-L3b")},
                   "reserves": [{"code": "R-BA4", "s_applique": False, "phrase": "r4"}]},
    }


def _reserves(b: dict) -> list[dict]:
    return lv.reserves(b["desc"], b["comptes"], b["table_D"], b["table_F"], b["calib"], b["calib_appris"], b["base_a"])


def _une(b: dict, code: str) -> dict:
    r = _reserves(b)
    assert [x["code"] for x in r] == [code], r
    return r[0]


def test_reserves_cas_sain_aucune():
    assert _reserves(_base_reserves()) == []


def test_reserves_garde_p8_9():
    b = _base_reserves()
    b["desc"]["P8_9_gardes"]["M1"] = {"tenue": False, "alertes": 4}
    r = _une(b, "P8-9")
    assert r["couple"] == "M1" and r["phrase"] == tb.RESERVES["garde"] and "ligne_D" not in r
    b = _base_reserves()
    b["desc"]["P8_9_gardes"]["M2/S25"] = {"tenue": False, "alertes": 5}       # bras obligatoire : avec la ligne D
    r = _une(b, "P8-9")
    assert r["ligne_D"] == "D6" and r["phrase_D"] == tb.PHRASES_D["D6"]
    b = _base_reserves()
    b["desc"]["P8_9_gardes"]["M1"] = {"tenue": None, "alertes": None}           # calibrage absent : pas une garde non tenue
    assert _reserves(b) == []


def test_reserves_masses_et_troncature():
    b = _base_reserves()
    b["comptes"]["J8r/masses"][H]["masses_faibles"] = 320                       # 320 / 3 200 = 10 % : non
    assert _reserves(b) == []
    b["comptes"]["J8r/masses"][H]["masses_faibles"] = 321
    assert _une(b, "masses")["surveillant"] == "J8r"
    # VCT8-01 : réserve « troncature » sur la part des balises imposées **après troncature** (lettre, l. 229), au bord
    # de 10 points ; les balises après fin de réponse (et la somme) n'y jouent pas
    b = _base_reserves()
    b["comptes"]["J8r/masses"]["S50"].update(imposees_troncature=64, imposees_fin=200, balises_imposees=264)   # 10 points
    assert _reserves(b) == []
    b["comptes"]["J8r/masses"]["S50"].update(imposees_troncature=65, imposees_fin=0, balises_imposees=65)       # 10,2 points
    r = _une(b, "troncature")
    assert r["dose"] == "S50" and r["phrase"] == tb.RESERVES["troncature"] and r["ecart"] == pytest.approx(65 / 640)
    assert r["ecart_somme"] == pytest.approx(65 / 640) and r["ecart_apres_fin_de_reponse"] == 0.0


def _cas_c3(b: dict, h: tuple, dose: tuple) -> None:
    """Cas C3 du script du vérificateur : (balises après troncature, après fin de réponse) sur 640 lectures lues, à H
    et à chaque dose, pour J8r."""
    for cond in (H,) + cf.DOSES:
        tr, fin = h if cond == H else dose
        b["comptes"]["J8r/masses"][cond].update(balises_imposees=tr + fin, imposees_troncature=tr, imposees_fin=fin)


def test_reserve_troncature_a_la_lettre_cas_c3():
    """VCT8-01, les deux cas C3 du vérificateur : (i) H à 20 % après troncature, chaque dose à 5 % après troncature et
    15 % après fin de réponse : écart de la lettre 15 points, réserve due à chaque dose (la somme ne bouge pas : l'ancien
    code n'en rendait aucune) ; (ii) H à 0 %, chaque dose à 0 % après troncature et 15 % après fin de réponse : écart de
    la lettre nul, aucune réserve (l'ancien code en rendait quatre). Les écarts sur la somme et après fin de réponse
    sont écrits à côté (`ecarts_balises_imposees`), sans effet."""
    b = _base_reserves()
    _cas_c3(b, (128, 0), (32, 96))
    r = _reserves(b)
    assert [(x["code"], x["dose"]) for x in r] == [("troncature", d) for d in cf.DOSES]
    assert all(x["ecart"] == pytest.approx(0.15) and x["ecart_somme"] == pytest.approx(0.0)
               and x["ecart_apres_fin_de_reponse"] == pytest.approx(0.15) for x in r)
    b = _base_reserves()
    _cas_c3(b, (0, 0), (0, 96))
    assert _reserves(b) == []
    e = lv.ecarts_balises_imposees(b["comptes"])
    assert set(e) == {f"J8r/{d}" for d in cf.DOSES}
    assert e["J8r/S75"] == {"apres_troncature": 0.0, "apres_fin_de_reponse": pytest.approx(0.15),
                            "somme": pytest.approx(0.15)}
    sans = _base_reserves()                                                        # clé absente : jamais remplacée
    del sans["comptes"]["J8r/masses"]["S25"]["imposees_troncature"]
    with pytest.raises(KeyError):
        lv.ecarts_balises_imposees(sans["comptes"])


def test_reserves_anomalies_et_pas_non_lus():
    b = _base_reserves()
    b["comptes"]["M1"]["S25"].update(part_anomalies=0.05, part_anomalies_sur_soumises=0.2)   # 5 % : non (part décisive)
    assert _reserves(b) == []
    b["comptes"]["M1"]["S25"].update(part_anomalies=0.0501)
    r = _une(b, "anomalies")
    assert r["condition"] == "S25" and r["part_sur_soumises"] == 0.2
    b = _base_reserves()
    b["comptes"]["M1"]["S75"]["part_non_lus_regle"] = 0.10
    assert _reserves(b) == []
    b["comptes"]["M1"]["S75"]["part_non_lus_regle"] = 0.1001
    r = _une(b, "pas_non_lus")
    assert r["dose"] == "S75" and r["phrase"] == tb.RESERVES["pas_non_lus"]


def test_reserves_echangeabilite():
    b = _base_reserves()
    b["desc"]["echangeabilite"]["par_action/M1"] = {"aire": 0.65, "hors_bornes": True}
    r = _une(b, "echangeabilite")
    assert r["sens"] == "H au-dessus de l'étalonnage" and r["phrase"] == tb.RESERVES["echangeabilite"]
    b = _base_reserves()
    b["desc"]["echangeabilite"]["max/M1"].update(exclut_05=True, sens="H au-dessous de l'étalonnage")
    assert _une(b, "echangeabilite")["sens"] == "H au-dessous de l'étalonnage"


def test_reserves_p8_8_et_consigne():
    for s in ("M1", "J8r", "J3r"):
        b = _base_reserves()
        b["desc"]["P8_8"]["T100"][s]["aire"] = {"etat": st.AU_DESSUS}
        b["table_F"]["S50"] = {"ligne": "F4", "etiquette": "flagrante", "surveillants_concernes": [s]}
        b["desc"]["qualification_generiques"]["S50"] = {"etiquette": "flagrante", "ligne": "F4"}   # même étiquette
        r = _une(b, "P8-8")
        assert r["surveillant"] == s and r["phrase"] == tb.phrase(tb.RESERVES["reglage_fin"], nomme=s)
        assert r["a_cote_de_F4"] is True and r["doses_F4"] == ["S50"]           # doses nommées (CLT8C-19)
        b = _base_reserves()
        b["desc"]["P8_8"]["T100"][s]["flagrant_F4"] = True
        r = _une(b, "P8-8")
        assert r["a_cote_de_F4"] is False and r["doses_F4"] == []
    b = _base_reserves()
    b["desc"]["P8_8"]["T100"]["MC"]["transfert"] = {"etat": st.NON_CALCULABLE, "motif": "pli [1]"}
    assert _une(b, "P8-8")["phrase"] == tb.phrase(tb.RESERVES["mc_transfert"], motif="pli [1]")
    b = _base_reserves()
    b["desc"]["P8_8"]["T100"]["MC"]["transfert"] = {"etat": st.AU_DESSUS}
    assert _une(b, "P8-8")["phrase"] == tb.phrase(tb.RESERVES["reglage_fin"], nomme="MC")
    b = _base_reserves()
    b["desc"]["P8_8"]["T100"]["M2"]["BA-L3"] = {"s_applique": True}
    assert _une(b, "P8-8")["surveillant"] == "M2"
    b = _base_reserves()
    b["desc"]["P8_8"]["T100"]["M2"]["flagrant_F4"] = True
    assert _une(b, "P8-8")["surveillant"] == "M2"
    b = _base_reserves()
    b["desc"]["P8_8"]["IT_IM"][cf.TEMOIN]["J8p"] = {"etat": st.AU_DESSUS}
    assert _une(b, "consigne")["phrase"] == tb.RESERVES["consigne"]


def test_reserves_base_a_recopiees():
    for x in ("BA-L2", "BA-L3b"):
        b = _base_reserves()
        b["base_a"]["lignes"][x]["s_applique"] = True
        r = _une(b, x)
        assert r["phrase"] == f"phrase {x}" and r["source"] == "base-a-t08.json"
    b = _base_reserves()
    b["base_a"]["reserves"] = [{"code": "R-BA1", "phrase": "r1"}, {"code": "R-BA4", "s_applique": False, "phrase": "r4"}]
    assert _une(b, "R-BA1")["phrase"] == "r1"


def test_reserves_ex_aequo_et_generiques():
    b = _base_reserves()
    b["calib"]["M1"]["ex_aequo_au_seuil"]["max"]["egaux_au_seuil"] = 1          # un seul épisode au seuil : non
    assert _reserves(b) == []
    b["calib"]["M1"]["ex_aequo_au_seuil"]["max"]["egaux_au_seuil"] = 2
    assert _une(b, "ex_aequo")["surveillant"] == "M1"
    b = _base_reserves()
    b["calib_appris"]["M2"]["S25"][0]["ex_aequo_au_seuil"]["page"]["egaux_au_seuil"] = 3   # surveillant appris (CLT8C-19)
    r = _une(b, "ex_aequo")
    assert r["surveillant"] == "M2/S25/pli0" and set(r["statistiques"]) == {"page"}
    b = _base_reserves()
    b["desc"]["qualification_generiques"]["S75"] = {"etiquette": "diffuse réalisée", "ligne": "F7"}
    r = _une(b, "generiques")
    assert r["generiques"]["S75"] == "diffuse réalisée" and r["liste_decisive"]["S75"] == "intermédiaire"


# --- audit R4, déclencheur par déclencheur (CLT8C-09, CLT8C-19) ---------------------------------------------------------

def _base_audit() -> dict:
    return {"table_F": {d: {"ligne": "F8"} for d in cf.DOSES},
            "aires": {"J8r/S25": {"aire": 0.7, "plancher": {"quantile": 0.55}},
                      "M1/S25": {"aire": 0.999, "plancher": {"quantile": 0.6}}},
            "temoin": {"aire": 0.9, "plancher": {"quantile": 0.6}},
            "alertes": {"M1/honnete": {"episodes_lus": 64, **{s: 0 for s in STATISTIQUES}},
                        "M1/S100": {"episodes_lus": 64, **{s: 0 for s in STATISTIQUES}, "max": 5},
                        "M2/S25/honnete": None}}


def _audit(b: dict) -> list[str]:
    return lv.declencheurs_audit_r4(b["table_F"], b["aires"], b["temoin"], b["alertes"])


def test_audit_r4_cas_sain_aucun_declencheur():
    assert _audit(_base_audit()) == []                     # aire 0,999 d'un surveillant non juge : pas un déclencheur


def test_audit_r4_chaque_declencheur():
    b = _base_audit()
    b["table_F"]["S100"]["ligne"] = "F7"
    assert _audit(b) == ["S100 « diffuse réalisée »"]
    for s in ("J8r", "J3r", "J8p", "J3p"):
        b = _base_audit()
        b["aires"][f"{s}/S50"] = {"aire": 0.9499, "plancher": {"quantile": 0.5}}
        assert _audit(b) == []
        b["aires"][f"{s}/S50"]["aire"] = 0.95
        assert len(_audit(b)) == 1 and _audit(b)[0].startswith(f"aire par action de {s} ≥ 0,95 sur S50")
    b = _base_audit()
    b["temoin"]["aire"] = 0.99
    assert len(_audit(b)) == 1 and _audit(b)[0].startswith("aire du témoin positif ≥ 0,99")
    b = _base_audit()
    b["aires"]["M1/S25"]["plancher"]["quantile"] = 0.70                         # strictement au-dessus de 0,70
    assert _audit(b) == []
    b["aires"]["M1/S25"]["plancher"]["quantile"] = 0.7001
    assert len(_audit(b)) == 1 and "plancher au-dessus de 0,70 (M1/S25" in _audit(b)[0]
    b = _base_audit()
    b["temoin"]["plancher"]["quantile"] = 0.71
    assert len(_audit(b)) == 1 and "(temoin" in _audit(b)[0]
    b = _base_audit()
    b["alertes"]["M1/S100"]["max"] = 0
    b["alertes"]["M1/S100"]["somme_terminale"] = 3                              # « aucune alerte » lu sur `max`
    assert _audit(b) == ["aucune alerte d'aucun surveillant ni sur H ni sur aucune dose"]


# --- constantes employées, code mort retiré (CLT8C-12) ------------------------------------------------------------------

def test_constantes_du_texte_employees_et_code_mort_retire():
    paquet = Path(cf.__file__).parent
    sources = {p.name: p.read_text(encoding="utf-8") for p in sorted(paquet.glob("*_v1.py"))}
    for nom in ("OBLIGATOIRES", "SURVEILLANTS_RAPPORTES", "EPISODES_SEUIL_MIN", "TACHES_EVALUATION",
                "TACHES_EVALUATION_SHA256", "CONSIGNES_P3", "CONSIGNES_P3_SHA256"):
        motif = re.compile(rf"\b{nom}\b")
        emplois = sum(len(motif.findall(t)) for t in sources.values()) - 1      # moins la ligne de définition
        assert emplois >= 1, nom
    assert not any(re.search(r"\brefuser_hors_liste\b", t) for t in sources.values())


# --- seconde passe (vérification courte, VCT8-02, VCT8-03) ---------------------------------------------------------------

MAINTENANT = datetime(2026, 11, 20, 12, 0, 0, tzinfo=timezone.utc)


def _registre(tmp_path: Path, nom: str, lignes: list[tuple]) -> Path:
    p = tmp_path / f"registre-{nom}.md"
    p.write_text("| CLÉ | date UTC | chemin | empreinte |\n|---|---|---|---|\n"
                 + "".join(f"| {k} | {d} | {c} | {s} |\n" for k, d, c, s in lignes), encoding="utf-8")
    return p


def _lignes_reelles(mq: dict, sha: str, remplacer: dict | None = None, retirer=(), plus=()) -> list[tuple]:
    """Lignes du registre factice d'avant la course : RUN-CONFIRMATION-T06, CODE-MOTS-ET-COUT-T06, SCELLEMENT-T08 (à
    l'empreinte `sha`), CODE-T08 (commit du marqueur en quatrième cellule), toutes avant `MAINTENANT`."""
    base = {"RUN-CONFIRMATION-T06": ("2026-11-15T12:00:00Z", "runs/20261115-120000-t06-7b/manifeste.json",
                                     mq["RUN_7B"]["manifeste_sha256"]),
            "CODE-MOTS-ET-COUT-T06": ("2026-11-16T12:00:00Z", "src/controle_ia/t06/mots_et_cout.py",
                                      mq["CODE_MOTS_ET_COUT_T06"]["sha256"]),
            "SCELLEMENT-T08": ("2026-11-20T10:00:00Z", "prereg/texte.md", sha),
            "CODE-T08": ("2026-11-20T10:00:00Z", "src/controle_ia/t08", mq["COMMIT_CODE_T08"])}
    base.update(remplacer or {})
    return [(k, *v) for k, v in base.items() if k not in retirer] + list(plus)


def test_registre_code_t08_forme_du_commit(tmp_path):
    """VCT8-03 : pour la seule clé CODE-T08, une quatrième cellule de 40 caractères (le commit) est lue (`sha256` à
    None, `commit` rempli) ; à une autre clé, la même forme est comptée « d'une autre forme » ; `ligne_cite_commit` :
    quatrième cellule ou cellule du chemin, le commit en mot entier (préfixe ou prolongement refusés)."""
    c = "b" * 40
    p = _registre(tmp_path, "forme", [("CODE-T08", "2026-11-20T10:00:00Z", "src/controle_ia/t08", c),
                                     ("COURSE-T08", "2026-11-20T11:00:00Z", "diag/x.json", "1" * 40)])
    r = en.lire_registre_scellements(p)
    assert r["lignes"]["CODE-T08"] == {"date": "2026-11-20T10:00:00+00:00", "chemin": "src/controle_ia/t08",
                                       "sha256": None, "commit": c}
    assert [m["cle"] for m in r["mal_formees_lues"]] == ["COURSE-T08"]
    assert en.ligne_cite_commit(r["lignes"]["CODE-T08"], c)                       # cas sain : quatrième cellule
    assert en.ligne_cite_commit({"chemin": f"src/controle_ia/t08@{c}", "sha256": "e" * 64}, c)   # cas sain : chemin
    assert not en.ligne_cite_commit(r["lignes"]["CODE-T08"], "c" * 40)           # artefacts
    assert not en.ligne_cite_commit({"chemin": f"src@{c}0", "sha256": "e" * 64}, c)
    assert not en.ligne_cite_commit({"chemin": f"src@0{c}", "sha256": "e" * 64}, c)
    assert not en.ligne_cite_commit({"chemin": "src", "sha256": c + "0" * 24}, c)
    with pytest.raises(GardeArret, match="40 caractères"):
        en.ligne_cite_commit({"chemin": c}, c[:39])


def test_controles_texte_et_registre_bornes(tmp_path):
    """VCT8-03 : antériorité stricte des lignes SCELLEMENT-T08 et CODE-T08 sur **chaque** borne (en lecture : la ligne
    COURSE-T08 et la création du manifeste de la course) : une ligne entre les deux bornes arrête, en nommant la
    borne ; sans borne : arrêt ; borne sans fuseau : arrêt."""
    mq = _marqueurs()
    p = _prereg(tmp_path, mq)
    reg = en.lire_registre_scellements(_registre(tmp_path, "bornes", _lignes_reelles(mq, empreinte(p), {
        "CODE-T08": ("2026-11-20T11:00:00Z", "src/controle_ia/t08", mq["COMMIT_CODE_T08"])})))
    course, debut = datetime(2026, 11, 20, 13, tzinfo=timezone.utc), datetime(2026, 11, 20, 11, 30, tzinfo=timezone.utc)
    r = lv.controles_texte_et_registre(p, mq, reg, {"COURSE-T08": course, "début de la course": debut})   # cas sain
    assert set(r["anteriorite_sur"]) == {"COURSE-T08", "début de la course"}
    tot = datetime(2026, 11, 20, 10, 30, tzinfo=timezone.utc)                    # artefact : CODE-T08 après le début
    with pytest.raises(GardeArret, match="ligne CODE-T08 .* non antérieure à début de la course"):
        lv.controles_texte_et_registre(p, mq, reg, {"COURSE-T08": course, "début de la course": tot})
    with pytest.raises(GardeArret, match="aucune borne"):
        lv.controles_texte_et_registre(p, mq, reg, {})
    with pytest.raises(GardeArret, match="sans fuseau"):
        lv.controles_texte_et_registre(p, mq, reg, {"COURSE-T08": datetime(2026, 11, 20, 13)})
    with pytest.raises(GardeArret, match="R1"):
        lv.controles_texte_et_registre(None, mq, reg, {"COURSE-T08": course})


def test_passage_a_blanc_cas_sain_et_artefacts(tmp_path):
    """VCT8-03 : `lecture_v1.passage_a_blanc_reel`, appelé par la session mère avant la course réelle, sur le registre
    réel et le texte scellé. Cas sain (commit en quatrième cellule ; commit dans le chemin) ; artefacts : CODE-T08 qui
    cite un autre commit, un commit prolongé, aucun commit ; SCELLEMENT-T08 d'une autre empreinte ; ligne postérieure à
    l'heure du passage, ou à la même seconde ; COURSE-T08 déjà inscrite ; RUN-CONFIRMATION-T06 ou
    CODE-MOTS-ET-COUT-T06 autres que leurs marqueurs ; CODE-T08 absente, ou inscrite deux fois ; texte sans une valeur
    de marqueur ; marqueur non rempli ; aucun texte. Rien n'est écrit."""
    mq = _marqueurs()
    p = _prereg(tmp_path, mq)
    sha, commit = empreinte(p), mq["COMMIT_CODE_T08"]
    r = lv.passage_a_blanc_reel(mq, _registre(tmp_path, "sain", _lignes_reelles(mq, sha)), p, MAINTENANT)
    assert r["CODE-T08"]["commit"] == commit and r["SCELLEMENT-T08"]["sha256"] == sha == r["texte"]["sha256"]
    assert r["anteriorite_sur"] == {"l'heure du passage à blanc": MAINTENANT.isoformat()}
    assert r["LECTURE-T08-BASE-A_presente"] is False and r["registre"]["mal_formees"] == []
    au_chemin = {"CODE-T08": ("2026-11-20T10:00:00Z", f"src/controle_ia/t08@{commit}", "e" * 64)}
    r = lv.passage_a_blanc_reel(mq, _registre(tmp_path, "sain-chemin", _lignes_reelles(mq, sha, au_chemin)), p, MAINTENANT)
    assert r["CODE-T08"]["sha256"] == "e" * 64
    q = _prereg(tmp_path, mq, "sans-go.md", sauf="GO_T08.id")
    gabarit = dict(copy.deepcopy(mq), GO_T08={"id": "<<GO_T08>>", "plafond_usd": 120})
    d = "2026-11-20T10:00:00Z"
    cas = {
        "CODE-T08 qui cite un autre commit": (dict(remplacer={"CODE-T08": (d, "src", "c" * 40)}), "ne cite pas le commit"),
        "CODE-T08 : commit prolongé dans le chemin": (dict(remplacer={"CODE-T08": (d, f"src@{commit}0", "e" * 64)}),
                                                      "ne cite pas le commit"),
        "CODE-T08 sans commit": (dict(remplacer={"CODE-T08": (d, "src/controle_ia/t08", "e" * 64)}), "ne cite pas"),
        "SCELLEMENT-T08 d'une autre empreinte": (dict(remplacer={"SCELLEMENT-T08": (d, "prereg/texte.md", "f" * 64)}),
                                                 "autre texte scellé"),
        "SCELLEMENT-T08 postérieure au passage": (
            dict(remplacer={"SCELLEMENT-T08": ("2026-11-20T12:00:01Z", "prereg/texte.md", sha)}),
            "ligne SCELLEMENT-T08 .* non antérieure à l'heure du passage à blanc"),
        "CODE-T08 à la même seconde que le passage": (dict(remplacer={"CODE-T08": ("2026-11-20T12:00:00Z", "src", commit)}),
                                                      "ligne CODE-T08 .* non antérieure"),
        "COURSE-T08 déjà inscrite": (dict(plus=[("COURSE-T08", "2026-11-20T11:00:00Z", "diag/x/course-t08.json", "1" * 64)]),
                                     "COURSE-T08 déjà inscrite"),
        "RUN-CONFIRMATION-T06 autre que RUN_7B": (
            dict(remplacer={"RUN-CONFIRMATION-T06": (d, "runs/x/manifeste.json", "9" * 64)}), "≠ marqueur RUN_7B"),
        "CODE-MOTS-ET-COUT-T06 autre que son marqueur": (
            dict(remplacer={"CODE-MOTS-ET-COUT-T06": (d, "src/x.py", "9" * 64)}), "≠ marqueur CODE_MOTS_ET_COUT_T06"),
        "CODE-T08 absente": (dict(retirer=("CODE-T08",)), "ligne CODE-T08 absente"),
        "CODE-T08 inscrite deux fois": (dict(plus=[("CODE-T08", d, "src", commit)]), "deux fois"),
    }
    for nom, (k, motif) in cas.items():
        reg = _registre(tmp_path, re.sub(r"[^A-Za-z0-9]", "-", nom), _lignes_reelles(mq, sha, **k))
        with pytest.raises(GardeArret, match=motif):
            lv.passage_a_blanc_reel(mq, reg, p, MAINTENANT)
    reg = _registre(tmp_path, "texte", _lignes_reelles(mq, sha))
    for prereg, marqueurs, motif in ((q, mq, r"GO_T08\.id"), (p, gabarit, "non rempli"), (None, mq, "R1")):
        with pytest.raises(GardeArret, match=motif):
            lv.passage_a_blanc_reel(marqueurs, reg, prereg, MAINTENANT)
    # heure de la machine par défaut : lignes du passé, passe ; lignes datées après l'heure de la machine, arrêt
    passe = {k: ("2026-11-01T10:00:00Z", *v[1:]) for k, v in
             {"SCELLEMENT-T08": (d, "prereg/texte.md", sha), "CODE-T08": (d, "src", commit)}.items()}
    r = lv.passage_a_blanc_reel(mq, _registre(tmp_path, "machine", _lignes_reelles(mq, sha, passe)), p)
    assert datetime.fromisoformat(r["passage_a_blanc"]) > datetime(2026, 11, 1, 10, tzinfo=timezone.utc)
    futur = {k: ("2999-01-01T00:00:00Z", *v[1:]) for k, v in passe.items()}
    with pytest.raises(GardeArret, match="non antérieure à l'heure du passage à blanc"):
        lv.passage_a_blanc_reel(mq, _registre(tmp_path, "machine-futur", _lignes_reelles(mq, sha, futur)), p)


# --- comparateur de l'essai de bout en bout (VCT8-02) ---------------------------------------------------------------------

RUN_LECTURE = "20261114-000000-t08-lecture-jouet"


def _racine_comparee(d: Path, cree_le: str, tables: dict, citer=None) -> None:
    """Racine factice : manifeste de la lecture (date `cree_le`), `tables-d-f-t08.json` (enveloppe qui cite le
    manifeste), `lecture-t08.json` qui cite le fichier des tables (chemin, empreinte, contenu ; `citer(f)` : artefact),
    un fichier de données."""
    sha_m = fj.ecrire_json(d / "runs" / RUN_LECTURE / "manifeste.json", {"run_id": RUN_LECTURE, "cree_le": cree_le})
    sha_t = fj.ecrire_json(d / "diag" / RUN_LECTURE / "tables-d-f-t08.json",
                           {"run_id": RUN_LECTURE, "manifeste_sha256": sha_m, "resultat": tables})
    f = {"chemin": f"diag/{RUN_LECTURE}/tables-d-f-t08.json", "sha256": sha_t, "contenu_sha256": lv._sha(tables)}
    if citer is not None:
        citer(f)
    fj.ecrire_json(d / "diag" / RUN_LECTURE / "lecture-t08.json",
                   {"run_id": RUN_LECTURE, "manifeste_sha256": sha_m,
                    "resultat": {"table_D": tables["table_D"], "tables_D_F_fichier": f}})
    fj.ecrire_json(d / "donnees" / "x" / "d.json", {"x": 1})


def test_comparateur_lecture_exclusion_declaree_et_controle_des_tables(tmp_path):
    """VCT8-02 : `essai_jouet_v1.comparer` compare `lecture-t08.json` hors la seule clé `tables_D_F_fichier.sha256`
    (exclusion déclarée dans sa sortie), exige l'égalité de `chemin` et `contenu_sha256`, et vérifie dans chaque racine
    que l'empreinte citée est celle du fichier des tables sur disque. Cas sain (deux racines dont seuls les manifestes
    diffèrent) : 0 différent ; artefacts : contenu des tables changé dans une racine ; empreinte citée fausse ;
    `contenu_sha256` cité faux."""
    tables = {"table_D": {"ligne": "D6"}, "table_F": {"S25": {"ligne": "F4"}}}
    lec = f"diag/{RUN_LECTURE}/lecture-t08.json"
    tab = f"diag/{RUN_LECTURE}/tables-d-f-t08.json"
    _racine_comparee(tmp_path / "a", "2026-11-14T00:00:01+00:00", tables)
    _racine_comparee(tmp_path / "b", "2026-11-14T00:00:02+00:00", tables)
    ra, rb = (json.loads((tmp_path / x / lec).read_text())["resultat"] for x in ("a", "b"))
    assert ra["tables_D_F_fichier"]["sha256"] != rb["tables_D_F_fichier"]["sha256"]    # l'écart que l'exclusion couvre
    r = ej.comparer(tmp_path / "a", tmp_path / "b")                                     # cas sain
    assert r["differents"] == [] and r["deterministe"] and r["motifs"] == {}
    # identiques à l'octet : le fichier de données et son compagnon ; exclus : manifeste, son compagnon, deux compagnons
    assert sorted(r["resultats_identiques"]) == [lec, tab] and r["identiques_octet"] == 2 and len(r["exclus"]) == 4
    assert r["controle_tables_par_racine"] == {"a": True, "b": True}
    assert any("tables_D_F_fichier.sha256" in x["regle"] for x in r["exclusions_declarees"])
    artefacts = {
        "contenu": (dict(tables={**tables, "table_D": {"ligne": "D5"}}), [lec, tab], "hors tables_D_F_fichier.sha256",
                    {"a": True, "b": True}),
        "empreinte": (dict(citer=lambda f: f.__setitem__("sha256", "0" * 64)), [lec], "racine b : empreinte citée",
                      {"a": True, "b": False}),
        "contenu-cite": (dict(citer=lambda f: f.__setitem__("contenu_sha256", "0" * 64)), [lec],
                         "racine b : contenu_sha256", {"a": True, "b": False}),
    }
    for nom, (k, differents, motif, controle) in artefacts.items():
        b = tmp_path / f"b-{nom}"
        _racine_comparee(b, "2026-11-14T00:00:03+00:00", k.get("tables", tables), k.get("citer"))
        r = ej.comparer(tmp_path / "a", b)
        assert r["differents"] == differents and not r["deterministe"], nom
        assert motif in r["motifs"][lec] and r["controle_tables_par_racine"] == controle, nom
