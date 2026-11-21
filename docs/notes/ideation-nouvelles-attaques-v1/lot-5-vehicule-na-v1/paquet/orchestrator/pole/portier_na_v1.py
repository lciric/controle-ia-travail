"""Véhicule NA-1, lot 5 — le portier, code neuf (`portier_na_v1`) : lecture des seules étiquettes de D3, deux sortes
d'appel, passeports, journal sans contenu.

Lettre : V9 (`864f39a7…`), l. 88 (trois classes, garde « concret »), l. 92 à 101 (classes d'issue d'appel), l. 148 (classes
d'issue de fiche), l. 375 et 376 (arrêts n° 4 et n° 5) ; conception du véhicule v5 (`1b7f6822…`), § 0 bis (D6 ; D13 ;
07:46Z, mots 1, 2 et 8 ; 07:51Z : portier neuf, refus écrit « au coffre »), § 2.4 (portier et ses classes), § 2.13 (ce
que rend un refus écrit, par rôle), § 5.1 (interface), § 6.2 (portier forme ; classes d'issue d'appel ; portier neuf ; ce
que rend un refus écrit), § 7 (lot 5).

**Ce que ce portier n'appelle pas** : ni la classe d'aiguilleur du noyau, ni sa lecture (`aiguilleur_v53`), ni son passeport.
Il appelle la fonction `appeler` que lui donne la génération (lot 6), qui passe par `self.appel`, donc par la surcharge du
lot 4, sous l'étiquette de rôle de l'aiguilleur, avec **sa propre fonction de lecture**.

**Les deux sortes d'appel** (§ 2.4) : (a) l'appel « fiche » : la consigne de D3, puis une fiche (`assembler_portier_fiche`) ;
(b) l'appel « réponse sans fiche » : la même consigne, puis le texte d'une réponse où le lecteur n'a reconnu aucune fiche
(`assembler_portier_reponse_sans_fiche` ; forme tranchée par la mère : titre `## La réponse`, objet `{"reponse": texte}`).

**Lecture des étiquettes** (`lire_etiquette`) : elle lit **les étiquettes fermées de la consigne de D3, et elles seules**,
dans la forme que la déclaration fixe. Forme connue de ce code : « ligne ancrée » : une ligne de la réponse, blancs de
tête et de queue retirés, faite de la clé déclarée, de deux-points, et d'une étiquette de la liste fermée, à l'octet. Une
étiquette hors liste, absente ou double vaut « illisible ». La lecture rend **toujours un objet** dès qu'un texte lui est
donné (§ 2.13) : le suivi des rôles du noyau ne compte donc jamais d'échec pour le portier. *La consigne de D3 et sa
déclaration ne sont pas écrites à ce jour : les essais tournent sur un brouillon d'essai factice, déclaré comme tel.*

**Ordre décidé par la mère (D6)** : (i) forme, par programme (`contrat_fiche_na_v1`) : un champ en plus, une valeur qui
n'est pas une chaîne, une valeur au-dessus de sa borne : « au coffre », **sans appel au modèle** ; (ii) modèle :
« concret » : « au coffre » ; illisible, réponse non lue, appel refusé par écrit ou non lancé : « au coffre », compté à part
sous sa cause ; (iii) programme : un champ fermé qui diffère à l'octet de la ligne de case : « hors case » (arrêt n° 4) ;
(iv) sinon « passée », avec un passeport. Le champ `case` qui diffère de l'identifiant servi est consigné et compté ; la
classe ne change pas (07:46Z, mot 2). **Aucune fiche rendue ne reste sans classe.**

**Passeports** : l'identifiant de la fiche (dix-huit lettres, réencodé, § 5.2) et l'empreinte du texte classé (les octets de
la fiche servie au portier : `json.dumps(contenu, ensure_ascii=False, indent=1)`), délivrés à la seule fiche « passée ».
`exiger_passeport` les exige (A17 sous le portier neuf : `ArretSansPasseportNA`, arrêt nommé de course, numéroté à
l'additif) ; le passeport de l'aiguilleur du noyau n'est lu par personne.

**Journal** : ajout seul, dans le dossier de sortie, scellé à la fin de la génération ; une ligne par classement :
identifiant, sorte, génération, case, empreinte, classe, cause ; **aucun contenu**.

Un refus de la garde de motifs (arrêt n° 16) ou un arrêt de course levé par la surcharge d'`appel` traverse le portier sans
être attrapé : ce sont des arrêts de la course. Aucun message d'erreur ne recopie un octet d'une fiche ou d'une réponse.
Bibliothèque standard, et les modules des lots 1, 3 et 5.
"""

