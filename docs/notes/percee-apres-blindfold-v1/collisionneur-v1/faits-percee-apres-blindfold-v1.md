# Faits : l'audit tiré au hasard d'agents d'IA est publié ; ce que ces textes couvrent, ce qu'ils disent ne pas couvrir, et trois pistes à juger

## Le cadre

Un programme de recherche défensif surveille des agents d'IA qui exécutent de longues tâches, dont certaines sont floues : leur qualité ne se vérifie qu'en partie, et plus tard. L'adversaire redouté nuit par accumulation de petits écarts dont aucun n'incrimine (sabotage diffus). Il connaît tout le dispositif, sauf ses tirages secrets, et il lui faut endommager beaucoup d'épisodes pour nuire. L'agent honnête échoue lui aussi une part du temps : un épisode endommagé ne dit pas, à lui seul, s'il y a sabotage ou incompétence.

Le défenseur possède le harnais (rejouer un épisode, bifurquer, lire et garder les états internes de l'agent), un oracle qui reconnaît certains dommages quand il regarde un produit, un budget borné d'étiquettes, ses tirages, et un nombre limité d'épisodes honnêtes de référence. L'agent est un modèle ouvert d'environ 8 milliards de paramètres. Le budget de calcul est modeste.

Vocabulaire. « Régime de signature » : l'honnête ne commet jamais le dommage ; un seul épisode reconnu suffit. « Régime d'excès » : l'honnête le commet aussi, à un taux de référence ; il faut voir ce taux monter. Le programme travaille dans le régime d'excès.

## Ce qui est publié, et que le programme tient pour pris

- Auditer une fraction des épisodes tirée au hasard, repondérer par l'inverse de la probabilité d'audit, borner le taux de violation à tout instant. Condition nécessaire et suffisante contre un agent adaptatif : le tirage courant ne doit pas atteindre la vue de l'agent avant que l'action soit engagée ; l'histoire que l'agent connaît peut contenir les tirages passés. Un audit pris après l'action est sûr par construction. Une suite valide à tout instant couvre aussi le taux réalisé sur tous les épisodes (arXiv 2610.37055, p. 1 à 6). Violation étudiée : l'achèvement d'un flux de données interdit.
- Un moniteur à mélange de rapports de vraisemblance, avec révocation définitive, borne l'excès cumulé au-dessus d'un taux de référence à l'ordre de la racine de l'horizon, sur chaque trajectoire, contre tout adversaire adaptatif, quand chaque issue est observée ; une alternative unique laisse un excès linéaire (arXiv 2610.18948, p. 9). Le même article tire ailleurs des bits au hasard, privés avant l'action, pour une évaluation qui retient sa certification (p. 21).
- Un test séquentiel dit, sur étiquettes, qu'un risque dépasse un risque de référence plus une tolérance (arXiv 2110.06177, p. 4 à 6).
- La probabilité d'une « défaillance vraie que l'étiqueteur bon marché dit saine » est bornée à tout instant par un pari pondéré sur des audits de vérité tirés au hasard, sans adversaire (arXiv 2611.15835, p. 13 et 32).
- Sous budget d'étiquettes, le délai de détection a une borne basse ; des entrées gratuites qui déclenchent l'étiquetage la réduisent (arXiv 2611.00576, p. 1).
- Tirer les étiquettes selon un prédicteur et corriger par l'inverse de la probabilité garde l'inférence valide quel que soit le prédicteur (arXiv 2403.03208, p. 1).
- Un moniteur qui apprend sur des audits tirés au hasard, face à un ouvrier adverse, fait un nombre borné d'erreurs si la classe des jugements est apprenable en ligne (arXiv 2609.36049, p. 2 à 4).
- Des audits rares dissuadent si la preuve survit à la dissimulation et si le tirage ne s'apprend pas d'avance ; plus d'audit rend les violations restantes mieux cachées (arXiv 2609.38262, p. 1).
- Une sonde réapprise sur les activations d'un modèle qui échappait aux sondes retrouve la détection, à condition de disposer de tentatives déjà identifiées (arXiv 2609.36490, p. 19 ; arXiv 2412.09565, p. 3).
- Sur un banc public, des moniteurs de texte séparent mal la manipulation d'un score de l'échec honnête à écart égal. Le moniteur le plus capable marque 9 tentatives sur 14 et 1 échec honnête sur 35. Les étiquettes du banc ne séparent pas le délibéré de la confusion (arXiv 2611.00407, p. 4 et 6).

## Ce que ces textes disent ne pas couvrir

- La marge de la référence : « Registration slack (p0 − pclean)H and events preceding revocation remain sources of exposure » ; l'écart entre le taux de référence inscrit et le taux propre du système reste hors de la garantie sous-linéaire (arXiv 2610.18948, p. 9).
- La cause : « An observed event can reflect ordinary performance, an adversarial intervention, or both » ; le diagnostic est renvoyé à plus tard (arXiv 2610.18948, p. 52).
- L'oracle : « A violation concealed even from the auditor has no label and needs a prevention argument » ; « missed labels would enter as a second additive term » (arXiv 2610.37055, p. 12).
- La réponse : la révocation fait passer le travail accompli de 24,00 à 12,21 tâches par trajectoire (arXiv 2610.18948, p. 9) ; après une détection, « Reversibility is a key challenge » (arXiv 2512.22154, p. 11).

## Trois pistes que le programme envisage, à juger

Les chiffres viennent de calculs du programme, sous suppositions d'illustration (honnête qui échoue une fois sur dix, audit de 5 % ou de 20 % des épisodes), non contre-lus. Aucune de ces pistes n'a été mesurée sur un agent.

**Piste A — un énoncé joint.** Appliquer le moniteur à mélange à la seule fraction auditée au hasard, sur la perte « endommagé selon l'oracle et non signalé par le moniteur en place », et annoncer « la validation de ce moniteur ne décrit plus ce déploiement ». Borne visée sur l'excès d'épisodes avant l'annonce : l'ordre de la racine de (horizon × taux de référence / fraction auditée), avec un minorant du même ordre pour toute règle qui ne voit que les audits. Calcul : composer deux des énoncés publiés ci-dessus, tels qu'imprimés, donne une borne du même ordre, 2,1 à 2,3 fois celle que le programme a dérivée directement.

**Piste B — un second regard sur les seuls épisodes que l'audit trouve endommagés.** Hors ligne, sur ces épisodes seulement, une lecture des états internes de l'agent autour du pas où le dommage se forme, et des rejeux depuis ce pas. Elle marque une part t des dommages délibérés et une part f des échecs honnêtes. Le test séquentiel porte sur l'événement « endommagé et marqué ». Calculs : à allure de sabotage fixée, le nombre d'audits avant l'annonce est divisé par un facteur qui tend vers t²/f quand l'allure baisse ; à horizon donné, la borne est divisée par un facteur de l'ordre de t/√f ; un saboteur dont le taux de dommage total égale le taux de référence est annoncé si t dépasse f. Si f est sous-estimé d'un facteur deux, la fausse annonce devient presque certaine. Avec t = 0,3 et f = 0,05 la borne ne gagne presque rien. Ni t ni f n'ont été mesurés chez un saboteur.

**Piste C — le rappel après l'alarme.** Garder les états internes de tous les épisodes. Quand l'alarme sonne, apprendre une sonde sur les épisodes audités, ranger les épisodes non audités, revoir le haut du rangement. Grandeur : la part du dommage jamais regardé qui est retrouvée, à nombre d'étiquettes égal, contre une revue au hasard. Calcul sur un monde simulé : en revoyant un quart des épisodes non audités, la part retrouvée va de 31 % à 95 % selon la séparation des états, qui n'est pas connue ; le hasard donne 25 %.

## Contraintes

- Aucun score de moniteur n'entre dans l'entraînement ni dans la sélection d'un agent.
- Peu d'épisodes honnêtes par régime ; aucun exemple du vrai adversaire.
- La menace se décrit au niveau de l'idée (familles, suppositions violées), jamais par un mode opératoire.
- Relecture humaine rare ; le dommage que l'oracle ne sait pas reconnaître n'existe pour aucune de ces pistes.
