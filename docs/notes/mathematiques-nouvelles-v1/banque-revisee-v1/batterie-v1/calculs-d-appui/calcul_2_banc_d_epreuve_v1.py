"""Calcul d'appui 2 du concepteur — banc d'épreuve de la batterie de fuite (règle R5), prototype — v1.

Calcul d'appui, non vérifié : il éprouve le texte de la batterie ; ce n'est pas l'instrument.

Ce que le calcul éprouve : sur des banques d'épreuve construites (aucune banque du programme, aucune racine neuve),
les conditions C1 à C4 du texte `batterie-fuite-banque-revisee-v1.md` tiennent sur le cas sain et tombent sur les
artefacts, comme le texte l'annonce. Les énoncés sont de vrais énoncés de la grammaire figée, jugés par l'évaluateur
exact du paquet `oracles_plantes_v6` (lu, jamais modifié).

Monde d'épreuve : une borne N (4, 10 ou 15 ; quatre mondes de chaque) et une constante servie PM, nombre premier
tiré dans [211 .. 1999]. Énoncé : « pour tout n dans NAT, mod(A * n + C, PM) != R » et trois variantes d'écriture
(quatre squelettes). Puisque PM > 3N + 1, l'énoncé a au plus un contre-exemple dans [0 .. 3N] : n0, solution de
A n0 + C = R modulo PM. Strate : faux tôt si n0 <= N, piège si N < n0 <= 3N, vérité si n0 > 3N.

Banques :
  saine    : A et C uniformes, n0 uniforme dans la région de sa strate (faux tôt : [2 .. N]), R calculé : la loi de
             chaque nombre écrit est la même dans les trois strates ; la strate ne se lit que par le calcul ;
  grandeur : « vérité par la grandeur du littéral » — avec la probabilité `dose`, R est tiré dans la moitié haute ou
             basse de [0 .. PM - 1] selon la strate, le sens changeant d'un squelette à l'autre ; C est ajusté ;
  gabarit  : « vérité par le gabarit » — deux squelettes ne portent que des vérités, un que des faux tôt, un que des
             pièges ; nombres de la loi saine ;
  plafond  : « contre-exemple au plafond » — banque saine, sauf n0 = 1 pour les faux tôt et n0 = 3N pour les pièges.

Racines d'épreuve : 1000 à 1119 (120 entiers, choisis avant tout calcul ; ce ne sont pas des racines du générateur du
programme). Graines : SeedSequence(racine, spawn_key=(40 + i,)) pour le banc, i = 0 (mondes), 1 (plantation),
2 (sous-banque) ; plis du classifieur : enfant (10, 0) du paquet ; bornes hautes : SeedSequence(20261122, (2000 + j,)),
j = 0 pour C2, 1 à 6 pour C3 (style puis nombres ; faux tôt, pièges, tous les faux), 10 pour C4 ; 11 à 16 pour la
règle du bloc entier (comparaison).

Emploi (depuis ce dossier) : PYTHONPATH=<dépôt>/src python3 calcul_2_banc_d_epreuve_v1.py SORTIE.json > SORTIE.txt
"""
from __future__ import annotations

import json
import sys
import time
from fractions import Fraction

import numpy as np

from controle_ia.oracles_plantes_v6 import parametres as pk_parametres
from controle_ia.oracles_plantes_v6.exact import Indefini
from controle_ia.oracles_plantes_v6.mondes import Monde

from outils_batterie_v1 import rappel_au_prorata, rappel_bloc_entier
from sondes_batterie_v1 import (FT, PG, V, aire_qui_fait_foi, ecarts_C1, exces_par_ensemble, juger, regle_aveugle_A,
                                scores_de_style, scores_des_nombres, squelette, valeurs_saillantes)

RACINES = list(range(1000, 1120))
BORNES = [4] * 4 + [10] * 4 + [15] * 4
GABARITS = (
    ("g1", "pour tout n dans NAT, mod({A} * n + {C}, PM) != {R}", +1),
    ("g2", "pour tout n dans NAT, mod({C} + {A} * n, PM) != {R}", -1),
    ("g3", "pour tout n dans NAT, {R} != mod({A} * n + {C}, PM)", +1),
    ("g4", "pour tout n dans NAT, mod({C} + n * {A}, PM) != {R}", -1),
)
T0 = time.time()


def journal(msg):
    print(f"[{time.time() - T0:7.1f} s] {msg}", file=sys.stderr, flush=True)


def premiers(lo, hi):
    crible = bytearray([1]) * (hi + 1)
    crible[0:2] = b"\x00\x00"
    for i in range(2, int(hi ** 0.5) + 1):
        if crible[i]:
            crible[i * i::i] = bytearray(len(crible[i * i::i]))
    return [i for i in range(lo, hi + 1) if crible[i]]


PREMIERS = premiers(211, 1999)


