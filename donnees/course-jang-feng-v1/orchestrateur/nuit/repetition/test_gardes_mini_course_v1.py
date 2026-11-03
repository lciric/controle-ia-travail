"""Gardes de la mini-course éprouvées sur un cas sain et sur un artefact (R5), sans réseau ni dépense — version 1.

Rédigé le 1er novembre 2026 (sous-agent de session-depot). `python3 -m pytest -q nuit/repetition/test_gardes_mini_course_v1.py`
depuis le dossier `orchestrateur/`. Aucun appel de modèle : commandes factices, relais Argon servi sur la boucle locale avec un
appelant factice, moteur simulé v56.
"""

import copy
import json
import os
import subprocess
import sys
import threading
from http.server import HTTPServer

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
NUIT = os.path.dirname(ICI)
RACINE = os.path.dirname(NUIT)
sys.path.insert(0, RACINE)
sys.path.insert(0, NUIT)

import commande_argon_v56_nuit_v1 as cmd_argon  # noqa: E402
import lancer_mini_course_v1 as lanceur  # noqa: E402
import registre_depense_cumulee_v1 as reg  # noqa: E402
import trace_agregee_mini_course_v1 as trace  # noqa: E402
from pole import course2_nuit_v1 as nuit  # noqa: E402
from pole.configuration_v53 import ConfigurationRefusee, GoRefuse  # noqa: E402
from pole.simulation_v56 import AdaptateurSimuleV56  # noqa: E402

CONF_CHEMIN = os.path.join(NUIT, "configuration-mini-course-kimi-argon-v1.json")
REGISTRE_GO = "/home/user/controle-ia-travail/registres/go.md"
PY = "/usr/bin/python3"


def conf_lue():
    return lanceur.lire_conf(CONF_CHEMIN)


# --- registre cumulé -------------------------------------------------------------------------------------------------------


def test_registre_cumule_sain_et_artefact(tmp_path):
    r = str(tmp_path / "reg.jsonl")
    i = reg.reserver(r, plafond_cumule_usd=10, pire_cas_usd=9.0, fournisseur="kimi", role="juge_ideation", modele="m")
    reg.regler(r, i, cout_usd=9.0, pire_cas_usd=9.0, statut="ok", code=0, cout_origine="usage")
    reg.reserver(r, plafond_cumule_usd=10, pire_cas_usd=0.5, fournisseur="argon", role="juge_ideation", modele="m")  # sain
    with pytest.raises(reg.PlafondCumule):  # artefact : 9 réglés + 0,5 engagés + 0,6 > 10
        reg.reserver(r, plafond_cumule_usd=10, pire_cas_usd=0.6, fournisseur="argon", role="juge_ideation", modele="m")
    assert reg.etat(r)["engage_usd"] == 0.5  # l'appel non réglé reste compté à son pire cas


def test_registre_garde_etape(tmp_path):
    r = str(tmp_path / "reg.jsonl")
    reg.reserver(r, plafond_cumule_usd=10, pire_cas_usd=0.2, fournisseur="kimi", role="j", modele="m", etape="juges",
                 plafond_etape_usd=0.3)
    reg.reserver(r, plafond_cumule_usd=10, pire_cas_usd=0.2, fournisseur="argon", role="j", modele="m", etape="autre",
                 plafond_etape_usd=0.3)  # sain : autre étape
    with pytest.raises(reg.PlafondCumule):
        reg.reserver(r, plafond_cumule_usd=10, pire_cas_usd=0.2, fournisseur="argon", role="j", modele="m", etape="juges",
                     plafond_etape_usd=0.3)


def test_registre_illisible(tmp_path):
    r = tmp_path / "reg.jsonl"
    r.write_text('{"type": "fin", "id": "x", "cout_usd": 1}\n', encoding="utf-8")
    with pytest.raises(reg.RegistreIllisible):
        reg.etat(str(r))


# --- commandes ---------------------------------------------------------------------------------------------------------------


def lancer_commande(script, args, environ, entree="consigne d'essai"):
    p = subprocess.run([PY, "-I", "-B", os.path.join(NUIT, script)] + args, input=entree.encode("utf-8"),
                       capture_output=True, env=environ, timeout=60)
    return p.returncode, json.loads(p.stdout.decode().strip().splitlines()[-1])


ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PLAFOND_SESSION_USD": "0.25", "ROLE_POLE": "juge_ideation"}


def test_commande_kimi_refuse_sans_envoi_au_plafond_cumule(tmp_path):
    r = str(tmp_path / "reg.jsonl")
    i = reg.reserver(r, plafond_cumule_usd=10, pire_cas_usd=9.9, fournisseur="argon", role="j", modele="m")
    reg.regler(r, i, cout_usd=9.9, pire_cas_usd=9.9, statut="ok", code=0, cout_origine="usage")
    code, o = lancer_commande("commande_kimi_v2.py", ["--url-relais", "http://127.0.0.1:9", "--registre", r,
                                                      "--plafond-cumule-usd", "10"], dict(ENV, MODELE_DEMANDE_POLE="kimi-k3.1-pro"))
    assert code == 4 and o["envoye"] is False and "garde cumulée" in o["erreur"] and o["cout_usd"] == 1e-6


