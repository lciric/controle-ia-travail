"""Véhicule NA-1, lot 4 — la surcharge d'`appel` (`appel_garde_na_v1`, mélange `AppelGardeNA`) : routage par rôle, part de la
clé et cumul compté, garde de motifs au point d'envoi, journal, égalité entre ce qui est journalisé et ce qui part, refus
avant le noyau (« non envoyé », sans coût), « refus écrit », lecture des statuts et de l'état du relais, `hors_course`.

Lettre : V9 (`864f39a7…`), l. 77 (journal avant chaque envoi ; un appel sans ligne ne part pas ; une requête changée après
la journalisation est refusée à l'envoi), l. 156, l. 372 (arrêt n° 1), l. 383 (arrêt n° 12), l. 384 (arrêt n° 13), l. 387
(arrêt n° 16) ; conception du véhicule v5 (`1b7f6822…`), § 2.3 (pas 0 à 7 ; refus avant le noyau ; statuts et arrêt
n° 13 sur les clés Claude ; interface avec le lot 6), § 2.13 (gardes héritées, refus écrits, A2), § 6.1 et § 6.2 ; relevé
du lot 0 (`10ac79ec…`), Q2, Q5, Q11, Q13 ; mandat du lot 4 et ses errata 1 à 3.

**Le lieu** : un mélange, placé devant la classe de génération (lot 6), qui surcharge `appel` et appelle `super().appel`
(le noyau, inchangé) seulement si tout est permis. **Ordre**, exactement :

0. rôle déjà arrêté par une garde héritée (le suivi le dit) : « refus écrit », sans coût ; rien n'est présenté au noyau ;
1. routage : le couple (rôle, nom d'adaptateur) de la table scellée ; sinon arrêt n° 12, seconde clause ;
   puis trois contrôles de forme : la consigne est une requête assemblée par le lot 3 ; sa case est celle que la session
   désigne ; sa génération est celle de la génération qui l'envoie ; sinon l'arrêt « requête journalisée » ;
2. part de la clé (cumul + pire en vol + pire de l'appel) ; sinon arrêt n° 12, première clause ;
3. et 4. garde de motifs puis ligne « envoi » (journal du lot 3, qui lit les octets de la requête une fois) ; un motif :
   ligne « non envoyé », puis l'arrêt n° 16, qui dit la famille et le rang, jamais le texte trouvé ; un journal en panne
   (`JournalRefuse` ou `OSError`) : rien ne part, arrêt « requête journalisée » ;
5. égalité : la chaîne remise au noyau est le décodage strict des octets gardés ; son encodage UTF-8 est comparé aux octets
   que la garde a lus (`verifier_avant_envoi`) ; un écart, après la ligne « envoi » : une ligne « non envoyé » qui renvoie
   à la ligne « envoi » par son rang, sans coût, puis l'arrêt « requête journalisée » ; la requête n'est jamais comptée à
   la fois comme envoyée et comme refusée (`comptes_envois_na`) ;
6. `super().appel`, inchangé ; le coût que le noyau compte (écart de `etat["cout"]`, plafond compris en cas d'exception) est
   ajouté au cumul de la clé ;
7. au retour : rien de rendu (coupure au plafond dur) : ligne « non lancé » ; statut, champ de refus et champ d'erreur lus :
   refus d'un classifieur : arrêt n° 1 (porté par l'appel par défaut, D8 en attente ; par la course si la configuration le
   dit) ; modèle servi absent ou changé : arrêt d'A2, nommé ; erreur sur une clé Claude (le message synthétique de l'outil
   compris, que le kit rend en refus `assistant.model`) : l'état du relais est lu par son adresse locale ; un refus pour
   crédit qu'il montre : arrêt n° 13, qui dit la clé ; sinon « réponse illisible », au sous-compte « cause non établie ».

**Un refus avant le noyau** (pas 0 à 5) ne passe jamais par `super().appel` : aucune consommation au coffre, aucun coût au
cumul de l'étape ni de la clé, aucun passage par le suivi des rôles ; une ligne au journal ; un compte (`na_comptes`).

**Arrêts nommés neufs, numérotés à l'additif** : « requête journalisée » (V9, l. 77 : journal en panne, écart d'égalité,
consigne qui n'est pas une requête assemblée, case ou génération incohérente) et A2 (07:46Z, mot 6). Le texte trouvé par
la garde ne va qu'à la ligne « non envoyé » : l'arrêt n° 16 levé ici est neuf, levé hors du bloc qui a reçu celui du lot 2,
et ne porte ni le texte, ni l'arrêt du lot 2 en contexte.

Bibliothèque standard, et les modules des lots 2 à 4 (`garde_motifs_na_v4`, `requete_na_v3`, `journal_na_v3`,
`routage_na_v1`).
"""

