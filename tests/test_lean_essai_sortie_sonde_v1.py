"""Essais R5 de la sortie structurée, des verdicts des chaînes L et S et de la sonde réseau (boucle locale seulement) —
essai Lean, D-1a."""
import json

import pytest

from controle_ia.lean_essai import sonde_reseau_v1 as R
from controle_ia.lean_essai import sortie_v1 as S

ACC_L = json.dumps({"verdict": "ACCEPTE", "etape": None, "raison": "ok", "fichier_lean": "theorem etape_1 : True := trivial"})
REJ_L = json.dumps({"verdict": "REJET", "etape": 3, "raison": "l'étape 3 est fausse", "fichier_lean": "-- échec"})
GARDES_OK = {"accepte_gardes": True, "gardes": {}}
GARDES_KO = {"accepte_gardes": False, "gardes": {"G-L2": {"ok": False, "motifs": ["sorryAx"]}, "G-L1": {"ok": True}}}


def test_sortie_saine_et_artefacts():
    assert S.lire_sortie(ACC_L, "L")[0]["verdict"] == "ACCEPTE"
    assert S.lire_sortie(REJ_L, "L")[0]["etape"] == 3
    for texte in ("pas du json", json.dumps([1]), json.dumps({"verdict": "ACCEPTE", "etape": None, "raison": "x"}),
                  json.dumps({"verdict": "PEUT-ETRE", "etape": None, "raison": "x", "fichier_lean": "f"}),
                  json.dumps({"verdict": "REJET", "etape": None, "raison": "x", "fichier_lean": "f"}),
                  json.dumps({"verdict": "ACCEPTE", "etape": 2, "raison": "x", "fichier_lean": "f"}),
                  json.dumps({"verdict": "ACCEPTE", "etape": None, "raison": "x", "fichier_lean": " "})):
        obj, motif = S.lire_sortie(texte, "L")
        assert obj is None and motif


def test_verdict_chaine_L():
    assert S.verdict_chaine_L(ACC_L, GARDES_OK, {"infidele": False})["verdict"] == "ACCEPTE"
    assert S.verdict_chaine_L(ACC_L, GARDES_KO, {"infidele": False})["motif"] == "gardes"
    assert S.verdict_chaine_L(ACC_L, GARDES_OK, {"infidele": True, "etapes": [2]})["motif"] == "infidélité"
    assert S.verdict_chaine_L(ACC_L, GARDES_OK, None)["motif"] == "relecteur absent"
    assert S.verdict_chaine_L(REJ_L, GARDES_OK, {"infidele": False}) == \
        {"verdict": "NON-ACCEPTE", "motif": "rejet", "detail": "l'étape 3 est fausse", "etape": 3}
    assert S.verdict_chaine_L("{", GARDES_OK, {"infidele": False})["motif"] == "sortie invalide"
    assert S.verdict_chaine_L(ACC_L, GARDES_OK, {"infidele": False}, plafond=True)["motif"] == "plafond"
    assert S.verdict_chaine_L(ACC_L, GARDES_OK, {"infidele": False}, refus=True)["motif"] == "refus"
    assert S.verdict_chaine_L(None, GARDES_OK, {"infidele": False}, delai=True)["motif"] == "délai"


def test_verdict_suite_S_regle_du_ou():
    acc = json.dumps({"verdict": "ACCEPTE", "etape": None, "raison": "ok"})
    rej = json.dumps({"verdict": "REJET", "etape": 0, "raison": "énoncé annoncé faux"})
    assert S.verdict_suite_S(acc, {"etapes_fausses": []})["verdict"] == "ACCEPTE"
    assert S.verdict_suite_S(acc, {"etapes_fausses": [4]})["etape"] == 4
    assert S.verdict_suite_S(rej, {"etapes_fausses": []})["etape"] == 0
    assert S.verdict_suite_S(rej, None)["motif"] == "rejet"
    assert S.verdict_suite_S(acc, None)["motif"] == "relecteur absent"
    with pytest.raises(ValueError):
        S._non("inconnu")


def test_sonde_boucle_locale_saine_et_jugement():
    assert R.sonde_boucle_locale()[0] == "ouverte"
    releve = [{"cible": "boucle locale (sain)", "classe": "ouverte", "cause": ""},
              {"cible": "tcp 1.1.1.1:443", "classe": "fermée", "cause": "refus local (EPERM)"},
              {"cible": "dns udp 185.12.64.1:53", "classe": "fermée", "cause": "sans réponse"}]
    assert R.juger(releve, "fermee") == []
    assert len(R.juger(releve, "ouverte")) == 2
    releve[1]["classe"] = "indéterminée"
    assert R.juger(releve, "fermee") and R.juger(releve, "ouverte")
    releve[0]["classe"] = "fermée"   # artefact : la sonde ne verrait même pas la boucle locale
    assert any("boucle locale" in e for e in R.juger(releve, "fermee"))


def test_requete_dns_bien_formee():
    q = R._requete_dns("example.com")
    assert q[:2] == b"\x4c\x33" and b"\x07example\x03com\x00" in q and q.endswith(b"\x00\x01\x00\x01")
