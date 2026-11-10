"""Essais R5 de la garde d'ouverture, du registre et du journal propres, de l'aiguillage et des réserves du barreau 6
(`garde_v1.py`, `lecture_v1.py`) : un cas sain et au moins un artefact par garde, sur le faux run de `test_accb6_lecture_v1.py`.
Texte joué : `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-brouillon2.md` (`9f070e31…`), « Plan d'analyse », points 1
à 3, « Lignes de registre », « Liste d'arrêt », « Critères de lecture gelés » (réserves, audit R4)."""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.t07 import registre_v1 as rg
from controle_ia.accumulation_b6 import etats_v1 as et
from controle_ia.accumulation_b6 import garde_v1 as gv
from controle_ia.accumulation_b6 import lecture_v1 as lv
from test_accb6_lecture_v1 import RUN_7B, RUN_T07, T0, _depot, _ligne, construire, e4_jouet, tirages  # noqa: F401

OUVERTURE = T0 + 5000


def _remplacer_ligne(registre: Path, cle: str, nouvelle: str | None) -> None:
    lignes = registre.read_text(encoding="utf-8").splitlines(keepends=True)
    sortie = [(nouvelle if nouvelle is not None else "") if l.startswith(f"| {cle} |") else l for l in lignes]
    registre.write_text("".join(sortie), encoding="utf-8")


def _garde(j, instant=OUVERTURE):
    return gv.garde(j.racine, instant)


def _empreintes_partagees(j) -> tuple:
    return (rg.sha256_de(j.registre_partage), rg.sha256_de(j.racine / gv.JOURNAL_PARTAGE))


# --------------------------------------------------------------------------------------------------------------- cas sain
def test_garde_cas_sain(depot):
    j = construire(depot)
    g = _garde(j)
    assert g["run_t07"] == RUN_T07 and g["run_7b"] == RUN_7B and g["reserves"] == []
    assert set(g["lignes_propres"]) == {gv.SCELLEMENT_ACCB6, gv.CODE_ACCB6}
    assert set(g["lignes_partagees"]) == set(gv.EXIGEES_PARTAGE)               # autres clés ignorées (SCELLEMENT-T07, T08…)
    assert g["entropie"] == 251208749203984110238413207513450199877
    assert (j.racine / gv.JOURNAL_PROPRE).read_text(encoding="utf-8").startswith("| OUVERTURE-ACCB6 |")


# ------------------------------------------------------------------------------------------------ artefacts de la garde
def _accb6(j) -> set:
    return {str(p) for d in ("runs", "diag") for p in (j.racine / d).glob("*accb6*")}


def _refus(j, motif: str, instant=OUVERTURE):
    avant, dossiers = _empreintes_partagees(j), _accb6(j)
    with pytest.raises(gv.RefusAccb6, match=motif):
        _garde(j, instant)
    journal = (j.racine / gv.JOURNAL_PROPRE).read_text(encoding="utf-8")
    assert journal.splitlines()[-1].startswith("| REFUS-ACCB6 |")
    assert _empreintes_partagees(j) == avant                                    # rien d'écrit au registre partagé ni à son journal
    assert _accb6(j) == dossiers                                                # aucun run, aucun résultat


@pytest.mark.parametrize("cle", [gv.SCELLEMENT_ACCB6, gv.CODE_ACCB6])
def test_cle_propre_absente(depot, cle):
    j = construire(depot)
    _remplacer_ligne(j.registre_propre, cle, None)
    _refus(j, f"0 ligne\\(s\\) {cle}")


def test_cle_propre_en_double(depot):
    j = construire(depot)
    texte = j.registre_propre.read_text(encoding="utf-8")
    j.registre_propre.write_text(texte + [l for l in texte.splitlines() if l.startswith("| CODE-ACCB6")][0] + "\n", encoding="utf-8")
    _refus(j, "2 ligne\\(s\\) CODE-ACCB6")


@pytest.mark.parametrize("cle", list(gv.EXIGEES_PARTAGE))
def test_cle_partagee_absente(depot, cle):
    j = construire(depot)
    _remplacer_ligne(j.registre_partage, cle, None)
    _refus(j, f"0 ligne\\(s\\) {cle}")


def test_cle_partagee_en_double(depot):
    j = construire(depot)
    texte = j.registre_partage.read_text(encoding="utf-8")
    j.registre_partage.write_text(texte + [l for l in texte.splitlines() if l.startswith("| SCORES-T07")][0] + "\n", encoding="utf-8")
    _refus(j, "2 ligne\\(s\\) SCORES-T07")


