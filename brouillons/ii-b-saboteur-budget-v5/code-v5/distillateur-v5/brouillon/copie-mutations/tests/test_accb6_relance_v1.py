"""Essais R5 de la garde de non-relance du barreau 6 (`garde_v1.garde` ; candidat 1 du texte, C1-12, C1-13 ; R-2275) :
`diag/<run>/arret-accb6.json` d'un run quelconque déjà présent → refus, code 2, nœud, avant tout calcul. Faux runs de
`test_accb6_lecture_v1.py` (jeux synthétiques seulement)."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from controle_ia.manifeste import ecrire_resultat
from controle_ia.accumulation_b6 import code_accb6_v1 as ca
from controle_ia.accumulation_b6 import garde_v1 as gv
from controle_ia.accumulation_b6 import lecture_v1 as lv
from test_accb6_lecture_v1 import DOSSIER_PAQUET_JOUET, RUN_T07, T0, _depot, construire, e4_jouet, tirages  # noqa: F401

OUVERTURE = T0 + 5000
MOTIF = "aucune relance après un arrêt"


def _accb6(j) -> set:
    return {str(p) for d in ("runs", "diag") for p in (j.racine / d).glob("*accb6*")}


def test_cas_sain_autres_fichiers_d_arret(depot):
    """Cas sain : un `arret.json` (T0.6) ou un `arret-etape-b.json` d'un autre run de T0.7 ne déclenchent pas cette garde."""
    j = construire(depot)
    _depot(j.racine, "diag/20261101-010000-t06-reel/arret.json", "{}\n")
    _depot(j.racine, "diag/20261101-020000-t07-lecture-reel/arret-etape-b.json", "{}\n")
    assert gv.garde(j.racine, OUVERTURE)["run_t07"] == RUN_T07


def test_artefact_arret_d_un_run_quelconque(depot):
    """Artefact : `arret-accb6.json` sous un run quelconque de `diag/` → refus (nœud), ligne `REFUS-ACCB6`, rien d'autre d'écrit."""
    j = construire(depot)
    _depot(j.racine, "diag/20261101-120000-accb6-lecture/arret-accb6.json", "{}\n")
    avant = _accb6(j)
    with pytest.raises(gv.RefusAccb6, match=MOTIF):
        gv.garde(j.racine, OUVERTURE)
    assert _accb6(j) == avant
    assert (j.racine / gv.JOURNAL_PROPRE).read_text(encoding="utf-8").splitlines()[-1].startswith("| REFUS-ACCB6 |")


def test_relance_apres_un_arret_refusee_avant_tout_calcul(depot, tirages, monkeypatch, capsys):
    """De bout en bout : une lecture s'arrête après le manifeste (code 3, aire par action en écart de 2·10⁻⁹) ; la relance, même sur
    des entrées corrigées, est refusée (code 2) par la garde, avant le contrôle du code, l'aiguillage et tout calcul ; aucun run neuf."""
    j = construire(depot, sans_e4=True)
    e4 = e4_jouet(j, "G-4")
    nom = j.sondes[0]["nom"]
    e4["jeux"][nom]["(i-a)"]["aire"] += 2e-9
    ecrire_resultat(j.racine, j.racine / "runs" / RUN_T07 / "manifeste.json", "lecture-t07", e4)
    with pytest.raises(lv.ArretAccb6):
        lv.lire(j.racine, instant=OUVERTURE, dossier_code=j.racine / DOSSIER_PAQUET_JOUET)
    arrets = list((j.racine / "diag").glob("*-accb6-lecture/arret-accb6.json"))
    assert len(arrets) == 1
    avant = _accb6(j)
    appels = []
    monkeypatch.setattr(ca, "controler_code", lambda *a, **k: appels.append("code"))
    monkeypatch.setattr(gv, "lire_e4", lambda *a, **k: appels.append("e4"))
    with pytest.raises(gv.RefusAccb6, match=MOTIF):
        lv.lire(j.racine, instant=OUVERTURE + 10, dossier_code=j.racine / DOSSIER_PAQUET_JOUET)
    assert appels == [] and _accb6(j) == avant
    monkeypatch.setattr(ca, "dossier_du_paquet", lambda: (j.racine / DOSSIER_PAQUET_JOUET).resolve())
    monkeypatch.setattr(lv, "N_TIRAGES", lv.TIRAGES_GELES)          # la commande exige la constante du texte ; aucun tirage ici
    assert lv.main(["lire", str(j.racine)]) == lv.CODE_REFUS
    assert MOTIF in capsys.readouterr().err and _accb6(j) == avant
