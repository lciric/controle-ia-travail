"""Extrait de la seule liste des exclus de l'ordre neuf de la course lue du saboteur à budget (barreau 8), v2.

CÔTÉ EXPOSÉ. Pièce de travail pour les mandats du lecteur et du juge des sondes (condition D-5 du texte des sondes, lue avec
l'additif 1 : « la liste des exclus de l'ordre neuf, à la section `exclus.section` » de la pièce d'attestation de l'ordre).

v2 = v1 corrigée selon la contre-lecture d'un Opus 5.5 neuf (`contre-lecture-cote-expose-v1.md`) :
- B-1 : le renvoi « le § 8 de l'ordre de la première course » vise l'ordre SCELLÉ de la première course, que la pièce de rang 1
  nomme en tête (`ordre-exploratoire-ii-b-v1.md`, `43a7a050…`), non son brouillon 8 ; phrases d'exclusion de son en-tête prises ;
- M-1 : la pièce de rang 2 (additif 1 de l'ordre de l'étalonnage) est exigée à son empreinte, scellée, et fouillée : l'extrait
  écrit qu'elle ne porte aucune phrase d'exclusion, ou refuse si elle en porte une que ce programme ne recopie pas ;
- M-2 : la phrase d'exclusion de l'en-tête de la pièce de rang 1 est prise ;
- m-1 : la puce « Jamais montré » du brouillon 3 est prise ; m-3 : l'identification du rédacteur de la pièce de rang 0 est prise ;
- m-4 : chaque source est comparée à sa référence ET à son compagnon `.sha256` ; m-5, m-6 : écriture exclusive (« xb »),
  erreurs du système rendues en refus ; m-8 : imports en tête.
Recopie à l'octet, sans rien reformuler. Chaque passage doit se trouver une seule fois. Aucun repli.

    python3 -I extraire_liste_exclus_ordre_course_lue_v2.py --racine-pieces DOSSIER --sortie CHEMIN

DOSSIER contient, à leur chemin relatif au dépôt, l'attestation de l'ordre, les trois pièces de l'ordre neuf, l'ordre scellé de la
première course et son brouillon 3, chacun avec son compagnon. Écrit CHEMIN et son compagnon ; imprime l'empreinte. Code 0 ; 1 sinon.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ATTESTATION_ORDRE = ("docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-ordre-course-lue-additif-1-v1.json",
                     "8f6b502581cb32d546e84cf13d52d07f1faa011484ef585bde3635f56e86e76a")
SOURCES = {
    "rang0": ("brouillons/ii-b-saboteur-budget-v5/additif-course-v1/additif-ordre-course-voie-A-v1.md",
              "8e1d340a2e676b722489e6ae68b6ed9cd7d96bcf95d42e3490557ab3db7fb6c9"),
    "rang1": ("brouillons/ii-b-saboteur-budget-v5/ordre-etalonnage-v5/ordre-etalonnage-ii-b-v5-v2.md",
              "7219083abf74a23ae2411b7d27d7da6cfb047731cfb0559d9af301542e5d1c64"),
    "rang2": ("brouillons/ii-b-saboteur-budget-v5/ordre-etalonnage-v5/additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon3.md",
              "a9d43d5921252b4d60152a4d7b48e4cab50633337b53fcbe3f9e9ee80f754b92"),
    "premiere": ("brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1.md",
                 "43a7a050d769792f3c5d7859509b69f34e082f953840909a1f59a1535bf01b3e"),
    "b3": ("brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1-brouillon3.md",
           "eed42f07329c5f064554b799f0d49ff0a1ed6e4571545c94dca3d6783f0c165f"),
}
# Motifs d'une phrase d'exclusion, cherchés dans la pièce de rang 2 (M-1).
MOTIFS_EXCLUSION = re.compile(r"exclu|exclusion|côté sondes|lecteur des sondes", re.I)
AVERTISSEMENT = ("EXPLORATOIRE, NON OPPOSABLE (R-522) : liste des exclus de l'ordre neuf de la course lue, recopiée à l'octet, "
                 "sans autre contenu de l'ordre")

# (titre du bloc, source, section « ## <titre> » où chercher ou None pour tout le texte, début, fin comprise ou None = fin de ligne)
PASSAGES = [
    ("1. Ordre neuf, pièce de rang 1, § 8, point 4 (section « 1:8 » de l'attestation de l'ordre)",
     "rang1", "8.", "4. **Aucune sonde n'est apprise", None),
    ("2. Ordre neuf, pièce de rang 1, en-tête, phrase d'exclusion de son rédacteur",
     "rang1", None, "Il entre dans la liste d'exclusion des rôles côté sondes (§ 8).", "Il entre dans la liste d'exclusion des rôles côté sondes (§ 8)."),
    ("3. Ordre neuf, pièce de rang 0, en-tête (ligne « Statut »), identification du rédacteur",
     "rang0", None, "Écrit le 2026-11-22 vers 18:53Z (`date -u`) par Claude Fable 5.2, rédacteur, du côté du saboteur",
     "du côté du saboteur"),
    ("4. Ordre neuf, pièce de rang 0, en-tête (ligne « Statut »), phrase d'exclusion",
     "rang0", None, "Le rédacteur entre dans la liste d'exclusion des rôles côté sondes.",
     "Le rédacteur entre dans la liste d'exclusion des rôles côté sondes."),
    ("5. Renvoi du bloc 1 : « le § 8 de l'ordre de la première course » (ordre scellé que la pièce de rang 1 nomme en tête), § 8, "
     "phrases d'exclusion", "premiere", "8.", "**Exclus de toute lecture des sondes du barreau 8**", None),
    ("6. Même ordre scellé de la première course, en-tête : rédacteur du brouillon 11",
     "premiere", None, "Écrit le 2026-11-19 vers 08:29 UTC (`date -u`) par le rédacteur du brouillon 11", "côté sondes du barreau 8"),
    ("7. Même ordre scellé de la première course, en-tête : rédacteur neuf de 08:26 UTC",
     "premiere", None, "Écrit le 2026-11-19 vers 08:26 UTC (`date -u`) par un rédacteur neuf", "(rédaction, contre-lecture, lecture, verdict ; § 8)."),
    ("8. Même ordre scellé de la première course, en-tête : rédacteur du brouillon 9",
     "premiere", None, "Écrit le 2026-11-19 vers 07:56 UTC (`date -u`) par le rédacteur du brouillon 9", "côté sondes du barreau 8"),
    ("9. Même ordre scellé de la première course, en-tête : rédacteur neuf de 07:48 UTC",
     "premiere", None, "Écrit le 2026-11-19 vers 07:48 UTC (`date -u`) par un rédacteur neuf", "(rédaction, contre-lecture, lecture, verdict ; § 8)."),
    ("10. Renvoi du bloc 5 : « Comme au brouillon 3, § 8 », brouillon 3, § 8, puce « Jamais montré »",
     "b3", "8.", "- **Jamais montré**", None),
    ("11. Renvoi du bloc 5 : « Comme au brouillon 3, § 8 », brouillon 3, § 8, puce d'exclusion",
     "b3", "8.", "- **Exclus de toute lecture des sondes du barreau 8**", None),
]


class Refus(Exception):
    pass


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def lire_exige(racine: Path, rel: str, attendu: str) -> bytes:
    p = racine / rel
    if not p.is_file():
        raise Refus(f"{rel} absent")
    b = p.read_bytes()
    if sha(b) != attendu:
        raise Refus(f"{rel} : empreinte différente de la référence")
    comp = Path(str(p) + ".sha256")
    if not comp.is_file() or comp.read_text(encoding="utf-8").split()[:1] != [attendu]:
        raise Refus(f"{rel} : compagnon .sha256 absent ou différent")
    return b


def section(texte: str, titre: str) -> str:
    """Du titre « ## <titre> » (compris) au titre de niveau 1 ou 2 suivant (exclu) ; une seule occurrence exigée."""
    lignes = texte.split("\n")
    debuts = [i for i, l in enumerate(lignes) if l.startswith("## " + titre)]
    if len(debuts) != 1:
        raise Refus(f"section « {titre} » : {len(debuts)} occurrence(s)")
    i = debuts[0]
    j = next((k for k in range(i + 1, len(lignes)) if lignes[k].startswith("## ") or lignes[k].startswith("# ")), len(lignes))
    return "\n".join(lignes[i:j])


