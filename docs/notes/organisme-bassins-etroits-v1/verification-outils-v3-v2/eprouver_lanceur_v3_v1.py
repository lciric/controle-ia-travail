"""Épreuves du vérificateur neuf (Claude Fable 5.2) sur le lanceur v3 de l'atelier « bassins étroits » — v1.

13 novembre 2026. Doublures seulement : le faux orchestrateur et la fixture `monde` des essais scellés du v3 sont repris
tels quels (module chargé par son chemin). Aucun modèle, aucun réseau, aucune dépense, aucune écriture dans le dépôt hors
du dossier temporaire de pytest. Le lanceur n'est jamais lancé avec ses réglages de production : `Reglages.production()`
ne sert ici qu'à des lectures (`runs_du_lanceur`, `depense_run`, `relance_permise`). Chaque épreuve affirme le
comportement **observé** ; le rapport dit lesquels sont des défauts.

Usage (racine du dépôt) : PYTHONPATH=src .venv/bin/python -B -m pytest -q -p no:cacheprovider <ce fichier> -v
"""
import hashlib
import importlib.util
import json
import os
import shutil
import signal
import subprocess
import sys
import time
import types
from pathlib import Path

import pytest

DEPOT = Path("/home/user/controle-ia-travail")
ICI = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("essais_v3_scelles", DEPOT / "tests" / "test_lancer_course_ideation_bassins_etroits_v3.py")
tm = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = tm
_spec.loader.exec_module(tm)
lc = tm.lc
monde = tm.monde                      # fixture des essais scellés
COUPLES = json.loads((ICI / "couples-epingle-lanceur-v3-v1.json").read_text(encoding="utf-8"))


def _attendre_fichier(p: Path, s: float = 20.0):
    fin = time.time() + s
    while time.time() < fin:
        if p.exists() and Path(str(p) + ".sha256").exists():
            return True
        time.sleep(0.05)
    return False


# ------------------------------------------------------------------------------------------------ P1 : état réel, en lecture
def test_p1_etat_reel_la_relance_de_la_generation_1_est_refusee_dans_ce_conteneur():
    r = lc.Reglages.production()
    runs = [x for x in lc.runs_du_lanceur(r) if x["generation"] == 1]
    assert [x["version"] for x in runs] == ["lancer_course_ideation_bassins_etroits_v2"]
    sup = runs[0]["depart"]["superviseur"]
    hors_depot = Path(sup["dossier"]).parent
    assert not hors_depot.exists(), "le dossier de sortie hors dépôt du run du v2 est absent de ce conteneur"
    d = lc.depense_run(runs[0])
    assert d["course_usd"] == 20.0 and d["course_lisible"] is False and "sans fin propre" in d["lecture"]
    ok, motif = lc.relance_permise(runs)
    assert not ok and "dépense illisible" in motif
    assert runs[0]["fin"]["code"] == 2 and runs[0]["fin"]["code_scelle"]["code"] == 2   # le dépôt, lui, porte la fin propre
    assert lc.garde_cumul(lc.runs_du_lanceur(r), 20.0, 60.0)["depense_relevee_usd"] == 20.0


