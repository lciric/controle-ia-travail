"""Véhicule NA-1, lot 6 v5 — la génération et la course du régime, **branchées** sur le lot 4 v3 (repli) et le registre
v4 (`course_na_v5`).

Ce que la v5 change au v3 (`course_na_v3.py`, `7c154a89…`, gardé sans modification ; il reste la base des pièces reprises
ici par import : refus de câblage, contexte de génération, assemblage des requêtes, garde de motifs) :

- **Mélange du lot 4 v3** : `GenerationNAV5(appel_garde_na_v3.AppelGardeNA, GenerationV68)`. Le contexte d'appel reçoit
  `modeles_par_role`, `modeles_repli` et `pires_repli`, lus dans la configuration (`replis`, champ distinct de
  `a11_modeles`, qui reste vide) ; `lire_etat_relais` est retiré (lot 4 v2, § 5).
- **Les deux issues neuves** du lot 4 v3 sont lues : « refus par classifieur, servi par repli » (texte au portier, marqué
  `par_repli`) et « arrêt n° 1, consigné après trois refus ».
- **Registre des tentatives v4** (`registre_na_v4`, dans ce dossier : le v3 du lot 5 plus `id_tentative`, erratum 3) :
  chaque chaîne d'un proposeur (une à trois tentatives) y est écrite par `ajouter_chaine`, avec `type_ligne`, `par_repli`
  (au registre servi, par le v3), les classes de l'erratum 2 et un `id_tentative` par ligne. Les tentatives d'une chaîne
  sont lues dans `na_replis` (lot 4 v3), au rang près (`rang_repli` = rang de la tentative du lot 4 moins un).
- **Portier v3** (`portier_na_v3.PortierNAV3`) : la fonction `appeler` rend le dictionnaire du lot 4 v3, qui porte
  `par_repli` ; le passeport est marqué.
- **`juger`** : l'arrêt d'A2 sur la version servie d'un juge n'est pas levé quand `par_repli` est vrai ; la clé est
  (juge, modèle demandé) ; le n° 31 du lot 4 v3 reste la garde de chaque tentative.
- **Comptes de la ligne de la génération** : en plus du v3, les comptes du registre v4 (M6 par rôle, par espèce, par case,
  par (case, espèce), à la première tentative ; replis par espèce demandée et par modèle servi, nombre et coût ; M3 en
  lecture scellée et « espèces seules » ; M4 à la première tentative plus une ligne « replis »), la mesure « replis » du lot
  4 v3 (`comptes_replis_na`), et la garde du coffre sur les seules lignes `fiche` (servies par repli comprises).
- **Contrôle du code chargé** (additif v2, C-1 à C-4 ; arrêt n° 33, proposé) : au départ et à chaque génération, si la
  course le reçoit (`controle_code_charge`) ; son absence est **dite** au journal des arrêts (« non demandé »), jamais tue.
- Sorties en v5 (R12) : `journal-arrets-et-generations-na-v5.jsonl`, `bilan-course-na-v5.json`,
  `registre-tentatives-g<g>-na-v4.jsonl`.

**Ce qui n'est pas écrit au registre** (déclaré au rapport) : les chaînes du portier et des juges (l'interface ne fixe pas
leur classe ; elles sont dans `na_replis` et dans la mesure « replis ») ; une chaîne coupée par un arrêt qui arrête la
course (n° 12, 13, 16, 31, « requête journalisée ») ; un appel non lancé au rang 0 (ce n'est pas un appel).

Aucun message ne recopie un octet d'une réponse ou d'une fiche. Bibliothèque standard, orchestrateur `a41b7b50…`, v68, lots
2 à 5 et 10 a, lot 6 v3.
"""

import dataclasses
import os

from pole import appel_garde_na_v3 as ag
from pole import code_charge_na_v1 as cc
from pole import configuration_course_na_v1 as cfn
from pole import course_na_v3 as cn
from pole import identifiants_na_v1 as ident
from pole import journal_na_v3 as jn
from pole import portier_na_v1 as pt
from pole import portier_na_v3 as pt3
from pole import registre_na_v3 as rg3
from pole import registre_na_v4 as rg4
from pole import requete_na_v3 as rq
from pole import routage_na_v1 as rt
from pole import tirage_na_v4 as tn
from pole import verifier_registre_servi_na_v3 as vr3
from pole.budget_course_v68 import GardeBudgetCourseV68
from pole.budget_v53 import NON_MESUREE
from pole.course2_v68 import GenerationV68
from pole.juges_croises_v53 import lire_verdict
from pole.noyau_v54 import NoeudArret
from pole.noyau_v56 import ArretParSignal, ArretSurSignal, motif_arret
from pole.outils import ecrire_json_scelle

VERSION = "course-na-v5"
NOM_JOURNAL_ARRETS = "journal-arrets-et-generations-na-v5.jsonl"
NOM_BILAN = "bilan-course-na-v5.json"
ROLE_KIT_PROPOSEUR, ROLE_KIT_JUGE = cn.ROLE_KIT_PROPOSEUR, cn.ROLE_KIT_JUGE
LOT_JUGES = cn.LOT_JUGES
CODE_CHARGE_NON_DEMANDE = "contrôle du code chargé non demandé à la course (dit, non tu)"

# Issues d'un appel de proposeur (lot 6), v5 : celles du v3, et les deux neuves du lot 4 v3.
ISSUE_SERVI_PAR_REPLI = "texte rendu par repli, au portier"
ISSUE_ARRET_1_APRES_REPLI = "arrêt n° 1, consigné après trois refus"
ISSUE_ARRET_1_SANS_REPLI = cn.ISSUE_ARRET_1
# Raisons d'arrêt écrites au registre quand l'adaptateur ne les rend pas (déclarées au rapport).
RAISON_HORS_DIRECT_SERVIE = "non rendue par l'adaptateur (réponse servie, hors adaptateur direct)"
RAISON_REFUS_SANS_REPLI = "refus de classifieur, sans repli (commande externe ou protocole)"
CATEGORIE_NON_LUE = "catégorie non lue"


