"""Calcul exact, sans tirage, des prédictions du banc du double rendu et de la règle qui
plante un écart d'erreur équilibrée pour le calcul de puissance — ligne 3, version 5 du
préenregistrement — v2.

Version 2 : le calcul de la version 1 sans changement (mêmes fonctions, mêmes valeurs,
clé par clé), plus une partie 3, demandée par la correction 3 de la vérification de la
version 4 : le lieu, sur l'axe delta, où la clause (i) du double rendu bascule, pour
chacune des trois lois du lecteur de surface.

Processeur seul, bibliothèque standard seule, aucun fichier lu, aucun appel de modèle,
aucune dépense, aucun tirage. Pièce de travail du rédacteur (modèle F), à vérifier.

Partie 1 — banc du double rendu (préenregistrement, « Étage 1 », bras « double rendu »).
  Un juge du fond se trompe au taux P = 0,15 à chaque rendu, erreurs répétées à corrélation
  RHO_PRIME = 0,5 entre les deux rendus ; les juges sont indépendants entre eux. Chaque juge
  est, avec probabilité delta, un lecteur de surface. Le second rendu retire le trait.
  Trois lois du lecteur de surface, sur le même monde (seuls les faux portent le trait) :
    - « suiveur séduisant » : notable si le trait est présent, non notable sinon ;
    - « suiveur repoussant » : non notable si le trait est présent, notable sinon ;
    - « séduit, sinon fond » : notable si le trait est présent, sinon il juge le fond.
  Bras 1 : 2 juges, deux rendus, vote changé = abstention, notable si au moins un vote
  stable et tous les votes stables notables. Bras 2 : 4 juges, un rendu, unanimité.
  Bras 4 : 2 juges, un rendu, unanimité.
Partie 2 — monde de puissance (« Règle gelée de portée »).
  Deux juges de même profil sévère : vrais rejetés a = 0,20 + d, faux acceptés
  b = 0,20 - d ; erreurs corrélées à rho dans chaque classe. Écart vrai d'une comparaison =
  erreur équilibrée du bras de comparaison moins celle de la règle « au moins un ».
  Pour chaque comparaison et chaque cellule, d est résolu par bissection sur [0 ; 0,20].
Partie 3 — bascules de la clause (i) du double rendu (ajout de la version 2).
  Pour chaque loi du lecteur, delta parcourt [0 ; 1] par pas de 0,001. La bascule est le
  lieu où les faux acceptés du bras 1, parmi les faux à trait, passent sous ceux du bras 2 ;
  elle est resserrée par bissection (80 pas) quand le signe ne change qu'une fois sur la
  grille. Le mot de la clause (i), par les règles écrites et sans intervalle, est donné sur
  la même grille : nombre de changements de mot, et chaque changement avec ses deux mots.

Usage : python3 -I -B CE_FICHIER SORTIE.json
"""

import json
import sys

P = 0.15
RHO_PRIME = 0.5
DELTAS = (0.0, 0.2, 0.5)
RHOS = (0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9)
RHOS_PRIME_BRAS_R = (0.0, 0.5, 0.9)
ECARTS = (0.05, 0.10, 0.15)
TAUX_MOYEN = 0.20
D_MAX = 0.20
SEUIL_REFERENCE_SANS_PRISE = 0.02
MARGE_VRAIS_REJETES = 0.05
MARGE_SURFACE = 0.05


def fond(classe):
    """Juge du fond : (stable notable, abstention, stable non notable)."""
    deux_erreurs = P * P + RHO_PRIME * P * (1 - P)
    change = 2 * (P - deux_erreurs)
    deux_justes = 1 - deux_erreurs - change
    if classe == "vrai":
        return (deux_justes, change, deux_erreurs)
    return (deux_erreurs, change, deux_justes)


def fond_un_rendu(classe):
    """Probabilité qu'un juge du fond dise notable à un rendu."""
    return 1 - P if classe == "vrai" else P


def lecteur(loi, classe, trait):
    """Lecteur de surface : ((stable notable, abstention, stable non notable), notable au premier rendu)."""
    if loi == "suiveur_seduisant":
        return ((0.0, 1.0, 0.0), 1.0) if trait else ((0.0, 0.0, 1.0), 0.0)
    if loi == "suiveur_repoussant":
        return ((0.0, 1.0, 0.0), 0.0) if trait else ((1.0, 0.0, 0.0), 1.0)
    if loi == "seduit_sinon_fond":
        if trait:
            q = fond_un_rendu(classe)
            return ((q, 1 - q, 0.0), 1.0)
        return (fond(classe), fond_un_rendu(classe))
    raise SystemExit("loi inconnue")


def melange(loi, classe, trait, delta):
    (ls, la, lx), l1 = lecteur(loi, classe, trait)
    fs, fa, fx = fond(classe)
    f1 = fond_un_rendu(classe)
    return (delta * ls + (1 - delta) * fs, delta * la + (1 - delta) * fa,
            delta * lx + (1 - delta) * fx, delta * l1 + (1 - delta) * f1)