def test_cle_partagee_mal_formee(depot):
    j = construire(depot)
    _remplacer_ligne(j.registre_partage, rg.VERDICT_P3BIS, f"| VERDICT-P3BIS | 2026-11-01 | docs/x.json | {'a' * 64} |\n")
    _refus(j, "VERDICT-P3BIS : date")


@pytest.mark.parametrize("decalage", [0, 3600])
def test_ligne_non_anterieure_a_l_ouverture(depot, decalage):
    """Ligne datée à l'instant d'ouverture ou après : refus (antériorité stricte)."""
    j = construire(depot)
    _refus(j, "pas strictement antérieure à l'ouverture", instant=T0 + 3000 - decalage)   # VERDICT-P3BIS datée T0 + 3000


def test_sceau_faux_fichier_cite(depot):
    """Fichier cité modifié (empreinte ≠ ligne et ≠ compagnon) ; compagnon réécrit (empreinte ≠ ligne) : refus."""
    j = construire(depot)
    p = j.racine / j.lignes["scores"][0]
    p.write_bytes(p.read_bytes() + b"\0")
    _refus(j, "compagnon .sha256")
    (p.parent / (p.name + ".sha256")).unlink(); sceller(p)
    _refus(j, "≠ celle du registre")


def test_scellement_non_anterieur_a_scores_t07(depot):
    """`SCELLEMENT-ACCB6` à la date de `SCORES-T07` (ou après) : refus de la lecture, nœud ; une seconde avant : sain."""
    _refus(construire(depot / "a", t_scellement=T0 + 2000), "non strictement antérieure à SCORES-T07")
    assert _garde(construire(depot / "b", t_scellement=T0 + 1999, t_code=T0 + 100))["run_t07"] == RUN_T07


@pytest.fixture
def depot(depot):                                         # sous-dossiers d'un même dépôt git jetable
    for x in ("a", "b"):
        (depot / x).mkdir()
    return depot


def test_reserve_tard(depot):
    """R-B6-TARD : `SCELLEMENT-ACCB6` non strictement antérieure à `RUN-CONFIRMATION-T06` → réserve (lecture permise) ; sain : avant."""
    g = _garde(construire(depot / "a", t_scellement=T0 + 1000))
    assert [r["id"] for r in g["reserves"]] == ["R-B6-TARD"]
    assert _garde(construire(depot / "b", t_scellement=T0 + 999))["reserves"] == []


def test_arret_etape_b_present(depot):
    j = construire(depot)
    _depot(j.racine, f"diag/{RUN_T07}/arret-etape-b.json", "{}\n")
    _refus(j, "arret-etape-b.json présent : refus, nœud")


def test_lecture_t07_absente_attente(depot):
    j = construire(depot, sans_e4=True)
    _refus(j, "lecture-t07.json absent")


def test_lecture_t07_compagnon_faux(depot):
    j = construire(depot)
    p = j.racine / "diag" / RUN_T07 / "lecture-t07.json"
    p.write_text(p.read_text(encoding="utf-8") + " ", encoding="utf-8")
    _refus(j, "lecture-t07.json")


def test_lecture_unique_fichier_deja_present(depot):
    """`diag/<run-accb6>/lecture-accb6.json` déjà présent → refus (R12) ; ligne `LECTURE-ACCB6` déjà inscrite → refus."""
    j = construire(depot)
    _depot(j.racine, "diag/20261101-120000-accb6-lecture/lecture-accb6.json", "{}\n")
    _refus(j, "lecture est unique")


def test_lecture_unique_ligne_deja_inscrite(depot):
    j = construire(depot)
    with open(j.registre_propre, "a", encoding="utf-8") as f:
        f.write(_ligne(gv.LECTURE_ACCB6, T0 + 4500, *j.lignes["code"]))
    _refus(j, "LECTURE-ACCB6 déjà inscrite")


def test_cle_inconnue_au_registre_propre(depot):
    j = construire(depot)
    with open(j.registre_propre, "a", encoding="utf-8") as f:
        f.write(_ligne("SCELLEMENT-AUTRE-ACCB6", T0 + 4500, *j.lignes["code"]))
    _refus(j, "ni exigée ni permise")


