"""Épreuves de l'ouverture à noms suffixés, v1 (`controle_ia.barreau5_familles.ouverture_suffixes_v1`,
`scripts/lancer_b5f_ouverture_suffixes_v1.sh`) : erratum de chaîne de la relecture décisive du barreau 5, v2 (`01298f0f…`),
§ 5, et les précisions 1 à 3 de sa vérification ; cas sain et artefact pour chaque garde (R5). Écrites avant le module.

Montages réemployés, déclarés (C13, point 2) :
- la branche de la formation des essais figés de `preparer` (`tests/test_barreau5_familles_lecture_v1.py` :
  `_branche_de_formation`, `registre`, `SEL`, `MEMBRES`), importée sans changement ;
- le monde git de la commande v3 (`tests/test_commande_lecture_v3.py` : gabarit, `monter3`, `epinglage`), plus un « commit
  prouvé » (enfant de la marche, qui n'ajoute qu'une sortie sous `donnees/`) ;
- les mondes de la fabrique figée (`epreuve_verite_plantee_v1.fabriquer`, paramètres : l'empreinte du programme de lecture de
  ce dépôt), et leur jumeau suffixé, bâti ici : même sel ; instance 2 relancée (`T03-x1`, `T04-x1-r1`), `T04` et `T05`
  retirées (`-r1`) ; noms opaques redérivés ; renommage dans tous les fichiers du monde (arbre, noms de fichiers des
  jetons) ; table engagée recalculée depuis le plan de la fabrique ; inventaire, `ENGAGEMENT-B5F`, `SCORES-B5F`,
  `OUVERTURE-B5F` recalculés, ligne de relance ajoutée au registre fabriqué ; champ « copie » des coûts et du résumé posé
  selon la règle.

Parité (§ 5.6) : sur un échantillon fixé de `liste_mondes()` (les deux premiers mondes de chaque groupe, les neuf de V7), ou
sur tous si `B5F_PARITE_TOUS=1` (écart déclaré au rapport : environ trois heures pour les 7 269 mondes), le rendu du
traducteur figé est le même pour l'entrée figée sur le monde nu et pour l'ouverture recomposée sur le jumeau ; égalité exacte
des codes, niveaux, motifs, rangs et comptes, 10⁻¹² relatif pour les réels. Aucun essai n'atteint le réseau.
"""
from __future__ import annotations

import hashlib
import inspect
import json
import math
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

import test_barreau5_familles_lecture_v1 as tl     # montage figé de `preparer` (déclaré)
import test_commande_lecture_v2 as t2
import test_commande_lecture_v3 as t3
from test_commande_lecture_v3 import gabarit3, monde3  # noqa: F401  (gabarits du monde git, réemployés)
from controle_ia.barreau5_familles import engagement_v1 as en
from controle_ia.barreau5_familles import epreuve_verite_plantee_v1 as ev
from controle_ia.barreau5_familles import lecture_v1 as lv
from controle_ia.barreau5_familles import ouverture_suffixes_v1 as ov
from controle_ia.barreau5_familles import traducteur_verite_plantee_v1 as tr
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller, verifier

RACINE = Path(__file__).resolve().parents[1]
LANCEUR = "scripts/lancer_b5f_ouverture_suffixes_v1.sh"
SEL, MEMBRES = tl.SEL, tl.MEMBRES
ENTROPIE = 20261122
GRAPHIE = {"T03": "T03-x1", "T04": "T04-x1-r1", "T05": "T05-r1"}     # instance 2 relancée ; T04 et T05 retirées
RELANCE_LIGNE = ("GO-RELANCE-FORMATION-B5F", "2026-11-20T12:00:00Z", "GO-2026-11-20-99 ; instances 2")
CODE_B = {"arbre_gele": "égal hors des listes fermées de la v2 et de l'erratum"}


def _table(familles, ordre=None):
    t = en.table_des_etiquettes(SEL, [(f, m) for f in familles for m in MEMBRES])
    return t if ordre is None else [t[i] for i in ordre(len(t))]


# --- objets privés récrits à l'identique, objets figés appelés tels quels -----------------------------------------------

@pytest.mark.parametrize("nom", ["_exiger", "_lire_json", "_familles_formees", "_convertible", "_registre_au_commit"])
def test_objets_prives_de_la_lecture_recrits_a_l_identique(nom):
    assert t2._lignes_du_corps(getattr(ov, nom)) == t2._lignes_du_corps(getattr(lv, nom))
    assert inspect.signature(getattr(ov, nom)) == inspect.signature(getattr(lv, nom))