class DefautLot6V5(cn.DefautLot6):
    """Un défaut de programme du lot 6 v5 : arrêt, motif dit."""


class ArretCodeChargeCourseNA(cn.ArretCourseNA):
    """N° 33 (proposé) : module chargé hors table ou d'une autre empreinte (C-1), au départ ou à une génération."""

    numero = cc.NUMERO_ARRET

    def __init__(self, moment, cause):
        super().__init__(f"arrêt n° {self.numero} (proposé), code chargé : {moment} ; {cause}")
        self.moment, self.cause = moment, cause


ARRETS_CONNUS_V5 = (
    (ArretCodeChargeCourseNA, cc.NUMERO_ARRET, "code chargé hors table ou d'une autre empreinte (proposé)"),
    (cc.ArretCodeChargeNA, cc.NUMERO_ARRET, "code chargé hors table ou d'une autre empreinte (proposé)"),
    (vr3.RegistreServiNonConformeV3, None, "registre servi non conforme (n° 8, 9 ou 19)"),
    (rg4.RegistreRefuse, None, "registre des tentatives : ligne ou chaîne refusée"),
    (ag.ArretMotifNA, 16, "motif interdit dans un texte à servir"),
    (ag.ArretCreditNA, 13, "refus pour crédit"),
    (ag.ArretClassifieurNA, 1, "refus d'un classifieur de sûreté"),
    (ag.ArretA2NA, ag.NUMERO_ARRET_A2, "n° 31 (proposé) : modèle servi absent ou différent du modèle demandé"),
    (ag.PireManquantNA, ag.NUMERO_ARRET_PIRE, "n° 34 (proposé) : pire manquant pour un (rôle, modèle)"),
    (ag.ArretRequeteJournaliseeNA, None, "requête journalisée"),
    (pt3.PortierRefuse, None, "portier : issue d'appel sans la marque `par_repli`"),
) + tuple(e for e in cn.ARRETS_CONNUS if e[0] not in (cn.ag.ArretMotifNA, cn.ag.ArretCreditNA, cn.ag.ArretClassifieurNA,
                                                       cn.ag.ArretA2NA, cn.ag.ArretRequeteJournaliseeNA))


def decrire_arret(e):
    for classe, numero, nom in ARRETS_CONNUS_V5:
        if isinstance(e, classe):
            break
    else:
        numero, nom = None, "arrêt non nommé (défaut ou exception de base)"
    d = cn.decrire_arret(e)
    d.update(numero=numero, nom=nom)
    return d


class JournalArretsGenerationsNAV5(cn.JournalArretsGenerationsNA):
    VERSION = "journal-arrets-et-generations-na-v5"


# --- les replis, lus dans la configuration ----------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class ReplisNA:
    modeles_par_role: dict
    modeles_repli: tuple
    pires_repli: dict


def lire_replis(config, table):
    """Le champ `replis` de la configuration (champ distinct de `a11_modeles`, P16) : `modeles_repli` (deux, dans l'ordre
    de GO-35), `pires_repli_usd` ({rôle d'une clé Claude : {modèle de repli : USD}}). Le modèle de chaque rôle d'une clé
    Claude est lu dans la configuration du noyau (proposeurs, aiguilleur, juges). Rien n'a de défaut."""
    r = config.objet.get("replis")
    if not isinstance(r, dict) or sorted(r) != ["modeles_repli", "pires_repli_usd"]:
        raise cfn.ConfigurationCourseRefusee("replis : exactement `modeles_repli` et `pires_repli_usd` (aucun défaut)")
    if config.gardes.get("a11_modeles") != []:
        raise cfn.ConfigurationCourseRefusee("A11 reste vide : les modèles de repli vivent dans `replis`")
    noyau = config.noyau
    modele_de = {p["etiquette"]: p["modele"] for p in noyau["proposeurs"]}
    modele_de.update({j["etiquette"]: j["modele"] for j in noyau["juges"]})
    modele_de[noyau["aiguilleur"]["etiquette"]] = noyau["aiguilleur"]["modele"]
    claude = [ro for ro, e in table.roles.items() if e.cle != rt.CLE_HORS_COURSE and table.cles[e.cle].type == ag.TYPE_CLE_CLAUDE]
    if any(ro not in modele_de for ro in claude):
        raise cfn.ConfigurationCourseRefusee("replis : un rôle d'une clé Claude sans modèle dans la configuration du noyau")
    return ReplisNA({ro: modele_de[ro] for ro in claude}, tuple(r["modeles_repli"]),
                    {ro: dict(v) for ro, v in r["pires_repli_usd"].items()})


def modeles_demandes(replis, config):
    """La liste fermée des modèles demandés d'une génération (registre v4) : ceux de la configuration et les deux de repli."""
    noyau = config.noyau
    ms = [p["modele"] for p in noyau["proposeurs"]] + [j["modele"] for j in noyau["juges"]] + [noyau["aiguilleur"]["modele"]]
    vus = []
    for m in ms + list(replis.modeles_repli):
        if m not in vus:
            vus.append(m)
    return tuple(vus)


# --- d'une suite de tentatives du lot 4 v3 à une chaîne du registre ----------------------------------------------------

def espece_de(table, role):
    e = table.entree(role)
    if e is None or type(e.espece) is not int or e.sorte != "proposeur":
        raise DefautLot6V5("une chaîne au registre est celle d'un proposeur de la table")
    return f"espece-{e.espece}"


