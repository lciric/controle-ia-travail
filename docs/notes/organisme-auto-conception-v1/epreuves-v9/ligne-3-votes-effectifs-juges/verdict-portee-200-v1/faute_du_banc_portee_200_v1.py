"""Faute du banc de la mesure « portée à 200 » (additif 3 v3, § 6), contrôlée AVANT toute puissance.

Écrit par l'agent qui prononce, modèle O. Ne lit, n'imprime et n'écrit aucune puissance ni aucun compte de répliques
gagnées : seuls les champs de structure sont lus (comparaison, écart visé, loi, rho, rho', faisable, d, a, b, écart vrai
par formule, répliques, cause).

Usage : python3 -B faute_du_banc_portee_200_v1.py RESULTAT_200 RESULTAT_ETAGE_1 SORTIE_JSON
"""
import json
import math
import sys

RHOS = (0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9)
RHOS_PRIME = (0.0, 0.5, 0.9)
ECARTS = (0.05, 0.10, 0.15)
LOIS = (1, 3)
COMPARAISONS = ("unanimite", "juge_seul", "juge_repete_trois_votes_majorite")
TAUX = 0.20
D_MAX = 0.20
F = 0.25
TOL_ECART = 1e-9
REPLIQUES = 2000
CHAMPS_STRUCTURE = ("comparaison", "ecart_vise", "loi", "rho", "rho_prime", "faisable", "d", "vrais_rejetes_a",
                    "faux_acceptes_b", "ecart_vrai_formule", "repliques", "cause")


def enumeration_attendue():
    cellules = []
    for comp in COMPARAISONS:
        primes = RHOS_PRIME if comp == "juge_repete_trois_votes_majorite" else (0.0,)
        for ec in ECARTS:
            for loi in LOIS:
                for rho in RHOS:
                    for rp in primes:
                        cellules.append((comp, ec, loi, rho, rp))
    return cellules


def deux_en_erreur(p, rho):
    # probabilité que les deux juges se trompent, taux p chacun, corrélation des erreurs rho (lois 1 et 3)
    return p * p + rho * p * (1.0 - p)


def ee(d, rho, rho_prime):
    a, b = TAUX + d, TAUX - d
    qa, qb = deux_en_erreur(a, rho), deux_en_erreur(b, rho)
    r = lambda p: rho_prime * p + (1.0 - rho_prime) * (3 * p * p - 2 * p ** 3)
    return {
        "au_moins_un": 0.5 * (qa + (2 * b - qb)),
        "unanimite": 0.5 * ((2 * a - qa) + qb),
        "juge_seul": 0.5 * (a + b),
        "juge_repete_trois_votes_majorite": 0.5 * (r(a) + r(b)),
    }


def ecart_vrai(comp, d, rho, rho_prime):
    e = ee(d, rho, rho_prime)
    return e[comp] - e["au_moins_un"]


def resoudre(comp, ecart, rho, rho_prime):
    f = lambda d: ecart_vrai(comp, d, rho, rho_prime) - ecart
    lo, hi = 0.0, D_MAX
    flo, fhi = f(lo), f(hi)
    if flo > 0 or fhi < 0:
        return None
    for _ in range(200):
        mi = 0.5 * (lo + hi)
        if f(mi) < 0:
            lo = mi
        else:
            hi = mi
    return 0.5 * (lo + hi)


def loi_3_ok(p, rho):
    x = math.sqrt(rho * p * (1 - p) / (F * (1 - F)))
    return p - 0.25 * x >= -1e-12 and p + 0.75 * x <= 1 + 1e-12


def faisable_par_moi(comp, ecart, loi, rho, rp):
    d = resoudre(comp, ecart, rho, rp)
    if d is None:
        return False, None
    if loi == 3 and not (loi_3_ok(TAUX + d, rho) and loi_3_ok(TAUX - d, rho)):
        return False, d
    return True, d