import collections
import dataclasses
import hashlib
import json
import os
import re
from collections.abc import Mapping

from pole import contrat_fiche_na_v1 as ct
from pole import identifiants_na_v1 as ident
from pole import journal_na_v3 as jn
from pole import lecteur_fiches_na_v1 as lf
from pole import requete_na_v3 as rq

VERSION = "portier-na-v1"

# Classes (V9, l. 92 à 101, 148).
PASSEE, AU_COFFRE, HORS_CASE = "passée", "au coffre", "hors case"
CLASSES_FICHE = (PASSEE, AU_COFFRE, HORS_CASE)
FICHES_RENDUES = "fiches rendues"
VIDE_MOTIVEE, REFUS_DU_MODELE, ILLISIBLE = "réponse vide motivée", "refus du modèle", "réponse illisible"
CLASSES_APPEL = (FICHES_RENDUES, VIDE_MOTIVEE, REFUS_DU_MODELE, ILLISIBLE)

# Sens des étiquettes fermées (§ 2.4) ; la déclaration leur associe le texte que la consigne fixe.
NIVEAU_IDEE, CONCRET = "niveau de l'idée", "concret"
SENS_FICHE = (NIVEAU_IDEE, CONCRET)
SENS_REPONSE = (VIDE_MOTIVEE, REFUS_DU_MODELE, ILLISIBLE)
SORTE_FICHE, SORTE_REPONSE = "fiche", "réponse sans fiche"
FORME_LIGNE_ANCREE = "ligne ancrée"

# Causes, liste fermée.
CAUSE_PASSEE = "passée"
CAUSE_CONCRET = "concret"
CAUSE_ETIQUETTE_ILLISIBLE = "étiquette du portier illisible"
CAUSE_NON_LUE = "réponse du portier non lue"
CAUSE_REFUS_ECRIT_FICHE = "au coffre par refus du portier"
CAUSE_REFUS_ECRIT_REPONSE = "appel du portier refusé par écrit"
CAUSE_NON_LANCE = "appel du portier non lancé"
CAUSE_HORS_CASE = "champ fermé différent"
CAUSE_ETIQUETTE_LUE = "étiquette lue"
CAUSES_FICHE = (CAUSE_PASSEE, ct.CAUSE_CHAMP_EN_PLUS, ct.CAUSE_TYPE, ct.CAUSE_LONGUEUR, CAUSE_CONCRET,
                CAUSE_ETIQUETTE_ILLISIBLE, CAUSE_NON_LUE, CAUSE_REFUS_ECRIT_FICHE, CAUSE_NON_LANCE, CAUSE_HORS_CASE)
CAUSES_REPONSE = (CAUSE_ETIQUETTE_LUE, CAUSE_ETIQUETTE_ILLISIBLE, CAUSE_NON_LUE, CAUSE_REFUS_ECRIT_REPONSE,
                  CAUSE_NON_LANCE)
# Sous-compte des réponses illisibles nées du portier (§ 2.4 ; § 2.8, M6).
SOUS_COMPTE_PORTIER = "étiquette du portier illisible"

