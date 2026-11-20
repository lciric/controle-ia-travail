"""Essais de l'étape de préparation des lectures des deux moniteurs à modèle de langue du bras A, version 3 (aucune
position tirée : le juge lit toutes les actions). Données factices seulement ; aucun modèle chargé. Chaque garde a un
cas sain et un artefact (R5).

Essais ciblés :
    PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_preparation_des_lectures_v3.py

Fichier neuf (R12) : les essais de la version 2 éprouvent toujours la version 2. Ceux-ci reprennent ses essais, sauf
celui du sous-échantillon du juge, remplacé par `test_le_juge_lit_toutes_les_actions` ; la garde neuve du bilan (cinq
comptes par condition) a son cas sain et ses artefacts.
"""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

import pytest

from controle_ia import manifeste
from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets.bras_a_v2_habilite import autres_moniteurs_v10 as A
from controle_ia.organismes_discrets.bras_a_v2_habilite import moniteurs_langue_v3 as ML
from controle_ia.organismes_discrets.bras_a_v2_habilite_preparation import preparation_des_lectures_v2 as P2
from controle_ia.organismes_discrets.bras_a_v2_habilite_preparation import preparation_des_lectures_v3 as P

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
    assert bilan["honnete"] == {"actions": 1280, "non_lues": 1, "demandes": 1279,
                                "marqueur_dans_le_texte_de_l_agent": 0, "hors_forme_composee": 0}
    assert bilan["dose-0.50"]["non_lues"] == 2 and bilan["dose-1.00"]["demandes"] == 1280
    assert len(demandes) == 6400 - 3 and [d["cle"] for d in demandes] == sorted(d["cle"] for d in demandes)
    assert all(tuple(d) == P.CHAMPS_DEMANDE for d in demandes)
    d = demandes[0]
    nom, t, e, p = table[d["cle"]].split("__")
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


def test_le_juge_lit_toutes_les_actions(table):
    """Version 3 : aucune position tirée ; le juge a une demande par action lue, comme le moniteur boîte noire, et les
    mêmes messages ; seules ses graines diffèrent (clé du moniteur)."""
    demandes, bilan = P.preparer(_actions(ILLISIBLES), QUESTIONS, table, ENTROPIE, "juge")
    bn, _ = P.preparer(_actions(ILLISIBLES), QUESTIONS, table, ENTROPIE, "moniteur-boite-noire")
    assert len(demandes) == 6400 - 3 and [d["cle"] for d in demandes] == [d["cle"] for d in bn]
    assert [d["utilisateur"] for d in demandes] == [d["utilisateur"] for d in bn]
    assert all("hors_du_sous_echantillon" not in b for b in bilan.values())
    assert bilan["dose-1.00"] == {"actions": 1280, "non_lues": 0, "demandes": 1280,
                                  "marqueur_dans_le_texte_de_l_agent": 0, "hors_forme_composee": 0}
    d = demandes[0]
    _, t, e, p = table[d["cle"]].split("__")
    cle_graine = ML.cle_de_graine("juge", t, int(e[1:]), int(p[1:]))
    assert d["graine"] == ML.graine_entiere(manifeste.graines([cle_graine], ENTROPIE)[cle_graine])
    # la version 2, elle, tire 32 positions par tâche : c'est ce qui change, et rien d'autre
    v2, _ = P2.preparer(_actions(ILLISIBLES), QUESTIONS, table, ENTROPIE, "juge")
    assert len(v2) < 2560 + 1 and {x["cle"]: x for x in v2}.items() <= {x["cle"]: x for x in demandes}.items()


def test_rien_dans_le_fichier_des_demandes_ne_dit_la_condition(tmp_path, table):
    demandes, bilan = P.preparer(_actions(), QUESTIONS, table, ENTROPIE, "juge")
    e = P.ecrire_les_demandes(tmp_path / "production", "juge", demandes)
    assert e["fichier"] == "demandes-juge.jsonl" and e["lignes"] == 6400
    brut = e["chemin"].read_text(encoding="utf-8")
    for marque in ("__e", "H__", "honnete", "dose-", '"condition"', '"tache"', '"episode"', '"pas"'):
        assert marque not in brut, marque
    assert all(tuple(json.loads(l)) == P.CHAMPS_DEMANDE for l in brut.splitlines())
    b = P.ecrire_le_bilan(tmp_path / "a-part", "juge", bilan, e["sha256"])
    contenu = json.loads(b["chemin"].read_text(encoding="utf-8"))
    assert contenu["demandes_sha256"] == e["sha256"] and set(contenu["par_condition"]) == set(P.ROLES_LUS)
    assert not (tmp_path / "production" / P.fichier_du_bilan("juge")).exists()
    with pytest.raises(GardeArret, match="n'écrase jamais"):
        P.ecrire_les_demandes(tmp_path / "production", "juge", demandes)
    with pytest.raises(GardeArret, match="n'écrase jamais"):
        P.ecrire_le_bilan(tmp_path / "a-part", "juge", bilan, e["sha256"])


