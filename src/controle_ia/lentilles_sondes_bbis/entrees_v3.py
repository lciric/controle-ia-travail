"""Entrées de la lecture des sondes de l'étape B bis par la lentille publique — version 3 : la clé de l'addendum (EC-4).

Texte : `prereg/lecture-sondes-bbis-par-lentilles-v1.md` (`ca5066d7…`), corrigé par l'addendum scellé
`prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`
(`7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970`), § 3, EC-4 (avec le couple C1).

Seul ajout depuis `entrees_v2`, dont tout le reste est repris tel quel, par appel : la ligne
`ADDENDUM-CONCENTRATION-LENTILLES-BBIS` du registre propre est exigée **avant toute requête ou ouverture** :
- une seule ligne (absente ou en plusieurs lignes : rien ne part ; nœud) ;
- inscrite avant `CODE-LENTILLES-BBIS` et avant `ENTREES-LENTILLES-BBIS` (inscrite après l'une d'elles : rien ne part ; nœud) ;
- du chemin et de l'empreinte que porte la fiche du code (une autre empreinte : rien ne part ; nœud) ; le chemin et
  l'empreinte que ce code porte en constantes sont ceux de l'addendum scellé, et la ligne doit les citer aussi.
« Inscrite avant » se lit sur le registre propre, dont les lignes sont ajoutées et jamais réécrites : la ligne de l'addendum
est placée plus haut que toute ligne `CODE-LENTILLES-BBIS` et `ENTREES-LENTILLES-BBIS`, et son heure n'est postérieure à
aucune des leurs. `ouvrir_entrees` et `recuperer_entrees` font ce contrôle avant ceux de `entrees_v2`.
"""
from __future__ import annotations

from pathlib import Path

from . import constantes_v1 as K
from . import entrees_v2 as _v2
from .constantes_v1 import Refus

# L'addendum scellé (EC-4 : la fiche du code, le manifeste et les tables le citent à côté du texte).
ADDENDUM = "prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md"
EMPREINTE_ADDENDUM = "7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970"

# Repris tels quels de `entrees_v2`.
BRANCHE_DONNEES, OBJETS_DECODES, CHAMPS_SONDE = _v2.BRANCHE_DONNEES, _v2.OBJETS_DECODES, _v2.CHAMPS_SONDE
MOTIF_ECHEC_SONDE, MOTIF_LECTEUR_NON_APPRIS, MOTIF_ECHEC_LECTEUR = _v2.MOTIF_ECHEC_SONDE, _v2.MOTIF_LECTEUR_NON_APPRIS, _v2.MOTIF_ECHEC_LECTEUR
LigneRegistre, CourseBbis, VueE2, ArchiveE1, Sonde, Entrees = _v2.LigneRegistre, _v2.CourseBbis, _v2.VueE2, _v2.ArchiveE1, _v2.Sonde, _v2.Entrees
lignes_par_cle, exiger_scores_et_verdict = _v2.lignes_par_cle, _v2.exiger_scores_et_verdict
exiger_scellement_avant_verdict, chemins_permis, exiger_chemin_permis = _v2.exiger_scellement_avant_verdict, _v2.chemins_permis, _v2.exiger_chemin_permis
empreinte_sonde, empreinte_extrait, lire_sondes = _v2.empreinte_sonde, _v2.empreinte_extrait, _v2.lire_sondes

CLE_ADDENDUM = "ADDENDUM-CONCENTRATION-LENTILLES-BBIS"
CLES_POSTERIEURES_A_L_ADDENDUM = ("CODE-LENTILLES-BBIS", "ENTREES-LENTILLES-BBIS")


def lignes_ordonnees(registre: str | Path, cles: tuple[str, ...]) -> list[tuple[int, LigneRegistre]]:
    """Lignes du registre dont la clé est l'une de `cles`, avec leur place (numéro de ligne du fichier), dans l'ordre du
    fichier. Mêmes contrôles de forme que `entrees_v2.lignes_par_cle` (appelée d'abord) ; toute autre ligne est écartée sans
    être gardée ni rendue."""
    lignes_par_cle(registre, cles)
    sortie = []
    for place, ligne in enumerate(Path(registre).read_text(encoding="utf-8").splitlines()):
        m = _v2._RE_LIGNE.match(ligne.strip())
        if not m:
            continue
        cellules = [c.strip() for c in m.group(1).split("|")]
        if cellules and cellules[0] in cles:
            sortie.append((place, LigneRegistre(*cellules)))
    return sortie


