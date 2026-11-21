"""Phrases gelées de la **seconde passe** : phrase de tête, phrases permises du critère d'identité recopiées, verdict
d'ensemble, phrases de notre R, de notre S et des comparaisons entre lentilles ; refus des paraphrases interdites.

Texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (`a2bbed7a…`), « Critères de lecture gelés », partie de la seconde
passe ; « Entrées », condition de lecture. Les phrases permises du critère d'identité (CI, § 5) sont des **constantes**
recopiées du texte scellé ; un essai compare chacune, octet pour octet, au texte du préenregistrement. Seuls se remplissent,
d'après la fiche de rangement, les crochets « [R | S] », « (empreinte …) » ou « (empreintes …) », les crochets de chiffres
et le dernier crochet ; aucun autre mot ne change. Le texte décide, le code suit.

Ce que ce code ne recopie pas, et laisse au lecteur entre crochets : la ligne « Verdict d'ensemble » du verdict de la
tranche, et les mots des réserves (R-a) à (R-e), que le lecteur compare d'abord au verdict de la tranche (plan, point 8).
"""
from __future__ import annotations

import re

from . import comparaisons_lentilles_v1 as co
from . import constantes_v1 as K
from . import constantes_v2 as K2
from . import nos_lentilles_v1 as nl
from . import phrases_v1 as _v1
from . import statistiques_v4 as st
from .constantes_v1 import Arret, Refus

nombre, nom_sonde, phrase_comparaison, phrase_non_lue = _v1.nombre, _v1.nom_sonde, _v1.phrase_comparaison, _v1.phrase_non_lue
NOMS_FAMILLES = _v1.NOMS_FAMILLES
NOMS_LENTILLES = dict(_v1.NOMS_LENTILLES) | {K2.LENTILLE_NOTRE_R: "notre lentille R", K2.LENTILLE_NOTRE_S: "notre lentille S côté entrée"}

# --- phrase de tête de la seconde passe, toujours écrite --------------------------------------------------------------------------------
PHRASE_DE_TETE_V2 = (
    "Lecture descriptive des mêmes directions, à la couche où chaque sonde lit, par la lentille publique côté sortie, par la "
    "lentille des logits, et par nos lentilles : notre lentille R côté sortie et notre lentille S côté entrée, ajustées par "
    "nous sur Llama 3.1 8B Instruct avec le code public `stdlogits/neuron-lens`, sur 932 documents de 128 jetons du corpus "
    "DCLM. Notre R se lit comme la lentille publique : les directions des sondes y sont lues comme des directions écrites "
    "dans le flux. Notre S dit quels jetons d'entrée font monter, en moyenne linéarisée sur son corpus d'ajustement, le score "
    "de chaque direction ; elle ne dit pas ce que la sonde fait sur un épisode. Ni l'une ni l'autre ne dit rien de la "
    "détection du sabotage. Ce texte de lecture a été scellé après le verdict de l'apprentissage des sondes sur la tâche ; "
    "cette exposition est déclarée.")

# --- phrases permises du critère d'identité (CI, § 5), recopiées du texte scellé, crochets compris ---------------------------------------
CI_DEUX_AU_PREMIER_PALIER = (
    "Les fichiers d'ajustement réajustés sont identiques à l'octet à ceux du 18 novembre (empreintes …) ; les mesures du 18"
    " novembre décrivent ces lentilles.")
CI_UNE_AU_PREMIER_PALIER = (
    "Le fichier d'ajustement réajusté de la lentille [R | S] est identique à l'octet à celui du 18 novembre (empreinte …) ;"
    " les mesures du 18 novembre faites sur cette lentille la décrivent.")
CI_DEUX_AU_DEUXIEME_PALIER = (
    "Les deux lentilles mesurées le 18 novembre ont été détruites avec la machine louée. Nous les avons réajustées avec le "
    "même code d'ajustement, le même corpus et les mêmes graines sur une autre machine. Les fichiers obtenus ne sont pas "
    "identiques à l'octet. Deux comparaisons restent possibles. La différence entre les deux moitiés du corpus, couche par "
    "couche, s'écarte d'au plus [écart mesuré] de celle du 18 novembre (tolérance fixée d'avance, par convention, à 10⁻³) ;"
    " cette grandeur ne voit pas un déplacement commun aux deux moitiés. Pour la lentille R seulement, l'écart maximal de "
    "chaque matrice à la lentille publique et à l'identité change d'au plus [valeur] et [valeur] d'une course à l'autre, "
    "pour des écarts qui valaient de [valeur] à [valeur] le 18 novembre ; aucun seuil n'était fixé d'avance pour ces deux "
    "séries, et ces changements sont un plancher, non un plafond, de l'écart maximal, entrée par entrée, entre les matrices"
    " des deux courses. Pour la lentille S, aucune comparaison de ce genre n'existe. Nous ne savons pas si les lentilles "
    "réajustées lisent comme celles du 18 novembre. Les mesures du 18 novembre [n'ont pas été refaites sur elles | ont été "
    "refaites sur elles et sont rapportées à côté].")
