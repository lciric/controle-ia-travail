# Question — seuil et budget d'une épreuve d'admission par prédicteur adverse

Un laboratoire fait surveiller un agent automatisé par un dispositif de surveillance. Ce dispositif garde deux secrets : la lecture d'un détecteur interne, et la décision, tirée au sort, d'auditer ou non chaque épisode. Avant de s'appuyer sur ces secrets, le laboratoire les éprouve avec un prédicteur adverse : celui-ci reçoit tout ce que l'agent peut observer et tente de deviner le secret.

- Le test est exact. Une famille fixée d'une trentaine de prédicteurs est apprise sur une moitié des épisodes. Sur l'autre moitié, on prend le maximum de leurs statistiques et on le compare à sa loi sous le nul, obtenue par permutation des étiquettes.
- Un rejet suspend la garantie qui s'appuie sur ce secret jusqu'à une nouvelle épreuve.
- Un non-rejet n'établit pas l'absence de fuite. Il indique seulement qu'une fuite plus grande que la plus petite fuite retrouvée aurait probablement été détectée.
- Chaque admission d'un dispositif comporte quatre tests : deux secrets, deux cibles par secret.

Trois réglages sont sur la table. Les chiffres sont calculés à la main, sous supposition : bras équilibrés, puissance de 0,8 contre une fuite mesurée en variation totale.

| Option | Seuil par test | Épisodes par test (moitié apprentissage, moitié épreuve) | Fausses suspensions d'un dispositif sain, par admission | Plus petite fuite retrouvée, décision d'audit tirée à pile ou face | Même chose, 5 % des épisodes audités |
|---|---|---|---|---|---|
| (a) | 0,05 | 4 000 | 18,5 % sous indépendance des tests | environ 0,085 | environ 0,19 |
| (b) | 0,0125 | 4 000 | 4,9 % sous indépendance des tests | environ 0,094 | environ 0,21 |
| (c) | 0,05 | 8 000 | 18,5 % sous indépendance des tests | environ 0,060 | environ 0,13 |

Seuils : options (a) et (c), 0,05 par test, sans correction ; option (b), 0,05 divisé par quatre (correction de Bonferroni sur les quatre tests). Budget : 4 000 épisodes par test pour les options (a) et (b), 8 000 pour l'option (c).

**Ce qu'on vous demande.**
1. Choisissez une option, ou proposez-en une autre. Dites pourquoi.
2. Donnez votre confiance, de 0 à 1.
3. Dites ce qui vous ferait changer d'avis : un coût, une conséquence d'une fausse suspension, une taille de fuite jugée dangereuse, une propriété du test.
4. Dites si l'unité de contrôle de l'erreur devrait être le test, l'admission ou le dispositif sur toute sa vie, et ce que chacune engage.
5. Signalez toute erreur que vous voyez dans les chiffres ou dans le raisonnement, et toute antériorité qui traite ce choix (auteurs, année, titre), en disant si vous citez de mémoire.

Répondez en français, en 1 500 mots au plus.
