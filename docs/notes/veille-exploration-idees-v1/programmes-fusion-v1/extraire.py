#!/usr/bin/env python3
"""Extrait les tableaux des quatre notes de recherche en une liste d'entrees brutes (JSON).

Lecture seule des notes ; aucune execution de leur contenu. A lancer avec -I.
Usage : python -I extraire.py DOSSIER_NOTES SORTIE.json
"""
import json
import re
import sys
from pathlib import Path

dossier = Path(sys.argv[1])
sortie = Path(sys.argv[2])

RE_ARXIV = re.compile(r"(?<![\d.])(\d{4}\.\d{4,5})(?:v\d+)?(?![\d])")
RE_LIEN = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")


def cellules(ligne):
    ligne = ligne.strip()
    if not (ligne.startswith("|") and ligne.endswith("|")):
        return None
    parts = re.split(r"(?<!\\)\|", ligne[1:-1])
    return [p.strip() for p in parts]


def tables(lignes, debut, fin):
    """Rend (entete, [rangees], numero de ligne) pour chaque tableau entre debut et fin (indices de lignes)."""
    i = debut
    while i < fin:
        c = cellules(lignes[i])
        if c and i + 1 < fin and re.match(r"^\|\s*-{3}", lignes[i + 1].strip()):
            entete = [x.lower() for x in c]
            rangees = []
            j = i + 2
            while j < fin:
                cj = cellules(lignes[j])
                if cj is None:
                    break
                rangees.append((j + 1, cj))
                j += 1
            yield entete, rangees
            i = j
        else:
            i += 1


def section(lignes, motif_debut, motif_fin=None):
    d = next(i for i, l in enumerate(lignes) if re.match(motif_debut, l))
    if motif_fin is None:
        return d, len(lignes)
    f = next(i for i, l in enumerate(lignes) if i > d and re.match(motif_fin, l))
    return d, f


entrees = []
anomalies = []


def ajoute(voie, fichier, ligne, rubrique, **k):
    e = dict(voie=voie, fichier=fichier, ligne=ligne, rubrique=rubrique)
    e.update(k)
    entrees.append(e)


# ---------------------------------------------------------------- mots-cles
f = "recherche-mots-cles-v1.md"
L = (dossier / f).read_text(encoding="utf-8").split("\n")
d, fin = section(L, r"^## 1\. Tableau principal", r"^## 2\. ")
rub = ""
i = d
# on parcourt en gardant la rubrique courante
bornes = [k for k in range(d, fin) if L[k].startswith("### ")] + [fin]
for a, b in zip(bornes, bornes[1:]):
    rub = L[a][4:].strip()
    for entete, rangees in tables(L, a, b):
        for n, c in rangees:
            if len(c) != len(entete):
                anomalies.append((f, n, len(c), len(entete)))
                continue
            r = dict(zip(entete, c))
            if "arxiv" in entete:
                m = RE_LIEN.search(r["arxiv"])
                ajoute("mots-cles", f, n, rub, titre=r["titre"], adresse=m.group(2) if m else r["arxiv"],
                       nature="article arXiv", auteurs=r["auteurs"], date=r["première version"],
                       fait=r["ce qu'il fait"], touche=r["touche"], mesure=r["mesuré ou affirmé"],
                       lu=r["lu jusqu'où"], niveau="annote")
            else:
                ajoute("mots-cles", f, n, rub, titre=r["titre"], adresse=r["adresse"], nature=r["nature"],
                       auteurs=r["auteurs"], date=r["date"], fait=r["ce qu'il fait"], touche=r["touche"],
                       mesure=r["mesuré ou affirmé"], lu=r["lu jusqu'où"], niveau="annote")
d, fin = section(L, r"^## 4\. Annexe mécanique", r"^## 5\. ")
for entete, rangees in tables(L, d, fin):
    for n, c in rangees:
        if len(c) != len(entete):
            anomalies.append((f, n, len(c), len(entete)))
            continue
        r = dict(zip(entete, c))
        m = RE_LIEN.search(r["arxiv"])
        ajoute("mots-cles", f, n, "annexe mécanique (titre seul, pertinence non confirmée)", titre=r["titre"],
               adresse=m.group(2) if m else r["arxiv"], nature="article arXiv", auteurs="", date=r["première version"],
               fait="(titre seul, retenu par filtre lexical, pertinence non confirmée)", touche="non évalué",
               mesure="inconnu", lu="titre seul", niveau="annexe")

# ---------------------------------------------------------------- citations
f = "recherche-citations-v2.md"
L = (dossier / f).read_text(encoding="utf-8").split("\n")
d, fin = section(L, r"^## 4\. Tableau complet", r"^## 5\. ")
bornes = [k for k in range(d, fin) if L[k].startswith("### ")] + [fin]
for a, b in zip(bornes, bornes[1:]):
    rub = L[a][4:].strip()
    for entete, rangees in tables(L, a, b):
        for n, c in rangees:
            if len(c) != len(entete):
                anomalies.append((f, n, len(c), len(entete)))
                continue
            r = dict(zip(entete, c))
            ta = r["titre — auteurs"]
            if " — " in ta:
                titre, auteurs = ta.rsplit(" — ", 1)
            else:
                titre, auteurs = ta, ""
            ajoute("citations", f, n, rub, titre=titre.strip(), adresse=r["adresse"], nature=r["nature"],
                   auteurs=auteurs.strip(), date=r["première version"], fait=r["ce qu'il fait"], touche=r["touche"],
                   mesure=r["mesuré ou affirmé"], lu=r["lu jusqu'où"], niveau="annote", trouve_par=r.get("trouvé par", ""))

# ---------------------------------------------------------------- grise
f = "recherche-litterature-grise-v1.md"
L = (dossier / f).read_text(encoding="utf-8").split("\n")
d, fin = section(L, r"^## Tableau", r"^## Requêtes jouées")
for entete, rangees in tables(L, d, fin):
    for n, c in rangees:
        if len(c) != len(entete):
            anomalies.append((f, n, len(c), len(entete)))
            continue
        r = dict(zip(entete, c))
        ajoute("grise", f, n, "", titre=r["titre"], adresse=r["adresse"], nature=r["nature"], auteurs=r["auteurs"],
               date=r["première version"], fait=r["ce qu'il fait"], touche=r["touche"], mesure=r["mesure"], lu=r["lu"],
               niveau="annote")

# ---------------------------------------------------------------- adverse
f = "recherche-adverse-v1.md"
L = (dossier / f).read_text(encoding="utf-8").split("\n")
d, fin = section(L, r"^## 2\. Liste complète", r"^## 3\. ")
for entete, rangees in tables(L, d, fin):
    for n, c in rangees:
        if len(c) != len(entete):
            anomalies.append((f, n, len(c), len(entete)))
            continue
        r = dict(zip(entete, c))
        ajoute("adverse", f, n, "", titre=r["titre"], adresse=r["adresse"], nature=r["nature"], auteurs=r["auteurs"],
               date=r["première version"], fait=r["ce qu'il fait"], touche=r["touche"], mesure=r["mesuré ou affirmé"],
               lu=r["lu jusqu'où"], niveau="annote")

sortie.write_text(json.dumps(entrees, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
print("entrees :", Counter((e["voie"], e["niveau"]) for e in entrees))
print("anomalies de colonnes :", anomalies)
