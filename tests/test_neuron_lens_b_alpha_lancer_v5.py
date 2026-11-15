"""Essais de `controle_ia.neuron_lens.b_alpha_lancer_v5` (v5 : essais de v4 + chaîne B-7 « par le haut », vrai `_verdicts` aux deux séries, bascule idempotente, mesure au lot 64 interrompue, gardes de fichier absent ; v4 : essais de v3 + seconde série au lot 64, bascule, essais_ok lu ; v3 : essais de v2 + lot réduit de `measure` ; v2 : essais de v1 + copie du script d'origine, environnement de
`etape_b0`, `etape_partie2` de bout en bout avec l'environnement de l'amorce) (R5 : cas sain et artefacts), sans réseau, sans modèle, sans code voisin :
le hub, les processus enfants et la lecture des lentilles sont remplacés."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.neuron_lens import addendum_partie2_b_alpha_v1 as p2
from controle_ia.neuron_lens import b_alpha_lancer_v5 as bl

ENV_SAIN = {"GO_ID": bl.GO_ATTENDU, "NEURON_LENS_MODEL": bl.LLAMA, "HF_HOME": "/tmp/hf"}


def env_pour(etape, **extra):
    e = dict(ENV_SAIN)
    if etape in bl.JETON:
        e["HF_TOKEN"] = "x"
    if etape not in bl.EN_LIGNE:
        e["HF_HUB_OFFLINE"] = "1"
    return e | extra


# ------------------------------------------------------------------------------------------------ environnement

@pytest.mark.parametrize("etape", bl.ETAPES)
def test_environnement_sain(etape):
    assert bl.verifier_environnement(etape, env_pour(etape)) == []


@pytest.mark.parametrize("etape,modif,motif", [
    ("b0", {"HF_TOKEN": "x"}, "HF_TOKEN présent"),
    ("corpus", {"HF_TOKEN": "x"}, "HF_TOKEN présent"),
    ("measure", {"HUGGING_FACE_HUB_TOKEN": "x"}, "HUGGING_FACE_HUB_TOKEN présent"),
    ("telecharger-poids", {"HF_TOKEN": ""}, "HF_TOKEN absent"),
    ("telecharger-tokeniseur", {"HUGGING_FACE_HUB_TOKEN": "x"}, "HUGGING_FACE_HUB_TOKEN présent"),
    ("score", {"GH_TOKEN": "x"}, "GH_TOKEN"),
    ("fumee", {"HF_HUB_OFFLINE": "0"}, "exigé"),
    ("corpus", {"HF_HUB_OFFLINE": "1"}, "télécharge"),
    ("passe", {"GO_ID": "GO-2026-11-14-05"}, "GO_ID"),
    ("passe", {"NEURON_LENS_MODEL": "Qwen/Qwen3-8B"}, "NEURON_LENS_MODEL"),
    ("inconnue", {}, "inconnue"),
])
def test_environnement_artefacts(etape, modif, motif):
    env = env_pour(etape if etape in bl.ETAPES else "b0") | modif
    if modif.get("HF_TOKEN") == "":
        del env["HF_TOKEN"]
    pb = bl.verifier_environnement(etape, env)
    assert pb and any(motif in p for p in pb), pb


def test_env_enfant_sans_secret(monkeypatch, tmp_path):
    for k in ("HF_TOKEN", "HUGGING_FACE_HUB_TOKEN", "GH_TOKEN"):
        monkeypatch.setenv(k, "VALEUR-SECRETE-7731")
    monkeypatch.setenv("HF_HUB_OFFLINE", "1")
    e = bl.env_enfant(tmp_path, hors_ligne=False)
    assert not {"HF_TOKEN", "HUGGING_FACE_HUB_TOKEN", "GH_TOKEN", "HF_HUB_OFFLINE"} & set(e)
    assert e["PYTHONPATH"] == str(tmp_path) and e["NEURON_LENS_MODEL"] == bl.LLAMA
    e = bl.env_enfant(tmp_path, hors_ligne=True, modele=bl.QWEN, NEURON_LENS_ROOT=tmp_path)
    assert e["HF_HUB_OFFLINE"] == "1" and e["NEURON_LENS_MODEL"] == bl.QWEN and e["NEURON_LENS_ROOT"] == str(tmp_path)
    assert "VALEUR-SECRETE-7731" not in json.dumps(e)


def test_executer(tmp_path):
    j = tmp_path / "j" / "x.log"
    s = bl.executer([sys.executable, "-c", "print('bonjour')"], tmp_path, {"PATH": "/usr/bin"}, j, 60)
    assert s["code"] == 0 and "bonjour" in s["fin"]
    s = bl.executer([sys.executable, "-c", "import sys; sys.exit(3)"], tmp_path, {}, j, 60)
    assert s["code"] == 3
    s = bl.executer([sys.executable, "-c", "import time; time.sleep(5)"], tmp_path, {}, j, 0.5)
    assert s["code"] == 124
    assert j.read_text().count("===") == 3  # journal en ajout


@pytest.mark.parametrize("ligne,ok", [("12 passed in 1.0s", True), ("11 passed, 1 skipped in 1s", False),
                                      ("1 failed, 3 passed in 2s", False), ("no tests ran in 0.1s", False),
                                      ("3 passed, 1 error in 2s", False)])
def test_bilan_pytest(ligne, ok):
    x = {"code": 0 if ok or "skipped" in ligne else 1, "resume": bl.resume_pytest({"fin": ["....", ligne, ""]})}
    assert x["resume"] == ligne and bl._ok_pytest(x) is ok


def test_epingler(tmp_path):
    bl.epingler(tmp_path, bl.LLAMA, "a" * 40)
    ref = tmp_path / "hub" / "models--meta-llama--Llama-3.1-8B-Instruct" / "refs" / "main"
    assert ref.read_text() == "a" * 40
    bl.epingler(tmp_path, bl.LLAMA, "a" * 40)  # idempotent
    with pytest.raises(bl.Arret, match="refs/main"):
        bl.epingler(tmp_path, bl.LLAMA, "b" * 40)
    bl.epingler(tmp_path, "stdlogits/neuron-lens", "c" * 40, "dataset")
    assert (tmp_path / "hub" / "datasets--stdlogits--neuron-lens" / "refs" / "main").exists()


def _info(sha=p2.REVISION_LLAMA, sans=None):
    sib = [SimpleNamespace(rfilename=n, lfs=None, blob_id="1" * 40, size=10) for n in bl.TOKENISEUR if n != sans]
    sib += [SimpleNamespace(rfilename="model-00001-of-00002.safetensors", lfs=SimpleNamespace(sha256="2" * 64, size=99),
                            blob_id="3" * 40, size=99),
            SimpleNamespace(rfilename="original/consolidated.00.pth", lfs=SimpleNamespace(sha256="4" * 64, size=9), blob_id="5" * 40,
                            size=9),
            SimpleNamespace(rfilename="LICENSE", lfs=None, blob_id="6" * 40, size=5)]
    return SimpleNamespace(sha=sha, siblings=sib)


def test_attendus_hub():
    a = bl._attendus_hub(_info(), p2.REVISION_LLAMA)
    assert set(a) == set(bl.TOKENISEUR) | {"model-00001-of-00002.safetensors"}  # ni original/, ni LICENSE
    assert a["model-00001-of-00002.safetensors"] == {"lfs_sha256": "2" * 64, "taille": 99}
    assert a["config.json"] == {"git_sha1": "1" * 40, "taille": 10}
    with pytest.raises(bl.Arret, match="révision"):
        bl._attendus_hub(_info(sha="f" * 40), p2.REVISION_LLAMA)
    with pytest.raises(bl.Arret, match="tokenizer.json"):
        bl._attendus_hub(_info(sans="tokenizer.json"), p2.REVISION_LLAMA)


# ------------------------------------------------------------------------------------------------ machine à étapes

def _depot(tmp_path):
    r = tmp_path / "depot"
    r.mkdir()
    (r / ".gitignore").write_text("diag/\nruns/\n")
    subprocess.run(["git", "init", "-q", str(r)], check=True)
    subprocess.run(["git", "-C", str(r), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(r), "-c", "user.name=t", "-c", "user.email=t@example.invalid", "commit", "-q", "-m", "i"],
                   check=True)
    return r


@pytest.fixture
def ctx(tmp_path, monkeypatch):
    from controle_ia.manifeste import creer_manifeste
    c = bl.Contexte(_depot(tmp_path), "20261120-100000-neuron-lens-b-alpha", tmp_path / "hf")
    appels = []

    def faux(etape):
        def f(ctx_):
            appels.append(etape)
            if etape == "preparer" and not ctx_.manifeste.exists():
                creer_manifeste(ctx_.racine, ctx_.run_id, {"essai": 1}, ["b-alpha-intervalles"], entropie=bl.ENTROPIE)
            if etape == "verdicts":
                return {"audits_requis": list(getattr(c, "_requis", []))}
            return {"ok": True}
        return f
    monkeypatch.setattr(bl, "ETAPE_FONCTIONS", {e: faux(e) for e in bl.ETAPES})
    c._appels = appels
    return c


def jouer(c, e):
    return bl.jouer(c, e, env=env_pour(e))


def test_suite_ordre_et_reprise(ctx):
    assert not ctx.manifeste.exists()
    for e in [e for e in bl.ETAPES if e not in bl.AUDITS]:
        assert bl.suite(ctx) == e if ctx.manifeste.exists() else e == "preparer"
        chemin = jouer(ctx, e)
        assert chemin == ctx.resultat(e) and ctx.fait(e)
    assert bl.suite(ctx) is None  # aucun audit requis
    n = len(ctx._appels)
    assert jouer(ctx, "measure") == ctx.resultat("measure") and len(ctx._appels) == n  # étape faite : non rejouée
    r = ctx.lire("passe")
    assert r["etape"] == "passe" and r["echeance_h"] == {"attendu": 1.4, "pire_cas": 2.5} and r["depassement_pire_cas"] is False


def test_prerequis_refuses(ctx):
    jouer(ctx, "preparer")
    with pytest.raises(bl.Arret, match="préalable non faite : b0"):
        jouer(ctx, "telecharger-poids")
    arrets = sorted(p.name for p in ctx.diag.glob("arret-*.json"))
    assert arrets == ["arret-telecharger-poids-1.json"]
    with pytest.raises(bl.Arret):
        jouer(ctx, "telecharger-poids")
    assert (ctx.diag / "arret-telecharger-poids-2.json").exists()  # jamais d'écrasement (R12)
    with pytest.raises(SystemExit, match="environnement"):
        bl.jouer(ctx, "b0", env=env_pour("b0", HF_TOKEN="x"))


def test_manifeste_exige(ctx):
    with pytest.raises(SystemExit, match="manifeste absent"):
        jouer(ctx, "b0")


def test_audits_seulement_requis(ctx):
    ctx._requis = ["audit-tout-negatif"]
    for e in [e for e in bl.ETAPES if e not in bl.AUDITS]:
        jouer(ctx, e)
    assert bl.suite(ctx) == "audit-tout-negatif"
    with pytest.raises(bl.Arret, match="non requis"):
        jouer(ctx, "audit-trop-beau")
    jouer(ctx, "audit-tout-negatif")
    assert bl.suite(ctx) is None


def test_resultat_altere(ctx):
    jouer(ctx, "preparer")
    jouer(ctx, "telecharger-tokeniseur")
    p = ctx.resultat("telecharger-tokeniseur")
    p.write_text(p.read_text().replace("true", "false"))
    with pytest.raises(GardeArret):
        bl.suite(ctx)


def test_echec_consigne(ctx, monkeypatch):
    jouer(ctx, "preparer")

    def casse(c):
        raise RuntimeError("panne simulée")
    monkeypatch.setitem(bl.ETAPE_FONCTIONS, "telecharger-tokeniseur", casse)
    with pytest.raises(RuntimeError):
        jouer(ctx, "telecharger-tokeniseur")
    a = json.loads((ctx.diag / "arret-telecharger-tokeniseur-1.json").read_text())["resultat"]
    assert a == {"etape": "telecharger-tokeniseur", "type": "RuntimeError", "message": "panne simulée"}
    assert not ctx.fait("telecharger-tokeniseur")


# ------------------------------------------------------------------------------------------------ B0, partie 2, fumée

def _ecrire(ctx, etape, contenu):
    from controle_ia.manifeste import creer_manifeste, ecrire_resultat
    if not ctx.manifeste.exists():
        creer_manifeste(ctx.racine, ctx.run_id, {"essai": 1}, ["b-alpha-intervalles"], entropie=bl.ENTROPIE)
    ecrire_resultat(ctx.racine, ctx.manifeste, f"b-alpha-{etape}", contenu)


def faux_executer(codes):
    """Rend, dans l'ordre des appels, (code, dernière ligne)."""
    file = list(codes)

    def f(cmd, cwd, env, journal, timeout_s):
        assert "HF_TOKEN" not in env and "GH_TOKEN" not in env
        code, ligne = file.pop(0)
        return {"code": code, "duree_s": 0.1, "fin": ["...", ligne]}
    return f


