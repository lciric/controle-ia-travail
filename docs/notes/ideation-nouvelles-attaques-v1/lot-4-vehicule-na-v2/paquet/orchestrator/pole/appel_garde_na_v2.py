"""Véhicule NA-1, lot 4 v2 — la surcharge d'`appel` (`appel_garde_na_v2`, mélange `AppelGardeNA`) : routage par rôle, part
de la clé et cumul compté **par tentative**, garde de motifs au point d'envoi, journal, égalité, refus avant le noyau,
« refus écrit », lecture des retours, `hors_course`, et **la règle de repli** de GO-2026-11-22-35 pour les clés Claude, sur
l'adaptateur direct (`adaptateur_claude_direct_na_v1`).

v2 (remplace `appel_garde_na_v1.py`, `d16d07bf…`, archivé sans modification). Lettre neuve : nœuds du véhicule v2
(`79b9d423…`), § 1 (A1 à A7), § 2 (N2), § 5 (R1 à R16) ; projet d'additif v2 (`6e9bb88e…`), A-6, § 5 (P1 à P17), § 10
(n° 31, n° 34) ; décisions de la mère portées par le mandat du lot 4 v2. La lettre de la v1 (V9 l. 77, 372, 383, 384, 387 ;
conception v5, § 2.3, § 2.13 ; errata 1 à 3 du lot 4 v1) reste tenue, sauf ce que le repli change.

**Ordre d'un appel**, exactement :

0. rôle déjà arrêté par une garde héritée : « refus écrit », sans coût (inchangé) ;
1. routage : le couple (rôle, adaptateur) de la table scellée, sinon n° 12, seconde clause ; puis les contrôles de forme
   (requête assemblée, case, génération : arrêt « requête journalisée ») ; **pour un rôle d'une clé Claude, le modèle
   demandé est celui du rôle** (configuration), sinon arrêt n° 31 avant l'envoi ;
2. à 6. **pour chaque tentative** d'une chaîne fermée (le modèle du rôle, puis le premier, puis le second modèle de repli ;
   une seule tentative hors des clés Claude) : rôle arrêté (pas 0, sans coût) ; n° 12 avec **le pire de la tentative**
   (rôle, modèle) ; garde de motifs et **ligne « envoi » neuve** (rang neuf) ; égalité, et **la même requête assemblée**
   (même empreinte) à chaque tentative, sinon « requête journalisée » (cause « reformulation ») ; `super().appel(…,
   modele=<tentative>)`, qui repasse la réservation du noyau (n° 6, n° 7 : une coupure arrête la chaîne, « non lancé ») ;
   le coût que compte le noyau va au cumul de la clé, et **le pire de la tentative si le coût est inconnu** (A3) ;
7. au retour d'une tentative, liste fermée (A6) :
   - réponse « ok » : n° 31 si le modèle servi est absent ou n'est pas le modèle demandé **de la tentative** ; sinon, au
     rang 1, « ok » ; au rang 2 ou 3, « refus par classifieur, servi par repli » (fiche attribuée au modèle servi) ;
   - raison d'arrêt « refusal » lue par l'adaptateur direct (`messages.stop_reason`) : **repli** vers la tentative
     suivante ; au troisième refus, l'arrêt n° 1 (portée « appel » par défaut, « course » sur réglage) ;
   - trace de repli du fournisseur ou du kit, refus du relais pour modèle : n° 31 ;
   - refus de classifieur d'une commande externe ou du protocole : n° 1, sans repli (lettre de la V9 l. 372) ;
   - erreur : crédit d'amont (402, `billing_error`) ou plafond du relais : n° 13, qui dit la clé, sans repli ; budget
     dépassé du relais de protocole : n° 13 ; toute autre erreur d'une clé Claude : « réponse illisible, cause non
     établie » (sous-compte « en repli » si la chaîne était ouverte) ; une réponse servie mais coupée ou hors liste est
     « servie » au sens du § 5 du projet d'additif ;
   - tout autre événement de refus : « réponse illisible, cause non établie », sous-compte « refus hors liste », jamais
     rejoué ni lu comme un n° 1 (remplace « tout autre refus » de la v1, l. 74).

**Chaque tentative** est consignée (`na_replis`) : rôle, génération, case, session, rang de la ligne « envoi », rang de la
tentative, modèle demandé, modèle servi, catégorie (ou « catégorie non lue »), coût compté (micro-dollars), coût inconnu,
issue, attribution, fichier de la réponse brute ; la clé n'y figure pas : elle ne va qu'au journal des arrêts
(`na_journal_arrets_cles["tentatives_de_repli"]`).

**Arrêts** : n° 1, 12, 13, 16 et « requête journalisée » comme en v1 ; A2 devient le **n° 31** (proposé, § 10 du projet
d'additif) ; un pire de (rôle, modèle) manquant refuse la construction (**n° 34**, proposé) ; l'adaptateur direct refuse
un réglage non admis (**n° 32**, proposé). **L'arrêt n° 27 n'est pas touché** : il vit au lot 6 (sonde), et ce module
n'en lit ni n'en lève aucun. **Rien n'est ajouté à l'enveloppe** : la chaîne remise au noyau est, à chaque tentative, le
décodage strict des octets gardés.

Bibliothèque standard, et les modules des lots 2 à 4 (`garde_motifs_na_v4`, `requete_na_v3`, `journal_na_v3`,
`routage_na_v1`, `adaptateur_claude_direct_na_v1`).
"""

import dataclasses
import re

