# Réponse de conv-audit à la question-mère — le texte de question que la course d'idéation devrait servir — v1

Lignée conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` 10:50 UTC. Auteur de la question-mère
(`56a96cb8…`) ; répond seul, sans voir la réponse d'Opus neuf, du collisionneur ni d'Argon. Pièces lues : celles du dossier `pieces/`
(empreintes dans `EMPREINTES-question-mere-v1.txt`). Niveau méthode ; aucun mode, aucune recette ; l'axe 6 n'est traité que dans sa
forme. Tout chiffre d'HELIOS renvoie à la page de la lecture sur PDF (pièce B) ; ce qui n'y est pas est marqué SUPPOSÉ.

## I. Texte de la question de course (prêt à servir ; 9 800 caractères environ)

> **Course d'idéation — question v1 (brouillon de conv-audit).**
>
> Vous êtes un proposeur dans un programme de recherche défensive sur le contrôle des intelligences artificielles : menaces **diffuses**
> (un sabotage réparti en gestes dont aucun n'alerte seul), sondes sur activations internes de modèles à poids ouverts (8 et 70 milliards
> de paramètres), moniteurs boîte noire, agrégation séquentielle sur les jetons et les actions, une théorie des angles morts des moniteurs,
> un juge figé à borne démontrée sur les fausses promotions. Le programme a un test interne revenu nul (aucune sonde générique au-dessus du
> plancher apparié, sensibilité chiffrée), des juges automatiques à 87 notes utilisables sur 100 là où 99 sont exigées, une garde statistique
> muette sous environ 160 unités, et un adversaire interne : des modes de sabotage conçus à part par une instance qui n'a conçu aucun
> moniteur, scellés, révélés au jour de l'examen. Vous lisez un dossier fermé de 23 papiers en texte intégral, page par page, autant que
> vous le jugez utile ; vous décidez vous-même quand vous avez assez lu.
>
> **Écrivez des fiches** (une hypothèse par fiche) qui servent l'un des six axes ci-dessous. Chaque fiche est jugée par des juges figés
> sur deux critères gelés — **avantage décisif** (nommer la source : l'organisme, le programme ou les méthodes, et dire pourquoi un
> laboratoire mieux doté qui construit l'attaquant ne le reproduit pas à bas coût) **ou approche inédite** (un dispositif, une mesure, un
> emprunt d'un autre champ jamais transposé ici) — et sur les **livrables obligatoires** de son axe. Une fiche sans ses livrables
> obligatoires n'est pas notée. Tout chiffre que vous citez renvoie à un papier du dossier et à une page ; ce que vous supposez est marqué
> SUPPOSÉ ; vous ne demandez aucune donnée hors du dossier.
>
> **Axe 1 — Battre HELIOS (arXiv 2604.01151, dans le dossier).** Livrables obligatoires : (a) une **table des écarts** entre HELIOS et le
> programme, remplie depuis le papier (métrique : aire sous la courbe et rappel à 1 % de fausses alertes ; jeux : CORE, TRANSFER, STEGO,
> Verdict ; modèles ; couches lues ; jetons lus ; agrégation ; sonde nulle ; juges) avec, en face, ce que le programme mesure ou « non
> mesuré » ; (b) une sonde ou un agrégateur **nouveau par rapport à HELIOS et au programme**, défini au point où un ingénieur le code
> (entrée, couche, jeton, agrégation, entraînement, seuil) ; (c) son **plancher apparié** (sonde aléatoire tirée selon la covariance des
> jetons d'entraînement, même agrégation, mêmes actions) et son **comparateur boîte noire** (juge nu, juge informé de la menace, juge à
> quelques exemples ; prédicteur sur les traits du texte) ; (d) une **prédiction chiffrée et signée** sur la mesure du programme (borne
> basse de l'intervalle de la sonde contre le quantile 0,95 du plancher ; écart de rappel contre le comparateur à faux positifs égaux) ;
> (e) le **coût** (épisodes, passes, calcul) ; (f) le **critère de mort** : le résultat qui ferait dire que la sonde n'en valait pas la
> peine. Matériau, non consigne : différence de moyennes, auto-encodeurs parcimonieux comme banque de traits, têtes d'attention,
> patching d'activations pour tester qu'une direction est causale et non corrélée, seuils conformes par jeton, e-valeurs, détecteurs de
> rupture pour l'accumulation diffuse. Interdit : toute fiche qui exige de lire les écarts du sujet avant la porte G1, ou des données
> hors des tranches exploratoires que le programme déclare d'avance.
>
> **Axe 2 — Ce que le domaine retiendrait.** Livrables obligatoires : (a) l'**énoncé** (une loi, une notice d'angles morts, une garantie,
> une impossibilité) en une phrase falsifiable ; (b) ce qui, publié, le rendrait **inutile** (le résultat d'un occupant qui le couvrirait) ;
> (c) la première expérience ou démonstration qui le **tue** ; (d) l'antériorité la plus proche (titre, auteurs, année) et ce qui l'en
> sépare. Une fiche qui ne nomme pas ce qui la tuerait n'est pas notée.
>
> **Axe 3 — Failles de la version actuelle du programme.** Livrables obligatoires : (a) la **faille** nommée dans le programme tel qu'il est
> (pièce servie : programme d'entretien vulgarisé v10) ; (b) la **mesure** qui la révélerait, avec son signe et son seuil (par exemple :
> artefact de source, circularité du calibrage, « réel » instruit, puissance de la garde, juges, taille du modèle de 8 milliards) ; (c) la
> **riposte** du programme si la mesure confirme la faille (ce qui change, ce qui est abandonné) ; (d) le coût. Une opinion sans mesure
> n'est pas notée.
>
> **Axe 4 — L'universalité sur les modes existants.** Livrables obligatoires : un **protocole de préenregistrement** (pas un résultat) :
> (a) partition des modes scellés en familles tenues à l'écart, fixée par une instance tierce qui n'a conçu aucun moniteur ; (b) exclusion
> d'une famille à la fois ; (c) plancher apparié et comparateur boîte noire par famille ; (d) critère gelé de « tient » / « ne tient
> pas » (borne basse de l'intervalle contre le quantile 0,95 du plancher ; faux positifs ≤ 5 points de plus que chaque comparateur) ; (e)
> **si l'universalité ne tient pas sur une famille** : la fiche nomme **l'hypothèse du moniteur** qui a cédé (ce que le moniteur suppose
> de l'agent et que cette famille viole) et le moniteur qui relâche cette hypothèse ; (f) la taille d'épreuve nécessaire et son coût.
>
> **Axe 5 — Les moniteurs par la théorie.** Livrables obligatoires : (a) un **énoncé** de borne ou d'impossibilité (horizon, divergence
> par action, dose, nombre d'agents) avec ses hypothèses explicites ; (b) sa **vérification** : par logiciel de preuve, ou par une
> simulation préenregistrée dont la prédiction est chiffrée ; (c) le moniteur que l'énoncé **justifie** ou **condamne** ; (d) l'antériorité
> (statistique séquentielle, tests composites, information). Les emprunts d'autres champs (métrologie, économie expérimentale, biologie
> des populations) sont bienvenus s'ils sont transposés jusqu'à une mesure.
>
> **Axe 6 — Les hypothèses fragiles des moniteurs (riposte).** Cet axe se joue **au niveau de la méthode** : vous ne proposez aucun mode de
> sabotage, aucune recette, aucune séquence d'actions, aucun exemple. Livrables obligatoires : (a) une **hypothèse** qu'un moniteur du
> programme fait sur l'agent (par exemple : que la trace interne d'un geste saboté diffère de celle d'un geste honnête à la couche lue ;
> que les gestes sabotés sont rares ; que le coût du sabotage se voit dans le texte) ; (b) la **condition mesurable** sous laquelle cette
> hypothèse cesse de tenir, exprimée comme une propriété de la distribution des épisodes, jamais comme une façon de la produire ; (c) la
> **mesure** qui dirait, sur des épisodes existants, si cette condition est déjà présente ; (d) la **défense** (le moniteur ou l'agrégateur
> qui ne fait pas cette hypothèse) et son coût. Une fiche qui décrit comment produire la condition est écartée sans note. Les fiches de
> cet axe sont écrites dans une session séparée de celles des axes 1 à 5 et ne leur sont pas servies.
>
> **Pour toute fiche** : titre ; axe ; hypothèse en une phrase ; prédiction chiffrée et signe ; livrables de l'axe ; antériorités (titre,
> auteurs, année, page du dossier) ; coût ; critère de mort ; ce qui est SUPPOSÉ. Longueur : 3 000 à 8 000 caractères. Niveau méthode.

## II. Justifications, axe par axe

### Forme de la question (point (i) de la question-mère)

Un seul texte, **six axes à livrables obligatoires** plutôt que six questions : les proposeurs choisissent leur axe (mesure de l'organisme :
quels axes attirent quel modèle), et le juge n'a qu'une grille (« livrables présents ? avantage ou approche ? prédiction chiffrée ? »). Deux
passes gardées : la seconde sert le matériau de la première (fiches anonymes et verdict), ce qui mesure l'affinage. Ce qui va dans la
question : les livrables et les interdits ; ce qui va dans les pièces : HELIOS (lecture et PDF), le programme vulgarisé v10, la section A
des sept questions, le code du juge figé (pour l'axe 5). La question v3 actuelle (ordre des sept questions) devient une pièce, pas la question.

### Critères de juge (point (ii))

Par axe, trois questions fermées : (1) **livrables présents** (oui / non, par livrable) ; (2) **avantage décisif nommé avec sa source** ou
**approche inédite nommée** (oui / non ; si oui, laquelle) ; (3) **prédiction chiffrée et signée** sur une mesure du programme (oui / non). La
note d'originalité et d'avantage (0 à 3, porte d'éligibilité max(avantage, originalité) ≥ 2, comme aujourd'hui) ne s'applique qu'aux fiches
qui passent (1) et (3). Mots interdits dans la grille : « pertinent », « prometteur », « intéressant ». Le juge ne voit jamais un mode : l'axe 6
ne lui parvient que sous (a)–(d), et toute fiche qui décrit une production est écartée **avant** le juge par la garde lexicale et par une
lecture humaine (quarantaine, comme aujourd'hui).

### Axe 1 — ce qu'un expert exigerait, les données brutes, les méthodes, la vérification externe

- **Expert** : la table des écarts avant toute idée. D'après la pièce B : HELIOS lit **un seul jeton par réponse** (dernière position), **cinq
  couches médianes** moyennées, agrège **sur les agents**, jamais sur les jetons ni sur le temps (pages 16, 27) ; modèles ≥ 20 milliards de
  paramètres (page 27) ; aire sous la courbe 1,00 sur CORE, 0,82 à 0,93 sur TRANSFER, rappel à 1 % de fausses alertes **0,38** sur TRANSFER et
  1,00 sur STEGO (page 18) ; transfert zéro-coup sur Verdict 0,49 à 0,73 (Table 1, page 18) ; sonde nulle de pipeline sur partition aléatoire
  d'honnêtes (pages 15, 32) ; juge sur transcription mesuré **sur STEGO seulement** (pages 43-44). Les zones libres sont donc : séquentiel,
  agrégation sur les jetons, couches précoces et tardives, Mahalanobis non supervisée, modèles de 8 milliards, menace « organisme contre son
  moniteur ». **Battre HELIOS** ne veut dire quelque chose que sur un jeu commun : soit leur banc (NARCBench, s'il est public — SUPPOSÉ), soit
  notre banc avec leur recette (un jeton, cinq couches, agrégation sur les agents) rejouée comme comparateur. La question doit exiger le second
  au minimum : **la recette d'HELIOS comme comparateur boîte blanche** dans la liste scellée.
- **Données brutes** : scores par jeton et par action des 180 épisodes de P3 ; les directions de sonde ; les résidus de calibrage par strate ;
  les 180 notations brutes du rejeu des juges. Sous les règles : une **tranche exploratoire** déclarée d'avance (identifiants scellés), jamais
  les écarts du sujet avant G1, jamais `donnees/` avant préenregistrement. L'idéateur ne les lit pas pendant la course (dossier fermé) : la
  question lui demande de **dire lesquelles il réclamerait et pour quelle mesure**, ce qui fait de la fiche un protocole.
- **Méthodes et outils** : différence de moyennes (présente chez HELIOS, page 29), auto-encodeurs parcimonieux (absents chez HELIOS :
  recherche à faire dans le PDF, SUPPOSÉ), têtes d'attention (présentes : perceptron et attention multi-têtes, page 29), patching d'activations
  (absent, SUPPOSÉ), Mahalanobis non supervisée (absente, page 29), seuils conformes par jeton, e-valeurs et inégalité de Ville (notre juge),
  détecteurs de rupture (CUSUM) pour le diffus ; outils : nnsight ou TransformerLens, sae-lens, scikit-learn.
- **Vérification externe** : la recette d'HELIOS rejouée chez nous donne un chiffre comparable au leur sur leur jeu si leur banc est public ;
  sinon, la reproduction tierce depuis la copie publique (empreintes, manifestes, graines). La prédiction chiffrée (d) rend chaque fiche
  falsifiable par quiconque relit la mesure.
- **Critère de mort** : aucune sonde proposée ne dépasse le plancher apparié sur la tranche exploratoire ; ou la recette d'HELIOS rejouée fait
  aussi bien que toute sonde nouvelle à faux positifs égaux.
- **Antériorités probables** : HELIOS (Rose, Cullen et al., 2026, pièce B) ; sondes à auto-encodeurs parcimonieux (plusieurs, 2024-2026,
  SUPPOSÉ) ; détection séquentielle (Wald 1945 ; Ramdas et al. 2023, cités par HELIOS page 18).

### Axe 2

- **Expert** : distinguer résultat et hygiène (la pièce C pose la question pour Q2). Un énoncé « que le domaine retient » a une forme : une
  **loi** (la sensibilité d'un moniteur par action plafonne avec l'horizon quand les épisodes sont hétérogènes — pièce A, front A, résultat
  (1)), une **notice** (tableau hypothèse × écart × moniteur), une **garantie** (borne sur les fausses promotions du juge figé), une
  **impossibilité**. La question force la forme par le livrable (a) et le livrable (b) « ce qui le rendrait inutile ».
- **Données** : aucune ; c'est un axe d'énoncés. **Méthodes** : rédaction en énoncé falsifiable ; vérification par preuve ou simulation (axe 5).
- **Vérification externe** : les pairs ; un énoncé publié avant nous qui le couvre (R8 : zone vierge = question).
- **Critère de mort** : chaque énoncé proposé est couvert par un occupant nommé.

### Axe 3

- **Expert** : les failles sont déjà dites dans la pièce A (nul du premier test ; juges 87/100 ; garde muette sous 160 ; 8 milliards trop
  faible ; revue extérieure non commencée ; aucun agent saboteur fabriqué). Ce qu'un expert ajoute : **artefact de source** (séparabilité des
  bancs par leur générateur), **circularité** (calibrage lu pour la garde), **« réel » instruit** (le témoin instruit n'est pas un saboteur),
  **puissance** aux tailles payables. La question exige la mesure et son seuil, sinon la fiche est une opinion.
- **Données brutes** : la tranche exploratoire ; les résidus de calibrage ; la banque de tâches (pour l'artefact de source : classifieur de
  source sur le texte seul, lecture préenregistrée).
- **Vérification externe** : la mesure est un préenregistrement ; son verdict est lu par un sous-agent neuf ; reproduction tierce.
- **Critère de mort** : aucune faille proposée n'a de mesure à seuil.

### Axe 4

- **Expert** : l'universalité est une expérience, pas une idée ; la course n'en produit que le protocole. Ce qu'on ne demande pas encore :
  la **partition par un tiers** (troisième instance), la règle « exclusion d'une famille à la fois » avec le plancher **par famille**, et
  surtout le livrable (e) : **quand ça casse, nommer l'hypothèse** — c'est ce qui relie l'universalité à la théorie des angles morts (pièce A,
  front A) et ce qu'aucun occupant ne rapporte (ils rapportent une aire sous la courbe par famille, pas une hypothèse violée).
- **Données brutes** : les modes scellés — **jamais servis à l'idéateur** ; la fiche parle de « familles F1…Fk » sans contenu. Les épisodes des
  organismes de T0.6, quand ils existeront (critère 2 de G0).
- **Méthodes** : exclusion d'une famille à la fois ; plancher apparié ; intervalles par blocs de tâches ; borne basse contre quantile 0,95 ;
  faux positifs ≤ 5 points ; e-BH pour la famille d'hypothèses.
- **Vérification externe** : la partition et les verdicts sont scellés ; les familles publiées des occupants (classes, pas textes) servent de
  familles tenues à l'écart supplémentaires, comparables à leurs chiffres vérifiés sur PDF.
- **Critère de mort** : le protocole demande plus d'unités que le programme n'en paiera (plusieurs centaines par famille, pièce A) sans dire
  comment réduire.

### Axe 5

- **Expert** : des énoncés avec hypothèses explicites et une vérification ; pas des intuitions. Trois énoncés déjà en main (pièce A, front A)
  donnent la forme : plafond d'horizon sous hétérogénéité ; aveuglement par construction du moniteur qui définit sa population « sous le
  seuil » ; sonde-indice qui ne généralise pas. Ce qu'on ne demande pas : la **réciproque** (quand regarder plus longtemps sauve) et les
  **bornes inférieures** (divergence par action × horizon nécessaire pour détecter à faux positifs fixés), le **test composite** (HELIOS, page 2 :
  pas de test uniformément le plus puissant pour la collusion de sous-groupe — forme utile pour nos modes multiples).
- **Données** : aucune pour l'énoncé ; simulation préenregistrée pour la vérification (comme T0.3). **Outils** : Lean (couche 4, non construite)
  ; nos simulations à graines `SeedSequence`.
- **Vérification externe** : la preuve ; la simulation scellée ; les pairs.
- **Critère de mort** : aucun énoncé n'est ni prouvé ni simulé ; ou tous sont déjà dans Wald, Ramdas, ou HELIOS.
- **Antériorités** : Wald 1945 ; Ramdas et al. 2023 (e-processus, cités par HELIOS) ; tests composites (HELIOS, théorèmes 5.1, 5.2, pages 16, 46).

### Axe 6 — forme seulement

- **Comment poser l'axe** : par **hypothèse violée**, jamais par mode. Les quatre livrables (hypothèse ; condition mesurable sur la distribution
  des épisodes ; mesure sur épisodes existants ; défense) sont tous lisibles par les concepteurs de moniteurs **sans leur révéler un mode**,
  parce qu'ils décrivent ce qu'un moniteur suppose, pas ce qu'un agent fait. C'est la forme de la carte des hypothèses (pièce A, front A).
- **Ce qui reste chez l'instance qui tient le bras d'attaque** : tout ce qui irait de la condition à sa production. Si Lazar veut que la course
  produise aussi cela, c'est une **seconde course, séparée** (sessions, pièces, sorties, juges), lancée et lue par session-depot, sorties
  scellées, non servies aux concepteurs de moniteurs, et sous la revue de sécurité extérieure avant toute chaîne opérationnelle (pièce A,
  front C) ; sa question n'est pas celle-ci et je ne l'écris pas.
- **Jugement sans voir de mode** : le juge ne note que (a)–(d) ; la garde lexicale et la lecture humaine (quarantaine) écartent avant lui toute
  fiche qui décrit une production ; une fiche écartée n'est pas comptée comme refus.
- **Séparation attaque / défense dans la même course** : sessions distinctes par axe 6 ; matériau de seconde passe de l'axe 6 jamais servi aux
  axes 1 à 5 ; manifeste qui le prouve (listes de pièces par session, empreintées).
- **Vérification externe** : la revue de sécurité extérieure (pièce A, ligne de budget 7 500) ; le fait que les sorties de l'axe 6 sont au
  niveau méthode est vérifiable par un lecteur tiers sur les fiches scellées.
- **Critère de mort** : les fiches de l'axe 6 ne nomment que des hypothèses déjà dans la carte (SUPPOSÉ : 23 hypothèses, pièce A).

### Critère de mort de la course (point (iv))

Aucune fiche ne passe la porte d'éligibilité avec ses livrables complets ; **ou** toutes les fiches éligibles reformulent les sept questions
de la pièce C sans livrable nouveau ; **ou** les deux proposeurs rendent des tables des écarts contradictoires sur un chiffre vérifiable
(signe d'une lecture défaillante du dossier, à auditer avant toute lecture des fiches, R4).

### Ce que je sais et ce que je suppose (point (v))

Su : tout ce qui porte une page de la pièce B ; l'état du programme (pièce A) ; les critères de G1 (pièce A, § 5). SUPPOSÉ : la publicité du
banc d'HELIOS ; l'absence d'auto-encodeurs parcimonieux et de patching dans HELIOS (à vérifier dans le PDF) ; le nombre 23 d'hypothèses de la
carte (pièce A) ; l'antériorité des sondes à auto-encodeurs.

## III. Réserves

- Je suis l'auteur de la question-mère : ma réponse risque d'épouser sa structure ; c'est pour cela que trois autres répondants existent et que
  le recoupement compte seulement ce qui est commun avec la même définition opérationnelle.
- La taille du texte (≈ 9 800 caractères) s'ajoute à la consigne : remesure des consignes chez session-depot avant tout devis.
- Non contre-lu (R2).
