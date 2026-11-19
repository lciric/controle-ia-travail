# Barreau 5 — comment le résoudre : note de synthèse pour Lazar (version 1)

- Écrite le 19 novembre 2026 par le synthétiseur (Claude Fable 5.2), à partir du socle des faits (`barreau5-comprendre/00-socle-des-faits.md`) et des trois conceptions indépendantes du dossier `barreau5-concevoir/` : A « le plus sûr avant l'entretien », B « l'identification propre », C « la validation hors de nous ». Pièce de travail, non scellée.
- Rien lancé, rien dépensé, rien commis. Aucun refus d'outil. Seuls chiffres de résultat : ceux de l'apprentissage des sondes sur la tâche (étape B bis), déjà dans le socle. Les puissances viennent de simulations à loi inventée (fichiers `puissance_conception_A_v1.py`, `simulation-puissance-B-identification-v1.py`, `simulation-puissance-C-externe-v1.py`, même dossier).

## 1. Le verdict en trois lignes

1. **Ta question en cache trois, et une seule se tranche avant l'entretien.** « La sonde ne lit-elle que la présence d'un adaptateur ? » se tranche à 0 USD sur les scores déjà gardés, plus une demi-heure de carte (5 USD au plus). « Lit-elle le sabotage, ou l'empreinte de cet adaptateur-ci ? » ne se tranche qu'avec plusieurs paires d'adaptateurs (saboteur et jumeau distillé de l'honnête, intensité mesurée égale) : après l'entretien, 18 à 47 USD. « Lit-elle l'acte, ou la disposition ? » demande un contraste à poids constants et une intervention.
2. **Ce qui ne peut pas le résoudre.** Le texte scellé de validité de l'adaptateur joué tel quel (il vise les sondes génériques, ne produit qu'un seul jumeau, ne garde aucune activation). Toute lecture de plus qui conclurait « sabotage » avec un seul adaptateur saboteur. Un effacement de direction jugé contre le modèle nu (0,80 à 0,97 d'aire sans aucun sabotage, en simulation).
3. **Avant le 1er décembre, les issues ne sont pas symétriques.** Un nul est une réponse ferme (« nous avons appris à lire l'adaptateur »). Un positif dit seulement « la présence de l'adaptateur n'explique pas tout » ; jamais « la sonde lit le sabotage ».

## 2. Les quatre points de ta demande, pris dans les trois plans

**Ce qu'un expert ferait.** Il commencerait par nommer l'unité. Le sabotage est donné à l'adaptateur par ses données de distillation, et il n'y a qu'un adaptateur saboteur : les 640 actions sont des mesures répétées d'une seule unité traitée (conception B). Il noterait aussi que la sonde a été apprise avec une étiquette confondue avec l'adaptateur : positifs sous adaptateur, négatifs sous le modèle nu (socle, point 0.3). Puis il poserait le plan à quatre cases (adaptateur présent ou absent, sabotage présent ou absent) avec plusieurs réalisations par case (conception C), et il apprendrait la sonde contre le jumeau honnête, jugée sur une paire jamais vue (conception B).

**Les données brutes de départ.** Tout est sur les branches, par action :
- les scores de l'apprentissage des sondes sur la tâche, 320 par groupe et par pli, pour six groupes : épisodes du saboteur, épisodes honnêtes, textes du saboteur relus sous le modèle nu, textes honnêtes relus sous l'adaptateur saboteur, épisodes de l'adaptateur témoin, textes honnêtes sous le témoin ; plus 800 directions aléatoires et la sonde jumelle du second ordre de calcul ;
- les poids des dix sondes, les deux adaptateurs, le coût déclaré de chaque action ;
- une seconde paire d'adaptateurs de la même recette, sur la course exploratoire.
Perdus : les activations complètes et les textes de distillation.

**Les méthodes.** Le meilleur de chaque plan :
- de A, le **plan factoriel déjà présent dans les scores gardés et jamais lu** : état (adaptateur, modèle nu) croisé avec texte (saboteur, honnête), sous la même sonde. Son contraste principal, épisodes du saboteur contre textes honnêtes sous le même adaptateur à la même dose, est centré sur 0,5 : il contourne le plafond qui a rendu muette la différence « texte égal moins adaptateur seul ». S'y ajoute la tendance du score avec l'excès de coût déclaré, à adaptateur fixé ;
- de A encore, **le défaut de ce plan** : son interaction est exactement confondue avec le chemin de calcul (deux cases par l'ancien chemin, deux par le neuf, jamais comparés aux doses 0,25 à 0,75). Une relecture des quatre cases par le même chemin le lève ;
- de B, **les paires répliquées** et le test exact par changement de signe, la mesure d'intensité comme condition de tout, et l'interdit sur l'effacement jugé contre le modèle nu ;
- de C, **l'épreuve à vérité plantée** du programme de lecture, et son résultat : un témoin à 90 % de l'intensité du saboteur donne 47,5 % de faux « au-delà de l'adaptateur ». Donc « saboteur au-dessus du témoin actuel » ne conclut rien.

**Ce qui validerait hors de nous.** Par force croissante :
- texte scellé avant lecture ; scores par action et programme publiés, recalculables sur un portable (A) ;
- épreuve à vérité plantée où le tiers tire lui-même le monde, et double programmation par l'autre modèle, accord à 10⁻⁶ près (C) ;
- relecture sur une autre pile logicielle (C) ;
- le précédent publié du contraste à adaptateur constant : « Caught in the Act », arXiv 2610.12445v1, page 26, vérifié sur PDF par le critique ; sa figure de tête porte elle-même la confusion que nous mesurons ;
- après l'entretien : rejouer la règle sur les organismes publiés par l'institut britannique de sécurité de l'IA (référence Cooney et al., 2606.12618, **non vérifiée sur PDF**), et un statisticien externe.

**Où les plans divergent.**
- *Peut-on apprendre quelque chose à l'intérieur de l'organisme ?* A : oui, « au-delà de la présence de l'adaptateur ». B et C : non pour « sabotage », parce que adaptateur et disposition sont la même variable par construction. Je retiens les deux : A répond à la première question, B et C à la deuxième.
- *Jouer le jumeau honnête du texte scellé avant le 27 novembre ?* A : oui si le code est prêt le 25. B et C : non. Je retiens non : un jumeau unique sans activation gardée ne permet aucun test, et son code disputerait la semaine à la lecture qui, elle, tient.
- *Combien de paires ?* B : six (test exact impossible sous cinq). C : quatre contre quatre par permutation (90 % de puissance pour un écart de 2,5 écarts-types entre graines, jamais mesuré). À fixer par devis après la première mesure de la variance entre graines.
- *Finesse du contraste principal.* A : aire détectable 0,62 à 0,68 contre un plancher de directions aléatoires supposé à 0,56. C : 0,55 à 0,60 contre 0,5, tâches appariées. Je garde le chiffre prudent de A.

## 3. Le plan retenu

### Avant le 1er décembre

| n° | étape | ce qu'elle tranche | données | coût | durée | puissance | tient ? |
|---|---|---|---|---|---|---|---|
| 0 | Tes décisions D1 à D3, **avant toute lecture** | rend valide tout le reste (aucune pièce lancée « sur la foi d'une sortie ») | — | 0 | 20 novembre | — | condition |
| 1 | Épreuve à vérité plantée du programme de lecture, double programmation | le programme distingue-t-il les mondes « adaptateur seul », « acte », « disposition », et tombe-t-il dans le piège de l'intensité | loi inventée | 0 | 20 au 23 | adaptateur seul retrouvé à 93,5 %, acte et disposition à 99,5 % | oui (routine) |
| 2 | Texte neuf court, scellé et contre-lu : « validité de l'adaptateur pour les sondes apprises sur la tâche », deux lectures déclarées d'avance | — | — | 0 | scellé le 23 ou le 24 | — | oui, si la conception se fait à temps (réserve 1) |
| 3 | Première lecture, au processeur : plan factoriel, tendance avec l'excès, saboteur contre témoin, géométrie des poids | la sonde ne lit-elle que la présence de l'adaptateur | scores et poids gardés, coût joint par clé, deux adaptateurs | 0 | lecture le 24 ou le 25, verdict par agent neuf | aire 0,62 à 0,68 à 99 % ; différence de deux aires 0,09 à 0,16 ; tendance 0,13 à 0,19 ; chaque ligne tenue seulement si la sonde et sa jumelle s'accordent | oui |
| 4 | Relecture sur carte, les quatre cases et le témoin par le même chemin, quatre doses ; intensité mesurée ; vecteur moyen par action gardé ; puis seconde lecture | lève la réserve de chemin de calcul ; donne la première mesure d'intensité | adaptateurs, textes, poids des sondes, module de relecture existant | 1 à 5 USD, plafond 5 | carte le 25 ou le 26, lecture le 27 | mêmes seuils, sans réserve | oui si D3 ; sinon l'entretien se fait sur la première lecture |

### Après le 1er décembre

| n° | étape | ce qu'elle tranche | coût | puissance |
|---|---|---|---|---|
| 5 | Relecture des quatre adaptateurs existants (course exploratoire comprise), sur une autre pile | première estimation de la variance entre graines ; transfert d'une sonde d'une graine à l'autre | 2,5 à 4,6 USD | deux saboteurs : aucun test, descriptif |
| 6 | Paires répliquées, saboteur et jumeau distillé de l'honnête, intensité égale, textes de distillation gardés ; sonde apprise contre les jumeaux, jugée sur une paire tenue à l'écart | **sabotage contre empreinte de l'adaptateur** : la question du barreau | 17 à 19 USD (trois graines sur deux tirages), 34 à 37 USD (six paires), 47 USD avec les épisodes générés | six paires : 0,88 à 0,99 pour un écart de 2 écarts-types entre graines |
| 7 | Contraste à poids constants, actions gonflées contre non gonflées, stratifié par tâche et cumulé ; intervention sur la direction lue, jugée par le coût, contre 19 directions aléatoires | acte ou trace ; lien causal | 6 à 20 USD | aire 0,57 à 0,60 ; baisse de 10 points vue à 0,98 |
| 8 | Organismes d'une autre main, statisticien externe | la méthode hors de notre fabrication | sur devis | — |

Le texte scellé de validité de l'adaptateur reste intact et non lu : lire ses lignes gratuites fermerait ses lignes payantes.

## 4. Ce qu'on dit au jury le 1er décembre

- **Rien de fait.** « Confusion mesurée, non levée : l'adaptateur seul déplace la sonde autant que l'organisme, et le contrôle qui trancherait est conçu, chiffré, non joué. »
- **Première lecture seule, nul.** « À adaptateur et dose fixés, la sonde ne distingue pas les épisodes du saboteur de textes honnêtes relus sous le même adaptateur, et ne suit pas l'excès déclaré : ce que nous avons appris à lire est la présence de l'adaptateur ; la cause est l'étiquette d'apprentissage, et la sonde suivante s'apprend contre un jumeau. »
- **Première lecture seule, positif.** « Un signal apparaît à adaptateur fixé, mais sous réserve de chemin de calcul : nous ne le retenons pas. »
- **Deux lectures, positif.** « La présence de l'adaptateur n'explique pas toute la lecture ; ne sont pas écartés l'empreinte du réglage fin, le texte propre de l'adaptateur, et le fait qu'il n'y a qu'un adaptateur. »
- **Deux lectures, signal au niveau du texte seul.** « Au-delà de l'adaptateur, la sonde lit le texte. »
- **Dans tous les cas.** « La question "sabotage ou adaptateur" exige des paires répliquées ; leur plan est scellé, sa puissance connue. »

## 5. Tes décisions

**D1 — Écrire un texte neuf pour les sondes apprises sur la tâche, et y réemployer les scores fermés.** *Nœud.*
- Enjeu : sans lui, aucune lecture gratuite n'est permise et rien ne change avant l'entretien.
- Option a, texte neuf, le texte scellé reste intact : répond à la question posée ; coûte quatre jours de chaîne complète.
- Option b, jouer le texte scellé tel quel : déjà contre-lu ; ne vise pas les sondes en cause, son aiguillage est inconnu.
- Option c, ne rien lire : aucun risque ; l'entretien se fait sur « non levée ».
- Recommandation : a, confiance haute. Défaut : aucun.

**D2 — Sort de l'accord de 30 USD (GO-2026-11-10-07, échéance le 27 novembre).** *Nœud.*
- Enjeu : il couvre deux pièces du texte scellé qu'aucun code ne peut lancer proprement d'ici là.
- Option a, le prolonger au 12 décembre et le reporter sur le texte neuf et les paires répliquées : garde la dépense ouverte sans course hâtive ; change l'objet de l'accord.
- Option b, jouer le jumeau honnête du texte scellé avant le 27 : consomme l'accord ; un seul jumeau, sans activation gardée.
- Option c, le laisser échoir : simple ; il faudra un devis neuf.
- Recommandation : a, confiance moyenne. Défaut : aucun.

**D3 — Dépenser 5 USD au plus pour la relecture par un même chemin (étape 4).** *Nœud de dépense, devis à écrire.*
- Enjeu : sans elle, un positif de la première lecture n'est pas lisible.
- Option a, oui, sur l'accord reporté : meilleur rapport du plan ; exige D1 et D2.
- Option b, non : 0 USD ; seule l'issue nulle sera dicible.
- Recommandation : a, confiance haute. Défaut : aucun.

**D4 — Taille des paires répliquées après l'entretien.** *Nœud de dépense et d'énoncé* (il donne le témoin apparié du brouillon de la décision N-074 pour la porte G1).
- Option a, six paires indépendantes, 34 à 47 USD : test exact valide ; dépasse 30 USD.
- Option b, trois graines sur deux tirages de données, 17 à 29 USD : tient dans 30 USD ; paires non indépendantes.
- Option c, attendre la variance entre graines de l'étape 5 puis demander le devis : dimensionné sur une mesure ; deux semaines de plus.
- Recommandation : c, confiance moyenne. Défaut : aucun.

**D5 — Niveaux et règles de lecture du texte neuf.** *Proposer avec recommandation.*
- Niveau 99 % par ligne ; ligne tenue seulement si la sonde et sa jumelle du second ordre de calcul s'accordent ; saboteur contre témoin et géométrie sans seuil ; à l'étape 4, vecteur moyen par action gardé à la couche retenue de chaque pli et à la couche 15.
- Recommandation : tel quel, confiance haute. Défaut sous 48 heures : appliqué.

**D6 — Validation d'une autre main (organismes publics, statisticien externe).** *Nœud* : rouvre la décision R-122, contact externe.
- Recommandation : après l'entretien, sur devis et licences vérifiées ; confiance moyenne. Défaut : aucun.

**Routine, sans ton mot** : l'épreuve à vérité plantée ; le code de lecture et ses essais sur scores factices ; la lecture des deux booléens de l'aiguillage du texte scellé par un agent autorisé ; les normes des adaptateurs.

## 6. Réserves et inconnues

1. **Calendrier, jamais compté.** Scellement le 23 ou le 24, carte le 25 ou le 26, verdict avant le 30 : aucune marge. Le socle consigne une limite d'usage de Fable jusqu'au 22 novembre à 18:00Z (R-3791) ; concevoir le texte neuf sur un autre modèle avant cette date serait un changement de modèle, donc ton mot.
2. **Variance entre deux adaptateurs de même recette : jamais mesurée.** Toute puissance de l'étape 6 est un pari sur elle.
3. **Intensité : mesurée pour aucun adaptateur.** Le témoin actuel n'est ni honnête ni étalonné.
4. **Réserves propres au contraste principal.** L'adaptateur lit son propre texte d'un côté, un texte imposé de l'autre ; les deux plis portent des sondes différentes et divergent souvent ; la dose 0,25 est instable ; à la dose 1 la différence de deux aires est marginale (place 0,12, seuil 0,09 à 0,16).
5. **Un seul mode de sabotage**, étiqueté par le coût déclaré et non par un oracle.
6. **Question à faire porter par une session autorisée** (je n'ai pas le droit de lire ces pièces) : le saboteur à budget ou le bras A font-ils varier le sabotage à poids constants par une variable que l'oracle connaît ? Si oui, c'est le meilleur banc pour ce barreau.
7. **État de l'art.** Effacement de concept (LEACE), comparaison de modèles, Cooney et al. : non vérifiés sur PDF. Aucune phrase « la séparation du comportement et de la trace de l'adaptateur est libre » : zone peu cherchée.
8. **Coûts** : ordres de grandeur tirés des devis scellés, à refaire en devis. Puissances : lois inventées.
9. **Ménage** : environ 100 Mo d'extraits restent sous `barreau5-comprendre/extraits/` ; leur effacement a été refusé par une garde et reste à faire par toi ou par la session mère.
