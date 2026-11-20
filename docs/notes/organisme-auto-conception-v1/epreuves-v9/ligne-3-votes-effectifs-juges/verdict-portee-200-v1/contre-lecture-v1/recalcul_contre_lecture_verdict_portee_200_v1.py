"""Recalcul indépendant du contre-lecteur neuf (modèle F) pour le verdict de la mesure « portée à 200 » de la ligne 3.

Écrit sans reprendre le code de l'agent qui prononce ni celui du banc. Deux temps, dans l'ordre de l'additif 3 v3, § 6 :
  temps 1 : faute du banc (cinq contrôles), sur les seuls champs de structure, sans aucune puissance ni aucun compte ;
  temps 2 : seulement si le temps 1 ne trouve aucun manque : comptes entiers, minima, puissance qui décide, issue du § 3,
            déclencheurs de l'audit du § 6, comparaison à l'étage 1, puis, en dernier, l'aide du code.

Formules, écrites par moi d'après le texte v7 (l. 101 à 104, l. 205, l. 236 à 238) :
  erreur commune de deux juges de taux p, corrélation rho : c(p) = p (rho + (1 - rho) p) ;
  bons témoins : taux d'erreur a = 0,20 + d ; mauvais témoins : b = 0,20 - d ;
  écart vrai contre l'unanimité : (a - b) - (c(a) - c(b)) = 1,2 d (1 - rho)   (forme fermée) ;
  écart vrai contre un juge seul : la moitié = 0,6 d (1 - rho)               (forme fermée) ;
  écart vrai contre le bras R : (m(a) + m(b)) / 2 - (c(a) + 2 b - c(b)) / 2,
      m(p) = rho' p + (1 - rho') (3 p^2 - 2 p^3)                              (racine cherchée par balayage puis dichotomie).

Usage : python3 -B recalcul_contre_lecture_verdict_portee_200_v1.py RESULTAT_200 RESULTAT_ETAGE_1 MANIFESTE_200 SORTIE_JSON
"""
import json
import math
import sys

TAUX_MOYEN = 0.20
BORNE_D = 0.20
PART_DIFFICILE = 0.25
REPLIQUES_VOULUES = 2000
LES_RHO = [0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9]
LES_RHO_PRIME = [0.0, 0.5, 0.9]
LES_ECARTS = [0.05, 0.10, 0.15]
LES_LOIS = [1, 3]
MONDES = ["unanimite", "juge_seul", "juge_repete_trois_votes_majorite"]
PLANTEES = {"unanimite": ["U"], "juge_seul": ["S_1", "S_2"], "juge_repete_trois_votes_majorite": ["R_3"]}
QUATRE = ["U", "S_1", "S_2", "R_3"]

# Les treize mondes faisables à l'écart de 0,10 (additif 3 v3, § 1, point 5), écrits à la main : (monde, loi, rho, rho').
TREIZE = {
    ("unanimite", 1, 0.0, 0.0), ("unanimite", 1, 0.15, 0.0), ("unanimite", 1, 0.3, 0.0), ("unanimite", 1, 0.45, 0.0),
    ("unanimite", 3, 0.0, 0.0), ("unanimite", 3, 0.15, 0.0),
    ("juge_seul", 1, 0.0, 0.0), ("juge_seul", 1, 0.15, 0.0),
    ("juge_seul", 3, 0.0, 0.0),
    ("juge_repete_trois_votes_majorite", 1, 0.0, 0.5), ("juge_repete_trois_votes_majorite", 1, 0.0, 0.9),
    ("juge_repete_trois_votes_majorite", 3, 0.0, 0.5), ("juge_repete_trois_votes_majorite", 3, 0.0, 0.9),
}


def commune(p, rho):
    return p * (rho + (1.0 - rho) * p)


def majorite_de_trois(p, rho_prime):
    return rho_prime * p + (1.0 - rho_prime) * (3.0 * p * p - 2.0 * p * p * p)


