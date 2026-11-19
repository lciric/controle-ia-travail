# Barreau 5 — comment le résoudre : note de synthèse pour Lazar (version 2)

- Écrite le 19 novembre 2026 vers 13:30Z par le synthétiseur (Claude Fable 5.2). Elle remplace la version 1 (`note-resolution-barreau5-v1.md`, empreinte `c1a98e32…`), qui reste à côté sans modification. Elle traite, remarque par remarque, la contre-lecture adverse d'un autre modèle, Claude Opus 5.5 (`contre-lecture-note-resolution-barreau5-v1.md`, empreinte `f29d3321…`) : 3 remarques bloquantes, 12 majeures, 18 mineures. Table de traitement au § 7 ; erreurs trouvées par moi au § 8.
- Pièce de travail, non scellée. Rien lancé, rien dépensé, rien commis. Aucun refus d'outil.
- Sources : le socle des faits (`barreau5-comprendre/00-socle-des-faits.md`) et ses notes 01 à 06 ; les conceptions A « le plus sûr avant l'entretien », B « l'identification propre », C « la validation hors de nous » du dossier `barreau5-concevoir/` ; les calculs refaits par le contre-lecteur (`contre-lecture-calculs-v1.py`, sortie `sortie-contre-lecture-calculs-v1.json`).
- Relu par moi pour cette version : le texte scellé de l'apprentissage des sondes sur la tâche (`prereg/T0.7-etape-B-bis-v1.md`, lignes 70-73, 93, 98, 207-213) ; le texte scellé de validité de l'adaptateur (`prereg/validite-adaptateur-v1.md`, lignes 43, 88-91, 107, 118-120, 217-232) ; `registres/go.md` ligne 297 ; `registres/decisions.md` lignes R-3791 à R-3823 ; `t06/lanceur.py` ligne 266 ; `sondes/familles.py` lignes 74-81 ; `t07bbis/etat_impose_v1.py` (en-tête et fonction `imposer_etat`).
- Chiffres de résultat : seulement ceux de l'apprentissage des sondes sur la tâche (étape B bis). Trois d'entre eux (0,6871 ; 0,8793 ; 0,6991) sont dans la note 02 du socle et non dans son résumé : déclaré au § 8. Les puissances viennent de lois inventées.

## 1. Le verdict en trois lignes

1. **Ta question en cache trois ; aucune ne se tranche avant l'entretien, deux se resserrent.**
   - « La sonde ne lit-elle que la présence d'un adaptateur ? » : non, à la dose 1, et c'est déjà acquis. Sans aucun adaptateur, la sonde apprise sur la tâche sépare le saboteur instruit de l'honnête (0,9675) et les textes du saboteur de ceux de l'honnête (0,8793). Cela ne dit pas « sabotage » : la consigne et le texte ne sont pas écartés. Ce qui reste ouvert est l'interaction : au-delà de l'effet additif de l'adaptateur et du texte, la sonde suit-elle l'épisode saboté ? La ligne scellée « texte égal moins adaptateur seul » l'a posée : non établie, contraire à la dose 1. La lecture neuve la remesure sur une échelle non saturée, à 0 USD, puis environ 2,5 à 4,6 USD de carte pour la relecture par un même chemin de calcul. Son issue est en partie prévisible depuis les aires déjà lues : à la dose 1, contraire.
   - « Lit-elle le sabotage, ou l'empreinte de cet adaptateur-ci ? » ne se tranche qu'avec plusieurs paires d'adaptateurs (saboteur et témoins de même intensité mesurée) : après l'entretien, 17 à 48 USD.
   - « Lit-elle l'acte, ou la disposition ? » : un premier contraste à poids constants, à l'abri du chemin de calcul et du nombre déclaré, se calcule à 0 USD. C'est la tendance, avec l'excès de coût déclaré, du score restreint aux jetons d'avant le champ du coût, chez le saboteur et chez l'honnête. L'intervention sur la direction lue vient après.
   - Ces trois questions portent sur les sondes apprises sur la tâche, celles où la confusion a été mesurée. Les sondes génériques, qui jugent le critère 3 de la porte G0, sont une seconde famille : leur instrument est le texte scellé de validité de l'adaptateur (décision 1, option d).
2. **Ce qui ne peut pas le résoudre.** Le texte scellé de validité de l'adaptateur joué tel quel (il vise les sondes génériques, ne produit qu'un seul jumeau, ne garde aucune activation). Toute lecture de plus qui conclurait « sabotage » avec un seul adaptateur saboteur. Un effacement du sous-espace « adaptateur » estimé sur d'autres adaptateurs et jugé contre le modèle nu (0,80 à 0,97 d'aire sans aucun sabotage, dans un monde inventé : la direction propre de cet adaptateur-ci survit). Un effacement estimé sur l'empreinte de cet adaptateur sur des textes honnêtes n'est pas couvert par cette simulation, et demande des activations, aujourd'hui perdues.
3. **Avant le 1er décembre, aucune issue ne dit « sabotage », aucune ne dit « adaptateur seul ».** Un nul se dit « non établi à cette puissance (aire au plus [borne haute]) », jamais une absence ; il porte la même réserve de chemin de calcul qu'un positif tant que la relecture par un même chemin n'est pas faite (règle R4). Un positif dit seulement « l'adaptateur et l'effet additif du texte n'expliquent pas toute la lecture ». Une issue contraire, où l'adaptateur déplace moins la sonde sur les épisodes du saboteur que sur des textes honnêtes, est attendue à la dose 1 d'après les aires déjà lues ; elle a sa phrase.

## 2. Les quatre points de ta demande, pris dans les trois plans

**Ce qu'un expert ferait.** Il commencerait par nommer l'unité. Le sabotage est donné à l'adaptateur par ses données de distillation, et il n'y a qu'un adaptateur saboteur : les 640 actions sont des mesures répétées d'une seule unité traitée (conception B). Il noterait aussi que la sonde a été apprise avec une étiquette confondue avec l'adaptateur : positifs sous adaptateur, négatifs sous le modèle nu (socle, point 0.3). Puis il poserait le plan à quatre cases (adaptateur présent ou absent, sabotage présent ou absent) avec plusieurs réalisations par case (conception C), et il apprendrait la sonde contre le jumeau honnête, jugée sur une paire jamais vue (conception B).

