"""Idée 1.1, version 3 (vérification du différentiel `549e4597…`) — essai d'égalité au différentiel près : chaque fichier v3 est
exactement son fichier v2, auquel on applique, dans l'ordre, les couples « ancien → nouveau » déclarés (chaque ancien
présent une seule fois) et l'ajout de fin déclaré, d'après `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v3/couples-v2-vers-v3.json`.
Les fichiers v2 sont inchangés (empreinte égale à leur compagnon)."""
import json
from pathlib import Path

import pytest

from controle_ia.scellement import empreinte, lire_compagnon

RACINE_DEPOT = Path(__file__).resolve().parents[1]
COUPLES = RACINE_DEPOT / "docs/notes/organisme-idees-juge-v1/code-idee-1-1-v3/couples-v2-vers-v3.json"
DECL = json.loads(COUPLES.read_text(encoding="utf-8"))


def appliquer(texte: str, d: dict) -> str:
    for c in d["couples"]:
        assert texte.count(c["ancien"]) == 1, c["ancien"][:80]
        texte = texte.replace(c["ancien"], c["nouveau"])
    return texte + d.get("ajout_fin", "")


def test_douze_fichiers_v3_declares():
    assert len(DECL) == 12
    assert all(v3.endswith("_v3.py") and d["source"].endswith("_v2.py") for v3, d in DECL.items())


@pytest.mark.parametrize("v2", sorted(DECL))
def test_v2_egal_a_v1_au_differentiel_pres(v2):
    d = DECL[v2]
    src = RACINE_DEPOT / d["source"]
    assert empreinte(src) == lire_compagnon(Path(str(src) + ".sha256"), src.name)     # v1 intact (R12)
    assert (RACINE_DEPOT / v2).read_text(encoding="utf-8") == appliquer(src.read_text(encoding="utf-8"), d)
