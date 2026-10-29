"""Lentille jacobienne contre lentille des logits, appliquées aux directions des sondes de P3 — v1.

Rédigé le 29 octobre 2026 sur le « yes go » de Lazar (08:26, heure de Paris). **Exploratoire, processeur seul, non
préenregistré, non opposable** : aucun chiffre sorti de ce script ne sert de critère de porte.

Ce que fait le script (sous-commande `comparer`) :
- relit `diag/<run>/sondes-figees.json` (sceau vérifié) et le fichier de poids des sondes
  `donnees/<run>/sondes-figees-legeres.npz` (format de `src/controle_ia/premier_test_ia/figees.py` : clé `index` = JSON
  en octets, tableaux `s<k>_w`, `s<k>_q`… ; empreinte du fichier contrôlée contre `sondes_legeres_sha256`, empreinte de
  chaque sonde recalculée comme dans `src/controle_ia/sondes/familles.py`) ;
- pour chaque sonde retenue (par défaut : la famille de la sonde principale de chaque concept, aux couches 7, 15 et 23),
  prend la direction w (activations brutes, normalisation repliée) et la décode :
    * lentille des logits : logits = W_U · (g ⊙ v / rms(v)),  v = w ;
    * lentille jacobienne : même chose avec v = J_l · w  (J_l : jacobienne moyenne de la couche l vers la dernière
      couche, format du dépôt `anthropics/jacobian-lens`) ;
  W_U = poids de désembedding (`lm_head.weight`, forme [vocabulaire, largeur]), g = gain de la normalisation finale
  (`model.norm.weight`). Pour une direction seule, la normalisation RMS n'agit que par un facteur positif : le classement
  des jetons ne dépend pas de l'échelle de w, et la direction −w donne exactement les logits opposés (pas de biais) ;
- sort, pour chaque sonde, chaque lentille et chaque signe (+ : vers la classe positive, trompeur ou enjeux élevés ;
  − : vers la classe négative), les k jetons de tête (k = 20), leur version restreinte aux jetons « mots » (même règle
  que `jlens/vis.py::_meaningful_token_mask`), les recouvrements entre lentilles, et une cohérence avec une liste de
  mots du concept (option `--concepts`) : nombre de jetons du concept dans la tête, meilleur rang, et un score
  z = (moyenne des logits des jetons du concept − moyenne sur le vocabulaire) / écart type sur le vocabulaire, comparé à
  deux références nulles passées par la même lentille : les directions « plancher » appariées en covariance de P3
  (si elles sont à la même couche) et des directions isotropes tirées par `numpy.random.SeedSequence` (R9) ;
- variantes facultatives : `--covariances` (motif d'activation a = Σ·w, lecture « ce que la sonde voit » plutôt que
  « ce qu'elle lit ») ; `--activations-moyennes` (lentille appliquée à h̄ ± α‖h̄‖ŵ autour d'une activation moyenne,
  différence des logits ; la normalisation y redevient non linéaire) ;
- écrit la sortie JSON, un manifeste (empreintes des entrées, versions, graines, commande) et leurs empreintes
  compagnons au format `sha256sum` ; refuse d'écraser (R12).

Refus nommés (code de sortie 2, ligne « REFUS <code> : … ») : entrée absente, sceau absent ou faux, sonde introuvable ou
d'empreinte fausse, couche absente de la lentille, dimensions discordantes, sortie existante, lentille `.pt` sans torch.

Sous-commande `convertir-lentille` (exige torch, à lancer sur l'instance) : lit un fichier de lentille `.pt` du dépôt
(`torch.load(..., weights_only=True)`, clés `J`, `n_prompts`, `source_layers`, `d_model`), garde les couches demandées et
écrit un `.npz` (clés `J_<couche>`, `n_prompts`, `d_model`, `source_layers`), lisible ici sans torch.

Usage (exemple sur l'instance, depuis la racine du dépôt) :
  python3 -I -B <ce script> comparer \\
     --sondes-json diag/20261019-230011-p3-reel/sondes-figees.json \\
     --sondes-npz donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz \\
     --lentille lentille-llama-3.1-8b-instruct-c7-c15-c23.npz \\
     --desembedding <modele>/model.safetensors.index.json:lm_head.weight \\
     --norme-finale <modele>/model.safetensors.index.json:model.norm.weight \\
     --vocabulaire <modele>/tokenizer.json \\
     --concepts concepts-sondes-p3-v1.json \\
     --sortie sortie-jlens-sondes-p3-v1.json
Spécification d'un tableau : `chemin.npy`, `chemin.npz:cle`, `chemin.safetensors:nom` ou
`model.safetensors.index.json:nom` (le fragment est résolu par `weight_map`).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import struct
import sys
import time
from pathlib import Path

import numpy as np

VERSION = "v1"
GRAINE_DEFAUT = 20261029
EPS_RMS_LLAMA = 1e-5          # rms_norm_eps de Llama-3.1-8B-Instruct (config.json), utilisé seulement en variante « autour »
TAILLE_BLOC = 16384           # lignes de W_U traitées à la fois


class Refus(Exception):
    def __init__(self, code: str, message: str):
        super().__init__(f"{code} : {message}")
        self.code = code


# --------------------------------------------------------------------------------------------------------------------
# Fichiers, empreintes

def sha256_fichier(chemin) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 22), b""):
            h.update(bloc)
    return h.hexdigest()


def exiger(chemin, quoi: str) -> Path:
    p = Path(chemin)
    if not p.is_file():
        raise Refus("entree-absente", f"{quoi} introuvable : {p}")
    return p


def verifier_compagnon(chemin: Path, obligatoire: bool) -> str | None:
    """Empreinte compagnon `<fichier>.sha256` (format sha256sum). Rend l'empreinte vérifiée, ou None si absente."""
    comp = Path(str(chemin) + ".sha256")
    if not comp.is_file():
        if obligatoire:
            raise Refus("sceau-absent", f"{comp} absent")
        return None
    lignes = [l for l in comp.read_text(encoding="utf-8").splitlines() if l.strip()]
    if len(lignes) != 1 or len(lignes[0].split()) != 2:
        raise Refus("sceau-illisible", f"{comp}")
    attendue, nom = lignes[0].split()
    if nom != chemin.name:
        raise Refus("sceau-faux", f"{comp} nomme {nom!r}, pas {chemin.name!r}")
    reelle = sha256_fichier(chemin)
    if reelle != attendue:
        raise Refus("sceau-faux", f"{chemin} : empreinte {reelle[:12]}… ≠ sceau {attendue[:12]}…")
    return reelle


