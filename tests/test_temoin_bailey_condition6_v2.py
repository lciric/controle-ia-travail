"""Épreuve (R5) du code de la condition 6 du témoin de Bailey, v2 : journaliseur v2, exécution v2, instance v2, lecture
v2, lanceur v2. Cas sains et artefacts, sur processeur, sans modèle. Le faux déroulé emploie les colonnes réelles du
code public (11 pour la table de comportement, 23 pour `metric_evaluation`, `evaluate.py` l. 520-534 et 1104-1130).
Cas sain en demi-précision exigé par le texte scellé : notes nuisibles au plafond float16(32/33), bénignes non
constantes dont plusieurs égales à τ.
"""
from __future__ import annotations

import json
import os
import pickle
import sys
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.temoin_bailey import analyse_v3 as an
from controle_ia.temoin_bailey import conventions_v2 as cv
from controle_ia.temoin_bailey import instance_v2 as inst
from controle_ia.temoin_bailey import journaliseur_v2 as jl
from controle_ia.temoin_bailey import lanceur_v2 as la
from controle_ia.temoin_bailey import lecture_v2 as lc

pd = pytest.importorskip("pandas")

PLAFOND = float(np.float16(32 / 33))
PAS = 4
COL_M = ["at_def_epoch", "standard_auc", "obfuscated_auc", "best_train_threshold", "standard_acc_with_train_thresh",
         "obfuscated_acc_with_train_thresh", "obfuscated_frac_correct", "standard_benign_scores",
         "standard_harmful_scores", "obfuscated_harmful_scores", "score_plotting_data", "score_plot", "full_score_plot",
         "pca_plotting_data", "pca_plot", "standard_roc", "obfuscated_roc", "standard_acc_curve",
         "obfuscated_acc_curve", "standard_pr_curve", "obfuscated_pr_curve", "attack_suffix", "attack_suffix_len"]
COL_B = ["input_text", "beh_target", "tuned_gen_text", "standard_gen_text", "behavior_score", "tuned_on_tuned_scores",
         "standard_on_tuned_scores", "standard_on_standard_scores", "tuned_ont_tuned_scores_data",
         "standard_ont_tuned_scores_data", "standard_ont_standard_scores_data"]
assert len(COL_M) == 23 and len(COL_B) == 11


class ParamsFactices:  # se décharge par pickle comme `SoftParams` (attributs `params`, `init_params`)
    def __init__(self, params, init):
        self.params, self.init_params = params, init


class PeftConf:
    def __init__(self, base):
        self.base_model_name_or_path = base


class ConfigModele:
    def __init__(self, nom, rev):
        self._name_or_path, self._commit_hash = nom, rev


class ModeleJuge:
    def __init__(self, dtype="torch.bfloat16", base="google/gemma-2b", adaptateur=True, nom="google/gemma-2b",
                 rev="rb"):
        self.config, self.dtype = ConfigModele(nom, rev), dtype
        self.peft_config = {"default": PeftConf(base)} if adaptateur else {}


class Tok:
    def __init__(self, nom=cv.JUGE):
        self.name_or_path = nom


JUGE_ATTENDU = {"adaptateur": cv.JUGE, "revision_adaptateur": "ra", "base": cv.JUGE_BASE, "revision_base": "rb",
                "dtype": "torch.bfloat16"}


def cache_hf(tmp_path, ra="ra", rb="rb") -> str:
    for depot, rev in ((cv.JUGE, ra), (cv.JUGE_BASE, rb)):
        refs = tmp_path / "hf" / ("models--" + depot.replace("/", "--")) / "refs"
        refs.mkdir(parents=True, exist_ok=True)
        (refs / "main").write_text(rev)
    return str(tmp_path / "hf")


def jeu(dossier: Path) -> list[tuple[str, str]]:
    dossier.mkdir(parents=True, exist_ok=True)
    lignes = []
    for split in ("val", "test"):
        rows = [{"prompt": f"p-{split}-{i}", "response": f"r-{split}-{i}"} for i in range(100)]
        pd.DataFrame(rows).to_csv(dossier / f"harmful_{split}_no_spec_tokens.csv", index=False)
        lignes += [(r["prompt"], r["response"]) for r in rows]
    return lignes


