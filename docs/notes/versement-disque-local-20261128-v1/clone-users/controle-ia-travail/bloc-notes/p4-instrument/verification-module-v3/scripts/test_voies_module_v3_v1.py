"""Voies adverses contre le module v3 de P4-instrument (verificateur neuf). Chaque test monte un depot jouet jetable
(montage des tests du module v3, importes comme bibliotheque depuis une copie octet pour octet), joue une voie, et
consigne ce qui est constate (une ligne JSON par voie dans VOIES_SORTIE). Les assertions decrivent le constat ; elles ne
jugent pas : le jugement est dans le rapport.

Variables : COPIE_V3 (dossier de la copie du module v3), VOIES_SORTIE (fichier des constats), PYTHONPATH (src du depot).
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
from pathlib import Path  # noqa: E402

import pytest  # noqa: E402

COPIE = Path(os.environ["COPIE_V3"]).resolve()
if str(COPIE) not in sys.path:
    sys.path.insert(0, str(COPIE))

import instrument_p4_v1 as ip  # noqa: E402
import lecture_p4_v1 as lp  # noqa: E402
import test_gardes_p4_v1 as tg  # noqa: E402
import test_instrument_p4_v1 as ti  # noqa: E402

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.manifeste import creer_manifeste, ecrire_resultat, lire_manifeste, verifier_resultat  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402

SORTIE = Path(os.environ["VOIES_SORTIE"])
RACINE_REELLE = tg.RACINE_REELLE
RUN_D, RUN_X, RUN_Y = tg.RUN_DECISIF, tg.RUN_X, tg.RUN_Y
ENT = ti.ENTROPIE_JOUET
LECT = "20261020-200000-lecture-p4"


def consigner(voie: str, constat: str, **k) -> None:
    with open(SORTIE, "a", encoding="utf-8") as f:
        f.write(json.dumps({"voie": voie, "constat": constat, **k}, ensure_ascii=False) + "\n")


def arbre(d: Path) -> list:
    return sorted((str(p.relative_to(d)), p.is_symlink()) for p in d.rglob("*") if ".git" not in p.relative_to(d).parts)


def cli(d: Path, *args, b=True, env_extra=None, pythonpath=None):
    env = dict(os.environ, PYTHONPATH=str(pythonpath or (RACINE_REELLE / "src")))
    if env_extra:
        env.update(env_extra)
    cmd = [sys.executable] + (["-B"] if b else []) + [str(COPIE / "lecture_p4_v1.py"), *args]
    return subprocess.run(cmd, cwd=d, env=env, capture_output=True, text=True, timeout=900)


def decisif(tmp_path_factory, tmp_path, nom="d") -> Path:
    return ti.copie(tg.depot_decisif_partage(tmp_path_factory), tmp_path / nom)


def lecture_ecrite(d: Path, lecture: str) -> bool:
    return (d / "runs" / lecture).exists() or (d / "diag" / lecture).exists()


# ------------------------------------------------------------------------------------------------ A. sain et CL3-01

def test_a01_sain_run_jouet_non_decisif_lu_en_ligne_de_commande(tmp_path_factory, tmp_path):
    d0, run = ti.depot_p4(tmp_path_factory)
    d = ti.copie(d0, tmp_path / "d")
    r = cli(d, "--run-source", run, "--run-lecture", LECT, "--entropie", "4242")
    s = verifier_resultat(d, d / "diag" / LECT / "lecture-p4.json")["resultat"]
    assert r.returncode == 0 and s["source"]["etat"] == "complet" and lp.calcule(s["C1"])
    consigner("A01 sain : run jouet non décisif, ligne de commande, sans --prereg",
              f"code 0 ; source complète ; C1 calculé ; issue {s['issue']['ligne']}")


def test_a02_run_decisif_sans_prereg_ligne_de_commande(tmp_path_factory, tmp_path):
    d = decisif(tmp_path_factory, tmp_path)
    avant = arbre(d)
    r = cli(d, "--run-source", RUN_D, "--run-lecture", LECT, "--entropie", str(ENT))
    assert r.returncode == 1 and f"ARRÊT : {lp.MOTIF_SANS_PREREG}" in r.stderr and "Traceback" not in r.stderr
    assert arbre(d) == avant and not lecture_ecrite(d, LECT)
    consigner("A02 run décisif jouet, sans --prereg, ligne de commande", "ARRÊT, motif de CL3-01, code 1 ; rien écrit")


def test_a03_run_decisif_avec_prereg_sans_verdict(tmp_path_factory, tmp_path):
    d = decisif(tmp_path_factory, tmp_path)
    avant = arbre(d)
    r = cli(d, "--run-source", RUN_D, "--run-lecture", LECT, "--prereg", tg.PREREG, "--entropie", str(ENT))
    assert r.returncode == 1 and "verdict complété de P3 absent" in r.stderr and "Traceback" not in r.stderr
    assert arbre(d) == avant
    consigner("A03 run décisif jouet, --prereg, sans verdict complété", "ARRÊT « verdict complété de P3 absent … reportée » ; rien écrit")


def test_a04_run_en_mode_reel_sans_prereg(tmp_path_factory, tmp_path):
    d, run = tg.run_en_mode_reel(tmp_path_factory, tmp_path / "d")
    avant = arbre(d)
    r = cli(d, "--run-source", run, "--run-lecture", LECT, "--entropie", "4242")
    assert r.returncode == 1 and f"ARRÊT : {lp.MOTIF_SANS_PREREG}" in r.stderr and arbre(d) == avant
    consigner("A04 run en mode réel (non décisif), sans --prereg", "ARRÊT, motif de CL3-01 ; rien écrit")


# ------------------------------------------------------------------------------------------------ B. rattachement (-01)

FORMES = ["copies scellées : manifeste de X sous Y, résumé et identité du run décisif sous diag/Y",
          "liens physiques (os.link) au lieu de copies",
          "liens symboliques de fichiers : runs/Y/manifeste.json → X, diag/Y/resume.json → run décisif",
          "liens symboliques de dossiers : runs/Y → runs/X, diag/Y → diag/<run décisif>",
          "--run-source ../diag/<run décisif>, manifeste de X recopié dans diag/<run décisif>",
          "--run-source <run décisif>, manifeste de X recopié sur celui du run décisif",
          "--run-source <run décisif>, runs/<run décisif> remplacé par un lien vers runs/X",
          "--run-source Y/., Y monté par copies"]


def monter(d: Path, forme: str) -> str:
    dd, rx, ry, dy, rd = d / "diag" / RUN_D, d / "runs" / RUN_X, d / "runs" / RUN_Y, d / "diag" / RUN_Y, d / "runs" / RUN_D
    if forme.startswith("copies") or forme.startswith("--run-source Y/."):
        tg._copier_scelles(rx, ry, ["manifeste.json"])
        tg._copier_scelles(dd, dy, ["resume.json", "identite-p4.json"])
        source = RUN_Y if forme.startswith("copies") else RUN_Y + "/."
    elif forme.startswith("liens physiques"):
        ry.mkdir(parents=True)
        dy.mkdir(parents=True)
        for n in ("manifeste.json", "manifeste.json.sha256"):
            os.link(rx / n, ry / n)
        for n in ("resume.json", "resume.json.sha256", "identite-p4.json", "identite-p4.json.sha256"):
            os.link(dd / n, dy / n)
        source = RUN_Y
    elif forme.startswith("liens symboliques de fichiers"):
        ry.mkdir(parents=True)
        dy.mkdir(parents=True)
        for n in ("manifeste.json", "manifeste.json.sha256"):
            (ry / n).symlink_to(rx / n)
        for n in ("resume.json", "resume.json.sha256", "identite-p4.json", "identite-p4.json.sha256"):
            (dy / n).symlink_to(dd / n)
        source = RUN_Y
    elif forme.startswith("liens symboliques de dossiers"):
        ry.symlink_to(RUN_X)
        dy.symlink_to(RUN_D)
        source = RUN_Y
    elif forme.startswith("--run-source ../diag/"):
        tg._copier_scelles(rx, dd, ["manifeste.json"])
        source = f"../diag/{RUN_D}"
    elif forme.startswith("--run-source <run décisif>, manifeste de X"):
        for n in ("manifeste.json", "manifeste.json.sha256"):
            shutil.copyfile(rx / n, rd / n)
        source = RUN_D
    elif forme.startswith("--run-source <run décisif>, runs/<run décisif> remplacé"):
        shutil.rmtree(rd)
        rd.symlink_to(RUN_X)
        source = RUN_D
    ti.committer(d, forme[:60])
    return source


@pytest.mark.parametrize("forme", FORMES)
def test_b_donnees_d_un_autre_run_sans_prereg(tmp_path_factory, tmp_path, forme):
    d = decisif(tmp_path_factory, tmp_path)
    source = monter(d, forme)
    avant = arbre(d)
    r = cli(d, "--run-source", source, "--run-lecture", LECT, "--entropie", str(ENT))
    refuse = r.returncode == 1 and "ARRÊT : " in r.stderr and "Traceback" not in r.stderr
    motif = r.stderr.strip().splitlines()[-1][:200] if r.stderr.strip() else ""
    assert refuse and arbre(d) == avant and not lecture_ecrite(d, LECT), (r.returncode, r.stderr[-800:])
    consigner(f"B {forme}", f"refus, rien écrit ; {motif}")


def test_b09_fraude_par_les_fonctions_gelees_cr3_02(tmp_path_factory, tmp_path):
    """CR3-02 : run Y neuf non décisif (creer_manifeste), résumé et identité du run décisif réécrits sous ce manifeste
    (ecrire_resultat : run_id et empreinte de Y). Rien n'est rescellé à la main, mais deux résultats neufs sont écrits
    par les fonctions gelées : fraude délibérée. Constat : la lecture sans --prereg lit les tables du run décisif."""
    d = decisif(tmp_path_factory, tmp_path)
    dd = d / "diag" / RUN_D
    m, _ = lire_manifeste(d / "runs" / RUN_X / "manifeste.json")
    chemin_my, _ = creer_manifeste(d, RUN_Y, m["config"], ["x"], autoriser_depot_sale=True)
    identite = verifier_resultat(d, dd / "identite-p4.json")["resultat"]
    resume = verifier_resultat(d, dd / "resume.json")["resultat"]
    ch_id = ecrire_resultat(d, chemin_my, "identite-p4", identite)
    resume = dict(resume, identite_sha256=sceller(ch_id))
    ecrire_resultat(d, chemin_my, "resume", resume)
    ti.committer(d, "fraude CR3-02")
    r = cli(d, "--run-source", RUN_Y, "--run-lecture", LECT, "--entropie", str(ENT))
    s = verifier_resultat(d, d / "diag" / LECT / "lecture-p4.json")["resultat"]
    assert r.returncode == 0 and s["source"]["etat"] == "complet" and lp.calcule(s["C1"])
    assert s["resume_source"]["scores_sha256"] == verifier_resultat(d, dd / "resume.json")["resultat"]["scores_sha256"]
    consigner("B09 fraude par les fonctions gelées (CR3-02) : manifeste neuf de Y, résumé et identité du run décisif "
              "réécrits sous Y par ecrire_resultat", f"code 0 ; source complète ; C1 calculé (aire "
              f"{s['C1'].get('aire')}, état {s['C1'].get('etat')}) ; tables du run décisif lues (scores_sha256 égal) ; "
              "limite connue (CR3-02), non couverte par la lettre de -01")


# ------------------------------------------------------------------------------------------------ C. mode décisif et texte

def test_c01_mode_decisif_verdict_verse_manifeste_d_un_autre_run(tmp_path_factory, tmp_path):
    """Phrases 1 (troisième tiret) et 5 du rapport : « Dans tous les modes … le manifeste lu sous runs/<run source>/
    porte l'identifiant de ce run … sinon la lecture est refusée sans rien écrire ». Mode décisif, verdict complété versé,
    manifeste de X (non décisif) recopié sur celui du run décisif : constat de ce que fait le module."""
    d = decisif(tmp_path_factory, tmp_path)
    tg.verser_verdict(d)
    ti.committer(d, "verdict complété synthétique")
    for n in ("manifeste.json", "manifeste.json.sha256"):
        shutil.copyfile(d / "runs" / RUN_X / n, d / "runs" / RUN_D / n)
    ti.committer(d, "manifeste de X recopié sur celui du run décisif")
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(ip, "exiger_code_importe_sous", lambda racine: None)
        s = lp.analyser(d, RUN_D, LECT, tg.PREREG, entropie=ENT)
    assert s["issue"]["ligne"] == "L1" and "non décisif" in s["issue"]["motif"]
    ml, _ = lire_manifeste(d / "runs" / LECT / "manifeste.json")
    assert ml["decisif"] is True and (d / "diag" / LECT / "lecture-p4.json").is_file()
    e = decisif(tmp_path_factory, tmp_path, "e")
    for n in ("manifeste.json", "manifeste.json.sha256"):
        shutil.copyfile(e / "runs" / RUN_X / n, e / "runs" / RUN_D / n)
    ti.committer(e, "même montage, sans --prereg")
    with pytest.raises(GardeArret, match=re.escape(lp.AUTRE_RUN)):
        lp.analyser(e, RUN_D, LECT, None, entropie=ENT)
    consigner("C01 mode décisif, verdict versé, manifeste de X recopié sur celui du run décisif",
              f"L1 écrite sous un manifeste de lecture décisif ({s['issue']['motif'][:120]}) ; sans --prereg, même montage : "
              "refus AUTRE_RUN, rien écrit. Le texte proposé dit « dans tous les modes … refusée sans rien écrire »")


def test_c02_chemin_detourne_x_point_point_sans_dossier_x(tmp_path_factory, tmp_path):
    """« chemin détourné » de la phrase 1 : --run-source x/../<run décisif>, runs/x absent : le manifeste n'est pas lu."""
    d = decisif(tmp_path_factory, tmp_path)
    r = cli(d, "--run-source", f"x/../{RUN_D}", "--run-lecture", LECT, "--entropie", str(ENT))
    s = verifier_resultat(d, d / "diag" / LECT / "lecture-p4.json")["resultat"]
    ml, _ = lire_manifeste(d / "runs" / LECT / "manifeste.json")
    assert r.returncode == 0 and s["issue"]["ligne"] == "L1" and "C1" not in s and ml["decisif"] is False
    consigner("C02 --run-source x/../<run décisif>, runs/x absent, sans --prereg",
              f"L1 écrite sous un manifeste de lecture non décisif ({s['issue']['motif'][:90]}) ; aucune donnée lue "
              "(comportement -08 gardé, inchangé depuis le v2)")