def ecrire_scelle(chemin: Path, texte: str) -> str:
    if chemin.exists() or Path(str(chemin) + ".sha256").exists():
        raise Refus("sortie-existe", f"{chemin} existe déjà (R12)")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(texte, encoding="utf-8")
    sha = sha256_fichier(chemin)
    Path(str(chemin) + ".sha256").write_text(f"{sha}  {chemin.name}\n", encoding="utf-8")
    return sha


# --------------------------------------------------------------------------------------------------------------------
# Sondes (format de figees.py, relu sans torch)

def empreinte_sonde(famille, nom, couche, agregation, tableaux) -> str:
    """Copie de `sondes.familles._empreinte` appliquée à f"{famille}:{nom}"."""
    h = hashlib.sha256(f"{famille}:{nom}/{couche}/{agregation}".encode("utf-8"))
    for t in tableaux:
        h.update(np.ascontiguousarray(t, dtype=np.float64).tobytes())
    return h.hexdigest()


ORDRE_TABLEAUX = {"SondeLineaireJetons": ("w", "b", "q"), "SondeLineaire": ("w", "b", "q"),
                  "SondePerceptron": ("mu", "s", "W", "c", "v", "b", "q"), "SondeMahalanobis": ("mu", "P")}


def lire_sondes_npz(chemin: Path) -> tuple[dict, dict]:
    with np.load(chemin, allow_pickle=False) as z:
        if "index" not in z.files:
            raise Refus("sondes-npz-illisible", f"{chemin} : clé « index » absente (format de figees.py attendu)")
        index = json.loads(bytes(z["index"]).decode("utf-8"))
        sondes = {}
        for k, e in enumerate(index["sondes"]):
            t = {n: np.asarray(z[f"s{k}_{n}"], dtype=np.float64) for n in e["tableaux"]}
            classe = e["classe"]
            if classe not in ORDRE_TABLEAUX:
                raise Refus("sondes-npz-illisible", f"classe {classe!r} inconnue")
            ordre = []
            for n in ORDRE_TABLEAUX[classe]:
                if n == "b":
                    ordre.append(np.array([e["b"]], dtype=np.float64))
                elif n in t:
                    ordre.append(t[n])
            if classe == "SondeLineaire":      # harnais.sondes.SondeLineaire : empreinte non recopiée ici
                emp = None
            else:
                fam = e["famille"] if e.get("famille") is not None else {"SondePerceptron": "perceptron",
                                                                           "SondeMahalanobis": "mahalanobis"}.get(classe)
                emp = empreinte_sonde(fam, e["nom"], e["couche"], e["agregation"], ordre)
            if emp is not None and emp != e["empreinte"]:
                raise Refus("empreinte-sonde", f"{e['nom']} : empreinte recalculée {emp[:12]}… ≠ écrite {e['empreinte'][:12]}…")
            sondes[e["nom"]] = {**{c: e[c] for c in ("classe", "nom", "couche", "agregation", "famille", "b", "empreinte")},
                                "tableaux": t}
    return sondes, index.get("meta", {})