OCTETS_IDENTIFIANT = 6
NOM_ARRET_A17 = "A17, fiche sans passeport du portier neuf"
_FINS_DE_LIGNE = re.compile(r"\r\n|\n|\r")


class PortierRefuse(RuntimeError):
    """Un défaut de programme autour du portier (entrée mal formée, identifiant redit, issue d'appel inconnue) ; le message
    ne recopie aucun contenu."""


class ArretSansPasseportNA(RuntimeError):
    """A17 sous le portier neuf : une fiche présentée à un juge sans le passeport de ce portier, ou dont le texte n'est plus
    celui qui a été classé. Arrêt nommé de la course ; son numéro est donné par l'additif."""

    nom = NOM_ARRET_A17

    def __init__(self, cause):
        super().__init__(f"{NOM_ARRET_A17} : {cause} ; arrêt nommé de la course")
        self.cause = cause


# --- déclaration des étiquettes (D3) ------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class DeclarationEtiquettes:
    """La forme des étiquettes que la consigne de D3 fixe et que l'additif déclare : la forme, la clé, et pour chaque
    sorte d'appel le texte de chaque étiquette fermée, par son sens. `statut` dit d'où elle vient."""

    forme: str
    cle: str
    fiche: tuple  # ((sens, texte), …)
    reponse_sans_fiche: tuple
    statut: str

    def textes(self, sorte):
        return dict(self.fiche if sorte == SORTE_FICHE else self.reponse_sans_fiche)


def _texte_d_etiquette(t):
    return type(t) is str and t != "" and t == t.strip() and _FINS_DE_LIGNE.search(t) is None


def declaration_de(*, forme, cle, fiche, reponse_sans_fiche, statut):
    """Construit et vérifie une déclaration : forme connue, clé d'une ligne, sens complets, textes distincts."""
    if forme != FORME_LIGNE_ANCREE:
        raise PortierRefuse("forme d'étiquette inconnue de ce code")
    if not _texte_d_etiquette(cle) or ":" in cle:
        raise PortierRefuse("clé d'étiquette : une chaîne d'une ligne, sans deux-points")
    for sens_attendus, d in ((SENS_FICHE, fiche), (SENS_REPONSE, reponse_sans_fiche)):
        if not isinstance(d, dict) or set(d) != set(sens_attendus):
            raise PortierRefuse("déclaration : chaque sens fermé reçoit un texte, et aucun autre")
        if not all(_texte_d_etiquette(t) for t in d.values()) or len(set(d.values())) != len(d):
            raise PortierRefuse("déclaration : des textes d'une ligne, distincts")
    if type(statut) is not str or not statut:
        raise PortierRefuse("déclaration : son statut est dit")
    return DeclarationEtiquettes(forme, cle, tuple((s, fiche[s]) for s in SENS_FICHE),
                                 tuple((s, reponse_sans_fiche[s]) for s in SENS_REPONSE), statut)


@dataclasses.dataclass(frozen=True)
class LectureEtiquette:
    """Ce que la lecture du portier rend, toujours : la sorte d'appel, le sens lu (ou None, illisible) et la cause."""

    sorte: str
    sens: object
    cause: str  # « lue », « absente », « hors liste », « double »


def lire_etiquette(texte, sorte, declaration):
    """Lit l'étiquette d'une réponse du modèle portier ; rend toujours une `LectureEtiquette` pour un texte."""
    if sorte not in (SORTE_FICHE, SORTE_REPONSE):
        raise PortierRefuse("sorte d'appel inconnue")
    if not isinstance(declaration, DeclarationEtiquettes):
        raise PortierRefuse("la déclaration est construite par `declaration_de`")
    if type(texte) is not str:
        raise PortierRefuse("la lecture du portier lit un texte")
    motif = re.compile(r"^" + re.escape(declaration.cle) + r"[ \t]*:[ \t]*(?P<v>.*?)[ \t]*$")
    trouvees = []
    for ligne in _FINS_DE_LIGNE.split(texte):
        m = motif.match(ligne.strip())
        if m is not None:
            trouvees.append(m.group("v"))
    if not trouvees:
        return LectureEtiquette(sorte, None, "absente")
    if len(trouvees) > 1:
        return LectureEtiquette(sorte, None, "double")
    par_texte = {t: s for s, t in declaration.textes(sorte).items()}
    if trouvees[0] not in par_texte:
        return LectureEtiquette(sorte, None, "hors liste")
    return LectureEtiquette(sorte, par_texte[trouvees[0]], "lue")