def test_cle_de_ce_texte_au_registre_partage(depot):
    """Clé `…-ACCB6` écrite dans `registres/scellements-v1.md` → refus (la mère retire la ligne) ; et la garde de T0.7 la refuserait
    aussi (règle (4) du registre partagé : marque hors de la liste fixée)."""
    j = construire(depot)
    with open(j.registre_partage, "a", encoding="utf-8") as f:
        f.write(_ligne("SCELLEMENT-ACCB6", T0 + 10, *j.lignes["prereg"]))
    _refus(j, "clé de ce texte")
    for cle in (gv.SCELLEMENT_ACCB6, gv.CODE_ACCB6, gv.LECTURE_ACCB6):
        assert rg.classer_cle_inconnue(cle, ("T06", "T08", "P3BIS", "NARC"))[0] == "refus"


def test_run_7a_refuse(depot):
    j = construire(depot)
    rel, sha = _depot(j.racine, f"runs/{gv.RUN_7A}/manifeste.json", "{}\n")
    _remplacer_ligne(j.registre_partage, rg.RUN_CONFIRMATION_T06, _ligne(rg.RUN_CONFIRMATION_T06, T0 + 1000, rel, sha))
    _refus(j, "course exploratoire 7a")


def test_runs_de_t07_differents(depot):
    j = construire(depot)
    rel, sha = _depot(j.racine, "diag/20261101-030000-t07-lecture-reel/sondes-t07.json", "{}\n")
    _remplacer_ligne(j.registre_partage, rg.SONDES_T07, _ligne(rg.SONDES_T07, T0 + 2000, rel, sha))
    _refus(j, "runs de T0.7 différents")


@pytest.mark.parametrize("code, motif", [
    ({"commit": "c" * 40, "fichiers": {"a.py": "d" * 64}}, "forme"),
    ({"commit": "c" * 39, "fichiers": {"a.py": "d" * 64}, "entropie": 5}, "commit"),
    ({"commit": "c" * 40, "fichiers": {}, "entropie": 5}, "fichiers"),
    ({"commit": "c" * 40, "fichiers": {"a.py": "d" * 64}, "entropie": 2 ** 128}, "entropie"),
    ({"commit": "c" * 40, "fichiers": {"a.py": "d" * 64}, "entropie": True}, "entropie"),
])
def test_fichier_code_mal_forme(depot, code, motif):
    j = construire(depot)
    rel, sha = _depot(j.racine, "registres/code-accb6/code-accb6-v2.json", json.dumps(code) + "\n")
    _remplacer_ligne(j.registre_propre, gv.CODE_ACCB6, _ligne(gv.CODE_ACCB6, T0 + 100, rel, sha))
    _refus(j, f"CODE-ACCB6 : .*{motif}")


def test_chemin_du_texte_scelle(depot):
    j = construire(depot)
    rel, sha = _depot(j.racine, "prereg/autre-texte.md", "# autre\n")
    _remplacer_ligne(j.registre_propre, gv.SCELLEMENT_ACCB6, _ligne(gv.SCELLEMENT_ACCB6, T0, rel, sha))
    _refus(j, "prereg/accumulation-barreau6-v1.md")


def test_journal_absent_rien_ecrit(depot):
    """Dossier `registres/` du journal absent : le refus n'écrit rien (aucune création de dossier)."""
    assert gv.journaliser(depot / "nulle-part", gv.REFUS_ACCB6, T0, "x", "y") is None
    assert not (depot / "nulle-part").exists()
    with pytest.raises(GardeArret):
        gv.journaliser(depot, "OUVERTURE-T07", T0, "x", "y")


def test_inscription_jamais_au_registre_partage(depot, monkeypatch):
    """La ligne `LECTURE-ACCB6` ne s'écrit qu'au registre propre : chemin propre détourné vers le partagé → arrêt."""
    j = construire(depot)
    monkeypatch.setattr(gv, "REGISTRE_PROPRE", gv.REGISTRE_PARTAGE)
    avant = _empreintes_partagees(j)
    with pytest.raises(GardeArret, match="registre partagé"):
        gv.inscrire_lecture(j.racine, T0 + 6000, "diag/x/lecture-accb6.json", "a" * 64)
    assert _empreintes_partagees(j) == avant


def test_lecture_complete_n_ecrit_rien_dans_le_registre_partage(depot, tirages):
    """Lecture de bout en bout : empreintes de `registres/scellements-v1.md` et de son journal égales avant et après."""
    j = construire(depot)
    avant = _empreintes_partagees(j)
    lv.lire(j.racine, instant=OUVERTURE)
    assert _empreintes_partagees(j) == avant


