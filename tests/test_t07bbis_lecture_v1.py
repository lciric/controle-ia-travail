"""Essais R5 de `t07bbis.lecture_v1` (états, issue, phrases, libellés, (i-a), audit R4, gardes), `t07bbis.conjointe_v1`,
`t07bbis.registre_bbis_v1` et du script `scripts/enumerer_issues_bbis_v1.py` (B bis, « Critères de lecture gelés », « Liste
d'arrêt », « Épreuves » : antériorité de `SCELLEMENT-BBIS` sur `lecture-t07.json` (cas sain, artefact) ; clé de B bis dans
`registres/scellements-v1.md` (refus) ; arrêt au cumul plus un quart d'heure ; énumération des grilles)."""
from __future__ import annotations

import importlib.util
import os
import re
import subprocess
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t07bbis import conjointe_v1 as cj
from controle_ia.t07bbis import lecture_v1 as lv
from controle_ia.t07bbis import registre_bbis_v1 as rb

RACINE = Path(__file__).resolve().parents[1]
DOSES = ("S25", "S50", "S75", "S100")


def _script():
    spec = importlib.util.spec_from_file_location("enum_bbis", RACINE / "scripts" / "enumerer_issues_bbis_v1.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_enumeration_grilles_a_b_c_sans_trou_ni_chevauchement():
    m = _script()
    a2, a1 = m.grille_a("(ii)"), m.grille_a("(i-a)")
    assert a2["combinaisons"] == 4374 and a1["combinaisons"] == 486
    b = m.grille_b()
    assert b["paires"] == 16777216 and b["classes_I_suffixe"] == 28 and b["libelles"]["dure_sans_lettre"] == 0
    c = m.grille_c()
    assert c["combinaisons_ii"] == 3 * 25 ** 4 and c["combinaisons_ia"] == 18
    p = m.phrases_28()
    assert len(p) == 28 and len({(x["I"], x["T"]) for x in p}) == 28
    assert not any(re.search(r"\{[a-z_]+\}", x["phrase"]) for x in p)


def _ok(**k):
    d = {"au_dessus": True, "passe": True, "aire": 0.8, "Q": 0.6, "bas_echelle_aire": 0.62, "haut_echelle_aire": 0.9,
         "difference": 0.1, "bas": 0.02, "haut": 0.2, "contraire": False, "quantile_nul": 0.53, "bas_sonde": 0.45}
    d.update(k)
    return d


def _cellule(etat_vise, famille="(ii)", dose=0.5, **lignes):
    r = {"famille": famille, "dose": dose, "positifs": "S50", "D": _ok(), "R": _ok(), "triviaux": {"pas": {"separation": 0.55}},
         "MC": _ok(aire_b=0.66), "LEX": _ok(), "ENC": _ok(), "TE": _ok(), "DD": _ok(), "MU": _ok(au_dessus=False),
         "ART": _ok(deplacement=False), "RF": _ok(au_dessus=False), "SC": _ok()}
    if etat_vise == "E3":
        r["LEX"] = _ok(au_dessus=False)
    if etat_vise == "E5":
        r["DD"] = _ok(au_dessus=False)
    r.update(lignes)
    r["etat"] = lv.etat_cellule(r)
    return r


def test_etats_d_une_cellule_et_ordre():
    assert _cellule("E6")["etat"]["etat"] == "E6"
    assert _cellule("E3")["etat"] == {"etat": "E3", "lecteur": "LEX", "motif": None}
    assert lv.etat_cellule({**_cellule("E6"), "R": {"non_calculable": "x"}})["etat"] == "E0"
    assert lv.etat_cellule({**_cellule("E6"), "D": _ok(au_dessus=False)})["etat"] == "E1"
    assert lv.etat_cellule({**_cellule("E6"), "R": _ok(passe=False)})["etat"] == "E1b"
    assert lv.etat_cellule({**_cellule("E6"), "triviaux": {"jetons_notes": {"separation": 0.8}}})["etat"] == "E2"
    assert lv.etat_cellule({**_cellule("E6"), "TE": {"non_calculable": "série coupée"}})["etat"] == "E4"
    assert lv.etat_cellule({**_cellule("E6"), "famille": "(i-a)"})["etat"] == "E6′"


def test_issue_libelles_qualifications_et_marque_g3():
    pl = {"S25": _cellule("E3"), "S50": _cellule("E6"), "S75": _cellule("E5"),
          "S100": _cellule("E6", MU=_ok(au_dessus=True, aire=0.7))}
    tr = {d: _cellule("E1", D=_ok(au_dessus=False)) for d in DOSES}
    r = lv.issue_complete(pl, tr, None)
    assert r["I"] == "I6" and r["doses_I"] == ["S50", "S100"] and r["T"] == "T−"
    assert r["libelles"]["lecture_dure"]["doses"] == ["S50"] and r["libelles"]["lettre_R2716"]["doses"] == ["S50", "S75", "S100"]
    assert r["plafond_tient_transfert_echoue"] and r["au_bout_transfert_echoue"]
    assert r["qualifications"]["S100"]["R-MU"] and "s'allume" in r["qualifications"]["S100"]["MU"]
    assert "{" not in r["phrase_I"] + r["phrase_T"]
    g = lv.issue_complete(pl, tr, "A2")
    assert g["phrase_I"].startswith("(ii) non établi comme saboteur (A2) : lecture rapportée sans portée")
    assert lv.issue_complete({d: {"etat": {"etat": "E0"}} for d in DOSES}, tr, None)["I"] == "I0"


def test_lignes_ia_et_reserve_it():
    c = _cellule("E6", famille="(i-a)", TE_instruit=_ok(au_dessus=False), IT=_ok(au_dessus=True))
    s = lv.ligne_i(c)
    assert s.startswith("tient et bat le texte") and "non au-dessus" in s and "R-IT" in s
    assert lv.ligne_i({**c, "etat": {"etat": "E0", "motif": "sonde en échec"}, "IT": None}).startswith("non calculable (sonde")


def test_audit_r4_cas_sain_et_motifs():
    sain = {"P-S50": _cellule("E3"), "P-instruit": _cellule("E3", famille="(i-a)")}
    assert not lv.audit_r4(sain, {}, {})["declenche"]
    trop = {f"P-{d}": _cellule("E6", dose=0.25) for d in DOSES}
    trop["P-instruit"] = _cellule("E6", famille="(i-a)")
    tr = {f"T-{i}": _cellule("E6") for i in range(5)}
    r = lv.audit_r4(trop, tr, {n: (trop["P-instruit"], None) for n in tr})
    assert any(m.startswith("(iii)") for m in r["motifs"])
    haut = {"P-S50": _cellule("E3", D=_ok(aire=0.97, Q=0.75)), "P-instruit": _cellule("E3", famille="(i-a)")}
    haut["P-S50"]["R"] = _ok(quantile_nul=0.65)
    r = lv.audit_r4(haut, {}, {})
    assert {m[:4] for m in r["motifs"]} >= {"(i) ", "(ii)", "(vii"}
    echec = {f"P-{d}": _cellule("E1", dose=(1.0 if d == "S100" else 0.5), D=_ok(au_dessus=False), MC=_ok(aire_b=0.75))
             for d in DOSES}
    echec["P-instruit"] = _cellule("E1", famille="(i-a)", D=_ok(au_dessus=False))
    t = {"T-instruit-S50": _cellule("E3")}
    r = lv.audit_r4(echec, t, {"T-instruit-S50": (echec["P-instruit"], echec["P-S50"])})
    assert any(m.startswith("(v)") for m in r["motifs"]) and any(m.startswith("(vi)") for m in r["motifs"])
    contraire = {"P-S50": _cellule("E1", D=_ok(au_dessus=False, contraire=True))}
    assert any(m.startswith("(iv)") for m in lv.audit_r4(contraire, {}, {})["motifs"])


def test_garde_processeur_et_liste_blanche(monkeypatch, tmp_path):
    monkeypatch.setenv("BBIS_INSTANCE", "1")
    with pytest.raises(GardeArret, match="sur l'instance"):
        lv.exiger_processeur()
    monkeypatch.delenv("BBIS_INSTANCE")
    lv.exiger_processeur()
    g = lv.GardeEntrees(tmp_path, lv.entrees_autorisees("R7B", "RB", {}))
    assert g.exiger("diag/R7B/episodes-t06.json") == tmp_path / "diag/R7B/episodes-t06.json"
    for jamais in ("diag/R7B/lecture-sondes-t06.json", "diag/R7B/resume.json", "donnees/T07/scores-actions-t07.npz",
                   "donnees/bras-attaque-v1/x.json"):
        with pytest.raises(GardeArret, match="Jamais"):
            g.exiger(jamais)
    with pytest.raises(GardeArret, match="liste blanche"):
        g.exiger("diag/R7B/autre.json")


def _git(d, *a, date=None):
    env = dict(os.environ)
    if date:
        env.update({"GIT_COMMITTER_DATE": date, "GIT_AUTHOR_DATE": date})
    subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True, env=env)