def choisir_sondes(fig: dict, sondes_npz: dict, mode: str) -> list[dict]:
    res = fig["resultat"]
    entrees = {s["nom"]: s for s in res["sondes"]}
    choix = []
    if mode == "principales-par-couche":
        for concept, nom_p in sorted(res["principales"].items()):
            if nom_p not in entrees:
                raise Refus("sonde-introuvable", f"principale {nom_p} absente de sondes-figees.json")
            p = entrees[nom_p]
            if p["classe"] != "SondeLineaireJetons":
                raise Refus("principale-non-lineaire", f"{nom_p} est {p['classe']} : pas une direction")
            soeurs = sorted((s for s in res["sondes"] if s["famille"] == p["famille"] and s["nom"].startswith(concept + "-")
                             and s["famille"] != "plancher"), key=lambda s: s["couche"])
            for s in soeurs:
                choix.append({"concept": concept, "principale": s["nom"] == nom_p, **s})
    elif mode == "toutes-lineaires":
        princ = set(res["principales"].values())
        for s in res["sondes"]:
            if s["classe"] == "SondeLineaireJetons" and s["famille"] != "plancher":
                choix.append({"concept": s["nom"].split("-")[0], "principale": s["nom"] in princ, **s})
    else:
        raise Refus("parametre", f"mode de sondes {mode!r} inconnu")
    for c in choix:
        if c["nom"] not in sondes_npz:
            raise Refus("sonde-introuvable", f"{c['nom']} absente du fichier de poids")
        n = sondes_npz[c["nom"]]
        if n["empreinte"] != c["empreinte"] or int(n["couche"]) != int(c["couche"]):
            raise Refus("empreinte-sonde", f"{c['nom']} : le fichier de poids ne porte pas la sonde de sondes-figees.json")
    return choix


# --------------------------------------------------------------------------------------------------------------------
# Lentille

def lire_lentille(chemin: Path, couches: list[int]) -> tuple[dict, dict]:
    if chemin.suffix == ".npz":
        with np.load(chemin, allow_pickle=False) as z:
            J = {}
            for c in couches:
                cle = f"J_{c}"
                if cle not in z.files:
                    raise Refus("couche-absente-lentille", f"{chemin} : pas de clé {cle} (clés : {sorted(z.files)[:12]}…)")
                J[c] = np.asarray(z[cle], dtype=np.float64)
            meta = {k: (z[k].tolist() if k in z.files else None) for k in ("n_prompts", "d_model", "source_layers")}
    elif chemin.suffix == ".pt":
        try:
            import torch
        except ImportError:
            raise Refus("torch-absent-pour-pt", "lentille .pt : convertir d'abord en .npz par `convertir-lentille` "
                        "sur une machine qui a torch") from None
        ck = torch.load(str(chemin), map_location="cpu", weights_only=True)
        if "J" not in ck:
            raise Refus("lentille-illisible", f"{chemin} : clé « J » absente (point de reprise de fit() ?)")
        J = {}
        for c in couches:
            if c not in ck["J"]:
                raise Refus("couche-absente-lentille", f"{chemin} : couche {c} absente ({sorted(ck['J'])})")
            J[c] = ck["J"][c].float().numpy().astype(np.float64)
        meta = {"n_prompts": ck.get("n_prompts"), "d_model": ck.get("d_model"), "source_layers": ck.get("source_layers")}
    else:
        raise Refus("lentille-illisible", f"{chemin} : .npz ou .pt attendu")
    for c, m in J.items():
        if m.ndim != 2 or m.shape[0] != m.shape[1]:
            raise Refus("dimension", f"J_{c} de forme {m.shape} : carrée attendue")
        if not np.all(np.isfinite(m)):
            raise Refus("lentille-non-finie", f"J_{c} contient des valeurs non finies")
    return J, meta


# --------------------------------------------------------------------------------------------------------------------
# Poids : npy, npz, safetensors (lu en numpy, sans la bibliothèque safetensors)

_DTYPES_ST = {"F32": np.float32, "F16": np.float16, "F64": np.float64, "BF16": "bf16"}


def _lire_safetensors(chemin: Path, nom: str) -> np.ndarray:
    with open(chemin, "rb") as f:
        n = struct.unpack("<Q", f.read(8))[0]
        if n > 100_000_000:
            raise Refus("poids-illisibles", f"{chemin} : en-tête safetensors démesuré")
        entete = json.loads(f.read(n).decode("utf-8"))
    if nom not in entete:
        raise Refus("poids-introuvables", f"{chemin} : tenseur {nom!r} absent")
    e = entete[nom]
    debut, fin = e["data_offsets"]
    if e["dtype"] not in _DTYPES_ST:
        raise Refus("poids-illisibles", f"{nom} : type {e['dtype']} non pris en charge")
    brut = np.memmap(chemin, dtype=np.uint8, mode="r", offset=8 + n + debut, shape=(fin - debut,))
    if _DTYPES_ST[e["dtype"]] == "bf16":
        u = np.frombuffer(brut, dtype="<u2")
        x = (u.astype(np.uint32) << 16).view(np.float32)
    else:
        x = np.frombuffer(brut, dtype=np.dtype(_DTYPES_ST[e["dtype"]]).newbyteorder("<")).astype(np.float32)
    if x.size != int(np.prod(e["shape"])):
        raise Refus("poids-illisibles", f"{nom} : taille {x.size} ≠ forme {e['shape']}")
    return x.reshape(e["shape"])


