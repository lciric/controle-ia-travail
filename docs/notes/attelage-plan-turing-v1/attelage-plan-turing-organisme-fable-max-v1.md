# Attelage du plan Turing avant le lancement de l'organisme d'idéation : la cible, la vérité, les épreuves et l'ordre de montage — v1

- **Nature.** Pièce de travail (classe C), réponse à une demande approfondie du directeur. Elle ne décide rien, ne dépense rien et n'a rien modifié au dépôt. Les décisions qu'elle appelle sont au § 4.5.
- **Auteur.** Claude Fable 5.2, effort maximal, sous-agent de la session mère, 24 novembre 2026 (heure de fin relevée par `date -u`, en pied de pièce).
- **Demande, mot pour mot.** « il ne cherchera pas seul de manière efficace, il faut mettre en place l'attelage sophistiqué du plan Turing avant. demande à Fable [effort maximal] comment faire. » Précisions : « Définir la cible avant de construire le générateur. Que veut dire "découverte à fort impact" pour ce programme : exactement le genre d'idée que l'organisme avec le plan Turing est censé chercher, c'est-à-dire le pousser à chercher les puits étroits et profonds mieux que le hasard » ; le choix des problèmes se fait « en s'inspirant de tous les brainstorms d'hier et d'aujourd'hui = plan Turing ».
- **Lu.** Les pièces du mandat, les quatre pièces déposées par le directeur, puis, transmis en cours de travail, le registre des idées de la veille de cap et l'inventaire du bibliothécaire neuf, avec les pièces qu'il désigne comme socle ; la liste, avec empreintes, est en annexe. Noyau : la réponse du 23 novembre sur le modèle testable de l'idée intéressante (`reponse-fable-max-v1.md`, `8ec4f9e0…`) et sa provenance (`85b171ec…`).
- **Non lu.** Rien sous `archives-reponses-modeles`, aucun coffre, aucun score ni verdict cloisonné, aucune sortie brute d'une course de l'organisme.
- **Calcul.** Un seul, déterministe : `/tmp/claude-0/-home-user-controle-ia-travail/4bfc0ef9-1358-5ad4-b42a-4fb6de433e11/scratchpad/fable-attelage/calculs/calcul-dimensionnement-attelage-v1.py` (`462f382f…`), sortie `calcul-dimensionnement-attelage-v1-sortie.txt` dans le même dossier (`4ee1293a…`). Ses chiffres sont des ordres de grandeur sous hypothèses écrites, à refaire au préenregistrement.
- **En ligne.** Treize notices ou résumés consultés ce jour pour l'antériorité ; aucun PDF lu. Tout ce qui en vient est marqué « à vérifier sur PDF ».
- **Écarts déclarés.** Sous-agent à mandat étroit, en lecture seule : la routine de reprise (empreintes de lancement, tests, inventaire des machines) n'a pas été faite. Deux `git fetch` de branches distantes ont mis à jour des références de suivi du dépôt local, à la manière de la commande transmise par la mère ; aucun fichier suivi, aucune branche locale, aucun commit n'a été touché.
- **Réserve de lignée.** L'auteur est du modèle qui a écrit le modèle du 23 novembre et de la famille de plusieurs proposeurs de l'organisme. À faire contre-lire par une autre famille avant d'en tirer une pièce décisive.
- **Statut des références.** « Vérifié au dépôt » : lu ici dans une pièce du dépôt, chemin donné. « Rapporté par le dépôt » : lu sur PDF par un autre agent. « À vérifier sur PDF » : notice vue en ligne ce jour, ou mémoire.

---

# Partie 1 — Les quatre points

## 1.1 Ce qu'un expert du domaine ferait ici, et qui n'est pas demandé

1. **Poser la grandeur à estimer avant l'instrument.** « Chercher mieux que le hasard » n'est jugeable que si l'on a écrit : quel événement compte (une idée vérifiée, étroite, profonde), sous quel budget, contre quel hasard, avec quelle règle de décision. Sans cela, toute course se lit après coup.
2. **Séparer trois fonctions que la demande confond**, parce qu'elles n'ont ni le même hasard ni le même test : *choisir où chercher* (un classement de lieux), *faire naître l'idée dans le lieu* (la présence des pièces et l'émission du lien), *la reconnaître* (ne pas perdre ce qui est proposé). Puis localiser le goulot sur les journaux déjà produits, avant d'investir.
3. **Nommer la structure sur laquelle on parie.** Les séances du dépôt l'ont établi : sans structure, rien ne bat le tirage indépendant ; un attelage est un pari sur l'endroit où vivent les puits. L'expert écrit chaque pari (un parent existe dans une bibliothèque ; une anomalie désigne le lieu ; une correspondance de structure se prolonge), et l'éprouve sur des mondes qui ont cette structure **et** sur des mondes qui ne l'ont pas.
4. **Étalonner l'instrument sur une vérité plantée avant de mesurer le réel**, et valider le banc lui-même : la mesure de profondeur suit-elle la profondeur plantée ? Le classement obtenu sur mondes plantés prédit-il le classement sur des tâches exécutées ? Sinon le banc choisit pour le banc.
5. **Auditer le résolveur dans la queue.** Quand la fréquence des vraies idées rares est de l'ordre du taux de fausse acceptation du contrôle, la plupart des « découvertes » sont fausses. À fréquence 0,001, un contrôle qui accepte à tort une fois sur mille ne donne que 44 % d'acceptés vrais ; il en faut un à une fois sur dix mille pour 89 % (calcul, bloc 8).
6. **Dimensionner par la puissance, avec la famille de mondes comme unité.** Les puits étroits sont rares : peu d'événements, donc beaucoup de mondes, et une issue « non jugeable » écrite d'avance.
7. **Comparer à coût facturé égal, sous un plancher de bruit mesuré.** La veille du dépôt rapporte que l'écart médian publié entre méthodes est sous l'écart entre deux courses d'une même méthode, et qu'une proposition évolutive coûte environ six fois un tirage simple.
8. **Traiter le choix des problèmes comme une prévision** : ensemble à risque daté, négatifs compris (paires jamais nées, ponts morts), bases simples difficiles à battre (volume, ancienneté, attachement préférentiel, répartition des experts), règle de score fixée d'avance.
9. **Garder du hasard dans chaque course et journaliser les probabilités de choix.** Une part fixe du budget tirée uniformément donne à chaque course son propre témoin sans biais, et rend toute autre politique évaluable après coup.
10. **Tenir deux comptes** : la *récupération utile* d'un outil connu ailleurs et la *création* d'un objet neuf. Pour ce programme, la première est la plus proche et n'est pas un lot de consolation.
11. **Chercher les voisins avant d'écrire « neuf »**, et **écrire ce qui tue chaque pièce**.

## 1.2 Les données brutes qu'il prendrait au départ, au lieu de celles déjà analysées

- Les **graines et le code des générateurs** de mondes : la seule vérité connue par construction.
- Les **journaux bruts de l'organisme** (chaque proposition, son coût facturé, sa lignée, son sort à chaque étage), non leurs synthèses ; lus par un lecteur habilité, sans rien qui revienne à l'organisme.
- Des **graphes datés à horloge native** : le graphe de concepts daté de Gu et Krenn (une co-mention de deux concepts par article daté), les relations biomédicales typées de la base ouverte PubTator 3 jointes à une table de dates des articles, un banc daté écrit par des tiers (§ 3.4).
- Les **sources LaTeX de l'archive ouverte arXiv, en échantillon stratifié complet par année**, et non le fonds local du dépôt, constitué après coup (410 articles en aval contre 92 en amont dans la rétrodiction réfutée).
- Les **fils d'évaluation ouverte avec les refusés**, les essais arrêtés et les rétractations : les négatifs.
- L'**historique d'une bibliothèque formelle** et des **listes de problèmes ouverts avec leurs dates de résolution**.
- L'**extraction primaire** de la cartographie des verrous (`extractions-brutes-primaires-v1.json`, `catalogue-verrous-v1.json`), non son récit.
- Les **coûts facturés par le relais**, non déclarés par les agents.

## 1.3 Les méthodes et outils

- **Mondes** : générateurs par graine (`numpy.random.SeedSequence`), banc à deux processus (un joueur qui ne voit pas la clé, un noteur qui la tient), admission d'un monde par politiques témoins.
- **Cible** : modèle de surface logistique calibré ; signatures de rôle typées par raffinement de Weisfeiler et Lehman ; mise en correspondance de structures ou transport de Gromov et Wasserstein sur liste courte (bibliothèque Python Optimal Transport 0.9.7, relevée au conteneur) ; nul par recâblage à degrés et types constants ; compteur de Good pour la masse non vue.
- **Naissances datées** : modèle de Cox à covariables dépendant du temps, échantillonnage cas-témoins dans l'ensemble à risque, rééchantillonnage par concept.
- **Décision** : valeurs e et processus valides à tout instant, procédure de Benjamini et Hochberg en valeurs e, garantie disjonctive à zéro succès, intervalle entièrement d'un côté du seuil ou « non jugeable ».
- **Allocation** : éliminations successives, bandit visant le maximum, choix de la source par masse manquante majorée, part uniforme garantie.
- **Recherche dans un puits à parent lointain** : énumérateur mécanique des transferts (M lois × T^k renommages), ordre d'essai par longueur de description, appariement du grossier au fin en candidat.
- **Preuve** : assistant de preuve Lean 4.35.0 avec la bibliothèque Mathlib épinglée ; énumération exhaustive exacte en rationnels.

## 1.4 Ce qui, hors du directeur et du modèle, vérifierait la validité

1. **La graine**, tenue par un processus où aucun code écrit par un modèle ne tourne.
2. **Le noyau d'un assistant de preuve**.
3. **L'exécution sur instances cachées**, rejouée par un vérificateur d'une autre lignée.
4. **Le futur** : des prévisions scellées aujourd'hui, résolues par ce qui paraîtra. C'est la seule épreuve qu'aucune mémoire de modèle ne contamine.
5. **Des bancs et des partitions écrits par des tiers**, et des mondes écrits par une instance aveugle d'une autre famille.
6. **La contre-lecture par un autre modèle**, puis par d'autres familles au collisionneur ; des experts à l'aveugle si le directeur ouvre ce contact.

---

# Partie 2 — La demande reformulée

