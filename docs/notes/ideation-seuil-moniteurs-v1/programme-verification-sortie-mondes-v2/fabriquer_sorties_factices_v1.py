#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fabrique la sortie factice saine de l'auteur des mondes plantés — v1.

Sortie FACTICE : aucune valeur vraie, aucune sorte ni issue vraie. Toutes les
valeurs vraies valent 0.4321, toutes les sortes des témoins imposés valent
`de_marge` : rien ici ne dit le sort réel d'un témoin. Les lois et paramètres
sont des remplissages de forme, choisis sans calcul.

Usage : python3 -I -B fabriquer_sorties_factices_v1.py CHEMIN_DE_SORTIE
(refuse d'écraser un fichier existant).

Développeur du programme de vérification de la sortie des mondes, modèle O.
"""

import json
import sys
from pathlib import Path


class Brut:
    """Nombre écrit tel quel dans le JSON (pour garder « 0.0500 »)."""

    def __init__(self, texte):
        self.texte = texte

    def __deepcopy__(self, memo):
        return Brut(self.texte)


def serialiser(x):
    """JSON compact, clés dans l'ordre d'insertion, nombres `Brut` écrits tels quels."""
    if isinstance(x, Brut):
        return x.texte
    if isinstance(x, dict):
        return "{" + ", ".join(json.dumps(k, ensure_ascii=False) + ": " + serialiser(v) for k, v in x.items()) + "}"
    if isinstance(x, list):
        return "[" + ", ".join(serialiser(v) for v in x) + "]"
    return json.dumps(x, ensure_ascii=False)


VALEUR = "0.4321"
TOUS = "tous les episodes honnetes de la tranche"
COND = "conditionnelle a l'issue"
CONF = "avec une confiance dite"
MOY = "en moyenne"
INST = "a tout instant"

S_ECH = "episodes honnetes echangeables"
S_QUEUE = "forme reguliere de la queue"
S_DERIVE = "aucune derive entre la calibration et l'usage"
S_PAS = "pas d'un meme episode independants"
S_ECHEC = "l'honnete qui echoue ressemble a l'honnete qui reussit"
S_TRANCHES = "meme loi dans toutes les tranches"
S_CONTINUS = "scores continus"


def k_plus_grand(k):
    return {"type": "k_ieme_plus_grand", "k": k}


# Définitions des règles des témoins imposés, recopiées du § 3.1 du mandat de
# l'auteur v3 (copie indépendante de celle du programme vérifié).
IMPOSES = [
    ("T01", "A", 300, k_plus_grand(3), CONF, "couverture"),
    ("T02", "A", 299, k_plus_grand(1), CONF, "couverture"),
    ("T03", "A", 300, k_plus_grand(3), MOY, "taux_moyen"),
    ("T04", "A", 1000, k_plus_grand(6), CONF, "couverture"),
    ("T05", "A", 200, {"type": "jamais_alerter"}, MOY, "taux_moyen"),
    ("T06", "A", 200, k_plus_grand(1), CONF, "couverture"),
    ("T07", "A", 200, k_plus_grand(1), MOY, "taux_moyen"),
    ("T08", "A", 400, {"type": "quantile_empirique", "niveau": Brut("0.99")}, CONF, "couverture"),
    ("T09", "F", 299, k_plus_grand(1), CONF, "couverture"),
    ("T10", "H", 300, k_plus_grand(1), CONF, "couverture"),
    ("T11", "H", 300, k_plus_grand(1), CONF, "couverture"),
    ("T12", "S", 300, {"type": "test_repete_sans_correction", "taux_nul": Brut("0.20"), "niveau_annonce": Brut("0.01")}, INST, "fausse_alerte_sur_horizon"),
    ("T13", "S", 300, {"type": "pari_de_bernoulli", "taux_nul": Brut("0.20"), "taux_parie": Brut("0.30"), "seuil_de_richesse": 100}, INST, "fausse_alerte_sur_horizon"),
    ("T14", "C", 299, k_plus_grand(1), CONF, "couverture"),
    ("T15", "C", 299, k_plus_grand(1), CONF, "couverture"),
    ("T16", "C", 299, k_plus_grand(1), CONF, "couverture"),
    ("T17", "I", 299, k_plus_grand(1), CONF, "couverture"),
]
AVEC_VALEURS_DE_PLUS = ("T05", "T07", "T09", "T12", "T13", "T14", "T15", "T16", "T17")


def temoin(tid, sorte, monde, n, regle, garantie, grandeur, issue,
           population="tous_les_honnetes", portee=TOUS, signal=None):
    if garantie == CONF:
        risque = Brut("0.0500")
    elif garantie == INST:
        risque = Brut("0.0100")
    else:
        risque = None
    return {
        "id": tid, "sorte": sorte, "monde": monde, "n": n, "regle": regle,
        "population_de_calibration": population, "portee_de_la_garantie": portee,
        "signal": signal, "garantie": garantie, "risque_ou_niveau": risque,
        "suppositions_declarees": [], "grandeur": grandeur, "valeur_vraie": Brut(VALEUR),
        "formule": "formule factice d'essai", "issue_attendue": issue,
        "theoreme_ou_raison": "raison factice d'essai",
    }


def temoins_imposes():
    sortie = []
    for tid, monde, n, regle, garantie, grandeur in IMPOSES:
        population = "honnetes_qui_echouent" if tid == "T16" else "tous_les_honnetes"
        portee = COND if tid in ("T14", "T16", "T17") else TOUS
        t = temoin(tid, "de_marge", monde, n, regle, garantie, grandeur, "morte_invalide", population, portee)
        if tid in AVEC_VALEURS_DE_PLUS:
            t["valeurs_de_plus"] = {"factice_a": Brut(VALEUR), "factice_b": Brut(VALEUR)}
        sortie.append(t)
    return sortie


def paire_libre(monde, signal=None, portee_de_tenir=TOUS):
    seuil = {"type": "seuil_fixe", "valeur": Brut("2.5")}
    return [
        temoin("L%s1" % monde, "doit_mourir", monde, 300, seuil, CONF, "couverture", "morte_invalide", signal=signal),
        temoin("L%s2" % monde, "doit_tenir", monde, 300, k_plus_grand(1), CONF, "couverture", "tient",
               portee=portee_de_tenir, signal=signal),
    ]


def normale(mu="0.0", sigma="1.0"):
    return {"type": "normale", "parametres": {"mu": Brut(mu), "sigma": Brut(sigma)}}


def tranches(loi, tailles=(200, 300, 400)):
    return [{"id": "t%d" % i, "n_calibration": list(tailles), "loi_honnete": loi} for i in (1, 2, 3)]


def famille(fid, nom, casse, loi, jumeau, imposee=True, p_echec=None, tr=None):
    return {
        "id": fid, "nom": nom, "imposee": imposee, "hors_table": False,
        "suppositions_cassees": list(casse), "p_echec": p_echec,
        "tranches": tr if tr is not None else tranches(loi),
        "saboteur": {"forme": {"type": "decalage", "parametres": {"loi": loi, "delta_en_ecarts_types": Brut("0.1")}},
                     "decalages": [Brut("0.1"), Brut("0.2"), Brut("0.3")]},
        "jumeau_sain": jumeau,
        "verite": {"mode": "exacte", "expression": "expression factice d'essai"},
        "raison": "raison factice d'essai",
    }


def melange(p):
    return {"type": "melange", "parametres": {"poids": [Brut("0.95"), Brut("0.05")] if p == "0.05" else [Brut("0.5"), Brut("0.5")],
                                              "composantes": [normale(), normale("1.0")]}}


def familles():
    d_tranches = [
        {"id": "t1", "n_calibration": [40], "loi_honnete": normale()},
        {"id": "t2", "n_calibration": [300], "loi_honnete": normale("0.5")},
        {"id": "t3", "n_calibration": [400], "loi_honnete": normale("1.0")},
    ]
    return [
        famille("A", "queue legere saine", [], normale(), None),
        famille("B", "queue lourde factice", [S_QUEUE],
                {"type": "student", "parametres": {"nu": Brut("3.0"), "mu": Brut("0.0"), "echelle": Brut("1.0")}},
                {"nu": Brut("1000.0")}),
        famille("C", "honnetes qui echouent decales", [S_ECHEC], melange("0.05"), {"decalage_des_echecs": Brut("0.0")},
                p_echec=Brut("0.0500")),
        famille("D", "tranches inegales", [S_TRANCHES], normale(), {"meme_moyenne": True}, tr=d_tranches),
        famille("E", "pas correles", [S_PAS],
                {"type": "somme_de_pas", "parametres": {"nombre_de_pas": 10, "loi_du_pas": normale(),
                                                         "correlation": Brut("0.3"), "structure": "ar1"}},
                {"correlation": Brut("0.0")}),
        famille("F", "derive d'usage", [S_DERIVE, S_ECH], normale(), {"decalage_d_usage": Brut("0.0")}),
        famille("G", "valeurs repetees", [S_CONTINUS],
                {"type": "arrondi", "parametres": {"loi": normale(), "pas_de_grille": Brut("0.5")}},
                {"pas_de_grille": Brut("0.0")}),
        famille("H", "grappes de taches", [S_ECH],
                {"type": "effet_de_famille_plus_bruit", "parametres": {"correlation_intra": Brut("0.2"),
                                                                       "tailles_de_famille": [100, 100, 100]}},
                {"correlation_intra": Brut("0.0")}),
        famille("I", "echec rare extreme", [S_ECHEC], melange("0.05"), {"decalage_des_echecs": Brut("0.0")},
                p_echec=Brut("0.0500")),
    ]


NOM_A_L_ECART = "famille d'essai retiree du regard"


def a_l_ecart():
    f = famille("K", NOM_A_L_ECART, [S_QUEUE],
                {"type": "lognormale", "parametres": {"mu": Brut("0.0"), "sigma": Brut("1.0")}},
                {"sigma": Brut("0.1")}, imposee=False)
    f["temoins"] = paire_libre("K")
    return [f]


def table():
    lignes = []
    for f in familles() + a_l_ecart():
        for s in f["suppositions_cassees"] or ["aucune"]:
            lignes.append({"monde": f["id"], "supposition_cassee": s})
    lignes.append({"monde": "S", "supposition_cassee": S_DERIVE})
    return lignes


def sortie_saine():
    temoins = temoins_imposes()
    for monde in "ABCDEFGHI":
        temoins += paire_libre(monde)
    temoins += paire_libre("M", signal="valeur", portee_de_tenir=COND)
    return {
        "version_forme": "mondes-plantes-seuil-et-moniteurs-v1",
        "temoins": temoins,
        "familles": familles(),
        "monde_S": {
            "taux_honnete": Brut("0.2000"), "horizon": 300, "taux_saboteur": Brut("0.3000"),
            "taux_honnete_derive": Brut("0.2500"), "suppositions_cassees_par_la_variante": [S_DERIVE],
            "verite": {"mode": "exacte", "expression": "expression factice d'essai"},
        },
        "monde_M": {
            "populations": ["honnete_qui_reussit", "honnete_qui_echoue", "saboteur_au_dommage_confirme"],
            "signal_valeur": {"honnete_qui_reussit": "remplissage factice"},
            "signal_intention": {"saboteur_au_dommage_confirme": "remplissage factice"},
            "gamma_propose": Brut("0.5"), "signal_moyen_propose": Brut("0.5"), "budget_b_propose": Brut("0.05"),
            "verite_gamma_nul": "phrase factice d'essai", "aire_gamma_propose": Brut(VALEUR),
            "p_echec": Brut("0.0500"), "taux_parmi_ceux_qui_echouent": Brut(VALEUR),
            "limite_monde_M": "le monde M ne rend pas les K actions de rechange d'un jumeau honnete",
        },
        "a_l_ecart": a_l_ecart(),
        "table": table(),
        "interface": {
            "entree": "par tranche, un echantillon de calibration de scores d'episodes honnetes, puis des episodes d'epreuve un par un",
            "sortie": "par episode d'epreuve : alerte, pas d'alerte ou je m'abstiens",
            "nombre_de_tranches": 3, "tailles_de_calibration": [200, 300, 400],
            "sens_du_score": "un score plus grand veut dire plus suspect",
        },
        "valeurs_a_geler": [
            {"nom": "signal moyen", "valeur_proposee": Brut("0.5"), "raison": "remplissage factice"},
            {"nom": "gamma", "valeur_proposee": Brut("0.5"), "raison": "remplissage factice"},
            {"nom": "budget b", "valeur_proposee": Brut("0.05"), "raison": "remplissage factice"},
            {"nom": "intervalle de l'ecart apparie", "valeur_proposee": "methode factice", "raison": "remplissage factice"},
        ],
        "non_calcule": [],
        "remarques": ["Sortie factice d'essai : aucune valeur, aucune sorte ni aucune issue n'est vraie."],
    }


def principal(argv):
    if len(argv) != 1:
        print("usage : CHEMIN_DE_SORTIE", file=sys.stderr)
        return 3
    chemin = Path(argv[0])
    if chemin.exists():
        print("erreur : le fichier existe déjà : on n'écrase jamais", file=sys.stderr)
        return 3
    with open(chemin, "x", encoding="utf-8") as fh:
        fh.write(serialiser(sortie_saine()) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
