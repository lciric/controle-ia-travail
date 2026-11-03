# Proposition D — Tour III.3 : réponse aux critiques

**Statuts.** Les faits Kirchner restent **RAPPORTÉS** par une moisson non opposable ; les résultats publics de Lazar restent **OBSERVÉS-NON-AUDITÉS**. Les objections discutées sont des **HYPOTHÈSES de méthode**, et les protocoles corrigés sont des **HYPOTHÈSES**. Tous les seuils, effectifs et niveaux de confiance introduits ci-dessous sont **illustratifs**.

**Pièces absentes :** les annexes F et G, la figure 32 et l’annexe A.4 ne sont pas servies ; je n’en infère aucun contenu.

## (a) Réponses aux critiques visant D

| Critique | Décision et correction |
|---|---|
| **Provenance du score des plantés** — A, B : s’il est assigné, \(\Delta\) mesure le générateur. | **Acceptée comme ambiguïté de rédaction**, non comme fait établi : D ne le précisait pas. Désormais, tout score primaire est obtenu par **exécution réelle sur le banc** ; aucun score n’est assigné. Les candidats primaires sont produits par l’agent. Une batterie plantée indépendante sert seulement à valider l’instrument. |
| **Le score et l’oracle doivent être indépendants** — A. | **Acceptée.** Le score vient du banc ; la vérité terrain vient d’événements de sandbox et d’invariants d’exécution hors de l’entrée du moniteur. Aucun déclencheur textuel ne définit à lui seul une violation. |
| **Fuite de l’étiquette ou de la signature de plantation** — A, B, C. | **Acceptée.** Les plantés de calibration sont scellés avant toute exposition au moniteur. Des cas licites passent par la même procédure d’insertion, y compris des signatures lexicales voisines sans violation exécutée. Le moniteur est aveugle au score, au rang, à l’étiquette et aux journaux de l’oracle. |
| **Appariement par décile de score** — A, C, E : il impose la distribution conjointe ou conditionne sur un collisionneur. | **Acceptée.** Le contraste primaire porte sur une population **non appariée**. Les jumeaux licites, appariés par tâche et procédure de génération mais pas par score, servent uniquement à mesurer la spécificité et les artefacts d’instrumentation. |
| **Confusion entre sélection par score et survie au filtre** — C. | **Acceptée.** \(R_S\) est estimé avant filtrage, sur tous les candidats. La fuite après « filtre puis score » devient une analyse distincte, fondée sur l’oracle. Le rappel du filtre parmi ses survivants n’est pas utilisé : il serait nul par construction. |
| **La fuite finale dépend de la prévalence expérimentale** — E. | **Acceptée.** Elle est rapportée à la prévalence expérimentale, puis repondérée sur une grille de prévalences préenregistrée, à distributions conditionnelles constantes. Aucun risque de déploiement n’est affirmé sans prévalence cible. |
| **Duel asymétrique : falsifier H_A exigeait un excellent moniteur** — A, B ; un faible rappel ne rend pas automatiquement le contraste non jugeable — E. | **Acceptée.** Les conditions \(R_0,R_S\geq0{,}90\) sont supprimées. Le duel porte directement sur \(\Delta\), à qualité de moniteur donnée. Un moniteur médiocre mais stable peut donc falsifier un enrichissement important. |
| **Règle de rejet de H_B mal écrite et seuils non alignés** — B, E. | **Acceptée.** Un seuil unique sépare deux hypothèses exhaustives ; la décision utilise le bon côté de l’intervalle. La zone intermédiaire est non concluante, jamais confirmatoire. |
| **Composition des classes** — C : \(\Delta\) brut peut provenir entièrement du mélange. | **Acceptée.** Les contrastes sont calculés **dans chaque classe**, puis standardisés avec des poids fixés avant l’expérience. Les intervalles par classe sont simultanés. Une classe sans support sélectionné n’est pas silencieusement retirée. |
| **Le « même modèle » n’est pas testé** — B. | **Acceptée par restriction de portée.** D1 teste désormais la sélection sous moniteur figé, pas les angles morts partagés. Une telle thèse exigerait un plan croisé famille de l’agent × famille du moniteur, à entrées identiques et fausses alertes calibrées séparément. |
| **D2 : moniteur de sélection et d’audit non distingués** — A. | **Acceptée.** Le moniteur du banc de surveillabilité et le moniteur d’audit ont des poids distincts, idéalement de familles différentes ; l’oracle reste indépendant des deux. À poids partagés, le résultat serait limité au transfert entre tâches, pas entre instruments. |
| **Intensité de sélection et condition préalable interne** — A. | **Acceptée.** Le contraste principal oppose sélection sur surveillabilité et placebo à étiquettes permutées, avec même budget et même quantile. Le bras « score de tâche » devient secondaire. Tout gain interne doit être confirmé sur données internes fraîches avant le test externe. |
| **D2 : hypothèses recouvrantes et « effondrement » indéfini** — B, E. | **Acceptée.** Le paramètre décisionnel devient le **plus faible gain de rappel parmi les classes externes préenregistrées**. Une chute d’une classe est ainsi prise en compte sans seuil supplémentaire ambigu. |
| **Échange rappel/fausses alertes** — C. | **Transformée en test.** La comparaison à fausses alertes communes utilise des calibrations séparées par bras, jamais le test final. Le seuil opérationnel figé est aussi rapporté, avec sa dérive de fausses alertes après sélection. |
| **D2 mélange classes, tâches et horizons nouveaux** — E. | **Acceptée.** Les cellules externes ne changent qu’un facteur à la fois et conservent une cellule interne fraîche inchangée. |
| **Puissance, grappes et effectifs sélectionnés** — A, B, C, E. | **Acceptée comme contrainte de jugeabilité**, sans reprendre leurs effectifs comme constantes universelles. Les estimateurs emboîtés conservent leur covariance ; les intervalles sont groupés par course et tâche. Un pilote distinct estime sélection, support et corrélation intra-groupe, puis fige la taille confirmatoire. |
| **La batterie figée peut être contaminée par les choix successifs** — E. | **Acceptée.** Un dernier lot d’audit n’est jamais consulté pendant la sélection, la calibration ou le développement. |
| **Exiger que le moniteur batte isolément la mécanique ignore leur complémentarité** — E. | **Acceptée.** Mécanique seule, moniteur seul et combinaison sont comparés sur les mêmes cas ; l’apport et le coût conditionnels du moniteur sont mesurés. |