def lire_tableau(spec: str, quoi: str) -> tuple[np.ndarray, list[Path]]:
    """Rend le tableau en float32 et la liste des fichiers effectivement lus (pour le manifeste)."""
    chemin, _, cle = spec.partition(":")
    p = exiger(chemin, quoi)
    if p.name.endswith(".safetensors.index.json"):
        carte = json.loads(p.read_text(encoding="utf-8")).get("weight_map", {})
        if cle not in carte:
            raise Refus("poids-introuvables", f"{p} : {cle!r} absent de weight_map")
        fragment = exiger(p.parent / carte[cle], f"fragment de {quoi}")
        return _lire_safetensors(fragment, cle), [p, fragment]
    if p.suffix == ".safetensors":
        return _lire_safetensors(p, cle), [p]
    if p.suffix == ".npy":
        return np.load(p, allow_pickle=False).astype(np.float32), [p]
    if p.suffix == ".npz":
        with np.load(p, allow_pickle=False) as z:
            if cle not in z.files:
                raise Refus("poids-introuvables", f"{p} : clé {cle!r} absente")
            return np.asarray(z[cle], dtype=np.float32), [p]
    raise Refus("poids-illisibles", f"{p} : format non reconnu (npy, npz:cle, safetensors:nom, index.json:nom)")


# --------------------------------------------------------------------------------------------------------------------
# Vocabulaire

def _octets_vers_unicode() -> dict[int, str]:
    """Table de l'encodage par octets de GPT-2, reprise par les tokenizer.json « ByteLevel » (Llama 3 compris)."""
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs = bs[:]
    n = 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return dict(zip(bs, (chr(c) for c in cs)))


def lire_vocabulaire(chemin: Path, taille: int) -> tuple[list[str], dict]:
    info = {"format": None, "jetons_lus": 0, "manquants": 0}
    textes: list[str | None] = [None] * taille
    if chemin.suffix == ".json":
        d = json.loads(chemin.read_text(encoding="utf-8"))
        if isinstance(d, list):
            info["format"] = "liste"
            for i, t in enumerate(d[:taille]):
                textes[i] = str(t)
        else:
            info["format"] = "tokenizer.json"
            inverse = {v: k for k, v in _octets_vers_unicode().items()}
            octets = isinstance(d.get("pre_tokenizer"), dict) or isinstance(d.get("decoder"), dict)
            for s, i in d["model"]["vocab"].items():
                if 0 <= i < taille:
                    if octets and all(ch in inverse for ch in s):
                        textes[i] = bytes(inverse[ch] for ch in s).decode("utf-8", errors="replace")
                    else:
                        textes[i] = s.replace("▁", " ")
            for a in d.get("added_tokens", []):
                if 0 <= a["id"] < taille:
                    textes[a["id"]] = a["content"]
    else:
        info["format"] = "texte, un jeton par ligne"
        for i, l in enumerate(chemin.read_text(encoding="utf-8").split("\n")[:taille]):
            textes[i] = l
    info["jetons_lus"] = sum(t is not None for t in textes)
    info["manquants"] = taille - info["jetons_lus"]
    return [t if t is not None else f"<id {i}>" for i, t in enumerate(textes)], info


def masque_mots(textes: list[str]) -> np.ndarray:
    """Même règle que jlens/vis.py::_meaningful_token_mask."""
    m = np.zeros(len(textes), dtype=bool)
    for i, t in enumerate(textes):
        s = t.strip()
        if not s or "<|" in s or (s.startswith("<") and s.endswith(">")):
            continue
        m[i] = all(ch.isalnum() or (0 < k < len(s) - 1 and ch in "'-’") for k, ch in enumerate(s))
    return m


def jetons_du_concept(textes: list[str], mots: list[str], prefixe: bool) -> tuple[list[int], list[str]]:
    cibles = {m.strip().lower() for m in mots if m.strip()}
    ids, trouves = [], set()
    for i, t in enumerate(textes):
        s = t.strip().lower()
        if not s or s.startswith("<id "):
            continue
        if s in cibles:
            ids.append(i)
            trouves.add(s)
        elif prefixe and len(s) >= 4 and any(c.startswith(s) or s.startswith(c) for c in cibles):
            ids.append(i)
            trouves.update(c for c in cibles if c.startswith(s) or s.startswith(c))
    return ids, sorted(cibles - trouves)


# --------------------------------------------------------------------------------------------------------------------
# Désembedding : statistiques du vocabulaire (moyenne, Gram) pour les scores z sans matrice [V, n]

