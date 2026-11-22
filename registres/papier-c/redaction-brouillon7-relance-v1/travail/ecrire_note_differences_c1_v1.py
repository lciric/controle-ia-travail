"""Écrit la note des différences entre le brouillon 7 de relance et sa version c1, depuis le journal du programme de
construction. Usage (racine du dépôt) : python3 <ce fichier>. Refuse d'écraser (R12)."""
import csv
import hashlib
import sys
from pathlib import Path

D = Path("registres/papier-c/redaction-brouillon7-relance-v1")
S = Path("brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22.md")
T = Path("brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c1.md")
J = D / "travail/construire_brouillon7_relance_c1_v1.journal.tsv"
P = D / "travail/construire_brouillon7_relance_c1_v1.py"
SORTIE = D / "note-differences-brouillon7-relance-c1-v1.md"
if SORTIE.exists():
    sys.exit(f"refus d'écraser {SORTIE} (R12)")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
espace = lambda n: f"{n:,}".replace(",", " ")
lignes = lambda p: len(Path(p).read_text(encoding="utf-8").splitlines())
rows = list(csv.reader(J.open(encoding="utf-8"), delimiter="\t"))[1:]
o = []
o.append("# Papier C — note des différences entre le brouillon 7 de relance et sa version c1 — v1\n")
o.append("Date : 2026-11-22. Auteur : rédacteur du brouillon 7 de relance (session fille `session_013QMayk1rjSZrn2u9UAVhEp`).\nClasse C.\n")
o.append(f"- Source : brouillon 7 de relance, `{S}`\n  (`{sha(S)}`, {espace(S.stat().st_size)} octets,\n  {espace(lignes(S))} lignes).")
o.append(f"- Résultat : version c1, `{T}`\n  (`{sha(T)}`, {espace(T.stat().st_size)} octets,\n  {espace(lignes(T))} lignes).")
o.append(f"- Programme : `{P}`\n  (`{sha(P)}`) ; journal :\n  `{J}`\n  (`{sha(J)}`).")
o.append(f"- Méthode : {len(rows)} remplacements exacts, appliqués dans l'ordre : un fragment trouvé une fois, ou un bloc dont le\n"
         "  début est trouvé une fois et la fin une fois après lui. Gardes de sortie : titres de section inchangés ; aucun\n"
         "  « À REMPLIR » ajouté ni retiré hors de la section « Contre-lecture », un seul dans celle-ci ; marqueurs de\n"
         "  gabarit = ceux du brouillon 7 de relance, plus `<<MOT_DU_DIRECTEUR_H1>>` ; chaque précision de 1 à 40 nommée.")
o.append("- Motif de chaque remplacement : la remarque du contre-lecteur qu'il traite (rapport `30239c46…`), selon la table\n"
         f"  `{D}/table-traitement-contre-lecture-brouillon7-relance-v1.md`.\n")
o.append("## 1. Ce qui ne change pas\n")
o.append("Les énoncés de HC1, HC2, HC2b et HC3 ; les prédictions C-P1 à C-P6, leurs signes, leurs marges et leurs seuils ; la\n"
         "règle de HC2 ; les vingt décisions D-1 à D-20 ; les champs du scellement ; les précisions 1 à 35, mot pour mot ;\n"
         "l'audit de symétrie, sauf une phrase ajoutée à A9. Aucune revendication n'est ajoutée ; aucun chiffre de l'état\n"
         "de l'art n'est ajouté ; une citation héritée est ramenée à ce que sa page porte (C-21).\n")
o.append("## 2. Ce qui change dans une règle ou une ligne écrite\n")
o.append("- Condition de la version (a) de la clause de repli et issue 3 : « contre-lu » précisé (C-17, C-18), dans le sens\n"
         "  qui mène plus souvent à la version (b).")
o.append("- Précision 36 : une ligne rapportée de plus (C-30). Précision 37 : prémisse corrigée, déclarations, statut de\n"
         "  nœud (C-31, C-32). Précisions 38 et 39 réécrites, précision 40 neuve (C-33). Garde 15 complétée (C-40).")
o.append("- Mention de la réserve 20 étendue à la ligne de la porte GC et aux mentions de l'audit A9, et déplacée hors de la\n"
         "  colonne « non concluante » du tableau (C-27, C-34 à C-38). Elle ne change ni règle ni verdict.")
o.append("- Entrées de l'appel au harnais : une graine possible, selon la précision 40 (C-24, C-26).\n")
o.append("## 3. Table des remplacements\n")
o.append("| identifiant | lieu | remarque ou motif | forme | signes retirés | signes écrits |")
o.append("|---|---|---|---|---|---|")
for r in rows:
    o.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} |")
o.append("\nLes empreintes de chaque fragment retiré et écrit sont au journal du programme.\n")
o.append("## 4. Erratum à la note du brouillon 7 de relance (remarque CB-13)\n")
o.append("La note `note-differences-r3-brouillon7-relance-v1.md` (`9c9774a4…`) écrit, section 1, que « les 37 précisions de\n"
         "la section 8 » ne changent pas entre la version r3 et le brouillon 7 de relance. C'est inexact : les précisions\n"
         "20 et 36 y ont été allongées (remplacements T-34 et T-35 : les parts de la précision 39 ajoutées à leurs listes)\n"
         "et l'introduction de la section 8 changée (T-32). Les 35 autres sont inchangées, mot pour mot. La note v1 n'est\n"
         "pas réécrite (R12) ; cet erratum prime sur sa phrase.")
SORTIE.write_text("\n".join(o) + "\n", encoding="utf-8")
print(SORTIE, sha(SORTIE))