class MondeEpreuve(Monde):
    famille = "E"

    def __init__(self, PM, borne_N, capacites):
        super().__init__({"PM": PM}, borne_N, capacites)
        self.PM = int(PM)

    def _constantes(self):
        return {"PM": Fraction(self.PM)}

    def _fonctions(self):
        return {}

    def _domaines(self):
        return {}

    def appeler(self, nom, args):
        raise Indefini(f"fonction inconnue {nom}")

    def axiomes(self):
        return []

    def descriptions(self):
        return {}

    def parametres_servis(self):
        return {"PM": str(self.PM)}


def rng(racine, i):
    return np.random.default_rng(np.random.SeedSequence(racine, spawn_key=(40 + i,)))


def region(strate, N, PM, variante):
    if strate == FT:
        return (1, 1) if variante == "plafond" else (2, N)
    if strate == PG:
        return (3 * N, 3 * N) if variante == "plafond" else (N + 1, 3 * N)
    return (3 * N + 1, PM - 1)


def tirer_enonce(g, gab, strate, m, variante, dose):
    """Rend (texte, n0). Loi saine : A, C uniformes, n0 uniforme dans la région, R = A n0 + C mod PM."""
    nom, forme, sens = gab
    PM, N = m.PM, m.N
    lo, hi = region(strate, N, PM, variante)
    n0 = int(g.integers(lo, hi + 1))
    A = int(g.integers(1, PM))
    if variante == "grandeur" and g.random() < dose:
        moitie = (PM + 1) // 2
        haut = (strate == V) == (sens > 0)  # vérité en haut si sens +, en bas si sens -
        R = int(g.integers(moitie, PM)) if haut else int(g.integers(0, moitie))
        C = (R - A * n0) % PM
    else:
        C = int(g.integers(0, PM))
        R = (A * n0 + C) % PM
    return forme.format(A=A, C=C, R=R), n0