**Les données brutes de départ.** Tout est sur les branches, par action :
- les scores de l'apprentissage des sondes sur la tâche, 320 par groupe et par pli, pour six groupes : épisodes du saboteur, épisodes honnêtes, textes du saboteur relus sous le modèle nu, textes honnêtes relus sous l'adaptateur saboteur, épisodes de l'adaptateur témoin, textes honnêtes sous le témoin ; plus 800 directions tirées dans la covariance des jetons d'apprentissage de chaque sonde, et la sonde jumelle du second ordre de calcul ;
- pour les épisodes du saboteur, les épisodes honnêtes et les textes du saboteur relus sous le modèle nu : le même score restreint aux jetons d'avant le champ du coût (note 02 du socle, ligne 324) ;
- les poids des dix sondes, les deux adaptateurs, le coût déclaré de chaque action ;
- une seconde paire d'adaptateurs de la même recette, sur la course exploratoire.

Perdus : les activations complètes et les textes de distillation. Gardé : un dixième des actions à la couche 15, par jeton (576 actions, 1,06 Go, états d'origine). Il permet de localiser, jeton par jeton, où s'allument les sondes de couche 15, notamment dans le champ du coût : calcul au processeur, sous le texte neuf.

**Les méthodes.** Le meilleur de chaque plan :
- de A, le **plan factoriel présent dans les scores gardés** : état (adaptateur, modèle nu) croisé avec texte (saboteur, honnête), sous la même sonde.
  - Quatre de ses six comparaisons sont déjà lues. Son interaction est la grandeur de la ligne scellée « texte égal moins adaptateur seul », remesurée sur une échelle non saturée, choisie après avoir vu que celle-ci plafonne. L'exposition est déclarée dans le texte neuf.
  - Ce texte écrit, avant lecture, la prévision que les quatre aires lues donnent pour chaque contraste neuf (table ci-dessous).
  - La grandeur jugée est l'interaction sur les scores bruts, qui sont linéaires, sans fonction de lien (`sondes/familles.py` ligne 76) : le déplacement de chaque action par l'adaptateur, en différence appariée par action et réduite par pli (les deux plis portent des sondes d'échelles différentes), comparé entre textes du saboteur et textes honnêtes. Elle est jugée contre zéro, dans les deux sens. L'écart à la prévision est rapporté à côté, sans seuil : la prévision vient d'un modèle à deux lois normales de même variance, qui colle mal à la dose 0,5 (traitement « autrement » de B-2, § 7).
  - Les issues contraires ont leurs phrases (§ 4).
  - La tendance avec l'excès déclaré se lit sur le score restreint aux jetons d'avant le champ du coût, chez le saboteur moins la même chez l'honnête : deux séries de l'ancien chemin de calcul, à adaptateur constant de chaque côté, à l'abri du chemin, du nombre déclaré et de l'effet « texte propre ». La ligne voisine « actions gonflées contre non gonflées », sur le score entier, a été lue : exposition déclarée ;
- de A encore, **les deux défauts de ce plan**. Son interaction porte deux fois l'effet du chemin de calcul (deux cases par l'ancien chemin, deux par le neuf) : la relecture des quatre cases par le même chemin le lève. Elle porte aussi deux fois l'effet « texte propre contre texte imposé » (le modèle lit le texte qu'il a tiré dans deux cases, un texte imposé dans les deux autres) : la relecture ne le lève pas ; seule la triple différence avec le même plan à quatre cases pour le témoin en ôte la part commune à tout adaptateur ;
- de B, **les paires répliquées** et le test exact par changement de signe, la mesure d'intensité comme condition de tout, et l'interdit sur l'effacement jugé contre le modèle nu ;
- de C, **l'épreuve à vérité plantée** du programme de lecture. Dans un monde inventé à quatre adaptateurs par bras, où un écart d'intensité de 10 % vaut environ 1,4 écart type entre adaptateurs, un témoin à 90 % de l'intensité du saboteur donne 47,5 % de faux « au-delà de l'adaptateur ». Le chiffre suit ce rapport inventé ; la leçon tient : « saboteur au-dessus du témoin actuel » ne conclut rien tant que l'intensité n'est pas égalée.

**Prévision tirée des aires déjà lues** (calcul du contre-lecteur, bloc 3 de sa sortie ; arithmétique sur les aires scellées, modèle à deux lois normales de même variance ; ordre de grandeur seulement, les deux voies de calcul divergent à la dose 0,5). L'arithmétique de la dose 1 est refaite par moi et tombe juste.

