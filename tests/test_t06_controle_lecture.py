"""Contrôle d'ouverture de la lecture des sondes de T0.6 (R-1654) : cas sain et artefacts (R5)."""
from __future__ import annotations

import hashlib
import importlib.util
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
SCRIPT, SH = RACINE / "scripts" / "controle_lecture_t06_v1.py", RACINE / "scripts" / "controle_lecture_t06_v1.sh"
spec = importlib.util.spec_from_file_location("controle_lecture", SCRIPT)
cl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cl)
T0 = int(datetime(2026, 11, 12, 12, 0, 0, tzinfo=timezone.utc).timestamp())          # instant d'ouverture des essais
Z = lambda s: datetime.fromtimestamp(s, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sceller(f: Path) -> str:
    sha = hashlib.sha256(f.read_bytes()).hexdigest()
    Path(str(f) + ".sha256").write_text(f"{sha}  {f.name}\n", encoding="utf-8")
    return sha


def monde(tmp_path: Path):
    for d in ("prereg", "registres", "diag"):
        (tmp_path / d).mkdir(parents=True)
    t07, p3b, res = tmp_path / "prereg" / "T0.7.md", tmp_path / "prereg" / "P3-bis.md", tmp_path / "diag" / "lecture-sondes-t06.json"
    t07.write_text("t07", encoding="utf-8")
    p3b.write_text("p3bis", encoding="utf-8")
    res.write_text("CONTENU_QUE_LE_CONTROLE_NE_LIT_PAS", encoding="utf-8")
    reg = tmp_path / "registres" / "lectures.md"
    ecrire_registre(reg, sceller(t07), sceller(p3b))
    sceller(res)
    return reg, res, t07, p3b


def ecrire_registre(reg, sha7, shb, d7=None, db=None, extra=""):
    reg.write_text(f"| SCELLEMENT-T07 | {d7 or Z(T0 - 7200)} | prereg/T0.7.md | {sha7} |\n| SCELLEMENT-P3BIS | {db or Z(T0 - 3600)} | prereg/P3-bis.md | {shb} |\n{extra}", encoding="utf-8")


def test_cas_sain_autorise_et_journalise(tmp_path):
    reg, res, *_ = monde(tmp_path)
    sortie = cl.controler(reg, res, tmp_path, T0)
    assert sortie.startswith("OUVERTURE AUTORISÉE") and "SCELLEMENT-T07" in sortie and "SCELLEMENT-P3BIS" in sortie
    j = Path(str(reg) + ".ouvertures.md").read_text(encoding="utf-8")
    assert Z(T0) in j and "lecture-sondes-t06.json" in j and hashlib.sha256(res.read_bytes()).hexdigest() in j
    cl.controler(reg, res, tmp_path, T0 + 5)                                              # chaque ouverture est journalisée
    assert Path(str(reg) + ".ouvertures.md").read_text(encoding="utf-8").count("OUVERTURE-SONDES-T06") == 2


def test_cli_et_script_shell(tmp_path):
    reg, res, t07, p3b = monde(tmp_path)
    ecrire_registre(reg, sceller(t07), sceller(p3b), "2026-01-01T00:00:00Z", "2026-01-02T00:00:00Z")      # dates passées pour l'instant réel
    r = subprocess.run(["bash", str(SH), str(reg), str(res), str(tmp_path)], capture_output=True, text=True, timeout=60)
    assert r.returncode == 0 and "OUVERTURE AUTORISÉE" in r.stdout, r.stdout + r.stderr
    (tmp_path / "prereg" / "T0.7.md").write_text("altéré", encoding="utf-8")
    r = subprocess.run(["bash", str(SH), str(reg), str(res), str(tmp_path)], capture_output=True, text=True, timeout=60)
    assert r.returncode == 2 and r.stdout.startswith("REFUS")
    assert subprocess.run(["bash", str(SH), str(reg)], capture_output=True, text=True).returncode == 2           # usage


def _refus(tmp_path, motif, modif):
    reg, res, t07, p3b = monde(tmp_path)
    modif(reg, res, t07, p3b)
    with pytest.raises(cl.Refus, match=motif):
        cl.controler(reg, res, tmp_path, T0)
    assert not Path(str(reg) + ".ouvertures.md").exists()                                # rien n'est journalisé ni ouvert


def test_artefacts_registre(tmp_path):
    _refus(tmp_path / "a", "absent", lambda reg, *_: reg.unlink())
    _refus(tmp_path / "b", "0 ligne\\(s\\) SCELLEMENT-P3BIS", lambda reg, *_: reg.write_text(reg.read_text(encoding="utf-8").splitlines()[0] + "\n", encoding="utf-8"))
    _refus(tmp_path / "c", "2 ligne\\(s\\) SCELLEMENT-T07", lambda reg, *_: reg.write_text(reg.read_text(encoding="utf-8") + reg.read_text(encoding="utf-8").splitlines()[0] + "\n", encoding="utf-8"))
    _refus(tmp_path / "d", "date", lambda reg, *_: ecrire_registre(reg, sceller(tmp_path / "d" / "prereg" / "T0.7.md"), sceller(tmp_path / "d" / "prereg" / "P3-bis.md"), d7="2026-11-10 09:00"))
    _refus(tmp_path / "e", "empreinte", lambda reg, *_: ecrire_registre(reg, "abc", "def"))
    _refus(tmp_path / "f", "chemin", lambda reg, *_: reg.write_text(reg.read_text(encoding="utf-8").replace("prereg/T0.7.md", "../T0.7.md"), encoding="utf-8"))
    _refus(tmp_path / "g", "mal formée", lambda reg, *_: reg.write_text("| SCELLEMENT-T07 | x |\n| SCELLEMENT-P3BIS | y |\n", encoding="utf-8"))


def test_artefacts_sceaux_et_fichiers(tmp_path):
    _refus(tmp_path / "a", "empreinte .* ≠ celle du registre", lambda reg, res, t07, p3b: (t07.write_text("modifié", encoding="utf-8"), sceller(t07)))   # sceau refait sur un autre fichier : le registre garde l'ancienne empreinte
    _refus(tmp_path / "b", "compagnon .sha256", lambda reg, res, t07, p3b: Path(str(p3b) + ".sha256").write_text("0" * 64 + "\n", encoding="utf-8"))
    _refus(tmp_path / "c", "compagnon .sha256 absent", lambda reg, res, t07, p3b: Path(str(t07) + ".sha256").unlink())
    _refus(tmp_path / "d", "absent", lambda reg, res, t07, p3b: p3b.unlink())
    _refus(tmp_path / "e", "compagnon .sha256 absent", lambda reg, res, t07, p3b: Path(str(res) + ".sha256").unlink())
    _refus(tmp_path / "f", "compagnon .sha256", lambda reg, res, t07, p3b: res.write_text("autre résultat", encoding="utf-8"))
    _refus(tmp_path / "g", "absent", lambda reg, res, t07, p3b: res.unlink())


def test_artefacts_anteriorite(tmp_path):
    def ecrire(tp, d7=None, db=None):
        return lambda reg, res, t07, p3b: ecrire_registre(reg, hashlib.sha256(t07.read_bytes()).hexdigest(), hashlib.sha256(p3b.read_bytes()).hexdigest(), d7, db)
    _refus(tmp_path / "a", "strictement antérieure", ecrire(tmp_path / "a", d7=Z(T0)))                 # même seconde : refus
    _refus(tmp_path / "b", "strictement antérieure", ecrire(tmp_path / "b", db=Z(T0 + 60)))             # inscrite après l'ouverture
    reg, res, *_ = monde(tmp_path / "c")
    with pytest.raises(cl.Refus, match="strictement antérieure"):
        cl.controler(reg, res, tmp_path / "c", T0 - 4000)                                             # ouverture avant l'inscription de P3-bis
    assert cl.controler(reg, res, tmp_path / "c", T0).startswith("OUVERTURE AUTORISÉE")