def test_autres_objets_prives_recrits_et_noms_figes_importes():
    assert t2._lignes_du_corps(ov._empreinte_engagee) == t2._lignes_du_corps(en._empreinte_engagee)
    for nom in ("_NOM_OPAQUE", "_CODE_LECTURE", "_SCORES_LIGNE"):
        assert getattr(ov, nom).pattern == getattr(lv, nom).pattern and getattr(ov, nom).flags == getattr(lv, nom).flags
    for nom in ("instance_de", "prefixe_de_copie", "exiger_copie_lue", "lire_registre_de_lecture", "programme_sha256",
                "exiger_arbre", "exiger_arbre_sans_etiquettes", "charger_entrees", "partition_des_plis", "charger_arbre",
                "exiger_alignement", "lire", "couts_depuis_formation", "resume_formation_depuis_branche",
                "relance_du_registre", "TENUES", "MEMBRES", "APPRENTISSAGE", "FORMAT_RESULTAT", "TEXTE", "TEXTE_SHA256"):
        assert getattr(ov, nom) is getattr(lv, nom), nom
    assert ov.sceller is lv.sceller and ov.en is en and ov.GardeArret is GardeArret


def _blocs(figee, recomposee):
    import difflib
    a, b = t2._lignes_du_corps(figee), t2._lignes_du_corps(recomposee)
    return [(o, [x.strip() for x in a[i1:i2]], [x.strip() for x in b[j1:j2]])
            for o, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if o != "equal"]


def test_difference_fermee_preparer():
    """`preparer` recomposé : une ligne insérée après la cohérence (engagement, épinglage, règle et traduction, gardes de
    ligne sur T_nu), rien d'autre."""
    assert _blocs(lv.preparer, ov.preparer) == [
        ("insert", [], ["table = table_nue_de_preparer(racine_formation, texte_registre, table, racine)"])]


def test_difference_fermee_garde_d_ouverture():
    assert _blocs(lv.garde_d_ouverture, ov.garde_d_ouverture) == [
        ("replace", ['code = exiger_code_de_lecture_au_commit(racine, reg["code_lecture"]["commit"]) if racine is not None else None'],
         ["code = code_au_commit_v3(racine, texte_registre) if racine is not None else None"]),
        ("replace", ["for x in table:"],
         ['decision = decider(table, copies_du_resume(formation, table, reg["relance"]), reg["engagement"])',
          "table_nu = table_traduite(table, decision)", "for x in table_nu:"]),
        ("replace", ['_exiger(len({(x["famille"], x["membre"]) for x in table}) == len(table), "table : adaptateur en double")'],
         ['_exiger(len({(x["famille"], x["membre"]) for x in table_nu}) == len(table_nu), "table : adaptateur en double")']),
        ("replace", ['return {"registre": reg, "programme_sha256": sha, "code": code, "table": v, "arbre": ar}'],
         ['return {"registre": reg, "programme_sha256": sha, "code": code, "table": v, "arbre": ar, "decision": decision,',
          '"table_nu": table_nu}'])]


def test_difference_fermee_ouvrir():
    assert _blocs(lv.ouvrir, ov.ouvrir) == [
        ("replace", ["garde = garde_d_ouverture(texte_registre, table, arbre, racine)"],
         ["garde = garde_d_ouverture(texte_registre, table, arbre, formation, racine)", 'table = garde["table_nu"]']),
        ("insert", [], ['ecrire_traduction(sortie, garde["decision"])'])]


# --- la règle (§ 5.2) sur des tables écrites ------------------------------------------------------------------------------

COPIES = {"T03": "T03-x1", "T04": "T04", "T05": "T05-r1"}


def test_graphie_cas_sains():
    for f, base in (("T03", "T03"), ("T03-x1", "T03"), ("T03-r1", "T03"), ("T03-x1-r1", "T03"), ("T10-x1", "T10")):
        assert ov.base_de(f) == base


@pytest.mark.parametrize("famille", ["T03-y1", "T03-x2", "T03-r1-x1", "T11", "T00", "A1", "t03", "T03-x1 ", "T3"])
def test_graphie_suffixe_inconnu(famille):
    with pytest.raises(GardeArret, match="suffixe inconnu"):
        ov.base_de(famille)


def test_decision_variante_b_traces_et_traduction():
    t = _table(["T03-x1", "T04", "T05-r1"])
    d = ov.decider(t, COPIES, en.empreinte_table(t))
    assert d["variante"] == "b" and d["E_b"] == en.empreinte_table(t) == d["engagement"]
    nu = [dict(x, famille=ov.base_de(x["famille"])) for x in t]
    assert d["E_a"] == en.empreinte_table(nu) != d["E_b"]
    assert d["traduction"] == {"T03-x1": "T03", "T04": "T04", "T05-r1": "T05"}
    tn = ov.table_traduite(t, d)
    assert tn == nu and [x["nom"] for x in tn] == [x["nom"] for x in t] and {x["sel"] for x in tn} == {SEL}
    with pytest.raises(GardeArret, match="noms opaques qui ne se dérivent pas"):
        en.exiger_table_coherente(tn)                     # pourquoi la cohérence n'est jamais jouée sur T_nu


def test_decision_variante_a_table_nue_meme_si_les_copies_sont_suffixees():
    t = _table(["T03", "T04", "T05"])
    d = ov.decider(t, COPIES, en.empreinte_table(t))
    assert d["variante"] == "a" and d["E_a"] == en.empreinte_table(t)
    with pytest.raises(GardeArret, match="variante \\(a\\)"):
        ov.table_traduite(t, d)


