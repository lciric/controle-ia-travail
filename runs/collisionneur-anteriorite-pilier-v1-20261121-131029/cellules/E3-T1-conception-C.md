Voici l’analyse et la conception ciblée pour la proposition C, en croisant strictement le livrable du Tour III.1 et la structure de la question de l'arbitre. Les faits issus du bloc de contexte sont marqués **[RAPPORTÉ]**, nos postulats de travail ou propositions sont marqués **[HYPOTHÈSE]**. Conformément à la consigne de la question, cette réponse n'invente aucun chiffre ni aucune référence.

---

### (a) Ce que la question suppose sans que ce soit établi

La formulation de l'arbitre et les trois options (a, b, c) reposent sur cinq présupposés non démontrés :

1. **L'équivalence d'isomorphisme de l'agent lecteur [HYPOTHÈSE]** : L'option (a) suppose qu'un agent lisant et « empreintant » des articles peut reconnaître qu'un théorème publié sous un vocabulaire A (ex. théorie de l'information, contrôle stochastique ou bandits) est mathématiquement identique ou implique trivialement une cible formulée sous un vocabulaire B (contrôle de systèmes d'IA).
2. **L'homogénéité du besoin d'antériorité entre les trois formes de cibles [HYPOTHÈSE]** : La question traite le pilier en bloc, alors que les cibles sont sous trois formes **[RAPPORTÉ]** :
   - *Objet à score exact* (ex. issu de la recherche de programmes pour des règles de décision) : une collision avec la littérature n'invalide pas l'utilité opérationnelle si le score bat l'état de l'art, et la nouveauté s'évalue contre un nombre, pas contre une preuve.
   - *Lemme de bibliothèque* : la nouveauté mathématique absolue importe peu ; seule compte l'absence du lemme dans la bibliothèque Lean publique **[RAPPORTÉ]** (qui se vérifie mécaniquement sans lire la littérature papier).
   - *Énoncé à démontrer ou réfuter* : c'est la seule forme où l'antériorité bibliographique papier détruit la valeur de la cible.
3. **La gratuité de la contamination de la mémoire de travail [HYPOTHÈSE]** : Lire massivement en amont (options a et c) suppose que l'injection d'énoncés voisins de 2026 **[RAPPORTÉ]** dans le contexte des agents ne va pas biaiser leur exploration vers de la simple traduction ou paraphrase, au détriment de constructions indépendantes.
4. **La séparabilité temporelle entre formulation et lecture [HYPOTHÈSE]** : L'option (b) suppose qu'on peut formuler et « sceller » une cible de recherche pertinente en liste fermée **[RAPPORTÉ]** sans connaître les lignes de crête exactes (les constantes et les conditions de régularité des travaux de 2026 **[RAPPORTÉ]**), au risque de sceller des énoncés faux ou triviaux.
5. **La nature du coût de collision [HYPOTHÈSE]** : Il est établi qu'une collision découverte après dépense ou après revendication coûte cher **[RAPPORTÉ]**, mais la question suppose implicitement que ces deux coûts sont de même nature. Or, le coût après dépense est un coût budgétaire interne borné (le budget alloué à la cible), tandis que le coût après revendication publique est un coût de réputation externe.

---

### 1. Ce qu'un expert ferait ici, et qu'on ne demande pas

Un expert en mathématiques appliquées et en formalisation ne choisirait aucune des trois options temporelles uniformes. Il appliquerait trois découplages qu'on ne demande pas ici **[HYPOTHÈSE]** :

* **Découplage par le type de cible (Stratification)** : Il exempterait immédiatement de toute veille bibliographique papier les *lemmes de bibliothèque* (soumis uniquement à une recherche formelle dans le dépôt Lean existant) et les *objets à score exact* (soumis uniquement à un banc d'évaluation). Il réserverait la lecture d'antériorité aux seuls *énoncés à démontrer ou réfuter*.
* **Auto-formalisation des seules « frontières » avant de sceller** : Au lieu de lire des articles entiers sur cinq zones, l'expert extrairait uniquement les *énoncés des théorèmes principaux* (sans les preuves) des travaux de 2026 croisés par hasard **[RAPPORTÉ]**, les traduirait en énoncés formels Lean (avec `sorry`), et définirait les cibles de la liste fermée formellement comme des *strictes améliorations* (ex. affaiblissement d'une hypothèse d'indépendance, réduction d'une constante) ou des *négations* de ces énoncés.
* **Test de mémorisation à coût nul (Canari de contamination)** : Avant de lancer un agent de preuve ou un agent lecteur sur une cible candidats, l'expert demanderait au modèle de langage de base de compléter l'énoncé à partir de son préfixe ou d'en deviner les auteurs. Si le modèle régurgite une preuve ou une citation précise, la cible est déjà dans le corpus de pré-entraînement (antériorité certaine sans aucune recherche externe).

