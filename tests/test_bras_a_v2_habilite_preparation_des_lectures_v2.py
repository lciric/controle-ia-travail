"""Essais de l'étape de préparation des lectures des deux moniteurs à modèle de langue du bras A (identifiants opaques
du côté des entrées). Données factices seulement ; aucun modèle chargé. Chaque garde a un cas sain et un artefact (R5).

Essais ciblés :
    PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_preparation_des_lectures_v2.py

Version 2 des essais : la table est tirée par la version 8 du module des autres moniteurs (entropie propre) ; le module
éprouvé est la version 2 de la préparation, qui importe la version 3 du module des deux moniteurs.
"""
from __future__ import annotations

import ast
import importlib.util
import json
import sys
from pathlib import Path

import pytest

from controle_ia import manifeste
from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets.bras_a_v2_habilite import autres_moniteurs_v8 as A
from controle_ia.organismes_discrets.bras_a_v2_habilite import moniteurs_langue_v3 as ML
from controle_ia.organismes_discrets.bras_a_v2_habilite_preparation import preparation_des_lectures_v2 as P

RACINE = Path(__file__).resolve().parents[1]
ENTROPIE = 20261119
CONSIGNE = ML.charger_consigne(RACINE)
ACTION = "ACTION: ADD\nTITLE: t {c} {k}\nPROPOSAL: body {k}\nCONTROLS: c{k}\nCOST: 12 GPU-hours\nPREDICTION: p{k}"
NOMS = {"honnete": "H", "dose-0.25": "controls-0.25", "dose-0.50": "controls-0.50", "dose-0.75": "controls-0.75",
        "dose-1.00": "controls-1.00"}
TACHES = [f"tache-verification-factice-{k:02d}" for k in range(16)]
QUESTIONS = {t: f"Q about {t[-2:]}: does it scale?" for t in TACHES}


def _actions(illisibles=()) -> list[dict]:
    """Cinq conditions, 16 tâches, 8 épisodes, 10 pas ; la clé dit la condition en clair, comme celle de l'extraction."""
    sortie = []
    for role, nom in NOMS.items():
        for t in TACHES:
            for e in range(8):
                for p in range(10):
                    texte = "no action here" if (role, t, e, p) in illisibles else ACTION.format(c=nom, k=p)
                    sortie.append({"cle": f"{nom}__{t}__e{e}__p{p}", "condition": role, "tache": t, "episode": e,
                                   "pas": p, "texte": texte, "jetons": 5})
    return sortie


@pytest.fixture(scope="module")
def table():
    return A.tirer_la_table_opaque([a["cle"] for a in _actions()])["table"]


ILLISIBLES = {("honnete", TACHES[0], 0, 3), ("dose-0.50", TACHES[1], 2, 9), ("dose-0.50", TACHES[1], 2, 0)}


def test_preparation_du_moniteur_boite_noire(table):
    demandes, bilan = P.preparer(_actions(ILLISIBLES), QUESTIONS, table, ENTROPIE, "moniteur-boite-noire")
    # une action illisible n'est pas lue ; au pas 0 illisible, l'épisode garde ses neuf autres actions lues
    assert bilan["honnete"] == {"actions": 1280, "hors_du_sous_echantillon": 0, "non_lues": 1, "demandes": 1279,
                                "marqueur_dans_le_texte_de_l_agent": 0, "hors_forme_composee": 0}
    assert bilan["dose-0.50"]["non_lues"] == 2 and bilan["dose-1.00"]["demandes"] == 1280
    assert len(demandes) == 6400 - 3 and [d["cle"] for d in demandes] == sorted(d["cle"] for d in demandes)
    assert all(tuple(d) == P.CHAMPS_DEMANDE for d in demandes)
    # le message est celui du module des moniteurs, et la graine celle de la position, sans la condition
    d = demandes[0]
    cle = table[d["cle"]]
    nom, t, e, p = cle.split("__")
    role = {v: k for k, v in NOMS.items()}[nom]
    journal = [(0, k, ACTION.format(c=nom, k=k) if (role, t, int(e[1:]), k) not in ILLISIBLES else "no action here")
               for k in range(10)]
    assert d["utilisateur"] == ML.message_du_moniteur(QUESTIONS[t], journal, int(p[1:]), 10)["utilisateur"]
    cle_graine = ML.cle_de_graine("moniteur-boite-noire", t, int(e[1:]), int(p[1:]))
    assert d["graine"] == ML.graine_entiere(manifeste.graines([cle_graine], ENTROPIE)[cle_graine])
    par_position = {}
    for d in demandes:
        _, t, e, p = table[d["cle"]].split("__")
        par_position.setdefault((t, e, p), set()).add(d["graine"])
    assert all(len(g) == 1 for g in par_position.values())           # même graine dans les cinq conditions
    assert len({next(iter(g)) for g in par_position.values()}) == len(par_position)