def structure(c):
    return {k: c.get(k) for k in CHAMPS_STRUCTURE if k in c}


def main():
    chemin_200, chemin_100, chemin_sortie = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(chemin_200, encoding="utf-8") as fh:
        cell_200 = [structure(c) for c in json.load(fh)["monde_de_puissance"]]
    with open(chemin_100, encoding="utf-8") as fh:
        cell_100 = [structure(c) for c in json.load(fh)["monde_de_puissance"]]

    manques = []
    attendu = enumeration_attendue()

    # 1. 210 cellules, ordre gelé
    if len(cell_200) != 210:
        manques.append(f"nombre de cellules à 200 : {len(cell_200)} au lieu de 210")
    ordre_ok = len(cell_200) == len(attendu) and all(
        (c["comparaison"], c["ecart_vise"], c["loi"], c["rho"], c["rho_prime"]) == t for c, t in zip(cell_200, attendu))
    if not ordre_ok:
        manques.append("ordre des cellules à 200 différent de l'énumération gelée")
    ordre_100_ok = len(cell_100) == len(attendu) and all(
        (c["comparaison"], c["ecart_vise"], c["loi"], c["rho"], c["rho_prime"]) == t for c, t in zip(cell_100, attendu))
    if not ordre_100_ok:
        manques.append("ordre des cellules de l'étage 1 différent de l'énumération gelée")

    # 2. 2 000 répliques dans chaque cellule faisable
    faisables = [i for i, c in enumerate(cell_200) if c.get("faisable") is True]
    rep_mauvaises = [i for i in faisables if cell_200[i].get("repliques") != REPLIQUES]
    if rep_mauvaises:
        manques.append(f"répliques autres que 2 000 dans les cellules {rep_mauvaises}")

    # 3. treize mondes faisables à 0,10, eux seuls ; recalcul indépendant de la faisabilité
    a_010 = [i for i in faisables if abs(cell_200[i]["ecart_vise"] - 0.10) < 1e-12]
    mondes_010 = [(cell_200[i]["comparaison"], cell_200[i]["loi"], cell_200[i]["rho"], cell_200[i]["rho_prime"])
                  for i in a_010]
    attendus_par_paragraphe = {  # § 1, point 5 : comptes et bornes
        ("unanimite", 1): 4, ("unanimite", 3): 2, ("juge_seul", 1): 2, ("juge_seul", 3): 1,
        ("juge_repete_trois_votes_majorite", 1): 2, ("juge_repete_trois_votes_majorite", 3): 2}
    comptes = {}
    for comp, loi, rho, rp in mondes_010:
        comptes[(comp, loi)] = comptes.get((comp, loi), 0) + 1
        if comp == "unanimite" and rho > 0.45 + 1e-12:
            manques.append(f"monde faisable hors borne : {comp} loi {loi} rho {rho}")
        if comp == "juge_seul" and rho > 0.15 + 1e-12:
            manques.append(f"monde faisable hors borne : {comp} loi {loi} rho {rho}")
        if comp == "juge_repete_trois_votes_majorite" and not (rho == 0.0 and rp in (0.5, 0.9)):
            manques.append(f"monde faisable hors borne : {comp} loi {loi} rho {rho} rho' {rp}")
    if len(mondes_010) != 13:
        manques.append(f"mondes faisables à 0,10 : {len(mondes_010)} au lieu de 13")
    if comptes != attendus_par_paragraphe:
        manques.append(f"comptes de mondes faisables à 0,10 par comparaison et loi : {comptes}")

    desaccords_faisabilite = []
    d_moi_max_ecart = 0.0
    for i, (c, t) in enumerate(zip(cell_200, attendu)):
        f_moi, d_moi = faisable_par_moi(*t)
        if bool(c.get("faisable")) != f_moi:
            desaccords_faisabilite.append(i)
        if f_moi and c.get("d") is not None:
            d_moi_max_ecart = max(d_moi_max_ecart, abs(d_moi - c["d"]))
    if desaccords_faisabilite:
        manques.append(f"faisabilité recalculée différente aux rangs {desaccords_faisabilite}")

    # 4. écart vrai par formule égal à l'écart visé à 1e-9 près, dans chaque cellule faisable
    ecart_max_champ = 0.0
    ecart_max_moi = 0.0
    for i in faisables:
        c = cell_200[i]
        e_champ = abs(c["ecart_vrai_formule"] - c["ecart_vise"])
        e_moi = abs(ecart_vrai(c["comparaison"], c["d"], c["rho"], c["rho_prime"]) - c["ecart_vise"])
        ecart_max_champ = max(ecart_max_champ, e_champ)
        ecart_max_moi = max(ecart_max_moi, e_moi)
        if e_champ > TOL_ECART:
            manques.append(f"écart vrai par formule (champ) loin de l'écart visé au rang {i} : {e_champ}")
        if e_moi > TOL_ECART:
            manques.append(f"écart vrai recalculé loin de l'écart visé au rang {i} : {e_moi}")
        if abs(c["vrais_rejetes_a"] - (TAUX + c["d"])) > 1e-15 or abs(c["faux_acceptes_b"] - (TAUX - c["d"])) > 1e-15:
            manques.append(f"a ou b différent de 0,20 ± d au rang {i}")

    # 5. d, a, b égaux, cellule par cellule, à ceux de l'étage 1
    inegaux = []
    comparees = 0
    for i, (c2, c1) in enumerate(zip(cell_200, cell_100)):
        for k in ("faisable", "d", "vrais_rejetes_a", "faux_acceptes_b"):
            if (k in c2) != (k in c1):
                inegaux.append((i, k, "présence"))
            elif k in c2:
                comparees += 1
                if c2[k] != c1[k]:
                    inegaux.append((i, k, c2[k], c1[k]))
    if inegaux:
        manques.append(f"d, a, b ou faisabilité différents de l'étage 1 : {inegaux}")

    sortie = {
        "programme": "faute_du_banc_portee_200_v1.py",
        "aucune_puissance_lue": True,
        "cellules_a_200": len(cell_200),
        "cellules_etage_1": len(cell_100),
        "ordre_gele_a_200": ordre_ok,
        "ordre_gele_etage_1": ordre_100_ok,
        "cellules_faisables_tous_ecarts": len(faisables),
        "repliques_des_cellules_faisables": sorted({cell_200[i].get("repliques") for i in faisables}),
        "mondes_faisables_a_0_10": [
            {"rang": i, "comparaison": cell_200[i]["comparaison"], "loi": cell_200[i]["loi"], "rho": cell_200[i]["rho"],
             "rho_prime": cell_200[i]["rho_prime"], "d": cell_200[i]["d"], "a": cell_200[i]["vrais_rejetes_a"],
             "b": cell_200[i]["faux_acceptes_b"], "ecart_vrai_formule": cell_200[i]["ecart_vrai_formule"]}
            for i in a_010],
        "comptes_par_comparaison_et_loi_a_0_10": {f"{k[0]} loi {k[1]}": v for k, v in sorted(comptes.items())},
        "faisabilite_recalculee_par_moi_desaccords": desaccords_faisabilite,
        "d_recalcule_par_moi_plus_grand_ecart_au_champ": d_moi_max_ecart,
        "ecart_vrai_champ_plus_grand_ecart_a_l_ecart_vise": ecart_max_champ,
        "ecart_vrai_recalcule_plus_grand_ecart_a_l_ecart_vise": ecart_max_moi,
        "valeurs_d_a_b_faisable_comparees_a_l_etage_1": comparees,
        "valeurs_inegales_a_l_etage_1": len(inegaux),
        "manques": manques,
        "faute_du_banc": bool(manques),
    }
    with open(chemin_sortie, "x", encoding="utf-8") as fh:
        json.dump(sortie, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    print(json.dumps(sortie, ensure_ascii=False, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
