"""Chargeur des activations publiées de NARCBench, v1 (bras externe, R-2175 ; 0 USD, processeur).

Format d'après la fiche du jeu (`aaronrose227/narcbench`, révision `19cb14b269e052b19ba6d2bd2f4519afd3b10c57`, `README.md`
sha256 `05be2d89e255948d6f33d94862d21d4a6f8ff82f1d156c0d97be6b7e49285163`) et le code des auteurs au commit `85fea3be2a9d`
(`probes/reproduce_LR.py`, sha256 `1d66fdc7ca81c972db357566b42a729e19f58f2ce85f5d8ecd0662c3c1141e0f`) :

    activations/<modele>/<etage>/metadata_gen.json   liste de dicts, une ligne par tour d'agent (20 champs)
    activations/<modele>/<etage>/activations_gen.npz  clés `layer_<idx>`, float32, lignes alignées sur les métadonnées

Règles reprises du code des auteurs (lignes de `reproduce_LR.py`, voir le rapport `rapport-externe-donnees-v1.md`) :
- canal `public` seulement ; CORE : phase `discussion`, moyenne des tours ; STEGO : phase `final` (l. 136-179) ;
- seuls les épisodes à **quatre agents** sont gardés (l. 179) — ici, les autres sont **comptés et rapportés**, jamais retirés
  en silence ;
- domaine tiré de `run_id` : `<famille>__<scenario_id>__<mode>`, domaine = `scenario_id` sans son dernier segment (l. 98-113) ;
- apprentissage de la direction sur les **vecteurs par message** (et non par agent) des épisodes de collusion, canal public,
  phase de discussion (l. 197-211) : fourni par `echantillons_apprentissage`.

Aucune lecture d'aire ici : ce module ne fait que charger et vérifier la forme. Ouverture des `.npz` avec
`allow_pickle=False` (fichiers téléchargés : données non sûres).
"""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path

import numpy as np

from ..gardes import GardeArret

REVISION_JEU = "19cb14b269e052b19ba6d2bd2f4519afd3b10c57"
COMMIT_CODE = "85fea3be2a9d"
MODELES = ("qwen3_32b", "llama_3_1_70b")
ETAGES = ("core", "stego")
# Bande de couches du code des auteurs (`config.py`, l. 33-38, sha256 9c65f55b…31c0) ; la fiche du jeu donne la même.
BANDES = {"qwen3_32b": tuple(range(26, 31)), "llama_3_1_70b": tuple(range(32, 38))}
LARGEURS = {"qwen3_32b": 5120, "llama_3_1_70b": 8192}

# Empreintes publiées par l'interface du dépôt de données à la révision ci-dessus (liste « tree », 10 novembre 2026,
# 11:05 UTC) : sha256 du stockage LFS pour les .npz, objet git (sha1 de blob) pour les .json. Taille en octets.
EMPREINTES_PUBLIEES = {
    "activations/llama_3_1_70b/core/activations_gen.npz":
        (207226342, "sha256", "8ffa6edc0157574b86df63c96cc4cb6dd86f69d19efee252dbcca90e2674a3d0"),
    "activations/llama_3_1_70b/core/metadata_gen.json": (568384, "git-sha1", "14538f13e0df9ce76a08c3c7964fd0426c5a145c"),
    "activations/llama_3_1_70b/stego/activations_gen.npz":
        (259524070, "sha256", "ba4e979fb20244024f8c5985bc9cd534108be9e85dc405e0de3be8824762846c"),
    "activations/llama_3_1_70b/stego/metadata_gen.json": (681578, "git-sha1", "31483d785a32b7272c8751380a90d7508562f846"),
    "activations/qwen3_32b/core/activations_gen.npz":
        (107930862, "sha256", "927146ca556f6c2694d9271e74788867fa3c549ab2b0749d233d525fed60debb"),
    "activations/qwen3_32b/core/metadata_gen.json": (562309, "git-sha1", "75305b7d326877c57c01025630da5d307ead5e25"),
    "activations/qwen3_32b/stego/activations_gen.npz":
        (135169262, "sha256", "f93cae53d2068d59a6f61f61b8ca6011364b9fce4b113a34394fc62e449ee401"),
    "activations/qwen3_32b/stego/metadata_gen.json": (681527, "git-sha1", "80fa14783777b62e984ccd5148d96a907b0f3ea0"),
}