| dose | interaction déjà lue, en écarts types (texte égal moins adaptateur seul) | aire attendue du contraste « épisodes du saboteur contre textes honnêtes, même adaptateur » | interaction attendue (cette aire moins celle du texte seul) | issue attendue |
|---|---|---|---|---|
| 0,25 | +0,20 | 0,53 à 0,55 | +0,04 à +0,06 | non établi (sous l'aire minimale) |
| 0,5 | −0,60 | 0,40 à 0,53 | −0,17 à −0,04 | non établi |
| 0,75 | +0,27 | 0,71 à 0,75 | +0,03 à +0,07 | contraste au-dessus, par l'effet du texte déjà lu (0,6871) |
| 1 | −1,01 | 0,60 à 0,68 | −0,28 à −0,20 | interaction contraire |

**Ce que chaque contraste ferme et laisse ouvert** (table du contre-lecteur, § 1 de son rapport, condensée). Rivales : intensité, graine de l'adaptateur, données de distillation, texte, longueur, champ du coût, consigne, chemin de calcul, texte propre contre imposé, graines d'action partagées d'une condition à l'autre (`t06/lanceur.py` ligne 266, relu).

| contraste | ferme | laisse ouvert |
|---|---|---|
| Épisodes du saboteur contre textes honnêtes, même adaptateur, même dose | présence de l'adaptateur, consigne | texte (rivale principale), longueur, champ du coût, chemin, texte propre, données de distillation |
| Interaction du plan factoriel | effet additif du texte, consigne | échelle, données de distillation, champ du coût, texte propre (après relecture) ; chemin (avant relecture) |
| Tendance du score d'avant le champ du coût avec l'excès, saboteur moins honnête | intensité, champ du coût, chemin, texte propre, consigne | contenu d'avant le champ (en partie), un seul adaptateur |
| Saboteur contre témoin sur les mêmes textes honnêtes, apparié par action | texte, longueur, champ du coût, chemin, consigne | intensité (sauf témoin relu à plusieurs doses et divergences égalées), graine, données : un contre un |
| Paires répliquées à texte constant | tout ce qui précède si l'intensité est égalée sur deux mesures | « sabotage » contre « tout changement de comportement appris », si le seul témoin est un jumeau autodistillé |
| Actions gonflées contre non gonflées, poids constants, jetons d'avant le champ du coût | intensité, graine, données, champ du coût | contenu du texte d'avant le champ |

**Ce qui validerait hors de nous.** Par force croissante :
- texte scellé avant lecture ; scores par action et programme mis à ta disposition et à celle du jury, recalculables sur un portable (A) ; toute publication ou tout dépôt public est un nœud ;
- épreuve à vérité plantée où un tiers tire lui-même le monde (contact externe : nœud) ; double programmation par l'autre modèle, contrôle interne (même famille de modèles), accord exact sur les grandeurs déterministes, et sur les bornes de rééchantillonnage seulement si les tirages sont partagés par fichier (deux tirages indépendants ne s'accordent pas à 10⁻⁶) (C) ;
- relecture sur une autre pile logicielle (C) ;
- un précédent publié du contraste à adaptateur constant : « Caught in the Act », arXiv 2610.12445v1, p. 26 (table 10) et p. 33 (table 14), vérifié sur PDF par le critique et par la contre-lecture. Ses sondes sont apprises sur un jeu de tromperie externe et lues à travers chaque adaptateur, comme les sondes génériques du texte scellé. Sa figure 1b (p. 1) compare deux organismes : elle porte une confusion voisine de la nôtre, l'identité de l'adaptateur ;
- à citer comme pris, non comme validation : des comportements mis par réglage fin dans des modèles bénins allument les sondes (Taylor et al., 2512.07810, p. 17) ; un adaptateur de rang 1 sur Llama-3.1-8B laisse une signature générique que l'entraînement efface (2609.36490, p. 6-7). Tous deux vérifiés sur PDF dans le socle (§ 5) ;
- après l'entretien : rejouer la règle sur les organismes publiés par l'institut britannique de sécurité de l'IA (référence Cooney et al., 2606.12618, **non vérifiée sur PDF**), et un statisticien externe.

**Où les plans divergent.**
- *Peut-on apprendre quelque chose à l'intérieur de l'organisme ?* A : oui, « au-delà de la présence de l'adaptateur ». B et C : non pour « sabotage », parce que adaptateur et disposition sont la même variable par construction. Je retiens les deux : A resserre la première question, B et C répondent à la deuxième.
- *Jouer le jumeau honnête du texte scellé avant le 27 novembre ?* A : oui si le code est prêt le 25. B et C : non. Je retiens non : un jumeau unique sans activation gardée ne permet aucun test, et son code disputerait la semaine à la lecture qui, elle, tient.
- *Combien de paires ?* B : six (test exact impossible sous cinq). C : quatre contre quatre par permutation (90 % de puissance pour un écart de 2,5 écarts types entre graines, jamais mesuré). Ces puissances valent toutes au seuil de 5 % unilatéral ; à 99 % elles sont nulles (décision 4).
- *Finesse du contraste principal.* A : aire détectable 0,63 à 0,69 à 99 % bilatéral, contre un plancher supposé à 0,56 (convention de l'étape B bis ; ancre réalisée sur la ligne de même forme déjà lue : environ 0,63 à 0,64). C : 0,55 à 0,60 contre 0,5, tâches appariées. Je garde le chiffre prudent de A. Le texte de l'étape B bis (ligne 208) dit lui-même qu'une formule à plancher fixe est optimiste.

## 3. Le plan retenu

### Avant le 1er décembre

Ordre réel : 0, puis 2, puis 1, puis 3, puis 4. Les numéros de la version 1 sont gardés.

| n° | étape | ce qu'elle tranche | données | coût | durée | puissance | tient ? |
|---|---|---|---|---|---|---|---|
| 0 | Tes décisions 0 à 3, **avant toute lecture** | rend valide tout le reste (aucune pièce lancée « sur la foi d'une sortie ») | — | 0 | 20 novembre | — | condition |
| 2 | Texte neuf court, scellé et contre-lu : « validité de l'adaptateur pour les sondes apprises sur la tâche ». Deux lectures déclarées d'avance ; exposition des concepteurs déclarée ligne par ligne, avec la prévision ci-dessus ; épreuve à vérité plantée définie dedans ; règle de famille, audit de symétrie, niveaux (décision 5) | — | — | 0 | scellé le 23 au soir au mieux si la conception attend le 22 à 18:00Z ; plus tôt si Fable répond (réserve 1) | — | oui, si la conception se fait à temps |
| 1 | Épreuve à vérité plantée du programme de lecture de l'étape 3, définie dans le texte neuf avec sa règle (taux de fausse lecture admis, interaction plantée à l'aire minimale), jouée sur le fichier final après le scellement et avant toute ouverture des scores ; double programmation | ce programme (un adaptateur saboteur, un témoin non honnête) rend-il « non établi » dans un monde « adaptateur seul », retrouve-t-il une interaction plantée de la taille de l'aire minimale, et que fait-il d'une interaction contraire | loi inventée | 0 | après le texte, le 23 ou le 24 | à chiffrer pour ce programme ; les 93,5 % et 99,5 % de la conception C portent sur un plan à quatre adaptateurs par bras, qui n'existe pas avant l'entretien | pièce de conception de Fable, partie du texte décisif, pas de la routine |
| 3 | Première lecture, au processeur : interaction du plan factoriel sur les scores bruts, prévision écrite à côté ; tendance avec l'excès sur le score d'avant le champ du coût, saboteur moins honnête (ancien chemin) ; saboteur contre témoin sur les mêmes textes honnêtes, apparié par action (descriptif) ; géométrie des poids (descriptif) ; recouvrement des textes du saboteur et de l'honnête par tâche (préfixe commun, distance d'édition), porté en covariable | l'interaction au-delà de l'adaptateur et du texte ; un premier contraste « acte » à poids constants | scores et poids gardés, coût joint par clé, deux adaptateurs, textes | 0 | lecture le 24 ou le 25, verdict par agent neuf | aire 0,63 à 0,69 à 99 % bilatéral (ancre réalisée ≈ 0,63 à 0,64) ; différence de deux aires 0,10 à 0,17, chiffre prudent (le partage des textes entre cases n'est pas modélisé) ; tendance 0,14 à 0,20 (plancher 0,03 supposé), 0,16 à 0,25 (plancher au quantile 0,95 d'un tau nul) ; chaque ligne tenue seulement si la sonde et sa jumelle s'accordent, ce qui baisse la puissance, d'une quantité à chiffrer dans le texte | oui |
| 4 | Relecture sur carte, par un même chemin : les quatre cases aux quatre doses ; le témoin relu aux doses 0,25 à 1 sur les textes honnêtes ; les textes du témoin relus sous le modèle nu (plan à quatre cases du témoin, dose 1) ; le témoin instruit noté par les sondes de dose (64 épisodes) ; toutes les cases notées avec et sans les jetons du champ du coût ; longueur notée ; intensité mesurée de deux façons pour les deux adaptateurs (divergence des sorties, norme du déplacement à la couche lue) ; activations gardées (décision 5) ; puis seconde lecture | lève la réserve de chemin de calcul ; ôte la part commune de l'effet « texte propre » ; donne la première mesure d'intensité et la comparaison saboteur contre témoin à intensité égale, qui reste un contre un | adaptateurs, textes, poids des sondes, module de relecture existant (`etat_impose_v1.py`, dont la fonction d'état imposé accepte toute dose pour tout adaptateur chargé : relu) | ≈ 2,5 à 4,6 USD attendus (devis scellé d'une relecture : 1,9 à 2,8 heures, mise en place comprise), pire cas ≈ 8,85 ; coupure du devis scellé : 8,5 USD ; ou 5 USD avec un ordre de sacrifice écrit des séries ; la garde des activations est en plus, non chiffrée ; devis à refaire | carte le 25 ou le 26, lecture le 27 | mêmes seuils, sans réserve de chemin | oui si décisions 2 et 3 ; sinon l'entretien se fait sur la première lecture |