def _depot(tmp_path, avant: bool):
    d = tmp_path / ("artefact" if avant else "sain")
    d.mkdir()
    _git(d, "init", "-q", "-b", "main")
    _git(d, "config", "user.email", "essai@example.invalid")
    _git(d, "config", "user.name", "essai")
    (d / "registres").mkdir()
    reg = d / rb.REGISTRE_PROPRE
    reg.write_text("# registre\n", encoding="utf-8")
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "init", date="2026-11-14T10:00:00Z")

    def lecture(date):
        (d / "diag" / "run-t07").mkdir(parents=True, exist_ok=True)
        (d / "diag" / "run-t07" / "lecture-t07.json").write_text("{}", encoding="utf-8")
        _git(d, "add", "-A")
        _git(d, "commit", "-q", "-m", "lecture B", date=date)

    if avant:
        lecture("2026-11-14T11:00:00Z")
    rb.ajouter_ligne_propre(d, rb.REGISTRE_PROPRE, "SCELLEMENT-BBIS", 1789000000, "prereg/T0.7-etape-B-bis-v1.md", "a" * 64)
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "scellement", date="2026-11-14T12:00:00Z")
    if not avant:
        lecture("2026-11-15T12:00:00Z")
    return d


def test_anteriorite_du_scellement_sur_lecture_t07_sain_et_artefact(tmp_path):
    r = lv.anteriorite_etape_b(_depot(tmp_path, False), rb.REGISTRE_PROPRE)
    assert r["premiers_ajouts"] and r["premiers_ajouts"][0]["instant"] > r["instant_scellement"]
    with pytest.raises(lv.RefusLecture, match="étape B exécutée avant le scellement"):
        lv.anteriorite_etape_b(_depot(tmp_path, True), rb.REGISTRE_PROPRE)


