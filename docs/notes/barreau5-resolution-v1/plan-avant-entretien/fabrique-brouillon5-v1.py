#!/usr/bin/env python3
"""Barreau 5 : fabrique du brouillon 5 du texte, de son devis et de la fiche, à partir du brouillon 4 (v1).

Écrit par le rédacteur (Claude Fable 5.2), dans la nuit du 19 au 20 novembre 2026. Aucune donnée du programme.
  1. les 20 couples de la vérification du brouillon 4, à la lettre, dans leur ordre (liste `COUPLES` du programme du
     vérificateur, chargée telle quelle) ;
  2. les écritures du rédacteur (`sections_brouillon5_v1.py`) : mots de Lazar écrits comme décidés, tenue du brouillon.
Chaque « avant » doit se trouver une seule fois au moment où il s'applique ; sinon le programme s'arrête sans rien écrire.
Sorties : texte, devis et fiche du brouillon 5 (une sortie scellée ne s'écrase jamais), compte rendu sur la sortie
standard. Avec « --erratum », voir `fabrique-erratum-brouillon5-v1.py` : ce programme-ci ne lève aucune marque.
"""
from __future__ import annotations

import hashlib
import os
import runpy
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
NOM = "barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1"
ENTREES = {"T": (os.path.join(RACINE, "prereg", NOM + "-brouillon4.md"), "dbe66dc9"),
           "DV": (os.path.join(ICI, "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md"), "084cd547"),
           "FI": (os.path.join(ICI, "fiche-v4-lazar-v1.md"), "a88a3a12")}
SORTIES = {"T": os.path.join(RACINE, "prereg", NOM + "-brouillon5.md"),
           "DV": os.path.join(ICI, "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon5.md"),
           "FI": os.path.join(ICI, "fiche-v5-lazar-v1.md")}
sys.path.insert(0, ICI)
import sections_brouillon5_v1 as S                                     # noqa: E402


def dire(x):
    print(x)


def une_fois(t, avant, apres, nom):
    n = t.count(avant)
    if n != 1:
        raise SystemExit(f"ARRÊT : {nom} : « avant » trouvé {n} fois : {avant[:90]!r}")
    return t.replace(avant, apres)


def ligne(t, prefixe, nouvelle, nom, ajouter):
    lignes = t.split("\n")
    idx = [i for i, l in enumerate(lignes) if l.startswith(prefixe)]
    if len(idx) != 1:
        raise SystemExit(f"ARRÊT : {nom} : {len(idx)} lignes commencent par {prefixe!r}")
    lignes[idx[0]] = (lignes[idx[0]] + "\n" + nouvelle) if ajouter else nouvelle
    return "\n".join(lignes)


def bloc(t, debut, fin, nouveau, nom):
    if t.count(debut) != 1:
        raise SystemExit(f"ARRÊT : {nom} : début trouvé {t.count(debut)} fois")
    i = t.index(debut)
    return t[:i] + nouveau + t[t.index(fin, i + len(debut)):]


def main():
    for chemin in SORTIES.values():
        if os.path.exists(chemin) and (os.path.exists(chemin + ".sha256") or "--refaire" not in sys.argv):
            raise SystemExit(f"ARRÊT : {chemin} existe déjà (on n'écrase jamais une pièce scellée)")
    p = {}
    for k, (chemin, attendu) in ENTREES.items():
        p[k] = open(chemin, encoding="utf-8").read()
        e = hashlib.sha256(p[k].encode()).hexdigest()
        if not e.startswith(attendu):
            raise SystemExit(f"ARRÊT : {chemin} : empreinte {e[:8]} au lieu de {attendu}")

    # ------------------------------------------------------------ 1. les 20 couples du vérificateur, à la lettre
    v = runpy.run_path(os.path.join(ICI, "outils-verification-plan-brouillon4-v1", "couples-verification-brouillon4-v1.py"),
                       run_name="verificateur")
    cle = {v["T"]: "T", v["DV"]: "DV", v["FI"]: "FI"}
    couples = [(c[0], c[2], cle[c[3]], c[4], c[5]) for c in v["COUPLES"]]
    if len(couples) != 20:
        raise SystemExit(f"ARRÊT : {len(couples)} couples au lieu de 20")
    for nom, touche, k, avant, apres in couples:
        p[k] = une_fois(p[k], avant, apres, nom)
    dire(f"couples de la vérification du brouillon 4 appliqués : {len(couples)} "
         f"(texte {sum(c[2] == 'T' for c in couples)}, devis {sum(c[2] == 'DV' for c in couples)}, fiche {sum(c[2] == 'FI' for c in couples)})")

    # ------------------------------------------------------------ 2. écritures du rédacteur
    journal = []
    for nom, sorte, avant, apres in S.RETOUCHES_TEXTE:
        p["T"] = une_fois(p["T"], avant, apres, nom); journal.append(("texte", nom, sorte))
    for nom, sorte, avant, apres, attendu in S.PARTOUT_TEXTE:
        if p["T"].count(avant) != attendu:
            raise SystemExit(f"ARRÊT : {nom} : trouvé {p['T'].count(avant)} fois au lieu de {attendu}")
        p["T"] = p["T"].replace(avant, apres); journal.append(("texte", nom, sorte))
    for nom, sorte, prefixe, nouvelle, ajouter in S.LIGNES_TEXTE:
        p["T"] = ligne(p["T"], prefixe, nouvelle, nom, ajouter); journal.append(("texte", nom, sorte))
    for nom, sorte, debut, fin, nouveau in S.BLOCS_TEXTE:
        p["T"] = bloc(p["T"], debut, fin, nouveau, nom); journal.append(("texte", nom, sorte))
    for nom, sorte, avant, apres in S.RETOUCHES_DEVIS:
        p["DV"] = une_fois(p["DV"], avant, apres, nom); journal.append(("devis", nom, sorte))
    for nom, sorte, avant, apres in S.RETOUCHES_FICHE:
        p["FI"] = une_fois(p["FI"], avant, apres, nom); journal.append(("fiche", nom, sorte))
    for piece, nom, sorte in journal:
        dire(f"  écriture du rédacteur : {piece:5s} {sorte:5s} {nom}")
    dire(f"écritures du rédacteur : {len(journal)} (mots de Lazar : {sum(j[2] == 'lazar' for j in journal)} ; tenue du brouillon : {sum(j[2] == 'tenue' for j in journal)})")

    # ------------------------------------------------------------ contrôles
    for nom, touche, k, avant, apres in couples:
        dire(f"  {nom:6s} {k:2s} ({touche}) « après » présent à l'octet dans la pièce finale : {'oui' if p[k].count(apres) == 1 else 'non'}")
    marque = "[à confirmer par le rapport v4]"
    dire(f"marques « {marque} » : texte {p['T'].count(marque)}, devis {p['DV'].count(marque)}")
    for mot in ("demandé 200", "Lazar peut dire", "si Lazar le dit", "Si Lazar l'accorde", "brouillon4.md"):
        dire(f"  reste « {mot} » : texte {p['T'].count(mot)}, devis {p['DV'].count(mot)}")
    sys.path.insert(0, os.path.join(RACINE, "src"))
    for k, chemin in SORTIES.items():
        open(chemin, "w", encoding="utf-8").write(p[k])
        dire(f"écrit : {os.path.relpath(chemin, RACINE)} : {len(p[k])} signes, {hashlib.sha256(p[k].encode()).hexdigest()}")
    from controle_ia.prereg import problemes
    dire(f"validateur du dépôt sur le texte : {problemes(SORTIES['T']) or 'aucun problème'}")


if __name__ == "__main__":
    main()
