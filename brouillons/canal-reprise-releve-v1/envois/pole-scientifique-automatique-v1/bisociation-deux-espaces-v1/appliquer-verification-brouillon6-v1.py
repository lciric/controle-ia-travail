"""Brouillon 6 = brouillon 5 + retouches R1 à R3 de la vérification des corrections (verification-corrections-brouillon5-v1.md).
Usage : python3 -I appliquer-verification-brouillon6-v1.py BROUILLON5 BROUILLON6 HH:MM"""
import sys
src, dst, heure = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src, encoding="utf-8").read()

def rep(old, new, n=1):
    global t
    c = t.count(old)
    assert c == n, (c, old[:80])
    t = t.replace(old, new)

COND = ("si l'avance de N_β0 sur b en « moyen » est d'au moins +3 points ; à P4 = 3, elle vaut 0,00 pour une avance de +1 point ou moins : "
        "l'adoption exige à la fois P4 ≥ 3 environ et une somme (avance + P4) d'au moins 5 points environ")

rep("BROUILLON 5 (version soumise au gel de Lazar ; corrections de la contre-lecture 4)",
    "BROUILLON 6 (version soumise au gel de Lazar ; corrections de la contre-lecture 4 et de leur vérification)")
rep("seules changent des phrases (N1, N4, N5, N7)",
    "seules changent des phrases (N1, N4, N5, N7), la confiance de P4, retirée (N1)")
rep("et la définition opérationnelle de l'issue de l'audit et de V7 (N3).",
    "et la définition opérationnelle de l'issue de l'audit et de V7 (N3). **Brouillon 6** : retouches R1 à R3 de la vérification des "
    "corrections (Sonnet 5.5 neuf, `verification-corrections-brouillon5-v1.md`), appliquées par conv-audit (Opus 5.5) à " + heure +
    " UTC ; aucun chiffre ni seuil changé.")

# R3 — condition des chiffres de sensibilité
rep("l'adoption vaut 0,88 / 0,82 à P4 = 3, 0,23 à P4 = 2,5 et 0,00 à P4 = 1,5 (script § 17 ; contre-lecture 4, N1).",
    "l'adoption vaut 0,88 / 0,82 à P4 = 3, 0,23 à P4 = 2,5 et 0,00 à P4 = 1,5 " + COND + " (script § 17 ; contre-lecture 4, N1 ; vérification, R3).")
rep("(adoption 0,88 / 0,82 à P4 = 3, 0,23 à 2,5, 0,00 à 1,5)",
    "(adoption 0,88 / 0,82 à P4 = 3, 0,23 à 2,5, 0,00 à 1,5, " + COND + ")")
rep("(0,23 à P4 = 2,5)", "(0,23 à P4 = 2,5 au mieux ; 0,00 à P4 = 3 si l'avance de N_β0 sur b en « moyen » est de +1 point ou moins)")

# R1 — reste de l'ancienne conséquence de V7
rep("(V7 : version nouvelle, sans réglage)", "(lue par J, A7 et les déclencheurs d'audit ; V7 sans conséquence depuis le brouillon 5)")

# R2 — audit : X de (ii), contrastes de (iii), audit de V9
rep("la borne basse à 99 % de Δ(N_PCg, N_β0) est > 0 ;",
    "la borne basse à 99 % de Δ(N_PCg, N_β0) est > 0 en M_bien ou en M_moyen (l'une suffit) ;")
rep("au moins un contraste décisif de plus que sa demi-largeur à 95 %.",
    "au moins un contraste décisif du § 7 (1 à 9 et 11 à 15, plus 20 si S17 = option 1) de plus que sa demi-largeur à 95 %.")
rep("le rapport d'audit étant scellé.",
    "le rapport d'audit étant scellé. **Audit déclenché par V9 (rendu avant l'invocation des mondes de décision, § 9 ; vérification, R2)** : "
    "il se limite à la relecture du code et à la relance des seuls témoins d1c et c sur les graines de validation ; aucun bras candidat "
    "(N, ses ablations, ses placebos dont N_PCg) n'est exécuté ; (i) s'y applique ; (ii) ne s'y applique pas ; (iii) y porte sur "
    "Δ(d1c, c) dans les miroirs de validation de `M_inertes`. Ses issues sont les mêmes.")

# Mentions de version
rep("corrigés dans ce brouillon 5", "corrigés dans les brouillons 5 et 6")
rep("lues dans le brouillon 5", "lues dans le brouillon 6")
rep("Le brouillon 5 n'est pas la version relue.", "Ni le brouillon 5 ni le brouillon 6 ne sont la version relue.")
rep("(brouillon 5) aux valeurs", "(brouillon 6) aux valeurs")
rep("traitement de chaque remarque).\n\n### Historique — ce qui avait changé entre le brouillon 3",
    "traitement de chaque remarque).\n8. **Vérification des corrections (brouillon 6)** — Sonnet 5.5 neuf, `verification-corrections-brouillon5-v1.md` : script rejoué "
    "au bit près, chiffres conformes au § 17 ; R1 (reste « V7 : version nouvelle » dans le traitement de la contre-lecture 3) corrigé ; "
    "R2 (l'audit de V9 ne peut pas exécuter N_PCg avant l'invocation) : audit de V9 limité au code et aux témoins d1c et c, X de (ii) "
    "et contrastes de (iii) nommés ; R3 (les chiffres 0,88 / 0,82, 0,23, 0,00 supposent une avance d'au moins +3) : condition écrite, "
    "suppression de la confiance de P4 nommée dans l'en-tête.\n\n"
    "### Historique — ce qui avait changé entre le brouillon 3")

open(dst, "w", encoding="utf-8").write(t)
print("REMPLIR restants:", t.count("À REMPLIR"))
