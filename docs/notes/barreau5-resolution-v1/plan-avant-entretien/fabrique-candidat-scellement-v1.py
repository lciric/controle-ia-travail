#!/usr/bin/env python3
"""Barreau 5 : fabrique et contrôle du candidat au scellement du texte et de son devis (v1).

Écrit par le rédacteur (Claude Fable 5.2), dans la nuit du 19 au 20 novembre 2026. Aucune donnée du programme.
Il repart du brouillon 4 vérifié et rejoue toute la chaîne, en quatre étapes :
  1. les 20 couples de la vérification du brouillon 4 (18 visent le texte et le devis ; les 2 de la fiche sont rejoués
     à part, sur la fiche v4, pour le compte) ;
  2. les écritures du rédacteur au brouillon 5 (`sections_brouillon5_v1.py` : mots de Lazar, tenue du brouillon) ;
     -> l'état doit égaler, à l'octet, le brouillon 5 scellé ;
  3. les 18 couples de l'erratum 1 (lus dans `erratum-1-brouillon5-plan-sabotage-ou-empreinte-v1.md`) ;
     -> l'état doit avoir les empreintes annoncées par `controle-erratum-1-brouillon5-v1.py` ;
  4. les retouches de consolidation (`sections_candidat_scellement_v1.py`).
Chaque « avant » doit se trouver une fois au moment où il s'applique ; sinon arrêt, rien n'est écrit.
Contrôles finals : chaque « après » présent à l'octet dans le candidat, ou repris par une écriture nommée ; aucune
marque ; validateur du dépôt. Sorties : les deux candidats (une pièce scellée ne s'écrase jamais), une table de
différence en Markdown (option « --table CHEMIN »), et un compte rendu sur la sortie standard.
"""
from __future__ import annotations

import hashlib
import os
import re
import runpy
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
sys.path.insert(0, ICI)
import sections_brouillon5_v1 as S5                                    # noqa: E402
import sections_candidat_scellement_v1 as SK                           # noqa: E402

NOM = SK.NOM
B4 = {"T": (os.path.join(RACINE, "prereg", NOM + "-brouillon4.md"), SK.E_B4),
      "DV": (os.path.join(ICI, "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md"), "084cd547"),
      "FI": (os.path.join(ICI, "fiche-v4-lazar-v1.md"), "a88a3a12")}
B5 = {"T": (os.path.join(RACINE, "prereg", NOM + "-brouillon5.md"), SK.E_B5),
      "DV": (os.path.join(ICI, "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon5.md"), SK.E_DV5)}
APRES_ERRATUM = {"T": SK.E_B5_ERRATUM, "DV": SK.E_DV5_ERRATUM}
ERRATUM = (os.path.join(ICI, "erratum-1-brouillon5-plan-sabotage-ou-empreinte-v1.md"), SK.E_ERRATUM)
CANDIDATS = {"T": os.path.join(RACINE, "prereg", NOM + "-candidat-scellement.md"),
             "DV": os.path.join(ICI, "devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement.md")}
MARQUE = "[à confirmer par le rapport v4]"
MOTIF = re.compile(r"#### Couple (?P<nom>[A-Z]+-\d+[a-z]) — (?P<piece>T|DV) — (?P<ou>[^\n]*)\n\nAvant :\n\n```text\n(?P<avant>.*?)\n```\n\n"
                   r"Après :\n\n```text\n(?P<apres>.*?)\n```\n", re.S)
NOMS = {"T": "texte", "DV": "devis"}


def e(texte):
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def lire(chemin, attendu):
    t = open(chemin, encoding="utf-8").read()
    if not e(t).startswith(attendu):
        raise SystemExit(f"ARRÊT : {chemin} : empreinte {e(t)[:16]} au lieu de {attendu[:16]}")
    return t


