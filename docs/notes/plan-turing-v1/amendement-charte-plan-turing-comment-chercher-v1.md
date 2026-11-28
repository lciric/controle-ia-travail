# Amendement de la charte du plan Turing : « Comment chercher les nouvelles idées » — v1

- **Nature.** Pièce de travail (classe C). Section à ajouter à la charte du plan Turing (`docs/notes/plan-turing-v1/plan-turing-directeur-v1.md`, `69c8deae…`), sans en réécrire une ligne. Forme proposée, selon la règle des versions (on n'écrase jamais) : une charte v2 qui reprend la v1 à l'octet et lui ajoute ce texte comme § 3 ; la mère tranche la forme.
- **Décision qui la commande.** Mot de Lazar du 24 novembre vers 17:00Z (accord sur la note de l'attelage, GO-2026-11-24-38) : « go recos fable y compris 7, je veux qu'on sache comment chercher les nouvelles idées ». Nœuds de l'attelage retenus : 1 (a), 2 (a), 3 (a), 4 (b), 5 (a), 6 attendre l'étape 7, 7 oui, 8 plus tard.
- **Source unique du fond.** La note de Fable en effort maximal sur l'attelage du plan Turing (`docs/notes/attelage-plan-turing-v1/attelage-plan-turing-organisme-fable-max-v1.md`, `5aa73e46…`), citée « note, § x » ; les décisions du 22 novembre sur ce que « forcer » veut dire (`docs/notes/demandes-fable-api-2026-11-22-v1/synthese-protocole-x-puits-etroits-v2.md`, `6112172f…`, § 9 ; GO-2026-11-22-74). Ajoutées à la demande de la mère, lues sur la branche `idees/questions-directeur-2026-11-24-v1` au commit `ee6b868c7` (demande de fusion n° 97, non fusionnée), dossier `docs/notes/questions-directeur-2026-11-24-v1/` : réponse à la question 5, amendements A1 à A6 (`reponse-q5-carbon-fable-et-plan-turing-v1.md`, `0bdc9810…`) ; errata 1 des questions 5 (`7bcaec6f…`) et 9 (`c4a93d16…`) ; erratum transversal sur κ et l'hypergraphe (`72afe693…`) ; errata mineurs des questions 1, 2 et 7 (`fcac74f5…`). Rien n'est ajouté au-delà de ces pièces.
- **Auteur.** Opus 5.5, sous-agent de la mère, 24 novembre 2026. Rédaction de forme sur un cadre écrit par Fable ; aucun critère neuf. Réserve de lignée : la note source est de la famille de plusieurs proposeurs de l'organisme ; elle reste à contre-lire par une autre famille avant d'en tirer une pièce décisive (note, en-tête).

---

## § 3 — Comment chercher les nouvelles idées

### 3.0 En une phrase

Avant de produire, savoir mesurer sans juge-modèle trois choses : **où** sont les puits (un sélecteur de lieux, éprouvé comme une prévision), si on les **trouve** mieux que le hasard (probabilité de découverte selon l'étroitesse, à coût facturé égal), et si on les **reconnaît** (survie de puits glissés dans le flux) (note, § 3.0, point 1).

La charte v1 disait où chercher et comment juger ; elle ne disait ni la cible, ni le hasard de référence, et son banc des verrous plante des mondes dont la solution de référence est publiée : il mesure le rappel du bon outil, non la découverte d'un puits (note, § 3.0, points 3 et 4, et correction (b)). Cette section comble ces trois manques.

### 3.1 La cible, posée avant tout instrument

**Trois objets figés par empreinte avant toute mesure** (note, § 3.1) :
1. **l'espace** : une grammaire publique d'engagements résolubles (loi chiffrée, fonction à signature imposée, énoncé fini, prévision) ; deux engagements sont la même idée s'ils ont la même signature de prédiction sur une grille publique de sondes ;
2. **le chercheur de référence** : le meilleur modèle seul, consigne de référence, vue nue, une session neuve par appel ; il définit « étroit » ; il est figé par cycle et nommé dans tout résultat ;
3. **le prédicteur de référence** : ce que le savoir admis prédit déjà (sur monde planté, la loi exacte sachant l'archive des lois connues ; sur corpus, le modèle de surface ajusté avant la date de gel) ; il définit « profond ».

**Puits étroit et profond** : une classe d'engagements (i) résolue vraie par un résolveur qui n'est pas un agent ; (ii) étroite : le chercheur de référence, au budget facturé de l'épreuve, la trouve avec une probabilité sous un seuil gelé ; (iii) profonde : portée réalisée (surprise retirée ailleurs) au-dessus d'un seuil gelé. La **viabilité** (la serrure tient) est exigée comme garde : l'étroit sans serrure est du bruit. Les seuils proposés par la note (0,2 ; quatre bassins sur huit ou domaine masqué prédit) sont des propositions à geler au préenregistrement, non des valeurs décidées (note, § 3.1, Définitions).

**Trois grandeurs d'« étroit », à ne pas confondre.** (a) *L'étroitesse d'accès* : moins le logarithme de la probabilité qu'un appel du chercheur de référence produise l'idée. (b) *L'étroitesse de serrure*, ou son contraire la *largeur locale* : la part des correspondances voisines (une ou deux paires changées) qui gardent le score à une tolérance fixée. (c) *La rareté au hasard* : la part des bonnes correspondances dans tout l'espace, sous un tirage uniforme. Le jouet de l'exposé sur le graphe méta-mathématique montre qu'elles divergent : sur les 36 correspondances à une paire près, 16 gardent le score à un huitième près (puits *localement large*), alors que seules 768 bijections sur 362 880 sont aussi bonnes (*rareté au hasard* de 2,1 × 10⁻³). La phrase « le puits est étroit » de cet exposé est retirée (erratum 1 de la question 9). La définition (ii) de la cible n'emploie que (a) ; (b) est une coordonnée mesurée de la cible ; (c) dit seulement la difficulté d'un tirage aveugle (note, § 3.1, tableau des coordonnées).

**Notation fixée.** Viabilité : `K_r = max_φ [c(φ) − κ(φ)]`, `Z_r` son écart centré et réduit sous recâblage à degrés et types constants ; c est la couverture ; **κ ne désigne que la part des conflits** ; le score de Carbon s'écrit `K_C = max c_C·exp(−γ_C χ_C)`, jamais avec κ (erratum transversal, § 1).

**Découverte à fort impact pour le programme** : un puits étroit et profond situé sur la carte des verrous du contrôle, qui bat le plancher des méthodes connues sur des familles de verrous où il n'a pas été conçu, puis devient une épreuve, une sonde ou une cible de preuve (note, § 3.1).

**Deux comptes toujours séparés** : *profond* (ce que l'idée vaut, même si le modèle seul la trouve) et *profond et étroit* (l'apport propre de l'attelage). **Deux natures** : *transfert* (le parent existe dans une bibliothèque lointaine) et *création* (hors de l'alphabet des relations). **Décision (nœud 1, a)** : le premier chiffre porte sur les transferts ; les créations viennent ensuite (note, § 3.1 et § 4.5).

### 3.2 Premier niveau : ce que l'organisme fait

**Un noyau minimal gelé avant mesure**, et non l'orchestrateur complet, dont la boucle n'a jamais tourné avec de vrais agents (note, § 3.6) :
- un **cartographe**, qui est un programme : il sert des cartes de problème typées, figées par empreinte, avec la pièce lointaine choisie par un moyen indépendant du goût du modèle (criblage par la serrure, ou énumération) ;
- des **proposeurs** indépendants, sans vue des autres ni d'aucune note, qui écrivent dans la langue du résolveur, et **deux espèces sans modèle** : l'énumérateur par longueur de description et le tirage uniforme dans la grammaire ;
- des **réfutateurs** d'une autre lignée, avec le droit d'exécuter ;
- des **résolveurs qui ne sont pas des agents** (banc noteur, noyau de preuve, juge statistique au nul formé des lois connues) : eux seuls rendent des verdicts ;
- un **registre et une bibliothèque écrits par programme** : un modèle peut proposer une abstraction, seul le réemploi mesuré l'admet ;
- un **répartiteur** : éliminations successives sur les issues résolues, choix de la source par masse manquante, **part uniforme garantie** (proposition de la note : un dixième à un cinquième du budget), probabilités de chaque choix journalisées.

**La recherche se fait à deux niveaux** (note, § 3.3, « Correspondances plantées ») : choisir le lieu (quelle paire, quel verrou, quelle anomalie), puis, dans le lieu, trouver la correspondance entre les deux voisinages, problème d'affectation dont le paysage a précisément des puits étroits.

**Les opérateurs** (transfert par serrure, explication d'une anomalie, scission, compression entre bassins, libre) sont des bras à rendement mesuré, chacun avec son bras hasard ; aucun n'est un principe (note, § 3.6).

**La part mécanique du budget, seule garantie** (décisions du 22 novembre, synthèse, § 1 et § 9) :
- **D1** : « forcer » veut dire, dans toute revendication, une garantie de pire cas dans la grammaire publique, à prix affiché ; un gain moyen sous un a priori n'est qu'une mesure ;
- **D2** : un bras sans modèle de langage (énumérateur ordonné par longueur, valeurs e pondérées par la longueur) est le premier essai et la base obligatoire de toute méthode ; réserve de Neon gardée : « garantie complète » seulement une fois prouvée la validité sous le nul composite de l'organisme ;
- **D3** : diagnostics bon marché au premier étage (collisions, autocorrélation, audit formel de la grammaire ; puis, sur budget pilote compté, audit du juge et masse non vue) ;
- **D4** : le juge statistique ne guide jamais la recherche en course ; au banc, seulement sur des tirages d'exploration à part, comptés au budget (appui, Dwork et al. 2015 : à vérifier sur PDF) ;
- **D5** : vérification sur PDF avant tout usage dans une pièce décisive.

La part ε donnée au tirage mécanique assure à chaque classe une probabilité d'au moins ε fois sa masse sous ce tirage, quel que soit le modèle. Prix : la force brute diluée par ε, rien hors de la grammaire, et la proposition seulement, non la reconnaissance (note, § 3.1, « Le hasard » ; synthèse, § 8). Tout le reste est un pari sur une structure, à mesurer.

**Ce qui pousse réellement vers l'étroit, par ordre de solidité** (note, § 3.6, chiffres rapportés d'une seule étude chacun) : (1) la part mécanique ; (2) la pièce lointaine servie avec un indice ; (3) les décisions d'exploration sorties du modèle ; (4) ne rien perdre des idées proposées ; (5) le sélecteur de lieux, qui n'est encore qu'un pari.

### 3.3 Second niveau : ce que l'attelage mesure et impose

**Trois hasards, exécutés et non seulement calculés**, dans la même grammaire et notés par le même oracle (note, § 3.1) : le tirage uniforme ; l'énumérateur mécanique par longueur ; le chercheur de référence tiré N fois à coût facturé égal (« le meilleur modèle seul »). S'y ajoutent une boucle simple qui réinjecte le meilleur, et un attelage placebo (mêmes rouages, cartes leurres ou bibliothèque sans rapport).

**Le test.** Grandeur principale, par famille de mondes (l'unité statistique) : part des puits étroits et profonds plantés retrouvés dans le budget facturé, moins la même part pour le chercheur de référence, mêmes mondes, mêmes graines. La strate étroite est fixée avant la course par les boutons du générateur et par un étalonnage du chercheur de référence sur des mondes **disjoints**. Décision : une marge d'utilité fixée d'avance par Lazar, un intervalle entièrement d'un côté, sinon « non jugeable » ; garde conjointe sur les fausses promotions (mondes où toute promotion est fausse, tricheurs scellés). Est « mieux que le hasard et que le meilleur modèle seul à coût facturé égal » ce qui passe ce test contre les trois hasards (note, § 3.1, « Grandeur principale », « Règle de décision » ; comparateurs, § 3.5).

**Les sept comparateurs** à coût facturé égal (note, § 3.5) : tirage uniforme ; énumérateur ; chercheur de référence tiré N fois ; boucle simple ; même effectif sans échange ; attelage placebo ; verdicts permutés rendus à l'organisme (Gupta, Hartford et Liu : à vérifier sur PDF).

**Les huit épreuves de l'instrument, avant le premier appel payant** (note, § 3.5) : diagnostics bon marché ; tests de mort de chaque monde (dont le devin de la forme sous son plafond) ; tests de mort du banc ; validation de la mesure de profondeur contre la portée plantée ; validation de la mesure d'étroitesse contre les boutons ; répétition générale de la chaîne par des proposeurs scriptés ; audit du résolveur dans la queue (taux de fausse acceptation très inférieur à la fréquence des puits) ; plancher de bruit entre deux courses du même bras.

**Les sources de vérité** (note, § 3.3) :

| Source | Ce qu'elle tranche | Règle |
|---|---|---|
| graine d'un monde planté | la découverte d'une loi cachée | mondes à puits (boutons de portée, de longueur sachant la bibliothèque, de trace d'ordre inférieur, de chaîne, de ressemblance, de confinement, de piège, de filles), leurres obligatoires, plan deux sur deux mémoire contre compétence |
| valeur optimale calculable d'un verrou ouvert | la qualité d'une règle sans connaître la bonne | optimum exact sur petits paramètres, règle notée sur des tailles non servies ; noyau « réellement ouvert » à vérifier sur PDF, verrou par verrou |
| passé daté | un sélecteur de lieux | trois régimes à ne pas mélanger : long sans modèle de langage (valide mesures et sélecteurs, rien de l'organisme) ; court, après la coupure d'un modèle ; prospectif. Événement désigné par règle fixée avant lecture, ensemble à risque avec paires jamais nées |
| noyau d'un assistant de preuve | la vérité d'un énoncé fini | portée par ablation à budget égal ; **décision (nœud 6)** : pas de cibles finies de preuve dans l'attelage avant l'étape 7 |
| futur | l'information sur l'avenir | registre prospectif scellé |

Cinq leçons de la rétrodiction réfutée s'imposent à toute épreuve sur le passé : unité = paire ou lieu avec effets fixes par champ ; cible = événement daté ; corpus = échantillon stratifié complet par année ; signal relationnel, en différence dans le champ ; bases toujours rapportées (note, § 3.3).

**Le banc des correspondances plantées est inscrit à la charte (nœud 7)** (note, § 3.3, « Correspondances plantées ») : mondes à correspondance vraie isolée près d'un leurre large de même masse, à relation correspondant à une chaîne de deux, à leurre de popularité ; bras sans modèle (énumération, programme exact en nombres entiers), signatures de rôle, transport régularisé, appariement du grossier au fin, recuit, proposeurs ; mesure : correspondances retrouvées et coût, selon l'étroitesse de serrure plantée. Aucun de ces bras ne se dira « forcer ». La relation qui correspond à une chaîne de deux se représente dans l'**hypergraphe fusionné** du dossier des questions du 24 : ni celui de Carbon (qui n'écrit nulle part « hypergraphe ») ni celui de Fable, mais un hypergraphe orienté dont chaque hyperarc va d'un ensemble de prémisses à une conclusion, avec le cœur de Fable et la couche typée de Carbon (réponse à la question 7, § 5 ; erratum transversal, § 2) ; la fusion est une recommandation de ce dossier, à reprendre dans la conception de l'étape 1.

**Qui écrit les mondes.** Le générateur par graine pour les mondes de conception ; **décision (nœud 4, b)** : les familles tenues à l'écart sont écrites par une instance aveugle d'Opus, aveugle aux cartes et aux candidats ; la banque de confirmation finale vient d'un générateur distinct (note, § 3.3, « Qui écrit »). Réserve à consigner : la note recommandait une autre famille ; Opus n'en est pas une par rapport à Fable et à plusieurs proposeurs. La parade qui reste est celle du tableau des risques (générateur mécanique ; auteurs aveugles) (note, § 4.4).

**La portée plantée dans l'oracle** — **décision (nœud 2, a)** : elle entre dans l'oracle qui juge une composition, sur les seuls mondes plantés ; c'est une lecture de la règle du choix des compositions sur l'oracle et le coût (N-058), non un juge (note, § 4.5).

**Le retour par étages** (note, § 3.6) : riche sur les mondes de conception et semi-synthétiques ; borné à un choix dans une liste déclarée sur les familles de validation écrites à l'aveugle ; **rien** sur les familles tenues à l'écart (lecture unique) et sur les épreuves réelles. Ne remonte jamais : un score de moniteur ; une portée estimée par un lecteur, comme récompense ; un verdict de juge dans le choix d'une composition ; les taux d'identification de l'oracle par strate ; une consigne réécrite après lecture d'un résultat. La forme stricte pour le tenu à l'écart et le réel est la décision de Lazar (R-5294) ; le retour par étages ailleurs est appliqué par la mère (R-5316) et reste à confirmer par Lazar.

**Le registre prospectif scellé, interne** — **décision (nœud 5, a)** : ouvert dès le 7 décembre, non public ; prévisions de l'instrument puis de l'organisme à trois, six et douze mois (note, § 4.1, étape 6).

### 3.4 Les sélecteurs de lieux

Un sélecteur classe des lieux avec la seule information disponible avant la recherche ; il s'éprouve comme une prévision, contre un tirage au hasard dans le même vivier et contre les bases simples (volume, ancienneté, attachement préférentiel, répartition des experts) (note, § 3.2).

**Gardés (sept)** : (1) interaction de la surprise et de la serrure, premier rang, préenregistrement à réécrire avec une spline de distance et une permutation des signes ; (2) cortège et trous d'une correspondance, premier rang ; (3) couche des problèmes pondérés, sous garde de mesurabilité ; (4) cadres en croissance, comme covariable ; (5) résidus du prédicteur de référence ; (6) masse manquante par source, pour l'allocation ; (7) liste des paires non croisées par l'archive et plan des focalisations, qui pose l'inconnue centrale : la vue déplace-t-elle la loi des propositions ?

**En attente (cinq)** : compression sur plusieurs bassins (après l'audit de réemploi) ; scission d'une fausse identité (après un préenregistrement) ; inflation descriptive et entropie des notations (monde de signaux plantés d'abord) ; marchepieds et frontière de l'archive ; cinétique des collisions en température (étape 7, mesure de l'organisme et non sélecteur).

**Morts, rangés ou hors de la v1** : le **détecteur lexical de tensions est mort** (rétrodiction réfutée : aire 0,17, corrélation de rang −0,63) ; ce qui le remplace doit être relationnel, daté, comparé à un nul. La fenêtre fixe de distance est morte comme règle. Les détecteurs sémantiques de signaux précurseurs par modèle de langage sont **prospectifs seulement** (fuite du futur en rétrospectif). Transition de phase et ensemble autocatalytique : rangés. Signal interne de surprise et plasticité : hors de la v1 (note, § 3.2, lignes 8 à 16 ; § 3.7).

### 3.5 Ordre et dates

Du moins cher au plus cher (note, § 4.1) ; aucune épreuve avant son texte scellé, simulation comprise.

| Étape | Quoi | Dates |
|---|---|---|
| 0 | préparatifs sans Fable : faits de données, plomberie du banc, audit du goulot, lecture sur PDF des voisins, dépouillement du remue-méninges des 2 et 3 novembre | 25 novembre au 1er décembre |
| 1 | **conception de l'instrument de la cible et des deux familles de mondes** (Fable, effort maximal, un seul texte) | **2 au 4 décembre** ; contre-lecture et scellement jusqu'au 7 |
| 2 | code, validation de l'instrument, tests de mort, courbe du hasard et de l'énumérateur, banc des correspondances plantées en bras sans modèle (0 dollar) | 7 au 11 décembre |
| 3 | préenregistrement et devis de l'apport propre à coût égal | 9 au 14 décembre |
| 4 | première course payante, sur devis | 15 au 19 décembre au plus tôt |
| 5 et 5 bis | sélecteurs en rétrodiction longue sans modèle de langage ; épreuves datées secondes | décembre ; janvier |
| 6 | registre prospectif scellé | dès le 7 décembre |
| 7 à 9 | verrous ouverts, opérateurs, cinétique ; transfert vers une épreuve réelle ; détecteurs sémantiques prospectifs | janvier ; janvier-février ; pas avant février |

**Décision (nœud 3, a)** : un seul socle, celui de l'attelage ; la course d'auto-conception reprend après le premier chiffre. Chemin minimal viable sans dépense : étapes 0 (b), 1 et 2, vers le 10-12 décembre ; le premier chiffre payant glisse en janvier si la porte de fin décembre prend le quota de Fable (note, § 4.2). **Nœud 8** (lecteur habilité, accès payant aux sources d'arXiv en masse) : plus tard.

### 3.6 Arrêts et limites

Les critères d'arrêt de la note (§ 4.3 : banc mort, instrument invalide, notion à refaire, résolveur inapte à la queue, architecture rangée, sélecteur écarté) et ses limites (§ 3.8) valent tels quels ; jamais d'arrêt sur un résultat négatif en soi ; une panne technique n'est pas un résultat.

### 3.7 Les amendements A1 à A6 proposés le 24 (réponse à la question 5), confrontés à la note de Fable

La réponse à la question 5 propose six amendements au plan Turing (§ 8) ; son erratum 1 corrige une sévérité inégale envers Carbon et Fable (règle de symétrie) sans changer les amendements. Lecture, pour chacun :

| | Amendement | Rapport à la note de Fable | Sort |
|---|---|---|---|
| A1 | section « comment chercher » à deux niveaux, renvoyant aux décisions D1 à D5, base sans modèle obligatoire | **concorde** ; la note le reprend (§ 3.0, dernier point ; § 4.5, nœud 7) et **l'élargit** : cible, trois hasards, test à coût facturé égal, sources de vérité, retour par étages | décidé (nœud 7) ; c'est la présente section |
| A2 | banc des correspondances plantées, au Pas 1 avec les mondes plantés, **au Pas 0 si le créneau processeur le permet** | **concorde sur le fond** (mêmes mondes, mêmes bras, même mesure : note, § 3.3) ; **diffère sur la date** : la note le place à l'étape 2 (7 au 11 décembre), après le texte de conception scellé de l'étape 1, et permet de le faire passer après les mondes à puits s'il faut couper (§ 4.2). L'option « au Pas 0 » précéderait un texte scellé : elle n'est pas reprise | inscrit (§ 3.3 ci-dessus), à la date de la note |
| A3 | dans l'épreuve du pont sur PubTator 3, avant scellement : spline de distance dans le modèle des naissances, permutation des signes à côté de celle des types | **concorde** mot pour mot (note, § 3.2, ligne 1) ; **diffère sur le support** : A3 amende le brouillon ; la note le juge non scellable et le fait réécrire par Fable après les faits de données de l'étape 0, A3 compris | dans le texte réécrit, étape 5 |
| A4 | « les cinq signaux localisent les objets nouveaux » est l'énoncé d'un seul modèle, réfuté sous forme lexicale ; toute version relationnelle passe d'abord par un monde de signaux plantés | **concorde** (note, § 3.2, lignes 10, 12 et 14 ; § 3.3, « Signaux plantés ») ; la note **ajoute** : les détecteurs sémantiques ne se valident qu'en prospectif | inscrit (§ 3.4 ci-dessus) |
| A5 | errata de provenance dans les pièces qui citent Carbon (Bettencourt 2009 et non 2008 ; jumeaux de Bikard « à vérifier » ; Galison non « démontré », sans dire pour autant que Fable a raison, selon l'erratum 1) | **hors du champ** de la note, qui ne le contredit pas ; l'inventaire le porte aussi | hors de la charte : errata au registre, par la mère |
| A6 | volet 4 : les chiffres du bilan de Carbon sont des illustrations, jamais opposables | **non traité** par la note ; conforme à sa règle « aucun chiffre sans source » (partie 2) | renvoi de lecture au volet 4 (§ 3.8) |

**Un écart à trancher par l'ordre décidé.** La même réponse range parmi « ce qui ne doit pas changer » l'épreuve du pont « en tête ». La note la place à l'étape 5, après l'instrument ; Lazar ayant suivi les recommandations de Fable (GO-2026-11-24-38), l'ordre de la note prévaut : l'épreuve du pont reste le premier des sélecteurs, non la première épreuve.

### 3.8 Renvois de lecture pour les volets de la v1 (sans les réécrire)

- **Volet 1** : la « rétrodiction 7 sur 8 » de la cartographie est un rappel sur huit transitions choisies, sans négatifs, sans taux de base ni base concurrente (`temoins-externes-et-protocole-v1.md`, § 4) ; la cartographie vaut catalogue d'énoncés, à revérifier avant service (note, § 3.0, correction (a)).
- **Volet 3** : le rang 1 du Pas 0 est réfuté ; le préenregistrement sur la base ouverte de relations biomédicales PubTator 3 est non scellable (six bloquants), à réécrire par Fable après les faits de données de l'étape 0 (note, § 3.0, « État des lieux »).
- **Volet 4** : le banc des verrous mesure le rappel ; il est complété par les mondes à puits et les correspondances plantées (§ 3.3 ci-dessus).

**Références à vérifier sur PDF avant tout usage décisif** : Dwork et al. 2015 ; Gupta, Hartford et Liu (arXiv 2509.21403) ; les bancs voisins de découverte de lois et de prévision de percées listés en annexe de la note ; Hesterberg 1995 est confirmé en partie (synthèse, § 6).

---

Fin de rédaction : 2026-11-24 (heure en pied du message de remise).