CI_R_SEULE_AU_DEUXIEME_PALIER = (
    "La lentille R mesurée le 18 novembre a été détruite avec la machine louée. Nous l'avons réajustée avec le même code "
    "d'ajustement, le même corpus et les mêmes graines sur une autre machine. Le fichier obtenu n'est pas identique à "
    "l'octet. La différence entre les deux moitiés du corpus, couche par couche, s'écarte d'au plus [écart mesuré] de celle"
    " du 18 novembre (tolérance fixée d'avance, par convention, à 10⁻³) ; cette grandeur ne voit pas un déplacement commun "
    "aux deux moitiés. L'écart maximal de chaque matrice à la lentille publique et à l'identité change d'au plus [valeur] "
    "et [valeur] d'une course à l'autre, pour des écarts qui valaient de [valeur] à [valeur] le 18 novembre ; aucun seuil "
    "n'était fixé d'avance pour ces deux séries, et ces changements sont un plancher, non un plafond, de l'écart maximal, "
    "entrée par entrée, entre les matrices des deux courses. Nous ne savons pas si la lentille réajustée lit comme celle du"
    " 18 novembre. Les mesures du 18 novembre [n'ont pas été refaites sur elle | ont été refaites sur elle et sont "
    "rapportées à côté].")
PHRASE_DES_DEUX_SERIES = CI_R_SEULE_AU_DEUXIEME_PALIER[CI_R_SEULE_AU_DEUXIEME_PALIER.index("L'écart maximal de chaque matrice"):
                                                       CI_R_SEULE_AU_DEUXIEME_PALIER.index("Nous ne savons pas")].rstrip()
REMPLACEMENT_POUR_S = "Aucune autre comparaison n'existe pour cette lentille."
# CI, § 5 : « la même phrase, « La lentille S… », où la phrase des deux séries […] est remplacée par « Aucune autre comparaison
# n'existe pour cette lentille. » » : construite par cette règle ; l'essai la compare à celle que le texte écrit en entier.
CI_S_SEULE_AU_DEUXIEME_PALIER = CI_R_SEULE_AU_DEUXIEME_PALIER.replace("La lentille R mesurée", "La lentille S mesurée").replace(
    PHRASE_DES_DEUX_SERIES, REMPLACEMENT_POUR_S)
CI_AUTRE_VERDICT = "Lentille [R | S] : verdict d'identité « [libellé exact] » ; elle n'est pas lue ici."
FORMES_CI = {"deux au premier palier": CI_DEUX_AU_PREMIER_PALIER, "une seule au premier palier": CI_UNE_AU_PREMIER_PALIER,
             "deux au deuxième palier": CI_DEUX_AU_DEUXIEME_PALIER, "R seule au deuxième palier": CI_R_SEULE_AU_DEUXIEME_PALIER,
             "S seule au deuxième palier": CI_S_SEULE_AU_DEUXIEME_PALIER, "tout autre verdict": CI_AUTRE_VERDICT}
CROCHET_REFAITES = {"elle": ("[n'ont pas été refaites sur elle | ont été refaites sur elle et sont rapportées à côté]",
                             "n'ont pas été refaites sur elle", "ont été refaites sur elle et sont rapportées à côté"),
                    "elles": ("[n'ont pas été refaites sur elles | ont été refaites sur elles et sont rapportées à côté]",
                              "n'ont pas été refaites sur elles", "ont été refaites sur elles et sont rapportées à côté")}
PHRASE_SANS_MESURE = nl.PHRASE_SANS_MESURE
NOTE_DERNIER_CROCHET = ("phrase permise du deuxième palier non écrite : la fiche de rangement et le registre ne permettent pas de "
                        "dire si les mesures du 18 novembre ont été refaites et lues (note du code, non une phrase gelée)")

# --- paraphrases interdites (CI, § 5) -------------------------------------------------------------------------------------------------------
PARAPHRASES_INTERDITES = (r"\béquivalentes?\b", r"\bproches?\b", r"la même à la précision près", r"couvertes? par concordance",
                          r"\brattachées?\b", r"réajustées? à l'identique")
_RE_INTERDITES = [re.compile(m, re.IGNORECASE) for m in PARAPHRASES_INTERDITES]


