"""Plongement lexical des sondes : ce que Gemini appelait « plongement de concepts mathématiques ».

Ce que c'est vraiment : un vecteur de fréquences pondérées (tf-idf) de jetons mathématiques et lexicaux, projeté
par hachage signé dans une dimension fixe. C'est une heuristique de diversité, pas une mesure de concepts (B-09).

Corrections :
- B-09 : le hachage `md5` modulo 1024 sur des jetons LaTeX seuls est remplacé par un hachage sha256 signé, sur les
  jetons LaTeX, les identifiants indicés, les opérateurs et les mots ; la pondération tf-idf est calculée sur le
  corpus des sondes seulement (jamais sur les consignes : constat 27 de l'essaim d'inspection, fuite transductive) ;
- B-20 : les textes sont normalisés en UTF-8 ; un caractère de remplacement (U+FFFD) ou un « ? » à la place d'un
  accent dans une consigne est détecté par `texte_corrompu` et refusé en amont (constat 16).
"""
from __future__ import annotations

import hashlib
import math
import re
import unicodedata

import numpy as np

DIM_DEFAUT = 2048
MOTIF_LATEX = re.compile(r"\\[a-zA-Z]+")
MOTIF_INDICE = re.compile(r"\b[A-Za-z]{1,8}(?:_\{[^}]{1,24}\}|_[A-Za-z0-9]{1,8}|\^\{[^}]{1,24}\}|\^[A-Za-z0-9]{1,4})")
MOTIF_OPERATEUR = re.compile(r"(?:<=|>=|!=|==|->|\|\||\\subseteq|\\supseteq|\\in\b|\\perp|\\otimes|\\oplus|\\circ|\\mapsto)")
MOTIF_MOT = re.compile(r"[a-zà-ÿ][a-zà-ÿ'-]{2,}")
MOTIF_CORRUPTION = re.compile(r"�|(?<=[a-z])\?(?=[a-z])")

MOTS_VIDES = frozenset("""les des une est pour par sur dans avec que qui pas sont ses aux cette ces leur leurs
the and for with that this from are our not into than then which""".split())


def normaliser(texte: str) -> str:
    return unicodedata.normalize("NFC", str(texte or ""))


def texte_corrompu(texte: str) -> bool:
    """Vrai si le texte porte des traces d'un encodage cassé (U+FFFD, ou `?` entre deux lettres : « m?thode »)."""
    return bool(MOTIF_CORRUPTION.search(normaliser(texte)))


def jetons(texte: str) -> list[str]:
    t = normaliser(texte)
    sortie = [j.lower() for j in MOTIF_LATEX.findall(t)]
    sortie += [j.lower() for j in MOTIF_INDICE.findall(t)]
    sortie += [j.lower() for j in MOTIF_OPERATEUR.findall(t)]
    sortie += [m for m in MOTIF_MOT.findall(t.lower()) if m not in MOTS_VIDES]
    return sortie


def _coordonnee(jeton: str, dim: int) -> tuple[int, float]:
    h = hashlib.sha256(jeton.encode("utf-8")).digest()
    indice = int.from_bytes(h[:4], "big") % dim
    signe = 1.0 if h[4] % 2 == 0 else -1.0
    return indice, signe


class Plongeur:
    """Ajusté sur un corpus de sondes (idf), puis appliqué à tout texte."""

    def __init__(self, dim: int = DIM_DEFAUT):
        self.dim = int(dim)
        self.idf: dict[str, float] = {}
        self.n_documents = 0

    def ajuster(self, corpus: list[str]) -> "Plongeur":
        docs = [set(jetons(t)) for t in corpus]
        self.n_documents = len(docs)
        freq: dict[str, int] = {}
        for d in docs:
            for j in d:
                freq[j] = freq.get(j, 0) + 1
        n = max(1, self.n_documents)
        self.idf = {j: math.log((1 + n) / (1 + f)) + 1.0 for j, f in freq.items()}
        return self

    def vecteur(self, texte: str) -> np.ndarray:
        v = np.zeros(self.dim, dtype=np.float64)
        js = jetons(texte)
        if not js:
            return v
        comptes: dict[str, int] = {}
        for j in js:
            comptes[j] = comptes.get(j, 0) + 1
        for j, c in comptes.items():
            idx, signe = _coordonnee(j, self.dim)
            v[idx] += signe * (1.0 + math.log(c)) * self.idf.get(j, 1.0 + math.log(1 + max(1, self.n_documents)))
        norme = float(np.linalg.norm(v))
        return v / norme if norme > 0 else v

    def matrice(self, textes: list[str]) -> np.ndarray:
        if not textes:
            return np.zeros((0, self.dim))
        return np.stack([self.vecteur(t) for t in textes], axis=0)


def similarite(v1: np.ndarray, v2: np.ndarray) -> float:
    n1, n2 = float(np.linalg.norm(v1)), float(np.linalg.norm(v2))
    if n1 == 0 or n2 == 0:
        return 0.0
    return float(np.dot(v1, v2) / (n1 * n2))
