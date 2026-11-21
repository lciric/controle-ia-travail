#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle, sur une sortie factice, que le décalage de la dérive de F porté par T09 triple
le taux de 1 % sous la loi (normale) de la tranche de F dont `n_calibration` contient 299.

Lit le fichier, trouve la tranche (la première qui contient 299) et la clé de décalage
(`decalage_en_ecarts_types`), puis calcule, avec `statistics.NormalDist` :
- le seuil s au quantile à 99 % de la loi de la tranche ;
- le taux au même seuil sous la loi décalée de δ écarts types.
Écrit les nombres et le verdict à la tolérance absolue de 0,001 sur 0,03.

Usage : python3 -I -B verifier_decalage_factice_v4.py SORTIE_FACTICE

Développeur du programme de vérification de la sortie des mondes, modèle O.
"""

import json
import sys
from statistics import NormalDist


def principal(argv):
    if len(argv) != 1:
        print("usage : SORTIE_FACTICE", file=sys.stderr)
        return 3
    with open(argv[0], encoding="utf-8") as fh:
        doc = json.load(fh)
    f = next(x for x in doc["familles"] if x["id"] == "F")
    tranche = next(tr for tr in f["tranches"] if 299 in tr["n_calibration"])
    loi = tranche["loi_honnete"]
    if loi["type"] != "normale":
        print("loi de la tranche non normale : contrôle hors de ce programme", file=sys.stderr)
        return 3
    mu, sigma = loi["parametres"]["mu"], loi["parametres"]["sigma"]
    t09 = next(t for t in doc["temoins"] if t["id"] == "T09")
    delta = t09["valeurs_de_plus"]["decalage_en_ecarts_types"]
    avant = NormalDist(mu, sigma)
    seuil = avant.inv_cdf(0.99)
    apres = NormalDist(mu + delta * sigma, sigma)
    taux_avant = 1 - avant.cdf(seuil)
    taux_apres = 1 - apres.cdf(seuil)
    exact = (avant.inv_cdf(0.99) - avant.inv_cdf(0.97)) / sigma
    coherent = abs(taux_apres - 0.03) <= 0.001
    print("loi de la tranche a 299 : normale(mu=%r, sigma=%r)" % (mu, sigma))
    print("decalage transmis (ecarts types) : %r" % delta)
    print("decalage exact qui triple (ecarts types) : %.10f" % exact)
    print("taux avant derive au seuil : %.10f" % taux_avant)
    print("taux apres derive au seuil : %.10f" % taux_apres)
    print("ecart absolu a 0.03 : %.3e ; tolerance absolue 0.001" % abs(taux_apres - 0.03))
    print("verdict : %s" % ("coherente" if coherent else "incoherente"))
    return 0 if coherent else 1


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
