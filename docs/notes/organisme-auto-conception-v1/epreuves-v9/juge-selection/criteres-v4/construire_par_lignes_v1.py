#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construit une version neuve d'un texte à partir d'une version scellée, par numéros de lignes — v1.

La source n'est jamais modifiée ; son empreinte est vérifiée avant tout (les numéros de lignes
n'ont de sens que sur elle). La sortie est un fichier neuf ; refus s'il existe (règle R12).

Fichier d'opérations, texte brut. Chaque opération commence par une ligne de commande :
  @@ REMPLACER a-b       remplace les lignes a à b (numéros de la source, bornes comprises)
  @@ INSERER-APRES a     insère après la ligne a (0 : en tête)
  @@ FIN                 fin du fichier d'opérations (obligatoire)
Les lignes qui suivent la commande, jusqu'à la suivante, sont le texte neuf (vide permis :
suppression). Deux opérations ne peuvent pas toucher la même ligne.

Usage : python3 -B construire_par_lignes_v1.py --source F --sha-source S --operations O --sortie N
"""
import argparse
import hashlib
import os
import re
import sys


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--source", required=True)
    p.add_argument("--sha-source", required=True)
    p.add_argument("--operations", required=True)
    p.add_argument("--sortie", required=True)
    a = p.parse_args(argv)
    if os.path.exists(a.sortie):
        print("REFUS : la sortie existe déjà", file=sys.stderr)
        return 2
    with open(a.source, "rb") as f:
        octets = f.read()
    if hashlib.sha256(octets).hexdigest() != a.sha_source.strip().lower():
        print("REFUS : empreinte de la source différente de celle annoncée", file=sys.stderr)
        return 2
    source = octets.decode("utf-8").split("\n")
    if source and source[-1] == "":
        source.pop()
    with open(a.operations, encoding="utf-8") as f:
        lignes = f.read().split("\n")
    ops, courant, fini = [], None, False
    for ligne in lignes:
        if fini:
            if ligne.strip():
                print("REFUS : texte après « @@ FIN »", file=sys.stderr)
                return 2
            continue
        m = re.fullmatch(r"@@ (REMPLACER) (\d+)-(\d+)|@@ (INSERER-APRES) (\d+)|@@ (FIN)", ligne)
        if ligne.startswith("@@ ") and not m:
            print(f"REFUS : commande illisible : {ligne}", file=sys.stderr)
            return 2
        if m:
            if m.group(6):
                fini = True
                courant = None
            elif m.group(1):
                courant = {"genre": "remplacer", "de": int(m.group(2)), "a": int(m.group(3)), "texte": []}
                ops.append(courant)
            else:
                courant = {"genre": "inserer", "de": int(m.group(5)), "a": int(m.group(5)), "texte": []}
                ops.append(courant)
        elif courant is None:
            if ligne.strip():
                print("REFUS : texte avant la première commande", file=sys.stderr)
                return 2
        else:
            courant["texte"].append(ligne)
    if not fini:
        print("REFUS : « @@ FIN » absent — fichier d'opérations peut-être tronqué", file=sys.stderr)
        return 2
    touchees = set()
    for o in ops:
        if o["genre"] == "remplacer":
            if not (1 <= o["de"] <= o["a"] <= len(source)):
                print(f"REFUS : bornes hors de la source : {o['de']}-{o['a']}", file=sys.stderr)
                return 2
            plage = set(range(o["de"], o["a"] + 1))
            if plage & touchees:
                print(f"REFUS : deux opérations touchent la même ligne ({o['de']}-{o['a']})", file=sys.stderr)
                return 2
            touchees |= plage
        elif not (0 <= o["de"] <= len(source)):
            print(f"REFUS : insertion hors de la source : {o['de']}", file=sys.stderr)
            return 2
    # du bas vers le haut ; à ligne égale, l'insertion (après la ligne) s'applique avant le remplacement
    for o in sorted(ops, key=lambda o: (o["a"], o["genre"] == "inserer"), reverse=True):
        if o["genre"] == "remplacer":
            source[o["de"] - 1:o["a"]] = o["texte"]
        else:
            source[o["de"]:o["de"]] = o["texte"]
    sortie = ("\n".join(source) + "\n").encode("utf-8")
    with open(a.sortie, "xb") as f:
        f.write(sortie)
    print(f"{hashlib.sha256(sortie).hexdigest()}  {os.path.basename(a.sortie)}  ({len(ops)} opérations, {len(source)} lignes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
