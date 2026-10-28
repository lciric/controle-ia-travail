# Antériorité — Q3 : « Peut-on prédire ses propres angles morts avant de les rencontrer ? »

Avertissement : tout ce qui suit est RAPPORTÉ d'après des pages de résumé, des pages HTML de billets et des listes de résultats de recherche. Aucun PDF n'a été lu en entier ni vérifié. Aucune technique d'attaque n'est décrite ; les travaux côté attaque sont nommés par classe seulement.

## 1. Verdict

**SEMI-OCCUPÉ. Confiance moyenne.** L'idée générale est ancienne et bien occupée : « dériver les angles morts d'un détecteur à partir de ses hypothèses » remonte à la sécurité informatique (1998-2006), et le benchmark SLEIGHT-Bench (Anthropic et Redwood, mai 2026) la transpose aux moniteurs de modèles de langage. Mais je n'ai trouvé aucun travail qui réunisse les quatre éléments de Q3 : (a) des prédictions **par famille** tirées d'hypothèses explicites du moniteur, (b) **préenregistrées** avant le test, (c) sur des familles **tenues à l'écart** d'une défense **évoluée**, (d) **notées contre le hasard**, avec éventuellement des lemmes vérifiés en Lean. Ce sont précisément l'évaluation et la notation de la prédiction qui manquent, plus que l'idée elle-même.

## 2. Occupants et voisins (du plus proche au plus lointain)

