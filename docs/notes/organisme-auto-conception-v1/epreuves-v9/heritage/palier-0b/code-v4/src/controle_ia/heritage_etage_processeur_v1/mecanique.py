"""B2 — la couche mécanique : les objets réels (mondes en fichiers, part servie et tranche d'épreuve, registre chaîné par
empreintes, engagements scellés, exécuteur simulé, comparateur sans juge, compteur de coût, règle de retrait, gardes).

Elle porte C6, les fréquences M12 (par loi engagée et par monde, par type — loi vraie du monde source, loi vraie d'un monde
cible, loi fausse, loi non plantée par origine — ; criblage par composition et par monde) et les moyennes de la garde
d'équivalence S8. `jouer_source` joue une source entière : course source (trois générations du monde source, registre né vide
servi et payé comme au bras 2, aucune entrée héritée), puis chaque bras demandé sur trois mondes cibles et le monde final.
"""

import os
import shutil

import numpy as np

from .comparateur import apparier, loi_du_texte
from .constantes import (APPELS_PAR_GENERATION, CLASSES, DESCRIPTION_FIXE, DOSE_JEU_GARDE_27, GENERATIONS_COURSE_SOURCE,
                         JUSTIFICATION_FIXE, MONDES_CIBLES_D_EVOLUTION, PREDICTION_FIXE, REPERE_LECTURE, TIENT, VERSION)
from .cout import cout_hors_budget, cout_lecture_par_appel, nombre_de_tentatives, retrait_v1, retrait_v2, verifier_retrait
from .enveloppe import cartes_d_un_lot, eprouver_generation, exiger_taux_egaux, lots_par_domaine
from .executeur import Executeur, engagement, sceller
from .graines import etiquette, verifier_graines_des_bras
from .lois import json_canonique
from .mondes import BORNES_GELEES, ecrire_monde, ensemble_exclu, generer_suite, lire_csv, verifier_tranche_jamais_servie
from .organisme import DesaccordOrganisme, comparer_verdicts
from .proposeurs import PartsServies, proposer
from .registre import (Registre, empreinte_vue, exiger_historique_vide, nouvelle_entree, provenance, verifier_bras_1_non_servi,
                       verifier_cloisonnement, verifier_finale_sans_ecriture, verifier_registre_etranger,
                       verifier_vue_etrangere_4b)

ORIGINES_NON_PLANTEES = ("base", "composition", "copie")
STRATES = ("vraie-source", "vraie-cible", "fausse") + tuple("non-plantee-" + o for o in ORIGINES_NON_PLANTEES)


class ArretMecanique(RuntimeError):
    pass


class Frequences:
    """Comptes de la couche mécanique pour M12 : par (monde, loi) engagée — strate, classe sans échec, dépendante ; par
    (monde, composition) criblée — dépendante du monde ou non, retenue sur son domaine, passage ; par tentative, la classe
    rendue (échecs de l'expérimentateur compris)."""

    def __init__(self):
        self.par_loi = {}
        self.criblage = {}
        self.tentatives = {c: 0 for c in CLASSES}

    def noter_loi(self, cle, strate, classe, dependante):
        if cle not in self.par_loi:
            self.par_loi[cle] = (strate, classe, bool(dependante))

    def comptes(self):
        out = {s: {"engagees": 0, "tiennent": 0} for s in STRATES}
        out["non-plantee"] = {"engagees": 0, "tiennent": 0}
        out["vraie-dependante"] = {"engagees": 0, "tiennent": 0}
        out["vraie-independante"] = {"engagees": 0, "tiennent": 0}
        for strate, classe, dep in self.par_loi.values():
            for s in (strate,) + (("non-plantee",) if strate.startswith("non-plantee") else ()) + (
                    (("vraie-dependante" if dep else "vraie-independante"),) if strate.startswith("vraie") else ()):
                out[s]["engagees"] += 1
                out[s]["tiennent"] += classe == TIENT
        vraies = [v for v in self.criblage.values() if v[0]]
        autres = [v for v in self.criblage.values() if not v[0]]
        out["criblage"] = {"vraies_examinees": len(vraies), "vraies_retenues": sum(v[1] for v in vraies),
                           "autres_examinees": len(autres), "autres_passees": sum(v[2] for v in autres)}
        out["tentatives_par_classe"] = dict(self.tentatives)
        return out

    def fusionner(self, autre):
        for k, v in autre.par_loi.items():
            self.par_loi.setdefault(k, v)
        for k, v in autre.criblage.items():
            self.criblage.setdefault(k, v)
        for c in CLASSES:
            self.tentatives[c] += autre.tentatives[c]


