"""Tests des gardes du mode décisif, du GO et de l'accord de P4-instrument (v1). Texte : brouillon 4 (`32d821fb…`).

Nombre de tests attendu : 81

Lancement (depuis la racine du dépôt, par chemin explicite) :
    PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider docs/procedures/P4-instrument-v1/test_gardes_p4_v1.py

Données : dépôts jetables (préenregistrement, configuration, verdict et registres synthétiques ; copies des six fichiers
du module) et le run jouet de P3 de `test_instrument_p4_v1.py` (modèle jouet). Le dépôt réel n'est que lu : ses
registres des GO et des décisions (contrôle du GO cité, garde de calcul gelée rejouée), sans rien écrire.

Gardes (R5 : cas sain et artefact) :
- `exiger_module_cite` : six lignes « Module de P4 : `chemin` : `empreinte` » ; ligne absente, empreinte fausse, ligne
  en trop, ligne en double, forme non exacte (l'empreinte « au candidat » du brouillon), fichier absent ; la prose qui
  nomme la forme est ignorée ; `exiger_module_execute` : fichier exécuté au contenu cité, ou non ;
- verdict complété de P3 : sain ; absent, non scellé, altéré après scellement, sans ligne du registre, ligne qui cite le
  chemin sans la forme exacte « **Verdict complété de P3 scellé** » (ou pas en tête de la cellule), empreinte différente
  du sceau ; un refus est un report : la lecture n'écrit rien ;
- autres gardes du mode décisif de la lecture (entropie, module, run source non décisif ou hors du mode réel, autre
  préenregistrement, configuration) : sain, puis chaque refus, écrit en ligne L1 avec son motif ;
- mode décisif du run : citations (configuration, entropie, révision) avant le manifeste ; code importé, commit cité,
  instrument figé (arbre gelé égal à celui de P3), module cité et exécuté après le manifeste, avec résumé ; run décisif
  jouet sain de bout en bout, puis sa lecture décisive refusée (run source hors du mode réel, L1) ;
- GO : GO-2026-10-20-07 seul ; type, accordé par Lazar, huit colonnes ; plafond qui commence par « 10 USD par
  lancement » ; échéance de sa colonne ; borne de l'étape inférieure à 10 USD ; révocations (ligne de type
  « révocation » qui nomme GO-2026-10-04-08, GO-2026-10-20-06, GO-2026-10-20-07, R-262 ou R-269 ; ligne R-… qui commence
  par « **Révocation de R-262** » ou « **Révocation de R-269** ») ; registres réels du dépôt au 2026-10-20 ;
- accord du jour : préfixe exact, jour, délégation ou message de Lazar, GO échu ;
- garde de calcul gelée rejouée : sain ; registre mal formé, GO échu, d'un autre type, révoqué ; garde absente ;
- lignes de commande `--controle module` et `--controle go`.
"""
import sys

sys.dont_write_bytecode = True          # rien n'est écrit à côté des sources

import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
from pathlib import Path  # noqa: E402

import pytest  # noqa: E402

ICI = Path(__file__).resolve().parent
if str(ICI) not in sys.path:
    sys.path.insert(0, str(ICI))

import instrument_p4_v1 as ip  # noqa: E402
import lecture_p4_v1 as lp  # noqa: E402
from test_instrument_p4_v1 import (ENTROPIE_JOUET, _signal_term_efface, committer, config_p4_jouet, copie,  # noqa: E402,F401
                                   depot_neuf, depot_p3, git, resume_de)

import controle_ia  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.manifeste import lire_manifeste, verifier_resultat  # noqa: E402
from controle_ia.prereg import SECTIONS  # noqa: E402
from controle_ia.scellement import empreinte, sceller  # noqa: E402

RACINE_REELLE = Path(controle_ia.__file__).resolve().parents[2]
PREREG = "prereg/P4-instrument-v1.md"
JOUR = "2026-10-21"
SHA_A, SHA_B = "a" * 64, "b" * 64


# ------------------------------------------------------------------------------------------------ outillage

def verser_module(racine: Path) -> dict:
    """Copie les six fichiers du module sous `docs/procedures/P4-instrument-v1/` ; rend {chemin: empreinte}."""
    (racine / ip.DOSSIER_MODULE).mkdir(parents=True, exist_ok=True)
    cites = {}
    for nom, chemin in zip(ip.NOMS_MODULE, ip.FICHIERS_MODULE):
        shutil.copyfile(ICI / nom, racine / chemin)
        cites[chemin] = empreinte(racine / chemin)
    return cites


