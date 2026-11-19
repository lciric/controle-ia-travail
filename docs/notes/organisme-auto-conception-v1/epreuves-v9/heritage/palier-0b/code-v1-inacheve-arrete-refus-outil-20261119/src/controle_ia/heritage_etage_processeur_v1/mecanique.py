"""B2 — la couche mécanique : les objets réels (mondes en fichiers, part servie et tranche d'épreuve, registre chaîné par
empreintes, engagements scellés, exécuteur simulé, comparateur sans juge, compteur de coût, règle de retrait, gardes).

Elle porte C6, les fréquences M12 (par loi engagée et par monde, par type ; criblage par composition et par monde) et les
moyennes de la garde d'équivalence S8. `jouer_source` joue une source entière : course source (trois générations du monde
source, registre né vide servi et payé comme au bras 2), puis chaque bras demandé sur trois mondes cibles et le monde final.
"""

import json
import os
import shutil

import numpy as np

from .comparateur import apparier, loi_du_texte
from .constantes import (APPELS_PAR_GENERATION, CLASSES, COUT_EPREUVE_USD, GENERATIONS_COURSE_SOURCE, JUSTIFICATION_FIXE,
                         MONDES_CIBLES_D_EVOLUTION, NE_TIENT_PAS, PREDICTION_FIXE, REPERE_LECTURE, TIENT, VERSION)
from .cout import (BUDGET_GENERATION, cout_lecture_par_appel, nombre_de_tentatives, retrait_v1, retrait_v2, verifier_retrait)
from .enveloppe import eprouver_generation, exiger_taux_egaux
from .executeur import Executeur, engagement, sceller
from .graines import etiquette, verifier_graines_des_bras
from .lois import json_canonique
from .mondes import ecrire_monde, ensemble_exclu, generer_suite, lire_csv, verifier_tranche_jamais_servie
from .proposeurs import DESCRIPTION_FIXE, proposer
from .registre import (Registre, exiger_historique_vide, nouvelle_entree, provenance, verifier_bras_1_non_servi,
                       verifier_finale_sans_ecriture)

ORIGINES_NON_PLANTEES = ("base", "composition", "copie")
VUE_PAR_BRAS = {"1": "aucune", "2": "entiere", "3": "entiere", "4a": "entiere", "4b": "entiere"}


class Frequences:
    """Comptes de la couche mécanique pour M12 : par (loi, monde) engagée — type et classe sans échec ; par (composition, monde)
    criblée — dépendante ou non, passage."""

    def __init__(self):
        self.par_loi = {}  # (monde, texte) -> (type, classe, origine de la première tentative qui l'engage)
        self.criblage = {}  # (monde, texte) -> (vraie, passe_sur_son_domaine, passe)
        self.tentatives = {c: 0 for c in CLASSES}

    def comptes(self):
        out = {t: {"engagees": 0, "tiennent": 0} for t in ("vraie", "fausse", "non-plantee")}
        for o in ORIGINES_NON_PLANTEES:
            out["non-plantee-" + o] = {"engagees": 0, "tiennent": 0}
        for typ, classe, origine in self.par_loi.values():
            out[typ]["engagees"] += 1
            out[typ]["tiennent"] += classe == TIENT
            if typ == "non-plantee":
                out["non-plantee-" + origine]["engagees"] += 1
                out["non-plantee-" + origine]["tiennent"] += classe == TIENT
        vraies = [v for v in self.criblage.values() if v[0]]
        autres = [v for v in self.criblage.values() if not v[0]]
        out["criblage"] = {"vraies_examinees": len(vraies), "vraies_retenues": sum(v[1] for v in vraies),
                           "autres_examinees": len(autres), "autres_passees": sum(v[2] for v in autres)}
        out["tentatives_par_classe"] = dict(self.tentatives)
        return out

    def fusionner(self, autre):
        self.par_loi.update(autre.par_loi)
        self.criblage.update(autre.criblage)
        for c in CLASSES:
            self.tentatives[c] += autre.tentatives[c]


