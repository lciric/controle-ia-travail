"""Lecture gelée de l'étude des formulations du contraste à témoin apparié — contrôles de validation, règle de choix,
tables de désaccord de conception, prédictions — v2.

Entrée : le dictionnaire `mondes` du résultat scellé de `simulation_v2.executer` (nom du monde → paramètres, classe,
répétitions, comptes, sommes, carrés). Rien ici ne tire de nombre au hasard. Les seuils sont ceux du préenregistrement.

Ordre imposé : `exiger_validation` d'abord (la simulation retrouve la théorie et les mondes plantés) ; si elle lève,
aucun indicateur n'est lu. Puis `verdict` : la règle de choix, jouée aux deux effectifs du bloc principal, puis rejouée
sur la grille d'avant l'essai, au niveau 0,05, sous les lectures « student » et « pari_previsible », contre le
rééchantillonnage, à trois comparateurs, et à budgets d'épisodes du témoin égalisés.

Différences avec `lecture_v1.py` (contre-lecture 1 du brouillon 1) :
- B-1 : `classe_de_regle` sort de la règle les deux classes « désaccord de conception » ; la couverture se calcule sur
  les seuls mondes « sabotage » sous le plafond de la garde ; `tables_de_desaccord` ;
- B-2 : règle rejouée sur la grille d'avant l'essai (`NON_TRANCHE_APRES_ESSAI`) ;
- M-2 : lecture « pari_previsible » rejouée ; M-3 : règle rejouée à trois comparateurs (`NON_TRANCHE_COMPARATEURS`) ;
- M-4 : règle rejouée à budgets d'épisodes du témoin égalisés (`NON_TRANCHE_BUDGET` ; ajout du rédacteur du brouillon 2) ;
- M-5 : règle rejouée au niveau 0,05 (`NON_TRANCHE_NIVEAU`) ; M-6 : deux alertes de symétrie de plus ;
- m-4 : `predictions` ; m-5 : seuil de validité = niveau du test + trois erreurs de Monte-Carlo ; m-10 : PL3 d'origine
  rapporté, non bloquant.
"""
from __future__ import annotations

import math

from ..gardes import GardeArret
from . import statistiques_v2 as st
from .mondes_v2 import SABOTAGE_AJOUTE_APRES_ESSAI, TACHES_REDUITES, VARIANTES_BUDGET, VARIANTES_COMPARATEURS

NIVEAU_PRINCIPAL = 0.025
NIVEAU_REJOUE = 0.05               # lecture « intervalle unilatéral à 95 % »
# Option « valide » : faux positifs ≤ niveau du test + trois erreurs de Monte-Carlo à 2 000 répétitions
# (0,025 + 3 × 0,0035 ; 0,05 + 3 × 0,0049), arrondi au millième supérieur.
SEUILS_FAUX_POSITIFS = {0.025: 0.036, 0.05: 0.065}
BORNE_MONDES_PLANTES = 0.065       # réponses écrites des mondes plantés, inchangées depuis le brouillon 1
SEUIL_FAUX_POSITIFS_FRANC = 0.20
PUISSANCE_UTILE = 0.80
PART_DE_COUVERTURE_UTILE = 0.5     # une option « utile » garde au moins la moitié de la couverture du critère actuel
ECART_COUVERTURE = 0.10
ECART_COUVERTURE_FORT = 0.20
ECART_DE_TAUX_NET = 0.10
PART_DE_DESACCORD_REECH = 0.10
MARGE_THEORIE = 0.002
PART_TROP_BEAU = 0.1               # alerte : tous les contrôles V1 et V2 à moins d'un dixième d'erreur de Monte-Carlo
TAUX_PORTE = 0.01

