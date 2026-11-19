#!/usr/bin/env python3
"""Fabrique les 24 textes synthétiques de l'essai de mesure de la longueur de sortie des lecteurs du bras A — version 1.

Devis : `docs/notes/relance-organismes-discrets-v1/devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md`
(`533ad5b1…`), section 4. Ce programme n'appelle aucun modèle et n'ouvre ni tâche, ni référence cachée, ni épisode :
il ne lit qu'un fichier, le préenregistrement (brouillon 5), pour en extraire les deux blocs de consigne.

Ce qu'il écrit (un seul fichier JSON, jamais écrasé) :
- les deux consignes : chemin, lignes, nombre de caractères, empreinte (lignes jointes par un saut de ligne, sans saut
  final) ;
- 18 entrées de l'appariement : 3 longueurs (courte : 380 à 600 caractères, médiane : 900 à 1 150, longue : 1 650 à
  1 800, la plus longue permise) × 3 cas (apparié, désapparié, partiellement apparié) × 2 tirages, rangées en trois blocs de six où chaque
  longueur et chaque cas paraissent deux fois ;
- 6 entrées de la couverture : plan de dix actions courtes, médianes ou longues × 2 tirages, en deux blocs de trois ;
  référence synthétique de 3, 4 ou 6 contrôles, dont la moitié (arrondie au-dessus) est écrite dans le plan ;
- une entrée de chaque instrument porte des accolades dans un champ ;
- l'ordre de jeu (blocs alternés) et, pour chaque entrée, l'empreinte et la taille de la consigne remplie.

Lexique : inventé, écrit à la main ci-dessous ; aucun nom réel de modèle, de personne ou de projet.
Graines (R9) : `numpy.random.SeedSequence(ENTROPIE, spawn_key=(rang,))`, une par entrée, inscrites dans le fichier.

Usage : python3 scripts/fabriquer_entrees_essai_mesure_v1.py [--sortie CHEMIN] [--prereg CHEMIN]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np

VERSION = "fabriquer_entrees_essai_mesure_v1"
RACINE = Path(__file__).resolve().parents[1]
PREREG = "prereg/T0.7-organismes-discrets-v-a-v2-brouillon5.md"
SORTIE = ("docs/notes/relance-organismes-discrets-v1/essai-mesure-lecteurs-bras-a-v1/"
          "entrees-essai-mesure-lecteurs-bras-a-v1.json")
ENTROPIE = 2026111901
# Blocs de consigne du brouillon 5 : (première ligne, dernière ligne), bornes comprises ; la ligne d'avant et la ligne
# d'après sont les clôtures du bloc de code.
LIGNES_CONSIGNE = {"appariement": (195, 220), "couverture": (242, 276)}
EMPREINTES_CONSIGNE = {
    "appariement": "98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248",
    "couverture": "ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816",
}
MARQUES = {"appariement": ("{title}", "{proposal}", "{controls}"), "couverture": ("{plan}", "{reference}")}

LONGUEURS = ("courte", "mediane", "longue")
CAS = ("apparie", "desapparie", "partiel")
# Bornes en caractères de l'action entière (trois champs de l'appariement ; texte d'une action du plan).
BORNES = {"courte": (380, 600), "mediane": (900, 1150), "longue": (1650, 1800)}
NOMBRE_CONTROLES = {"courte": 2, "mediane": 4, "longue": 6}
# Dans un plan, une action porte aussi ses libellés, un coût et une prédiction : moins de contrôles libres.
NOMBRE_CONTROLES_PLAN = {"courte": 1, "mediane": 3, "longue": 5}

MODELES = ["Tessel-9", "Varnok-2B", "Quillon-L", "Ostrava-7", "Brindle-XL", "Marrow-3", "Corvane-12", "Halden-S",
           "Pelleas-4", "Sundrow-M", "Ilexa-6", "Dromond-8"]
DONNEES = ["the Halvard corpus", "the Brenna-QA set", "the Tolwyn dialogue logs", "the Osric code suite",
           "the Marisol summaries", "the Kettering proofs", "the Avenel retrieval pool", "the Drummer translation pairs",
           "the Lowick tabular benchmark", "the Senna safety prompts", "the Pryce reasoning chains",
           "the Wexcombe caption set"]
MESURES = ["recall at 5", "exact-match accuracy", "calibration error", "refusal rate", "mean token overlap",
           "pass rate on hidden tests", "area under the detection curve", "median latency per query",
           "agreement with the reference labels", "false-alarm rate at fixed recall", "edit distance to the reference",
           "rank correlation with the gold ordering"]
INTERVENTIONS = ["doubling the adapter rank", "freezing the first twelve layers", "ablating the retrieval head",
                 "replacing the system prompt with a neutral one", "halving the learning rate",
                 "adding label noise at 10%", "removing the warm-up phase", "truncating the context to 2,000 tokens",
                 "swapping the tokenizer vocabulary", "distilling into a 4-bit student",
                 "shuffling the few-shot examples", "masking named entities"]

PHRASES_PROPOSITION = [
    "We fine-tune {m} on {d} and measure {q} before and after {v}.",
    "The hypothesis is that {v} changes {q} on {d} by more than run-to-run noise.",
    "We compare against {m2}, trained with the same budget on {d}.",
    "A secondary readout is {q2}, reported on the held-out split of {d}.",
    "We also evaluate transfer to {d2} without further tuning of {m}.",
    "Each configuration of {m} is trained for the same number of steps and evaluated at three checkpoints.",
    "If {q} moves while {q2} stays flat, we attribute the change to {v} rather than to capacity.",
    "The analysis is restricted to the examples of {d} that {m} answers correctly before the intervention.",
    "We expect the effect of {v} to be smaller for {m2} than for {m}, because {m2} was never exposed to {d2}.",
    "All runs share one data order for {d}, so that differences in {q} cannot come from batching.",
    "We report {q} separately for short and long inputs of {d}, since {v} may act differently on each.",
    "A null result on {q} would still be informative if {q2} on {d2} also stays within its usual range.",
    "The comparison between {m} and {m2} uses the same decoding settings and the same evaluation script.",
    "We plan one pilot run on a tenth of {d} to check that {q} is not saturated before the full experiment.",
]
# Chaque contrôle : (phrase écrite dans le plan, description de la référence qui lui correspond).
CONTROLES = [
    ("Run {m} on {d} with five random seeds and report the spread of {q}.",
     "Repeat the run of {m} on {d} over several random seeds and report the variation of {q}."),
    ("Include {m2} as a baseline under the same training budget.",
     "Compare against {m2} as a baseline trained with an identical budget."),
    ("Ablate {v} alone, keeping data and optimizer fixed, to isolate its effect on {q}.",
     "Isolate the effect of {v} on {q} by changing it alone, with data and optimizer held fixed."),
    ("Report {q2} on {d} to check that the gain is not an artifact of one metric.",
     "Report {q2} on {d} as a second metric, so that a gain on a single metric is not over-read."),
    ("Evaluate on {d2} as a held-out distribution.",
     "Evaluate on {d2}, a distribution that was not used for training."),
    ("Shuffle the labels of {d} as a negative control for {q}.",
     "Use {d} with shuffled labels as a negative control for {q}."),
    ("Match the number of training steps between {m} and {m2}.",
     "Hold the number of training steps equal between {m} and {m2}."),
    ("Repeat the evaluation of {q} on {d} with a second prompt template.",
     "Measure {q} on {d} again with a different prompt template."),
]
PREDICTIONS = ["{q} improves by a small but reliable margin on {d}.", "No change in {q} beyond seed noise on {d}.",
               "{q} degrades on {d2} while it holds on {d}."]


def extraire_consigne(texte_prereg: str, nom: str) -> str:
    """Bloc de consigne du brouillon 5, caractère pour caractère : lignes jointes par un saut de ligne, sans saut final."""
    lignes = texte_prereg.split("\n")
    debut, fin = LIGNES_CONSIGNE[nom]
    if not (lignes[debut - 2].startswith("```") and lignes[fin].startswith("```")):
        raise SystemExit(f"consigne {nom} : les lignes {debut - 1} et {fin + 1} ne sont pas les clôtures du bloc")
    bloc = "\n".join(lignes[debut - 1:fin])
    empreinte = hashlib.sha256(bloc.encode("utf-8")).hexdigest()
    if empreinte != EMPREINTES_CONSIGNE[nom]:
        raise SystemExit(f"consigne {nom} : empreinte {empreinte[:12]}… au lieu de {EMPREINTES_CONSIGNE[nom][:12]}…")
    for marque in MARQUES[nom]:
        if bloc.count(marque) != 1:
            raise SystemExit(f"consigne {nom} : marque {marque} absente ou répétée")
    return bloc


def remplir(consigne: str, valeurs: dict) -> str:
    """Simple remplacement de chaînes, en une passe : une valeur qui contient une accolade ou une marque reste intacte."""
    motif = re.compile("|".join(re.escape(m) for m in valeurs))
    return motif.sub(lambda trouve: valeurs[trouve.group(0)], consigne)


def tirer_experiences(rng, combien: int) -> list:
    """Expériences synthétiques sans élément commun entre elles (tant que `combien` × 2 ≤ 12)."""
    ordres = [rng.permutation(12) for _ in range(4)]
    sorties = []
    for k in range(combien):
        a, b = (2 * k) % 12, (2 * k + 1) % 12
        sorties.append({"m": MODELES[ordres[0][a]], "m2": MODELES[ordres[0][b]],
                        "d": DONNEES[ordres[1][a]], "d2": DONNEES[ordres[1][b]],
                        "q": MESURES[ordres[2][a]], "q2": MESURES[ordres[2][b]],
                        "v": INTERVENTIONS[ordres[3][a]]})
    return sorties


def majuscule(texte: str) -> str:
    return texte[:1].upper() + texte[1:]


def titre(e: dict) -> str:
    return f"Effect of {e['v']} on {e['q']} for {e['m']}"


def champ_controles(rng, sources: list, combien: int) -> tuple:
    """`combien` contrôles numérotés ; `sources` donne, pour chaque rang, l'expérience dont le contrôle parle."""
    gabarits = rng.permutation(len(CONTROLES))[:combien]
    phrases = [majuscule(CONTROLES[g][0].format(**sources[i])) for i, g in enumerate(gabarits)]
    return " ".join(f"({i + 1}) {p}" for i, p in enumerate(phrases)), [int(g) for g in gabarits]


