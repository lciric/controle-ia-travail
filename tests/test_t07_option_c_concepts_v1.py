"""Essais R5 de l'option (c) des phrases des concepts (brouillon 21 de T0.7, `f7dcb226…`, « Accord au code », point 20 ; R-2158)
et de la réserve des couches sous le repli (plan, point 8, CLT7B-12).

- (i) `SCELLEMENT-CONCEPTS-T07` est **permise** à l'étape A, plus exigée ;
- (ii) les jeux génériques sont lus sans la ligne des concepts ; les phrases seulement si leur ligne précède strictement l'instant
  de fermeture (première `OUVERTURE-T07` de l'étape A du run, ou l'ouverture même) ; quatre concepts au moins en mode réel ;
  aucune phrase → aucune direction, aucune tâche de plancher de concept au manifeste ;
- (iii) T7-P9 « non lue : jeu des phrases des concepts non scellé à l'ouverture » et réserve R15 ;
- (iv) cas sain (ligne avant la fermeture : T7-P9 lue, pas de R15), cas du repli (ligne absente : étape A au bout, T7-P9 non lue,
  R15), artefact (ligne après la fermeture : non lue, R15 ; la lire ferait échouer l'essai), trois concepts en mode réel → refus ;
- réserve « couches … non vérifiées » écrite sous le repli (fonction et chemin de bout en bout).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t07 import lecture_v2 as lv
from controle_ia.t07 import lectures_t07_v1 as lt
from controle_ia.t07 import registre_v1 as rg
from controle_ia.t07 import sondes_neuves_v1 as sn
from test_t07_lecture_v1 import APRES_A, INSTANT, RUN_T06, _depot, _sans_ligne
from test_t07_lecture_v2 import lignes_audit, lignes_p3bis
from test_t07_sondes_neuves_v1 import _a, _b, _resultat, construire_complet, phrases_concepts

ETAT_P9_SANS = f"non lue : {lt.MOTIF_P9_SANS_PHRASES}"


@pytest.fixture
def complet(depot):
    return construire_complet(depot)


def _manifeste(j, run7: str) -> dict:
    return json.loads((j.racine / "runs" / run7 / "manifeste.json").read_text(encoding="utf-8"))


def _a_puis_b(j):
    ra = _a(j)
    run7 = ra["run_t07"]
    lignes_audit(j, run7)
    lignes_p3bis(j, APRES_A)
    return ra, run7, _b(j, run7)


def _reecrire_concepts(j, date: str) -> None:
    ligne = _sans_ligne(j, rg.SCELLEMENT_CONCEPTS_T07)
    cellules = [c.strip() for c in ligne.strip("|").split("|")]
    with open(j.registre, "a", encoding="utf-8") as f:
        f.write(rg.ecrire_ligne(rg.SCELLEMENT_CONCEPTS_T07, date, cellules[2], cellules[3]) + "\n")


# ------------------------------------------------------------------------------------------------------------------------ (i)
def test_cle_des_concepts_permise_et_non_exigee():
    assert rg.SCELLEMENT_CONCEPTS_T07 not in rg.EXIGEES_ETAPE_A and rg.SCELLEMENT_CONCEPTS_T07 in rg.PERMISES_ETAPE_A
    assert rg.EXIGEES_ETAPE_A == (rg.RUN_CONFIRMATION_T06,)


# ------------------------------------------------------------------------------------------------------- (iv) cas sain
def test_ligne_avant_la_fermeture_T7P9_lue_sans_R15(complet):
    ra, run7, lec = _a_puis_b(complet)
    s = _resultat(complet, run7, "sondes-t07.json")
    assert s["phrases_concepts"]["etat"] == lt.ETAT_PHRASES_LUES
    assert any(t.startswith("plancher-concept/") for t in _manifeste(complet, run7)["graines"])
    with np.load(complet.racine / ra["scores"]["chemin"]) as z:
        assert any(k.startswith("concept_") for k in z.files)
    assert lec["predictions"]["T7-P9"]["etat"] != ETAT_P9_SANS and "lectures" in lec["predictions"]["T7-P9"]
    assert "R15" not in [r["id"] for r in lec["reserves_identifiees"]]


# ------------------------------------------------------------------------------------- (iv) ligne absente (cas du repli)
def test_ligne_absente_etape_A_au_bout_T7P9_non_lue_R15(complet):
    _sans_ligne(complet, rg.SCELLEMENT_CONCEPTS_T07)
    ra, run7, lec = _a_puis_b(complet)
    s = _resultat(complet, run7, "sondes-t07.json")
    assert s["phrases_concepts"] == {"etat": lt.ETAT_PHRASES_NON_LUES, "motif": lt.MOTIF_P9_SANS_PHRASES, "ligne": "absente"}
    neuves = s["sondes_neuves"]                     # (ii) jeux lus sans la ligne : sondes neuves apprises
    assert sum(len(neuves["concepts"][c]["couples"]) for c in ("dissimulation", "domaine")) == 30 and neuves["directions"] == []
    assert not any(t.startswith("plancher-concept/") for t in _manifeste(complet, run7)["graines"])
    with np.load(complet.racine / ra["scores"]["chemin"]) as z:
        assert not any(k.startswith(("concept_", "plancher_concept_")) for k in z.files)
        assert {f"neuf_{k}" for k in range(30)} <= set(z.files)
    assert lec["predictions"]["T7-P9"]["etat"] == ETAT_P9_SANS
    r15 = [r for r in lec["reserves_identifiees"] if r["id"] == "R15"]
    assert len(r15) == 1 and r15[0]["phrase"] == lt.PHRASES["R15"] and "absente" in r15[0]["motif"]


# ----------------------------------------------------------------------------------- (iv) artefact : ligne postérieure
def test_ligne_posterieure_a_la_fermeture_exclue_pour_de_bon(complet):
    """Première `OUVERTURE-T07` de l'étape A une demi-heure avant l'instant (repli de la variante B) ; ligne des concepts inscrite
    après elle, avant l'instant → phrases non lues, T7-P9 non lue, R15 (la lire serait l'échec de cet essai)."""
    fermeture = INSTANT - 1800
    rg.journaliser_ouverture(complet.registre, fermeture, f"etape-A/{RUN_T06}", "0" * 64)
    _reecrire_concepts(complet, rg.date_utc(INSTANT - 900))
    ra, run7, lec = _a_puis_b(complet)
    s = _resultat(complet, run7, "sondes-t07.json")
    assert s["phrases_concepts"]["etat"] == lt.ETAT_PHRASES_NON_LUES and "exclue pour de bon" in s["phrases_concepts"]["ligne"]
    assert s["sondes_neuves"]["directions"] == []
    assert lec["predictions"]["T7-P9"]["etat"] == ETAT_P9_SANS
    assert "R15" in [r["id"] for r in lec["reserves_identifiees"]]


def test_ligne_juste_avant_la_fermeture_lue(complet):
    """Cas sain voisin de l'artefact : même ouverture antérieure, ligne une seconde avant elle → lue."""
    fermeture = INSTANT - 1800
    rg.journaliser_ouverture(complet.registre, fermeture, f"etape-A/{RUN_T06}", "0" * 64)
    _reecrire_concepts(complet, rg.date_utc(fermeture - 1))
    ra = _a(complet)
    s = _resultat(complet, ra["run_t07"], "sondes-t07.json")
    assert s["phrases_concepts"]["etat"] == lt.ETAT_PHRASES_LUES and len(s["sondes_neuves"]["directions"]) > 0


