"""Course d'idéation de l'organisme (v7, version 33) : lanceur.

Deux moteurs :
- `--moteur simule` (sans dépense) : des proposeurs scriptés rendent des fiches au gabarit tirées d'un petit catalogue, des
  juges scriptés notent par une règle fixe qui respecte le critère des témoins — répétition de la plomberie, du scellement et
  de la lecture ; ce n'est pas l'idéation ; les coûts sont **fictifs** (marqués au manifeste, jamais comptés comme réels) ;
- `--moteur claude-sdk --url-relais http://127.0.0.1:PORT --confirmer-moteur-reel` (dépense, chez session-depot, sous un
  GO cité) : vrais agents (Opus 5.5 et Fable 5.1 seuls), **aucun outil**, deux tours au plus, bac à sable exigé, clé tenue par
  le relais du noyau avec son propre plafond ; **appel de contrôle de bout en bout par modèle avant la course** (CL31-01) ;
  toute session en erreur arrête la course et le lanceur rend un code ≠ 0.

Usage :
  python -I -B demonstrations/ideation_v1.py SORTIE_NEUVE --liste-blanche LISTE.json --question Q.md --piece P1.md …
      --temoins TEMOINS.json [--piece-juge A1.md …] [--materiau M.md … --seconde-passe]
      [--proposeur opus=claude-opus-5-5] [--proposeur fable=claude-fable-5-1]
      [--juge juge-fable=claude-fable-5-1] [--juge juge-opus=claude-opus-5-5]
      [--budget proposeur_ideation|claude-fable-5-1=5] … [--budget-total-usd 20] [--nombre 8] [--graine 20261028]
      [--moteur simule|claude-sdk] [--url-relais URL] [--confirmer-moteur-reel] [--horodatage "date -u"]
      [--juge-externe argon=gemini-argon --commande-juge-externe "python appel_argon.py"]   # bras rapporté (v33)

Juge externe (décision de Lazar, 28 octobre, 17:58 heure de Paris : juge d'une autre lignée, extension de N-053 point 4) :
la commande reçoit la consigne anonymisée sur l'entrée standard et imprime en dernière ligne `{"texte": …, "cout_usd": …}` ;
elle tient sa clé elle-même ; ses notes sont rapportées à part, jamais agrégées. En moteur simulé, `--commande-juge-externe`
peut être omise : un juge externe scripté est joué.

La liste blanche (`{chemin réel: sha256}`) est écrite par `--construire-liste-blanche FICHIERS…` puis scellée par le devis ;
le noyau refuse toute pièce, question, matériau ou témoin hors liste ou à empreinte différente, tout lien symbolique, et
toute zone interdite (quarantaine, banques, préenregistrements, carte des hypothèses).
"""

import argparse
import json
import os
import re
import sys
import urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, RACINE)

from pole import ideation as idn  # noqa: E402
from pole.adaptateurs import Resultat  # noqa: E402
from pole.outils import graine_derivee, horodatage  # noqa: E402

BUDGETS_PAR_DEFAUT = {("proposeur_ideation", "claude-opus-5-5"): 2.0, ("proposeur_ideation", "claude-fable-5-1"): 5.0,
                      ("juge_ideation", "claude-opus-5-5"): 1.5, ("juge_ideation", "claude-fable-5-1"): 3.0}