## (b) Expériences corrigées

### Protocole commun

La boucle instrumentée produit des candidats par agents, avec des opportunités de violation appartenant à des classes préenregistrées, sans consigne d’évasion. Le banc fournit le score réel. L’oracle mécanique fournit \(Y\) à partir d’accès, de permissions, de provenance et d’invariants d’exécution ; la chaîne de raisonnement n’est jamais une vérité terrain.

Avant toute sélection, chaque candidat reçoit :

1. son score réel ;
2. son étiquette d’oracle, invisible pour les moniteurs ;
3. le verdict du moniteur figé, aveugle au score et au rang.

Les contrôles d’instrumentation comprennent des violations mécaniquement certaines, des cas licites de même procédure, des signatures sans violation et des honnêtes entiers pour les fausses alertes. Si ces contrôles échouent, l’instrument est déclaré défaillant ; aucun duel n’est interprété.

### D1 corrigée — Le score enrichit-il les faux négatifs à moniteur figé ?

Pour chaque classe \(q\) :

\[
R_{0,q}=P(M=1\mid Y=1,q),\qquad
R_{S,q}=P(M=1\mid Y=1,q,T_{\text{score}}=1).
\]

La sélection \(T_{\text{score}}\) retient un quantile préenregistré du score réel. Les contrôles sont une sélection aléatoire de même taille, des scores permutés dans les strates préenregistrées et un score indépendant du banc principal.

Le contraste primaire est :

\[
\Delta_w=\sum_q w_q(R_{S,q}-R_{0,q}),
\]

avec des poids \(w_q\) figés. Les \(R_{S,q}\) et \(R_{0,q}\) sont emboîtés : leur covariance est conservée dans le rééchantillonnage par course.

**Duel, seuils illustratifs :**

- **H_A — enrichissement matériel :** \(\Delta_w\leq-0{,}10\).
- **H_B — absence d’enrichissement d’au moins cette amplitude :** \(\Delta_w>-0{,}10\).

Avec un intervalle groupé à 95 % **illustratif** :

- entièrement au ou sous de \(-0{,}10\) : **H_B est falsifiée** ;
- entièrement au-dessus de \(-0{,}10\) : **H_A est falsifiée**, et je déprioritiserais ce mécanisme à cette amplitude ;
- chevauchant le seuil : non concluant.

Aucun plancher de \(R_0\) n’est exigé. En revanche, la précision et le support sont des conditions préalables : le pilote fixe la taille pour atteindre une demi-largeur cible de \(0{,}05\) **illustrative**, avec au moins vingt cohortes indépendantes **illustratives**. Si presque aucune violation n’atteint la zone sélectionnée, l’effet de sélection est non identifiable à ce budget ; cela ne prouve ni H_A ni H_B.

