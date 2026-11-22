#!/usr/bin/env python3
"""Écrit `textes-neufs-t08-brouillon13-v1.json` : les opérations du brouillon 12 au brouillon 13 de T0.8.

Le brouillon 13 ne fait qu'inscrire la décision de Lazar du 22 novembre sur la garde d'antériorité du texte et du code sur
la course (GO-2026-11-22-122, option (a) : gardée dans le code et déclarée, sans écart au gel de la liste d'arrêt).
Ce programme ne lit que le fichier des textes neufs du brouillon 12, pour en reprendre la ligne « Statut » et les valeurs.
Usage (depuis la racine du dépôt) : python3 brouillons/t08-texte-complet-fable-v1/ecrire-textes-neufs-t08-brouillon13-v1.py
"""
import json
from pathlib import Path

ICI = "brouillons/t08-texte-complet-fable-v1"
SORTIE = Path(ICI) / "textes-neufs-t08-brouillon13-v1.json"
V12 = json.loads((Path(ICI) / "textes-neufs-t08-brouillon12-v1.json").read_text(encoding="utf-8"))
B11 = "4342b1a5e1aae3d5595ccac86fc8488a5c3e97b7c57c8355d7cb38db8df33456"
B12 = "e55a33ce78ab6b7b97b6b9a53b84c054898ca9823ee30ca64df573394aca8d73"
GO = "GO-2026-11-22-122"
COMMIT_GO = "37a5afed2838b69aad63333a5f79c7443080c6af"


def une(texte: str, ancien: str, nouveau: str) -> str:
    assert texte.count(ancien) == 1, (texte.count(ancien), ancien[:60])
    return texte.replace(ancien, nouveau)


def statut() -> str:
    s = next(o["nouveau"] for o in V12["operations"] if o["id"] == "T12-02")
    s = une(s, "**brouillon 12 (candidat 3, texte complet)**", "**brouillon 13 (candidat 4, texte complet)**")
    s = une(s, f"Écrit par programme sur le brouillon 11 (`{B11}`), qui est écrit",
            f"Écrit par programme sur le brouillon 12 (`{B12}`), écrit sur le brouillon 11 (`{B11}`), qui est écrit")
    s = une(s, "**Ce qu'aucun des deux ne fait** :",
            "**Ce que le brouillon 13 fait** : il inscrit la décision de Lazar du 22 novembre sur la garde d'antériorité du texte "
            f"et du code sur la course (`{GO}`, option (a) : gardée dans le code et déclarée, sans écart au gel), et rien d'autre. "
            "**Ce qu'aucun des trois ne fait** :")
    s = une(s, "differentiel-gel-t08-brouillon12-v1.md", "differentiel-gel-t08-brouillon13-v1.md")
    s = une(s, "faire-t08-brouillon12-v1.py", "faire-t08-brouillon13-v1.py")
    s = une(s, "textes-neufs-t08-brouillon12-v1.json", "textes-neufs-t08-brouillon13-v1.json")
    s = une(s, "couples-t08-brouillon12-v1.json", "couples-t08-brouillon13-v1.json")
    s = une(s, "journal-t08-brouillon12-v1.md` (ceux du brouillon 11, même dossier, gardés tels quels)",
            "journal-t08-brouillon13-v1.md` (ceux des brouillons 11 et 12, même dossier, gardés tels quels)")
    s = une(s, "la ligne du registre qui confirme les gardes de code plus strictes que la lettre et dit le sort de VT5-07 "
               "(`LIGNE_MOT_LAZAR_T5_19`)",
            "la ligne du registre qui confirme les trois autres gardes de code plus strictes que la lettre "
            "(`LIGNE_MOT_LAZAR_T5_19`)")
    return s


GARDES_ANCIEN = (
    "La quatrième est VT5-07 : le mot de Lazar « go a pour T5-19 » ne la nomme pas. **Recommandation de l'auteur du brouillon "
    "11** : les garder toutes les quatre. La quatrième ne fait qu'appliquer R1 et l'en-tête de ce texte : une course partie avant "
    "le scellement n'aurait pas de lecture préenregistrée, et l'arrêt est la seule issue honnête. Confiance 0,8. La ligne du "
    "registre qui les confirme, et qui dit le sort de VT5-07, remplit le marqueur `LIGNE_MOT_LAZAR_T5_19` avec R-2657.")
