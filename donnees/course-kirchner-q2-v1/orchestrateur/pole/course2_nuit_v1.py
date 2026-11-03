"""Génération de la mini-course d'idéation, Kimi et Argon seuls (GO-2026-11-01-12, devis scénario B) — version 1.

Rédigé le 1er novembre 2026 (sous-agent de session-depot) au-dessus de `course2_v56` (inchangé, R12) ; rien n'a été lancé
par le rédacteur. Adaptation 4 du devis `docs/notes/devis-mini-course-kimi-argon-nuit-v1/devis-mini-course-kimi-argon-nuit-v1.md` :

1. **Sans passe « tableau »** : `etape_passe_tableau` ne fait **aucun appel** et n'écrit rien (ni `tableaux.json`, ni
   passe 2) ; l'étape reste au plan de dépense (la v53 exige ses six noms, dans l'ordre), avec un attendu et un plafond de
   relais nuls ; elle est notée « hors scénario B » au journal des événements et au manifeste. Sans cela, la passe relance
   les proposeurs (aucun interrupteur dans la v56).
2. **Une seule génération**, sans étage entre générations (`executer_mini_course_v1`).
3. **Liste d'arrêt du préenregistrement**, codée ici (les autres motifs le sont déjà dans le noyau v56) :
   - **modèle servi différent** (`ArretModeleServiDifferent`) : l'adaptateur de commande externe de la nuit lève l'arrêt dès
     que la commande rend un refus R-764 « modèle servi » (le noyau v56 ne compterait qu'un appel inexploitable) ; le coût de
     l'appel est compté au plafond de session par le bloc `finally` de `OrchestreV56.appel` (côté prudent) ;
   - **trois échecs consécutifs** d'un même rôle (A3, `arrets.a3_echecs_consecutifs` = 3) : arrêt de **la course**
     (`ArretTroisEchecs`), pas seulement du rôle ;
   - **débordement de la garde Kimi** (M5, S12) : arrêt de la course (`ArretDebordementKimi`) ;
   - plafond de l'étape atteint (coupure : étape protégée « non mesurée (budget) », nœud C13 ; fusions retirées), signal
     reçu (`ArretParSignal`), toute autre exception : déjà dans le noyau v56, sans repli.

Rien d'autre ne change : noyau v56 (A1 du brouillon 10, portes de plafond, A2, A4, A14, A17, A21), aiguilleur, juges, lecteurs,
bisociateur (bras « basique » seul ici, par la configuration), fusions complètes seulement, sorties scellées.
"""

import os

from .adaptateurs_v56 import AdaptateurCommandeExterneV56
from .course2_v56 import GenerationV56
from .noyau_v56 import ArretSurSignal, motif_arret
from .outils import EcrasementInterdit, ecrire_json_scelle

VERSION = "course-2-nuit-v1 (mini-course Kimi et Argon, scénario B, au-dessus de la v56)"
SCENARIO = "B : une génération, 12 fiches attendues, bras « basique », sans passe « tableau » (devis, 68 appels)"


class ArretModeleServiDifferent(RuntimeError):
    """Liste d'arrêt : une commande rend un modèle servi différent du modèle demandé (refus R-764)."""


class ArretTroisEchecs(RuntimeError):
    """Liste d'arrêt : trois échecs consécutifs d'un même rôle (A3) arrêtent la course."""


class ArretDebordementKimi(RuntimeError):
    """Liste d'arrêt : débordement de la garde de niveau méthode de Kimi proposeur (M5, S12)."""


EVENEMENTS_MODELE = ("commande.modele_servi",)


class AdaptateurCommandeExterneNuitV1(AdaptateurCommandeExterneV56):
    """Commande externe v56 (recopie du modèle servi, porte « environnement ») ; un refus « modèle servi » arrête la course."""

    nom = "commande-externe-nuit-v1"

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        r = super().lancer(role, consigne, dossier, budget_usd, max_tours, modele=modele)
        if r.statut == "refus" and isinstance(r.refus, dict) and r.refus.get("evenement") in EVENEMENTS_MODELE:
            raise ArretModeleServiDifferent(f"modèle servi {r.refus.get('modele_servi')!r} ≠ modèle demandé {modele!r} "
                                            "(refus R-764) : arrêt de la course (liste d'arrêt)")
        return r

    def description(self):
        d = super().description()
        d["nuit"] = "refus « modèle servi » = arrêt de la course (ArretModeleServiDifferent, liste d'arrêt)"
        return d


