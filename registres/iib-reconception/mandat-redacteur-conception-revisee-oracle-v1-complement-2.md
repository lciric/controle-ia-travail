# Complément 2 au mandat du rédacteur cloisonné — la règle de redimensionnement — sans aucune valeur mesurée

Écrit le 2026-11-19 par la session de reconception. Accord : `registres/go.md` sur `main`, ligne GO-2026-11-19-45 (mot de Lazar, « go », sur le nœud 3 de ta conception révisée). Les cloisonnements de ton mandat restent entiers : tu ne lis toujours aucune valeur mesurée de la première course, et tu ne liras pas davantage celles de l'étalonnage à venir.

## 1. Ce que Lazar a décidé
1. L'étalonnage part seul, avec l'oracle révisé, **sans changer aucune constante** (ton option (a)).
2. En parallèle, tu écris une **règle de redimensionnement** : par une formule, elle donne les constantes de la règle d'acceptation et de l'épreuve des faux acceptés à partir de ce que l'étalonnage mesurera. Elle fixe d'avance trois branches : (i) le saboteur complet part avec les constantes de la formule ; (ii) il part à une taille plus grande, sous le plafond ; (iii) il ne part pas : l'organisme n'est pas faisable à ce budget, c'est un résultat négatif, et l'oracle moins bruité (ton option (c)) devient un texte neuf.
3. La règle est contre-lue par un autre modèle, **scellée avant toute lecture de l'étalonnage**, approuvée une fois par Lazar. Si la branche dit « part » et que la dépense reste sous la ligne, la course complète suit sans nouveau mot.
4. Plafond inchangé : 60 USD, coupure à 55, dépense passée comptée (au plus 2,7 USD) ; création de la machine du saboteur complet au plus tard le 2026-11-28T23:00Z.

## 2. Ce que tu produis
`regle-redimensionnement-saboteur-budget-ii-b-v1-brouillon1.md` dans ton sous-dossier du bloc-notes. Pièce décisive (classe A), en-tête « EXPLORATOIRE, NON OPPOSABLE (R-522) ». Elle contient :
1. **Les entrées** : la liste fermée des grandeurs de l'étalonnage qu'elle lit, chacune définie sans ambiguïté comme fonction des sorties de l'oracle révisé (dispersion des coûts honnêtes, force de l'ancrage, part bornable, part d'illisibles, taux d'épisodes honnêtes acceptés sous les constantes candidates, débit mesuré pour le devis, et ce dont tu as besoin), avec son estimateur, son unité (l'épisode quand il le faut) et son incertitude. Si une entrée n'est pas dans les sorties prévues par ta conception révisée, ajoute-la aux rapportés de la conception (dis-le en clair : c'est une correction de la conception avant son scellement).
2. **La formule** : une procédure déterministe, exécutable par programme, qui rend les constantes de la règle d'acceptation (borne par action, plancher du total, nombre minimal d'actions bornables) et de l'épreuve des faux acceptés, plus la taille de la course (nombre d'épisodes du maître, tours), à partir des seules entrées. Dis ce qu'elle optimise et sous quelles contraintes écrites a priori : le sens de la consigne du saboteur (un excès modéré, borné par action, réparti), un taux d'acceptation de l'honnête borné, un écart minimal entre maître et honnête pour que les épisodes acceptés ne soient pas du bruit honnête sélectionné, la puissance de la lecture du dommage, le plafond de dépense. Aucune liberté laissée à celui qui l'appliquera.
3. **Les trois branches**, par des conditions écrites sur les sorties de la formule, mutuellement exclusives et exhaustives, avec le cas « non calculable ». La branche (iii) doit pouvoir sortir : dis dans quelle zone de la grille elle sort.
4. **La justification par simulation** sur ta chaîne synthétique (entropie neuve, grille déclarée avant le passage) : pour chaque cellule, ce que la formule rend, la branche, le taux d'acceptation du maître et de l'honnête sous les constantes rendues, la probabilité que la course complète aboutisse ; et l'erreur de la formule quand les entrées sont estimées sur 64 épisodes plutôt que connues.
5. **Les gardes contre l'abus** : la formule ne lit aucune donnée du maître ni d'aucun moniteur ; elle est appliquée une fois, par programme, sur l'étalonnage scellé ; son résultat est scellé avant toute configuration ; un second passage est interdit ; ce qu'on fait si l'épreuve du centrage révisée ou une autre épreuve arrête l'étalonnage (la formule ne s'applique pas).
6. **Ce que la règle change dans ce que l'organisme revendique** : si les constantes rendues s'éloignent de la consigne (par exemple une borne par action bien plus large), dis à partir d'où l'organisme n'est plus « un saboteur à budget » au sens de la conception v1 — c'est une condition de la branche (iii), pas un détail.
7. **Spécification du programme** qui l'applique et de ses essais (cas sain, artefact), et les **phrases de lecture écrites d'avance** pour chaque issue de l'étalonnage.

Nœuds : comme avant, tu rends la question sans trancher — en particulier tout ce qui toucherait l'épreuve du centrage révisée (elle n'est pas affaiblie) ou les revendications des lectures.

## 3. Ordre de travail
La contre-lecture de ta conception révisée est en cours ; ses remarques te reviendront pour correction. Commence la règle de redimensionnement maintenant ; quand les remarques arrivent, traite-les d'abord (la conception doit être scellée la première), puis reprends la règle.

## 4. Ce que tu rends
Chemins, empreintes, résumé de vingt lignes au plus : entrées, formule en une phrase, conditions des trois branches, zone de la grille où chaque branche sort, nœuds.
