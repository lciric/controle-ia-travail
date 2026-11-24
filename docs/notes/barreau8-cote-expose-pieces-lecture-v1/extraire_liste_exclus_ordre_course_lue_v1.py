"""Extrait de la seule liste des exclus de l'ordre neuf de la course lue du saboteur à budget (barreau 8), v1.

CÔTÉ EXPOSÉ. Pièce de travail pour les mandats du lecteur et du juge des sondes (condition D-5 du texte des sondes, lue avec
l'additif 1 : « la liste des exclus de l'ordre neuf, à la section `exclus.section` » de la pièce d'attestation de l'ordre).

Recopie à l'octet, sans rien ajouter ni reformuler, les seuls passages qui nomment des exclus :
  1. pièce de rang 1 de l'ordre neuf (ordre de l'étalonnage v2, scellé), § 8, point 4 (section `1:8` de l'attestation) ;
  2. pièce de rang 0 (additif de la voie (A), scellé), en-tête, phrase « Le rédacteur entre dans la liste d'exclusion… » ;
  3. renvoi du point 1 au « § 8 de l'ordre de la première course » : brouillon 8 de l'ordre exploratoire, § 8, phrases
     d'exclusion (du début de « **Exclus de toute lecture » jusqu'à la fin du paragraphe) ;
  4. renvoi du brouillon 8 (« Comme au brouillon 3, § 8 ») : brouillon 3, § 8, puce « **Exclus de toute lecture… ».
Chaque source est exigée à son empreinte (celle de l'attestation de l'ordre pour les pièces 0 et 1 ; celle de son compagnon,
égale à la référence écrite ici, pour les brouillons 3 et 8). Chaque passage doit se trouver une seule fois. Aucun repli.

    python3 -I extraire_liste_exclus_ordre_course_lue_v1.py --racine-pieces DOSSIER --sortie CHEMIN

DOSSIER contient, à leur chemin relatif au dépôt, les quatre sources (les pièces de l'ordre sont prises sur leurs branches).
Écrit CHEMIN (jamais d'écrasement) et son compagnon `.sha256` ; imprime l'empreinte. Code 0 ; 1 sur toute garde.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

ATTESTATION_ORDRE = ("docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-ordre-course-lue-additif-1-v1.json",
                     "8f6b502581cb32d546e84cf13d52d07f1faa011484ef585bde3635f56e86e76a")
SOURCES = {
    "rang0": ("brouillons/ii-b-saboteur-budget-v5/additif-course-v1/additif-ordre-course-voie-A-v1.md",
              "8e1d340a2e676b722489e6ae68b6ed9cd7d96bcf95d42e3490557ab3db7fb6c9"),
    "rang1": ("brouillons/ii-b-saboteur-budget-v5/ordre-etalonnage-v5/ordre-etalonnage-ii-b-v5-v2.md",
              "7219083abf74a23ae2411b7d27d7da6cfb047731cfb0559d9af301542e5d1c64"),
    "b8": ("brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1-brouillon8.md",
           "eb83e9444df3bdfa822ef3bf76efe4039b450a7a8458fe4c91ba20f73d4eb76e"),
    "b3": ("brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1-brouillon3.md",
           "eed42f07329c5f064554b799f0d49ff0a1ed6e4571545c94dca3d6783f0c165f"),
}
AVERTISSEMENT = ("EXPLORATOIRE, NON OPPOSABLE (R-522) : liste des exclus de l'ordre neuf de la course lue, recopiée à l'octet, "
                 "sans autre contenu de l'ordre")


class Refus(Exception):
    pass


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def lire(racine: Path, cle: str) -> str:
    rel, attendu = SOURCES[cle]
    p = racine / rel
    if not p.is_file():
        raise Refus(f"{rel} absent")
    b = p.read_bytes()
    if sha(b) != attendu:
        raise Refus(f"{rel} : empreinte différente de la référence")
    return b.decode("utf-8")


def section(texte: str, titre: str) -> str:
    """Du titre « ## <titre> » (compris) au titre de niveau 2 suivant (exclu) ; une seule occurrence exigée."""
    lignes = texte.split("\n")
    debuts = [i for i, l in enumerate(lignes) if l.startswith("## " + titre)]
    if len(debuts) != 1:
        raise Refus(f"section « {titre} » : {len(debuts)} occurrence(s)")
    i = debuts[0]
    j = next((k for k in range(i + 1, len(lignes)) if lignes[k].startswith("## ") or lignes[k].startswith("# ")), len(lignes))
    return "\n".join(lignes[i:j])


