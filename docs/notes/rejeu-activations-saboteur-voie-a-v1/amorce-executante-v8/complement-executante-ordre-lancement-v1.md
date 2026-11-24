# Complément de l'exécutante à l'ordre de lancement du rejeu — v1

Pièce de travail (classe C), 2026-11-24T10:41:13Z, exécutante v8. Changements apportés à l'ordre rédigé par Fable (87cbc7ad… avant changement), sur les mots de la mère du 2026-11-24 vers 10:35Z et 10:38Z, et eux seuls :
1. Clé « go » : GO-2026-11-24-13 (accord de calcul, 11 USD, empreinte entière du devis), au lieu de GO-2026-11-24-06 (type « dépense », refusé par le crochet). Le code de l'amorce suit (constante GO_ATTENDU) ; les essais remplacent dans le gabarit l'accord d'avant.
2. Préparation ajoutée en tête, « fichiers-course » : les trois fichiers de la course (règle M-2 de l'additif 2) et leurs compagnons sont exigés, dans le clone, sous diag/20261122-202132-iib-reel/, à leurs empreintes entières ; sinon refus de départ. Ils entrent au commit de lancement par « git add -f » (diag/ n'est pas ignoré ; la passe exige un arbre propre), tirés de origin/essai/iib-explo-v8. Cas sain joué sur les vrais fichiers (code 0, « conformes ») ; faux cas dans les essais (absents ; empreinte fausse).
3. Branche mise à jour depuis main (additif 2 scellé, ligne SCELLEMENT-ADDITIF-2-SONDES-IIB, ligne GO-2026-11-24-13).
Reste « A_FIXER » : le module de la passe conforme aux deux additifs (trois occurrences), transmis par la mère à sa livraison ; sa ligne de commande est à confirmer sur sa notice.
