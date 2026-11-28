"""Essai hors dépôt : la borne du coût (bornes_champs) désigne-t-elle l'occurrence que lire_action lit ?
Émulation de _nettoyer avec suivi des positions (finditer sur le même motif), vérifiée égale à _nettoyer."""
import random
import re
import sys

from controle_ia.environnements.propositions import _CLE, _nettoyer, lire_action
from controle_ia.harnais.modeles import tokeniseur_caracteres_chat
from controle_ia.premier_test_ia import conditions as cd

MOTIF = re.compile(r"[*_]{1,3}(ACTION|TITLE|PROPOSAL|CONTROLS|COST|PREDICTION)\s*:?\s*[*_]{1,3}\s*:?", re.I)


def choix_lire_action(texte):
    """Position brute du mot COST de l'occurrence que lire_action retient (None : aucune)."""
    morceaux, carte, prec = [], [], 0          # carte : (début nettoyé, début brut du mot) pour les clés remplacées
    propre = ""
    decal = []                                  # (position nettoyée, décalage brut − nettoyé) après chaque remplacement
    for m in MOTIF.finditer(texte):
        propre += texte[prec:m.start()]
        carte.append((len(propre), m.start(1)))
        propre += m.group(1) + ":"
        decal.append((len(propre), m.end() - len(propre)))
        prec = m.end()
    propre += texte[prec:]
    assert propre == _nettoyer(texte)
    if lire_action(texte).motif and "ACTION" in (lire_action(texte).motif or ""):
        return None
    cles = list(_CLE.finditer(propre))
    for k, c in enumerate(cles):
        if c["cle"].upper() != "COST":
            continue
        fin = cles[k + 1].start() if k + 1 < len(cles) else len(propre)
        if propre[c.end():fin].strip():
            p = c.start("cle")
            for debut, brut in carte:
                if debut == p:
                    return brut
            d = 0
            for pos, dd in decal:
                if pos <= p:
                    d = dd
            return p + d
    return None


tok = tokeniseur_caracteres_chat()
FORMES = ["{k}:", "**{k}:**", "**{k}**:", "*{k}:*", "__{k}:__", "**{k} :**"]
VALEURS = ["", " ", "  ", " 30", "30 GPU-hours", " **", "\n40", " 5 x 3"]
rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
ecarts, n = [], 0
for _ in range(20000):
    lignes = ["ACTION: ADD", "TITLE: a", "PROPOSAL: x"]
    for _ in range(rng.randint(1, 4)):
        k = rng.choice(["COST", "COST", "CONTROLS", "PREDICTION"])
        lignes.append(rng.choice(FORMES).format(k=k) + rng.choice(VALEURS))
    texte = rng.choice(["\n", "\n\n"]).join(lignes) + rng.choice(["", "\n", "  \n"])
    attendu = choix_lire_action(texte)
    b = cd.bornes_champs(tok, tok(texte, add_special_tokens=False)["input_ids"], texte)["COST"]
    b = None if b == -1 else b
    n += 1
    if attendu != b:
        ecarts.append((texte, attendu, b))
print(f"{n} textes, {len(ecarts)} écarts")
for t, a, b in ecarts[:8]:
    print(repr(t), "lire_action:", a, "bornes:", b)

# comparaison avec l'ancienne règle (première occurrence, vide ou non), par catégorie d'écart
_ANCIEN = re.compile(r"^\s*[*_]{0,3}(?P<cle>TITLE|PROPOSAL|CONTROLS|COST|PREDICTION)[*_]{0,3}\s*:", re.I | re.M)


def ancienne(texte):
    for m in _ANCIEN.finditer(texte):
        if m["cle"].upper() == "COST":
            return m.start("cle")
    return None


rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
cats = {"nouvelle": {}, "ancienne": {}}
exemples = {}
for _ in range(20000):
    lignes = ["ACTION: ADD", "TITLE: a", "PROPOSAL: x"]
    for _ in range(rng.randint(1, 4)):
        k = rng.choice(["COST", "COST", "CONTROLS", "PREDICTION"])
        lignes.append(rng.choice(FORMES).format(k=k) + rng.choice(VALEURS))
    texte = rng.choice(["\n", "\n\n"]).join(lignes) + rng.choice(["", "\n", "  \n"])
    attendu = choix_lire_action(texte)
    nb = cd.bornes_champs(tok, tok(texte, add_special_tokens=False)["input_ids"], texte)["COST"]
    for nom, b in (("nouvelle", None if nb == -1 else nb), ("ancienne", ancienne(texte))):
        if attendu == b:
            c = "égal"
        elif attendu is None:
            c = "clé invisible pour lire_action"
        elif b is None:
            c = "borne absente, coût lu"
        else:
            c = "autre occurrence"
        cats[nom][c] = cats[nom].get(c, 0) + 1
        if nom == "nouvelle" and c in ("borne absente, coût lu", "autre occurrence"):
            exemples.setdefault(c, []).append((texte, attendu, b))
print(cats)
for c, l in exemples.items():
    for t, a, b in l[:4]:
        print(c, repr(t), "lire_action:", a, "bornes:", b)