class AdaptateurIdeationSimule:
    """Moteur simulé : fiches au gabarit tirées d'un catalogue, notes par règle fixe (les témoins sont reconnus à leur
    nom, comme un juge honnête les reconnaîtrait à leur contenu), « OK » à l'appel de contrôle. Coûts fictifs."""
    nom = "simule-ideation"
    COUT = {"proposeur_ideation": 0.40, "juge_ideation": 0.60}

    def __init__(self, graine):
        self.graine = graine

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        import random
        rng = random.Random(graine_derivee(self.graine, role, dossier))
        if consigne == idn.APPEL_DE_CONTROLE_CONSIGNE:
            return Resultat("OK", [], 0.0, "ok")
        if role == "proposeur_ideation":
            n = rng.randint(2, 4)
            fiches = [{
                "nom": f"Idée simulée {i + 1}", "type": rng.choice(idn.TYPES_FICHE),
                "enonce": "Énoncé simulé, falsifiable par construction.",
                "loi_predictive": {"espace_instances": "dix familles", "prediction": "effet de 0,2",
                                   "signe": rng.choice(idn.SIGNES), "metrique": "rappel à fausses alertes fixées"},
                "perte_traduction": "aucune, c'est une simulation",
                "questions_servies": [rng.choice(["Q1", "Q2", "Q3", "Q4", "Q-pont", "nouvelle"])],
                "avantage": {"source": rng.choice(idn.SOURCES_AVANTAGE), "texte": "avantage simulé",
                             "incopiable_parce_que": "raison simulée"},
                "originalite": {"niveau": rng.choice(idn.NIVEAUX_ORIGINALITE), "texte": "texte simulé"},
                "demande_organisme": {"nature": rng.choice(idn.NATURES_DEMANDE), "texte": "module simulé"},
                "cout": {"nature": rng.choice(idn.NATURES_COUT), "ordre_de_grandeur": "simulé"},
                "piege": "piège simulé", "cosmetique_si": "si rien ne bouge",
                "anteriorite": [{"reference": "référence simulée", "statut": "SUPPOSE"}]} for i in range(n)]
            return Resultat("```json\n" + json.dumps({"fiches": fiches}, ensure_ascii=False) + "\n```", [],
                            self.COUT[role], "ok")
        if role == "juge_ideation":
            bloc = json.loads(re.search(r"```json\n(\[.*\])\n```", consigne, re.S).group(1))
            notes, doublons, par_nom = [], [], {f["nom"]: f["identifiant"] for f in bloc}
            for f in bloc:
                c = {k: rng.randint(1, idn.NOTE_MAX) for k in idn.CRITERES}
                nom = f["nom"].lower()
                if "verbeux" in nom or "occup" in nom:
                    c.update({"avantage": 1, "originalite": 0, "falsifiabilite": 1})
                if "sobre" in nom or "jumeau" in nom:
                    c.update({"avantage": 3, "originalite": 2})
                notes.append({"identifiant": f["identifiant"], "criteres": c,
                              "justifications": {k: "justification simulée" for k in idn.CRITERES}})
            for f in bloc:
                if f["nom"].lower().startswith("jumeau"):
                    cible = next((v for k, v in par_nom.items() if k.lower().startswith("sobre")), None)
                    if cible:
                        doublons.append([f["identifiant"], cible])
            return Resultat("```json\n" + json.dumps({"notes": notes, "doublons": doublons}) + "\n```", [],
                            self.COUT[role], "ok")
        raise ValueError(role)


def paire(texte, defaut_etiquette):
    if "=" in texte:
        etiquette, modele = texte.split("=", 1)
    else:
        etiquette, modele = defaut_etiquette, texte
    return etiquette.strip(), modele.strip()


