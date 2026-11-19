#!/usr/bin/env python3
"""Barreau 5 : contrôle des couples de `couples-du-code-pour-brouillon4-v1.md` (v1).

Lit le fichier des couples, applique chaque couple dans l'ordre à une copie en mémoire du texte (brouillon 3) ou du
devis (brouillon 3), et vérifie que chaque « avant » s'y trouve exactement une fois au moment où il s'applique.
N'écrit rien : imprime un compte rendu. Aucune donnée du programme.
"""
import hashlib
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
PIECES = {"T": os.path.join(RACINE, "prereg", "barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md"),
          "DV": os.path.join(ICI, "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md")}
ATTENDU = {"T": "525f338e7899e6a8", "DV": "7ac56a7b9f133a9a"}
MOTIF = re.compile(r"#### Couple (?P<nom>[CD]-\d+[a-z]) — (?P<piece>T|DV) — [^\n]*\n\nAvant :\n\n```text\n(?P<avant>.*?)\n```\n\n"
                   r"Après :\n\n```text\n(?P<apres>.*?)\n```\n", re.S)


def main():
    textes = {}
    for k, chemin in PIECES.items():
        brut = open(chemin, "rb").read()
        e = hashlib.sha256(brut).hexdigest()
        print(f"{k} : {e[:16]} ({'égale à celle attendue' if e.startswith(ATTENDU[k]) else 'DIFFÉRENTE'})")
        textes[k] = brut.decode("utf-8")
    source = open(os.path.join(ICI, "couples-du-code-pour-brouillon4-v1.md"), encoding="utf-8").read()
    couples = list(MOTIF.finditer(source))
    titres = re.findall(r"^#### Couple ", source, re.M)
    defauts = 0
    for m in couples:
        k, avant, apres = m["piece"], m["avant"], m["apres"]
        n = textes[k].count(avant)
        deja = textes[k].count(apres) if apres not in avant and avant not in apres else 0
        etat = "ok" if n == 1 and deja == 0 else "DÉFAUT"
        defauts += etat != "ok"
        print(f"{m['nom']:6s} {k:2s} avant trouvé {n} fois ; après déjà présent {deja} fois : {etat}")
        if n == 1:
            textes[k] = textes[k].replace(avant, apres)
    groupes = {"C": sum(m["nom"].startswith("C") for m in couples), "D": sum(m["nom"].startswith("D") for m in couples)}
    print(f"couples lus : {len(couples)} sur {len(titres)} titres ; groupe 1 : {groupes['C']} ; groupe 2 : {groupes['D']} ; défauts : {defauts}")
    sys.exit(1 if defauts or len(couples) != len(titres) else 0)


if __name__ == "__main__":
    main()