def exiger_sans_paraphrase_interdite(texte: str) -> str:
    """Aucune phrase interdite de CI, § 5, ni paraphrase, dans une sortie du code : refus d'écrire."""
    for motif in _RE_INTERDITES:
        m = motif.search(texte)
        if m:
            raise Refus(f"phrase interdite du critère d'identité dans une sortie du code (« {m.group(0)} ») : refus d'écrire")
    return texte


def nombre_de_la_fiche(x) -> str:
    """Chiffre de la fiche, tel quel, sans aucun qualificatif : notation à trois chiffres significatifs, virgule décimale."""
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise Arret("chiffre de la fiche de rangement absent ou d'une autre forme : arrêt (crochets obligatoires)")
    return f"{x:.3g}".replace(".", ",")


# --- phrases permises, forme choisie d'après le couple des deux verdicts --------------------------------------------------------------------
def formes_des_phrases_permises(conditions: dict) -> dict:
    """Forme de la phrase permise de chaque lentille, d'après le couple des deux verdicts : `{lettre: forme}` ; une lentille
    sans verdict n'a pas de phrase (`None`). La forme au pluriel ne s'emploie que si les **deux** lentilles sont au même
    palier."""
    p = {l: conditions[l].palier for l in K2.NOS_LENTILLES}
    formes = {}
    for l in K2.NOS_LENTILLES:
        autre = "S" if l == "R" else "R"
        if conditions[l].verdict is None:
            formes[l] = None
        elif p[l] == 1:
            formes[l] = "deux au premier palier" if p[autre] == 1 else "une seule au premier palier"
        elif p[l] == 2:
            formes[l] = "deux au deuxième palier" if p[autre] == 2 else f"{l} seule au deuxième palier"
        else:
            formes[l] = "tout autre verdict"
    return formes


def exiger_forme(forme: str, lettre: str, conditions: dict) -> None:
    """Refus d'écrire une forme qui ne convient pas au couple des verdicts (par exemple la forme au pluriel alors qu'une
    seule lentille est à ce palier)."""
    if formes_des_phrases_permises(conditions).get(lettre) != forme:
        raise Refus(f"phrase permise : la forme « {forme} » ne convient pas au verdict de la lentille {lettre} et de l'autre : "
                    "refus d'écrire")


def dernier_crochet(course: str, lecture_seconde_course_inscrite: bool) -> bool | None:
    """Vrai : « ont été refaites […] et sont rapportées à côté » (course rejouée menée en entier, et sa lecture inscrite) ;
    faux : « n'ont pas été refaites » (ajustement seul, ou seconde course incomplète) ; `None` : ni l'un ni l'autre ne peut
    être écrit sans risque d'être faux (fiche muette ; course menée en entier dont la lecture n'est pas inscrite)."""
    if course in (nl.COURSE_AJUSTEMENT_SEUL, nl.COURSE_REJOUEE_INCOMPLETE):
        return False
    if course == nl.COURSE_REJOUEE and lecture_seconde_course_inscrite:
        return True
    return None


def _remplir_deuxieme_palier(gabarit: str, lettres: tuple, conditions: dict, refaites: bool) -> str:
    chiffres = {l: conditions[l].chiffres for l in lettres}
    ecart = max(c.get("ecart_max_abs_diffs_float64") if isinstance(c.get("ecart_max_abs_diffs_float64"), (int, float)) else float("nan")
                for c in chiffres.values())
    texte = gabarit.replace("[écart mesuré]", nombre_de_la_fiche(ecart))
    if "R" in lettres:
        series = chiffres["R"].get("series_export_R_sans_critere") or {}
        try:
            a, b = (series[s]["ecart_max_abs"] for s in nl.SERIES_R)
            bas, haut = min(series[s]["ref_min"] for s in nl.SERIES_R), max(series[s]["ref_max"] for s in nl.SERIES_R)
        except (KeyError, TypeError):
            raise Arret("chiffres des deux séries de notre R absents de la fiche : arrêt (crochets obligatoires)") from None
        for valeur in (a, b, bas, haut):
            texte = texte.replace("[valeur]", nombre_de_la_fiche(valeur), 1)
    pronom = "elles" if len(lettres) == 2 else "elle"
    crochet, non, oui = CROCHET_REFAITES[pronom]
    texte = texte.replace(crochet, oui if refaites else non)
    if "[" in texte:
        raise Arret("phrase permise du deuxième palier : un crochet n'a pas été rempli : arrêt")
    return texte


