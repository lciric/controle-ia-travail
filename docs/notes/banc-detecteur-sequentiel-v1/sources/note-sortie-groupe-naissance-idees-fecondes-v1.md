# Naissance des idées scientifiques fécondes et contrôle boîte blanche : note de sortie du collisionneur groupé, bras principal et bras témoin

- **Date** : 2026-11-24, après 18:18 UTC.
- **Dossier** : `runs/collisionneur-groupe-naissance-idees-fecondes-v1/bras-principal/` et `.../bras-temoin/` (branche `idees/lot-8-chef-d-orchestre-v1`).
- **Questions** (dossier `docs/notes/protocole-x-structure-du-langage-v1/`) : bras principal, `question-neutre-collisionneur-groupe-g1-v1.md` ; bras témoin, `question-temoin-neutre-collisionneur-groupe-g1-v1.md`. Chaque `question-etage3.md` est identique à sa source (vérifié par comparaison).
- **Faits** : `faits-neutres-groupe-g1-v1.md`, identiques octet pour octet au `faits.md` des deux bras (vérifié par comparaison).
- **Accords** : relance pour faux échec (GO-2026-11-24-03) ; ligne de reprise de 30 dollars par bras (GO-2026-11-24-35).
- **Dépense comptée** (`verifier-fin.log` de chaque bras) : bras principal 6,99 dollars, dont Opus 2,11, Carbon 3,11, Neon 1,77 ; bras témoin 8,20 dollars, dont Opus 2,20, Carbon 3,80, Neon 2,20. Google étant servi par une clé gratuite, le coût réel de Carbon et de Neon est nul. Le payé réel est celui d'Opus, environ 2 dollars par bras.
- **Tours** : neuf cellules valides par bras, chacune réussie au premier essai servi. Trois conceptions à l'aveugle (tour III.1), trois critiques croisées (III.2), trois réponses aux critiques (III.3).
- **Historique technique.**
  - Première course le 24 novembre à 06:42:04 UTC, avec le programme `collisionneur-v9-v8d` prévu au devis. Seule l'invite de la conception d'Opus est partie (« essai 1 », sans réponse), puis le conteneur a été coupé. Le journal de console de chaque bras ne contient que cette ligne.
  - Relance à 17:10:40 UTC, pour faux échec, avec le programme `collisionneur-v9-v8r` (empreinte `3943e1ca…`). Un seul écart au devis : Google est appelé par l'interface Interactions en arrière-plan, parce que le conteneur coupe à 300 secondes une connexion qui n'a pas reçu son premier octet. Chaque interaction a été supprimée chez Google après lecture (`journal-etage3.txt`).
  - La conception d'Opus porte le numéro d'essai 2 dans `journal-etage3.txt`, mais 1 dans le tableau de `verifier`. Le lecteur a vérifié, dans les deux bras, que les invites des essais 1 et 2 sont identiques et que la cellule écrite est la réponse de l'essai 2. L'écart n'est qu'une numérotation.
  - Cellules faites de 17:10 à 18:05 UTC (principal) et de 17:10 à 18:11 UTC (témoin).
- **Vérification finale** : « tout tient » dans les deux bras (`verifier-fin.log`).
- **Modèles et lettres** (les mêmes dans les deux bras) : Claude Opus 5.5 = lettre A (réflexion adaptative, toujours active ; effort « high » envoyé par le programme ; la « provision de réflexion 0 » des journaux n'est qu'un poste de devis) ; Carbon (`gemini-4-carbon`) = lettre B (réflexion « high ») ; Neon (`gemini-4-neon`) = lettre C (réflexion « xhigh »).

Rédigé par un lecteur Opus 5.5, classe C, à partir des deux questions, des faits et des dix-huit cellules lues en entier ; les journaux ont été survolés. **Le lecteur est du même modèle que la lettre A.** Il l'a traitée comme les autres, mais il a pu lui être plus indulgent sans le voir. Deux propositions retenues plus bas viennent d'abord d'elle, et une erreur de calcul d'Opus, que personne n'a relevée, est signalée en section 5.

**Ce que la note n'est pas.** Aucune cellule ne rapporte de mesure. Tout est argument, calcul sous hypothèses ou protocole proposé. Tous les seuils, effectifs, durées, coûts et « chances de succès » sont marqués « illustratif » par leurs auteurs. Chaque bras est un seul tirage par modèle : les différences entre bras ne s'attribuent pas avec certitude à la question.

**Comment lire les renvois.** « (A, principal, III.2) » veut dire : Opus, bras principal, tour des critiques croisées. Chaque modèle numérote à sa façon ses propositions (P1 à P8, A1 à A10, E1 à E6, Action 1 à 7), et un même numéro désigne des choses différentes d'une cellule à l'autre. La note nomme chaque proposition par ce qu'elle teste. Elle distingue trois statuts : **argument** (raisonnement sans calcul), **calcul** (dérivation ou arithmétique, refaite ou non par le lecteur), **mesure** (il n'y en a aucune).

**Vocabulaire.** *Référence honnête* : l'échantillon fini de trajectoires ou d'épisodes honnêtes sur lequel un détecteur s'étalonne ; sa taille est notée $n$ et sa fraction contaminée $\varepsilon$. *Processus-e* : accumulation multiplicative de facteurs d'évidence dont l'espérance sous l'hypothèse nulle reste au plus 1 ; l'inégalité de Ville en tire une garantie de fausses alertes valide à tout instant d'arrêt. *Fausse identité* : un concept tenu pour un seul alors qu'il en recouvre deux (chaleur et température). *Promotion en principe* : le destin inverse, une égalité empirique élevée au rang de principe (masses inerte et grave). *Monde planté* : monde synthétique dont la loi n'est connue que d'un évaluateur externe.

## Réserve sur les faits : deux familles manquent

Le §3 de `faits-neutres-groupe-g1-v1.md` annonce « six familles de mécanismes candidats » et n'en énumère que quatre : rapprochement structurel à distance, scission d'identités, dynamiques variationnelles et percolation, invention d'objets hors de l'alphabet. Treize cellules sur dix-huit le signalent, dans les deux bras. Ne le signalent pas : les conceptions de Carbon et de Neon dans les deux bras, et la critique d'Opus au témoin. Au témoin, Carbon déclare même les faits « complets et intègres » (B, témoin, III.1), ce que Neon relève (C, témoin, III.2). Aucun modèle n'invente les deux familles absentes.

- Le lecteur ne sait pas quelles étaient les deux familles prévues. La tâche parle de « dossiers thématiques 1 à 6 » ; il est possible que la rédaction des faits en ait perdu deux.
- Conséquence : rien, dans ce dossier, ne couvre ces deux familles. Si le dossier doit être rejoué, ou servi à l'organisme d'idéation, il faut d'abord corriger les faits.

## 1. Les deux questions, et ce qui les distingue

Les deux bras reçoivent **les mêmes faits** : quatre contraintes du programme (aucun juge génératif, épreuves préenregistrées sur mondes plantés ou en rétrodiction étanche, aucun signal de moniteur comme objectif hors bras d'attaque déclaré, processeur seul d'abord) ; un socle « vérifié » de trente-trois articles sur la géométrie statistique du langage ; quatre familles de mécanismes de naissance des idées ; deux verrous du contrôle boîte blanche (sabotage diffus sous référence finie contaminée ; marge des sondes, juges, poids et essaims à poids partagés). Les deux questions demandent sept points dans le même ordre, avec la même formule de score et les mêmes règles d'intégrité.

Elles diffèrent sur cinq points.

