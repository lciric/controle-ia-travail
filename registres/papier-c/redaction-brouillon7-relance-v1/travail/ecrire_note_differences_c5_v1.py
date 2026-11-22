"""Écrit la note des différences entre les versions c4 et c5 du brouillon 7 de relance, depuis le journal du
programme de construction. Usage (racine du dépôt) : python3 <ce fichier>. Refuse d'écraser (R12)."""
import csv
import hashlib
import sys
from pathlib import Path

D = Path("registres/papier-c/redaction-brouillon7-relance-v1")
S = Path("brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c4.md")
T = Path("brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c5.md")
J = D / "travail/construire_brouillon7_relance_c5_v1.journal.tsv"
P = D / "travail/construire_brouillon7_relance_c5_v1.py"
SORTIE = D / "note-differences-brouillon7-relance-c5-v1.md"
if SORTIE.exists():
    sys.exit(f"refus d'écraser {SORTIE} (R12)")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
espace = lambda n: f"{n:,}".replace(",", " ")
lignes = lambda p: len(Path(p).read_text(encoding="utf-8").splitlines())
rows = list(csv.reader(J.open(encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))[1:]
o = []
o.append("# Papier C — note des différences entre les versions c4 et c5 du brouillon 7 de relance — v1\n")
o.append("Date : 2026-11-22. Auteur : rédacteur du brouillon 7 de relance (session fille `session_013QMayk1rjSZrn2u9UAVhEp`).\nClasse C.\n")
o.append(f"- Source : version c4, `{S}`\n  (`{sha(S)}`, {espace(S.stat().st_size)} octets,\n  {espace(lignes(S))} lignes).")
o.append(f"- Résultat : version c5, `{T}`\n  (`{sha(T)}`, {espace(T.stat().st_size)} octets,\n  {espace(lignes(T))} lignes).")
o.append(f"- Programme : `{P}`\n  (`{sha(P)}`) ; journal :\n  `{J}`\n  (`{sha(J)}`).")
o.append(f"- Méthode : {len(rows)} remplacements exacts (chaque fragment trouvé une fois). Gardes de sortie : titres de section\n"
         "  inchangés ; un seul « À REMPLIR » dans la section « Contre-lecture », aucun ajouté ni retiré ailleurs ;\n"
         "  marqueurs de gabarit contrôlés (ligne suivante).")
o.append("- Gardes de marqueurs : ceux de la version c4 moins « MOT_DU_DIRECTEUR_H1 », et rien d'autre (seize restent).")
o.append("- Sources : la ligne GO-2026-11-22-125 de `registres/go.md` (décision de la chaîne sur le point H-1 ; R-5037 pour\n"
         "  les recommandations des deux juges) ; la vérification de la version c4 (rapport `c530b6df…`, remarque CY-01) et\n"
         f"  l'erratum 1 de la version c4 ; table : `{D}/table-traitement-verification-c4-et-devis-brouillon4-v1.md`.\n")
o.append("## 1. Ce qui ne change pas\n")
o.append("Les énoncés, les prédictions, les marges, les seuils, la règle de HC2, les décisions D-1 à D-24, les précisions 1 à\n"
         "35 et 38 à 40, les réserves 1 à 20, l'audit de symétrie, les règles et les verdicts des critères de lecture, les\n"
         "gardes 1 à 24, le bras « saboteur sans consigne ». La lecture de la précision 37 est gardée telle qu'écrite.\n")
o.append("## 2. Ce qui change dans une règle écrite\n")
o.append("- Précision 37, « Statut » (N-14) : le nœud H-1 est tranché par la chaîne de décision, non par le directeur, et\n"
         "  reste révisable par lui jusqu'au scellement ; le marqueur qui retenait le scellement disparaît (N-09, N-14).\n"
         "- Précision 37, fin, et précision 36 (N-14, N-13) : trois lignes rapportées de plus, sans verdict — nombre de\n"
         "  couples où ĉ n'est pas identifiable, écrit sur C-P3a et C-P3b ; mention « rangs sans gain mesuré : stabilité\n"
         "  non éprouvée » ; statistiques de rang sur le gain de la loi séparée. Phrase de renvoi sous le tableau des\n"
         "  critères (N-15). Ajouts du rédacteur sur recommandation des juges : à vérifier par le contre-lecteur.\n")
o.append("## 3. Table des remplacements\n")
o.append("| identifiant | lieu | remarque ou motif | signes retirés | signes écrits |")
o.append("|---|---|---|---|---|")
for r in rows:
    o.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |")
o.append("\nLes empreintes de chaque fragment retiré et écrit sont au journal du programme.")
SORTIE.write_text("\n".join(o) + "\n", encoding="utf-8")
print(SORTIE, sha(SORTIE))