VUE_PAR_BRAS = {"1": "aucune", "2": "entiere", "3": "entiere", "4a": "entiere", "4b": "entiere"}


class ContexteSource:
    def __init__(self, graines, base, prop, dose, taux_echec, dossier, executeur=None, repere=REPERE_LECTURE,
                 regle_retrait="v2", liste="avec_description", repli=False, faute=None, bornes=BORNES_GELEES, organisme=None):
        if "source" not in base:
            raise ArretMecanique("le contexte d'une source porte son numéro (champ « source » de l'étiquette)")
        self.graines, self.base, self.prop, self.dose, self.taux = graines, dict(base), prop, dose, taux_echec
        self.dossier, self.executeur = dossier, executeur or Executeur()
        self.repere, self.regle, self.liste, self.repli, self.faute = repere, regle_retrait, liste, repli, faute
        self.bornes, self.organisme = bornes, organisme
        self.source = base["source"]
        self.libelle = etiquette(**self.base)
        self.configuration_sha = __import__("hashlib").sha256(json_canonique(
            {"base": self.base, "prop": prop, "dose": dose, "taux": taux_echec, "repere": repere, "regle": regle_retrait,
             "liste": liste, "repli": repli, "version": VERSION}).encode("utf-8")).hexdigest()
        self.cout_hors_budget = 0.0
        self.etiquettes_employees = {}
        self.desaccords_organisme = []
        self.tentatives_vues_par_l_organisme = 0

    def g(self, **champs):
        return self.graines.g(**self.base, **champs)

    def etiquette(self, **champs):
        return etiquette(**self.base, **champs)


def parts_servies_depuis_fichiers(dossier_monde, monde):
    """La part servie lue sur disque (ce que reçoit le proposeur) ; garde 10 vérifiée contre la tranche d'épreuve."""
    parts = {}
    for d in monde.domaines:
        servi = lire_csv(os.path.join(dossier_monde, "servi", d["nom"] + ".csv"))
        epreuve = lire_csv(os.path.join(dossier_monde, "epreuve", d["nom"], "episodes.csv"))
        verifier_tranche_jamais_servie(servi, epreuve)
        champs = [l.split(",") for l in servi]
        parts[d["nom"]] = {"Z": np.array([[float(c[1]), float(c[2])] for c in champs]),
                           "G": np.array([int(c[3]) for c in champs]), "y": np.array([int(c[4]) for c in champs])}
    return parts


def _appels(ctx, bras, generation, n_servi, paie):
    lecture = float(cout_lecture_par_appel(n_servi, ctx.repere)) if (paie and n_servi) else 0.0
    if ctx.regle == "v1":
        return int(retrait_v1(lecture)[0].sum()), 0.0
    perm = ctx.g(bras=bras, generation=generation, role="retrait").permutation(APPELS_PAR_GENERATION)
    gardes, retires, reliquat = retrait_v2(perm, np.full(APPELS_PAR_GENERATION, lecture))
    verifier_retrait(perm, gardes, retires, np.full(APPELS_PAR_GENERATION, lecture))
    return len(gardes), reliquat


def _strate(monde, ident, origine):
    if ident is None:
        return "non-plantee-" + origine
    l = monde.lois[ident]
    if l["type"] == "fausse":
        return "fausse"
    return "vraie-source" if monde.role == "source" else "vraie-cible"


def _organisme(ctx, dossier, monde, dossier_monde, bras, generation, entrees, sorties, echecs):
    """Garde 17 : les tentatives de la génération passées à l'étage de l'organisme, lot par lot (un domaine par lot) ; les
    tentatives dont l'expérimentateur simulé a échoué y sont jouées avec la doublure « rien envoyé »."""
    for k, (dom, lot) in enumerate(lots_par_domaine(entrees)):
        for echoue in (False, True):
            sel = [i for i in lot if bool(echecs[i]) == echoue and sorties[i][0]["classe"] in CLASSES]
            if not sel:
                continue
            cartes, _ = cartes_d_un_lot(entrees, sel, ctx.liste)
            lois = {c["identifiant"]: loi_du_texte(entrees[i]["tentative"]["engagement"]["test_de_mort"]["test"])
                    for c, i in zip(cartes, sel)}
            with open(os.path.join(dossier_monde, "epreuve", dom, "episodes.csv"), encoding="utf-8") as f:
                lignes = f.read()
            verdicts = ctx.organisme.eprouver_lot(os.path.join(dossier, f"organisme-{bras}-g{generation}-lot{k}-{int(echoue)}"),
                                                  cartes, lois, lignes, "rien_envoye" if echoue else None)
            simules = {c["identifiant"]: sorties[i][0]["classe"] for c, i in zip(cartes, sel)}
            d = comparer_verdicts(simules, verdicts)
            ctx.tentatives_vues_par_l_organisme += len(sel)
            if d:
                ctx.desaccords_organisme.extend(d)
                raise DesaccordOrganisme(f"garde 17 : exécuteur simulé et étage de l'organisme en désaccord : {d[:3]} : arrêt")


