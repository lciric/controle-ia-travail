"""Essai de régression de l'arrêt de l'étape A de T0.7 (R-2588 ; cause R-2589 ; correction (a), R-2593) — v1, fichier neuf.

Cause (diagnostic `docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/diagnostic-arret-cache-v1/` : note `194ca20e…`,
reproduction `reproduire_arret_cache_v1.py` `8a85a3f7…`, sortie `88360a5d…`) : pendant le préchargement en ligne
(`harnais.modeles.precharger_modele`, motifs `MOTIFS_PRECHARGEMENT`), `huggingface_hub` 1.33.0 écrit au cache la liste complète de
l'arbre du dépôt du modèle (`<cache>/models--…/trees/<commit>.json`, `_tree_cache.write_tree_cache`) ; `revision_au_cache`
(`t07/reextraction_p3_v1.py`) appelait ensuite `snapshot_download(local_files_only=True)` sans motifs, et la bibliothèque déclarait
incomplet (`IncompleteSnapshotError`) un instantané préchargé par motifs (10 fichiers sur 17, dossier `original/` exclu comme voulu).
Les caches factices des essais antérieurs n'avaient pas cette liste : leur cas sain n'était pas celui de l'instance (R4, R5).

Cache factice « comme après le préchargement » : les fichiers que `MOTIFS_PRECHARGEMENT` retient (par `filter_repo_objects`, le
filtre de la bibliothèque) parmi les 17 noms de l'arbre réel de `meta-llama/Llama-3.1-8B-Instruct` à la révision de P3 (liste de la
reproduction), contenus factices non vides, index des poids bien formé (quatre morceaux) ; plus la liste de l'arbre (les 17 noms)
écrite par `huggingface_hub._tree_cache.write_tree_cache`, comme en ligne.

Mémoire de la bibliothèque : `write_tree_cache` amorce aussi `_tree_cache._IN_MEMORY_TREE_CACHE`, que `read_tree_cache` consulte avant
le disque. Sur l'instance, préchargement et contrôle sont deux processus : le contrôle lit la liste sur le disque. Ici, la mémoire est
vidée avant et après chaque essai (fixation automatique) et après la construction de chaque cache ; chaque cache vérifie que sa liste
n'est pas en mémoire avant l'appel contrôlé, et les cas sains vérifient après l'appel que la liste a été lue sur le disque (présente)
ou jamais lue (absente). Le cas (vi) rejoue l'étape 8 du script v4 dans un processus neuf, sans aucune mémoire partagée.

Cas : (i) cache comme après le préchargement, liste présente → passe ; (ii) un morceau de poids absent → `GardeArret`, liste présente
ou absente ; (iii) index des poids absent ou illisible → `GardeArret`, liste présente ou absente ; (iv) sans liste de l'arbre → passe
(témoin, cas 5 de la reproduction) ; (v) comportement épinglé de la bibliothèque : sans motifs, liste présente →
`IncompleteSnapshotError` (sous-classe de `LocalEntryNotFoundError`), sans liste → l'instantané, avec les motifs du préchargement →
l'instantané ; (vi) `lecture_v4 controle-avant-ouverture` en mode réel (configuration v8, fichiers réels de P3), processus neuf,
`HF_HUB_OFFLINE=1`, cache par défaut désigné par `HF_HUB_CACHE` (comme l'étape 8) → code 0 ; et la forme scellée de l'appel (sans
motifs), processus neuf, même cache → `IncompleteSnapshotError`.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest
from huggingface_hub import _tree_cache, snapshot_download
from huggingface_hub.errors import IncompleteSnapshotError, LocalEntryNotFoundError
from huggingface_hub.utils import filter_repo_objects

from controle_ia.gardes import GardeArret
from controle_ia.harnais.modeles import MOTIFS_PRECHARGEMENT
from controle_ia.t07 import reextraction_p3_v1 as rx

RACINE_DEPOT = Path(__file__).resolve().parents[1]
MODELE = "meta-llama/Llama-3.1-8B-Instruct"
REV = "0e9e39f249a16976918f6564b8830bc894c89659"             # révision du modèle de P3 (manifeste de P3 ; REV_P3 de l'ordre)
MORCEAUX = tuple(f"model-0000{i}-of-00004.safetensors" for i in range(1, 5))
INDEX = "model.safetensors.index.json"
ARBRE = (("config.json", "generation_config.json", "tokenizer.json", "tokenizer_config.json", "special_tokens_map.json", INDEX)
         + MORCEAUX + ("LICENSE", "README.md", "USE_POLICY.md", ".gitattributes", "original/consolidated.00.pth",
                       "original/params.json", "original/tokenizer.model"))
NON_PRECHARGES = [".gitattributes", "LICENSE", "README.md", "USE_POLICY.md", "original/consolidated.00.pth", "original/params.json",
                  "original/tokenizer.model"]
PRECHARGES = tuple(filter_repo_objects(items=ARBRE, allow_patterns=list(MOTIFS_PRECHARGEMENT)))
ABSENT_LISTE = r"absent du cache local \(IncompleteSnapshotError\)"   # refus venu de la bibliothèque (liste présente)
REELS_P3 = ("runs/20261019-230011-p3-reel/manifeste.json", "diag/20261019-230011-p3-reel/sondes-figees.json",
            "donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz", "donnees/T0.7-faits-repe-v1/facts_true_false.csv",
            "donnees/T0.7-models-under-pressure-v1/training/train.jsonl")
CONFIG_V8 = "docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v8.json"


def _vider_memoire() -> None:
    with _tree_cache._IN_MEMORY_TREE_CACHE_LOCK:
        _tree_cache._IN_MEMORY_TREE_CACHE.clear()


@pytest.fixture(autouse=True)
def _memoire_de_la_bibliotheque_videe():
    _vider_memoire()
    yield
    _vider_memoire()


def _stockage(cache: Path) -> Path:
    return cache / ("models--" + MODELE.replace("/", "--"))


def _chemin_liste(cache: Path) -> str:
    """Chemin de la liste de l'arbre, tel que la bibliothèque le calcule (clé de sa mémoire comprise)."""
    return _tree_cache._tree_cache_path(str(_stockage(cache)), REV)