def ecart_vrai(monde, d, rho, rho_prime):
    a = TAUX_MOYEN + d
    b = TAUX_MOYEN - d
    au_moins_un = 0.5 * (commune(a, rho) + 2.0 * b - commune(b, rho))
    if monde == "unanimite":
        autre = 0.5 * (2.0 * a - commune(a, rho) + commune(b, rho))
    elif monde == "juge_seul":
        autre = 0.5 * (a + b)
    else:
        autre = 0.5 * (majorite_de_trois(a, rho_prime) + majorite_de_trois(b, rho_prime))
    return autre - au_moins_un


def racine_par_balayage(monde, cible, rho, rho_prime):
    """Plus petit d de [0 ; 0,20] où l'écart vrai vaut la cible ; None si aucun d ne l'atteint."""
    pas = 4000
    precedent_d = 0.0
    precedent_g = ecart_vrai(monde, 0.0, rho, rho_prime) - cible
    if abs(precedent_g) <= 1e-12:
        return 0.0
    for i in range(1, pas + 1):
        d = BORNE_D * i / pas
        g = ecart_vrai(monde, d, rho, rho_prime) - cible
        if abs(g) <= 1e-12:
            return d
        if (precedent_g < 0.0) != (g < 0.0):
            bas, haut, g_bas = precedent_d, d, precedent_g
            for _ in range(120):
                milieu = (bas + haut) / 2.0
                g_m = ecart_vrai(monde, milieu, rho, rho_prime) - cible
                if (g_m < 0.0) == (g_bas < 0.0):
                    bas, g_bas = milieu, g_m
                else:
                    haut = milieu
            return (bas + haut) / 2.0
        precedent_d, precedent_g = d, g
    return None


def forme_fermee(monde, cible, rho):
    if monde == "unanimite":
        return cible / (1.2 * (1.0 - rho))
    if monde == "juge_seul":
        return cible / (0.6 * (1.0 - rho))
    return None


def loi_3_tient(p, rho):
    etalement = math.sqrt(rho * p * (1.0 - p) / (PART_DIFFICILE * (1.0 - PART_DIFFICILE)))
    return (p - PART_DIFFICILE * etalement >= -1e-12) and (p + (1.0 - PART_DIFFICILE) * etalement <= 1.0 + 1e-12)


def mon_calcul(monde, cible, loi, rho, rho_prime):
    d = racine_par_balayage(monde, cible, rho, rho_prime)
    if d is None:
        return False, None
    if loi == 3 and not (loi_3_tient(TAUX_MOYEN + d, rho) and loi_3_tient(TAUX_MOYEN - d, rho)):
        return False, d
    return True, d


def mon_enumeration():
    liste = []
    for monde in MONDES:
        for cible in LES_ECARTS:
            for loi in LES_LOIS:
                for rho in LES_RHO:
                    for rho_prime in (LES_RHO_PRIME if monde == "juge_repete_trois_votes_majorite" else [0.0]):
                        liste.append((monde, cible, loi, rho, rho_prime))
    return liste


def proche(x, y, tol=1e-12):
    return abs(x - y) <= tol