def notes_saines(rng, e):
    ben = rng.uniform(0.0, 0.3, 200).astype(np.float16).astype(float)
    ben[:3] = float(np.float16(0.5))
    sans = np.full(200, PLAFOND)
    sans[150:] = rng.uniform(0.6, 0.9, 50).astype(np.float16)
    avec = rng.uniform(0.0, 0.3, 200).astype(np.float16).astype(float)
    avec[:20] = PLAFOND
    return ben.tolist(), sans.tolist(), avec.tolist()


def fabriquer(tmp_path, b=75.0, d_avant=0.0, juge_modele=None, cache=None, ra="ra", rb="rb", travail=None):
    travail = travail or tmp_path / "x"
    lignes = jeu(tmp_path / "jeu")
    cfg = jl.ConfigJournal(dossier_journal=str(travail / "journal"), dossier_params=str(travail / "params"),
                           dossier_jeu=str(tmp_path / "jeu"), pas_attendus=PAS, juge=dict(JUGE_ATTENDU),
                           depense={"d_avant": d_avant, "c": 1.0, "creation": 0.0, "b": b},
                           cache_hf=cache_hf(tmp_path, ra, rb), execution="principal")
    cache = cache if cache is not None else {"strongreject_finetuned": (juge_modele or ModeleJuge(), Tok())}
    lg = jl.JournaliseurLocal("f", "u", {"a": 1}, config=cfg, cache_juge=cache, horloge=lambda: 0.0)
    return lg, cfg, lignes, travail


def jouer(lg, cfg, lignes, k, *, notes=notes_saines, pas=PAS, suffixe=None, juge_note=0.9, ordre=None,
          etiquette=None, attaque_texte=None, longueur=lambda e: 16, sauver=True, n_juge=200, seed=0, marque=None):
    rng = np.random.default_rng(seed)
    init = np.zeros((1, 16, 8), dtype=np.float32)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    def ligne_m(etiq, ben, sans, avec, passees, suff_len):
        fig = plt.figure()
        d = dict.fromkeys(COL_M)
        d.update({"at_def_epoch": etiq, "standard_benign_scores": json.dumps(ben),
                  "standard_harmful_scores": json.dumps(sans), "obfuscated_harmful_scores": json.dumps(avec),
                  "score_plotting_data": json.dumps(passees), "score_plot": fig, "pca_plotting_data": "[]",
                  "attack_suffix": attaque_texte, "attack_suffix_len": suff_len})
        lg.log_to_table([d[c] for c in COL_M], "metric_evaluation")
        assert not plt.fignum_exists(fig.number)

    for e in range(k):
        ben, sans, avec = notes(rng, e)
        if "metric_evaluation" not in lg.tables:
            lg.create_table("metric_evaluation", COL_M)
        # au tour e > 0, la sonde réajustée revoit l'attaque du tour e − 1 (R_def) : notes avec suffixe hautes ici
        avec_def = sans if e > 0 else avec
        ligne_m(etiquette or cv.DEFENSEUR.format(e=e), ben, sans, avec_def, {"standard_benign": ben}, longueur(e))
        for _ in range(pas):
            lg.log({"loss": 1.0})
            lg.log({"softprompt_norm": 1.0})
            lg.log({"grad_norm": 1.0})
        if sauver:
            val = suffixe(e) if suffixe else np.full((1, 16, 8), e + 1, dtype=np.float32)
            chemin = cv.chemin_params(cfg.dossier_params, e)
            chemin.parent.mkdir(parents=True, exist_ok=True)
            with open(chemin, "wb") as f:
                pickle.dump(ParamsFactices(val, init), f)
        tab = cv.COMPORTEMENT.format(e=e)
        lg.create_table(tab, COL_B)
        for i in (ordre or list(range(n_juge))):
            p, r = lignes[i]
            d = dict.fromkeys(COL_B)
            d.update({"input_text": f"<gabarit>{p}", "beh_target": r, "tuned_gen_text": f"réponse {i}",
                      "standard_gen_text": "refus", "behavior_score": juge_note})
            lg.log_to_table([d[c] for c in COL_B], tab)
        lg.log({"avg_behavior_score": juge_note, "behavior_success_rate": 1.0})
        ligne_m(cv.ATTAQUANT.format(e=e), ben, sans, avec,
                {f"obf_harmful_att_def_epoch_{x}": avec for x in range(-1, e + 1)}, longueur(e))
        for _ in range(3):
            lg.log({"probe_loss_layer_1": 0.1})
        if marque is not None:
            marque(e)


