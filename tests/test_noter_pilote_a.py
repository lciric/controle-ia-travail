"""Lanceur « notations seules » du pilote de T0.5 (N-021) : sur un pilote jouet arrêté pendant ses notations décisives,
notations refaites dans un run distinct, aux mêmes graines ; gardes d'avant le manifeste (cas sain et artefact, R5) ;
échéances par juge et globale ; signal TERM ; lignes de progression sans texte."""
from __future__ import annotations

import json

import pytest

from conftest import committer
from controle_ia import gardes
from controle_ia.environnements import lancer_pilote_a as lp
from controle_ia.environnements import noter_pilote_a as npa
from controle_ia.environnements import pilote_a as pa
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import verifier_resultat
from controle_ia.scellement import empreinte, sceller
from test_pilote_a import CIBLES_TEST, TACHES, _config_lanceur

PILOTE = "20261012-100000-pilote-jouet"


def _taches(depot):
    f = depot / "taches.json"
    f.write_text(json.dumps({"taches": [dict(t, cibles=CIBLES_TEST) for t in TACHES]}), encoding="utf-8")
    return f, sceller(f)


def _pilote_arrete(depot, monkeypatch, etape_arret="decisives"):
    """Pilote jouet complet jusqu'à l'appariement, ensembles non vides, arrêté à l'échéance pendant les notations
    décisives du 8B, comme le vrai pilote."""
    vrai_jouer = lp.jouer_pilote

    def jouer(*a, **k):
        fiches, vecteurs, cn = vrai_jouer(*a, **k)
        for f in fiches:
            f["bilan"]["ensemble"] = f"PROPOSAL 1: idée {f['episode']}"
        return fiches, vecteurs, cn

    def noter(*a, **k):
        raise GardeArret("limite de durée dépassée pendant les notations")

    def apparier_en_panne(*a, **k):
        raise GardeArret("panne simulée de l'appariement")

    monkeypatch.setattr(lp, "jouer_pilote", jouer)
    monkeypatch.setattr(lp, "noter_ensembles", noter)
    if etape_arret == "appariement":
        monkeypatch.setattr(lp, "apparier", apparier_en_panne)
    f, sha = _taches(depot)
    committer(depot)
    with pytest.raises(GardeArret):
        lp.executer(_config_lanceur(), depot, PILOTE, None, str(f))
    monkeypatch.undo()
    committer(depot)
    return f, sha


def _config(**changes):
    c = _config_lanceur()
    base = {k: c[k] for k in npa.CLES_EGALES_AU_PILOTE}
    return {**base, "mode": "jouet", "run_pilote": PILOTE,
            "duree_max_juges_s": {"jouet-8B": 600, "jouet-3B": 600}, "duree_globale_s": 1200,
            "notations_attendues_par_juge": 4, **changes}


def _fichiers(depot, run):
    return sorted(p.name for p in (depot / "diag" / run).glob("*.json"))


def test_bout_en_bout_notations_dans_un_run_distinct(depot, monkeypatch, capsys):
    f, _ = _pilote_arrete(depot, monkeypatch)
    avant = _fichiers(depot, PILOTE)
    assert avant == ["appariements.json", "arret.json", "episodes.json"]
    run = "20261012-110000-notations-jouet"
    resume = npa.executer(_config(), depot, run, None, str(f))
    assert _fichiers(depot, PILOTE) == avant                       # rien d'écrit dans le dossier du pilote
    assert _fichiers(depot, run) == ["notations-jouet-3B-decisives.json", "notations-jouet-8B-decisives.json",
                                     "resume.json"]
    assert {n: j["statut"] for n, j in resume["juges"].items()} == {"jouet-8B": "écrit", "jouet-3B": "écrit"}
    fiches = json.loads((depot / "diag" / PILOTE / "episodes.json").read_text())["resultat"]["fiches"]
    import hashlib
    ensembles = {x["episode"]: hashlib.sha256(x["bilan"]["ensemble"].encode()).hexdigest() for x in fiches}
    for juge in ("jouet-8B", "jouet-3B"):
        r = verifier_resultat(depot, depot / "diag" / run / f"notations-{juge}-decisives.json")
        assert r["run_id"] == run
        cles = [n["cle"] for n in r["resultat"]["notations"]]
        assert cles == [f"juge-{juge}/{t['identifiant']}/e0/passe-{p}" for t in TACHES for p in (0, 1)]
        assert all(n["ensemble_sha256"] == ensembles[n["cle"].split("/", 1)[1].rsplit("/", 1)[0]]
                   for n in r["resultat"]["notations"])
    mp = json.loads((depot / "runs" / PILOTE / "manifeste.json").read_text())
    mn = json.loads((depot / "runs" / run / "manifeste.json").read_text())
    assert all(mn["graines"][k] == mp["graines"][k] for k in mn["graines"])
    err = capsys.readouterr().err
    lignes = [x for x in err.splitlines() if x.startswith("PROGRES ")]
    assert len(lignes) == 2 + 1 + 2 + 1 and "PROPOSAL" not in err and "idée" not in err
    assert "juge=jouet-8B lot=1/2" in lignes[0]