def temps_1(m200, m100):
    """Faute du banc. Ne touche que : comparaison, ecart_vise, loi, rho, rho_prime, faisable, d, a, b, écart vrai, répliques."""
    manques = []
    rendu = {}
    attendu = mon_enumeration()

    # contrôle 1 : 210 cellules (et leur ordre)
    rendu["c1_cellules_a_200"] = len(m200)
    rendu["c1_cellules_etage_1"] = len(m100)
    if len(m200) != 210:
        manques.append("c1 : %d cellules au lieu de 210" % len(m200))
    def ordre(m):
        return len(m) == len(attendu) and all(
            c["comparaison"] == t[0] and proche(c["ecart_vise"], t[1]) and c["loi"] == t[2]
            and proche(c["rho"], t[3]) and proche(c["rho_prime"], t[4]) for c, t in zip(m, attendu))
    rendu["c1_ordre_gele_a_200"] = ordre(m200)
    rendu["c1_ordre_gele_etage_1"] = ordre(m100)
    if not rendu["c1_ordre_gele_a_200"]:
        manques.append("c1 : ordre des cellules à 200 autre que l'énumération gelée")
    if not rendu["c1_ordre_gele_etage_1"]:
        manques.append("c1 : ordre des cellules de l'étage 1 autre que l'énumération gelée")

    faisables = [i for i, c in enumerate(m200) if c.get("faisable") is True]
    rendu["cellules_faisables_tous_ecarts"] = len(faisables)
    rendu["cellules_faisables_par_ecart"] = {
        "%.2f" % e: sum(1 for i in faisables if proche(m200[i]["ecart_vise"], e)) for e in LES_ECARTS}

    # contrôle 2 : 2 000 répliques dans chaque cellule faisable
    hors = [i for i in faisables if m200[i].get("repliques") != REPLIQUES_VOULUES]
    rendu["c2_cellules_faisables_sans_2000_repliques"] = hors
    if hors:
        manques.append("c2 : répliques autres que 2 000 aux rangs %s" % hors)

    # contrôle 3 : à 0,10, les treize mondes, et eux seuls
    vus = {(m200[i]["comparaison"], m200[i]["loi"], round(m200[i]["rho"], 6), round(m200[i]["rho_prime"], 6))
           for i in faisables if proche(m200[i]["ecart_vise"], 0.10)}
    rendu["c3_mondes_faisables_a_0_10"] = len(vus)
    rendu["c3_absents_des_treize"] = sorted(map(list, TREIZE - vus))
    rendu["c3_en_trop"] = sorted(map(list, vus - TREIZE))
    if vus != TREIZE:
        manques.append("c3 : les mondes faisables à 0,10 ne sont pas les treize du § 1, point 5")

    # faisabilité et d recalculés par moi, sur les 210 cellules
    desaccords = []
    plus_grand_ecart_d = 0.0
    plus_grand_ecart_ferme = 0.0
    for i, (c, t) in enumerate(zip(m200, attendu)):
        f, d = mon_calcul(*t)
        if f != (c.get("faisable") is True):
            desaccords.append(i)
        if f and isinstance(c.get("d"), float):
            plus_grand_ecart_d = max(plus_grand_ecart_d, abs(d - c["d"]))
            ferme = forme_fermee(t[0], t[1], t[3])
            if ferme is not None:
                plus_grand_ecart_ferme = max(plus_grand_ecart_ferme, abs(ferme - c["d"]))
    rendu["faisabilite_recalculee_desaccords"] = desaccords
    rendu["d_balayage_plus_grand_ecart_au_resultat"] = plus_grand_ecart_d
    rendu["d_forme_fermee_plus_grand_ecart_au_resultat"] = plus_grand_ecart_ferme
    if desaccords:
        manques.append("faisabilité recalculée autre aux rangs %s" % desaccords)

    # contrôle 4 : écart vrai par formule égal à l'écart visé à 1e-9 près, cellules faisables
    pire_champ = 0.0
    pire_moi = 0.0
    for i in faisables:
        c = m200[i]
        e1 = abs(c["ecart_vrai_formule"] - c["ecart_vise"])
        e2 = abs(ecart_vrai(c["comparaison"], c["d"], c["rho"], c["rho_prime"]) - c["ecart_vise"])
        pire_champ = max(pire_champ, e1)
        pire_moi = max(pire_moi, e2)
        if e1 > 1e-9 or e2 > 1e-9:
            manques.append("c4 : écart vrai loin de l'écart visé au rang %d" % i)
    rendu["c4_plus_grand_ecart_champ"] = pire_champ
    rendu["c4_plus_grand_ecart_recalcule_par_moi"] = pire_moi

    # contrôle 5 : d, a, b égaux à l'étage 1, cellule par cellule (égalité exacte des flottants), et a = 0,20 + d, b = 0,20 - d
    inegaux = []
    comparees = 0
    hors_definition = []
    for i, (c2, c1) in enumerate(zip(m200, m100)):
        for k in ("faisable", "d", "vrais_rejetes_a", "faux_acceptes_b"):
            if (k in c2) != (k in c1):
                inegaux.append([i, k])
            elif k in c2:
                comparees += 1
                if c2[k] != c1[k] or type(c2[k]) is not type(c1[k]):
                    inegaux.append([i, k])
        if c2.get("faisable") is True:
            if c2["vrais_rejetes_a"] != TAUX_MOYEN + c2["d"] or c2["faux_acceptes_b"] != TAUX_MOYEN - c2["d"]:
                hors_definition.append(i)
    rendu["c5_valeurs_comparees_a_l_etage_1"] = comparees
    rendu["c5_valeurs_inegales"] = inegaux
    rendu["c5_a_b_hors_de_0_20_plus_ou_moins_d"] = hors_definition
    if inegaux:
        manques.append("c5 : d, a, b ou faisabilité autres qu'à l'étage 1 : %s" % inegaux)
    if hors_definition:
        manques.append("c5 : a ou b autre que 0,20 ± d aux rangs %s" % hors_definition)

    rendu["manques"] = manques
    rendu["faute_du_banc"] = bool(manques)
    return rendu, faisables


