"""Outils communs aux essais des briques 2, 3 et 4 de la méta-conception (organisme v6.2.1).

Lecture seule de fournis/ : les fonctions de l'organisme sont extraites du source par l'arbre
syntaxique et exécutées depuis une copie en mémoire, sans import du module (donc sans fichier
compilé écrit dans fournis/). Chaque fichier lu est vérifié par son empreinte SHA-256.
Graines : numpy.random.SeedSequence(entropy=ENTROPIE_RACINE, spawn_key=(tâche, indices...)).
"""
import ast
import hashlib
import json
import math
import re
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

import numpy as np

RACINE = Path(__file__).resolve().parent.parent
FOURNIS = RACINE / "fournis"
SORTIE = RACINE / "sortie"

EMPREINTES_ATTENDUES = {
    "organisme/memoire_isvd.py": "e39295c5d3d04a45ef3024347bf30ee6744aee88fd77ea058e2c8f231f3e1710",
    "organisme/mitose_spectrale.py": "dcba040c45d7936dfb8732bc5aa935052529ce2bf9963dacaa51dbc4f81ae492",
    "rapport-meta-conception.md": "96d12112c8d8d7e376943fa42fc0a4d6faed52b7ed09ae9ecac981c65949c6cf",
    "organisme/principal.py": "98993dd0ef24bae54d9fd0649532559fc739d952ae98796b1f25b753cf5ac026",
}
ENTROPIE_RACINE = 20261026
TACHES = {
    "b2_psd": 1, "b2_trace": 2, "b2_tirages": 3, "b2_degenerescence": 4,
    "b3_seuil": 5, "b3_remedes": 6, "b3_cout": 7, "b4_verbosite": 8, "b4_filtre": 9,
}


# --- Lecture vérifiée de fournis/ et copie des fonctions -------------------------------------

def lire_fourni(relatif: str) -> bytes:
    octets = (FOURNIS / relatif).read_bytes()
    empreinte = hashlib.sha256(octets).hexdigest()
    attendue = EMPREINTES_ATTENDUES[relatif]
    if empreinte != attendue:
        raise RuntimeError(f"empreinte inattendue pour {relatif} : {empreinte} != {attendue}")
    return octets


def copier_fonction(relatif: str, nom: str, source_texte: str = None) -> tuple:
    """Copie exacte d'une fonction de premier niveau ; renvoie (fonction, empreinte du segment)."""
    source = source_texte if source_texte is not None else lire_fourni(relatif).decode("utf-8")
    arbre = ast.parse(source)
    noeuds = [n for n in arbre.body if isinstance(n, ast.FunctionDef) and n.name == nom]
    if len(noeuds) != 1:
        raise RuntimeError(f"fonction {nom} introuvable ou multiple dans {relatif}")
    segment = ast.get_source_segment(source, noeuds[0])
    espace = {"math": math, "re": re, "hashlib": hashlib, "Counter": Counter, "__builtins__": __builtins__}
    code = compile(ast.Module(body=[noeuds[0]], type_ignores=[]), f"copie:{relatif}:{nom}", "exec")
    exec(code, espace)
    return espace[nom], hashlib.sha256(segment.encode("utf-8")).hexdigest()


def copier_fonctions(relatif: str, noms: list, source_texte: str = None) -> tuple:
    """Copie exacte de plusieurs fonctions dans un même espace (pour les appels entre elles)."""
    source = source_texte if source_texte is not None else lire_fourni(relatif).decode("utf-8")
    arbre = ast.parse(source)
    espace = {"math": math, "re": re, "hashlib": hashlib, "Counter": Counter, "__builtins__": __builtins__}
    empreintes = {}
    for nom in noms:
        noeuds = [n for n in arbre.body if isinstance(n, ast.FunctionDef) and n.name == nom]
        if len(noeuds) != 1:
            raise RuntimeError(f"fonction {nom} introuvable ou multiple dans {relatif}")
        segment = ast.get_source_segment(source, noeuds[0])
        empreintes[nom] = hashlib.sha256(segment.encode("utf-8")).hexdigest()
        exec(compile(ast.Module(body=[noeuds[0]], type_ignores=[]), f"copie:{relatif}:{nom}", "exec"), espace)
    return {nom: espace[nom] for nom in noms}, empreintes


def jacobi_organisme():
    return copier_fonction("organisme/memoire_isvd.py", "decomposer_jacobi_symetrique")


def capacite_organisme():
    return copier_fonction("organisme/mitose_spectrale.py", "calculer_capacite_shannon_gram")


def code_caste1_rapport() -> str:
    """Bloc de code Python de la caste 1 dans le rapport (premier bloc ```python)."""
    texte = lire_fourni("rapport-meta-conception.md").decode("utf-8").replace("\r\n", "\n")
    debut = texte.index("```python\n# MODULE: bisociation_dpp.py (v6.3)")
    fin = texte.index("```", debut + 9)
    return texte[debut + len("```python\n"):fin]


# --- Graines ---------------------------------------------------------------------------------

def graine(tache: str, *indices) -> np.random.SeedSequence:
    return np.random.SeedSequence(entropy=ENTROPIE_RACINE, spawn_key=(TACHES[tache],) + tuple(int(i) for i in indices))


def generateur(tache: str, *indices) -> np.random.Generator:
    return np.random.default_rng(graine(tache, *indices))


def description_graines() -> dict:
    return {
        "methode": "numpy.random.SeedSequence(entropy=ENTROPIE_RACINE, spawn_key=(id_tache, indices...))",
        "entropie_racine": ENTROPIE_RACINE,
        "identifiants_taches": TACHES,
        "numpy": np.__version__,
    }


