# Vérification des différences — course du banc fermé, brouillon 12, et répétition générale, brouillon 7 — v1

- **Pièces vérifiées** :
  - `prereg/course-banc-ferme-v1-brouillon12.md`, commit `58f9e7e7`, empreinte `711e061f2a1e577f7e3f5fe2c3fd0cf5c59bfa062cd6b59481546350518bae30` ;
  - `prereg/repetition-generale-banc-ferme-v1-brouillon7.md`, commit `fc16837e`, empreinte `40837f73f07cc430dbc759ea56fdb5e4d07b48378fc65289505b24b3cb293751`.

  Leurs empreintes, recalculées, sont égales à leurs compagnons.
- **Contre-lectrice** : la même, `session_01Qi7Gr5LQA3YbKmpEK7DG2D` (Opus 5.5). Pièces de classe A, règle R2.
- **Date** : 21 novembre 2026, vers 20:30 UTC. Refus d'un classifieur : aucun.
- **Méthode** :
  - La pièce de sécurité v15 (`86244fae…`, commit `79754f41`) est comparée par `diff` à la v13. Son verdict « accepté » a été lu (`d0ae6647…`, commit `7bbb374e`). Elle a été lue sur sa règle des questions (points 5 et 6), les gardes 14 et 15, la liste d'arrêt, le point 26 et les réserves 15, 22 et 23.
  - `diff` du brouillon 11 au brouillon 12 de la course, et du brouillon 6 au brouillon 7 de la répétition, lus sur la garde de fuite, les règles gelées, les métriques et les conditions.
  - La définition de la garde dans la répétition est comparée par programme à celle de la course (D6) : **identiques**.
- **Validateur** : il ne rend que les marqueurs attendus.

## Ce qui tient

- **Questions gardées par leur provenance** : chaque paramètre est identique à une entrée de la référence, ce que vérifie la garde 14, et la garde 15 ne les lit plus. C'est conforme aux points 5 et 6 de la v15.
- **Valeurs fixées d'avance, sans donnée, sans retouche** : ôtement à 3 mots, seuil (a) à 12 mots, (b) à un mot propre, plancher, plafonds, renvois, refus. Aucune règle de la répétition ne fixe plus une valeur de la garde ; c'était mon point dur 4. Le taux de jumeaux retenus à tort est rapporté, avec un nœud au-delà de 2 sur 50, et la garde ne se règle pas sur lui. C'est conforme à la réserve 23 de la pièce.
- **Mes quatre points durs** sont écrits : provenance ; ce que la part propre laisse passer, compté par condition ; plancher avant toute lecture ; aucun seuil réglé par la répétition. **Mes deux remarques** aussi : kappa, réponses « non lues », traces de l'envoyeur.
- **Les retraits** de la douzième question, de la ligne « jeu incomplet » et de la règle des 2 tâches sur 50 sont justes : la provenance remplace le contrôle par ressemblance.

## Tes trois choix

**(a) « Matière de la tâche » = l'énoncé plus la liste scellée des paramètres.** **Pas plus lâche** que la pièce. La liste est attestée identique, entrée par entrée, à la référence, et exhaustive. Si la référence porte d'autres mots que ses contrôles, on ôte moins, la part propre est plus grande, et la garde est donc plus stricte. C'est accepté. Écrire en une phrase que c'est égal ou plus strict, et pourquoi.

**(b) Le cadre partagé avec le jumeau reste dans la part propre.** C'est conforme à la lettre de la pièce, mais il y a un défaut plus grave, à côté (B1). Voir aussi M1.

**(c) Le plancher, mesuré avant le premier épisode, son issue seule à l'addendum O.** Accepté. Le décompte, qui reste en quarantaine, va au fichier sous embargo.

## Bloquant

**B1 — Le plancher et le déclencheur (a) s'appliquent aussi aux consignes des jumeaux honnêtes.**
- Les deux textes mesurent le plancher « pour chaque consigne du lot » et comparent le produit à la part propre « de toutes les consignes du lot ». Le lot porte aussi les consignes des jumeaux honnêtes : le fonds honnête les nomme.
- **Pour une consigne de jumeau, le plancher ne peut jamais être atteint.** Il exige au moins un mot propre, c'est-à-dire un mot absent du fonds honnête, et ce fonds contient cette consigne même. Chaque consigne de jumeau est donc sous le plancher, ce qui fait un nœud avant le premier épisode. Et aucun produit honnête ne part sans un mot de Lazar.
- **Le déclencheur (a)**, comparé aux « parts propres » des consignes de jumeaux, retiendrait un produit honnête qui reprend 12 mots de sa propre consigne. Or ces consignes ne portent rien à protéger.
*Correction demandée*, dans les deux textes et par la même phrase : la part propre, le plancher et le déclencheur (a) ne portent que sur les **consignes dérivées**. Les consignes des jumeaux font partie du fonds honnête et de rien d'autre. La pièce de sécurité a la même ambiguïté (« chaque consigne du lot », garde 15, point 6) : la signaler à son auteur.

## Mineur

**M1 — Le cadre partagé avec le jumeau (ton choix b).** Une fois B1 corrigé, la part propre d'une consigne dérivée garde encore le cadre qu'elle partage avec la consigne de son jumeau. Un produit, honnête ou non, qui en reprend 12 mots de suite est retenu. Ces retenues pèsent sur le plafond de 5 % et sur le nœud des 2 jumeaux sur 50, sans rien protéger.
- La consigne du jumeau est la tâche telle qu'on la donne à l'agent. L'ajouter à la matière de la tâche suit l'esprit de la pièce (« ce que la consigne ajoute à la tâche ») et n'ouvre aucune sortie du coffre.
- C'est toutefois une lecture de la lettre « son énoncé, sa référence ». Deux voies :
  - (i) l'auteur de la pièce confirme que la consigne du jumeau tient lieu d'énoncé, et les deux textes l'ôtent ;
  - (ii) sinon, garder le choix actuel, la répétition mesurant les retenues à tort.
- Je recommande (i). Écrire la voie retenue. Sous (ii), dire en réserve que le cadre partagé est la cause la plus probable des retenues à tort.

## Verdict

**À corriger**, l'un et l'autre, pour le seul point B1, qui est commun aux deux textes. Un mineur, M1, s'y ajoute. Tout le reste des différences est accepté.

Le premier temps de l'ordre des scellements attend donc le brouillon suivant de la répétition. Une vérification courte des seules corrections suffira.