@pytest.mark.parametrize("variante, familles", [("a", ["T03", "T04", "T05"]), ("b", ["T03-x1", "T04", "T05-r1"])])
def test_temoin_table_dans_un_autre_ordre_que_celui_des_noms(variante, familles):
    """C4 : la décision porte sur T elle-même ; une table rangée autrement que par ses noms, égale à son propre
    engagement, garde sa variante ; les traces sont calculées dans son propre ordre."""
    t = _table(familles, ordre=lambda n: list(reversed(range(n))))
    assert [x["nom"] for x in t] != sorted(x["nom"] for x in t)
    d = ov.decider(t, COPIES, en.empreinte_table(t))
    assert d["variante"] == variante and d[f"E_{variante}"] == en.empreinte_table(t)


@pytest.mark.parametrize("familles, motif", [
    (["T03-x1", "T03", "T05-r1"], "deux graphies"),                    # deux graphies pour une famille
    (["T03-x1", "T04", "T05"], "ni \\(a\\) ni \\(b\\)"),             # table mélangée : T05 nu, copie lue T05-r1
    (["T03-x1-r1", "T04", "T05-r1"], "ni \\(a\\) ni \\(b\\)"),       # troisième graphie (§ 5.7)
    (["T03-y1", "T04", "T05-r1"], "suffixe inconnu")])
def test_decision_artefacts(familles, motif):
    if familles[:2] == ["T03-x1", "T03"]:
        t = en.table_des_etiquettes(SEL, [("T03-x1", "jumeau"), ("T03", "saboteur"), ("T05-r1", "jumeau")])
    else:
        t = _table(familles)
    with pytest.raises(GardeArret, match=motif):
        ov.decider(t, COPIES, en.empreinte_table(t))


def test_decision_trace_differente_de_l_engagement_refus():
    t = _table(["T03-x1", "T04", "T05-r1"])
    with pytest.raises(GardeArret, match="engagement"):
        ov.decider(t, COPIES, "0" * 64)


def test_gardes_de_ligne_sur_t_nu_doublon_et_famille_hors_plan():
    """Les gardes figées des l. 529 à 532, sur T_nu : un doublon après traduction, une famille d'apprentissage, un nom hors
    du format sont refusés."""
    t = _table(["T03-x1", "T05-r1"])
    tn = ov.table_traduite(t, ov.decider(t, COPIES, en.empreinte_table(t)))
    ov.exiger_lignes_du_plan(tn)
    with pytest.raises(GardeArret, match="adaptateur en double"):
        ov.exiger_lignes_du_plan(tn + [dict(tn[0], nom="X-99")])
    with pytest.raises(GardeArret, match="hors du plan"):
        ov.exiger_lignes_du_plan(tn + [{"nom": "X-98", "famille": "A1", "membre": "jumeau", "sel": SEL}])
    with pytest.raises(GardeArret, match="hors du plan"):
        ov.exiger_lignes_du_plan(tn + [{"nom": "Y-01", "famille": "T06", "membre": "jumeau", "sel": SEL}])


# --- preparer et variante sur la branche de formation figée (copie lue base par base, précision 3) ----------------------

@pytest.fixture
def formation(tmp_path):
    """Branche de formation : instance 2 relancée (marche `-2-x1`, copie `T03-x1`), instance 3 non relancée, famille T05
    retirée (copie `T05-r1`) ; et une autre branche où l'instance 2 n'est pas relancée (copie `T03`)."""
    rf, r2 = tmp_path / "formation", tmp_path / "formation-sans-relance"
    tl._branche_de_formation(rf, "20261123-101010-b5f-formation-2-x1", "T03-x1")
    tl._branche_de_formation(rf, "20261122-101010-b5f-formation-3", "T05-r1")
    tl._branche_de_formation(r2, "20261122-101010-b5f-formation-2", "T03")
    tl._branche_de_formation(r2, "20261122-101010-b5f-formation-3", "T05-r1")
    return {"t": tmp_path, "rf": rf, "r2": r2}


def _ecrire_table(f, t, nom="table.json"):
    p = f["t"] / nom
    p.write_text(json.dumps(t), encoding="utf-8")
    return p


def test_variante_et_preparer_cas_sain_b(formation):
    f = formation
    t = _table(["T03-x1", "T05-r1"], ordre=lambda n: [(5 * i) % n for i in range(n)])
    reg = tl.registre(en.empreinte_table(t), "b" * 64, relance=[2])
    v = ov.variante(f["rf"], reg, _ecrire_table(f, t))
    assert v["variante"] == "b" and v["E_b"] == en.empreinte_table(t) and v["copies"] == {"T03": "T03-x1", "T05": "T05-r1"}
    rendu = ov.preparer(f["rf"], reg, _ecrire_table(f, t), f["t"] / "sortie")
    assert set(rendu) == {"couts.json", "formation.json"}
    couts = json.loads((f["t"] / "sortie" / "couts.json").read_text())["familles"]
    form = json.loads((f["t"] / "sortie" / "formation.json").read_text())["familles"]
    assert {k: x["copie"] for k, x in couts.items()} == {k: x["copie"] for k, x in form.items()} == v["copies"]
    # mêmes coûts et même résumé que l'entrée figée sur la table nue (bases, même sel, noms redérivés)
    nue = _table(["T03", "T05"])
    lv.preparer(f["rf"], tl.registre(en.empreinte_table(nue), "b" * 64, relance=[2]), _ecrire_table(f, nue, "nue.json"),
                f["t"] / "sortie-figee")
    assert json.loads((f["t"] / "sortie-figee" / "couts.json").read_text())["familles"] == couts
    assert json.loads((f["t"] / "sortie-figee" / "formation.json").read_text())["familles"] == form
    # témoin : l'entrée figée refuse la table suffixée
    with pytest.raises(GardeArret, match="famille de base"):
        lv.preparer(f["rf"], reg, _ecrire_table(f, t), f["t"] / "sortie-suffixee")


