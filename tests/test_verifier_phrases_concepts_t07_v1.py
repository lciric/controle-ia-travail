"""Essais de `scripts/verifier_phrases_concepts_t07_v1.py` (consigne `docs/procedures/consigne-concepts-sans-lien-T0.7-v2.md`,
`79f2c89c…`, section 6.1 : chaque contrôle C0 à C13 éprouvé sur un cas sain et sur l'artefact nommé, R5).

Entrées réelles prises dans les objets git du clone, jamais sur le réseau : la consigne v2 au commit `f9fee3a8`, le
tokeniseur réel (trois fichiers, commit `03e3cbd9` de `donnees/tokeniseur-llama-3.1-8b-instruct-v1`, `git show` borné à
son dossier), le code du module (`git archive 8dc1cb09 src`). Si ces objets manquent, les essais échouent (jamais un saut).

Le jeu factice (4 × 72 paires engendrées par gabarits) est écrit par les essais : **ce ne sont pas des paires du jeu**. Le
script importe `controle_ia` du seul `--module-src` (CC-01) : chaque essai rend ensuite au processus le chemin d'import et
les modules `controle_ia*` d'avant (le reste de la suite lit `src/`).
"""
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

import numpy as np
import pytest

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "verifier_phrases_concepts_t07_v1.py"
COMMIT_CONSIGNE = "f9fee3a87c7cc2644d65c93ab0617108fe197167"
CHEMIN_CONSIGNE = "docs/procedures/consigne-concepts-sans-lien-T0.7-v2.md"
COMMIT_TOKENISEUR = "03e3cbd9"
DOSSIER_TOKENISEUR = "donnees/tokeniseur-llama-3.1-8b-instruct-v1"
COMMIT_MODULE = "8dc1cb09"
ENTROPIE_ESSAI = 20261110


