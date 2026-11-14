"""Vérification courte du lanceur v2 — outil 2 : épreuves du lancement détaché sous superviseur (M7) et des états que la
commande relancée rencontre, sur le faux orchestrateur des essais du v2 (aucun modèle, aucun réseau).

Écrit par le contre-lecteur (Claude Fable 5.2), 13 novembre 2026. Fichier d'essais pytest : il réemploie le monde factice de
`tests/test_lancer_course_ideation_bassins_etroits_v2.py` (chargé par son chemin, non modifié). Chaque épreuve **constate** ce
que fait le lanceur et l'écrit dans le fichier JSON nommé par la variable `RESULTATS` ; ses assertions sont les constats que la
vérification rapporte (un échec voudrait dire que mon rapport est faux). Les processus lancés sont arrêtés par leur PID.

Usage : RESULTATS=<fichier.json> <python avec pytest> -B -m pytest -q -p no:cacheprovider --basetemp <dossier> eprouver_detache_v2.py
"""
import importlib.util
import json
import os
import signal
import sys
import threading
import time
from pathlib import Path

import pytest

RACINE = Path("/home/user/controle-ia-travail")
_spec = importlib.util.spec_from_file_location("essais_du_v2", RACINE / "tests" / "test_lancer_course_ideation_bassins_etroits_v2.py")
t = importlib.util.module_from_spec(_spec)
sys.modules["essais_du_v2"] = t
_spec.loader.exec_module(t)
lc = t.lc
monde = t.monde          # le monde factice des essais du v2 (fixture)


def noter(nom, objet):
    chemin = os.environ.get("RESULTATS")
    if not chemin:
        return
    d = json.loads(Path(chemin).read_text()) if Path(chemin).exists() else {}
    d[nom] = objet
    Path(chemin).write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n")


def pid_orchestrateur(sup, delai=10.0):
    f = Path(sup["dossier"]) / "pid-orchestrateur.json"
    fin = time.time() + delai
    while time.time() < fin:
        if f.exists() and Path(str(f) + ".sha256").exists():
            return json.loads(f.read_text())["pid_orchestrateur"]
        time.sleep(0.05)
    raise AssertionError("pid-orchestrateur.json absent")


def attendre_fin(pid, delai=30.0):
    fin = time.time() + delai
    while time.time() < fin:
        if lc.debut_processus(pid) is None:
            return True
        time.sleep(0.1)
    return False


def tuer(pid):
    try:
        os.kill(pid, signal.SIGKILL)
    except OSError:
        pass
    try:
        os.waitpid(pid, 0)
    except (ChildProcessError, OSError):
        pass


def test_p1_deux_lancements_concurrents(monde, capsys, monkeypatch):
    """Deux invocations qui ont toutes deux lu l'état avant que l'une crée son dossier de run (entrelacement forcé par une
    barrière posée à la sonde du bac à sable, dernière étape avant la création du dossier)."""
    monde["env"]["FAUX_DORT"] = "2"
    barriere = threading.Barrier(2, timeout=60)
    vraie = lc.sonder_bac_a_sable

    def sonde(*a, **k):
        res = vraie(*a, **k)
        barriere.wait()
        return res
    monkeypatch.setattr(lc, "sonder_bac_a_sable", sonde)
    codes = []

    def lance():
        codes.append(lc.principal(["1"], monde["r"]))
    fils = [threading.Thread(target=lance) for _ in range(2)]
    for f in fils:
        f.start()
    for f in fils:
        f.join(120)
    monkeypatch.undo()
    capsys.readouterr()
    runs = t.run_de(monde, 1)
    t.attendre(monde)
    courses = [j for j in t.journal(monde) if j["mode"] == "course"]
    c1, s1 = t.lancer(monde, 1, capsys)
    c2, s2 = t.lancer(monde, 1, capsys)
    cumul = lc.garde_cumul(lc.runs_du_lanceur(monde["r"]), 0.0, 60.0)["depense_relevee_usd"]
    noter("P1_deux_lancements_concurrents", {
        "codes_des_deux_invocations": sorted(codes), "runs_avec_manifeste_de_depart": len([x for x in runs if x["depart"]]),
        "courses_lancees_par_l_orchestrateur": len(courses), "pids_distincts": len({j["pid"] for j in courses}),
        "relance_1": [c1, s1.strip()[:160]], "relance_2": [c2, s2.strip()[:200]], "depense_relevee_usd": cumul})
    assert sorted(codes) == [0, 0] and len(courses) == 2          # deux courses de la même génération sont parties
    assert c2 == 2 and "2 courses réussies" in s2                 # la suite est un refus (nœud), dépense des deux comptée


