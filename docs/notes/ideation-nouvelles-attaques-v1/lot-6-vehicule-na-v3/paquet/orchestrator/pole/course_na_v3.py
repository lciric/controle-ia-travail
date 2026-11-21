"""Véhicule NA-1, lot 6 v3 — la génération et la course du régime (`course_na_v3`).

**v3** (vérification S du lot 6 v2, « À corriger » ; décisions de la mère, 18:59Z, GO-2026-11-21-69) : en état 1 ou 2, le
journal doit être **de type exact** `JournalRequetesColonneNA` (une sous-classe ne compte pas ; une classe falsifiée par
`__class__` non plus), et son envoi ne doit être surchargé ni sur la classe ni sur l'instance ; fichiers de sortie nommés
en v3 (R12 vaut pour les sorties). Le reste est le v2.

Lettre : V9 (`864f39a7…`), l. 60 à 64, 77, 92 à 101, 376 à 381, 385 ; conception du véhicule v5 (`1b7f6822…`), § 2.4,
§ 2.5 (surcharge de `juger`), § 2.9 (génération et course), § 2.13 (gardes héritées, refus écrits, garde de remplacement,
A17, A2), § 5.1, § 6 (arrêts n° 5, 6, 7, 10, 14) ; contrôle de la v5 (`4b369004…`), point 1 ; relevé du lot 0
(`10ac79ec…`), Q3, Q4, Q9, Q11, Q12 ; mandat du lot 6 et son erratum 1 (E4 à E8) ; mandat de reprise du lot 6 v3
(`89b2a38d…`) et mot de la mère du 21 novembre à 18:15Z (GO-2026-11-21-69).

**Ce que la v2 ajoute au v1 récupéré : le refus de câblage.** La course reçoit l'état de l'interrupteur de la colonne
« matière première » (`etat_colonne`, 0, 1 ou 2, sans défaut) et une fabrique de journal (`fabrique_journal(dossier, nom)`,
sans défaut). Au départ de la course (sur le journal de la génération 1, fait par la fabrique) et à la construction de
chaque génération (sur le journal du contexte d'appel), le contexte est refusé si l'état est 1 ou 2 et que le journal n'est
pas un `JournalRequetesColonneNA` du lot 10 a : arrêt nommé `ArretCablageColonneNA` (numéro à l'additif), inscrit aux
arrêts connus et au journal des arrêts et des générations. Renforcement déclaré (écart au mandat, rapport) : en état 1 ou 2,
le journal de la colonne doit porter un contrôle de départ du même état, colonne chargée. En état 0, tout journal du lot 3
est reçu. Un état inconnu est refusé par le même arrêt. Le reste est le v1, inchangé.

**La classe de génération** : `GenerationNA(AppelGardeNA, GenerationV68)`, le mélange du lot 4 devant la v68 (interface
figée du lot 4, § 8). Elle passe à la v68 un héritage `None` et sert le registre par sa propre proposition.

- `fournisseurs_requis` surchargée : seuls les adaptateurs des proposeurs, de l'aiguilleur et des juges (les rôles de la
  table) sont exigés ; les lecteurs d'étiquettes et le metteur en fusion désignent `hors_course` et ne sont jamais
  appelés (un appel planté est refusé par la surcharge d'`appel`, n° 12, seconde clause).
- **Six étapes déclarées** (la vérification du noyau les exige ; relevé du lot 0, Q3) : « proposition », « aiguillage » et
  « juges » jouées avec appels ; « etiquettes » jouée sans appel (aucun bras) ; « passe_tableau » et « fusions » retirées
  par construction (sacrifiables, plafond de relais au-dessus de S17). Une étape neutralisée qui serait jouée est un
  défaut de configuration : arrêt (`EtapeNeutraliseeJouee`), jamais un repli.
- **Proposition neuve** : la requête de chaque appel est assemblée par le module `requete` du lot 3 (assemblée et mesurée
  avant le départ, arrêt n° 8) ; la réponse est gardée pour le portier ; rien du noyau n'est repris (ni `rstrip`, ni
  section « Case », ni section d'héritage). La lecture passée à `appel` rend le texte tel quel dès qu'un texte est rendu
  (§ 2.13, tenue (i)) : le suivi des rôles ne compte jamais d'échec pour une réponse sans fiche.
- **Étape « aiguillage » surchargée** : le portier neuf du lot 5 classe chaque réponse ; la fonction `appeler` qu'il reçoit
  rend `a["refus_ecrit"]` dès qu'il est présent, avant toute lecture de `a["r"]` ou de `a["lu"]` (erratum 1, E4).
- **Surcharge de `juger`** : exige le passeport du portier neuf (A17 sous le portier neuf : arrêt nommé) ; sert
  l'identifiant réencodé, fait des mêmes octets que le jeton du noyau ; appelle `self.appel` ; dépose les verdicts au coffre
  comme le noyau ; lève l'arrêt d'A2 quand la version servie d'un juge change.
- **Ce que rend un refus écrit, par rôle** (§ 2.13) : proposeur, case non jouée pour son espèce ; portier, la fiche « au
  coffre » avec sa classe écrite (par le lot 5) ; juge, verdict absent, compté. **Garde de remplacement** : onze refus
  écrits d'un même proposeur dans une génération (borne lue dans la configuration) : arrêt nommé de la course. Le compte
  repart de zéro à chaque génération. Un rôle arrêté le reste jusqu'à la fin de la génération : un proposeur arrêté à sa
  k-ième case ne rend que 12 − k refus écrits, ses cases sont comptées « non jouées », et la course continue (contrôle de
  la v5, point 1, à la lettre).
- **Mémoire anti-redite déclarée** : elle tourne dans `executer` (non surchargé), écrit `memoire.json` dans le dossier de
  la génération, n'est servie à personne et n'entre ni dans les classes, ni au registre, ni dans les comptes.

**La course** (`executer_course_na_v3`) : sur le modèle d'`executer_course_v68`, qu'elle n'appelle pas, non plus que
`verifier_regime_v68`. Avant toute écriture : le régime (quatre conditions) et les gardes héritées. Au départ de chaque
génération : garde d'empreintes (n° 14, pièces et copie de la configuration de la génération), garde de disjonction
(n° 10), registre servi fabriqué et vérifié (n° 8, 9, 19), requêtes assemblées et mesurées (n° 8), réservation du plafond
d'une génération sur le plafond de la course (n° 6). Après chacune : seuils de la génération (n° 7, un nœud budgétaire
est un arrêt nommé), garde du coffre (n° 5), ligne de la génération, sceaux.

**Le journal des arrêts et des générations** (erratum 1, E5) : un fichier à part, en ajout seul, scellé à la clôture,
jamais servi ; le journal du lot 3 reste fermé à ses quatre événements. **La ligne de la génération** (E6) fusionne les
comptes du mélange (`na_comptes`), du portier (`portier.comptes()`) et du journal (`journal_na_v3.comptes`), chacun sous
sa clé, sans renommer ni additionner deux sous-comptes distincts ; « au coffre par refus du portier » reste à part.

Aucun message, aucune ligne hors du dossier de sortie ne recopie un octet d'une réponse, d'une fiche ou d'une ligne du
registre servi. Bibliothèque standard, orchestrateur `a41b7b50…` et v68, modules des lots 1 à 5.
"""

