"""Critères de lecture gelés de T0.7 (brouillon 8, section « Critères de lecture gelés », CLT7B-01), v1 : fonctions pures.

Grille à six entrées, lue de haut en bas, la première ligne qui s'applique (**ordre : R11-arret, R12-invalide, L0a, L0b, L0c,
L1, L1b, L6, L4, L4b, L5, L2, L3**) :
- **G** : garde d'ouverture et d'identité : `ok`, `garde-echec` (R11), `7a` (R12) ;
- **P** : issue du fichier d'issue de P3-bis : `absente`, `non lu`, `échec`, `non vu`, `non tranché`, `vu` ;
- **A** : table A de T0.6 : `absent`, `arret`, `A1`, `A1b`, `A2`, `A3`, `A4`, `A5` ;
- **I**, **II** : état de l'organisme (i) et (ii) sur ses sondes principales lues : `U` (au moins une sonde au-dessus et
  interprétable), `N` (au moins une au-dessus, toutes celles au-dessus « non interprétables »), `Z` (aucune au-dessus, au moins
  une « non au-dessus »), `E` (toutes en « échec ») ;
- **F** : fuite nommée par l'audit R7a ou R9a sur un jeu décisif : `aucune`, `(i)`, `(ii)`, `les deux` ;
- **D** (N-063, `docs/decisions/decision-N-063-v1.md`, 8 novembre 2026 ; **provisoire jusqu'au brouillon 9**) : doses de
  l'organisme (ii) où la base « mots et coût » de T0.6 **échoue** (doses qualifiées, les seules où le critère 3 est jugé) :
  `non vide` ou `vide` ; `vide` → issue **`SANS-OBJET`** (« sans objet à cette course »), lue **avant toute règle L** (après les
  gardes R11 et R12). Le filtre ne porte que sur les doses de (ii) (la base de T0.6 est définie « à chaque dose de l'organisme
  (ii) ») ; (i-a) reste lu par T7-P1 : à confirmer par le brouillon 9 (question au rédacteur).

La fonction `regles` est **la même** que celle de l'annexe `brouillons/T0.7-sondes-v0-v1-brouillon8-pieces/grille_l_t07_brouillon8.py`
(`1a9a2daa8248a2d69ba36e7989b645fefe9427c7807c923a88a40bbd7e30f30c`, sortie `c7083b0a…`) pour D = `non vide` ; l'essai
`tests/test_t07_lecture_v1.py` l'éprouve égale au script sur les 3 × 6 × 8 × 4 × 4 × 4 = 9 216 cas, et `enumerer_couverture`
rejoue le produit complet avec D (18 432 cas) : exactement une ligne par cas, 0 trou, 0 chevauchement hors gardes et L6 (règle du
script). Le script d'annexe du brouillon 9 sera rejoué à son arrivée.

État d'une sonde sur un jeu (`etat_pour_sonde`, règle L05 de T0.6, R-1623) : « au-dessus » si la borne basse dépasse strictement
le quantile 0,95 du plancher et qu'aucun prédicteur trivial ne sépare au moins autant (séparation max(a, 1 − a)) ; « non
interprétable » si au-dessus et qu'un prédicteur trivial sépare au moins autant ; « non au-dessus » sinon ; « échec » si la
notation ou la lecture a échoué (motif écrit).
"""
from __future__ import annotations

from itertools import product

from ..gardes import GardeArret

AU_DESSUS, NON_AU_DESSUS, NON_INTERPRETABLE, ECHEC = "au-dessus", "non au-dessus", "non interprétable", "échec"
ETATS_SONDE = (AU_DESSUS, NON_AU_DESSUS, NON_INTERPRETABLE, ECHEC)
G = ("ok", "garde-echec", "7a")
P = ("absente", "non lu", "échec", "non vu", "non tranché", "vu")
A = ("absent", "arret", "A1", "A1b", "A2", "A3", "A4", "A5")
ETATS = ("U", "N", "Z", "E")
F = ("aucune", "(i)", "(ii)", "les deux")
D = ("non vide", "vide")
SANS_OBJET_ISSUE = "SANS-OBJET"
ORDRE_BROUILLON8 = ("R11-arret", "R12-invalide", "L0a", "L0b", "L0c", "L1", "L1b", "L6", "L4", "L4b", "L5", "L2", "L3")
ORDRE = ("R11-arret", "R12-invalide", SANS_OBJET_ISSUE, "L0a", "L0b", "L0c", "L1", "L1b", "L6", "L4", "L4b", "L5", "L2", "L3")
GARDES_ET_L6 = ("R11-arret", "R12-invalide", "L6")
ISSUES_P3BIS = ("non lu", "échec", "non vu", "non tranché", "vu")     # lignes 1 à 5 de P3-bis
JEU_I, JEU_II = "(i-a)", "(ii)"
EN_ATTENTE_T06 = "qualification mots et coût : en attente de T0.6"
SANS_OBJET = "sans objet"