| | Bras principal | Bras témoin |
|---|---|---|
| Cadrage | « Quels mécanismes **résistent à l'analyse mathématique et statistique**, où sont les **frontières infranchissables ou les illusions méthodologiques**, quels **opérateurs prioritaires** pour un organisme couplé au contrôle » | « Concevoir et évaluer » un système d'idéation ; quels mécanismes sont solides, lesquels reposent sur des analogies fragiles, quelles expériences mener d'abord |
| Point 1 | Énumère les angles morts attendus (survivant, comparaisons multiples, circularité, géométrie contre causalité, taille finie, Goodhart) | « Analyse d'expert », sans liste |
| Point 3 | **Formalisation mathématique unifiée** en trois volets imposés : invariant transférable contre artefact ; critère de scission d'une fausse identité et d'objet manquant ; ce qui est défendable ou réfutable en variationnel et percolation | « Démarcation et risques » : ce qu'on peut inférer des corpus, solidité formelle, liste de biais |
| Point 4 | **Comparer plusieurs familles algorithmiques** (principes, hypothèses, **complexité sur processeur seul**, modes d'échec) pour trois usages, dont le transfert au contrôle **nommé en détail** (référence contaminée, marge asymétrique, poids, essaims) | Méthodes et protocoles hors modèle ; instruments de contrôle cités en trois mots (détection séquentielle, robustesse des sondes, audit des poids) |
| Point 7 | **Sensibilité du rang** aux pondérations ; pour six propositions : idée en deux phrases, ce qu'elle suppose, contrôle négatif **apparié en fréquence, degré ou permutation**, **estimation honnête des chances** ; « ce qui demeure hors de portée sans intervention causale » | Pas de sensibilité, pas de chances ; contrôle négatif « explicite » ; « limites qui subsistent » |

Le principal pousse donc vers la formalisation, les frontières d'impossibilité et la comparaison d'algorithmes. Le témoin pousse vers la conception d'un banc et l'ordre des expériences. Le titre de la question témoin dit « bras témoin neutre » : elle a été écrite comme contrôle du cadrage.

## 2. En bref

- **Rien n'est mesuré ; tout ce qui suit est argument ou calcul.**
- **Le détecteur séquentiel sous référence contaminée est l'objet le plus travaillé, dans les deux bras.** Carbon et Neon le placent premier aux tours III.1 et III.3 des deux bras ; Opus le place troisième au principal en III.1, premier au témoin en III.1, et deuxième dans les deux bras en III.3.
  - Les quatre constructions initiales ont été réfutées par les critiques : écrêtage des plus hauts scores qui rend le test anticonservateur (A et C contre B, principal, III.2) ; boule de contamination en variation totale centrée sur la loi empirique, donc vide (A et B contre C, principal, III.2) ; correction statique du seuil $\alpha - k/(n+1)$ (B et C contre A, témoin, III.2) ; troncature dans le mauvais sens (C contre B, témoin, III.2).
  - Un défaut commun a été établi dans les deux bras, indépendamment : **une référence finie gelée rend les facteurs dépendants**, et le produit n'est plus une surmartingale, même sans contamination (A et C contre B, principal, III.2 ; B et C contre A, témoin, III.2). C'est un calcul ; le lecteur l'a suivi et le juge juste.
  - Les réparations du tour III.3 convergent : l'épisode comme unité échangeable, une enveloppe uniforme sur la fonction de répartition par l'inégalité de Dvoretzky-Kiefer-Wolfowitz, un budget d'erreur partagé entre étalonnage et arrêt (B et C, principal, III.3 ; A, témoin, III.3).
- **Les critiques ont surtout démoli des critères formels, au principal, et des plans d'expérience, au témoin.** Au principal : test « cordal » qui ne discrimine pas (B et C contre A ; A et C contre B), Laplacien de faisceau mal lu (A et C contre B), critère de non-polysémie vide (A et B contre C). Au témoin : fuite du futur dans le banc mathlib (B et C contre A), mondes synthétiques qui inversent la règle de leur générateur (B et C contre A ; A et C contre B), confusion entre scission et controverse (B contre A ; A contre B et C).
- **Fausse identité : le texte seul ne suffit pas.** Une fausse identité et un concept unique controversé ont la même loi sur les paires (contexte, prédicat) (B contre A, témoin, III.2 ; accepté et re-dérivé par A, III.3). Le test décisif doit se faire sur un monde planté par un tiers ; les quelque dix cas historiques sont déclarés non jugeables à l'avance (A, B, C, deux bras, III.3).
- **Essaims à poids partagés : la statistique de paire n'apporte rien au-delà de la politique d'une seule copie.** Sous « mêmes poids, contextes indépendants, sans aléa partagé », la loi jointe se factorise (B et C contre A, témoin, III.2 ; A contre B et C, principal, III.2). Opus retire sa proposition au témoin (III.3).
- **Marge asymétrique : attaquer une seule sonde linéaire ne teste rien.** Une rotation orthogonale l'élude en laissant les voisinages intacts (B et C contre A, témoin, III.2 ; C contre B, principal, III.2). La marge mesurée contre une famille d'attaques n'est qu'une borne supérieure (B et C contre A, principal, III.2 ; accepté, III.3).
- **Carbon appose « vérifié » à des énoncés absents des faits** (Ramsey, Gödel, Rice, Ville, noyau Lean ; principal, III.1) et « rapporté » à ses propres choix (témoin, III.1). Repris par A et C dans les deux bras, il corrige au tour III.3.
- **L'expérience proposée en premier dépend surtout du modèle.** Carbon et Neon ouvrent par le détecteur séquentiel dans les deux bras. Opus ouvre, dans les deux bras, par un test des corpus contre des nuls topologiques et fréquentiels (A, principal, III.3 ; A, témoin, III.3).

## 3. Ce que chaque modèle a proposé

### Claude Opus 5.5 (lettre A)

**Bras principal.**

- **Angles morts** (A, principal, III.1). Le dénominateur absent ; les comparaisons multiples cachées (granularité, plongement, fenêtre) ; la circularité des citations ; la géométrie qui n'est pas un mécanisme ; la taille finie ; Goodhart deux fois ; le **confondant instrumental de Merton** (la diffusion d'un instrument cause à la fois le rapprochement et la découverte).
- **Données brutes** (A, principal, III.1). Sources LaTeX et versions successives ; les **macros définies par les auteurs comme trace datée de l'enrichissement de l'alphabet** (argument ; statut « observé non audité ») ; errata et rapprochements abandonnés ; modèles à données d'entraînement publiques (Pythia, OLMo) pour un audit de fuite par recherche exacte.
- **Formalisation** (A, principal, III.1), argument.
  - Invariant transférable : non-réductibilité au nul conditionnel aux nuisances, transfert prédictif étanche, équivalence comportementale au sens de Myhill-Nerode ; un test « continu contre discret » par interpolation sur la corde.
  - Fausse identité : recouvrement relationnel élevé **et** union des contraintes insatisfaisable (sous-ensemble minimal insatisfaisable couvrant deux contextes), scission retenue par gain de longueur de description au-delà de scissions aléatoires. Objet manquant : gain de compression d'un symbole latent sur des données non vues.
  - Percolation : défendable comme famille exponentielle jugée en vraisemblance, ou comme prédiction datée de fusion ; illusoire comme exposant critique sur un graphe unique.
- **Transfert au contrôle** (A, principal, III.1). Argument d'identifiabilité : si un tiers place une masse $\varepsilon$ sur le motif même du sabotage, aucun test de niveau uniforme n'a de puissance contre un taux $r \le \varepsilon$. Marge définie comme la perte de performance minimale imposée à l'attaquant. Coordination d'essaim : contrefactuel « croyance en l'existence d'autres copies ».
- **Classement** (A, principal, III.1). Banc de démarcation par nul conditionnel (200), fausse identité (120), détecteur séquentiel (96), primitives par compression (53), marge (40), transitions en taille finie (36).
- **Défauts relevés** (B et C, principal, III.2).
  - Le test de la corde se trompe dans les deux sens : la corde sort d'une variété courbe, et un décodeur lisse rend monotone une paire d'états discrets (B, C).
  - Le sous-ensemble insatisfaisable booléen déclare fausse toute vraie identité mesurée par des instruments biaisés ou à des ordres d'approximation différents (B, C).
  - Le monde planté est défini dans les termes du critère ; comparer le minimum de la longueur de description à des scissions aléatoires crée un biais d'extremum (C).
  - L'argument d'identifiabilité ne vaut que si la contamination porte sur les lois de trajectoires entières ; contre une contamination par action indépendante, un sabotage corrélé dans le temps reste séparable (B, C).
  - Pythia et OLMo laissent passer une fuite structurelle : des manuels postérieurs réorganisent la taxonomie sans contenir la chaîne cherchée (B, C). B propose un duel : modèle moderne filtré contre modèle entraîné sur archives antérieures à 1900.
  - Le nul omet communautés, fermeture triadique et dates d'instruments (C) ; il est à l'inverse « sur-conditionné » au point d'atomiser la fibre et d'annuler la puissance (B).
  - Le contrefactuel d'essaim confond coordination et sensibilité à la consigne (B, C).
