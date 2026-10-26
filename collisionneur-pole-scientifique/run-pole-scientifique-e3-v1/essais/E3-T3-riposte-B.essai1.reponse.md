# Proposition B, tour III.3 : riposte

## Pièces reçues

- Les attaques A et C contre B sont présentes et complètes : la balise de fin et `FIN-DE-CELLULE` sont lues dans chacune.
- Les faits C (méta-conception v6.3 et relecture) et le code v6.2.1 sont toujours absents. Je n'en utilise rien.

Je ne réponds qu'aux sections « Contre la proposition B ».

**Leçon acceptée.** A la formule, C l'illustre : ma conception prenait pour vraie une déclaration de l'agent (loi p_h, opérateur, contraintes, référence p₀) là où le noyau doit mesurer. Chaque correction ci-dessous remplace une déclaration par une mesure du noyau. Tout ce qui suit est **HYPOTHÈSE** de conception : rien n'a été exécuté.

---

## (a) Verdicts

### Attaques de A (« Contre la proposition B »)

| n° | Attaque | Verdict | Ce qui change |
|---|---|---|---|
| B-1 | p₀ est un modèle, pas la loi nulle. Ville ne vaut que si p₀ est exacte. | **Acceptée** | Le nul devient **composite** : une bibliothèque figée de prédicteurs aveugles au domaine (taux de base, marginale empirique, AR(1), dérive linéaire). Le dénominateur est le maximum de vraisemblance sur cette bibliothèque, calculé après coup, ce qui le rend conservateur. Le numérateur est prévisible. C'est le schéma de l'inférence universelle (Wasserman, Ramdas & Balakrishnan, 2020, « Universal inference », *PNAS*). Je reformule aussi : la promotion signifie « h capte une structure que la bibliothèque n'a pas », et non « h est vraie ». Si le vrai nul sort de la bibliothèque, la garantie tombe ; ce cas devient le test T1b. |
| B-2 | Le contenu d'une loi probabiliste n'est pas défini. | **Acceptée** | Il n'y a plus qu'une notion d'hypothèse : un programme qui émet p_h. Son contenu est le **risque déclaré** ρ_h = KL(p_ref ‖ p_h), c'est-à-dire la perte de richesse attendue si la référence est juste. Il est calculé par le noyau et multiplié par la couverture κ_h du domaine. |
| B-3 | E1 est vraie par construction sur les tautologies injectées. | **Acceptée** | Les injections deviennent des vérifications de mise en œuvre. La métrique porte sur les hypothèses **produites par les agents**. |
| B-4 | L'engagement date la configuration, pas l'information. | **Acceptée, transformée en test** | Chaque test noté reçoit un **tirage frais** du générateur : la table n'est plus un réservoir fini. Le réservoir d'exploration est disjoint du réservoir de notation. Test T2. |
| B-5 | Le même monde sert à régler l'aptitude et à juger le reste. | **Acceptée** | Une famille de mondes distincte par expérience. Les réglages du sélecteur sont figés par empreinte avant la génération des familles suivantes. |
| B-6 | Le générateur et les agents partagent leurs a priori. | **Acceptée, transformée en test** | Des lois tirées d'une grammaire aléatoire (un programme, aucun modèle) sont opposées à des lois écrites par un modèle d'une autre lignée. Test T5. |
| B-7 | L'adversaire peut tester hors du domaine de l'hypothèse. | **Acceptée** | Le domaine D_h est déclaré, et le noyau confine l'adversaire à D_h. La couverture κ_h entre dans le contenu comme un coût. Je reprends ici la correction que A adresse au domaine de C. Le taux de mise à mort est rapporté **loi par loi**. |
| B-8 | L'opérateur et les contraintes sont déclarés par l'agent ; la fertilité récompense la longueur et l'ajout au hasard. | **Acceptée** | L'opérateur est extrait par le noyau d'un arbre syntaxique **canonisé** (opérations neutres éliminées). Les contraintes sont calculées par le noyau. La fertilité est mesurée contre le rival « concaténation des parents ». La taille est bornée. Voir E3′. |
| B-9 | E4 : pont manquant entre les bras, budgets comptés en appels, couverture vraie par construction. | **Acceptée** | Les deux bras émettent le même objet (un programme qui produit p_h). Le budget est égalisé en jetons, réflexion comprise, et en secondes de processeur. La batterie est figée par un tiers aveugle au langage, avant que celui-ci soit écrit. La couverture est aussi mesurée sur les hypothèses produites par le bras code libre. |
| B-10 | E7 vise la mauvaise menace. | **Acceptée** (C fait la même remarque) | La ré-exécution ne sert plus qu'à détecter un rapport falsifié. Son 0 % prévu sur un bridage engagé dans le code devient un témoin. E7′ teste une implémentation indépendante. |
| B-11 | Les paires de c1 sont contradictoires. | **Acceptée** | Paires de **même multiensemble de jetons**, qui ne diffèrent que par l'ordre, la structure ou la position. Un sac de mots à l'aléatoire sur ces paires est une condition de validité (T7). Que de telles paires puissent porter l'indice reste une HYPOTHÈSE. |
| B-12 | Les jetons-témoins ne détectent que la copie. | **Acceptée** | Dans le monde planté, la part scellée est retirée à chaque évaluation : apprendre sa distribution revient à apprendre la loi, ce qui est légitime. Sur données réelles, la limite reste entière. |