import dataclasses
import json
import os

from pole import appel_garde_na_v1 as ag
from pole import configuration_course_na_v1 as cfn
from pole import contrat_fiche_na_v1 as ct
from pole import garde_motifs_na_v4 as gm
from pole import identifiants_na_v1 as ident
from pole import journal_na_v3 as jn
from pole import matiere_premiere_na_v1 as mp
from pole import portier_na_v1 as pt
from pole import registre_na_v1 as rg
from pole import requete_na_v3 as rq
from pole import routage_na_v1 as rt
from pole import tirage_na_v4 as tn
from pole import verifier_registre_servi_na_v1 as vr
from pole.budget_course_v68 import CumulCourseAuDela, GardeBudgetCourseV68, PlafondDeCourseAtteint
from pole.budget_v53 import NON_MESUREE
from pole.course2_v68 import GenerationV68
from pole.juges_croises_v53 import lire_verdict
from pole.noyau_v54 import NoeudArret
from pole.noyau_v56 import ArretParSignal, ArretSurSignal, motif_arret
from pole.outils import ecrire_json_scelle

VERSION = "course-na-v3"
ETATS_COLONNE = (mp.ETAT_ETEINTE, mp.ETAT_GARDE_SEULE, mp.ETAT_ALLUMEE)
ETATS_COLONNE_GARDES = (mp.ETAT_GARDE_SEULE, mp.ETAT_ALLUMEE)
# La méthode d'envoi du journal de la colonne, telle que le lot 10 a la définit, relevée à l'import de ce module (v3).
_ENVOI_DE_LA_COLONNE = mp.JournalRequetesColonneNA.__dict__["journaliser_envoi"]
ETAPES_JOUEES_AVEC_APPELS = ("proposition", "aiguillage", "juges")
ETAPE_JOUEE_SANS_APPEL = "etiquettes"
ETAPES_RETIREES = ("passe_tableau", "fusions")
NOM_JOURNAL_ARRETS = "journal-arrets-et-generations-na-v3.jsonl"  # R12 vaut pour les sorties (mère, 18:59Z)
NOM_BILAN = "bilan-course-na-v3.json"
DOSSIER_JOURNAUX = "journaux"
LOT_JUGES = "passe1"
ROLE_KIT_PROPOSEUR, ROLE_KIT_JUGE = "proposeur_ideation", "juge_ideation"

# Issues d'un appel de proposeur, tenues par le lot 6 (hors du portier : aucun texte rendu à classer).
ISSUE_NON_LANCE = "appel non lancé"
ISSUE_REFUS_ECRIT = "refus écrit"
ISSUE_ARRET_1 = "arrêt n° 1, consigné, non relancé"
ISSUE_ILLISIBLE_NON_LUE = "réponse illisible, réponse non lue"
ISSUE_ILLISIBLE_CAUSE = "réponse illisible, cause non établie"
ISSUE_ILLISIBLE_ERREUR = "réponse illisible, erreur"
ISSUE_TEXTE_RENDU = "texte rendu, au portier"
ISSUES_PROPOSEUR = (ISSUE_NON_LANCE, ISSUE_REFUS_ECRIT, ISSUE_ARRET_1, ISSUE_ILLISIBLE_NON_LUE, ISSUE_ILLISIBLE_CAUSE,
                    ISSUE_ILLISIBLE_ERREUR, ISSUE_TEXTE_RENDU)
ABSENCES_JUGE = ("non lancé", "refus écrit", "verdict illisible")


# --- arrêts nommés neufs (numérotés à l'additif) ----------------------------------------------------------------------

class ArretCourseNA(RuntimeError):
    """Un arrêt nommé de la course, levé par le lot 6 ; le message ne recopie aucun contenu."""

    numero = None
    nom = None


class ArretRemplacementRefusEcritsNA(ArretCourseNA):
    """Garde de remplacement (§ 2.13) : onze refus écrits d'un même proposeur dans une génération ; numéro à l'additif."""

    nom = "garde de remplacement : refus écrits d'un même proposeur"

    def __init__(self, role, n, generation):
        super().__init__(f"arrêt nommé « {self.nom} » : rôle « {role} », {n} refus écrits à la génération {generation} ; "
                         "la composition gelée n'est plus tenue")
        self.role, self.n, self.generation = role, n, generation


class ArretSeuilsGenerationNA(ArretCourseNA):
    """Arrêt n° 7 : une étape protégée non lancée ou coupée sous les seuils d'une génération ; consigné."""

    numero = 7
    nom = "seuils d'une génération"

    def __init__(self, generation, etape, etat):
        super().__init__(f"arrêt n° 7, seuils d'une génération : génération {generation}, étape « {etape} » ({etat}) ; le "
                         "poste suivant n'est pas lancé")
        self.generation, self.etape, self.etat = generation, etape, etat


class EtapeNeutraliseeJouee(ArretCourseNA):
    """Une étape neutralisée (« passe_tableau », « fusions ») jouée : défaut de configuration, arrêt."""

    nom = "étape neutralisée jouée"


class ArretCablageColonneNA(ArretCourseNA):
    """Refus de câblage (mot de la mère, GO-2026-11-21-69) : en état 1 ou 2 de la colonne « matière première », un contexte
    d'appel dont le journal n'est pas `JournalRequetesColonneNA` (lot 10 a) ; numéro à l'additif. Le message ne dit que le
    moment, l'état, le type du journal et la cause."""

    nom = "câblage de la colonne : journal du contexte d'appel autre que celui de la colonne"

    def __init__(self, moment, etat, journal, cause):
        etat_dit = etat if type(etat) is int else f"non entier ({type(etat).__name__})"
        super().__init__(f"arrêt nommé « {self.nom} » : {moment}, état de la colonne {etat_dit}, journal de type "
                         f"« {type(journal).__name__} » ; {cause} ; le contexte d'appel est refusé")
        self.moment, self.cause = moment, cause
        self.etat_colonne = etat if type(etat) is int else None
        self.type_journal = type(journal).__name__