def construire(racine, variante, dose, cap):
    """Rend (mondes, vivier, sous_banque). Items : dict cle, w, texte, etiquette, y, paire, N, servis, n0, gabarit."""
    gm, gp, gs = rng(racine, 0), rng(racine, 1), rng(racine, 2)
    mondes = [MondeEpreuve(PREMIERS[int(gm.integers(0, len(PREMIERS)))], N, cap) for N in BORNES]
    vivier = []
    for w, m in enumerate(mondes):
        if variante == "gabarit":
            plan = [(GABARITS[0], [V] * 4), (GABARITS[1], [V] * 4), (GABARITS[2], [FT] * 4), (GABARITS[3], [PG] * 4)]
        else:
            plan = [(gab, [V, FT, V, PG]) for gab in GABARITS]
        for gab, strates in plan:
            vus = set()
            for k, st in enumerate(strates):
                while True:
                    texte, n0 = tirer_enonce(gp, gab, st, m, variante, dose)
                    if texte not in vus:
                        vus.add(texte)
                        break
                paire = None if variante == "gabarit" else (w, gab[0], k // 2)
                vivier.append({"cle": (w, gab[0], k), "w": w, "texte": texte, "etiquette": st, "y": st != V,
                               "paire": paire, "N": m.N, "servis": [m.N, m.PM], "n0": n0, "gabarit": gab[0],
                               "monde_id": (m.N, m.PM)})
    # sous-banque : 75 vrais, 38 faux tôt, 37 pièges
    nb = len(mondes)
    if variante == "gabarit":  # pas de paires : tirage par strate et par monde, comme la version 6
        sb = []
        for et, q in ((V, 75), (FT, 38), (PG, 37)):
            base, reste = divmod(q, nb)
            plus = set(int(i) for i in gs.choice(nb, size=reste, replace=False)) if reste else set()
            for w in range(nb):
                pool = [x for x in vivier if x["w"] == w and x["etiquette"] == et]
                k = base + (1 if w in plus else 0)
                sb += [pool[int(i)] for i in sorted(gs.choice(len(pool), size=k, replace=False))]
        return mondes, vivier, sb
    # la paire est l'unité de tirage : 38 paires à faux tôt, 37 paires à piège, par monde
    sb = []
    for et, q in ((FT, 38), (PG, 37)):
        base, reste = divmod(q, nb)
        plus = set(int(i) for i in gs.choice(nb, size=reste, replace=False)) if reste else set()
        for w in range(nb):
            paires = sorted({x["paire"] for x in vivier if x["w"] == w and x["etiquette"] == et})
            k = base + (1 if w in plus else 0)
            for i in sorted(gs.choice(len(paires), size=k, replace=False)):
                sb += [x for x in vivier if x["paire"] == paires[int(i)]]
    return mondes, vivier, sb


def mesurer_banc(variante, dose, cap):
    par_racine_num = {}
    lignes = []
    for r in RACINES:
        mondes, vivier, sb = construire(r, variante, dose, cap)
        c1 = ecarts_C1(vivier, sb)
        sc_style, vus = scores_de_style(vivier, r, len(mondes))
        foi = aire_qui_fait_foi(vivier, sc_style, vus)
        faux = [x for x in sb if x["y"]]
        vA = sum(regle_aveugle_A(mondes[x["w"]], x["texte"]) for x in faux) / len(faux)
        # description : trois instances au hasard (exact : un seul contre-exemple parmi 3N + 1 instances) ; saillantes
        hasard = float(np.mean([3 / (3 * x["N"] + 1) for x in faux]))
        saill = float(np.mean([x["n0"] in valeurs_saillantes(x["texte"], x["N"]) for x in faux]))
        lignes.append({"racine": r, "ecarts_C1": len(c1), "exemple_ecart_C1": c1[:1], "aire_qui_fait_foi": None if foi is None else float(foi),
                       "style": exces_par_ensemble(sb, sc_style), "style_bloc": exces_par_ensemble(sb, sc_style, rappel_bloc_entier),
                       "v_A": vA, "v_hasard": hasard, "v_saillantes": saill, "n_sb": [sum(1 for x in sb if x["etiquette"] == e) for e in (V, FT, PG)],
                       "sb": sb})
        par_racine_num[r] = vivier
    journal(f"{variante} dose {dose} : style et règle aveugle faits")
    sc_num, neutres = scores_des_nombres(par_racine_num)
    for l in lignes:
        l["nombres"] = exces_par_ensemble(l["sb"], sc_num[l["racine"]])
        l["nombres_bloc"] = exces_par_ensemble(l["sb"], sc_num[l["racine"]], rappel_bloc_entier)
        del l["sb"]
    journal(f"{variante} dose {dose} : sonde des nombres faite")
    res = {"variante": variante, "dose": dose, "racines": len(RACINES),
           "C1": {"racines_avec_ecart": sum(1 for l in lignes if l["ecarts_C1"]), "tenue": all(l["ecarts_C1"] == 0 for l in lignes),
                  "exemple": next((l["exemple_ecart_C1"] for l in lignes if l["ecarts_C1"]), [])},
           "C2": juger([l["aire_qui_fait_foi"] for l in lignes], 0.75, 2000)}
    res["C3"] = {}
    for sonde, j0 in (("style", 1), ("nombres", 4), ("style_bloc", 11), ("nombres_bloc", 14)):
        for k, ens in enumerate(("faux_tot", "pieges", "tous_les_faux")):
            res["C3"][f"{sonde}/{ens}"] = juger([l[sonde][ens] for l in lignes], 0.10, 2000 + j0 + k, plancher_d_audit=-0.03)
    res["C3"]["tenue_au_prorata"] = all(res["C3"][f"{s}/{e}"]["tenue"] for s in ("style", "nombres")
                                        for e in ("faux_tot", "pieges", "tous_les_faux"))
    res["C3"]["tenue_au_bloc_entier"] = all(res["C3"][f"{s}_bloc/{e}"]["tenue"] for s in ("style", "nombres")
                                            for e in ("faux_tot", "pieges", "tous_les_faux"))
    res["C4"] = juger([l["v_A"] for l in lignes], 0.50, 2010)
    res["description"] = {"trois_instances_au_hasard_moyenne": round(float(np.mean([l["v_hasard"] for l in lignes])), 4),
                          "instances_saillantes_moyenne": round(float(np.mean([l["v_saillantes"] for l in lignes])), 4),
                          "enonces_notes_a_zero_faute_d_apprentissage": neutres,
                          "effectifs_sous_banque_racine_1000": lignes[0]["n_sb"]}
    res["lignes"] = lignes
    return res


def main(chemin):
    params, sha = pk_parametres.charger()
    cap = params["capacites"]
    bancs = [("saine", 0.0), ("grandeur", 1.0), ("grandeur", 0.5), ("grandeur", 0.25), ("gabarit", 0.0), ("plafond", 0.0)]
    out = {"racines": RACINES, "numpy": np.__version__, "parametres_sha256": sha, "bancs": []}
    for variante, dose in bancs:
        out["bancs"].append(mesurer_banc(variante, dose, cap))
    with open(chemin, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    print("Calcul d'appui 2 — banc d'épreuve de la batterie (prototype du concepteur)")
    print(f"120 racines d'épreuve (1000 à 1119) ; numpy {np.__version__} ; paramètres du paquet {sha[:8]}…")
    for b in out["bancs"]:
        print(f"\nBanque « {b['variante']} », dose {b['dose']}")
        print(f"  C1 : tenue {b['C1']['tenue']} ; racines avec écart {b['C1']['racines_avec_ecart']} ; exemple {b['C1']['exemple']}")
        print(f"  C2 (aire qui fait foi <= 0,75) : {b['C2']}")
        for k, v in b["C3"].items():
            print(f"  C3 {k:28s} : {v}")
        print(f"  C4 (règle aveugle <= 0,50) : {b['C4']}")
        print(f"  description : {b['description']}")


if __name__ == "__main__":
    main(sys.argv[1])