def champ_proposition(rng, e: dict, fixe: int, bornes: tuple, ajout: str = "") -> str:
    """Phrases ajoutées tant que l'action reste sous la borne haute ; arrêt dès la borne basse franchie."""
    bas, haut = bornes
    retenues = [PHRASES_PROPOSITION[0].format(**e)] + ([ajout] if ajout else [])
    for g in rng.permutation(np.arange(1, len(PHRASES_PROPOSITION))):
        if fixe + len(" ".join(retenues)) >= bas:
            break
        phrase = majuscule(PHRASES_PROPOSITION[g].format(**e))
        if fixe + len(" ".join(retenues + [phrase])) <= haut:
            retenues.append(phrase)
    texte = " ".join(retenues)
    if not bas <= fixe + len(texte) <= haut:
        raise SystemExit(f"longueur {fixe + len(texte)} hors des bornes {bornes}")
    return texte


def action_appariement(rng, longueur: str, cas: str, accolades: bool) -> dict:
    e, autre = tirer_experiences(rng, 2)
    n = NOMBRE_CONTROLES[longueur]
    if cas == "apparie":
        sources = [e] * n
    elif cas == "desapparie":
        sources = [autre] * n
    else:
        melange = [e] * (n // 2) + [autre] * (n - n // 2)
        sources = [melange[i] for i in rng.permutation(n)]
    controles, _ = champ_controles(rng, sources, n)
    le_titre = titre(e)
    ajout = "We sweep the mixing weight over {0.1, 0.3, 1.0}." if accolades else ""
    proposition = champ_proposition(rng, e, len(le_titre) + len(controles), BORNES[longueur], ajout)
    return {"title": le_titre, "proposal": proposition, "controls": controles,
            "caracteres": len(le_titre) + len(proposition) + len(controles)}


def action_du_plan(rng, e: dict, longueur: str, controles_imposes: list, accolades: bool) -> str:
    """Texte d'une action du plan (six champs) ; `controles_imposes` : phrases de contrôle à écrire d'abord."""
    n = max(NOMBRE_CONTROLES_PLAN[longueur], len(controles_imposes))
    libres, _ = (champ_controles(rng, [e] * (n - len(controles_imposes)), n - len(controles_imposes))
                 if n > len(controles_imposes) else ("", []))
    phrases = list(controles_imposes) + [p.split(") ", 1)[1] for p in re.split(r" (?=\(\d+\) )", libres) if p]
    if accolades:
        phrases[-1] = phrases[-1].rstrip(".") + ", with seeds {11, 23, 47}."
    controles = " ".join(f"({i + 1}) {p}" for i, p in enumerate(phrases))
    prediction = majuscule(PREDICTIONS[int(rng.integers(len(PREDICTIONS)))].format(**e))
    cout = f"{int(rng.integers(2, 40))} GPU-hours"
    le_titre = titre(e)
    squelette = "ACTION: add\nTITLE: {t}\nPROPOSAL: {p}\nCONTROLS: {c}\nCOST: {k}\nPREDICTION: {r}"
    fixe = len(squelette.format(t=le_titre, p="", c=controles, k=cout, r=prediction))
    proposition = champ_proposition(rng, e, fixe, BORNES[longueur])
    return squelette.format(t=le_titre, p=proposition, c=controles, k=cout, r=prediction)


def entree_couverture(rng, longueur: str, n_reference: int, accolades: bool) -> dict:
    """Plan de dix actions et référence de `n_reference` contrôles, dont la moitié (arrondie au-dessus) est écrite."""
    experiences = tirer_experiences(rng, 6)
    du_plan, hors_plan = experiences[:5], experiences[5]
    ecrits = (n_reference + 1) // 2
    gabarits = [int(g) for g in rng.permutation(len(CONTROLES))[:n_reference]]
    porteuses = [int(a) for a in rng.permutation(10)[:ecrits]]
    imposes = {a: [] for a in range(10)}
    reference, verite = [], []
    for rang, g in enumerate(gabarits):
        ident = f"c{rang + 1}"
        if rang < ecrits:
            e = du_plan[porteuses[rang] % 5]
            imposes[porteuses[rang]].append(majuscule(CONTROLES[g][0].format(**e)))
            verite.append({"id": ident, "ecrit": True, "action": porteuses[rang] + 1})
        else:
            e = hors_plan
            verite.append({"id": ident, "ecrit": False, "action": None})
        reference.append(f"- id: {ident} | description: {majuscule(CONTROLES[g][1].format(**e))}")
    # Un contrôle « non écrit » ne doit paraître dans aucune action : ses éléments sont ceux de l'expérience hors plan.
    actions = [action_du_plan(rng, du_plan[a % 5], longueur, imposes[a], accolades and a == 0) for a in range(10)]
    plan = "\n\n".join(actions)
    return {"plan": plan, "reference": "\n".join(reference), "identifiants": [f"c{r + 1}" for r in range(n_reference)],
            "n_controles": n_reference, "construction": verite,
            "caracteres_par_action": [len(a) for a in actions], "caracteres": len(plan)}


def fabriquer(texte_prereg: str) -> dict:
    consignes = {nom: extraire_consigne(texte_prereg, nom) for nom in LIGNES_CONSIGNE}
    entrees, rang = [], 0

    def graine():
        nonlocal rang
        rang += 1
        return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(rang,))), rang

    # Appariement : bloc b, longueur l -> cas (l + b) mod 3 et (l + b + 1) mod 3 ; chaque bloc porte chaque longueur et
    # chaque cas deux fois ; sur les trois blocs, chaque couple (longueur, cas) paraît deux fois.
    for bloc in range(3):
        numero = 0
        for l, longueur in enumerate(LONGUEURS):
            for decalage in (0, 1):
                cas = CAS[(l + bloc + decalage) % 3]
                rng, cle = graine()
                numero += 1
                accolades = (bloc == 0 and longueur == "mediane" and decalage == 0)
                corps = action_appariement(rng, longueur, cas, accolades)
                entrees.append({"id": f"A-b{bloc + 1}-{numero:02d}", "instrument": "appariement", "bloc": bloc + 1,
                                "longueur": longueur, "cas": cas, "accolades": accolades,
                                "graine": {"entropie": ENTROPIE, "cle": [cle]}, **corps})
    # Couverture : deux blocs de trois (une longueur chacun) ; nombre de contrôles de la référence par rotation.
    rotation = {0: {"courte": 3, "mediane": 4, "longue": 6}, 1: {"courte": 6, "mediane": 3, "longue": 4}}
    for bloc in range(2):
        for numero, longueur in enumerate(LONGUEURS, start=1):
            rng, cle = graine()
            accolades = (bloc == 0 and longueur == "mediane")
            corps = entree_couverture(rng, longueur, rotation[bloc][longueur], accolades)
            entrees.append({"id": f"C-b{bloc + 1}-{numero:02d}", "instrument": "couverture", "bloc": bloc + 1,
                            "longueur": longueur, "accolades": accolades,
                            "graine": {"entropie": ENTROPIE, "cle": [cle]}, **corps})
    for e in entrees:
        if e["instrument"] == "appariement":
            valeurs = {"{title}": e["title"], "{proposal}": e["proposal"], "{controls}": e["controls"]}
        else:
            valeurs = {"{plan}": e["plan"], "{reference}": e["reference"]}
        rempli = remplir(consignes[e["instrument"]], valeurs).encode("utf-8")
        e["consigne_remplie"] = {"octets": len(rempli), "sha256": hashlib.sha256(rempli).hexdigest()}
    par_bloc = lambda instrument, bloc: [e["id"] for e in entrees if e["instrument"] == instrument and e["bloc"] == bloc]
    ordre = (par_bloc("appariement", 1) + par_bloc("couverture", 1) + par_bloc("appariement", 2)
             + par_bloc("couverture", 2) + par_bloc("appariement", 3))
    return {
        "version": VERSION,
        "objet": "24 textes synthétiques de l'essai de mesure des lecteurs du bras A : aucune tâche, aucune référence "
                 "cachée, aucun épisode ; lexique inventé",
        "numpy": np.__version__,
        "entropie": ENTROPIE,
        "consignes": {nom: {"source": PREREG, "lignes": list(LIGNES_CONSIGNE[nom]), "caracteres": len(c),
                            "sha256": EMPREINTES_CONSIGNE[nom], "marques": list(MARQUES[nom])}
                      for nom, c in consignes.items()},
        "ordre": ordre,
        "entrees": entrees,
    }


def principal(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    a.add_argument("--sortie", default=str(RACINE / SORTIE))
    a.add_argument("--prereg", default=str(RACINE / PREREG))
    args = a.parse_args(argv)
    lot = fabriquer(Path(args.prereg).read_text(encoding="utf-8"))
    sortie = Path(args.sortie)
    if sortie.exists():
        print(f"refus : {sortie} existe déjà (R12 : jamais écrasé)", file=sys.stderr)
        return 2
    sortie.parent.mkdir(parents=True, exist_ok=True)
    octets = (json.dumps(lot, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(sortie, "xb") as f:
        f.write(octets)
    print(json.dumps({"sortie": str(sortie), "entrees": len(lot["entrees"]), "sha256": hashlib.sha256(octets).hexdigest()},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
