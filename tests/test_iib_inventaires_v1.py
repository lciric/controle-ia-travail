"""(ii-b), inventaires v1 : les fonctions neuves de `src/controle_ia/iib/` que les inventaires existants trouvent (constructeurs d'invite et
lecteurs de la clé `cibles` de `tests/test_cibles_invisibles_v3.py`, liste fermée sur `main`) sont examinées ici, une à une, avec leur
raison ; l'essai v3 lui-même n'est pas modifié (il les nomme, déclaré au rapport du développeur). Aucun module de
`src/controle_ia/` hors de `iib/` n'importe `controle_ia.iib`. Le lanceur n'importe directement ni `bases`, ni `sondes`, ni `t07`, ni
`environnements.juges`. Artefact (R5) : une fonction neuve plantée dans `iib/` qui construit une invite fait échouer l'inventaire."""
from __future__ import annotations

import ast
import json
import re
from pathlib import Path

import pytest

import test_cibles_invisibles_v3 as v3

RACINE = Path(__file__).resolve().parents[1]
SRC = RACINE / "src"
COUVERT, EXEMPT = v3.COUVERT, v3.EXEMPT
INVISIBLE = "tests/test_iib_consigne_invisible_v1.py (marqueurs de la consigne et des cibles, répétition jouet)"
# Registre des constructeurs d'invite de (ii-b) : chaque tâche n'entre dans une invite que par `pilote_a.tache_de` (énoncé et
# classification) ; l'essai à marqueur les conduit tous, de la tâche (cibles marquées) à l'invite, et balaie les fichiers écrits.
REGISTRE_IIB = {
    "controle_ia/iib/consigne_v1.py::environnement_maitre": (COUVERT, INVISIBLE),
    "controle_ia/iib/episodes_v1.py::jouer_lot": (COUVERT, INVISIBLE),
    "controle_ia/iib/lanceur_v1.py::_apres_manifeste": (COUVERT, INVISIBLE),
    "controle_ia/iib/lanceur_v1.py::_debut_de_controle": (COUVERT, INVISIBLE + " ; contexte de contrôle d'identité, environnement honnête"),
    "controle_ia/iib/lanceur_v1.py::charger_entrees": (EXEMPT, "charge le guide de classification H1 (invite scellée, sans tâche)"),
    "controle_ia/iib/lanceur_v1.py::env_de": (COUVERT, INVISIBLE),
    "controle_ia/iib/lanceur_v1.py::env_honnete": (COUVERT, INVISIBLE),
    "controle_ia/iib/modele_v1.py::ModeleTorch.generer_actions": (COUVERT, INVISIBLE + " ; contextes reçus de jouer_lot"),
    "controle_ia/iib/modele_v1.py::ModeleTorch.suites": (COUVERT, INVISIBLE + " ; préfixes reçus de oracle_episode"),
    "controle_ia/iib/oracle_v1.py::oracle_episode": (COUVERT, INVISIBLE + " ; tests/test_iib_oracle_v1.py (espion des contextes)"),
}
# FAUX LECTEURS de la clé `cibles` : la configuration d'un adaptateur LoRA (`config["adaptateur"]["cibles"]`, modules de projection) et
# la fabrique des tâches factices du monde jouet ; aucune ne lit la référence cachée d'une tâche.
LECTEURS_IIB = {
    "controle_ia/iib/configuration_v1.py": {"exiger_config_iib_v1"},
    "controle_ia/iib/jouet_v1.py": {"taches_factices", "config_jouet"},
    "controle_ia/iib/lanceur_v1.py": {"_apres_manifeste"},
}


def _iib(d: dict) -> dict:
    return {k: v for k, v in d.items() if k.startswith("controle_ia/iib/")}