def _jouer_generation(ctx, registre, monde, dossier_monde, bras, generation, vue, finale, freqs, dossier_bras):
    """Une génération d'un bras (ou de la course source, bras « source »). Rend la liste des (entrée, résultat, appariement) et
    le reliquat."""
    n_servi = len(vue) if vue else 0
    verifier_bras_1_non_servi(bras, vue)
    appels, reliquat = _appels(ctx, bras, generation, n_servi, ctx.prop["paie"])
    etiq = ctx.etiquette(bras=bras, generation=generation, role="echantillonnage")
    ctx.etiquettes_employees.setdefault(bras, []).append(etiq)  # garde 20 : les étiquettes réellement employées
    rng = ctx.graines.generateur(etiq)
    n_tent = int(nombre_de_tentatives(np.array([appels]), rng)[0])
    parts = PartsServies(parts_servies_depuis_fichiers(dossier_monde, monde))
    mesure = []
    tentatives = proposer(ctx.prop, vue, monde, parts, n_tent, rng, ctx.source, bras, repli=ctx.repli, mesure=mesure)
    for t, vraie, retenue, passe in mesure:
        freqs.criblage.setdefault((ctx.libelle, monde.nom, t), (vraie, retenue, passe))
    entrees = []
    for dom, loi, _origine in tentatives:
        eng = engagement(dom, loi)
        entrees.append(nouvelle_entree(dom, eng, sceller(eng), DESCRIPTION_FIXE, JUSTIFICATION_FIXE, PREDICTION_FIXE))
    sorties, _, echecs = eprouver_generation(entrees, monde.tranche_epreuve, ctx.executeur,
                                             ctx.g(bras=bras, generation=generation, role="echec"), ctx.taux, 2 * appels,
                                             ctx.g(bras=bras, generation=generation, role="budget"), ctx.liste)
    if finale:
        ctx.cout_hors_budget += cout_hors_budget(sum(1 for s in sorties if s[0]["classe"] in CLASSES))
    if ctx.organisme is not None:
        _organisme(ctx, dossier_bras, monde, dossier_monde, bras, generation, entrees, sorties, echecs)
    rendu = []
    for e, (resultat, gardee), (_, _, origine) in zip(entrees, sorties, tentatives):
        eng = e["tentative"]["engagement"]
        ident, _ = apparier(eng, e["tentative"]["engagement_sha256"], eng["domaine"], monde.lois_du_domaine(eng["domaine"]),
                            monde.oracle)
        loi = loi_du_texte(eng["test_de_mort"]["test"])
        dep = ident is not None and monde.lois[ident]["dependante"]
        freqs.noter_loi((ctx.libelle, monde.nom, json_canonique(loi)), _strate(monde, ident, origine),
                        ctx.executeur.classe_sans_echec(loi, monde.tranche_epreuve(eng["domaine"])), dep)
        if resultat["classe"] in freqs.tentatives:
            freqs.tentatives[resultat["classe"]] += 1
        rendu.append((e, resultat, ident))
        if not finale:
            registre.ajouter(dict(e, resultat=resultat, gardee=gardee,
                                  provenance=provenance("course-source" if bras == "source" else "continuation", generation,
                                                        VERSION, ctx.configuration_sha, ctx.source, bras)))
    if not finale:
        registre.sceller_generation(f"generation-{generation}")
        registre.verifier_chaine()
    return rendu, reliquat


