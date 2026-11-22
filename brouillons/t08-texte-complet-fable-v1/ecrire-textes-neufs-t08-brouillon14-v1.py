#!/usr/bin/env python3
"""Écrit `textes-neufs-t08-brouillon14-v1.json` : les opérations du brouillon 13 au brouillon 14 de T0.8.

Le brouillon 14 applique le mineur r-1 de la vérification du brouillon 12 par le contre-lecteur 8 (portée exacte de la garde
du calibrage, dans la déclaration de la référence honnête) et inscrit cette vérification ; rien d'autre.
Ce programme ne lit que le fichier des textes neufs du brouillon 13, pour en reprendre la ligne « Statut » et les valeurs.
Usage (depuis la racine du dépôt) : python3 brouillons/t08-texte-complet-fable-v1/ecrire-textes-neufs-t08-brouillon14-v1.py
"""
import json
from pathlib import Path

ICI = "brouillons/t08-texte-complet-fable-v1"
SORTIE = Path(ICI) / "textes-neufs-t08-brouillon14-v1.json"
V13 = json.loads((Path(ICI) / "textes-neufs-t08-brouillon13-v1.json").read_text(encoding="utf-8"))
B11 = "4342b1a5e1aae3d5595ccac86fc8488a5c3e97b7c57c8355d7cb38db8df33456"
B12 = "e55a33ce78ab6b7b97b6b9a53b84c054898ca9823ee30ca64df573394aca8d73"
B13 = "f63a305ed5a3528eba8e6832f39ddd4614ff96f3973edf42a792f49604e48213"
VERIF12 = "185038defaeca81216a5ea2a3274f06f5f1ee56a3e297881ad4724a16d25d885"
GO = "GO-2026-11-22-122"


def une(texte: str, ancien: str, nouveau: str) -> str:
    assert texte.count(ancien) == 1, (texte.count(ancien), ancien[:60])
    return texte.replace(ancien, nouveau)


def statut() -> str:
    s = next(o["nouveau"] for o in V13["operations"] if o["id"] == "T13-02")
    s = une(s, "**brouillon 13 (candidat 4, texte complet)**", "**brouillon 14 (candidat 5, texte complet)**")
    s = une(s, f"Écrit par programme sur le brouillon 12 (`{B12}`), écrit sur le brouillon 11 (`{B11}`), qui est écrit",
            f"Écrit par programme sur le brouillon 13 (`{B13}`), écrit sur le brouillon 12 (`{B12}`, déclaré conforme par la "
            f"vérification du contre-lecteur 8), écrit sur le brouillon 11 (`{B11}`), qui est écrit")
    s = une(s, "**Ce qu'aucun des trois ne fait** :",
            "**Ce que le brouillon 14 fait** : il applique le mineur r-1 de cette vérification (portée exacte de la garde du "
            "calibrage, dans la déclaration de la référence honnête) et l'inscrit, et rien d'autre. **Ce qu'aucun des quatre ne "
            "fait** :")
    for nom in ("differentiel-gel-t08-brouillon{}-v1.md", "faire-t08-brouillon{}-v1.py", "textes-neufs-t08-brouillon{}-v1.json",
                "couples-t08-brouillon{}-v1.json"):
        s = une(s, nom.format(13), nom.format(14))
    s = une(s, "journal-t08-brouillon13-v1.md` (ceux des brouillons 11 et 12, même dossier, gardés tels quels)",
            "journal-t08-brouillon14-v1.md` (ceux des brouillons 11 à 13, même dossier, gardés tels quels)")
    s = une(s, "la vérification de ces corrections par le contre-lecteur 8 (`VERIFICATION_CL8_T08`)",
            "la vérification, par le contre-lecteur 8, de ce qui sépare ce brouillon du brouillon 12, qu'il a déclaré conforme "
            "(`VERIFICATION_CL8_T08`)")
    return s


R1_ANCIEN = ("par couple d'un surveillant et d'un jeu ; à 4 ou plus, la qualification est « non tranchée » (ligne F6) et une réserve "
             "s'écrit ; elle ne voit qu'un seuil trop bas.")
R1_NOUVEAU = ("par couple (surveillant décisif ou obligatoire, jeu) ; à 4 ou plus, pour un surveillant décisif, la qualification est "
              "« non tranchée » (ligne F6), et pour un bras obligatoire, une réserve est écrite avec la phrase de la ligne D "
              "retenue ; elle ne voit qu'un seuil trop bas.")