def test_commande_kimi_relais_absent_sain(tmp_path):
    """Cas sain de la garde : sous le plafond, la commande réserve, tente l'envoi (relais absent : rien n'est parti), règle."""
    r = str(tmp_path / "reg.jsonl")
    code, o = lancer_commande("commande_kimi_v2.py", ["--url-relais", "http://127.0.0.1:9", "--registre", r,
                                                      "--plafond-cumule-usd", "10"], dict(ENV, MODELE_DEMANDE_POLE="kimi-k3.1-pro"))
    assert code == 3 and o["envoye"] is False and reg.etat(r)["appels"] == 1 and reg.etat(r)["engage_usd"] == 0


def test_commande_kimi_porte_incomplete(tmp_path):
    code, o = lancer_commande("commande_kimi_v2.py", ["--registre", str(tmp_path / "r.jsonl"), "--plafond-cumule-usd", "10"],
                              dict(ENV, ETAPE_POLE="juges"))
    assert code == 2 and "porte" in o["erreur"]


@pytest.fixture
def relais_argon(tmp_path):
    """Relais Argon réel (serveur de `commande_argon_v56_nuit_v1`), appelant factice réglable, boucle locale."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("coll", cmd_argon.COLLISIONNEUR_DEFAUT)
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)
    reglage = {"servi": "gemini-4-argon", "fin": "STOP"}

    def appelant(modele, prompt, mt):
        return c.Reponse(texte="réponse", modele_servi=reglage["servi"], fin=reglage["fin"], usage={"entree": 10, "sortie": 5})
    etat = cmd_argon.EtatRelais(10, 10, ["gemini-4-argon"], str(tmp_path / "j.jsonl"), cmd_argon.SHA_COLLISIONNEUR)
    etat.nature_appelant = "essai"
    serveur = HTTPServer(("127.0.0.1", 0), cmd_argon.fabriquer_gestion(etat, appelant, c, str))
    t = threading.Thread(target=serveur.serve_forever, daemon=True)
    t.start()
    yield f"http://127.0.0.1:{serveur.server_address[1]}", reglage
    serveur.shutdown()
    serveur.server_close()


def test_commande_argon_modele_servi(tmp_path, relais_argon):
    url, reglage = relais_argon
    args = ["appeler", "--url-relais", url, "--registre", str(tmp_path / "r.jsonl"), "--plafond-cumule-usd", "10"]
    env = dict(ENV, MODELE_DEMANDE_POLE="gemini-4-argon")
    code, o = lancer_commande("commande_argon_v56_nuit_v1.py", args, env)
    assert code == 0 and o["modele_servi"] == "gemini-4-argon"  # sain
    reglage["servi"] = "gemini-4-argon-preview"
    code, o = lancer_commande("commande_argon_v56_nuit_v1.py", args, env)
    assert code == 5 and o["modele_servi"] == "gemini-4-argon-preview"  # artefact
    reglage.update(servi="gemini-4-argon", fin="SAFETY")
    code, o = lancer_commande("commande_argon_v56_nuit_v1.py", args, env)
    assert code == 5 and o.get("refus") is True


def test_adaptateur_nuit_arrete_sur_modele_servi(tmp_path):
    def commande(servi):
        p = tmp_path / f"c-{servi}.py"
        p.write_text("import json, sys\nsys.stdin.read()\nprint(json.dumps({'texte': 'x', 'cout_usd': 0.01, 'modele_servi': %r}))\n"
                     % servi, encoding="utf-8")
        return [PY, "-I", "-B", str(p)]
    env = {"PATH": "/usr/bin:/bin"}
    ok = nuit.AdaptateurCommandeExterneNuitV1(commande("m-essai"), environnement=env, delai_s=30, exiger_modele_servi=True)
    assert ok.lancer("juge_ideation", "c", str(tmp_path), 0.1, 1, modele="m-essai").statut == "ok"
    autre = nuit.AdaptateurCommandeExterneNuitV1(commande("m-autre"), environnement=env, delai_s=30, exiger_modele_servi=True)
    with pytest.raises(nuit.ArretModeleServiDifferent):
        autre.lancer("juge_ideation", "c", str(tmp_path), 0.1, 1, modele="m-essai")


# --- génération (moteur simulé) -----------------------------------------------------------------------------------------------


def simules(conf, decider_argon=None):
    s = conf["simulation"]
    return {f: AdaptateurSimuleV56(champs_fiche=conf["champs_fiche"], items=conf["items_juge"], champ_titre=conf["champ_titre"],
                                   cout_par_appel_usd=s["cout_par_appel_usd"], fiches_par_appel=6,
                                   decider=decider_argon if f == "argon" else None) for f in ("kimi", "argon")}


def test_generation_saine_sans_passe_tableau(tmp_path):
    conf = conf_lue()
    ad = simules(conf)
    res = nuit.executer_mini_course_v1(conf, str(tmp_path / "c"), ad, go={"moteur": "simule"}, racine_sessions=str(tmp_path / "s"))
    assert res["noeud"] is None
    assert not any(a["tableau"] for x in ad.values() for a in x.appels)
    assert not os.path.exists(tmp_path / "c" / "generation-1" / "tableaux.json")
    assert sum(len(x.appels) for x in ad.values()) == 66


def test_trois_echecs_arretent_la_course(tmp_path):
    conf = conf_lue()

    def decider(role, consigne, modele, n):
        return {"statut": "erreur"} if "RÔLE : JUGE" in consigne else None
    with pytest.raises(nuit.ArretTroisEchecs):
        nuit.executer_mini_course_v1(conf, str(tmp_path / "c"), simules(conf, decider), go={"moteur": "simule"},
                                     racine_sessions=str(tmp_path / "s"))
    bilan = json.load(open(tmp_path / "c" / "bilan-course.json", encoding="utf-8"))
    assert "ArretTroisEchecs" in bilan["arret"]


def test_debordement_kimi_arrete_la_course(tmp_path):
    conf = conf_lue()

    def decider(role, consigne, modele, n):
        return {"texte": json.dumps({"classe": "concret", "categorie": "essai"})} if "RÔLE : AIGUILLEUR" in consigne else None
    with pytest.raises(nuit.ArretDebordementKimi):
        nuit.executer_mini_course_v1(conf, str(tmp_path / "c"), simules(conf, decider), go={"moteur": "simule"},
                                     racine_sessions=str(tmp_path / "s"))


def test_configuration_nuit_artefacts():
    conf = conf_lue()
    assert nuit.verifier_configuration_nuit(conf)
    for chemin, valeur in ((("bisociateur", "bras"), ["basique", "meta"]), (("aiguilleur", "fournisseur"), "claude")):
        c = copy.deepcopy(conf)
        c[chemin[0]][chemin[1]] = valeur
        with pytest.raises(ConfigurationRefusee):
            nuit.verifier_configuration_nuit(c)
    c = copy.deepcopy(conf)
    next(e for e in c["budget"]["etapes"] if e["nom"] == "passe_tableau")["plafond_relais_usd"] = 0.5
    with pytest.raises(ConfigurationRefusee):
        nuit.verifier_configuration_nuit(c)


# --- lanceur : GO, pièces gelées, spécification --------------------------------------------------------------------------------


def test_go_sain_et_artefacts(tmp_path):
    ligne, lecture = lanceur.verifier_go_nuit("GO-2026-11-01-12", REGISTRE_GO, 10.0)
    assert ligne["plafond_lu_usd"] == 10.0 and lecture["lignes_extraites"] == 1
    with pytest.raises(GoRefuse):  # montant requis différent
        lanceur.verifier_go_nuit("GO-2026-11-01-12", REGISTRE_GO, 9.0)
    faux = tmp_path / "go.md"
    faux.write_text(lanceur.EN_TETE_GO + "| GO-2026-11-01-12 | 2026-11-01 | calcul | essai | 10 USD | 2099-12-31 | Lazar | r |\n"
                    "| GO-2026-11-01-12 | 2026-11-01 | calcul | extension essai | 10 USD | 2099-12-31 | Lazar | r |\n",
                    encoding="utf-8")
    with pytest.raises(GoRefuse):  # ligne d'extension sur le GO cité
        lanceur.verifier_go_nuit("GO-2026-11-01-12", str(faux), 10.0)


def test_pieces_gelees_saines_et_artefact(tmp_path):
    from pole.outils import ecrire_scelle, sha256_fichier
    piece = "donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/pieces/concepts-mini-course-v1.json"
    vrai = sha256_fichier(os.path.join(lanceur.DEPOT, piece))
    ok = tmp_path / "ok.md"
    ecrire_scelle(str(ok), f"### Pièces gelées\n\n| `{piece}` | `{vrai}` | essai |\n")
    assert lanceur.verifier_pieces_gelees(str(ok))[0]["sha256"] == vrai
    faux = tmp_path / "faux.md"
    ecrire_scelle(str(faux), f"### Pièces gelées\n\n| `{piece}` | `{'0' * 64}` | essai |\n")
    with pytest.raises(lanceur.LancementRefuse):
        lanceur.verifier_pieces_gelees(str(faux))


def test_moteur_reel_refuse_sans_specification_scellee(tmp_path):
    sortie = tmp_path / "run" / "course"
    (tmp_path / "run").mkdir()
    code = lanceur.principal(["lancer", "--configuration", CONF_CHEMIN, "--sortie", str(sortie), "--registre-depense",
                              str(tmp_path / "run" / "r.jsonl"), "--registre-go", REGISTRE_GO, "--confirmer-moteur-reel",
                              "--preenregistrement", str(tmp_path / "absent.md"), "--contre-lecture", str(tmp_path / "absent2.md")],
                             environnement={"GO_ID": "GO-2026-11-01-12"})
    assert code == 2 and not sortie.exists() and os.listdir(tmp_path / "run") == []


# --- trace --------------------------------------------------------------------------------------------------------------------


def test_garde_de_la_trace():
    assert trace.tester_garde() == {"cas_sain": True, "artefacts": True}
