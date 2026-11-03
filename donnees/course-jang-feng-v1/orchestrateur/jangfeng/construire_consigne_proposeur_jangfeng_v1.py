#!/usr/bin/env python3
"""KIT JANG-FENG, v1 (sous-agent de session-depot, 3 novembre 2026) : dérivé du kit Ibrahim v2 (outils/course-ibrahim-q1-v1, 965eb21b) par substitution de noms et par les changements de la course Jang-Feng (question à une section servie et ses règles d'intégrité, deux pièces servies, trois variantes comme Ibrahim, juge du n° 419, marge d'appels 2 × plan + 5). Pièces : piece-jang-feng-v1.md, piece-nos-resultats-v1.md.
Construit `pieces/consigne-proposeur-jangfeng-v1.md` en ENCHÂSSANT, octet pour octet, les textes servis de conv-audit — v1.

Rédigé le 3 novembre 2026 (sous-agent de session-depot) ; aucun appel, aucune dépense. Dérivé de
`construire_consigne_proposeur_kirchner_v1.py` (kit Kirchner Q2). Rien n'est réécrit : la consigne est (1) un en-tête du
rédacteur (rôle, repère de consigne), (2) deux sections de `pieces/conv-audit/question-collisionneur-jangfeng-v1.md`, telles
quelles : « La question, telle que le mentor la pose » (jusqu'avant « ## Ce qu'on attend de chaque espèce ») et « Règles
d'intégrité » (jusqu'avant « ## Lecture prévue de la sortie ») — la section « Ce qu'on attend de chaque espèce », propre au
collisionneur, est remplacée par le livrable du kit (spécification de la course, § 1) —, (3) `piece-jangfeng-v1.md`,
(4) `piece-sycophancie-publique-v1.md`, (5) `piece-nos-resultats-v1.md`, en entier, dans cet ordre (n° 417 de conv-audit),
(6) le livrable (6 fiches, champs du kit). Les sources sont vérifiées à leur empreinte. Jamais écrasé (R12) ; `--verifier`
refait la construction et compare à l'octet.

  python3 -I -B construire_consigne_proposeur_jangfeng_v1.py --sortie pieces/consigne-proposeur-jangfeng-v1.md
  python3 -I -B construire_consigne_proposeur_jangfeng_v1.py --verifier pieces/consigne-proposeur-jangfeng-v1.md
"""

import argparse
import hashlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
CA = os.path.join(ICI, "pieces", "conv-audit")
QUESTION = ('question-course-jang-feng-v1.md', 'd68c6c5ca567c2a867c9a0eb0e64d7b7340af0414e0f382c19416d67ab63c10e')
PIECES = (('piece-jang-feng-v1.md', '1f42364322988bf591ead6ce41842dd389ab179b11bc27853d66750ab5196774', 'PIÈCE « FENG ET JANG »'),
          ('piece-nos-resultats-v1.md', 'd6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c', 'PIÈCE « NOS RÉSULTATS »'),
          )
CANARI = 'JF1-PROPOSEUR-1f530111'
SECTIONS = (('## La question, telle que les mentors la posent', "## Règles d'intégrité"),
            ("## Règles d'intégrité", None))  # None : jusqu'à la fin du texte
AXES = ('valeur_pour_l_audit', 'limite_actuelle', 'comparaison_a_la_boite_noire')

EN_TETE = f"""# Consigne du proposeur — course d'idéation sur la question des mentors Feng et Jang (v1)

Repère de consigne (à ne pas recopier) : {CANARI}

Tu proposes des fiches d'idéation au niveau méthode, en français. Ci-dessous, sans retouche : deux sections de la question
servie (la question, puis les règles d'intégrité), puis deux pièces en entier. Le livrable vient en dernier.

=== QUESTION SERVIE (deux sections, reprises telles quelles) ===

"""

LIVRABLE = """
## Livrable

Exactement **six fiches**, distinctes entre elles : chacune est **une affirmation falsifiable** sur la valeur ou une limite des
moniteurs et des méthodes d'audit en boîte blanche (lecture des activations, sondes, autoencodeurs épars, élicitation par les
poids), avec l'expérience qui la tranche, son témoin et le résultat qui la tuerait, dans **un seul bloc JSON** à la fin de ta
réponse, de la forme :

```json
{"fiches": [
  {"titre": "…", "hypothese": "…", "axe": "…", "epreuve": "…", "controle": "…", "prediction": "…", "test_de_mort": "…", "cout": "…"}
]}
```

Champs (tous obligatoires, non vides, en texte) :

- `titre` : au plus 80 caractères ;
- `hypothese` : l'affirmation falsifiable sur la valeur ou une limite d'une méthode boîte blanche, et ce qu'elle ajoute aux
  travaux des mentors (pièce « Feng et Jang », section 1) ;
- `axe` : exactement une des trois valeurs, tirées de la question : `valeur_pour_l_audit` (ce que la boîte blanche apporte à
  l'audit), `limite_actuelle` (une limite actuelle), `comparaison_a_la_boite_noire` (ce qu'elle ajoute ou non à la boîte noire) ;
- `epreuve` : l'expérience qui la tranche : méthode boîte blanche, modèle ouvert ou organisme public de la pièce, jeu
  d'évaluation, ligne de base ;
- `controle` : **le témoin** (boîte noire, organisme bénin, ligne de base calibrée), une chose qui rendrait le résultat
  trompeur et le contrôle qui la détecterait ;
- `prediction` : le résultat attendu, chiffré, avec son signe et un intervalle, marqué « supposé » (ou « calcul ») ;
- `test_de_mort` : **le résultat qui la tuerait** — le nombre qui, lu une seule fois, la réfute ;
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
        i, j = texte.find("\n" + debut), (texte.find("\n" + fin) if fin else len(texte) - 1)
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