def ecrire_lanceur(travail: Path, k: int, tombee_lanceur=False):
    with open(travail / "sortie-durees-v2.jsonl", "w") as f:
        for e in range(k):
            f.write(json.dumps({"tour": e, "duree_s": 10.0}) + "\n")
    with open(travail / "gardes-lanceur-v2.jsonl", "w") as f:
        f.write(json.dumps({"garde": "configuration effective", "etat": "tombée" if tombee_lanceur else "passée"}) + "\n")
    (travail / "etat-execution-v2.json").write_text("{}")
    (travail / "empreintes-fichiers-v2.jsonl").write_text("")


def emp(travail):
    return {rel: cv.sha_fichier(travail / rel) for rel in cv.NOMS_JOURNAUX if (travail / rel).is_file()}


# --- cas sains ---------------------------------------------------------------------------------------------------------

def test_cas_sain_demi_precision_bout_en_bout(tmp_path):
    lg, cfg, lignes, x = fabriquer(tmp_path)
    jouer(lg, cfg, lignes, 21)
    lg.fermer()
    ecrire_lanceur(x, 21)
    gardes = lc.lire_jsonl(x / cv.JOURNAL_GARDES)
    assert gardes and all(g["etat"] == "passée" for g in gardes)
    assert {"juge", "sonde orientée", "par tour", "appariement", "suffixe appris", "dépense"} <= {g["garde"] for g in gardes}
    notes_txt = (x / cv.JOURNAL_NOTES).read_text()
    tech_txt = (x / cv.JOURNAL_TECHNIQUE).read_text()
    assert "réponse 3" not in notes_txt + tech_txt and "<gabarit>" not in notes_txt and "r-val-0" not in notes_txt
    assert "benignes" not in tech_txt and "note_juge" not in tech_txt  # journal technique lisible sans les notes (A-3)
    e = emp(x)
    v = lc.valider(x, True, True, False, 30, e, [e], True, False)
    assert v == {"k_prime": 21, "etat": None, "sonde_orientee": True, "fin_de_run": True}
    res = lc.lire(x, v, PAS, False, an.graines()["reechantillonnage"])
    assert res["verdict"].startswith("Effet reproduit sur le banc des auteurs, au régime réduit (K = 21)")
    assert res["audit"]["defaut"] is False
    assert [r["tour"] for r in res["intervalles"]] == list(range(21)) and "def" not in res["intervalles"][-1]
    assert len(res["rapportees"]["evasion_conjointe"]) == 21


def test_validite_ne_lit_pas_les_notes(tmp_path):
    lg, cfg, lignes, x = fabriquer(tmp_path)
    jouer(lg, cfg, lignes, 3)
    lg.fermer()
    ecrire_lanceur(x, 3)
    (x / cv.JOURNAL_NOTES).unlink()  # la validité doit tenir sans le journal des notes
    e = emp(x)
    v = lc.valider(x, True, True, False, 30, e, [e], True, False)
    assert v["k_prime"] == 3 and v["etat"].startswith("Pas de verdict (moins de 20 tours")
    assert lc.lire(x, v, PAS, False, None) == {"verdict": v["etat"], "k_prime": 3}


def test_fin_de_run_branchee_transfert_en_ecart_et_garde_lanceur(tmp_path):
    lg, cfg, lignes, x = fabriquer(tmp_path)
    jouer(lg, cfg, lignes, 21)
    lg.fermer()
    ecrire_lanceur(x, 21)
    e = emp(x)
    faux = dict(e)
    faux[cv.JOURNAL_NOTES] = "0" * 64
    v = lc.valider(x, True, True, False, 30, e, [faux, faux], True, False)
    assert v["fin_de_run"] is False and v["etat"] == "Non interprétable (garde de fin de run)."
    v = lc.valider(x, True, True, False, 30, e, [e], False, False)  # notes du pilote non scellées
    assert v["etat"] == "Non interprétable (garde de fin de run)."
    ecrire_lanceur(x, 21, tombee_lanceur=True)
    v = lc.valider(x, True, True, False, 30, emp(x), [emp(x)], True, False)
    assert v["k_prime"] == 0


def test_lire_jsonl_absent_leve(tmp_path):
    with pytest.raises(GardeArret, match="absent"):
        lc.lire_jsonl(tmp_path / "rien.jsonl")