def lentille_saine(voisin, s):
    return {"arrets": [], "defauts": [], "autres_cles": "['provenance']", "sortie": "ok"}


def _faux_original(c, monkeypatch):
    c.original_06.parent.mkdir(parents=True, exist_ok=True)
    c.original_06.write_text("# script d'origine factice\n")
    monkeypatch.setattr(bl, "ORIGINAL_06", ("scripts/06_activations.py", bl.sha256(c.original_06)))


def test_b0_environnement_des_essais(tmp_path, monkeypatch):
    """L'essai du correctif (1) reçoit NEURON_LENS_ORIG (la copie d'origine) et NEURON_LENS_ROOT ; artefact : copie absente ou
    altérée → arrêt avant tout essai."""
    c = bl.Contexte(tmp_path, "r", tmp_path / "hf")
    vus = []

    def ex(cmd, cwd, env, journal, timeout_s):
        vus.append(env)
        return {"code": 0, "duree_s": 0.1, "fin": ["12 passed in 1s"]}
    c.executer = ex
    with pytest.raises(bl.Arret, match="origine"):
        bl.etape_b0(c, lire_lentille=lentille_saine)
    assert vus == []
    _faux_original(c, monkeypatch)
    bl.etape_b0(c, lire_lentille=lentille_saine)
    for env in vus[:4]:
        assert env["NEURON_LENS_ORIG"] == str(c.original_06) and env["NEURON_LENS_ROOT"] == str(c.voisin)
        assert env["HF_HUB_OFFLINE"] == "1" and "HF_TOKEN" not in env
    c.original_06.write_text("altéré\n")
    with pytest.raises(bl.Arret, match="origine"):
        bl.etape_b0(c, lire_lentille=lentille_saine)


