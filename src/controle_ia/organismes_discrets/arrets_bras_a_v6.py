"""Arrêt de la lecture de la discrétion, bras A des organismes discrets, version 6 du code (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon24.md`, 6.9, « Ce que vaut cet arrêt » et « Ce que rend le programme
qui refuse — définition unique » ; 8.4, ligne « issue d'un arrêt de la lecture de la discrétion » ; section 12,
point 21 ; notes des brouillons 23 et 24, partie 6, points 3, 15 et 16).

Une garde de 8.4 qui refuse une livraison du côté habilité, ou un cas que la rédaction retenue tient pour une
anomalie, lève **un événement nommé** : `ArretDeLaLectureDeLaDiscretion`. Il porte **exactement les cinq éléments de la
définition unique de 6.9** :
1. le nom de la garde de 8.4 qui refuse, ou, pour un cas tenu pour une anomalie, le nom de la règle d'arrêt
   (« intervalle impossible » ; « moniteur appris non ajustable ») ;
2. le nom du champ en défaut — le nom d'une clé des listes fermées, jamais ce qu'elle porte ; quand le défaut est
   celui d'une liste entière (un champ de plus ou de moins, un champ en double) ou d'une ligne du fichier des rangs,
   aucune clé des listes n'est en défaut : ce code nomme alors la liste, par l'une des désignations fermées de
   `DESIGNATIONS` (relevé des défauts du texte) ;
3. la lettre du cas de la table des formes où l'analyse a rangé la lecture, ou « aucun cas » ;
4. l'étape, (m) ou (n) — **déduite de la pièce contrôlée, jamais de la dose** : toute garde sur la sortie de la lecture
   commune donne l'étape (m), même pour une lecture à la dose ¼ ; seules les gardes du fichier des scores par unité
   donnent l'étape (n) ;
5. quand le défaut tient à une lecture, le moniteur et la dose de cette lecture, pris dans les listes de ce code.
Il ne porte **aucun nombre de la livraison** — aire, aire d'un pli, valeur p, compte, borne, quantile, effectif, rang —,
**ni la valeur de `motif`, ni celle de `calculable`**, ni aucun nom de clé inconnu. Chaque élément est pris dans une
liste fermée de ce module, contrôlée à la fabrication : rien de la livraison ne peut s'y glisser.

**Ce que cet événement entraîne n'est pas écrit ici.** C'est un choix nommé, sans valeur par défaut, lu dans la
configuration scellée (`configuration_bras_a_v6`, choix de l'issue d'un arrêt, fiche 12, en attente du mot de Lazar)
et appliqué par `verdicts_bras_a_v6`. Ce module ne nomme aucune ligne d'aucune table de verdict.

`ArretDeLaLectureDeLaDiscretion` est une `GardeArret`. Rien ne l'attrape pour continuer la lecture : l'analyse le
consigne (fichier scellé de l'arrêt) et le laisse remonter ; l'enchaînement n'en tire que le constat, pour composer
l'issue selon le choix retenu. Aucun état de moniteur n'est dit après lui.
"""
from __future__ import annotations

from ..gardes import GardeArret

ETAPE_M, ETAPE_N = "m", "n"
ETAPES = (ETAPE_M, ETAPE_N)

# Les gardes de 8.4 qui peuvent arrêter la lecture de la discrétion (noms des lignes de la table), et les deux règles
# d'arrêt des cas tenus pour une anomalie (6.9, définition unique).
GARDE_FAMILLE = "famille de Holm complète"
GARDE_INTERVALLE = "intervalle dégénéré seul"
GARDE_FORME = "forme d'une livraison"
GARDE_LISTES = "listes fermées des noms rendus"
GARDE_REGLAGES = "réglages rendus"
GARDE_RANGS = "fichier des scores par unité"
REGLE_INTERVALLE_IMPOSSIBLE = "intervalle impossible"
REGLE_NON_AJUSTABLE = "moniteur appris non ajustable"
GARDES = (GARDE_FAMILLE, GARDE_INTERVALLE, GARDE_FORME, GARDE_LISTES, GARDE_REGLAGES, GARDE_RANGS,
          REGLE_INTERVALLE_IMPOSSIBLE, REGLE_NON_AJUSTABLE)
REGLES_D_ARRET = (REGLE_INTERVALLE_IMPOSSIBLE, REGLE_NON_AJUSTABLE)

# Les cas de la table des formes (6.9), et « aucun cas ».
CAS_A, CAS_B, CAS_C, CAS_D, CAS_E, AUCUN_CAS = "A", "B", "C", "D", "E", "aucun cas"
CAS = (CAS_A, CAS_B, CAS_C, CAS_D, CAS_E, AUCUN_CAS)

MONITEURS = ("classifieur-lexical", "moniteur-boite-noire", "agregateur-sequentiel", "classifieur-de-surface", "juge")
FORMES_DOSE = ("dose-0.25", "dose-0.50", "dose-0.75", "dose-1.00")

# Les quatre listes fermées des noms rendus par le module du côté habilité, version 8 (6.9), et les dix champs du
# fichier des scores par unité : ce sont les seuls noms de champ qu'un arrêt peut dire.
CLES_PAR_MONITEUR_ET_PAR_DOSE = (
    "moniteur", "dose", "calculable", "motif", "aire", "pli0", "pli1", "valeur_p_bas", "valeur_p_haut", "n_permutations",
    "permutations_degenerees", "au_moins_egales", "borne_haute", "quantile_borne_haute", "tirages", "tirages_degeneres",
    "effectifs", "valeur_p_pour_la_famille")                                              # dix-huit