GARDES_NOUVEAU = (
    "La quatrième est VT5-07 : le mot de Lazar « go a pour T5-19 » ne la nommait pas. **Décision de Lazar, le 22 novembre vers "
    f"19:11 UTC** (`{GO}`, « go recos ») : option (a) — la garde d'antériorité est gardée dans le code et déclarée ici, sans "
    "être écrite dans la « Liste d'arrêt » gelée ; aucun écart au gel. Elle ne fait qu'appliquer R1 et l'en-tête de ce texte : "
    "une course partie avant le scellement n'aurait pas de lecture préenregistrée. L'auteur du brouillon 11 recommandait de "
    "garder aussi les trois premières ; la ligne du registre qui les confirme remplit le marqueur `LIGNE_MOT_LAZAR_T5_19`, avec "
    f"R-2657 et `{GO}`.")
SOURCE_GARDE_ANCIEN = "| VT5-07 ; en-tête, « avant toute exécution » ; R1 |"
SOURCE_GARDE_NOUVEAU = f"| VT5-07 ; en-tête, « avant toute exécution » ; R1 ; gardée par la décision `{GO}` |"

LAZAR_1 = (f"1. **Garde d'antériorité du texte et du code sur la course (VT5-07)** : **tranché** le 22 novembre (`{GO}`) — option "
           "(a), gardée dans le code et déclarée ici, sans écart au gel. Les options étaient : la garder, la retirer du code, ou "
           "l'inscrire à la « Liste d'arrêt » par un écart déclaré.")
CAL_25 = ("| ≤ 25 nov. | session mère | ligne du registre : confirmation des trois autres gardes de code plus strictes ; la garde "
          f"d'antériorité (VT5-07) est tranchée par Lazar le 22 novembre, `{GO}` | — |")
LIGNE_TABLE = (
    "| `LIGNE_MOT_LAZAR_T5_19` | le mot de Lazar sur la phrase T5-19 du point 1 du plan (« go a pour T5-19 » : option (a), phrase "
    "gardée ; journal du compte 4, C4-0054) est inscrit par la session mère : R-2657, 14 novembre ; le sort de VT5-07 est tranché "
    f"par Lazar le 22 novembre : `{GO}`, option (a) ; reste, sur une ligne neuve du registre, la confirmation par la session mère "
    "des trois autres gardes de code gardées plus strictes que ce texte (section « Depuis le gel du 10 novembre », « Gardes de "
    f"code ») ; le marqueur reçoit R-2657, `{GO}` et cette ligne | avant le scellement | session mère |")
VUE_13 = (f" **Pour le brouillon 13** : la ligne `{GO}` de `registres/go.md`, lue sur `main` au commit `{COMMIT_GO}`, et le message "
          "de la session mère qui l'annonce.")
AUTEUR_13 = f" **Brouillon 13 (candidat 4)** : le même auteur, sur la décision de Lazar inscrite en `{GO}`."
DATE_13 = "brouillon 13 écrit le 2026-11-22 à partir de 19:15 UTC (heure de fin au journal) ; "
RELECTURE_ANCIEN = "**Vérification des corrections de la contre-lecture 8** :"
RELECTURE_NOUVEAU = (
    "**Brouillon 13** : il ne diffère du brouillon 12 que par l'inscription de la décision de Lazar sur la garde d'antériorité "
    f"(`{GO}` ; programme `{ICI}/faire-t08-brouillon13-v1.py`, différentiel `{ICI}/differentiel-gel-t08-brouillon13-v1.md`) ; "
    f"le programme de scellement passe en version 3 (`{ICI}/finaliser-t08-scellement-v3.py`), qui cite cette décision dans la "
    f"valeur du marqueur `LIGNE_MOT_LAZAR_T5_19`, et ses essais en version 2 (`{ICI}/essais-controle-gel-t08-v2.py`) ; la "
    "vérification porte sur le brouillon 13. **Vérification des corrections de la contre-lecture 8** :")