class Chaine:
    """Applique des écritures à des copies en mémoire, et garde le journal de chacune."""

    def __init__(self, pieces):
        self.p, self.journal = pieces, []

    def une_fois(self, etape, nom, sorte, k, avant, apres, ou=""):
        n = self.p[k].count(avant)
        if n != 1:
            raise SystemExit(f"ARRÊT : {etape} {nom} : « avant » trouvé {n} fois dans le {NOMS[k]} : {avant[:80]!r}")
        deja = 0 if avant in apres else self.p[k].count(apres)
        if deja:
            raise SystemExit(f"ARRÊT : {etape} {nom} : « après » déjà présent {deja} fois")
        self.p[k] = self.p[k].replace(avant, apres)
        self.journal.append(dict(etape=etape, nom=nom, sorte=sorte, piece=k, forme="couple", avant=avant, apres=apres, ou=ou))

    def partout(self, etape, nom, sorte, k, avant, apres, attendu):
        if self.p[k].count(avant) != attendu:
            raise SystemExit(f"ARRÊT : {etape} {nom} : trouvé {self.p[k].count(avant)} fois au lieu de {attendu}")
        self.p[k] = self.p[k].replace(avant, apres)
        self.journal.append(dict(etape=etape, nom=nom, sorte=sorte, piece=k, forme=f"{attendu} occurrences", avant=avant, apres=apres, ou=""))

    def ligne(self, etape, nom, sorte, k, prefixe, nouvelle, ajouter):
        lignes = self.p[k].split("\n")
        idx = [i for i, l in enumerate(lignes) if l.startswith(prefixe)]
        if len(idx) != 1:
            raise SystemExit(f"ARRÊT : {etape} {nom} : {len(idx)} lignes commencent par {prefixe!r}")
        avant = lignes[idx[0]]
        lignes[idx[0]] = (avant + "\n" + nouvelle) if ajouter else nouvelle
        self.p[k] = "\n".join(lignes)
        self.journal.append(dict(etape=etape, nom=nom, sorte=sorte, piece=k, forme="ligne ajoutée après" if ajouter else "ligne remplacée",
                                 avant=avant, apres=nouvelle, ou=""))

    def bloc(self, etape, nom, sorte, k, debut, fin, nouveau):
        if self.p[k].count(debut) != 1:
            raise SystemExit(f"ARRÊT : {etape} {nom} : début trouvé {self.p[k].count(debut)} fois")
        i = self.p[k].index(debut)
        j = self.p[k].index(fin, i + len(debut))
        avant = self.p[k][i:j]
        self.p[k] = self.p[k][:i] + nouveau + self.p[k][j:]
        self.journal.append(dict(etape=etape, nom=nom, sorte=sorte, piece=k, forme="bloc remplacé", avant=avant, apres=nouveau, ou=""))


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

    # ---------------------------------------------------------------- 1. les 20 couples de la vérification du brouillon 4
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
    dire(f"étape 1 : {len(v['COUPLES'])} couples du vérificateur : {len(c.journal)} au texte et au devis, {n_fiche} à la fiche (hors candidat)")

    # ---------------------------------------------------------------- 2. écritures du brouillon 5
    n1 = len(c.journal)
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
        if e(c.p[k]) != B5[k][1] or c.p[k] != lire(*B5[k]):
            raise SystemExit(f"ARRÊT : après l'étape 2, le {NOMS[k]} n'égale pas le brouillon 5 scellé")
    dire(f"étape 2 : {len(c.journal) - n1} écritures du brouillon 5 ; état égal à l'octet au brouillon 5 scellé : texte {e(c.p['T'])}, devis {e(c.p['DV'])}")

    # ---------------------------------------------------------------- 3. les 18 couples de l'erratum 1
    n2 = len(c.journal)
    for m in MOTIF.finditer(lire(*ERRATUM)):
        c.une_fois("3. erratum 1", m["nom"], "couple de l'erratum 1", m["piece"], m["avant"], m["apres"], m["ou"])
    for k in ("T", "DV"):
        if e(c.p[k]) != APRES_ERRATUM[k]:
            raise SystemExit(f"ARRÊT : après l'erratum, le {NOMS[k]} a l'empreinte {e(c.p[k])} au lieu de {APRES_ERRATUM[k]}")
    dire(f"étape 3 : {len(c.journal) - n2} couples de l'erratum 1 ; empreintes AVANT les retouches de consolidation : texte {e(c.p['T'])}, devis {e(c.p['DV'])} (égales à celles annoncées)")

    # ---------------------------------------------------------------- 4. retouches de consolidation
    n3 = len(c.journal)
    for nom, avant, apres in SK.RETOUCHES_TEXTE:
        c.une_fois("4. consolidation", nom, "retouche de consolidation", "T", avant, apres)
    for nom, avant, apres, attendu in SK.PARTOUT_TEXTE:
        c.partout("4. consolidation", nom, "retouche de consolidation", "T", avant, apres, attendu)
    for nom, prefixe, nouvelle, ajouter in SK.LIGNES_TEXTE:
        c.ligne("4. consolidation", nom, "retouche de consolidation", "T", prefixe, nouvelle, ajouter)
    for nom, avant, apres in SK.RETOUCHES_DEVIS:
        c.une_fois("4. consolidation", nom, "retouche de consolidation", "DV", avant, apres)
    dire(f"étape 4 : {len(c.journal) - n3} retouches de consolidation ; empreintes APRÈS : texte {e(c.p['T'])}, devis {e(c.p['DV'])}")

    # ---------------------------------------------------------------- contrôles finals
    defauts = 0
    for j in c.journal:
        final = c.p[j["piece"]]
        n = final.count(j["apres"])
        j["present"] = n >= 1
        j["ligne"] = final.count("\n", 0, final.index(j["apres"])) + 1 if n else None
        if not n:                                     # repris par une écriture postérieure : laquelle ?
            suite = [x["nom"] for x in c.journal[c.journal.index(j) + 1:] if x["piece"] == j["piece"]
                     and (x["avant"] in j["apres"] or j["apres"] in x["avant"] or any(l and l in j["apres"] for l in x["avant"].split("\n")[:1]))]
            j["repris"] = suite
            if not suite:
                defauts += 1
    absents = [j for j in c.journal if not j["present"]]
    dire(f"écritures : {len(c.journal)} ; « après » présents à l'octet dans le candidat : {len(c.journal) - len(absents)} ; repris par une écriture postérieure : {len(absents)}")
    for j in absents:
        dire(f"  {j['etape']} {j['nom']} ({NOMS[j['piece']]}) : repris par {j.get('repris') or 'RIEN : DÉFAUT'}")
    couples = [j for j in c.journal if j["sorte"].startswith("couple")]
    perdus = [j["nom"] for j in couples if not j["present"]]
    dire(f"couples du vérificateur et de l'erratum : {len(couples)} ; non présents à l'octet : {perdus or 'aucun'}")
    defauts += len(perdus)
    for k in ("T", "DV"):
        n = c.p[k].count(MARQUE)
        dire(f"marques « {MARQUE} » dans le {NOMS[k]} : {n}")
        defauts += n
        for mot in ("brouillon5.md", "brouillon4.md"):
            dire(f"  reste « {mot} » dans le {NOMS[k]} : {c.p[k].count(mot)}")
    dire(f"nom définitif du texte, dans le texte : {c.p['T'].count('prereg/' + NOM + '.md')} fois ; dans le devis : {c.p['DV'].count('prereg/' + NOM + '.md')} fois")
    for nom, motif, avant, apres in SK.PROPOSITIONS:
        n = c.p["T"].count(avant)
        dire(f"proposition NON appliquée {nom} : « avant » trouvé {n} fois dans le candidat")
        defauts += n != 1
    for k, chemin in CANDIDATS.items():
        open(chemin, "w", encoding="utf-8").write(c.p[k])
    sys.path.insert(0, os.path.join(RACINE, "src"))
    from controle_ia.prereg import problemes
    pb = problemes(CANDIDATS["T"])
    dire(f"validateur du dépôt sur le candidat du texte : {pb or 'aucun problème'}")
    defauts += len(pb)
    dire(f"écrits : {os.path.relpath(CANDIDATS['T'], RACINE)} ({len(c.p['T'])} signes) ; {os.path.relpath(CANDIDATS['DV'], RACINE)} ({len(c.p['DV'])} signes)")
    dire(f"défauts : {defauts}")

    if table:
        court = lambda s, n=150: (s[:n] + " […]") if len(s) > n else s
        cell = lambda s: court(s.replace("\n", " ⏎ ")).replace("|", "\\|")
        L = ["# Table de différence — candidat au scellement du plan « sabotage ou empreinte de l'adaptateur » (barreau 5) — v1", "",
             "Écrite par le programme `fabrique-candidat-scellement-v1.py` du rédacteur (Claude Fable 5.2), pour le contre-lecteur. Elle énumère tout ce qui sépare le candidat du brouillon 4 vérifié. Aucune donnée du programme.", "",
             "## Compte rendu du programme", ""] + ["- " + x for x in rapport] + ["",
             "## Toutes les écritures, dans l'ordre où elles s'appliquent", "",
             "« ligne » : ligne du candidat où commence l'« après ». « repris » : l'« après » n'est plus à l'octet, une écriture postérieure, nommée, l'a modifié.", "",
             "| étape | repère | pièce | sorte | forme | début de l'« avant » | à l'octet dans le candidat |", "|---|---|---|---|---|---|---|"]
        for j in c.journal:
            etat = f"oui, ligne {j['ligne']}" if j["present"] else "repris par " + ", ".join(j.get("repris") or ["?"])
            L.append(f"| {j['etape']} | {j['nom']} | {NOMS[j['piece']]} | {j['sorte']} | {j['forme']} | {cell(j['avant'])} | {etat} |")
        L += ["", "## Les retouches de consolidation, en entier", ""]
        for j in c.journal[n3:]:
            L += [f"### {j['nom']} — {NOMS[j['piece']]} — {j['forme']}", "", "Avant :", "", "```text", j["avant"], "```", "", "Après :", "", "```text", j["apres"], "```", ""]
        L += ["## Couples proposés par le rédacteur, non appliqués", "",
              "Le mandat bornait les retouches. Ces quatre couples visent la section des marqueurs ; leur « avant » se trouve une fois dans le candidat. À la mère et au contre-lecteur de dire s'il les faut.", ""]
        for nom, motif, avant, apres in SK.PROPOSITIONS:
            L += [f"### {nom} — {motif}", "", "Avant :", "", "```text", avant.rstrip("\n"), "```", "", "Après :", "", "```text", apres.rstrip("\n"), "```", ""]
        open(table, "w", encoding="utf-8").write("\n".join(L) + "\n")
        print(f"table écrite : {os.path.relpath(table, RACINE)}")
    sys.exit(1 if defauts else 0)


if __name__ == "__main__":
    main()