def test_registre_propre_et_refus_du_registre_partage(tmp_path):
    l = rb.ajouter_ligne_propre(tmp_path, rb.REGISTRE_PROPRE, "CODE-BBIS", 1789000000, "docs/x.json", "b" * 64)
    assert l.startswith("| CODE-BBIS | 2026-")
    with pytest.raises(GardeArret, match="déjà présente"):
        rb.ajouter_ligne_propre(tmp_path, rb.REGISTRE_PROPRE, "CODE-BBIS", 1789000001, "docs/x.json", "b" * 64)
    with pytest.raises(GardeArret, match="scellements-v1.md"):
        rb.ajouter_ligne_propre(tmp_path, rb.REGISTRE_PARTAGE, "SCORES-BBIS", 1789000000, "diag/x.json", "c" * 64)
    with pytest.raises(GardeArret, match="hors des clés"):
        rb.ajouter_ligne_propre(tmp_path, rb.REGISTRE_PROPRE, "SCORES-T07", 1789000000, "diag/x.json", "c" * 64)
    partage = tmp_path / rb.REGISTRE_PARTAGE
    partage.write_text("| RUN-CONFIRMATION-T06 | 2026-11-12T05:00:00Z | runs/x/manifeste.json | " + "d" * 64 + " |\n",
                       encoding="utf-8")
    rb.exiger_partage_sans_bbis(partage)
    with open(partage, "a", encoding="utf-8") as f:
        f.write("| SCELLEMENT-BBIS | 2026-11-16T05:00:00Z | prereg/x.md | " + "e" * 64 + " |\n")
    with pytest.raises(GardeArret, match="la garde de T0.7"):
        rb.exiger_partage_sans_bbis(partage)


