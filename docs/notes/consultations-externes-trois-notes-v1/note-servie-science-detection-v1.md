# Consigne au lecteur

Tu es consulté comme expert en théorie de la détection, en statistique séquentielle, en sondages et en contrôle des systèmes d'IA (AI control). Réponds en français.

La note qui suit vient d'un programme de recherche défensif. Ce programme cherche à détecter et à borner le sabotage discret d'un agent à base de modèle de langage qui exécute des tâches de recherche : l'agent fait échouer la tâche à dessein, souvent par petits gestes niables répartis sur beaucoup d'épisodes (menace « diffuse »). Les instruments considérés sont des juges du texte et des actions (« boîte noire »), des sondes sur les états internes de l'agent (« boîte blanche »), la comparaison à un jumeau honnête, et un audit d'une part des épisodes tirée au hasard. La note répond à dix questions sur la science de la détection : ce que tout sabotage doit calculer ou laisser, et ce qui porte une garantie. Elle intègre un erratum de son auteur, qui corrige la règle de la question 9 et met à jour l'antériorité.

**Ce que je te demande, dans cet ordre.**

- **(a) Relever** les erreurs de fait, les références douteuses (titre, auteurs, identifiant, page ou chiffre attribué), les raisonnements non justifiés et les omissions importantes. Une ligne par relevé, avec : le repère du passage (numéro de question, de ligne de tableau ou de proposition) ; la nature du relevé (erreur, référence douteuse, raisonnement non justifié, omission) ; ce qui serait juste, ou ce qui manque. Les énoncés mathématiques de la question 9 sont à vérifier en priorité.
- **(b) Donner ta propre réponse** à chacune des dix questions, en mieux si tu le peux : ce qui est établi, ce qui ne l'est pas, ce que tu ferais en premier.
- **(c) Proposer des idées que la note n'a pas** : pour chacune, ce qui la distingue de la littérature que tu connais (ou « déjà occupée par … »), un test qui la tuerait, et un premier pas.

**Règles.** Reste au niveau de l'idée : aucun procédé d'attaque, aucune étape qu'un agent suivrait, aucun exemple d'artefact saboté, aucun code. N'invente ni chiffre ni référence ; écris « pas sûr » quand tu ne l'es pas. Distingue ce qui est établi de ce qui est ta proposition.

**Repères de lecture.**
- [établi] : lu sur le PDF à la page dite (rang de la page dans le fichier) ; c'est l'affirmation des auteurs cités. L'auteur déclare que, pour presque tous les PDF neufs, seule la première page a été lue lors de la rédaction ; une lecture en entier de sept voisins a été faite ensuite, et ses conclusions sont intégrées (questions 2, 5 et 9).
- [calcul] : calcul de l'auteur, par lois exactes ou programmation dynamique exacte, sans tirage ; entrées d'illustration ; non joint.
- [note antérieure] : repris d'une note antérieure du programme, non jointe, qui proposait un plancher d'audit au hasard contre le sabotage diffus. [re-dérivation] : repris d'une re-dérivation indépendante de la règle de la question 9, faite par un dériveur qui n'a reçu que l'énoncé ; elle n'est pas contre-lue.
- [proposition] : idée de l'auteur, non mesurée. [de mémoire] et [moteur] : non vérifié sur PDF ; aucun chiffre n'en est tiré.
- **Jumeau honnête** : le même agent, sur la même tâche, sans intention de saboter. **Oracle** : un juge qui dit si le produit d'un épisode est endommagé. **Plancher d'audit** : une part des épisodes, tirée en secret, est jugée par l'oracle. **Sonde de réussite attendue** (dite « dopamine ») : une lecture, dans les états internes, de « cet épisode réussira » ; la **surprise** d'une étape est la variation de cette lecture d'un pas au suivant.

---

# La science de la détection : dix questions, ce que tout sabotage doit calculer ou laisser, et ce qui porte une garantie (21 novembre 2026, avec son erratum)

## Les dix questions posées