def phrases_permises(conditions: dict, fiche: dict, course: str, lecture_seconde_course_inscrite: bool) -> list[dict]:
    """Pour chacune de nos deux lentilles, la phrase que CI, § 5, donne à son verdict, recopiée mot pour mot, dans la forme de
    son cas ; une lentille non lue reçoit quand même la phrase de son verdict, suivie de sa ligne « Non lue […] ». La phrase du
    déclencheur (vi), si la fiche la porte pour notre R, suit la phrase permise, mot pour mot."""
    formes = formes_des_phrases_permises(conditions)
    refaites = dernier_crochet(course, lecture_seconde_course_inscrite)
    sortie, faites = [], set()
    for lettre in K2.NOS_LENTILLES:
        forme, cond = formes[lettre], conditions[lettre]
        if forme is None:
            sortie.append({"lentilles": [lettre], "forme": None, "phrases": [], "non_lue": cond.motif})
            continue
        if forme in faites:
            continue
        exiger_forme(forme, lettre, conditions)
        lettres = K2.NOS_LENTILLES if forme.startswith("deux") else (lettre,)
        ligne = {"lentilles": list(lettres), "forme": forme, "phrases": [], "notes": []}
        gabarit = FORMES_CI[forme]
        if forme == "deux au premier palier":
            faites.add(forme)
            empreintes = ", ".join(fiche["lentilles"][l]["sha256_relecture"] for l in lettres)
            ligne["phrases"].append(gabarit.replace("(empreintes …)", f"(empreintes {empreintes})"))
        elif forme == "une seule au premier palier":
            ligne["phrases"].append(gabarit.replace("[R | S]", lettre).replace(
                "(empreinte …)", f"(empreinte {fiche['lentilles'][lettre]['sha256_relecture']})"))
        elif forme == "tout autre verdict":
            ligne["phrases"].append(gabarit.replace("[R | S]", lettre).replace("[libellé exact]", cond.verdict))
        else:
            faites.add(forme) if forme.startswith("deux") else None
            if refaites is None:
                ligne["notes"].append(NOTE_DERNIER_CROCHET)
            else:
                ligne["phrases"].append(_remplir_deuxieme_palier(gabarit, lettres, conditions, refaites))
                if "R" in lettres and conditions["R"].phrase_vi:
                    ligne["phrases"].append(conditions["R"].phrase_vi)
                if refaites is False:
                    ligne["phrases"].append(PHRASE_SANS_MESURE)
        ligne["non_lues"] = [conditions[l].motif for l in lettres if conditions[l].motif]
        for phrase in ligne["phrases"]:
            exiger_sans_paraphrase_interdite(phrase)
        sortie.append(ligne)
    return sortie


def ligne_du_verdict_d_identite(conditions: dict, course: str) -> str:
    """« Verdict d'identité : notre R : […] ; notre S : […]. Course du réajustement : […]. »"""
    def un(lettre: str) -> str:
        c = conditions[lettre]
        return c.verdict if c.verdict is not None else c.motif[0].lower() + c.motif[1:]
    return f"Verdict d'identité : notre R : {un('R')} ; notre S : {un('S')}. Course du réajustement : {course}."


# --- verdict d'ensemble de la tranche et réserves -----------------------------------------------------------------------------------------
LIGNE_DE_V = (f"[ligne « Verdict d'ensemble » à recopier par le lecteur, telle quelle, de {K2.VERDICT_TRANCHE}, empreinte "
              f"{K2.EMPREINTE_VERDICT_TRANCHE} ; empreinte différente : « ligne non recopiée : empreinte »]")
RESERVES_DES_DEUX = "[les réserves (R-a) à (R-e) de « Hypothèse », vérifiées contre V par le lecteur, plan, point 8]"
RESERVES_DE = {"R": "[(R-a) pour la lecture contre pilotage, (R-b), (R-c) et (R-e) ; vérifiées contre V par le lecteur, plan, point 8]",
               "S": "[(R-d) et (R-e) ; vérifiées contre V par le lecteur, plan, point 8]"}
PHRASE_DOMAINE_D_USAGE = ("Domaine d'usage : le code voisin donne la lecture côté entrée par S pour les premières couches (jusqu'à "
                          "la couche 8 de son modèle de 36 couches) ; les couches 15 et 23 sont hors de ce domaine, la couche 7 à "
                          "son bord ; la cible lue ici n'a aucune mesure de fidélité.")


def _mesures_du_deuxieme_palier(course: str, fiche: dict, lettres: tuple) -> str:
    if course == nl.COURSE_REJOUEE:
        seconde = fiche.get("lecture_seconde_course") or {}
        limites = " ; ".join(f"notre lentille {l}, couche {c} : {(fiche['lentilles'][l].get('seconde_course_par_couche') or {}).get(str(c), {}).get('limite')}"
                             for l in lettres for c in K.COUCHES)
        return f"Ses mesures sont celles de la seconde course : {seconde.get('ligne_d_ensemble')} ; {limites}."
    return PHRASE_SANS_MESURE


