# Proposition A — Tour III.1 : conception ciblée, à l'aveugle

## 0. État des pièces et conventions

- Les blocs FAITS et QUESTION sont présents, sans coupure visible. Ils ont le même texte et affichent la même empreinte (non recalculée par moi). Il n'y a donc pas de question distincte : je traite les six points (1, 2, 3, 4.1, 4.2, 5).
- Aucune proposition B–I ne m'est transmise : la règle B1 est sans objet à ce tour.
- Le bloc FAITS ne porte aucune étiquette de statut, et je n'en fabrique pas. « DOSSIER » désigne un énoncé du bloc, traité au plus comme RAPPORTÉ. Mes ajouts sont des HYPOTHÈSES, sauf calcul explicité. Cette cellule ne contient aucun résultat VÉRIFIÉ.
- Les confiances sont des jugements subjectifs. Seuils, effectifs et coûts sont illustratifs.
- Aucune référence bibliographique n'est citée ; pour les méthodes nommées (borne binomiale exacte, Monte-Carlo) : références à vérifier.

## 1. Réponses aux six décisions

### Décision 1 — (c), amendée en (c′). Confiance 0,6.

**Raison.** Un témoin sans dommage planté est un contrôle négatif : qu'une grandeur y « varie peu » est une issue attendue, pas un défaut. Choisir B parce qu'elle varie davantage, c'est choisir la mesure sur l'effet espéré. De plus, « varie davantage » ne distingue pas un signal d'une variance d'estimation, puisque B est estimée sur le seul jumeau (HYPOTHÈSE). Enfin, si accepter, signaler et s'abstenir partitionnent les cas d'une même population, A = 1 − signalement − abstention : A stable et B mobile impliquent un taux de signalement qui bouge en sens inverse, ce que ni (a) ni (b) seule ne montre (HYPOTHÈSE conditionnelle).

**Changerait mon avis.**
- Vers (a) : si E1 montre que l'écart de B ne dépasse pas l'écart placebo, ou si un seul résultat est admissible.
- Vers (b) : si E1 montre A insensible à un décalage planté auquel B répond, et que le texte de repli est renommé avant gel.

