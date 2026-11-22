# Papier « dopamine », étape 1 exploratoire — seconde instance : arrêt sur la garde de la vérité plantée (2026-11-22T13:24:39Z, `date -u`)

**EXPLORATOIRE, non opposable** (GO-2026-11-21-44). Aucune revendication. Classe C.

## Verdict
La chaîne a marché de bout en bout, de la génération au noyau. Le noyau s'est arrêté sur sa garde de vérité plantée. Dans chacun des cinq plis, la sonde lit l'issue plantée sans faute (aire 1,0). Mais la garde lit l'aire des scores mis en commun entre les plis, et celle-ci vaut 0,813 (intervalle à 95 % : 0,781 à 0,843, sous le seuil de 0,9). Ce n'est pas une panne de la chaîne : c'est la lecture de la garde (scores mis en commun ou plis pris un par un) qui doit être tranchée par son concepteur. Machine détruite par son identifiant, tout est versé.

## Faits (pièces sur donnees/dopamine-exploratoire-v1, commit a9296c52)
- Course 20261122-124749-dopamine-exploratoire-v1-etape-1, instance 61972365, offre 29296808. Créée à 12:50:35Z, détruite à 13:23:21Z, absente de l'inventaire relu.
- Tranche de mesure (32 questions), sans arrêt : 0 réponse au plafond, longueur moyenne 763 jetons, 10 réussites, 4 réponses sans boîte, 64 s.
- Génération (500 questions, 613 s) : 187 réussites (37,4 %), 1 au plafond, longueur moyenne 808 jetons, **100 réponses sans boîte (20 %)**, 4 désaccords en égalité stricte.
- Noyau, vérité plantée (couche 3, force 4, 249 issues plantées, graine 0) : aire 1,0 dans chacun des cinq plis, et 0,813 sur les scores mis en commun. Les scores ne prennent qu'une poignée de valeurs par pli (de 0,36 à 0,51 environ) : chaque pli a son propre niveau, et mettre les plis en commun brouille l'ordre.
- Pièces : diag/<course>/etape1-{tranche,generation,noyau-arret}-exploratoire.json ; 32 lots de générations, de notation et d'index d'états ; états de la position de lecture aux couches 2 à 4 ; 5 sondes de la vérité plantée. Le journal de la machine est versé ici : docs/notes/papier-dopamine-moniteur-v1/exploratoire/course-20261122-124749-arret-verite-plantee-v1/.
- Coût : environ 0,7 USD pour cette instance (0,55 h à 1,188 USD/h, réseau en plus). L'écart du crédit, 18,04 → 14,99 USD, compte aussi les deux autres instances du compte. Cumul du bras sous GO-41 : 3,82 USD au plus.

## Décision à porter (conception de Fable : critère de la garde)
Décision en une phrase : sur quoi la garde de vérité plantée du noyau lit-elle son seuil de 0,9 ?
- (a) La moyenne des aires par pli, comme le chiffre du papier (champ « aire_papier_moyenne_des_plis », 1,0 ici). Avantage : c'est ce que le papier rapporte et ce que la chaîne doit prouver. Inconvénient : l'aire mise en commun, qui sera lue plus tard, reste non contrôlée.
- (b) Garder l'aire mise en commun, mais après un recalage des scores pli par pli, par rangs dans chaque pli. Avantage : contrôle la lecture commune. Inconvénient : du code neuf, à contre-lire, et le recalage est un choix d'analyse.
- (c) Les deux : l'arrêt seulement si la moyenne par pli est sous 0,9 ; la lecture commune rapportée à côté. Avantage : ne bloque pas une chaîne saine et ne cache rien.
Recommandation : (c), confiance moyenne. C'est à faire écrire par Fable (critère de décision), puis code et essais par Opus, contre-lecture, relance sous le reste de GO-41 (environ 6 USD). Les générations et les états versés permettent peut-être de rejouer le noyau au processeur sans regénérer (les états de toutes les positions ne sont pas versés : à vérifier).

## Réserve
Les 100 réponses sans boîte (20 %) méritent un regard avant la lecture du chiffre publié. L'invite est la lecture « qwen-boxed » du plan ; le taux de réussite (37,4 %) est à lire contre le chiffre publié sur ce modèle, sans conclusion ici.

## Prochaine action
Attendre ta décision sur la garde. Aucune instance de ce bras en marche.
