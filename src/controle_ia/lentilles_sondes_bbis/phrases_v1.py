"""Phrases gelées (texte scellé, « Critères de lecture gelés »), rendues mécaniquement à partir des tables.

Les phrases sont recopiées du texte, mot pour mot ; seuls les crochets sont remplis. Aucune phrase ne nomme les jetons d'une
lecture « non distincte du nul » ou « intermédiaire » comme ce que la direction capte ; le mot « soupçon » ne paraît que pour
une famille sur-représentée.
"""
from __future__ import annotations

from . import constantes_v1 as K
from . import statistiques_v1 as st
from .constantes_v1 import Arret

PHRASE_DE_TETE = (
    "Lecture descriptive, par la lentille publique côté sortie (lentille R de Llama 3.1 8B Instruct publiée par Neuronpedia, "
    "ajustée par un tiers sur 64 textes de WikiText), des directions des sondes apprises sur la tâche et des lecteurs honnêtes "
    "de même recette, à la couche où chaque sonde lit. Ce n'est pas notre lentille ajustée. Les directions des sondes sont des "
    "vecteurs de lecture ; elles sont lues ici comme des directions écrites dans le flux : la lecture dit ce que la lentille "
    "associe à un tel vecteur écrit, non ce que la sonde lit. Elle dit quels jetons et quels pôles la lentille associe à chaque "
    "direction ; elle ne dit rien de la détection du sabotage, qui appartient au verdict de l'apprentissage des sondes sur la "
    "tâche, ni de ce qu'une sonde fait sur un épisode.")
# La ligne du verdict d'ensemble de la tranche des lentilles publiques est recopiée par le lecteur, non par ce code.
SUITE_VERDICT_LENTILLES = ("Verdict d'ensemble de la tranche des lentilles publiques sur cette lentille : [ligne à recopier par "
                           "le lecteur, telle quelle, de docs/notes/neuron-lens-v1/lecture-b-alpha/verdict-b-alpha-v1.md, empreinte "
                           "ca06acb1550ccc76fef1ec89ae0aec170c5f05252bda2711f131eaa0e645fc1d ; empreinte différente : « ligne non "
                           "recopiée : empreinte »].")
NOMS_LENTILLES = {K.LENTILLE_PUBLIQUE: "la lentille publique côté sortie", K.LENTILLE_LOGITS: "la lentille des logits"}
NOMS_CELLULES = {"P-instruit": "l'organisme à consigne cachée", "P-S25": "l'adaptateur saboteur à la dose 0,25",
                 "P-S50": "l'adaptateur saboteur à la dose 0,5", "P-S75": "l'adaptateur saboteur à la dose 0,75",
                 "P-S100": "l'adaptateur saboteur à la dose 1"}
NOMS_VECTEURS = {"w": "vecteur de score", "q": "requête d'attention"}
NOMS_FAMILLES = {"nombres": ("nombres", "des nombres"), "cout": ("coût", "le coût")}


def nombre(x: float) -> str:
    """Nombre à la française (virgule), forme courte."""
    return f"{x:.4g}".replace(".", ",")


def nom_sonde(cellule: str, pli: str, role: str, vecteur: str) -> str:
    """Nom en clair d'une direction : rôle, cellule, pli, vecteur."""
    if cellule not in NOMS_CELLULES or pli not in K.PLIS or role not in K.ROLES or vecteur not in NOMS_VECTEURS:
        raise Arret(f"direction inconnue : {cellule}/{pli}/{role}/{vecteur}")
    qui = "la sonde apprise sur" if role == "sonde" else "le lecteur honnête de la cellule de"
    return f"{qui} {NOMS_CELLULES[cellule]}, pli {pli} ({NOMS_VECTEURS[vecteur]})"


def phrase_de_tete(couches_lentilles_non_tenues: list[tuple[int, str]] | None = None) -> str:
    """Phrase de tête, toujours écrite ; suivie de la ligne à recopier par le lecteur et, si la garde du rapport à ε a imposé
    des nuls par direction, de la phrase de l'indépendance à la norme."""
    texte = f"{PHRASE_DE_TETE} {SUITE_VERDICT_LENTILLES}"
    if couches_lentilles_non_tenues:
        ou = ", ".join(f"couche {c} ({NOMS_LENTILLES[l]})" for c, l in sorted(couches_lentilles_non_tenues))
        texte += f" Indépendance à la norme non tenue à {ou} : nuls isotropes refaits par direction."
    return texte