« Avant tout lancement de l'organisme d'idéation, spécifie l'attelage qui rend sa recherche mesurable et orientée, pièce par pièce et dans l'ordre de montage. (1) Définis la cible sans juge-modèle, en partant du modèle du 23 novembre (surprise de surface, serrure et clé, portée, cortège) : un puits étroit — faible masse d'accès sous un chercheur de référence figé, peu de correspondances qui tiennent — et profond — surprise retirée ailleurs, réalisée sur des faits tenus à l'écart ; définis le hasard dans le même espace et le test qui dit "mieux que le hasard" et "mieux que le meilleur modèle seul à coût facturé égal". (2) Dis quels mécanismes de choix des problèmes, tirés des remue-méninges des 23 et 24 novembre, survivent au double filtre "mesurable sans juge-modèle" et "comparé au hasard", et comment chacun s'éprouve comme une prévision. (3) Dis comment chaque source de vérité — graine d'un monde planté, passé daté, noyau d'un assistant de preuve, exécution — porte des puits étroits et profonds, et ce que la rétrodiction réfutée impose. (4) Donne les données brutes, leur horloge, leur licence, leur ingestion. (5) Donne les épreuves de l'instrument lui-même et les comparateurs. (6) Donne l'architecture de l'organisme attelé, ce qui remonte vers lui et ce qui ne remonte pas. (7) Range le tout du moins cher au plus cher, avec ce qui tue chaque pièce, le chemin minimal viable, des dates à partir du 2 décembre, les risques et le réemploi de l'existant ; dis franchement ce qui reste hors d'atteinte. Aucun chiffre sans source ; toute zone qui semble vierge est une question. »

---

# Partie 3 — Réponse : l'attelage

## 3.0 Verdict

1. **L'attelage, en une phrase.** Avant de produire, savoir mesurer trois choses sans juge-modèle : *où* sont les puits (un sélecteur de problèmes, éprouvé comme une prévision), si on les *trouve* mieux que le hasard (probabilité de découverte selon l'étroitesse, à coût facturé égal), si on les *reconnaît* (survie de puits glissés dans le flux).
2. **La cible est le modèle du 23 novembre rendu opérationnel** : une idée vérifiée, de forte surprise de surface (étroite), dont la serrure tient (viable), et qui retire de la surprise ailleurs (profonde). « Étroit » se définit contre un chercheur de référence figé ; « profond » contre un prédicteur de référence figé ; la fécondité est un critère différé.
3. **Ce qui manque à la charte du plan Turing** : la cible, le hasard de référence, et des mondes où des puits sont plantés. Le banc qu'elle prévoit plante des verrous dont la solution de référence est publiée : il mesure le rappel du bon outil, pas la découverte d'un puits.
4. **Une bonne part de l'attelage existe déjà, hors de la charte, et n'y est pas citée** : cinq décisions du 22 novembre sur ce que « forcer » veut dire, une conception du banc de recherche à lois plantées, un banc des correspondances plantées proposé le 24. L'inventaire du bibliothécaire le confirme : aucune épreuve de génération d'idées n'a encore tourné ; ce qui manque n'est pas une idée de plus, c'est l'assemblage et la première mesure.
5. **Sept mécanismes de choix des problèmes survivent au double filtre**, cinq attendent, cinq sont morts, rangés ou hors de la première version (§ 3.2).
6. **Le premier objet à concevoir est l'instrument, non l'organisme** : deux familles de mondes — des « mondes à puits » à étroitesse et profondeur réglées, des correspondances plantées dans un puits étroit — avec leurs témoins et leurs tests de mort. L'organisme attelé minimal n'y entre qu'après, contre sept comparateurs.
7. **Dates.** Instrument validé, banc vivant et courbe du hasard, sans dépense : vers le 10-12 décembre. Premier chiffre de l'organisme attelé : entre le 15 et le 19 décembre au plus tôt (§ 4).
8. **Franchise.** Aucun attelage ne certifie d'avance qu'un lieu réel contient un puits ; la rétrodiction longue ne vaut que pour des mesures sans modèle de langage ; la profondeur vraie se révèle sur des durées qu'aucune boucle ne couvre (§ 3.8).

### Ce que les textes corrigent dans la compréhension de la mère

La lecture en cinq pièces (a) à (e) est fidèle, à cinq corrections près.

- **(c) n'est pas dans la charte.** La note directrice n'a ni définition de la cible ni hasard de référence ; elle parle de « découvertes valides par dollar » sur le banc. Les mesures (étroitesse, profondeur, fécondité) viennent du modèle du 23 et des questions du 24, et le registre le dit lui-même : le plan « dit où chercher et comment juger, pas encore comment chercher dans un puits étroit » (R-5271). C'est la pièce à écrire en premier.
- **(a) : la « rétrodiction 7 sur 8 » de la cartographie n'en est pas une.** C'est un rappel sur huit transitions choisies par l'auteur, sans négatifs, sans taux de base, sans base concurrente (`temoins-externes-et-protocole-v1.md`, § 4). Elle contrôle le collecteur ; elle ne montre pas que la carte prédit où naissent les percées. La seule rétrodiction prédictive du plan (celle des foyers de tension) est réfutée. La cartographie vaut comme catalogue d'énoncés de verrous. Elle n'a pas été auditée ; la démonstration compagne du même agent, d'un autre modèle, l'a été : « tient avec réserves », quatre affirmations fausses (R-5254). Ses énoncés se revérifient donc avant de devenir des cartes servies.
- **(b) et (d) : le banc des verrous mesure le rappel.** Par construction du cahier des charges (§ 2), la solution de référence d'un monde est un optimum calculable ou une méthode publiée. Un modèle pré-entraîné peut la tirer de sa mémoire. Il faut des mondes dont la vérité sort d'une graine, et des verrous *ouverts* dont l'oracle sait calculer la valeur optimale sans connaître de forme close (§ 3.3).
- **Le mot « puits » désigne deux objets.** Dans le modèle du 23, un puits est une communauté du graphe d'usage, profonde quand on en sort rarement : c'est le bassin où marche le chercheur spontané. Dans les mots du directeur, c'est l'idée rare et de grande portée. Ils sont duaux : une idée est étroite d'accès *parce qu'*elle est de l'autre côté des bassins d'usage profonds de ses parents (ma lecture, à vérifier : la surprise de surface d'un pont est, au premier ordre, la somme des profondeurs de sortie des deux bassins).
- **Le « comment chercher » est en partie décidé, hors de la charte.** Cinq décisions du directeur du 22 novembre (synthèse du protocole X sur les puits étroits, § 9) : « forcer » veut dire une garantie de pire cas dans la grammaire publique, à prix affiché ; un bras sans modèle de langage est le premier essai et la base obligatoire ; les diagnostics bon marché d'abord ; le juge statistique ne guide jamais la recherche en course ; vérification sur PDF avant tout usage décisif. Et six amendements proposés le 24 par la réponse à la question sur le plan Turing, dont la recherche à deux niveaux et le banc des correspondances plantées. L'attelage les reprend.

### Ce que l'état des lieux du 24 novembre change

- **La première expérience du modèle du 23 n'est pas prête.** Le préenregistrement « le pont suit-il la carte ? », rédigé par Carbon, est jugé non scellable : six bloquants (script d'épreuve plantée introuvable ; relations sans date ; fécondité fondée sur des auteurs absents des données ; types de relation inexistants ; porte incompatible avec l'effet prédit ; règles de réfutation contradictoires). L'idée est saine ; le texte est à réécrire par Fable, après des faits de données qu'Opus peut établir avant le 2 décembre (§ 4).
- **Deux conceptions de bancs existent et ne sont pas codées.** Le banc de recherche à lois plantées, conçu le 21 novembre et vérifié « conforme » : générateur de mondes, oracle hors de la machine, treize épreuves d'admission. Il dit lui-même où il casse : un devin qui ne lit que la forme de la fiche obtient une aire de 0,69, au-dessus du plafond qu'il propose, de sorte que sa composition de fiche est à refaire. Dans les parties lues, il ne mesure ni portée ni fécondité. Et le banc des correspondances plantées, proposé le 24. La passe de conception de l'étape 1 est donc une extension de ces deux pièces, non une page blanche.
- **Rien n'attend le collisionneur groupé** (aucune cellule valide sur dix-huit) : l'attelage ne doit pas en dépendre.
- **La course principale d'auto-conception n'a ni table d'admission ni code.** Je ne la relancerais pas telle quelle : son socle (banc noteur, contre-calcul à l'octet, registre des tentatives) est celui de l'attelage ; un seul code suffit (§ 4.5, nœud 3).
- **Trois préenregistrements n'existent pas** (réanalyse des notes de Gu et Krenn, macros, scissions). Ils passent après l'instrument.
- **Le détecteur lexical est mort** ; ce qui le remplace doit être relationnel, daté, comparé à un nul.

## 3.1 Pièce 1 — La cible, définie en premier

### Trois objets figés par empreinte avant toute mesure

1. **L'espace** : une grammaire publique d'engagements *résolubles* (loi chiffrée, fonction à signature imposée, énoncé fini, prévision). Deux engagements sont « la même idée » s'ils ont la même signature de prédiction sur une grille publique de sondes : identité par ce que l'objet prédit, non par son texte ; signature numérique, car des verdicts binaires fusionnent toutes les vérités en une seule classe (défaut concédé au collisionneur du 22 novembre).
2. **Le chercheur de référence** : le meilleur modèle seul, consigne de référence, vue nue (ni carte de problème ni bibliothèque), une session neuve par appel. C'est lui qui définit « étroit ». La largeur n'est pas un bouton du générateur : c'est une propriété du triplet modèle, vue, archive, qui s'estime.
3. **Le prédicteur de référence** : ce que le savoir admis prédit déjà. Sur monde planté, la loi exacte sachant l'archive des lois connues — c'est le nul du juge de l'organisme, complété d'un panel de prévision au moins aussi informé que les proposeurs. Sur corpus, le modèle de surface ajusté avant la date de gel. C'est lui qui définit « profond ».

### Les coordonnées de la cible

| Coordonnée | Définition | Sur monde planté | Sur corpus daté | Nul de comparaison |
|---|---|---|---|---|
| **Étroitesse d'accès** | moins le logarithme de la probabilité qu'un appel du chercheur de référence produise l'idée : « peu de chemins y mènent » | estimée sur des mondes d'étalonnage, par famille de paramètres, jamais en retenant les graines où le témoin échoue ; masse non vue par le compteur de Good | surprise de surface S du modèle du 23 : moins le logarithme de la probabilité que le modèle de surface, ajusté avant la date, prête au lien | N tirages indépendants : 1 − (1 − w)^N |
| **Étroitesse de serrure** | part des correspondances voisines (une ou deux paires changées) dont le score de structure s'effondre : aiguille ou entonnoir | connue : nombre de renommages qui tiennent, sur M·T^k | perturbation de la meilleure correspondance | recâblage à degrés et types constants |
| **Viabilité** (serrure et clé, Z) | couverture moins conflits de la meilleure correspondance entre les voisinages typés des deux parents, centrée et réduite | exacte | signatures de rôle typées, puis transport sur liste courte | le même recâblage ; permutation de tous les types |
| **Profondeur** (portée, W) | surprise retirée ailleurs : gain de log-vraisemblance du prédicteur de référence sur des faits hors du voisinage de l'idée, terme d'unification compris, sans pondération par la centralité | exacte : gain dans les bassins que l'engagement n'a pas déclarés et dans un domaine masqué | *prévue* : surprise totale du cortège que la correspondance prédit (relations absentes entre images, objets sans image) ; *réalisée* : naissances de ce cortège, en écart à des paires croisées appariées | pont au hasard apparié en degrés et en dates, sans quoi la portée prévue ne lit que la taille des voisinages ; témoins à zéro (bruit, paraphrase, universel vide) |
| **Fécondité** (différée) | filles distinctes et vérifiées par service, en écart à une carte placebo de même longueur ; fécondité restante par le compteur de Good | filles plantées | rapport de taux du cortège ; liens futurs datés | appariement au hasard à dose égale |

