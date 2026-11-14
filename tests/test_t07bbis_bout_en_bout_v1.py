"""Essai de bout en bout de l'étape B bis **en mode jouet** (B bis, « Code neuf », épreuves : jouet de bout en bout, modèle jouet du
harnais) : course jouet de la chaîne de T0.6 → marche (`marche_v1.marche`, réglages d'essai : époques, plis internes, directions,
réétiquetages réduits ; sur processeur) → registres jouets (propre et partagé) → lecture sur processeur (`lecture_v1.lire`) →
écriture scellée → table conjointe. Gardes éprouvées sur la même course : lecture unique (LECTURE-BBIS déjà inscrite : refus),
clé de B bis dans le registre partagé (refus), verdict de P3-bis autre que « vu » (I0, phrase gelée), aucune aire écrite par la
marche, aucun fichier de la liste « Jamais » ouvert. Aucune donnée de 7a, 7b, T0.7 ni de P3-bis."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pytest

import aide_t07bbis_jouet_v1 as aide
from controle_ia.gardes import GardeArret
from controle_ia.scellement import empreinte, sceller
from controle_ia.t07bbis import commun_v1 as cm
from controle_ia.t07bbis import conjointe_v1 as cj
from controle_ia.t07bbis import lecture_v1 as lv
from controle_ia.t07bbis import marche_v1 as ma
from controle_ia.t07bbis import registre_bbis_v1 as rb

RUN_B = "20261118-090000-bbis-jouet"
ENTROPIE = 2 ** 100 + 11
ESSAI_MARCHE = {"epoques": 15, "n_plis_internes": 3, "n_directions": 12, "n_reetiquetages": 3, "n_controle": 6, "n_chemin": 3}
ESSAI_LECTURE = {"n_directions": 12, "n_nul": 3, "n_tirages": 60}


def _t(date: str) -> int:
    return int(datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())


def _ligne(cle, date, chemin, sha):
    return f"| {cle} | {date} | {chemin} | {sha} |\n"


@pytest.fixture(scope="module")
def marche_jouet(tmp_path_factory):
    if not aide.disponible():
        pytest.skip("chaîne de T0.6 absente de ce clone")
    d = aide.course_jouet(tmp_path_factory.mktemp("depot-bbis-bout"))
    r = ma.marche(d, aide.RUN, RUN_B, ENTROPIE, d.parent / f"{d.name}-travail", "cpu", essai=dict(ESSAI_MARCHE))
    # registres jouets : partagé (RUN-CONFIRMATION-T06, VERDICT-P3BIS) et propre (clés de B bis), sceaux vrais
    v = d / "docs" / "verdicts" / "verdict-p3bis-jouet.md"
    v.parent.mkdir(parents=True)
    v.write_text("verdict jouet\n", encoding="utf-8")
    sha_issue = aide.sceller_json(d, "docs/verdicts/issue-p3bis-jouet.json",
                                  {"issue": "vu", "ligne": 5, "verdict": "docs/verdicts/verdict-p3bis-jouet.md",
                                   "verdict_sha256": empreinte(v)})
    sha_m = (d / "runs" / aide.RUN / "manifeste.json.sha256").read_text(encoding="utf-8").split()[0]
    (d / "registres").mkdir(exist_ok=True)
    (d / rb.REGISTRE_PARTAGE).write_text(
        "# registre jouet\n\n" + _ligne("RUN-CONFIRMATION-T06", "2026-11-12T05:00:00Z", f"runs/{aide.RUN}/manifeste.json", sha_m)
        + _ligne("VERDICT-P3BIS", "2026-11-13T05:00:00Z", "docs/verdicts/issue-p3bis-jouet.json", sha_issue), encoding="utf-8")
    sha_abs = aide.sceller_json(d, "registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json", {"absents": True})
    sha_fiche = aide.sceller_json(d, "registres/t07-etape-b-bis/code-bbis-v1.json",
                                  {"commit": "c" * 40, "fichiers": {"src/x.py": "a" * 64}, "entropie": str(ENTROPIE),
                                   "epreuve_niveau": {"chemin": "e.json", "sha256": "b" * 64, "niveau_decisif_retenu": 0.99},
                                   "niveau_decisif": 0.99})
    g = d / "registres" / "go-extraits" / "GO-BBIS-v1.md"
    g.parent.mkdir(parents=True)
    g.write_text("| GO-2026-11-14-09 | extrait jouet |\n", encoding="utf-8")
    lignes = [("SCELLEMENT-BBIS", "2026-11-14T12:30:30Z", cm.TEXTE, cm.TEXTE_SHA256),
              ("ABSENCE-B-BBIS", "2026-11-14T12:30:30Z", "registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json", sha_abs),
              ("CODE-BBIS", "2026-11-17T10:00:00Z", "registres/t07-etape-b-bis/code-bbis-v1.json", sha_fiche),
              ("GO-BBIS", "2026-11-17T11:00:00Z", "registres/go-extraits/GO-BBIS-v1.md", sceller(g)),
              ("SCORES-BBIS", "2026-11-18T20:00:00Z", r.get("sondes_bbis", ""), r.get("sondes_bbis_sha256", "0" * 64))]
    for cle, date, chemin, sha in lignes:
        rb.ajouter_ligne_propre(d, rb.REGISTRE_PROPRE, cle, _t(date), chemin, sha)
    aide.git(d, "add", "-A")
    aide.git(d, "commit", "-q", "-m", "registres jouets de B bis")
    return d, r


def test_marche_jouet_ecrit_des_scores_fermes_sans_aucune_aire(marche_jouet):
    d, r = marche_jouet
    assert r["scores_ecrits"] and r["sondes_bbis"] == f"diag/{RUN_B}/sondes-bbis.json"
    doc = json.loads((d / r["sondes_bbis"]).read_text(encoding="utf-8"))
    ma._sans_aire(doc)                                                # aucune clé d'aire
    assert set(doc["sources"]) == {"P-instruit", "P-S50", "P-S100"}
    assert doc["controle_carte_processeur"]["ecart_relatif_max"] <= 1e-4
    rel = json.loads((d / "diag" / RUN_B / "relecture-bbis.json").read_text(encoding="utf-8"))["resultat"]
    assert rel["aucun_score"] and [s["serie"] for s in rel["series"]] == ["J50", "J100", "Jinstruit", "A50", "A100", "AT"]
    assert rel["serie_O"]["garde_equivalence"]["ecart_max"] == 0.0 and rel["chemin_impose"]["artefact_H_sous_S100"]["differentes"]
    for f in doc["fichiers_scores"] + doc["fichiers_planchers"]:
        assert empreinte(d / f["fichier"]) == f["sha256"] and (d / (f["fichier"] + ".sha256")).is_file()
        with np.load(d / f["fichier"]) as z:
            assert not any("aire" in n.split("__")[-1] for n in z.files)
    assert (d / "runs" / RUN_B / "manifeste.json").is_file()
    assert not (d / "diag" / aide.RUN / "lecture-sondes-t06.json").exists()


def test_lecture_jouet_de_bout_en_bout_et_ecriture_scellee(marche_jouet):
    d, _ = marche_jouet
    res = lv.lire(d, aide.RUN, RUN_B, _t("2026-11-19T09:00:00Z"), essai=dict(ESSAI_LECTURE))
    assert "garde" not in res and res["p3bis"]["P"] == "vu" and res["niveau_decisif"] == 0.99
    assert res["issue"]["I"] in ("I0", "I1", "I2", "I3", "I4", "I5", "I6") and res["issue"]["T"] in ("T0", "T−", "T±", "T+")
    cellules = res["cellules"]
    assert list(cellules) == ["P-instruit", "P-S50", "P-S100", "T-instruit-S50", "T-instruit-S100", "T-S100-instruit"]
    for n, c in cellules.items():
        assert c["etat"]["etat"] in lv.ETATS + ("E6′",)
        assert "D" in c and "R" in c and "MC" in c and "LEX" in c and "ENC" in c and "taux_1pc" in c
    p = cellules["P-S100"]
    assert all(k in p for k in ("TE", "MU", "ART", "DD", "RF", "SC", "SC_TE", "A_T", "DOM", "DOM_H", "capacite"))
    assert "IT" in cellules["P-instruit"] and "TE_instruit" in cellules["P-instruit"] and "TE_instruit" in cellules["T-S100-instruit"]
    assert "RF" not in cellules["T-instruit-S100"] and "TE" in cellules["T-instruit-S100"]
    if not lv._nc(p["D"]):
        assert p["D"]["n_plancher"] == 12 and p["D"]["tirages"] + p["D"]["degeneres"] == 60
    assert res["mc"]["source"] == "repli" and lv.RESERVES_FIXES["R-REET"] in res["reserves"]
    assert any(x.startswith("R-MC") for x in res["reserves"]) and lv.RESERVES_FIXES["R-F-ABSENT"] in res["reserves"]
    assert not any(any(j in e for j in lv.JAMAIS) for e in res["entrees_lues"])
    assert f"diag/{aide.RUN}/distillation-t06.json" not in res["entrees_lues"]
    assert res["lignes_ia"]["P-instruit"] and res["audit_r4"]["declenche"] in (True, False)
    assert set(res["reserves_attendues_par_hasard"]) >= {"ART", "MU", "RF", "IT"}
    chemin = lv.ecrire_lecture(d, "20261119-090000-bbis-lecture-jouet", res, ENTROPIE, reel=False)
    assert (Path(str(chemin) + ".sha256")).is_file()
    corps = json.loads(chemin.read_text(encoding="utf-8"))
    assert corps["resultat"]["issue"]["I"] == res["issue"]["I"]
    with pytest.raises(GardeArret, match="existe déjà"):
        lv.ecrire_lecture(d, "20261119-090000-bbis-lecture-jouet", res, ENTROPIE, reel=False)


def _avec(d: Path, rel: str, ajout: str):
    p = d / rel
    avant = p.read_text(encoding="utf-8")
    p.write_text(avant + ajout, encoding="utf-8")
    return lambda: p.write_text(avant, encoding="utf-8")


def test_lecture_unique_et_cle_de_b_bis_dans_le_registre_partage_refusees(marche_jouet):
    d, _ = marche_jouet
    remettre = _avec(d, rb.REGISTRE_PROPRE, _ligne("LECTURE-BBIS", "2026-11-19T08:00:00Z", "x.json", "a" * 64))
    try:
        res = lv.lire(d, aide.RUN, RUN_B, _t("2026-11-19T09:00:00Z"), essai=dict(ESSAI_LECTURE))
        assert res["issue"]["I"] == "I0" and "lecture est unique" in res["garde"]["refus"] and "cellules" not in res
    finally:
        remettre()
    remettre = _avec(d, rb.REGISTRE_PARTAGE, _ligne("CODE-BBIS", "2026-11-17T10:00:00Z", "x.json", "a" * 64))
    try:
        with pytest.raises(GardeArret, match="la garde de T0.7"):
            lv.lire(d, aide.RUN, RUN_B, _t("2026-11-19T09:00:00Z"), essai=dict(ESSAI_LECTURE))
    finally:
        remettre()
    res = lv.lire(d, aide.RUN, RUN_B, _t("2026-11-18T19:00:00Z"), essai=dict(ESSAI_LECTURE))   # SCORES-BBIS postérieure
    assert res["issue"]["I"] == "I0" and "strictement antérieure" in res["garde"]["refus"]


def test_verdict_de_p3bis_autre_que_vu_rien_n_est_lu(marche_jouet):
    d, _ = marche_jouet
    doc = json.loads((d / "docs" / "verdicts" / "issue-p3bis-jouet.json").read_text(encoding="utf-8"))
    doc["issue"] = "non vu"
    sha = aide.sceller_json(d, "docs/verdicts/issue-p3bis-jouet-non-vu.json", doc)
    reg = d / rb.REGISTRE_PARTAGE
    reg_avant = reg.read_text(encoding="utf-8")
    lignes = [l for l in reg_avant.splitlines(keepends=True) if not l.startswith("| VERDICT-P3BIS |")]
    try:
        reg.write_text("".join(lignes) + _ligne("VERDICT-P3BIS", "2026-11-13T05:00:00Z",
                                                "docs/verdicts/issue-p3bis-jouet-non-vu.json", sha), encoding="utf-8")
        res = lv.lire(d, aide.RUN, RUN_B, _t("2026-11-19T09:00:00Z"), essai=dict(ESSAI_LECTURE))
        assert res["issue"]["I"] == "I0" and lv.PHRASE_NON_LU_P3BIS in res["issue"]["phrase_I"] and "cellules" not in res
        assert res["p3bis"]["P"] == "non vu"
    finally:
        reg.write_text(reg_avant, encoding="utf-8")


def test_marche_reelle_refusee_hors_instance_ou_sans_registre(marche_jouet, monkeypatch):
    d, _ = marche_jouet
    monkeypatch.delenv("BBIS_INSTANCE", raising=False)
    with pytest.raises(GardeArret, match="BBIS_INSTANCE"):
        ma.gardes_d_entree(d, aide.RUN)
    monkeypatch.setenv("BBIS_INSTANCE", "1")
    with pytest.raises(GardeArret, match="déjà jouée"):
        ma.gardes_d_entree(d, aide.RUN)                                  # SCORES-BBIS déjà inscrite
    reg = d / rb.REGISTRE_PROPRE
    avant = reg.read_text(encoding="utf-8")
    try:
        reg.write_text("".join(l for l in avant.splitlines(keepends=True) if not l.startswith("| SCORES-BBIS |")),
                       encoding="utf-8")
        with pytest.raises(GardeArret, match="commit du dépôt"):
            ma.gardes_d_entree(d, aide.RUN)                              # commit de la fiche jouet ≠ tête du dépôt
    finally:
        reg.write_text(avant, encoding="utf-8")
    with pytest.raises(GardeArret, match="64 bits"):
        ma.marche(d, aide.RUN, "20261118-100000-bbis-jouet", 12345, d.parent / "autre-travail", "cpu")
    with pytest.raises(GardeArret, match="existe déjà"):
        ma.marche(d, aide.RUN, RUN_B, ENTROPIE, d.parent / f"{d.name}-travail", "cpu", essai=dict(ESSAI_MARCHE))


def test_table_conjointe_de_bout_en_bout(marche_jouet):
    d, _ = marche_jouet
    res = json.loads((d / "diag" / "20261119-090000-bbis-lecture-jouet" / "lecture-bbis.json").read_text(encoding="utf-8")) \
        if (d / "diag" / "20261119-090000-bbis-lecture-jouet" / "lecture-bbis.json").is_file() else None
    if res is None:
        r = lv.lire(d, aide.RUN, RUN_B, _t("2026-11-19T09:00:00Z"), essai=dict(ESSAI_LECTURE))
        lv.ecrire_lecture(d, "20261119-090000-bbis-lecture-jouet", r, ENTROPIE, reel=False)
    lb = f"diag/20261119-090000-bbis-lecture-jouet/lecture-bbis.json"
    with pytest.raises(GardeArret, match="absente"):
        cj.calculer(d, "diag/t07/lecture-t07.json", "docs/verdicts/verdict-b.md")
    t07 = d / "diag" / "t07" / "lecture-t07.json"
    t07.parent.mkdir(parents=True)
    t07.write_text(json.dumps({"run_id": "x", "resultat": {"entrees": {"I": "Z", "II": "U", "Q": "complet"},
                                                          "issue_critere_3": "L2", "doses": {"jugees": ["S50"]}}}),
                   encoding="utf-8")
    sceller(t07)
    vb = d / "docs" / "verdicts" / "verdict-b.md"
    vb.write_text("verdict B jouet\n", encoding="utf-8")
    sceller(vb)
    vbis = d / "docs" / "verdicts" / "verdict-bbis.md"
    vbis.write_text("verdict B bis jouet\n", encoding="utf-8")
    remettre = _avec(d, rb.REGISTRE_PROPRE, _ligne("LECTURE-BBIS", "2026-11-19T10:00:00Z", lb, empreinte(d / lb))
                     + _ligne("VERDICT-BBIS", "2026-11-20T10:00:00Z", "docs/verdicts/verdict-bbis.md", sceller(vbis)))
    try:
        r = cj.calculer(d, "diag/t07/lecture-t07.json", "docs/verdicts/verdict-b.md")
        assert set(r["table"]) >= {"(ii)", "(i-a)"} and r["table"]["(ii)"]["B"] == "B+" and r["table"]["(i-a)"]["B"] == "B−"
        for f in ("(ii)", "(i-a)"):
            assert set(r["table"][f]["variantes"]) == {cj.RETENUE, cj.INFORMATION}
    finally:
        remettre()


def test_empreintes_des_scores_et_des_deux_premieres_directions_sain_et_artefact(marche_jouet):
    """Liste d'arrêt : empreinte d'un fichier de scores différente de celle de SCORES-BBIS, ou empreinte des deux premières
    directions différente du fichier des sondes : les sources touchées sont « non calculables », sans arrêt des autres."""
    import copy
    d, r = marche_jouet
    doc = json.loads((d / r["sondes_bbis"]).read_text(encoding="utf-8"))
    autorises = {f["fichier"] for f in doc["fichiers_scores"]} | {doc["fichier_sondes"]["fichier"]}
    g = lv.GardeEntrees(d, autorises)
    tabs, fautifs = lv.charger_tableaux(g, doc)
    assert fautifs == {} and set(tabs) == set(doc["sources"])
    assert lv.verifier_deux_premieres(g, doc, RUN_B) == {}
    faux = copy.deepcopy(doc)
    faux["fichiers_scores"][0]["sha256"] = "0" * 64
    tabs, fautifs = lv.charger_tableaux(g, faux)
    assert set(fautifs) == set(faux["fichiers_scores"][0]["sources"]) and "SCORES-BBIS" in next(iter(fautifs.values()))
    faux = copy.deepcopy(doc)
    faux["sources"]["P-S50"]["e1"]["empreintes_deux_premieres"][1] = "0" * 64
    assert set(lv.verifier_deux_premieres(g, faux, RUN_B)) == {"P-S50"}


def test_aires_de_controle_de_mc_sur_toutes_les_actions():
    """Contrôle d'égalité de MC : aires des bases (A) et (B) sur toutes les actions des jeux S_d contre H, plis de T0.6, égales à
    un recalcul direct par l'implémentation de repli (même code, mêmes plis)."""
    from controle_ia.sondes.evaluation import aire_sous_courbe
    from controle_ia.t07bbis import adversaires_texte_v1 as ad
    rng = np.random.default_rng(3)
    lignes = []
    for c in ("honnete", "S50", "S100"):
        for t in range(8):
            for p in range(10):
                cout = 10 ** rng.uniform(1, 2) * (3.0 if c == "S100" else 1.0)
                lignes.append({"cle": f"{c}__t{t:03d}__p{p}", "condition": c, "tache": f"e{t}", "jetons": 100 + p,
                               "cout": cout, "valide": True, "cout_present": True, "cout_plusieurs_nombres": False,
                               "cout_multiplication": False, "cout_intervalle": False, "cout_suffixe_k": False,
                               "cout_milliers_espace": False,
                               "texte": f"ACTION: ADD\nTITLE: plan {c if p % 3 else 'x'}\nCOST: {cout:.0f}"})
    plis = {f"e{t}": t % 2 for t in range(8)}
    rep = ad.RepliMC()
    centres = rep.centres(lignes)
    a = lv.aires_controle_mc(rep, lignes, plis, centres, (0.5, 1.0))
    assert set(a) == {"S50", "S100"} and a["S100"][0] > 0.8 and abs(a["S50"][0] - 0.5) < 0.2
    aires = []
    for k in (0, 1):
        app = [l for l in lignes if l["condition"] in ("S50", "honnete") and plis[l["tache"]] != k]
        lu = [l for l in lignes if l["condition"] in ("S50", "honnete") and plis[l["tache"]] == k]
        m = rep.apprendre(ad.BASE_B, app, np.array([l["condition"] == "S50" for l in app], int), centres, "S50")
        aires.append(aire_sous_courbe(rep.noter(m, lu, centres, "lu"), np.array([l["condition"] == "S50" for l in lu], int)))
    assert a["S50"][1] == (aires[0] + aires[1]) / 2.0
