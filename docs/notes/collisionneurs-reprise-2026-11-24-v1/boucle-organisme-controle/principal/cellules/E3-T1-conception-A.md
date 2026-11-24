# Proposition A : Tour III.1, conception ciblée à l'aveugle

**Remarques préalables (une ligne chacune).**
- Le bloc FAITS n'attribue aucun statut. Je lui applique par défaut le statut **RAPPORTÉ**. Tout ce qui vient de moi est **HYPOTHÈSE** ou proposition, et tout chiffre qui ne vient pas des faits est marqué « illustratif ».
- Je n'ai pas vérifié les empreintes sha256.
- Je ne vois aucune proposition B ou C. Je n'en critique donc aucune.
- Correspondance avec le livrable du tour : (a) se trouve en §1.2, (b) en §3.6 et §7, (c) en §4.3, (d) en §7.3. Pour la forme, la question de l'arbitre prime.
- Conformément à la règle d'intégrité 3, qui prime sur la demande de l'arbitre, je ne donne aucun identifiant arXiv de mémoire : « pas sûr » partout.

---

## 1. Ce qu'un expert du domaine ferait ici, et que la demande d'origine omet

### 1.1 Gestes d'expert absents de la demande (propositions)

1. **Changer de monnaie.** La ressource rare de la boucle n'est ni le calcul ni le nombre d'idées. C'est le nombre de **lectures uniques** de familles de sabotage inédites. La règle de lecture unique est RAPPORTÉ, et une famille inédite coûte cher à concevoir. Un expert compterait le rendement en découvertes validées par lecture consommée, pas par heure de calcul. Le §3.4 montre que, la contrainte de lectures étant saturée, augmenter la production d'idées ne sert à rien : seule la précision du tri en amont compte.
2. **Repérer la contradiction avec la règle de séparation.** Les faits (RAPPORTÉ) interdisent qu'un score de moniteur ou de juge du programme de contrôle entre dans la sélection « d'un agent ou d'un proposeur ». Or l'organisme est un proposeur. La voie de retour « orienter l'organisme à partir des observations du contrôle » est donc, lue strictement, en partie interdite. La demande ne le dit pas. Un expert ferait trancher cette question avant toute ingénierie (voir §3.2).
3. **Traiter la boucle comme une surface d'attaque statistique.** Un proposeur optimisé contre les jeux d'évaluation d'un programme de contrôle est un analyste de données adaptatif. Le risque est connu : sur-ajustement adaptatif et Goodhart. Il est décrit par Dwork, Feldman, Hardt, Pitassi, Reingold et Roth (2015), « The reusable holdout: Preserving validity in adaptive data analysis », *Science* (arXiv : pas sûr), et par Blum et Hardt (2015), « The Ladder: A Reliable Leaderboard for Machine Learning Competitions », ICML.
4. **Séparer validité et puissance.** Pour les objets séquentiels de l'axe 1, l'expert restreindrait la recherche de l'organisme à des classes **valides par construction** : des processus-e, dont l'erreur de première espèce est garantie quel que soit l'objet trouvé. La recherche ne peut alors agir que sur la puissance. Une idée ingénieuse ne peut plus casser la garantie de faux positifs.
5. **Exiger un nul fort.** Il faut battre trois bases : des recombinaisons aléatoires de méthodes déjà connues, une prédiction de liens triviale sur le graphe daté, et le carnet de problèmes de l'équipe de contrôle rédigé avant l'exécution.
6. **Fixer une politique sur le double usage.** L'organisme doit produire des « scénarios de défaillance » sous forme de structures statistiques abstraites (décalages de distribution sur des scores de sonde), jamais de procédures opérationnelles. Tout scénario plus concret relève d'un bras d'attaque déclaré, une exception prévue par les faits.
7. **Commencer par la feuille de route.** L'organisme est en pause dans l'attente d'une feuille de route validée (RAPPORTÉ). Le premier livrable est donc la feuille de route, avec des critères d'arrêt ou de poursuite, et pas une modification de l'organisme.

