"""Essais de SPARKS-EXP7-NUL, v3 (contre-lecture du delta v2) : a priori de B3 au construit inversé, secondaire « sur M5 »,
jetons du format de conversation, ordres de redémarrage et lots de copie, minuterie de destruction (bash et `curl`
seuls, `curl` et `vastai` simulés par des exécutables d'essai : aucun réseau), amorce v3 (création, refus, redémarrage
sur ordre écrit) contre un dépôt d'essai local. Chaque garde neuve sur un cas sain et sur un artefact (R5)."""
from __future__ import annotations

import copy
import json
import os
import re
import shutil
import signal
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pytest

torch = pytest.importorskip("torch")
pytest.importorskip("transformers")

from controle_ia.sparks_exp7_nul_v1 import jouet  # noqa: E402
from controle_ia.sparks_exp7_nul_v2 import aveugle, consignes, depense, outil_attention  # noqa: E402
from controle_ia.sparks_exp7_nul_v3 import analyse, bases, garde_code, instance, plan, redemarrage  # noqa: E402

RACINE = Path(__file__).resolve().parents[1]
AMORCE = RACINE / "scripts" / "amorce_instance_sparks_exp7_nul_v3.sh"
L_BASE = ("| GO-2026-11-04-04 | 2026-11-04 | calcul | SPARKS-EXP7-NUL, variante carte | 25 USD | 2026-11-18 | Lazar | mot |")
L_EXT = ("| GO-2026-11-04-04 | 2026-11-04 | calcul | extension : SPARKS-EXP7-NUL, addendum | 40 USD | 2026-11-18 | Lazar | mot |")


# --- 1. a priori de B3 au construit inversé ---------------------------------------------------------------------------
ROLES = {f"h{i}": "honest" for i in range(4)} | {f"s{i}": "sycophant" for i in range(4)}


def test_orientation_b3_a_priori_inverse_et_garde():
    egal = {m: 1.0 for m in ROLES}
    assert bases.orientation_b3(egal, ROLES)["o3"] == 1
    assert bases.orientation_b3(egal, ROLES, a_priori=-1)["o3"] == -1          # égalité : a priori gardé (−1)
    proche_syc = {m: (1.0 if r == "sycophant" else 2.0) for m, r in ROLES.items()}
    assert bases.orientation_b3(proche_syc, ROLES)["o3"] == 1
    assert bases.orientation_b3(proche_syc, ROLES, a_priori=-1)["o3"] == 1      # les données renversent l'a priori −1
    proche_hon = {m: (2.0 if r == "sycophant" else 1.0) for m, r in ROLES.items()}
    assert bases.orientation_b3(proche_hon, ROLES, a_priori=-1)["o3"] == -1
    assert bases.orientation_b3(proche_hon, ROLES)["o3"] == -1
    with pytest.raises(ValueError):
        bases.orientation_b3(egal, ROLES, a_priori=0)


def test_a_priori_transmis_par_l_instance(monkeypatch):
    vu = {}
    monkeypatch.setattr(bases, "etalonnage_b3_b4", lambda *a, **k: vu.setdefault("a_priori", k["a_priori"]))
    m, _, _ = jouet.depart_jouet()
    instance.bases_etalonnage(Path("."), {"modeles": {}, "construit": "construit inversé"}, m, est_gemma=False)
    assert vu.pop("a_priori") == -1
    instance.bases_etalonnage(Path("."), {"modeles": {}, "construit": "normal"}, m, est_gemma=False)
    assert vu.pop("a_priori") == 1


# --- 2. secondaire « sur M5 » ------------------------------------------------------------------------------------------
def _cle():
    cle = {}
    for t, n in (("vraie", 24), ("hh", 12), ("ss", 12)):
        for i in range(n):
            r1, r2 = {"vraie": ("honest", "sycophant"), "hh": ("honest", "honest"), "ss": ("sycophant", "sycophant")}[t]
            a, b = f"{t}{i}-1", f"{t}{i}-2"
            cle[f"cas_{t}{i:02d}"] = {"cas": f"{t}{i:02d}", "type": t, "A": a, "B": b, "roles": {a: r1, b: r2}}
    return cle


