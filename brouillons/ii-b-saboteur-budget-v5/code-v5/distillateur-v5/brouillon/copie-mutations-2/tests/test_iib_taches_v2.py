"""(ii-b), contrôle « les tâches de réserve et d'évaluation n'ont aucune tâche commune » de `scripts/lancer_iib_v1.sh controles-explo`.
Défaut corrigé : le contrôle cherchait la liste au premier niveau du fichier (`KeyError: 'taches'`), alors que les fichiers réels de
l'extraction la portent sous `resultat.taches` (forme de `manifeste.ecrire_resultat`) ; les essais tournaient sur la seule forme
plate du jouet. Le contrôle lit désormais comme la course (`environnements/pilote_a.charger_taches`) : `resultat.taches` si
présent, sinon `taches` ; refus explicite si ni l'une ni l'autre n'est une liste non vide. Cas sains (forme réelle, forme plate du
jouet), artefacts refusés (clé absente, liste vide, tâche commune), R5 ; et les deux fichiers réels de `donnees/` : 32 tâches de
réserve, 64 d'évaluation, aucune commune. À blanc : dépôt factice, registres factices, faux outils, aucun réseau, aucune instance."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from controle_ia.environnements.pilote_a import charger_taches
from controle_ia.iib import configuration_v1 as cf
from controle_ia.iib import jouet_v1 as jv
from controle_ia.scellement import sceller, verifier
from test_iib_scripts_v1 import _controles, _git, monde  # noqa: F401  (fixture du dépôt factice et des faux outils)

RACINE = Path(__file__).resolve().parents[1]
CLES = ("taches_reserve", "taches_evaluation")
REELS = {cle: RACINE / cf.TACHES_REELLES[cle]["chemin"] for cle in CLES}
CONFIG = "prereg/config-iib-jouet.json"


def _forme_reelle(taches) -> dict:
    """Même structure que les fichiers de l'extraction, données factices."""
    return {"run_id": "00000000-000000-factice", "manifeste_sha256": "0" * 64, "resultat": {"taches": taches}}


def _recommiter(m, fichiers: dict) -> str:
    """Remplace des fichiers de tâches du dépôt factice ({clé: contenu, ou Path d'un fichier à copier}), les rescelle, recite leur
    empreinte dans la configuration jouet, pousse : rend le commit neuf."""
    src = m["src"]
    cfg = src / CONFIG
    c = json.loads(cfg.read_text(encoding="utf-8"))
    for cle, contenu in fichiers.items():
        f = src / c[cle]["chemin"]
        if isinstance(contenu, Path):
            shutil.copy(contenu, f)
        else:
            f.write_text(json.dumps(contenu, ensure_ascii=False), encoding="utf-8")
        Path(str(f) + ".sha256").unlink()
        c[cle]["sha256"] = sceller(f)
    cfg.write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    Path(str(cfg) + ".sha256").unlink()
    sceller(cfg)
    _git(src, "add", "-A")
    _git(src, "commit", "-qm", "tâches changées")
    _git(src, "push", "-q", "origin", "HEAD:refs/heads/prep/iib-essai")
    _git(src, "fetch", "-q", "origin", "refs/heads/prep/iib-essai:refs/remotes/origin/prep/iib-essai")
    return _git(src, "rev-parse", "HEAD")


def _conformes(d: Path, r) -> None:
    assert r.returncode == 0 and "CONTRÔLES CONFORMES" in r.stdout, r.stdout + r.stderr
    assert "KeyError" not in r.stderr and "Traceback" not in r.stderr, r.stderr
    assert (d / "lancement.txt").is_file() and not (d / "reserve.json").exists() and not (d / "evaluation.json").exists()


def _refuses(d: Path, r, motif: str) -> None:
    assert r.returncode == 2 and "contrôle « aucune tâche commune » refusé" in r.stdout and motif in r.stdout, r.stdout + r.stderr
    assert "CONTRÔLES CONFORMES" not in r.stdout and "Traceback" not in r.stderr and not (d / "lancement.txt").exists()


# --- cas sains ----------------------------------------------------------------------------------------------------------------
def test_controles_explo_sain_forme_reelle(monde):
    """Les deux fichiers sous `resultat.taches` (la forme qui levait `KeyError: 'taches'`)."""
    monde["commit"] = _recommiter(monde, {"taches_reserve": _forme_reelle(jv.taches_factices("r", 4)),
                                          "taches_evaluation": _forme_reelle(jv.taches_factices("e", 8))})
    _conformes(*_controles(monde))