def texte_prereg(cites: dict, config_sha=None, entropie=ip.ENTROPIE_P4, revision=ip.REVISION_P3, commit=None,
                 lignes_module=None) -> str:
    """Préenregistrement synthétique conforme à `prereg.problemes` (sections exigées, contre-lecture à deux empreintes) :
    citations de l'en-tête et lignes « Module de P4 » ; la prose qui nomme la forme est gardée."""
    l = ["# Préenregistrement synthétique (tests des gardes de P4)", ""]
    if commit:
        l.append(f"- Commit du code d'analyse : `{commit}`")
    l += [f"- Entropie : `{entropie}`", f"- Révision du modèle : `{revision}`"]
    if config_sha:
        l.append(f"- Configuration de P4 (empreinte canonique) : `{config_sha}` — chemin `prereg/P4-instrument-config-v1.json`.")
    l.append("- Module de P4, une ligne par fichier, sous `docs/procedures/P4-instrument-v1/` :")
    if lignes_module is None:
        lignes_module = [f"  - Module de P4 : `{c}` : `{s}`" for c, s in cites.items()]
    l += lignes_module
    l += ["", "  Chaque ligne a la forme exacte « Module de P4 : `chemin` : `empreinte` » (empreinte sha256 en 64 signes).",
          ""]
    for s in SECTIONS:
        corps = (f"- **Contre-lecture 1** : brouillon `{SHA_A}` ; rapport `{SHA_B}`." if s == "Contre-lecture"
                 else f"Contenu synthétique de la section « {s} ».")
        l += [f"## {s}", "", corps, ""]
    return "\n".join(l)


def ecrire_prereg(racine: Path, texte: str) -> Path:
    p = racine / PREREG
    p.parent.mkdir(parents=True, exist_ok=True)
    for x in (p, p.with_name(p.name + ".sha256")):
        if x.exists():
            x.unlink()
    p.write_text(texte, encoding="utf-8")
    sceller(p)
    return p


def racine_module(tmp_path) -> tuple[Path, dict]:
    d = tmp_path / "racine"
    d.mkdir()
    return d, verser_module(d)


def ligne_verdict(sha: str, prefixe=lp.PREFIXE_VERDICT, chemin=lp.CHEMIN_VERDICT_P3, ident="R-300") -> str:
    return f"| {ident} | 2026-10-25 | {prefixe} : `{chemin}` (`{sha}`), addendum 2 de P3. | raison |"


def verser_verdict(racine: Path, ligne=None, sceller_verdict=True) -> str:
    """Verdict complété de P3 synthétique, scellé, et registre des décisions qui l'annonce (ou `ligne`)."""
    v = racine / lp.CHEMIN_VERDICT_P3
    v.parent.mkdir(parents=True, exist_ok=True)
    v.write_text("# Verdict complété de P3 (synthétique)\n", encoding="utf-8")
    sha = sceller(v) if sceller_verdict else empreinte(v)
    (racine / "registres").mkdir(exist_ok=True)
    corps = ligne_verdict(sha) if ligne is None else ligne.replace("<SHA>", sha)
    (racine / lp.CHEMIN_DECISIONS).write_text("| id | date (UTC) | décision | raison |\n|---|---|---|---|\n"
                                              f"| R-262 | 2026-10-20 | décision synthétique | raison |\n{corps}\n",
                                              encoding="utf-8")
    return sha


# ------------------------------------------------------------------------------------------------ module cité

def test_module_cite_cas_sain_six_lignes_et_prose_ignoree(tmp_path):
    d, cites = racine_module(tmp_path)
    p = ecrire_prereg(d, texte_prereg(cites))
    assert ip.exiger_module_cite(d, p) == cites and len(cites) == 6
    ip.exiger_module_execute(cites, [ICI / "instrument_p4_v1.py", ICI / "lecture_p4_v1.py"])


@pytest.mark.parametrize("artefact, motif", [
    ("ligne absente", "sans ligne"),
    ("empreinte fausse", "empreinte"),
    ("ligne en trop", "hors du module"),
    ("ligne en double", "en double"),
    ("empreinte au candidat", "mal formée"),
    ("fichier absent", "absent")])
def test_module_cite_artefacts_refuses(tmp_path, artefact, motif):
    d, cites = racine_module(tmp_path)
    lignes = [f"  - Module de P4 : `{c}` : `{s}`" for c, s in cites.items()]
    if artefact == "ligne absente":
        lignes = lignes[1:]
    elif artefact == "empreinte fausse":
        lignes[2] = lignes[2].replace(cites[ip.FICHIERS_MODULE[2]], "0" * 64)
    elif artefact == "ligne en trop":
        (d / ip.DOSSIER_MODULE / "outil_p4_v1.py").write_text("x = 1\n", encoding="utf-8")
        lignes.append(f"  - Module de P4 : `{ip.DOSSIER_MODULE}/outil_p4_v1.py` : "
                      f"`{empreinte(d / ip.DOSSIER_MODULE / 'outil_p4_v1.py')}`")
    elif artefact == "ligne en double":
        lignes.append(lignes[0])
    elif artefact == "empreinte au candidat":
        lignes[0] = f"  - Module de P4 : `{ip.FICHIERS_MODULE[0]}` : `<empreinte au candidat>`"
    elif artefact == "fichier absent":
        (d / ip.FICHIERS_MODULE[4]).unlink()
    p = ecrire_prereg(d, texte_prereg(cites, lignes_module=lignes))
    with pytest.raises(GardeArret, match=motif):
        ip.exiger_module_cite(d, p)