# --- Algèbre ---------------------------------------------------------------------------------

def unitaires(rng, n: int, dim: int = 16) -> np.ndarray:
    x = rng.standard_normal((n, dim))
    return x / np.linalg.norm(x, axis=1, keepdims=True)


def normaliser_lignes(x: np.ndarray) -> np.ndarray:
    return x / np.linalg.norm(x, axis=1, keepdims=True)


def noyau_rapport(d, o, q):
    """Forme exacte du rapport : L_ij = q_i q_j <o_i,o_j>^2 (1 - <d_i,d_j>^2)."""
    c = d @ d.T
    g = o @ o.T
    return np.outer(q, q) * g ** 2 * (1.0 - c ** 2)


def noyau_trace_ferme(d, o, q, dim: int = 16):
    """Forme trace (caste 2) en forme close : q_i q_j <o_i,o_j> (dim - 2 + <d_i,d_j>^2)."""
    c = d @ d.T
    g = o @ o.T
    return np.outer(q, q) * g * (dim - 2.0 + c ** 2)


def noyau_correctif(d, q, gamma: float = 0.0, s_remplace=None):
    """Correctif : L = diag(q) (S + gamma I) diag(q), S_ij = <d_i,d_j>^2."""
    s = (d @ d.T) ** 2 if s_remplace is None else s_remplace
    s = s + gamma * np.eye(s.shape[0])
    return np.outer(q, q) * s


def sinkhorn_knopp(a: np.ndarray, iterations: int = 5):
    """Équilibrage alterné lignes/colonnes ; renvoie (version symétrique D A D, écart à la bistochasticité,
    asymétrie de la version non symétrisée) ou None si une somme devient non positive."""
    n = a.shape[0]
    r = np.ones(n)
    c = np.ones(n)
    for _ in range(iterations):
        ac = a @ c
        if np.any(ac <= 0):
            return None
        r = 1.0 / ac
        atr = a.T @ r
        if np.any(atr <= 0):
            return None
        c = 1.0 / atr
    p = r[:, None] * a * c[None, :]
    ecart = float(max(np.abs(p.sum(1) - 1).max(), np.abs(p.sum(0) - 1).max()))
    asym = float(np.abs(p - p.T).max())
    dsym = np.sqrt(r * c)
    return dsym[:, None] * a * dsym[None, :], ecart, asym


def valeurs_propres_jacobi(jacobi, l: np.ndarray, max_iter: int):
    """Décomposition par la copie de decomposer_jacobi_symetrique (sur une copie de la matrice).
    La fonction de l'organisme renvoie |lambda| triées ; le signe est restitué par le quotient de
    Rayleigh u_k^T L u_k sur la matrice d'origine ; résidu ||L u_k - lambda_k u_k||."""
    n = l.shape[0]
    copie = [[float(l[i, j]) for j in range(n)] for i in range(n)]
    u, sigma = jacobi(copie, dim=n, max_iter=max_iter)
    u = np.array(u)
    lam = np.einsum("ik,ij,jk->k", u, l, u)
    residus = np.linalg.norm(l @ u - u * lam, axis=0)
    return lam, np.array(sigma), residus


def glouton_det(l: np.ndarray, k: int, mode: str = "signe", candidats=None, deja=None):
    """Sélection gloutonne du déterminant maximal ; mode 'signe' (déterminant signé), 'abs' (|det|,
    comme det_sous_matrice de la caste 1). Égalités : premier indice. Renvoie la liste choisie."""
    choisis = list(deja or [])
    pool = list(range(l.shape[0])) if candidats is None else list(candidats)
    while len(choisis) < k:
        meilleur, valeur = None, -np.inf
        for c in pool:
            if c in choisis:
                continue
            idx = choisis + [c]
            v = float(np.linalg.det(l[np.ix_(idx, idx)]))
            if mode == "abs":
                v = abs(v)
            if v > valeur:
                meilleur, valeur = c, v
        if meilleur is None:
            break
        choisis.append(meilleur)
    return choisis


def glouton_cholesky(l: np.ndarray, k: int):
    """Glouton rapide par Cholesky incrémentale (Chen et al. 2018). Renvoie (choisis, échec)."""
    n = l.shape[0]
    cis = np.zeros((k, n))
    di2 = np.diag(l).astype(float).copy()
    j = int(np.argmax(di2))
    choisis = [j]
    for t in range(1, k):
        if di2[j] <= 1e-12:
            return choisis, True
        dj = math.sqrt(di2[j])
        e = (l[j, :] - cis[:t - 1, j] @ cis[:t - 1, :]) / dj
        cis[t - 1, :] = e
        di2 = di2 - e ** 2
        di2[choisis] = -np.inf
        j = int(np.argmax(di2))
        choisis.append(j)
    return choisis, False


def sous_ensembles(n: int, k: int) -> np.ndarray:
    return np.array(list(combinations(range(n), k)), dtype=int)


def dets_sous_ensembles(l: np.ndarray, se: np.ndarray) -> np.ndarray:
    blocs = l[se[:, :, None], se[:, None, :]]
    return np.linalg.det(blocs)


def ecrire_json(chemin: Path, contenu: dict) -> None:
    chemin.write_text(json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=False) + "\n", encoding="utf-8")


def versions() -> dict:
    import scipy
    return {"python": sys.version.split()[0], "numpy": np.__version__, "scipy": scipy.__version__}