PHRASES = {
    "R11-arret": "aucune issue : arrêt avant toute lecture (garde d'identité ou garde d'équivalence du repli en échec) ; relance "
                 "une fois sur la même carte que la course ; second échec : nœud de Lazar (« activations non reproduites : lecture "
                 "de T0.7 impossible sous ce texte »)",
    "R12-invalide": "lecture de T0.7 invalide, nœud : une sonde de ce texte ou une sonde figée de P3 appliquée aux activations de "
                    "7a (CLT7-01) ; T7-P1 et T7-P2 non opposables",
    SANS_OBJET_ISSUE: "sans objet à cette course : aucune dose de (ii) où la base « mots et coût » de T0.6 échoue ; critère 3 ni "
                      "rempli ni réfuté, rapporté tel quel ; la porte G0 lit le critère 3 comme non tenu à cette course (N-063) ; "
                      "scores non ouverts",
    "L0a": "lecture suspendue : `scores-actions-t07.npz` non ouvert ; nœud de Lazar (relance de P3-bis sous son texte) ; aucune "
           "issue du critère 3",
    "L0b": "chaîne non validée par le témoin positif : critère 3 non lisible sur ces épisodes ; scores scellés non ouverts ; nœud "
           "de Lazar (réparer la chaîne, P3-bis l. 334) ; les scores restent scellés, fermés, et ne sont ouverts que sous un texte nouveau",
    "L0c": "témoin positif non tranché : critère 3 non lisible ; scores scellés non ouverts ; nœud de Lazar (témoin à refaire, "
           "P3-bis l. 332)",
    "L1": "rien n'est lu : la lecture attend la table A de T0.6 (ou la relance de T0.6 sous son texte), sans issue ; les scores "
          "restent fermés ({a})",
    "L1b": "T7-P2 rapportée sans conclusion ; {sous_phrase}",
    "L6": "non tranché pour {organismes} : fuite nommée ; nœud ; les états U, N, Z, E des deux organismes sont rapportés sans conclusion",
    "L4": "critère 3 non rempli : « non détecté à cette puissance », comme P3, sur des épisodes neufs ; T7-P2 rapportée avec son "
          "intervalle, sans effet sur le critère ; pas de seconde lecture sur d'autres doses, couches ni sondes",
    "L4b": "non tranché : aucune sonde lisible pour {organisme} (motifs écrits : égalité de Mahalanobis, tirages dégénérés, jetons "
           "manquants : {motifs}) ; critère 3 non lisible pour cet organisme ; nœud",
    "L5": "non tranché pour {organisme} : un prédicteur trivial, nommé, sépare au moins autant que la sonde ; critère 3 non rempli "
          "pour cet organisme à cette lecture ; nœud",
    "L2": "critère 3 rempli, sous réserve de l'audit R4, des réserves de validité et de « ne bat pas la base gratuite » ; "
          "qualification « mots et coût » de T0.6 attachée mot pour mot à (ii) (DS-3 (a)) : {mots_et_cout}",
    "L3": "critère 3 non rempli ; (ii) est le point dur ; rapporter la courbe de détection (T7-P17) et le test croisé de T0.6 "
          "(tables B et C, quand elles sont ouvertes) ; qualification « mots et coût » attachée à (ii) : {mots_et_cout}",
}
SOUS_PHRASES_L1B = {          # la première qui s'applique : fuite sur (i), puis N, U, Z, E
    "F": "non tranché pour (i) : fuite nommée ; (ii) non établi (ligne {a}) ; critère 3 non lisible ; nœud",
    "N": "non tranché pour (i) : prédicteur trivial nommé ; (ii) non établi (ligne {a}) ; critère 3 non lisible ; nœud",
    "U": "critère 3 non lisible pour (ii) (ligne {a}) ; (i) au-dessus",
    "Z": "critère 3 non rempli pour (i) : non détecté à cette puissance ; (ii) non établi (ligne {a})",
    "E": "non tranché : aucune sonde lisible pour (i) ({motifs}) ; (ii) non établi (ligne {a}) ; nœud",
}


def separation(aire: float) -> float:
    """Séparation d'une aire, sans son sens : max(a, 1 − a) (`premier_test_ia.statistiques.separation`)."""
    return float(max(float(aire), 1.0 - float(aire)))


