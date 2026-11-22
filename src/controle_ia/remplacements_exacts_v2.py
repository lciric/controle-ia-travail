"""Application d'une liste fermée de remplacements exacts à un texte — v2.

Pièce d'instrument, classe B (session fille de l'attaquant informé, 22 novembre 2026). Copie corrigée de
remplacements_exacts_v1.py (inchangée, R12), après les contre-lectures de Sonnet et d'Opus :
- occurrences comptées avec chevauchement (str.count ne les voyait pas : « B\\nB » dans « B\\nB\\nB ») ;
- lecture et écriture en octets décodés à la main : aucune normalisation des fins de ligne ; empreintes sur les octets ;
- refus : « \\r » dans la liste ou dans la source, marque d'ordre d'octets (BOM) dans la liste, texte non NFC, ancien
  qui coupe un caractère combinant, numéros non ASCII ou à zéro de tête, ancien égal au nouveau, erreur de lecture ;
- écriture atomique : fichier temporaire du même dossier, puis lien dur vers le nom final (échoue s'il existe) ;
- option --marques TABLE.json : remet en clair, dans la liste seulement, les marques réversibles d'une copie servie
  (⟦D⟧, ⟦S1⟧, ⟦C1⟧…) avant l'analyse ; toute marque « ⟦…⟧ » restante, connue ou non, est refusée.

Rôle : produire un brouillon neuf d'un préenregistrement à partir du brouillon précédent et d'une liste rendue par un
concepteur, sans réécriture libre. Chaque ancien texte doit se trouver exactement une fois dans la source.

Format des blocs (tout le reste du fichier, hors lignes qui commencent par un marqueur, est ignoré) :

    <<<ANCIEN k
    texte exact de la source (une ou plusieurs lignes)
    ===NOUVEAU k
    texte de remplacement (zéro, une ou plusieurs lignes)
    >>>FIN k

k entier ASCII sans zéro de tête, croissant de 1 en 1 à partir de 1. Les marqueurs occupent une ligne entière.
Conventions : les lignes d'un ancien ou d'un nouveau sont jointes par « \\n », sans « \\n » final. Un nouveau sans ligne
vaut le texte vide ; un nouveau d'une ligne vide aussi. Pour qu'un ancien finisse par un saut de ligne, il faut une ligne
vide de plus. Aucune ligne d'un bloc, ni du reste du fichier, ne peut commencer par « <<<ANCIEN », « ===NOUVEAU » ou
« >>>FIN » : c'est refusé, sans échappement possible.

Garde (aucun repli silencieux, R5) : en cas de refus, code 4, message, rien d'écrit. Sortie déjà présente : code 3 (R12).
Le compagnon .sha256 de la sortie reste à produire par l'appelant (`python -m controle_ia.scellement sceller`).

Usage : python -m controle_ia.remplacements_exacts_v2 SOURCE REMPLACEMENTS SORTIE [--marques TABLE.json]
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import tempfile
import unicodedata
from dataclasses import dataclass

MARQUE_ANCIEN = re.compile(r"^<<<ANCIEN ([1-9][0-9]*)$", re.ASCII)
MARQUE_NOUVEAU = re.compile(r"^===NOUVEAU ([1-9][0-9]*)$", re.ASCII)
MARQUE_FIN = re.compile(r"^>>>FIN ([1-9][0-9]*)$", re.ASCII)
TOUTE_MARQUE = re.compile(r"^(<<<ANCIEN|===NOUVEAU|>>>FIN)")
MARQUE_REVERSIBLE = re.compile(r"⟦[^⟧\n]*⟧")
BOM = "﻿"


class RefusRemplacement(Exception):
    pass


@dataclass(frozen=True)
class Bloc:
    numero: int
    ancien: str
    nouveau: str


def _controle_texte(texte: str, nom: str, bom_admis: bool) -> None:
    if "\r" in texte:
        raise RefusRemplacement(f"{nom} : retour chariot « \\r » présent (fins de ligne « \\n » seules admises)")
    if not bom_admis and BOM in texte:
        raise RefusRemplacement(f"{nom} : marque d'ordre d'octets (BOM) présente")
    if not unicodedata.is_normalized("NFC", texte):
        raise RefusRemplacement(f"{nom} : texte non normalisé en NFC")


def remettre_marques(texte: str, table: dict[str, str]) -> str:
    for marque, valeur in table.items():
        if not MARQUE_REVERSIBLE.fullmatch(marque):
            raise RefusRemplacement(f"table des marques : clé mal formée {marque!r}")
        texte = texte.replace(marque, valeur)
    reste = MARQUE_REVERSIBLE.findall(texte)
    if reste:
        raise RefusRemplacement(f"marque réversible restante après remise en clair : {sorted(set(reste))}")
    return texte


def lire_blocs(texte: str) -> list[Bloc]:
    _controle_texte(texte, "liste", bom_admis=False)
    lignes = texte.split("\n")
    blocs: list[Bloc] = []
    i = 0
    while i < len(lignes):
        m = MARQUE_ANCIEN.match(lignes[i])
        if not m:
            if TOUTE_MARQUE.match(lignes[i]):
                raise RefusRemplacement(f"marqueur hors d'ordre ou mal formé, ligne {i + 1}")
            i += 1
            continue
        k = int(m.group(1))
        j = i + 1
        while j < len(lignes) and not MARQUE_NOUVEAU.match(lignes[j]):
            if TOUTE_MARQUE.match(lignes[j]):
                raise RefusRemplacement(f"bloc {k} : marqueur inattendu ligne {j + 1}")
            j += 1
        if j >= len(lignes) or int(MARQUE_NOUVEAU.match(lignes[j]).group(1)) != k:
            raise RefusRemplacement(f"bloc {k} : « ===NOUVEAU {k} » absent ou mal numéroté")
        f = j + 1
        while f < len(lignes) and not MARQUE_FIN.match(lignes[f]):
            if TOUTE_MARQUE.match(lignes[f]):
                raise RefusRemplacement(f"bloc {k} : marqueur inattendu ligne {f + 1}")
            f += 1
        if f >= len(lignes) or int(MARQUE_FIN.match(lignes[f]).group(1)) != k:
            raise RefusRemplacement(f"bloc {k} : « >>>FIN {k} » absent ou mal numéroté")
        ancien = "\n".join(lignes[i + 1:j])
        nouveau = "\n".join(lignes[j + 1:f])
        if ancien == "":
            raise RefusRemplacement(f"bloc {k} : ancien texte vide")
        if ancien == nouveau:
            raise RefusRemplacement(f"bloc {k} : nouveau texte égal à l'ancien")
        blocs.append(Bloc(k, ancien, nouveau))
        i = f + 1
    if not blocs:
        raise RefusRemplacement("aucun bloc de remplacement")
    if [b.numero for b in blocs] != list(range(1, len(blocs) + 1)):
        raise RefusRemplacement("numéros de blocs non consécutifs à partir de 1")
    return blocs


def occurrences(source: str, motif: str) -> list[int]:
    """Toutes les positions de motif dans source, chevauchements compris."""
    positions, p = [], source.find(motif)
    while p != -1:
        positions.append(p)
        p = source.find(motif, p + 1)
    return positions


def _coupe_un_caractere(source: str, debut: int, fin: int) -> bool:
    if unicodedata.combining(source[debut]):
        return True
    return fin < len(source) and bool(unicodedata.combining(source[fin]))


def appliquer(source: str, blocs: list[Bloc]) -> str:
    _controle_texte(source, "source", bom_admis=True)
    positions = []
    for b in blocs:
        trouvees = occurrences(source, b.ancien)
        if len(trouvees) != 1:
            raise RefusRemplacement(
                f"bloc {b.numero} : ancien texte trouvé {len(trouvees)} fois dans la source (exactement 1 exigé)")
        debut = trouvees[0]
        fin = debut + len(b.ancien)
        if _coupe_un_caractere(source, debut, fin):
            raise RefusRemplacement(f"bloc {b.numero} : l'ancien texte coupe un caractère combinant")
        positions.append((debut, fin, b))
    positions.sort(key=lambda p: p[0])
    for (_d1, f1, b1), (d2, _f2, b2) in zip(positions, positions[1:]):
        if d2 < f1:
            raise RefusRemplacement(f"blocs {b1.numero} et {b2.numero} : anciens textes qui se chevauchent")
    morceaux, curseur = [], 0
    for debut, fin, b in positions:
        morceaux.append(source[curseur:debut])
        morceaux.append(b.nouveau)
        curseur = fin
    morceaux.append(source[curseur:])
    return "".join(morceaux)


def _lire(chemin: str, nom: str) -> tuple[bytes, str]:
    try:
        with open(chemin, "rb") as f:
            octets = f.read()
        return octets, octets.decode("utf-8")
    except (OSError, UnicodeDecodeError) as e:
        raise RefusRemplacement(f"{nom} illisible ({type(e).__name__}) : {chemin}") from e


def _ecrire_atomique(chemin: str, octets: bytes) -> None:
    dossier = os.path.dirname(os.path.abspath(chemin))
    fd, temporaire = tempfile.mkstemp(dir=dossier, prefix=".remplacements-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(octets)
            f.flush()
            os.fsync(f.fileno())
        os.link(temporaire, chemin)  # échoue si le nom final existe : jamais d'écrasement
    finally:
        os.unlink(temporaire)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    table = None
    if "--marques" in argv:
        i = argv.index("--marques")
        if i + 1 >= len(argv):
            print("REFUS : --marques sans fichier", file=sys.stderr)
            return 2
        table = argv[i + 1]
        del argv[i:i + 2]
    if len(argv) != 3:
        print(__doc__.strip().splitlines()[-1], file=sys.stderr)
        return 2
    chemin_source, chemin_blocs, chemin_sortie = argv
    if os.path.exists(chemin_sortie):
        print(f"REFUS : {chemin_sortie} existe déjà (R12)", file=sys.stderr)
        return 3
    try:
        o_source, source = _lire(chemin_source, "source")
        o_blocs, texte_blocs = _lire(chemin_blocs, "liste")
        if table is not None:
            o_table, texte_table = _lire(table, "table des marques")
            try:
                marques = json.loads(texte_table)["marques"]
            except (ValueError, KeyError, TypeError) as e:
                raise RefusRemplacement(f"table des marques mal formée : {table}") from e
            if not isinstance(marques, dict):
                raise RefusRemplacement(f"table des marques mal formée : {table}")
            texte_blocs = remettre_marques(texte_blocs, marques)
        blocs = lire_blocs(texte_blocs)
        sortie = appliquer(source, blocs)
        o_sortie = sortie.encode("utf-8")
        _ecrire_atomique(chemin_sortie, o_sortie)
    except RefusRemplacement as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 4
    except FileExistsError:
        print(f"REFUS : {chemin_sortie} existe déjà (R12)", file=sys.stderr)
        return 3
    h = lambda o: hashlib.sha256(o).hexdigest()
    ligne = f"source {h(o_source)} ; liste {h(o_blocs)} ; {len(blocs)} blocs ; sortie {h(o_sortie)}"
    if table is not None:
        ligne += f" ; table des marques {h(o_table)}"
    print(ligne)
    return 0


if __name__ == "__main__":
    sys.exit(main())
