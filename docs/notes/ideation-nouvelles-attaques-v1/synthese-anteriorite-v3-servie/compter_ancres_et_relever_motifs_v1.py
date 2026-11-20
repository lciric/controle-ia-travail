#!/usr/bin/env python3
"""Compte des ancres et relevé des motifs — synthèse d'antériorité servie — v1 (bibliothèque standard seulement).

Usage : python3 -B CE_FICHIER MODE ...

  ancres  CIBLE REMPLACEMENTS.json SORTIE
      compte chaque texte ancien du JSON dans la cible (occurrences à l'octet, chevauchantes comprises) ;
      écrit le rang, le compte et les lignes. Les textes eux-mêmes ne sont pas réaffichés (rang seulement).

  releve  FICHIER REFERENCE_V2B SORTIE
      relève dans FICHIER les motifs du mandat (0 attendu sur la version servie), puis, à part, des motifs
      complémentaires : noms de règles « R » et un ou deux chiffres ; mots de la ligne « Especes : » de la
      référence v2b (noms de fournisseurs, de familles de modèles, de clés), tirés de cette ligne par le
      programme et jamais écrits ici ; ces mots sont masqués à l'affichage.

SORTIE est créée en mode exclusif (jamais réécrite). Code 0 si le programme a tourné ; le total est dans la sortie.
Rédacteur neuf, modèle F.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path


def sans_accents(t: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def positions(meule: bytes, aiguille: bytes) -> list[int]:
    res, i = [], meule.find(aiguille)
    while i != -1:
        res.append(i)
        i = meule.find(aiguille, i + 1)
    return res


def mode_ancres(cible: Path, json_r: Path, sortie: Path) -> None:
    b = cible.read_bytes()
    donnees = json.loads(json_r.read_text(encoding="utf-8"))
    lignes = [f"=== compte des ancres : cible {cible.name} ({sha(b)}) ; JSON {json_r.name} ({sha(json_r.read_bytes())}) ==="]
    fautes = 0
    for rang, r in enumerate(donnees, 1):
        pos = positions(b, r["ancien"].encode("utf-8"))
        ou = [b.count(b"\n", 0, p) + 1 for p in pos]
        neuf_avant = len(positions(b, r["neuf"].encode("utf-8"))) if r["neuf"] else None
        if len(pos) != 1:
            fautes += 1
        lignes.append(f"  ancre n° {rang} : {len(pos)} occurrence(s) ; ligne(s) {ou} ; texte neuf présent avant : {neuf_avant}")
    lignes.append(f"total : {len(donnees)} ancre(s) ; {fautes} ancre(s) hors « exactement une »")
    ecrire(sortie, lignes)


MOTIFS_MANDAT = [
    ("prénom du directeur", r"\blazar\b", True),
    ("nom de famille du directeur", r"ciric", True),
    ("session_", r"session_", False),
    ("@", r"@", False),
    ("R- suivi de chiffres", r"R-\d+", False),
    ("N- suivi de chiffres", r"N-\d+", False),
    ("GO-20", r"GO-20", False),
    ("nom du compte distant", r"lciric", True),
    ("github", r"github", True),
    ("controle-ia", r"controle-ia", True),
    ("chemin docs/", r"docs/", False),
    ("chemin prereg/", r"prereg/", False),
    ("chemin registres/", r"registres/", False),
    ("chemin donnees/", r"donnees/", True),
    ("hexadécimal de 16 et plus", r"[0-9a-fA-F]{16,}", False),
    ("CLAUDE.md", r"CLAUDE\.md", False),
    ("nom de clé en majuscules (_KEY ou _TOKEN)", r"[A-Z0-9_]+_(?:KEY|TOKEN)\b", False),
]

MASQUES = {"prénom du directeur", "nom de famille du directeur", "nom du compte distant"}


def mots_de_la_reference(reference: Path) -> list[str]:
    """Mots alphabétiques de 4 lettres et plus entre parenthèses, sur la ligne « Especes : » de la v2b."""
    for ligne in reference.read_text(encoding="utf-8").splitlines():
        if ligne.startswith("Especes :"):
            mots = set()
            for bloc in re.findall(r"\(([^)]*)\)", ligne):
                for m in re.findall(r"[A-Za-z]{4,}", bloc):
                    mots.add(m.casefold())
            return sorted(mots)
    return []


def chercher(texte_lignes: list[str], motif: str, replie: bool) -> list[tuple[int, str]]:
    res = []
    rx = re.compile(motif, re.IGNORECASE if replie else 0)
    for n, ligne in enumerate(texte_lignes, 1):
        vue = sans_accents(ligne) if replie else ligne
        for m in rx.finditer(vue):
            res.append((n, m.group(0)))
    return res


def mode_releve(fichier: Path, reference: Path, sortie: Path) -> None:
    b = fichier.read_bytes()
    texte_lignes = b.decode("utf-8").splitlines()
    out = [f"=== relevé des motifs : {fichier.name} ({sha(b)}) ; {len(texte_lignes)} lignes ==="]
    out.append("--- motifs du mandat (0 attendu sur la version servie) ---")
    total = 0
    for nom, motif, replie in MOTIFS_MANDAT:
        t = chercher(texte_lignes, motif, replie)
        total += len(t)
        if nom in MASQUES:
            valeurs = ["[masqué]"] if t else []
        else:
            valeurs = sorted({v if len(v) <= 12 else v[:12] + "…" for _, v in t})
        out.append(f"  {nom} : {len(t)} ; lignes {sorted({n for n, _ in t})} ; valeurs {valeurs}")
    out.append(f"  TOTAL motifs du mandat : {total}")
    out.append("--- motifs complémentaires (rapportés à part) ---")
    t = chercher(texte_lignes, r"\bR\d{1,2}\b", False)
    out.append(f"  nom de règle R1 à R99 : {len(t)} ; lignes {sorted({n for n, _ in t})} ; valeurs {sorted({v for _, v in t})}")
    total_c = len(t)
    mots = mots_de_la_reference(reference)
    out.append(f"  mots tirés de la ligne « Especes : » de la référence ({reference.name}, {sha(reference.read_bytes())}) : "
               f"{len(mots)} mot(s), masqués")
    t = []
    for mot in mots:
        t += chercher(texte_lignes, r"\b" + re.escape(mot) + r"\b", True)
    total_c += len(t)
    out.append(f"  nom de fournisseur, de famille de modèle ou de clé : {len(t)} ; lignes {sorted({n for n, _ in t})} ; "
               f"valeurs {['[masqué]'] if t else []}")
    out.append(f"  TOTAL motifs complémentaires : {total_c}")
    ecrire(sortie, out)


def ecrire(sortie: Path, lignes: list[str]) -> None:
    contenu = "\n".join(lignes) + "\n"
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(contenu)
    sys.stdout.write(contenu)


def main(argv: list[str]) -> int:
    if len(argv) == 4 and argv[0] == "ancres":
        mode_ancres(Path(argv[1]), Path(argv[2]), Path(argv[3]))
        return 0
    if len(argv) == 4 and argv[0] == "releve":
        mode_releve(Path(argv[1]), Path(argv[2]), Path(argv[3]))
        return 0
    sys.stderr.write(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