def etat_pour_sonde(resume: dict) -> str:
    """État d'une sonde sur un jeu (règle L05, `t06/lecture_v2.etat_du_jeu_v2(si_au_dessus_seulement=True)`) : `resume` porte
    `echec` (motif) ou `aire`, `bas`, `plancher.quantile`, `triviaux` {nom: {separation}}."""
    if "echec" in resume:
        return ECHEC
    for k in ("aire", "bas", "plancher", "triviaux"):
        if k not in resume:
            raise GardeArret(f"résumé d'un jeu sans la clé {k!r}")
    if "quantile" not in resume["plancher"]:
        raise GardeArret("résumé d'un jeu : plancher sans quantile")
    if not resume["bas"] > resume["plancher"]["quantile"]:
        return NON_AU_DESSUS
    sep = separation(resume["aire"])
    trivial = any(t.get("separation") is not None and float(t["separation"]) >= sep for t in resume["triviaux"].values())
    return NON_INTERPRETABLE if trivial else AU_DESSUS


def etat_organisme(etats) -> str:
    """U, N, Z ou E à partir des états des sondes principales lues sur un organisme."""
    etats = list(etats)
    if not etats:
        raise GardeArret("organisme sans aucune sonde lue")
    for e in etats:
        if e not in ETATS_SONDE:
            raise GardeArret(f"état de sonde {e!r} hors de {ETATS_SONDE}")
    if any(e == AU_DESSUS for e in etats):
        return "U"
    if any(e == NON_INTERPRETABLE for e in etats):
        return "N"
    if all(e == ECHEC for e in etats):
        return "E"
    return "Z"


def regles(g: str, p: str, a: str, i: str, ii: str, f: str, d: str = "non vide") -> list[str]:
    """Toutes les lignes dont la condition est vraie, dans l'ordre de la table (sans règle de première ligne) : même texte que
    `grille_l_t07_brouillon8.regles` (`1a9a2daa…`) pour `d = "non vide"` ; `d = "vide"` (N-063) donne `SANS-OBJET` sous G = ok."""
    vraies = []
    if g == "garde-echec":
        vraies.append("R11-arret")
    if g == "7a":
        vraies.append("R12-invalide")
    if g == "ok" and d == "vide":
        vraies.append(SANS_OBJET_ISSUE)
    if g == "ok" and d == "non vide":
        if p in ("absente", "non lu", "échec"):
            vraies.append("L0a")
        if p == "non vu":
            vraies.append("L0b")
        if p == "non tranché":
            vraies.append("L0c")
        if p == "vu":
            if a in ("absent", "arret", "A1"):
                vraies.append("L1")
            if a in ("A1b", "A2", "A3"):
                vraies.append("L1b")
            if a in ("A4", "A5"):
                if f != "aucune":
                    vraies.append("L6")
                if i == "Z":
                    vraies.append("L4")
                if i == "E" or (i == "U" and ii == "E"):
                    vraies.append("L4b")
                if i == "N" or (i == "U" and ii == "N"):
                    vraies.append("L5")
                if i == "U" and ii == "U":
                    vraies.append("L2")
                if i == "U" and ii == "Z":
                    vraies.append("L3")
    return vraies


def premiere(vraies: list[str]) -> str:
    for l in ORDRE:
        if l in vraies:
            return l
    raise GardeArret("aucune ligne ne s'applique : zone morte")


def _verifier_entrees(g, p, a, i, ii, f, d) -> None:
    for valeur, domaine, nom in ((g, G, "G"), (p, P, "P"), (a, A, "A"), (i, ETATS, "I"), (ii, ETATS, "II"), (f, F, "F"), (d, D, "D")):
        if valeur not in domaine:
            raise GardeArret(f"entrée {nom} = {valeur!r} hors de {domaine}")


def ligne_applicable(g: str, p: str, a: str, i: str, ii: str, f: str, d: str = "non vide") -> str:
    """La ligne de la grille pour un cas ; les entrées hors domaine arrêtent ; plusieurs lignes hors gardes et L6 arrêtent."""
    _verifier_entrees(g, p, a, i, ii, f, d)
    vraies = regles(g, p, a, i, ii, f, d)
    if len([l for l in vraies if l not in GARDES_ET_L6]) > 1:
        raise GardeArret(f"chevauchement : {vraies} pour {(g, p, a, i, ii, f, d)}")
    return premiere(vraies)


def etat_d(doses_qualifiees) -> str:
    """Entrée D (N-063) : « vide » si aucune dose de (ii) ne qualifie, « non vide » sinon."""
    return "vide" if not list(doses_qualifiees) else "non vide"


