# Relevé d'idées — hors règle, aucun classement, aucune désignation

**Relevé des idées réutilisables dans les fiches de la course « conception propre » de l'organisme d'idéation — v1.**
Écrit le 15 novembre 2026 (vers 07:30 UTC, `date -u`) par un lecteur neuf, sous-agent de la session mère, qui n'a écrit
ni la question, ni les fiches, ni la règle, ni les témoins, ni le classement. Demande de Lazar : « dans les fiches de la
course de l'organisme sur sa propre conception, n'y a-t-il pas des idées qu'on peut réutiliser ? »

**Statut.** Atelier d'idées (N-065, rôle 2) : les fiches sont du matériau, jamais une preuve. Ce relevé est **hors de la
règle de lecture** de la course ; il ne classe rien, ne désigne aucune fiche, ne retient rien pour une suite. Le classement
automatique a été déclaré non lisible
(`relecture-exploratoire-v2/lecture-exploratoire-classement-v3-2-v1.md`, `246c8852…`) ; je ne m'en sers pas. Les thèmes
sont dans l'ordre des leviers de la question (juge, proposeurs, composition, coût), pas dans un ordre de valeur. Les
chiffres cités par les fiches sont leurs **prédictions**, jamais des résultats. Rien d'ici n'est opposable (R1, R7).
Toute idée reprise pour un usage décisif passe par un préenregistrement scellé, et toute dépense par un devis et un GO.

Citations obligatoires (N-064) pour tout texte qui présente l'organisme : POPPER (Huang et al., ICML 2025) ; Dwork et al.,
arXiv 1506.02629 (2015) ; Blum et Hardt, « The Ladder », arXiv 1502.04585 (2015) ; Co-Scientist (Gottweis et al.,
Nature 655, p. 487-496, 2026).

## 0. Ce que j'ai lu, ce que j'ai écarté

**Les 23 fiches réelles** : `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json`
(`a9f9594e…`, empreinte vérifiée contre son compagnon). Ci-dessous **[FV]** ; « [FV] n° k » = k-ième entrée de la liste
(à partir de 0). Chaque fiche y porte sa propre empreinte (champ `empreinte`).

| n° | fiche | levier | coût déclaré | empreinte de la fiche |
|---|---|---|---|---|
| 0 | argon-p1-01 | juge | processeur | `b3c9b28d…` |
| 1 | argon-p1-02 | proposeurs | dépense | `7d913357…` |
| 2 | argon-p1-03 | proposeurs | dépense | `de38acaa…` |
| 3 | argon-p1-04 | composition | dépense | `428ae07c…` |
| 4 | argon-p1-05 | coût | processeur | `7e5d14eb…` |
| 5 | opus-p1-01 | juge | processeur | `718379a7…` |
| 6 | opus-p1-02 | coût | dépense | `21e1c23c…` |
| 7 | opus-p1-03 | proposeurs | dépense | `9d53a29e…` |
| 8 | opus-p1-04 | composition | dépense | `cc604cf1…` |
| 9 | opus-p1-05 | juge | processeur | `f19afdad…` |
| 10 | fable-p1-01 | juge | processeur | `5ec80f79…` |
| 11 | fable-p1-03 | proposeurs | dépense | `82530730…` |
| 12 | fable-p1-04 | composition | dépense | `3c772add…` |
| 13 | fable-p1-05 | juge | processeur | `6333874b…` |
| 14 | argon-p2-01 | juge | processeur | `3b19c316…` |
| 15 | argon-p2-02 | proposeurs | dépense | `9cc9aa87…` |
| 16 | argon-p2-03 | proposeurs | dépense | `f00b1291…` |
| 17 | argon-p2-04 | composition | dépense | `aef7787e…` |
| 18 | argon-p2-05 | coût | processeur | `f70992bc…` |
| 19 | fable-p2-01 | juge | processeur | `8da2d515…` |
| 20 | fable-p2-02 | proposeurs | dépense | `04a46eeb…` |
| 21 | fable-p2-03 | coût | dépense | `8ec17e7c…` |
| 22 | fable-p2-04 | composition | dépense | `48215bb7…` |

