"""Course 2, version 68 (fichiers neufs, R12 ; rien de la v54 à la v67 n'est touché) — la boucle de la v59 réparée, un étage
après la dernière génération, une garde de budget de la course, et deux régimes séparés.

Défauts de l'orchestrateur a41b7b50 corrigés (rang 0 des épreuves v9, rapport du développeur § 5 ; contre-lecture, constat 9) :

1. **Héritage illisible** : `course2_v59.heritage_depuis_selection` rend du Markdown ; `GenerationV56` le lit par `json.loads`
   (`course2_v54.py`, l. 123) → `JSONDecodeError` à la génération 2. En v68, la sélection scellée est lue (sceau et empreinte
   vérifiés avant lecture, comme la v59 : `boucle_fermee_v59.lire_scelle_verifie`) en un **objet** (`lignes_depuis_selection_v68` :
   identifiant, nom, énoncé des seules retenues), jamais en texte ; `GenerationV68._heritage_garde` passe **chaque ligne** à la
   garde A4 (`fiches_v54.trouver` ; ligne exclue ou arrêt selon `a4.action`, comme la v54) puis rend la section ; `_proposer`
   (copie de la v54, l. 135-166) prend le titre de la section dans un attribut (`TITRE_HERITAGE_SELECTION`) au lieu de
   « titres, résumés, verdict agrégé ». Un héritage texte (classement des juges de la v56, Markdown de la v59) est **refusé**
   (`HeritageNonSelection`) : la v68 ne sert jamais le classement des juges (verdict agrégé).
2. **Aucun étage après la dernière génération** : `etage_apres_derniere=True` joue l'étage après chaque génération, la dernière
   comprise ; la sélection de la dernière est écrite et scellée, jamais servie (`heritage_servi_a_la_suivante: null`).
3. **Budget remis à zéro par génération** : `budget_course_v68.GardeBudgetCourseV68` cumule générations et étages sur la course
   et s'arrête à son plafond (réservation au pire avant chaque poste, coût réel compté après) ; la portée « course » est
   refusée pour plus d'une génération ou un étage (`configuration_v68.montant_requis_v68`).
4. **`heritage_lu` jamais rempli** (précision ii) : la ligne de bilan de la génération g + 1 porte ce qu'elle a lu (empreinte
   de la sélection, génération source, retenues, servies, exclues par A4, section servie ou omise, empreinte du texte servi,
   nombre de consignes qui l'ont reçue).
5. **Sélection vide** (précision iii) : `selection_vide` ∈ {« omettre », « servir_vide »} ; **défaut « omettre »**, ce qui
   minimise ce qui est servi (aucune section : la consigne de la génération g + 1 est alors celle d'une génération sans
   héritage) ; « servir_vide » sert « - (aucune fiche retenue) » comme la v59. À fixer par l'additif (nœud 14 de l'ordre v3).

Régimes (arguments nommés, **aucun défaut** pour les deux interrupteurs) :

| régime | `lecture_selection` | `etage_apres_derniere` | ce qui est servi aux proposeurs |
|---|---|---|---|
| éteint | False | False | rien (aucun héritage) ; étage entre générations s'il est donné, sélection scellée jamais servie |
| tests de mort sans rien servir | False | True | rien ; étage après chaque génération, la dernière comprise (N ≥ 1) |
| lecture de la sélection | True | False ou True | g + 1 : nom et énoncé des retenues de l'étage de g (N ≥ 2, étage exigé) |

La mémoire anti-redite passe d'une génération à l'autre comme en v56 ; elle n'est **jamais servie** aux proposeurs et ne porte
aucun verdict (garde du complément 3 de N-073). Refus avant toute génération et toute écriture : nombre de générations ;
interrupteurs non booléens ; lecture avec une seule génération ou sans étage ; étage après la dernière sans étage ; portée
« course » avec N > 1 ou un étage ; plafond de la course absent, nul ou au-delà du montant requis ; étage sans plafond total
dans ses réglages ou au-delà de `plafond_etage_usd` ; expérimentateur externe sans plafond externe ; `selection_vide` inconnu ;
titre de section vide ou porteur d'une étiquette interdite ; étage sans machine jetable ou à clé manquante (v56) ; sortie
présente (R12).
"""

import hashlib
import json
import os