def test_secondaire_m5_par_c_base_et_lecteur():
    cle = _cle()
    rng = np.random.default_rng(3)
    par_cas = {k["cas"]: {"p": {m: float(r == "sycophant") for m, r in k["roles"].items()}, "type": k["type"],
                          "roles": k["roles"], "A": k["A"], "B": k["B"]} for k in cle.values()}
    base = {m: float(rng.normal()) for k in cle.values() for m in k["roles"]}
    r = analyse.m5_secondaire(par_cas, base)
    assert r["M5_lecteur"] == 1.0 and r["n_ss"] == 12 and r["n_hh"] == 12 and 0 <= r["M5_par_base"] <= 1
    assert r["M5_par_c"] > r["M5_par_base"] and r["M5_par_c"] != r["M5_lecteur"]
    sans_hh = {c: v for c, v in par_cas.items() if v["type"] != "hh"}
    assert analyse.m5_secondaire(sans_hh, base)["M5_par_c"] is None


def test_analyser_v3_ajoute_m5_sans_changer_les_tirages():
    from controle_ia.sparks_exp7_nul_v2 import analyse as a2
    cle = _cle()
    lat = {m: float(np.random.default_rng(5).normal()) + (1.5 if r == "sycophant" else 0) for k in cle.values()
           for m, r in k["roles"].items()}
    bp = {nom: {X: {"d": -lat[k[X]], "n": 100 - lat[k[X]]} for X in ("A", "B")} for nom, k in cle.items()}
    roles = {f"e{i}": ("sycophant" if i < 4 else "honest") for i in range(8)}
    sc = {m: {"d": (1.0 if r == "sycophant" else 2.0) + 0.1 * i, "n": 10.0 + i} for i, (m, r) in enumerate(roles.items())}
    etal = {"scores": sc, "roles": roles, "B3": bases.orientation_b3({m: v["d"] for m, v in sc.items()}, roles)}
    reps = [{"lecteur": l, "cas": nom, "statut": "repondu", "infraction": False, "variante": "principal",
             "reponse": {"p_A": float(k["roles"][k["A"]] == "sycophant"), "p_B": float(k["roles"][k["B"]] == "sycophant"),
                         "composants": []}} for nom, k in cle.items() for l in ("opus", "fable")]
    gens = lambda: {t: np.random.default_rng(i) for i, t in enumerate(plan.TACHES_NEUVES)}   # noqa: E731
    r2 = a2.analyser(reps, cle, ("opus", "fable"), np.random.default_rng(0), gens(), bases_poids=bp, etal=etal, n_boot=40, n_perm=40)
    r3 = analyse.analyser(reps, cle, ("opus", "fable"), np.random.default_rng(0), gens(), bases_poids=bp, etal=etal, n_boot=40, n_perm=40)
    assert r3["principal"]["increment"]["B3"]["ic95"] == r2["principal"]["increment"]["B3"]["ic95"]
    assert r3["increment_secondaire"]["B3"]["m5"]["M5_lecteur"] == 1.0 and "m5" not in r2["increment_secondaire"]["B3"]


# --- 3. jetons du format de conversation (secours) -------------------------------------------------------------------
def _ids(x):
    return list(x["input_ids"]) if isinstance(x, dict) or hasattr(x, "keys") else list(x)


def test_jetons_de_l_outil_egaux_au_gabarit_tokenise():
    _, tok, _ = jouet.depart_jouet()
    msg = "What is two plus three ?"
    for t in (tok, _sans_debut(tok)):
        fmt = json.loads(consignes.format_conversation(t))
        assert "{message}" in fmt
        outil = outil_attention.jetons_texte(t, fmt.replace("{message}", msg))
        gab = _ids(t.apply_chat_template([{"role": "user", "content": msg}], tokenize=True, add_generation_prompt=True))
        assert outil == gab
    # artefact : format gardé avec le jeton de début (sortie brute du gabarit) → un jeton de début de trop
    brut = tok.apply_chat_template([{"role": "user", "content": "{message}"}], tokenize=False, add_generation_prompt=True)
    gab = _ids(tok.apply_chat_template([{"role": "user", "content": msg}], tokenize=True, add_generation_prompt=True))
    assert outil_attention.jetons_texte(tok, brut.replace("{message}", msg)) != gab


def _sans_debut(tok):
    t = copy.deepcopy(tok)
    t.chat_template = jouet.GABARIT_CONVERSATION.replace("{{ bos_token }}", "")
    t.bos_token = None
    return t


# --- 4. ordres de redémarrage et lots -----------------------------------------------------------------------------------
def _ordre(d: Path, n: int, **o) -> Path:
    p = d / f"ordre-{n:03d}.json"
    p.write_text(json.dumps({"numero": n, **o}), encoding="utf-8")
    return p


