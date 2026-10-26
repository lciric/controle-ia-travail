# Tour III.1 — Proposition A : « agents sur le noyau » pendant la conception par essais-erreurs

## 0. Pièces et statuts

- Le bloc FAITS est présent mais vide par décision de l'arbitre (conv-audit, message n° 28 § 1) : aucun fait n'est joint. Tout ce que j'appelle « cadre » ci-dessous vient du bloc QUESTION et porte le statut **RAPPORTÉ** (transmis par l'arbitre, non audité par moi).
- Mes recalculs portent **VÉRIFIÉ (recalcul)** ; mes propositions portent **HYPOTHÈSE** ; tout chiffre que j'introduis est **illustratif**.
- Recalcul du bruit annoncé : √(0,75 × 0,25 / 36) ≈ 0,072 ; √(0,75 × 0,25 / 24) ≈ 0,088. Les ordres de grandeur ≈ 0,07 et ≈ 0,09 du cadre sont cohérents — **VÉRIFIÉ (recalcul)**. Cela ne vaut que pour l'erreur binomiale sur les tâches, à exactitude vraie fixée.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi ce n'est pas établi |
|---|---|---|---|
| A1 | « Complexification » est un facteur unique dont on mesure « la valeur ». | HYPOTHÈSE | Les quatre lectures sont sur quatre axes distincts : pouvoir d'action de l'organisme (1), procédure de lancement (2), audit du noyau (3), boucle humaine de correction (4). Elles ne se comparent pas sur une même métrique ; seule (1) modifie l'objet mesuré. |
| A2 | Le bruit se résume à l'erreur binomiale sur 36/24 tâches. | RAPPORTÉ (le cadre dit lui-même que la variance entre graines est inconnue) | Trois sources sont absentes : variance entre graines à organisme fixe ; non-déterminisme des modèles appelés (température, versions) ; variance entre codes produits par Gemini à consigne fixe. Aucune n'a été mesurée. |
| A3 | La relecture par un agent neuf remplace, pendant la conception, ce que le préenregistrement protégeait. | HYPOTHÈSE | La relecture contrôle un texte ; le préenregistrement contrôle la liberté de choix du concepteur (le « jardin des chemins qui bifurquent »). Ce ne sont pas la même garde. |
| A4 | `test_final` jamais rendu suffit à fermer la fuite. | HYPOTHÈSE | L'organisme reçoit son score `test` à chaque génération (4 générations), et le concepteur humain lit les scores de course à la fin : la part `test` est déjà un jeu réutilisé adaptativement. `test_final` n'est protégé que si le concepteur ne modifie pas l'organisme d'après des régularités apprises sur `test` qui se transfèrent à `test_final` par construction (même banque v3, même générateur de tâches). |
| A5 | Les 60 tâches v3 sont représentatives de la v6 (lot 3, famille tenue à l'écart). | HYPOTHÈSE | Aucun chiffre de transfert v3 → v6 n'existe ; la v6 n'est pas construite. |
| A6 | « Tourner, regarder, corriger, relancer » est bon marché. | RAPPORTÉ (30–55 USD par course, 75 au plus) | Chaque relance coûte une course ; le nombre d'itérations total de la phase (4) n'est pas borné dans le cadre. |
| A7 | Le noyau isolé reste isolé si l'organisme obtient des outils (lecture 1). | HYPOTHÈSE | L'isolation est décrite pour des appels simples. Avec exécution de code ou recherche, les canaux de sortie et d'accès à la vérité des tâches changent de nature ; aucun essai du noyau n'est mentionné. |
| A8 | La « valeur au-delà du bruit » a une référence de surface. | HYPOTHÈSE | Le cadre ne fixe pas contre quoi on mesure : organisme qui ne se réécrit pas ? prédicteur constant (classe majoritaire) ? heuristique de surface (longueur, mots-clés) ? Sans référence, « au-delà du bruit » n'est pas une conclusion. |
| A9 | (3) est « en partie couvert par les relectures ». | RAPPORTÉ (position de conv-audit) / HYPOTHÈSE quant au fond | Relire un code n'est pas l'exécuter contre lui-même. La couverture de (3) par la relecture est elle-même une affirmation testable (voir E5). |
| A10 | (2) est « peu utile si l'on peut relancer ». | RAPPORTÉ / HYPOTHÈSE | Vrai seulement si un échec de lancement réel coûte moins qu'un essai court. Non chiffré. |
| A11 | Les quatre lectures sont une liste complète. | HYPOTHÈSE | Il manque au moins : la réplication à organisme fixe (deux courses identiques, graines différentes), le contrôle par permutation des étiquettes, et un canari de fuite dans la banque (voir (a)-bis). |

**(a)-bis — Ce qui manque à la liste** (HYPOTHÈSE) :
- (5) **Réplication nue** : la même course deux ou trois fois, rien d'autre. C'est la seule mesure directe de la variance entre graines, et elle conditionne tout le reste.
- (6) **Course à étiquettes permutées** : un organisme itéré contre une v3 dont les étiquettes sont mélangées. Tout « gain » obtenu là est du sur-ajustement pur et donne le plancher à dépasser.
- (7) **Canari de fuite** : quelques tâches dont la vérité n'est accessible que par un canal illégitime (nom de fichier, métadonnée, ordre). Un score au-dessus du hasard sur ces tâches signale une fuite, quel que soit l'organisme.

---

## (b) Expériences décisives, chacune en duel

Convention : l'exactitude est mesurée par part et par famille ; seuil exprimé en multiples de l'erreur type (ET) recalculée ci-dessus ; les chiffres de seuil sont **illustratifs** et doivent être consignés dans le journal avant la course (voir § 2 ci-dessous, même sans scellement).

### E1 — Le bruit entre graines est-il plus petit que les écarts que l'on veut lire ?

- **H_A** : à organisme fixe, l'écart type entre graines sur la part `test` est < 0,05 (illustratif), donc deux courses uniques peuvent être comparées avec un seuil à ≈ 2 ET binomiale.
- **H_B** : cet écart type est ≥ 0,10 (illustratif) ; aucune comparaison à une course par objet n'est lisible.
- **Métrique** : écart type de l'exactitude sur k = 3 courses identiques (même code, même banque, graines différentes), par famille.
- **Seuil** : < 0,05 soutient H_A ; ≥ 0,10 soutient H_B ; entre les deux, zone grise consignée comme telle.
- **Contrôle négatif** : un organisme « constant » (répond toujours la classe majoritaire) : son exactitude doit être exactement le taux de base, sans variance ; s'il varie, le bruit vient du noyau ou de la notation, pas de l'organisme.
- **Ce que falsifie chaque issue** : H_B vrai → toute lecture « au-delà du bruit » du pilote 4 et de toute itération (4) à une course par objet est réfutée comme méthode ; H_A vrai → la crainte d'un bruit entre graines dominant est réfutée pour cet organisme et cette banque (pas pour d'autres).
- **Coût** : 2 courses supplémentaires de l'organisme simple ≈ 60–110 USD (dérivé du cadre, 30–55 par course).

