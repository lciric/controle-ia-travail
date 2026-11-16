#!/usr/bin/env python3
"""Corrige un fait périmé de procedure-machine-jeu-idee-1-1-v2.md (tête de `main` citée au § 6) dans une v3 neuve.

Usage : python3 -I corriger_procedure_v2_vers_v3_v1.py SOURCE CIBLE HEURE_UTC TETE_MAIN
- SOURCE : la procédure v2, dont l'empreinte doit être EMPREINTE_SOURCE ;
- CIBLE : la procédure v3, fichier neuf (jamais écrasé, R12) ;
- HEURE_UTC : `date -u +%FT%TZ` au moment du scellement ;
- TETE_MAIN : `git rev-parse refs/remotes/origin/main` lu dans le même appel (40 caractères).
Raison : entre la vérification des faits et le scellement de la v2, la tête de `main` est passée de e395dd47 à une autre ;
la v2 écrit « revus à 21:41Z » avec l'ancienne. Aucune autre correction : le texte de la v2 reste celui de ses couples.
"""
import hashlib
import re
import sys

EMPREINTE_SOURCE = "ce23095ae7dad7b9595fd38388d6b4c0eb4dd03c913cc5eab20a36df2a810d17"

COUPLES = [
    ("titre",
     "# Procédure de la machine louée du jeu relancé de l'idée 1.1 — v2",
     "# Procédure de la machine louée du jeu relancé de l'idée 1.1 — v3"),
    ("statut (couple 18, numéro de version suivi)",
     "corrections de ce tour en v2 ;",
     "corrections de ce tour en v3 ;"),
    ("version",
     "- **Version** : v2, scellée à 2026-11-16T21:41:25Z (`date -u`) ; suit la v1 (`0d674c39…`) ; changements : corrections de la\n"
     "  contre-lecture du tour 1 (§ 6).",
     "- **Version** : v3, scellée à {HEURE} (`date -u`) ; suit la v1 (`0d674c39…`) ; changements : corrections de la\n"
     "  contre-lecture du tour 1 (§ 6). La v2 (`ce23095a…`, même dossier, même rédacteur) citait au § 6 une tête de `main`\n"
     "  périmée au moment de son scellement ; seul ce fait et la numérotation changent de la v2 à la v3."),
    ("§ 6, cette version",
     "- **Cette version** : v2, écrite par un rédacteur neuf au moyen du programme de couples\n"
     "  `appliquer_contre_lecture_procedure_tour1_v1.py` (même dossier),",
     "- **Cette version** : v3, écrite par un rédacteur neuf au moyen du programme de couples\n"
     "  `appliquer_contre_lecture_procedure_tour1_v1.py` (même dossier, v1 → v2), puis de `corriger_procedure_v2_vers_v3_v1.py`\n"
     "  (v2 → v3, un fait du § 6),"),
    ("§ 6, M1",
     "Dépendance** : le pas 7 et le geste 13 de\n    cette v2 décrivent",
     "Dépendance** : le pas 7 et le geste 13 de\n    cette version décrivent"),
    ("§ 6, M1 (suite)",
     "Cette v2 ne part donc pas au feu avec l'amorce v1",
     "Cette version ne part donc pas au feu avec l'amorce v1"),
    ("§ 6, M3 (fait périmé)",
     "Faits revus à 21:41Z\n",
     "Faits revus à {HM}\n"),
    ("§ 6, M3 (tête de main)",
     "`14a0dfc5…` ancêtre de la\n    référence locale `origin/main`, `e395dd47…`.",
     "`14a0dfc5…` ancêtre de la\n    référence locale `origin/main`, lue à {HM} : `{TETE}…` (la tête bouge : à relire au feu)."),
]


def main() -> int:
    if len(sys.argv) != 5:
        print("REFUS : usage SOURCE CIBLE HEURE_UTC TETE_MAIN")
        return 2
    source, cible, heure, tete = sys.argv[1:]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", heure):
        print("REFUS : heure illisible")
        return 2
    if not re.fullmatch(r"[0-9a-f]{40}", tete):
        print("REFUS : tête de main illisible (40 caractères hexadécimaux)")
        return 2
    brut = open(source, "rb").read()
    e = hashlib.sha256(brut).hexdigest()
    if e != EMPREINTE_SOURCE:
        print(f"REFUS : empreinte de la source {e} ≠ {EMPREINTE_SOURCE}")
        return 2
    texte = brut.decode("utf-8")
    for nom, ancien, _ in COUPLES:
        if texte.count(ancien) != 1:
            print(f"REFUS : {nom} : « ancien » trouvé {texte.count(ancien)} fois dans la source (1 exigée)")
            return 2
    for nom, ancien, nouveau in COUPLES:
        if texte.count(ancien) != 1:
            print(f"REFUS : {nom} : « ancien » trouvé {texte.count(ancien)} fois au moment de son couple")
            return 2
        nouveau = nouveau.replace("{HEURE}", heure).replace("{HM}", heure[11:16] + "Z").replace("{TETE}", tete[:8])
        texte = texte.replace(ancien, nouveau, 1)
        print(f"appliqué : {nom}")
    try:
        with open(cible, "x", encoding="utf-8") as f:
            f.write(texte)
    except FileExistsError:
        print(f"REFUS : {cible} existe déjà (R12, jamais écrasé)")
        return 2
    print(f"écrit : {cible} ({len(COUPLES)} couples) ; sha256 {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
