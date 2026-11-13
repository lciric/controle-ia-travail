# Rapport du lecteur — HC4, « taxe de déplacement », sur quatre pièces du lot 11 (v1)

- **Rôle** : lecteur (compte 2). **Modèle** : modèle A.
- **Heures** (relevées par `date -u`) : session ouverte le 2026-11-13 à 23:21:26 UTC ; lecture interrompue par un redémarrage du conteneur, reprise à 23:30:05 UTC ; rédaction commencée à 23:30:42 UTC. L'heure de fin est celle du scellement (fichier compagnon `.sha256`).
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (conforme). `interdits-communs-v2.md` lu : la consigne du compte 2 est plus stricte (aucune commande git), et c'est elle que j'ai suivie.
- **Fichiers du dépôt lus, et seulement aux lignes du mandat** : `docs/programme-controle-ia-v2.md` l. 85-125 et 190-215 ; `docs/decisions/decision-N-013-v1.md` l. 46-55 ; `docs/decisions/decision-N-068-v1.md` l. 1-115 ; `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` l. 279-292 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` l. 412-431 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` l. 509-535 et 696-726. Aucun autre fichier n'a été ouvert, et en particulier aucun rapport d'un autre lecteur. Aucune ouverture fautive, aucun refus.
- **Pièces** (dossier de pièces `…/lot11/` du mandat). Chaque empreinte a été vérifiée contre son compagnon `.sha256` avant la lecture, puis de nouveau après le redémarrage ; les quatre sont conformes :

| pièce | empreinte sha256 | pages | étendue lue |
|---|---|---|---|
| `2601.04603v1.pdf` (« Constitutional Classifiers++ ») | `ba8ec6570a41c42554ac89b9869020a2356cead5bdcf2618fc9c6208a89afdb5` | 17 | p. 1-17 ligne à ligne ; figures 2 et 3 (p. 7-8) lues sur l'image |
| `2309.10253v4.pdf` (GPTFuzzer) | `f2b76387acd042a27db07e8093dc4f4f4b876eb28d6a16fcf886432b31f1ffac` | 26 | p. 1-26 ligne à ligne ; figures 5, 8 et 9 (p. 13, 23, 24) lues sur l'image |
| `2310.08419v4.pdf` (PAIR, « Twenty Queries ») | `590bf40aa58061928f54d01b7d53f0d5141bb2ecf4f01483c6849423934f44e4` | 34 | p. 1-34 ligne à ligne ; captures des p. 27-33 lues sur l'image |
| `2502.19537v5.pdf` (NOICE, réglage fin) | `4f991dbe01b2c853189b45e1b36906bf355a367550f96703cf320b6e9f291d3c` | 37 | p. 1-37 ligne à ligne (p. 24-35 : exemples de sorties, sans chiffre) |

- **Citations contrôlées par programme** : 79, **0 échec**. Elles sont dans `citations-HC4-v1.json`, qui se trouve dans l'archive. Le contrôle est fait par `scripts/verifier_citations_v1.py`, lancé par `python3 -I`, avec et sans `-layout`, après normalisation. Le script a d'abord été essayé sur un cas juste (0 échec) puis sur trois cas altérés (texte, page, empreinte ; 3 échecs attendus et obtenus).
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi). Les noms de modèles qui apparaissent sont ceux des articles.

---

## 0. Verdict d'ensemble

**HC4 : « occupé en partie ».**

**La partie occupée.** 2601.04603 compare dans un même cadre une sonde linéaire (lecture interne du modèle protégé) et des classifieurs externes affinés, c'est-à-dire des modèles qui lisent le texte de l'échange. Les deux sont calibrés au même taux de refus (0,1 % sur WildChat) et entraînés sur la même distribution. La comparaison est faite sous les mêmes attaques en boîte noire : environ 7 000 échanges d'équipe rouge humaine, statiques. Elle ne porte que sur **l'axe « taux de succès »** :
- le taux de succès d'attaque contre la sonde est d'environ **1,4 %** (auteurs, p. 8) ;
- contre le petit classifieur, il est d'environ 1,1 % (figure, p. 7) ;
- contre le très petit classifieur, il est d'environ 4,5 % (figure, p. 7).

La sonde « almost matches the Haiku 4.5 classifier » (p. 8). Ce point est un **contre-indice** à la prémisse de HC4 dans le régime boîte noire : à durcissement et calibration comparables, la sonde ne coûte pas plus cher à évader.

**La partie non trouvée dans les quatre pièces.** Le coût d'attaque mesuré en requêtes, jetons, calcul, temps ou exemples de réglage fin pour **déplacer une sonde**, comparé au même coût pour **un juge génératif** :
- dans un même cadre ;
- par régime d'accès (contexte seul, lecture des activations ou des poids, écriture dans les poids) ;
- sous attaque adaptative ;
- avec une sonde qui lit l'intention ou l'action de l'agent auteur, au sens de la lettre restreinte par N-068.