def lignes_du_verdict_d_ensemble(conditions: dict, fiche: dict, course: str) -> list[dict]:
    """Lignes du verdict d'ensemble de la tranche, selon les paliers des lentilles **lues** :
    - nos deux lentilles au premier palier : une ligne, réserves (R-a) à (R-e) ;
    - une seule au premier palier : la forme « ne se transportent pas tels quels », et les seules réserves de la lentille ;
    - deuxième palier : « Ce verdict ne se transporte pas à la lentille lue ici. », mesures de la seconde course ou phrase
      gelée, puis le rappel de contexte ;
    - une lentille à chaque palier : **les deux lignes**, chacune nommant sa lentille ; la ligne du deuxième palier ne porte
      que les réserves de sa lentille."""
    lues = {l: conditions[l].palier for l in K2.NOS_LENTILLES if conditions[l].lue}
    premier = tuple(l for l, p in lues.items() if p == 1)
    deuxieme = tuple(l for l, p in lues.items() if p == 2)
    lignes = []
    if len(premier) == 2:
        texte = f"Verdict d'ensemble de la tranche de nos lentilles : {LIGNE_DE_V}."
        seconde = fiche.get("lecture_seconde_course")
        if isinstance(seconde, dict) and seconde.get("ligne_d_ensemble"):
            texte += (f" Ligne d'ensemble de la lecture de la seconde course, recopiée de la fiche : {seconde['ligne_d_ensemble']} "
                      "[si elle diffère de la ligne de V : « désaccord entre les deux mesures de la tranche, nœud de Lazar »].")
        texte += f" Réserves sur nos lentilles à ces couches : {RESERVES_DES_DEUX}."
        lignes.append({"palier": 1, "lentilles": list(premier), "texte": texte, "reserves": "(R-a) à (R-e)"})
    elif len(premier) == 1:
        l = premier[0]
        lignes.append({"palier": 1, "lentilles": [l], "reserves": RESERVES_DE[l], "texte": (
            f"Verdict d'ensemble de la tranche sur les deux lentilles du 18 novembre : {LIGNE_DE_V}. Ce verdict d'ensemble et les "
            f"conditions communes aux deux lentilles ne se transportent pas tels quels : seules les mesures faites sur notre "
            f"lentille {l} la décrivent. Réserves qui portent sur notre lentille {l} à ces couches : {RESERVES_DE[l]}.")})
    if deuxieme:
        mixte = bool(premier)
        qui = f"notre lentille {deuxieme[0]}" if mixte else "la lentille lue ici"
        reserves = RESERVES_DE[deuxieme[0]] if mixte else "[(R-a) à (R-e)]"
        lignes.append({"palier": 2, "lentilles": list(deuxieme), "reserves": reserves, "texte": (
            f"Verdict d'ensemble de la tranche sur les lentilles du 18 novembre, détruites : {LIGNE_DE_V}. Ce verdict ne se "
            f"transporte pas à {qui}. {_mesures_du_deuxieme_palier(course, fiche, deuxieme)} Mesures faites le 18 novembre sur "
            f"des lentilles détruites, rappelées pour contexte ; elles ne décrivent pas {'notre lentille ' + deuxieme[0] if mixte else 'la lentille lue'} : "
            f"{reserves}.")})
    exiger_lignes_du_verdict_d_ensemble(lignes, lues)
    for ligne in lignes:
        exiger_sans_paraphrase_interdite(ligne["texte"])
    return lignes


def exiger_lignes_du_verdict_d_ensemble(lignes: list[dict], paliers_des_lentilles_lues: dict) -> None:
    """Refus : une seule ligne écrite quand une de nos lentilles est au premier palier et l'autre au deuxième ; ou la liste
    entière des réserves (R-a) à (R-e) sur une ligne qui ne décrit qu'une lentille de ce cas."""
    paliers = set(paliers_des_lentilles_lues.values())
    if paliers == {1, 2}:
        if len(lignes) != 2 or {l["palier"] for l in lignes} != {1, 2}:
            raise Refus("verdict d'ensemble : une lentille à chaque palier exige les deux lignes, chacune nommant sa lentille : "
                        "refus d'écrire")
        for ligne in lignes:
            lettre = ligne["lentilles"][0]
            if len(ligne["lentilles"]) != 1 or f"notre lentille {lettre}" not in ligne["texte"] or ligne["reserves"] != RESERVES_DE[lettre]:
                raise Refus("verdict d'ensemble : une ligne ne nomme pas sa lentille, ou porte d'autres réserves que les siennes "
                            "(la liste entière (R-a) à (R-e) n'y a pas sa place) : refus d'écrire")
    elif len(lignes) != len(paliers):
        raise Refus("verdict d'ensemble : nombre de lignes différent du nombre de paliers des lentilles lues : refus d'écrire")