def chaine_au_registre(tents, *, espece, case, classe_servie=None):
    """Les tentatives (lignes de `na_replis`, avec `raison_arret` relevée par `_consigner_tentative_na`) en dictionnaires
    du registre v3/v4. Rend None si rien n'est un appel (non lancé au rang 0). Les classes suivent l'erratum 2 :
    servie : refus précédents « servi par repli », la dernière la classe de sa réponse ; sans réponse : toutes « réponse
    illisible » ; trois refus : toutes « refus du modèle »."""
    if not tents:
        return None
    rendu = []
    for t in tents:
        issue = t["issue"]
        if issue == "non lancé" and t["rang_tentative"] == 1:
            return None
        sans_reponse = issue in ("non lancé", ag.ISSUE_ERREUR) or (issue == ag.ISSUE_ILLISIBLE and t.get("raison_arret") is None)
        if sans_reponse:
            raison, servi = rg3.RAISON_SANS_REPONSE, None
        elif issue == "refus de classifieur":
            raison, servi = rg3.RAISON_REFUS, t["modele_servi"]
        elif issue == ag.ISSUE_ARRET_1:
            raison, servi = RAISON_REFUS_SANS_REPLI, t["modele_servi"] or None
        else:
            raison, servi = t.get("raison_arret") or RAISON_HORS_DIRECT_SERVIE, t["modele_servi"]
        cat = t.get("categorie")
        cat = None if cat in (None, CATEGORIE_NON_LUE) or raison != rg3.RAISON_REFUS else cat
        rendu.append({"espece": espece, "case": case, "rang_repli": t["rang_tentative"] - 1,
                      "modele_demande": t["modele_demande"], "modele_servi": servi, "raison_arret": raison,
                      "categorie_refus": cat, "cout_compte_usd": t["cout_micro"] / 1_000_000, "classe_issue": None})
    der = rendu[-1]
    if der["raison_arret"] == rg3.RAISON_REFUS:
        for t in rendu:
            t["classe_issue"] = rg3.CLASSE_TROIS_REFUS
    elif der["raison_arret"] == rg3.RAISON_SANS_REPONSE:
        for t in rendu:
            t["classe_issue"] = rg3.CLASSE_SANS_REPONSE
    else:
        for t in rendu[:-1]:
            t["classe_issue"] = rg3.REFUS_SERVI_PAR_REPLI
        if der["raison_arret"] == RAISON_REFUS_SANS_REPLI:
            der["classe_issue"] = rg3.CLASSE_TROIS_REFUS
        else:
            if classe_servie not in pt.CLASSES_APPEL:
                raise DefautLot6V5("chaîne servie : la classe de sa réponse (portier, ou programme) est dite")
            der["classe_issue"] = classe_servie
    return rendu


@dataclasses.dataclass
class ReponseGardeeV5:
    texte: str
    case: rq.CaseServie
    role: str
    identifiant: str
    jetons_fiche: dict
    tentatives: list
    par_repli: bool


# --- la génération -------------------------------------------------------------------------------------------------------

