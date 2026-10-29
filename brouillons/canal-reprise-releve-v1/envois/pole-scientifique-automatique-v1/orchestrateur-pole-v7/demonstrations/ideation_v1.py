"""Course d'idéation de l'organisme (v7, version 38) : lanceur.

Deux moteurs :
- `--moteur simule` (sans dépense) : des proposeurs scriptés rendent des fiches au gabarit tirées d'un petit catalogue, des
  juges scriptés notent par une règle fixe qui respecte le critère des témoins — répétition de la plomberie, du scellement et
  de la lecture ; ce n'est pas l'idéation ; les coûts sont **fictifs** (marqués au manifeste, jamais comptés comme réels) ;
- `--moteur claude-sdk --url-relais http://127.0.0.1:PORT --confirmer-moteur-reel` (dépense, chez session-depot, sous un
  GO cité) : vrais agents (Opus 5.5 et Fable 5.1 seuls), **aucun outil intégré** (`tools=[]` du kit, soit `--tools ''`),
  deux tours au plus, borne de temps par session, bac à sable exigé, clé tenue par le relais du noyau avec son propre
  plafond ; **appel de contrôle de bout en bout par modèle avant la course** (CL31-01), compté au journal ; toute session en
  erreur arrête la course et le lanceur rend un code ≠ 0.

Usage (course) :
  python -I -B demonstrations/ideation_v1.py SORTIE_NEUVE --liste-blanche LISTE.json --question Q.md --piece P1.md …
      --temoins TEMOINS.json [--piece-juge A1.md …] [--materiau M.md … --seconde-passe]
      [--proposeur opus=claude-opus-5-5] [--proposeur fable=claude-fable-5-1]
      [--juge juge-fable=claude-fable-5-1] [--juge juge-opus=claude-opus-5-5]
      [--proposeur-externe argon=gemini-argon --commande-externe "…" [--variable-transmise NOM] …]
      [--juge-externe argon=gemini-argon] [--attestation-materiau ATT.json]
      [--budget proposeur_ideation|claude-fable-5-1=10] … [--budget-total-usd 40] [--budget-externe-usd 9]
      [--nombre 8] [--graine 20261028] [--moteur simule|claude-sdk] [--url-relais URL] [--confirmer-moteur-reel]
      [--horodatage "date -u"] [--racine-depot CHEMIN] [--delai-session-s 1800] [--delai-commande-s 900]
      [--taille-max-pieces 650000]                                                        # v37 : corpus primaire servi

v36 (décisions de Lazar du 28 octobre, 21:05 et 21:20 UTC ; messages n° 117 à 119 de session-depot) :
- **Argon propose à égalité** (`--proposeur-externe`, joué dans la course par `--commande-externe`, qui reçoit la question
  et les pièces sur l'entrée standard) ; sa seconde passe exige `--attestation-materiau` (lecture humaine attestée,
  scellée, du matériau de seconde passe), sinon la course refuse avant tout appel ;
- **Argon juge à poids égal** (`--juge-externe`), **toujours différé** : la course n'appelle jamais le juge externe, écrit
  sa consigne en attente scellée **et n'écrit aucun classement** ; après l'attestation de lecture humaine
  (`{"lecteur", "lu_le", "fiches_validees_sha256", "consignes_en_attente_sha256": {etiquette: …}}`, scellée), le bras joue
  Argon (appel de contrôle, plafond externe séparé) puis écrit le classement **à trois juges** (médiane par critère) :
  python -I -B demonstrations/ideation_v1.py SORTIE --bras-rapporte-differe --attestation-lecture-humaine ATTEST.json \
      --juge-externe argon=gemini-argon --commande-externe "…" [--variable-transmise NOM]
- plafonds : `--budget-total-usd` (Claude, contrôles compris) et `--budget-externe-usd` (Argon, proposeur et juge), séparés.
`--attestation-lecture-humaine` hors du bras, `--commande-externe` sans proposeur externe ni bras, un bras sans commande sur
une course réelle, `--delai-session-s` ≤ 0 : refusés.
Codes de sortie : 0 lisible (ou course écrite, en attente du bras) ; 2 arrêt (session en erreur, pièce refusée, appel de
contrôle, réglage refusé, toute exception) ; 4 témoins échoués chez un juge (classement écrit, marqué illisible ; aucune
« retenue » imprimée) ; 5 juge externe sans réponse (classement à deux juges écrit, marqué « sans juge externe, illisible
au sens du devis »).

La commande externe : consigne sur l'entrée standard, environnement minimal explicite (plus `PLAFOND_SESSION_USD`,
`ROLE_POLE` et `--variable-transmise`, jamais un nom de clé), dernière ligne `{"texte": …, "cout_usd": …}` — coût
**obligatoire, fini, strictement positif** ; sur un échec, le coût imprimé est compté, sinon le plafond de session l'est
(marqué inconnu) ; au délai, tout son groupe de processus est arrêté. En moteur simulé, sans commande, un adaptateur scripté
joue les rôles externes (jamais sur une course réelle).

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

# v37 (CL36-04) : défauts = devis en vigueur (v7 bis : corpus primaire servi) ; tout est réglable par --budget
BUDGETS_PAR_DEFAUT = {("proposeur_ideation", "claude-opus-5-5"): 5.0, ("proposeur_ideation", "claude-fable-5-1"): 9.3,
                      ("juge_ideation", "claude-opus-5-5"): 4.0, ("juge_ideation", "claude-fable-5-1"): 7.0}
BUDGET_EXTERNE_PROPOSEUR = 2.5
BUDGET_EXTERNE_JUGE = 3.5


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
    """v35 (CL34-09) : ouvreur sans mandataire (`ProxyHandler({})`) — les variables de mandataire de l'environnement ne
    détournent jamais la lecture de l'état du relais local."""
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))

    def lire():
        with ouvreur.open(url.rstrip("/") + "/relais/etat", timeout=10) as r:
            return json.loads(r.read().decode("utf-8"))
    return lire