def frequences_gelees(comptes):
    """Les cinq fréquences injectées dans la couche statistique (fichier scellé avant tout tirage décisif)."""
    def part(a, b):
        return a / b if b else 0.0
    c = comptes["criblage"]
    return {"p_tient_vraie": part(comptes["vraie"]["tiennent"], comptes["vraie"]["engagees"]),
            "p_tient_fausse": part(comptes["fausse"]["tiennent"], comptes["fausse"]["engagees"]),
            "p_tient_non_plantee": part(comptes["non-plantee"]["tiennent"], comptes["non-plantee"]["engagees"]),
            "p_passage_vraie": part(c["vraies_retenues"], c["vraies_examinees"]),
            "p_faux_passage": part(c["autres_passees"], c["autres_examinees"])}


def frequences_gelees_par_origine(comptes):
    """Variante (point pour la mère) : la fréquence de « tient » des lois non plantées, par origine de la tentative (recherche
    de base, composition criblée, copie). À la lettre de M12, la loi non plantée a une seule fréquence."""
    f = frequences_gelees(comptes)
    for o in ORIGINES_NON_PLANTEES:
        c = comptes["non-plantee-" + o]
        f["p_tient_non_plantee_" + o] = c["tiennent"] / c["engagees"] if c["engagees"] else f["p_tient_non_plantee"]
    return f


def verifier_s8_i(freqs):
    """S8 (i) (garde 24) : l'épreuve simulée discrimine ; sinon arrêt (liste d'arrêt, point 4)."""
    if not (freqs["p_tient_vraie"] >= 0.5 and freqs["p_tient_fausse"] <= 0.5):
        raise RuntimeError(f"S8 (i) : l'épreuve simulée ne discrimine pas ({freqs}) : arrêt, aucun tirage décisif")
    return True


class ContexteSource:
    def __init__(self, graines, base, prop, dose, taux_echec, dossier, executeur=None, repere=REPERE_LECTURE,
                 regle_retrait="v2", liste="avec_description", repli=False, faute=None, organisme=None):
        self.graines, self.base, self.prop, self.dose, self.taux = graines, dict(base), prop, dose, taux_echec
        self.dossier, self.executeur = dossier, executeur or Executeur()
        self.repere, self.regle, self.liste, self.repli, self.faute = repere, regle_retrait, liste, repli, faute
        self.organisme = organisme
        self.configuration_sha = __import__("hashlib").sha256(json_canonique(
            {"base": self.base, "prop": prop, "dose": dose, "taux": taux_echec, "repere": repere, "regle": regle_retrait,
             "liste": liste, "repli": repli, "version": VERSION}).encode("utf-8")).hexdigest()

    def g(self, **champs):
        return self.graines.g(**self.base, **champs)

    def etiquette(self, **champs):
        return etiquette(**self.base, **champs)


def _parts_servies_depuis_fichiers(dossier_monde, monde):
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


def _appels(ctx, bras, generation, n_servi, paie, jumelle=None):
    lecture = float(cout_lecture_par_appel(n_servi, ctx.repere)) if (paie and n_servi) else 0.0
    extra = {} if jumelle is None else {"jumelle": jumelle}
    if ctx.regle == "v1":
        par_espece = retrait_v1(lecture)[0]
        return int(par_espece.sum()), 0.0
    perm = ctx.g(bras=bras, generation=generation, role="retrait", **extra).permutation(APPELS_PAR_GENERATION)
    gardes, retires, reliquat = retrait_v2(perm, np.full(APPELS_PAR_GENERATION, lecture))
    verifier_retrait(perm, gardes, retires, np.full(APPELS_PAR_GENERATION, lecture))
    return len(gardes), reliquat