class GenerationNAV5(ag.AppelGardeNA, GenerationV68):
    """La génération du régime : le mélange du lot 4 v3 devant `GenerationV68`."""

    fournisseurs_requis = staticmethod(cn.GenerationNA.fournisseurs_requis)

    def __init__(self, conf, sortie, adaptateurs, *, contexte_na, course_na, numero, modeles_demandes, **kw):
        if not isinstance(course_na, cn.ContexteGenerationNA):
            raise DefautLot6V5("la génération du véhicule exige le contexte de la course (`ContexteGenerationNA`)")
        if kw.get("heritage_selection") is not None or kw.get("heritage_texte") is not None:
            raise DefautLot6V5("aucun héritage de la v68 : le registre est servi par la proposition neuve")
        kw["heritage_selection"] = None
        cn.refuser_cablage(course_na.etat_colonne, getattr(contexte_na, "journal", None),
                           f"construction de la génération {numero}")
        self.course_na = course_na
        super().__init__(conf, sortie, adaptateurs, contexte_na=contexte_na, numero=numero, **kw)
        if self.na.numero_generation != numero:
            raise DefautLot6V5("le contexte d'appel n'est pas celui de cette génération")
        self.portier = pt3.PortierNAV3(consigne=course_na.consigne_portier, declaration=course_na.declaration,
                                       bornes=course_na.bornes, appeler=self._appeler_portier, dossier_sortie=sortie,
                                       nom_journal=f"journal-portier-g{numero}.jsonl", generation=numero)
        self.registre_na = rg4.RegistreTentativesV4(sortie, f"registre-tentatives-g{numero}-na-v4.jsonl", generation=numero,
                                                    cases_servies=[c.identifiant for c in course_na.cases],
                                                    modeles_demandes=modeles_demandes)
        self.modeles_demandes_na = tuple(modeles_demandes)
        self.reponses_na, self.issues_reponses_na, self.passees_na = [], [], []
        self.jetons_noyau_na = {}
        self._etat_aiguillage = None
        self._appels_portier = 0
        self.comptes_lot6 = {
            "appels_proposeur": {}, "issues_proposeur": {}, "cases_non_jouees": {}, "refus_ecrits_proposeur": {},
            "verdicts_absents": {}, "appels_juge": {}, "fiches_jugees": 0, "registre_servi_recu_par": 0,
            "chaines_au_registre": 0, "verdicts_juges_par_repli": {},
        }

    # --- le lot 4 v3 : la raison d'arrêt de chaque tentative est relevée (crochet du mélange) ------------------------

    def _consigner_tentative_na(self, tentatives, *, r=None, **kw):
        ligne = super()._consigner_tentative_na(tentatives, r=r, **kw)
        t = getattr(r, "tentative", None) if r is not None else None
        ligne["raison_arret"] = t.get("raison_arret") if isinstance(t, dict) else None
        return ligne

    etape_passe_tableau = cn.GenerationNA.etape_passe_tableau
    etape_fusions = cn.GenerationNA.etape_fusions
    _espece = cn.GenerationNA._espece
    _jeton_fiche = cn.GenerationNA._jeton_fiche
    _identifiant_fiche = cn.GenerationNA._identifiant_fiche
    identifiant_servi_juge = cn.GenerationNA.identifiant_servi_juge
    etape_juges = cn.GenerationNA.etape_juges
    lot_mesure = cn.GenerationNA.lot_mesure
    sceller_na = cn.GenerationNA.sceller_na

    # --- la proposition ---------------------------------------------------------------------------------------------

    def _proposer(self, etat, passe, supplement_par_case=None):
        if passe != 1 or supplement_par_case is not None:
            raise cn.EtapeNeutraliseeJouee("arrêt « étape neutralisée jouée » : seule la proposition (passe 1) est jouée")
        for case in self.course_na.cases:
            for p in self.conf["proposeurs"]:
                role = p["etiquette"]
                requete = self.course_na.requetes[(case.identifiant, role)]
                if requete.registre == rq.REGISTRE_SERVI:
                    self.comptes_lot6["registre_servi_recu_par"] += 1
                cn._plus(self.comptes_lot6["appels_proposeur"], role)
                debut = len(self.na_replis)
                a = self.appel(etat, role=role, role_kit=ROLE_KIT_PROPOSEUR, fournisseur=p["fournisseur"], modele=p["modele"],
                               consigne=requete, plafond_role="proposeur", session=("proposition", case.identifiant, role),
                               lire=cn._lire_texte)
                self._classer_retour_proposeur(a, case, role, [dict(t) for t in self.na_replis[debut:]])
        return []

    def _issue(self, role, issue):
        cn._plus(self.comptes_lot6["issues_proposeur"].setdefault(role, {}), issue)

    def _ecrire_chaine(self, tents, case, role, classe_servie=None, fiches=()):
        ch = chaine_au_registre(tents, espece=espece_de(self.course_na.table, role), case=case.identifiant,
                                classe_servie=classe_servie)
        if ch is None:
            return None
        self.registre_na.ajouter_chaine(ch, fiches)
        self.comptes_lot6["chaines_au_registre"] += 1
        return ch

    def _classer_retour_proposeur(self, a, case, role, tents):
        if a is None:
            self._issue(role, cn.ISSUE_NON_LANCE)
            return self._ecrire_chaine(tents, case, role)
        if "refus_ecrit" in a:
            self._issue(role, cn.ISSUE_REFUS_ECRIT)
            cn._plus(self.comptes_lot6["cases_non_jouees"], str(self._espece(role)))
            cn._plus(self.comptes_lot6["refus_ecrits_proposeur"], role)
            n = self.comptes_lot6["refus_ecrits_proposeur"][role]
            if n >= self.course_na.seuil_refus_ecrits:
                raise cn.ArretRemplacementRefusEcritsNA(role, n, self.numero)
            return None
        issue = a.get("issue_na")
        if issue == ag.ISSUE_ARRET_1_APRES_REPLI:
            self._issue(role, ISSUE_ARRET_1_APRES_REPLI)
            return self._ecrire_chaine(tents, case, role)
        if issue == ag.ISSUE_ARRET_1:
            self._issue(role, ISSUE_ARRET_1_SANS_REPLI)
            return self._ecrire_chaine(tents, case, role)
        if issue == ag.ISSUE_ILLISIBLE:
            self._issue(role, cn.ISSUE_ILLISIBLE_CAUSE)
            return self._ecrire_chaine(tents, case, role, classe_servie=pt.ILLISIBLE)
        if issue == ag.ISSUE_ERREUR:
            self._issue(role, cn.ISSUE_ILLISIBLE_ERREUR)
            return self._ecrire_chaine(tents, case, role, classe_servie=pt.ILLISIBLE)
        if issue not in (ag.ISSUE_OK, ag.ISSUE_SERVI_PAR_REPLI):
            raise DefautLot6V5("issue d'appel inconnue du mélange du lot 4 v3")
        par_repli = a.get("par_repli")
        if type(par_repli) is not bool or par_repli != (issue == ag.ISSUE_SERVI_PAR_REPLI):
            raise DefautLot6V5("issue servie sans la marque `par_repli` cohérente")
        texte = a.get("lu")
        if texte is None:  # servie, non lue (coupée, ou délai d'A3) : « réponse illisible » par programme
            self._issue(role, cn.ISSUE_ILLISIBLE_NON_LUE)
            return self._ecrire_chaine(tents, case, role, classe_servie=pt.ILLISIBLE)
        if type(texte) is not str:
            raise DefautLot6V5("la lecture d'un proposeur rend le texte tel quel")
        self._issue(role, ISSUE_SERVI_PAR_REPLI if par_repli else cn.ISSUE_TEXTE_RENDU)
        jeton_rep = "r" + self.graines.jeton_opaque(self.tache("ident-reponse", 1, case.identifiant, role), 6)
        self.reponses_na.append(ReponseGardeeV5(texte, case, role, ident.reencoder_jeton_noyau(jeton_rep, "r", 6), {},
                                                tents, par_repli))
        return None

    # --- l'aiguillage : le portier v3 -------------------------------------------------------------------------------

    _appeler_portier = cn.GenerationNA._appeler_portier

    def etape_aiguillage(self, etat):
        self._etat_aiguillage = etat
        try:
            for rep in self.reponses_na:
                issue = self.portier.traiter_reponse(rep.texte, case=rep.case, identifiant_reponse=rep.identifiant,
                                                     identifiant_fiche=self._identifiant_fiche(rep))
                self.issues_reponses_na.append((rep.role, issue))
                self._ecrire_chaine(rep.tentatives, rep.case, rep.role, classe_servie=issue.classe_appel,
                                    fiches=issue.fiches)
                for f in issue.fiches:
                    if f.classe == pt.PASSEE:
                        self.passees_na.append(f)
                        fournisseur = next(p["fournisseur"] for p in self.conf["proposeurs"] if p["etiquette"] == rep.role)
                        self.fiches[f.identifiant] = {"ident": f.identifiant, "contenu": f.contenu, "empreinte": f.empreinte,
                                                      "meta": {"case": f.identifiant_case, "proposeur": rep.role,
                                                               "fournisseur": fournisseur, "origine": "proposition",
                                                               "passe": 1, "par_repli": rep.par_repli}}
                        self.ordre.append(f.identifiant)
        finally:
            self._etat_aiguillage = None

    # --- `juger` : A2 non levé sur un verdict servi par repli --------------------------------------------------------

    def juger(self, fiche, lot, etat):
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
            cn._plus(self.comptes_lot6["appels_juge"], nom)
            a = self.appel(etat, role=nom, role_kit=ROLE_KIT_JUGE, fournisseur=j["fournisseur"], modele=j["modele"],
                           consigne=requete, plafond_role="juge",
                           session=("juges", fiche.identifiant_case, nom, fiche.identifiant),
                           lire=lambda t: lire_verdict(t, self.conf["items_juge"]))
            v = None
            if a is None:
                cn._plus(self.comptes_lot6["verdicts_absents"].setdefault(nom, {}), "non lancé")
            elif "refus_ecrit" in a:
                cn._plus(self.comptes_lot6["verdicts_absents"].setdefault(nom, {}), "refus écrit")
            else:
                r = a["r"]
                servi = getattr(r, "modele_servi", None)
                if a.get("par_repli") is True:
                    cn._plus(self.comptes_lot6["verdicts_juges_par_repli"], nom)
                elif getattr(r, "statut", None) == "ok" and servi:
                    vu = self.modele_servi_juges.setdefault(f"{nom} ; {j['modele']}", servi)
                    if vu != servi:
                        raise ag.ArretA2NA(nom, "version servie d'un juge changée entre deux fiches, sans repli")
                v = a.get("lu")
                if v is None:
                    cn._plus(self.comptes_lot6["verdicts_absents"].setdefault(nom, {}), "verdict illisible")
            if v is None:
                self.absents_juges[nom] = self.absents_juges.get(nom, 0) + 1
            verdicts[nom] = v
            presents[nom] = v is not None
            self.cles_anonymisation.setdefault(nom, {})[ident_servi] = fiche.identifiant
        self.coffre.deposer(f"verdicts-{lot}-{fiche.identifiant}", {"ident": fiche.identifiant, "empreinte": fiche.empreinte,
                                                                     "verdicts": verdicts})
        self.verdicts_presents[fiche.identifiant] = presents
        return True

    def lignes_registre(self, exiger_sceau=False):
        return rg4.lire_registre_tentatives_v4(self.registre_na.chemin, generation=self.numero,
                                               cases_servies=[c.identifiant for c in self.course_na.cases],
                                               modeles_demandes=self.modeles_demandes_na, exiger_sceau=exiger_sceau)

    def verifier_aucune_fiche_sans_classe(self):
        fiches = [l for l in self.lignes_registre() if l["type_ligne"] == rg3.TYPE_FICHE]
        if len(fiches) != self.portier.comptes()["fiches_rendues"] or any(l["classe"] not in pt.CLASSES_FICHE for l in fiches):
            raise DefautLot6V5("une fiche rendue sans classe, ou absente du registre, à la fin de la génération")
        return len(fiches)