**Pourquoi « en partie » et pas « non trouvé ».** Le mandat sépare « juge » et « classifieur ». Si l'on exige un juge génératif, la comparaison de 2601.04603 n'est qu'un voisin très proche. Si l'on prend la glose du mandat (« JUGE (modèle qui lit du texte) »), un classifieur affiné à partir d'un modèle de langue y entre. Sous R8, je retiens la lecture qui trouve la collision. Ce choix est une réserve explicite (section 9) : le contre-lecteur peut le trancher autrement.

---

## 1. L'énoncé confronté

- Programme v2, l. 105 : « Obtenir sur une sonde le déplacement que la rhétorique obtient gratuitement sur un juge exige l'obfuscation d'activations, pour un coût supérieur de plusieurs ordres de grandeur (accès, requêtes, calcul, taux de succès) ».
- N-013, l. 46-55, énoncé retenu : « exige un accès en écriture aux activations ou aux poids : le contexte seul n'y suffit pas ». Le coût se mesure par axe et par régime :
  - pour le contexte seul, l'écart « de plusieurs ordres de grandeur » reste une prédiction ;
  - pour les poids réglables, il n'est plus revendiqué.
- N-068, § 8, point 8a (a) : la lettre « le contexte seul n'y suffit pas » vaut désormais pour des **sondes entraînées qui lisent l'intention ou l'action de l'agent auteur, à taux de faux positifs fixé**. Pour les sondes de propriété de l'entrée et pour les lectures non supervisées, le déplacement par le contexte seul est publié.
- Composantes confrontées, selon le mandat :
  - (a) un coût d'attaque mesuré ;
  - (b) côté sonde ;
  - (c) côté juge ;
  - (d) la comparaison dans un même cadre, à durcissement égal et par régime d'accès ;
  - (e) la prémisse et ses contre-indices.

---

## 2. 2601.04603v1 — Cunningham, Wei et collègues, « Constitutional Classifiers++ »

**Venue imprimée.** arXiv, cs.CR, 8 janvier 2026 (p. 1). Aucune conférence n'est indiquée. Tous les auteurs sont d'une même entreprise (p. 1).

**Ce que l'article fait.** C'est une défense contre les « jailbreaks universels » sur des questions chimiques, biologiques, radiologiques et nucléaires. L'article :
1. remplace les classifieurs d'entrée et de sortie par un classifieur d'**échange**, qui lit la sortie avec son entrée (§ 3) ;
2. monte une **cascade** à deux étages (§ 4) ;
3. ajoute des **sondes linéaires** sur les activations du modèle protégé, entraînées avec un lissage par fenêtre glissante et une perte pondérée par softmax, puis assemblées avec un classifieur externe (§ 5) ;
4. assemble le tout en un système « de production » : la sonde est le premier étage, et le second étage est un ensemble sonde plus classifieur externe (§ 6).

La sonde lit le modèle qui génère : « The linear probe uses activations from Claude Sonnet 4, which is the protected model » (p. 8) ; « As such, the probe uses activations from that model » (p. 9). L'attaquant n'est pas ce modèle : c'est un utilisateur humain doté d'un accès par interface (« We provide red-teamers with API access to the defended model », p. 15).

**Points de coût chiffrés**