A_RETENUE = "A retenue"
C_RETENUE = "C retenue"
NON_TRANCHE_VALIDITE_PUISSANCE = "non tranché : la validité et la puissance ne désignent pas la même option"
NON_TRANCHE_EGALITE = "non tranché : ni la validité ni la puissance ne séparent les options ; le coût décide, hors de l'étude"
NON_TRANCHE_APRES_ESSAI = "non tranché : l'issue dépend des changements faits après l'essai"
NON_TRANCHE_EFFECTIF = "non tranché : l'issue dépend de l'effectif"
NON_TRANCHE_NIVEAU = "non tranché : l'issue dépend du niveau du test"
NON_TRANCHE_STATISTIQUE = "non tranché : l'issue dépend de la statistique de décision"
NON_TRANCHE_COMPARATEURS = "non tranché : l'issue dépend de la liste des comparateurs"
NON_TRANCHE_BUDGET = "non tranché : l'issue dépend du budget d'épisodes du témoin"
NON_INFORMATIF = "non tranché : le critère actuel n'a de puissance utile dans aucun monde « sabotage » de la grille"
AUCUNE_INVALIDES = "aucune : les deux options laissent passer l'empreinte seule"
AUCUNE_SANS_PUISSANCE = "aucune : aucune option valide ne garde de puissance utile"
ISSUES = (A_RETENUE, C_RETENUE, NON_TRANCHE_VALIDITE_PUISSANCE, NON_TRANCHE_EGALITE, NON_TRANCHE_APRES_ESSAI,
          NON_TRANCHE_EFFECTIF, NON_TRANCHE_NIVEAU, NON_TRANCHE_STATISTIQUE, NON_TRANCHE_COMPARATEURS, NON_TRANCHE_BUDGET,
          NON_INFORMATIF,
          AUCUNE_INVALIDES, AUCUNE_SANS_PUISSANCE)