def comptes_200(c):
    """Comptes entiers lus dans le champ entier du résultat, recoupés avec la puissance."""
    k = c["repliques_gagnees_par_comparaison"]
    p = c["puissance_par_comparaison"]
    for nom in QUATRE:
        if type(k[nom]) is not int or not (0 <= k[nom] <= c["repliques"]):
            raise SystemExit("compte non entier ou hors bornes")
        if abs(k[nom] / c["repliques"] - p[nom]) > 1e-12:
            raise SystemExit("compte et puissance en désaccord")
    return {nom: k[nom] for nom in QUATRE}


def comptes_100(c):
    """L'étage 1 ne porte que des puissances : compte = puissance fois répliques, exigé entier."""
    sortie = {}
    for nom in QUATRE:
        x = c["puissance_par_comparaison"][nom] * c["repliques"]
        k = int(round(x))
        if abs(x - k) > 1e-7:
            raise SystemExit("puissance de l'étage 1 qui n'est pas un compte entier")
        sortie[nom] = k
    return sortie


def lecture_du_paragraphe_3(m, lire):
    """Minima par comparaison sur les cellules faisables des lois 1 et 3 à l'écart de 0,10 ; issue du § 3."""
    par_comparaison = {nom: [] for nom in QUATRE}
    for rang, c in enumerate(m):
        if c.get("faisable") is True and proche(c["ecart_vise"], 0.10) and c["loi"] in (1, 3):
            k = lire(c)
            for nom in PLANTEES[c["comparaison"]]:
                par_comparaison[nom].append((k[nom], rang))
    sans = [nom for nom in QUATRE if not par_comparaison[nom]]
    minima = {}
    for nom in QUATRE:
        if par_comparaison[nom]:
            plus_bas = min(k for k, _ in par_comparaison[nom])
            minima[nom] = {"compte": plus_bas, "rangs": [r for k, r in par_comparaison[nom] if k == plus_bas]}
    return par_comparaison, sans, minima