from . import fiches_v54 as fv
from .boucle_fermee_v59 import HeritageRefuse, lire_scelle_verifie
from .budget_course_v68 import GardeBudgetCourseV68
from .configuration_v53 import ConfigurationRefusee
from .configuration_v68 import montant_requis_v68, nombre_etages_v68
from .course2_v54 import _fiches_ou_none
from .course2_v56 import GenerationV56
from .noyau_v54 import NoeudArret
from .noyau_v56 import ArretSurSignal, motif_arret
from .outils import EcrasementInterdit, ecrire_json_scelle, verifier_scelle

VERSION = "course-2-generation-v68"
TYPE_HERITAGE = "selection-v68 (nom et énoncé des retenues, sceau et empreinte vérifiés)"
TITRE_HERITAGE_SELECTION = "Fiches retenues par l'étage de tests de mort de la génération précédente (nom et énoncé)"
SELECTION_VIDE = ("omettre", "servir_vide")
SELECTION_VIDE_DEFAUT = "omettre"  # ce qui minimise ce qui est servi ; à fixer par l'additif (nœud 14 de l'ordre v3)
LIGNE_SELECTION_VIDE = "- (aucune fiche retenue)"
REGIMES = ("eteint", "tests_de_mort_sans_rien_servir", "lecture_de_la_selection")
CLES_ETAGE = ("adaptateur", "reglages", "nombre", "tranche_index_sha256", "correspondance", "plafond_etage_usd")


class HeritageNonSelection(RuntimeError):
    """Un héritage autre que l'objet de sélection v68 (texte du classement des juges, Markdown de la v59) : refusé."""


def _une_ligne(v):
    return " ".join(v.split())


# --- la sélection lue en objet ----------------------------------------------------------------------------------------------------


def lignes_depuis_selection_v68(dossier_etage, sha256_selection, depuis_generation):
    """L'héritage de la génération suivante, **en objet** : la sélection scellée de l'étage lue après vérification de son
    sceau et de l'empreinte consignée (`lire_scelle_verifie`, comme la v59), les fiches de l'étage (sceau vérifié), les seules
    retenues, par identifiant, nom et énoncé (chacun ramené à une ligne). Lève `SelectionNonVerifiee` ou `HeritageRefuse`."""
    from .etage_entre_generations_v57 import NOM_SELECTION
    from .etage_entre_generations_v57 import VERSION as VERSION_SELECTION
    selection = lire_scelle_verifie(os.path.join(dossier_etage, NOM_SELECTION), sha256_selection, "sélection de l'étage")
    if selection.get("version") != VERSION_SELECTION or not isinstance(selection.get("retenues"), list):
        raise HeritageRefuse("sélection d'une autre version que l'étage entre générations v57 : refus")
    chemin_fiches = os.path.join(dossier_etage, "fiches-validees.json")
    if not verifier_scelle(chemin_fiches):
        raise HeritageRefuse("fiches de l'étage : sceau absent ou faux : refus")
    with open(chemin_fiches, encoding="utf-8") as f:
        fiches = {x["identifiant_auteur"]: x for x in json.load(f)}
    absentes = [i for i in selection["retenues"] if i not in fiches]
    if absentes:
        raise HeritageRefuse(f"retenue(s) absente(s) des fiches de l'étage : {absentes} : refus")
    lignes = []
    for i in selection["retenues"]:
        nom, enonce = fiches[i].get("nom"), fiches[i].get("enonce")
        if not isinstance(nom, str) or not nom.strip() or not isinstance(enonce, str) or not enonce.strip():
            raise HeritageRefuse(f"retenue {i} sans nom ou sans énoncé (chaîne non vide exigée) : refus, aucun champ inventé")
        lignes.append({"identifiant_auteur": i, "nom": _une_ligne(nom), "enonce": _une_ligne(enonce)})
    return {"type": TYPE_HERITAGE, "selection_sha256": sha256_selection, "depuis_generation": depuis_generation, "lignes": lignes}


def verifier_heritage_selection(h):
    if h is None:
        return None
    if not isinstance(h, dict) or h.get("type") != TYPE_HERITAGE or not isinstance(h.get("lignes"), list) \
            or not isinstance(h.get("selection_sha256"), str) or len(h["selection_sha256"]) != 64:
        raise HeritageNonSelection("héritage v68 : objet de sélection (lignes_depuis_selection_v68) exigé ; tout autre héritage "
                                   "est refusé (classement des juges, texte Markdown, JSON libre)")
    for l in h["lignes"]:
        if not isinstance(l, dict) or set(l) != {"identifiant_auteur", "nom", "enonce"} \
                or not all(isinstance(l[k], str) and l[k] for k in l):
            raise HeritageNonSelection("héritage v68 : chaque ligne porte exactement identifiant_auteur, nom et énoncé (chaînes)")
    return h


