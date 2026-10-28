"""Une génération : (a) gel, (b) expérimentateurs en parallèle, (c) vérificateurs d'un autre modèle, (d) sélection,
(e) mesure de qualité sur les témoins.

Deux modes de sélection :
- « seuil » (brief) : l'expérimentateur rend {verdict, statistique, seuil, code, empreinte_fiche} ; le vérificateur rejoue ;
- « pari » (second ajout) : l'expérimentateur ne rend que des tirages frais liés à l'engagement gelé ; le vérificateur
  rejoue leur production ; la richesse et la promotion sont calculées ici, par l'orchestrateur (`selection_pari`).

Version 0.3.0 (`orchestrateur-pole-v3`) : en sélection par pari, juge v1 par défaut (`juge="v1"` : ordre d'exécution secret
tiré par le noyau après le gel, écrit pour l'expérimentateur dans `ordre-execution.json`, recalculé à l'évaluation ;
urne dans 𝓛), adopté par l'expérience 1 pour les fiches sans parents ; nul des filles v2 par défaut (`nul_filles="v2"` :
membres ajustés, lecture aux instants fixés), adopté par l'expérience 2. La graine du noyau ne quitte jamais
l'orchestrateur (en simulation, elle dérive de la graine du pôle). `juge="v0"` et `nul_filles="v0"` rendent v0.
"""

import concurrent.futures
import json
import math
import os
import random
import shutil
import threading
from dataclasses import asdict, dataclass

from . import selection_pari as sp
from .caviardage import caviarder
from .fiche import STATUTS, FicheModifieeApresGel, ecrire_fiche_gelee, verifier_fichier_fiche
from .outils import (chemin_dans, ecrire_json_scelle, ecrire_scelle, extraire_bloc_json, graine_derivee,
                     json_canonique, nombre_fini, sha256_fichier)

VERDICTS = ("survit", "eliminee", "indecise")
EXCLUS_DU_REJEU = {"fiche.json", "fiche.json.sha256", "engagement.json", "engagement.json.sha256", "resultat.json",
                   "tirages.json", "reponse.txt", "consigne.txt"}


@dataclass
class ConfigGeneration:
    modele_experimentateur: str = "simule-a"
    modele_verificateur: str = "simule-b"
    modele_recombinaison: str = "simule-c"
    modele_synthese: str = "simule-d"
    selection: str = "seuil"
    concurrence: int = 4
    budget_generation_usd: float = 10.0
    plafond_experimentateur_usd: float = 1.0
    plafond_verificateur_usd: float = 0.5
    plafond_recombinaison_usd: float = 0.3
    plafond_synthese_usd: float = 0.2
    max_tours_experimentateur: int = 40
    max_tours_verificateur: int = 30
    max_tours_recombinaison: int = 10
    max_tours_synthese: int = 5
    alpha: float = 0.05
    taille_plan: int = 120
    reservoir: int = 600
    lecture: str = "continu"
    delta0: float = 0.01
    part_calibrage: int = 40
    graine: int = 20261026
    taille_max_rejeu_octets: int = 20_000_000
    juge: str = "v1"
    nul_filles: str = "v2"
    instants_filles: int = 8
    tirage_recombinaison: str = "stratifie"

    def valider(self):
        if self.modele_verificateur == self.modele_experimentateur:
            raise ValueError("le vérificateur doit être d'un autre modèle que l'expérimentateur")
        if self.selection not in ("seuil", "pari"):
            raise ValueError("selection : « seuil » ou « pari »")
        if not (isinstance(self.concurrence, int) and self.concurrence >= 1):
            raise ValueError("concurrence : entier ≥ 1")
        for nom in ("budget_generation_usd", "plafond_experimentateur_usd", "plafond_verificateur_usd",
                    "plafond_recombinaison_usd", "plafond_synthese_usd"):
            if not (nombre_fini(getattr(self, nom)) and getattr(self, nom) > 0):
                raise ValueError(f"{nom} : nombre fini strictement positif")
        if not (0 < self.alpha < 1):
            raise ValueError("alpha dans ]0 ; 1[")
        if self.juge not in ("v0", "v1"):
            raise ValueError("juge : « v0 » ou « v1 »")
        if self.nul_filles not in ("v0", "v2", "v2_souple"):
            raise ValueError("nul_filles : « v0 », « v2 » ou « v2_souple »")
        if self.nul_filles != "v0" and self.juge != "v1":
            raise ValueError("le nul des filles v2 suppose le juge v1 (ordre secret, urne)")
        if not (isinstance(self.instants_filles, int) and 1 <= self.instants_filles <= self.taille_plan):
            raise ValueError("instants_filles : entier dans [1 ; taille_plan]")
        if self.tirage_recombinaison not in ("stratifie", "noyau_corrige"):
            raise ValueError("tirage_recombinaison : « stratifie » (R-527) ou « noyau_corrige » (v0)")
        return self


