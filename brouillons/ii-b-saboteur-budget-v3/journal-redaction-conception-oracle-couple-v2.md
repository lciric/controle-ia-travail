EXPLORATOIRE, NON OPPOSABLE (R-522)

# Journal de rédaction — suite : règle de redimensionnement (arrêtée) et texte neuf de l'oracle couplé — v2

Suite de `journal-redaction-conception-revisee-v1.md` (intact). Même rédacteur, mêmes cloisonnements. Fin vers 2026-11-19T12:28Z. Aucun commit, aucune poussée, aucune suppression, aucune dépense. Aucun refus d'outil. Une interruption par la limite d'usage du modèle, avant l'écriture du texte ; reprise sur les fichiers.

## Ce qui a été lu en plus
- Complément 2 (`af6cb411…`, vérifié) puis complément 3 (`f23a79da…`, vérifié), qui le remplace.
- Contre-lecture 1 du brouillon 1 de la v2 (`cee9711d…`, vérifiée), en entier, et les deux sorties de ses rejeux.
- Rien d'autre : ni le registre des accords, ni le devis, ni `t06/cout.py`, ni `premier_test_ia/conditions.py`.

## Complément 2 (règle de redimensionnement)
Script `simulation-regle-redimensionnement-ii-b-v1.py` écrit, **jamais passé**, gardé. Sa logique (candidats, admissibilité, tours, branches) a servi aux sections 5 et 6 du texte neuf. Aucun texte de règle n'a été écrit.

## Complément 3 (oracle couplé)
- **Famille examinée** : voisine de rang du coût déclaré, retenue par un noyau qui rend chaque suite également probable sous l'hypothèse nulle ; puis tirage dans un bloc de 1, 2, 4 ou 8 rangs.
- **Passage v1** : illisibles rangés en bas → dérive de l'excès honnête. Défaut de ma définition ; corrigé (lisibilité suivie).
- **Passage v2** : la règle écrite d'avance rend le bloc de 8 (aucun couplage). Je n'ai pas changé la règle.
- **Passage v3** : mêmes règles, blocs aval joués aussi pour le meilleur bloc couplé ; rend encore le bloc de 8. À sa lecture, **défaut de programme** : pour le bloc de 8, les blocs C et D passaient deux fois le même bloc. Chiffres faux, non cités.
- **Passage v4** (fait foi) : défaut corrigé ; rend le bloc de 4, de 0,9 point.
- **Constat de fond** : le couplage baisse le bruit et le signal ensemble ; il ne sert vraiment que contre un maître qui s'ancre sur ses propres coûts gonflés. Rendu comme nœud 1, sans trancher.
- **Statistique de chaîne** : celle du brouillon 1 de la v2 n'est plus symétrique sous couplage ; remplacée par les rangs au contexte réécrit, par la règle écrite d'avance.
- **Étalonnage à excès planté** : idée de ce texte, pour que les branches ne lisent ni maître ni moniteur.

## Écartés
- Blocs de 1 rang (épreuve arrêtant un oracle sain jusqu'à 19 %) ; blocs de 2 (admis, non retenus par la règle).
- Tirage de réécriture long, hors des huit suites (brouillon 1 de la v2) : le couplage demande une des huit suites ; plus de surcoût.
- Suites de couplage à part des suites d'estimation (pour rendre la paire échangeable) : coût doublé, non simulé.

## Ce que je n'ai pas pu trancher
Onze nœuds, section 13 du texte. Le premier décide du reste.

## Réserves
- Le choix du bloc n'est pas stable d'une entropie à l'autre.
- Le couplage par le préfixe n'est pas joué dans la grille de l'oracle couplé (nœud 6).
- Les seuils des branches sont a priori et discutables (nœud 5) ; le plafond de tours dépend d'un devis non lu.
- Pour les épreuves de sensibilité et de rejet du flagrant, un seul défaut rejoué.
- Les essais réduits n'ont pas été écrits sur disque.
- Les lois nulles de la simulation sont des approximations normales ; au code, convolution.
