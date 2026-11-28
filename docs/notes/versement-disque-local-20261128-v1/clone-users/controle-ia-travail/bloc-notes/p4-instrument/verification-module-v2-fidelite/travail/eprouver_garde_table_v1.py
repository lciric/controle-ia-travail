"""Épreuve indépendante de la garde « table du texte » du module v2 (`exiger_table_des_criteres`), R5.

Cas sain : le texte du candidat 1, tel quel. Artefacts : chaque cellule changée d'un seul signe (22 cas), chaque ligne
retirée (11 cas), ligne en plus de plusieurs formes, ordre changé, double espace, espace insécable, barre échappée
rendue nue, brouillon 4, section dupliquée. Chaque cas : « refus » (GardeArret, motif) ou « passe ». Sortie JSON.

Usage (depuis la racine du dépôt, en lecture seule) :
  PYTHONPATH=src:<module-v2> python -B eprouver_garde_table_v1.py <candidat1.md> <brouillon4.md>
"""
import json
import sys
from pathlib import Path

import lecture_p4_v1 as lp
from controle_ia.gardes import GardeArret


def essai(nom, texte, attendu):
    try:
        r = lp.exiger_table_des_criteres(texte)
        obtenu, motif = "passe", r
    except GardeArret as e:
        obtenu, motif = "refus", str(e)
    return {"cas": nom, "attendu": attendu, "obtenu": obtenu, "conforme": obtenu == attendu,
            "motif": motif if isinstance(motif, str) else json.dumps(motif, ensure_ascii=False)}


def main(argv):
    texte = Path(argv[0]).read_text(encoding="utf-8")
    b4 = Path(argv[1]).read_text(encoding="utf-8")
    lignes = texte.split("\n")
    idx = {}
    for i, x in enumerate(lignes):
        for k in lp.LIGNES:
            if x.startswith(f"| {k} |"):
                idx[k] = i
    assert list(idx) == list(lp.LIGNES), idx
    res = [essai("sain : candidat 1 tel quel", texte, "passe")]

    def avec(remplacements):
        l2 = list(lignes)
        for i, v in remplacements:
            l2[i] = v
        return "\n".join(l2)

    # une cellule changée d'un seul signe : on ajoute « x » à la fin de la cellule
    for k, i in idx.items():
        x = lignes[i]
        pos = [j for j, ch in enumerate(x) if ch == "|" and (j == 0 or x[j - 1] != "\\")]
        assert len(pos) == 4, (k, len(pos))
        for c, nom in ((1, "issue"), (2, "lecture")):
            fin = pos[c + 1]
            y = x[:fin].rstrip() + "x " + x[fin:]
            res.append(essai(f"cellule {k} {nom} : un signe ajouté", avec([(i, y)]), "refus"))
    # chaque ligne retirée
    for k, i in idx.items():
        l2 = [y for j, y in enumerate(lignes) if j != i]
        res.append(essai(f"ligne {k} retirée", "\n".join(l2), "refus"))
    # lignes en plus
    i11 = idx["L11"]
    for nom, extra in (("| L12 | issue ajoutée | non lu ; nœud |", "ligne en plus « | L12 | »"),
                       ("| L4bis | issue ajoutée | non lu ; nœud |", "ligne en plus « | L4bis | »"),
                       ("| **L12** | issue ajoutée | non lu ; nœud |", "ligne en plus « | **L12** | »"),
                       ("| M1 | issue ajoutée | non lu ; nœud |", "ligne en plus « | M1 | »"),
                       ("L12 | issue ajoutée | non lu ; nœud |", "ligne en plus sans barre initiale « L12 | … »")):
        l2 = lignes[:i11 + 1] + [nom] + lignes[i11 + 1:]
        res.append(essai(extra, "\n".join(l2), "refus"))
    # ligne en plus insérée au milieu de la table (entre L3 et L4), forme « | L3b | »
    i3 = idx["L3"]
    l2 = lignes[:i3 + 1] + ["| L3b | issue ajoutée | non lu ; nœud |"] + lignes[i3 + 1:]
    res.append(essai("ligne en plus « | L3b | » entre L3 et L4", "\n".join(l2), "refus"))
    # ordre changé (L3 et L4 échangées)
    res.append(essai("ordre : L3 et L4 échangées", avec([(idx["L3"], lignes[idx["L4"]]), (idx["L4"], lignes[idx["L3"]])]),
                     "refus"))
    # double espace dans une cellule
    x = lignes[idx["L5"]]
    res.append(essai("L5 : double espace dans la cellule issue", avec([(idx["L5"], x.replace("de C1", "de  C1", 1))]),
                     "refus"))
    # espace insécable
    res.append(essai("L5 : espace insécable à la place d'une espace",
                     avec([(idx["L5"], x.replace("de C1", "de C1", 1))]), "refus"))
    # barre échappée rendue nue dans L11
    x = lignes[idx["L11"]]
    res.append(essai("L11 : barre échappée rendue nue", avec([(idx["L11"], x.replace("\\|", "|"))]), "refus"))
    # signe moins (U+2212) devenu tiret
    res.append(essai("L11 : signe moins devenu tiret", avec([(idx["L11"], x.replace("−", "-"))]), "refus"))
    # brouillon 4
    res.append(essai("brouillon 4 (table du module v1)", b4, "refus"))
    # section dupliquée : une première section « Critères de lecture gelés » à la table changée, puis la vraie
    t = lignes.index("## Critères de lecture gelés")
    faux = [y.replace("non lu ; nœud |", "lu ; aucun nœud |") if y.startswith("| L5 |") else y
            for y in lignes[t:t + 20]]
    fin_sec = next(j for j in range(t + 1, len(lignes)) if lignes[j].startswith("## "))
    l2 = lignes[:t] + lignes[t:fin_sec] + [y.replace("| L5 | lecture de C1 en échec (motif écrit) | non lu ; nœud |",
                                                      "| L5 | lecture de C1 en échec (motif écrit) | lu ; aucun nœud |")
                                           for y in lignes[t:fin_sec]] + lignes[fin_sec:]
    # d'abord la section changée, puis la section vraie : inverser l'ordre des deux copies
    l3 = lignes[:t] + [y.replace("| L5 | lecture de C1 en échec (motif écrit) | non lu ; nœud |",
                                 "| L5 | lecture de C1 en échec (motif écrit) | lu ; aucun nœud |")
                       for y in lignes[t:fin_sec]] + lignes[t:fin_sec] + lignes[fin_sec:]
    assert "lu ; aucun nœud" in "\n".join(l3)
    res.append(essai("section « Critères de lecture gelés » en double : la première changée (L5), la seconde vraie",
                     "\n".join(l3), "refus"))
    res.append(essai("section « Critères de lecture gelés » en double : la première vraie, la seconde changée (L5)",
                     "\n".join(l2), "refus"))
    # espace de fin de ligne ajoutée (sans effet sur le contenu des cellules) : doit passer
    res.append(essai("espaces de fin de ligne ajoutées (contenu des cellules inchangé)",
                     "\n".join(y + "  " if y.startswith("| L") else y for y in lignes), "passe"))
    sortie = {"cas": len(res), "conformes": sum(r["conforme"] for r in res),
              "non_conformes": [r for r in res if not r["conforme"]], "detail": res}
    print(json.dumps(sortie, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main(sys.argv[1:])
