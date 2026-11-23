"""Écrit la note des différences entre les versions c1 et c2 du brouillon 7 de relance, depuis le journal du
programme de construction. Usage (racine du dépôt) : python3 <ce fichier>. Refuse d'écraser (R12)."""
import csv
import hashlib
import sys
from pathlib import Path

D = Path("registres/papier-c/redaction-brouillon7-relance-v1")
S = Path("brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c1.md")
T = Path("brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c2.md")
J = D / "travail/construire_brouillon7_relance_c2_v1.journal.tsv"
P = D / "travail/construire_brouillon7_relance_c2_v1.py"
SORTIE = D / "note-differences-brouillon7-relance-c2-v1.md"
if SORTIE.exists():
    sys.exit(f"refus d'écraser {SORTIE} (R12)")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
espace = lambda n: f"{n:,}".replace(",", " ")
lignes = lambda p: len(Path(p).read_text(encoding="utf-8").splitlines())
rows = list(csv.reader(J.open(encoding="utf-8"), delimiter="\t"))[1:]
o = []
o.append("# Papier C — note des différences entre les versions c1 et c2 du brouillon 7 de relance — v1\n")
o.append("Date : 2026-11-22. Auteur : rédacteur du brouillon 7 de relance (session fille `session_013QMayk1rjSZrn2u9UAVhEp`).\nClasse C.\n")
o.append(f"- Source : version c1, `{S}`\n  (`{sha(S)}`, {espace(S.stat().st_size)} octets,\n  {espace(lignes(S))} lignes).")
o.append(f"- Résultat : version c2, `{T}`\n  (`{sha(T)}`, {espace(T.stat().st_size)} octets,\n  {espace(lignes(T))} lignes).")
o.append(f"- Programme : `{P}`\n  (`{sha(P)}`) ; journal :\n  `{J}`\n  (`{sha(J)}`).")
o.append(f"- Méthode : {len(rows)} remplacements exacts, chaque fragment trouvé une fois. Gardes de sortie : titres de section\n"
         "  inchangés ; un seul « À REMPLIR » dans la section « Contre-lecture », aucun ajouté ni retiré ailleurs ;\n"
         "  marqueurs de gabarit inchangés, sauf `<<MOT_DU_DIRECTEUR_D21_D22>>`, qui devient `<<MOT_DU_DIRECTEUR_D22>>`.")
o.append("- Deux sources : la vérification de la version c1 (rapport `ba712818…`, remarques CV-01 à CV-03) et le mot du\n"
         f"  directeur (GO-2026-11-22-123 : D-21, D-23, D-24) ; table : `{D}/table-traitement-verification-c1-brouillon7-relance-v1.md`.\n")
o.append("## 1. Ce qui ne change pas\n")
o.append("Les énoncés, les prédictions, les marges, les seuils, la règle de HC2, les décisions D-1 à D-20, les précisions 1 à\n"
         "37 et 39 sauf un mot de renvoi dans celle-ci (K-20), l'audit de symétrie, les gardes 1 à 23.\n")
o.append("## 2. Ce qui change dans une règle écrite\n")
o.append("- Précision 38 : la règle de désignation suit la lettre de la décision D-21 (toute famille jugée pour ce mode, au\n"
         "  lieu de la seule famille (iv) en plus de (i) et (ii)) ; une famille « sans objet » n'impose rien (K-17 à K-19).")
o.append("- Précision 40 : les tirages d'une condition viennent d'un flux propre ; sinon sortie sous un motif nommé (K-21).")
o.append("- Plan, section 3 : paragraphe du bras « saboteur sans consigne » ; garde 24, neuve : nœud (K-14, K-22).\n")
o.append("## 3. Table des remplacements\n")
o.append("| identifiant | lieu | remarque, décision ou motif | signes retirés | signes écrits |")
o.append("|---|---|---|---|---|")
for r in rows:
    o.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |")
o.append("\nLes empreintes de chaque fragment retiré et écrit sont au journal du programme.")
SORTIE.write_text("\n".join(o) + "\n", encoding="utf-8")
print(SORTIE, sha(SORTIE))
