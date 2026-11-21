"""Idée 1.1, version 2 (contre-lecture du code `8def0cf5…`) — essai d'égalité au différentiel près : chaque fichier v2 est
exactement son fichier v1, auquel on applique, dans l'ordre, les couples « ancien → nouveau » déclarés (chaque ancien
présent une seule fois) et l'ajout de fin déclaré, d'après `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v2/couples-v1-vers-v2.json`.
Les fichiers v1 sont inchangés (empreinte égale à leur compagnon)."""
import json
from pathlib import Path

import pytest

from controle_ia.scellement import empreinte, lire_compagnon

RACINE_DEPOT = Path(__file__).resolve().parents[1]
COUPLES = RACINE_DEPOT / "docs/notes/organisme-idees-juge-v1/code-idee-1-1-v2/couples-v1-vers-v2.json"
DECL = json.loads(COUPLES.read_text(encoding="utf-8"))


def appliquer(texte: str, d: dict) -> str:
    for c in d["couples"]:
        assert texte.count(c["ancien"]) == 1, c["ancien"][:80]
        texte = texte.replace(c["ancien"], c["nouveau"])
    return texte + d.get("ajout_fin", "")


def test_treize_fichiers_v2_declares():
    assert len(DECL) == 13
    assert all(v2.endswith("_v2.py") and d["source"].endswith("_v1.py") for v2, d in DECL.items())


@pytest.mark.parametrize("v2", sorted(DECL))
def test_v2_egal_a_v1_au_differentiel_pres(v2):
    d = DECL[v2]
    src = RACINE_DEPOT / d["source"]
    assert empreinte(src) == lire_compagnon(Path(str(src) + ".sha256"), src.name)     # v1 intact (R12)
    assert (RACINE_DEPOT / v2).read_text(encoding="utf-8") == appliquer(src.read_text(encoding="utf-8"), d)