class Budget:
    """Plafond de dépense d'une génération : réservation avant chaque lancement, règlement au coût déclaré."""

    def __init__(self, plafond):
        self.plafond, self.engage, self.depense, self.depassements = float(plafond), 0.0, 0.0, 0.0
        self._verrou = threading.Lock()

    def reserver(self, montant):
        with self._verrou:
            if self.depense + self.engage + montant > self.plafond + 1e-9:
                return False
            self.engage += montant
            return True

    def regler(self, reserve, cout):
        with self._verrou:
            self.engage -= reserve
            self.depense += cout
            self.depassements += max(0.0, cout - reserve)

    def etat(self):
        return {"plafond": self.plafond, "depense": round(self.depense, 6), "restant": round(self.plafond - self.depense, 6),
                "depassements_declares": round(self.depassements, 6)}


def suit_le_seuil(verdict, statistique, seuil, signe):
    passe = statistique >= seuil if signe == "+" else statistique <= seuil
    return verdict == ("survit" if passe else "eliminee")


def consigne_experimentateur(fiche, empreinte, texte_memoire, mode, empreinte_engagement=None, ordre_secret=False):
    morceaux = [
        "Tu es expérimentateur. Le test ci-dessous est gelé : son empreinte SHA-256 est " + empreinte + ".",
        "La fiche est dans `fiche.json` (son SHA-256 doit rester égal à l'empreinte). Ne la modifie jamais.",
        "Fiche publique :\n" + json.dumps(fiche.vue_publique(), ensure_ascii=False, indent=1, sort_keys=True),
    ]
    if mode == "seuil":
        morceaux.append("Écris le code de l'expérience dans ce dossier, exécute-le, et termine ta réponse par un bloc "
                        "```json {\"verdict\": \"survit\"|\"eliminee\"|\"indecise\", \"statistique\": <nombre>, "
                        "\"seuil\": <le seuil gelé>, \"code\": \"<chemin relatif>\", \"empreinte_fiche\": \"<sha256>\"}```.")
    else:
        morceaux.append(f"Sélection par pari : l'engagement gelé (`engagement.json`, empreinte {empreinte_engagement}) fixe "
                        "la loi prédictive, la bibliothèque nulle et le plan d'instances. Produis les issues aux instances "
                        "du plan par un code rejouable, écris-les dans `tirages.json` ({empreinte_engagement, issues}) et "
                        "termine par un bloc ```json {\"tirages\": \"tirages.json\", \"code\": \"<chemin>\", "
                        "\"empreinte_fiche\": \"<sha256>\", \"empreinte_engagement\": \"<sha256>\"}```. Tu ne calcules "
                        "aucune richesse : l'orchestrateur la calcule.")
        if ordre_secret:
            morceaux.append("Ordre d'exécution imposé par le noyau (`ordre-execution.json`, écrit après le gel) : au temps s, "
                            "traite l'instance d'indice ordre[s] du plan ; range chaque issue à l'indice de son instance ; "
                            "écris aussi dans `tirages.json` le plan (« ordre_secret ») et l'empreinte de l'ordre.")
    if texte_memoire:
        morceaux.append("Mémoire du pôle (à titre d'aide, le test gelé prime) :\n" + texte_memoire)
    return "\n\n".join(morceaux)