# ------------------------------------------------------------------------------------------------ P2 : fenêtre R3
def test_p2_mort_entre_detachement_et_manifeste_de_depart(monde, capsys, monkeypatch):
    monde["env"]["FAUX_DORT"] = "2"
    vrai = lc.ecrire_scelle

    def panne(chemin, contenu):
        if Path(chemin).name == "manifeste-lanceur-depart.json":
            raise OSError("mort simulée après le détachement")
        return vrai(chemin, contenu)
    monkeypatch.setattr(lc, "ecrire_scelle", panne)
    with pytest.raises(OSError):                       # `principal` ne garde que Refus : trace, aucun PID imprimé
        lc.principal(["1"], monde["r"])
    sortie = capsys.readouterr()
    assert "pid_superviseur" not in sortie.out
    monkeypatch.undo()
    runs_dir = monde["r"].dossier_runs
    (nom,) = os.listdir(runs_dir)
    assert not (runs_dir / nom / "manifeste-lanceur-depart.json").exists()
    assert not (runs_dir / nom / "manifeste-lanceur-refus.json").exists()
    sup = monde["r"].dossier_sorties / nom / "superviseur-course"
    assert _attendre_fichier(sup / "pid-orchestrateur.json")      # la course tourne, non suivie
    for _ in range(200):                                # le faux orchestrateur consigne son départ
        if [j["mode"] for j in tm.journal(monde)] == ["mesure", "course"]:
            break
        time.sleep(0.05)
    assert [j["mode"] for j in tm.journal(monde)] == ["mesure", "course"]
    for g in (1, 2, 3):                                 # tout lancement suivant est refusé, toute génération
        code, err = tm.lancer(monde, g, capsys)
        assert code == 2 and "état inconnu" in err
    assert _attendre_fichier(sup / "code.json")        # elle finit seule ; le refus demeure
    try:
        os.waitpid(-1, 0)
    except ChildProcessError:
        pass
    code, err = tm.lancer(monde, 1, capsys)
    assert code == 2 and "état inconnu" in err
    assert [j["mode"] for j in tm.journal(monde)] == ["mesure", "course"]     # aucune autre dépense


# ------------------------------------------------------------------------------------------------ P3 : dossier hors dépôt perdu
def test_p3a_perte_entiere_du_dossier_hors_depot_apres_des_fiches(monde, capsys):
    monde["env"]["FAUX_CODE"] = "2"
    assert tm.jouer(monde, 1, capsys)[0] == 0
    run = tm.run_de(monde, 1)[0]
    shutil.rmtree(run["sortie"].parent)
    d = lc.depense_run(tm.run_de(monde, 1)[0])
    assert d["course_usd"] == 20.0 and not d["course_lisible"]
    code, err = tm.lancer(monde, 1, capsys)
    assert code == 2 and "dépense illisible" in err


def test_p3b_perte_de_la_seule_sortie_apres_des_fiches_la_relance_part(monde, capsys):
    monde["env"]["FAUX_CODE"] = "2"                     # course en défaut après des fiches, 4,5 USD relevés
    assert tm.jouer(monde, 1, capsys)[0] == 0
    run = tm.run_de(monde, 1)[0]
    assert lc.depense_run(run)["course_usd"] == pytest.approx(4.5) and lc.fiches_produites(run["sortie"]) is not False
    shutil.rmtree(run["sortie"])                        # la sortie seule disparaît ; superviseur-course/code.json reste
    d = lc.depense_run(tm.run_de(monde, 1)[0])
    assert d["course_usd"] == 0.0 and d["course_lisible"] is True      # 4,5 USD relus 0, « rien parti »
    assert lc.relance_permise(tm.run_de(monde, 1))[0] is True          # et la relance est permise après des fiches
    code, _ = tm.lancer(monde, 1, capsys)
    assert code == 0
    tm.attendre(monde)


# ------------------------------------------------------------------------------------------------ P4 : environnement
def test_p4_environnement_reel_noms_seulement():
    garde, desc = lc.environnement_permis(os.environ, Path("/x/pyc"), Path("/x/home"))
    assert set(garde) <= set(lc.NOMS_PERMIS) | {"GO_ID", "HOME", "PYTHONPYCACHEPREFIX"}
    assert garde["HOME"] == "/x/home" and garde["GO_ID"] == "GO-2026-11-13-03"
    assert not [n for n in garde if n.startswith(("CLAUDE", "ANTHROPIC", "CCR")) or "PROXY" in n.upper()]
    assert "CLAUDE_CODE_REMOTE" not in garde
    texte = json.dumps(desc)
    for n in desc["noms_exclus"]:                       # aucune valeur d'un nom exclu dans la description (valeurs ≥ 8 caractères)
        v = os.environ.get(n, "")
        if len(v) >= 8 and v not in desc["noms_exclus"] and v not in desc["noms_transmis"]:
            assert v not in texte
    print("\nP4 noms transmis :", desc["noms_transmis"], "; exclus :", len(desc["noms_exclus"]),
          "; CLAUDE_CODE_REMOTE présent dans la session :", "CLAUDE_CODE_REMOTE" in os.environ)


