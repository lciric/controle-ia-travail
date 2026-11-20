#!/usr/bin/env python3
"""Relevé des motifs de données internes, section par section, dans la question v4 (et la v3 pour comparaison) — v1.

Contre-lecteur neuf, modèle O. Bibliothèque standard seulement. Lit les fichiers donnés en arguments, n'écrit que sur la
sortie standard. Usage :

    python3 -B releve_motifs_question_v4_v1.py QUESTION_V3 QUESTION_V4

Ce qu'il fait :
  1. découpe chaque question en sections : « en-tête » (avant le premier titre « ## »), puis une section par titre « ## » ;
  2. cherche dans chaque section les motifs du mandat (prénom et nom de famille du directeur, insensibles à la casse et aux
     accents ; « session_ » ; « @ » ; « R- » suivi de chiffres ; « GO-20 » ; « N-0 » ; le nom du compte distant ; « github » ;
     « controle-ia » ; « docs/ », « prereg/ », « registres/ », « donnees/ » ; suite hexadécimale de 16 caractères ou plus ;
     « CLAUDE.md »), puis des motifs complémentaires, rapportés à part (noms de règles « R » suivi d'un ou deux chiffres,
     « GO- », nom de fichier « .md » ou « .py », « modèle F » / « modèle O », « commit », noms de clés) ;
  3. rend, par section, le compte de chaque motif et les lignes touchées ; les noms de personne sont masqués à l'affichage ;
  4. compare, section par section, la v3 et la v4 à l'octet, et vérifie que la colonne « valeurs » de la table des axes du § 5
     est égale dans les deux versions (l'ordre des valeurs fixe la numérotation des cases au préenregistrement court) ;
  5. vérifie que les énoncés des trois règles dont le nom a été retiré sont présents dans la v4.
"""
from __future__ import annotations

import hashlib
import re
import sys
import unicodedata
from pathlib import Path


def sans_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)).casefold()


# Motifs du mandat. Le premier élément est l'étiquette ; « masque » dit si la valeur trouvée est masquée à l'affichage ;
# « pli » dit si la recherche se fait sur le texte sans accents et replié en casse.
MOTIFS_MANDAT = [
    ("prénom du directeur", r"lazar", True, True),
    ("nom de famille du directeur", r"ciric", True, True),
    ("session_", r"session_", False, False),
    ("@", r"@", False, False),
    ("R- suivi de chiffres", r"R-\d+", False, False),
    ("GO-20", r"GO-20", False, False),
    ("N-0", r"N-0", False, False),
    ("nom du compte distant", r"lciric", True, True),
    ("github", r"github", False, True),
    ("controle-ia", r"controle-ia", False, True),
    ("chemin docs/", r"docs/", False, False),
    ("chemin prereg/", r"prereg/", False, False),
    ("chemin registres/", r"registres/", False, False),
    ("chemin donnees/", r"donnees/", False, False),
    ("hexadécimal de 16 et plus", r"[0-9A-Fa-f]{16,}", False, False),
    ("CLAUDE.md", r"CLAUDE\.md", False, False),
]

MOTIFS_COMPLEMENTAIRES = [
    ("nom de règle R1 à R99", r"(?<![\w-])R\d{1,2}(?![\w-])", False, False),
    ("GO-", r"GO-", False, False),
    ("nom de fichier .md ou .py", r"[\w.-]+\.(?:md|py|json|diff|txt)\b", False, False),
    ("modèle F ou O", r"modèle [FO]\b", False, False),
    ("commit", r"commit", False, True),
    ("nom de clé (Minuit, Luc, Rigaud, KIMI)", r"\b(?:minuit|luc|rigaud|kimi)\b", True, True),
    ("nom de fournisseur ou de famille de modèle", r"\b(?:claude|anthropic|openai|fable|opus|sonnet|haiku|gpt|gemini)\b", True, True),
]


def decouper(texte: str) -> list[tuple[str, int, list[str]]]:
    """Liste de (titre, numéro de la première ligne, lignes)."""
    sections: list[tuple[str, int, list[str]]] = [("en-tête", 1, [])]
    for i, ligne in enumerate(texte.split("\n"), 1):
        if ligne.startswith("## "):
            sections.append((ligne[3:].strip(), i, [ligne]))
        else:
            sections[-1][2].append(ligne)
    return sections


def chercher(lignes: list[str], debut: int, motifs) -> list[tuple[str, int, int, list[str]]]:
    res = []
    for etiquette, motif, masque, pli in motifs:
        rx = re.compile(motif)
        touchees, total, valeurs = [], 0, []
        for k, ligne in enumerate(lignes):
            sujet = sans_accents(ligne) if pli else ligne
            trouves = rx.findall(sujet)
            if trouves:
                touchees.append(debut + k)
                total += len(trouves)
                for t in trouves:
                    v = "[masqué]" if masque else (t if len(t) <= 20 else t[:12] + "…")
                    if v not in valeurs:
                        valeurs.append(v)
        res.append((etiquette, total, touchees, valeurs))
    return res


