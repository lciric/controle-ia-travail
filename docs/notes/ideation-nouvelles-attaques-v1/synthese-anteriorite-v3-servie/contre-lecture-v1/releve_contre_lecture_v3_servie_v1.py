#!/usr/bin/env python3
"""Relevé du contre-lecteur — synthèse d'antériorité servie v3 — v1 (bibliothèque standard seulement).

Usage : python3 -B CE_FICHIER V2B V3 SORTIE

Relève dans V3 (et dans V2B comme témoin positif) :
  (a) les motifs du mandat (prénom et nom du directeur, session_, @, R- et N- suivis de chiffres, GO-20, nom du compte
      distant, github, controle-ia, docs/, prereg/, registres/, donnees/, hexadécimal de 16 et plus, CLAUDE.md, noms de
      clés _KEY/_TOKEN) ;
  (b) des motifs complémentaires : noms de règles R et chiffres ; identifiants « lettres-tiret-chiffres » ; mots tirés des
      parenthèses de la ligne « Especes : » de V2B (jamais écrits ici, masqués) ; liste générique de noms de familles de
      modèles et de fournisseurs (masqués) ; accents graves, http, extensions de fichiers, courriels ;
  (c) les mots à majuscule initiale de V3 (pour lecture : tous doivent être des références publiques ou des termes neutres) ;
  (d) les caractères non ASCII de V3 ;
  (e) la comparaison ligne à ligne V2B → V3 : nombre de lignes, lignes changées, et intégrité des lignes 114 à 196
      (sections 3, 4 et 5 : références, combinaison, zones vierges) hors des seules lignes attendues ;
  (f) le compte des ancres des corrections proposées par le contre-lecteur (occurrences dans V3, chevauchantes comprises).

SORTIE est créée en mode exclusif. Contre-lecteur neuf, modèle O.
"""
from __future__ import annotations

import hashlib
import re
import sys
import unicodedata
from pathlib import Path

# (nom, motif, insensible à la casse et aux accents, masqué à l'affichage)
MOTIFS_MANDAT = [
    ("prénom du directeur", r"\blazar\b", True, True),
    ("nom de famille du directeur", r"ciric", True, True),
    ("session_", r"session_", True, False),
    ("@", r"@", False, False),
    ("R- suivi de chiffres", r"R-\d", False, False),
    ("N- suivi de chiffres", r"N-\d", False, False),
    ("GO-20", r"GO-20", True, False),
    ("nom du compte distant", r"lciric", True, True),
    ("github", r"github", True, False),
    ("controle-ia", r"controle-ia", True, False),
    ("docs/", r"docs/", True, False),
    ("prereg/", r"prereg/", True, False),
    ("registres/", r"registres/", True, False),
    ("donnees/", r"donnees/", True, False),
    ("hexadécimal de 16 et plus", r"[0-9a-fA-F]{16,}", False, False),
    ("CLAUDE.md", r"claude\.md", True, False),
    ("nom de clé _KEY ou _TOKEN", r"[A-Za-z0-9_]+_(?:KEY|TOKEN)\b", True, False),
]

COMPLEMENTAIRES = [
    ("nom de règle R et chiffres", r"\bR\d{1,3}\b", False, False),
    ("identifiant lettres-tiret-chiffres (2 chiffres et plus)", r"\b[A-Z]{1,5}-\d{2,}", False, False),
    ("GO- (toute forme)", r"\bGO-", False, False),
    ("accent grave (code ou chemin)", r"`", False, False),
    ("http", r"https?:", True, False),
    ("extension de fichier", r"\.(?:md|py|json|txt|sha256|diff|zip|yaml|yml|csv)\b", True, False),
    ("courriel", r"[\w.+-]+@[\w-]+\.[\w.]+", False, False),
    ("mot « session »", r"\bsession", True, False),
    ("mot « compte »", r"\bcompte\b", True, False),
    ("mot « cle » ou « clef »", r"\bcle[fs]?\b", True, False),
    ("mot « plafond »", r"\bplafond", True, False),
    ("mot « fournisseur »", r"\bfournisseur", True, False),
    ("mot « fabricant »", r"\bfabricant", True, False),
    ("mot « lignee »", r"\blignee", True, False),
    ("mot « directeur »", r"\bdirecteur", True, False),
    ("mot « registre »", r"\bregistre", True, False),
    ("mot « v2b » ou « v3 »", r"\bv2b\b|\bv3\b", True, False),
    ("mot « entretien »", r"entretien", True, False),
]

# Noms génériques de familles de modèles et de fournisseurs (masqués à l'affichage).
GENERIQUES = ["claude", "anthropic", "gemini", "google", "deepmind", "openai", "gpt", "chatgpt", "llama", "meta",
              "mistral", "qwen", "alibaba", "deepseek", "grok", "xai", "sonnet", "haiku", "moonshot", "kimi", "cohere",
              "phi", "microsoft", "gemma", "nvidia", "nemotron", "yi", "zhipu", "glm", "minimax", "baidu", "ernie"]

# Ancres des corrections proposées (texte exact de V3).
ANCRES = [
    ("C1 (8.2 pt 1)", "de trois fabricants differents (la v2b en nommait quatre)"),
    ("C2 (1.2 pt 3, à la mère)", "La demonstration d'avant-entretien doit preserver ce temoin."),
]


