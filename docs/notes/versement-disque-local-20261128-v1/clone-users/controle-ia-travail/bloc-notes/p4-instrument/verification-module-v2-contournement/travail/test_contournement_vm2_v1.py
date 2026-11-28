"""Vérification adverse « contournement » du module v2 de P4-instrument (VM2-contournement) — modèle jouet seulement.

But : lire un run décisif (ou réel) du modèle jouet SANS verdict complété de P3 versé, ou obtenir une lecture décisive
avec une table `LIGNES` différente du texte, avec le module v2. Chaque voie écrit une ligne « VOIE … » (fichier nommé
par VOIES_SORTIE, et sortie standard). Les affirmations (assert) décrivent le comportement CONSTATÉ, pas le comportement
voulu : un test qui passe ici documente une voie, il ne la juge pas.

Lancement (depuis n'importe où ; rien n'est écrit dans le dépôt de travail ni dans module-v2) :
    VOIES_SORTIE=<fichier> PYTHONPATH=<dépôt>/src:<module-v2> PYTHONDONTWRITEBYTECODE=1 <python> -B -m pytest -q -s
        -p no:cacheprovider --import-mode=append --basetemp=<dossier neuf> test_contournement_vm2_v1.py
"""
import sys

sys.dont_write_bytecode = True

import json  # noqa: E402
import os  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
import hashlib  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import pytest  # noqa: E402

import instrument_p4_v1 as ip  # noqa: E402
import lecture_p4_v1 as lp  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.manifeste import config_canonique, graines, lire_manifeste, verifier_resultat  # noqa: E402
from controle_ia.prereg import problemes  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402
from test_instrument_p4_v1 import ENTROPIE_JOUET, copie  # noqa: E402
from test_gardes_p4_v1 import (PREREG, RACINE_REELLE, RUN_DECISIF, _depot_de_lecture, code_sous_la_racine,  # noqa: E402,F401
                               committer, ecrire_prereg, git, run_decisif_jouet, table_markdown, texte_prereg)
from test_lecture_p4_v1 import table_recodee  # noqa: E402

MODULE_V2 = Path(lp.__file__).resolve().parent
EMPREINTES_V2 = {"lecture_p4_v1.py": "3e41ec106589f9cd6907543ebf4b6e83ed74637f1e40e69ec9c65a15c5b38579",
                 "instrument_p4_v1.py": "c3e78becc07a1e265490c96842ae810dbee72a0a52c3d0cab195fede851621fc"}
RUN_X = "20261020-170000-p4-jouet"          # run jouet NON décisif, même configuration que le run décisif
SORTIE = os.environ.get("VOIES_SORTIE")
_BASE: dict = {}


def note(voie: str, texte: str) -> None:
    ligne = f"VOIE {voie} | {texte}"
    print("\n" + ligne)
    if SORTIE:
        with open(SORTIE, "a", encoding="utf-8") as f:
            f.write(ligne + "\n")


def instantane(d: Path) -> set:
    return {str(p.relative_to(d)) for p in d.rglob("*") if ".git" not in p.relative_to(d).parts}


