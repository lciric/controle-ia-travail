# Réponse de conv-audit à la question 4 (apprendre concepts, dimensions, chapelles, hypergraphe, paramètres de la fertilité) — version 2

- Version 2, 31 octobre 2026, 01:25 à 02:10 heure UTC, sous-agent neuf Opus 5.5 (lignée conv-audit), auteur ni de la v1, ni des relectures, ni de la synthèse. La v1 reste intacte ; erreurs dans `erratum-reponses-v1-v1.md`.
- Niveau méthode ; aucune décision. Statuts comme en réponse 1 v2.
- Pièces intégrées (sha256sum) :
  - `question-4-apprendre-v1.md` — `d051c7bdce39c809465b6d227ca1869eff3afc38f1594c0a8ad6be041113be09`
  - `reponse-conv-audit-question-4-v1.md` — `69ca070747e5a3a7fb64935d32e631fb45fe1aafd5e0ef82376df0b0e90db927`
  - `relecture-fable-reponse-4-v1.md` — `8d04cc131fd20478972f15165df6257bb3c69ae1929d66ca4a75c751c7aed933`
  - `reponse-fable-independante-question-4-v1.md` — `b72fda876b498b21a3430a5cc807621fc875ee412241859b3848a056dc44c3a4`
  - `revue-biblio-fertilite-v1.md` — `307b4f2fe6e53dcfa517c6da5d2591a6cee1e1508cd8197f4778fe014d6b718f`
  - réponse d'Argon (commit `b1a21a07`) — `c2a991060f0ef87887e97e482009a754121ce29415d1f2a2159df24d35159ed7`
  - synthèse v2 du collisionneur — `23c2888ddd924b85a0bbd0009a17f64723399d69ffd17669f56c4fddf7d18a86`
  - `docs/sources/pdf/bisociation-fertilite-v1/arxiv-2402.08640-gu-krenn-2024.pdf` (empreinte vérifiée par son compagnon ; page 1 lue)
  - `registres/decisions.md`, lignes R-626, R-669.

## Réponse courte

Oui, on peut apprendre la représentation (concepts, chapelles, distance) plutôt que la décréter, mais la tâche « prédire les liens futurs d'un graphe de concepts sous coupure » est **occupée** (Krenn et collègues 2023 ; Gu et Krenn 2024, aire sous la courbe au-delà de 0,9). Ce qui peut être propre au programme : apprendre **dans cet ordre, chaque étage gelé avant le suivant**, la partition en chapelles (variables latentes d'un modèle de blocs), une fonction de fertilité à étiquette gelée, puis la loi ; et montrer qu'elle bat le modèle **« popularité seule »**. Une transition se lit sur le **taux empirique**, jamais sur la sortie du modèle.

## Ce qui change par rapport à la v1

