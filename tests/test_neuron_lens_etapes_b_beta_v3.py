"""Essais complémentaires des étapes câblées du lanceur v2 (`b_beta_lancer_v2`, inchangé), selon la vérification du code de course v2
(`docs/notes/neuron-lens-v1/correctifs-b-beta/verification-code-de-course-b-beta-v2.md`, `4d24a10a…` : majeur N-M1, mineurs N-m2,
N-m7). Joués dans le conteneur avant la course (R5) ; non embarqués sur la machine (déclaré dans la commande v3). Repris des doubles du
vérificateur (scratchpad), mis en assertions."""
import json
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

torch = pytest.importorskip("torch")

sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_neuron_lens_etapes_b_beta_v2 as T  # noqa: E402
import test_neuron_lens_verdicts_b_beta_v4 as TV  # noqa: E402
from test_neuron_lens_etapes_b_beta_v2 import ctx, resultat  # noqa: E402,F401

from controle_ia.neuron_lens import b_beta_lancer_v2 as L  # noqa: E402
from controle_ia.neuron_lens import controles_b_beta_v2 as cb  # noqa: E402

RESUME = f"causal_lens_{L.TAG}_{L.STEM}.json"


def monter(ctx, modif=None):
    """Sortie de `score` et série repère tirées du cas sain du code des verdicts (référence publiée de Qwen3-8B ramenée à 32 couches)."""
    e = TV.sain()
    if modif:
        modif(e)
    ctx.diag.mkdir(parents=True, exist_ok=True)
    (ctx.diag / RESUME).write_text(json.dumps({"targets": e.score}))
    rep = ctx.racine / L.SERIE_REPERE
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text(json.dumps({"targets": {"steer 1x": {"npR": {"layer": list(range(32)), "r_med": e.repere_npR}}}}))
    return e


# ---------------------------------------------------------------- gardes (a)–(c), (e), (j) à l'étape des grandeurs (m-4)

def test_grandeurs_sain(ctx, monkeypatch):
    e = monter(ctx)
    monkeypatch.setattr(L, "_grandeurs", lambda *a, **k: {"n": e.n, "ecartes": {}, "grandeurs": "x"})
    assert L.etape_grandeurs(ctx)["n"] == e.n


@pytest.mark.parametrize("artefact", ["j", "a"])
def test_grandeurs_artefacts(ctx, monkeypatch, artefact):
    def modif(e):
        if artefact == "j":  # lentille R publique écartée de 0,11 de la série repère à une couche (P.4, branches, (j))
            e.score["steer 1x"]["npR"]["r_med"][5] = round(e.score["steer 1x"]["npR"]["r_med"][5] + 0.11, 4)
        else:  # témoin de notre R à 0,20 à la couche 10 (cas (ii-b))
            e.score["steer 1x"][L.NOTRE_R]["control_med"][10] = 0.2
    e = monter(ctx, modif)
    monkeypatch.setattr(L, "_grandeurs", lambda *a, **k: {"n": e.n, "ecartes": {}, "grandeurs": "x"})
    with pytest.raises(L.ChaineEnDefaut) as x:
        L.etape_grandeurs(ctx)
    motifs = " ".join(x.value.lettres["a-c-e-j"])
    assert f"({artefact})" in motifs


# ---------------------------------------------------------------- cas sain de bout en bout : déclencheurs → verdict → intervalles

def _resultats_sains(ctx, e):
    resultat(ctx, "ajustement-R", {"diffs": {"out": e.stabilite[("R", "out")], "mid": e.stabilite[("R", "mid")]}})
    resultat(ctx, "ajustement-S", {"diffs": {"mid": e.stabilite[("S", "mid")], "out": e.stabilite[("S", "out")]}})
    sortie = {"neurons": {"layers": [{"layer": l, "read_S": e.read_S[l], "silent": e.silent[l]} for l in range(32)]}}
    (ctx.diag / "reads.json").write_text(json.dumps(sortie))
    resultat(ctx, "reads", {"sortie": str((ctx.diag / "reads.json").relative_to(ctx.racine))})
    resultat(ctx, "lens-compare", {"accord": {str(l): v for l, v in e.accord.items()}})
    (ctx.diag / "poles.json").write_text(json.dumps({"poles": []}))
    resultat(ctx, "grandeurs", {"n": e.n, "grandeurs": str((ctx.diag / "poles.json").relative_to(ctx.racine))})
    resultat(ctx, "b0", {"essais": {"a.py": {"code": 0, "resume": "5 passed in 1s", "passes": 5}},
                         "lentilles_np": {"J": {"e": []}}, "artefacts_d": {}})
    resultat(ctx, "fumee", {"code": 0})
    resultat(ctx, "corpus-activations", {"garde_i": []})


