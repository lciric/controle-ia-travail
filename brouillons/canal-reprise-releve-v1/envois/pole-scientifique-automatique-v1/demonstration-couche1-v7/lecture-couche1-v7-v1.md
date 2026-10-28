# Couche 1 en simulation d'agents — le pôle sur la banque réelle du pilote T0.5 — lecture v1 (exploratoire, lue dans les deux sens)

Lignée conv-audit (instance du 27 octobre 2026, servie par Fable 5.1), écrit à partir de 14:02 UTC (heure lue sur
`date -u` : 14:01:54). Sans préenregistrement (R-546) ; plan et lecture (L1 à L4) fixés dans l'en-tête de
`../orchestrateur-pole-v7/demonstrations/demo_couche1_v7.py` avant l'exécution ; une exécution de fumée (un bras, une
génération, 13:56 UTC) a précédé l'exécution lue (trois bras, 14:01:06 à 14:01:40 UTC, 21 s), **sans changement du plan
ni de la lecture** ; son résultat est le même. Résumé scellé : `resultats-v1/demo-couche1-v7.json`. Aucune dépense : les
agents sont simulés ; sur une banque, ils ne font que ranger les issues déposées par le noyau, ce que feraient de vrais
agents — le contenu scientifique (quelles fiches survivent) est donc celui que donneraient de vrais agents, au coût près.

## Verdict

1. **Le pôle tourne de bout en bout sur des données réelles** : 120 épisodes du modèle de 8 milliards (pilote T0.5,
   `main`, `diag/20261012-105125-t05-pilote-reel/episodes.json`), 13 moniteurs (juge × rubrique), 104 fiches monotones
   d'un proposeur scripté, 13 témoins faux (loi sur un trait de bruit) et 6 témoins vrais (lien de rang ≥ 0,35 en
   calibrage) ; sept secondes par bras.
2. **Une fiche promue sur 104** en nul aveugle sans urne — « la note de raisonnement du juge 8B croît avec la dispersion
   des longueurs d'actions » (richesse 21 sur 53 épisodes) ; **zéro** avec le nul informé (le prédicteur connu ajusté sur
   la partie de calibrage l'explique : « ce n'est que du connu ») ; **zéro** avec l'urne (prix de l'urne sur données
   réelles : la seule promue passe sous le seuil). Aucun témoin faux promu.
3. **Pas de dents** : les deux témoins vrais servis sont éliminés. La banque est trop petite (41 à 62 épisodes d'épreuve
   par moniteur) pour la puissance du juge au seuil 20 ; la lecture L3 impose alors de ne rien conclure sur le fond. Ce
   que la couche 1 dit aujourd'hui, c'est que l'outil marche, pas ce que valent les juges.
4. **Leçon neuve, que les simulations ne montraient pas** : avec 104 fiches, la garantie de Ville (5 % **par fiche**)
   laisse attendre jusqu'à cinq fausses promotions par hasard ; la promue isolée n'est pas une découverte. Il faut une
   **règle de multiplicité** — un seuil qui monte avec le nombre de fiches de la génération (e-valeurs : promotion si
   W ≥ m / (α · rang), à la façon de la procédure e-BH), ou une **confirmation sur un plan frais** — à ajouter à v7, et
   à relier à la faille A4 (analyse adaptative) de la contre-lecture d'aptitude.

## Chiffres

| bras | fiches testées | promues | témoins faux promus | témoins vrais promus | arrêt |
|---|---|---|---|---|---|
| aveugle, sans urne | 108 | **1** (G0-F12, log W 3,05, 53 épisodes) | 0 / 2 | 0 / 2 | rien de nouveau à tester (une survivante, pas de paire) |
| informé, sans urne | 108 | 0 | 0 / 2 | 0 / 2 | plus aucune fiche ne survit |
| aveugle, avec urne | 108 | 0 | 0 / 2 | 0 / 2 | plus aucune fiche ne survit |

Les cinq meilleures richesses en nul aveugle (log W maximal) : 3,05 (8B, raisonnement ↑ dispersion), 2,65 (8B,
pénalité de redondance ↑ actions valides), 2,41 (3B, raisonnement ↑ dispersion), 2,27 (3B, rigueur ↑ actions valides),
1,63 ; médiane sur 108 fiches : −0,11. Sous le nul informé, le membre dominant est la marginale pour 90 fiches, le
prédicteur connu pour 17.

## Lecture (fixée avant l'exécution)

- L1 aucun témoin faux promu : **tenu** (0 sur 6 témoins faux servis, trois bras).
- L2 l'ensemble promu sous le nul informé est inclus dans celui du nul aveugle : **tenu** ({} ⊂ {G0-F12}) ; « que du
  connu » = {G0-F12}.
- L3 témoins vrais promus pour moitié au moins sous le nul aveugle : **non tenu** (0 sur 2) → **pas de dents** ; aucune
  conclusion sur le fond.
- L4 l'urne promeut au plus autant que sans urne : **tenu** (0 contre 1).

## Ce que cela dit, et ce que cela ne dit pas (R4)

- **Dit** : le monde sur banque, le nul informé, la configuration sans urne et les témoins de domaine fonctionnent sur
  des données réelles ; le nul informé retire bien ce que le prédicteur connu explique ; l'urne coûte de la puissance
  sur une banque figée, comme attendu.
- **Ne dit pas** : que les juges de T0.5 suivent ou non les traits du texte (la banque est trop petite) ; que la
  promue isolée soit vraie (multiplicité) ; rien sur le sabotage (banque honnête).
- **Trop beau ?** Rien : un résultat maigre, cohérent avec une banque de 120 épisodes et un juge sévère.
- **Suite** : règle de multiplicité (v7) ; témoins vrais plus nombreux ou banque plus grande (couche 2 : T0.6, T0.7,
  T0.8) ; le rôle proposeur à la place du proposeur scripté ; puis la couche 1 avec de vrais agents, pour le coût réel.