**SLEIGHT-Bench : Finding Blind Spots in AI Monitors** (Najt, Toft, Tracy, Roger, Benton ; billet Alignment Science d'Anthropic, 19 mai 2026 ; arXiv 2605.16626 ; préimpression et billet). RAPPORTÉ (billet) : la méthode consiste à « identifier un angle mort conceptuel dans la façon dont les moniteurs raisonnent », puis à construire des transcriptions synthétiques d'agent de programmation qui l'exploitent (40 transcriptions, 11 catégories), puis à mesurer les taux de détection à 1 % de faux positifs. Les catégories sont tirées des limites de capacité connues, des défaillances observées et des lacunes des modèles de menace des moniteurs. Certaines catégories ne sont jamais détectées (0 %), d'autres le sont à 90 %. **Ce qu'il ne fait pas** (RAPPORTÉ par absence sur la page) : il ne présente pas les catégories comme des prédictions notées, ne donne aucun taux de réussite des prédictions, aucune référence au hasard, pas de préenregistrement et pas de séparation tenue à l'écart. Les invites de moniteur ciblées sont évaluées sur le jeu même qui a servi à les concevoir. Le moniteur est figé, pas évolué. INFÉRÉ : c'est l'occupant le plus proche du **mécanisme** (une théorie produit des familles), mais pas de la **mesure** que pose Q3.

**Fetterman, « Inherited Circuits, Learned Semantics » (arXiv 2606.27091, 2026, préimpression, Cisco Talos).** RAPPORTÉ (page de résumé) : sur un classifieur de maliciels affiné, une sonde linéaire combinée à un test d'ablation d'indicateurs, appliqué aux seules entrées canoniques, signale avant tout essai d'évasion **une** famille de commandes comme vulnérable, et cette prédiction se confirme. En revanche, d'autres familles qui ont échoué n'avaient pas été prédites. Les explications mécanistes sont venues après coup, les effectifs sont très petits et les résultats dépendent de l'invite. Il n'y a pas de prédiction par catégorie engagée d'avance ni de préenregistrement. INFÉRÉ : c'est la seule prédiction a priori par famille confirmée que j'aie trouvée, mais elle est anecdotique et ne vise pas la sécurité de l'intelligence artificielle.

**Zhang, « Why Formal Monitors Fail: Attack Distribution Entropy as a Coverage Bound for LTL-Based LLM Agent Safety » (arXiv 2608.01388, août 2026, préimpression).** RAPPORTÉ (page Pith) : ce travail borne le rappel d'un moniteur en logique temporelle linéaire par la couverture des motifs d'attaque les plus fréquents, une quantité liée à l'entropie de la distribution d'attaque. La relation est testée sur huit architectures (r = −0,87, n = 8). **Ce qu'il ne fait pas** : il ne prédit rien au niveau des familles, le leave-one-out porte sur les architectures et non sur les familles, il n'y a ni préenregistrement ni preuve vérifiée par machine. La revue automatique de Pith signale des erreurs de preuve et une validation en partie circulaire. À VÉRIFIER.

**Sécurité informatique : les angles morts déduits des hypothèses du détecteur (classique, relu par les pairs).**
- Ptacek et Newsham 1998, « Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection » (rapport technique Secure Networks). RAPPORTÉ (titre et pages de référence) : ils dérivent des classes d'évasion de l'**écart d'hypothèses** entre le détecteur réseau et l'hôte final, puis les testent sur des produits commerciaux. INFÉRÉ : c'est le précédent historique exact du schéma « théorie → familles → vérification », mais sans préenregistrement ni notation.
- Wagner et Soto, « Mimicry Attacks on Host-Based Intrusion Detection Systems » (ACM CCS 2002) et Wagner et Dean (IEEE S&P 2001). RAPPORTÉ (listes de références) : les classes d'évasion d'un détecteur d'anomalies d'appels système sont dérivées de son modèle. À VÉRIFIER sur PDF.
- Tan et Maxion, « Why 6? Defining the Operational Limits of stide » (IEEE S&P 2002). Je n'ai pas pu ouvrir la page dblp. À VÉRIFIER : d'après mon souvenir, il cartographie analytiquement les régions aveugles en fonction de la taille de fenêtre puis les vérifie.
- Li et Das (arXiv cs/0410068). RAPPORTÉ : des théorèmes donnent les conditions de détectabilité (taille de fenêtre comparée aux longueurs minimales de séquences étrangères) et concluent qu'il existe des intrusions indétectables. Ces conditions sont vérifiées sur les jeux de données UNM, MIT et CERT.
- Inoue et Somayaji, « What Happened to Anomaly Detection? » (rapport technique Carleton TR-07-09, 2006). RAPPORTÉ : un cadre ensembliste prédit des **classes** d'attaques structurellement indétectables, par exemple celles qui ne changent pas le graphe de flot de contrôle, mais pas les attaques individuelles. Il n'y a pas de vérification préenregistrée.

**Prédiction a priori de la défaillance hors distribution (apprentissage automatique).**
- Chou, Kirsanov, Yang, Chung, « Finding Fingerprints of OOD Failures from In-Distribution Geometry » (NeurIPS 2025) et « Diagnosing Generalization Failures from Representational Geometry Markers » (arXiv 2603.01879). RAPPORTÉ : la géométrie des représentations en distribution prédit la performance hors distribution. Mais elle prédit **si** et **combien** le modèle échoue, pas **sur quelle famille**, et rien n'est préenregistré.
- « Prospective Prediction of OOD Degradation from Source-Side Training Dynamics » (arXiv 2610.12397, 2026). RAPPORTÉ : c'est une preuve de principe sur la prédiction prospective de la dégradation. Elle porte sur le « si », pas sur le « où ».
- Dai, Mahloujifar, Mittal, « Formulating Robustness Against Unforeseen Attacks » (NeurIPS 2022). RAPPORTÉ : une borne sur l'écart de risque entre modèle de menace source et cible, fondée sur la « variation ». Les auteurs reconnaissent que les bornes sont lâches et ne prédisent pas bien la perte face aux attaques imprévues. C'est un antécédent théorique, pas une prédiction par famille.

**Théorie des limites de détection.**
- Goldwasser, Kim, Vaikuntanathan, Zamir, « Planting Undetectable Backdoors » (FOCS 2022, arXiv 2204.06974). RAPPORTÉ : ils prouvent l'indétectabilité de portes dérobées sous hypothèses cryptographiques. Cela fournit des familles indétectables **par construction**, sans test empirique de prédiction.
- Reiss, Cohen, Hoshen, « No Free Lunch: The Hazards of Over-Expressive Representations in Anomaly Detection » (arXiv 2306.07284). RAPPORTÉ : dans un modèle jouet gaussien, un détecteur de densité tend vers le hasard sur une variation d'un attribut non pertinent quand la dimension croît. La preuve est une esquisse, et les auteurs vérifient empiriquement que des attributs non catégoriels sont manqués. INFÉRÉ : c'est le meilleur exemple « théorie → famille manquée → vérification », mais sans préenregistrement ni contexte de sécurité.

**Vérification formelle de moniteurs.** VeriMon (Basin, Traytel et coauteurs ; RV 2019 et ICTAC 2022, Isabelle/HOL) et le programme « monitorability » d'Aceto et Francalanza (Université de Malte). RAPPORTÉ (titres) : ils certifient qu'un moniteur est **correct vis-à-vis d'une spécification** et caractérisent quelles propriétés sont surveillables. Ils ne prédisent pas sur quelle famille d'attaque statistique un moniteur appris échouera. INFÉRÉ : c'est un voisin lointain, utile pour l'outillage du juge garanti.

**Occupants du cadre commun vérifiés pour Q3.** Hills, Caspary, Cooper Stickland (arXiv 2607.02514), MonitoringBench et Terekhov **mesurent** des évasions ; ils ne les prédisent pas avant le test. RAPPORTÉ (résumés).

## 3. Ce qui survit

Voici la formulation la plus étroite qui reste apparemment ouverte. On produit, à partir d'hypothèses statistiques explicites d'un moniteur **évolué** (boîte blanche ou boîte noire), un classement ou une étiquette « échoue / tient » **par famille d'attaque tenue à l'écart**. Ce classement est **préenregistré**, éventuellement adossé à des lemmes vérifiés en Lean. On le **note une seule fois** contre une référence de hasard, par exemple une permutation des étiquettes ou une prédiction naïve fondée sur les taux en distribution. Et on répète l'exercice au fil des générations de la co-évolution. Ni SLEIGHT-Bench (pas de notation, pas de séparation, moniteur figé) ni Fetterman (une seule famille, a posteriori pour le reste) ni la tradition des détecteurs d'intrusion (pas de notation statistique des prédictions) ne font cela. INFÉRÉ, avec une garde : cette absence ressort de mes recherches, pas d'une preuve. Le point vraiment distinctif est la **notation de la théorie comme prévisionniste**, pas l'idée que la théorie suggère des familles.

## 4. Traitabilité

- **Sur processeur seulement** : rédiger les hypothèses du moniteur, dériver les prédictions par famille, les préenregistrer (horodatage, dépôt figé), écrire en Lean les lemmes de type « sous l'hypothèse H, une variation de type V ne change pas la statistique du moniteur ». Les moniteurs linéaires ou à seuil s'y prêtent bien.
- **Prérequis** : une taxonomie de familles tenues à l'écart fixée **avant** la dérivation et produite par un tiers ou un benchmark existant (SLEIGHT-Bench, MonitoringBench). Sans cela, le préenregistrement est vulnérable au choix a posteriori des familles.
- **Dépense** : l'évaluation finale exige de faire tourner le moniteur évolué sur les familles tenues à l'écart. C'est modeste si l'on réutilise des transcriptions existantes (quelques centaines à quelques milliers d'appels de modèle, soit quelques dizaines à centaines de dollars, ordre de grandeur INFÉRÉ). C'est plus coûteux si un moniteur par sonde exige d'extraire les activations d'un modèle ouvert (de l'ordre de quelques heures de processeur graphique, INFÉRÉ).
- **Pièges** : (1) le petit nombre de familles, une dizaine, donne une puissance statistique faible : il faut calculer d'avance quel taux de réussite bat le hasard. (2) Il y a une circularité si les familles sont définies à partir des échecs du moniteur, comme le reproche Pith à 2608.01388. (3) La dépendance à l'invite ou au seuil des résultats, observée par Fetterman. (4) Des prédictions triviales, du type « tout échoue » quand le taux de base d'échec est élevé (plusieurs catégories de SLEIGHT-Bench à 0 %) : il faut une référence par taux de base. (5) Les bornes lâches (Dai et al.), qui ne discriminent pas entre familles.

## 5. À vérifier sur PDF avant toute revendication

- SLEIGHT-Bench (2605.16626) : les catégories ont-elles été formulées avant les tests ? Des catégories hypothétiques ont-elles été écartées parce que détectées, ce qui serait un biais de survie ? Y a-t-il une section sur l'anticipation ?
- Fetterman (2606.27091) : le protocole du test de signe, et le moment exact où la prédiction a été fixée.
- Zhang (2608.01388) : la validité des preuves, et si une prédiction par famille est implicite.
- Tan et Maxion (S&P 2002) : la carte des régions aveugles est-elle dérivée analytiquement puis vérifiée ? Vérifier aussi la référence elle-même.
- Ptacek et Newsham 1998 : la structure « hypothèse → classe → test produit » (au niveau méthode seulement).
- Reiss et al. (2306.07284) : le lieu de publication, et si la famille manquée a été prédite avant l'expérience.
- Chou et al. (NeurIPS 2025) : existe-t-il une variante par famille de décalage ?
- Les citations récentes de SLEIGHT-Bench, pour un éventuel travail de « prévision des angles morts » publié entre juin et octobre 2026.

## 6. Requêtes faites (19)

1. predicting which attack family a detector will fail on before testing, theory-driven blind spot prediction
2. monitorability runtime verification which properties are monitorable assumptions undetectable violations
3. Ptacek Newsham 1998 insertion evasion intrusion detection assumptions network IDS
4. Tan Maxion "Why 6?" defining the operational limits of stide anomaly detector blind regions
5. predicting out-of-distribution failure of classifier before deployment preregistered predictions of failure modes
6. AI control monitor assumptions threat model predict which attacks evade monitor theoretical analysis 2026 arXiv
7. Tan Maxion 2002 "Why 6" stide window size blind region anomaly detector analytical prediction
8. Goldwasser Kim Vaikuntanathan Zamir planting undetectable backdoors machine learning models
9. automated detector coverage map "blind spots" anomaly detectors … "benchmarking anomaly-based detection systems"
10. no free lunch anomaly detection impossibility theorem detector must have blind spots
11. LLM monitor failure prediction "a priori" which sabotage categories monitor misses hypothesis preregistered control evaluation 2026
12. formally verified runtime monitor Lean Coq Isabelle certified monitor correctness detectability guarantees
13. theory predicts unforeseen adversarial attack family robustness transfer between threat models prediction before evaluation
14. hypothesis-driven blind spot discovery classifier predict failure slices before evaluation LLM-generated hypotheses verified
15. forecasting which jailbreak or attack categories a safeguard will fail on, predicting held-out attack success from defense properties
16. linear probe monitor theoretical blind spots predicted evasion families activation monitoring obfuscation theory 2026
17. "mimicry attacks" host-based intrusion detection Wagner Soto 2002 detector assumption analysis predicted undetectable
18. preregistered predictions machine learning robustness evaluation held-out attack categories "pre-registered" defense
19. Anthropic Redwood AI control "monitor" anticipate failure modes "assumptions" safety case monitorability argument 2026 ; plus une recherche étendue : derive LLM agent monitor blind spots from its assumptions, predict held-out sabotage strategy failures, then validate empirically
