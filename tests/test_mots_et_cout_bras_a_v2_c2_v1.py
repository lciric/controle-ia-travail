"""Essai de complément de la base « mots et coût » du bras A, version 2 — filtre de la correction C2 — v1.

Fichier neuf (R12) : `tests/test_mots_et_cout_bras_a_v2.py` (`76e1e772…`) est scellé et reste tel quel ; la pièce
`scripts/mots_et_cout_bras_a_v2.py` (`db124c6e…`) ne change pas. Ce fichier ajoute l'essai que donne la vérification courte
`docs/notes/bras-a-moniteurs-v1/verification-courte-code-base-mots-et-cout-bras-a-v2-v1.md` (`384b8088…`), partie 4, recopié à
la lettre : il lit la liste `doses_detectees_sans_controle` que rend le code, dans le calcul entier, au lieu de recopier
son filtre. Les aides et les données factices sont celles du fichier d'essais de la version 2, importé sans le changer.

Second essai : la forme de l'inscription. `ecrire-fichier-code` ne cite que `FICHIERS_ESSAIS` ; ce fichier s'ajoute à la clé
`essais` du fichier d'inscription, avant son scellement, sans toucher la pièce : `lire_fichier_code` admet toute entrée
{chemin: sha256} sous `essais`, et `controler_code` vérifie chacune au commit cité.

Essais ciblés (jamais la suite complète) :
    PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_mots_et_cout_bras_a_v2_c2_v1.py
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import sys
from pathlib import Path

import pytest

ICI = Path(__file__).resolve()
RACINE = ICI.parents[1]
CE_FICHIER = "tests/test_mots_et_cout_bras_a_v2_c2_v1.py"
ESSAIS_V2 = RACINE / "tests" / "test_mots_et_cout_bras_a_v2.py"


def _charger(nom: str, chemin: Path):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


t2 = _charger("essais_mots_et_cout_bras_a_v2_aides", ESSAIS_V2)
mc, M, contexte, _lecture = t2.mc, t2.M, t2.contexte, t2._lecture
base_factice, lues = t2.base_factice, t2.lues                 # fixtures du fichier de la version 2 (données factices)


def test_c2_doses_sans_controle_filtrees_dans_le_calcul(lues, monkeypatch):
    """C2 dans le calcul entier : seule la dose où la base sur le sac de mots est décisive ET détecte est nommée."""
    haut, bas = _lecture(0.90, 0.85, 0.55), _lecture(0.60, 0.50, 0.56)
    construits = {"dose-0.25": (bas, _lecture(0.65, 0.50, 0.56)),        # sac de mots décisif, échoue : non nommée
                  "dose-0.50": (bas, haut),                               # sac de mots décisif, détecte : nommée
                  "dose-0.75": (haut, bas),                               # traits du texte décisifs, détecte : non nommée
                  "dose-1.00": (haut, _lecture(0, 0, 0, False, "vocabulaire vide"))}   # non calculable : non nommée
    origine, ordre = mc.etat_dose_bras_a, iter(mc.DOSES)
    monkeypatch.setattr(mc, "etat_dose_bras_a", lambda ra, rb, n: origine(*construits[next(ordre)], n))
    docs = mc.calculer(contexte(lues[1]["donnees"], n_tirages=5, n_perm=5))
    assert docs["issue"]["controle_adaptateur"]["doses_detectees_sans_controle"] == ["dose-0.50"]


def test_ce_fichier_se_cite_a_l_inscription_sans_changer_la_piece(tmp_path):
    """Cas sain : ce fichier, ajouté à la clé `essais` du fichier d'inscription qu'écrit `ecrire-fichier-code`, est lu et
    vérifié au commit cité par la pièce telle quelle. Artefact : une empreinte fausse pour ce fichier est refusée."""
    assert mc.FICHIERS_PIECE[0] == "scripts/mots_et_cout_bras_a_v2.py" and CE_FICHIER not in mc.FICHIERS_ESSAIS
    assert hashlib.sha256((RACINE / mc.FICHIERS_PIECE[0]).read_bytes()).hexdigest() == \
        "db124c6e29edf2e3547bf9b9f13c9fe311f0f53061baa997765efc30c429ebc1"                # la pièce n'est pas touchée
    r = t2.depot_jouet(tmp_path / "depot", avec_code=True)
    (r / "tests").mkdir()
    for p in (CE_FICHIER, "tests/test_mots_et_cout_bras_a_v2.py"):
        shutil.copy2(RACINE / p, r / p)
    t2.git(r, "add", "-A")
    t2.git(r, "commit", "-q", "-m", "essais")
    commit = t2.git(r, "rev-parse", "HEAD").strip()
    code = r / mc.DOSSIER_CODE / "CODE-MOTS-ET-COUT-BRAS-A-v2.json"
    mc.ecrire_fichier_code(r, commit, code, r / t2.CONTRE_LECTURE)
    d = json.loads(code.read_text(encoding="utf-8"))
    assert CE_FICHIER not in d["essais"] and "tests/test_mots_et_cout_bras_a_v2.py" in d["essais"]
    sha = hashlib.sha256(ICI.read_bytes()).hexdigest()

    def inscrire(empreinte: str) -> dict:                                 # le geste de l'inscription : une entrée de plus
        d["essais"][CE_FICHIER] = empreinte
        code.write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        s = hashlib.sha256(code.read_bytes()).hexdigest()
        Path(str(code) + ".sha256").write_text(f"{s}  {code.name}\n", encoding="utf-8")
        return {"cle": mc.CLES_LIGNES["code"], "date": "2026-11-19T00:00:00Z", "chemin": str(code.relative_to(r)), "sha256": s}

    copie = _charger(f"mc_bras_a_v2_c2_depot_{abs(hash(str(r)))}", r / mc.FICHIERS_PIECE[0])
    rep = copie.controler_code(r, inscrire(sha))
    assert rep["essais"][CE_FICHIER] == sha and rep["commit"] == commit
    with pytest.raises(copie.ArretPiece, match="empreintes différentes"):
        copie.controler_code(r, inscrire("0" * 64))
