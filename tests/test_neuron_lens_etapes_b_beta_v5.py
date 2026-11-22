"""Essais des gardes **telles que câblées** dans les étapes du lanceur v2 (contre-lecture du code de course v1, M-6) : les vraies fonctions
v3 du code de course (2026-11-18, session de la lecture par lentille neuronale) : seul changement de fond, la ligne de calcul exigée GO-2026-11-18-35 (R-3314) au lieu de la ligne de décision GO-2026-11-18-02, que le crochet de calcul refuse dans une commande de création ; le reste suit les noms v3 (lanceur, partie 2, amorce, dépôt réduit, essais).

d'étape, avec seulement les processus enfants (`ctx.executer`), le code voisin (`ctx.voisin_py`) et l'horloge remplacés ; petits fichiers
d'ajustement factices écrits par torch. Cas sain et artefact pour chaque garde câblée."""
import json
import subprocess
from pathlib import Path

import pytest

torch = pytest.importorskip("torch")

from controle_ia.manifeste import creer_manifeste, ecrire_resultat  # noqa: E402
from controle_ia.neuron_lens import b_beta_lancer_v3 as L  # noqa: E402
from controle_ia.neuron_lens import controles_b_beta_v2 as cb  # noqa: E402

D = 4  # dimension factice


@pytest.fixture
def ctx(tmp_path):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    (tmp_path / ".gitignore").write_text("/voisin/\n/voisin-banc/\n/originaux/\n")
    subprocess.run(["git", "-C", str(tmp_path), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "x"], check=True)
    c = L.Contexte(tmp_path, "20261119-230000-neuron-lens-b-beta", tmp_path / "hf")
    creer_manifeste(tmp_path, c.run_id, {"essai": True}, list(cb.TACHES_INTERVALLES), entropie=cb.ENTROPIE)
    for d in ("data/fits", "data/corpus", "data/summary", "data/checks"):
        (c.voisin / d).mkdir(parents=True, exist_ok=True)
        (c.banc_voisin / d).mkdir(parents=True, exist_ok=True)
    (c.voisin / "data/corpus/dclm.jsonl").write_text('{"text": "x"}\n')
    c.voisin_py = FauxVoisin()
    return c


def resultat(ctx, etape, contenu):
    ecrire_resultat(ctx.racine, ctx.manifeste, f"b-beta-{etape}", contenu)


class FauxVoisin:
    def __init__(self):
        self.rendu_fits = ("hub", "hub")
        self.lentilles = {}
        self.comptes_pilotes = {"dclm": 4, "code": 2, "chat": 2}
        self.k = list(range(10))

    def lens_docs_ajustement(self):
        rows = [[1] * 128 for _ in range(932)]
        return rows, cb.rows_sha256(rows), list(range(932))

    def fits(self):
        return self.rendu_fits

    def kept(self):
        return self.k

    def pilotes_comptes(self):
        return self.comptes_pilotes

    def load_lens(self, spec):
        if spec not in self.lentilles:
            raise FileNotFoundError(f"no R-lens in fit {spec!r}")
        return self.lentilles[spec]

    def split_half(self, saved):
        st = saved["state"]
        return {t: cb.split_half(st["sums"][(t, 0)].numpy(), st["sums"][(t, 1)].numpy(), *st["n_docs"])
                for t in sorted({t for t, _ in st["sums"]})}

    def textes(self, chemin):
        return [json.loads(l)["text"] for l in Path(chemin).read_text().splitlines() if l.strip()]


def ecrire_fit(chemin, lentille="R", n_docs=(466, 466), meta=None, graine=0):
    g = torch.Generator().manual_seed(graine)
    cibles = {"R": (("out", 31), ("mid", 32)), "S": (("mid", 32), ("out", 32))}[lentille]
    sums = {(t, h): torch.randn(n, D, D, generator=g) * 466 for t, n in cibles for h in (0, 1)}
    m = {"lens": lentille, "model": L.LLAMA, "docs": 932, "rows_sha256": cb.ROWS_SHA256, "full_length": True} | (meta or {})
    torch.save({"meta": m, "state": {"sums": sums, "n_docs": list(n_docs)}, "next_doc": 932}, chemin)
    return sums


