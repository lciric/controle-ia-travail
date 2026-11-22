# Question — seuil et budget d'une épreuve d'admission par « devin »

Un laboratoire fait surveiller un agent automatisé par un harnais. Ce harnais garde deux secrets : la lecture d'un détecteur interne, et la décision, tirée au sort, d'auditer ou non chaque épisode. Avant de s'appuyer sur ces secrets, le laboratoire les éprouve par un « devin ». Un prédicteur reçoit tout ce que l'agent peut observer et tente de deviner le secret.

- Le test est exact : une famille fixée d'une trentaine de prédicteurs est apprise sur une moitié des épisodes ; sur l'autre moitié, on prend le maximum de leurs statistiques et on le compare à sa loi sous le nul, obtenue par permutation des étiquettes.
- Un rejet suspend la garantie qui s'appuyait sur le secret, jusqu'à réparation du canal puis nouvelle épreuve.
- Un non-rejet ne prouve rien : il borne seulement la fuite par en bas.
- Chaque admission d'un harnais comporte **quatre courses** : deux secrets et deux cibles chacun.

Trois réglages sont sur la table. Les chiffres sont calculés à la main, sous supposition (bras équilibrés, puissance de 0,8 contre une fuite mesurée en variation totale) :

| Option | Seuil par course | Épisodes par course | Fausses suspensions d'un harnais sain, par admission | Plus petite fuite retrouvée, si la décision d'audit est tirée à pile ou face | Même chose, si l'on audite 5 % des épisodes |
|---|---|---|---|---|---|
| (a) | 0,05 | 4 000 | jusqu'à 18,5 % | environ 0,085 | environ 0,19 |
| (b) | 0,0125 | 4 000 | au plus 5 % | environ 0,094 | environ 0,21 |
| (c) | 0,05 | 8 000 | jusqu'à 18,5 % | environ 0,060 | environ 0,13 |

Dans les options (a) et (c), le seuil de 0,05 vaut pour chaque course. Dans l'option (b), il est divisé par quatre pour borner le taux par admission. L'option (c) double le budget d'épisodes.

**Ce qu'on vous demande.**
1. Choisissez une option, ou proposez-en une autre (par exemple une correction séquentielle, ou un seuil différent selon le secret). Dites pourquoi.
2. Donnez votre confiance, de 0 à 1.
3. Dites ce qui vous ferait changer d'avis : un coût, une conséquence d'une fausse suspension, une taille de fuite jugée dangereuse, une propriété du test.
4. Dites si l'unité de contrôle de l'erreur devrait être la course, l'admission ou le harnais sur toute sa vie, et ce que chacune engage.
5. Signalez toute erreur que vous voyez dans les chiffres ou dans le raisonnement, et toute antériorité qui traite ce choix (auteurs, année, titre), en disant si vous citez de mémoire.

Répondez en français, en 1 500 mots au plus.
