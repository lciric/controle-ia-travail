"""Étage M0 : la mémoire de l'essaim — sous-espace incrémental (« Koopman ISVD ») et base de connaissances.

Ce que décrivait Gemini : « auto-programmation en Python via `ast.parse` d'un opérateur de SVD incrémentale sur
dictionnaire non linéaire de Koopman, avec diagonalisation de Jacobi symétrique (r_max = 6) », et un fichier
`endogenous_memory_plugin_invented_by_swarm.py` absent de toutes les branches.

Ce qui est gardé : une décomposition en valeurs singulières incrémentale de rang borné sur les plongements des
découvertes, mise à jour par la diagonalisation de Jacobi d'une petite matrice symétrique ; un relèvement quadratique
optionnel ([v ; v²], nom « Koopman » gardé, sans autre prétention). La nouveauté d'un énoncé est son résidu hors du
sous-espace mémorisé : c'est elle qui dit « déjà couvert », pas le modèle (B-17, B-18).

Ce qui est retiré : l'auto-programmation (B-14) — aucun code écrit par un modèle n'est exécuté, jamais. L'opérateur
est fixe ; l'essaim ne décide que de ses paramètres (rang, seuil, relèvement) via le génome.

La base de connaissances garde chaque découverte avec sa provenance et son statut (`verifie-code`,
`verifie-verificateur`, `non-verifie`), et un compteur d'utilité alimenté par le juge externe ; elle est écrite en
versions numérotées, jamais écrasée (R12).
"""
from __future__ import annotations

import datetime as _dt
import json
import pathlib

import numpy as np

from .plongement import Plongeur

STATUTS = ("verifie-code", "verifie-verificateur", "non-verifie")


def jacobi_symetrique(a: np.ndarray, tol: float = 1e-12, max_balayages: int = 100) -> tuple[np.ndarray, np.ndarray]:
    """Valeurs et vecteurs propres d'une matrice symétrique réelle par rotations de Jacobi cycliques."""
    a = np.array(a, dtype=np.float64, copy=True)
    n = a.shape[0]
    v = np.eye(n)
    for _ in range(max_balayages):
        hors = np.sqrt(np.sum(np.tril(a, -1) ** 2))
        if hors < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(a[p, q]) < 1e-300:
                    continue
                theta = (a[q, q] - a[p, p]) / (2.0 * a[p, q])
                t = np.sign(theta) / (abs(theta) + np.sqrt(theta * theta + 1.0)) if theta != 0 else 1.0
                c = 1.0 / np.sqrt(t * t + 1.0)
                s = t * c
                j = np.eye(n)
                j[p, p] = c; j[q, q] = c; j[p, q] = s; j[q, p] = -s
                a = j.T @ a @ j
                v = v @ j
    valeurs = np.diag(a).copy()
    ordre = np.argsort(valeurs)[::-1]
    return valeurs[ordre], v[:, ordre]


class MemoireISVD:
    """Sous-espace de rang ≤ r_max engendré par les plongements ingérés, mis à jour incrémentalement."""

    def __init__(self, dim: int, r_max: int = 6, relevement_quadratique: bool = False):
        self.dim = int(dim)
        self.r_max = int(r_max)
        self.relevement = bool(relevement_quadratique)
        d = 2 * self.dim if self.relevement else self.dim
        self.u = np.zeros((d, 0))
        self.s = np.zeros(0)
        self.n_ingeres = 0

    def _relever(self, v: np.ndarray) -> np.ndarray:
        if not self.relevement:
            return v
        w = np.concatenate([v, v * v])
        n = np.linalg.norm(w)
        return w / n if n > 0 else w

    def nouveaute(self, v: np.ndarray) -> float:
        w = self._relever(v)
        if self.u.shape[1] == 0:
            return float(np.linalg.norm(w))
        return float(np.linalg.norm(w - self.u @ (self.u.T @ w)))

    def ajouter(self, v: np.ndarray) -> float:
        w = self._relever(v)
        self.n_ingeres += 1
        if self.u.shape[1] == 0:
            n = float(np.linalg.norm(w))
            if n > 0:
                self.u = (w / n).reshape(-1, 1)
                self.s = np.array([n])
            return n
        p = self.u.T @ w
        r = w - self.u @ p
        rho = float(np.linalg.norm(r))
        k = self.u.shape[1]
        if rho > 1e-10:
            base = np.hstack([self.u, (r / rho).reshape(-1, 1)])
            petite = np.zeros((k + 1, k + 1))
            petite[:k, :k] = np.diag(self.s)
            petite[:k, k] = p
            petite[k, k] = rho
        else:
            # le vecteur est déjà dans le sous-espace : la base ne grandit pas, seuls les poids bougent
            base = self.u
            petite = np.hstack([np.diag(self.s), p.reshape(-1, 1)])  # k × (k+1)
        # valeurs singulières de `petite` par Jacobi sur petite·petiteᵀ (symétrique)
        valeurs, vecteurs = jacobi_symetrique(petite @ petite.T)
        valeurs = np.clip(valeurs, 0.0, None)
        garde = min(self.r_max, int(np.sum(valeurs > 1e-14)))
        self.u = base @ vecteurs[:, :garde]
        self.s = np.sqrt(valeurs[:garde])
        return rho

    def etat(self) -> dict:
        return {"rang": int(self.u.shape[1]), "valeurs_singulieres": [round(float(x), 6) for x in self.s],
                "n_ingeres": self.n_ingeres, "r_max": self.r_max, "relevement_quadratique": self.relevement}


