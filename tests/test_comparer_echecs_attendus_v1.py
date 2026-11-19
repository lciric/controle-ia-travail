"""Essais du comparateur des échecs attendus (`scripts/comparer_echecs_attendus_v1.py`, R-3686) : cas sains (liste exacte,
sous-ensemble, échappements de pytest) et artefacts (échec neuf injecté, sortie sans `-rf`, sortie tronquée, note sans
marqueurs, liste en double ou vide) ; puis la note réelle du dépôt, lue par le programme. Données factices seulement."""
from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
PROGRAMME = RACINE / "scripts" / "comparer_echecs_attendus_v1.py"
NOTE_REELLE = RACINE / "docs" / "notes" / "essais-dates-t06-v1" / "echecs-attendus-dates-v1.md"
_spec = importlib.util.spec_from_file_location("comparer_echecs_attendus_v1", PROGRAMME)
cmp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cmp)

A1 = "tests/test_x.py::test_un"
A2 = "tests/test_x.py::test_deux[cité plusieurs fois]"
A4 = "tests/test_x.py::test_quatre[a - b]"
A3 = "tests/test_y.py::test_trois[env_sup4-fin du GO reçue (1794873500) ≠ calendrier.fin_go_utc]"


def _note(*ids: str) -> str:
    corps = "\n".join(ids)
    return f"# note factice\n\nTexte, `tests/test_hors_liste.py::test_cite` hors des marqueurs.\n\n{cmp.DEBUT}\n```text\n{corps}\n```\n{cmp.FIN}\n"


def _sortie(echecs: list[str], passes: int = 5, escape: bool = True, message: bool = True, bilan: bool = True) -> str:
    lignes = ["........F.F", "=========================== short test summary info ============================"]
    for e in echecs:
        i = e.encode("ascii", "backslashreplace").decode("ascii") if escape else e
        lignes.append(f"FAILED {i}" + (" - AssertionError: AMORCE - refus" if message else ""))
    if bilan:
        lignes.append(f"{len(echecs)} failed, {passes} passed in 12.34s" if echecs else f"{passes} passed in 1.00s")
    return "\n".join(lignes) + "\n"


def _jouer(tmp_path, note: str, *sorties: str) -> subprocess.CompletedProcess:
    n = tmp_path / "note.md"
    n.write_text(note, encoding="utf-8")
    chemins = []
    for k, s in enumerate(sorties):
        p = tmp_path / f"sortie-{k}.txt"
        p.write_text(s, encoding="utf-8")
        chemins.append(str(p))
    return subprocess.run([sys.executable, "-I", str(PROGRAMME), str(n), *chemins], capture_output=True, text=True, timeout=60)


def test_cas_sain_liste_exacte_code_0(tmp_path):
    r = _jouer(tmp_path, _note(A1, A2, A3), _sortie([A1, A2, A3]))
    assert r.returncode == 0, r.stdout + r.stderr
    assert "CONFORME" in r.stdout and "échecs neufs : 0" in r.stdout and "ATTENDU NON VU" not in r.stdout


def test_cas_sain_sous_ensemble_nomme_les_attendus_qui_passent(tmp_path):
    r = _jouer(tmp_path, _note(A1, A2, A3), _sortie([A2]))
    assert r.returncode == 0, r.stdout
    assert f"ATTENDU NON VU EN ÉCHEC (passe désormais, ou fichier non joué) : {A1}" in r.stdout and A3 in r.stdout
    assert "attendus non vus en échec : 2" in r.stdout


def test_cas_sain_plusieurs_sorties_et_aucun_echec(tmp_path):
    r = _jouer(tmp_path, _note(A1, A2), _sortie([A1]), _sortie([], passes=9))
    assert r.returncode == 0 and A2 in r.stdout and "échecs vus : 1" in r.stdout, r.stdout