VERIF_ANCIEN = ("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon12.md | sort | uniq -c` ; chaque marqueur a une seule "
                "occurrence et une seule valeur ; `controle_ia.prereg.problemes` refuse tout marqueur restant. Au "
                "brouillon 12 : cinq marqueurs, une occurrence chacun (contrôlé par le programme du brouillon 12).")
VERIF_NOUVEAU = ("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon13.md | sort | uniq -c` ; chaque marqueur a une seule "
                 "occurrence et une seule valeur ; `controle_ia.prereg.problemes` refuse tout marqueur restant. Au "
                 "brouillon 13 : cinq marqueurs, une occurrence chacun (contrôlé par le programme du brouillon 13).")


def operations() -> list:
    return [
        {"id": "T13-01", "nature": "remplacer", "motif": "titre : brouillon 13",
         "ancien": "— v1 — brouillon 12 (candidat 3, texte complet)", "nouveau": "— v1 — brouillon 13 (candidat 4, texte complet)"},
        {"id": "T13-02", "nature": "remplacer_ligne", "motif": "statut du brouillon 13",
         "prefixe": "- **Statut** : **brouillon 12 (candidat 3, texte complet)**", "nouveau": statut()},
        {"id": "T13-03", "nature": "ajouter_en_fin_de_ligne", "motif": "auteur du brouillon 13",
         "prefixe": "- **Auteurs** : brouillon 1,", "ajout": AUTEUR_13},
        {"id": "T13-04", "nature": "ajouter_en_debut_de_valeur", "motif": "date du brouillon 13",
         "prefixe": "- **Date (UTC)** : ", "ajout": DATE_13},
        {"id": "T13-05", "nature": "ajouter_en_fin_de_ligne", "motif": "déclaration de vue : ligne de GO lue",
         "prefixe": "- **Auteur du brouillon 11** (session", "ajout": VUE_13},
        {"id": "T13-06", "nature": "remplacer_ligne", "motif": "calendrier : garde d'antériorité tranchée",
         "prefixe": "| ≤ 25 nov. |", "nouveau": CAL_25},
        {"id": "T13-07", "nature": "remplacer", "motif": "table des gardes : source de la quatrième",
         "ancien": SOURCE_GARDE_ANCIEN, "nouveau": SOURCE_GARDE_NOUVEAU},
        {"id": "T13-08", "nature": "remplacer", "motif": "gardes de code : décision de Lazar, option (a)",
         "ancien": GARDES_ANCIEN, "nouveau": GARDES_NOUVEAU},
        {"id": "T13-09", "nature": "remplacer_ligne", "motif": "point 1 pour Lazar : tranché",
         "prefixe": "1. **Garde d'antériorité du texte et du code sur la course (VT5-07)**", "nouveau": LAZAR_1},
        {"id": "T13-10", "nature": "remplacer", "motif": "relecture : la vérification porte sur le brouillon 13",
         "ancien": RELECTURE_ANCIEN, "nouveau": RELECTURE_NOUVEAU},
        {"id": "T13-11", "nature": "remplacer", "motif": "vérification des marqueurs : brouillon 13",
         "ancien": VERIF_ANCIEN, "nouveau": VERIF_NOUVEAU},
        {"id": "T13-12", "nature": "remplacer_ligne", "motif": "table des marqueurs : sort de VT5-07 tranché",
         "prefixe": "| `LIGNE_MOT_LAZAR_T5_19` |", "nouveau": LIGNE_TABLE},
    ]


def main() -> None:
    doc = {
        "objet": "opérations du brouillon 12 au brouillon 13 de T0.8 (candidat 4, texte complet)",
        "marqueurs_restants": V12["marqueurs_restants"],
        "valeurs_marqueurs_en_sections_gelees": V12["valeurs_marqueurs_en_sections_gelees"],
        "debut_ligne_t5_19": V12["debut_ligne_t5_19"],
        "sha_ligne_t5_19_brouillon10": V12["sha_ligne_t5_19_brouillon10"],
        "operations": operations(),
    }
    SORTIE.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("écrit :", SORTIE, len(doc["operations"]), "opérations")


if __name__ == "__main__":
    main()