def test_inventaire_des_constructeurs_de_iib_tous_examines():
    trouves = _iib(v3._constructeurs())
    assert set(trouves) - set(REGISTRE_IIB) == set(), sorted(set(trouves) - set(REGISTRE_IIB))
    assert set(REGISTRE_IIB) - set(trouves) == set(), sorted(set(REGISTRE_IIB) - set(trouves))
    assert all(s in (COUVERT, EXEMPT) and r for s, r in REGISTRE_IIB.values())


def test_les_seuls_lecteurs_de_cibles_de_iib_sont_des_faux_lecteurs():
    lecteurs = {}
    for rel, f in v3._modules():
        if not rel.startswith("controle_ia/iib/"):
            continue
        for nom, n in v3._fonctions(f):
            if any(isinstance(m, ast.Constant) and m.value in v3.CLES_CACHEES for m in ast.walk(n)):
                lecteurs.setdefault(rel, set()).add(nom)
    assert lecteurs == LECTEURS_IIB


def test_preuve_la_cle_cibles_du_lanceur_est_celle_de_l_adaptateur():
    arbre = ast.parse((SRC / "controle_ia" / "iib" / "lanceur_v1.py").read_text(encoding="utf-8"))
    lectures = [n for n in ast.walk(arbre) if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant) and n.slice.value == "cibles"]
    assert lectures and all(isinstance(n.value, ast.Name) and n.value.id == "a" for n in lectures)     # a = config["adaptateur"]
    from controle_ia.iib import configuration_v1 as cf
    assert cf.TEXTE["adaptateur"]["cibles"] == ["q_proj", "k_proj", "v_proj", "o_proj"]


def test_artefact_un_constructeur_plante_dans_iib_est_vu(tmp_path, monkeypatch):
    plante = tmp_path / "controle_ia" / "iib"
    plante.mkdir(parents=True)
    (plante / "plante_v1.py").write_text("def invite(tache, fmt):\n    return fmt.ouverture(str(tache['cibles']), 'x')\n", encoding="utf-8")
    monkeypatch.setattr(v3, "SRC", tmp_path)
    trouves = _iib(v3._constructeurs())
    assert "controle_ia/iib/plante_v1.py::invite" in trouves and set(trouves) - set(REGISTRE_IIB)


def test_aucun_module_hors_de_iib_n_importe_controle_ia_iib():
    hors = []
    for f in sorted((SRC / "controle_ia").rglob("*.py")):
        rel = f.relative_to(SRC).as_posix()
        if rel.startswith("controle_ia/iib/"):
            continue
        texte = f.read_text(encoding="utf-8")
        if re.search(r"controle_ia\.iib|from \.+iib\b|from \.\. import iib|from \. import iib", texte):
            hors.append(rel)
    assert hors == []


def test_le_lanceur_et_la_regle_n_importent_directement_aucun_moniteur():
    interdits = ("bases", "sondes", "t07", "environnements.juges")
    for nom in ("lanceur_v1.py", "regle_v1.py", "tours_v1.py", "oracle_v1.py", "episodes_v1.py", "modele_v1.py"):
        arbre = ast.parse((SRC / "controle_ia" / "iib" / nom).read_text(encoding="utf-8"))
        modules = {n.module or "" for n in ast.walk(arbre) if isinstance(n, ast.ImportFrom)}
        modules |= {a.name for n in ast.walk(arbre) if isinstance(n, ast.Import) for a in n.names}
        assert not [m for m in modules if any(m.lstrip(".").startswith(i) or f".{i}" in m for i in interdits)], (nom, modules)


def test_la_liste_ciblee_de_iib_existe_et_couvre_les_essais_de_iib():
    liste = RACINE / "scripts" / "tests-cibles-iib-v1.txt"
    noms = liste.read_text(encoding="utf-8").split()
    sur_disque = sorted(p.relative_to(RACINE).as_posix() for p in (RACINE / "tests").glob("test_iib_*_v1.py"))
    assert noms == sur_disque and all(re.fullmatch(r"tests/test_[A-Za-z0-9_]+\.py", n) for n in noms)
    assert json.dumps(noms)