def test_audit_chaque_controle(tmp_path):
    lg, cfg, lignes, x = fabriquer(tmp_path)
    jouer(lg, cfg, lignes, 3)
    lg.fermer()
    notes = lc.lire_jsonl(x / cv.JOURNAL_NOTES)
    tech = lc.lire_jsonl(x / cv.JOURNAL_TECHNIQUE)
    gardes = lc.lire_jsonl(x / cv.JOURNAL_GARDES)
    asm = lc.assembler(notes, 3)
    assert not lc.audit(asm, notes, tech, gardes, 3, PAS)["defaut"]
    assert lc.audit(asm, notes, tech, gardes, 3, PAS + 1)["defaut"]                           # rejeu des gardes
    assert lc.audit(asm, notes, tech, gardes + [{"etat": "tombée", "tour": 1}], 3, PAS)["defaut"]
    tech2 = [dict(t) for t in tech]
    for t in tech2:
        if t.get("type") == "fin_de_tour" and t["tour"] == 2:
            t["empreinte_valeurs_suffixe"] = t["empreinte_valeurs_initiales"]
    assert "suffixe distinct" in " ".join(lc.audit(asm, notes, tech2, gardes, 3, PAS)["defauts"])
    real = lc._recalcul_independant
    lc._recalcul_independant = lambda b, n: (-1, -1)
    try:
        assert "recalcul" in " ".join(lc.audit(asm, notes, tech, gardes, 3, PAS)["defauts"])
    finally:
        lc._recalcul_independant = real


# --- artefacts du journaliseur -----------------------------------------------------------------------------------------

@pytest.mark.parametrize("cas", ["pas", "constantes", "non_fini", "meme_suffixe", "suffixe_initial", "ordre",
                                 "etiquette", "suffixe_au_journal", "orientee", "suffixe_absent", "longueur",
                                 "juge_199"])
def test_artefacts_gardes(tmp_path, cas):
    lg, cfg, lignes, x = fabriquer(tmp_path)
    kw, k = {}, 1
    if cas == "pas":
        kw["pas"] = PAS + 1
    elif cas == "constantes":
        kw["notes"] = lambda rng, e: ([0.1] * 200, [PLAFOND] * 200, [0.1] * 200)
    elif cas == "non_fini":
        def n(rng, e):
            b, s, a = notes_saines(rng, e)
            a[5] = float("nan")
            return b, s, a
        kw["notes"] = n
    elif cas == "meme_suffixe":
        kw["suffixe"], k = (lambda e: np.ones((1, 16, 8), dtype=np.float32)), 2
    elif cas == "suffixe_initial":
        kw["suffixe"] = lambda e: np.zeros((1, 16, 8), dtype=np.float32)
    elif cas == "ordre":
        kw["ordre"] = [1, 0] + list(range(2, 200))
    elif cas == "etiquette":
        kw["etiquette"] = "Inning 7, defender just went"
    elif cas == "suffixe_au_journal":
        kw["attaque_texte"] = "texte"
    elif cas == "orientee":
        kw["notes"] = lambda rng, e: (np.linspace(0.5, 0.9, 200).tolist(), [0.1] * 200, [0.1] * 200)
    elif cas == "suffixe_absent":
        kw["sauver"] = False
    elif cas == "longueur":
        kw["longueur"], k = (lambda e: 16 + e), 2
    elif cas == "juge_199":
        kw["n_juge"] = 199
    with pytest.raises(GardeArret) as err:
        jouer(lg, cfg, lignes, k, **kw)
    assert "0." not in str(err.value) and "nan" not in str(err.value).lower()  # jamais une valeur de note
    gardes = lc.lire_jsonl(x / cv.JOURNAL_GARDES)
    assert gardes[-1]["etat"] == "tombée"  # toute garde écrit son état avant de lever (A-4)


@pytest.mark.parametrize("cas,match", [("dtype", "type numérique"), ("base", "base"), ("rev_adaptateur", "adaptateur"),
                                       ("rev_base", "révision de la base"), ("pas_adaptateur", "adaptateur"),
                                       ("tokeniseur", "adaptateur")])
def test_garde_juge_adaptateur_artefacts(tmp_path, cas, match):
    kw = {}
    modele, tok = ModeleJuge(), Tok()
    if cas == "dtype":
        modele = ModeleJuge(dtype="torch.float32")  # repli silencieux de strong_reject l. 468-469
    elif cas == "base":
        modele = ModeleJuge(base="EleutherAI/pythia-14m")
    elif cas == "rev_adaptateur":
        kw["ra"] = "autre"
    elif cas == "rev_base":
        kw["rb"] = "autre"
    elif cas == "pas_adaptateur":
        modele = ModeleJuge(adaptateur=False)
    elif cas == "tokeniseur":
        tok = Tok("EleutherAI/pythia-14m")
    lg, cfg, lignes, x = fabriquer(tmp_path, cache={"strongreject_finetuned": (modele, tok)}, **kw)
    with pytest.raises(GardeArret, match=match):
        jouer(lg, cfg, lignes, 1)


