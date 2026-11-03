"""Gardes de la mini-course, version 2 : artefacts demandés par la contre-lecture (CLM-02, CLM-03, CLM-06, CLM-09, CLM-10, CLM-13),
chacun avec un cas sain, sans réseau ni dépense. Rédigé le 1er novembre 2026 (sous-agent de session-depot).

`python -m pytest -q nuit/repetition/test_gardes_mini_course_v2.py` depuis `orchestrateur/` (les essais v1 restent valables :
`test_gardes_mini_course_v1.py`). Le piège du lanceur et le contrôle en échec sont éprouvés par `repetition_complete_v2.sh`.
"""

import json
import os
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
NUIT = os.path.dirname(ICI)
RACINE = os.path.dirname(NUIT)
sys.path.insert(0, RACINE)
sys.path.insert(0, NUIT)

import chercher_cles_v1 as cc  # noqa: E402
import commande_argon_v56_nuit_v2 as cmd_argon  # noqa: E402
import lancer_mini_course_v2 as lanceur  # noqa: E402
import registre_depense_cumulee_v1 as reg  # noqa: E402
import trace_agregee_mini_course_v2 as trace  # noqa: E402
from pole import course2_nuit_v2 as nuit  # noqa: E402
from pole.configuration_v53 import GoRefuse  # noqa: E402
from pole.simulation_v56 import AdaptateurSimuleV56  # noqa: E402

CONF_CHEMIN = os.path.join(NUIT, "configuration-mini-course-kimi-argon-v2.json")
REGISTRE_GO = "/home/user/controle-ia-travail/registres/go.md"
PY = "/usr/bin/python3"
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PLAFOND_SESSION_USD": "0.25", "ROLE_POLE": "juge_ideation"}


def lancer_commande(script, args, environ, entree="consigne d'essai"):
    p = subprocess.run([PY, "-I", "-B", os.path.join(NUIT, script)] + args, input=entree.encode("utf-8"),
                       capture_output=True, env=environ, timeout=60)
    return p.returncode, json.loads(p.stdout.decode().strip().splitlines()[-1])


def commande_factice(tmp_path, nom, objet, code):
    p = tmp_path / f"{nom}.py"
    p.write_text(f"import json, sys\nsys.stdin.read()\nprint(json.dumps({objet!r}))\nsys.exit({code})\n", encoding="utf-8")
    return [PY, "-I", "-B", str(p)]


def adaptateur(commande):
    return nuit.AdaptateurCommandeExterneNuitV2(commande, environnement={"PATH": "/usr/bin:/bin"}, delai_s=60, exiger_modele_servi=True)


# --- CLM-02 : dépassement de réserve = arrêt de la course ----------------------------------------------------------------------


def test_adaptateur_v2_depassement_reserve(tmp_path):
    sain = adaptateur(commande_factice(tmp_path, "ok", {"texte": "x", "cout_usd": 0.01, "modele_servi": "m"}, 0))
    assert sain.lancer("juge_ideation", "c", str(tmp_path), 0.25, 1, modele="m").statut == "ok"
    art = adaptateur(commande_factice(tmp_path, "dep", {"texte": "", "cout_usd": 0.3, "modele_servi": "m", "depassement_reserve": True,
                                                        "erreur": "coût lu au-dessus du pire cas réservé (liste d'arrêt)"}, 5))
    with pytest.raises(nuit.ArretDepassementReserve):
        art.lancer("juge_ideation", "c", str(tmp_path), 0.25, 1, modele="m")