def rendre_heritage_v68(heritage, interdites, mode, action, *, selection_vide, titre, evenement=None):
    """A4 sur chaque ligne « - nom : énoncé » (ligne exclue ou arrêt selon `action`, comme `GenerationV54._heritage_garde`),
    puis le corps de la section ; rend (corps ou None, état). Corps None : section omise (sélection vide, ou toutes les lignes
    exclues par A4, et `selection_vide` = « omettre »)."""
    if selection_vide not in SELECTION_VIDE:
        raise ConfigurationRefusee(f"selection_vide ∈ {SELECTION_VIDE} exigé (reçu {selection_vide!r})")
    gardees, exclues = [], []
    for l in heritage["lignes"]:
        texte = f"- {l['nom']} : {l['enonce']}"
        trouvees = fv.trouver(texte, interdites, mode)
        if not trouvees:
            gardees.append(texte)
        elif action == "fiche_exclue":
            exclues.append(l["identifiant_auteur"])
            if evenement is not None:
                evenement("incident-a4-heritage-ligne-exclue", etiquettes=trouvees)
        else:
            raise fv.EtiquetteDansEntree("A4 : étiquette interdite dans une ligne de l'héritage de la sélection ("
                                         + ", ".join(trouvees) + ")")
    if gardees:
        corps, section = "\n".join(gardees), "servie"
    elif selection_vide == "servir_vide":
        corps, section = LIGNE_SELECTION_VIDE, "servie vide"
    else:
        corps, section = None, ("omise (sélection vide)" if not heritage["lignes"] else "omise (toutes les lignes exclues par A4)")
    texte_section = None if corps is None else "## " + titre + "\n" + corps + "\n"
    etat = {"type": heritage["type"], "selection_sha256": heritage["selection_sha256"],
            "depuis_generation": heritage.get("depuis_generation"), "retenues": len(heritage["lignes"]), "servies": len(gardees),
            "exclues_a4": exclues, "section": section, "selection_vide": selection_vide, "titre": titre,
            "texte_sha256": None if texte_section is None else hashlib.sha256(texte_section.encode("utf-8")).hexdigest()}
    return corps, etat


# --- la génération --------------------------------------------------------------------------------------------------------------


