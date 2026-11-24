"""Réserve de questions témoins (règle 2 du protocole X v2) : questions à réponse connue, vérifiable hors du programme.

Deux sortes :
 - calcul refait par code (la réponse est calculée ici, à la précision dite) ;
 - fait publié lu sur un PDF du dépôt, à la page (pdftotext ; le passage attendu doit s'y trouver mot pour mot).
Aucune ne porte sur un résultat du programme ni sur une pièce cloisonnée.
Sorties : ../questions-temoins-v1.md (questions seules, servables) ;
          ../reponses-ne-pas-servir/reponses-questions-temoins-v1.md et .json (réponses, pièce séparée, à ne jamais servir).
Le script échoue si un passage attendu manque à la page dite.
"""
import json
import math
import subprocess
import sys
from math import comb
from pathlib import Path

from audit_commun_v2 import SORTIES

ICI = SORTIES.parent
PDF = Path("docs/sources/pdf")


def page(fichier, p):
    r = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-q", str(PDF / fichier), "-"],
                       capture_output=True, text=True)
    return " ".join(r.stdout.split())


def bh(pvals, q):
    m = len(pvals)
    s = sorted(pvals)
    k = max([i + 1 for i in range(m) if s[i] <= (i + 1) * q / m] or [0])
    return k


CALCULS = [
    ("C-01", "Combien d'essais indépendants sans aucun échec faut-il au minimum pour affirmer, au niveau de confiance de 95 % (borne exacte unilatérale), que le taux d'échec est au plus de 1 sur 1 000 ? Donne un entier.",
     lambda: min(n for n in range(1, 10000) if (1 - 0.001) ** n <= 0.05), "entier exact"),
    ("C-02", "Un détecteur repère chaque épisode saboté avec une probabilité de 0,02, indépendamment d'un épisode à l'autre. Quelle est la probabilité d'au moins une détection sur 100 épisodes sabotés ? Quatre décimales.",
     lambda: round(1 - 0.98 ** 100, 4), "±0,0001"),
    ("C-03", "Procédure de Benjamini et Hochberg au taux q = 0,05 sur les six valeurs p 0,001 ; 0,008 ; 0,039 ; 0,041 ; 0,042 ; 0,06. Combien d'hypothèses sont rejetées ?",
     lambda: bh([0.001, 0.008, 0.039, 0.041, 0.042, 0.06], 0.05), "entier exact"),
    ("C-04", "Deux lecteurs classent 50 propositions en « retenue » ou « non ». Ils s'accordent sur 20 « retenue » et 15 « non » ; le premier seul dit « retenue » 5 fois, le second seul 10 fois. Quel est le kappa de Cohen ? Deux décimales.",
     lambda: round(((35 / 50) - ((25 / 50) * (30 / 50) + (25 / 50) * (20 / 50))) / (1 - ((25 / 50) * (30 / 50) + (25 / 50) * (20 / 50))), 2), "±0,01"),
    ("C-05", "Trois prévisions 0,9 ; 0,7 ; 0,2 ont pour issues respectives 1 ; 0 ; 0. Quel est le score de Brier moyen ? Deux décimales.",
     lambda: round(((0.9 - 1) ** 2 + 0.7 ** 2 + 0.2 ** 2) / 3, 2), "±0,005"),
    ("C-06", "Zéro succès en 50 essais : quelle est la borne supérieure exacte de Clopper et Pearson de l'intervalle bilatéral à 95 % ? Quatre décimales.",
     lambda: round(1 - 0.025 ** (1 / 50), 4), "±0,0001"),
    ("C-07", "X suit une loi binomiale de paramètres n = 10 et p = 1/2. Quelle est P(X ≥ 8) ? Quatre décimales.",
     lambda: round(sum(comb(10, k) for k in range(8, 11)) / 2 ** 10, 4), "±0,0001"),
    ("C-08", "Test séquentiel du rapport de vraisemblance de Wald avec α = 0,05 et β = 0,20, seuils approchés de Wald : quelles sont les deux bornes sur le logarithme naturel du rapport ? Trois décimales chacune.",
     lambda: (round(math.log((1 - 0.20) / 0.05), 3), round(math.log(0.20 / (1 - 0.05)), 3)), "±0,001 chacune"),
    ("C-09", "Une martingale positive part de 1. D'après l'inégalité de Ville, quelle est la borne sur la probabilité qu'elle dépasse un jour 40 ?",
     lambda: 1 / 40, "exact (0,025)"),
    ("C-10", "Correction de Bonferroni pour 12 tests au niveau global 0,05 : quel seuil par test ? Cinq décimales.",
     lambda: round(0.05 / 12, 5), "±0,00001"),
]

