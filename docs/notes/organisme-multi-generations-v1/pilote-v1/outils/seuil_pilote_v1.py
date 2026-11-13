"""Seuils de la règle du pilote (calcul léger, bibliothèque standard ; aucun appel). Usage :
`python3 -I -B seuil_pilote_v1.py SORTIE.json`.

Modèle d'approximation, écrit d'avance (sans pièce au-delà de la conception v4) :
- une conditionnelle survit à la génération 1 si aucune des 24 cartes ne la porte : s(p) = (1 − p)^24 (toute carte qui la porte
  est supposée retenue et captante : approximation **favorable à la capture**, donc défavorable à la règle de garde) ;
- monde sans chaîne (une conditionnelle) : garde une composante si elle survit ; monde à chaîne (deux) : si l'une des deux
  survit, 1 − (1 − s)² (indépendance supposée) ; part des mondes à chaîne : 2 sur 12 (sorties v4, `table-v4.json`, `145c0dbc…`) ;
- les moyennes ordinaires restées par hasard (1 monde sur 12 en v4) sont **ignorées** (défavorable à la règle) ;
- banc de 24 mondes ; la règle de garde tient si au moins 12 mondes gardent une composante : X ~ Binomiale(24, π(p)).
Rend : π(p) et P(règle tenue) sur une grille ; **p_max** = plus petit p de la grille (pas 0,0005) où P(règle tenue) ≤ 0,05 ;
**p_min_vue** = plus grand p tel que 1 − (1 − p)^24 < 0,5 (une conditionnelle dont la condition est connue serait trouvée en une
génération dans moins d'un monde sur deux) ; contrôle : π(0,02) comparé aux 8 mondes sur 12 de la v4 (`resume-v4.json`).
"""
import json
import math
import os
import sys

CARTES, MONDES_BANC, PART_CHAINE = 24, 24, 2 / 12


def survie(p):
    return (1.0 - p) ** CARTES


def pi(p):
    s = survie(p)
    return (1 - PART_CHAINE) * s + PART_CHAINE * (1 - (1 - s) ** 2)


def p_tenue(p, n=MONDES_BANC):
    q = pi(p)
    k0 = math.ceil(n / 2)
    return sum(math.comb(n, k) * q ** k * (1 - q) ** (n - k) for k in range(k0, n + 1))


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        print("usage : seuil_pilote_v1.py SORTIE.json (neuve)")
        return 2
    grille = [round(0.0005 * i, 4) for i in range(0, 601)]
    table = {f"{p:.4f}": {"survie": round(survie(p), 4), "pi": round(pi(p), 4), "regle_tenue": round(p_tenue(p), 4)} for p in grille}
    p_max = next(p for p in grille if p_tenue(p) <= 0.05)
    p_min_vue = max(p for p in grille if 1 - (1 - p) ** CARTES < 0.5)
    out = {"modele": {"cartes": CARTES, "mondes_banc": MONDES_BANC, "part_chaine": PART_CHAINE},
           "p_max": p_max, "regle_tenue_a_p_max": round(p_tenue(p_max), 4),
           "p_min_vue": p_min_vue,
           "controle_v4": {"pi_0_02": round(pi(0.02), 4), "observe_v4": "8/12 = 0,667", "regle_tenue_0_02_banc_24": round(p_tenue(0.02), 4)},
           "points": {k: table[k] for k in ("0.0000", "0.0100", "0.0200", "0.0300", "0.0400", "0.0500", "0.0750", "0.1000", "0.2500")},
           "table": table}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({k: out[k] for k in ("p_max", "regle_tenue_a_p_max", "p_min_vue", "controle_v4", "points")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