from pole import adaptateur_claude_direct_na_v1 as ad
from pole import garde_motifs_na_v4 as gm
from pole import journal_na_v3 as jn
from pole import requete_na_v3 as rq
from pole import routage_na_v1 as rt
from pole.adaptateurs import modele_conforme

VERSION = "appel-garde-na-v2"
ARRET_REQUETE_JOURNALISEE = "requête journalisée"
ARRET_A2 = "A2"
NUMERO_ARRET_CLASSIFIEUR = 1
NUMERO_ARRET_CREDIT = 13
NUMERO_ARRET_MOTIF = gm.NUMERO_ARRET
NUMERO_ARRET_A2 = 31  # proposé (projet d'additif v2, § 10) ; la mère le confirme à l'assemblage
NUMERO_ARRET_PIRE = 34  # proposé (projet d'additif v2, § 10)
PORTEES_ARRET_1 = ("appel", "course")
PORTEE_ARRET_1_DEFAUT = "appel"  # proposition du concepteur (conception v5, § 9, point 6) ; D8 en attente de Lazar
CAUSES_REQUETE = ("journal", "égalité", "requête non assemblée", "case incohérente", "génération incohérente",
                  "reformulation")
CAUSE_EGALITE = "égalité refusée après la ligne « envoi »"
TYPE_CLE_CLAUDE = "claude_sdk"
TENTATIVES_MAX = 3
_RENVOI = re.compile(r" ; renvoi à la ligne « envoi » de rang ([1-9][0-9]*)$")
_GARDE = re.compile(r"^(A[0-9]+(?:/A[0-9]+)?)\b")
# A6 : le seul événement qui ouvre le repli (clé Claude, adaptateur direct).
EVENEMENTS_REPLI = (ad.EVENEMENT_REFUS_CLASSIFIEUR,)
# N° 31 : modèle changé, repli du fournisseur ou du kit, modèle refusé par un relais.
EVENEMENTS_MODELE = ("assistant.model", "result.model_usage", "system.model_fallback", "system.model_refusal_fallback",
                     "commande.modele_servi", "commande.modele_servi_absent", "commande.modele_demande_inconnu",
                     "resultat.modele_servi", ad.EVENEMENT_MODELE_NON_PERMIS, ad.EVENEMENT_REPLI_FOURNISSEUR)
# N° 1 sans repli : refus de classifieur d'une commande externe ou du protocole (et du kit, s'il servait encore).
EVENEMENTS_CLASSIFIEUR_SANS_REPLI = ("commande.refus", "kimi.content_filter", "assistant.stop_reason",
                                     "result.stop_reason", "system.model_refusal_no_fallback")
ERREURS_CREDIT = (ad.ERREUR_CREDIT_AMONT, ad.ERREUR_PLAFOND_RELAIS)
# Issues rendues au lot 6 (`issue_na`).
ISSUE_OK = "ok"
ISSUE_SERVI_PAR_REPLI = "refus par classifieur, servi par repli"
ISSUE_ARRET_1 = "arrêt n° 1, consigné, non relancé"  # commande externe, protocole : sans repli (inchangée)
ISSUE_ARRET_1_APRES_REPLI = "arrêt n° 1, consigné après trois refus"
ISSUE_ILLISIBLE = "réponse illisible, cause non établie"
ISSUE_ERREUR = "erreur"
ISSUE_REFUS_ECRIT = "refus écrit"
ATTRIBUTION_ESPECE = "espèce"
PREFIXE_ATTRIBUTION_REPLI = "servie par repli : "


class ContexteRefuse(ValueError):
    """Le contexte que la génération donne au mélange ne tient pas sa forme : aucune génération ne se construit."""


class PireManquantNA(ContexteRefuse):
    """N° 34 (proposé) : un (rôle, modèle) sans pire écrit ; le départ est refusé."""

    numero = NUMERO_ARRET_PIRE


class ArretNA(RuntimeError):
    """Un arrêt nommé de la course, levé par la surcharge d'`appel` ; le message ne recopie aucun contenu."""

    numero = None
    nom = None


class ArretMotifNA(ArretNA):
    """Arrêt n° 16 au point d'envoi : la famille et le rang, jamais le texte trouvé (qui est à la ligne « non envoyé »)."""

    numero = NUMERO_ARRET_MOTIF
    nom = "motif interdit dans un texte à servir"

    def __init__(self, famille, rang, role):
        super().__init__(f"arrêt n° {NUMERO_ARRET_MOTIF}, motif interdit dans un texte à servir : famille « {famille} », "
                         f"rang {rang} ; rôle « {role} » ; envoi refusé, rien ne part")
        self.famille, self.rang, self.role = famille, rang, role


class ArretRequeteJournaliseeNA(ArretNA):
    """Arrêt nommé « requête journalisée » (V9, l. 77), numéroté à l'additif : rien ne part ; la course s'arrête."""

    nom = ARRET_REQUETE_JOURNALISEE

    def __init__(self, cause, role):
        if cause not in CAUSES_REQUETE:
            raise ValueError("cause inconnue")
        super().__init__(f"arrêt « {ARRET_REQUETE_JOURNALISEE} » ({cause}) : rôle « {role} » ; rien ne part, sans coût")
        self.cause, self.role = cause, role