- **Après les critiques** (A, principal, III.3). Opus accepte presque tout, en rejette une partie (le nul sur-conditionné : les trois conditionnements ne portent pas sur le même objet ; le fond, atomicité de la fibre, est accepté).
  - **Banc à nul hiérarchique** : fréquences, puis degrés, puis blocs estimés sur le passé seul, puis dates d'instruments. Règle d'arrêt : un niveau dont la fibre compte moins de $1/\alpha$ graphes distincts est déclaré non jugeable avant lecture. Coupures placebo. Statistique unique contre le maximum des comparateurs.
  - **Scission par tension ordinale** : la contradiction doit porter sur des signes de variation, invariante à toute recalibration monotone par contexte. Un biais d'étalonnage ne déclenche rien ; en échange, les tensions seulement cardinales échappent au critère.
  - **Frontière d'identifiabilité** reformulée relativement au modèle de menace du contaminateur ; à démontrer, la simulation ne vérifiant que l'implémentation.
  - Continu contre discret par **sortie d'enveloppe convexe** le long d'une géodésique empirique, étalonné d'abord sur cercle et étoile synthétiques.
  - Essaim rétrogradé en test de non-identifiabilité, avec issue attendue négative.
  - Première expérience : le banc à nul hiérarchique, sur processeur seul.

**Bras témoin.**

- **Analyse** (A, témoin, III.1). « L'évaluation, et non la génération, est le goulot. » La contrainte du processeur est un atout d'étanchéité : de petits modèles entraînés sur des tranches antérieures sont étanches par construction. Une part de la « connaissance latente » pourrait n'être que de la cooccurrence de second ordre, que des prédicteurs de liens triviaux captent déjà.
- **Proposition phare** (A, témoin, III.1) : **la connaissance latente bat-elle le modèle nul topologique ?** Gain d'aire sous la courbe précision-rappel d'un modèle « topologie + plongement » sur « topologie seule », par décile de fréquence.
- **Autres propositions** (A, témoin, III.1). Détecteur séquentiel avec correction $\alpha - k/(n+1)$ ; fausse identité contre homonymie sur monde synthétique ; tension formelle avant une nouvelle définition dans mathlib ; marge sur petit transformeur ; chaînage typé par MeSH contre filtre de fréquence.
- **Défauts relevés** (B et C, témoin, III.2).
  - La correction statique ne protège pas un processus-e : la référence gelée fait diverger le produit même sans contamination (calcul de B et de C).
  - Le banc mathlib conditionne sur « les preuves refactorisées plus tard » : fuite du futur (B, C).
  - Le monde de scission encode sa propre règle ; la controverse ordinaire sur un concept unique a la même loi qu'une fausse identité (B).
  - Le nul « deux sauts » est myope ; une décomposition spectrale capte chemins longs et communautés (B, C).
  - Sous le nul « mêmes poids, contextes indépendants », la loi jointe se factorise : corrélation nulle sous les deux hypothèses (B).
  - La passerelle vers les cartes graphiques présuppose l'invariance d'échelle qu'Opus contestait (C).
- **Après les critiques** (A, témoin, III.3). Opus accepte presque tout et rejette trois points : le contrôle « recâblage + dates permutées » sert encore à détecter des fuites ; une variable cachée non décodable de l'entrée n'existe pas pour un réseau déterministe, la vraie question est la profondeur de calcul ; la passerelle est une règle de budget, transformée en test (A10).
  - **Règle commune** : statistique unique, seuil unique, effectif fixé pour une puissance donnée, « non exécutable » déclaré si l'effectif est hors d'atteinte.
  - **A1′** : géométrie lexicale contre topologie multi-sauts (Katz, PageRank personnalisé, décomposition spectrale), avec contrôle de capacité par coordonnées aléatoires et un **contrôle du contrôle** : un monde où l'information n'est que dans les fenêtres de phrase, pour vérifier que le nul ne l'absorbe pas.
  - **A3′** : boule de contamination sur la fonction de répartition, rayon $k/n + \gamma$, fonction de pari monotone ; un contrôle de banc qui doit faire échouer la construction initiale.
  - **A2′** : fausse identité contre quatre familles de concepts uniques (variable de régime, controverse de laboratoire, métonymie, piège à deux prédicats).
  - **A5′** : définitions mathlib *non préfigurées* par anti-unification, tous modules scorés, sans filtrage par le futur.
  - **A10** : la suite Pythia prédit-elle le gain de la taille suivante ?
  - Essaim retiré : la coordination de copies sans aléa partagé est une propriété d'une seule copie.
  - Première expérience : A1′, avec A3′ en parallèle.

### Carbon (identifiant gemini-4-carbon, lettre B)

**Bras principal.**

- **Formalisation** (B, principal, III.1), argument.
  - Invariant : équivariance multi-pas d'un alignement sur des mots d'opérateurs typés, contre un nul de configuration ; « continuité cordale » par rang du jacobien ; stabilité sous repondération des mentions.
  - Fausse identité par **cohomologie de faisceau** : pivot déductif fortement connexe (conductance) avec « holonomie non nulle », lue sur la plus petite valeur propre du Laplacien de faisceau.
  - Objet manquant : résidu de compression entre macros du premier ordre et quotients d'ordre deux.
  - Frontières : Gödel, Rice et un « plancher minimax de Huber », tous marqués « vérifié ».
