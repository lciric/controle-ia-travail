"""Course d'idéation de l'organisme (v7, version 31) : lanceur.

Deux moteurs :
- `--moteur simule` (sans dépense) : des proposeurs scriptés rendent des fiches au gabarit tirées d'un petit catalogue,
  des juges scriptés notent par une règle fixe — répétition de la plomberie, du scellement et de la lecture ; ce n'est
  pas l'idéation ;
- `--moteur claude-sdk --url-relais URL --confirmer-moteur-reel` (dépense, chez session-depot, sous un GO cité) : vrais
  agents (Opus 5.5 et Fable 5.1 seuls, décision de Lazar du 27 octobre), bac à sable exigé, lectures bornées au dossier de
  chaque agent, clé tenue par le relais du noyau (`pole/relais_reel.py`) avec son propre plafond.

Usage :
  python -I -B demonstrations/ideation_v1.py SORTIE_NEUVE --question QUESTION.md --piece P1.md [--piece P2.md …]
      [--proposeur opus=claude-opus-5-5] [--proposeur fable=claude-fable-5-1] [--juge j1=claude-fable-5-1] …
      [--materiau M.md …] [--seconde-passe] [--nombre 8] [--budget-total-usd 20] [--budget-session-usd 3]
      [--graine 20261028] [--moteur simule|claude-sdk] [--url-relais URL] [--confirmer-moteur-reel]
      [--horodatage "date -u"]

Pièces refusées quoi qu'il arrive (garde dans `pole/ideation.py`) : zone en quarantaine, banques, internes des moniteurs,
carte des hypothèses.
"""

import argparse
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, RACINE)

from pole import ideation as idn  # noqa: E402
from pole.adaptateurs import Resultat  # noqa: E402
from pole.outils import graine_derivee, horodatage  # noqa: E402


class AdaptateurIdeationSimule:
    """Moteur simulé de la course d'idéation : fiches au gabarit tirées d'un catalogue, notes par règle fixe."""
    nom = "simule-ideation"
    COUT = {"proposeur_ideation": 0.40, "juge_ideation": 0.60}

    def __init__(self, graine):
        self.graine = graine

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        import random
        rng = random.Random(graine_derivee(self.graine, role, dossier))
        if role == "proposeur_ideation":
            n = rng.randint(2, 4)
            fiches = []
            for i in range(n):
                fiches.append({
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
                    "anteriorite": [{"reference": "référence simulée", "statut": "SUPPOSE"}]})
            return Resultat("```json\n" + json.dumps({"fiches": fiches}, ensure_ascii=False) + "\n```", [],
                            self.COUT[role], "ok")
        if role == "juge_ideation":
            import re
            idents = sorted(set(re.findall(r'"identifiant": "(T\d\d)"', consigne)))
            notes = [{"identifiant": i, "criteres": {k: rng.randint(0, idn.NOTE_MAX) for k in idn.CRITERES},
                      "justifications": {k: "justification simulée" for k in idn.CRITERES}} for i in idents]
            return Resultat("```json\n" + json.dumps({"notes": notes, "doublons": []}) + "\n```", [],
                            self.COUT[role], "ok")
        raise ValueError(role)


def paire(texte, defaut_etiquette):
    if "=" in texte:
        etiquette, modele = texte.split("=", 1)
    else:
        etiquette, modele = defaut_etiquette, texte
    return etiquette.strip(), modele.strip()


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("sortie", help="dossier de sortie, absent (jamais écrasé)")
    a.add_argument("--question", required=True, help="fichier texte de la question posée aux proposeurs")
    a.add_argument("--piece", action="append", default=[], help="pièce servie aux proposeurs (répétable)")
    a.add_argument("--piece-juge", action="append", default=[], help="pièce de contexte servie aux juges (répétable)")
    a.add_argument("--materiau", action="append", default=[], help="matériau servi en seconde passe seulement")
    a.add_argument("--seconde-passe", action="store_true")
    a.add_argument("--proposeur", action="append", default=[], help="etiquette=modele (répétable)")
    a.add_argument("--juge", action="append", default=[], help="etiquette=modele (répétable)")
    a.add_argument("--nombre", type=int, default=8, help="fiches au plus par proposeur et par passe")
    a.add_argument("--max-tours", type=int, default=6)
    a.add_argument("--budget-total-usd", type=float, default=20.0)
    a.add_argument("--budget-session-usd", type=float, default=3.0)
    a.add_argument("--graine", type=int, default=20261028)
    a.add_argument("--moteur", choices=("simule", "claude-sdk"), default="simule")
    a.add_argument("--url-relais")
    a.add_argument("--confirmer-moteur-reel", action="store_true")
    a.add_argument("--accepter-sans-bac-a-sable", action="store_true")
    a.add_argument("--motif-sans-bac-a-sable", default="")
    a.add_argument("--horodatage", help="heure UTC lue sur `date -u`")
    args = a.parse_args(argv)

    proposeurs = [paire(p, f"proposeur-{i + 1}") for i, p in enumerate(args.proposeur)] or \
        [("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")]
    juges = [paire(j, f"juge-{i + 1}") for i, j in enumerate(args.juge)] or \
        [("juge-fable", "claude-fable-5-1"), ("juge-opus", "claude-opus-5-5")]
    with open(args.question, "r", encoding="utf-8") as f:
        question = f.read()

    if args.moteur == "claude-sdk":
        from pole.adaptateurs import (AdaptateurClaudeSDK, MoteurNonArme, exiger_bac_a_sable, importer_sdk,
                                      verifier_modele_reel)
        if not args.confirmer_moteur_reel:
            raise MoteurNonArme("--moteur claude-sdk exige --confirmer-moteur-reel (dépense réelle, relais local requis)")
        if not args.url_relais:
            raise MoteurNonArme("--moteur claude-sdk exige --url-relais")
        for _, m in proposeurs + juges:
            verifier_modele_reel(m)
        adaptateur = AdaptateurClaudeSDK(args.url_relais, arme=True, interdire_lecture=[os.path.abspath(args.sortie)])
        adaptateur.bac_a_sable = exiger_bac_a_sable(importer_sdk(), args.accepter_sans_bac_a_sable,
                                                    args.motif_sans_bac_a_sable)
    else:
        adaptateur = AdaptateurIdeationSimule(args.graine)

    res = idn.executer_ideation(adaptateur, os.path.abspath(args.sortie), pieces=args.piece, question_texte=question,
                                proposeurs=proposeurs, juges=juges, graine=args.graine,
                                budget_total_usd=args.budget_total_usd, budget_session_usd=args.budget_session_usd,
                                nombre_par_proposeur=args.nombre, max_tours=args.max_tours, materiau=args.materiau,
                                seconde_passe=args.seconde_passe, pieces_juge=args.piece_juge,
                                horodatage=horodatage(args.horodatage))
    print(json.dumps({"fiches_validees": len(res["fiches"]), "refusees": len(res["refus"]),
                      "quarantaine": len(res["quarantaine"]), "notes_refusees": len(res["notes_refusees"]),
                      "cout_total_usd": round(res["journal"]["cout_total_usd"], 4), "arret": res["journal"]["arret"],
                      "retenues": [(l["rang"], l["identifiant"], l["nom"], l["total"]) for l in res["classement"]
                                   if l["eligible"]][:5]}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(principal())