def test_p4b_manifeste_de_depart_sans_valeur_et_orchestrateur_sans_nom_d_hote(monde, capsys):
    monde["env"]["FAUX_DORT"] = "0"
    assert tm.jouer(monde, 1, capsys)[0] == 0
    run = tm.run_de(monde, 1)[0]
    texte = (run["dossier"] / "manifeste-lanceur-depart.json").read_text(encoding="utf-8")
    for valeur in ("valeur-factice-d-essai", "http://hote.invalid", "http://mandataire.invalid", "--x"):
        assert valeur not in texte
    for j in tm.journal(monde):
        assert not [n for n in j["noms_env"] if n.startswith(("CLAUDE", "ANTHROPIC", "CCR")) or n in ("HTTPS_PROXY", "NODE_OPTIONS")]
        assert j["home"] != monde["env"]["HOME"]


# ------------------------------------------------------------------------------------------------ P5 : une relance par génération
def test_p5_une_relance_par_generation_donc_trois_au_plus_sur_la_ligne(monde, capsys):
    tm.generation_complete(monde, 1, capsys)
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", "0.3"
    assert tm.jouer(monde, 2, capsys)[0] == 0           # génération 2 : défaut au contrôle
    del monde["env"]["FAUX_CONTROLE_SEUL"]
    assert tm.jouer(monde, 2, capsys)[0] == 0           # relance de la génération 2 : permise aussi
    assert len([x for x in tm.run_de(monde, 2) if x["depart"]]) == 2


# ------------------------------------------------------------------------------------------------ P6 : orphelin sans fichier de PID
def test_p6_orphelin_non_vu_si_le_superviseur_meurt_avant_d_ecrire_le_pid(monde, capsys):
    monde["env"]["FAUX_DORT"] = "30"
    assert tm.lancer(monde, 1, capsys)[0] == 0
    sup = tm.run_de(monde, 1)[0]["depart"]["superviseur"]
    p = tm._tuer_superviseur(monde, sup)
    pidf = Path(sup["dossier"]) / "pid-orchestrateur.json"
    pidf.unlink()                                       # artefact : comme si le superviseur était mort avant de l'écrire
    Path(str(pidf) + ".sha256").unlink()
    try:
        code, sortie = tm.lancer(monde, 1, capsys)
        assert code == 0 and "mort sans fin propre" in sortie and "ENCORE VIVANT" not in sortie
        assert lc.debut_processus(p["pid_orchestrateur"]) is not None      # l'orchestrateur vit, non signalé
        code, err = tm.lancer(monde, 1, capsys)
        assert code == 2 and "sans fin propre" in err                      # mais plafond compté, génération verrouillée
    finally:
        os.kill(p["pid_orchestrateur"], signal.SIGKILL)                    # par PID


# ------------------------------------------------------------------------------------------------ P7 : le lanceur ne se garde pas lui-même
def test_p7_le_lanceur_ne_verifie_ni_sa_propre_empreinte_ni_son_mode_isole():
    source = (DEPOT / "scripts" / "lancer_course_ideation_bassins_etroits_v3.py").read_text(encoding="utf-8")
    assert source.count("sha256_fichier(Path(__file__))") == 2            # deux écritures au manifeste, aucune comparaison
    for ligne in source.splitlines():
        if "sha256_fichier(Path(__file__))" in ligne:
            assert '"sha256": sha256_fichier(Path(__file__))' in ligne
    assert "sys.flags" not in source and "os.getcwd" not in source
    assert "ligne_sha256" in source and source.count("ligne_sha256") == 1  # empreinte de la ligne de GO écrite, non comparée


# ------------------------------------------------------------------------------------------------ P8 : crochet, joué à la main
def _jouer_crochet(commande, cwd=str(DEPOT)):
    p = subprocess.run([sys.executable, "-I", "-B", str(DEPOT / ".claude" / "hooks" / "garde_calcul.py")],
                       input=json.dumps({"tool_input": {"command": commande}, "cwd": cwd}), capture_output=True, text=True)
    return p.returncode, p.stderr