# ------------------------------------------------------------------------------ (ii) minimum de concepts, lecture directe
def _lignes_v(racine: Path, contenu: str, instant: int) -> dict:
    rel, sha = _depot(racine, "prereg/jeux-c/concepts.jsonl", contenu)
    return {rg.SCELLEMENT_CONCEPTS_T07: {"instant": instant, "date": rg.date_utc(instant), "chemin": rel, "sha256": sha}}


def _trois_concepts() -> str:
    lignes = phrases_concepts().splitlines()
    extra = [json.dumps({"concept": "routes", "indice": k, "phrase_concept": f"la route {k} file", "phrase_neutre": f"la note {k} file"},
                        ensure_ascii=False) for k in (1, 2, 3)]
    return "\n".join(lignes + extra) + "\n"


def test_trois_concepts_en_mode_reel_refus_quatre_exiges(complet, monkeypatch):
    monkeypatch.setattr(lv.sn, "controler_disjonction", lambda jeux, taches: {"etat": "essai"})
    lv_ = _lignes_v(complet.racine, _trois_concepts(), INSTANT - 10)
    assert len(sn.lire_phrases_concepts(complet.racine / lv_[rg.SCELLEMENT_CONCEPTS_T07]["chemin"], 3)["concepts"]) == 3
    with pytest.raises(GardeArret, match="au moins 4"):
        lv.lire_jeux_et_phrases(complet.racine, lv_, INSTANT, complet.racine, RUN_T06, 4)
    x = lv.lire_jeux_et_phrases(complet.racine, lv_, INSTANT, complet.racine, RUN_T06, 3)
    assert x["phrases_etat"]["etat"] == lt.ETAT_PHRASES_LUES and x["phrases"] is not None
    # ligne après la fermeture : jamais lue, donc aucun refus de minimum (le jeu est exclu, R15)
    y = lv.lire_jeux_et_phrases(complet.racine, lv_, INSTANT - 10, complet.racine, RUN_T06, 4)
    assert y["phrases"] is None and y["phrases_etat"]["etat"] == lt.ETAT_PHRASES_NON_LUES
    z = lv.lire_jeux_et_phrases(complet.racine, {}, INSTANT, complet.racine, RUN_T06, 4)
    assert z["phrases"] is None and z["phrases_etat"]["ligne"] == "absente"