def exiger_addendum(registre_propre: str | Path, chemin_de_la_fiche, sha256_de_la_fiche) -> LigneRegistre:
    """Addendum, EC-4 et « Liste d'arrêt » : `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` absente, en plusieurs lignes, inscrite
    après `CODE-LENTILLES-BBIS` ou après `ENTREES-LENTILLES-BBIS`, ou d'une autre empreinte que celle que porte la fiche du
    code : rien ne part ; nœud. `chemin_de_la_fiche`, `sha256_de_la_fiche` : ce que la fiche du code porte pour l'addendum."""
    lignes = lignes_ordonnees(registre_propre, (CLE_ADDENDUM,) + CLES_POSTERIEURES_A_L_ADDENDUM)
    addenda = [(p, l) for p, l in lignes if l.cle == CLE_ADDENDUM]
    if not addenda:
        raise Refus(f"{CLE_ADDENDUM} absente du registre propre : rien ne part ; nœud")
    if len(addenda) > 1:
        raise Refus(f"{CLE_ADDENDUM} en plusieurs lignes ({len(addenda)}) : rien ne part ; nœud")
    place, ligne = addenda[0]
    if ligne.chemin != ADDENDUM or ligne.sha256 != EMPREINTE_ADDENDUM:
        raise Refus(f"{CLE_ADDENDUM} ne cite pas l'addendum scellé de ce code (chemin ou empreinte différents) : rien ne part ; "
                    "nœud")
    if chemin_de_la_fiche != ligne.chemin or sha256_de_la_fiche != ligne.sha256:
        raise Refus(f"{CLE_ADDENDUM} d'un autre chemin ou d'une autre empreinte que ceux que porte la fiche du code : rien ne "
                    "part ; nœud")
    for autre_place, autre in lignes:
        if autre.cle == CLE_ADDENDUM:
            continue
        if autre_place < place or autre.heure < ligne.heure:
            raise Refus(f"{CLE_ADDENDUM} inscrite après {autre.cle} : rien ne part ; nœud")
    return ligne


def exiger_registre_propre(registre_propre: str | Path, chemin_de_la_fiche=ADDENDUM,
                           sha256_de_la_fiche=EMPREINTE_ADDENDUM) -> dict[str, LigneRegistre]:
    """Contrôles de `entrees_v2.exiger_registre_propre` (`SCELLEMENT-`, `GO-` et `CODE-LENTILLES-BBIS` présentes, scellement
    qui cite le texte), puis la clé de l'addendum. Sans les valeurs de la fiche, la ligne est comparée aux constantes du code ;
    le lanceur la compare en plus à ce que la fiche du code porte."""
    lignes = _v2.exiger_registre_propre(registre_propre)
    return lignes | {CLE_ADDENDUM: exiger_addendum(registre_propre, chemin_de_la_fiche, sha256_de_la_fiche)}


def ouvrir_entrees(racine: str | Path, registre_bbis: str | Path, registre_propre: str | Path,
                   largeur: int = K.LARGEUR) -> Entrees:
    """`entrees_v2.ouvrir_entrees`, précédée du contrôle de la clé de l'addendum : rien n'est ouvert sans elle."""
    exiger_registre_propre(registre_propre)
    return _v2.ouvrir_entrees(racine, registre_bbis, registre_propre, largeur)


def recuperer_entrees(url_depot: str, destination: str | Path, registre_bbis: str | Path, registre_propre: str | Path,
                      branche: str = BRANCHE_DONNEES) -> Path:
    """`entrees_v2.recuperer_entrees`, précédée du contrôle de la clé de l'addendum : aucune requête sans elle."""
    exiger_registre_propre(registre_propre)
    return _v2.recuperer_entrees(url_depot, destination, registre_bbis, registre_propre, branche)
