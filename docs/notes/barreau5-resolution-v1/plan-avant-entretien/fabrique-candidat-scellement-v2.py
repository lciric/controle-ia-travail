#!/usr/bin/env python3
"""Barreau 5 : fabrique et contrôle du candidat au scellement v2 du texte et de son devis.

Écrit par le rédacteur (Claude Fable 5.2), dans la nuit du 19 au 20 novembre 2026. Aucune donnée du programme.
Il repart du brouillon 4 vérifié et rejoue toute la chaîne, en cinq étapes :
  1. les 20 couples de la vérification du brouillon 4 (18 au texte et au devis ; les 2 de la fiche, hors candidat) ;
  2. les écritures du rédacteur au brouillon 5 -> état égal à l'octet au brouillon 5 scellé ;
  3. les 18 couples de l'erratum 1 -> empreintes annoncées par le contrôle de l'erratum ;
  4. les retouches de consolidation -> état égal à l'octet au premier candidat scellé (texte et devis) ;
  5. la section des marqueurs mise à l'état du scellement (`sections_candidat_scellement_v2.py`) : texte seulement.
Le devis v2 est le devis du premier candidat, à l'octet. Chaque « avant » doit se trouver une fois au moment où il
s'applique ; sinon arrêt, rien n'est écrit. Contrôles finals : chaque « après » présent à l'octet dans le candidat, ou
repris par une écriture postérieure nommée ; aucune marque ; validateur du dépôt. Sorties : les deux candidats v2
(une pièce scellée ne s'écrase jamais), la table de différence (« --table CHEMIN »), un compte rendu.
Les classes et fonctions de `fabrique-candidat-scellement-v1.py` sont réemployées telles quelles (chargées par runpy).
"""
from __future__ import annotations

import os
import runpy
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
sys.path.insert(0, ICI)
import sections_brouillon5_v1 as S5                                    # noqa: E402
import sections_candidat_scellement_v1 as SK                           # noqa: E402
import sections_candidat_scellement_v2 as SK2                          # noqa: E402

F1 = runpy.run_path(os.path.join(ICI, "fabrique-candidat-scellement-v1.py"), run_name="fabrique_v1")
Chaine, lire, e, MOTIF, NOMS, MARQUE = F1["Chaine"], F1["lire"], F1["e"], F1["MOTIF"], F1["NOMS"], F1["MARQUE"]
B4, B5, APRES_ERRATUM, ERRATUM, NOM = F1["B4"], F1["B5"], F1["APRES_ERRATUM"], F1["ERRATUM"], F1["NOM"]
CANDIDATS_V1 = {"T": (F1["CANDIDATS"]["T"], "54bf29c3f45ae0b2b0318b275948c836bc05aaada97c22a846a64fd776892df5"),
                "DV": (F1["CANDIDATS"]["DV"], "94a628a7714edfa5aabd84e52d37c71ba9ff8c029676390ed7b893de8a3c9f98")}
CANDIDATS = {"T": os.path.join(RACINE, "prereg", NOM + "-candidat-scellement-v2.md"),
             "DV": os.path.join(ICI, "devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md")}


