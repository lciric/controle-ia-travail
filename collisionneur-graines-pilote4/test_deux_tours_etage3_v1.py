"""Essais du pilote deux tours (III.1 et III.2), sans aucun appel réseau : doubles du collisionneur."""
import collisionneur_v2 as cv
import deux_tours_etage3_v1 as dt
from test_collisionneur_v2 import Doubles, cellules, faits, question

DEUX = sorted(cv.id_cellule(t, l) for t in ("E3-T1", "E3-T2") for l in cv.LETTRES)


def courir(tmp_path, d, *extra):
    dossier = tmp_path / "graines"
    code = dt.principal(["collisionneur_v2.py", "etage3", "--faits", faits(tmp_path), "--question", question(tmp_path),
                         "--sortie", str(dossier), *extra], d.appelants())
    return code, dossier


def test_sain_deux_tours_seulement(tmp_path):
    d = Doubles()
    code, dossier = courir(tmp_path, d)
    assert code == cv.CODE_FINI
    assert cellules(dossier) == DEUX
    assert len(d.appels) == 6
    assert not any("Tour III.3" in a["prompt"] for a in d.appels)
    assert sum("Tour III.2" in a["prompt"] for a in d.appels) == 3
    assert cv.ORDRE_ETAGE[3] == ("E3-T1", "E3-T2", "E3-T3")  # ordre d'origine rétabli


def test_temoin_sans_pilote_trois_tours(tmp_path):
    d, dossier = Doubles(), tmp_path / "temoin"
    code = cv.principal(["etage3", "--faits", faits(tmp_path), "--question", question(tmp_path), "--sortie", str(dossier)],
                        d.appelants())
    assert code == cv.CODE_FINI and len(d.appels) == 9  # l'outil seul fait bien III.3 : c'est le pilote qui l'ôte


def test_refus_consigne_tel_quel_et_porte_fermee(tmp_path):
    refus = cv.Reponse(texte="", modele_servi="claude-opus-5-5", fin="refusal", categorie="cyber",
                       usage={"entree": 1, "sortie": 1})
    d = Doubles({"claude-opus-5-5": [refus]})
    code, dossier = courir(tmp_path, d)
    assert code == cv.CODE_PORTE
    assert sum(a["modele"] == "claude-opus-5-5" for a in d.appels) == 1  # une tentative, aucune relance
    assert not any("Tour III.2" in a["prompt"] for a in d.appels)
    assert cv.statut_courant(dossier, "E3-T1-conception-B") == "REFUS"
    assert cv.ORDRE_ETAGE[3] == ("E3-T1", "E3-T2", "E3-T3")


def test_plafond_aucun_appel(tmp_path):
    d = Doubles()
    code, _ = courir(tmp_path, d, "--plafond-usd", "0.01")
    assert code == cv.CODE_PLAFOND and d.appels == []


def test_refuse_autre_commande(tmp_path):
    assert dt.principal(["collisionneur_v2.py", "etage1"]) == 1
