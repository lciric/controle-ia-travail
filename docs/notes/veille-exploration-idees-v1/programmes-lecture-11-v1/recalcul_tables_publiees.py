"""Lecture 11 de la veille sur l'exploration d'idees (v1) -- recalcul sur les tables publiees.

Source lue : le paquet de sources d'arXiv 2609.35875v1 (tables TeX par modele), lu en memoire,
jamais extrait sur disque ni execute. A lancer avec `python3 -I` :

    python3 -I recalcul_tables_publiees.py CHEMIN/arxiv-2609.35875v1-source.tar.gz

Ce que le programme fait, et rien d'autre :
  1. relit les quatre tables par modele (arithmetique, GSM8K, MMLU, CommonsenseQA) et verifie que
     leurs moyennes redonnent la table 1 du papier ;
  2. reconstruit les paliers de capacite par la regle ecrite en annexe I du papier (moyenne de la
     precision d'un agent seul sur GSM8K, MMLU et CommonsenseQA : fort >= 85, moyen 60 a 85,
     faible < 60), sur les 19 modeles du vivier des equipes mixtes (table 3 : les quatre modeles
     ajoutes apres le gel en sont exclus) ;
  3. compare, par palier, le vote de neuf tirages d'UN SEUL modele (colonne « SC-9 » des tables par
     modele) au vote de neuf tirages d'une equipe de TROIS modeles differents du meme palier
     (table 12 du papier, lignes SSS, MMM, WWW), que le papier ne met jamais cote a cote.

Reserves, ecrites aussi dans la sortie : la comparaison 3 n'est pas appariee ; l'appartenance aux
paliers est reconstruite par moi (le papier ne la liste pas) ; les valeurs par modele sont
arrondies a l'unite (100 problemes) ; les politiques de temperature different (etalement 0,5 a 1,0
pour le vote d'un seul modele de la table 1, temperature 1,0 pour les ensembles d'equipe ; le
papier borne cet ecart a 0,4 point en valeur absolue, page 6).
Graine : aucune, le calcul est deterministe.
"""
import hashlib
import re
import sys
import tarfile

TACHES = {
    "arithmetique": "tables/table_a1_math.tex",
    "GSM8K": "tables/table_a1_gsm.tex",
    "MMLU": "tables/table_a1_mmlu.tex",
    "CommonsenseQA": "tables/table_a1_csqa.tex",
}
COLONNES = ["seul", "debat", "vote9", "personas"]
# Table 1 du papier (page 5) : moyennes sur les 23 modeles.
TABLE_1 = {
    "arithmetique": [91.2, 91.5, 90.6, 90.0],
    "GSM8K": [87.9, 91.2, 91.0, 88.5],
    "MMLU": [69.9, 76.5, 76.8, 75.2],
    "CommonsenseQA": [72.6, 78.3, 80.6, 73.9],
}
# Table 3 du papier (page 12) : quatre modeles ajoutes apres le gel du tirage des equipes mixtes.
AJOUTES_APRES_GEL = [
    "R1-Distill-Qwen-14B",
    "gemma-4-26B-A4B-it-FP8-dy",
    "R1-Distill-Qwen-32B-w4a16",
    "Qwen3.5-35B-A3B (GPTQ)",
]
# Table 12 du papier (page 17) : equipes de trois modeles differents, par composition de paliers.
TABLE_12 = {"SSS": (93.7, 93.2), "MMM": (87.0, 88.2), "WWW": (75.6, 76.7)}


def lire_table(texte):
    lignes = {}
    for ligne in texte.split("\n"):
        if "&" not in ligne or ligne.strip().startswith("Model"):
            continue
        cellules = [c.strip() for c in ligne.replace("\\\\", "").split("&")]
        nom = cellules[0]
        valeurs = []
        for c in cellules[1:]:
            m = re.search(r"-?\d+(?:\.\d+)?", c.replace("\\textbf{", ""))
            valeurs.append(float(m.group(0)))
        if len(valeurs) != 4:
            raise SystemExit("ligne inattendue : %r" % ligne)
        lignes[nom] = valeurs
    return lignes


def moyenne(xs):
    xs = list(xs)
    return sum(xs) / len(xs)


