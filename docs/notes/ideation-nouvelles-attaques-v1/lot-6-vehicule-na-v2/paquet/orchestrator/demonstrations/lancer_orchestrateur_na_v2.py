"""Véhicule NA-1, lot 6 v2 — le lanceur de l'orchestrateur (`lancer_orchestrateur_na_v2`).

v2 : le lanceur exige le contrôle de départ de la colonne « matière première » (`depart_colonne`, un `DepartColonne` du
lot 10 a, rendu par `preparer_depart` au lanceur de course, lot 8) ; sans lui, refus avant toute écriture. Il passe à la
course l'état de ce contrôle et la fabrique du journal de la colonne (`course_na_v2.fabrique_journal_colonne`). Le reste
est le v1, inchangé.

Lettre : conception du véhicule v5 (`1b7f6822…`), § 1.2 (le lanceur neuf lève le refus du moteur réel de la v68 sans
appeler son lanceur), § 2.9 (« lève le refus du moteur réel pour ce seul régime, à quatre conditions tenues ensemble : le
nom du régime ; la ligne d'accord au montant exact ; l'additif du véhicule épinglé à son empreinte ; trois générations,
aucun étage. Tout autre jeu d'options reste refusé, moteur simulé compris hors de l'essai à blanc. Il construit
l'adaptateur Claude neuf du § 2.3 pour Minuit et pour Luc »).

    python -I -B demonstrations/lancer_orchestrateur_na_v1.py --configuration CONF --empreinte-configuration SHA \
        --sortie SORTIE_NEUVE --regime NOM --generations 3 --ligne-accord-usd MONTANT --additif FICHIER \
        --empreinte-additif SHA (--moteur simule --essai-a-blanc | --moteur reel --confirmer-moteur-reel) \
        [--verifier-seulement]

Ordre, **avant toute écriture et tout appel** : configuration à son empreinte (n° 14) ; additif à son empreinte, égale à
celle que la configuration épingle ; régime (les quatre conditions) ; gardes héritées ; moteur. Le moteur simulé n'est
permis qu'à l'essai à blanc ; le moteur réel, qu'avec les quatre conditions et `--confirmer-moteur-reel`. Ce lanceur ne
lit aucune clé et n'en nomme aucune : les relais, l'environnement filtré et la ligne d'accord vérifiée au registre sont au
lanceur de course (lot 8), qui l'appelle. Rien de ce qu'il écrit hors de la sortie ne recopie un contenu : la sortie
d'écran est faite d'identifiants, d'empreintes et de comptes.

Codes : 0, sortie écrite (ou vérification faite) ; 2, refus ou arrêt nommé (nom de l'arrêt sur la sortie d'erreur, sans
contenu).
"""

import argparse
import hashlib
import json
import os
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
if RACINE not in sys.path:
    sys.path.insert(0, RACINE)

from pole import configuration_course_na_v1 as cfn  # noqa: E402
from pole import course_na_v2 as cn  # noqa: E402
from pole import matiere_premiere_na_v1 as mp  # noqa: E402

VERSION = "lanceur-orchestrateur-na-v2"
MOTEURS = ("simule", "reel")


class LancementRefuseNA(RuntimeError):
    """Un jeu d'options que ce lanceur refuse : rien n'est écrit, rien n'est appelé."""


def decider_moteur(moteur, *, essai_a_blanc, confirmer_moteur_reel):
    """Le moteur simulé seulement à l'essai à blanc ; le moteur réel seulement confirmé, hors de l'essai à blanc."""
    if moteur not in MOTEURS:
        raise LancementRefuseNA("--moteur simule ou --moteur reel exigé")
    if moteur == "simule":
        if not essai_a_blanc or confirmer_moteur_reel:
            raise LancementRefuseNA("moteur simulé : seulement à l'essai à blanc (--essai-a-blanc)")
        return "simule"
    if essai_a_blanc or not confirmer_moteur_reel:
        raise LancementRefuseNA("moteur réel : --confirmer-moteur-reel exigé, jamais à l'essai à blanc")
    return "reel"


def verifier_additif(config, chemin, empreinte):
    try:
        with open(chemin, "rb") as f:
            sha = hashlib.sha256(f.read()).hexdigest()
    except OSError:
        raise cfn.ArretEmpreinteNA("additif du véhicule", "lancement ; pièce illisible") from None
    if sha != empreinte:
        raise cfn.ArretEmpreinteNA("additif du véhicule", "lancement")
    return sha


def adaptateurs_simules(config, table):
    from pole import simulation_na_v1 as sim
    s = config.noyau.get("simulation") or {}
    if "cout_par_appel_usd" not in s:
        raise LancementRefuseNA("moteur simulé : noyau.simulation.cout_par_appel_usd exigé (coût fictif, aucun défaut)")
    return sim.adaptateurs_simules_na(table, declaration=cfn.declaration_portier(config), items=config.noyau["items_juge"],
                                      cout_par_appel_usd=float(s["cout_par_appel_usd"]))


