#!/usr/bin/env python3
"""Construit `pieces/consigne-proposeur-ibrahim-v1.md` en ENCHÂSSANT, octet pour octet, les textes servis de conv-audit — v1.

Rédigé le 3 novembre 2026 (sous-agent de session-depot) ; aucun appel, aucune dépense. Dérivé de
`construire_consigne_proposeur_kirchner_v1.py` (kit Kirchner Q2). Rien n'est réécrit : la consigne est (1) un en-tête du
rédacteur (rôle, repère de consigne), (2) deux sections de `pieces/conv-audit/question-collisionneur-ibrahim-v1.md`, telles
quelles : « La question, telle que le mentor la pose » (jusqu'avant « ## Ce qu'on attend de chaque espèce ») et « Règles
d'intégrité » (jusqu'avant « ## Lecture prévue de la sortie ») — la section « Ce qu'on attend de chaque espèce », propre au
collisionneur, est remplacée par le livrable du kit (spécification de la course, § 1) —, (3) `piece-ibrahim-v1.md`,
(4) `piece-sycophancie-publique-v1.md`, (5) `piece-nos-resultats-v1.md`, en entier, dans cet ordre (n° 417 de conv-audit),
(6) le livrable (6 fiches, champs du kit). Les sources sont vérifiées à leur empreinte. Jamais écrasé (R12) ; `--verifier`
refait la construction et compare à l'octet.

  python3 -I -B construire_consigne_proposeur_ibrahim_v1.py --sortie pieces/consigne-proposeur-ibrahim-v1.md
  python3 -I -B construire_consigne_proposeur_ibrahim_v1.py --verifier pieces/consigne-proposeur-ibrahim-v1.md
"""

import argparse
import hashlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
CA = os.path.join(ICI, "pieces", "conv-audit")
QUESTION = ("question-collisionneur-ibrahim-v1.md", "5e905798a512db9fb9c607be0fbe74972d7df618cf8b9026c23eb0bc8ed6d9c0")
PIECES = (("piece-ibrahim-v1.md", "4e3851e3816fc3afaa573693f8f3d0aa2b9fc6c0e726ae54bab8cd4a248d6149", "PIÈCE « IBRAHIM »"),
          ("piece-sycophancie-publique-v1.md", "9e424a025280908baf5e2eec65f285a746f92ce14991cdc5d7d80cb5978716b8",
           "PIÈCE « SYCOPHANCIE, RÉSULTATS PUBLICS »"),
          ("piece-nos-resultats-v1.md", "d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c", "PIÈCE « NOS RÉSULTATS »"))
CANARI = "IQ1-PROPOSEUR-099875e1"
SECTIONS = (("## La question, telle que le mentor la pose", "## Ce qu'on attend de chaque espèce"),
            ("## Règles d'intégrité", "## Lecture prévue de la sortie"))
AXES = ("tenue_de_la_persona", "sycophancie_apres_rl", "mesure_et_juge", "resultat_trompeur")

EN_TETE = f"""# Consigne du proposeur — course d'idéation sur la question 1 de la mentore Ibrahim (v1)

Repère de consigne (à ne pas recopier) : {CANARI}

Tu proposes des fiches d'idéation au niveau méthode, en français. Ci-dessous, sans retouche : deux sections de la question
servie (la question, puis les règles d'intégrité), puis trois pièces en entier. Le livrable vient en dernier.

=== QUESTION SERVIE (deux sections, reprises telles quelles) ===

"""

LIVRABLE = """
## Livrable

Exactement **six fiches**, distinctes entre elles : chacune est une **première expérience** candidate pour la question de la
mentore, dans **un seul bloc JSON** à la fin de ta réponse, de la forme :

```json
{"fiches": [
  {"titre": "…", "hypothese": "…", "axe": "…", "epreuve": "…", "controle": "…", "prediction": "…", "test_de_mort": "…", "cout": "…"}
]}
```

Champs (tous obligatoires, non vides, en texte) :

- `titre` : au plus 80 caractères ;
- `hypothese` : l'hypothèse falsifiable, et ce que l'expérience ajoute aux travaux de la mentore (pièce « Ibrahim », section 1) ;
- `axe` : exactement une des quatre valeurs, tirées de la question : `tenue_de_la_persona` (la persona installée par
  entraînement de caractère tient-elle après un apprentissage par renforcement), `sycophancie_apres_rl` (qu'advient-il de la
  sycophancie), `mesure_et_juge` (ce qu'on mesure et avec quel juge), `resultat_trompeur` (ce qui rendrait le résultat trompeur) ;
- `epreuve` : ce qu'on entraîne ou mesure (modèle et points de contrôle publiés, étape d'apprentissage par renforcement, jeu
  d'évaluation, juge) ;
- `controle` : **une chose qui rendrait le résultat trompeur**, et l'expérience de contrôle qui la détecterait ;
- `prediction` : le résultat attendu, chiffré, avec son signe et un intervalle, marqué « supposé » (ou « calcul ») ;
- `test_de_mort` : la mesure qui tuerait l'hypothèse — le nombre qui, lu une seule fois, la réfute ;
- `cout` : le coût en jours et en heures de carte, marqué « supposé » s'il n'est pas calculé.

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
    morceaux = []
    for debut, fin in SECTIONS:
        i, j = texte.find("\n" + debut), texte.find("\n" + fin)
        if i < 0 or j < 0 or j <= i:
            raise SystemExit("question : sections attendues introuvables (structure changée) : refus")
        morceaux.append(texte[i + 1:j + 1])
    return morceaux


def construire():
    q = lire_verifie(*QUESTION)
    s = EN_TETE + "\n".join(sections_question(q)) + "\n=== FIN DE LA QUESTION SERVIE ===\n"
    for nom, empreinte, titre in PIECES:
        s += f"\n=== {titre} (texte entier, repris tel quel) ===\n\n" + lire_verifie(nom, empreinte) + f"\n=== FIN DE LA {titre} ===\n"
    return s + LIVRABLE


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
