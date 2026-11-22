# Additif 1 à l'ordre de l'étalonnage, version 2 — seuil de la coupure propre relevé à 16 USD ; versement par lot dit selon le code (brouillon 1)

Écrit le 2026-11-22 par la session de reconception. Il complète l'ordre v2 scellé par la mère (brouillon 3 : `ordre-etalonnage-ii-b-v5-v2-brouillon3.md`, `3ec3a60523bbf45c0f345c91d5bdf8e20e9bb220b39a78efa93ea7c57420cc6f`) sans le réécrire, et prime sur les passages qu'il nomme. **Il ne s'applique qu'au mot de Lazar** (le relèvement d'un seuil accordé est un nœud), porté par la mère ; tant que ce mot manque, l'ordre v2 vaut tel quel.

## 1. Le seuil de la coupure propre : 12 → 16 USD
- **Cause** : l'étalonnage en cours tourne 5 à 7 fois plus lentement que le devis, à cause de l'hôte et non du code (lecture du code à 43d6d067 : `brouillons/ii-b-saboteur-budget-v5/code-v5/contre-lecture-cl1/note-lecture-code-versement-coupure-rythme-v1.md`). La projection est de 10 à 12 heures. Coupé à 12 USD, l'étalonnage ne serait pas exploitable : le fichier des sorties d'oracle n'est écrit qu'à la fin, et l'issue serait « non calculable ».
- **Bornes** : 16 USD reste sous le plafond de 17 USD de l'étape 1 au devis scellé (`devis-ii-b-v5-scelle-v1.md`, cb881522…) et sous la ligne `GO-2026-11-21-70` (plafond 60, coupure de la ligne à 55, qui reste et prime).
- **Où vit le seuil** : c'est une constante du code, `COUPURE_ETALONNAGE_USD` dans `src/controle_ia/iib/session_v5.py`, que la surveillance lit côté session exécutante, jamais sur la machine. La configuration scellée ne le porte pas : elle ne change pas.
- **Correctif 0013** : `brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0013/0013-…patch` (8538c203…). Il ne change que la constante, ses textes et les essais de la règle, avec les mêmes formes ; 275 essais, inchangés. Vérification : `<<VERIFICATION_CORRECTIF_0013>>`.
- **Passages de l'ordre v2 visés** : partout où l'ordre dit « 12 USD » pour la coupure propre de l'étalonnage (ligne d'accord, § 3 « Coupure propre », § 4 étape 6, § 5 étape 3, § 5 compte rendu, § 6 Arrêts, § 6 Dépense), lire « 16 USD », à partir de la relance de la surveillance sous ce correctif. L'en-tête de la version 2, qui décrit la tentative 1, reste tel quel. L'écart déclaré de dépense à la coupure (0,1 à 0,4 USD au-delà du seuil) vaut désormais au-delà de 16 USD : la dépense réelle à la coupure serait d'environ 16,1 à 16,4 USD, sous le plafond de 17 USD de l'étape 1. À cela s'ajoute, comme avant, le forfait de téléchargement (1,04 USD au plus), hors du compte de la règle. **Ce point est à faire accepter par Lazar avec le seuil.**

## 2. Versement par lot : la phrase vraie
Les passages « écrits, scellés et poussés lot par lot » (§ 3, « Versement par lot »), « sorties scellées et poussées » (§ 5 étape 4) et « scellés et poussés » (§ 7) se lisent ainsi, d'après le code à 43d6d067 :
- chaque lot est écrit et scellé **sur le disque de la machine** ;
- l'amorce ne **pousse** qu'au départ, à la fin normale, sur une sortie en erreur du lanceur, par la minuterie (55 USD ou échéance), et à un second démarrage ;
- à la coupure propre, rien n'est poussé : les lots restent sur le disque de la machine arrêtée. Leur rapatriement demande de redémarrer la machine (chemin « run interrompu » de l'amorce, qui pousse puis demande la destruction), **sur le mot de la mère**.

Corriger la poussée par lot dans le code est remis à la course, avec la consignation du repli du cache.

## 3. Commande de relance, pour l'exécutante, au mot de Lazar seulement
`<<COMMANDE_RELANCE_SURVEILLANCE>>`
