#!/usr/bin/env python3
"""Barreau 5 : contrôle de l'erratum 1 au brouillon 5 (v1).

Écrit par le rédacteur (Claude Fable 5.2). Lit les couples de `erratum-1-brouillon5-plan-sabotage-ou-empreinte-v1.md`,
les applique dans l'ordre à des copies en mémoire du texte et du devis du brouillon 5, et vérifie : chaque « avant »
trouvé une fois au moment où il s'applique ; aucun « après » déjà présent ; marques levées ; les « après » des 20
couples de la vérification du brouillon 4 encore présents à l'octet ; validateur du dépôt sur la copie du texte.
N'écrit rien dans le dépôt : compte rendu sur la sortie standard, avec l'empreinte des deux copies consolidées.
Aucune donnée du programme.
"""
import hashlib
import os
import re
import runpy
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
PIECES = {"T": (os.path.join(RACINE, "prereg", "barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon5.md"), "6f7e2041"),
          "DV": (os.path.join(ICI, "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon5.md"), "9ba5db06")}
MARQUE = "[à confirmer par le rapport v4]"
MOTIF = re.compile(r"#### Couple (?P<nom>[A-Z]+-\d+[a-z]) — (?P<piece>T|DV) — [^\n]*\n\nAvant :\n\n```text\n(?P<avant>.*?)\n```\n\n"
                   r"Après :\n\n```text\n(?P<apres>.*?)\n```\n", re.S)


def consolider():
    """Rend les deux copies consolidées et le compte des défauts."""
    p, defauts = {}, 0
    for k, (chemin, attendu) in PIECES.items():
        p[k] = open(chemin, encoding="utf-8").read()
        e = hashlib.sha256(p[k].encode()).hexdigest()
        print(f"{k} : {e[:16]} ({'égale à celle attendue' if e.startswith(attendu) else 'DIFFÉRENTE'})")
        defauts += not e.startswith(attendu)
        print(f"  marques avant l'erratum : {p[k].count(MARQUE)}")
    source = open(os.path.join(ICI, "erratum-1-brouillon5-plan-sabotage-ou-empreinte-v1.md"), encoding="utf-8").read()
    couples = list(MOTIF.finditer(source))
    titres = len(re.findall(r"^#### Couple ", source, re.M))
    for m in couples:
        k, avant, apres = m["piece"], m["avant"], m["apres"]
        n = p[k].count(avant)
        deja = 0 if avant in apres else p[k].count(apres)
        ok = n == 1 and deja == 0
        defauts += not ok
        print(f"{m['nom']:6s} {k:2s} avant trouvé {n} fois ; après déjà présent {deja} fois : {'ok' if ok else 'DÉFAUT'}")
        if n == 1:
            p[k] = p[k].replace(avant, apres)
    print(f"couples lus : {len(couples)} sur {titres} titres (texte {sum(m['piece'] == 'T' for m in couples)}, devis {sum(m['piece'] == 'DV' for m in couples)})")
    defauts += len(couples) != titres
    return p, defauts


def main():
    p, defauts = consolider()
    # les marques qui supposaient un comportement du code : toutes levées ; restent les mentions qui parlent des marques
    for k in p:
        lignes = [i + 1 for i, l in enumerate(p[k].split("\n")) if MARQUE in l]
        print(f"{k} : marques après l'erratum : {p[k].count(MARQUE)} (lignes {lignes})")
    v = runpy.run_path(os.path.join(ICI, "outils-verification-plan-brouillon4-v1", "couples-verification-brouillon4-v1.py"),
                       run_name="verificateur")
    cle = {v["T"]: "T", v["DV"]: "DV"}
    perdus = [c[0] for c in v["COUPLES"] if c[3] in cle and p[cle[c[3]]].count(c[5]) != 1]
    print(f"« après » des couples de la vérification du brouillon 4 qui ne sont plus à l'octet : {perdus or 'aucun'}")
    sys.path.insert(0, os.path.join(RACINE, "src"))
    from controle_ia.prereg import problemes
    with tempfile.TemporaryDirectory(dir="/dev/shm" if os.path.isdir("/dev/shm") else None) as d:
        chemin = os.path.join(d, "copie.md")
        open(chemin, "w", encoding="utf-8").write(p["T"])
        print(f"validateur du dépôt sur la copie consolidée du texte : {problemes(chemin) or 'aucun problème'}")
    for k in p:
        print(f"{k} consolidé : {len(p[k])} signes, {hashlib.sha256(p[k].encode()).hexdigest()}")
    print(f"défauts : {defauts}")
    sys.exit(1 if defauts else 0)


if __name__ == "__main__":
    main()