def lecteur_relais(url):
    def lire():
        with urllib.request.urlopen(url.rstrip("/") + "/relais/etat", timeout=10) as r:
            return json.loads(r.read().decode("utf-8"))
    return lire


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("sortie", nargs="?", help="dossier de sortie, absent (jamais écrasé)")
    a.add_argument("--construire-liste-blanche", nargs="+", metavar="FICHIER",
                   help="écrit la liste blanche (chemins réels et empreintes) des fichiers donnés dans SORTIE puis sort")
    a.add_argument("--liste-blanche", help="fichier JSON {chemin réel: sha256} (scellé par le devis)")
    a.add_argument("--question", help="fichier texte de la question posée aux proposeurs (dans la liste blanche)")
    a.add_argument("--piece", action="append", default=[], help="pièce servie aux proposeurs (répétable)")
    a.add_argument("--piece-juge", action="append", default=[], help="pièce d'antériorité servie aux juges (répétable)")
    a.add_argument("--materiau", action="append", default=[], help="matériau servi en seconde passe seulement")
    a.add_argument("--temoins", help="fichier JSON des témoins plantés écrits par un tiers (dans la liste blanche)")
    a.add_argument("--seconde-passe", action="store_true")
    a.add_argument("--proposeur", action="append", default=[], help="etiquette=modele (répétable)")
    a.add_argument("--juge", action="append", default=[], help="etiquette=modele (répétable)")
    a.add_argument("--juge-externe", action="append", default=[], help="etiquette=modele d'une autre lignée (bras rapporté)")
    a.add_argument("--commande-juge-externe", help="commande (shell, découpée) qui joue le juge externe")
    a.add_argument("--budget", action="append", default=[], help="role|modele=plafond par session en dollars (répétable)")
    a.add_argument("--nombre", type=int, default=8, help="fiches au plus par proposeur et par passe")
    a.add_argument("--max-tours", type=int, default=idn.MAX_TOURS_IDEATION)
    a.add_argument("--budget-total-usd", type=float, default=20.0)
    a.add_argument("--budget-controle-usd", type=float, default=0.2)
    a.add_argument("--graine", type=int, default=20261028)
    a.add_argument("--moteur", choices=("simule", "claude-sdk"), default="simule")
    a.add_argument("--url-relais")
    a.add_argument("--confirmer-moteur-reel", action="store_true")
    a.add_argument("--accepter-sans-bac-a-sable", action="store_true")
    a.add_argument("--motif-sans-bac-a-sable", default="")
    a.add_argument("--horodatage", help="heure UTC lue sur `date -u`")
    args = a.parse_args(argv)

    if args.construire_liste_blanche:
        if not args.sortie:
            a.error("--construire-liste-blanche exige SORTIE (le fichier JSON à écrire)")
        liste = idn.construire_liste_blanche(args.construire_liste_blanche, args.sortie)
        print(json.dumps({"liste_blanche": args.sortie, "fichiers": len(liste)}, indent=1))
        return 0
    for nom in ("sortie", "liste_blanche", "question", "temoins"):
        if not getattr(args, nom):
            a.error(f"--{nom.replace('_', '-')} est requis" if nom != "sortie" else "SORTIE est requis")

    proposeurs = [paire(p, f"proposeur-{i + 1}") for i, p in enumerate(args.proposeur)] or \
        [("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")]
    juges = [paire(j, f"juge-{i + 1}") for i, j in enumerate(args.juge)] or \
        [("juge-fable", "claude-fable-5-1"), ("juge-opus", "claude-opus-5-5")]
    externes = [paire(j, f"externe-{i + 1}") for i, j in enumerate(args.juge_externe)]
    budgets = dict(BUDGETS_PAR_DEFAUT)
    for _, m in externes:
        budgets.setdefault(("juge_ideation", m), 3.0)
    for b in args.budget:
        cle, valeur = b.split("=", 1)
        role, modele = cle.split("|", 1)
        budgets[(role.strip(), modele.strip())] = float(valeur)

    etat_bac = None
    versions = {"python": sys.version.split()[0]}
    lire_relais = None
    if args.moteur == "claude-sdk":
        from pole.adaptateurs import (AdaptateurClaudeSDK, MoteurNonArme, etat_bac_a_sable_detaille, importer_sdk,
                                      verifier_modele_reel)
        if not args.confirmer_moteur_reel:
            raise MoteurNonArme("--moteur claude-sdk exige --confirmer-moteur-reel (dépense réelle, relais local requis)")
        if not args.url_relais:
            raise MoteurNonArme("--moteur claude-sdk exige --url-relais")
        idn.valider_url_relais_ideation(args.url_relais)
        for _, m in proposeurs + juges:
            verifier_modele_reel(m)
        sdk = importer_sdk()
        versions["claude_agent_sdk"] = getattr(sdk, "__version__", "inconnue")
        etat_bac = etat_bac_a_sable_detaille()
        if not etat_bac["actif"]:
            raise idn.CourseInterrompue("bac à sable inactif : " + etat_bac["motif"])
        if not etat_bac["proc_neuf"] and os.geteuid() == 0:
            raise idn.CourseInterrompue("le bac à sable ne monte pas un /proc neuf et l'orchestrateur tourne sous root : "
                                        "lancer les agents sous un utilisateur non root distinct de celui du relais (CL31-15)")
        # CL31-08 : lectures interdites sur la sortie, la racine du dépôt et le dossier personnel
        interdits = [os.path.abspath(args.sortie), os.path.abspath(os.path.join(RACINE, os.pardir, os.pardir, os.pardir,
                                                                                   os.pardir, os.pardir)),
                     os.path.expanduser("~")]
        adaptateur = AdaptateurClaudeSDK(args.url_relais, arme=True, interdire_lecture=interdits)
        adaptateur.bac_a_sable = etat_bac
        lire_relais = lecteur_relais(args.url_relais)
    else:
        adaptateur = AdaptateurIdeationSimule(args.graine)
    juges_externes = []
    if externes:
        if args.commande_juge_externe:
            import shlex
            from pole.adaptateurs import AdaptateurJugeExterne
            externe = AdaptateurJugeExterne(shlex.split(args.commande_juge_externe))
        elif args.moteur == "simule":
            externe = AdaptateurIdeationSimule(args.graine + 1)
        else:
            raise idn.CourseInterrompue("--juge-externe exige --commande-juge-externe avec le moteur réel")
        juges_externes = [(e, m, externe) for e, m in externes]

    sortie = os.path.abspath(args.sortie)
    os.makedirs(os.path.dirname(sortie), exist_ok=True)
    # CL31-01 : appel de contrôle par modèle, avant tout (le dossier `controle` est créé sous la sortie, que la course
    # crée ensuite avec exist_ok=False → la sortie est créée ici par l'appel de contrôle ; on la passe en revue).
    modeles = sorted({m for _, m in proposeurs} | {m for _, m in juges})
    sortie_controle = sortie + "-controle"
    try:
        controle = idn.appel_de_controle(adaptateur, modeles, sortie_controle, args.budget_controle_usd, lire_relais,
                                         exiger_cout=(args.moteur == "claude-sdk"))
        for e, m, a in juges_externes:  # le bras rapporté a son propre appel de contrôle (sans relais)
            controle[f"externe:{m}"] = idn.appel_de_controle(a, [m], sortie_controle + "-" + e, args.budget_controle_usd,
                                                              None, exiger_cout=bool(args.commande_juge_externe))[m]
    except idn.CourseInterrompue as e:
        print(json.dumps({"arret": "appel de contrôle : " + str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    try:
        res = idn.executer_ideation(adaptateur, sortie, liste_blanche=args.liste_blanche, question=args.question,
                                    pieces=args.piece, proposeurs=proposeurs, juges=juges, temoins=args.temoins,
                                    graine=args.graine, budget_total_usd=args.budget_total_usd, budgets=budgets,
                                    nombre_par_proposeur=args.nombre, max_tours=args.max_tours, materiau=args.materiau,
                                    seconde_passe=args.seconde_passe, pieces_juge=args.piece_juge,
                                    horodatage=horodatage(args.horodatage), moteur=args.moteur,
                                    lire_etat_relais=lire_relais, etat_bac_a_sable=etat_bac, url_relais=args.url_relais,
                                    versions=dict(versions, appel_de_controle=controle), juges_externes=juges_externes)
    except (idn.CourseInterrompue, idn.PieceInterdite, idn.FicheIdeationInvalide) as e:
        print(json.dumps({"arret": type(e).__name__ + " : " + str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    bilan = {"fiches_validees": len(res["fiches"]), "refusees": len(res["refus"]), "quarantaine": len(res["quarantaine"]),
             "temoins_ok": res["lecture"]["temoins"]["temoins_ok"], "classement_lisible_L2_L4":
             res["lecture"]["temoins"]["temoins_ok"] and res["lecture"]["complet"],
             "cout_total_usd": round(res["journal"]["cout_total_usd"], 4), "cout_fictif": res["journal"]["cout_fictif"],
             "bras_rapporte": {j: res["lecture"]["bras_rapporte"]["accord_avec_le_classement_agrege"][j]
                               for j in res["lecture"].get("bras_rapporte", {}).get("juges", {})},
             "retenues": [(l["rang"], l["identifiant_auteur"], l["nom"], l["total"]) for l in res["classement"]
                          if l["eligible"]][:5]}
    print(json.dumps(bilan, ensure_ascii=False, indent=1))
    return 0 if res["classement"] else 3


if __name__ == "__main__":
    raise SystemExit(principal())
