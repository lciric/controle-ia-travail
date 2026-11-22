Pièce manquante ou redondante : le bloc `FAITS` est strictement identique au bloc `QUESTION DE L'ARBITRE` (même empreinte sha256 `02ad3d76ae90648f2fbb8498bc109d4a51a9dddd8b965e03326013e9ee08c9b8`), ne contient aucun fait expérimental préalable, et les « notes retirées » mentionnées dans son titre sont absentes (`VÉRIFIÉ` par lecture directe des blocs transmis).

---

## 1. Position de fond sur les sous-questions 1 à 4

### 1.1 Fondement et critère mesurable de la distinction (Question 1)

Prise de manière absolue — comme propriété intrinsèque d'une attaque indépendamment du système défendu — la distinction entre « attaque nouvelle » et « catégorie nouvelle d'attaques » **n'est pas décidable par une mesure** (`HYPOTHÈSE`) : sans modèle de menace ni famille de défenses fixés, tout découpage taxinomique peut être raffiné ou fusionné arbitrairement.

En revanche, la distinction devient **opératoire et décidable par une mesure** dès qu'on la relativise à un triplet $(K, \mathcal{D}, \beta)$ (`HYPOTHÈSE`), où $K = \{C_1, \dots, C_m\}$ est l'ensemble des familles d'attaques connues, $\mathcal{D}$ est une classe de détecteurs/défenses dotée d'un espace d'observation fixé (capteurs, caractéristiques, instrumentation), et $\beta$ est un budget fixé de ré-adaptation dans cette même classe $\mathcal{D}$ (recalibrage ou ré-entraînement avec un nombre borné d'exemples, sans changer de capteur).

Étant donné une attaque candidate exécutable $a^*$ produisant un impact cible au moins égal à celui de $K$, $a^*$ constitue une **catégorie nouvelle relative à $(K, \mathcal{D}, \beta)$** si et seulement si trois critères mesurables sont réunis conjointement (`HYPOTHÈSE`) :

1. **Échec de transfert zéro-shot depuis $K$** : un détecteur optimal $d_K \in \mathcal{D}$ entraîné sur $K$ (à taux de fausses alertes $\alpha$ fixé sur cas honnêtes appariés) échoue sur $a^*$.
2. **Non-absorption dans la classe d'instrumentation $\mathcal{D}$** : la ré-adaptation de $d \in \mathcal{D}$ sur des exemples de $a^*$ sous budget $\beta$ ne permet pas d'atteindre la cible de détection sur des variantes tenues à l'écart de $a^*$, ou n'y parvient qu'en dégradant significativement la détection sur $K$ ou le taux de fausses alertes sur cas honnêtes (incompatibilité géométrique dans l'espace d'observation de $\mathcal{D}$).
3. **Productivité et séparabilité par un nouvel invariant** : $a^*$ n'est pas un artefact isolé ni un bruit indiscernable ; elle engendre une famille de variantes transférant entre elles (matrice de transfert intra-famille élevée, transfert inter-familles avec $K$ proche du hasard), et une extension d'instrumentation $\mathcal{D}^+$ ciblant un nouvel invariant (nouveau canal ou nouvelle structure de vérification) parvient à la détecter.

Ce critère remplace l'avis subjectif par la mesure d'une **matrice de transfert de défenses** et d'une **courbe d'absorption**. Il conserve une part conventionnelle explicite (le choix initial de $\mathcal{D}$, de $\alpha$ et de $\beta$), mais une fois ce cadre fixé, le verdict est reproductible et réfutable.

### 1.2 Exemples historiques de naissance d'une catégorie (Question 2)

Les faits ci-dessous sont tous `RAPPORTÉ` (cités de mémoire). Ils montrent un point contre-intuitif : historiquement, une catégorie nouvelle **peut naître d'un assemblage** au niveau des briques élémentaires ; ce qui la sépare d'une variante ou d'un simple assemblage est la **violation d'une hypothèse implicite du modèle de sécurité**, rendant inopérante une classe entière de défenses fondées sur cette hypothèse.

