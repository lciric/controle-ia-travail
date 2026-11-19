"""Essais du lanceur de la tranche de l'ajustement de nos lentilles et de la partie 2 de l'addendum (sans modèle, sans réseau, sans code
v3 du code de course (2026-11-18, session de la lecture par lentille neuronale) : seul changement de fond, la ligne de calcul exigée GO-2026-11-18-35 (R-3314) au lieu de la ligne de décision GO-2026-11-18-02, que le crochet de calcul refuse dans une commande de création ; le reste suit les noms v3 (lanceur, partie 2, amorce, dépôt réduit, essais).

voisin : étapes remplacées par des doubles là où elles toucheraient la machine)."""
import json
import subprocess
from pathlib import Path

import pytest

from controle_ia.neuron_lens import addendum_partie2_b_beta_v3 as p2
from controle_ia.neuron_lens import b_beta_lancer_v3 as L
from controle_ia.neuron_lens import controles_b_beta_v2 as cb

RACINE = Path(__file__).resolve().parents[1]
ENV_OK = {"GO_ID": L.GO_ATTENDU, "NEURON_LENS_MODEL": L.LLAMA, "HF_HOME": "/tmp/hf", "HF_HUB_OFFLINE": "1"}


# ---------------------------------------------------------------- environnement

def test_environnement():
    assert L.verifier_environnement("score", ENV_OK) == []
    assert L.verifier_environnement("score", ENV_OK | {"HF_TOKEN": "x"})
    assert L.verifier_environnement("score", {k: v for k, v in ENV_OK.items() if k != "HF_HUB_OFFLINE"})
    jeton = {k: v for k, v in ENV_OK.items() if k != "HF_HUB_OFFLINE"} | {"HF_TOKEN": "x"}
    assert L.verifier_environnement("telecharger-poids", jeton) == []
    assert L.verifier_environnement("telecharger-poids", ENV_OK | {"HF_TOKEN": "x"})  # hors ligne à une étape qui télécharge
    assert L.verifier_environnement("corpus-ajustement", jeton)  # clé hors des téléchargements de Llama
    assert L.verifier_environnement("preparer", ENV_OK | {"GO_ID": "GO-2026-11-18-01"})
    assert L.verifier_environnement("score", ENV_OK | {"GH_TOKEN": "x"})
    assert L.verifier_environnement("inconnue", ENV_OK)


def test_env_enfant_sans_secret(monkeypatch):
    monkeypatch.setenv("HF_TOKEN", "secret")
    monkeypatch.setenv("GH_TOKEN", "secret")
    e = L.env_enfant(Path("/v"), True)
    assert "HF_TOKEN" not in e and "GH_TOKEN" not in e and e["HF_HUB_OFFLINE"] == "1" and e["NEURON_LENS_MODEL"] == L.LLAMA


def test_etapes_et_pieces_coherentes():
    assert set(L.ECHEANCES) == set(L.ETAPES) == set(L.ETAPE_FONCTIONS)
    assert L.ETAPES.index("banc") < L.ETAPES.index("ajustement-R") < L.ETAPES.index("export") < L.ETAPES.index("ajustement-S")
    assert L.ETAPES.index("ajustement-S") < L.ETAPES.index("lens-compare")
    assert L.ETAPES.index("comptes-jetons") < L.ETAPES.index("partie2-corpus") < L.ETAPES.index("lens-compare") < L.ETAPES.index("fumee")
    assert L.ETAPES.index("measure") < L.ETAPES.index("reads") < L.ETAPES.index("declencheurs")


def test_pieces_empreintes_sur_le_depot():
    """Toutes les pièces, correctifs et essais empreintés existent sur la branche, avec leur compagnon conforme."""
    from controle_ia.scellement import verifier
    for chemin, h in (L.PIECES | L.CORRECTIFS | {k: v for k, (v, _) in L.ESSAIS.items()}).items():
        assert verifier(RACINE / chemin) == h, chemin


# ---------------------------------------------------------------- artefacts de la garde (d) sur l'essai réel

def test_artefacts_d_motifs_uniques(tmp_path):
    src = RACINE / L.ESSAI_MINIATURE
    for nom, (avant, apres) in L.ARTEFACTS_D.items():
        L._copie_artefact(src, tmp_path / f"{nom}.py", avant, apres)
        t = (tmp_path / f"{nom}.py").read_text(encoding="utf-8")
        assert apres in t and t != src.read_text(encoding="utf-8")
    with pytest.raises(L.Arret):
        L._copie_artefact(src, tmp_path / "x.py", "motif absent de l'essai", "y")


def test_motif_hub_dans_le_correctif():
    diff = (RACINE / "docs/notes/neuron-lens-v1/correctifs/06_activations-llama-v2.diff").read_text(encoding="utf-8")
    assert "no released R-lens for {MODEL}: heads/acts without out_R_z" in diff
    assert cb.MOTIF_HUB == f"no released R-lens for {L.LLAMA}: heads/acts without out_R_z"