# --- issues et passeports ----------------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class Passeport:
    """Délivré à la seule fiche « passée » : son identifiant et l'empreinte du texte classé."""

    identifiant: str
    empreinte: str
    generation: object
    identifiant_case: str


@dataclasses.dataclass(frozen=True)
class IssueFiche:
    """La classe d'une fiche rendue, sa cause, et ce qu'en lisent le registre et la surcharge de `juger`. Le contenu reste
    dans la mémoire du véhicule (dossier de sortie) ; il n'est jamais écrit au journal du portier."""

    identifiant: str
    generation: object
    identifiant_case: str
    classe: str
    cause: str
    case_differe: bool
    empreinte: str
    passeport: object
    contenu: dict
    defauts_de_forme: tuple  # causes de forme relevées (toutes), pour les comptes


@dataclasses.dataclass(frozen=True)
class IssueReponse:
    """La classe d'issue d'un appel de proposeur et, s'il y a des fiches, leurs issues."""

    identifiant: str
    generation: object
    identifiant_case: str
    classe_appel: str
    cause: str
    sous_compte: object
    fiches: tuple
    non_reconnus: tuple


def empreinte_texte_classe(contenu):
    """L'empreinte des octets de la fiche servie au portier (forme du noyau, déclarée : mot 8 de 07:46Z)."""
    return hashlib.sha256(json.dumps(contenu, ensure_ascii=False, indent=rq.INDENTATION_JSON).encode("utf-8")).hexdigest()


def _sha256(octets):
    return hashlib.sha256(octets).hexdigest()


# --- fichier en ajout seul ---------------------------------------------------------------------------------------------

class AjoutSeulRefuse(RuntimeError):
    """Écriture refusée dans un fichier en ajout seul ; le message ne recopie aucun contenu."""


