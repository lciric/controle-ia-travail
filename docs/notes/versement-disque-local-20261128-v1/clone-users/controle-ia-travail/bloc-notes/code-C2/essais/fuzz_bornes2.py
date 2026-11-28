"""Essai hors dépôt (2) : écarts de la borne du coût à l'occurrence que lit lire_action, séparés en deux causes :
clé brute invisible pour lire_action (nettoyage qui joint des lignes, gras non fermé) ou règle du vide."""
import random
import re
import sys

from controle_ia.environnements.propositions import _CLE, _nettoyer, lire_action
from controle_ia.harnais.modeles import tokeniseur_caracteres_chat
from controle_ia.premier_test_ia import conditions as cd

MOTIF = re.compile(r"[*_]{1,3}(ACTION|TITLE|PROPOSAL|CONTROLS|COST|PREDICTION)\s*:?\s*[*_]{1,3}\s*:?", re.I)


def emulation(texte):
    """Clés COST vues par lire_action (position brute du mot) et celle retenue."""
    propre, prec, carte, decal = "", 0, [], []
    for m in MOTIF.finditer(texte):
        propre += texte[prec:m.start()]
        carte.append((len(propre), m.start(1)))
        propre += m.group(1) + ":"
        decal.append((len(propre), m.end() - len(propre)))
        prec = m.end()
    propre += texte[prec:]
    assert propre == _nettoyer(texte)

    def brut(p):
        for debut, b in carte:
            if debut == p:
                return b
        d = 0
        for pos, dd in decal:
            if pos <= p:
                d = dd
        return p + d

    cles = list(_CLE.finditer(propre))
    vues, retenue = [], None
    for k, c in enumerate(cles):
        if c["cle"].upper() != "COST":
            continue
        vues.append(brut(c.start("cle")))
        fin = cles[k + 1].start() if k + 1 < len(cles) else len(propre)
        if retenue is None and propre[c.end():fin].strip():
            retenue = brut(c.start("cle"))
    return vues, retenue


tok = tokeniseur_caracteres_chat()
FORMES = ["{k}:", "**{k}:**", "**{k}**:", "*{k}:*", "__{k}:__", "**{k} :**"]
VALEURS = ["", " ", "  ", " 30", "30 GPU-hours", " **", "\n40", " 5 x 3"]
rng = random.Random(int(sys.argv[1]))
compte, exemples = {}, {}
brute = re.compile(r"^\s*[*_]{0,3}(COST)[*_]{0,3}\s*:", re.I | re.M)
for _ in range(30000):
    lignes = ["ACTION: ADD", "TITLE: a", "PROPOSAL: x"]
    for _ in range(rng.randint(1, 4)):
        k = rng.choice(["COST", "COST", "CONTROLS", "PREDICTION"])
        lignes.append(rng.choice(FORMES).format(k=k) + rng.choice(VALEURS))
    texte = rng.choice(["\n", "\n\n"]).join(lignes) + rng.choice(["", "\n", "  \n"])
    vues, retenue = emulation(texte)
    b = cd.bornes_champs(tok, tok(texte, add_special_tokens=False)["input_ids"], texte)["COST"]
    b = None if b == -1 else b
    toutes = [m.start(1) for m in brute.finditer(texte)]
    invisibles = [p for p in toutes if p not in vues]
    if b == retenue:
        c = "égal"
    elif invisibles and (b in invisibles or retenue is None or any(p < max(b or 0, retenue or 0) for p in invisibles)):
        c = "clé brute invisible pour lire_action"
    else:
        c = "règle du vide"
    compte[c] = compte.get(c, 0) + 1
    exemples.setdefault(c, []).append((texte, retenue, b))
print(compte)
for t, a, b in exemples.get("règle du vide", [])[:6]:
    print(repr(t), "lire_action:", a, "bornes:", b)