Deux précisions qui viennent des pièces du 24. Perturber les *faits* éprouve la profondeur (sa robustesse) ; perturber la *correspondance* mesure l'étroitesse. Et l'étroitesse *dans les données* (un effet confiné à une région rare, que le juge dilue) reste une troisième grandeur, à ne pas confondre : elle relève du juge, non de la recherche.

La profondeur *prévue* est ma lecture du modèle du 23, non éprouvée : une correspondance qui transporte beaucoup de relations absentes et individuellement surprenantes annonce une grande portée. Elle hérite de la réserve de la réponse du 24 sur la portée : un lien nu ne retire jamais plus que sa propre surprise ; la portée vient du contenu transporté, donc de la somme sur le cortège.

### Définitions

- **Puits étroit et profond** : une classe d'engagements (i) résolue vraie par un résolveur qui n'est pas un agent ; (ii) étroite : le chercheur de référence, au budget facturé de l'épreuve, la trouve avec une probabilité sous un seuil gelé (proposition : 0,2) ; (iii) profonde : portée réalisée au-dessus d'un seuil gelé (proposition, sur monde planté : loi présente dans au moins quatre bassins sur huit, ou domaine masqué prédit). La viabilité est exigée comme garde : l'étroit sans serrure est du bruit, de forte surprise et de portée nulle.
- **Découverte à fort impact pour ce programme** : un puits étroit et profond situé sur la carte des verrous du contrôle — un engagement (statistique, règle, protocole, lemme) qui bat le plancher des méthodes connues sur des familles de verrous où il n'a pas été conçu, puis devient une épreuve, une sonde ou une cible de preuve.
- **Deux comptes, toujours séparés.** *Profond* : ce que l'idée vaut pour le programme, même si le modèle seul la trouve. *Profond et étroit* : l'apport propre de l'attelage. Un attelage qui ne trouverait que du profond large ne justifierait pas son coût ; il ne faut pas pour autant jeter ce profond-là.
- **Deux natures.** *Transfert* : le parent existe dans une bibliothèque lointaine (récupération utile). *Création* : objet hors de l'alphabet des relations. Le premier chiffre visé porte sur les transferts. Raison tirée du dépôt : dans la rétrodiction réfutée, les formalisations de 2025-2026 sont venues d'un outillage importé (jeux à meneur et suiveur, martingales de test), non des sous-domaines qui se plaignaient le plus. C'est une lecture après coup : une hypothèse pour le prochain préenregistrement, pas un résultat.
- **Étroit pour qui ?** Pour le modèle (chercheur de référence) et pour la littérature (modèle de surface) : deux mesures. Étroit pour le modèle seul : angle mort du modèle, récupération utile. Étroit pour la littérature seule : d'autres agents y arriveront, c'est une course. Étroit pour les deux : la cible.

### Le hasard dans le même espace, et le test

Trois hasards, tous exécutés et non seulement calculés, dans la même grammaire et notés par le même oracle :

1. **le tirage uniforme dans la grammaire** (production par production) ;
2. **l'énumérateur mécanique par longueur de description** : il dit jusqu'où la force brute suffit ;
3. **le chercheur de référence tiré N fois à coût facturé égal** : c'est « le meilleur modèle seul ».

S'y ajoutent une boucle simple qui réinjecte le meilleur, et un **attelage placebo** (mêmes rouages, cartes leurres ou bibliothèque sans rapport), qui sépare ce que porte la carte de ce que porte la machinerie.

Les deux premiers ne sont pas seulement des témoins : eux seuls *forcent*. Une part ε du budget donnée à un tirage mécanique sur la grammaire assure à chaque classe une probabilité d'au moins ε fois sa masse sous ce tirage, quel que soit le modèle de langage. C'est la garantie de pire cas des décisions du 22 novembre, à prix affiché : la force brute, diluée par ε, et sur la proposition seulement. Tout le reste de l'attelage est un pari sur une structure, à mesurer.