def test_b0_sain_et_artefacts(tmp_path, monkeypatch):
    c = bl.Contexte(tmp_path, "r", tmp_path / "hf")
    _faux_original(c, monkeypatch)
    ok = [(0, "12 passed in 1s")] * 5
    c.executer = faux_executer(ok)
    r = bl.etape_b0(c, lire_lentille=lentille_saine)
    assert set(r["essais"]) == set(p2.ESSAIS_B0) and r["verdicts_b3"]["code"] == 0
    c.executer = faux_executer([(0, "12 passed in 1s"), (0, "11 passed, 1 skipped in 1s")] + ok[:3])
    with pytest.raises(bl.Arret, match="essai-lenses-neuronpedia-v3.py"):
        bl.etape_b0(c, lire_lentille=lentille_saine)
    c.executer = faux_executer(ok)
    with pytest.raises(bl.Arret, match="lentille npR"):
        bl.etape_b0(c, lire_lentille=lambda v, s: lentille_saine(v, s) | ({"arrets": ["30 couches"]} if s == "npR" else {}))
    c.executer = faux_executer(ok[:4] + [(1, "1 failed, 39 passed in 2s")])
    with pytest.raises(bl.Arret, match="B.3"):
        bl.etape_b0(c, lire_lentille=lentille_saine)
    c.executer = faux_executer(ok)  # un défaut (e) n'arrête pas B0 : il est jugé au verdict
    r = bl.etape_b0(c, lire_lentille=lambda v, s: lentille_saine(v, s) | {"defauts": ["identité couche 2"]})
    assert r["lentilles"]["J"]["defauts"] == ["identité couche 2"]


def test_fumee_exige_la_partie2(tmp_path):
    c = bl.Contexte(_depot(tmp_path), "20261120-100000-neuron-lens-b-alpha", tmp_path / "hf")
    c.executer = faux_executer([(0, "fumée")] * 3)
    _ecrire(c, "preparer", {})
    with pytest.raises(GardeArret):  # résultat de la partie 2 absent
        bl.etape_fumee(c)
    c.diag.mkdir(parents=True, exist_ok=True)
    h = p2.ecrire_et_sceller(bl.chemin_partie2(c), "# partie 2\n")
    _ecrire(c, "partie2", {"sha256": h, "ecarts": []})
    assert bl.etape_fumee(c)["code"] == 0
    bl.chemin_partie2(c).write_text("# partie 2 altérée\n")
    with pytest.raises(GardeArret):
        bl.etape_fumee(c)


def test_fumee_refuse_partie2_avec_ecarts(tmp_path):
    c = bl.Contexte(_depot(tmp_path), "20261120-100000-neuron-lens-b-alpha", tmp_path / "hf")
    c.executer = faux_executer([(0, "fumée")])
    _ecrire(c, "preparer", {})
    c.diag.mkdir(parents=True, exist_ok=True)
    h = p2.ecrire_et_sceller(bl.chemin_partie2(c), "# partie 2\n")
    _ecrire(c, "partie2", {"sha256": h, "ecarts": ["lentille npR : empreinte"]})
    with pytest.raises(bl.Arret, match="écarts"):
        bl.etape_fumee(c)


# ------------------------------------------------------------------------------------------------ téléchargements