def test_ordres_sains_et_artefacts(tmp_path):
    ok = [("copie", dict(phase="copie", deja_usd=3.5, cas=["vraie01", "hh02"], premier=True, copie_minutes=20)),
          ("causal", dict(phase="causal", deja_usd=20)), ("fin", dict(phase="fin", deja_usd=0))]
    for i, (_, o) in enumerate(ok, 1):
        assert redemarrage.lire_ordre(_ordre(tmp_path, i, **o))["phase"] == o["phase"]
    mauvais = [dict(phase="arret", deja_usd=1), dict(phase="fin", deja_usd=-1), dict(phase="fin", deja_usd=1, autre=2),
               dict(phase="copie", deja_usd=1, cas=["vraie01"], premier=True, copie_minutes=61),
               dict(phase="copie", deja_usd=1, cas=["../x"], premier=True, copie_minutes=10),
               dict(phase="copie", deja_usd=1, cas=["vraie01"] * 5, premier=False, copie_minutes=10),
               dict(phase="copie", deja_usd=1, cas=["vraie01"], premier="oui", copie_minutes=10)]
    for j, o in enumerate(mauvais, 10):
        with pytest.raises(redemarrage.GardeOrdre):
            redemarrage.lire_ordre(_ordre(tmp_path, j, **o))
    (tmp_path / "ordre-020.json").write_text(json.dumps({"numero": 21, "phase": "fin", "deja_usd": 0}))
    with pytest.raises(redemarrage.GardeOrdre, match="numéro"):
        redemarrage.lire_ordre(tmp_path / "ordre-020.json")


def test_ordre_deja_fait_refuse_et_dernier_ordre(tmp_path):
    for i in (1, 2, 3):
        _ordre(tmp_path, i, phase="fin", deja_usd=0)
    assert redemarrage.dernier_ordre(tmp_path).name == "ordre-003.json"
    faits = tmp_path / "faits.txt"
    o = redemarrage.lire_ordre(redemarrage.dernier_ordre(tmp_path))
    redemarrage.exiger_nouveau(o, faits)
    redemarrage.marquer_fait(faits, 3)
    with pytest.raises(redemarrage.GardeOrdre, match="déjà"):
        redemarrage.exiger_nouveau(o, faits)
    with pytest.raises(redemarrage.GardeOrdre):
        redemarrage.dernier_ordre(tmp_path / "vide")
    assert redemarrage.main(["verifier", str(tmp_path), str(faits)]) == 2


def _sortie_fab(d: Path) -> Path:
    s = d / "sortie"
    fab = {"cas": {"vraie01": {"ok": True, "modeles": {"vraie01-h": "vraie01-h", "vraie01-s": "vraie01-s-r1"}},
                   "hh02": {"ok": False, "modeles_remplacement": {"res-hh1-h1": "res-hh1-h1", "res-hh1-h2": "res-hh1-h2"}},
                   "ss03": {"ok": False, "modeles_remplacement": None}},
           "modeles": {f"etal-e1-{x}": {"final": f"etal-e1-{x}"} for x in ("h1", "h2", "s1", "s2")}}
    for mid in ("vraie01-h", "vraie01-s-r1", "res-hh1-h1", "res-hh1-h2", "etal-e1-h1", "etal-e1-s1", "etal-e1-h2"):
        f = s / "modeles" / mid / "final" / "couches.safetensors"
        f.parent.mkdir(parents=True)
        f.write_bytes(mid.encode() * 10)
    (s / "fabrication-v1.json").write_text(json.dumps(fab))
    (s / "fabrication-complement-v2.json").write_text("{}")
    (s / "couches-depart-v1.safetensors").write_bytes(b"depart")
    return s


