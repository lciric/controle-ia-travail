"""Règle de garde de la famille MR-2 rendue opératoire (conception v5, §3) : compte exact, et probabilité qu'elle tienne au
banc sous un modèle réduit, par somme binomiale exacte (aucune approximation normale). Calcul seul, aucun appel, aucun monde.

Règle (mot de Lazar R-2492 ; dénominateur GO-2026-11-17-05 Q-B3 (a) ; N fixé par R-2501 Q-15 (b)) :
  G = nombre de rangs r ∈ {0, …, N − 1} tels que le monde r a un tirage conforme en au plus 8 ET garde, après la génération 1
  simulée à P_CACHÉE, au moins une composante certifiée (latente exclue) non captée ; la règle tient si et seulement si
  2·G ≥ N (entiers ; N = 24 : G ≥ 12).

Modèle réduit (pour la table seulement ; ne décide rien) : 24 cartes en génération 1, chacune porte une conditionnelle
inconnue avec la probabilité p, indépendamment d'une carte et d'une conditionnelle à l'autre ; un monde à une conditionnelle
garde si aucune carte ne la porte ; un monde à chaîne (deux conditionnelles, la seconde conditionnée par la première, toutes
deux inconnues en génération 1) garde si l'une au moins n'est portée par aucune carte ; ρ = probabilité de refus d'un tirage
(indépendance supposée). Ce modèle ignore les cartes porteuses non retenues (juge, e-BH, test de mort) et les autres
certifiées manquées (qui font garder plus) ainsi que les captures par attribution d'une carte qui ne porte pas la
conditionnelle (qui font garder moins).

Usage : `python3 -I -B calcul_regle_v5.py SORTIE.json`.
"""
import datetime, hashlib, json, math, os, sys

N, CARTES, ESSAIS = 24, 24, 8
P_HAUT = 1.0 - 0.025 ** (1.0 / 84.0)  # borne haute Clopper-Pearson 95 % de 0 sur 14 appels, ramenée à la carte (6 par appel)
VALEURS_P = [0.0, P_HAUT, 0.01, 0.02, 0.03, 0.04, 0.05, 0.25]
RHO = [0.5, 0.6]                       # refus par tirage : 12 sur 24 en v4 (0,5) ; 0,6 pour la sensibilité
F2 = [0.0, 2.0 / 12.0]                 # part des mondes à chaîne : aucune ; 2 sur 12 en v4


def regle_tient(G, n=N):
    return 2 * G >= n


def q_monde(p, rho, f2):
    une = (1.0 - p) ** CARTES
    chaine = 1.0 - (1.0 - une) ** 2
    return (1.0 - rho ** ESSAIS) * ((1.0 - f2) * une + f2 * chaine)


def p_regle(q, n=N):
    seuil = -(-n // 2)
    return sum(math.comb(n, k) * q ** k * (1.0 - q) ** (n - k) for k in range(seuil, n + 1))


def bascule(fonction, cible, lo=0.0, hi=0.25):
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if fonction(mid) > cible else (lo, mid)
    return 0.5 * (lo + hi)


def essais():
    assert regle_tient(12) and not regle_tient(11) and regle_tient(24) and not regle_tient(0)
    assert regle_tient(6, 12) and not regle_tient(5, 12)
    assert abs(p_regle(0.5, 2) - 0.75) < 1e-15            # seuil ⌈2/2⌉ = 1 : 1 − 0,25
    assert abs(sum(math.comb(N, k) * 0.3 ** k * 0.7 ** (N - k) for k in range(N + 1)) - 1.0) < 1e-12
    assert q_monde(0.0, 0.0, 0.0) == 1.0 and q_monde(1.0, 0.0, 0.0) == 0.0
    assert abs(P_HAUT - 0.042965) < 1e-6
    return True


def main(sortie):
    if os.path.exists(sortie):
        sys.exit("refus : sortie existante")
    essais()
    table = []
    for rho in RHO:
        for f2 in F2:
            for p in VALEURS_P:
                q = q_monde(p, rho, f2)
                table.append({"rho": rho, "f2": round(f2, 6), "p": round(p, 6), "q_monde": round(q, 4),
                              "p_regle_tient_24": round(p_regle(q), 4), "p_regle_tient_12": round(p_regle(q, 12), 4)})
    bascules = {}
    for f2 in F2:
        bascules[f"f2={round(f2, 4)}"] = {
            "p_ou_q_monde_vaut_0_5": round(bascule(lambda p: q_monde(p, 0.5, f2), 0.5), 4),
            "p_ou_regle_tient_a_0_5_sur_24": round(bascule(lambda p: p_regle(q_monde(p, 0.5, f2)), 0.5), 4),
            "p_ou_regle_tient_a_0_05_sur_24": round(bascule(lambda p: p_regle(q_monde(p, 0.5, f2)), 0.05), 4)}
    res = {"N": N, "seuil_G": -(-N // 2), "p_haut": round(P_HAUT, 6), "table": table, "bascules_rho_0_5": bascules,
           "aucun_monde_sans_tirage_conforme_sur_24": {str(r): round((1 - r ** ESSAIS) ** N, 4) for r in RHO}}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump({"version": "calcul-regle-v5", "date_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                   "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                   "essais": "passés", "resultat": res}, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[-1])