def temps_2(m200, m100, faisables, aide):
    rendu = {}
    par_comparaison, sans, minima = lecture_du_paragraphe_3(m200, comptes_200)
    rendu["cellules_lues_par_comparaison"] = {nom: len(v) for nom, v in par_comparaison.items()}
    rendu["comptes_lus_par_comparaison"] = {
        nom: [{"rang": r, "loi": m200[r]["loi"], "rho": m200[r]["rho"], "rho_prime": m200[r]["rho_prime"], "compte": k}
              for k, r in v] for nom, v in par_comparaison.items()}
    rendu["comparaisons_sans_cellule_faisable"] = sans
    rendu["minima_par_comparaison"] = {
        nom: {"compte": v["compte"], "puissance": v["compte"] / REPLIQUES_VOULUES,
              "cellules": [{"rang": r, "monde": m200[r]["comparaison"], "loi": m200[r]["loi"], "rho": m200[r]["rho"],
                            "rho_prime": m200[r]["rho_prime"]} for r in v["rangs"]]} for nom, v in minima.items()}
    if sans:
        k_decide = None
        issue = "B"
    else:
        k_decide = min(v["compte"] for v in minima.values())
        issue = "B" if k_decide < 1000 else "A"   # « sous 0,5 » strict : 1 000 sur 2 000 est l'issue A
    rendu["compte_qui_decide"] = k_decide
    rendu["puissance_qui_decide"] = None if k_decide is None else k_decide / REPLIQUES_VOULUES
    rendu["cellules_qui_decident"] = [] if k_decide is None else [
        {"comparaison": nom, "rang": r, "monde": m200[r]["comparaison"], "loi": m200[r]["loi"], "rho": m200[r]["rho"],
         "rho_prime": m200[r]["rho_prime"]} for nom, v in minima.items() if v["compte"] == k_decide for r in v["rangs"]]
    rendu["issue_du_paragraphe_3"] = issue
    rendu["pres_du_seuil"] = k_decide is not None and 956 <= k_decide <= 1044   # 0,478 à 0,522 de 2 000
    rendu["prediction_du_paragraphe_1_tenue"] = k_decide is not None and 600 <= k_decide < 1000  # 0,30 à 0,50, sous 0,5
    rendu["prediction_refutee_0_5_ou_plus"] = k_decide is not None and k_decide >= 1000

    # étage 1, même lecture
    _, sans_1, minima_1 = lecture_du_paragraphe_3(m100, comptes_100)
    repliques_1 = sorted({c["repliques"] for c in m100 if c.get("faisable") is True})
    k_1 = min(v["compte"] for v in minima_1.values())
    rendu["etage_1_repliques_des_cellules_faisables"] = repliques_1
    rendu["etage_1_compte_qui_decide"] = k_1
    rendu["etage_1_puissance_qui_decide"] = k_1 / repliques_1[0]
    rendu["etage_1_cellules_qui_decident"] = [
        {"comparaison": nom, "rang": r, "loi": m100[r]["loi"], "rho": m100[r]["rho"]}
        for nom, v in minima_1.items() if v["compte"] == k_1 for r in v["rangs"]]
    rendu["etage_1_comparaisons_sans_cellule_faisable"] = sans_1

    # déclencheurs de l'audit du § 6
    zeros_et_uns = []
    lignes = []
    baissent = []
    regles = []
    somme_replis = 0
    for rang in faisables:
        c = m200[rang]
        k2 = comptes_200(c)
        k1 = comptes_100(m100[rang])
        r1 = m100[rang]["repliques"]
        for nom in QUATRE:
            if k2[nom] == 0 or k2[nom] == c["repliques"]:
                d = c["d"]
                a, b = TAUX_MOYEN + d, TAUX_MOYEN - d
                amu = 0.5 * (commune(a, c["rho"]) + 2.0 * b - commune(b, c["rho"]))
                r_zero = 0.5 * (majorite_de_trois(a, 0.0) + majorite_de_trois(b, 0.0))
                zeros_et_uns.append({
                    "rang": rang, "monde": c["comparaison"], "ecart_vise": c["ecart_vise"], "loi": c["loi"],
                    "rho": c["rho"], "rho_prime": c["rho_prime"], "comparaison": nom,
                    "plantee": nom in PLANTEES[c["comparaison"]], "compte": k2[nom],
                    "ecart_vrai_bras_R_a_rho_prime_0_moins_au_moins_un": r_zero - amu,
                    "ecart_observe_moyen": c["ecart_observe_moyen"][nom]})
        for nom in PLANTEES[c["comparaison"]]:
            ligne = {"rang": rang, "monde": c["comparaison"], "ecart_vise": c["ecart_vise"], "loi": c["loi"],
                     "rho": c["rho"], "rho_prime": c["rho_prime"], "comparaison": nom,
                     "compte_a_100": k1[nom], "compte_a_200": k2[nom],
                     "baisse": k2[nom] * r1 < k1[nom] * c["repliques"]}
            lignes.append(ligne)
            if ligne["baisse"]:
                baissent.append(ligne)
        somme_replis += c["bras_C_repli_poids_egaux"]
        regles.append({"rang": rang, "ecart_vise": c["ecart_vise"], "monde": c["comparaison"], "loi": c["loi"],
                       "rho": c["rho"], "rho_prime": c["rho_prime"], "regles": c["bras_C_regle_choisie"],
                       "somme_des_regles": sum(c["bras_C_regle_choisie"].values()),
                       "replis": c["bras_C_repli_poids_egaux"],
                       "ecart_observe_moyen": c["ecart_observe_moyen"]})
    p2 = rendu["puissance_qui_decide"]
    p1 = rendu["etage_1_puissance_qui_decide"]
    rendu["declencheurs"] = {
        "a_200_sous_celle_de_100": p2 is not None and p2 < p1,
        "au_dessus_de_0_90": p2 is not None and p2 > 0.90,
        "cellule_faisable_a_0_ou_1_toute_comparaison": bool(zeros_et_uns),
        "cellule_faisable_a_0_ou_1_comparaison_plantee": any(z["plantee"] for z in zeros_et_uns),
        "hors_de_l_intervalle_predit": p2 is None or p2 < 0.30 or p2 >= 0.50,
    }
    rendu["cellules_a_0_ou_1"] = zeros_et_uns
    rendu["lignes_comparees_100_contre_200"] = len(lignes)
    rendu["lignes_qui_baissent"] = baissent
    rendu["treize_mondes_100_vers_200"] = [l for l in lignes if proche(l["ecart_vise"], 0.10)]
    rendu["somme_des_replis_du_bras_C_cellules_faisables"] = somme_replis
    rendu["regles_du_bras_C_a_0_10"] = [r for r in regles if proche(r["ecart_vise"], 0.10)]
    rendu["regles_du_bras_C_a_0_05_monde_unanimite"] = [
        r for r in regles if proche(r["ecart_vise"], 0.05) and r["monde"] == "unanimite"]
    rendu["au_moins_un_la_plus_choisie_dans_chaque_cellule_a_0_10"] = all(
        r["regles"]["au_moins_un"] == max(r["regles"].values()) for r in rendu["regles_du_bras_C_a_0_10"])

    # en dernier : l'aide du code
    rendu["aide"] = {
        "issue": aide.get("issue"), "puissance_qui_decide": aide.get("puissance_qui_decide"),
        "compte": aide.get("repliques_gagnees_dans_la_cellule_la_plus_basse"),
        "minima_en_comptes": aide.get("minima_par_comparaison_en_repliques_gagnees"),
        "pres_du_seuil": aide.get("pres_du_seuil"),
        "comparaisons_sans_cellule_faisable": aide.get("comparaisons_sans_cellule_faisable")}
    rendu["aide_egale_a_mon_recalcul"] = (
        aide.get("issue") == issue and aide.get("repliques_gagnees_dans_la_cellule_la_plus_basse") == k_decide
        and aide.get("puissance_qui_decide") == rendu["puissance_qui_decide"]
        and aide.get("minima_par_comparaison_en_repliques_gagnees") == {n: v["compte"] for n, v in minima.items()}
        and aide.get("comparaisons_sans_cellule_faisable") == sans)
    return rendu