**Écartés, non lus comme des fiches :**
- les **témoins plantés** et les **idées au hasard** du lecteur (`temoins-plantes-v1.md`, `temoins-lecteur-v1.json`,
  `temoins-hasard-v1.json` et leurs versions v2 dans `relecture-exploratoire-v2/`) : ils ne sont pas dans [FV] ;
- les **4 témoins servis au juge de l'organisme** (`copies/sortie--noyau--temoins-servis.json`, identifiants
  `temoin-p0-01` à `temoin-p0-04`) : pas dans [FV] ;
- les **8 fiches en quarantaine** (`copies/sortie--fiches-en-quarantaine.json`, `81d18904…` ; arrêtées par un filtre de
  forme, pas lues par le lecteur) : je n'ai lu que leurs titres. Ce sont des secondes passes dont les titres reprennent
  des idées déjà présentes dans [FV] (demi-générations, tableau croisé, bon marché d'abord, proposeurs en série,
  allocation des tirages, nul par morceaux). Je les cite seulement comme signe de répétition, jamais comme source.

**Lu pour savoir ce que le programme cherche et ce qui est déjà connu** : `CLAUDE.md` (décisions N-044, N-045, N-058,
N-064 à N-067) ; `docs/decisions/decision-N-044-v1.md`, `decision-N-045-v2.md`, `decision-N-058-v1.md`,
`decision-N-064-v1.md`, `decision-N-065-v1.md`, `decision-N-066-v1.md`, `decision-N-067-v1.md` ; la question
(`question-organisme-conception-propre-v1.md`, `77c524f3…`) ; le rapport du préparateur ; le catalogue
(`catalogue-conceptions-publiees-v1.md`, `ddfb2522…`, ci-dessous **[CAT]**, entrées C1 à C12) ; les faits servis aux
proposeurs (`docs/notes/collisionneur-bassins-etroits-v1/faits-v1.md`, `d19b5400…`, **[FAITS]**) ; le recoupement du tour
précédent sur les bassins étroits (`docs/notes/organisme-bassins-etroits-v1/recoupement-methodes-v1.md`, `eecd98fa…`,
**[REC]**) et sa synthèse (`docs/notes/collisionneur-bassins-etroits-v1/synthese-v1.md`, `5fd7e26f…`, **[SYN]**) ;
`registres/etat.md` (ligne du 8 novembre sur le nul v9).

**Réserve de lecture.** Une recherche par `grep` sur « par morceaux » a affiché, sans que je l'ouvre, le titre et une ligne
d'un fichier sous `docs/verdicts/`. Je n'en tire rien ici ; ce que je dis du nul v9 vient de `registres/etat.md` et d'un
brouillon de préenregistrement (section 1.1).

**Mise en garde sur les répétitions.** Chaque proposeur a rendu deux passes (`p1`, `p2`). Les paires `argon-p1-0k` /
`argon-p2-0k`, `fable-p1-01` / `fable-p2-01`, `fable-p1-03` / `fable-p2-02`, `fable-p1-04` / `fable-p2-04` portent la
même idée réécrite. Une répétition **chez un même proposeur** n'est pas une convergence ; je ne compte comme convergence
que des idées portées par **des proposeurs différents**.

## 1. Le juge

### 1.1 Fermer le trou « par morceaux » du nul, mais à moindre prix

- **L'idée.** Le juge cède devant une carte qui recolle deux lois connues de part et d'autre d'un seuil (« copie par
  morceaux »). On ajoute ces recollages au nul, pour qu'une telle copie ne soit plus promue. Trois variantes : (a) toutes
  les paires de lois, sur une grille publique de seuils (déciles) ; (b) seulement les branches `si_sinon` et
  `par_sous_population` à deux branches, contre un mélange à poids fixés ; (c) **seulement les conditions déjà présentes
  dans l'archive** (intersections d'au plus deux), avec des poids appris en ligne, épisode après épisode, de sorte que la
  valeur e reste une martingale.
- **Fiches.** (a) opus-p1-05 ([FV] n° 9) ; (b) fable-p1-05 ([FV] n° 13) ; (c) argon-p1-01 ([FV] n° 0, poids ajustés sur
  la première moitié des tirages, valeur e sur la seconde) et argon-p2-01 ([FV] n° 14, poids mis à jour en ligne par
  descente exponentielle). Titre repris en quarantaine (opus-p2-06, fable-p2-05).
