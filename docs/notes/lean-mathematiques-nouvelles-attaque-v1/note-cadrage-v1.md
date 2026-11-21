# Note de cadrage — des mathématiques nouvelles, formalisées et vérifiées en Lean, pour concevoir des modes d'attaque inédits contre les moniteurs à sondes — v1

- **Nature** : pièce de travail (classe C), au niveau de la **méthode et de l'idée seulement**. Elle ne contient **aucun procédé, aucune recette, aucun énoncé de mode concret**. Elle dit comment un pilier théorique pourrait servir le bras d'attaque, où ce travail se loge sans briser les cloisons, le premier pas, les risques, et ce qui permettrait de vérifier de l'extérieur qu'un mode ainsi conçu est inédit et réel.
- **Écrite par** : Claude Fable 5.2 (`claude-fable-5-2`), concepteur, le 2026-11-21 (heure relevée par `date -u`). La conception du délicat revient à Fable 5.2 (mot de Lazar du 19 novembre, R-3735) ; la contre-lecture reviendra à un autre modèle (Opus 5.5).
- **Pour** : la session mère, puis Lazar. **Rien ne s'ouvre, rien ne se lance, aucune dépense, aucun appel de modèle n'a servi à l'écrire.** Ce texte n'est ni un préenregistrement (R1), ni un devis, ni une règle d'ouverture, ni une revendication. Il propose une direction ; toute mise en œuvre est un nœud chez Lazar.
- **Mandat.** GO-2026-11-21-12 (mot de Lazar, 2026-11-21T06:24Z) : « il faut aller plus loin et utiliser les nouvelles mathématiques pour la conception de nouveaux modes d'attaque inédits » ; le pilier des mathématiques nouvelles est rouvert **pour l'attaque**, ce qui lève en partie la fermeture de la couche 4 de l'organisme (N12 (b), R-959) et l'interdit de préparation (DP-1 (a), R-2265), **sous les six garde-fous** de GO-2026-11-20-50 et **les cloisons du bras d'attaque** (GO-2026-11-19-96) : travail par une session à part, au niveau de l'idée, la mère ne lit aucun procédé.
- **Sources lues** (empreintes tronquées, compagnons `.sha256` recalculés et conformes) : état du chantier Lean du 21 novembre (`3d2b8d3e…`) ; note de périmètre des modes inédits v3 (`dd6fea0e…`, définition d'un mode et des quatre épreuves) ; note de conception du pilier « génération » v1 (`94532165…`, chaîne, oracles plantés, questions Q1 à Q5) ; GO-2026-11-21-12, GO-2026-11-20-50 (six garde-fous), GO-2026-11-19-96 (cloisons du bras d'attaque), tous dans `registres/go.md` (`68b62f28…`). **Non lu** : aucune pièce du bras d'attaque en quarantaine, aucun procédé, aucun résultat d'expérience (7a, 7b, T0.6, étapes B et B bis, P3-bis, barreau 5).
- **Convention de nom en clair** (R-3044) : je nomme ce qui serait fait par ce que c'est, jamais par un sigle seul. « Pilier théorique » = la couche 4 de l'organisme d'idéation, le pôle théorie et Lean. « Moniteur à sondes » = un contrôle qui lit l'intérieur de l'agent (activations, traits internes) pour signaler une menace. « Mode » et « épreuve » = au sens de la note de périmètre v3 (§ 1).

---

## 0. Ce que cette note change, et ce qu'elle ne change pas