import dataclasses
import json
import re
import urllib.parse
import urllib.request

from pole import garde_motifs_na_v4 as gm
from pole import journal_na_v3 as jn
from pole import requete_na_v3 as rq
from pole import routage_na_v1 as rt
from pole.relais import valider_url_relais

VERSION = "appel-garde-na-v1"
ARRET_REQUETE_JOURNALISEE = "requête journalisée"
ARRET_A2 = "A2"
NUMERO_ARRET_CLASSIFIEUR = 1
NUMERO_ARRET_CREDIT = 13
NUMERO_ARRET_MOTIF = gm.NUMERO_ARRET
PORTEES_ARRET_1 = ("appel", "course")
PORTEE_ARRET_1_DEFAUT = "appel"  # proposition du concepteur (conception v5, § 9, point 6) ; D8 en attente de Lazar
CAUSES_REQUETE = ("journal", "égalité", "requête non assemblée", "case incohérente", "génération incohérente")
CAUSE_EGALITE = "égalité refusée après la ligne « envoi »"
_RENVOI = re.compile(r" ; renvoi à la ligne « envoi » de rang ([1-9][0-9]*)$")
_GARDE = re.compile(r"^(A[0-9]+(?:/A[0-9]+)?)\b")
# Événements de refus qui disent un changement ou une absence de modèle (A2), lus au champ `refus["evenement"]`.
EVENEMENTS_MODELE = ("assistant.model", "result.model_usage", "system.model_fallback", "commande.modele_servi",
                     "commande.modele_servi_absent", "commande.modele_demande_inconnu", "resultat.modele_servi",
                     "relais.modele_non_permis")
# Tout autre refus (statut « refus ») est le refus d'un classifieur de sûreté (arrêt n° 1), dont ceux-ci, nommés.
EVENEMENTS_CLASSIFIEUR = ("assistant.stop_reason", "result.stop_reason", "commande.refus", "kimi.content_filter",
                          "system.model_refusal_fallback", "system.model_refusal_no_fallback")
# Le message que l'outil fabrique lui-même pour une erreur (crédit, accès, réponse coupée : relevé au faux fournisseur)
# porte ce modèle ; l'adaptateur du kit le rend en « refus » `assistant.model`. Ce n'est pas un modèle servi : la surcharge
# le lit comme une erreur de la clé (état du relais, puis « cause non établie »), jamais comme A2.
MODELE_SYNTHETIQUE = "<synthetic>"
CHAMPS_ETAT_RELAIS = ("plafond_usd", "depense_usd", "engage_usd", "reserve_par_appel_usd", "refus", "refus_modele")
DELAI_ETAT_RELAIS_S = 10


class ContexteRefuse(ValueError):
    """Le contexte que la génération donne au mélange ne tient pas sa forme : aucune génération ne se construit."""


class EtatRelaisIllisible(ValueError):
    """L'état du relais n'a pas pu être lu ou n'a pas sa forme."""


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
                         "consigné tel quel, non relancé")
        self.role, self.evenement = role, evenement


class ArretCreditNA(ArretNA):
    """Arrêt n° 13 : refus pour crédit ; arrêt nommé de la course, qui dit la clé ; aucune bascule."""

    numero = NUMERO_ARRET_CREDIT
    nom = "refus pour crédit"

    def __init__(self, cle, role, lu_par):
        super().__init__(f"arrêt n° {NUMERO_ARRET_CREDIT}, refus pour crédit : clé « {cle} » ({lu_par}) ; rôle « {role} » ; "
                         "aucune bascule")
        self.cle, self.role, self.lu_par = cle, role, lu_par


class ArretA2NA(ArretNA):
    """A2 (07:46Z, mot 6) : modèle servi absent ou changé ; arrêt nommé de la course, qui dit le rôle et la cause."""

    nom = ARRET_A2

    def __init__(self, role, cause):
        super().__init__(f"arrêt d'A2 : rôle « {role} » ; {cause} ; la composition gelée n'est plus tenue")
        self.role, self.cause = role, cause


# --- l'état du relais (clés Claude) ------------------------------------------------------------------------------------

