"""Notations complémentaires de T0.5 : sur un run source jouet de la chaîne du pilote (une tâche, trois épisodes, e0 et e1
décisifs, e0 noté deux fois : une seule tâche, car chaque lot de notation du modèle jouet coûte plusieurs secondes sur
processeur), arrêté pendant ses notations décisives, les couples demandés (e2 passe 0 des deux juges ;
notations manquantes du 3B) sont notés dans un run distinct, aux mêmes graines ; mêmes notations que la chaîne complète
à la même entropie ; gardes d'avant le manifeste (cas sain et artefact, R5) ; échéance par juge ; signal TERM."""
from __future__ import annotations

import atexit
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest

from conftest import committer
from controle_ia import gardes
from controle_ia.environnements import lancer_pilote_a as lp
from controle_ia.environnements import noter_complement_t05 as nc
from controle_ia.environnements import pilote_a as pa
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste as vrai_creer
from controle_ia.manifeste import ecrire_resultat, graines, verifier_resultat
from controle_ia.scellement import empreinte, sceller
from test_pilote_a import CIBLES_TEST, TACHES, _config_lanceur

PILOTE = "20261027-100000-source-jouet"          # arrêté pendant les notations décisives du 8B (aucune notation)
COMPLET = "20261027-100001-source-complete"      # même entropie, chaîne complète (décisives et descriptives)
TROIS_B = "20261027-100002-source-3b-manquant"   # 8B décisives écrites, arrêté pendant les décisives du 3B
ENTROPIE = 20261027
JUGES = ("jouet-8B", "jouet-3B")
TACHE = TACHES[0]
ECHUS = {"jouet-8B": 1e-9, "jouet-3B": 1e-9}          # deux juges échus : aucune notation (suite courte)
_GABARITS: dict = {}


def _config_source():
    """Chaîne du pilote en jouet, au plan du vrai pilote : trois épisodes par tâche, e0 et e1 décisifs, e0 noté deux
    fois ; e2 n'est jamais noté en décisif."""
    return {**_config_lanceur(), "episodes_par_tache": 3, "episodes_decisifs": [0, 1], "episodes_notes_deux_fois": [0]}


def _construire(gabarit, monkeypatch, sorte):
    """Runs sources jouets de la chaîne (`lancer_pilote_a`), ensembles non vides, entropie fixe."""
    vrai_jouer, vrai_noter = lp.jouer_pilote, lp.noter_ensembles

    def jouer(*a, **k):
        fiches, vecteurs, cn = vrai_jouer(*a, **k)
        for x in fiches:
            x["bilan"]["ensemble"] = f"PROPOSAL 1: idée {x['episode']}"
        return fiches, vecteurs, cn

    def noter(sauf_juge):
        def f(m, fmt, demandes, *a, **k):
            if sauf_juge is None or (demandes and demandes[0]["cle"].startswith(f"juge-{sauf_juge}/")):
                raise GardeArret("limite de durée dépassée pendant les notations")
            return vrai_noter(m, fmt, demandes, *a, **k)
        return f

    monkeypatch.setattr(lp, "jouer_pilote", jouer)
    monkeypatch.setattr(lp, "creer_manifeste", lambda *a, **k: vrai_creer(*a, **{**k, "entropie": ENTROPIE}))
    f = gabarit / "taches.json"
    f.write_text(json.dumps({"taches": [dict(TACHE, cibles=CIBLES_TEST)]}), encoding="utf-8")
    sceller(f)
    committer(gabarit)
    if sorte == "arrete":
        lp.executer(_config_source(), gabarit, COMPLET, None, str(f))
        committer(gabarit)
        monkeypatch.setattr(lp, "noter_ensembles", noter(None))
        with pytest.raises(GardeArret):
            lp.executer(_config_source(), gabarit, PILOTE, None, str(f))
    else:
        monkeypatch.setattr(lp, "noter_ensembles", noter("jouet-3B"))
        with pytest.raises(GardeArret):
            lp.executer(_config_source(), gabarit, TROIS_B, None, str(f))
    monkeypatch.undo()
    committer(gabarit)