def unique(texte: str, debut: str, fin: str | None, ou: str) -> str:
    """Passage qui commence par `debut` (une seule occurrence) et va jusqu'à `fin` comprise, ou jusqu'à la fin de la ligne."""
    if texte.count(debut) != 1:
        raise Refus(f"{ou} : début du passage trouvé {texte.count(debut)} fois")
    i = texte.index(debut)
    if fin is None:
        j = texte.find("\n", i)
        j = len(texte) if j < 0 else j
    else:
        k = texte.find(fin, i)
        if k < 0:
            raise Refus(f"{ou} : fin du passage absente")
        j = k + len(fin)
    return texte[i:j]


def construire(racine: Path) -> str:
    att = racine / ATTESTATION_ORDRE[0]
    if not att.is_file() or sha(att.read_bytes()) != ATTESTATION_ORDRE[1]:
        raise Refus("attestation de l'ordre absente ou d'empreinte différente")
    import json
    a = json.loads(att.read_text(encoding="utf-8"))
    pieces = [(a["ordre"]["chemin"], a["ordre"]["sha256"])] + [(p["chemin"], p["sha256"]) for p in a["ordre"]["pieces"]]
    if pieces[0] != SOURCES["rang0"] or pieces[1] != SOURCES["rang1"]:
        raise Refus("les pièces de rang 0 et 1 de l'attestation ne sont pas celles de ce programme")
    if a["exclus"]["section"] != "1:8":
        raise Refus("l'attestation ne place pas la liste des exclus à la section 1:8")
    r0, r1, b8, b3 = (lire(racine, k) for k in ("rang0", "rang1", "b8", "b3"))
    p1 = unique(section(r1, "8."), "4. **Aucune sonde n'est apprise", None, "rang 1, § 8, point 4")
    p0 = unique(r0, "Le rédacteur entre dans la liste d'exclusion des rôles côté sondes.", None, "rang 0, en-tête")
    p0 = p0[:len("Le rédacteur entre dans la liste d'exclusion des rôles côté sondes.")]
    p8 = unique(section(b8, "8."), "**Exclus de toute lecture des sondes du barreau 8**", None, "brouillon 8, § 8")
    p3 = unique(section(b3, "8."), "- **Exclus de toute lecture des sondes du barreau 8**", None, "brouillon 3, § 8")
    blocs = [
        ("1. Ordre neuf, pièce de rang 1, § 8, point 4 (section « 1:8 » de l'attestation de l'ordre)", SOURCES["rang1"], p1),
        ("2. Ordre neuf, pièce de rang 0, en-tête (ligne « Statut »), phrase d'exclusion", SOURCES["rang0"], p0),
        ("3. Renvoi du bloc 1 : « le § 8 de l'ordre de la première course », brouillon 8, § 8, phrases d'exclusion",
         SOURCES["b8"], p8),
        ("4. Renvoi du bloc 3 : « Comme au brouillon 3, § 8 », brouillon 3, § 8, puce d'exclusion", SOURCES["b3"], p3),
    ]
    out = ["# Liste des exclus de l'ordre neuf de la course lue (saboteur à budget, barreau 8) — extrait v1", "",
           f"> {AVERTISSEMENT}.", "",
           f"- Écrit par programme (`extraire_liste_exclus_ordre_course_lue_v1.py`) ; attestation de l'ordre : "
           f"`{ATTESTATION_ORDRE[0]}` (`{ATTESTATION_ORDRE[1]}`).",
           "- Chaque bloc recopie à l'octet un passage de sa source, entre les lignes `---8<---` ; rien n'est reformulé.", ""]
    for titre, (rel, s), passage in blocs:
        out += [f"## {titre}", "", f"Source : `{rel}` (`{s}`), passage `sha256` `{sha(passage.encode('utf-8'))}`.", "",
                "---8<---", passage, "---8<---", ""]
    return "\n".join(out)


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="extraire_liste_exclus_ordre_course_lue_v1")
    p.add_argument("--racine-pieces", required=True)
    p.add_argument("--sortie", required=True)
    a = p.parse_args(argv)
    sortie = Path(a.sortie)
    try:
        if sortie.exists() or Path(str(sortie) + ".sha256").exists():
            raise Refus(f"{sortie} existe déjà : R12 interdit d'écraser")
        texte = construire(Path(a.racine_pieces))
    except (Refus, KeyError, TypeError, ValueError) as e:
        print(f"EXTRAIT REFUSÉ : {e}", file=sys.stderr)
        return 1
    b = texte.encode("utf-8")
    sortie.write_bytes(b)
    s = sha(b)
    Path(str(sortie) + ".sha256").write_text(f"{s}  {sortie.name}\n", encoding="utf-8")
    print(f"EXTRAIT ÉCRIT : {sortie} sha256 {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
