#!/usr/bin/env python3
"""Applique au devis du banc de calibration MR-2 (v2) les corrections de sa contre-lecture du tour 2.

Couples « ancien -> nouveau ». Le programme :
- vérifie l'empreinte de la pièce de départ (v2) et celle du rapport de contre-lecture du tour 2 ;
- vérifie que chaque « ancien » figure exactement une fois dans la pièce de départ ;
- refuse d'écraser la cible (v3) si elle existe ;
- prend l'heure de scellement (lue par `date -u`) en argument.

Usage : python3 appliquer-corrections-devis-banc-calibration-mr2-tour2-v1.py "AAAA-MM-JJTHH:MM:SSZ"
"""
import hashlib
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "devis-banc-calibration-mr2-v2.md"
SOURCE_SHA256 = "4103d02ce509a8b3d280299aeaa0e82d62d7a796f8a5f8fc6a0f72ed018b47f3"
RAPPORT = ICI / "contre-lecture-devis-banc-calibration-mr2-tour2-v1.md"
RAPPORT_SHA256 = "ec7c4e9de51f73c37424e111b889aab41695ac80b9e508cb59fdcb67e4b597e8"
CIBLE = ICI / "devis-banc-calibration-mr2-v3.md"
PROGRAMME = pathlib.Path(__file__).name