def test_temoin_table_nue_variante_a_l_entree_figee_passe_le_module_neuf_refuse(formation):
    f = formation
    t = _table(["T03", "T05"])
    reg = tl.registre(en.empreinte_table(t), "b" * 64, relance=[2])
    assert ov.variante(f["rf"], reg, _ecrire_table(f, t))["variante"] == "a"
    lv.preparer(f["rf"], reg, _ecrire_table(f, t), f["t"] / "sortie-figee")
    with pytest.raises(GardeArret, match="variante \\(a\\)"):
        ov.preparer(f["rf"], reg, _ecrire_table(f, t), f["t"] / "sortie")
    assert not (f["t"] / "sortie").exists()


@pytest.mark.parametrize("cas, motif", [
    ("x1_sans_relance", "ni \\(a\\) ni \\(b\\)"), ("melangee", "ni \\(a\\) ni \\(b\\)"),
    ("deux_graphies", "deux graphies"), ("suffixe_inconnu", "suffixe inconnu"), ("retouchee", "engagement"),
    ("incoherente", "noms opaques qui ne se dérivent pas"), ("apprentissage", "suffixe inconnu")])
def test_variante_et_preparer_artefacts(formation, cas, motif):
    f = formation
    rf, relance = f["rf"], [2]
    if cas == "x1_sans_relance":                     # branche sans relance de l'instance 2 : la copie lue est T03
        t, rf, relance = _table(["T03-x1", "T05-r1"]), f["r2"], None
    elif cas == "melangee":                          # T03 à son nom formé, T05 nu alors que sa copie lue est T05-r1
        t = _table(["T03-x1", "T05"])
    elif cas == "deux_graphies":
        t = en.table_des_etiquettes(SEL, [("T03-x1", "jumeau"), ("T03", "saboteur"), ("T05-r1", "jumeau")])
    elif cas == "suffixe_inconnu":
        t = _table(["T03-x2", "T05-r1"])
    elif cas == "apprentissage":
        t = en.table_des_etiquettes(SEL, [("T03-x1", "jumeau"), ("A1", "jumeau")])
    else:
        t = _table(["T03-x1", "T05-r1"])
    engage = t
    if cas == "retouchee":                            # table retouchée après l'engagement, cohérente, graphie inconnue
        t = _table(["T03-y1", "T05-r1"])
    elif cas == "incoherente":
        t = [dict(x, famille="T05" if x["famille"] == "T05-r1" else x["famille"]) for x in t]
    reg = tl.registre(en.empreinte_table(engage), "b" * 64, relance=relance)
    with pytest.raises(GardeArret, match=motif):
        ov.variante(rf, reg, _ecrire_table(f, t))
    with pytest.raises(GardeArret, match=motif):
        ov.preparer(rf, reg, _ecrire_table(f, t), f["t"] / "sortie")
    assert not (f["t"] / "sortie").exists()           # aucun fichier écrit


def test_preparer_sans_ligne_d_engagement_refus(formation):
    f = formation
    t = _table(["T03-x1", "T05-r1"])
    reg = tl.registre(en.empreinte_table(t), "b" * 64, relance=[2], sans=("ENGAGEMENT-B5F",))
    with pytest.raises(GardeArret, match="engagement absent"):
        ov.preparer(f["rf"], reg, _ecrire_table(f, t), f["t"] / "sortie")


# --- l'épinglage, au registre du commit prouvé que cite SCORES-B5F (§ 5.5 ; précision 1) ---------------------------------

def _prouve(m):
    """Commit prouvé : enfant de la marche, une sortie de plus sous `donnees/` (le registre est celui de la marche)."""
    r = m["fige"]
    (r / "donnees" / "sortie-essai").mkdir(parents=True, exist_ok=True)
    (r / "donnees" / "sortie-essai" / "inventaire.json").write_text("{}\n")
    t3._g(r, "add", "-f", "-A", "donnees")
    t3._g(r, "commit", "-q", "-m", "sorties (commit prouvé)")
    m["prouve"] = t3._g(r, "rev-parse", "HEAD")
    return m