def refuser_cablage(etat, journal, moment):
    """Le refus de câblage, au départ de la course et à la construction de chaque génération. Rend le nom du type du
    journal reçu ; lève `ArretCablageColonneNA` :
    - si l'état n'est pas l'un de 0, 1, 2 (un entier, non un booléen) ;
    - si l'état est 1 ou 2 et que le journal n'est pas un `JournalRequetesColonneNA` ;
    - (renforcement déclaré) si l'état est 1 ou 2 et que le journal de la colonne porte un contrôle de départ d'un autre
      état, ou sans colonne chargée (la garde y serait muette).
    En état 0, tout journal du lot 3 est reçu (le journal de la colonne aussi)."""
    if type(etat) is not int or etat not in ETATS_COLONNE:
        raise ArretCablageColonneNA(moment, etat, journal, "état de l'interrupteur inconnu (0, 1 ou 2 attendu)")
    if not isinstance(journal, jn.JournalRequetes):
        raise ArretCablageColonneNA(moment, etat, journal, "le journal n'est pas un journal des requêtes du lot 3")
    if etat in ETATS_COLONNE_GARDES:
        # v3 (décision de la mère) : type exact. `type()` lit la classe réelle, non l'attribut `__class__` (qu'un objet
        # peut falsifier) ; une sous-classe ne compte pas comme le journal de la colonne.
        if type(journal) is not mp.JournalRequetesColonneNA:
            raise ArretCablageColonneNA(moment, etat, journal, "en état 1 ou 2, le journal doit être celui de la colonne, "
                                                               "de type exact")
        # Surcharge de l'envoi : ni sur la classe (défense en profondeur, si la classe était modifiée après import), ni
        # sur l'instance (attribut posé sur l'objet).
        if mp.JournalRequetesColonneNA.__dict__.get("journaliser_envoi") is not _ENVOI_DE_LA_COLONNE \
                or "journaliser_envoi" in vars(journal):
            raise ArretCablageColonneNA(moment, etat, journal, "en état 1 ou 2, l'envoi du journal de la colonne est "
                                                               "surchargé")
        depart = journal.depart
        if not isinstance(depart, mp.DepartColonne) or depart.etat != etat or not isinstance(depart.colonne, mp.Colonne):
            raise ArretCablageColonneNA(moment, etat, journal, "le journal de la colonne porte un contrôle de départ d'un "
                                                               "autre état, ou sans colonne chargée")
    return type(journal).__name__


def fabrique_journal_colonne(depart):
    """La fabrique de journal que le lanceur (lot 8) passe à la course : chaque génération reçoit un
    `JournalRequetesColonneNA` neuf, muni du contrôle de départ `depart` (lot 10 a, `preparer_depart`)."""
    if not isinstance(depart, mp.DepartColonne):
        raise DefautLot6("la fabrique du journal de la colonne exige le contrôle de départ (`DepartColonne`)")

    def fabrique(dossier, nom):
        return mp.JournalRequetesColonneNA(dossier, nom, depart=depart)
    return fabrique


def _sceller_si_ouvert(journal):
    if isinstance(journal, jn.JournalRequetes) and not journal.scelle:
        journal.sceller()


class DefautLot6(RuntimeError):
    """Un défaut de programme du lot 6 (une fiche rendue sans classe, un état incohérent) : arrêt, motif dit."""


# Les arrêts, nommés pour le journal des arrêts : (classe, numéro, nom). Les numéros neufs sont à l'additif (None ici).
ARRETS_CONNUS = (
    (cfn.ArretEmpreinteNA, 14, "empreinte d'une pièce scellée différente"),
    (tn.ArretDisjonction, 10, "garde de disjonction"),
    (rq.ArretConsigneTropLongue, 8, "consigne plus longue que sa borne"),
    (vr.RegistreServiNonConforme, None, "registre servi non conforme (n° 8, 9 ou 19)"),
    (rg.ArretGardeCoffre, 5, "garde du coffre"),
    (PlafondDeCourseAtteint, 6, "plafond de la course atteint (réservation impossible)"),
    (CumulCourseAuDela, 6, "cumul de la course au-delà de son plafond"),
    (ArretSeuilsGenerationNA, 7, "seuils d'une génération"),
    (rt.ArretPartCle, 12, "part d'une clé épuisée ou rôle sur une autre clé"),
    (ag.ArretMotifNA, 16, "motif interdit dans un texte à servir"),
    (gm.ArretMotifInterdit, 16, "motif interdit dans un texte à servir"),
    (ag.ArretCreditNA, 13, "refus pour crédit"),
    (ag.ArretClassifieurNA, 1, "refus d'un classifieur de sûreté"),
    (ag.ArretA2NA, None, "A2, modèle servi absent ou changé"),
    (ag.ArretRequeteJournaliseeNA, None, "requête journalisée"),
    (pt.ArretSansPasseportNA, None, "A17, fiche sans passeport du portier neuf"),
    (ArretRemplacementRefusEcritsNA, None, "garde de remplacement : refus écrits d'un même proposeur"),
    (EtapeNeutraliseeJouee, None, "étape neutralisée jouée"),
    (ArretCablageColonneNA, None, "câblage de la colonne : journal du contexte d'appel autre que celui de la colonne"),
    (mp.ArretColonneNA, None, "garde de la colonne « matière première »"),
    (mp.GenerationRefuseeColonneNA, None, "garde de la colonne « matière première », registre servi"),
    (mp.RefusColonneNA, None, "refus de la colonne « matière première »"),
    (NoeudArret, None, "nœud"),
)


def decrire_arret(e):
    """La ligne d'un arrêt, sans contenu : sa classe, son numéro (ou None, à l'additif), son nom et quelques attributs
    sans contenu (rôle, clé, pièce, génération, étape)."""
    for classe, numero, nom in ARRETS_CONNUS:
        if isinstance(e, classe):
            break
    else:
        numero, nom = None, "arrêt non nommé (défaut ou exception de base)"
    d = {"type": type(e).__name__, "numero": numero, "nom": nom}
    if isinstance(e, vr.RegistreServiNonConforme):
        d["numeros"] = list(e.numeros)
    for attr in ("role", "cle", "piece", "generation", "etape", "clause", "famille", "rang", "cause", "n", "moment",
                 "etat_colonne", "type_journal"):
        v = getattr(e, attr, None)
        if isinstance(v, (str, int)) and not isinstance(v, bool):
            d[attr] = v
    return d