class FichierAjoutSeul:
    """Un fichier de lignes JSON, créé neuf dans le dossier de sortie, écrit en ajout seul ; relu et comparé avant chaque
    ajout ; chaque ligne porte son rang et l'empreinte de la précédente ; scellé par un compagnon `.sha256`."""

    CHAMPS_PERMIS = ()
    VERSION = VERSION

    def __init__(self, dossier_sortie, nom_fichier):
        if type(nom_fichier) is not str or os.path.basename(nom_fichier) != nom_fichier or not nom_fichier.endswith(".jsonl"):
            raise AjoutSeulRefuse("un nom de fichier simple, fini par « .jsonl »")
        if not os.path.isdir(dossier_sortie):
            raise AjoutSeulRefuse("le dossier de sortie doit exister")
        self.chemin = os.path.join(dossier_sortie, nom_fichier)
        if os.path.exists(self.chemin) or os.path.exists(self.chemin + ".sha256"):
            raise AjoutSeulRefuse("fichier existant : on n'écrase jamais (R12)")
        with open(self.chemin, "xb"):
            pass
        self._taille, self._empreinte, self._precedente, self._rang, self._scelle = 0, _sha256(b""), "aucune", 0, False

    def _verifier_intact(self):
        try:
            with open(self.chemin, "rb") as f:
                present = f.read()
        except OSError:
            raise AjoutSeulRefuse("le fichier n'est plus lisible : écriture refusée") from None
        if len(present) != self._taille or _sha256(present) != self._empreinte:
            raise AjoutSeulRefuse("le fichier ne porte plus ce qui y a été écrit : écriture refusée")
        return present

    def ajouter(self, champs):
        if self._scelle:
            raise AjoutSeulRefuse("fichier scellé : aucun ajout")
        inconnus = set(champs) - set(self.CHAMPS_PERMIS)
        if inconnus:
            raise AjoutSeulRefuse("champ hors de la liste fermée")
        present = self._verifier_intact()
        ligne = dict(champs, rang=self._rang + 1, precedente=self._precedente, version=self.VERSION)
        octets = (json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
        with open(self.chemin, "ab") as f:
            f.write(octets)
        self._taille += len(octets)
        self._empreinte = _sha256(present + octets)
        self._precedente = _sha256(octets)
        self._rang += 1
        return ligne

    def sceller(self):
        if self._scelle:
            raise AjoutSeulRefuse("déjà scellé")
        self._verifier_intact()
        with open(self.chemin + ".sha256", "x", encoding="utf-8") as f:
            f.write(f"{self._empreinte}  {os.path.basename(self.chemin)}\n")
        self._scelle = True
        return self._empreinte

    @property
    def scelle(self):
        return self._scelle


def relire_ajout_seul(chemin, exiger_sceau=False):
    """Relit un fichier en ajout seul : rangs sans trou, chaînage, compagnon s'il existe (exigé si demandé)."""
    with open(chemin, "rb") as f:
        octets = f.read()
    if octets and not octets.endswith(b"\n"):
        raise AjoutSeulRefuse("fichier coupé au milieu d'une ligne")
    lignes, precedente = [], "aucune"
    for i, brute in enumerate(octets.splitlines(keepends=True), start=1):
        try:
            ligne = json.loads(brute.decode("utf-8"))
        except (UnicodeDecodeError, ValueError):
            raise AjoutSeulRefuse(f"ligne {i} illisible") from None
        if not isinstance(ligne, dict) or ligne.get("rang") != i or ligne.get("precedente") != precedente \
                or (json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8") != brute:
            raise AjoutSeulRefuse(f"ligne {i} : rang, chaînage ou forme rompus")
        precedente = _sha256(brute)
        lignes.append(ligne)
    compagnon = chemin + ".sha256"
    if exiger_sceau and not os.path.exists(compagnon):
        raise AjoutSeulRefuse("fichier non scellé")
    if os.path.exists(compagnon):
        with open(compagnon, encoding="utf-8") as f:
            if f.read().split()[0] != _sha256(octets):
                raise AjoutSeulRefuse("le compagnon ne porte pas l'empreinte du fichier")
    return tuple(lignes)


class JournalPortier(FichierAjoutSeul):
    """Le journal du portier : sans contenu ; identifiant, sorte, génération, case, empreinte, classe, cause."""

    CHAMPS_PERMIS = ("identifiant", "sorte", "generation", "case", "empreinte", "classe", "cause", "case_differe",
                     "appel_au_modele")
    VERSION = "journal-portier-na-v1"


# --- le portier ---------------------------------------------------------------------------------------------------------

class PortierNA:
    """Le portier d'une génération (ou de l'épreuve des témoins) : une consigne de D3, sa déclaration, les bornes, et la
    fonction `appeler(requete, lire)` que donne la génération (lot 6), qui rend `None` (appel non lancé), un
    `journal_na_v3.RenduRefusEcrit` (refus écrit), ou le dictionnaire du noyau (`{"lu": …, …}`)."""

    def __init__(self, *, consigne, declaration, bornes, appeler, dossier_sortie, nom_journal, generation=None):
        if not isinstance(consigne, rq.Piece):
            raise PortierRefuse("la consigne de D3 est une pièce lue à son empreinte (`requete_na_v3`)")
        if not isinstance(declaration, DeclarationEtiquettes):
            raise PortierRefuse("la déclaration est construite par `declaration_de`")
        if not isinstance(bornes, ct.BornesFiche):
            raise PortierRefuse("les bornes sont construites par `contrat_fiche_na_v1.bornes_de`")
        if not callable(appeler):
            raise PortierRefuse("`appeler` est la fonction d'appel de la génération")
        if generation is not None and (type(generation) is not int or generation not in (1, 2, 3)):
            raise PortierRefuse("génération hors de 1 à 3")
        self.consigne, self.declaration, self.bornes, self._appeler = consigne, declaration, bornes, appeler
        self.generation = generation
        self.journal = JournalPortier(dossier_sortie, nom_journal)
        self._passeports = {}
        self._identifiants = set()
        self._issues_fiches = []
        self._issues_reponses = []
        self.appels_au_modele = 0

    # --- outils -------------------------------------------------------------------------------------------------------

    def _identifiant(self, mot):
        try:
            ident.decoder_octets(mot, OCTETS_IDENTIFIANT)
        except (ident.MotRefuse, ident.EncodageRefuse):
            raise PortierRefuse("identifiant : un mot réencodé de dix-huit lettres (§ 5.2)") from None
        if mot in self._identifiants:
            raise PortierRefuse("identifiant déjà classé par ce portier")
        self._identifiants.add(mot)
        return mot

    def _verifier_case(self, case):
        if not isinstance(case, rq.CaseServie):
            raise PortierRefuse("la case est une case du tirage (`requete_na_v3.CaseServie`)")
        ct.valeurs_de_la_case(case)
        return case

    def _appeler_modele(self, requete, sorte):
        """Rend (sens, cause) ; sens None si rien n'est lisible. Le refus de la garde de motifs et les arrêts de course
        levés par la surcharge d'`appel` ne sont pas attrapés."""
        self.appels_au_modele += 1
        issue = self._appeler(requete, lambda texte: lire_etiquette(texte, sorte, self.declaration))
        if issue is None:
            return None, CAUSE_NON_LANCE
        if isinstance(issue, jn.RenduRefusEcrit):
            if issue.sorte != requete.sorte:
                raise PortierRefuse("refus écrit d'une autre sorte d'appel que celle qui a été présentée")
            return None, (CAUSE_REFUS_ECRIT_FICHE if sorte == SORTE_FICHE else CAUSE_REFUS_ECRIT_REPONSE)
        if isinstance(issue, Mapping) and "lu" in issue:
            lu = issue["lu"]
            if lu is None:
                return None, CAUSE_NON_LUE
            if not isinstance(lu, LectureEtiquette) or lu.sorte != sorte:
                raise PortierRefuse("lecture d'une autre fonction que celle du portier")
            if lu.sens is None:
                return None, CAUSE_ETIQUETTE_ILLISIBLE
            return lu.sens, CAUSE_ETIQUETTE_LUE
        raise PortierRefuse("issue d'appel inconnue : ni « non lancé », ni refus écrit, ni résultat du noyau")

    def _consigner(self, *, identifiant, sorte, case, empreinte, classe, cause, case_diff, appel):
        self.journal.ajouter({"identifiant": identifiant, "sorte": sorte, "generation": self.generation,
                              "case": case.identifiant, "empreinte": empreinte, "classe": classe, "cause": cause,
                              "case_differe": case_diff, "appel_au_modele": appel})

    # --- les deux sortes d'appel ---------------------------------------------------------------------------------------

    def lire_reponse(self, texte):
        """Le lecteur neuf : rend toujours une `Lecture` pour un texte."""
        return lf.lire_fiches(texte)

    def classer_fiche(self, fiche, *, identifiant, case):
        """(i) forme, (ii) modèle, (iii) hors case, (iv) passée ; rend une `IssueFiche`, jamais sans classe."""
        if not isinstance(fiche, lf.FicheLue):
            raise PortierRefuse("seule une fiche lue par `lecteur_fiches_na_v1` se classe")
        case = self._verifier_case(case)
        identifiant = self._identifiant(identifiant)
        verdict = ct.verifier(fiche, self.bornes)
        contenu = fiche.contenu()
        case_diff = ct.case_differe(contenu, case.identifiant)
        defauts = tuple(c for c, l in ((ct.CAUSE_CHAMP_EN_PLUS, verdict.champs_en_plus), (ct.CAUSE_TYPE, verdict.types_faux),
                                       (ct.CAUSE_LONGUEUR, verdict.hors_longueur)) if l)
        appel = False
        passeport = None
        if not verdict.au_contrat:  # (i) forme : le modèle n'est pas appelé
            classe, cause = AU_COFFRE, verdict.cause
            empreinte = _sha256(json.dumps(contenu, ensure_ascii=False, sort_keys=True, default=repr).encode("utf-8"))
        else:
            requete = rq.assembler_portier_fiche(self.consigne, contenu, case.identifiant, self.generation)
            empreinte = empreinte_texte_classe(contenu)
            servie = [e for e in requete.composition if e.nom == "fiche servie"]
            if len(servie) != 1 or servie[0].sha256 != empreinte:
                raise PortierRefuse("la fiche servie n'a pas l'empreinte du texte classé")
            appel = True
            sens, cause_appel = self._appeler_modele(requete, SORTE_FICHE)  # (ii) modèle
            if sens is None:
                classe, cause = AU_COFFRE, cause_appel
            elif sens == CONCRET:
                classe, cause = AU_COFFRE, CAUSE_CONCRET
            elif ct.champs_fermes_differents(contenu, case):  # (iii) hors case, arrêt n° 4
                classe, cause = HORS_CASE, CAUSE_HORS_CASE
            else:  # (iv)
                classe, cause = PASSEE, CAUSE_PASSEE
                passeport = Passeport(identifiant, empreinte, self.generation, case.identifiant)
                self._passeports[identifiant] = passeport
        self._consigner(identifiant=identifiant, sorte=SORTE_FICHE, case=case, empreinte=empreinte, classe=classe,
                        cause=cause, case_diff=case_diff, appel=appel)
        issue = IssueFiche(identifiant, self.generation, case.identifiant, classe, cause, case_diff, empreinte, passeport,
                           contenu, defauts)
        self._issues_fiches.append(issue)
        return issue

    def classer_reponse_sans_fiche(self, texte, *, identifiant_reponse, case, non_reconnus=()):
        """L'appel « réponse sans fiche » : une des trois étiquettes ; illisible, refus écrit, non lue ou non lancé :
        « réponse illisible », sous-compte « étiquette du portier illisible »."""
        if type(texte) is not str:
            raise PortierRefuse("une réponse sans fiche est un texte rendu")
        case = self._verifier_case(case)
        identifiant = self._identifiant(identifiant_reponse)
        requete = rq.assembler_portier_reponse_sans_fiche(self.consigne, texte, case.identifiant, self.generation)
        sens, cause = self._appeler_modele(requete, SORTE_REPONSE)
        if sens is None:
            classe, sous_compte = ILLISIBLE, SOUS_COMPTE_PORTIER
        else:
            classe, sous_compte = sens, None
        empreinte = _sha256(texte.encode("utf-8"))
        self._consigner(identifiant=identifiant, sorte=SORTE_REPONSE, case=case, empreinte=empreinte, classe=classe,
                        cause=cause, case_diff=False, appel=True)
        issue = IssueReponse(identifiant, self.generation, case.identifiant, classe, cause, sous_compte, (),
                             tuple(non_reconnus))
        self._issues_reponses.append(issue)
        return issue

    def traiter_reponse(self, texte, *, case, identifiant_reponse, identifiant_fiche):
        """Une réponse de proposeur : « fiches rendues » par programme dès qu'une fiche est reconnue (chacune classée,
        `identifiant_fiche(rang)` donnant son identifiant réencodé) ; sinon l'appel « réponse sans fiche »."""
        lecture = self.lire_reponse(texte)
        if not lecture.a_des_fiches:
            return self.classer_reponse_sans_fiche(texte, identifiant_reponse=identifiant_reponse, case=case,
                                                   non_reconnus=lecture.non_reconnus)
        case = self._verifier_case(case)
        ident_rep = self._identifiant(identifiant_reponse)
        issues = tuple(self.classer_fiche(f, identifiant=identifiant_fiche(f.rang), case=case) for f in lecture.fiches)
        issue = IssueReponse(ident_rep, self.generation, case.identifiant, FICHES_RENDUES, "par programme", None, issues,
                             lecture.non_reconnus)
        self._issues_reponses.append(issue)
        return issue

    # --- passeports ----------------------------------------------------------------------------------------------------

    def exiger_passeport(self, identifiant, contenu):
        """Pour la surcharge de `juger` (lot 6) : rend le passeport de ce portier pour cette fiche, ou lève l'arrêt A17.
        `contenu` est le contenu de la fiche (les douze champs), sans l'identifiant servi au juge."""
        p = self._passeports.get(identifiant) if type(identifiant) is str else None
        if p is None:
            raise ArretSansPasseportNA("aucun passeport du portier neuf pour cette fiche")
        if not isinstance(contenu, dict) or empreinte_texte_classe(contenu) != p.empreinte:
            raise ArretSansPasseportNA("le texte présenté n'est pas celui qui a été classé")
        return p

    # --- comptes et sceau ----------------------------------------------------------------------------------------------

    def comptes(self):
        """Les comptes de la ligne de la génération (lot 6) : classes de fiche, par case, par cause ; classes d'appel ;
        sous-comptes ; défauts de forme ; champ `case` différent ; appels au modèle ; passeports. Aucun contenu."""
        fiches = self._issues_fiches
        par_case = {}
        for f in fiches:
            d = par_case.setdefault(f.identifiant_case, {c: 0 for c in CLASSES_FICHE})
            d[f.classe] += 1
        reps = self._issues_reponses
        return {
            "fiches_rendues": len(fiches),
            "classes_fiche": {c: sum(1 for f in fiches if f.classe == c) for c in CLASSES_FICHE},
            "classes_fiche_par_case": par_case,
            "causes_fiche": dict(collections.Counter(f.cause for f in fiches)),
            "au_coffre_par_refus_du_portier": sum(1 for f in fiches if f.cause == CAUSE_REFUS_ECRIT_FICHE),
            "hors_contrat_de_longueur": sum(1 for f in fiches if ct.CAUSE_LONGUEUR in f.defauts_de_forme),
            "champ_en_plus": sum(1 for f in fiches if ct.CAUSE_CHAMP_EN_PLUS in f.defauts_de_forme),
            "champ_qui_n_est_pas_une_chaine": sum(1 for f in fiches if ct.CAUSE_TYPE in f.defauts_de_forme),
            "champ_case_different": sum(1 for f in fiches if f.case_differe),
            "classes_appel": {c: sum(1 for r in reps if r.classe_appel == c) for c in CLASSES_APPEL},
            "sous_comptes_reponse_illisible": {SOUS_COMPTE_PORTIER: sum(1 for r in reps if r.sous_compte == SOUS_COMPTE_PORTIER)},
            "causes_reponse": dict(collections.Counter(r.cause for r in reps if r.classe_appel != FICHES_RENDUES)),
            "morceaux_non_reconnus": sum(len(r.non_reconnus) for r in reps),
            "appels_au_modele": self.appels_au_modele,
            "passeports": len(self._passeports),
        }

    def issues_fiches(self):
        return tuple(self._issues_fiches)

    def sceller(self):
        """Scelle le journal du portier (fin de la génération) ; rend son empreinte."""
        return self.journal.sceller()
