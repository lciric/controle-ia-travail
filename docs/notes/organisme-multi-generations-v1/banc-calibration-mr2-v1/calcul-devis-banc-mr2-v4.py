"""Calcul du devis v4 du banc complet MR-2 (arithmétique seule : aucun monde, aucun tirage aléatoire, aucun appel, aucun réseau).

Entrées : la sortie scellée de `mesure-durees-banc-mr2-v1.py` (durées unitaires mesurées sur la graine publique de
développement r = 0, juge simplifié) et les comptes par étape de la pièce des règles v1 (`regles-banc-calibration-mr2-v1.md`) ;
prix et durées de la machine du pilote lus au verdict v2 (`e64458e8…`, « Dépense rapprochée », « Pour les cribles »).
Usage : `python3 -I -B calcul-devis-banc-mr2-v4.py MESURE.json SORTIE.json` (refuse d'écraser).
"""
import hashlib
import json
import math
import os
import sys

# --- machine du pilote (verdict v2) ------------------------------------------------------------------------------------
PRIX_PILOTE = 0.052222          # USD/h, « 1,5706 h à 0,052222 USD/h »
DEBUT_MACHINE, DEBUT_PASSE = "11:26:57", "12:14:34"  # création ; début du manifeste
FIN_PASSE, DESTRUCTION = "12:59:07", "13:01:11"
GENERER_4_MONDES_S = 882        # rapport du développeur v68 §6 : 4 mondes de développement vérifiés en 882 s
PRIX_OFFRE, PRIX_RELU = 0.15, 0.17  # bornes de l'offre (procédure du pilote, recopiées du devis v3 §4)
PLAFOND = 3.0                   # USD, GO-2026-11-17-05
MARGE_MINUTERIE = 1.15

# --- facteurs du pire (écrits d'avance, devis v4 §4) ---------------------------------------------------------------------
F_JUGE = 2.0      # juge de la course contre juge simplifié (non mesuré ; garde de durée à l'essai à blanc)
F_SIMU = 1.1      # générations simulées : le jugement n'y pèse qu'une petite part (regroupement surtout)
F_LOURD = 1.25    # mondes de 10 composantes contre 8 au monde mesuré
F_MACHINE = 1.5   # machine louée plus lente que ce conteneur
EFFICACITE = 0.8  # barrières entre étapes, mondes inégaux
RHO_ATT, RHO_PIRE = 0.5, 0.6
REP_M7 = 20       # répétitions du jeu planté (24 mondes × 20 = 12 mondes × 40 de la conception)


def s_de(h):
    a, b, c = (int(x) for x in h.split(":"))
    return 3600 * a + 60 * b + c


