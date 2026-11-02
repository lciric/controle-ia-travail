"""Assemble les faits courts du collisionneur N12-N13 (question v2 de conv-audit, `9faee0aa…`), forme (a) du devis
`docs/notes/ideation-organisme-v1/course-2/devis-collisionneur-n12-n13-v1.md`. Usage : assembler-faits-n12-n13-v1.py PIECES SORTIE.
Règles : (1) aucun mémo, aucun avis de conv-audit, aucune annexe du tour 2 ; (2) toute ligne portant une recommandation, une
confiance d'auteur ou un défaut sous 48 heures est remplacée par une marque de retrait ; (3) chaque pièce est servie entière,
entre balises, avec son origine (branche, commit) et son empreinte ; (4) aucune donnée de `donnees/`, aucune clé, aucun contenu
d'attaque (balayage à part). Pièces lues sur disque (copies vérifiées des branches `main` et `canal/conv-audit-n04`)."""
import hashlib, sys
from pathlib import Path
PIECES_DIR, SORTIE = Path(sys.argv[1]), Path(sys.argv[2])
MARQUE = "[retiré, règle 2 : recommandation, confiance d'auteur ou défaut]"
# (numéro, fichier, origine, nœuds, note, lignes à retirer (règle 2))
PIECES = [
 ("1", "decision-N-045-v2.md", "main, docs/decisions/", "N12, N13", "décision de Lazar, texte scellé", ()),
 ("2", "decision-N-058-v1.md", "main, docs/decisions/", "N12, N13", "décision de Lazar, texte scellé", ()),
 ("3", "precollision-tour1-opus.md", "canal/conv-audit-n04, brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/preideation-interne-v1/", "N12", "pré-collision d'Opus, tour 1 : la question la cite comme fait (« recommandait … pas en douze mois ») ; servie entière, sauf la ligne de confiance d'auteur (règle 2)", ("**Ordre proposé** (confiance",)),
 ("4", "lecture-verifiee-avalon-m1-v1.md", "canal/conv-audit-n04, docs/notes/rlcr-v1/", "N13", "lecture vérifiée sur PDF (Opus neuf) ; § 2.5 : recommandation et défaut retirés (règle 2), options gardées", ("- **Recommandation**", "- **Défaut sous 48 heures**")),
 ("5", "lecture-verifiee-damani-rlcr-v1.md", "canal/conv-audit-n04, docs/notes/rlcr-v1/", "N13", "lecture vérifiée sur PDF (Sonnet neuf)", ()),
 ("6", "provenance-rlcr-v2.md", "canal/conv-audit-n04, docs/sources/pdf/rlcr-v1/", "N13", "provenance des deux PDF (empreintes)", ()),
]
def emp(p): return hashlib.sha256(p.read_bytes()).hexdigest()
out = ["# Faits — collisionneur N12-N13 (couches 3 et 4 de l'organisme ; récompense collective) — v1", "",
       "Assemblés par session-depot (instance 3) le 31 octobre 2026 pour la question v2 de conv-audit "
       "(`question-collisionneur-n12-n13-couches-recompense-v2.md`, sha256 `9faee0aadf01…` recalculée à l'assemblage), "
       "forme (a) « faits courts » du devis `devis-collisionneur-n12-n13-v1.md`. Les deux PDF (Avalon-M1, Damani) ne sont "
       "pas servis : les lectures vérifiées (pages citées) en tiennent lieu ; toute affirmation sur les PDF hors de ces lectures "
       "est SUPPOSÉ.", "",
       "Règles appliquées : (1) ni mémo, ni avis de conv-audit, ni annexe du tour 2 ; (2) toute ligne portant une recommandation, "
       f"une confiance d'auteur ou un défaut est remplacée par « {MARQUE} » ; (3) pièces entières entre balises, origine et "
       "empreinte données ; (4) balayage à part (`balayage-faits-n12-n13-v1.txt`).", ""]
total, table = 0, ["| Pièce | Fichier | Origine | Nœuds | SHA-256 | Mots |", "|---|---|---|---|---|---|"]
corps = []
for num, f, orig, noeuds, note, retirer in PIECES:
    p = PIECES_DIR / f
    texte = p.read_text(encoding="utf-8")
    lignes = texte.split("\n")
    n_ret = 0
    for i, l in enumerate(lignes):
        if any(l.startswith(r) for r in retirer):
            lignes[i] = MARQUE; n_ret += 1
    assert n_ret == len(retirer), (f, n_ret)
    mots = sum(len(l.split()) for l in lignes); total += mots
    table.append(f"| {num} | `{f}` | {orig} | {noeuds} | `{emp(p)}` | {mots} |")
    corps += [f"### Pièce {num} — `{f}` (entier) — nœuds {noeuds}", "",
              f"Origine : {orig} ; empreinte du fichier source `{emp(p)}` ; {mots} mots ; {note} ; lignes retirées (règle 2) : {n_ret}.", "",
              f"<<<DÉBUT PIÈCE {num}>>>", *lignes, f"<<<FIN PIÈCE {num}>>>", ""]
out += table + ["", f"Total : {total} mots dans les pièces.", ""] + corps
SORTIE.write_text("\n".join(out), encoding="utf-8")
print(f"{SORTIE} : {total} mots, {len(PIECES)} pièces")