def test_rejeu_identique_et_r12(depot, monkeypatch):
    f, _ = _pilote_arrete(depot, monkeypatch)
    a = "20261012-110001-notations-jouet"
    b = "20261012-110002-notations-jouet"
    npa.executer(_config(), depot, a, None, str(f), autoriser_depot_sale=True)
    npa.executer(_config(), depot, b, None, str(f), autoriser_depot_sale=True)
    for juge in ("jouet-8B", "jouet-3B"):
        na, nb = (json.loads((depot / "diag" / r / f"notations-{juge}-decisives.json").read_text())["resultat"]
                  ["notations"] for r in (a, b))
        assert [(x["reponse"], x["score"]) for x in na] == [(x["reponse"], x["score"]) for x in nb]
    with pytest.raises(GardeArret, match="R12"):
        npa.executer(_config(), depot, a, None, str(f), autoriser_depot_sale=True)


@pytest.mark.parametrize("changement, motif", [
    ({"lot_juge": 3}, "lot_juge ≠ celui du pilote"),
    ({"notations_attendues_par_juge": 5}, "4 notations à faire, 5 attendues"),
    ({"duree_globale_s": 0}, "durée globale"),
    ({"duree_max_juges_s": {"jouet-8B": 600}}, "une durée par juge"),
    ({"run_pilote": "20261012-100001-autre"}, "manifeste du pilote absent"),
])
def test_gardes_de_configuration_cas_sain_et_artefacts(depot, monkeypatch, changement, motif):
    f, _ = _pilote_arrete(depot, monkeypatch)
    run = "20261012-110003-notations-jouet"
    with pytest.raises(GardeArret, match=motif):
        npa.executer(_config(**changement), depot, run, None, str(f), autoriser_depot_sale=True)
    assert not (depot / "runs" / run).exists()
    npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)        # cas sain


def test_config_incomplete_et_reel_sans_preenregistrement(depot):
    with pytest.raises(GardeArret, match="incomplète"):
        npa.executer({k: v for k, v in _config().items() if k != "fils"}, depot, "20261012-110004-x", None, "t.json")
    with pytest.raises(GardeArret, match="R1"):
        npa.executer(_config(mode="reel"), depot, "20261012-110005-x", None, "t.json")
    assert not (depot / "runs").exists()


