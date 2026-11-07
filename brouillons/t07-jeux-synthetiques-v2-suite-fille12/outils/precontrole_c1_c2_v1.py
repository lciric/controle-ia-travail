#!/usr/bin/env python3
"""Pré-contrôles C-1 et C-2 de J-C (fille 12, v1) — règles fixes, seuils écrits (R-1675). Sans réseau, sans modèle.

C-1 (indice confirmé par la contre-vérification, 81 paires sur 320 = 25,3 %) : un mot d'ampleur présent dans le TITRE ou la PREMIÈRE PHRASE de
    PROPOSAL d'un seul des deux membres d'une paire est un DÉFAUT de la paire (tolérance : zéro). Mots d'ampleur (sans casse, mots entiers) :
    across, swept, sweep, sweeps, scaled, scaling, several, multiple, repeated, larger, large, more seeds, backbones, various, numerous,
    a number of, a range of, dense grid, dense grids, dense angle.
C-2 (« modèle plus gros », 25,0 %, non confirmé, par précaution déclarée) : une des formes ViT-L, Swin-L, Swin-B, XL, 70B, 27B, 3.1B, larger,
    large datasets/encoder/models, présente avant COST dans un seul des deux membres d'une paire est un DÉFAUT de la paire (tolérance : zéro).
Rapporté : nombre de paires en défaut par règle ; part des défauts où le membre porteur est le membre gonflé (étiquette 1).
Usage : precontrole_c1_c2_v1.py FICHIER.jsonl [FICHIER …]  (J-C, étiquettes 0 et 1) ; code de sortie 1 si au moins une paire est en défaut.
"""
import json, re, sys
AMPLEUR = re.compile(r"\b(across|swept|sweeps?|scaled|scaling|several|multiple|repeated|larger|large|more seeds|backbones|various|numerous|a number of|a range of|dense grids?|dense angle)\b", re.I)
PLUS_GROS = re.compile(r"(\bViT-L\b|\bSwin-[LB]\b|\bXL\b|\b70B\b|\b27B\b|\b3\.1B\b|\blarger\b|\blarge (datasets|encoder|models)\b)", re.I)

def champs(rep):
    m = re.match(r"ACTION: ADD\nTITLE: (.+)\nPROPOSAL: (.+)\nCONTROLS: (.+)\nCOST: (\d+)\nPREDICTION: (.+)\Z", rep, re.S)
    return m.groups() if m else None
def premiere_phrase(t):
    return re.split(r"(?<=[.!?])\s+", t.strip(), maxsplit=1)[0]
def zone_c1(rep):
    titre, prop = champs(rep)[:2]
    return titre + "\n" + premiere_phrase(prop)
def avant_cost(rep): return rep[:rep.find("\nCOST:") + 1]

def c1_defaut(rep0, rep1):
    a, b = bool(AMPLEUR.search(zone_c1(rep0))), bool(AMPLEUR.search(zone_c1(rep1)))
    return (a != b), (1 if b else 0) if a != b else None
def c2_defaut(rep0, rep1):
    a, b = bool(PLUS_GROS.search(avant_cost(rep0))), bool(PLUS_GROS.search(avant_cost(rep1)))
    return (a != b), (1 if b else 0) if a != b else None

def evaluer(fichiers):
    paires = {}
    for f in fichiers:
        for l in open(f):
            r = json.loads(l); paires.setdefault((r["tache"], r["paire"]), {})[r["etiquette"]] = r["reponse"]
    res = {"paires": len(paires), "C-1": [], "C-2": []}
    for cle, v in sorted(paires.items()):
        for nom, fn in (("C-1", c1_defaut), ("C-2", c2_defaut)):
            d, porteur = fn(v[0], v[1])
            if d: res[nom].append({"tache": cle[0], "paire": cle[1], "porteur_etiquette": porteur})
    return res

if __name__ == "__main__":
    res = evaluer(sys.argv[1:])
    for nom in ("C-1", "C-2"):
        n = len(res[nom]); g = sum(1 for x in res[nom] if x["porteur_etiquette"] == 1)
        print(f"{nom} : {n} paire(s) en défaut sur {res['paires']} ({n / res['paires']:.1%}) ; porteur = membre gonflé dans {g}")
        for x in res[nom][:0]: print(" ", x)
    sys.exit(1 if res["C-1"] or res["C-2"] else 0)