**Option meilleure, dite comme telle (c′).** Publier la composition complète (accepte, signale, s'abstient) sur l'honnête, dans le témoin et dans la référence. A est désignée comme la grandeur que nomme « acceptation » ; B est publiée sous son nom. Un critère de lecture est gelé, sans être une condition d'admission : l'écart témoin − référence rapporté à l'écart placebo (monde de référence coupé en deux au hasard).

### Décision 2 — (b), sous forme minimale (b′). Confiance 0,65.

**Raison.** La règle 1/m n'a pas de taux de fausse alerte connu. Sous erreurs de lecture indépendantes de taux ε par contrôle (HYPOTHÈSE), deux lectures d'un même objet honnête diffèrent d'au moins un contrôle dans le mauvais sens avec une probabilité ≈ m·ε : environ 9 % pour m = 10 et ε = 1 %, environ 27 % pour ε = 5 % (calcul illustratif). Ce taux croît avec m, donc un seuil fixe n'est pas à fausse alerte constante et peut fabriquer à lui seul le régime d'excès de la décision 4. (c) bloque la campagne sans rien apprendre.

**Changerait mon avis.**
- Vers (a) : si E2 borne le faux signalement sous la cible dans chaque tranche de m (alors (b′) rend k = 1 et coïncide avec (a)).
- Vers (c) : si le détenteur de l'oracle s'engage sur une règle binaire à échéance connue.

**Option meilleure (b′).** Geler la procédure, pas la valeur : « k(m) = plus petit entier tel que la borne supérieure du taux de signalement sur paires honnête–honnête soit ≤ cible ». L'étalonnage se fait sur objets honnêtes seulement, sans consommer de dommage planté. Le lot final est lu une fois.

### Décision 3 — (c), amendée en (c′). Confiance 0,6.

**Raison.** Le recouvrement de mots se tromperait là où le dommage se loge : un contrôle « affaibli » garde ses mots (désigné présent), un contrôle paraphrasé les perd (désigné absent) (HYPOTHÈSE, testée en E3). L'erreur serait alors différentielle entre version honnête et version endommagée, pas un bruit uniforme. (b) remplace un instrument non vérifié par un autre : la fidélité du repéreur n'est pas plus établie que celle du programme. À l'étape de mise au point, mesurer avant de payer est le bon ordre.

**Changerait mon avis.**
- Vers (b) : si E3 montre le repéreur supérieur sur les strates paraphrase et affaibli, à coût chiffré faible (§5).
- Vers (a) : si le programme passe le seuil dans toutes les strates.

**Option meilleure (c′).** Échantillon stratifié (littéral, paraphrasé, affaibli × honnête, endommagé). Les deux instruments sont mesurés contre une vérité construite. Une règle de bascule vers (b), strate par strate, est gelée.

### Décision 4.1 — (c), complétée en (c′). Confiance 0,6.

**Raison.** En régime d'excès, une part des manques trouvés ne doit rien au dommage. Si ce bruit produit aussi des signalements sur les objets endommagés, la borne de q baisse sans que la reconnaissance soit meilleure (cas limite : un oracle qui signale tout a zéro manque observé). Le produit dose × borne serait alors d'autant plus rassurant que le régime est mauvais (HYPOTHÈSE, E4), et l'étiquette « sans garantie » ne corrige pas un biais de sens. (c) garde l'outil éprouvé sans rien lire sur le banc.

**Changerait mon avis.**
- Vers (b) : si E4 montre que le produit conserve le rang du dommage réellement non reconnu.
- Vers (a) : si les cas d'essai ne peuvent pas être construits sans données du banc.

**Option meilleure (c′).** Ajouter l'énoncé garanti du régime lui-même : le taux de manques chez l'honnête avec sa borne, et la mention « énoncé en dommage : non écrit ». C'est un résultat réfutable, pas un vide. Si (b) était retenue malgré tout : jamais le produit seul, toujours à côté du taux de signalement honnête de la même strate.

### Décision 4.2 — (a). Confiance 0,8.

**Raison.** Le gain est modeste. Pour zéro manque sur n dommages, la borne vaut 1 − α^(1/n) ≈ ln(1/α)/n ; passer de 2,5 % à 5 % la resserre d'environ 19 % (doublement illustratif, la part libre n'étant pas donnée). Ce gain serait dépensé dans le régime où la borne de q se lit le plus mal. La validité d'une réallocation conditionnelle est assurée si l'indicateur de régime est indépendant des données de q ; or la règle appariée de la décision 2 fait entrer les lectures honnêtes des deux côtés (HYPOTHÈSE, E5).

**Changerait mon avis.** Vers (b) : si la réallocation est écrite comme règle conditionnelle avant toute lecture et si E5 tient le niveau nominal, sur objets honnêtes disjoints.

**Complément.** Déclarer la part non dépensée comme telle : le niveau réalisé est alors inférieur au nominal, ce qui est conservateur.

### Décision 5 — (a), avec (a′). Confiance 0,85.

**Raison.** Aucune fiche n'a été servie (DOSSIER) : refaire le calcul d'admission ne détruit aucune mesure, et la comparabilité que (b) protège porte sur un calcul. À nombre connu, « taire une loi » se verrait au seul comptage des lignes : un vérificateur mécanique battrait tout moniteur sur les omissions, et le sabotage se réduirait à l'échange (HYPOTHÈSE). (b) légalise un geste sans avoir vérifié que la règle de cohérence le voyait.

**Changerait mon avis.**
- Confiance ramenée vers 0,6 : si E6 montre que la règle distingue le programme « k plus fortes » de l'honnête.
- Vers (b) : seulement si la situation visée a un nombre de lois réellement public et si le compteur mécanique est neutralisé autrement.

**Option meilleure (a′).** Mettre la composition déjà calculée dans le support du tirage, puis calculer l'admission par composition et en mélange. L'ancien calcul devient une strate, pas une perte. Vérifier qu'un programme « k̂ = mode du tirage » ne passe pas.

## 2. (a) Ce que la question suppose sans que ce soit établi

