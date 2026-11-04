"""Mise à disposition aveugle (texte scellé, section « Mise à disposition aveugle »).

- Entropie **secrète** : 128 bits par `secrets.randbits` au moment de la mise à disposition, écrits au coffre seul,
  engagés par leur empreinte (sha256 du secret écrit en 32 chiffres hexadécimaux) dans le manifeste ; jamais dérivés
  de l'empreinte publique du préenregistrement. Une `SeedSequence` sur ce secret (R9) tire le pile ou face A/B et les
  noms de cas en hexadécimal.
- Copies servies : exactement `config.json`, `model.safetensors` (bf16, tenseurs triés, métadonnées `{"format": "pt"}`),
  `tokenizer.json`, `tokenizer_config.json`, comme la manche « outil d'attention » des auteurs (journaux,
  `code/make_release.py` : l. 16-17 et l. 40-56, MIT) ; `generation_config.json` et `chat_template.jinja` retirés des
  deux (option permise par le texte) ; dates de modification normalisées.
- Contrôle de fuite `controle_fuite()` : garde éprouvée sur un cas sain et sur des artefacts (R5) par les essais.
- Le code qui sert les modèles aux lecteurs (`harnais.py`, `outil_attention.py`) n'importe pas ce module et ne reçoit
  jamais le chemin du coffre.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import secrets
import shutil
import struct
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

FICHIERS_SERVIS = ("config.json", "model.safetensors", "tokenizer.json", "tokenizer_config.json")
FICHIERS_TOKENISEUR = ("tokenizer.json", "tokenizer_config.json")
DATE_NORMALISEE = int(datetime(2026, 1, 1, tzinfo=timezone.utc).timestamp())
NOM_CAS = re.compile(r"^cas_[0-9a-f]{12}$")
CHAINES_INTERDITES = ("honest", "sycophant", "nul", "null", "/home", "/root", "/tmp", "coffre", "private", "prive",
                      "honnete", "honnête", "sycophante", "ancre", "etal", "reserve", "vraie")


class GardeFuite(RuntimeError):
    pass


class GardeCoffre(RuntimeError):
    pass


def sha256_fichier(p: str | Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


# --- tirage ---------------------------------------------------------------------------------------------------
def tirer_secret() -> int:
    return secrets.randbits(128)


def engagement(secret: int) -> str:
    return hashlib.sha256(f"{secret:032x}".encode()).hexdigest()


def tirer_attribution(secret: int, cas: list[str]) -> dict[str, dict]:
    """Pour chaque cas (identifiant interne), un nom hexadécimal et un pile ou face : `premier_en_A` vrai si le premier
    modèle du cas (ordre du plan) est servi en A. Tout vient de la `SeedSequence` du secret."""
    if not 0 < secret < (1 << 128):
        raise GardeCoffre("secret hors de 128 bits")
    rng = np.random.default_rng(np.random.SeedSequence(secret))
    noms: set[str] = set()
    out = {}
    for c in cas:
        while True:
            nom = "cas_" + rng.bytes(6).hex()
            if nom not in noms:
                noms.add(nom)
                break
        out[c] = {"nom": nom, "premier_en_A": bool(rng.integers(0, 2))}
    return out


def ordre_lecteur(noms: list[str], rng: np.random.Generator) -> list[str]:
    """Ordre des cas propre à un lecteur (générateur de la tâche `ordre-des-cas-<lecteur>`)."""
    s = sorted(noms)
    return [s[i] for i in rng.permutation(len(s))]


# --- coffre ---------------------------------------------------------------------------------------------------
def verifier_emplacement_coffre(coffre: Path, interdits: list[Path]) -> None:
    c = coffre.resolve()
    for d in interdits:
        d = d.resolve()
        if c == d or d in c.parents or c in d.parents:
            raise GardeCoffre(f"coffre {c} mêlé à {d} (servi, dépôt ou bac à sable)")


def ecrire_coffre(coffre: Path, secret: int, cle: dict, *, interdits: list[Path]) -> dict:
    """Écrit `coffre/cle-v1.json` (droits 600, dossier 700) ; renvoie ce qui va au manifeste : l'engagement du secret
    et l'empreinte du fichier de clé (jamais la clé, jamais les empreintes des fichiers servis)."""
    verifier_emplacement_coffre(coffre, interdits)
    coffre.mkdir(parents=True, exist_ok=False)
    os.chmod(coffre, 0o700)
    chemin = coffre / "cle-v1.json"
    corps = {"secret_hex": f"{secret:032x}", "engagement": engagement(secret), "cle": cle,
             "ecrit_le": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    chemin.write_text(json.dumps(corps, indent=1, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    os.chmod(chemin, 0o600)
    with open(coffre / "journal-v1.txt", "a", encoding="utf-8") as j:
        j.write(f"{corps['ecrit_le']} écriture de la clé\n")
    return {"engagement_secret": corps["engagement"], "sha256_cle": sha256_fichier(chemin)}


def ouvrir_coffre(coffre: Path, sortie: Path, *, sha256_cle: str, reponses_scellees: list[Path],
                  sha256_script_analyse: str, attendues: int) -> dict:
    """Ouverture unique : exige toutes les réponses scellées (sceaux vérifiés) et l'empreinte du script d'analyse ;
    écrit une copie de la clé dans `sortie/cle-ouverte-v1.json` (scellée) et refuse toute seconde ouverture."""
    from ..scellement import sceller, verifier

    marque = coffre / "ouvert-v1.json"
    if marque.exists():
        raise GardeCoffre("coffre déjà ouvert : lire la copie scellée de la première ouverture")
    if len(reponses_scellees) != attendues:
        raise GardeCoffre(f"{len(reponses_scellees)} réponses scellées, {attendues} attendues")
    for r in reponses_scellees:
        verifier(r)
    if not re.fullmatch(r"[0-9a-f]{64}", sha256_script_analyse or ""):
        raise GardeCoffre("empreinte du script d'analyse absente")
    chemin = coffre / "cle-v1.json"
    if sha256_fichier(chemin) != sha256_cle:
        raise GardeCoffre("clé du coffre altérée (empreinte ≠ manifeste)")
    corps = json.loads(chemin.read_text(encoding="utf-8"))
    if engagement(int(corps["secret_hex"], 16)) != corps["engagement"]:
        raise GardeCoffre("secret ≠ engagement")
    quand = datetime.now(timezone.utc).isoformat(timespec="seconds")
    sortie.mkdir(parents=True, exist_ok=True)
    copie = sortie / "cle-ouverte-v1.json"
    if copie.exists():
        raise GardeCoffre(f"{copie} existe déjà (R12)")
    copie.write_text(json.dumps({"ouvert_le": quand, "sha256_script_analyse": sha256_script_analyse, **corps},
                                indent=1, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    sceller(copie)
    marque.write_text(json.dumps({"ouvert_le": quand}), encoding="utf-8")
    with open(coffre / "journal-v1.txt", "a", encoding="utf-8") as j:
        j.write(f"{quand} ouverture unique ; script d'analyse {sha256_script_analyse}\n")
    return corps


# --- copies servies -------------------------------------------------------------------------------------------
def entete_safetensors(p: Path) -> tuple[dict, int]:
    with open(p, "rb") as f:
        n = struct.unpack("<Q", f.read(8))[0]
        return json.loads(f.read(n)), n


def ecrire_safetensors(tenseurs: dict, chemin: Path) -> None:
    from safetensors.torch import save_file

    save_file(dict(sorted(tenseurs.items())), str(chemin), metadata={"format": "pt"})


def normaliser_dates(racine: Path) -> None:
    for p in sorted(racine.rglob("*"), reverse=True):
        os.utime(p, (DATE_NORMALISEE, DATE_NORMALISEE), follow_symlinks=False)
    os.utime(racine, (DATE_NORMALISEE, DATE_NORMALISEE))


def servir_cas(dest: Path, tenseurs_A: dict, tenseurs_B: dict, config_json: bytes, dossier_tokeniseur: Path) -> dict:
    """Écrit `dest/A` et `dest/B` ; renvoie les empreintes des fichiers servis (pour le coffre seul)."""
    if not NOM_CAS.match(dest.name):
        raise GardeFuite(f"nom de cas {dest.name!r} : hexadécimal tiré attendu")
    dest.mkdir(parents=True, exist_ok=False)
    emp = {}
    for lettre, t in (("A", tenseurs_A), ("B", tenseurs_B)):
        d = dest / lettre
        d.mkdir()
        ecrire_safetensors(t, d / "model.safetensors")
        (d / "config.json").write_bytes(config_json)
        for f in FICHIERS_TOKENISEUR:
            shutil.copyfile(dossier_tokeniseur / f, d / f)
        emp[lettre] = {f: sha256_fichier(d / f) for f in FICHIERS_SERVIS}
    normaliser_dates(dest)
    return emp


def _chaines_json(x) -> list[str]:
    if isinstance(x, dict):
        return [s for k, v in x.items() for s in [str(k)] + _chaines_json(v)]
    if isinstance(x, list):
        return [s for v in x for s in _chaines_json(v)]
    return [x] if isinstance(x, str) else []


def _interdites(chaines: list[str]) -> list[str]:
    trouve = []
    for s in chaines:
        b = s.lower()
        trouve += [f"{c!r} dans {s[:60]!r}" for c in CHAINES_INTERDITES if c in b]
    return trouve


def controle_fuite(dossier_cas: Path, *, sha_tokeniseur_reference: dict[str, str], taille_attendue: int | None = None) -> dict:
    """Garde de fuite d'un cas servi ; lève `GardeFuite` au premier défaut, renvoie un résumé sinon.

    Chaînes interdites cherchées dans les clés et valeurs textuelles de `config.json`, dans l'en-tête `safetensors`
    (noms, métadonnées) et dans les noms de fichiers ; les fichiers du tokéniseur, dont le vocabulaire contient ces
    mots, sont exigés identiques à l'octet à ceux du modèle de départ (référence), ce qui exclut qu'ils portent une
    étiquette."""
    d = Path(dossier_cas)
    if not NOM_CAS.match(d.name):
        raise GardeFuite(f"nom de cas {d.name!r}")
    if sorted(p.name for p in d.iterdir()) != ["A", "B"]:
        raise GardeFuite(f"{d} : contenu {sorted(p.name for p in d.iterdir())} au lieu de A, B")
    entetes, tailles = {}, {}
    for lettre in ("A", "B"):
        x = d / lettre
        noms = sorted(p.name for p in x.iterdir())
        if noms != sorted(FICHIERS_SERVIS):
            raise GardeFuite(f"{x} : fichiers {noms}")
        for f in FICHIERS_TOKENISEUR:
            if sha256_fichier(x / f) != sha_tokeniseur_reference[f]:
                raise GardeFuite(f"{x / f} ≠ tokéniseur du modèle de départ")
        cfg = json.loads((x / "config.json").read_text(encoding="utf-8"))
        h, n = entete_safetensors(x / "model.safetensors")
        meta = h.pop("__metadata__", None)
        if meta != {"format": "pt"}:
            raise GardeFuite(f"{x} : métadonnées safetensors {meta}")
        mauvaises = _interdites(_chaines_json(cfg) + list(h) + _chaines_json(meta))
        if mauvaises:
            raise GardeFuite(f"{x} : chaînes interdites {mauvaises[:3]}")
        entetes[lettre] = [(k, v["dtype"], v["shape"], v["data_offsets"]) for k, v in h.items()]
        if [k for k, *_ in entetes[lettre]] != sorted(h):
            raise GardeFuite(f"{x} : tenseurs non triés")
        tailles[lettre] = (x / "model.safetensors").stat().st_size
    if entetes["A"] != entetes["B"]:
        raise GardeFuite("A et B : ordre, formes, types ou décalages des tenseurs différents")
    if tailles["A"] != tailles["B"] or (taille_attendue is not None and tailles["A"] != taille_attendue):
        raise GardeFuite(f"tailles {tailles} (attendue {taille_attendue})")
    for f in ("config.json",) + FICHIERS_TOKENISEUR:
        if (d / "A" / f).read_bytes() != (d / "B" / f).read_bytes():
            raise GardeFuite(f"{f} diffère entre A et B")
    for p in [d] + list(d.rglob("*")):
        if int(p.lstat().st_mtime) != DATE_NORMALISEE:
            raise GardeFuite(f"{p} : date de modification non normalisée")
    return {"cas": d.name, "taille": tailles["A"], "n_tenseurs": len(entetes["A"])}
