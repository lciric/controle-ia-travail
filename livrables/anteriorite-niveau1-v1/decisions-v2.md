# Décisions soumises à Lazar — v2 (après lecture des PDF de niveau 1)

Rédigé le 2026-10-04 (UTC). Complète `livrables/premier-rendu-v1/decisions-v1.md`, sans le remplacer.
Sources : `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md` et les rapports scellés de `docs/sources/lecture-pdf-niveau1/` (dont le contrôle de traçabilité).
Les probabilités d'originalité citées ici sont **mes estimations**, non sourcées.

## Nœuds de décision (sans réponse, rien n'avance sur le point concerné)

**N-003 (renforcé) — Reformuler le théorème négatif.**

*Enjeu.* 2606.10456 revendique déjà, dans le temps, en boîte noire et pour un seul agent : « Any monitor whose decision rule depends only on F̂att (i.e., a marginal feature) has detection power equal to its false-positive rate against any zero-stealth-budget attack » (p. 3). Mais :
- l'énoncé est vide : une attaque à « budget nul » est impossible avec une marginale continue ;
- il est faux pour sa propre construction (simulation) : la moyenne atteint ≈ 2α à son point phare et ≈ 17α à δφ = 0,40, et le max reste sous α.

L'énoncé actuel du programme a le même défaut.

*Options.*
- (a) Énoncé par invariance (note mathématique v2), avec 2606.10456 cité comme antécédent défectueux :
  - classe C, où la loi du multi-ensemble est préservée : toute statistique invariante sous le groupe a son taux sous P₀ (T1) ;
  - impossibilité sans structure sous une loi honnête invariante (T2) ;
  - garanties locales sous structure (T3) ;
  - distinction explicite des classes C et K (copule) ;
  - temps et agents traités comme des sous-groupes de permutations.

  Avantage : T1 est vrai, corroboré par les sources et par la contre-vérification. T2 et T3 sont des énoncés de la note v2, contre-vérifiés une fois, que T0.3 préenregistrera et testera. Inconvénient : T1 est élémentaire ; la valeur est dans l'unification, T2, T3 et la mesure sur activations.
- (b) Restreindre l'énoncé actuel aux tests par action. Inconvénient : trivial.
- (c) Retirer T des revendications. Inconvénient : on perd le pont entre A et B. L'énoncé correct n'est qu'*adjacent* dans 2606.10456 (une remarque informelle sur le multi-ensemble, p. 1). Il n'est libre que vis-à-vis de ce papier, la recherche affirmative restant à finir (R8).

*Recommandation.* (a), confiance haute.

**N-005 (élargi) — Loi de déférence (HC1) : collision plus large qu'annoncé ; la porte GC vise le mauvais papier.**

*Enjeu.*
- 2508.07805 mesure déjà une note continue par juge et par technique ; il couvre 3 des 5 familles du programme.
- 2606.07897 mesure déjà une pente de déférence continue sur des intensités graduées, avec des rangs stables (sur des assistants, sans attaquant).
- 2607.08066 ne mesure qu'un taux.
- PARROT et BASIL, non lus, peuvent toucher le nul de régression vers la moyenne et le verdict lu par probabilité du jeton.

*Options.*
- (a) Reformuler HC1 sur la conjonction encore libre dans les sources lues :
  - g normalisé par l'écart à la cible de l'attaquant, dans un moniteur de contrôle ;
  - cinq familles d'attaque, dont usurpation et ordres en bande ;
  - régression multi-intensités avec nul de régression vers la moyenne ;
  - verdict lu par probabilité du jeton ;
  - opposition juge/sonde ;
  - stabilité de *rang* et invariance à l'attaquant préenregistrées ;
  - porte GC réécrite pour viser 2508.07805 et 2606.07897, sous réserve de PARROT et BASIL.

  Avantage : honnête et encore original. Inconvénient : originalité à revoir à la baisse (mon estimation : ≈ 0,5, contre 0,75).
- (b) Basculer maintenant vers HC4 et HC6. HC4 est libre, HC6 adjacent. Inconvénient : on abandonne la pièce centrale de C alors que la conjonction reste libre.
- (c) Maintenir HC1. Inconvénient : revendication en partie publiée.

*Recommandation.* (a), confiance moyenne à haute, à confirmer après lecture de PARROT et BASIL.

**N-007 — H2 : reformuler l'accumulation séquentielle sur sondes.**

*Enjeu.*
- *Doomed from the Start* (2607.06503) occupe la combinaison « sondes de l'agent + multi-tours + garantie de rappel au niveau de l'épisode ». C'est une cascade de portes indépendantes, sur un horizon figé ; elle n'est exacte qu'avec un certificat optionnel.
- E-valuator accepte tout score.
- « L'application aux sondes internes » ne se revendique donc plus.

