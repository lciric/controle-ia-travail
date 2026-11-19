#!/usr/bin/env python3
"""Vérification du candidat au scellement v2 (barreau 5) : rejeu en mémoire de la chaîne du rédacteur, et mes 20 couples (v1).

Écrit par le vérificateur (Claude Opus 5.5) le 19 novembre 2026 au soir (UTC). Ne lit que des textes du dépôt ; n'écrit rien : la sortie
standard seule. La fabrique du rédacteur (`fabrique-candidat-scellement-v2.py`) écrit ses pièces dans sa fonction `main` :
je ne la lance pas. Je charge ses objets (classe `Chaine`, listes d'écritures des modules de sections, couples de
l'erratum) sans exécuter `main`, je rejoue ses cinq étapes en mémoire, dans le même ordre, et je compare à l'octet le
résultat au candidat v2 scellé (texte et devis) et aux états intermédiaires scellés (brouillon 5, premier candidat).
Puis je cherche à l'octet, dans le candidat v2, l'« après » de chacun de mes 20 couples de la vérification du brouillon 4.
"""
from __future__ import annotations

import hashlib
import runpy
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
PLAN = ICI.parent
RACINE = PLAN.parents[3]
T2 = RACINE / "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md"
DV2 = PLAN / "devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md"
FICHE = PLAN / "fiche-v5-lazar-v1.md"                    # la fiche v4 (a88a3a12…) avec mes deux couples de la fiche
ATTENDU = {T2: "088e15ef", DV2: "94a628a7", FICHE: "25a37968"}


def empreinte(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main():
    sys.path.insert(0, str(PLAN))
    F2 = runpy.run_path(str(PLAN / "fabrique-candidat-scellement-v2.py"), run_name="fabrique_v2_charge_sans_main")
    Chaine, lire, MOTIF = F2["Chaine"], F2["lire"], F2["MOTIF"]
    B4, B5, ERRATUM, APRES = F2["B4"], F2["B5"], F2["ERRATUM"], F2["APRES_ERRATUM"]
    CV1 = F2["CANDIDATS_V1"]
    S5, SK, SK2 = F2["S5"], F2["SK"], F2["SK2"]
    print("# Rejeu en mémoire de la chaîne du rédacteur — sortie (v1)\n")
    for p, debut in ATTENDU.items():
        h = empreinte(p.read_bytes())
        print(f"- {p.relative_to(RACINE)} : {h[:16]}… ({'attendue' if h.startswith(debut) else 'INATTENDUE'})")
    c = Chaine({k: lire(*B4[k]) for k in ("T", "DV")})
    v = runpy.run_path(str(PLAN / "outils-verification-plan-brouillon4-v1/couples-verification-brouillon4-v1.py"),
                       run_name="verificateur")
    cle = {v["T"]: "T", v["DV"]: "DV", v["FI"]: "FI"}
    for ident, _constat, touche, piece, avant, apres in v["COUPLES"]:
        if cle[piece] != "FI":
            c.une_fois("1", ident, "couple du vérificateur (" + touche + ")", cle[piece], avant, apres)
    print(f"\nétape 1 : {len(c.journal)} de mes couples appliqués au texte et au devis")
    sorte = {"lazar": "mot de Lazar", "tenue": "tenue"}
    for nom, s, avant, apres in S5.RETOUCHES_TEXTE:
        c.une_fois("2", nom, sorte[s], "T", avant, apres)
    for nom, s, avant, apres, attendu in S5.PARTOUT_TEXTE:
        c.partout("2", nom, sorte[s], "T", avant, apres, attendu)
    for nom, s, prefixe, nouvelle, ajouter in S5.LIGNES_TEXTE:
        c.ligne("2", nom, sorte[s], "T", prefixe, nouvelle, ajouter)
    for nom, s, debut, fin, nouveau in S5.BLOCS_TEXTE:
        c.bloc("2", nom, sorte[s], "T", debut, fin, nouveau)
    for nom, s, avant, apres in S5.RETOUCHES_DEVIS:
        c.une_fois("2", nom, sorte[s], "DV", avant, apres)
    print("étape 2 : égal à l'octet au brouillon 5 scellé : "
          + ", ".join(f"{k} {c.p[k] == lire(*B5[k])}" for k in ("T", "DV")))
    n = len(c.journal)
    for m in MOTIF.finditer(lire(*ERRATUM)):
        c.une_fois("3", m["nom"], "couple de l'erratum 1", m["piece"], m["avant"], m["apres"], m["ou"])
    print(f"étape 3 : {len(c.journal) - n} couples de l'erratum ; empreintes annoncées : "
          + ", ".join(f"{k} {empreinte(c.p[k].encode()) == APRES[k]}" for k in ("T", "DV")))
    for nom, avant, apres in SK.RETOUCHES_TEXTE:
        c.une_fois("4", nom, "consolidation", "T", avant, apres)
    for nom, avant, apres, attendu in SK.PARTOUT_TEXTE:
        c.partout("4", nom, "consolidation", "T", avant, apres, attendu)
    for nom, prefixe, nouvelle, ajouter in SK.LIGNES_TEXTE:
        c.ligne("4", nom, "consolidation", "T", prefixe, nouvelle, ajouter)
    for nom, avant, apres in SK.RETOUCHES_DEVIS:
        c.une_fois("4", nom, "consolidation", "DV", avant, apres)
    print("étape 4 : égal à l'octet au premier candidat scellé : "
          + ", ".join(f"{k} {c.p[k] == lire(*CV1[k])}" for k in ("T", "DV")))
    n = len(c.journal)
    for nom, s, avant, apres in SK2.RETOUCHES_TEXTE:
        c.une_fois("5", nom, s, "T", avant, apres)
    for nom, s, avant, apres, attendu in SK2.PARTOUT_TEXTE:
        c.partout("5", nom, s, "T", avant, apres, attendu)
    print(f"étape 5 : {len(c.journal) - n} écritures")
    t2, dv2 = T2.read_text(encoding="utf-8"), DV2.read_text(encoding="utf-8")
    print(f"\nrésultat égal à l'octet au candidat v2 scellé : texte {c.p['T'] == t2} ; devis {c.p['DV'] == dv2}")
    print(f"écritures rejouées : {len(c.journal)}")
    print("\n## Mes 20 couples dans le candidat v2 (« après » à l'octet)\n")
    fiche = FICHE.read_text(encoding="utf-8")
    cible = {"T": t2, "DV": dv2, "FI": fiche}
    for ident, _constat, _touche, piece, _avant, apres in v["COUPLES"]:
        k = cle[piece]
        lieu = "candidat v2, texte" if k == "T" else ("candidat v2, devis" if k == "DV" else "fiche v5 (hors candidat)")
        print(f"{ident:6s} {lieu} : {cible[k].count(apres)} fois")


if __name__ == "__main__":
    main()