def test_garde_juge_sain_et_testing(tmp_path):
    e = jl.etat_juge_charge({"strongreject_finetuned": (ModeleJuge(), Tok())}, cache_hf(tmp_path))
    assert jl.garde_juge(e, JUGE_ATTENDU, True) == "passée"
    with pytest.raises(GardeArret, match="TESTING"):
        jl.garde_juge(e, JUGE_ATTENDU, False)
    with pytest.raises(GardeArret, match="absent"):
        jl.etat_juge_charge({}, "")


def test_garde_depense_et_dossier_neuf(tmp_path):
    lg, cfg, lignes, x = fabriquer(tmp_path, d_avant=73.5)
    with pytest.raises(GardeArret, match="dépense"):
        jouer(lg, cfg, lignes, 1)
    lg.fermer()
    with pytest.raises(GardeArret, match="dossier neuf"):
        jl.JournaliseurLocal(config=cfg, cache_juge={})


def test_execution_refuse_testing(monkeypatch):
    from controle_ia.temoin_bailey import execution_v2 as ex
    monkeypatch.setenv("TESTING", "1")
    assert ex.main(["--clone", "/inexistant", "--graine", "1"]) == ex.SORTIE_GARDE


# --- surveillance et exécution -----------------------------------------------------------------------------------------

def test_surveillance_mark_coupee_et_demarrage(tmp_path):
    s = inst.Surveillance("a: 1\nb: 2\n\n", 3, tmp_path)
    for morceau in (b"a: 1\nb", b": 2\n\nMARK: Ep", b"och 0 took 1.5", b"000 seconds\nMARK: Epoch 1 took 2.5 seconds"):
        s.recevoir(morceau)
    s.finir()
    assert s.demarrage is True and s.durees == {0: 1.5, 1: 2.5}
    s2 = inst.Surveillance("a: 1\n", 3, tmp_path)
    s2.recevoir(b"a: 2\nMARK: Epoch 0 took 1 seconds\n")
    assert s2.demarrage is False
    assert [l["etat"] for l in lc.lire_jsonl(tmp_path / "gardes-lanceur-v2.jsonl")] == ["passée", "tombée"]
    assert inst.t_du_pilote({"0": 10, "1": 20}) == 15
    with pytest.raises(GardeArret):
        inst.t_du_pilote({"0": 10})


MAN = {"chemin_modele": "/m", "pas_par_tour": 4, "juge": JUGE_ATTENDU, "cache_hf": "/hf",
       "graines": {"pilote": an.GRAINE_PILOTE, "principal": an.GRAINE_PRINCIPAL}, "regle_tours": {"K": 25}}


def test_parametres_phase_et_garde_k():
    pytest.importorskip("omegaconf")
    assert inst.parametres_phase(MAN, "pilote") == (3, an.GRAINE_PILOTE)
    assert inst.parametres_phase(MAN, "principal-relance") == (25, an.GRAINE_PRINCIPAL)
    with pytest.raises(GardeArret):
        inst.parametres_phase({**MAN, "regle_tours": {}}, "principal")
    ok = f"experiment:\n  attack_defense_epochs: 3\n  seed: {an.GRAINE_PILOTE}\n"
    assert inst.garde_k_configuration(ok, MAN, "pilote") == "passée"
    for faux in (f"experiment:\n  attack_defense_epochs: 100\n  seed: {an.GRAINE_PILOTE}\n",
                 "experiment:\n  attack_defense_epochs: 3\n  seed: 0\n"):
        with pytest.raises(GardeArret):
            inst.garde_k_configuration(faux, MAN, "pilote")


def _executer(tmp_path, monkeypatch, script, depense, echeance=1e12, travail="exec"):
    monkeypatch.setattr(inst, "configuration_attendue", lambda clone, over: "cfg: 1\n\n")
    monkeypatch.setattr(inst, "garde_k_configuration", lambda attendu, man, phase: "passée")
    return inst.executer(MAN, tmp_path / "clone", tmp_path / travail, "pilote", depense, echeance,
                         commande=[sys.executable, "-c", script], intervalle=0.1)