def test_etat_du_pilote_artefacts(depot, monkeypatch):
    """Notations ou résumé déjà présents, épisodes altérés, tâches différentes : arrêt avant le manifeste."""
    f, _ = _pilote_arrete(depot, monkeypatch)
    run = "20261012-110006-notations-jouet"
    d = depot / "diag" / PILOTE
    # tâches différentes de celles du pilote
    g = depot / "taches-autres.json"
    g.write_text(json.dumps({"taches": [dict(t, cibles=CIBLES_TEST) for t in TACHES[:1]]}), encoding="utf-8")
    sceller(g)
    with pytest.raises(GardeArret, match="tâches ≠ celles du pilote"):
        npa.executer(_config(), depot, run, None, str(g), autoriser_depot_sale=True)
    # épisodes altérés : le sceau ne tient plus
    texte = (d / "episodes.json").read_text()
    (d / "episodes.json").write_text(texte.replace("idée", "idee"))
    with pytest.raises(GardeArret):
        npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    (d / "episodes.json").write_text(texte)
    # notation déjà présente dans le dossier du pilote
    (d / "notations-jouet-8B-decisives.json").write_text("{}")
    with pytest.raises(GardeArret, match="déjà présents"):
        npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    (d / "notations-jouet-8B-decisives.json").unlink()
    assert not (depot / "runs" / run).exists()
    npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)        # cas sain


def test_pilote_arrete_ailleurs_que_pendant_les_notations(depot, monkeypatch):
    f, _ = _pilote_arrete(depot, monkeypatch, etape_arret="appariement")
    with pytest.raises(GardeArret, match="appariements.json absent"):
        npa.executer(_config(), depot, "20261012-110007-notations-jouet", None, str(f), autoriser_depot_sale=True)