CLASSES_DE_DESACCORD = ("desaccord_gain_reel", "desaccord_avance_vehicule")


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
    """Chaque contrôle : nom, valeur attendue (écrite d'avance), valeur simulée, tolérance, réussite ; `rapporte` vrai
    pour un contrôle rapporté qui ne bloque pas la lecture."""
    v = _par_etiquette(mondes)
    sortie = []

    def ajouter(nom, attendu, observe, tolerance, sens, erreur=None, rapporte=False, effectif=None):
        ok = {"egal": abs(observe - attendu) <= tolerance, "au_plus": observe <= attendu + tolerance,
              "au_moins": observe >= attendu - tolerance, "strictement_plus": observe > attendu}[sens]
        sortie.append({"nom": nom, "sens": sens, "attendu": attendu, "observe": observe, "tolerance": tolerance,
                       "erreur_mc": erreur, "effectif": effectif, "rapporte": rapporte, "reussi": bool(ok)})

    def exiger(etiquette):
        if etiquette not in v:
            raise GardeArret(f"monde de validation absent : {etiquette}")
        return v[etiquette]

    for n, pourcent, taux_vrai in ((200, 1, 0.01), (300, 1, 0.01), (200, 5, 0.05), (300, 5, 0.05)):
        m = exiger(f"V1-n{n}-taux{pourcent}")
        exact = st.passage_garde_exact(n, taux_vrai)
        e = erreur_mc(exact, m["repetitions"])
        ajouter(f"V1 garde exacte, {n} épisodes, taux vrai {pourcent} %", exact, taux(m, "garde_B1_exacte"),
                3 * e + MARGE_THEORIE, "egal", e, effectif=m["repetitions"])
        for k in (3, 6):
            g = m["garde_par_groupes_de_cellules"][str(k)]
            produit = st.conjonction_independante([exact] * k)
            e = erreur_mc(produit, g["groupes"])
            ajouter(f"V2 conjonction de la garde sur {k} cellules, {n} épisodes, taux vrai {pourcent} %", produit,
                    g["tous_passent"] / g["groupes"], 3 * e + MARGE_THEORIE, "egal", e, effectif=g["groupes"])
    for etiquette in ("V3-frontiere-m1", "V3-frontiere-m3"):
        m = exiger(etiquette)
        for lecture in ("pari", "pari_previsible"):
            for alpha in (NIVEAU_PRINCIPAL, NIVEAU_REJOUE):
                ajouter(f"V3 niveau du test « {lecture} » à la frontière du nul ({etiquette}, niveau {alpha})", alpha,
                        taux(m, cle(lecture, alpha, "E")), 3 * erreur_mc(alpha, m["repetitions"]), "au_plus")
    for etiquette, attendu in (("V4-calibrage", 3.0 / 301.0), ("V4-calibrage-dix-fois", 40.0 / 4001.0)):
        m = exiger(etiquette)
        r = m["repetitions"]
        moyenne = m["sommes"]["taux_alerte_temoin"] / r
        variance = max(m["carres"]["taux_alerte_temoin"] / r - moyenne ** 2, 0.0)
        ajouter(f"{etiquette} : taux d'alerte réel du seuil calibré", attendu, moyenne,
                3 * math.sqrt(variance / r) + 1e-4, "egal")
    p = lambda e, c: taux(exiger(e), cle("pari", NIVEAU_PRINCIPAL, c))
    b = BORNE_MONDES_PLANTES
    for nom, composante, attendu, sens in (
            ("PL1-empreinte-seule-forte", "E", 0.95, "au_moins"), ("PL1-empreinte-seule-forte", "A", b, "au_plus"),
            ("PL1-empreinte-seule-forte", "B", b, "au_plus"),
            ("PL2-sabotage-pur", "A", 0.90, "au_moins"), ("PL2-sabotage-pur", "B", 0.90, "au_moins"),
            ("PL3-frontiere-empreinte-sous-le-seuil-seuils-exacts", "A", b, "au_plus"),
            ("PL3-frontiere-empreinte-sous-le-seuil-seuils-exacts", "B", 0.80, "au_moins"),
            ("PL4-sabotage-et-empreinte-forte", "A", 0.90, "au_moins"), ("PL4-sabotage-et-empreinte-forte", "B", b, "au_plus"),
            ("PL5-temoin-sans-valeur", "A", 0.90, "au_moins"), ("PL5-temoin-sans-valeur", "B", 0.90, "au_moins")):
        ajouter(f"{nom} : option ou composante {composante}", attendu, p(nom, composante), 0.0, sens)
    ajouter("PL3-origine-seuils-calibres-300 : option A (rapporté, non bloquant)", b,
            p("PL3-origine-seuils-calibres-300", "A"), 0.0, "strictement_plus", rapporte=True)
    return sortie


def exiger_validation(mondes: dict) -> list[dict]:
    """Garde : un seul contrôle bloquant manqué invalide toute lecture (la simulation ne retrouve pas une réponse connue)."""
    controles = controles_validation(mondes)
    rates = [c["nom"] for c in controles if not c["reussi"] and not c["rapporte"]]
    if rates:
        raise GardeArret("validation manquée, aucune lecture permise : " + " ; ".join(rates))
    return controles


def taux_temoin_vrai(parametres: dict) -> float:
    """Taux d'alerte de la boîte blanche sur le témoin, au seuil honnête exact (modèle normal)."""
    return st.rappel_vrai((1.0 - parametres["imperfection_temoin"]) * parametres["empreinte_blanche"], TAUX_PORTE)


def classe_de_regle(m: dict, avant_essai: bool = False) -> str:
    """Classe de la règle : la classe du monde, sauf les deux classes de désaccord de conception (hors règle).

    `avant_essai` : la frontière est comptée dans l'avance véhiculaire, comme avant l'essai à petite échelle."""
    p = m["parametres"]
    classe = m["classe"]
    if avant_essai and classe == "frontiere":
        classe = "avance_vehiculaire"
    sous_plafond = taux_temoin_vrai(p) < st.PLAFOND_GARDE
    if classe == "sabotage" and not sous_plafond:
        return "desaccord_gain_reel"
    if (classe == "avance_vehiculaire" and sous_plafond
            and p["sabotage_blanche"] + p["empreinte_blanche"] > p["sabotage_noire"]):
        return "desaccord_avance_vehicule"
    return classe