def sans_accents(t: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def chercher(lignes: list[str], motif: str, replie: bool) -> list[tuple[int, str]]:
    rx = re.compile(motif, re.IGNORECASE if replie else 0)
    res = []
    for n, ligne in enumerate(lignes, 1):
        vue = sans_accents(ligne) if replie else ligne
        for m in rx.finditer(vue):
            res.append((n, m.group(0)))
    return res


def rendre(nom: str, t: list[tuple[int, str]], masque: bool) -> str:
    lignes = sorted({n for n, _ in t})
    if masque:
        valeurs = ["[masqué]"] if t else []
    else:
        valeurs = sorted({v if len(v) <= 24 else v[:24] + "…" for _, v in t})
    return f"  {nom} : {len(t)} ; lignes {lignes} ; valeurs {valeurs}"


def mots_especes(lignes_v2b: list[str]) -> list[str]:
    for ligne in lignes_v2b:
        if ligne.startswith("Especes :"):
            mots = set()
            for bloc in re.findall(r"\(([^)]*)\)", ligne):
                for m in re.split(r"[,\s]+", bloc):
                    if re.search(r"[A-Za-z]", m) and len(m) >= 3:
                        mots.add(m.casefold())
            return sorted(mots)
    return []


def releve(nom_fichier: str, lignes: list[str], lignes_v2b: list[str], out: list[str]) -> tuple[int, int]:
    out.append(f"--- {nom_fichier} : motifs du mandat ---")
    total = 0
    for nom, motif, replie, masque in MOTIFS_MANDAT:
        t = chercher(lignes, motif, replie)
        total += len(t)
        out.append(rendre(nom, t, masque))
    out.append(f"  TOTAL motifs du mandat : {total}")
    out.append(f"--- {nom_fichier} : motifs complémentaires ---")
    for nom, motif, replie, masque in COMPLEMENTAIRES:
        out.append(rendre(nom, chercher(lignes, motif, replie), masque))
    mots = mots_especes(lignes_v2b)
    t = []
    for mot in mots:
        t += chercher(lignes, r"(?<![A-Za-z0-9])" + re.escape(mot) + r"(?![A-Za-z0-9])", True)
    out.append(f"  mots tirés des parenthèses de la ligne « Especes : » de la v2b ({len(mots)} mots, masqués)")
    out.append(rendre("  occurrences", t, True))
    total_noms = len(t)
    t = []
    for mot in GENERIQUES:
        t += chercher(lignes, r"\b" + re.escape(mot) + r"\b", True)
    out.append(f"  liste générique de familles et fournisseurs ({len(GENERIQUES)} mots, masqués)")
    out.append(rendre("  occurrences", t, True))
    total_noms += len(t)
    out.append(f"  TOTAL noms d'espèces et de fournisseurs : {total_noms}")
    return total, total_noms


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        sys.stderr.write(__doc__)
        return 2
    p2, p3, ps = (Path(a) for a in argv)
    b2, b3 = p2.read_bytes(), p3.read_bytes()
    l2, l3 = b2.decode("utf-8").splitlines(), b3.decode("utf-8").splitlines()
    out = [f"=== relevé du contre-lecteur ; v2b {p2.name} ({sha(b2)}, {len(l2)} lignes) ; "
           f"v3 {p3.name} ({sha(b3)}, {len(l3)} lignes) ==="]

    out.append("=== (a, b) témoin positif : v2b ===")
    releve("v2b", l2, l2, out)
    out.append("=== (a, b) version servie : v3 ===")
    tm, tn = releve("v3", l3, l2, out)
    out.append(f"BILAN v3 : motifs du mandat {tm} ; noms d'espèces et de fournisseurs {tn}")

    out.append("=== (c) mots à majuscule initiale de v3 (3 lettres et plus, hors début de phrase non filtré) ===")
    caps = {}
    for n, ligne in enumerate(l3, 1):
        for m in re.finditer(r"\b[A-ZÀ-Ý][A-Za-zÀ-ÿ'’-]{2,}", ligne):
            caps.setdefault(m.group(0), set()).add(n)
    for mot in sorted(caps):
        out.append(f"  {mot} : lignes {sorted(caps[mot])}")

    out.append("=== (d) caractères non ASCII de v3 ===")
    na = {}
    for c in b3.decode("utf-8"):
        if ord(c) > 127:
            na[c] = na.get(c, 0) + 1
    for c in sorted(na):
        out.append(f"  U+{ord(c):04X} {unicodedata.name(c, '?')} : {na[c]}")

    out.append("=== (e) comparaison ligne à ligne v2b → v3 ===")
    out.append(f"  lignes : v2b {len(l2)} ; v3 {len(l3)} ; égales : {len(l2) == len(l3)}")
    changees = [i + 1 for i in range(min(len(l2), len(l3))) if l2[i] != l3[i]]
    out.append(f"  lignes changées ({len(changees)}) : {changees}")
    zone = [n for n in changees if 114 <= n <= 196]
    out.append(f"  lignes changées dans 114 à 196 (sections 3 à 5) : {zone}")
    tables = [n for n in changees if 118 <= n <= 151]
    out.append(f"  lignes changées dans 118 à 151 (tables des références 3.1 à 3.3 et remarque d'intégrité) : {tables}")
    combi = [n for n in changees if 159 <= n <= 176]
    out.append(f"  lignes changées dans 159 à 176 (les quatorze éléments de la combinaison) : {combi}")

    out.append("=== (f) ancres des corrections proposées, comptées dans v3 ===")
    for nom, ancre in ANCRES:
        ab = ancre.encode("utf-8")
        pos, i = [], b3.find(ab)
        while i != -1:
            pos.append(i)
            i = b3.find(ab, i + 1)
        lig = [b3.count(b"\n", 0, p) + 1 for p in pos]
        out.append(f"  {nom} : {len(pos)} occurrence(s) ; ligne(s) {lig}")

    contenu = "\n".join(out) + "\n"
    with open(ps, "x", encoding="utf-8") as f:
        f.write(contenu)
    sys.stdout.write(contenu)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