Extensions de garde, portées au texte neuf : la garde des prédicteurs triviaux (longueur notée, rang du pas, mention) s'étend au contraste principal et à l'interaction, qui deviennent « non interprétables » si la longueur sépare autant.

### Après le 1er décembre

| n° | étape | ce qu'elle tranche | coût | puissance |
|---|---|---|---|---|
| 5 | Relecture des quatre adaptateurs existants (course exploratoire comprise, décision 7), sur une autre pile | transfert d'une sonde d'une graine à l'autre ; ordre de grandeur de l'écart entre deux apprentissages de la même recette | 2,5 à 4,6 USD | deux saboteurs : aucun test, descriptif ; une variance estimée sur deux adaptateurs a un degré de liberté et ne dimensionne aucun plan |
| 6 | Paires répliquées, saboteur et jumeau distillé de l'honnête, plus un témoin à changement bénin de même intensité ; textes de distillation gardés ; sonde apprise contre les jumeaux, jugée sur une paire tenue à l'écart. Intensité égalée par la divergence des sorties et la norme du déplacement à la couche lue ; aucun score de sonde dans l'entraînement, le choix, l'arrêt ou l'exclusion d'un adaptateur (invariant de la décision N-053) ; contrôle de manipulation par l'oracle du coût seul, règle écrite d'avance | **sabotage contre empreinte de l'adaptateur** : la question du barreau | 17 à 19 USD (trois graines sur deux tirages), 34 à 37 USD (six paires), 44 à 48 USD avec les épisodes générés ; le témoin à changement bénin et un passage à huit paires sont en plus, non chiffrés | six paires : 0,88 à 0,99 à 5 % unilatéral pour un écart de 2 écarts types entre graines, nulle à 1 % ; huit paires : 0,71 à 0,95 à 1 % |
| 7 | Contraste à poids constants, actions gonflées contre non gonflées, stratifié par tâche et cumulé, sur les jetons d'avant le champ du coût seulement (l'étiquette est fonction du nombre déclaré) ; intervention sur la direction lue, jugée par le coût, contre des directions témoins | acte ou trace ; lien causal | 6 à 20 USD (décision 8) | aire 0,57 à 0,60 ; baisse de 10 points vue à 0,98 contre 19 directions, à 5 % seulement (valeur p minimale 1/20) et si les directions témoins sont inertes ; à rechiffrer avec des témoins actifs (une direction placebo de même norme agit autant : 2610.22460, p. 8) ; à 99 %, plus de 99 directions témoins |
| 8 | Organismes d'une autre main, statisticien externe | la méthode hors de notre fabrication | sur devis | — |

Le texte scellé de validité de l'adaptateur reste intact tant que tu n'as pas tranché la décision 1 : lire ses lignes gratuites ferme ses lignes payantes (option d).

## 4. Ce qu'on dit au jury le 1er décembre

