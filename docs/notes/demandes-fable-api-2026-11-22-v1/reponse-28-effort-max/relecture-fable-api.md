# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHuLffeUcqjbDLMuWCyC`
- Heure (UTC) : 2026-11-22T11:49:27Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 106000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-28-idees-originales-puits-profonds-v1.md` — sha256 f552f514961f78bed9b5ab4153fb4206c252bfb38f9ca542b545c03f339898e9 (compagnon : vérifié)
  - remarques : `docs/notes/organisme-bassins-etroits-v1/recoupement-methodes-v1.md` — sha256 eecd98fab0beff8c99414380a5d12b18feafd1581d38c7fe54b94491327ab172 (compagnon : vérifié)
- Empreinte de l'invite envoyée : df1cd04332cdad28f484c1e66e30320f6faa73482f867255554adefd70fc278f
- Jetons : entrée 15886, sortie 61679 (dont réflexion 53099), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 2.594248 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 28 — idées originales : réponse par la méthode « demande approfondie »

**Conventions.** Chaque affirmation est marquée FAIT RAPPORTÉ, HYPOTHÈSE ou PROPOSITION, à l'échelle de la phrase ou du paragraphe. Toute antériorité a le statut « rapporté, non vérifié sur PDF » (fichier de l'article non relu). La certitude indiquée (élevée, moyenne) porte sur l'existence de la référence et le sens de son résultat. Aucun chiffre publié n'est repris. Seuls des auteurs d'antériorités sont nommés, comme la consigne l'exige. Les titres sont cités tels quels : leurs sigles désignent les grands modèles de langue (LLM), le traitement automatique des langues (NLP) et l'intelligence artificielle (AI).

## A. Les quatre points préalables

**1. Ce qu'un expert ferait et qui n'est pas demandé** (PROPOSITIONS, sauf mention).

- Vérifier que le défaut existe, et à quel étage. FAIT RAPPORTÉ (recoupement, section 9) : on ignore si, dans les courses passées, les idées étroites n'ont pas été proposées ou l'ont été puis perdues. Les trois leviers (vue, proposeurs, ne pas perdre) en dépendent.
- Mesurer la loi spontanée des proposeurs : courbe rang-fréquence des classes d'idées, masse jamais vue, recouvrement entre familles. HYPOTHÈSE : des familles différentes partagent les mêmes bassins, si bien qu'ajouter une famille élargit peu le support (indice : Wenger et Kenett, 2025, *We're Different, We're the Same: Creative Homogeneity Across LLMs*, certitude moyenne).
- Retourner la métaphore. Un puits n'est étroit que sous une mesure : plutôt que tirer plus fort, chercher le proposeur, la représentation ou le domaine d'origine sous lequel il est large.
- Refuser le scalaire « originalité ». Rareté, justesse et fécondité sont trois grandeurs. HYPOTHÈSE (dénombrement) : la plupart des idées rares sont fausses, donc forcer la rareté abaisse la précision, et le goulot réel est le coût de vérification par candidat. Les usages diffèrent : mécanismes de contrôle et modes d'attaque s'éprouvent sur mondes plantés, les questions de recherche n'ont pas de vérificateur bon marché.
- Exiger de chaque méthode qu'elle nomme la structure, connaissable sans l'oracle, qu'elle exploite (parent détectable, anomalie dans des données, idée commune ailleurs, retour d'un vérificateur exact). L'éprouver aussi là où cette structure manque : elle doit alors échouer.
- Poser la validité externe (retrouver une interaction plantée ne prouve pas qu'on trouve des questions fécondes) et écrire le contrôle des erreurs d'une génération à l'autre, absent selon le recoupement.

**2. Données brutes de départ** (PROPOSITION). Non les archives retenues ni les synthèses de tours, mais :

- toutes les propositions brutes des courses passées, y compris refusées par le gardien ou fusionnées comme doublons, avec proposeur, vue servie et coût en jetons ;
- les tirages du juge, issue par issue ;
- les spécifications des mondes plantés ;
- des tirages frais et indépendants de chaque proposeur sous la vue ordinaire ;
- pour le monde réel, des textes datés complets, non des résumés plongés.

**3. Méthodes et outils** (PROPOSITION, détail en C3). Statistique des espèces pour la masse non vue. Événement « couvre la composante plantée » défini par l'oracle. Échantillonnage préférentiel et simulation d'événements rares comme cadre de calcul. Valeurs e séquentielles avec contrôle en ligne des fausses découvertes. Énumérateur mécanique de la grammaire, comme base et comme garde. Plans appariés par monde, préenregistrés.

**4. Vérification hors du directeur et du modèle qui répond** (PROPOSITION).

- La vérité plantée, clé scellée par une empreinte cryptographique publiée avant la course.
- Un oracle rejouable par un tiers et des critères de réfutation horodatés.
- Une réplication indépendante sur des graines neuves.
- Pour les idées réelles, une recherche d'antériorité confiée à un tiers et un jury d'experts aveugle à la source, étalonné par des leurres (idées banales et idées déjà publiées glissées dans le lot).
- Le temps : des prédictions scellées que l'expérience tranche.

## B. Demande reformulée

« À partir des journaux bruts et d'un banc de mondes à puits plantés dont la clé est scellée :
(a) établir à quel étage les idées étroites se perdent ;
(b) mesurer la loi spontanée des proposeurs et sa masse non vue ;
(c) définir rareté, justesse et fécondité par des fréquences, un oracle ou des tirages frais, sans juge de nouveauté ;
(d) pour chaque famille de méthodes, dire la structure exploitée, ce qui est garanti et l'antériorité la plus forte, puis la comparer, à budget de jetons égal, à trois bases nommées, sur des mondes où la structure est présente puis absente, avec un critère de réfutation écrit d'avance ;
(e) dire ce qui établirait le transfert hors des mondes plantés. »

## C. Réponse

### 1. Grandeurs mesurables (PROPOSITION)

Pour une classe d'idées c :

- **Largeur** w(c | proposeur, vue) : probabilité qu'un appel produise c, estimée par fréquence sur N appels frais. FAIT RAPPORTÉ (calcul élémentaire) : une classe jamais vue en N tirages a, avec une confiance de 95 %, une probabilité inférieure à environ 3/N. L'étroitesse n'est certifiable qu'à cette résolution. Le seuil « étroit » se fixe sur des mondes d'étalonnage, jamais là où le témoin a échoué.
- **Étroitesse dans les données** : masse r de la région où l'effet vit, distincte de la largeur (recoupement, section 1).
- **Profondeur** : gain moyen de log-vraisemblance par tirage frais contre la meilleure loi du nul, de l'ordre de r·Δ. Un puits n'est un objet d'épreuve que si n·r·Δ dépasse le seuil de détection (borne 5). Sinon on teste le budget du juge, pas l'organisme.
- **Justesse** : survie aux tirages frais sous contrôle de multiplicité ; sur monde planté, accord avec l'oracle.
- **Fécondité** : écart de rendement de la génération suivante avec et sans c dans l'archive (ablation) ; à défaut, nombre de descendants retenus.
- **Grandeur visée** : nombre de classes à la fois étroites, profondes et retenues par million de jetons, avec la précision dans la zone rare.

Sur le banc, l'appartenance à c est décidée par l'oracle, ce qui contourne la borne 13. En course réelle on ne mesure que des groupes de doublons, limite à écrire. La distance à un corpus ne sert que de filtre de copie, en distance fonctionnelle, jamais de score. Aucun modèle ne note la nouveauté.

### 2. Familles de méthodes

Les « garantit / ne garantit pas » sont des HYPOTHÈSES d'analyse. Les résultats cités sont des FAITS RAPPORTÉS, au statut dit en tête.

1. **Qualité et diversité.**
   - Garantit : une case de descripteur occupée le reste, les pierres de gué sont conservées.
   - Ne garantit pas que les cases correspondent aux bassins ; le descripteur est choisi à la main.
   - Pour : Lehman et Stanley, 2011, *Abandoning Objectives: Evolution Through the Search for Novelty Alone* (élevée) ; Mouret et Clune, 2015, *Illuminating search spaces by mapping elites* (élevée).
   - Ici : structurer l'archive servie, non récompenser.

2. **Échantillonnage contre la vraisemblance.**
   - Garantit un changement des formes, rien sur les idées.
   - Contre : Peeperkorn et collaborateurs, 2024, *Is Temperature the Creativity Parameter of Large Language Models?* (moyenne) : lien faible avec la nouveauté, davantage d'incohérence.
   - Contre : Si, Yang et Hashimoto, 2024, *Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers* (élevée) : les doublons dominent quand on multiplie les tirages.
   - Pour : Meincke, Mollick et Terwiesch, 2024, *Prompting Diverse Ideas: Increasing AI Idea Variance* (moyenne).
   - Pour, chez l'humain : Beaty et Silvia, 2012, *Why do ideas get more creative across time? An executive interpretation of the serial order effect in divergent thinking tasks* (élevée) : les idées tardives d'une liste sont plus originales (transfert aux modèles : HYPOTHÈSE).

3. **Cibles d'expert et vérificateur exact.**
   - Garantit la justesse de ce qui est gardé, donc le droit de tirer massivement.
   - Ne garantit pas que la cible soit profonde ni atteignable.
   - Pour, indice le plus fort que je connaisse : Romera-Paredes et collaborateurs, 2023, *Mathematical discoveries from program search with large language models* (élevée) ; Novikov et collaborateurs, 2025, *AlphaEvolve: A coding agent for scientific and algorithmic discovery* (élevée).
   - Portée déclarée de ces travaux, non lacune du champ : problèmes à score exact et bon marché.

4. **Adversaire qui prédit le banal et le retire.**
   - Garantit le retrait des classes prédites, si l'équivalence est décidable.
   - Ne garantit pas que le reste soit juste, et pousse hors du nul.
   - Pour : Sourati et Evans, 2023, *Accelerating science with human-aware artificial intelligence* (moyenne).
   - Contre la forme naïve : Burda et collaborateurs, 2019, *Large-Scale Study of Curiosity-Driven Learning* (élevée) : récompenser l'erreur de prédiction attire vers le bruit.

5. **Recombinaison contrainte.**
   - Garantit la couverture des affectations, non des idées (borne 11).
   - Pour : Uzzi et collaborateurs, 2013, *Atypical Combinations and Scientific Impact* (élevée) : fond conventionnel plus une combinaison atypique.
   - Pour : Fleming, 2001, *Recombinant Uncertainty in Technological Search* (élevée) : moyenne plus basse, variance plus haute.

6. **Abstraction et transfert.**
   - Aucune garantie formelle ; change la mesure : une idée rare ici peut être commune ailleurs.
   - Pour : Hope et collaborateurs, 2017, *Accelerating Innovation Through Analogy Mining* (moyenne).
   - Contre : Gick et Holyoak, 1980, *Analogical Problem Solving* (élevée) : chez l'humain, le transfert spontané est rare sans indice. Pour les modèles, question ouverte.

7. **Curriculum.**
   - Garantit des paliers si une hiérarchie existe, rien devant un puits sans parent (borne 3).
   - Pour : Wang et collaborateurs, 2019, *Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions* (élevée).

8. **Programme à archive complète.**
   - Garantit que rien de proposé n'est perdu et que l'audit est possible.
   - Ne garantit aucune découverte ; l'archive ancre.
   - Pour : Ecoffet et collaborateurs, 2021, *First return, then explore* (élevée).
   - Mise en garde : Si, Hashimoto et Yang, 2025, *The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas* (moyenne) : la note donnée avant exécution ne tient pas après.
   - Mise en garde : Gupta et Pruthi, 2025, *All That Glitters is Not Novel: Plagiarism in AI Generated Research* (moyenne) : nouveauté apparente par emprunt non signalé.

HYPOTHÈSE de synthèse : les succès documentés tiennent à un vérificateur bon marché et à une archive de paliers, non à un mécanisme de nouveauté. Je ne connais pas d'antériorité sur un organisme à juge statistique et nul composite : est-ce une zone vierge ? Question à instruire, non revendication.

### 3. Mathématiques et outils, et où chacun échoue

Usages : PROPOSITIONS. Propriétés et échecs : FAITS RAPPORTÉS (résultats classiques, statut dit en tête).

- **Statistique des espèces** (Good, 1953, *The Population Frequencies of Species and the Estimation of Population Parameters*, élevée) : la masse non vue s'estime par la part des classes vues une seule fois. Échoue si la définition des classes est instable.
- **Échantillonnage préférentiel** : le gain d'une vue ou d'un proposeur vaut au plus le rapport des largeurs p′/p, et ce qu'un bassin gagne est pris aux autres (borne 2).
- **Fractionnement multiniveau** (Cérou et Guyader, 2007, *Adaptive Multilevel Splitting for Rare Event Analysis*, élevée) : exige une fonction de progression. Sans structure, aucune méthode ne domine (Wolpert et Macready, 1997, *No Free Lunch Theorems for Optimization*, élevée). Forme voisine de la barrière de parité : Kearns, 1998, *Efficient Noise-Tolerant Learning from Statistical Queries* (élevée).
- **Théorie de l'information** : la surprise −log p est maximale pour le bruit. La profondeur logique (Bennett, 1988, *Logical Depth and Physical Complexity*, élevée) sépare en principe le profond de l'aléatoire mais n'est pas calculable ; le juge sur tirages frais en tient lieu.
- **Densité dans un espace de plongement** : sensible à la paraphrase, dilue une différence rare. À réserver au dédoublonnage grossier.
- **Processus ponctuels répulsifs** (Kulesza et Taskar, 2012, *Determinantal Point Processes for Machine Learning*, élevée) : diversité des vues, non des sorties.
- **Bandits extrêmes** (Carpentier et Valko, 2014, *Extreme bandits*, moyenne) : le bon objectif (le maximum, non la moyenne), mais ils exigent une récompense. Ici hors ligne seulement, sur mondes d'étalonnage. Même réserve pour la recherche arborescente.
- **Contrôle en ligne des fausses découvertes** (Javanmard et Montanari, 2018, *Online rules for control of false discovery rate and false discovery exceedance*, élevée) : répond au contrôle entre générations. Ne répare pas un nul qui cède devant les copies par morceaux.
- **Vérificateurs formels, solveurs exacts, énumération exhaustive** : certifient l'énoncé, pas son intérêt. L'énumérateur est la base qu'un modèle doit battre.

### 4. Banc d'épreuve (PROPOSITION)

**Mondes**, familles fixées avant tirage, clé scellée :

- (i) puits à parent détectable ;
- (ii) puits sans parent, contrôle négatif où aucun bras ne doit battre nettement l'énumération, sinon soupçon de fuite (je tranche ici un désaccord ouvert du recoupement, à valider) ;
- (iii) puits « transférable », commun sous un autre habillage ;
- (iv) hors structure (trois traits, seuil décentré, effet non monotone) ;
- (v) mondes entièrement dans le nul ;
- (vi) copies hors de la classe du nul ;
- plus une carte additionnelle de contrôle positif.

Largeur étalonnée sur des mondes frères, profondeur au-dessus du seuil de détection.

**Bras**, à budget total de jetons égal : proposeur seul répété ; énumérateur mécanique tirant au hasard ; sélection par nouveauté seule (distance à l'archive sur le jeu public) ; organisme actuel ; organisme plus méthode ; vue placebo.

**Mesures**, par monde, bras appariés : récupération du puits au budget fixé, en trois lectures (propositions brutes, représentants, cartes retenues) ; fausses promotions.

**Taille** : la base propose le puits avec une probabilité voisine de k·w (FAIT RAPPORTÉ, calcul). Le nombre de mondes croît comme l'inverse de l'écart de récupération attendu, à fixer sur pilote.

**Réfutation, écrite avant, par famille de mondes.** La thèse est : « l'organisme atteint mieux les puits étroits que la meilleure base ».

- Elle est démontrée si la borne inférieure de l'écart apparié dépasse zéro.
- Elle est réfutée si sa borne supérieure passe sous la marge minimale d'intérêt fixée d'avance.
- Sinon elle est indécise, et dite telle.
- Une méthode qui ne bat pas son placebo est réfutée.
- Tout gain est annulé si les fausses promotions dépassent le niveau annoncé en (v) ou (vi).
- Un gain en (ii) ouvre une enquête, non un succès.

### 5. Fausse originalité et sa mise à mort (PROPOSITION)

- **Bruit** (rare, sans gain sur tirages frais) : le juge.
- **Bizarrerie** (rare, structurée, sans prédiction discriminante) : refus mécanique de toute carte qui ne diffère du nul sur aucune instance publique.
- **Reformulation** (renommage, paraphrase, recollage par morceaux) : canonisation fonctionnelle, invariance sous renommage, nul étendu dont la validité reste à prouver (recoupement, section 9).
- **Complication** (gain acheté par des paramètres) : gain par bit de description, hors échantillon.
- **Ignorance d'antériorité** (nouveau pour le système, connu du monde) : recherche par un tiers.
- **Artefact de vue** : placebo.
- **Surajustement au banc** : familles de structures tenues en réserve, équipe adverse chargée de tromper les mesures.
- **Sélection après coup** des mondes « étroits » : interdite par construction.

### 6. Plan d'expériences (PROPOSITION), du moins cher au plus cher

0. **Audit des pertes** sur journaux bruts, sans aucun appel. Décide entre amont et aval.
1. **Loi spontanée** : appels frais par famille ; rang-fréquence, masse non vue, recouvrement. Décide si changer de proposeur est un levier ; fixe les seuils de largeur.
2. **Qualification de la garde** : mondes nuls, copies, contrôle positif. Décide si une méthode poussant vers le conditionnel peut être comparée.
3. **Réactivité à la vue** : liste des paires non croisées contre placebo contre appels supplémentaires. Puis deux manipulations sans verdict : listes longues dont on écarte le début, liste d'exclusion des classes spontanément fréquentes. Décide si le levier « vue » existe ; sinon toute la section 2 du recoupement tombe.
4. **Banc complet**, scellé et préenregistré. Décide quelle structure est exploitable.
5. **Chaînes sur plusieurs générations**, avec contrôle en ligne des erreurs et mesure de la concentration des lignées (HYPOTHÈSE : l'héritage récompensé favorise le raffinement des bassins larges).
6. **Validité externe** : rétrodiction sur textes postérieurs à la date de coupure des modèles, puis prédictions scellées jugées à l'aveugle. Décide ce que la thèse peut affirmer.

### 7. Question neutre

« Un système de plusieurs modèles de langue propose des hypothèses écrites dans une grammaire publique. Un test statistique, calculé hors de tout modèle sur des données fraîches, retient ou rejette chacune ; les hypothèses retenues sont transmises à la génération suivante. On se demande si les propositions se concentrent sur un petit nombre d'hypothèses fréquentes, et ce qu'il faudrait en conclure.
1. Quelles grandeurs définiriez-vous pour dire qu'une hypothèse est rarement proposée, qu'elle est juste, qu'elle est utile en aval ? Comment les mesurer sans demander à un modèle de noter la nouveauté ?
2. Peut-on, à coût égal, augmenter la probabilité qu'une hypothèse rare et juste soit proposée puis retenue ? Donnez les arguments pour et contre, résultats d'impossibilité compris.
3. Quelles méthodes, quelles comparaisons minimales, quels contrôles ?
4. Quel résultat d'expérience vous ferait conclure que votre proposition est fausse ?
Citez auteurs, année et titre ; séparez ce que vous savez de ce que vous supposez ; aucun chiffre sans source. »

## D. Décisions pour le directeur

**D1. Faire l'audit des pertes et la mesure de la loi spontanée avant tout essai de méthode.**
- Enjeu : sans eux, on ignore quel levier tirer.
- Option (a), audit d'abord — avantage : presque gratuit, oriente tout ; inconvénient : quelques jours de délai.
- Option (b), essais de vues tout de suite — avantage : élan ; inconvénient : risque d'optimiser le mauvais étage.
- Recommandation : (a). Confiance : 0,85.

**D2. Dire si une liste d'exclusion des classes spontanément fréquentes est compatible avec la règle « aucun score de nouveauté servi à un agent ».**
- Enjeu : c'est la forme la moins chère de l'adversaire du banal. Elle ne contient ni verdict ni issue, mais pousse vers la classe que le nul ne couvre pas.
- Option (a), interdire — avantage : garde intacte ; inconvénient : levier amont inexploré.
- Option (b), permettre au banc seulement, après qualification de la garde, avec placebo — avantage : mesure nette ; inconvénient : un bras de plus.
- Option (c), permettre en course — avantage : effet immédiat ; inconvénient : bizarrerie non mesurée.
- Recommandation : (b). Confiance : 0,65.

**D3. Choisir l'épreuve de validité externe.**
- Enjeu : la portée des papiers.
- Option (a), mondes plantés seuls — avantage : vérité exacte ; inconvénient : transfert non établi.
- Option (b), ajouter la rétrodiction datée — avantage : monde réel ; inconvénient : contamination par les données d'entraînement.
- Option (c), ajouter des prédictions scellées — avantage : seule preuve prospective ; inconvénient : délai.
- Recommandation : (a) puis (c), (b) en appoint. Confiance : 0,6.

**D4. Borner la revendication des papiers.**
- Enjeu : crédibilité.
- Option (a), revendiquer l'« originalité » — avantage : portée ; inconvénient : indéfendable sans validité externe.
- Option (b), revendiquer la récupération de puits plantés à budget égal, résultats négatifs compris — avantage : vérifiable par un tiers ; inconvénient : moins spectaculaire.
- Recommandation : (b). Confiance : 0,85.

FIN DE LA RÉPONSE