# ------------------------------------------------------------------------------------------------ D. -04, CR3-04, -08

@pytest.mark.parametrize("config", [None, "reel", 3, [], ["x"], {"a": 1}])
def test_d_config_non_dictionnaire_rescelle_ligne_de_commande(tmp_path_factory, tmp_path, config):
    d = decisif(tmp_path_factory, tmp_path)
    ch = d / "runs" / RUN_D / "manifeste.json"
    m = json.loads(ch.read_text(encoding="utf-8"))
    m.pop("decisif")
    m["config"] = config
    import hashlib
    from controle_ia.manifeste import config_canonique
    m["config_sha256"] = hashlib.sha256(config_canonique(m["config"])).hexdigest()
    ch.with_name(ch.name + ".sha256").unlink()
    ch.write_text(json.dumps(m, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(ch)
    ti.committer(d, "config autre")
    avant = arbre(d)
    r = cli(d, "--run-source", RUN_D, "--run-lecture", LECT, "--entropie", str(ENT))
    if isinstance(config, dict):
        ecrit = (d / "diag" / LECT / "lecture-p4.json").is_file()
        consigner(f"D config = {config!r} (dictionnaire sans « mode »), « decisif » retiré, rescellé",
                  f"code {r.returncode} ; lecture écrite : {ecrit} (comportement du v2 gardé : « mode absent »)")
        return
    assert r.returncode == 1 and f"ARRÊT : {lp.MOTIF_SANS_PREREG}" in r.stderr and "Traceback" not in r.stderr
    assert arbre(d) == avant
    consigner(f"D config = {config!r}, « decisif » retiré, rescellé, sans --prereg", "ARRÊT, motif de CL3-01, code 1 ; sans trace ; rien écrit")


def test_d07_config_non_dictionnaire_sceau_rompu(tmp_path_factory, tmp_path):
    d = decisif(tmp_path_factory, tmp_path)
    ch = d / "runs" / RUN_D / "manifeste.json"
    m = json.loads(ch.read_text(encoding="utf-8"))
    m.pop("decisif")
    m["config"] = ["x"]
    ch.write_text(json.dumps(m, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    ti.committer(d, "config liste, sceau rompu")
    avant = arbre(d)
    r = cli(d, "--run-source", RUN_D, "--run-lecture", LECT, "--entropie", str(ENT))
    assert r.returncode == 1 and f"ARRÊT : {lp.MOTIF_SANS_PREREG}" in r.stderr and arbre(d) == avant
    consigner("D07 config = ['x'], « decisif » retiré, sceau rompu (contenu brut lu)", "ARRÊT, motif de CL3-01 ; rien écrit")


@pytest.mark.parametrize("contenu", ["[1, 2]", "\"texte\"", "null", "{\"run_id\": \"x\"}"])
def test_d08_manifeste_json_non_objet_ou_incomplet_scelle(tmp_path_factory, tmp_path, contenu):
    """CR3-04 (hors des décisions) : manifeste du run décisif remplacé par un JSON scellé qui n'est pas un objet, ou par
    un objet sans « config » : ce que fait la ligne de commande sans --prereg."""
    d = decisif(tmp_path_factory, tmp_path)
    ch = d / "runs" / RUN_D / "manifeste.json"
    ch.with_name(ch.name + ".sha256").unlink()
    ch.write_text(contenu + "\n", encoding="utf-8")
    sceller(ch)
    ti.committer(d, "manifeste remplacé")
    avant = arbre(d)
    r = cli(d, "--run-source", RUN_D, "--run-lecture", LECT, "--entropie", str(ENT))
    trace = "Traceback" in r.stderr
    derniere = r.stderr.strip().splitlines()[-1][:160] if r.stderr.strip() else ""
    ecrit = arbre(d) != avant
    consigner(f"D08 manifeste du run décisif = {contenu} (scellé), sans --prereg",
              f"code {r.returncode} ; trace Python : {trace} ; écrit : {ecrit} ; {derniere}")
    assert r.returncode != 0 or ecrit


def test_d09_manifeste_rescelle_sans_decisif_l1_gardee(tmp_path_factory, tmp_path):
    d = decisif(tmp_path_factory, tmp_path)
    ch = d / "runs" / RUN_D / "manifeste.json"
    m = json.loads(ch.read_text(encoding="utf-8"))
    m["decisif"] = False
    ch.with_name(ch.name + ".sha256").unlink()
    ch.write_text(json.dumps(m, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(ch)
    ti.committer(d, "decisif à false, rescellé")
    r = cli(d, "--run-source", RUN_D, "--run-lecture", LECT, "--entropie", str(ENT))
    s = verifier_resultat(d, d / "diag" / LECT / "lecture-p4.json")["resultat"]
    assert r.returncode == 0 and s["issue"]["ligne"] == "L1" and "C1" not in s and "M5" not in s
    consigner("D09 manifeste du run décisif, « decisif » à false, rescellé (-08)",
              f"L1 écrite ({s['issue']['motif'][:100]}) ; aucune donnée lue")


# ------------------------------------------------------------------------------------------------ E. -05

@pytest.mark.parametrize("forme", ["fichier ordinaire diag/<lecture>", "lien vers un dossier existant",
                                   "lien pendant", "dossier avec sous-dossier"])
def test_e_diag_de_lecture_present(tmp_path_factory, tmp_path, forme):
    d0, run = ti.depot_p4(tmp_path_factory)
    d = ti.copie(d0, tmp_path / "d")
    sortie = d / "diag" / LECT
    if forme.startswith("fichier"):
        sortie.write_text("x\n", encoding="utf-8")
    elif forme.startswith("lien vers"):
        sortie.symlink_to(run)
    elif forme == "lien pendant":
        sortie.symlink_to("absent")
    else:
        (sortie / "sous").mkdir(parents=True)
    avant = arbre(d)
    r = cli(d, "--run-source", run, "--run-lecture", LECT, "--entropie", "4242")
    assert r.returncode == 1 and "R12" in r.stderr and "Traceback" not in r.stderr
    assert arbre(d) == avant and not (d / "runs" / LECT).exists()
    consigner(f"E diag/<lecture> présent : {forme}", "ARRÊT R12 avant tout manifeste ; rien écrit, aucun runs/<lecture>")


# ------------------------------------------------------------------------------------------------ F. -06 (sans -B)

def _copier_src(tmp_path) -> Path:
    src = tmp_path / "src"
    shutil.copytree(RACINE_REELLE / "src" / "controle_ia", src / "controle_ia",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    return src


def _depot_module_verse(tmp_path_factory, tmp_path):
    d0, run = ti.depot_p4(tmp_path_factory)
    d = ti.copie(d0, tmp_path / "d")
    tg.verser_module(d)
    ti.committer(d, "module versé")
    return d, run, _copier_src(tmp_path)


def _caches(*racines):
    return [str(x) for r in racines for x in Path(r).rglob("*") if x.name == "__pycache__" or x.suffix == ".pyc"]


@pytest.mark.parametrize("cas", ["lecture lue (run jouet, sans --prereg)", "lecture refusée (run décisif, sans --prereg)",
                                 "contrôle du module refusé (instrument, --controle module)"])
def test_f_sans_option_b_aucun_cache(tmp_path_factory, tmp_path, cas):
    if cas.startswith("lecture refusée"):
        d = decisif(tmp_path_factory, tmp_path)          # module déjà versé et committé par le montage du run décisif
        assert (d / ip.DOSSIER_MODULE / "lecture_p4_v1.py").is_file()
        run, src = RUN_D, _copier_src(tmp_path)
    else:
        d, run, src = _depot_module_verse(tmp_path_factory, tmp_path)
    if cas.startswith("contrôle"):
        (d / "prereg").mkdir(exist_ok=True)
        (d / tg.PREREG).write_text("Texte synthétique, non scellé, sans ligne du module.\n", encoding="utf-8")
    module = d / ip.DOSSIER_MODULE
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONDONTWRITEBYTECODE", "PYTHONPYCACHEPREFIX")}
    env["PYTHONPATH"] = str(src)
    if cas.startswith("contrôle"):
        args = [str(module / "instrument_p4_v1.py"), "--controle", "module", "--prereg", tg.PREREG]
    else:
        args = [str(module / "lecture_p4_v1.py"), "--run-source", run, "--run-lecture", LECT, "--entropie",
                "4242" if cas.startswith("lecture lue") else str(ENT)]
    r = subprocess.run([sys.executable, *args], cwd=d, env=env, capture_output=True, text=True, timeout=900)
    caches = _caches(d, src)
    if cas.startswith("lecture lue"):
        assert r.returncode == 0, r.stderr[-800:]
    else:
        assert r.returncode == 1 and "ARRÊT" in r.stderr and "Traceback" not in r.stderr, r.stderr[-800:]
    assert caches == [], caches[:5]
    consigner(f"F sans -B ni PYTHONDONTWRITEBYTECODE : {cas}", f"code {r.returncode} ; aucun __pycache__ ni .pyc sous le "
              "dépôt jetable ni sous le code copié")


def test_f04_mesures_conception_sans_option_b_cr3_05(tmp_path_factory, tmp_path):
    """CR3-05 (hors des décisions) : `mesures_conception_p4_v1.py` lancé sans -B (sans argument : erreur d'usage), avec
    PYTHONPYCACHEPREFIX vers le dossier temporaire : le cache d'instrument_p4_v1 est-il écrit (décision d'écrire) ?"""
    d, run, src = _depot_module_verse(tmp_path_factory, tmp_path)
    module = d / ip.DOSSIER_MODULE
    prefixe = tmp_path / "prefixe"
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONDONTWRITEBYTECODE", "PYTHONPYCACHEPREFIX")}
    env.update(PYTHONPATH=str(src), PYTHONPYCACHEPREFIX=str(prefixe))
    r = subprocess.run([sys.executable, str(module / "mesures_conception_p4_v1.py"), "--aide-inexistante"], cwd=d,
                       env=env, capture_output=True, text=True, timeout=900)
    ecrits = [str(x.relative_to(prefixe)) for x in prefixe.rglob("*.pyc")] if prefixe.exists() else []
    vise = [x for x in ecrits if "instrument_p4_v1" in x]
    consigner("F04 mesures_conception_p4_v1.py sans -B (préfixe de cache vers le dossier temporaire)",
              f"code {r.returncode} ; caches décidés : {len(ecrits)} ; dont instrument_p4_v1 : {vise[:1]}")
    assert _caches(d, src) == []


# ------------------------------------------------------------------------------------------------ G. -07

def test_g_lire_sources_fabriquees(tmp_path_factory):
    from controle_ia.manifeste import graines
    d, run = ti.depot_p4(tmp_path_factory)
    g = graines(lp.CLES_LECTURE, 4242)
    src = lp.charger_source_p4(d, run)
    vus = {}
    for nom, autre in (("sans clé manifeste", {k: v for k, v in src.items() if k != "manifeste"}),
                       ("manifeste None", dict(src, manifeste=None)), ("manifeste liste", dict(src, manifeste=[1])),
                       ("manifeste {} (dictionnaire vide)", dict(src, manifeste={})),
                       ("manifeste fabriqué non décisif", dict(src, manifeste={"decisif": False, "config": {"mode": "jouet"}}))):
        try:
            s = lp.lire(autre, g)
            vus[nom] = f"lu (issue {s['issue']['ligne']})"
        except GardeArret as e:
            vus[nom] = f"refus ({str(e)[:60]})"
    assert vus["sans clé manifeste"].startswith("refus") and vus["manifeste None"].startswith("refus")
    assert vus["manifeste liste"].startswith("refus")
    consigner("G lire sur sources fabriquées à la main (appels Python)", json.dumps(vus, ensure_ascii=False))