# --- comptes du registre v4 -----------------------------------------------------------------------------------------------

def _plus(d, k, n=1):
    d[k] = d.get(k, 0) + n


CLASSES_M6 = (pt.VIDE_MOTIVEE, pt.REFUS_DU_MODELE, pt.ILLISIBLE, rg3.REFUS_SERVI_PAR_REPLI)


def comptes_registre_v4(lignes, role_de_l_espece):
    """M6 (première tentative de chaque chaîne : sa classe à l'espèce demandée — « servi par repli » si une tentative de
    repli est servie, P12 ; trois refus : hors de M6, arrêt n° 1), replis (rangs 1 et 2 : par espèce demandée et modèle
    servi, nombre et coût ; servies par repli au nom du modèle servi), M3 (scellée ; « espèces seules »), M4 (rang 0 à
    l'espèce ; ligne « replis »)."""
    tents = [l for l in lignes if l["type_ligne"] == rg3.TYPE_TENTATIVE]
    fiches = [l for l in lignes if l["type_ligne"] == rg3.TYPE_FICHE]
    chaines = {}
    for l in tents:
        chaines.setdefault(l[rg4.CHAMP_ID][:8], []).append(l)
    m6 = {"par_role": {}, "par_espece": {}, "par_case": {}, "par_case_et_espece": {}, "trois_refus_arret_1": {}}
    for ch in chaines.values():
        t0, der = ch[0], ch[-1]
        servie = der["raison_arret"] not in (rg3.RAISON_REFUS, rg3.RAISON_SANS_REPONSE)
        if der["raison_arret"] == rg3.RAISON_REFUS or der["raison_arret"] == RAISON_REFUS_SANS_REPLI:
            _plus(m6["trois_refus_arret_1"], t0["espece"])
            continue
        k = rg3.REFUS_SERVI_PAR_REPLI if servie and der["rang_repli"] > 0 else der["classe_issue"]
        if k not in CLASSES_M6:
            continue
        _plus(m6["par_role"].setdefault(role_de_l_espece.get(t0["espece"], t0["espece"]), {}), k)
        _plus(m6["par_espece"].setdefault(t0["espece"], {}), k)
        _plus(m6["par_case"].setdefault(t0["case"], {}), k)
        _plus(m6["par_case_et_espece"].setdefault(t0["case"], {}).setdefault(t0["espece"], {}), k)
    replis = {"par_espece_et_modele_servi": {}, "servies_par_repli": {}}
    for l in tents:
        if l["rang_repli"] == 0:
            continue
        servi = l["modele_servi"] or "aucun (sans réponse)"
        e = replis["par_espece_et_modele_servi"].setdefault(l["espece"], {}).setdefault(servi, {"nombre": 0, "cout_usd": 0.0})
        e["nombre"] += 1
        e["cout_usd"] = round(e["cout_usd"] + l["cout_compte_usd"], 6)
        if l["raison_arret"] not in (rg3.RAISON_REFUS, rg3.RAISON_SANS_REPONSE):
            s = replis["servies_par_repli"].setdefault(l["modele_servi"], {"tentatives": {}, "fiches": {}})
            _plus(s["tentatives"], l["classe_issue"])
    for l in fiches:
        if l["rang_repli"] > 0:
            s = replis["servies_par_repli"].setdefault(l["modele_servi"], {"tentatives": {}, "fiches": {}})
            _plus(s["fiches"], l["classe"])
    m3 = {"scellee": {}, "especes_seules": {}}
    for l in fiches:
        for lec in ["scellee"] + (["especes_seules"] if l["rang_repli"] == 0 else []):
            c = m3[lec].setdefault(l["case"], {"rendues": 0, pt.AU_COFFRE: 0, pt.HORS_CASE: 0})
            c["rendues"] += 1
            if l["classe"] in (pt.AU_COFFRE, pt.HORS_CASE):
                c[l["classe"]] += 1
    m4 = {"par_espece": {}, "replis": {"cout_usd": 0.0, "par_modele_demande": {}, "fiches_passees": 0}}
    for l in tents:
        if l["rang_repli"] == 0:
            e = m4["par_espece"].setdefault(l["espece"], {"cout_usd": 0.0, "fiches_passees": 0})
            e["cout_usd"] = round(e["cout_usd"] + l["cout_compte_usd"], 6)
        else:
            m4["replis"]["cout_usd"] = round(m4["replis"]["cout_usd"] + l["cout_compte_usd"], 6)
            pm = m4["replis"]["par_modele_demande"]
            pm[l["modele_demande"]] = round(pm.get(l["modele_demande"], 0.0) + l["cout_compte_usd"], 6)
    for l in fiches:
        if l["classe"] == pt.PASSEE:
            if l["rang_repli"] == 0:
                m4["par_espece"].setdefault(l["espece"], {"cout_usd": 0.0, "fiches_passees": 0})["fiches_passees"] += 1
            else:
                m4["replis"]["fiches_passees"] += 1
    return {"chaines": len(chaines), "lignes_tentative": len(tents), "lignes_fiche": len(fiches), "m6": m6,
            "replis": replis, "m3": m3, "m4": m4}


