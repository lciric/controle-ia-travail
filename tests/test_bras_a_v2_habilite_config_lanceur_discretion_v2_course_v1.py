"""Essais de la configuration de course du lanceur de l'étape de discrétion du bras A, version 2 — configuration v1.

Mandat : `docs/notes/bras-a-contre-lecture-habilitee-v1/mandat-lecteur-habilite-lanceur-discretion-v2-et-configuration-
v1.md` (e65415a7…), reste (c). La configuration fixe le dossier du fichier des scores par unité et cite le texte scellé
du bras A par un marqueur unique, `EMPREINTE_TEXTE_V2_BRAS_A`, que la mère remplace par l'empreinte du texte après son
scellement. Tant que le marqueur reste, la configuration est refusée : par la garde de ce fichier
(`exiger_marqueur_remplace`) et par le lanceur lui-même (empreinte du texte hors format). Chaque garde a un cas sain et
un artefact (R5). Aucun fichier de course, aucun modèle, aucune donnée réelle : copies dans un dossier temporaire.

    PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider \\
        tests/test_bras_a_v2_habilite_config_lanceur_discretion_v2_course_v1.py
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets.bras_a_v2_habilite import autres_moniteurs_v11 as A
from controle_ia.organismes_discrets.bras_a_v2_habilite_lanceur import lanceur_discretion_v2 as L
from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
DOSSIER = RACINE / "docs/notes/bras-a-moniteurs-v1"
CONFIG_V1 = DOSSIER / "config-lanceur-discretion-bras-a-v2-course-v1.json"
GABARIT_V2 = DOSSIER / "config-lanceur-discretion-bras-a-gabarit-v2.json"
MARQUEUR = "EMPREINTE_TEXTE_V2_BRAS_A"
RANGS = "donnees/bras-a-v2-discretion/rangs-par-unite"
TEXTE = "prereg/T0.7-organismes-discrets-v-a-v2.md"
ENTREE_FICHIER = L.MODULES_APPELES["entree"]
ENTREE_SHA = "cb668bb95a9c0a37b1a08a91f304e1b756ef5b0ebddc0a3f193be0692e0bfa10"
# Valeurs factices, pour les seules clés que cette configuration laisse à fixer : elles ne servent qu'à mener la
# lecture du lanceur jusqu'à la garde du texte scellé.
FACTICES = {
    "registre_des_accords_fige": {"chemin": "registres/go-fige-essai.md", "sha256": "f" * 64, "commit": "c" * 40},
    "rejeu": {"chemin": "essai/rejeu.jsonl", "sha256": "1" * 64},
    "configuration_du_bras": {"chemin": "essai/bras.json", "sha256": "2" * 64},
    "taches": {"chemin": "essai/taches.json", "sha256": "3" * 64},
    "statistique_agregateur": "moyenne",
    "lecture": {"max_nouveaux": 8, "temperature": 1.0, "regle_balise_absente": "imposer", "masse_min": 0.5, "lot": 400},
    "fins_moniteur_boite_noire": [1, 2],
}


def exiger_marqueur_remplace(chemin: Path) -> None:
    """Garde de la configuration de course : refus tant que le marqueur de l'empreinte du texte reste ; sinon, une
    empreinte entière en minuscules au texte scellé."""
    texte = Path(chemin).read_text(encoding="utf-8")
    if MARQUEUR in texte:
        raise GardeArret(f"configuration {Path(chemin).name} : marqueur {MARQUEUR} encore présent : refus")
    sha = json.loads(texte)["texte_scelle"]["sha256"]
    if not (isinstance(sha, str) and re.fullmatch(r"[0-9a-f]{64}", sha)):
        raise GardeArret(f"configuration {Path(chemin).name} : empreinte du texte scellé hors format")


def _sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _copie_scellee(tmp_path: Path, cfg: dict, nom: str) -> Path:
    p = tmp_path / nom
    p.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(p)
    return p


def _config_v1() -> dict:
    return json.loads(CONFIG_V1.read_text(encoding="utf-8"))


def test_configuration_v1_scellee_et_conforme_au_gabarit():
    """Compagnon égal ; clés du lanceur, dans l'ordre ; seule différence au gabarit v2 : le texte scellé cité."""
    assert (Path(str(CONFIG_V1) + ".sha256").read_text(encoding="utf-8").split()[0]) == _sha(CONFIG_V1)
    c, g = _config_v1(), json.loads(GABARIT_V2.read_text(encoding="utf-8"))
    assert tuple(c) == L.CLES_CONFIG
    assert {k for k in c if c[k] != g[k]} == {"texte_scelle"}
    assert c["texte_scelle"] == {"chemin": TEXTE, "sha256": MARQUEUR}
    assert c["version"] == L.VERSION and c["mode"] == "reel"
    assert (c["n_permutations"], c["n_tirages"]) == (A.N_PERMUTATIONS, A.N_TIRAGES)