# --- journal des arrêts et des générations (E5) ------------------------------------------------------------------------

class JournalArretsGenerationsNA(pt.FichierAjoutSeul):
    """En ajout seul, dans le dossier de sortie, jamais servi, scellé à la clôture. Événements : « départ », « copies de
    configuration », « arrêt », « génération », « cumul par clé » (journal des arrêts n° 11 à n° 13 : le seul lieu du
    cumul par clé), « clôture »."""

    CHAMPS_PERMIS = ("evenement", "generation", "depart", "copies", "arret", "ligne", "cles", "cloture")
    VERSION = "journal-arrets-et-generations-na-v3"
    EVENEMENTS = ("départ", "copies de configuration", "arrêt", "génération", "cumul par clé", "clôture")

    def ecrire(self, evenement, **champs):
        if evenement not in self.EVENEMENTS:
            raise pt.AjoutSeulRefuse("événement hors de la liste fermée")
        return self.ajouter(dict(champs, evenement=evenement))


def lire_journal_arrets_generations(chemin, exiger_sceau=False):
    return pt.relire_ajout_seul(chemin, exiger_sceau=exiger_sceau)


# --- ce que la course donne à une génération ---------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class ContexteGenerationNA:
    """Ce que la course donne à une génération, en plus du contexte d'appel du lot 4."""

    gabarit: rq.Piece
    synthese: rq.Piece
    consigne_portier: rq.Piece
    consigne_juges: rq.Piece
    declaration: pt.DeclarationEtiquettes
    bornes: ct.BornesFiche
    cases: tuple  # rq.CaseServie, dans l'ordre du tirage
    requetes: dict  # (identifiant de case, rôle) -> rq.RequeteAssemblee
    registre: object  # rg.RegistreServi ou None (génération 1)
    seuil_refus_ecrits: int
    table: rt.TableRolesCles
    etat_colonne: object  # 0, 1 ou 2 : l'état de l'interrupteur que la course a reçu (refus de câblage, v2)

    def __post_init__(self):
        for nom in ("gabarit", "synthese", "consigne_portier", "consigne_juges"):
            if not isinstance(getattr(self, nom), rq.Piece):
                raise DefautLot6(f"{nom} : une pièce lue à son empreinte")
        if type(self.seuil_refus_ecrits) is not int or self.seuil_refus_ecrits < 1:
            raise DefautLot6("borne de la garde de remplacement : un entier ≥ 1")


@dataclasses.dataclass
class ReponseGardee:
    texte: str
    case: rq.CaseServie
    role: str
    identifiant: str  # mot réencodé de dix-huit lettres (lot 5, remarque 10)
    jetons_fiche: dict  # rang de la fiche -> jeton du noyau (« f » + douze caractères hexadécimaux)


def _lire_texte(texte):
    """La lecture d'un proposeur : le texte tel que rendu, toujours un objet dès qu'un texte est rendu (§ 2.13, (i))."""
    return texte


def _plus(d, k, n=1):
    d[k] = d.get(k, 0) + n


# --- la génération ------------------------------------------------------------------------------------------------------

