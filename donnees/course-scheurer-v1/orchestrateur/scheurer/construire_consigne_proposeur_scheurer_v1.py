#!/usr/bin/env python3
"""KIT SCHEURER, v1 (sous-agent de session-depot, 3 novembre 2026) : dérivé du kit Ibrahim v2 (outils/course-ibrahim-q1-v1, 965eb21b) par substitution de noms et par les changements de la course Scheurer (deux pièces servies, cinq variantes dont trois sans Opus proposeur, jeu de rôles par variante (Opus ou Fable), garde lexicale sans « gemini » ni « openai », juge du n° 419, marge d'appels 2 × plan + 5). Pièces : piece-scheurer-v1.md, piece-nos-resultats-v1.md.
Construit `pieces/consigne-proposeur-scheurer-v1.md` en ENCHÂSSANT, octet pour octet, les textes servis de conv-audit — v1.

Rédigé le 3 novembre 2026 (sous-agent de session-depot) ; aucun appel, aucune dépense. Dérivé de
`construire_consigne_proposeur_kirchner_v1.py` (kit Kirchner Q2). Rien n'est réécrit : la consigne est (1) un en-tête du
rédacteur (rôle, repère de consigne), (2) deux sections de `pieces/conv-audit/question-collisionneur-scheurer-v1.md`, telles
quelles : « La question, telle que le mentor la pose » (jusqu'avant « ## Ce qu'on attend de chaque espèce ») et « Règles
d'intégrité » (jusqu'avant « ## Lecture prévue de la sortie ») — la section « Ce qu'on attend de chaque espèce », propre au
collisionneur, est remplacée par le livrable du kit (spécification de la course, § 1) —, (3) `piece-scheurer-v1.md`,
(4) `piece-sycophancie-publique-v1.md`, (5) `piece-nos-resultats-v1.md`, en entier, dans cet ordre (n° 417 de conv-audit),
(6) le livrable (6 fiches, champs du kit). Les sources sont vérifiées à leur empreinte. Jamais écrasé (R12) ; `--verifier`
refait la construction et compare à l'octet.

  python3 -I -B construire_consigne_proposeur_scheurer_v1.py --sortie pieces/consigne-proposeur-scheurer-v1.md
  python3 -I -B construire_consigne_proposeur_scheurer_v1.py --verifier pieces/consigne-proposeur-scheurer-v1.md
"""

import argparse
import hashlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
CA = os.path.join(ICI, "pieces", "conv-audit")
QUESTION = ('question-collisionneur-scheurer-v1.md', 'edb1d5f130c9e60cfc35b12ba6a4fb83ce2c9805cd8ad91085d5c1f1aab5f930')
PIECES = (('piece-scheurer-v1.md', '2d0e60fc78e5930fb4ad1fe60d6fba8f2a17f4a03729570ea896db0c339f3796', 'PIÈCE « SCHEURER »'),
          ('piece-nos-resultats-v1.md', 'd6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c', 'PIÈCE « NOS RÉSULTATS »'),
          )
CANARI = 'SCH-PROPOSEUR-6cffc79c'
SECTIONS = (('## La question, telle que le mentor la pose', "## Ce qu'on attend de chaque espèce"),
            ("## Règles d'intégrité", "## Lecture prévue de la sortie"))
AXES = ('propension_mal_alignee', 'capacite_mal_alignee', 'surveillance_et_controle', 'essaim_multi_agents')

EN_TETE = f"""# Consigne du proposeur — course d'idéation sur la question du mentor Scheurer (v1)

Repère de consigne (à ne pas recopier) : {CANARI}

Tu proposes des fiches d'idéation au niveau méthode, en français. Ci-dessous, sans retouche : deux sections de la question
servie (la question, puis les règles d'intégrité), puis deux pièces en entier. Le livrable vient en dernier.

=== QUESTION SERVIE (deux sections, reprises telles quelles) ===

"""

LIVRABLE = """
## Livrable

Exactement **six fiches**, distinctes entre elles : chacune est **une tendance candidate** pour la question du mentor (la
question en demande trois à cinq : la course en demande six par espèce), dans **un seul bloc JSON** à la fin de ta réponse,
de la forme :

```json
{"fiches": [
  {"titre": "…", "hypothese": "…", "axe": "…", "epreuve": "…", "controle": "…", "prediction": "…", "test_de_mort": "…", "cout": "…"}
]}
```

Champs (tous obligatoires, non vides, en texte) :

- `titre` : au plus 80 caractères ;
- `hypothese` : la tendance énoncée (« [grandeur] croît ou décroît d'un facteur X par mois ou par an »), et ce qu'elle ajoute
  aux travaux du mentor (pièce « Scheurer », section 1) ;
- `axe` : exactement une des quatre valeurs, tirées de la question : `propension_mal_alignee` (une propension mal alignée :
  manigance, tromperie, désalignement), `capacite_mal_alignee` (la capacité de le faire), `surveillance_et_controle` (notre
  capacité à surveiller ou contrôler par un schéma donné), `essaim_multi_agents` (le désalignement d'un essaim d'agents) ;
- `epreuve` : la grandeur mesurée et pourquoi elle se mesure de la même façon d'un modèle à l'autre ; l'analogue de la durée
  humaine ou du calcul expérimental qui donne une échelle continue ; les modèles et leurs dates (combien, sur combien de mois) ;
  l'ajustement et l'incertitude sur le facteur ;
- `controle` : pourquoi la tendance a des chances de réussir là où une tendance de propension échoue ; ses menaces principales
  (élicitation, refus, plafond du juge, contamination, changement de moniteur) et le contrôle qui tient chacune ;
- `prediction` : l'énoncé attendu, chiffré et signé (facteur par mois ou par an, avec un intervalle), marqué « supposé » s'il
  n'est pas tiré des pièces ;
- `test_de_mort` : ce qui ferait échouer le plan, ou déclarer le premier pilote non concluant — le nombre qui, lu une seule
  fois, le réfute ;
- `cout` : le premier pilote (taille, coût en jours et en heures de carte ou en appels), marqué « supposé » s'il n'est pas calculé.

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
