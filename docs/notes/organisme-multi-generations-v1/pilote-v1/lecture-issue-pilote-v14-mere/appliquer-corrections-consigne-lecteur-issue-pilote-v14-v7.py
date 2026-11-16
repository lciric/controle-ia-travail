"""Applique à la consigne v6 les corrections du tour 1 de sa contre-lecture (v6 → v7).

Couples « ancien → nouveau » : chaque « ancien » doit figurer exactement une fois dans la v6 ;
l'empreinte de la v6 et celle du rapport sont vérifiées ; la cible n'est jamais écrasée (R12).
Usage : python appliquer-corrections-consigne-lecteur-issue-pilote-v14-v7.py HEURE_UTC
"""
import hashlib
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "consigne-lecteur-issue-pilote-v14-v6.md"
CIBLE = ICI / "consigne-lecteur-issue-pilote-v14-v7.md"
RAPPORT = ICI / "contre-lecture-consigne-lecteur-issue-pilote-v14-v6-tour1-v1.md"
EMPREINTE_SOURCE = "0fcd736cc30ea2b2c1c002c16817fdf0ebd7cc6c4ec7673df7ac940f42a49468"
EMPREINTE_RAPPORT = "63965d0f0966defcbb53012ef0b20610de4bff462f99e5bc3c56826939abfac7"


def empreinte(chemin):
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def couples(heure):
    return [
        # En-tête : titre et version.
        (
            "# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v6\n",
            "# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v7\n",
        ),
        (
            "Version 6, 2026-11-16T15:07:46Z (`date -u`, lue juste avant l'écriture et le scellement) : correction du tour 3 de la contre-lecture de la v3 et décisions de la mère (R-2992) appliquées (section « Contre-lecture », en fin de pièce) ; la v5 (`05f4f325…`),",
            f"Version 7, {heure} (`date -u`, lue juste avant l'écriture et le scellement) : corrections du tour 1 de la contre-lecture de la v6 appliquées (section « Contre-lecture », en fin de pièce) ; la v6 (`0fcd736c…`), la v5 (`05f4f325…`),",
        ),
        # m1, couple 1.
        (
            "`fichier_mondes_sha256` du manifeste égal à `H` inscrit",
            "`controles.mondes.fichier_mondes_sha256` du manifeste égal à `H` inscrit",
        ),
        # m1, couple 2.
        (
            "empreintes de mondes égales à `S1` à `S4` (la liste",
            "empreintes de mondes (`controles.mondes.mondes_sha256` du manifeste, indexé par numéro de monde : le monde k égal à `Sk`) égales à `S1` à `S4` (la liste",
        ),
        # m2.
        (
            "liste `hors_corps.modules_importes` de la sortie de mesure comparée au bloc",
            "liste `hors_corps.modules_importes` de la sortie de mesure (13 couples [chemin relatif à `orchestrator/mr2_v68/`, empreinte]) comparée, comme ensemble, aux 13 lignes `orchestrator/mr2_v68/…` du bloc",
        ),
        # m3, couple 1.
        (
            "- **Application** : par un rédacteur neuf (modèle C), qui n'a écrit ni la v1, ni le texte scellé, ni le code, par le programme",
            "- **Application** : par le rédacteur des corrections (modèle A), qui n'a pas écrit le texte scellé ni le code, par le programme",
        ),
        # m3, couple 2, puis sous-section du tour 1 de la v6 ajoutée en fin de pièce.
        (
            "  - Non touchée : la puce « Application » du tour 1 (« rédacteur neuf (modèle C) »), que ni ce rapport ni les décisions\n"
            "    transmises ne nomment ; R-2992 (point 0) dit fausses les mentions « lettre C » des rédacteurs lancés au modèle A : à la\n"
            "    mère de dire si celle-ci en est une.\n",
            "  - Rectifiée : la puce « Application » du tour 1, qui disait « rédacteur neuf (modèle C) », dit désormais « le rédacteur des\n"
            "    corrections (modèle A) » : R-2992 (point 0) tient fausses les mentions « lettre C » des rédacteurs de corrections lancés au\n"
            "    modèle A.\n"
            + TOUR1_V6,
        ),
        # m4.
        (
            "et, si l'issue est P-2, la phrase",
            "et, si l'issue est P-2 (avec ou sans réserve) et que `regle.classe` vaut « favorable », la phrase",
        ),
    ]


TOUR1_V6 = """
### Tour 1 de la v6

- **Rapport** : `contre-lecture-consigne-lecteur-issue-pilote-v14-v6-tour1-v1.md` (même dossier), empreinte
  `63965d0f0966defcbb53012ef0b20610de4bff462f99e5bc3c56826939abfac7` (égale à son compagnon) ; verdict « corrections » (aucune
  majeure, quatre mineures) ; pièce lue : la v6, `0fcd736cc30ea2b2c1c002c16817fdf0ebd7cc6c4ec7673df7ac940f42a49468`.
- **Application** : par un rédacteur neuf des corrections, qui n'a écrit ni le texte scellé ni le code, par le programme
  `appliquer-corrections-consigne-lecteur-issue-pilote-v14-v7.py` (même dossier) : empreintes de la v6 et du rapport vérifiées,
  chaque « ancien » présent une seule fois, cible jamais écrasée. `diff` v5 → v6 relu : la correction du tour 3 de la v3 (trois
  couples) et les décisions de la mère (pièce de dépense, sommet final, section « Pour les cribles ») y sont appliquées fidèlement,
  rien d'autre. Noms des pièces citées revérifiés présents dans la copie de sortie (noms et tailles seulement, aucune pièce de la
  copie ouverte ; aucun `CARTES-partiel.json`). Texte scellé relu (`8aa33014…`) : 31 lignes au bloc gelé, dont 13 sous
  `orchestrator/mr2_v68/` ; phrase « Une issue P-2 favorable ne dit pas… » et colonne de classe (« favorable », « défavorable »).
- **Réponse point par point** :
  - m1 (chemins `controles.mondes.…` du manifeste, deux couples) : appliquée mot pour mot.
  - m2 (comparaison de `hors_corps.modules_importes` aux 13 lignes `orchestrator/mr2_v68/…` du bloc gelé) : appliquée mot pour mot.
  - m3 (puce « Application » du tour 1 et question laissée à la mère, deux couples) : appliquée mot pour mot. La condition du
    rapport est tenue par R-2982 (13:08Z : « les corrections sont écrites par A »), antérieure à la passe v1 → v2 (13:36Z), et
    par R-2992 (point 0 : les rédacteurs de corrections lancés au modèle A ont été servis par le modèle A).
  - m4 (phrase du point 6 limitée au P-2 favorable) : appliquée mot pour mot.
  - Remarques facultatives F1 à F6 : non appliquées (non exigées).
"""


def main():
    if len(sys.argv) != 2:
        sys.exit("usage : HEURE_UTC")
    if CIBLE.exists():
        sys.exit(f"refus : {CIBLE.name} existe déjà")
    if empreinte(SOURCE) != EMPREINTE_SOURCE:
        sys.exit("refus : empreinte de la v6 inattendue")
    if empreinte(RAPPORT) != EMPREINTE_RAPPORT:
        sys.exit("refus : empreinte du rapport inattendue")
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