def main():
    chemin = sys.argv[1]
    with open(chemin, "rb") as f:
        empreinte = hashlib.sha256(f.read()).hexdigest()
    print("paquet de sources :", chemin.split("/")[-1])
    print("sha256            :", empreinte)
    archive = tarfile.open(chemin, "r:gz")
    tables = {}
    for tache, nom in TACHES.items():
        tables[tache] = lire_table(archive.extractfile(nom).read().decode("utf-8"))
    modeles = sorted(tables["GSM8K"])
    for tache in TACHES:
        if sorted(tables[tache]) != modeles:
            raise SystemExit("les tables n'ont pas les memes modeles")
    print("modeles lus       :", len(modeles))

    print("\n== 1. Les tables par modele redonnent-elles la table 1 ? (moyennes sur 23 modeles)")
    ecart_max = 0.0
    for tache in TACHES:
        calcule = [moyenne(tables[tache][m][k] for m in modeles) for k in range(4)]
        ecarts = [abs(a - b) for a, b in zip(calcule, TABLE_1[tache])]
        ecart_max = max(ecart_max, max(ecarts))
        print("  %-14s recalcule %s | papier %s" % (
            tache, " ".join("%5.2f" % v for v in calcule), " ".join("%5.1f" % v for v in TABLE_1[tache])))
    print("  ecart maximal en valeur absolue : %.3f point (arrondi a 0,1 attendu : 0,05)" % ecart_max)

    print("\n== 2. Debat (3 agents, 3 rondes) contre vote de neuf tirages du meme modele, par modele")
    for tache in TACHES:
        plus = sum(1 for m in modeles if tables[tache][m][1] > tables[tache][m][2])
        moins = sum(1 for m in modeles if tables[tache][m][1] < tables[tache][m][2])
        egal = len(modeles) - plus - moins
        print("  %-14s debat au-dessus : %2d ; egal : %2d ; debat au-dessous : %2d" % (tache, plus, egal, moins))

    print("\n== 3. Paliers reconstruits (regle de l'annexe I), vivier des 19 modeles des equipes mixtes")
    vivier = [m for m in modeles if m not in AJOUTES_APRES_GEL]
    if len(vivier) != 19:
        raise SystemExit("vivier inattendu : %d" % len(vivier))
    paliers = {"fort": [], "moyen": [], "faible": []}
    for m in vivier:
        seul = moyenne(tables[t][m][0] for t in ("GSM8K", "MMLU", "CommonsenseQA"))
        palier = "fort" if seul >= 85 else ("moyen" if seul >= 60 else "faible")
        vote9 = moyenne(tables[t][m][2] for t in TACHES)
        debat = moyenne(tables[t][m][1] for t in TACHES)
        seul4 = moyenne(tables[t][m][0] for t in TACHES)
        paliers[palier].append((m, seul, seul4, debat, vote9))
    for palier, code in (("fort", "SSS"), ("moyen", "MMM"), ("faible", "WWW")):
        membres = paliers[palier]
        print("  palier %s : %d modeles" % (palier, len(membres)))
        for m, seul, seul4, debat, vote9 in sorted(membres, key=lambda x: -x[4]):
            print("    %-36s seul (3 taches) %5.1f | sur 4 taches : seul %5.1f, debat %5.1f, vote de 9 %5.1f"
                  % (m, seul, seul4, debat, vote9))
        if not membres:
            continue
        moy_vote9 = moyenne(x[4] for x in membres)
        max_vote9 = max(x[4] for x in membres)
        moy_seul4 = moyenne(x[2] for x in membres)
        d, e = TABLE_12[code]
        print("    -> un seul modele, vote de 9, moyenne du palier : %.1f ; meilleur du palier : %.1f ; agent seul : %.1f"
              % (moy_vote9, max_vote9, moy_seul4))
        print("    -> papier, table 12, equipes %s de trois modeles differents : ensemble vote %.1f ; debat %.1f"
              % (code, e, d))
        print("    -> ecart ensemble mixte moins vote d'un seul modele (moyenne du palier) : %+.1f point" % (e - moy_vote9))

    print("\n== 4. Coherence interne : la table 12 (dix compositions, huit equipes chacune) redonne-t-elle")
    print("      la ligne « trois modeles » de la table 2 (80 equipes) ?")
    # Table 12 (page 17) : composition -> (debat, ensemble, ecart publie)
    table_12_complete = {
        "SSS": (93.7, 93.2, +0.44), "SSM": (92.5, 92.8, -0.28), "SMM": (90.3, 91.5, -1.22),
        "MMM": (87.0, 88.2, -1.16), "SSW": (91.7, 92.2, -0.59), "SMW": (90.6, 90.9, -0.31),
        "MMW": (84.9, 87.1, -2.19), "SWW": (87.4, 89.3, -1.91), "MWW": (80.8, 83.7, -2.87),
        "WWW": (75.6, 76.7, -1.13),
    }
    d12 = moyenne(v[0] for v in table_12_complete.values())
    e12 = moyenne(v[1] for v in table_12_complete.values())
    x12 = moyenne(v[2] for v in table_12_complete.values())
    print("  moyenne simple des dix compositions : debat %.2f ; ensemble %.2f ; ecart %.2f" % (d12, e12, x12))
    print("  table 2 (page 7), 80 equipes        : debat 88.4 ; ensemble 89.4 ; ecart -1.04")
    print("  difference                          : debat %+.2f ; ensemble %+.2f ; ecart %+.2f"
          % (d12 - 88.4, e12 - 89.4, x12 - (-1.04)))
    print("  (a effectifs egaux par composition, les deux devraient coincider a l'arrondi pres)")

    print("\n== 5. Nombre de lancements, somme de la table 4 (page 13), hors passes de jugement")
    lancements = [460, 345, 690, 190, 400, 150, 200, 400, 350, 200, 800, 170, 1150, 138, 93]
    print("  somme :", sum(lancements), "(le papier dit « 5,500+ ») ; passes de jugement : 2720")

    print("\nReserves : comparaison 3 non appariee (memes 100 problemes par tache, mais moyennes de")
    print("groupes differents) ; paliers reconstruits par le lecteur, et douteux pour le palier faible :")
    print("la regle n'y range que 4 modeles, soit 4 trios distincts, alors que le papier dit 8 equipes")
    print("par composition (les paliers du papier ont donc ete fixes sur d'autres chiffres, ou les")
    print("equipes se repetent) ; valeurs par modele arrondies a")
    print("l'unite ; temperatures differentes entre les deux bras (ecart borne a 0,4 point par le papier).")
    print("Ce calcul n'est pas un resultat du papier : c'est le bras que le papier ne rapporte pas.")


if __name__ == "__main__":
    main()