def test_telecharger_tokeniseur(tmp_path, monkeypatch):
    fichiers = {}

    def creer(nom, contenu):
        p = tmp_path / "cache" / nom.replace("/", "_")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(contenu)
        fichiers[nom] = p
        return p
    sib = []
    for n in bl.TOKENISEUR:
        b = f"contenu {n}".encode()
        creer(n, b)
        sib.append(SimpleNamespace(rfilename=n, lfs=None, blob_id=p2.git_sha1(b), size=len(b)))
    sib.append(SimpleNamespace(rfilename="model-00001-of-00001.safetensors", lfs=SimpleNamespace(sha256="9" * 64, size=1),
                               blob_id="0" * 40, size=1))
    lent, conf = {}, {}
    for s, f in bl.LENTILLES_FICHIERS.items():
        b = f"lentille {s}".encode()
        creer(f, b)
        lent[s] = __import__("hashlib").sha256(b).hexdigest()
    for n in p2.CONFIG_NEURONPEDIA:
        b = f"config {n}".encode()
        creer(f"llama3.1-8b-it/{n}", b)
        conf[n] = p2.git_sha1(b)
    monkeypatch.setattr(p2, "LENTILLES", lent)
    monkeypatch.setattr(p2, "CONFIG_NEURONPEDIA", conf)
    jetons = []

    def telecharger(depot, nom, revision=None, token=None, **k):
        jetons.append((depot, token))
        return str(fichiers[nom])
    c = bl.Contexte(tmp_path, "r", tmp_path / "hf", hub=(lambda *a, **k: SimpleNamespace(sha=p2.REVISION_LLAMA, siblings=sib),
                                                          telecharger))
    c.executer = lambda cmd, cwd, env, journal, t: ({"code": 0, "duree_s": 0, "fin": ["nv 128256"]}
                                                     if "HF_TOKEN" not in env else pytest.fail("clé transmise à un enfant"))
    r = bl.etape_telecharger_tokeniseur(c, charger_tokeniseur=lambda: 128256)
    assert r["nv"] == 128256 and set(r["tokeniseur"]) == set(bl.TOKENISEUR)
    assert all(t is False for d, t in jetons if d == bl.NP) and all(t is None for d, t in jetons if d == bl.LLAMA)
    assert (tmp_path / "hf/hub/models--neuronpedia--jacobian-lens/refs/main").read_text() == p2.REVISION_NEURONPEDIA
    # artefacts : un autre tokeniseur répond sans clé ; une lentille différente ; un fichier du tokeniseur altéré
    c.executer = lambda cmd, cwd, env, journal, t: {"code": 0, "duree_s": 0, "fin": ["nv 32000"]}
    with pytest.raises(bl.Arret, match="autre tokeniseur"):
        bl.etape_telecharger_tokeniseur(c, charger_tokeniseur=lambda: 128256)
    c.executer = lambda cmd, cwd, env, journal, t: {"code": 0, "duree_s": 0, "fin": ["nv 128256"]}
    fichiers[bl.LENTILLES_FICHIERS["npR"]].write_bytes(b"autre")
    with pytest.raises(bl.Arret, match="lentille npR"):
        bl.etape_telecharger_tokeniseur(c, charger_tokeniseur=lambda: 128256)
    fichiers["tokenizer.json"].write_bytes(b"autre")
    with pytest.raises(bl.Arret, match="tokenizer.json"):
        bl.etape_telecharger_tokeniseur(c, charger_tokeniseur=lambda: 128256)


# ------------------------------------------------------------------------------------------------ audit « tout négatif »

def _table(valeurs):
    return {c: {s: {"layer": [0, 1], "r_med": v} for s, v in valeurs.items()} for c in ("steer 1x", "ablate win")}


def test_cas_sain_qwen():
    publie = {"targets": _table({"logit": [0.9, 0.8], "J": [0.5, 0.6], "R:dclm": [0.7, 0.7]})}
    sain = bl.ecarts_qwen(_table({"logit": [0.9, 0.81], "J": [0.52, 0.6], "hub": [0.7, 0.7]}), publie)
    assert bl.cas_sain_qwen(sain) == [] and sain["steer 1x|J"] == 0.02
    hub_loin = bl.ecarts_qwen(_table({"logit": [0.9, 0.8], "J": [0.5, 0.6], "hub": [0.2, 0.7]}), publie)
    assert bl.cas_sain_qwen(hub_loin) == [] and hub_loin["steer 1x|hub"] == 0.5  # rapporté, non jugé
    manque = bl.ecarts_qwen(_table({"logit": [0.9, 0.8], "J": [0.5, 0.66], "hub": [0.7, 0.7]}), publie)
    assert bl.cas_sain_qwen(manque) == ["steer 1x|J", "ablate win|J"]
    absente = bl.ecarts_qwen({"steer 1x": {"logit": {"layer": [0], "r_med": [0.9]}}}, publie)
    assert "steer 1x|J" in bl.cas_sain_qwen(absente)


def test_intervalles_reproductibles(tmp_path):
    c = bl.Contexte(_depot(tmp_path), "20261120-100000-neuron-lens-b-alpha", tmp_path / "hf")
    _ecrire(c, "preparer", {})
    poles = [{"couche": l, "aleatoire": True, "lectures": {"steer 1x": {s: {"r": 0.01 * (i % 50) + l / 100, "motif": "retenu"}
                                                                          for s in ("npR", "logit")}}}
             for l in range(32) for i in range(64)]
    (c.diag / "grandeurs-par-pole-b-alpha-v1.json").write_text(json.dumps({"poles": poles}))
    a, b = bl.intervalles(c, 200), bl.intervalles(c, 200)
    assert a == b and len(a["steer 1x"]["npR"]) == 32
    lo, hi = a["steer 1x"]["npR"][0]
    assert lo <= 0.245 <= hi


# ------------------------------------------------------------------------------------------------ préparer, sur une vraie copie

VOISIN_LECTURE = Path("/home/user/stdlogits/neuron-lens")