class ArretClassifieurNA(ArretNA):
    """Arrêt n° 1 porté par la course (D8, si la configuration le dit)."""

    numero = NUMERO_ARRET_CLASSIFIEUR
    nom = "refus d'un classifieur de sûreté"

    def __init__(self, role, evenement):
        super().__init__(f"arrêt n° {NUMERO_ARRET_CLASSIFIEUR}, refus d'un classifieur de sûreté : rôle « {role} » ; "
                         "consigné tel quel")
        self.role, self.evenement = role, evenement


class ArretCreditNA(ArretNA):
    """Arrêt n° 13 : refus pour crédit ; arrêt nommé de la course, qui dit la clé ; aucune bascule, aucun repli."""

    numero = NUMERO_ARRET_CREDIT
    nom = "refus pour crédit"

    def __init__(self, cle, role, lu_par):
        super().__init__(f"arrêt n° {NUMERO_ARRET_CREDIT}, refus pour crédit : clé « {cle} » ({lu_par}) ; rôle « {role} » ; "
                         "aucune bascule")
        self.cle, self.role, self.lu_par = cle, role, lu_par


class ArretA2NA(ArretNA):
    """N° 31 (proposé ; A2 de la v1) : modèle servi absent ou différent du modèle demandé de la tentative ; trace de repli du
    fournisseur ou du kit ; arrêt nommé de la course, qui dit le rôle et la cause."""

    numero = NUMERO_ARRET_A2
    nom = ARRET_A2

    def __init__(self, role, cause):
        super().__init__(f"arrêt n° {NUMERO_ARRET_A2} (A2) : rôle « {role} » ; {cause} ; la composition gelée n'est plus "
                         "tenue")
        self.role, self.cause = role, cause


# --- le contexte -------------------------------------------------------------------------------------------------------

def _roles_claude(table):
    return sorted(r for r, e in table.roles.items() if e.cle != rt.CLE_HORS_COURSE
                  and table.cles[e.cle].type == TYPE_CLE_CLAUDE)


@dataclasses.dataclass(frozen=True)
class ContexteAppelGardeNA:
    """Ce que le mélange attend de la classe de génération (interface v2 avec le lot 6).

    En plus de la v1 : `modeles_par_role` ({rôle d'une clé Claude : modèle}), `modeles_repli` (les deux modèles de repli
    de GO-35, dans leur ordre, lus de la configuration), `pires_repli` ({rôle d'une clé Claude : {modèle de repli : USD au
    micro-dollar}}). `pires_par_role` reste le pire du modèle du rôle. `lire_etat_relais` (v1) est retiré : l'adaptateur
    direct rend l'erreur d'amont et celle du relais telles quelles (N2)."""

    numero_generation: object
    table: rt.TableRolesCles
    parts: dict
    pires_par_role: dict
    journal: jn.JournalRequetes
    garde: gm.GardeMotifs
    identifiant_case_de_session: object
    cumul: rt.CumulParCle
    modeles_par_role: dict
    modeles_repli: tuple
    pires_repli: dict
    portee_arret_1: str = PORTEE_ARRET_1_DEFAUT
    parts_micro: dict = dataclasses.field(init=False, repr=False)
    pires_micro: dict = dataclasses.field(init=False, repr=False)
    pires_tentative_micro: dict = dataclasses.field(init=False, repr=False)

    def __post_init__(self):
        if not isinstance(self.table, rt.TableRolesCles) or self.table.marque == rt.MARQUE_ARTEFACT:
            raise ContexteRefuse("table : une table de course ou de ligne à part lue par `routage_na_v1`")
        if self.table.marque == rt.MARQUE_COURSE:
            if type(self.numero_generation) is not int or self.numero_generation not in (1, 2, 3):
                raise ContexteRefuse("numéro de la génération : 1, 2 ou 3")
        elif self.numero_generation is not None:
            raise ContexteRefuse("une ligne à part n'a pas de numéro de génération")
        if not isinstance(self.journal, jn.JournalRequetes):
            raise ContexteRefuse("journal : un journal du lot 3")
        if not isinstance(self.garde, gm.GardeMotifs):
            raise ContexteRefuse("garde : la garde de motifs du lot 2")
        if not callable(self.identifiant_case_de_session):
            raise ContexteRefuse("identifiant_case_de_session : une fonction de la session")
        if not isinstance(self.cumul, rt.CumulParCle) or self.cumul.table_sha256 != self.table.sha256:
            raise ContexteRefuse("cumul : celui de cette table")
        if self.portee_arret_1 not in PORTEES_ARRET_1:
            raise ContexteRefuse("portée de l'arrêt n° 1 : « appel » ou « course »")
        try:
            object.__setattr__(self, "parts_micro", rt.lire_parts(self.table, self.parts))
            object.__setattr__(self, "pires_micro", rt.lire_pires(self.table, self.pires_par_role))
        except rt.TableRefusee as e:
            raise ContexteRefuse(str(e)) from None
        self._lire_repli()

    def _lire_repli(self):
        claude = _roles_claude(self.table)
        mr = self.modeles_repli
        if type(mr) is not tuple or len(mr) != TENTATIVES_MAX - 1 or len(set(mr)) != len(mr) \
                or any(type(m) is not str or not m for m in mr):
            raise ContexteRefuse("modèles de repli : deux noms distincts, dans l'ordre de GO-35 (premier, second)")
        if not isinstance(self.modeles_par_role, dict) or sorted(self.modeles_par_role) != claude \
                or any(type(m) is not str or not m for m in self.modeles_par_role.values()):
            raise ContexteRefuse("modèles par rôle : exactement un par rôle d'une clé Claude")
        if any(m in mr for m in self.modeles_par_role.values()):
            raise ContexteRefuse("un modèle de rôle ne peut pas être un modèle de repli")
        if not isinstance(self.pires_repli, dict) or sorted(self.pires_repli) != claude:
            raise PireManquantNA(f"arrêt n° {NUMERO_ARRET_PIRE} (proposé) : un pire de repli pour chaque rôle d'une clé "
                                 "Claude ; départ refusé")
        micro = {}
        for role in claude:
            p = self.pires_repli[role]
            if not isinstance(p, dict) or sorted(p) != sorted(mr):
                raise PireManquantNA(f"arrêt n° {NUMERO_ARRET_PIRE} (proposé) : le rôle « {role} » n'a pas un pire pour "
                                     "chaque modèle de repli ; départ refusé")
            for m in mr:
                try:
                    v = rt.micro_exact(p[m])
                except rt.MontantRefuse:
                    raise PireManquantNA(f"arrêt n° {NUMERO_ARRET_PIRE} (proposé) : pire de repli de « {role} » sans "
                                         "sa forme (micro-dollar) ; départ refusé") from None
                if v <= 0:
                    raise PireManquantNA(f"arrêt n° {NUMERO_ARRET_PIRE} (proposé) : pire de repli de « {role} » "
                                         "strictement positif ; départ refusé")
                micro[(role, m)] = v
            micro[(role, self.modeles_par_role[role])] = self.pires_micro[role]
        object.__setattr__(self, "pires_tentative_micro", micro)

    def chaine(self, role, modele):
        """La suite fermée des modèles d'un appel : le modèle du rôle puis les deux modèles de repli (clé Claude) ; le seul
        modèle demandé ailleurs."""
        if role in self.modeles_par_role:
            return (modele,) + self.modeles_repli
        return (modele,)

    def pire(self, role, modele):
        if role in self.modeles_par_role:
            return self.pires_tentative_micro[(role, modele)]
        return self.pires_micro[role]