def mesure_finale(rendu, monde, exclu):
    """M1 (lois vraies plantées distinctes appariées, ensemble exclu retiré), D, I, lois fausses tenues (distinctes, au moins une
    tentative classée « tient » au test de mort du monde final), et, rapportés sans seuil, lois fausses engagées et lois vraies
    engagées et tenues."""
    vraies, fausses_tenues, fausses_engagees, vraies_tenues, exclues = set(), set(), set(), set(), set()
    for e, resultat, ident in rendu:
        if ident is not None and ident in exclu:
            exclues.add(ident)
        if ident is None or ident in exclu:
            continue
        if monde.lois[ident]["type"] == "vraie":
            vraies.add(ident)
            if resultat["classe"] == TIENT:
                vraies_tenues.add(ident)
        else:
            fausses_engagees.add(ident)
            if resultat["classe"] == TIENT:
                fausses_tenues.add(ident)
    d = sum(1 for i in vraies if monde.lois[i]["dependante"])
    return {"M1": len(vraies), "D": d, "I": len(vraies) - d, "fausses_tenues": len(fausses_tenues),
            "fausses_engagees": len(fausses_engagees), "vraies_tenues": len(vraies_tenues),
            "appariees": sorted(vraies), "exclues_appariees": sorted(exclues)}


def copie_scellee_4b(sortie_etrangere):
    """La copie que l'orchestrateur dépose au bras 4b (garde 27 ; code v3, C2) : la source étrangère, la liste, par
    génération, des vues du registre que tenait son bras 2 au début de cette génération, et l'empreinte canonique de chacune,
    prise au moment où le bras 2 l'a reçue (`empreintes_vues_bras_2` de la sortie de la source étrangère)."""
    vues, empreintes = sortie_etrangere["vues_bras_2"], sortie_etrangere["empreintes_vues_bras_2"]
    if len(vues) != MONDES_CIBLES_D_EVOLUTION + 1 or len(empreintes) != len(vues):
        raise ArretMecanique("garde 27 : copie du bras 2 de la source étrangère incomplète (bras 2 non joué ?) : arrêt")
    return {"source": sortie_etrangere["source"], "vues": [list(v) for v in vues], "empreintes": list(empreintes)}


