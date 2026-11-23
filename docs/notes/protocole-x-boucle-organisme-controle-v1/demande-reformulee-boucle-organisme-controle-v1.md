# Demande reformulée en quatre points — Boucle de rétroaction « Organisme d'idéation ⇄ Programme de contrôle de l'intelligence artificielle » (v1)

Pièce de conception de classe C, mandatée par l'accord `GO-2026-11-23-34` (Carbon en effort élevé en remplacement temporaire de Fable autorisé par `GO-2026-11-23-33`). Langue : français, aucun acronyme non développé, aucun emoji.

---

## Demande d'origine de Lazar

> « et si on veut améliorer l'organisme d'idéation pour derrière contribuer de façon significative pour le domaine via notre programme contrôle IA, que faut-il faire, quel est le programme des priorités ? avec la même méthode de classement. c'est-à-dire que l'organisme amélioré doit permettre de trouver des idées profondes et des découvertes qui peuvent être exploitées dans le programme contrôle IA, tu vois la boucle de rétroaction ? »
> puis :
> « même protocole collisionneur pour cette question »

---

## Prompt obligatoire appliqué verbatim (`CLAUDE.md` ligne 61, `GO-2026-11-22-25`)

> « Je souhaite une version plus approfondie de cette tâche, pas une version plus longue. Avant de la reformuler : (1) indiquez ce qu'un expert du domaine ferait ici, et que je ne demande pas ; (2) précisez les données brutes qu'il utiliserait au départ, au lieu de celles déjà analysées ; (3) indiquez les méthodes et outils spécifiques qu'il utiliserait ; (4) expliquez ce qui, en dehors de vous ou de moi, permettrait de vérifier la validité du résultat. Ensuite, reformulez ma demande pour qu'elle réponde précisément à cette exigence. »

---

## Les quatre points préalables

### 1. Ce qu'un expert du domaine ferait ici, et qui n'est pas demandé

1. **Formaliser le couplage comme un problème d'optimisation à deux boucles séparées par une frontière d'étanchéité stricte.** Un spécialiste de l'évaluation adaptative et du contrôle boîte blanche traiterait la boucle « organisme d'idéation ⇄ programme de contrôle » non comme un cercle vertueux intuitif, mais comme un système à deux horloges sous contrainte d'anti-contamination : (a) l'organisme ne doit **jamais** optimiser un score provenant des moniteurs ou des juges du programme de contrôle (sinon il apprend des raccourcis lexicaux ou des biais du générateur de bancs, ce qui ruine la validité hors distribution) ; (b) le rendement net d'un opérateur ajouté à l'organisme doit être mesuré par l'espérance du nombre d'idées **réellement valides retenues après filtrage** par dollar de calcul dépensé sur cartes graphiques dans le programme de contrôle, et non par la quantité ni la séduction apparente des fiches produites.
2. **Séparer formellement les régimes de transfert et en caractériser la perte d'information.** L'expert refuserait de supposer que des améliorations sur l'idéation générale (graphes biomédicaux ou équations physiques) se transfèrent automatiquement aux problèmes de contrôle boîte blanche. Il mesurerait d'abord le recouvrement entre les **classes d'invariants du monde réel** (sabotage diffus sous pression, évasion adaptative, collusion par poids partagés, corruption d'oracle) et les **classes d'invariants plantables** dans les mondes de l'organisme, car toute classe manquante crée un plafond de rendement asymptotique et une taxe de sur-spécialisation lorsque l'organisme est trop poussé sur ses mondes d'entraînement.
3. **Imposer des objets « doit mourir » et des contrôles négatifs appariés sur chaque maillon de la boucle.** Avant de classer des chantiers, l'expert construirait des cas-tests négatifs par construction : (i) un organisme branché sur les verdicts des juges du contrôle (qui doit être disqualifié ou montrer une explosion de fausses percées) ; (ii) un monde planté où le sabotage ne touche pas la classe d'invariants encodée par l'opérateur (l'opérateur doit s'y déclarer muet) ; (iii) un test de comparaison à coût en jetons et en temps égal contre un tirage indépendant sans réutilisation d'archive.
4. **Distinguer les trois sens de la boucle de rétroaction.** L'expert dissocierait explicitement trois flux aux exigences statistiques incompatibles :
   - *Flux aval (Organisme → Contrôle)* : production d'objets mathématiques candidats (opérateurs d'agrégation, détecteurs d'obstructions, invariants de scission) et de bancs à vérité plantée exécutables ;
   - *Flux amont (Littérature et corpus du contrôle → Organisme)* : détection précoce des tensions, épicycles et faux amalgames dans les papiers récents de sûreté et d'interprétabilité pour orienter l'exploration de l'organisme vers les vrais verrous ;
   - *Flux adverse (Organisme → Équipe rouge du contrôle)* : synthèse de modes de sabotage inédits pour mettre les moniteurs à l'épreuve, à condition absolue de quarantaine (aucune fuite de ces recettes vers l'entraînement des moniteurs).

