"""Complément de `phrases_v2` pour le lanceur de la seconde passe v2 : trois corrections non bloquantes de la contre-lecture du
code de la seconde passe (`docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-code-seconde-passe-v1.md`,
`0c90e0f6…`). `phrases_v2` n'est pas réécrit (R12) ; toutes ses phrases gelées restent les siennes, mot pour mot, et ce module
n'en ajoute ni n'en change aucune.

- **N2** — verdict d'ensemble, premier palier avec **une seule** de nos lentilles : la ligne d'ensemble de la lecture de la
  seconde course est recopiée à côté de celle du verdict de la tranche, comme pour nos deux lentilles (texte, « Entrées »,
  « Seconde course » : « au premier palier […] si sa lecture est scellée […] sa ligne d'ensemble est recopiée à côté de celle
  de V »). Elle suit la phrase gelée « Ce verdict d'ensemble […] la décrivent. » et précède les réserves, dans l'ordre que le
  texte donne pour nos deux lentilles.
- **N2 bis** — cette ligne n'est recopiée, à tout premier palier, que **si la lecture de la seconde course est inscrite** : le
  lanceur donne la ligne qu'il a relevée (`_ligne_de_la_seconde_course` : ligne `LECTURE-SECONDE-COURSE-NOS-LENTILLES-BBIS`
  inscrite, seconde course menée en entier, ligne d'ensemble portée par la fiche), ou `None` ; la seule présence du champ dans
  la fiche ne suffit plus.
- **N4** — phrase de tête de la reproduction quand l'état de la première passe a changé entre le montage et le calcul de la
  seconde (nœud N-dev-9, option (a) : le sens sévère est gardé, la phrase est corrigée). La phrase gelée « Reproduction de la
  première passe : non faite, première passe lancée et non achevée ; […] avant le nœud de la v1. » n'est plus écrite là où elle
  serait inexacte ; une note du code, qui dit ce qui s'est passé, la remplace :
  - passe en cours au montage et achevée depuis : il n'y a pas de nœud de la v1 (texte, plan, point 11, « Passe encore en
    cours ») ;
  - passe jamais lancée au montage et lancée depuis : elle n'était pas « lancée et non achevée » au montage.
  Dans les deux cas, comme avant, aucune phrase de la lentille publique ni de la lentille des logits n'est écrite par la seconde
  passe et aucune reproduction n'est faite. **Ces lignes dépendent du nœud N-dev-9** : si Lazar tranche autrement, une version
  suivante les portera.
Le texte décide, le code suit.
"""
from __future__ import annotations

from . import constantes_v2 as K2
from . import nos_lentilles_v1 as nl
from . import phrases_v2 as p2
from . import reproduction_v1 as rp

# --- N2 et N2 bis : ligne d'ensemble de la lecture de la seconde course, au premier palier --------------------------------------------------
SUITE_SECONDE_COURSE = (" Ligne d'ensemble de la lecture de la seconde course, recopiée de la fiche : {ligne} [si elle diffère de la "
                        "ligne de V : « désaccord entre les deux mesures de la tranche, nœud de Lazar »].")


def lignes_du_verdict_d_ensemble(conditions: dict, fiche: dict, course: str, ligne_de_la_seconde_course: str | None) -> list[dict]:
    """Les lignes du verdict d'ensemble de `phrases_v2.lignes_du_verdict_d_ensemble`, à deux différences près, au premier
    palier seulement : la ligne d'ensemble de la lecture de la seconde course n'est recopiée que si le lanceur la donne
    (`ligne_de_la_seconde_course` : lecture inscrite au registre propre) ; et elle l'est aussi quand une seule de nos lentilles
    est au premier palier. Le deuxième palier est celui de `phrases_v2`, inchangé."""
    lues = {l: conditions[l].palier for l in K2.NOS_LENTILLES if conditions[l].lue}
    premier = tuple(l for l, p in lues.items() if p == 1)
    deuxieme = tuple(l for l, p in lues.items() if p == 2)
    suite = SUITE_SECONDE_COURSE.format(ligne=ligne_de_la_seconde_course) if ligne_de_la_seconde_course else ""
    lignes = []
    if len(premier) == 2:
        texte = (f"Verdict d'ensemble de la tranche de nos lentilles : {p2.LIGNE_DE_V}.{suite} Réserves sur nos lentilles à ces "
                 f"couches : {p2.RESERVES_DES_DEUX}.")
        lignes.append({"palier": 1, "lentilles": list(premier), "texte": texte, "reserves": "(R-a) à (R-e)"})
    elif len(premier) == 1:
        l = premier[0]
        lignes.append({"palier": 1, "lentilles": [l], "reserves": p2.RESERVES_DE[l], "texte": (
            f"Verdict d'ensemble de la tranche sur les deux lentilles du 18 novembre : {p2.LIGNE_DE_V}. Ce verdict d'ensemble et les "
            f"conditions communes aux deux lentilles ne se transportent pas tels quels : seules les mesures faites sur notre "
            f"lentille {l} la décrivent.{suite} Réserves qui portent sur notre lentille {l} à ces couches : {p2.RESERVES_DE[l]}.")})
    if deuxieme:
        mixte = bool(premier)
        qui = f"notre lentille {deuxieme[0]}" if mixte else "la lentille lue ici"
        reserves = p2.RESERVES_DE[deuxieme[0]] if mixte else "[(R-a) à (R-e)]"
        lignes.append({"palier": 2, "lentilles": list(deuxieme), "reserves": reserves, "texte": (
            f"Verdict d'ensemble de la tranche sur les lentilles du 18 novembre, détruites : {p2.LIGNE_DE_V}. Ce verdict ne se "
            f"transporte pas à {qui}. {p2._mesures_du_deuxieme_palier(course, fiche, deuxieme)} Mesures faites le 18 novembre sur "
            f"des lentilles détruites, rappelées pour contexte ; elles ne décrivent pas {'notre lentille ' + deuxieme[0] if mixte else 'la lentille lue'} : "
            f"{reserves}.")})
    p2.exiger_lignes_du_verdict_d_ensemble(lignes, lues)
    for ligne in lignes:
        p2.exiger_sans_paraphrase_interdite(ligne["texte"])
    return lignes