def test_bout_en_bout_sain(ctx):
    e = monter(ctx)
    _resultats_sains(ctx, e)
    r = L.etape_declencheurs(ctx)
    assert r["declenches"] == []
    resultat(ctx, "declencheurs", r)
    out = L.etape_verdicts(ctx)
    v = json.loads(ctx.fichier_verdicts.read_text())
    assert v["verdict"]["verdict"] == "reproduit avec nos lentilles"
    iv = json.loads((ctx.diag / "intervalles-b-beta-v1.json").read_text())
    assert set(cb.TACHES_INTERVALLES) <= set(iv) and out["intervalles_sha256"]


def test_intervalles_en_erreur_n_empechent_pas_le_verdict(ctx):
    e = monter(ctx)
    _resultats_sains(ctx, e)
    (ctx.diag / "poles.json").write_text("pas du json")  # m-13 : une erreur des intervalles ne touche pas au verdict
    resultat(ctx, "declencheurs", L.etape_declencheurs(ctx))
    L.etape_verdicts(ctx)
    assert json.loads(ctx.fichier_verdicts.read_text())["verdict"]["verdict"] == "reproduit avec nos lentilles"
    assert "erreur" in json.loads((ctx.diag / "intervalles-b-beta-v1.json").read_text())


def test_declencheurs_chaine_en_defaut_ecrite(ctx, monkeypatch):
    monkeypatch.setattr(L, "exiger_prerequis", lambda c, e: None)  # seuls les résultats lus par l'étape sont posés ici
    e = monter(ctx, lambda e: e.score["steer 1x"][L.NOTRE_R]["control_med"].__setitem__(10, 0.2))
    _resultats_sains(ctx, e)
    with pytest.raises(L.ChaineEnDefaut):
        L.jouer(ctx, "declencheurs", {"GO_ID": L.GO_ATTENDU, "NEURON_LENS_MODEL": L.LLAMA, "HF_HOME": "/h", "HF_HUB_OFFLINE": "1"})
    assert json.loads(ctx.fichier_verdicts.read_text())["verdict"] == "chaîne en défaut"


# ---------------------------------------------------------------- temps réservé relu après les grandeurs de la graine 1 (M-5)

def test_relance_depasse_l_heure_pendant_les_grandeurs(ctx, monkeypatch):
    resultat(ctx, "declencheurs", {"declenches": ["A1"], "debut_audits": 0.0})
    resultat(ctx, "grandeurs", {"temoin_distinct": True, "normes_non_nulles": True})
    t = {"v": 100.0}
    ctx.horloge = lambda: t["v"]
    monkeypatch.setattr(L, "_measure", lambda *a, **k: {"code": 0})
    monkeypatch.setattr(L, "_score", lambda *a, **k: {"code": 0})

    def grandeurs_lentes(*a, **k):
        t["v"] = 3700.0
        return {"n": {}, "temoin_distinct": True, "normes_non_nulles": True}
    monkeypatch.setattr(L, "_grandeurs", grandeurs_lentes)
    assert L.etape_audit_relance(ctx)["resultat"] == "non joué"
    t["v"] = 100.0
    monkeypatch.setattr(L, "_grandeurs", lambda *a, **k: {"n": {}, "temoin_distinct": True, "normes_non_nulles": False})
    r = L.etape_audit_relance(ctx)
    assert r["resultat"] == "joué" and r["graine_1"]["normes_non_nulles"] is False


def test_audits_controles_depassent_pendant_les_calculs(ctx, monkeypatch):
    resultat(ctx, "declencheurs", {"declenches": ["A4"], "debut_audits": 0.0})
    resultat(ctx, "ajustement-R", {"n_docs": [466, 466], "ecarts_sommes": {}, "longueurs": [128], "meta": {}, "sha256": "r"})
    resultat(ctx, "ajustement-S", {"n_docs": [466, 466], "ecarts_sommes": {}, "longueurs": [128], "meta": {}, "sha256": "s"})
    resultat(ctx, "corpus-ajustement", {"p1": {"rows_sha256_moities": []}})
    resultat(ctx, "export", {"matrices_moities": {}})
    (ctx.voisin / "data/fits" / cb.FIT_NOMS_ARCH["S"]).write_bytes(b"s")
    t = {"v": 10.0}
    ctx.horloge = lambda: t["v"]

    def points_fixes_lents():
        t["v"] = 3601.0
        return [2] * 32
    monkeypatch.setattr(cb, "points_fixes_permutation", points_fixes_lents)
    assert L.etape_audits_controles(ctx)["audits"] == {"A4": "non joué"}


# ---------------------------------------------------------------- jeton de début (B-1, 2) et « une seule fois » (m-1)