---

### 2. Les données brutes de départ

Pour opérer sans laisser d'angle mort sur les cinq zones **[RAPPORTÉ]**, les données brutes nécessaires sont **[HYPOTHÈSE]** :

* **Bases d'articles et prépublications** : Les flux bruts (LaTeX source quand disponible, sinon PDF converti en texte structuré) des dépôts de prépublications en statistique, théorie de l'information, apprentissage et théorie des jeux, ainsi que les actes de conférences récentes, incluant spécifiquement le lot des travaux voisins de 2026 croisés par hasard **[RAPPORTÉ]**.
* **Bibliothèques formelles** : Le code source complet de la bibliothèque Lean de statistique publique qui couvre déjà divergences, Fano, Bretagnolle–Huber, identité de Wald et e-valeurs **[RAPPORTÉ]**, ainsi que la bibliothèque mathématique standard de Lean sur laquelle elle s'appuie (arbres syntaxiques abstraits et graphes de dépendances des théorèmes).
* **Listes de problèmes ouverts et monographies de référence** : Les sections « Open Problems » ou « Future Work » extraites des articles de synthèse récents sur les e-valeurs, les tests séquentiels et l'inspection, ainsi que les listes d'exercices des manuels avancés du domaine (souvent source de « fausses nouveautés » redémontrées par les modèles).
* **Notices de bancs (Benchmarks)** : Pour les *objets à score exact* et la recherche de programmes **[RAPPORTÉ]**, les spécifications exactes des fonctions de perte, les contraintes de budget/calcul, et les meilleures valeurs numériques connues (baselines triviales et état de l'art) sur ces règles de décision statistique.

---

### 3. Les méthodes et outils précis d'une recherche d'antériorité (et leurs modes d'échec)

Aucune méthode seule ne bloque toutes les collisions. Voici la chaîne d'outils proposée **[HYPOTHÈSE]** :

| Méthode / Outil | Ce qu'il fait exactement | Ce qu'il suppose | Comment il échoue (Mode de défaillance) |
| :--- | :--- | :--- | :--- |
| **1. Recherche par unification de types et sous-typage (sur Lean)** | Cherche dans la bibliothèque Lean **[RAPPORTÉ]** si la signature de type de la cible (ou une variante à permutation d'arguments près) existe déjà. | Que la bibliothèque formelle utilise les mêmes définitions de base (ex. même définition d'une e-valeur ou d'une divergence) que la cible. | Échoue sur l'antériorité papier non formalisée, ou si un concept identique a été formalisé avec une structure de données différente (ex. mesure vs distribution). |
| **2. « Empreintage » structurel invariant à la notation (Canonisation par agent)** | L'agent extrait chaque théorème d'un article et le réécrit dans un schéma canonique standardisé : *(Espace de probabilité, Hypothèse nulle $H_0$, Hypothèse alternative $H_1$, Structure de dépendance, Borne/Complexité)* en remplaçant les variables par des symboles fixes. | Que le modèle de langage sait parser fidèlement le LaTeX mathématique et identifier correctement les quantificateurs implicites des articles humains. | Échoue par hallucination lors de la compression, ou lorsqu'un résultat statistique est formulé dans un langage purement géométrique, algébrique ou de théorie des jeux sans mentionner $H_0/H_1$. |
| **3. Vérification d'implication logique par solveur / prouveur sur squelettes formels** | Traduit l'empreinte de la littérature ($T_{lit}$) et la cible ($T_{cible}$) en énoncés Lean (sans preuves), puis lance un tactique automatique pour tenter de prouver $T_{lit} \implies T_{cible}$ en quelques étapes. | Que la traduction formelle des deux énoncés est syntaxiquement valide et sémantiquement fidèle (alignement des définitions). | Échoue si la déduction $T_{lit} \implies T_{cible}$ est mathématiquement élémentaire pour un humain (ex. changement de variable ou application de Jensen) mais dépasse la profondeur du prouveur automatique. |
| **4. Traversée du graphe de citations amont/aval à partir des graines de 2026** | Utilise les travaux voisins de 2026 **[RAPPORTÉ]** comme nœuds de départ : récupère toute leur bibliographie (amont) et tous les papiers qui partagent les mêmes co-auteurs ou les citent (aval). | Que la communauté scientifique est connectée et cite correctement les travaux antérieurs pertinents. | Échoue face aux travaux isolés (« silos » disciplinaires : ex. un résultat d'inspection prouvé en recherche opérationnelle industrielle qui ne cite aucun papier de statistique ou d'IA). |

---

### 4. Ce qui, hors du programme, vérifierait qu'une cible est neuve

Pour valider l'absence de collision hors de l'écosystème des agents du programme **[HYPOTHÈSE]** :

1. **Les mainteneurs de la bibliothèque Lean de statistique publique** : Soumettre un *lemme de bibliothèque* ou un *énoncé* **[RAPPORTÉ]** via une requête d'intégration (Pull Request) publique. Les mainteneurs savent immédiatement si le lemme fait doublon avec une branche en cours de développement ou s'il découle trivialement d'un théorème abstrait déjà présent dans la bibliothèque mathématique générale.
2. **Le lecteur humain du domaine (prévu au programme [RAPPORTÉ]) utilisé en « aveugle inversé »** : Plutôt que de lui demander « est-ce nouveau ? » (ce qui incite à un hochement de tête superficiel), on lui soumet l'énoncé sans la preuve en lui demandant : *« Dans quel manuel ou article classique ce résultat apparaît-il comme corollaire, et comment le prouveriez-vous en dix lignes à partir des théorèmes connus ? »* S'il échoue à le réduire à un résultat connu, la nouveauté est étayée.
3. **Moteurs externes de recherche formelle et de théorèmes** : Requêter les moteurs d'indexation publics de l'écosystème Lean par signature de type et par langage naturel pour vérifier qu'aucun dépôt externe (hors de la bibliothèque statistique du programme) n'a déjà formalisé l'énoncé.
4. **Preuve d'horodatage et sollicitation ciblée d'auteurs** : Pour un *énoncé à démontrer* de haute valeur, envoyer l'énoncé seul aux auteurs des travaux voisins de 2026 **[RAPPORTÉ]** avant toute revendication publique, en leur demandant s'ils considèrent que cela découle de leurs résultats.

---

### (b) Expériences décisives en duel ($H_A$ contre $H_B$)

Conformément à la règle d'inférence forte (B4) et à l'interdiction d'inventer des chiffres, les seuils ci-dessous sont exprimés de manière algébrique en fonction des paramètres réels du programme (que le directeur connaît, mais qui ne sont pas chiffrés dans les faits : je ne sais pas quelles sont leurs valeurs numériques exactes).

#### Expérience 1 : Taux de collision a priori des cibles (Faut-il lire avant de sceller ?)
* **Protocole** : Prendre un échantillon de cibles candidates générées à veille gelée **[RAPPORTÉ]**, uniquement de la catégorie *énoncé à démontrer ou réfuter*. Débloquer la lecture d'antériorité (humain du domaine + agent lecteur avec empreintage) sur cet échantillon *avant* de lancer les agents de preuve. Soit $C_{lect}$ le coût d'effort de cette lecture par cible, et $B_{cible}$ le budget de recherche égal alloué à chaque cible **[RAPPORTÉ]**.
* **Hypothèse $H_A$ (Nécessité du filtrage amont - Option a)** : La proportion $p_{coll}$ de cibles candidates qui sont déjà résolues (ou trivialement impliquées) par la littérature existante (incluant les travaux de 2026 **[RAPPORTÉ]**) est supérieure au ratio de coût critique $\tau_1 = C_{lect} / B_{cible}$.
* **Hypothèse $H_B$ (Viabilité de la lecture tardive - Option b)** : La proportion $p_{coll}$ est inférieure ou égale à $\tau_1$ ; l'effort de lecture amont coûte plus cher que le budget gaspillé sur les rares collisions.
* **Métrique et Seuil** : Taux empirique de cibles invalidées par antériorité avant dépense de preuve ($p_{coll}$ vs $\tau_1$).
* **Contrôle négatif** : Insérer à l'aveugle dans l'échantillon des variantes obfusquées (changement de nom des variables) de théorèmes classiques déjà présents dans la bibliothèque Lean publique **[RAPPORTÉ]** (Fano, Bretagnolle–Huber, identité de Wald). Si le protocole de lecture ne détecte pas la totalité de ces contrôles négatifs, l'instrument de lecture est invalide et l'expérience est nulle.
* **Issue falsificatrice** : Si $p_{coll} > \tau_1$, $H_B$ (et donc l'option b pour les énoncés) est falsifiée. Si $p_{coll} \le \tau_1$, $H_A$ (l'obligation de tout lire avant de sceller) est falsifiée.

#### Expérience 2 : Capacité du juge/agent à détecter une équivalence non triviale (L'empreintage par agent suffit-il ?)
* **Protocole** : Construire un banc de paires d'énoncés $(E_1, E_2)$ issus des cinq zones **[RAPPORTÉ]**, où $E_2$ est une reformulation mathématiquement équivalente ou un corollaire direct de $E_1$ sous un changement de vocabulaire (ex. un jeu d'inspection sous budget reformulé en test séquentiel minimax), mêlées à des paires $(E_1, E_3)$ où $E_3$ diffère par une condition critique (ex. dépendance arbitraire au lieu d'indépendance). Soumettre ces paires à l'agent lecteur/juge de nouveauté **[RAPPORTÉ]**.
* **Hypothèse $H_A$ (Fiabilité de l'empreintage agentique)** : L'agent lecteur distingue les collisions sémantiques profondes des innovations réelles avec un taux de rappel supérieur à la recherche mécanique par mots-clés/types, sans augmenter le taux de fausses alertes au-delà de la capacité d'arbitrage du lecteur humain **[RAPPORTÉ]**.
* **Hypothèse $H_B$ (Cécité syntaxique de l'agent)** : L'agent lecteur ne détecte que les similarités de surface ; il échoue sur les isomorphismes de vocabulaire ou génère des fausses alertes dès que les mêmes mots-clés (ex. « e-valeurs », « Wald ») apparaissent.
* **Métrique et Seuil** : Exactitude équilibrée sur les paires appariées, comparée au seuil de performance d'une baseline purement lexicale (BM25 / TF-IDF sur les formules LaTeX).
* **Contrôle négatif** : Paires d'énoncés strictement identiques mot pour mot (doivent donner une détection parfaite) et paires tirées de domaines disjoints (doivent donner zéro alerte).
* **Issue falsificatrice** : Si l'agent ne bat pas significativement la baseline lexicale sur les paires isomorphes à vocabulaire modifié, $H_A$ est falsifiée (on ne peut pas déléguer la lecture amont à l'agent seul sans formalisation Lean). Dans le cas contraire, $H_B$ est falsifiée.

---

### (c) Mesure minimale de fonctionnement des instruments nommés

Quatre instruments interviennent dans les faits et la question : l'**agent lecteur (avec empreintage)**, le **juge de nouveauté** **[RAPPORTÉ]**, le **lecteur humain du domaine** **[RAPPORTÉ]**, et la **recherche formelle sur la bibliothèque Lean** **[RAPPORTÉ]**.

Pour chacun, le fonctionnement minimal exige d'évaluer simultanément le **taux de détection** (rappel sur de vraies collisions) et le **taux de fausses alertes** (déclarer connue une cible réellement neuve) sur le jeu de **cas honnêtes appariés** suivant **[HYPOTHÈSE]** :

* **Cas positifs (vraies collisions à détecter)** : Un théorème extrait d'un des travaux voisins de 2026 non lus **[RAPPORTÉ]** (ou un théorème déjà présent dans la bibliothèque Lean **[RAPPORTÉ]**), dont on a réécrit la prose dans le style du programme de contrôle d'IA et renommé toutes les variables mathématiques.
* **Cas négatifs appariés (vraies nouveautés à ne pas bloquer)** : Le même énoncé que le cas positif, mais dans lequel une hypothèse structurelle est modifiée de façon décisive selon les axes du programme **[RAPPORTÉ]** (ex. remplacer une hypothèse i.i.d. par un « nul non stationnaire », ou remplacer l'indépendance par une « fusion sous dépendance »), rendant le théorème antérieur inapplicable.

**Vérifications mécaniques (baselines) que chaque instrument doit battre pour justifier son coût :**
1. **Contre la recherche textuelle / lexicale** : Un simple calcul de recouvrement de n-grammes et d'identifiants LaTeX (type BM25) entre l'énoncé cible et le texte brut des articles. (Un instrument qui a le même taux de détection et de fausses alertes que BM25 ne comprend pas les mathématiques, il lit seulement les mots-clés).
2. **Contre la recherche syntaxique Lean (`exact?` / `apply?`)** : Pour la bibliothèque formelle, la simple requête mécanique du compilateur Lean cherchant si le type exact existe déjà. L'agent et le juge de nouveauté doivent détecter des collisions que le compilateur Lean ne voit pas immédiatement (par exemple, parce que les définitions ne sont pas alignées).
3. **Pour le lecteur humain du domaine** : Il sert d'étalon-or sur un sous-échantillon, mais sa propre mesure minimale de fonctionnement (calibration) consiste à vérifier qu'il ne déclare pas « nouveau » un théorème classique (Fano, Bretagnolle–Huber **[RAPPORTÉ]**) déguisé sous le jargon du contrôle de l'IA.

---

### (d) Ancrage matériel

*Note d'intégrité : La règle (d) du livrable général demande un coût estimé marqué « illustratif », tandis que la règle finale de la QUESTION DE L'ARBITRE ordonne strictement : « n'invente aucun chiffre ». Conformément à la règle 6 (la question de l'arbitre fixe la forme de la réponse) et au principe de non-invention, je ne donne aucun chiffre inventé ci-dessous ; les grandeurs matérielles dont la valeur exacte n'est pas dans les faits sont indiquées comme « je ne sais pas (paramètre à mesurer) ».* **[HYPOTHÈSE]**

* **Modèles ouverts et environnement formel** :
  * Exécution locale ou sur serveur dédié du vérificateur de preuves Lean 4, chargé avec la bibliothèque de statistique publique **[RAPPORTÉ]** (divergences, Fano, Bretagnolle–Huber, identité de Wald, e-valeurs).
  * Modèles de langage à poids ouverts (spécialisés en raisonnement mathématique et traduction formelle auto-formalisante LaTeX $\leftrightarrow$ Lean) pour l'empreintage et la génération de squelettes d'énoncés.
  * Parseur documentaire ouvert (conversion de PDF scientifiques en LaTeX/Markdown mathématique propre) pour ingérer les travaux voisins de 2026 **[RAPPORTÉ]**.
* **Calcul nécessaire et coût estimé** :
  * *Compilation et recherche dans la bibliothèque Lean* : Calcul sur processeur standard (CPU), coût marginal négligeable devant celui des agents de recherche.
  * *Ingestion et empreintage des articles des cinq zones* : Proportionnel au volume de jetons (tokens) du corpus d'articles collectés dans les cinq zones multiplié par le coût d'inférence du modèle ouvert choisi. Quantité exacte de jetons du corpus et coût financier en devises : **je ne sais pas** (cela dépend du nombre exact d'articles dans les cinq zones et du tarif de l'infrastructure de calcul du programme, non fournis dans les faits).

---

### 5. Reformulation de la demande

La demande initiale : *« Quand et sur quelle étendue faut-il lire l'antériorité (a: maintenant sur 5 zones ; b: à la première revendication ; c: pour tout le pilier) ? »* est mal posée car elle confond trois objets dont la vulnérabilité à l'antériorité est disjointe **[HYPOTHÈSE]**.

**Demande reformulée :**
> *« Comment répartir l'effort de vérification d'antériorité entre la vérification mécanique formelle (Lean), la lecture d'articles par agent (empreintage) et l'expertise humaine, de manière différenciée selon les trois formes de cibles en liste fermée (objet à score exact, lemme de bibliothèque, énoncé à démontrer ou réfuter) **[RAPPORTÉ]**, afin de minimiser la somme du coût de retard des pilotes et du coût d'une collision découverte après dépense ou revendication **[RAPPORTÉ]** ? »*

---

### 6. Recommandation : Option (d) — Protocole stratifié par forme de cible et lecture des seules frontières

Je rejette (a), (b) et (c) prises en bloc, et je recommande une **autre option** **[HYPOTHÈSE]** qui hybride (a) et (b) selon la forme de la cible :

1. **Pour les « lemmes de bibliothèque » [RAPPORTÉ] $\rightarrow$ Aucune lecture d'articles (ni maintenant, ni après) ; vérification mécanique immédiate.**
   * *Action* : Avant de sceller la cible, vérifier uniquement par script et recherche de type que le lemme n'est pas déjà dans la bibliothèque Lean publique **[RAPPORTÉ]** ou dans sa bibliothèque standard. S'il est dans un article papier mais absent de Lean, le formaliser reste un gain valide pour la bibliothèque.
2. **Pour les « objets à score exact » (et recherche de programmes) [RAPPORTÉ] $\rightarrow$ Option (b) allégée.**
   * *Action* : Extraire immédiatement des travaux voisins de 2026 **[RAPPORTÉ]** la seule valeur numérique du meilleur score connu (baseline à battre), sans lire ni empreinter les preuves. Lancer les pilotes tout de suite. Ne lire la littérature en détail qu'à la première revendication de nouveauté (si un programme découvert bat le score).
3. **Pour les « énoncés à démontrer ou réfuter » [RAPPORTÉ] $\rightarrow$ Option (a) ciblée sur les énoncés frontières.**
   * *Action* : Dès maintenant, avant de sceller ces cibles, débloquer la veille *uniquement* pour extraire et empreinter (sous forme de signatures formelles Lean ou de schémas canoniques) les **énoncés des théorèmes** (sans lire le corps des preuves) des travaux voisins de 2026 croisés par hasard **[RAPPORTÉ]** et de leurs références directes sur les cinq zones. Ne sceller un énoncé cible que s'il résiste au test d'implication triviale à partir de ces empreintes. Un second contrôle approfondi (par le juge de nouveauté et le lecteur humain du domaine **[RAPPORTÉ]**) n'est déclenché qu'après réussite d'une preuve, juste avant toute revendication.

#### Ce que cette recommandation coûte
* **Avant de sceller les cibles** : Un délai très court (limité à la vérification mécanique dans Lean pour les lemmes, et à l'extraction des seuls *énoncés* des travaux de 2026 **[RAPPORTÉ]** pour les théorèmes, sans lecture intégrale des démonstrations ni couverture exhaustive de toute la littérature historique).
* **En cours de programme** : Le maintien du juge de nouveauté et du lecteur humain **[RAPPORTÉ]** uniquement en aval, sur les rares cibles où les agents auront effectivement trouvé une preuve ou battu un score.

#### Ce qu'elle suppose
* Que les trois formes de cibles ont des conditions de victoire distinctes (un lemme de bibliothèque tire sa valeur de son code Lean vérifié ; un objet à score exact tire sa valeur de sa performance chiffrée ; seul l'énoncé à démontrer tire toute sa valeur de sa nouveauté théorique) **[HYPOTHÈSE]**.
* Que les travaux voisins de 2026 croisés par hasard **[RAPPORTÉ]** contiennent ou citent l'état de l'art pertinent sur les cinq zones (propriété de Markov du graphe de citations récent) **[HYPOTHÈSE]**.

#### Ce qui la ferait changer (Conditions de bascule)
* **Bascule vers l'Option (b) pure (tout retarder à la première revendication)** : Si l'Expérience 1 montre que le taux de collision a priori $p_{coll}$ sur les énoncés est inférieur au ratio coût de lecture / budget de la cible ($\tau_1$), ou si le taux de succès des agents de preuve sur les cibles est extrêmement faible (si les agents échouent presque toujours à prouver les cibles, il est mathématiquement optimal de ne vérifier l'antériorité que sur les très rares cibles qu'ils réussissent à prouver).
* **Bascule vers l'Option (a) ou (c) intégrale (lecture profonde de tout le pilier en amont)** : Si le directeur du programme exige que *même les lemmes de bibliothèque et les objets à score exact* fassent l'objet d'une publication académique revendiquant une priorité théorique absolue, ou si l'Expérience 1 révèle que la majorité des cibles candidates formulées à veille gelée sont en réalité des résultats déjà publiés dans les travaux de 2026 **[RAPPORTÉ]**.

FIN-DE-CELLULE