**Scénarios d'évasion de A**

- **Pari couvert : acceptée en partie.** Promouvoir un pari couvert dont la composante nette est vraie n'est pas une faute, puisque l'évidence est réelle. La faute serait de le classer comme fort. Le contenu ρ_h le classe bas. Test T3.
- **Explorer d'abord** : traité par B-4.
- **Déplacer le domaine vers les zones où p₀ est mal spécifié** : traité par le nul composite et T1b. Le résidu hors bibliothèque est dit.
- **Étiqueter l'opérateur, allonger la descendance** : traité par B-8.
- **Saboter le code** : traité par B-10.
- **Paraphraser** : traité par B-12.
- **« Tous à la fois » : acceptée en partie.** Le programme *est* désormais l'hypothèse, et le récit n'est pas noté. Il reste un point non résolu : rien ne vérifie que le récit décrit le programme. Ce point est dit, il n'est pas réglé.

**Contrôles négatifs de A** : les sept sont adoptés, sous les noms T1 à T7.

### Attaques de C (« Contre la proposition B »)

| n° | Attaque | Verdict | Ce qui change |
|---|---|---|---|
| C-B1 | Le pari ne s'applique pas aux inégalités ; une loi déterministe est ruinée à la première valeur aberrante ; les agents vont lisser. | **Acceptée en partie, transformée en test** | *Inégalités* : une hypothèse peut être composite. On parie contre son complément avec une marge δ, et l'élimination a lieu quand l'e-processus contre « FPR ≤ α » atteint 1/α. *Ruine* : rejetée sur le principe. Une loi qui donne une probabilité nulle à une issue observée est réfutée par cette issue, et c'est voulu : l'hypothèse doit prédire les observations, bruit compris. *Lissage* : la pression est réelle. Test T8. |
| C-B2 | Le « rival » n'est pas défini. | **Acceptée** | Le rival est soit une hypothèse nommée avant les tirages, soit le **mélange prévisible** de la population, dont les poids ne sont mis à jour que sur le passé. Pour tout q_t prévisible, Π q_t/p_h est une martingale sous h, donc Ville tient. Limite dite : une hypothèse fausse n'est éliminée que si un rival fait mieux qu'elle. Comme diagnostic, et dans le monde planté seulement, je rapporte la part des lois fausses qui survivent faute de meilleur rival. |
| C-B3 | Asymétrie de puissance dans le contrôle de E2. | **Acceptée** | L'égalité entre bras est exigée sur la **fausse promotion** (erreur de type I contre le nul composite), pas sur la puissance. La puissance est rapportée bras par bras. |
| C-B4 | La batterie de E4 est sélectionnée a priori. | **Acceptée** | Même correction que B-9. |
| C-B5 | Le budget est contradictoire. | **Acceptée en partie** | Je retire le chiffre de 40 000 appels : irréaliste, et non chiffré en argent. Je rejette deux prémisses. (i) Les « 2 000 à 4 000 jetons » estimaient une consommation, pas un réglage de `max_tokens`, et je n'ai proposé aucun plafond bas. (ii) `--appels-max 160` est la configuration du pilote 4 (RAPPORTÉ), pas une borne du pôle ; A fait la même objection à C sur ce même chiffre. Correction : les prédictions sont des programmes que le noyau évalue **sans appel par test**. Les appels ne servent plus qu'à formuler, muter et recombiner. |

**Scénarios d'évasion de C**