def test_comptes_jetons(ctx):
    comptes = torch.zeros(128256, dtype=torch.long)
    comptes[128000], comptes[3] = 50, 70
    ctx.voisin_py.comptes_jetons = lambda: comptes
    ctx.voisin_py.k = [1, 2, 3, 128000]
    sortie = ctx.voisin / "data" / f"token_counts-{L.STEM}.pt"
    ctx.executer = T.executer_ok(lambda cmd, cwd, fh: sortie.write_bytes(b"c") and None)
    r = L.etape_comptes_jetons(ctx)
    assert r["jeton_de_debut"] == {"compte": 50, "garde": True, "rang_par_compte": 2,
                                   "regle_egalites": "1 + jetons gardés de compte strictement plus grand"}
    with pytest.raises(L.Arret, match="relance de la machine"):
        L.etape_comptes_jetons(ctx)


# ---------------------------------------------------------------- export : moitiés aux mêmes sommes (M-1 de bout en bout, N-m2)

def test_export_moities_egales_vues_par_a2(ctx):
    f = ctx.voisin / "data/fits" / cb.FIT_NOMS["R"]
    g = torch.Generator().manual_seed(0)
    une = {t: torch.randn(n, T.D, T.D, generator=g) * 466 for t, n in (("out", 31), ("mid", 32))}
    sums = {(t, h): une[t].clone() for t in une for h in (0, 1)}  # moitiés aux sommes identiques
    torch.save({"meta": {"lens": "R", "model": L.LLAMA, "docs": 932, "rows_sha256": cb.ROWS_SHA256, "full_length": True},
                "state": {"sums": sums, "n_docs": [466, 466]}, "next_doc": 932}, f)
    resultat(ctx, "ajustement-R", {"sha256": L.sha256(f)})
    for spec, (nom, moitie) in L.EXPORTS.items():
        ctx.voisin_py.lentilles[spec] = {l: (une["out"][l] / 466).clone() for l in range(31)}
    ctx.voisin_py.lentilles["npR"] = {l: torch.randn(T.D, T.D, generator=g) for l in range(31)}

    def effet(cmd, cwd, fh):
        home = ctx.voisin / "data/lenses" / cmd[cmd.index("--name") + 1] / "local/r"
        home.mkdir(parents=True, exist_ok=True)
        (home / "manifest.json").write_text("{}")
    ctx.executer = T.executer_ok(effet)
    r = L.etape_export(ctx)  # (o) tient : chaque export égale la moyenne de sa moitié
    mm = {int(l): tuple(v) for l, v in r["matrices_moities"].items()}
    assert all(a == b for a, b in mm.values())
    ok, pb = cb.controles_a2_a3({"R": [466, 466]}, list(cb.ROWS_SHA256_MOITIES), {"R|out": 0.0}, mm)
    assert not ok and any("égales" in p for p in pb)


# ---------------------------------------------------------------- la chaîne de l'aller-retour du banc, jouée (N-m7)

FAUX_LENSES = textwrap.dedent('''
    import torch
    MODE = open(__file__.replace("lenses.py", "mode.txt")).read().strip()
    def load_lens(spec, model):
        saved = torch.load(__file__.replace("neuron_lens/lenses.py", "fit.pt"), weights_only=False)
        st = saved["state"]
        moy = (st["sums"][("out", 0)] + st["sums"][("out", 1)]).float() / sum(st["n_docs"])
        J = {l: moy[l].clone() for l in range(moy.shape[0])}
        if MODE == "none":
            J[3] = None
        if MODE == "leve":
            raise FileNotFoundError("no R-lens")
        return J
''')


@pytest.mark.parametrize("mode,attendu", [("sain", 0), ("none", 1), ("leve", 1)])
def test_chaine_aller_retour(tmp_path, mode, attendu):
    (tmp_path / "neuron_lens").mkdir()
    (tmp_path / "neuron_lens/__init__.py").write_text("")
    (tmp_path / "neuron_lens/lenses.py").write_text(FAUX_LENSES)
    (tmp_path / "neuron_lens/mode.txt").write_text(mode)
    T.ecrire_fit(tmp_path / "fit.pt")
    src = Path(L.__file__).resolve().parents[2]
    r = subprocess.run([sys.executable, "-c", L.ALLER_RETOUR, str(tmp_path / "fit.pt"), str(tmp_path)], cwd=tmp_path,
                       env={"PYTHONPATH": f"{tmp_path}:{src}", "PATH": "/usr/bin:/bin"}, capture_output=True, text=True)
    ligne = next(l for l in r.stdout.splitlines() if l.startswith("ALLER-RETOUR "))
    pb = json.loads(ligne.removeprefix("ALLER-RETOUR "))
    assert len(pb) == attendu, (r.stderr[-500:], pb)
