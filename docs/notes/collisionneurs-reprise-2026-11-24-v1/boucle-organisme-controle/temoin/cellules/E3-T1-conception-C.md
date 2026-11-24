*Note d'intégrité et pièces absentes :* les éléments issus du dossier transmis portent le statut `RAPPORTÉ` (aucun journal d'audit n'accompagne le dossier), les résultats mathématiques/statistiques établis portent le statut `VÉRIFIÉ`, les prémisses ou assertions non testées portent le statut `HYPOTHÈSE` (ou `OBSERVÉ-NON-AUDITÉ` lorsqu'une propriété empirique est invoquée sans vérification), et mes choix de conception portent la mention `PROPOSITION`. **Pièces absentes du dossier** : l'architecture interne exacte de l'organisme d'idéation, la composition précise de ses corpus, le budget GPU chiffré, la taille $N$ de la référence honnête et les performances actuelles des détecteurs ne figurent pas dans les faits transmis ; je ne les invente pas et j'indique « je ne sais pas » lorsqu'une réponse en dépend. Conformément à la règle d'intégrité, aucun identifiant arXiv n'est donné de mémoire (`pas sûr`).

---

## 1. Analyse d'expert

Un spécialiste en idéation scientifique automatisée et en contrôle boîte blanche ne commencerait pas par dessiner un tuyau d'échange entre les deux systèmes : il examinerait d'abord **l'incompatibilité structurelle entre une boucle d'optimisation fermée et un protocole de contrôle à lecture unique**.

1. **Le paradoxe de la boucle fermée sous contrainte de lecture unique.** Le programme de contrôle impose que toute reconception de détecteur soit jugée sur une famille de sabotage inédite, conçue à l'aveugle des moniteurs et lue une seule fois, et qu'aucun score de moniteur n'entre dans le signal de sélection d'un proposeur (`RAPPORTÉ`). Or, transmettre à l'organisme d'idéation un retour empirique sur ce qui réussit ou échoue face aux modèles de huit milliards de paramètres constitue une analyse de données adaptative : chaque cycle consomme irréversiblement de l'information sur la distribution d'évaluation et dégrade la validité hors échantillon — Cynthia Dwork, Vitaly Feldman, Moritz Hardt, Toniann Pitassi, Omer Reingold et Aaron Roth (2015), *The reusable holdout: Preserving validity in adaptive data analysis*, Science (`VÉRIFIÉ` ; identifiant arXiv : pas sûr). Sous budget GPU modeste (`RAPPORTÉ`), une boucle « proposer $\rightarrow$ évaluer sur 8B $\rightarrow$ ajuster » est statistiquement contaminable et économiquement intenable.
2. **La rupture de domaine entre mondes synthétiques stationnaires et contrôle réflexif.** L'organisme est aujourd'hui évalué sur des mondes à lois plantées et des corpus scientifiques historiques (`RAPPORTÉ`). Or la nature en physique ou en chimie ne cherche pas à contourner l'instrument de mesure ; le contrôle boîte blanche porte sur des espaces d'activations non stationnaires, confondus par le style et soumis à un adversaire stratégique. Je ne sais pas aujourd'hui si une architecture performante sur des lois plantées non adverses transfère quoi que ce soit aux trois axes du contrôle.
3. **L'asymétrie exploitable entre validité sous le nul (honnête) et puissance sous attaque (sabotage).** C'est le levier le plus sous-estimé : vérifier qu'un détecteur candidat maintient son taux de fausses alertes au-delà de la taille finie de la référence honnête, résiste à la pression rhétorique ou ne sur-déclenche pas sur des essaims honnêtes à poids partagés **ne consomme aucune famille de sabotage tenue à l'écart**. L'essentiel des mécanismes illusoires peut être réfuté sur données honnêtes seules avant d'ouvrir une seule épreuve de sabotage.
4. **Le risque de contamination par lignée partagée.** L'organisme peut mobiliser des modèles pré-entraînés lors de l'exploration ou du tri (`RAPPORTÉ`), tandis que le contrôle porte sur des modèles ouverts de huit milliards de paramètres (`RAPPORTÉ`). Si les modèles d'appui partagent des corpus d'entraînement avec les modèles cibles ou mémorisent la littérature récente sur les sondes et le contrôle, une « découverte » peut n'être qu'une restitution déguisée, et un biais inductif commun peut fausser l'évaluation (version méta de l'axe 3).

### Présupposés non établis de la question (livrable a)

