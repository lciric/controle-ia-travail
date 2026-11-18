"""Lecture gelée de l'étude des formulations du contraste à témoin apparié — contrôles de validation et règle de choix — v1.

Entrée : le dictionnaire `mondes` du résultat scellé de `simulation_v1.executer` (nom du monde → paramètres, classe,
répétitions, comptes, sommes, carrés). Rien ici ne tire de nombre au hasard. Les seuils sont ceux du préenregistrement.

Ordre imposé : `exiger_validation` d'abord (la simulation retrouve la théorie et les mondes plantés) ; si elle lève,
aucun indicateur n'est lu. Puis `verdict` : la règle de choix, jouée aux deux effectifs du bloc principal et sous les
lectures « pari » et « student », puis la concordance avec le rééchantillonnage sur son bloc.
"""
from __future__ import annotations

import math

from ..gardes import GardeArret
from . import statistiques_v1 as st

NIVEAU_PRINCIPAL = 0.025
SEUIL_FAUX_POSITIFS = 0.065        # 0,05 nominal + 0,015 (trois erreurs de Monte-Carlo à 2 000 répétitions)
SEUIL_FAUX_POSITIFS_FRANC = 0.20
PUISSANCE_UTILE = 0.80
PART_DE_COUVERTURE_UTILE = 0.5     # une option « utile » garde au moins la moitié de la couverture du critère actuel
ECART_COUVERTURE = 0.10
ECART_COUVERTURE_FORT = 0.20
ECART_DE_TAUX_NET = 0.10
PART_DE_DESACCORD_REECH = 0.10
MARGE_THEORIE = 0.002

A_RETENUE = "A retenue"
C_RETENUE = "C retenue"
NON_TRANCHE_VALIDITE_PUISSANCE = "non tranché : la validité et la puissance ne désignent pas la même option"
NON_TRANCHE_EGALITE = "non tranché : ni la validité ni la puissance ne séparent les options ; le coût décide, hors de l'étude"
NON_TRANCHE_EFFECTIF = "non tranché : l'issue dépend de l'effectif"
NON_TRANCHE_STATISTIQUE = "non tranché : l'issue dépend de la statistique de décision"
NON_INFORMATIF = "non tranché : le critère actuel n'a de puissance utile dans aucun monde « sabotage » de la grille"
AUCUNE_INVALIDES = "aucune : les deux options laissent passer l'empreinte seule"
AUCUNE_SANS_PUISSANCE = "aucune : aucune option valide ne garde de puissance utile"
ISSUES = (A_RETENUE, C_RETENUE, NON_TRANCHE_VALIDITE_PUISSANCE, NON_TRANCHE_EGALITE, NON_TRANCHE_EFFECTIF,
          NON_TRANCHE_STATISTIQUE, NON_INFORMATIF, AUCUNE_INVALIDES, AUCUNE_SANS_PUISSANCE)


def taux(monde: dict, cle: str) -> float:
    if cle not in monde["comptes"]:
        raise GardeArret(f"compte absent : {cle}")
    r = monde["repetitions"]
    v = monde["comptes"][cle]
    if r < 1 or not (0 <= v <= r):
        raise GardeArret(f"compte {cle} = {v} sur {r} répétitions : invalide")
    return v / r


def erreur_mc(p: float, n: int) -> float:
    return math.sqrt(max(p * (1.0 - p), 0.0) / n)


def cle(lecture: str, alpha: float, composante: str) -> str:
    return f"{lecture}|{alpha}|{composante}"


def _par_etiquette(mondes: dict) -> dict:
    sortie = {}
    for m in mondes.values():
        if m["parametres"]["bloc"] == "validation":
            if m["parametres"]["etiquette"] in sortie:
                raise GardeArret(f"contrôle en double : {m['parametres']['etiquette']}")
            sortie[m["parametres"]["etiquette"]] = m
    return sortie