# --- N4 : phrase de tête de la reproduction quand l'état de la première passe a changé depuis le montage ------------------------------------
NOTE_ACHEVEE_DEPUIS_LE_MONTAGE = (
    "Reproduction de la première passe : non faite ; première passe encore en cours au montage de la seconde passe et achevée "
    "depuis : les phrases de la lentille publique et de la lentille des logits sont celles de la première passe, aucune n'est "
    "écrite ici ; il n'y a pas de nœud de la v1 (note du code, non une phrase gelée)")
NOTE_LANCEE_DEPUIS_LE_MONTAGE = (
    "Reproduction de la première passe : non faite ; première passe jamais lancée au montage de la seconde passe et lancée "
    "depuis : la seconde passe ne la remplace pas ; aucune phrase de la lentille publique ni de la lentille des logits n'est "
    "écrite ici (note du code, non une phrase gelée)")


def phrases_de_la_reproduction(reproduction: dict, modules_differents: tuple) -> list[str]:
    """Les phrases de `phrases_v2.phrases_de_la_reproduction`, sauf quand la reproduction n'est pas faite et que l'état de la
    première passe relevé au calcul (`premiere_passe_au_calcul`) n'est plus celui du montage (`premiere_passe_au_montage`) :
    la phrase gelée, inexacte dans ces deux cas, cède la place à la note qui dit le cas. Sans ces deux champs, ou pour tout
    autre couple, la phrase de `phrases_v2` vaut."""
    if reproduction["etat"] == rp.ETAT_NON_FAITE:
        montage, calcul = reproduction.get("premiere_passe_au_montage"), reproduction.get("premiere_passe_au_calcul")
        if montage == nl.PREMIERE_PASSE_NON_ACHEVEE and calcul == nl.PREMIERE_PASSE_ACHEVEE:
            return [NOTE_ACHEVEE_DEPUIS_LE_MONTAGE]
        if montage == nl.PREMIERE_PASSE_JAMAIS_LANCEE and calcul in (nl.PREMIERE_PASSE_NON_ACHEVEE, nl.PREMIERE_PASSE_ACHEVEE):
            return [NOTE_LANCEE_DEPUIS_LE_MONTAGE]
    return p2.phrases_de_la_reproduction(reproduction, modules_differents)


# --- la tête, avec ces deux corrections ---------------------------------------------------------------------------------------------------
def tete(conditions: dict, fiche: dict, course: str, lecture_seconde_course_inscrite: bool, reproduction: dict,
         modules_differents: tuple, phrases_des_noeuds: list, independance_non_tenue: list | None = None,
         ligne_de_la_seconde_course: str | None = None) -> dict:
    """La tête de la seconde passe, dans l'ordre du texte : les mêmes clés, dans le même ordre, que `phrases_v2.tete`, dont le
    corps est repris ici ligne pour ligne ; seuls le verdict d'ensemble et les phrases de la reproduction sont ceux de ce
    module (`phrases_v2.tete` n'est pas appelée : elle recopierait la ligne de la seconde course sans que sa lecture soit
    inscrite)."""
    non_lues = [c.motif for c in (conditions[l] for l in K2.NOS_LENTILLES) if c.motif]
    non_lues += [case["motif"] for l in K2.NOS_LENTILLES if conditions[l].lue for case in conditions[l].couches.values()
                 if case.get("motif")]
    sortie = {"issue_des_noeuds": list(phrases_des_noeuds), "phrase_de_tete": p2.PHRASE_DE_TETE_V2,
              "verdict_d_identite": p2.ligne_du_verdict_d_identite(conditions, course),
              "phrases_permises": p2.phrases_permises(conditions, fiche, course, lecture_seconde_course_inscrite),
              "verdict_d_ensemble": lignes_du_verdict_d_ensemble(conditions, fiche, course, ligne_de_la_seconde_course),
              "domaine_d_usage": p2.PHRASE_DOMAINE_D_USAGE if conditions["S"].lue else None,
              "non_lues": non_lues, "reproduction": phrases_de_la_reproduction(reproduction, modules_differents),
              "independance_a_la_norme": p2.phrase_independance_non_tenue(independance_non_tenue or [])}
    p2.exiger_sans_paraphrase_interdite(sortie["verdict_d_identite"])
    for texte in non_lues:
        p2.exiger_sans_paraphrase_interdite(texte)
    return sortie