class Desembedding:
    def __init__(self, WU: np.ndarray):
        self.WU = WU                                   # float32 [V, d]
        V, d = WU.shape
        self.moyenne = np.zeros(d)
        self.gram = np.zeros((d, d))
        for a in range(0, V, TAILLE_BLOC):
            R = WU[a:a + TAILLE_BLOC].astype(np.float64)
            self.moyenne += R.sum(axis=0)
            self.gram += R.T @ R
        self.moyenne /= V
        self.gram /= V

    def logits(self, y: np.ndarray) -> np.ndarray:
        return (self.WU @ y.astype(np.float32)).astype(np.float64)

    def z_lot(self, Y: np.ndarray, moyenne_concept: np.ndarray) -> np.ndarray:
        """Y [d, n] : z_j = ((c̄ − m)·y_j) / sqrt(y_jᵀ G y_j − (m·y_j)²)."""
        num = (moyenne_concept - self.moyenne) @ Y
        var = np.sum(Y * (self.gram @ Y), axis=0) - (self.moyenne @ Y) ** 2
        return num / np.sqrt(np.maximum(var, 1e-300))


# --------------------------------------------------------------------------------------------------------------------
# Lentilles appliquées à des directions

def rms(x, axis=0, eps=0.0):
    return np.sqrt(np.mean(x * x, axis=axis, keepdims=True) + eps)


def vers_sortie(V: np.ndarray, transport: np.ndarray | None, g: np.ndarray, variante: str, ctx: dict) -> np.ndarray:
    """Directions V [d, n] (espace de la couche) → vecteurs y [d, n] tels que logits = W_U · y.
    transport = J_l (lentille jacobienne) ou None (lentille des logits)."""
    T = (lambda X: X) if transport is None else (lambda X: transport @ X)
    if variante == "direction":
        U = T(V)
        return g[:, None] * U / rms(U)
    if variante == "motif":
        S = ctx["covariance"]
        A = (S[:, None] * V) if S.ndim == 1 else S @ V
        U = T(A)
        return g[:, None] * U / rms(U)
    if variante == "autour":
        h = ctx["activation_moyenne"][:, None]
        Vn = V / np.linalg.norm(V, axis=0, keepdims=True)
        pas = ctx["alpha"] * np.linalg.norm(h)
        Up, Um = T(h + pas * Vn), T(h - pas * Vn)
        return g[:, None] * (Up / rms(Up, eps=EPS_RMS_LLAMA) - Um / rms(Um, eps=EPS_RMS_LLAMA))
    raise Refus("parametre", f"variante {variante!r} inconnue")


def tete(logits: np.ndarray, textes: list[str], k: int, masque: np.ndarray | None = None) -> list[dict]:
    x = logits if masque is None else np.where(masque, logits, -np.inf)
    idx = np.argpartition(-x, k)[:k]
    idx = idx[np.argsort(-x[idx], kind="stable")]
    return [{"id": int(i), "texte": textes[i], "logit": round(float(logits[i]), 6)} for i in idx]


def recouvrement(a: list[dict], b: list[dict]) -> dict:
    A, B = {t["id"] for t in a}, {t["id"] for t in b}
    return {"intersection": len(A & B), "jaccard": round(len(A & B) / max(1, len(A | B)), 6),
            "communs": sorted(t["texte"] for t in a if t["id"] in B)}


def p_haut(z: float, nuls: np.ndarray) -> float:
    return float((1 + np.sum(nuls >= z)) / (len(nuls) + 1))


def graines_aleatoires(graine: int, etiquette: str) -> np.random.SeedSequence:
    cle = int.from_bytes(hashlib.sha256(etiquette.encode("utf-8")).digest()[:8], "little")
    return np.random.SeedSequence(entropy=graine, spawn_key=(cle,))


# --------------------------------------------------------------------------------------------------------------------
# Comparer