def _source(depot, monkeypatch, sorte="arrete"):
    """Runs sources construits une fois par processus dans un gabarit, puis copiés dans le dépôt du test (mêmes
    fichiers, même histoire git) : la suite reste courte."""
    if sorte not in _GABARITS:
        gabarit = Path(tempfile.mkdtemp(prefix=f"source-jouet-{sorte}-"))
        atexit.register(shutil.rmtree, gabarit, True)
        for args in (("init", "-q", "-b", "main"), ("config", "user.email", "test@example.invalid"),
                     ("config", "user.name", "test")):
            subprocess.run(["git", "-C", str(gabarit), *args], check=True, capture_output=True)
        (gabarit / "README").write_text("x\n")
        committer(gabarit)
        _construire(gabarit, monkeypatch, sorte)
        _GABARITS[sorte] = gabarit
    shutil.rmtree(depot / ".git")
    shutil.copytree(_GABARITS[sorte], depot, dirs_exist_ok=True)
    return depot / "taches.json"


def _config(source=PILOTE, **changes):
    c = _config_source()
    return {**{k: c[k] for k in nc.CLES_EGALES_A_LA_SOURCE}, "mode": "jouet", "run_source": source,
            "duree_max_juges_s": {"jouet-8B": 600, "jouet-3B": 600}, "duree_globale_s": 1200,
            "notations_attendues_par_juge": {"jouet-8B": 1, "jouet-3B": 1},
            "notations_a_faire": {"jouet-8B": {"2": [0]}, "jouet-3B": {"2": [0]}}, **changes}


def _fichiers(depot, run):
    return sorted(p.name for p in (depot / "diag" / run).glob("*.json"))


def _instantane(depot, run):
    return {str(p.relative_to(depot)): empreinte(p) for d in ("diag", "runs") for p in (depot / d / run).iterdir()}


def _notations(depot, run, juge):
    return verifier_resultat(depot, depot / "diag" / run / f"notations-{juge}-decisives.json")




def test_bout_en_bout_e2_des_deux_juges_memes_notations_que_la_chaine(depot, monkeypatch, capsys):
    """e2 passe 0 des deux juges, dans un run distinct ; dossier source inchangé ; graines du manifeste source ; et, à
    la même entropie, notations égales clé à clé (réponses, scores, jetons, ensembles notés) à celles que la chaîne
    complète a faites de e2 en descriptif."""
    f = _source(depot, monkeypatch)
    avant = _instantane(depot, PILOTE)
    assert _fichiers(depot, PILOTE) == ["appariements.json", "arret.json", "episodes.json"]
    run = "20261027-110000-complement-jouet"
    resume = nc.executer(_config(), depot, run, None, str(f))
    assert _instantane(depot, PILOTE) == avant                           # rien d'écrit dans le dossier du run source
    assert _fichiers(depot, run) == ["notations-jouet-3B-decisives.json", "notations-jouet-8B-decisives.json",
                                     "resume.json"]
    assert {n: j["statut"] for n, j in resume["juges"].items()} == {"jouet-8B": "écrit", "jouet-3B": "écrit"}
    assert resume["run_source"] == PILOTE and resume["notations_a_faire"] == _config()["notations_a_faire"]
    assert resume["arret_source_sha256"] == empreinte(depot / "diag" / PILOTE / "arret.json")
    assert resume["notations_source_sha256"] == hashlib.sha256(b"[]").hexdigest()    # aucune notation au run source
    fiches = json.loads((depot / "diag" / PILOTE / "episodes.json").read_text())["resultat"]["fiches"]
    ensembles = {x["episode"]: hashlib.sha256(x["bilan"]["ensemble"].encode()).hexdigest() for x in fiches}
    champs = ("cle", "reponse", "score", "jetons_reponse", "tronquee", "ensemble_sha256")
    for juge in JUGES:
        r = _notations(depot, run, juge)
        assert r["run_id"] == run
        assert [n["cle"] for n in r["resultat"]["notations"]] == [f"juge-{juge}/{TACHE['identifiant']}/e2/passe-0"]
        assert all(n["ensemble_sha256"] == ensembles[n["cle"].split("/", 1)[1].rsplit("/", 1)[0]]
                   for n in r["resultat"]["notations"])
        chaine = verifier_resultat(depot, depot / "diag" / COMPLET / f"notations-{juge}-descriptives.json")
        assert [{k: x[k] for k in champs} for x in chaine["resultat"]["notations"]] == \
               [{k: x[k] for k in champs} for x in r["resultat"]["notations"]]
    ms = json.loads((depot / "runs" / PILOTE / "manifeste.json").read_text())
    mn = json.loads((depot / "runs" / run / "manifeste.json").read_text())
    assert set(mn["graines"]) == {f"juge-{j}/{TACHE['identifiant']}/e2/passe-0" for j in JUGES} | {"modele-jouet"}
    assert all(mn["graines"][k] == ms["graines"][k] for k in mn["graines"])
    err = capsys.readouterr().err
    lignes = [x for x in err.splitlines() if x.startswith("PROGRES ")]
    assert len(lignes) == 4 and "PROPOSAL" not in err and "idée" not in err
    assert "juge=jouet-8B lot=1/1" in lignes[0] and "juge=jouet-8B fin=écrit lots_faits=1/1" in lignes[1]
    assert all(set(k.split("=")[0] for k in x.split()[2:]) <= {"juge", "lot", "duree_s", "fin", "lots_faits"}
               for x in lignes)


