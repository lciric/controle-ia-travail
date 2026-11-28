"""Recalcule les moyennes de ChatInject (2509.22830v3, tableau 1, p. 5) annoncées p. 1 et p. 5.

Usage : python3 -I -B recalcul_moyennes_chatinject_v1.py PAGE5.txt
Lit les lignes du tableau 1 dans le texte brut de la page 5 (pdftotext -raw), sans rien saisir à la main.
Colonnes : InjecPrompt default, ChatInject, +think, +tool, Multi-turn default, Multi-turn ChatInject.
"""
import re
import sys

MODELES = ["Qwen-3", "GPT-oss", "Llama-4", "GLM-4.5", "Kimi-K2", "Grok-2"]


def lire_bloc(lignes, debut, fin):
    bloc = {}
    for ligne in lignes[debut:fin]:
        for m in MODELES:
            if ligne.startswith(m + " ") and m not in bloc:
                reste = ligne[len(m):]
                reste = re.sub(r"\([+-][0-9.]+\)", " ", reste)  # retire les écarts entre parenthèses
                valeurs = [None if v == "–" else float(v) for v in reste.split()]
                bloc[m] = valeurs
    return bloc


def main(chemin):
    lignes = [l.strip() for l in open(chemin, encoding="utf-8")]
    i_agent = next(i for i, l in enumerate(lignes) if l == "AgentDojo")
    i_util = next(i for i, l in enumerate(lignes) if l == "Utility")
    injec = lire_bloc(lignes, 0, i_agent)
    dojo = lire_bloc(lignes, i_agent, i_util)
    for nom, bloc in (("InjecAgent", injec), ("AgentDojo", dojo)):
        print(nom)
        for m in MODELES:
            print("  ", m, bloc[m])
        d = [bloc[m][0] for m in MODELES]
        c = [bloc[m][1] for m in MODELES]
        print(f"   moyenne InjecPrompt default = {sum(d)/6:.4f} ; InjecPrompt + ChatInject = {sum(c)/6:.4f}")
    mt_def = [b[m][-2] for b in (injec, dojo) for m in MODELES]
    mt_ci = [b[m][-1] for b in (injec, dojo) for m in MODELES]
    print(f"Multi-turn default, moyenne sur 12 (6 modèles x 2 bancs) = {sum(mt_def)/12:.4f}")
    print(f"Multi-turn + ChatInject, moyenne sur 12 = {sum(mt_ci)/12:.4f}")
    toutes_def = [b[m][0] for b in (injec, dojo) for m in MODELES]
    print(f"InjecPrompt default, moyenne sur 12 = {sum(toutes_def)/12:.4f}")
    print(f"Qwen-3, AgentDojo : InjecPrompt default {dojo['Qwen-3'][0]} ; Multi-turn default {dojo['Qwen-3'][-2]}")


if __name__ == "__main__":
    main(sys.argv[1])