def relais_montre_refus_credit(etat):
    """Vrai si l'état du relais (`/relais/etat`, relais v2) montre un refus pour crédit : au moins un refus autre que de
    modèle, et plus de quoi réserver un appel (la règle même du relais : dépense + engagé + réserve > plafond)."""
    if not isinstance(etat, dict) or any(k not in etat for k in CHAMPS_ETAT_RELAIS):
        raise EtatRelaisIllisible("état du relais sans ses champs")
    try:
        v = {k: float(etat[k]) for k in CHAMPS_ETAT_RELAIS}
    except (TypeError, ValueError):
        raise EtatRelaisIllisible("état du relais aux champs non numériques") from None
    return v["refus"] - v["refus_modele"] > 0 and v["depense_usd"] + v["engage_usd"] + v["reserve_par_appel_usd"] \
        > v["plafond_usd"] + 1e-12


def lecteur_etat_relais_http(table, delai_s=DELAI_ETAT_RELAIS_S):
    """Un lecteur de l'état du relais d'une clé, par son adresse locale (`GET /relais/etat`), sans mandataire réseau."""
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))

    def lire(cle):
        adresse = table.cles[cle].relais
        valider_url_relais(adresse)
        url = urllib.parse.urljoin(adresse.rstrip("/") + "/", "relais/etat")
        try:
            with ouvreur.open(url, timeout=delai_s) as r:
                return json.loads(r.read().decode("utf-8"))
        except (OSError, ValueError) as e:
            raise EtatRelaisIllisible(f"relais de « {cle} » illisible ({type(e).__name__})") from None

    return lire