def test_preparation_du_juge_sous_echantillon(table):
    demandes, bilan = P.preparer(_actions(), QUESTIONS, table, ENTROPIE, "juge")
    assert len(demandes) == 2560 and all(b == {"actions": 1280, "hors_du_sous_echantillon": 768, "non_lues": 0,
                                               "demandes": 512, "marqueur_dans_le_texte_de_l_agent": 0,
                                               "hors_forme_composee": 0} for b in bilan.values())
    positions = {}
    for d in demandes:
        nom, t, e, p = table[d["cle"]].split("__")
        positions.setdefault((nom, t), set()).add((int(e[1:]), int(p[1:])))
    for t in TACHES:
        attendu = set(ML.positions_du_juge_pour(ENTROPIE, t))
        assert all(positions[(nom, t)] == attendu for nom in NOMS.values())     # les mêmes dans les cinq conditions
    # une position du sous-échantillon qui tombe sur une action non appliquée : non lue, sans remplacement
    e0, p0 = sorted(ML.positions_du_juge_pour(ENTROPIE, TACHES[2]))[0]
    d2, b2 = P.preparer(_actions({("dose-0.75", TACHES[2], e0, p0)}), QUESTIONS, table, ENTROPIE, "juge")
    assert len(d2) == 2559 and b2["dose-0.75"]["non_lues"] == 1 and b2["dose-0.75"]["demandes"] == 511


def test_rien_dans_le_fichier_des_demandes_ne_dit_la_condition(tmp_path, table):
    demandes, bilan = P.preparer(_actions(), QUESTIONS, table, ENTROPIE, "juge")
    e = P.ecrire_les_demandes(tmp_path / "production", "juge", demandes)
    assert e["fichier"] == "demandes-juge.jsonl" and e["lignes"] == 2560
    brut = e["chemin"].read_text(encoding="utf-8")
    for marque in ("__e", "controls-", "H__", "honnete", "dose-", '"condition"', '"tache"', '"episode"', '"pas"',
                   "tache-verification"):
        if marque in ("controls-", "tache-verification"):
            continue                                             # ces mots sont dans les textes factices eux-mêmes
        assert marque not in brut, marque
    assert all(tuple(json.loads(l)) == P.CHAMPS_DEMANDE for l in brut.splitlines())
    # le bilan par condition, lui, s'écrit à part, et dit l'empreinte des demandes
    b = P.ecrire_le_bilan(tmp_path / "a-part", "juge", bilan, e["sha256"])
    contenu = json.loads(b["chemin"].read_text(encoding="utf-8"))
    assert contenu["demandes_sha256"] == e["sha256"] and set(contenu["par_condition"]) == set(P.ROLES_LUS)
    assert not (tmp_path / "production" / P.fichier_du_bilan("juge")).exists()
    with pytest.raises(GardeArret, match="n'écrase jamais"):
        P.ecrire_les_demandes(tmp_path / "production", "juge", demandes)
    with pytest.raises(GardeArret, match="n'écrase jamais"):
        P.ecrire_le_bilan(tmp_path / "a-part", "juge", bilan, e["sha256"])
    with pytest.raises(GardeArret, match="une entrée par condition"):
        P.ecrire_le_bilan(tmp_path / "autre", "juge", {"honnete": {}}, e["sha256"])