# ------------------------------------------------------------------------------------- réserve des couches sous le repli
def test_reserve_couches_repli_fonction():
    r = lv.reserve_couches_repli([7, 15, 23], {"couche": 15})
    assert r is not None and "[7, 23] non vérifiées" in r
    assert lv.reserve_couches_repli([15], {"couche": 15}) is None
    with pytest.raises(GardeArret, match="couche de la garde d'équivalence illisible"):
        lv.reserve_couches_repli([7, 15, 23], {})


# ------------------------------------------------------------- repli (variante B) : ligne exigée manquante, réserve des couches
from test_t07_repli_etapes_v1 import T0, _espion, _journal, _repli, b, banc  # noqa: E402,F401  (fixtures du banc du repli)
from controle_ia.t07 import repli_etapes_v1 as rt  # noqa: E402


def test_repli_ligne_exigee_manquante_rien_calcule_puis_relance(b, monkeypatch):
    """Remplace l'artefact de `test_t07_repli_etapes_v1` qui retirait `SCELLEMENT-CONCEPTS-T07`, devenue permise (option (c)) :
    la seule exigée de l'étape A, `RUN-CONFIRMATION-T06`, manque → refus de la garde, journalisé, aucun recalcul ; relance
    quand la ligne est inscrite : recalcul fait."""
    racine, run, _ = b
    reg = racine / "registres" / "scellements-v1.md"
    texte = reg.read_text(encoding="utf-8")
    ligne = next(l for l in texte.splitlines() if l.startswith(f"| {rg.RUN_CONFIRMATION_T06} |"))
    reg.write_text(texte.replace(ligne + "\n", ""), encoding="utf-8")
    appels = _espion(monkeypatch)
    with pytest.raises(rg.RefusRegistre, match="RUN-CONFIRMATION-T06"):
        _repli(b)
    assert not appels and not [x for x in (racine / "donnees" / run).glob("activations*") if x.is_dir()]
    assert any(l.startswith("| REFUS-T07 |") for l in _journal(racine))
    reg.write_text(texte, encoding="utf-8")
    assert not _repli(b, T0 + 1)["reprise"] and len(appels) == 1


def test_repli_sans_ligne_des_concepts_garde_passee(b, monkeypatch):
    """Option (c) sous la variante B : sans `SCELLEMENT-CONCEPTS-T07`, la garde du repli passe (clé permise) et le recalcul se fait."""
    racine, run, _ = b
    reg = racine / "registres" / "scellements-v1.md"
    texte = reg.read_text(encoding="utf-8")
    ligne = next(l for l in texte.splitlines() if l.startswith(f"| {rg.SCELLEMENT_CONCEPTS_T07} |"))
    reg.write_text(texte.replace(ligne + "\n", ""), encoding="utf-8")
    appels = _espion(monkeypatch)
    assert not _repli(b)["reprise"] and len(appels) == 1


def test_reserve_des_couches_ecrite_sous_le_repli_de_bout_en_bout(b, capsys):
    """`repli-seul` puis `etape-a-apres-repli` : `ouverture-t07.json` porte la garde d'équivalence et la réserve des couches que
    la garde ne voit pas (toutes les couches lues sauf celle du sous-ensemble poussé)."""
    racine, run, cfg = b
    chemin = racine / "config-t07-jouet.json"
    reg = racine / "registres" / "scellements-v1.md"
    assert lv.main(["repli-seul", str(racine), run, str(chemin), "--registre", str(reg)]) == rt.CODE_OK
    assert lv.main(["etape-a-apres-repli", str(racine), run, str(chemin), "--registre", str(reg)]) == rt.CODE_OK
    run7 = sorted(p.name for p in (racine / "runs").iterdir() if "-t07-lecture-" in p.name)[-1]
    g = json.loads((racine / "diag" / run7 / "ouverture-t07.json").read_text(encoding="utf-8"))["resultat"]["garde_identite"]
    assert g["remplacee_par"].startswith("garde d'équivalence")
    hors = [int(c) for c in cfg["couches"] if int(c) != int(g["couche"])]
    assert hors and g["reserve"] == lv.reserve_couches_repli(cfg["couches"], g)