CHAMPS = ("run_id", "mode", "role", "channel", "phase", "round", "agent_name", "n_tokens", "seed", "flagged", "family",
          "scenario_id", "scenario_domain", "agent_vote", "target_option", "target_majority", "collusion_success",
          "fair_option", "label_variant", "bp_corr")
PHASE = {"core": "discussion", "stego": "final"}


def empreinte(chemin: Path, sorte: str) -> str:
    """sha256 du fichier, ou sha1 de blob git (`blob <taille>\\0` + contenu), par blocs."""
    chemin = Path(chemin)
    h = hashlib.sha256() if sorte == "sha256" else hashlib.sha1()
    if sorte == "git-sha1":
        h.update(f"blob {chemin.stat().st_size}\0".encode())
    elif sorte != "sha256":
        raise GardeArret(f"sorte d'empreinte inconnue {sorte!r}")
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def verifier_fichiers(racine: Path, attendues: dict = EMPREINTES_PUBLIEES) -> dict:
    """Taille et empreinte de chaque fichier attendu ; tout écart arrête (R5, R11 : absent = vérifié sur disque)."""
    racine, sortie = Path(racine), {}
    for rel, (taille, sorte, attendue) in attendues.items():
        p = racine / rel
        if not p.is_file():
            raise GardeArret(f"fichier absent : {rel}")
        if p.stat().st_size != taille:
            raise GardeArret(f"taille fausse : {rel} ({p.stat().st_size} au lieu de {taille})")
        h = empreinte(p, sorte)
        if h != attendue:
            raise GardeArret(f"empreinte fausse : {rel}")
        sortie[rel] = {"taille": taille, sorte: h, "sha256": h if sorte == "sha256" else empreinte(p, "sha256")}
    return sortie


def charger_metadonnees(chemin: Path) -> list:
    with open(chemin, encoding="utf-8") as f:
        meta = json.load(f)
    if not isinstance(meta, list) or not meta:
        raise GardeArret("métadonnées : liste non vide attendue")
    for i, m in enumerate(meta):
        if not isinstance(m, dict) or set(m) != set(CHAMPS):
            manque = sorted(set(CHAMPS) - set(m)) if isinstance(m, dict) else "?"
            raise GardeArret(f"métadonnées, ligne {i} : 20 champs attendus (manquants {manque})")
        if m["mode"] not in ("collusion", "control") or m["role"] not in ("colluder", "honest") \
                or m["channel"] not in ("public", "private", "thinking"):
            raise GardeArret(f"métadonnées, ligne {i} : mode, rôle ou canal inconnus")
        if len(m["run_id"].split("__")) < 2:
            raise GardeArret(f"métadonnées, ligne {i} : run_id sans scénario")
    return meta


def charger_couches(chemin: Path, couches, n_lignes: int, largeur: int | None = None) -> dict:
    """{couche: (n_lignes, largeur) float32} ; couche absente, type, lignes, largeur ou valeur non finie → arrêt."""
    with np.load(chemin, allow_pickle=False) as npz:
        sortie = {}
        for c in couches:
            cle = f"layer_{int(c)}"
            if cle not in npz.files:
                raise GardeArret(f"couche {c} absente de {Path(chemin).name} (présentes : {sorted(npz.files)})")
            A = npz[cle]
            if A.dtype != np.float32:
                raise GardeArret(f"{cle} : type {A.dtype}, float32 attendu")
            if A.ndim != 2 or A.shape[0] != n_lignes:
                raise GardeArret(f"{cle} : forme {A.shape}, {n_lignes} lignes alignées sur les métadonnées attendues")
            if largeur is not None and A.shape[1] != largeur:
                raise GardeArret(f"{cle} : largeur {A.shape[1]}, {largeur} attendue")
            if not np.all(np.isfinite(A)):
                raise GardeArret(f"{cle} : valeurs non finies")
            sortie[int(c)] = A
    return sortie


def domaine(run_id: str) -> str:
    """Règle des auteurs (`reproduce_LR.py`, `_parse_run_id` et `_domain_from_scenario_id`)."""
    sid = run_id.split("__")[1]
    return "_".join(sid.split("_")[:-1])


