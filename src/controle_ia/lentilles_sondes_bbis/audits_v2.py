"""Audit de symétrie de la seconde passe (R4) : déclencheurs gelés, en plus de ceux de la première passe.

Texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (`a2bbed7a…`), « Critères de lecture gelés », « Audit de symétrie de
la seconde passe ». Le texte décide, le code suit. Les déclencheurs de la première passe (`audits_v1.declencheurs`), la
calibration et ses bornes (`audits_v1`) sont réemployés tels quels ; ce module n'ajoute que ce que la v2 ajoute.

(i) **trop beau** : les vingt directions « concentrées » par notre R, ou par notre S ; pour une direction de la couche 7,
les mêmes vingt premiers jetons par notre R et par la lentille publique ; recouvrement de 20 sur 20 entre les deux lentilles R
pour plus de la moitié des directions ; pour une direction, les mêmes vingt premiers jetons par notre S et par notre R ; pour
une direction, les mêmes vingt premiers jetons par notre S et par les plongements seuls.
(ii) **tout négatif** : aucune lecture d'aucune direction « concentrée » ni « intermédiaire » par aucune des quatre
lentilles ; recouvrement de 0 sur 20 entre les deux lentilles R pour plus de la moitié des directions de la couche 23.
(iii) **incohérent** : une reproduction de la première passe dont un libellé ou les vingt premiers jetons diffèrent ; pour
plus de la moitié des directions, un recouvrement des deux moitiés de notre R inférieur à celui entre les deux lentilles R.
Issue écrite en réserve ; aucune table ne change.
"""
from __future__ import annotations

from . import audits_v1 as _v1
from . import constantes_v1 as K
from . import constantes_v2 as K2
from . import statistiques_v4 as st

# Repris tels quels de `audits_v1`.
bornes_calibration, calibration, MOTIF_CALIBRATION = _v1.bornes_calibration, _v1.calibration, _v1.MOTIF_CALIBRATION
declencheurs_premiere_passe, relire_par_chemin_independant = _v1.declencheurs, _v1.relire_par_chemin_independant
comparer_relecture = _v1.comparer_relecture

CONTENU_AUDIT_V2 = _v1.CONTENU_AUDIT + (
    "fiche de rangement et verdict d'identité", "empreintes des douze matrices contre le montage", "`meta` des deux fichiers",
    "orientation de K (`c @ K` contre `K @ c`)", "plongements contre lignes de `lm_head.weight`",
    "deux directions relues par notre R et par notre S sur un chemin indépendant en double précision",
    "pour une reproduction différente : versions des modules et des bibliothèques des deux passes")
N_SONDES = len(K.CELLULES) * len(K.PLIS) * len(K.ROLES)          # vingt


def _plus_de_la_moitie(n: int, total: int) -> bool:
    return bool(total and 2 * n > total)