def test_module_execute_au_contenu_cite_ou_refuse(tmp_path):
    d, cites = racine_module(tmp_path)
    ip.exiger_module_execute(cites, [ICI / "lecture_p4_v1.py"])
    autre = tmp_path / "lecture_p4_v1.py"
    autre.write_text((ICI / "lecture_p4_v1.py").read_text(encoding="utf-8") + "\n# modifié\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="contenu cité"):
        ip.exiger_module_execute(cites, [autre])
    with pytest.raises(GardeArret, match="contenu cité"):
        ip.exiger_module_execute(cites, [tmp_path / "inconnu_p4_v1.py"])


# ------------------------------------------------------------------------------------------------ verdict complété de P3

def test_verdict_complete_de_p3_cas_sain(tmp_path):
    sha = verser_verdict(tmp_path)
    r = lp.exiger_verdict_complete_p3(tmp_path)
    assert r == {"chemin": lp.CHEMIN_VERDICT_P3, "sha256": sha, "lignes_du_registre": ["R-300"]}


@pytest.mark.parametrize("artefact, motif", [
    ("absent", "absent"),
    ("non scellé", "non scellé"),
    ("altéré", "non scellé ou altéré"),
    ("sans ligne", "aucune ligne"),
    ("forme non exacte", "aucune ligne"),
    ("préfixe hors de la tête", "aucune ligne"),
    ("autre chemin", "aucune ligne"),
    ("empreinte différente", "empreinte")])
def test_verdict_complete_de_p3_artefacts_lecture_reportee(tmp_path, artefact, motif):
    lignes = {"sans ligne": "| R-300 | 2026-10-25 | autre décision | raison |",
              "forme non exacte": ligne_verdict("<SHA>", prefixe="Verdict complété de P3 scellé"),
              "préfixe hors de la tête": ligne_verdict("<SHA>", prefixe=f"Note : {lp.PREFIXE_VERDICT}"),
              "autre chemin": ligne_verdict("<SHA>", chemin="docs/verdicts/verdict-P3-premier-test-i-a-v1.md"),
              "empreinte différente": ligne_verdict("c" * 64)}
    verser_verdict(tmp_path, ligne=lignes.get(artefact), sceller_verdict=artefact != "non scellé")
    if artefact == "absent":
        (tmp_path / lp.CHEMIN_VERDICT_P3).unlink()
    if artefact == "altéré":
        with open(tmp_path / lp.CHEMIN_VERDICT_P3, "a", encoding="utf-8") as f:
            f.write("ajout\n")
    with pytest.raises(GardeArret, match=motif) as e:
        lp.exiger_verdict_complete_p3(tmp_path)
    assert "reportée" in str(e.value)


def test_deux_lignes_du_verdict_dont_une_d_empreinte_fausse_refusees(tmp_path):
    sha = verser_verdict(tmp_path)
    with open(tmp_path / lp.CHEMIN_DECISIONS, "a", encoding="utf-8") as f:
        f.write(ligne_verdict("d" * 64, ident="R-301") + "\n")
    with pytest.raises(GardeArret, match=r"R-301"):
        lp.exiger_verdict_complete_p3(tmp_path)
    assert sha


# ------------------------------------------------------------------------------------------------ lecture décisive

def _manifeste_source(racine: Path, config: dict, decisif=True, chemin=PREREG):
    return {"decisif": decisif, "config": config,
            "preenregistrement": {"chemin": chemin, "sha256": empreinte(racine / PREREG)}}


def _lecture_decisive(tmp_path):
    d, cites = racine_module(tmp_path)
    config = ip.config_de_reference(ip.CANDIDATES_B[0], ip.CANDIDATES_BPRIME[0])
    ecrire_prereg(d, texte_prereg(cites, config_sha=ip.empreinte_config(config)))
    return d, cites, config


def test_gardes_de_la_lecture_decisive_cas_sain(tmp_path):
    d, cites, config = _lecture_decisive(tmp_path)
    lien = lp.exiger_lecture_sous_prereg_p4(d, PREREG, "20261101-120000-p4-reel", ip.ENTROPIE_P4,
                                            _manifeste_source(d, config))
    assert lien == {"entropie": ip.ENTROPIE_P4, "module_cite": cites, "run_source_verifie": True}
    lien = lp.exiger_lecture_sous_prereg_p4(d, PREREG, "20261101-120000-p4-reel", ip.ENTROPIE_P4, None)
    assert lien["run_source_verifie"] is False                     # run source sans manifeste : la ligne L1 s'écrira


@pytest.mark.parametrize("artefact, motif", [
    ("entropie", "entropie"),
    ("module", "module de P4"),
    ("run source non décisif", "non décisif"),
    ("run source hors du mode réel", "hors du mode réel"),
    ("autre préenregistrement", "autre préenregistrement"),
    ("configuration", "configuration")])
def test_gardes_de_la_lecture_decisive_artefacts(tmp_path, artefact, motif):
    d, cites, config = _lecture_decisive(tmp_path)
    entropie, m = ip.ENTROPIE_P4, _manifeste_source(d, config)
    if artefact == "entropie":
        entropie += 1
    elif artefact == "module":
        with open(d / ip.FICHIERS_MODULE[1], "a", encoding="utf-8") as f:
            f.write("# modifié\n")
    elif artefact == "run source non décisif":
        m["decisif"] = False
    elif artefact == "run source hors du mode réel":
        m["config"] = dict(config, mode="jouet")
    elif artefact == "autre préenregistrement":
        m["preenregistrement"]["chemin"] = "prereg/P3-premier-test-i-a-v1.md"
    elif artefact == "configuration":
        m["config"] = dict(config, n_tirages=1_000)
    with pytest.raises(GardeArret, match=motif):
        lp.exiger_lecture_sous_prereg_p4(d, PREREG, "20261101-120000-p4-reel", entropie, m)


def _depot_de_lecture(tmp_path):
    d, cites, config = _lecture_decisive(tmp_path)
    depot_neuf(d)
    verser_verdict(d)
    committer(d, "candidat synthétique")
    return d


def test_analyser_decisif_refus_d_une_garde_ecrit_l1_avec_son_motif(tmp_path):
    """Entropie autre que l'entropie citée : la lecture est refusée par une garde du mode décisif ; l'issue L1 est
    écrite avec son motif, sous un manifeste décisif, sans autre table."""
    d = _depot_de_lecture(tmp_path)
    s = lp.analyser(d, "20261101-120000-p4-reel", "20261101-130000-lecture-p4", PREREG, entropie=ip.ENTROPIE_P4 + 1,
                    autoriser_depot_sale=True)
    assert s["issue"]["ligne"] == "L1" and "lecture refusée par une garde du mode décisif" in s["issue"]["motif"]
    assert "entropie" in s["issue"]["motif"] and "C1" not in s and "M5" not in s
    corps = verifier_resultat(d, d / "diag" / "20261101-130000-lecture-p4" / "lecture-p4.json")["resultat"]
    assert corps["issue"] == s["issue"] and corps["lien_au_preenregistrement"]["verdict_p3"]["lignes_du_registre"] == ["R-300"]
    m, _ = lire_manifeste(d / "runs" / "20261101-130000-lecture-p4" / "manifeste.json")
    assert m["decisif"] is True and m["preenregistrement"]["chemin"] == PREREG


@pytest.mark.parametrize("artefact", ["préenregistrement non scellé", "verdict absent"])
def test_analyser_decisif_refus_sans_ecriture(tmp_path, artefact):
    """Préenregistrement non scellé : refus ; verdict complété absent : report ; rien n'est écrit (ni manifeste, ni
    sortie)."""
    d = _depot_de_lecture(tmp_path)
    if artefact == "préenregistrement non scellé":
        (d / (PREREG + ".sha256")).unlink()
    else:
        (d / lp.CHEMIN_VERDICT_P3).unlink()
    with pytest.raises(GardeArret, match="sha256|scell|reportée"):
        lp.analyser(d, "20261101-120000-p4-reel", "20261101-130000-lecture-p4", PREREG, entropie=ip.ENTROPIE_P4,
                    autoriser_depot_sale=True)
    assert not (d / "runs" / "20261101-130000-lecture-p4").exists()
    assert not (d / "diag" / "20261101-130000-lecture-p4").exists()


# ------------------------------------------------------------------------------------------------ run décisif

def candidat_jouet(tmp_path_factory, cible: Path, cite_commit="tete", lignes_module=None, config_sha=None,
                   revision=None):
    """Dépôt jouet de P3 avec un candidat décisif : un changement de l'arbre gelé (avant/tête), module versé sous
    `docs/procedures/P4-instrument-v1/`, configuration sous `prereg/`, préenregistrement scellé qui cite le commit, la
    configuration, l'entropie du run jouet de P3, la révision de l'agent jouet et le module ; tout committé."""
    d = copie(depot_p3(tmp_path_factory), cible)
    avant = git(d, "rev-parse", "HEAD").strip()
    (d / "README").write_text("x\ny\n", encoding="utf-8")                 # arbre gelé changé après « avant »
    committer(d, "changement de l'arbre gelé")
    tete = git(d, "rev-parse", "HEAD").strip()
    cites = verser_module(d)
    cfg = config_p4_jouet(d)
    chemin_cfg = d / "prereg" / "P4-instrument-config-v1.json"
    chemin_cfg.parent.mkdir(parents=True, exist_ok=True)
    chemin_cfg.write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller(chemin_cfg)
    ecrire_prereg(d, texte_prereg(cites, config_sha=config_sha or ip.empreinte_config(cfg), entropie=ENTROPIE_JOUET,
                                  revision=revision or cfg["agent"]["revision"],
                                  commit=tete if cite_commit == "tete" else avant, lignes_module=lignes_module))
    committer(d, "candidat jouet")
    return {"depot": d, "config": cfg, "prereg": str(d / PREREG), "avant": avant, "tete": tete, "cites": cites}


@pytest.fixture
def code_sous_la_racine(monkeypatch):
    """Le dépôt jetable n'a pas de `src/` : le code est importé du dépôt réel ; cette garde est neutralisée ici, et
    éprouvée seule dans `test_run_decisif_gardes_apres_le_manifeste_avec_resume`."""
    monkeypatch.setattr(ip, "exiger_code_importe_sous", lambda racine: None)


def test_run_decisif_jouet_de_bout_en_bout_puis_lecture_decisive_refusee(tmp_path_factory, tmp_path, monkeypatch,
                                                                       code_sous_la_racine):
    """Run décisif jouet sain : citations, manifeste décisif, commit cité, instrument figé (commit de P3 pris égal à la
    tête du dépôt jetable), module cité et exécuté ; résumé complet. Puis lecture décisive : verdict complété présent,
    run source hors du mode réel : issue L1 avec son motif."""
    c = candidat_jouet(tmp_path_factory, tmp_path / "d")
    d = c["depot"]
    monkeypatch.setattr(ip, "COMMIT_P3", c["tete"])
    r = ip.executer(c["config"], d, "20261020-180000-p4-decisif", c["prereg"])
    assert r["arret"] is None and r["commit_cite"] == c["tete"] and r["instrument_fige"] == c["tete"]
    assert r["module_cite"] == c["cites"] and r["config_sha256"] == ip.empreinte_config(c["config"])
    m, _ = lire_manifeste(d / "runs" / "20261020-180000-p4-decisif" / "manifeste.json")
    assert m["decisif"] is True and m["preenregistrement"]["chemin"] == PREREG and m["depot_propre"] is True
    verser_verdict(d)
    committer(d, "verdict complété synthétique et run")
    s = lp.analyser(d, "20261020-180000-p4-decisif", "20261020-181000-lecture-p4", PREREG, entropie=ENTROPIE_JOUET)
    assert s["issue"]["ligne"] == "L1" and "hors du mode réel" in s["issue"]["motif"]


@pytest.mark.parametrize("artefact, motif", [
    ("configuration non citée", "configuration"),
    ("entropie autre", "entropie"),
    ("révision autre", "révision")])
def test_run_decisif_citations_refusees_avant_le_manifeste(tmp_path_factory, tmp_path, artefact, motif):
    k = {"configuration non citée": {"config_sha": "e" * 64}, "révision autre": {"revision": "f" * 40}}.get(artefact, {})
    c = candidat_jouet(tmp_path_factory, tmp_path / "d", **k)
    entropie = ENTROPIE_JOUET + 1 if artefact == "entropie autre" else None
    with pytest.raises(GardeArret, match=motif):
        ip.executer(c["config"], c["depot"], "20261020-180100-p4-decisif", c["prereg"], entropie=entropie)
    assert not (c["depot"] / "runs" / "20261020-180100-p4-decisif").exists()


@pytest.mark.parametrize("artefact, etape, motif", [
    ("code importé hors de la racine", "code", "code importé hors"),
    ("commit cité autre", "code", "modifié depuis le commit cité"),
    ("instrument non figé", "code", "instrument non figé"),
    ("module d'empreinte fausse", "module", "empreinte"),
    ("module exécuté autre que cité", "module", "contenu cité")])
def test_run_decisif_gardes_apres_le_manifeste_avec_resume(tmp_path_factory, tmp_path, monkeypatch, artefact, etape,
                                                          motif):
    k = {"commit cité autre": {"cite_commit": "avant"}}.get(artefact, {})
    if artefact == "module d'empreinte fausse":
        k = {"lignes_module": [f"  - Module de P4 : `{x}` : `{'0' * 64 if i == 3 else '<SHA>'}`"
                               for i, x in enumerate(ip.FICHIERS_MODULE)]}
    c = candidat_jouet(tmp_path_factory, tmp_path / "d", **k)
    d = c["depot"]
    if "lignes_module" in k:                                   # empreintes vraies, sauf la quatrième
        texte = (d / PREREG).read_text(encoding="utf-8")
        for x in ip.FICHIERS_MODULE:
            texte = texte.replace(f"`{x}` : `<SHA>`", f"`{x}` : `{c['cites'][x]}`")
        ecrire_prereg(d, texte)
        committer(d, "préenregistrement corrigé")
    if artefact == "module exécuté autre que cité":            # copie versée modifiée et citée : le fichier exécuté diffère
        with open(d / ip.FICHIERS_MODULE[1], "a", encoding="utf-8") as f:
            f.write("# copie modifiée\n")
        texte = (d / PREREG).read_text(encoding="utf-8").replace(c["cites"][ip.FICHIERS_MODULE[1]],
                                                                 empreinte(d / ip.FICHIERS_MODULE[1]))
        ecrire_prereg(d, texte)
        committer(d, "copie modifiée citée")
    if artefact != "code importé hors de la racine":
        monkeypatch.setattr(ip, "exiger_code_importe_sous", lambda racine: None)
    monkeypatch.setattr(ip, "COMMIT_P3", c["avant"] if artefact == "instrument non figé" else c["tete"])
    run = "20261020-180200-p4-decisif"
    with pytest.raises(GardeArret, match=motif):
        ip.executer(c["config"], d, run, c["prereg"])
    r = resume_de(d, run)
    assert r["arret"]["etape"] == etape and re.search(motif, r["arret"]["motif"])
    assert not (d / "donnees" / run).exists()


# ------------------------------------------------------------------------------------------------ GO et accord

GO_SAIN = [
    "| GO-2026-10-04-08 | 2026-10-04 | calcul | devis de calcul de la phase 0 | 150 USD, alerte à 120 USD | 2026-10-31 | "
    "Lazar | devis |",
    "| GO-2026-10-17-01 | 2026-10-17 | calcul | pilote du papier C | 30 USD | 2026-11-30 | Lazar | R-200 |",
    "| GO-2026-10-20-06 | 2026-10-20 | calcul | prolongation de GO-2026-10-04-08 jusqu'au 2026-11-30 | 150 USD | "
    "2026-11-30 | Lazar | message |",
    "| GO-2026-10-20-07 | 2026-10-20 | calcul | extension de la délégation R-217 : lancements préenregistrés, scellés et "
    "contre-lus | 10 USD par lancement, dans les 150 USD de GO-2026-10-04-08 prolongé | 2026-11-30 | Lazar | R-269 |",
]
ENTETE_GO = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
ACCORD = (f"| R-300 | {JOUR} | **Accord de Lazar pour le lancement de P4-instrument** : délégation GO-2026-10-20-07 ; "
          "dépense consignée 40 USD + 5,41 USD < 150 USD | raison |")
ENTETE_DEC = "| id | date (UTC) | décision | raison |\n|---|---|---|---|\n| R-262 | 2026-10-20 | P4 décidée | raison |\n"


def registres(go=None, decisions=None) -> tuple[str, str]:
    return (ENTETE_GO + "\n".join(GO_SAIN if go is None else go) + "\n",
            ENTETE_DEC + "\n".join([ACCORD] if decisions is None else decisions) + "\n")


def remplacer_go07(**cellules) -> list[str]:
    noms = ["id", "accorde", "type", "perimetre", "plafond", "echeance", "par", "ref"]
    c = [x.strip() for x in GO_SAIN[3].strip().strip("|").split("|")]
    for k, v in cellules.items():
        c[noms.index(k)] = v
    return GO_SAIN[:3] + ["| " + " | ".join(c) + " |"]


def test_go_cite_cas_sain():
    go, dec = registres()
    r = ip.controler_go(ip.GO_CITE, go, dec, JOUR, ip.BORNE_ETAPE_USD)
    assert r == {"go": "GO-2026-10-20-07", "echeance": "2026-11-30", "plafond": GO_SAIN[3].split(" | ")[4],
                 "borne_usd": 5.41, "conforme": True}
    assert ip.controler_go(ip.GO_CITE, go, dec, "2026-11-30", 9.99)["conforme"]               # dernier jour ; sous 10


@pytest.mark.parametrize("cas, motif", [
    ("autre GO cité", "seul"),
    ("type autre", "calcul"),
    ("accordé par un autre", "Lazar"),
    ("sept colonnes", "huit colonnes"),
    ("absent", "absent ou en double"),
    ("en double", "absent ou en double"),
    ("plafond autre", "plafond"),
    ("plafond sans le préfixe en tête", "plafond"),
    ("échéance illisible", "échéance"),
    ("GO échu", "échu"),
    ("borne égale à 10", "inférieure à 10"),
    ("borne au-dessus de 10", "inférieure à 10"),
    ("jour mal formé", "jour")])
def test_go_cite_artefacts_aucune_creation(cas, motif):
    go_lignes, jour, borne, cite = GO_SAIN, JOUR, ip.BORNE_ETAPE_USD, ip.GO_CITE
    if cas == "autre GO cité":
        cite = "GO-2026-10-20-06"
    elif cas == "type autre":
        go_lignes = remplacer_go07(type="lecture complémentaire")
    elif cas == "accordé par un autre":
        go_lignes = remplacer_go07(par="session")
    elif cas == "sept colonnes":
        go_lignes = GO_SAIN[:3] + [GO_SAIN[3].replace(" | R-269 |", " |")]
    elif cas == "absent":
        go_lignes = GO_SAIN[:3]
    elif cas == "en double":
        go_lignes = GO_SAIN + [GO_SAIN[3]]
    elif cas == "plafond autre":
        go_lignes = remplacer_go07(plafond="15 USD par lancement")
    elif cas == "plafond sans le préfixe en tête":
        go_lignes = remplacer_go07(plafond="dans les 150 USD, 10 USD par lancement")
    elif cas == "échéance illisible":
        go_lignes = remplacer_go07(echeance="fin novembre")
    elif cas == "GO échu":
        jour = "2026-12-01"
    elif cas == "borne égale à 10":
        borne = 10.0
    elif cas == "borne au-dessus de 10":
        borne = 10.01
    elif cas == "jour mal formé":
        jour = "21/10/2026"
    go, dec = registres(go_lignes)
    with pytest.raises(GardeArret, match=motif):
        ip.controler_go(cite, go, dec, jour, borne)


@pytest.mark.parametrize("nom", ["GO-2026-10-04-08", "GO-2026-10-20-06", "GO-2026-10-20-07", "R-262", "R-269"])
@pytest.mark.parametrize("colonne", ["perimetre", "ref"])
def test_revocation_au_registre_des_go_refusee(nom, colonne):
    perimetre, ref = ("révocation de " + nom, "message de Lazar") if colonne == "perimetre" else ("révocation", nom)
    ligne = f"| GO-2026-10-25-01 | 2026-10-25 | révocation | {perimetre} | — | 2026-10-25 | Lazar | {ref} |"
    go, dec = registres(GO_SAIN + [ligne])
    with pytest.raises(GardeArret, match="révocation"):
        ip.controler_go(ip.GO_CITE, go, dec, JOUR, ip.BORNE_ETAPE_USD)


def test_revocations_hors_du_perimetre_ou_mal_formees():
    """Cas sains : une révocation qui nomme un autre GO (GO-2026-10-17-01) ; une ligne R-… qui mentionne une révocation de
    R-262 sans la forme exacte en tête. Artefacts : ligne de révocation à sept colonnes ; lignes R-… qui commencent par
    « **Révocation de R-262** » ou « **Révocation de R-269** »."""
    autre = "| GO-2026-10-25-01 | 2026-10-25 | révocation | révocation de GO-2026-10-17-01 | — | 2026-10-25 | Lazar | m |"
    mention = "| R-301 | 2026-10-25 | Rappel : aucune révocation de R-262 n'est demandée. | raison |"
    go, dec = registres(GO_SAIN + [autre], [ACCORD, mention])
    assert ip.controler_go(ip.GO_CITE, go, dec, JOUR, ip.BORNE_ETAPE_USD)["conforme"]
    go, dec = registres(GO_SAIN + ["| GO-2026-10-25-01 | 2026-10-25 | révocation | révocation de GO-2026-10-20-07 | — | "
                                   "2026-10-25 | Lazar |"])
    with pytest.raises(GardeArret, match="huit colonnes"):
        ip.controler_go(ip.GO_CITE, go, dec, JOUR, ip.BORNE_ETAPE_USD)
    for r in ("R-262", "R-269"):
        go, dec = registres(None, [ACCORD, f"| R-302 | 2026-10-25 | **Révocation de {r}** : par Lazar. | raison |"])
        with pytest.raises(GardeArret, match="R-302"):
            ip.controler_go(ip.GO_CITE, go, dec, JOUR, ip.BORNE_ETAPE_USD)


def test_registres_reels_du_depot_go_cite_conforme_au_2026_10_20():
    """Registres réels (lus, jamais écrits) : GO-2026-10-20-07 conforme le 2026-10-20 (huit colonnes, plafond « 10 USD par
    lancement », échéance 2026-11-30, aucune révocation) ; échu le 2026-12-01 ; garde gelée rejouée sur le dépôt réel."""
    cache = RACINE_REELLE / ".claude" / "hooks" / "__pycache__"
    avant = sorted((x.name, x.stat().st_mtime_ns) for x in cache.glob("*")) if cache.is_dir() else None
    go = (RACINE_REELLE / "registres" / "go.md").read_text(encoding="utf-8")
    dec = (RACINE_REELLE / "registres" / "decisions.md").read_text(encoding="utf-8")
    r = ip.controler_go(ip.GO_CITE, go, dec, "2026-10-20", ip.borne_de_l_etape())
    assert r["echeance"] == "2026-11-30" and r["plafond"].startswith("10 USD par lancement")
    with pytest.raises(GardeArret, match="échu"):
        ip.controler_go(ip.GO_CITE, go, dec, "2026-12-01", ip.borne_de_l_etape())
    ip.rejouer_garde_de_calcul(RACINE_REELLE, f"GO_ID={ip.GO_CITE} vastai create instance", "2026-10-20")
    with pytest.raises(GardeArret, match="garde de calcul gelée"):
        ip.rejouer_garde_de_calcul(RACINE_REELLE, f"GO_ID={ip.GO_CITE} vastai create instance", "2026-12-01")
    apres = sorted((x.name, x.stat().st_mtime_ns) for x in cache.glob("*")) if cache.is_dir() else None
    assert apres == avant                                       # rien d'écrit dans le dépôt réel


def test_accord_du_jour_cas_sains():
    go, dec = registres()
    r = ip.controler_accord("R-300", go, dec, JOUR)
    assert r["conforme"] and r["cite_delegation"] and not r["cite_message_du_jour"]
    message = ACCORD.replace("délégation GO-2026-10-20-07", "message de Lazar dans la session ce jour-là")
    go, dec = registres(None, [message])
    r = ip.controler_accord("R-300", go, dec, JOUR)
    assert r["conforme"] and r["cite_message_du_jour"] and not r["cite_delegation"]


@pytest.mark.parametrize("cas, motif", [
    ("absent", "absent ou en double"),
    ("autre jour", "ligne du jour"),
    ("préfixe inexact", "ne commence pas"),
    ("préfixe hors de la tête", "ne commence pas"),
    ("ni délégation ni message", "ni GO-2026-10-20-07"),
    ("délégation échue", "échu"),
    ("message, GO échu", "échu"),
    ("identifiant mal formé", "mal formé")])
def test_accord_du_jour_artefacts(cas, motif):
    ident, jour, lignes = "R-300", JOUR, [ACCORD]
    if cas == "absent":
        ident = "R-399"
    elif cas == "autre jour":
        jour = "2026-10-22"
    elif cas == "préfixe inexact":
        lignes = [ACCORD.replace("**Accord de Lazar pour le lancement de P4-instrument**", "**Accord de Lazar pour P4**")]
    elif cas == "préfixe hors de la tête":
        lignes = [ACCORD.replace("**Accord de Lazar", "Note : **Accord de Lazar")]
    elif cas == "ni délégation ni message":
        lignes = [ACCORD.replace("délégation GO-2026-10-20-07", "accord oral")]
    elif cas in ("délégation échue", "message, GO échu"):
        jour = "2026-12-01"
        texte = ACCORD.replace(JOUR, jour)
        lignes = [texte if cas == "délégation échue" else texte.replace("délégation GO-2026-10-20-07",
                                                                        "message de Lazar dans la session")]
    elif cas == "identifiant mal formé":
        ident = "GO-2026-10-20-07"
    go, dec = registres(None, lignes)
    with pytest.raises(GardeArret, match=motif):
        ip.controler_accord(ident, go, dec, jour)


# ------------------------------------------------------------------------------------------------ garde de calcul gelée

def racine_go(tmp_path, go_lignes=None) -> Path:
    d = tmp_path / "racine-go"
    (d / ".claude" / "hooks").mkdir(parents=True)
    shutil.copyfile(RACINE_REELLE / ".claude" / "hooks" / "garde_calcul.py", d / ".claude" / "hooks" / "garde_calcul.py")
    (d / "registres").mkdir()
    go, dec = registres(go_lignes)
    (d / "registres" / "go.md").write_text(go, encoding="utf-8")
    (d / "registres" / "decisions.md").write_text(dec, encoding="utf-8")
    return d


@pytest.mark.parametrize("cas, motif", [
    ("sain", None),
    ("registre mal formé", "8 colonnes"),
    ("GO échu", "hors de sa période"),
    ("autre type", "pas « calcul »"),
    ("révoqué", "révoqué"),
    ("garde absente", "absente")])
def test_garde_de_calcul_gelee_rejouee_jamais_contournee(tmp_path, cas, motif):
    lignes, jour = GO_SAIN, JOUR
    if cas == "registre mal formé":
        lignes = GO_SAIN[:3] + [GO_SAIN[3].replace(" | R-269 |", " |")]
    elif cas == "GO échu":
        jour = "2026-12-01"
    elif cas == "autre type":
        lignes = remplacer_go07(type="décision")
    elif cas == "révoqué":
        lignes = GO_SAIN + ["| GO-2026-10-25-01 | 2026-10-25 | révocation | révocation de GO-2026-10-20-07 | — | "
                            "2026-10-25 | Lazar | m |"]
    d = racine_go(tmp_path, lignes)
    if cas == "garde absente":
        (d / ".claude" / "hooks" / "garde_calcul.py").unlink()
    commande = f"GO_ID={ip.GO_CITE} vastai create instance"
    if motif is None:
        ip.rejouer_garde_de_calcul(d, commande, jour)
    else:
        with pytest.raises(GardeArret, match=motif):
            ip.rejouer_garde_de_calcul(d, commande, jour)
    assert not list(d.rglob("__pycache__"))


# ------------------------------------------------------------------------------------------------ lignes de commande

def _cli(cwd: Path, *args) -> subprocess.CompletedProcess:
    env = dict(os.environ, PYTHONPATH=str(RACINE_REELLE / "src"))
    return subprocess.run([sys.executable, "-B", str(ICI / "instrument_p4_v1.py"), *args], cwd=cwd, env=env,
                          capture_output=True, text=True, timeout=300)


def test_ligne_de_commande_controle_go_sain_et_borne_refusee(tmp_path):
    d = racine_go(tmp_path)
    r = _cli(d, "--controle", "go", "--go", ip.GO_CITE, "--accord", "R-300", "--jour", JOUR)
    assert r.returncode == 0, r.stderr[-1000:]
    assert "GO-2026-10-20-07 (échéance 2026-11-30" in r.stdout and "conformes" in r.stdout
    r = _cli(d, "--controle", "go", "--go", ip.GO_CITE, "--accord", "R-300", "--jour", JOUR, "--borne", "10")
    assert r.returncode == 1 and "ARRÊT" in r.stderr and "inférieure à 10" in r.stderr
    r = _cli(d, "--controle", "go", "--go", ip.GO_CITE, "--accord", "R-300", "--jour", "2026-10-22")
    assert r.returncode == 1 and "ligne du jour" in r.stderr
    assert not list(d.rglob("__pycache__"))


def test_ligne_de_commande_controle_module_sain_et_altere(tmp_path):
    d, cites = racine_module(tmp_path)
    ecrire_prereg(d, texte_prereg(cites))
    r = _cli(d, "--controle", "module", "--prereg", PREREG)
    assert r.returncode == 0 and "6 fichiers à l'empreinte citée" in r.stdout, r.stderr[-1000:]
    with open(d / ip.FICHIERS_MODULE[5], "a", encoding="utf-8") as f:
        f.write("# modifié\n")
    r = _cli(d, "--controle", "module", "--prereg", PREREG)
    assert r.returncode == 1 and "ARRÊT" in r.stderr and "empreinte" in r.stderr


def test_nombre_de_tests_ecrit_en_tete(request):
    """Le nombre de tests écrit en tête égale le nombre de tests de ce fichier (lancé en entier)."""
    if request.config.option.keyword or request.config.option.markexpr or any("::" in a for a in request.config.args):
        pytest.skip("sélection partielle : le compte vaut pour le fichier entier")
    attendu = int(re.search(r"Nombre de tests attendu : (\d+)", __doc__).group(1))
    ici = Path(__file__).resolve()
    items = [i for i in request.session.items if Path(str(getattr(i, "path", None) or i.fspath)).resolve() == ici]
    assert len(items) == attendu