def racine_depot(donnee=None):
    """v35 (CL34-06) : la racine du dépôt, donnée (`--racine-depot`) ou lue par `git rev-parse --show-toplevel` depuis le
    dossier du code ; sinon, cinq niveaux au-dessus du code (arborescence d'envoi), avec son origine consignée."""
    import subprocess
    if donnee:
        return os.path.abspath(donnee), "--racine-depot"
    try:
        r = subprocess.run(["git", "-C", RACINE, "rev-parse", "--show-toplevel"], capture_output=True, timeout=10)
        if r.returncode == 0 and r.stdout.strip():
            return os.path.abspath(r.stdout.decode("utf-8").strip()), "git rev-parse --show-toplevel"
    except (OSError, subprocess.SubprocessError):
        pass
    return os.path.abspath(os.path.join(RACINE, *([os.pardir] * 5))), "cinq niveaux au-dessus du code (repli)"


def version_outil_ligne_de_commande(sdk):
    """v35 (CL34-09) : version de l'outil en ligne de commande que le kit lance (`claude --version`), ou « inconnue »."""
    import shutil
    import subprocess
    candidats = []  # CL35-10 : l'outil que le kit lance réellement d'abord (embarqué), PATH en repli
    try:
        from claude_agent_sdk._internal.transport.subprocess_cli import SubprocessCLITransport
        candidats.append(SubprocessCLITransport("", sdk.ClaudeAgentOptions())._find_cli())
    except Exception:  # noqa: BLE001 — la version est une information du manifeste, jamais une condition
        pass
    candidats.append(shutil.which("claude"))
    for c in candidats:
        if c and os.path.exists(c):
            try:
                r = subprocess.run([c, "--version"], capture_output=True, timeout=30)
                if r.returncode == 0:
                    return {"chemin": c, "version": r.stdout.decode("utf-8", "replace").strip()[:80]}
            except (OSError, subprocess.SubprocessError):
                pass
    return {"chemin": None, "version": "inconnue"}


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
    a.add_argument("--proposeur-externe", action="append", default=[],
                   help="etiquette=modele d'une autre lignée, joué dans la course par --commande-externe")
    a.add_argument("--juge-externe", action="append", default=[], help="etiquette=modele d'une autre lignée, juge différé")
    a.add_argument("--commande-externe", "--commande-juge-externe", dest="commande_externe",
                   help="commande (shell, découpée) qui joue les rôles externes (consigne sur l'entrée standard)")
    a.add_argument("--variable-transmise", action="append", default=[],
                   help="nom d'une variable d'environnement transmise à la commande externe (jamais un nom de clé)")
    a.add_argument("--attestation-lecture-humaine",
                   help="JSON scellé {lecteur, lu_le, fiches_validees_sha256, consignes_en_attente_sha256} : autorise le bras")
    a.add_argument("--attestation-materiau",
                   help="JSON scellé {lecteur, lu_le, materiau_sha256: {nom: sha256}} : seconde passe d'un proposeur externe")
    a.add_argument("--bras-rapporte-differe", action="store_true",
                   help="joue seulement les juges externes différés d'une course déjà faite (SORTIE existante)")
    a.add_argument("--budget", action="append", default=[], help="role|modele=plafond par session en dollars (répétable)")
    a.add_argument("--nombre", type=int, default=8, help=f"fiches au plus par proposeur et par passe (1 à {idn.MAX_FICHES_ABSOLU})")
    a.add_argument("--max-tours", type=int, default=idn.MAX_TOURS_IDEATION)
    a.add_argument("--budget-total-usd", type=float, default=40.0, help="plafond total côté Claude, contrôles compris (devis v7 bis)")
    a.add_argument("--budget-externe-usd", type=float, default=9.0,
                   help="plafond total des sessions externes (Argon : deux passes à 2,5, un jugement à 3,5, contrôles ; devis v7 bis)")
    a.add_argument("--budget-controle-usd", type=float, default=0.2)
    a.add_argument("--racine-depot", help="racine du dépôt (lecture interdite aux agents) ; défaut : git rev-parse")
    a.add_argument("--delai-session-s", type=float, default=None, help="borne de temps par session réelle (défaut 3600, CL37-08)")
    a.add_argument("--delai-commande-s", type=float, default=1800.0, help="borne de temps de la commande externe (CL37-08)")
    a.add_argument("--budget-controle-externe-usd", type=float, default=2.5,
                   help="plafond de l'appel de contrôle du proposeur externe à la taille réelle de la consigne (CL37-01)")
    a.add_argument("--tolerer-somme-plafonds", action="store_true",
                   help="accepte une somme des plafonds par session au-dessus du total (CL37-03 ; sinon refus)")
    a.add_argument("--taille-max-pieces", type=int, default=750_000,
                   help=f"caractères servis au plus par lot de pièces (défaut : devis v7 ter ; plafond dur {idn.TAILLE_MAX_PIECES_ABSOLUE})")
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
    requis = ("sortie",) if args.bras_rapporte_differe else ("sortie", "liste_blanche", "question", "temoins")
    for nom in requis:
        if not getattr(args, nom):
            a.error(f"--{nom.replace('_', '-')} est requis" if nom != "sortie" else "SORTIE est requis")
    if args.bras_rapporte_differe and not (args.juge_externe and args.attestation_lecture_humaine):
        a.error("--bras-rapporte-differe exige --juge-externe et --attestation-lecture-humaine")
    if args.attestation_lecture_humaine and not args.bras_rapporte_differe:  # CL34-01
        a.error("--attestation-lecture-humaine ne se donne qu'avec --bras-rapporte-differe : le bras est toujours différé")
    if args.commande_externe and not (args.bras_rapporte_differe or args.proposeur_externe):  # CL35-07a
        a.error("--commande-externe n'a d'usage qu'avec --proposeur-externe (course) ou --bras-rapporte-differe")
    if args.bras_rapporte_differe and args.proposeur_externe:
        a.error("--bras-rapporte-differe ne joue que des juges externes")
    if not 1 <= args.nombre <= idn.MAX_FICHES_ABSOLU:  # CL34-11
        a.error(f"--nombre ∉ [1, {idn.MAX_FICHES_ABSOLU}]")
    if args.delai_session_s is not None and not args.delai_session_s > 0:  # CL35-09
        a.error("--delai-session-s doit être strictement positif")
    if not args.delai_commande_s > 0:
        a.error("--delai-commande-s doit être strictement positif")
    try:
        return _principal(args)
    except Exception as e:  # noqa: BLE001 — CL35-08 : toute exception après l'analyse des arguments rend 2
        print(json.dumps({"arret": type(e).__name__ + " : " + str(e)[:1000]}, ensure_ascii=False), file=sys.stderr)
        return 2