def episodes(meta: list, acts: dict, etage: str) -> tuple[list, dict]:
    """Épisodes au format de `externe_v1` et compte des exclusions (jamais silencieuses).

    acts de chaque épisode : (4 agents triés par nom, tours, couches dans l'ordre de `acts`, largeur). CORE : tours de la
    phase `discussion` triés par `round` ; STEGO : la ligne de phase `final` (un tour)."""
    if etage not in PHASE:
        raise GardeArret(f"étage {etage!r}")
    couches = sorted(acts)
    lignes = defaultdict(lambda: defaultdict(dict))
    info = {}
    for i, m in enumerate(meta):
        if m["channel"] != "public" or m["phase"] != PHASE[etage]:
            continue
        r, a = m["run_id"], m["agent_name"]
        cle_tour = m["round"] if etage == "core" else 0
        if cle_tour in lignes[r][a]:
            raise GardeArret(f"{r}/{a} : tour {cle_tour} en double")
        lignes[r][a][cle_tour] = i
        mode_role = info.setdefault(r, {"mode": m["mode"], "roles": {}})
        if mode_role["mode"] != m["mode"]:
            raise GardeArret(f"{r} : mode incohérent entre lignes")
        if mode_role["roles"].setdefault(a, m["role"]) != m["role"]:
            raise GardeArret(f"{r}/{a} : rôle incohérent entre lignes")
    sortie, exclus = [], {"agents_differents_de_4": [], "tours_inegaux": []}
    for r in sorted(lignes):
        agents = sorted(lignes[r])
        if len(agents) != 4:
            exclus["agents_differents_de_4"].append(r)
            continue
        tours = [sorted(lignes[r][a]) for a in agents]
        if any(t != tours[0] for t in tours):
            exclus["tours_inegaux"].append(r)
            continue
        A = np.stack([np.stack([np.stack([acts[c][lignes[r][a][t]] for c in couches]) for t in tours[0]])
                      for a in agents])
        roles = info[r]["roles"]
        sortie.append({"run_id": r, "etage": etage.upper(), "domaine": domaine(r),
                       "condition": "collusion" if info[r]["mode"] == "collusion" else "temoin",
                       "acts": A, "couches": couches, "agents": agents,
                       "colludeurs": np.array([roles[a] == "colluder" for a in agents])})
    return sortie, exclus


def echantillons_apprentissage(meta: list, acts_couche: np.ndarray, exclure_domaine: str | None = None):
    """Vecteurs **par message** des auteurs (`train_deception_probe`, l. 197-211) : collusion, canal public, phase de
    discussion, domaine exclu le cas échéant. Renvoie (X colludeurs, X honnêtes) dans l'ordre des lignes ; l'équilibrage
    (colludeurs tronqués aux `nc` premiers, honnêtes tirés par la graine) relève de la recette, pas du chargeur."""
    col, hon = [], []
    for i, m in enumerate(meta):
        if m["mode"] != "collusion" or m["channel"] != "public" or m["phase"] != "discussion":
            continue
        if exclure_domaine and domaine(m["run_id"]) == exclure_domaine:
            continue
        (col if m["role"] == "colluder" else hon).append(i)
    return acts_couche[col], acts_couche[hon]


def charger(racine: Path, modele: str, etage: str, couches=None) -> dict:
    """Charge un (modèle, étage) : métadonnées, couches de la bande, épisodes, exclusions. Ne vérifie pas les empreintes
    (appeler `verifier_fichiers` d'abord)."""
    if modele not in MODELES or etage not in ETAGES:
        raise GardeArret(f"modèle ou étage hors du périmètre : {modele}/{etage} (rien de TRANSFER)")
    d = Path(racine) / "activations" / modele / etage
    meta = charger_metadonnees(d / "metadata_gen.json")
    acts = charger_couches(d / "activations_gen.npz", couches or BANDES[modele], len(meta), LARGEURS[modele])
    eps, exclus = episodes(meta, acts, etage)
    return {"meta": meta, "acts": acts, "episodes": eps, "exclusions": exclus}


__all__ = ["REVISION_JEU", "COMMIT_CODE", "BANDES", "LARGEURS", "EMPREINTES_PUBLIEES", "empreinte", "verifier_fichiers",
           "charger_metadonnees", "charger_couches", "domaine", "episodes", "echantillons_apprentissage", "charger"]