### 1.2 (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut |
|---|---|---|
| P1 | L'organisme peut produire des « découvertes profondes » ou des « objets mathématiques nouveaux ». | HYPOTHÈSE. Les faits ne rapportent qu'une évaluation sur lois plantées, sans aucun résultat. |
| P2 | Un gain sur les mondes à lois plantées se transfère en utilité pour le contrôle. | HYPOTHÈSE |
| P3 | Une boucle « rigoureuse » est compatible avec la lecture unique et la séparation sélection/évaluation. | HYPOTHÈSE. Les contraintes elles-mêmes sont RAPPORTÉ. |
| P4 | Les données du programme de contrôle portent une information utile pour orienter l'organisme. | HYPOTHÈSE |
| P5 | La « profondeur » est mesurable autrement que par un jugement humain. | HYPOTHÈSE. Je ne sais pas la mesurer directement (§7.4). |
| P6 | Les modèles pré-entraînés mobilisés par l'organisme sont exempts de fuite temporelle vis-à-vis des graphes datés. | HYPOTHÈSE, et même risque probable non mesuré. |
| P7 | Des protocoles sont « directement exploitables » malgré l'écart entre exécution sur processeur et exécution sur 8B. | HYPOTHÈSE. L'écart des deux régimes est RAPPORTÉ. |
| P8 | Les deux systèmes fonctionnent aujourd'hui séparément. | RAPPORTÉ |

---

## 2. Les données brutes de départ

Ces données sont à collecter avant toute synthèse. Je ne sais pas lesquelles existent déjà.

1. **Le dénominateur complet de l'organisme.** Il s'agit de toutes ses sorties sur les mondes plantés, et pas seulement des meilleures : graines, horodatage, coût, et verdict de l'orchestrateur. Sans dénominateur, aucun taux de fausses découvertes n'est calculable.
2. **Les dates de coupure.** Il faut celle de chaque instantané du graphe de concepts et celle des données d'entraînement de chaque modèle pré-entraîné utilisé. Le croisement des deux est la condition minimale d'un test temporel (voir P6).
3. **Le carnet de besoins du contrôle**, rédigé et haché avant toute sortie de l'organisme. C'est le seul canal de retour certainement licite.
4. **Les traces brutes d'activations honnêtes** sur les modèles d'environ 8B, avec la **taille m de la référence honnête**. Le plafonnement de l'accumulation au-delà de m est RAPPORTÉ. Tout objet séquentiel proposé doit être confronté à m.
5. **Les mesures brutes, par strate, de l'oracle d'audit sur dommages plantés** : probabilité d'identification par strate (exigence RAPPORTÉ). Je ne sais pas si elles existent déjà.
6. **L'historique des idées déjà essayées par le contrôle**, avec leur sort sur les familles de développement uniquement. Les résultats sur familles d'épreuve et sur la banque finale restent hors de portée de l'organisme.
7. **Les jugements bruts**, notes individuelles et non moyennées, de tout juge humain ou génératif ayant trié des idées.

---

## 3. Formalisation mathématique et conditions de validité de la boucle fermée

*Tout ce paragraphe est ma proposition (HYPOTHÈSE de modélisation). Seules les contraintes citées comme RAPPORTÉ viennent des faits.*

### 3.1 Objets

- **Organisme.** $O_\theta$ associe à un contexte $c=(G_t, \mathcal N, \mathcal A)$ une loi sur des propositions $p$. Ici $G_t$ est le graphe daté coupé à la date $t$, $\mathcal N$ les besoins hachés et $\mathcal A$ l'archive.
- **Traduction.** $T(p)\in\{\bot\}\cup\Pi$ transforme une proposition en protocole exécutable $\pi$, ou la rejette ($\bot$).
- **Partition des données du contrôle.**
  - $D_{\text{dev}}$ : familles de développement, réutilisables.
  - $D_{\text{ep}}^{(1..R)}$ : familles d'épreuve inédites, lues une fois chacune (RAPPORTÉ).
  - $D_{\text{val}}$ : banque finale, lue une fois en fin de boucle (RAPPORTÉ).
- **Utilité d'un protocole.** $U(\pi)=\Delta\beta(\pi)$, le gain de puissance de détection à niveau $\alpha$ fixé par rapport à la meilleure base existante, évalué sur une famille non vue.

### 3.2 Les deux directions et la non-circularité

