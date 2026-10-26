# Question pour un tour du collisionneur — méta-structure de l'organisme (brainstorm et relecture) — v1 (brouillon de conv-audit ; session-depot fige sa version)

Écrit par conv-audit le 26 octobre 2026 (mots de Lazar, 18:17 et 18:19 heure de Paris : « lance le grand collisionneur
dessus pour qu'il brainstorme et relise » ; « je veux un brainstorm sur la méta-structure de l'organisme »). Forme
« arbitre », trois modèles, une tentative par cellule, refus consignés tels quels.

## Question

« Un organisme de recherche automatique (code Python pur fourni en faits : moissonnage d'articles, tri par recouvrement
lexical, mémoire spectrale par décomposition en valeurs singulières incrémentale sur des vecteurs hachés, répulsion des
termes saturés, castes contradictoires, archive d'hypothèses) doit être refondu pour maximiser la fertilité de ses
associations d'idées inter-domaines — des associations qui mènent à des hypothèses testables à bas coût, pas des
chimères verbales. Un rapport de refonte (fourni) propose quatre briques : encodage par SimHash sur n-grammes avec
normalisation avant relèvement non linéaire ; tirage conjoint par processus ponctuel déterminantal avec équilibrage de
Sinkhorn ; répulsion déplacée sur les paires de concepts pour préserver les termes-ponts ; fusion de deux articles sur
leur interface commune sous filtre de compatibilité des contraintes. Une relecture critique (fournie) conteste deux de
ces briques sur le plan mathématique.

1. Relis les quatre briques et la relecture : où la relecture a-t-elle raison, où a-t-elle tort, et qu'est-ce que les
   deux ont manqué ?
2. Brainstorm : propose d'autres lois de tirage et d'autres mémoires (trois au plus chacun, un paragraphe par
   proposition) qui maximisent les associations fertiles sous les contraintes dures : Python pur sans dépendance, corpus
   de 12 à 50 résumés courts par génération, aucun score de course ne peut servir de récompense, critère d'arrêt à
   re-étalonner si l'encodage change.
3. Pour chaque proposition gardée : le test sur processeur qui la départagerait (métrique, nul, seuil qui peut échouer),
   et ce qui la réfuterait. »

## Faits à servir

- Le code de la v6.2.1 : `principal.py`, `memoire_isvd.py`, `mitose_spectrale.py` (commit `7ea3270`).
- Le rapport de méta-conception (`96d12112…`, commit `5512513`).
- La relecture de conv-audit (`relecture-meta-conception-v6-3-v1.md`, empreinte au compagnon).
- À la discrétion de session-depot : les verdicts des essais a et b s'ils sont rendus avant le tour.

Aucun élément confidentiel dans ces pièces (vérifier avant de servir : le rapport de méta-conception est propre ; les
chemins de dossiers de la branche de Gemini qui portent le sigle du financeur ne doivent pas apparaître dans les faits —
servir les fichiers copiés sous des noms neutres).