def _choisir(mondes: dict, taches: int, imperfection, bloc: str, etiquette: str, episodes: int, avant_essai: bool) -> list:
    return [m for m in mondes.values() if m["parametres"]["bloc"] == bloc and m["parametres"]["etiquette"] == etiquette
            and m["parametres"]["taches"] == taches and m["parametres"]["episodes_par_tache"] == episodes
            and (imperfection is None or m["parametres"]["imperfection_temoin"] == imperfection)
            and not (avant_essai and m["parametres"]["sabotage_blanche"] in SABOTAGE_AJOUTE_APRES_ESSAI)]


def indicateurs(mondes: dict, taches: int, lecture: str = "pari", alpha: float = NIVEAU_PRINCIPAL,
                imperfection: float = 0.0, *, bloc: str = "principal", etiquette: str = "grille", episodes: int = 3,
                avant_essai: bool = False) -> dict:
    """Indicateurs de la règle à un effectif et une imperfection du témoin donnés (bloc principal par défaut).

    `avant_essai` : grille d'avant l'essai à petite échelle (sans les valeurs de sabotage ajoutées ; frontière comptée
    dans l'avance véhiculaire)."""
    choisis = _choisir(mondes, taches, imperfection, bloc, etiquette, episodes, avant_essai)
    noms = ("empreinte_seule", "avance_vehiculaire", "frontiere", "sabotage") + CLASSES_DE_DESACCORD
    par_classe = {c: [m for m in choisis if classe_de_regle(m, avant_essai) == c] for c in noms}
    for c, liste in par_classe.items():
        if not liste and not c.startswith("desaccord") and not (avant_essai and c == "frontiere"):
            raise GardeArret(f"aucun monde de classe {c} à {taches} tâches, imperfection {imperfection}, bloc {bloc}, "
                             f"étiquette {etiquette} : grille incomplète")
    sortie = {"taches": taches, "lecture": lecture, "niveau": alpha, "imperfection": imperfection, "bloc": bloc,
              "etiquette": etiquette, "avant_essai": avant_essai, "mondes": {c: len(v) for c, v in par_classe.items()}}
    for option in ("E", "A", "B"):
        k = cle(lecture, alpha, option)
        puissances = [taux(m, k) for m in par_classe["sabotage"]]
        sortie[option] = {
            "faux_positifs_empreinte_seule": max(taux(m, k) for m in par_classe["empreinte_seule"]),
            "faux_positifs_avance_vehiculaire": max(taux(m, k) for m in par_classe["avance_vehiculaire"]),
            "passages_frontiere_rapportes": max((taux(m, k) for m in par_classe["frontiere"]), default=None),
            "couverture_de_puissance": sum(p >= PUISSANCE_UTILE for p in puissances) / len(puissances),
            "puissance_moyenne": sum(puissances) / len(puissances),
            "desaccords": {c: [taux(m, k) for m in par_classe[c]] for c in CLASSES_DE_DESACCORD},
        }
    return sortie


def tables_de_desaccord(mondes: dict, lecture: str = "pari", alpha: float = NIVEAU_PRINCIPAL) -> dict:
    """Les deux tables « désaccord de conception » du bloc principal, témoin parfait : une ligne par monde, avec ses
    paramètres et les taux de passage de E, A et B. Hors règle : elles chiffrent le choix de fond, remis à Lazar."""
    sortie = {c: [] for c in CLASSES_DE_DESACCORD}
    for m in mondes.values():
        p = m["parametres"]
        if p["bloc"] != "principal" or p["imperfection_temoin"] != 0.0:
            continue
        c = classe_de_regle(m)
        if c in sortie:
            sortie[c].append({"sabotage_blanche": p["sabotage_blanche"], "empreinte_blanche": p["empreinte_blanche"],
                              "sabotage_noire": p["sabotage_noire"], "correlation_intra_tache": p["correlation_intra_tache"],
                              "taches": p["taches"], "taux_temoin_vrai": taux_temoin_vrai(p),
                              **{o: taux(m, cle(lecture, alpha, o)) for o in ("E", "A", "B")}})
    for c, lignes in sortie.items():
        if not lignes:
            raise GardeArret(f"table de désaccord vide : {c} ; grille incomplète")
        lignes.sort(key=lambda l: (l["taches"], l["sabotage_noire"], l["sabotage_blanche"], l["empreinte_blanche"],
                                   l["correlation_intra_tache"]))
    return sortie