def executer_ok(effet=None):
    appels = []

    def ex(cmd, cwd, env, journal, timeout):
        appels.append([str(c) for c in cmd])
        Path(journal).parent.mkdir(parents=True, exist_ok=True)
        with open(journal, "a") as fh:
            fh.write("\n=== " + " ".join(map(str, cmd)) + "\n")
            fin = effet(cmd, cwd, fh) if effet else None
        return {"code": 0, "duree_s": 0.1, "fin": fin or ["ok"]}
    ex.appels = appels
    return ex


# ---------------------------------------------------------------- ajustement : (q), (g), (h)

def test_ajustement_sain_puis_artefacts(ctx):
    f = ctx.voisin / "data/fits" / cb.FIT_NOMS["R"]
    ctx.executer = executer_ok(lambda cmd, cwd, fh: ecrire_fit(f) and None)
    r = L._ajustement(ctx, "R")
    assert r["n_docs"] == [466, 466] and len(r["diffs"]["out"]) == 31 and r["diffs_recopie"] == r["diffs"]


def test_q_fichier_present_au_premier_lancement(ctx):
    ecrire_fit(ctx.voisin / "data/fits" / cb.FIT_NOMS["R"])
    ctx.executer = executer_ok()
    with pytest.raises(L.ChaineEnDefaut) as e:
        L._ajustement(ctx, "R")
    assert list(e.value.lettres) == ["q"]


def test_q_point_de_sauvegarde_altere_a_la_relance(ctx):
    f = ctx.voisin / "data/fits" / cb.FIT_NOMS["R"]
    ctx.journal("ajustement-R").parent.mkdir(parents=True, exist_ok=True)
    ctx.journal("ajustement-R").write_text("premier lancement\n")
    ecrire_fit(f, meta={"rows_sha256": "0" * 64})
    with pytest.raises(L.ChaineEnDefaut) as e:
        L._ajustement(ctx, "R")
    assert list(e.value.lettres) == ["q"]


def test_g_moities_inegales(ctx):
    f = ctx.voisin / "data/fits" / cb.FIT_NOMS["S"]
    ctx.executer = executer_ok(lambda cmd, cwd, fh: ecrire_fit(f, "S", n_docs=(465, 467)) and None)
    with pytest.raises(L.ChaineEnDefaut) as e:
        L._ajustement(ctx, "S")
    assert "g" in e.value.lettres


# ---------------------------------------------------------------- export : (e), (n), (o), reprise par le manifeste

def _preparer_export(ctx):
    f = ctx.voisin / "data/fits" / cb.FIT_NOMS["R"]
    sums = ecrire_fit(f)
    resultat(ctx, "ajustement-R", {"sha256": L.sha256(f)})
    moy = {None: (sums[("out", 0)] + sums[("out", 1)]) / 932, 0: sums[("out", 0)] / 466, 1: sums[("out", 1)] / 466}
    for spec, (nom, moitie) in L.EXPORTS.items():
        ctx.voisin_py.lentilles[spec] = {l: moy[moitie][l].clone() for l in range(31)}
    g = torch.Generator().manual_seed(9)
    ctx.voisin_py.lentilles["npR"] = {l: torch.randn(D, D, generator=g) for l in range(31)}

    def effet(cmd, cwd, fh):
        nom = cmd[cmd.index("--name") + 1]
        home = ctx.voisin / "data/lenses" / nom / "local/r"
        home.mkdir(parents=True, exist_ok=True)
        (home / "manifest.json").write_text(json.dumps({"nom": nom}))
        (home / "layer-0.safetensors").write_bytes(nom.encode())
    ctx.executer = executer_ok(effet)