def _registre_ouvreur(m, table_sha, relance=None, scores=None, code=None):
    texte = tl.registre(table_sha, "b" * 64, relance=relance)
    texte = texte.replace(f"commit {'c' * 40} ; lecture sha256", f"commit {code or m['code']} ; lecture sha256")
    return texte.replace(f"commit {'c' * 40} ; inventaire sha256", f"commit {scores or m['prouve']} ; inventaire sha256")


def test_epinglage_de_l_ouverture_cas_sain(monde3):
    m = _prouve(t3.monter3(monde3))
    texte = _registre_ouvreur(m, "a" * 64)
    assert ov.code_au_commit_v3(m["commande"], texte) == {
        "commit": m["code"], "arbre_gele": CODE_B["arbre_gele"], "commit_de_code": m["k3"],
        "erratum_sha256": t3.ERRATUM}


@pytest.mark.parametrize("cas, motif", [
    ("absente", "épinglage"), ("autre_accord", "épinglage"), ("scores_absent", "SCORES-B5F"),
    ("scores_inconnu", "absent du commit"), ("v3_hors_v2", "ne descend pas"), ("session_v2", "tête de la session"),
    ("v2_retouche", "hors de la liste fermée"), ("v2_non_cite", "ne cite pas")])
def test_epinglage_de_l_ouverture_artefacts(monde3, cas, motif):
    k = {}
    if cas == "absente":
        k["lignes"] = lambda k3: []
    elif cas == "autre_accord":
        k["lignes"] = lambda k3: [t3.epinglage(k3, accord="GO-2026-11-22-117")]
    elif cas == "v3_hors_v2":
        k["v3_parent"] = lambda m, k2: m["code"]
    elif cas == "v2_retouche":
        k["dans_v2"] = lambda c: (c / "scripts" / "autre.sh").write_text("echo x\n")
    m = _prouve(t3.monter3(monde3, **k))
    texte = _registre_ouvreur(m, "a" * 64, scores={"scores_inconnu": "9" * 40}.get(cas))
    racine = m["commande"]
    if cas == "scores_absent":
        texte = "\n".join(x for x in texte.split("\n") if "SCORES-B5F" not in x)
    elif cas == "session_v2":
        racine = m["v2"]
    elif cas == "v2_non_cite":
        r = m["fige"]
        (r / en.REGISTRE_PROPRE).write_text(t2._registre(m["code"], "session_x") + t3.epinglage(m["k3"]) + "\n")
        t3._g(r, "commit", "-q", "-a", "-m", "registre sans citation")
        texte = _registre_ouvreur(m, "a" * 64, scores=t3._g(r, "rev-parse", "HEAD"))
    with pytest.raises(GardeArret, match=motif):
        ov.code_au_commit_v3(racine, texte)


def test_variante_et_preparer_exigent_l_epinglage_quand_la_racine_est_donnee(monde3, tmp_path):
    rf = tmp_path / "formation"
    tl._branche_de_formation(rf, "20261123-101010-b5f-formation-2-x1", "T03-x1")
    t = _table(["T03-x1"])
    (tmp_path / "t.json").write_text(json.dumps(t))
    m = _prouve(t3.monter3(monde3))
    texte = _registre_ouvreur(m, en.empreinte_table(t), relance=[2])
    assert ov.variante(rf, texte, tmp_path / "t.json", m["commande"])["variante"] == "b"
    ov.preparer(rf, texte, tmp_path / "t.json", tmp_path / "sortie", m["commande"])
    with pytest.raises(GardeArret, match="tête de la session"):
        ov.variante(rf, texte, tmp_path / "t.json", m["v2"])
    with pytest.raises(GardeArret, match="tête de la session"):
        ov.preparer(rf, texte, tmp_path / "t.json", tmp_path / "sortie-2", m["v2"])
    assert not (tmp_path / "sortie-2").exists()


# --- mondes de la fabrique figée et leur jumeau suffixé ------------------------------------------------------------------

def _params(**k):
    return ev.Parametres(empreinte_lecture=lv.programme_sha256(), **k)


def _canon(table) -> bytes:
    return en.forme_canonique(table)


def _suffixer(table):
    """Même sel (celui de la table), familles suffixées selon `GRAPHIE`, noms redérivés ; ordre gardé. Rend la table et
    le renommage ancien nom → nouveau nom."""
    sel = table[0]["sel"]
    cles = [(GRAPHIE.get(x["famille"], x["famille"]), x["membre"]) for x in table]
    noms = en.noms_opaques(sel, cles)
    return ([{"nom": noms[k], "famille": k[0], "membre": k[1], "sel": sel} for k in cles],
            {x["nom"]: noms[k] for x, k in zip(table, cles)})


def _renommer(x, ren):
    if isinstance(x, dict):
        return {ren.get(k, k): _renommer(v, ren) for k, v in x.items()}
    if isinstance(x, list):
        return [_renommer(v, ren) for v in x]
    if isinstance(x, str):
        return ren.get(x, x)
    return x


