"""Idée 1.1, version 5 (étape 0 du 16 novembre, R-2976 : complément de la copie du v9 dans la vue) — essai d'égalité au
différentiel près : chaque fichier v5 (et `vue_v9_v2.py`) est exactement son fichier source (v4, ou `vue_v9_v1.py`),
auquel on applique, dans l'ordre, les couples « ancien → nouveau » déclarés, chacun avec son nombre exact d'occurrences
`n`, puis l'ajout de fin déclaré, d'après `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v5/couples-v4-vers-v5.json`.
Les fichiers sources sont inchangés."""
import json
from pathlib import Path

import pytest

from controle_ia.scellement import empreinte, lire_compagnon

RACINE_DEPOT = Path(__file__).resolve().parents[1]
COUPLES = RACINE_DEPOT / "docs/notes/organisme-idees-juge-v1/code-idee-1-1-v5/couples-v4-vers-v5.json"
DECL = json.loads(COUPLES.read_text(encoding="utf-8"))


def appliquer(texte: str, d: dict) -> str:
    for c in d["couples"]:
        assert texte.count(c["ancien"]) == c["n"] >= 1, c["ancien"][:80]
        texte = texte.replace(c["ancien"], c["nouveau"])
    return texte + d.get("ajout_fin", "")


def test_dix_fichiers_declares():
    assert len(DECL) == 10
    for cible, d in DECL.items():
        assert (cible.endswith("_v5.py") and d["source"].endswith("_v4.py")) or (cible.endswith("vue_v9_v2.py") and d["source"].endswith("vue_v9_v1.py"))


@pytest.mark.parametrize("cible", sorted(DECL))
def test_egal_a_la_source_au_differentiel_pres(cible):
    d = DECL[cible]
    src = RACINE_DEPOT / d["source"]
    assert empreinte(src) == lire_compagnon(Path(str(src) + ".sha256"), src.name)     # source intacte (R12)
    assert (RACINE_DEPOT / cible).read_text(encoding="utf-8") == appliquer(src.read_text(encoding="utf-8"), d)