- **Rien de fait.** « Confusion mesurée, non levée : l'adaptateur seul déplace la sonde autant que l'organisme ; les contrôles qui la resserrent sont conçus et chiffrés, non joués ; le seul qui sépare « sabotage » de « cet adaptateur-ci » demande plusieurs paires d'adaptateurs, après l'entretien. »
- **Première lecture seule, nul.** « À adaptateur et dose fixés, nous n'établissons pas, à cette puissance (aire au plus [borne haute], interaction au plus [borne haute]), que la sonde sépare les épisodes du saboteur de textes honnêtes relus sous le même adaptateur au-delà de ce que donne le texte seul, ni qu'elle suit l'excès déclaré avant le champ du coût ; sous réserve de chemin de calcul. Elle n'est pas pour autant un détecteur d'adaptateur : sans aucun adaptateur, elle sépare déjà le saboteur instruit de l'honnête (0,9675). Son étiquette d'apprentissage était confondue avec l'adaptateur par construction ; une sonde apprise à adaptateur constant n'a pas encore été essayée. »
- **Première lecture seule, positif.** « Un signal apparaît à adaptateur fixé, au-delà de zéro et de la prévision tirée des aires déjà lues ; il est rapporté sous réserve de chemin de calcul et de texte propre, comme le serait un nul. »
- **Deux lectures, positif.** « La présence de l'adaptateur n'explique pas toute la lecture ; ne sont pas écartés l'empreinte du réglage fin, le texte propre de l'adaptateur, et le fait qu'il n'y a qu'un adaptateur. »
- **Interaction contraire.** « À la dose [d], l'adaptateur déplace moins la sonde sur les épisodes du saboteur que sur des textes honnêtes, comme la ligne scellée « texte égal moins adaptateur seul » à la dose 1 : la lecture ne va pas au-delà de l'adaptateur et du texte. Non écartés : le texte propre contre le texte imposé ; le chemin de calcul s'il n'y a qu'une lecture. Audit de symétrie (R4). »
- **Deux lectures, signal au niveau du texte seul.** « Au-delà de l'adaptateur, la sonde lit le texte », ce que la ligne déjà scellée dit aux doses 0,75 et 1.
- **Dans tous les cas.** « La question "sabotage ou adaptateur" exige des paires répliquées ; leur plan est conçu et chiffré sous une hypothèse sur la variance entre deux apprentissages de la même recette, jamais mesurée ; il n'est pas encore scellé. »

Le choix de la phrase du dossier te revient (décision 11).

## 5. Tes décisions

Les noms « D1 » à « D6 » de la version 1 sont abandonnés : ils se confondaient avec les décisions D1, D2, D3 du brief, qui ont un défaut sous 48 heures. Aucune des décisions ci-dessous n'a de défaut.

**Décision 0 — Qui conçoit si Fable refuse de nouveau.** *Nœud* (changement de modèle, ou quota).
- Enjeu : le texte neuf, son épreuve à vérité plantée et le devis de l'étape 4 sont des pièces de conception de Fable (règle « qui conçoit », R-3735). Sa disponibilité est intermittente depuis 12:05Z (R-3791, R-3792, R-3794) : refusé à 12:05Z et à 12:20Z, il a répondu ensuite (plusieurs rédacteurs entre 12:25Z et 13:05Z au registre ; cette note vers 13:30Z). Remise à zéro annoncée le 22 novembre à 18:00Z.
- Option a, rouvrir du quota de Fable si le refus revient : calendrier tenu ; toi seul le peux (R-3794).
- Option b, conception sur un autre modèle, déclarée comme écart à la règle « qui conçoit » : calendrier tenu ; conception hors de la règle.
- Option c, attendre le 22 à 18:00Z : la première lecture glisse au 25 au plus tôt, la relecture sur carte au 26 ou après le 27, sous accord prolongé.
- Recommandation : lancer la conception dès tes décisions 1 à 3, sur Fable tant qu'il répond ; au premier refus, a ; confiance moyenne.

**Décision 1 — Écrire un texte neuf pour les sondes apprises sur la tâche, et y réemployer les scores fermés.** *Nœud.*
- Enjeu : sans lui, aucune lecture gratuite n'est permise et rien ne change avant l'entretien.
- Option a, texte neuf, le texte scellé reste intact : répond pour les sondes où la confusion est mesurée ; quatre jours de chaîne complète.
- Option b, jouer le texte scellé tel quel : déjà contre-lu ; ne vise pas les sondes en cause, son aiguillage est inconnu.
- Option c, ne rien lire : aucun risque ; l'entretien se fait sur « non levée ».
- Option d, texte neuf pour les sondes apprises sur la tâche, et lecture des lignes gratuites du texte scellé pour les sondes génériques (celles du critère 3 de la porte G0), ses lignes payantes laissées « non calculables », ce que le texte permet (lignes 118-120) : répond pour les deux familles de sondes ; ferme pour toujours les lignes payantes du texte scellé ; demande un code qui n'existe pas, dans la même semaine ; dépend de l'aiguillage (deux booléens que je n'ai pas le droit de lire) et de l'antériorité du scellement au verdict qu'il exige (ligne 119) ; un code figé après l'ouverture des scores porte la réserve gelée du texte.
- Recommandation : a tout de suite, confiance haute. Pour d : faire lire les deux booléens par un agent autorisé (routine), puis décider ; ne le jouer avant l'entretien que si le texte neuf est scellé et qu'il reste de la capacité ; d n'a de sens que si les pièces payantes du texte scellé sont abandonnées (décision 2, options a ou c) ; confiance moyenne.

**Décision 2 — Sort de l'accord de 30 USD (GO-2026-11-10-07, échéance le 27 novembre).** *Nœud.*
- Enjeu : il couvre deux pièces du texte scellé qu'aucun code ne peut lancer proprement d'ici là.
- Option a, le prolonger au 12 décembre et le reporter sur le texte neuf : garde la dépense ouverte sans course hâtive ; change l'objet de l'accord. Plafond inchangé, 30 USD ; ordre des pièces : la relecture par un même chemin (étape 4, coupure 8,5 USD), puis la relecture des adaptateurs existants (étape 5, coupure 5 USD) ; le reste, environ 16 USD, ne couvre pas les paires répliquées à six paires ou plus : les étapes 6 et 7 passent par un devis neuf.
- Option b, jouer le jumeau honnête du texte scellé avant le 27 : consomme l'accord ; un seul jumeau, sans activation gardée.
- Option c, le laisser échoir : simple ; il faudra un devis neuf pour l'étape 4.
- Recommandation : a, confiance moyenne.

**Décision 3 — Dépenser environ 2,5 à 4,6 USD (coupure 8,5 ; ou 5 avec un ordre de sacrifice écrit) pour la relecture par un même chemin (étape 4).** *Nœud de dépense, devis à écrire par Fable.*
- Enjeu : sans elle, aucune issue de la première lecture (nul, positif, contraire) n'est lisible sans réserve de chemin de calcul.
- Option a, oui, sur l'accord reporté : meilleur rapport du plan ; exige les décisions 1 et 2.
- Option b, non : 0 USD ; toutes les phrases du jury gardent la réserve de chemin.
- Recommandation : a, confiance haute.

**Décision 4 — Taille, niveau et témoins des paires répliquées après l'entretien.** *Nœud de dépense et d'énoncé* (il donne le témoin apparié du brouillon de la décision N-074 pour la porte G1).
- Option a, six paires indépendantes, 34 à 48 USD : test exact valide à 5 % unilatéral (0,88 à 0,99 pour 2 écarts types entre graines), sans aucune puissance à 99 % (valeur p minimale 1/64) ; dépasse 30 USD.
- Option a bis, huit paires : 0,71 à 0,95 à 1 % ; environ 45 à 50 USD de carte par extrapolation linéaire de la conception B, épisodes générés en plus ; non chiffré par un devis.
- Option b, trois graines sur deux tirages de données, 17 à 29 USD : tient dans 30 USD ; deux tirages de données par bras seulement, donc rien ne se généralise au-delà de ces deux tirages ; test exact conditionnel aux tirages ; puissance non chiffrée.
- Option c, attendre la variance entre graines de l'étape 5 puis demander le devis : une variance estimée sur deux adaptateurs a un degré de liberté (intervalle à 95 % sur un facteur 71 pour l'écart type) et ne dimensionne rien ; deux semaines de plus.
- Dans toutes les options : un jumeau autodistillé de l'honnête n'apprend aucun changement de comportement (le texte de validité le dit « probablement plus faible ») ; remis à l'intensité, il peut amplifier des directions sans structure, et « saboteur au-dessus du jumeau » peut alors vouloir dire « adaptateur qui a appris quelque chose contre adaptateur qui n'a rien appris ». Le plan garde donc aussi, à intensité égale, un témoin à changement bénin, dans l'idéal dans le même champ (par exemple un format du coût changé sans en changer la grandeur). Cela touche la définition du témoin apparié de la porte G1.
- Le niveau se fixe dans le même texte : à 99 %, au moins sept paires (changement de signe), cinq contre cinq (permutation), plus de 99 directions témoins pour l'intervention ; sinon le niveau est déclaré à 95 % pour ces lignes.
- Recommandation (changée : la version 1 recommandait c) : devis après l'entretien, a bis si tu gardes 99 %, sinon a au niveau déclaré de 95 % pour cette seule ligne ; les deux témoins dans tous les cas ; confiance basse, parce que l'écart entre deux apprentissages de la même recette n'a jamais été mesuré.