def _principal(args):
    proposeurs = [paire(p, f"proposeur-{i + 1}") for i, p in enumerate(args.proposeur)] or \
        [("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")]
    juges = [paire(j, f"juge-{i + 1}") for i, j in enumerate(args.juge)] or \
        [("juge-fable", "claude-fable-5-1"), ("juge-opus", "claude-opus-5-5")]
    juges_ext = [paire(j, f"externe-{i + 1}") for i, j in enumerate(args.juge_externe)]
    prop_ext = [paire(j, f"externe-{i + 1}") for i, j in enumerate(args.proposeur_externe)]
    budgets = dict(BUDGETS_PAR_DEFAUT)
    for _, m in juges_ext:
        budgets.setdefault(("juge_ideation", m), BUDGET_EXTERNE_JUGE)
    for _, m in prop_ext:
        budgets.setdefault(("proposeur_ideation", m), BUDGET_EXTERNE_PROPOSEUR)
    for b in args.budget:
        cle, valeur = b.split("=", 1)
        role, modele = cle.split("|", 1)
        budgets[(role.strip(), modele.strip())] = float(valeur)

    etat_bac = None
    versions = {"python": sys.version.split()[0]}
    lire_relais = None
    interdits = []
    sortie = os.path.abspath(args.sortie)
    sortie_controle = sortie + "-controle"
    delai_session = None
    if args.moteur == "claude-sdk" and not args.bras_rapporte_differe:
        from pole.adaptateurs import (DELAI_SESSION_S, AdaptateurClaudeSDK, MoteurNonArme, etat_bac_a_sable_detaille,
                                      importer_sdk, verifier_modele_reel)
        if not args.confirmer_moteur_reel:
            raise MoteurNonArme("--moteur claude-sdk exige --confirmer-moteur-reel (dépense réelle, relais local requis)")
        if not args.url_relais:
            raise MoteurNonArme("--moteur claude-sdk exige --url-relais")
        idn.valider_url_relais_ideation(args.url_relais)
        for _, m in proposeurs + juges:
            verifier_modele_reel(m)
        sdk = importer_sdk()
        versions["claude_agent_sdk"] = getattr(sdk, "__version__", "inconnue")
        versions["outil_ligne_de_commande"] = version_outil_ligne_de_commande(sdk)  # CL34-09, CL35-10
        etat_bac = etat_bac_a_sable_detaille()
        if not etat_bac["actif"]:
            raise idn.CourseInterrompue("bac à sable inactif : " + etat_bac["motif"])
        if not etat_bac["proc_neuf"] and os.geteuid() == 0:
            raise idn.CourseInterrompue("le bac à sable ne monte pas un /proc neuf et l'orchestrateur tourne sous root : "
                                        "lancer les agents sous un utilisateur non root distinct de celui du relais (CL31-15)")
        racine, origine_racine = racine_depot(args.racine_depot)
        interdits = [sortie, sortie_controle, racine, os.path.expanduser("~")]
        versions["racine_depot"] = {"chemin": racine, "origine": origine_racine}
        delai_session = args.delai_session_s or DELAI_SESSION_S
        adaptateur = AdaptateurClaudeSDK(args.url_relais, arme=True, interdire_lecture=interdits, delai_s=delai_session)
        adaptateur.bac_a_sable = etat_bac
        lire_relais = lecteur_relais(args.url_relais)
    else:
        adaptateur = AdaptateurIdeationSimule(args.graine)

    # --- adaptateur des rôles externes (Argon) : la commande, ou un adaptateur scripté en moteur simulé seulement
    externe, commande_externe = None, None
    if args.commande_externe:
        import shlex
        from pole.adaptateurs import AdaptateurCommandeExterne
        externe = AdaptateurCommandeExterne(shlex.split(args.commande_externe), delai_s=args.delai_commande_s,
                                            variables_transmises=tuple(args.variable_transmise))
        commande_externe = externe.description()
    elif args.moteur == "simule" and (prop_ext or args.bras_rapporte_differe):
        externe = AdaptateurIdeationSimule(args.graine + 1)
    elif prop_ext:
        raise idn.CourseInterrompue("--proposeur-externe exige --commande-externe avec le moteur réel")
    elif args.bras_rapporte_differe:
        raise idn.CourseInterrompue("--bras-rapporte-differe exige --commande-externe avec le moteur réel")

    os.makedirs(os.path.dirname(sortie), exist_ok=True)
    if args.bras_rapporte_differe:
        try:
            res = idn.executer_bras_differe(sortie, attestation_lecture_humaine=args.attestation_lecture_humaine,
                                            juges_externes=[(e, m, externe) for e, m in juges_ext], budgets=budgets,
                                            horodatage=horodatage(args.horodatage), budget_controle_usd=args.budget_controle_usd,
                                            exiger_cout_controle=bool(args.commande_externe), budget_externe_usd=None,
                                            commande_externe=commande_externe)
        except idn.SansJugeExterne as e:
            print(json.dumps({"arret": "sans juge externe, illisible au sens du devis : " + str(e),
                              "classement_sans_bras": "classement-sans-bras.json (deux juges, illisible)",
                              "cout_total_usd": round(e.resultat["journal"]["cout_total_usd"], 4)}, ensure_ascii=False,
                             indent=1), file=sys.stderr)
            return 5
        lisible = res["lecture"]["lisible_L2_L4"]
        bilan = {"juges_agreges": res["lecture"]["juges_agreges"], "nom_agregat": res["lecture"]["nom_agregat"],
                 "temoins_ok": res["lecture"]["temoins"]["temoins_ok"], "classement_lisible_L2_L4": lisible,
                 "accords_de_rang_par_paire": res["lecture"]["accords_de_rang_par_paire"],
                 "cout_total_usd": round(res["journal"]["cout_total_usd"], 4), "cout_fictif": res["journal"]["cout_fictif"]}
        if lisible:
            bilan["retenues"] = [(l["rang"], l["identifiant_auteur"], l["nom"], l["total"]) for l in res["classement"]
                                 if l["eligible"]][:5]
        print(json.dumps(bilan, ensure_ascii=False, indent=1))
        return 0 if lisible else 4
    # CL31-01 : appel de contrôle par modèle Claude, avant tout, dans `SORTIE-controle` (interdit en lecture aux agents) ;
    # son coût est compté dans le plafond total (CL34-07). Le juge externe fait le sien sur le chemin différé.
    if args.moteur == "claude-sdk" and not (prop_ext and juges_ext):  # CL36-03
        raise idn.CourseInterrompue("course réelle : --proposeur-externe et --juge-externe (Argon) sont obligatoires "
                                    "(décision de Lazar : poids égal, égalité)")
    # v38 (CL37-04) : tous les réglages vérifiés AVANT tout appel de contrôle (liste blanche, pièces et tailles, attestation
    # du matériau, plafonds finis, somme des plafonds) — un refus ici ne coûte rien
    verif = idn.verifier_reglages(
        liste_blanche=args.liste_blanche, question=args.question, pieces=args.piece, materiau=args.materiau,
        pieces_juge=args.piece_juge, temoins=args.temoins, taille_max_pieces=args.taille_max_pieces,
        attestation_materiau=args.attestation_materiau if (prop_ext and args.seconde_passe) else None,
        budgets=budgets, budget_total_usd=args.budget_total_usd,
        budget_externe_usd=args.budget_externe_usd if (prop_ext or juges_ext) else 0.0, proposeurs=proposeurs, juges=juges,
        proposeurs_externes=prop_ext, juges_externes=juges_ext, seconde_passe=args.seconde_passe,
        cout_controles_prevu_usd=args.budget_controle_usd * len({m for _, m in proposeurs + juges}),
        cout_controles_externes_prevu_usd=args.budget_controle_externe_usd * len(prop_ext),
        tolerer_somme_plafonds=args.tolerer_somme_plafonds)
    if lire_relais is not None:  # CL37-03 : cohérence entre le plafond du relais, sa réserve et le total du cœur
        etat_relais = lire_relais()
        plafond_relais = etat_relais.get("plafond_usd")
        reserve = etat_relais.get("reserve_par_appel_usd")
        if plafond_relais is not None and reserve is not None:
            plus_petit_juge = min(budgets[("juge_ideation", m)] for _, m in juges)
            if float(plafond_relais) - float(reserve) < args.budget_total_usd - plus_petit_juge - 1e-9:
                raise idn.CourseInterrompue(f"relais : plafond {plafond_relais} − réserve {reserve} < total {args.budget_total_usd} − "
                                            f"plus petit juge {plus_petit_juge} : le relais refuserait une session que le cœur "
                                            "lance (CL37-03) ; relancer le relais avec --reserve-par-appel 4")
    modeles = sorted({m for _, m in proposeurs} | {m for _, m in juges})
    controle = idn.appel_de_controle(adaptateur, modeles, sortie_controle, args.budget_controle_usd, lire_relais,
                                     exiger_cout=(args.moteur == "claude-sdk"))
    cout_controle = sum(float(c.get("cout_declare_usd") or 0.0) for c in controle.values())
    cout_controle_externe = 0.0
    for e, m in prop_ext:  # CL36-02 / CL37-01 : contrôle du proposeur externe AVANT la passe 1, sous son rôle, à la
        # taille réelle de la consigne (les pièces servies, à ignorer) — quota, taille de requête et délai éprouvés
        lecture_ext = idn.appel_de_controle(externe, [m], sortie_controle + "-externe-" + e, args.budget_controle_externe_usd,
                                            None, exiger_cout=bool(args.commande_externe), role="proposeur_ideation",
                                            supplement=verif["texte_pieces"])[m]
        controle[f"externe:{e}"] = lecture_ext
        cout_controle_externe += float(lecture_ext.get("cout_declare_usd") or 0.0)
    res = idn.executer_ideation(adaptateur, sortie, liste_blanche=args.liste_blanche, question=args.question,
                                pieces=args.piece, proposeurs=proposeurs, juges=juges, temoins=args.temoins,
                                graine=args.graine, budget_total_usd=args.budget_total_usd, budgets=budgets,
                                nombre_par_proposeur=args.nombre, max_tours=args.max_tours, materiau=args.materiau,
                                seconde_passe=args.seconde_passe, pieces_juge=args.piece_juge,
                                horodatage=horodatage(args.horodatage), moteur=args.moteur,
                                lire_etat_relais=lire_relais, etat_bac_a_sable=etat_bac, url_relais=args.url_relais,
                                versions=dict(versions, appel_de_controle=controle), juges_externes=juges_ext,
                                proposeurs_externes=[(e, m, externe) for e, m in prop_ext],
                                budget_externe_usd=args.budget_externe_usd if (prop_ext or juges_ext) else 0.0,
                                attestation_materiau=args.attestation_materiau, cout_deja_engage_usd=cout_controle,
                                lectures_interdites=interdits, commande_externe=commande_externe,
                                delai_session_s=delai_session, taille_max_pieces=args.taille_max_pieces,
                                cout_externe_deja_engage_usd=cout_controle_externe,
                                tolerer_somme_plafonds=args.tolerer_somme_plafonds)
    bilan = {"fiches_validees": len(res["fiches"]), "refusees": len(res["refus"]), "quarantaine": len(res["quarantaine"]),
             "quarantaine_par_proposeur": res["lecture"]["quarantaine_par_proposeur"],
             "temoins_ok": res["lecture"]["temoins"]["temoins_ok"],
             "cout_total_usd": round(res["journal"]["cout_total_usd"], 4),
             "cout_externe_usd": round(res["journal"]["cout_externe_usd"], 4), "cout_fictif": res["journal"]["cout_fictif"]}
    if res["en_attente_bras"]:
        bilan["en_attente_bras"] = res["lecture"]["bras_rapporte_differe"]
        bilan["classement"] = "aucun avant le bras (n° 118 point 1)"
        print(json.dumps(bilan, ensure_ascii=False, indent=1))
        return 0 if res["lecture"]["temoins"]["temoins_ok"] else 4
    lisible = res["lecture"]["temoins"]["temoins_ok"]
    bilan["classement_lisible_L2_L4"] = lisible
    if lisible:  # v34 (P-7) : aucune « retenue » n'est imprimée quand les témoins ont échoué
        bilan["retenues"] = [(l["rang"], l["identifiant_auteur"], l["nom"], l["total"]) for l in res["classement"]
                             if l["eligible"]][:5]
    print(json.dumps(bilan, ensure_ascii=False, indent=1))
    return 0 if lisible else 4


if __name__ == "__main__":
    raise SystemExit(principal())