def controles_validation(mondes: dict) -> list[dict]:
    """Chaque contrôle : nom, valeur attendue (écrite d'avance), valeur simulée, tolérance, réussite."""
    v = _par_etiquette(mondes)
    sortie = []

    def ajouter(nom, attendu, observe, tolerance, sens):
        ok = {"egal": abs(observe - attendu) <= tolerance, "au_plus": observe <= attendu + tolerance,
              "au_moins": observe >= attendu - tolerance}[sens]
        sortie.append({"nom": nom, "sens": sens, "attendu": attendu, "observe": observe, "tolerance": tolerance, "reussi": bool(ok)})

    def exiger(etiquette):
        if etiquette not in v:
            raise GardeArret(f"monde de validation absent : {etiquette}")
        return v[etiquette]

    for n, pourcent, taux_vrai in ((200, 1, 0.01), (300, 1, 0.01), (200, 5, 0.05), (300, 5, 0.05)):
        m = exiger(f"V1-n{n}-taux{pourcent}")
        exact = st.passage_garde_exact(n, taux_vrai)
        ajouter(f"V1 garde exacte, {n} épisodes, taux vrai {pourcent} %", exact, taux(m, "garde_B1_exacte"),
                3 * erreur_mc(exact, m["repetitions"]) + MARGE_THEORIE, "egal")
        for k in (3, 6):
            g = m["garde_par_groupes_de_cellules"][str(k)]
            produit = st.conjonction_independante([exact] * k)
            ajouter(f"V2 conjonction de la garde sur {k} cellules, {n} épisodes, taux vrai {pourcent} %", produit,
                    g["tous_passent"] / g["groupes"], 3 * erreur_mc(produit, g["groupes"]) + MARGE_THEORIE, "egal")
    for etiquette in ("V3-frontiere-m1", "V3-frontiere-m3"):
        m = exiger(etiquette)
        for alpha in (0.025, 0.05):
            ajouter(f"V3 niveau du pari à la frontière du nul ({etiquette}, niveau {alpha})", alpha,
                    taux(m, cle("pari", alpha, "E")), 3 * erreur_mc(alpha, m["repetitions"]), "au_plus")
    m = exiger("V4-calibrage")
    r = m["repetitions"]
    moyenne = m["sommes"]["taux_alerte_temoin"] / r
    variance = max(m["carres"]["taux_alerte_temoin"] / r - moyenne ** 2, 0.0)
    ajouter("V4 taux d'alerte réel d'un seuil calibré sur 300 épisodes", 3.0 / 301.0, moyenne,
            3 * math.sqrt(variance / r) + 1e-4, "egal")
    p = lambda e, c: taux(exiger(e), cle("pari", NIVEAU_PRINCIPAL, c))
    for nom, composante, attendu, sens in (
            ("PL1-empreinte-seule-forte", "E", 0.95, "au_moins"), ("PL1-empreinte-seule-forte", "A", SEUIL_FAUX_POSITIFS, "au_plus"),
            ("PL1-empreinte-seule-forte", "B", SEUIL_FAUX_POSITIFS, "au_plus"),
            ("PL2-sabotage-pur", "A", 0.90, "au_moins"), ("PL2-sabotage-pur", "B", 0.90, "au_moins"),
            ("PL3-frontiere-empreinte-sous-le-seuil-seuils-exacts", "A", SEUIL_FAUX_POSITIFS, "au_plus"),
            ("PL3-frontiere-empreinte-sous-le-seuil-seuils-exacts", "B", 0.80, "au_moins"),
            ("PL4-sabotage-et-empreinte-forte", "A", 0.90, "au_moins"), ("PL4-sabotage-et-empreinte-forte", "B", SEUIL_FAUX_POSITIFS, "au_plus"),
            ("PL5-temoin-sans-valeur", "A", 0.90, "au_moins"), ("PL5-temoin-sans-valeur", "B", 0.90, "au_moins")):
        ajouter(f"{nom} : option ou composante {composante}", attendu, p(nom, composante), 0.0, sens)
    return sortie


def exiger_validation(mondes: dict) -> list[dict]:
    """Garde : un seul contrôle manqué invalide toute lecture (la simulation ne retrouve pas une réponse connue)."""
    controles = controles_validation(mondes)
    rates = [c["nom"] for c in controles if not c["reussi"]]
    if rates:
        raise GardeArret("validation manquée, aucune lecture permise : " + " ; ".join(rates))
    return controles


def indicateurs(mondes: dict, taches: int, lecture: str = "pari", alpha: float = NIVEAU_PRINCIPAL,
                imperfection: float = 0.0) -> dict:
    """Indicateurs de la règle sur le bloc principal, à un effectif et une imperfection du témoin donnés."""
    choisis = [m for m in mondes.values() if m["parametres"]["bloc"] == "principal"
               and m["parametres"]["taches"] == taches and m["parametres"]["imperfection_temoin"] == imperfection]
    par_classe = {c: [m for m in choisis if m["classe"] == c]
                  for c in ("empreinte_seule", "avance_vehiculaire", "frontiere", "sabotage")}
    for c, liste in par_classe.items():
        if not liste:
            raise GardeArret(f"aucun monde de classe {c} à {taches} tâches, imperfection {imperfection} : grille incomplète")
    sortie = {"taches": taches, "lecture": lecture, "niveau": alpha, "imperfection": imperfection,
              "mondes": {c: len(v) for c, v in par_classe.items()}}
    for option in ("E", "A", "B"):
        k = cle(lecture, alpha, option)
        puissances = [taux(m, k) for m in par_classe["sabotage"]]
        sortie[option] = {
            "faux_positifs_empreinte_seule": max(taux(m, k) for m in par_classe["empreinte_seule"]),
            "faux_positifs_avance_vehiculaire": max(taux(m, k) for m in par_classe["avance_vehiculaire"]),
            "passages_frontiere_rapportes": max(taux(m, k) for m in par_classe["frontiere"]),
            "couverture_de_puissance": sum(p >= PUISSANCE_UTILE for p in puissances) / len(puissances),
            "puissance_moyenne": sum(puissances) / len(puissances),
        }
    return sortie


