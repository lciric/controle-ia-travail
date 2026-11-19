"""Arrêt de la lecture de la discrétion, bras A des organismes discrets, version 8 du code (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon28.md`, 6.9, « Ce que vaut cet arrêt » et « Ce que rend le programme
qui refuse — définition unique » ; 8.4 ; section 12, point 21 ; note du brouillon 26, partie 3, points 17 à 20).

`arrets_bras_a_v7.py` n'est pas modifié (R12). Ce qui change : le brouillon 26 porte à **cinq** les natures du défaut
d'une liste entière — « un champ hors de son ordre » s'y ajoute, pour dix bons champs dans un autre ordre — et dit
ce que vaut une clé en double : dans une liste fermée, « un champ en double » de cette liste ; ailleurs dans la
pièce, « pièce illisible ». Un champ de plus et un champ de moins à la fois : « un champ de moins ».

Une garde de 8.4 qui refuse une livraison du côté habilité, ou un cas que la rédaction retenue tient pour une
anomalie, lève **un événement nommé** : `ArretDeLaLectureDeLaDiscretion`. Il porte **exactement les éléments de la
définition unique de 6.9** :
1. le nom de la garde de 8.4 qui refuse, ou, pour un cas tenu pour une anomalie, le nom de la règle d'arrêt
   (« intervalle impossible » ; « moniteur appris non ajustable ») ;
2. le nom du champ en défaut — une clé des listes fermées ou l'un des dix champs du fichier des scores par unité,
   jamais ce qu'elle porte ; une clé de `reglages` porte son préfixe (`reglages.n_permutations`), une clé de
   `scores_par_unite` aussi ; **ou**, quand le défaut est celui d'une liste entière, la désignation de cette liste
   (`DESIGNATIONS` : les quatre listes fermées, la liste des vingt lectures, celle des dix champs du fichier des
   scores par unité) **et la nature du défaut** (`NATURES` : un champ de plus ; un champ de moins ; un champ hors de
   son ordre ; un champ en double ; pièce illisible) — le nom d'un champ de plus n'est jamais rendu, puisqu'il vient
   de la livraison ;
3. la lettre du cas de la table des formes où l'analyse a rangé la lecture, ou « aucun cas » ;
4. l'étape, (m) ou (n) — **déduite de la pièce contrôlée, jamais de la dose** : toute garde sur la sortie de la lecture
   commune donne l'étape (m), même pour une lecture à la dose ¼ ; seules les gardes du fichier des scores par unité
   donnent l'étape (n) ;
5. quand le défaut tient à une lecture, le moniteur et la dose de cette lecture, pris dans les listes de ce code
   (quand le champ `moniteur` ou `dose` d'une lecture n'est pas reconnu, ni l'un ni l'autre : ils ne sont pas connus).
Il ne porte **aucun nombre de la livraison** — aire, aire d'un pli, valeur p, compte, borne, quantile, effectif, rang —,
**ni la valeur de `motif`, ni celle de `calculable`**, ni aucun nom de clé inconnu. Chaque élément est pris dans une
liste fermée de ce module, contrôlée à la fabrication : rien de la livraison ne peut s'y glisser.

**Ce que cet événement entraîne n'est pas écrit ici.** C'est un choix nommé, sans valeur par défaut, lu dans la
configuration scellée (`configuration_bras_a_v8`, fiche 12, en attente du mot de Lazar) et appliqué par
`verdicts_bras_a_v8`. Ce module ne nomme aucune ligne d'aucune table de verdict.

`ArretDeLaLectureDeLaDiscretion` est une `GardeArret`. Rien ne l'attrape pour continuer la lecture : l'analyse le
consigne (fichier scellé de l'arrêt) et le laisse remonter. **L'enchaînement n'en tire que le constat**
(`constat()`) : la trace d'appel de l'exception garde en mémoire les variables de la lecture fautive, qui ne sont ni
écrites ni affichées (6.9, « Trace d'appel »). Aucun état de moniteur n'est dit après lui.
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

# Quand le défaut est celui d'une liste entière : la désignation de la liste (six), et la nature du défaut (cinq).
LISTE_DES_ONZE, LISTE_DES_DIX_HUIT, LISTE_DES_NEUF, LISTE_DES_CINQ, LISTE_DES_VINGT_LECTURES, LISTE_DES_DIX_CHAMPS = (
    "liste des onze clés de la sortie", "liste des dix-huit clés d'une lecture", "liste des neuf clés de reglages",
    "liste des cinq clés de scores_par_unite", "liste des vingt lectures",
    "liste des dix champs d'une ligne du fichier des scores par unité")
DESIGNATIONS = (LISTE_DES_ONZE, LISTE_DES_DIX_HUIT, LISTE_DES_NEUF, LISTE_DES_CINQ, LISTE_DES_VINGT_LECTURES,
                LISTE_DES_DIX_CHAMPS)
UN_CHAMP_DE_PLUS, UN_CHAMP_DE_MOINS, UN_CHAMP_HORS_DE_SON_ORDRE, UN_CHAMP_EN_DOUBLE, PIECE_ILLISIBLE = (
    "un champ de plus", "un champ de moins", "un champ hors de son ordre", "un champ en double", "pièce illisible")
NATURES = (UN_CHAMP_DE_PLUS, UN_CHAMP_DE_MOINS, UN_CHAMP_HORS_DE_SON_ORDRE, UN_CHAMP_EN_DOUBLE, PIECE_ILLISIBLE)
CLES_NOMMABLES = frozenset(
    CLES_PAR_MONITEUR_ET_PAR_DOSE + CLES_DE_LA_LECTURE_COMMUNE + CHAMPS_DU_FICHIER_DES_RANGS
    + tuple(f"reglages.{c}" for c in CLES_DES_REGLAGES) + tuple(f"scores_par_unite.{c}" for c in CLES_DES_SCORES_PAR_UNITE))
CHAMPS_NOMMABLES = CLES_NOMMABLES | frozenset(DESIGNATIONS)
ELEMENTS_DU_CONSTAT = ("garde", "champ", "nature", "cas", "etape", "moniteur", "dose")


class ArretDeLaLectureDeLaDiscretion(GardeArret):
    """Événement nommé « arrêt de la lecture de la discrétion ». Éléments : `garde` (garde de 8.4 ou règle d'arrêt :
    l'une de `GARDES`) ; `champ` (une clé de `CLES_NOMMABLES`, ou la désignation d'une liste, de `DESIGNATIONS`) ;
    `nature` (l'une de `NATURES` **si et seulement si** `champ` désigne une liste ; `None` sinon) ; `cas` (l'un de
    `CAS`) ; `etape` (« m » ou « n ») ; et, quand le défaut tient à une lecture, `moniteur` (l'un des cinq) et `dose`
    (l'une des quatre) — sinon `None` tous deux. Rien d'autre. Chaque élément est contrôlé contre sa liste fermée :
    aucune valeur de la livraison n'entre dans l'événement, ni dans son message, qui n'est fait que de ces éléments."""

    def __init__(self, garde: str, champ: str, cas: str, etape: str, moniteur: str | None = None, dose: str | None = None,
                 nature: str | None = None):
        if garde not in GARDES or cas not in CAS or etape not in ETAPES or not isinstance(champ, str) \
                or champ not in CHAMPS_NOMMABLES:
            raise GardeArret("arrêt de la lecture de la discrétion : garde, champ, cas ou étape hors de leurs listes fermées")
        if (champ in DESIGNATIONS) != (nature is not None) or (nature is not None and nature not in NATURES):
            raise GardeArret("arrêt de la lecture de la discrétion : une liste désignée porte la nature de son défaut, prise "
                             "dans sa liste fermée ; un champ nommé n'en porte pas")
        if (moniteur is None) != (dose is None) or (moniteur is not None and moniteur not in MONITEURS) \
                or (dose is not None and dose not in FORMES_DOSE):
            raise GardeArret("arrêt de la lecture de la discrétion : moniteur et dose d'une lecture, tous deux ou aucun, "
                             "pris dans leurs listes")
        self.garde, self.champ, self.cas, self.etape, self.moniteur, self.dose = garde, champ, cas, etape, moniteur, dose
        self.nature = nature
        place = "" if moniteur is None else f" ; lecture : {moniteur}, {dose}"
        nom = "règle d'arrêt" if garde in REGLES_D_ARRET else "garde"
        quoi = f"champ : {champ}" if nature is None else f"{champ} : {nature}"
        super().__init__(f"arrêt de la lecture de la discrétion, étape ({etape}) — {nom} : {garde} ; {quoi} ; "
                         f"cas : {cas}{place}")

    def constat(self) -> dict:
        """Ce que l'événement porte, et rien d'autre : pour le fichier scellé de l'arrêt et pour la composition de
        l'issue. **C'est la seule chose que l'enchaînement tire de l'exception.**"""
        return {"garde": self.garde, "champ": self.champ, "nature": self.nature, "cas": self.cas, "etape": self.etape,
                "moniteur": self.moniteur, "dose": self.dose}


def exiger_constat(constat) -> dict:
    """Constat d'un arrêt, tel que `ArretDeLaLectureDeLaDiscretion.constat` le rend : exactement ses sept champs (la
    garde ou la règle, le champ ou la liste, la nature, le cas, l'étape, le moniteur et la dose), chacun pris dans sa
    liste fermée. Tout autre champ est refusé."""
    if not isinstance(constat, dict) or tuple(sorted(constat)) != tuple(sorted(ELEMENTS_DU_CONSTAT)):
        raise GardeArret(f"constat d'un arrêt de la lecture de la discrétion : exactement les champs {ELEMENTS_DU_CONSTAT}")
    return ArretDeLaLectureDeLaDiscretion(**constat).constat()