def declencheurs(lectures: list[dict], recouvrements: list[dict], plongements_seuls: list[dict], reproduction: dict) -> dict:
    """Déclencheurs gelés de la seconde passe.
    `lectures` : une ligne par (sonde, vecteur, signe, lentille) : `sonde`, `vecteur`, `signe`, `couche`, `lentille`, `libelle`
    (ou `None`), `ids` (vingt premiers jetons). `recouvrements` : une ligne par (direction, signe) où il est calculable :
    `couche`, `publique_et_notre_r`, `moities` (ou `None`). `plongements_seuls` : une ligne par (direction, signe) :
    `sonde`, `vecteur`, `signe`, `ids`. `reproduction` : ce que rend `reproduction_v1`.
    Une sonde est « concentrée » par une lentille si l'une de ses lectures (vecteur, signe) l'est, comme à la première passe."""
    concentrees = {(l["sonde"], l["lentille"]) for l in lectures if l["libelle"] == st.LIBELLE_CONCENTREE}
    par_direction: dict = {}
    for l in lectures:
        if l.get("ids") is not None:
            par_direction.setdefault((l["sonde"], l["vecteur"], l["signe"]), {})[l["lentille"]] = (set(l["ids"]), l["couche"])
    sondes = {l["sonde"] for l in lectures}

    def toutes_concentrees(lentille: str) -> bool:
        return len(sondes) == N_SONDES and all((s, lentille) in concentrees for s in sondes)

    def memes(a: str, b: str, couches=None) -> list[str]:
        return sorted("/".join(cle) for cle, d in par_direction.items()
                      if a in d and b in d and d[a][0] == d[b][0] and (couches is None or d[a][1] in couches))

    seuls = {(p["sonde"], p["vecteur"], p["signe"]): set(p["ids"]) for p in plongements_seuls}
    memes_que_les_plongements = sorted("/".join(cle) for cle, d in par_direction.items()
                                       if K2.LENTILLE_NOTRE_S in d and cle in seuls and d[K2.LENTILLE_NOTRE_S][0] == seuls[cle])
    n = len(recouvrements)
    pleins = sum(1 for r in recouvrements if r["publique_et_notre_r"] == K.K_JETONS)
    couche_23 = [r for r in recouvrements if r["couche"] == 23]
    vides_23 = sum(1 for r in couche_23 if r["publique_et_notre_r"] == 0)
    avec_moities = [r for r in recouvrements if r.get("moities") is not None]
    moities_sous = sum(1 for r in avec_moities if r["moities"] < r["publique_et_notre_r"])
    distinctes = [l for l in lectures if l["libelle"] in (st.LIBELLE_CONCENTREE, st.LIBELLE_INTERMEDIAIRE)]

    trop_beau = {
        "vingt_directions_concentrees_par_notre_r": toutes_concentrees(K2.LENTILLE_NOTRE_R),
        "vingt_directions_concentrees_par_notre_s": toutes_concentrees(K2.LENTILLE_NOTRE_S),
        "memes_vingt_jetons_par_notre_r_et_la_lentille_publique_couche_7": memes(K2.LENTILLE_NOTRE_R, K.LENTILLE_PUBLIQUE, (7,)),
        "recouvrement_de_20_sur_20_pour_plus_de_la_moitie_des_directions": _plus_de_la_moitie(pleins, n),
        "memes_vingt_jetons_par_notre_s_et_notre_r": memes(K2.LENTILLE_NOTRE_S, K2.LENTILLE_NOTRE_R),
        "memes_vingt_jetons_par_notre_s_et_les_plongements_seuls": memes_que_les_plongements}
    tout_negatif = {
        "aucune_lecture_concentree_ni_intermediaire_par_aucune_lentille": bool(lectures) and not distinctes,
        "recouvrement_de_0_sur_20_pour_plus_de_la_moitie_des_directions_de_la_couche_23": _plus_de_la_moitie(vides_23, len(couche_23))}
    incoherent = {
        "reproduction_de_la_premiere_passe_differente": bool(reproduction.get("audit_de_symetrie_a_jouer")),
        "recouvrement_des_moities_inferieur_a_celui_des_deux_lentilles_r_pour_plus_de_la_moitie_des_directions":
            _plus_de_la_moitie(moities_sous, len(avec_moities))}
    leves = {"trop_beau": any(bool(v) for v in trop_beau.values()), "tout_negatif": any(tout_negatif.values()),
             "incoherent": any(incoherent.values())}
    return {"trop_beau": trop_beau, "tout_negatif": tout_negatif, "incoherent": incoherent,
            "trop_beau_declenche": leves["trop_beau"], "tout_negatif_declenche": leves["tout_negatif"],
            "incoherent_declenche": leves["incoherent"], "audit_a_jouer": any(leves.values()),
            "comptes": {"directions_comparees": n, "recouvrements_de_20": pleins, "directions_de_la_couche_23": len(couche_23),
                        "recouvrements_de_0_a_la_couche_23": vides_23, "directions_avec_moities": len(avec_moities),
                        "moities_sous_les_deux_lentilles_r": moities_sous}}