def test_controles_explo_sain_forme_plate_du_jouet(monde):
    """La forme plate qu'écrit le jouet (`{"taches": […]}`) reste lue, comme par la course."""
    c = json.loads((monde["src"] / CONFIG).read_text(encoding="utf-8"))
    for cle in CLES:
        assert sorted(json.loads((monde["src"] / c[cle]["chemin"]).read_text(encoding="utf-8"))) == ["taches"]
    _conformes(*_controles(monde))


def test_controles_explo_sain_formes_melees(monde):
    monde["commit"] = _recommiter(monde, {"taches_evaluation": _forme_reelle(jv.taches_factices("e", 8))})
    _conformes(*_controles(monde))


# --- artefacts ----------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("cas, cle, contenu, quoi", [
    ("cle_absente", "taches_reserve", {"run_id": "x", "manifeste_sha256": "0" * 64}, "réserve"),
    ("resultat_sans_taches", "taches_evaluation", {"run_id": "x", "manifeste_sha256": "0" * 64, "resultat": {"insuffisant": []}}, "évaluation"),
    ("liste_vide_forme_reelle", "taches_evaluation", _forme_reelle([]), "évaluation"),
    ("liste_vide_forme_plate", "taches_reserve", {"taches": []}, "réserve"),
    ("taches_pas_une_liste", "taches_evaluation", _forme_reelle({"e0": {"identifiant": "e0"}}), "évaluation"),
    ("liste_au_premier_niveau", "taches_reserve", jv.taches_factices("r", 4), "réserve")])
def test_controles_explo_artefacts_liste_absente_ou_vide(monde, cas, cle, contenu, quoi):
    monde["commit"] = _recommiter(monde, {cle: contenu})
    d, r = _controles(monde, "x")
    _refuses(d, r, f"liste des tâches de {quoi} illisible : ni resultat.taches ni taches ne sont une liste non vide")


@pytest.mark.parametrize("forme", ["reelle", "plate"])
def test_controles_explo_artefact_tache_de_reserve_dans_l_evaluation(monde, forme):
    taches = jv.taches_factices("e", 7) + jv.taches_factices("r", 1)
    monde["commit"] = _recommiter(monde, {"taches_evaluation": _forme_reelle(taches) if forme == "reelle" else {"taches": taches}})
    d, r = _controles(monde, "x")
    _refuses(d, r, "communes r0")


# --- les deux fichiers réels de l'extraction ----------------------------------------------------------------------------------
reels_presents = pytest.mark.skipif(not all(f.is_file() and Path(str(f) + ".sha256").is_file() for f in REELS.values()),
                                    reason="fichiers de tâches de l'extraction absents de cet arbre")


@reels_presents
def test_fichiers_reels_32_de_reserve_64_d_evaluation_aucune_commune():
    """Par le chargeur de la course (sceau contrôlé) ; seuls les identifiants sont regardés."""
    assert REELS["taches_reserve"].name == "taches-entrainement.json" and REELS["taches_evaluation"].name == "taches-evaluation.json"
    for cle, f in REELS.items():
        assert verifier(f) == cf.TACHES_REELLES[cle]["sha256"]
        assert "taches" in json.loads(f.read_text(encoding="utf-8"))["resultat"]                   # forme de manifeste.ecrire_resultat
    reserve = [t["identifiant"] for t in charger_taches(REELS["taches_reserve"])]
    evaluation = [t["identifiant"] for t in charger_taches(REELS["taches_evaluation"])]
    assert len(reserve) == len(set(reserve)) == 32 and len(evaluation) == len(set(evaluation)) == 64
    assert not set(reserve) & set(evaluation)


@reels_presents
def test_controles_explo_sain_sur_les_deux_fichiers_reels(monde):
    """Le contrôle du lanceur passe sur les deux fichiers réels (copie de travail dans le dépôt factice de l'essai, effacée avec lui)."""
    monde["commit"] = _recommiter(monde, dict(REELS))
    c = json.loads((monde["src"] / CONFIG).read_text(encoding="utf-8"))
    assert {cle: c[cle]["sha256"] for cle in CLES} == {cle: cf.TACHES_REELLES[cle]["sha256"] for cle in CLES}
    _conformes(*_controles(monde))
