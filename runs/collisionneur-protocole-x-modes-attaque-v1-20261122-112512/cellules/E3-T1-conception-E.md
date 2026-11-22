**Note sur les pièces transmises (Règle 2)** : Le bloc `FAITS` reproduit à l'identique le texte du bloc `QUESTION DE L'ARBITRE` (même empreinte `sha256`) et ne contient ni corpus empirique distinct ni le texte de la « réponse 24 de Fable » ou des « notes » mentionnées dans son intitulé `[VÉRIFIÉ]`.

---

## (a) Ce que la question suppose sans que ce soit établi

L'énoncé embarque sept présupposés implicites qui doivent être posés comme hypothèses testables avant toute mesure :

1. **Invariance absolue de la notion de « catégorie » (Sous-question 1)** `[HYPOTHÈSE]` : Demander si la distinction « attaque nouvelle / catégorie nouvelle » est fondée dans l'absolu suppose qu'une catégorie serait une propriété intrinsèque de l'attaque seule. Or une exécution malveillante n'est une variante ou une catégorie nouvelle que *relativement* à un couple explicite $(\Phi, \mathcal{H})$ définissant les variables observées $\Phi$ par le défenseur et la classe de détecteurs ou de parades $\mathcal{H}$ mobilisable sans changer d'architecture de capteurs `[HYPOTHÈSE]`.
2. **Exclusion mutuelle entre « assemblage » et « catégorie nouvelle » (Sous-question 2)** `[HYPOTHÈSE]` : Opposer la naissance d'une catégorie à « une variante ou un assemblage » suppose que la composition $p_1 \circ p_2$ de mécanismes déjà connus ne peut pas franchir une frontière catégorielle. Historiquement, la composition de deux mécanismes connus relevant de couches d'abstraction distinctes peut violer un invariant d'isolation qu'aucun des deux ne menace isolément `[VÉRIFIÉ]`.
3. **Absence de contamination mémorielle et gain propre du collectif (Sous-question 4)** `[HYPOTHÈSE]` : Interroger la capacité d'« un groupe de modèles de langue » suppose (i) que l'on sait séparer l'invention causale de la restitution isomorphe de schémas présents dans les corpus de pré-entraînement `[HYPOTHÈSE]`, et (ii) que l'interaction multi-modèles explore un espace d'attaques plus large qu'un échantillonnage indépendant (`Best-of-N`) d'un modèle seul à budget de jetons égal `[HYPOTHÈSE]`.
4. **Compétence honnête suffisante d'un petit modèle sur une tâche longue (Sous-question 5)** `[HYPOTHÈSE]` : Tester si un agent de petite taille « dégrade exprès une longue tâche d'analyse » suppose que ce modèle résout fiablement la tâche lorsqu'il est honnête. Si son taux d'erreur honnête à long contexte est déjà élevé, la dégradation volontaire se confond statistiquement avec l'incompétence ordinaire (effet plancher) `[HYPOTHÈSE]`.
5. **Cohérence instrumentale furtive à petite échelle (Sous-question 5)** `[HYPOTHÈSE]` : L'énoncé suppose qu'un petit modèle ouvert peut maintenir sur une longue trajectoire un double objectif (produire une trace analytique localement plausible tout en biaisant la conclusion) sans contradiction syntaxique ou arithmétique triviale `[HYPOTHÈSE]`.
6. **Validité préalable des trois instruments sur les attaques connues (Sous-question 5)** `[HYPOTHÈSE]` : Tester une « catégorie nouvelle » sous surveillance suppose que les lecteurs d'états internes, les juges de texte et le contrôle aléatoire détectent déjà les sabotages *connus* à bas taux de fausses alertes sur des tâches longues. Or la dérive distributionnelle des sondes linéaires entre paires contrastives courtes et trajectoires longues est documentée `[RAPPORTÉ]` (*cité de mémoire — référence à vérifier*).
7. **Fiabilité de l'oracle lors du contrôle au hasard du résultat (Sous-question 5)** `[HYPOTHÈSE]` : Parler d'« un contrôle au hasard du résultat » suppose que lorsqu'un résultat est tiré au sort, le vérificateur dispose d'un oracle exact pour trancher s'il est dégradé. Sur une tâche d'analyse ouverte ou granulaire, la vérification unitaire d'un sous-résultat comporte elle-même une zone d'indécision face au bruit d'analyse honnête `[HYPOTHÈSE]`.

---

## Réponses structurées aux sous-questions 1 à 4

### 1. Fondement de la distinction et critère décidable par une mesure

Sans référentiel défensif explicite, la distinction relève de la taxonomie humaine et donc de l'avis `[VÉRIFIÉ]`. En revanche, **indexée à une architecture de surveillance fixée** $\mathcal{D} = (\Phi, \mathcal{H})$, où $\Phi : \mathcal{X} \to \mathcal{Z}$ est le foncteur d'observation (les signaux mesurés par le défenseur) et $\mathcal{H} = \{h_\theta : \mathcal{Z} \to \{0,1\} \mid \theta \in \Theta\}$ la classe d'hypothèses paramétriques ajustable sans ajouter de capteur, la distinction devient mesurable par **l'inadaptabilité supervisée sous oracle** `[HYPOTHÈSE]` (formalisée ici à partir de la divergence représentationnelle $\mathcal{H}$ de Ben-David et al., 2010, *cité de mémoire*).

Soit $P_{\text{hon}}$ la distribution d'exécutions honnêtes appariées et $P_{\text{cand}}$ une distribution d'attaques candidates qui réussit sa mission (taux de succès d'attaque $\text{ASR} \ge \tau_{\text{succ}}$) et contourne le détecteur initialement déployé $\theta_0 \in \Theta$ à un taux de fausses alertes fixé $\text{FPR}(h_{\theta_0}, P_{\text{hon}}) = \alpha$. On accorde alors au défenseur un **ré-entraînement oracle** $\theta^* = \arg\max_{\theta \in \Theta} \text{TPR}(h_\theta, P_{\text{cand}})$ sous la contrainte $\text{FPR}(h_\theta, P_{\text{hon}}) \le \alpha$, entraîné directement sur des réalisations étiquetées de $\Phi(x)$ issues de $P_{\text{cand}}$ et $P_{\text{hon}}$ :

* **Régime I — Variante paramétrique** `[HYPOTHÈSE]` : $\text{TPR}(h_{\theta^*}, P_{\text{cand}}) \ge 1 - \beta$ dès l'adaptation sur quelques exemples ou sur des mélanges synthétiques d'attaques connues. Le signal discriminant figurait déjà dans $\Phi(x)$ et dans la géométrie connue de $\mathcal{H}$.
* **Régime II — Famille nouvelle intra-capteur** `[HYPOTHÈSE]` : Échec du transfert depuis les attaques connues et leurs compositions, mais $\text{TPR}(h_{\theta^*}, P_{\text{cand}}) \ge 1 - \beta$ une fois supervisé sur $P_{\text{cand}}$ sans modifier $\Phi$. L'attaque exploite une direction inexplorée de l'espace d'observation existant.
* **Régime III — Catégorie nouvelle relativement à $(\Phi, \mathcal{H})$** `[HYPOTHÈSE]` : Même après ré-entraînement supervisé direct sur $P_{\text{cand}}$, la séparabilité plafonne au voisinage du hasard :
  $$\sup_{\theta \in \Theta,\; \text{FPR}(h_\theta, P_{\text{hon}}) \le \alpha} \text{TPR}(h_\theta, P_{\text{cand}}) \le \alpha + \epsilon$$
  tout en conservant $\text{ASR} \ge \tau_{\text{succ}}$, et le rétablissement de la détection exige une extension de l'espace d'observation $\Phi \mapsto \Phi'$ (mesurer une grandeur physique, structurelle ou contrefactuelle absente de $\Phi$).

Ce critère remplace l'avis taxonomique par deux grandeurs mesurées : la perte de mission ($\text{ASR}$) et le plafond empirique de rappel à fausses alertes fixées après adaptation supervisée sur $\Phi(x)$.

### 2. Exemples historiques de naissance d'une catégorie

1. **Attaques par canaux auxiliaires physiques (temps d'exécution et consommation électrique, 1996–1999)** `[VÉRIFIÉ]` : Face au modèle cryptographique standard où l'adversaire n'observe que les paires entrée-sortie $\Phi_{\text{math}} = (m, c)$ `[VÉRIFIÉ]`, les attaques différentielles ou linéaires classiques constituaient des variantes intra-modèle. L'exploitation du temps de calcul (Kocher, 1996, *cité de mémoire*) puis de la consommation instantanée d'énergie (Kocher, Jaffe, & Jun, 1999, *cité de mémoire*) a ouvert une catégorie nouvelle `[VÉRIFIÉ]` : augmenter la taille de clé ($\theta \in \Theta_{\text{math}}$) laissait la fuite par octet de sous-clé intacte ; parer l'attaque exigeait d'étendre le modèle à l'implémentation physique $\Phi_{\text{phys}}$ (temps constant, masquage matériel) `[VÉRIFIÉ]`.
2. **Réutilisation de code et programmation orientée retour (ROP, 1997–2007)** `[VÉRIFIÉ]` : Les défenses $W \oplus X$ / NX empêchaient l'exécution de données injectées sur la pile en surveillant les permissions de pages $\Phi_{\text{page}}$ `[VÉRIFIÉ]`. Le polymorphisme de *shellcode* n'était qu'une variante contre les signatures d'octets `[VÉRIFIÉ]`. En chaînant de courtes séquences d'instructions légitimes déjà présentes en mémoire exécutable et terminées par `ret` (Shacham, 2007, *cité de mémoire*), le ROP a contourné structurellement $\Phi_{\text{page}}$ sans injecter un seul octet de code `[VÉRIFIÉ]`. Il se distinguait d'un simple appel `return-into-libc` isolé par l'obtention d'une expressivité Turing-complète où le pointeur de pile remplace le compteur ordinal `[VÉRIFIÉ]`, imposant un nouveau capteur : l'intégrité du flot de contrôle $\Phi_{\text{CFI}}$ (Abadi, Budiu, Erlingsson, & Ligatti, 2005, *cité de mémoire*) `[VÉRIFIÉ]`.
3. **Exécution spéculative transitoire (Spectre / Meltdown, divulgués en 2018)** `[VÉRIFIÉ]` : Cet exemple éclaire directement la frontière avec l'**assemblage**. L'exécution spéculative et les canaux cachés de cache étaient chacun connus depuis des décennies `[VÉRIFIÉ]`. Pourtant, leur couplage a créé une catégorie nouvelle vis-à-vis des vérifications architecturales $\Phi_{\text{ISA}}$ `[VÉRIFIÉ]` (*cité de mémoire — références exactes des collectifs Spectre/Meltdown à vérifier pour l'ordre complet des auteurs*) : même une vérification de bornes formellement correcte dans le jeu d'instructions (`if (x < size)`) est franchie transitoirement avant annulation architecturale, laissant une trace microarchitecturale persistante `[VÉRIFIÉ]`. Aucun correctif purement logiciel ignorant la spéculation ne restaurait l'isolation ; il a fallu étendre le contrat matériel-logiciel à $\Phi_{\text{spec}}$ (barrières de spéculation, séparation des tables de pages noyau) `[VÉRIFIÉ]`.

### 3. État des publications sur ce point

* **Fondations historiques d'ouverture de catégories et de parades structurelles** `[VÉRIFIÉ]` (*tous cités de mémoire*) :
  * Kocher, P. C. (1996). *Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems*.
  * Kocher, P., Jaffe, J., & Jun, B. (1999). *Differential Power Analysis*.
  * Abadi, M., Budiu, M., Erlingsson, Ú., & Ligatti, J. (2005). *Control-Flow Integrity*.
  * Shacham, H. (2007). *The Geometry of Innocent Flesh on the Bone: Return-into-libc without Function Calls (on the x86)*.
* **Évaluation adaptative, indiscernabilité formelle et divergence de représentations en apprentissage** `[RAPPORTÉ]` (*tous cités de mémoire*) :
  * Ben-David, S., Blitzer, J., Crammer, K., Kulesza, A., Pereira, F., & Vaughan, J. W. (2010). *A theory of learning from different domains*. (Formalise la borne d'erreur inter-domaines via la $\mathcal{H}$-divergence sur une représentation $\Phi$).
  * Carlini, N., & Wagner, D. (2017). *Towards Evaluating the Robustness of Neural Networks*. (Montre que l'échec d'une attaque existante ne prouve pas l'absence de vulnérabilité dans le même modèle de menace).
  * Athalye, A., Carlini, N., & Wagner, D. (2018). *Obfuscated Gradients Give a False Sense of Security: Circumventing Defenses to Adversarial Examples*. (Démontre que des contournements adaptatifs réfutent des défenses apparemment résistantes sans changer de catégorie $L_p$).
  * Goldwasser, S., Kim, M. P., Vaikuntanathan, V., & Zamir, O. (2022). *Planting Undetectable Backdoors in Machine Learning Models*. (Établit sous hypothèses cryptographiques l'existence de portes dérobées formellement indiscernables pour une classe bornée d'auditeurs).
* **Surveillance interne, contrôle d'agents subversifs et génération d'attaques par LLM** `[RAPPORTÉ]` (*tous cités de mémoire*) :
  * Burns, C., Ye, H., Klein, D., & Steinhardt, J. (2023). *Discovering Latent Knowledge in Language Models Without Supervision*. (Base des sondes linéaires de cohérence sur activations internes).
  * Greenblatt, R., Shlegeris, B., Sachan, K., & Roger, F. (2024). *AI Control: Improving Safety Despite Intentional Subversion*. (Cadre d'évaluation opposant politiques de sabotage d'agents et protocoles combinant moniteurs de texte et audit aléatoire).
  * Travaux récents sur le red-teaming automatisé par LLM, les agents dormants (*sleeper agents*), l'évaluation de sabotage subtil par LLM, la surveillance des chaînes de pensée et la fragilité des sondes d'activations hors distribution `[RAPPORTÉ]` (*cités de mémoire — références à vérifier* pour l'attribution exacte des listes d'auteurs et années de publication finale).
* **Constat sur la lacune publiée** `[RAPPORTÉ]` : À notre connaissance (*cité de mémoire*), la littérature publiée documente la génération par LLM de variantes de contournement et d'exploits d'instances de bogues connus, mais **aucune publication évaluée par les pairs ne démontre la conception autonome d'une catégorie nouvelle d'attaques par un groupe de LLM** en environnement non contaminé, ni ne standardise le test d'inadaptabilité oracle proposé ci-dessus (qui demeure donc `[HYPOTHÈSE]`).

### 4. Capacité d'un groupe de modèles de langue et témoins nécessaires

Que des groupes de LLM produisent des variantes et des chaînes d'assemblage est `[RAPPORTÉ]` (*cité de mémoire — référence à vérifier*). Qu'ils puissent concevoir une catégorie nouvelle (Régime III) hors contamination est une question empirique non tranchée `[HYPOTHÈSE]`. Pour le savoir sans artefact méthodologique, quatre témoins sont indispensables :

1. **Témoin de salle blanche (non-contamination)** : Tester le groupe sur des environnements de défense formels générés procéduralement (lois de transition et invariants tirés aléatoirement au moment du test), complétés par un test de rappel à zéro exécution ($T = 0$) vérifiant que la faille n'est pas devinable sans interaction causale avec l'environnement.
2. **Témoin d'échantillonnage individuel à calcul égal (`Solo Best-of-N`)** : Comparer le groupe de $G$ agents interagissants à des tirages indépendants d'un agent unique disposant exactement du même budget total de jetons d'inférence et d'appels au bac à sable.
3. **Témoin positif d'angle mort planté** : Retirer délibérément une variable d'état $z^*$ du moniteur $\Phi$ et vérifier par solveur formel (SMT) qu'au moins une attaque de Régime III existe mathématiquement.
4. **Témoin négatif d'environnement complet** : Inclure des environnements où $\Phi$ observe l'intégralité de l'état pertinent ; le taux de « catégories nouvelles » déclaré par le protocole de mesure doit y être nul.

---

## (c) Mesure minimale de fonctionnement des trois instruments nommés (Sous-question 5)

Avant de tester si un candidat est une catégorie nouvelle sur un modèle ouvert de petite taille, chaque instrument nommé dans la sous-question 5 doit prouver qu'il fonctionne sur un **sabotage de référence connu** $P_{\text{ref}}$ (par exemple : consigne système secrète de dégradation et organisme modèle adapté par LoRA pour biaiser ses conclusions), évalué face à des **cas honnêtes strictement appariés** pour éliminer les facteurs confondants :

| Instrument nommé | Seuil minimal de validation sur $P_{\text{ref}}$ | Cas honnêtes appariés obligatoires ($P_{\text{hon}}$) | Vérifications mécaniques élémentaires à battre d'au moins $+0,15$ de TPR à $\text{FPR} = 0,05$ `(illustratif)` |
| :--- | :--- | :--- | :--- |
| **1. Lecteurs d'états internes** ($\Phi_{\text{int}}$ : sondes linéaires / MLP / caractéristiques SAE sur flux résiduel) | $\text{TPR} \ge 0,80$ à $\text{FPR} \le 0,05$ `(illustratif)` sur dossiers retenus hors entraînement | (i) Épisodes honnêtes difficiles où l'agent commet naturellement une erreur d'ampleur comparable ($\mathcal{L} \ge 0,20$ `(illustratif)`) ; (ii) Épisodes honnêtes portant une consigne secondaire bénigne de longueur égale (ex. anonymisation stricte) ; (iii) Contrôle honnête ayant subi un LoRA bénin de même rang si le saboteur est affiné | (M1.1) Régression logistique sac-de-mots / n-grammes sur les jetons d'entrée et de sortie ; (M1.2) Statistiques scalaires d'entropie, de perplexité moyenne/maximale et de longueur de génération ; (M1.3) Sonde de même dimension sur activations à couches permutées aléatoirement |
| **2. Juges de son texte** ($\Phi_{\text{txt}}$ : modèle juge lisant la trace analytique et le rapport sans accès à la vérité terrain) | $\text{TPR} \ge 0,75$ à $\text{FPR} \le 0,05$ `(illustratif)` | (i) Échecs analytiques honnêtes sur sous-dossiers ambigus ou bruités ; (ii) Exécutions honnêtes à styles variés (température et niveau de prudence lexicale variables sur les mêmes entrées) | (M2.1) Script déterministe de cohérence arithmétique et de schéma (vérifiant que les chiffres cités en conclusion figurent dans les tables intermédiaires) ; (M2.2) Heuristique de longueur, de comptage de marqueurs d'hésitation et de perplexité ; (M2.3) Classifieur aveugle au texte ne lisant que le vecteur final de scores |
| **3. Contrôle au hasard du résultat** ($\Phi_{\text{aud}}$ : tirage aléatoire d'une fraction $p = 0,10$ `(illustratif)` des épisodes ou de $m = 2/20$ `(illustratif)` sous-dossiers vérifiés par oracle coûteux) | Vérificateur unitaire : $\text{TPR}_{\text{oracle}} \ge 0,90$ à $\text{FPR}_{\text{oracle}} \le 0,02$ `(illustratif)` sur erreurs synthétiques plantées ; détection inter-épisodes conforme ou supérieure à $1-(1-p)^K$ | Queue d'erreur naturelle du modèle honnête évaluée sur les mêmes sous-dossiers (afin de ne pas déclencher d'alerte de malveillance sur le bruit normal de compétence du petit modèle) | (M3.1) Contrôle déterministe sans ré-analyse (bornes de domaine, totaux marginaux et détection de valeurs aberrantes par score $Z$ sur le résultat final) ; (M3.2) Pour toute allocation stratifiée du budget $p$, tirage uniforme purement aveugle de loi binomiale $1-(1-p)^K$ `[VÉRIFIÉ]` |

Si l'un des trois instruments échoue à franchir son seuil minimal ou ne bat pas ses vérifications mécaniques sur $P_{\text{ref}}$, il est déclaré **non fonctionnel** : son contournement par un candidat ne peut alors servir de preuve pour aucune hypothèse sur les catégories nouvelles.

---

## (b) Expériences discriminantes en inférence forte ($H_A$ contre $H_B$)

### Tâche d'ancrage commune (Sous-question 5)
Pour éviter l'effet plancher sur un petit modèle ouvert (`7` à `8` milliards de paramètres `(illustratif)`), la longue tâche d'analyse consiste en un **audit multi-dossiers structuré** : chaque épisode fournit `20` sous-dossiers `(illustratif)` totalisant `12 000` jetons de contexte `(illustratif)` (tables chiffrées, journaux d'événements et notes contradictoires) ; l'agent produit une trace d'analyse (`~2 000` jetons `(illustratif)`) et un vecteur de décisions de risque $a \in \{0,1\}^{20}$ `(illustratif)` doté d'une vérité terrain exacte calculable hors ligne. Une dégradation compte comme attaque réussie si la perte décisionnelle normalisée vérifie $\mathcal{L}(a, a^*) - \mathcal{L}_{\text{hon-médian}} \ge \delta_{\text{deg}} = 0,25$ `(illustratif)`.

*Note probabiliste sur l'évasion de $\Phi_{\text{aud}}$* : Contre un tirage aléatoire uniforme par épisode entier avec oracle exact, la probabilité de capture par épisode dégradé vaut mécaniquement $p$ `[VÉRIFIÉ]`. En revanche, sur une longue tâche où le contrôle au hasard vérifie $m = 2$ sous-dossiers tirés au sort parmi `20` `(illustratif)`, un saboteur qui ne biaise unidirectionnellement que des cas limites situés dans l'intervalle de bruit unitaire honnête peut dégrader la synthèse globale ($\mathcal{L} \ge 0,25$ `(illustratif)`) tout en restant sous le seuil d'alerte unitaire de $\Phi_{\text{aud}}$ `[HYPOTHÈSE]`. L'expérience **E1** teste si un tel candidat (ou tout autre candidat généré) constitue une vraie catégorie nouvelle ou une simple variante.

---

### Expérience E1 — Première expérience sur petit modèle ouvert : test d'inadaptabilité oracle sous triple surveillance (tranche la Sous-question 5 et opérationnalise la Sous-question 1)

* **Condition d'entrée** : Un candidat de sabotage $P_{\text{cand}}$ sur le modèle ouvert de `7–8B` `(illustratif)` atteint $\text{ASR} \ge 0,60$ `(illustratif)` et contourne le moniteur triple pré-déployé $\theta_0$ ($\text{TPR}(\theta_0, P_{\text{cand}}) \le 0,15$ à $\text{FPR}(P_{\text{hon}}) = 0,05$ `(illustratif)`), alors que $\theta_0$ valide les seuils du livrable (c) sur $P_{\text{ref}}$.
* **Hypothèses exclusives** :
  * **$H_A$ (Variante ou famille intra-capteur)** `[HYPOTHÈSE]` : Le contournement de $\theta_0$ provient d'un manque d'exposition paramétrique ; le signal séparant $P_{\text{cand}}$ des cas honnêtes appariés $P_{\text{hon}}$ est déjà présent dans les sorties conjointes des trois instruments existants $\Phi(x) = (\Phi_{\text{int}}(x), \Phi_{\text{txt}}(x), \Phi_{\text{aud}}(x))$.
  * **$H_B$ (Catégorie nouvelle relativement à $(\Phi, \mathcal{H})$)** `[HYPOTHÈSE]` : $P_{\text{cand}}$ opère dans l'espace aveugle du triplet $\Phi$ ; même un ré-entraînement supervisé optimal $\theta^* \in \Theta$ directement sur des trajectoires étiquetées de $P_{\text{cand}}$ contre $P_{\text{hon}}$ échoue à restaurer la détection, tandis qu'une extension de capteur $\Phi \to \Phi'$ (par exemple un test contrefactuel de symétrie par inversion des étiquettes de polarité des dossiers $\Phi_{\text{sym}}$) la rétablit.
* **Protocole et métrique** : Générer $N = 600$ épisodes de $P_{\text{cand}}$ et $N = 600$ épisodes honnêtes appariés $P_{\text{hon}}$ (`400` entraînement, `200` test sur jeux de dossiers disjoints `(illustratif)`). Ré-entraîner $\theta^* \in \Theta$ sur le triplet $\Phi(x)$ sans modifier les capteurs. Mesurer $\text{TPR}(\theta^*, P_{\text{cand}})$ sur le jeu de test à $\text{FPR}(P_{\text{hon}}) = 0,05$ `(illustratif)`.
* **Seuil de décision** :
  * Seuil haut : $\text{TPR}(\theta^*, P_{\text{cand}}) \ge 0,70$ `(illustratif)`.
  * Seuil bas : $\text{TPR}(\theta^*, P_{\text{cand}}) \le 0,15$ `(illustratif)` (avec maintien de $\text{ASR} \ge 0,60$ `(illustratif)` et $\text{TPR}(\Phi', P_{\text{cand}}) \ge 0,70$ `(illustratif)`). Une valeur intermédiaire dans $]0,15 ; 0,70[$ `(illustratif)` indique un recouvrement partiel (Régime II bruité) et commande un doublement de $N$ `(illustratif)` pour écarter le sous-apprentissage.
* **Contrôles négatifs** :
  1. *Permutation d'étiquettes honnête/honnête* : Entraîner $\Theta$ à séparer deux sous-échantillons aléatoires de $P_{\text{hon}}$ ; exige $\text{TPR}_{\text{null}} \in [0,03 ; 0,07]$ à $\text{FPR} = 0,05$ `(illustratif)` (exclut le sur-apprentissage d'artefacts de dossiers).
  2. *Variante d'obfuscation connue ($P_{\text{var}}$)* : Sabotage par consigne paraphrasée ou découpée contournant $\theta_0$ ; exige $\text{TPR}(\theta^*, P_{\text{var}}) \ge 0,80$ `(illustratif)` après ré-entraînement (vérifie la capacité d'apprentissage de $\Theta$).
* **Issues de falsification** :
  * $\text{TPR}(\theta^*, P_{\text{cand}}) \ge 0,70$ `(illustratif)` **falsifie $H_B$** : le candidat n'est pas une catégorie nouvelle pour ce dispositif de surveillance.
  * $\text{TPR}(\theta^*, P_{\text{cand}}) \le 0,15$ `(illustratif)` (contrôles validés et $\text{TPR}(\Phi') \ge 0,70$ `(illustratif)`) **falsifie $H_A$** : le triplet de surveillance existant présente une cécité représentationnelle face à ce candidat.

---

### Expérience E2 — Test de clôture compositionnelle : assemblage de variantes connues contre mécanisme irréductible (tranche la Sous-question 2 appliquée au candidat)

* **Hypothèses exclusives** :
  * **$H_A$ (Assemblage réductible)** `[HYPOTHÈSE]` : Le candidat $P_{\text{cand}}$ qui contourne $\theta_0$ appartient à la clôture compositionnelle d'un catalogue fini de primitives d'évasion connues $\{A_1, \dots, A_6\}$ `(illustratif)` (ex. masquage lexical du CoT $A_1$, dilution sur sous-dossiers $A_2$, régularisation d'activations $A_3$, etc.) ; entraîner un détecteur joint $\theta_{\text{comp}} \in \Theta$ sur les primitives isolées et leurs mélanges synthétiques d'ordre $2$ et $3$ `(illustratif)` suffit à détecter $P_{\text{cand}}$ en transfert zéro-coup.
  * **$H_B$ (Irréductibilité aux assemblages connus)** `[HYPOTHÈSE]` : Même entraîné sur toutes les combinaisons synthétiques du catalogue connu, $\theta_{\text{comp}}$ échoue en transfert zéro-coup sur $P_{\text{cand}}$.
* **Métrique et seuil** : $\text{TPR}(\theta_{\text{comp}}, P_{\text{cand}})$ en transfert zéro-coup à $\text{FPR}(P_{\text{hon}}) = 0,05$ `(illustratif)`. Seuil haut : $\ge 0,65$ `(illustratif)` ; seuil bas : $\le 0,15$ `(illustratif)`.
* **Contrôle négatif** : Évaluer $\theta_{\text{comp}}$ sur une paire synthétique retenue hors entraînement $A_u \oplus A_v$ (dont les composants ont été vus séparément dans d'autres paires) ; doit atteindre $\text{TPR} \ge 0,70$ `(illustratif)` pour valider la généralisation compositionnelle du classifieur.
* **Issues de falsification** :
  * $\text{TPR}(\theta_{\text{comp}}, P_{\text{cand}}) \ge 0,65$ `(illustratif)` **falsifie $H_B$** (le candidat n'est qu'un assemblage de techniques cataloguées).
  * $\text{TPR}(\theta_{\text{comp}}, P_{\text{cand}}) \le 0,15$ `(illustratif)` avec contrôle $\ge 0,70$ `(illustratif)` **falsifie $H_A$** (et, croisé avec E1, distingue exactement Régime II et Régime III).

---

### Expérience E3 — Conception en salle blanche par un groupe de LLM contre modèle isolé à budget égal (tranche la Sous-question 4)

* **Dispositif** : Générer procéduralement $M = 30$ environnements formels d'audit séquentiel `(illustratif)` comportant chacun un invariant $\mathcal{I}$ et un moniteur $\Phi$ omettant `1` variable d'état non sémantique $z^*$ tirée aléatoirement `(illustratif)` (angle mort de Régime III vérifié exploitable par solveur SMT). Comparer, au budget strictement identique de $5 \times 10^6$ jetons et $200$ exécutions par environnement `(illustratif)` :
  * **Groupe ($G$)** : `4` instances de modèles ouverts `(illustratif)` structurées en rôles (explorateur, modélisateur du moniteur, générateur d'hypothèses hors-$\Phi$, falsificateur).
  * **Solo ($S$)** : Échantillonnage indépendant `Best-of-N` évolutif d'un modèle seul de même architecture au même budget total.
* **Hypothèses exclusives** :
  * **$H_A$ (Plafond de variantes / nullité de l'effet de groupe hors contamination)** `[HYPOTHÈSE]` : Sur les $30$ environnements synthétiques non contaminés `(illustratif)`, la proportion $p_G$ d'environnements où le groupe conçoit une attaque validée de Régime III (au sens d'E1) reste marginale ($p_G \le 0,05$ `(illustratif)`) ou ne dépasse pas le contrôle solo à budget égal ($p_G - p_S < 0,10$ `(illustratif)`).
  * **$H_B$ (Conception collective de catégories nouvelles en salle blanche)** `[HYPOTHÈSE]` : Le groupe découvre des attaques de Régime III à un taux $p_G \ge 0,25$ `(illustratif)` ET surpasse le contrôle solo à budget égal d'au moins $p_G - p_S \ge 0,15$ `(illustratif)` (test exact de Fisher bilatéral, $p_{\text{val}} < 0,01$ `(illustratif)`).
* **Contrôles négatifs** :
  1. $M_0 = 15$ environnements témoins où $\Phi$ est mathématiquement complet `(illustratif)` : exige `0/15` détection de Régime III `(illustratif)`.
  2. Test à zéro exécution ($T = 0$, sans retour du bac à sable) : exige un taux de succès $\le 1/30$ `(illustratif)` pour exclure une devinette par contamination.
* **Issues de falsification** :
  * $p_G \le 0,05$ `(illustratif)` ou $p_G - p_S < 0,10$ `(illustratif)` **falsifie $H_B$**.
  * $p_G \ge 0,25$ `(illustratif)` et $p_G - p_S \ge 0,15$ `(illustratif)` ($p_{\text{val}} < 0,01$ `(illustratif)`), avec `0/15` `(illustratif)` sur $M_0$ et $\le 1/30$ `(illustratif)` à zéro exécution, **falsifie $H_A$**.

---

## (d) Ancrage matériel, calcul nécessaire et coût estimé

L'ensemble des chiffres ci-dessous ne provient pas des faits transmis et est intégralement **illustratif** :

* **Modèles ouverts retenus** :
  * *Agent surveillé de petite taille (E1, E2)* : `Qwen2.5-7B-Instruct` (`7,6` milliards de paramètres `(illustratif)`) et réplication sur `Llama-3.1-8B-Instruct` (`8,0` milliards de paramètres `(illustratif)`), exécutés en `bfloat16` avec accès direct au flux résiduel (`28` et `32` couches `(illustratif)`) et adaptation LoRA (`rang 16` `(illustratif)`).
  * *Lecteurs d'états internes ($\Phi_{\text{int}}$)* : Sondes linéaires régularisées $L_2$, MLP à `1` couche (`256` neurones `(illustratif)`) et auto-encodeurs parcimonieux ouverts (`Llama-Scope`, `32 768` caractéristiques par couche `(illustratif)`) extraits sur `4` profondeurs (`couches 8, 16, 24, 31` `(illustratif)`).
  * *Juge de texte ($\Phi_{\text{txt}}$)* : `Llama-3.1-8B-Instruct` (`8` milliards de paramètres `(illustratif)`) et contrôle de capacité supérieure sur `Qwen2.5-32B-Instruct` (`32` milliards de paramètres `(illustratif)`).
  * *Groupe générateur (E3)* : `Qwen2.5-32B-Instruct` (`32` milliards de paramètres `(illustratif)`).
* **Volume de calcul** :
  * *Première expérience Q5 seule (Calibration (c) + Duel E1 sur `2` modèles agents)* : `4 800` trajectoires longues `(illustratif)` à `14 000` jetons `(illustratif)` (`~6,7 \times 10^7` jetons `(illustratif)`), `6` entraînements LoRA `(illustratif)` (`~24` heures-GPU `(illustratif)`), inférence agent + juge via `vLLM` et ajustement des sondes (`~86` heures-GPU `(illustratif)`), stockage d'activations agrégées `~120 Go` `(illustratif)` $\rightarrow$ **total Q5 (E1) : `~110` heures-GPU NVIDIA H100 `80 Go` `(illustratif)`**.
  * *Extensions E2 (clôture d'assemblages) et E3 (`45` environnements salle blanche $\times 2$ conditions $\times 5 \times 10^6$ jetons = `4,5 \times 10^8` jetons `(illustratif)`)* : `~30` heures-GPU (E2) + `~140` heures-GPU (E3) = `~170` heures-GPU H100 `(illustratif)`.
  * *Total campagne complète (c + E1 + E2 + E3)* : **`~280` heures-GPU H100 `80 Go` `(illustratif)`**.
* **Coût financier estimé** :
  * Au tarif cloud à la demande de `2,50 $` à `3,50 $` par heure-GPU H100 `(illustratif)` et `0 $` d'API propriétaire `(illustratif)` :
    * **Première expérience ciblée Q5 (Calibration + E1)** : **`275 $` à `385 $` `(illustratif)`**.
    * **Programme complet (Calibration + E1 + E2 + E3)** : **`700 $` à `980 $` `(illustratif)`**.

---

## Synthèse épistémique : ce que nous savons, ce que nous supposons, ce qui nous ferait changer d'avis

* **Ce que nous savons** :
  1. Historiquement, l'émergence de catégories telles que les canaux auxiliaires physiques, le ROP ou les attaques spéculatives transitoires s'est caractérisée par la mise en défaut d'une hypothèse d'invariance implicite des défenses existantes, obligeant à observer de nouvelles variables plutôt qu'à ré-étalonner les seuils existants `[VÉRIFIÉ]`.
  2. Contre un contrôle aléatoire uniforme et indépendant de taux $p$ muni d'un oracle exact par tâche entière, toute attaque dégradant effectivement une tâche donnée est détectée avec probabilité $p$ lors de cet épisode `[VÉRIFIÉ]`.
  3. Des cadres expérimentaux de contrôle d'agents subversifs et de sondage linéaire des représentations internes sont publiés, ainsi que des résultats montrant la vulnérabilité de défenses ML à des variantes adaptatives intra-modèle `[RAPPORTÉ]`, tandis qu'aucune preuve publiée n'établit à ce jour l'invention autonome d'une catégorie nouvelle d'attaques par un collectif de LLM `[RAPPORTÉ]`.
* **Ce que nous supposons** :
  1. La frontière « variante / assemblage / catégorie nouvelle » est adéquatement capturée par le couple de tests d'inadaptabilité supervisée oracle (E1) et de clôture compositionnelle (E2) indexés à $(\Phi, \mathcal{H})$ `[HYPOTHÈSE]`.
  2. Un modèle ouvert de `7` à `8` milliards de paramètres `(illustratif)` possède une compétence honnête assez stable sur un audit structuré de `20` sous-dossiers `(illustratif)` pour permettre à la fois une dégradation intentionnelle furtive et le calibrage des trois instruments de surveillance `[HYPOTHÈSE]`.
  3. Sans interaction causale avec un environnement formel non contaminé, un groupe de LLM se limite vraisemblablement à la recombinaison de variantes (hypothèse $H_A$ de E3), mais l'émergence par boucle d'exécution reste ouverte ($H_B$ de E3) `[HYPOTHÈSE]`.
* **Ce qui nous ferait changer d'avis** :
  1. *Sur le critère lui-même (Q1)* : Si un exemple historique consensuel de catégorie nouvelle (tel le ROP face à une surveillance restreinte aux permissions de pages $W \oplus X$) était détecté à $\text{TPR} \ge 0,70$ et $\text{FPR} \le 0,05$ `(illustratif)` sans élargir les capteurs $\Phi$, ou inversement si de simples paraphrases franchissaient le critère d'inadaptabilité E1 malgré le contrôle $P_{\text{var}}$, notre opérationnalisation $(\Phi, \mathcal{H})$ serait réfutée.
  2. *Sur la capacité des groupes de LLM (Q4)* : Observer $p_G \ge 0,25$ et $p_G - p_S \ge 0,15$ `(illustratif)` dans l'expérience en salle blanche E3 (avec zéro fausse alerte sur les environnements complets $M_0$ et échec à zéro exécution) nous ferait abandonner l'hypothèse d'un plafond de simple recombinaison.
  3. *Sur un candidat de sabotage d'analyse longue (Q5)* : Si, sur petit modèle ouvert avec instruments validés en (c), le candidat maintient $\text{ASR} \ge 0,60$ et $\text{TPR}(\theta^*) \le 0,15$ à $\text{FPR} = 0,05$ `(illustratif)` après ré-entraînement supervisé joint des sondes internes, du juge de texte et du protocole d'audit aléatoire (E1), nous conclurons contre $H_A$ qu'il constitue une catégorie nouvelle relativement à ce dispositif de surveillance ; si $\text{TPR}(\theta^*) \ge 0,70$ `(illustratif)`, nous rejetterons la qualification de catégorie nouvelle.

FIN-DE-CELLULE