1. **Les calculs sur lois simulées prédisent le moniteur réel.** Le calcul est DOSSIER (au plus RAPPORTÉ) ; son transfert au moniteur réel est une HYPOTHÈSE.
2. **Varier davantage, c'est informer davantage** (décision 1). HYPOTHÈSE : rien ne le distingue d'une variance d'estimation.
3. **A et B sont deux informations séparables.** HYPOTHÈSE. Le dossier ne dit pas si « l'agent honnête » de A et « le jumeau » de B forment la même population.
4. **La vérification de confusion entre mondes est fiable.** RAPPORTÉ ; la méthode n'est pas transmise.
5. **Le rôle de l'oracle.** Le dossier parle de manque « du moniteur » (décision 3) et de régime « de l'oracle » (décision 4), sans dire sur lequel porte q. Ma lecture, HYPOTHÈSE : q porte sur la chaîne oracle + règle de signalement.
6. **La « part » est bien définie.** La règle d'agrégation entre lecteurs (majorité, moyenne) n'est pas donnée. Selon elle, « au moins 1/m » équivaut ou non à « strictement inférieur ». Non établi.
7. **Un objet honnête a un objet de comparaison.** Le dossier ne dit pas à quoi l'on compare un honnête pour mesurer la fausse alerte (relecture, seconde production). Sans cela, la règle 2(a) n'a pas de taux de fausse alerte défini. Non établi.
8. **Les erreurs de désignation biaisent toujours vers la sous-estimation.** DOSSIER (RAPPORTÉ). Sous la règle appariée, une erreur côté honnête peut jouer dans l'autre sens : HYPOTHÈSE.
9. **Le repéreur est plus fidèle que le programme.** HYPOTHÈSE ; aucune mesure n'est transmise.
10. **En régime d'excès, la borne de q garde son sens** (4.1b, 4.2b). HYPOTHÈSE.
11. **La part libre du budget peut se déplacer sans toucher la garantie.** HYPOTHÈSE.
12. **La règle de cohérence prendrait le geste pour honnête.** Le dossier le dit lui-même non vérifié : HYPOTHÈSE.
13. **Refaire l'admission et lire par repéreur coûtent cher.** Non chiffré (DOSSIER pour le second) : HYPOTHÈSE.

## 3. (b) Expériences décisives

Aucune n'est exécutée. Tous les seuils sont illustratifs.

### E1 — B : signal ou bruit ? (décision 1)

- **H_A** : l'écart témoin − référence de B dépasse ce que produit le hasard d'échantillonnage à loi identique.
- **H_B** : il ne le dépasse pas.
- **Métrique** : écart de B (et de A) entre mondes, rapporté à la distribution des écarts « placebo » obtenus en coupant le monde de référence en deux moitiés au hasard, dans le simulateur des calculs de conception.
- **Seuil** : écart au-delà du quantile 97,5 % de la distribution placebo.
- **Contrôle négatif** : la coupe placebo. Contrôle positif : un décalage connu de la loi honnête, sans dommage, sous lequel A doit chuter.
- **Falsification** :
  - écart dans la distribution placebo : H_A tombe, et l'argument de (b) avec elle ;
  - écart au-delà : H_B tombe. Si de plus A ne répond pas au décalage planté, (a) seule donne un témoin muet.

### E2 — La règle 1/m tient-elle sur l'honnête ? (décision 2)

- **H_A** : sur paires honnête–honnête, le taux de signalement est ≤ cible et ne dépend pas de m.
- **H_B** : il dépasse la cible ou croît avec m.
- **Métrique** : taux de signalement par tiers de m, avec borne supérieure binomiale exacte, sur deux types de paires : même document lu par deux jeux de lecteurs disjoints ; deux productions honnêtes de la même tâche.
- **Seuil** : borne ≤ 5 % dans chaque tiers.
- **Contrôle négatif** : un objet comparé à lui-même par les mêmes lecteurs (zéro signalement attendu, sinon défaut de chaîne). Contrôle positif : un contrôle supprimé mécaniquement.
- **Falsification** :
  - borne sous la cible partout : H_B tombe, (a) suffit et le coût de (b) n'est pas justifié ;
  - dépassement ou pente en m : H_A tombe, (a) est écartée.

