"""Comptes numériques sur les notations H.4 scellées : aucun texte de réponse n'est lu ni affiché.

Champs lus : jetons_contexte, jetons_reponse, tronquee (et la position dans la liste, qui suit l'ordre des lots).
"""
import json
import math
import sys

import numpy as np

racine = sys.argv[1]
D = f"{racine}/diag/20261017-193648-t05-notations-reel"
LOT = 8


def k_de(N):
    return N - math.floor(0.99 * (N - 1))


for juge in ("8B", "3B"):
    d = json.load(open(f"{D}/notations-{juge}-decisives.json"))
    ns = d["resultat"]["notations"]
    ctx = np.array([n["jetons_contexte"] for n in ns])
    rep = np.array([n["jetons_reponse"] for n in ns])
    tr = np.array([bool(n["tronquee"]) for n in ns])
    lots = [list(range(k, min(k + LOT, len(ns)))) for k in range(0, len(ns), LOT)]
    lots_tr = [i + 1 for i, l in enumerate(lots) if tr[l].any()]
    lots_sans = [i + 1 for i, l in enumerate(lots) if not tr[l].any()]
    cadre = [i + 1 for i, l in enumerate(lots) if len(l) == LOT and tr[l].any()]
    q75 = float(np.quantile(rep, 0.75))
    seuil = math.ceil(q75)
    part = float(np.mean(rep >= seuil))
    print(f"== juge {juge} : {len(ns)} notations, {len(lots)} lots (tailles {[len(l) for l in lots][-2:]})")
    print(f"   contexte : min {ctx.min()} max {ctx.max()} médiane {np.median(ctx)}")
    print(f"   réponses : médiane {np.median(rep)} ; q75 (linéaire) {q75} ; seuil entier {seuil} ; min {rep.min()} ; max {rep.max()}")
    print(f"   tronquées : {tr.sum()} ; longueurs des tronquées : {sorted(set(rep[tr].tolist()))}")
    print(f"   part des réponses >= seuil : {part:.4f} ({int(np.sum(rep >= seuil))}/{len(rep)}) ; P(au moins 1 sur 16) = {1 - (1 - part) ** 16:.4f}")
    print(f"   lots avec tronquée : {len(lots_tr)} ; sans : {lots_sans} ; cadre (lots de 8 avec tronquée) : {len(cadre)}")
    print(f"   lots avec tronquée (liste) : {lots_tr}")
    print(f"   dernier lot ({len(lots[-1])} rangées) porte une tronquée : {bool(tr[lots[-1]].any())}")
    pos = ctx + rep
    print(f"   positions (contexte + réponse) max : {pos.max()}")
    # Zone générée capturée pendant la génération : le dernier jeton tiré n'est jamais repassé (generer_lot l. 126-127),
    # d'où au plus min(passes, n_generes) positions ; pour une rangée tronquée : 3 071.
    gz_max_tronquee = 3072 - 1
    print(f"   zone générée capturée d'une rangée tronquée : au plus {gz_max_tronquee} positions")
    # Règle k(n - 1) sur les rangées H.4 (n = positions capturées au plus = contexte + réponse) :
    sous = 0
    for c, g in zip(ctx, rep):
        n = c + g          # borne haute ; la capture peut compter une position de moins
        N = n - 1
        zone = g - 1
        if zone < max(4, k_de(N)):
            sous += 1
    print(f"   rangées sous k(n-1) (avec n = contexte + réponse) : {sous}")
    sous2 = 0
    for c, g in zip(ctx, rep):
        n = c + g - 1      # cas où le dernier jeton n'est pas repassé
        N = n - 1
        zone = g - 2
        if zone < max(4, k_de(N)):
            sous2 += 1
    print(f"   rangées sous k(n-1) (avec n = contexte + réponse - 1) : {sous2}")

# Queues binomiales du témoin (16 tirages)
from math import comb


def queue_haute(k, n, p):
    return sum(comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


def queue_basse(k, n, p):
    return sum(comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(0, k + 1))


for juge, p in (("8B", 60 / 180), ("3B", 9 / 180)):
    bas = [k for k in range(17) if queue_basse(k, 16, p) < 0.005]
    haut = [k for k in range(17) if queue_haute(k, 16, p) < 0.005]
    print(f"== témoin {juge}, p = {p:.4f} : queue basse < 0,5 % pour T_w <= {max(bas) if bas else None} "
          f"(P(T<=0) = {queue_basse(0, 16, p):.5f}) ; queue haute < 0,5 % pour T_w >= {min(haut) if haut else None} "
          f"(P(T>={min(haut)}) = {queue_haute(min(haut), 16, p):.5f}, P(T>={min(haut) - 1}) = {queue_haute(min(haut) - 1, 16, p):.5f})")
