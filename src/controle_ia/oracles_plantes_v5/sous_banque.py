"""Sous-banque des bras S et N : 150 énoncés stratifiés par monde et par strate (75 vrais, 38 faux tôt, 37 pièges).

v5 (brouillon 2, § Plan d'analyse et A4) : plus 48 témoins servis, hors analyse (2 triviaux et 2 grossiers par monde,
tirés par l'enfant [2] après les strates), et 10 des 150 énoncés servis une seconde fois sous un autre identifiant
(tirés par l'enfant [6]) : 208 items par bras, mêlés, identifiants et ordre tirés par l'enfant (3, 1).

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
    items = [(w, p, "analyse", None) for w, p in choisis]
    # témoins servis, hors analyse (A4)
    tq = quotas.get("temoins", {"triviaux_par_monde": 0, "grossiers_par_monde": 0})
    for w, (_m, plantes) in enumerate(banque):
        for etiquette, cle_q in (("TEMOIN_TRIVIAL", "triviaux_par_monde"), ("TEMOIN_GROSSIER", "grossiers_par_monde")):
            pool = [p for p in plantes if p.etiquette == etiquette]
            k = int(tq[cle_q])
            if k > len(pool):
                raise GardeArret(f"sous-banque : {k} témoins {etiquette} demandés dans le monde {w}")
            for i in sorted(int(x) for x in rng.choice(len(pool), size=k, replace=False)):
                items.append((w, pool[i], "temoin_hors_analyse", None))
    # énoncés servis deux fois (enfant [6]), parmi les analysés
    nd = int(quotas.get("servis_deux_fois", 0))
    if nd:
        rng_d = generateur(racine, 6)
        for i in sorted(int(x) for x in rng_d.choice(len(choisis), size=nd, replace=False)):
            w, p = choisis[i]
            items.append((w, p, "second_service", i))
    rng_id = generateur(racine, 3, 1)
    ids = identifiants_opaques(rng_id, len(items), "item-")
    ordre = [int(i) for i in rng_id.permutation(len(items))]
    servis, cle = [], []
    for pos in ordre:
        w, p, role, double_de = items[pos]
        servis.append({"identifiant": ids[pos], "identifiant_monde": identifiants_mondes[w], "enonce": p.texte})
        cle.append({"identifiant": ids[pos], "identifiant_monde": identifiants_mondes[w], "etiquette": p.etiquette,
                    "gabarit": p.gabarit, "empreinte_normalisee": p.empreinte, "role": role,
                    "double_de": None if double_de is None else ids[double_de],
                    "instance": p.en_dict()["instance"]})
    return ({"version": VERSION, "consigne": CONSIGNE_SERVIE, "items": servis},
            {"version": VERSION, "quotas": dict(quotas), "items": cle})