def _cache_precharge(base: Path, liste: bool = True, sans: tuple = (), index: str | None = None) -> Path:
    """Cache comme après `precharger_modele` : fichiers retenus par les motifs, contenus factices non vides, index bien formé ;
    `liste` : liste de l'arbre (17 noms) écrite par `write_tree_cache`, comme en ligne ; `sans` : fichiers retirés ensuite ;
    `index` : contenu de l'index à la place du bon. Mémoire de la bibliothèque vidée : la liste se lit sur le disque."""
    cache = base.resolve()                                # la bibliothèque résout `cache_dir` : même chemin, même clé de mémoire
    instant = _stockage(cache) / "snapshots" / REV
    instant.mkdir(parents=True)
    carte = {"weight_map": {f"model.layers.{i}": m for i, m in enumerate(MORCEAUX)}}
    for f in PRECHARGES:
        contenu = json.dumps(carte) if f == INDEX else ("{}" if f.endswith(".json") else "x")
        (instant / f).write_text(contenu, encoding="utf-8")
    if index is not None:
        (instant / INDEX).write_text(index, encoding="utf-8")
    for f in sans:
        (instant / f).unlink()
    if liste:
        entrees = {f: _tree_cache.TreeCacheEntry(size=1, blob_id="0" * 40) for f in ARBRE}
        _tree_cache.write_tree_cache(str(_stockage(cache)), REV, entrees)
        assert os.path.isfile(_chemin_liste(cache)), "liste de l'arbre non écrite sur le disque"
    else:
        assert not os.path.exists(_chemin_liste(cache))
    _vider_memoire()
    assert _chemin_liste(cache) not in _tree_cache._IN_MEMORY_TREE_CACHE
    return cache


def test_cache_factice_comme_apres_le_prechargement():
    """Le préchargement retient 10 des 17 fichiers de l'arbre ; les 7 autres (dossier `original/` et textes) restent dehors."""
    assert len(ARBRE) == 17 and len(PRECHARGES) == 10
    assert sorted(set(ARBRE) - set(PRECHARGES)) == NON_PRECHARGES
    assert set(MORCEAUX) | {INDEX, "config.json", "tokenizer.json", "tokenizer_config.json"} <= set(PRECHARGES)