def test_lot_de_copie_liens_manifeste_et_gardes(tmp_path):
    s = _sortie_fab(tmp_path)
    o = redemarrage.lire_ordre(_ordre(tmp_path, 4, phase="copie", deja_usd=1, cas=["vraie01", "hh02", "pilote-vraie"],
                                      premier=True, copie_minutes=10))
    d = redemarrage.preparer_lot(o, s, tmp_path / "lots")
    assert d.name == "lot-004"
    f = d / "modeles" / "vraie01-s-r1" / "final" / "couches.safetensors"
    assert f.stat().st_ino == (s / "modeles" / "vraie01-s-r1" / "final" / "couches.safetensors").stat().st_ino  # lien en dur
    assert (d / "couches-depart-v1.safetensors").exists() and (d / "modeles" / "etal-e1-s1").exists()
    r = subprocess.run(["sha256sum", "-c", "--quiet", "MANIFESTE-LOT.txt"], cwd=d, capture_output=True)
    assert r.returncode == 0 and len((d / "MANIFESTE-LOT.txt").read_text().splitlines()) == 9
    with pytest.raises(redemarrage.GardeOrdre, match="R12"):
        redemarrage.preparer_lot(o, s, tmp_path / "lots")
    o2 = redemarrage.lire_ordre(_ordre(tmp_path, 5, phase="copie", deja_usd=1, cas=["ss03"], premier=False, copie_minutes=10))
    with pytest.raises(redemarrage.GardeOrdre, match="bornes"):
        redemarrage.preparer_lot(o2, s, tmp_path / "lots")
    o3 = redemarrage.lire_ordre(_ordre(tmp_path, 6, phase="copie", deja_usd=1, cas=["vraie09"], premier=False, copie_minutes=10))
    with pytest.raises(redemarrage.GardeOrdre, match="absent"):
        redemarrage.preparer_lot(o3, s, tmp_path / "lots")


# --- 5. minuterie de destruction (bash, curl simulé) ----------------------------------------------------------------------
def _faux_bin(d: Path) -> Path:
    b = d / "faux-bin"
    b.mkdir(exist_ok=True)
    (b / "curl").write_text('#!/bin/bash\necho "curl $*" >> "$FAUX_JOURNAL"\nprintf %s "${FAUX_HTTP:-200}"\n')
    (b / "vastai").write_text('#!/bin/bash\necho "vastai $*" >> "$FAUX_JOURNAL"\necho SORTIE-BRUTE-SECRETE\nexit "${FAUX_VASTAI:-0}"\n')
    for f in b.iterdir():
        f.chmod(0o755)
    return b


def _script_minuterie(d: Path) -> Path:
    t = AMORCE.read_text(encoding="utf-8")
    m = re.search(r"<<'MINUTERIE'\n(.*?)\nMINUTERIE\n", t, re.S)
    assert m, "minuterie absente de l'amorce"
    p = d / "minuterie.sh"
    p.write_text(m.group(1) + "\n")
    return p


def _env(d: Path, **kw) -> dict:
    e = {"PATH": f"{_faux_bin(d)}:/usr/bin:/bin", "HOME": str(d), "FAUX_JOURNAL": str(d / "faux.log"),
         "CONTAINER_ID": "123456", "CONTAINER_API_KEY": "cle-factice", "MINUTERIE_PAS_S": "1",
         "MINUTERIE_REESSAI_S": "1", "MINUTERIE_MARGE_S": "4"}
    e.update({k: str(v) for k, v in kw.items()})
    return e


def _minuterie(d, ech, **kw):
    return subprocess.run(["bash", str(_script_minuterie(d)), str(ech), str(d), "https://exemple.invalid/api"],
                          env=_env(d, **kw), capture_output=True, text=True, timeout=60)


def test_minuterie_detruit_a_l_echeance_par_l_identifiant(tmp_path):
    r = _minuterie(tmp_path, int(time.time()) + 1)
    assert r.returncode == 0
    j = (tmp_path / "faux.log").read_text()
    assert "-X DELETE" in j and "https://exemple.invalid/api/instances/123456/" in j and "vastai" not in j
    log = (tmp_path / "sparks-v3-minuterie.log").read_text()
    assert "HTTP 200" in log and "détruite" in log and "cle-factice" not in log


def test_minuterie_ordre_de_la_machine_avant_l_echeance(tmp_path):
    (tmp_path / "sparks-v3-detruire").write_text("fin du contrôle causal")
    t0 = time.time()
    r = _minuterie(tmp_path, int(time.time()) + 3600)
    assert r.returncode == 0 and time.time() - t0 < 20 and "ordre de la machine" in (tmp_path / "sparks-v3-minuterie.log").read_text()


def test_minuterie_repli_vastai_avec_y_et_sans_sortie_brute(tmp_path):
    r = _minuterie(tmp_path, int(time.time()), FAUX_HTTP="500", FAUX_VASTAI="0")
    assert r.returncode == 0
    j = (tmp_path / "faux.log").read_text()
    assert "vastai destroy instance 123456 -y" in j
    log = (tmp_path / "sparks-v3-minuterie.log").read_text()
    assert "HTTP 500" in log and "code 0" in log and "SORTIE-BRUTE-SECRETE" not in log + r.stdout + r.stderr


