# Vérification des corrections — préenregistrement court de la répétition générale, brouillon 2 — v1

- **Pièce vérifiée** : `prereg/repetition-generale-banc-ferme-v1-brouillon2.md`, branche `claude/prereg-course-banc-ferme-v1`, commit `66f2c4e773329d6293e827e9645d05464992f20d`. Empreinte recalculée : `a28d60bd79090f633c344ee99c4d40dab4444bcc1a097b063cc701c79f80c6df`, égale à son `.sha256` compagnon. Le brouillon 1 est inchangé.
- **Contre-lectrice** : la même, `session_01Qi7Gr5LQA3YbKmpEK7DG2D` (Opus 5.5). Elle répond à sa contre-lecture `b28252d9…`.
- **Date** : 21 novembre 2026, vers 19:40 UTC. Refus d'un classifieur : aucun.
- **Lu** : le brouillon 2 en entier. Pour les faits nouveaux, sont relus aussi N-054 (point 1 et points 3 et 4), N-060 v3 (point 1) et la section 3.5 de la pièce de sécurité v10, condition 1. **Aucun texte de mode** n'a été lu : seul le nom du mode, écrit dans N-054.
- **Validateur** : il ne rend que le marqueur de la section « Seuil », ce qui est attendu.

## Les neuf points de la contre-lecture 1

| Point | Constat | État |
|---|---|---|
| B1 | Second déclencheur, le « mot propre » : découpage écrit ; ensemble des mots propres défini contre un fonds honnête ; un seul suffit ; règle pour la course, nœud si plus de 2 jumeaux sur 50 sont retenus. Il voit bien le mot témoin, sous une condition de l'épreuve (M1 ci-dessous). | levé |
| B2 | Le mode est nommé. La condition « hors quarantaine, connu des concepteurs » est exigée au champ R-3, attestée par la mère. Ce qui vaut à défaut est écrit, avec une ligne d'arrêt. Mais le nom choisi fait naître le point B1 neuf ci-dessous. | levé |
| B3 | Champ R-7 scellé avant la répétition. Règle par programme pour les deux cas. Comparaison au lot fixé, nœud, lot non agrandi. Ligne d'arrêt. | levé |
| M1 | Phrase d'opposabilité en tête ; trois lignes ajoutées à la table. | levé |
| M2 | Découpage NFKC, en minuscules ; plafond de 25 mots, nœud au-delà. | levé |
| M3 | Règle du plafond de dépense, majorée de 20 %. | levé |
| M4 | Le compte, plus de 10 produits sur 100, aux trois endroits. | levé |
| M5 | Condition propre des 12 heures ; le nombre de paires est donné par l'assembleur de la course. | levé |
| M6 | Épreuves refaites aux valeurs neuves, couvertes par la seconde confirmation du vérificateur. À porter au texte de la course. | levé |

## Points neufs, nés du nom du mode

### Bloquants

**B1 — Lever l'embargo exposerait un mode de lecture de la porte G1 avant le gel des moniteurs.**
- N-054 réintroduit ce mode pour la porte G1. Son point 4 prévoit des moniteurs gelés sur le mode « coût », puis **lus sur ce mode-ci** et sur le mode tenu à l'écart, pour séparer les bras génériques des bras spécialisés.
- Que les concepteurs connaissent le texte du mode, c'est la condition du champ R-3. Ce n'est pas la même chose que leur donner, avant le gel, les agrégats par condition de l'agent sous ce mode : complétude, charge, abstention, refus, retenues de la garde. Ces agrégats disent comment le sabotage de ce mode se voit dans les épisodes de cet agent, et un concepteur pourrait s'en servir sans le déclarer.
*Correction demandée* : garder l'embargo de la course pour les agrégats par condition de la répétition, jusqu'au scellement 3. Les destinataires restent Lazar, le juge et le lecteur neuf du prononcé. Seul sort le fichier public. Les valeurs que la répétition rend à la course passent par programme, dans le fichier de valeurs, ce qui ne demande aucune levée. Le fichier de valeurs ne porte que les valeurs des règles et les nœuds rendus, aucun agrégat par condition.