| point | objet attaqué | attaque | combien | succès | nature | page |
|---|---|---|---|---|---|---|
| A1 | système « dernière génération » : classifieur d'entrée et classifieur de sortie, **classifieurs** | équipe rouge humaine, boîte noire | 695 000 requêtes ; découverte moyenne en 27 h « self-reported » | 13 vulnérabilités à haut risque (0,01871 pour mille requêtes) | auteurs | 4, 10 |
| A2 | classifieur d'échange seul, **classifieur** (environ 50 % plus coûteux en calcul) | idem | 226 000 requêtes ; l'unique attaque universelle a demandé 100 h | 2 vulnérabilités (0,00885 pour mille) | auteurs | 4, 10 |
| A3 | cascade à deux étages sans sonde, **classifieurs** | idem | 569 000 requêtes ; découverte moyenne en 33 h | 5 vulnérabilités (0,00878 pour mille) ; hors programme de primes, des experts trouvent des jailbreaks universels « with substantial effort and automated tools » (non chiffré) | auteurs | 5, 10 |
| A4 | système de production, **sonde en premier étage**, puis ensemble sonde et classifieur | idem | environ 1 736 h cumulées (estimées par journaux d'interface), environ 198 000 tentatives ; découverte minimale en 30 h | 1 vulnérabilité (0,005 pour mille) ; aucun jailbreak universel sur les 8 questions | auteurs | 9, 10 |
| A5 | **sonde seule**, contre **petit classifieur** (affiné d'un modèle Haiku 4.5) et **très petit classifieur** (environ un tiers de sa taille) | jeu statique d'environ 7 000 échanges d'équipe rouge humaine, jamais utilisés à l'entraînement, à calibration égale (0,1 % de refus sur WildChat) | coût non mesuré (le jeu est fixe) | sonde environ 1,4 % (auteurs) ; petit classifieur environ 1,1 % ; très petit environ 4,5 % (figure 2a) | auteurs et figure | 7, 8 |
| A6 | ensembles statiques | idem | — | sonde avec petit classifieur environ 0,45 % ; deux classifieurs environ 0,8 % ; petit classifieur seul environ 1,1 % ; sonde seule environ 1,4 % (figure 3a). Le poids α est « optimized per pair to minimize attack success rate on the test set » | figure | 8 |

**Points de coût de défense (calcul du défenseur), à ne pas confondre avec un coût d'attaque**

| point | contenu | page | nature |
|---|---|---|---|
| D1 | sonde de toutes les couches sur Gemma 3 27B : 2Ld ≈ 377 000 opérations par jeton ; une passe de Gemma 3 4B coûte environ 8 milliards d'opérations ; « The probe is thus several orders of magnitude cheaper than a small external classifier » | 7 | auteurs (formule lue sur le PDF, non contrôlée par programme) ; rapport d'environ 2,1 × 10⁴ (calcul) |
| D2 | surcoût de calcul relatif : 100 (dernière génération), 150 (échange), 27,8 (cascade), 3,5 (production) ; réductions de 40 fois, 8 fois et 5,4 fois | 1, 2, 5, 9, 10 | auteurs ; 150/3,5 = 42,9 ; 27,8/3,5 = 7,9 ; 150/27,8 = 5,4 (calcul, conformes) |
| D3 | cascade sonde et petit classifieur : « 100x reduction in compute costs » à robustesse supérieure au petit classifieur seul | 8, 9 | auteurs |
| D4 | le premier étage de la cascade sans sonde pèse environ 77 % du coût total | 5 | auteurs |

« Plusieurs ordres de grandeur » apparaît dans cette pièce, mais pour le **coût de défense** de la sonde, qui est plus faible. Ce n'est en aucun cas un coût d'attaque, et le sens est inverse de celui de HC4.

**Ce que l'article ne fait pas**
- Aucune attaque n'est **dirigée contre la sonde** : aucune obfuscation d'activations, aucune optimisation contre le score de la sonde, aucun régime « activations » ni « poids ».
- Aucun coût d'évasion n'est mesuré séparément pour la sonde et pour le classifieur : A5 est un taux de succès sur un jeu figé.
- Aucun juge génératif sous rhétorique : les classifieurs sont des classifieurs affinés.
- Aucun agent auteur : l'auteur du contenu adverse est un utilisateur externe.
- La tâche du moniteur est de détecter un contenu nuisible, pas une intention ou une action de sabotage.

**Limites reconnues par les auteurs**
- « This may underestimate the attack success rate » (note 6, p. 7).
- Les systèmes ne protègent pas le même modèle, mais « we do not believe this affects the comparison substantially » (note 2, p. 4).
- La sonde signale davantage de requêtes scientifiques bénignes : « the flag rate on benign scientific requests was higher for the probe » (p. 8).
- Les heures sont déclarées par les participants ou estimées (p. 4 ; note 7, p. 9).

**Incohérences et réserves de lecture**
1. Le rapport « 2.2x fewer » (p. 2) devient 0,01871/0,00885 = **2,11** (calcul).
2. Les campagnes d'équipe rouge ne sont pas comparables entre elles :
   - les questions changent (« We replaced four of the original eight target queries », p. 15) ;
   - les primes changent (maximum de 25 000 à 35 000 dollars, multiplicateur ajouté, p. 15) ;
   - le modèle protégé change.

   La comparaison des systèmes A1 à A4 n'est donc pas faite à effort d'attaque constant. Elle ne mesure pas un coût d'attaque contrôlé.
3. **Résultat trop beau (R4)** : le poids des ensembles est optimisé sur le jeu de test (p. 8). Les résultats A6 sont optimistes par construction.
4. Le dénombrement des requêtes ne garde que les utilisateurs dont plus de 5 % des requêtes sont refusées (p. 14). Ce filtre dépend du défenseur lui-même.

**Verdicts par composante**

| composante | verdict | appui |
|---|---|---|
| (a) coût d'attaque mesuré | **occupée en partie** | requêtes et heures par vulnérabilité contre des systèmes de classifieurs (A1-A4), mais pas pour déplacer un moniteur isolé ; aucun calcul d'attaquant (p. 4, 5, 9, 10) |
| (b) sonde | **occupée en partie** | taux de succès d'attaques statiques en boîte noire contre une sonde du modèle protégé (A5, p. 7-8) ; aucun coût, aucune attaque adaptative |
| (c) juge | **voisin** | classifieurs affinés, non génératifs ; aucune rhétorique dirigée vers le moniteur |
| (d) comparaison dans un même cadre | **occupée en partie** | sonde contre classifieurs, mêmes attaques, calibration égale, même distribution d'entraînement (p. 7-9) ; axe « taux de succès » seulement, régime boîte noire statique seulement |
| (e) prémisse | **contre-indice** | sonde environ 1,4 % contre petit classifieur environ 1,1 % (p. 8) : pas d'écart en faveur de la sonde ; un classifieur durci n'est pas gratuit à déplacer (100 h pour l'unique attaque universelle, p. 4) |

---

## 3. 2309.10253v4 — Yu, Lin, Yu, Xing, « GPTFuzzer »

**Venue imprimée.** arXiv v4, 27 juin 2024 (p. 1). Aucune venue n'est imprimée.

**Ce que l'article fait.** C'est un « fuzzing » en boîte noire de gabarits de jailbreak. Il part de 77 gabarits humains, choisit une graine par une variante de recherche arborescente de Monte-Carlo, la fait muter par un modèle de langue (générer, croiser, étendre, raccourcir, reformuler) et juge le succès par un RoBERTa affiné. Le régime d'accès est dit explicitement : « given that we neither access the source code nor the weights of the models under examination » (p. 3).

**Points de coût chiffrés.** L'objet attaqué est toujours **le modèle lui-même** (son refus), jamais un moniteur.

| point | objet | attaque | combien | succès | page |
|---|---|---|---|---|---|
| G1 | Llama-2-7B-Chat, 46 questions résistant aux gabarits humains | fuzzing, une question à la fois, plafond de 500 requêtes | 22,47 requêtes en moyenne avec les 5 meilleures graines ; 105,62 avec les graines valides ; 177,54 avec toutes ; 358,91 avec les graines invalides | 46/46 ; 45/46 ; 43/46 ; 21/46 | 11, 12 (tableau 3) |
| G2 | Llama-2-7B-Chat, 100 questions | budget de 50 000 requêtes au total | — | premier gabarit 47-60 % ; cinq meilleurs 87-96 % | 12 |
| G3 | transfert vers 12 modèles | 80 000 requêtes de fuzzing sur trois modèles | — | cinq meilleurs gabarits environ 80 % sur Llama-2-70B ; plus de 90 % sur Claude2 ; plus de 96 % sur PaLM2 ; plus de 60 % sur Bard et GPT-4 | 13, 14 |
| G4 | référence en boîte blanche (GCG) | 500 pas d'optimisation, 4 graines | — | sous les gabarits humains contre les modèles commerciaux (figure 5) | 13, 14 |
| G5 | coût global de l'étude | — | plus de 300 millions de jetons pour interroger ChatGPT | — | 9 |
| G6 | coût des **juges de mesure** (non attaqués) : 1 540 réponses | — | RoBERTa 37 s ; ChatGPT 9 min 15 s ; GPT-4 1 h 27 min | précision 0,96 ; 0,88 ; 0,92 | 9 (tableau 1) |

**Ce que l'article ne fait pas.** Aucune sonde. Aucun moniteur attaqué : les juges servent à mesurer le succès, ils ne sont pas visés. Aucune comparaison sonde contre juge.

**Limites reconnues.** Il dépend des gabarits humains (p. 15). L'outil « needs a lot of queries to the target model and has a risk of being blocked » (p. 15). Le juge commet des erreurs (p. 15).

**Incohérences**
- Un renvoi « Appendix XXX » est resté non rempli (p. 16).
- La version « gpt-3.5-turbo-0631 » est une date impossible (p. 4, 26).
- Dans la figure 9 (p. 24), l'axe « ASR (%) » est gradué de 0 à 1,0.

**Verdicts par composante**

| composante | verdict |
|---|---|
| (a) | **voisin** : coûts d'attaque en boîte noire, en requêtes, mesurés contre le modèle lui-même |
| (b) | **ne touche pas** |
| (c) | **ne touche pas** : les juges mesurent, ils ne sont pas attaqués |
| (d) | **ne touche pas** |
| (e) | **contre-indice faible et indirect** : un modèle durci par sécurité (Llama-2-7B-Chat) résiste aux gabarits humains (premier gabarit à 20 %, p. 10-11) et demande de 22 à 359 requêtes par question (p. 12). Un lecteur de texte durci n'est pas déplacé « gratuitement ». Ce n'est pourtant pas un moniteur. |

---

## 4. 2310.08419v4 — Chao, Robey, Dobriban, Hassani, Pappas, Wong, « Jailbreaking Black Box Large Language Models in Twenty Queries » (PAIR)

**Venue imprimée.** « Preprint. Under review. », version du 18 juillet 2024 (p. 1).

**Ce que l'article fait.** Un modèle attaquant affine itérativement, en boîte noire, une consigne de jailbreak contre un modèle cible. Llama Guard sert de juge **de mesure**. Les trois stratégies sont **rhétoriques** : « logical appeal, authority endorsement, and role-playing » (p. 3). Ce sont les familles d'attaque de EC.1.

**Points de coût chiffrés.** L'objet attaqué est toujours **le modèle lui-même**.

| point | objet | attaque | combien | succès | page |
|---|---|---|---|---|---|
| P1 | 7 modèles cibles, 100 comportements | PAIR, 30 flux de profondeur 3 au plus, soit 90 requêtes au plus | requêtes par succès : Vicuna 10,0 ; Llama-2 56,0 ; GPT-3.5 33,0 ; GPT-4 23,7 ; Claude-1 13,7 ; Gemini 23,5 | 88 % ; 4 % ; 51 % ; 48 % ; 3 % ; Claude-2 0 % ; Gemini 73 % | 5, 6 (tableau 2) |
| P2 | Vicuna, Llama-2 | GCG en **boîte blanche**, 500 itérations, lot de 512 | environ 256 000 requêtes par comportement | 56 % ; 2 % | 5, 6 |
| P3 | Vicuna (attaquant Mixtral) | PAIR contre GCG | PAIR 34 s, 366 Mo de processeur, 0,026 dollar ; GCG 1,8 h sur A100, 72 Go de processeur graphique | — | 2, 7, 8 (tableau 4) |
| P4 | défenses statiques : SmoothLLM et filtre de perplexité (un **filtre**, pas un juge génératif) | consignes trouvées sans défense, puis rejouées | — | PAIR sur GPT-4 : 48 % sans défense, 25 % sous SmoothLLM, 40 % sous filtre de perplexité ; GCG tombe à 0-5 % | 7, 8 (tableau 5) |
| P5 | AdvBench, 50 comportements | PAIR (attaquant Vicuna) contre GCG | PAIR de 11,9 à 33,8 requêtes par succès ; GCG **5 120** requêtes par succès | Vicuna 100 % ; Llama-2 10 % (PAIR) contre 98 % et 54 % (GCG) | 15 (tableau 8) |
| P6 | juges de **mesure** (non attaqués) | — | — | taux de faux positifs de 4 à 23 % ; taux de faux négatifs de 7 à 74 % | 4 (tableau 1) |

**Ce que l'article ne fait pas.** Aucune sonde. Aucun moniteur visé par l'attaque : le juge mesure. Les défenses P4 sont évaluées « statically » (p. 7), sans attaque adaptative.

**Ce qui touche HC4 dans la méthode.** P2, P3 et P5 sont une comparaison de coût **par régime d'accès** (boîte noire contre boîte blanche) sur un **même objet** : la boîte blanche coûte plusieurs ordres de grandeur de requêtes en plus.
- Ce n'est pas un écart sonde contre juge.
- Mais cela montre que, dans un même cadre, le coût dépend autant de l'algorithme d'attaque que de l'accès. Plus d'accès ne veut pas dire coût plus faible.
- C'est un contre-indice de méthode pour toute lecture de la « taxe » qui confondrait régime d'accès et coût.

**Limites reconnues.** PAIR « struggles against strongly fine-tuned models including Llama-2 and Claude-1/2 » (p. 9).

**Incohérences**
1. « fewer than twenty queries » (résumé, p. 1) : le tableau 2 donne plus de 20 requêtes par succès pour Llama-2, GPT-3.5, GPT-4 et Gemini (p. 5).
2. « more than 250-fold improvement over existing attacks such as GCG » (p. 2) : 256 000/10 = 25 600 ; 256 000/56 = 4 571 ; 5 120/11,9 = 430 ; 5 120/33,8 = 151 (calcul). Aucun de ces rapports ne donne « 250 ».
3. Le budget de GCG passe de 256 000 requêtes (p. 6) à 5 120 requêtes par succès (p. 15), sans explication.
4. La même configuration (attaquant Mixtral, cible Vicuna, 30 flux de profondeur 3) donne **88 %** au tableau 2 et **93 %** au tableau 7 (« Default », p. 9).
5. « Vicuna-17B » (p. 2) : ailleurs, le modèle est Vicuna-13B.

**Verdicts par composante**

| composante | verdict |
|---|---|
| (a) | **voisin** : coût d'attaque mesuré (requêtes, temps, dollars) contre le modèle, pas contre un moniteur |
| (b) | **ne touche pas** |
| (c) | **voisin** : rhétorique en boîte noire contre un lecteur de texte (le modèle lui-même) ; aucun juge visé |
| (d) | **voisin de méthode** : comparaison de coût par régime d'accès sur un même objet (P2, P3, P5), sans sonde ni juge |
| (e) | **contre-indice indirect** : la rhétorique ne « déplace » pas gratuitement un lecteur de texte durci (Claude-2 0 %, Llama-2 4 %, p. 5) ; l'appui d'autorité est la stratégie la moins efficace (p. 8) |

---

## 5. 2502.19537v5 — Kazdan, Puri, Schaeffer, Yu, Cundy, Stanley, Koyejo, Dvijotham, « No, of Course I Can! » (NOICE)

**Venue imprimée.** « Preprint. Under review. », version du 12 juillet 2025 (p. 1).

**Ce que l'article fait.** C'est une attaque par **réglage fin** sur des données d'apparence inoffensive. Le modèle apprend à refuser d'abord, puis à répondre. L'attaque traverse :
- les défenses « superficielles » (la défense AMD : un modèle aligné écrit les premiers jetons) ;
- le filtre de sortie Llama Guard, « deceived by the refusal prefix » (p. 7).

Le régime est celui des **poids du modèle surveillé**, réglés par l'attaquant. Il n'y a aucune écriture dans le moniteur.

**Points de coût chiffrés**

| point | objet attaqué | attaque | combien | succès | nature | page |
|---|---|---|---|---|---|---|
| N1 | GPT-4o, par l'interface de réglage fin | NOICE | 1 000 exemples, 1 époque, 3,3 millions de jetons, environ 85 dollars ; plafond du modèle de menace : 100 dollars | 57 % (référence 8,6 %) | auteurs | 1, 2, 5, 6 (tableau 3) |
| N2 | Claude-3-Haiku | NOICE | 1 000 exemples, 1 époque | 72 % (référence 1,3 %) | auteurs | 1, 6 (tableau 4) |
| N3 | **filtre de sortie Llama Guard** (un **juge** à base de modèle de langue, lisant la sortie d'un modèle réglé par l'attaquant) | NOICE, réglage fin du modèle surveillé | 5 000 exemples ; environ 30 min sur 2 A100 pour les modèles de 7 milliards de paramètres | taux de succès malgré le filtre : Llama-3-8B 47 % ; Gemma-2-9B 31 % ; Mistral-7B 37 % | auteurs | 7, 8 (tableau 8), 21 |
| N4 | défense AMD | NOICE | 5 000 exemples | 48 % ; 29 % ; 60 % | auteurs | 7, 8 |
| N5 | tailles de 1 à 70 milliards de paramètres | NOICE, 5 000 exemples | 2 à 8 A100 | 24-56 % (Llama) ; 28-35 % (Gemma) | auteurs | 7 (tableau 7), 21 |
| N6 | courbe en fonction du nombre d'exemples | 10, 100, 1 000, 5 000 | — | Llama-3-8B sans défense : 1 %, 18 %, 36 %, 56 % ; « as few as 100 » suffisent à compromettre la sécurité | auteurs | 36, 37 (tableau 16) |

**Ce que l'article ne fait pas**
- Aucune sonde ni lecture interne (« probe » n'apparaît que dans un titre de référence, p. 18).
- Aucune comparaison avec un moniteur interne.
- Aucune attaque contre les poids du juge.
- Llama Guard n'est appliqué qu'aux modèles ouverts, pas à GPT-4o ni à Claude-3-Haiku (tableaux 3, 4 et 8).

**Limites reconnues.** AMD « is vulnerable to inference-time attacks » (p. 9). Les auteurs supposent une modération plus stricte des modèles réglés chez le fournisseur (p. 6).

**Incohérences**
1. « seven times higher than previous fine-tuning attacks (see Table 5) » (p. 2) : les chiffres sont au tableau 3, et 0,57 divisé par 0,086 / 0,06 / 0,043 / 0,013 donne 6,6 / 9,5 / 13,3 / 43,8 (calcul).
2. Le texte annonce « Llama 3.1 7b-Instruct » (p. 7) alors que le tableau 7 donne « 70B ».
3. « Table 4 shows ASRs for the attacked and original models » (p. 5) parle de GPT-4o, alors que GPT-4o est au tableau 3.
4. Une défense « FRD » apparaît aux tableaux 16 et 17 (p. 37) sans être définie.
5. Les tableaux 11 à 15 se disent « with defenses » sans dire quelle défense s'applique à chaque ligne.

**Verdicts par composante**

| composante | verdict |
|---|---|
| (a) | **occupée en partie, côté juge** : exemples de réglage fin, temps de calcul et dollars pour faire passer un contenu nuisible sous un filtre de sortie (N3) ; régime « poids du modèle surveillé » |
| (b) | **ne touche pas** |
| (c) | **voisin** : juge de type filtre (Llama Guard) déplacé par une forme de surface, le préfixe de refus ; ni rhétorique dirigée vers le juge, ni juge génératif de contrôle |
| (d) | **ne touche pas** |
| (e) | **contre-indice indirect au « gratuitement »** : déplacer ce juge a demandé un réglage fin (de 100 à 5 000 exemples) ; mais le juge a été trompé par la forme, ce qui va dans le sens de la fragilité des juges |

---

## 6. Table de synthèse (composante × pièce)

| composante | 2601.04603 | 2309.10253 | 2310.08419 | 2502.19537 |
|---|---|---|---|---|
| (a) coût d'attaque mesuré | occupée en partie (p. 4, 5, 9, 10) | voisin (p. 11-12) | voisin (p. 5-8) | occupée en partie, côté juge (p. 7-8, 21) |
| (b) sonde | occupée en partie (taux, p. 7-8) | ne touche pas | ne touche pas | ne touche pas |
| (c) juge | voisin (classifieur) | ne touche pas | voisin | voisin |
| (d) comparaison dans un même cadre | occupée en partie (taux, boîte noire statique, p. 7-9) | ne touche pas | voisin de méthode (régimes, p. 5-8, 15) | ne touche pas |
| (e) prémisse | contre-indice (p. 4, 8) | contre-indice faible | contre-indice indirect (p. 5, 8) | contre-indice indirect, et appui à la fragilité des juges |

---

## 7. Ce qui reste revendicable (formulation exacte)

> « Le coût d'attaque — requêtes, jetons, calcul, temps, exemples de réglage fin — nécessaire pour obtenir un déplacement donné du score d'une sonde entraînée qui lit l'intention ou l'action de l'agent auteur, à taux de faux positifs fixé, comparé dans un même cadre au coût du même déplacement sur un juge génératif sous les mêmes attaques, par régime d'accès (contexte seul ; lecture des activations ou des poids ; écriture dans les poids), à durcissement déclaré et sous attaque adaptative. »

- C'est **non trouvé dans les quatre pièces lues**. HC4 reste « peu cherché » (M14) : ce verdict ne vaut pas « trou du champ ».
- La prédiction « de plusieurs ordres de grandeur » reste une prédiction. Aucune des quatre pièces ne la soutient. La seule pièce qui compare une sonde et un lecteur de texte (2601.04603) trouve des taux comparables dans le régime boîte noire statique.

---

## 8. Ce qu'une phrase publique sur HC4 ne doit pas affirmer

1. Qu'aucune comparaison d'une sonde et d'un moniteur qui lit le texte, sous les mêmes attaques et à calibration égale, n'est publiée. 2601.04603 en publie une, sur l'axe du taux de succès (p. 7-9).
2. Que les sondes sont plus robustes ou plus coûteuses à évader que les classifieurs. À calibration égale, la sonde est à environ 1,4 % contre environ 1,1 % pour le petit classifieur (p. 7-8).
3. Que la rhétorique déplace « gratuitement » un lecteur de texte durci :
   - classifieurs durcis : 100 h pour l'unique attaque universelle (p. 4) ;
   - PAIR : 0 % sur Claude-2 et 4 % sur Llama-2 (p. 5) ;
   - GPTFuzzer : de 22 à 359 requêtes par question sur Llama-2 (p. 12).
4. Citer « several orders of magnitude » (2601.04603, p. 7) comme un écart de coût d'attaque : c'est le coût de **défense** de la sonde, plus faible.
5. Citer « fewer than twenty queries » (PAIR) comme le coût de déplacement d'un **juge** : c'est le coût de jailbreak du modèle lui-même, mesuré par un juge non attaqué. En plus, le tableau 2 contredit ce chiffre pour quatre cibles sur six (p. 5).
6. Citer le facteur « 250-fold » de PAIR (p. 2) : il ne se retrouve pas dans les tableaux.
7. Lire le système de production de 2601.04603 (1 736 h, 1 vulnérabilité) comme la robustesse d'une sonde seule. C'est une cascade sonde plus classifieur, et les campagnes ne sont pas faites à effort constant (p. 9, 15).

---

## 9. Réserves

- **R8, sur le mot « juge ».** Le verdict « occupé en partie » repose sur la lecture du mandat (« JUGE (modèle qui lit du texte) »), qui fait entrer un classifieur affiné à partir d'un modèle de langue. Si le contre-lecteur exige un juge génératif, le verdict d'ensemble devient « non trouvé dans les pièces lues », avec 2601.04603 comme voisin très proche et contre-indice. Je signale ce point sans le trancher davantage.
- **R4, résultat trop propre.** L'ensemble sonde plus classifieur de 2601.04603 est optimisé sur le jeu de test (p. 8). Le système de production est jugé par une équipe rouge dont l'effort, les questions et les primes ont changé (p. 15).
- **Profondeur.** Les quatre pièces ont été lues en entier (journal dans l'archive). Les valeurs des figures 2 et 3 de 2601.04603 sont lues sur l'image, donc approximatives (nature « figure »).
- **Constat B2.** Je n'ai pas ouvert la l. 140 de l'état de l'art v1, qui est hors mandat. Les chiffres vérifiés sur PDF qui pourraient la soutenir, ou la corriger, sont les suivants :
  - PAIR : 34 s, 366 Mo, 0,026 dollar, 10 à 56 requêtes par succès (p. 2, 5, 8) ; GCG : environ 256 000 requêtes et 1,8 h sur A100 (p. 6, 8) ;
  - GPTFuzzer : moins de 23 requêtes en moyenne sur Llama-2 avec les meilleures graines (p. 11), budgets de 500 et 50 000 requêtes (p. 11-12).

  La confrontation reste à faire par la session mère.

---

## 10. Voisins nommés dans les pièces et non lus

| voisin | nommé dans | page |
|---|---|---|
| Cunningham et collègues 2025, « Cost-effective constitutional classifiers via representation re-use » (billet) | 2601.04603 | 10, 12 |
| McKenzie et collègues 2025, « Detecting high-stakes interactions with activation probes » (2506.10805) | 2601.04603 | 10, 12 |
| Hua et collègues 2025, « Combining cost-constrained runtime monitors for AI safety » (2507.15886) | 2601.04603 | 10, 12 |
| Sharma et collègues 2025, « Constitutional classifiers » (2501.18837) | 2601.04603 | 1, 13 |
| Youstra et collègues 2025, attaques par chiffrement contre les interfaces de réglage fin (2508.17158) | 2601.04603 | 13 |
| Casper et collègues 2024, entraînement adverse latent (2403.05030) | 2601.04603 ; 2502.19537 | 10, 12 ; 11 |
| Zou et collègues 2024, « circuit breakers » (2406.04313) | 2601.04603 | 10, 13 |
| Nikolić et collègues 2025, « The jailbreak tax » (2504.10694) | 2601.04603 | 3, 12 |
| Zeng et collègues 2024, persuasion contre les modèles de langue (« How Johnny can persuade ») | 2310.08419 | 3, 11 |
| Chao et collègues 2024, JailbreakBench (2404.01318) | 2310.08419 | 5, 12 |
| Jain et collègues 2023 (2309.00614) ; Alon et Kamfonas 2023 (2308.14132), défenses par perplexité | 2310.08419 | 7, 12 |
| Deng et collègues 2023, « Jailbreaker » / Masterkey (2307.08715) | 2309.10253 | 13, 17 |
| Huang et collègues 2025, « Virus: … bypassing guardrail moderation » (2501.17433) : réglage fin contre un filtre de modération, voisin côté juge | 2502.19537 | 13 |
| Halawi et collègues, réglage fin malveillant dissimulé | 2502.19537 | 3, 13, 20 |
| Davies et collègues 2025, « Fundamental limitations in defending LLM finetuning APIs » (2502.14828) | 2502.19537 | 1, 11 |
| Qi et collègues 2024, durabilité des garde-fous des modèles ouverts (2412.07097) ; Tamirisa et collègues 2024 (2408.00761) ; Rosati et collègues 2024 (2405.14577) | 2502.19537 | 15 ; 16 ; 16 |
| Wang et collègues 2024, classifieur de transcription (2412.02159) | 2502.19537 | 17 |

Les plus proches de HC4, à lire en priorité si la zone est cherchée plus avant : McKenzie et collègues 2025 et Cunningham et collègues 2025 (sondes contre classifieurs), puis Hua et collègues 2025 (moniteurs sous contrainte de coût).

---

## 11. Note à part, sans verdict : ce qui touche HC2

Le système de production de 2601.04603 a une **sonde en premier étage**. Il a été attaqué par contenu en boîte noire (équipe rouge humaine, accès par interface, p. 15) :
- environ 1 736 h et environ 198 000 tentatives ;
- une seule vulnérabilité à haut risque ; découverte minimale en 30 h ;
- aucun jailbreak universel sur les huit questions (p. 9).

Sur le jeu statique, la sonde seule laisse passer environ 1,4 % des attaques (p. 8), et elle signale davantage de requêtes bénignes (p. 8). Pour HC2 (N-068), plusieurs différences comptent :
- la sonde lit le modèle protégé, et l'auteur du contenu adverse est un utilisateur externe, non l'agent ;
- la propriété détectée est un contenu nuisible ;
- l'évasion de la sonde seule n'est pas isolée dans l'équipe rouge vivante ;
- aucune mesure du déplacement continu g.

C'est une matière pour le lecteur de HC2 ; je ne prononce rien à son sujet.
