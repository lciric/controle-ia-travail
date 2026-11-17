"""Aide des essais du second addendum de B bis : jeux **fabriqués** (aucune donnée de 7a ni de 7b, aucune activation), processeur
seulement. Deux générateurs repris des pièces du diagnostic, à graines fixes écrites ici :
- `jeu_residuel` : celui de `diagnostic-carte-processeur-v1/essai-amplification-lineaire-v1.py` (`2e063fcc…`, fonction `jeu`,
  forme « résiduelle » : moyenne forte, spectre décroissant, jetons voisins corrélés, quelques valeurs massives ; option
  « gabarits » : part des jetons remplacés par des quasi-copies de cinq jetons communs ; « répétition » : bruit N(0, I)
  indépendant en simple précision), demi-précision ;
- `jeu_anisotrope` : celui de la contre-lecture (`contre-lecture-essai-independant-v1.py`, `0b687970…`, `kind="aniso"` : rang 8,
  sans quasi-copie), demi-précision.
« Carte émulée » (`carte_emulee`) : le code de la carte (`apprentissage_carte_v1.entrainer`) joué sur un `LotCarte` des **mêmes
actions dans un autre ordre** (permutation tirée, étiquettes de même) : même problème, même départ, seul l'ordre des sommes change."""
from __future__ import annotations

import numpy as np

ENTROPIE = 0x5ECD_ADD2_2026_1116_B815_0004


def _rng(cle: int) -> np.random.Generator:
    return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(int(cle),)))


def jeu_residuel(nom: str, n_app: int, n_ctrl: int, d: int, lmin: int, lmax: int, decalage: float, rho: float, massif: float,
                 cle: int, gabarits: float = 0.0, bruit: float = 0.3, puissance: float = 0.8, bruit_gabarit: float = 1e-3):
    """(séquences d'apprentissage, y, séquences de contrôle, y de contrôle) ; deux classes égales (générateur du diagnostic)."""
    rng = _rng(cle)
    u = rng.standard_normal(d)
    u /= np.linalg.norm(u)
    k = min(d, 64)
    spectre = 1.0 / np.arange(1, k + 1) ** float(puissance)
    A = rng.standard_normal((d, k)) * np.sqrt(spectre)[None, :] * 3.0
    m0 = rng.standard_normal(d) * 2.0
    massives = rng.choice(d, size=4, replace=False)
    modeles = m0[None, :] + rng.standard_normal((5, k)) @ A.T + bruit * rng.standard_normal((5, d))

    def action(pos: bool):
        n = int(rng.integers(lmin, lmax + 1))
        if nom == "repetition":
            x = rng.standard_normal((n, d))
            if pos:
                x[: max(1, n // 4)] += 0.5 * u
            return x.astype(np.float32)
        c = rng.standard_normal(k)
        z = np.empty((n, k))
        z[0] = rng.standard_normal(k)
        e = rng.standard_normal((n, k))
        for i in range(1, n):
            z[i] = rho * z[i - 1] + np.sqrt(1.0 - rho ** 2) * e[i]
        x = m0[None, :] + (c[None, :] + z) @ A.T + bruit * rng.standard_normal((n, d))
        if gabarits > 0:
            t = np.flatnonzero(rng.random(n) < gabarits)
            x[t] = modeles[rng.integers(0, 5, size=len(t))] + bruit_gabarit * rng.standard_normal((len(t), d))
        if massif > 0:
            x[0, massives] = massif * (1.0 + 0.05 * rng.standard_normal(len(massives)))
            t = rng.random(n) < 0.01
            x[np.ix_(t, massives)] = 0.3 * massif
        if pos and decalage:
            w = max(1, n // 4)
            a = int(rng.integers(0, n - w + 1))
            x[a:a + w] += decalage * np.sqrt(d) / 8.0 * u
        return x.astype(np.float16).astype(np.float32)

    y = np.r_[np.ones(n_app // 2, int), np.zeros(n_app - n_app // 2, int)]
    app = [action(bool(t)) for t in y]
    yc = np.array([1 if i % 2 == 0 else 0 for i in range(n_ctrl)])
    ctrl = [action(bool(t)) for t in yc]
    return app, y, ctrl, yc


def jeu_anisotrope(cle: int, n: int = 480, nc: int = 192, d: int = 768, lo: int = 30, hi: int = 90, signal: float = 0.3):
    """Régime anisotrope de bas rang (rang 8), sans quasi-copie (générateur de la contre-lecture, `kind="aniso"`)."""
    rng = _rng(cle)
    rng.standard_normal((6, d))                                # gabarits du générateur d'origine, non employés (même suite)
    mu = rng.standard_normal(d) * 3.0
    L = rng.standard_normal((d, 8))
    dirsig = rng.standard_normal(d)
    dirsig /= np.linalg.norm(dirsig)

    def action(y):
        m = int(rng.integers(lo, hi + 1))
        x = rng.standard_normal((m, d))
        x = 0.3 * x + (rng.standard_normal((m, 8)) * 3.0) @ L.T / np.sqrt(8)
        x = x + mu
        if y:
            j = int(rng.integers(0, m))
            x[j] = x[j] + signal * 10 * dirsig
        return x.astype(np.float16).astype(np.float64)

    ya = np.array([i % 2 for i in range(n)])
    yc = np.array([i % 2 for i in range(nc)])
    return [action(y) for y in ya], ya, [action(y) for y in yc], yc


def carte_emulee(ac, app, origine, cle: int = 7):
    """`entrainer` de la carte émulée : le lot reçu est remplacé par celui des mêmes actions permutées (une fois, gardé)."""
    from controle_ia.gardes import GardeArret
    perm = _rng(1000 + int(cle)).permutation(len(app))
    lp = ac.LotCarte([app[i] for i in perm], "cpu")

    def entrainer(lot, famille, nom, couche, y, l2, graine, epoques=300, pas=0.05):
        if lot.n != len(app):
            raise GardeArret("carte émulée : lot inattendu")
        return origine(lp, famille, nom, couche, np.asarray(y)[perm], l2, graine, epoques=epoques, pas=pas)
    return entrainer