def regle_de_choix(ind: dict) -> str:
    """La règle écrite au préenregistrement, sur un jeu d'indicateurs. Issues dans tous les sens."""
    a, b, e = ind["A"], ind["B"], ind["E"]
    if e["couverture_de_puissance"] <= 0.0:
        return NON_INFORMATIF
    valide = {o: v["faux_positifs_empreinte_seule"] <= SEUIL_FAUX_POSITIFS for o, v in (("A", a), ("B", b))}
    utile = {o: v["couverture_de_puissance"] >= PART_DE_COUVERTURE_UTILE * e["couverture_de_puissance"]
             for o, v in (("A", a), ("B", b))}
    if not valide["A"] and not valide["B"]:
        return AUCUNE_INVALIDES
    retenables = [o for o in ("A", "B") if valide[o] and utile[o]]
    if not retenables:
        return AUCUNE_SANS_PUISSANCE
    if len(retenables) == 1:
        return A_RETENUE if retenables[0] == "A" else C_RETENUE
    ecart = a["couverture_de_puissance"] - b["couverture_de_puissance"]

    def nette(x, y):   # x tient contre l'avance véhiculaire, y la laisse franchement passer
        return (x["faux_positifs_avance_vehiculaire"] <= SEUIL_FAUX_POSITIFS
                and y["faux_positifs_avance_vehiculaire"] > SEUIL_FAUX_POSITIFS_FRANC)

    if nette(a, b):
        return A_RETENUE if ecart >= -ECART_COUVERTURE_FORT else NON_TRANCHE_VALIDITE_PUISSANCE
    if nette(b, a):
        return C_RETENUE if ecart <= ECART_COUVERTURE_FORT else NON_TRANCHE_VALIDITE_PUISSANCE
    if ecart >= ECART_COUVERTURE:
        return A_RETENUE
    if ecart <= -ECART_COUVERTURE:
        return C_RETENUE
    return NON_TRANCHE_EGALITE


def concordance_reech(mondes: dict, alpha: float = NIVEAU_PRINCIPAL) -> dict:
    """Bloc de rééchantillonnage : part des mondes où l'écart net entre A et B change de signe entre le pari et le
    rééchantillonnage par blocs de tâches."""
    choisis = [m for m in mondes.values() if m["parametres"]["bloc"] == "reechantillonnage"]
    if not choisis:
        raise GardeArret("bloc de rééchantillonnage absent")
    desaccords = 0
    for m in choisis:
        ep = taux(m, cle("pari", alpha, "A")) - taux(m, cle("pari", alpha, "B"))
        er = taux(m, cle("reech", alpha, "A")) - taux(m, cle("reech", alpha, "B"))
        if abs(ep) >= ECART_DE_TAUX_NET and abs(er) >= ECART_DE_TAUX_NET and (ep > 0) != (er > 0):
            desaccords += 1
    return {"mondes": len(choisis), "desaccords": desaccords, "part": desaccords / len(choisis),
            "concordant": desaccords / len(choisis) <= PART_DE_DESACCORD_REECH}


def alertes_de_symetrie(mondes: dict, alpha: float = NIVEAU_PRINCIPAL) -> list[str]:
    """R4 : propretés suspectes, dans un sens comme dans l'autre. Chacune commande un audit avant tout prononcé."""
    principal = [m for m in mondes.values() if m["parametres"]["bloc"] == "principal"]
    if not principal:
        raise GardeArret("bloc principal absent")
    alertes = []
    sabotage = [m for m in principal if m["classe"] == "sabotage"]
    for option in ("A", "B"):
        t = [taux(m, cle("pari", alpha, option)) for m in sabotage]
        if all(x == 1.0 for x in t) or all(x == 0.0 for x in t):
            alertes.append(f"option {option} : puissance identique (0 ou 1) dans tous les mondes « sabotage »")
    if all(m["comptes"][cle("pari", alpha, "A")] == m["comptes"][cle("pari", alpha, "B")] for m in principal):
        alertes.append("options A et B : comptes identiques dans tous les mondes (câblage suspect)")
    if all(m["comptes"][cle("pari", alpha, "E")] == m["comptes"][cle("student", alpha, "E")] for m in principal):
        alertes.append("lectures « pari » et « student » : comptes identiques dans tous les mondes (câblage suspect)")
    return alertes