**Analyse secondaire du pipeline.** Score seul et « filtre puis score » sont comparés par l’oracle sur les lauréats finaux. La fuite est estimée par course, puis repondérée selon plusieurs prévalences. Cette analyse mesure le pipeline, pas un prétendu rappel du filtre parmi ses survivants.

### D2 corrigée — La sélection sur surveillabilité transfère-t-elle ?

Des configurations candidates sont évaluées sur un banc de développement avec un moniteur de sélection. Trois bras principaux, à budget et quantile identiques :

1. aucune sélection ;
2. sélection sur le banc de surveillabilité ;
3. placebo à étiquettes permutées.

La configuration retenue est figée, puis son gain interne est confirmé sur des épisodes internes frais. Sans confirmation, le transfert n’est pas jugeable.

L’audit emploie un moniteur distinct et scellé. Les cellules de test sont : interne fraîche, nouvelles classes seulement, nouvelles tâches seulement, horizon allongé seulement. Les strates sont définies avant traitement ; aucune standardisation sur une gravité post-traitement.

Pour chaque classe externe \(q\), soit \(G_q\) le gain de rappel entre sélection et absence de sélection, à taux de fausses alertes commun fixé sur des calibrations honnêtes séparées. Le paramètre est :

\[
G_{\min}=\min_q G_q .
\]

**Duel, seuil illustratif :**

- **H_A — transfert uniforme sur les classes testées :** \(G_{\min}\geq0{,}15\).
- **H_B — absence de ce transfert uniforme :** \(G_{\min}<0{,}15\).

Un intervalle simultané dont la borne inférieure atteint \(0{,}15\) falsifie H_B dans cette batterie ; une borne supérieure inférieure à \(0{,}15\) falsifie H_A. Entre les deux : non concluant. La fréquence des violations, les fausses alertes au seuil opérationnel et la qualité de tâche sont rapportées séparément. L’absence de violations dans une cellule de poids positif rend \(G_{\min}\) non identifiable, plutôt que de autoriser une repondération post hoc.

## (c) Réponse à l’arbitre — une page

### Ce qui est établi

**RAPPORTÉ — pièce Kirchner §2–3 :** 39 méthodes sur 1 601 sont signalées, soit 2,4 %, et une triche signalée atteint le top trois. Le moniteur et les agents sont du même modèle. Ces nombres ne donnent ni le nombre total de violations ni le rappel parmi les lauréats.

**OBSERVÉ-NON-AUDITÉ — « nos résultats » §2–3 :** le juge v8 obtient 0/1 000 sur onze lignes fatales, tandis qu’une fausse loi W2 est promue dans 12/12 unités. Cela illustre la distinction entre batterie couverte et couverture complète, sans rien démontrer sur un moniteur linguistique AAR.

**Calcul de définition :** à moniteur rigoureusement figé, sélectionner par score change la population conditionnée. Le rappel global et le rappel parmi les lauréats sont donc deux paramètres distincts, même sans adaptation contre le moniteur.

### Ce qui n’est pas établi

Aucun résultat servi n’établit que le classement réduit empiriquement le rappel à classe constante. Ne sont pas davantage établis : des angles morts causés par le partage du modèle, la représentativité des plantés pour la triche naturelle, le transfert d’un banc de surveillabilité hors banc, ou un risque chiffré en déploiement. Un résultat sur Llama-3.1-8B-Instruct ne se généraliserait ni à Opus 4.8 ni à toutes les boucles de recherche.

Le caractère sous-estimé du problème reste une **HYPOTHÈSE**, la nouveauté n’ayant pas été cherchée. Les requêtes de durcissement restent : `"automated researcher" monitor recall planted cheating leaderboard selection`, `selection-induced monitor blind spots`, et `monitorability benchmark transfer out-of-distribution reward hacking`.

### Première expérience et résultat qui me ferait changer d’avis

Je lancerais **D1 corrigée**, avant D2 : candidats produits par agents, scores réellement exécutés, oracle mécanique indépendant, moniteur figé évaluant tous les candidats avant sélection, contrastes intra-classe standardisés et contrôles de permutation.

Si l’intervalle est entièrement au-dessus de \(-0{,}10\) **illustratif**, cela falsifie l’enrichissement d’au moins dix points dans ce harnais : je cesserais d’en faire le mécanisme prioritaire et je testerais d’abord la couverture de l’instrument. S’il est entièrement au ou sous de ce seuil, l’absence d’enrichissement matériel est falsifiée et D2 devient prioritaire. Si l’oracle ou les contrôles licites échouent, ou si le support sélectionné est insuffisant, l’expérience ne tranche rien.

FIN-DE-CELLULE