- **Parasite de Kelly.** Le parasite est une loi i.i.d. aveugle au domaine. La bibliothèque contient explicitement la marginale empirique, donc le dénominateur maximisé fait au moins aussi bien que lui et W ≤ 1. Test T6 : promotion attendue ≤ α.
- **Disjonction partitionnée.** Le rival « concaténation des parents » annule son gain par construction. Test T9.
- **Bridage engagé dans le code** : traité par E7′.
- **Combinaison.** Chaque canal est fermé par une mesure. Un résidu reste et je le dis : un bridage coordonné de *toutes* les lignées par un même modèle échappe à la sélection interne. Seule une référence externe peut le voir (E7′, volet population).

**Contrôles négatifs de C** : les quatre sont adoptés, sous les noms T6, T8, T9 et T10.

---

## (b) Expériences corrigées

### Substrat commun révisé (HYPOTHÈSE)

1. **Hypothèse = programme.** Une expression du langage borné, ou une fonction sous bac à sable dans le bras code libre. Elle porte un domaine D_h et émet p_h, éventuellement composite, sur chaque configuration de test.
2. **Tirages frais.** Le noyau génère une issue neuve pour chaque test noté, après l'engagement de l'hypothèse. L'exploration se fait dans un réservoir disjoint et elle est comptée.
3. **Promotion.** L'e-processus Π p_h(x_t) / sup_{q∈𝓛} Π q(x_t) atteint 1/α, où 𝓛 est la bibliothèque aveugle figée par empreinte. La multiplicité dans la population est traitée par e-BH, comme au tour III.1.
4. **Élimination.** Π q_t/p_h atteint 1/α, avec q_t le mélange prévisible de la population ou un rival nommé.
5. **Poids de reproduction** des promues : proportionnel à κ_h·ρ_h.
6. **Mondes.** Une famille par expérience, avec des lois issues d'une grammaire et des lois écrites par un modèle d'une autre lignée.

### E1′. Aptitude : porte d'entrée et contenu, contre survie binaire

- **Bras** : (1) survie binaire à une batterie figée ; (2) porte seule ; (3) porte puis poids κρ.
- **H_A** : à la génération K, le bras 3 donne un κρ moyen des survivants produits par les agents au moins 1,5 fois (illustratif) celui du bras 1. La part de lois vraies ne baisse pas de plus de 3 points (illustratif).
- **H_B** : aucune différence au-delà du bruit d'amorçage.
- **Contrôles fatals** (un échec invalide le bras) :
  - T1a : nul dans 𝓛, promotion ≤ α ;
  - T6 : parasite de Kelly, promotion ≤ α ;
  - T3 : paris couverts (ε = 0,05 et 0,2, illustratif), promus seulement si leur composante nette est vraie, et classés sous la loi nette.
- **Contrôles qui réfutent une partie de mon schéma** :
  - T1b : nul hors de 𝓛 (dérive non modélisée). Une promotion supérieure à 2α (illustratif) réfute « la bibliothèque suffit ». 𝓛 doit alors être étendue avant toute autre expérience.
  - T8 : loi vraie exacte, avec 1 % de bruit d'étiquetage. On compare trois versions : déterministe, avec modèle de bruit, et couverte vers p_ref. Si la version couverte est mieux classée que celle qui porte le modèle de bruit, ma règle de contenu sélectionne le lissage, et H_A tombe.
- **Ce qui falsifie H_A** : un rapport inférieur à 1,2 (illustratif), ou une perte de lois vraies supérieure à 3 points.
- **Ce qui falsifie H_B** : un rapport d'au moins 1,5 avec tous les contrôles fatals tenus.

### E2′. Qui écrit le test (pari inversé)

La théorie prédit maintenant l'*absence* d'effet. Avec tirages frais, engagement préalable et nul composite, Ville tient quel que soit le rédacteur du test.

- **H_A** : la fausse promotion du bras auteur est ≤ α + 2 points (illustratif) et égale à celle du bras scellé.
- **H_B** : le bras auteur dépasse le bras scellé d'au moins 5 points. Un canal de fuite subsiste alors.
- **Puissance** : rapportée par bras, jamais exigée égale.
- **T2** : mêmes hypothèses fausses, engagées après 0 puis après k requêtes d'exploration. Une pente de log W en k significativement positive réfute le scellé par tirage frais.
- **Lois vraies étroites** : taux de mise à mort par l'adversaire confiné à D_h, rapporté loi par loi.
- **Ce qui falsifie H_A** : un écart ≥ 5 points ou une pente T2 positive.
- **Ce qui falsifie H_B** : un écart < 2 points avec une pente nulle.

### E3′. Recombinaison

- **Bras** :
  1. tirage stratifié avec filtre ;
  2. appariement par opérateur, extrait par le noyau d'un sous-arbre canonisé, avec filtre ;
  3. squelette d'opérateur tiré au hasard. Ce contrôle est celui que A oppose à C ; je l'emprunte.