def consigne_verificateur(empreinte, declaration, mode):
    quoi = ("rejoue le code déclaré et compare la statistique et le verdict au seuil gelé" if mode == "seuil"
            else "rejoue le code déclaré et compare les tirages produits à `tirages-declares.json`")
    return ("Tu es vérificateur, d'un autre modèle que l'expérimentateur. Le dossier contient la fiche gelée "
            f"(`fiche.json`, empreinte {empreinte}), le code et les données de l'expérience, et la déclaration "
            f"(`declaration.json`) : {json.dumps(declaration, ensure_ascii=False, sort_keys=True)}. Tu {quoi}, tu vérifies "
            "que le test exécuté est le test gelé et tu cherches les raccourcis. Termine par un bloc ```json "
            "{\"confirme\": true|false, \"test_conforme\": true|false, \"motif\": \"...\"}```.")


def _copier_pour_rejeu(source, cible, limite):
    os.makedirs(cible, exist_ok=False)
    total = 0
    for racine, _, fichiers in os.walk(source):
        for nom in fichiers:
            relatif = os.path.relpath(os.path.join(racine, nom), source)
            if relatif in EXCLUS_DU_REJEU or os.path.islink(os.path.join(racine, nom)):
                continue
            total += os.path.getsize(os.path.join(racine, nom))
            if total > limite:
                raise OverflowError("artefacts trop volumineux pour le rejeu")
            os.makedirs(os.path.dirname(os.path.join(cible, relatif)), exist_ok=True)
            shutil.copyfile(os.path.join(racine, nom), os.path.join(cible, relatif))


def instants_reguliers(n, nombre):
    """`nombre` instants de lecture régulièrement espacés dans [1 ; n], le dernier égal à n."""
    return sorted({max(1, round(n * (i + 1) / nombre)) for i in range(nombre)} | {n})


def preparer_engagement(fiche, config, lois_parents=None):
    """Plan d'instances choisi ex ante par le sélecteur mécanique, bibliothèque nulle, seuil : tout est gelé ici.

    Fiche fille (deux parents à loi connue) : nul augmenté des parents et de leurs enveloppes, part de calibrage en tête
    du plan, marge 2·delta0 sur le gain moyen de score logarithmique (troisième ajout au brief) ; sous le nul des filles
    v2, membres ajustés et instants de lecture sous l'empreinte. Juge v1 : ordre d'exécution secret, urne dans 𝓛.
    """
    espace = fiche.espace_instances or {}
    k, d = int(espace.get("nombre_issues", 3)), int(espace.get("dimension", 2))
    rng = random.Random(graine_derivee(config.graine, "plan", fiche.empreinte()))
    reservoir = sp.tirer_instances(rng, config.reservoir, d, int(espace.get("sous_populations", 2)))
    v1 = config.juge == "v1"
    standard = sp.BIBLIOTHEQUE_STANDARD_V1 if v1 else sp.BIBLIOTHEQUE_STANDARD
    plan_execution = "ordre_secret" if v1 else "ordre_naturel"
    if lois_parents:
        plan = sp.selection_divergence(fiche.loi_predictive, reservoir, [1.0 / k] * k, config.taille_plan + config.part_calibrage)
        rng.shuffle(plan)
        bibliotheque = sp.bibliotheque_fille(lois_parents, d, standard, nombre_issues=k)
        if config.nul_filles != "v0":
            from . import nul_filles_v2 as nf  # numpy, importé seulement ici
            bibliotheque = bibliotheque + nf.membres_de_variante(config.nul_filles, lois_parents)
            engagement = nf.construire_engagement_v2(fiche.identifiant, fiche.loi_predictive, plan, k, config.alpha,
                                                     bibliotheque, config.part_calibrage, config.delta0,
                                                     instants_reguliers(config.taille_plan, config.instants_filles),
                                                     plan_execution)
            engagement["empreinte_fiche"] = fiche.empreinte()
        else:
            engagement = sp.construire_engagement(fiche.identifiant, fiche.loi_predictive, plan, k, config.alpha, bibliotheque,
                                                  config.lecture, fiche.empreinte(), part_calibrage=config.part_calibrage,
                                                  delta0=config.delta0, plan_execution=plan_execution)
    else:
        plan = sp.selection_divergence(fiche.loi_predictive, reservoir, [1.0 / k] * k, config.taille_plan)
        engagement = sp.construire_engagement(fiche.identifiant, fiche.loi_predictive, plan, k, config.alpha,
                                              standard, config.lecture, fiche.empreinte(), plan_execution=plan_execution)
    return sp.geler_engagement(engagement)


