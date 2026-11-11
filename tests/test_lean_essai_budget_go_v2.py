"""Essais R5 de A7 avec verrou (CLL-12), de A12 par égalité (CLL-11) et des verdicts avec incident du bac (CLL-15)."""
import json
import threading
import time
from datetime import date

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.lean_essai import budget_v2 as B
from controle_ia.lean_essai import garde_go_v2 as GO
from controle_ia.lean_essai import sortie_v2 as S

ENTETE = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
L_D1A = ("| GO-2026-11-10-13 | 2026-11-10 | calcul | Essai Lean, D-1a : outillage seul ; **aucun appel de modèle** ; tout "
         "appel de modèle (D-1b, pilote) exige une ligne de GO à part | 65 USD | 2026-11-30 | Lazar | R-2265 |\n")
L_PILOTE = "| GO-2026-11-20-01 | 2026-11-20 | calcul | Essai Lean, pilote | 578 USD | 2026-12-10 | Lazar | R-9999 |\n"
L_AUTRE = ("| GO-2026-11-20-02 | 2026-11-20 | calcul | Autre course ; cite D-1b en passant | 40 USD | 2026-12-10 | Lazar "
           "| R-9998 |\n")
JOUR = date(2026, 11, 21)


def registre(tmp_path, *lignes):
    p = tmp_path / "go.md"
    p.write_text(ENTETE + "".join(lignes), encoding="utf-8")
    return p


# ---- CLL-12 ---------------------------------------------------------------------------------------------------------------

def test_a7_verrou_sous_concurrence(monkeypatch):
    c = B.CompteurPhase(plafond=8.0)
    origine = c._peut_lancer

    def lent(pire):
        ok = origine(pire)
        time.sleep(0.05)   # fenêtre entre le contrôle et l'inscription
        return ok
    monkeypatch.setattr(c, "_peut_lancer", lent)
    resultats = []

    def fil(i):
        try:
            c.lancer(f"L{i}", 4.0)
            resultats.append("lancé")
        except GardeArret:
            resultats.append("refusé")
    fils = [threading.Thread(target=fil, args=(i,)) for i in range(4)]
    for f in fils:
        f.start()
    for f in fils:
        f.join()
    assert sorted(resultats) == ["lancé", "lancé", "refusé", "refusé"] and sum(c.en_vol.values()) == 8.0


def test_a7_v2_sain_et_artefacts():
    c = B.CompteurPhase(plafond=100.0)
    c.lancer("L1", 4.0)
    c.terminer("L1", 1.0)
    assert c.depense == 1.0 and c.peut_lancer(4.0) and not c.coupure()
    with pytest.raises(GardeArret):
        c.terminer("L1", 1.0)
    c.lancer("L2", 4.0)
    with pytest.raises(GardeArret, match="compteur faux"):
        c.terminer("L2", 5.0)


# ---- CLL-11 ---------------------------------------------------------------------------------------------------------------

def test_a12_sain_par_egalite(tmp_path):
    p = registre(tmp_path, L_D1A, L_PILOTE, L_AUTRE)
    assert GO.autoriser_appels_modele("GO-2026-11-20-01", p, JOUR, "GO-2026-11-20-01")["plafond"] == "578 USD"


@pytest.mark.parametrize("go_id,pilote,motif", [
    ("GO-2026-11-20-02", "GO-2026-11-20-01", "≠ GO du pilote"),   # cite « D-1b » : accepté en v1 par sous-chaîne
    ("GO-2026-11-20-01", None, "non fixé"),
    ("GO-2026-11-20-01", "pas-un-go", "non fixé"),
    ("GO-2026-11-10-13", "GO-2026-11-10-13", "exclut"),
    ("GO-2026-12-01-01", "GO-2026-12-01-01", "absent"),
])
def test_a12_artefacts(tmp_path, go_id, pilote, motif):
    p = registre(tmp_path, L_D1A, L_PILOTE, L_AUTRE)
    with pytest.raises(GardeArret, match=motif):
        GO.autoriser_appels_modele(go_id, p, JOUR, pilote)


def test_a12_porte(tmp_path):
    c = B.CompteurPhase(plafond=578.0)
    p = registre(tmp_path, L_PILOTE, L_AUTRE)
    porte = GO.AppelsModeleGardes("GO-2026-11-20-02", "GO-2026-11-20-01", p, c, aujourdhui=lambda: JOUR)
    with pytest.raises(GardeArret):
        porte.appeler("L1", 4.0, {})
    assert c.en_vol == {}
    porte = GO.AppelsModeleGardes("GO-2026-11-20-01", "GO-2026-11-20-01", p, c, aujourdhui=lambda: JOUR,
                                  transport=lambda r: {"cout_usd": 0.5})
    porte.appeler("L1", 4.0, {})
    assert c.depense == 0.5
    assert isinstance(GO.jour_utc(), date)


# ---- CLL-15 ---------------------------------------------------------------------------------------------------------------

ACC = json.dumps({"verdict": "ACCEPTE", "etape": None, "raison": "ok", "fichier_lean": "theorem etape_1 : True := trivial"})


def test_verdicts_avec_incident():
    gardes = {"accepte_gardes": True, "gardes": {}}
    assert S.verdict_chaine_L(ACC, gardes, {"infidele": False})["verdict"] == "ACCEPTE"
    assert S.verdict_chaine_L(ACC, gardes, {"infidele": False}, incident_bac="délai")["motif"] == "délai"
    assert S.verdict_chaine_L(ACC, gardes, {"infidele": False}, incident_bac="mémoire")["motif"] == "mémoire"
    acc_s = json.dumps({"verdict": "ACCEPTE", "etape": None, "raison": "ok"})
    assert S.verdict_suite_S(acc_s, {"etapes_fausses": []}, incident_bac="mémoire")["motif"] == "mémoire"
    assert S.verdict_suite_S(acc_s, {"etapes_fausses": []})["verdict"] == "ACCEPTE"
    with pytest.raises(ValueError):
        S.verdict_chaine_L(ACC, gardes, {"infidele": False}, incident_bac="panne")