- **Classement** (B, principal, III.1). Supermartingale conforme écrêtée sur la cohérence inter-pas (240), objets manquants par anti-unification d'ordre deux sur mathlib (200), faisceau (150), essaims par spectres invariants et points de Schelling (128), aligneur équivariant (120), sonde d'homomorphisme sur modèles d'environ 8 milliards (80). Chances données de 35 à 65 % (illustratif).
- **Défauts relevés** (A et C, principal, III.2).
  - La supermartingale écrête les **plus hauts** scores de la référence : la p-valeur devient anticonservatrice, même sans contamination ; et une référence finie fixe rend les facteurs dépendants (A, C ; calcul de C par l'inégalité de Jensen).
  - $\lambda_{\min}$ du Laplacien $\delta_0^\top\delta_0$ renseigne sur l'absence de section globale ($H^0$), pas sur $H^1$ ; scinder ne peut que faire baisser $\lambda_{\min}$ (A, C).
  - « Amputer en dépliant les usages » laisse l'empreinte de la définition retirée : sa redécouverte est vraie par construction (A, C).
  - Les spectres de $W_QW_K^\top$ ne sont pas invariants sous les reparamétrisations exactes non orthogonales (C) ; la proximité spectrale détecte la parenté des poids, vraie par prémisse, non la coordination (A, C).
  - La sonde d'homomorphisme n'est pas attaquée : le duel teste la non-transférabilité d'une attaque visant un autre instrument (C).
  - Arithmétique de la sensibilité fausse : sous un coût à la puissance 1/2, la sonde reste sixième (A ; refait par le lecteur, juste).
- **Après les critiques** (B, principal, III.3). Carbon accepte presque tout, rétrograde ses statuts « vérifié » et rejette deux points.
  - **Enveloppe de Dvoretzky-Kiefer-Wolfowitz à dénominateur $\lfloor(1-\varepsilon)n\rfloor$**, sur épisodes réinitialisés : majorant déterministe de la survie honnête, valide sous toute contamination ; calibrateur $f(u)=0{,}5\,u^{-1/2}$, seuil $1/(\alpha-\beta)$.
  - Rejet argumenté : une contamination **basse** rend ce test plus puissant, pas moins ; la pire est en queue haute.
  - Rejet sur $H^1$ : sur un graphe sans 2-cellules, $H^1 \ne 0$ dès qu'il y a des cycles ; il garde un $0$-Laplacien normalisé sur contraintes ordinales, avec pénalité de partition et ré-optimisation sous le nul.
  - Essaims : contrôle par **clones honnêtes de mêmes poids**, permutations des choix, statistique d'excès de collision.
  - Sonde attaquée directement, à budget égal, avec une seconde sonde linéaire secrète comme témoin.
  - Première expérience : l'enveloppe sur processeur seul, quatre contrôles (référence propre, contamination basse, haute, dérive de tâche).

**Bras témoin.**

- **Audit des mécanismes** (B, témoin, III.1), argument. Alignement « fragile sur texte non typé » ; scission « sous-exploitée et formalisable » par **frustration de cycles signés** dans un seul cluster dense ; percolation « à haut risque d'artefact » ; abstractions : deux pistes solides (symétries, anti-unification) et une risquée (surprise interne).
- **Classement** (B, témoin, III.1). Processus-e « Huber-DKW » (500), frustration signée (400), test microcanonique de percolation (300), synthèse d'objets par longueur de description (256), sondes d'holonomie de cycle (250), audit spectral des poids et coordination (187,5).
- **Défauts relevés** (A et C, témoin, III.2).
  - Troncature dans le mauvais sens : elle sous-estime la moyenne honnête et fait diverger les fausses alertes ; la marge de Dvoretzky-Kiefer-Wolfowitz dépasse déjà le signal aux valeurs proposées (C).
  - Validité « vraie par construction » si le simulateur respecte les hypothèses de l'outil (A).
  - Une loi multivariée ou une rétroaction produisent des cycles frustrés sans fausse identité ; permuter les signes **gonfle** la frustration du nul (C, avec la formule $3p(1-p)^2+p^3$ ; refait par le lecteur, juste).
  - **Scission contre promotion en principe** : une frustration peut marquer toute identité contestée ; A propose un test de recevabilité qui oppose les deux destins à volume de controverse égal (A).
  - Concepts OpenAlex attribués par un classifieur postérieur (C, en reprenant A).
  - Sonde d'holonomie : budget de six requêtes contre une, ensemble d'évasion sélectionné sur les échecs de la sonde linéaire, contrôle par permutation des coordonnées qui laisse les distances invariantes (A, C).
  - Accord entre copies : $\sum p_i^2 \ge 1/K$ du seul fait du biais positionnel (A, C).
- **Après les critiques** (B, témoin, III.3). Carbon accepte presque tout, rejette deux points.
  - Rejet partiel du plancher en $\sigma_0\sqrt{\varepsilon}$ d'A : pour des scores bornés dans $[0,1]$, le biais de contamination est borné par environ $\varepsilon/(1-\varepsilon)$, et la variance pertinente est celle des moyennes d'épisode (calcul non refait).
  - Rejet de « $h(x_k)-h(x_0)=0$ identiquement » (C) : une boucle neutre concaténée donne une autre chaîne, de même état canonique.
  - **E1** : processus-e de type Bernstein empirique sur blocs, moyenne écrêtée des deux côtés majorée du biais pire cas, contre une somme cumulée écrêtée sur la **même** référence.
  - **E2** : le test de recevabilité d'A (scission contre promotion), sur 400 concepts générés par un tiers.
  - E3 à E6 : anti-unification sous réécriture algébrique et cônes de dépendance disjoints ; boucles de Myhill-Nerode contre sonde linéaire à budget égal, sous attaque adaptative ; percolation strictement antérieure à la coupure ; audit spectral sur cohortes d'adaptateurs de même rang.
  - Première expérience : E1.

### Neon (identifiant gemini-4-neon, lettre C)

**Bras principal.**

- **Présupposés** (C, principal, III.1). Six. Le premier : l'idéation affronte un bruit non stratégique, le contrôle un agent adaptatif ; le transfert entre les deux n'est établi par aucun fait.
- **Formalisation** (C, principal, III.1), argument. Un principe unificateur : survivre à un nul qui préserve les marges, respecter une invariance de quotient, et gagner en longueur de description hors échantillon.
  - Invariant : nul de marges, **invariance entre genres de textes** (contre le biais de déclaration), congruence de Myhill-Nerode et homomorphisme sous intervention.
  - Fausse identité : recouvrement de surface « pour toute partition » et obstruction de recollement.
  - Objet manquant : dérive d'épicycles, résidu à symétrie non représentée, goulot compressif.
  - Percolation : test de connectivité géante normalisé par un modèle à blocs stochastiques corrigé du degré.
- **Classement** (C, principal, III.1). Processus-e robuste dans une boule de Huber (400), filtre de démarcation à trois étages (200), scission (150), essaim par corrélation résiduelle sur choix équivalents (128), zones de tension par e-graphes (100), marge des sondes causales sur 8 milliards (50). Sensibilité calculée sous trois pondérations (refaite par le lecteur, juste).
- **Défauts relevés** (A et B, principal, III.2).
  - Une boule en variation totale autour d'une loi empirique ne contient aucune loi continue : les facteurs sont invalides ou triviaux (A) ; l'erreur d'échantillonnage expulse la vraie loi de la boule (B).
  - Le critère « pour toute partition » est vide : la partition qui coupe selon les contextes rend les deux lois disjointes (A et B, indépendamment).
  - L'invariance entre genres rejette une vraie loi sous un biais de déclaration qui dépend de l'issue, et laisse passer un biais commun à tous les genres (B, avec un calcul par rapport de cotes ; A).
  - La congruence de Myhill-Nerode, exigée sur tout suffixe, favorise les tables discrètes et rejette un flot continu chaotique (B).
  - Un modèle à blocs ajusté sur le graphe même absorbe la structure : « réfuter par non-significativité » n'a pas de valeur sans contrôle de puissance (A, B).
  - P6 n'est pas testable : « dégradation pour tout contournement » quantifie sur des attaquants non observés (A) ; l'ablation statique ne prouve pas l'impossibilité d'une ré-allocation vers un canal libre (B).
- **Après les critiques** (C, principal, III.3). Neon accepte presque tout et rejette un point : un gain prédictif dû à une cause commune (instrument partagé) n'est pas un faux positif mais un levier d'idéation ; il précise que ce gain n'identifie pas une flèche causale directe.
  - **Boule de Kolmogorov-Smirnov** augmentée d'un rayon de Dvoretzky-Kiefer-Wolfowitz, référence scindée en deux moitiés (construction, étalonnage), seuil $2/\alpha$.
  - Invariance entre genres remplacée par l'invariance des **rapports de cotes différentiels**, valable pour un biais multiplicatif propre à un genre ; un biais commun à tous les genres est déclaré non identifiable.
  - **Coupe-circuit sur processeur** emprunté à B : un réseau témoin à canal orthogonal libre ; si le comportement y migre sans coût, la campagne sur 8 milliards est bloquée.
  - Essaim recentré sur la coïncidence sémantique sous permutations de surface indépendantes, étalonnée sur des copies honnêtes de mêmes poids.
  - Percolation suspendue.
  - Première expérience : la martingale robuste, puis le coupe-circuit.

**Bras témoin.**

- **Analyse** (C, témoin, III.1). Trois constats : stationnarité descriptive contre adversité adaptative ; effondrement des protocoles naïfs ; **taux de base** (positifs rares dans les deux tâches). Données : hypergraphes **non projetés**, la projection unipartite créant de fausses cliques.
- **Classement** (C, témoin, III.1). Frontière d'identifiabilité des processus-e robustes (400), percolation sur hypergraphes non projetés (300), scission par tension intra-documentaire (256), alignement typé contre BM25 et chaînage A-B-C (192), primitives par symétries et vérificateur formel (187,5), invariants locaux sur petits modèles (150).
- **Défauts relevés** (A et B, témoin, III.2).
  - Zones grises dans les six duels (A, B).
  - Frontière « $\rho > 2\varepsilon$ » mal posée : sans amplitude du décalage ni variance honnête, une fréquence n'est pas une condition d'identifiabilité ; A propose un plancher en $\sigma_0\sqrt{\varepsilon}$ et un duel sur la pente (A).
  - Aux valeurs proposées, le plancher fini dépasse le signal : $H_A$ est inaccessible (B ; calcul refait par le lecteur, juste).
  - Le nul de percolation conserve les dates d'entrée, donc la loi de Heaps, cible même des urnes (A) ; un modèle auto-excité bat ce nul sans aucune transition (B).
  - Les jeux d'intérêt d'experts (Gu et Krenn ; Sternlicht et Hope) ne sont pas des ponts réalisés ; l'audit de polysémie exige un humain ou un juge génératif interdit (A). L'alignement d'arbres d'équations apparie des gabarits ubiquitaires stériles (B).
  - Copies de même graine contre graines distinctes : excès garanti par Cauchy-Schwarz ; filtrer les choix à forte entropie censure la coordination focale (A, B).
- **Après les critiques** (C, témoin, III.3). Neon accepte presque tout et rejette un point : il refuse le critère de B (battre la somme cumulée à horizon fixe), parce qu'à horizon connu la somme cumulée est optimale ; l'enjeu d'un processus-e est l'arrêt optionnel.
  - Règle anti-zone grise : intervalle plus étroit que l'écart entre seuil opérationnel et seuil nul ; trois issues, dont « les deux réfutées ».
  - **Sous-test 1a** : pente de la frontière, en deux régimes (variance bornée : pente 1/2 ; scores bornés lus par indicateur de queue : pente 1).
  - **Sous-test 1b** : processus-e contre somme cumulée corrigée de Bonferroni sur quatre horizons, même score, même référence.
  - Percolation contre un nul composite (auto-excitation, blocs, croissance exogène) ; scission contre promotion et controverse sur monde scellé ; alignement après masquage des gabarits ubiquitaires ; invariants locaux en mode inductif à un seul exemple, sous attaque adaptative.
  - Première expérience : l'Action 1, « porte théorique éliminatoire » pour tout le volet contrôle.

## 4. Ce que la différence de question change, et ce qu'elle ne change pas

**Ce qui ne change pas.** Ces points apparaissent dans les deux bras, chez les trois modèles. Ils sont robustes au cadrage, au moins sur ces deux tirages.

- Le détecteur séquentiel sous référence contaminée est l'instrument de contrôle le plus prêt, et il se teste d'abord par simulation sur processeur.
- Une référence finie gelée ne donne pas de garantie séquentielle par simple correction de seuil ; l'unité échangeable est l'épisode ; le budget d'erreur se partage entre étalonnage et arrêt.
- La rétrodiction historique des scissions n'a pas la puissance d'un test : une dizaine de cas.
- Les mondes synthétiques écrits par l'équipe qui écrit le détecteur sont vrais par construction ; il faut un évaluateur externe aveugle au score.
- Dépliage d'une définition retirée : sa redécouverte n'est pas une invention.
- Essaims : sans aléa partagé, la paire n'apporte rien de plus que la copie seule ; tout test comportemental exige des permutations indépendantes des options.
- Une marge mesurée contre une attaque visant un autre instrument ne vaut rien ; une marge mesurée contre une famille d'attaques n'est qu'une borne supérieure.
- Percolation et principes variationnels : illusoires comme exposants critiques sur un graphe fini, défendables seulement comme modèles prédictifs battant un nul riche.
- Le score multiplicatif n'a pas de sens cardinal ; seul l'ordre grossier compte (A, B, C, deux bras).
- Les trois modèles disent ne pas savoir, au moins dans un bras, si une marge asymétrique durable existe à 8 milliards de paramètres.

**Ce qui change.** Les écarts suivent la lettre des questions, sauf le dernier.

1. **Formalisation.** Seul le principal en produit vraiment : conditions d'invariant, cohomologie, critères de longueur de description, conditions de puissance écrites en lois et estimateurs. Les critiques du principal y ont consacré l'essentiel de leurs efforts, et en ont réfuté la plupart. Au témoin, les critiques portent sur les plans : contrôles manquants, fuites, puissance.
2. **Contrôles nés dans un seul bras.**
   - Au témoin seulement : **la promotion en principe** comme classe négative obligatoire (A, témoin, III.2, adoptée par B et C) ; la **non-identifiabilité entre fausse identité et controverse** depuis les paires (contexte, prédicat) (B, témoin, III.2) ; la fuite du futur dans mathlib (B, C) ; le nul auto-excité pour la percolation (B) ; la somme cumulée sur le même score (B, C) ; la pente $\varepsilon$ contre $\sigma_0\sqrt{\varepsilon}$ (A) ; le masquage des gabarits ubiquitaires (B).
   - Au principal seulement : les vraies identités sous biais d'instrument et ordres d'approximation différents (B, C contre A) ; la loi du minimum pour le nul de la scission (C) ; le nul hiérarchique jusqu'aux dates d'instruments (C contre A, puis A, III.3) ; le témoin à canal orthogonal libre (B contre C) ; la fuite structurelle des modèles à données ouvertes (B contre A) ; l'invariance de jauge des spectres de poids (C contre B).
   - Les faits mentionnent la promotion en principe dans les deux bras. Le principal ne l'a pas exploitée : sa question oriente vers le critère formel de scission, non vers le destin historique d'une identité. Le lecteur y voit un effet probable du cadrage, sans pouvoir l'établir avec un tirage.
   - Rien n'empêche de transposer chacun de ces contrôles à l'autre bras.
3. **Ce qui est demandé seulement au principal** est fourni seulement là : sensibilité du rang, chances honnêtes (Carbon de 35 à 65 %, Neon par fourchettes, Opus en mots ; toutes illustratives), comparaison d'algorithmes avec complexité.
4. **La percolation garde un rang plus haut au témoin.** Neon la place deuxième aux deux tours, Carbon troisième en III.1. Au principal, elle est dernière ou suspendue chez les trois. La question principale demande explicitement « ce qui est défendable ou réfutable », ce qui a pu pousser vers le verdict d'illusion. Le lecteur ne peut pas l'établir.
5. **La première expérience suit le modèle, pas la question.** Carbon et Neon ouvrent par le détecteur séquentiel dans les deux bras ; Opus, par la démarcation des corpus dans les deux bras. Ce n'est pas un effet de cadrage.

## 5. Accords et désaccords

### Accords nés des critiques

- **Duels sans zone grise** : une statistique, un seuil, deux hypothèses complémentaires sur le même dispositif, effectif fixé à l'avance (A, B, C, deux bras, III.3). Les formes diffèrent ; voir « Fragile ».
- **Le nul d'une statistique maximisée doit être recalculé en refaisant la maximisation** sur chaque tirage nul : alignement ré-optimisé (A et C contre B, principal), partition ré-optimisée (C contre A ; B contre C), maximum des comparateurs (A, principal, III.3).
- **Comparateur de même capacité** : anti-unification paramétrée plutôt que fouille de sous-arbres ou compression par paires (C contre A, principal ; A, B, C, témoin) ; sonde linéaire à budget de requêtes égal (C contre B, témoin) ; somme cumulée écrêtée sur la même référence (A, B, C, témoin).
- **Unité statistique explicite et règle de trois** : certifier un taux de fausses alertes de 1 % exige environ 300 unités honnêtes indépendantes sans alerte ; à 8 milliards de paramètres, l'unité est le modèle, d'où une certification hors d'atteinte (A, principal et témoin, III.2 ; accepté par B et C).
- **Extracteurs figés avant la coupure** : pas de spaCy entraîné sur la prose moderne, pas de concepts OpenAlex, MeSH millésimé (A, B, C, témoin).
- **Monde planté écrit par un tiers aveugle au score**, avec lois inédites contre lois isomorphes à des lois célèbres (A, principal, III.2 ; C, principal, III.3).

### Calculs refaits et calculs non refaits

Refaits par le lecteur, à la main ou par un court calcul exact sur processeur :

- tous les scores des tableaux de classement des six conceptions (justes) ;
- la sensibilité de Neon au principal, sous trois pondérations (juste) ; la correction par A de la sensibilité de Carbon au principal : sous un coût à la puissance 1/2, P2 vaut 282,8 et la sonde reste sixième (juste) ;
- **la sensibilité d'Opus au principal est fausse, et personne ne l'a relevé.** Opus écrit : « si D est élevé au carré, P4 passe deuxième et P2 troisième ; si C est élevé au carré, P5 tombe derrière P8 » (A, principal, III.1). En réalité, sous le potentiel au carré, l'ordre de tête devient : fausse identité 480, banc de démarcation 400, détecteur séquentiel 288, primitives 266,7. Le banc perd donc la tête, contrairement à l'énoncé « P1 reste en tête sous toute pondération raisonnable ». Sous le coût au carré, la marge vaut 8 et l'essaim 6 : la marge reste devant. Les conclusions d'Opus n'en dépendent pas, mais l'énoncé est faux ;
- l'espérance de frustration d'un triangle sous signes aléatoires, $3p(1-p)^2+p^3$ (C, témoin, III.2) ; l'atténuation $(1-2q)^L$, $0{,}8^6 \approx 0{,}26$ (A, témoin, III.2) ;
- le plancher $\sigma_0 \lesssim 0{,}13$ pour $p_s=0{,}03$, $\varepsilon=0{,}05$ ; $\sqrt{0{,}015}\approx 0{,}12$ (A, témoin, III.2) ;
- l'erreur type de Hanley et McNeil, environ 0,10 pour dix positifs, dix négatifs et une aire de 0,80 (A, témoin, III.2 ; le lecteur trouve 0,102) ;
- la marge finie $\sqrt{\ln 20/2000}\approx 0{,}039$, soit $0{,}015+0{,}039 > 0{,}04$ (B contre C, témoin, III.2 ; accepté par C) ; les rayons 0,012 et 0,0027 et le plancher composite 0,032 contre un signal de 0,048 (C, témoin, III.3) ;
- le calibrateur $0{,}5\,u^{-1/2}$ d'intégrale 1 et le seuil $1/(\alpha-\beta)=200$ (B, principal, III.3). Le seuil de 9 alertes sur 400 est présenté comme « borne binomiale à 95 % » d'un vrai niveau 0,01 : c'est plutôt le quantile à 99 % (probabilité 0,992 d'au plus 9 alertes ; au quantile 95 %, 7). L'écart est conservateur et sans conséquence ;
- la règle de trois, 150 unités pour 2 %, 300 pour 1 % (A, principal et témoin, III.2) ;
- l'inégalité déterministe de l'enveloppe à dénominateur $\lfloor(1-\varepsilon)n\rfloor$ (B, principal, III.3) et l'argument de validité de la boule sur la fonction de répartition (A, témoin, III.3) : justes dans leurs grandes lignes, sous l'hypothèse d'épisodes honnêtes indépendants et de même loi ; non démontrés formellement par le lecteur.