def test_banc_lit_le_journal():
    lignes = ["12:00:01 r-llama-3.1-8b-instruct-L32-dclm-T128 doc 1/2 (128 tokens) in 40.2s",
              "12:00:12 r-llama-3.1-8b-instruct-L32-dclm-T128 doc 2/2 (128 tokens) in 11.5s"]
    t = [float(m.group(4)) for l in lignes if (m := L._DOC.search(l)) and m.group(2) == "2"]
    assert t == [40.2, 11.5] and cb.regle_banc(t[1]) == "part"


# ---------------------------------------------------------------- déroulé : suite, prérequis, chaîne en défaut, verdict unique

@pytest.fixture
def ctx(tmp_path, monkeypatch):
    """Dépôt jouet (git propre) avec un manifeste, et des étapes remplacées par des doubles."""
    from controle_ia.manifeste import creer_manifeste
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    (tmp_path / "f.txt").write_text("x")
    subprocess.run(["git", "-C", str(tmp_path), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "x"], check=True)
    c = L.Contexte(tmp_path, "20261119-230000-neuron-lens-b-beta", tmp_path / "hf")
    creer_manifeste(tmp_path, c.run_id, {"essai": True}, list(cb.TACHES_INTERVALLES), entropie=cb.ENTROPIE)
    monkeypatch.setattr(L, "ETAPE_FONCTIONS", {e: (lambda ctx, e=e: {"double": e}) for e in L.ETAPES})
    return c


def _env(etape):
    e = dict(ENV_OK)
    if etape in L.EN_LIGNE:
        e.pop("HF_HUB_OFFLINE")
    if etape in L.JETON:
        e["HF_TOKEN"] = "x"
    return e


def test_suite_sans_audit_puis_fin(ctx, monkeypatch):
    vues = []
    while (e := L.suite(ctx)) is not None:
        vues.append(e)
        if e == "declencheurs":
            L.ETAPE_FONCTIONS[e] = lambda c: {"declenches": [], "debut_audits": 0.0}
        if e == "verdicts":
            L.ETAPE_FONCTIONS[e] = lambda c: {"fichier": str(L.ecrire_verdicts(c, {"verdict": "partiel"}))}
        L.jouer(ctx, e, _env(e))
    assert "audit-relance" not in vues and "audits-controles" not in vues
    assert vues[-1] == "verdicts" and ctx.fichier_verdicts.exists()
    with pytest.raises(SystemExit):
        L.jouer(ctx, "score", _env("score"))  # fichier de verdicts écrit : la course est finie


def test_suite_avec_audits(ctx):
    for e in L.ETAPES[:L.ETAPES.index("declencheurs")]:
        L.jouer(ctx, e, _env(e))
    L.ETAPE_FONCTIONS["declencheurs"] = lambda c: {"declenches": ["A1", "A4"], "debut_audits": 0.0}
    L.jouer(ctx, "declencheurs", _env("declencheurs"))
    assert L.suite(ctx) == "audits-controles"  # v2 : contrôles (secondes) avant la relance (M-5)
    L.jouer(ctx, "audits-controles", _env("audits-controles"))
    assert L.suite(ctx) == "audit-relance"
    with pytest.raises(L.Arret):
        L.exiger_prerequis(ctx, "verdicts")


def test_prerequis_et_audit_non_declenche(ctx):
    with pytest.raises(L.Arret):
        L.jouer(ctx, "b0", _env("b0"))  # préparation non faite
    for e in L.ETAPES[:L.ETAPES.index("declencheurs")]:
        L.jouer(ctx, e, _env(e))
    L.ETAPE_FONCTIONS["declencheurs"] = lambda c: {"declenches": [], "debut_audits": 0.0}
    L.jouer(ctx, "declencheurs", _env("declencheurs"))
    with pytest.raises(L.Arret):
        L.jouer(ctx, "audit-relance", _env("audit-relance"))
    assert L.suite(ctx) == "verdicts"


def test_chaine_en_defaut_ecrit_le_verdict_puis_arrete(ctx):
    L.jouer(ctx, "preparer", _env("preparer"))

    def defaut(c):
        L.exiger(q=["(q) fichier -T128 présent avant le premier lancement"], g=[])
    L.ETAPE_FONCTIONS["telecharger-tokeniseur"] = defaut
    with pytest.raises(L.ChaineEnDefaut):
        L.jouer(ctx, "telecharger-tokeniseur", _env("telecharger-tokeniseur"))
    v = json.loads(ctx.fichier_verdicts.read_text(encoding="utf-8"))
    assert v["verdict"] == "chaîne en défaut" and list(v["gardes_en_defaut"]) == ["q"]
    assert list(ctx.diag.glob("arret-telecharger-tokeniseur-*.json"))
    assert L.suite(ctx) is None
    with pytest.raises(L.Arret):
        L.ecrire_verdicts(ctx, {"verdict": "autre"})  # R12 : aucun écrasement