def cli(d: Path, *args) -> subprocess.CompletedProcess:
    env = dict(os.environ, PYTHONPATH=str(RACINE_REELLE / "src"), PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run([sys.executable, "-B", str(MODULE_V2 / "lecture_p4_v1.py"), *args], cwd=d, env=env,
                          capture_output=True, text=True, timeout=900)


def derniere(r: subprocess.CompletedProcess) -> str:
    x = (r.stderr.strip().splitlines() or [""])[-1] if r.returncode else (r.stdout.strip().splitlines() or [""])[-1]
    return x[:220]


def base(tmp_path_factory, monkeypatch) -> Path:
    """Dépôt jouet : run décisif jouet (sans verdict complété de P3) et run jouet NON décisif X, même configuration."""
    if "d" not in _BASE:
        for nom, sha in EMPREINTES_V2.items():
            assert hashlib.sha256((MODULE_V2 / nom).read_bytes()).hexdigest() == sha, nom
        d = run_decisif_jouet(tmp_path_factory, tmp_path_factory.mktemp("base") / "d", monkeypatch)
        m, _ = lire_manifeste(d / "runs" / RUN_DECISIF / "manifeste.json")
        r = ip.executer(m["config"], d, RUN_X, None, entropie=ENTROPIE_JOUET, autoriser_depot_sale=True)
        assert r["arret"] is None
        mx, _ = lire_manifeste(d / "runs" / RUN_X / "manifeste.json")
        assert mx["decisif"] is False and mx["config"] == m["config"] and m["decisif"] is True
        committer(d, "run jouet non décisif X")
        assert not (d / lp.CHEMIN_VERDICT_P3).exists()
        _BASE["d"] = d
    return _BASE["d"]


def depot(tmp_path_factory, tmp_path, monkeypatch) -> Path:
    return copie(base(tmp_path_factory, monkeypatch), tmp_path / "d")


def resultat_ecrit(d: Path, run_lecture: str):
    p = d / "diag" / run_lecture / "lecture-p4.json"
    if not p.exists():
        return None
    return verifier_resultat(d, p)["resultat"]


def resume_c1(corps) -> str:
    if corps is None:
        return "aucune lecture écrite"
    c1 = corps.get("C1")
    return (f"source {corps['source']['etat']} ; issue {corps['issue']['ligne']} ; C1 calculé : {lp.calcule(c1)}"
            + (f" (aire {c1['aire']:.4f})" if lp.calcule(c1) else ""))


def resceller(chemin: Path, m) -> None:
    c = chemin.with_name(chemin.name + ".sha256")
    if c.exists():
        c.unlink()
    chemin.write_text(json.dumps(m, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(chemin)


# ------------------------------------------------------------------------------------------------ V01 témoin

def test_v01_cli_sans_prereg_temoin(tmp_path_factory, tmp_path, monkeypatch, code_sous_la_racine):
    d = depot(tmp_path_factory, tmp_path, monkeypatch)
    avant = instantane(d)
    r = cli(d, "--run-source", RUN_DECISIF, "--run-lecture", "20261020-200000-lecture-p4", "--entropie",
            str(ENTROPIE_JOUET))
    ecrit = sorted(instantane(d) - avant)
    note("V01", f"CLI sans --prereg, run décisif jouet, pas de verdict : code {r.returncode} ; {derniere(r)} ; "
                f"écrit : {ecrit} ; git : {git(d, 'status', '--porcelain', '--untracked-files=all')!r}")
    assert r.returncode == 1 and lp.MOTIF_SANS_PREREG in r.stderr and not ecrit


# ------------------------------------------------------------------------------------------------ V02 --prereg

VARIANTES_PREREG = ["vide", "texte du run", "chemin absolu du texte", "dossier", "/dev/null", "configuration scellée",
                    "copie non scellée", "autre texte scellé, table égale", "autre texte scellé, table autre",
                    "texte jouet scellé sans section de critères", "chemin hors du dépôt"]


@pytest.mark.parametrize("variante", VARIANTES_PREREG)
def test_v02_cli_avec_prereg_sans_verdict(tmp_path_factory, tmp_path, monkeypatch, code_sous_la_racine, variante):
    d = depot(tmp_path_factory, tmp_path, monkeypatch)
    arg = {"vide": "", "texte du run": PREREG, "chemin absolu du texte": str(d / PREREG), "dossier": "prereg",
           "/dev/null": "/dev/null", "configuration scellée": "prereg/P4-instrument-config-v1.json"}.get(variante)
    if variante == "copie non scellée":
        arg = "prereg/copie-non-scellee.md"
        (d / arg).write_text((d / PREREG).read_text(encoding="utf-8"), encoding="utf-8")
    elif variante.startswith("autre texte scellé"):
        arg = "prereg/autre-v1.md"
        t = (d / PREREG).read_text(encoding="utf-8")
        if variante.endswith("table autre"):
            t = t.replace("\n".join(table_markdown()), "\n".join(table_markdown(dict(lp.LIGNES, L6=("x", "y")))))
        (d / arg).write_text(t + "\n<!-- autre texte -->\n", encoding="utf-8")
        sceller(d / arg)
    elif variante == "texte jouet scellé sans section de critères":
        arg = "prereg/jouet-v1.md"
        t = (d / PREREG).read_text(encoding="utf-8").replace(f"## {lp.TITRE_CRITERES}", "## Critères de lecture")
        (d / arg).write_text(t, encoding="utf-8")
        sceller(d / arg)
    elif variante == "chemin hors du dépôt":
        hors = tmp_path / "hors" / "P4.md"
        hors.parent.mkdir()
        shutil.copyfile(d / PREREG, hors)
        sceller(hors)
        arg = str(hors)
    committer(d, f"variante {variante}") if git(d, "status", "--porcelain") else None
    avant = instantane(d)
    r = cli(d, "--run-source", RUN_DECISIF, "--run-lecture", "20261020-201000-lecture-p4", "--prereg", arg,
            "--entropie", str(ENTROPIE_JOUET))
    ecrit = sorted(instantane(d) - avant)
    note("V02", f"--prereg {variante} ({arg!r}) : code {r.returncode} ; {derniere(r)} ; écrit : {ecrit}")
    assert r.returncode == 1 and not ecrit


# ------------------------------------------------------------------------------------------------ V03 --run-source

@pytest.mark.parametrize("forme", ["barre finale", "point", "détour", "absolu"])
def test_v03_cli_formes_du_run_source(tmp_path_factory, tmp_path, monkeypatch, code_sous_la_racine, forme):
    d = depot(tmp_path_factory, tmp_path, monkeypatch)
    arg = {"barre finale": RUN_DECISIF + "/", "point": "./" + RUN_DECISIF, "détour": "x/../" + RUN_DECISIF,
           "absolu": str((d / "runs" / RUN_DECISIF).resolve())}[forme]
    avant = instantane(d)
    r = cli(d, "--run-source", arg, "--run-lecture", "20261020-202000-lecture-p4")
    ecrit = sorted(instantane(d) - avant)
    note("V03", f"--run-source {forme} : code {r.returncode} ; {derniere(r)} ; écrit : {ecrit}")
    assert r.returncode == 1 and not ecrit


# ------------------------------------------------------------------------------------------------ V04 manifeste altéré

ALTERATIONS = ["decisif retiré, sceau rompu", "decisif retiré, rescellé", "decisif à false, rescellé",
               "clé renommée (Decisif), rescellé", "decisif à 1, sceau rompu", "manifeste du run X recopié avec son sceau",
               "manifeste et sceau supprimés", "JSON tronqué", "config non dictionnaire, rescellé"]


@pytest.mark.parametrize("alteration", ALTERATIONS)
def test_v04_cli_manifeste_altere(tmp_path_factory, tmp_path, monkeypatch, code_sous_la_racine, alteration):
    d = depot(tmp_path_factory, tmp_path, monkeypatch)
    ch = d / "runs" / RUN_DECISIF / "manifeste.json"
    m = json.loads(ch.read_text(encoding="utf-8"))
    if alteration == "decisif retiré, sceau rompu":
        del m["decisif"]
        ch.write_text(json.dumps(m, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    elif alteration == "decisif retiré, rescellé":
        del m["decisif"]
        resceller(ch, m)
    elif alteration == "decisif à false, rescellé":
        m["decisif"] = False
        resceller(ch, m)
    elif alteration.startswith("clé renommée"):
        m["Decisif"] = m.pop("decisif")
        resceller(ch, m)
    elif alteration == "decisif à 1, sceau rompu":
        m["decisif"] = 1
        ch.write_text(json.dumps(m, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    elif alteration.startswith("manifeste du run X"):
        for s in ("", ".sha256"):
            shutil.copyfile(d / "runs" / RUN_X / ("manifeste.json" + s), d / "runs" / RUN_DECISIF / ("manifeste.json" + s))
    elif alteration == "manifeste et sceau supprimés":
        ch.unlink()
        ch.with_name("manifeste.json.sha256").unlink()
    elif alteration == "JSON tronqué":
        ch.write_text(ch.read_text(encoding="utf-8")[:200], encoding="utf-8")
    elif alteration.startswith("config non dictionnaire"):
        del m["decisif"]
        m["config"] = ["x"]
        m["config_sha256"] = hashlib.sha256(config_canonique(m["config"])).hexdigest()
        resceller(ch, m)
    committer(d, f"manifeste : {alteration}")
    avant = instantane(d)
    r = cli(d, "--run-source", RUN_DECISIF, "--run-lecture", "20261020-203000-lecture-p4")
    ecrit = sorted(instantane(d) - avant)
    corps = resultat_ecrit(d, "20261020-203000-lecture-p4")
    note("V04", f"{alteration} : code {r.returncode} ; {derniere(r)} ; écrit : {ecrit} ; {resume_c1(corps)}"
                + (f" ; motif : {corps['source']['motif'][:120]}" if corps else ""))
    assert corps is None or not lp.calcule(corps.get("C1"))          # aucune donnée du run n'est lue


# ------------------------------------------------------------------------------------------------ V05 copie du diag

@pytest.mark.parametrize("forme", ["copie des fichiers scellés", "lien symbolique du dossier"])
def test_v05_cli_donnees_du_run_decisif_sous_le_manifeste_d_un_autre_run(tmp_path_factory, tmp_path, monkeypatch,
                                                                         code_sous_la_racine, forme):
    """Run Y = manifeste du run jouet NON décisif X recopié avec son sceau (rien n'est rescellé) ; diag/Y = résumé et
    identité du run DÉCISIF (copies scellées, ou lien symbolique). Lecture sans --prereg, par la ligne de commande."""
    d = depot(tmp_path_factory, tmp_path, monkeypatch)
    y = "20261020-171500-p4-copie"
    (d / "runs" / y).mkdir()
    for s in ("", ".sha256"):
        shutil.copyfile(d / "runs" / RUN_X / ("manifeste.json" + s), d / "runs" / y / ("manifeste.json" + s))
    if forme == "copie des fichiers scellés":
        (d / "diag" / y).mkdir()
        for nom in ("resume.json", "identite-p4.json"):
            for s in ("", ".sha256"):
                shutil.copyfile(d / "diag" / RUN_DECISIF / (nom + s), d / "diag" / y / (nom + s))
    else:
        (d / "diag" / y).symlink_to(RUN_DECISIF)
    committer(d, "run Y")
    assert not (d / lp.CHEMIN_VERDICT_P3).exists()
    r_decisif = cli(d, "--run-source", RUN_DECISIF, "--run-lecture", "20261020-204000-lecture-p4")
    assert r_decisif.returncode == 1 and lp.MOTIF_SANS_PREREG in r_decisif.stderr
    avant = instantane(d)
    r = cli(d, "--run-source", y, "--run-lecture", "20261020-204500-lecture-p4")
    ecrit = sorted(instantane(d) - avant)
    corps = resultat_ecrit(d, "20261020-204500-lecture-p4")
    rz = verifier_resultat(d, d / "diag" / RUN_DECISIF / "resume.json")
    ml, _ = lire_manifeste(d / "runs" / "20261020-204500-lecture-p4" / "manifeste.json") if corps else (None, None)
    note("V05", f"{forme} : même run décisif lu directement : code {r_decisif.returncode} (refus) ; par Y : code "
                f"{r.returncode} ; {resume_c1(corps)} ; scores lus = ceux du run décisif : "
                f"{bool(corps) and corps['resume_source']['scores_sha256'] == rz['resultat']['scores_sha256']} ; "
                f"résumé rattaché au run {rz['run_id']} ; manifeste de lecture décisif : {ml and ml['decisif']} ; "
                f"verdict complété présent : {(d / lp.CHEMIN_VERDICT_P3).exists()} ; écrit : {ecrit}")
    assert r.returncode == 0 and corps["source"]["etat"] == "complet" and lp.calcule(corps["C1"])
    assert corps["resume_source"]["scores_sha256"] == rz["resultat"]["scores_sha256"]


# ------------------------------------------------------------------------------------------------ V06 appels Python directs

def test_v06_appels_python_directs(tmp_path_factory, tmp_path, monkeypatch, code_sous_la_racine):
    d = depot(tmp_path_factory, tmp_path, monkeypatch)
    g = graines(lp.CLES_LECTURE, 4242)
    avant = instantane(d)
    # (a) source construite à la main, sans clé « manifeste » : `lire` ne regarde rien
    dz = d / "diag" / RUN_DECISIF
    resume = verifier_resultat(d, dz / "resume.json")["resultat"]
    identite = verifier_resultat(d, dz / "identite-p4.json")["resultat"]
    tables = {}
    for cle in ("scores", "jetons_principales", "validation"):
        with np.load(d / resume[cle], allow_pickle=False) as z:
            tables[cle] = {k: z[k] for k in z.files}
    m, _ = lire_manifeste(d / "runs" / RUN_DECISIF / "manifeste.json")
    s_a = lp.lire({"etat": "complet", "resume": resume, "identite": identite, "tables": tables, "config": m["config"]}, g)
    # (b) lien fabriqué de la forme écrite par `analyser`
    src = lp.charger_source_p4(d, RUN_DECISIF, {"run_source_verifie": True, "verdict_p3": {}, "table_des_criteres": {}})
    s_b = lp.lire(src, g)
    # (c) source chargée par (b), clés « manifeste » et « lien » retirées
    s_c = lp.lire({k: v for k, v in src.items() if k not in ("manifeste", "lien")}, g)
    # (d) charger_source_p4 sans lien : refus (témoin)
    with pytest.raises(GardeArret, match="sans préenregistrement"):
        lp.charger_source_p4(d, RUN_DECISIF)
    ecrit = sorted(instantane(d) - avant)
    note("V06", f"(a) lire(source sans manifeste) : C1 calculé {lp.calcule(s_a['C1'])} ; (b) lien fabriqué : C1 "
                f"calculé {lp.calcule(s_b['C1'])} ; (c) clés retirées : C1 calculé {lp.calcule(s_c['C1'])} ; (d) sans lien : "
                f"refus ; rien d'écrit : {not ecrit}")
    assert lp.calcule(s_a["C1"]) and lp.calcule(s_b["C1"]) and lp.calcule(s_c["C1"]) and not ecrit


# ------------------------------------------------------------------------------------------------ V07 table des critères

LIGNES_CACHEES = {
    "rangée sans barre initiale (GFM)": "L12 | C1 au-dessus | « témoin positif passé » |",
    "identifiant en gras": "| **L12** | C1 au-dessus | « témoin positif passé » |",
    "identifiant à suffixe": "| L6bis | C1 au-dessus ; M6 non lu | « témoin positif passé » |",
    "identifiant à espace": "| L 12 | C1 au-dessus | « témoin positif passé » |",
    "identifiant en minuscule": "| l12 | C1 au-dessus | « témoin positif passé » |",
}


@pytest.mark.parametrize("forme", list(LIGNES_CACHEES))
def test_v07a_ligne_en_plus_ignoree_par_la_garde(forme):
    texte = texte_prereg({}, table=table_markdown() + [LIGNES_CACHEES[forme]])
    try:
        g = lp.exiger_table_des_criteres(texte)
    except GardeArret as e:
        g = f"refus : {e}"
    try:
        t = table_recodee(texte)
        test = "passe" if list(t) == list(lp.LIGNES) and all(t[k] == lp.LIGNES[k] for k in t) else f"échoue ({list(t)[-2:]})"
    except AssertionError as e:
        test = f"échoue ({str(e)[:60]})"
    note("V07a", f"table du texte + « {LIGNES_CACHEES[forme][:40]}… » ({forme}) : garde : {g} ; test P4_TEXTE_PREREG : {test} "
                 f"; validateur : {problemes_texte(texte)}")


def problemes_texte(texte: str):
    import tempfile
    with tempfile.TemporaryDirectory(dir=os.environ.get("TMP_VM2")) as t:
        p = Path(t) / "p.md"
        p.write_text(texte, encoding="utf-8")
        return problemes(p)


@pytest.mark.parametrize("ordre", ["autre puis égale", "égale puis autre"])
def test_v07b_section_des_criteres_en_double(ordre):
    autre = "\n".join(table_markdown(dict(lp.LIGNES, L6=(lp.LIGNES["L6"][0], "« témoin positif passé » (autre lecture)"))))
    egale = "\n".join(table_markdown())
    premiere, seconde = (autre, egale) if ordre == "autre puis égale" else (egale, autre)
    texte = texte_prereg({}, table=premiere.split("\n")) + f"\n## {lp.TITRE_CRITERES}\n\n{seconde}\n"
    try:
        g = lp.exiger_table_des_criteres(texte)
    except GardeArret as e:
        g = f"refus : {str(e)[:90]}"
    t = table_recodee(texte)
    note("V07b", f"deux sections « {lp.TITRE_CRITERES} » ({ordre}) : garde (lit la dernière) : {g} ; test P4_TEXTE_PREREG "
                 f"(lit la première) : L6 égale : {t['L6'] == lp.LIGNES['L6']} ; validateur : {problemes_texte(texte)}")


def test_v07c_lecture_decisive_avec_rangee_cachee(tmp_path):
    """Dépôt synthétique avec verdict complété : texte scellé dont la table a une douzième rangée sans barre initiale.
    La lecture décisive passe la garde de table et écrit son lien « 22 cellules égales »."""
    d = _depot_de_lecture(tmp_path)
    texte = (d / PREREG).read_text(encoding="utf-8")
    sain = "\n".join(table_markdown())
    ecrire_prereg(d, texte.replace(sain, sain + "\n" + LIGNES_CACHEES["rangée sans barre initiale (GFM)"]))
    committer(d, "texte à douze rangées")
    s = lp.analyser(d, "20261101-120000-p4-reel", "20261101-150000-lecture-p4", PREREG, entropie=ip.ENTROPIE_P4,
                    autoriser_depot_sale=True)
    m, _ = lire_manifeste(d / "runs" / "20261101-150000-lecture-p4" / "manifeste.json")
    note("V07c", f"lecture décisive, texte scellé à 12 rangées (dont une sans barre initiale) : manifeste décisif "
                 f"{m['decisif']} ; lien table : {s['lien_au_preenregistrement']['table_des_criteres']} ; issue "
                 f"{s['issue']['ligne']} (run source absent du dépôt synthétique)")
    assert m["decisif"] is True and s["lien_au_preenregistrement"]["table_des_criteres"]["cellules_egales"] == 22


# ------------------------------------------------------------------------------------------------ V08 dossier de sortie

@pytest.mark.parametrize("cas", ["lecture = run source (non décisif)", "lecture = run décisif existant",
                                 "lecture-p4.json déjà là, runs/<lecture> absent", "identifiant hors forme",
                                 "run décisif, dossier de lecture existant"])
def test_v08_dossier_de_sortie(tmp_path_factory, tmp_path, monkeypatch, code_sous_la_racine, cas):
    d = depot(tmp_path_factory, tmp_path, monkeypatch)
    source, lecture = RUN_X, {"lecture = run source (non décisif)": RUN_X, "lecture = run décisif existant": RUN_DECISIF,
                              "identifiant hors forme": "../evil"}.get(cas, "20261020-205000-lecture-p4")
    if cas.startswith("lecture-p4.json déjà là"):
        (d / "diag" / lecture).mkdir()
        (d / "diag" / lecture / "lecture-p4.json").write_text("{}\n", encoding="utf-8")
        sceller(d / "diag" / lecture / "lecture-p4.json")
        committer(d, "sortie préexistante")
    elif cas == "run décisif, dossier de lecture existant":
        source, lecture = RUN_DECISIF, RUN_X
    avant = instantane(d)
    r = cli(d, "--run-source", source, "--run-lecture", lecture)
    ecrit = sorted(instantane(d) - avant)
    note("V08", f"{cas} : code {r.returncode} ; {derniere(r)} ; écrit : {ecrit}")
    assert r.returncode == 1
