"""Essais du programme de l'extrait des états, v4 (gardes neuves : trois scellements, racine des registres, nom de sortie,
écriture exclusive), sur cas sains et artefacts (R5). Aucune donnée de la course n'est lue : sorties de lectures fabriquées.

    PYTHONPATH=src python -m pytest -q docs/notes/barreau8-cote-expose-pieces-lecture-v1/test_extrait_iib_etats_lectures_cote_moniteurs_v4.py
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller

ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[2]
spec = importlib.util.spec_from_file_location("extrait_v4", ICI / "extrait_iib_etats_lectures_cote_moniteurs_v4.py")
ev4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ev4)

RUN = "20261123-043944-iib-course-reel"
CLES = [c for c, _ in ev4.SCELLEMENTS]


def registre_jouet(tmp: Path, heures=("2026-11-19T06:32:25Z", "2026-11-24T04:21:08Z", "2026-11-24T10:34:26Z"),
                   extra: str = "", alterer: int | None = None) -> Path:
    racine = tmp / "main"
    (racine / "registres").mkdir(parents=True)
    lignes = ["# registre jouet", ""]
    for k, (cle, h) in enumerate(zip(CLES, heures)):
        t = racine / "prereg" / f"texte-{k}.md"
        t.parent.mkdir(exist_ok=True)
        t.write_text(f"texte {k}\n", encoding="utf-8")
        sha = sceller(t)
        if alterer == k:
            t.write_text("altéré\n", encoding="utf-8")
        lignes.append(f"| {cle} | {h} | prereg/texte-{k}.md | {sha} |")
    lignes.append("| CODE-PASSE-IIB | 2026-11-24T11:31:45Z | x.json | " + "0" * 64 + " |")
    if extra:
        lignes.append(extra)
    r = racine / "registres" / "sondes-iib-v1.md"
    r.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return r


def lectures_jouet(tmp: Path) -> Path:
    racine = tmp / "course"
    (racine / "runs" / RUN).mkdir(parents=True)
    m = racine / "runs" / RUN / "manifeste.json"
    m.write_text(json.dumps({"run_id": RUN}), encoding="utf-8")
    sceller(m)
    d = racine / "diag" / RUN
    d.mkdir(parents=True)
    l1 = d / ev4.NOM_DOMMAGE
    l1.write_text(json.dumps({"phrase": "dommage non vu à cette puissance"}), encoding="utf-8")
    sha1 = sceller(l1)
    jeux = {k: {"etat": "échoue"} for k in ev4.JEUX}
    unites = {u: {"etat": "non calculable"} for u in ev4.UNITES}
    l2 = d / ev4.NOM_DIFFUSION
    l2.write_text(json.dumps({"lecture_1": {"sha256": sha1, "phrase": "dommage non vu à cette puissance"}, "jeux": jeux,
                              "etat_par_unite": {"unites": unites}, "phrase": None}), encoding="utf-8")
    sceller(l2)
    return racine


# --- trois scellements ------------------------------------------------------------------------------------------------------
def test_sain_trois_scellements(tmp_path):
    lus = ev4.exiger_trois_scellements(registre_jouet(tmp_path), empreintes_attendues=False)
    assert [c for c, _, _ in lus] == CLES


def test_sain_registre_reel_de_main():
    r = DEPOT / "registres" / "sondes-iib-v1.md"
    if not r.is_file():
        pytest.skip("registre de main absent de cet arbre")
    lus = ev4.exiger_trois_scellements(r)          # empreintes attendues exigées
    assert [e for _, _, e in lus] == [e for _, e in ev4.SCELLEMENTS]


@pytest.mark.parametrize("cas", ["absente", "doublon", "cle_inconnue", "mal_formee", "ordre", "futur", "absolu", "altere"])
def test_artefacts_scellements(tmp_path, cas):
    h = ("2026-11-19T06:32:25Z", "2026-11-24T04:21:08Z", "2026-11-24T10:34:26Z")
    if cas == "absente":
        r = registre_jouet(tmp_path)
        r.write_text("\n".join(l for l in r.read_text(encoding="utf-8").splitlines() if CLES[2] not in l) + "\n", encoding="utf-8")
    elif cas == "doublon":
        r = registre_jouet(tmp_path)
        l0 = [l for l in r.read_text(encoding="utf-8").splitlines() if l.startswith(f"| {CLES[0]} |")][0]
        r.write_text(r.read_text(encoding="utf-8") + l0 + "\n", encoding="utf-8")
    elif cas == "cle_inconnue":
        r = registre_jouet(tmp_path, extra="| SCELLEMENT-AUTRE-IIB | 2026-11-24T12:00:00Z | prereg/texte-0.md | " + "a" * 64 + " |")
    elif cas == "mal_formee":
        r = registre_jouet(tmp_path, extra="| SCELLEMENT-SONDES-IIB | hier | x |")
    elif cas == "ordre":
        r = registre_jouet(tmp_path, heures=(h[0], h[2], h[1]))
    elif cas == "futur":
        r = registre_jouet(tmp_path, heures=(h[0], h[1], "2099-01-01T00:00:00Z"))
    elif cas == "absolu":
        r = registre_jouet(tmp_path)
        r.write_text(r.read_text(encoding="utf-8").replace("| prereg/texte-1.md |", "| /etc/texte-1.md |"), encoding="utf-8")
    else:
        r = registre_jouet(tmp_path, alterer=1)
    with pytest.raises(GardeArret):
        ev4.exiger_trois_scellements(r, empreintes_attendues=False)


def test_artefact_empreinte_attendue(tmp_path):
    with pytest.raises(GardeArret, match="empreinte différente"):
        ev4.exiger_trois_scellements(registre_jouet(tmp_path), empreintes_attendues=True)


def test_ligne_d_une_autre_cle_ignoree(tmp_path):
    r = registre_jouet(tmp_path, extra="| SPEC-LECTURES-DOMMAGE-DIFFUSION-V5-IIB | 2026-11-24T17:18:19Z | a (b) | " + "c" * 64 + " |")
    assert len(ev4.exiger_trois_scellements(r, empreintes_attendues=False)) == 3


@pytest.mark.parametrize("chemin", ["registres/autre.md", "ailleurs/sondes-iib-v1.md"])
def test_artefacts_racine_des_registres(tmp_path, chemin):
    with pytest.raises(GardeArret):
        ev4.racine_des_registres(tmp_path / chemin)


# --- programme entier -------------------------------------------------------------------------------------------------------
def jouer(tmp_path, monkeypatch, sortie_nom=ev4.NOM_SORTIE):
    r = registre_jouet(tmp_path)
    racine = lectures_jouet(tmp_path)
    vrai = ev4.exiger_trois_scellements
    monkeypatch.setattr(ev4, "exiger_trois_scellements", lambda reg: vrai(reg, empreintes_attendues=False))
    sortie = tmp_path / "sortie" / sortie_nom
    code = ev4.main(["--racine", str(racine), "--run-id", RUN, "--registre-sondes", str(r), "--sortie", str(sortie)])
    return code, sortie


def test_sain_programme(tmp_path, monkeypatch):
    code, sortie = jouer(tmp_path, monkeypatch)
    assert code == 0
    x = json.loads(sortie.read_text(encoding="utf-8"))
    assert sorted(x) == ["avertissement", "lecture_diffusion", "lecture_dommage", "run_id"]
    etats = [v for p in x["lecture_diffusion"]["par_paire"].values() for v in p.values()]
    assert len(etats) == 13
    assert (sortie.parent / (sortie.name + ".sha256")).is_file()


def test_artefact_nom_de_sortie(tmp_path, monkeypatch):
    code, sortie = jouer(tmp_path, monkeypatch, sortie_nom="autre.json")
    assert code == 1 and not sortie.exists()


def test_artefact_ecrasement(tmp_path, monkeypatch):
    code, sortie = jouer(tmp_path, monkeypatch)
    assert code == 0
    r = tmp_path / "main" / "registres" / "sondes-iib-v1.md"
    racine = tmp_path / "course"
    assert ev4.main(["--racine", str(racine), "--run-id", RUN, "--registre-sondes", str(r), "--sortie", str(sortie)]) == 1


def test_artefact_registre_sans_scellements(tmp_path):
    racine = lectures_jouet(tmp_path)
    (tmp_path / "vide" / "registres").mkdir(parents=True)
    r = tmp_path / "vide" / "registres" / "sondes-iib-v1.md"
    r.write_text("| CODE-PASSE-IIB | 2026-11-24T11:31:45Z | x | " + "0" * 64 + " |\n", encoding="utf-8")
    sortie = tmp_path / "s" / ev4.NOM_SORTIE
    assert ev4.main(["--racine", str(racine), "--run-id", RUN, "--registre-sondes", str(r), "--sortie", str(sortie)]) == 1
    assert not sortie.exists()