Non refaits :

- les conditions asymptotiques de perte de puissance écrites par Carbon au principal (tour III.2) : chaos et exposant de Lyapunov, transition spectrale de Baik, Ben Arous et Péché, mélange des chaînes de recâblage ;
- la borne $\varepsilon/(1-\varepsilon)$ du biais sur scores bornés (B, témoin, III.3), pourtant au cœur du désaccord sur la pente ;
- le taux minimax $\sigma_0\sqrt{\varepsilon}$ de l'estimation robuste de la moyenne (A, témoin, III.2 ; « référence à vérifier » chez A et C) ;
- l'optimalité de la somme cumulée à horizon fixe (C, témoin, III.3) ;
- « $\gamma \approx 0{,}066$ à $n=500$ » attribué à C par Carbon (B, témoin, III.3) : C n'écrit pas ce nombre ; le lecteur trouve 0,061 à $\delta=0{,}05$.

### Désaccords

- **Quelle première expérience.** Au principal : banc de démarcation à nul hiérarchique (A), enveloppe de Dvoretzky-Kiefer-Wolfowitz (B), boule de Kolmogorov-Smirnov puis coupe-circuit (C). Au témoin : géométrie lexicale contre topologie (A), processus-e de Bernstein empirique (B), frontière et arrêt optionnel (C). Les six sont sur processeur seul, sans dépense notable.
- **Pente de la frontière d'identifiabilité.** Plancher en $\sigma_0\sqrt{\varepsilon}$ (A, témoin, III.2) ; faux pour des scores bornés, où le biais reste de l'ordre de $\varepsilon$ (B, témoin, III.3) ; deux régimes, à départager par un duel sur la pente (C, témoin, III.3). Non tranché.
- **Que doit battre un processus-e ?** La somme cumulée à horizon fixe, sur le même score (B, témoin, III.2) ; non, car elle est optimale à horizon connu ; la comparaison juste porte sur l'arrêt optionnel (C, témoin, III.3).
- **Contamination basse et puissance.** Elle fait perdre la puissance (A, principal, III.2, sur la construction initiale de B) ; elle la fait gagner avec l'enveloppe corrigée (B, principal, III.3). Les deux énoncés portent sur deux constructions différentes ; pas de contradiction réelle, mais la seconde n'a été critiquée par personne.
- **Cause commune et gain prédictif.** Faux positif (B contre C, principal, III.2) ; levier d'idéation, à condition de ne pas y lire une flèche causale (C, principal, III.3).
- **Cycle neutre et sonde d'holonomie.** Nul par identité pour un réseau déterministe (C, témoin, III.2) ; non, la chaîne concaténée est différente (B, témoin, III.3).
- **Variable cachée non décodable de l'entrée.** Remède proposé (C, témoin, III.2) ; impossible pour un réseau déterministe, la question est la profondeur de calcul (A, témoin, III.3).
- **Rang de la percolation** : deuxième chez Neon au témoin, dernière ailleurs.
- **Coûts** : de 0 à 500 euros par expérience, tous illustratifs et sur des plans non comparables.

