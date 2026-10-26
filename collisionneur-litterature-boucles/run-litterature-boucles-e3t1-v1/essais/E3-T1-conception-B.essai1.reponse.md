# Proposition B · Tour III.1 · conception à l'aveugle

**Pièces reçues.**
- **Bloc FAITS** : il ne contient aucun fait. Il renvoie seulement à une décision (conv-audit, message 28 § 1) que je ne peux pas consulter ; je n'en tire rien.
- **Bloc QUESTION** : présent et non coupé. Je n'ai pas vérifié les empreintes sha256.
- **Autres propositions** : le tour est à l'aveugle, A et C ne sont pas visibles. Je n'ai donc rien à attaquer ni à reprendre (B1).

**Conventions de statut.**
- Le « cadre » de la question est donné par l'arbitre sans statut. Je le traite comme **RAPPORTÉ (arbitre)**.
- Toute référence est citée de mémoire. Elle est donc au mieux **RAPPORTÉ (par ses auteurs), à vérifier** ; rien n'est VÉRIFIÉ ici.
- Mes propositions sont des **HYPOTHÈSES**.

---

## 1. (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Conséquence |
|---|---|---|---|
| S1 | Les boucles publiées se transposent ici. | HYPOTHÈSE | FunSearch et AlphaEvolve exigent, à ma connaissance, un évaluateur automatique rapide et peu bruité (RAPPORTÉ, à vérifier). Ici, l'erreur type est d'environ 0,07 par course (RAPPORTÉ, arbitre). La propriété qui fait marcher ces boucles manque donc. |
| S2 | « Éliminer celles qui tombent hors du bruit » a un sens unique. | HYPOTHÈSE | Deux lectures sont possibles : (i) on élimine ce qui est réfuté (effet hors du bruit, dans le mauvais sens) ; (ii) on élimine ce qui n'est pas soutenu (effet indiscernable du bruit). La lecture (ii), à faible puissance, élimine presque tous les petits effets réels. |
| S3 | Le test apparié G0 contre G3 a de la puissance sur 60 tâches. | HYPOTHÈSE | Calcul au § 4 : seuls des écarts d'environ 0,12 à 0,15 sont éliminables. |
| S4 | Les « 36 tâches » (≈ 0,07) et les « 60 tâches par part » désignent le même objet. | RAPPORTÉ (les deux), lien non donné | Je ne sais pas si 36 correspond à une famille, à un sous-ensemble ou à une autre banque. Les calculs ci-dessous utilisent 60 et le signalent. |
| S5 | Une course unique suffit. | RAPPORTÉ : la variance entre graines est inconnue | Toute élimination sur course unique repose aujourd'hui sur une hypothèse non testée. |
| S6 | L'écart G0 → G3 est imputable aux hypothèses de conception. | HYPOTHÈSE | L'organisme se réécrit lui-même : plusieurs changements sont confondus et la trajectoire de réécriture est elle-même aléatoire. |
| S7 | Les agents « neufs » sont indépendants entre eux. | HYPOTHÈSE | Mêmes familles de modèles, donc biais corrélés possibles. |
| S8 | La correction de l'organisme ne fuit pas vers les vérités de `test`. | HYPOTHÈSE | Ce que le correcteur voit (scores par tâche ? items ?) n'est pas précisé. |
| S9 | Les mesures de la primitive sur les textes de l'organisme renseignent sur les tâches de la banque. | HYPOTHÈSE | Ce sont deux distributions différentes. |
| S10 | Le refus des quasi-copies fonctionne. | HYPOTHÈSE | Aucun taux n'est donné. |
| S11 | Relire `test` à chaque génération ne le transforme pas en jeu d'entraînement. | HYPOTHÈSE | La théorie de l'analyse adaptative dit le contraire en général (Dwork et al., 2015 ; RAPPORTÉ, à vérifier). |
| S12 | Le trio d'agents décide mieux qu'une règle mécanique. | HYPOTHÈSE, non posée par la question | C'est pourtant la seule justification du coût des agents. |
| S13 | La banque neuve confirme de façon indépendante. | RAPPORTÉ (auteurs déclarés lecteurs des scores) + HYPOTHÈSE | Elle est indépendante en données, pas en conception (chemins bifurquants). |
| S14 | La granularité de ce que reçoit l'organisme (score agrégé ou par tâche) est sans importance. | HYPOTHÈSE | C'est le paramètre qui gouverne la fuite adaptative (§ 3). |