**Grandeur principale.** Par famille de mondes (l'unité statistique), la part des puits étroits et profonds plantés que la méthode retrouve dans le budget facturé, moins la même part pour le chercheur de référence, sur les mêmes mondes et les mêmes graines (plan apparié). L'appartenance d'un puits à la strate est fixée avant la course, par les boutons du générateur et par l'étalonnage du chercheur de référence sur des mondes disjoints de ceux de l'épreuve. Sans cette disjonction, la strate ne serait que l'ensemble des endroits où il a manqué de chance, et tout comparateur y paraîtrait meilleur.

**Règle de décision.** Un paramètre, une marge d'utilité fixée d'avance par le directeur, un intervalle entièrement d'un côté ; chevauchement : « non jugeable ». Garde conjointe : les fausses promotions, lues sur des mondes où toute promotion est fausse et sur des tricheurs scellés, ne montent pas au-delà d'une marge.

**Lectures secondes** : la courbe de découverte selon l'étroitesse, par méthode (c'est la courbe dose-réponse des séances du 13 novembre, avec l'étroitesse *estimée*) ; le même compte par dollar ; le facteur d'allumage où le gain se produit (présence, émission, reconnaissance, poursuite).

**Ordres de grandeur** (calcul, blocs 1 à 3). Un puits de masse 0,001 par appel est trouvé 18 fois sur 100 en 200 tirages indépendants ; doubler la masse par appel porte à 33, la quintupler à 63. Distinguer 18 de 63 demande une quinzaine de mondes par bras ; distinguer 18 de 33 en demande une centaine (bras indépendants, test unilatéral à 5 %, puissance 80 % ; un plan apparié en demande moins). Avec douze familles de vingt-cinq mondes et une corrélation de 0,2 dans la famille, l'effectif efficace tombe à une cinquantaine. Conséquence : il faut un générateur de *familles*, pas une poignée de mondes écrits à la main.

### Pièges de la définition

- Le rare n'est pas le profond : la conjonction avec la portée et le rapport de la portée à la surprise écartent le bruit et l'universel vide.
- La rareté mesurée dans l'échantillon d'un bras se fabrique par dilution : elle se mesure sur un panel de tirages de référence gelé et disjoint.
- Pondérer la portée par la centralité fait revenir le nœud par la fenêtre : mesure principale non pondérée.
- Le chercheur de référence change avec les modèles : il est figé par cycle et nommé dans tout résultat.

## 3.2 Pièce 2 — Le choix des problèmes

**Principe.** Un mécanisme de choix est un *sélecteur* : il classe des lieux (un verrou, une anomalie, une paire de concepts, un énoncé) avec la seule information disponible avant la recherche. Il s'éprouve comme une prévision : les puits réalisés ou plantés sont-ils enrichis dans ses premiers rangs, contre un tirage au hasard dans le même vivier et contre les bases simples ? Le score de rang que le modèle du 23 fournit est l'intérêt prévu : crédibilité (fonction de la viabilité et de la surprise) multipliée par la somme de la surprise et de la portée prévue.

| | Mécanisme et source | Mesurable sans juge-modèle | Comparé au hasard et aux bases | Sort |
|---|---|---|---|---|
| 1 | **Interaction de la surprise et de la serrure** : la distance de surface ne paie que si les structures s'emboîtent (réponse du 23, § 2 et 7 ; fiches 001, 003 et 020 du registre du 23) | oui : relations typées, recâblage | cas-témoins dans l'ensemble à risque ; attachement préférentiel, voisins communs, plongements, répartition des experts | **garder**, premier rang ; préenregistrement à réécrire, avec une spline de distance dans le modèle des naissances et la permutation des signes à côté de celle des types : elles départagent, sans coût, la cloche à optimum fixe de Carbon et l'optimum mobile du modèle du 23 |
| 2 | **Cortège et trous d'une correspondance** : après un pont vérifié, chercher les relations absentes entre images et les objets sans image (réponse du 23, § 7 C ; complément de la mère sur les quatre cas ; question du 24 sur la forme d'une anomalie, en attente) | oui | paires croisées appariées, et paires jamais pontées (différence de différences) | **garder**, premier rang |
| 3 | **Couche des problèmes pondérés** : anomalies et questions ouvertes, pesées par écart, résistance, portée, maturation, couplées au taux de naissance (réponse du 24 à la question 7 ; fiche 017) | oui si l'anomalie est relationnelle (conflits de signe entre groupes indépendants) | faux problèmes à activité égale ; signes permutés | **garder**, sous garde de mesurabilité d'abord |
| 4 | **Cadres en croissance** : un instrument ou un formalisme dont la part monte rend deux domaines comparables (champ du modèle du 23 ; seconde définition de la note des hypothèses, § 3.5) | oui : part annuelle des documents qui citent la méthode | activité seule | **garder** comme covariable ; les deux définitions sont concurrentes |
| 5 | **Résidus du prédicteur de référence** sur les expériences de l'organisme lui-même : chercher là où le savoir admis prédit mal (avis du 24, § 9.5) | oui ; exact sur monde planté | lieux tirés uniformément | **garder** |
| 6 | **Masse manquante par source et par vue** : servir la source dont la part de classes vues une fois est la plus haute (remue-méninges du 13, E1 ; réponse du 22, § 7) | oui | répartition égale | **garder** pour l'allocation |
| 7 | **Liste des paires non croisées par l'archive, plan des focalisations** (collisionneur des bassins étroits, V2 et V3) | oui | vue nue à jetons égaux ; placebo de même forme | **garder** : c'est l'inconnue centrale, « la vue déplace-t-elle la loi des propositions ? » |
| 8 | **Compression sur plusieurs bassins** : un modèle propose une abstraction, un compresseur de bibliothèque ne garde que ce qui raccourcit plusieurs bassins éloignés (fiches 031 et 043) | oui : bits gagnés, par programme | abstractions au hasard ; bassins permutés | **attendre** l'audit de réemploi ; puis opérateur et estimateur de profondeur |
| 9 | **Scission d'une fausse identité** (fiches 006, 014, 033) | oui si l'événement est désigné par règle (scissions de descripteurs du vocabulaire d'indexation de PubMed, par année) | polysémies banales | **attendre** un préenregistrement ; opérateur déjà plantable (monde « empreinte de recette contre acte réel ») |
| 10 | **Inflation descriptive et entropie des notations** dans les sources LaTeX (signaux 1 et 3 de Carbon ; fiches 030 et 032) | oui | volume | **attendre** : énoncé d'un seul modèle ; un cas historique unique est une anecdote ; il faut d'abord un monde de signaux plantés, puis un ensemble à risque (toutes les rubriques nouvelles d'une classification) |
| 11 | **Marchepieds et frontière de l'archive** sur plusieurs générations | oui | meilleur de N à coût égal | **attendre** un levier montré par la ligne 7 |
| 11 bis | **Cinétique des collisions d'idées** : le taux de naissance lu comme une loi d'Arrhenius ; dans l'organisme, la température d'échantillonnage est une vraie température, la barrière s'y mesure et un catalyseur se sépare d'un simple préfacteur (réponse du 24 à la question 3) | oui, sur mondes plantés : quatre températures, catalyseur présent ou non, trois concentrations | étiquettes de température permutées | **attendre** l'étape 7 : c'est une mesure de l'organisme, non un sélecteur ; puissance annoncée de 0,96 à 12 800 collisions par sa simulation, non relue ici |
| 12 | **Détecteur lexical de tensions** | — | battu par le hasard, le volume et l'ancienneté | **mort** (rétrodiction réfutée) |
| 13 | **Fenêtre fixe de distance** entre parents | — | ne teste jamais hors de sa bande | **morte** comme règle ; a priori réversible seulement |
| 14 | **Détecteurs sémantiques par modèle de langage** des signaux précurseurs dans la littérature d'alignement (fiches 041 et 051) | non en rétrospectif : le modèle connaît la suite | — | **prospectif seulement** (§ 3.8) |
| 15 | **Transition de phase, percolation, ensemble autocatalytique** | la clôture naïve est triviale, le taux de reproduction est fixé par la dose | — | **rangé** ; l'ablation du catalyseur reste une mesure de fécondité |
| 16 | **Signal interne de surprise, symétries du langage, plasticité d'un graphe** | lecture de l'erreur de prédiction à moins de 0,4 de corrélation de rang, jamais sur tâches ouvertes ; les plongements sont la base de surface à battre ; la plasticité est une question en cours | — | **hors de l'attelage v1** |

**Le vivier réel des lieux** existe : les dix-huit verrous du catalogue et les six cibles du pilier mathématique ; les quatre-vingt-treize idées des mentors, versées comme matière première (N-072). **La bibliothèque des parents lointains** existe en germe : l'audit de réduction hors du domaine de la cartographie liste, verrou par verrou, les théorèmes classiques qui en résolvent une part. La typer (ce qu'un outil garantit, sous quelles hypothèses) est le premier travail du cartographe.

## 3.3 Pièce 3 — Les sources de vérité

| Source | Ce qu'elle tranche | Comment elle porte des puits étroits et profonds | Piège principal | État |
|---|---|---|---|---|
| **Graine d'un monde planté** | la découverte d'une loi cachée | boutons réglés (ci-dessous) | raccourci du générateur ; rappel d'une méthode publiée | conçu en partie, non codé ; extension à concevoir |
| **Valeur optimale calculable d'un verrou ouvert** | la qualité d'une règle, sans connaître la bonne | l'oracle calcule l'optimum exact sur petits paramètres ; la proposition est une règle en forme close, notée sur des tailles non servies | surajustement aux petites tailles | cinq miniatures exactes au catalogue ; deux familles dans le générateur du pilote mathématique |
| **Passé daté** | un sélecteur de problèmes | percées désignées par règle (ci-dessous) | mémoire des modèles ; biais du survivant ; registre disciplinaire | données identifiées ; aucun texte scellable |
| **Noyau d'un assistant de preuve** | la vérité d'un énoncé fini | portée = cibles scellées devenues démontrables quand le lemme entre dans la bibliothèque | énoncé infidèle ou vide ; connu reformulé | outillage au quatrième essai |
| **Futur** | l'information qu'une idée porte sur l'avenir | prévisions scellées | lenteur | à ouvrir |

### Mondes à puits : comment planter l'étroit et le profond

Le socle existe : le générateur du banc de recherche à lois plantées (graphe de causes, lois tirées d'une grammaire, fausses lois tentantes nées de la structure, six molettes de difficulté) et ses trois règles de construction — une bande vide entre le vrai et le nul, rien de ce qui est servi n'est fonction de la vérité, la composition se tire. Il lui manque ce que la cible demande, la portée et l'accès ; c'est le trou que l'inventaire relève : aucune pièce ne définit un monde concret qui mesure la portée ou la fécondité. L'extension : une famille de mondes à huit bassins de vocabulaires disjoints, des lois locales, une archive de lois connues servie, et les boutons suivants.

| Bouton | Ce qu'il règle | Valeurs |
|---|---|---|
| Portée | la loi mère est plantée dans k bassins sous des habillages différents, plus un domaine masqué jamais servi | k de 1 à 8 |
| Longueur sachant la bibliothèque | le parent est ou non dans une bibliothèque de M lois ; renommage de k traits parmi T | parent présent ou absent ; k de 1 à 3 |
| Trace d'ordre inférieur | la loi laisse ou non un effet marginal détectable (barrière de parité) | présente, absente |
| Chaîne | nombre de marchepieds sans valeur immédiate avant le puits | 0, 1, 2 |
| Ressemblance de surface | le parent ressemble ou non à la cible en surface | présente, absente |
| Confinement | part des données où l'effet vit | 1 ; 0,2 ; 0,05 |
| Piège | un bassin large et peu profond, bien noté à court terme, coexiste avec le puits | présent, absent |
| Filles | lois qui ne valent que sous la mère | 0, 2, 8 |

**Leurres**, sans lesquels le banc récompense la rareté : l'aiguille stérile (rare, de portée nulle) ; le large et profond (pour le premier compte) ; le faux profond (un « universel » qui tient sur les bassins servis et casse dans le domaine masqué) ; la mère générique à filles triviales ; les mondes sans aucun puits.

**Mémoire contre compétence.** Plan deux sur deux : lois historiques déguisées contre lois tirées de la grammaire, avec ou sans modèle pré-entraîné. Sans lui, un succès sur loi historique ne dit rien.

**Admission d'un monde**, à la manière publiée par un banc voisin (Openhagen Worlds, rapporté par la veille) : la politique qui connaît la graine réussit au-dessus d'un plancher, la meilleure politique sans déduction et chaque raccourci restent sous un plafond. Les raccourcis à écrire comprennent la **forme seule** : dans le générateur du pilote mathématique, un classifieur de style sépare déjà le vrai du faux avec une aire de 0,94 à 0,98, au-dessus du seuil d'emploi de 0,75 (passation du 22 novembre). Le raccourci de forme est donc réel, et mesurable.

**Qui écrit.** Le générateur par graine pour les mondes de conception ; une instance aveugle d'une autre famille pour les familles tenues à l'écart, aveugle aux cartes et aux candidats. Un lot tiré du même générateur ne voit pas un raccourci propre à ce générateur (décision sur les revendications resserrées, N-073, § 4) : le générateur est donc audité sur ses seuls traits de présentation avant toute banque sœur, et la banque de confirmation finale vient d'un générateur distinct.

### Correspondances plantées : comment chercher dans un puits étroit

C'est le second niveau de la recherche, que la réponse du 24 à la question sur le plan Turing sépare du premier. Une fois le lieu choisi (quelle paire essayer), il reste à trouver la correspondance entre les deux voisinages : un problème d'affectation quadratique, dont le paysage a précisément des puits étroits. Le banc, sur processeur pour tous ses bras sauf le dernier :

- **Mondes** : une correspondance vraie isolée près d'un leurre large de même masse ; une relation qui correspond à une chaîne de deux ; un leurre de popularité (grands modes communs, structure fine différente), témoin qui doit tuer une méthode spectrale non normalisée.
- **Bras** : la base sans modèle (énumération, programme linéaire en nombres entiers exact sur petits voisinages) ; criblage par signatures de rôle ; transport régularisé à régularisation décroissante, puis arrondi ; appariement du grossier au fin par les modes propres ; recuit ; proposeurs divers.
- **Mesure** : correspondances retrouvées et coût par correspondance, selon l'étroitesse de serrure plantée.

Ce que les sources lues par la réponse du 24 laissent attendre, et que le banc doit confirmer ou démentir : l'appariement du grossier au fin se ramène à une seule résolution linéaire pour des formes presque isométriques (Ovsjanikov et al., lu sur PDF par elle), mais deux domaines éloignés ne le sont pas, et les grands modes d'un graphe de concepts codent d'abord communautés et popularité ; le transport régularisé ne trouve qu'un point stationnaire ; le recuit n'est sûr qu'à refroidissement logarithmique, donc en temps exponentiel, et mélange lentement quand un pic étroit voisine un pic large de même masse. Aucun de ces bras ne se dira « forcer ».

### Signaux plantés : avant toute carte des tensions

Un petit monde où une vraie anomalie (elle survit aux remesures) et un leurre (il disparaît) sont plantés, ainsi que des signaux précurseurs vrais et faux. Aucune version relationnelle des signaux précurseurs ne s'applique à la littérature avant d'y avoir retrouvé ce qui est planté.

### Verrous ouverts : là où une découverte pour le programme peut sortir

Pour l'agrégation d'un panel de moniteurs sous corrélation en partie contrainte, ni les bornes de Fréchet et Hoeffding ni la fusion de Vovk et Wang ne donnent la règle (catalogue, verrou 6). Mais la programmation linéaire exacte donne la *valeur* optimale sur petit support : le générateur du pilote mathématique le fait déjà en rationnels (famille « agrégation à marges fixées »). Une règle en forme close proposée par l'organisme se note donc exactement, sur des tailles et des contraintes qu'elle n'a pas vues. Si elle approche l'optimum partout, c'est une conjecture sérieuse, à porter à l'assistant de preuve. Aucune mémoire ne peut la fournir si le noyau est réellement ouvert — ce qui reste à vérifier sur PDF, verrou par verrou.

### Rétrodiction à coupure temporelle : désigner les percées par une règle

Trois régimes, à ne pas mélanger.

1. **Longue, sans modèle de langage** (gel en 2010 ou 2014, suivi sur dix ans) : elle valide les *mesures* et les *sélecteurs* algorithmiques. Elle ne dit rien de l'organisme.
2. **Courte, dans la fenêtre entre la date de coupure d'un modèle et aujourd'hui** : quelques mois de publications ; seule rétrodiction licite pour un organisme à modèles de langage. La consigne d'ignorer ce qu'on sait ne vaut rien (écart de 52 %, dossier sur la structure du langage, § 6.3). Voisin à lire : la redécouverte d'hypothèses de chimie publiées après la coupure (MOOSE-Chem, à vérifier sur PDF).
3. **Prospective** : scellée aujourd'hui.

**La règle de désignation**, fixée avant toute lecture : un *événement* est une naissance datée (premier lien typé entre deux concepts jamais reliés avant le gel ; ou problème d'une liste datée, résolu). Il est **étroit à la date du gel** si sa surprise de surface, calculée sur les seules données antérieures, est dans le décile supérieur de l'ensemble à risque ; **profond** si la portée réalisée de son cortège, en écart à des ponts au hasard appariés, est dans le décile supérieur. Le sélecteur ne voit que l'avant ; l'étiquette vient de l'après ; l'ensemble à risque contient les paires jamais nées.

**Cinq leçons de la rétrodiction réfutée** (rapport du premier rang, `0a617ab1…`) :
- l'unité est la paire ou le lieu, avec effets fixes par champ : onze sous-domaines ne séparent pas un signal d'un registre disciplinaire ;
- la cible se définit par un événement daté, non par une densité de vocabulaire formel, elle-même affaire de registre ;
- le corpus est un échantillon stratifié complet par année, non un fonds constitué après coup ;
- le signal est relationnel (résultats chiffrés incompatibles sur une même cible, conflits de signe), en différence dans le champ ;
- les bases se rapportent toujours : l'ancienneté seule atteignait une aire de 0,86 dans une des partitions.

### Preuve formelle et épreuves exécutables

Le noyau tranche la vérité d'un énoncé, jamais sa nouveauté ni sa profondeur : la portée s'y mesure par ablation (cibles scellées démontrées avec et sans le lemme, à budget égal). L'outillage a rendu « noyau 18 sur 18 » au quatrième essai, avec un cas d'épreuve en écart toléré (R-4684, R-4716). Le pilier « génération » reste fermé par décision, et l'inventaire dit l'assistant de preuve bloqué pour l'organisme par un garde-fou d'exécution (à vérifier) ; y prendre des cibles finies avant l'heure est un nœud (§ 4.5). Les épreuves exécutables reprennent l'interface du cahier des charges : proposition en forme fermée, banc joueur et banc noteur, tests de mort.

## 3.4 Pièce 4 — Données brutes et ingestion

| Donnée | Ce qu'en dit le dépôt | Ingestion | Verrou |
|---|---|---|---|
| Graphe de concepts daté de Gu et Krenn | dépôt Zenodo 13900962, licence CC BY 4.0, archive de 3 018 689 216 octets, 375 fichiers ; colonnes : deux concepts, date en jours depuis 1990, citations par année (fiche de faisabilité, `1736e5f0…`) | lecture par morceaux sur processeur ; 4 cœurs, 15 gigaoctets de mémoire, 50 de disque relevés | pas de relations typées : sert la surprise et le cortège non typé, pas la serrure |
| Notes d'intérêt de Gu et Krenn | 2 996 idées sur paire, 144 traits ; l'identité des deux concepts n'est probablement pas publique (même fiche) | à vérifier après scellement | sans identités, le calcul de rôle par paire n'est pas faisable tel que proposé |
| Relations typées de PubTator 3 | fichier de 288 mégaoctets, domaine public, quatre colonnes, **aucune date** ; huit types listés dans le fichier, douze dans l'article selon la réponse du 24 à la question 7 : à trancher à la source | jointure avec une table de dates des articles | nommer et empreinter la source des dates et des auteurs ; candidats : instantanés de la base de citations iCite des instituts américains de la santé (identifiant d'article, année, auteurs : notice vue ce jour, à vérifier), ou fichiers annuels de PubMed |
| Banc daté écrit par des tiers | graphes annuels de cooccurrence de 65 027 sous-domaines, de 1827 à 2024, partitions et code publics (FOS, arXiv 2511.18631 : résumé vu ce jour, licence et PDF à vérifier) | téléchargement | sert les bases de surface, pas la serrure |
| Sources LaTeX d'arXiv | l'accès en masse est en compartiments payés par le demandeur (page d'arXiv vue ce jour) | échantillon stratifié par année, par l'interface article par article, à débit limité | l'archive entière est une dépense : nœud |
| Graphe bibliographique OpenAlex | clé d'interface obligatoire depuis février 2026, palier gratuit ; instantané gratuit mais volumineux (pages vues ce jour, à vérifier) | clé gratuite, ou rien | création de compte : nœud |
| Historique de Mathlib | graphes de dépendances publiés par des tiers en 2026 (notices vues ce jour, à vérifier) | à dimensionner | la prédiction du réemploi futur n'a pas été trouvée publiée : une question, non un trou |
| Problèmes ouverts datés | carnet de Kourovka, versions depuis 1965 (réponse du 24 à la question 7) | extraction par règles | petit effectif |
| Scissions de concepts | versions annuelles du vocabulaire d'indexation de PubMed (réponse du 23, § 3) | non essayé | — |
| Négatifs | registre d'essais cliniques, rétractations, articles refusés des fils d'évaluation ouverte | par interfaces publiques | aucun catalogue d'analogies ratées : à construire |
| Journaux de l'organisme | cloisonnés | lecteur habilité | rien n'en revient à l'organisme |
| Carte des verrous | catalogue de 18 verrous et extraction primaire | revérification avant service | jamais auditée ; quatre affirmations fausses relevées dans la démonstration compagne du même agent |

**Règles d'ingestion** : chaque source nommée et empreintée ; date manquante = exclusion, jamais imputation ; identifiants d'aujourd'hui appliqués au passé déclarés comme limite ; aucun modèle postérieur à la date de gel dans une extraction rétrospective ; comptage des effectifs à l'aveugle des issues avant tout scellement.

## 3.5 Pièce 5 — L'évaluateur d'abord, puis les comparateurs

**Huit épreuves de l'instrument**, sur processeur et avant le premier appel payant, sauf mention :

0. **Diagnostics bon marché** (décision du 22 novembre) : audit formel de la grammaire ; collisions et autocorrélation des propositions, sur les journaux déjà produits ; puis, au premier budget pilote compté, l'indépendance des tirages, car des tirages qui partagent un état caché plafonnent la découverte même à budget infini — part des campagnes sans aucun succès en session continue contre sessions réinitialisées, avec un mélange à état caché planté comme contrôle positif.
1. **Tests de mort de chaque monde** : la référence passe, la base naïve meurt, la fuite de clé est prise, la difficulté se règle de façon monotone, deux exécutions rendent le même octet ; le devin de la forme reste sous son plafond.
2. **Tests de mort du banc** : un juge faible qui voit tout ne classe pas comme l'oracle ; un proposeur faible n'égale pas le fort ; un oracle qui fuit est pris ; un proposeur au hasard ne franchit aucun seuil ; une recette fixe ne gagne pas sur les mondes tenus à l'écart.
3. **Validation de la mesure de profondeur** contre la portée plantée : corrélation de rang, réponse croissante avec le nombre de bassins, corrélation partielle avec le degré du parent proche de zéro, témoins à zéro (seuils de la réponse du 24 à la question 2, à geler).
4. **Validation de la mesure d'étroitesse** : la masse estimée du chercheur de référence suit-elle les boutons ? Courbe plate : la définition de la largeur est fausse, et il vaut mieux le savoir là.
5. **Répétition générale de la chaîne entière** sur des objets à issue connue, jouée par des proposeurs scriptés. Zéro fausse admission sur n mondes sans structure borne le taux à 1 % pour n = 300 et à 0,3 % pour n = 1 000 (calcul, bloc 4), non à zéro.
6. **Audit du résolveur dans la queue** : son taux de fausse acceptation, mesuré sur des négatifs, doit être très inférieur à la fréquence des puits.
7. **Plancher de bruit** : deux courses du même bras ne doivent pas différer ; le nombre de courses se fixe par la puissance.

**Comparateurs**, tous à coût facturé égal, sur les mêmes mondes et les mêmes graines :

| Comparateur | Ce qu'il isole |
|---|---|
| tirage uniforme dans la grammaire | les seuils sont-ils trop bas |
| énumérateur mécanique par longueur | jusqu'où la force brute suffit ; à partir d'où un modèle a quelque chose à apporter |
| chercheur de référence tiré N fois | l'apport propre |
| boucle simple qui réinjecte le meilleur | ce qu'ajoutent rôles, archive et générations |
| même effectif sans échange | ce qu'ajoute la communication |
| attelage placebo (cartes leurres, bibliothèque sans rapport, carte recâblée à degrés et dates constants) | ce que porte la carte |
| verdicts permutés rendus à l'organisme | l'organisme lit-il le retour (des agents publiés ne bougent pas quand on permute les étiquettes : Gupta, Hartford et Liu, à vérifier sur PDF) |

## 3.6 Pièce 6 — L'organisme branché sur l'attelage

**Un noyau minimal, gelé avant mesure**, plutôt que l'orchestrateur complet, dont la boucle n'a jamais tourné avec de vrais agents (programme de l'organisme v3, verdict) :

1. **Un cartographe**, qui est un programme : il sert des cartes de problème typées, figées par empreinte, et y joint la pièce lointaine (un parent de la bibliothèque) choisie par un moyen qui ne dépend pas du goût du modèle — criblage par la serrure, ou énumération. C'est le levier le plus fort mesuré dans la réponse du 22 : sans la pièce dans le contexte et sans indice, le lien n'est pas émis.
2. **Des proposeurs**, indépendants, sans vue des autres ni d'aucune note, qui écrivent dans la langue du résolveur ; et deux **espèces sans modèle**, l'énumérateur et le tirage uniforme.
3. **Des réfutateurs** d'une autre lignée, avec le droit d'exécuter.
4. **Des résolveurs qui ne sont pas des agents** : banc noteur, noyau de preuve, juge statistique au nul formé des lois connues. Eux seuls rendent des verdicts.
5. **Un registre et une bibliothèque écrits par programme** ; un modèle peut proposer une abstraction, seul le réemploi mesuré l'admet.
6. **Un répartiteur** : éliminations successives sur les issues résolues, choix de la source par masse manquante, **part uniforme garantie** (proposition : un dixième à un cinquième du budget) tirée sur les lieux et les opérateurs, probabilités de chaque choix journalisées.

Les **opérateurs** (transfert par serrure, explication d'une anomalie, scission, compression entre bassins, libre) sont des bras à rendement mesuré, chacun avec son bras hasard ; aucun n'est un principe.

**Ce qui, là-dedans, pousse réellement vers l'étroit**, par ordre de solidité. (1) La part mécanique : une garantie, au prix de la force brute. (2) La pièce lointaine servie avec un indice : une analogie employée 1 fois sur 15 sans indice et 15 fois sur 15 avec, chez un modèle, sur un problème ; mais une analogie sur deux y est fausse, d'où le résolveur. (3) Les décisions d'exploration sorties du modèle : un agent seul trouve l'optimum d'un réglage simulé 2 % des fois, le hasard uniforme 42 %, une optimisation classique 73 %. (4) Ne rien perdre : 60 % des idées abandonnées par un système le sont pour une erreur de mise en œuvre. (5) Le sélecteur de lieux, qui n'est encore qu'un pari. Ces chiffres sont rapportés par la réponse du 22 novembre, chacun d'une seule étude.

**Ce qui descend, ce qui remonte, ce qui ne remonte jamais**

| Étage | Données | Vers l'organisme | Règle |
|---|---|---|---|
| 1 | mondes de conception, engendrés à volonté | riche : issue de l'oracle, données d'expérience, contre-exemples | graines fraîches à chaque requête ; effort de recherche compté dans les seuils ; journal |
| 2 | mondes semi-synthétiques sur traces honnêtes réelles, sabotage planté | riche | réservoirs honnêtes disjoints ; fausses alertes finales sur traces jamais servies |
| 3 | familles de validation écrites à l'aveugle | borné : un choix dans une liste déclarée | comptabilité |
| 4 | familles plantées tenues à l'écart | **rien** ; lecture unique | forme stricte |
| 5 | épreuves sur modèles réels | **rien** dans le cycle | forme stricte |

La forme stricte pour ce qui est tenu à l'écart et pour le réel est la décision du directeur (R-5294). Le retour par étages sur les mondes de conception et semi-synthétiques est appliqué sous l'autonomie de la mère (R-5316), sans effet avant le 2 décembre, et reste à confirmer par le directeur. Il se concilie avec la décision du 22 novembre selon laquelle le juge statistique ne guide jamais la recherche en course : à l'étage 1, ce qui revient à l'organisme vient du vérificateur exact (la graine), ou de tirages d'exploration à part, comptés au budget ; jamais des tirages qui servent ensuite à juger.

**Descend seulement, figé avant la première lecture** : énoncés de verrous, vues publiques des mondes, statistiques de traces honnêtes, bibliothèque. **Ne remonte jamais** : un score de moniteur ; une portée estimée par un lecteur, comme récompense ; un verdict de juge dans le choix d'une composition, qui se juge sur l'oracle et le coût (N-058) ; les taux d'identification de l'oracle par strate ; une consigne réécrite par quelqu'un qui a vu un résultat.

**Transfert vers le programme réel.** Ce qui survit sort *gelé* du sas : une règle devient une conjecture et une cible de preuve ; une statistique devient une candidate d'épreuve préenregistrée sur modèles réels ; un schéma transféré deux fois devient une carte de la bibliothèque. Le transfert se juge dans la queue sélectionnée, non par une corrélation d'ensemble.

## 3.7 Ce qui se réemploie, ce qui est mort, où vont les leviers du 23

**Réemploi** (sources : inventaire du bibliothécaire, registre des idées de la veille de cap, état des lieux, passations).

| Existant | Où | Emploi dans l'attelage |
|---|---|---|
| Conception du banc de recherche à lois plantées, version 2, vérifiée « conforme », non codée : générateur, oracle hors de la machine, treize épreuves d'admission, calculs rejoués à l'octet | `docs/notes/banc-lois-plantees-c2-v1/` | socle des mondes à puits ; ses épreuves d'admission et sa leçon sur la fuite par la forme |
| Banc des correspondances plantées, et recherche à deux niveaux | réponse du 24 à la question sur le plan Turing, § 7 et 8 | famille de mondes pour l'étroitesse de serrure |
| Cinq décisions du 22 novembre sur ce que « forcer » veut dire | synthèse du protocole X sur les puits étroits, § 9 | règles de l'attelage : base sans modèle obligatoire, diagnostics d'abord, juge hors de la recherche |
| Portée comme surprise retirée ailleurs, trois estimateurs, monde à portée connue | réponse du 24 à la question 2 | mesure de profondeur et son épreuve |
| Quatre étapes de procédure lues comme oracles (répétition générale, courbe de capacité avec jumeau à dose nulle) | réponse du 24 à la question 1 | épreuves de l'instrument |
| Couche des questions ouvertes pondérées | réponse du 24 à la question 7 | sélecteur de problèmes, sous garde |
| Générateur de mondes mathématiques plantés, version 6 : trois familles (détection finie, agrégation à marges fixées, suites), évaluateur exact en rationnels, six tests de mort, registre de lignée, bases « grammaire aléatoire » et « forme seule », 233 essais | branche `claude/mathematiques-nouvelles-v1` | socle des mondes de verrous ouverts ; deux comparateurs déjà écrits |
| Pôle de test de l'organisme : nul formé de l'archive, tests de mort, oracle du tour fermé, sélection | dépôt public de l'organisme ; copie empreintée de 47 modules | prédicteur de référence ; résolveur |
| Banc de tricheurs, mondes où toute promotion est fausse | organisme | audit de la queue |
| Cinq miniatures exactes du catalogue ; simulation du lemme et du théorème négatif | `test_mort_catalogue_v1.py` ; `src/controle_ia/simulation_t03` | témoins « doit passer, doit mourir » |
| Scellement, manifeste, gardes, gabarit de préenregistrement | `src/controle_ia/` | plomberie |
| Cahier des charges du banc, version 3 | plan Turing sur processeur | interface, tests de mort, gardes |
| Outillage de l'assistant de preuve | branches du chantier | résolveur formel |
| Idées en file au registre : banc à puits plantés et courbe dose-réponse ; audit des pertes ; loi de découverte par vue ; bras sans modèle comme base obligatoire ; journal des probabilités de choix | registre, fiches en file ou proposées | elles *sont* l'attelage : il les éprouve enfin |
| Quatre-vingt-treize idées des mentors ; vingt-quatre papiers à exploiter par décision, rien de lancé | registre | vivier réel des lieux ; bibliothèque |

Le registre compte 311 fiches liées à l'organisme : 260 proposées, 44 en file, 5 essais non évaluables, une gardée, une fusionnée. Presque rien n'a été éprouvé. L'attelage est la machine qui donne à chaque fiche une des trois issues : bouton ou bras du banc, lieu du vivier réel, ou abandon par décision nommée.

**Mort ou rangé.**

| Objet | Cause |
|---|---|
| détecteur lexical de tensions | réfuté (aire 0,17, corrélation de rang −0,63) |
| décomposition orthogonale de l'archive, code couvrant, processus gaussien sur les lois, homologie de l'archive, opérateur d'expansion | retirés à la critique du collisionneur des bassins étroits |
| valeur e par strates pour une carte déjà localisée ; poids de multiplicité selon la nouveauté ; tirages du juge stratifiés | identité démontrée ; prime de nouveauté sous un autre nom |
| fenêtre fixe de distance ; entropie du verdict comme objectif | rejetées par les trois modèles |
| juge de nouveauté par modèle ; tournoi comme signal de sélection ; récompense de la nouveauté | décisions et veille (sélection au niveau du hasard) |
| pont de la fiche à la loi par traducteur séparé | épreuve fraîche : aucune fiche traduite sur quinze |
| bit de retour depuis les épreuves réelles | retiré par son auteur ; garantie vide aux tailles en jeu |
| clôture autocatalytique naïve ; identification des causes de la fertilité par apprentissage profond seul | triviale ; mal posée |
| tirage déterminantal d'origine du bisociateur ; indices de dispersion, bandits sur sous-grammaires, tests groupés | noyau invalide ; écartés à la critique |
| Noether, lagrangien, polarisation, résonance comme mécanismes | sans prédiction mesurable |
| atelier d'idées immédiat à juges-modèles (trois générations sur les bassins étroits) | écarté par la demande ; sa première génération s'est close en défaut sans fiche ; « gardé » au registre comme faux échec, à ne relancer qu'attelé |

**Non évaluables, donc ni morts ni vivants** : le duel des proposeurs, le collisionneur des bancs plantés, trois sessions arrêtées par le classifieur. Ils ont droit à une relance, après l'instrument.

**Trois constats de l'inventaire à ne pas perdre.** Les pièces d'octobre sont souvent reprises sans être citées (les ponts historiques déguisés du 23 octobre sont devenus le plan deux sur deux ; « valider le critère avant le moteur » du 26 octobre est devenu « l'évaluateur d'abord ») : tout texte de l'attelage les cite. Un remue-méninges du directeur des 2 et 3 novembre, payé, n'a jamais été synthétisé : c'est un gisement à dépouiller avant de concevoir, par un lecteur qui y a droit. Et quatre pistes d'octobre restent sans suite alors qu'elles tombent dans la cible : un parent contre deux parents, l'entraînement sur affectation biaisée suivi d'une épreuve randomisée, la mémoire jugée sur la loi prédictive, l'allocation entre classe d'hypothèses et paramètres ; elles deviennent des bras ou des boutons du banc, ou sont abandonnées par décision nommée.

**Les leviers du rapport du 23, rangés.**

| Levier ou expérience du rapport | Place dans le plan (§ 4.1) |
|---|---|
| protocole de vérité terrain sans fuite temporelle | règle transversale, dès l'étape 0 |
| épreuve « le pont suit-il la carte ? » | sa garde sur monde planté entre à l'étape 2 ; l'épreuve, réécrite, à l'étape 5 |
| hypergraphes, résolvantes de chemins | raffinement de la serrure ; second monde planté (une relation correspond à une chaîne de deux), étape 2 |
| notes de Gu et Krenn : prédiction hors temps | étape 5, sur le graphe daté |
| notes de Gu et Krenn : réanalyse par paire | étape 5 bis, suspendue à la publicité des identités de concepts |
| opérateur de scission | bras de l'organisme attelé, étapes 4 et 7 ; épreuve sur scissions datées, étape 5 bis |
| cycle éveil et sommeil avec compression de bibliothèque | audit de réemploi à l'étape 0 ; opérateur et mesure de profondeur à l'étape 7 |
| macros et arbres d'équations avant les algèbres amassées ; formes d'équations | étape 5 bis, sur un ensemble à risque et un échantillon stratifié, pas sur un cas |
| détecteurs sémantiques des cinq signaux sur la littérature d'alignement | étape 9, prospectif seulement |
| lecture de neurones de récompense | hors de l'attelage |

## 3.8 Ce qui est hors d'atteinte

1. **Certifier d'avance qu'un lieu réel contient un puits.** L'attelage relève les chances là où la structure pariée existe, et mesure qu'il le fait sur mondes plantés et sur le passé. Une percée dont la structure échappe à tous les paris reste hors de sa portée : c'est la borne « pas de repas gratuit » des séances de novembre.
2. **Mesurer la profondeur vraie dans une boucle courte.** Toute boucle favorise ce qui se résout vite. Seul un registre prospectif y répond, en partie, et lentement.
3. **Rétrodire sur dix ans avec un organisme à modèles de langage.** Ses modèles connaissent la suite. Restent quelques mois après leur date de coupure, et l'avenir.
4. **Garantir le passage des mondes plantés au programme réel.** C'est l'hypothèse non testée la plus lourde ; les premières lectures de transfert porteront sur peu de familles et réfuteront mieux qu'elles ne généraliseront.
5. **Des mathématiques neuves du contrôle, prouvées formellement par l'organisme, à court terme.** Atteignable d'abord : des énoncés finis dont le test numérique existe déjà.
6. **Valider en rétrospectif un détecteur sémantique de signaux précurseurs** : fuite du futur.
7. **Un panel d'experts** : contact externe, donc nœud du directeur.

---

# Partie 4 — Plan et dates

## 4.1 Ordre du moins cher au plus cher

Toute pièce décisive (préenregistrement, verdict, devis) suit la chaîne complète : Fable écrit, Opus contre-lit puis vérifie les corrections, la mère scelle. Le code est d'Opus, contre-lu par un autre modèle. Aucune épreuve ne tourne avant son texte scellé, simulation comprise.

| Étape | Quoi | Qui, classe | Coût | Ce que cela tranche | Ce qui tue | Dates |
|---|---|---|---|---|---|---|
| 0 | **Préparatifs sans Fable.** (a) Faits de données : source des dates et des auteurs pour PubTator 3, types réels du fichier, sens de l'ordre des deux concepts, effectifs comptés à l'aveugle ; schéma du graphe daté ; licence du banc de tiers. (b) Plomberie du banc à deux processus, gardes, proposeurs témoins scriptés, sans mondes ni seuils. (c) Audit du goulot sur les journaux, par un lecteur habilité, avec les diagnostics de collisions et d'autocorrélation. (d) Lecture sur PDF des voisins ; audit de réemploi des compresseurs de bibliothèque. (e) Dépouillement du remue-méninges des 2 et 3 novembre, jamais synthétisé | Opus ; B et C | processeur, 0 dollar | où est la limite de l'organisme actuel ; ce qui est faisable sur les données | l'effort sur le tri, si le vivier ne contient presque jamais la vérité plantée | 25 novembre au 1er décembre, sans toucher la file de l'entretien |
| 1 | **Conception de l'instrument de la cible et des deux familles de mondes** (mondes à puits, correspondances plantées), avec le préenregistrement de leur validation. C'est une extension de la conception du banc à lois plantées et du banc proposé le 24, fondue avec la conception demandée par le cahier des charges : un seul texte | Fable, effort maximal ; A | quota de Fable | — | — | 2 au 4 décembre ; contre-lecture et scellement jusqu'au 7 |
| 2 | **Code des mondes, validation de l'instrument, tests de mort du banc, répétition générale, courbe de découverte du hasard et de l'énumérateur ; banc des correspondances plantées joué par ses bras sans modèle** (énumération, programme exact, signatures de rôle, transport, spectral, recuit) ; familles tenues à l'écart écrites par une instance aveugle d'une autre famille | Opus et processeur ; B, puis verdict par un sous-agent neuf | 0 dollar | l'instrument mesure-t-il la profondeur et l'étroitesse plantées ; jusqu'où la force brute suffit ; quelle méthode trouve une correspondance étroite, et à quel coût | le banc, si un juge faible classe comme l'oracle ou si un raccourci passe ; la notion, si la courbe est plate ; une méthode savante, si elle ne bat pas l'énumération à coût égal | 7 au 11 décembre |
| 3 | **Préenregistrement et devis de l'apport propre à coût égal** dans la strate étroite et profonde | Fable, effort élevé ; A ; accord du directeur | quota de Fable | — | — | 9 au 14 décembre |
| 4 | **Première course payante** : chercheur de référence, boucle simple, organisme attelé minimal, attelage placebo ; lecture unique des mondes tenus à l'écart | exécutant ; lecteur neuf | à deviser ; pour repère, la plus petite course réelle de l'organisme avait une ligne de 45 dollars (GO-2026-11-10-10) | l'attelage bat-il le meilleur modèle seul là où celui-ci échoue | l'architecture à rôles et générations, si l'écart reste sous le bruit entre courses | 15 au 19 décembre au plus tôt |
| 5 | **Sélecteur de problèmes en rétrodiction longue, sans modèle de langage** : graphe daté (surprise, cortège non typé), puis PubTator 3 sur préenregistrement réécrit | Fable pour le texte ; Opus et processeur | 0 dollar | la serrure et le cortège prédisent-ils au-delà des bases | le sélecteur, s'il ne bat pas hors période le volume, l'ancienneté et la répartition des experts | texte du 9 au 12 ; courses du 14 au 23 décembre |
| 5 bis | **Épreuves datées secondes**, chacune sur son préenregistrement : scissions de descripteurs ; inflation descriptive et entropie des notations sur un échantillon stratifié de sources LaTeX ; couche des problèmes pondérés ; réanalyse des notes de Gu et Krenn si les identités sont publiques | Fable pour les textes ; Opus et processeur | 0 dollar hors accès en masse | quels autres sélecteurs prédisent | chaque sélecteur qui ne bat pas ses bases | janvier |
| 6 | **Registre prospectif scellé, interne** : prévisions de l'instrument, puis de l'organisme, à trois, six et douze mois | mère ; C | presque nul | l'information portée sur l'avenir | la prétention, si elle ne bat pas le modèle seul | ouverture dès le 7 décembre |
| 7 | **Verrous ouverts à valeur optimale calculable ; cibles finies de preuve ; opérateurs comme bras** (scission, compression entre bassins, marchepieds) ; **dose-réponse en température** pour séparer un catalyseur d'un préfacteur dans l'organisme ; signaux plantés avant toute carte relationnelle des tensions | Fable, Opus | sur devis | une vraie candidate pour le programme sort-elle ; qu'est-ce qui abaisse réellement une barrière | l'opérateur sans rendement mesuré | janvier |
| 8 | **Transfert par le sas vers une épreuve réelle préenregistrée** | chaîne complète | sur devis | le banc prédit-il le réel, dans la queue sélectionnée | le banc comme oracle de choix | janvier et février |
| 9 | **Détecteurs sémantiques de signaux précurseurs sur la littérature d'alignement**, en prospectif | — | sur devis | — | — | pas avant février |

## 4.2 Chemin minimal viable

**Sans dépense, sur processeur** : étapes 0 (b), 1 et 2. À la sortie : la cible gelée, une famille de mondes à puits avec ses familles tenues à l'écart, un banc qui a passé ses tests de mort, une mesure de profondeur et d'étroitesse validée contre la graine, la courbe de découverte du hasard et de l'énumérateur selon l'étroitesse, et un premier classement des méthodes de recherche d'une correspondance étroite. **Date réaliste : entre le 10 et le 12 décembre**, si la passe de Fable a lieu du 2 au 4. S'il faut couper, le banc des correspondances plantées passe après : la question du directeur porte d'abord sur les mondes à puits.

**Avec modèles payants** : étapes 3 et 4, le premier chiffre de l'organisme attelé, **entre le 15 et le 19 décembre au plus tôt**. Si les pièces de la porte de sortie de la phase 0, due fin décembre, prennent le quota de Fable, ce chiffre glisse en janvier ; la partie sans dépense, elle, tient.

Ce chemin ne contient ni rétrodiction, ni preuve formelle, ni opérateur savant. C'est voulu : il répond d'abord à la question du directeur — l'organisme attelé cherche-t-il les puits étroits et profonds mieux que le hasard et que le meilleur modèle seul ?

## 4.3 Critères d'arrêt

- **Banc mort**, il ne choisit rien : un juge faible qui voit tout classe comme l'oracle ; un proposeur faible égale le fort ; une fuite de clé est notée ; le tirage uniforme franchit un seuil.
- **Instrument invalide**, aucune lecture : la profondeur mesurée ne suit pas la portée plantée, ou un témoin à zéro n'est pas à zéro.
- **Notion à refaire** : la découverte ne dépend pas de l'étroitesse telle que définie.
- **Résolveur inapte à la queue** : taux de fausse acceptation du même ordre que la fréquence des puits. On répare le résolveur avant toute intervention qui pousse vers le rare.
- **Architecture rangée jusqu'à preuve** : à coût égal, l'écart au chercheur de référence reste sous le bruit entre courses dans la strate étroite et profonde.
- **Sélecteur écarté** : il ne bat pas les bases hors période, gardes tenues ; « non concluant » si une garde tombe.
- **Jamais d'arrêt sur un résultat négatif en soi** : chaque cycle est rapporté, une famille neuve par cycle. Une panne technique donne droit à une relance et n'est pas un résultat.

## 4.4 Risques

| Risque | Parade |
|---|---|
| le banc choisit pour le banc | transfert mesuré dans la queue sélectionnée ; mondes de tiers en confirmation |
| mémoire des modèles pré-entraînés | lois tirées d'une graine ; plan deux sur deux ; verrous réellement ouverts |
| fuite par spécification : les cartes décrivent ce que les mondes instancient | cartes leurres ; auteurs des mondes aveugles |
| lignée commune entre qui écrit les mondes et qui les résout | générateur mécanique ; autre famille |
| une portée estimée devient une cible à gonfler | elle n'est jamais rendue aux proposeurs ; la mémoire s'indexe sur l'oracle |
| strate étroite trop rare pour la puissance | générateur de familles ; issue « non jugeable » écrite |
| l'organisme n'a jamais bouclé en réel | noyau minimal gelé |
| quota de Fable et porte de fin décembre | un seul texte de conception, une seule passe ; Opus avant le 2 |
| cartographie écrite par un autre modèle, jamais auditée | revérification des énoncés avant service |
| voisins publiés partout | lecture sur PDF avant toute phrase sortante ; rien ici n'est revendiqué |

## 4.5 Nœuds pour toi

1. **Périmètre de la première cible.** Enjeu : ce que mesure le premier chiffre. (a) Les transferts d'abord, les créations hors alphabet ensuite : atteignable, conforme à ce que montre le passé récent ; ne dit rien de la création. (b) Les deux ensemble : plus ambitieux ; puissance divisée. Recommandation : (a), confiance 0,7. Défaut sous 48 heures : (a).
2. **La portée plantée entre-t-elle dans l'oracle qui juge une composition ?** Enjeu : sans elle, le choix d'une composition ignore la profondeur ; avec elle, le critère de la décision sur l'oracle change. (a) Oui, pour les seuls mondes plantés. (b) Non, mesure rapportée. Recommandation : (a), confiance 0,6. Pas de défaut : c'est une lecture de règle.
3. **Noyau attelé minimal ou course principale d'auto-conception.** Enjeu : deux socles pour le même banc. (a) Un seul socle, celui de l'attelage ; la course d'auto-conception reprend après le premier chiffre. (b) Les deux en parallèle. Recommandation : (a), confiance 0,7. Défaut : (a).
4. **Qui écrit les familles tenues à l'écart.** (a) Une instance aveugle d'un modèle de Google par la clé gratuite, sous la garde des appels à Google. (b) Une instance aveugle d'Opus. Recommandation : (a), confiance 0,6. Défaut : (a).
5. **Registre prospectif scellé, interne, dès décembre.** (a) Oui, non public. (b) Plus tard. Recommandation : (a), confiance 0,8. Défaut : (a).
6. **Cibles finies de preuve dans l'attelage avant la levée de la fermeture du pilier.** Pas de défaut ; recommandation : attendre l'étape 7.
7. **Amender la charte du plan Turing** par une section « comment chercher », à deux niveaux, qui renvoie aux décisions du 22 novembre, et y inscrire le banc des correspondances plantées (amendements proposés le 24 par la réponse sur le plan Turing). Recommandation : oui, confiance 0,7 ; c'est une proposition avec défaut sous 48 heures, coût nul, réversible.
8. **Lecteur habilité pour l'audit du goulot et pour le remue-méninges des 2 et 3 novembre**, et **accès payant aux sources d'arXiv en masse** : à dire quand tu le voudras ; l'échantillon stratifié gratuit suffit pour commencer.

## 4.6 Confiance

Probabilités subjectives, écrites pour être démenties ; aucune course ne vise un signe.

- La définition de la cible rend bien ce que tu appelles un puits étroit et profond : 0,6.
- Le chemin sans dépense tient pour le 12 décembre : 0,55. Le premier chiffre payant avant le 20 décembre : 0,4.
- L'attelage entier, espèces mécaniques comprises, bat le meilleur modèle seul à coût égal sur des puits à parent présent dans la bibliothèque : 0,6. La société d'agents ajoute quelque chose à l'attelage servi à un seul modèle : 0,35. Sur des puits sans parent : 0,3.
- L'interaction de la surprise et de la serrure bat les bases sur données datées : 0,4.
- Une idée sortie de l'attelage devient une épreuve, une sonde ou une cible de preuve du programme avant fin février : 0,3.

---

# Annexe — Références et pièces lues

**Voisins vus en ligne le 24 novembre (notice ou résumé ; à vérifier sur PDF).** Bancs de découverte de lois résistants à la mémoire : NewtonBench (arXiv 2510.07172), LLM-SRBench (arXiv 2504.10415 ; l'exactitude symbolique y est jugée par un modèle), DiscoveryWorld (arXiv 2406.06769), BoxingGym (arXiv 2501.01540). Redécouverte après la date de coupure : MOOSE-Chem (arXiv 2410.07076). Exploration par un modèle : Krishnamurthy et al. (arXiv 2403.15371) ; Gupta, Hartford et Liu (arXiv 2509.21403). Prévision de percées sur graphes de concepts : Maillart et al. (arXiv 2606.03864) ; FOS (arXiv 2511.18631). Structure de Mathlib : arXiv 2604.24797. La zone « prédire où naîtront les percées » est donc occupée : toute phrase sortante les cite après lecture.

**Rapporté par le dépôt.** Zeng et al. (arXiv 2611.23068) ; Oved et al. (arXiv 2610.23977) ; « A Society of AI Scientists » ; Cang (arXiv 2611.19841) ; Openhagen Worlds (arXiv 2611.24711) ; Guo et al. (arXiv 2611.25534) ; Li et al. sur l'ignorance simulée (arXiv 2601.13717) ; Zhu et al. sur les raccourcis d'un générateur (arXiv 2609.18366) ; Good 1953 ; Bubeck, Ernst et Garivier 2013 ; et, lus sur PDF par la réponse du 24 à la question sur le plan Turing : Ovsjanikov et al. 2012 (applications fonctionnelles), Melzi et al. 2019, Peyré, Cuturi et Solomon 2016. Citations obligatoires de l'organisme, inchangées : POPPER, Dwork et al., Blum et Hardt, Co-Scientist, et la liste étendue des décisions de resserrement.

**De mémoire, à vérifier sur PDF.** Ellis et al. (DreamCoder) ; Bowers et al. (Stitch) ; Kaliszyk et Urban (fouille de lemmes).

**Pièces lues, empreintes sha256 abrégées** (racine : copie de travail de `main` au commit `e7ae9ad6`, sauf mention).

| Pièce | Empreinte |
|---|---|
| `docs/notes/plan-turing-v1/plan-turing-directeur-v1.md` | `69c8deae…` |
| `docs/notes/plan-turing-processeur-v1/etat-des-lieux-plan-turing-processeur-v1.md` | `0e562d8c…` |
| `docs/notes/plan-turing-processeur-v1/cahier-des-charges-banc-mondes-plantes-verrous-controle-v3.md` | `495f92c7…` |
| `docs/notes/plan-turing-processeur-v1/contre-lecture-pubtator3-v1/contre-lecture-prereg-pubtator3-brouillon1-v1.md` | `bd528999…` |
| `docs/notes/plan-turing-v1/pas0-rang1-foyers-tension-v1/rapport-pas0-rang1-foyers-tension-v1.md` | `0a617ab1…` |
| `docs/notes/cartographie-mathematiques-ouvertes-v1/cartographie-verrous-mathematiques-ia-v1.md` | `00c551b0…` |
| `docs/notes/cartographie-mathematiques-ouvertes-v1/temoins-externes-et-protocole-v1.md` | `bcfbd25e…` |
| `docs/notes/avis-fable-organisme-ideation-v1/avis-fable-organisme-ideation-v1.md` | `8c2f45e2…` |
| note de sortie du collisionneur sur la boucle entre l'organisme et le contrôle (bloc-notes de la mère) | `456fbebf…` |
| `docs/notes/collisionneur-bassins-etroits-v1/synthese-v1.md` | `5fd7e26f…` |
| `docs/notes/bassins-etroits-idees-v1/remue-meninges-mere-v1.md` | `f3c46703…` |
| `docs/notes/exploration-idees-fable-v1/reponse-demande-reformulee-v2.md` | `29c5f73c…` |
| `docs/notes/collisionneur-v9/notes-de-sortie-v1/note-sortie-puits-etroits-v1.md` (début) | `556df57b…` |
| `docs/notes/collisionneur-boucle-d-or-v1/synthese-boucle-d-or-v1.md` | `b52d7aee…` |
| `docs/notes/bisociation-litterature-reelle-v1/collisionneur-question-6-v1/synthese-question-6-v2.md` | `ff3b19e3…` |
| `docs/notes/bisociation-litterature-reelle-v1/collisionneur-question-7-v1/synthese-question-7-v2.md` (début) | `0ced3b28…` |
| `docs/notes/protocole-x-structure-du-langage-v1/synthese-structure-du-langage-v1.md` | `baca15c9…` |
| `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md` | `6f6397ee…` |
| `docs/notes/idee-interessante-v1/lot-8/registre-idees-session-2026-11-23-v1.md` (table et quinze fiches) | `e7bf754c…` |
| `docs/notes/idee-interessante-v1/lot-8/rapport-priorites-et-impact-organisme-2026-11-23-v1.md` | `88d80f76…` |
| `reponse-fable-max-v1.md` et sa provenance (pièces du directeur) | `8ec4f9e0…`, `85b171ec…` |
| `note-hypotheses-et-appuis-v1.pdf` (pièce du directeur ; parties 1.7, 1.11 à 1.13 et 3 lues sur extraction de texte) | `b776c857…` |
| réponses du 24 aux questions 1, 2, 3, 4 et 7 et trois compléments de la mère (branche `idees/questions-directeur-2026-11-24-v1`, `92a8e511`) | `2cc29632…`, `7f4cf73f…`, `af126ebf…`, `249c611c…`, `937e3e69…`, `b2dc5ebe…`, `43716a8a…`, `58d2e517…` |
| fiche de faisabilité des données publiques (branche `idees/rang4-etalonnage-pont-v1`) | `1736e5f0…` |
| `docs/notes/veille-organismes-ideation-v3/synthese-v1.md` | `2bc3af77…` |
| `docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v3.md` (verdict, § 0, 1.4, 4.1 à 4.4) | `bbde32b7…` |
| `docs/notes/etat-chantier-lean-2026-11-21-v1.md` ; passation du chantier des mathématiques nouvelles du 22 novembre | `3d2b8d3e…` |
| générateur de mondes plantés du pilote mathématique, version 6 (en-têtes de modules ; branche `claude/mathematiques-nouvelles-v1`) | — |
| décisions sur l'oracle des mondes plantés, l'universalité, la composition apprise, le resserrement de l'organisme (N-058, N-044, N-045, N-067) ; lignes R-5241, R-5254, R-5268, R-5271, R-5285, R-5294, R-5301, R-5316 du registre | `854f2724…` pour N-058 |
| transmission du registre des idées de la veille de cap (branche `claude/veille-de-cap-v1`, `e09918f2`) | `14c143d6…` |
| inventaire des pistes du plan Turing depuis le 15 octobre (bibliothécaire neuf ; catalogue, accords, réfutations, trous lus ; tableau des 102 pièces parcouru) | `65ce3c09…` |
| réponse du 24 à la question sur Carbon, Fable et le plan Turing (branche des questions, `10305094`) | `0bdc9810…` |
| `docs/notes/demandes-fable-api-2026-11-22-v1/synthese-protocole-x-puits-etroits-v2.md` (verdict, § 4, 5, 8 et 9) | `6112172f…` |
| `docs/notes/banc-lois-plantees-c2-v1/conception-fable-banc-lois-plantees-v2.md` (verdict, § 6.1, 6.2 et 7) et la vérification de ses corrections | `62c519c0…` |
| `docs/notes/protocole-x-boucle-organisme-controle-v1/` : explication des mondes plantés ; réponse approfondie de Carbon (§ 2) | `895dbc0e…`, `f744320d…` |
| `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` (§ 4, par recherche) | `b95688df…` |

---

Fin de rédaction : 2026-11-24T16:38:13Z (`date -u`).