def sha256(chemin):
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def couples(heure):
    tour_2 = f"""
### Tour 2 (v2 → v3)

- **Rapport** : `contre-lecture-devis-banc-calibration-mr2-tour2-v1.md` (même dossier), empreinte
  `{RAPPORT_SHA256}` ; lecteur : modèle C, contre-lecteur neuf (R2) ; verdict : **corrections (0 majeure, 2 mineures)**.
- **Pièce lue par le rapport** : la v2 de ce devis, `{SOURCE_SHA256}` ; la v2 reste intacte (R12).
- **Application** : par le programme `{PROGRAMME}` (même dossier, scellé à côté), couples « ancien → nouveau » ; il vérifie
  l'empreinte de la v2 et du rapport, que chaque « ancien » figure une seule fois, et refuse d'écraser la v3.
  Rédacteur des corrections : un rédacteur neuf que sa consigne déclare du modèle C (la même consigne porte aussi « corrections
  par le modèle A ») ; le rapport du tour 2 est lui aussi du modèle C : à ce tour, le même modèle a lu et corrigé. Rien d'autre n'a
  changé que les couples du rapport, le titre, la version et l'heure de l'en-tête, la ligne « Rédacteur » de l'en-tête, les
  intertitres « Tour 1 » et « Tour 2 », et cette sous-section.

Réponse point par point :

| point du rapport | où | suite |
|---|---|---|
| **m6** — rédacteur des corrections du tour 1 faussement attribué | section 11, tour 1 ; en-tête, ligne « Rédacteur » | **appliquée en substance, « nouveau » du rapport refusé dans sa lettre** : le rapport propose d'écrire « modèle A (rédacteur de la v1) » ; je ne peux pas l'établir, et ma propre consigne porte la même double mention (« tu es du modèle C » et « corrections par le modèle A ») ; écrire « modèle A » comme un fait remplacerait une attribution non vérifiée par une autre. La phrase dit maintenant ce qui est su : la v2 se déclarait du modèle C, le rapport du tour 2 relève que la consigne donnait le modèle A, la provenance n'est pas établie, et le rapport du tour 1 est du modèle C. L'en-tête renvoie à cette section pour les rédacteurs des corrections (relecture demandée par m6) |
| **m7** — « deux décisions » contre trois posées | section 0, point 3 ; section 11, tour 1 | **appliquée** (« trois décisions de Lazar (section 9 : Q-B1, Q-B2, Q-B3) ») ; l'observation sans changement du tour 1 est remplacée par « corrigée au tour 2 (m7) », comme le demande le rapport |
| remarques facultatives 1 à 3 | — | aucune correction exigée ; la remarque 1 (le titre) est prise dans la phrase « Rien d'autre n'a changé » de ce tour ; la remarque 2 reste au préenregistrement et à la procédure du banc ; la remarque 3 rejoint le point 1 pour la mère |
| points pour la session mère 1 à 4 | — | rien à porter dans la pièce : le point 1 l'est déjà par Q-B2 ; le point 2 est traité par m6 ci-dessus (même modèle au rapport et aux corrections à ce tour, et peut-être au tour 1 si la déclaration de la v2 est exacte : un tour 3 serait à confier à un lecteur d'un autre modèle) ; les points 3 et 4 n'appellent rien |

Aucune autre correction refusée.

Version v3 scellée : {heure} (`date -u`).
"""
    return [
        # En-tête : version (titre).
        ("(suite de l'issue P-2 du pilote) — v2",
         "(suite de l'issue P-2 du pilote) — v3"),
        # En-tête : version et heure.
        ("  La v1 (`6172ae59…`) reste intacte.",
         "  La v1 (`6172ae59…`) reste intacte.\n"
         f"- **Version v3** : corrections de la contre-lecture du tour 2 appliquées (section 11) ; scellée le {heure} (`date -u`).\n"
         "  La v2 (`4103d02c…`) reste intacte."),
        # m6, en-tête (relecture demandée par le rapport).
        ("- **Rédacteur** : modèle A, rédacteur neuf (je n'ai écrit ni le texte du pilote, ni son code, ni la conception v4, ni le verdict).",
         "- **Rédacteur** : modèle A, rédacteur neuf (je n'ai écrit ni le texte du pilote, ni son code, ni la conception v4, ni le verdict).\n"
         "  Rédacteurs des corrections des tours 1 et 2 : section 11."),
        # m7, section 0 point 3.
        ("une ligne « calcul » de 3 USD ; et deux décisions de Lazar (section 9).",
         "une ligne « calcul » de 3 USD ; et trois décisions de Lazar (section 9 : Q-B1, Q-B2, Q-B3)."),
        # Section 11 : intertitre du tour 1.
        ("## 11. Contre-lecture\n",
         "## 11. Contre-lecture\n\n### Tour 1 (v1 → v2)\n"),
        # m6, section 11 tour 1 (« nouveau » du rapport refusé dans sa lettre ; voir la sous-section du tour 2).
        ("Rédacteur des corrections : un rédacteur neuf (modèle C), qui n'a écrit ni la v1 ni le rapport.",
         "Rédacteur des corrections : déclaré par la v2 « un rédacteur neuf (modèle C) » ; le rapport du tour 2 relève que la consigne"
         " donnait les corrections au modèle A, rédacteur de la v1 ; provenance non établie (tour 2, m6) ; le rapport du tour 1 est du"
         " modèle C."),
        # m7, conséquence : l'observation du tour 1 devient sans objet.
        ("Aucune correction refusée. Observation sans changement (hors du rapport, donc non appliquée) : la section 0, point 3, annonce\n"
         "« deux décisions de Lazar (section 9) », alors que la section 9 en pose trois (Q-B1 à Q-B3).",
         "Aucune correction refusée. Observation du tour 1 sur la section 0, point 3 (deux décisions annoncées, trois posées) :"
         " corrigée au tour 2 (m7)."),
        # Sous-section du tour 2, après la ligne de scellement de la v2.
        ("Version v2 scellée : 2026-11-16T20:58:19Z (`date -u`).\n",
         "Version v2 scellée : 2026-11-16T20:58:19Z (`date -u`).\n" + tour_2),
    ]


def main():
    if len(sys.argv) != 2 or not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", sys.argv[1]):
        sys.exit("refus : donner l'heure de scellement lue par `date -u`, forme AAAA-MM-JJTHH:MM:SSZ")
    heure = sys.argv[1]
    if CIBLE.exists():
        sys.exit(f"refus : la cible {CIBLE.name} existe déjà ; on n'écrase jamais (R12)")
    if sha256(SOURCE) != SOURCE_SHA256:
        sys.exit(f"refus : empreinte de {SOURCE.name} inattendue")
    if sha256(RAPPORT) != RAPPORT_SHA256:
        sys.exit(f"refus : empreinte de {RAPPORT.name} inattendue")
    texte = SOURCE.read_text(encoding="utf-8")
    for i, (ancien, _) in enumerate(couples(heure), 1):
        n = texte.count(ancien)
        if n != 1:
            sys.exit(f"refus : couple {i}, « ancien » trouvé {n} fois (exigé : 1)")
    for ancien, nouveau in couples(heure):
        texte = texte.replace(ancien, nouveau, 1)
    with open(CIBLE, "x", encoding="utf-8") as f:
        f.write(texte)
    print(f"écrit : {CIBLE.name} ({len(couples(heure))} couples)")


if __name__ == "__main__":
    main()