## 6. Ce qui est neuf, ce qui est fragile

### Neuf, au regard de ce que les modèles citent comme connu

Personne n'a cherché l'antériorité. Les éléments suivants pourraient être propres au dossier, sous réserve d'une recherche bibliographique ; plusieurs sont probablement déjà publiés sous un autre nom.

- la **scission par tension ordinale**, invariante à toute recalibration monotone par contexte (A, principal, III.3) ;
- le **contraste entre scission et promotion en principe**, à volume de controverse égal, comme test de recevabilité de tout détecteur de fausse identité (A, témoin, III.2 ; adopté par B et C) ;
- la **non-identifiabilité entre fausse identité et concept unique controversé** depuis les seules paires (contexte, prédicat) (B, témoin, III.2) ;
- la **réduction de l'essaim sans aléa partagé à l'audit d'une seule copie** (A, témoin, III.3, à partir de B et C) ;
- le **nul hiérarchique jusqu'aux dates de disponibilité des instruments**, avec une règle d'arrêt par entropie de fibre, et le dilemme qu'elle exprime : conditionner davantage écarte les artefacts mais atomise la fibre (A, principal, III.3, à partir de B et C) ;
- le **contrôle du contrôle** : un monde où l'information n'est que dans les fenêtres de phrase, pour vérifier que le nul ne l'absorbe pas (A, témoin, III.3) ;
- le **témoin à canal orthogonal libre** comme coupe-circuit avant toute campagne de marge (B, principal, III.2 ; adopté par A et C) ;
- les **macros LaTeX comme trace datée de l'alphabet formel** (A, principal, III.1), retenues ensuite comme simple source de candidats ;
- les **définitions mathlib non préfigurées par anti-unification** (A, témoin, III.3) ;
- le **masquage des gabarits mathématiques ubiquitaires** avant tout alignement d'équations (B, témoin, III.2 ; C, III.3).

Les enveloppes de Dvoretzky-Kiefer-Wolfowitz robustes à une fraction contaminée (B, principal, III.3 ; A, témoin, III.3) relèvent très probablement de la littérature sur la prédiction conforme robuste : le lecteur ne les compte pas comme neuves.

### Fragile

- **Rien n'est mesuré.** Toutes les expériences sont des plans ; aucun modèle ne connaît les effectifs réels (nombre de cas historiques, taille d'une référence honnête du programme).
- **Les faits sont amputés de deux familles** (voir la réserve).
- **Les propositions du tour III.3 n'ont pas été critiquées** : enveloppe de Carbon et son rejet sur la contamination basse ; boule de Kolmogorov-Smirnov de Neon ; processus-e de Bernstein empirique de Carbon au témoin ; sous-tests 1a et 1b de Neon ; tension ordinale, banc hiérarchique et A10 d'Opus.
- **Les règles « sans zone grise » n'en sont pas toutes.** Carbon au témoin garde une indétermination après un doublement d'échantillon ; Neon au témoin admet une troisième issue, « les deux réfutées ». Seule la forme d'Opus (une statistique, un seuil, deux hypothèses complémentaires, « non exécutable » déclaré d'avance) est strictement binaire.
- **Un seuil étalonné sur l'échantillon qui le juge.** Neon fixe le seuil au quantile 0,98 de 160 modèles honnêtes et y lit un taux de fausses alertes « vérifiable par règle de trois » (C, principal, III.3) : sur ce même échantillon, environ 3 sur 160 dépassent par construction. Il faut un lot d'étalonnage séparé.
- **Les statuts de Carbon.** Corrigés au tour III.3, mais plusieurs calculs de ses tours III.2 n'ont été refaits par personne.
- **Les dates de coupure** des modèles « antérieurs à 1900 ou à 1913 » et la fin du corpus de Pythia sont à vérifier ; A10 en dépend.
- **La sensibilité d'Opus au principal est fausse** (section 5) et a échappé aux deux critiques.
- **Le lecteur est du même modèle qu'Opus**, dont deux propositions sont retenues ci-dessous.

## 7. Références à vérifier

