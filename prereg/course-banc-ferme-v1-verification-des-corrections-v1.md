# Vérification des corrections — préenregistrement de la course du banc fermé, brouillon 2 — v1

- **Pièce vérifiée** : `prereg/course-banc-ferme-v1-brouillon2.md`, branche `claude/prereg-course-banc-ferme-v1`, commit `6d0cedeaf2aa254650a30806283e5fbedbf2c7f4`. Empreinte recalculée : `025d386e9450018c33fe237d65f315d014e78c8a940c08b441514c1a8e98c998`, égale à son `.sha256` compagnon. Le brouillon 1 est inchangé au même commit (`d4e6d712…`), et le diff entre `857fcbbb` et `6d0cedea` n'ajoute que le brouillon 2 et son compagnon.
- **Contre-lectrice** : la même que pour la contre-lecture 1, `session_01Qi7Gr5LQA3YbKmpEK7DG2D` (Opus 5.5). Rapport vérifié : `prereg/course-banc-ferme-v1-contre-lecture-v1.md` (`e9ed547d5dd7006ef93610ebefcc8c05680036685a385894a23aa01580f066ef`), commit `dd92828d`.
- **Date** : 21 novembre 2026, vers 19:10 UTC. Refus d'un classifieur : aucun.
- **Lu** : le brouillon 2 en entier, et rien d'autre de neuf. Les interdits de la contre-lecture 1 valent toujours.
- **Validateur** : sur le brouillon 2, `problemes` rend « marqueur À REMPLIR restant hors des sections exigées ». C'est l'effet voulu de la correction M10 : le scellement est refusé par le code tant qu'un champ reste ouvert.

## Point par point

| Point | Correction attendue | Constat | État |
|---|---|---|---|
| B1 | champs remplissables dans l'ordre | heures chiffrées (48) ; dépense, minimum de paires et attestation à l'addendum A, avant la construction des gardes ; lot, commit et manifeste des moniteurs à l'addendum B, avant le GO ; garde 10 sur les trois empreintes ; lecture de l'assembleur au registre (D2, conditions 2 et 9, liste d'arrêt) | levé |
| B2 | référence de la garde 5 | D7 bis : qui, programme sans contenu, périmètre large et daté, trois manifestes (épreuve, répétition, pose), lieu ; champ n° 16 ; nœud 9 ; ligne d'arrêt | levé |
| B3 | aveuglement à la condition | lecture en deux temps ; extraction du seul produit par programme ; identifiants neufs ; graine de lecture `(2,)` ; réponses scellées avant le second temps ; D8 réécrite ; ligne d'arrêt ; question à l'assembleur sur ce que permet la pièce 3 | levé (voir R1 ci-dessous) |
| B4 | nœud 1 et voie de sortie | nœud 1 reposé, avantages et inconvénients ; moyen de lecture écrit (D6) ; ligne d'arrêt sur l'envoi à un autre fournisseur ; coût mis à jour. La recommandation (a) porte un écart déclaré à N-060 v3 point 1 : c'est bien un nœud de Lazar, posé comme tel | levé |
| B5 | embargo | fichier public sans distinction de condition ; fichier sous embargo pour tout agrégat par condition, charge comprise ; levée liée au scellement 3 et au scellement de la part de G1 ; destinataires en liste fermée ; lignée de l'attaquant informé, mère, concepteurs exclus ; compte rendu de l'opérateur borné au fichier public ; identifiants neutres | levé |
| M1 | format et pile du calage | champ n° 2 étendu ; « Forme : celle du calage » (D3) ; condition 5 ; ligne d'arrêt ; réserve 7 | levé |
| M2 | positions et type des activations | déroulement, point 4 : toutes positions du contexte, une fois, type du harnais ; lieu non enregistré : réserve et nœud, aucune régénération | levé |
| M3 | métriques 5 et 6 | conditionnelles à la définition de la pièce 3 | levé |
| M4 | course tronquée | exception écrite en tête des critères, et dans la ligne | levé |
| M5 | liste d'arrêt | parenthèse dite ; ligne de l'invariant en toutes lettres ; dépôt non cloné à la pose | levé |
| M6 | lecteur de la question fermée | D7 ter, champ n° 17, D8, condition 10 | levé |
| M7 | moyen de lecture | D6 | levé |
| M8 | garde 10 et addenda | liste fermée de deux addenda | levé |
| M9 | provenance | branche et commit dans la table | levé |
| M10 | validateur | marqueur du gabarit sur les champs d'avant scellement | levé |
| M11 | nœud 4 et renvoi | trois options et leur coût ; renvoi à l'addendum 1 au nœud 5 | levé |

Les ajouts hors contre-lecture (nœud 9, réserves 7 et 8, lecteur du prononcé hors de la lignée de l'attaquant informé) sont déclarés. Ils ne retirent rien et n'introduisent aucun contenu de mode.

## Restes mineurs, non bloquants

**R1 — Comparaison au jumeau dans la lecture aveugle.** Le déroulement, point 7, présente les deux produits d'une paire « côte à côte, sans étiquette » quand la pièce 3 compare au jumeau. Le texte doit dire comment le dommage se calcule sans que le lecteur sache lequel est le jumeau. Proposition : le lecteur juge chaque produit séparément (la question fermée par contrôle), et le programme calcule la baisse par la table de correspondance scellée. Si la pièce 3 exige un jugement qui voit lequel est l'honnête, l'aveuglement ne tient plus, et c'est un nœud.

**R2 — Le vérificateur interne et l'addendum B.** Le vérificateur interne rend sa pièce à la condition 7. L'addendum B (empreinte du lot, manifeste des moniteurs du jour de la pose) est scellé à la condition 9. D8 lui fait pourtant lire « ses addenda », et ses points 8 et 21 ([PS] section 6.1) portent sur ce que fixe l'addendum B. Il faut l'écrire comme la pièce de sécurité le fait pour son point 4 : le vérificateur confirme ces points de nouveau, après l'addendum B et avant le GO. Ou bien déplacer sa pièce après la condition 9.

Ces deux restes ne changent ni l'hypothèse, ni les métriques, ni les seuils, ni les critères. Ils se reprennent dans la version définitive, avant le scellement par `sceller_prereg`, sans nouvelle contre-lecture complète : une relecture courte de ces deux lignes par la même contre-lectrice suffit.

## Verdict final

**Accepté.** Les cinq bloquants et les onze mineurs de la contre-lecture 1 sont levés. Deux restes mineurs (R1, R2) sont à reprendre dans la version définitive. Aucun contenu de mode, de recette ni de paramètre. Le scellement définitif attend en plus les champs ouverts, les nœuds 1 à 9 et le mot de Lazar.
