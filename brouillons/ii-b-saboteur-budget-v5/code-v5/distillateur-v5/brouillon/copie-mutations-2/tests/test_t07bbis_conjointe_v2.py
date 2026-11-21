"""G. Table conjointe v2 : deux lignes CODE-BBIS acceptées (majeur M1, contre-lecture code v4 tour 1).

- G1 : cas sain — registre à deux lignes CODE-BBIS, la garde passe complètement.
- G2 : artefact — trois lignes CODE-BBIS, refus (GardeArret mentionnant CODE-BBIS).
- G3 : artefact — seconde ligne CODE-BBIS non postérieure à la première, refus.
"""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t07bbis import conjointe_v2 as cv2
from controle_ia.t07bbis import registre_bbis_v1 as rb1


# ---------------------------------------------------------------------------------------------------- auxiliaires


def _t(date: str) -> int:
    return int(datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())


def _l(cle: str, date: str, chemin: str = "registres/x.json", sha: str = "a" * 64) -> str:
    return f"| {cle} | {date} | {chemin} | {sha} |\n"


def _sceau(parent: Path, nom: str, contenu: str = "{}") -> tuple[str, str]:
    """Crée fichier + compagnon .sha256 dans parent ; rend (nom, sha256)."""
    parent.mkdir(parents=True, exist_ok=True)
    p = parent / nom
    p.write_text(contenu, encoding="utf-8")
    sha = hashlib.sha256(p.read_bytes()).hexdigest()
    (parent / (nom + ".sha256")).write_text(f"{sha}  {nom}\n", encoding="utf-8")
    return nom, sha


def _env_sain(tmp_path: Path) -> tuple[Path, str, str]:
    """Prépare une racine avec toutes les pièces pour gardes_conjointe : deux lignes CODE-BBIS."""
    reg_dir = tmp_path / "registres"
    _, sha_lec = _sceau(reg_dir, "lecture-bbis.json")
    _, sha_ver = _sceau(reg_dir, "verdict-bbis.json")
    diag_t07 = tmp_path / "diag" / "run-t07"
    diag_vb = tmp_path / "diag" / "run-b"
    _sceau(diag_t07, "lecture-t07.json")
    _sceau(diag_vb, "verdict-b.json")

    reg = (
        "# registre\n\n"
        + _l("SCELLEMENT-BBIS", "2026-11-14T12:30:30Z")
        + _l("CODE-BBIS",       "2026-11-16T12:57:51Z", "registres/x.json")
        + _l("GO-BBIS",         "2026-11-16T13:00:00Z")
        + _l("CODE-BBIS",       "2026-11-17T09:00:00Z", "registres/x.json")
        + _l("LECTURE-BBIS",    "2026-11-17T10:00:00Z", "registres/lecture-bbis.json", sha_lec)
        + _l("VERDICT-BBIS",    "2026-11-17T11:00:00Z", "registres/verdict-bbis.json", sha_ver)
    )
    (reg_dir / "t07-etape-b-bis-v1.md").write_text(reg, encoding="utf-8")
    return tmp_path, "diag/run-t07/lecture-t07.json", "diag/run-b/verdict-b.json"


# ---------------------------------------------------------------------------------------------------- G. gardes_conjointe


def test_G1_deux_code_bbis_garde_passe(tmp_path):
    racine, chemin_t07, chemin_vb = _env_sain(tmp_path)
    r = cv2.gardes_conjointe(racine, chemin_t07, chemin_vb)
    assert "lecture_bbis" in r and "verdict_bbis" in r
    assert r["lecture_bbis"]["chemin"] == "registres/lecture-bbis.json"
    assert r["verdict_bbis"]["chemin"] == "registres/verdict-bbis.json"


def test_G2_trois_code_bbis_refus(tmp_path):
    reg_dir = tmp_path / "registres"
    reg_dir.mkdir(parents=True, exist_ok=True)
    reg = (
        "# registre\n\n"
        + _l("SCELLEMENT-BBIS", "2026-11-14T12:30:30Z")
        + _l("CODE-BBIS",       "2026-11-16T12:57:51Z")
        + _l("GO-BBIS",         "2026-11-16T13:00:00Z")
        + _l("CODE-BBIS",       "2026-11-17T09:00:00Z")
        + _l("CODE-BBIS",       "2026-11-17T10:00:00Z")
        + _l("LECTURE-BBIS",    "2026-11-17T11:00:00Z")
        + _l("VERDICT-BBIS",    "2026-11-17T12:00:00Z")
    )
    (reg_dir / "t07-etape-b-bis-v1.md").write_text(reg, encoding="utf-8")
    with pytest.raises(GardeArret, match="CODE-BBIS"):
        cv2.gardes_conjointe(tmp_path, "lecture-t07.json", "verdict-b.json")


def test_G3_seconde_code_bbis_non_posterieure_refus(tmp_path):
    reg_dir = tmp_path / "registres"
    reg_dir.mkdir(parents=True, exist_ok=True)
    reg = (
        "# registre\n\n"
        + _l("SCELLEMENT-BBIS", "2026-11-14T12:30:30Z")
        + _l("CODE-BBIS",       "2026-11-16T13:00:00Z")
        + _l("GO-BBIS",         "2026-11-16T13:00:00Z")
        + _l("CODE-BBIS",       "2026-11-16T12:57:51Z")   # antérieure à la première : refus
        + _l("LECTURE-BBIS",    "2026-11-17T10:00:00Z")
        + _l("VERDICT-BBIS",    "2026-11-17T11:00:00Z")
    )
    (reg_dir / "t07-etape-b-bis-v1.md").write_text(reg, encoding="utf-8")
    with pytest.raises(GardeArret, match="CODE-BBIS"):
        cv2.gardes_conjointe(tmp_path, "lecture-t07.json", "verdict-b.json")
