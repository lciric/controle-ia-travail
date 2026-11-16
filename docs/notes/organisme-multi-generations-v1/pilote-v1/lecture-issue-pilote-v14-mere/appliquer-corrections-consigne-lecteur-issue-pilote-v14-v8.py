"""Écrit la consigne v8 à partir de la v7 (v7 → v8) : arrêts du point 0 absents de la « Liste d'arrêt » du texte scellé
retirés et remplacés par des contrôles rapportés.

Raison : un premier lecteur s'est arrêté au point 0 de la v7 sur `appels_complets_illisibles` différent de 0, critère que la
consigne ajoutait ; le texte scellé (`8aa33014…`) fait foi et le lecteur en applique la « Liste d'arrêt » et rien d'autre.
Couples « ancien → nouveau » : chaque « ancien » doit figurer exactement une fois dans la v7 ; l'empreinte de la v7 est
vérifiée ; la cible n'est jamais écrasée (R12). Aucun autre octet de la v7 n'est changé.
Usage : python appliquer-corrections-consigne-lecteur-issue-pilote-v14-v8.py HEURE_UTC
"""
import hashlib
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "consigne-lecteur-issue-pilote-v14-v7.md"
CIBLE = ICI / "consigne-lecteur-issue-pilote-v14-v8.md"
EMPREINTE_SOURCE = "b97062809d9ffe24ae9bc13445aa431048d91c2618d96ee0e57f646b56ede95c"


def empreinte(chemin):
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


ILLISIBLES = """
   **Appels à réponse illisible** (contrôle rapporté, **jamais un arrêt** : ni la « Liste d'arrêt », ni la « Métrique », ni E-2 du
   texte scellé n'en font un). Par le code (lanceur `demonstrations/pilote_mr2_v74.py`, `5dc01676…`, sous-commande `jouer` ;
   `pole/pilote_mr2_v70.py`, `7541b0c3…`, fonctions `cartes_d_un_appel` et `extraire_propositions`),
   `appels_complets_illisibles` compte les entrées de `gardien` du relevé dont `lecture.lecture` n'est pas nul : des appels joués
   dont l'état n'est pas `echec` (donc `complet` **ou** `tronque`, malgré le nom du champ) et dont le texte rendu ne donne aucune
   liste de propositions (motif « réponse illisible (JSON) » ou « réponse sans liste de propositions ») ; leur réponse brute et
   leur témoin d'isolement sont écrits et scellés avant l'extraction, comme pour tout appel ; aucune carte n'en sort. Il rapporte
   la valeur et vérifie qu'elle concorde, en ne lisant que ces champs de contrôle (`gardien` : `monde`, `proposeur`,
   `lecture.lecture`, `lecture.propositions` ; `appels` du relevé et de `CARTES.json` : `monde`, `proposeur`, `etat` ; cartes de
   `CARTES.json` : `monde`, `proposeur`, jamais `loi`) : (a) elle égale le nombre d'entrées de `gardien` à `lecture.lecture` non
   nul, chacune rapportée (monde, proposeur, motif) ; (b) chacun de ces appels a, dans `appels` du relevé, l'état `complet` ou
   `tronque`, et `lecture.propositions` à 0 ; (c) `CARTES.json` ne porte aucune carte de ce couple (monde, proposeur) et lui donne
   le même état dans `appels` ; (d) au point 3, quand les comptes de la sortie sont lus : `mesure_pilote_v4.py` (`676d5f37…`)
   classe un tel appel `complet` « sans carte » et un tel appel `tronque` « tronqué », tous deux hors du dénominateur, comptés à
   part, sans refus nommé (« Métrique », E-2 (i)) ; il vérifie que `corps.appels.sans_carte` est au moins le nombre de ces appels
   à l'état `complet` (il compte aussi les appels complets dont aucune carte admise n'est évaluable) et `corps.appels.tronque` au
   moins le nombre de ceux à l'état `tronque` ; si le minimum (12 appels répondus sur 16, au moins 3 par monde) n'est pas tenu,
   l'issue est P-0, causes rapportées (« Critères de lecture gelés »). Un désaccord est un écart rapporté, sans arrêt ; un
   contrôle de cet alinéa qu'il ne peut faire est écrit « non fait », sans arrêt.
"""