def _charger_script():
    spec = importlib.util.spec_from_file_location("verifier_phrases_concepts_t07_v1", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m                       # exigé par `dataclass` (annotations différées)
    spec.loader.exec_module(m)
    return m


vp = _charger_script()


# ----------------------------------------------------------------------------------------------------------------------
# Isolement du paquet `controle_ia` (CC-01 : le script l'importe de `--module-src`)
# ----------------------------------------------------------------------------------------------------------------------

def _du_paquet(nom: str) -> bool:
    return nom == "controle_ia" or nom.startswith("controle_ia.")


@contextlib.contextmanager
def isolement():
    chemin = list(sys.path)
    avant = {k: v for k, v in sys.modules.items() if _du_paquet(k)}
    bytecode = sys.dont_write_bytecode
    env = {k: os.environ.get(k) for k in ("HF_HUB_OFFLINE", "TRANSFORMERS_OFFLINE")}
    try:
        yield
    finally:
        for k in [k for k in sys.modules if _du_paquet(k)]:
            del sys.modules[k]
        sys.modules.update(avant)
        sys.path[:] = chemin
        sys.dont_write_bytecode = bytecode
        for k, v in env.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


@pytest.fixture(autouse=True)
def _isoler():
    with isolement():
        yield


# ----------------------------------------------------------------------------------------------------------------------
# Entrées réelles (objets git du clone)
# ----------------------------------------------------------------------------------------------------------------------

def _git(*args) -> bytes:
    r = subprocess.run(["git", "-C", str(RACINE), *args], capture_output=True)
    if r.returncode != 0:
        pytest.fail(f"git {' '.join(args[:2])} : {r.stderr.decode(errors='replace')[:300]} — objets absents du clone : "
                    "essais impossibles (jamais un saut)")
    return r.stdout


def _sceller(chemin: Path) -> str:
    h = hashlib.sha256(chemin.read_bytes()).hexdigest()
    c = Path(str(chemin) + ".sha256")
    if c.exists():
        c.unlink()
    c.write_text(f"{h}  {chemin.name}\n", encoding="utf-8")
    return h


class Reel:
    def __init__(self, base: Path) -> None:
        self.base = base
        self.tok = base / "tokeniseur"
        self.tok.mkdir()
        for nom in vp.EMPREINTES_TOKENISEUR:
            (self.tok / nom).write_bytes(_git("show", f"{COMMIT_TOKENISEUR}:{DOSSIER_TOKENISEUR}/{nom}"))
        arbre = base / "module"
        arbre.mkdir()
        with tarfile.open(fileobj=io.BytesIO(_git("archive", "--format=tar", COMMIT_MODULE, "src"))) as tar:
            tar.extractall(arbre, filter="data")
        self.src = arbre / "src"
        cdir = base / "consigne"
        cdir.mkdir()
        self.consigne = cdir / Path(CHEMIN_CONSIGNE).name
        self.consigne.write_bytes(_git("show", f"{COMMIT_CONSIGNE}:{CHEMIN_CONSIGNE}"))
        Path(str(self.consigne) + ".sha256").write_bytes(_git("show", f"{COMMIT_CONSIGNE}:{CHEMIN_CONSIGNE}.sha256"))

    def args(self, mode: str, dossier: Path, *extra, consigne: Path | None = None, tok: Path | None = None,
             src: Path | None = None) -> list[str]:
        a = [mode, "--consigne", str(consigne or self.consigne), "--dossier", str(dossier)]
        if mode != "decompter":
            a += ["--module-src", str(src or self.src)]
        if mode not in ("echantillon", "decompter"):
            a += ["--tokeniseur", str(tok or self.tok)]
        return a + [str(x) for x in extra]

    def consigne_modifiee(self, dossier: Path, ancien: str, nouveau: str, compte: int = 1) -> tuple[Path, str]:
        """Copie de la consigne avec un remplacement, scellée à son tour ; rend (chemin, empreinte)."""
        texte = self.consigne.read_text(encoding="utf-8")
        assert texte.count(ancien) == compte, (ancien, texte.count(ancien))
        dossier.mkdir(parents=True, exist_ok=True)
        c = dossier / self.consigne.name
        c.write_text(texte.replace(ancien, nouveau), encoding="utf-8")
        return c, _sceller(c)


@pytest.fixture(scope="session")
def reel(tmp_path_factory) -> Reel:
    return Reel(tmp_path_factory.mktemp("reel"))


@pytest.fixture(scope="session")
def ctx(reel):
    with isolement():
        a = vp.analyser(reel.args("extraire", reel.base / "inutile"))
        return vp.charger_contexte(a, vp.Journal("essai"), extraits=False)


def lancer(argv) -> int:
    return vp.main([str(x) for x in argv])


# ----------------------------------------------------------------------------------------------------------------------
# Jeu factice (écrit par les essais ; jamais des paires du jeu)
# ----------------------------------------------------------------------------------------------------------------------

ADJ = ["small", "quiet", "grey", "large", "young", "pale", "brown", "sleek"]
LIEU = ["shed", "table", "bench", "stairs", "ledge", "rug", "sofa", "chair", "crate"]
GABARITS = {
    "chats": ("The {a} {b} usually naps on the {d} near the back porch in the afternoon.",
              ["cat", "kitten", "tabby", "tomcat", "kitty", "feline", "calico", "ragdoll", "siamese"],
              "The {a} {b} usually rests on the {d} near the back pantry in the late afternoon.",
              ["basket", "blanket", "teapot", "ladle", "bucket", "saucepan", "inkwell", "platter", "thimble"]),
    "meteo": ("A {a} {b} often drifts over the {d} before the market opens on weekdays.",
              ["drizzle", "mist", "fog", "breeze", "sleet", "hail", "snow", "rain", "frost"],
              "A {a} {b} often sits beside the {d} before the old bakery opens on weekdays.",
              ["tablecloth", "ribbon", "banner", "curtain", "napkin", "towel", "scarf", "quilt", "coaster"]),
    "sports": ("Each {a} {b} squad stores its gear in the {d} after the morning practice.",
               ["tennis", "rugby", "cricket", "hockey", "golf", "volleyball", "badminton", "baseball", "basketball"],
               "Each {a} {b} group stores its tools in the {d} after the morning delivery.",
               ["pottery", "quilting", "choir", "knitting", "bakery", "ceramics", "woodwork", "weaving", "carpentry"]),
    "geographie": ("The {a} {b} sits west of the {d} across a wide stretch of open land.",
                   ["river", "lake", "valley", "island", "peninsula", "glacier", "canyon", "plateau", "delta"],
                   "The {a} {b} sits left of the {d} across a wide stretch of open shelf.",
                   ["drawer", "cupboard", "dresser", "wardrobe", "cabinet", "bookcase", "sideboard", "mirror", "bedframe"]),
}
MARQUEUR = "veranda"     # un seul mot, dans une seule phrase du jeu factice (chats/5), pour le gabarit falsifié (C4)


def phrases_factices(c: str, k: int) -> tuple[str, str]:
    tc, bc, tn, bn = GABARITS[c]
    a, b = (k - 1) // 9, (k - 1) % 9
    d = (a + b) % 9
    pc = tc.format(a=ADJ[a], b=bc[b], d=LIEU[d])
    if (c, k) == ("chats", 5):
        pc = pc.replace("porch", MARQUEUR)
    return pc, tn.format(a=ADJ[a], b=bn[b], d=LIEU[d])


def enregistrement(c: str, k: int, **change) -> dict:
    pc, pn = phrases_factices(c, k)
    r = {"concept": c, "indice": k, "domaine_neutre": f"N{(k - 1) % 8 + 1}", "phrase_concept": pc, "phrase_neutre": pn}
    r.update(change)
    return r


def remise_factice(changes: dict | None = None, ote=()) -> list[dict]:
    changes = changes or {}
    return [enregistrement(c, k, **changes.get((c, k), {})) for c in vp.CONCEPTS for k in range(1, 73)
            if (c, k) not in ote]


def ecrire_jsonl(chemin: Path, recs) -> Path:
    chemin.write_text("".join(json.dumps(r) + "\n" for r in recs), encoding="utf-8")
    return chemin


def paire(c: str, k: int, **change) -> "vp.Paire":
    r = enregistrement(c, k, **change)
    return vp.Paire(c, k, r["domaine_neutre"], r["phrase_concept"], r["phrase_neutre"])


def base_paires() -> list:
    return [paire(c, k) for c in vp.CONCEPTS for k in (1, 2)]


def controler(ctx, paires, perdant=None):
    j = vp.Journal("essai")
    defs, jetons = vp.controler_paires(ctx, paires, perdant or vp.perdant_passe1, j)
    return defs, jetons, j


def defauts_de(defs, nom, controle=None):
    return [d for d in defs if d["paire"] == nom and (controle is None or d["controle"] == controle)]


# ----------------------------------------------------------------------------------------------------------------------
# Parcours sain partagé (extraire, passe 1, passe 2), copié par les essais qui en partent
# ----------------------------------------------------------------------------------------------------------------------

@pytest.fixture(scope="session")
def extrait(reel, tmp_path_factory):
    d = tmp_path_factory.mktemp("extrait") / "jeu"
    with isolement():
        assert lancer(reel.args("extraire", d)) == 0
    return d


@pytest.fixture(scope="session")
def sain(reel, extrait, tmp_path_factory):
    d = tmp_path_factory.mktemp("sain") / "jeu"
    shutil.copytree(extrait, d)
    remise = ecrire_jsonl(d / "remise-ecrivain-v1.jsonl", remise_factice())
    _sceller(remise)
    with isolement():
        assert lancer(reel.args("verifier", d, "--passe", 1, "--remise", remise)) == 0
        assert lancer(reel.args("verifier", d, "--passe", 2, "--remise", remise)) == 0
    return d


def copie(source: Path, tmp_path: Path) -> Path:
    d = tmp_path / "jeu"
    shutil.copytree(source, d)
    return d


# ======================================================================================================================
# C0 — entrées et annexes ; mode `extraire`
# ======================================================================================================================

def test_c0_extraire_cas_sain(extrait, reel):
    noms = sorted(p.name for p in extrait.iterdir())
    for n in list(vp.NOMS_EXTRAITS.values()) + [vp.JOURNAL_EXTRACTION]:
        assert n in noms and f"{n}.sha256" in noms
    remise = (extrait / "remise-a-l-ecrivain-v1.md").read_text(encoding="utf-8")
    assert remise.startswith("You are writing pairs of English sentences")
    assert "```annexe-a\nA1 | pain, pains" in remise and "```annexe-b\nchats | noyau | cat/cats" in remise
    assert "<!--" not in remise and "\n> " not in remise and "Statut" not in remise
    lecteur = (extrait / "remise-au-lecteur-v1.md").read_text(encoding="utf-8")
    assert lecteur.startswith("## 1. Objet") and "\n## 7. Contre-vérification" in lecteur
    assert "## 2. " not in lecteur and "## 8. " not in lecteur and "annexe-a" not in lecteur and "E1" not in lecteur
    texte = reel.consigne.read_text(encoding="utf-8")
    i = {b: texte.index(f"\n{b}") + 1 for b in ("## 1. ", "## 2. ", "## 7. ", "## 8. ")}   # bornes en début de ligne
    assert "`## 7. `" in texte[:i["## 7. "]]                  # la prose cite la borne avant le titre : piège évité
    assert texte[i["## 1. "]:i["## 2. "]] + texte[i["## 7. "]:i["## 8. "]] == lecteur
    assert len((extrait / "exemples-v1.jsonl").read_text().splitlines()) == 8
    assert (extrait / "format-lecture-v1.json").read_text() == '{"format_lecture": "message_utilisateur"}\n'
    a = json.loads((extrait / "annexe-a-mots-interdits-v1.json").read_text())
    assert sum(len(v) for v in a.values()) == 942
    j = (extrait / vp.JOURNAL_EXTRACTION).read_text(encoding="utf-8")
    assert "[OK] C0 — emplacement du paquet (CC-01)" in j and "[OK] C10" in j and "942 entrées" in j
    assert "huit exemples conformes à C2-C8 et C10" in j and "code 0" in j
    assert "manifeste.py : sha256 1a5c7464" in j and "lecture_v2.py : sha256 9d5c1c05" in j


def test_c0_extraire_refuse_d_ecraser(extrait, reel, tmp_path, capsys):
    d = copie(extrait, tmp_path)
    assert lancer(reel.args("extraire", d)) == 2
    assert "R12" in capsys.readouterr().err


def test_c0_paquet_charge_du_seul_module_src(ctx, reel):
    """Cas sain de CC-01 : les fonctions employées viennent des fichiers de `--module-src`."""
    for f in (ctx.mod["lire_phrases_concepts"], ctx.mod["exiger_concept_sans_affect"],
              ctx.mod["jetons_message_utilisateur"], ctx.mod["graines"]):
        assert Path(f.__code__.co_filename).resolve().is_relative_to(reel.src.resolve())


def test_c0_cas_sain_cc01_de_bout_en_bout_et_paquet_d_avant_rendu(reel, tmp_path):
    import controle_ia.gardes as gardes_avant                   # paquet de `src/` (réglage de pytest)
    with isolement():
        assert lancer(reel.args("extraire", tmp_path / "jeu")) == 0
        for nom in vp.MODULES_EMPLOYES:
            assert Path(sys.modules[nom].__file__).resolve().is_relative_to(reel.src.resolve()), nom
    assert sys.modules["controle_ia.gardes"] is gardes_avant


def test_c0_artefact_arbre_sans_lecture_v2(reel, tmp_path, capsys):
    src = tmp_path / "src"
    shutil.copytree(reel.src, src)
    (src / "controle_ia" / "t07" / "lecture_v2.py").unlink()
    assert lancer(reel.args("extraire", tmp_path / "jeu", src=src)) == 2
    assert "t07/lecture_v2.py absent sur disque" in capsys.readouterr().err


def test_c0_artefact_tokenizer_un_octet_change(reel, tmp_path, capsys):
    tok = tmp_path / "tok"
    shutil.copytree(reel.tok, tok)
    b = bytearray((tok / "tokenizer.json").read_bytes())
    b[100] = ord("x") if b[100] != ord("x") else ord("y")
    (tok / "tokenizer.json").write_bytes(bytes(b))
    d = tmp_path / "jeu"
    assert lancer(reel.args("extraire", d, tok=tok)) == 2
    assert "tokeniseur altéré : tokenizer.json" in capsys.readouterr().err
    assert not d.exists()


def test_c0_artefact_copie_d_annexe_privee_d_une_entree(sain, reel, tmp_path, capsys):
    d = copie(sain, tmp_path)
    for f in ("journal-verification-passe1-v1.txt", vp.RENVOIS):
        for x in (d / f, Path(str(d / f) + ".sha256")):
            x.unlink()
    f = d / "annexe-a-mots-interdits-v1.json"
    a = json.loads(f.read_text())
    a["A3"].remove("goal" if "goal" in a["A3"] else a["A3"][0])
    f.write_bytes(vp.json_canonique(a))
    _sceller(f)
    assert lancer(reel.args("verifier", d, "--passe", 1, "--remise", d / "remise-ecrivain-v1.jsonl")) == 2
    err = capsys.readouterr().err
    assert "copie annexe-a-mots-interdits-v1.json ≠ bloc de la consigne" in err and "entrées manquantes" in err
    assert not (d / vp.RENVOIS).exists()


@pytest.mark.parametrize("ancien,nouveau,motif", [
    ("chats | noyau | cat/cats,", "chats | noyau | fear, cat/cats,", "A ∩ B non vide"),
    ("sports | champ | race/races/racing,", "sports | champ | sky, race/races/racing,", "lexiques de meteo et de sports non disjoints"),
    ("sports | noyau | sport/sports,", "sports | noyau | high stakes jump, sport/sports,", "contient un mot de l'annexe A"),
    ("chats | champ | paw/paws,", "chats | champ | rain hood, paw/paws,", "contient un mot du lexique d'un autre concept"),
], ids=["mot-A-au-noyau", "champ-meteo-dans-sports", "high-stakes-jump", "entree-avec-mot-d-un-autre-concept"])
def test_c0_artefacts_annexes(reel, tmp_path, capsys, ancien, nouveau, motif):
    c, h = reel.consigne_modifiee(tmp_path / "consigne", ancien, nouveau)
    d = tmp_path / "jeu"
    assert lancer(reel.args("extraire", d, "--empreinte-consigne", h, consigne=c)) == 2
    assert motif in capsys.readouterr().err
    assert not d.exists()


def test_c0_artefact_fichier_du_module_change(reel, tmp_path, capsys):
    src = tmp_path / "src"
    shutil.copytree(reel.src, src)
    with open(src / "controle_ia" / "harnais" / "formats.py", "a", encoding="utf-8") as f:
        f.write("# changé\n")
    assert lancer(reel.args("extraire", tmp_path / "jeu", src=src)) == 2
    assert "code du module altéré : harnais/formats.py" in capsys.readouterr().err


def test_c0_artefact_paquet_de_l_arbre_de_travail_avant_module_src(reel, tmp_path, monkeypatch, capsys):
    """CC-01 : `src/` de l'arbre de travail placé avant `--module-src` ; son paquet n'a pas le module de T0.7."""
    vrai = vp.placer_en_tete

    def placer(src):
        vrai(src)
        sys.path.insert(0, str(RACINE / "src"))
    monkeypatch.setattr(vp, "placer_en_tete", placer)
    assert lancer(reel.args("extraire", tmp_path / "jeu")) == 2
    err = capsys.readouterr().err
    assert "C0 —" in err and ("hors de --module-src" in err or "import du paquet controle_ia depuis --module-src impossible" in err)


def test_c0_artefact_paquet_complet_importe_d_ailleurs(reel, tmp_path, monkeypatch, capsys):
    """CC-01 : un arbre complet (mêmes fichiers) placé avant `--module-src` : l'import réussit d'ailleurs, la garde
    d'emplacement refuse."""
    ailleurs = tmp_path / "ailleurs"
    shutil.copytree(reel.src, ailleurs)
    vrai = vp.placer_en_tete

    def placer(src):
        vrai(src)
        sys.path.insert(0, str(ailleurs))
    monkeypatch.setattr(vp, "placer_en_tete", placer)
    assert lancer(reel.args("extraire", tmp_path / "jeu")) == 2
    err = capsys.readouterr().err
    assert "modules du paquet controle_ia importés hors de --module-src" in err and str(ailleurs) in err


def test_c0_artefact_exemple_fautif(reel, tmp_path, capsys):
    c, h = reel.consigne_modifiee(tmp_path / "consigne", "A grey tabby cat sleeps on the wide",
                                  "A grey tabby cat sleeps in fear on the wide")
    assert lancer(reel.args("extraire", tmp_path / "jeu", "--empreinte-consigne", h, consigne=c)) == 2
    err = capsys.readouterr().err
    assert "C0 — exemple(s) en défaut" in err and "E1 C6" in err


@pytest.mark.parametrize("ancien,nouveau,motif", [
    ("```annexe-a\n", "```annexe-x\n", "bloc `annexe-a` trouvé 0 fois"),
    ("<!-- section-5-fin -->\n", "<!-- section-5-fin -->\n<!-- section-5-fin -->\n", "marqueurs de la section 5"),
    ("## 8. Fichiers", "## 7. Fichiers", "borne « ## 7. » de la remise au lecteur trouvée 2 fois"),
], ids=["bloc-absent", "marqueur-double", "borne-lecteur-double"])
def test_c0_artefacts_blocs_et_bornes(reel, tmp_path, capsys, ancien, nouveau, motif):
    c, h = reel.consigne_modifiee(tmp_path / "consigne", ancien, nouveau)
    assert lancer(reel.args("extraire", tmp_path / "jeu", "--empreinte-consigne", h, consigne=c)) == 2
    assert motif in capsys.readouterr().err


def test_c0_artefact_consigne_differente_de_son_compagnon(reel, tmp_path, capsys):
    c, _ = reel.consigne_modifiee(tmp_path / "consigne", "## 1. Objet", "## 1. Objet ")
    Path(str(c) + ".sha256").write_text(f"{'0' * 64}  {c.name}\n", encoding="utf-8")
    assert lancer(reel.args("extraire", tmp_path / "jeu", consigne=c)) == 2
    assert "≠ son compagnon" in capsys.readouterr().err


def test_c0_artefact_autre_consigne_sans_option(reel, tmp_path, capsys):
    c, _ = reel.consigne_modifiee(tmp_path / "consigne", "## 1. Objet", "## 1. Objet ")
    assert lancer(reel.args("extraire", tmp_path / "jeu", consigne=c)) == 2
    assert f"≠ attendue {vp.EMPREINTE_CONSIGNE}" in capsys.readouterr().err


def test_c0_artefact_bibliotheque_tokenizers_absente(reel, tmp_path, monkeypatch, capsys):
    monkeypatch.setitem(sys.modules, "tokenizers", None)
    assert lancer(reel.args("extraire", tmp_path / "jeu")) == 2
    assert "bibliothèque `tokenizers` absente" in capsys.readouterr().err


def test_c0_artefact_tokeniseur_dans_l_arbre_de_travail(reel, tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(vp, "RACINE_DEPOT", reel.base)
    assert lancer(reel.args("extraire", tmp_path / "jeu")) == 2
    assert "tokeniseur : dossier dans l'arbre de travail" in capsys.readouterr().err


def test_c0_artefact_autre_commit_sans_empreintes(reel, tmp_path, capsys):
    assert lancer(reel.args("extraire", tmp_path / "jeu", "--commit-module", "0123abcd")) == 2
    assert "ses empreintes sont à relire" in capsys.readouterr().err


# ======================================================================================================================
# C1 — schéma de la remise
# ======================================================================================================================

def test_c1_cas_sain(tmp_path):
    paires, defs, rejets, info = vp.lire_remise(ecrire_jsonl(tmp_path / "r.jsonl", remise_factice()), initiale=True)
    assert len(paires) == 288 and defs == [] and rejets == [] and info["ordre_des_cles_autre"] == 0


@pytest.mark.parametrize("cas", ["cle-en-trop", "indice-repete", "indice-true", "meteo-accent", "cats",
                                 "domaine-N2-indice-1", "71-paires"])
def test_c1_artefacts(tmp_path, cas):
    recs = remise_factice()
    if cas == "cle-en-trop":
        recs[2]["note"] = "x"
        attendu = ("chats", 3, "en trop : ['note']")
    elif cas == "indice-repete":
        recs.insert(5, dict(recs[2]))
        attendu = ("chats", 3, "indice répété")
    elif cas == "indice-true":
        recs[0]["indice"] = True
        attendu = ("chats", 1, "paire absente")
    elif cas == "meteo-accent":
        recs[72]["concept"] = "météo"
        attendu = ("meteo", 1, "paire absente")
    elif cas == "cats":
        recs[72]["concept"] = "cats"
        attendu = ("meteo", 1, "paire absente")
    elif cas == "domaine-N2-indice-1":
        recs[0]["domaine_neutre"] = "N2"
        attendu = ("chats", 1, "domaine_neutre 'N2' ≠ N1")
    else:
        del recs[72 * 2 + 71]
        attendu = ("sports", 72, "paire absente")
    _, defs, rejets, info = vp.lire_remise(ecrire_jsonl(tmp_path / "r.jsonl", recs), initiale=True)
    assert [d for d in defs if (d["concept"], d["indice"]) == attendu[:2] and attendu[2] in d["motif"]], defs
    if cas in ("indice-true", "meteo-accent", "cats"):
        assert len(rejets) == 1 and ("entier non booléen" in rejets[0]["motif"] or "hors de la liste fermée" in rejets[0]["motif"])
    if cas == "71-paires":
        assert info["par_concept"]["sports"] == 71


def test_c1_artefact_paire_non_renvoyee_dans_la_remise_des_renvois(tmp_path):
    recs = [enregistrement("chats", 3), enregistrement("chats", 4)]
    paires, defs, _, _ = vp.lire_remise(ecrire_jsonl(tmp_path / "r.jsonl", recs), initiale=False,
                                         renvoyees={("chats", 3)})
    assert set(paires) == {("chats", 3)}
    assert [d for d in defs if d["indice"] == 4 and "paire non renvoyée" in d["motif"] and d["valeurs"]["non_renvoyee"]]


# ======================================================================================================================
# C2 à C9 sur des paires (cas sain : paires factices ; artefacts nommés par la consigne)
# ======================================================================================================================

def test_c2_a_c9_cas_sain(ctx):
    defs, _, j = controler(ctx, base_paires())
    assert defs == []
    for c in ("C2", "C3", "C4", "C5", "C6", "C7", "C9", "C8"):
        assert f"[OK] {c} —" in j.texte()


@pytest.mark.parametrize("role,texte,motif", [
    ("phrase_neutre", "The small basket usually rests on the shed near the back pantry?", "'?'"),
    ("phrase_neutre", "The small basket usually rests on the shed near the back pantry!", "'!'"),
    ("phrase_neutre", "The small basket usually rests on 2 sheds near the back pantry.", "'2'"),
    ("phrase_concept", "The small cat usually naps on the café shelf near the back porch.", "U+00E9"),
    ("phrase_neutre", "The small basket usually rests on the § near the back pantry.", "U+00A7"),
    ("phrase_neutre", "The small basket usually rests on the shed\nnear the back pantry.", "U+000A"),
    ("phrase_concept", "The small cat usually naps. The kitten sleeps near the back porch.", "point ailleurs"),
    ("phrase_neutre", " The small basket usually rests on the shed near the back pantry.", "espace en tête"),
    ("phrase_neutre", "The small basket usually rests on the shed near the back pantry", "ne finit pas par un point"),
    ("phrase_neutre", "The small basket usually rests on the shed; near the back pantry.", "';'"),
    ("phrase_neutre", "The small basket usually rests on the shed <|eot_id|> near the pantry.", "'<'"),
    ("phrase_neutre", "The small basket usually rests on the shed near the pantry in London.", "['London']"),
], ids=["question", "exclamation", "chiffre", "accent", "paragraphe", "saut-de-ligne", "deux-phrases", "espace-en-tete",
        "point-final-absent", "point-virgule", "jeton-special", "London-neutre"])
def test_c2_artefacts(ctx, role, texte, motif):
    p = paire("chats", 1, **{role: texte})
    d = [x for x in vp.controle_c2([p]) if x["role"] == role]
    assert d and any(motif in x["motif"] for x in d), d


def test_c2_artefact_wimbledon_dans_sports(ctx):
    p = paire("sports", 1, phrase_concept="Each small tennis squad stores its gear at Wimbledon after the morning practice.")
    assert any("['Wimbledon']" in x["motif"] for x in vp.controle_c2([p]))


@pytest.mark.parametrize("concept,role,texte", [
    ("chats", "phrase_concept", "The small Siamese usually naps on the shed near the back porch in the afternoon."),
    ("meteo", "phrase_concept", "A small mist often drifts over the shed when the air is near Fahrenheit freezing."),
    ("geographie", "phrase_concept", "The small river sits west of the Pacific across a wide stretch of open land."),
], ids=["Siamese-admis", "Fahrenheit-admis", "Pacific-admis-en-geographie"])
def test_c2_majuscules_admises(ctx, concept, role, texte):
    assert vp.controle_c2([paire(concept, 1, **{role: texte})]) == []


def test_c2_pacific_refuse_hors_de_geographie(ctx):
    p = paire("meteo", 1, phrase_concept="A small mist often drifts over the Pacific before the market opens on weekdays.")
    assert any("['Pacific']" in x["motif"] for x in vp.controle_c2([p]))


def phrase_de(ctx, n: int) -> str:
    for m in range(300):
        t = "The cat" + " sat" * m + "."
        if vp.compter_jetons(ctx.tok, t) == n:
            return t
    raise AssertionError(n)


@pytest.mark.parametrize("n,motif,controle", [(7, "7 jetons < 8", "C3"), (41, "41 jetons > 40", "C3"),
                                              (129, "129 jetons > 128", "C3-borne")])
def test_c3_artefacts_longueurs(ctx, n, motif, controle):
    t = phrase_de(ctx, n)
    assert vp.compter_jetons(ctx.tok, t) == n
    defs, borne, _ = vp.controle_c3(ctx, [paire("chats", 1, phrase_concept=t, phrase_neutre=t)])
    assert any(motif in d["motif"] and d["controle"] == controle for d in defs + borne), defs + borne
    if n == 129:
        assert any("41" in d["motif"] or "> 40" in d["motif"] for d in defs)


def test_c3_artefact_ecart_020(ctx):
    a, b = phrase_de(ctx, 20), phrase_de(ctx, 16)
    defs, _, _ = vp.controle_c3(ctx, [paire("chats", 1, phrase_concept=a, phrase_neutre=b)])
    assert [d for d in defs if d["role"] == "paire" and "écart relatif 0.200" in d["motif"]]
    defs, _, _ = vp.controle_c3(ctx, [paire("chats", 1, phrase_concept=phrase_de(ctx, 20), phrase_neutre=phrase_de(ctx, 17))])
    assert defs == []                                   # 0,15 tout juste : admis


@pytest.mark.parametrize("controle,role,texte,motif", [
    ("C5", "phrase_neutre", "The small basket you see rests on the shed near the back pantry.", "['you']"),
    ("C5", "phrase_neutre", "Our small basket usually rests on the shed near the back pantry.", "['our']"),
    ("C5", "phrase_neutre", "The small basket you'll see rests on the shed near the back pantry.", "['you']"),
    ("C6", "phrase_concept", "The small cat usually naps in fear on the shed near the back porch.", "fear (A1)"),
    ("C6", "phrase_neutre", "The small basket is a sabotage of the shed near the back pantry.", "sabotage (A2)"),
    ("C6", "phrase_neutre", "The small basket sits on purpose on the shed near the back pantry.", "on purpose (A2)"),
    ("C6", "phrase_neutre", "Training baskets usually rest on the shed near the back pantry.", "training (A5)"),
    ("C6", "phrase_neutre", "The small basket's goal's place is the shed near the back pantry.", "goal (A2)"),
    ("C7", "phrase_concept", "The small pillow usually naps on the shed near the back porch.", "aucun mot du noyau de chats"),
    ("C7", "phrase_concept", "The small cat usually naps on the football near the back porch.", "football (sports noyau)"),
    ("C7", "phrase_neutre", "The small basket usually rests in the rain near the back pantry.", "rain/rains/rained/raining (meteo noyau)"),
    ("C7", "phrase_neutre", "The small basket usually rests on the north side of the pantry.", "north (geographie champ)"),
], ids=["you", "Our-en-tete", "you-ll", "fear-concept", "sabotage-neutre", "on-purpose", "Training", "goal-s",
        "sans-noyau", "chats-avec-football", "neutre-avec-rain", "neutre-avec-north"])
def test_c5_c6_c7_artefacts(ctx, controle, role, texte, motif):
    p = paire("chats", 1, **{role: texte})
    d5, d6 = vp.controle_c5_c6(ctx, [p])
    d = {"C5": d5, "C6": d6, "C7": vp.controle_c7(ctx, [p])}[controle]
    assert any(x["role"] == role and motif in x["motif"] for x in d), d


def test_c8_artefact_meme_phrase_dans_deux_concepts(ctx):
    ps = base_paires()
    ps[2] = paire("meteo", 1, phrase_concept=ps[0].phrase_concept)
    d = vp.controle_c8(ps, vp.perdant_passe1)
    assert [x for x in d if x["paire"] == "meteo/1" and x["valeurs"]["paire_en_conflit"] == "chats/1"
            and x["valeurs"]["distance"] == 0]
    assert not [x for x in d if x["paire"] == "chats/1"]          # la paire de rang le plus bas n'est pas en défaut


def test_c8_artefact_neutre_egale_au_concept_a_un_mot_pres(ctx):
    pc, _ = phrases_factices("chats", 1)
    p = paire("chats", 1, phrase_neutre=pc.replace("cat", "basket"))
    d = vp.controle_c8([p], vp.perdant_passe1)
    assert [x for x in d if x["paire"] == "chats/1" and x["role"] == "paire" and x["valeurs"]["distance"] == 1]


def test_c9_artefacts(ctx):
    e1 = "A grey tabby cat sleeps on the wide kitchen windowsill through most of the afternoon."
    copiee = paire("chats", 1, phrase_concept=e1.replace("grey", "white"))
    longue = paire("chats", 2, phrase_concept="Every morning a tabby cat sleeps on the wide kitchen windowsill near the old door.")
    d = vp.controle_c9(ctx, [copiee, longue])
    assert [x for x in d if x["paire"] == "chats/1" and x["valeurs"].get("distance") == 1
            and x["valeurs"]["exemple"] == "E1 (phrase_concept)"]
    suites = [x["valeurs"].get("suite") for x in d if x["paire"] == "chats/2"]
    assert suites and all(s and len(s.split()) == 6 and s in e1.lower() for s in suites), suites


# ======================================================================================================================
# C4 — gabarit (CC-04) ; C10 ; passe 1 de bout en bout
# ======================================================================================================================

def falsifier(marque):
    vrai = vp.construire_format

    def construire(mod, tok_hf):
        fmt = vrai(mod, tok_hf)
        rendre = fmt.rendre

        def rendre_faux(messages, invite):
            ids = rendre(messages, invite)
            return ids + [ids[-1]] if any(marque(m["content"]) for m in messages) else ids
        fmt.rendre = rendre_faux
        return fmt
    return construire


def test_passe1_cas_sain(sain):
    j = (sain / "journal-verification-passe1-v1.txt").read_text(encoding="utf-8")
    for c in ("C0", "C10", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C13"):
        assert f"[OK] {c} —" in j, c
    assert "[DÉFAUT]" not in j and "[RÉSERVE]" not in j and "code 0" in j
    assert json.loads((sain / vp.RENVOIS).read_text())["renvois"] == []


def test_c4_artefact_gabarit_falsifie_pour_une_seule_phrase(extrait, reel, tmp_path, monkeypatch):
    d = copie(extrait, tmp_path)
    remise = ecrire_jsonl(d / "remise-ecrivain-v1.jsonl", remise_factice())
    monkeypatch.setattr(vp, "construire_format", falsifier(lambda t: MARQUEUR in t))
    assert lancer(reel.args("verifier", d, "--passe", 1, "--remise", remise)) == 1
    j = (d / "journal-verification-passe1-v1.txt").read_text(encoding="utf-8")
    assert "[DÉFAUT] C4 — gabarit et identité des jetons : 1 défaut(s)" in j and "chats/5 (phrase_concept) : gabarit" in j
    r = json.loads((d / vp.RENVOIS).read_text())["renvois"]
    assert [(x["concept"], x["indice"]) for x in r] == [("chats", 5)] and r[0]["motifs"][0]["controle"] == "C4"


def test_c4_artefact_gabarit_falsifie_pour_toutes_les_phrases(extrait, reel, tmp_path, monkeypatch, capsys):
    d = copie(extrait, tmp_path)
    remise = ecrire_jsonl(d / "remise-ecrivain-v1.jsonl", remise_factice())
    monkeypatch.setattr(vp, "construire_format", falsifier(lambda t: t not in ("", "§")))
    assert lancer(reel.args("verifier", d, "--passe", 1, "--remise", remise)) == 2
    assert "C0 — exemple(s) en défaut" in capsys.readouterr().err
    assert not (d / vp.RENVOIS).exists() and not (d / "journal-verification-passe1-v1.txt").exists()


def test_c10_artefact_concept_fear(reel, tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(vp, "CONCEPTS", vp.CONCEPTS + ("fear",))
    assert lancer(reel.args("extraire", tmp_path / "jeu")) == 2
    err = capsys.readouterr().err
    assert "C10 — concept sans affect" in err and "arrêt et nœud" in err


def test_passe1_artefacts_renvoyes_avec_motifs_et_valeurs(extrait, reel, tmp_path):
    d = copie(extrait, tmp_path)
    pc3, _ = phrases_factices("chats", 4)
    changes = {("chats", 3): {"phrase_concept": phrases_factices("chats", 3)[0].replace("naps", "naps in fear")},
               ("meteo", 9): {"phrase_concept": pc3},                       # C7 et doublon de chats/4
               ("sports", 1): {"note": 1}}
    remise = ecrire_jsonl(d / "remise-ecrivain-v1.jsonl", remise_factice(changes, ote={("geographie", 72)}))
    assert lancer(reel.args("verifier", d, "--passe", 1, "--remise", remise)) == 1
    r = {(x["concept"], x["indice"]): x for x in json.loads((d / vp.RENVOIS).read_text())["renvois"]}
    assert set(r) == {("chats", 3), ("meteo", 9), ("sports", 1), ("geographie", 72)}
    assert [m for m in r[("chats", 3)]["motifs"] if m["controle"] == "C6" and m["valeurs"]["mots"][0]["mot"] == "fear"]
    assert [m for m in r[("meteo", 9)]["motifs"] if m["controle"] == "C8" and m["valeurs"]["paire_en_conflit"] == "chats/4"]
    assert r[("geographie", 72)]["phrase_concept"] is None
    assert vp.lire_compagnon(d / vp.RENVOIS) == hashlib.sha256((d / vp.RENVOIS).read_bytes()).hexdigest()


# ======================================================================================================================
# Section 3 : second passage, retraits, réserve, plancher (CC-16)
# ======================================================================================================================

def selection_de(d: Path) -> dict:
    return json.loads((d / vp.SELECTION).read_text())


def test_passe2_cas_sain(sain):
    s = selection_de(sain)
    assert s["code_passe2"] == 0
    for c in vp.CONCEPTS:
        e = s["concepts"][c]
        assert e["n"] == 64 and e["statut"] == "complet" and [r["indice"] for r in e["pris"]] == list(range(1, 65))
        assert [r["indice_remise"] for r in e["reserve"]] == list(range(65, 73))


def passes(reel, d, initiale, renvois=None, code1=1, code2=0):
    ri = ecrire_jsonl(d / "remise-ecrivain-v1.jsonl", initiale)
    assert lancer(reel.args("verifier", d, "--passe", 1, "--remise", ri)) == code1
    autres = [ecrire_jsonl(d / "remise-ecrivain-renvois-v1.jsonl", renvois)] if renvois is not None else []
    assert lancer(reel.args("verifier", d, "--passe", 2, "--remise", ri, *autres)) == code2
    return selection_de(d) if (d / vp.SELECTION).exists() else None


def fautive(c, k):
    """Paire factice en défaut à C6 (`fear`, A1) au premier passage."""
    return {"phrase_concept": phrases_factices(c, k)[0][:-1] + " in fear."}


def test_passe2_retraits_reserve_et_non_rendue(extrait, reel, tmp_path):
    d = copie(extrait, tmp_path)
    initiale = remise_factice({("chats", 3): fautive("chats", 3), ("chats", 10): fautive("chats", 10),
                               ("meteo", 5): fautive("meteo", 5)})
    renvois = [enregistrement("chats", 3),                                     # rendue juste : gardée
               enregistrement("chats", 10, phrase_concept="The cat naps 9 times."),  # second défaut : retirée
               ]                                                               # meteo/5 non rendue : retirée
    s = passes(reel, d, initiale, renvois)
    ch, me = s["concepts"]["chats"], s["concepts"]["meteo"]
    assert ch["n"] == 64 and 10 not in ch["valides"] and ch["table_indices"]["11"] == 10 and ch["table_indices"]["65"] == 64
    assert [r for r in ch["pris"] if r["indice_remise"] == 3][0]["reecrite"] is True
    assert me["n"] == 64 and 5 not in me["valides"]
    motifs = {(r["concept"], r["indice_remise"]): r["motifs"] for r in s["retraits"]}
    assert set(motifs) == {("chats", 10), ("meteo", 5)} and motifs[("meteo", 5)][0]["motif"] == "non rendue"
    j = (d / "journal-verification-passe2-v1.txt").read_text(encoding="utf-8")
    assert "Retraits définitifs (second défaut) : 2" in j and "code 0" in j


def test_passe2_conflits_cc16(extrait, reel, tmp_path):
    d = copie(extrait, tmp_path)
    neuve = "The small tabby usually dozes on the windowsill near the back porch in the morning."
    initiale = remise_factice({(c, k): fautive(c, k) for c, k in
                               (("chats", 3), ("chats", 4), ("chats", 7), ("chats", 8), ("chats", 9))})
    renvois = [
        enregistrement("chats", 3, phrase_concept=phrases_factices("chats", 20)[0]),   # = paire non renvoyée : retirée
        enregistrement("chats", 4, phrase_concept=neuve,                                # réécrites en conflit : gardée
                       phrase_neutre="The small kettle usually stands on the windowsill near the back pantry in the late morning."),
        enregistrement("chats", 7, phrase_concept=neuve,                                # rang le plus élevé : retirée
                       phrase_neutre="The small teapot usually stands on the windowsill near the back pantry in the late evening."),
        enregistrement("chats", 8, phrase_concept=neuve.replace("dozes", "dozes in fear"),   # C6 : retirée d'abord
                       phrase_neutre="The small ladle usually hangs on the windowsill near the back pantry in the late morning."),
        enregistrement("chats", 9, phrase_concept=neuve.replace("dozes", "dozes in shade"),  # à distance 1 de 8 seulement
                       phrase_neutre="The small candle usually sits on the windowsill near the old pantry in the late morning."),
    ]
    s = passes(reel, d, initiale, renvois)
    retraits = {r["indice_remise"]: r["motifs"] for r in s["retraits"] if r["concept"] == "chats"}
    assert set(retraits) == {3, 7, 8}, retraits
    assert any(m["controle"] == "C8" and m["valeurs"]["paire_en_conflit"] == "chats/20" for m in retraits[3])
    assert any(m["controle"] == "C8" and m["valeurs"]["paire_en_conflit"] == "chats/4" for m in retraits[7])
    assert any(m["controle"] == "C6" for m in retraits[8]) and not any(m["controle"] == "C8" for m in retraits[8])
    assert {4, 9} <= set(s["concepts"]["chats"]["valides"])


def test_passe2_plancher_et_sous_le_plancher(extrait, reel, tmp_path):
    d = copie(extrait, tmp_path / "a")
    initiale = remise_factice({("chats", k): fautive("chats", k) for k in range(1, 10)})
    s = passes(reel, d, initiale, renvois=[])
    assert s["concepts"]["chats"]["n"] == 63 and s["concepts"]["chats"]["statut"] == "plancher" and s["code_passe2"] == 0
    assert "[RÉSERVE] chats : 63 paires" in (d / "journal-verification-passe2-v1.txt").read_text(encoding="utf-8")
    d = copie(extrait, tmp_path / "b")
    initiale = remise_factice({("chats", k): fautive("chats", k) for k in range(1, 18)})
    s = passes(reel, d, initiale, renvois=[], code2=1)
    assert s["concepts"]["chats"]["n"] == 55 and s["concepts"]["chats"]["statut"] == "sous-plancher" and s["code_passe2"] == 1


def test_passe2_artefact_paire_non_renvoyee_dans_la_remise_des_renvois(extrait, reel, tmp_path):
    d = copie(extrait, tmp_path)
    s = passes(reel, d, remise_factice({("chats", 3): fautive("chats", 3)}),
               [enregistrement("chats", 3), enregistrement("chats", 4)], code2=1)
    assert s["code_passe2"] == 1 and s["concepts"]["chats"]["n"] == 64
    assert "paire non renvoyée dans la remise des renvois" in (d / "journal-verification-passe2-v1.txt").read_text()


def test_passe2_artefact_remise_des_renvois_absente(extrait, reel, tmp_path, capsys):
    d = copie(extrait, tmp_path)
    ri = ecrire_jsonl(d / "remise-ecrivain-v1.jsonl", remise_factice({("chats", 3): fautive("chats", 3)}))
    assert lancer(reel.args("verifier", d, "--passe", 1, "--remise", ri)) == 1
    assert lancer(reel.args("verifier", d, "--passe", 2, "--remise", ri)) == 2
    assert "la remise des renvois est exigée" in capsys.readouterr().err


# ======================================================================================================================
# C11, C12 ; mode `assembler` (CC-05, CC-06) et `rejouer-c12`
# ======================================================================================================================

def selection_factice(ote=()) -> dict:
    valides = {c: [paire(c, k) for k in range(1, 73) if (c, k) not in ote] for c in vp.CONCEPTS}
    return {"concepts": vp.selectionner(valides)}


def test_c11_cas_sain_et_deux_assemblages(ctx):
    sel = selection_factice()
    assert vp.controle_c11_selection(sel) == []
    o1, o2 = vp.octets_assemblage(ctx, sel), vp.octets_assemblage(ctx, sel)
    assert o1 == o2
    defs, paires, n = vp.controle_c11_octets(ctx, o1)
    assert defs == [] and n == {c: 64 for c in vp.CONCEPTS} and len(paires) == 256
    assert o1.split(b"\n")[0] == b'{"format_lecture": "message_utilisateur"}'
    assert json.loads(o1.split(b"\n")[1]) == {"concept": "chats", "indice": 1, "phrase_concept": phrases_factices("chats", 1)[0],
                                              "phrase_neutre": phrases_factices("chats", 1)[1]}


def test_c11_artefact_deux_entrees_differentes_empreintes_differentes(ctx):
    a = vp.octets_assemblage(ctx, selection_factice())
    b = vp.octets_assemblage(ctx, selection_factice(ote={("meteo", 3)}))
    assert hashlib.sha256(a).hexdigest() != hashlib.sha256(b).hexdigest()


@pytest.mark.parametrize("cas,motif", [
    ("premiere-ligne-absente", "≠ bloc `format-lecture`"),
    ("premiere-ligne-cle-en-plus", "aucune autre clé"),
    ("valeur-hors-FORMATS_LECTURE", "aucune autre clé"),
    ("trois-concepts", "3 concept(s) seulement"),
    ("indices-avec-un-trou", "sans trou ni répétition"),
    ("domaine-neutre-garde", "domaine_neutre ôté"),
])
def test_c11_artefacts_octets(ctx, cas, motif):
    lignes = vp.octets_assemblage(ctx, selection_factice()).decode().split("\n")[:-1]
    if cas == "premiere-ligne-absente":
        lignes = lignes[1:]
    elif cas == "premiere-ligne-cle-en-plus":
        lignes[0] = '{"format_lecture": "message_utilisateur", "x": 1}'
    elif cas == "valeur-hors-FORMATS_LECTURE":
        lignes[0] = '{"format_lecture": "gabarit_action"}'
    elif cas == "trois-concepts":
        lignes = [l for l in lignes if '"geographie"' not in l]
    elif cas == "indices-avec-un-trou":
        lignes[5] = lignes[5].replace('"indice": 5,', '"indice": 99,')
    else:
        o = json.loads(lignes[3])
        lignes[3] = json.dumps({"concept": o["concept"], "indice": o["indice"], "domaine_neutre": "N3",
                                "phrase_concept": o["phrase_concept"], "phrase_neutre": o["phrase_neutre"]})
    defs, _, _ = vp.controle_c11_octets(ctx, ("\n".join(lignes) + "\n").encode())
    assert any(motif in d["motif"] for d in defs), defs


@pytest.mark.parametrize("cas,motif", [("trois-concepts", "3 concept(s) seulement"), ("n-55", "n = 55 < 56"),
                                       ("indices-avec-un-trou", "de 1 à n sans trou")])
def test_c11_artefacts_selection(cas, motif):
    sel = selection_factice(ote={("chats", k) for k in range(1, 18)} if cas == "n-55" else ())
    if cas == "trois-concepts":
        del sel["concepts"]["sports"]
    if cas == "indices-avec-un-trou":
        sel["concepts"]["meteo"]["pris"][-1]["indice"] = 65
    assert any(motif in d["motif"] for d in vp.controle_c11_selection(sel))


def ecrire_fichier(tmp_path, lignes) -> Path:
    f = tmp_path / "phrases.jsonl"
    f.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return f


def test_c12_cas_sain(ctx, tmp_path):
    f = tmp_path / "ok.jsonl"
    f.write_bytes(vp.octets_assemblage(ctx, selection_factice()))
    assert vp.controle_c12(ctx, f, {c: 64 for c in vp.CONCEPTS}) == []


@pytest.mark.parametrize("cas,motif", [
    ("premiere-ligne-absente", "le module refuse"),
    ("premiere-ligne-fautive", "le module refuse"),
    ("cle-en-trop", "le module refuse"),
    ("moins-de-quatre-concepts", "le module refuse"),
    ("indice-repete", "entiers uniques de 1 à n"),
    ("phrase-de-plus-de-128-jetons", "jetons > 128"),
])
def test_c12_artefacts(ctx, tmp_path, cas, motif):
    lignes = vp.octets_assemblage(ctx, selection_factice()).decode().split("\n")[:-1]
    if cas == "premiere-ligne-absente":
        lignes = lignes[1:]
    elif cas == "premiere-ligne-fautive":
        lignes[0] = '{"format_lecture": "gabarit_action"}'
    elif cas == "cle-en-trop":
        o = json.loads(lignes[2]) | {"x": 1}
        lignes[2] = json.dumps(o)
    elif cas == "moins-de-quatre-concepts":
        lignes = [l for l in lignes if '"sports"' not in l]
    elif cas == "indice-repete":
        lignes[2] = lignes[2].replace('"indice": 2,', '"indice": 1,')
    else:
        o = json.loads(lignes[2])
        o["phrase_concept"] = phrase_de(ctx, 129)
        lignes[2] = json.dumps(o)
    d = vp.controle_c12(ctx, ecrire_fichier(tmp_path, lignes), None)
    assert any(motif in x["motif"] for x in d), d


def test_assembler_cas_sain_puis_rejouer_c12(sain, reel, tmp_path):
    d = copie(sain, tmp_path)
    assert lancer(reel.args("assembler", d)) == 0
    f = d / vp.FICHIER_ASSEMBLE
    assert vp.lire_compagnon(f) == hashlib.sha256(f.read_bytes()).hexdigest()
    sel = selection_de(d)
    attendu = [json.dumps({"concept": c, "indice": r["indice"], "phrase_concept": r["phrase_concept"],
                           "phrase_neutre": r["phrase_neutre"]}) for c in vp.CONCEPTS for r in sel["concepts"][c]["pris"]]
    assert f.read_text().split("\n")[:-1] == ['{"format_lecture": "message_utilisateur"}'] + attendu
    j = (d / vp.JOURNAL_ASSEMBLAGE).read_text(encoding="utf-8")
    for x in ("[OK] C11 — deux assemblages", "[OK] C11 — forme des octets", "[OK] C12 — forme par le module sur une copie",
              "[OK] C10", "écrit, relu égal à l'octet, scellé", "code 0"):
        assert x in j
    assert lancer(reel.args("rejouer-c12", d, "--fichier", f)) == 0
    assert "[OK] C12" in (d / "journal-c12-8dc1cb09-v1.txt").read_text(encoding="utf-8")


def test_assembler_refuse_si_le_fichier_existe(sain, reel, tmp_path, capsys):
    d = copie(sain, tmp_path)
    (d / vp.FICHIER_ASSEMBLE).write_text("x\n")
    assert lancer(reel.args("assembler", d)) == 2
    assert "R12" in capsys.readouterr().err and (d / vp.FICHIER_ASSEMBLE).read_text() == "x\n"


def test_assembler_artefact_c11_refus_code_2_et_nom_final_absent(sain, reel, tmp_path, capsys):
    """CC-05, CC-06 : une sélection à n = 55 pour un concept (scellée, code 0 forcé) : refus, code 2, rien d'écrit."""
    d = copie(sain, tmp_path)
    s = selection_de(d)
    s["concepts"]["chats"] = vp.selectionner({"chats": [paire("chats", k) for k in range(18, 73)]})["chats"]
    f = d / "selection-essai-v1.json"
    f.write_bytes(vp.json_canonique(s))
    _sceller(f)
    assert lancer(reel.args("assembler", d, "--selection", f.name)) == 2
    assert "C11 — sélection refusée" in capsys.readouterr().err
    assert not (d / vp.FICHIER_ASSEMBLE).exists() and not (d / vp.JOURNAL_ASSEMBLAGE).exists()


def test_assembler_artefact_c12_refus_code_2_et_nom_final_absent(sain, reel, tmp_path, monkeypatch, capsys):
    d = copie(sain, tmp_path)
    monkeypatch.setattr(vp, "controle_c12", lambda ctx, chemin, attendus: [vp.defaut_lieu("fichier", "C12", "refus simulé")])
    assert lancer(reel.args("assembler", d)) == 2
    assert "assemblage refusé" in capsys.readouterr().err and not (d / vp.FICHIER_ASSEMBLE).exists()


def test_assembler_artefact_selection_du_second_passage_en_code_1(extrait, reel, tmp_path, capsys):
    d = copie(extrait, tmp_path)
    passes(reel, d, remise_factice({("chats", k): fautive("chats", k) for k in range(1, 18)}), renvois=[], code2=1)
    assert lancer(reel.args("assembler", d)) == 2
    assert "aucun assemblage" in capsys.readouterr().err


# ======================================================================================================================
# C13 — mesures et réserves
# ======================================================================================================================

def mesurer(ctx, paires):
    _, _, jetons = vp.controle_c3(ctx, paires)
    return vp.mesures_c13(ctx, paires, jetons, vp.Journal("essai"), "essai")


def tout_le_factice():
    return [paire(c, k) for c in vp.CONCEPTS for k in range(1, 65)]


def test_c13_cas_sain(ctx):
    mesures, reserves = mesurer(ctx, tout_le_factice())
    assert reserves == [] and all(m["noyau_employees"] >= 8 for m in mesures.values())


def test_c13_artefact_cat_seul(ctx):
    ps = [p if p.concept != "chats" else paire("chats", p.indice, phrase_concept=p.phrase_concept.replace(
        GABARITS["chats"][1][(p.indice - 1) % 9], "cat")) for p in tout_le_factice()]
    _, reserves = mesurer(ctx, ps)
    assert any("chats : 1 entrée(s) du noyau" in r for r in reserves)
    assert any("chats : l'entrée 'cat/cats' est dans 64 phrases" in r for r in reserves)


def test_c13_artefact_two_dans_une_seule_phrase(ctx):
    ps = tout_le_factice()
    ps[70] = paire("meteo", 7, phrase_concept=phrases_factices("meteo", 7)[0].replace("A ", "Two ", 1).replace(" often drifts", " often drift"))
    _, reserves = mesurer(ctx, ps)
    assert any("meteo : 1 paire(s) sans les mêmes mots de nombre" in r and "meteo/7" in r for r in reserves)


def test_c13_artefact_un_jeton_de_plus_dans_chaque_phrase_du_concept(ctx):
    ps = [paire(p.concept, p.indice, phrase_concept=p.phrase_concept[:-1] + " now.") for p in tout_le_factice()]
    for p in ps[:5]:
        n = vp.compter_jetons(ctx.tok, p.phrase_concept) - vp.compter_jetons(ctx.tok, p.phrase_neutre)
        assert n >= 1
    _, reserves = mesurer(ctx, ps)
    assert any("chats : moyenne signée +0.0" in r for r in reserves)


def test_c13_artefact_premier_mot(ctx):
    ps = [paire("chats", p.indice, phrase_concept="One" + p.phrase_concept[3:]) if p.concept == "chats" else p
          for p in tout_le_factice()]
    _, reserves = mesurer(ctx, ps)
    assert any("chats : le premier mot 'the' ouvre 64/64 phrases (phrase_neutre) et 0/64" in r for r in reserves)


# ======================================================================================================================
# Section 7 : `echantillon` (R9) et `decompter` (CC-15)
# ======================================================================================================================

def test_echantillon_graines_et_aveugle(sain, reel, tmp_path):
    d1, d2 = copie(sain, tmp_path / "a"), copie(sain, tmp_path / "b")
    for d in (d1, d2):
        assert lancer(reel.args("echantillon", d, "--entropie", ENTROPIE_ESSAI)) == 0
    assert (d1 / vp.ECHANTILLON).read_bytes() == (d2 / vp.ECHANTILLON).read_bytes()
    ech = json.loads((d1 / vp.ECHANTILLON).read_text())
    cle = json.loads((d1 / vp.CLE_ECHANTILLON).read_text())
    assert len(ech["items"]) == 28 and all(set(it) == {"item", "phrase_A", "phrase_B"} for it in ech["items"])
    assert cle["entropie"] == str(ENTROPIE_ESSAI) and cle["entropie_imposee"] is True
    assert {c: sum(1 for it in cle["items"] if it["concept"] == c) for c in vp.CONCEPTS} == {c: 7 for c in vp.CONCEPTS}
    sel = selection_de(d1)
    for c in vp.CONCEPTS:                                       # R9 : le tirage se rejoue depuis la clé, par numpy seul
        g = cle["graines"][f"echantillon-{c}"]
        assert int(g["spawn_key"][0]) == int.from_bytes(hashlib.sha256(f"echantillon-{c}".encode()).digest()[:8], "big")
        ss = np.random.SeedSequence(int(g["entropie"]), spawn_key=(int(g["spawn_key"][0]),))
        tires = sorted(int(i) + 1 for i in np.random.default_rng(ss).choice(64, size=7, replace=False))
        assert sorted(it["indice"] for it in cle["items"] if it["concept"] == c) == tires
    for it, k in zip(ech["items"], cle["items"]):
        r = sel["concepts"][k["concept"]]["pris"][k["indice"] - 1]
        assert it[f"phrase_{k['place_concept']}"] == r["phrase_concept"]
    assert "[ÉCART DÉCLARÉ] entropie imposée" in (d1 / vp.JOURNAL_ECHANTILLON).read_text(encoding="utf-8")
    d3 = copie(sain, tmp_path / "c")
    assert lancer(reel.args("echantillon", d3)) == 0
    c3 = json.loads((d3 / vp.CLE_ECHANTILLON).read_text())
    assert c3["entropie_imposee"] is False and c3["entropie"] != str(ENTROPIE_ESSAI) and int(c3["entropie"]) >= 2 ** 64


def test_echantillon_artefact_selection_en_code_1(extrait, reel, tmp_path, capsys):
    d = copie(extrait, tmp_path)
    passes(reel, d, remise_factice({("chats", k): fautive("chats", k) for k in range(1, 18)}), renvois=[], code2=1)
    assert lancer(reel.args("echantillon", d, "--entropie", ENTROPIE_ESSAI)) == 2
    assert "aucun échantillon" in capsys.readouterr().err


@pytest.fixture
def echantillonne(sain, reel, tmp_path):
    d = copie(sain, tmp_path)
    assert lancer(reel.args("echantillon", d, "--entropie", ENTROPIE_ESSAI)) == 0
    return d


def reponses(d: Path, defauts: dict | None = None) -> dict:
    """Réponses conformes tirées de la clé ; `defauts` : {item: {clé: valeur}}."""
    ech = json.loads((d / vp.ECHANTILLON).read_text())
    cle = json.loads((d / vp.CLE_ECHANTILLON).read_text())
    items = []
    for it, k in zip(ech["items"], cle["items"]):
        pc = k["place_concept"]
        q1 = {pc: k["concept"], ("B" if pc == "A" else "A"): "aucun"}
        e = {"item": it["item"], "Q1_A": q1["A"], "Q1_B": q1["B"], "Q2": "oui", "Q3_A": "non", "Q3_B": "non",
             "Q4_A": "non", "citation_Q4_A": None, "Q4_B": "non", "citation_Q4_B": None, "Q5_A": "oui", "Q5_B": "oui"}
        e.update((defauts or {}).get(it["item"], {}))
        items.append(e)
    f = d / vp.REPONSES
    f.write_text(json.dumps({"items": items}, indent=1), encoding="utf-8")
    _sceller(f)
    return cle


def items_de(cle, c):
    return [it for it in cle["items"] if it["concept"] == c]


def test_decompter_cas_sain_quatre_acceptes(echantillonne, reel):
    reponses(echantillonne)
    assert lancer(reel.args("decompter", echantillonne)) == 0
    dc = json.loads((echantillonne / vp.DECOMPTE).read_text())
    assert dc["acceptes"] == list(vp.CONCEPTS) and not (echantillonne / vp.SELECTION_V2).exists()


def test_decompter_une_non_conforme_retiree_et_remplacee(echantillonne, reel):
    cle = json.loads((echantillonne / vp.CLE_ECHANTILLON).read_text())
    it = items_de(cle, "sports")[0]
    reponses(echantillonne, {it["item"]: {"Q2": "non"}})
    assert lancer(reel.args("decompter", echantillonne)) == 0
    s2 = json.loads((echantillonne / vp.SELECTION_V2).read_text())
    sp = s2["concepts"]["sports"]
    assert sp["n"] == 64 and it["indice_remise"] not in [r["indice_remise"] for r in sp["pris"]]
    assert sp["pris"][-1]["indice_remise"] == 65 and s2["retraits_contre_verification"] == {"sports": [it["indice_remise"]]}
    assert s2["code_passe2"] == 0
    assert lancer(reel.args("assembler", echantillonne, "--selection", vp.SELECTION_V2)) == 0


def test_decompter_deux_non_conformes_reecriture_prime_sur_q4(echantillonne, reel):
    cle = json.loads((echantillonne / vp.CLE_ECHANTILLON).read_text())
    a, b = items_de(cle, "meteo")[:2]
    ech = {x["item"]: x for x in json.loads((echantillonne / vp.ECHANTILLON).read_text())["items"]}
    mot = ech[a["item"]]["phrase_A"].split()[1]
    reponses(echantillonne, {a["item"]: {"Q4_A": "oui", "citation_Q4_A": mot}, b["item"]: {"Q5_B": "non"}})
    assert lancer(reel.args("decompter", echantillonne)) == 1
    dc = json.loads((echantillonne / vp.DECOMPTE).read_text())
    assert dc["concepts"]["meteo"]["decision"].startswith("réécriture") and "meteo" not in dc["acceptes"]
    assert not (echantillonne / vp.SELECTION_V2).exists()


def test_decompter_un_oui_a_q4_second_lecteur(echantillonne, reel):
    cle = json.loads((echantillonne / vp.CLE_ECHANTILLON).read_text())
    a = items_de(cle, "geographie")[0]
    ech = {x["item"]: x for x in json.loads((echantillonne / vp.ECHANTILLON).read_text())["items"]}
    reponses(echantillonne, {a["item"]: {"Q4_B": "oui", "citation_Q4_B": ech[a["item"]]["phrase_B"][4:15]}})
    assert lancer(reel.args("decompter", echantillonne)) == 1
    dc = json.loads((echantillonne / vp.DECOMPTE).read_text())
    assert dc["concepts"]["geographie"]["decision"].startswith("second lecteur de Q4")


def test_decompter_artefact_q4_sans_citation(echantillonne, reel, capsys):
    cle = json.loads((echantillonne / vp.CLE_ECHANTILLON).read_text())
    reponses(echantillonne, {cle["items"][0]["item"]: {"Q4_A": "oui", "citation_Q4_A": "texte absent de la phrase"}})
    assert lancer(reel.args("decompter", echantillonne)) == 2
    assert "sans citation tirée de la phrase" in capsys.readouterr().err


def test_decompter_artefact_reponses_non_scellees(echantillonne, reel, capsys):
    reponses(echantillonne)
    Path(str(echantillonne / vp.REPONSES) + ".sha256").unlink()
    assert lancer(reel.args("decompter", echantillonne)) == 2
    assert "compagnon" in capsys.readouterr().err