def _plus(d, k, n=1):
    d[k] = d.get(k, 0) + n


# --- le mélange --------------------------------------------------------------------------------------------------------

class AppelGardeNA:
    """Mélange à placer devant la classe de génération : `class GenerationNA(AppelGardeNA, GenerationV68)`. Le contexte est
    passé en argument nommé `contexte_na`, ou posé sur l'instance (`_contexte_na_demande`) avant `__init__`."""

    def __init__(self, *a, **kw):
        contexte = kw.pop("contexte_na", None)
        if contexte is None:
            contexte = getattr(self, "_contexte_na_demande", None)
        if not isinstance(contexte, ContexteAppelGardeNA):
            raise ContexteRefuse("la génération du véhicule exige son contexte d'appel (`ContexteAppelGardeNA`)")
        self.na = contexte
        self.na_comptes = {"non_envoyes": {}, "refus_ecrits": {}, "non_lances": {}, "arrets_consignes": {},
                           "cause_non_etablie": {}, "replis": {}}
        self.na_arrets_consignes = []
        self.na_journal_arrets_cles = {"cause_non_etablie": {}, "tentatives_de_repli": {}}
        self.na_servis = {}
        self.na_replis = []
        super().__init__(*a, **kw)
        self._verifier_adaptateurs_directs_na()

    def _verifier_adaptateurs_directs_na(self):
        """D-N1 : chaque adaptateur d'une clé Claude est l'adaptateur direct, et sa liste fermée admet le modèle de chaque
        rôle qu'il sert et les deux modèles de repli ; sinon aucune génération ne se construit."""
        adaptateurs = getattr(self, "ad", None)
        if not isinstance(adaptateurs, dict):
            raise ContexteRefuse("la génération ne porte pas ses adaptateurs (`ad`)")
        t = self.na.table
        for nom, c in t.cles.items():
            if c.type != TYPE_CLE_CLAUDE:
                continue
            for nom_ad in c.adaptateurs:
                a = adaptateurs.get(nom_ad)
                if not isinstance(a, ad.AdaptateurClaudeDirectNA):
                    raise ContexteRefuse(f"clé Claude « {nom} » : l'adaptateur « {nom_ad} » doit être l'adaptateur direct "
                                         "(D-N1)")
                exiges = {self.na.modeles_par_role[r] for r, e in t.roles.items()
                          if e.adaptateur == nom_ad and r in self.na.modeles_par_role} | set(self.na.modeles_repli)
                if not exiges <= set(a.modeles_admis):
                    raise ContexteRefuse(f"adaptateur « {nom_ad} » : sa liste fermée n'admet pas tous les modèles de ses "
                                         "rôles et de repli")

    # --- crochets, surchargeables par le lot 6 et par les essais ----------------------------------------------------

    def role_arrete_na(self, role):
        """La cause, si le suivi des rôles dit le rôle arrêté ; sinon None."""
        suivi = getattr(self, "suivi", None)
        r = suivi.roles.get(role) if suivi is not None else None
        return r.get("arrete") if r else None

    def _chaine_pour_noyau_na(self, envoi):
        """La chaîne que reçoit le noyau : le décodage strict des octets gardés (un seul encodage, au lot 3)."""
        return rq.chaine_pour_le_noyau(envoi.octets)

    def _requete_de_tentative_na(self, consigne, rang_tentative):
        """La requête d'une tentative : la requête assemblée même, à chaque rang (P1 : aucune reformulation)."""
        return consigne

    # --- refus avant le noyau ----------------------------------------------------------------------------------------

    def _case_de_session_na(self, session):
        try:
            case = self.na.identifiant_case_de_session(session)
        except Exception:  # noqa: BLE001 — la ligne de refus s'écrit quand même, la case dite illisible
            return "", " ; case de la session illisible"
        return (case, "") if type(case) is str else ("", " ; case de la session illisible")

    def _non_envoye_na(self, arret, role, cle, case, generation, **details):
        """Une ligne « non envoyé » et un compte ; un journal en panne arrête la course (« requête journalisée »)."""
        _plus(self.na_comptes["non_envoyes"].setdefault(role, {}), str(arret))
        try:
            self.na.journal.journaliser_non_envoye(arret=arret, role=role, generation=generation, case=case, cle=cle,
                                                   **details)
        except (jn.JournalRefuse, OSError):
            panne = True
        else:
            panne = False
        if panne:
            _plus(self.na_comptes["non_envoyes"][role], ARRET_REQUETE_JOURNALISEE)
            raise ArretRequeteJournaliseeNA("journal", role)

    def _refuser_requete_na(self, cause, role, cle, case, generation):
        self._non_envoye_na(ARRET_REQUETE_JOURNALISEE, role, cle, case, generation, cause=cause)
        raise ArretRequeteJournaliseeNA(cause, role)

    def _refus_ecrit_na(self, role, fournisseur, consigne, session, cause):
        """Pas 0 : une ligne « refus écrit » ; rend ce que le § 2.13 fixe pour la sorte du rôle ; aucun coût."""
        entree = self.na.table.entree(role)
        cle = entree.cle if entree is not None else "rôle hors table"
        if not isinstance(consigne, rq.RequeteAssemblee) or consigne.sorte not in jn.RENDUS_REFUS_ECRIT:
            case, suffixe = self._case_de_session_na(session)
            self._refuser_requete_na("requête non assemblée", role, cle, case, self.na.numero_generation)
        m = _GARDE.match(cause) if isinstance(cause, str) else None
        garde = m.group(1) if m else "garde héritée"
        try:
            rendu = self.na.journal.journaliser_refus_ecrit(sorte=consigne.sorte, role=role, generation=consigne.generation,
                                                            case=consigne.identifiant_case, garde=garde,
                                                            cause=str(cause)[:300])
        except (jn.JournalRefuse, OSError):
            panne = True
        else:
            panne = False
        if panne:
            _plus(self.na_comptes["non_envoyes"].setdefault(role, {}), ARRET_REQUETE_JOURNALISEE)
            raise ArretRequeteJournaliseeNA("journal", role)
        _plus(self.na_comptes["refus_ecrits"].setdefault(role, {}), garde)
        return {"r": None, "lu": None, "motif": f"refus écrit ({garde})", "duree": 0.0, "refus_ecrit": rendu,
                "issue_na": ISSUE_REFUS_ECRIT, "par_repli": False, "tentatives": []}

    # --- consignation des tentatives ---------------------------------------------------------------------------------

    def _consigner_tentative_na(self, tentatives, *, role, cle, consigne, session, rang_tentative, modele, envoi=None,
                                r=None, cout_micro=0, inconnu=False, issue, attribution=None):
        t = getattr(r, "tentative", None) if r is not None else None
        t = t if isinstance(t, dict) else {}
        ligne = {"role": role, "generation": consigne.generation, "case": consigne.identifiant_case,
                 "session": "/".join(map(str, session)) if isinstance(session, (tuple, list)) else str(session),
                 "rang_envoi": envoi.rang if envoi is not None else None, "rang_tentative": rang_tentative,
                 "modele_demande": modele, "modele_servi": getattr(r, "modele_servi", None) if r is not None else None,
                 "categorie": t.get("categorie"), "classe_erreur": t.get("classe_erreur"),
                 "cout_micro": cout_micro, "cout_inconnu": bool(inconnu), "issue": issue,
                 "attribution": attribution, "reponse_brute": t.get("reponse_brute")}
        tentatives.append(ligne)
        self.na_replis.append(ligne)
        if rang_tentative > 1:
            _plus(self.na_journal_arrets_cles["tentatives_de_repli"], cle)
        return ligne

    def _compte_repli_na(self, role, quoi):
        _plus(self.na_comptes["replis"].setdefault(role, {}), quoi)

    # --- l'appel -----------------------------------------------------------------------------------------------------

    def appel(self, etat, *, role, role_kit, fournisseur, modele, consigne, plafond_role, session, lire=None):
        na = self.na
        # pas 0 : rôle déjà arrêté par une garde héritée
        cause_arret = self.role_arrete_na(role)
        if cause_arret:
            return self._refus_ecrit_na(role, fournisseur, consigne, session, cause_arret)
        # pas 1 : routage par rôle, puis contrôles de forme, puis modèle du rôle (clé Claude)
        try:
            entree = na.table.router(role, fournisseur)
        except rt.ArretPartCle as arret:
            case, suffixe = self._case_de_session_na(session)
            self._non_envoye_na(rt.NUMERO_ARRET_PART, role, arret.cle, case, na.numero_generation,
                                clause=arret.clause, cause=arret.motif + suffixe)
            raise
        cle = entree.cle
        if not isinstance(consigne, rq.RequeteAssemblee):
            case, _ = self._case_de_session_na(session)
            self._refuser_requete_na("requête non assemblée", role, cle, case, na.numero_generation)
        case_session, _ = self._case_de_session_na(session)
        if case_session != consigne.identifiant_case:
            self._refuser_requete_na("case incohérente", role, cle, consigne.identifiant_case, na.numero_generation)
        if consigne.generation is not None and consigne.generation != na.numero_generation:
            self._refuser_requete_na("génération incohérente", role, cle, consigne.identifiant_case, na.numero_generation)
        if role in na.modeles_par_role and modele != na.modeles_par_role[role]:
            self._non_envoye_na(NUMERO_ARRET_A2, role, cle, consigne.identifiant_case, na.numero_generation,
                                cause="modèle demandé autre que celui du rôle", sorte=consigne.sorte)
            raise ArretA2NA(role, "modèle demandé autre que celui du rôle")
        chaine = na.chaine(role, modele)
        tentatives = []
        for i, m in enumerate(chaine, start=1):
            if i > 1:
                cause_arret = self.role_arrete_na(role)
                if cause_arret:
                    rendu = self._refus_ecrit_na(role, fournisseur, consigne, session, cause_arret)
                    self._consigner_tentative_na(tentatives, role=role, cle=cle, consigne=consigne, session=session,
                                                 rang_tentative=i, modele=m, issue="refus écrit en chaîne")
                    self._compte_repli_na(role, "arrêtées par une garde héritée")
                    return dict(rendu, tentatives=list(tentatives))
            requete = self._requete_de_tentative_na(consigne, i)
            if not isinstance(requete, rq.RequeteAssemblee) or requete.sha256 != consigne.sha256 \
                    or requete.taille != consigne.taille or requete.octets != consigne.octets:
                self._consigner_tentative_na(tentatives, role=role, cle=cle, consigne=consigne, session=session,
                                             rang_tentative=i, modele=m, issue="reformulation refusée")
                self._refuser_requete_na("reformulation", role, cle, consigne.identifiant_case, na.numero_generation)
            rendu = self._tentative_na(etat, role=role, role_kit=role_kit, fournisseur=fournisseur, modele=m,
                                       consigne=requete, plafond_role=plafond_role, session=session, lire=lire, cle=cle,
                                       entree=entree, rang_tentative=i, dernier=i == len(chaine), tentatives=tentatives)
            if rendu is not _REPLI:
                return rendu
        raise AssertionError("la chaîne se termine toujours par une issue")  # pragma: no cover

    def _tentative_na(self, etat, *, role, role_kit, fournisseur, modele, consigne, plafond_role, session, lire, cle,
                      entree, rang_tentative, dernier, tentatives):
        na = self.na
        consigner = dict(tentatives=tentatives, role=role, cle=cle, consigne=consigne, session=session,
                         rang_tentative=rang_tentative, modele=modele)
        # pas 2 : part de la clé, au pire de la tentative
        pire = na.pire(role, modele)
        try:
            compte = rt.verifier_part(na.table, na.parts_micro, na.cumul, cle, role, pire)
        except rt.ArretPartCle as arret:
            self._consigner_tentative_na(**consigner, issue="arrêt n° 12")
            self._non_envoye_na(rt.NUMERO_ARRET_PART, role, cle, consigne.identifiant_case, na.numero_generation,
                                clause=arret.clause, sorte=consigne.sorte, sha256=consigne.sha256, taille=consigne.taille)
            raise
        # pas 3 et 4 : garde de motifs, puis ligne « envoi » neuve
        envoi, motif, panne = None, None, False
        try:
            envoi = na.journal.journaliser_envoi(consigne, na.garde, role=role, cle=cle)
        except gm.ArretMotifInterdit as arret:
            motif = (arret.famille, arret.rang)
        except (jn.JournalRefuse, OSError):
            panne = True
        if motif is not None:
            _plus(self.na_comptes["non_envoyes"].setdefault(role, {}), str(NUMERO_ARRET_MOTIF))
            self._consigner_tentative_na(**consigner, issue="arrêt n° 16")
            raise ArretMotifNA(motif[0], motif[1], role)
        if panne:
            _plus(self.na_comptes["non_envoyes"].setdefault(role, {}), ARRET_REQUETE_JOURNALISEE)
            raise ArretRequeteJournaliseeNA("journal", role)
        # pas 5 : égalité, sur les octets mêmes de la chaîne remise au noyau
        try:
            chaine = self._chaine_pour_noyau_na(envoi)
            octets_remis = chaine.encode("utf-8")
            gm.verifier_avant_envoi(envoi.requete_gardee, octets_remis)
        except (gm.EcartApresGarde, rq.RequeteRefusee, UnicodeError, AttributeError):
            self._non_envoye_na(ARRET_REQUETE_JOURNALISEE, role, cle, consigne.identifiant_case, consigne.generation,
                                cause=f"{CAUSE_EGALITE} ; renvoi à la ligne « envoi » de rang {envoi.rang}",
                                sorte=consigne.sorte, sha256=envoi.requete_gardee.sha256, taille=envoi.requete_gardee.taille)
            raise ArretRequeteJournaliseeNA("égalité", role) from None
        # pas 6 : le noyau, inchangé ; le coût qu'il compte va au cumul de la clé ; inconnu : le pire de la tentative (A3)
        cout_avant = float(etat["cout"])
        jeton = na.cumul.ouvrir_vol(compte, pire)
        a, fini, compte_micro, inconnu = None, False, 0, True
        try:
            a = super().appel(etat, role=role, role_kit=role_kit, fournisseur=fournisseur, modele=modele, consigne=chaine,
                              plafond_role=plafond_role, session=session, lire=lire)
            fini = True
        finally:
            na.cumul.fermer_vol(jeton)
            delta = rt.micro_cout(max(0.0, float(etat["cout"]) - cout_avant))
            r = a.get("r") if isinstance(a, dict) else None
            inconnu = (not fini) or bool(getattr(r, "cout_inconnu", False))
            compte_micro = max(delta, pire) if inconnu else delta
            na.cumul.ajouter(compte, compte_micro)
        consigner.update(envoi=envoi, cout_micro=compte_micro, inconnu=inconnu)
        # pas 7 : au retour
        if a is None:
            cause = jn.CAUSE_NON_LANCE if etat.get("coupee") else "rôle arrêté par une garde héritée, vu par le noyau"
            try:
                na.journal.journaliser_non_lance(envoi, cause)
            except (jn.JournalRefuse, OSError):
                raise ArretRequeteJournaliseeNA("journal", role) from None
            _plus(self.na_comptes["non_lances"], role)
            self._consigner_tentative_na(**consigner, issue="non lancé")
            if rang_tentative > 1:
                self._compte_repli_na(role, "arrêtées en repli : non lancé")
            return None
        return self._apres_retour_na(a, role, cle, entree, rang_tentative, dernier, consigner)

    def _apres_retour_na(self, a, role, cle, entree, rang_tentative, dernier, consigner):
        r = a["r"]
        statut = getattr(r, "statut", None)
        servi = getattr(r, "modele_servi", None)
        demande = consigner["modele"]
        tentatives = consigner["tentatives"]
        type_cle = self.na.table.cles[cle].type
        direct = isinstance(getattr(r, "tentative", None), dict)
        servie = direct and bool(r.tentative.get("servie"))

        def fin(issue, **plus):
            return dict(a, issue_na=issue, tentatives=list(tentatives), **plus)

        # n° 31 sur toute réponse servie : le modèle servi est celui demandé à la tentative
        if statut == "ok" or servie:
            if not servi:
                self._consigner_tentative_na(**consigner, r=r, issue=f"arrêt n° {NUMERO_ARRET_A2}")
                raise ArretA2NA(role, "modèle servi absent pour une réponse servie")
            if not modele_conforme(demande, servi):
                self._consigner_tentative_na(**consigner, r=r, issue=f"arrêt n° {NUMERO_ARRET_A2}")
                raise ArretA2NA(role, "modèle servi différent du modèle demandé de la tentative")
            vu = self.na_servis.setdefault((role, demande), servi)
            if vu != servi:
                self._consigner_tentative_na(**consigner, r=r, issue=f"arrêt n° {NUMERO_ARRET_A2}")
                raise ArretA2NA(role, "modèle servi changé entre deux appels du rôle, au même modèle demandé")
            if rang_tentative > 1:
                attribution = PREFIXE_ATTRIBUTION_REPLI + servi
                classe = "ok" if statut == "ok" else "réponse illisible"
                self._consigner_tentative_na(**consigner, r=r, issue=ISSUE_SERVI_PAR_REPLI, attribution=attribution)
                self._compte_repli_na(role, "servies par repli")
                return fin(ISSUE_SERVI_PAR_REPLI, par_repli=True, modele_servi_repli=servi, attribution=attribution,
                           classe_tentative_servie=classe)
            if statut == "ok":
                self._consigner_tentative_na(**consigner, r=r, issue=ISSUE_OK, attribution=ATTRIBUTION_ESPECE)
                return fin(ISSUE_OK, par_repli=False, attribution=ATTRIBUTION_ESPECE)
        refus = getattr(r, "refus", None)
        ev = refus.get("evenement") if isinstance(refus, dict) else None
        if statut == "refus":
            if ev in EVENEMENTS_MODELE:
                self._consigner_tentative_na(**consigner, r=r, issue=f"arrêt n° {NUMERO_ARRET_A2}")
                raise ArretA2NA(role, "modèle servi changé, repli du fournisseur ou modèle refusé par le relais")
            if ev in EVENEMENTS_REPLI and type_cle == TYPE_CLE_CLAUDE and direct:
                self._consigner_tentative_na(**consigner, r=r, issue="refus de classifieur")
                if rang_tentative == 1:
                    self._compte_repli_na(role, "chaînes ouvertes")
                if not dernier:
                    return _REPLI
                self._compte_repli_na(role, "trois refus")
                return self._arret_1_na(a, role, ev, fin, ISSUE_ARRET_1_APRES_REPLI, tentatives)
            if ev in EVENEMENTS_CLASSIFIEUR_SANS_REPLI and not (type_cle == TYPE_CLE_CLAUDE and direct):
                self._consigner_tentative_na(**consigner, r=r, issue=ISSUE_ARRET_1)
                return self._arret_1_na(a, role, ev, fin, ISSUE_ARRET_1, tentatives)
            # A6 : tout autre événement de refus est une réponse illisible, jamais rejouée
            self._consigner_tentative_na(**consigner, r=r, issue=ISSUE_ILLISIBLE)
            _plus(self.na_comptes["cause_non_etablie"].setdefault(role, {}), "refus hors liste")
            _plus(self.na_journal_arrets_cles["cause_non_etablie"], cle)
            return fin(ISSUE_ILLISIBLE, par_repli=False, en_repli=rang_tentative > 1)
        if type_cle == "kimi_protocole" and statut == "budget_depasse":
            self._consigner_tentative_na(**consigner, r=r, issue=f"arrêt n° {NUMERO_ARRET_CREDIT}")
            raise ArretCreditNA(cle, role, "statut du relais de protocole")
        if type_cle == TYPE_CLE_CLAUDE:
            classe = r.tentative.get("classe_erreur") if direct else None
            if classe in ERREURS_CREDIT:
                self._consigner_tentative_na(**consigner, r=r, issue=f"arrêt n° {NUMERO_ARRET_CREDIT}")
                if rang_tentative > 1:
                    self._compte_repli_na(role, "arrêtées en repli : crédit")
                raise ArretCreditNA(cle, role, classe)
            self._consigner_tentative_na(**consigner, r=r, issue=ISSUE_ILLISIBLE)
            sous = "en repli" if rang_tentative > 1 else (classe or "erreur hors adaptateur direct")
            _plus(self.na_comptes["cause_non_etablie"].setdefault(role, {}), sous)
            _plus(self.na_journal_arrets_cles["cause_non_etablie"], cle)
            if rang_tentative > 1:
                self._compte_repli_na(role, "arrêtées en repli : cause non établie")
            return fin(ISSUE_ILLISIBLE, par_repli=False, en_repli=rang_tentative > 1)
        self._consigner_tentative_na(**consigner, r=r, issue=ISSUE_ERREUR)
        return fin(ISSUE_ERREUR, par_repli=False)

    def _arret_1_na(self, a, role, ev, fin, issue, tentatives):
        _plus(self.na_comptes["arrets_consignes"].setdefault(role, {}), str(NUMERO_ARRET_CLASSIFIEUR))
        self.na_arrets_consignes.append({"arret": NUMERO_ARRET_CLASSIFIEUR, "role": role,
                                         "evenement": ev if isinstance(ev, str) else None,
                                         "tentatives": len(tentatives),
                                         "categories": [t["categorie"] for t in tentatives]})
        if self.na.portee_arret_1 == "course":
            raise ArretClassifieurNA(role, ev)
        return fin(issue, par_repli=False)