def test_export_sain_et_valeurs_versees(ctx):
    _preparer_export(ctx)
    r = L.etape_export(ctx)
    assert r["couches_out"] == list(range(31)) and len(r["matrices_moities"]) == 31
    assert all(v == 0.0 or v < 1e-6 for v in r["valeurs"]["aller_retour"][L.NOTRE_R].values())
    assert len(ctx.executer.appels) == 3


def test_export_reprise_sans_manifeste_refait(ctx):
    _preparer_export(ctx)
    partiel = ctx.voisin / "data/lenses/dclm-llama/local/r"
    partiel.mkdir(parents=True)
    (partiel / "layer-3.safetensors").write_bytes(b"interrompu")
    L.etape_export(ctx)
    assert not (partiel / "layer-3.safetensors").exists() and len(ctx.executer.appels) == 3


@pytest.mark.parametrize("artefact,lettre", [("none12", "o"), ("ecart5", "o"), ("identite10", "e"), ("egale_npR", "n"),
                                             ("absente", "o")])
def test_export_artefacts(ctx, artefact, lettre):
    _preparer_export(ctx)
    lent = ctx.voisin_py.lentilles
    if artefact == "none12":
        lent[L.NOTRE_R][12] = None
    elif artefact == "ecart5":
        lent[L.NOTRE_R][5] = lent[L.NOTRE_R][5] * 1.01
    elif artefact == "identite10":
        lent[L.NOTRE_R][10] = torch.eye(D)
    elif artefact == "egale_npR":
        lent["npR"][7] = lent[L.NOTRE_R][7].clone()
    else:
        del lent[L.MOITIES_R[1]]
    with pytest.raises(L.ChaineEnDefaut) as e:
        L.etape_export(ctx)
    assert lettre in e.value.lettres


# ---------------------------------------------------------------- pilotes : (k), (r), (p), tables

def _kept(ctx):
    resultat(ctx, "comptes-jetons", {"kept": {"n": 10, "sha256": cb.empreinte_liste_gardee(range(10))}})


def test_pilotes(ctx):
    _kept(ctx)
    cat = ctx.voisin / "data/catalog/llama"

    def effet(cmd, cwd, fh):
        for l in range(32):
            (cat / "neurons/drivers").mkdir(parents=True, exist_ok=True)
            (cat / f"neurons/drivers/L{l:02d}.parquet").write_bytes(b"t")
        (cat / "heads").mkdir(parents=True, exist_ok=True)
        (cat / "heads/drivers.parquet").write_bytes(b"h")
    ctx.executer = executer_ok(effet)
    assert L.etape_pilotes(ctx)["n_tables"] == 33
    ctx.voisin_py.comptes_pilotes = {"dclm": 3, "code": 2, "chat": 2}
    with pytest.raises(L.ChaineEnDefaut) as e:
        L.etape_pilotes(ctx)
    assert list(e.value.lettres) == ["p"]
    ctx.voisin_py.comptes_pilotes = {"dclm": 4, "code": 2, "chat": 2}
    ctx.voisin_py.rendu_fits = ("r-x", "s-x")
    with pytest.raises(L.ChaineEnDefaut) as e:
        L.etape_pilotes(ctx)
    assert list(e.value.lettres) == ["k"]
    ctx.voisin_py.rendu_fits = ("hub", "hub")
    ctx.voisin_py.k = list(range(9)) + [99]
    with pytest.raises(L.ChaineEnDefaut) as e:
        L.etape_pilotes(ctx)
    assert list(e.value.lettres) == ["r"]


def test_pilotes_tables_manquantes(ctx):
    _kept(ctx)
    ctx.executer = executer_ok()
    with pytest.raises(L.Arret, match="pilotes"):
        L.etape_pilotes(ctx)


# ---------------------------------------------------------------- measure : (p)

def test_measure_contextes(ctx):
    for i, n in enumerate((16, 15)):
        f = L._causal(ctx, 0)
        f.parent.mkdir(parents=True, exist_ok=True)
        torch.save({"meta": {"contexts": n}}, f)
        ctx.executer = executer_ok()
        if n == 16:
            assert L._measure(ctx, 0, "measure")["meta"]["contexts"] == 16
        else:
            with pytest.raises(L.ChaineEnDefaut) as e:
                L._measure(ctx, 0, "measure")
            assert list(e.value.lettres) == ["p"]