def phrase_direction(lentille: str, sonde: str, couche: int, signe: str, libelle: str, concentration: float, p_iso: float,
                     p_signes: float, jetons: list[str]) -> str:
    """Une phrase par libellé (« concentrée au-delà des deux nuls », « intermédiaire », « non distincte du nul »)."""
    tete = f"Par {NOMS_LENTILLES[lentille]}, la direction de {sonde} (couche {couche}, signe {signe})"
    p = f"p {nombre(p_iso)} et {nombre(p_signes)}"
    if libelle == st.LIBELLE_CONCENTREE:
        return (f"{tete} se distingue des deux nuls (concentration {nombre(concentration)} ; {p}) ; ses premiers jetons : "
                f"{', '.join(repr(j) for j in jetons)}.")
    if libelle == st.LIBELLE_INTERMEDIAIRE:
        return (f"{tete} ne se distingue des nuls qu'en partie ({p}) : ses premiers jetons sont rapportés, sans être nommés "
                "comme ce qu'elle capte.")
    if libelle == st.LIBELLE_NON_DISTINCTE:
        return (f"{tete} ne se distingue pas du nul ({p}) : ses jetons sont en table, et aucune phrase ne les nomme comme ce "
                "qu'elle capte.")
    raise Arret(f"libellé {libelle!r} inconnu")


def phrase_famille(famille: str, n: int, attendu: float, p_iso: float, p_signes: float, sur_representee: bool) -> str:
    nom, objet = NOMS_FAMILLES[famille]
    if sur_representee:
        return (f"La famille {nom} paraît {n} fois dans ses vingt premiers jetons (attendu sous le nul {nombre(attendu)} ; p "
                f"{nombre(p_iso)} et {nombre(p_signes)}) : la lecture ajoute un soupçon que la sonde lise {objet} ; elle ne le "
                "prouve pas.")
    return (f"La famille {nom} n'y est pas sur-représentée ({n} ; p {nombre(p_iso)} et {nombre(p_signes)}) : cela ne blanchit "
            "pas la sonde.")


def phrase_poles(libelle: str, poles: list[dict], p_iso: float, p_signes: float,
                 jetons_par_pole: list[list[str]]) -> str | None:
    """Pôles alignés : « concentrés » → phrase qui les nomme ; « non distincts » → « aucun pôle… ». Le texte ne gèle aucune
    phrase pour des pôles « intermédiaires » : rien n'est rendu (les valeurs restent en table)."""
    if libelle == st.LIBELLE_INTERMEDIAIRE:
        return None
    if libelle not in (st.LIBELLE_CONCENTREE, st.LIBELLE_NON_DISTINCTE):
        raise Arret(f"libellé {libelle!r} inconnu")
    if libelle == st.LIBELLE_CONCENTREE:
        noms = ", ".join(f"neurone {p['neurone']} signe {p['signe']}" for p in poles)
        cos = ", ".join(nombre(p["cosinus"]) for p in poles)
        lus = " ; ".join(f"neurone {p['neurone']} signe {p['signe']} : {', '.join(repr(j) for j in js)}"
                         for p, js in zip(poles, jetons_par_pole))
        return (f"Les pôles qui écrivent le plus près de la direction ({noms}, cosinus {cos}) se distinguent des nuls (p "
                f"{nombre(p_iso)} et {nombre(p_signes)}) ; la lentille publique les lit : {lus}.")
    return f"Aucun pôle de la couche n'écrit plus près de la direction que sous le nul (p {nombre(p_iso)} et {nombre(p_signes)})."


def phrase_comparaison(sonde: str, autre: str, cosinus: float | None, jetons_communs: int | None) -> str:
    if cosinus is None:
        return "couches différentes : sans objet"
    return f"Cosinus {nombre(cosinus)} entre {sonde} et {autre} (même couche) ; {jetons_communs} jetons communs sur vingt."


def phrase_non_lue(motif: str) -> str:
    return f"Non lue : {motif}."


MOTIF_SANS_LENTILLE_ENTREE = "aucune lentille côté entrée publique"