class Generation:
    def __init__(self, numero, adaptateur, config, racine, registre_gel, budget, memoire=None, lois_connues=None):
        self.numero, self.adaptateur, self.config, self.racine = numero, adaptateur, config.valider(), racine
        self.registre_gel, self.budget, self.memoire = registre_gel, budget, memoire
        self.lois_connues = lois_connues or {}
        self.dossier = os.path.join(racine, "archive", "generations", f"generation-{numero:02d}")
        self.engagements = {}
        # Graine du noyau (ordre d'exécution secret) : jamais écrite dans un dossier d'agent. En simulation, elle dérive de
        # la graine du pôle ; en exécution réelle, le noyau la tient hors de toute vue d'agent.
        self.graine_noyau = graine_derivee(config.graine, "noyau", numero)

    # (a) gel ---------------------------------------------------------------------------------------------------
    def geler(self, fiche):
        """Rend None si la fiche est gelée et prête, sinon le motif du refus (statut déjà posé)."""
        try:
            if self.config.selection == "pari":
                self._controler_pari(fiche)
            empreinte = self.registre_gel.geler(fiche)
        except FicheModifieeApresGel as e:
            fiche.statut = "refusee (modifiee apres gel)"
            return str(e)
        except (ValueError, sp.LoiInvalide) as e:
            fiche.statut = "refusee (invalide)"
            return str(e)
        dossier_exp = os.path.join(self.dossier, fiche.identifiant, "experience")
        os.makedirs(dossier_exp, exist_ok=False)
        ecrire_fiche_gelee(fiche, dossier_exp)
        ecrire_json_scelle(os.path.join(self.racine, "archive", "fiches", fiche.identifiant,
                                        f"gel-generation-{self.numero:02d}.json"),
                           dict(fiche.vue_complete_gelee(), empreinte=empreinte, empreinte_complete=fiche.empreinte_complete()))
        if self.config.selection == "pari":
            parents = {p: self.lois_connues[p] for p in fiche.parents if p in self.lois_connues}
            gele = preparer_engagement(fiche, self.config, parents if len(parents) == 2 else None)
            self.engagements[fiche.identifiant] = gele
            ecrire_scelle(os.path.join(dossier_exp, "engagement.json"), json_canonique(gele.engagement))
            if sp.plan_execution_de(gele.engagement) == "ordre_secret":
                ordre = sp.ordre_execution(self.graine_noyau, gele.empreinte, len(gele.engagement["instances"]))
                ecrire_json_scelle(os.path.join(dossier_exp, "ordre-execution.json"),
                                   {"empreinte_engagement": gele.empreinte, "ordre": ordre})
        fiche.statut = "gelee"
        return None

    def _controler_pari(self, fiche):
        if fiche.loi_predictive is None:
            raise ValueError("sélection par pari : la fiche doit engager une loi prédictive")
        if abs(fiche.severite_attendue - self.config.alpha) > 1e-12:
            raise ValueError(f"sélection par pari : la sévérité est l'α du pôle ({self.config.alpha})")
        espace = fiche.espace_instances or {}
        sp.valider_loi(fiche.loi_predictive, int(espace.get("nombre_issues", 3)), int(espace.get("dimension", 2)))

    # (b) et (c) : un expérimentateur puis un vérificateur par fiche ---------------------------------------------
    def traiter(self, fiche):
        issue = {"identifiant": fiche.identifiant, "famille_source": fiche.famille_source(), "desaccord": False,
                 "couts": {}, "verdict_declare": None, "code": {}}
        try:
            self.registre_gel.verifier(fiche)
        except FicheModifieeApresGel as e:
            return dict(issue, verdict_final="refusee (modifiee apres gel)", motif=str(e))
        empreinte = self.registre_gel.empreinte(fiche.identifiant)
        dossier_exp = os.path.join(self.dossier, fiche.identifiant, "experience")
        gele = self.engagements.get(fiche.identifiant)
        texte_memoire = self.memoire.texte_consigne("experimentateur") if self.memoire else ""
        consigne = consigne_experimentateur(fiche, empreinte, texte_memoire, self.config.selection,
                                            gele.empreinte if gele else None,
                                            ordre_secret=bool(gele) and sp.plan_execution_de(gele.engagement) == "ordre_secret")
        ecrire_scelle(os.path.join(dossier_exp, "consigne.txt"), consigne)
        plafond_exp = min(fiche.cout_borne, self.config.plafond_experimentateur_usd)
        res = self.adaptateur.lancer("experimentateur", consigne, dossier_exp, plafond_exp,
                                     self.config.max_tours_experimentateur, modele=self.config.modele_experimentateur)
        self.budget.regler(plafond_exp, res.cout_declare_usd)
        issue["couts"]["experimentateur"] = res.cout_declare_usd
        ecrire_scelle(os.path.join(dossier_exp, "reponse.txt"), caviarder(res.texte_final)[0])
        cle = "verdict" if self.config.selection == "seuil" else "tirages"
        bloc = extraire_bloc_json(res.texte_final, cle)
        if res.statut != "ok" or bloc is None:
            return dict(issue, verdict_final="indecise", motif="exécution en échec ou bloc JSON absent")
        issue["verdict_declare"] = bloc.get("verdict", "tirages") if cle == "verdict" else "tirages"
        if bloc.get("empreinte_fiche") != empreinte or not verifier_fichier_fiche(os.path.join(dossier_exp, "fiche.json"), empreinte):
            return dict(issue, verdict_final="rejetee (test change)", motif="empreinte de fiche différente de l'empreinte gelée")
        if gele and (bloc.get("empreinte_engagement") != gele.empreinte
                     or sha256_fichier(os.path.join(dossier_exp, "engagement.json")) != gele.empreinte):
            return dict(issue, verdict_final="rejetee (test change)", motif="engagement différent de l'engagement gelé")
        if cle == "verdict":
            if bloc.get("seuil") != fiche.seuil:
                return dict(issue, verdict_final="rejetee (test change)", motif="seuil déclaré différent du seuil gelé")
            if bloc.get("verdict") not in VERDICTS or not nombre_fini(bloc.get("statistique")):
                return dict(issue, verdict_final="indecise", motif="bloc JSON incomplet")
            if bloc["verdict"] != "indecise" and not suit_le_seuil(bloc["verdict"], bloc["statistique"], fiche.seuil,
                                                                  fiche.prediction["signe"]):
                return dict(issue, verdict_final="indecise", motif="verdict incohérent avec la statistique et le seuil")
        code = bloc.get("code")
        if not isinstance(code, str) or not chemin_dans(dossier_exp, code) or not os.path.isfile(os.path.join(dossier_exp, code)):
            return dict(issue, verdict_final="indecise", motif="code introuvable dans le dossier de l'expérience")
        issue["code"] = {"chemin": os.path.relpath(os.path.join(dossier_exp, code), self.racine),
                         "sha256": sha256_fichier(os.path.join(dossier_exp, code))}
        tirages = None
        if gele:
            chemin_t = bloc.get("tirages")
            if not isinstance(chemin_t, str) or not chemin_dans(dossier_exp, chemin_t) or not os.path.isfile(os.path.join(dossier_exp, chemin_t)):
                return dict(issue, verdict_final="indecise", motif="tirages introuvables")
            with open(os.path.join(dossier_exp, chemin_t), encoding="utf-8") as f:
                tirages = json.load(f)
        return self._verifier(fiche, issue, bloc, dossier_exp, empreinte, gele, tirages)

    def _verifier(self, fiche, issue, bloc, dossier_exp, empreinte, gele, tirages):
        dossier_v = os.path.join(self.dossier, fiche.identifiant, "verification")
        try:
            _copier_pour_rejeu(dossier_exp, dossier_v, self.config.taille_max_rejeu_octets)
        except OverflowError as e:
            return dict(issue, verdict_final="indecise", motif=str(e))
        ecrire_fiche_gelee(fiche, dossier_v)
        if gele:
            ecrire_scelle(os.path.join(dossier_v, "engagement.json"), json_canonique(gele.engagement))
            ecrire_scelle(os.path.join(dossier_v, "tirages-declares.json"), json_canonique(tirages))
        ecrire_scelle(os.path.join(dossier_v, "declaration.json"), json_canonique(bloc))
        consigne = consigne_verificateur(empreinte, bloc, self.config.selection)
        res = self.adaptateur.lancer("verificateur", consigne, dossier_v, self.config.plafond_verificateur_usd,
                                     self.config.max_tours_verificateur, modele=self.config.modele_verificateur)
        self.budget.regler(self.config.plafond_verificateur_usd, res.cout_declare_usd)
        issue["couts"]["verificateur"] = res.cout_declare_usd
        ecrire_scelle(os.path.join(dossier_v, "reponse.txt"), caviarder(res.texte_final)[0])
        bloc_v = extraire_bloc_json(res.texte_final, "confirme")
        issue["verification"] = bloc_v
        if bloc_v is None:
            return dict(issue, verdict_final="indecise", desaccord=True, motif="vérification sans conclusion")
        if bloc_v.get("test_conforme") is False:
            return dict(issue, verdict_final="rejetee (test change)", desaccord=True,
                        motif="vérificateur : test exécuté différent du test gelé")
        if bloc_v.get("confirme") is not True:
            return dict(issue, verdict_final="indecise", desaccord=True,
                        motif="verdict non confirmé par le vérificateur : " + str(bloc_v.get("motif", "")))
        if gele:
            try:
                if gele.engagement.get("instants_lecture"):
                    from . import nul_filles_v2 as nf
                    ev = nf.evaluer_v2(gele, tirages, graine_noyau=self.graine_noyau)
                else:
                    ev = sp.evaluer(gele, tirages, graine_noyau=self.graine_noyau)
            except (sp.EngagementModifie, sp.TiragesNonLies, ValueError) as e:  # plan d'exécution non conforme compris
                return dict(issue, verdict_final="rejetee (test change)", motif=f"{type(e).__name__} : {e}")
            issue["pari"] = ev
            issue["statistique"], issue["seuil"] = ev["log_richesse_max" if ev.get("mode", "continu") == "continu"
                                                     else "log_richesse_finale"], ev["seuil_log"]
            verdict = "survit" if ev["promue"] else "eliminee"
            motif = "richesse au seuil 1/α" if ev["promue"] else "richesse sous le seuil 1/α (réfutée par le pari)"
            return dict(issue, verdict_final=verdict, motif=motif)
        issue["statistique"], issue["seuil"] = bloc["statistique"], bloc["seuil"]
        motifs = {"survit": "seuil franchi, verdict confirmé", "eliminee": "statistique sous le seuil (réfutée)",
                  "indecise": "l'expérimentateur déclare l'expérience indécise"}
        return dict(issue, verdict_final=bloc["verdict"], motif=motifs[bloc["verdict"]])

    # ordonnancement : vagues bornées par la concurrence, budget réservé avant chaque lancement ------------------
    def executer(self, fiches):
        ordre = sorted(fiches, key=lambda f: (f.temoin is None, f.identifiant))
        issues, a_lancer = {}, []
        for fiche in ordre:
            refus = self.geler(fiche)
            if refus is not None:
                issues[fiche.identifiant] = {"identifiant": fiche.identifiant, "verdict_final": fiche.statut, "motif": refus,
                                             "famille_source": fiche.famille_source(), "couts": {}, "desaccord": False}
            else:
                a_lancer.append(fiche)
        arret_budget = False
        for debut in range(0, len(a_lancer), self.config.concurrence):
            vague = []
            for fiche in a_lancer[debut:debut + self.config.concurrence]:
                reserve = min(fiche.cout_borne, self.config.plafond_experimentateur_usd) + self.config.plafond_verificateur_usd
                if arret_budget or not self.budget.reserver(reserve):
                    arret_budget = True
                    fiche.statut = "hors budget"
                    issues[fiche.identifiant] = {"identifiant": fiche.identifiant, "verdict_final": "hors budget",
                                                 "motif": "plafond de la génération atteint", "couts": {},
                                                 "famille_source": fiche.famille_source(), "desaccord": False}
                    continue
                vague.append((fiche, reserve))
            with concurrent.futures.ThreadPoolExecutor(max_workers=self.config.concurrence) as pool:
                futurs = {pool.submit(self._traiter_sur, f): f for f, _ in vague}
                for futur in concurrent.futures.as_completed(futurs):
                    fiche = futurs[futur]
                    issue = futur.result()
                    if "experimentateur" not in issue["couts"]:
                        self.budget.regler(min(fiche.cout_borne, self.config.plafond_experimentateur_usd), 0.0)
                    if "verificateur" not in issue["couts"]:
                        self.budget.regler(self.config.plafond_verificateur_usd, 0.0)
                    issues[fiche.identifiant] = issue
        for fiche in ordre:
            self.selectionner(fiche, issues[fiche.identifiant])
        return {"generation": self.numero, "issues": {i: issues[i] for i in sorted(issues)},
                "arret_budget": arret_budget, "budget": self.budget.etat(), "qualite": mesure_qualite(ordre, self.registre_gel)}

    def _traiter_sur(self, fiche):
        """Une erreur de l'orchestrateur sur une fiche la rend indécise, motif écrit ; elle n'arrête pas la génération."""
        try:
            return self.traiter(fiche)
        except Exception as e:  # noqa: BLE001 — consigné dans l'issue, jamais avalé en silence
            return {"identifiant": fiche.identifiant, "famille_source": fiche.famille_source(), "desaccord": False,
                    "couts": {}, "verdict_final": "indecise",
                    "motif": f"erreur de l'orchestrateur : {type(e).__name__} : {caviarder(str(e))[0][:300]}"}

    # (d) sélection ---------------------------------------------------------------------------------------------
    @staticmethod
    def selectionner(fiche, issue):
        verdict = issue["verdict_final"]
        if verdict in ("survit", "eliminee", "indecise", "rejetee (test change)"):
            fiche.essais += 1
        if verdict == "survit":
            fiche.statut = "survit"
            issue["aptitude"] = fiche.aptitude()
        elif verdict == "indecise":
            fiche.statut = "retiree" if fiche.essais >= 2 else "indecise"
        elif verdict in STATUTS:
            fiche.statut = verdict
        fiche.historique.append({"verdict": verdict, "motif": issue.get("motif")})
        issue["statut"] = fiche.statut