def jouer_source(ctx, bras=("1", "2", "3"), suite=None, registre_etranger=None, copie_etrangere_4b=None,
                 historique_de_depart=None):
    """Joue une source. Rend {"suite", "registre_source", "bras": {bras: {mesure, reliquats, entrees_servies, registre}},
    "frequences", "exclu", "vues_bras_2", "empreintes_vues_bras_2", "source"}. `registre_etranger` (bras 4a : le registre de la
    course de la source étrangère) et `copie_etrangere_4b` (bras 4b : `copie_scellee_4b` de la sortie de la source étrangère —
    la liste, par génération, du registre que tient le bras 2 de la source étrangère au début de cette génération, avec
    l'empreinte de chaque vue) sont des copies scellées déposées par l'orchestrateur (garde 27). Au bras 4b, chaque vue est
    contrôlée avant d'être servie (`registre.verifier_vue_etrangere_4b`)."""
    exiger_historique_vide(historique_de_depart)
    exiger_taux_egaux({b: ctx.taux for b in bras})
    os.makedirs(ctx.dossier)
    if suite is None:
        suite = generer_suite(ctx.graines, ctx.base, ctx.dose, ctx.bornes, faute=ctx.faute)
    dossiers = {}
    for m in [suite.source] + suite.mondes_cibles():
        dossiers[m.nom] = os.path.join(ctx.dossier, "mondes", m.nom)
        ecrire_monde(dossiers[m.nom], m)
    freqs = Frequences()
    d_src = os.path.join(ctx.dossier, "course-source")
    os.makedirs(d_src)
    rs = Registre(os.path.join(d_src, "registre.jsonl"))
    for gen in range(1, GENERATIONS_COURSE_SOURCE + 1):
        vue = rs.vue("sans_resultat_ni_gardee" if ctx.repli else "entiere")
        _jouer_generation(ctx, rs, suite.source, dossiers[suite.source.nom], "source", gen, vue, False, freqs, d_src)
    lois_source = [loi_du_texte(e["tentative"]["engagement"]["test_de_mort"]["test"]) for e in rs.entrees]
    exclu = ensemble_exclu(suite.finale, lois_source)
    sha_source = rs.empreinte_fichier()
    sha_etranger = registre_etranger.empreinte_fichier() if registre_etranger is not None else None
    etiquettes = {}
    sortie = {"suite": suite, "registre_source": rs, "bras": {}, "frequences": freqs, "exclu": exclu, "vues_bras_2": [],
              "empreintes_vues_bras_2": [], "sha_registre_source": sha_source, "source": ctx.source}
    dossiers_bras = {b: os.path.join(ctx.dossier, f"bras-{b}") for b in bras}
    for b in bras:
        d = dossiers_bras[b]
        os.makedirs(d)
        if b in ("3", "4a"):
            src = rs if b == "3" else registre_etranger
            if src is None:
                raise ArretMecanique("garde 27 : bras 4a sans registre étranger déposé")
            shutil.copyfile(src.chemin, os.path.join(d, "registre.jsonl"))
            r = Registre(os.path.join(d, "registre.jsonl"), entrees=src.entrees)
            sha_depart = r.empreinte_fichier()
        else:
            r = Registre(os.path.join(d, "registre.jsonl"))
            sha_depart = None
        verifier_registre_etranger(b, sha_depart, sha_etranger, sha_source)
        r.verifier_chaine()
        reliquats, tailles = [], []
        for gen, monde in enumerate(suite.mondes_cibles(), 1):
            finale = gen == MONDES_CIBLES_D_EVOLUTION + 1
            mode = "sans_resultat_ni_gardee" if (ctx.repli and b != "1") else VUE_PAR_BRAS[b]
            if b == "4b":
                if copie_etrangere_4b is None:
                    raise ArretMecanique("garde 27 : bras 4b sans registre étranger déposé")
                vue = copie_etrangere_4b["vues"][gen - 1]
                verifier_vue_etrangere_4b(vue, copie_etrangere_4b["empreintes"][gen - 1], ctx.source,
                                          copie_etrangere_4b["source"])
                if ctx.repli:
                    vue = [{k: v for k, v in e.items() if k not in ("resultat", "gardee")} for e in vue]
            else:
                vue = r.vue(mode)
            if b == "2":
                sortie["vues_bras_2"].append(r.vue("entiere"))
                sortie["empreintes_vues_bras_2"].append(empreinte_vue(sortie["vues_bras_2"][-1]))
            verifier_cloisonnement(d, vue, [dossiers_bras[x] for x in bras if x != b] + [d_src])
            avant = r.octets()
            if finale:
                r.fermer()
            rendu, reliquat = _jouer_generation(ctx, r, monde, dossiers[monde.nom], b, gen, vue, finale, freqs, d)
            reliquats.append(reliquat)
            tailles.append(len(vue) if vue else 0)
            if finale:
                verifier_finale_sans_ecriture(avant, r)
                sortie["bras"][b] = {"mesure": mesure_finale(rendu, monde, set(exclu)), "reliquats": reliquats,
                                     "entrees_servies": tailles, "registre": r}
        etiquettes[b] = {"monde": [m.nom for m in suite.mondes_cibles()],
                         "echantillonnage": list(ctx.etiquettes_employees.get(b, []))}
    verifier_graines_des_bras(etiquettes)
    return sortie


def jouer_jeu_diagnostic(graines, bases, prop, dose, taux, dossier, suites, **kw):
    """B7 bis, garde 27 : un jeu de sources à sources étrangères (`mondes.generer_jeu_avec_etrangeres`) ; chaque source joue
    d'abord ses bras 1, 2, 3 (pour que son registre de course source et les vues de son bras 2 existent), puis les bras 4a et 4b
    reçoivent les copies scellées de la source suivante. Rend la liste des sorties par source. Code v4 (version 7, annexe H,
    écart 1) : ce jeu ne se joue qu'à la dose 0,25 (`DOSE_JEU_GARDE_27`) ; toute autre dose arrête avant de jouer."""
    if float(dose) != DOSE_JEU_GARDE_27:
        raise ArretMecanique(f"garde 27 : le jeu de sources à sources étrangères ne se joue qu'à la dose {DOSE_JEU_GARDE_27} "
                             f"(reçu {dose!r}) : arrêt (B7 bis, version 7)")
    S = len(bases)
    premieres = []
    for k in range(S):
        ctx = ContexteSource(graines, bases[k], prop, dose, taux, os.path.join(dossier, f"source-{k}"), **kw)
        premieres.append(jouer_source(ctx, ("1", "2", "3"), suite=suites[k]))
    secondes = []
    for k in range(S):
        e = premieres[(k + 1) % S]
        ctx = ContexteSource(graines, bases[k], prop, dose, taux, os.path.join(dossier, f"source-{k}-diagnostic"), **kw)
        secondes.append(jouer_source(ctx, ("4a", "4b"), suite=suites[k], registre_etranger=e["registre_source"],
                                     copie_etrangere_4b=copie_scellee_4b(e)))
    return premieres, secondes
