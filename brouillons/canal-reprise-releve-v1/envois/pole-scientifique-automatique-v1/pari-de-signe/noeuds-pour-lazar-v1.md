# Deux nœuds pour Lazar, au format de décision, en clair — 27 octobre 2026

Lignée conv-audit (session servie par Opus 5.5 depuis 20:00 UTC environ), écrit à partir de 20:20 UTC. À la demande de
session-depot (message n° 94, point 2 (b) et (c)) : présenter chacun des deux nœuds restés ouverts après N-055 au format
de décision. Ce sont des **modifications de décisions déjà prises** (N-007, N-008, N-054) : sans mot de Lazar, **rien ne
change** (les décisions restent telles qu'écrites). Rien ici n'est une dépense.

## Rappel en clair (sans sigles)

- **La porte G1** est le test qui clôt la première phase du programme : elle dit si le **moniteur « boîte blanche »** (qui
  lit l'intérieur du modèle surveillé) détecte mieux le sabotage que **les moniteurs « boîte noire »** (qui ne lisent que
  le texte produit), à 1 % de fausses alarmes, pour chaque manière de saboter.
- **Les bases** sont les moniteurs de comparaison. Quatre ont été ajoutées par la décision N-007 : (i) une accumulation de
  scores **boîte noire** ; (ii) une **cascade** de portes sur les mêmes sondes **boîte blanche** ; (iii) une sonde
  **boîte blanche** sur le dernier état seulement ; (iv) un modèle temporel sur un observateur **boîte noire**.
- **Les planchers** sont deux repères grossiers : « tout signaler » (alarme permanente) et « un juge qui lit tout d'un
  coup avec le même modèle ». Ils servent à montrer que les bases ne sont pas des épouvantails.
- **Le mode tenu à l'écart** est une manière de saboter conçue par une instance qui n'a conçu aucun moniteur, scellée,
  révélée seulement à l'évaluation (N-054) : elle teste si nos moniteurs généralisent à un sabotage qu'ils n'ont jamais vu.

---

## Nœud 1 — Contre qui la boîte blanche doit-elle gagner pour franchir G1 ?

**Décision en une phrase** : garder la règle actuelle (la boîte blanche doit battre **chaque moniteur boîte noire** ; les
bases boîte blanche (ii) et (iii) servent à une autre hypothèse ; les planchers sont seulement rapportés), ou durcir G1
en exigeant aussi qu'elle batte les bases (ii), (iii) et/ou les planchers.

**Enjeu** : ce que G1 prouve. La question de G1 est « lire l'intérieur du modèle apporte-t-il quelque chose que le texte
ne donne pas ? ». Les bases (ii) et (iii) sont **déjà** boîte blanche : battre la cascade (ii) ne dit rien sur
« blanc contre noir », cela dit que **notre façon d'accumuler** les scores est meilleure — c'est la question de
l'hypothèse H2 (« l'accumulation additive détecte ce que le seuil par action manque »), pas celle de G1. Mes versions
2 et 3 de la conception du pari les avaient mises par erreur dans la liste de G1 ; la contre-lecture de la v3 l'a
relevé ; la v4 les en a retirées pour revenir à N-007 et N-008.

| option | avantage | inconvénient |
|---|---|---|
| **(a) garder N-007 et N-008 tels qu'écrits** (G1 contre les seules bases boîte noire ; (ii) et (iii) testées dans H2 ; planchers rapportés) | G1 mesure exactement ce qu'elle promet ; chaque question a son test ; pas de dépense ni de tâches en plus | G1 franchie ne dit pas, à elle seule, que notre accumulation bat une cascade (il faut lire H2 pour cela) |
| (b) ajouter (ii) et (iii) aux conditions de G1 | une G1 franchie dirait plus (blanc meilleur que noir **et** notre accumulation meilleure que les autres façons de lire le blanc) | mélange deux questions : un échec de G1 ne dirait plus laquelle a échoué ; demande la puissance du contraste le plus difficile (le blanc contre le blanc : écart probablement petit, donc plusieurs centaines de tâches de plus) |
| (c) ajouter les planchers aux conditions | protège contre une liste de bases faibles | inutile : un plancher est par construction plus faible qu'une base ; le contrôle « la meilleure base bat le plancher » est déjà rapporté |

