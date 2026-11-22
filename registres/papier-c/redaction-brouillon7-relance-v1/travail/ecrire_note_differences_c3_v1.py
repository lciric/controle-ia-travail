"""Écrit la note des différences entre les versions c2 et c3 du brouillon 7 de relance, depuis le journal du
programme de construction. Usage (racine du dépôt) : python3 <ce fichier>. Refuse d'écraser (R12)."""
import csv
import hashlib
import sys
from pathlib import Path

D = Path("registres/papier-c/redaction-brouillon7-relance-v1")
S = Path("brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c2.md")
T = Path("brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c3.md")
J = D / "travail/construire_brouillon7_relance_c3_v1.journal.tsv"
P = D / "travail/construire_brouillon7_relance_c3_v1.py"
SORTIE = D / "note-differences-brouillon7-relance-c3-v1.md"
if SORTIE.exists():
    sys.exit(f"refus d'écraser {SORTIE} (R12)")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
espace = lambda n: f"{n:,}".replace(",", " ")
lignes = lambda p: len(Path(p).read_text(encoding="utf-8").splitlines())
rows = list(csv.reader(J.open(encoding="utf-8"), delimiter="\t"))[1:]
o = []
o.append("# Papier C — note des différences entre les versions c2 et c3 du brouillon 7 de relance — v1\n")
o.append("Date : 2026-11-22. Auteur : rédacteur du brouillon 7 de relance (session fille `session_013QMayk1rjSZrn2u9UAVhEp`).\nClasse C.\n")
o.append(f"- Source : version c2, `{S}`\n  (`{sha(S)}`, {espace(S.stat().st_size)} octets,\n  {espace(lignes(S))} lignes).")
o.append(f"- Résultat : version c3, `{T}`\n  (`{sha(T)}`, {espace(T.stat().st_size)} octets,\n  {espace(lignes(T))} lignes).")
o.append(f"- Programme : `{P}`\n  (`{sha(P)}`) ; journal :\n  `{J}`\n  (`{sha(J)}`).")
o.append(f"- Méthode : {len(rows)} remplacements exacts (un fragment trouvé une fois, ou un bloc dont le début est trouvé une fois\n"
         "  et la fin une fois après lui). Gardes de sortie : titres de section inchangés ; un seul « À REMPLIR » dans la\n"
         "  section « Contre-lecture », aucun ajouté ni retiré ailleurs ; marqueurs de gabarit inchangés.")
o.append("- Source : la vérification de la version c2 (rapport `52b9ce5f…`, remarques CW-01 à CW-03) ; table :\n"
         f"  `{D}/table-traitement-verification-c2-brouillon7-relance-v1.md`.\n")
o.append("## 1. Ce qui ne change pas\n")
o.append("Les énoncés, les prédictions, les marges, les seuils, la règle de HC2, les décisions D-1 à D-20, les précisions 1 à\n"
         "40 (la précision 38 ne reçoit qu'une phrase sur la source de la lettre qu'elle suit : sa règle est inchangée),\n"
         "l'audit de symétrie, les gardes 1 et 3 à 23.\n")
o.append("## 2. Ce qui change dans une règle écrite\n")
o.append("- Plan, section 3 : le cadre du bras « saboteur sans consigne » est écrit, le complément ne fixant que ce qui\n"
         "  dépend du verdict de G0 (L-10) ; « Préalables » de l'étape 2 : le complément y est nommé (L-09).")
o.append("- Garde 24 : « l'étape 2 ne s'ouvre pas ; nœud » (L-13) ; garde 2 : renvoi à la garde 24 (L-12).\n")
o.append("## 3. Table des remplacements\n")
o.append("| identifiant | lieu | remarque ou motif | forme | signes retirés | signes écrits |")
o.append("|---|---|---|---|---|---|")
for r in rows:
    o.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} |")
o.append("\nLes empreintes de chaque fragment retiré et écrit sont au journal du programme.")
SORTIE.write_text("\n".join(o) + "\n", encoding="utf-8")
print(SORTIE, sha(SORTIE))