| Constat | Sort | Correction |
|---|---|---|
| RL4-01 Gu et Krenn 2024 occupe la zone « fertilité calibrée » | accepté | Référence à battre ; vérifié sur PDF (p. 1). La nouveauté revendiquée se réduit (voir RL4-13). |
| RL4-02 « reprise d'une paire » et « lien futur » confondus ; étiquette non définie | accepté | Étiquette gelée : lien apparu **et** repris par un tiers hors des deux niches au-delà d'un seuil, à horizon fixe (réponse 3 v2, section 1). |
| RL4-03 transition cherchée dans la fonction apprise (sigmoïde) | accepté | Lue sur le taux empirique par classe du paramètre de contrôle, avec témoins sur toute la plage. |
| RL4-04 pas de critère de mort, pas de référence, pas de témoin « popularité seule » | accepté | Ci-dessous. |
| RL4-05 fuites par étiquettes assignées après coup et par croissance du réseau | accepté | Concepts extraits par une méthode datée, vocabulaire figé avant la coupure ; calibration refaite par fenêtre. |
| RL4-06 tests de mort rangés hors de nous | accepté | Retirés de « hors de nous » ; restent le futur, les bancs publics et la reproduction par un tiers. |
| RL4-07 témoins durs sans antériorité ; aire sous la courbe trompeuse sous déséquilibre | accepté | Poursafaei et collègues 2022 (témoins historiques et inductifs) ; aire sous la courbe précision-rappel et précision dans les k premiers, k fixé par le budget du bisociateur. |
| RL4-08 hyperarêtes (Benson 2018) et inférence conjointe hyperarêtes et communautés non citées | accepté | Cités ; voir la divergence avec Fable plus bas. |
| RL4-09 goulot de concepts, régression symbolique, découverte fondée sur la littérature sans antériorité | accepté | Nommés, SUPPOSÉ. |
| RL4-10 « Arrowsmith » | accepté | « Les redécouvertes de Swanson, utilisées comme étalon. » |
| RL4-11 bornes « 2015-2021 » de Science4Cast non confirmées | accepté | Retirées jusqu'à lecture du PDF. |
| RL4-12 transfert sans protocole | accepté | Entraîner sur un champ, tester sur un autre, perte tolérée gelée. |
| RL4-13 nouveauté « apprendre la représentation » trop large | accepté | Sourati-Evans et Krenn apprennent déjà des plongements ; la nouveauté défendable est l'apprentissage par étages gelés, sous préenregistrement. |
| Synthèse : la « domination par la centralité » de Gu-Krenn est sans source (seule Argon l'affirme) | accepté | Je ne l'affirme pas ; c'est une question que E6′ tranche. |
| Synthèse : au-delà d'une distance de 3, les voisins communs sont nuls par construction (T2-C) | accepté | La référence locale ne peut pas servir dans cette strate ; on garde le produit des degrés (T3-A). |

## 1. Trois apprentissages, dans l'ordre

1. **Structure.** L'hypergraphe est **observé** : chaque article est une hyperarête sur ses concepts, auteurs, méthodes, objets (réponse Fable indépendante 4, point 5). Ce qui est caché, c'est la **partition** : les chapelles sont les blocs d'un modèle de blocs stochastiques sur hypergraphe, sélectionné contre un modèle nul à degrés conservés. Gelée avant l'étage suivant.
2. **Fonction.** Probabilité, pour une paire de chapelles, de l'étiquette gelée ; sortie calibrée par fenêtre (la croissance du réseau change le taux de base).
3. **Loi.** Forme de la relation entre la fonction et un paramètre de contrôle : droite, seuil ou cloche, lue sur le taux empirique. Gelée avant toute lecture du test.

Un jeu de test distinct par étage ; sinon les degrés de liberté s'additionnent sans contrôle (relecture 4, section c).

## 2. Deux voies, retenues par Lazar

- **Goulot de traits nommés puis ablation** : canal, structure commune, désaccord, densité de contacts, popularité. Argon propose d'y ajouter la courbure d'arête et la modularité : candidats, non testés.
- **Apprentissage libre puis régression symbolique** : la loi extraite est descriptive ; elle est jugée à part (seuil proposé par C au collisionneur : coefficient de détermination ≥ 0,85, T3-C duel 3).

## 3. Fuites et témoins

- Plongements préentraînés après la coupure ; étiquettes OpenAlex et intentions de citation assignées par des modèles postérieurs : à exclure ou à mesurer.
- Témoins appariés en taille, âge, croissance, jamais reliés après la coupure ; **jamais** appariés sur la variable testée (synthèse, A).
- Deux granularités au moins : un signal qui ne tient qu'à un découpage dépend du découpage (Fable 4).

## 4. Gu et Krenn dans le bisociateur, dès maintenant ?

C'est l'objet de **E6′** : mesurer le gain conditionnel de leur score au-dessus de « popularité seule », dans la strate de distance supérieure à 3, là où le bisociateur veut aller. Tant que E6′ n'est pas fait, l'utiliser comme proposeur de paires n'est pas justifié. Un échec de reproduction **suspend**, il ne falsifie pas (T2-A, accepté par D). Coût : nul selon A, 300 à 1 000 € de carte graphique selon B (synthèse, décision proposée n° 3 : vérifier d'abord le code sur processeur ; dépense = nœud, non tranché ici).