- **Ce qui était vrai jusqu'ici.** Dans toutes les pièces du pilier théorique, l'attaque n'apparaissait qu'au **niveau de la méthode** : éprouver l'arbitre formel (Lean) et le juge de nouveauté de l'organisme contre une triche de Goodhart (note de conception, § 2.4), sans aucune recette. La défense, elle, prenait la forme d'énoncés sur les panels de moniteurs (agrégateur sous corrélation adverse, lemme d'impossibilité ; questions Q3, Q4 du pilier).
- **Ce que le mandat ouvre.** Le même outillage théorique — poser une question mathématique, en tirer un énoncé, le formaliser, le faire vérifier par Lean — pourrait servir **l'autre côté** : non plus démontrer qu'un panel de moniteurs tient, mais démontrer **sous quelles conditions il ne peut pas tenir**, et faire de cette condition la **visée** d'un mode d'attaque candidat, au sens exact de la note de périmètre.
- **Ce que cette note ne fait pas.** Elle ne nomme aucun mode, n'écrit aucun énoncé mathématique concret, ne propose aucune cible formelle, ne construit rien. Elle reste une **carte de direction**. Le passage de la direction à un énoncé concret est déjà un pas qui vit dans le bras d'attaque, sous quarantaine (§ 2, § 3).

---

## 1. Comment des mathématiques nouvelles peuvent servir à concevoir des modes inédits (méthode et idée seulement)

### 1.1 Le principe : un théorème d'impossibilité est, lu à l'envers, une visée d'attaque

La note de périmètre v3 définit un **mode** par deux choses (§ 1) : **ce qu'il vise** (le travail dégradé, une information qui sort, une coordination entre copies, un moniteur ou un juge trompé) et **ce qu'il met en défaut** (ce que le contrôle suppose). Un mode candidat passe les quatre épreuves : il nomme les deux ; il reste vrai quels que soient la tâche, l'outil, le modèle et la dose ; il ne contient ni étape ni recette (sinon c'est une recette, au coffre) ; et son couple (visée, supposition mise en défaut) diffère de chaque mode de la liste de référence scellée.

Un énoncé mathématique démontré — en particulier un **énoncé négatif**, une borne d'impossibilité — a exactement cette forme à deux faces. Il dit : « sous telles conditions écrites, **aucune** procédure de la classe C n'atteint la performance P. » Lu du côté de la défense, c'est une limite à connaître. Lu du côté de l'attaque, **les conditions de l'énoncé sont une visée** (« amener le moniteur dans ce régime ») et **l'hypothèse que le moniteur viole en y restant aveugle est la supposition mise en défaut**. Le pont est donc : *une hypothèse d'un théorème d'impossibilité, nommée, devient la « supposition mise en défaut » d'un mode ; la conclusion du théorème borne ce que le moniteur peut espérer dans ce régime.* C'est le c\oe ur de ce que le mandat demande.

