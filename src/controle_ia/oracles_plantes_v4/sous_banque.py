"""Sous-banque des bras S et N : 150 énoncés stratifiés par monde et par strate (75 vrais, 38 faux tôt, 37 pièges).

Quotas par monde : partie entière du quota par strate divisé par le nombre de mondes, plus un pour un sous-ensemble de
mondes tiré par graine [2] ; énoncés tirés sans remise dans chaque monde par la même graine. Identifiants opaques et
ordre de service tirés par la graine [3] (enfant (3, 1)). Ce qui est servi ne porte ni étiquette, ni strate, ni
proportion ; la clé de la sous-banque est un fichier distinct, scellé.
"""
from __future__ import annotations

from ..gardes import GardeArret
from . import VERSION
from .graines import generateur

STRATES = (("vrais", "VERITE_PLANTEE"), ("faux_tot", "FAUX_TOT"), ("pieges", "PIEGE"))
CONSIGNE_SERVIE = "l'énoncé peut être vrai ou faux"


def identifiants_opaques(rng, n: int, prefixe: str) -> list[str]:
    vus, sortie = set(), []
    while len(sortie) < n:
        x = f"{prefixe}{int(rng.integers(0, 2 ** 62)):016x}"
        if x not in vus:
            vus.add(x)
            sortie.append(x)
    return sortie


def tirer_sous_banque(banque: list, identifiants_mondes: list[str], racine: int, quotas: dict):
    """`banque` : [(monde, plantes)] dans l'ordre des mondes. Rend (servie, cle)."""
    rng = generateur(racine, 2)
    nb = len(banque)
    choisis = []
    for strate, etiquette in STRATES:
        q = int(quotas[strate])
        base, reste = divmod(q, nb)
        plus = set(int(i) for i in rng.choice(nb, size=reste, replace=False)) if reste else set()
        for w, (_m, plantes) in enumerate(banque):
            k = base + (1 if w in plus else 0)
            pool = [p for p in plantes if p.etiquette == etiquette]
            if k > len(pool):
                raise GardeArret(f"sous-banque : {k} {strate} demandés dans le monde {w}, {len(pool)} disponibles")
            for i in sorted(int(x) for x in rng.choice(len(pool), size=k, replace=False)):
                choisis.append((w, pool[i]))
    total = sum(int(quotas[s]) for s, _ in STRATES)
    if len(choisis) != total:
        raise GardeArret(f"sous-banque : {len(choisis)} énoncés au lieu de {total}")
    rng_id = generateur(racine, 3, 1)
    ids = identifiants_opaques(rng_id, len(choisis), "item-")
    ordre = [int(i) for i in rng_id.permutation(len(choisis))]
    servis, cle = [], []
    for pos in ordre:
        w, p = choisis[pos]
        servis.append({"identifiant": ids[pos], "identifiant_monde": identifiants_mondes[w], "enonce": p.texte})
        cle.append({"identifiant": ids[pos], "identifiant_monde": identifiants_mondes[w], "etiquette": p.etiquette,
                    "gabarit": p.gabarit, "empreinte_normalisee": p.empreinte,
                    "instance": p.en_dict()["instance"]})
    return ({"version": VERSION, "consigne": CONSIGNE_SERVIE, "items": servis},
            {"version": VERSION, "quotas": dict(quotas), "items": cle})