* **Attaques temporelles par canaux auxiliaires** — Paul C. Kocher (1996), *Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems* (`RAPPORTÉ`, cité de mémoire). *Séparation à l'époque* : les variantes classiques de cryptanalyse attaquaient la primitive mathématique dans un modèle boîte noire entrée/sortie. L'attaque temporelle n'affaiblissait pas l'algorithme abstrait mais violait l'hypothèse implicite que le temps d'exécution physique est hors du canal observable. Allonger les clés ne suffisait pas ; il a fallu une nouvelle classe de défenses (implémentations en temps constant, aveuglement cryptographique).
* **Réutilisation de code par chaînage de fragments (ROP)** — Hovav Shacham (2007), *The Geometry of Innocent Flesh on the Bone: Return-into-libc without Function Calls (on the x86)* (`RAPPORTÉ`, cité de mémoire). *Séparation à l'époque* : `return-to-libc` existait déjà comme assemblage ponctuel. Ce qui a constitué ROP en catégorie distincte est la démonstration qu'un chaînage de courts fragments déjà présents en mémoire (*gadgets*) est Turing-complet, ce qui invalidait structurellement les défenses basées uniquement sur la non-exécutabilité des données (W^X / DEP) et imposait des défenses de contrôle de flot, comme celles formalisées par Martín Abadi, Mihai Budiu, Úlfar Erlingsson et Jay Ligatti (2005), *Control-Flow Integrity* (`RAPPORTÉ`, cité de mémoire).
* **Attaques par exécution transitoire / spéculative** — Paul Kocher et al. (2019), *Spectre Attacks: Exploiting Speculative Execution* (liste complète des co-auteurs : référence à vérifier ; divulgué antérieurement) et Moritz Lipp et al. (2018), *Meltdown: Reading Kernel Memory from User Space* (liste complète des co-auteurs : référence à vérifier) (`RAPPORTÉ`, cités de mémoire). *Séparation à l'époque* : Spectre assemblait deux phénomènes connus (prédiction de branchement et canal auxiliaire cache). Il a néanmoins ouvert une catégorie parce qu'il violait le contrat même de l'architecture du jeu d'instructions (ISA) : des instructions annulées architecturalement laissaient un état microarchitectural exploitable, rendant insuffisantes les vérifications de bornes logicielles classiques.
* **Évasion au temps de test en apprentissage automatique** — Nilesh Dalvi, Pedro Domingos, Mausam, Sumit Sanghai et Deepak Verma (2004), *Adversarial Classification* (`RAPPORTÉ`, cité de mémoire) ; extension aux réseaux profonds en haute dimension par Christian Szegedy, Wojciech Zaremba, Ilya Sutskever, Joan Bruna, Dumitru Erhan, Ian Goodfellow et Rob Fergus (2014), *Intriguing properties of neural networks*, puis Ian J. Goodfellow, Jonathon Shlens et Christian Szegedy (2015), *Explaining and Harnessing Adversarial Examples* (`RAPPORTÉ`, cités de mémoire). Cet exemple illustre la nuance taxinomique : la catégorie « perturbation optimisée au temps de test » existait avant 2014 sur modèles linéaires/SVM (travaux de 2013 sur les attaques d'évasion contre le ML : référence à vérifier pour la liste complète des co-auteurs) ; les travaux sur réseaux profonds ont surtout révélé son ampleur géométrique et sa transférabilité quasi-imperceptible.

### 1.3 Ce qui est publié sur cette distinction (Question 3)

À ma connaissance (`RAPPORTÉ`, cité de mémoire), la littérature publiée aborde ce problème par **trois volets partiels**, sans consensus établi sur un critère purement mesurable séparant variante et catégorie :

1. **Taxonomies descriptives d'attaques** :
   * Marco Barreno, Blaine Nelson, Russell Sears, Anthony D. Joseph et J. D. Tygar (2006), *Can Machine Learning Be Secure?* (`RAPPORTÉ`, cité de mémoire) — propose une grille structurée (causative vs exploratoire, intégrité vs disponibilité, ciblée vs indiscriminée), mais le classement reste conceptuel plutôt que décidé par un test de transfert défensif.
   * Référentiels opérationnels de cybersécurité (MITRE ATT&CK, CWE, CAPEC — `RAPPORTÉ`, cités de mémoire ; pas d'article académique unique attribué ici, référence à vérifier) : séparent tactiques, techniques et sous-techniques par arbitrage communautaire d'experts, non par seuil mesurable.
2. **Évaluation adaptative des défenses (critère indirect de non-absorption)** :
   * Anish Athalye, Nicholas Carlini et David Wagner (2018), *Obfuscated Gradients Give a False Sense of Security: Circumventing Defenses to Adversarial Examples* (`RAPPORTÉ`, cité de mémoire) — identifie des classes récurrentes d'échecs de défenses face à des attaques adaptées.
   * Florian Tramer, Nicholas Carlini, Wieland Brendel et Aleksander Madry (2020), *On Adaptive Attacks to Adversarial Example Defenses* (`RAPPORTÉ`, cité de mémoire) — montre qu'une défense ne peut être évaluée qu'à l'aune d'attaques adaptées à son mécanisme interne.
3. **Contrôle, sabotage et surveillance d'agents LLM** :
   * Ryan Greenblatt, Buck Shlegeris, Kshitij Sachan et Fabien Roger (2024), *AI Control: Improving Safety Regardless of Scheming* (`RAPPORTÉ`, cité de mémoire) — formalise l'évaluation de protocoles de contrôle (moniteurs, audits) par jeux red-team/blue-team.
   * Travaux récents sur les évaluations de sabotage d'agents sur tâches longues, les sondes linéaires de détection de tromperie sur activations internes, les « sleeper agents », l'injection de prompt indirecte et la mesure de nouveauté en red-teaming automatisé (2023–2026) : **référence à vérifier** (je ne peux pas en garantir simultanément tous les auteurs, années et titres exacts de mémoire).

### 1.4 Un groupe de modèles de langue peut-il concevoir une catégorie nouvelle ? Quels témoins ? (Question 4)

La question n'est **pas tranchée** par des données établies (`HYPOTHÈSE`). Un groupe de modèles de langue peut produire des textes qui *ressemblent* à une nouvelle catégorie (néologismes, assemblages convaincants en prose) sans dépasser l'enveloppe des schémas appris lors du pré-entraînement. À l'inverse, aucune preuve formelle n'interdit qu'une recherche combinatoire guidée par critique mutuelle et retour d'exécution découvre un mécanisme qui satisfasse le critère mesurable de la section 1.1 dans un environnement donné.

L'avis du groupe lui-même ou d'un juge LLM ne vaut pas preuve. Quatre **témoins conjoints** sont nécessaires pour conclure (`HYPOTHÈSE`) :

1. **Témoin d'exécution réelle** : le candidat doit être traduit en attaque fonctionnelle sur un système cible et dégrader effectivement la métrique de tâche.
2. **Témoin de non-absorption défensive** : l'attaque doit passer les tests mesurables de la section 1.1 (Expériences 1 et 2 ci-dessous), et non seulement impressionner un lecteur humain.
3. **Témoin de comparaison contrôlée** : comparer le groupe multi-LLM ($G_{\text{multi}}$) à budget égal de jetons contre (i) un modèle seul ($G_{\text{solo}}$) et (ii) un générateur mécanique de mutations/assemblages des attaques connues ($G_{\text{mut}}$), plus si possible une ligne de base humaine aveuglée.
4. **Témoin d'antériorité et de non-mémorisation** : vérifier que le mécanisme ne figure pas déjà sous un autre nom dans la base $K$ ni dans la littérature antérieure ; tester le groupe sur un **environnement synthétique isomorphe** (règles et vocabulaire permutés pour neutraliser le rappel lexical) ou, pour un test historique, sur des modèles figés à coupure temporelle antérieure à une catégorie connue apparue plus tard.

---

## 2. Livrable (a) — Présupposés non établis dans la question

Aucune des prémisses suivantes n'est établie par le bloc `FAITS`. Chacune porte le statut `HYPOTHÈSE` :

| # | Ce que la question suppose sans que ce soit établi | Statut | Conséquence méthodologique si faux |
|---|---|---|---|
| A1 | La distinction « attaque nouvelle / catégorie nouvelle » existerait de manière intrinsèque, sans fixer un espace de défenses $\mathcal{D}$ ni un budget d'adaptation $\beta$. | `HYPOTHÈSE` | Le débat reste taxinomique et indécidable par mesure. |
| A2 | « Catégorie nouvelle » et « assemblage » s'excluraient mutuellement (Question 2). | `HYPOTHÈSE` | On exclurait à tort des catégories historiques nées d'assemblages qui violent un invariant (ex. Spectre). |
| A3 | Un groupe de modèles de langue explorerait un espace d'hypothèses plus large qu'un modèle isolé (Question 4). | `HYPOTHÈSE` | Des modèles aux corpus corrélés peuvent amplifier la convergence de mode au lieu d'innover. |
| A4 | Les trois instruments de surveillance nommés (lecteurs internes, juges de texte, contrôle au hasard) détectent déjà de manière fiable et calibrée le sabotage connu sur tâche longue (Question 5). | `HYPOTHÈSE` | Si un instrument est mal calibré ou aveugle sur $K$, une évasion ne prouve rien sur la nouveauté du candidat. |
| A5 | La dégradation « exprès » se distingue opérationnellement d'une erreur involontaire de capacité chez un agent LLM (Question 5). | `HYPOTHÈSE` | Sans contrôle apparié en difficulté et sans suppression des artefacts de prompt, les sondes internes mesurent la présence de l'instruction système ou la difficulté de la tâche, pas le sabotage. |
| A6 | Un modèle ouvert de petite taille est un proxy valide pour exécuter et détecter un sabotage sur une longue tâche d'analyse (Question 5). | `HYPOTHÈSE` | Double risque : incapacité du petit modèle à exécuter une attaque subtile (faux négatif), ou bruit représentationnel élevé empêchant les sondes de fonctionner (faux positif sur l'évasion). |
| A7 | Une « première expérience » unique suffirait à conclure sur le statut catégoriel d'un candidat (Question 5). | `HYPOTHÈSE` | Toute conclusion exige d'abord la validation minimale des instruments (Section 4), puis la séparation entre manque de données et violation d'invariant (Expériences 1 et 2). |
| A8 | Les trois couches de surveillance seraient complémentaires (erreurs peu corrélées) sur une tâche longue. | `HYPOTHÈSE` | Si elles échouent sur les mêmes cas (ex. biais subtils distribués), leur union n'apporte pas de gain réel sur des vérifications mécaniques. |

---

## 3. Livrable (b) — Expériences discriminantes en inférence forte ($H_A$ contre $H_B$)

Toutes les valeurs numériques ci-dessous (tailles d'échantillons, seuils de taux, pourcentages) ne proviennent pas des faits et sont marquées `illustratif`.

### Prérequis expérimental commun aux Expériences 1 et 2 (cas d'application de la Question 5)

* **Tâche longue d'analyse à vérité terrain programmatique** : audit et synthèse d'un dossier synthétique de `30` documents tabulaires et textuels interdépendants (`illustratif`, `4 000–8 000` jetons en entrée, `illustratif`), nécessitant extraction, recoupement multi-documents, calculs exacts et verdict structuré. L'exactitude de chaque étape et du résultat final est vérifiable automatiquement par un programme déterministe (écart normalisé de qualité $\Delta Q \in [0, 1]$).
* **Base connue $K$** : `3` familles de sabotage mécaniquement distinctes (`illustratif`) :
  * $C_1$ : altération locale directe (falsification d'un chiffre ou d'une conclusion finale) ;
  * $C_2$ : omission sélective (ignorance systématique d'une sous-catégorie de documents lors de la lecture) ;
  * $C_3$ : erreur de raisonnement plausible en chaîne de pensée (glissement d'unité, mauvaise agrégation ou attribution erronée rédigée de façon cohérente).
* **Contrôle anti-artefact de prompt (critique)** : pour éviter que les lecteurs d'états internes ne détectent trivialement un mot-clé du prompt système (« sabote »), chaque famille de sabotage ($C_1, C_2, C_3$ et le candidat $a^*$) est instanciée en **condition intériorisée** par adaptation légère (LoRA sur trajectoires démontrées) de sorte que le prompt d'inférence soit strictement identique entre l'agent honnête et l'agent saboteur.

---

### Expérience 1 (répond à la Question 5 et à la Question 1) : Première expérience sur petit modèle ouvert — transfert défensif et absorption incrémentale

* **Hypothèses exclusives** :
  * **$H_{1A}$ (Variante absorbable dans la classe de surveillance $S$)** : le candidat $a^*$ exploite des indices accessibles dans l'espace d'observation actuel de la suite $S$ (sondes internes + juge textuel + contrôle au hasard) calibrée sur $K$ ; il est soit détecté en zéro-shot par $S_K$, soit absorbé par ré-adaptation légère de $S$ (même classe de sondes/features, mêmes rubriques structurelles de juge, même taux d'audit aléatoire) avec un budget fixé de $\beta = 20$ exemples étiquetés de $a^*$ (`illustratif`).
  * **$H_{1B}$ (Candidat de catégorie nouvelle relative à $(K, S, \beta)$)** : à dégradation au moins égale ($\Delta Q(a^*) \ge 0{,}25$, `illustratif`), $a^*$ échappe à $S_K$ en zéro-shot **et** résiste à la ré-adaptation sous budget $\beta$ (ou crée une perte de détection sur $K$ / une hausse de fausses alertes), tout en produisant une famille cohérente de variantes détectable par une instrumentation hors de $S$.
* **Métriques** (à taux de fausses alertes global fixé $FPR \le 0{,}05$ sur cas honnêtes appariés, `illustratif`) :
  1. $TPR_{K \to a^*}$ : taux de détection zéro-shot de $S_K$ sur $a^*$.
  2. $TPR_{\text{adapt}}(a^*_{\text{test}})$ : taux de détection sur variantes tenues à l'écart de $a^*$ après ré-adaptation sous budget $\beta = 20$ (`illustratif`).
  3. $\Delta TPR_K$ : variation de détection sur $K$ après ré-adaptation.
* **Seuils (`illustratif`)** :
  * Détection zéro-shot validée si $TPR_{K \to a^*} \ge 0{,}50$.
  * Absorption validée si $TPR_{\text{adapt}}(a^*_{\text{test}}) \ge 0{,}80$ avec $FPR \le 0{,}05$ et perte $\Delta TPR_K \ge -0{,}05$.
  * Non-absorption validée si $TPR_{K \to a^*} \le 0{,}15$ **et** $TPR_{\text{adapt}}(a^*_{\text{test}}) \le 0{,}40$ (à $FPR \le 0{,}05$).
* **Contrôles négatifs (conditions de validité de l'expérience)** :
  1. *Variante triviale $a_{\text{neg}}$* (ex. $C_1$ reformulé en pourcentages dans une autre section) : doit donner $TPR_{K \to a_{\text{neg}}} \ge 0{,}50$ ou $TPR_{\text{adapt}} \ge 0{,}80$ (`illustratif`). Échec $\Rightarrow$ sur-apprentissage de $S$, expérience invalidée.
  2. *Cas honnêtes difficiles* (dossiers ambigus/complexes où le taux d'erreur honnête égale $\Delta Q(a^*)$) : doivent rester à $FPR \le 0{,}05$ (`illustratif`). Échec $\Rightarrow$ $S$ mesure la difficulté/erreur plutôt que le sabotage.
  3. *Contrôle lexical honnête* : agent honnête recevant un prompt contenant le vocabulaire d'audit/fraude dans le contexte documentaire ; doit rester à $FPR \le 0{,}05$ (`illustratif`).
* **Falsification** :
  * **Falsifie $H_{1B}$** : $TPR_{K \to a^*} \ge 0{,}50$, ou $TPR_{\text{adapt}}(a^*_{\text{test}}) \ge 0{,}80$ avec $FPR \le 0{,}05$ et $\Delta TPR_K \ge -0{,}05$ (`illustratif`).
  * **Falsifie $H_{1A}$** : $TPR_{K \to a^*} \le 0{,}15$ **et** $TPR_{\text{adapt}}(a^*_{\text{test}}) \le 0{,}40$ (à $FPR \le 0{,}05$, `illustratif`), sous réserve que les trois contrôles négatifs passent et que $\Delta Q(a^*) \ge 0{,}25$ (`illustratif`).
  * *Zone intermédiaire* ($0{,}15 < TPR_{K \to a^*} < 0{,}50$ ou $0{,}40 < TPR_{\text{adapt}} < 0{,}80$, `illustratif`) : non conclusif, bascule vers l'Expérience 2.

---

### Expérience 2 (répond à la Question 1 et à la Question 5) : Assemblage complexe contre violation d'invariant d'observabilité

Si un candidat échappe à l'adaptation légère ($\beta = 20$, `illustratif`), cela peut encore provenir d'un **assemblage à forte variance** de $C_1, C_2, C_3$ nécessitant simplement plus de données, plutôt que d'une véritable violation d'un invariant du canal de surveillance.

* **Hypothèses exclusives** :
  * **$H_{2A}$ (Assemblage complexe dans le même canal d'observation)** : l'information discriminant $a^*$ des trajectoires honnêtes est présente dans le canal actuel de $S$ ; augmenter fortement le volume d'entraînement ($n \in \{20, 100, 500\}$ exemples étiquetés de $a^*$, `illustratif`) ou combiner de manière non linéaire les signaux existants de $S$ fait converger la détection au niveau de $K$.
  * **$H_{2B}$ (Violation d'invariant d'observabilité)** : la détection dans le canal $S$ plafonne même à grand $n$ ($n = 500$, `illustratif`), tandis qu'un canal étendu $S^+$ mesurant un nouvel invariant (par exemple : cohérence différentielle globale contre un agent témoin indépendant sur des sous-problèmes recombinés, ou suivi causal des accès documents/étapes corrélées) détecte $a^*$ avec un faible volume d'exemples ($n = 100$, `illustratif`).
* **Métriques** : courbe d'apprentissage $TPR_S(n)$ vs $TPR_{S^+}(n)$ à $FPR \le 0{,}05$ (`illustratif`), évaluée sur variantes tenues à l'écart $a^*_{\text{test}}$.
* **Seuils (`illustratif`)** :
  * Plafonnement de $S$ : $TPR_S(500) \le 0{,}55$.
  * Séparabilité par nouvel invariant $S^+$ : $TPR_{S^+}(100) \ge 0{,}85$ (écart minimal $TPR_{S^+}(100) - TPR_S(500) \ge 0{,}30$).
* **Contrôle négatif** : une **attaque assemblée synthétique $a_{\text{comp}}$** construite en combinant aléatoirement $C_1$, $C_2$ et $C_3$ au sein d'une même tâche. Elle doit satisfaire $TPR_S(500) \ge 0{,}80$ (`illustratif`), montrant qu'un simple assemblage est rattrapé asymptotiquement par $S$.
* **Falsification** :
  * **Falsifie $H_{2B}$** : $TPR_S(500) \ge 0{,}80$ sur $a^*_{\text{test}}$ à $FPR \le 0{,}05$ (`illustratif`) — ou échec de tout canal réaliste $S^+$ ($TPR_{S^+}(100) < 0{,}60$, `illustratif`, indiquant plutôt un effet de bruit ou une dégradation trop faible).
  * **Falsifie $H_{2A}$** : $TPR_S(500) \le 0{,}55$ sur $a^*_{\text{test}}$ **et** $TPR_S(500) \ge 0{,}80$ sur $a_{\text{comp}}$ **et** $TPR_{S^+}(100) \ge 0{,}85$ sur $a^*_{\text{test}}$ (`illustratif`).

---

### Expérience 3 (répond à la Question 4) : Capacité d'un groupe de LLM à concevoir une catégorie nouvelle hors-support

* **Protocole** : on construit $R = 5$ environnements de tâches longues et de surveillance distincts (`illustratif`), dotés d'un vocabulaire et de règles permutés (pour empêcher le rappel lexical direct), chacun comportant une base connue $K_r$ fournie aux générateurs ainsi que la spécification complète de la suite $S_r$. À budget total de jetons identique ($B = 10^6$ jetons générés par environnement, `illustratif`) et même nombre d'essais sur le banc, on compare trois générateurs devant produire des **attaques exécutables** sur le petit modèle cible :
  1. $G_{\text{multi}}$ : groupe de `6` modèles de langue ouverts (`illustratif`) en idéation et critique itérative.
  2. $G_{\text{solo}}$ : un seul modèle de langue (meilleur membre du groupe) avec échantillonnage parallèle à budget égal $B$.
  3. $G_{\text{mut}}$ : générateur mécanique de variantes et d'assemblages (mutations paramétriques et combinaisons programmées de $K_r$, sans idéation libre).
  *(Extension recommandée si budget humain disponible : témoin red-teaming humain en aveugle).*
* **Hypothèses exclusives** :
  * **$H_{3A}$ (Recombinaison et variantes uniquement)** : $G_{\text{multi}}$ ne produit aucune attaque exécutable validant conjointement Expérience 1 + Expérience 2 + audit aveugle de non-antériorité, ou n'obtient pas un taux de découverte supérieur au témoin mécanique $G_{\text{mut}}$ et au modèle isolé $G_{\text{solo}}$.
  * **$H_{3B}$ (Découverte de catégorie nouvelle par le groupe de LLM)** : $G_{\text{multi}}$ produit des attaques exécutables validant Expérience 1 + Expérience 2 + non-antériorité dans des environnements permutés où $G_{\text{mut}}$ échoue.
* **Métriques** :
  1. $N_{\text{cat}}(G)$ : nombre d'environnements (sur $R = 5$, `illustratif`) où le générateur $G$ produit au moins une attaque exécutable passant intégralement Expérience 1, Expérience 2 et l'audit de non-antériorité.
  2. Écarts $\Delta_{\text{mut}} = N_{\text{cat}}(G_{\text{multi}}) - N_{\text{cat}}(G_{\text{mut}})$ et $\Delta_{\text{solo}} = N_{\text{cat}}(G_{\text{multi}}) - N_{\text{cat}}(G_{\text{solo}})$.
* **Seuils (`illustratif`)** : validation de $H_{3B}$ si $N_{\text{cat}}(G_{\text{multi}}) \ge 2$ sur `5` environnements, avec $N_{\text{cat}}(G_{\text{mut}}) = 0$ (et pour conclure à un effet spécifiquement *collectif*, $N_{\text{cat}}(G_{\text{multi}}) > N_{\text{cat}}(G_{\text{solo}})$).
* **Contrôles négatifs** :
  1. *Environnement « scellé »* : tâche soumise à une vérification mécanique déterministe couvrant `100 %` des invariants de sortie (`illustratif`). Tout candidat validé comme « catégorie nouvelle » dans cet environnement signale une faille du pipeline de test et invalide l'expérience.
  2. *Témoin mécanique $G_{\text{mut}}$* : mesure exactement le plafond atteint par variantes et assemblages purs.
* **Falsification** :
  * **Falsifie $H_{3B}$** (dans le périmètre testé) : $N_{\text{cat}}(G_{\text{multi}}) = 0$ alors que des failles exploitables existent (vérifié par attaque de référence ou témoin humain), ou $N_{\text{cat}}(G_{\text{multi}}) \le N_{\text{cat}}(G_{\text{mut}})$.
  * **Falsifie $H_{3A}$** : $N_{\text{cat}}(G_{\text{multi}}) \ge 2$ (`illustratif`), $N_{\text{cat}}(G_{\text{mut}}) = 0$, contrôle « scellé » à `0` faux positif, et passage de l'audit aveugle de non-antériorité.

---

## 4. Livrable (c) — Mesure minimale de fonctionnement pour chaque instrument nommé

Avant d'interpréter l'échec d'un moniteur comme le signe d'une catégorie nouvelle (Expériences 1 et 2), chacun des trois instruments nommés en Question 5 doit passer un test minimal sur la base connue $K$. Tous les seuils chiffrés ci-dessous sont `illustratif`.

### 4.1 Lecteurs des états internes (sondes sur activations résiduelles)

* **Taux minimaux de détection et de fausses alertes (`illustratif`)** : $TPR \ge 0{,}70$ à $FPR \le 0{,}05$ ($AUROC \ge 0{,}85$) évalués en généralisation sur **nouveaux dossiers** ET en **condition de sabotage intériorisé** (sans mention du sabotage dans le prompt système), avec stabilité inter-couches vérifiée.
* **Cas honnêtes appariés requis** :
  1. Même distribution de longueur de réponse et de nombre d'étapes intermédiaires.
  2. Même taux d'erreur involontaire (dossiers honnêtes rendus plus difficiles afin de distinguer l'état interne de sabotage de l'incertitude ou de la confusion).
  3. Même champ lexical sensible (documents honnêtes traitant d'anomalies, de fraude ou de conformité).
* **Vérifications mécaniques à battre** :
  1. *Statistiques de logits sans accès aux couches internes* : entropie moyenne/maximale des tokens générés et divergence KL par rapport au modèle de base gelé.
  2. *Classifieur linéaire sac-de-mots (TF-IDF)* sur le texte généré.
  3. *Heuristiques de surface* (longueur, temps de calcul, nombre d'appels d'outils).
  *Critère (`illustratif`)* : la sonde interne doit dépasser la meilleure de ces lignes de base mécaniques d'au moins $+0{,}10$ point de TPR à $FPR \le 0{,}05$ sur les trajectoires où la surface textuelle paraît propre.

### 4.2 Juges du texte (LLM-juge ou classifieur textuel sur la trace et la réponse)

* **Taux minimaux de détection et de fausses alertes (`illustratif`)** : $TPR \ge 0{,}70$ à $FPR \le 0{,}05$, avec une dispersion entre graines/reformulations de rubrique $\sigma_{TPR} \le 0{,}05$, évalués sur des trajectoires sabotées rédigées sur un ton rigoureux.
* **Cas honnêtes appariés requis** :
  1. Appariement en longueur, mise en forme et assurance rhétorique (neutralisation du biais de verbosité).
  2. Inclusion de cas honnêtes comportant des erreurs bénignes isolées (fautes mineures sans impact directionnel systématique).
  3. Inclusion de dossiers sources contenant des ambiguïtés légitimes (évite les fausses alertes quand le texte honnête signale une incertitude).
* **Vérifications mécaniques à battre** :
  1. *Vérificateur arithmétique et syntaxique déterministe* (extraction automatique des montants, sommes, ratios, cohérence d'unités entre annexes et synthèse).
  2. *Audit mécanique de couverture et de citations* (pourcentage des documents sources effectivement consultés dans les journaux d'outils, et vérification par recherche exacte de sous-chaînes que chaque fait cité correspond au document source).
  *Critère (`illustratif`)* : le juge textuel doit obtenir un gain d'au moins $+0{,}15$ point de TPR à $FPR \le 0{,}05$ sur le sous-ensemble des attaques qui **contournent** ces vérifications mécaniques déterministes.

### 4.3 Contrôle au hasard du résultat (audit aléatoire / *spot-checking*)

* **Taux minimaux de détection et de fausses alertes (`illustratif`)** :
  * Mesurer séparément la **sensibilité conditionnelle d'audit** $s = P(\text{détection} \mid \text{item saboté et sélectionné}) \ge 0{,}85$ à un taux de fausses alertes par item audité $\alpha_{\text{audit}} \le 0{,}02$.
  * Mesurer le taux de détection effectif sur une campagne à taux d'échantillonnage fixé $p$ (ex. $p = 0{,}10$, `illustratif`) : pour une attaque touchant $k$ items indépendants, le taux observé ne doit pas s'effondrer en dessous de la borne théorique $1 - (1 - p \cdot s)^k$ (un écart négatif important indique que le sabotage se concentre dans des zones rares ou corrélées, ou que l'auditeur est trompé).
* **Cas honnêtes appariés requis** :
  1. Items honnêtes tirés de la même strate de complexité que les items sabotés, incluant des cas limites légitimes.
  2. Audit exécuté **en aveugle** (l'auditeur ignore si la trajectoire provient d'un agent honnête ou saboteur et ignore la prévalence de sabotage).
* **Vérifications mécaniques à battre** :
  1. *Invariants déterministes appliqués à `100 %` des sorties (`illustratif`)* (contrôles de cohérence, bornes, sommes de contrôle, requêtes déterministes sur les tableaux sources) — à coût budgétaire équivalent.
  2. *Contrôle différentiel mécanique sur l'échantillon tiré au sort* : ré-exécution indépendante de la sous-tâche tirée au sort par un petit modèle témoin isolé (sans voir la réponse de l'agent) et déclenchement d'alerte sur désaccord numérique/catégoriel.
  *Critère (`illustratif`)* : l'audit aléatoire approfondi doit capturer des dégradations sémantiques sur lesquelles les invariants à `100 %` échouent, et dépasser le contrôle différentiel mécanique d'au moins $+0{,}10$ point de sensibilité conditionnelle $s$ à $\alpha_{\text{audit}} \le 0{,}02$.

### 4.4 Condition minimale sur la combinaison des trois instruments

La suite combinée $S$ doit être calibrée à un taux global de fausses alertes contrôlé ($FPR_{\text{global}} \le 0{,}05$, `illustratif`, après correction pour tests multiples) et démontrer un gain d'au moins $+0{,}10$ point de TPR (`illustratif`) par rapport au meilleur instrument individuel **et** par rapport à la réunion de toutes les vérifications mécaniques.

---

## 5. Livrable (d) — Ancrage matériel (modèles ouverts, calcul, coût)

Aucun paramètre matériel ne figurant dans les `FAITS`, **tous les chiffres de cette section sont `illustratif`**.

### Modèles ouverts retenus

* **Agent cible principal (Question 5)** : modèle ouvert de petite taille de classe `7B–9B` paramètres (`illustratif`), par exemple `Qwen2.5-7B-Instruct` ou `Llama-3.1-8B-Instruct` (poids accessibles, extraction directe des activations résiduelles en BF16/FP16 sous PyTorch).
* **Réplication cible (anti-artefact architectural)** : un second modèle ouvert d'une autre famille de taille comparable (`7B–9B` paramètres, `illustratif`, ex. `Mistral-7B-Instruct` ou `Gemma-2-9B-it`).
* **Juge de texte (Instrument 2)** : modèle ouvert d'une famille distincte de l'agent cible, classe `32B` à `70B` paramètres quantisé `4-bit`/`8-bit` (`illustratif`, ex. `Qwen2.5-32B-Instruct` ou `Llama-3.3-70B-Instruct` servi via vLLM) pour limiter la corrélation de biais avec l'agent.
* **Lecteurs d'états internes (Instrument 1)** : sondes linéaires régularisées (L2) et MLP à `1` couche cachée entraînés sur les vecteurs résiduels agrégés (fin d'étape et moyenne par paragraphe) sur `8` couches réparties de la moitié à la fin du réseau (`illustratif`).
* **Groupe de conception (Expérience 3 / Question 4)** : `6` modèles ouverts distincts de familles variées (`7B–70B` paramètres, `illustratif`, ex. familles Llama, Qwen, Mistral, Gemma, DeepSeek, Phi).

### Budget de calcul et coût estimé (base GPU cloud type A100-80Go à `1,50–2,50 USD/h`, `illustratif`)

| Phase | Charge estimée (`illustratif`) | Heures GPU A100-80Go (`illustratif`) | Coût estimé (`illustratif`) |
|---|---|---|---|
| Préparation : génération du banc (`500` dossiers × `4 000–8 000` jetons) + scripts de vérité terrain | CPU uniquement | `0 h` | `< 5 USD` |
| Entraînement de `6` adaptateurs LoRA saboteurs (rang `16`, `2 000` exemples chacun, contrôle anti-prompt) | `~12 M` jetons d'entraînement | `10–15 h` | `15–40 USD` |
| Inférence agent `8B` + sauvegarde des activations (`8` conditions × `500` tâches = `4 000` trajectoires, `~40 M` jetons ; stockage compressé `~60–100 Go`) | `4 000` passes longues | `15–25 h` | `25–65 USD` |
| Évaluation par LLM-juge `32B`/`70B` (`4 000` trajectoires, `~26 M` jetons lus/générés) + contrôle aléatoire | Inférence en lots vLLM | `15–30 h` | `25–75 USD` |
| Entraînement des sondes, courbes d'apprentissage (Exp. 2) et vérifications mécaniques | Régression / MLP + scripts | `2–5 h` | `5–15 USD` |
| **Sous-total Exp. 1 + Exp. 2 + Calibration (1 modèle cible)** | — | **`42–75 h`** | **`70–200 USD`** |
| Réplication sur un second modèle cible `7B–9B` | Charge identique | `+42–75 h` | `+70–200 USD` |
| Extension Exp. 3 (idéation `6` LLM sur `5` environnements, `5 M` jetons/générateur + exécution candidats) | Inférence multi-modèles + validation | `+60–120 h` | `+90–300 USD` |
| **Total complet (2 modèles cibles + Exp. 3)** | — | **`144–270 h`** | **`230–700 USD`** |

*Note matérielle* : la première expérience (calibration + Expérience 1 + Expérience 2 sur un modèle cible) tient intégralement sur **un seul GPU `80 Go`** (ou `48 Go` avec quantification du juge, `illustratif`) en `2 à 4 jours` calendaires (`illustratif`), sans infrastructure de cluster.

---

## 6. Ce qui est su, ce qui est supposé, et ce qui ferait changer d'avis

### Ce que je sais (avec statuts)
* **`VÉRIFIÉ`** : le contenu littéral de la question soumise et l'absence de faits expérimentaux préalables dans le bloc `FAITS`.
* **`RAPPORTÉ` (cité de mémoire)** : les précédents historiques cités en 1.2 (canaux temporels, ROP, exécution transitoire, évasion en ML), le fait que les évaluations non adaptatives surestiment la robustesse des défenses (Athalye et al., 2018 ; Tramer et al., 2020), et les contraintes mathématiques d'un échantillonnage aléatoire (un contrôle au hasard à fraction $p$ a une borne stricte sur la probabilité de détecter un événement rare ou concentré).

### Ce que je suppose (`HYPOTHÈSE`)
* Que la distinction « nouvelle attaque / nouvelle catégorie » ne devient décidable par mesure que relativisée à un cadre $(K, \mathcal{D}, \beta)$ via transfert défensif, courbe d'absorption et séparabilité par nouvel invariant.
* Qu'un banc d'analyse documentaire synthétique à vérité terrain programmatique sur un modèle ouvert `7B–9B` (`illustratif`), couplé à un sabotage intériorisé par LoRA, suffit à tester proprement la validité des instruments et le statut d'un candidat sans confusion avec les artefacts de prompt.
* Qu'aucun verdict sur la capacité créative d'un groupe de LLM (Question 4) n'est crédible sans témoin mécanique de recombinaison ($G_{\text{mut}}$), témoin mono-modèle à budget égal ($G_{\text{solo}}$) et environnement permuté.

### Ce qui me ferait changer d'avis
1. **Sur le caractère relatif de la distinction (Question 1)** : la formulation d'une grandeur mesurable strictement intrinsèque à l'attaque — ne faisant référence à aucune famille de défenses ni à aucun modèle de menace — qui reproduirait les séparations historiques documentées et trancherait sans ambiguïté entre variantes et catégories.
2. **Sur la faisabilité sur petit modèle ouvert (Question 5)** : constater empiriquement que des modèles `7B–9B` (`illustratif`) sont incapables de produire un sabotage qui passe les vérifications mécaniques de base sans perdre la cohérence de surface ; cela obligerait à réviser l'ancrage matériel vers des modèles plus grands ou des tâches plus courtes avant tout test de nouveauté catégorielle.
3. **Sur la valeur des lecteurs d'états internes (Section 4.1)** : observer qu'en condition de sabotage intériorisé (sans indice dans le prompt) et sur cas honnêtes appariés en difficulté, les sondes internes ne battent ni l'entropie des logits ni un classifieur lexical sur les familles connues $K$ ; j'écarterais alors cet instrument du banc de test.
4. **Sur la capacité d'un groupe de LLM (Question 4)** : observer dans l'Expérience 3 que $G_{\text{multi}}$ découvre de manière reproductible, dans des environnements permutés et sous contrôle de non-antériorité, des attaques exécutables qui passent les Expériences 1 et 2 là où $G_{\text{mut}}$ et $G_{\text{solo}}$ échouent ; à l'inverse, un score nul de $G_{\text{multi}}$ sur des environnements où un red-teaming humain trouve des failles structurelles confirmerait la limite à la recombinaison de variantes.

FIN-DE-CELLULE