#!/usr/bin/env python3
"""Construit `pieces/consigne-proposeur-kirchner-v1.md` en ENCHÂSSANT, octet pour octet, les textes servis de conv-audit — v1.

Rédigé le 3 novembre 2026 (sous-agent de session-depot) ; aucun appel, aucune dépense. Dérivé de
`construire_consigne_proposeur_heimersheim_v1.py`. Rien n'est réécrit : la consigne est (1) un en-tête du rédacteur (rôle,
repère de consigne), (2) les quatre sections servies de `pieces/conv-audit/question-ideation-kirchner-v1.md` — « La
question… », « Ce qu'on attend des proposeurs », « Ce qui est déjà pris », « Règles d'intégrité » —, recopiées telles
quelles (de la ligne « ## La question » à la ligne qui précède « ## Lecture prévue de la sortie »), (3) la pièce
`piece-kirchner-v2.md` en entier, (4) la pièce `piece-nos-resultats-v1.md` en entier, dans cet ordre, (5) le livrable du
rédacteur (8 fiches, champs). Ne sont PAS servis : titre et provenance de la question, « Lecture prévue de la sortie » et
« Pièces jointes prévues » (la question les dit non servis). Les trois sources sont vérifiées à leur empreinte. Jamais écrasé
(R12) ; `--verifier FICHIER` refait la construction et compare à l'octet.

  python3 -I -B construire_consigne_proposeur_kirchner_v1.py --sortie pieces/consigne-proposeur-kirchner-v1.md
  python3 -I -B construire_consigne_proposeur_kirchner_v1.py --verifier pieces/consigne-proposeur-kirchner-v1.md
"""

import argparse
import hashlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
CA = os.path.join(ICI, "pieces", "conv-audit")
SOURCES = (("question-ideation-kirchner-v1.md", "291f91f882d9a130570b1da600212f07435ec19cb87b9e9d65380a5c4c650253"),
           ("piece-kirchner-v2.md", "6e7fb1c56cb292aa97667f11093959f775f940b06dc85d8038e728813e4203f5"),
           ("piece-nos-resultats-v1.md", "d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c"))
CANARI = "KQ2-PROPOSEUR-59114cf4"
DEBUT_SECTIONS = "## La question, telle que le mentor la pose"
FIN_SECTIONS = "## Lecture prévue de la sortie"
AXES = ("probleme_peu_couvert", "rappel_apres_selection", "transfert_hors_banc", "lien_non_fait")

EN_TETE = f"""# Consigne du proposeur — course d'idéation sur la question 2 du mentor Kirchner (v1)

Repère de consigne (à ne pas recopier) : {CANARI}

Tu proposes des fiches d'idéation au niveau méthode, en français. Ci-dessous, sans retouche : la question servie (quatre
sections), puis la pièce « Kirchner » en entier, puis la pièce « nos résultats » en entier. Le livrable vient en dernier.

=== QUESTION SERVIE (texte repris tel quel) ===

"""

ENTRE_1 = """
=== FIN DE LA QUESTION SERVIE ===

=== PIÈCE « KIRCHNER » (texte entier, repris tel quel) ===

"""

ENTRE_2 = """
=== FIN DE LA PIÈCE « KIRCHNER » ===

=== PIÈCE « NOS RÉSULTATS » (texte entier, repris tel quel) ===

"""

LIVRABLE = """
=== FIN DE LA PIÈCE « NOS RÉSULTATS » ===

## Livrable

Exactement **huit fiches**, distinctes entre elles, dans **un seul bloc JSON** à la fin de ta réponse, de la forme :

```json
{"fiches": [
  {"titre": "…", "probleme": "…", "sous_estime": "…", "hypothese": "…", "axe": "…", "premiere_experience": "…", "changer_d_avis": "…", "test_de_mort": "…", "cout": "…"}
]}
```

Champs (tous obligatoires, non vides, en texte) :

- `titre` : au plus 80 caractères ;
- `probleme` : le problème ouvert d'alignement, et ce qu'il touche de ce que Kirchner construit (classement, moniteur de triche,
  banc tenu à l'écart, Petri, harnais ouvert, ou ses remèdes déclarés) et de nos travaux publics ;
- `sous_estime` : pourquoi il est sous-estimé, la différence exacte avec le travail publié le plus proche, et comment le
  vérifier (quelles requêtes ou quels travaux montreraient qu'il est déjà pris) ;
- `hypothese` : l'hypothèse falsifiable et l'effet prédit avec son signe, en une ou deux phrases ;
- `axe` : exactement une des quatre valeurs, qui reprennent les demandes 1 à 4 « particulièrement bienvenues » de la question,
  dans leur ordre : `probleme_peu_couvert` (1), `rappel_apres_selection` (2), `transfert_hors_banc` (3), `lien_non_fait` (4) ;
- `premiere_experience` : la première expérience, faisable en quelques jours sur notre organisme public, sur un modèle de
  8 milliards de paramètres à poids ouverts (Llama-3.1-8B-Instruct) ou sur le harnais ouvert de Kirchner (demande 5) ;
- `changer_d_avis` : le résultat chiffré, avec son signe et son seuil, qui ferait changer d'avis, énoncé d'avance ;
- `test_de_mort` : la mesure qui tuerait l'hypothèse — le nombre qui, lu une seule fois, la réfute ;
- `cout` : le coût de la première expérience (jours, heures de calcul, mémoire), marqué « supposé » s'il n'est pas calculé.

N'ajoute aucun autre champ dans les fiches. Aucune fiche ne nomme un modèle qui l'aurait écrite.
"""


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def lire_verifie(nom, attendu):
    p = os.path.join(CA, nom)
    vu = sha(p)
    if vu != attendu:
        raise SystemExit(f"{nom} : empreinte {vu[:12]}… ≠ {attendu[:12]}… : refus (texte servi modifié)")
    with open(p, "rb") as f:
        return f.read().decode("utf-8")


def sections_question(texte):
    i, j = texte.find("\n" + DEBUT_SECTIONS), texte.find("\n" + FIN_SECTIONS)
    if i < 0 or j < 0 or j <= i:
        raise SystemExit("question : sections attendues introuvables (structure changée) : refus")
    return texte[i + 1:j + 1]


def construire():
    q, k, n = (lire_verifie(nom, s) for nom, s in SOURCES)
    return EN_TETE + sections_question(q) + ENTRE_1 + k + ENTRE_2 + n + LIVRABLE


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