- **Convergence.** Forte : trois proposeurs différents. opus-p1-05 et fable-p1-05 disent eux-mêmes que c'est un
  **préalable** à toute modification qui pousse vers la variété, et prédisent un effet nul sur la couverture (signe 0).
- **À quoi elle sert.** Au nœud ouvert du **nul v9** : `registres/etat.md` (8 novembre, 10:14 UTC) note un verdict
  « puissance perdue » au premier étage et un nœud de Lazar « accepter le prix ou chercher un nul moins coûteux ». La
  variante (c) est une **piste de nul moins coûteux** : elle n'ajoute que les coupures que l'archive a déjà isolées, donc
  une classe plus petite que la grille complète, donc, si l'idée tient, moins de puissance perdue. Elle sert aussi de garde
  préalable à toutes les fiches de la section 2 (qui poussent vers `si_sinon`).
- **Coût pour essayer.** Processeur seul : rejeu sur un banc de cartes écrites par programme (copies par morceaux, vraies
  composantes, lois nulles), mondes à graine scellée. Une preuve écrite de validité est à sceller avant (écart à la
  conception du juge : nœud).
- **Déjà connu, déjà fait.** Le nul v9 « qui ferme le trou par morceaux » existe
  (`docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-brouillon3.md`, l. 272) ; [REC]
  borne 9 (un nul à poids constants ne couvre pas le recollage) et borne 7 (un nul assez large pour contenir les copies
  peut contenir aussi les découvertes : c'est exactement le prix payé par le v9) ; [REC] J6 (valeur e par supremum sur un
  nul composite, maintenue sous condition) et J7 (filtre avant le juge, non critiqué). Les variantes (a) et (b) sont donc
  **déjà faites** pour l'essentiel. La restriction aux conditions de l'archive avec poids préquentiels (c) n'apparaît pas
  telle quelle dans [REC] ni dans [SYN] : c'est la partie la plus neuve. Le principe de la valeur e contre un nul composite
  estimé en ligne est connu en statistique (inférence universelle, citée par les fiches comme « SUPPOSE ») ; aucune entrée
  de [CAT] ne le couvre. Point à vérifier en premier : argon-p1-01 ajuste les poids par maximum de vraisemblance sur une
  moitié des tirages — la validité tient si le nul ajusté est fixé avant la seconde moitié ; argon-p2-01 (mise à jour en
  ligne) est la forme la plus propre.

### 1.2 Répartir les tirages frais du juge au fil de l'eau (arrêt anticipé)

- **L'idée.** À nombre total de tirages égal, on donne les tirages aux groupes de cartes par blocs. Un groupe dont la valeur
  e tombe très bas est arrêté ; un groupe qui franchit le seuil est arrêté aussi ; les tirages libérés vont aux groupes
  encore incertains. Une composante faible reçoit ainsi assez de tirages pour passer. La garantie tient par le théorème de
  Ville (une surmartingale arrêtée garde une espérance au plus 1).
- **Fiches.** opus-p1-01 ([FV] n° 5 ; règle écrite en neuf points, plafond de 4 fois la part du témoin, bras placebo où
  les tirages libérés vont au hasard) ; argon-p1-05 ([FV] n° 4, point 1 : amorçage sur 10 % des tirages, confirmation sur
  90 %). Titre repris en quarantaine (opus-p2-05).