def fabrique_adaptateurs_reels(config, table, base_sessions):
    """La fabrique du moteur réel, appelée par la course une fois la sortie créée : pour chaque nom d'adaptateur de la table
    qui porte un rôle, l'adaptateur de son type, lu dans `noyau.fournisseurs` ; une clé Claude reçoit **l'adaptateur neuf
    du lot 4**, sans texte système, qui conserve ses réponses brutes dans la sortie ; une porte de plafond par adaptateur.
    Aucune clé n'est lue ici."""
    def fabrique(sortie):
        from pole.adaptateur_kimi_v53 import AdaptateurKimiProtocole
        from pole.adaptateurs_v56 import AdaptateurCommandeExterneV56, porte_depuis_configuration
        from pole import adaptateur_claude_na_v1 as acn
        fournisseurs = config.noyau.get("fournisseurs") or {}
        interdits = [os.path.realpath(base_sessions), os.path.realpath(os.path.abspath(sortie))]
        reponses = os.path.join(os.path.abspath(sortie), "reponses-brutes")
        os.makedirs(reponses)
        adaptateurs, portes = {}, {}
        noms = sorted({e.adaptateur for e in table.roles.values() if e.cle != "hors_course"})
        for nom in noms:
            f = fournisseurs.get(nom)
            cle = table.cle_de_adaptateur(nom)
            if not isinstance(f, dict) or f.get("type") != cle.type:
                raise LancementRefuseNA(f"adaptateur « {nom} » : son type est celui de sa clé dans la table")
            if f["type"] == "claude_sdk":
                ad = acn.AdaptateurClaudeNA(f["url_relais"], reponses, arme=True, interdire_lecture=interdits)
            elif f["type"] == "commande_externe":
                ad = AdaptateurCommandeExterneV56(f["commande"], exiger_modele_servi=True,
                                                  modeles_servis_permis=f.get("modeles_servis_permis"))
            elif f["type"] == "kimi_protocole":
                ad = AdaptateurKimiProtocole(f["url_relais"], modele=f["modele"], prix_entree=f["prix_entree"],
                                             prix_sortie=f["prix_sortie"], max_sortie_jetons=f["max_sortie_jetons"],
                                             sortie_min_jetons=f["sortie_min_jetons"], delai_s=f["delai_s"])
            else:
                raise LancementRefuseNA(f"adaptateur « {nom} » : type inconnu")
            adaptateurs[nom] = ad
            portes[nom] = porte_depuis_configuration(nom, f.get("porte_plafond"), ad)
        return adaptateurs, portes
    return fabrique


def preparer(args, depart_colonne=None):
    """Tout ce qui se vérifie avant l'écriture : rend (configuration, table, moteur, montant)."""
    if not isinstance(depart_colonne, mp.DepartColonne):
        raise LancementRefuseNA("contrôle de départ de la colonne « matière première » exigé (`DepartColonne`, lot 10 a)")
    config = cfn.lire_configuration_course(args.configuration, args.empreinte_configuration)
    epingle = next((p.sha256 for p in config.pieces_epinglees if p.nom == "additif du véhicule"), None)
    verifier_additif(config, args.additif, args.empreinte_additif)
    montant = cfn.verifier_regime(config, regime=args.regime, nombre_generations=args.generations,
                                  ligne_accord_usd=args.ligne_accord_usd, additif_sha256=args.empreinte_additif,
                                  additif_epingle_sha256=epingle, etage=None)
    cfn.verifier_gardes_heritees(config)
    table = cfn.table_de_course(config)
    moteur = decider_moteur(args.moteur, essai_a_blanc=args.essai_a_blanc, confirmer_moteur_reel=args.confirmer_moteur_reel)
    return config, table, moteur, montant


def executer(args, fabrique_reelle=None, depart_colonne=None):
    config, table, moteur, montant = preparer(args, depart_colonne)
    if args.verifier_seulement:
        return {"version": VERSION, "regime": cfn.REGIME, "configuration_sha256": config.sha256, "moteur": moteur,
                "montant_requis_usd": montant, "etat_colonne": depart_colonne.etat, "ecriture": "aucune",
                "appel": "aucun"}
    if os.path.exists(args.sortie):
        raise LancementRefuseNA("sortie déjà présente : jamais écrasée (R12)")
    base_sessions = tempfile.mkdtemp(prefix="sessions-na-v1-")
    if moteur == "reel":
        adaptateurs = (fabrique_reelle or fabrique_adaptateurs_reels)(config, table, base_sessions)
    else:
        adaptateurs = adaptateurs_simules(config, table)
    go = {"moteur": moteur, "ligne_accord_usd": montant}
    bilan = cn.executer_course_na_v2(config, args.sortie, adaptateurs, regime=args.regime,
                                     nombre_generations=args.generations, ligne_accord_usd=args.ligne_accord_usd,
                                     additif_sha256=args.empreinte_additif, etat_colonne=depart_colonne.etat,
                                     fabrique_journal=cn.fabrique_journal_colonne(depart_colonne), go=go,
                                     racine_sessions=base_sessions)
    return {"version": VERSION, "regime": cfn.REGIME, "moteur": moteur, "generations_completes": len(bilan),
            "cout_par_generation_usd": [l["cout_generation_usd"] for l in bilan]}


def analyseur():
    p = argparse.ArgumentParser(description="lanceur de l'orchestrateur, véhicule NA-1 (un seul régime)")
    p.add_argument("--configuration", required=True)
    p.add_argument("--empreinte-configuration", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--regime", required=True)
    p.add_argument("--generations", type=int, required=True)
    p.add_argument("--ligne-accord-usd", type=float, required=True)
    p.add_argument("--additif", required=True)
    p.add_argument("--empreinte-additif", required=True)
    p.add_argument("--moteur", choices=MOTEURS)
    p.add_argument("--essai-a-blanc", action="store_true")
    p.add_argument("--confirmer-moteur-reel", action="store_true")
    p.add_argument("--verifier-seulement", action="store_true")
    return p


def principal(argv=None, fabrique_reelle=None, depart_colonne=None):
    args = analyseur().parse_args(argv)
    try:
        rendu = executer(args, fabrique_reelle=fabrique_reelle, depart_colonne=depart_colonne)
    except BaseException as e:  # noqa: BLE001 — tout refus ou arrêt : son nom, sans contenu
        d = cn.decrire_arret(e)
        print(json.dumps({"version": VERSION, "refus_ou_arret": d}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(rendu, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