def _jouer_generation(ctx, registre, monde, dossier_monde, bras, generation, origine, vue, finale, freqs, jumelle=None):
    """Une génération d'un bras (ou de la course source). Rend la liste des (tentative, classe, appariement) et le reliquat."""
    extra = {} if jumelle is None else {"jumelle": jumelle}
    n_servi = len(vue) if vue else 0
    verifier_bras_1_non_servi(bras, vue)
    appels, reliquat = _appels(ctx, bras, generation, n_servi, ctx.prop["paie"], jumelle)
    rng = ctx.g(bras=bras, generation=generation, role="echantillonnage", **extra)
    n_tent = int(nombre_de_tentatives(np.array([appels]), rng)[0])
    parts = _parts_servies_depuis_fichiers(dossier_monde, monde)
    propre = bool(vue) and any(e.get("gardee") and e["provenance"]["origine"] == origine for e in vue)
    mesure = []
    tentatives = proposer(ctx.prop, vue, monde, parts, n_tent, rng, repli=ctx.repli, propre_gardee=propre, mesure=mesure,
                          en_continuation=origine == "continuation")
    for t, vraie, retenue, passe in mesure:
        freqs.criblage[(monde.nom, t)] = (vraie, retenue, passe)
    entrees = []
    for dom, loi, _origine in tentatives:
        eng = engagement(dom, loi)
        entrees.append(nouvelle_entree(dom, eng, sceller(eng), DESCRIPTION_FIXE, JUSTIFICATION_FIXE, PREDICTION_FIXE))
    sorties, _ = eprouver_generation(entrees, monde.tranche_epreuve, ctx.executeur,
                                     ctx.g(bras=bras, generation=generation, role="echec", **extra), ctx.taux,
                                     2 * appels, ctx.g(bras=bras, generation=generation, role="budget", **extra), ctx.liste)
    rendu = []
    for (e, (resultat, gardee)), (_, _, origine) in zip(zip(entrees, sorties), tentatives):
        eng = e["tentative"]["engagement"]
        ident, _ = apparier(eng, e["tentative"]["engagement_sha256"], eng["domaine"], monde.lois_du_domaine(eng["domaine"]),
                            monde.oracle)
        typ = "non-plantee" if ident is None else monde.lois[ident]["type"]
        loi = loi_du_texte(eng["test_de_mort"]["test"])
        cle = (monde.nom, json_canonique(loi))
        if cle not in freqs.par_loi:
            freqs.par_loi[cle] = (typ, ctx.executeur.classe_sans_echec(loi, monde.tranche_epreuve(eng["domaine"])), origine)
        if resultat["classe"] in freqs.tentatives:
            freqs.tentatives[resultat["classe"]] += 1
        rendu.append((e, resultat, ident))
        if not finale:
            registre.ajouter(dict(e, resultat=resultat, gardee=gardee,
                                  provenance=provenance(origine, generation, VERSION, ctx.configuration_sha)))
    if not finale:
        registre.sceller_generation(f"generation-{generation}")
        registre.verifier_chaine()
    return rendu, reliquat


def mesure_finale(rendu, monde, exclu):
    """M1 (lois vraies plantées distinctes appariées, ensemble exclu retiré), D, I, et lois fausses tenues (distinctes, au moins
    une tentative classée « tient » au test de mort du monde final)."""
    vraies, fausses_tenues = set(), set()
    for e, resultat, ident in rendu:
        if ident is None or ident in exclu:
            continue
        if monde.lois[ident]["type"] == "vraie":
            vraies.add(ident)
        elif resultat["classe"] == TIENT:
            fausses_tenues.add(ident)
    d = sum(1 for i in vraies if monde.lois[i]["dependante"])
    return {"M1": len(vraies), "D": d, "I": len(vraies) - d, "fausses_tenues": len(fausses_tenues)}