# ---------------------------------------------------------------- lectures : (s), liens durs, (k)

def _preparer_reads(ctx):
    _kept(ctx)
    for le in ("R", "S"):
        f = ctx.voisin / "data/fits" / cb.FIT_NOMS[le]
        f.write_bytes(le.encode() * 10)
        resultat(ctx, f"ajustement-{le}", {"sha256": L.sha256(f)})
    ctx.voisin_py.rendu_fits = tuple(n.removesuffix(".pt") for n in (cb.FIT_NOMS_ARCH["R"], cb.FIT_NOMS_ARCH["S"]))
    sortie = {"neurons": {"layers": [{"layer": l, "read_S": 0.5, "silent": 0.0} for l in range(32)]}}

    def effet(cmd, cwd, fh):
        (ctx.voisin / f"data/summary/reads_at_firings_{cb.STEM}.json").write_text(json.dumps(sortie))
    ctx.executer = executer_ok(effet)


def test_reads_sain_liens_poses(ctx):
    _preparer_reads(ctx)
    r = L.etape_reads(ctx)
    for le in ("R", "S"):
        a, b = ctx.voisin / "data/fits" / cb.FIT_NOMS[le], ctx.voisin / "data/fits" / cb.FIT_NOMS_ARCH[le]
        assert a.stat().st_ino == b.stat().st_ino  # lien dur
    assert r["n_couches"] == 32 and "--device" not in ctx.executer.appels[0]


def test_reads_s_premier_lancement_et_relance(ctx):
    _preparer_reads(ctx)
    (ctx.voisin / f"data/checks/reads_at_firings-{cb.STEM}.pt").write_bytes(b"ancien")
    with pytest.raises(L.ChaineEnDefaut) as e:
        L.etape_reads(ctx)
    assert list(e.value.lettres) == ["s"]
    ctx.journal("reads").parent.mkdir(parents=True, exist_ok=True)
    ctx.journal("reads").write_text("lancement interrompu\n")
    with pytest.raises(L.Arret) as e2:
        L.etape_reads(ctx)
    assert not isinstance(e2.value, L.ChaineEnDefaut)


def test_reads_k_hub_et_lien_different(ctx):
    _preparer_reads(ctx)
    ctx.voisin_py.rendu_fits = ("hub", "hub")
    with pytest.raises(L.ChaineEnDefaut) as e:
        L.etape_reads(ctx)
    assert list(e.value.lettres) == ["k"]


def test_reads_k_lien_d_une_autre_empreinte(ctx):
    _preparer_reads(ctx)
    (ctx.voisin / "data/fits" / cb.FIT_NOMS_ARCH["S"]).write_bytes(b"autre fichier")
    with pytest.raises(L.ChaineEnDefaut) as e:
        L.etape_reads(ctx)
    assert list(e.value.lettres) == ["k"]


# ---------------------------------------------------------------- banc

def test_banc(ctx):
    def effet_temps(t2):
        def effet(cmd, cwd, fh):
            if "02_fit.py" in " ".join(cmd):
                le = cmd[cmd.index("--lens") + 1].lower()
                for i, t in enumerate((40.0, t2, 30.0), 1):
                    fh.write(f"12:00:0{i} {le}-llama-3.1-8b-instruct-L32-dclm-T128 doc {i}/3 (128 tokens) in {t}s\n")
                ecrire_fit(ctx.banc_voisin / "data/fits" / cb.FIT_NOMS["R"])
            elif "-c" in cmd:
                fh.write("ALLER-RETOUR []\n")
                return ["ALLER-RETOUR []"]
        return effet
    ctx.executer = executer_ok(effet_temps(11.5))
    r = L.etape_banc(ctx)
    assert r["banc"]["R"]["secondes"] == [40.0, 11.5, 30.0] and r["compte_rendu"] is False  # le dernier (écriture) n'est pas lu
    ctx.executer = executer_ok(effet_temps(15.0))
    assert L.etape_banc(ctx)["compte_rendu"] is True
    ctx.executer = executer_ok(effet_temps(24.0))
    with pytest.raises(L.Arret, match="23,6"):
        L.etape_banc(ctx)