def test_dossier_des_rangs_fixe_et_disjoint(tmp_path):
    c = _config_v1()
    assert tuple(c["dossiers"]) == L.DOSSIERS and c["dossiers"]["rangs"] == RANGS
    L.exiger_dossiers_disjoints({k: tmp_path / v for k, v in c["dossiers"].items()})            # cas sain
    with pytest.raises(GardeArret, match="disjoints"):                                           # artefact
        L.exiger_dossiers_disjoints({**{k: tmp_path / v for k, v in c["dossiers"].items()},
                                     "sortie": tmp_path / RANGS / "sortie"})


def test_modules_a_leur_empreinte():
    c = _config_v1()
    assert set(c["modules"]) == set(L.MODULES_APPELES.values())
    for chemin, sha in c["modules"].items():
        if chemin == ENTREE_FICHIER:                     # module d'entrée : sur la branche de la relance seulement
            assert sha == ENTREE_SHA
        else:
            assert _sha(RACINE / chemin) == sha, chemin


def test_marqueur_unique_au_seul_texte_scelle():
    texte = CONFIG_V1.read_text(encoding="utf-8")
    assert texte.count(MARQUEUR) == 1
    assert _config_v1()["texte_scelle"]["sha256"] == MARQUEUR


def test_garde_du_marqueur_cas_sain_et_artefact(tmp_path):
    c = _config_v1()
    artefact = _copie_scellee(tmp_path, c, "config-avec-marqueur.json")
    with pytest.raises(GardeArret, match="marqueur"):
        exiger_marqueur_remplace(artefact)
    with pytest.raises(GardeArret, match="marqueur"):
        exiger_marqueur_remplace(CONFIG_V1)               # la configuration telle que versée est refusée
    sain = _copie_scellee(tmp_path, {**c, "texte_scelle": {"chemin": TEXTE, "sha256": "a" * 64}}, "config-saine.json")
    exiger_marqueur_remplace(sain)
    hors_format = _copie_scellee(tmp_path, {**c, "texte_scelle": {"chemin": TEXTE, "sha256": "A" * 64}}, "config-hf.json")
    with pytest.raises(GardeArret, match="hors format"):
        exiger_marqueur_remplace(hors_format)


def test_le_lanceur_refuse_le_marqueur_et_admet_son_remplacement(tmp_path):
    """Les clés laissées à fixer reçoivent des valeurs factices, pour que la lecture du lanceur arrive au texte scellé :
    avec le marqueur, refus sur le texte scellé ; marqueur remplacé par une empreinte entière, configuration admise."""
    c = {**_config_v1(), **FACTICES}
    assert [k for k, v in c.items() if v is None] == []
    artefact = _copie_scellee(tmp_path, c, "config-complete-avec-marqueur.json")
    with pytest.raises(GardeArret, match="texte scellé"):
        L.lire_la_configuration(artefact, cli=True)
    sain = _copie_scellee(tmp_path, {**c, "texte_scelle": {"chemin": TEXTE, "sha256": "a" * 64}},
                          "config-complete-saine.json")
    cfg, sha = L.lire_la_configuration(sain, cli=True)
    assert cfg["dossiers"]["rangs"] == RANGS and sha == _sha(sain)


def test_la_configuration_versee_n_est_pas_jouable():
    """Telle que versée, la configuration v1 garde des valeurs à fixer nulles : le lanceur la refuse."""
    with pytest.raises(GardeArret, match="laissées nulles"):
        L.lire_la_configuration(CONFIG_V1, cli=True)