class GenerationV68(GenerationV56):
    """`GenerationV56` dont l'héritage est l'objet de sélection v68 (ou rien), gardé ligne par ligne, servi sous un titre
    neuf. Tout le reste est la v56."""

    def __init__(self, conf, sortie, adaptateurs, *, heritage_selection=None, selection_vide=SELECTION_VIDE_DEFAUT,
                 titre_heritage=TITRE_HERITAGE_SELECTION, **kw):
        if kw.get("heritage_texte") is not None:
            raise HeritageNonSelection("GenerationV68 : heritage_texte refusé (classement des juges ou texte libre) ; seul "
                                       "heritage_selection (objet de sélection v68) est servi")
        verifier_heritage_selection(heritage_selection)
        if selection_vide not in SELECTION_VIDE:
            raise ConfigurationRefusee(f"selection_vide ∈ {SELECTION_VIDE} exigé (reçu {selection_vide!r})")
        if not isinstance(titre_heritage, str) or not titre_heritage.strip() or "\n" in titre_heritage:
            raise ConfigurationRefusee("titre de la section d'héritage : une ligne non vide exigée")
        kw["heritage_texte"] = None
        super().__init__(conf, sortie, adaptateurs, **kw)
        self.heritage_selection, self.selection_vide, self.titre_heritage = heritage_selection, selection_vide, titre_heritage
        self.heritage_servi_etat, self.consignes_avec_heritage = None, 0

    def _heritage_garde(self):
        if self.heritage_selection is None:
            return None
        corps, etat = rendre_heritage_v68(self.heritage_selection, self.interdites, self.a4_mode, self.a4_action,
                                          selection_vide=self.selection_vide, titre=self.titre_heritage, evenement=self.ev)
        self.heritage_servi_etat = etat
        return corps

    def _proposer(self, etat, passe, supplement_par_case=None):
        nouvelles = []
        heritage = self._heritage_garde() if passe == 1 else None
        etape = "proposition" if passe == 1 else "passe_tableau"
        for ic, case in enumerate(self.conf["cases"]):
            for p in self.conf["proposeurs"]:
                if p["etiquette"] in self.roles_arretes:
                    continue
                consigne = self.piece(p["consigne"] if passe == 1 else self.conf["tableau"]["consigne_passe"])
                consigne = consigne.rstrip() + f"\n\n## Case\nTexte : {case[0]} ; bras : {case[1]}\n"
                if heritage:
                    consigne += "\n## " + self.titre_heritage + "\n" + heritage + "\n"
                    self.consignes_avec_heritage += 1
                if supplement_par_case is not None:
                    consigne += "\n## Tableau minimal de ta case (titres et résumés seulement)\n```json\n" + supplement_par_case[ic] + "\n```\n"
                a = self.appel(etat, role=p["etiquette"], role_kit="proposeur_ideation", fournisseur=p["fournisseur"],
                               modele=p["modele"], consigne=consigne, plafond_role="proposeur",
                               session=(etape, ic, p["etiquette"]), lire=lambda t: _fiches_ou_none(t))
                if a is None or a["lu"] is None:
                    continue
                for k, b in enumerate(a["lu"]):
                    ident = "f" + self.graines.jeton_opaque(self.tache("ident", passe, ic, p["etiquette"], k), 6)
                    try:
                        f = fv.preparer(b, self.conf["champs_fiche"], ident=ident, case=case, fournisseur=p["fournisseur"], passe=passe)
                    except fv.FicheRefusee as e:
                        self.ev("fiche-refusee", proposeur=p["etiquette"], passe=passe, case=ic, motif=str(e)[:200])
                        continue
                    f["meta"]["proposeur"] = p["etiquette"]
                    self.fiches[ident] = f
                    self.ordre.append(ident)
                    nouvelles.append(f)
        return nouvelles

    def heritage_lu(self):
        if self.heritage_servi_etat is None:
            return None
        return dict(self.heritage_servi_etat, consignes_avec_section=self.consignes_avec_heritage)


# --- le régime ------------------------------------------------------------------------------------------------------------------