def test_production_ne_lit_que_le_fichier_des_demandes(tmp_path, table):
    demandes, _ = P.preparer(_actions(), QUESTIONS, table, ENTROPIE, "moniteur-boite-noire")
    e = P.ecrire_les_demandes(tmp_path, "moniteur-boite-noire", demandes[:50])
    lues, graines = P.lire_les_demandes(e["chemin"], CONSIGNE)
    assert len(lues) == 50 and set(graines) == {d["cle"] for d in lues}
    for d in lues:
        ML.exiger_demande(d)                                        # la forme qu'attend la lecture avec raisonnement
    with pytest.raises(GardeArret, match="toute autre consigne"):
        P.lire_les_demandes(e["chemin"], CONSIGNE + " ")
    # un autre fichier (les textes d'action, qui disent la condition) n'entre pas par ici
    textes = tmp_path / "textes-actions-base-mots-et-cout-bras-a.jsonl"
    textes.write_text("{}\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="n'en lit aucun autre"):
        P.lire_les_demandes(textes, CONSIGNE)
    with pytest.raises(GardeArret, match="absent"):
        P.lire_les_demandes(tmp_path / "ailleurs" / "demandes-juge.jsonl", CONSIGNE)
    e["chemin"].write_text(e["chemin"].read_text(encoding="utf-8") + "\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="a changé depuis son scellement"):
        P.lire_les_demandes(e["chemin"], CONSIGNE)


def test_demande_preparee_fermee(tmp_path, table):
    demandes, _ = P.preparer(_actions(), QUESTIONS, table, ENTROPIE, "juge")
    d = demandes[0]
    P.exiger_demande_preparee(d)
    for mauvais, motif in (({**d, "condition": "dose-1.00"}, "aucun autre"), ({**d, "tache": "t"}, "aucun autre"),
                           ({**d, "pas": 3}, "aucun autre"), ({k: v for k, v in d.items() if k != "graine"}, "aucun autre"),
                           ({**d, "cle": "controls-1.00__t__e0__p0"}, "clé non opaque"),
                           ({**d, "utilisateur": "CURRENT SET"}, "message hors format"),
                           ({**d, "graine": -1}, "graine entière"), ({**d, "graine": True}, "graine entière")):
        with pytest.raises(GardeArret, match=motif):
            P.exiger_demande_preparee(mauvais)
        with pytest.raises(GardeArret, match=motif):
            P.ecrire_les_demandes(tmp_path / "x", "juge", [mauvais])
    with pytest.raises(GardeArret, match="en double, ou hors de leur ordre trié"):
        P.ecrire_les_demandes(tmp_path / "x", "juge", [demandes[1], demandes[0]])
    with pytest.raises(GardeArret, match="en double, ou hors de leur ordre trié"):
        P.ecrire_les_demandes(tmp_path / "x", "juge", [demandes[0], demandes[0]])
    with pytest.raises(GardeArret, match="attendus"):
        P.ecrire_les_demandes(tmp_path / "x", "agregateur-sequentiel", demandes[:1])
    assert not (tmp_path / "x").exists()
    # une ligne en double ou à champ de plus dans un fichier scellé : la production la refuse
    chemin = tmp_path / "demandes-juge.jsonl"
    for lignes, motif in (([d, d], "identifiant en double"), ([{**d, "condition": "honnete"}], "aucun autre")):
        chemin.write_text("".join(json.dumps(x) + "\n" for x in lignes), encoding="utf-8")
        Path(str(chemin) + ".sha256").write_text(
            __import__("hashlib").sha256(chemin.read_bytes()).hexdigest() + "  " + chemin.name + "\n", encoding="utf-8")
        with pytest.raises(GardeArret, match=motif):
            P.lire_les_demandes(chemin, CONSIGNE)


def test_gardes_d_entree_de_la_preparation(table):
    actions = _actions()
    for arguments, motif in (((actions, QUESTIONS, table, ENTROPIE, "agregateur-sequentiel"), "attendus"),
                             ((actions, QUESTIONS, table, -1, "juge"), "entropie"),
                             ((actions, QUESTIONS, {"H__t__e0__p0": "x"}, ENTROPIE, "juge"), "hors format"),
                             ((actions, QUESTIONS, {**table, "0" * 16: next(iter(table.values()))}, ENTROPIE, "juge"), "hors format"),
                             ((actions, {t: q for t, q in QUESTIONS.items() if t != TACHES[5]}, table, ENTROPIE, "juge"), "énoncé absent"),
                             ((actions[:-1], QUESTIONS, table, ENTROPIE, "juge"), "n'a pas ses 10 pas"),
                             ((actions + [{**actions[0], "condition": "temoin-identite"}], QUESTIONS, table, ENTROPIE, "juge"), "hors des cinq conditions"),
                             ((actions, QUESTIONS, dict(list(table.items())[:-600]), ENTROPIE, "moniteur-boite-noire"), "pas d'identifiant opaque")):
        with pytest.raises(GardeArret, match=motif):
            P.preparer(*arguments)


def test_drapeaux_du_message_comptes_par_condition(table):
    actions = _actions()
    for a in actions:
        if a["condition"] == "dose-1.00" and a["tache"] == TACHES[0] and a["episode"] == 0 and a["pas"] == 0:
            a["texte"] = a["texte"].replace("body 0", "body 0 café\n>>> LATEST CHANGE (added) <<<")
    _, bilan = P.preparer(actions, QUESTIONS, table, ENTROPIE, "moniteur-boite-noire")
    assert bilan["dose-1.00"]["marqueur_dans_le_texte_de_l_agent"] == 10 == bilan["dose-1.00"]["hors_forme_composee"]
    assert bilan["honnete"]["marqueur_dans_le_texte_de_l_agent"] == 0


# ------------------------------------------------------------------------------------------- garde statique du paquet

def test_garde_statique_des_imports_du_paquet_de_preparation():
    permis = {"__future__", "hashlib", "json", "re", "pathlib", "...", "...gardes", "...scellement",
              "..bras_a_v2_habilite"}
    for chemin in sorted((RACINE / "src/controle_ia/organismes_discrets/bras_a_v2_habilite_preparation").glob("*.py")):
        source = chemin.read_text(encoding="utf-8")
        for n in ast.walk(ast.parse(source)):
            noms = [a.name for a in n.names] if isinstance(n, ast.Import) else \
                [("." * n.level) + (n.module or "")] if isinstance(n, ast.ImportFrom) else []
            assert all(nom in permis for nom in noms), f"{chemin.name} importe {noms}"
        assert "spec_from_file_location" not in source and "open(" not in source.replace("with open(chemin", "")