def comparer(a) -> int:
    t0 = time.time()
    sortie = Path(a.sortie)
    manifeste_ch = sortie.with_name(sortie.stem + "-manifeste.json")
    for p in (sortie, manifeste_ch):
        if p.exists() or Path(str(p) + ".sha256").exists():
            raise Refus("sortie-existe", f"{p} existe déjà (R12)")
    lus: dict[str, Path] = {}

    # Sondes
    p_json = exiger(a.sondes_json, "sondes-figees.json")
    verifier_compagnon(p_json, obligatoire=True)
    fig = json.loads(p_json.read_text(encoding="utf-8"))
    lus["sondes_json"] = p_json
    p_npz = exiger(a.sondes_npz, "fichier de poids des sondes (sondes-figees-legeres.npz)")
    sha_npz = sha256_fichier(p_npz)
    attendue = a.sha256_sondes_npz or fig["resultat"].get("sondes_legeres_sha256")
    if a.sha256_sondes_npz is None and p_npz.name == "sondes-figees.npz":
        attendue = fig["resultat"].get("sondes_figees_sha256")
    if sha_npz != attendue:
        raise Refus("empreinte-sondes-npz", f"{p_npz} : {sha_npz[:12]}… ≠ attendue {str(attendue)[:12]}… "
                    "(sondes_legeres_sha256 de sondes-figees.json)")
    lus["sondes_npz"] = p_npz
    sondes_npz, meta_npz = lire_sondes_npz(p_npz)
    choix = choisir_sondes(fig, sondes_npz, a.sondes)
    couches = sorted({int(c["couche"]) for c in choix})

    # Lentille, poids, vocabulaire
    p_lent = exiger(a.lentille, "fichier de lentille")
    J, meta_lent = lire_lentille(p_lent, couches)
    lus["lentille"] = p_lent
    WU, f_wu = lire_tableau(a.desembedding, "désembedding")
    g, f_g = lire_tableau(a.norme_finale, "normalisation finale")
    for i, f in enumerate(f_wu):
        lus[f"desembedding_{i}"] = f
    for i, f in enumerate(f_g):
        lus[f"norme_finale_{i}"] = f
    g = g.astype(np.float64).reshape(-1)
    if WU.ndim != 2:
        raise Refus("dimension", f"désembedding de forme {WU.shape} : [vocabulaire, largeur] attendu")
    Vt, d = WU.shape
    tailles = {"désembedding (colonnes)": d, "normalisation finale": g.size,
               **{f"J_{c}": J[c].shape[0] for c in couches},
               **{c["nom"]: sondes_npz[c["nom"]]["tableaux"]["w"].size for c in choix}}
    if len(set(tailles.values())) != 1:
        raise Refus("dimension", f"largeurs discordantes : {tailles}")
    p_voc = exiger(a.vocabulaire, "vocabulaire")
    lus["vocabulaire"] = p_voc
    textes, info_voc = lire_vocabulaire(p_voc, Vt)
    mots = masque_mots(textes)

    # Concepts
    concepts = {}
    if a.concepts:
        p_c = exiger(a.concepts, "liste de mots des concepts")
        lus["concepts"] = p_c
        for nom, liste in json.loads(p_c.read_text(encoding="utf-8")).items():
            if nom.startswith("_"):
                continue
            ids, sans = jetons_du_concept(textes, liste, a.correspondance == "prefixe")
            concepts[nom] = {"mots": liste, "jetons": [{"id": i, "texte": textes[i]} for i in ids], "mots_sans_jeton": sans}

    # Variantes
    ctx_par_couche = {c: {} for c in couches}
    variantes = ["direction"]
    if a.covariances:
        p_cov = exiger(a.covariances, "covariances")
        lus["covariances"] = p_cov
        with np.load(p_cov, allow_pickle=False) as z:
            for c in couches:
                if f"c{c}" not in z.files:
                    raise Refus("couche-absente-covariances", f"{p_cov} : clé c{c} absente")
                S = np.asarray(z[f"c{c}"], dtype=np.float64)
                if S.shape not in ((d,), (d, d)):
                    raise Refus("dimension", f"covariance c{c} de forme {S.shape}")
                ctx_par_couche[c]["covariance"] = S
        variantes.append("motif")
    if a.activations_moyennes:
        p_am = exiger(a.activations_moyennes, "activations moyennes")
        lus["activations_moyennes"] = p_am
        with np.load(p_am, allow_pickle=False) as z:
            for c in couches:
                if f"c{c}" not in z.files:
                    raise Refus("couche-absente-activations", f"{p_am} : clé c{c} absente")
                h = np.asarray(z[f"c{c}"], dtype=np.float64).reshape(-1)
                if h.size != d:
                    raise Refus("dimension", f"activation moyenne c{c} de taille {h.size}")
                ctx_par_couche[c].update(activation_moyenne=h, alpha=a.alpha)
        variantes.append("autour")

    de = Desembedding(WU)

    # Références nulles : planchers de P3 à la même couche, et directions isotropes (SeedSequence)
    planchers = {}
    for concept, noms in (meta_npz.get("planchers") or {}).items():
        for n in noms:
            if n in sondes_npz:
                s = sondes_npz[n]
                planchers.setdefault((concept, int(s["couche"])), []).append(s["tableaux"]["w"])
    graines = {}
    aleatoires = {}
    for c in couches:
        ss = graines_aleatoires(a.graine, f"aleatoire/c{c}")
        graines[f"aleatoire/c{c}"] = {"entropie": str(ss.entropy), "spawn_key": [str(x) for x in ss.spawn_key]}
        aleatoires[c] = np.random.default_rng(ss).standard_normal((d, a.n_aleatoires))

    resultats = []
    for c in choix:
        s = sondes_npz[c["nom"]]
        w = s["tableaux"]["w"]
        L = int(c["couche"])
        entree = {"nom": c["nom"], "concept": c["concept"], "principale": c["principale"], "famille": c["famille"],
                  "couche": L, "classe": c["classe"], "agregation": c["agregation"], "empreinte": c["empreinte"],
                  "biais_b": s["b"], "norme_w": float(np.linalg.norm(w)),
                  "norme_Jw_sur_norme_w": float(np.linalg.norm(J[L] @ w) / np.linalg.norm(w)),
                  "cosinus_w_Jw": float(w @ (J[L] @ w) / (np.linalg.norm(w) * np.linalg.norm(J[L] @ w))),
                  "variantes": {}}
        for var in variantes:
            ctx = ctx_par_couche[L]
            bloc = {}
            logits_par_lentille = {}
            for lentille, T in (("logits", None), ("jacobienne", J[L])):
                y = vers_sortie(w[:, None], T, g, var, ctx)[:, 0]
                lg = de.logits(y)
                logits_par_lentille[lentille] = lg
                r = {"plus": {"tete": tete(lg, textes, a.k), "tete_mots": tete(lg, textes, a.k, mots)},
                     "moins": {"tete": tete(-lg, textes, a.k), "tete_mots": tete(-lg, textes, a.k, mots)}}
                coh = {}
                for nom_c, info_c in concepts.items():
                    ids = np.array([j["id"] for j in info_c["jetons"]], dtype=int)
                    if ids.size == 0:
                        coh[nom_c] = {"statut": "concept-sans-jeton"}
                        continue
                    cbar = WU[ids].astype(np.float64).mean(axis=0)
                    z = float(de.z_lot(y[:, None], cbar)[0])
                    z_direct = float((lg[ids].mean() - lg.mean()) / lg.std())
                    if not np.isclose(z, z_direct, rtol=1e-4, atol=1e-4):      # logits en simple précision
                        raise Refus("incoherence-interne", f"score z par Gram {z} ≠ direct {z_direct}")
                    rangs = np.empty(Vt, dtype=int)
                    rangs[np.argsort(-lg, kind="stable")] = np.arange(1, Vt + 1)
                    tete_p = {t["id"] for t in r["plus"]["tete"]}
                    tete_m = {t["id"] for t in r["moins"]["tete"]}
                    item = {"z": z, "jetons_concept": int(ids.size),
                            "n_concept_tete_plus": len(tete_p & set(ids.tolist())),
                            "n_concept_tete_moins": len(tete_m & set(ids.tolist())),
                            "meilleur_rang_plus": int(rangs[ids].min()),
                            "meilleur_rang_moins": int((Vt + 1 - rangs[ids]).min())}
                    Yn = vers_sortie(aleatoires[L], T, g, var, ctx)
                    zn = de.z_lot(Yn, cbar)
                    item["aleatoires"] = {"n": int(zn.size), "p_haut": p_haut(z, zn), "p_bas": p_haut(-z, -zn),
                                          "p_bilateral": p_haut(abs(z), np.abs(zn)),
                                          "z_quantiles_5_50_95": [float(q) for q in np.quantile(zn, [0.05, 0.5, 0.95])]}
                    pl = planchers.get((c["concept"], L))
                    if pl:
                        zp = de.z_lot(vers_sortie(np.stack(pl, axis=1), T, g, var, ctx), cbar)
                        item["planchers"] = {"n": int(zp.size), "p_haut": p_haut(z, zp), "p_bas": p_haut(-z, -zp),
                                             "p_bilateral": p_haut(abs(z), np.abs(zp)),
                                             "z_quantiles_5_50_95": [float(q) for q in np.quantile(zp, [0.05, 0.5, 0.95])]}
                    else:
                        item["planchers"] = {"statut": "pas de plancher de ce concept à cette couche"}
                    coh[nom_c] = item
                r["coherence"] = coh
                bloc[lentille] = r
            a_, b_ = logits_par_lentille["logits"], logits_par_lentille["jacobienne"]
            ac, bc = a_ - a_.mean(), b_ - b_.mean()
            bloc["recouvrement"] = {
                "plus": recouvrement(bloc["logits"]["plus"]["tete"], bloc["jacobienne"]["plus"]["tete"]),
                "moins": recouvrement(bloc["logits"]["moins"]["tete"], bloc["jacobienne"]["moins"]["tete"]),
                "plus_mots": recouvrement(bloc["logits"]["plus"]["tete_mots"], bloc["jacobienne"]["plus"]["tete_mots"]),
                "moins_mots": recouvrement(bloc["logits"]["moins"]["tete_mots"], bloc["jacobienne"]["moins"]["tete_mots"]),
                "cosinus_logits_centres": float(ac @ bc / (np.linalg.norm(ac) * np.linalg.norm(bc)))}
            entree["variantes"][var] = bloc
        resultats.append(entree)

    corps = {
        "version": VERSION, "statut": "exploratoire, non préenregistré, non opposable",
        "lecture_des_signes": "plus = direction +w (vers la classe 1 : consigne malhonnête pour « tromperie », "
                              "« high-stakes » pour « enjeux ») ; moins = −w",
        "run_sondes": fig.get("run_id"), "principales": fig["resultat"].get("principales"),
        "lentille_meta": meta_lent, "largeur": d, "vocabulaire": {"taille_desembedding": Vt, **info_voc,
                                                                  "jetons_mots": int(mots.sum())},
        "parametres": {"k": a.k, "n_aleatoires": a.n_aleatoires, "graine": a.graine, "sondes": a.sondes,
                       "variantes": variantes, "alpha": a.alpha if a.activations_moyennes else None,
                       "correspondance": a.correspondance},
        "concepts": concepts, "sondes": resultats,
    }
    sha_sortie = ecrire_scelle(sortie, json.dumps(corps, ensure_ascii=False, indent=1) + "\n")
    try:
        import torch  # noqa: F401
        v_torch = torch.__version__
    except ImportError:
        v_torch = None
    manifeste = {
        "script": str(Path(__file__).name), "script_sha256": sha256_fichier(__file__), "version": VERSION,
        "commande": [Path(sys.executable).name, *sys.argv],
        "drapeaux_python": {"isolated": sys.flags.isolated, "dont_write_bytecode": sys.flags.dont_write_bytecode},
        "cree_le_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "duree_s": round(time.time() - t0, 2),
        "versions": {"python": sys.version.split()[0], "numpy": np.__version__, "torch": v_torch,
                     "plateforme": platform.platform()},
        "entrees": {k: {"chemin": str(p), "sha256": sha256_fichier(p), "octets": p.stat().st_size} for k, p in lus.items()},
        "graines": {"mode": "numpy.random.SeedSequence(entropy=graine, spawn_key=(sha256(etiquette)[:8],))", **graines},
        "sortie": {"chemin": sortie.name, "sha256": sha_sortie},
    }
    ecrire_scelle(manifeste_ch, json.dumps(manifeste, ensure_ascii=False, indent=1) + "\n")
    print(f"sortie : {sortie} ({sha_sortie[:12]}…) ; manifeste : {manifeste_ch} ; {len(resultats)} sondes, "
          f"variantes {variantes}")
    return 0