def rendre(nom: str, texte: str) -> None:
    print(f"=== {nom} : {hashlib.sha256(texte.encode('utf-8')).hexdigest()} ===")
    for titre, debut, lignes in decouper(texte):
        fin = debut + len(lignes) - 1
        print(f"--- section « {titre} » (lignes {debut} à {fin}) ---")
        for groupe, motifs in (("mandat", MOTIFS_MANDAT), ("complémentaire", MOTIFS_COMPLEMENTAIRES)):
            r = chercher(lignes, debut, motifs)
            somme = sum(t for _, t, _, _ in r)
            print(f"  motifs du {groupe} : {somme} occurrence(s) au total")
            for etiquette, total, touchees, valeurs in r:
                if total:
                    print(f"    {etiquette} : {total} ; lignes {touchees} ; valeurs {valeurs}")


def section_octets(texte: str, prefixe: str) -> str | None:
    for titre, _, lignes in decouper(texte):
        if titre.startswith(prefixe):
            return "\n".join(lignes)
    return None


def colonne_valeurs_axes(texte: str) -> list[str]:
    s5 = section_octets(texte, "5.") or ""
    vals = []
    for ligne in s5.split("\n"):
        if ligne.startswith("| ") and not ligne.startswith("| axe") and not ligne.startswith("|---"):
            cellules = [c.strip() for c in ligne.strip("|").split("|")]
            if len(cellules) == 3:
                vals.append(cellules[0] + " || " + cellules[1])
    return vals


def main(argv: list[str]) -> int:
    if len(argv) == 2:
        # Relevé seul d'un autre texte servi (par exemple la pièce d'antériorité) : points 1 à 3, rien d'autre.
        rendre(f"relevé seul de {Path(argv[1]).name}", Path(argv[1]).read_bytes().decode("utf-8", errors="strict"))
        return 0
    if len(argv) != 3:
        print("usage : releve_motifs_question_v4_v1.py QUESTION_V3 QUESTION_V4 | releve_motifs_question_v4_v1.py TEXTE", file=sys.stderr)
        return 2
    v3 = Path(argv[1]).read_bytes().decode("utf-8", errors="strict")
    v4 = Path(argv[2]).read_bytes().decode("utf-8", errors="strict")
    rendre("question v4", v4)
    print()
    rendre("question v3 (pour comparaison)", v3)
    print()
    print("=== comparaison v3 / v4, section par section (texte de la section, titre compris) ===")
    s3 = {t: "\n".join(l) for t, _, l in decouper(v3)}
    for titre, _, lignes in decouper(v4):
        a = s3.get(titre)
        b = "\n".join(lignes)
        if a is None:
            print(f"  « {titre} » : absente de la v3 sous ce titre")
        else:
            egal = a.encode("utf-8") == b.encode("utf-8")
            print(f"  « {titre} » : {'égale à l octet' if egal else 'différente'}"
                  f" (v3 {hashlib.sha256(a.encode('utf-8')).hexdigest()[:16]}…, v4 {hashlib.sha256(b.encode('utf-8')).hexdigest()[:16]}…)")
    print()
    q3, q4 = section_octets(v3, "4."), section_octets(v4, "4.")
    print(f"§ 4 « La question servie » égal à l'octet : {q3 is not None and q3.encode('utf-8') == q4.encode('utf-8')}"
          f" ; empreinte du § 4 (v4) : {hashlib.sha256((q4 or '').encode('utf-8')).hexdigest()}")
    a3, a4 = colonne_valeurs_axes(v3), colonne_valeurs_axes(v4)
    print(f"§ 5, colonnes « axe » et « valeurs » de la table des axes égales : {a3 == a4} ({len(a4)} lignes)")
    print()
    print("=== énoncés des trois règles dont le nom est retiré, présents dans la v4 ===")
    for nom, enonce in (
        ("zone vierge (ancien renvoi R8)", "Une zone qui paraît vierge est une question ; plus elle séduit, plus elle se vérifie durement."),
        ("PDF empreinté (ancien renvoi R7)", "Aucune antériorité ne s'affirme sans pièce lue sur PDF empreinté, page citée."),
        ("même rang (ancien renvoi R3)", "« aucune fiche n'est inédite » et « plusieurs le sont » sont écrites au même rang."),
    ):
        print(f"  {nom} : {v4.count(enonce)} occurrence(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