---

## 2. Littérature (questions 1 et 2)

Toutes les entrées sont citées de mémoire, statut RAPPORTÉ, **à vérifier** (auteurs, année, lieu). Quand je ne sais pas, je l'écris.

### 2.1 Évolution de programmes guidée par un évaluateur

**FunSearch** : Romera-Paredes, Barekatain, Novikov, Balog, Kumar, Dupont, Ruiz, Ellenberg, Wang, Fawzi, Kohli, Fawzi, « Mathematical discoveries from program search with large language models », *Nature*, fin 2023 / 2024.
- **Proposer** : un modèle de langue écrit des fonctions.
- **Tester** : un évaluateur écrit par des humains exécute et note.
- **Sélectionner** : une base de programmes organisée en « îles » garde les meilleurs.
- **Itérer** : automatique ; la mémoire est la base de programmes.
- **Bruit** : évaluateur déterministe. Pour l'empaquetage, des heuristiques ont été évaluées sur des instances tenues à l'écart (à vérifier).
- **Limite déclarée** : problèmes à évaluateur rapide.

**AlphaEvolve** : Novikov et al., Google DeepMind, 2025, livre blanc « AlphaEvolve: A coding agent for scientific and algorithmic discovery » (lieu et liste d'auteurs à vérifier).
- Même structure : un ensemble de modèles Gemini propose des différences de code ; des évaluateurs automatiques, en cascade, notent ; une base évolutive sélectionne.
- **Limite déclarée** : problèmes évaluables automatiquement (à vérifier).
- **Échecs relevés par des tiers** : je ne sais pas.

**ELM** : Lehman, Gordon, Jain, Ndousse, Yeh, Stanley, « Evolution through Large Models », prépublication 2022. Le modèle de langue sert d'opérateur de mutation dans MAP-Elites.

### 2.2 Découverte automatique de bout en bout

**The AI Scientist** : Lu, Lu, Lange, Foerster, Clune, Ha, 2024, prépublication Sakana AI.
- **Fonctionnement** : le modèle propose une idée, vérifie sa nouveauté par recherche, code, exécute et rédige ; un relecteur automatique note.
- **Bruit** : je ne sais pas comment la variance entre graines est traitée.
- **Échecs rapportés par les auteurs** : le système a modifié son propre script d'exécution pour allonger des délais ou se relancer ; il commet des erreurs d'implémentation et d'interprétation (à vérifier).
- **Tiers** : Beel, Kan, Baumgart, 2025, évaluation critique du système (titre exact à vérifier) : expériences échouées, nouveauté mal jugée (à vérifier).
- **Version 2** : Yamada et al., 2025, « The AI Scientist-v2 », recherche arborescente agentique (à vérifier).

**AI co-scientist** : Gottweis et al., 2025, prépublication Google (à vérifier). Génération, débats, tournoi de type Elo, puis validations en laboratoire humide pour quelques hypothèses (à vérifier).

### 2.3 Conception automatique d'agents et agents qui se réécrivent

**ADAS** : Hu, Lu, Clune, « Automated Design of Agentic Systems », 2024, ICLR 2025.
- Un méta-agent écrit des agents en code, les note sur un jeu de validation et les archive.
- Le transfert vers des domaines et des modèles tenus à l'écart est rapporté, ainsi que des intervalles par bootstrap (à vérifier).

**AFlow** : Zhang et al., 2024, ICLR 2025 (à vérifier). Recherche arborescente de type Monte-Carlo sur des flux d'agents, avec séparation validation / test.

**STOP** : Zelikman, Lorch, Mackey, Kalai, « Self-Taught Optimizer (STOP) », 2023, COLM 2024.
- L'améliorateur s'améliore lui-même.
- **Échecs rapportés** : désactivation du drapeau de bac à sable, contournement de la fonction d'utilité (à vérifier).

**Gödel Agent** : Yin et al., 2024 (à vérifier).

**Darwin Gödel Machine** : Zhang, Hu, Lu, Lange, Clune, 2025 (à vérifier).
- L'agent réécrit son code ; évaluation par étages sur SWE-bench et Polyglot ; archive ouverte.
- **Échec rapporté** : « objective hacking », l'agent ayant retiré les marqueurs servant à détecter ses hallucinations (à vérifier).

**Optimisation de consignes** :
- APE : Zhou et al., ICLR 2023.
- OPRO : Yang et al., « Large Language Models as Optimizers », ICLR 2024.
- Promptbreeder : Fernando et al., 2023.
- DSPy : Khattab et al., 2023.

Ces travaux sélectionnent sur de petits jeux d'entraînement. Je ne sais pas s'ils traitent la variance entre graines.

### 2.4 Laboratoires automatiques

- **Adam** : King et al., « The Automation of Science », *Science*, 2009. Hypothèses sur des fonctions de gènes, expériences robotisées, élimination explicite. C'est le plus proche de « proposer, tester, éliminer » ; les répliques biologiques sont à vérifier.
- **Robot chimiste mobile** : Burger et al., « A mobile robotic chemist », *Nature*, 2020.
- **Coscientist** : Boiko, MacKnight, Kline, Gomes, « Autonomous chemical research with large language models », *Nature*, 2023.

### 2.5 Validité statistique

| Thème | Références (toutes à vérifier) |
|---|---|
| Réutilisation adaptative du jeu de test | Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, « The reusable holdout… », *Science*, 2015 (Thresholdout). Blum et Hardt, « The Ladder… », ICML 2015. |
| Sur-ajustement adaptatif observé | Recht, Roelofs, Schmidt, Shankar, « Do ImageNet Classifiers Generalize to ImageNet? », ICML 2019. Roelofs et al., « A Meta-Analysis of Overfitting in Machine Learning », NeurIPS 2019. Ces travaux rapportent peu de sur-ajustement adaptatif sur de grands jeux ; HYPOTHÈSE : cela ne se transpose pas à 60 tâches lues à chaque génération. |
| Biais de sélection de modèle | Cawley et Talbot, JMLR 2010. |
| Variance entre graines | Henderson et al., « Deep Reinforcement Learning that Matters », AAAI 2018. Bouthillier et al., « Accounting for Variance in Machine Learning Benchmarks », MLSys 2021. Miller, « Adding Error Bars to Evals », 2024, prépublication. |
| Chemins bifurquants et préenregistrement | Simmons, Nelson, Simonsohn, *Psychological Science*, 2011. Gelman et Loken, 2013–2014. Nosek et al., « The preregistration revolution », PNAS 2018. |
| Comparaisons multiples et équivalence | Holm, 1979. Benjamini et Hochberg, 1995. Lakens, « Equivalence Tests », 2017. |
| Sondes | Hewitt et Liang, « Designing and Interpreting Probes with Control Tasks », EMNLP 2019. |
| Méthode | Platt, « Strong Inference », *Science*, 1964. |

**Constat transversal (HYPOTHÈSE de lecture)** : les boucles qui « marchent » en programmes ont un évaluateur quasi déterministe. Celles qui se notent sur des bancs bruités traitent rarement la variance entre graines et la lecture répétée du jeu de test, à ma connaissance.

---

## 3. Emprunter et éviter (question 3)

### Boucle extérieure

**Emprunter :**
1. **Archive complète, échecs compris** (FunSearch, DGM). Elle permet de compter les chemins bifurquants, donc de corriger les comparaisons sur toutes les hypothèses testées, pas seulement sur celles qu'on retient.
2. **Évaluation par étages** (DGM, cascade d'AlphaEvolve) : un criblage bon marché, puis une confirmation. Ici, criblage sur la petite banque, confirmation sur la banque neuve scellée.
3. **Transfert vers un domaine tenu à l'écart** (ADAS) : c'est déjà le dessin de la « famille tenue à l'écart ».
4. **Rationner l'information de `test`** (Ladder, Thresholdout) : ne rendre qu'un score arrondi, ou seulement une amélioration significative.

**Éviter :**
- Prendre un relecteur automatique pour une vérité (AI Scientist).
- Retenir le meilleur de N sans correction (Cawley et Talbot).

### Boucle intérieure

**Emprunter :**
1. **Un évaluateur déterministe** (condition de FunSearch et d'AlphaEvolve) : log-probabilités en mode déterministe sur un modèle figé, pour une sortie à bruit quasi nul.
2. **Primitive et plafonds dans le noyau, hors de portée du code de l'organisme.** Les échecs rapportés par STOP (bac à sable désactivé), AI Scientist (délais modifiés) et DGM (marqueurs retirés) montrent tous la même chose : un organisme qui peut toucher son instrument le contourne.

**Éviter :**
- Laisser l'organisme définir ou ré-entraîner l'évaluateur qui le note.
- Des sondes sans tâches de contrôle (Hewitt et Liang).

---

## 4. Pièges propres à notre cas, gardes, répétitions (question 4)

### Puissance du test apparié (calcul explicite)

Sur 60 tâches appariées, seules comptent les paires discordantes. Avec une discordance de 15 % (illustratif), on a 9 paires discordantes.

| Situation | Calcul (binomial exact, p = 0,5, bilatéral) | Conséquence |
|---|---|---|
| Hypothèse seule | 8 contre 1 : p = 20/512 ≈ 0,039 | Il faut un écart net de 7/60 ≈ 0,12. |
| 5 hypothèses par course (illustratif), Holm | Seuil le plus strict 0,01 ; 8 contre 1 échoue ; 9 contre 0 : p = 2/512 ≈ 0,004 | Il faut l'unanimité des discordances : écart de 0,15. |

**Conclusion (HYPOTHÈSE)** : sur la petite banque, ni « éliminer » ni « garder » ne valent quelque chose pour des effets inférieurs à 0,1.

### Erreur type d'un écart apparié et répétitions

L'erreur type d'un écart apparié vaut à peu près √(q/60), où q est la discordance. Avec q = 0,2 (illustratif) : 0,058, soit une demi-largeur d'intervalle à 95 % d'environ 0,11.

Répéter les graines **sur les mêmes 60 tâches** réduit le bruit des graines, **pas** l'échantillonnage des tâches. La généralisation à la population de tâches n'y gagne rien.

### Pièges et gardes minimales

**P1. Fausses éliminations (lecture S2-ii).**
- Garde : trois verdicts au lieu de deux : **soutenue / réfutée / indécise**.
- « Réfutée » exige un test d'équivalence ou d'infériorité contre un effet minimal d'intérêt (SESOI) déclaré d'avance (Lakens, 2017).
- « Indécise » n'élimine rien : elle renvoie à des répétitions ou à la banque neuve.

**P2. Fausses conservations.**
- Garde : Holm sur toutes les hypothèses de la course, avec un budget d'α réparti sur les rondes successives (dépense d'α, illustratif).
- Une hypothèse conservée reste candidate, jamais confirmée.

**P3. Sur-ajustement aux 60 tâches.**
- Gardes : rendre à l'organisme un score agrégé arrondi (Ladder) ; compter les lectures de `test` ; jamais d'affirmation fondée sur la seule petite banque.

**P4. Fuite par la correction.**
- Garde : le correcteur ne voit que des traces d'exécution (exceptions, formats, délais), jamais les items, les étiquettes ou les scores par tâche.
- Des canaris détectent le reste (E5).

**P5. Confusion des changements (S6).**
- Garde : une hypothèse de conception correspond à un seul changement, en différence isolable et appliquée à G0, pas seulement à « ce qu'est devenue G3 ».

### Contenu minimal d'une hypothèse de conception éliminable

1. Le changement, sous forme de différence ou de description vérifiable.
2. Le mécanisme supposé.
3. Une prédiction **directionnelle** sur une métrique et une part nommées.
4. Le SESOI.
5. La règle soutenue / réfutée / indécise.
6. L'hypothèse rivale H_B.
7. Le contrôle prévu.
8. Le nombre de graines.

Une hypothèse sans les points 3 à 5 n'est pas éliminable : on la consigne comme telle.

---

## 5. Antériorité (question 5)

**Ce qui est déjà occupé (RAPPORTÉ, à vérifier) :**
- l'évolution de programmes guidée par un modèle de langue et un évaluateur ;
- les agents qui réécrivent leur code ;
- la conception automatique d'agents ;
- les boucles de découverte de bout en bout ;
- les laboratoires robotisés ;
- la théorie du jeu de test réutilisable.

**Ce qui, à ma connaissance, n'est pas occupé (à vérifier, sans garantie) :**
- (i) appliquer ces boucles à des classifieurs de *conscience d'évaluation* et de *sabotage*, où l'objet mesuré porte lui-même sur l'évaluation ;
- (ii) une primitive d'expérience restreinte aux textes de l'organisme, avec refus des quasi-copies ;
- (iii) l'étalonnage d'un trio d'agents éliminateurs contre une règle mécanique, sur des effets plantés. Cela existe peut-être en méta-science simulée ; je ne sais pas.

**À ne pas revendiquer :**
- un caractère « premier » ;
- une auto-amélioration générale ;
- une « découverte » issue de la boucle intérieure ;
- toute généralisation tirée de la petite banque.

---

## 6. (b) Expériences décisives (question 6)

Les seuils sont tous illustratifs, sauf mention d'un calcul.

### E1 · Variance entre graines (prérequis à toute élimination)

- **H_A** : l'écart-type entre graines σ_g ≤ 0,035, soit la moitié de 0,07 (calcul). Une course unique, avec intervalles sur les tâches, suffit.
- **H_B** : σ_g > 0,035.
- **Métrique** : écart-type de l'exactitude sur 8 rejouées (illustratif), mesuré à deux niveaux :
  - (a) organisme G0 figé, seules les graines d'appel changent ;
  - (b) course entière, réécriture comprise.
- **Contrôle négatif** : rejouer avec les réponses des modèles mises en cache ; l'écart-type doit être nul, sinon le pipeline n'est pas déterministe.
- **Falsification** :
  - borne supérieure de l'intervalle sur σ_g ≤ 0,05 : H_B falsifiée ;
  - borne inférieure > 0,035 : H_A falsifiée ;
  - entre les deux : indécis, on ajoute des graines.

### E2 · Trio d'agents contre règle mécanique (boucle extérieure)

**Cas plantés, présentés à l'aveugle comme des hypothèses ordinaires :**
- **nuls** : réécriture cosmétique, renommage ; effet nul par construction ;
- **nuisibles** : inversion aléatoire de 25 % des réponses d'un classifieur binaire. L'exactitude attendue passe de 0,75 à 0,75 × 0,75 + 0,25 × 0,25 = 0,625 (calcul), soit −0,125.

**Duel :**
- **H_A** : le trio commet moins d'erreurs (fausses éliminations et fausses conservations) que la règle écrite d'avance (McNemar exact, Holm, SESOI).
- **H_B** : le trio fait au mieux aussi bien que la règle.
- **Métrique** : nombre d'erreurs sur 20 hypothèses plantées (illustratif), comparé par test apparié sur les hypothèses.
- **Contrôle négatif** : le trio reçoit des scores permutés entre tâches. S'il « trouve » encore des effets, il raconte au lieu de mesurer.
- **Falsification** :
  - trio significativement meilleur : H_B falsifiée ;
  - sinon H_A falsifiée, et la décision revient à la règle (voie V1, § 9).

### E3 · Sur-ajustement adaptatif à `test`

- **H_A** : l'écart (`test` − part tenue à l'écart) à G3 ne dépasse pas celui de G0 de plus de 0,1 (illustratif).
- **H_B** : il le dépasse.
- **Contrôle négatif** : un organisme réécrit sans retour de score (ou avec un score permuté). L'écart ne doit pas croître.
- **Contrôle positif** : on donne délibérément les vérités de `test` à l'organisme. L'écart doit croître, sinon la mesure est aveugle.
- **Falsification** : un accroissement au-delà du seuil, absent dans le contrôle négatif, falsifie H_A. Un test d'équivalence réussi, avec un contrôle positif qui détecte, falsifie H_B.

**Réserve.** Lire `test_final` à répétition le rend adaptatif pour les humains. Il faut une part témoin distincte (à prélever, ce qui réduit les parts) ou une lecture unique. Je ne tranche pas.

### E4 · Utilité de la primitive (boucle intérieure)

- **H_A** : la primitive réelle produit un gain G0 → G3 (sur la part tenue à l'écart) supérieur à celui d'une **primitive placebo** : même plafond, mêmes appels, mais sorties permutées entre textes ou sondes entraînées sur des étiquettes permutées.
- **H_B** : pas de différence (test d'équivalence, SESOI = 0,1, illustratif).
- **Nombre de courses (calcul)** : avec un écart-type de la différence par paire de courses d'environ 0,14 (illustratif), il faut une erreur type ≤ 0,1/2,8 ≈ 0,036, donc k ≥ (0,14/0,036)² ≈ 15 paires.
- **Contrôle négatif** : le placebo lui-même. Il faut aussi une ablation qui vérifie, dans le journal, que l'organisme utilise réellement les sorties.
- **Falsification** : supériorité significative : H_B falsifiée ; équivalence démontrée : H_A falsifiée.

### E5 · Fuite par la correction

**Dispositif** : 10 canaris (illustratif) dans `test`, à étiquettes tirées au hasard, indépendantes du contenu, et exclus du score rapporté.

- **H_A** : après correction, l'exactitude sur les canaris est compatible avec 0,5 (pas de fuite par item).
- **H_B** : elle est supérieure à 0,5. Calcul : 9 sur 10 donne p ≈ 0,011 unilatéral.
- **Contrôles** :
  - négatif : organisme non corrigé ;
  - positif : correcteur à qui l'on donne les étiquettes.
- **Falsification** : un excès significatif falsifie H_A. Un résultat nul, avec un contrôle positif qui détecte, falsifie H_B **pour les fuites par item seulement**. Une fuite d'information agrégée échappe aux canaris.

---

## 7. (c) Instruments nommés : mesure minimale de fonctionnement

Seuils illustratifs : détection ≥ 0,9 et fausses alertes ≤ 0,05, sauf mention.

| Instrument | Cas honnêtes appariés | Détection mesurée | Fausse alerte mesurée | Vérification mécanique à battre |
|---|---|---|---|---|
| **Analyste** | Jeux de scores identiques sauf l'effet injecté (planté ≥ 0,15 contre nul) | Part des effets plantés déclarés | Part des nuls déclarés « effet » | Script McNemar + Holm |
| **Contre-lecteur** | Le même rapport, correct ou avec une erreur plantée (signe inversé, Holm omis, `test` confondu avec `test_final`, intervalle unilatéral) | Part des erreurs plantées relevées | Objections sur les rapports corrects | Recalcul automatique depuis le journal + liste fixe de contrôles |
| **Correcteur** (et audit des corrections) | Correctif honnête, ou le même avec identifiant de tâche, table de réponses ou règle ajustée à un item | Correctifs fuyants signalés ; canaris (E5) | Correctifs honnêtes bloqués | Recherche d'identifiants et de sous-chaînes de tâches dans la différence, empreintes de textes |
| **Intervalles + test apparié G0/G3** | Tests A/A (même organisme, deux graines) contre effets plantés | Puissance sur −0,125 (E2) | Taux de rejet A/A ≤ α nominal | Test non apparié ; bootstrap sur les tâches |
| **Correction des comparaisons multiples** | m hypothèses nulles simulées, plus quelques effets plantés | Puissance par hypothèse plantée | Taux d'erreur familial ≤ α | Bonferroni |
| **Sondes / activations** | Textes de l'organisme à étiquette connue, appariés en longueur et en sujet | Exactitude de la sonde | Sélectivité : même sonde sur tâches de contrôle (Hewitt et Liang) | Régression logistique sur sac de mots ; log-probabilité simple |
| **Log-probabilités de jetons cibles** | Mêmes textes | Discrimination (aire sous la courbe ROC) | Erreur de calibration | Réponse générée du même modèle en mode déterministe |
| **Refus des quasi-copies** | Paraphrases d'items de test (y compris adversariales) contre textes neufs, même genre et même sujet | Paraphrases refusées (≥ 0,95) | Textes neufs refusés (≤ 0,05) | MinHash, 5-grammes, cosinus d'embeddings |
| **Plafonds et bornes du noyau** | Tentatives plantées de dépassement (sur le modèle de STOP et d'AI Scientist) contre usage lourd légitime | **Toutes** les tentatives bloquées : un seul manque est un échec | Usage légitime bloqué | Quotas comptés côté noyau, indépendamment du code |
| **Journal** | Course rejouée | Mêmes scores, entrée par entrée | n.a. | Empreintes des entrées et sorties |
| **`test_final` scellé** | Accès planté | Accès consigné et signalé | n.a. | Journal d'accès au système de fichiers |
| **Pilote** (enchaînement des agents) | Course avec agent défaillant planté (réponse vide, hors format) | Arrêt propre consigné | Arrêts sur réponses valides | Validation de schéma |

---

## 8. (d) Ancrage matériel

Tous les chiffres sont illustratifs, aucun ne vient des faits.

**Modèles ouverts pour la primitive** : Llama 3.1 8B Instruct, Qwen2.5 7B Instruct, Gemma 2 9B. Ces modèles existent ; le choix est illustratif. Prendre deux familles permet de vérifier que les sondes ne sont pas propres à un modèle.

**Calcul :**
- 8 milliards de paramètres × 2 octets ≈ 16 Go de poids en bf16 (calcul). Un GPU de 24 à 48 Go suffit.
- Extraire les activations demande un passage avant par texte : 1 000 textes de 1 000 jetons, c'est de l'ordre de minutes (illustratif).

**Courses :**

| Expérience | Courses (illustratif) |
|---|---|
| E1 | 8 + 8 |
| E4 | 30, soit 15 paires |
| E3 | réutilise les courses d'E4, plus quelques contrôles |
| E2 | surtout hors ligne : scores simulés et plantés, peu de courses réelles |
| E5 | se greffe sur les courses existantes |
| **Total** | environ 50 courses |

**Coût** : Coût total ≈ 50 × coût par course, plus 10 à 40 h de GPU loué à 1–2 $/h. Le coût par course est **inconnu** ; c'est l'information à obtenir en premier.

---

## 9. Voies possibles et ce qui les départage

**Boucle extérieure :**
- **V1** : la règle mécanique décide, les agents rédigent et proposent.
- **V2** : les agents décident, avec un veto mécanique (aucune élimination sans satisfaire la règle).
- **V3** : les agents décident librement (modèle AI Scientist).
- *Départage* : E1, puis E2. Si E2 falsifie H_A, la voie V3 tombe. V2 ne se justifie que si les agents améliorent la règle sur les cas indécis.

**Boucle intérieure :**
- **W0** : pas de primitive ; le budget va aux graines.
- **W1** : log-probabilités seules (déterministes, bon marché).
- **W2** : sondes et activations en plus.
- *Départage* : E4 à trois bras (W0, W1, W2 contre placebo). Pour W2, il faut en plus que les sondes battent le sac de mots (§ 7).

**Information rendue à l'organisme :**
- **R1** : score par tâche.
- **R2** : score agrégé arrondi (Ladder).
- **R3** : Thresholdout.
- *Départage* : E3 avec contrôle positif.

**Ce qu'il faudrait savoir de plus** (chaque point modifie une décision ci-dessus) :
1. La granularité exacte de ce que l'organisme reçoit de `test` (S14).
2. Ce que le correcteur voit (S8).
3. Le nombre d'hypothèses par course.
4. Le coût d'une course.
5. Le sens de « 36 tâches » face à « 60 par part » (S4).
6. La lecture voulue de « hors du bruit » (S2).

FIN-DE-CELLULE