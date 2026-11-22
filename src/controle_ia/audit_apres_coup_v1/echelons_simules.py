"""L'échelle des échelons simulée (rang 12 de l'ordre d'écriture ; boucle v2, bloc C2), monde planté seul, sous le
jeton de provenance.

Trois échelons, aux étiquettes 3, 10, 30, 100, 300, avec m témoins honnêtes pour négatifs :
- **choisir** dans une réserve scellée de M = 20 détecteurs plantés : prendre celui de plus haute moyenne sur les n
  positifs ; l'espace de la réserve porte la moitié de l'écart (Δ_r = 2), un seul détecteur le voyant ;
- **repondérer** : différence des moyennes dans l'espace des M scores de la réserve ;
- **réapprendre** en dimension complète : différence des moyennes en dimension d (écart complet Δ = 4, d = 4 096).

Les rappels rendus sont les rappels exacts, à 1 % de fausses alertes, de la direction obtenue (loi gaussienne connue,
direction donnée), jamais une relecture des positifs qui l'ont instruite : la relecture en échantillon présentée comme
rappel reçoit le refus nommé ci-dessous (bloc C3 : 1,000 à 4 096 poids et trois étiquettes).

Les positifs sont des étiquettes de la vérité plantée ; aucune sonde du programme n'est touchée, aucun verdict d'un
oracle réel n'entre. [FAIT RAPPORTÉ, sous supposition] : bloc C2 (0,34, 0,14, 0,03 à trois étiquettes ; plafond
0,787 du réapprentissage à m = 400), chiffres repris de la contre-lecture, non relus par le concepteur.
"""
from __future__ import annotations

import math

import numpy as np
from scipy import special, stats

from ..gardes import GardeArret
from .graines import emettre_jeton, empreinte_tableaux, enregistrer_derivation, generateur_auxiliaire
from .harnais_simule import HarnaisSimule

ALPHA = 0.01
Z = float(stats.norm.ppf(1 - ALPHA))
REFUS_RELECTURE_RAPPEL = "relecture en échantillon présentée comme rappel : refus"
ECHELONS = ("choisir", "repondérer", "réapprendre")


def Phi(x):
    return special.ndtr(x)


def _deriver_echelons(entropie: int, cle: tuple[int, ...]) -> bytes:
    """Monde planté : scores de la réserve (positifs n × M, négatifs m × M) et états complets (n × d, m × d)."""
    n, m, d, M, delta_dixiemes, delta_r_dixiemes, rep = cle
    g = generateur_auxiliaire(entropie, 12, *cle)
    Sp = g.standard_normal((n, M))
    Sn = g.standard_normal((m, M))
    Sp[:, 0] += delta_r_dixiemes / 10.0
    Xp = g.standard_normal((n, d))
    Xn = g.standard_normal((m, d))
    Xp[:, 0] += delta_dixiemes / 10.0
    return b"".join(a.tobytes() for a in (Sp, Sn, Xp, Xn))


enregistrer_derivation("echelons_boucle_v1", _deriver_echelons)


def rappels_echelons(entropie: int, n: int, m: int = 400, d: int = 4096, M: int = 20, delta: float = 4.0,
                     delta_r: float = 2.0, rep: int = 0, harnais: HarnaisSimule | None = None) -> dict:
    """Rappels exacts des trois échelons pour une répétition (la réserve, scellée, est fixée par la graine)."""
    harnais = harnais or HarnaisSimule()
    cle = (n, m, d, M, int(round(delta * 10)), int(round(delta_r * 10)), rep)
    contenu, jeton = emettre_jeton(entropie, cle, "echelons_boucle_v1", empreinte_tableaux(cle=np.array(cle)))
    harnais.admettre(contenu, jeton)
    a = np.frombuffer(contenu, dtype=np.float64)
    o = 0
    Sp = a[o:o + n * M].reshape(n, M); o += n * M
    Sn = a[o:o + m * M].reshape(m, M); o += m * M
    Xp = a[o:o + n * d].reshape(n, d); o += n * d
    Xn = a[o:o + m * d].reshape(m, d)
    plafond_reserve = float(Phi(delta_r - Z))
    choix = int(np.argmax(Sp.mean(axis=0)))
    r_choisir = plafond_reserve if choix == 0 else ALPHA
    w = Sp.mean(axis=0) - Sn.mean(axis=0)
    r_repond = float(Phi(delta_r * w[0] / np.linalg.norm(w) - Z))
    W = Xp.mean(axis=0) - Xn.mean(axis=0)
    r_reapp = float(Phi(delta * W[0] / np.linalg.norm(W) - Z))
    return {"n": n, "m": m, "choisir": r_choisir, "bon_choix": choix == 0, "repondérer": r_repond,
            "réapprendre": r_reapp, "nature": "rappel exact de la direction obtenue"}


def plafond_reapprentissage(delta: float, d: int, m: int) -> float:
    """Plafond du réapprentissage quand n grandit, à m témoins : Φ(Δ²/√(Δ² + d/m) − z)."""
    return float(Phi(delta ** 2 / math.sqrt(delta ** 2 + d / m) - Z))


def echelle(entropie: int, etiquettes=(3, 10, 30, 100, 300), R: int = 50, **kw) -> dict:
    """Moyennes et erreurs types des rappels exacts par échelon et par nombre d'étiquettes."""
    out = {}
    for n in etiquettes:
        vals = {e: [] for e in ECHELONS}
        for rep in range(R):
            r = rappels_echelons(entropie, n, rep=rep, **kw)
            for e in ECHELONS:
                vals[e].append(r[e])
        out[n] = {e: (float(np.mean(v)), float(np.std(v, ddof=1) / math.sqrt(R))) for e, v in vals.items()}
    return out


def annoncer_rappel(valeur: float, nature: str) -> float:
    """Seul un rappel exact (ou mesuré sur un pli jamais vu) s'annonce ; une relecture en échantillon est refusée."""
    if nature != "rappel exact de la direction obtenue" and nature != "pli jamais vu":
        raise GardeArret(REFUS_RELECTURE_RAPPEL)
    return valeur


def relecture_en_echantillon(entropie: int, n: int, m: int = 400, d: int = 4096, rep: int = 0) -> tuple[float, str]:
    """L'artefact du bloc C3 : la direction réapprise relit ses propres positifs, dans le monde sans trace (Δ = 0).
    Rend la valeur et sa nature, « relecture en échantillon » ; `annoncer_rappel` la refuse."""
    cle = (n, m, d, 20, 0, 0, rep)
    contenu, jeton = emettre_jeton(entropie, cle, "echelons_boucle_v1", empreinte_tableaux(cle=np.array(cle)))
    HarnaisSimule().admettre(contenu, jeton)
    a = np.frombuffer(contenu, dtype=np.float64)
    o = n * 20 + m * 20
    Xp = a[o:o + n * d].reshape(n, d)
    Xn = a[o + n * d:].reshape(m, d)
    W = Xp.mean(axis=0) - Xn.mean(axis=0)
    return float(np.mean(Xp @ W > Z * np.linalg.norm(W))), "relecture en échantillon"