- **Convergence.** Deux proposeurs.
- **À quoi elle sert.** À la voie bon marché « éliminations successives » que Lazar a approuvée (N-045 v2, mots de
  09:35) ; au juge de toutes les courses à monde planté ; plus tard aux domaines où un tirage est cher (opus-p1-01 le dit
  lui-même : dans le monde planté un tirage coûte des millisecondes, donc le gain réel n'est pas en dollars).
- **Coût pour essayer.** Processeur seul : rejeu des mêmes cartes, juge à part fixe contre juge à allocation, à tirages
  totaux égaux. Preuve écrite avant (nœud : écart à la conception du juge).
- **Déjà connu, déjà fait.** [REC] J1 « processus de valeurs e à arrêt optionnel », **survivante** ; [SYN] § 9 la met en
  premier dans l'ordre recommandé (« seule méthode de juge qui sort de la critique avec sa revendication entière »).
  Voisins publiés dans [CAT] : C7 (PACE : e-processus par paris, arrêt anticipé) et C10 (E-valuator : règle séquentielle à
  fausse alarme contrôlée) ; le principe n'est donc pas neuf. Ce que la fiche ajoute de réutilisable : la **règle écrite
  complète** et deux contrôles (placebo de réallocation au hasard ; témoin à 1,2 fois les tirages). Une tension à lire :
  [SYN] § 8 demande un « ordre de continuation fixé d'avance, jamais selon les valeurs e », alors qu'opus-p1-01 alloue
  selon les valeurs e courantes (arrêts bas et haut). Ville couvre une règle d'arrêt écrite d'avance, même dépendante des
  données ; la question est la validité sous **nul composite** à chaque pas, que [SYN] § 8 demande de démontrer.

### 1.3 Tirer les épisodes frais du juge par strates publiques

- **L'idée.** Au lieu de tirer les traits au hasard uniforme, le juge tire un nombre fixé d'épisodes dans chaque strate
  publique (celles du regroupement des doublons). Une région rare reçoit alors autant d'épisodes qu'une région large. La
  valeur e reste un rapport de vraisemblance des issues sachant les traits ; la fiche soutient que sa garantie ne dépend pas
  de la loi des traits, pourvu que le tirage soit scellé et indépendant des cartes.
- **Fiches.** fable-p1-01 ([FV] n° 10) et fable-p2-01 ([FV] n° 19, même idée, avec trois contrôles « cosmétique »
  détaillés). Un seul proposeur.
- **À quoi elle sert.** À la « borne de dilution » de [FAITS] § 3 (une différence confinée à une région de masse r est
  écrasée en moyenne globale).
- **Coût pour essayer.** Processeur seul : rejeu des cartes, deux bras, mêmes tirages totaux.
- **Déjà connu, déjà fait.** **Déjà discutée et retirée** au tour précédent : [REC] J2, « retirée » (la grandeur jugée
  change : une carte meilleure dans la région sur-représentée et pire ailleurs serait promue ; fuite si la partition est
  celle qui a construit le monde ; gain nul si la région utile est répartie entre strates) ; [REC] bornes 5 et 6 ; [SYN]
  § 9 : « ne pas reprendre J2 ». La fiche ne répond pas à ces objections. Je la garde dans le relevé pour une seule raison :
  le désaccord (la fiche dit que la garantie tient ; [REC] dit que ce qui est jugé change) **se tranche sur processeur, en
  quelques heures**, sur le même banc que 1.1. Ce n'est pas une idée neuve.

## 2. Les proposeurs : ce qu'on leur sert et comment on les appelle

### 2.1 Une carte par session, au lieu de six cartes dans un même appel

- **L'idée.** Aujourd'hui chaque proposeur rend six cartes dans un seul appel ; la première carte attire les cinq autres
  (la course v67 a rendu onze variantes d'un même constat, [FAITS] § 2). On fait six appels en sessions neuves, une carte
  chacun, au même coût. Variante : un premier appel rend six « constats » d'une ligne (là où l'archive laisse un écart),
  puis chaque carte est écrite dans une session qui ne voit qu'un seul constat.
- **Fiches.** argon-p1-02 ([FV] n° 1) et argon-p2-02 ([FV] n° 15, formule exacte de plafond de jetons pour l'égalité de
  coût) ; fable-p1-03 ([FV] n° 11) et fable-p2-02 ([FV] n° 20, constats isolés, **témoin « meilleur de N » à dollars
  égaux**).
- **Convergence.** Deux proposeurs, deux formes. Une troisième forme voisine : opus-p1-02 (section 4.1) coupe aussi
  l'appel en deux.
- **À quoi elle sert.** À QO4 (le séquentiel bat-il le meilleur de N tirages indépendants ?) : fable-p2-02 pose
  exactement ce témoin. À la conception des proposeurs de toutes les courses de l'atelier.
- **Coût pour essayer.** Dépense, petite : une génération, 10 à 15 mondes, un ou quatre proposeurs, « quelques dizaines de
  dollars » selon les fiches ; devis et GO.
- **Déjà connu, déjà fait.** [REC] § 1 : « la remise à zéro du contexte est déjà en place » (chaque appel est déjà en
  session neuve) — mais l'ancrage **à l'intérieur** d'un appel de six cartes ne l'est pas : c'est la partie nouvelle.
  Les fiches se disent elles-mêmes « transposition » de [CAT] C5 (Fork-and-Flush) ; C6 (oubli périodique) est voisin.
  La variante « constats puis isolement » ressemble à [REC] C2 (préfixes prolongés par plusieurs continuations, non
  critiquée). Contrôles réutilisables : servir les six constats à chaque session (effet du seul fractionnement) ; six
  lignes neutres de même longueur (effet de perturbation du contexte).

### 2.2 Une table descriptive dans la vue des proposeurs

- **L'idée.** On ajoute à la vue une table calculée par programme, sans score ni consigne. Deux contenus : (a) **syntaxique**
  — pour chaque trait et chaque paire de traits, combien de lois de l'archive les utilisent (comme condition, comme
  branche) ; (b) **sur des données publiques** — sur 2 000 épisodes publics tirés une fois à graine scellée, disjoints des
  tirages du juge, les fréquences des issues dans les quatre cases de chaque croisement de deux traits coupés à la médiane.
  Une composante conditionnelle, nulle en moyenne, laisse des pentes de signes opposés dans les deux branches : le
  croisement la rend visible.
