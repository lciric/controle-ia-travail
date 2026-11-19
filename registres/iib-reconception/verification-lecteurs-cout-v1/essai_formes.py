"""Essai d'égalité des deux lecteurs du coût, par forme, sur chaînes synthétiques (commit 836c7ccc).
Lecteur A : cout_action(action entière) ; lecteur B : lire_cout(suite coupée au premier saut de ligne), la suite étant
ce qui suit « COST: » dans l'action (comme la coupe du préfixe de l'oracle), y compris les marques de gras de fermeture."""
import re
from controle_ia.t06.cout import cout_action, lire_cout

GABARIT = "ACTION: ADD\nTITLE: t\nPROPOSAL: p\nCONTROLS: c\n{cle} {valeur}\nPREDICTION: q\n"

FORMES = [
    ("nombre simple", "COST:", "500 GPU-hours"),
    ("décimales point", "COST:", "2.5 GPU-hours"),
    ("décimales virgule", "COST:", "2,5 GPU-hours"),
    ("milliers virgule", "COST:", "2,500 GPU-hours"),
    ("milliers virgule + décimale", "COST:", "12,500.5 GPU-hours"),
    ("milliers point (convention européenne)", "COST:", "2.500 GPU-hours"),
    ("milliers espace", "COST:", "2 500 GPU-hours"),
    ("milliers espace insécable", "COST:", "2 500 GPU-hours"),
    ("suffixe k", "COST:", "2.5k GPU-hours"),
    ("suffixe K espacé", "COST:", "3 K GPU-hours"),
    ("plusieurs nombres", "COST:", "4 GPUs for 100 hours"),
    ("multiplication", "COST:", "8 x 50 = 400 GPU-hours"),
    ("intervalle", "COST:", "200-400 GPU-hours"),
    ("intervalle « to »", "COST:", "200 to 400 GPU-hours"),
    ("unité collée", "COST:", "120h"),
    ("unité collée k", "COST:", "120kh"),
    ("gras sur la valeur", "COST:", "**500** GPU-hours"),
    ("gras sur la clé", "**COST:**", "500 GPU-hours"),
    ("gras clé et valeur", "**COST:**", "**1,000 GPU-hours**"),
    ("monnaie dollar", "COST:", "$1,200 (about 400 GPU-hours)"),
    ("monnaie euro collée", "COST:", "1200€"),
    ("approximation", "COST:", "~1e3 GPU-hours"),
    ("tilde", "COST:", "~300 GPU-hours"),
    ("valeur sur la ligne suivante", "COST:", "\n500 GPU-hours"),
    ("premier nombre sur la ligne 2", "COST:", "moderate\n500 GPU-hours"),
    ("zéro puis nombre", "COST:", "0 extra, 200 GPU-hours"),
]


def suite_de(cle, valeur):
    # préfixe coupé après « COST: » (gras retiré pour le test de fin de clé) : la suite commence par ce qui reste de la clé
    reste_cle = cle[re.search(r"COST\s*:", cle).end():]
    return (reste_cle + " " + valeur).split("\n", 1)[0]


if __name__ == "__main__":
    print(f"{'forme':42s} {'action entière':>15s} {'suite':>10s}  accord")
    for nom, cle, valeur in FORMES:
        a = cout_action(GABARIT.format(cle=cle, valeur=valeur))["cout"]
        b = lire_cout(suite_de(cle, valeur))["cout"]
        print(f"{nom:42s} {a!s:>15s} {b!s:>10s}  {'oui' if a == b else 'NON'}")