class GenerationNA(ag.AppelGardeNA, GenerationV68):
    """La génération du régime : le mélange du lot 4 devant `GenerationV68`."""

    @staticmethod
    def fournisseurs_requis(conf):
        """Seuls les adaptateurs des rôles de la table : proposeurs, aiguilleur, juges (§ 2.9)."""
        return ({p["fournisseur"] for p in conf["proposeurs"]} | {j["fournisseur"] for j in conf["juges"]}
                | {conf["aiguilleur"]["fournisseur"]})

    def __init__(self, conf, sortie, adaptateurs, *, contexte_na, course_na, numero, **kw):
        if not isinstance(course_na, ContexteGenerationNA):
            raise DefautLot6("la génération du véhicule exige le contexte de la course (`ContexteGenerationNA`)")
        if kw.get("heritage_selection") is not None or kw.get("heritage_texte") is not None:
            raise DefautLot6("aucun héritage de la v68 : le registre est servi par la proposition neuve")
        kw["heritage_selection"] = None
        # Refus de câblage à la construction de la génération, avant toute écriture de la v68 et du lot 4.
        refuser_cablage(course_na.etat_colonne, getattr(contexte_na, "journal", None),
                        f"construction de la génération {numero}")
        self.course_na = course_na
        super().__init__(conf, sortie, adaptateurs, contexte_na=contexte_na, numero=numero, **kw)
        if self.na.numero_generation != numero:
            raise DefautLot6("le contexte d'appel n'est pas celui de cette génération")
        self.portier = pt.PortierNA(consigne=course_na.consigne_portier, declaration=course_na.declaration,
                                    bornes=course_na.bornes, appeler=self._appeler_portier, dossier_sortie=sortie,
                                    nom_journal=f"journal-portier-g{numero}.jsonl", generation=numero)
        self.registre_na = rg.RegistreTentatives(sortie, f"registre-tentatives-g{numero}.jsonl")
        self.reponses_na = []
        self.issues_reponses_na = []
        self.passees_na = []
        self.jetons_noyau_na = {}  # identifiant réencodé de la fiche -> jeton du noyau
        self._etat_aiguillage = None
        self._appels_portier = 0
        self.comptes_lot6 = {
            "appels_proposeur": {}, "issues_proposeur": {}, "cases_non_jouees": {}, "refus_ecrits_proposeur": {},
            "verdicts_absents": {}, "appels_juge": {}, "fiches_jugees": 0,
            "registre_servi_recu_par": 0,
        }

    # --- les étapes neutralisées -----------------------------------------------------------------------------------

    def etape_passe_tableau(self, etat):
        raise EtapeNeutraliseeJouee("arrêt « étape neutralisée jouée » : « passe_tableau » est retirée par construction "
                                    "(plafond de relais au-dessus de S17) ; défaut de configuration")

    def etape_fusions(self, etat):
        raise EtapeNeutraliseeJouee("arrêt « étape neutralisée jouée » : « fusions » est retirée par construction "
                                    "(plafond de relais au-dessus de S17) ; défaut de configuration")

    # --- la proposition neuve -----------------------------------------------------------------------------------------

    def _espece(self, role):
        e = self.course_na.table.entree(role)
        return e.espece if e is not None else None

    def _jeton_fiche(self, case, role, rang):
        return "f" + self.graines.jeton_opaque(self.tache("ident", 1, case.identifiant, role, rang), 6)

    def _proposer(self, etat, passe, supplement_par_case=None):
        if passe != 1 or supplement_par_case is not None:
            raise EtapeNeutraliseeJouee("arrêt « étape neutralisée jouée » : seule la proposition (passe 1) est jouée")
        for case in self.course_na.cases:
            for p in self.conf["proposeurs"]:
                role = p["etiquette"]
                requete = self.course_na.requetes[(case.identifiant, role)]
                if requete.registre == rq.REGISTRE_SERVI:
                    self.comptes_lot6["registre_servi_recu_par"] += 1
                _plus(self.comptes_lot6["appels_proposeur"], role)
                a = self.appel(etat, role=role, role_kit=ROLE_KIT_PROPOSEUR, fournisseur=p["fournisseur"], modele=p["modele"],
                               consigne=requete, plafond_role="proposeur", session=("proposition", case.identifiant, role),
                               lire=_lire_texte)
                self._classer_retour_proposeur(a, case, role)
        return []

    def _issue(self, role, issue):
        _plus(self.comptes_lot6["issues_proposeur"].setdefault(role, {}), issue)

    def _classer_retour_proposeur(self, a, case, role):
        if a is None:
            return self._issue(role, ISSUE_NON_LANCE)
        if "refus_ecrit" in a:
            self._issue(role, ISSUE_REFUS_ECRIT)
            _plus(self.comptes_lot6["cases_non_jouees"], str(self._espece(role)))
            _plus(self.comptes_lot6["refus_ecrits_proposeur"], role)
            n = self.comptes_lot6["refus_ecrits_proposeur"][role]
            if n >= self.course_na.seuil_refus_ecrits:
                raise ArretRemplacementRefusEcritsNA(role, n, self.numero)
            return None
        issue = a.get("issue_na")
        if issue == "arrêt n° 1, consigné, non relancé":
            return self._issue(role, ISSUE_ARRET_1)
        if issue == "réponse illisible, cause non établie":
            return self._issue(role, ISSUE_ILLISIBLE_CAUSE)
        if issue == "erreur":
            return self._issue(role, ISSUE_ILLISIBLE_ERREUR)
        if issue != "ok":
            raise DefautLot6("issue d'appel inconnue du mélange du lot 4")
        texte = a.get("lu")
        if texte is None:  # réponse rendue mais non lue (délai d'A3 dépassé, ou aucun texte)
            return self._issue(role, ISSUE_ILLISIBLE_NON_LUE)
        if type(texte) is not str:
            raise DefautLot6("la lecture d'un proposeur rend le texte tel quel")
        self._issue(role, ISSUE_TEXTE_RENDU)
        jeton_rep = "r" + self.graines.jeton_opaque(self.tache("ident-reponse", 1, case.identifiant, role), 6)
        self.reponses_na.append(ReponseGardee(texte, case, role, ident.reencoder_jeton_noyau(jeton_rep, "r", 6), {}))
        return None

    # --- l'étape « aiguillage », surchargée : le portier neuf ----------------------------------------------------------

    def _appeler_portier(self, requete, lire):
        """La fonction `appeler` que le portier du lot 5 reçoit : `self.appel` sous l'étiquette de l'aiguilleur, avec la
        lecture du portier. Rend `None` (non lancé), le `RenduRefusEcrit` (lu **avant** `r` et `lu`, E4), ou le dictionnaire
        du noyau."""
        etat = self._etat_aiguillage
        if etat is None:
            raise DefautLot6("le portier n'appelle que pendant l'étape « aiguillage »")
        self._appels_portier += 1
        ai = self.conf["aiguilleur"]
        a = self.appel(etat, role=ai["etiquette"], role_kit=ROLE_KIT_JUGE, fournisseur=ai["fournisseur"], modele=ai["modele"],
                       consigne=requete, plafond_role="aiguilleur",
                       session=("aiguillage", requete.identifiant_case, self._appels_portier), lire=lire)
        if a is None:
            return None
        if "refus_ecrit" in a:
            return a["refus_ecrit"]
        return a

    def _identifiant_fiche(self, reponse):
        def fabrique(rang):
            jeton = self._jeton_fiche(reponse.case, reponse.role, rang)
            mot = ident.reencoder_jeton_noyau(jeton, "f", 6)
            reponse.jetons_fiche[rang] = jeton
            self.jetons_noyau_na[mot] = jeton
            return mot
        return fabrique

    def etape_aiguillage(self, etat):
        self._etat_aiguillage = etat
        try:
            for rep in self.reponses_na:
                issue = self.portier.traiter_reponse(rep.texte, case=rep.case, identifiant_reponse=rep.identifiant,
                                                     identifiant_fiche=self._identifiant_fiche(rep))
                self.issues_reponses_na.append((rep.role, issue))
                for f in issue.fiches:
                    self.registre_na.ajouter_fiche(f)
                    if f.classe == pt.PASSEE:
                        self.passees_na.append(f)
                        fournisseur = next(p["fournisseur"] for p in self.conf["proposeurs"] if p["etiquette"] == rep.role)
                        self.fiches[f.identifiant] = {"ident": f.identifiant, "contenu": f.contenu, "empreinte": f.empreinte,
                                                      "meta": {"case": f.identifiant_case, "proposeur": rep.role,
                                                               "fournisseur": fournisseur, "origine": "proposition",
                                                               "passe": 1}}
                        self.ordre.append(f.identifiant)
        finally:
            self._etat_aiguillage = None

    # --- l'étape « juges » et la surcharge de `juger` ------------------------------------------------------------------

    def etape_juges(self, etat):
        for f in self.passees_na:
            self.juger(f, LOT_JUGES, etat)

    def identifiant_servi_juge(self, juge, fiche):
        """L'identifiant servi au juge : le jeton du noyau (cinq octets, tâche « anonymisation » sur le jeton de la fiche),
        réencodé dans l'alphabet des syllabes (§ 5.2) : mêmes octets, autre écriture ; aucun tirage neuf."""
        jeton_fiche = self.jetons_noyau_na.get(fiche.identifiant)
        if jeton_fiche is None:
            raise pt.ArretSansPasseportNA("fiche inconnue de cette génération")
        jeton = "F" + self.graines.jeton_opaque(self.tache("anonymisation", juge, jeton_fiche), 5)
        return ident.reencoder_jeton_noyau(jeton, "F", 5), jeton

    def juger(self, fiche, lot, etat):
        """Surcharge de `juger` (§ 2.5) : passeport du portier neuf exigé (A17) ; un appel par juge, sous identifiant
        réencodé ; verdicts au coffre ; présence notée ; A2 quand la version servie d'un juge change."""
        if not isinstance(fiche, pt.IssueFiche):
            raise pt.ArretSansPasseportNA("une fiche présentée à un juge sans passer par le portier neuf")
        self.portier.exiger_passeport(fiche.identifiant, fiche.contenu)
        self.lots_juges.add(lot)
        verdicts, presents = {}, {}
        self.comptes_lot6["fiches_jugees"] += 1
        for j in self.conf["juges"]:
            nom = j["etiquette"]
            ident_servi, _ = self.identifiant_servi_juge(nom, fiche)
            requete = rq.assembler_juge(self.course_na.consigne_juges, fiche.contenu, ident_servi, fiche.identifiant_case,
                                        self.numero)
            _plus(self.comptes_lot6["appels_juge"], nom)
            a = self.appel(etat, role=nom, role_kit=ROLE_KIT_JUGE, fournisseur=j["fournisseur"], modele=j["modele"],
                           consigne=requete, plafond_role="juge",
                           session=("juges", fiche.identifiant_case, nom, fiche.identifiant),
                           lire=lambda t: lire_verdict(t, self.conf["items_juge"]))
            v = None
            if a is None:
                _plus(self.comptes_lot6["verdicts_absents"].setdefault(nom, {}), "non lancé")
            elif "refus_ecrit" in a:
                _plus(self.comptes_lot6["verdicts_absents"].setdefault(nom, {}), "refus écrit")
            else:
                r = a["r"]
                servi = getattr(r, "modele_servi", None)
                if getattr(r, "statut", None) == "ok" and servi:
                    vu = self.modele_servi_juges.setdefault(nom, servi)
                    if vu != servi:
                        raise ag.ArretA2NA(nom, "version servie d'un juge changée entre deux fiches")
                v = a.get("lu")
                if v is None:
                    _plus(self.comptes_lot6["verdicts_absents"].setdefault(nom, {}), "verdict illisible")
            if v is None:
                self.absents_juges[nom] = self.absents_juges.get(nom, 0) + 1
            verdicts[nom] = v
            presents[nom] = v is not None
            self.cles_anonymisation.setdefault(nom, {})[ident_servi] = fiche.identifiant
        self.coffre.deposer(f"verdicts-{lot}-{fiche.identifiant}", {"ident": fiche.identifiant, "empreinte": fiche.empreinte,
                                                                     "verdicts": verdicts})
        self.verdicts_presents[fiche.identifiant] = presents
        return True

    # --- ce que lit la fin de `executer` (v56) ---------------------------------------------------------------------------

    def lot_mesure(self):
        """Les fiches « passées » munies du passeport du portier neuf (la mémoire et le classement des juges les lisent)."""
        return [self.fiches[f.identifiant] for f in self.passees_na]

    # --- fin de génération ------------------------------------------------------------------------------------------------

    def sceller_na(self):
        """Scelle le registre des tentatives et le journal du portier (une fois) ; rend leurs empreintes."""
        rendu = {}
        for nom, o in (("registre_tentatives", self.registre_na), ("journal_portier", self.portier.journal)):
            rendu[nom] = None if o.scelle else o.sceller()
        return rendu

    def verifier_aucune_fiche_sans_classe(self):
        lignes = rg.lire_registre_tentatives(self.registre_na.chemin)
        c = self.portier.comptes()
        if len(lignes) != c["fiches_rendues"] or any(l.get("classe") not in pt.CLASSES_FICHE for l in lignes):
            raise DefautLot6("une fiche rendue sans classe à la fin de la génération")
        return len(lignes)