def _prereg(depot, config, pilote_d, sha_taches, entropie, commit, nom="prereg-notations.md", lignes_en_plus=()):
    (depot / "prereg").mkdir(exist_ok=True)
    p = depot / "prereg" / nom
    lignes = [f"- Commit du code d'analyse : `{commit}`",
              f"- Configuration des notations (empreinte canonique) : `{lp.empreinte_config(config)}`",
              f"- Run du pilote noté : `{PILOTE}`",
              f"- Manifeste du pilote noté : `{empreinte(depot / 'runs' / PILOTE / 'manifeste.json')}`",
              f"- Épisodes du pilote noté : `{empreinte(pilote_d / 'episodes.json')}`",
              f"- Arrêt du pilote noté : `{empreinte(pilote_d / 'arret.json')}`",
              f"- Tâches du pilote : `{sha_taches}`", f"- Entropie : `{entropie}`", *lignes_en_plus]
    corps = ["# Préenregistrement de test", "", *lignes, ""]
    for s in ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
              "Critères de lecture gelés", "Liste d'arrêt"):
        corps += [f"## {s}", "", f"contenu {s}", ""]
    corps += ["## Contre-lecture", "", f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`", ""]
    p.write_text("\n".join(corps), encoding="utf-8")
    sceller(p)
    return p


def test_gardes_de_citation_cas_sain_et_artefacts(depot, monkeypatch):
    f, sha = _pilote_arrete(depot, monkeypatch)
    monkeypatch.setattr(npa, "exiger_code_importe_sous", lambda racine: None)
    import subprocess
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    d = depot / "diag" / PILOTE
    mp = json.loads((depot / "runs" / PILOTE / "manifeste.json").read_text())
    entropie = int(next(iter(mp["graines"].values()))["entropie"])
    c = _config()
    sain = _prereg(depot, c, d, sha, entropie, commit)
    cas = [(_prereg(depot, _config(duree_globale_s=1100), d, sha, entropie, commit, "p-config.md"), "configuration"),
           (_prereg(depot, c, d, sha, entropie + 1, commit, "p-entropie.md"), "entropie ≠ celle du pilote"),
           (_prereg(depot, c, d, "c" * 64, entropie, commit, "p-taches.md"), "tâches"),
           (_prereg(depot, c, d, sha, entropie, commit, "p-double.md",
                    (f"- Run du pilote noté : `20261012-100009-autre`",)), "plusieurs fois")]
    committer(depot)
    for p, motif in cas:
        with pytest.raises(GardeArret, match=motif):
            npa.executer(c, depot, "20261012-110008-notations-jouet", str(p), str(f))
        assert not (depot / "runs" / "20261012-110008-notations-jouet").exists()
    resume = npa.executer(c, depot, "20261012-110009-notations-jouet", str(sain), str(f), autoriser_depot_sale=True)
    assert resume["commit_cite"] == commit
    m = json.loads((depot / "runs" / "20261012-110009-notations-jouet" / "manifeste.json").read_text())
    assert m["decisif"] and m["preenregistrement"]["chemin"] == "prereg/prereg-notations.md"


def test_echeance_du_8b_le_3b_continue(depot, monkeypatch):
    f, _ = _pilote_arrete(depot, monkeypatch)
    run = "20261012-110010-notations-jouet"
    resume = npa.executer(_config(duree_max_juges_s={"jouet-8B": 1e-9, "jouet-3B": 600}), depot, run, None, str(f),
                          autoriser_depot_sale=True)
    assert resume["juges"]["jouet-8B"]["statut"] == "échu" and resume["juges"]["jouet-8B"]["lots_faits"] == 0
    assert resume["juges"]["jouet-3B"]["statut"] == "écrit"
    assert _fichiers(depot, run) == ["notations-jouet-3B-decisives.json", "resume.json"]


def test_echeance_globale_arrete_et_consigne(depot, monkeypatch):
    f, _ = _pilote_arrete(depot, monkeypatch)
    run = "20261012-110011-notations-jouet"
    with pytest.raises(GardeArret, match="limite de durée"):
        npa.executer(_config(duree_globale_s=1e-9), depot, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot, run) == ["arret.json"]
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["etape"] == "notations decisives par jouet-8B" and r["partiel"]["juges"]["jouet-8B"]["lots_faits"] == 0


def test_signal_term_pendant_le_8b_n_ouvre_jamais_le_3b(depot, monkeypatch):
    """Un TERM reçu pendant le 8B arrête le run (jamais avalé pour continuer) : aucun fichier de notation, le 3B
    n'est pas commencé, `arret.json` consigne l'étape."""
    f, _ = _pilote_arrete(depot, monkeypatch)
    vrai = npa.noter_ensembles

    def noter(*a, **k):
        sortie = vrai(*a, **k)
        gardes.SIGNAL_TERM_RECU.append(15)          # signal avalé par une bibliothèque : drapeau seul
        return sortie

    monkeypatch.setattr(npa, "noter_ensembles", noter)
    run = "20261012-110012-notations-jouet"
    with pytest.raises(GardeArret):
        npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot, run) == ["arret.json"]
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["etape"] == "notations decisives par jouet-8B" and set(r["partiel"]["juges"]) == {"jouet-8B"}
    assert r["partiel"]["juges"]["jouet-8B"]["lots_faits"] == 1


def test_format_different_du_pilote_arrete(depot, monkeypatch):
    f, _ = _pilote_arrete(depot, monkeypatch)
    vrai = npa.controler_format

    def controle(fmt, spec, role, config):
        r = vrai(fmt, spec, role, config)
        return {**r, "altere": True} if spec["nom"] == "jouet-3B" else r

    monkeypatch.setattr(npa, "controler_format", controle)
    run = "20261012-110013-notations-jouet"
    with pytest.raises(GardeArret, match="format ≠ celui du début du pilote"):
        npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]["etape"] == "contrôle du format"


def test_graines_differentes_du_pilote_arretent():
    pilote = {"manifeste": {"graines": {"a": {"entropie": "7", "spawn_key": ["1"]}}}}
    with pytest.raises(GardeArret, match="entropie ≠ celle du pilote"):
        npa.exiger_graines_du_pilote(["a"], 8, pilote)
    from controle_ia.manifeste import graines
    pilote = {"manifeste": {"graines": graines(["a", "b"], 7)}}
    npa.exiger_graines_du_pilote(["a", "b"], 7, pilote)                                # cas sain
    pilote["manifeste"]["graines"]["b"] = {"entropie": "7", "spawn_key": ["0"]}
    with pytest.raises(GardeArret, match="graines ≠ celles du pilote"):
        npa.exiger_graines_du_pilote(["a", "b"], 7, pilote)


def test_noter_ensembles_inchange():
    """Le lanceur importe `noter_ensembles` du code cité, sans copie ni enveloppe."""
    assert npa.noter_ensembles is pa.noter_ensembles and npa.demandes_de_notation is lp.demandes_de_notation