def test_artefact_echec_neuf_injecte_code_1(tmp_path):
    neuf = "tests/test_x.py::test_neuf_injecte"
    r = _jouer(tmp_path, _note(A1, A2, A3), _sortie([A1, A2, A3, neuf]))
    assert r.returncode == 1, r.stdout
    assert f"ÉCHEC NEUF : {neuf}" in r.stdout and "NON CONFORME : 1 échec(s)" in r.stdout


def test_artefact_erreur_de_mise_en_place_neuve_code_1(tmp_path):
    s = _sortie([A1]).replace("1 failed, 5 passed in 12.34s", "ERROR tests/test_z.py::test_fixture - RuntimeError\n1 failed, 5 passed, 1 error in 2.00s")
    r = _jouer(tmp_path, _note(A1), s)
    assert r.returncode == 1 and "ÉCHEC NEUF : tests/test_z.py::test_fixture" in r.stdout, r.stdout


@pytest.mark.parametrize("escape, message", [(True, True), (False, True), (True, False)])
def test_identifiants_echappes_et_message_coupe_hors_crochets(tmp_path, escape, message):
    """pytest écrit « \\xe9 » et « \\u2260 » dans les identifiants paramétrés ; un « - » dans les crochets n'est pas le séparateur."""
    r = _jouer(tmp_path, _note(A2, A3, A4), _sortie([A2, A3, A4], escape=escape, message=message))
    assert r.returncode == 0 and "échecs vus : 3" in r.stdout, r.stdout


@pytest.mark.parametrize("sortie, motif", [
    (_sortie([A1], bilan=False), "aucune ligne de bilan"),                                    # sortie tronquée
    ("........FF\n2 failed, 8 passed in 3.00s\n", "relancer pytest avec -rf"),               # lancée sans -rf
    (_sortie([A1]).replace("1 failed", "2 failed"), "relancer pytest avec -rf"),            # bilan plus grand que la liste
    ("", "aucune ligne de bilan"),                                                            # sortie vide
])
def test_artefacts_sortie_illisible_code_2(tmp_path, sortie, motif):
    r = _jouer(tmp_path, _note(A1), sortie)
    assert r.returncode == 2 and "ILLISIBLE" in r.stdout and motif in r.stdout, r.stdout


@pytest.mark.parametrize("note, motif", [
    ("# note sans marqueurs\n- `tests/test_x.py::test_un`\n", "marqueur"),
    (_note(A1, A1), "en double"),
    (_note(), "vide"),
    (_note(A1).replace(cmp.DEBUT, "@@").replace(cmp.FIN, cmp.DEBUT).replace("@@", cmp.FIN), "avant le marqueur de début"),
    (_note(A1, "pas un identifiant"), "illisible"),
])
def test_artefacts_note_illisible_code_2(tmp_path, note, motif):
    r = _jouer(tmp_path, note, _sortie([A1]))
    assert r.returncode == 2 and motif in r.stdout, r.stdout


def test_sans_argument_code_2():
    r = subprocess.run([sys.executable, "-I", str(PROGRAMME)], capture_output=True, text=True, timeout=60)
    assert r.returncode == 2 and "NOTE.md" in r.stderr


def test_note_reelle_du_depot_lisible_178_identifiants_des_onze_fichiers():
    attendus = cmp.lire_attendus(NOTE_REELLE.read_text(encoding="utf-8"))
    assert len(attendus) == 178 and len(set(attendus)) == 178
    fichiers = {a.split("::")[0] for a in attendus}
    assert fichiers == {f"tests/test_t06_{n}.py" for n in ("scripts", "v2_scripts", "v3_scripts", "v5_amorce", "v6_amorce", "v7_amorce",
                                                          "v7_amorce_minuterie", "v12_amorce", "v11_liste", "v12_liste", "v13_liste")}
    r = cmp.comparer(attendus, attendus[:10] + ["tests/test_t06_v12_amorce.py::test_injecte"])
    assert r["neufs"] == ["tests/test_t06_v12_amorce.py::test_injecte"] and len(r["attendus_non_vus"]) == 168