def ligne_de_generation_v5(gen, g, *, copie_sha256, journal, journal_sha256, servi, constat, lignes_registre):
    """La ligne du v3 (mêmes clés, mêmes sources), plus `comptes_registre_v4`, `comptes_replis_lot_4` et le coffre sur les
    lignes `fiche`."""
    lignes_journal = jn.verifier_journal(journal.chemin, exiger_sceau=True)
    comptes_portier = gen.portier.comptes()
    par_role, par_adaptateur = cn._couts_par_role(gen.coffre.consommations())
    roles = {espece_de(gen.course_na.table, p["etiquette"]): p["etiquette"] for p in gen.conf["proposeurs"]}
    dont_repli = sum(1 for l in lignes_registre if l["type_ligne"] == rg3.TYPE_FICHE and l["rang_repli"] > 0)
    return {
        "generation": g,
        "cases_servies": [c.identifiant for c in gen.course_na.cases],
        "copie_configuration_sha256": copie_sha256,
        "registre_servi": (None if servi is None else {
            "sha256": servi.sha256, "taille": servi.taille, "lignes": servi.lignes, "lignes_tentative": servi.lignes_tentative,
            "lignes_compte": servi.lignes_compte, "comptes_permutes": servi.comptes_permutes,
            "section": rq.REGISTRE_SERVI if servi.taille else rq.REGISTRE_OMIS,
            "requetes_l_ayant_recu": gen.comptes_lot6["registre_servi_recu_par"],
            "marques_par_repli": len(rg3.marques_par_repli(servi))}),
        "comptes_melange_lot_4": gen.na_comptes,
        "comptes_portier_lot_5": comptes_portier,
        "comptes_journal_lot_3": jn.comptes(lignes_journal),
        "comptes_envois_lot_4": ag.comptes_envois_na(lignes_journal),
        "comptes_replis_lot_4": ag.comptes_replis_na(gen.na_replis),
        "comptes_lot_6": gen.comptes_lot6,
        "comptes_registre_v4": comptes_registre_v4(lignes_registre, roles),
        "au_coffre_par_refus_du_portier": comptes_portier["au_coffre_par_refus_du_portier"],
        "arrets_consignes": gen.na_arrets_consignes,
        "coffre": {"au_coffre": constat.au_coffre, "rendues": constat.rendues, "depasse": constat.depasse,
                   "consigne": constat.consigne, "dont_servies_par_repli": dont_repli},
        "etapes": dict(gen.etapes_etat),
        "cout_generation_usd": round(gen.budget.cumul, 6),
        "cout_par_role_usd": par_role,
        "cout_par_adaptateur_usd": par_adaptateur,
        "memoire": {"fichier": "memoire.json", "servie": False},
        "journal_requetes_sha256": journal_sha256,
        "noeud": gen.noeud,
    }