A_FAIRE_3B = {"jouet-8B": {"2": [0]}, "jouet-3B": {"0": [0, 1], "1": [0], "2": [0]}}


def test_source_8b_ecrit_3b_manquant(depot, monkeypatch):
    """Run source arrêté pendant les décisives du 3B : le complément note e0 (passes 0 et 1), e1 et e2 du 3B, et e2 du
    8B ; demander un couple que le 8B a déjà noté arrête avant le manifeste (on ne renote jamais)."""
    f = _source(depot, monkeypatch, "3b")
    d = depot / "diag" / TROIS_B
    assert _fichiers(depot, TROIS_B) == ["appariements.json", "arret.json", "episodes.json",
                                         "notations-jouet-8B-decisives.json"]
    avant = _instantane(depot, TROIS_B)
    c = _config(TROIS_B, notations_a_faire=A_FAIRE_3B, notations_attendues_par_juge={"jouet-8B": 1, "jouet-3B": 4})
    # artefact : e0 passe 0 du 8B, déjà noté au run source
    recouvre = _config(TROIS_B, notations_a_faire={**A_FAIRE_3B, "jouet-8B": {"0": [0], "2": [0]}},
                       notations_attendues_par_juge={"jouet-8B": 2, "jouet-3B": 4})
    with pytest.raises(GardeArret, match="juge jouet-8B : 1 couples déjà notés dans le run source .* on ne renote"):
        nc.executer(recouvre, depot, "20261027-110002-complement-jouet", None, str(f), autoriser_depot_sale=True)
    assert not (depot / "runs" / "20261027-110002-complement-jouet").exists()
    run = "20261027-110003-complement-jouet"
    resume = nc.executer(c, depot, run, None, str(f), autoriser_depot_sale=True)
    assert _instantane(depot, TROIS_B) == avant
    i = TACHE["identifiant"]
    assert [n["cle"] for n in _notations(depot, run, "jouet-3B")["resultat"]["notations"]] == [
        f"juge-jouet-3B/{i}/{e}" for e in ("e0/passe-0", "e0/passe-1", "e1/passe-0", "e2/passe-0")]
    assert [n["cle"] for n in _notations(depot, run, "jouet-8B")["resultat"]["notations"]] == [
        f"juge-jouet-8B/{i}/e2/passe-0"]
    # clés du run source et du complément disjointes : ensemble, les décisives complètes plus e2
    deja = {n["cle"] for n in verifier_resultat(depot, d / "notations-jouet-8B-decisives.json")["resultat"]["notations"]}
    neuves = {n["cle"] for n in _notations(depot, run, "jouet-8B")["resultat"]["notations"]}
    assert not deja & neuves and len(deja) == 3
    nom = "notations-jouet-8B-decisives.json"
    attendu = hashlib.sha256(json.dumps([[nom, empreinte(d / nom)]], separators=(",", ":")).encode()).hexdigest()
    assert resume["notations_source_sha256"] == attendu
    ms = json.loads((depot / "runs" / TROIS_B / "manifeste.json").read_text())
    mn = json.loads((depot / "runs" / run / "manifeste.json").read_text())
    assert len(mn["graines"]) == 6 and all(mn["graines"][k] == ms["graines"][k] for k in mn["graines"])


