"""Apprentissage des sondes de l'étape B bis sur la carte (`prereg/T0.7-etape-B-bis-v1.md`, plan, point 5), v1.

Même calcul que `sondes.familles._entrainer` pour les deux familles de la grille (« linéaire » agrégée par le maximum ;
« attention »), sans le modifier : apprentissage par sacs (jetons de toutes les actions mis bout à bout, indice de l'action de
chaque jeton), entrées centrées-réduites par jeton sur l'apprentissage (moyenne, écart type ddof 0, écart ≤ 10⁻¹² remplacé par
1), score par jeton w·x + b, agrégation par le **maximum** (`scatter_reduce` « amax ») ou par l'**attention** (logits q·x,
poids softmax par action), perte logistique moyenne (`BCEWithLogitsLoss`) + l2·‖w‖², Adam (pas 0,05), 300 époques, départ
w = 0, b = 0, q ~ 0,01·N(0, I) tiré par le générateur de processeur de torch juste après `torch.manual_seed(graine)` (comme
`familles`, puis porté sur l'appareil) ; normalisation repliée dans la sonde rendue (`SondeLineaireJetons` du paquet gelé, que
`harnais.sondes.score_action` applique telle quelle). **Jamais la moyenne ni la médiane sur les jetons** (N-026).

Différences déclarées avec `familles` : tenseurs en double précision sur l'appareil (« cuda » en marche, « cpu » dans les
essais) ; moyenne et écart type calculés par torch sur l'appareil (et non par numpy) ; sur la carte, algorithmes déterministes
exigés (`torch.are_deterministic_algorithms_enabled()`, réglés par `harnais.modeles.regler_determinisme`), sinon arrêt.
`LotCarte` garde les jetons réduits d'un ensemble d'apprentissage à une couche, pour les six réglages (famille × régularisation)
qui le partagent.

**Contrôle carte-processeur** (`controle_carte_processeur`, garde de la marche) : un (cellule, pli) tiré par graine est réappris
sur le processeur par `sondes.familles.entrainer` ; écart relatif maximal des scores sur 256 actions tirées
max |a − b| / max(|b|, 1) (interprétation déclarée de « écart relatif », plancher 1 au dénominateur) ≤ 10⁻⁴, sinon arrêt
(erreur de chaîne).
"""
from __future__ import annotations

import numpy as np
import torch

from ..gardes import GardeArret
from ..harnais.sondes import score_action
from ..sondes import familles as fam
from .commun_v1 import AGREGATION_DE, EPOQUES, FAMILLES, PAS, TOLERANCE_CARTE, exiger_agregation


class SondeEnEchec(GardeArret):
    """Perte non finie à l'apprentissage : la sonde est « non calculable » (aucun score), motif écrit."""


def _exiger_deterministe(appareil: str) -> None:
    if str(appareil).startswith("cuda") and not torch.are_deterministic_algorithms_enabled():
        raise GardeArret("apprentissage sur la carte sans algorithmes déterministes (regler_determinisme non appelé) : arrêt")


class LotCarte:
    """Jetons réduits d'un ensemble d'apprentissage (une couche), indice de l'action de chaque jeton, sur l'appareil."""

    def __init__(self, sequences, appareil: str = "cpu"):
        self.d = fam._verifier_donnees(sequences)
        _exiger_deterministe(appareil)
        self.appareil = torch.device(appareil)
        longueurs = [int(np.asarray(s).shape[0]) for s in sequences]
        X = torch.empty((sum(longueurs), self.d), dtype=torch.float64, device=self.appareil)
        a = 0
        for s, n in zip(sequences, longueurs):
            X[a:a + n] = torch.as_tensor(np.asarray(s, dtype=np.float64), device=self.appareil)
            a += n
        mu = X.mean(dim=0)
        s = X.std(dim=0, correction=0)
        s = torch.where(s > 1e-12, s, torch.ones_like(s))
        X.sub_(mu).div_(s)
        self.X, self.n = X, len(longueurs)
        self.idx = torch.repeat_interleave(torch.arange(self.n, device=self.appareil),
                                           torch.as_tensor(longueurs, device=self.appareil))
        self.mu, self.s = mu.to("cpu").numpy(), s.to("cpu").numpy()
        self.longueurs = longueurs


def _agreger(sj, lj, idx, n, agregation):
    """`familles._agreger`, tenseurs créés sur l'appareil des scores."""
    dev, dt = sj.device, sj.dtype
    if agregation == "max":
        return torch.full((n,), -torch.inf, dtype=dt, device=dev).scatter_reduce(0, idx, sj, reduce="amax", include_self=True)
    m = torch.full((n,), -torch.inf, dtype=dt, device=dev).scatter_reduce(0, idx, lj, reduce="amax", include_self=True)
    e = torch.exp(lj - m[idx])
    z = torch.zeros(n, dtype=dt, device=dev).index_add(0, idx, e)
    return torch.zeros(n, dtype=dt, device=dev).index_add(0, idx, e * sj) / z