def test_minuterie_recommence_puis_alarme_sans_jamais_arreter(tmp_path):
    r = _minuterie(tmp_path, int(time.time()), FAUX_HTTP="503", FAUX_VASTAI="1")
    assert r.returncode == 4
    log = (tmp_path / "sparks-v3-minuterie.log").read_text()
    assert log.count("DELETE instance 123456") >= 2 and "ALARME" in log
    assert "stop" not in (tmp_path / "faux.log").read_text()


def test_minuterie_identifiant_illisible_aucun_geste(tmp_path):
    r = _minuterie(tmp_path, int(time.time()), CONTAINER_ID="12; rm -rf /")
    assert r.returncode == 3 and not (tmp_path / "faux.log").exists()


def test_aucun_arret_de_machine_dans_les_scripts_v3():
    for f in ("amorce_instance_sparks_exp7_nul_v3.sh", "sparks_exp7_nul_instance_v3.sh", "lancer_sparks_exp7_nul_v3.sh"):
        t = (RACINE / "scripts" / f).read_text(encoding="utf-8")
        assert not re.search(r"vastai\s+stop|/stop|\"state\"\s*:\s*\"stopped\"", t), f
        assert all("-y" in l for l in t.splitlines() if "vastai destroy" in l), f


# --- 6. amorce v3 contre un dépôt d'essai local ---------------------------------------------------------------------------
def _git(d, *a):
    return subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True, text=True).stdout.strip()


@pytest.fixture
def depot_essai(tmp_path):
    d = tmp_path / "depot"
    (d / "registres").mkdir(parents=True)
    (d / "registres" / "go.md").write_text("| id | a | b | c | d | e | f | g |\n|---|---|---|---|---|---|---|---|\n"
                                           + L_BASE + "\n" + L_EXT + "\n")
    for v, fs in (("sparks_exp7_nul_v2", ("go.py", "depense.py", "garde_code.py")),
                  ("sparks_exp7_nul_v3", ("garde_code.py", "redemarrage.py"))):
        (d / "src" / "controle_ia" / v).mkdir(parents=True, exist_ok=True)
        for f in fs:
            shutil.copy(RACINE / "src" / "controle_ia" / v / f, d / "src" / "controle_ia" / v / f)
    (d / "scripts").mkdir()
    (d / "scripts" / "sparks_exp7_nul_instance_v3.sh").write_text(
        '#!/bin/bash\necho "INSTANCE FACTICE $PHASE $CLE" >> "$FAUX_JOURNAL"\nmkdir -p "$TRAVAIL"\n'
        '[ -n "${FAUX_POUSSEE:-}" ] && echo tete > "$TRAVAIL/POUSSEE-VERIFIEE"\nexit 0\n')
    _git(d, "init", "-q", "-b", "main")
    _git(d, "config", "user.email", "t@example.invalid")
    _git(d, "config", "user.name", "t")
    _git(d, "config", "uploadpack.allowFilter", "true")
    _git(d, "config", "uploadpack.allowAnySHA1InWant", "true")
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "essai")
    return d, _git(d, "rev-parse", "HEAD")


def _ordres(depot: Path, ordres: list[dict], causal: bool = False):
    _git(depot, "checkout", "-q", "-B", plan.BRANCHE_ORDRES)
    (depot / "ordres").mkdir(exist_ok=True)
    for o in ordres:
        (depot / "ordres" / f"ordre-{o['numero']:03d}.json").write_text(json.dumps(o))
    if causal:
        (depot / "ordres" / "causal" / "reponses").mkdir(parents=True, exist_ok=True)
        (depot / "ordres" / "causal" / "cle-ouverte-v1.json").write_text("{}")
    _git(depot, "add", "-A")
    _git(depot, "commit", "-q", "-m", "ordres")
    _git(depot, "checkout", "-q", "main")


def _amorce(tmp_path, depot, commit, *, timeout=90, **kw):
    r_ = tmp_path / "racine"
    r_.mkdir(exist_ok=True)
    env = _env(tmp_path, RACINE_AMORCE=r_, DEPOT_URL=f"file://{depot}", COMMIT=commit, COMMIT_CODE=commit,
               GH_TOKEN="x", PRIX_HEURE_USD="0.8", PRIX_STOCKAGE_HEURE_USD="0.05", GO_DATE="2026-11-04",
               ECHEANCE_UTC_S=int(time.time()) + 3600)
    env.update({k: str(v) for k, v in kw.items()})
    env = {k: v for k, v in env.items() if v != "∅"}
    try:
        r = subprocess.run(["bash", str(AMORCE)], env=env, capture_output=True, text=True, timeout=timeout)
        out, code = r.stdout + r.stderr, r.returncode
    except subprocess.TimeoutExpired as e:
        out, code = ((e.stdout or b"").decode() if isinstance(e.stdout, bytes) else (e.stdout or "")), "délai"
    return code, out, r_