def _gardes_saines(depot, f, c=None):
    """Cas sain des gardes d'avant le manifeste, rejouées dans l'ordre d'`executer` sans lancer de notation."""
    c = c or _config()
    nc.exiger_config_complement(c)
    src = nc.charger_source(depot, c["run_source"], list(JUGES))
    nc.exiger_taches_de_la_source(src, empreinte(f))
    nc.exiger_egal_a_la_source(c, src, c["mode"])
    par_id = {x["identifiant"]: x for x in pa.charger_taches(str(f))}
    dem = {j: nc.demandes_a_faire(src, par_id, c, j) for j in JUGES}
    nc.exiger_nombre_et_disjonction(dem, c, src)
    nc.exiger_graines_de_la_source(nc.cles_des_graines(dem), ENTROPIE, src)
    return src


def test_gardes_de_configuration_cas_sain_et_artefacts(depot, monkeypatch):
    f = _source(depot, monkeypatch)
    run = "20261027-110004-complement-jouet"
    sans_fils = {k: v for k, v in _config().items() if k != "fils"}
    cas = [
        (sans_fils, "incomplète"),                                                        # clé égale manquante
        (_config(lot_juge=3), "lot_juge ≠ celui du run source"),                          # clé égale différente
        (_config(juges=[_config()["juges"][0]], duree_max_juges_s={"jouet-8B": 600},
                 notations_attendues_par_juge={"jouet-8B": 1}), "notations_a_faire : une entrée par juge"),
        (_config(notations_a_faire={"jouet-8B": {"2": [0]}}), "notations_a_faire : une entrée par juge"),
        (_config(notations_a_faire={"jouet-8B": {"2": [0]}, "jouet-3B": {"2": [1]}}), r"range\(1\)"),
        (_config(notations_a_faire={"jouet-8B": {"0": [2]}, "jouet-3B": {"2": [0]}}), r"range\(2\)"),
        (_config(notations_a_faire={"jouet-8B": {"02": [0]}, "jouet-3B": {"2": [0]}}), "illisible"),
        (_config(notations_a_faire={"jouet-8B": {"2": [0, 0]}, "jouet-3B": {"2": [0]}}), "distinctes"),
        (_config(notations_a_faire={"jouet-8B": {}, "jouet-3B": {"2": [0]}}), "au moins un épisode"),
        (_config(notations_attendues_par_juge={"jouet-8B": 3, "jouet-3B": 1}), "jouet-8B : 1 notations à faire, 3 att"),
        (_config(notations_attendues_par_juge={"jouet-8B": 1}), "un nombre par juge"),
        (_config(notations_attendues_par_juge={"jouet-8B": 1, "jouet-3B": True}), "entier positif"),
        (_config(duree_globale_s=23101), "durée globale"),
        (_config(duree_max_juges_s={"jouet-8B": 600}), "une durée par juge"),
        (_config(run_source="20261027-100009-autre"), "manifeste du run source absent"),
        (_config(mode="autre"), "inconnu"),
    ]
    for c, motif in cas:
        with pytest.raises(GardeArret, match=motif):
            nc.executer(c, depot, run, None, str(f), autoriser_depot_sale=True)
    with pytest.raises(GardeArret, match="R1"):
        nc.executer(_config(mode="reel"), depot, run, None, str(f))
    assert not (depot / "runs" / run).exists()
    _gardes_saines(depot, f)                                                              # cas sain
    nc.exiger_config_complement(_config(duree_globale_s=23100))