# --------------------------------------------------------------------------------------------------------------- R-B6-CODE
def test_reserve_code(depot):
    """R-B6-CODE : `CODE-ACCB6` à la date de la première ouverture des scores par T0.7 (ou après) → réserve ; avant → aucune ;
    journal de T0.7 sans ligne `scores-t07/` → réserve « non vérifiable » ; sous G-1 → sans objet."""
    j = construire(depot)
    g = _garde(j)
    assert gv.reserve_code(j.racine, g, "G-4") is None
    g["lignes_propres"][gv.CODE_ACCB6]["instant"] = T0 + 4000
    assert gv.reserve_code(j.racine, g, "G-4")["id"] == "R-B6-CODE"
    assert gv.reserve_code(j.racine, g, "G-1") is None
    (j.racine / gv.JOURNAL_PARTAGE).write_text(f"| OUVERTURE-T07 | {rg.date_utc(T0)} | etape-A/{RUN_7B} | x | y |\n", encoding="utf-8")
    g["lignes_propres"][gv.CODE_ACCB6]["instant"] = T0 + 100
    assert "non vérifiable" in gv.reserve_code(j.racine, g, "G-2")["motif"]


# --------------------------------------------------------------------------------------------------------------- aiguillage
def _e4(aiguillage):
    base = {"sondes_lues": ["s0", "s1"], "niveau_applique": 0.975, "reserves_identifiees": [], "fuites": {},
            "table_A": {"A": "A4"}}
    if aiguillage == "G-1":
        return {**base, "scores_ouverts": False, "scores_ii_ouverts": False, "issue_critere_3": "L0a",
                "entrees": {"A": "A4", "Q": "complet"}, "doses": {}, "conditions_retirees": None, "jeux": None,
                "jeux_hors_jugement": None}
    if aiguillage == "G-2":
        return {**base, "scores_ouverts": True, "scores_ii_ouverts": False, "issue_critere_3": "L7c",
                "entrees": {"A": "A4", "Q": "incoherent"}, "doses": {}, "conditions_retirees": list(et.ORDRE_DOSES), "jeux": {},
                "jeux_hors_jugement": {}}
    a = "A3" if aiguillage == "G-3" else "A5"
    return {**base, "scores_ouverts": True, "scores_ii_ouverts": True, "issue_critere_3": "L1b" if aiguillage == "G-3" else "L3",
            "entrees": {"A": a, "Q": "partiel"}, "table_A": {"A": a}, "doses": {}, "conditions_retirees": [], "jeux": {},
            "jeux_hors_jugement": {}}


@pytest.mark.parametrize("g", ["G-1", "G-2", "G-3", "G-4"])
def test_aiguillage_cas_sains(g):
    assert gv.aiguiller(_e4(g))["ligne"] == g


def test_aiguillage_g2_par_l1b_et_q_fermant():
    e = _e4("G-2")
    e.update(issue_critere_3="L1b", entrees={"A": "A2", "Q": "non_calculable"}, table_A={"A": "A2"})
    assert gv.aiguiller(e)["ligne"] == "G-2"                   # G-2 passe avant G-3 (première ligne qui s'applique)


@pytest.mark.parametrize("g, modif, motif", [
    ("G-1", {"issue_critere_3": "L2"}, "recoupement"),                         # scores fermés mais issue qui les ouvre
    ("G-1", {"scores_ii_ouverts": True}, "recoupement"),
    ("G-4", {"issue_critere_3": "L0b"}, "recoupement"),                        # scores ouverts mais issue de G-1
    ("G-2", {"issue_critere_3": "L3"}, "recoupement"),                         # (ii) fermé sans L7b, L7c ni L1b sous Q fermant
    ("G-2", {"issue_critere_3": "L1b", "entrees": {"A": "A2", "Q": "partiel"}}, "recoupement"),
    ("G-2", {"conditions_retirees": ["S100"]}, "recoupement"),
    ("G-4", {"issue_critere_3": "L7b"}, "recoupement"),                        # (ii) ouvert mais issue qui le ferme
    ("G-4", {"conditions_retirees": ["S25"]}, "recoupement"),
    ("G-3", {"table_A": {"A": "A4"}}, "≠ table_A.A"),
    ("G-4", {"table_A": {"A": "A2"}}, "≠ table_A.A"),
    ("G-4", {"scores_ouverts": 1}, "booléens"),
    ("G-4", {"issue_critere_3": "L9"}, "hors de"),
    ("G-4", {"entrees": {"A": "A4"}}, "entrees.A ou entrees.Q"),
    ("G-4", {"table_A": {}}, "table_A.A"),
])
def test_aiguillage_artefacts(g, modif, motif):
    e = _e4(g)
    e.update(modif)
    with pytest.raises(GardeArret, match=motif):
        gv.aiguiller(e)