class GenerationNuitV1(GenerationV56):
    def etape_passe_tableau(self, etat):
        """Hors scénario B : aucun appel, aucune écriture (adaptation 4 du devis)."""
        self.passe2 = []
        self.ev("passe-tableau-hors-scenario", regle="scénario B : passe « tableau » retirée par conception, aucun appel")

    def appel(self, etat, **kw):
        a = super().appel(etat, **kw)
        role = kw.get("role")
        r = self.suivi.roles.get(role) or {}
        if isinstance(r.get("arrete"), str) and r["arrete"].startswith("A3"):
            raise ArretTroisEchecs(f"rôle {role} : {r['arrete']} — arrêt de la course (liste d'arrêt)")
        return a

    def _aiguiller(self, fiches, etat, lot):
        avant = sum(1 for e in self.evenements if e.get("evenement") == "arret-role-kimi")
        super()._aiguiller(fiches, etat, lot)
        if sum(1 for e in self.evenements if e.get("evenement") == "arret-role-kimi") > avant:
            raise ArretDebordementKimi("débordement de la garde de niveau méthode de Kimi proposeur au-dessus de S12 : arrêt de la "
                                       "course (liste d'arrêt)")

    def manifeste_depart_v56(self):
        d = super().manifeste_depart_v56()
        d["version_nuit"] = VERSION
        d["scenario"] = SCENARIO
        d["passe_tableau"] = "hors scénario B : étape au plan (attendu 0, plafond de relais 0), aucun appel, rien d'écrit"
        d["liste_arret_nuit"] = ["modèle servi différent", "trois échecs consécutifs d'un rôle", "débordement de la garde Kimi",
                                 "plafond de l'étape atteint (noyau)", "signal reçu (noyau)", "toute autre exception (noyau)"]
        return d


def verifier_configuration_nuit(conf):
    """Contrôles propres au scénario B, avant tout appel : une génération, bras « basique » seul, passe « tableau » nulle."""
    from .configuration_v53 import ConfigurationRefusee
    manques = []
    b = conf.get("bisociateur") or {}
    if b.get("bras") != ["basique"]:
        manques.append(f"bisociateur.bras : [\"basique\"] exigé au scénario B (reçu {b.get('bras')!r})")
    if (conf.get("tableau") or {}).get("juger_passe_tableau") is not False:
        manques.append("tableau.juger_passe_tableau : false exigé (passe retirée)")
    pt = [e for e in conf["budget"]["etapes"] if e.get("nom") == "passe_tableau"]
    if len(pt) != 1 or pt[0].get("attendu_usd") != 0 or pt[0].get("plafond_relais_usd") != 0 or pt[0].get("role") != "sacrifiable":
        manques.append("budget.etapes : passe_tableau sacrifiable, attendu 0 et plafond de relais 0 exigés (scénario B)")
    fournisseurs = sorted({p["fournisseur"] for p in conf["proposeurs"]} | {j["fournisseur"] for j in conf["juges"]}
                          | {l["fournisseur"] for l in conf["lecteurs_etiquettes"]} | {conf["aiguilleur"]["fournisseur"]}
                          | {b["metteur_fusion"]["fournisseur"]})
    if fournisseurs != ["argon", "kimi"]:
        manques.append(f"fournisseurs : Kimi et Argon seuls (reçu {fournisseurs})")
    if conf["budget"].get("portee_plafond") != "course":
        manques.append("budget.portee_plafond : « course » exigé (une génération ; la ligne de GO porte S17)")
    if manques:
        raise ConfigurationRefusee("configuration de la mini-course refusée :\n- " + "\n- ".join(manques))
    return True


def executer_mini_course_v1(conf, sortie, adaptateurs, *, go, racine_sessions=None, portes=None, specification=None, horloge=None):
    """Une génération (`GenerationNuitV1`), sans étage ; `bilan-course.json` écrit sur tout chemin (arrêt compris)."""
    verifier_configuration_nuit(conf)
    if os.path.exists(sortie):
        raise EcrasementInterdit(f"sortie {sortie} déjà présente (R12)")
    os.makedirs(sortie)
    bilan, noeud, arret = [], None, None
    with ArretSurSignal() as garde:
        try:
            rs = None if racine_sessions is None else os.path.join(racine_sessions, "generation-1")
            gen = GenerationNuitV1(conf, os.path.join(sortie, "generation-1"), adaptateurs, numero=1, memoire=None,
                                   heritage_texte=None, go=go, horloge=horloge, racine_sessions=rs, portes=portes,
                                   specification=specification)
            resultat = gen.executer()
            ligne = {"generation": 1, "fiches_classees": len(resultat), "notables": sum(l["notable"] for l in resultat),
                     "c13_satisfaite": gen.budget.etat()["c13_satisfaite"], "noeud": gen.noeud}
            if gen.noeud:
                noeud = f"génération 1 : {gen.noeud}"
            bilan.append(ligne)
        except BaseException as e:
            arret = motif_arret(e)
            raise
        finally:
            garde.nettoyage()
            ecrire_json_scelle(os.path.join(sortie, "bilan-course.json"), {"version": VERSION, "scenario": SCENARIO, "go": go,
                                                                           "generations": bilan, "noeud": noeud, "arret": arret,
                                                                           "signaux": garde.etat()})
    return {"bilan": bilan, "noeud": noeud}


__all__ = ("GenerationNuitV1", "AdaptateurCommandeExterneNuitV1", "executer_mini_course_v1", "verifier_configuration_nuit",
           "ArretModeleServiDifferent", "ArretTroisEchecs", "ArretDebordementKimi", "VERSION", "SCENARIO")