### 2. Les données brutes de départ (au lieu des synthèses déjà analysées)

1. **Corpus scientifiques et techniques datés en texte intégral et en code source**, avant toute synthèse :
   - les prépublications de sûreté, d'interprétabilité mécaniste et de contrôle de l'intelligence artificielle (sources LaTeX brutes, tableaux d'échecs, définitions formelles et annexes d'articles) avec coupure temporelle stricte (`t0`) vérifiable ;
   - les graphes de relations typées datés en accès libre (relations biomédicales extraites par date, arbres syntaxiques d'opérateurs mathématiques issus des sources de prépublications avant l'introduction de nouveaux formalismes, historiques de dépôts logiciels ouverts avec horodatage) ;
   - les données d'évaluation par des experts humains déjà publiées avec leurs notes brutes et identifiants d'articles (pour calibrer l'écart entre intérêt perçu et fécondité ultérieure).
2. **Spécifications brutes et journaux de fonctionnement des bancs de contrôle et d'idéation** :
   - la géométrie exacte des tâches du programme de contrôle (contributions décomposables par agent et par pas de temps, rubriques des oracles de couverture, journaux de longueur de contexte et de défauts techniques des appels aux modèles) ;
   - les lois génératrices explicites des mondes plantés disponibles sur processeur et les traces brutes des échecs de sondes et d'oracles (strates non couvertes, taux de faux positifs sous corrélation ou sous dérive de régime).
3. **Comptes réels d'usage et de tarification** :
   - coûts réels mesurés par espèce de modèle, taux de pannes et de troncatures constatés dans les journaux d'appels, coût horaire des cartes graphiques pour les épreuves sur modèles de huit milliards de paramètres.

### 3. Les méthodes et outils spécifiques

1. **Modélisation analytique de la boucle fermée** :
   - équation de bilan reliant le taux de base de découvertes exploitables `pi_0`, la sensibilité `q_o` et le taux de fausses admissions `alpha_o` de l'oracle sur mondes plantés au coût unitaire de filtrage sur processeur contre le coût unitaire de vérification sur carte graphique ;
   - modèle de sur-ajustement adaptatif (borne d'optimisme logarithmique sur banc partagé de taille finie, attaque de type *Ladder*) pour quantifier la contamination selon la fraction de recouvrement `rho` entre familles d'entraînement de l'organisme, familles tenues à l'écart et familles de validation finale ;
   - théorème de rendement décroissant sous couverture incomplète `kappa < 1` des invariants réels, avec calcul explicite de l'effort d'optimisation maximal `E*` au-delà duquel la généralisation réelle baisse.
2. **Outils algorithmiques de la couche de structure et d'invention** :
   - représentations sans fuite lexicale : graphes ou hypergraphes orientés typés, matrices de résolvante normalisée et transport optimal de Gromov-Wasserstein fusionné ou partiel pour aligner des schémas causaux entre domaines ;
   - détection d'obstructions et scission conceptuelle : faisceaux cellulaires sur graphes finis, calcul du noyau du cobord et du laplacien de faisceau pour isoler les nœuds confondus par des restrictions incompatibles (faux amalgames entre intention, conscience d'évaluation et style) ;
   - détection ex ante de tensions et synthèse hors alphabet : extracteurs sémantiques sur corpus datés (repérage d'inflation de correctifs ad hoc, d'entropie notationnelle et de ruptures de typage), couplés à un cycle Éveil-Sommeil hybride où un grand modèle propose des abstractions et un compresseur symbolique exact (apprentissage de bibliothèque par longueur de description minimale de type Stitch) sélectionne celles qui compriment conjointement plusieurs bassins éloignés.
3. **Méthode de classement rigoureuse et analyse de sensibilité** :
   - application exacte du score `score = (gain_informatif × facilité × portée × potentiel_de_découverte_majeure) / coût` sur des chantiers atomiques et testables ;
   - analyse de sensibilité bilatérale en faisant varier les exposants de pondération de chaque critère (de `0,5` à `1,5`) pour identifier le noyau invariant des priorités indépendant du choix subjectif des poids.
4. **Protocoles d'inférence statistique et d'anti-fuite** :
   - préenregistrement haché avant toute lecture de résultat, contrôle du taux de fausses découvertes ou processus e toujours valides contre un nul formé de l'archive connue, étanchéité temporelle vérifiée (données postérieures à la coupure du modèle ou modèles entraînés avant `t0`), et audits du générateur de mondes plantés sur des traits de présentation seuls.

### 4. Ce qui, en dehors du directeur et de l'agent concepteur, permettrait de vérifier la validité du résultat

1. **Une expérience rétrospective hors-temps sur données publiques libres** (préenregistrée, sur processeur seul), prouvant que les détecteurs de tensions, l'opérateur de scission ou l'alignement structurel retrouvent des concepts et ruptures historiques publiés après la date de gel `t0` mieux que des modèles nuls de fréquence ou de distance de surface, sans fuite temporelle.
2. **La batterie de mondes plantés exécutables à trois cloisons disjointes** : un générateur indépendant produit des familles d'entraînement pour l'organisme, des familles tenues à l'écart à usage unique par cycle et une famille de validation finale construite par un autre générateur ; un lecteur tiers indépendant vérifie que les opérateurs promus par l'organisme conservent leur gain hors famille et échouent exactement sur les objets « doit mourir ».
3. **Le passage effectif des candidats de l'organisme sur le banc réel du programme de contrôle (modèles de huit milliards de paramètres)** : le critère ultime externe est le franchissement d'une épreuve préenregistrée sur une famille de sabotage jamais vue (mesure de rappel à 1 % de faux positifs, ou réduction prouvée de la corruptibilité sous attaque, ou validation d'un nouveau banc exécutable flou-à-la-relecture) battant les bases déjà établies, avec réplication par une lignée de modèles et un auditeur indépendants.
4. **Le test d'aveuglement et de confrontation multi-modèles (collisionneur épistémique avec bras témoin neutre)** : la confrontation indépendante d'espèces d'architectures distinctes vérifie si les mécanismes et priorités survivent à la critique adverse croisée sans avoir été soufflés dans la question de départ.

---

## Demande reformulée pour le protocole X, le collisionneur et l'organisme

> **Objectif.** Concevoir l'architecture et le programme priorisé des améliorations de l'organisme d'idéation qui maximisent la probabilité de produire des objets mathématiques nouveaux, des concepts rigoureux et des protocoles expérimentaux directement exploitables et décisifs pour le programme de contrôle boîte blanche des menaces diffuses — tout en garantissant mathématiquement et empiriquement que la boucle de rétroaction entre l'organisme et le programme de contrôle reste étanche au sur-ajustement adaptatif, à la circularité des juges et à la spécialisation stérile sur des mondes incomplets.
>
> **Exigences analytiques et formelles.**
> 1. **Architecture des flux de la boucle fermée.** Modéliser distinctement les trois sens de couplage (Organisme → Instruments et bancs de contrôle ; Corpus et échecs du contrôle → Orientation de l'organisme ; Organisme → Modes de sabotage en quarantaine) et fixer les invariants qui interdisent tout retour du score des moniteurs ou des juges de contrôle dans l'entraînement ou la sélection de l'organisme.
> 2. **Modélisation mathématique.** Établir (a) l'équation de rendement de découverte exploitable en fonction du taux de base, de la sensibilité et du taux de fausses alertes du filtre sur mondes plantés face au coût d'épreuve sur cartes graphiques ; (b) la borne de contamination par sélection répétée sur banc partagé et la preuve de son annulation par cloisonnement strict en trois ensembles disjoints (familles d'entraînement de l'organisme, familles tenues à l'écart à lecture unique, familles de validation finale à générateur distinct) ; (c) le théorème de rendement décroissant lorsque la couverture des mondes plantés manque une fraction des classes d'invariants réels, avec borne d'effort optimal au-delà de laquelle optimiser sur les mondes plantés dégrade la généralisation.
> 3. **Objets de contrôle « doit mourir ».** Spécifier au moins trois mécanismes ou bancs artificiels défectueux (filtre à sensibilité nulle, sélection circulaire sur verdict du juge, mondes plantés à couverture nulle des invariants cibles) qui doivent obligatoirement être rejetés par l'architecture proposée.
> 4. **Classement multicritère et sensibilité.** Évaluer chaque levier candidat selon la formule `score = (gain_informatif × facilité × portée × potentiel_de_découverte_majeure) / coût`, en vérifiant par calcul reproductible la stabilité du haut et du bas du classement sous perturbation bilatérale des poids, et en intégrant dès le court terme des épreuves de réfutation en quelques jours sur processeur à coût quasi nul.
> 5. **Protocole de validation externe.** Définir pour chaque levier prioritaire l'expérience décisive en duel d'hypothèses exclusives `H_A` contre `H_B`, son contrôle négatif, ses seuils préenregistrés, son coût matériel minimal et ce qui réfuterait son utilité pour le programme de contrôle.
