#!/usr/bin/env python3
"""Applique au devis du banc de calibration MR-2 (v1) les corrections de sa contre-lecture du tour 1.

Couples « ancien -> nouveau ». Le programme :
- vérifie l'empreinte de la pièce de départ (v1) et celle du rapport de contre-lecture ;
- vérifie que chaque « ancien » figure exactement une fois dans la pièce de départ ;
- refuse d'écraser la cible (v2) si elle existe ;
- prend l'heure de scellement (lue par `date -u`) en argument.

Usage : python3 appliquer-corrections-devis-banc-calibration-mr2-tour1-v1.py "AAAA-MM-JJTHH:MM:SSZ"
"""
import hashlib
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "devis-banc-calibration-mr2-v1.md"
SOURCE_SHA256 = "6172ae590c29901a040bd39804177a844e74b9f9f7589acf22b7b5e22ca942db"
RAPPORT = ICI / "contre-lecture-devis-banc-calibration-mr2-tour1-v1.md"
RAPPORT_SHA256 = "7fd26c76bfcb6c16c722dc4a9a18f91da193b2271c76ec98f8f009598be3e191"
CIBLE = ICI / "devis-banc-calibration-mr2-v2.md"
PROGRAMME = pathlib.Path(__file__).name


def sha256(chemin):
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def couples(heure):
    section_11 = f"""

## 11. Contre-lecture

- **Rapport** : `contre-lecture-devis-banc-calibration-mr2-tour1-v1.md` (même dossier), empreinte
  `{RAPPORT_SHA256}` ; lecteur : modèle C, contre-lecteur neuf (R2) ; verdict : **corrections (2 majeures, 5 mineures)**.
- **Pièce lue par le rapport** : la v1 de ce devis, `{SOURCE_SHA256}` ; la v1 reste intacte (R12).
- **Application** : par le programme `{PROGRAMME}` (même dossier, scellé à côté), couples « ancien → nouveau » recopiés du
  rapport ; il vérifie l'empreinte de la v1 et du rapport, que chaque « ancien » figure une seule fois, et refuse d'écraser la v2.
  Rédacteur des corrections : un rédacteur neuf (modèle C), qui n'a écrit ni la v1 ni le rapport. Rien d'autre n'a changé que les
  couples du rapport, la version et l'heure de l'en-tête, et cette section.

Réponse point par point :

| point du rapport | où | suite |
|---|---|---|
| **M1** — liste d'arrêt contre dénominateur | section 6 point 1 ; section 7 point 5 | **appliquée** : « monde sans tirage conforme » retiré de la liste d'arrêt, compté selon Q-B3 et rapporté ; probabilité d'au moins un monde sans tirage conforme chiffrée (≈ 9 % à 0,5 refus par tirage, ≈ 33 % à 0,6 ; recalculées : 1 − (1 − 0,5^8)^24 = 0,089 ; 1 − (1 − 0,6^8)^24 = 0,335) |
| **M2** — condition de la course non remplie sous Q-B2 (a) | section 9, Q-B2 | **appliquée** : Lazar est averti que (a) laisse ouverte la condition « banc de calibration fait (n et seuils fixés par leurs règles) » de GO-2026-11-13-01 et -02, et que le défaut à 48 heures ne la lève pas |
| **m1** — 13 lignes du bloc gelé, non 12 | section 2, Code | **appliquée** (recompté : 13 lignes `orchestrator/mr2_v68/…` aux lignes 562 à 574 du texte scellé `8aa33014…` ; le verdict dit aussi 13) |
| **m2** — arrondi de l'attendu et prix non borné | section 5 | **appliquée** (5 h × 0,052222 = 0,26 ; 0,75 à 0,15 USD/h) |
| **m3** — coûts « chacun » de `fable52` | section 3 | **appliquée** (moyennes ; les durées des deux complets diffèrent au verdict : 388,807 s et 430,542 s) |
| **m4** — prédiction chiffrée à la borne haute | section 7 point 4 | **appliquée** (bascule du modèle approché du texte scellé à 0,034, probabilité 0,5, et à 0,051, probabilité 0,05 : vérifiées dans le texte scellé) |
| **m5** — couplage des deux passes | section 6 point 2 | **appliquée** (flux commun en génération 1 seulement) |
| remarques facultatives 1 à 4 | — | aucune correction exigée ; non portées dans la pièce (rien d'autre ne change) ; les remarques 1 (ne jouer que ce que décide le préenregistrement) et 2 (garde d'échéance équivalente à celle de la v14) restent à prendre au préenregistrement et à la procédure du banc |
| points pour la session mère 1 à 5 | — | les points 1 à 3 sont portés par M2, M1 et m4 ; le point 4 par m2 ; le point 5 n'appelle rien |

Aucune correction refusée. Observation sans changement (hors du rapport, donc non appliquée) : la section 0, point 3, annonce
« deux décisions de Lazar (section 9) », alors que la section 9 en pose trois (Q-B1 à Q-B3).

Version v2 scellée : {heure} (`date -u`).
"""
    return [
        # En-tête : version.
        ("(suite de l'issue P-2 du pilote) — v1",
         "(suite de l'issue P-2 du pilote) — v2"),
        # En-tête : heure de la version.
        ("- **Heures** (`date -u`) : début 2026-11-16 20:44:10Z ; fin : dernière ligne.",
         "- **Heures** (`date -u`) : début 2026-11-16 20:44:10Z ; fin : dernière ligne.\n"
         f"- **Version v2** : corrections de la contre-lecture du tour 1 appliquées (section 11) ; scellée le {heure} (`date -u`).\n"
         "  La v1 (`6172ae59…`) reste intacte."),
        # M1, section 6 point 1.
        ("(empreinte d'un module, nombre de parties différent de 24, monde sans tirage conforme, exception)",
         "(empreinte d'un module, nombre de parties différent de 24, exception ; un monde sans tirage conforme en 8 n'arrête pas le banc : il est compté selon Q-B3 et rapporté)"),
        # M1, section 7 point 5.
        ("sous la borne de 8 par monde ; un monde sans tirage conforme pèse selon Q-B3.",
         "sous la borne de 8 par monde ; un monde sans tirage conforme pèse selon Q-B3. Probabilité qu'au moins un des 24 mondes n'en ait aucun : ≈ 9 % au taux de refus observé en v4 (12 refus pour 12 mondes, 0,5 par tirage, indépendance supposée), ≈ 33 % à 0,6 ; l'événement est donc à prévoir, non exceptionnel, et le préenregistrement le traite par Q-B3, sans arrêt."),
        # M2, section 9, Q-B2.
        ("confiance 0,55. Défaut sous 48 heures : (a).",
         "confiance 0,55. Défaut sous 48 heures : (a). À savoir avant de choisir : sous (a), la condition « banc de calibration fait (n et seuils fixés par leurs règles) » de GO-2026-11-13-01 et -02 (échéance 2026-11-30) n'est pas remplie par ce banc ; le banc plus large reste dû avant la course, ou un mot de Lazar qui lève cette condition ; le défaut à 48 heures ne la lève pas, et je n'ai pas vérifié que le code v68 de la course existe."),
        # m1, section 2.
        ("(12 lignes `orchestrator/mr2_v68/…` du bloc gelé)",
         "(13 lignes `orchestrator/mr2_v68/…` du bloc gelé, dont `mesure_pilote_v4.py` et `seuil_pilote_v1.py`, qui n'entrent pas au banc)"),
        # m2, section 5.
        ("**0,30** (≈ 5 h à 0,052 USD/h, arrondi)",
         "**0,30** (≈ 5 h à 0,052 USD/h = 0,26, arrondi au-dessus ; à 0,15 USD/h, plafond de l'offre, 5 h coûteraient 0,75)"),
        # m3, section 3.
        ("complets 2,216780 chacun ; tronqués 2,792996 chacun (5,585992 pour les deux)",
         "complets 2,216780 en moyenne (4,433560 pour les deux, par différence) ; tronqués 2,792996 en moyenne (5,585992 pour les deux)"),
        # m4, section 7 point 4.
        ("(permise à tort 0,27 si p vaut 0,051, à 14 appels)",
         "(permise à tort 0,27 si p vaut 0,051, à 14 appels) ; le modèle approché du texte scellé place la bascule de la règle à 0,034 (probabilité 0,5) et à 0,051 (probabilité 0,05) : la passe à 0,0430 n'est pas acquise d'avance, et le préenregistrement y écrit sa prédiction chiffrée (R1) et ce que devient un résultat sous 12 sur 24 à cette borne (information rapportée, ne décide pas)"),
        # m5, section 6 point 2.
        ("0,0430 consomment donc le même flux et se comparent monde par monde.",
         "0,0430 consomment donc le même flux en génération 1 (les connus y sont {K1} dans les deux passes) et se comparent monde par monde pour la règle, qui se lit après la génération 1 ; leurs flux divergent dès la génération 2."),
        # Section « Contre-lecture » créée (absente de la v1).
        ("Fin de la rédaction : 2026-11-16T20:51:17Z (`date -u`).\n",
         "Fin de la rédaction : 2026-11-16T20:51:17Z (`date -u`)." + section_11),
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
