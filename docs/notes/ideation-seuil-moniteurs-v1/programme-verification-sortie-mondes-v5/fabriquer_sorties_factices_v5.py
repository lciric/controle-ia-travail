#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fabrique la sortie factice saine de l'auteur des mondes plantés — v5.

v5 (contrôle par l'aire, arbitrage a8f8acfa…) : chaque famille porte trois décalages de
saboteur qui réalisent, sous la lecture retenue (écarts types de la loi honnête de la
tranche), les aires 0,69, 0,80 et 0,95. Ils sont calculés ICI, par un code indépendant du
moteur du programme de vérification :
- formes fermées pour la loi normale, la loi de Laplace et les mélanges de normales ;
- somme finie pour la loi arrondie ;
- dichotomie pour inverser l'aire.
Pour que les lois soient calculables en forme fermée, deux lois factices changent : B devient
une Laplace(0, 1), et K (à l'écart) un mélange de normales d'échelles différentes. La grille
de G passe à 0,001, pour que l'aire, fonction en escalier sur un réseau, approche les aires
dites à mieux que 0,001.
Option `--unite-brute` : la sortie factice d'essai dont la famille A, de loi normale(0, 2),
porte ses décalages en unité brute ; le contrôle doit y rendre l'issue (b).

v4 : le décalage de la dérive de F, dans `valeurs_de_plus` de T09, est cohérent. Il porte le
taux de 1 % à 3 % sous la loi de la tranche de F à n = 299 (normale factice, mu 0.25,
sigma 1). Il est calculé ici par programme (bibliothèque standard, `statistics.NormalDist`) :
pour une loi normale, et pour tout décalage exprimé en écarts types, δ = z(0,99) − z(0,97),
quels que soient mu et sigma. Il est écrit à quatre décimales. Le contrôle a posteriori se
fait par `verifier_decalage_factice_v4.py`, sur le fichier produit.

v3 : `valeurs_de_plus` de T09 porte une clé de décalage de la dérive de F (règle de
lecture de la mère, 11:00Z) et une clé de couverture, toutes deux factices ; la famille F
a une tranche à n = 299, celle de T09 (sa deuxième tranche, de loi factice distincte).

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
from statistics import NormalDist

# Loi factice de la tranche de F à n = 299, et décalage (en écarts types) qui triple un taux de 1 %.
MU_TRANCHE_299, SIGMA_TRANCHE_299 = "0.25", "1.0"
_LOI_299 = NormalDist(float(MU_TRANCHE_299), float(SIGMA_TRANCHE_299))
_SEUIL_A_1_POUR_CENT = _LOI_299.inv_cdf(0.99)
_SEUIL_DECALE_A_3_POUR_CENT = _LOI_299.inv_cdf(0.97)
DECALAGE_DE_F = "%.4f" % ((_SEUIL_A_1_POUR_CENT - _SEUIL_DECALE_A_3_POUR_CENT) / _LOI_299.stdev)

# ---- v5 : aires du saboteur, en formes fermées, indépendamment du programme vérifié ----
import math

AIRES_VISEES = (0.69, 0.80, 0.95)
_Z = NormalDist()


def _inverser(fonction, cible, lo=0.0, hi=50.0):
    for _ in range(60):
        mi = 0.5 * (lo + hi)
        if fonction(mi) < cible:
            lo = mi
        else:
            hi = mi
    return 0.5 * (lo + hi)


def aire_normale(sigma):
    return lambda d: _Z.cdf(d / (sigma * math.sqrt(2.0)))


def aire_laplace(b):
    # X − Y, X et Y de Laplace(0, b) indépendantes : P(X − Y < d) = 1 − ½ e^(−d/b) (1 + d/(2b)), d ≥ 0.
    return lambda d: 1.0 - 0.5 * math.exp(-d / b) * (1.0 + d / (2.0 * b))


def aire_melange_de_normales(poids, mus, sigmas):
    def aire(d):
        return sum(wi * wj * _Z.cdf((d + mi - mj) / math.sqrt(si * si + sj * sj))
                   for wi, mi, si in zip(poids, mus, sigmas) for wj, mj, sj in zip(poids, mus, sigmas))
    return aire


def ecart_type_melange(poids, mus, sigmas):
    m = sum(w * mu for w, mu in zip(poids, mus))
    return math.sqrt(sum(w * (s * s + mu * mu) for w, mu, s in zip(poids, mus, sigmas)) - m * m)


def reseau_arrondi_normal(pas, mu=0.0, sigma=1.0):
    """Masses de la normale arrondie au multiple le plus proche de `pas`."""
    kmin, kmax = int(math.floor((mu - 9 * sigma) / pas)), int(math.ceil((mu + 9 * sigma) / pas))
    loi = NormalDist(mu, sigma)
    masses = [loi.cdf((k + 0.5) * pas) - loi.cdf((k - 0.5) * pas) for k in range(kmin, kmax + 1)]
    s = sum(masses)
    return kmin, [m / s for m in masses]


def aire_reseau(pas, kmin, masses):
    cumul, s = [], 0.0
    for m in masses:
        s += m
        cumul.append(s)

    def aire(d):
        v0 = d / pas
        total = 0.0
        for i, m in enumerate(masses):
            v = i + v0
            j = round(v)
            if abs(v - j) < 1e-9:
                inf = cumul[j - 1] if 1 <= j <= len(masses) else (0.0 if j < 1 else 1.0)
                eq = masses[j] if 0 <= j < len(masses) else 0.0
                total += m * (inf + 0.5 * eq)
            else:
                f = math.floor(v)
                total += m * (cumul[f] if 0 <= f < len(masses) else (0.0 if f < 0 else 1.0))
        return total
    return aire


def decalages_ecarts_types(aire, ecart_type, reseau_pas=None):
    """Les trois décalages, en écarts types, qui réalisent les aires visées. Sur un réseau, le
    décalage brut est pris au milieu d'un palier (stable à l'arrondi à quatre décimales)."""
    sortie = []
    for cible in AIRES_VISEES:
        brut = _inverser(aire, cible)
        if reseau_pas is not None:
            k = math.floor(brut / reseau_pas)
            candidats = [(j + 0.5) * reseau_pas for j in (k - 1, k, k + 1)]
            brut = min(candidats, key=lambda x: abs(aire(x) - cible))
        sortie.append("%.4f" % (brut / ecart_type))
    return sortie


DEC_NORMALE = decalages_ecarts_types(aire_normale(1.0), 1.0)
DEC_LAPLACE = decalages_ecarts_types(aire_laplace(1.0), math.sqrt(2.0))
_MEL = ([0.95, 0.05], [0.0, 1.0], [1.0, 1.0])
DEC_MELANGE = decalages_ecarts_types(aire_melange_de_normales(*_MEL), ecart_type_melange(*_MEL))
_MEL_K = ([0.9, 0.1], [0.0, 0.0], [1.0, 3.0])
DEC_MELANGE_K = decalages_ecarts_types(aire_melange_de_normales(*_MEL_K), ecart_type_melange(*_MEL_K))
PAS_DE_G = "0.001"
_KMIN_G, _MASSES_G = reseau_arrondi_normal(float(PAS_DE_G))
_ET_G = math.sqrt(sum(m * ((_KMIN_G + i) * float(PAS_DE_G)) ** 2 for i, m in enumerate(_MASSES_G))
                  - sum(m * (_KMIN_G + i) * float(PAS_DE_G) for i, m in enumerate(_MASSES_G)) ** 2)
DEC_G = decalages_ecarts_types(aire_reseau(float(PAS_DE_G), _KMIN_G, _MASSES_G), _ET_G, reseau_pas=float(PAS_DE_G))
SIGMA_UNITE_BRUTE = 2.0
DEC_UNITE_BRUTE = ["%.4f" % _inverser(aire_normale(SIGMA_UNITE_BRUTE), c) for c in AIRES_VISEES]


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
        if tid == "T09":
            t["valeurs_de_plus"] = {"couverture_qui_reste": Brut(VALEUR), "decalage_en_ecarts_types": Brut(DECALAGE_DE_F)}
        elif tid in AVEC_VALEURS_DE_PLUS:
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


def famille(fid, nom, casse, loi, jumeau, imposee=True, p_echec=None, tr=None, decalages=None):
    decalages = decalages or DEC_NORMALE
    return {
        "id": fid, "nom": nom, "imposee": imposee, "hors_table": False,
        "suppositions_cassees": list(casse), "p_echec": p_echec,
        "tranches": tr if tr is not None else tranches(loi),
        "saboteur": {"forme": {"type": "decalage", "parametres": {"loi": loi, "delta_en_ecarts_types": Brut(decalages[1])}},
                     "decalages": [Brut(x) for x in decalages]},
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
                {"type": "laplace", "parametres": {"mu": Brut("0.0"), "echelle": Brut("1.0")}},
                {"echelle_normale": Brut("1.0")}, decalages=DEC_LAPLACE),
        famille("C", "honnetes qui echouent decales", [S_ECHEC], melange("0.05"), {"decalage_des_echecs": Brut("0.0")},
                p_echec=Brut("0.0500"), decalages=DEC_MELANGE),
        famille("D", "tranches inegales", [S_TRANCHES], normale(), {"meme_moyenne": True}, tr=d_tranches),
        famille("E", "pas correles", [S_PAS],
                {"type": "somme_de_pas", "parametres": {"nombre_de_pas": 10, "loi_du_pas": normale(),
                                                         "correlation": Brut("0.3"), "structure": "ar1"}},
                {"correlation": Brut("0.0")}),
        famille("F", "derive d'usage", [S_DERIVE, S_ECH], normale(), {"decalage_d_usage": Brut("0.0")},
                tr=[{"id": "t1", "n_calibration": [200, 300, 400], "loi_honnete": normale()},
                    {"id": "t2", "n_calibration": [299], "loi_honnete": normale(MU_TRANCHE_299, SIGMA_TRANCHE_299)},
                    {"id": "t3", "n_calibration": [200, 300, 400], "loi_honnete": normale()}]),
        famille("G", "valeurs repetees", [S_CONTINUS],
                {"type": "arrondi", "parametres": {"loi": normale(), "pas_de_grille": Brut(PAS_DE_G)}},
                {"pas_de_grille": Brut("0.0")}, decalages=DEC_G),
        famille("H", "grappes de taches", [S_ECH],
                {"type": "effet_de_famille_plus_bruit", "parametres": {"correlation_intra": Brut("0.2"),
                                                                       "tailles_de_famille": [100, 100, 100]}},
                {"correlation_intra": Brut("0.0")}),
        famille("I", "echec rare extreme", [S_ECHEC], melange("0.05"), {"decalage_des_echecs": Brut("0.0")},
                p_echec=Brut("0.0500"), decalages=DEC_MELANGE),
    ]


NOM_A_L_ECART = "famille d'essai retiree du regard"


def a_l_ecart():
    loi_k = {"type": "melange", "parametres": {"poids": [Brut("0.9"), Brut("0.1")],
                                               "composantes": [normale("0.0", "1.0"), normale("0.0", "3.0")]}}
    f = famille("K", NOM_A_L_ECART, [S_QUEUE], loi_k, {"poids_de_la_queue": Brut("0.0")}, imposee=False,
                decalages=DEC_MELANGE_K)
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


def sortie_unite_brute():
    """Sortie factice d'ESSAI : la famille A, de loi normale(0, 2) dans ses trois tranches, porte
    des décalages en unité brute (le nombre ajouté tel quel au score). Le contrôle par l'aire
    doit y rendre « unité brute constatée »."""
    d = sortie_saine()
    a = next(f for f in d["familles"] if f["id"] == "A")
    loi = normale("0.0", "%.1f" % SIGMA_UNITE_BRUTE)
    for tr in a["tranches"]:
        tr["loi_honnete"] = loi
    a["saboteur"] = {"forme": {"type": "decalage", "parametres": {"loi": loi, "delta_en_ecarts_types": Brut(DEC_UNITE_BRUTE[1])}},
                     "decalages": [Brut(x) for x in DEC_UNITE_BRUTE]}
    d["remarques"] = ["Sortie factice d'essai, en unité brute pour la famille A : aucune valeur, aucune sorte ni aucune issue n'est vraie."]
    return d


def principal(argv):
    unite_brute = bool(argv) and argv[0] == "--unite-brute"
    if unite_brute:
        argv = argv[1:]
    if len(argv) != 1:
        print("usage : [--unite-brute] CHEMIN_DE_SORTIE", file=sys.stderr)
        return 3
    chemin = Path(argv[0])
    if chemin.exists():
        print("erreur : le fichier existe déjà : on n'écrase jamais", file=sys.stderr)
        return 3
    with open(chemin, "x", encoding="utf-8") as fh:
        fh.write(serialiser(sortie_unite_brute() if unite_brute else sortie_saine()) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