def _arreter_minuterie(r_: Path):
    p = r_ / "sparks-v3-minuterie.pid"
    if p.exists():
        try:
            os.kill(int(p.read_text().strip()), signal.SIGTERM)      # R10 : par son identifiant de processus
        except (ProcessLookupError, ValueError):
            pass


def test_amorce_refuse_sans_curl(tmp_path, depot_essai):
    sans = tmp_path / "sans-curl"
    sans.mkdir()
    for x in Path("/usr/bin").iterdir():
        if x.name != "curl":
            (sans / x.name).symlink_to(x)
    code, out, r_ = _amorce(tmp_path, *depot_essai, PATH=str(sans))
    assert code == 2 and "curl absent" in out and not (r_ / "sparks-v3-minuterie.sh").exists()


def test_amorce_refuse_sans_echeance(tmp_path, depot_essai):
    code, out, r_ = _amorce(tmp_path, *depot_essai, ECHEANCE_UTC_S="∅")
    assert code == 2 and "ECHEANCE_UTC_S" in out and not (r_ / "sparks-v3-minuterie.sh").exists()


def test_amorce_apres_echeance_detruit_sans_calcul(tmp_path, depot_essai):
    code, out, r_ = _amorce(tmp_path, *depot_essai, ECHEANCE_UTC_S=int(time.time()) - 5)
    assert code == 0 and "aucun calcul" in out and not (r_ / "amorce-depot").exists()
    assert "DELETE instance 123456" in (r_ / "sparks-v3-minuterie.log").read_text()


def test_amorce_echeance_bornee_a_la_fin_du_go(tmp_path, depot_essai):
    code, out, r_ = _amorce(tmp_path, *depot_essai, ECHEANCE_UTC_S=1895046400, COMMIT="0" * 40)
    _arreter_minuterie(r_)
    assert (r_ / "sparks-v3-echeance.txt").read_text().strip() == str(plan.FIN_ECHEANCE_UTC_S)


@pytest.mark.parametrize("cas,attendu", [
    ("go", "non conforme (base et extension"),
    ("duree", "plafond trop bas"),
    ("code", "code ou addendum non conformes"),
])
def test_amorce_refus_avant_tout_calcul(tmp_path, depot_essai, cas, attendu):
    d, c = depot_essai
    kw = {}
    if cas == "go":
        (d / "registres" / "go.md").write_text("| id | a | b | c | d | e | f | g |\n" + L_BASE + "\n")
        _git(d, "commit", "-qam", "sans extension")
        c = _git(d, "rev-parse", "HEAD")
    if cas == "duree":
        kw["DEJA_USD"] = "39.99"
    code, out, r_ = _amorce(tmp_path, d, c, **kw)
    _arreter_minuterie(r_)
    assert code == 2 and attendu in out, out
    assert (r_ / "sparks-v3-minuterie.sh").exists() and out.index("minuterie lancée") < out.index(attendu)
    assert "INSTANCE FACTICE" not in ((tmp_path / "faux.log").read_text() if (tmp_path / "faux.log").exists() else "")


def _disque_existant(tmp_path, depot, commit):
    r_ = tmp_path / "racine"
    r_.mkdir(exist_ok=True)
    subprocess.run(["git", "clone", "-q", str(depot), str(r_ / "amorce-depot")], check=True)
    _git(r_ / "amorce-depot", "checkout", "-q", commit)
    (r_ / "sparks-v3-echeance.txt").write_text(str(int(time.time()) + 3600) + "\n")
    return r_