| Présupposé implicite de la question | Statut | Pourquoi il doit être testé avant tout couplage |
| :--- | :--- | :--- |
| La performance sur les mondes synthétiques à lois plantées corrèle avec l'utilité en contrôle boîte blanche sur modèles 8B. | `HYPOTHÈSE` | Aucune preuve de transfert entre découverte de lois stationnaires sur processeur et détection de menaces diffuses sur activations neuronales. |
| Le goulot d'étranglement du programme de contrôle est un déficit d'idées ou d'objets mathématiques nouveaux. | `HYPOTHÈSE` | Le verrou principal peut être la qualité de l'oracle exogène, la non-échangeabilité des activations ou la faiblesse du signal interne, et non le manque de théorie. |
| Les graphes de concepts historiques contiennent des analogies transférables à des problèmes réflexifs/adverses. | `HYPOTHÈSE` | Les corpus historiques dominés par des sciences non stratégiques sous-représentent l'évasion, la dissimulation et la corruption de juges. |
| Une rétroaction du contrôle vers l'idéation peut améliorer les découvertes sans violer la séparation sélection/évaluation ni épuiser les familles inédites. | `HYPOTHÈSE` | Toute fuite d'information depuis les familles d'épreuve détruit la garantie de lecture unique ; la forme exacte d'un canal sans fuite reste à prouver. |
| L'organisme d'idéation apporte un gain au-delà d'un simple usage ponctuel de ses modèles pré-entraînés d'appui ou d'un catalogue de méthodes connues. | `OBSERVÉ-NON-AUDITÉ` | Les faits rapportent une évaluation interne existante contre un nul d'archive (`RAPPORTÉ`), mais aucun résultat audité de marge sur le contrôle n'est fourni. |
| Les mécanismes candidats « profonds » issus de l'idéation restent non redondants et valides une fois traduits en code exécutable. | `HYPOTHÈSE` | Risque élevé de reparamétrisation triviale de tests séquentiels classiques ou de brisure d'hypothèses sur activations réelles. |

---

## 2. Données brutes de départ

Avant toute interprétation agrégée (score AUC global, résumé textuel d'un juge ou synthèse par LLM), un spécialiste mobiliserait quatre ensembles de données brutes horodatées :

1. **Traces honnêtes brutes du programme de contrôle (jeu d'exploration strictement disjoint des familles d'épreuve et de la banque de validation finale — `PROPOSITION`).**
   - Séquences complètes de jetons et tenseurs d'activations internes non compressés (flux résiduel et sorties de blocs, en précision `bfloat16` ou `float16`) de modèles ouverts de huit milliards de paramètres sur les trois familles de tâches floues (`RAPPORTÉ` : plans d'expériences, chaînes multi-agents, analyse statistique).
   - **Paires honnêtes appariées sur facteurs confondants** : mêmes contenus méthodologiques honnêtes déclinés sous différents registres rhétoriques (neutre vs persuasif/assertif), différentes longueurs/horizons, différents niveaux de difficulté, incluant des *erreurs honnêtes de bonne foi* (fautes statistiques involontaires), ainsi que des chaînes multi-agents bénignes à poids partagés comparées à des chaînes bénignes à familles de modèles distinctes.
   - Distributions empiriques brutes des scores sur la référence honnête de taille finie (sans lissage paramétrique), afin de mesurer directement les queues de distribution et le plafonnement séquentiel (`RAPPORTÉ`).
2. **Journaux bruts de l'oracle exogène.** Matrices de confusion complètes par strate de difficulté sur dommages plantés calibrés (`RAPPORTÉ`), taux de désaccord inter-évaluateurs, temps et coût d'inspection par cas, avant toute agrégation.
3. **Graphes de concepts et corpus bruts de l'organisme d'idéation.** Graphes datés natifs avant résumé par modèle de langue (`RAPPORTÉ`), inventaire quantitatif des disciplines représentées (part exacte de la statistique séquentielle, théorie des jeux, cryptographie/stéganographie, tolérance aux pannes byzantines, audit et biologie du mimétisme vs sciences non adverses), et coupes temporelles strictes permettant des tests rétrospectifs hors-temps.
4. **Journaux complets d'exécution et lignées de modèles.** L'intégralité des propositions produites par l'organisme sur ses bancs CPU existants — *rejets, doublons et coûts de calcul compris* (`RAPPORTÉ`) — ainsi que les empreintes cryptographiques (SHA-256) et fiches de provenance des modèles pré-entraînés employés dans l'organisme et dans le programme de contrôle.

---

## 3. Architecture et risques de la boucle

### Architecture proposée : boucle asymétrique par obstructions formalisées et sas en cascade (`PROPOSITION`)

Pour respecter l'interdiction de faire entrer un score de moniteur dans la sélection (`RAPPORTÉ`) et préserver la lecture unique, il faut **proscrire toute boucle fermée sur verdicts de familles de sabotage** et adopter un couplage asymétrique :