_REPLI = object()


# --- comptes, pour la ligne de la génération (lot 6) -------------------------------------------------------------------

def comptes_envois_na(lignes):
    """Comptes d'un journal relu (`journal_na_v3.verifier_journal`) : une ligne « envoi » suivie d'une ligne « non lancé »
    ou d'une ligne « non envoyé » qui la renvoie par son rang (écart d'égalité) n'est pas comptée comme partie ; aucune
    requête n'est comptée deux fois. Chaque tentative d'une chaîne de repli est un envoi. Rend {"partis",
    "journalises_non_lances", "journalises_puis_refuses", "non_envoyes", "refus_ecrits"} par rôle."""
    envois = {l["rang"]: l for l in lignes if l["evenement"] == "envoi"}
    retires = {}
    for l in lignes:
        if l["evenement"] == "non lancé":
            rang, quoi = l["envoi_rang"], "journalises_non_lances"
        elif l["evenement"] == "non envoyé" and l.get("arret") == ARRET_REQUETE_JOURNALISEE \
                and isinstance(l.get("cause"), str) and _RENVOI.search(l["cause"]):
            rang, quoi = int(_RENVOI.search(l["cause"]).group(1)), "journalises_puis_refuses"
        else:
            continue
        if rang not in envois or rang in retires or rang >= l["rang"]:
            raise jn.JournalReecrit("un renvoi qui ne vise pas une ligne « envoi » antérieure, une seule fois")
        retires[rang] = quoi
    rendu = {"partis": {}, "journalises_non_lances": {}, "journalises_puis_refuses": {}}
    for rang, l in envois.items():
        _plus(rendu[retires.get(rang, "partis")], l["role"])
    base = jn.comptes(lignes)
    rendu["non_envoyes"] = base["non_envoyes"]
    rendu["refus_ecrits"] = base["refus_ecrits"]
    return rendu