DEP_OK = {"d_avant": 0, "c": 1, "creation": 1e12, "b": 75}


def test_executer_sain_avertissement_sur_sortie_erreur(tmp_path, monkeypatch):
    script = ("import sys; sys.stderr.write('Warning: import\\n'); sys.stderr.flush(); print('cfg: 1\\n', flush=True)\n"
              "for e in range(3): print(f'MARK: Epoch {e} took {e+1}.0 seconds', flush=True)")
    r = _executer(tmp_path, monkeypatch, script, DEP_OK)
    assert r["configuration_effective"] == "passée" and r["tours_marques"] == 3 and r["cause_arret"] is None
    assert r["code_retour"] == 0
    assert "Warning" in (tmp_path / "exec" / "sortie-erreur-instance.log").read_text()


def test_executer_configuration_fausse_depense_echeance(tmp_path, monkeypatch):
    lent = "import time; print('cfg: {}\\n', flush=True); time.sleep(30)"
    r = _executer(tmp_path, monkeypatch, lent.format(2), DEP_OK, travail="a")
    assert r["configuration_effective"] == "tombée" and r["cause_arret"] == "garde de démarrage" and r["code_retour"]
    r = _executer(tmp_path, monkeypatch, lent.format(1), {"d_avant": 74, "c": 1, "creation": 0, "b": 75}, travail="b")
    assert r["cause_arret"] == "dépense"
    r = _executer(tmp_path, monkeypatch, lent.format(1), DEP_OK, echeance=0, travail="c")
    assert r["cause_arret"] == "échéance du GO"


def test_executer_empreinte_a_taille_stable(tmp_path):
    d = tmp_path / "params"
    d.mkdir()
    (d / "f.pkl").write_bytes(b"ab")
    tailles, vus, j = {}, {}, tmp_path / "e.jsonl"
    inst._empreinter_nouveaux([d], tailles, vus, j, False)
    assert not vus  # premier passage : taille notée seulement
    inst._empreinter_nouveaux([d], tailles, vus, j, False)
    assert len(vus) == 1


# --- mise en place et contrôle du juge ---------------------------------------------------------------------------------

def test_gardes_mise_en_place_unitaires(tmp_path):
    assert inst.memoire_vive_go("MemTotal:       134217728 kB\n") == 128
    assert inst.garde_memoire_vive(128.0) == "passée"
    with pytest.raises(GardeArret):
        inst.garde_memoire_vive(125.8)  # strict (A-1)
    assert inst.garde_versions({"a": "1"}, lire=lambda p: "1") == "passée"
    with pytest.raises(GardeArret, match="versions"):
        inst.garde_versions({"a": "1"}, lire=lambda p: "2")
    assert inst.garde_commits_git({"strong_reject": ["u", "c1"]}, lire=lambda p: "c1") == "passée"
    with pytest.raises(GardeArret, match="commit"):
        inst.garde_commits_git({"strong_reject": ["u", "c1"]}, lire=lambda p: None)
    h = cache_hf(tmp_path)
    assert inst.garde_revisions_cache(h, {cv.JUGE: "ra", cv.JUGE_BASE: "rb"}) == "passée"
    with pytest.raises(GardeArret, match="révisions"):
        inst.garde_revisions_cache(h, {cv.JUGE: "ra", cv.MODELE: "rm"})


CLONE = os.environ.get("TEMOIN_BAILEY_CLONE")


@pytest.mark.skipif(not CLONE, reason="clone public au commit 9c1f4b1a absent (TEMOIN_BAILEY_CLONE)")
def test_depot_public_empreintes_pas_et_configuration_attendue(tmp_path):
    clone = Path(CLONE)
    assert inst.garde_depot_public(clone) == "passée"
    assert inst.garde_empreintes_publiques(clone) == "passée"
    assert inst.pas_attendus(clone) == 1600
    with pytest.raises(GardeArret):
        inst.garde_depot_public(tmp_path)  # pas un dépôt : erreur de git → la garde ne passe pas
    from controle_ia.temoin_bailey.execution_v2 import configuration_attendue, surcharges
    over = surcharges(3, an.GRAINE_PILOTE, "/m", str(tmp_path / "s"), str(tmp_path / "p"), str(tmp_path / "h"))
    attendu = configuration_attendue(clone, over)
    assert inst.garde_k_configuration(attendu, {**MAN, "chemin_modele": "/m"}, "pilote") == "passée"