@pytest.mark.skipif(not (VOISIN_LECTURE / ".git").exists(), reason="copie de lecture du dépôt voisin absente (essai du conteneur)")
def test_preparer_sur_copie_reelle(tmp_path):
    """Cas sain : copie du code voisin à 849bfe16 (git archive, rien n'est exécuté), pièces et modules du dépôt copiés ; les quatre
    correctifs s'appliquent et donnent les empreintes attendues ; reprise idempotente. Artefact : un fichier voisin modifié → arrêt."""
    import shutil
    src = Path(__file__).resolve().parents[1]
    r = _depot(tmp_path)
    fichiers = list(bl.PIECES) + [f"src/controle_ia/neuron_lens/{m}" for m in bl.MODULES]
    fichiers += [f"{bl.DOSSIER_CORRECTIFS}/{d}" for d in bl.CORRECTIFS + p2.ESSAIS_B0]
    for f in fichiers:
        for x in (f, f + ".sha256"):
            (r / x).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src / x, r / x)
    v = r / "voisin" / "neuron-lens"
    v.mkdir(parents=True)
    arch = subprocess.run(["git", "-C", str(VOISIN_LECTURE), "archive", p2.COMMIT_VOISIN], capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "-C", str(v)], input=arch, check=True)
    subprocess.run(["git", "-C", str(r), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(r), "-c", "user.name=t", "-c", "user.email=t@example.invalid", "commit", "-q", "-m", "c"],
                   check=True)
    c = bl.Contexte(r, "20261120-100000-neuron-lens-b-alpha", tmp_path / "hf")
    res = bl.ETAPE_FONCTIONS["preparer"](c)
    assert res["voisin_apres"] == bl.VOISIN_APRES and c.manifeste.exists()
    assert sorted(p.name for p in (c.diag / "references").glob("*.json")) == sorted(Path(x).name for x, _ in bl.REFERENCES.values())
    assert c.original_06.exists() and bl.sha256(c.original_06) == bl.ORIGINAL_06[1]  # copie d'origine gardée avant les correctifs
    assert res["original_06"]["sha256"] == bl.ORIGINAL_06[1]
    assert bl.ETAPE_FONCTIONS["preparer"](c)["voisin_apres"] == bl.VOISIN_APRES  # reprise : correctifs déjà appliqués
    c.original_06.unlink()
    with pytest.raises(bl.Arret, match="origine"):  # reprise sans la copie : arrêt
        bl.ETAPE_FONCTIONS["preparer"](c)
    (v / "neuron_lens" / "arch.py").write_text("# autre\n")
    with pytest.raises(bl.Arret, match="inattendu"):
        bl.ETAPE_FONCTIONS["preparer"](c)


# ------------------------------------------------------------------------------------------------ partie 2 de bout en bout

def _partie2_monte(tmp_path):
    """Contexte avec manifeste et résultats des étapes préalables tels que le lanceur les écrit, corpus et provenances factices
    cohérents ; les valeurs fixées par le texte gelé (révisions, lentilles, configurations) sont les vraies."""
    c = bl.Contexte(_depot(tmp_path), "20261120-100000-neuron-lens-b-alpha", tmp_path / "hf")
    fich = {n: {"sha256": f"{i:064x}", "git_sha1": f"{i:040x}", "taille": 10 + i} for i, n in enumerate(bl.TOKENISEUR, start=1)}
    poids = {"model-00001-of-00001.safetensors": {"sha256": "a" * 64, "git_sha1": "b" * 40, "taille": 99}}
    att = {n: {"git_sha1": f["git_sha1"], "taille": f["taille"]} for n, f in fich.items()}
    att["model-00001-of-00001.safetensors"] = {"lfs_sha256": "a" * 64, "taille": 99}
    _ecrire(c, "preparer", {})
    _ecrire(c, "telecharger-tokeniseur", {
        "attendus": att, "tokeniseur": fich, "config_neuronpedia": {n: {"git_sha1": h, "taille": 1} for n, h in p2.CONFIG_NEURONPEDIA.items()},
        "lentilles": {"revision": p2.REVISION_NEURONPEDIA, "fichiers": {s: {"chemin": f, "sha256": p2.LENTILLES[s], "taille": 1}
                                                                       for s, f in bl.LENTILLES_FICHIERS.items()}}})
    _ecrire(c, "telecharger-poids", {"poids": poids})
    _ecrire(c, "b0", {"essais": {e: {"code": 0, "resume": "7 passed in 4.8s"} for e in p2.ESSAIS_B0},
                      "lentilles": {s: {"arrets": [], "defauts": [], "autres_cles": "[]", "sortie": "x"} for s in bl.LENTILLES_FICHIERS},
                      "verdicts_b3": {"code": 0, "resume": "35 passed in 0.1s"}})
    d = c.voisin / "data" / "corpus"
    d.mkdir(parents=True)
    (c.diag / "references").mkdir(parents=True, exist_ok=True)
    for t, f in bl.CORPUS_FICHIERS.items():
        n = p2.LIGNES[t]
        (d / f).write_text("".join(f'{{"text": "doc {i}", "id": "{t}-{i}"}}\n' for i in range(n)))
        prov = {"repo": f"depot/{t}", "config": None, "split": "train", "revision": "r" * 40, "skip": 0, "n": n,
                "ids": [f"{t}-{i}" for i in range(n)], "file": f}
        (d / bl.PROVENANCES_PRODUITES[t]).write_text(json.dumps(prov))
        (c.diag / "references" / Path(bl.REFERENCES[t][0]).name).write_text(json.dumps(prov))
    debuts = lambda v: ({t: ({"2": n} if t == "chat" else {"1": n}) for t, n in p2.LIGNES.items()}, {"n": 120000, "sha256": "c" * 64})
    return c, debuts


def test_partie2_bout_en_bout(tmp_path, monkeypatch):
    """Cas sain : l'environnement que l'amorce v4 donne au lanceur (COMMIT_REDUIT, COMMIT_SOURCE, INSTANCE_ID vide) → partie 2 sans
    écart, scellée, fumée permise. Artefact (M1 de la vérification courte) : sans COMMIT_SOURCE → arrêt, partie 2 versée avec l'écart."""
    c, debuts = _partie2_monte(tmp_path)
    monkeypatch.setenv("COMMIT_REDUIT", "d" * 40)
    monkeypatch.delenv("COMMIT_SOURCE", raising=False)
    monkeypatch.setenv("INSTANCE_ID", "")
    with pytest.raises(bl.Arret, match="commit_source illisible"):
        bl.etape_partie2(c, debuts_et_gardes=debuts)
    texte = bl.chemin_partie2(c).read_text(encoding="utf-8")
    assert "commit_source illisible" in texte  # versée avec l'écart, pour le diagnostic
    (tmp_path / "sain").mkdir()
    c2, debuts2 = _partie2_monte(tmp_path / "sain")
    monkeypatch.setenv("COMMIT_SOURCE", "e" * 40)
    r = bl.etape_partie2(c2, debuts_et_gardes=debuts2)
    assert r["ecarts"] == [] and "Aucun." in bl.chemin_partie2(c2).read_text(encoding="utf-8")
    from controle_ia.manifeste import ecrire_resultat
    ecrire_resultat(c2.racine, c2.manifeste, "b-alpha-partie2", r)
    c2.executer = faux_executer([(0, "fumée faite")])
    assert bl.etape_fumee(c2)["code"] == 0


# ------------------------------------------------------------------------------------------------ lot réduit de measure (v3)