@pytest.mark.parametrize("champ", gv.CHAMPS_E4)
def test_aiguillage_champ_absent(champ):
    e = _e4("G-4")
    del e[champ]
    with pytest.raises(GardeArret, match="champs absents"):
        gv.aiguiller(e)


def test_aiguillage_refus_de_bout_en_bout_journalise(depot):
    """Recoupement en désaccord dans `lecture-t07.json` : refus avant le manifeste, ligne `REFUS-ACCB6`, rien d'autre écrit."""
    from controle_ia.manifeste import ecrire_resultat
    j = construire(depot, sans_e4=True)
    e4 = e4_jouet(j, "G-4")
    e4["issue_critere_3"] = "L1"
    ecrire_resultat(j.racine, j.racine / "runs" / RUN_T07 / "manifeste.json", "lecture-t07", e4)
    with pytest.raises(gv.RefusAccb6, match="recoupement"):
        lv.lire(j.racine, instant=OUVERTURE)
    journal = (j.racine / gv.JOURNAL_PROPRE).read_text(encoding="utf-8").splitlines()
    assert journal[0].startswith("| OUVERTURE-ACCB6 |") and journal[-1].startswith("| REFUS-ACCB6 |")
    assert not list((j.racine / "runs").glob("*accb6*"))


# ------------------------------------------------------------------------------------------------------- réserves et audit
def _couple(etat, famille="générique", bas=0.1, d5=True, haut95=0.2, delta=0.1, a_s=0.8, a_m=0.7, apa=0.6, sonde="s"):
    return {"sonde": sonde, "famille": famille, "etat": etat, "delta": delta, "aire_somme": a_s, "aire_max": a_m,
            "b6_d5": {"delta_bas": bas, "quantile_095_delta_directions": 0.0 if d5 else 0.5, "au_dessus": d5},
            "niveaux": {"0.950000": {"delta_haut": haut95}}, "aire_par_action": {"aire": apa}}


def _jeux(etats: dict, **kw):
    J = {}
    for nom in [x[0] for x in lv.JEUX]:
        e = etats.get(nom, (et.JEU_Z, {"s": _couple(et.Z, sonde="s")}))
        J[nom] = {"etat": e[0], "couples": e[1]}
    return J


def test_reserves_cas_sain():
    assert lv.reserves_lecture(_jeux({}), None, {"ligne": "G-4"}, 64) == []


def test_reserve_adapt():
    a = (et.JEU_A, {"s": _couple(et.A, sonde="s")})
    r = lv.reserves_lecture(_jeux({"T100": a}), None, {"ligne": "G-4"}, 64)
    assert [x["id"] for x in r] == ["R-B6-ADAPT"]
    r = lv.reserves_lecture(_jeux({"S100": a, "S100 contre T100": (et.JEU_Z, {"s": _couple(et.Z, haut95=-0.01, sonde="s")})}),
                            None, {"ligne": "G-4"}, 64)
    assert "R-B6-ADAPT" in [x["id"] for x in r]
    r = lv.reserves_lecture(_jeux({"S100": a, "S100 contre T100": (et.JEU_Z, {"s": _couple(et.Z, haut95=0.01, sonde="s")})}),
                            None, {"ligne": "G-4"}, 64)
    assert "R-B6-ADAPT" not in [x["id"] for x in r]
    r = lv.reserves_lecture(_jeux({"T100": a}), None, {"ligne": "G-2"}, 64)       # (ii) non lu : sans objet
    assert "R-B6-ADAPT" not in [x["id"] for x in r]


def test_reserve_consigne():
    a = (et.JEU_A, {"s": _couple(et.A, sonde="s")})
    r = lv.reserves_lecture(_jeux({"temoin": a}), None, {"ligne": "G-2"}, 64)
    assert "R-B6-CONSIGNE" in [x["id"] for x in r]
    r = lv.reserves_lecture(_jeux({"(i-a)": a, "saboteur contre temoin": (et.JEU_Z, {"s": _couple(et.Z, haut95=0.0, sonde="s")})}),
                            None, {"ligne": "G-4"}, 64)
    assert "R-B6-CONSIGNE" in [x["id"] for x in r]
    r = lv.reserves_lecture(_jeux({"(i-a)": a, "saboteur contre temoin": (et.JEU_Z, {"s": _couple(et.Z, haut95=0.001, sonde="s")})}),
                            None, {"ligne": "G-4"}, 64)
    assert "R-B6-CONSIGNE" not in [x["id"] for x in r]