def test_i_liste_presente_cache_comme_apres_le_prechargement_passe(tmp_path):
    """(i) Le cas de l'instance (R-2588) : liste de l'arbre au cache, instantané préchargé entier → la garde passe ; la liste a été
    lue sur le disque pendant l'appel (le contrôle de la bibliothèque a donc joué, avec les motifs)."""
    cache = _cache_precharge(tmp_path / "c")
    r = rx.revision_au_cache(MODELE, REV, str(cache))
    assert r == {"modele": MODELE, "revision": REV, "dossier": str(_stockage(cache) / "snapshots" / REV), "poids": 4}
    assert _chemin_liste(cache) in _tree_cache._IN_MEMORY_TREE_CACHE


@pytest.mark.parametrize("liste", [True, False], ids=["liste-presente", "sans-liste"])
@pytest.mark.parametrize("morceau", MORCEAUX)
def test_ii_un_morceau_de_poids_absent_garde_arret(tmp_path, liste, morceau):
    """(ii) Un morceau de poids absent → `GardeArret` : refus de la bibliothèque (liste présente) ou de la fonction (sans liste)."""
    cache = _cache_precharge(tmp_path / "c", liste=liste, sans=(morceau,))
    motif = ABSENT_LISTE if liste else re.escape(f"incomplet au cache local : ['{morceau}']")
    with pytest.raises(GardeArret, match=motif):
        rx.revision_au_cache(MODELE, REV, str(cache))


@pytest.mark.parametrize("liste", [True, False], ids=["liste-presente", "sans-liste"])
def test_iii_index_des_poids_absent_garde_arret(tmp_path, liste):
    """(iii) Index des poids absent, morceaux présents → `GardeArret`."""
    cache = _cache_precharge(tmp_path / "c", liste=liste, sans=(INDEX,))
    with pytest.raises(GardeArret, match=ABSENT_LISTE if liste else "morceaux sans index"):
        rx.revision_au_cache(MODELE, REV, str(cache))


@pytest.mark.parametrize("liste", [True, False], ids=["liste-presente", "sans-liste"])
@pytest.mark.parametrize("index, motif", [
    ("{pas du json", "JSONDecodeError"),
    (json.dumps({"metadata": {}}), "KeyError"),
    (json.dumps({"weight_map": {}}), "ValueError : weight_map vide"),
], ids=["json-faux", "sans-weight-map", "weight-map-vide"])
def test_iii_index_des_poids_illisible_garde_arret(tmp_path, liste, index, motif):
    """(iii) Index des poids présent mais illisible → `GardeArret` de la fonction, que la liste soit présente (le contrôle de la
    bibliothèque, qui ne regarde que la présence des fichiers, passe) ou absente."""
    cache = _cache_precharge(tmp_path / "c", liste=liste, index=index)
    with pytest.raises(GardeArret, match=r"index des poids illisible \(" + motif):
        rx.revision_au_cache(MODELE, REV, str(cache))


def test_iv_sans_liste_de_l_arbre_passe(tmp_path):
    """(iv) Témoin (cas 5 de la reproduction) : sans liste de l'arbre au cache, la garde passe ; aucune liste n'est lue."""
    cache = _cache_precharge(tmp_path / "c", liste=False)
    r = rx.revision_au_cache(MODELE, REV, str(cache))
    assert r["revision"] == REV and r["poids"] == 4
    assert _chemin_liste(cache) not in _tree_cache._IN_MEMORY_TREE_CACHE and not os.path.exists(_chemin_liste(cache))