def test_arret_ordinaire_consigne(ctx):
    L.jouer(ctx, "preparer", _env("preparer"))
    L.ETAPE_FONCTIONS["telecharger-tokeniseur"] = lambda c: (_ for _ in ()).throw(L.Arret("panne"))
    with pytest.raises(L.Arret):
        L.jouer(ctx, "telecharger-tokeniseur", _env("telecharger-tokeniseur"))
    assert not ctx.fichier_verdicts.exists() and list(ctx.diag.glob("arret-telecharger-tokeniseur-*.json"))


# ---------------------------------------------------------------- relevés d'ajustement (torch)

def test_resume_fit_et_moyennes():
    torch = pytest.importorskip("torch")
    g = torch.Generator().manual_seed(0)
    sums = {(t, h): torch.randn(n, 4, 4, generator=g) for t, n in (("out", 31), ("mid", 32)) for h in (0, 1)}
    saved = {"meta": {"lens": "R", "docs": 932}, "state": {"sums": sums, "n_docs": [466, 466]}, "next_doc": 932}
    r = L.resume_fit(saved)
    assert r["premiere_dim"] == {"mid": 32, "out": 31} and r["finies"] is True and len(r["diffs"]["out"]) == 31
    assert all(v > 0 for v in r["ecarts_sommes"].values())
    m = L.moyennes_fit(saved, "out", 0)
    assert torch.allclose(torch.as_tensor(m[3]), sums[("out", 0)][3] / 466)
    sums[("mid", 1)][5, 0, 0] = float("inf")
    assert L.resume_fit(saved)["finies"] is False


# ---------------------------------------------------------------- partie 2

def _releve_b0_sain():
    essais = {Path(e).name: {"code": 0, "resume": f"{n} passed in 1s", "passes": n} for e, (_, n) in L.ESSAIS.items()}
    return {"date_utc": "2026-11-19T23:30:00Z", "instance": "1", "commit_reduit": "a", "commit_source": "b",
            "voisin": {"head": L.COMMIT_VOISIN, "arbre": L.ARBRE_VOISIN, "apres": dict(L.VOISIN_APRES)},
            "modele": dict(L.MODELE_FICHIERS), "lentilles_np": {s: h for s, (_, h) in L.LENTILLES_NP.items()},
            "versions": {k: v for k, v in cb.VERSIONS.items() if k != "drowse.ai"},
            "drowse": {"version": cb.DROWSE_VERSION, "roue_sha256": cb.DROWSE_SHA256}, "essais": essais,
            "artefacts_d": {"saute": {"code": 0, "resume": "10 passed, 1 skipped", "vu_en_defaut": True},
                            "signe": {"code": 1, "resume": "3 failed, 8 passed", "vu_en_defaut": True}},
            "corpus_ajustement": {"provenance_sha256": "p", "dclm_jsonl_sha256": "d",
                                  "p1": {"docs": 932, "moities": [466, 466], "longueurs": [128], "rows_sha256": cb.ROWS_SHA256,
                                         "rows_sha256_moities": list(cb.ROWS_SHA256_MOITIES)}}}


def test_partie2_b0_sain_et_ecarts():
    texte, pb = p2.rediger_b0(_releve_b0_sain())
    assert pb == [] and "Aucun." in texte
    for modif in (lambda r: r["modele"].update({"tokenizer.json": "0" * 64}),
                  lambda r: r["versions"].update({"transformers": "5.22.0"}),
                  lambda r: r["drowse"].update({"roue_sha256": "1" * 64}),
                  lambda r: r["essais"]["essai-transport-llama-miniature-v3.py"].update({"resume": "10 passed, 1 skipped"}),
                  lambda r: r["artefacts_d"]["signe"].update({"vu_en_defaut": False}),
                  lambda r: r["corpus_ajustement"]["p1"].update({"docs": 931}),
                  lambda r: r["voisin"].update({"head": "0" * 40})):
        r = _releve_b0_sain()
        modif(r)
        assert p2.rediger_b0(r)[1], modif


def test_partie2_corpus_et_secret():
    r = {"corpus": dict(cb.CORPUS_ACT_SHA256), "kept": {"n": cb.KEPT_N, "sha256": cb.KEPT_SHA256}, "provenances": []}
    assert p2.rediger_corpus(r)[1] == []
    assert p2.rediger_corpus(r | {"kept": {"n": cb.KEPT_N - 1, "sha256": cb.KEPT_SHA256}})[1]
    assert p2.rediger_corpus(r | {"provenances": ["dclm : liste des identifiants de lignes différente"]})[1]
    r2 = _releve_b0_sain()
    r2["instance"] = "hf_" + "a" * 30
    assert any("secret" in p for p in p2.rediger_b0(r2)[1])


def test_ecrire_une_fois(tmp_path):
    f = tmp_path / "p2.md"
    h = p2.ecrire_une_fois(f, "- date : 1\nx\n")
    assert p2.ecrire_une_fois(f, "- date : 2\nx\n") == h
    with pytest.raises(ValueError):
        p2.ecrire_une_fois(f, "- date : 3\ny\n")