def jumeau(nu: Path, dest: Path, entropie: int, monde: str, params) -> Path:
    plan = ev.planter(entropie, monde, params)
    eng = [{"nom": plan["noms"][f][r], "famille": f, "membre": params.membre(r), "sel": plan["sels"][f][r]}
           for f in plan["familles"] for r in plan["membres"][f]]
    eng = [eng[i] for i in plan["ordre_table"]]
    reg = json.loads((nu / "registre.json").read_text(encoding="utf-8"))
    contenus = {x["nom"]: x["contenu"] for x in reg}
    assert contenus["ENGAGEMENT-B5F"] == f"sha256 {en.empreinte_table(eng)}"
    eng_j, ren = _suffixer(eng)
    fichier = (nu / "etiquettes.json").read_bytes()
    fichier_j = _canon(eng_j) if fichier == _canon(eng) else _canon(_suffixer(json.loads(fichier))[0])
    dest.mkdir(parents=True)
    (dest / "etiquettes.json").write_bytes(fichier_j)
    a, aj = nu / "arbre", dest / "arbre"
    inv = json.loads((a / "inventaire.json").read_text(encoding="utf-8"))
    fichiers = []
    for f in inv["fichiers"]:
        p = a / f["chemin"]
        octets = p.read_bytes()
        rel = f["chemin"]
        if octets == _canon(eng):                       # la table posée dans l'arbre (V7)
            octets = _canon(eng_j)
        elif p.suffix == ".json":
            octets = json.dumps(_renommer(json.loads(octets), ren), ensure_ascii=False, separators=(",", ":"),
                                allow_nan=False).encode("utf-8")
            m = re.fullmatch(r"(jetons/[^/]+/)(X-[0-9]{2})\.json", rel)
            if m:
                rel = f"{m[1]}{ren[m[2]]}.json"
        (aj / rel).parent.mkdir(parents=True, exist_ok=True)
        (aj / rel).write_bytes(octets)
        fichiers.append({"chemin": rel, "octets": len(octets), "sha256": hashlib.sha256(octets).hexdigest()})
    inv_j = dict(inv, fichiers=sorted(fichiers, key=lambda x: x["chemin"]))
    inv_octets = json.dumps(inv_j, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    (aj / "inventaire.json").write_bytes(inv_octets)
    for nom in ("couts.json", "formation-resume.json"):
        x = json.loads((nu / nom).read_text(encoding="utf-8"))
        for b, y in x["familles"].items():
            if b in GRAPHIE:
                y["copie"] = GRAPHIE[b]
        (dest / nom).write_text(json.dumps(x, ensure_ascii=False), encoding="utf-8")
    sha = lambda o: hashlib.sha256(o).hexdigest()  # noqa: E731
    engage_j = sha(_canon(eng_j))
    ouverture_nu = contenus["OUVERTURE-B5F"].split()[-1]
    for x in reg:
        if x["nom"] == "ENGAGEMENT-B5F":
            x["contenu"] = f"sha256 {engage_j}"
        elif x["nom"] == "SCORES-B5F":
            x["contenu"] = re.sub(r"inventaire sha256 [0-9a-f]{64}", f"inventaire sha256 {sha(inv_octets)}", x["contenu"])
        elif x["nom"] == "OUVERTURE-B5F":
            x["contenu"] = f"table sha256 {engage_j if ouverture_nu == en.empreinte_table(eng) else sha(fichier_j)}"
    reg.append({"nom": RELANCE_LIGNE[0], "horodatage": RELANCE_LIGNE[1], "contenu": RELANCE_LIGNE[2]})
    reg = sorted(reg, key=lambda x: x["horodatage"])
    (dest / "registre.txt").write_text("".join(params.format_ligne.format(**x) + "\n" for x in reg), encoding="utf-8")
    return dest


def _lire_monde(d: Path):
    return (d / "arbre", d / "etiquettes.json", d / "couts.json", d / "formation-resume.json",
            (d / "registre.txt").read_text(encoding="utf-8"))


def _rendu(nom, f, d: Path, sortie: Path, **k):
    try:
        r = f(*_lire_monde(d), sortie, **k)
    except GardeArret as e:
        return {"refus": True, "motif": str(e)}
    return tr.traduire(nom, 0, "", json.loads(r["resultat"].read_text(encoding="utf-8")))


def egal(a, b, chemin="rendu"):
    """Égalité fixée d'avance (C13, point 4) : exacte pour les codes, niveaux, motifs, rangs et comptes ; 10⁻¹² relatif
    pour les nombres réels."""
    if isinstance(a, float) or isinstance(b, float):
        assert isinstance(a, (int, float)) and isinstance(b, (int, float)), chemin
        assert math.isclose(a, b, rel_tol=1e-12, abs_tol=0.0) or a == b, (chemin, a, b)
        return
    assert type(a) is type(b), (chemin, a, b)
    if isinstance(a, dict):
        assert set(a) == set(b), chemin
        for k in a:
            egal(a[k], b[k], f"{chemin}.{k}")
    elif isinstance(a, list):
        assert len(a) == len(b), chemin
        for i, (x, y) in enumerate(zip(a, b)):
            egal(x, y, f"{chemin}[{i}]")
    else:
        assert a == b, (chemin, a, b)


def _echantillon():
    tous = ev.liste_mondes()
    if os.environ.get("B5F_PARITE_TOUS") == "1":
        return tous
    vus, choisis = {}, []
    for x in tous:
        g = x.rsplit("-", 1)[0]
        vus[g] = vus.get(g, 0) + 1
        if g == "V7" or vus[g] <= 2:
            choisis.append(x)
    return choisis


TABLE_ARTEFACTS = ("table-dans-arbre", "table-differente", "table-differente-ouverture")


@pytest.mark.parametrize("monde", _echantillon())
def test_parite_entree_figee_sur_le_monde_nu_ouverture_recomposee_sur_le_jumeau(tmp_path, monde):
    P = _params()
    nu = tmp_path / "nu"
    ev.fabriquer(ENTROPIE, monde, nu, P)
    j = jumeau(nu, tmp_path / "jumeau", ENTROPIE, monde, P)
    a = _rendu(monde, lv.ouvrir, nu, tmp_path / "sortie-figee")
    b = _rendu(monde, ov.ouvrir, j, tmp_path / "sortie-recomposee")
    cas = ev.planter(ENTROPIE, monde, P)["cas"]
    if a.get("refus") or b.get("refus"):
        assert a.get("refus") and b.get("refus"), (a, b)
        if cas not in TABLE_ARTEFACTS:
            assert re.sub(r"X-[0-9]{2}", "X-NN", a["motif"]) == re.sub(r"X-[0-9]{2}", "X-NN", b["motif"]), (a, b)
        return
    assert cas not in TABLE_ARTEFACTS
    egal(a, b)
    # le jumeau est bien en variante (b), avec la ligne de relance et des noms redérivés ; l'entrée figée le refuse
    assert json.loads((tmp_path / "sortie-recomposee" / "traduction-table-b5f.json").read_text())["variante"] == "b"
    with pytest.raises(GardeArret):
        lv.ouvrir(*_lire_monde(j), tmp_path / "sortie-figee-sur-le-jumeau")


def test_ouverture_recomposee_en_b_avec_racine_champ_code_et_fichier_de_traduction(monde3, tmp_path):
    """Le montage complet en (b) : le monde fabriqué cite le code et le commit prouvé du monde git ; le résultat porte le
    contenu de `a_garde_d_ouverture.code` fixé par l'erratum (précision 2), et le fichier de traduction scellé porte la
    table de traduction, E_a, E_b, l'engagement et l'empreinte de l'erratum."""
    m = _prouve(t3.monter3(monde3))
    P = _params(commit_code=m["code"], commit_scores=m["prouve"])
    nu = tmp_path / "nu"
    ev.fabriquer(ENTROPIE, "V1-0000", nu, P)
    j = jumeau(nu, tmp_path / "jumeau", ENTROPIE, "V1-0000", P)
    r = ov.ouvrir(*_lire_monde(j), tmp_path / "sortie", racine=m["commande"], source_registre="essai")
    assert r["contenu"]["a_garde_d_ouverture"]["code"] == {"commit": m["code"], "arbre_gele": CODE_B["arbre_gele"],
                                                           "commit_de_code": m["k3"], "erratum_sha256": t3.ERRATUM}
    tf = tmp_path / "sortie" / "traduction-table-b5f.json"
    verifier(tf)
    x = json.loads(tf.read_text(encoding="utf-8"))
    table = json.loads((j / "etiquettes.json").read_text())
    assert x["variante"] == "b" and x["erratum_sha256"] == t3.ERRATUM and x["engagement"] == x["E_b"]
    assert x["engagement"] == en.empreinte_table(table) and x["E_a"] != x["E_b"]
    assert x["traduction"] == {f: ov.base_de(f) for f in sorted({y["famille"] for y in table})}
    verifier(r["resultat"])
    # la session à l'arbre v2 : refus, rien d'écrit
    with pytest.raises(GardeArret, match="tête de la session"):
        ov.ouvrir(*_lire_monde(j), tmp_path / "sortie-v2", racine=m["v2"])
    assert not (tmp_path / "sortie-v2").exists()


def test_ouverture_recomposee_artefacts_d_ouverture(tmp_path):
    """OUVERTURE-B5F différente de la table ; table retouchée après l'engagement ; table nue (variante (a)) : refus, aucun
    fichier écrit ; l'entrée figée lit le monde nu."""
    P = _params()
    nu = tmp_path / "nu"
    ev.fabriquer(ENTROPIE, "V1-0001", nu, P)
    j = jumeau(nu, tmp_path / "jumeau", ENTROPIE, "V1-0001", P)
    with pytest.raises(GardeArret, match="variante \\(a\\)"):
        ov.ouvrir(*_lire_monde(nu), tmp_path / "s-nu")
    lv.ouvrir(*_lire_monde(nu), tmp_path / "s-nu-figee")
    texte = (j / "registre.txt").read_text()
    autre = re.sub(r"table sha256 [0-9a-f]{64}", "table sha256 " + "0" * 64, texte)
    arbre, table, couts, form, _ = _lire_monde(j)
    with pytest.raises(GardeArret, match="OUVERTURE-B5F"):
        ov.ouvrir(arbre, table, couts, form, autre, tmp_path / "s-ouverture")
    t = json.loads(table.read_text())
    cles = [("T03" if x["famille"] == "T03-x1" else x["famille"], x["membre"]) for x in t]
    noms = en.noms_opaques(t[0]["sel"], cles)
    t_ret = [{"nom": noms[k], "famille": k[0], "membre": k[1], "sel": t[0]["sel"]} for k in cles]
    (tmp_path / "retouchee.json").write_bytes(_canon(t_ret))
    with pytest.raises(GardeArret, match="engagement"):
        ov.ouvrir(arbre, tmp_path / "retouchee.json", couts, form, texte, tmp_path / "s-retouchee")
    # table mélangée, engagée et ouverte telle quelle : T05 écrit nu alors que la copie lue du résumé est T05-r1 ; la copie
    # lue se prend au résumé de la formation, jamais aux graphies de la table : ni (a) ni (b)
    cles = [("T05" if x["famille"] == "T05-r1" else x["famille"], x["membre"]) for x in t]
    noms = en.noms_opaques(t[0]["sel"], cles)
    t_mel = [{"nom": noms[k], "famille": k[0], "membre": k[1], "sel": t[0]["sel"]} for k in cles]
    (tmp_path / "melangee.json").write_bytes(_canon(t_mel))
    texte_mel = texte.replace(en.empreinte_table(t), en.empreinte_table(t_mel))
    assert texte_mel.count(en.empreinte_table(t_mel)) == 2
    with pytest.raises(GardeArret, match="ni \\(a\\) ni \\(b\\)"):
        ov.ouvrir(arbre, tmp_path / "melangee.json", couts, form, texte_mel, tmp_path / "s-melangee")
    for s in ("s-nu", "s-ouverture", "s-retouchee", "s-melangee"):
        assert not (tmp_path / s).exists()


# --- le lanceur ---------------------------------------------------------------------------------------------------------

def _jouer_lanceur(racine, *args):
    e = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHON_B5F": sys.executable, "PYTHONDONTWRITEBYTECODE": "1"}
    return subprocess.run(["bash", str(Path(racine) / LANCEUR), *args], capture_output=True, text=True, env=e,
                          cwd=str(racine))


def test_lanceur_variante_depuis_l_arbre_v3_cas_sain_et_refus(monde3, tmp_path):
    rf = tmp_path / "formation"
    tl._branche_de_formation(rf, "20261123-101010-b5f-formation-2-x1", "T03-x1")
    t = _table(["T03-x1"])
    (tmp_path / "t.json").write_text(json.dumps(t))
    m = _prouve(t3.monter3(monde3))
    r = m["fige"]
    (r / en.REGISTRE_PROPRE).write_text(_registre_ouvreur(m, en.empreinte_table(t), relance=[2]))
    t3._g(r, "commit", "-q", "-a", "-m", "registre de l'ouvreur")
    commit_registre = t3._g(r, "rev-parse", "HEAD")
    p = _jouer_lanceur(m["commande"], "variante", str(m["commande"]), commit_registre, str(rf), str(tmp_path / "t.json"))
    assert p.returncode == 0, p.stderr
    assert json.loads(p.stdout.splitlines()[-1])["variante"] == "b"
    p = _jouer_lanceur(m["commande"], "preparer", str(m["commande"]), commit_registre, str(rf), str(tmp_path / "t.json"),
                       str(tmp_path / "sortie"))
    assert p.returncode == 0, p.stderr
    assert (tmp_path / "sortie" / "couts.json.sha256").is_file()
    # le module joué depuis un autre arbre que RACINE : refus
    p = _jouer_lanceur(RACINE, "variante", str(m["commande"]), commit_registre, str(rf), str(tmp_path / "t.json"))
    assert p.returncode == 2 and "joué depuis un autre arbre" in p.stderr


@pytest.mark.parametrize("args", [[], ["inconnue"], ["commande"] + ["a"] * 10, ["monde"] + ["a"] * 6,
                                  ["variante", "a", "b", "c"], ["preparer"] + ["a"] * 4, ["ouvrir"] + ["a"] * 6,
                                  ["scores", "a", "b", "c"]])
def test_lanceur_refuse_toute_autre_forme(args):
    p = _jouer_lanceur(RACINE, *args)
    assert p.returncode == 2 and "B5F REFUS" in p.stderr and p.stdout == ""


def test_texte_du_lanceur_sans_commande_d_arret_de_creation_ni_de_reseau():
    texte = (RACINE / LANCEUR).read_text(encoding="utf-8")
    code = "\n".join(x for x in texte.splitlines() if not x.lstrip().startswith("#"))
    arret = "k" + "ill"
    for interdit in (rf"\b{arret}\b", r"vastai", r"\bcurl\b", r"\bwget\b", r"\bgit\b", r"\brm\s",
                     r"barreau5_familles\.lecture_v1"):
        assert re.search(interdit, code) is None, interdit
    assert "set -uo pipefail" in texte and "ouverture_suffixes_v1" in code