def comptes_replis_na(tentatives):
    """La mesure descriptive « replis » (P10, point 3) d'une liste de tentatives (`na_replis`) : comptes et coûts par
    (rôle, modèle demandé, modèle servi, catégorie, issue). Rien n'en est rendu à la composition."""
    rendu = {}
    for t in tentatives:
        k = (t["role"], t["modele_demande"], t["modele_servi"] or "aucun", t["categorie"] or "sans objet", t["issue"])
        e = rendu.setdefault(k, {"tentatives": 0, "cout_micro": 0, "couts_inconnus": 0})
        e["tentatives"] += 1
        e["cout_micro"] += t["cout_micro"]
        e["couts_inconnus"] += int(t["cout_inconnu"])
    return [dict(zip(("role", "modele_demande", "modele_servi", "categorie", "issue"), k), **v)
            for k, v in sorted(rendu.items())]


__all__ = ("AppelGardeNA", "ContexteAppelGardeNA", "ContexteRefuse", "PireManquantNA", "ArretNA", "ArretMotifNA",
           "ArretRequeteJournaliseeNA", "ArretClassifieurNA", "ArretCreditNA", "ArretA2NA", "comptes_envois_na",
           "comptes_replis_na", "ARRET_REQUETE_JOURNALISEE", "PORTEE_ARRET_1_DEFAUT", "ISSUE_OK", "ISSUE_SERVI_PAR_REPLI",
           "ISSUE_ARRET_1", "ISSUE_ARRET_1_APRES_REPLI", "ISSUE_ILLISIBLE", "ISSUE_ERREUR", "ISSUE_REFUS_ECRIT",
           "NUMERO_ARRET_A2", "NUMERO_ARRET_PIRE")