def main():
    chemin_200, chemin_100, chemin_manifeste, chemin_sortie = sys.argv[1:5]
    with open(chemin_200, encoding="utf-8") as fh:
        r200 = json.load(fh)
    with open(chemin_100, encoding="utf-8") as fh:
        r100 = json.load(fh)
    with open(chemin_manifeste, encoding="utf-8") as fh:
        manifeste = json.load(fh)

    def chercher_n(objet):
        trouves = []
        if isinstance(objet, dict):
            for k, v in objet.items():
                if k == "n":
                    trouves.append(v)
                trouves.extend(chercher_n(v))
        elif isinstance(objet, list):
            for v in objet:
                trouves.extend(chercher_n(v))
        return trouves

    sortie = {"programme": "recalcul_contre_lecture_verdict_portee_200_v1.py",
              "n_au_manifeste_de_la_mesure": chercher_n(manifeste)}
    faute, faisables = temps_1(r200["monde_de_puissance"], r100["monde_de_puissance"])
    sortie["temps_1_faute_du_banc"] = faute
    if faute["faute_du_banc"]:
        sortie["temps_2"] = "non joué : faute du banc, issue C"
        sortie["issue"] = "C"
    else:
        sortie["temps_2_comptes_et_issue"] = temps_2(
            r200["monde_de_puissance"], r100["monde_de_puissance"], faisables, r200["criteres_mecaniques"]["puissance"])
        sortie["issue"] = sortie["temps_2_comptes_et_issue"]["issue_du_paragraphe_3"]
    with open(chemin_sortie, "x", encoding="utf-8") as fh:
        json.dump(sortie, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    print("issue :", sortie["issue"], "; faute du banc :", faute["faute_du_banc"], "; manques :", len(faute["manques"]))


if __name__ == "__main__":
    main()