# --- reproduction, nœuds, non-lectures ---------------------------------------------------------------------------------------------------------
PHRASE_REPRODUCTION = "Reproduction de la première passe : {n}."
PHRASE_CODE_DIFFERENT = "code de lecture différent de celui de la première passe : {modules}"
PHRASE_REPRODUCTION_NON_FAITE = ("Reproduction de la première passe : non faite, première passe lancée et non achevée ; aucune "
                                 "phrase de la lentille publique ni de la lentille des logits n'est écrite ici avant le nœud de la "
                                 "v1.")
NOTE_PREMIERE_PASSE_REMPLACEE = ("première passe jamais lancée : la seconde passe la remplace pour la lentille publique et la lentille "
                                 "des logits ; aucune lecture humaine de la lentille publique n'a eu lieu avant (note du code)")


def phrases_de_la_reproduction(reproduction: dict, modules_differents: tuple) -> list[str]:
    from . import reproduction_v1 as rp
    if reproduction["etat"] == rp.ETAT_NON_FAITE:
        return [PHRASE_REPRODUCTION_NON_FAITE]
    code = PHRASE_CODE_DIFFERENT.format(modules=", ".join(modules_differents)) if modules_differents else None
    if reproduction["etat"] == rp.ETAT_REMPLACEE:
        return [NOTE_PREMIERE_PASSE_REMPLACEE] + ([code] if code else [])
    n = reproduction["nombre_de_lectures_differentes"]
    return [PHRASE_REPRODUCTION.format(n="aucune" if not n else n)] + ([code] if code else [])


def phrase_independance_non_tenue(couches_lentilles: list) -> str | None:
    """La même phrase que la première passe, si la garde du rapport à ε a imposé des nuls par direction."""
    if not couches_lentilles:
        return None
    ou = ", ".join(f"couche {c} ({NOMS_LENTILLES[l]})" for c, l in sorted(couches_lentilles))
    return f"Indépendance à la norme non tenue à {ou} : nuls isotropes refaits par direction."


def tete(conditions: dict, fiche: dict, course: str, lecture_seconde_course_inscrite: bool, reproduction: dict,
         modules_differents: tuple, phrases_des_noeuds: list, independance_non_tenue: list | None = None) -> dict:
    """La tête de la seconde passe, dans l'ordre du texte."""
    non_lues = [c.motif for c in (conditions[l] for l in K2.NOS_LENTILLES) if c.motif]
    non_lues += [case["motif"] for l in K2.NOS_LENTILLES if conditions[l].lue for case in conditions[l].couches.values()
                 if case.get("motif")]
    sortie = {"issue_des_noeuds": list(phrases_des_noeuds), "phrase_de_tete": PHRASE_DE_TETE_V2,
              "verdict_d_identite": ligne_du_verdict_d_identite(conditions, course),
              "phrases_permises": phrases_permises(conditions, fiche, course, lecture_seconde_course_inscrite),
              "verdict_d_ensemble": lignes_du_verdict_d_ensemble(conditions, fiche, course),
              "domaine_d_usage": PHRASE_DOMAINE_D_USAGE if conditions["S"].lue else None,
              "non_lues": non_lues, "reproduction": phrases_de_la_reproduction(reproduction, modules_differents),
              "independance_a_la_norme": phrase_independance_non_tenue(independance_non_tenue or [])}
    exiger_sans_paraphrase_interdite(sortie["verdict_d_identite"])
    for texte in non_lues:
        exiger_sans_paraphrase_interdite(texte)
    return sortie


# --- renvois aux réserves (règles de la seconde passe) ---------------------------------------------------------------------------------------
RENVOI_NON_REFAITE = "mesurée sur la lentille du 18 novembre, non refaite sur la lentille lue"


def renvois(lentille: str, couche: int, palier: int | None, ligne_de_la_seconde_course: str | None = None) -> list[str]:
    """Aux couches 7 et 15, toute phrase sur notre R porte en renvoi la réserve (R-c) ; toute phrase sur notre S porte en
    renvoi les réserves (R-d) et (R-u). Au deuxième palier, chaque renvoi à une réserve tirée de V ajoute « mesurée sur la
    lentille du 18 novembre, non refaite sur la lentille lue », ou, si la lecture de la seconde course est scellée, renvoie à
    sa ligne. (R-u), indépendante de V, ne reçoit pas cet ajout."""
    if lentille == K2.LENTILLE_NOTRE_R:
        tirees = ["(R-c)"] if int(couche) in (7, 15) else []
        autres = []
    elif lentille == K2.LENTILLE_NOTRE_S:
        tirees, autres = ["(R-d)"], ["(R-u)"]
    else:
        return []
    if palier == 2:
        suite = f"voir la lecture de la seconde course : {ligne_de_la_seconde_course}" if ligne_de_la_seconde_course else RENVOI_NON_REFAITE
        tirees = [f"{r} — {suite}" for r in tirees]
    return tirees + autres


