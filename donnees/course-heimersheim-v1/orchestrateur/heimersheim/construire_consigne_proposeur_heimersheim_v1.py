#!/usr/bin/env python3
"""Construit `pieces/consigne-proposeur-heimersheim-v1.md` en ENCHÂSSANT, octet pour octet, les textes servis de conv-audit — v1.

Rédigé le 3 novembre 2026 (sous-agent de session-depot) ; aucun appel, aucune dépense. Rien n'est réécrit : la consigne est
(1) un en-tête du rédacteur (rôle, repère de consigne), (2) les sections « La question… », « Ce qu'on attend des
proposeurs » et « Règles d'intégrité… » de `pieces/conv-audit/question-ideation-heimersheim-v1.md`, recopiées telles quelles
(de la ligne « ## La question » à la ligne qui précède « ## Lecture prévue de la sortie »), (3) la pièce
`pieces/conv-audit/piece-etat-de-l-art-pilotage-conscience-evaluation-v1.md` en entier, telle quelle, (4) le livrable du
rédacteur (8 fiches, champs). Ne sont PAS servis : le titre et le paragraphe de provenance de la question, et sa section
« Lecture prévue de la sortie » (adressée au lecteur de la sortie, pas aux proposeurs) — écart déclaré au LISEZMOI.

Les deux sources sont vérifiées à leur empreinte (compagnons `.sha256` de conv-audit). Le fichier produit n'est jamais
écrasé (R12) : `--sortie` doit être neuf. `--verifier FICHIER` refait la construction en mémoire et compare à l'octet.

  python3 -I -B construire_consigne_proposeur_heimersheim_v1.py --sortie pieces/consigne-proposeur-heimersheim-v1.md
  python3 -I -B construire_consigne_proposeur_heimersheim_v1.py --verifier pieces/consigne-proposeur-heimersheim-v1.md
"""

import argparse
import hashlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
QUESTION = os.path.join(ICI, "pieces", "conv-audit", "question-ideation-heimersheim-v1.md")
PIECE = os.path.join(ICI, "pieces", "conv-audit", "piece-etat-de-l-art-pilotage-conscience-evaluation-v1.md")
SHA_QUESTION = "e9528e254e2dcad9506e323d3bcd9101e458628dd9c6dabfa4e96174ce660007"
SHA_PIECE = "6445fd6f9dae33500b628bdeff354ed2c7b75bd50d05cbd2aef08c3e6ce49162"
CANARI = "HQ1-PROPOSEUR-2fc47821"
DEBUT_SECTIONS = "## La question, telle que le mentor la pose"
FIN_SECTIONS = "## Lecture prévue de la sortie"
AXES = ("raison_echec_absente", "evaluation_contre_registre", "residu_non_verbalise", "lien_objets_non_relies",
        "prediction_chiffree_8b")

EN_TETE = f"""# Consigne du proposeur — course d'idéation sur la question 1 du mentor Heimersheim (v1)

Repère de consigne (à ne pas recopier) : {CANARI}

Tu proposes des fiches d'idéation au niveau méthode, en français. Ci-dessous, sans retouche : la question servie (trois
sections), puis la pièce servie en entier. Le livrable vient en dernier.

=== QUESTION SERVIE (texte repris tel quel) ===

"""

ENTRE = """
=== FIN DE LA QUESTION SERVIE ===

=== PIÈCE SERVIE (texte entier, repris tel quel) ===

"""

LIVRABLE = """
=== FIN DE LA PIÈCE SERVIE ===

## Livrable

Exactement **huit fiches**, distinctes entre elles, dans **un seul bloc JSON** à la fin de ta réponse, de la forme :

```json
{"fiches": [
  {"titre": "…", "hypothese": "…", "axe": "…", "epreuve": "…", "controle": "…", "prediction": "…", "test_de_mort": "…", "cout": "…"}
]}
```

Champs (tous obligatoires, non vides, en texte) :

- `titre` : au plus 80 caractères ;
- `hypothese` : l'hypothèse falsifiable et l'effet prédit, en une ou deux phrases ;
- `axe` : exactement une des cinq valeurs, qui reprennent les cinq demandes « particulièrement bienvenues » de la question,
  dans leur ordre : `raison_echec_absente` (1), `evaluation_contre_registre` (2), `residu_non_verbalise` (3),
  `lien_objets_non_relies` (4), `prediction_chiffree_8b` (5) ;
- `epreuve` : l'expérience ou la mesure proposée (modèle, intervention, dose, lecture), au niveau méthode ;
- `controle` : ce qui sépare l'effet cherché d'un effet générique (perturbation de même norme, direction sans rapport, paire de
  registre à statut d'évaluation constant, ou autre), et pourquoi il est exigeant ;
- `prediction` : une prédiction chiffrée, avec son signe et un intervalle, marquée « supposé » (ou « calcul ») ;
- `test_de_mort` : la mesure qui tuerait l'hypothèse — le nombre qui, lu une seule fois, la réfute ;
- `cout` : le coût sur Llama-3.1-8B-Instruct ou sur processeur (jours, heures de calcul, mémoire), marqué « supposé » s'il
  n'est pas calculé.

N'ajoute aucun autre champ dans les fiches. Aucune fiche ne nomme un modèle qui l'aurait écrite.
"""


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def lire_verifie(chemin, attendu):
    vu = sha(chemin)
    if vu != attendu:
        raise SystemExit(f"{chemin} : empreinte {vu[:12]}… ≠ {attendu[:12]}… : refus (texte servi modifié)")
    with open(chemin, "rb") as f:
        return f.read().decode("utf-8")


def sections_question(texte):
    """Les trois sections servies, à l'octet : de « ## La question » jusqu'avant « ## Lecture prévue de la sortie »."""
    i, j = texte.find("\n" + DEBUT_SECTIONS), texte.find("\n" + FIN_SECTIONS)
    if i < 0 or j < 0 or j <= i:
        raise SystemExit("question : sections attendues introuvables (structure changée) : refus")
    return texte[i + 1:j + 1]


def construire():
    q = lire_verifie(QUESTION, SHA_QUESTION)
    p = lire_verifie(PIECE, SHA_PIECE)
    return EN_TETE + sections_question(q) + ENTRE + p + LIVRABLE


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = a.add_mutually_exclusive_group(required=True)
    g.add_argument("--sortie")
    g.add_argument("--verifier")
    args = a.parse_args(argv)
    texte = construire()
    if args.verifier:
        with open(args.verifier, "rb") as f:
            ok = f.read() == texte.encode("utf-8")
        print("conforme" if ok else "DIFFÉRENT")
        return 0 if ok else 3
    if os.path.exists(args.sortie):
        raise SystemExit(f"{args.sortie} existe déjà (R12) : refus")
    with open(args.sortie, "wb") as f:
        f.write(texte.encode("utf-8"))
    print(f"écrit : {args.sortie} ({sha(args.sortie)})")
    return 0


if __name__ == "__main__":
    sys.exit(principal())