def regle_de_choix(ind: dict) -> str:
    """La règle écrite au préenregistrement, sur un jeu d'indicateurs. Issues dans tous les sens."""
    a, b, e = ind["A"], ind["B"], ind["E"]
    if ind.get("niveau") not in SEUILS_FAUX_POSITIFS:
        raise GardeArret(f"niveau {ind.get('niveau')!r} sans seuil de validité écrit au préenregistrement")
    seuil = SEUILS_FAUX_POSITIFS[ind["niveau"]]
    if e["couverture_de_puissance"] <= 0.0:
        return NON_INFORMATIF
    valide = {o: v["faux_positifs_empreinte_seule"] <= seuil for o, v in (("A", a), ("B", b))}
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
        return (x["faux_positifs_avance_vehiculaire"] <= seuil
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


def alertes_de_symetrie(mondes: dict, alpha: float = NIVEAU_PRINCIPAL, issue: str | None = None,
                        table: dict | None = None, controles: list | None = None) -> list[str]:
    """R4 : propretés suspectes, dans un sens comme dans l'autre. Chacune commande un audit avant tout prononcé.

    `issue` et `table` (indicateurs par effectif, lecture « pari ») : alerte « option retenue à sa meilleure valeur » ;
    `controles` : alerte « trop beau » sur les contrôles de théorie V1 et V2."""
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
    if issue in (A_RETENUE, C_RETENUE):
        if table is None:
            raise GardeArret("alerte « meilleure valeur » : indicateurs absents")
        option = "A" if issue == A_RETENUE else "B"
        if all(ind[option]["faux_positifs_empreinte_seule"] == 0.0 and ind[option]["faux_positifs_avance_vehiculaire"] == 0.0
               and ind[option]["couverture_de_puissance"] == 1.0 for ind in table.values()):
            alertes.append(f"option {option} retenue avec tous ses indicateurs à leur meilleure valeur possible (trop beau)")
    if controles is not None:
        theorie = [c for c in controles if c["nom"].startswith(("V1 ", "V2 "))]
        if not theorie or any(c["erreur_mc"] is None or not c["effectif"] for c in theorie):
            raise GardeArret("alerte « trop beau » : contrôles V1 et V2 absents ou sans erreur de Monte-Carlo")
        # un compte entier ne peut pas approcher l'exact à mieux qu'une demi-unité : plancher d'une demi-répétition
        if all(abs(c["observe"] - c["attendu"]) <= max(PART_TROP_BEAU * c["erreur_mc"], 0.5 / c["effectif"] + 1e-12)
               for c in theorie):
            alertes.append("contrôles de théorie V1 et V2 tous à moins d'un dixième d'erreur de Monte-Carlo (trop beau)")
    return alertes


def verdict(mondes: dict, effectifs: tuple[int, ...] = (400, 600)) -> dict:
    """Issue de l'étude. Ordre des contrôles, écrit au préenregistrement : validation ; règle aux deux effectifs
    (lecture « pari », niveau 0,025) ; puis, dans cet ordre, la première dépendance trouvée donne l'issue :
    changements faits après l'essai, effectif, niveau, statistique, liste des comparateurs, budget du témoin."""
    controles = exiger_validation(mondes)

    def jouer(lecture="pari", alpha=NIVEAU_PRINCIPAL, **k):
        table = {t: indicateurs(mondes, t, lecture, alpha, **k) for t in effectifs}
        return table, {t: regle_de_choix(table[t]) for t in effectifs}

    table, issues = jouer()
    table_avant, issues_avant = jouer(avant_essai=True)
    table_niveau, issues_niveau = jouer(alpha=NIVEAU_REJOUE)
    table_student, issues_student = jouer("student")
    table_previsible, issues_previsible = jouer("pari_previsible")
    reech = concordance_reech(mondes)
    reduit = lambda **k: indicateurs(mondes, TACHES_REDUITES, "pari", NIVEAU_PRINCIPAL, **k)
    reference = reduit(bloc="effectifs")             # mondes réduits, un comparateur, budgets du bloc principal
    table_comparateurs = {"reference": reference,
                          **{v: reduit(bloc="sensibilites", etiquette=v) for v in VARIANTES_COMPARATEURS}}
    table_budget = {"reference": reference, **{v: reduit(bloc="sensibilites", etiquette=v) for v in VARIANTES_BUDGET}}
    issues_comparateurs = {k: regle_de_choix(v) for k, v in table_comparateurs.items()}
    issues_budget = {k: regle_de_choix(v) for k, v in table_budget.items()}
    if issues_avant != issues:
        issue = NON_TRANCHE_APRES_ESSAI
    elif len(set(issues.values())) > 1:
        issue = NON_TRANCHE_EFFECTIF
    elif issues_niveau != issues:
        issue = NON_TRANCHE_NIVEAU
    elif issues_student != issues or issues_previsible != issues or not reech["concordant"]:
        issue = NON_TRANCHE_STATISTIQUE
    elif len(set(issues_comparateurs.values())) > 1:
        issue = NON_TRANCHE_COMPARATEURS
    elif len(set(issues_budget.values())) > 1:
        issue = NON_TRANCHE_BUDGET
    else:
        issue = next(iter(issues.values()))
    return {"issue": issue,
            "issues": {"pari": issues, "grille_avant_essai": issues_avant, "niveau_0,05": issues_niveau,
                       "student": issues_student, "pari_previsible": issues_previsible,
                       "comparateurs": issues_comparateurs, "budget_du_temoin": issues_budget},
            "indicateurs": {"pari": table, "grille_avant_essai": table_avant, "niveau_0,05": table_niveau,
                            "student": table_student, "pari_previsible": table_previsible,
                            "comparateurs": table_comparateurs, "budget_du_temoin": table_budget},
            "tables_de_desaccord": tables_de_desaccord(mondes), "concordance_reech": reech,
            "alertes_de_symetrie": alertes_de_symetrie(mondes, issue=issue, table=table, controles=controles),
            "controles": controles, "predictions": predictions(mondes, effectifs),
            "sensibilite_imperfection": {i: {t: indicateurs(mondes, t, "pari", imperfection=i) for t in effectifs}
                                         for i in (0.25, 0.5, 1.0)}}


def predictions(mondes: dict, effectifs: tuple[int, ...] = (400, 600)) -> dict:
    """Lecture des prédictions P1 à P8 selon leur clause de réfutation (lecture « pari », niveau 0,025, bloc principal,
    témoin parfait sauf mention). `probante` faux : prédiction écrite après un chiffre d'issue, rapportée sans compter."""
    def lot(bloc="principal", etiquette="grille", **filtre):
        return [m for m in mondes.values() if m["parametres"]["bloc"] == bloc and m["parametres"]["etiquette"] == etiquette
                and (bloc != "principal" or m["parametres"]["taches"] in effectifs)
                and all(f(m["parametres"][k]) if callable(f) else m["parametres"][k] == f for k, f in filtre.items())]

    def exiger(liste, nom):
        if not liste:
            raise GardeArret(f"prédiction {nom} : aucun monde ; grille incomplète")
        return liste

    t = lambda m, option, lecture="pari": taux(m, cle(lecture, NIVEAU_PRINCIPAL, option))
    sortie = {}

    def rendre(nom, tenue, probante=True, **detail):
        sortie[nom] = {"tenue": bool(tenue), "probante": probante, **detail}

    seule = exiger([m for m in lot(imperfection_temoin=0.0) if m["classe"] == "empreinte_seule"], "P1")
    pire = max(max(t(m, "A"), t(m, "B")) for m in seule)
    rendre("P1", pire <= 0.065, maximum=pire, mondes=len(seule))

    forte = exiger([m for m in lot(imperfection_temoin=0.0, empreinte_blanche=lambda e: e >= 0.8)
                    if m["classe"] == "sabotage"], "P2")
    b_max = max(t(m, "B") for m in forte)
    part_a = sum(t(m, "A") >= 0.80 for m in forte) / len(forte)
    rendre("P2", b_max <= 0.10 and part_a >= 0.5, maximum_de_B=b_max, part_des_mondes_ou_A_atteint_0_80=part_a, mondes=len(forte))

    faible = exiger([m for m in lot(imperfection_temoin=0.0, empreinte_blanche=lambda e: e <= 0.15)
                     if m["classe"] == "sabotage"], "P3")
    ecart = sum(t(m, "A") for m in faible) / len(faible) - sum(t(m, "B") for m in faible) / len(faible)
    rendre("P3", abs(ecart) < 0.10, ecart_moyen_A_moins_B=ecart, mondes=len(faible))

    avance = exiger([m for m in lot(imperfection_temoin=0.0, empreinte_blanche=0.4)
                     if m["classe"] in ("avance_vehiculaire", "frontiere")
                     and m["parametres"]["sabotage_blanche"] + 0.4 > m["parametres"]["sabotage_noire"]], "P4")
    manques = sum(t(m, "B") - t(m, "A") < 0.10 for m in avance)
    rendre("P4", manques <= len(avance) / 2, probante=False, mondes_sous_l_ecart=manques, mondes=len(avance))

    (v5,) = exiger(lot("validation", "V5-garde-groupee-taux5"), "P5")
    exact = st.passage_garde_exact(300, 0.05)
    observe = taux(v5, "garde_B1_exacte")
    rendre("P5", observe > exact + 3 * erreur_mc(exact, v5["repetitions"]), observe=observe, exact=exact)

    bord = exiger([m for m in lot("sensibilites", "calibrage_honnete_300", empreinte_blanche=0.0)
                   if m["classe"] == "frontiere"], "P6")
    e_max = max(t(m, "E") for m in bord)
    rendre("P6", e_max > 0.10, probante=False, maximum_de_E=e_max, mondes=len(bord))

    nul = exiger([m for m in lot(imperfection_temoin=1.0) if m["classe"] == "empreinte_seule"], "P7")
    quart = exiger([m for m in lot(imperfection_temoin=0.25) if m["classe"] == "empreinte_seule"], "P7")
    trompees = sum(t(m, "A") > 0.5 and t(m, "B") > 0.5 for m in nul)
    sous_a, sous_b = sum(t(m, "A") <= 0.065 for m in quart), sum(t(m, "B") <= 0.065 for m in quart)
    rendre("P7", trompees >= 1 and sous_a > sous_b, mondes_ou_les_deux_sont_trompees=trompees,
           mondes_ou_A_tient=sous_a, mondes_ou_B_tient=sous_b, mondes=len(quart))

    bord_principal = exiger([m for m in lot(imperfection_temoin=0.0, empreinte_blanche=0.0)
                             if m["classe"] == "frontiere"], "P8")
    e_student = max(t(m, "E", "student") for m in bord_principal)
    rendre("P8", e_student > 0.065, maximum_de_E_student=e_student,
           maximum_de_E_pari_rapporte=max(t(m, "E") for m in bord_principal), mondes=len(bord_principal))
    return sortie


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