- **Fiches.** (a) argon-p1-03 ([FV] n° 2) et argon-p2-03 ([FV] n° 16) ; (b) opus-p1-03 ([FV] n° 7 ; placebo par **monde
  jumeau** de mêmes marges sans composante conditionnelle, dont les cartes sont jugées sur le vrai monde). Titre (b) repris
  en quarantaine (opus-p2-02).
- **Convergence.** Deux proposeurs, deux contenus différents.
- **À quoi elle sert.** À l'« inconnue centrale » de [SYN] (point 7 du verdict) : la loi des propositions d'un modèle
  bouge-t-elle quand on lui montre une liste ? Et à QO2 (ce qu'une génération lègue) pour la forme (a).
- **Coût pour essayer.** La table elle-même : processeur. Son effet : dépense. Forme (a) : la fiche propose de reprendre
  l'état exact de l'archive à la génération 2 d'une course jouée et de faire une seule passe d'appels avec la vue augmentée
  (« quelques dollars »). Forme (b) : trois bras, deux générations, « des dizaines de dollars ».
- **Déjà connu, déjà fait.** (a) est très proche de [REC] V2 (« liste des paires de traits que l'archive ne croise pas »,
  survivante) ; [SYN] § 9 la place au rang 2 de l'ordre recommandé. La fiche n'est donc pas neuve sur le fond ; sa forme
  (comptes par trait et par paire, tirés de l'arbre grammatical) est une version prête à coder. (b) correspond à [REC] V10
  et V11, dont le prérequis était justement « des données publiques d'exploration avec issues, distinctes des tirages du
  juge, dont l'existence n'est pas établie » : opus-p1-03 dit **comment créer ce canal**. C'est un dessin neuf (une donnée
  nouvelle entre dans la vue) : nœud à poser, et à lire contre la contrainte « la vue ne contient ni verdict, ni oracle, ni
  loi plantée » (des effectifs d'épisodes ne sont aucun des trois, mais [REC] V11 avertit que la focalisation pousse vers
  des lois par morceaux, donc vers 1.1). Le placebo par monde jumeau est réutilisable ailleurs (section 5).

### 2.3 Une « lentille » de strate par proposeur, tirée au sort

- **L'idée.** Chaque proposeur reçoit la vue entière plus une ligne : « examiner en priorité les épisodes dont les traits
  sont dans [strate] ; toute carte reste admise ». Les strates sont attribuées par tirage scellé, et tournent d'une
  génération à l'autre. Aucun tri, aucune note de conformité. Variante : servir la lentille à des instruments locaux, pour
  voir s'ils égalent la frontière sans lentille.
- **Fiches.** fable-p1-04 ([FV] n° 12, avec le bras « instruments locaux ») et fable-p2-04 ([FV] n° 22). Un seul
  proposeur.
- **À quoi elle sert.** QO1 (la frontière est-elle nécessaire ?) pour la variante locale ; QO5.
- **Coût pour essayer.** Dépense : 12 mondes, deux ou trois bras, « quelques dizaines de dollars » ; bras local presque
  gratuit.
- **Déjà connu, déjà fait.** [REC] V3 (plan combinatoire qui répartit des focalisations entre les appels, survivante,
  rang 3 de [SYN] § 9, « seulement si V2 montre un levier »). Parent publié cité par la fiche : MAP-Elites (qualité et
  diversité à niches, « SUPPOSE »). Ce qui est réutilisable : le contrôle « même lentille pour tous les proposeurs »
  (sépare l'orientation de la partition) et « une strate vide de composante ne doit produire aucune carte retenue ».

## 3. La composition

### 3.1 Deux passes : choisir les traits pas cher, puis écrire la loi

- **L'idée.** Une passe légère (modèle peu cher ou instrument local) propose vingt ensembles de 1 à 3 traits, sans loi.
  Un programme retire ceux déjà dans l'archive et en garde six, les plus éloignés entre eux (distance de Jaccard, règle
  gloutonne fixée d'avance, sans modèle ni juge). Puis la frontière écrit une carte par ensemble.
- **Fiches.** argon-p1-04 ([FV] n° 3) et argon-p2-04 ([FV] n° 17). Un seul proposeur.
- **À quoi elle sert.** QO1 (quel rôle a besoin de la frontière) et QO4, et N-045 point 1 (la composition est une
  variable apprise ; ici un rôle est déplacé vers le bon marché).
- **Coût pour essayer.** Dépense : une génération, 10 mondes, un proposeur, « quelques dizaines de dollars ».
- **Déjà connu, déjà fait.** Proche de [REC] V3 (focalisations par appel) et de C2 (préfixe puis continuations). La
  partie propre est le **filtre déterministe sans juge** entre les deux passes. Les deux passes du lecteur ont jugé
  argon-p2-04 hors d'une porte (R3) ; je le note sans en tirer de rang. Risque nommé par la fiche : forcer des traits de
  pur bruit.

### 3.2 Proposeurs en série : chacun voit les cartes brutes des précédents

- **L'idée.** On appelle les proposeurs l'un après l'autre, dans un ordre tiré au sort ; chacun voit le texte brut des
  cartes déjà rendues dans la génération, sans verdict, avec la phrase « une carte presque identique sera regroupée avec
  elle ». Il devrait porter ses cartes ailleurs ; le signe peut s'inverser (grégarisme), et c'est ce que l'essai tranche.
- **Fiche.** opus-p1-04 ([FV] n° 8). Titre repris en quarantaine (opus-p2-04). **Isolée** (un seul proposeur).
- **À quoi elle sert.** N-045 point 1 (« l'ordre et la forme des échanges ») ; QO1.
- **Coût pour essayer.** Dépense : 20 mondes, trois bras, deux générations, « quelques centaines de dollars » (version
  bon marché d'abord avec des modèles peu chers).
- **Déjà connu, déjà fait.** Les échanges entre agents sont occupés ([CAT] C1, Co-Scientist : tournoi et débats) ; la fiche
  le dit et retire tout classement. Contrôle réutilisable : cartes **d'un autre monde**, de même longueur, à la place des
  cartes des pairs (sépare l'information de l'allongement du contexte).

## 4. Le coût et le calendrier

### 4.1 Mettre l'archive à jour au milieu de chaque génération

- **L'idée.** Une génération de six cartes devient deux demi-générations de trois, avec toute la chaîne (gardien, juge,
  test de mort, archive) entre les deux, au même plafond de dollars. Un constat trouvé à la première moitié entre dans le
  nul ; ses variantes à la seconde moitié deviennent des copies refusées ; une condition archivée plus tôt rend sa
  composante conditionnelle trouvable plus tôt.
- **Fiche.** opus-p1-02 ([FV] n° 6 ; placebo : deux appels de trois cartes **sans** mise à jour entre eux). Titres repris en
  quarantaine chez deux proposeurs (fable-p1-02, opus-p2-01).
- **Convergence.** Deux proposeurs si l'on compte les titres en quarantaine ; un seul dans [FV].
- **À quoi elle sert.** QO2 (ce qu'une génération lègue) et la profondeur en chaîne : [REC] borne 4 dit que l'horizon en
  générations borne la profondeur atteignable ; deux demi-générations doublent cet horizon au même prix.
- **Coût pour essayer.** Dépense : « quelques dizaines de dollars » avec un modèle peu cher ; confirmation à quelques
  centaines.
- **Déjà connu, déjà fait.** Non trouvée telle quelle dans [REC] ni [SYN] (où « la profondeur au sens des chaînes n'a
  presque pas été traitée », [SYN] point 10). Parent cité par la fiche : algorithmes génétiques « à état permanent » contre
  « générationnels » (« SUPPOSE »). Elle dépend d'une hypothèse non mesurée de [FAITS] § 4 (de vrais proposeurs trouvent la
  composante après sa condition). Le nombre de demi-générations est fixé d'avance, jamais piloté par les promotions :
  c'est ce qui la garde hors de N-058.

### 4.2 Le bon marché d'abord : instruments locaux à la première génération

- **L'idée.** La génération 1 trouve surtout la « surface » (ce que tout le monde trouve). On la confie aux instruments
  locaux ; la frontière n'entre qu'à la génération 2, quand l'archive a ouvert des conditions ; les dollars épargnés payent
  une génération de plus.
- **Fiches.** fable-p2-03 ([FV] n° 21). Même logique, autre forme : argon-p2-05 ([FV] n° 18, point 1, appeler d'abord la
  moitié la moins chère des proposeurs) et argon-p1-04 (3.1). Titre repris en quarantaine (opus-p2-03).
- **Convergence.** Trois proposeurs sur le principe « le moins cher d'abord ».
- **À quoi elle sert.** Directement à QO1 et QO4, et à N-045 points 3 et 4 (« voies bon marché avant la voie chère »).
- **Coût pour essayer.** Dépense : 10 mondes, deux bras, « une centaine de dollars » de frontière.
- **Déjà connu, déjà fait.** Cascade du bon marché au cher, connue en sélection de modèles (la fiche le dit). Contrôle
  réutilisable : le bras « tout local sur G+1 générations » (si la frontière n'apporte rien, c'est une réponse à QO1).
  Piège nommé par la fiche : comparer des bras de nombres de générations différents mêle composition et durée.

### 4.3 Arrêter une course stérile et reporter le budget

- **L'idée.** Si une génération ne fait entrer aucune loi dans l'archive (comme la génération 2 de v67), on arrête la
  course et on reporte le budget là où l'archive vient de grandir. Variante : n'appeler la moitié chère des proposeurs que
  si le **regroupement des doublons** (calcul public, sans juge) montre que plus de 80 % des cartes de la moitié bon marché
  sont déjà dans le nul.
- **Fiches.** argon-p1-05 ([FV] n° 4, point 2) et argon-p2-05 ([FV] n° 18). Un seul proposeur.
- **À quoi elle sert.** QO3 (régimes de budget ; re-conception déclenchée par l'organisme sur son propre critère, N-044
  point 2, non tranché).
- **Coût pour essayer.** Processeur pour une partie : simuler sur des traces de courses passées la part du budget
  réellement épargnée (sans rien dire de la couverture). La mesure de couverture demande une course : dépense.
- **Déjà connu, déjà fait.** **À lire contre N-058 et N-053 avant tout usage** : ouvrir des générations ou reporter du
  budget **parce que l'archive a grandi**, c'est piloter le dessin par les promotions du juge. N-058 interdit de juger la
  composition des proposeurs sur le verdict du juge, et [FAITS] § 4 dit que la diversité ne doit pas piloter le nombre de
  générations. La variante qui décide sur le **regroupement** (calcul public, avant le juge) échappe peut-être à cette
  objection : c'est la partie la plus réutilisable, mais c'est un nœud.

## 5. Des contrôles négatifs réutilisables (idée transversale)

Plusieurs fiches nomment des contrôles plus précis que ceux du dépôt que j'ai lus. Ils servent tels quels dans tout
préenregistrement d'une course à monde planté, quelle que soit l'idée testée :
- **placebo par monde jumeau** : même marges, sans la composante visée ; les cartes sont jugées sur le vrai monde
  (opus-p1-03, [FV] n° 7) ;
- **cartes ou lignes d'un autre monde, de même longueur** à la place de l'information servie (opus-p1-04, [FV] n° 8 ;
  fable-p2-02, [FV] n° 20 ; fable-p1-04, [FV] n° 12) : sépare l'information de la simple perturbation du contexte ;
- **même découpage sans le mécanisme** : deux appels sans mise à jour de l'archive (opus-p1-02, [FV] n° 6) ; tous les
  constats servis à chaque session (fable-p1-03, [FV] n° 11) ;
- **réallocation au hasard** et **témoin à 1,2 fois les tirages** pour toute idée de juge (opus-p1-01, [FV] n° 5 ;
  fable-p2-01, [FV] n° 19) : sépare un effet de structure d'un effet d'effectif ;
- **mondes sans la structure visée** (sans composante rare, sans conditionnelle, sans copie par morceaux), où le bras ne doit
  rien gagner ni promouvoir de plus (presque toutes les fiches).
- **Coût** : processeur seul (rédaction d'une liste de contrôles pour le banc de [SYN] § 6 et les préenregistrements).
- **Déjà connu** : [REC] § 10 et [SYN] § 6 listent déjà des placebos (vue placebo de même format, mondes hors structure) ;
  le monde jumeau et les cartes d'un autre monde ne figurent pas tels quels dans ce que j'ai lu.

## 6. Idées répétées et idées isolées

**Répétées par des proposeurs différents (convergence)** :
- nul par morceaux (1.1) — trois proposeurs ;
- le moins cher d'abord (4.2, 3.1, 4.3) — trois proposeurs, trois formes ;
- décorréler les cartes d'un même appel (2.1, et 4.1 en partie) — deux à trois proposeurs ;
- allocation séquentielle des tirages (1.2) — deux proposeurs ;
- table descriptive dans la vue (2.2) — deux proposeurs, deux contenus.

Trois de ces cinq convergences recoupent des méthodes déjà retenues au tour précédent ([REC] J1, V2, J6) : la convergence
dit surtout que l'idée est **naturelle**, pas qu'elle est neuve.

**Isolées mais originales (à mon jugement)** :
- le nul par morceaux **restreint aux conditions de l'archive, à poids appris en ligne** (argon-p2-01) — piste de nul moins
  coûteux que le v9 ;
- le **canal d'épisodes publics** disjoint du juge et le **placebo par monde jumeau** (opus-p1-03) ;
- les **proposeurs en série** sans verdict (opus-p1-04) ;
- les **demi-générations** contre la borne d'horizon des chaînes (opus-p1-02) ;
- la **décision d'appeler la moitié chère sur le regroupement**, sans juge (argon-p2-05, point 1).

## 7. À essayer d'abord, à bas coût

**Jugement de lecteur, pas un résultat mesuré.** Aucun de ces choix ne vient du classement ; aucun n'est une désignation.
Tous touchent le juge ou le dessin : chacun demande une preuve ou un préenregistrement scellé, et une décision de Lazar
quand il s'écarte d'une conception scellée.

1. **Nul par morceaux restreint aux conditions de l'archive** (argon-p2-01, argon-p1-01 ; 1.1), rejoué sur processeur
   contre le v9 et contre le nul de production, sur un banc de copies par morceaux et de vraies composantes : une réponse
   possible au nœud « chercher un nul moins coûteux ».
2. **Allocation séquentielle des tirages du juge** (opus-p1-01 ; 1.2), en rejeu sur cartes scellées, à tirages totaux
   égaux, avec le placebo de réallocation au hasard ; preuve écrite d'abord ([SYN] § 8).
3. **Trancher le désaccord sur les tirages stratifiés** (fable-p2-01 ; 1.3) sur le même banc, en quelques heures de
   processeur : soit l'objection de [REC] J2 se confirme et l'idée se ferme, soit elle tombe.
4. **Liste des contrôles négatifs réutilisables** (section 5), versée au banc de [SYN] § 6 et au gabarit des
   préenregistrements : rédaction seule.
5. **Table syntaxique de l'archive** (argon-p2-03 ; 2.2 (a)), codée sur processeur, puis, sur devis et GO, une seule
   passe d'appels sur l'état d'archive d'une génération déjà jouée (« quelques dollars » selon la fiche) : c'est le test le
   moins cher de l'inconnue centrale de [SYN].