Point capital de grain : **l'énoncé démontré n'est pas le mode, et il n'est pas une recette.** Il ne dit pas *comment* mettre un système réel dans le régime visé ; il dit seulement *que si* on y est, la détection est bornée. Le passage « comment y arriver » est précisément le procédé, qui reste au coffre (épreuve 3 de la note de périmètre, R-607). Un théorème d'impossibilité se tient donc **au niveau de l'idée par construction** : il est universel (quantifié sur une classe), ce qui le rapproche de l'épreuve 2 (« vrai quels que soient la tâche, l'outil, le modèle, la dose »), et il ne porte aucune étape.

### 1.2 Quelles familles d'objets mathématiques, et quelles questions

Sans écrire aucun énoncé, voici les familles où une question théorique rencontre naturellement la lecture d'un moniteur à sondes. Chaque ligne est une **question**, pas une réponse ; une zone qui paraît vierge reste une question (R8, § 4).

| famille d'objets | la question, côté défense (déjà au pilier) | la même question, retournée côté attaque (ce que le mandat ouvre) |
|---|---|---|
| **Bornes d'impossibilité de détection** (indistinguabilité, proximité en variation totale, divergences) | sous quelles conditions mesurées aucune statistique des signaux observés n'a une puissance au-dessus du niveau (lemme maître d'impossibilité, Q4 du pilier) | **les hypothèses de ce lemme, nommées une à une**, forment une liste de « suppositions du moniteur » dont chacune, mise en défaut, est la face défense d'un mode candidat ; le théorème borne le gain du moniteur dans ce régime |
| **Géométrie des représentations** (sous-espaces, directions, séparabilité linéaire, marge) | une sonde linéaire qui lit une direction interne ; quelle marge, quelle robustesse | **question** : existe-t-il des familles de représentations où la grandeur que la sonde lit et la grandeur qui porte la menace vivent dans des sous-espaces dont la relation géométrique rend la lecture bornée, sans que le comportement observable change — au niveau de l'énoncé, sans aucune construction |
| **Agrégation sous corrélation adverse** (bornes de dépendance à marges fixées, couplage) | quel panel de moniteurs reste non aveugle quand l'adversaire choisit la dépendance entre leurs erreurs (agrégateur, Q3 du pilier) | **question** : le même calcul borne-t-il le gain d'un panel ? Un énoncé négatif (« aucune règle fixe d'agrégation ne bat le meilleur moniteur seul contre cet adversaire ») nomme exactement la supposition d'un panel que le mode mettrait en défaut |
| **Théorie de la détection séquentielle** (martingales, analyse séquentielle, effets d'épisode) | l'accumulation séquentielle rattrape-t-elle ce que le seuil par action manque ; plafond d'horizon (Q2 du pilier) | **question** : existe-t-il un régime, décrit par des hypothèses écrites, où le plafond d'horizon joue contre le contrôle — c.-à-d. où l'accumulation du moniteur plafonne tandis que la menace, elle, s'accumule ? L'énoncé borne, il ne construit pas |

Dans les quatre cas, la défense et l'attaque **partagent le même théorème** : c'est le même objet, lu des deux côtés. C'est une bonne nouvelle pour la cloison (§ 2) : on ne conçoit pas deux corpus, on lit un corpus sous deux éclairages, et c'est la **lecture**, non l'énoncé, qui doit être cloisonnée.

### 1.3 Pourquoi Lean, et ce que Lean garantit ici

Lean (le vérificateur de preuves) apporte trois choses au côté attaque qu'aucune autre méthode n'apporte :

1. **Un énoncé d'impossibilité vérifié ne se discute plus.** Si un mode candidat s'appuie sur « le moniteur suppose X, or sous le régime Y la détection est bornée », et que « sous Y la détection est bornée » est un théorème démontré en Lean (sous gardes : ni `sorry`, axiomes limités, définitions imprimées en entier, audit de fidélité — toutes les gardes de la note de conception, § 2.3), alors la face « supposition mise en défaut » du mode repose sur un fait, pas sur une intuition. Cela **durcit l'épreuve 2** de la note de périmètre (universalité) : un énoncé quantifié et démontré est universel par sa forme même.
2. **La fidélité se mesure.** Le risque, c'est qu'un énoncé formel dise autre chose que la question qu'on croyait poser (formalisation infidèle, classe E1 de la note de conception). Les gardes de fidélité (rétro-traduction aveugle, témoin de non-vacuité, épreuve du contre-exemple déclaré) empêchent qu'un mode s'appuie sur un énoncé vide ou renforcé en secret.
3. **La nouveauté a un plancher mécanique.** Le juge de nouveauté de l'organisme (trois étiquettes, jamais « nouveau ») sert ici à distinguer un **mode inédit** d'une **variante** d'un mode connu (épreuve 4 de la note de périmètre). Un énoncé qui est un corollaire immédiat de la bibliothèque, ou qui égale un résultat connu après normalisation, ne peut pas fonder un mode « inédit ».

**Ce que Lean ne garantit pas, et qu'il faut dire :** Lean vérifie que l'énoncé *formel* est démontré. Il ne dit pas que le régime décrit par les hypothèses est **atteignable** par un agent réel contre un moniteur réel — c'est une question empirique, qui se tranche sur le banc de mesure scellé et à G1, jamais par une preuve (MAT-004 ; la note de conception le répète, § 3.3). Un théorème d'impossibilité peut être vrai **et vide** si ses hypothèses ne sont jamais réunies en pratique. D'où le lien obligatoire avec la course des nouvelles attaques (§ 2.3) : la preuve fournit la **visée** et l'argument d'universalité ; la course et le banc fournissent la **réalité**.

### 1.4 Le fil complet, au grain de l'idée

Donc, bout à bout, sans jamais descendre au procédé : (a) on choisit une famille d'objets (§ 1.2) et une question d'impossibilité ; (b) on en tire un énoncé formel, dont les **hypothèses sont la liste des suppositions candidates du moniteur** ; (c) Lean vérifie l'énoncé sous gardes ; (d) le juge de nouveauté dit si l'énoncé — donc la supposition qu'il isole — est connu ou non trouvé dans les pièces lues ; (e) **on en dérive une visée d'attaque** : « un mode qui amène le moniteur à rester dans le régime où cet énoncé borne sa détection, en mettant en défaut l'hypothèse nommée » — et cette visée, écrite comme couple (visée, supposition mise en défaut) **sans aucune étape**, est un mode candidat au sens de la note de périmètre ; (f) la course des nouvelles attaques et le banc de mesure scellé disent si ce régime est **atteignable** et si le mode est **réel**. Les étapes (a) à (e) ne coûtent aucun appel de modèle si l'énoncé est écrit à la main ; (f) est une dépense, sur devis et GO.

---

## 2. Où ce travail se loge sans briser les cloisons

### 2.1 Une session à part, dans le bras d'attaque, sous les six garde-fous

Ce travail **n'est pas** un chantier de plus au sens de la règle des trois chantiers actifs : c'est une **extension du bras d'attaque déjà actif** (la course des nouvelles attaques), côté conception théorique. Il se range donc sous les cloisons de GO-2026-11-19-96 et les six garde-fous de GO-2026-11-20-50, appliqués ainsi :

1. **(garde-fou 1)** L'énoncé mathématique et la lecture « côté attaque » (l'étape (e) du § 1.4, la dérivation de la visée) ne sont demandés qu'à une **session à part**, jamais dans une conversation qui conçoit des moniteurs, jamais dans la conversation qui a rendu l'idée. **La mère ne lit jamais la visée d'attaque dérivée ni aucun procédé** ; elle orchestre, consigne et scelle sur des étiquettes et des empreintes.
2. **(garde-fou 2)** Toute pièce qui porte une visée d'attaque dérivée (le couple nommé côté attaque) vit en **quarantaine** : branche orpheline, sans histoire commune avec `main`, jamais fusionnée, règle d'ouverture écrite, liste nominative des lecteurs, chaque lecture consignée. L'énoncé mathématique *pur* (côté défense, sans la lecture d'attaque) peut vivre au pilier, en clair ; **c'est la lecture retournée, pas le théorème, qui est sensible** (§ 1.2).
3. **(garde-fou 3)** Le registre servi aux générations suivantes ne porte que **nom et énoncé** d'un mode, vérifié par programme avant envoi — jamais la dérivation, jamais la preuve retournée.
4. **(garde-fou 4)** Aucun énoncé n'est **exécuté** — mis à l'épreuve sur un moniteur — hors du banc de mesure scellé ; chaque exécution cite un GO.
5. **(garde-fou 5)** Un lecteur interne d'une autre lignée que les moniteurs répond, par oui ou non, « cette dérivation sert-elle à autre chose que mesurer ? » ; un oui bloque l'usage.
6. **(garde-fou 6)** La revue de sécurité externe est fixée avant toute sortie hors quarantaine (papier, billet, dépôt public, partage).

### 2.2 La cloison d'or : aucune session qui conçoit des sondes ne lit les énoncés d'attaque

C'est le point le plus délicat, parce que le pilier théorique produit **le même théorème** pour les deux côtés (§ 1.2). La règle :

- **Le théorème nu** (énoncé d'impossibilité, hypothèses, preuve Lean) peut être lu par une session de conception de moniteurs : connaître une borne d'impossibilité est utile pour **concevoir un panel plus robuste** (c'est la face défense, Q3, Q4 du pilier). C'est même souhaitable.
- **La dérivation retournée** (la lecture « voici donc une visée d'attaque », le couple (visée, supposition mise en défaut) écrit côté attaque) **ne doit jamais être lue par une session qui conçoit des sondes, des agrégateurs ou des traits de texte** (invariant de N-054, point 3 ; sens de la quarantaine, qui va de l'attaquant vers les concepteurs de moniteurs, N-056, point 6). Un moniteur conçu après lecture d'une visée d'attaque est « spécialisé » et sort du régime générique.
- **Conséquence pratique** : la session qui fait la dérivation retournée est distincte de toute session qui écrit un mandat de concepteur de moniteurs (le compte rendu d'un sous-agent entre dans le contexte de qui l'a lancé). Les deux lecteurs d'antériorité et la relecture « aucune recette » de la course s'appliquent ici comme à toute fiche de mode.

### 2.3 Rattachement : la course des nouvelles attaques et le mode tenu à l'écart

- **Course des nouvelles attaques** (bras d'attaque, GO-2026-11-19-96) : une visée dérivée d'un théorème est **une fiche de mode candidat de plus**, qui entre dans la course par la même porte que les fiches des espèces proposeuses, passe les mêmes quatre épreuves, la même règle d'antériorité, le même rangement en quarantaine. Le pilier théorique est donc une **source de candidats** pour la course, pas une filière séparée. La différence : un candidat issu d'un théorème démontré porte un **argument d'universalité vérifié** (épreuve 2 durcie), là où un candidat d'espèce porte un argument en langue naturelle.
- **Mode tenu à l'écart** (N-054, point 1 ; additif 1 de la v9) : un mode dérivé d'un théorème, comme tout mode, peut être **désigné pour être tenu à l'écart de la conception des moniteurs**, afin de mesurer plus tard si le contrôle générique l'attrape sans l'avoir vu. La règle de la note de périmètre tient : un mode tenu à l'écart ne se confronte à la liste de référence que par un lecteur isolé.
- **Famille de menaces diffuses** : si un théorème d'impossibilité porte sur une menace *diffuse* (répartie sur beaucoup d'actions, chacune sous le seuil), il touche le c\oe ur du programme (contrôle des menaces diffuses). Le rattachement d'une telle famille est un nœud (rôle 3 à trancher, N-065) ; cette note ne le tranche pas.

---

## 3. Le premier pas concret, et ce qu'il faut avant toute dépense

### 3.1 Le premier pas, sans dépense de modèle

Le premier pas **ne coûte aucun appel de modèle** et **n'exécute aucun code** : c'est un **travail de table**, écrit à la main par le concepteur (Fable 5.2), en quarantaine.

- **Objet** : choisir **une seule** famille du § 1.2 — je recommande les **bornes d'impossibilité de détection** (Q4 du pilier), parce que c'est la famille où le pont « hypothèse du théorème ⇒ supposition mise en défaut » est le plus direct et le plus clairement au niveau de l'idée — et écrire, en langue naturelle d'abord, **la forme** d'une question d'impossibilité : quelles hypothèses un moniteur à sondes fait-il, implicitement, et laquelle un énoncé d'impossibilité pourrait-il isoler ? **Sans écrire l'énoncé formel, sans aucune cible chiffrée, sans aucune construction.**
- **Produit** : une courte liste de **questions** (pas d'énoncés), rangée en quarantaine, qui sert de matière première à la course des nouvelles attaques et au pilier. Chaque question est formulée de sorte que sa réponse serait un théorème, pas une recette.
- **Pourquoi sans dépense** : écrire des questions et repérer des hypothèses de moniteurs ne demande ni appel de modèle, ni machine, ni Lean installé. Lean n'entre qu'à l'étape de **formalisation** d'un énoncé choisi, qui est déjà une dépense (outillage D-1a, puis pilote).

### 3.2 Ce qu'il faut avant toute dépense

Dans l'ordre, aucune de ces pièces n'existe aujourd'hui pour ce travail :

1. **Un texte préenregistré** (R1), écrit par Fable 5.2, contre-lu par Opus 5.5 (R2), qui fixe : la famille visée, la forme des énoncés, les gardes de fidélité et de nouveauté reprises de la note de conception, le rangement en quarantaine, les quatre épreuves de la note de périmètre appliquées aux candidats dérivés, et la liste d'arrêt. **Aucune lecture de résultat avant scellement.**
2. **Un devis par phase** (nœud, dépense) : l'outillage Lean est déjà couvert jusqu'au 30 novembre (GO-2026-11-10-13, 0,56 USD dépensés sur 65) pour l'installation seule, sans appel de modèle ; **la formalisation assistée et toute course sont des dépenses neuves, sans devis ni GO à ce jour**. Les ordres de grandeur du pilier (note de conception, § 5 : de l'ordre du millier de dollars pour un pilote) valent comme borne, pas comme devis.
3. **Le mot du directeur** : la levée partielle de N12 (b) et de DP-1 (a) que porte GO-2026-11-21-12 autorise **le travail de table du § 3.1** (au niveau de l'idée, session à part, mère aveugle au procédé). Tout ce qui va au-delà — formaliser un énoncé en Lean, lancer une course, construire une banque — est un **nœud** : arrêt, attente du GO.
4. **La règle des trois chantiers actifs** : ce travail se range sous le bras d'attaque déjà actif (§ 2.1). S'il devait devenir un chantier distinct (par exemple un pilote de formalisation dédié à l'attaque), il faudrait fermer un chantier actif ou un mot de Lazar.

---

## 4. Risques

1. **Antériorité (R7, R8).** L'idée « lire un théorème d'impossibilité à l'envers pour en tirer une attaque » n'est pas neuve en soi : c'est la logique de toute preuve de borne inférieure en sécurité et en apprentissage. **Ce qui pourrait être neuf**, ce sont des *modes* précis qu'on en dérive — et seule la règle d'antériorité de la course (deux lecteurs isolés, lecture sur PDF empreinté, page citée) peut le dire, après coup. La zone « théorèmes d'impossibilité pour les sondes d'intention » **paraît** peu occupée ; c'est une **question**, à durcir, pas un trou acquis (R8 ; faux-gap). Les antériorités du § 6.3 de la note de conception (bancs de preuve, génération de conjectures, juges de nouveauté sous attaque) ne sont pas vérifiées sur PDF.
2. **Faux-gap propre au côté attaque.** Un théorème d'impossibilité **vrai mais vide** (hypothèses jamais réunies en pratique) donnerait une visée d'attaque séduisante et creuse. Le garde contre ce risque est le lien obligatoire avec le banc de mesure scellé (§ 1.3, § 2.3) : la preuve donne la visée, la course donne la réalité ; **une visée non éprouvée n'est jamais revendiquée comme un mode réel.** La symétrie (R3, R4) joue : un théorème « trop beau » (une impossibilité large et facile) déclenche le même audit qu'un échec.
3. **Double usage.** C'est le risque central. Un mode d'attaque conçu ici est, par nature, une connaissance qui pourrait servir à **contourner** un contrôle, pas seulement à le mesurer. Les six garde-fous existent pour cela ; le garde-fou 5 (un lecteur d'une autre lignée demande « sert-il à autre chose que mesurer ? ») est le filtre explicite du double usage, et un « oui » bloque. **Aucun mode ne sort de la quarantaine sans la revue de sécurité externe** (garde-fou 6, R-611 étendue).
4. **Ce qui ne doit jamais sortir de la quarantaine** : la dérivation retournée (la lecture « côté attaque » d'un théorème), le couple (visée, supposition mise en défaut) écrit côté attaque, et *a fortiori* tout procédé si un jour un procédé était permis (mot de Lazar du 20 novembre sur les recettes de modes inédits, note de périmètre § 6, qui reste un nœud à trancher). Hors quarantaine ne peuvent aller que : le **théorème nu** (côté défense, utile aux concepteurs de moniteurs), et, dans le registre servi, le **nom et l'énoncé** d'un mode, vérifiés par programme. **Jamais** un énoncé d'attaque dans un registre du dépôt, une passation ou un message : un nom suffit à spécialiser un moniteur (note de périmètre, § 4).
5. **Cloison d'or fragile (§ 2.2).** Comme le théorème est le même des deux côtés, le risque est qu'une session de conception de moniteurs lise, par mégarde, la dérivation retournée au lieu du théorème nu. La règle : la dérivation ne vit qu'en quarantaine, et toute pièce en clair (au pilier, sur `main`) ne porte que le théorème nu. Toute ambiguïté se tranche **vers la quarantaine**.
6. **Dérive de G0 et des chantiers actifs.** Le pilier théorique n'est pas sur le chemin de la porte de sortie G0 (instruments). Ce travail ne doit pas prendre le temps des trois chantiers actifs (saboteur et sondes pour l'entretien, bras A, organisme v9). Le premier pas (§ 3.1) est léger ; au-delà, c'est un nœud.

---

## 5. Comment vérifier, de l'extérieur, qu'un mode ainsi conçu est inédit et réel

Deux affirmations distinctes, deux vérifications distinctes ; aucune ne repose sur notre seule parole.

### 5.1 Inédit

- **Antériorité à deux lecteurs isolés** (règle de la course, R8) : chaque épreuve (dont l'épreuve 4, « diffère de chaque mode de la liste de référence scellée ») est tranchée par deux lecteurs d'antériorité à part, chacun sur PDF empreinté, page citée (R7) ; un désaccord vaut non.
- **Le juge de nouveauté de l'organisme** sur l'énoncé mathématique sous-jacent : trois étiquettes (« connu », « corollaire immédiat de la bibliothèque », « non trouvé dans les pièces lues »), jamais « nouveau », avec un plancher mécanique (pas un corollaire immédiat de Mathlib au commit épinglé) et un taux de faux « neuf » mesuré sur une banque de connus plantés. Si l'énoncé est connu, le mode qui s'en dérive est une variante, pas un inédit.
- **La revue de sécurité externe** (garde-fou 6) : un lecteur extérieur, hors du programme, confirme ou infirme la nouveauté avant toute sortie. C'est la vérification « hors de nous » la plus forte sur l'inédit.
- **La trace rejouable** : la preuve Lean est rejouable à la version épinglée de la chaîne et de Mathlib par quiconque, sans nous croire. L'énoncé démontré est un fait public vérifiable (une fois la revue externe franchie et la sortie autorisée).

### 5.2 Réel

- **Le banc de mesure scellé et la course** (garde-fou 4) : un mode n'est dit **réel** que si, préenregistré, il **bat** une base de contrôle sur le banc — c.-à-d. si le régime visé par le théorème est **atteignable** et si le mode y dégrade la détection, mesuré contre un jumeau honnête et des bases boîte blanche (dans l'esprit de N-056, G1). Une visée dérivée d'un théorème **vrai mais vide** échoue ici : c'est le filtre du faux-gap (§ 4, risque 2).
- **Préenregistrement et contre-lecture** (R1, R2, R13) : prédiction chiffrée et signe gelés avant le run, verdict prononcé par un sous-agent neuf qui applique les critères gelés, scellé, soumis à Lazar. Aucun run ne vise un signe positif (R3).
- **Reproduction externe** : à terme, après la revue de sécurité et une éventuelle publication, un tiers peut rejouer la preuve Lean (inédit, § 5.1) **et** le banc de mesure (réel) — les deux moitiés de la vérification, séparées, chacune opposable.

---

## 6. Pour Lazar (résumé)

- **Ce qui est ouvert par GO-2026-11-21-12** : le travail de table du § 3.1 (une liste de *questions* d'impossibilité, au niveau de l'idée, session à part, mère aveugle au procédé, en quarantaine), sans dépense de modèle. C'est le seul pas sans nœud.
- **Ce qui reste un nœud** (arrêt, attente du GO) : formaliser un énoncé en Lean pour l'attaque ; toute course ou banque qui appelle un modèle ; le rattachement d'une famille de menaces diffuses au programme ; la question (ouverte, note de périmètre § 6) de savoir si un procédé est un jour permis sur un mode inédit.
- **Recommandation** : commencer par la famille des **bornes d'impossibilité de détection** (le pont le plus net entre hypothèse de théorème et supposition de moniteur), au niveau des questions seulement ; écrire ensuite un préenregistrement contre-lu avant toute formalisation ; ne rien dépenser sans devis par phase et ton mot. Confiance : moyenne-haute sur la direction ; la valeur réelle ne se saura qu'au banc. Défaut : aucun (tout pas au-delà du § 3.1 est un nœud).