def fabriquer_registre_servi_na_v5(config, generation, lignes_par_generation, cases_par_generation):
    """Le registre servi marqué `par_repli` (lot 5 v3), à partir des registres v4 scellés des générations précédentes,
    vérifié par programme (arrêts n° 8, 9, 19) avant tout envoi."""
    lignes = [l for g in range(1, generation) for l in lignes_par_generation[g]]
    servi = rg4.fabriquer_registre_servi_v4(lignes, {g: list(cases_par_generation[g]) for g in range(1, generation)},
                                            generation, permuter_comptes=config.objet["permuter_comptes"])
    noms = [l["identifiant"] for l in lignes if l["type_ligne"] == rg3.TYPE_FICHE and l["classe"] == pt.PASSEE]
    cases = [c for g in range(1, generation) for c in cases_par_generation[g]]
    if servi.taille:
        vr3.verifier_registre_servi_v3(servi.octets, borne_registre_octets=cfn.borne(config, "registre_octets"),
                                       borne_enonce_octets=cfn.borne(config, "enonce_octets"), noms_attendus=noms,
                                       cases_attendues=cases)
    return servi


def _controler_code(controle_code_charge, moment):
    if controle_code_charge is None:
        return CODE_CHARGE_NON_DEMANDE
    try:
        return controle_code_charge(moment)
    except cc.ArretCodeChargeNA as e:
        raise ArretCodeChargeCourseNA(moment, e.cause) from None


# --- la course ------------------------------------------------------------------------------------------------------------

