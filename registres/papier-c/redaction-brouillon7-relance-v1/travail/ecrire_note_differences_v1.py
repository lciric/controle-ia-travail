"""Écrit la note des différences entre la version r3 et le brouillon 7 de relance, depuis le journal du programme de
construction. Usage (racine du dépôt) : python3 <ce fichier>. Refuse d'écraser (R12)."""
import csv
import hashlib
import sys
from pathlib import Path

D = Path("registres/papier-c/redaction-brouillon7-relance-v1")
T = Path("brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22.md")
J = D / "travail/construire_brouillon7_relance_v1.journal.tsv"
P = D / "travail/construire_brouillon7_relance_v1.py"
SORTIE = D / "note-differences-r3-brouillon7-relance-v1.md"
if SORTIE.exists():
    sys.exit(f"refus d'écraser {SORTIE} (R12)")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
espace = lambda n: f"{n:,}".replace(",", " ")
rows = list(csv.reader(J.open(encoding="utf-8"), delimiter="\t"))[1:]
classes = {
    "état et forme (aucune règle)": ["T-01", "T-02", "T-03", "T-04", "T-05", "T-06", "T-07", "T-08", "T-09", "T-10",
                                     "T-11", "T-12", "T-13", "T-14", "T-15", "T-16", "T-17", "T-18", "T-19", "T-20",
                                     "T-21", "T-41"],
    "proposition D-21 (désignation des sondes)": ["T-25", "T-33", "T-36", "T-39"],
    "proposition D-22 (réserve 20, mention, parts de D₀)": ["T-22", "T-23", "T-24", "T-26", "T-27", "T-28", "T-29",
                                                            "T-30", "T-34", "T-35", "T-37", "T-38", "T-40"],
    "forme de la section 8 (commun à D-21 et D-22)": ["T-31", "T-32"],
}
de = {i: c for c, l in classes.items() for i in l}
assert sorted(de) == sorted(r[0] for r in rows)
texte = T.read_text(encoding="utf-8")
o = []
o.append("# Papier C — note des différences entre la version r3 et le brouillon 7 de relance du préenregistrement — v1\n")
o.append("Date : 2026-11-22. Auteur : rédacteur du brouillon 7 de relance (session fille `session_013QMayk1rjSZrn2u9UAVhEp`).\nClasse C.\n")
o.append(f"- Source : version r3, `{D}/source/papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r3.md`\n"
         "  (`160730b4c3980d8d96b0d05ed4041f011b5bf78a7d8dc7f927ee1ed0c2463cac`, 216 428 octets, 2 009 lignes).")
o.append(f"- Résultat : `{T}`\n  (`{sha(T)}`, {espace(T.stat().st_size)} octets,\n  {espace(len(texte.splitlines()))} lignes).")
o.append(f"- Programme : `{P}`\n  (`{sha(P)}`) ; journal :\n  `{J}`\n  (`{sha(J)}`).")
o.append(f"- Méthode : {len(rows)} remplacements exacts, appliqués dans l'ordre ; chaque fragment retiré se trouvait une fois\n"
         "  exactement ; le programme refuse d'écraser une sortie. Gardes de sortie : titres de section inchangés ; aucun\n"
         "  « À REMPLIR » ajouté ni retiré hors de la section « Contre-lecture » ; marqueurs de gabarit = ceux de r3, plus\n"
         "  `<<MOT_DU_DIRECTEUR_D21_D22>>`.\n")
o.append("## 1. Ce qui ne change pas\n")
o.append("Les énoncés de HC1, HC2, HC2b et HC3 ; les prédictions C-P1 à C-P6, leurs signes, leurs marges et leurs seuils ; la\n"
         "règle de HC2 (décision D-15) ; le bloc de la stabilité de rang et sa clause de repli ; les 37 précisions de la\n"
         "section 8 ; l'audit de symétrie ; toutes les gardes de la liste d'arrêt sauf les gardes 15 et 20, complétées ; les\n"
         "vingt décisions D-1 à D-20 ; les champs du scellement. Aucune revendication n'est ajoutée ; aucun chiffre de l'état\n"
         "de l'art n'est ajouté (les seules citations neuves sont deux phrases du brief v2, T0.7 et critère 3 de la porte G0,\n"
         "et des phrases de décisions du dépôt).\n")
o.append("## 2. Ce qui change, en quatre groupes\n")
for c, l in classes.items():
    o.append(f"- **{c}** : {', '.join(l)}.")
o.append("\nT-33 et T-36 portent aussi la précision 39, qui relève de D-22. Une incohérence de la version r3 est corrigée au\n"
         "passage (T-26) : le plan comptait « une lecture forcée par contenu SP_m et SU », alors que le point 14 de la\n"
         "« Métrique » en écrit trois (L-SP, L-HP, L-H). Seul le compte du devis en dépend.\n")
o.append("## 3. Table des remplacements\n")
o.append("| identifiant | lieu | source ou motif | groupe | signes retirés | signes écrits |")
o.append("|---|---|---|---|---|---|")
for r in rows:
    o.append(f"| {r[0]} | {r[1]} | {r[2]} | {de[r[0]]} | {r[3]} | {r[4]} |")
o.append("\nLes empreintes de chaque fragment retiré et écrit sont au journal du programme.\n")
o.append("## 4. Ce que je n'ai pas fait\n")
o.append("- Je n'ai pas vérifié que la version r3 porte bien les corrections de CR-01 à CR-10 : c'est le travail du\n"
         "  contre-lecteur (consigne, point 3). En lisant r3 en entier, je n'ai relevé qu'une incohérence (T-26).")
o.append("- Je n'ai rejoué aucune simulation ; les taux simulés que le texte cite restent ceux des pièces du 19 novembre et\n"
         "  de la session 16.")
o.append("- Je n'ai rouvert aucun PDF de l'état de l'art : les chiffres et les pages cités sont ceux de la version r3, repris\n"
         "  des rapports de lecteurs (R7 : contrôle par échantillon demandé au contre-lecteur, consigne, point 6).")
o.append("- Je n'ai pas raccourci l'en-tête (près de 500 lignes d'historique et de verrous) : le déplacer dans une note à\n"
         "  part demanderait une version dont le différentiel ne serait plus lisible ; à faire, si la conduite le veut, au\n"
         "  moment du scellement, par un programme qui prouve que les sections normatives restent égales à l'octet.")
SORTIE.write_text("\n".join(o) + "\n", encoding="utf-8")
print(SORTIE, sha(SORTIE))
