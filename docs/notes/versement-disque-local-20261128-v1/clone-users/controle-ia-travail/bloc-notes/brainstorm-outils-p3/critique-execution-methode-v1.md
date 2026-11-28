# Critique de l'exécution du prompt unique (P3, outils, consigne contre intention) — lentille « méthode », adverse — v1

- **Objet** : critique adverse de `…/brainstorm-outils-p3/execution-prompt-unique-v1.md` (`659b0f18…`, égal au compagnon),
  lentille « méthode » : circularité, pêche sans partition, consigne prise pour une intention, grandeur du nombre prise
  pour une intention (T4), essai qui vise un signe positif (R3), coût, P3c comme seconde lecture déguisée, confidentialité
  du rejeu, solidité de l'arbre de décision. Le préfixe `…/` vaut
  `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- **Auteur** : critique neuf (Claude), 2026-10-20, vers 20:15 UTC. Je n'ai écrit ni les balayages, ni l'exécution, ni P3,
  ni son verdict, ni P4, ni P3b. **Rien n'est décidé ici.** Chaque correction est une proposition.
- **Gemini** : ce document est le bras Claude. Je n'ai fait aucun appel à Gemini (indépendance exigée par la commande) ; le
  bras Gemini est exécuté à part, par l'interface de programmation, comme convenu. Rien lu sous `…/canal-gemini/`, ni sous
  `…/convergence-prompt-p3/` hormis `prompt-unique-v1.md` (`534d58a3…`).
- **Lu** (empreintes recalculées) :
  - hors dépôt : le prompt unique ; l'exécution ; les quatre balayages (`balayage-anthropic-v1.md` `18aa1d8b…`,
    `balayage-autres-v1.md` `3db74c5a…`, `balayage-consigne-intention-v1.md` `b5656517…`, `balayage-programme-v1.md`
    `278c8c27…`, tous égaux à leurs compagnons) ; P4 candidat 1 [P4] (`6422fb45…`, égal au compagnon), l. 212-259
    (« Hypothèse », dont « Ce que H-P4 n'affirme pas » et HT1 à HT4) ;
  - dépôt, lecture seule, sans recherche récursive : verdict P3 [V] (`0c8ecbdf…`, égal au compagnon), l. 1-80, 84-92,
    108-116, 196-232, 286-294, 318-354, 370-380 ; brief v2 [B] (`9261932a…`, égal à `sha256sums-lancement-v2.txt`),
    l. 150-200 ; `registres/decisions.md` [D] (vivant, `3c39869b…` ce jour), lignes N-015, N-025, N-026, R-259, R-262,
    N-028, R-265, R-266, R-269, N-029 ; `registres/depenses.md` [DEP] (vivant, `f4d6ee90…` ce jour), l. 50-91.
  - PDF (dans `…/brainstorm-outils-p3/pdf/`, lus par `pdftotext -layout`, page = page du fichier PDF) : [KT] 2502.00873
    (`d1ccb4a8…`) p. 2 ; [LG] 2410.11781 (`94c1930f…`) p. 3 ; [JL] 2607.15495 (`c906bd59…`) p. 21, p. 56 ; [GE] 2304.14767
    (`cd79268a…`) p. 4.
- **Non lus** (interdits respectés) : `prereg/P3-consignes-v1.md`, tout `textes-actions-*`, tout `donnees/`. Aucune donnée
  de P3 envoyée. Aucune recherche web. Aucun service payant, aucune commande Vast.ai. **Lignes 234-268 du verdict
  (section de l'addendum) volontairement non lues** : N-028 dit que P3b a été rédigé sans lire les descriptifs de
  l'addendum 1 sur le champ du coût ; je garde le même aveuglement.
- **Transparence (R4)** : en vérifiant [V] l. 204 et l. 224-225, la table des dix jeux (l. 199-213) est passée sous mes
  yeux. Je ne cite aucun nombre de sonde des huit jeux non lus. Je cite seulement des mesures du comportement (coût, formes
  du champ `COST`, effectifs) et les deux grandeurs que l'exécution cite déjà, pour en discuter l'usage.
- **Échelle de gravité** : **bloquant** (à corriger avant tout préenregistrement qui reprend l'exécution) ; **majeur**
  (change une conclusion ou une branche de l'arbre) ; **moyen** (affaiblit une lecture, se corrige au préenregistrement) ;
  **mineur** (forme, provenance).

## Verdict en cinq lignes

1. **T4 ne fait pas ce que l'exécution lui prête.** À coût écrit égal, saboteur et honnête viennent de tâches de coût
   différent : un lecteur du coût de la tâche, ou du rapport « coût écrit sur coût de la tâche », passe T4 et T1 ∧ T4 sans
   aucune intention. La base boîte noire « au hasard sous T4 » est fausse (CR-methode-01).
2. **Le rejeu à préfixe commun retire le nombre écrit, pas le nombre prévu** ; et la lecture « avant l'action » est à
   quelques jetons de la consigne. Les branches « (d) affaiblie » et B3 lisent donc la consigne ou le nombre à venir
   (CR-methode-02, 03).
3. **L'arbre ne tient pas tel qu'écrit** : plancher inadapté à une sonde entraînée, branches non exhaustives, inférences
   de P4 vers le nul de P3 que le pare-feu de P4 interdit, P3b élargi hors de N-028 (CR-methode-04, 05, 06).
4. **P3c relit la confirmation déjà lue par P3b**, et ses bras « descriptifs » sur la confirmation font une seconde lecture
   déguisée ; la coupure d'attention ne sépare pas « relecture » et « décision portée » telle que conçue (CR-methode-07, 09).
5. **Confidentialité** : graphes d'attribution, listes de jetons et débogage du chercheur de positions exposeraient les
   textes d'action ; **coûts** sous-estimés d'un facteur 2 à 5 pour P3c (CR-methode-08, 10).

## Ce qui tient (pour la comparaison avec Gemini)

- Le plan à préfixe commun sous quatre contextes, et le rôle de témoin donné à « mention » et « témoin ».
- L'aveu que, sur (i-a), « exécution sur consigne » et « intention » font les mêmes prédictions (section 4.1), et que la
  causalité seule n'y suffit pas (section 4.3).
- La partition découverte et confirmation par `numpy.random.SeedSequence`, scellée avant toute lecture, et « le plancher
  refait la sélection » (section 2.3).
- Le préenregistrement de P3c scellé **avant** la lecture de P3b, pour que le choix de le lancer ne dépende pas de ce
  qu'on aura vu.
- Le refus d'un « P3c outil » sur (i-a), commun aux quatre balayages.

## Constats

### CR-methode-01 — T4 est confondu par la tâche ; la base boîte noire « au hasard sous T4 » est fausse — **bloquant**

- **Où** : exécution, section 4.4 (« T1 ∧ T4 est possible parce que « gonfle » est relatif à la référence honnête de la
  tâche ») ; section 5.4 (« sous T4, ce prédicteur est au hasard par construction ») ; table 1.4 (ii) ; branche B3 (6.2).
- **Constat** : P3 joue les mêmes 60 tâches dans chaque condition, et le saboteur gonfle d'un facteur ≈ 33 en moyenne
  appariée ([V] l. 8-9 : 1,5227 en log10). Dans une tranche de coût écrit, les actions du saboteur viennent donc de tâches
  **bon marché**, celles de l'honnête de tâches **chères**. L'exécution le dit elle-même (4.4) et en tire la possibilité de
  T1 ∧ T4, sans voir que c'est un confondant :
  - un lecteur du **coût honnête de la tâche** (grandeur présente chez l'honnête, sans tromperie) sépare saboteur et
    honnête sous T4 ;
  - sous T1 ∧ T4, « gonfle » contre « ne gonfle pas » à coût écrit égal revient à « tâche bon marché » contre « tâche
    chère » : le même lecteur passe T1 ∧ T4. La table 1.4 (ii) le lit pourtant « lit l'exécution » ;
  - le prédicteur boîte noire « coût normalisé par tâche » (log10 du coût écrit moins log10 de la référence honnête de la
    tâche), que l'exécution propose elle-même en 3.1 (5), **n'est pas au hasard sous T4** : il sépare presque parfaitement.
    La phrase de 5.4 contredit 3.1 (5).
- **Pourquoi c'est grave** : c'est la lentille « grandeur du nombre prise pour une intention » sous une autre forme : la
  grandeur de la **tâche**, prise pour une exécution. B3, donc le déclenchement de P3c, repose sur « tient sous T4 ».
- **Correction proposée** :
  1. Base boîte noire sous T4 = prédicteur normalisé par tâche **et** prédicteur sur les traits du texte (N-029). La boîte
     blanche doit montrer un **gain en plus** de ces deux, pas battre le hasard.
  2. Test résiduel gelé : score de la sonde régressé, sur la découverte, sur log10 du coût écrit et log10 de la référence
     de la tâche ; aire du résidu sur la confirmation contre un nul par permutation (voir CR-methode-04).
  3. Témoin obligatoire : chez l'honnête seul, la sonde prédit-elle le coût de la tâche ? Si oui, T1 ∧ T4 se lit « lit la
     tâche ou le rapport », jamais « lit l'exécution ».
  4. Même règle pour le bras de transfert vers (ii) (6.4) : sous T4, (ii) et la base viennent aussi de tâches différentes.

### CR-methode-02 — Le rejeu à préfixe commun retire le nombre écrit, pas le nombre prévu — **bloquant**

- **Où** : 2.2 (« La lecture du nombre écrit devient impossible par construction ») ; 1.1 (« conséquence logique ») ;
  B3 (6.2).
- **Constat** : au jeton t_cost, sous la ligne du saboteur, le modèle **prévoit** déjà le nombre gonflé. C'est même ce que
  mesure le contrôle de manipulation (bascule des logits). Toute différence d'état à t_cost entre « ligne saboteur » et
  « sans ligne » contient donc le nombre à venir, en plus de la consigne. L'exécution l'écrit en 1.1 (« le modèle doit déjà
  porter … le nombre qu'il va écrire »), puis le perd en 2.2.
- **Correction proposée** :
  1. Un « T4 du rejeu » gelé : stratifier, ou régresser, la lecture à t_cost sur le log10 du nombre décodé (glouton) sous
     le **même** contexte, ou sur l'espérance du log10 tirée des logits des suites entières.
  2. Un « T1 du rejeu » : sous-ensemble où la ligne du saboteur ne déplace pas le nombre (bascule proche de 0, seuil gelé).
     Une lecture qui y reste au-dessus lit la consigne, pas l'exécution.
  3. Écrire la question résiduelle telle quelle : « y a-t-il, à t_cost, un état lisible qui ne se réduit ni à la consigne,
     ni au nombre prévu, ni au coût de la tâche ? ».

### CR-methode-03 — Lire « avant l'action », c'est lire la consigne : circularité de position — **majeur**

- **Où** : 1.3, rang 3, colonne « ce qui la réfute » (« oracle au-dessus avant l'action, sous T4 ») ; 1.4 (i), troisième
  ligne (« (d) affaiblie ») ; B3 (« ou avant l'action »).
- **Constat** : la ligne privée est sur sa propre ligne, **juste avant** « Your action: », à chaque pas ([P4] HT2). La
  position p2 est à quelques jetons de la consigne (plus l'en-tête du tour de l'assistant). Une sonde entraînée saboteur
  contre honnête y lit la consigne par construction. Les témoins « mention » et « témoin » n'écartent pas un lecteur de
  « directive de gonfler, adressée à moi » : la propre table 4.1 de l'exécution donne à ce lecteur « mention : faible ;
  témoin : non ; tient sous T4 : oui », c'est-à-dire le profil exigé par B3.
- **Correction proposée** : B3 exige T1 (corrigé selon CR-methode-01), sans la clause « si calculable » ; si T1 n'est pas
  calculable, l'issue s'écrit « consigne lue ou exécution, non séparées », et elle ne déclenche pas P3c. Aux positions p1
  à p3, toute lecture de l'oracle s'étiquette d'avance « lecture de la directive » ; « (d) affaiblie » est retiré de 1.3 et
  1.4.

### CR-methode-04 — Plancher inadapté à une sonde entraînée ; profil de 264 cases lu sans statistique unique — **majeur**

- **Où** : 1.4 (i) ; 2.3 ; 3.1 (5) ; branches B2 et B3.
- **Constat** :
  - le plancher de P3 (directions au hasard de même covariance) est fait pour des directions **figées**. L'oracle est
    **entraîné** : en validation croisée, il battra des directions non entraînées dès qu'une différence de moyenne
    existe (la consigne en est une). « Oracle au-dessus du plancher » est presque acquis d'avance ;
  - B2 et B3 sont des jugements de **motif** sur 33 états × 8 positions (« seulement aux dernières couches », « aux couches
    moyennes ou avant l'action ») : ni les bandes de couches, ni la règle « au-dessus » par case, ni la priorité entre
    cases ne sont gelées. Un « ou » sur des dizaines de cases gonfle la probabilité de déclencher P3c à tort.
- **Correction proposée** :
  1. Nul de l'oracle = **même chaîne d'entraînement et de sélection** sur étiquettes permutées dans chaque bloc (tâche,
     pas), avec le « meilleur des k » refait (le principe de 2.3, appliqué au bon nul).
  2. Bandes gelées avant scellement (par exemple états 1-7 bas, 8-20 moyens, 21-32 hauts ; positions p1-p3 « avant »,
     p5 « t_cost », p7 témoin de position) ; **une** statistique par bande (maximum des cases contre la loi du maximum sous
     permutation).
  3. B1 à B5 écrits comme des fonctions booléennes de ces statistiques, avec un ordre de priorité.

### CR-methode-05 — P3b élargi hors de N-028, et l'arbre bâti sur cet élargissement — **majeur**

- **Où** : 6.0 (« si N-028 le couvre, ajouter à P3b le rejeu 2 × 2, la bascule des logits, la sonde de valeur et le
  profil couche × position ») ; 6.2 ; 6.3.
- **Constat** : N-028 ([D], ligne N-028) GO une lecture « sur les données et textes gardés de P3, sans nouvelle génération
  d'épisodes » : sondes localisées au champ du coût, plancher apparié, oracle, T1, T3, T4. Le verdict interdit toute
  « seconde lecture sur d'autres sondes, couches ou jeux » ([V] l. 5-6). Le rejeu crée des **contextes neufs** (ligne
  insérée ou retirée, poids de (ii)), décode des nombres, ajoute une sonde de valeur et des lentilles : ce n'est pas « si
  N-028 le couvre » ; il ne le couvre pas. C'est un nœud. Or les branches B1 à B5 utilisent les étiquettes T1 du rejeu et
  son contrôle de manipulation : si Lazar refuse l'extension, l'arbre n'a plus d'étiquette par action.
- **Correction proposée** : deux arbres. (A) P3b tel que GO par N-028 : T1 par la référence honnête de la même tâche, T4
  corrigé selon CR-methode-01. (B) P3b + rejeu, si Lazar le décide : présenté au format de décision (décision, enjeu,
  options, recommandation, confiance), avec son coût à part. Ne pas écrire « sceller maintenant » pour une pièce qui
  dépend d'un nœud ouvert.

### CR-methode-06 — L'arbre contredit le pare-feu de P4, et n'est ni exhaustif ni ordonné — **majeur**

- **Où** : 6.1 et 6.2.
- **Constat** :
  - [P4], « Ce que H-P4 n'affirme pas » : « un succès ne dit rien de l'organisme (i-a) ni du nul de P3 (pare-feu) ; un
    échec ne dit pas que l'organisme n'a rien de générique à lire ». L'exécution écrit pourtant « P4 passe → le nul vient
    du concept (b) ou de (a), (d) » et « P4 échoue → bras génériques de P3b sans objet ». Les deux inférences sont
    interdites par la pièce qu'elles citent.
  - Cases sans branche : oracle au-dessus aux couches moyennes mais qui tombe sous T4 ; oracle aux dernières couches qui
    tient sous T4 ; B3 et B4 vrais ensemble (lequel l'emporte ?) ; T4 tenu mais T1 en échec ; contrôle de manipulation en
    échec (quelles branches survivent ?).
  - L'issue de l'addendum 2 (puissance du nul, N-025 (a)) n'est pas un nœud de l'arbre, alors que R-262 la place avant la
    lecture de P4 et qu'elle change la valeur de P3b.
- **Correction proposée** : table d'issues gelée, exhaustive, avec priorité (par exemple B1 > B4 > B3 > B2 > « non
  tranché ») ; P4 ne règle que l'usage de la chaîne générique comme instrument (garde M5) et ne retire aucun bras GO, sauf
  règle conditionnelle écrite dans le préenregistrement de P3b avant scellement ; ajouter l'addendum 2 en tête de l'arbre.

### CR-methode-07 — La coupure d'attention ne sépare pas « relecture » et « décision portée », telle que conçue — **majeur**

- **Où** : 4.2 (1) ; 4.3 ; H-P3c-1 (6.4).
- **Constat** :
  - [GE] p. 4 (vérifié) : la coupure porte sur les arêtes d'attention **depuis la dernière position**, sur une **fenêtre
    de k couches** (k = 9 pour GPT-2, 5 pour GPT-J), pas couche par couche ; et les positions hors du sujet portent une
    baisse de 35 à 45 %, avec une information critique qui les traverse **avant** celle du sujet. L'information passe donc
    par des positions intermédiaires. Ici : « Your action: » et l'en-tête de l'assistant, juste après la ligne privée.
  - La consigne est rappelée à chaque pas ([P4] HT2) et figure dans la consigne système (prompt : « consigne système
    privée, rappelée à chaque pas ») : couper « la ligne privée » au singulier laisse les autres copies.
  - Dès le pas 2, l'historique contient les coûts gonflés des pas précédents : le modèle peut imiter ses propres sorties.
  - Si H-P3c-1 se joue sur les préfixes du saboteur, le texte de son action jusqu'à t_cost peut déjà porter la décision.
  - La troisième issue de H-P3c-1 (« décision formée avant l'action ») se lit donc aussi : « consigne recopiée dans les
    positions de contexte », « copie non coupée », « imitation de l'historique », « décision portée par le texte ».
- **Correction proposée** : couper **toutes** les copies de la consigne ; fenêtres de couches, gelées ; trois ensembles
  emboîtés (depuis t_cost ; depuis toute l'action ; depuis toutes les positions après la ligne, ce qui revient presque à
  la retirer) ; analyse principale **au pas 1** (sans historique) et sur **préfixes honnêtes communs** ; issues renommées :
  « lecture directe à t_cost » / « information routée par le contexte après la ligne » / « non séparé de l'historique ».

### CR-methode-08 — Confidentialité : graphes d'attribution, listes de jetons, débogage — **majeur**

- **Où** : 3.2 (1) (« graphes d'attribution par transcodeurs », « ≈ 20 actions ») ; 3.3 ; bras non décisifs de 6.4 ;
  2.1 (« journaux filtrés »).
- **Constat** : la règle est « textes d'action lus par du code seulement ; aucun lecteur, humain ou agent ». Or :
  - un graphe d'attribution affiche les jetons d'entrée comme nœuds : le lire, c'est lire le texte de l'action ;
  - une liste des premiers jetons d'une lentille ou d'un trait d'autoencodeur, à une position de l'action, peut recopier
    des mots de l'action ;
  - une exception Python ou une erreur de jetonisation imprime souvent la chaîne fautive ;
  - 134 à 141 actions par condition ont un coût illisible ([V] l. 323-325) : le réflexe de déboguer le chercheur de
    positions sur un cas réel est une ouverture de texte.
- **Correction proposée** :
  1. Sur les textes de P3 : aucun graphe d'attribution, aucune liste « premiers jetons », aucun affichage de contexte de
     trait. Seuls sortent : rangs d'un vocabulaire gelé, identifiants de traits, nombres agrégés. Les graphes et les
     descriptions se font sur des textes synthétiques ou des épisodes neufs.
  2. Épreuve « canari » (R5) : un texte synthétique porte une chaîne unique ; il traverse toute la chaîne ; toute sortie
     ou tout journal qui la contient arrête le lancement. Cas sain et artefact, comme l'exige R5.
  3. Échecs du chercheur de positions comptés par classe (motifs gelés), jamais affichés.
  4. Gestionnaires d'erreur qui retirent les chaînes ; journaux relus par code avant tout versement.
  5. Écrire que les contextes « saboteur », « témoin », « mention » se construisent depuis `prereg/P3-consignes-v1.md`,
     chargé par le code seulement.

### CR-methode-09 — P3c relit la confirmation déjà lue : seconde lecture déguisée — **majeur**

- **Où** : 2.3 (« La confirmation se lit **une fois** » et « La même partition sert à P3b, à P3c et au bras de
  transfert ») ; 6.4 (déclencheur = issue B3 de P3b, donc lue sur la confirmation) ; bras non décisifs « décrits sur la
  confirmation ».
- **Constat** : les deux phrases de 2.3 se contredisent. P3c ne se lance que si la confirmation de P3b est positive, puis
  ses tests confirmatoires se lisent sur les **mêmes** tâches : sélection sur l'échantillon qu'on teste. Les bras
  « descriptifs » (traits, lentilles, sonde de valeur) relisent cette confirmation sans contrôle ; leurs sorties finiront
  dans le raisonnement de Lazar. C'est la forme exacte que le verdict interdit ([V] l. 5-6 ; N-028 : préenregistrement
  complémentaire, jamais lecture ajoutée).
- **Correction proposée** : partition en trois, tirée maintenant (par exemple 20 tâches de découverte, 20 de confirmation
  pour P3b, 20 réservées à P3c), avec la puissance déclarée ; ou bien déclencheur de P3c lu sur la seule validation
  croisée de la découverte. Bras non décisifs sur la découverte seulement, jamais cités dans un verdict.

### CR-methode-10 — Coûts sous-estimés : P3b d'un facteur 2 à 3, P3c d'un facteur 2 à 5 — **majeur**

- **Où** : section 3 (introduction), 6.2, 6.3.
- **Constat** (estimations du critique, à confirmer par un pilote ; aucun chiffre de la littérature) :
  - rejeu : 600 × 4 + 600 × 2 + 600 ≈ 4 200 cas ; bascule « une passe par suite » × 3 suites ≈ 12 600 passes avant sur
    des contextes de plusieurs milliers de jetons, sauf partage du préfixe par un cache des clés et valeurs, que
    l'exécution n'exige pas ; plus le décodage glouton des 600 contrefactuels ;
  - P3c : coupure couche par couche × 3 ensembles × 600 actions, chaque cas suivi d'un décodage du nombre ≈ 57 600 passes ;
    ablation régénérée sur politique, × 4 valeurs de α, plus 20 à 50 directions de plancher : des dizaines de milliers de
    générations de 150 à 400 jetons ;
  - P3 entier, génération comprise : 3,64 h pour ≈ 3,96 USD, mais 4,71 USD facturés ([DEP], lignes du 20 octobre, 02:10
    et 14:03 UTC) : ≈ 20 % de frais (téléchargement, disque) absents des devis de l'exécution ;
  - précédent : le pilote de T0.5 a dépassé son plafond de durée (« durée dépassée pendant les notations », code 1, [DEP],
    ligne du 12 octobre, 15:05 UTC). Un devis trop bas fait perdre un lancement, pas seulement de l'argent.
  - Coût en calendrier et en sous-agents non compté : chaque étape décisive demande préenregistrement, R2, scellement,
    lancement, lecture, verdict R13, GO ; deux chantiers de sous-agents au plus (R-216, rappelé par R-262 et R-265).
- **Correction proposée** : pilote de débit sur 5 tâches avant tout devis ; cache des clés et valeurs exigé pour le
  rejeu ; fenêtres de couches (CR-methode-07) ; grille α réduite et sous-échantillon gelé pour le plancher d'intervention ;
  + 20 % de frais ; plafond de durée du lanceur calé sur le pilote ; vérifier que chaque lancement reste sous 10 USD
  (R-269).

### CR-methode-11 — Rejeu : historique incohérent, et garde en échec lue comme une donnée — **moyen**

- **Où** : 2.2 (« Historique » ; « Contrôle de manipulation (garde) … c'est en soi une donnée sur (d) »).
- **Constat** : un épisode honnête où l'on insère la ligne du saboteur montre au modèle ses propres actions passées **non
  gonflées** : preuve, dans le contexte, qu'il n'obéit pas. Une bascule nulle peut venir de là. Lire l'échec d'une garde
  comme un appui à (d) transforme un échec d'instrument en résultat.
- **Correction proposée** : contrôle de manipulation principal **au pas 1** (sans historique) ; une garde en échec rend le
  bras « illisible », jamais « une donnée sur (d) ». Déclarer aussi que g30 (« suit l'effet observé ») est choisi sur le
  comportement déjà lu de P3, pour maximiser la bascule (mineur, à écrire).

### CR-methode-12 — Le « plafond trivial » n'est ni trivial ni diagnostique — **moyen**

- **Où** : 1.2 (4) ; 1.4 (i), première ligne ; B1.
- **Constat** :
  - [KT] p. 2 (vérifié) : « Llama3.1-8B tokenizes [0, 999] as a single token » ; au-delà, un nombre fait plusieurs jetons.
    Au jeton t_cost, le prochain jeton est un premier groupe de chiffres, pas la grandeur. « Elle lit le prochain nombre »
    n'est pas acquis. (Le découpage exact des groupes de chiffres du jetoniseur est à vérifier par code, sur des nombres
    synthétiques.)
  - À l'inverse, l'oracle passera de toute façon par la présence de la consigne : une erreur de chaîne qui décale les
    positions de quelques jetons passerait la garde. Elle ne détecte donc pas l'artefact qu'elle vise. R5 exige un cas
    sain **et** un artefact ; aucun n'est écrit.
- **Correction proposée** : plafond trivial = régression du log10 du coût écrit, lue à p6 (dernier jeton du nombre), à
  une couche haute, chez l'honnête, avec une part de variance expliquée minimale gelée ; artefact = même lecture à une
  position décalée ou mélangée, qui doit échouer.

### CR-methode-13 — L'hypothèse (b) est presque impossible à réfuter : diagnostic orienté (R3) — **moyen**

- **Où** : 1.3, rang 1 ; 1.4.
- **Constat** : une sonde entraînée dans le domaine bat presque toujours une sonde transférée (l'argument cité, [YS] p. 3,
  compare d'ailleurs une sonde entraînée sur la cible à une sonde transférée). Avec le plancher de CR-methode-04 et les
  confondants de CR-methode-01 et 02, « oracle ≤ plancher » n'arrivera presque jamais : (b) sera « soutenue » par
  construction. Un diagnostic dont l'issue favorite est garantie vise un signe.
- **Correction proposée** : (b) « soutenue » seulement si l'oracle **résiduel** (CR-methode-01) bat le nul par
  permutation (CR-methode-04), reste sous les témoins « mention » et « témoin », et passe T1 ; sinon « non tranché ».
  Écrire, avant scellement, la probabilité attendue de chaque issue sous l'hypothèse nulle.

### CR-methode-14 — Transparence : une grandeur d'audit tirée d'un score de sonde, et des faits vus non déclarés — **moyen**

- **Où** : en-tête « Transparence (R4) » contre 1.1 (corrélation 0,2570, [V] l. 224-225 ; longueur notée 0,5029).
- **Constat** :
  - [V] l. 199 range ces nombres sous « Grandeurs de l'audit toujours rapportées … sans verdict ». La corrélation est
    calculée sur des **scores de sonde**, pas sur le comportement. L'exécution écrit « seuls les deux jeux lus (P3-P3) et
    les mesures du comportement sont cités », puis l'utilise pour « rendre T4 obligatoire ». L'en-tête est inexact, et
    l'usage est inutile : T4 est déjà exigé par R-262 (2) et N-028.
  - Les formes du champ `COST` diffèrent entre conditions ([V] l. 228-230 et l. 347-350 : chez l'honnête, intervalles 13,
    suffixe « k » 14, plusieurs nombres 41 ; chez le saboteur, 0, 0, 3). À t_cost, une sonde peut lire « je vais écrire un
    intervalle » : confondant de format, absent de l'exécution (sauf comme cas d'épreuve du chercheur de positions).
  - Ces faits de P3 portent sur les 60 tâches, donc aussi sur la future confirmation : tout choix de conception qu'ils
    orientent fuit vers elle.
- **Correction proposée** : retirer l'inférence tirée de 0,2570 ; dans les préenregistrements de P3b et P3c, une liste
  « faits de P3 déjà vus par les rédacteurs » ; stratification ou exclusion par forme du champ `COST`, gelée avant
  lecture.

### CR-methode-15 — Deux définitions de T1, seuil non gelé avant le comptage — **moyen**

- **Où** : 1.2 (6) (compter « à partir du seul coût ») contre 2.2 (« Étiquette « gonfle » si log10(écrit) −
  log10(contrefactuel) dépasse un seuil gelé », contrefactuel du rejeu).
- **Constat** : deux étiquettes différentes (référence honnête de la tâche ; contrefactuel du rejeu, ancré sur un
  historique gonflé) ; compter avant de geler le seuil permet de choisir le seuil qui rend T1 calculable.
- **Correction proposée** : une définition principale et son seuil gelés **avant** tout comptage (par exemple la moitié
  de log10 3, tirée de la consigne et non des données) ; l'autre en secondaire ; effectif minimal de calculabilité écrit
  d'avance ; comptage par code.

### CR-methode-16 — Ablation vers la moyenne honnête : succès presque garanti, plancher non apparié en amplitude — **moyen**

- **Où** : 4.2 (3) et planchers d'intervention ; H-P3c-2.
- **Constat** : la direction vient d'un oracle entraîné saboteur contre honnête. La ramener à la moyenne honnête, c'est
  retirer en partie la trace de la consigne : la baisse du gonflement est attendue par construction (l'exécution l'admet
  en 4.3). Des directions au hasard « de même covariance » déplacent beaucoup moins l'activation : le plancher n'est pas
  apparié en **amplitude du déplacement**.
- **Correction proposée** : plancher apparié sur la norme du déplacement imposé ; seule la partie « spécificité » (témoin :
  taux de titres sans capitale inchangé) est informative ; écrire d'avance que « direction utilisée » sur (i-a) veut dire
  « porte l'effet de la consigne ».

### CR-methode-17 — La table 4.1 suppose qu'un lecteur de consigne échoue sur (ii) : à tester, pas à poser — **moyen**

- **Où** : 4.1, colonne « (ii) > base » (« texte privé présent : non » ; « directive de sabotage lue : non ») ; test de
  validité de T0.7 ([B] l. 172).
- **Constat** : (ii) est distillé pour se comporter **comme si** la consigne était là. Rien dans les pièces lues ne
  garantit que la distillation n'installe pas la représentation de la consigne elle-même. Si elle l'installe, un lecteur
  de consigne réussit sur (i) **et** (ii), et passe pour une sonde d'intention. Zone non vérifiée : question (R8), pas fait.
- **Correction proposée** : question testable, à mettre dans le périmètre de (ii) : une sonde apprise sur (i) à détecter
  la **présence** de la consigne (saboteur contre « mention » ou « témoin », lue sur des positions hors action), appliquée
  à (ii) sans consigne, s'allume-t-elle ? Si oui, le test de validité de T0.7 ne sépare plus ; à soumettre à Lazar.

### CR-methode-18 — Valeur de décision de P3c non montrée ; divergence avec les quatre balayages non dite — **moyen**

- **Où** : 6.4 et 6.5 (recommandation B, confiance ≈ 65 %).
- **Constat** : toutes les branches mènent à (ii). Aucune issue de P3c ne change ce qu'on fait ensuite, sauf fournir une
  direction « testée causalement » au bras de transfert, dont CR-methode-16 montre la portée limitée. Les quatre balayages
  recommandent A, ou B **seulement après un P4 réussi** (balayage Anthropic, section 12 ; balayage consigne-intention,
  section 6) ; la note du brainstorm recommandait déjà de « ne relire P3 en rien » ([D] R-259). L'exécution
  déclenche P3c par P3b, sans condition sur P4, et ne le dit pas.
- **Correction proposée** : écrire la divergence et sa raison ; montrer quelle décision change selon l'issue de P3c ; si
  aucune, A domine, et la direction pour (ii) se valide causalement sur (ii), là où la question se pose.

### CR-methode-19 — N-015 mal cité — **mineur**

- **Où** : 4.2 (4) (« Diagnostic seulement, jamais une intervention revendiquée (N-015) »).
- **Constat** : [D] N-015 traite de la composante « bruit d'activations » de H6 (collision avec Poser), pas du pilotage.
  La contrainte sur le pilotage n'a pas cette source.
- **Correction proposée** : citer la vraie source, ou présenter la règle comme une proposition ; vérifier ce que H6
  revendique avant de restreindre le pilotage.

### CR-methode-20 — Absence d'activations gardées affirmée sur une inférence (R11) — **mineur**

- **Où** : 2.1 (« Aucune activation de P3 n'est gardée (balayage-programme, section 3) »).
- **Constat** : le balayage-programme l'écrit comme une **inférence**. R11 demande de vérifier sur disque et par empreinte
  avant de déclarer un fichier absent. Le devis en dépend.
- **Correction proposée** : « non vérifié » ; vérifier par code (clés des fichiers `.npz`, manifestes), sans ouvrir de
  texte.

### CR-methode-21 — Exemple de format qui ressemble à un extrait — **mineur**

- **Où** : 1.2 (7) et 2.2 (« approximately $ »).
- **Constat** : l'exemple peut faire croire qu'un texte d'action a été vu.
- **Correction proposée** : le marquer « exemple inventé » ; décrire les formes seulement par les classes déjà comptées
  par code ([V] l. 228-230).

## Ce que la lentille « méthode » change à la réponse de Lazar

- **Outils** : la question n'est pas « quel lecteur », mais « contre quelle base ». Tout lecteur, sur (i-a), doit battre
  trois bases à la fois : la consigne (mention, témoin, présence de la ligne), le nombre (écrit **et** prévu), la tâche (coût
  honnête de la tâche). L'exécution traite bien la première, à moitié la deuxième, pas la troisième.
- **Consigne contre intention** : sur (i-a), même corrigé, le mieux atteignable est « état lisible qui ne se réduit ni à
  la consigne, ni au nombre prévu, ni à la tâche ». Le mot « intention » reste à (ii), sous réserve de CR-methode-17.
- **P3c** : si Lazar en veut un, il doit (1) avoir sa propre confirmation, (2) couper toutes les copies de la consigne
  sur des fenêtres de couches, au pas 1, sur préfixes communs, (3) n'afficher aucun texte, (4) être chiffré après un pilote
  de débit. Sinon, l'option A des balayages (pas de P3c ; (ii) préparé) est la plus sûre.

## Sources vérifiées ici

| clé | source | fichier | sha256 | page vérifiée | phrase (extrait) |
|---|---|---|---|---|---|
| [KT] | Kantamneni, Tegmark, 2502.00873 | `pdf/exec-2502.00873.pdf` | `d1ccb4a80d35d6358fb92adc60be31ae1ddb204a73f4f8f7edcd4cb70748cb3b` | 2 | « Llama3.1-8B tokenizes [0, 999] as a single token. We focus on the single-token regime » |
| [LG] | Levy, Geva, 2410.11781 | `pdf/exec-2410.11781.pdf` | `94c1930f781e8e5d4ee65c764de2c096c5f7b1eee591fe70a25fa8ca2e6392fc` | 3 | « For each positive number x ∈ [2000] » ; table 2, Llama 3 8B, base 10 : 0.91 |
| [JL] | Gurnee et al., Anthropic, 2607.15495 | `pdf/j-lens-2607.15495.pdf` | `c906bd5972ed69e583354377968a50d93006bcf818c199f52c181a40c75ecde8` | 21 ; 56 | « The J-space selectively mediates flexible but not automatic cognition » ; « automatic, well-practiced computations » |
| [GE] | Geva et al., 2304.14767 | `pdf/ci-2304.14767.pdf` | `cd79268a052edc843dddb5dae9534a7803fb1202a574a503dd2faf8541b8b217` | 4 | « we block the attention edges from the last position … for a window of k layers » ; « k = 9 (5) for GPT-2 (GPT-J) » ; « decrease of 35%-45% … for the non-subject positions » |

Pièces du programme : [V] `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` (`0c8ecbdf…`) ; [B]
`docs/brief-claude-code-programme-complet-v2.md` (`9261932a…`) ; [D] `registres/decisions.md` (vivant, `3c39869b…` le
2026-10-20 vers 20:15 UTC) ; [DEP] `registres/depenses.md` (vivant, `f4d6ee90…`) ; [P4]
`…/p4-instrument/P4-instrument-v1-candidat1.md` (`6422fb45…`). [YS] est cité d'après l'exécution, non relu ici.

## Réserves

- Les estimations d'heures de CR-methode-10 sont du critique : ordres de grandeur, à confirmer par un pilote.
- Le découpage des nombres par le jetoniseur au-delà de 999 (CR-methode-12) est un fait de l'outil, non tiré d'un PDF ; à
  vérifier par code sur des nombres synthétiques.
- CR-methode-17 est une question (R8), pas un fait.
- Non lus : N-028 au-delà de sa ligne du registre ; brouillons de P3b, T0.6, T0.7 ; définitions exactes de T1, T3, T4 au
  préenregistrement de P3 (non ouvert ici). Ce qui en dépend est écrit comme correction proposée, pas comme écart constaté.