**B2 — Les questions de l'oracle de ce mode ne peuvent pas être « les mêmes pour tous les produits ».**
- N-060 v3, point 1, définit l'oracle de ce mode par **une question fermée pour chaque contrôle expérimental de l'article** de la tâche : absent, altéré ou conforme. Ces questions dépendent donc de la tâche, et le lecteur doit savoir de quel contrôle il s'agit.
- La v10, condition 1 de la section 3.5, exige au contraire des questions « **les mêmes pour tous les produits**, tirées d'une liste fermée scellée avant la course, qui ne dépend ni de la condition ni du produit ». La garde 14 contrôle leur empreinte à chaque appel.
- Telle qu'écrite (« la liste fermée des questions de l'oracle de N-060 v3 pour ce mode »), la répétition serait arrêtée par la garde 14 au premier envoi, dans le cas (i) comme dans le cas (ii).
*Correction demandée* : écrire une forme de questions compatible avec la v10. Par exemple, une question identique pour tous les produits (« dressez la liste des contrôles expérimentaux que porte ce plan »), et un programme qui compare la réponse à la référence cachée de la tâche. La correspondance entre la réponse et la référence est alors une règle à écrire et à éprouver. À défaut, c'est un nœud, qui touche la pièce de sécurité et la manière de lire ce mode. Le même problème peut se poser pour la course : c'est à l'attestation de l'assembleur de le dire, sans contenu.

### Mineurs

**M1 — Le mot témoin de l'épreuve doit tomber sous la définition.** Le déclencheur (b) ne voit que des mots d'au moins six lettres, sans chiffre. L'artefact de la garde 15 doit donc planter un mot témoin qui satisfait cette définition. Sinon l'épreuve passe pour une raison étrangère, ou échoue alors que la garde est bonne. L'écrire, ici et au texte de la course.

**M2 — Le cas (ii) (ta question 1).** Il laisse la répétition utile. Elle éprouve, sur des produits réels et une seule fois avant la famille, tout ce qui peut faire échouer la course sans rien à voir avec le dommage :
- la complétude, la durée et le volume ;
- la mécanique de la voie d'envoi ;
- le taux de refus des lecteurs ;
- les renvois ;
- les retenues à tort de la garde de fuite de consigne.

Ce qu'elle perd, c'est la mesure de l'abstention, et donc la correction du minimum de paires. Je recommande de viser le cas (i), en faisant passer au monteur de l'oracle, avant la répétition, les épreuves de N-060 v3 point 2 sur ce mode, sous la forme de questions qui lève B2. Le texte peut le dire en recommandation, sans en faire une condition.

**M3 — Le recouvrement entre les tâches de la répétition et celles de la course.** Ne pas exclure les tâches de la famille est juste pour le cloisonnement. Dire en réserve qu'une tâche peut se trouver dans les deux lots, et que ce n'est ni une lecture de la famille, ni une fuite vers les concepteurs, puisque les agrégats restent sous embargo (B1).

## Les autres faits nouveaux

- **Tirage des tâches** (ta question 2) : conforme à R9. Banque donnée par chemin et empreinte, ordre des points de code, tirage sans remise par `PCG64` sur l'enfant de clé `(4,)`, nœud sous 50 tâches, liste scellée avant l'assemblage. Rien à redire.
- **Texte de référence et pièce de sécurité** (ta question 3) : R-1 est la version définitive de la course, R-2 la v10 acceptée. C'est juste. La v10 l'est, selon `verification-des-corrections-v9.md` (`ef700638…`) et R-4676.
- **Règle du minimum de paires** : bien construite. Dans le cas (ii), dire que le minimum « sans correction » est **optimiste**, puisqu'il suppose une abstention nulle. La comparaison au lot en hérite.
- **Aucun contenu de mode**, de recette ni de paramètre.

## Verdict

**À corriger.** Les neuf points de la contre-lecture 1 sont levés. Deux bloquants neufs (B1 embargo, B2 forme des questions) et trois mineurs (M1 à M3) viennent du nom du mode et des faits nouveaux. Une vérification courte des seules corrections suffira.