def jouer_source(ctx, bras=("1", "2", "3"), registre_etranger=None, registres_etrangers_par_generation=None,
                 historique_de_depart=None, jumelles=(None,)):
    """Joue une source. Rend {"suite", "registre_source", "bras": {bras: {mesure, reliquats, entrees_par_generation}},
    "frequences", "exclu"}. `registre_etranger` (bras 4a) et `registres_etrangers_par_generation` (bras 4b) sont des copies
    scellées déposées par l'orchestrateur (garde 27)."""
    exiger_historique_vide(historique_de_depart)
    exiger_taux_egaux({b: ctx.taux for b in bras})
    os.makedirs(ctx.dossier)
    suite = generer_suite(ctx.graines, ctx.base, ctx.dose, faute=ctx.faute)
    dossiers = {}
    for m in [suite.source] + suite.mondes_cibles():
        dossiers[m.nom] = os.path.join(ctx.dossier, "mondes", m.nom)
        ecrire_monde(dossiers[m.nom], m)
    freqs = Frequences()
    # course source
    os.makedirs(os.path.join(ctx.dossier, "course-source"))
    rs = Registre(os.path.join(ctx.dossier, "course-source", "registre.jsonl"))
    for gen in range(1, GENERATIONS_COURSE_SOURCE + 1):
        _jouer_generation(ctx, rs, suite.source, dossiers[suite.source.nom], "source", gen, "course-source",
                          rs.vue("entiere"), False, freqs)
    lois_source = [loi_du_texte(e["tentative"]["engagement"]["test_de_mort"]["test"]) for e in rs.entrees]
    exclu = ensemble_exclu(suite.finale, lois_source)
    etiquettes = {}
    sortie = {"suite": suite, "registre_source": rs, "bras": {}, "frequences": freqs, "exclu": exclu}
    for b in bras:
        for jum in jumelles:
            cle = b if jum is None else f"{b}-j{jum}"
            d = os.path.join(ctx.dossier, f"bras-{cle}")
            os.makedirs(d)
            if b in ("3", "4a"):
                src = rs if b == "3" else registre_etranger
                if src is None:
                    raise RuntimeError("garde 27 : bras 4a sans registre étranger déposé")
                shutil.copyfile(src.chemin, os.path.join(d, "registre.jsonl"))
                r = Registre(os.path.join(d, "registre.jsonl"), entrees=src.entrees)
            else:
                r = Registre(os.path.join(d, "registre.jsonl"))
            r.verifier_chaine()
            reliquats, tailles, vues = [], [], []
            for gen, monde in enumerate(suite.mondes_cibles(), 1):
                finale = gen == MONDES_CIBLES_D_EVOLUTION + 1
                if b == "4b":
                    vue = registres_etrangers_par_generation[gen - 1].vue("entiere")
                else:
                    vue = r.vue("sans_resultat_ni_gardee" if (ctx.repli and b != "1") else VUE_PAR_BRAS[b])
                avant = r.octets()
                if finale:
                    r.fermer()
                rendu, reliquat = _jouer_generation(ctx, r, monde, dossiers[monde.nom], b, gen, "continuation", vue, finale,
                                                    freqs, jumelle=jum)
                if finale:
                    verifier_finale_sans_ecriture(avant, r)
                    sortie["bras"][cle] = {"mesure": mesure_finale(rendu, monde, set(exclu)), "reliquats": reliquats + [reliquat],
                                           "entrees_servies": tailles + [len(vue) if vue else 0], "registre": r}
                reliquats.append(reliquat)
                tailles.append(len(vue) if vue else 0)
            etiquettes[cle] = {"monde": [m.nom for m in suite.mondes_cibles()],
                               "echantillonnage": [ctx.etiquette(bras=b, generation=g, role="echantillonnage",
                                                                 **({} if jum is None else {"jumelle": jum}))
                                                   for g in range(1, MONDES_CIBLES_D_EVOLUTION + 2)]}
    verifier_graines_des_bras(etiquettes)
    return sortie