def couples(heure):
    return [
        # En-tête : titre et version.
        (
            "# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v7\n",
            "# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v8\n",
        ),
        (
            "Version 7, 2026-11-16T15:28:59Z (`date -u`, lue juste avant l'écriture et le scellement) : corrections du tour 1 de la contre-lecture de la v6 appliquées (section « Contre-lecture », en fin de pièce) ; la v6 (`0fcd736c…`),",
            f"Version 8, {heure} (`date -u`, lue juste avant l'écriture et le scellement) : un premier lecteur s'est arrêté au point 0 de la v7 sur un critère que la consigne ajoutait à la « Liste d'arrêt » du texte scellé (`appels_complets_illisibles` à 0) ; le texte fait foi, et le lecteur en applique la « Liste d'arrêt » et rien d'autre : les arrêts du point 0 absents de cette liste deviennent des contrôles rapportés (sous-section « Version 8 », en fin de pièce) ; rédacteur : un rédacteur neuf (modèle A), qui n'a écrit ni le texte scellé ni le code ; la v7 (`b9706280…`), la v6 (`0fcd736c…`),",
        ),
        # Point 0 : `exclus_balayage=` rapporté, sans arrêt propre.
        (
            " ; le champ `exclus_balayage=` ne nomme aucune pièce remise ici) ;",
            ") ; le champ `exclus_balayage=` de `etat.txt` rapporté, **sans arrêt** (il n'est pas dans la « Liste d'arrêt » ; une pièce"
            " remise qu'il nommerait manque à la copie, et chaque contrôle qui l'exige suit la règle « non fait » ci-dessous) ;",
        ),
        # Point 0 : `"aucun_monde"` rapporté, sans arrêt ; `CARTES-partiel.json` gardé (arrêt code 3 de la liste).
        (
            "`rapatrie-reel/liste-rapatriement-pilote-v70.json` : `\"aucun_monde\": true`\n"
            "   et pas de `CARTES-partiel.json` ;",
            "`rapatrie-reel/liste-rapatriement-pilote-v70.json` et noms de la copie :\n"
            "   pas de `CARTES-partiel.json` ; le champ `\"aucun_monde\"` de cette liste rapporté, **sans arrêt** (il n'est pas dans la"
            " « Liste d'arrêt » ; la machine le garde elle-même, procédure v14, section 9) ;",
        ),
        # Point 0 : `appels_complets_illisibles` rapporté, sans arrêt.
        (
            " ; `appels_complets_illisibles` à 0 dans le relevé) ;",
            ") ; `appels_complets_illisibles` du relevé rapporté, **sans arrêt** (alinéa « Appels à réponse illisible » ci-dessous) ;",
        ),
        # Point 0 : alinéa ajouté en fin de point.
        (
            "au point 7 seul, il est écrit « non fait » sans arrêt.\n",
            "au point 7 seul, il est écrit « non fait » sans arrêt.\n" + ILLISIBLES,
        ),
        # Sous-section « Version 8 » en fin de pièce.
        (
            "  - Remarques facultatives F1 à F6 : non appliquées (non exigées).\n",
            "  - Remarques facultatives F1 à F6 : non appliquées (non exigées).\n" + VERSION_8,
        ),
    ]


