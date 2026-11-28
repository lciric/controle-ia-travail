"""Tests des gardes du mode décisif, du GO et de l'accord de P4-instrument (v1). Texte : le préenregistrement scellé
(`prereg/P4-instrument-v1.md`).

Nombre de tests attendu : 138

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
  préenregistrement, configuration, configuration non dictionnaire) : sain, puis chaque refus, écrit en ligne L1 avec son
  motif ;
- table « Critères de lecture gelés » du préenregistrement contre `LIGNES` (CL3-03 ; lue en entier depuis le module v3 :
  VM2-contournement-02 et -03, VM2-fidelite-01) : sains (barres de L11 échappées ; paragraphes avant et après la table ;
  espaces de fin et séparateur aligné ; table en fin de section) ; issue de L1 et lecture de L4 du module v1, un signe
  changé, ligne absente, en trop, en double, ordre autre, barre non échappée, section sans table, section absente ;
  rangée hors de la forme « | Lk | » (sans barre initiale, en gras, « L6bis », « L 12 », « l12 », « M1 »), ligne collée
  sous la table, seconde table, en-tête autre, séparateur absent, section en double (trois formes) ; à la lecture
  décisive, refus sans rien écrire ;
- lecture sans préenregistrement (CL3-01) : sain (run jouet non décisif lu) ; run décisif jouet (reprise de la
  démonstration de la contre-lecture 3 : la lecture décisive attend le verdict complété, la lecture sans `--prereg` est
  refusée), run en mode réel, manifeste décisif au sceau rompu : refus, aucun dossier ni fichier de lecture écrit ; même
  refus en ligne de commande ; autres voies (`charger_source_p4`, `lire`) sans le lien des gardes du mode décisif ; règle
  `exiger_lecture_permise` ; voie décisive saine (toutes les gardes passées : le run décisif est lu) ;
- module v3, contournements de la vérification du module v2 : données rattachées à un autre run que celui du manifeste lu
  et du dossier (VM2-contournement-01 : sain ; six formes, copie, lien symbolique, chemin détourné, identité d'un autre
  run : refus sans rien écrire, aussi en ligne de commande ; manifeste du run décisif rescellé : L1 gardée, -08) ;
  configuration du manifeste non dictionnaire (-04 : refus au motif de CL3-01, « ARRÊT », sans trace Python) ;
  `diag/<run de lecture>` déjà présent (-05 : refus R12 avant tout manifeste) ; lancement sans `-B` (-06 : lecture et
  instrument refusés, aucun cache de code écrit ; artefact : ligne `sys.dont_write_bytecode` retirée, le cache
  s'écrit) ; source « complet » sans manifeste (-07 : `lire` refuse) ;
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

import hashlib  # noqa: E402
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
                                   depot_neuf, depot_p3, depot_p4, git, resume_de)

import controle_ia  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.manifeste import (config_canonique, creer_manifeste, ecrire_resultat, graines, lire_manifeste,  # noqa: E402
                                   verifier_resultat)
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


def table_markdown(lignes=None) -> list[str]:
    """Table « Critères de lecture gelés » écrite comme au texte (en-tête, séparateur, une ligne par Lk), « | » des
    cellules échappé en « \\| » ; par défaut, les cellules de `LIGNES`."""
    lignes = lp.LIGNES if lignes is None else lignes
    e = lambda x: x.replace("|", "\\|")  # noqa: E731
    return ["| ligne | issue | lecture |", "|---|---|---|"] + [f"| {k} | {e(i)} | {e(t)} |" for k, (i, t) in lignes.items()]


def texte_prereg(cites: dict, config_sha=None, entropie=ip.ENTROPIE_P4, revision=ip.REVISION_P3, commit=None,
                 lignes_module=None, table=None) -> str:
    """Préenregistrement synthétique conforme à `prereg.problemes` (sections exigées, contre-lecture à deux empreintes) :
    citations de l'en-tête et lignes « Module de P4 » ; la prose qui nomme la forme est gardée ; section « Critères de
    lecture gelés » : la table de `LIGNES` (`table_markdown`), ou les lignes `table`."""
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
                 else "\n".join(table_markdown() if table is None else table) if s == lp.TITRE_CRITERES
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
    ("configuration", "configuration"),
    ("configuration non dictionnaire", "hors du mode réel")])
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
    elif artefact == "configuration non dictionnaire":            # VM2-contournement-04 : refus, pas de trace Python
        m["config"] = ["x"]
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


# ------------------------------------------------------------------------------------------------ table des critères (CL3-03)

ISSUE_L1_V1 = ("run sans résumé (perdu avant d'écrire son résumé), récupération non conforme, ou lecture refusée par une "
               "garde du mode décisif (entropie, module, configuration, données, run source ; motif écrit)")
LECTURE_L4_V1 = "non lu ; nœud"


def test_table_des_criteres_cas_sain():
    """Table écrite comme au texte (barres de L11 échappées), suivie du paragraphe des réserves : lue cellule par cellule,
    égale à `LIGNES` ; la barre échappée est rendue « | »."""
    texte = texte_prereg({}, table=table_markdown() + ["", "Réserves (toujours écrites à part, avec la ligne) : synthétique."])
    t = lp.table_des_criteres(texte)
    assert t == lp.LIGNES and list(t) == [f"L{k}" for k in range(1, 12)] and "|aire − 0,5|" in t["L11"][1]
    assert lp.exiger_table_des_criteres(texte) == {"lignes": list(lp.LIGNES), "cellules_egales": 22}


@pytest.mark.parametrize("artefact, motif", [
    ("issue de L1 du module v1", "cellules : L1 issue"),
    ("lecture de L4 du module v1", "cellules : L4 lecture"),
    ("signe moins devenu tiret dans L11", "cellules : L11 lecture"),
    ("ligne absente", "lignes"),
    ("ligne en trop", "lignes"),
    ("ligne en double", "en double"),
    ("ordre autre", "lignes"),
    ("barre non échappée", "cellules au lieu de 3"),
    ("section sans table", r"lignes \[\]"),
    ("section absente", "sans section"),
    # module v3 : toute la table est lue (VM2-contournement-02 et -03, VM2-fidelite-01)
    ("rangée sans barre initiale", "rangée hors de la forme"),
    ("rangée en gras", "rangée hors de la forme"),
    ("rangée L6bis entre L6 et L7", "rangée hors de la forme"),
    ("rangée « | L 12 | »", "rangée hors de la forme"),
    ("rangée « | l12 | »", "rangée hors de la forme"),
    ("rangée « | M1 | »", "rangée hors de la forme"),
    ("ligne de texte collée sous la table", "rangée hors de la forme"),
    ("seconde table dans la section", "ligne à barre hors du tableau"),
    ("en-tête autre", "en-tête"),
    ("séparateur absent", "séparateur"),
    ("section en double, la première changée", "présente 2 fois"),
    ("section en double, la seconde changée", "présente 2 fois"),
    ("section en double, identiques", "présente 2 fois")])
def test_table_des_criteres_artefacts_refuses(artefact, motif):
    lignes = dict(lp.LIGNES)
    table = None
    ajout = "| ligne ajoutée | non lu ; nœud |"
    if artefact == "issue de L1 du module v1":
        lignes["L1"] = (ISSUE_L1_V1, lignes["L1"][1])
    elif artefact == "lecture de L4 du module v1":
        lignes["L4"] = (lignes["L4"][0], LECTURE_L4_V1)
    elif artefact == "signe moins devenu tiret dans L11":
        lignes["L11"] = (lignes["L11"][0], lignes["L11"][1].replace("−", "-"))
    elif artefact == "ligne absente":
        del lignes["L5"]
    elif artefact == "ligne en trop":
        lignes["L12"] = ("ligne ajoutée", "non lu ; nœud")
    elif artefact == "ordre autre":
        lignes = {k: lignes[k] for k in ["L1", "L2", "L4", "L3"] + [f"L{k}" for k in range(5, 12)]}
    table = table_markdown(lignes)
    if artefact == "ligne en double":
        table.insert(5, table[4])
    elif artefact == "barre non échappée":
        table[-1] = table[-1].replace("\\|", "|")
    elif artefact == "section sans table":
        table = ["Aucune table."]
    elif artefact == "rangée sans barre initiale":
        table.append(f"L12 {ajout}")
    elif artefact == "rangée en gras":
        table.append(f"| **L12** {ajout}")
    elif artefact == "rangée L6bis entre L6 et L7":
        table.insert(table.index(next(x for x in table if x.startswith("| L7 |"))), f"| L6bis {ajout}")
    elif artefact == "rangée « | L 12 | »":
        table.append(f"| L 12 {ajout}")
    elif artefact == "rangée « | l12 | »":
        table.append(f"| l12 {ajout}")
    elif artefact == "rangée « | M1 | »":
        table.append(f"| M1 {ajout}")
    elif artefact == "ligne de texte collée sous la table":
        table.append("Réserves collées sous la table, sans ligne vide.")
    elif artefact == "seconde table dans la section":
        table += ["", "| ligne | issue | lecture |", "|---|---|---|", f"| L12 {ajout}"]
    elif artefact == "en-tête autre":
        table[0] = "| ligne | issue | lecture lue |"
    elif artefact == "séparateur absent":
        del table[1]
    texte = texte_prereg({}, table=table)
    titre = f"## {lp.TITRE_CRITERES}\n"
    autre = "\n".join(table_markdown(dict(lp.LIGNES, L6=("autre issue", "autre lecture"))))
    if artefact == "section absente":
        texte = texte.replace(f"## {lp.TITRE_CRITERES}", "## Critères de lecture")
    elif artefact == "section en double, la première changée":
        assert texte.count(titre) == 1
        texte = texte.replace(titre, f"{titre}\n{autre}\n\n{titre}")
    elif artefact == "section en double, la seconde changée":
        texte += f"\n{titre}\n{autre}\n"
    elif artefact == "section en double, identiques":
        texte += f"\n{titre}\n" + "\n".join(table_markdown()) + "\n"
    with pytest.raises(GardeArret, match=motif) as e:
        lp.exiger_table_des_criteres(texte)
    assert "lecture refusée sans rien écrire" in str(e.value)


PREAMBULE = ("La ligne qui s'applique est toujours calculée et écrite (`issue_p4`). Lignes de haut en bas, la première qui "
             "s'applique :")
RESERVES = "Réserves (toujours écrites à part, avec la ligne) : synthétique."


@pytest.mark.parametrize("forme", ["paragraphes avant et après la table (forme du texte)",
                                   "espaces de fin de ligne et séparateur aligné", "table en fin de section"])
def test_table_des_criteres_cas_sains_formes_du_texte(forme):
    """Cas sains de la table lue en entier (module v3) : la forme du texte (paragraphe, ligne vide, table, ligne vide,
    paragraphe des réserves), des espaces de fin de ligne et un séparateur aligné, ou la table seule en fin de section :
    lue cellule par cellule, égale à `LIGNES`."""
    table = table_markdown()
    if forme.startswith("paragraphes"):
        table = [PREAMBULE, ""] + table + ["", RESERVES]
    elif forme.startswith("espaces"):
        table = [x + "  " for x in table]
        table[1] = "|:---|:---:|---:|"
    texte = texte_prereg({}, table=table)
    assert lp.table_des_criteres(texte) == lp.LIGNES
    assert lp.exiger_table_des_criteres(texte) == {"lignes": list(lp.LIGNES), "cellules_egales": 22}


def test_analyser_decisif_table_des_criteres_autre_refus_sans_rien_ecrire(tmp_path):
    """Cas sain : table du préenregistrement égale à `LIGNES` : la garde passe, son résultat est écrit dans le lien
    (run source absent : L1). Artefact : préenregistrement scellé dont la table garde l'issue de L1 du module v1 : lecture
    décisive refusée avant tout manifeste ; aucun dossier ni fichier de lecture écrit."""
    d = _depot_de_lecture(tmp_path)
    s = lp.analyser(d, "20261101-120000-p4-reel", "20261101-130000-lecture-p4", PREREG, entropie=ip.ENTROPIE_P4,
                    autoriser_depot_sale=True)
    assert s["lien_au_preenregistrement"]["table_des_criteres"] == {"lignes": list(lp.LIGNES), "cellules_egales": 22}
    assert s["issue"]["ligne"] == "L1"
    texte = (d / PREREG).read_text(encoding="utf-8")
    sain = "\n".join(table_markdown())
    assert sain in texte
    autre = dict(lp.LIGNES, L1=(ISSUE_L1_V1, lp.LIGNES["L1"][1]))
    ecrire_prereg(d, texte.replace(sain, "\n".join(table_markdown(autre))))
    committer(d, "préenregistrement à la table autre")
    with pytest.raises(GardeArret, match="cellules : L1 issue"):
        lp.analyser(d, "20261101-120000-p4-reel", "20261101-140000-lecture-p4", PREREG, entropie=ip.ENTROPIE_P4,
                    autoriser_depot_sale=True)
    assert not (d / "runs" / "20261101-140000-lecture-p4").exists()
    assert not (d / "diag" / "20261101-140000-lecture-p4").exists()


@pytest.mark.parametrize("artefact, motif", [("rangée L12 sans barre initiale", "rangée hors de la forme"),
                                             ("section en double, la première changée", "présente 2 fois")])
def test_analyser_decisif_table_hors_forme_ou_section_double_refus_sans_rien_ecrire(tmp_path, artefact, motif):
    """VM2-contournement-02 et -03 (V07c de la vérification) à la lecture décisive, verdict complété versé. Cas sain : la
    table du préenregistrement passe la garde (lien écrit, run source absent : L1). Artefact : préenregistrement scellé
    avec une douzième rangée hors de la forme « | Lk | », ou une section « Critères de lecture gelés » en double dont la
    première est changée : refus avant tout manifeste ; aucun dossier ni fichier de lecture écrit."""
    d = _depot_de_lecture(tmp_path)
    s = lp.analyser(d, "20261101-120000-p4-reel", "20261101-130000-lecture-p4", PREREG, entropie=ip.ENTROPIE_P4,
                    autoriser_depot_sale=True)
    assert s["lien_au_preenregistrement"]["table_des_criteres"] == {"lignes": list(lp.LIGNES), "cellules_egales": 22}
    texte = (d / PREREG).read_text(encoding="utf-8")
    sain, titre = "\n".join(table_markdown()), f"## {lp.TITRE_CRITERES}\n"
    assert texte.count(sain) == 1 and texte.count(titre) == 1
    if artefact.startswith("rangée"):
        texte = texte.replace(sain, f"{sain}\nL12 | ligne ajoutée | non lu ; nœud |")
    else:
        autre = "\n".join(table_markdown(dict(lp.LIGNES, L6=("autre issue", "autre lecture"))))
        texte = texte.replace(titre, f"{titre}\n{autre}\n\n{titre}")
    ecrire_prereg(d, texte)
    committer(d, artefact)
    with pytest.raises(GardeArret, match=motif):
        lp.analyser(d, "20261101-120000-p4-reel", "20261101-140000-lecture-p4", PREREG, entropie=ip.ENTROPIE_P4,
                    autoriser_depot_sale=True)
    assert not (d / "runs" / "20261101-140000-lecture-p4").exists()
    assert not (d / "diag" / "20261101-140000-lecture-p4").exists()


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


# ------------------------------------------------------------------------------------------------ lecture sans préenregistrement (CL3-01)

RUN_DECISIF = "20261020-180000-p4-decisif"
LIEN_SAIN = {"entropie": ENTROPIE_JOUET, "module_cite": {}, "run_source_verifie": True,
             "verdict_p3": {"chemin": lp.CHEMIN_VERDICT_P3, "sha256": SHA_A, "lignes_du_registre": ["R-300"]},
             "table_des_criteres": {"lignes": list(lp.LIGNES), "cellules_egales": 22}}


def run_decisif_jouet(tmp_path_factory, cible: Path, monkeypatch) -> Path:
    """Run décisif jouet de P4 sous un préenregistrement scellé, sans verdict complété de P3 (montage de la démonstration
    de la contre-lecture 3) ; dépôt committé."""
    c = candidat_jouet(tmp_path_factory, cible)
    d = c["depot"]
    monkeypatch.setattr(ip, "COMMIT_P3", c["tete"])
    r = ip.executer(c["config"], d, RUN_DECISIF, c["prereg"])
    assert r["arret"] is None
    m, _ = lire_manifeste(d / "runs" / RUN_DECISIF / "manifeste.json")
    assert m["decisif"] is True and m["config"]["mode"] == "jouet"
    committer(d, "run décisif, sans verdict complété de P3")
    return d


def run_en_mode_reel(tmp_path_factory, cible: Path) -> tuple[Path, str]:
    """Copie du run jouet non décisif dont le manifeste porte `config.mode == "reel"`, cohérent (empreinte de
    configuration recalculée) et rescellé ; aucun modèle réel n'est chargé."""
    d0, run = depot_p4(tmp_path_factory)
    d = copie(d0, cible)
    chemin = d / "runs" / run / "manifeste.json"
    m = json.loads(chemin.read_text(encoding="utf-8"))
    m["config"]["mode"] = "reel"
    m["config_sha256"] = hashlib.sha256(config_canonique(m["config"])).hexdigest()
    chemin.with_name(chemin.name + ".sha256").unlink()
    chemin.write_text(json.dumps(m, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(chemin)
    committer(d, "manifeste en mode réel")
    m2, _ = lire_manifeste(chemin)
    assert m2["config"]["mode"] == "reel" and m2["decisif"] is False
    return d, run


def _rien_d_ecrit(d: Path, run_lecture: str) -> None:
    assert not (d / "runs" / run_lecture).exists() and not (d / "diag" / run_lecture).exists()
    assert git(d, "status", "--porcelain", "--untracked-files=all") == ""


def test_lecture_sans_prereg_cas_sain_run_jouet_non_decisif(tmp_path_factory, tmp_path):
    """Répétition jouet de la chaîne : run jouet non décisif (manifeste non décisif, mode jouet) lu sans `--prereg` : la
    garde de CL3-01 laisse passer ; `lecture-p4.json` est écrit sous un manifeste de lecture non décisif."""
    d0, run = depot_p4(tmp_path_factory)
    d = copie(d0, tmp_path / "d")
    m, _ = lire_manifeste(d / "runs" / run / "manifeste.json")
    assert m["decisif"] is False and m["config"]["mode"] == "jouet"
    lp.exiger_lecture_permise(m)
    s = lp.analyser(d, run, "20261020-190000-lecture-p4", None, entropie=4242)
    assert s["source"]["etat"] == "complet" and s["lien_au_preenregistrement"] is None and lp.calcule(s["C1"])
    corps = verifier_resultat(d, d / "diag" / "20261020-190000-lecture-p4" / "lecture-p4.json")["resultat"]
    assert corps["issue"] == s["issue"]
    ml, _ = lire_manifeste(d / "runs" / "20261020-190000-lecture-p4" / "manifeste.json")
    assert ml["decisif"] is False and ml["preenregistrement"] is None


@pytest.mark.parametrize("artefact", ["run décisif jouet (démonstration de la contre-lecture 3)", "run en mode réel",
                                      "manifeste décisif au sceau rompu"])
def test_lecture_sans_prereg_d_un_run_decisif_ou_reel_refusee_sans_rien_ecrire(tmp_path_factory, tmp_path, monkeypatch,
                                                                               code_sous_la_racine, artefact):
    """CL3-01. Run décisif jouet sans verdict complété de P3 : la lecture décisive attend (report), puis la même lecture
    sans `--prereg`, qui lisait le run et écrivait C1 dans le module v1, est refusée. Run en mode réel (non décisif), et
    run décisif dont le manifeste ne passe plus son sceau (contenu brut lu) : refusés. Chaque fois : motif exact, aucun
    dossier ni fichier de lecture écrit, arbre propre."""
    if artefact == "run en mode réel":
        d, run = run_en_mode_reel(tmp_path_factory, tmp_path / "d")
    else:
        d, run = run_decisif_jouet(tmp_path_factory, tmp_path / "d", monkeypatch), RUN_DECISIF
    if artefact.startswith("run décisif jouet"):
        with pytest.raises(GardeArret, match="verdict complété de P3 absent"):
            lp.analyser(d, run, "20261020-181000-lecture-p4", PREREG, entropie=ENTROPIE_JOUET)
        _rien_d_ecrit(d, "20261020-181000-lecture-p4")
    if artefact == "manifeste décisif au sceau rompu":
        with open(d / "runs" / run / "manifeste.json", "a", encoding="utf-8") as f:
            f.write("\n")
        with pytest.raises(GardeArret):
            lire_manifeste(d / "runs" / run / "manifeste.json")
        committer(d, "manifeste altéré après son sceau")
    with pytest.raises(GardeArret) as e:
        lp.analyser(d, run, "20261020-182000-lecture-p4", None, entropie=ENTROPIE_JOUET)
    assert str(e.value) == lp.MOTIF_SANS_PREREG
    assert lp.MOTIF_SANS_PREREG == "lecture sans préenregistrement d'un run décisif ou réel : refusée sans rien écrire"
    _rien_d_ecrit(d, "20261020-182000-lecture-p4")


def test_lecture_sans_prereg_en_ligne_de_commande_refusee_sans_rien_ecrire(tmp_path_factory, tmp_path, monkeypatch,
                                                                         code_sous_la_racine):
    """La ligne de commande passe par `analyser` : run décisif jouet lu sans `--prereg` : « ARRÊT » avec le motif, code 1,
    aucun dossier ni fichier de lecture, ni `__pycache__`."""
    d = run_decisif_jouet(tmp_path_factory, tmp_path / "d", monkeypatch)
    env = dict(os.environ, PYTHONPATH=str(RACINE_REELLE / "src"))
    r = subprocess.run([sys.executable, "-B", str(ICI / "lecture_p4_v1.py"), "--run-source", RUN_DECISIF, "--run-lecture",
                        "20261020-183000-lecture-p4", "--entropie", str(ENTROPIE_JOUET)], cwd=d, env=env,
                       capture_output=True, text=True, timeout=600)
    assert r.returncode == 1 and f"ARRÊT : {lp.MOTIF_SANS_PREREG}" in r.stderr, r.stderr[-1000:]
    _rien_d_ecrit(d, "20261020-183000-lecture-p4")
    assert not list(d.rglob("__pycache__"))


def test_regle_de_la_lecture_permise_cas_sains_et_artefacts():
    """`exiger_lecture_permise` : run ni décisif ni réel, avec ou sans lien : permis ; run décisif ou réel : permis avec le
    lien complet des gardes du mode décisif seulement ; lien absent, avec un refus, run source non vérifié, sans verdict
    complété ou sans table des critères : refus."""
    jouet, decisif = {"decisif": False, "config": {"mode": "jouet"}}, {"decisif": True, "config": {"mode": "jouet"}}
    reel, les_deux = {"decisif": False, "config": {"mode": "reel"}}, {"decisif": True, "config": {"mode": "reel"}}
    for m, lien in ((None, None), (jouet, None), (jouet, LIEN_SAIN), ({"decisif": False}, None), (decisif, LIEN_SAIN),
                    (reel, LIEN_SAIN), (les_deux, LIEN_SAIN)):
        lp.exiger_lecture_permise(m, lien)
    sans = lambda k: {x: v for x, v in LIEN_SAIN.items() if x != k}  # noqa: E731
    for m in (decisif, reel, les_deux):
        for lien in (None, "lien", dict(LIEN_SAIN, refus="entropie"), dict(LIEN_SAIN, run_source_verifie=False),
                     sans("run_source_verifie"), sans("verdict_p3"), sans("table_des_criteres")):
            with pytest.raises(GardeArret, match=re.escape(lp.MOTIF_SANS_PREREG)):
                lp.exiger_lecture_permise(m, lien)


def test_autres_voies_charger_source_et_lire_refusent_un_run_decisif_sans_les_gardes(tmp_path_factory, tmp_path,
                                                                                    monkeypatch, code_sous_la_racine):
    """`charger_source_p4` et `lire`, appelées hors d'`analyser` : run décisif jouet sans lien, ou avec un lien incomplet
    → refus ; avec un lien de la forme écrite par `analyser` après toutes ses gardes (construit ici) → chargé et lu ;
    source chargée dont le lien est retiré ou changé → `lire` refuse. Cas sain : run jouet non décisif chargé et lu
    sans lien. Rien n'est écrit."""
    d = run_decisif_jouet(tmp_path_factory, tmp_path / "d", monkeypatch)
    g = graines(lp.CLES_LECTURE, 4242)
    with pytest.raises(GardeArret, match=re.escape(lp.MOTIF_SANS_PREREG)):
        lp.charger_source_p4(d, RUN_DECISIF)
    src = lp.charger_source_p4(d, RUN_DECISIF, LIEN_SAIN)
    assert src["etat"] == "complet" and src["manifeste"]["decisif"] is True and src["lien"] == LIEN_SAIN
    assert lp.lire(src, g)["issue"]["ligne"] in lp.LIGNES
    for autre in (None, dict(LIEN_SAIN, refus="entropie"), dict(LIEN_SAIN, run_source_verifie=False)):
        with pytest.raises(GardeArret, match=re.escape(lp.MOTIF_SANS_PREREG)):
            lp.charger_source_p4(d, RUN_DECISIF, autre)
        with pytest.raises(GardeArret, match=re.escape(lp.MOTIF_SANS_PREREG)):
            lp.lire(dict(src, lien=autre), g)
    with pytest.raises(GardeArret, match=re.escape(lp.MOTIF_SANS_PREREG)):
        lp.lire({k: v for k, v in src.items() if k != "lien"}, g)
    _rien_d_ecrit(d, "20261020-184000-lecture-p4")
    d0, run = depot_p4(tmp_path_factory)
    sain = lp.charger_source_p4(d0, run)
    assert sain["etat"] == "complet" and sain["lien"] is None and lp.lire(sain, g)["issue"]["ligne"] in lp.LIGNES


def test_voie_decisive_lit_un_run_decisif_quand_toutes_les_gardes_passent(tmp_path_factory, tmp_path, monkeypatch,
                                                                          code_sous_la_racine):
    """Cas sain de la voie décisive : préenregistrement scellé, table égale, verdict complété versé, gardes du run source
    passées (le jouet ne peut pas passer la garde « mode réel » : `exiger_lecture_sous_prereg_p4`, éprouvée plus haut,
    est remplacée ici par un lien de sa forme) : le run décisif est chargé et lu, sous un manifeste de lecture décisif."""
    d = run_decisif_jouet(tmp_path_factory, tmp_path / "d", monkeypatch)
    verser_verdict(d)
    committer(d, "verdict complété synthétique")
    monkeypatch.setattr(lp, "exiger_lecture_sous_prereg_p4", lambda racine, prereg, run, entropie, m: {
        "entropie": entropie, "module_cite": {}, "run_source_verifie": m is not None})
    s = lp.analyser(d, RUN_DECISIF, "20261020-185000-lecture-p4", PREREG, entropie=ENTROPIE_JOUET)
    assert s["source"]["etat"] == "complet" and lp.calcule(s["C1"])
    lien = s["lien_au_preenregistrement"]
    assert lien["table_des_criteres"]["cellules_egales"] == 22 and lien["verdict_p3"]["lignes_du_registre"] == ["R-300"]
    m, _ = lire_manifeste(d / "runs" / "20261020-185000-lecture-p4" / "manifeste.json")
    assert m["decisif"] is True and m["preenregistrement"]["chemin"] == PREREG


# ------------------------------------------------------------------------------------------------ module v3 : contournements (VM2)

RUN_X, RUN_Y = "20261020-170000-p4-jouet", "20261020-175000-p4-copie"
_DEPOTS: dict = {}


def depot_decisif_partage(tmp_path_factory) -> Path:
    """Dépôt du run décisif jouet (sans verdict complété de P3) et d'un manifeste non décisif X de même configuration,
    sans données ; joué une fois par session ; chaque test en prend une copie."""
    if "decisif" not in _DEPOTS:
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(ip, "exiger_code_importe_sous", lambda racine: None)
            d = run_decisif_jouet(tmp_path_factory, tmp_path_factory.mktemp("decisif-partage") / "depot", mp)
        m, _ = lire_manifeste(d / "runs" / RUN_DECISIF / "manifeste.json")
        creer_manifeste(d, RUN_X, m["config"], ["x"], autoriser_depot_sale=True)
        committer(d, "manifeste non décisif X")
        _DEPOTS["decisif"] = d
    return _DEPOTS["decisif"]


def _copier_scelles(de: Path, vers: Path, noms) -> None:
    vers.mkdir(parents=True, exist_ok=True)
    for n in noms:
        for x in (n, n + ".sha256"):
            shutil.copyfile(de / x, vers / x)


FORMES_AUTRE_RUN = ["manifeste de X recopié sous Y, résumé et identité du run décisif recopiés",
                    "manifeste neuf de Y, résumé et identité du run décisif recopiés",
                    "manifeste neuf de Y, diag/Y lien symbolique vers diag du run décisif",
                    "--run-source ../diag/<run décisif>, manifeste de X recopié",
                    "résumé de Y écrit sous son manifeste, identité du run décisif recopiée",
                    "--run-source X/ (chemin détourné)"]


def monter_autre_run(d: Path, forme: str) -> str:
    """Monte dans `d` une forme de VM2-contournement-01 (sans rien resceller à la main) ; rend le `--run-source`."""
    dd, rx, ry, diag_y = d / "diag" / RUN_DECISIF, d / "runs" / RUN_X, d / "runs" / RUN_Y, d / "diag" / RUN_Y
    if "manifeste neuf de Y" in forme or forme.startswith("résumé de Y"):
        m, _ = lire_manifeste(rx / "manifeste.json")
        creer_manifeste(d, RUN_Y, m["config"], ["x"], autoriser_depot_sale=True)      # manifeste propre de Y, non décisif
    source = RUN_Y
    if forme.startswith("manifeste de X recopié sous Y"):
        _copier_scelles(rx, ry, ["manifeste.json"])
        _copier_scelles(dd, diag_y, ["resume.json", "identite-p4.json"])
    elif forme == "manifeste neuf de Y, résumé et identité du run décisif recopiés":
        _copier_scelles(dd, diag_y, ["resume.json", "identite-p4.json"])
    elif forme.startswith("manifeste neuf de Y, diag/Y lien symbolique"):
        diag_y.symlink_to(RUN_DECISIF)
    elif forme.startswith("--run-source ../diag/"):
        _copier_scelles(rx, dd, ["manifeste.json"])
        source = f"../diag/{RUN_DECISIF}"
    elif forme.startswith("résumé de Y"):
        resume_d = verifier_resultat(d, dd / "resume.json")["resultat"]
        ecrire_resultat(d, ry / "manifeste.json", "resume", resume_d)                 # rattaché à Y : run_id et manifeste
        _copier_scelles(dd, diag_y, ["identite-p4.json"])
    elif forme.startswith("--run-source X/"):
        source = RUN_X + "/"                                                          # aucun fichier changé
    if git(d, "status", "--porcelain", "--untracked-files=all"):
        committer(d, forme)
    return source


def test_donnees_rattachees_au_run_source_cas_sain(tmp_path_factory, tmp_path):
    """VM2-contournement-01, cas sain : run jouet non décisif, lu sous son nom exact ; manifeste, résumé et identité
    portent ce `run_id` (et l'empreinte de ce manifeste) ; la source est complète et C1 est calculé."""
    d0, run = depot_p4(tmp_path_factory)
    d = copie(d0, tmp_path / "d")
    m, sha_m = lire_manifeste(d / "runs" / run / "manifeste.json")
    for nom in ("resume.json", "identite-p4.json"):
        corps = json.loads((d / "diag" / run / nom).read_text(encoding="utf-8"))
        assert (corps["run_id"], corps["manifeste_sha256"]) == (run, sha_m) == (m["run_id"], sha_m)
        lp.exiger_rattache_au_run(d / "diag" / run / nom, run)
    s = lp.analyser(d, run, "20261020-187000-lecture-p4", None, entropie=4242)
    assert s["source"]["etat"] == "complet" and lp.calcule(s["C1"])


@pytest.mark.parametrize("forme", FORMES_AUTRE_RUN)
def test_donnees_rattachees_a_un_autre_run_refusees_sans_rien_ecrire(tmp_path_factory, tmp_path, forme):
    """VM2-contournement-01 (V05 de la vérification) : manifeste lu sous `runs/<run source>/` d'un autre run, ou résumé ou
    identité rattachés à un autre run que celui du manifeste lu et du dossier (copies de fichiers scellés, lien
    symbolique, chemin détourné, résumé écrit sous un manifeste neuf) : refus avant tout manifeste de lecture, par
    `analyser` comme par `charger_source_p4` ; aucun dossier ni fichier de lecture écrit, arbre propre. La première forme
    est aussi lancée en ligne de commande : « ARRÊT », code 1, sans trace Python."""
    d = copie(depot_decisif_partage(tmp_path_factory), tmp_path / "d")
    source = monter_autre_run(d, forme)
    with pytest.raises(GardeArret, match=re.escape(lp.AUTRE_RUN)) as e:
        lp.charger_source_p4(d, source)
    assert str(e.value).endswith("lecture refusée sans rien écrire")
    with pytest.raises(GardeArret, match=re.escape(lp.AUTRE_RUN)):
        lp.analyser(d, source, "20261020-187000-lecture-p4", None, entropie=ENTROPIE_JOUET)
    _rien_d_ecrit(d, "20261020-187000-lecture-p4")
    if forme == FORMES_AUTRE_RUN[0]:
        env = dict(os.environ, PYTHONPATH=str(RACINE_REELLE / "src"))
        r = subprocess.run([sys.executable, "-B", str(ICI / "lecture_p4_v1.py"), "--run-source", source, "--run-lecture",
                            "20261020-187100-lecture-p4", "--entropie", str(ENTROPIE_JOUET)], cwd=d, env=env,
                           capture_output=True, text=True, timeout=600)
        assert r.returncode == 1 and "ARRÊT : " in r.stderr and lp.AUTRE_RUN in r.stderr, r.stderr[-1000:]
        assert "Traceback" not in r.stderr
        _rien_d_ecrit(d, "20261020-187100-lecture-p4")


def test_manifeste_du_run_decisif_rescelle_l1_gardee_manifeste_d_un_autre_run_refuse(tmp_path_factory, tmp_path):
    """VM2-contournement-08 gardé, à côté de la règle de -01. Manifeste du run décisif réécrit sans `decisif` et rescellé :
    son `run_id` reste celui du dossier, le résumé aussi ; le résumé reste rattaché à l'ancien manifeste : L1 écrite
    (« résumé non conforme »), sous un manifeste de lecture non décisif, rien du run lu (comportement du module v2).
    Manifeste du run non décisif X recopié sous `runs/<run décisif>/` : manifeste d'un autre run que celui du dossier :
    refus par la règle de -01, rien n'est écrit (le module v2 écrivait L1)."""
    d = copie(depot_decisif_partage(tmp_path_factory), tmp_path / "d")
    chemin = d / "runs" / RUN_DECISIF / "manifeste.json"
    m = json.loads(chemin.read_text(encoding="utf-8"))
    m.pop("decisif")
    chemin.with_name(chemin.name + ".sha256").unlink()
    chemin.write_text(json.dumps(m, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(chemin)
    committer(d, "manifeste du run décisif sans « decisif », rescellé")
    s = lp.analyser(d, RUN_DECISIF, "20261020-187200-lecture-p4", None, entropie=ENTROPIE_JOUET)
    assert s["issue"]["ligne"] == "L1" and "résumé non conforme" in s["issue"]["motif"] and "C1" not in s
    ml, _ = lire_manifeste(d / "runs" / "20261020-187200-lecture-p4" / "manifeste.json")
    assert ml["decisif"] is False
    e = copie(depot_decisif_partage(tmp_path_factory), tmp_path / "e")
    _copier_scelles(e / "runs" / RUN_X, e / "runs" / RUN_DECISIF, ["manifeste.json"])
    committer(e, "manifeste de X recopié sous le run décisif")
    with pytest.raises(GardeArret, match=re.escape(lp.AUTRE_RUN)):
        lp.analyser(e, RUN_DECISIF, "20261020-187300-lecture-p4", None, entropie=ENTROPIE_JOUET)
    _rien_d_ecrit(e, "20261020-187300-lecture-p4")


def test_config_non_dictionnaire_suspecte_refus_au_motif_de_cl3_01(tmp_path_factory, tmp_path):
    """VM2-contournement-04 : configuration du manifeste présente et non dictionnaire (liste, nulle, texte, nombre) :
    suspecte, refusée au motif de CL3-01 ; cas sains : configuration jouet, manifeste du run jouet. En ligne de commande
    (V04 de la vérification : `decisif` retiré, `config = ["x"]`, manifeste rescellé) : « ARRÊT » avec le motif de
    CL3-01, code 1, sans trace Python, rien d'écrit."""
    for config in (["x"], None, "reel", 3):
        m = {"decisif": False, "config": config}
        assert lp.est_decisif_ou_reel(m) is True
        with pytest.raises(GardeArret, match=re.escape(lp.MOTIF_SANS_PREREG)):
            lp.exiger_lecture_permise(m)
    lp.exiger_lecture_permise({"decisif": False, "config": {"mode": "jouet"}})
    d0, run = depot_p4(tmp_path_factory)
    d = copie(d0, tmp_path / "d")
    chemin = d / "runs" / run / "manifeste.json"
    lp.exiger_lecture_permise(lire_manifeste(chemin)[0])
    m = json.loads(chemin.read_text(encoding="utf-8"))
    m.pop("decisif")
    m["config"] = ["x"]
    m["config_sha256"] = hashlib.sha256(config_canonique(m["config"])).hexdigest()
    chemin.with_name(chemin.name + ".sha256").unlink()
    chemin.write_text(json.dumps(m, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(chemin)
    committer(d, "configuration non dictionnaire, manifeste rescellé")
    assert lire_manifeste(chemin)[0]["config"] == ["x"]
    env = dict(os.environ, PYTHONPATH=str(RACINE_REELLE / "src"))
    r = subprocess.run([sys.executable, "-B", str(ICI / "lecture_p4_v1.py"), "--run-source", run, "--run-lecture",
                        "20261020-188000-lecture-p4", "--entropie", "4242"], cwd=d, env=env, capture_output=True,
                       text=True, timeout=600)
    assert r.returncode == 1 and f"ARRÊT : {lp.MOTIF_SANS_PREREG}" in r.stderr, r.stderr[-1000:]
    assert "Traceback" not in r.stderr
    _rien_d_ecrit(d, "20261020-188000-lecture-p4")


@pytest.mark.parametrize("cas", ["sain", "fichier de lecture déjà là", "dossier vide", "lien symbolique pendant"])
def test_diag_de_lecture_existant_refus_r12_avant_tout_manifeste(tmp_path_factory, tmp_path, cas):
    """VM2-contournement-05 : `diag/<run de lecture>` déjà présent (fichier de lecture, dossier vide, lien symbolique
    pendant), `runs/<run de lecture>` absent : refus R12 avant `creer_manifeste` ; aucun manifeste orphelin, rien de
    changé. Cas sain : ni l'un ni l'autre, la lecture est écrite."""
    d0, run = depot_p4(tmp_path_factory)
    d = copie(d0, tmp_path / "d")
    lecture = "20261020-189000-lecture-p4"
    sortie = d / "diag" / lecture
    if cas == "sain":
        s = lp.analyser(d, run, lecture, None, entropie=4242)
        assert verifier_resultat(d, sortie / "lecture-p4.json")["resultat"]["issue"] == s["issue"]
        assert (d / "runs" / lecture / "manifeste.json").is_file()
        return
    if cas == "fichier de lecture déjà là":
        sortie.mkdir(parents=True)
        (sortie / "lecture-p4.json").write_text("{}\n", encoding="utf-8")
    elif cas == "dossier vide":
        sortie.mkdir(parents=True)
    else:
        sortie.symlink_to("absent-ailleurs")
    avant = sorted((str(p.relative_to(d)), p.is_symlink()) for p in d.rglob("*") if ".git" not in p.relative_to(d).parts)
    with pytest.raises(GardeArret, match="R12") as e:
        lp.analyser(d, run, lecture, None, entropie=4242)
    assert "existe déjà" in str(e.value) and "lecture refusée sans rien écrire" in str(e.value)
    assert not (d / "runs" / lecture).exists()
    assert sorted((str(p.relative_to(d)), p.is_symlink()) for p in d.rglob("*")
                  if ".git" not in p.relative_to(d).parts) == avant
    if cas == "fichier de lecture déjà là":
        assert (sortie / "lecture-p4.json").read_text(encoding="utf-8") == "{}\n"


DRAPEAU = "sys.dont_write_bytecode = True          # VM2-contournement-06 : aucun cache de code écrit, avant tout import du dépôt"


@pytest.mark.parametrize("script", ["lecture_p4_v1.py", "instrument_p4_v1.py"])
@pytest.mark.parametrize("cas", ["sain", "artefact : ligne sys.dont_write_bytecode retirée"])
def test_lancement_refuse_sans_option_b_n_ecrit_aucun_cache_de_code(tmp_path_factory, tmp_path, script, cas):
    """VM2-contournement-06. Lancement refusé, sans `-B` ni `PYTHONDONTWRITEBYTECODE`, du module versé sous
    `docs/procedures/P4-instrument-v1/` d'un dépôt jetable, le code du dépôt copié hors du dépôt réel : lecture (texte non
    scellé) et `--controle module` (texte sans ligne « Module de P4 ») : « ARRÊT », code 1. Cas sain : aucun `__pycache__`
    ni `.pyc` sous le dossier du module, ni sous le code copié. Artefact : la ligne `sys.dont_write_bytecode = True` du
    script retirée → le cache s'écrit (de `instrument_p4_v1` importé par la lecture ; du code copié pour l'instrument).
    Dans l'artefact, `PYTHONPYCACHEPREFIX` envoie ce cache sous le dossier temporaire des tests : rien n'est écrit dans
    l'environnement Python ni dans le dépôt réel ; ce réglage déplace le cache, il ne change pas la décision de l'écrire."""
    d = depot_neuf(tmp_path / "d")
    verser_module(d)
    module = d / ip.DOSSIER_MODULE
    (d / "prereg").mkdir()
    (d / PREREG).write_text("Texte synthétique, non scellé, sans ligne du module.\n", encoding="utf-8")
    src = tmp_path / "src"
    shutil.copytree(RACINE_REELLE / "src" / "controle_ia", src / "controle_ia",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONDONTWRITEBYTECODE", "PYTHONPYCACHEPREFIX")}
    env["PYTHONPATH"] = str(src)
    prefixe = tmp_path_factory.getbasetemp() / "prefixe-cache-de-code"
    if cas != "sain":
        p = module / script
        texte = p.read_text(encoding="utf-8")
        assert texte.count(DRAPEAU) == 1
        p.write_text(texte.replace(DRAPEAU, "sys.dont_write_bytecode = False  # artefact"), encoding="utf-8")
        env["PYTHONPYCACHEPREFIX"] = str(prefixe)
    args = (["--run-source", RUN_DECISIF, "--run-lecture", "20261020-186000-lecture-p4", "--prereg", PREREG, "--entropie",
             "1"] if script == "lecture_p4_v1.py" else ["--controle", "module", "--prereg", PREREG])
    r = subprocess.run([sys.executable, str(module / script), *args], cwd=d, env=env, capture_output=True, text=True,
                       timeout=600)
    assert r.returncode == 1 and "ARRÊT : " in r.stderr and "Traceback" not in r.stderr, r.stderr[-1000:]
    assert not (d / "runs").exists() and not (d / "diag").exists()
    caches = [x for x in tmp_path.rglob("*") if x.name == "__pycache__" or x.suffix == ".pyc"]
    if cas == "sain":
        assert caches == [], caches[:5]
    else:
        vise = (module if script == "lecture_p4_v1.py" else src).resolve()
        ecrits = [x for x in prefixe.rglob("*.pyc") if str(vise).lstrip("/") in str(x)]
        assert ecrits, "artefact non vu : aucun cache écrit sans la ligne"
        if script == "lecture_p4_v1.py":
            assert any(x.name.startswith("instrument_p4_v1.") for x in ecrits)


def test_lire_refuse_une_source_complete_sans_manifeste(tmp_path_factory):
    """VM2-contournement-07 : `lire` sur une source « complet » sans manifeste (clé retirée, nulle, texte ; clés
    `manifeste` et `lien` retirées) : refus. Cas sains : la source chargée du run jouet est lue (C1 calculé) ; une source
    L1 sans manifeste est lue (ligne L1)."""
    d, run = depot_p4(tmp_path_factory)
    g = graines(lp.CLES_LECTURE, 4242)
    src = lp.charger_source_p4(d, run)
    assert src["etat"] == "complet" and lp.calcule(lp.lire(src, g)["C1"])
    assert lp.lire({"etat": "L1", "motif": "manifeste absent"}, g)["issue"]["ligne"] == "L1"
    for autre in ({k: v for k, v in src.items() if k != "manifeste"}, dict(src, manifeste=None),
                  dict(src, manifeste="x"), {k: v for k, v in src.items() if k not in ("manifeste", "lien")}):
        with pytest.raises(GardeArret, match=re.escape(lp.MOTIF_SANS_MANIFESTE)):
            lp.lire(autre, g)


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
