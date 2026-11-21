# Note de vérification courte — ordre de l'étalonnage de l'organisme retenu, brouillon 4 — cl1

Date : 2026-11-21. Pièce décisive (classe A), vérification courte par un autre modèle que le rédacteur (Claude Opus 5.5 ; le rédacteur est Claude Fable 5.2). Même mandat (`47b53672…`). Pièce : `brouillons/ii-b-saboteur-budget-v5/ordre-etalonnage-v5/ordre-etalonnage-ii-b-v5-brouillon4.md` (`12fb6dac…`, compagnon vérifié). Rien poussé, aucune dépense, aucune machine, aucun refus d'outil.

**Verdict : scellable une fois les champs remplis, après deux corrections de forme** (F1, F2), à faire par programme dans une version nouvelle. Aucune ne touche une règle.

## Ce qui est vérifié
- **Rejeu des quatre programmes de fabrication**, chaînés dans un dossier neuf (`ordre-rejeu-v2/`), avec les dates écrites dans les pièces : les brouillons 1 à 4 et les quatre notes de différences sont **identiques à l'octet** aux pièces versées.
- **Empreintes citées, recalculées** : elles sont toutes justes.
  - le texte scellé, ses errata 1 et 2, le devis et son erratum 1 ;
  - le mandat du rédacteur et l'ordre de la première course ;
  - les treize correctifs ;
  - mes quatre pièces : contre-lecture du code, vérification des corrections, notes 0008-0009 et 0010 ;
  - les rapports et notes du développeur, v1 à v5, ses sorties d'essais v3 à v5 et de répétition v2 et v3 ;
  - à la tête du code : liste figée `342ee21d…`, amorce `42196f90…`, lanceur de session v3 `42d295c8…`, gabarit v4 `eb329185…`, module de lecture `6446a304…` ;
  - les empreintes des trois consignes, lues dans leurs compagnons sans ouvrir les fichiers.
  
  L'arbre `ed9b0e48…` est celui que j'ai reconstruit.
- **Ligne GO-2026-11-21-70** : présente une fois au registre de `main`. Son contenu est conforme à l'ordre : 60 et 55, coupure à 12 par la surveillance, 1,38 et 6,90, dernière création au 27, échéance le 30. Instants vérifiés : 1796076000 pour 2026-11-30T22:00Z, 1796083200 pour 2026-12-01T00:00Z.
- **Différences justifiées** : chaque changement des notes renvoie au texte scellé et à ses errata, au devis et à son erratum, à la ligne d'accord, ou à une de mes vérifications : B1, M1 à M7, R1 et R2, risque « :\n », cas du plafond de tours sous 12, deux mineurs du 0010 déclarés, arrêt sans destruction ni relance après la coupure (devis § 3).
- **Aucune liberté de lecture avant la désignation** : personne n'ouvre une sortie avant le résultat scellé (§ 8) ; les conditions et la désignation se jouent une fois, par programme, sur processeur (§ 5, étape 6), et le code refuse le second passage. Le compte rendu de l'exécutante ne porte que l'issue et les phrases écrites par le programme.
- **Les neuf champs** sont bien ceux de la mère, de l'exécutante et de Lazar : branche du code, commit revu, commit de lancement, configuration, fichier d'entrées, intouchables, étiquette, mot de Lazar sur la première action, sort de la machine. Aucun autre chevron ne reste dans le texte. L'extrait du préalable 7b se trouve une fois au registre des décisions de `main`. Rien d'autre ne manque pour l'étalonnage.

## Deux corrections de forme
- **F1 (§ 7, table des sorties)** : `ids-actions-etalonnage-iib-v5.json` n'existe plus à la tête du code. Les identifiants sont versés par lot sous `donnees/<run>/lots/ids-lot-*.json`, et aucun fichier d'ensemble n'est écrit, comme le montre la répétition. La table omet aussi `graines-etalonnage-iib-v5.json`, les lots `diag/<run>/lots/lot-*.json` et `arret.json`. Or l'étape 5 compare le manifeste à cette liste : l'exécutante y verrait un écart et retiendrait la destruction. *Correction* : la table selon les noms réels ; les durées par oracle sont dans les rapportés.
- **F2 (§ 11, correctifs 9 à 11)** : la table les nomme `correctifs/0001-…distillateur…`, et la phrase les place « sous `code-v5/` ». Ils sont sous `code-v5/distillateur-v5/correctifs/`. Le contrôle de l'arbre rattrape toute erreur, mais le chemin doit être juste. *Correction* : le chemin entier.

## Mineur
- m1 (§ 3, marques de progrès) : « pour les épreuves » ; à l'étalonnage, les marques sont le chargement, le début, chaque lot, les oracles écrits et la fin, et les épreuves se jouent aux conditions, sur processeur. Phrase à ajuster, sans effet.