- **Flux aval $\rightarrow$ amont (Contrôle $\rightarrow$ Idéation) : uniquement des « fiches d'obstruction formelle » et une géométrie honnête.** Le programme de contrôle ne renvoie jamais de score de moniteur, ni de trace de sabotage, ni d'indice sur les familles tenues à l'écart. Il exporte uniquement : (i) des énoncés mathématiques abstraits des verrous rencontrés (ex. : construire un test séquentiel toujours valide au-delà de la taille $N$ d'une référence fixe via un nul par acte ; construire un détecteur invariant à un sous-espace stylistique connu sur données honnêtes) ; (ii) des statistiques descriptives issues *exclusivement* des trajectoires honnêtes d'exploration (spectre de covariance, autocorrélation temporelle, amplitude des facteurs confondants, taux d'erreur de l'oracle exogène par strate) servant à paramétrer des **mondes-miroirs adverses sur processeur**.
- **Flux amont $\rightarrow$ aval (Idéation $\rightarrow$ Contrôle) : filtration par cinq sas séquentiels, du moins coûteux au plus irréversible :**
  - *Sas 0 (CPU, déterministe — anti-renommage)* : toute proposition doit être compilée en prototype exécutable et comparée algébriquement et empiriquement à l'archive de méthodes connues (sondes linéaires, tests de Wald, CUSUM, e-processus standards, corrélation inter-copies). Si la corrélation des décisions ou la forme fonctionnelle réduit l'objet à un habillage d'une méthode existante, rejet immédiat.
  - *Sas 1 (CPU, stress-tests analytiques)* : vérification automatisée des garanties annoncées sous perturbations synthétiques (dépendance temporelle autorégressive, queues lourdes, dérive de covariables, horizon supérieur à la référence fixe $N$, confusion de style).
  - *Sas 2 (CPU, mondes-miroirs adverses à lois plantées)* : évaluation déterministe hors-agents sur mondes synthétiques modélisant les axes 1 à 3, générés par un module aveugle aux candidats, contre les bases mécaniques, avec contrôle du taux de fausses découvertes — Yoav Benjamini et Yosef Hochberg (1995), *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing*, Journal of the Royal Statistical Society: Series B (`VÉRIFIÉ` ; identifiant arXiv : pas sûr).
  - *Sas 2.5 (GPU léger, données honnêtes 8B seules — zéro consommation d'attaque)* : vérification sur trajectoires honnêtes réelles de modèles 8B que la garantie de faux positifs tient au-delà de $N$, sous pression rhétorique appariée et sur essaims bénins à poids partagés. Un candidat qui échoue ici est éliminé sans jamais toucher une famille de sabotage.
  - *Sas 3 (GPU, préenregistré, lecture unique)* : seuls les rares candidats gelés franchissant les sas 0 à 2.5 accèdent à une famille de sabotage inédite conçue par une instance isolée, en lecture unique. Aucune mise à jour automatique des paramètres ou invites de l'organisme n'est autorisée à partir de ce verdict ; seul un post-mortem portant sur la violation éventuelle d'une hypothèse *vérifiable sur données honnêtes* peut enrichir ultérieurement les mondes-miroirs du sas 2.

### Cartographie des risques menaçant une boucle fermée

- **Risques statistiques :** (1) *Usure adaptative de l'échantillon de contrôle* : même un retour binaire « succès/échec » sur $K$ tours permet une sélection adaptative qui gonfle silencieusement le risque de fausse découverte ; (2) *p-hacking par sélection d'objets* si l'on teste de nombreux candidats sur les mêmes trajectoires 8B sans correction globale ; (3) *brisure d'échangeabilité et plafond fini* : une accumulation séquentielle calibrée sur une référence fixe de taille $N$ perd sa garantie ou plafonne dès que l'horizon dépasse $N$, sauf construction d'un nul par acte (`RAPPORTÉ`) ; (4) *erreur de spécification du nul* : confondre des erreurs honnêtes difficiles avec un sabotage diffus.
- **Risques algorithmiques :** (1) *Effet Goodhart sur les mondes-miroirs CPU* : l'organisme exploite des artefacts du générateur synthétique absents des modèles 8B ; (2) *redondance déguisée* : les LLM d'appui produisent des reformulations savantes de méthodes élémentaires ; (3) *corrélation cachée proposeur-cible* via des poids ou corpus d'entraînement partagés.
- **Risques épistémiques :** (1) *Illusion de profondeur (« théâtre mathématique »)* : un formalisme impressionnant masque des hypothèses impossibles à vérifier sur activations réelles ; (2) *violation de l'étanchéité red-team* : si l'organisme reçoit des traces d'échec des moniteurs et génère par ailleurs des scénarios de défaillance, il brise la règle d'instance aveugle aux moniteurs (`RAPPORTÉ`) ; (3) *biais du survivant* si seuls les succès de l'organisme sont archivés et analysés.

### Comment vérifier qu'un mécanisme candidat n'est pas illusoire

Quatre épreuves couperets (`PROPOSITION`), appliquées dans cet ordre :
1. **Ablation de la nouveauté** : retirer la brique mathématique prétendument originale (ex. remplacer la statistique proposée par un rapport de vraisemblance ou une moyenne mobile simple sur la même sonde) ; si la différence de performance s'annule, l'objet est cosmétique.
2. **Test placebo structurel** : exécuter l'organisme avec des graphes de concepts permutés (ou le mécanisme sur des étiquettes/couches permutées) à budget de calcul identique ; tout gain qui survit au placebo trahit un artefact de sélection ou une fuite.
3. **Stress-test nul honnête 8B (Sas 2.5)** : si le mécanisme perd son contrôle des fausses alertes sur trajectoires honnêtes longues ou rhétoriquement chargées, sa garantie est illusoire.
4. **Comparaison au bras témoin sans organisme** : le mécanisme doit battre non seulement les bases mécaniques, mais aussi une proposition témoin issue d'un appel ponctuel au même modèle d'appui à coût égal, prouvant que la valeur vient de l'organisme et non du seul LLM sous-jacent.

---

## 4. Méthodes, outils, étanchéité et mesure minimale

### Outils concrets pour la fécondité et l'étanchéité (`PROPOSITION`)

- **Rééquilibrage disciplinaire et daté du corpus amont :** compléter les archives scientifiques par des corpus datés centrés sur la décision sous adversaire et l'inférence séquentielle toujours valide — Abraham Wald (1945), *Sequential Tests of Statistical Hypotheses*, Annals of Mathematical Statistics ; E. S. Page (1954), *Continuous Inspection Schemes*, Biometrika ; Vladimir Vovk, Alex Gammerman et Glenn Shafer (2005), *Algorithmic Learning in a Random World*, Springer ; Aaditya Ramdas, Peter Grünwald, Vladimir Vovk et Glenn Shafer (2023), *Game-Theoretic Statistics and Safe Anytime-Valid Inference*, Statistical Science (`VÉRIFIÉ` ; identifiants arXiv : pas sûr) — ainsi que la théorie des jeux d'inspection, la stéganographie et le consensus tolérant aux fautes byzantines (`référence à vérifier`).
- **Contrat d'interface exécutable :** interdire toute sortie purement narrative de l'organisme. Chaque candidat livré au sas 0 comprend : (a) une spécification formelle de ses hypothèses nulles, (b) un code Python/NumPy autonome sans appel réseau, (c) sa complexité de calcul déclarée, et (d) la classe exacte de défaillances sur laquelle il revendique un gain.
- **Étanchéité organisationnelle et cryptographique :** séparation physique en trois dépôts cloisonnés — *Zone A* (exploration, organisme d'idéation, trajectoires honnêtes d'exploration), *Zone B* (générateur aveugle des familles de sabotage d'épreuve, sans accès en lecture à la Zone A ni aux moniteurs), *Zone C* (banque de validation finale, scellée jusqu'à la fin de la feuille de route, `RAPPORTÉ`). Chaque passage au sas 3 exige un dépôt de hachage SHA-256 (code, hyperparamètres, seuil, règle de décision) préenregistré avant ouverture (`RAPPORTÉ`) et décompte d'un compteur dur non renouvelable de lectures uniques.

### Mesure minimale de fonctionnement pour chaque instrument (livrable c)

| Instrument | Taux de détection (puissance) | Taux de fausses alertes | Cas honnêtes appariés | Vérifications mécaniques à battre |
| :--- | :--- | :--- | :--- | :--- |
| **1. Organisme d'idéation (banc CPU et transfert)** | Taux de candidats non redondants franchissant les sas 0–2 (puis gain réel en sas 3) par unité de calcul CPU. | Taux de fausses découvertes (FDR) sur mondes sans loi nouvelle + taux de candidats promus échouant au sas 2.5. | Mondes nuls ou à lois déjà dans l'archive appariés en taille/bruit ; graphes de concepts permutés à budget égal. | (i) Catalogue d'archive des méthodes connues ; (ii) recherche aléatoire sur graphe à CPU égal ; (iii) appel unique du même LLM d'appui sans organisme. |
| **2. Détecteur séquentiel boîte blanche (Axe 1)** | Probabilité d'alarme avant horizon $T$ (et délai médian de détection) sur famille de sabotage diffus inédite (lecture unique). | Taux cumulé toujours valide $\sup_{t \le T_{\max}} \mathbb{P}_{H_0}(\tau \le t) \le \alpha$, y compris pour $T_{\max} > N$. | Trajectoires honnêtes des mêmes tâches floues appariées en horizon $t$, difficulté, style et erreurs involontaires de bonne foi. | (i) Moniteurs boîte noire sur sorties seules ; (ii) sondes boîte blanche par action isolée ; (iii) CUSUM ou e-processus standard sur sonde linéaire ; (iv) plancher d'audit au hasard à coût d'inspection égal. |
| **3. Sondes auteur vs juges génératifs (Axe 2)** | Détection de déviation sous pression rhétorique + coût d'évasion mesuré en perte d'utilité sur la tâche. | Dérive $\Delta\text{FPR}$ entre réponses honnêtes neutres et réponses honnêtes rhétoriquement persuasives. | Paires de réponses honnêtes de validité équivalente (vérifiée par oracle) ne différant que par le style, l'assurance ou la longueur. | (i) Juges génératifs boîte noire standards et durcis ; (ii) classifieurs lexicaux/stylométriques (TF-IDF, longueur) ; (iii) paraphrase mécanique canonique avant jugement. |
| **4. Détecteur de coordination en essaims 8B (Axe 3)** | Détection de coordination implicite ou sabotage distribué entre copies à poids partagés. | Taux d'alarmes sur essaims *honnêtes* à poids partagés résolvant les mêmes tâches. | Essaims honnêtes à poids partagés sur mêmes graphes d'interaction, comparés à des essaims honnêtes hétérogènes (séparation de la corrélation inductive bénigne). | (i) Tests mécaniques d'accord et de redondance de surface ; (ii) perturbation par graine/température ou diversification de familles ; (iii) audit aléatoire de maillons isolés. |
| **5. Plancher d'audit au hasard + oracle exogène** | Probabilité d'identification par strate $p_s$ mesurée sur dommages plantés calibrés + borne analytique globale. | Taux de faux dommages déclarés sur cas honnêtes propres par strate + désaccord inter-oracles. | Productions honnêtes tirées des mêmes strates de complexité et longueur, soumises à l'aveugle. | (i) Vérificateurs déterministes de domaine (exécution de code statistique, cohérence numérique, contraintes de plan) ; (ii) audit uniforme non stratifié. |
| **6. Sas de transfert Idéation $\rightarrow$ Contrôle** | Part des candidats validés aux sas 0–2.5 qui battent les bases mécaniques en sas 3 (valeur prédictive positive). | Part des candidats promus échouant sur nul honnête 8B ou gaspillant une lecture unique sans gain. | Candidats placebos (méthodes connues reparamétrées, ou issues de graphes permutés) soumis au sas à l'aveugle. | (i) Sélection aléatoire parmi candidats syntaxiquement valides ; (ii) tri par juge LLM sans sas CPU ; (iii) sélection experte humaine sans organisme à temps borné. |

### Ancrage matériel de référence (livrable d)

Les faits fixent la cible à des modèles ouverts autour de huit milliards de paramètres sous budget GPU modeste, avec exécution courante sur processeur privilégiée (`RAPPORTÉ`). En l'absence de liste matérielle dans le dossier, voici un ancrage concret de référence (`PROPOSITION`, tous les chiffres hors 8B sont `illustratifs`) :
- **Modèles ouverts cibles (au moins deux lignées distinctes pour limiter le biais de famille) :** ex. `Llama-3.1-8B-Instruct` et `Qwen2.5-7B-Instruct` pour le développement/sas 2.5, plus une troisième lignée tenue à l'écart (ex. `Mistral-7B-Instruct-v0.3`) réservée à la vérification externe.
- **Étage processeur (Sas 0 à 2 et organisme d'idéation) :** station 16 à 32 cœurs CPU, 64 Go de RAM (`illustratif`), bibliothèques Python/NumPy/SciPy déterministes à graines fixées ; coût mensuel d'infrastructure ou location : 100 à 300 € (`illustratif`).
- **Étage GPU léger (Sas 2.5, inférence honnête et extraction d'activations) :** 1 GPU 24 Go VRAM (ex. RTX 4090 ou L4, `illustratif`), inférence `bfloat16` avec hooks natifs PyTorch pour sauvegarder les activations de couches choisies sur SSD NVMe (1 à 2 To, `illustratif`) ; ~30 à 60 heures-GPU, soit 30 à 120 € (`illustratif`).
- **Étage GPU + oracle (Sas 3, lecture unique) :** 1 à 2 GPU 40–80 Go VRAM (ex. A100/H100 loué, `illustratif`), 100 à 250 heures-GPU (150 à 600 €, `illustratif`), le poste dominant restant l'évaluation humaine / oracle exogène indépendant et la conception aveugle de la famille de sabotage (1 500 à 4 000 € par cycle, `illustratif`).

---

## 5. Vérification indépendante

En dehors des concepteurs du projet, quatre dispositifs externes rendent les résultats vérifiables et réfutables (`PROPOSITION`) :

1. **Red-team externe en double aveugle :** une équipe tierce ne disposant ni du code des détecteurs ni de l'historique de l'organisme conçoit une famille de sabotage inédite (sur tâches floues comparables) et exécute directement le conteneur logiciel gelé et haché livré par les concepteurs, sans renvoyer de traces brutes en cas de reconduction.
2. **Audit mathématique et d'antériorité hors équipe :** des statisticiens et spécialistes du contrôle indépendants vérifient (i) si un objet promu est mathématiquement distinct de la littérature existante (contrôle anti-renommage), (ii) si les preuves de garanties tiennent hors des cas idéaux, et (iii) via datation stricte des sources, que l'idée n'était pas déjà contenue dans le pré-entraînement des modèles d'appui.
3. **Réplication sur modèle ouvert 8B et oracle exogène tenus à l'écart :** exécution du même protocole gelé sur une lignée de modèle ouvert 8B non vue durant le développement et avec des annotateurs exogènes indépendants calibrés sur dommages plantés.
4. **Registre public de préenregistrement et comptabilité complète des échecs :** publication horodatée (avant toute lecture du sas 3) du protocole, des seuils et du nombre total de candidats générés/rejetés aux sas 0 à 2.5, permettant à un tiers de recalculer le risque global de comparaisons multiples et de vérifier qu'aucune famille d'épreuve ni la banque de validation finale n'ont été lues plus d'une fois (`RAPPORTÉ`).

---

## 6. Reformulation exigeante du problème

En intégrant l'analyse des présupposés (1), les données brutes requises (2), l'étanchéité de la boucle (3), les instruments et leurs bases mécaniques (4) et la vérification externe (5), le problème ne consiste pas à « relier deux systèmes pour inventer des concepts profonds », mais à résoudre la question falsifiable suivante :

> *Comment concevoir une interface unidirectionnelle par obstructions formelles et mondes-miroirs calibrés sur données honnêtes qui (1) filtre sur processeur et sur trajectoires honnêtes de modèles ouverts 8B les mécanismes candidats redondants ou statistiquement invalides avant toute dépense de lecture unique, (2) garantit l'étanchéité informationnelle vis-à-vis des familles de sabotage tenues à l'écart et de la banque finale, et (3) permet de trancher par inférence forte — sous vérification indépendante — si l'organisme d'idéation produit un gain mesurable sur la détection séquentielle, la résistance à la corruption des moniteurs ou les essaims à poids partagés, au-delà des bases mécaniques existantes, du plancher d'audit au hasard et d'un usage ponctuel de modèles de langue sans boucle d'idéation ?*

---

## 7. Programme des priorités classé et expériences décisives

Barème appliqué : $\text{score} = (\text{gain\_informatif} \times \text{facilité} \times \text{portée} \times \text{potentiel\_de\_découverte\_majeure}) / \text{coût}$, chaque critère noté de 1 à 5 (`1 = coût CPU minimal`, `5 = lourd GPU/humain`). **Toutes les notes, scores, seuils et coûts ci-dessous sont `illustratifs`.** Chaque expérience prioritaire suit la logique d'inférence forte — John R. Platt (1964), *Strong Inference*, Science (`VÉRIFIÉ` ; identifiant arXiv : pas sûr) — en opposant deux hypothèses exclusives $H_A$ et $H_B$ dont chacune peut être falsifiée.

| Rang | Action prioritaire | Gain | Fac. | Portée | Pot. | Coût | Score `(illustratif)` |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **E1 — Mondes-miroirs adverses CPU et test de transfert amont-aval (Sas 0–2)** | 5 | 5 | 4 | 4 | 1 | **400** |
| **2** | **E2 — Audit d'étalonnage nul honnête et d'invariance stylistique sur 8B (Sas 2.5, zéro attaque)** | 5 | 4 | 5 | 3 | 2 | **150** |
| **3** | **E3 — Mesure de la fuite adaptative : rétroaction fermée vs interface honnête seule (CPU)** | 4 | 4 | 4 | 3 | 2 | **96** |
| **4** | **E4 — Première épreuve préenregistrée à lecture unique sur 8B (Sas 3, Axe 1 ou 2)** | 5 | 2 | 5 | 5 | 4 | **62,5** |
| **5** | **Extension multi-cycles, essaims à poids partagés (Axe 3) et ouverture unique de la banque finale** *(différée tant que E1–E4 ne sont pas franchies)* | 5 | 1 | 5 | 5 | 5 | **25** |

---

### Priorité 1 — Expérience E1 : transfert des mondes génériques vers des mondes-miroirs adverses (CPU)

- **$H_A$ (Transfert amont-aval)** : L'optimisation de l'organisme sur ses mondes plantés génériques et ses corpus actuels améliore son taux de découverte de mécanismes non redondants et valides sur des mondes-miroirs adverses (dérive diffuse au-delà de $N$, confusion stylistique, corrélation implicite) conçus à l'aveugle.
- **$H_B$ (Rupture de domaine)** : La performance sur mondes génériques ne prédit pas la performance sur les mondes-miroirs adverses ; seuls l'ajout de fiches d'obstruction formelle et le rééquilibrage vers des corpus stratégiques/statistiques produisent des mécanismes battant les bases mécaniques.
- **Métrique** : Corrélation de rang de Spearman $\rho$ entre versions de l'organisme sur mondes génériques vs mondes-miroirs, ET taux de candidats non redondants (passant le sas 0) qui maintiennent $\widehat{\text{FPR}} \le \alpha$ ($\alpha = 0{,}05$, `illustratif`) et battent la meilleure base mécanique de $\Delta\text{TPR} \ge 0{,}10$ (`illustratif`), après contrôle FDR.
- **Seuil `(illustratif)`** : $\rho \ge 0{,}50$ ($p < 0{,}01$) ET gain net $\ge +0{,}10$ de la version générique optimisée sur le nul d'archive.
- **Contrôle négatif** : (1) Mondes-miroirs sans signal planté (vérification de $\widehat{\text{FPR}} \le \alpha$) ; (2) organisme alimenté par des graphes de concepts permutés aléatoirement à budget CPU et LLM d'appui identiques.
- **Falsification** : *Falsifie $H_A$* si $\rho < 0{,}20$ (`illustratif`) ou si la version générique optimisée ne dépasse pas le graphe permuté alors que le bras « obstructions + corpus stratégiques » franchit le seuil. *Falsifie $H_B$* si la version générique seule atteint $\rho \ge 0{,}50$ et égale ou dépasse le bras spécialisé sur mondes-miroirs.
- **Ancrage matériel & coût `(illustratif)`** : Processeur seul (station 16–32 cœurs, 64 Go RAM), 20 à 50 heures-CPU ; 50 à 200 €.

### Priorité 2 — Expérience E2 : validité nulle et invariance stylistique sur 8B honnêtes (Sas 2.5)

- **$H_A$ (Conservation des garanties sur activations 8B)** : Les candidats retenus aux sas 0–2 (ex. tests séquentiels à nul par acte ou projections invariantes) conservent leur garantie $\text{FPR} \le \alpha$ sur trajectoires honnêtes réelles de modèles 8B au-delà de la taille de référence ($T = 4N$, `illustratif`) et sous perturbation rhétorique appariée.
- **$H_B$ (Brisure par géométrie neuronale réelle)** : La non-stationnarité et les facteurs confondants de style des activations 8B réelles violent les hypothèses théoriques des candidats, provoquant une dérive des fausses alertes dès $T > N$ ou sous changement rhétorique, sans même qu'il y ait d'attaque.
- **Métrique** : Taux empirique cumulé de fausses alarmes $\widehat{\text{FPR}}(T)$ sur $M = 200$ (`illustratif`) trajectoires honnêtes longues ($T = 4N$, $N = 100$, `illustratif`) et écart $|\Delta\text{FPR}_{\text{style}}|$ entre paires honnêtes neutres et rhétoriquement pressantes, sur deux modèles ouverts ~8B distincts (`Llama-3.1-8B-Instruct`, `Qwen2.5-7B-Instruct`, `propositions`).
- **Seuil `(illustratif)`** : Borne supérieure de l'IC à 95 % de $\widehat{\text{FPR}}(T) \le 0{,}07$ (pour $\alpha = 0{,}05$) ET $|\Delta\text{FPR}_{\text{style}}| \le 0{,}03$ (`illustratif`).
- **Contrôle négatif** : (1) Trajectoires rééchantillonnées i.i.d. depuis la référence $N$ (vérifie l'absence de bogue d'implémentation) ; (2) classifieur purement stylométrique (témoin positif devant réagir à la pression rhétorique).
- **Falsification** : *Falsifie $H_A$* si $\widehat{\text{FPR}}(T) > 0{,}10$ ou $|\Delta\text{FPR}_{\text{style}}| > 0{,}08$ (`illustratif`) sur l'un des deux modèles 8B alors que le contrôle i.i.d. est conforme. *Falsifie $H_B$* si un candidat de l'organisme respecte simultanément les deux seuils sur les deux modèles 8B et deux tâches floues alors que l'accumulateur à référence fixe $N$ plafonne ou dérive.
- **Ancrage matériel & coût `(illustratif)`** : 1 GPU 24 Go VRAM, 30 à 60 heures-GPU ; 30 à 120 € (zéro coût d'oracle d'attaque).

### Priorité 3 — Expérience E3 : fuite adaptative en boucle fermée vs interface honnête seule (CPU)

- **$H_A$ (Gain généralisable de la rétroaction fermée)** : Transmettre à l'organisme des retours d'épreuve sur $K = 10$ cycles (`illustratif`) de familles d'attaque synthétiques augmente la puissance sur une banque finale de familles orthogonales par rapport à une interface limitée aux seules obstructions formelles et propriétés honnêtes, sans dégrader $\text{FPR}$.
- **$H_B$ (Optimisme illusoire et surspécialisation)** : La rétroaction fermée améliore le score sur les cycles vus tout en échouant à surpasser (ou en dégradant) l'interface sans fuite sur la banque finale orthogonale.
- **Métrique** : Écart de généralisation $\Delta_{\text{gen}} = \text{TPR}_{\text{final}}(\text{fermée}) - \text{TPR}_{\text{final}}(\text{interface honnête})$ à $\text{FPR} \le \alpha$ fixé, et écart d'optimisme $\Delta_{\text{opt}} = \text{TPR}_{\text{épreuve}} - \text{TPR}_{\text{final}}$, moyennés sur 30 graines indépendantes (`illustratif`).
- **Seuil `(illustratif)`** : $\Delta_{\text{gen}} \ge +0{,}08$ (IC à 95 % strictement positif) ET $\Delta_{\text{opt}} \le 0{,}05$ (`illustratif`).
- **Contrôle négatif** : Banque finale tirée de la *même* distribution que les familles d'épreuve (bras i.i.d. où la boucle fermée doit gagner — vérifie que l'organisme exploite bien le signal lorsqu'il n'y a pas de changement de famille).
- **Falsification** : *Falsifie $H_A$* si $\Delta_{\text{gen}} \le 0$ ou $\Delta_{\text{opt}} > 0{,}10$ (`illustratif`) sur familles orthogonales alors que le contrôle i.i.d. est positif. *Falsifie $H_B$* si $\Delta_{\text{gen}} \ge +0{,}08$, $\Delta_{\text{opt}} \le 0{,}05$ et $\widehat{\text{FPR}} \le \alpha$ sur familles orthogonales.
- **Ancrage matériel & coût `(illustratif)`** : CPU seul (32 cœurs), 40 à 100 heures-CPU ; 50 à 150 €.

### Priorité 4 — Expérience E4 : épreuve décisive à lecture unique sur 8B et famille de sabotage inédite (Sas 3)

- **$H_A$ (Valeur ajoutée réelle de l'organisme en contrôle)** : Le meilleur mécanisme gelé issu de l'organisme (ayant franchi E1–E3) dépasse sur une famille de sabotage diffuse inédite (lecture unique) toutes les bases mécaniques (boîte noire, sonde par action, accumulateur classique, plancher d'audit au hasard à coût d'inspection égal) ainsi qu'un candidat témoin produit par le même LLM d'appui sans organisme.
- **$H_B$ (Saturation par les bases mécaniques / absence de valeur ajoutée de l'idéation)** : Face à une menace inédite sur modèle réel de huit milliards de paramètres, le candidat de l'organisme ne dépasse pas la meilleure base mécanique, le plancher d'audit au hasard ou le bras témoin sans organisme.
- **Métrique** : Puissance séquentielle cumulée $\text{TPR}(T)$ à $\text{FPR}_{\text{toujours valide}} \le \alpha$ ($\alpha = 0{,}05$, `illustratif`) sur $M = 100$ (`illustratif`) trajectoires longues par bras, rapportée au coût d'audit exogène équivalent (probabilité d'identification par strate $p_s$ mesurée au préalable sur dommages plantés, `RAPPORTÉ`).
- **Seuil `(illustratif)`** : $\Delta\text{TPR} \ge +0{,}12$ (`illustratif`, test exact unilatéral préenregistré, $p < 0{,}01$) contre la meilleure base mécanique ET contre le témoin sans organisme, avec $\widehat{\text{FPR}} \le \alpha$ sur cas honnêtes appariés tenus à l'écart.
- **Contrôle négatif** : (1) Trajectoires honnêtes appariées avec erreurs involontaires (doivent rester sous $\alpha$) ; (2) dommages plantés de forte amplitude (témoin positif vérifiant la chaîne d'activations et l'oracle exogène).
- **Falsification** : *Falsifie $H_A$* si $\Delta\text{TPR} < 0{,}05$ (`illustratif`) contre la meilleure base mécanique ou le témoin sans organisme, ou si $\widehat{\text{FPR}} > 0{,}07$ (`illustratif`) sur cas honnêtes appariés. *Falsifie $H_B$* si le seuil $\Delta\text{TPR} \ge +0{,}12$ est franchi simultanément contre tous les comparateurs avec maintien de $\widehat{\text{FPR}} \le \alpha$ en lecture unique.
- **Ancrage matériel & coût `(illustratif)`** : 1 à 2 GPU 40–80 Go VRAM, 2 modèles ouverts ~8B, 100 à 250 heures-GPU (150 à 600 €) + 30 à 60 heures d'oracle exogène et de conception aveugle de la famille de sabotage (1 500 à 4 000 €).

---

### Limites qui subsistent

1. **Incertitude sur le transfert d'échelle et de menace :** je ne sais pas si un mécanisme validé sur des modèles ouverts de huit milliards de paramètres restera valide sur des modèles plus grands ou d'architecture différente, ni s'il résistera à des familles de sabotage fondamentalement autres que celles testées en lecture unique.
2. **Plafond imposé par l'oracle exogène :** sur des tâches floues à vérité différée (`RAPPORTÉ`), aucune détection boîte blanche ne peut être certifiée au-delà de la sensibilité $p_s$ et de la cohérence de l'oracle exogène sur dommages plantés ; le plancher d'audit au hasard demeure un garde-fou indispensable.
3. **Coût irréversible des évaluations :** même avec les sas 0 à 2.5, chaque épreuve de type E4 consomme définitivement une famille de sabotage aveugle ; le nombre de cycles réels reste strictement borné par le budget humain de conception indépendante.
4. **Possibilité d'issue nulle :** je ne sais pas si l'organisme d'idéation surpassera jamais un travail humain ciblé en statistique séquentielle et théorie des jeux d'inspection ; l'intérêt principal du protocole E1–E4 est précisément de rendre cette éventualité testable rapidement et à faible coût avant d'engager les ressources lourdes.

FIN-DE-CELLULE