*Options.*
- (a) Reformuler H2 :
  - Énoncé : sur des trajectoires où chaque action sabotée reste sous le seuil d'un moniteur par action calibré à 1 % de faux positifs, l'accumulation additive toujours valide de scores de sondes de l'agent qui agit détecte le sabotage avec un rappel qui croît avec l'horizon. Le contexte privé de l'agent est compris dans la lecture, et le seuil est calibré sur des épisodes honnêtes, sans aucun exemple de sabotage.
  - Quatre bases ajoutées au plan 2 × 2 : (i) accumulation sur scores boîte noire, type E-valuator ; (ii) cascade de portes indépendantes sur les mêmes sondes, type Doomed ; (iii) sonde sur le dernier état seul ; (iv) modèle temporel sur un observateur séparé, type TRACES.

  Avantage : différenciation nette. Inconvénient : plus de bases à faire tourner, pour un coût GPU modeste.
- (b) Garder H2 telle quelle. Inconvénient : revendication en partie occupée.

*Recommandation.* (a), **à confirmer après lecture** de Kulkarni 2026 (2604.28129), Padhi et al. 2026 (2604.19775), FIPER et Yueh-Han et al. 2025 (2506.10949). Confiance moyenne d'ici là. Originalité à revoir à la baisse (mon estimation : ≈ 0,35, contre 0,50).

**N-008 — Critère de la porte G1 : le bras « + 5 points de F1 » ne mesure pas une détection réelle.**

*Enjeu.*
- TRACE atteint son F1 publié en signalant environ 75 % des trajectoires honnêtes (calcul) ; « tout signaler » fait mieux, avec un F1 de 0,755 en moyenne par tâche.
- Même corrigé à taux de faux positifs égal, le F1 n'est, à prévalence fixée, qu'une fonction croissante du rappel. Le bras F1 redevient alors une comparaison de rappels, sans intervalle de confiance, et ses « + 5 points » dépendent de la prévalence.
- Modifier un critère de porte relève de Lazar.

*Options.*
- (a) Retirer le bras F1 ; ne garder que le rappel à 1 % de faux positifs, avec son intervalle à 95 %, contre la meilleure base boîte noire. Planchers « tout signaler » et « juge en une passe » rapportés. Avantage : un seul critère, sain et lisible. Inconvénient : plus exigeant.
- (b) F1 au seuil calibré sur les épisodes honnêtes réservés, au même taux de faux positifs pour tous les bras, avec plancher « tout signaler ». Avantage : garde la forme disjonctive. Inconvénient : disjonction surtout nominale, dépendante de la prévalence.
- (c) Statu quo. Inconvénient : porte gagnable sans détection réelle.

*Recommandation.* (a), confiance moyenne à haute.

## Propositions avec recommandation (défaut sous 48 heures)

**P-003 — Rendre forts les bras boîte noire de G1, contre l'homme de paille (R4).**
- Ajouter dans les deux colonnes boîte noire (par action et séquentielle) un juge robustifié de type b*, d'après les invites publiées par Terekhov et collègues. Ses poids d'agrégation ne sont pas publiés : à fixer et préenregistrer. b* a été trouvé avec le proxy de vérité : il faut le revalider avec un juge 8B ou 3B.
- Garder TRACE-lite, avec ces planchers préenregistrés : « tout signaler » et « juge en une passe avec le même modèle ».
- Journaliser les arrêts précoces et les JSON invalides.
- Lire un score continu par probabilité des jetons du verdict.

Défaut : appliqué. Confiance haute.

**P-004 — Environnement (a) : une reconstruction, pas un portage.**
- Reprendre les invites publiées : génération, rubrique à 10 critères, juge faible, proxy, détecteur, b*.
- Fixer et préenregistrer ce qui manque : agrégation de la rubrique, poids de b*, liste des papiers, échantillonnage, réimplémentation de l'optimiseur multi-objectif.
- Ajouter :
  - les contributions (agent, pas), par révision ou en multi-agents ;
  - des cibles semées préenregistrées, le proxy « modèle qui lit le papier » restant une composante de vérification différée sur sous-échantillon ;
  - une dose : proportion de tâches attaquées × intensité.
- Sceller d'abord un pilote 8B : g bénin de Llama-3.1-8B et décomposition de variance du juge. Le plan B « rubrique simplifiée » reste pertinent.
- Corriger « porté en 8 milliards de paramètres » (programme, section 6) en « reconstruit ».

Défaut : appliqué. Confiance haute.

**P-005 — Scinder la famille d'organismes (i) et ajouter un témoin d'instruction.**
- (i-a) Consigne explicite de saboter en dissimulant.
- (i-b) Stratégie biaisée d'apparence sincère, du type « science totalisante » de 2606.08892.
- Témoin « instruit sans sabotage » : même forme d'instruction cachée, sans mission de sabotage. Il sert à distinguer la lecture de l'instruction de la lecture de l'intention. AcMAS signale 100 % de faux positifs hors domaine, et les sondes de NARCBench sont apprises sur des rôles instruits.
- Prédiction de validité (programme, section 7) précisée :
  - une sonde d'intention doit réussir sur (i-a) et (ii), sans s'allumer sur le témoin ;
  - son échec sur (i-b) n'est pas un échec de validité.
- La rubrique est donnée à l'optimiseur rouge pour l'élicitation.

Défaut : appliqué. Confiance moyenne.