# --- la course ------------------------------------------------------------------------------------------------------------

def _couts_par_role(consommations):
    """Coût par rôle et par nom d'adaptateur, des seules lignes d'appel (une par appel, § 2.9) ; aucun nom de clé."""
    par_role, par_adaptateur = {}, {}
    for c in consommations:
        if c.get("role") in ("plafond-relais", "coupure", "a14", "m6-lue-reduite") or "statut" not in c:
            continue
        par_role[c["role"]] = round(par_role.get(c["role"], 0.0) + float(c["cout_usd"]), 6)
        f = c.get("fournisseur")
        par_adaptateur[f] = round(par_adaptateur.get(f, 0.0) + float(c["cout_usd"]), 6)
    return par_role, par_adaptateur


def assembler_requetes_proposeurs(contexte, conf, generation, titre_registre, borne_requete):
    """Les requêtes des proposeurs d'une génération, assemblées par le lot 3 et mesurées contre leur borne (arrêt n° 8 :
    départ refusé) ; rend {(identifiant de case, rôle): requête}."""
    requetes = {}
    for case in contexte["cases"]:
        for p in conf["proposeurs"]:
            if generation == 1:
                r = rq.assembler_proposeur(contexte["gabarit"], case, contexte["synthese"], 1)
            else:
                piece = rq.charger_piece("registre servi", contexte["registre"].octets, contexte["registre"].sha256)
                r = rq.assembler_proposeur(contexte["gabarit"], case, contexte["synthese"], generation, piece, titre_registre)
            rq.verifier_borne(r, borne_requete)
            requetes[(case.identifiant, p["etiquette"])] = r
    return requetes


def fabriquer_registre_servi_na(config, generation, chemins_registres, cases_par_generation):
    """Le registre servi des générations 2 et 3 (lot 5), à partir des registres scellés des générations précédentes,
    vérifié par programme sur le fichier entier (arrêts n° 8, 9, 19) avant tout envoi."""
    lignes = []
    for g in range(1, generation):
        lignes.extend(rg.lire_registre_tentatives(chemins_registres[g], exiger_sceau=True))
    servi = rg.fabriquer_registre_servi(lignes, {g: list(cases_par_generation[g]) for g in range(1, generation)}, generation,
                                        permuter_comptes=config.objet["permuter_comptes"])
    noms = [l["identifiant"] for l in lignes if l.get("classe") == pt.PASSEE and l["generation"] < generation]
    cases = [c for g in range(1, generation) for c in cases_par_generation[g]]
    if servi.taille:
        vr.verifier_registre_servi(servi.octets, borne_registre_octets=cfn.borne(config, "registre_octets"),
                                   borne_enonce_octets=cfn.borne(config, "enonce_octets"), noms_attendus=noms,
                                   cases_attendues=cases)
    return servi


def construire_garde(config):
    norm = gm.Normaliseur(gm.lire_donnees_ignorables(config.octets_piece("donnees_ignorables"),
                                                     config.piece("donnees_ignorables").sha256))
    liste = gm.lire_liste_motifs(config.octets_piece("liste_motifs"), config.piece("liste_motifs").sha256, norm)
    return gm.GardeMotifs(liste)


