"""Essais du pilote « tour III.2 défensif », sans aucun appel réseau : doubles du collisionneur."""
import collisionneur_v2 as cv
import tour_audit_defensif_v1 as ta
from test_collisionneur_v2 import Doubles, cellules, faits, question

NEUF = sorted(cv.id_cellule(t, l) for t in ("E3-T1", "E3-T2", "E3-T3") for l in cv.LETTRES)


def courir(tmp_path, d, *extra):
    dossier = tmp_path / "audit"
    code = ta.principal(["collisionneur_v2.py", "etage3", "--faits", faits(tmp_path), "--question", question(tmp_path),
                         "--sortie", str(dossier), *extra], d.appelants())
    return code, dossier


def test_sain_trois_tours_iii2_defensif(tmp_path):
    origine = cv.CONSIGNES["E3-T2"]
    d = Doubles()
    code, dossier = courir(tmp_path, d)
    assert code == cv.CODE_FINI
    assert cellules(dossier) == NEUF
    iii2 = [a["prompt"] for a in d.appels if "Tour III.2" in a["prompt"]]
    assert len(iii2) == 3
    assert all(ta.NOUVEAU in p and "scénarios d'évasion" not in p for p in iii2)
    assert cv.CONSIGNES["E3-T2"] == origine  # consigne d'origine rétablie


def test_temoin_sans_pilote_demande_l_evasion(tmp_path):
    d, dossier = Doubles(), tmp_path / "temoin"
    code = cv.principal(["etage3", "--faits", faits(tmp_path), "--question", question(tmp_path), "--sortie", str(dossier)],
                        d.appelants())
    iii2 = [a["prompt"] for a in d.appels if "Tour III.2" in a["prompt"]]
    assert code == cv.CODE_FINI and iii2 and all("scénarios d'évasion" in p for p in iii2)  # c'est le pilote qui l'ôte


def test_consigne_inattendue_refusee_sans_appel(tmp_path, monkeypatch):
    monkeypatch.setitem(cv.CONSIGNES, "E3-T2", "Tour III.2 : autre texte.")
    d = Doubles()
    code, _ = courir(tmp_path, d)
    assert code == 1 and d.appels == []


def test_refus_consigne_tel_quel_et_porte_fermee(tmp_path):
    origine = cv.CONSIGNES["E3-T2"]
    refus = cv.Reponse(texte="", modele_servi="claude-opus-5-5", fin="refusal", categorie="cyber",
                       usage={"entree": 1, "sortie": 1})
    d = Doubles({"claude-opus-5-5": [refus]})
    code, dossier = courir(tmp_path, d)
    assert code == cv.CODE_PORTE
    assert sum(a["modele"] == "claude-opus-5-5" for a in d.appels) == 1  # une tentative, aucune relance
    assert cv.statut_courant(dossier, "E3-T1-conception-B") == "REFUS"
    assert cv.CONSIGNES["E3-T2"] == origine


def test_plafond_aucun_appel(tmp_path):
    d = Doubles()
    code, _ = courir(tmp_path, d, "--plafond-usd", "0.01")
    assert code == cv.CODE_PLAFOND and d.appels == []


def test_refuse_autre_commande(tmp_path):
    assert ta.principal(["collisionneur_v2.py", "etage1"]) == 1