RELECTURE_ANCIEN = next(o["nouveau"] for o in V13["operations"] if o["id"] == "T13-10")
SUFFIXE = " **Vérification des corrections de la contre-lecture 8** :"
assert RELECTURE_ANCIEN.endswith(SUFFIXE.strip())
RELECTURE_NOUVEAU = (
    "**Brouillon 12 vérifié** par le contre-lecteur 8 : rapport "
    f"`prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon12-verification-cl8-v1.md`, `{VERIF12}` (égale à son "
    "compagnon) ; « conforme : scellable après les marqueurs » ; les 17 constats corrigés ; un mineur restant, r-1. "
    f"**Brouillons 13 et 14** : le brouillon 13 inscrit la décision de Lazar sur la garde d'antériorité (`{GO}`) ; le brouillon "
    "14 applique r-1 et inscrit cette vérification. Ce qui les sépare du brouillon 12, déjà déclaré conforme : 12 puis 8 "
    f"opérations, aucune dans une section gelée (`{ICI}/differentiel-gel-t08-brouillon13-v1.md` et `…-brouillon14-v1.md`, "
    f"sections 3). Le programme de scellement est en version 3 (`{ICI}/finaliser-t08-scellement-v3.py`), qui cite la décision "
    f"dans la valeur du marqueur `LIGNE_MOT_LAZAR_T5_19` ; ses essais sont en version 3 (`{ICI}/essais-controle-gel-t08-v3.py`). "
    "La vérification finale porte sur le brouillon 14 ; c'est son rapport, citant l'empreinte du brouillon 14, que reçoit le "
    "marqueur. **Vérification des corrections de la contre-lecture 8** :")
VERIF_ANCIEN = next(o["nouveau"] for o in V13["operations"] if o["id"] == "T13-11")
VERIF_NOUVEAU = VERIF_ANCIEN.replace("brouillon13.md", "brouillon14.md").replace("brouillon 13", "brouillon 14")
assert VERIF_NOUVEAU != VERIF_ANCIEN and VERIF_NOUVEAU.count("brouillon 14") == 2
AUTEUR = " **Brouillon 14 (candidat 5)** : le même auteur, sur le rapport de vérification du brouillon 12 par le contre-lecteur 8."
DATE = "brouillon 14 écrit le 2026-11-22 à partir de 19:27 UTC (heure de fin au journal) ; "
VUE = " **Pour le brouillon 14** : le rapport de vérification du brouillon 12 par le contre-lecteur 8, en entier."


def operations() -> list:
    return [
        {"id": "T14-01", "nature": "remplacer", "motif": "titre : brouillon 14",
         "ancien": "— v1 — brouillon 13 (candidat 4, texte complet)", "nouveau": "— v1 — brouillon 14 (candidat 5, texte complet)"},
        {"id": "T14-02", "nature": "remplacer_ligne", "motif": "statut du brouillon 14",
         "prefixe": "- **Statut** : **brouillon 13 (candidat 4, texte complet)**", "nouveau": statut()},
        {"id": "T14-03", "nature": "ajouter_en_fin_de_ligne", "motif": "auteur du brouillon 14",
         "prefixe": "- **Auteurs** : brouillon 1,", "ajout": AUTEUR},
        {"id": "T14-04", "nature": "ajouter_en_debut_de_valeur", "motif": "date du brouillon 14",
         "prefixe": "- **Date (UTC)** : ", "ajout": DATE},
        {"id": "T14-05", "nature": "ajouter_en_fin_de_ligne", "motif": "déclaration de vue : rapport de vérification lu",
         "prefixe": "- **Auteur du brouillon 11** (session", "ajout": VUE},
        {"id": "T14-06", "nature": "remplacer", "motif": "r-1 : portée exacte de la garde du calibrage (décisif, obligatoire)",
         "ancien": R1_ANCIEN, "nouveau": R1_NOUVEAU},
        {"id": "T14-07", "nature": "remplacer", "motif": "vérification du brouillon 12 inscrite ; la vérification finale porte sur le brouillon 14",
         "ancien": RELECTURE_ANCIEN, "nouveau": RELECTURE_NOUVEAU},
        {"id": "T14-08", "nature": "remplacer", "motif": "vérification des marqueurs : brouillon 14",
         "ancien": VERIF_ANCIEN, "nouveau": VERIF_NOUVEAU},
    ]


def main() -> None:
    doc = {
        "objet": "opérations du brouillon 13 au brouillon 14 de T0.8 (candidat 5, texte complet)",
        "marqueurs_restants": V13["marqueurs_restants"],
        "valeurs_marqueurs_en_sections_gelees": V13["valeurs_marqueurs_en_sections_gelees"],
        "debut_ligne_t5_19": V13["debut_ligne_t5_19"],
        "sha_ligne_t5_19_brouillon10": V13["sha_ligne_t5_19_brouillon10"],
        "operations": operations(),
    }
    SORTIE.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("écrit :", SORTIE, len(doc["operations"]), "opérations")


if __name__ == "__main__":
    main()