PUBLIES = [
    ("P-01", "Selon le résumé de Wen et al., « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats » (arXiv 2411.17693), de quel pourcentage la stratégie de déploiement adaptatif réduit-elle le nombre de portes dérobées par rapport aux bases non adaptatives, à utilité donnée ?",
     "2411.17693v1.pdf", 1, "reduces the number of backdoors by 80% compared to non-adaptive baselines", "80 %"),
    ("P-02", "Selon le résumé de Bailey et al., « Obfuscated Activations Bypass LLM Latent-Space Defenses » (arXiv 2412.09565), de combien à combien les attaques font-elles souvent tomber le rappel des moniteurs, et quel taux de contournement des garde-fous gardent-elles ?",
     "2412.09565v2.pdf", 1, "reduce recall from 100% to 0% while retaining a 90% jailbreaking rate", "de 100 % à 0 %, en gardant 90 %"),
    ("P-03", "Dans « AI Control: Improving Safety Despite Intentional Subversion » (Greenblatt et al., arXiv 2312.06942), combien de problèmes de programmation compte le cadre d'essai dit « APPS backdooring » ?",
     "2312.06942v5.pdf", 3, "solve 5,000", "5 000"),
    ("P-04", "Dans Korbak et al., « How to evaluate control measures for LLM agents? » (arXiv 2504.05259), combien de niveaux de contrôle de l'IA (et de modèles fictifs) la trajectoire définit-elle ?",
     "2504.05259v1.pdf", 1, "five fictional models (M1-M5)", "cinq (M1 à M5)"),
    ("P-05", "Selon Foygel Barber, Candès, Ramdas et Tibshirani, « The limits of distribution-free conditional predictive inference » (arXiv 1903.04684), une garantie de couverture conditionnelle exacte est-elle possible sans hypothèse sur la loi des données ?",
     "1903.04684v2.pdf", 1, "exact conditional inference guarantees are known to be impossible without imposing assumptions", "non, impossible sans hypothèse sur la loi"),
    ("P-06", "Dans quelle revue, quelle année et quel volume a paru « Microarrays, Empirical Bayes and the Two-Groups Model » de Bradley Efron (arXiv 0808.0572) ?",
     "0808.0572v1.pdf", 1, "Statistical Science 2008, Vol. 23, No. 1", "Statistical Science, 2008, volume 23, numéro 1"),
]


def main():
    rep = []
    for i, q, f, tol in CALCULS:
        rep.append({"id": i, "sorte": "calcul refait par code", "question": q, "reponse": f(), "tolerance": tol,
                    "verification": "scripts/temoins_v1.py (fonction de la ligne " + i + ")"})
    for i, q, pdf, p, passage, r in PUBLIES:
        t = page(pdf, p)
        if passage not in t:
            print("PASSAGE ABSENT :", i, pdf, p)
            return 1
        rep.append({"id": i, "sorte": "fait publié, PDF du dépôt, à la page", "question": q, "reponse": r,
                    "source": f"docs/sources/pdf/{pdf}", "page_du_fichier": p, "passage_mot_pour_mot": passage,
                    "verification": f"pdftotext -f {p} -l {p} docs/sources/pdf/{pdf} -"})
    (ICI / "reponses-ne-pas-servir").mkdir(exist_ok=True)
    (ICI / "reponses-ne-pas-servir" / "reponses-questions-temoins-v1.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1))
    md = ["# Questions témoins du protocole X — réserve v1 (questions seules)", "",
          "Pièce servable. Règle 2 du protocole X, version 2 : trois à cinq de ces questions sont mêlées à chaque question servie, après le test de neutralité. Chaque modèle donne sa réponse et sa confiance (probabilité d'avoir juste, entre 0 et 1). Les réponses sont dans une pièce séparée, à ne jamais servir : `reponses-ne-pas-servir/`.",
          "", "Consigne à joindre : « Réponds à chaque question témoin en une ligne, puis donne ta confiance (probabilité que ta réponse soit juste). »", ""]
    for r in rep:
        md.append(f"- **{r['id']}** — {r['question']}")
    (ICI / "questions-temoins-v1.md").write_text("\n".join(md) + "\n")
    md2 = ["# Réponses des questions témoins — réserve v1 — NE PAS SERVIR", "",
           "Pièce séparée des questions (règle 2). Les calculs sont refaits par `scripts/temoins_v1.py` ; les faits publiés sont lus à la page dite, le passage attendu figurant mot pour mot dans la sortie de `pdftotext` (le script échoue sinon).", "",
           "| id | sorte | réponse | tolérance ou source |", "|---|---|---|---|"]
    for r in rep:
        src = r.get("tolerance") or f"{r['source']}, page {r['page_du_fichier']} du fichier : « {r['passage_mot_pour_mot']} »"
        md2.append(f"| {r['id']} | {r['sorte']} | {r['reponse']} | {src} |")
    md2 += ["", "Notation : exactitude = part des réponses justes à la tolérance dite ; score de Brier = moyenne de (confiance − juste)², juste valant 1 ou 0."]
    (ICI / "reponses-ne-pas-servir" / "reponses-questions-temoins-v1.md").write_text("\n".join(md2) + "\n")
    for r in rep:
        print(r["id"], r["reponse"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