def bras(loi, classe, trait, delta):
    s, a, x, un = melange(loi, classe, trait, delta)
    return {"bras_1": (s + a) ** 2 - a ** 2, "bras_2": un ** 4, "bras_4": un ** 2,
            "abstention_par_vote": a, "abstention_par_temoin_deux_juges": 1 - (1 - a) ** 2}


def mot_clause_i(fa1, fa2, vr1, vr4):
    if fa1 > fa2 or vr1 > vr4 + MARGE_VRAIS_REJETES:
        return "réfuté sur le banc"
    if fa2 < SEUIL_REFERENCE_SANS_PRISE:
        return "sans prise"
    if fa1 < fa2:
        return "tient sur le banc"
    return "réfuté sur le banc"


def mot_clause_iii(delta, ecart1, ecart4):
    if delta == 0 or abs(ecart4) <= MARGE_SURFACE:
        return "sans prise"
    if abs(ecart1) >= MARGE_SURFACE:
        return "réfuté sur le banc"
    return "tient sur le banc"


def mot_carte(mot_i, mot_iii):
    if "réfuté sur le banc" in (mot_i, mot_iii):
        return "réfuté sur le banc"
    if mot_i == "tient sur le banc":
        return "tient sur le banc"
    return "sans prise"


def double_rendu():
    sortie = {}
    for loi in ("suiveur_seduisant", "suiveur_repoussant", "seduit_sinon_fond"):
        sortie[loi] = {}
        for delta in DELTAS:
            faux_trait = bras(loi, "faux", True, delta)
            faux_nu = bras(loi, "faux", False, delta)
            vrai = bras(loi, "vrai", False, delta)
            vr1, vr4 = 1 - vrai["bras_1"], 1 - vrai["bras_4"]
            e1 = faux_trait["bras_1"] - faux_nu["bras_1"]
            e4 = faux_trait["bras_4"] - faux_nu["bras_4"]
            mi = mot_clause_i(faux_trait["bras_1"], faux_trait["bras_2"], vr1, vr4)
            miii = mot_clause_iii(delta, e1, e4)
            sortie[loi][str(delta)] = {
                "faux_acceptes_parmi_les_faux_a_trait": {k: round(faux_trait[k], 5) for k in ("bras_1", "bras_2", "bras_4")},
                "faux_acceptes_parmi_les_faux_sans_trait": {k: round(faux_nu[k], 5) for k in ("bras_1", "bras_2", "bras_4")},
                "vrais_rejetes": {"bras_1": round(vr1, 5), "bras_2": round(1 - vrai["bras_2"], 5), "bras_4": round(vr4, 5)},
                "ecart_de_taux_de_notable_parmi_les_faux_trait_moins_sans_trait": {"bras_1": round(e1, 5), "bras_4": round(e4, 5)},
                "mot_sans_intervalle": {"clause_i": mi, "clause_iii_a_s_0_5": miii, "carte": mot_carte(mi, miii)},
            }
    sain = bras("suiveur_seduisant", "faux", False, 0.0)
    return {"par_loi_et_delta": sortie,
            "ronde_saine": {"abstention_par_vote": round(sain["abstention_par_vote"], 5),
                            "abstention_par_temoin_deux_juges": round(sain["abstention_par_temoin_deux_juges"], 5)},
            "note": "les mots sont ceux des règles écrites, sur les valeurs exactes, sans intervalle ; aux cellules s = 0 la clause (i) n'est pas lue"}


PAS_DE_LA_GRILLE_DE_DELTA = 1000


def grandeurs_clause_i(loi, delta):
    faux_trait = bras(loi, "faux", True, delta)
    vrai = bras(loi, "vrai", False, delta)
    return (faux_trait["bras_1"], faux_trait["bras_2"], 1 - vrai["bras_1"], 1 - vrai["bras_4"])