@pytest.fixture
def relais_argon(tmp_path):
    """Serveur réel du relais Argon (`fabriquer_gestion`), appelant factice réglable, boucle locale."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("coll", cmd_argon.COLLISIONNEUR_DEFAUT)
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)
    reglage = {"servi": "gemini-4-argon", "sortie": 5, "plafond": 10.0, "max_appels": 10}
    etat = {}

    def appelant(modele, prompt, mt):
        return c.Reponse(texte="réponse", modele_servi=reglage["servi"], fin="STOP", usage={"entree": 10, "sortie": reglage["sortie"]})

    def demarrer():
        e = cmd_argon.EtatRelais(reglage["plafond"], reglage["max_appels"], ["gemini-4-argon"], str(tmp_path / "j.jsonl"),
                                 cmd_argon.SHA_COLLISIONNEUR)
        e.nature_appelant = "essai"
        s = HTTPServer(("127.0.0.1", 0), cmd_argon.fabriquer_gestion(e, appelant, c, str))
        threading.Thread(target=s.serve_forever, daemon=True).start()
        etat["s"] = s
        return f"http://127.0.0.1:{s.server_address[1]}"
    yield demarrer, reglage
    if "s" in etat:
        etat["s"].shutdown()
        etat["s"].server_close()


def args_argon(url, r):
    return ["appeler", "--url-relais", url, "--registre", r, "--plafond-cumule-usd", "10"]


def test_commande_argon_depassement_reserve_bout_en_bout(tmp_path, relais_argon):
    demarrer, reglage = relais_argon
    url, r = demarrer(), str(tmp_path / "r.jsonl")
    env = dict(ENV, MODELE_DEMANDE_POLE="gemini-4-argon")
    code, o = lancer_commande("commande_argon_v56_nuit_v2.py", args_argon(url, r), env)
    assert code == 0 and not o.get("depassement_reserve")  # sain
    reglage["sortie"] = 1_000_000  # usage lu très au-dessus du pire cas réservé
    code, o = lancer_commande("commande_argon_v56_nuit_v2.py", args_argon(url, r), env)
    assert code == 5 and o["depassement_reserve"] is True and reg.etat(r)["depassements_reserve"] == 1


# --- CLM-03 : garde cumulée côté Argon, plafonds du relais Argon, refus sans clé ---------------------------------------------------


def test_commande_argon_garde_cumulee(tmp_path, relais_argon):
    demarrer, _ = relais_argon
    url, r = demarrer(), str(tmp_path / "r.jsonl")
    env = dict(ENV, MODELE_DEMANDE_POLE="gemini-4-argon")
    assert lancer_commande("commande_argon_v56_nuit_v2.py", args_argon(url, r), env)[0] == 0  # sain
    i = reg.reserver(r, plafond_cumule_usd=10, pire_cas_usd=9.9, fournisseur="kimi", role="j", modele="m")
    reg.regler(r, i, cout_usd=9.9, pire_cas_usd=9.9, statut="ok", code=0, cout_origine="usage")
    code, o = lancer_commande("commande_argon_v56_nuit_v2.py", args_argon(url, r), env)
    assert code == 4 and o["envoye"] is False and o["erreur"].startswith("garde cumulée")
    cmd = [PY, "-I", "-B", os.path.join(NUIT, "commande_argon_v56_nuit_v2.py")] + args_argon(url, r)
    with pytest.raises(nuit.ArretPlafondCumule):  # CLM-09 : motif distinct, arrêt de la course
        adaptateur(cmd).lancer("juge_ideation", "c", str(tmp_path), 0.25, 1, modele="gemini-4-argon")


def test_relais_argon_plafond_402(tmp_path, relais_argon):
    demarrer, reglage = relais_argon
    reglage["plafond"] = 0.05  # sous le pire cas d'un appel court (≈ 0,2 USD)
    url = demarrer()
    code, o = lancer_commande("commande_argon_v56_nuit_v2.py", args_argon(url, str(tmp_path / "r.jsonl")),
                              dict(ENV, MODELE_DEMANDE_POLE="gemini-4-argon"))
    assert code == 4 and o["erreur"].startswith("HTTP 402") and o["envoye"] is False


def test_relais_argon_max_appels_429(tmp_path, relais_argon):
    demarrer, reglage = relais_argon
    reglage["max_appels"] = 1
    url, r = demarrer(), str(tmp_path / "r.jsonl")
    env = dict(ENV, MODELE_DEMANDE_POLE="gemini-4-argon")
    assert lancer_commande("commande_argon_v56_nuit_v2.py", args_argon(url, r), env)[0] == 0  # sain : premier appel
    code, o = lancer_commande("commande_argon_v56_nuit_v2.py", args_argon(url, r), env)
    assert code == 4 and o["erreur"].startswith("HTTP 429")
    cmd = [PY, "-I", "-B", os.path.join(NUIT, "commande_argon_v56_nuit_v2.py")] + args_argon(url, r)
    with pytest.raises(nuit.ArretPlafondRelais):
        adaptateur(cmd).lancer("juge_ideation", "c", str(tmp_path), 0.25, 1, modele="gemini-4-argon")


def test_relais_argon_modele_non_permis(tmp_path, relais_argon):
    demarrer, _ = relais_argon
    url = demarrer()
    code, o = lancer_commande("commande_argon_v56_nuit_v2.py", args_argon(url, str(tmp_path / "r.jsonl")) + ["--modele", "gemini-autre"],
                              dict(ENV, MODELE_DEMANDE_POLE="gemini-autre"))
    assert code == 3 and o["erreur"].startswith("HTTP 403")


def test_relais_argon_refus_sans_cle(tmp_path):
    import argparse
    a = argparse.Namespace(port=0, plafond_usd=1.0, max_appels=1, journal=str(tmp_path / "j"), modeles_permis="gemini-4-argon",
                           collisionneur=cmd_argon.COLLISIONNEUR_DEFAUT, sha_collisionneur=cmd_argon.SHA_COLLISIONNEUR)
    with pytest.raises(SystemExit, match="GEMINI_API_KEY absente"):
        cmd_argon.servir(a, environ={})
    b = argparse.Namespace(**dict(vars(a), sha_collisionneur="0" * 64))
    with pytest.raises(SystemExit, match="empreinte"):  # collisionneur à empreinte différente : refus de servir
        cmd_argon.servir(b, environ={"GEMINI_API_KEY": "cle-factice-0123456789"})


# --- CLM-03 : 502 « modèle servi » du relais Kimi, converti par la commande ------------------------------------------------------


@pytest.fixture
def faux_relais_kimi():
    reglage = {"mode": "ok"}

    class G(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            corps = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            if reglage["mode"] == "502":
                b = json.dumps({"error": {"message": "modèle servi différent du modèle demandé (R-764) : réponse non relayée"}}, ensure_ascii=False).encode()  # comme relais_kimi_v3 (ensure_ascii=False, l. 464)
                self.send_response(502)
            else:
                b = json.dumps({"model": corps["model"], "choices": [{"message": {"content": "réponse"}, "finish_reason": "stop"}],
                                "usage": {"prompt_tokens": 10, "completion_tokens": 5}}).encode()
                self.send_response(200)
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)
    s = HTTPServer(("127.0.0.1", 0), G)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{s.server_address[1]}", reglage
    s.shutdown()
    s.server_close()


def test_commande_kimi_502_modele_servi(tmp_path, faux_relais_kimi):
    url, reglage = faux_relais_kimi
    args = ["--url-relais", url, "--registre", str(tmp_path / "r.jsonl"), "--plafond-cumule-usd", "10"]
    env = dict(ENV, MODELE_DEMANDE_POLE="kimi-k3.1-pro")
    code, o = lancer_commande("commande_kimi_v2.py", args, env)
    assert code == 0 and o["modele_servi"] == "kimi-k3.1-pro"  # sain
    reglage["mode"] = "502"
    code, o = lancer_commande("commande_kimi_v2.py", args, env)
    assert code == 5 and o["modele_servi"] == "ecart-signale-par-le-relais"
    cmd = [PY, "-I", "-B", os.path.join(NUIT, "commande_kimi_v2.py")] + args
    with pytest.raises(nuit.ArretModeleServiDifferent):
        adaptateur(cmd).lancer("juge_ideation", "c", str(tmp_path), 0.25, 1, modele="kimi-k3.1-pro")


# --- CLM-03 : révocation lue à travers l'extrait ; GO_ID autre ---------------------------------------------------------------------


def registre(tmp_path, *lignes):
    p = tmp_path / "go.md"
    p.write_text(lanceur.EN_TETE_GO + "".join(l + "\n" for l in lignes), encoding="utf-8")
    return str(p)


LIGNE = "| GO-2026-11-01-12 | 2026-11-01 | calcul | essai | 10 USD | 2099-12-31 | Lazar | r |"


def test_go_revocation_dans_l_extrait(tmp_path):
    ligne, lecture = lanceur.verifier_go_nuit("GO-2026-11-01-12", registre(tmp_path, LIGNE), 10.0)  # sain
    assert ligne["plafond_lu_usd"] == 10.0 and lecture["lignes_extraites"] == 1
    d = tmp_path / "art"
    d.mkdir()
    rev = "| GO-2026-11-01-90 | 2026-11-01 | révocation | révoque GO-2026-11-01-12 | 0 USD | 2099-12-31 | Lazar | essai |"
    with pytest.raises(GoRefuse, match="révoqué"):
        lanceur.verifier_go_nuit("GO-2026-11-01-12", registre(d, LIGNE, rev), 10.0)


def test_go_id_autre(tmp_path):
    base = ["verifier", "--configuration", CONF_CHEMIN, "--registre-go", REGISTRE_GO]
    assert lanceur.principal(base, environnement={"GO_ID": "GO-2026-11-01-12"}) == 0  # sain
    assert lanceur.principal(base, environnement={"GO_ID": "GO-2026-11-01-11"}) == 2


# --- CLM-06 : recherche des clés -------------------------------------------------------------------------------------------------


def test_chercher_cles(tmp_path):
    (tmp_path / "a.txt").write_text("rien de secret", encoding="utf-8")
    env = {"K1": "cle-factice-abcdefgh", "K2": "cle-factice-ijklmnop"}
    assert cc.principal([str(tmp_path), "K1", "K2"], env) == 0  # sain
    (tmp_path / "sous").mkdir()
    (tmp_path / "sous" / "b.json").write_text('{"x": "cle-factice-ijklmnop"}', encoding="utf-8")
    assert cc.principal([str(tmp_path), "K1", "K2"], env) == 6
    assert cc.principal([str(tmp_path), "K3"], env) == 2  # variable absente : aucun repli silencieux


# --- CLM-09, CLM-10, CLM-13 : trace v2 -----------------------------------------------------------------------------------------


def test_trace_v2_motifs_et_o12():
    assert trace.classer_fin({"arret": "ArretDepassementReserve : x"})["motif_arret"] == "depassement_reserve"
    assert trace.classer_fin({"arret": "ArretPlafondCumule : x"})["motif_arret"] == "plafond_cumule"
    assert trace.classer_fin({"arret": "ArretPlafondRelais : x"})["motif_arret"] == "plafond_relais"
    assert trace.classer_fin({"arret": None, "noeud": None})["fin"] == "generation_terminee"
    assert trace.tester_garde() == {"cas_sain": True, "artefacts": True}


def test_trace_v2_l4_sans_fusion_et_arret_non_calcule(tmp_path):
    conf = lanceur.lire_conf(CONF_CHEMIN)
    ad = {f: AdaptateurSimuleV56(champs_fiche=conf["champs_fiche"], items=conf["items_juge"], champ_titre="titre",
                                 cout_par_appel_usd=0.01, fiches_par_appel=6) for f in ("kimi", "argon")}
    nuit.executer_mini_course_v1(conf, str(tmp_path / "ok" / "course"), ad, go={"moteur": "simule"})
    t, permises, canaris, contenus, titres = trace.agreger(str(tmp_path / "ok"), json.load(open(CONF_CHEMIN, encoding="utf-8")))
    trace.valider_liste_blanche(t, permises)
    assert t["l1"]["l3_l4"] == "calcules" and t["l4"]["meme_famille"]["n"] == 12 and t["l4"]["autre_famille"]["n"] == 12

    def dec(role, consigne, modele, n):
        return {"statut": "erreur"} if "RÔLE : JUGE" in consigne else None
    ad2 = {f: AdaptateurSimuleV56(champs_fiche=conf["champs_fiche"], items=conf["items_juge"], champ_titre="titre",
                                  cout_par_appel_usd=0.01, fiches_par_appel=6, decider=dec if f == "argon" else None)
           for f in ("kimi", "argon")}
    with pytest.raises(nuit.ArretTroisEchecs):
        nuit.executer_mini_course_v1(conf, str(tmp_path / "arret" / "course"), ad2, go={"moteur": "simule"})
    t2 = trace.agreger(str(tmp_path / "arret"), json.load(open(CONF_CHEMIN, encoding="utf-8")))[0]
    assert t2["l1"]["l3_l4"] == "non_calcules_o12" and t2["verdicts"] == [] and t2["l3"]["accord"]["kappa_cohen"] is None


def test_commande_argon_v2_echec_au_pire_cas_sans_faux_depassement(tmp_path):
    """Correction trouvée par la répétition v2 : un échec de l'interface est compté au pire cas réservé exactement, jamais au-dessus
    (la v1 lisait l'arrondi du relais et pouvait marquer un faux dépassement de réserve, qui arrête la course en v2)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("coll2", cmd_argon.COLLISIONNEUR_DEFAUT)
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)
    e = cmd_argon.EtatRelais(10, 10, ["gemini-4-argon"], str(tmp_path / "j.jsonl"), cmd_argon.SHA_COLLISIONNEUR)
    e.nature_appelant = "essai"
    s = HTTPServer(("127.0.0.1", 0), cmd_argon.fabriquer_gestion(e, lambda m, p, t: c.Reponse(echec="connexion : essai"), c, str))
    threading.Thread(target=s.serve_forever, daemon=True).start()
    try:
        r = str(tmp_path / "r.jsonl")
        for prompt in ("Réponds seulement par le mot OK.", "x" * 1001, "é" * 37):  # longueurs qui donnaient un arrondi au-dessus
            code, o = lancer_commande("commande_argon_v56_nuit_v2.py", args_argon(f"http://127.0.0.1:{s.server_address[1]}", r),
                                      dict(ENV, MODELE_DEMANDE_POLE="gemini-4-argon"), entree=prompt)
            assert code == 3 and o["cout_origine"] == "pire_cas" and not o.get("depassement_reserve")
        assert reg.etat(r)["depassements_reserve"] == 0
        cmd = [PY, "-I", "-B", os.path.join(NUIT, "commande_argon_v56_nuit_v2.py")] + args_argon(f"http://127.0.0.1:{s.server_address[1]}", r)
        assert adaptateur(cmd).lancer("juge_ideation", "c", str(tmp_path), 0.25, 1, modele="gemini-4-argon").statut == "erreur"
    finally:
        s.shutdown()
        s.server_close()
