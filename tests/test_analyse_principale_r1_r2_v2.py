"""Analyse principale de R1-R2, code v2 (brouillon 2 ; décisions de conv-audit, R-1091) : essais R5 sur données
synthétiques (générateur et écrivains des essais v1, formats exacts du fournisseur). Q9 : graines dérivées de l'empreinte
de ce préenregistrement scellé (mode décisif), entropie explicite exigée sinon ; Q8 : « décision de Lazar » ; calcul et
issue inchangés par rapport à v1 à entropie égale ; liste fermée du code cité v2."""
import json
from pathlib import Path

import pytest

from conftest import committer
from controle_ia.analyse_principale_r1_r2 import constantes_v1 as K
from controle_ia.analyse_principale_r1_r2 import constantes_v2 as K2
from controle_ia.analyse_principale_r1_r2 import lecture_v1 as LP
from controle_ia.analyse_principale_r1_r2 import lecture_v2 as LP2
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import graines
from controle_ia.scellement import empreinte, sceller
from test_analyse_principale_r1_r2_v1 import D, RUN, _donnees, _source

RACINE = Path(__file__).resolve().parents[1]


@pytest.fixture(autouse=True)
def constantes_reduites(monkeypatch):
    for nom, v in (("DIMENSION", D), ("TIRAGES", 300), ("N_PLANCHER", 50), ("RUN_P3", RUN)):
        monkeypatch.setattr(K, nom, v)


def _prereg(depot, nom="prereg/ap-v2.md", alterer=False):
    fichiers = LP2.FICHIERS_PAQUET + LP2.FICHIERS_ESSAIS + LP2.FICHIERS_REUTILISES
    lignes = [f"- `{c}` : `{empreinte(RACINE / c)}`" for c in fichiers]
    if alterer:
        lignes[-1] = lignes[-1][:-3] + ("0" if lignes[-1][-3] != "0" else "1") + lignes[-1][-2:]
    texte = "\n\n".join([
        "# Préenregistrement jouet v2",
        f"Empreinte des constantes (analyse principale, code v2) : `{K2.empreinte_constantes()}`",
        "## Code", *lignes, "## Hypothèse", "h", "## Prédiction chiffrée et signe attendu", "p", "## Métrique", "m",
        "## Seuil", "s", "## Plan d'analyse", "a", "## Critères de lecture gelés", "c", "## Liste d'arrêt", "l",
        "## Contre-lecture", f"relu `{'a' * 64}`, rapport `{'b' * 64}`"]) + "\n"
    p = depot / nom
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
    return sceller(p)


def test_v2_identique_a_v1_a_entropie_egale_et_entropie_exigee(depot, monkeypatch):
    d = _donnees(21, w=3.0, j=0.5)
    _source(depot, monkeypatch, d)
    with pytest.raises(GardeArret, match="entropie explicite"):
        LP2.analyser(depot, "fiche.json", "20261102-030000-x", None, autoriser_depot_sale=True)
    r2 = LP2.analyser(depot, "fiche.json", "20261102-030001-v2", None, entropie=K.entropie_racine(),
                      autoriser_depot_sale=True)
    r1 = LP.analyser(depot, "fiche.json", "20261102-030002-v1", None, autoriser_depot_sale=True)
    assert r2["calcul"] == r1["calcul"] and r2["issue"] == r1["issue"]           # même calcul, même issue
    r3 = LP2.analyser(depot, "fiche.json", "20261102-030003-v2", None, entropie=12345, autoriser_depot_sale=True)
    assert r3["calcul"]["plis"] != r1["calcul"]["plis"]                         # la graine gouverne les plis
    assert (depot / "diag" / "20261102-030001-v2" / f"{K2.NOM_SORTIE}.md.sha256").exists()


def test_Q8_mention_contraire_decision_de_Lazar(depot, monkeypatch):
    d = _donnees(9, w=3.0, mention=3.0, j=0.3)
    _source(depot, monkeypatch, d)
    r = LP2.analyser(depot, "fiche.json", "20261102-031000-v2", None, entropie=77, autoriser_depot_sale=True)
    assert r["issue"]["mention"] == "contraire" and r["issue"]["classes"]["W-J3s"] == "supérieure"
    ligne = [x for x in r["issue"]["lignes"] if x.startswith("P-R2, W − J3s")][0]
    assert "décision de Lazar" in ligne and "sans verdict" in ligne and "au-dessus du moniteur" not in ligne
    assert any("Confondu" in x for x in r["issue"]["lignes"])


def test_mode_decisif_v2_graines_de_notre_texte(depot, monkeypatch):
    d = _donnees(15)
    _source(depot, monkeypatch, d)
    monkeypatch.setattr(LP, "exiger_code_importe_sous", lambda r: None)          # vraie garde éprouvée en v1
    monkeypatch.setattr(K, "VERSIONS_EXIGEES", {k: v for k, v in LP.versions().items() if k in ("python", "numpy", "scipy")})
    sha = _prereg(depot)
    _prereg(depot, "prereg/ap-v2-altere.md", alterer=True)
    committer(depot)
    with pytest.raises(GardeArret, match="empreinte citée"):
        LP2.analyser(depot, "fiche.json", "20261102-032001-x", "prereg/ap-v2-altere.md")
    with pytest.raises(GardeArret, match="entropie"):
        LP2.analyser(depot, "fiche.json", "20261102-032002-x", "prereg/ap-v2.md", entropie=K.entropie_racine())
    r = LP2.analyser(depot, "fiche.json", "20261102-032003-analyse-principale", "prereg/ap-v2.md")
    attendue = int.from_bytes(bytes.fromhex(sha)[:16], "big")
    assert r["statut"] == "décisif" and int(r["entropie"]) == attendue == K2.entropie_de(sha)
    assert attendue != K.entropie_racine()
    man = json.loads((depot / "runs" / "20261102-032003-analyse-principale" / "manifeste.json").read_text(encoding="utf-8"))
    assert man["decisif"] and man["preenregistrement"]["sha256"] == sha and man["commande"] == K2.COMMANDE
    ref = graines(list(K.CLES_GRAINES), attendue)
    assert all(man["graines"][k] == ref[k] for k in K.CLES_GRAINES)
    committer(depot)
    with pytest.raises(GardeArret, match="second passage"):
        LP2.analyser(depot, "fiche.json", "20261102-032004-x", "prereg/ap-v2.md")
    monkeypatch.setattr(K2, "MOTIF_Q8", "autre")                                 # constantes ≠ empreinte citée
    _prereg(depot, "prereg/ap-v2-b.md")
    monkeypatch.setattr(K2, "MOTIF_Q8", "encore autre")
    committer(depot)
    with pytest.raises(GardeArret, match="constantes gelées"):
        LP2.analyser(depot, "fiche.json", "20261102-032005-x", "prereg/ap-v2-b.md")


def test_liste_fermee_v2():
    for c in LP2.FICHIERS_PAQUET + LP2.FICHIERS_ESSAIS + LP2.FICHIERS_REUTILISES:
        assert (RACINE / c).is_file(), c
    assert set(LP.FICHIERS_PAQUET) < set(LP2.FICHIERS_PAQUET)
    with pytest.raises(GardeArret, match="liste fermée"):
        LP2.exiger_code_cite("rien")
    assert K2.entropie_de("00" * 15 + "01" + "ff" * 16) == 1
    assert isinstance(K2.entropie_de("ab" * 32), int) and K2.entropie_de("ab" * 32) < 2 ** 128