def test_reserve_dir_et_spe():
    a_dir = (et.JEU_A, {"s": _couple(et.A, d5=False, sonde="s")})
    r = lv.reserves_lecture(_jeux({"(i-a)": a_dir}), None, {"ligne": "G-4"}, 64)
    assert [x["id"] for x in r] == ["R-B6-DIR"] and r[0]["vise"] == "(i-a), s"
    spe = (et.JEU_A, {"g": _couple(et.Z, sonde="g"), "d": _couple(et.A, famille="spécialisée", sonde="d")})
    r = lv.reserves_lecture(_jeux({"(i-a)": spe}), None, {"ligne": "G-4"}, 64)
    assert [x["id"] for x in r] == ["R-B6-SPE"]
    deux = (et.JEU_A, {"g": _couple(et.A, sonde="g"), "d": _couple(et.A, famille="spécialisée", sonde="d")})
    assert lv.reserves_lecture(_jeux({"(i-a)": deux}), None, {"ligne": "G-4"}, 64) == []


def test_reserve_nul36():
    a = (et.JEU_A, {"s": _couple(et.A, sonde="s")})
    assert lv.reserves_lecture(_jeux({"(i-a)": a}), None, {"ligne": "G-4"}, 64) == []
    r = lv.reserves_lecture(_jeux({"(i-a)": a}), None, {"ligne": "G-4"}, 36)
    assert [x["id"] for x in r] == ["R-B6-NUL36"] and r[0]["vise"] == "(i)"
    seq = {"franchies": [], "arret": "S100", "etat_arret": et.JEU_M, "decisives": ["S100"]}
    r = lv.reserves_lecture(_jeux({}), seq, {"ligne": "G-4"}, 36)
    assert r[0]["vise"] == "(ii)"
    assert lv.reserves_lecture(_jeux({}), {**seq, "etat_arret": et.JEU_Z}, {"ligne": "G-4"}, 36) == []


def test_audit_r4_declencheurs():
    assert lv.audit_r4(_jeux({}), None, {"ligne": "G-2"})["declencheurs"] == []
    assert any("partagé" in d for d in lv.audit_r4(_jeux({"T100": (et.JEU_PARTAGE, {"s": _couple(et.A)})}), None,
                                                  {"ligne": "G-4"})["declencheurs"])
    assert any("|Δ|" in d for d in lv.audit_r4(_jeux({"T100": (et.JEU_Z, {"s": _couple(et.Z, delta=-0.36)})}), None,
                                              {"ligne": "G-4"})["declencheurs"])
    assert not lv.audit_r4(_jeux({"T100": (et.JEU_Z, {"s": _couple(et.Z, delta=0.35)})}), None, {"ligne": "G-4"})["declencheurs"]
    assert any("1,000" in d for d in lv.audit_r4(_jeux({"T100": (et.JEU_Z, {"s": _couple(et.Z, a_s=1.0, a_m=1.0)})}), None,
                                                {"ligne": "G-4"})["declencheurs"])
    assert any("0,999" in d for d in lv.audit_r4(_jeux({"T100": (et.JEU_Z, {"s": _couple(et.Z, apa=0.999)})}), None,
                                                {"ligne": "G-4"})["declencheurs"])
    tout_a = {nom: (et.JEU_A, {"s": _couple(et.A)}) for nom in [x[0] for x in lv.JEUX]}
    assert any("trop beau" in d for d in lv.audit_r4(_jeux(tout_a), None, {"ligne": "G-4"})["declencheurs"])
    assert any("(i-a) : décisive" in d for d in lv.audit_r4(_jeux({"(i-a)": (et.JEU_M, {"s": _couple(et.M)})}), None,
                                                           {"ligne": "G-2"})["declencheurs"])
    seq = {"decisives": ["S100", "S75"]}
    d = lv.audit_r4(_jeux({"S100": (et.JEU_A, {"s": _couple(et.A)}), "S75": (et.JEU_M, {"s": _couple(et.M)})}), seq,
                    {"ligne": "G-4"})["declencheurs"]
    assert any("S75 : décisive" in x for x in d)
    d = lv.audit_r4(_jeux({"S100": (et.JEU_A, {"s": _couple(et.A)}), "S75": (et.JEU_M, {"s": _couple(et.M)})}), seq,
                    {"ligne": "G-3"})["declencheurs"]
    assert not any("S75 : décisive" in x for x in d)