- **Fertilité** : la descendante est promue contre le mélange prévisible {parent a, parent b, concaténation de a sur D_a et de b sur D_b}, avec κρ ≥ le maximum des parents et une taille ≤ celle du plus grand parent plus une constante.
- **H_A** : dans le monde à isomorphismes plantés, le bras 2 fait au moins 1,5 fois le bras 1 et au moins 1,5 fois le bras 3 (illustratif). Dans le monde sans isomorphisme, il n'y a pas d'écart.
- **H_B** : le bras 2 fait au plus le bras 1, ou le bras 2 est proche du bras 3 (le gain vient alors du squelette fourni, pas de l'appariement).
- **Contrôles** :
  - T9 : la concaténation doit avoir une fertilité nulle. Sinon le rival est mal mis en œuvre et le bras est invalide.
  - T5 : lois de grammaire contre lois écrites par un modèle. Une chute de fertilité dans le premier cas montre que l'on mesurait la proximité des a priori.
  - Longueur : descendantes tronquées.
  - Remplissage : un squelette gonflé d'opérations neutres doit retomber sur la même forme canonique.
- **Ce qui falsifie H_A** : bras 2 < 1,2 × bras 1 dans le monde planté, ou un écart dans le monde témoin.
- **Ce qui falsifie H_B** : les seuils de H_A atteints, avec T9 et le remplissage tenus.

### E4′. Substrat : langage borné ou code libre

Plan croisé substrat × aptitude (défaut ou E1′). Budget égal en jetons, réflexion comprise, et en secondes de processeur.

- **Batterie** : 30 hypothèses figées par empreinte par un rédacteur aveugle au langage, *avant* l'écriture de celui-ci. Plus les hypothèses produites par le bras code libre à la génération 5.
- **H_A** : le langage borné couvre au moins 80 % de la batterie et au moins 60 % des hypothèses produites (illustratif), avec un écart d'exactitude d'élimination ≤ 5 points.
- **H_B** : couverture < 60 %, ou code libre supérieur de plus de 10 points.
- **Contrôles** :
  - des lois non testables par construction, que les deux bras doivent déclarer non testées ;
  - l'effet du substrat est comparé à celui de l'aptitude. S'il le dépasse, ma position du tour III.1 tombe.

### E5′ et E6′

Seuls changent la famille de mondes (neuve) et la métrique (κρ des promues, en remplacement de log W brut). Les bras, les seuils et les contrôles restent ceux du tour III.1. Ces deux expériences n'étaient attaquées que par héritage de B-1 et B-5.

### E7′. Sabotage dans le code engagé (méthode seulement)

Le bridage est **scripté, non appris**, et engagé dans le code. Je ne donne aucune procédure.

- **Détecteur (i), ré-exécution** : détection prévue proche de 0 %. Ce chiffre sert de témoin positif de l'attaque ; ce n'est pas un test.
- **Détecteur (ii), implémentation indépendante** : la spécification de l'expérience est figée, puis une autre lignée, d'une autre espèce, l'implémente sans accès au premier code. Le désaccord est jugé contre une bande calibrée sur des exécutions honnêtes non déterministes (T10), avec des graines fraîches secrètes, tirées **sur le réservoir d'exploration seulement**. Cela répond à l'objection de A contre C : la part scellée n'est jamais interrogée deux fois.
- **H_A** : (ii) détecte au moins 80 % des bridages à 1 % de fausses alertes (illustratif).
- **H_B** : (ii) ne dépasse pas (i) de 20 points.
- **Volet population** : une fraction f de lignées est bridée. La prédiction est que la sélection les élimine si f < 1. À f = 1, rien d'interne ne détecte le bridage, et c'est rapporté comme limite.
- **Ce qui falsifie H_A** : une détection < 50 % (illustratif).
- **Ce qui falsifie H_B** : (ii) dépasse (i) d'au moins 20 points avec T10 tenu.

### Instruments révisés

- **c1** : paires de même multiensemble de jetons. Un sac de mots au-dessus de l'aléatoire invalide la paire (T7).
- **c4** : part scellée retirée à chaque évaluation. Les jetons-témoins ne servent qu'à détecter la copie.
- **c5 et c6** : métriques calculées contre le nul composite et le rival de concaténation.

### Ancrage révisé (tout est illustratif)

- **Appels** : une population de 40, 8 générations, environ un appel par descendante et par recombinaison, soit 400 à 600 appels par bras et 5 000 à 7 000 sur une douzaine de bras. Les plafonds de réflexion de la v5.1 sont respectés. Le coût se calcule sur `budget()`.
- **Évaluation** : 10⁵ à 10⁶ tirages par expérience, sur processeur, sans appel de modèle.

### Règle de décision révisée (figée avant résultats)

1. Si T1a ou T6 échouent en E1′, aucune autre expérience n'est lancée : le critère est cassé.
2. Si T1b échoue, on étend 𝓛 puis on reprend E1′.
3. Ensuite, E4′ décide de la voie, comme au tour III.1 :
   - langage borné suffisant et aptitude dominante : perfectionner l'organisme ;
   - sinon : voie hybride, avec un moteur de mutation de la littérature sous le bac à sable du noyau, sans clé, et l'évaluateur E1′ tenu par le noyau.
4. Agentic Scientist v3 reste écarté tant que ses agents héritent des clés (RAPPORTÉ, faits B).

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi (RAPPORTÉ par les faits, sans audit de ma part)

- L'organisme n'exécute pas d'expériences arbitraires. Depuis C-17, sa réécriture passe par un gabarit de trois paramètres bornés. Le chemin du code brut a été retiré pour la sûreté.
- Dans la configuration notée du pilote 4, il y a une caste par tâche, donc aucun arbitrage. Les castes contradictoires n'y sont pas exercées.
- Le successeur est une copie du code avec une mémoire. L'apport de la mémoire ISVD n'est mesuré nulle part dans les faits.
- Une métrique qui ne lit pas la vérité a déjà été écrite dans ce programme, puis jugée non discriminante et écartée. Le risque de Goodhart s'est donc réalisé une fois.
- Agentic Scientist v3 lance des agents à pleins droits dans Docker, qui héritent des clés fournies. Ses auteurs rapportent des raccourcis qui violent la méthode, des grilles imparfaites, une dérive vers le réglage et une corrélation de 0,44 entre notes des relecteurs-agents et performance.
- Aucun score de pilote n'est servi. Les prouesses du dossier de passation n'ont pas de pièce sur `origin/main`.

### Ce qui n'est pas établi (HYPOTHÈSE)

- Que l'organisme apprenne d'une génération à l'autre, que ses castes calibrent mieux qu'une auto-cohérence à budget égal, ou que ses mécanismes nommés apportent quelque chose au-delà de leur nom.
- Que la bisociation soit plus fertile qu'un tirage stratifié. La pièce C est absente.
- Que ShinkaEvolve et OpenEvolve réécrivent le système lui-même plutôt qu'un programme cible. C'est à vérifier sur les README.
- Que mon aptitude fonctionne. Les deux équipes rouges y ont trouvé des failles réelles : p₀ mal spécifiée, contenu non défini, rival indéterminé, fuite par exploration, E7 hors de la menace. Je les corrige **sur le papier seulement**.
- Que le monde planté se transfère aux activations d'un modèle réel.
- Qu'une défense interne détecte un bridage coordonné de toutes les lignées par un même modèle. Je prévois que non.

### L'expérience à faire en premier : E1′, avec ses contrôles fatals

**Pourquoi elle.** Si le critère de sélection promeut des parasites, alors choisir entre organisme et littérature revient à choisir le moteur d'une sélection fausse. E1′ est aussi la moins chère : processeur, monde planté, quelques centaines d'appels par bras (illustratif), deux à trois jours en comptant la construction du nul composite (illustratif).

**Ce qu'elle peut réfuter, dans l'ordre :**

1. **T6 et T1a.** Si le parasite de Kelly ou un monde nul dans la bibliothèque donnent une promotion > α, ma mise en œuvre est fausse. On arrête, et ma proposition tombe.
2. **T1b.** Si un nul hors bibliothèque fait gonfler la promotion au-delà de 2α, la garantie ne vaut que sur 𝓛. Toute extension au réel exige alors d'étendre 𝓛, et c'est un coût qu'il faut dire.
3. **T8 et T3.** Si les lois couvertes sont mieux classées que les lois franches à modèle de bruit, ma règle de contenu récompense la prudence, contrairement à la question 2 de l'arbitre.
4. **Comparaison principale.** Si la survie binaire à une batterie figée égale la porte suivie du contenu, mon critère est un coût inutile. Le manque du pôle serait alors un substrat d'exécution, et adopter un moteur de la littérature sous le noyau passe devant l'écriture d'un critère.

**Ce qui me ferait changer d'avis** : l'issue 1 ou l'issue 4 ci-dessus, ou bien, en E4′, un effet du substrat supérieur à celui de l'aptitude.

FIN-DE-CELLULE