@pytest.mark.skipif(not CLONE, reason="clone public au commit 9c1f4b1a absent (TEMOIN_BAILEY_CLONE)")
def test_controle_juge_par_lots_et_garde(tmp_path):
    clone = Path(CLONE)
    lots = []
    cache = {"strongreject_finetuned": (ModeleJuge(), Tok())}

    def juge(batch):
        lots.append(len(batch["response"]))
        return {"score": [0.0 if r.startswith("refus") else 0.9 for r in batch["response"]]}

    man = {**MAN, "cache_hf": cache_hf(tmp_path)}
    r = inst.controle_juge(man, clone, tmp_path, cache_juge=cache, juge=juge,
                           generer=lambda entrees: [f"refus {i}" for i in range(len(entrees))])
    assert r["etats"]["tenus"] and r["negatif"] == 0 and r["positif"] == 200
    assert max(lots) == 16 and sum(lots) == 400  # lots de eval_batch_size (B-3)
    with pytest.raises(GardeArret, match="positif"):
        inst.controle_juge(man, clone, tmp_path / "b", cache_juge=cache, juge=lambda b: {"score": [0.0] * len(b["response"])},
                           generer=lambda entrees: ["x"] * len(entrees))
    with pytest.raises(GardeArret, match="type numérique"):
        inst.controle_juge(man, clone, tmp_path / "c", cache_juge={"strongreject_finetuned": (ModeleJuge("torch.float32"), Tok())},
                           juge=juge, generer=lambda entrees: ["refus"] * len(entrees))


# --- lanceur local -----------------------------------------------------------------------------------------------------

GO = ("| GO-2026-11-10-99 | 2026-11-10 | calcul | **Témoin de Bailey** devis v4 (`f9c8c66e…`) | 75 USD | "
      "2026-11-14 | Lazar | R-x |")


def test_ligne_go_et_echeance():
    go = la.ligne_go(GO, "GO-2026-11-10-99")
    la.verifier_go(go, 75)
    with pytest.raises(GardeArret):
        la.verifier_go(go, 80)
    with pytest.raises(GardeArret):
        la.ligne_go(GO, "GO-2026-11-10-98")
    fin = la.echeance_epoch(go["echeance"])
    la.verifier_echeance(fin, fin - 80 * 3600, 75, 1.0)
    with pytest.raises(GardeArret):
        la.verifier_echeance(fin, fin - 10 * 3600, 75, 1.0)


class FournisseurFactice(la.Fournisseur):
    def __init__(self, reponses=None, tmp=None):
        self.detruites, self.commandes, self.reponses, self.tmp = [], [], reponses or {}, tmp
        self.distant: dict[str, bytes] = {}

    def creer(self, offre, image, disque_go, env):
        return "77"

    def taux_horaire(self, ident):
        return 1.0

    def detruire(self, ident):
        self.detruites.append(ident)

    def executer(self, ident, commande, delai_s=None):
        self.commandes.append(commande)
        for cle, rep in self.reponses.items():
            if cle in commande:
                return rep(commande) if callable(rep) else rep
        return 0, ""

    def rapatrier_fichier(self, ident, distant, local):
        if distant not in self.distant:
            raise FileNotFoundError(distant)
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(self.distant[distant])


def test_poste_veilleur_de_secours(tmp_path):
    p = la.Poste(b=75)
    p.ajouter("1", 2.0, 0)
    p.detruite("1", 3600)
    p.ajouter("2", 1.0, 3600)
    assert p.depense(7200) == pytest.approx(3.0) and p.d_avant("2", 7200) == pytest.approx(2.0)
    f = FournisseurFactice()
    v = la.Veilleur(f, p, "2", echeance=1e12, journal=tmp_path / "a.jsonl", horloge=lambda: 3600 + 71 * 3600)
    assert v.verifier() is None  # B − 2 atteint : arrêt nominal sur l'instance, pas de destruction d'office
    v = la.Veilleur(f, p, "2", echeance=1e12, journal=tmp_path / "a.jsonl", horloge=lambda: 3600 + 72.6 * 3600)
    assert v.verifier() == "dépense (seuil de secours)"
    v.run()
    assert f.detruites == ["2"]
    v2 = la.Veilleur(f, la.Poste(b=75), "3", echeance=10, journal=tmp_path / "b.jsonl", horloge=lambda: 11 + 1800)
    assert v2.verifier() == "échéance du GO (délai de secours)"