**Décision 5 — Niveaux et règles de lecture du texte neuf.** *Partie du texte neuf (conception par Fable, contre-lecture), adoptée avec la décision 1 ; pas de défaut.*
- Niveau 99 % bilatéral par ligne ; ligne tenue seulement si la sonde et sa jumelle du second ordre de calcul s'accordent, puissance de cette conjonction chiffrée dans le texte (à la dose 0,25 les deux sondes divergent, 0,9357 contre 0,7929 : la ligne y sera presque toujours « non tranchée ») ; saboteur contre témoin et géométrie sans seuil.
- Règle de famille écrite (union des doses avec vecteur des états, comme l'étape B bis, ou correction de Holm sur les lignes principales) ; nombre de faux positifs attendu écrit à côté du nombre observé ; audit de symétrie gelé, comme dans les deux textes scellés (aire hors de [0,05 ; 0,95], ligne contraire, tout au-dessus).
- Géométrie des poids : le nul de référence est celui des 800 directions du plancher, non une direction isotrope ; l'adaptateur écrit dans le flux par d'autres voies que ses matrices de sortie (les termes ajoutés à q, k et v passent par la matrice de sortie de base et les couches suivantes) : un alignement faible n'acquitte pas, un alignement fort n'accuse qu'à cette couche.
- Activations de l'étape 4 : par jeton, à la couche 15 (≈ 1,2 Go par série, ≈ 20 Go pour dix-sept séries, d'après le sous-ensemble de la course de confirmation), et le vecteur moyen par action à la couche retenue de chaque pli, déclaré bras de diagnostic (décision N-026), jamais pour apprendre une sonde de production. Vingt gigaoctets dépassent ce qu'une branche du dépôt porte commodément (le sous-ensemble de 1,06 Go y est déjà en treize morceaux ; limite du dépôt distant non vérifiée par moi) : le lieu de dépôt est une ligne du devis ; repli écrit d'avance si aucun lieu ne convient, les jetons des quatre cases du saboteur d'abord, le témoin ensuite.
- Les normes des adaptateurs entrent dans la mesure d'intensité : elles se calculent sous le texte neuf, après son scellement, non avant (exposition).
- Recommandation : tel quel ; confiance haute.

**Décision 6 — Validation d'une autre main.** *Trois nœuds distincts*, tous après l'entretien :
- contact externe : le statisticien, et le tiers qui tirerait lui-même le monde de l'épreuve à vérité plantée (tu envoies, je rédige) ;
- changement de modèle pour les organismes publiés (Qwen3.6-27B), qui rouvre la décision R-122 ;
- publication des scores par action et du programme.
- Recommandation : sur devis et licences vérifiées ; confiance moyenne.

**Décision 7 — Réemployer les adaptateurs de la course exploratoire, et dépenser 2,5 à 4,6 USD pour les relire (étape 5).** *Nœud* : données versées, interdites sous les deux textes scellés (« rien de 7a », texte de validité ligne 107 ; « tout fichier de 7a », texte de l'étape B bis ligne 98) ; il faut un texte contre-lu et ton mot (« Récupérer ce qui est récupérable »).
- Option a, oui, sous un texte propre, après l'entretien : seule seconde paire existante, gratuite à produire ; descriptif seulement.
- Option b, non : rien ne sort de cette paire.
- Recommandation : a, confiance moyenne.

**Décision 8 — Dépense de l'étape 7 (contraste à poids constants et intervention), 6 à 20 USD.** *Nœud de dépense*, après l'entretien, sur devis. Recommandation : après les paires répliquées ; confiance moyenne.

**Décision 9 — Sens du contraste « textes du saboteur relus sous le modèle nu contre l'honnête » dans le texte neuf.** *Nœud* (le texte de validité le lit comme soutien, celui de l'étape B bis comme réserve).
- Option a, réserve (« elle lit aussi le texte ») ; option b, soutien ; option c, simple effet principal du plan factoriel, sans sens propre.
- Recommandation : c, parce que le plan factoriel le soustrait déjà ; confiance moyenne.