# --- phrases par direction ---------------------------------------------------------------------------------------------------------------------
def _p(p_iso: float, p_signes: float) -> str:
    return f"p {nombre(p_iso)} et {nombre(p_signes)}"


def _jetons(jetons: list) -> str:
    return ", ".join(repr(j) for j in jetons)


def phrase_direction(lentille: str, sonde: str, couche: int, signe: str, libelle: str, concentration: float, p_iso: float,
                     p_signes: float, jetons: list) -> str:
    """Lentille publique, lentille des logits, notre R : les phrases gelées de la première passe, avec [lentille] ; notre S :
    ses phrases propres (« font monter », jamais « la sonde détecte »)."""
    if lentille not in NOMS_LENTILLES:
        raise Arret(f"lentille {lentille!r} inconnue")
    if lentille != K2.LENTILLE_NOTRE_S:
        tete_ = f"Par {NOMS_LENTILLES[lentille]}, la direction de {sonde} (couche {couche}, signe {signe})"
        if libelle == st.LIBELLE_CONCENTREE:
            return (f"{tete_} se distingue des deux nuls (concentration {nombre(concentration)} ; {_p(p_iso, p_signes)}) ; ses "
                    f"premiers jetons : {_jetons(jetons)}.")
        if libelle == st.LIBELLE_INTERMEDIAIRE:
            return (f"{tete_} ne se distingue des nuls qu'en partie ({_p(p_iso, p_signes)}) : ses premiers jetons sont rapportés, "
                    "sans être nommés comme ce qu'elle capte.")
        if libelle == st.LIBELLE_NON_DISTINCTE:
            return (f"{tete_} ne se distingue pas du nul ({_p(p_iso, p_signes)}) : ses jetons sont en table, et aucune phrase ne "
                    "les nomme comme ce qu'elle capte.")
        raise Arret(f"libellé {libelle!r} inconnu")
    ou = f"la direction de {sonde} (couche {couche}, signe {signe})"
    if libelle == st.LIBELLE_CONCENTREE:
        return (f"Par notre lentille S côté entrée, les jetons d'entrée qui font monter en moyenne {ou} se distinguent des deux "
                f"nuls (concentration {nombre(concentration)} ; {_p(p_iso, p_signes)}) ; ces jetons : {_jetons(jetons)}.")
    if libelle == st.LIBELLE_INTERMEDIAIRE:
        return (f"Par notre lentille S côté entrée, {ou} ne se distingue des nuls qu'en partie ({_p(p_iso, p_signes)}) : ses "
                "premiers jetons d'entrée sont rapportés, sans être nommés comme ce qui la fait monter.")
    if libelle == st.LIBELLE_NON_DISTINCTE:
        return (f"Par notre lentille S côté entrée, {ou} ne se distingue pas du nul ({_p(p_iso, p_signes)}) : ses jetons d'entrée "
                "sont en table, et aucune phrase ne les nomme.")
    raise Arret(f"libellé {libelle!r} inconnu")


def phrase_famille(lentille: str, vecteur: str, couche: int, famille: str, n: int, attendu: float, p_iso: float, p_signes: float,
                   sur_representee: bool) -> str:
    """Famille sur-représentée ou non. Par notre S : phrase de `w` et phrase de `q` distinctes à la couche 7 ; aux couches 15
    et 23, « rapporté sans conclusion » (le mot « soupçon » ne s'emploie pour notre S qu'à la couche 7)."""
    if lentille != K2.LENTILLE_NOTRE_S:
        return _v1.phrase_famille(famille, n, attendu, p_iso, p_signes, sur_representee)
    nom, objet = NOMS_FAMILLES[famille]
    if not sur_representee:
        return (f"La famille {nom} n'est pas sur-représentée parmi ses jetons d'entrée par notre lentille S ({n} ; "
                f"{_p(p_iso, p_signes)}) : cela ne blanchit pas la sonde.")
    chiffres = f"(attendu sous le nul {nombre(attendu)} ; {_p(p_iso, p_signes)})"
    if int(couche) != 7:
        return (f"La famille {nom} paraît {n} fois dans ses vingt premiers jetons d'entrée par notre lentille S {chiffres} : "
                f"rapporté sans conclusion, la couche {couche} étant hors du domaine d'usage de la lecture côté entrée.")
    if vecteur == "w":
        return (f"La famille {nom} paraît {n} fois dans ses vingt premiers jetons d'entrée par notre lentille S {chiffres} : la "
                f"lecture ajoute un soupçon que la sonde monte avec {objet} dans le texte qu'elle lit ; elle ne le prouve pas.")
    if vecteur == "q":
        return (f"La famille {nom} paraît {n} fois dans les vingt premiers jetons d'entrée de la requête par notre lentille S "
                f"{chiffres} : la lecture ajoute un soupçon que l'attention de la sonde se porte sur les positions où paraît "
                f"{objet} ; elle ne le prouve pas.")
    raise Arret(f"vecteur {vecteur!r} inconnu")