# --------------------------------------------------------------------------------------------------------------------
# Convertir une lentille .pt en .npz (exige torch)

def convertir_lentille(a) -> int:
    try:
        import torch
    except ImportError:
        raise Refus("torch-absent-pour-pt", "convertir-lentille exige torch") from None
    p = exiger(a.pt, "lentille .pt")
    sortie = Path(a.sortie)
    if sortie.exists():
        raise Refus("sortie-existe", f"{sortie} existe déjà (R12)")
    ck = torch.load(str(p), map_location="cpu", weights_only=True)
    if "J" not in ck:
        raise Refus("lentille-illisible", f"{p} : clé « J » absente")
    tab = {}
    for c in a.couches:
        if c not in ck["J"]:
            raise Refus("couche-absente-lentille", f"{p} : couche {c} absente ({sorted(ck['J'])})")
        tab[f"J_{c}"] = ck["J"][c].to(torch.float16).numpy()
    tab["n_prompts"] = np.array(ck.get("n_prompts", -1))
    tab["d_model"] = np.array(ck.get("d_model", -1))
    tab["source_layers"] = np.array(ck.get("source_layers", []))
    with open(sortie, "wb") as f:
        np.savez(f, **tab)
    sha = sha256_fichier(sortie)
    Path(str(sortie) + ".sha256").write_text(f"{sha}  {sortie.name}\n", encoding="utf-8")
    print(f"{sortie} : couches {a.couches}, empreinte {sha} (source {p.name} : {sha256_fichier(p)})")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sp = ap.add_subparsers(dest="commande", required=True)
    c = sp.add_parser("comparer")
    c.add_argument("--sondes-json", required=True)
    c.add_argument("--sondes-npz", required=True)
    c.add_argument("--sha256-sondes-npz", default=None, help="empreinte attendue (défaut : celle de sondes-figees.json)")
    c.add_argument("--lentille", required=True)
    c.add_argument("--desembedding", required=True)
    c.add_argument("--norme-finale", required=True)
    c.add_argument("--vocabulaire", required=True)
    c.add_argument("--concepts", default=None)
    c.add_argument("--correspondance", choices=("exacte", "prefixe"), default="exacte")
    c.add_argument("--sondes", choices=("principales-par-couche", "toutes-lineaires"), default="principales-par-couche")
    c.add_argument("--covariances", default=None, help="npz, clés c<couche> : (d,) variances ou (d, d) covariance")
    c.add_argument("--activations-moyennes", default=None, help="npz, clés c<couche> : (d,)")
    c.add_argument("--alpha", type=float, default=0.1)
    c.add_argument("--k", type=int, default=20)
    c.add_argument("--n-aleatoires", type=int, default=200)
    c.add_argument("--graine", type=int, default=GRAINE_DEFAUT)
    c.add_argument("--sortie", required=True)
    v = sp.add_parser("convertir-lentille")
    v.add_argument("--pt", required=True)
    v.add_argument("--couches", type=int, nargs="+", default=[7, 15, 23])
    v.add_argument("--sortie", required=True)
    a = ap.parse_args(argv)
    try:
        return comparer(a) if a.commande == "comparer" else convertir_lentille(a)
    except Refus as e:
        print(f"REFUS {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