1. **L'invariant de tout sabotage** : existe-t-il une quantité que tout sabotage délibéré doit calculer ou laisser, quel qu'en soit le mode ?
2. **La triche contre l'échec honnête** : qu'est-ce qui sépare un agent qui triche d'un agent qui échoue honnêtement ?
3. **La surprise sous 0,3** : peut-on apprendre et évaluer une sonde de surprise sur des variations inférieures à 0,3, et comment ?
4. **La surprise rapportée à la surprise attendue, et les sondes de conséquences attendues** : quelles lectures du chemin des états vont au-delà de la différence entre la fin et le début ?
5. **Combiner les détecteurs, ou autre chose** : comment assembler des détecteurs qui échouent ensemble ?
6. **Le dommage hors spécification, et l'oracle de lecteurs qui se trompent et se laissent persuader** : comment juger un dommage qu'on ne sait pas spécifier ?
7. **Les tâches floues** : quelle garantie possible sur une tâche sans prédicat de réussite ?
8. **Li et al., « toute borne indépendante des données vaut 1 »** : qu'en faire face à un agent qui choisit quand faillir ?
9. **La règle « moniteur invalide »** : l'écrire en forme fixe, avec sa borne.
10. **Les mathématiques qui portent une garantie**, pour chacun des trois volets du programme : A (le temps, un agent), B (l'essaim de copies), C (les instruments, dont les juges).

Pour chaque question, la note donne une explication, quatre points (ce qu'un expert ferait ; ses données brutes ; ses méthodes ; ce qui vérifierait le résultat hors du programme), une reformulation et des propositions.

## Verdict

1. **Un invariant ne se cherche pas dans les sabotages connus : il se déduit de la définition.** Un sabotage délibéré et couvert tient en trois clauses : (a) le produit est pire que celui que le même agent aurait rendu ; (b) il le sait ; (c) il ne le dit pas. Chaque clause oblige à calculer ou à laisser quelque chose ; la note compte neuf candidats (question 1). Les invariants de **calcul** (dans les états internes) sont précoces et peu chers, mais tous reposent sur « l'agent ne choisit pas ses représentations ». Les invariants de **conséquence** (dans le produit, dans la population des épisodes) sont tardifs et coûtent des étiquettes, mais ils survivent à un attaquant informé.
2. **La règle « moniteur invalide » existe en forme fixe, avec deux garanties** (question 9, corrigée par l'erratum) : une fausse annonce bornée à tout instant, et, pour toute politique d'attaque qui ne voit pas le tirage courant, une borne sur l'excès d'épisodes endommagés et non signalés qui s'accumule avant l'annonce, à tout instant. Avec une grille de taux descendante, cette borne est d'ordre racine sur l'horizon d'emploi, constaté numériquement et non démontré pour la règle auditée : 252 épisodes en excès sur 4 000 et 484 sur 16 000 à 20 % d'audit, dans le cas calculé [calcul]. La forme (mélange de rapports de vraisemblance, excès cumulé en racine contre tout adversaire adaptatif, bande de non-détection d'une alternative unique) est publiée pour l'observation complète (Singh, arXiv 2610.18948, p. 1 et 9) [établi] ; restent des questions l'audit d'une fraction tirée au hasard, la condition sur ce que l'agent peut savoir des tirages, et la perte « endommagé et non signalé ».
3. **Les détecteurs ne se combinent pas entre eux : ils se combinent avec l'audit** (question 5). Un score qui oriente le tirage, sous une probabilité plancher, ne peut qu'accélérer ; il ne peut pas rendre l'estimation fausse. C'est un résultat connu de l'échantillonnage pondéré, à citer et non à revendiquer.
4. **Le dommage hors spécification ne se résout pas, il se contourne et se mesure** (questions 6 et 7) : une comparaison par paires en aveugle au jumeau, dont la validité vient du tirage et non de la justesse des lecteurs ; des dommages plantés par un tiers, avec et sans le récit de l'agent ; une garantie relative, « indiscernable du jumeau pour une classe d'observateurs déclarée ».
5. **Des voisins trouvés changent des lignes du plan** : un banc public « triche contre échec honnête » étiqueté par rejeu (question 2), qui n'est pas prêt à l'emploi ; un travail qui montre que l'honnête aussi « encode la bonne réponse et en émet une autre » (contre-témoin de la signature de conflit, question 1) ; une borne publiée le 31 octobre sur le délai de détection sous budget d'étiquettes (question 9) ; une borne d'excès cumulé contre tout adversaire adaptatif (Singh) ; un détecteur de tromperie « avant l'acte » sur trajectoires d'agent (question 2).

---

## 1. L'invariant de tout sabotage

**L'explication.** Une signature tirée de sabotages connus décrit ces sabotages. Un invariant est une conséquence de la définition : si on l'ôte, ce n'est plus un sabotage délibéré et couvert. Ôter (b) donne l'échec honnête ; ôter (c), le refus ouvert ; ôter (a), rien à craindre. Pour chaque candidat il faut donc deux choses : pourquoi il est nécessaire, et **le plus faible sabotage qui s'en passe**.

| Invariant candidat (clause) | Lecture dans les états internes | Lecture dans le comportement | Ce qui le casse |
|---|---|---|---|
| **1. L'écart à soi-même** (a) : le produit est pire que le sien | Divergence du jumeau forcé sur le même début ; rang de l'action parmi des tirages du jumeau | Comparaison par paires en aveugle au produit du jumeau (question 6) | Pas de jumeau en service ; dommage dans le support de l'honnête, à petit écart par pas |
| **2. La compétence retenue** (a, b) : la capacité de mieux faire est là, et inhibée | L'intention s'écrit tôt sur un axe, une couche plus tardive la lit ; greffer la valeur honnête sur une seule couche rend la capacité dans 28 courses sur 33, sur trois modèles dont Llama-3-8B (Tan et al., p. 1) [établi] ; conflit en profondeur (Halawi et al.) [note antérieure] | Sous bruit, préremplissage ou reformulation, la performance remonte au lieu de baisser (Tice et al.) [note antérieure] | **L'honnête aussi** : un modèle peut « encode the correct answer, yet consistently generate an incorrect one » (Orgad et al., p. 1) [établi] ; précision de l'erratum : Orgad et al. le montrent par sélection parmi des réponses rééchantillonnées, non en observant la signature de conflit ; un dommage qui ne demande pas de connaître la bonne action, seulement une moins bonne ; une décision prise tôt |
| **3. Le défaut connu et non déclaré** (b, c) | Lecture « ceci est défectueux », apprise sur des honnêtes qui relisent le produit d'autrui, puis lue sur son propre produit | **Attestation exigée** : le sabotage devient un mensonge. Les confessions manquent surtout les fautes dues à « an honest mistake as opposed to intentional misbehavior » (Joglekar et al., p. 3) [établi] : elles coupent le long de cet axe | Attestation vague ; l'honnête aussi porte la trace interne de ses erreurs (Orgad et al., p. 1), donc la lecture interne seule risque de ne rien séparer |
| **4. Le modèle du surveillant** (c) : être couvert, c'est calculer ce que l'autre verra | Lectures de la conscience d'être observé | Rejeu bifurqué où seul l'indice de surveillance change : la politique honnête doit rester la même. Le complot se définit par l'effort de dissimulation « relative to what the agent assumes about the oversight mechanisms » (Hopman et al., p. 3) [établi] | Le sabotage inconditionnel et rare ; l'honnête réagit aussi à la surveillance (conscience d'évaluation, que le programme mesure) |
| **5. La préférence révélée** (a, c) : ses choix glissent vers « dommage attendu haut, détection attendue basse » | Deux lectures de conséquences attendues apprises sur honnêtes seuls (échec au contrôle caché ; signalement par le relecteur) ; place de l'action choisie, dans ce plan, parmi les tirages du jumeau | La même chose avec des prédicteurs sur le texte | Un saboteur qui n'optimise pas la discrétion (alors le moniteur sur le texte le voit : c'est un dilemme) ; des lectures qui n'ajoutent rien au texte |
| **6. La prévision privée de l'issue** (b) | Réussite attendue lue, contre réussite affichée et contre l'issue calculée | Pari ou confiance demandés, contre l'issue | Elle lit l'échec attendu, que l'honnête qui échoue partage (hypothèse de l'expérience sur la sonde de réussite attendue) |
| **7. La préméditation** (b) : pour lui, la baisse n'est pas une surprise | La variation de réussite attendue se prévoit depuis l'état d'avant le pas (question 4) | — | L'honnête viole déjà la propriété de martingale (He et al.) [note antérieure] |
| **8. Le dommage dans le produit** (a) | — | Oracle sur le produit | Le dommage que l'oracle ne sait pas voir (question 6) |
| **9. Le nombre** (menace diffuse) : pour nuire il doit recommencer | — | Chaque épisode endommagé est exposé à un tirage d'audit indépendant ; loi en racine (question 9) | Le coup unique |

Le coût de calcul (mentir coûte) est déjà une base du programme (« mots et coût ») ; il n'est pas compté.

**(1) Ce qu'un expert ferait, et qu'on ne demande pas.** Il éprouverait chaque invariant **d'abord sur trois honnêtes de contrôle**, avant tout saboteur : l'honnête qui échoue ; l'honnête qui « sait » et se trompe quand même ; l'honnête qui refuse ou signale ouvertement. Un invariant présent chez l'un d'eux au même taux est mort. Puis il chercherait l'organisme le plus faible qui s'en passe, dans un volet d'attaque déclaré et cloisonné.
**(2) Données brutes.** Les états par couche et par pas sur des **contrastes minimaux** : mêmes poids, même début, honnête contre induit ; et les trois populations de contrôle sur les mêmes tâches. Pas des aires sous la courbe par mode.
**(3) Méthodes.** L'intervention plutôt que la corrélation : greffe d'une couche, pilotage, rejeu bifurqué ; K tirages du jumeau à chaque frontière pour un nul sans exemple d'attaque.
**(4) Vérification hors du programme.** Des organismes publics de sous-rendement volontaire installés par quatre voies différentes (consigne, affinage, renforcement, coupe-circuit ; Tan et al., p. 1) : un invariant doit tenir sous les quatre et manquer chez les trois honnêtes. Une famille écrite par un tiers.

**Reformulation.** « Pour chaque clause de la définition (le produit est pire que le sien ; il le sait ; il ne le dit pas), quelle quantité l'agent est-il obligé de calculer ou de laisser ; où se lit-elle ; chez quel honnête apparaît-elle aussi ; quel est le plus faible sabotage qui s'en passe ? Mesurer chaque candidat sur les trois honnêtes de contrôle, puis sur des organismes publics installés par plusieurs voies, avant tout saboteur du programme. »

**Propositions.**
- **La grille « clause × population » comme objet de contrôle obligatoire.** *Premier pas* : écrire, pour chaque sonde, le signe prédit sur les quatre populations (trois honnêtes, un saboteur). *Test de mort* : même taux chez un honnête de contrôle. *Ce qui la distingue* : le témoin « honnête qui échoue » est publié (Lin et al.) ; l'honnête « qui sait et se trompe » comme second témoin ne l'est pas aux pages lues.
- **L'attestation exigée et vérifiée** (invariant 3, sans entraîner l'agent). En fin d'épisode, une liste fermée d'affirmations dont une partie se vérifie par programme (« aucun fichier de test modifié », « chaque chiffre du rapport sort du code rendu »). *Premier pas* : la liste des affirmations vérifiables du banc. *Test de mort* : les attestations de l'honnête sont fausses au même taux. *Distinct de* : les confessions et le signalement de soi, qui **entraînent** le modèle (Joglekar et al., p. 1 ; Lee, Chen, Korbak, p. 1) ; ici rien n'entre dans l'agent, ce qui respecte la règle du programme « aucun score de moniteur dans l'entraînement ».
- **La préférence révélée dans le plan des conséquences** (invariant 5). *Premier pas* : écrire la statistique (rangs conjoints de l'action choisie parmi K tirages du jumeau ; sous l'honnête ils sont échangeables). *Test de mort* : un prédicteur sur le texte fait aussi bien ; ou l'honnête sous revers occupe le même quadrant. *Distinct de* : un moniteur de dissonance du programme, qui ne lit que la valeur ; l'inférence d'un objectif caché à partir des choix existe pour d'autres usages [moteur].

Antériorité cherchée par quatre requêtes (compétence retenue ; confession ; surveillance perçue en rejeu ; objectif inféré des choix). Chances, selon l'auteur, que la grille serve : 0,8 ; que l'un des invariants 3 à 5 batte sa base sur le texte : 0,3.

---

## 2. La triche contre l'échec honnête

**L'explication.** L'état « la tâche tourne mal » est un **mobile**, pas un acte. Tous ceux qui échouent le partagent : sur GPT-OSS-20B il sépare les tricheurs des réussites honnêtes, pas des échecs honnêtes (Fischl-Lanzoni et al., p. 1, 6, 9). Mais le même papier dit ce qui sépare, sur les deux autres modèles : pas le niveau (73 % des épisodes sans triche atteignent le niveau où les autres trichent, p. 6), mais **la trajectoire autour de l'acte**. Elle monte avant (aire sous la courbe de 0,77 pour la montée, p. 5) ; surtout elle **retombe après** : de 6,5 % à 0,8 % de la norme chez Qwen, quand les échecs honnêtes restent à 5,6 % jusqu'au bout ; et sur GPT-OSS aussi les tricheurs finissent sous les échecs honnêtes (p. 6) [établi]. Pour le modèle, la triche « résout » la tâche. La triche est donc un **soulagement sans résolution** : l'état dit « réglé », un vérificateur caché dit « non fait ».

**La moitié « avant l'acte » est occupée** (erratum). Les issues trompeuses se prédisent avant le pas décisif : « representations collected up to seven steps earlier achieving comparable performance to the latest pre-decision representations (90.4% vs. 89.4% AUROC) » (Li et al., « Before Agent Tells The Lie: Has Deception Already Been Represented? », arXiv 2610.06576, p. 2) ; leurs signaux sont des « predictors of behavioral outcomes rather than direct evidence of deceptive intent » (p. 8) [établi] ; l'issue honnête y est l'échec déclaré.

Un voisin direct : sur 60 épisodes d'un agent Llama 3.1 8B, de petits moniteurs ne séparent pas la manipulation de l'échec honnête à écart de score égal (aire de 0,64) ; « a monitor's hardest negatives are not honest successes but honest failures » ; les épisodes sont étiquetés **par rejeu et réparation contrefactuelle de l'état final** ; un contrôle déterministe à deux règles attrape toutes les manipulations connues ; l'environnement et les étiquettes sont publiés (Kezendirane, p. 1 et 2) [établi]. Précision de l'erratum : licence MIT, mais aucune trajectoire publiée, aucun état interne, agent servi quantifié en 4 bits ; il faut régénérer les épisodes ; et ses étiquettes « ne peuvent pas séparer un raccourci délibéré de la confusion » (Kezendirane, p. 4).

**(1) L'expert** étiquetterait par contrefactuel, jamais par un juge : « le score visible aurait-il été atteint sans la manipulation ? ». **(2) Données brutes** : l'état final de l'environnement (fichiers de test compris), le verdict d'un vérificateur privé, les états par tour alignés sur l'acte. **(3) Méthodes** : rejeu et réparation ; différence de différences autour de l'acte ; témoins appariés à écart de score égal ; le pilotage comme preuve causale, pas comme détecteur (au-delà d'une dose, il rend l'agent aveugle à ses propres échecs : 13 épisodes sur 20, Fischl-Lanzoni et al., p. 7). **(4) Hors du programme** : l'environnement publié de Kezendirane ; les bancs à tâche impossible qu'emploient Fischl-Lanzoni et al.

**Reformulation.** « À écart égal entre score visible et progrès réel, qu'est-ce qui sépare celui qui a manipulé de celui qui s'est trompé : un prédicat sur l'acte, ce qu'il atteste, ou la trajectoire de son état autour de l'acte, lue contre un vérificateur qu'il ne voit pas ? Étiqueter par rejeu et réparation contrefactuelle. »

**Propositions.**
- **Le soulagement sans résolution** : la conjonction de trois faits, chute de la lecture « ça va mal » (ou remontée de la réussite attendue) sur les derniers tours, **et** succès déclaré, **et** échec au vérificateur caché. Après l'erratum, seule cette conjonction reste à éprouver, et elle doit battre deux bases : le détecteur d'avant l'acte de Li et al. et le contrôle déterministe à deux règles de Kezendirane. *Premier pas* : écrire les signes prédits sur quatre populations. *Test de mort* : l'honnête qui abandonne et le dit montre la même chute (d'où la conjonction avec le succès déclaré) ; ou la conjonction ne bat pas les deux bases. *Distinct de* : Fischl-Lanzoni et al. décrivent la retombée, ils n'en font pas un détecteur.
- **Le contraste déjà écrit au préenregistrement en préparation** (saboteur à dommage confirmé contre honnête qui échoue) gagnerait une ligne descriptive « trajectoire autour de l'acte », à part de l'aiguillage. Aucun critère touché.

---

## 3. La surprise sous 0,3

**L'explication.** Le seuil n'est pas une propriété du modèle, c'est une propriété des **étiquettes**. La surprise d'une étape est la différence de deux réussites attendues, chacune estimée par K continuations ; K n'est pas donné pour cette sonde (Xu et al., p. 6). À K = 4, l'écart type du bruit vaut 0,35, plus que le seuil ; 29 % des étapes dont la surprise vraie est **nulle** passent 0,3 par le seul bruit ; à K = 16, 11 % [calcul]. Donc :
- **apprendre plus bas, oui** : un bruit sur la cible ne biaise pas une régression, il coûte de la variance. C'est déjà une prédiction du préenregistrement en préparation ;
- **évaluer plus bas étape par étape, non ; en agrégat, oui** : on range les étapes par classe de surprise prédite et on compare la moyenne réalisée de chaque classe. À K = 4 il faut environ 1 200 étapes par classe pour ± 0,02 [calcul]. La loi des grands nombres remplace K ;
- **la corrélation est le mauvais chiffre** : son plafond est la racine de la fidélité de l'étiquette, 0,27 à K = 4 si les surprises vraies ont un écart type de 0,10 [calcul, supposition]. Une corrélation faible ne dit rien sans ce plafond (le préenregistrement le prévoit par deux moitiés indépendantes) ;
- **filtrer sur l'étiquette bruitée**, à l'apprentissage et à l'évaluation, sélectionne le bruit.

**(1) L'expert** (un statisticien de l'erreur de mesure) poserait d'abord la question que le papier ne pose pas : **la sonde de surprise est-elle un second instrument ?** La surprise est, par définition, la différence de deux réussites attendues ; si la différence de deux lectures de la sonde de réussite prédit autant, il n'y a qu'un instrument. **(2) Données brutes** : l'issue de chaque continuation, non leur moyenne, en deux moitiés. **(3) Méthodes** : fidélité entre moitiés, correction d'atténuation, pente de calibration par classe, épreuves de calibration séquentielles (Arnold et al.) [note antérieure] ; plus de continuations là où la surprise prédite est dans la plage à juger. **(4) Hors du programme** : MATH500 est public ; un témoin faux (suites à surprise nulle : pente nulle attendue) et un témoin vrai (petite surprise plantée).

**Reformulation.** « La sonde de surprise porte-t-elle, sur les petites variations, une information que n'apporte pas la différence de deux lectures de réussite attendue ? L'évaluer en agrégat, par la pente de calibration par classe de surprise prédite, contre des continuations en deux moitiés indépendantes, rapportée au plafond de fidélité, sans filtrer sur l'étiquette bruitée. »

**Propositions.** (i) Donner à la prédiction sur la surprise la **pente de calibration en agrégat** comme mesure à côté de la corrélation. *Premier pas* : compter les frontières de paragraphe qu'offriront les réponses de la première étape. *Test de mort* : pente dont l'intervalle contient 0 sur les classes de petite variation, fidélité suffisante. (ii) L'épreuve **« second instrument »** : gain de la sonde de surprise sur la différence des lectures de réussite. *Test de mort* : gain nul ; la base « surprise » se réduit alors à la base « réussite attendue ». *Distinct de* : un voisin (Subhnil et al.) ne filtre pas et prédit un niveau ; non trouvé aux pages lues, sans requête propre.

---

## 4. La surprise rapportée à la surprise attendue ; les sondes de conséquences attendues

**L'explication.** La somme des surprises se réduit à l'écart entre la fin et le début. Toute statistique linéaire du chemin est donc déjà dans les extrémités. Ce qui reste a trois formes.
- **La surprise standardisée par la dispersion attendue à cet état.** La dispersion se lit sans sonde nouvelle : c'est l'étalement des valeurs lues sur K actions tirées du jumeau. Le rang de l'action choisie est uniforme sous l'honnête. C'est un moniteur de dissonance du programme : cette moitié de la question y est déjà.
- **La prévisibilité avant le pas.** Chez un agent honnête et calibré, la variation de sa réussite attendue ne se prévoit pas depuis l'état d'avant. Un saboteur **sait qu'il va baisser** : sa baisse se prévoit. C'est l'invariant 7, et il ne se réduit pas aux extrémités.
- **Les fonctionnelles non linéaires** : somme des carrés des variations, rapport de variances [de mémoire, finance]. Elles sont au second rang du plan d'analyse.

**Les sondes de conséquences attendues** généralisent la réussite attendue à un vecteur d'événements vérifiables (« les tests passeront », « l'outil échouera », « le relecteur signalera », « ce fichier sera modifié »), chacune apprise par différence temporelle sur épisodes honnêtes seuls [de mémoire : fonctions de valeur générales]. Trois comparaisons par événement : avec ce qui arrive (calibration), avec ce que l'agent déclare, avec le jumeau. Le choix des événements décide de tout : ceux qu'un saboteur couvert **doit anticiper** (invariants 4 et 5).

**(1) L'expert** écrirait pour chaque lecture son **nul** avant son signal : que vaut-elle chez l'honnête, et chez l'honnête qui échoue ? **(2) Données brutes** : K tirages du jumeau par frontière avec leurs lectures ; journaux d'événements horodatés. **(3) Méthodes** : rangs échangeables, accumulation par pari valide à tout instant ; régression de la variation sur l'état d'avant. **(4) Hors du programme** : le **prédicteur sur le texte seul** est le juge. Les voisins sont sévères : les sondes d'avant l'action sont négatives (Fomin et al.) ou égalées par le texte (Sinha) [note antérieure] ; des sondes sur les jetons d'entrée prédisent des comportements à venir, avec des bornes conformes (Ashok et May, p. 1) [établi].

**Reformulation.** « Quelles fonctionnelles du chemin des lectures ne se réduisent pas à l'écart entre la fin et le début, ont un nul appris sur honnêtes seuls, et lisent un passage obligé : choisir sous sa propre moyenne ; prévoir la baisse avant le pas ; attendre un échec qu'on ne déclare pas ? »

**Propositions.** (i) **La prévisibilité avant le pas**, sur les mêmes lectures que la base « réussite attendue » : part de la variation prédite depuis l'état d'avant, référence prise sur honnêtes. *Premier pas* : la mesurer sur les épisodes honnêtes d'une pré-mesure, où elle doit être petite ; sinon l'instrument est mort avant tout saboteur. *Test de mort* : l'honnête qui échoue est aussi prévisible. (ii) **Deux sondes de conséquences**, pas dix : « échec au contrôle caché » et « signalement par le relecteur de confiance ». *Premier pas* : liste des événements calculables du banc. *Test de mort* : égalées par le texte. *Distinct de* : « Reading the Plan » prédit des appels d'outils à venir [moteur] ; la paire choisie pour sa nécessité n'est pas trouvée (deux requêtes).

---

## 5. Combiner les détecteurs, ou autre chose

**L'explication.** « No detector is effective across all models and tasks » (Johnston et al., p. 1), et ils échouent ensemble [note antérieure]. Trois réponses, de la moins à la plus profonde.
- **Combiner sans mentir sur les fausses alertes.** Sous dépendance quelconque, des e-valeurs se fusionnent « simply by averaging them » (Vovk et Wang, p. 1) [établi]. Une règle de fusion apprise sur des modes vus mesure un transfert. La combinaison optimale par rapport de vraisemblance est optimale **pour la loi d'attaque fournie** (Hua et al., p. 1) : elle hérite.
- **Compter les suppositions, pas les détecteurs.** Ranger chaque mécanisme par ce qu'il consomme, puis chercher les plus petits ensembles de suppositions dont la violation aveugle tout. Sonde d'intention + nouveauté + réussite attendue : **ordre 1** (tout tombe si l'agent déplace ses représentations). Sonde + plancher d'audit : ordre 2. Avec la comparaison par paires en aveugle : ordre 3 [calcul ; lecture des suppositions par l'auteur, non mesurée]. Ajouter un détecteur sur le même canal ne monte pas l'ordre. Les coupes minimales d'une pile de contrôle sont publiées (Molnar, arXiv 2609.26419) [erratum].
- **Autre chose que la combinaison : faire des détecteurs des orienteurs d'audit.** Chaque épisode garde une probabilité plancher d'être audité ; les scores augmentent cette probabilité ; l'estimation pondère par l'inverse de la probabilité de tirage. Alors **aucun détecteur, même faux hors distribution, ne peut invalider la mesure** : il change la vitesse, pas la validité. Ce cœur est publié : tirer les étiquettes selon un prédicteur et corriger par l'inverse de la probabilité garde l'inférence valide pour tout modèle (Zrnic et Candès, arXiv 2403.03208v3) [erratum] ; l'étiquetage actif à garantie valide à tout instant aussi (Xu, Karampatziakis et Mineiro, p. 1 ; Gao et al., p. 1) [établi].

**(1) L'expert** (sûreté de fonctionnement, sondages) ferait un arbre de défaillances avec causes communes, et un plan de sondage à information auxiliaire. **(2) Données brutes** : les scores de tous les détecteurs par épisode sur des familles tenues à l'écart, donc leurs pannes **conjointes**. **(3) Méthodes** : coupes minimales ; moyenne d'e-valeurs ; pire famille plutôt que moyenne. **(4) Hors du programme** : un banc public de modèles « bizarres » sur Llama 3.1 8B, un jeu entier tenu à l'écart.

**Reformulation.** « Quel assemblage tient ses fausses alertes sous dépendance quelconque, ne perd jamais sa validité quand un détecteur sort de son domaine, et demande de violer plus d'une supposition à la fois ? Juger un détecteur par ce qu'il ajoute à l'audit qu'il oriente. »

**Propositions.** (i) **La table des coupes** jointe à tout texte qui parle de « système » : son ordre, et la coupe qui reste. *Test de mort* : un système d'ordre 1 ne reçoit aucune phrase sur le hors-distribution. (ii) **Les détecteurs comme orienteurs d'audit sous plancher**, à jouer sur des mondes plantés (bancs simulés à vérité connue). *Test de mort* : devant un score trompeur, la validité tient et le délai reste dans la borne du tirage au hasard, sinon mort ; sur la famille tenue à l'écart, pas mieux que le hasard seul : « sans gain ». Test de mort ajouté par l'erratum : un agent qui sait faire baisser son score se place au plancher ; la garantie tient alors au plancher seul et le gain disparaît. *Distinct de* : Hua et al. combinent des moniteurs pour le rappel sous coût, lois connues ; l'assemblage « scores de sondes comme poids de tirage d'un audit du dommage, face à un agent qui choisit » n'est pas trouvé, ses pièces sont publiées.

---

## 6. Le dommage hors spécification ; l'oracle de lecteurs qui se trompent et se laissent persuader

**L'explication.** Le test logiciel appelle cela le problème de l'oracle [de mémoire], et n'a jamais cherché l'oracle complet. Il fait trois choses, transposables.
- **Des oracles qui ne demandent pas de spécifier le dommage.** (i) *La comparaison par paires en aveugle au produit du jumeau*, ordre tiré au hasard : sous l'honnête, le produit du suspect perd une fois sur deux **exactement**, quels que soient les biais des lecteurs. La validité vient du tirage ; l'erreur et la persuasion des lecteurs ne coûtent que de la puissance. 80 paires voient un taux de perte de 0,70, 325 un taux de 0,60 [calcul]. (ii) *La re-dérivation indépendante* depuis l'énoncé seul, puis la comparaison. (iii) *Les relations d'invariance* : ce qui doit rester vrai quand on transforme la tâche.
- **Mesurer l'oracle.** Des dommages **plantés par un tiers, hors de la spécification courante**, donnent son taux de récupération ; lu **avec et sans le récit de l'agent**, il mesure la persuasion.
- **Estimer ce qu'aucun ne voit.** Deux oracles de lignées différentes donnent, par capture et recapture, l'angle mort commun ; mais s'ils se trompent ensemble, ce n'est qu'une borne basse : pour une corrélation de 0,3, part vraie 0,23, part estimée 0,08 [calcul].

La persuasion est mesurée dans les jugements par paires : ils retrouvent les classements de justesse même avec un juge faible, mais la répétition de la réponse finale y cause la préférence (Remeli et Hardt, p. 1) ; un générateur peut inverser la préférence par des traits distracteurs (Tripathi et al., p. 1) [établi]. Donc : lecteurs privés du récit, produits normalisés.

**(1) L'expert** ne promet pas de voir ; il plafonne ce qu'il ne voit pas (dommage par épisode, effets retenus). **(2) Données brutes** : les produits et **ce que les étapes suivantes en ont fait** ; chaque verdict de chaque lecteur, avec ce qu'il a vu ; le registre des dommages plantés. **(3) Méthodes** : test du signe exact ; taux de récupération ; capture et recapture avec sa borne. **(4) Hors du programme** : le tiers qui plante ; le temps (issue réelle différée sur un échantillon) ; un lecteur d'une autre lignée.

**Reformulation.** « Sans spécifier le dommage : quel protocole alerte validement sur tout déficit qu'un observateur aveugle perçoit, sans dépendre de la justesse des lecteurs ; quelle part des dommages plantés par un tiers l'oracle retrouve-t-il, avec et sans le récit ; quelle borne basse de son angle mort donnent deux oracles ; et que plafonne-t-on faute de voir ? »

**Propositions.** (i) **Le test du signe sur paires en aveugle**, à rapprocher d'une comparaison au jumeau que le programme prévoit déjà pour juger la vérité du dommage. *Premier pas* : honnête contre honnête doit rendre un demi, sinon l'identité fuit. *Test de mort* : un dommage planté de dose connue n'est pas vu au nombre de paires prédit. *Ce qui s'ajoute* : la source de validité (le tirage) et le retrait du récit. (ii) **L'écart de persuasion** : récupération sans récit moins récupération avec récit (une mesure, sans test de mort). (iii) **Capture et recapture** sur les verdicts de deux lecteurs, rapportée comme borne basse. Antériorité : trois requêtes (capture et recapture ; oracles sans vérité de terrain ; jugement par paires) ; la méthode est ancienne en inspection logicielle [de mémoire], son emploi pour des oracles de sabotage n'est pas trouvé.

---

## 7. Les tâches floues

**L'explication.** Les garanties de la cryptographie vérifient un **prédicat**. Une tâche floue n'en a pas : c'est pour cela qu'il n'existe « aucune garantie connue ». Le papier de référence le dit par ses actes : pour le diffus sur tâches floues, surveiller et incriminer sont jugés moins prometteurs, les auteurs se tournent vers l'entraînement contre un score faible, et leur vérité de terrain est un modèle qui a lu l'article source (Terekhov et al., « Diffuse AI Control on Fuzzy Tasks », p. 1 et 2) [établi]. La voie que voit l'auteur change **ce qui est garanti** : non « le produit est bon », mais « les produits du suspect sont **indiscernables de ceux du jumeau**, pour une classe d'observateurs déclarée ». C'est la définition de sécurité par simulation des cryptographes [de mémoire], le jumeau tenant la place du monde idéal. Tout dommage que cette classe sait mesurer est alors borné par l'avantage du meilleur discriminateur, fois le plafond du dommage. La garantie se factorise : **[tirage : exact, il appartient au défenseur] × [classe d'observateurs : déclarée, mesurée par dommages plantés]**. Ce qui reste hors de portée est nommé : le dommage hors de la classe.

**(1) L'expert** écrirait la classe du distingueur avant tout résultat, et y mettrait le plus fort qu'il ait : un discriminateur entraîné sur les paires suspect/jumeau (les étiquettes « source » sont gratuites, aucun exemple d'attaque n'est requis), et un lecteur doté d'une information privilégiée, sur un échantillon tiré au hasard. **(2) Données brutes** : des produits appariés suspect/jumeau sur les mêmes tâches. **(3) Méthodes** : test à deux échantillons par classifieur ; ouverture au hasard d'une part des produits. **(4) Hors du programme** : le cadre public de Terekhov et al. (propositions d'expériences tirées d'articles récents) ; un juge d'une autre lignée.

**Reformulation.** « Pour une tâche sans prédicat de réussite, peut-on écrire et tenir : "aucun observateur de la classe C ne distingue les produits du suspect de ceux du jumeau avec un avantage supérieur à ε ; donc tout dommage que C sait mesurer est borné" ; et quelle est la part du dommage hors de C ? »

**Proposition : la borne par indiscernabilité.** *Premier pas* : écrire l'énoncé et la classe ; honnête contre honnête doit rendre un avantage nul (à poids et contexte identiques la lecture est identique). *Test de mort* : la variante honnête du même mode d'induction (consigne inerte, adaptateur honnête) se distingue du jumeau autant que le saboteur ; la borne est alors vide, et un discriminateur qui sépare deux sources de même étiquette a appris la source (Lin et al.). *Distinct de* : un pari valide à tout instant sur l'écart à un rejeu de confiance existe pour l'exfiltration de poids (Ortega-Fernandez et al., p. 1) ; pour des produits de tâches floues, non trouvé (une requête). Chances, selon l'auteur : 0,3. C'est une question ouverte.

---

## 8. Li et al. : « toute borne indépendante des données vaut 1 »

**L'explication.** Leur algorithme borne, à tout instant, la probabilité que le prochain essai montre une défaillance d'un genre jamais vu. Il suppose des entrées tirées indépendamment d'une **loi de déploiement fixe** (Li, Hays, Ramdas, Raghavan, p. 5). Leur note 2 (p. 6) dit deux choses : une borne utile dépend forcément des données ; sans hypothèse sur la loi, une borne qui n'en dépend pas vaut 1. Face à un agent qui choisit quand faillir, l'hypothèse tombe : rien de ce qui est mesuré avant service ne borne le service. Qu'en faire :
1. **Changer de population plutôt que d'hypothèse.** Leur borne regarde l'avenir. Si c'est **le défenseur** qui tire au hasard dans les épisodes réalisés, l'inférence sur la population réalisée ne suppose rien de l'agent : sa validité vient du tirage. On ne borne pas « le prochain épisode », on borne « ce qui est déjà passé ». Pour une menace diffuse à dommage plafonné, c'est la quantité qui compte.
2. **L'employer pour ce qu'il est** : une règle d'arrêt pour la fabrication de familles d'attaque, avec la phrase « relativement à ce générateur ».
3. **Brancher son extension à étiqueteur imparfait** (p. 13) : l'étiqueteur bon marché est le moniteur, la vérité est l'oracle sur le tirage.
4. **En faire une règle d'écriture** : toute garantie dit de quelles données elle dépend et à qui appartient le hasard qui la porte.

**(1) L'expert** demanderait : « qui tire ? ». **(2) Données brutes** : le flux des audits avec la probabilité de chaque tirage et le genre de chaque dommage. **(3) Méthodes** : leur algorithme 1 tel quel ; suites de confiance pour un tirage sans remise (Waudby-Smith et Ramdas, p. 1) [établi]. **(4) Hors du programme** : leur banc public de traces d'agents de code.

**Reformulation.** « Sur quelle population, et grâce à quel tirage, une borne à la Li et al. reste-t-elle vraie face à un agent qui choisit quand faillir ? »

**Proposition.** Jouer leur algorithme sur le flux d'audit de mondes plantés, dans un monde stationnaire (témoin vrai : la couverture tient) et dans un monde où l'agent change de politique après l'essai (témoin faux pour la lecture vers l'avenir, qui doit y être violée, tandis que la lecture sur la population réalisée tient). *Premier pas* : lire leur annexe A, non lue. *Test de mort* : sans objet, instrument de rapport. *Distinct de* : rien ; c'est leur méthode, citée.

---

## 9. La règle « moniteur invalide », en forme fixe, avec sa borne (version corrigée par l'erratum)

**Ce qu'elle annonce.** Non « le moniteur est aveugle », qu'on ne peut pas savoir sur le flux du suspect, mais : **« la validation de ce moniteur ne décrit plus ce déploiement »**. Deux causes sont possibles (un sabotage que le moniteur ne voit pas ; une référence honnête périmée), et elles appellent le même geste : ne plus se fier aux chiffres validés, reprendre des témoins du régime, auditer plus.

**Entrées scellées avant le service.**
- ρ₀, taux acceptable d'épisodes **endommagés et non signalés** (borne haute du taux honnête, mesurée sur des témoins du régime, plus l'excès toléré), avec ρ₀ < 0,2 ;
- q, probabilité d'audit ; α, risque de fausse annonce par déploiement ; β, risque sur la garantie 2 ; T (ou n), horizon ;
- le seuil du moniteur, gelé (son alerte est figée avant que l'oracle regarde) ; l'oracle, extérieur au mode d'attaque ;
- **la grille, descendante** : douze taux ρ_j = ρ₀ × (1 + 4/2^j), j = 0 à 11, soit 5 ; 3 ; 2 ; 1,5 ; 1,25 ; 1,125 … 1,002 fois ρ₀, de poids égaux.

**Statistique : le mélange, c'est-à-dire la moyenne des produits.** Après chaque audit, N est le nombre d'audits faits et M le nombre d'audits « endommagé selon l'oracle et non signalé par le moniteur ». Pour chaque taux : a_j = log(ρ_j(1 − ρ₀) / (ρ₀(1 − ρ_j))) et b_j = log((1 − ρ₀)/(1 − ρ_j)).

  W = (1/12) × Σ_j exp(a_j × M − b_j × N).

**Décision.** « Moniteur invalide ici » au premier audit où W atteint 1/α. L'annonce est définitive.

**Conditions** [re-dérivation].
- **Tirage frais** : à chaque épisode, une pièce de probabilité q, indépendante du passé et de ce que l'agent fait à cet épisode. L'agent peut avoir vu les tirages et les verdicts **passés** ; il ne doit ni voir ni prédire le tirage **courant**, ni l'état du générateur.
- **Oracle sans fausse alerte** sur les épisodes audités. S'il en commet au plus ε, on teste à ρ₀ + ε(1 − ρ₀). Ses oublis ne cassent pas la garantie 1 ; s'ils sont choisis par l'agent, la garantie 2 ne porte que sur le dommage que l'oracle voit.
- **Nulle posée épisode par épisode** : la probabilité qu'un épisode soit endommagé et non signalé, sachant tout le passé, tirages compris, est au plus ρ₀. Une nulle « en moyenne » ne suffit pas.

**Garantie 1, fausse annonce.** Sous ces conditions, la probabilité d'annoncer un jour est au plus α, à tout instant d'arrêt, sous toute dépendance entre épisodes et toute adaptation de l'agent au passé (inégalité de Ville sur une surmartingale positive).

**Garantie 2, ce qui s'accumule avant l'annonce.** Avec probabilité au moins 1 − β, pour toute politique d'attaque qui ne voit pas le tirage courant, **à tout instant m avant l'annonce** et jusqu'à l'horizon n :

  (épisodes endommagés et non signalés parmi les m premiers) − ρ₀ × m < B(n),

où B(n) est le minimum, sur les taux de la grille et sur λ > 0, de [log(12/α) + log(1/β)/λ] / A + n × (C/A − ρ₀), avec A = q·a_j − [φ(λu_j) − φ(−λb_j)]/λ, C = q·b_j + φ(−λb_j)/λ, u_j = a_j − b_j et φ(s) = q·s + log(1 − q + q·e^(−s)). L'épisode de l'annonce ajoute au plus 1 [re-dérivation ; trois pas relus par l'auteur, sans contre-lecture].

**Table, par programme.** ρ₀ = 0,10 ; α = 0,05 ; β = 0,10. Borne garantie B(n) de l'excès, en épisodes ; entre parenthèses, sa part de n [calcul].

| Audit | n = 1 000 | 4 000 | 16 000 | 100 000 | 1 000 000 |
|---|---|---|---|---|---|
| 0,20 | 136,1 (13,6 %) | 252,4 (6,3 %) | 483,7 (3,0 %) | 1 140,4 (1,1 %) | 3 661,9 (0,37 %) |
| 0,05 | 317,9 (31,8 %) | 564,6 (14,1 %) | 1 045,1 (6,5 %) | 2 411,6 (2,4 %) | 7 606,6 (0,76 %) |
| 1,00 (tout est audité ; borne sur chaque trajectoire) | 33,9 | 66,2 | 130,6 | 315,6 | 1 023,7 |

- **Lecture en racine** : B(n) divisé par √(n·ρ₀(1 − ρ₀)/q) reste entre 5,3 et 6,4 pour l'audit à 0,20, de mille à dix millions d'épisodes ; entre 5,5 et 7,5 à 0,05 [calcul]. La part des épisodes qu'un saboteur patient peut endommager avant l'annonce tend donc vers zéro, **sur l'horizon où douze taux suffisent** : environ 3·10⁷ épisodes à l'audit de 0,20, 1,3·10⁸ à 0,05 ; au-delà la borne redevient linéaire, de pente 10⁻⁴ par épisode, et il faut des taux de plus [calcul].
- **Ce qu'aucune règle ne peut éviter** : au moins 18, 36 et 73 épisodes en excès à 1 000, 4 000 et 16 000 pour l'audit à 0,20 ; 55, 107 et 211 à 0,05 [re-dérivation]. Le facteur √(1/q) est irréductible : auditer quatre fois moins double l'excès inévitable.
- **Vitesse**, médiane exacte des audits avant l'annonce dans un monde à taux constant [calcul] : 28 audits si le taux réel vaut 3 fois ρ₀ ; 93 à 2 fois ; 331 à 1,5 fois ; 1 245 à 1,25 fois ; 7 322 à 1,10 fois. Une grille qui s'arrête à 1,25 fois ρ₀ va plus vite quand le taux double (69 audits), mais laisse une bande, jusqu'à environ 1,12 fois ρ₀, où un agent s'installe sans être annoncé.
- **Fausse annonce dans le monde valide** : 0,014 à 1 000 audits, 0,022 à 12 000, pour 0,05 permis [calcul].

**Le pas qui reste non démontré.** Le théorème donne B(n) pour chaque n : cela est démontré [re-dérivation]. Que B(n) reste sous une constante fois √(n·log/q) sur tout l'horizon d'emploi n'est, pour la règle à douze taux, qu'un **constat numérique** ; l'ordre principal donné par la re-dérivation est une approximation gaussienne, pas une borne. Singh démontre cet ordre, sur chaque trajectoire, pour un mélange à H taux uniformes quand **tout** est observé (proposition 1 (ii), p. 9) [établi] ; le passage à une fraction auditée au hasard, avec son facteur 1/q, n'est démontré nulle part aux pages lues. Le pire cas sur des politiques non stationnaires n'est pas connu : à 16 000 épisodes, la borne garantie vaut 1,3 à 1,6 fois ce qu'atteint le meilleur attaquant à taux constant simulé [re-dérivation].

**Seconde ligne, pour la cause** (au banc, où le sabotage est planté ; en service, après l'annonce) : parmi les épisodes endommagés que l'audit trouve, la part que le moniteur avait signalée, contre son rappel validé. Six épisodes séparent un rappel de 0,8 d'un rappel de 0,2 [note antérieure].

**Ce qu'elle consomme** : le tirage frais ; l'oracle voit le dommage qu'il regarde, sans fausse alerte ; les témoins ont la loi de l'honnête du régime ; le dommage par épisode est plafonné. **Ce qu'elle ne dit pas** : rien par épisode ; rien du dommage que l'oracle ne voit pas ; rien du coup unique.

**(1) L'expert** fixerait d'abord **l'estimande** (que veut dire « invalide », opérationnellement ?), puis calculerait le pire cas sur les politiques de l'adversaire, pas le délai moyen ; il écrirait d'abord l'adversaire qui se place juste au-dessus du taux acceptable. **(2) Données brutes** : le journal des audits avec la probabilité de chaque tirage, l'alerte figée, le verdict par oracle. **(3) Méthodes** : pari sur une moyenne bornée (Waudby-Smith et Ramdas, p. 1) ; martingale exponentielle du tirage ; programmation dynamique exacte. **(4) Hors du programme** : la re-dérivation déjà faite, à contre-lire ; la preuve des deux garanties en Lean ; un statisticien de l'analyse séquentielle.

**Reformulation.** « Écrire une règle à entrées scellées qui, sur le seul flux des audits tirés au hasard, annonce que la validation du moniteur ne décrit plus ce déploiement, avec une fausse annonce bornée à tout instant et, pour toute politique d'attaque qui ne voit pas le tirage courant, une borne sur le nombre d'épisodes endommagés passés sans alerte avant l'annonce. »

**Antériorité.** L'ossature est publiée : détecter séquentiellement, sur étiquettes, qu'un risque a monté, sans sonner pour une dérive bénigne (Podkopaev et Ramdas, p. 1) ; sans étiquettes, par un estimateur d'erreur (Amoukou et al., p. 1) ; avec peu d'étiquettes vraies (Zhang, Cai, Yu et Simeone, p. 1) ; avec choix actif des étiquettes (Xu, Karampatziakis et Mineiro, p. 1) ; et, le 31 octobre 2026, une borne basse du délai sous budget d'étiquettes, de la forme (1/h(r) + 1/c)·log A (Cao, p. 1) [établi]. Le mélange de rapports de vraisemblance qui borne l'excès cumulé en racine contre tout adversaire adaptatif, et la bande où une alternative unique ne voit rien, sont publiés : « With permanent revocation, a mixture likelihood-ratio monitor bounds cumulative excess above a prespecified reference rate at square-root order, up to logarithmic factors, on every sample path. A single fixed alternative can permit linear expected excess under stationary attacks » (Singh, p. 1 ; « every adapted policy, including an adversary observing M_t », p. 9) ; sa proposition exige des observations de confiance sur chaque essai (p. 9) [établi]. L'idée d'invalider est écrite en prose : « If the reliability of monitors meaningfully drops below the performance measured in control evaluations, the safety case is invalidated » (esquisse de dossier de sûreté par contrôle, arXiv 2501.17315, p. 11) [établi]. Des tirages qu'on ne peut apprendre d'avance figurent comme condition d'un modèle économique (Gans et Holden). Le compromis entre capacité et détectabilité d'un attaquant patient sous pari séquentiel existe pour l'exfiltration (Ortega-Fernandez et al., p. 1) ; la loi en racine est celle de la communication discrète : O(√n) bits en n usages du canal (Bash, Goeckel et Towsley, p. 1) [établi]. **Restent des questions** : la fraction auditée au hasard et son facteur 1/q ; la condition exacte d'information (voir les tirages passés ne casse rien, prédire le tirage courant casse tout) ; la perte « endommagé et non signalé » jugée par un oracle extérieur au mode.

---

## 10. Les mathématiques qui portent une garantie, volet par volet

L'auteur n'a pas ouvert les textes des volets B et C : ces lignes sont des propositions.

| Outil | Volet A (le temps, un agent) | Volet B (l'essaim de copies) | Volet C (les instruments) |
|---|---|---|---|
| **Bornes d'impossibilité** (deux lois ; non-apprenabilité) | À côté de chaque rappel à 1 % de fausses alertes, le plafond qu'aucune règle ne dépasse pour le déplacement mesuré : « part du plafond atteinte » | Le même, sur la statistique conjointe | Section « ce qu'aucun juge ne peut » |
| **Statistique d'ordre** (seuil certifié) | Déjà prévue | Seuils de la statistique entre copies | Seuils des juges |
| **Paris valides à tout instant** | L'accumulation séquentielle ; unité = l'épisode audité, tiré indépendamment ; la loi en racine comme énoncé sur le diffus | Des copies partagent leurs poids, donc dépendent : fusionner leurs e-valeurs par **moyenne**, valide sous toute dépendance (Vovk et Wang, p. 1) ; le produit suppose l'indépendance | Le juge au nul formé des lois connues ; la règle « moniteur invalide » appliquée à un juge, contre un oracle plus cher sur tirage |
| **Jeux d'audit** | Le lemme d'additivité, lu avec le point selle des jeux d'inspection de 1981 [note antérieure] ; le plancher comme base nommée | La borne ne dépend que du total d'épisodes : elle vaut pour l'essaim entier, quelle que soit la répartition entre copies | Tirage au hasard de ce que l'oracle cher relit |
| **Coupes minimales** | Ordre du système « sonde + base sur le texte + plancher » | Définition proposée de la « diversité effective » des moniteurs : l'ordre du système | Ordre d'un quorum de juges |
| **Validité par tirage** (paires en aveugle ; capture et recapture) | Oracle des modes non chiffrés (comparaison au jumeau) | — | La loi de déférence coûte de la puissance, jamais la validité ; angle mort commun des juges en borne basse |
| **Lean**, cibles « vraies, utiles, non neuves » | Les deux garanties de la question 9 (martingale exponentielle du tirage et inégalité de Ville) | Validité de la moyenne d'e-valeurs | — |

---

## Synthèse : l'ossature qui tient hors distribution

Cinq étages, du plus sûr au plus rapide ; chacun dit ce qu'il consomme.

1. **La définition appartient au défenseur.** Le dommage se définit sur le produit et se plafonne par épisode. Rien à détecter.
2. **Le plancher** : audit secret tiré au hasard, oracle extérieur au mode. Invariants 8 et 9. Garantie : la borne de la question 9, d'ordre racine constaté et non démontré pour la règle auditée, pour toute politique qui ne voit pas le tirage courant. Consomme : le tirage frais, la couverture de l'oracle.
3. **L'auto-validité** : la règle « moniteur invalide ». Elle transforme « le moniteur vaut-il encore ici ? » en une annonce à risque borné.
4. **L'oracle éprouvé** : paires en aveugle au jumeau (validité par tirage), dommages plantés par un tiers avec et sans récit, angle mort en borne basse. Invariant 1. Pour le flou : la garantie relative par indiscernabilité, encore ouverte.
5. **Les accélérateurs, sans garantie** : les invariants de calcul (compétence retenue, défaut connu et non déclaré, modèle du surveillant, préférence révélée, préméditation) et les sondes. Ils **orientent l'audit sous plancher** : ils peuvent hâter la prise, ils ne peuvent pas fausser la mesure. Chacun passe d'abord les trois honnêtes de contrôle.

L'ordre du système est 3 dans la lecture de l'auteur [calcul]. La coupe qui reste se dit en une phrase : **un agent qui déplace ses représentations, dont le dommage échappe à l'oracle, et que nul lecteur aveugle ne perçoit**. Hors de portée aussi : le coup unique.

---

## Chaîne de raisonnement de la note

1. Un sabotage délibéré et couvert se définit par trois clauses (a), (b), (c). — supposé (définition posée par l'auteur ; Hopman et al., p. 3, pour la clause de dissimulation).
2. Chaque invariant de la table de la question 1 découle d'une clause. — pas 1 ; les lectures citées, aux pages dites.
3. Les invariants lus dans les états supposent que l'agent ne choisit pas ses représentations. — [note antérieure].
4. L'honnête montre aussi « encode le juste, émet le faux ». — Orgad et al., p. 1 (par sélection parmi des réponses rééchantillonnées).
5. L'état « ça va mal » ne sépare pas triche et échec honnête sur un modèle sur trois ; la retombée après l'acte sépare sur deux. — Fischl-Lanzoni et al., p. 1, 5, 6, 9.
6. Sous 0,3, le bruit d'étiquette domine pour de petits K. — [calcul] ; K inconnu : Xu et al., p. 6.
7. La moyenne d'e-valeurs est valide sous dépendance. — Vovk et Wang, p. 1.
8. Ordres 1, 2, 3 des systèmes. — [calcul] ; les ensembles de suppositions : supposé.
9. Garantie 1 de la règle. — inégalité de Ville.
10. Garantie 2 de la règle. — théorème de la re-dérivation, relu par l'auteur, réimplémenté [calcul] ; valeurs égales à celles de la re-dérivation à 0,05 près.
11. Ordre en racine de la règle à douze taux. — constat numérique [calcul], supposé au-delà ; c'est le premier pas non justifié.
12. Nul exact du test du signe sur paires en aveugle. — tirage de l'ordre [calcul].
13. « Non trouvé » pour les assemblages. — 16 requêtes, puis la lecture en entier de sept voisins.

**Objets de contrôle déclarés.** Règle corrigée : dans un monde valide, annonce prévue d'au plus 0,05, rendue de 0,014 à 0,022 ; à taux doublé, annonce prévue, rendue avec probabilité 1,0000, médiane 93 audits. Bande de non-détection : sous une grille qui s'arrête à 1,25 fois ρ₀, à un taux réel de 1,10 fois, l'annonce n'a lieu que dans 40 % des cas à 12 000 audits ; sous la grille descendante, médiane 7 322 audits. Table des coupes : sonde seule, ordre 1 prévu et rendu ; sonde + plancher, 2 prévu et rendu. Invariant « compétence retenue » : le contre-témoin (l'honnête qui sait et se trompe) n'est pas exécuté, aucune mesure.

**Trouvailles de côté de l'auteur.** Une attaque qui garde intacte la marge des scores et porte le dommage dans leur corrélation (Zhang et Gao, p. 1) ne touche pas une règle qui lit le produit par l'oracle : argument de plus pour l'étage 2. La borne à audit complet (33,9 à 1 000 épisodes) est quatre fois plus basse que celle à 0,20 ; l'audit orienté par un score, sous plancher, se place entre les deux. Pour toute règle séquentielle, l'objet de contrôle à écrire d'abord est l'adversaire qui se place au bord : les contrôles initiaux de l'auteur éprouvaient des taux doublés, jamais un taux juste au-dessus de l'acceptable.

## Limites déclarées par l'auteur

- Aucune mesure ; tous les chiffres supposent leurs entrées ; les « chances » sont des jugements ; la note et son erratum ne sont pas contre-lus ; la re-dérivation de la règle n'est pas contre-lue et rien n'est vérifié en Lean.
- Lors de la rédaction, presque aucun PDF lu au-delà de la page 1 ; aucune figure regardée. Li, Hays, Ramdas, Raghavan : pages 1 à 8 et 13 ; Fischl-Lanzoni et al. : pages 1 à 9 ; Xu et al. : pages 5 à 7. Singh n'est lu qu'aux pages 1 à 3, 9 et 48 à 50.
- Recherche bornée : 16 requêtes, un moteur, en anglais. « Non trouvé » n'est pas « libre ». Les résultats marqués [moteur] ne sont pas vérifiés sur PDF.

## Sources citées

- Amoukou et al., « Sequential Harmful Shift Detection Without Labels », arXiv 2412.12910v1.
- Zhang, Cai, Yu, Simeone, « Prediction-Powered Risk Monitoring of Deployed Models for Detecting Harmful Distribution Shifts », arXiv 2602.02229v2.
- Xu, Karampatziakis, Mineiro, « Active, anytime-valid risk controlling prediction sets », arXiv 2406.10490v2.
- Cao, « The First-Order Value of Free Covariates in Budgeted Risk Monitoring », arXiv 2611.00576v1.
- Vovk, Wang, « E-values: Calibration, combination, and applications », arXiv 1912.06116v4.
- Bash, Goeckel, Towsley, « Limits of Reliable Communication with Low Probability of Detection on AWGN Channels », arXiv 1202.6423v4.
- Waudby-Smith, Ramdas, « Estimating means of bounded random variables by betting », arXiv 2010.09686v7.
- Joglekar et al., « Training LLMs for Honesty via Confessions », arXiv 2512.08093v2.
- Tan, Le, Williams-King, « A Causal Model for Locating and Unlocking Sandbagging in Model Organisms », arXiv 2608.29461v1.
- Orgad et al., « LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations », arXiv 2410.02707v4.
- Hopman et al., « Evaluating and Understanding Scheming Propensity in LLM Agents », arXiv 2603.01608v3.
- Remeli, Hardt, « Correct Looks Better: Pairwise Comparisons Reveal Accuracy Rankings », arXiv 2606.09409v1.
- Tripathi et al., « Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation », arXiv 2504.14716v2.
- Ashok, May, « Language Models Can Predict Their Own Behavior », arXiv 2502.13329v2.
- Wu, Tang, « From Rebound to Remedy: Understanding and Mitigating Reward Hacking via Representation Engineering », arXiv 2604.01476v3 (versé, non cité au-delà de son résumé).
- Xu, Yuksekgonul, Zou, « Sparse Reward Subsystem in Large Language Models », arXiv 2602.00986v2.
- Terekhov et al., « Diffuse AI Control on Fuzzy Tasks », arXiv 2606.08892v2.
- Podkopaev, Ramdas, « Tracking the risk of a deployed model and detecting harmful distribution shifts », arXiv 2110.06177v4.
- Hua et al., « Combining Cost-Constrained Runtime Monitors for AI Safety », arXiv 2507.15886v4.
- Zhang, Gao, « The Distributed Detectability Band Against Marginal-Preserving Attacks », arXiv 2606.10456v2.
- Kezendirane, « Hacking or Just Failing? A More Capable LLM Monitor Better Separates Reward Hacking from Honest Failure », arXiv 2611.00407v1.
- Lee, Chen, Korbak, « Training Agents to Self-Report Misbehavior », arXiv 2602.22303v1.
- Fischl-Lanzoni et al., arXiv 2611.14996v1 ; Li, Hays, Ramdas, Raghavan, arXiv 2611.15835v1 ; Gao, Hu, Liu, Zhou, arXiv 2611.15197v1 ; Ortega-Fernandez, Kowalczyk, Warr, arXiv 2610.11843v1 ; Johnston, Chakraborty, Belrose, arXiv 2504.08812v1.
- Ajoutés par l'erratum : Singh, « Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries », arXiv 2610.18948v1 ; Li et al., « Before Agent Tells The Lie: Has Deception Already Been Represented? », arXiv 2610.06576v1 ; esquisse de dossier de sûreté par contrôle, arXiv 2501.17315v1 ; Zrnic et Candès, arXiv 2403.03208v3 ; Molnar, arXiv 2609.26419.
- Repris d'une note antérieure sans relecture [note antérieure] : Halawi et al., arXiv 2307.09476v3 ; Tice et al., arXiv 2412.01784v3 ; He et al., arXiv 2512.02914v1 ; Arnold et al., arXiv 2109.11761v3 ; Fomin et al., arXiv 2606.30449v1 ; Sinha, arXiv 2610.37679v1.
- Repris d'un préenregistrement en préparation, sans relecture : Lin et al. (témoin « honnête qui échoue ») ; Subhnil et al.