def executer_course_na_v5(config, sortie, adaptateurs, *, regime, nombre_generations, ligne_accord_usd, additif_sha256,
                          etat_colonne, fabrique_journal, controle_code_charge, go=None, portes=None, horloge=None,
                          racine_sessions=None, crochets=None, gardes_depart_en_plus=()):
    """La course du régime, v5 : celle du v3 (même ordre des gardes), sur le lot 4 v3 et le registre v4.
    `controle_code_charge` : `f(moment) -> liste des modules vérifiés`, ou None, dit au journal (jamais tu)."""
    if type(etat_colonne) is not int or etat_colonne not in cn.ETATS_COLONNE:
        raise cn.ArretCablageColonneNA("départ de la course, avant toute écriture", etat_colonne, None,
                                       "état de l'interrupteur inconnu (0, 1 ou 2 attendu)")
    if not callable(fabrique_journal):
        raise cn.ArretCablageColonneNA("départ de la course, avant toute écriture", etat_colonne, fabrique_journal,
                                       "fabrique de journal absente")
    if controle_code_charge is not None and not callable(controle_code_charge):
        raise DefautLot6V5("contrôle du code chargé : une fonction, ou None (dit au journal)")
    crochets = dict(crochets or {})
    code_depart = _controler_code(controle_code_charge, "départ de la course")
    epingle = next((p.sha256 for p in config.pieces_epinglees if p.nom == "additif du véhicule"), None)
    plafond_course = cfn.verifier_regime(config, regime=regime, nombre_generations=nombre_generations,
                                         ligne_accord_usd=ligne_accord_usd, additif_sha256=additif_sha256,
                                         additif_epingle_sha256=epingle)
    gardes = cfn.verifier_gardes_heritees(config)
    cfn.verifier_empreintes(config, "départ de la course")
    table = cfn.table_de_course(config)
    replis = lire_replis(config, table)
    demandes = modeles_demandes(replis, config)
    garde = cn.construire_garde(config)
    gabarit, synthese, consigne_portier, consigne_juges = cfn.charger_pieces_servies(config)
    tirage = cfn.lire_tirage(config)
    cases = rq.cases_du_tirage(tirage, gabarit)
    declaration, bornes = cfn.declaration_portier(config), cfn.bornes_fiche(config)
    borne_requete = cfn.borne(config, "requete_proposeur_octets")
    seuil = config.gardes["garde_remplacement_refus_ecrits_proposeur"]
    if os.path.exists(sortie):
        raise cfn.ConfigurationCourseRefusee("sortie déjà présente : jamais écrasée (R12)")
    os.makedirs(os.path.join(sortie, cn.DOSSIER_JOURNAUX))
    journal_arrets = JournalArretsGenerationsNAV5(sortie, NOM_JOURNAL_ARRETS)
    if callable(adaptateurs):
        adaptateurs, portes_fabriquees = adaptateurs(sortie)
        portes = portes if portes is not None else portes_fabriquees
    copies = {g: cfn.deriver_copie_generation(config, cases[str(g)]) for g in (1, 2, 3)}
    journal_arrets.ecrire("départ", depart={"version": VERSION, "regime": cfn.REGIME, "gardes_heritees": gardes,
                                            "plafond_course_usd": plafond_course, "empreintes": cfn.table_des_empreintes(config),
                                            "statut_des_valeurs": config.statut, "go": go, "etat_colonne": etat_colonne,
                                            "modeles_repli": list(replis.modeles_repli), "code_charge": code_depart})
    journal_arrets.ecrire("copies de configuration", copies={str(g): copies[g][1] for g in copies})
    cumul = rt.CumulParCle(table)
    budget = GardeBudgetCourseV68(plafond_course)
    s17 = float(config.objet["plafond_generation_usd"])
    memoire, bilan, arret, lignes_reg, cases_ids = None, [], None, {}, {}
    poste, g, journal_g1 = None, None, None
    with ArretSurSignal() as signal:
        try:
            journal_g1 = cn._ouvrir_journal(fabrique_journal, sortie, 1)
            cn.refuser_cablage(etat_colonne, journal_g1, "départ de la course")
            for g in range(1, nombre_generations + 1):
                poste = f"generation-{g}"
                moment = f"départ de la génération {g}"
                _controler_code(controle_code_charge, moment)
                cfn.verifier_empreintes(config, moment)
                copie, copie_sha = crochets.get("copie", lambda g_, c: c)(g, copies[g][0]), copies[g][1]
                cfn.verifier_copie(copie, copie_sha, g)
                tn.garde_disjonction(tirage, g, cfn.triplets_de_la_copie(copie, tirage, g))
                cases_g = tuple(cases[str(g)])
                cases_ids[g] = [c.identifiant for c in cases_g]
                servi = None if g == 1 else fabriquer_registre_servi_na_v5(config, g, lignes_reg, cases_ids)
                ctx = {"cases": cases_g, "gabarit": gabarit, "synthese": synthese, "registre": servi}
                requetes = cn.assembler_requetes_proposeurs(ctx, copie, g, config.objet["titre_registre"], borne_requete)
                for f in gardes_depart_en_plus:
                    f(g, servi, requetes)
                budget.reserver(poste, s17)
                journal = journal_g1 if g == 1 else cn._ouvrir_journal(fabrique_journal, sortie, g)
                contexte_na = ag.ContexteAppelGardeNA(
                    numero_generation=g, table=table, parts=dict(config.objet["parts_usd"]),
                    pires_par_role=dict(config.objet["pires_par_role_usd"]), journal=journal, garde=garde,
                    identifiant_case_de_session=lambda s: s[1], cumul=cumul, modeles_par_role=dict(replis.modeles_par_role),
                    modeles_repli=replis.modeles_repli, pires_repli=dict(replis.pires_repli),
                    portee_arret_1=config.objet["portee_arret_1"])
                course_na = cn.ContexteGenerationNA(gabarit, synthese, consigne_portier, consigne_juges, declaration, bornes,
                                                    cases_g, requetes, servi, seuil, table, etat_colonne=etat_colonne)
                rs = None if racine_sessions is None else os.path.join(racine_sessions, f"generation-{g}")
                gen = None
                try:
                    gen = GenerationNAV5(copie, os.path.join(sortie, f"generation-{g}"), adaptateurs,
                                         contexte_na=contexte_na, course_na=course_na, numero=g, modeles_demandes=demandes,
                                         memoire=memoire, go=go, horloge=horloge, racine_sessions=rs, portes=portes)
                    if "avant_execution" in crochets:
                        crochets["avant_execution"](g, gen)
                    gen.executer()
                except BaseException:
                    budget.noter_arret(poste, gen.budget.cumul if gen is not None else 0.0)
                    if gen is not None:
                        gen.sceller_na()
                    cn._sceller_si_ouvert(journal)
                    raise
                budget.compter(poste, gen.budget.cumul)
                gen.sceller_na()
                if gen.noeud:
                    etape = next((n for n, e in gen.etapes_etat.items() if e == NON_MESUREE), None)
                    if not journal.scelle:
                        journal.sceller()
                    if etape is not None:
                        raise cn.ArretSeuilsGenerationNA(g, etape, gen.etapes_etat[etape])
                    raise NoeudArret(f"génération {g} : nœud")
                gen.verifier_aucune_fiche_sans_classe()
                journal_sha = journal.sceller()
                lignes_reg[g] = gen.lignes_registre(exiger_sceau=True)
                rg4.verifier_unicite_course(lignes_reg)
                constat = rg4.garde_du_coffre_v4(lignes_reg[g], g)
                ligne = ligne_de_generation_v5(gen, g, copie_sha256=copie_sha, journal=journal, journal_sha256=journal_sha,
                                               servi=servi, constat=constat, lignes_registre=lignes_reg[g])
                bilan.append(ligne)
                journal_arrets.ecrire("génération", generation=g, ligne=ligne)
                journal_arrets.ecrire("cumul par clé", generation=g, cles={
                    "cumul": cumul.etat(), "cause_non_etablie_par_cle": gen.na_journal_arrets_cles["cause_non_etablie"],
                    "tentatives_de_repli_par_cle": gen.na_journal_arrets_cles["tentatives_de_repli"]})
                memoire = gen.memoire
                poste = None
                if "entre_generations" in crochets:
                    crochets["entre_generations"](g)
        except BaseException as e:
            refus_sceau_g1 = None
            try:
                cn._sceller_si_ouvert(journal_g1)
            except (jn.JournalRefuse, OSError) as e_sceau:
                refus_sceau_g1 = type(e_sceau).__name__
            arret = decrire_arret(e)
            arret["poste"] = poste
            arret["generation"] = g
            if refus_sceau_g1 is not None:
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


lire_journal_arrets_generations = cn.lire_journal_arrets_generations

__all__ = ("GenerationNAV5", "executer_course_na_v5", "chaine_au_registre", "comptes_registre_v4", "lire_replis",
           "ligne_de_generation_v5", "fabriquer_registre_servi_na_v5", "decrire_arret", "ARRETS_CONNUS_V5",
           "ArretCodeChargeCourseNA", "DefautLot6V5", "NOM_JOURNAL_ARRETS", "NOM_BILAN", "VERSION",
           "lire_journal_arrets_generations", "CODE_CHARGE_NON_DEMANDE")