class BaseConnaissances:
    """Découvertes de l'essaim, avec provenance, statut de vérification et utilité mesurée par le juge externe."""

    def __init__(self, dim: int = 2048, r_max: int = 6, relevement_quadratique: bool = False):
        self.entrees: list[dict] = []
        self.plongeur = Plongeur(dim)
        self.memoire = MemoireISVD(dim, r_max, relevement_quadratique)
        self.version = 0

    # ---- lecture ----
    def enonces(self, statuts: tuple[str, ...] = ("verifie-code", "verifie-verificateur")) -> list[str]:
        return [e["enonce"] for e in self.entrees if e["statut"] in statuts]

    def deja_couvert(self, texte: str, seuil: float = 0.35) -> bool:
        if not self.entrees:
            return False
        return self.memoire.nouveaute(self.plongeur.vecteur(texte)) < seuil

    # ---- écriture ----
    def ingerer(self, enonce: str, statut: str, provenance: dict, generation: int) -> dict:
        if statut not in STATUTS:
            raise ValueError(f"statut inconnu : {statut}")
        entree = {"id": f"C-{len(self.entrees) + 1:04d}", "enonce": str(enonce).strip(), "statut": statut,
                  "provenance": dict(provenance), "generation": int(generation), "utilite": 0.0, "usages": 0,
                  "quand_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
        self.entrees.append(entree)
        self.reconstruire()
        return entree

    def crediter(self, ids: list[str], gain: float):
        for e in self.entrees:
            if e["id"] in ids:
                e["usages"] += 1
                e["utilite"] += float(gain)

    def reconstruire(self):
        """Réajuste le plongeur sur les énoncés et reconstruit le sous-espace (les vecteurs changent avec l'idf)."""
        textes = [e["enonce"] for e in self.entrees]
        self.plongeur.ajuster(textes)
        self.memoire = MemoireISVD(self.plongeur.dim, self.memoire.r_max, self.memoire.relevement)
        for t in textes:
            self.memoire.ajouter(self.plongeur.vecteur(t))

    # ---- persistance versionnée ----
    def sauver(self, dossier: str | pathlib.Path) -> pathlib.Path:
        dossier = pathlib.Path(dossier)
        dossier.mkdir(parents=True, exist_ok=True)
        self.version += 1
        chemin = dossier / f"connaissances-v{self.version:04d}.json"
        while chemin.exists():
            self.version += 1
            chemin = dossier / f"connaissances-v{self.version:04d}.json"
        chemin.write_text(json.dumps({"version": self.version, "entrees": self.entrees, "memoire": self.memoire.etat(),
                                      "r_max": self.memoire.r_max, "relevement_quadratique": self.memoire.relevement},
                                     indent=1, ensure_ascii=False), encoding="utf-8")
        return chemin

    @classmethod
    def charger(cls, chemin: str | pathlib.Path, dim: int = 2048) -> "BaseConnaissances":
        d = json.loads(pathlib.Path(chemin).read_text(encoding="utf-8"))
        base = cls(dim, int(d.get("r_max", 6)), bool(d.get("relevement_quadratique", False)))
        base.entrees = list(d["entrees"])
        base.version = int(d.get("version", 0))
        base.reconstruire()
        return base