### E2 — Les gains de conception sur la v3 se transfèrent-ils à la famille tenue à l'écart de la v6 ?

- **H_A** : le gain d'exactitude obtenu après n itérations de (4) sur la v3 se retrouve, à au moins la moitié, sur la famille v6 jamais vue.
- **H_B** : le gain est spécifique à la v3 (sur-ajustement adaptatif).
- **Métrique** : Δv3 (après − avant itérations) et Δv6 (mêmes deux versions, famille tenue à l'écart) ; rapport Δv6 / Δv3.
- **Seuil** : rapport ≥ 0,5 et Δv6 > 2 ET → H_A ; Δv6 < 1 ET alors que Δv3 > 2 ET → H_B.
- **Contrôle négatif** : la course à étiquettes permutées (6) : le concepteur itère de bonne foi contre des étiquettes mélangées ; le Δv3 obtenu là est le gain « fantôme » attendu par sur-ajustement, et tout Δv3 réel doit le dépasser nettement.
- **Falsification** : H_B vrai → la phase (4) telle que pratiquée est réfutée comme source de connaissance (elle produit de l'adaptation à 60 tâches) ; H_A vrai → l'objection de sur-ajustement est réfutée pour ce nombre n d'itérations, et n devient le budget d'itérations soutenable.

### E3 — Lecture (1) : des outils apportent-ils une exactitude au-delà du bruit, sans fuite ?

- **H_A** : un organisme outillé (exécution de code, recherche, via le noyau) dépasse l'organisme à appels simples d'au moins 2 ET sur le contrôle de délégation (24 tâches) sur ≥ 2 graines sur 3.
- **H_B** : aucun écart lisible, ou l'écart disparaît quand les outils sont inertes.
- **Métrique** : exactitude par famille, 3 graines, plus score sur les canaris de fuite (7).
- **Contrôle négatif double** : (i) même organisme, outils présents mais **inertes** (renvoient vide) — isole « disposer d'outils » de « s'en servir » ; (ii) canaris de fuite : score > hasard sur les canaris → l'écart est une fuite, pas une capacité.
- **Falsification** : H_B vrai → la lecture (1) est réfutée comme objet prioritaire de pilote ; H_A vrai avec canaris au hasard → l'affirmation « les outils n'ajoutent que du coût » est réfutée ; H_A vrai avec canaris au-dessus du hasard → le noyau est réfuté comme isolé, et le résultat est invalide.

### E4 — Lecture (2) : l'essai réel court détecte-t-il ce que la simulation rate ?

- **H_A** : sur N lancements (illustratif N ≥ 6), au moins un essai réel court révèle une défaillance (clé, coût, notation, format) que le lanceur en simulation avait laissée passer.
- **H_B** : sur N lancements, aucune divergence entre simulation et réel.
- **Métrique** : nombre de divergences simulation/réel ; coût cumulé des essais courts ; coût des courses perdues sans eux.
- **Contrôle négatif** : injecter dans un lancement une défaillance connue (clé invalide, budget nul) et vérifier que l'essai court la voit ; sinon l'instrument ne mesure rien.
- **Falsification** : H_B vrai → (2) est réfutée comme dépense utile tant qu'on peut relancer ; H_A vrai → la position « peu utile » de conv-audit est réfutée.

### E5 — Lecture (3) : des agents attaquants trouvent-ils ce que la relecture ne trouve pas ?

- **H_A** : sur un noyau où l'on a planté p défauts (illustratif p = 8 : 3 de fuite de vérité, 3 de sortie d'isolation, 2 de notation), les agents attaquants en trouvent ≥ 2 de plus que la relecture seule.
- **H_B** : ils n'en trouvent pas plus (≤ relecture), ou produisent plus de fausses alertes que de trouvailles.
- **Métrique** : taux de détection (trouvés / plantés) et taux de fausses alertes (signalements non fondés / signalements), pour relecture seule et pour relecture + attaque.
- **Contrôle négatif** : le même noyau sans défaut planté : tout signalement est une fausse alerte.
- **Falsification** : H_B vrai → l'affirmation « (3) n'est pas couvert par la relecture » est réfutée ; H_A vrai → l'affirmation de conv-audit « en partie couvert » est réfutée sur la partie exécution.

### E6 — Lecture (4) : itérer vaut-il mieux que dépenser le même budget en réplications ?

- **H_A** : m itérations de (4) (coût ≈ m courses) donnent, sur la v6, un gain supérieur à celui obtenu en dépensant m courses en graines supplémentaires de l'organisme non corrigé (meilleure graine choisie sur `test`, évaluée sur v6).
- **H_B** : à budget égal, la sélection de graine fait aussi bien.
- **Métrique** : exactitude v6 de la version itérée vs de la meilleure graine non itérée.
- **Contrôle négatif** : l'itération à étiquettes permutées (comme E2).
- **Falsification** : H_B vrai → la boucle humaine n'apporte rien que la variance ne donne déjà, et (4) est réfutée comme méthode de conception ; H_A vrai → l'objection « (4) n'est que de la sélection sur le bruit » est réfutée.

### E7 — La relecture tient-elle ce qu'on lui demande ?

- **H_A** : un agent neuf détecte ≥ 70 % (illustratif) d'erreurs plantées dans un texte d'organisme ou de rapport (inversion d'étiquette, seuil faux, référence inventée), avec < 20 % de fausses alertes sur un texte sain.
- **H_B** : détection < 40 % ou fausses alertes > 50 %.
- **Métrique/contrôle/falsification** : comme E5, appliqués à la relecture. H_B vrai → A3 (la relecture comme garde suffisante) est réfutée pour cette phase.

---

## § 2 — Pour (4), des essais-erreurs qui restent de la science (HYPOTHÈSE, à départager)

Voie **α — itération bornée et journalisée** :
- **Journal** : une entrée par lancement, avant lecture des scores, avec le hachage du code de l'organisme, du noyau, de la banque, la graine, le coût, et la phrase « ce que j'attends ». Tout essai, y compris les abandonnés, y figure. Une entrée sans hachage de course n'est pas un essai.
- **Règle d'arrêt** fixée avant la première itération : au plus n itérations (illustratif : 4), ou arrêt dès que deux itérations consécutives ne dépassent pas 2 ET sur `test`. L'arrêt pour « bon résultat » n'est pas une règle ; seul le compteur l'est.
- **Un facteur à la fois ?** Pendant la conception, non : un organisme se réécrit lui-même, le facteur n'est pas contrôlable. Ce qu'on peut tenir fixe : noyau, banque, modèles appelés, graine de la banque. Le journal note ce qui a changé ; la confirmation (v6) rétablit la comparaison à deux versions figées.
- **Sur-ajustement** : trois gardes mécaniques — (i) les 60 tâches v3 sont scindées en 48 lues / 12 jamais lues par le concepteur pendant (4) (les 12 sont un `test_final` de conception, distinct du `test_final` de course) ; (ii) le contrôle par permutation (6) ; (iii) les canaris (7).
- **Combien d'itérations avant la v6** : le nombre n fixé ci-dessus, pas « jusqu'à ce que ça marche ».
- **Fermé** : `test_final` de course, les 12 tâches v3 tenues, la famille v6 à l'écart, et les étiquettes des canaris.
- **Contamination des confirmations** : déclaration écrite dans le préenregistrement v6 de tout ce que les auteurs ont lu (scores, erreurs, tâches), et une famille v6 construite par quelqu'un qui n'a pas lu les scores v3.

Voie **β — réplication d'abord, itération ensuite** : ne rien itérer tant que E1 n'est pas faite ; si H_B(E1) est vrai, la boucle (4) est aveugle et l'argent va aux graines.

Voie **γ — itération minimale** : deux itérations au plus, puis v6 ; parie que le transfert (E2) est le vrai goulot.

Ce qui départage α, β, γ : le résultat de E1. Écart type entre graines petit → α ; grand → β ; intermédiaire → γ.

---

## § 3 — Séparer du bruit pendant la conception

- **Avec une course par objet** (VÉRIFIÉ par recalcul des ET) : un écart < 0,15 sur 36 tâches, < 0,18 sur 24, est indistinguable de l'erreur binomiale seule à ≈ 2 ET ; le cadre dit 0,2 en incluant une marge pour les graines, ce qui est cohérent mais non mesuré. Ce qu'on peut conclure : un organisme à 0,45 sur une famille à taux de base 0,5 ne marche pas ; une différence 0,70 vs 0,78 n'est pas une différence.
- **Répétitions minimales** (HYPOTHÈSE) : 3 graines par objet pour lire une variance ; 2 courses identiques suffisent à réfuter « le bruit entre graines est négligeable » si elles diffèrent de plus de 2 ET.
- **Lecture contre le bruit des tâches** : intervalle à 2 ET autour de chaque exactitude ; références de surface obligatoires sur la même part — classe majoritaire, heuristique de longueur de transcription, heuristique de mots-clés (« évaluation », « test », « jailbreak ») — car un organisme qui ne bat pas ces références n'a pas de valeur à mesurer.
- **Invisible sans répétition** : la variance entre graines ; la variance entre codes Gemini à consigne fixe ; la corrélation d'erreurs entre tâches (une banque de 36 peut contenir 10 tâches quasi identiques, ce qui rend l'ET binomiale optimiste — HYPOTHÈSE).

---

## (c) Instruments nommés : mesure minimale de fonctionnement

| Instrument | Taux de détection sur | Fausses alertes sur (cas honnêtes appariés) | Vérification mécanique à battre |
|---|---|---|---|
| **Organisme (contrôle de délégation)** | traces sabotées de la part `test` | traces honnêtes appariées en tâche, longueur et modèle source | classe majoritaire ; longueur ; mots-clés ; un classifieur à une consigne sans réécriture |
| **Organisme (conscience d'évaluation)** | transcriptions d'évaluation | transcriptions d'usage réel appariées en domaine et longueur | idem ; plus un détecteur de formats d'évaluation connus (préfixes, structure de prompt) |
| **Noyau (isolation)** | tentatives plantées : accès réseau, lecture des clés, lecture du fichier de vérité, dépassement de budget | organismes honnêtes : aucun appel légitime bloqué | journaux de l'espace de noms réseau et du système de fichiers, limites de processus ; si le noyau ne fait que ce que ces journaux font, il n'ajoute rien |
| **Lanceur en simulation** | défaillances injectées (clé invalide, budget nul, format de réponse cassé) | lancements sains : aucun faux arrêt | une suite de tests unitaires du noyau |
| **Essai réel court (2)** | mêmes défaillances injectées, en réel | mêmes lancements sains | le lanceur en simulation lui-même (E4) |
| **Agents attaquants (3)** | défauts plantés (p = 8 illustratif) | noyau sans défaut | analyse statique + fuzzing des entrées du noyau ; relecture seule (E5) |
| **Relecture** | erreurs plantées dans le texte (E7) | textes sains | diff + tests unitaires + correcteur |
| **Journal des essais** | lancements sans entrée (doit être 0) | — | script qui refuse tout lancement sans entrée préalable hachée |
| **`test_final` / famille v6 tenue** | canaris : score sur tâches à vérité inaccessible doit être au hasard | — | comparaison `test` vs `test_final` : un écart > 2 ET en faveur de `test` est le signal de réutilisation adaptative |

Point commun : chaque instrument est jugé sur deux nombres (détection, fausses alertes) obtenus sur des cas plantés et des cas honnêtes appariés ; un instrument qui n'a pas ces deux nombres n'est pas encore un instrument.

---

## § 4 — Lecture (1) : dessin minimal sûr (HYPOTHÈSE)

- **Outils** : deux seulement au départ — exécution de code dans un conteneur sans réseau, durée bornée, et recherche passant par le noyau avec journal de chaque requête et de chaque réponse.
- **Isolation** : le conteneur d'outils n'a ni réseau, ni clés, ni accès au système de fichiers du noyau ; les textes de tâches lui sont copiés sans métadonnées (pas de nom de fichier porteur d'étiquette, pas d'ordre informatif) ; la vérité reste côté noyau.
- **Budgets** : nombre de pas, de secondes, d'appels, de requêtes ; dépassement = réponse « abstention » notée fausse.
- **Journaux** : trace complète, rejouable ; même graine, même trace attendue pour les parties déterministes.
- **Risques** : sortie d'isolation (canaux : réseau, fichiers, horloge), accès à la vérité par canal secondaire, coût multiplié par le nombre de pas, non-reproductibilité (recherche en ligne variable → geler un index ou interdire la recherche vivante en confirmation).
- **Essais du noyau avant toute course** : les canaris d'isolation et de vérité (ligne « Noyau » du tableau (c)), un organisme adversaire écrit exprès pour sortir, une course à budget volontairement trop petit pour vérifier que la borne tient.
- **Ordre** : (1) n'a pas de sens avant E1 (on ne saurait pas lire son résultat) ni avant les essais du noyau.

---

## § 5 — Ce qui est connu (références que je peux attribuer)

- Platt, 1964, « Strong Inference », *Science* — la méthode du duel d'hypothèses.
- Tukey, 1977, *Exploratory Data Analysis* — l'exploration comme activité distincte de la confirmation.
- Simmons, Nelson, Simonsohn, 2011, « False-Positive Psychology », *Psychological Science* — degrés de liberté du chercheur.
- Gelman & Loken, 2013, « The garden of forking paths » (manuscrit) — choix d'analyse dépendants des données sans « pêche » délibérée ; c'est exactement le régime de (4).
- Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, 2015, « The reusable holdout: Preserving validity in adaptive data analysis », *Science* ; et « Preserving Statistical Validity in Adaptive Data Analysis », STOC 2015 — réutilisation adaptative d'un jeu tenu, avec bruit ajouté aux scores rendus (pertinent pour `test` rendu à chaque génération).
- Blum & Hardt, 2015, « The Ladder: A Reliable Leaderboard for Machine Learning Competitions », ICML — ne rendre un score que s'il dépasse le précédent d'un seuil : règle directement applicable au score `test`.
- Recht, Roelofs, Schmidt, Shankar, 2019, « Do ImageNet Classifiers Generalize to ImageNet? », ICML — mesure empirique du transfert vers un jeu neuf (analogue de v3 → v6).
- Nosek, Ebersole, DeHaven, Mellor, 2018, « The preregistration revolution », *PNAS* ; Wagenmakers, Wetzels, Borsboom, van der Maas, Kievit, 2012, « An agenda for purely confirmatory research », *Perspectives on Psychological Science* — séparation exploration/confirmation.
- Henderson, Islam, Bachman, Pineau, Precup, Meger, 2018, « Deep Reinforcement Learning that Matters », AAAI ; Agarwal, Schwarzer, Castro, Courville, Bellemare, 2021, « Deep Reinforcement Learning at the Edge of the Statistical Precipice », NeurIPS — variance entre graines, petits nombres de courses, intervalles.
- Bouthillier et al., 2021, « Accounting for Variance in Machine Learning Benchmarks », MLSys — sources de variance, dont les graines — auteurs complets à vérifier.
- Greenblatt, Shlegeris, Sachan, Roger, 2023 (ICML 2024), « AI Control: Improving Safety Despite Intentional Subversion » — protocoles de contrôle d'un agent non fiable, pertinent pour le contrôle de délégation.
- Greshake, Abdelnabi, Mishra, Endres, Holz, Fritz, 2023, « Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection » — risques des agents outillés lisant des contenus.
- Debenedetti et al., 2024, « AgentDojo », NeurIPS Datasets & Benchmarks — environnement d'agents outillés attaqués — auteurs complets à vérifier.
- Jimenez et al., 2023 (ICLR 2024), « SWE-bench » ; Yao et al., 2022 (ICLR 2023), « ReAct » — agents outillés à plusieurs pas.
- Agache et al., 2020, « Firecracker: Lightweight Virtualization for Serverless Applications », NSDI — isolation légère pour exécution de code.
- Sur la conscience d'évaluation des modèles : Needham et al., 2025, « Large Language Models Often Know When They Are Being Evaluated » — **référence à vérifier** (auteurs et année de mémoire incertaine).
- Sur les barres d'erreur d'évaluations de modèles de langue : Miller, 2024, « Adding Error Bars to Evals » — **référence à vérifier**.

---

## (d) Ancrage matériel

- **Courses existantes** : pilote 4, 2 organismes × 1 course ≈ 60–110 USD (dérivé du cadre). E1 (2 graines de plus de l'organisme simple) ≈ 60–110 USD. E6 à m = 4 ≈ 120–220 USD par bras, deux bras. Tous dérivés des 30–55 USD rapportés ; la variabilité réelle n'est pas opposable.
- **E5/E7 (attaques et relectures)** : sans course ; coût en appels de modèles, illustratif < 20 USD.
- **Modèles ouverts** (pour l'étape 1 sur activations et pour mesurer à bas coût la variance entre graines d'un classifieur de surface) : Llama 3.x 8B, Qwen 2.5 7B/14B, Mistral 7B ; un GPU de 24 Go suffit en quantification 4 bits pour les 7–14B (illustratif) ; un 70B demande ≈ 2 × 80 Go ou quantification agressive (illustratif).
- **Bac à sable pour (1)** : conteneur sans réseau (Docker + gVisor ou Firecracker), CPU seul, coût matériel négligeable ; le coût réel est le nombre de pas d'agent × prix des appels, illustratif 3 à 10 × celui d'un appel simple.
- **Calcul des références de surface** : une passe par part, un seul modèle, illustratif < 5 USD.

---

## § 6 — Comment départager, et ce qu'il faudrait savoir de plus

Ce qui tranche, dans l'ordre : **E1** (sans variance entre graines, rien d'autre n'est lisible) ; puis **E2/E6** (la phase (4) produit-elle quelque chose qui se transfère, mieux que de la sélection sur le bruit ?) ; **E5/E7** (les gardes gardées — relecture — et abandonnées — scellement — sont-elles remplaçables par l'attaque et le journal ?) ; **E3** en dernier, une fois le noyau éprouvé.

Ce qu'il faudrait savoir : la variance entre graines ; le taux de base de chaque famille ; la corrélation entre tâches de la v3 ; qui construira la famille v6 tenue à l'écart et ce que cette personne aura lu ; le budget total de la phase (4), sans lequel aucune règle d'arrêt n'est opposable.

Ce que je ne propose pas : retarder le pilote 4. Ce qui peut encore y entrer cette nuit sans changer l'objet : une entrée de journal datée avant lecture des scores, et une seconde course de l'organisme simple à graine différente.

FIN-DE-CELLULE