def test_banc_aller_retour_en_echec(ctx):
    def effet(cmd, cwd, fh):
        if "02_fit.py" in " ".join(cmd):
            for i in (1, 2, 3):
                fh.write(f"x doc {i}/3 (128 tokens) in 10.0s\n")
        elif "-c" in cmd:
            return ['ALLER-RETOUR ["(o) R:banc-aller-retour : None à la couche 3"]']
    ctx.executer = executer_ok(effet)
    with pytest.raises(L.Arret, match="aller-retour"):
        L.etape_banc(ctx)


def test_banc_qui_ecrit_dans_la_course(ctx):
    def effet(cmd, cwd, fh):
        if "02_fit.py" in " ".join(cmd):
            for i in (1, 2, 3):
                fh.write(f"x doc {i}/3 (128 tokens) in 10.0s\n")
            (ctx.voisin / "data/fits/intrus.pt").write_bytes(b"x")
    ctx.executer = executer_ok(effet)
    with pytest.raises(L.Arret, match=r"\(q\)"):
        L.etape_banc(ctx)


# ---------------------------------------------------------------- audits : temps réservé, contrôles des moitiés

def test_audits_controles_et_temps(ctx):
    resultat(ctx, "declencheurs", {"declenches": ["A2"], "debut_audits": 0.0})
    resultat(ctx, "ajustement-R", {"n_docs": [466, 466], "ecarts_sommes": {"out": 0.3, "mid": 0.2}, "longueurs": [128],
                                   "meta": {"full_length": True}, "sha256": "r"})
    resultat(ctx, "ajustement-S", {"n_docs": [466, 466], "ecarts_sommes": {"out": 0.1, "mid": 0.1}, "longueurs": [128],
                                   "meta": {"full_length": True}, "sha256": "s"})
    resultat(ctx, "corpus-ajustement", {"p1": {"rows_sha256_moities": list(cb.ROWS_SHA256_MOITIES)}})
    resultat(ctx, "export", {"matrices_moities": {str(l): ["a", "a" if l == 4 else "b"] for l in range(31)}})
    ctx.horloge = lambda: 10.0
    r = L.etape_audits_controles(ctx)
    assert r["audits"]["A2"]["controles_ok"] is False  # matrices des moitiés égales à la couche 4 (M-1)
    ctx.horloge = lambda: 3601.0
    assert L.etape_audits_controles(ctx)["audits"] == {"A2": "non joué"}


def test_audit_relance_temps_epuise(ctx):
    resultat(ctx, "declencheurs", {"declenches": ["A1"], "debut_audits": 0.0})
    resultat(ctx, "grandeurs", {"temoin_distinct": True, "normes_non_nulles": True})
    ctx.horloge = lambda: 4000.0
    assert L.etape_audit_relance(ctx)["resultat"] == "non joué"


# ---------------------------------------------------------------- B0 : import de Drowse

def test_b0_import_drowse_en_echec(ctx, monkeypatch):
    ctx.original_06.parent.mkdir(parents=True, exist_ok=True)
    ctx.original_06.write_bytes(b"x")
    monkeypatch.setattr(L, "ORIGINAL_06", (L.ORIGINAL_06[0], cb.sha256_octets(b"x")))

    def ex(cmd, cwd, env, journal, timeout):
        if cmd[1] == "-c":
            return {"code": 1, "duree_s": 0, "fin": ["ModuleNotFoundError: No module named 'yaml'"]}
        return {"code": 0, "duree_s": 0, "fin": ["7 passed in 1s"]}
    ctx.executer = ex
    with pytest.raises(L.Arret, match="import"):
        L.etape_b0(ctx, drowse=lambda: {"version": cb.DROWSE_VERSION, "roue_sha256": cb.DROWSE_SHA256})