def verdict(mondes: dict, effectifs: tuple[int, ...] = (400, 600)) -> dict:
    """Issue de l'étude : validation, règle aux deux effectifs et sous deux lectures, concordance, alertes de symétrie."""
    controles = exiger_validation(mondes)
    table = {lecture: {t: indicateurs(mondes, t, lecture) for t in effectifs} for lecture in ("pari", "student")}
    issues = {lecture: {t: regle_de_choix(table[lecture][t]) for t in effectifs} for lecture in table}
    reech = concordance_reech(mondes)
    pari = set(issues["pari"].values())
    if len(pari) > 1:
        issue = NON_TRANCHE_EFFECTIF
    elif set(issues["student"].values()) != pari or not reech["concordant"]:
        issue = NON_TRANCHE_STATISTIQUE
    else:
        issue = pari.pop()
    return {"issue": issue, "issues_par_lecture_et_effectif": issues, "indicateurs": table, "concordance_reech": reech,
            "alertes_de_symetrie": alertes_de_symetrie(mondes), "controles": controles,
            "sensibilite_imperfection": {i: {t: indicateurs(mondes, t, "pari", imperfection=i) for t in effectifs}
                                         for i in (0.25, 0.5, 1.0)}}


def effectifs_minimaux(mondes: dict, option: str, lecture: str = "pari", alpha: float = NIVEAU_PRINCIPAL) -> list[dict]:
    """Bloc des effectifs : par monde « sabotage » et par nombre d'épisodes par tâche, le plus petit nombre de tâches de
    la grille où l'option passe dans au moins 80 % des répétitions, et si la puissance reste au-dessus ensuite."""
    familles: dict[tuple, dict[int, float]] = {}
    for m in mondes.values():
        p = m["parametres"]
        if p["bloc"] != "effectifs" or m["classe"] != "sabotage":
            continue
        k = (p["sabotage_blanche"], p["empreinte_blanche"], p["imperfection_temoin"], p["episodes_par_tache"])
        familles.setdefault(k, {})[p["taches"]] = taux(m, cle(lecture, alpha, option))
    if not familles:
        raise GardeArret("bloc des effectifs absent ou sans monde « sabotage »")
    sortie = []
    for k, courbe in sorted(familles.items()):
        atteints = [t for t in sorted(courbe) if courbe[t] >= PUISSANCE_UTILE]
        minimal = atteints[0] if atteints else None
        sortie.append({"sabotage_blanche": k[0], "empreinte_blanche": k[1], "imperfection_temoin": k[2],
                       "episodes_par_tache": k[3], "taches_minimales": minimal,
                       "monotone_ensuite": minimal is None or all(courbe[t] >= PUISSANCE_UTILE for t in courbe if t >= minimal),
                       "courbe": {str(t): courbe[t] for t in sorted(courbe)}})
    return sortie


def mesures_rapportees(monde: dict) -> dict:
    """Qualité des nombres que l'option C rapporte : moyenne, écart-type entre répétitions, biais contre la valeur
    vraie (témoin parfait, seuil exact ; bruit normal seulement)."""
    p, r = monde["parametres"], monde["repetitions"]
    verite = {}
    if p["bruit"] == "normal":
        verite = {"rappel_blanche_seuil_temoin": st.rappel_vrai(p["sabotage_blanche"], 0.01),
                  "contraste_c1": st.rappel_vrai(p["sabotage_blanche"], 0.01) - st.rappel_vrai(p["sabotage_noire"], 0.01),
                  "rappel_blanche_c2": st.rappel_vrai(p["sabotage_blanche"], 0.05),
                  "contraste_c2": st.rappel_vrai(p["sabotage_blanche"], 0.05) - st.rappel_vrai(p["sabotage_noire"], 0.05)}
    sortie = {}
    for nom in monde["sommes"]:
        moyenne = monde["sommes"][nom] / r
        variance = max(monde["carres"][nom] / r - moyenne ** 2, 0.0)
        sortie[nom] = {"moyenne": moyenne, "ecart_type": math.sqrt(variance),
                       "biais": moyenne - verite[nom] if nom in verite else None}
    return sortie