def phrase_poles(lentille: str, libelle: str, poles: list, p_iso: float, p_signes: float, jetons_par_pole: list) -> str | None:
    """Pôles : la phrase de la première passe ; pour notre R : « …; notre lentille R les lit : [jetons par pôle] ». Notre S ne
    lit pas les pôles."""
    if lentille == K2.LENTILLE_NOTRE_S:
        raise Arret("notre S ne lit pas les pôles (directions d'écriture, non des covecteurs de lecture)")
    phrase = _v1.phrase_poles(libelle, poles, p_iso, p_signes, jetons_par_pole)
    if phrase is None or lentille == K.LENTILLE_PUBLIQUE:
        return phrase
    if lentille != K2.LENTILLE_NOTRE_R:
        raise Arret(f"les pôles ne sont lus que par la lentille publique et par notre R ({lentille!r})")
    return phrase.replace("; la lentille publique les lit :", "; notre lentille R les lit :")


def phrase_comparaison_entre_lentilles(direction: str, couche: int, signe: str, comparaison: dict) -> str:
    """Les quatre libellés entre les deux lentilles R, et « non calculable ». `comparaison` : `libelle`, et selon le cas
    `lentille`/`autre`, `libelles` (publique, notre R), `recouvrement`, `mediane`, `p` (isotrope, signes), `moities`, `motif`."""
    libelle = comparaison["libelle"]
    if libelle == co.NON_CALCULABLE:
        return f"Comparaison entre lentilles non faite pour {direction} : {comparaison['motif']}."
    ou = f"la direction de {direction} (couche {couche}, signe {signe})"
    o, m = comparaison["recouvrement"], nombre(comparaison["mediane"])
    if libelle == co.LECTURE_COMMUNE:
        return (f"La lecture de {ou} tient d'une lentille R à l'autre : les deux la distinguent des nuls, et leurs vingt premiers "
                f"jetons se recouvrent de {o} sur vingt (médiane des directions nulles : {m} sur vingt ; {_p(*comparaison['p'])} ; "
                f"les deux moitiés de notre R : {comparaison['moities']} sur vingt). Deux lentilles R, deux corpus, un seul "
                "modèle : cela ne dit pas que toute lentille lirait de même.")
    if libelle == co.LECTURE_PROPRE:
        une, autre = NOMS_LENTILLES[comparaison["lentille"]], NOMS_LENTILLES[comparaison["autre"]]
        return (f"La lecture de {ou} ne tient pas d'une lentille R à l'autre : {une} la distingue des nuls, {autre} non "
                f"(recouvrement {o} sur vingt ; médiane des directions nulles : {m} sur vingt ; les deux moitiés de notre R : "
                f"{comparaison['moities']} sur vingt). Ce que {une} lui associe est en table, sans être tenu pour ce que la "
                "direction pousse.")
    if libelle == co.DEUX_NON_DISTINCTES:
        return (f"Aucune des deux lentilles R ne distingue {ou} des nuls (recouvrement {o} sur vingt ; médiane des directions "
                f"nulles : {m} sur vingt).")
    if libelle == co.MIXTE:
        a, b = comparaison["libelles"]
        return (f"Lecture de {ou} par les deux lentilles R : {a} et {b} ; recouvrement {o} sur vingt (médiane des directions "
                f"nulles : {m} sur vingt ; {_p(*comparaison['p'])}) : rapporté sans conclusion.")
    raise Arret(f"libellé de comparaison {libelle!r} inconnu")


PORTE_UNE_PHRASE = ("concentration", "part au-dessus du nul", "familles", "pôles", "comparaison appariée",
                    "les quatre libellés entre les deux lentilles R")
RESTE_EN_TABLE = ("corrélations des scores", "paire (notre R, lentille des logits)", "recouvrement des deux moitiés",
                  "témoin de couche", "différence des deux recouvrements", "jetons communs par pôle",
                  "référence « plongements seuls »")