@pytest.mark.parametrize("graine", [0, 1])
def test_measure_lot_reduit(tmp_path, graine):
    """`measure` reçoit `--ctx-batch 16` (graine 0 et audit à la graine 1) ; aucun autre paramètre de mesure n'est passé (défauts publiés
    des lignes 374 à 377) ; artefact : une sortie absente est un arrêt."""
    c = bl.Contexte(tmp_path, "r", tmp_path / "hf")
    vus = []

    def ex(cmd, cwd, env, journal, timeout_s):
        vus.append([str(x) for x in cmd])
        f = bl._causal(c, graine)
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(b"x")
        return {"code": 0, "duree_s": 0.1, "fin": []}
    c.executer = ex
    r = bl._measure(c, graine, "measure")
    cmd = vus[0]
    i = cmd.index("--ctx-batch")
    assert cmd[i + 1] == "16" and bl.CTX_BATCH == 16
    assert not {"--per-layer", "--contexts", "--ctx-len", "--top-contexts", "--cond-batch"} & set(cmd)
    assert ("--seed" in cmd) == (graine != 0) and r["causal"]["taille"] == 1
    c.executer = lambda cmd, cwd, env, journal, t: {"code": 0, "duree_s": 0, "fin": []}
    bl._causal(c, graine).unlink()
    with pytest.raises(bl.Arret, match="measure"):
        bl._measure(c, graine, "measure")


# ------------------------------------------------------------------------------------------------ seconde série au lot 64 (v4)

def test_ordre_des_deux_series():
    i = bl.ETAPES.index
    assert i("verdicts") < i("bascule-lot64") < i("measure-lot64") < i("score-lot64") < i("grandeurs-lot64") < i("verdicts-lot64")
    assert bl.PREREQUIS["measure-lot64"] == ("bascule-lot64",) and bl.CTX_BATCH == 16 and bl.CTX_BATCH_LOT64 == 64


def test_audits_requis_par_serie(ctx):
    """L'audit « trop beau » du lot 64 n'est requis que par verdicts-lot64 ; « tout négatif » par l'une ou l'autre série ; la bascule
    attend l'audit « trop beau » du lot 16 s'il est requis (artefact : bascule refusée)."""
    jouer(ctx, "preparer")
    for e in ("telecharger-tokeniseur", "b0", "telecharger-poids", "corpus", "partie2", "fumee", "passe", "b3", "measure", "score",
              "grandeurs"):
        jouer(ctx, e)
    ctx._requis = ["audit-trop-beau"]
    jouer(ctx, "verdicts")
    assert bl.audit_requis(ctx, "audit-trop-beau") and not bl.audit_requis(ctx, "audit-trop-beau-lot64")
    assert not bl.audit_requis(ctx, "audit-tout-negatif")
    assert bl.suite(ctx) == "audit-trop-beau"
    with pytest.raises(bl.Arret, match="trop beau"):
        jouer(ctx, "bascule-lot64")
    jouer(ctx, "audit-trop-beau")
    assert bl.suite(ctx) == "bascule-lot64"
    for e in ("bascule-lot64", "measure-lot64", "score-lot64", "grandeurs-lot64"):
        jouer(ctx, e)
    ctx._requis = []  # le faux verdicts-lot64 rend {"ok": True} : aucun audit
    jouer(ctx, "verdicts-lot64")
    assert bl.suite(ctx) is None


def _mesure_factice(c, graine, contenu=b"lot16"):
    f = bl._causal(c, graine)
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_bytes(contenu)
    return f


def test_bascule_et_measure_lot64(tmp_path):
    """Cas sain : la bascule met de côté les fichiers du lot 16 (graines 0 et 1) sous un nom distinct, empreinte vérifiée ; measure-lot64
    passe `--ctx-batch 64`. Artefacts : fichier du lot 16 absent, cible déjà présente, fichier changé depuis measure, mesure au lot 64
    lancée alors qu'un fichier est en place."""
    c = bl.Contexte(_depot(tmp_path), "20261120-100000-neuron-lens-b-alpha", tmp_path / "hf")
    _ecrire(c, "measure", {"causal": {"sha256": hashlib.sha256(b"lot16").hexdigest()}})  # le manifeste avant les fichiers ignorés
    f0 = _mesure_factice(c, 0)
    _mesure_factice(c, 1, b"graine1")
    vus = []

    def ex(cmd, cwd, env, journal, timeout_s):
        vus.append([str(x) for x in cmd])
        _mesure_factice(c, 0, b"lot64")
        return {"code": 0, "duree_s": 0, "fin": []}
    c.executer = ex
    with pytest.raises(bl.Arret, match="déjà en place"):
        bl.etape_measure_lot64(c)
    r = bl.etape_bascule_lot64(c)
    assert set(r["deplaces"]) == {f0.name, bl._causal(c, 1).name}
    assert (f0.parent / f"{bl.STEM}-causal-lot16.pt").read_bytes() == b"lot16"
    assert (f0.parent / f"{bl.STEM}-causal-seed1-lot16.pt").read_bytes() == b"graine1"
    assert not f0.exists()
    m = bl.etape_measure_lot64(c)
    i = vus[0].index("--ctx-batch")
    assert vus[0][i + 1] == "64" and "--seed" not in vus[0] and m["lot"] == 64
    with pytest.raises(bl.Arret, match="existe déjà"):
        bl.etape_bascule_lot64(c)  # le fichier du lot 64 en place, la cible du lot 16 déjà là


def test_bascule_refuse_fichier_change(tmp_path):
    c = bl.Contexte(_depot(tmp_path), "20261120-100000-neuron-lens-b-alpha", tmp_path / "hf")
    _ecrire(c, "measure", {"causal": {"sha256": "0" * 64}})
    _mesure_factice(c, 0)
    with pytest.raises(bl.Arret, match="pas celui de measure"):
        bl.etape_bascule_lot64(c)