def test_garde_de_depense_au_cumul_plus_un_quart_d_heure():
    assert rb.garde_depense(30.0, 2.0)["projete"] == 30.5
    with pytest.raises(GardeArret, match="destruction par identifiant"):
        rb.garde_depense(39.0, 2.0)
    with pytest.raises(GardeArret, match="coupure"):
        rb.garde_depense(39.5, 0.0)


def test_garde_d_offre_et_de_creation(tmp_path):
    offre = {"carte": "A100 SXM4 80GB", "coeurs": 32, "memoire_vive_mo": 256000, "disque_go": 200, "stockage_usd_h": 0.05,
             "etiquette": "bbis-t07-v1"}
    rb.exiger_offre(offre)
    for faute in ({"carte": "H200 SXM 141GB"}, {"disque_go": 100}, {"etiquette": "t07-x"}, {"stockage_usd_h": 0.2}):
        with pytest.raises(GardeArret, match="hors des bornes"):
            rb.exiger_offre({**offre, **faute})
    t = 1789700000
    with pytest.raises(GardeArret, match="absente"):
        rb.exiger_creation(tmp_path, "feu GO-2026-11-14-09", t)
    for k in ("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS"):
        rb.ajouter_ligne_propre(tmp_path, rb.REGISTRE_PROPRE, k, t - 100, "x", "f" * 64)
    assert rb.exiger_creation(tmp_path, "feu de la mère : GO-2026-11-14-09", 1795003200)["relances"] == 0
    with pytest.raises(GardeArret, match="feu écrit"):
        rb.exiger_creation(tmp_path, "feu sans numéro", 1795003200)
    with pytest.raises(GardeArret, match="seconde relance"):
        rb.exiger_creation(tmp_path, "GO-2026-11-14-09", 1795003200, relances=2)
    with pytest.raises(GardeArret, match="21 novembre"):
        rb.exiger_creation(tmp_path, "GO-2026-11-14-09", 1795262401, relances=1)


def test_table_conjointe_variantes_et_ia():
    etats = {"S50": "E6", "S75": "E5"}
    mus = {"S50": lv.MU_MUETTE, "S75": lv.MU_MUETTE}
    t = cj.table_famille("(ii)", "U", "L2", "complet", etats, mus, ["S50", "S75"])
    assert t["variantes"][cj.RETENUE]["C"] == "C2" and t["variantes"][cj.INFORMATION]["C"] == "C1"
    assert t["variantes"][cj.INFORMATION]["phrase"].endswith("(aux doses en E5, l'artefact d'adaptateur n'est pas écarté : R-ART).")
    assert cj.table_famille("(ii)", "Z", "L3", "complet", etats, mus, [])["variantes"][cj.RETENUE]["C"] == "C0"
    assert cj.table_famille("(ii)", None, "L1", "illisible", etats, mus, ["S50"])["B"] == "B0"
    ia = cj.table_famille("(i-a)", "Z", "L3", "complet", etat_ia="E6′")
    assert ia["variantes"][cj.RETENUE]["C"] == "C4" and "à texte égal" not in ia["variantes"][cj.RETENUE]["phrase"]
    for code in cj.PHRASES_C:
        assert "meilleur des deux" not in cj.PHRASES_C[code]