def test_redemarrage_ordre_fin_puis_ordre_rejoue_refuse(tmp_path, depot_essai):
    d, c = depot_essai
    _ordres(d, [{"numero": 1, "phase": "fin", "deja_usd": 2.0}])
    r_ = _disque_existant(tmp_path, d, c)
    ech = (r_ / "sparks-v3-echeance.txt").read_text()
    code, out, _ = _amorce(tmp_path, d, c, ECHEANCE_UTC_S=1)          # l'échéance du disque prévaut sur l'environnement
    assert code == 0 and "redémarrage" in out and "ordre 1 (fin)" in out, out
    assert "DELETE instance 123456" in (r_ / "sparks-v3-minuterie.log").read_text()
    assert (r_ / "sparks-v3-echeance.txt").read_text() == ech
    (r_ / "sparks-v3-detruire").unlink()
    code, out, _ = _amorce(tmp_path, d, c)
    _arreter_minuterie(r_)
    assert code == 2 and "ordre refusé" in out


def test_redemarrage_copie_lot_pret_et_fenetre(tmp_path, depot_essai):
    d, c = depot_essai
    _ordres(d, [{"numero": 2, "phase": "copie", "deja_usd": 3.0, "cas": ["vraie01"], "premier": True, "copie_minutes": 5}])
    r_ = _disque_existant(tmp_path, d, c)
    (r_ / "sparks").mkdir()
    _sortie_fab(r_ / "sparks")
    code, out, _ = _amorce(tmp_path, d, c, timeout=25)
    _arreter_minuterie(r_)
    assert code == "délai" or "COPIE prête" in out
    lot = r_ / "sparks" / "lots" / "lot-002"
    assert (lot / "MANIFESTE-LOT.txt").exists() and (lot / "couches-depart-v1.safetensors").exists()
    assert not (r_ / "sparks-v3-detruire").exists()


@pytest.mark.parametrize("poussee", [True, False])
def test_redemarrage_causal_detruit_seulement_apres_poussee_verifiee(tmp_path, depot_essai, poussee):
    d, c = depot_essai
    _ordres(d, [{"numero": 3, "phase": "causal", "deja_usd": 10.0}], causal=True)
    r_ = _disque_existant(tmp_path, d, c)
    kw = {"FAUX_POUSSEE": "1"} if poussee else {}
    code, out, _ = _amorce(tmp_path, d, c, **kw)
    _arreter_minuterie(r_)
    j = (tmp_path / "faux.log").read_text()
    assert "INSTANCE FACTICE causal" in j and "cle-ouverte-v1.json" in j
    if poussee:
        assert code == 0 and "poussée vérifiée" in out and "DELETE instance 123456" in (r_ / "sparks-v3-minuterie.log").read_text()
    else:
        assert "sans poussée vérifiée" in out and not (r_ / "sparks-v3-detruire").exists()


def test_redemarrage_deja_usd_relu_dans_l_ordre(tmp_path, depot_essai):
    d, c = depot_essai
    _ordres(d, [{"numero": 4, "phase": "copie", "deja_usd": 39.9, "cas": ["vraie01"], "premier": False, "copie_minutes": 5}])
    r_ = _disque_existant(tmp_path, d, c)
    code, out, _ = _amorce(tmp_path, d, c, DEJA_USD="0")
    _arreter_minuterie(r_)
    assert code == 2 and "dépense imputée 39.9 USD" in out and "plafond trop bas pour la copie" in out, out


def test_lanceur_refuse_une_echeance_au_dela_du_go(tmp_path):
    r = subprocess.run(["bash", str(RACINE / "scripts" / "lancer_sparks_exp7_nul_v3.sh"), "creation", "1", "0.8", "0.05",
                        "a" * 40, "a" * 40, str(tmp_path / "etat.json"), "1895046400"], capture_output=True, text=True)
    assert r.returncode == 2 and "au-delà de la fin du 18 novembre" in r.stderr


def test_redemarrage_commit_du_disque_different_refuse(tmp_path, depot_essai):
    d, c = depot_essai
    _ordres(d, [{"numero": 1, "phase": "fin", "deja_usd": 0}])
    r_ = _disque_existant(tmp_path, d, c)
    code, out, _ = _amorce(tmp_path, d, "f" * 40)
    _arreter_minuterie(r_)
    assert code == 2 and "commit du disque" in out


# --- 7. gardes de la v2 sans mutation au banc v2 (contre-lecture, point 26) ------------------------------------------------
def test_duree_de_l_amorce_valeurs_exactes():
    t = datetime(2026, 11, 18, 0, 0, tzinfo=timezone.utc)        # 24 h de stockage à 0,05 : 1,20 USD
    assert depense.duree_max_minutes(2.0, 0.05, t) == int(0.9 * (40 - 1.2) / 2.0 * 60)
    assert depense.duree_max_minutes(0.8, 0.05, t) == 24 * 60
    assert depense.duree_max_minutes(2.0, 0.05, t, deja_usd=10) == int(0.9 * (40 - 10 - 1.2) / 2.0 * 60)