def test_transfert_liste_fermee_et_second_essai(tmp_path):
    f = FournisseurFactice()
    rel = cv.JOURNAL_NOTES
    f.distant["/r/" + rel] = b"notes"
    attendu = {rel: __import__("hashlib").sha256(b"notes").hexdigest()}
    assert la.transferer(f, "1", "/r", tmp_path, attendu) == [attendu]
    faux = {rel: "0" * 64}
    assert len(la.transferer(f, "1", "/r", tmp_path / "b", faux)) == 2
    with pytest.raises(GardeArret, match="hors de la liste"):
        la.transferer(f, "1", "/r", tmp_path, {"params/x.pkl": "h"})  # un suffixe ne sort jamais (B-6)


def test_lire_etat_filtre():
    assert la.lire_etat("bruit\nETAT {\"a\": 1}\n") == {"a": 1}
    with pytest.raises(GardeArret):
        la.lire_etat("rien")


def test_manifeste_et_amorce(tmp_path):
    m = la.ecrire_manifeste(tmp_path / "m.json", versions={"torch": "2.4.0", "peft": "0.13.0"},
                            git={"strong_reject": ["https://github.com/dsbowen/strong_reject", cv.JUGE_COMMIT_PAQUET]},
                            revision_modele="rm", revision_adaptateur="ra", revision_base="rb", commit_code="abc",
                            b=75, go_id="GO-x")
    assert json.loads((tmp_path / "m.json").read_text())["graines"]["pilote"] == an.GRAINE_PILOTE
    s = la.script_amorce(m)
    assert cv.COMMIT_PUBLIC in s and "lciric/controle-ia-travail.git" in s and "torch==2.4.0" in s
    assert "strong_reject @ git+https://github.com/dsbowen/strong_reject@" + cv.JUGE_COMMIT_PAQUET in s
    assert s.count("refs/main") == 3 and "lciric/controle-ia.git" not in s
    assert m["chemin_modele"].endswith("/snapshots/rm")


def test_conduite_factice_bout_en_bout(tmp_path, monkeypatch):
    man = la.ecrire_manifeste(tmp_path / "m.json", versions={}, git={}, revision_modele="rm", revision_adaptateur="ra",
                              revision_base="rb", commit_code="abc", b=75, go_id="GO-2026-11-10-99")
    etat = lambda **kw: (0, "ETAT " + json.dumps(kw))

    def executer(cmd):
        if "--phase pilote" in cmd:
            return etat(commande="executer", phase="pilote", code_retour=0, cause_arret=None,
                        configuration_effective="passée", durees={"0": 100.0, "1": 110.0, "2": 120.0}, tours_marques=3)
        return etat(commande="executer", phase="principal", code_retour=0, cause_arret=None,
                    configuration_effective="passée", durees={}, tours_marques=25)

    f = FournisseurFactice({
        "AMORCE": None, "ETAT '{\"commande\": \"amorce\"": etat(commande="amorce", finie=True),
        "mise-en-place": etat(commande="mise-en-place", gardes={}, longueur_suffixe=16, pas_par_tour=1600),
        "controle-juge": etat(commande="controle-juge", etats={"tenus": True}),
        "executer": executer,
        "regle-tours": etat(commande="regle-tours", B=75, R=10, D=1.0, c=1.0, t=105.0, H_heures=64.0, K=72, arret=False),
        "empreintes": etat(commande="empreintes", fichiers=[]),
    }, tmp_path)
    f.reponses.pop("AMORCE")
    monkeypatch.setenv("GO_ID", "GO-2026-11-10-99")
    c = la.Conduite(f, tmp_path / "m.json", tmp_path / "sortie", "GO-2026-11-10-99", GO, "offre", "image",
                    horloge=lambda: la.echeance_epoch("2026-11-10"))
    bilan = c.conduire()
    assert bilan["mise_en_place"]["pas_par_tour"] == 1600 and bilan["regle"]["K"] == 72
    assert len(bilan["pilote"]) == 1 and len(bilan["principal"]) == 1
    assert f.detruites == ["77"]  # détruite par son identifiant, après la tentative de transfert
    assert any("--phase principal" in x for x in f.commandes)
    monkeypatch.setenv("GO_ID", "GO-autre")
    with pytest.raises(GardeArret, match="GO_ID"):
        la.Conduite(f, tmp_path / "m.json", tmp_path / "s2", "GO-2026-11-10-99", GO, "o", "i").conduire()
