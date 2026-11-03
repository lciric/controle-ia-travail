#!/usr/bin/env python3
"""KIT COLOGNESE-WARD Q2, v1 (sous-agent de session-depot, 3 novembre 2026) : dérivé du kit Ibrahim v2 (outils/course-ibrahim-q1-v1, 965eb21b) par substitution de noms et par les changements de la course Colognese-Ward Q2 (deux pièces servies, trois variantes comme Ibrahim, garde lexicale sans « openai », juge du n° 419, marge d'appels 2 × plan + 5).
Commande externe Claude de la course Colognese-Ward Q2 (relais 8806, deux modèles) — v1 : aiguillage vers la commande A1-bis.

Rédigé le 3 novembre 2026 (sous-agent de session-depot) ; aucun appel réel. Le pôle v56 ne connaît qu'UNE commande par
fournisseur et passe le modèle demandé dans `MODELE_DEMANDE_POLE` ; la commande A1-bis (`commande_claude_a1bis_v1.py`,
7da79a5c…) exige `--modele` explicite et égal à cette variable. Ce fichier ne fait que : (1) vérifier les empreintes de la
commande A1-bis, de son contrat commun (1f56e466…) et du registre cumulé (8ba92066…) ; (2) lire `MODELE_DEMANDE_POLE` et
exiger qu'il soit l'un des deux modèles permis de la course (`claude-fable-5-1`, `claude-opus-5-5`) ; (3) appeler
`principal(["appeler", "--modele", <modèle demandé>] + arguments reçus)` de la commande A1-bis, dans ce processus. Aucun
repli, aucune bascule : un modèle absent, non permis ou une empreinte différente rend le code 2 (dernière ligne JSON au
contrat, coût plancher, rien n'est envoyé). Les réglages (`--effort high --reflexion adaptative`) viennent de la ligne de
commande de la configuration, comparés au relais par la commande A1-bis (refus 409 s'ils diffèrent).
"""

import hashlib
import importlib.util
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(ICI))))
A1BIS = os.path.join(DEPOT, "docs", "notes", "ideation-organisme-v1", "commandes-a1-bis-v1")
EMPREINTES = {"commande_claude_a1bis_v1.py": "7da79a5c34449dd7629aa3d1721c76058a34b56b43f2bd46c9dbfc94e20ef2c5",
              "commande_pole_v56_commun_v1.py": "1f56e466f5e80f82a25ccccbb5784fa0fa6dc34046dc99d887ec87f713c7eaed",
              "registre_depense_cumulee_v1.py": "8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff"}
MODELES_PERMIS = ("claude-fable-5-1", "claude-opus-5-5")
VERSION = "commande-claude-colognese-v1"


def refuser(motif):
    print(json.dumps({"texte": "", "cout_usd": 1e-06, "version": VERSION, "erreur": motif[:300], "envoye": False},
                     ensure_ascii=False))
    sys.stdout.flush()
    return 2


def principal(argv=None, environ=None, entree=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    environ = dict(os.environ) if environ is None else environ
    for nom, attendu in EMPREINTES.items():
        p = os.path.join(A1BIS, nom)
        try:
            with open(p, "rb") as f:
                vu = hashlib.sha256(f.read()).hexdigest()
        except OSError:
            return refuser(f"{nom} absent ({A1BIS}) : refus")
        if vu != attendu:
            return refuser(f"{nom} : empreinte {vu[:12]}… ≠ {attendu[:12]}… : refus")
    if "--modele" in argv or "servir" in argv or "appeler" in argv:
        return refuser("--modele, servir et appeler sont posés par cette commande, jamais reçus : refus")
    demande = environ.get("MODELE_DEMANDE_POLE")
    if demande not in MODELES_PERMIS:
        return refuser(f"MODELE_DEMANDE_POLE {demande!r} hors de {MODELES_PERMIS} : refus")
    spec = importlib.util.spec_from_file_location("commande_claude_a1bis_v1", os.path.join(A1BIS, "commande_claude_a1bis_v1.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.principal(["appeler", "--modele", demande] + argv, environ=environ, entree=entree)


if __name__ == "__main__":
    sys.exit(principal())
