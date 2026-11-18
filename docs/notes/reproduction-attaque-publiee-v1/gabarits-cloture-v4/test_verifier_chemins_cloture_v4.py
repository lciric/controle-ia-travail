# v4 : renommé (R12), contenu inchangé depuis la v3
# v3 : corrections de la contre-lecture de la v2 (8 constats)
# v2 : corrections de la contre-lecture de la v1 (14 constats)
"""Essais de `verifier_chemins_cloture_v4.py` (v3 : renommé, R12 ; essais de la v2 inchangés) : un cas sain et trois artefacts (R5) ; v2 : `--pousse` (constat 6) et
le rapport d'un lecteur passé par `--autre` (constat 12), chacun sur un cas sain et sur des artefacts. Joués en sous-processus
(`python -I`), sur des arbres jetables sous `tmp_path` ; aucun fichier du dépôt n'est lu ni écrit."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "verifier_chemins_cloture_v4.py"


def arbre(tmp_path: Path) -> dict:
    racine = tmp_path / "depot"
    (racine / "src" / "controle_ia").mkdir(parents=True)
    base = racine / "runs" / "temoin-bailey-v1-20261111"
    d1 = base / "lecture-assemblee-v1"
    d2 = base / "sortie-conduite-v15"
    d1.mkdir(parents=True)
    d2.mkdir(parents=True)
    hors = tmp_path / "hors"
    hors.mkdir()
    return {"racine": racine, "base": base, "d1": d1, "d2": d2, "hors": hors}


def args(t: dict, **rempl) -> list[str]:
    h, b = t["hors"], t["base"]
    v = {"racine": t["racine"], "dossiers_lus": [t["d1"], t["d2"]],
         "attendus": [b / "attendu-lecture-assemblee-v1-v1.json", b / "attendu-sortie-conduite-v15-v1.json"],
         "sorties": [b / "sortie-lecture-assemblee-v1-v1.json", b / "sortie-sortie-conduite-v15-v1.json"],
         "cache_p": h / "pycache-cloture-v1", "factice_dossier": h / "factice-v1",
         "factice_attendu": h / "attendu-factice-v1.json", "factice_sortie": h / "sortie-factice-v1.json",
         "note": t["racine"] / "registres" / "passations" / "2026-11-20-1200-note-cloture-bailey.md",
         "autres": [], "pousses": [], **rempl}
    out = ["--racine", str(v["racine"])]
    out += [x for d in v["dossiers_lus"] for x in ("--dossier-lu", str(d))]
    out += [x for d in v["attendus"] for x in ("--attendu", str(d))]
    out += [x for d in v["sorties"] for x in ("--sortie", str(d))]
    out += ["--cache-p", str(v["cache_p"]), "--factice-dossier", str(v["factice_dossier"]),
            "--factice-attendu", str(v["factice_attendu"]), "--factice-sortie", str(v["factice_sortie"]),
            "--note", str(v["note"])]
    out += [x for d in v["autres"] for x in ("--autre", str(d))]
    out += [x for d in v["pousses"] for x in ("--pousse", str(d))]
    return out


def jouer(argv: list[str]) -> tuple[int, list[str]]:
    r = subprocess.run([sys.executable, "-I", "-B", str(SCRIPT), *argv], capture_output=True, text=True)
    return r.returncode, r.stdout.splitlines()


def test_cas_sain_conforme(tmp_path):
    """Chemins sous <BASE> mais hors des dossiers lus, <P> absent, note dans le dépôt hors de src/ : conforme."""
    t = arbre(tmp_path)
    code, lignes = jouer(args(t))
    assert (code, lignes) == (0, ["conforme"])
    (t["hors"] / "pycache-cloture-v1").mkdir()  # <P> présent et vide : toujours conforme
    assert jouer(args(t)) == (0, ["conforme"])


def test_sous_src_par_point_point_et_p_non_vide(tmp_path):
    """Artefact : <P> écrit hors de src/ en apparence (`…/runs/../src/…`) mais résolu sous <racine>/src ; un attendu
    sous src/ ; puis <P> non vide."""
    t = arbre(tmp_path)
    p = t["racine"] / "runs" / ".." / "src" / "pyc"
    a = t["racine"] / "src" / "attendu.json"
    code, lignes = jouer(args(t, cache_p=p, attendus=[a, t["base"] / "attendu-2.json"]))
    assert code == 1 and lignes[0] == "écarts : 2"
    assert any(l.startswith("<P> : chemin résolu sous <racine>/src") for l in lignes)
    assert any(l.startswith("attendu : chemin résolu sous <racine>/src") for l in lignes)
    plein = t["hors"] / "pyc-plein"
    plein.mkdir()
    (plein / "x.pyc").write_bytes(b"")
    code, lignes = jouer(args(t, cache_p=plein))
    assert code == 1 and lignes[1].startswith("<P> : ni absent ni répertoire vide")


def test_sous_un_dossier_lu_par_lien_et_par_detour(tmp_path):
    """Artefact : une sortie écrite par un détour (`d2/../d2/…`) et une note par un lien symbolique qui mène dans d1 :
    toutes deux résolues sous un dossier lu ; le dossier factice dans d2."""
    t = arbre(tmp_path)
    lien = t["hors"] / "lien"
    lien.symlink_to(t["d1"], target_is_directory=True)
    s = t["d2"] / ".." / "sortie-conduite-v15" / "s.json"
    code, lignes = jouer(args(t, sorties=[t["base"] / "s1.json", s], note=lien / "note.md",
                              factice_dossier=t["d2"] / "factice"))
    assert code == 1 and lignes[0] == "écarts : 3"
    assert sum("sous le dossier lu" in l for l in lignes) == 3
    assert any(l.startswith("note de clôture : chemin résolu sous le dossier lu " + str(t["d1"])) for l in lignes)
    assert any(l.startswith("sortie : chemin résolu sous le dossier lu " + str(t["d2"])) for l in lignes)


def test_chemin_non_absolu(tmp_path):
    """Artefact : une note et un attendu factice donnés en chemins relatifs (même s'ils se résoudraient hors de src/
    et des dossiers lus) ; un dossier lu relatif aussi."""
    t = arbre(tmp_path)
    code, lignes = jouer(args(t, note="registres/note.md", factice_attendu="attendu-factice.json"))
    assert code == 1 and lignes[0] == "écarts : 2"
    assert "note de clôture : chemin non absolu (registres/note.md)" in lignes
    assert "attendu factice : chemin non absolu (attendu-factice.json)" in lignes
    code, lignes = jouer(args(t, dossiers_lus=["runs/x", t["d2"]]))
    assert code == 1 and "dossier lu : chemin non absolu (runs/x)" in lignes


def test_pousse_sous_racine_hors_src_git_et_dossiers_lus(tmp_path):
    """Constat 6 : les chemins ajoutés à la branche (attendus, sorties, note, journal) sont sous <racine>, hors de src/,
    de .git/ et des dossiers lus. Cas sain : sous <BASE> et sous registres/ ; artefacts : hors de <racine>, par un lien
    qui sort de <racine>, sous .git/, sous un dossier lu, sous src/ par détour."""
    t = arbre(tmp_path)
    b, r = t["base"], t["racine"]
    (r / ".git").mkdir()
    saines = [b / "attendu-lecture-assemblee-v1-v1.json", b / "sortie-lecture-assemblee-v1-v1.json",
              r / "registres" / "passations" / "2026-11-20-1200-note-cloture-bailey.md", b / "journal-cloture-v1.txt"]
    assert jouer(args(t, pousses=saines)) == (0, ["conforme"])
    lien = b / "lien-dehors"
    lien.symlink_to(t["hors"], target_is_directory=True)
    fautifs = [t["hors"] / "journal.txt", lien / "s.json", r / ".git" / "x.json", t["d1"] / "a.json",
               r / "runs" / ".." / "src" / "s.json"]
    code, lignes = jouer(args(t, pousses=saines + fautifs))
    assert code == 1 and lignes[0] == "écarts : 5"
    assert sum(l.startswith("chemin poussé : chemin résolu hors de <racine>") for l in lignes) == 2
    assert any(l.startswith("chemin poussé : chemin résolu sous <racine>/.git") for l in lignes)
    assert any(l.startswith("chemin poussé : chemin résolu sous le dossier lu " + str(t["d1"])) for l in lignes)
    assert any(l.startswith("chemin poussé : chemin résolu sous <racine>/src") for l in lignes)
    code, lignes = jouer(args(t, pousses=["runs/journal.txt"]))
    assert code == 1 and "chemin poussé : chemin non absolu (runs/journal.txt)" in lignes


def test_rapport_de_lecteur_par_autre(tmp_path):
    """Constat 12 : le chemin du rapport d'un lecteur, passé par `--autre` avant le lancement. Cas sain : hors de src/ et
    des dossiers lus ; artefacts : sous un dossier lu (par un lien), sous src/, relatif."""
    t = arbre(tmp_path)
    sain = t["racine"] / "registres" / "rapport-lecteur-a-v1.md"
    assert jouer(args(t, autres=[sain])) == (0, ["conforme"])
    lien = t["hors"] / "vers-d2"
    lien.symlink_to(t["d2"], target_is_directory=True)
    code, lignes = jouer(args(t, autres=[lien / "rapport.md", t["racine"] / "src" / "rapport.md", "rapport.md"]))
    assert code == 1 and lignes[0] == "écarts : 3"
    assert any(l.startswith("autre : chemin résolu sous le dossier lu " + str(t["d2"])) for l in lignes)
    assert any(l.startswith("autre : chemin résolu sous <racine>/src") for l in lignes)
    assert "autre : chemin non absolu (rapport.md)" in lignes
