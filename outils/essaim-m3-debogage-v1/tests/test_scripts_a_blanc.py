# -*- coding: utf-8 -*-
"""Les trois scripts corrigés tournent de bout en bout à blanc (aucun réseau, aucune dépense) et leurs comptes sont
cohérents : chaque appel est dans le journal, les statuts somment au nombre d'appels, rien n'est nommé « certifié »."""
import json
from pathlib import Path

import pytest

import run_1_decouverte_eval_awareness_v2 as s1
import run_2_generation2_failles_orthogonales_v2 as s2
import run_3_pascal_finesse_ab_v2 as s3

SUBSTRAT_MINI = {
    "PRIMORDIAL_MITOSIS_DONE_CACHE": {"castes": [
        {"mode": "MONOCULTURE", "lineages": ["GEMINI_ARGON"], "temp": 0.53, "focus": "a"},
        {"mode": "HYBRIDE", "lineages": ["CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"], "temp": 0.325, "focus": "b"},
        {"mode": "MONOCULTURE", "lineages": ["CLAUDE_OPUS_5_5"], "temp": 0.735, "focus": "c"}]},
    "custom_swarm_memory_store": {"novel_beyond_labs_flaws_eliminated": ["Rupture de rôle et refus d'audit (Agent #324)",
                                                                           "autre faille"]},
    "evolved_architecture_spec": "Description de l'architecture (non auditée).",
}


def _dossier(tmp_path: Path) -> Path:
    d = tmp_path / "d17"
    d.mkdir()
    (d / "SUBSTRAT_BRUT_CONNAISSANCES_INTER_GENERATIONS.json").write_text(
        json.dumps(SUBSTRAT_MINI, ensure_ascii=False), encoding="utf-8")
    return d


def _verifier_run(dossier: Path, nom: str, fichiers_attendus: list) -> dict:
    run = dossier / "runs_debogage" / nom
    resume = json.loads((run / "resume_run.json").read_text(encoding="utf-8"))
    journal = [json.loads(l) for l in (run / "journal_appels.jsonl").read_text(encoding="utf-8").splitlines()]
    assert resume["budget"]["appels"] == len(journal), "chaque appel réservé est dans le journal"
    r = resume["reponses"]
    assert r["ok"] + r["vide"] + r["echec_api"] == r["n"] == len(journal)
    assert all(e["modele_servi"] is None for e in journal if e["statut"] == "echec_api")
    for f in fichiers_attendus:
        assert (run / f).exists(), f
        assert (run / (f + ".sha256")).exists(), "empreinte compagnon (R6)"
    assert not any("CERTIF" in p.name.upper() for p in run.iterdir())
    return resume


@pytest.mark.parametrize("module, nom, argv, fichiers", [
    (s1, "r1", ["--n-castes-moisson", "4", "--n-castes-decouverte", "6", "--n-sondes-ecart", "2"],
     ["rapport_decouverte_eval_awareness.md", "extraction_m1.json"]),
    (s2, "r2", ["--n-castes", "6", "--n-sondes-ecart", "2"], ["rapport_generation2.md", "extraction_m1.json"]),
    (s3, "r3", ["--n-castes", "6", "--n-sondes-ecart", "2", "--n-par-bras", "6"],
     ["rapport_pascal_finesse_abc.md", "resultats_abc.json"]),
])
def test_script_a_blanc_bout_en_bout(tmp_path, module, nom, argv, fichiers):
    dossier = _dossier(tmp_path)
    code = module.main(["--a-blanc", "--dossier", str(dossier), "--nom-run", nom, "--max-appels", "300", "--graine", "5"] + argv)
    assert code == 0
    resume = _verifier_run(dossier, nom, fichiers)
    assert resume["arret"] is None
    substrat = json.loads((dossier / "SUBSTRAT_BRUT_CONNAISSANCES_INTER_GENERATIONS.json").read_text(encoding="utf-8"))
    hist = substrat["custom_swarm_memory_store"]["historique_runs_debogage"]
    assert hist[-1]["run"] == nom and hist[-1]["a_blanc"] is True
    assert any(p.name.endswith(".secours.json") for p in dossier.iterdir()), "copie de secours du substrat"


def test_plafond_arrete_le_script_proprement(tmp_path):
    dossier = _dossier(tmp_path)
    code = s3.main(["--a-blanc", "--dossier", str(dossier), "--nom-run", "plafond", "--max-appels", "5", "--graine", "5",
                    "--n-castes", "6", "--n-sondes-ecart", "2", "--n-par-bras", "3"])
    assert code == 3
    resume = _verifier_run(dossier, "plafond", [])
    assert resume["arret"] and "plafond" in resume["arret"] and resume["budget"]["appels"] == 5


def test_refus_d_ecraser_un_run_existant(tmp_path):
    dossier = _dossier(tmp_path)
    assert s2.main(["--a-blanc", "--dossier", str(dossier), "--nom-run", "x", "--n-castes", "3", "--n-sondes-ecart", "1"]) == 0
    import m3_commun as m3
    with pytest.raises(m3.ErreurEssaim):
        s2.main(["--a-blanc", "--dossier", str(dossier), "--nom-run", "x", "--n-castes", "3", "--n-sondes-ecart", "1"])


def test_resultats_abc_ont_trois_bras_et_taux_sur_ok(tmp_path):
    dossier = _dossier(tmp_path)
    assert s3.main(["--a-blanc", "--dossier", str(dossier), "--nom-run", "abc", "--graine", "9", "--n-castes", "3",
                    "--n-sondes-ecart", "1", "--n-par-bras", "9"]) == 0
    res = json.loads((dossier / "runs_debogage" / "abc" / "resultats_abc.json").read_text(encoding="utf-8"))
    assert set(res["resumes"]) == {"A_coercitif", "B_maieutique", "C_neutre"}
    for r in res["resumes"].values():
        assert r["n_appels"] == 9 and r["n_ok"] + r["n_vide"] + r["n_echec_api"] == 9
        if r["n_ok"] == 0:
            assert r["cooperation_pct_sur_ok"] is None
    assert res["statut_scientifique"].startswith("exploratoire")