def test_p2_lanceur_mort_entre_le_detachement_et_le_manifeste(monde, capsys, monkeypatch):
    monde["env"]["FAUX_DORT"] = "3"
    sups = []
    vrai_detache, vrai_ecrire = lc.lancer_detache, lc.ecrire_scelle

    def detache(*a, **k):
        s = vrai_detache(*a, **k)
        sups.append(s)
        return s

    def ecrire(chemin, contenu):
        if chemin.name == "manifeste-lanceur-depart.json":
            raise RuntimeError("mort simulée du lanceur après le détachement")
        return vrai_ecrire(chemin, contenu)
    monkeypatch.setattr(lc, "lancer_detache", detache)
    monkeypatch.setattr(lc, "ecrire_scelle", ecrire)
    with pytest.raises(RuntimeError):
        lc.principal(["1"], monde["r"])
    monkeypatch.undo()
    capsys.readouterr()
    vivant = lc.superviseur_vivant(sups[0])
    c1, s1 = t.lancer(monde, 1, capsys)
    c2, s2 = t.lancer(monde, 2, capsys)
    try:
        os.waitpid(sups[0]["pid"], 0)
    except ChildProcessError:
        pass
    c3, s3 = t.lancer(monde, 1, capsys)
    d = next(monde["r"].dossier_runs.iterdir())
    noter("P2_lanceur_mort_entre_detachement_et_manifeste", {
        "superviseur_vivant_sans_manifeste": vivant, "fichiers_du_dossier_de_run": sorted(p.name for p in d.iterdir()),
        "course_jouee_par_l_orchestrateur": [j["mode"] for j in t.journal(monde)],
        "relance_pendant": [c1, s1.strip()[:170]], "relance_generation_2": [c2, s2.strip()[:120]],
        "relance_apres_la_fin": [c3, s3.strip()[:120]]})
    assert vivant and c1 == 2 and "état inconnu" in s1 and c3 == 2 and "état inconnu" in s3


def test_p3_superviseur_tue_orchestrateur_orphelin(monde, capsys):
    monde["env"]["FAUX_DORT"] = "5"
    assert t.lancer(monde, 1, capsys)[0] == 0
    run = t.run_de(monde, 1)[0]
    sup = run["depart"]["superviseur"]
    pid = pid_orchestrateur(sup)
    tuer(sup["pid"])
    c1, s1 = t.lancer(monde, 1, capsys)
    orphelin_vivant = lc.debut_processus(pid) is not None
    c2, s2 = t.lancer(monde, 1, capsys)
    c3, s3 = t.lancer(monde, 2, capsys)
    fini = attendre_fin(pid)
    run = t.run_de(monde, 1)[0]
    fin_orchestrateur = (run["sortie"] / "manifeste-fin.json").exists()
    dep = lc.depense_run(run)
    c4, s4 = t.lancer(monde, 1, capsys)
    noter("P3_superviseur_tue_orchestrateur_orphelin", {
        "cloture": [c1, s1.strip()[:260]], "orchestrateur_orphelin_vivant_apres_la_cloture": orphelin_vivant,
        "pid_de_l_orphelin_dit_dans_la_cloture": str(pid) in s1, "relance_meme_generation": [c2, s2.strip()[:140]],
        "relance_generation_2": [c3, s3.strip()[:140]], "orphelin_fini_seul": fini,
        "course_finie_par_l_orphelin_manifeste_de_fin_present": fin_orchestrateur, "depense_run": dep,
        "relance_apres_la_fin_de_l_orphelin": [c4, s4.strip()[:140]]})
    assert c1 == 0 and "mort sans fin propre" in s1 and orphelin_vivant and str(pid) not in s1
    assert c2 == 2 and "verrouillée" in s2 and c3 == 2 and dep["course_usd"] == 20.0 and c4 == 2


