# Proposition B, tour III.1 : faire tester des agents sur le noyau, en restant de la science

**Pièces.** Le bloc FAITS est vide, par décision de l'arbitre : je n'en tire rien. Je ne vois pas les propositions A et C (tour à l'aveugle), donc je ne m'en sers pas et ne les attaque pas. Tout ce qui suit sur le cadre vient du bloc QUESTION et porte le statut RAPPORTÉ. Tout ce que je propose porte le statut HYPOTHÈSE.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Pourquoi c'est fragile |
|---|---|---|---|
| S1 | « Faire ses tests avec des agents sur le noyau » désigne l'une des quatre lectures. | HYPOTHÈSE | Il manque au moins une lecture plausible, la (5) : **un agent qui conçoit**, c'est-à-dire un agent qui exécute lui-même la boucle (4) (tourner, lire, corriger, relancer). C'est peut-être le sens visé. C'est aussi la lecture qui multiplie le plus la réutilisation adaptative de la v3. |
| S2 | L'erreur type ≈ 0,07 sur 36 tâches et ≈ 0,09 sur 24 décrit le bruit d'une course. | RAPPORTÉ | L'arithmétique est cohérente : √(0,75 × 0,25 / 36) ≈ 0,072 et √(0,1875 / 24) ≈ 0,088. Mais elle suppose des tâches indépendantes et de difficulté homogène, ce qui reste une HYPOTHÈSE. Elle ignore la variance entre graines, inconnue (RAPPORTÉ), et la variance de trajectoire de conception (HYPOTHÈSE : probablement la plus grande). |
| S3 | Un écart de moins de 0,2 entre deux courses uniques reste dans le bruit. | RAPPORTÉ | C'est vrai pour deux échantillons indépendants : 0,072 × √2 ≈ 0,10, donc 2σ ≈ 0,20. C'est **trop pessimiste** si les deux objets sont notés sur les mêmes tâches avec des prédictions appariées : la variance dépend alors des seules paires discordantes. C'est **trop optimiste** si la variance entre graines s'ajoute. Le sens du biais est inconnu. |
| S4 | Le noyau est isolé : réseau et clés au seul noyau, organismes sans accès à la vérité. | RAPPORTÉ | Je n'ai aucune trace d'un test d'évasion ni d'un test de fuite des étiquettes. Isolation non auditée de ce côté. |
| S5 | `test_final` n'a jamais fuité vers les concepteurs ni vers les organismes. | HYPOTHÈSE | « Jamais rendue à l'organisme » est RAPPORTÉ. Rien ne dit qu'elle n'est pas lisible par les concepteurs ou par la lignée qui corrige. |
| S6 | L'organisme simple est un bon contrôle pour « la complexification ». | HYPOTHÈSE | Les deux organismes diffèrent par plusieurs facteurs : code, budget effectivement consommé, nombre d'appels. Un gain de l'organisme complexe peut venir de la dépense, pas de la structure. |
| S7 | La relecture suffit comme garde une fois le préenregistrement levé. | HYPOTHÈSE | La relecture lit des textes. Elle ne mesure ni le bruit, ni la fuite, ni l'ajustement à la v3. Son taux de détection est inconnu (voir (c)). |
| S8 | La v6 lot 3 existera, sera neuve et sera scellée au moment de la confirmation. | RAPPORTÉ (« à construire ») | Toute la séparation entre exploration et confirmation repose sur un objet qui n'existe pas encore. Si la v6 est construite par des auteurs qui ont lu les échecs de la v3, elle peut hériter des biais de conception. HYPOTHÈSE. |
| S9 | La question de fond, « la complexification apporte-t-elle une valeur au-delà du bruit ? », peut être tranchée avec 60 tâches par part. | HYPOTHÈSE | Avec σ_diff ≈ 0,10 en non apparié, seul un effet ≥ 0,2 est visible sur une course. Les effets plausibles d'une complexification pourraient être plus petits. Je ne le sais pas. |
| S10 | Les prédictions par tâche du pilote 4 seront journalisées, pas seulement l'exactitude. | HYPOTHÈSE | Sans elles, aucune analyse appariée n'est possible et S3 reste le seul outil. |

**Attaque de la recommandation de conv-audit** (elle est soumise à l'épreuve, je ne la lisse pas) :

- « (4) pour la conception » n'est pas une méthode tant qu'elle ne contient pas d'instrument de bruit. Chaque décision « corriger dans tel sens » prise sur une course unique, avec σ_diff ≈ 0,10, revient presque à un tirage à pile ou face pour les effets de moins de 0,2.
- « (2) peu utile si l'on peut relancer » compare deux coûts sans les mesurer. Une relance coûte une course, entre 30 et 55 USD (RAPPORTÉ, non opposable). Un essai court en coûte une fraction. Le bon choix dépend du **taux d'échec par course**, inconnu ; voir E5.
- « (3) en partie couvert par les relectures » confond deux instruments. Lire un texte n'est pas exécuter du code muté ni tenter une évasion. Ce recouvrement se mesure (E6), il ne se présuppose pas.

---

## Les quatre lectures et ce qui manque (point 1 de la question)

| Lecture | Apport à la question de fond | Coût | Risque principal |
|---|---|---|---|
| (1) Agents outillés à plusieurs pas | Ouvre un **nouvel axe** de complexification. Elle ne répond pas à la question actuelle, elle en crée une seconde. | Élevé, à variance forte : nombre de pas, recherches. | Accès à la vérité par la recherche : on retrouve la source d'une transcription d'évaluation. Évasion. Non-reproductibilité. Confusion avec l'axe étudié si elle est introduite pendant la même phase. |
| (2) Essai réel court avant chaque course | Aucun sur le fond. Elle protège le budget et la validité opérationnelle. | Faible par course. | Fausse sécurité : un essai court ne voit pas les pannes tardives (génération 3, dépassement cumulé). |
| (3) Agents neufs qui attaquent les essais du lanceur et du noyau | **Indirect mais réel** : un défaut de notation ou une fuite d'étiquette peut produire un faux gain de la complexification. | Jetons seulement. | Fausses alertes ; bruit des attaquants ; attaques bornées par leur imagination. |
| (4) Tourner, regarder, corriger, relancer | Direct mais exploratoire. | Une course par itération. | Jardin aux sentiers qui bifurquent ; ajustement à la v3 ; lecture du bruit comme signal. |

**Ce qui manque à la liste** (HYPOTHÈSES) :

- (5) L'agent concepteur (voir S1).
- (6) Le **rejeu A/A** : le même organisme, figé, est noté plusieurs fois. C'est l'instrument de bruit le moins cher.
- (7) Des **références de surface** : classe majoritaire, longueur seule, mots-clés (« benchmark », « évaluation », « test »). Elles disent si l'organisme bat le niveau qu'atteint un indice trivial.
- (8) Un **canari** dans `test_final` pour détecter une fuite.
- (9) Le **contrôle à étiquettes permutées** : il détecte un accès à la vérité.

**Ce qui se combine** :

- (3), (6), (8) et (9) précèdent (4) et se jouent sans organisme nouveau.
- (2) se décide une fois E5 mesurée.
- (1) ne se combine pas avec la phase actuelle sans brouiller la question de fond.

**Trois voies d'ordre, aucune présentée comme la réponse** :

- **V-α (conv-audit)** : (4) maintenant, (1) plus tard.
  - Elle est réfutée si E1 montre σ_run ≥ 0,035 : chaque lecture de (4) est alors du bruit.
- **V-β** : (3), (6), (8) et (9) d'abord, ou en parallèle du pilote 4 ; puis (4) avec un budget d'itérations ; (2) seulement si E5 le justifie ; (1) comme pilote séparé.
  - Elle est réfutée si E6 montre que les attaquants ne trouvent rien de plus que la relecture, et E1 que σ_run est négligeable : on a alors payé pour rien.
- **V-γ** : (1) tôt, comme facteur d'un pilote dédié, parce que c'est peut-être ce que Lazar voulait dire.
  - Elle est réfutée si les essais du noyau (section 4) échouent, ou si E7 montre que le gain vient d'une fuite.

**Ce qui les départage** : E1 (bruit A/A), E5 (taux d'échec), E6 (mutations), puis E7. Et une question à poser à Lazar, qui coûte zéro : « par agents, voulez-vous dire des outils pour l'organisme, ou un agent qui fait la boucle de conception ? ».

---

## (b) Expériences décisives, en duel H_A contre H_B

Les seuils sont **illustratifs**, sauf mention d'un raisonnement explicite.

### E1 : le bruit d'évaluation à code figé (rejeu A/A)

- **H_A** : à code figé, la variance d'une course à l'autre, venue de l'échantillonnage des appels de modèles, est petite devant le bruit des tâches : σ_run < 0,035, soit la moitié de 0,07 (seuil tiré du raisonnement S2).
- **H_B** : σ_run ≥ 0,035.
- **Dispositif** : figer la dernière génération de chaque organisme du pilote 4. La rejouer k = 5 fois (illustratif) sur `test` v3, sans conception, notation seule.
- **Métrique** :
  - l'écart type de l'exactitude entre rejeux ;
  - le **taux de bascule par tâche** : part des tâches dont la prédiction change entre deux rejeux.
- **Contrôle négatif** : la référence de classe majoritaire et un classifieur déterministe rejoués de la même façon doivent donner une variance de **zéro exactement**. Sinon, le noyau introduit lui-même du non-déterminisme (ordre des tâches, notation) : c'est un défaut à corriger avant toute lecture.
- **Falsification** :
  - σ_run ≥ 0,035 falsifie H_A, et avec elle toute lecture d'une course unique dans (4) ;
  - σ_run < 0,035 falsifie H_B, et (4) peut alors s'appuyer sur les intervalles de tâches.
- **Limite honnête** : avec k = 5, l'estimation d'un écart type est imprécise. Pour 4 degrés de liberté, l'intervalle à 95 % va d'environ 0,6σ à 2,9σ, par le raisonnement du χ². E1 tranche donc un ordre de grandeur, pas une valeur fine.

### E2 : la variance de trajectoire (course identique répétée)

- **H_A** : deux courses complètes de la même configuration finissent à moins de 0,10 d'écart (illustratif).
- **H_B** : elles divergent d'au moins 0,10.
- **Dispositif** : relancer une fois la course de l'organisme simple, avec la même configuration et une autre graine.
- **Contrôle négatif** : l'écart A/A de E1. Si l'écart de trajectoire n'est pas plus grand que l'écart A/A, la réécriture ne crée pas de variance propre.
- **Falsification** :
  - un écart ≥ 0,10 falsifie H_A, et toute comparaison d'organismes sur une course chacun est ininterprétable ;
  - un écart < 0,10 falsifie H_B.
- **Limite** : n = 1 paire. Une seule répétition suffit à falsifier H_A, pas à établir H_B. C'est asymétrique, et je le dis.

### E3 : la valeur de la complexification (la question de fond, confirmatoire, sur la v6)

- **H_A** : l'organisme qui réécrit sa récompense dépasse l'organisme simple, à **dépense égale**, sur `test_final` v6, de plus que le seuil fixé d'après E1 et E2.
- **H_B** : non.
- **Métrique** : la différence appariée par tâche (test de McNemar, ou bootstrap sur tâches et graines), plusieurs graines par organisme.
- **Contrôles négatifs** :
  1. **Placebo de complexification** : l'organisme complexe, mécanisme de réécriture désactivé, avec le même budget d'appels. Un gain du placebo signale un effet de dépense, pas de structure.
  2. **Étiquettes permutées** : tout organisme doit tomber au hasard (≈ taux de base). Le dépasser au-delà du bruit signe une fuite de la vérité.
  