def main():
    table = sys.argv[sys.argv.index("--table") + 1] if "--table" in sys.argv else None
    for chemin in list(CANDIDATS.values()) + ([table] if table else []):
        if os.path.exists(chemin) and (os.path.exists(chemin + ".sha256") or "--refaire" not in sys.argv):
            raise SystemExit(f"ARRÊT : {chemin} existe déjà (on n'écrase jamais une pièce scellée)")
    c = Chaine({k: lire(*B4[k]) for k in ("T", "DV")})
    fiche = lire(*B4["FI"])
    rapport = []
    dire = lambda x: (rapport.append(x), print(x))
    dire(f"départ : brouillon 4, texte {e(c.p['T'])}, devis {e(c.p['DV'])}")
    bornes = []

    # ---- 1
    v = runpy.run_path(os.path.join(ICI, "outils-verification-plan-brouillon4-v1", "couples-verification-brouillon4-v1.py"),
                       run_name="verificateur")
    cle = {v["T"]: "T", v["DV"]: "DV", v["FI"]: "FI"}
    n_fiche = 0
    for ident, constat, touche, piece, avant, apres in v["COUPLES"]:
        if cle[piece] == "FI":
            if fiche.count(avant) != 1:
                raise SystemExit(f"ARRÊT : {ident} : « avant » trouvé {fiche.count(avant)} fois dans la fiche v4")
            fiche = fiche.replace(avant, apres); n_fiche += 1
        else:
            c.une_fois("1. vérification du brouillon 4", ident, "couple du vérificateur (" + touche + ")", cle[piece], avant, apres)
    bornes.append(len(c.journal))
    dire(f"étape 1 : {len(v['COUPLES'])} couples du vérificateur : {bornes[-1]} au texte et au devis, {n_fiche} à la fiche (hors candidat)")

    # ---- 2
    sorte = {"lazar": "mot de Lazar écrit comme décidé", "tenue": "tenue du brouillon 5"}
    for nom, s, avant, apres in S5.RETOUCHES_TEXTE:
        c.une_fois("2. brouillon 5", nom, sorte[s], "T", avant, apres)
    for nom, s, avant, apres, attendu in S5.PARTOUT_TEXTE:
        c.partout("2. brouillon 5", nom, sorte[s], "T", avant, apres, attendu)
    for nom, s, prefixe, nouvelle, ajouter in S5.LIGNES_TEXTE:
        c.ligne("2. brouillon 5", nom, sorte[s], "T", prefixe, nouvelle, ajouter)
    for nom, s, debut, fin, nouveau in S5.BLOCS_TEXTE:
        c.bloc("2. brouillon 5", nom, sorte[s], "T", debut, fin, nouveau)
    for nom, s, avant, apres in S5.RETOUCHES_DEVIS:
        c.une_fois("2. brouillon 5", nom, sorte[s], "DV", avant, apres)
    for k in ("T", "DV"):
        if c.p[k] != lire(*B5[k]):
            raise SystemExit(f"ARRÊT : après l'étape 2, le {NOMS[k]} n'égale pas le brouillon 5 scellé")
    dire(f"étape 2 : {len(c.journal) - bornes[-1]} écritures du brouillon 5 ; état égal à l'octet au brouillon 5 scellé : texte {e(c.p['T'])}, devis {e(c.p['DV'])}")
    bornes.append(len(c.journal))

    # ---- 3
    for m in MOTIF.finditer(lire(*ERRATUM)):
        c.une_fois("3. erratum 1", m["nom"], "couple de l'erratum 1", m["piece"], m["avant"], m["apres"], m["ou"])
    for k in ("T", "DV"):
        if e(c.p[k]) != APRES_ERRATUM[k]:
            raise SystemExit(f"ARRÊT : après l'erratum, le {NOMS[k]} a l'empreinte {e(c.p[k])}")
    dire(f"étape 3 : {len(c.journal) - bornes[-1]} couples de l'erratum 1 ; empreintes : texte {e(c.p['T'])}, devis {e(c.p['DV'])} (égales à celles annoncées)")
    bornes.append(len(c.journal))

    # ---- 4
    for nom, avant, apres in SK.RETOUCHES_TEXTE:
        c.une_fois("4. consolidation", nom, "retouche de consolidation", "T", avant, apres)
    for nom, avant, apres, attendu in SK.PARTOUT_TEXTE:
        c.partout("4. consolidation", nom, "retouche de consolidation", "T", avant, apres, attendu)
    for nom, prefixe, nouvelle, ajouter in SK.LIGNES_TEXTE:
        c.ligne("4. consolidation", nom, "retouche de consolidation", "T", prefixe, nouvelle, ajouter)
    for nom, avant, apres in SK.RETOUCHES_DEVIS:
        c.une_fois("4. consolidation", nom, "retouche de consolidation", "DV", avant, apres)
    for k in ("T", "DV"):
        if c.p[k] != lire(*CANDIDATS_V1[k]):
            raise SystemExit(f"ARRÊT : après l'étape 4, le {NOMS[k]} n'égale pas le premier candidat scellé")
    dire(f"étape 4 : {len(c.journal) - bornes[-1]} retouches de consolidation ; état égal à l'octet au premier candidat scellé : texte {e(c.p['T'])}, devis {e(c.p['DV'])}")
    bornes.append(len(c.journal))

    # ---- 5
    for nom, s, avant, apres in SK2.RETOUCHES_TEXTE:
        c.une_fois("5. marqueurs", nom, s, "T", avant, apres)
    for nom, s, avant, apres, attendu in SK2.PARTOUT_TEXTE:
        c.partout("5. marqueurs", nom, s, "T", avant, apres, attendu)
    dire(f"étape 5 : {len(c.journal) - bornes[-1]} écritures (texte seulement) ; candidat v2 : texte {e(c.p['T'])} ; devis {e(c.p['DV'])}, à l'octet celui du premier candidat")

    # ---- contrôles finals
    defauts = 0

    def touche(a, b):
        return a in b or b in a or any(a[i:i + 40] in b for i in range(0, max(1, len(a) - 40), 10))
    for i, j in enumerate(c.journal):
        final = c.p[j["piece"]]
        j["present"] = final.count(j["apres"]) >= 1
        j["ligne"] = final.count("\n", 0, final.index(j["apres"])) + 1 if j["present"] else None
        if not j["present"]:
            j["repris"] = [x["nom"] for x in c.journal[i + 1:] if x["piece"] == j["piece"] and touche(x["avant"], j["apres"])]
            defauts += not j["repris"]
    absents = [j for j in c.journal if not j["present"]]
    dire(f"écritures : {len(c.journal)} ; « après » présents à l'octet dans le candidat v2 : {len(c.journal) - len(absents)} ; repris par une écriture postérieure : {len(absents)}")
    for j in absents:
        dire(f"  {j['etape']} {j['nom']} ({NOMS[j['piece']]}) : repris par {j.get('repris') or 'RIEN : DÉFAUT'}")
    couples = [j for j in c.journal if j["sorte"].startswith("couple du vérificateur") or j["sorte"].startswith("couple de l'erratum")]
    perdus = [j["nom"] for j in couples if not j["present"]]
    dire(f"couples du vérificateur et de l'erratum : {len(couples)} ; non présents à l'octet : {perdus or 'aucun'}")
    defauts += len(perdus)
    for k in ("T", "DV"):
        n = c.p[k].count(MARQUE)
        dire(f"marques « {MARQUE} » dans le {NOMS[k]} : {n}")
        defauts += n
    dire(f"restes dans le texte : « à remplir avant le scellement » {c.p['T'].count('à remplir avant le scellement')} ; « différentiel du brouillon 5 » {c.p['T'].count('différentiel du brouillon 5')} ; « restent le plafond » {c.p['T'].count('restent le plafond')} ; « table-difference-candidat-scellement-v1.md » {c.p['T'].count('table-difference-candidat-scellement-v1.md')}")
    dire(f"« rapprochement non fait au scellement » dans le texte : {c.p['T'].count('rapprochement non fait au scellement')} fois")
    for k, chemin in CANDIDATS.items():
        open(chemin, "w", encoding="utf-8").write(c.p[k])
    egal = open(CANDIDATS["DV"], "rb").read() == open(CANDIDATS_V1["DV"][0], "rb").read()
    dire(f"devis v2 égal à l'octet au devis du premier candidat : {'oui' if egal else 'NON'}")
    defauts += not egal
    sys.path.insert(0, os.path.join(RACINE, "src"))
    from controle_ia.prereg import problemes
    pb = problemes(CANDIDATS["T"])
    dire(f"validateur du dépôt sur le candidat v2 du texte : {pb or 'aucun problème'}")
    defauts += len(pb)
    dire(f"écrits : {os.path.relpath(CANDIDATS['T'], RACINE)} ({len(c.p['T'])} signes) ; {os.path.relpath(CANDIDATS['DV'], RACINE)} ({len(c.p['DV'])} signes)")
    dire(f"défauts : {defauts}")

    if table:
        court = lambda s, n=150: (s[:n] + " […]") if len(s) > n else s
        cell = lambda s: court(s.replace("\n", " ⏎ ")).replace("|", "\\|")
        L = ["# Table de différence — candidat au scellement v2 du plan « sabotage ou empreinte de l'adaptateur » (barreau 5)", "",
             "Écrite par le programme `fabrique-candidat-scellement-v2.py` du rédacteur (Claude Fable 5.2), pour le contre-lecteur. Elle énumère tout ce qui sépare le candidat v2 du brouillon 4 vérifié. Elle remplace la table du premier candidat. Aucune donnée du programme.", "",
             "## Compte rendu du programme", ""] + ["- " + x for x in rapport] + ["",
             "## Toutes les écritures, dans l'ordre où elles s'appliquent", "",
             "« ligne » : ligne du candidat v2 où commence l'« après ». « repris » : l'« après » n'est plus à l'octet, une écriture postérieure, nommée, l'a modifié.", "",
             "| étape | repère | pièce | sorte | forme | début de l'« avant » | à l'octet dans le candidat v2 |", "|---|---|---|---|---|---|---|"]
        for j in c.journal:
            etat = f"oui, ligne {j['ligne']}" if j["present"] else "repris par " + ", ".join(j.get("repris") or ["?"])
            L.append(f"| {j['etape']} | {j['nom']} | {NOMS[j['piece']]} | {j['sorte']} | {j['forme']} | {cell(j['avant'])} | {etat} |")
        for titre, debut, fin in (("Étape 4 : les retouches de consolidation, en entier", bornes[2], bornes[3]),
                                  ("Étape 5 : la section des marqueurs à l'état du scellement, en entier", bornes[3], len(c.journal))):
            L += ["", f"## {titre}", ""]
            for j in c.journal[debut:fin]:
                L += [f"### {j['nom']} — {NOMS[j['piece']]} — {j['sorte']} — {j['forme']}", "", "Avant :", "", "```text", j["avant"].rstrip("\n"), "```", "",
                      "Après :", "", "```text", j["apres"].rstrip("\n"), "```", ""]
        open(table, "w", encoding="utf-8").write("\n".join(L) + "\n")
        print(f"table écrite : {os.path.relpath(table, RACINE)}")
    sys.exit(1 if defauts else 0)


if __name__ == "__main__":
    main()