VERSION_8 = """
### Version 8 (arrêt d'un premier lecteur au point 0)

- **Fait** : un premier lecteur de l'issue s'est arrêté au point 0 de la v7 parce que le relevé porte
  `appels_complets_illisibles` différent de 0, critère que la v7 exigeait « à 0 » et que la « Liste d'arrêt » du texte scellé
  (`8aa33014…`) ne contient pas. Le verdict de ce lecteur et les pièces de la sortie n'ont pas été ouverts par le rédacteur de la v8.
- **Ce que le code dit** (lu au commit `2d35cafa` de `lot/compte-organisme-v1` : arbre de l'organisme, tête `605e0f6`, paquet
  `arbre-organisme-complet-605e0f6.bundle`, `e3d83e47…`, égal à son compagnon ; empreintes du lanceur `5dc01676…`, de
  `pole/pilote_mr2_v70.py` `7541b0c3…`, de `pole/proposeurs_pilote_v70.py` `f1152a4d…` et de `mesure_pilote_v4.py` `676d5f37…`
  égales au bloc gelé du texte) : le champ compte les appels non en échec (complets ou tronqués) dont le texte ne donne aucune
  liste de propositions ; ils ne portent aucune carte ; la réponse brute et le témoin sont scellés avant l'extraction ; aucun
  code n'arrête le pilote ni ne refuse la mesure pour eux ; la mesure les classe « sans carte » (complets) ou « tronqué », hors
  du dénominateur, comptés à part, ce que disent « Métrique » et E-2 (i) ; un trop grand nombre mène à P-0 par le minimum.
  Ce n'est donc pas un arrêt du texte (ni « réponse brute absente », ni code 3, ni refus nommé, ni erreur de la mesure).
- **Arrêts du point 0 retirés** (absents de la « Liste d'arrêt », devenus des contrôles rapportés) : (1)
  `appels_complets_illisibles` à 0 (alinéa « Appels à réponse illisible ») ; (2) `exclus_balayage=` ne nommant aucune pièce
  remise (garde de la procédure ; une pièce exclue manque à la copie et la règle « non fait » s'applique aux contrôles qui
  l'exigent) ; (3) `"aucun_monde": true` (garde de confidentialité de la procédure, tenue par la machine).
- **Arrêts du point 0 gardés**, chacun relié à la « Liste d'arrêt » : `etat.txt` à `fini` sans autre état final (l'arrêt
  commun (A) de la procédure joue les arrêts de la liste ; un autre état final laisse un relevé partiel ou aucune mesure) ;
  codes d'étape à 0 (code 3 ; refus d'empreinte, de C-16 ou C-17, erreur de la mesure) ; une seule ligne à `lancements.jsonl`
  (aucune reprise sans texte neuf) ; pas de `CARTES-partiel.json`, relevé et manifeste complets (« Tout arrêt (code 3) ») ;
  réponse brute et témoin de chacun des 16 appels ; aucun coût au-dessus du pire cas ; aucune part atteinte, machine comprise
  (part de 3 USD de la ligne π2 du bloc gelé). La règle « un contrôle qu'il ne peut faire est un arrêt » est gardée : sans
  elle, l'absence d'un arrêt de la liste ne se constaterait pas (R5).
- **Application** : par le programme `appliquer-corrections-consigne-lecteur-issue-pilote-v14-v8.py` (même dossier) : empreinte
  de la v7 vérifiée, chaque « ancien » présent une seule fois, cible jamais écrasée ; rien d'autre de la v7 n'est changé.
- **À faire avant la remise** : contre-lecture de la v8 par un sous-agent neuf (R2).
"""


def main():
    if len(sys.argv) != 2:
        sys.exit("usage : HEURE_UTC")
    if CIBLE.exists():
        sys.exit(f"refus : {CIBLE.name} existe déjà")
    if empreinte(SOURCE) != EMPREINTE_SOURCE:
        sys.exit("refus : empreinte de la v7 inattendue")
    texte = SOURCE.read_text(encoding="utf-8")
    for ancien, nouveau in couples(sys.argv[1]):
        n = texte.count(ancien)
        if n != 1:
            sys.exit(f"refus : « {ancien[:60]}… » figure {n} fois")
        texte = texte.replace(ancien, nouveau)
    with open(CIBLE, "x", encoding="utf-8") as f:
        f.write(texte)
    print(f"écrit : {CIBLE.name} {empreinte(CIBLE)}")


if __name__ == "__main__":
    main()