def test_v_bibliotheque_sans_motifs_liste_presente_instantane_incomplet(tmp_path):
    """(v) Comportement épinglé de `huggingface_hub` (1.33.0, `requirements-cpu.txt`), cause de l'arrêt : sans motifs, liste de
    l'arbre présente, l'instantané préchargé est déclaré incomplet (les 7 fichiers non préchargés manquent) ; l'erreur dérive de
    `LocalEntryNotFoundError` (le chargeur de `transformers` la rattrape : cas 3 et 4 du diagnostic) ; sans liste, la même lecture
    rend l'instantané (d'où les essais antérieurs verts) ; avec les motifs du préchargement, elle le rend aussi. Si une version de la
    bibliothèque change l'un de ces points, cet essai échoue : le cas sain de la garde est alors à réexaminer."""
    cache = _cache_precharge(tmp_path / "c")
    with pytest.raises(IncompleteSnapshotError, match=r"7 file\(s\) are missing") as e:
        snapshot_download(repo_id=MODELE, revision=REV, local_files_only=True, cache_dir=str(cache))
    assert issubclass(IncompleteSnapshotError, LocalEntryNotFoundError) and isinstance(e.value, LocalEntryNotFoundError)
    _vider_memoire()
    d = snapshot_download(repo_id=MODELE, revision=REV, local_files_only=True, cache_dir=str(cache),
                          allow_patterns=list(MOTIFS_PRECHARGEMENT))
    assert Path(d) == _stockage(cache) / "snapshots" / REV and _chemin_liste(cache) in _tree_cache._IN_MEMORY_TREE_CACHE
    sans = _cache_precharge(tmp_path / "s", liste=False)
    assert Path(snapshot_download(repo_id=MODELE, revision=REV, local_files_only=True, cache_dir=str(sans))).name == REV


def _env_neuf(tmp_path: Path, cache: Path) -> dict:
    """Environnement minimal d'un processus neuf, comme à l'étape 8 du script v4 : hors ligne, cache par défaut désigné par
    `HF_HUB_CACHE`, aucun fichier de bytecode écrit sous `src/` (le script vérifie `src` et `tests` après les essais)."""
    return {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(tmp_path), "HF_HOME": str(tmp_path / "hf-home"),
            "HF_HUB_CACHE": str(cache), "HF_HUB_OFFLINE": "1", "PYTHONPATH": str(RACINE_DEPOT / "src"),
            "PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"}


def test_vi_etape_8_du_script_v4_en_processus_neuf(tmp_path):
    """(vi) Étape 8 du script v4 telle que l'instance la joue (`HF_HUB_OFFLINE=1 … -m controle_ia.t07.lecture_v4
    controle-avant-ouverture . CONFIG`, sans `--cache-dir`), dans un processus neuf, mode réel, configuration v8, fichiers réels de
    P3, cache préchargé avec la liste de l'arbre → code 0, révision de P3 au cache, quatre morceaux. Puis la forme scellée de
    l'appel (sans motifs), processus neuf, même cache → `IncompleteSnapshotError` : la liste lue sur le disque, sans mémoire
    partagée, suffit à l'arrêt corrigé ici."""
    for rel in REELS_P3 + (CONFIG_V8,):
        if not (RACINE_DEPOT / rel).is_file():
            pytest.skip(f"{rel} absent de l'extraction (fichiers réels de P3, configuration v8)")
    cache = _cache_precharge(tmp_path / "hub")
    env = _env_neuf(tmp_path, cache)
    p = subprocess.run([sys.executable, "-B", "-m", "controle_ia.t07.lecture_v4", "controle-avant-ouverture", ".", CONFIG_V8],
                       cwd=RACINE_DEPOT, env=env, capture_output=True, text=True, timeout=900)
    assert p.returncode == 0, p.stderr[-3000:]
    r = json.loads(p.stdout)
    assert r["modele_p3"] == {"modele": MODELE, "revision": REV, "dossier": str(_stockage(cache) / "snapshots" / REV), "poids": 4}
    assert set(r["figees"]) == {"tromperie-difference_moyennes-c15", "enjeux-lineaire-c15"}
    code = ("import sys\nfrom huggingface_hub import snapshot_download\ntry:\n"
            f"    snapshot_download(repo_id={MODELE!r}, revision={REV!r}, local_files_only=True)\n"
            "except Exception as e:\n    print(type(e).__name__)\n    sys.exit(3)\nprint('passe')\n")
    q = subprocess.run([sys.executable, "-B", "-c", code], cwd=tmp_path, env=env, capture_output=True, text=True, timeout=300)
    assert (q.returncode, q.stdout.strip()) == (3, "IncompleteSnapshotError"), (q.stdout, q.stderr[-2000:])