def unique(texte: str, debut: str, fin: str | None, ou: str) -> str:
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
    if "\n" in texte[i:j] and fin is not None:
        raise Refus(f"{ou} : le passage déborde de sa ligne")
    return texte[i:j]


def construire(racine: Path) -> str:
    a = json.loads(lire_exige(racine, *ATTESTATION_ORDRE).decode("utf-8"))
    pieces = [{"chemin": a["ordre"]["chemin"], "sha256": a["ordre"]["sha256"], "scelle": a["ordre"]["scelle"]}] + list(a["ordre"]["pieces"])
    if len(pieces) != 3:
        raise Refus(f"l'attestation liste {len(pieces)} pièces, trois attendues")
    for rang, p in enumerate(pieces):
        if (p["chemin"], p["sha256"]) != SOURCES[f"rang{rang}"] or p["scelle"] != "oui":
            raise Refus(f"pièce de rang {rang} de l'attestation : autre que celle de ce programme, ou non scellée")
    if a["exclus"]["section"] != "1:8":
        raise Refus("l'attestation ne place pas la liste des exclus à la section 1:8")
    textes = {k: lire_exige(racine, rel, s).decode("utf-8") for k, (rel, s) in SOURCES.items()}
    # M-1 : la pièce de rang 2 ne doit porter aucune phrase d'exclusion (ce programme n'en recopie aucune).
    touches = [n for n, l in enumerate(textes["rang2"].split("\n"), 1) if MOTIFS_EXCLUSION.search(l)]
    if touches:
        raise Refus(f"pièce de rang 2 : motif d'exclusion aux lignes {touches} ; ce programme ne la recopie pas : à revoir")
    out = ["# Liste des exclus de l'ordre neuf de la course lue (saboteur à budget, barreau 8) — extrait v2", "",
           f"> {AVERTISSEMENT}.", "",
           "- Écrit par programme (`extraire_liste_exclus_ordre_course_lue_v2.py`) ; attestation de l'ordre : "
           f"`{ATTESTATION_ORDRE[0]}` (`{ATTESTATION_ORDRE[1]}`), trois pièces, toutes « scellé : oui ».",
           "- Chaque bloc recopie à l'octet un passage de sa source, entre les lignes `---8<---` ; rien n'est reformulé.",
           f"- Pièce de rang 2 (`{SOURCES['rang2'][0]}`, `{SOURCES['rang2'][1]}`) : aucune ligne ne porte les motifs "
           f"`{MOTIFS_EXCLUSION.pattern}` ; elle ne nomme aucun exclu.", ""]
    for titre, cle, sect, debut, fin in PASSAGES:
        rel, s = SOURCES[cle]
        lieu = section(textes[cle], sect) if sect else textes[cle]
        passage = unique(lieu, debut, fin, titre)
        out += [f"## {titre}", "", f"Source : `{rel}` (`{s}`), passage `sha256` `{sha(passage.encode('utf-8'))}`.", "",
                "---8<---", passage, "---8<---", ""]
    return "\n".join(out)


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="extraire_liste_exclus_ordre_course_lue_v2")
    p.add_argument("--racine-pieces", required=True)
    p.add_argument("--sortie", required=True)
    a = p.parse_args(argv)
    sortie = Path(a.sortie)
    compagnon = Path(str(sortie) + ".sha256")
    try:
        if sortie.exists() or compagnon.exists():
            raise Refus(f"{sortie} existe déjà : R12 interdit d'écraser")
        b = construire(Path(a.racine_pieces)).encode("utf-8")
        s = sha(b)
        with open(compagnon, "x", encoding="utf-8") as f:       # compagnon d'abord : jamais un extrait sans compagnon
            f.write(f"{s}  {sortie.name}\n")
        with open(sortie, "xb") as f:
            f.write(b)
    except (Refus, KeyError, TypeError, ValueError, OSError) as e:
        print(f"EXTRAIT REFUSÉ : {type(e).__name__} : {e}", file=sys.stderr)
        return 1
    print(f"EXTRAIT ÉCRIT : {sortie} sha256 {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