# --- le contexte -------------------------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class ContexteAppelGardeNA:
    """Ce que le mélange attend de la classe de génération (interface figée avec le lot 6)."""

    numero_generation: object
    table: rt.TableRolesCles
    parts: dict
    pires_par_role: dict
    journal: jn.JournalRequetes
    garde: gm.GardeMotifs
    identifiant_case_de_session: object
    cumul: rt.CumulParCle
    lire_etat_relais: object = None
    portee_arret_1: str = PORTEE_ARRET_1_DEFAUT
    parts_micro: dict = dataclasses.field(init=False, repr=False)
    pires_micro: dict = dataclasses.field(init=False, repr=False)

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
        if self.lire_etat_relais is None:
            object.__setattr__(self, "lire_etat_relais", lecteur_etat_relais_http(self.table))
        elif not callable(self.lire_etat_relais):
            raise ContexteRefuse("lire_etat_relais : une fonction de la clé")


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
                           "cause_non_etablie": {}, "etat_relais_illisible": {}}
        self.na_arrets_consignes = []
        self.na_journal_arrets_cles = {"cause_non_etablie": {}, "etat_relais_illisible": {}}
        self.na_servis = {}
        super().__init__(*a, **kw)

    # --- crochets, surchargeables par le lot 6 et par les essais ----------------------------------------------------

    def role_arrete_na(self, role):
        """La cause, si le suivi des rôles dit le rôle arrêté ; sinon None."""
        suivi = getattr(self, "suivi", None)
        r = suivi.roles.get(role) if suivi is not None else None
        return r.get("arrete") if r else None

    def _chaine_pour_noyau_na(self, envoi):
        """La chaîne que reçoit le noyau : le décodage strict des octets gardés (un seul encodage, au lot 3)."""
        return rq.chaine_pour_le_noyau(envoi.octets)

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
                "issue_na": "refus écrit"}

    # --- l'appel -----------------------------------------------------------------------------------------------------

    def appel(self, etat, *, role, role_kit, fournisseur, modele, consigne, plafond_role, session, lire=None):
        na = self.na
        # pas 0 : rôle déjà arrêté par une garde héritée
        cause_arret = self.role_arrete_na(role)
        if cause_arret:
            return self._refus_ecrit_na(role, fournisseur, consigne, session, cause_arret)
        # pas 1 : routage par rôle
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
        # pas 2 : part de la clé
        pire = na.pires_micro[role]
        try:
            compte = rt.verifier_part(na.table, na.parts_micro, na.cumul, cle, role, pire)
        except rt.ArretPartCle as arret:
            self._non_envoye_na(rt.NUMERO_ARRET_PART, role, cle, consigne.identifiant_case, na.numero_generation,
                                clause=arret.clause, sorte=consigne.sorte, sha256=consigne.sha256, taille=consigne.taille)
            raise
        # pas 3 et 4 : garde de motifs, puis ligne « envoi » (le journal du lot 3 écrit la ligne « non envoyé » d'un motif)
        envoi, motif, panne = None, None, False
        try:
            envoi = na.journal.journaliser_envoi(consigne, na.garde, role=role, cle=cle)
        except gm.ArretMotifInterdit as arret:
            motif = (arret.famille, arret.rang)
        except (jn.JournalRefuse, OSError):
            panne = True
        if motif is not None:
            _plus(self.na_comptes["non_envoyes"].setdefault(role, {}), str(NUMERO_ARRET_MOTIF))
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
        # pas 6 : le noyau, inchangé ; le coût qu'il compte va au cumul de la clé
        cout_avant = float(etat["cout"])
        jeton = na.cumul.ouvrir_vol(compte, pire)
        try:
            a = super().appel(etat, role=role, role_kit=role_kit, fournisseur=fournisseur, modele=modele, consigne=chaine,
                              plafond_role=plafond_role, session=session, lire=lire)
        finally:
            na.cumul.fermer_vol(jeton)
            na.cumul.ajouter(compte, rt.micro_cout(max(0.0, float(etat["cout"]) - cout_avant)))
        # pas 7 : au retour
        if a is None:
            cause = jn.CAUSE_NON_LANCE if etat.get("coupee") else "rôle arrêté par une garde héritée, vu par le noyau"
            try:
                na.journal.journaliser_non_lance(envoi, cause)
            except (jn.JournalRefuse, OSError):
                panne = True
            if panne:
                raise ArretRequeteJournaliseeNA("journal", role)
            _plus(self.na_comptes["non_lances"], role)
            return None
        return self._apres_retour_na(a, role, cle, entree)

    def _apres_retour_na(self, a, role, cle, entree):
        r = a["r"]
        statut = getattr(r, "statut", None)
        servi = getattr(r, "modele_servi", None)
        if statut == "ok":
            if not servi:
                raise ArretA2NA(role, "modèle servi absent pour une réponse « ok »")
            vu = self.na_servis.setdefault(role, servi)
            if vu != servi:
                raise ArretA2NA(role, "modèle servi changé entre deux appels du rôle")
            return dict(a, issue_na="ok")
        refus = getattr(r, "refus", None)
        ev = refus.get("evenement") if isinstance(refus, dict) else None
        synthetique = statut == "refus" and ev == "assistant.model" and refus.get("modele_servi") == MODELE_SYNTHETIQUE
        if statut == "refus" and not synthetique:
            if ev in EVENEMENTS_MODELE:
                raise ArretA2NA(role, "modèle servi changé ou refusé par le transport")
            _plus(self.na_comptes["arrets_consignes"].setdefault(role, {}), str(NUMERO_ARRET_CLASSIFIEUR))
            self.na_arrets_consignes.append({"arret": NUMERO_ARRET_CLASSIFIEUR, "role": role,
                                             "evenement": ev if isinstance(ev, str) else None})
            if self.na.portee_arret_1 == "course":
                raise ArretClassifieurNA(role, ev)
            return dict(a, issue_na="arrêt n° 1, consigné, non relancé")
        type_cle = self.na.table.cles[cle].type
        if type_cle == "kimi_protocole" and statut == "budget_depasse":
            raise ArretCreditNA(cle, role, "statut du relais de protocole")
        if type_cle == "claude_sdk":
            try:
                credit = relais_montre_refus_credit(self.na.lire_etat_relais(cle))
            except Exception:  # noqa: BLE001 — relais illisible : compté, jamais en silence ; la cause reste non établie
                _plus(self.na_comptes["etat_relais_illisible"], role)
                _plus(self.na_journal_arrets_cles["etat_relais_illisible"], cle)
                credit = False
            if credit:
                raise ArretCreditNA(cle, role, "état du relais")
            _plus(self.na_comptes["cause_non_etablie"], role)
            _plus(self.na_journal_arrets_cles["cause_non_etablie"], cle)
            return dict(a, issue_na="réponse illisible, cause non établie")
        return dict(a, issue_na="erreur")


# --- comptes, pour la ligne de la génération (lot 6) -------------------------------------------------------------------

def comptes_envois_na(lignes):
    """Comptes d'un journal relu (`journal_na_v3.verifier_journal`) : une ligne « envoi » suivie d'une ligne « non lancé »
    ou d'une ligne « non envoyé » qui la renvoie par son rang (écart d'égalité) n'est pas comptée comme partie ; aucune
    requête n'est comptée deux fois. Rend {"partis", "journalises_non_lances", "journalises_puis_refuses", "non_envoyes",
    "refus_ecrits"} par rôle."""
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


__all__ = ("AppelGardeNA", "ContexteAppelGardeNA", "ContexteRefuse", "ArretNA", "ArretMotifNA", "ArretRequeteJournaliseeNA",
           "ArretClassifieurNA", "ArretCreditNA", "ArretA2NA", "EtatRelaisIllisible", "relais_montre_refus_credit",
           "lecteur_etat_relais_http", "comptes_envois_na", "ARRET_REQUETE_JOURNALISEE", "PORTEE_ARRET_1_DEFAUT")