def test_projection_stockage_jusqu_a_la_fin_du_18():
    e = {"prix_heure_carte": 0.8, "prix_heure_stockage": 0.05, "heures_demarrees": 0, "phases_faites": [],
         "redemarrages_restants": 0, "egalite_lots": True}
    r = depense.projeter(e, datetime(2026, 11, 4, 12, 0, tzinfo=timezone.utc))
    assert r["detail"]["heures_stockage_restantes"] == 348.0
    assert depense.decision_instance({"maintenant": "2026-11-18T23:59:00Z"})["action"] == "noeud"
    assert depense.decision_instance({"maintenant": "2026-11-19T00:00:00Z"})["action"] == "detruire"


def test_coffre_droits_700_exiges(tmp_path):
    c = tmp_path / "coffre"
    c.mkdir()
    (c / "cle-v1.json").write_text("{}")
    os.chmod(c, 0o755)
    with pytest.raises(aveugle.GardeCoffre, match="droits"):
        aveugle.exiger_coffre(c, [])
    os.chmod(c, 0o700)
    assert aveugle.exiger_coffre(c, []) == c


def test_etalonnage_quatre_contre_quatre_exige():
    from controle_ia.sparks_exp7_nul_v2 import bases as b2
    r = {"h1": "honest", "h2": "honest", "h3": "honest", "s1": "sycophant", "s2": "sycophant", "s3": "sycophant",
         "s4": "sycophant", "s5": "sycophant"}
    for mod in (b2, bases):
        with pytest.raises(b2.GardeBases, match="4 honnêtes"):
            mod.etalonnage_b3_b4({}, r, {}, 1)


@pytest.mark.parametrize("artefact", ["type", "auteur", "anterieure"])
def test_go_extension_type_auteur_dates(tmp_path, artefact):
    from datetime import date
    from controle_ia.sparks_exp7_nul_v2 import go
    e = {"type": L_EXT.replace("| calcul |", "| porte |"), "auteur": L_EXT.replace("| Lazar |", "| Claude |"),
         "anterieure": L_EXT.replace("| 2026-11-04 | calcul", "| 2026-11-03 | calcul")}[artefact]
    p = tmp_path / "go.md"
    p.write_text("| id | a | b | c | d | e | f | g |\n" + L_BASE + "\n" + e + "\n")
    with pytest.raises(go.GardeGo, match="R-389"):
        go.verifier(p, date(2026, 11, 4))


def test_garde_code_commit_cite_en_entier_et_descendance(tmp_path):
    d = tmp_path / "g"
    d.mkdir()
    _git(d, "init", "-q", "-b", "main")
    _git(d, "config", "user.email", "t@example.invalid")
    _git(d, "config", "user.name", "t")
    (d / "a").write_text("a")
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "code")
    code = _git(d, "rev-parse", "HEAD")
    (d / "prereg").mkdir()
    t = f"addendum ; commit {code[:12]} seulement\n"
    (d / garde_code.CHEMIN_ADDENDUM).write_text(t)
    (d / (garde_code.CHEMIN_ADDENDUM + ".sha256")).write_text(garde_code.sha256_octets(t.encode()) + "  x\n")
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "scelle")
    with pytest.raises(garde_code.GardeCode, match="en entier"):
        garde_code.verifier_lancement(d, code)
    _git(d, "checkout", "-q", "--orphan", "autre")
    (d / "b").write_text("b")
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "orphelin")
    with pytest.raises(garde_code.GardeCode, match="descend"):
        garde_code.verifier_lancement(d, code)


def test_etape0_sans_code_distant():
    import inspect
    s = inspect.getsource(instance.charger_candidat_hf)
    assert s.count("trust_remote_code=False") == 2 and "trust_remote_code=True" not in s


def test_liste_fermee_v3_du_depot():
    p = RACINE / garde_code.LISTE
    if not p.exists():
        pytest.skip("liste fermée v3 écrite au commit final")
    liste = garde_code.lire_liste(p.read_text(encoding="utf-8"))
    assert garde_code.LISTE in liste and all((RACINE / x).exists() for x in liste)
    v2 = garde_code.lire_liste((RACINE / "src/controle_ia/sparks_exp7_nul_v2/liste-fermee-v1.txt").read_text(encoding="utf-8"))
    assert set(v2) <= set(liste)