def test_garde_du_bilan_cinq_comptes_par_condition(tmp_path, table):
    _, bilan = P.preparer(_actions(), QUESTIONS, table, ENTROPIE, "moniteur-boite-noire")
    P.ecrire_le_bilan(tmp_path / "sain", "moniteur-boite-noire", bilan, "0" * 64)          # cas sain
    ancien = {r: {**b, "hors_du_sous_echantillon": 0} for r, b in bilan.items()}      # forme de la version 2
    for mauvais in ({"honnete": bilan["honnete"]}, ancien,
                    {**bilan, "honnete": {k: v for k, v in bilan["honnete"].items() if k != "non_lues"}}):
        with pytest.raises(GardeArret, match="cinq comptes"):
            P.ecrire_le_bilan(tmp_path / "x", "moniteur-boite-noire", mauvais, "0" * 64)
    assert not (tmp_path / "x").exists()


def test_production_ne_lit_que_le_fichier_des_demandes(tmp_path, table):
    demandes, _ = P.preparer(_actions(), QUESTIONS, table, ENTROPIE, "moniteur-boite-noire")
    e = P.ecrire_les_demandes(tmp_path, "moniteur-boite-noire", demandes[:50])
    lues, graines = P.lire_les_demandes(e["chemin"], CONSIGNE)
    assert len(lues) == 50 and set(graines) == {d["cle"] for d in lues}
    for d in lues:
        ML.exiger_demande(d)
    with pytest.raises(GardeArret, match="toute autre consigne"):
        P.lire_les_demandes(e["chemin"], CONSIGNE + " ")
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
                           ({k: v for k, v in d.items() if k != "graine"}, "aucun autre"),
                           ({**d, "cle": "controls-1.00__t__e0__p0"}, "clé non opaque"),
                           ({**d, "utilisateur": "CURRENT SET"}, "message hors format"),
                           ({**d, "graine": -1}, "graine entière"), ({**d, "graine": True}, "graine entière")):
        with pytest.raises(GardeArret, match=motif):
            P.exiger_demande_preparee(mauvais)
        with pytest.raises(GardeArret, match=motif):
            P.ecrire_les_demandes(tmp_path / "x", "juge", [mauvais])
    with pytest.raises(GardeArret, match="en double, ou hors de leur ordre trié"):
        P.ecrire_les_demandes(tmp_path / "x", "juge", [demandes[1], demandes[0]])
    with pytest.raises(GardeArret, match="attendus"):
        P.ecrire_les_demandes(tmp_path / "x", "agregateur-sequentiel", demandes[:1])
    assert not (tmp_path / "x").exists()
    chemin = tmp_path / "demandes-juge.jsonl"
    for lignes, motif in (([d, d], "identifiant en double"), ([{**d, "condition": "honnete"}], "aucun autre")):
        chemin.write_text("".join(json.dumps(x) + "\n" for x in lignes), encoding="utf-8")
        Path(str(chemin) + ".sha256").write_text(
            hashlib.sha256(chemin.read_bytes()).hexdigest() + "  " + chemin.name + "\n", encoding="utf-8")
        with pytest.raises(GardeArret, match=motif):
            P.lire_les_demandes(chemin, CONSIGNE)


def test_gardes_d_entree_de_la_preparation(table):
    actions = _actions()
    for arguments, motif in (((actions, QUESTIONS, table, ENTROPIE, "agregateur-sequentiel"), "attendus"),
                             ((actions, QUESTIONS, table, -1, "juge"), "entropie"),
                             ((actions, QUESTIONS, {"H__t__e0__p0": "x"}, ENTROPIE, "juge"), "hors format"),
                             ((actions, {t: q for t, q in QUESTIONS.items() if t != TACHES[5]}, table, ENTROPIE, "juge"),
                              "énoncé absent"),
                             ((actions[:-1], QUESTIONS, table, ENTROPIE, "juge"), "n'a pas ses 10 pas"),
                             ((actions + [{**actions[0], "condition": "temoin-identite"}], QUESTIONS, table, ENTROPIE,
                               "juge"), "hors des cinq conditions"),
                             ((actions, QUESTIONS, dict(list(table.items())[:-600]), ENTROPIE, "juge"),
                              "pas d'identifiant opaque")):
        with pytest.raises(GardeArret, match=motif):
            P.preparer(*arguments)


def test_garde_statique_des_imports_de_la_version_3():
    """Mêmes importations permises que le paquet de préparation ; aucune ouverture de fichier hors de l'écriture des
    demandes ; aucun tirage de position (ni `positions_du_juge`, ni `choice`)."""
    permis = {"__future__", "hashlib", "json", "re", "pathlib", "...", "...gardes", "...scellement",
              "..bras_a_v2_habilite"}
    chemin = RACINE / "src/controle_ia/organismes_discrets/bras_a_v2_habilite_preparation/preparation_des_lectures_v3.py"
    source = chemin.read_text(encoding="utf-8")
    for n in ast.walk(ast.parse(source)):
        noms = [a.name for a in n.names] if isinstance(n, ast.Import) else \
            [("." * n.level) + (n.module or "")] if isinstance(n, ast.ImportFrom) else []
        assert all(nom in permis for nom in noms), f"{chemin.name} importe {noms}"
    assert "spec_from_file_location" not in source and "open(" not in source.replace("with open(chemin", "")
    code = "\n".join(l for l in source.splitlines() if not l.lstrip().startswith("#"))
    corps = code.split('"""', 2)[2]                                   # hors de l'en-tête
    assert "positions_du_juge" not in corps and ".choice(" not in corps
