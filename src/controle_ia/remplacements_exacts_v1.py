"""Application d'une liste fermée de remplacements exacts à un texte — v1.

Pièce d'instrument, classe B (session fille de l'attaquant informé, 22 novembre 2026). Sert à produire un brouillon neuf
d'un préenregistrement à partir d'un brouillon précédent et d'une liste de remplacements rendue par un concepteur, sans
réécriture libre : chaque ancien texte doit se trouver exactement une fois dans la source, sinon rien n'est écrit.

Format des blocs dans le fichier de remplacements (tout le reste du fichier est ignoré) :

    <<<ANCIEN k
    texte exact de la source (une ou plusieurs lignes)
    ===NOUVEAU k
    texte de remplacement (peut être vide)
    >>>FIN k

où k est un entier, croissant de 1 en 1 à partir de 1. Les marqueurs occupent une ligne entière.

Garde (aucun repli silencieux, R5) : refus, code non nul et rien d'écrit si : aucun bloc ; numéros non consécutifs ;
marqueur mal formé ou non fermé ; ancien texte vide ; ancien texte absent ou présent plus d'une fois dans la source ;
deux anciens textes qui se chevauchent dans la source ; fichier de sortie déjà présent (R12).
Les remplacements sont appliqués sur la source d'origine (positions calculées avant tout remplacement), donc l'ordre ne
change pas le résultat et un nouveau texte ne peut jamais être repris par un autre bloc.

Usage : python -m controle_ia.remplacements_exacts_v1 SOURCE REMPLACEMENTS SORTIE
"""
from __future__ import annotations

import hashlib
import os
import re
import sys
from dataclasses import dataclass

MARQUE_ANCIEN = re.compile(r"^<<<ANCIEN (\d+)$")
MARQUE_NOUVEAU = re.compile(r"^===NOUVEAU (\d+)$")
MARQUE_FIN = re.compile(r"^>>>FIN (\d+)$")
TOUTE_MARQUE = re.compile(r"^(<<<ANCIEN|===NOUVEAU|>>>FIN)\b")


class RefusRemplacement(Exception):
    pass


@dataclass(frozen=True)
class Bloc:
    numero: int
    ancien: str
    nouveau: str


def lire_blocs(texte: str) -> list[Bloc]:
    lignes = texte.split("\n")
    blocs: list[Bloc] = []
    i = 0
    while i < len(lignes):
        ligne = lignes[i]
        m = MARQUE_ANCIEN.match(ligne)
        if not m:
            if TOUTE_MARQUE.match(ligne):
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
        blocs.append(Bloc(k, ancien, nouveau))
        i = f + 1
    if not blocs:
        raise RefusRemplacement("aucun bloc de remplacement")
    attendus = list(range(1, len(blocs) + 1))
    if [b.numero for b in blocs] != attendus:
        raise RefusRemplacement("numéros de blocs non consécutifs à partir de 1")
    return blocs


def appliquer(source: str, blocs: list[Bloc]) -> str:
    positions = []
    for b in blocs:
        n = source.count(b.ancien)
        if n != 1:
            raise RefusRemplacement(f"bloc {b.numero} : ancien texte trouvé {n} fois dans la source (exactement 1 exigé)")
        debut = source.index(b.ancien)
        positions.append((debut, debut + len(b.ancien), b))
    positions.sort(key=lambda p: p[0])
    for (d1, f1, b1), (d2, _f2, b2) in zip(positions, positions[1:]):
        if d2 < f1:
            raise RefusRemplacement(f"blocs {b1.numero} et {b2.numero} : anciens textes qui se chevauchent")
    morceaux, curseur = [], 0
    for debut, fin, b in positions:
        morceaux.append(source[curseur:debut])
        morceaux.append(b.nouveau)
        curseur = fin
    morceaux.append(source[curseur:])
    return "".join(morceaux)


def sha256(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 3:
        print(__doc__.strip().splitlines()[-1], file=sys.stderr)
        return 2
    chemin_source, chemin_blocs, chemin_sortie = argv
    if os.path.exists(chemin_sortie):
        print(f"REFUS : {chemin_sortie} existe déjà (R12)", file=sys.stderr)
        return 3
    with open(chemin_source, encoding="utf-8") as f:
        source = f.read()
    with open(chemin_blocs, encoding="utf-8") as f:
        texte_blocs = f.read()
    try:
        blocs = lire_blocs(texte_blocs)
        sortie = appliquer(source, blocs)
    except RefusRemplacement as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 4
    with open(chemin_sortie, "x", encoding="utf-8") as f:
        f.write(sortie)
    print(f"source {sha256(source)} ; remplacements {sha256(texte_blocs)} ; {len(blocs)} blocs ; sortie {sha256(sortie)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