## Convergences et divergences avec la réponse Fable indépendante 4

- **Convergent** : reproduire avant de battre ; battre voisins communs, Adamic-Adar, attachement préférentiel sur négatifs difficiles ; témoins appariés ; fuites temporelles ; paramètre d'ordre et de contrôle nommés avant de parler de transition ; effondrement par taille comme critère externe.
- **Divergent** : Fable dit « ne pas identifier l'hypergraphe : il est donné » ; la relecture 4 recommande l'inférence conjointe d'hyperarêtes et de communautés (Contisciani, Battiston, De Bacco 2022, SUPPOSÉ). Les deux tiennent : l'hypergraphe des articles est observé ; une structure d'ordre supérieur entre chapelles peut être inférée. Fable ajoute une **cible de rupture** distincte (indice de disruption) parce qu'un prédicteur de liens apprend la conformité : retenu.
- **Argon** : témoins appariés par score de propension sur l'activité marginale ; évaluation hors période avec précision dans les k premiers à distance supérieure à 4 : cohérent avec E6′.

## Antériorités

| Auteur, année | Support | Statut |
|---|---|---|
| Gu et Krenn 2024 (2402.08640) | prépublication, version 4 | **vérifié sur PDF**, p. 1 |
| Krenn et collègues 2023 (Science4Cast) | arXiv 2210.00881 | notice seulement |
| Krenn et Zeilinger 2020 | *PNAS* | notice seulement |
| Sourati et Evans 2023 ; Shi et Evans 2023 | revues | page en ligne (revue v1) |
| Benson, Abebe, Schaub, Jadbabaie, Kleinberg 2018 | arXiv 1802.06916 | notice seulement |
| Poursafaei, Huang, Pelrine, Rabbany 2022 | conférence | notice seulement |
| Chodrow, Veldt, Benson 2021 ; Contisciani, Battiston, De Bacco 2022 | revues | SUPPOSÉ |
| Koh et collègues 2020 ; Cranmer et collègues 2020 ; Udrescu et Tegmark 2020 ; Sybrandt, Tyagin, Safro 2020 | conférences | SUPPOSÉ |
| Tshitoyan et collègues 2019 | *Nature* | notice seulement |
| Funk et Owen-Smith 2017 ; Wu, Wang, Evans 2019 | revues | SUPPOSÉ |
| Swanson 1986 | revue | notice seulement |

## Critère de mort chiffré

Seuils **proposés, à geler** ; issus des cellules du collisionneur (synthèse, iii), illustratifs selon leurs auteurs.

1. **E6′** : « la fertilité s'apprend au-delà de la popularité » meurt si le gain conditionnel du modèle appris au-dessus de « popularité seule » (degré, âge, croissance), dans la strate de distance supérieure à 3, n'est pas positif avec un intervalle excluant zéro (T3-A).
2. **E1′ appliqué à la distance apprise** : la distance apprise meurt si son coefficient, à canal et popularité contrôlés, n'a pas d'intervalle à 90 % excluant zéro, ou si la rétrodiction inversée atteint le score prospectif moins δ₀ = 0,03 (T3-A, T3-B) ; elle doit aussi rester significative avec la distance entre domaines en covariable (Fable 4).
3. **Loi symbolique** : rejetée si son coefficient de détermination sur le jeu tenu à l'écart est inférieur à 0,85 (T3-C).
4. **Transition** : mot interdit tant que E2′ n'est pas passé (réponse 3 v2).

Préalable : calcul de puissance ; jeux disjoints par niche et par période ; graphe amputé des ponts (six garde-fous).

## Ce qui reste ouvert

- La forme de l'étiquette (réutilisation hors des citations) : trois variantes au collisionneur.
- La reproduction de Gu-Krenn : sur processeur ou sur devis (nœud de dépense).
- Le transfert entre champs : champ source, champ cible et perte tolérée à fixer.
- Remontée des citations de Gu-Krenn (qui l'a battu depuis ?) : non faite.