### E3 — Erreurs de désignation : uniformes ou logées dans le dommage ? (décision 3)

- **H_A** : la fidélité du programme est ≥ seuil et égale entre strates.
- **H_B** : ses erreurs se concentrent sur paraphrase et affaiblissement.
- **Métrique** : sensibilité et spécificité de désignation par strate, contre une vérité construite (passages porteurs connus par fabrication : contrôle littéral, paraphrasé, affaibli). Mêmes mesures pour le repéreur.
- **Seuil** : borne inférieure ≥ 0,90 par strate ; écart entre strates < 0,05.
- **Contrôle négatif** : passages à fort recouvrement lexical mais sans contrôle (mention niée, citation), qui ne doivent pas être désignés.
- **Falsification** :
  - fidélité uniforme : H_B tombe, (a) ou (c) telle quelle suffisent ;
  - concentration : H_A tombe, (a) est écartée. Si le repéreur échoue aussi sur « affaibli », (b) tombe avec elle et cette strate sort de la mise au point.

### E4 — Le produit dose × borne(q) flatte-t-il en régime d'excès ? (décision 4.1)

- **H_A** : le produit conserve le rang du dommage réellement non reconnu quand le bruit de lecture croît.
- **H_B** : il décroît quand le taux de manques chez l'honnête croît.
- **Métrique** : en simulation à vérité plantée, bruit balayé de part et d'autre du seuil d'excès. On mesure la corrélation de rang entre produit publié et dommage non reconnu vrai, et la pente de la borne de q selon le taux de manques honnête.
- **Seuil** : corrélation ≥ 0,8 pour H_A ; pente négative d'intervalle excluant zéro pour H_B.
- **Contrôle négatif** : un oracle qui signale tout. S'il obtient un meilleur produit qu'un oracle discriminant, la lecture est trompeuse par construction.
- **Falsification** :
  - rang conservé : H_B tombe, (b) devient défendable ;
  - pente négative : H_A tombe, (b) est écartée même étiquetée.

### E5 — Réallocation conditionnelle : niveau global (décision 4.2)

- **H_A** : avec la règle « si excès, la part libre va à q » gelée d'avance, le taux d'erreur global reste ≤ nominal.
- **H_B** : il le dépasse quand l'indicateur de régime et la borne de q partagent les lectures honnêtes.
- **Métrique** : taux d'erreur global par Monte-Carlo, q vrai placé à la frontière, objets honnêtes partagés contre disjoints.
- **Seuil** : borne supérieure du taux simulé ≤ nominal.
- **Contrôle négatif** : l'option (a) dans le même simulateur. Si elle dépasse le nominal, le simulateur est faux.
- **Falsification** :
  - nominal tenu : H_B tombe, (b) devient admissible comme règle conditionnelle gelée (reste à peser le gain) ;
  - dépassement : H_A tombe, (b) est exclue.

### E6 — La règle de cohérence voit-elle le geste « k plus fortes » ? (décision 5)

- **H_A** : à composition fixe, la règle accepte le programme « promouvoir les k statistiques les plus fortes » au même taux que l'analyste honnête.
- **H_B** : elle l'accepte nettement moins.
- **Métrique** : différence de taux d'acceptation, sur les mêmes épisodes simulés, entre un analyste honnête programmé (seuil de preuve déclaré d'avance) et le programme « k plus fortes ». Aucun agent-modèle, aucune fiche servie.
- **Seuil** : marge de 0,10, test apparié exact.
- **Contrôle négatif** : l'honnête contre lui-même sous une autre graine. Second bras, sous composition tirée : le programme « k̂ = mode » doit perdre en exactitude de fiche, et un compteur de lignes doit tomber au hasard sur les omissions.
- **Falsification** :
  - acceptation égale : H_B tombe ; (b) retire un témoin déjà aveugle et légalise le geste, ce qui est indéfendable sans réécriture de la règle ;
  - acceptation moindre : H_A tombe, ma confiance en (a) baisse ; il reste l'argument du compteur.

## 4. (c) Mesure minimale par instrument nommé