def main(mesure, sortie):
    if os.path.exists(sortie):
        sys.exit("refus : sortie existante")
    m = json.load(open(mesure, encoding="utf-8"))
    u = m["mesures"]
    J = {k: v["mediane_s"] for k, v in u["jugement_juge_simplifie"].items()}

    def c(n, k):
        """Durée d'un jugement (s) : mesurée à n = 200, 400, 800 ; interpolée linéairement à 300 et 600."""
        if n in (200, 400, 800):
            return J[f"n={n}|archive={k}"]
        a, b = (200, 400) if n == 300 else (400, 800)
        return J[f"n={a}|archive={k}"] + (J[f"n={b}|archive={k}"] - J[f"n={a}|archive={k}"]) * (n - a) / (b - a)

    t = u["tirages"]
    gen_conf = next(x for x in t if x["conforme"])
    ref = next(x for x in t if not x["conforme"])
    t_conf = gen_conf["generation_s"] + gen_conf["verification_s"]
    t_refus = ref["generation_s"] + ref["verification_s"]
    d_reg = u["regroupement_24_cartes_2000_instances_s"] - u["regroupement_24_cartes_1500_instances_s"]
    g1_400 = u["course_1_generation_n400_s"] + d_reg
    g1_800 = u["course_1_generation_n800_s"] + d_reg
    gk_400 = (u["course_3_generations_n400_s"] - u["course_1_generation_n400_s"]) / 2 + d_reg
    g2_800 = gk_400 + 24 * (c(800, 8) - c(400, 8))
    g3_800 = gk_400 + 24 * (c(800, 17) - c(400, 17))
    grille = (200, 300, 400, 600, 800)

    def par_monde(cas):
        pire = cas == "pire"
        n = 800 if pire else 400
        fj = F_JUGE if pire else 1.0
        fs = F_SIMU if pire else 1.0
        rho = RHO_PIRE if pire else RHO_ATT
        refus_attendus = sum(rho ** k for k in range(1, 8))
        s0 = t_conf + refus_attendus * (t_conf if pire else t_refus)
        s1 = 12 * (0.05 + u["attribution_une_loi_s"])
        s2 = 9 * ((3.0 if pire else 1.0) + u["attribution_une_loi_s"])
        s3 = (g1_400 + gk_400) * fs + (30.0 if pire else 11.0) + 2 * 200 * sum(c(x, 8) for x in grille) * fj
        s4 = 6 * 200 * c(n, 8) * fj
        g1, g2, g3 = (g1_800, g2_800, g3_800) if pire else (g1_400, gk_400, gk_400)
        s5 = (g1 + g2 + g3) * fs + 3 * u["enveloppe_archive_17_s"]
        s6 = 8 * g1 * fs
        comp = 3 if pire else 1
        m1 = 200 * comp * (c(n, 17) + c(n, 1)) * fj + 2 * comp
        lois = (15, 21, 21) if not pire else (19, 25, 25)
        m7 = REP_M7 * (lois[0] * c(n, 1) + lois[1] * c(n, 8) + lois[2] * c(n, 17)) * fj + 3 * 10.0
        autres = 5.0 + 10.0
        etapes = {"S0_tirage_verification": s0, "S1_f": s1, "S2_fusion": s2, "S3_n": s3, "S4_forme": s4, "S5_tau": s5,
                  "S6_regle": s6, "M1_surdite": m1, "M7_valeurs_banc": m7, "M2_M4_M5_M6": autres}
        if pire:
            etapes = {k: v * F_LOURD for k, v in etapes.items()}
        return {k: round(v, 1) for k, v in etapes.items()}

    surcharge_att_h = ((s_de(DEBUT_PASSE) - s_de(DEBUT_MACHINE)) - GENERER_4_MONDES_S + (s_de(DESTRUCTION) - s_de(FIN_PASSE))) / 3600
    surcharge_pire_h = 0.5 + 1.0 + 0.5
    res = {"unitaires": {"jugement_s": J, "tirage_conforme_s": round(t_conf, 1), "tirage_refuse_C6_s": round(t_refus, 1),
                         "generation_1_n400_s": round(g1_400, 1), "generation_1_n800_s": round(g1_800, 1),
                         "generation_2_ou_3_n400_s": round(gk_400, 1), "generation_2_n800_s": round(g2_800, 1),
                         "generation_3_n800_s": round(g3_800, 1)},
           "surcharge_machine_h": {"attendu": round(surcharge_att_h, 3), "pire": surcharge_pire_h},
           "facteurs_pire": {"juge": F_JUGE, "simulation": F_SIMU, "monde_lourd": F_LOURD, "machine": F_MACHINE,
                             "efficacite": EFFICACITE, "rho": [RHO_ATT, RHO_PIRE], "repetitions_M7": REP_M7},
           "par_monde_s": {}, "total": {}}
    for cas in ("attendu", "pire"):
        e = par_monde(cas)
        tot_monde = sum(e.values())
        calcul_h = 24 * tot_monde / 3600 * (F_MACHINE if cas == "pire" else 1.0)
        res["par_monde_s"][cas] = dict(e, total=round(tot_monde, 1))
        res["total"][cas] = {"calcul_processus_h": round(calcul_h, 2), "par_processus": {}}
        for P in (4, 6, 8):
            duree = calcul_h / (P * EFFICACITE) + (surcharge_att_h if cas == "attendu" else surcharge_pire_h)
            ligne = {"duree_h": round(duree, 2)}
            if cas == "attendu":
                ligne["cout_prix_pilote_usd"] = round(duree * PRIX_PILOTE, 3)
                ligne["cout_prix_offre_max_usd"] = round(duree * PRIX_OFFRE, 3)
            else:
                minuterie = math.ceil(duree * MARGE_MINUTERIE)
                prix_max = min(PRIX_RELU, math.floor(PLAFOND / minuterie * 1000) / 1000)
                ligne.update(minuterie_h=minuterie, prix_relu_max_usd_h=prix_max,
                             pire_usd=round(minuterie * prix_max, 3), sous_3_usd=minuterie * prix_max <= PLAFOND)
            res["total"][cas]["par_processus"][str(P)] = ligne
    sortie_obj = {"version": "calcul-devis-banc-mr2-v4", "mesure_sha256": hashlib.sha256(open(mesure, "rb").read()).hexdigest(),
                  "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(), "resultat": res}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(sortie_obj, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