def test_p4_bras_superviseur_tue(monde, capsys):
    assert t.jouer(monde, 1, capsys)[0] == 0
    t.attester(monde, 1)
    monde["env"]["FAUX_DORT_BRAS"] = "20"
    assert t.lancer(monde, 1, capsys)[0] == 0
    run = t.run_de(monde, 1)[0]
    sup = run["bras"][0]["depart"]["superviseur"]
    pid = pid_orchestrateur(sup)
    c0, s0 = t.lancer(monde, 1, capsys)
    tuer(sup["pid"])
    c1, s1 = t.lancer(monde, 1, capsys)
    dep = lc.depense_run(t.run_de(monde, 1)[0])
    c2, s2 = t.lancer(monde, 1, capsys)
    c3, s3 = t.lancer(monde, 2, capsys)
    try:
        os.kill(pid, signal.SIGKILL)                              # l'orphelin, par son PID
    except OSError:
        pass
    noter("P4_bras_superviseur_tue", {"pendant_le_bras": [c0, s0.strip()[:120]], "cloture": [c1, s1.strip()[:200]],
                                       "depense_run": dep, "relance": [c2, s2.strip()[:170]], "generation_2": [c3, s3.strip()[:120]]})
    assert c0 == 3 and c1 == 0 and dep["bras_usd"] == pytest.approx(lc.PLAFOND_BRAS_USD) and c2 == 2 and c3 == 2


def test_p5_exception_au_detachement_du_bras(monde, capsys, monkeypatch):
    assert t.jouer(monde, 1, capsys)[0] == 0
    t.attester(monde, 1)

    def panne(*a, **k):
        raise OSError("panne simulée au détachement du bras")
    monkeypatch.setattr(lc, "lancer_detache", panne)
    try:
        code, exc = lc.principal(["1"], monde["r"]), None
    except BaseException as e:  # noqa: BLE001 — c'est l'objet de l'épreuve
        code, exc = None, type(e).__name__
    monkeypatch.undo()
    capsys.readouterr()
    c1, s1 = t.lancer(monde, 1, capsys)
    d = t.run_de(monde, 1)[0]["dossier"]
    noter("P5_exception_au_detachement_du_bras", {
        "premiere_invocation": {"code": code, "exception_non_gardee": exc},
        "manifestes_du_run": sorted(p.name for p in d.iterdir() if "bras" in p.name or "refus" in p.name),
        "relance": [c1, s1.strip()[:200]]})
    assert exc == "OSError" and c1 == 2 and "déjà présent" in s1


@pytest.mark.parametrize("cout,verrou", [(0.01, True), (5e-6, False), (1.1e-5, True)])
def test_p6_seuil_sans_depense(monde, capsys, cout, verrou):
    monde["env"]["FAUX_CODE"], monde["env"]["FAUX_RIEN"] = "2", "1"
    assert t.jouer(monde, 1, capsys)[0] == 0
    run = t.run_de(monde, 1)[0]
    c = Path(str(run["sortie"]) + "-controle")
    (c / "tentative-1").mkdir(parents=True)
    t.sceller(c / "tentative-1.json", json.dumps({"reglages": {"cout_claude_usd": cout, "cout_externe_usd": 0.0}}))
    dep = lc.depense_run(t.run_de(monde, 1)[0])
    monde["env"]["FAUX_CODE"], monde["env"]["FAUX_RIEN"] = "0", "0"
    code, s = t.lancer(monde, 1, capsys)
    noter(f"P6_seuil_sans_depense_{cout!r}", {"depense_relevee": dep["course_usd"], "relance": [code, s.strip()[:120]]})
    assert (code == 2 and "verrouillée" in s) if verrou else code == 0


def test_p7_zombie_et_pid_d_un_autre_processus():
    import subprocess
    p = subprocess.Popen([sys.executable, "-c", "pass"])
    time.sleep(0.5)                                               # fini, non récolté : zombie
    etat_zombie = lc.debut_processus(p.pid)
    p.wait()
    moi = {"pid": os.getpid(), "debut_proc": lc.debut_processus(os.getpid())}
    autre = {"pid": os.getpid(), "debut_proc": str(int(moi["debut_proc"]) + 1)}
    noter("P7_zombie_et_pid_reutilise", {"debut_processus_d_un_zombie": etat_zombie,
                                          "vivant_meme_pid_meme_depart": lc.superviseur_vivant(moi),
                                          "vivant_meme_pid_autre_depart": lc.superviseur_vivant(autre)})
    assert etat_zombie is None and lc.superviseur_vivant(moi) and not lc.superviseur_vivant(autre)