**Recommandation : (a)**, confiance 0,8. **Défaut** : sans mot de toi, (a) — c'est l'état actuel, rien ne change.

---

## Nœud 2 — Avec quel intervalle lire l'expérience de lecture de N-054 (point 4) ?

**Décision en une phrase** : garder, pour l'expérience qui décide si la revendication de H1 est restreinte au seul mode
« coût », les **intervalles par rééchantillonnage des tâches** prévus par N-054, ou les remplacer (ou les doubler) par
l'intervalle du **pari apparié**, qui reste juste quel que soit le nombre de tâches.

**Enjeu** : N-054 point 4 dit : on gèle les moniteurs sur le mode « coût », on les lit sur le mode « affaiblir les
contrôles » et sur le mode tenu à l'écart, et **si la borne basse du gain blanc-sur-noir n'est pas au-dessus de zéro dans
les autres modes, H1 est restreinte au mode coût**. Un intervalle trop étroit fait croire à un gain là où il n'y en a pas,
donc **élargit H1 à tort**. Or le rééchantillonnage des tâches n'a pas de niveau garanti avec peu de tâches quand les
pertes sont rares (la situation typique : le blanc gagne un peu sur la plupart des tâches et perd beaucoup sur quelques
unes). Calcul exact de la contre-lecture de ma v3 : sous ce genre de situation, un intervalle à 95 % se trompe dans 4 à
7 % des cas à partir de 30 tâches (acceptable), mais dans **13 % à 100 tâches, 30 % à 60 tâches et 55 % à 30 tâches**
quand la perte touche 2 % des tâches ; le pari, lui, reste sous 1 % dans tous ces cas. Prix du pari : il lui faut environ
**2 à 3 fois plus de tâches** pour conclure, à effet égal.

| option | avantage | inconvénient |
|---|---|---|
| (a) garder le rééchantillonnage seul (N-054 tel qu'écrit) | plus puissant ; déjà prévu | peut élargir H1 à tort quand les pertes sont rares (jusqu'à 13 à 55 % d'erreur selon la rareté et le nombre de tâches), et on ne sait pas d'avance si elles le sont |
| (b) remplacer par l'intervalle du pari | juste à tout nombre de tâches, sous toute asymétrie | 2 à 3 fois plus de tâches pour la même puissance : la restriction de H1 au mode coût devient plus probable faute de données |
| **(c) le pari décide, le rééchantillonnage est rapporté à côté** | la décision « H1 restreinte ou non » reste juste ; on voit aussi ce que dirait le rééchantillonnage | le même coût en tâches que (b) pour que la décision tombe du bon côté |

**Recommandation : (c)**, confiance 0,7. **Défaut** : sans mot de toi, (a) — N-054 tel qu'écrit, rien ne change ; la
contre-lecture du préenregistrement de G1 devra alors vérifier le niveau du rééchantillonnage sur la banque réelle.

---

## Ce qui prend son défaut sans toi

Les décisions D-S13 à D-S23 de la conception du pari (v3 et v4 : convention d'égalité des scores, tirage des parties,
calibrage du développement, règle entre générations, calibrage de l'organisme, clé de l'héritage, exclusion du mode tenu
à l'écart, règles entre modes, témoins dans le compte, estimande par épisode, niveaux de H2b) prennent leur défaut le
**29 octobre vers 19:47 UTC** (20:47 heure de Paris) sauf mot contraire ; D-S11 et D-S20 restent des pièces du
préenregistrement de G1.