CLES_DE_LA_LECTURE_COMMUNE = (
    "plis", "lectures", "piece_source", "reglages", "agregateur_somme_sans_etat", "agregateur_maximum_sans_etat",
    "exclues", "preuve_d_ordre", "scores_par_unite", "comptes_des_lectures", "nombres_rendus")   # onze
CLES_DES_REGLAGES = ("n_permutations", "n_tirages", "taille_de_la_famille", "niveau", "statistique_agregateur",
                     "doses_de_la_famille", "dose_pour_information", "permutation", "unite_de_la_permutation")   # neuf
CLES_DES_SCORES_PAR_UNITE = ("fichier", "sha256", "lignes", "champs", "forme")            # cinq
CHAMPS_DU_FICHIER_DES_RANGS = ("moniteur", "dose", "cle", "condition", "tache", "episode", "pas", "pli", "etiquette", "rang")
if [len(x) for x in (CLES_PAR_MONITEUR_ET_PAR_DOSE, CLES_DE_LA_LECTURE_COMMUNE, CLES_DES_REGLAGES,
                     CLES_DES_SCORES_PAR_UNITE, CHAMPS_DU_FICHIER_DES_RANGS)] != [18, 11, 9, 5, 10]:
    raise GardeArret("listes fermées de la version 8 : dix-huit, onze, neuf, cinq et dix noms exigés")
# Quand le défaut est celui d'une liste entière ou d'une ligne du fichier des rangs : la liste, nommée.
LISTE_DES_ONZE, LISTE_DES_DIX_HUIT, LISTE_DES_NEUF, LISTE_DES_CINQ, LIGNE_DES_RANGS, CHAMP_EN_DOUBLE = (
    "liste des onze clés de la sortie", "liste des dix-huit clés d'une lecture", "liste des neuf clés de reglages",
    "liste des cinq clés de scores_par_unite", "liste des dix champs d'une ligne du fichier des rangs", "champ en double")
DESIGNATIONS = (LISTE_DES_ONZE, LISTE_DES_DIX_HUIT, LISTE_DES_NEUF, LISTE_DES_CINQ, LIGNE_DES_RANGS, CHAMP_EN_DOUBLE)
CHAMPS_NOMMABLES = frozenset(
    CLES_PAR_MONITEUR_ET_PAR_DOSE + CLES_DE_LA_LECTURE_COMMUNE + CHAMPS_DU_FICHIER_DES_RANGS + DESIGNATIONS
    + tuple(f"reglages.{c}" for c in CLES_DES_REGLAGES) + tuple(f"scores_par_unite.{c}" for c in CLES_DES_SCORES_PAR_UNITE))
ELEMENTS_DU_CONSTAT = ("garde", "champ", "cas", "etape", "moniteur", "dose")


class ArretDeLaLectureDeLaDiscretion(GardeArret):
    """Événement nommé « arrêt de la lecture de la discrétion ». Éléments : `garde` (garde de 8.4 ou règle d'arrêt :
    l'une de `GARDES`), `champ` (l'un de `CHAMPS_NOMMABLES`), `cas` (l'un de `CAS`), `etape` (« m » ou « n »), et,
    quand le défaut tient à une lecture, `moniteur` (l'un des cinq) et `dose` (l'une des quatre) — sinon `None` tous
    deux. Rien d'autre. Chaque élément est contrôlé contre sa liste fermée : aucune valeur de la livraison n'entre dans
    l'événement, ni dans son message, qui n'est fait que de ces éléments."""

    def __init__(self, garde: str, champ: str, cas: str, etape: str, moniteur: str | None = None, dose: str | None = None):
        if garde not in GARDES or cas not in CAS or etape not in ETAPES or not isinstance(champ, str) \
                or champ not in CHAMPS_NOMMABLES:
            raise GardeArret("arrêt de la lecture de la discrétion : garde, champ, cas ou étape hors de leurs listes fermées")
        if (moniteur is None) != (dose is None) or (moniteur is not None and moniteur not in MONITEURS) \
                or (dose is not None and dose not in FORMES_DOSE):
            raise GardeArret("arrêt de la lecture de la discrétion : moniteur et dose d'une lecture, tous deux ou aucun, "
                             "pris dans leurs listes")
        self.garde, self.champ, self.cas, self.etape, self.moniteur, self.dose = garde, champ, cas, etape, moniteur, dose
        place = "" if moniteur is None else f" ; lecture : {moniteur}, {dose}"
        nom = "règle d'arrêt" if garde in REGLES_D_ARRET else "garde"
        super().__init__(f"arrêt de la lecture de la discrétion, étape ({etape}) — {nom} : {garde} ; champ : {champ} ; "
                         f"cas : {cas}{place}")

    def constat(self) -> dict:
        """Ce que l'événement porte, et rien d'autre : pour le fichier scellé de l'arrêt et pour la composition de
        l'issue."""
        return {"garde": self.garde, "champ": self.champ, "cas": self.cas, "etape": self.etape, "moniteur": self.moniteur,
                "dose": self.dose}


def exiger_constat(constat) -> dict:
    """Constat d'un arrêt, tel que `ArretDeLaLectureDeLaDiscretion.constat` le rend : exactement ses six champs (la
    garde ou la règle, le champ, le cas, l'étape, le moniteur et la dose), chacun pris dans sa liste fermée. Tout autre
    champ est refusé."""
    if not isinstance(constat, dict) or tuple(sorted(constat)) != tuple(sorted(ELEMENTS_DU_CONSTAT)):
        raise GardeArret(f"constat d'un arrêt de la lecture de la discrétion : exactement les champs {ELEMENTS_DU_CONSTAT}")
    return ArretDeLaLectureDeLaDiscretion(**constat).constat()