Soit $\mathcal H_k$ la filtration de l'organisme après $k$ cycles. Je propose quatre conditions.

- **(NC1)** $D_{\text{val}}$ est indépendant de $\mathcal H_K$. La banque finale n'entre jamais dans le canal de retour.
- **(NC2)** Chaque $D_{\text{ep}}^{(j)}$ est conçue par une instance aveugle aux moniteurs (RAPPORTÉ). J'ajoute qu'elle doit aussi être aveugle aux propositions de l'organisme (proposition). Procédure de **dépôt-révélation** :
  1. publier $h_j=\text{sha256}(D_{\text{ep}}^{(j)})$ ;
  2. figer et hacher le lot de propositions $k$ ;
  3. lire la famille ;
  4. vérifier les empreintes.
- **(NC3)** Le retour $y_k=g(\pi_k, D_{\text{ep}}^{(j)})$ prend ses valeurs dans un ensemble fini $\mathcal Y$ préenregistré, par exemple {échec, neutre, succès}.
- **(NC4) Règle de séparation.** Deux lectures sont possibles.
  - Lecture stricte : $y_k$ dérive des scores de moniteurs. Il est donc interdit dans la sélection de l'organisme, et le retour se réduit à $\mathcal N$ et aux taxonomies de défaillance sur $D_{\text{dev}}$.
  - Lecture souple : $y_k$ est un verdict sur un **protocole**, pas un score sur un agent. Il est alors licite par un canal à capacité bornée.

  Je ne sais pas laquelle l'arbitre retient. Toute la suite est valable sous la lecture souple, et seule la voie aller subsiste sous la lecture stricte.

### 3.3 Capacité du canal de retour

Sous (NC3), l'information transmise vérifie $I(\mathcal H_K; D_{\text{ep}}^{(1..R)}) \le \sum_j \log_2|\mathcal Y_j|$. Avec trois issues et $R$ familles, cela fait au plus $R\log_2 3$ bits.

Les bornes de type « longueur de description » de la littérature sur l'analyse adaptative font croître l'erreur de généralisation avec ce nombre de bits rapporté à la taille d'échantillon. Je ne reproduis pas leurs constantes de mémoire (référence à vérifier, voir Dwork et al. 2015).

Conséquence fine : chaque famille étant lue une seule fois, le risque n'est pas le sur-ajustement à une famille. Le risque est que l'organisme apprenne la **distribution du concepteur**, c'est-à-dire ses tics de style, plutôt que la menace. Parade proposée : plusieurs concepteurs en rotation, et une banque $D_{\text{val}}$ issue d'un concepteur qui n'a pas servi à fabriquer les familles d'épreuve. On mesure ainsi la généralisation à la menace et non au concepteur.

### 3.4 Arbitrage entre coût des épreuves et rendement