def test_p8_crochet_actuel_joue_a_la_main():
    code, err = _jouer_crochet("sha256sum scripts/lancer_course_ideation_bassins_etroits_v2.py")
    assert code == 2 and "bassins étroits" in err       # la même commande est passée dans ma session à 17:59 UTC
    assert _jouer_crochet("/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v2.py 1")[0] == 0
    # le crochet actuel ne connaît pas le v3 : sa commande, et toute variante, passent
    assert _jouer_crochet("/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v3.py 1")[0] == 0
    assert _jouer_crochet("python3 scripts/lancer_course_ideation_bassins_etroits_v3.py 3", "/tmp")[0] == 0


# ------------------------------------------------------------------------------------------------ P9 : couples de l'épingle
def _appliquer(texte, couples):
    for c in couples:
        assert texte.count(c["avant"]) == 1, c["nom"]
        texte = texte.replace(c["avant"], c["apres"])
    return texte


def _crochet_corrige():
    chemin = DEPOT / ".claude" / "hooks" / "garde_calcul.py"
    octets = chemin.read_bytes()
    assert hashlib.sha256(octets).hexdigest() == COUPLES["crochet"]["sha256_avant"]
    source = _appliquer(octets.decode("utf-8"), COUPLES["crochet"]["couples"])
    m = types.ModuleType("garde_calcul_corrige")
    m.__file__ = str(chemin)                            # RACINE reste le dépôt ; rien n'est écrit
    exec(compile(source, str(chemin), "exec"), m.__dict__)
    return m


def _decide(m, commande, cwd=str(DEPOT)):
    import datetime
    try:
        m.decider(commande, datetime.date(2026, 11, 13), cwd)
    except SystemExit as e:
        return e.code
    return 0


def test_p9_couples_du_crochet(capsys):
    m = _crochet_corrige()
    v3 = "/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v3.py"
    v2 = "/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v2.py"
    assert _decide(m, v3 + " 1") == 0                                           # cas sain
    for artefact in (v3 + " 2", v3 + " 3", v3, v3 + " 1 2", v3 + " 1 ", "python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v3.py 1",
                     v3.replace(" -I -B", "") + " 1", "sha256sum scripts/lancer_course_ideation_bassins_etroits_v3.py",
                     "cd /tmp && " + v3 + " 1", v3 + " 1 ; echo x"):
        assert _decide(m, artefact) == 2, artefact
    assert _decide(m, v3 + " 1", "/tmp") == 2 and _decide(m, v3 + " 1", None) == 2      # autre dossier, dossier absent
    for artefact in (v2 + " 1", v2 + " 2", "sha256sum scripts/lancer_course_ideation_bassins_etroits_v2.py"):
        assert _decide(m, artefact) == 2, artefact                              # épingle du v2 retirée : plus rien ne passe
    assert _decide(m, "python -m pytest -q tests/test_lancer_course_ideation_bassins_etroits_v3.py") == 0   # les essais
    assert _decide(m, "ls scripts") == 0
    assert _decide(m, "pkill python") == 2                                      # R10 intact
    assert _decide(m, "/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_pilier_attaque_v2_v3.py") in (0, 2)
    m.EMPREINTE_LANCEUR_BE3 = "0" * 64                                          # artefact : épingle différente du fichier
    assert _decide(m, v3 + " 1") == 2
    capsys.readouterr()


def test_p9b_couples_des_reglages():
    chemin = DEPOT / ".claude" / "settings.json"
    octets = chemin.read_bytes()
    assert hashlib.sha256(octets).hexdigest() == COUPLES["reglages"]["sha256_avant"]
    neuf = json.loads(_appliquer(octets.decode("utf-8"), COUPLES["reglages"]["couples"]))
    assert neuf["permissions"]["allow"] == ["Bash(/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v3.py 1)"]
    assert len(neuf["permissions"]["deny"]) == 5 and "hooks" in neuf
