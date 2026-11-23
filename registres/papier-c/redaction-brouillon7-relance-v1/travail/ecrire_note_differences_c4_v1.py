"""Écrit la note des différences entre les versions c3 et c4 du brouillon 7 de relance, depuis le journal du
programme de construction. Usage (racine du dépôt) : python3 <ce fichier>. Refuse d'écraser (R12)."""
import csv
import hashlib
import sys
from pathlib import Path

D = Path("registres/papier-c/redaction-brouillon7-relance-v1")
S = Path("brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c3.md")
T = Path("brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c4.md")
J = D / "travail/construire_brouillon7_relance_c4_v1.journal.tsv"
P = D / "travail/construire_brouillon7_relance_c4_v1.py"
SORTIE = D / "note-differences-brouillon7-relance-c4-v1.md"
if SORTIE.exists():
    sys.exit(f"refus d'écraser {SORTIE} (R12)")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
espace = lambda n: f"{n:,}".replace(",", " ")
lignes = lambda p: len(Path(p).read_text(encoding="utf-8").splitlines())
rows = list(csv.reader(J.open(encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))[1:]
o = []
o.append("# Papier C — note des différences entre les versions c3 et c4 du brouillon 7 de relance — v1\n")
o.append("Date : 2026-11-22. Auteur : rédacteur du brouillon 7 de relance (session fille `session_013QMayk1rjSZrn2u9UAVhEp`).\nClasse C.\n")
o.append(f"- Source : version c3, `{S}`\n  (`{sha(S)}`, {espace(S.stat().st_size)} octets,\n  {espace(lignes(S))} lignes).")
o.append(f"- Résultat : version c4, `{T}`\n  (`{sha(T)}`, {espace(T.stat().st_size)} octets,\n  {espace(lignes(T))} lignes).")
o.append(f"- Programme : `{P}`\n  (`{sha(P)}`) ; journal :\n  `{J}`\n  (`{sha(J)}`).")
o.append(f"- Méthode : {len(rows)} remplacements exacts (chaque fragment trouvé une fois). Gardes de sortie : titres de section\n"
         "  inchangés ; un seul « À REMPLIR » dans la section « Contre-lecture », aucun ajouté ni retiré ailleurs ;\n"
         "  marqueurs de gabarit inchangés.")
o.append("- Source : la vérification de la version c3 (rapport `265f62e7…`, remarques CX-01 et CX-02) ; table :\n"
         f"  `{D}/table-traitement-verification-c3-brouillon7-relance-v1.md`.\n")
o.append("## 1. Ce qui ne change pas\n")
o.append("Les énoncés, les prédictions, les marges, les seuils, la règle de HC2, les décisions D-1 à D-20, les précisions 1 à\n"
         "40, les réserves 1 à 20, l'audit de symétrie, les critères de lecture, les gardes 1 à 24.\n")
o.append("## 2. Ce qui change dans une règle écrite\n")
o.append("Un seul lieu : Plan, section 3, bras « saboteur sans consigne ».\n"
         "- Cadre (M-10) : les cellules honnêtes ne sont plus figées ; le cadre fige le même contexte des deux côtés du\n"
         "  bras, consigne privée comprise ; le compte d'épisodes dépend du contexte sous lequel l'organisme se lit ; les\n"
         "  lignes du bras ne confirment ni ne réfutent rien au titre du présent texte.\n"
         "- Ce que fixe le complément (M-11) : le contexte commun, donc les cellules honnêtes ; ce qu'il fait de la\n"
         "  différence de modèle qui reste (ajout du rédacteur, hors remarque) ; des critères de lecture propres, s'il en\n"
         "  donne, dont l'issue ne remplace jamais une ligne du présent texte.\n")
o.append("## 3. Table des remplacements\n")
o.append("| identifiant | lieu | remarque ou motif | signes retirés | signes écrits |")
o.append("|---|---|---|---|---|")
for r in rows:
    o.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |")
o.append("\nLes empreintes de chaque fragment retiré et écrit sont au journal du programme.")
SORTIE.write_text("\n".join(o) + "\n", encoding="utf-8")
print(SORTIE, sha(SORTIE))