L'entonnoir comporte cinq étages :
- s0 : génération ;
- s1 : vérifications mécaniques (nouveauté contre l'archive, validité de première espèce par construction) ;
- s2 : substitut sur processeur ;
- s3 : développement sur 8B avec $D_{\text{dev}}$ ;
- s4 : lecture d'épreuve.

On note $N_{s+1}=q_sN_s$, et $\rho=P(\text{succès}\mid\text{atteint } s4)$ la précision du tri en amont. Le coût total s'écrit $C=\sum_s c_sN_s+\lambda N_4$, où $\lambda$ est le **prix fantôme** d'une famille inédite.

- **Règle d'envoi en s4.** On envoie $p$ si $\hat P(\text{succès}\mid p)\,V > c_4+\lambda$, avec $\hat P$ calibrée sur des cycles antérieurs.
- **Résultat structurel.** Il est élémentaire, et c'est ma dérivation. Si les lectures sont bornées par $R$ et que $N_3\ge R$, alors le nombre de découvertes validées est au plus $R\cdot\rho$. Augmenter $N_0$, donc la créativité brute, à précision de tri fixée n'augmente pas le rendement. **L'amélioration prioritaire de l'organisme est la calibration de son tri**, pas sa production.
- **Mesure.** La valeur d'un étage $s$ se juge à la corrélation de rang entre son score et l'issue en aval. Si elle est indiscernable de zéro, l'étage ne coûte rien d'utile et doit être supprimé.

### 3.5 Validité hors des environnements synthétiques

- **(T1) Transfert mesuré, jamais supposé.** On mesure le $\tau$ de Kendall entre le classement des détecteurs candidats sur le substitut et leur classement sur activations réelles en $D_{\text{dev}}$ (expérience E4).
- **(T2) Horizon contre référence.** Pour une accumulation $M_n=\prod_{i\le n} e_i$ avec $\mathbb E_{H_0}[e_i\mid\mathcal F_{i-1}]\le 1$, l'inégalité de Ville donne $P_{H_0}(\exists n: M_n\ge 1/\alpha)\le\alpha$ (Ville 1939, *Étude critique de la notion de collectif* ; voir Ramdas, Grünwald, Vovk et Shafer, « Game-theoretic statistics and safe anytime-valid inference », *Statistical Science*, 2023).
  - Le plafonnement au-delà de la taille $m$ de la référence honnête est RAPPORTÉ.
  - Mécanisme plausible (HYPOTHÈSE) : les p-valeurs étalonnées sur le même échantillon de référence sont dépendantes à travers lui, et la preuve accumulable est bornée par l'information contenue dans $m$.
  - Condition : tout objet proposé déclare soit $n\le m$, soit un nul par acte.
- **(T3) Plancher d'audit.** Tout protocole d'audit proposé rapporte la probabilité d'identification par strate de l'oracle exogène sur dommages plantés (exigence RAPPORTÉ).
- **(T4) Au moins deux familles de modèles ouverts.** Un résultat obtenu sur un seul modèle reste OBSERVÉ-NON-AUDITÉ quant à sa portée.

### 3.6 Contrôles négatifs qui disqualifient une boucle défaillante ou illusoire

1. **Retour placebo.** Les $y_k$ sont permutés entre propositions, avec la même loi marginale. Si l'« amélioration » persiste, la boucle n'apprend rien du contrôle (E1).
2. **Organisme nul.** Recombinaison aléatoire de méthodes de l'archive, à coût égal.
3. **Canaris.** Des structures marqueurs sont insérées dans $D_{\text{ep}}$ et $D_{\text{val}}$. Leur apparition dans les sorties de l'organisme signe une fuite.
4. **Besoin factice.** Un besoin sans solution connue est inséré dans $\mathcal N$. Si l'étage s2 « valide » des solutions, le tri n'est pas informatif.
5. **Graphe à dates permutées.** Toute prédiction « réussie » sur ce graphe révèle une fuite temporelle.
6. **Redécouverte.** Une déduplication mécanique contre l'archive est faite avant de compter quoi que ce soit comme nouveau.

---

## 4. Méthodes, outils et protocoles d'évaluation

### 4.1 Familles d'approches

| Famille | Principe | Hypothèse portante | Limites et mode d'échec | Vérification mécanique à battre |
|---|---|---|---|---|
| **F1. Découverte par la littérature, prédiction de liens sur graphe daté** | Les liens manquants entre concepts annoncent des découvertes. Exemples : Swanson (1986), « Fish oil, Raynaud's syndrome, and undiscovered public knowledge » ; Tshitoyan et al. (2019), « Unsupervised word embeddings capture latent knowledge from materials science literature », *Nature* ; Krenn & Zeilinger (2020), « Predicting research trends with semantic and neural networks… », *PNAS*. | Le futur est une recombinaison du présent. | Biais de popularité, propositions incrémentales, fuite via les plongements pré-entraînés. | Voisins communs ou attachement préférentiel sur $G_t$. |
| **F2. Recherche de programmes avec évaluateur exécutable** | Un modèle de langage propose du code, un évaluateur mécanique le note. Exemple : Romera-Paredes et al. (2023), « Mathematical discoveries from program search with large language models », *Nature*. | L'évaluateur encode bien l'objectif. | Goodhart sur l'évaluateur, sur-ajustement au substitut. **Atout propre :** restreinte à une classe valide par construction (produits de facteurs-e conditionnellement de moyenne ≤ 1), la recherche ne touche que la puissance. | Bases séquentielles connues : max par action corrigé de Bonferroni, statistique cumulative de type CUSUM, processus-e par mélange. |
| **F3. Génération puis tri par juges génératifs** | Génération en masse, puis classement par un modèle. Exemple : Lu, Lu, Lange, Foerster, Clune & Ha (2024), « The AI Scientist… ». | Le juge est fiable et invariant au style. | Le juge est corruptible par la rhétorique, ce qui est précisément l'axe 2 du contrôle. Biais de verbosité et de position documentés : Zheng et al. (2023), « Judging LLM-as-a-judge with MT-Bench and Chatbot Arena ». Une étude humaine sur la nouveauté des idées : Si, Yang & Hashimoto (2024), « Can LLMs Generate Novel Research Ideas? ». | Taux d'inversion de rang sous perturbation stylistique, comparé au plancher de bruit (E3). |
| **F4. Plan d'expériences bayésien** | Choisir le protocole qui maximise le gain d'information attendu. | Le modèle d'issues est bien spécifié. | Une mauvaise spécification rend le gain attendu trompeur, et le coût de modélisation est élevé. | Choix aléatoire uniforme parmi les protocoles admissibles. |
| **F5. Co-évolution attaque/défense** | L'organisme génère scénarios et détecteurs en alternance. | Les scénarios générés couvrent les menaces réelles. | Circularité : le détecteur apprend les tics du générateur. Risque de double usage. Admissible seulement comme bras d'attaque déclaré, avec des scénarios abstraits. | Familles conçues par une instance aveugle (RAPPORTÉ). |

**Lecture critique (proposition).**
- F2 est la seule famille où la garantie de faux positifs du contrôle peut être **héritée** de la construction et non testée a posteriori. C'est la cible naturelle pour les « objets mathématiques nouveaux » de l'axe 1 : statistiques séquentielles et contournements du plafond lié à $m$.
- F3 est la plus économique mais la plus fragile. Elle offre en outre une **expérience naturelle** pour l'axe 2, puisque les juges internes de l'organisme sont étudiables sans toucher aux juges du contrôle.
- F1 sert surtout à **étalonner** l'organisme par rétrodiction (E5), pas à produire des protocoles.

### 4.2 Protocoles contre les fuites

- **Temporelle.** Le modèle pré-entraîné doit avoir une coupure antérieure à $t$, la date de coupure du graphe. À défaut, il faut mesurer la fuite. Deux moyens :
  - des tests de complétion sur des énoncés postérieurs à $t$, dans l'esprit de Golchin & Surdeanu (2023), « Time Travel in LLMs: Tracing Data Contamination in Large Language Models » (attribution à vérifier) ;
  - une comparaison entre deux modèles aux coupures différentes (E5).
- **Statistique.**
  - Aucun résumé de $D_{\text{ep}}$ ni de $D_{\text{val}}$ dans les invites.
  - Dépôt-révélation (NC2).
  - Canal à $|\mathcal Y|$ fixé (NC3).
  - Correction des comparaisons multiples sous dépendance arbitraire par e-BH : Wang & Ramdas (2022), « False discovery rate control with e-values », *JRSS-B*.
- **Par le modèle pré-entraîné utilisé comme juge.** S'il a vu les familles publiques sur lesquelles le contrôle s'étalonne, son tri est contaminé. On le vérifie par des canaris sur une copie publique leurre.

### 4.3 (c) Mesure minimale pour chaque instrument nommé dans la question

| Instrument | Taux de détection | Fausses alertes | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| **Organisme d'idéation** | Fraction des lois plantées retrouvées. En rétrodiction : liens postérieurs à $t$ retrouvés. | Propositions affirmées « nouvelles » sur des mondes **sans loi plantée**. | Monde planté et son jumeau sans loi, mêmes graines de bruit et même rendu. | Nul d'archive (RAPPORTÉ) et prédiction de liens triviale. |
| **Boucle de rétroaction** | Promotion d'une **bonne idée injectée** dans le vivier, connue de l'organisateur seul. | Promotion d'idées leurres injectées. | Même cycle, retour réel contre retour placebo. | Sélection aléatoire à budget de lectures égal. |
| **Programme de contrôle boîte blanche** (sondes) | Puissance à taux de fausses alertes fixé sur les flux saboteurs. | Taux de fausses alertes empirique sur flux honnêtes **plus longs que $m$**. | Même tâche, même consigne, trajectoire honnête contre trajectoire sabotée. | Moniteur boîte noire, sonde par action (RAPPORTÉ), sonde sur direction aléatoire. Pour la logique des tâches de contrôle d'une sonde : Hewitt & Liang (2019), « Designing and Interpreting Probes with Control Tasks », EMNLP. |
| **Étage substitut sur processeur** | $\tau$ de Kendall avec l'issue sur 8B. | Taux de passage des candidats qui échouent ensuite. | Même candidat évalué dans les deux régimes. | Prédicteur trivial (complexité du détecteur). |

---

## 5. Ce qui, hors du programme et de son équipe, permettrait de vérifier la validité

1. **Réplication indépendante.** Une équipe sans accès aux données intermédiaires reçoit le protocole préenregistré et les objets figés, et reproduit E1, E2 et E4.
2. **Concepteurs de familles externes.** Un groupe de « red team » extérieur produit $D_{\text{val}}$ et en dépose l'empreinte avant la fin de la boucle.
3. **Audit des preuves de validité.** Des statisticiens extérieurs vérifient que les objets de F2 sont effectivement des processus-e sous le nul déclaré. Un contrôle numérique sur des flux nuls longs complète la vérification.
4. **Prédictions prospectives hachées.** L'organisme publie aujourd'hui, sous empreinte, des prédictions sur des développements futurs de la littérature. Elles sont vérifiées plus tard par un tiers. C'est le seul test temporel totalement immunisé contre la fuite par pré-entraînement.
5. **Panel en aveugle.** Des experts notent des idées sans connaître leur source (organisme, humain ou nul). Ce panel est coûteux, il est donc gardé pour la fin (§7).
6. **Adoption.** Un autre groupe de contrôle utilise un protocole issu de la boucle sans aide. C'est un signal lent et non décisif.

---

## 6. Reformulation exigeante de la tâche

> Concevoir, préenregistrer et exécuter une boucle entre l'organisme $O_\theta$ et le programme de contrôle. Cette boucle maximise le nombre de protocoles qui battent, sur une banque finale $D_{\text{val}}$ conçue par un tiers aveugle et lue une seule fois, la meilleure base existante à niveau $\alpha$ fixé. Elle le fait sous un budget de $R$ lectures de familles inédites et un budget de calcul fixé, et sous quatre contraintes :
> 1. le retour de C vers O passe par un canal fini et comptabilisé en bits, conforme à la lecture de la règle de séparation retenue par l'arbitre ;
> 2. les objets séquentiels sont valides par construction ;
> 3. la boucle bat un retour placebo et un organisme nul ;
> 4. tout transfert du substitut sur processeur vers 8B est mesuré et non supposé.
>
> « Profond » n'est pas un critère d'optimisation. C'est une étiquette posée a posteriori par un panel aveugle.

---

## 7. Programme des priorités classé

### 7.1 Notation

Les notes sont mon jugement (HYPOTHÈSE). Les quatre critères du numérateur vont de 1 à 5, 5 étant le plus favorable. Le coût va de 1 (processeur seul) à 5 (lourd en calcul ou en évaluation humaine).

| Chantier | Gain | Facilité | Portée | Potentiel | Coût | Score |
|---|---|---|---|---|---|---|
| **C1** Harnais de boucle : canal fini, dépôt-révélation, placebo, canaris | 4 | 5 | 4 | 2 | 1 | **160** |
| **C2** Recherche de programmes dans une classe de processus-e valides par construction (axe 1, plafond lié à $m$) | 4 | 4 | 4 | 4 | 2 | **128** |
| **C3** Invariance au style du tri interne de l'organisme | 3 | 5 | 3 | 2 | 1 | **90** |
| **C4** Étalonnage du transfert substitut → 8B | 5 | 3 | 5 | 3 | 4 | **56,25** |
| **C5** Rétrodiction temporelle sur graphes datés | 4 | 4 | 3 | 2 | 2 | **48** |
| C6 Objets d'audit stratifiés (oracle exogène) | 3 | 3 | 4 | 2 | 3 | 24 |
| C7 Bornes de fuite des ripostes en essaim | 3 | 2 | 3 | 4 | 3 | 24 |
| C8 Panel humain aveugle sur la profondeur | 3 | 2 | 3 | 3 | 5 | 10,8 |

### 7.2 Sensibilité du classement

| Variante | Effet sur le classement |
|---|---|
| Potentiel compté au carré | C2 (512) passe devant C1 (320). C3 (180) reste devant C4 (168,75), avec un écart faible. |
| Coût compté au carré | C4 tombe à 14,1, sous C5 (24). |
| Facilité retirée | C1 et C2 sont à égalité (32). C4 (18,75) passe devant C3 (18). |

- **Conclusion robuste :** C1 et C2 restent en tête dans toutes les variantes.
- **Fragilités :** C4 est le chantier le plus sensible à la pondération du coût, et l'ordre C3 contre C4 n'est pas robuste.
- **Défaut de la formule :** elle est multiplicative. Un seul point d'écart sur un critère noté 2 déplace le score de 50 %. Le classement ne vaut donc qu'à un rang près.

### 7.3 (b) et (d) Expériences décisives des cinq premiers chantiers

Ancrage matériel commun (proposition) :
- **Modèles.** Deux familles de modèles ouverts d'environ 8B, par exemple Llama-3.1-8B et Qwen2.5-7B. Le choix est le mien : les faits ne nomment aucun modèle.
- **Mémoire.** Les poids en bf16 occupent environ 16 Go, par calcul (8×10⁹ paramètres × 2 octets). Une carte de 24 Go ou plus suffit pour l'inférence et l'extraction d'activations.
- **Tests.** Tous en e-valeurs préenregistrées, avec un seuil $1/\alpha$ et $\alpha=0{,}05$ (illustratif).

---

**E1 (C1) : la boucle apprend-elle du contrôle ?**
- **Hypothèses.**
  - $H_A$ : le gain de l'organisme dépend du **contenu** du retour.
  - $H_B$ : le gain vient de l'itération et de la sélection seules.
- **Plan.** Bras appariés par graine, retour réel contre retour permuté de même loi marginale. Les cycles sont évalués sur familles de développement et sur substitut, sans consommer de lecture d'épreuve.
- **Métrique.** Écart de taux de passage à l'étage s1+s2 sur un lot figé non vu.
- **Seuil.**
  - Pour falsifier $H_B$ : e-valeur supérieure ou égale à 20.
  - Pour falsifier $H_A$ : test d'équivalence montrant un écart inférieur à un δ préenregistré (δ illustratif).
- **Contrôles négatifs.** Canaris, organisme nul, besoin factice.
- **Réfutation.**
  - Une équivalence entre réel et placebo réfute $H_A` : la boucle est illusoire, et la voie retour est abandonnée.
  - Un réel supérieur au placebo réfute $H_B$.
- **Coût.** Processeur seul, quelques jours-processeur (illustratif).

---

**E2 (C2) : des objets séquentiels nouveaux battent-ils les bases ?**
- **Hypothèses.**
  - $H_A$ : une recherche de type F2, restreinte aux processus-e valides par construction, trouve une statistique de puissance supérieure à la meilleure base sur des familles synthétiques de sabotage diffus **tenues à l'écart de la recherche**, à $\alpha$ égal.
  - $H_B$ : le gain observé en recherche disparaît sur les familles tenues à l'écart (sur-ajustement).
- **Métrique.** Puissance à horizon fixé, et taux de fausses alertes empirique sur flux honnêtes indépendants, y compris pour des **horizons supérieurs à $m$**.
- **Seuil.** Gain de puissance d'au moins δ (illustratif), avec un taux de fausses alertes inférieur ou égal à $\alpha$, intervalle compris.
- **Contrôles négatifs.**
  - Recherche avec étiquettes permutées (sabotage indiscernable) : elle ne doit trouver aucun gain.
  - Base par acte de la référence fixe : elle doit plafonner au-delà de $m$, ce qui reproduit le fait RAPPORTÉ et valide le banc.
- **Réfutation.**
  - Absence de gain sur les familles tenues à l'écart : $H_A$ est réfuté.
  - Gain répliqué sur les deux concepteurs synthétiques : $H_B$ est réfuté.
- **Suite.** Le seul gagnant consomme une lecture d'épreuve sur 8B.
- **Coût.** Processeur pour la recherche (jours-processeur, illustratif). Une épreuve sur 8B d'environ 10 à 30 heures-GPU (illustratif).

---

**E3 (C3) : le tri interne est-il invariant au style ?**
- **Hypothèses.**
  - $H_A$ : le juge interne de l'organisme classe de manière invariante des paires au contenu identique et au style différent (assurance, jargon).
  - $H_B$ : le style déplace le rang.
- **Métrique.** Taux d'inversion de rang sur les paires stylistiques, moins le taux d'inversion sur des rééchantillonnages du même texte (plancher de bruit).
- **Seuil.** Excès supérieur à δ (illustratif), avec une e-valeur supérieure ou égale à 20.
- **Contrôle négatif.** Paires de textes strictement identiques.
- **Réfutation.**
  - Un excès significatif réfute $H_A$ : F3 est disqualifiée comme étage s2, ou remplacée.
  - Une équivalence réfute $H_B$.
- **Règle de séparation.** On n'utilise que les juges de l'organisme, jamais ceux du contrôle.
- **Coût.** Un modèle de 7 à 8B en inférence, quelques heures-GPU, ou un modèle plus petit sur processeur (illustratif).

---

**E4 (C4) : le substitut prédit-il le réel ?**
- **Hypothèses.**
  - $H_A$ : le classement d'environ K détecteurs candidats sur substitut prédit leur classement sur activations réelles de deux modèles d'environ 8B ($\tau\ge\tau_0$).
  - $H_B$ : l'intervalle de $\tau$ contient 0, ou $\tau<\tau_0$.
- **Données.** $D_{\text{dev}}$ uniquement. Aucune lecture d'épreuve.
- **Paramètres illustratifs.** $\tau_0$ et K, de l'ordre de 10 à 20.
- **Contrôles négatifs.** Substitut à caractéristiques permutées ($\tau$ attendu proche de 0) et prédicteur trivial.
- **Réfutation.**
  - Si $H_B$ tient, l'étage s2 est supprimé, et les gains de E2 ne sont pas réputés transférables.
  - Si $H_A$ tient, $H_B$ est réfuté sur ces deux modèles seulement.
- **Coût.** Extraction d'activations honnêtes et de développement, quelques dizaines d'heures-GPU (illustratif). C'est le poste le plus coûteux.

---

**E5 (C5) : l'organisme prédit-il, ou se souvient-il ?**
- **Hypothèses.**
  - $H_A$ : avec $G_t$, l'organisme propose des liens apparus dans la fenêtre $(t, t+\Delta]$ avec une précision@k supérieure au nul de prédiction de liens, à taux de fausses alertes apparié, **et** cet avantage persiste quand on remplace le modèle pré-entraîné par un modèle dont la coupure est antérieure à $t$.
  - $H_B$ : pas d'avantage, ou un avantage qui disparaît avec le modèle à coupure antérieure (mémoire et non prédiction).
- **Appariement.** Une règle mécanique, préenregistrée, relie une proposition à un lien futur.
- **Contrôle négatif.** Graphe à dates permutées.
- **Réfutation.** Chacune des deux issues falsifie l'une des hypothèses, comme ci-dessus.
- **Coût.** Processeur, avec un petit modèle pré-entraîné (illustratif).

### 7.4 Ce qui reste hors de portée

- **Mesurer la « profondeur »** sans jugement humain : je ne sais pas le faire. C8 n'en fournit qu'un indice coûteux.
- **Garantir l'absence de fuite** par des modèles pré-entraînés dont les données d'entraînement sont inconnues. On ne peut que la borner par E5 et par des canaris.
- **Transférer les résultats** au-delà des modèles d'environ 8B testés, et au-delà d'adversaires plus capables que l'organisme lui-même.
- **Obtenir plus d'un verdict final** : $D_{\text{val}}$ étant lu une seule fois (RAPPORTÉ), il n'y en aura qu'un. Une boucle qui échoue ne pourra pas être « réessayée » sur la même banque.
- **Trancher (NC4).** C'est une décision de l'arbitre, pas un résultat expérimental.

FIN-DE-CELLULE