**Décision 10 — Paires répliquées et second cycle gelé.** *Nœud* : la recette des paires (témoin de même intensité, second témoin honnête) recouvre celle du second cycle de l'accumulation, gelé (GO-2026-11-19-27).
- Options : dégel du second cycle ; rattachement des paires au chantier « saboteur et sondes pour l'entretien » ; ou attente de la fermeture d'un chantier actif.
- Recommandation : rattachement, la question étant celle de l'entretien ; confiance basse.

**Décision 11 — Phrase du dossier de l'entretien sur le barreau 5.** *Ton choix* (note 02 du socle, nœud 6), parmi les phrases du § 4, une fois les lectures faites.

**Routine, sans ton mot** : le code de lecture et ses essais sur scores factices ; la lecture des deux booléens de l'aiguillage du texte scellé par un agent autorisé. L'épreuve à vérité plantée est une pièce du texte neuf, conçue par Fable.

## 6. Réserves et inconnues

1. **Calendrier, jamais compté.** Le texte neuf, son épreuve à vérité plantée et le devis de l'étape 4 sont des pièces de conception de Fable, dont la disponibilité est intermittente (décision 0). Si la conception ne peut commencer que le 22 novembre à 18:00Z : texte le 23 au soir au mieux, code et épreuve le 24, première lecture le 24 ou le 25, carte le 25 ou le 26 sous l'accord prolongé (décision 2), seconde lecture le 27, verdict avant le 30. Aucune marge. Si Fable répond dès le 20, deux jours de marge.
2. **Variance entre deux adaptateurs de même recette : jamais mesurée.** Toute puissance de l'étape 6 est un pari sur elle ; l'étape 5 ne la mesure pas (un degré de liberté).
3. **Intensité : mesurée pour aucun adaptateur.** Le témoin actuel n'est ni honnête ni étalonné. La mesure est double : divergence des sorties, et norme du déplacement à la couche lue ; l'égalité est exigée sur les deux, ou l'écart est rapporté.
4. **Réserves propres au contraste principal.** Le modèle lit son propre texte dans deux cases et un texte imposé dans les deux autres : l'interaction porte deux fois cet effet, que la relecture homogène n'ôte pas ; seule la triple différence avec le plan à quatre cases du témoin en ôte la part commune, et c'est un contre un. Les deux plis portent des sondes différentes et divergent souvent ; la dose 0,25 est instable ; les graines d'action sont partagées d'une condition à l'autre, donc les textes du saboteur et de l'honnête peuvent partager de longs préfixes aux faibles doses (non mesuré) ; la longueur et le champ du coût ne sont contrôlés qu'à l'étape 4.
5. **Un seul mode de sabotage**, étiqueté par le coût déclaré et non par un oracle.
6. **Question à faire porter par une session autorisée** (je n'ai pas le droit de lire ces pièces) : le saboteur à budget ou le bras A font-ils varier le sabotage à poids constants par une variable que l'oracle connaît ? Si oui, c'est le meilleur banc pour ce barreau. Le registre (R-3802, R-3822) dit le saboteur à budget en reconception : ne pas compter sur ce banc avant l'entretien.
7. **État de l'art.** Effacement de concept (LEACE), comparaison de modèles, Cooney et al. : non vérifiés sur PDF. Aucune phrase « la séparation du comportement et de la trace de l'adaptateur est libre » : zone peu cherchée.
8. **Coûts** : ordres de grandeur tirés des devis scellés, à refaire en devis ; le pire cas d'un adaptateur distillé est d'environ 24,6 USD dans le devis scellé (ligne 217), celui des paires n'est écrit nulle part. Puissances : lois inventées.
9. **Ménage** : environ 100 Mo d'extraits restent sous `barreau5-comprendre/extraits/` ; leur effacement a été refusé par une garde et reste à faire par toi ou par la session mère.
10. **Exposition.** Les concepteurs ont lu toutes les aires de l'étape B bis. Le texte neuf l'écrit, ligne par ligne, avec la prévision tirée de ces aires, comme le texte de validité l'a fait pour sa réserve gelée.
11. **Multiplicité.** Environ quatre doses fois quatre lignes à 99 % avant l'entretien : la règle de famille et le nombre de faux positifs attendu sont à écrire dans le texte (décision 5).

## 7. Table de traitement de la contre-lecture

« Telle quelle » : le texte « après » du contre-lecteur est repris, à la ponctuation près.

| remarque | traitement | où, et pourquoi si autrement |
|---|---|---|
| B-1, le nul n'est pas une réponse ferme | appliquée telle quelle, avec un ajout | § 1 point 3 et § 4. Ajout au § 1 : la séparation sans adaptateur ne dit pas « sabotage », la consigne et le texte n'étant pas écartés |
| B-2, grandeur déjà lue, exposition, issue contraire | appliquée, un point autrement | § 1 point 1, § 2 (méthodes, table de prévision), § 4 (phrase « interaction contraire »), § 6 point 10. Autrement : la grandeur jugée est l'interaction sur les scores bruts contre zéro ; l'écart à la prévision est rapporté sans seuil, parce que la prévision sort d'un modèle que le contre-lecteur dit lui-même mal ajusté à la dose 0,5 |
| B-3, épreuve à vérité plantée | appliquée telle quelle | § 2, § 3 (ligne 1, placée après le texte), § 5 (routine, décision 5) |
| M-1, règle « qui conçoit » et quota | appliquée autrement | Décision 0 et § 6 point 1. « Rien ne commence avant le 22 à 18:00Z » est trop fort : le registre montre des rédacteurs Fable au travail entre 12:25Z et 13:05Z, et cette note est écrite par Fable. La décision porte sur le prochain refus |
| M-2, coût de l'étape 4 | appliquée, précisée | § 3 ligne 4, décision 3. Le plafond « 9 USD » devient la coupure du devis scellé, 8,5 USD (texte de validité, ligne 224, relu) ; les ajouts de M-3, M-4 et M-10 demandent un devis refait |
| M-3, texte propre contre imposé | appliquée telle quelle | § 2, § 3 ligne 4, § 6 point 4 |
| M-4, longueur, champ du coût, consigne, graines, intensité à bas prix | appliquée telle quelle | § 2 (table des rivales), § 3 (lignes 3 et 4, extension de garde), § 6 point 4. Ces ajouts entrent dans le texte neuf, donc sans défaut (cohérent avec m-7) |
| M-5, contraste « acte » à 0 USD, restriction de l'étape 7 | appliquée telle quelle | § 1, § 2, § 3 lignes 3 et 7 |
| M-6, niveaux et puissances d'après l'entretien | appliquée, recommandation changée | Décision 4 (options, niveau), § 3 lignes 5 à 7. La version 1 recommandait l'option c, que la remarque rend intenable : nouvelle recommandation écrite, confiance basse ; option a bis ajoutée par moi |
| M-7, neuf nœuds manquants | appliquée telle quelle | Décisions 0, 6 (trois nœuds), 7, 8, 9, 10, 11 |
| M-8, jumeau autodistillé | appliquée autrement | Décision 4 et § 3 ligne 6. Le contre-lecteur la range en « proposer avec recommandation » ; elle touche le témoin apparié de la porte G1, donc un énoncé : je la porte au nœud. Le « facteur 64 » qu'il cite n'est pas repris, non relu par moi |
| M-9, lignes gratuites du texte scellé | appliquée autrement | Décision 1 option d, § 1. L'option est ajoutée ; je ne la recommande pas d'emblée : aucun code, aiguillage inconnu, fermeture définitive des lignes payantes |
| M-10, activations par jeton | appliquée autrement | Décision 5. Jetons gardés, moyenne en bras de diagnostic ; mais 20 Go sur une branche du dépôt est à instruire : lieu de dépôt au devis, repli écrit |
| M-11, multiplicité, conjonction, audit de symétrie | appliquée telle quelle | Décision 5, § 3 ligne 3, § 6 point 11 |
| M-12, trois phrases du jury | appliquée telle quelle | § 4 ; « au-delà de zéro et de la prévision » pour suivre le traitement de B-2 |
| m-1, chiffres de puissance | appliquée telle quelle | § 2, § 3 ligne 3 |
| m-2, « demi-heure de carte » | appliquée (par B-2) | § 1 |
| m-3, effacement | appliquée telle quelle | § 1 point 2 |
| m-4, « Caught in the Act » | appliquée telle quelle | § 2 |
| m-5, deux travaux pris | appliquée telle quelle | § 2 |
| m-6, validation hors de nous | appliquée telle quelle | § 2, décision 6 |
| m-7, statut de la décision 5 | appliquée telle quelle | Décision 5 |
| m-8, noms des décisions | appliquée telle quelle | § 5, en-tête |
| m-9, invariant de la décision N-053 | appliquée telle quelle | § 3 ligne 6 |
| m-10, cadrage de la décision 3 | appliquée telle quelle | Décision 3 ; l'option b est récrite dans le même sens |
| m-11, sous-ensemble d'activations | appliquée telle quelle | § 2, données brutes |
| m-12, « 800 directions » | appliquée telle quelle | § 2 |
| m-13, incohérence de coût | appliquée, corrigée | « 17 à 48 » et non « 17 à 47 » : 34,0 à 37,4 plus 10 à 11 donne 44 à 48 (son § 2.8). Pire cas : § 6 point 8 |
| m-14, géométrie des poids | appliquée telle quelle | Décision 5 ; le « 0,079 » de la conception B n'est pas cité |
| m-15, définition de l'intensité | appliquée telle quelle | § 3 lignes 4 et 6, § 6 point 3 |
| m-16, partage de l'accord reporté | appliquée telle quelle | Décision 2, option a |
| m-17, chiffres de Fable dépassés | appliquée (par M-1, autrement) | § 6 point 1 |
| m-18, intervention | appliquée telle quelle | § 3 ligne 7 |
| § 1 du rapport, table des contrastes | appliquée, condensée | § 2 |
| § 2.5 du rapport, prévision | appliquée | § 2 ; arithmétique de la dose 1 refaite par moi |
| § 5 du rapport, options manquantes | appliquées | Décisions 1, 2, 4 |

Aucune remarque refusée.

## 8. Erreurs et écarts trouvés par moi, déclarés

1. **Fable.** La version 1 et la contre-lecture datent toutes deux l'état de Fable ; les deux sont dépassés. Fait relu : refus à 12:05Z et 12:20Z, réponses ensuite (traitement de M-1).
2. **Coût haut des paires.** « 47 USD » de la version 1 devient « 44 à 48 » (arithmétique du § 2.8 de la contre-lecture).
3. **Chiffres hors du résumé du socle.** 0,6871, 0,8793 (textes du saboteur relus sous le modèle nu contre l'honnête, doses 0,75 et 1) et 0,6991 viennent de la note 02 du socle (lignes 298 et 400), non de son résumé. Ce sont des valeurs de l'étape B bis ; je les ai gardées parce que B-1 et B-2 reposent sur elles. À toi de dire si la consigne « déjà dans le socle » les couvre.
4. **Lecture incidente.** Pour vérifier l'état de Fable, j'ai lu les lignes R-3791 à R-3823 de `registres/decisions.md`. Elles portent aussi sur d'autres chantiers, dont quatre lignes sur le saboteur à budget (conclusions de conception en simulation, sans fichier interdit ouvert, sans la ligne R-2059). Je n'en tire que l'état de Fable et la phrase ajoutée à la réserve 6.
5. **Recommandation de la décision 4.** Changée (voir M-6) : c'est un changement de fond, non demandé mot pour mot, que la remarque impose.
6. **Coupure de l'étape 4.** 8,5 USD (devis scellé) et non 9.