def ligne_de_generation(gen, g, *, copie_sha256, journal, journal_sha256, servi, constat):
    """La ligne de la génération (E6) : chaque source de comptes sous sa clé, telle quelle ; rien n'est renommé ni
    additionné ; « au coffre par refus du portier » reste à part ; aucun contenu, aucun nom de clé. Le journal des
    requêtes est lu scellé."""
    lignes_journal = jn.verifier_journal(journal.chemin, exiger_sceau=True)
    comptes_portier = gen.portier.comptes()
    par_role, par_adaptateur = _couts_par_role(gen.coffre.consommations())
    return {
        "generation": g,
        "cases_servies": [c.identifiant for c in gen.course_na.cases],
        "copie_configuration_sha256": copie_sha256,
        "registre_servi": (None if servi is None else {
            "sha256": servi.sha256, "taille": servi.taille, "lignes": servi.lignes, "lignes_tentative": servi.lignes_tentative,
            "lignes_compte": servi.lignes_compte, "comptes_permutes": servi.comptes_permutes,
            "section": rq.REGISTRE_SERVI if servi.taille else rq.REGISTRE_OMIS,
            "requetes_l_ayant_recu": gen.comptes_lot6["registre_servi_recu_par"]}),
        "comptes_melange_lot_4": gen.na_comptes,
        "comptes_portier_lot_5": comptes_portier,
        "comptes_journal_lot_3": jn.comptes(lignes_journal),
        "comptes_envois_lot_4": ag.comptes_envois_na(lignes_journal),
        "comptes_lot_6": gen.comptes_lot6,
        "au_coffre_par_refus_du_portier": comptes_portier["au_coffre_par_refus_du_portier"],
        "arrets_consignes": gen.na_arrets_consignes,
        "coffre": {"au_coffre": constat.au_coffre, "rendues": constat.rendues, "depasse": constat.depasse,
                   "consigne": constat.consigne},
        "etapes": dict(gen.etapes_etat),
        "cout_generation_usd": round(gen.budget.cumul, 6),
        "cout_par_role_usd": par_role,
        "cout_par_adaptateur_usd": par_adaptateur,
        "memoire": {"fichier": "memoire.json", "servie": False},
        "journal_requetes_sha256": journal_sha256,
        "noeud": gen.noeud,
    }


def _ouvrir_journal(fabrique_journal, sortie, g):
    return fabrique_journal(os.path.join(sortie, DOSSIER_JOURNAUX), f"journal-requetes-g{g}.jsonl")