def _reel_positif(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and float(v) > 0


def verifier_regime_v68(conf, *, nombre_generations, lecture_selection, etage_present, etage_apres_derniere,
                        selection_vide=SELECTION_VIDE_DEFAUT, titre_heritage=TITRE_HERITAGE_SELECTION, plafond_etage_usd=None):
    """Le régime et le montant requis, ou un refus (`ConfigurationRefusee`) — sans aucune écriture ni aucun appel."""
    if isinstance(nombre_generations, bool) or not isinstance(nombre_generations, int) or nombre_generations < 1:
        raise ConfigurationRefusee("nombre de générations : entier ≥ 1, aucun défaut")
    if not isinstance(lecture_selection, bool) or not isinstance(etage_apres_derniere, bool):
        raise ConfigurationRefusee("interrupteurs lecture_selection et etage_apres_derniere : booléens exigés, aucun défaut")
    if lecture_selection and not etage_present:
        raise ConfigurationRefusee("lecture de la sélection sans étage de tests de mort : aucune sélection à lire (refus, aucun "
                                   "héritage du classement des juges)")
    if lecture_selection and nombre_generations < 2:
        raise ConfigurationRefusee("lecture de la sélection avec une seule génération : aucune génération pour la lire (refus)")
    if etage_apres_derniere and not etage_present:
        raise ConfigurationRefusee("étage après la dernière génération demandé sans étage de tests de mort : refus")
    if selection_vide not in SELECTION_VIDE:
        raise ConfigurationRefusee(f"selection_vide ∈ {SELECTION_VIDE} exigé (reçu {selection_vide!r})")
    if not isinstance(titre_heritage, str) or not titre_heritage.strip() or "\n" in titre_heritage:
        raise ConfigurationRefusee("titre de la section d'héritage : une ligne non vide exigée")
    trouvees = fv.trouver(titre_heritage, conf.get("etiquettes_interdites") or [], (conf.get("a4") or {}).get("mode", "prefixe"))
    if trouvees:
        raise ConfigurationRefusee("titre de la section d'héritage porteur d'une étiquette interdite (A4) : " + ", ".join(trouvees))
    nombre_etages = nombre_etages_v68(nombre_generations, etage_present, etage_apres_derniere)
    montant = montant_requis_v68(conf, nombre_generations, plafond_etage_usd, nombre_etages=nombre_etages)
    nom = ("lecture_de_la_selection" if lecture_selection else
           "tests_de_mort_sans_rien_servir" if etage_apres_derniere else "eteint")
    return {"nom": nom, "lecture_selection": lecture_selection, "etage_apres_derniere": etage_apres_derniere,
            "etage": etage_present, "nombre_generations": nombre_generations, "nombre_etages": nombre_etages,
            "selection_vide": selection_vide if lecture_selection else None,
            "titre_heritage": titre_heritage if lecture_selection else None, "montant_requis_usd": montant,
            "servi_aux_proposeurs": ("nom et énoncé des retenues de l'étage de la génération précédente" if lecture_selection
                                     else "rien (aucun héritage)"),
            "memoire": "anti-redite seulement, jamais servie aux proposeurs, aucun verdict (complément 3 de N-073)"}


def verifier_etage_v68(etage):
    """Clés de l'étage (v56) et plafond tenu par l'étage lui-même : `reglages.plafond_total_usd` présent et ≤
    `plafond_etage_usd` ; un expérimentateur externe exige `plafond_externe_usd`, la somme sous `plafond_etage_usd`."""
    for c in CLES_ETAGE:
        if c not in etage:
            raise ConfigurationRefusee(f"étage entre générations : {c} manquant (aucun défaut)")
    plafond = etage["plafond_etage_usd"]
    if not _reel_positif(plafond):
        raise ConfigurationRefusee("étage : plafond_etage_usd réel > 0 exigé")
    r = etage["reglages"] if isinstance(etage["reglages"], dict) else {}
    total = r.get("plafond_total_usd")
    if not _reel_positif(total) or float(total) > float(plafond) + 1e-9:
        raise ConfigurationRefusee("étage : reglages.plafond_total_usd exigé, réel > 0 et ≤ plafond_etage_usd (l'étage doit tenir "
                                   "lui-même ce que la course lui réserve)")
    if r.get("experimentateur_externe") is not None:
        ext = r.get("plafond_externe_usd")
        if not _reel_positif(ext) or float(total) + float(ext) > float(plafond) + 1e-9:
            raise ConfigurationRefusee("étage : expérimentateur externe sans plafond_externe_usd, ou plafond total + externe au-delà "
                                       "de plafond_etage_usd : refus")
    return True


def _cout_etage(resume):
    c = resume.get("couts") if isinstance(resume, dict) else None
    try:
        return float(c["claude_usd"]) + float(c["externe_usd"]), False
    except (TypeError, KeyError, ValueError):
        return None, True


# --- la course ------------------------------------------------------------------------------------------------------------------


def executer_course_v68(conf, sortie, adaptateurs, *, nombre_generations, go, lecture_selection, etage_apres_derniere,
                        plafond_course_usd, etage=None, environnement=None, horloge=None, racine_sessions=None, portes=None,
                        specification=None, selection_vide=SELECTION_VIDE_DEFAUT, titre_heritage=TITRE_HERITAGE_SELECTION):
    """La course v68 : générations `GenerationV68`, étage v57 (machine jetable v56, étage v5, sélection scellée), garde de
    budget de la course ; les régimes du tableau de l'en-tête. Rend le bilan (une ligne par génération)."""
    from .etage_entre_generations_v53 import preparer_generation
    from .etage_entre_generations_v56 import exiger_machine_jetable_v56
    from .etage_entre_generations_v57 import jouer_etage_v57
    regime = verifier_regime_v68(conf, nombre_generations=nombre_generations, lecture_selection=lecture_selection,
                                 etage_present=etage is not None, etage_apres_derniere=etage_apres_derniere,
                                 selection_vide=selection_vide, titre_heritage=titre_heritage,
                                 plafond_etage_usd=(etage or {}).get("plafond_etage_usd"))
    if not _reel_positif(plafond_course_usd) or float(plafond_course_usd) > regime["montant_requis_usd"] + 1e-9:
        raise ConfigurationRefusee(f"plafond de la course : réel > 0 et ≤ montant requis ({regime['montant_requis_usd']:g} USD) "
                                   f"exigé (reçu {plafond_course_usd!r}), aucun défaut")
    permis = (conf.get("etage_tests_de_mort") or {}).get("environnement_permis") or ()
    if etage is not None:
        verifier_etage_v68(etage)
        exiger_machine_jetable_v56(environnement, permis_en_plus=permis)
    if os.path.exists(sortie):
        raise EcrasementInterdit(f"sortie {sortie} déjà présente (R12)")
    os.makedirs(sortie)
    s17 = float(conf["budget"]["plafond_usd"])
    budget = GardeBudgetCourseV68(plafond_course_usd)
    regime = dict(regime, plafond_course_usd=float(plafond_course_usd))
    memoire, heritage, bilan, noeud, arret = None, None, [], None, None
    with ArretSurSignal() as garde:
        try:
            for g in range(1, nombre_generations + 1):
                poste = f"generation-{g}"
                budget.reserver(poste, s17)
                rs = None if racine_sessions is None else os.path.join(racine_sessions, f"generation-{g}")
                gen = None
                try:
                    gen = GenerationV68(conf, os.path.join(sortie, f"generation-{g}"), adaptateurs, numero=g, memoire=memoire,
                                        heritage_selection=heritage, selection_vide=selection_vide, titre_heritage=titre_heritage,
                                        go=go, horloge=horloge, racine_sessions=rs, portes=portes, specification=specification)
                    resultat = gen.executer()
                except BaseException:
                    budget.noter_arret(poste, gen.budget.cumul if gen is not None else 0.0)
                    raise
                ligne = {"generation": g, "fiches_classees": len(resultat), "notables": sum(l["notable"] for l in resultat),
                         "c13_satisfaite": gen.budget.etat()["c13_satisfaite"], "noeud": gen.noeud,
                         "cout_generation_usd": round(gen.budget.cumul, 6), "heritage_lu": gen.heritage_lu()}
                bilan.append(ligne)
                budget.compter(poste, gen.budget.cumul)
                if gen.noeud:
                    noeud = f"génération {g} : {gen.noeud}"
                    break
                memoire, heritage = gen.memoire, None
                if etage is not None and (g < nombre_generations or etage_apres_derniere):
                    poste = f"etage-apres-generation-{g}"
                    budget.reserver(poste, float(etage["plafond_etage_usd"]))
                    try:
                        d = preparer_generation(os.path.join(sortie, poste), resultat, gen.fiches, nombre=etage["nombre"],
                                                tranche_index_sha256=etage["tranche_index_sha256"],
                                                correspondance=etage["correspondance"], lisible=gen.arret is None)
                        resume = jouer_etage_v57(etage["adaptateur"], d, reglages=etage["reglages"], environnement=environnement,
                                                 executer=etage.get("executer"), permis_en_plus=permis)
                    except BaseException:
                        budget.noter_arret(poste, None)
                        raise
                    ligne["etage"] = resume
                    cout, inconnu = _cout_etage(resume)
                    ligne["cout_etage_usd"] = None if inconnu else round(cout, 6)
                    sha = resume["selection"]["sha256"]
                    servie = lecture_selection and g < nombre_generations
                    ligne["selection"] = {"sha256": sha, "retenues": len(resume["selection"]["retenues"]),
                                          "servie_a_la_suivante": servie}
                    budget.compter(poste, cout, inconnu=inconnu)
                    if servie:  # la génération g + 1 lit la sélection scellée (vérifiée), en objet
                        heritage = lignes_depuis_selection_v68(d, sha, g)
                        ligne["heritage_servi_a_la_suivante"] = {"selection_sha256": sha,
                                                                  "retenues": resume["selection"]["retenues"]}
                    else:
                        ligne["heritage_servi_a_la_suivante"] = None
        except BaseException as e:
            arret = motif_arret(e)
            raise
        finally:
            garde.nettoyage()
            ecrire_json_scelle(os.path.join(sortie, "bilan-course.json"), {
                "version": VERSION, "go": go, "regime": regime, "generations": bilan, "noeud": noeud, "arret": arret,
                "signaux": garde.etat(), "budget_course": budget.etat()})
    if noeud:
        raise NoeudArret(noeud)
    return bilan


__all__ = ("executer_course_v68", "GenerationV68", "lignes_depuis_selection_v68", "rendre_heritage_v68", "verifier_regime_v68",
           "verifier_etage_v68", "verifier_heritage_selection", "HeritageNonSelection", "TITRE_HERITAGE_SELECTION",
           "SELECTION_VIDE", "SELECTION_VIDE_DEFAUT", "LIGNE_SELECTION_VIDE", "REGIMES", "TYPE_HERITAGE", "VERSION")
