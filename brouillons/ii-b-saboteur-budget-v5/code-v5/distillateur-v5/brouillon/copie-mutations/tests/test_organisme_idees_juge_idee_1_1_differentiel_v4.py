"""Idée 1.1, version 4 (contrôle du différentiel v2 → v3, `02f4a1d7…`) — essai d'égalité au différentiel près : chaque
fichier v4 est exactement son fichier v3, auquel on applique, dans l'ordre, les couples « ancien → nouveau » déclarés
(chaque ancien présent une seule fois) et l'ajout de fin déclaré, d'après
`docs/notes/organisme-idees-juge-v1/code-idee-1-1-v4/couples-v3-vers-v4.json`. Les fichiers v3 sont inchangés."""
import json
from pathlib import Path

import pytest

from controle_ia.scellement import empreinte, lire_compagnon

RACINE_DEPOT = Path(__file__).resolve().parents[1]
COUPLES = RACINE_DEPOT / "docs/notes/organisme-idees-juge-v1/code-idee-1-1-v4/couples-v3-vers-v4.json"
DECL = json.loads(COUPLES.read_text(encoding="utf-8"))


def appliquer(texte: str, d: dict) -> str:
    for c in d["couples"]:
        assert texte.count(c["ancien"]) == 1, c["ancien"][:80]
        texte = texte.replace(c["ancien"], c["nouveau"])
    return texte + d.get("ajout_fin", "")


def test_treize_fichiers_v4_declares():
    assert len(DECL) == 13
    assert all(v4.endswith("_v4.py") and d["source"].endswith("_v3.py") for v4, d in DECL.items())


@pytest.mark.parametrize("v4", sorted(DECL))
def test_v4_egal_a_v3_au_differentiel_pres(v4):
    d = DECL[v4]
    src = RACINE_DEPOT / d["source"]
    assert empreinte(src) == lire_compagnon(Path(str(src) + ".sha256"), src.name)     # v3 intact (R12)
    assert (RACINE_DEPOT / v4).read_text(encoding="utf-8") == appliquer(src.read_text(encoding="utf-8"), d)