def executer_course_na_v3(config, sortie, adaptateurs, *, regime, nombre_generations, ligne_accord_usd, additif_sha256,
                          etat_colonne, fabrique_journal, go=None, portes=None, horloge=None, racine_sessions=None,
                          lire_etat_relais=None, crochets=None, gardes_depart_en_plus=()):
    """La course du régime. `config` : une `ConfigurationCourseNA` lue à son empreinte. `adaptateurs` : un dictionnaire
    {nom d'adaptateur: adaptateur}, ou une fabrique `f(sortie) -> (adaptateurs, portes)` appelée une fois la sortie créée
    (moteur réel : les réponses brutes vont dans la sortie). `etat_colonne` (v2) : l'état de l'interrupteur de la colonne
    « matière première », 0, 1 ou 2, sans défaut. `fabrique_journal` (v2) : `f(dossier, nom) -> journal`, appelée une fois
    par génération (le lanceur passe `fabrique_journal_colonne(depart)`), sans défaut. `crochets` (essais) :
    {"avant_execution": f(g, gen), "entre_generations": f(g)}. `gardes_depart_en_plus` (lot 10 a) : des fonctions
    f(g, registre_servi, requetes) jouées au départ de chaque génération, après les gardes du lot 6, avant la réservation.
    Rend le bilan (une ligne par génération)."""
    if type(etat_colonne) is not int or etat_colonne not in ETATS_COLONNE:
        raise ArretCablageColonneNA("départ de la course, avant toute écriture", etat_colonne, None,
                                    "état de l'interrupteur inconnu (0, 1 ou 2 attendu)")
    if not callable(fabrique_journal):
        raise ArretCablageColonneNA("départ de la course, avant toute écriture", etat_colonne, fabrique_journal,
                                    "fabrique de journal absente")
    crochets = dict(crochets or {})
    epingle = next((p.sha256 for p in config.pieces_epinglees if p.nom == "additif du véhicule"), None)
    plafond_course = cfn.verifier_regime(config, regime=regime, nombre_generations=nombre_generations,
                                         ligne_accord_usd=ligne_accord_usd, additif_sha256=additif_sha256,
                                         additif_epingle_sha256=epingle)
    gardes = cfn.verifier_gardes_heritees(config)
    cfn.verifier_empreintes(config, "départ de la course")
    table = cfn.table_de_course(config)
    garde = construire_garde(config)
    gabarit, synthese, consigne_portier, consigne_juges = cfn.charger_pieces_servies(config)
    tirage = cfn.lire_tirage(config)
    cases = rq.cases_du_tirage(tirage, gabarit)
    declaration, bornes = cfn.declaration_portier(config), cfn.bornes_fiche(config)
    borne_requete = cfn.borne(config, "requete_proposeur_octets")
    seuil = config.gardes["garde_remplacement_refus_ecrits_proposeur"]
    if os.path.exists(sortie):
        raise cfn.ConfigurationCourseRefusee("sortie déjà présente : jamais écrasée (R12)")
    os.makedirs(os.path.join(sortie, DOSSIER_JOURNAUX))
    journal_arrets = JournalArretsGenerationsNA(sortie, NOM_JOURNAL_ARRETS)
    if callable(adaptateurs):  # moteur réel : les adaptateurs écrivent leurs réponses brutes dans la sortie, créée ici
        adaptateurs, portes_fabriquees = adaptateurs(sortie)
        portes = portes if portes is not None else portes_fabriquees
    copies = {g: cfn.deriver_copie_generation(config, cases[str(g)]) for g in (1, 2, 3)}
    journal_arrets.ecrire("départ", depart={"version": VERSION, "regime": cfn.REGIME, "gardes_heritees": gardes,
                                            "plafond_course_usd": plafond_course, "empreintes": cfn.table_des_empreintes(config),
                                            "statut_des_valeurs": config.statut, "go": go, "etat_colonne": etat_colonne})
    journal_arrets.ecrire("copies de configuration", copies={str(g): copies[g][1] for g in copies})
    cumul = rt.CumulParCle(table)
    budget = GardeBudgetCourseV68(plafond_course)
    s17 = float(config.objet["plafond_generation_usd"])
    memoire, bilan, arret, registres, cases_ids = None, [], None, {}, {}
    poste, g = None, None
    journal_g1 = None
    with ArretSurSignal() as signal:
        try:
            # Refus de câblage au départ de la course : le journal de la génération 1, fait par la fabrique.
            journal_g1 = _ouvrir_journal(fabrique_journal, sortie, 1)
            refuser_cablage(etat_colonne, journal_g1, "départ de la course")
            for g in range(1, nombre_generations + 1):
                poste = f"generation-{g}"
                moment = f"départ de la génération {g}"
                cfn.verifier_empreintes(config, moment)
                copie, copie_sha = crochets.get("copie", lambda g_, c: c)(g, copies[g][0]), copies[g][1]
                cfn.verifier_copie(copie, copie_sha, g)
                tn.garde_disjonction(tirage, g, cfn.triplets_de_la_copie(copie, tirage, g))
                cases_g = tuple(cases[str(g)])
                cases_ids[g] = [c.identifiant for c in cases_g]
                servi = None if g == 1 else fabriquer_registre_servi_na(config, g, registres, cases_ids)
                ctx = {"cases": cases_g, "gabarit": gabarit, "synthese": synthese, "registre": servi}
                requetes = assembler_requetes_proposeurs(ctx, copie, g, config.objet["titre_registre"], borne_requete)
                for f in gardes_depart_en_plus:
                    f(g, servi, requetes)
                budget.reserver(poste, s17)
                journal = journal_g1 if g == 1 else _ouvrir_journal(fabrique_journal, sortie, g)
                contexte_na = ag.ContexteAppelGardeNA(
                    numero_generation=g, table=table, parts=dict(config.objet["parts_usd"]),
                    pires_par_role=dict(config.objet["pires_par_role_usd"]), journal=journal, garde=garde,
                    identifiant_case_de_session=lambda s: s[1], cumul=cumul, lire_etat_relais=lire_etat_relais,
                    portee_arret_1=config.objet["portee_arret_1"])
                course_na = ContexteGenerationNA(gabarit, synthese, consigne_portier, consigne_juges, declaration, bornes,
                                                 cases_g, requetes, servi, seuil, table, etat_colonne=etat_colonne)
                rs = None if racine_sessions is None else os.path.join(racine_sessions, f"generation-{g}")
                gen = None
                try:
                    gen = GenerationNA(copie, os.path.join(sortie, f"generation-{g}"), adaptateurs, contexte_na=contexte_na,
                                       course_na=course_na, numero=g, memoire=memoire, go=go, horloge=horloge,
                                       racine_sessions=rs, portes=portes)
                    if "avant_execution" in crochets:
                        crochets["avant_execution"](g, gen)
                    gen.executer()
                except BaseException:
                    budget.noter_arret(poste, gen.budget.cumul if gen is not None else 0.0)
                    if gen is not None:
                        gen.sceller_na()
                    _sceller_si_ouvert(journal)
                    raise
                budget.compter(poste, gen.budget.cumul)
                gen.sceller_na()
                registres[g] = gen.registre_na.chemin
                if gen.noeud:
                    etape = next((n for n, e in gen.etapes_etat.items() if e == NON_MESUREE), None)
                    if not journal.scelle:
                        journal.sceller()
                    if etape is not None:
                        raise ArretSeuilsGenerationNA(g, etape, gen.etapes_etat[etape])
                    raise NoeudArret(f"génération {g} : nœud")
                gen.verifier_aucune_fiche_sans_classe()
                journal_sha = journal.sceller()
                constat = rg.garde_du_coffre(rg.lire_registre_tentatives(gen.registre_na.chemin, exiger_sceau=True), g)
                ligne = ligne_de_generation(gen, g, copie_sha256=copie_sha, journal=journal, journal_sha256=journal_sha,
                                            servi=servi, constat=constat)
                bilan.append(ligne)
                journal_arrets.ecrire("génération", generation=g, ligne=ligne)
                journal_arrets.ecrire("cumul par clé", generation=g, cles={
                    "cumul": cumul.etat(), "cause_non_etablie_par_cle": gen.na_journal_arrets_cles["cause_non_etablie"],
                    "etat_relais_illisible_par_cle": gen.na_journal_arrets_cles["etat_relais_illisible"]})
                memoire = gen.memoire
                poste = None
                if "entre_generations" in crochets:
                    crochets["entre_generations"](g)
        except BaseException as e:
            refus_sceau_g1 = None
            try:  # le journal de la génération 1, ouvert au départ, scellé s'il n'a pas servi
                _sceller_si_ouvert(journal_g1)
            except (jn.JournalRefuse, OSError) as e_sceau:
                refus_sceau_g1 = type(e_sceau).__name__
            arret = decrire_arret(e)
            arret["poste"] = poste
            arret["generation"] = g
            if refus_sceau_g1 is not None:  # dit, jamais tu (R5)
                arret["journal_requetes_g1"] = f"scellement refusé ({refus_sceau_g1})"
            if isinstance(e, (KeyboardInterrupt, ArretParSignal)):
                arret["motif"] = motif_arret(e)
            try:
                journal_arrets.ecrire("arrêt", generation=g, arret=arret)
            except (pt.AjoutSeulRefuse, OSError):
                arret["ligne_d_arret"] = "écriture refusée par le journal des arrêts : dite au bilan"
            raise
        finally:
            signal.nettoyage()
            ecrire_json_scelle(os.path.join(sortie, NOM_BILAN), {
                "version": VERSION, "regime": cfn.REGIME, "go": go, "generations": bilan, "arret": arret,
                "signaux": signal.etat(), "budget_course": budget.etat(), "statut_des_valeurs": config.statut})
            journal_arrets.ecrire("clôture", cloture={"generations_completes": len(bilan), "arret": arret})
            journal_arrets.sceller()
    return bilan


__all__ = ("GenerationNA", "ContexteGenerationNA", "executer_course_na_v3", "JournalArretsGenerationsNA",
           "ArretCablageColonneNA", "refuser_cablage", "fabrique_journal_colonne", "ETATS_COLONNE",
           "lire_journal_arrets_generations", "ArretCourseNA", "ArretRemplacementRefusEcritsNA", "ArretSeuilsGenerationNA",
           "EtapeNeutraliseeJouee", "DefautLot6", "decrire_arret", "ligne_de_generation", "assembler_requetes_proposeurs",
           "fabriquer_registre_servi_na", "construire_garde", "NOM_JOURNAL_ARRETS", "NOM_BILAN", "VERSION")