def test_essais_ok_lu_des_resultats(tmp_path):
    """Cas sain : B0, B.3 et fumée passés → vrai ; artefacts : un essai sauté, un B.3 en échec, une fumée au code non nul → faux, avec le
    motif."""
    (tmp_path / "a").mkdir()
    c = bl.Contexte(_depot(tmp_path / "a"), "20261120-100000-neuron-lens-b-alpha", tmp_path / "hf")
    sain = {"code": 0, "resume": "7 passed in 1s"}
    b0 = {"essais": {e: dict(sain) for e in p2.ESSAIS_B0}, "lentilles": {s: {"arrets": [], "defauts": []} for s in bl.LENTILLES_FICHIERS},
          "verdicts_b3": dict(sain)}
    _ecrire(c, "b0", b0)
    _ecrire(c, "b3", {"verdicts_b3": dict(sain)})
    _ecrire(c, "fumee", {"code": 0})
    assert bl.essais_ok(c) == (True, [])
    for etape, contenu, motif in (
            ("b0", b0 | {"essais": b0["essais"] | {p2.ESSAIS_B0[0]: {"code": 0, "resume": "6 passed, 1 skipped in 1s"}}}, "essai"),
            ("b3", {"verdicts_b3": {"code": 1, "resume": "1 failed, 34 passed"}}, "B.3 avant measure"),
            ("fumee", {"code": 2}, "fumée")):
        d = tmp_path / etape
        d.mkdir()
        c2 = bl.Contexte(_depot(d), "20261120-100000-neuron-lens-b-alpha", tmp_path / "hf")
        _ecrire(c2, "b0", contenu if etape == "b0" else b0)
        _ecrire(c2, "b3", contenu if etape == "b3" else {"verdicts_b3": dict(sain)})
        _ecrire(c2, "fumee", contenu if etape == "fumee" else {"code": 0})
        ok, pb = bl.essais_ok(c2)
        assert ok is False and any(motif in p for p in pb), (etape, pb)


@pytest.mark.parametrize("graine", [0, 1])
def test_audit_lot64_lot_passe(tmp_path, graine):
    """L'audit « trop beau » du lot 64 mesure à la graine 1 au lot 64 (et le lot 16 reste celui de la première série)."""
    c = bl.Contexte(tmp_path, "r", tmp_path / "hf")
    vus = []

    def ex(cmd, cwd, env, journal, t):
        vus.append([str(x) for x in cmd])
        _mesure_factice(c, 1)
        return {"code": 0, "duree_s": 0, "fin": []}
    c.executer = ex
    lot = (bl.CTX_BATCH, bl.CTX_BATCH_LOT64)[graine]
    r = bl._measure(c, 1, "audit", lot)
    assert vus[0][vus[0].index("--ctx-batch") + 1] == str(lot) and r["lot"] == lot


# ------------------------------------------------------------------------------------------------ v5 : contre-lecture de la commande v6

REF_QWEN = Path(__file__).resolve().parents[1] / "docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/causal_lens_qwen3-8b.json"


def _ctx_verdicts(tmp_path, b7_haut=False, fumee=0):
    """Contexte avec de vrais résultats de B0, B.3, fumée, grandeurs (n = 64 partout) et un vrai résumé de `score` aux deux séries,
    tiré de la référence publiée convertie (cas sain : B-2, B-3, B-7 « reproduit »)."""
    from controle_ia.neuron_lens import verdicts_b_alpha_v3 as vb
    c = bl.Contexte(_depot(tmp_path), "20261120-100000-neuron-lens-b-alpha", tmp_path / "hf")
    sain = {"code": 0, "resume": "7 passed in 1s"}
    _ecrire(c, "b0", {"essais": {e: dict(sain) for e in p2.ESSAIS_B0},
                      "lentilles": {s: {"arrets": [], "defauts": []} for s in bl.LENTILLES_FICHIERS}, "verdicts_b3": dict(sain)})
    _ecrire(c, "b3", {"verdicts_b3": dict(sain)})
    _ecrire(c, "fumee", {"code": fumee})
    t = vb.depuis_reference_qwen(json.loads(REF_QWEN.read_text())["targets"])
    if b7_haut:
        for l in range(8, 16):
            t["ablate win"]["npR"]["r_med"][l] = 0.5
    n = {cb: [64] * 32 for cb in vb.CIBLES}
    for tag, gr in (("", "grandeurs"), ("lot64", "grandeurs-lot64")):
        (c.diag / bl._resume(c, tag).name).write_text(json.dumps({"targets": t}))
        _ecrire(c, gr, {"n": n})
    poles = [{"couche": l, "aleatoire": True, "lectures": {"steer 1x": {s: {"r": 0.5, "motif": "retenu"} for s in ("npR", "logit")}}}
             for l in range(32) for _ in range(8)]
    for f in ("grandeurs-par-pole-b-alpha-v1.json", "grandeurs-par-pole-b-alpha-lot64-v1.json"):
        (c.diag / f).write_text(json.dumps({"poles": poles}))
    from controle_ia.manifeste import lire_manifeste
    man, _ = lire_manifeste(c.manifeste)
    if "b-alpha-intervalles-lot64" not in man["graines"]:
        pytest.skip("manifeste de l'essai sans la tâche lot64")
    return c


def _ecrire_v5(ctx, etape, contenu):
    from controle_ia.manifeste import creer_manifeste, ecrire_resultat
    if not ctx.manifeste.exists():
        creer_manifeste(ctx.racine, ctx.run_id, {"essai": 1}, ["b-alpha-intervalles", "b-alpha-intervalles-lot64"],
                        entropie=bl.ENTROPIE)
    ecrire_resultat(ctx.racine, ctx.manifeste, f"b-alpha-{etape}", contenu)


@pytest.fixture
def v5(monkeypatch):
    monkeypatch.setitem(globals(), "_ecrire", _ecrire_v5)


def test_verdicts_vrais_deux_series_cas_sain(tmp_path, v5):
    c = _ctx_verdicts(tmp_path)
    a, b = bl.etape_verdicts(c), bl.etape_verdicts_lot64(c)
    for r in (a, b):
        assert r["audits_requis"] == [] and r["audit_b7_par_le_haut"] is False and r["essais_ok"] is True
        assert r["verdict"]["b7"]["verdict"] == "reproduit"
    assert a["lot"] == 16 and b["intervalles"]["fichier"] == "grandeurs-par-pole-b-alpha-lot64-v1.json"
    assert a["intervalles"]["fichier"] == "grandeurs-par-pole-b-alpha-v1.json"