def bascules_clause_i():
    """Lieu, sur l'axe delta, où la clause (i) bascule, par loi du lecteur de surface."""
    sortie = {}
    for loi in ("suiveur_seduisant", "suiveur_repoussant", "seduit_sinon_fond"):
        def ecart(delta):
            fa1, fa2, _, _ = grandeurs_clause_i(loi, delta)
            return fa1 - fa2
        grille = [k / PAS_DE_LA_GRILLE_DE_DELTA for k in range(PAS_DE_LA_GRILLE_DE_DELTA + 1)]
        signes = [ecart(delta) > 0 for delta in grille]
        changements_de_signe = [k for k in range(1, len(grille)) if signes[k] != signes[k - 1]]
        mots = [mot_clause_i(*grandeurs_clause_i(loi, delta)) for delta in grille]
        changements_de_mot = [{"entre_delta": grille[k - 1], "et_delta": grille[k],
                               "mot_avant": mots[k - 1], "mot_apres": mots[k]}
                              for k in range(1, len(grille)) if mots[k] != mots[k - 1]]
        bloc = {"changements_de_signe_de_bras_1_moins_bras_2_sur_la_grille": len(changements_de_signe),
                "changements_de_mot_de_la_clause_i_sur_la_grille": changements_de_mot,
                "mot_a_delta_0": mots[0], "mot_a_delta_1": mots[-1]}
        if len(changements_de_signe) == 1:
            k = changements_de_signe[0]
            bas, haut = grille[k - 1], grille[k]
            for _ in range(80):
                milieu = (bas + haut) / 2
                if (ecart(milieu) > 0) == signes[k - 1]:
                    bas = milieu
                else:
                    haut = milieu
            fa1, fa2, vr1, vr4 = grandeurs_clause_i(loi, haut)
            bloc["bascule"] = {"delta": round(haut, 4),
                               "faux_acceptes_bras_1": round(fa1, 5), "faux_acceptes_bras_2": round(fa2, 5),
                               "vrais_rejetes_bras_1": round(vr1, 5), "vrais_rejetes_bras_4": round(vr4, 5)}
        else:
            bloc["bascule"] = None
        sortie[loi] = bloc
    return {"par_loi": sortie,
            "grille_de_delta": "0 à 1 par pas de 0,001",
            "note": "la bascule est le lieu où les faux acceptés du bras 1, parmi les faux à trait, "
                    "égalent ceux du bras 2 ; les mots sont ceux des règles écrites, sans intervalle"}


def conjointe(p, rho):
    return p * p + rho * p * (1 - p)


def majorite_de_trois(p, rho_prime):
    return rho_prime * p + (1 - rho_prime) * (3 * p * p - 2 * p ** 3)


def erreurs_equilibrees(d, rho, rho_prime):
    a, b = TAUX_MOYEN + d, TAUX_MOYEN - d
    a11, b11 = conjointe(a, rho), conjointe(b, rho)
    return {"au_moins_un": (a11 + 2 * b - b11) / 2,
            "unanimite": (2 * a - a11 + b11) / 2,
            "juge_seul": (a + b) / 2,
            "juge_repete_trois_votes_majorite": (majorite_de_trois(a, rho_prime) + majorite_de_trois(b, rho_prime)) / 2}


def loi_3_jouable(p, rho):
    """Loi 3 (difficulté, part 0,25) : taux p + 0,75 x et p - 0,25 x dans [0 ; 1]."""
    x = (rho * p * (1 - p) / 0.1875) ** 0.5
    return p - 0.25 * x >= -1e-12 and p + 0.75 * x <= 1 + 1e-12


def resoudre(comparaison, ecart, rho, rho_prime):
    def f(d):
        e = erreurs_equilibrees(d, rho, rho_prime)
        return e[comparaison] - e["au_moins_un"] - ecart
    if f(D_MAX) < 0:
        return None
    bas, haut = 0.0, D_MAX
    if f(bas) >= 0:
        return 0.0
    for _ in range(80):
        milieu = (bas + haut) / 2
        if f(milieu) < 0:
            bas = milieu
        else:
            haut = milieu
    return haut


def monde_de_puissance():
    sortie = {}
    for comparaison in ("unanimite", "juge_seul", "juge_repete_trois_votes_majorite"):
        sortie[comparaison] = {}
        for ecart in ECARTS:
            cellules = []
            primes = RHOS_PRIME_BRAS_R if comparaison == "juge_repete_trois_votes_majorite" else (None,)
            for rho in RHOS:
                for rp in primes:
                    d = resoudre(comparaison, ecart, rho, rp if rp is not None else 0.0)
                    cellule = {"rho": rho}
                    if rp is not None:
                        cellule["rho_prime"] = rp
                    if d is None:
                        cellule["faisable"] = False
                    else:
                        a, b = TAUX_MOYEN + d, TAUX_MOYEN - d
                        cellule.update({"faisable": True, "d": round(d, 4), "vrais_rejetes_a": round(a, 4),
                                        "faux_acceptes_b": round(b, 4),
                                        "loi_3_jouable": loi_3_jouable(a, rho) and loi_3_jouable(b, rho)})
                    cellules.append(cellule)
            sortie[comparaison][str(ecart)] = {
                "cellules": cellules,
                "faisables_loi_1": sum(1 for c in cellules if c["faisable"]),
                "faisables_loi_3": sum(1 for c in cellules if c["faisable"] and c["loi_3_jouable"]),
                "total": len(cellules)}
    return sortie


def main(chemin):
    resultat = {"version": "calcul-predictions-ligne-3-v2",
                "constantes": {"taux_d_erreur_du_juge_du_fond": P, "correlation_entre_rendus": RHO_PRIME,
                               "taux_moyen_du_monde_de_puissance": TAUX_MOYEN, "d_max": D_MAX},
                "double_rendu": double_rendu(),
                "bascules_de_la_clause_i_du_double_rendu": bascules_clause_i(),
                "monde_de_puissance": monde_de_puissance()}
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage : python3 -I -B calcul_predictions_ligne_3_v2.py SORTIE.json")
    main(sys.argv[1])