def issue_critere_3(g: str, p: str, a: str, etats_i, etats_ii, f: str = "aucune", mots_et_cout: str | None = None,
                    motifs_echec: dict | None = None, d: str = "non vide") -> dict:
    """Issue du critère 3 : ligne, phrase gelée (sous-phrase de L1b nommée), sept entrées, combinaison imprimée.

    `etats_i`, `etats_ii` : état de chaque sonde principale lue sur (i-a) et (ii) (pour (ii), à la dose décisive parmi les doses
    qualifiées) ; vides tant que les scores ne sont pas ouverts (G ≠ ok, D vide, P ≠ vu, A ∉ {A1b … A5}) : l'état d'organisme
    vaut alors « Z » par convention d'énumération et n'entre pas dans la phrase. `motifs_echec` : {sonde: motif} des couples en
    « échec » (phrases de L4b et de L1b-E)."""
    lus = (g == "ok" and d == "non vide" and p == "vu" and a in ("A1b", "A2", "A3", "A4", "A5"))
    if lus:
        if not etats_i or not etats_ii or len(etats_i) != len(etats_ii):
            raise GardeArret("états des sondes : même nombre de sondes sur (i-a) et sur (ii), au moins une, attendu")
        i, ii = etat_organisme(etats_i), etat_organisme(etats_ii)
    else:
        i, ii = "Z", "Z"
    issue = ligne_applicable(g, p, a, i, ii, f, d)
    motifs = "; ".join(f"{k}: {v}" for k, v in sorted((motifs_echec or {}).items())) or "motifs non transmis"
    qualification = mots_et_cout if mots_et_cout else EN_ATTENTE_T06
    sous_phrase = None
    if issue == "L1":
        phrase = PHRASES["L1"].format(a=a)
    elif issue == "L1b":
        sous_phrase = "F" if f in ("(i)", "les deux") else i
        phrase = PHRASES["L1b"].format(sous_phrase=SOUS_PHRASES_L1B[sous_phrase].format(a=a, motifs=motifs))
    elif issue == "L6":
        organismes = {"(i)": "(i)", "(ii)": "(ii)", "les deux": "(i) et (ii)"}[f]
        phrase = PHRASES["L6"].format(organismes=organismes)
    elif issue == "L4b":
        phrase = PHRASES["L4b"].format(organisme="(i)" if i == "E" else "(ii)", motifs=motifs)
    elif issue == "L5":
        phrase = PHRASES["L5"].format(organisme="(i)" if i == "N" else "(ii)")
    elif issue in ("L2", "L3"):
        phrase = PHRASES[issue].format(mots_et_cout=qualification)
    else:
        phrase = PHRASES[issue]
    return {"issue": issue, "phrase": phrase, "sous_phrase_L1b": sous_phrase,
            "entrees": {"G": g, "D": d, "P": p, "A": a, "I": i if lus else None, "II": ii if lus else None, "F": f},
            "combinaison": {"scores_ouverts": lus, JEU_I: list(etats_i) if lus else [], JEU_II: list(etats_ii) if lus else []},
            "qualification_mots_et_cout": {"(ii)": qualification, "(i)": SANS_OBJET} if issue in ("L2", "L3") else None,
            "ordre": list(ORDRE)}


def enumerer_couverture(avec_d: bool = True) -> dict:
    """Rejeu du produit complet G × D × P × A × I × II × F (18 432 cas ; 9 216 sans D, comme le script du brouillon 8) :
    exactement une ligne par cas, 0 trou, 0 chevauchement hors gardes et L6 (même règle que `grille_l_t07_brouillon8.main`) ;
    lève `GardeArret` sinon ; rend les effectifs par ligne."""
    effectifs = {l: 0 for l in ORDRE}
    total = 0
    for d in (D if avec_d else ("non vide",)):
        for cas in product(G, P, A, ETATS, ETATS, F):
            total += 1
            effectifs[ligne_applicable(*cas, d)] += 1
    sous_a4a5 = sum(effectifs[l] for l in ("L6", "L4", "L4b", "L5", "L2", "L3"))
    attendu = 2 * len(ETATS) * len(ETATS) * len(F)
    attendu_total = 9216 * (2 if avec_d else 1)
    if sous_a4a5 != attendu or sum(effectifs.values()) != total or total != attendu_total:
        raise GardeArret(f"couverture : {total} cas (attendu {attendu_total}), A4/A5 sous vu {sous_a4a5} (attendu {attendu})")
    return {"cas": total, "effectifs": effectifs, "trous": 0, "chevauchements_hors_gardes_et_L6": 0, "exactement_une_ligne": True,
            "entrees": {"G": list(G), "D": list(D) if avec_d else ["non vide"], "P": list(P), "A": list(A), "etats": list(ETATS),
                        "F": list(F)}}


__all__ = ["AU_DESSUS", "NON_AU_DESSUS", "NON_INTERPRETABLE", "ECHEC", "ETATS_SONDE", "G", "P", "A", "ETATS", "F", "D", "ORDRE",
           "ORDRE_BROUILLON8", "SANS_OBJET_ISSUE", "PHRASES", "ISSUES_P3BIS", "EN_ATTENTE_T06", "SANS_OBJET", "separation",
           "etat_pour_sonde", "etat_organisme", "etat_d", "regles", "premiere", "ligne_applicable", "issue_critere_3",
           "enumerer_couverture"]