def _reecrire(chemin, changer):
    """Résultat scellé réécrit (contenu changé par `changer`), puis rescellé : seule la garde visée peut l'arrêter."""
    corps = json.loads(chemin.read_text())
    changer(corps)
    chemin.write_text(json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    Path(str(chemin) + ".sha256").unlink()
    sceller(chemin)


def test_etat_du_run_source_cas_sain_et_artefacts(depot, monkeypatch):
    """Tâches différentes ; arrêt avant les notations ; appariement non consigné ; fichier de notations inattendu ou
    d'un autre juge ; arrêt et résumé tous deux absents ; puis résumé seul (sans arrêt) : cas sain, run complet (juges
    échus : aucune notation)."""
    f = _source(depot, monkeypatch)
    d = depot / "diag" / PILOTE
    run = "20261027-110005-complement-jouet"
    g = depot / "taches-autres.json"
    g.write_text(json.dumps({"taches": [dict(TACHES[1], cibles=CIBLES_TEST)]}), encoding="utf-8")
    sceller(g)
    with pytest.raises(GardeArret, match=r"tâches ≠ celles du run source \(arret.json"):
        nc.executer(_config(), depot, run, None, str(g), autoriser_depot_sale=True)
    sauve = {n: (d / n).read_bytes() for n in ("arret.json", "arret.json.sha256")}

    def remettre():
        for n, b in sauve.items():
            (d / n).write_bytes(b)

    _reecrire(d / "arret.json", lambda c: c["resultat"].update(etape="épisodes"))
    with pytest.raises(GardeArret, match="arrêté à l'étape 'épisodes', avant les notations"):
        nc.charger_source(depot, PILOTE, list(JUGES))
    remettre()
    _reecrire(d / "arret.json", lambda c: c["resultat"]["partiel"].pop("appariement_ecrit"))
    with pytest.raises(GardeArret, match="appariement non consigné comme écrit"):
        nc.charger_source(depot, PILOTE, list(JUGES))
    remettre()
    for nom in ("notations-autre-decisives.json", "notations-jouet-8B-essai.json"):
        (d / nom).write_text("{}")
        with pytest.raises(GardeArret, match="fichier de notations inattendu"):
            nc.charger_source(depot, PILOTE, list(JUGES))
        (d / nom).unlink()
    # notations d'un autre juge sous le nom du 8B (rattachées au run source)
    chemin_m = depot / "runs" / PILOTE / "manifeste.json"
    ecrire_resultat(depot, chemin_m, "notations-jouet-8B-descriptives",
                    {"notations": [{"cle": "juge-jouet-3B/x/e2/passe-0"}]})
    with pytest.raises(GardeArret, match="clés d'un autre juge"):
        nc.charger_source(depot, PILOTE, list(JUGES))
    for n in ("notations-jouet-8B-descriptives.json", "notations-jouet-8B-descriptives.json.sha256"):
        (d / n).unlink()
    # ni arrêt ni résumé
    for n in sauve:
        (d / n).unlink()
    with pytest.raises(GardeArret, match="ni arret.json ni resume.json"):
        nc.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert not (depot / "runs" / run).exists()
    # résumé seul (run source terminé) : tâches lues dans le résumé ; une autre empreinte arrête
    ecrire_resultat(depot, chemin_m, "resume", {"taches_sha256": "c" * 64})
    with pytest.raises(GardeArret, match=r"tâches ≠ celles du run source \(resume.json"):
        nc.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    for n in ("resume.json", "resume.json.sha256"):
        (d / n).unlink()
    ecrire_resultat(depot, chemin_m, "resume", {"taches_sha256": empreinte(f)})
    src = _gardes_saines(depot, f)                                                        # cas sain
    assert src["arret_sha256"] is None
    resume = nc.executer(_config(duree_max_juges_s=ECHUS), depot, run, None, str(f), autoriser_depot_sale=True)
    assert resume["arret_source_sha256"] is None and {j["statut"] for j in resume["juges"].values()} == {"échu"}
    assert _fichiers(depot, run) == ["resume.json"]


def test_recouvrement_avec_les_descriptives_d_un_run_complet(depot, monkeypatch):
    """Run source complet (résumé, notations descriptives de e2) : demander e2 arrête (on ne renote jamais)."""
    f = _source(depot, monkeypatch)
    with pytest.raises(GardeArret, match="juge jouet-8B : 1 couples déjà notés"):
        nc.executer(_config(COMPLET), depot, "20261027-110006-complement-jouet", None, str(f),
                    autoriser_depot_sale=True)
    src = nc.charger_source(depot, COMPLET, list(JUGES))
    assert len(src["notations_presentes"]) == 4 and src["arret"] is None


def test_graines_absentes_ou_differentes_de_la_source():
    source = {"manifeste": {"graines": graines(["a", "b"], 7)}}
    nc.exiger_graines_de_la_source(["a", "b"], 7, source)                                 # cas sain
    with pytest.raises(GardeArret, match="entropie ≠ celle du run source"):
        nc.exiger_graines_de_la_source(["a", "b"], 8, source)
    with pytest.raises(GardeArret, match="1 clés absentes du manifeste du run source \\(dont 'c'\\)"):
        nc.exiger_graines_de_la_source(["a", "c"], 7, source)
    source["manifeste"]["graines"]["b"] = {**source["manifeste"]["graines"]["b"], "spawn_key": ["0"]}
    with pytest.raises(GardeArret, match="graines ≠ celles du run source pour 1 clés"):
        nc.exiger_graines_de_la_source(["a", "b"], 7, source)


def test_cle_egale_absente_du_run_source():
    source = {"manifeste": {"config": {k: _config()[k] for k in nc.CLES_EGALES_A_LA_SOURCE if k != "fils"}}}
    with pytest.raises(GardeArret, match="fils absent de la configuration du run source"):
        nc.exiger_egal_a_la_source(_config(), source, "jouet")
    source["manifeste"]["config"]["fils"] = _config()["fils"]
    nc.exiger_egal_a_la_source(_config(), source, "jouet")                                # cas sain


def test_garde_des_versions_en_mode_reel(depot, monkeypatch):
    _source(depot, monkeypatch)
    src = nc.charger_source(depot, PILOTE, list(JUGES))
    vs = src["manifeste"]["versions"]
    monkeypatch.setattr(nc, "versions", lambda: dict(vs))
    nc.exiger_egal_a_la_source(_config(), src, "reel")                                    # cas sain
    for b in nc.VERSIONS_EGALES:
        monkeypatch.setattr(nc, "versions", lambda b=b: {**vs, b: "0.0.essai"})
        with pytest.raises(GardeArret, match=rf"versions ≠ celles du run source : \['{b}'\]"):
            nc.exiger_egal_a_la_source(_config(), src, "reel")


def _prereg(depot, valeurs, nom, lignes_en_plus=()):
    (depot / "prereg").mkdir(exist_ok=True)
    p = depot / "prereg" / nom
    lignes = [f"- {k} : `{v}`" for k, v in valeurs.items() if v is not None] + list(lignes_en_plus)
    corps = ["# Préenregistrement de test", "", *lignes, ""]
    for s in ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
              "Critères de lecture gelés", "Liste d'arrêt"):
        corps += [f"## {s}", "", f"contenu {s}", ""]
    corps += ["## Contre-lecture", "", f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`", ""]
    p.write_text("\n".join(corps), encoding="utf-8")
    sceller(p)
    return p


def test_gardes_de_citation_cas_sain_et_artefacts(depot, monkeypatch):
    """Chaque citation fausse, absente ou doublée arrête avant le manifeste ; le préenregistrement sain lance un run
    décisif (juges échus : aucune notation) ; « aucun » est l'arrêt attendu d'un run source sans arrêt."""
    f = _source(depot, monkeypatch)
    monkeypatch.setattr(nc, "exiger_code_importe_sous", lambda racine: None)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    d = depot / "diag" / PILOTE
    c = _config(duree_max_juges_s=ECHUS)
    sains = {"Commit du code d'analyse": commit,
             "Configuration du complément (empreinte canonique)": lp.empreinte_config(c),
             "Run source noté": PILOTE,
             "Manifeste du run source": empreinte(depot / "runs" / PILOTE / "manifeste.json"),
             "Épisodes du run source": empreinte(d / "episodes.json"),
             "Arrêt du run source": empreinte(d / "arret.json"),
             "Notations déjà présentes dans le run source": hashlib.sha256(b"[]").hexdigest(),
             "Tâches du pilote": empreinte(f), "Entropie": ENTROPIE}
    sain = _prereg(depot, sains, "prereg-complement.md")
    faux = {"Configuration du complément (empreinte canonique)": ("1" * 64, "configuration"),
            "Run source noté": ("20261027-100009-autre", "run source"),
            "Manifeste du run source": ("2" * 64, "manifeste"), "Épisodes du run source": ("3" * 64, "épisodes"),
            "Arrêt du run source": ("aucun", "arrêt"),
            "Notations déjà présentes dans le run source": ("4" * 64, "notations présentes"),
            "Tâches du pilote": ("5" * 64, "tâches"), "Entropie": (ENTROPIE + 1, "entropie ≠ celle du run source")}
    cas = []
    for k, (v, motif) in faux.items():
        cas.append((_prereg(depot, {**sains, k: v}, f"p-faux-{len(cas)}.md"), motif))                   # fausse
    for k in sains:
        motif = "commit du code d'analyse" if k == "Commit du code d'analyse" else "cité nulle part"
        cas.append((_prereg(depot, {**sains, k: None}, f"p-absent-{len(cas)}.md"), motif))              # absente
        cas.append((_prereg(depot, sains, f"p-double-{len(cas)}.md", (f"- {k} : `{sains[k]}`",)),
                    "cité 2 fois"))                                                                       # doublée
    committer(depot)
    for p, motif in cas:
        with pytest.raises(GardeArret, match=motif):
            nc.executer(c, depot, "20261027-110007-complement-jouet", str(p), str(f))
    assert not (depot / "runs" / "20261027-110007-complement-jouet").exists()
    run = "20261027-110008-complement-jouet"
    resume = nc.executer(c, depot, run, str(sain), str(f), autoriser_depot_sale=True)
    assert resume["commit_cite"] == commit
    m = json.loads((depot / "runs" / run / "manifeste.json").read_text())
    assert m["decisif"] and m["preenregistrement"]["chemin"] == "prereg/prereg-complement.md"
    # run source sans arrêt (résumé seul) : « aucun » est la citation attendue
    src = nc.charger_source(depot, PILOTE, list(JUGES))
    src["arret_sha256"] = None
    with pytest.raises(GardeArret, match="arrêt"):
        nc.exiger_citations_complement(sain, c, empreinte(f), src)
    p = _prereg(depot, {**sains, "Arrêt du run source": "aucun"}, "p-aucun.md")
    assert nc.exiger_citations_complement(p, c, empreinte(f), src) == ENTROPIE


def test_echeance_par_juge(depot, monkeypatch):
    f = _source(depot, monkeypatch)
    run = "20261027-110009-complement-jouet"
    resume = nc.executer(_config(duree_max_juges_s={"jouet-8B": 1e-9, "jouet-3B": 600}), depot, run, None, str(f),
                         autoriser_depot_sale=True)
    assert resume["juges"]["jouet-8B"]["statut"] == "échu" and resume["juges"]["jouet-8B"]["lots_faits"] == 0
    assert set(resume["juges"]["jouet-8B"]) == {"lots", "lots_faits", "statut", "duree_s", "memoire_pic_gio"}
    assert resume["juges"]["jouet-3B"]["statut"] == "écrit"
    assert _fichiers(depot, run) == ["notations-jouet-3B-decisives.json", "resume.json"]
    run = "20261027-110010-complement-jouet"
    with pytest.raises(GardeArret, match="limite de durée"):
        nc.executer(_config(duree_globale_s=1e-9), depot, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot, run) == ["arret.json"]
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["etape"] == "notations complementaires par jouet-8B" and r["partiel"]["run_source"] == PILOTE


def test_signal_term_pendant_le_3b(depot, monkeypatch):
    """Un TERM reçu pendant le premier lot du 3B (avalé par une bibliothèque : drapeau seul) arrête le run avant son
    deuxième lot : fichier du 8B écrit, aucun fichier du 3B, `arret.json` consigne l'étape et les lots faits."""
    f = _source(depot, monkeypatch, "3b")
    vrai = nc.noter_ensembles

    def noter(m, fmt, demandes, *a, **k):
        sortie = vrai(m, fmt, demandes, *a, **k)
        if demandes[0]["cle"].startswith("juge-jouet-3B/"):
            gardes.SIGNAL_TERM_RECU.append(15)
        return sortie

    monkeypatch.setattr(nc, "noter_ensembles", noter)
    run = "20261027-110011-complement-jouet"
    c = _config(TROIS_B, notations_a_faire=A_FAIRE_3B, notations_attendues_par_juge={"jouet-8B": 1, "jouet-3B": 4})
    with pytest.raises(GardeArret, match="signal TERM reçu"):
        nc.executer(c, depot, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot, run) == ["arret.json", "notations-jouet-8B-decisives.json"]
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["etape"] == "notations complementaires par jouet-3B" and gardes.MOTIF_TERM in r["motif"]
    assert r["partiel"]["juges"]["jouet-3B"] == {"lots": 2, "lots_faits": 1, "statut": "en cours"}


def test_fonctions_de_la_chaine_importees_sans_copie():
    assert nc.noter_ensembles is pa.noter_ensembles and nc.demandes_de_notation is lp.demandes_de_notation
    assert nc.passes_de is lp.passes_de and nc.controler_format is lp.controler_format