Aucune de ces références n'a été vérifiée par le lecteur. Toutes sont citées de mémoire par les modèles, ou reprises des faits, qui ne donnent pas toujours de titre. **À vérifier sur PDF** avant toute citation (règle R7 du dépôt). Les identifiants arXiv ne sont recopiés que lorsqu'ils figurent dans les faits.

| Référence telle que citée | Qui la cite | Pour quoi faire | État |
|---|---|---|---|
| Karkada et al. (2026), arXiv 2602.15029 ; Gupta, Fruengel, Heimersheim (2026), arXiv 2610.37796 ; Gröger, Wen, Brbić (2026), arXiv 2602.14486 | Faits ; A, B, C, deux bras | Symétries de cooccurrence ; étoile discrète ; convergence locale | À vérifier sur PDF ; aucun titre donné |
| Li et al. (2026), arXiv 2601.13717 ; Ma et al. (2026), arXiv 2605.03762 ; Luo et al. (2026), arXiv 2606.02991 ; Hla (2026) | Faits ; A, B, C, deux bras | Ignorance simulée, masquage, modèles antérieurs à la coupure | À vérifier sur PDF ; « Hla » sans titre ni identifiant |
| Xu et al. (2026), arXiv 2602.00986 | Faits ; B, C | Sous-systèmes de récompense lus en lecture seule | À vérifier sur PDF |
| Vafa et al. (2024), « Evaluating the World Model Implicit in a Generative Model », arXiv 2406.03689 ; Vafa et al. (2025), arXiv 2507.06952 | Faits ; A, B, C | Myhill-Nerode, transfert de loi | À vérifier sur PDF |
| Hewitt, Liang (2019), « Designing and Interpreting Probes with Control Tasks », arXiv 1909.03368 | Faits ; tous | Sélectivité des sondes | À vérifier sur PDF |
| Huh et al. (2024), « The Platonic Representation Hypothesis », arXiv 2405.07987 | Faits ; B | Convergence globale | À vérifier sur PDF |
| Levy, Goldberg (2014), « Neural Word Embedding as Implicit Matrix Factorization » ; Mikolov et al. (2013), arXiv 1301.3781 ; Pennington et al. (2014), GloVe | Faits ; B, C | Factorisation de l'information mutuelle ponctuelle | À vérifier sur PDF |
| Gordon, Van Durme (2013), « Reporting Bias and Knowledge Acquisition » ; Bender, Koller (2020), « Climbing towards NLU… » ; Caliskan et al. (2017), arXiv 1608.07187 | Faits ; tous | Biais de déclaration ; forme sans ancrage ; biais culturels | À vérifier sur PDF |
| Tshitoyan et al. (2019), *Nature* 571 ; Luo et al. (2024), arXiv 2403.03230 | Faits ; A, B, C | Connaissance latente rétrospective | À vérifier sur PDF |
| Linzen (2016), arXiv 1606.07736 ; Nissim et al. (2020), arXiv 1905.09866 ; Hamilton et al. (2016), arXiv 1605.09096 ; Dubossarsky et al. (2017), « Outta Control… » | Faits ; A, B, C | Analogies ; dérive sémantique et fréquence | À vérifier sur PDF |
| Gurnee, Tegmark (2023), « Language Models Represent Space and Time », arXiv 2310.02207 ; Abdou et al. (2021), arXiv 2109.06129 ; Louwerse, Zwaan (2009) ; Tobler, Wineburg (1971), titre donné par C « A Cappadocian Speculation » | Faits ; A, B, C | Géométries reconstruites | À vérifier sur PDF ; titre de Tobler et Wineburg donné par un seul modèle |
| Li et al. (2023), « Emergent World Representations… », arXiv 2210.13382 | Faits ; A, B, C | Petits modèles synthétiques | À vérifier sur PDF |
| Swanson (1986) | A et B (« Fish oil, Raynaud's syndrome, and undiscovered public knowledge ») ; C (« Undiscovered Public Knowledge ») | Chaînage A-B-C | À vérifier sur PDF ; **titres divergents** selon les modèles |
| Gentner (1983) ; Uzzi et al. (2013) ; Burt (2004) ; Tria et al. (2014), « The dynamics of correlated novelties » ; Merton (1961), titre donné par C « Singletons and Multiples in Scientific Discovery » ; Davis (1971), titre donné par C ; Lakatos (1976) ; Kuhn (1962) ; Carey (2009), *The Origin of Concepts* | Faits ; A, B, C | Mécanismes de naissance des idées | À vérifier sur PDF |
| Udrescu, Tegmark (2020), « AI Feynman » ; Schmidhuber (2010), « Formal Theory of Creativity, Fun, and Intrinsic Motivation (1990–2010) » | Faits ; A, B, C | Symétries ; surprise et compression | À vérifier sur PDF |
| Gu, Krenn (2026) ; Sternlicht, Hope (2025) | Faits ; B, C | Jeux d'intérêt d'experts et de recombinaisons | À vérifier sur PDF ; aucun titre ; usage comme cible contesté (A contre C, témoin) |
| Ramdas, Grünwald, Vovk, Shafer (2023), « Game-theoretic statistics and safe anytime-valid inference » | A (deux bras), B (témoin) | Processus-e | À vérifier sur PDF |
| Ville (1939) ; Wald ; Page (somme cumulée) ; Lorden (1971) | A, B, C | Garantie à tout instant ; détection séquentielle | À vérifier sur PDF ; Lorden marqué « à vérifier » par A |
| Huber (1965), « A Robust Version of the Probability Ratio Test » | B (principal, III.2) | Contamination | À vérifier sur PDF |
| Massart (1990), « The Tight Constant in the Dvoretzky-Kiefer-Wolfowitz Inequality » | B (principal, III.3), A (témoin, III.3) | Rayon de l'enveloppe | À vérifier sur PDF |
| Benjamini, Hochberg (1995) | A (principal), B, C (témoin) | Taux de fausses découvertes | À vérifier sur PDF |
| Hanley, McNeil (1982), « The meaning and use of the area under a receiver operating characteristic (ROC) curve » | A, B, C (témoin) | Variance de l'aire sous la courbe | À vérifier sur PDF |
| Maslov, Sneppen (2002), « Specificity and stability in topology of protein networks » | A, C (principal) | Recâblage à degrés préservés | À vérifier sur PDF |
| Clauset, Shalizi, Newman (2009), « Power-law distributions in empirical data » ; Cohen et al. (2000), « Resilience of the Internet to random breakdowns » | A (principal) | Fragilité des lois de puissance ; seuil nul | À vérifier sur PDF |
| Hansen, Ghrist (2019), « Toward a spectral theory of cellular sheaves » | A (principal) | Langage des faisceaux | À vérifier sur PDF |
| Ellis et al. (2021), DreamCoder ; Bowers et al. (2023), Stitch | A, C (principal) | Bibliothèques par compression | À vérifier sur PDF ; C marque Ellis « à vérifier » |
| Baik, Ben Arous, Péché (2005) ; Marchenko, Pastur (1967) | B (deux bras), C (témoin) | Seuil spectral ; spectre nul des poids | À vérifier sur PDF ; usage de Marchenko-Pastur contesté (A et C contre B, témoin) |
| Biderman et al. (2023), « Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling » | A (deux bras) | Modèles à données ouvertes | À vérifier sur PDF ; date de fin du corpus à vérifier |
| Modèles et outils : OLMo-7B et Dolma, Llama-3-8B, Mistral-7B, Qwen2.5-7B, Pythia, spaCy/UD, Lean et mathlib, Metamath, OpenAlex, MeSH et PubMed | A, B, C | Ancrage matériel et données | Versions, licences, dates de coupure et réindexations à vérifier |

## 8. Propositions retenues et non retenues

Critères appliqués : soutien de plusieurs modèles, et si possible des deux bras ; résistance aux critiques ; coût ; réversibilité ; ce que la proposition tranche pour la suite. Rappel du dépôt : toute dépense de calcul, tout préenregistrement et toute modification d'hypothèse ou de revendication sont des décisions de Lazar ; les pièces décisives sont rédigées par Fable. Rien de ce qui suit n'est engagé.

### Retenues

1. **Un banc de validité du détecteur séquentiel sous référence finie contaminée, en simulation sur processeur seul.**
   - *Contenu.* Contrôle de banc d'abord : la construction naïve (référence gelée, aucune contamination, horizon très supérieur à $n$) doit échouer, sinon le banc est défectueux. Puis une grille : contamination basse, haute et ciblée ; contamination réelle double de la déclarée ; dérive bénigne graduée ; autocorrélation. Unité : l'épisode. Budget d'erreur partagé entre étalonnage et arrêt. Lignes de base : somme cumulée écrêtée au même rayon, sur le même score et la même référence, à horizon fixe et sous arrêt optionnel. Duel sur la pente de la frontière ($\varepsilon$ contre $\sigma_0\sqrt{\varepsilon}$), dans les deux régimes de Neon.
   - *Soutien.* Les six réponses finales, dans les deux bras ; constructions convergentes de B (principal), C (principal) et A (témoin).
   - *Pourquoi.* Gratuit, sans fuite possible, et c'est le verrou 1 du contrôle. Il rejoint le chantier du programme sur la référence honnête : il faut d'abord confronter ce banc à ce qui y est déjà écrit, pour ne pas le refaire.
2. **Un banc de démarcation des corpus contre des nuls topologiques et fréquentiels, avant tout usage de « connaissance latente ».**
   - *Contenu.* Dénominateur complet des paires candidates à la date $t$. Nuls emboîtés : fréquences, degrés, blocs estimés sur le passé seul, dates de disponibilité des instruments. Comparateurs multi-sauts (Katz, PageRank personnalisé, décomposition spectrale) et coordonnées aléatoires de même dimension. Coupures placebo ; bootstrap par nœuds ; règle d'arrêt par entropie de fibre ; contrôle du contrôle par un monde à information planté dans les seules fenêtres de phrase.
   - *Soutien.* Opus, premier choix dans les deux bras ; filtres de même esprit chez Carbon et Neon au principal, et chez Neon au témoin (alignement contre BM25 et degrés).
   - *Pourquoi.* Une journée de processeur ; ses deux issues réorientent tout le volet corpus.
   - *Réserve.* Proposition d'abord d'Opus, du même modèle que le lecteur.
3. **Pour la fausse identité, un test décisif sur monde planté par un évaluateur externe aveugle au score, avec toutes les classes négatives nées des critiques.**
   - *Contenu.* Vraies identités sous biais d'instrument et ordres d'approximation différents ; concepts uniques à variable de régime, lois multivariées ou rétroactions ; controverse sur un concept unique ; **identités promues en principe** ; polysémie dans un même domaine ; homonymes. Scores candidats à départager : tension ordinale (A), frustration conditionnée aux covariables (B), co-invocation et tension inter-documentaire (C). La rétrodiction historique est déclarée non jugeable d'avance et ne sert qu'à décrire.
   - *Soutien.* Les trois modèles, au tour III.3 des deux bras ; la promotion en principe vient du témoin seulement.
   - *Pourquoi.* C'est la seule façon de juger un mécanisme que les faits disent « peu formalisé » sans dépendre d'une dizaine de cas.
4. **Inscrire dans tout préenregistrement issu de ce dossier les règles de forme corrigées par les critiques.**
   - *Contenu.* Une statistique, un seuil, deux hypothèses complémentaires sur le même dispositif ; effectif fixé par une analyse de puissance, et « non exécutable » déclaré d'avance ; nul de la statistique maximisée recalculé en refaisant la maximisation ; comparateur de même capacité et de même budget de requêtes ; unité indépendante explicite et règle de trois ; extracteurs et taxonomies figés avant la coupure ; amputation placebo et réécriture hétérogène pour toute redécouverte de primitive ; seuils fixés sur des générateurs disjoints de ceux de l'épreuve ; lot d'étalonnage distinct du lot jugé.
   - *Soutien.* Corrections acceptées par les trois modèles dans les deux bras.
   - *Pourquoi.* Ce sont les défauts trouvés partout.
5. **Écrire comme frontière, et non comme expérience, que la coordination de copies à mêmes poids sans aléa partagé se ramène à l'audit d'une seule copie.**
   - *Contenu.* Tout test comportemental d'essaim exige des permutations indépendantes de l'ordre et des étiquettes des options, et un étalonnage sur des clones honnêtes de mêmes poids ; ne rien investir au-delà d'un petit banc sur processeur.
   - *Soutien.* A, B et C, deux bras.
   - *Pourquoi.* Évite une dépense sur un signal qui, sous ces hypothèses, n'existe pas.

### À reprendre ensuite

- **Primitives hors de l'alphabet** : banc sous réécriture algébrique, anonymisation, cônes de dépendance disjoints, comparateur d'anti-unification à variables liées, grammaire probabiliste bien typée comme nul (B et C, témoin, III.3 ; A et B, principal, III.3). Coûteux en ingénierie ; personne ne sait construire un contrôle réel bien typé sans redondance (A et C, témoin).
- **Définitions mathlib non préfigurées** (A, témoin, III.3), si le nombre de positifs, compté avant tout prédicteur, suffit.
- **Coupe-circuit de la marge** : réseau témoin à canal orthogonal libre, sur processeur (B, principal, III.2 ; A et C, III.3). La marge reste une borne supérieure, mesurée sous attaque adaptative directe à budget égal ; cela s'accorde avec le retrait de la marge asymétrique des hypothèses revendiquées du programme (décision N-077), où la mesure reste descriptive.
- **Transfert d'échelle** sur Pythia (A10, A, témoin, III.3), après vérification de la date de fin de son corpus.
- **Percolation** comme outil de réfutation seulement, contre un nul auto-excité à blocs et à croissance exogène (A, B, C, témoin, III.3).
- **Audit spectral des poids** sur cohortes d'adaptateurs de même rang et même budget (B et C, témoin, III.3) : jugeable sur petits modèles, non jugeable à 8 milliards pour un taux de 1 %.

### Non retenues

- **La supermartingale écrêtée des plus hauts scores** (B, principal, III.1) : anticonservatrice ; retirée.
- **La correction statique $\alpha - k/(n+1)$** (A, témoin, III.1) : ne protège pas un processus-e ; retirée.
- **La boule de Huber en variation totale centrée sur la loi empirique** (C, principal, III.1) : vide ; remplacée.
- **La troncature basse de la moyenne de référence** (B, témoin, III.1) : sens inversé ; remplacée.
- **Le test de la corde** (A et B, principal, III.1) : ne sépare pas continu et discret.
- **Le Laplacien de faisceau lu comme $H^1$** (B, principal, III.1) et **le sous-ensemble insatisfaisable booléen** (A, principal, III.1) : mal posés ; réécrits.
- **Le critère de non-polysémie « pour toute partition »** (C, principal, III.1) : vide.
- **La repondération des mentions** (B, principal) et **l'invariance entre genres par divergence de Jensen-Shannon** (C, principal) : n'identifient pas le biais de déclaration.
- **Les signaux d'épicycles $dL/dn$ et $L_\Sigma/H$** (A et C, principal, III.1) : confondus avec l'extension du domaine.
- **Les spectres « invariants de jauge » de $W_QW_K^\top$** (B, principal, III.1) : faux sous les reparamétrisations non orthogonales.
- **Le contrefactuel « d'autres copies existent »** (A, principal, III.1) : non identifiable.
- **Toute épreuve de marge où seule la sonde linéaire est attaquée** (A, témoin ; B, principal ; B, témoin, III.1).
- **Le banc mathlib conditionné sur les preuves refactorisées plus tard** (A, témoin, III.1) : fuite du futur.
- **Les jeux d'intérêt d'experts comme cible de rétrodiction** (C, témoin, III.1) ; **spaCy sur les archives anciennes**, **les concepts OpenAlex**, **MeSH non millésimé** : fuites.
- **Gödel et Rice comme frontières** (B, principal, III.1) : hors sujet pour des extensions définitionnelles et des circuits finis ; reformulées par B.

### Ce qui reste à trancher

- Les deux familles manquantes des faits : lesquelles, et faut-il corriger les faits avant toute suite ?
- La pente de la frontière d'identifiabilité ($\varepsilon$ ou $\sigma_0\sqrt{\varepsilon}$), et ce qu'un processus-e doit battre (horizon fixe ou arrêt optionnel) : à poser dans le banc retenu 1.
- Si ce dossier doit suivre la suite du protocole X (question fusionnée, test de neutralité, service à l'organisme d'idéation) : décision de Lazar.
- Le devis éventuel des pièces sur carte graphique (marge, transfert d'échelle, audit des poids), après les bancs sur processeur.