def entrainer(lot: LotCarte, famille: str, nom: str, couche: int, y, l2: float, graine: int, epoques: int = EPOQUES,
              pas: float = PAS) -> fam.SondeLineaireJetons:
    """Une sonde de la grille (famille « lineaire » ou « attention »), sur les jetons du lot."""
    if famille not in FAMILLES:
        raise GardeArret(f"famille {famille!r} hors de la grille {FAMILLES}")
    agregation = exiger_agregation(AGREGATION_DE[famille], f"sonde {nom}")
    y = np.asarray(y)
    if y.shape != (lot.n,) or not set(np.unique(y).tolist()) <= {0, 1} or len(set(y.tolist())) < 2:
        raise GardeArret("étiquettes 0/1 des deux classes attendues, une par action du lot")
    dev, d = lot.appareil, lot.d
    torch.manual_seed(int(graine))
    q0 = torch.randn(d, dtype=torch.float64) * 0.01 if agregation == "attention" else None
    w = torch.nn.Parameter(torch.zeros(d, dtype=torch.float64, device=dev))
    b = torch.nn.Parameter(torch.zeros((), dtype=torch.float64, device=dev))
    parametres = [w, b]
    q = None
    if q0 is not None:
        q = torch.nn.Parameter(q0.to(dev))
        parametres.append(q)
    opt = torch.optim.Adam(parametres, lr=float(pas))
    bce = torch.nn.BCEWithLogitsLoss()
    cible = torch.as_tensor(y.astype(np.float64), device=dev)
    perte = None
    for e in range(int(epoques)):
        opt.zero_grad()
        sj = lot.X @ w + b
        lj = lot.X @ q if q is not None else None
        sa = _agreger(sj, lj, lot.idx, lot.n, agregation)
        perte = bce(sa, cible) + float(l2) * (w ** 2).sum()
        if e in (0, int(epoques) - 1) and not bool(torch.isfinite(perte)):
            raise SondeEnEchec(f"sonde {nom} : perte non finie à l'époque {e}")
        perte.backward()
        opt.step()
    wn = w.detach().to("cpu").numpy()
    qn = q.detach().to("cpu").numpy() if q is not None else None
    w_brut = wn / lot.s
    sonde = fam.SondeLineaireJetons(nom, int(couche), agregation, w_brut, float(b.detach().to("cpu")) - float(lot.mu @ w_brut),
                                    (qn / lot.s) if qn is not None else None, famille)
    if not (np.all(np.isfinite(sonde.w)) and np.isfinite(sonde.b) and (qn is None or np.all(np.isfinite(sonde.q)))):
        raise SondeEnEchec(f"sonde {nom} : paramètres non finis")
    return sonde


def scores(sonde, sequences) -> np.ndarray:
    """Score de chaque action par la boucle du harnais (maximum ou attention ; jamais la moyenne ni la médiane)."""
    exiger_agregation(sonde.agregation, f"sonde {sonde.nom}")
    return np.array([score_action(sonde, np.asarray(s), 0, len(s)) for s in sequences], dtype=np.float64)


def ecart_relatif(a, b) -> float:
    a, b = np.asarray(a, dtype=np.float64), np.asarray(b, dtype=np.float64)
    return float(np.max(np.abs(a - b) / np.maximum(np.abs(b), 1.0)))


def controle_carte_processeur(sonde_carte, sequences_app, y_app, reglage: dict, graine: int, sequences_controle,
                              tolerance: float = TOLERANCE_CARTE, epoques: int = EPOQUES) -> dict:
    """La même sonde réapprise sur le processeur par `sondes.familles.entrainer` (paquet gelé) ; écart relatif maximal des
    scores sur les actions de contrôle ≤ `tolerance`, sinon arrêt (erreur de chaîne)."""
    ref = fam.entrainer(reglage["famille"], sonde_carte.nom, int(reglage["couche"]), list(sequences_app), np.asarray(y_app),
                        AGREGATION_DE[reglage["famille"]], int(graine),
                        fam.Reglages(l2=float(reglage["l2"]), epoques=int(epoques), pas=PAS))
    e = ecart_relatif(scores(sonde_carte, sequences_controle), scores(ref, sequences_controle))
    if not e <= float(tolerance):
        raise GardeArret(f"contrôle carte-processeur : écart relatif {e:.3e} > {tolerance:g} : arrêt (erreur de chaîne)")
    return {"ecart_relatif_max": e, "actions": len(list(sequences_controle)), "tolerance": float(tolerance),
            "reglage": reglage["nom"]}


__all__ = ["LotCarte", "entrainer", "scores", "ecart_relatif", "controle_carte_processeur", "SondeEnEchec"]
