#!/usr/bin/env python3
"""KIT COLOGNESE-WARD Q2, v1 (sous-agent de session-depot, 3 novembre 2026) : dérivé du kit Ibrahim v2 (outils/course-ibrahim-q1-v1, 965eb21b) par substitution de noms et par les changements de la course Colognese-Ward Q2 (deux pièces servies, trois variantes comme Ibrahim, garde lexicale sans « openai », juge du n° 419, marge d'appels 2 × plan + 5). Pièces : piece-colognese-ward-v1.md, piece-nos-resultats-v1.md.
Construit `pieces/consigne-proposeur-colognese-v1.md` en ENCHÂSSANT, octet pour octet, les textes servis de conv-audit — v1.

Rédigé le 3 novembre 2026 (sous-agent de session-depot) ; aucun appel, aucune dépense. Dérivé de
`construire_consigne_proposeur_kirchner_v1.py` (kit Kirchner Q2). Rien n'est réécrit : la consigne est (1) un en-tête du
rédacteur (rôle, repère de consigne), (2) deux sections de `pieces/conv-audit/question-collisionneur-colognese-v1.md`, telles
quelles : « La question, telle que le mentor la pose » (jusqu'avant « ## Ce qu'on attend de chaque espèce ») et « Règles
d'intégrité » (jusqu'avant « ## Lecture prévue de la sortie ») — la section « Ce qu'on attend de chaque espèce », propre au
collisionneur, est remplacée par le livrable du kit (spécification de la course, § 1) —, (3) `piece-colognese-v1.md`,
(4) `piece-sycophancie-publique-v1.md`, (5) `piece-nos-resultats-v1.md`, en entier, dans cet ordre (n° 417 de conv-audit),
(6) le livrable (6 fiches, champs du kit). Les sources sont vérifiées à leur empreinte. Jamais écrasé (R12) ; `--verifier`
refait la construction et compare à l'octet.

  python3 -I -B construire_consigne_proposeur_colognese_v1.py --sortie pieces/consigne-proposeur-colognese-v1.md
  python3 -I -B construire_consigne_proposeur_colognese_v1.py --verifier pieces/consigne-proposeur-colognese-v1.md
"""

import argparse
import hashlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
CA = os.path.join(ICI, "pieces", "conv-audit")
QUESTION = ('question-collisionneur-colognese-ward-v1.md', '06d837952cfe066a1414710fadda80f2624ac944c1d5c428b9073bb44686d6af')
PIECES = (('piece-colognese-ward-v1.md', '7533e4b58f03a5b8928ca2c411d8c29ee48f86e15e744afaf4b07e8a9b8f91b2', 'PIÈCE « COLOGNESE ET WARD »'),
          ('piece-nos-resultats-v1.md', 'd6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c', 'PIÈCE « NOS RÉSULTATS »'),
          )
CANARI = 'CW2-PROPOSEUR-9f1918d6'
SECTIONS = (('## La question, telle que les mentors la posent', "## Ce qu'on attend de chaque espèce"),
            ("## Règles d'intégrité", '## Lecture prévue de la sortie'))  # None : jusqu'à la fin du texte
AXES = ('changement_de_dispositif', 'resultat_le_plus_interessant', 'ce_que_le_billet_ne_dit_pas')

EN_TETE = f"""# Consigne du proposeur — course d'idéation sur la question 2 des mentors Colognese et Ward (v1)

Repère de consigne (à ne pas recopier) : {CANARI}

Tu proposes des fiches d'idéation au niveau méthode, en français. Ci-dessous, sans retouche : deux sections de la question
servie (la question, puis les règles d'intégrité), puis deux pièces en entier. Le livrable vient en dernier.

=== QUESTION SERVIE (deux sections, reprises telles quelles) ===

"""

LIVRABLE = """
## Livrable

Exactement **six fiches**, distinctes entre elles : chacune est **un changement de dispositif** précis et vérifiable, **ou le
résultat du billet** que tu tiens pour le plus intéressant avec l'expérience qui le confirmerait ou le tuerait (la question
demande trois à cinq changements et un résultat : la course demande six fiches par espèce), dans **un seul bloc JSON** à la fin
de ta réponse, de la forme :

```json
{"fiches": [
  {"titre": "…", "hypothese": "…", "axe": "…", "epreuve": "…", "controle": "…", "prediction": "…", "test_de_mort": "…", "cout": "…"}
]}
```

Champs (tous obligatoires, non vides, en texte) :

- `titre` : au plus 80 caractères ;
- `hypothese` : le changement proposé (ou le résultat jugé le plus intéressant), pourquoi il compte pour la surveillance ou le
  contrôle, et ce qu'il ajoute aux travaux des mentors (pièce « Colognese et Ward », sections 1 et 3) ;
- `axe` : exactement une des trois valeurs, tirées de la question : `changement_de_dispositif` (« aurions-nous dû faire quelque
  chose autrement ? »), `resultat_le_plus_interessant` (le résultat le plus intéressant, et pourquoi),
  `ce_que_le_billet_ne_dit_pas` (ce que le billet ne dit pas et que tu supposes) ;
- `epreuve` : ce qui change, sur quel résultat du billet (avec sa section), et le protocole (modèle, caractères, graines,
  triches, moniteurs, seuil) ;
- `controle` : **une chose qui rendrait le résultat trompeur**, et le contrôle qui la détecterait ; ce que le billet ne dit pas
  et que tu supposes, marqué « supposé » ;
- `prediction` : le résultat qui montrerait que le changement compte, chiffré, avec son signe et un intervalle, marqué
  « supposé » (ou « calcul ») ;
- `test_de_mort` : l'expérience ou le nombre qui, lu une seule fois, tue l'idée ; ce qui ferait échouer ton analyse ;
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