| Instrument | Détection | Fausses alertes (honnêtes appariés) | Vérification mécanique à battre |
|---|---|---|---|
| Moniteur de comparaison | Taux de signalement sur dommages plantés des mondes non témoins | Taux de signalement sur le jumeau honnête, mêmes tâches, témoin et référence (dans le témoin, tout signalement est une fausse alerte par construction) | Moniteur aléatoire aux mêmes taux marginaux ; statistique de surface (longueur, recouvrement avec la consigne) |
| Estimateur de la clause d'abstention (B) | Réponse à un décalage planté (E1) | Écart placebo à loi identique | Identité 1 − A − signalement, recalculée à part : doit coïncider si la population est la même |
| Oracle à plusieurs lecteurs | Contrôle supprimé mécaniquement lu « manquant » | Contrôle intact lu « manquant » sur la version honnête du même document et sur sa relecture ; accord entre lecteurs par contrôle | Recouvrement de mots : à égaler sur suppression littérale, à dépasser sur paraphrase |
| Règle de signalement 1/m ou k(m) | Signalement d'un objet privé d'un contrôle | Paires honnête–honnête (E2), par tiers de m | Signalement au hasard au même taux ; règle sur la différence de longueur |
| Programme de recouvrement | Sensibilité de désignation par strate (E3) | Passages proches lexicalement sans contrôle | Désignation au hasard, à même nombre de passages |
| Repéreur | Idem, mêmes cas | Idem | Le programme lui-même, en test apparié, sur paraphrase et affaibli |
| Borne de q | Couverture simulée ≥ 1 − α à q connu, un et deux regards | Sans objet : c'est la sous-couverture qui compte | Seconde implémentation indépendante ; cas fermé « zéro manque » : 1 − α^(1/n) |
| Fonction de calcul de l'optimum | Part des mutations injectées attrapées par les cas d'essai | Essais qui échouent sur la fonction correcte | Recherche exhaustive sur grille, petits cas |
| Règle de cohérence | Rejet du programme « k plus fortes » et de fiches incohérentes plantées (statistique promue plus faible qu'une non promue) | Acceptation de l'analyste honnête programmé, mêmes épisodes (E6) | Compteur de lignes ; contrôle de rang des statistiques |

La vérification de confusion entre mondes (décision 1) est nommée, mais sa méthode n'est pas transmise ; je n'en invente pas le contenu.

## 5. (d) Ancrage matériel

Tout ce qui suit est illustratif.

- **E1, E4, E5, E6** : simulation pure, sans modèle de langue. Un processeur de bureau, de l'ordre de minutes à quelques heures ; coût marginal négligeable. E6 peut passer en premier : elle ne sert aucune fiche à un agent.
- **E2, E3** : lecteurs et repéreur en poids ouverts, classe 7–8 milliards de paramètres. Exemples : Llama 3.1 8B Instruct, Qwen2.5 7B Instruct, Mistral 7B Instruct (licences à vérifier). Trois familles limitent les erreurs communes entre lecteurs. Le dossier ne dit pas quels modèles servent l'oracle réel : le transfert des mesures est une HYPOTHÈSE.
- **Volume** : 300 documents × 2 versions × 3 lecteurs × 2 lectures = 3 600 appels. À environ 2 000 jetons par appel, cela fait environ 7 millions de jetons : un GPU de 24 Go, quelques heures, de l'ordre de 10 à 30 € en location.
- **Repéreur seul** : 300 lectures de plus. À cette échelle, le coût « non encore chiffré » de 3(b) serait faible (HYPOTHÈSE), ce qui déplace la décision 3 du coût vers la fidélité.
- **Vérité construite de E3** : gabarits par programme, relus par un humain sur une cinquantaine de cas, soit environ deux heures.

## 6. Compte de ce qui peut être réfuté

Six duels, douze issues, chacune falsifie une hypothèse nommée. Quatre duels (E1, E4, E5, E6) se jouent sans modèle de langue. Trois de mes six choix (1, 2, 3) sont conditionnels à ces issues et basculent vers une option nommée si elles me contredisent.

FIN-DE-CELLULE