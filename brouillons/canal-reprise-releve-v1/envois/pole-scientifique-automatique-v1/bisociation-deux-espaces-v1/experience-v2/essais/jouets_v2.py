"""Mondes jouets construits à la main (réponse connue) et graines d'essai, pour les essais R5 et unitaires.

Graines d'essai : RACINE_VALIDATION avec des indices ≥ 950 000 (≥ 900 000 avant les corrections v2), hors de toute plage
du § 7 (validation 0 à 499) ; RACINE n'est jamais employée par les essais.
"""
import sys
from collections import Counter
from pathlib import Path
from types import MappingProxyType

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent))
sys.path.insert(0, str(ICI.parents[6] / "src"))

import numpy as np  # noqa: E402

import monde_v2 as mo  # noqa: E402

INDICE_ESSAI = 950_000


def monde_jouet(dom_obs, etiq, cos=None, vrais=(), c_obs=None, q=None, champ=None):
    n = len(dom_obs)
    etiq = [frozenset(e) for e in etiq]
    df = Counter()
    for e in etiq:
        df.update(e)
    c_obs = tuple(tuple(c) for c in (c_obs or [("0", "0", "0", "0")] * n))
    cos = np.eye(n) if cos is None else np.asarray(cos, dtype=float)
    paires, valides, pont = mo.etage_commun(n, etiq, c_obs, tuple(dom_obs), df)
    obs = mo.Obs(n=n, cos=mo._figer(cos), etiq_op=tuple(frozenset(l for l in e if l.startswith("op:")) for e in etiq),
                 etiq_co=tuple(frozenset(l for l in e if l.startswith("co:")) for e in etiq), c_obs=c_obs,
                 dom_obs=tuple(dom_obs), q=tuple(q or [1.0] * n), df=MappingProxyType(dict(df)), paires=paires,
                 valides=valides, pont=pont)
    champ = list(champ or range(max(dom_obs) + 1))
    idx = {p: x for x, p in enumerate(paires)}
    vr = {idx[(min(i, j), max(i, j))] for i, j in vrais}
    info = [{"eloigne": champ[dom_obs[i]] != champ[dom_obs[j]], "proche": False, "compat_vraie": True,
             "op_commun": [], "rare_commun": []} for i, j in paires]
    arts = [{"dom": dom_obs[i], "etiq_op": {}, "etiq_co": {}} for i in range(n)]
    latent = mo.Latent(condition="M_bien", vrais=vr, placebo=set(), plante={}, info_paires=info, arts=arts,
                       champ=champ, n_champs=len(set(champ)), tentatives=0, replantations=0, nr=False,
                       groupe=list(champ), plantes=[], rares={})
    return mo.Monde(obs, latent)