# (e) mesure de qualité ---------------------------------------------------------------------------------------------
def mesure_qualite(fiches, registre_gel):
    """Taux de fausses gardées et de vraies éliminées parmi les témoins tranchés ; vérité revérifiée par empreinte."""
    temoins = [f for f in fiches if f.temoin is not None and registre_gel.est_gelee(f.identifiant)]
    for f in temoins:
        registre_gel.verifier(f)
    testes = [f for f in temoins if f.statut in ("survit", "eliminee", "indecise", "retiree", "rejetee (test change)")]
    fausses = [f for f in testes if f.temoin == "fausse"]
    vraies = [f for f in testes if f.temoin == "vraie"]
    gardees = sum(f.statut == "survit" for f in fausses)
    eliminees = sum(f.statut == "eliminee" for f in vraies)
    return {"temoins_faux_testes": len(fausses), "temoins_vrais_testes": len(vraies),
            "fausses_gardees": gardees, "taux_fausses_gardees": gardees / len(fausses) if fausses else None,
            "vraies_eliminees": eliminees, "taux_vraies_eliminees": eliminees / len(vraies) if vraies else None,
            "detail": {f.identifiant: {"verite": f.temoin, "statut": f.statut} for f in temoins}}


def cumuler_qualite(mesures):
    total = {"temoins_faux_testes": 0, "temoins_vrais_testes": 0, "fausses_gardees": 0, "vraies_eliminees": 0}
    for m in mesures:
        for cle in total:
            total[cle] += m[cle]
    total["taux_fausses_gardees"] = total["fausses_gardees"] / total["temoins_faux_testes"] if total["temoins_faux_testes"] else None
    total["taux_vraies_eliminees"] = total["vraies_eliminees"] / total["temoins_vrais_testes"] if total["temoins_vrais_testes"] else None
    return total
