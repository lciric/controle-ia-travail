"""Epreuve independante de la garde de table du module v3 (`table_des_criteres`, `exiger_table_des_criteres`).

Chaque cas part du candidat 1 (texte qui fait foi), change une seule chose par remplacement exact (ancre trouvee une
seule fois), et compare la decision du module a la decision attendue, ecrite ici avant le lancement :
- « passe » : la table de la section, lue en entier, egale `LIGNES` (cas sains) ;
- « refus » : decisions VM2-contournement-02, -03 et VM2-fidelite-01 (rangee en plus, en moins, hors de la forme
  « | Lk | », section en double) et ce qui en decoule (seconde table dans la section) ;
- « hors » : la table de la section est egale, mais le texte montre a un lecteur une seconde section ou une seconde
  table de meme titre hors de la section lue (titre d'apparence identique, autre niveau de titre, table HTML) ; la
  decision ne tranche pas : on rapporte ce que fait le module.
Le validateur gele (`controle_ia.prereg.problemes`) est lance sur chaque texte (fichier temporaire, sous le dossier passe
en argument). Lecture recodee independante (sans le module) pour le cas sain. N'ecrit que le JSON de sortie et les
fichiers temporaires.

Usage : python -B eprouver_garde_table_v3_v1.py COPIE_V3 CANDIDAT1 DOSSIER_TMP SORTIE_JSON
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import hashlib  # noqa: E402
import json  # noqa: E402
import unicodedata  # noqa: E402
from pathlib import Path  # noqa: E402

COPIE, CAND, TMP, SORTIE = (Path(x) for x in sys.argv[1:5])
sys.path.insert(0, str(COPIE))
import lecture_p4_v1 as lp  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.prereg import problemes  # noqa: E402

TEXTE = CAND.read_text(encoding="utf-8")
TITRE = "## Critères de lecture gelés\n"
ENTETE = "| ligne | issue | lecture |\n|---|---|---|\n"
L11 = next(x for x in TEXTE.split("\n") if x.startswith("| L11 |"))
L7 = next(x for x in TEXTE.split("\n") if x.startswith("| L7 |"))
L4 = next(x for x in TEXTE.split("\n") if x.startswith("| L4 |"))
L3 = next(x for x in TEXTE.split("\n") if x.startswith("| L3 |"))
L5 = next(x for x in TEXTE.split("\n") if x.startswith("| L5 |"))
L6 = next(x for x in TEXTE.split("\n") if x.startswith("| L6 |"))
L10 = next(x for x in TEXTE.split("\n") if x.startswith("| L10 |"))
RESERVES = "Réserves (toujours écrites à part, avec la ligne) :"
PRECISIONS = "## Précisions d'application"
LISTE = "## Liste d'arrêt\n"
AJOUT = "| ligne ajoutée | non lu ; nœud |"


def une(t: str, a: str, b: str) -> str:
    n = t.count(a)
    if n != 1:
        raise SystemExit(f"ancre trouvée {n} fois : {a[:80]!r}")
    return t.replace(a, b)


def table_autre() -> str:
    """Table de la forme du texte, L1 changée (une seule cellule)."""
    lignes = ["| ligne | issue | lecture |", "|---|---|---|"]
    for k, (i, t) in lp.LIGNES.items():
        e = lambda x: x.replace("|", "\\|")  # noqa: E731
        lignes.append(f"| {k} | {e(i)} | {e(t)} |" if k != "L1" else f"| L1 | autre issue | {e(t)} |")
    return "\n".join(lignes)


def section_autre(titre_ligne: str) -> str:
    return f"{titre_ligne}\n\n{table_autre()}\n\n"


CAS = []


def cas(nom, attendu, texte):
    CAS.append((nom, attendu, texte))


# ---- sains
cas("S0 candidat 1 tel quel", "passe", TEXTE)
cas("S1 fins de ligne CRLF", "passe", TEXTE.replace("\n", "\r\n"))
cas("S2 espaces de fin sur les lignes de la table", "passe",
    "\n".join(x + "  " if x.startswith("|") else x for x in TEXTE.split("\n")))
cas("S3 commentaire HTML sans barre sous la table, après une ligne vide", "passe",
    une(TEXTE, f"{L11}\n\n", f"{L11}\n\n<!-- note sans barre -->\n\n"))
# ---- vérification de fidélité du v2 : six cas qui passaient à tort
cas("F1 « | L4bis | » après L4", "refus", une(TEXTE, f"{L4}\n", f"{L4}\n| L4bis {AJOUT}\n"))
cas("F2 « | L3b | » entre L3 et L4", "refus", une(TEXTE, f"{L3}\n", f"{L3}\n| L3b {AJOUT}\n"))
cas("F3 « | **L12** | » en plus", "refus", une(TEXTE, f"{L11}\n", f"{L11}\n| **L12** {AJOUT}\n"))
cas("F4 « | M1 | » en plus", "refus", une(TEXTE, f"{L11}\n", f"{L11}\n| M1 {AJOUT}\n"))
cas("F5 « L12 | … | » sans barre initiale", "refus", une(TEXTE, f"{L11}\n", f"{L11}\nL12 {AJOUT}\n"))
cas("F6 section en double, la première changée", "refus", une(TEXTE, TITRE, section_autre(TITRE.rstrip("\n")) + TITRE))
# ---- vérification de contournement du v2 : formes restantes
cas("C3 « | L6bis | »", "refus", une(TEXTE, f"{L6}\n", f"{L6}\n| L6bis {AJOUT}\n"))
cas("C4 « | L 12 | »", "refus", une(TEXTE, f"{L11}\n", f"{L11}\n| L 12 {AJOUT}\n"))
cas("C5 « | l12 | »", "refus", une(TEXTE, f"{L11}\n", f"{L11}\n| l12 {AJOUT}\n"))
cas("D1 section en double, la seconde changée", "refus", une(TEXTE, f"\n{PRECISIONS}", "\n" + section_autre(TITRE.rstrip("\n")) + PRECISIONS))
cas("D2 section en double, identiques", "refus",
    une(TEXTE, f"\n{PRECISIONS}", "\n" + TITRE + "\n" + "\n".join(["| ligne | issue | lecture |", "|---|---|---|"]
        + [x for x in TEXTE.split("\n") if x.startswith("| L")]) + "\n\n" + PRECISIONS))
# ---- neufs (même section)
cas("N1 rangée L12 sans barre finale", "refus", une(TEXTE, f"{L11}\n", f"{L11}\n| L12 | ligne ajoutée | non lu ; nœud\n"))
cas("N2 rangée L12 à quatre cellules", "refus", une(TEXTE, f"{L11}\n", f"{L11}\n| L12 | a | b | c |\n"))
cas("N3 ligne vide puis « | L12 | » (paragraphe à barres)", "refus", une(TEXTE, f"{L11}\n\n", f"{L11}\n\n| L12 {AJOUT}\n\n"))
cas("N4 seconde table après le paragraphe des réserves", "refus",
    une(TEXTE, f"\n{PRECISIONS}", f"\n| ligne | issue | lecture |\n|---|---|---|\n| L12 {AJOUT}\n\n{PRECISIONS}"))
cas("N5 table dans un bloc de code après les réserves", "refus",
    une(TEXTE, f"\n{PRECISIONS}", f"\n```\n| L12 {AJOUT}\n```\n\n{PRECISIONS}"))
cas("N6 rangée L12 en retrait de quatre espaces", "refus", une(TEXTE, f"{L11}\n", f"{L11}\n    | L12 {AJOUT}\n"))
cas("N7 rangée « | L１２ | » (chiffres pleine chasse)", "refus", une(TEXTE, f"{L11}\n", f"{L11}\n| L１２ {AJOUT}\n"))
cas("N8 rangée « | L1\\u200b2 | » (espace sans chasse)", "refus", une(TEXTE, f"{L11}\n", f"{L11}\n| L1​2 {AJOUT}\n"))
cas("N9 rangée L5 en double", "refus", une(TEXTE, f"{L5}\n", f"{L5}\n{L5}\n"))
cas("N10 L10 et L11 échangées", "refus", une(TEXTE, f"{L10}\n{L11}\n", f"{L11}\n{L10}\n"))
cas("N11 ligne vide entre L5 et L6", "refus", une(TEXTE, f"{L5}\n{L6}\n", f"{L5}\n\n{L6}\n"))
cas("N12 commentaire HTML à barres après la table", "refus", une(TEXTE, f"{L11}\n\n", f"{L11}\n\n<!-- | L12 {AJOUT} -->\n\n"))
cas("N13 espace insécable dans une cellule de L7", "refus", une(TEXTE, f"{L7}\n", L7.replace(" ; M6b", " ; M6b", 1) + "\n"))
cas("N14 en-tête autre", "refus", une(TEXTE, ENTETE, "| ligne | issue | lecture lue |\n|---|---|---|\n"))
cas("N15 séparateur absent", "refus", une(TEXTE, ENTETE, "| ligne | issue | lecture |\n"))
cas("N16 ligne de texte collée sous la table", "refus", une(TEXTE, f"{L11}\n", f"{L11}\nRéserve collée.\n"))
# ---- hors de la section lue : titre d'apparence identique, autre niveau, table HTML
cas("H1 seconde section, titre + espace sans chasse (U+200B), table autre, avant la vraie", "hors",
    une(TEXTE, TITRE, section_autre("## Critères de lecture gelés​") + TITRE))
cas("H2 seconde section, titre avec espace insécable, table autre, après la vraie", "hors",
    une(TEXTE, f"\n{PRECISIONS}", "\n" + section_autre("## Critères de lecture gelés") + PRECISIONS))
cas("H3 seconde section, titre décomposé (NFD), table autre, après la vraie", "hors",
    une(TEXTE, f"\n{PRECISIONS}", "\n" + section_autre(unicodedata.normalize("NFD", "## Critères de lecture gelés")) + PRECISIONS))
cas("H4 titre de niveau 1 « # Critères de lecture gelés » et table autre, dans une autre section", "hors",
    une(TEXTE, f"\n{LISTE}", "\n" + section_autre("# Critères de lecture gelés") + LISTE))
cas("H5 titre de niveau 3 et table autre, dans une autre section", "hors",
    une(TEXTE, f"\n{LISTE}", "\n" + section_autre("### Critères de lecture gelés") + LISTE))
cas("H6 titre souligné (setext, niveau 2) et table autre, dans une autre section", "hors",
    une(TEXTE, f"\n{LISTE}", "\nCritères de lecture gelés\n---\n\n" + table_autre() + "\n\n" + LISTE))
cas("H7 table HTML (rangée L12) dans la section, après les réserves", "hors",
    une(TEXTE, f"\n{PRECISIONS}", "\n<table><tr><th>ligne</th><th>issue</th><th>lecture</th></tr>"
        "<tr><td>L12</td><td>ligne ajoutée</td><td>non lu ; nœud</td></tr></table>\n\n" + PRECISIONS))
cas("H8 section « Critères de lecture gelés (suite) » avec une rangée L12", "hors",
    une(TEXTE, f"\n{PRECISIONS}", "\n## Critères de lecture gelés (suite)\n\n| ligne | issue | lecture |\n|---|---|---|\n"
        f"| L12 {AJOUT}\n\n" + PRECISIONS))
cas("H9 titre « ## Critères de lecture gelés » dans un bloc de code d'une autre section", "hors",
    une(TEXTE, f"\n{LISTE}", "\n```\n## Critères de lecture gelés\n```\n\n" + LISTE))


def lecture_independante(texte: str) -> dict:
    """Lecture recodée sans le module : section du titre exact au titre de niveau 2 suivant ; lignes « | Lk | » ;
    « \\| » protégé ; trois cellules."""
    lignes = texte.split("\n")
    d = lignes.index("## Critères de lecture gelés")
    f = next(k for k in range(d + 1, len(lignes)) if lignes[k].startswith("## "))
    t = {}
    for x in lignes[d + 1:f]:
        if x.startswith("| L"):
            c = [y.strip().replace("\x00", "|") for y in x.replace("\\|", "\x00").split("|")[1:-1]]
            assert len(c) == 3 and c[0] not in t
            t[c[0]] = (c[1], c[2])
    return t


resultats = []
TMP.mkdir(parents=True, exist_ok=True)
for k, (nom, attendu, texte) in enumerate(CAS):
    try:
        r = lp.exiger_table_des_criteres(texte)
        obtenu, motif = "passe", f"cellules égales : {r['cellules_egales']}"
    except GardeArret as e:
        obtenu, motif = "refus", str(e)[:220]
    p = TMP / f"texte-{k:02d}.md"
    p.write_text(texte, encoding="utf-8")
    pb = problemes(p)
    conforme = (obtenu == attendu) if attendu != "hors" else None
    resultats.append({"cas": nom, "attendu": attendu, "obtenu": obtenu, "conforme": conforme, "motif": motif,
                      "validateur": pb, "sha256_texte": hashlib.sha256(texte.encode("utf-8")).hexdigest()})

ind = lecture_independante(TEXTE)
sortie = {
    "candidat1_sha256": hashlib.sha256(CAND.read_bytes()).hexdigest(),
    "lecture_independante": {"lignes": list(ind), "egales_a_LIGNES": ind == lp.LIGNES,
                             "cellules_egales": sum(ind[k][j] == lp.LIGNES[k][j] for k in lp.LIGNES for j in (0, 1))},
    "cas": resultats,
    "bilan": {"sains_et_refus_conformes": sum(1 for r in resultats if r["conforme"] is True),
              "non_conformes": [r["cas"] for r in resultats if r["conforme"] is False],
              "hors_qui_passent": [r["cas"] for r in resultats if r["attendu"] == "hors" and r["obtenu"] == "passe"],
              "hors_refuses": [r["cas"] for r in resultats if r["attendu"] == "hors" and r["obtenu"] == "refus"]},
}
SORTIE.write_text(json.dumps(sortie, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(sortie["lecture_independante"], ensure_ascii=False))
print(json.dumps(sortie["bilan"], ensure_ascii=False, indent=1))
for r in resultats:
    print(f"{r['obtenu']:5} | attendu {r['attendu']:5} | {r['cas']} | {r['motif'][:110]} | validateur : {r['validateur']}")