def test_b7_par_le_haut_requiert_l_audit(tmp_path, v5):
    """Artefact B1 : « ablate win » de npR à 0,50 aux couches 8 à 15 → B-7 « non reproduit » par le haut → audit « trop beau » requis
    (graine 1, même série), chaîne versée telle quelle ; la v4 la perdait."""
    c = _ctx_verdicts(tmp_path, b7_haut=True)
    r = bl.etape_verdicts_lot64(c)
    assert r["audit_b7_par_le_haut"] is True and r["audits_requis"] == ["audit-trop-beau"]
    assert any(m.startswith("B-7") for m in r["motifs_audit"])
    from controle_ia.manifeste import ecrire_resultat
    ecrire_resultat(c.racine, c.manifeste, "b-alpha-verdicts-lot64", r)
    assert bl.audit_requis(c, "audit-trop-beau-lot64") and not bl.audit_requis(c, "audit-trop-beau")


def test_essais_ok_faux_dans_le_vrai_verdict(tmp_path, v5):
    c = _ctx_verdicts(tmp_path, fumee=2)
    r = bl.etape_verdicts(c)
    assert r["essais_ok"] is False and r["essais_en_defaut"] == ["fumée"]
    assert r["verdict"]["verdict"].startswith("chaîne en défaut")


def test_motif_inconnu_arrete(tmp_path, v5, monkeypatch):
    from controle_ia.neuron_lens import verdicts_b_alpha_v3 as vb
    c = _ctx_verdicts(tmp_path)
    vrai = vb.verdict

    def faux(*a, **k):
        v = vrai(*a, **k)
        v.audit_requis.append("motif nouveau")
        return v
    monkeypatch.setattr(vb, "verdict", faux)
    with pytest.raises(bl.Arret, match="motif d'audit inconnu"):
        bl.etape_verdicts(c)


def _ctx_mesure(tmp_path):
    c = bl.Contexte(_depot(tmp_path), "20261120-100000-neuron-lens-b-alpha", tmp_path / "hf")
    _ecrire(c, "measure", {"causal": {"sha256": hashlib.sha256(b"lot16").hexdigest()}})
    return c


def test_bascule_idempotente(tmp_path):
    """Arrêt après le renommage de la graine 0, avant celui de la graine 1 et avant le résultat : la reprise finit sans geste manuel."""
    c = _ctx_mesure(tmp_path)
    f0 = _mesure_factice(c, 0)
    _mesure_factice(c, 1, b"graine1")
    f0.rename(f0.with_name(f"{bl.STEM}-causal-lot16.pt"))
    r = bl.etape_bascule_lot64(c)
    assert r["deplaces"][f0.name]["deja_fait"] is True and "deja_fait" not in r["deplaces"][bl._causal(c, 1).name]
    assert bl.etape_bascule_lot64(c)["deplaces"][f0.name]["deja_fait"] is True  # rejouée entière : idempotente


def test_bascule_gardes_fichier(tmp_path):
    c = _ctx_mesure(tmp_path)
    with pytest.raises(bl.Arret, match="lot 16 absent"):
        bl.etape_bascule_lot64(c)
    f0 = _mesure_factice(c, 0, b"autre")
    with pytest.raises(bl.Arret, match="n'est pas celui de measure"):
        bl.etape_bascule_lot64(c)
    assert f0.exists() and not f0.with_name(f"{bl.STEM}-causal-lot16.pt").exists()  # rien n'est déplacé avant le contrôle
    f0.unlink()
    f0.with_name(f"{bl.STEM}-causal-lot16.pt").write_bytes(b"autre")
    with pytest.raises(bl.Arret, match="déjà mis de côté n'est pas celui"):
        bl.etape_bascule_lot64(c)


def test_measure_lot64_reprend_un_fichier_partiel(tmp_path):
    c = _ctx_mesure(tmp_path)
    _mesure_factice(c, 0)
    bl.etape_bascule_lot64(c)
    _mesure_factice(c, 0, b"partiel-lot64")

    def ex(cmd, cwd, env, journal, t):
        _mesure_factice(c, 0, b"lot64")
        return {"code": 0, "duree_s": 0, "fin": []}
    c.executer = ex
    r = bl.etape_measure_lot64(c)
    assert r["fichier_partiel_retire_sha256"] == hashlib.sha256(b"partiel-lot64").hexdigest() and r["lot"] == 64
    assert bl._causal(c, 0).read_bytes() == b"lot64"


def test_measure_lot64_refuse_le_fichier_du_lot16(tmp_path):
    c = _ctx_mesure(tmp_path)
    f0 = _mesure_factice(c, 0)
    f0.with_name(f"{bl.STEM}-causal-lot16.pt").write_bytes(b"lot16")  # copie, pas renommage : le fichier du lot 16 est encore en place
    with pytest.raises(bl.Arret, match="bascule non faite"):
        bl.etape_measure_lot64(c)


def test_grandeurs_refuse_fichier_absent(tmp_path):
    c = _ctx_mesure(tmp_path)
    with pytest.raises(bl.Arret, match="fichier de mesure absent"):
        bl.etape_grandeurs_lot64(c, calculer=lambda *a: ({}, []))


@pytest.mark.parametrize("requis16,requis64,attendu", [
    ([], ["audit-trop-beau"], ["bascule-lot64", "measure-lot64", "score-lot64", "grandeurs-lot64", "verdicts-lot64",
                               "audit-trop-beau-lot64"]),
    ([], ["audit-tout-negatif"], ["bascule-lot64", "measure-lot64", "score-lot64", "grandeurs-lot64", "verdicts-lot64",
                                  "audit-tout-negatif"]),
    (["audit-tout-negatif"], [], ["audit-tout-negatif", "bascule-lot64", "measure-lot64", "score-lot64", "grandeurs-lot64",
                                  "verdicts-lot64"]),
])
def test_ordre_des_audits_par_serie(ctx, monkeypatch, requis16, requis64, attendu):
    def faux(etape):
        def f(ctx_):
            if etape == "verdicts":
                return {"audits_requis": requis16}
            if etape == "verdicts-lot64":
                return {"audits_requis": requis64}
            return {"ok": True}
        return f
    monkeypatch.setattr(bl, "ETAPE_FONCTIONS", bl.ETAPE_FONCTIONS | {e: faux(e) for e in ("verdicts", "verdicts-lot64")})
    jouer(ctx, "preparer")
    for e in ("telecharger-tokeniseur", "b0", "telecharger-poids", "corpus", "partie2", "fumee", "passe", "b3", "measure", "score",
              "grandeurs", "verdicts"):
        jouer(ctx, e)
    vus = []
    while (e := bl.suite(ctx)) is not None:
        vus.append(e)
        jouer(ctx, e)
    assert vus == attendu
