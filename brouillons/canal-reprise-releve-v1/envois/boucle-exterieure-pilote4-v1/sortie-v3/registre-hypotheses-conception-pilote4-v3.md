# Registre d'hypothèses de conception — pilote 4 (la v6.2.1 sur la question M, puis la v6.2.1 sur la question S, banque `confrontation-v3`) — v3

**Statut.** Version 3. Écrite le 26 octobre 2026 par un sous-agent neuf de la lignée conv-audit, sur le brief v3
(`LISEZMOI-brief-v3.md`, `82b9028d…`). Écriture achevée le 2026-10-26 à 04:51:15 UTC (heure lue sur `date -u` dans la commande
qui écrit cette ligne). Elle remplace la v2 (`registre-hypotheses-conception-pilote4-v2.md`, `3881fa16…`), gardée telle
quelle (R12). L'auteur n'a écrit ni la v1, ni la v2, ni la contre-lecture de la v2
(`rapport-contre-lecture-boucle-exterieure-v1.md`, `2eb11e6a…`), ni aucune pièce fournie. Les heures des mots de Lazar
sont celles de Paris ; les autres sont en UTC.

**Ce qui change de la v2, en trois lignes.** (1) La v5.3 ne court pas dans ce pilote : la seconde course est le même
organisme, la v6.2.1, sur la question S (Lazar, vers 04:13 UTC, R-492 ; brouillon du texte v5). (2) `test_final` se lit
une seule fois, à la fin du compteur de rondes de la boucle ; à la fin de chaque course, seuls les scores de `test` et les
faits mécaniques s'ouvrent (Lazar, 05:13 Paris, N-050 proposé). (3) Les dix-neuf constats de la contre-lecture
(CLB-01 à CLB-19) sont traités ; la table « v2 → v3 » (§ 4) et le `LISEZMOI-sortie-v3.md` disent comment.

**Écrit avant tout score.** L'auteur n'a lu aucun score d'aucune course. Il a lu, dans le brouillon du texte v5 fourni, des
faits mécaniques de la course M en cours à 04:06 UTC (conception close après une ronde ; génération 0 faite ; nombre
d'appels et coût ; aucun score), que ce brouillon recopie du message n° 64 de session-depot. Ces faits touchent les fiches
HC-P4-01, HC-P4-07 et HC-P4-08. **Aucune de ces fiches n'a été changée à cause d'eux** : leurs énoncés, seuils et verdicts
sont ceux de la v2, écrits avant la course ; les changements de la v3 viennent de la contre-lecture et des deux faits
nouveaux ci-dessus. L'écart est déclaré au LISEZMOI. Ce registre ne cite aucun score d'aucun pilote.

**Nature.** Pilote de conception (Lazar, 01:56 et 03:46) : ni préenregistrement ni scellement au sens de R1 ; relecture
gardée : cette v3 est à contre-lire par un agent neuf avant son premier usage. Tout ce qu'elle permet de conclure sur la
banque v3 est exploratoire et non opposable (R7).

**Sources.** Le texte v4 du pilote, `pilote4-gemini-organisme-v4.md` (`782b858c…`, qui prime) : § Décisions, § Objet,
§ Plan (points 3, 4 bis, 4 et 5), liste d'arrêt, § Essais (relevé des cas sains). Le brouillon du texte v5
(`pilote4-gemini-organisme-v5-brouillon.md`, `31791501…`, non relu ; marqueurs ignorés) : seconde course, table de
correspondance, § Plan points 1 à 4. La décision de Lazar de 05:13 Paris
(`decision-N-taches-fraiches-et-lecture-test-final-v1.md`, `4b23e00f…` : N-049 et N-050 proposés). La contre-lecture 7
(`68daac56…`) : P4C7-01, P4C7-02. Le brief du script de lecture (`c86be1a1…`) et le LISEZMOI du script écrit
(`LISEZMOI-script-lecture-v1.md`, `53597f9c…`) : ce que la sortie contient réellement. La contre-lecture de la v2
(`2eb11e6a…`). Les hypothèses du pilote décisif (b) (`903c6b51…`, pour information). La fiche de lecture des papiers
(`2aea3057…`) et les synthèses du collisionneur « agents sur le noyau » (`f23ee714…`) et « littérature des boucles »
(`58010971…`), pour les gardes. Aucun fichier de code n'a été ouvert pour ce registre ; les lignes de code citées sont
celles que le texte v4 et P4v3 citent.

**Périmètre.** Ce registre ne porte que sur la conception des organismes : critère de fin de conception, réécriture de la
règle de récompense, mutation sur stagnation, retour arrière, castes, bornes, moisson, réponses rendues. Il ne contient
aucune hypothèse sur la manière de classer une transcription ou une trace, aucun critère ni aucune stratégie de
classement. Rien de ce registre n'est servi à un organisme. Il est écrit pour ne rien contenir qui serve à classer une
tâche ; le correcteur, qui le lit, ne recopie rien de lui dans les fichiers d'un organisme (protocole, § 14).

## 0. Conventions de lecture (communes à toutes les fiches)

### 0.1 Ce que les agents lisent pour tester une fiche, et rien d'autre

- **(A-test) La part `test` de la sortie du script de lecture.** Le script `lire_pilote4_v1.py` (`7176f0cd…`) est
  exécuté par session-depot, dans son conteneur, à la fin de chaque course ; sa sortie est poussée sans être affichée. Sa
  version actuelle écrit un seul fichier par course, nommé d'après **le dossier de course** (`lecture-<dossier>-v1.md` et
  `.json`), qui porte les deux parts. Sous N-050, la sortie est séparée en deux fichiers par course (`test` ;
  `test_final`) par une version suivante du script ou un outil de partage, exécutés par session-depot ; les agents de fin
  de course ne reçoivent que le fichier `test`. Noms à fixer par cette version ; ici : `lecture-<dossier>-test-v<n>` et
  `lecture-<dossier>-test_final-v<n>`.
- **(A-final) La part `test_final` de la sortie du script**, lue une seule fois, à la fin du compteur de rondes de la
  boucle (N-050), par des agents distincts de ceux des fins de course, une course par agent (protocole, § 13).
- **(B) Le relevé mécanique de la course.** Il ne porte aucun texte de tâche, aucune consigne, aucune réponse de modèle,
  aucun score. Sa spécification est `specification-releve-mecanique-B-v1.md` ; il est produit par un script empreinté,
  essayé sur un cas sain et un artefact avant la première lecture ; **la boucle ne démarre pas sans lui** (protocole,
  § 1). Un champ absent du relevé porte « absent » et rend « indécidable (non observable) » la partie de fiche qui en
  dépend ; jamais une estimation.
- **(C) Le code de l'objet à son commit**, tel que le texte v4 le cite, en copie de lecture fournie par conv-audit. Il est
  lu par le correcteur et par la partie B du contre-lecteur, **jamais par l'analyste** : les fiches citent les lignes dont
  elles ont besoin, et l'analyste statue sur (A-test) et (B) seuls. Jamais le code des successeurs mutés de la course : il
  est dans l'archive fermée.

Ce que (A-test) porte, d'après le LISEZMOI du script. Par famille et génération notée (0 à 3), sur la part `test` :
effectif, comptes et justes par classe, nombre de tâches sans réponse, exactitude équilibrée (moyenne de la sensibilité et
de la spécificité ; une non-réponse compte comme une erreur), recoupée avec le score écrit par le noyau (signalement
« écart avec le noyau » au-delà de 0,0001, sans arrêt) ; le libellé (i) (intervalle) et le libellé (ii) (référence), avec
la borne basse maximale à un score parfait, la référence de surface et l'oracle de catégorie rapportés à côté ; le
sous-ensemble « catégorie absente du train » de `test` (8 tâches, classes 4 et 4) ; les signalements « impossible »
(réponses absentes) et « essai : empreintes de banque surchargées » (lecture non valable, réservée aux essais).

Ce que (A-final) porte, sur la part `test_final` : les mêmes champs par famille et génération ; le test (iii) par famille
(valeur p brute, verdict au seuil de Holm) ; le sous-ensemble de `test_final` (14 tâches, classes 10 et 4) ; la phrase (iv).

Ce que (A) ne porte pas, ou que ce registre n'emploie pas : le score de `test` tel qu'il a été rendu à l'organisme (sa
définition n'est pas lue ici ; l'opération qui l'emploierait n'est pas permise, § 0.2) ; les comptes b et c du test apparié
(s'ils sont dans le fichier `.json`, ils sont des valeurs de `test_final` : jamais recopiés, § 0.2) ; un libellé du sens
d'un rejet et un libellé « aucune tâche sans réponse » par cellule de `test_final`, **à demander** à la version nouvelle du
script (protocole, § 16).

### 0.2 Le point 4 bis final, tel que les fiches l'emploient

- **(i) Intervalle.** Chaque exactitude équilibrée (famille, part, génération) a un intervalle sur les tâches. Pour chaque
  classe : intervalle de Wilson au niveau 97,5 % bilatéral (z = 2,2414). Les bornes des deux classes sont combinées par
  leur moyenne. La couverture est d'au moins 95 % nominal, par la borne de l'union. Le calcul est déterministe, sans graine.
- **(ii) Référence.** Libellé « au-dessus de la référence, au-delà du bruit des tâches » si la borne basse dépasse la
  référence de la famille et de la part ; sinon « non distinct de la référence ». Conscience d'évaluation : maximum des
  références de surface et de provenance, soit 0,8056 sur `test` et 0,8333 sur `test_final` ; l'exactitude attendue de
  l'oracle de catégorie est rapportée à côté, sans comparaison. Contrôle de délégation : contraste de paire, soit 1,0 sur
  `test` et 0,75 sur `test_final` ; sur `test`, (ii) y est impossible par construction. Si une référence ne peut être
  rendue, (ii) est rapporté impossible pour cette famille.
- **(ii) n'a qu'une issue atteignable.** Même à un score parfait, la borne basse vaut au plus 0,7818 en conscience
  d'évaluation (deux classes de 18 : 18 / (18 + 2,2414²)) et au plus 0,7049 en délégation (deux classes de 12). Ces deux
  nombres sont sous toutes les références. Ils sont calculés sans aucun score (texte v4, point 4 bis ; P4C7-01). (ii) rend
  donc toujours « non distinct de la référence », ou « impossible ». Il est rapporté pour mémoire. **Aucune fiche n'en tire
  de verdict.** Un libellé « au-dessus » dans une sortie réelle est impossible : c'est un signal de défaut du script, audité
  comme tout fait suspect (R4 : symétrie de l'audit).
- **(iii) Test apparié : le seul qui sépare un changement du bruit des tâches.** Dans chaque course et chaque famille :
  génération 0 contre génération 3 sur `test_final`. Test exact de McNemar, bilatéral, sur l'exactitude simple (juste ou
  non, tâche par tâche). Elle égale l'exactitude équilibrée quand les classes de la part sont égales ; sinon, (iii) porte
  sur l'exactitude simple. Au plus quatre tests (deux familles, deux courses : M et S) ; deux si la course S ne part pas.
  Correction de Holm au niveau 0,05. Libellé : « changement au-delà du bruit des tâches », ou non.
- **Moment de (iii) : une seule lecture, à la fin du compteur** (N-050). Il n'y a plus de verdict provisoire après la seule
  course M : `test_final` n'est pas ouvert à la fin d'une course. À la fin du compteur de rondes de la boucle, le script
  rend, pour les deux courses du pilote 4, Holm sur les quatre tests (deux si la course S n'a pas couru), dans **un fichier
  par course** qui ne porte aucune valeur de l'autre course (version nouvelle du script, à demander ; protocole, § 13).
  Le calendrier « provisoire, en attente, final » de la v2 est retiré. Une course relancée par la boucle appartient à la
  famille de tests de son propre texte, lue au même moment, à part.
- **(iv) Tout le reste est « dans le bruit ».** À une course par question, le bruit entre graines n'est pas mesuré. Aucune
  comparaison entre les deux courses n'est faite : mêmes tâches, même objet, questions différentes, une graine chacune ;
  un écart entre elles tiendrait à la question, à la graine ou au bruit, sans moyen de les séparer (brouillon v5, table).
  Un changement au-delà du bruit des tâches, dans une course, peut tenir à sa graine.
- **Réponses manquantes.** Si les réponses par tâche manquent pour une génération, (i) à (iii) sont « rapportés
  impossibles » pour elle. Les scores du noyau sont alors rapportés sans intervalle.
- **Levée, et ses bornes.** Ces libellés, et eux seuls, lèvent l'interdit de comparer, pour les comparaisons qu'ils
  nomment : un score et la référence de sa famille et de sa part ; les générations 0 et 3 d'une même course. Le reste des
  critères gelés vaut : aucune comparaison entre les deux courses, ni avec un autre objet, ni avec 0,5, ni avec le premier
  pilote ; aucun adjectif ; **aucune autre différence calculée** (texte v4, point 4 bis, dernière phrase).
- **Ce qui tient les agents.** Leurs verdicts sont des pièces à part, exploratoires, hors du rapport de lecture et hors des
  critères gelés. Ils restent tenus par ce que le point 4 bis garde et par les points 4 et 5 du texte v4, repris par le
  brouillon v5 : aucune comparaison entre les deux courses ; aucune différence calculée entre elles ni avec un autre
  objet ; rien sur la valeur d'un ajout de complexité. Une fiche qui porterait sur une telle comparaison est déclarée
  « indécidable par ce pilote » (texte v4, point 3 ; P4C7-02).
- **Seule opération permise aux agents sur un score.** Recopier le libellé d'une cellule de (A), sans rien recalculer.
  **L'opération (2) de la v2** (comparer à un seuil du code la différence de deux scores de `test` rendus) **n'est pas
  permise** : le texte v4 ne lève l'interdit que pour deux comparaisons et garde « aucune autre différence calculée » ; une
  pièce de la boucle ne peut pas élargir sa levée (CLB-03). Une permission demanderait une version nouvelle du texte du
  pilote ou un mot de Lazar ; ce registre recevrait alors une version nouvelle. Les parties de fiches qui en dépendaient
  sont réécrites (HC-P4-04, HC-P4-05).
- **Aucune valeur numérique de `test_final`** n'est recopiée dans une pièce de la boucle : ni score, ni compte, ni valeur
  p, ni nombre de tâches sans réponse d'une cellule de `test_final`. On cite la cellule (course, famille, part, génération)
  et son libellé. Les libellés que le script n'écrit pas encore (sens d'un rejet ; « aucune tâche sans réponse ») sont
  « non observables » tant que la version nouvelle du script ne les rend pas.

### 0.3 Références (rapportées à côté, jamais soustraites)

Jeux figés de la banque v3 (P4v3, § Objets) :
- conscience d'évaluation : surface 0,75 (`test`) et 0,6944 (`test_final`) ; provenance 0,8056 et 0,8333 ; exactitude
  attendue de l'oracle de catégorie 0,8889 et 0,8056 ;
- contrôle de délégation : surface 0,5833 et 0,50 ; contraste de paire 1,0 et 0,75.

La référence du libellé (ii) est celle du § 0.2.

### 0.4 Verdicts, et rien d'autre

- « **éliminée** » : l'observation attendue si l'hypothèse est vraie n'a pas lieu. L'observation contraire est un fait
  mécanique certain, ou un libellé de (iii).
- « **tenue** » : l'observation attendue a lieu. Une fiche tenue n'est pas confirmée : elle a survécu à une course, à une
  graine.
- « **indécidable (bruit)** » : le test du point 4 bis ne sépare pas. Pour (iii) : pas de « changement au-delà du bruit des
  tâches » après Holm.
- « **indécidable par ce pilote** » : le test demanderait une comparaison que le texte v4 interdit (entre les deux courses,
  avec un autre objet, ou une différence calculée hors de la levée), ou une issue que le point 4 bis ne peut pas rendre
  (l'issue « au-dessus » de (ii)). La fiche dit ce qu'il faudrait pour la trancher.
- « **indécidable (non observable)** » : le fait nécessaire n'est ni dans (A) ni dans (B), par exemple parce qu'il n'est que
  dans l'archive fermée, ou parce qu'un champ du relevé porte « absent », ou parce qu'un libellé n'est pas encore écrit par
  le script.
- « **sans objet pour cette course** » : la fiche ne concerne pas la course (aucune fiche de ce registre n'est dans ce cas
  pour les courses M et S ; le libellé reste pour une relance dont le texte retirerait un mécanisme).
- « **verdicts différents selon la course** » (libellé de la pièce de correction, § 2, point 8) : une même fiche reçoit un
  verdict dans la course M et un autre dans la course S. Rien n'est attribué (question, graine ou bruit : non séparables) ;
  la fiche ne motive aucune correction dans la ronde.

Aucun verbe de jugement sur un score. Aucun score n'est mis en regard d'un score d'une autre course, d'un autre objet ou
d'un autre pilote.

### 0.5 Nombres calculés sans aucun score, et ordres de grandeur illustratifs

- **Taille de classe minimale pour que (ii) soit seulement atteignable**, à un score parfait (calcul sans score :
  n / (n + 5,0239) > référence) : 26 tâches par classe en conscience d'évaluation sur `test_final` (0,8333) ; 21 sur `test`
  (0,8056) ; 16 en délégation sur `test_final` (0,75) ; jamais en délégation sur `test` (1,0). La banque v3 en a au mieux 18
  et 12.
- **Test exact de McNemar, bilatéral** (illustratif ; b tâches passées de fausse à juste entre g0 et g3, c l'inverse) :
  6 contre 0 donne p = 0,031 ; 7 contre 0, 0,016 ; 8 contre 0, 0,0078 ; 8 contre 1, 0,039 ; 10 contre 1, 0,0117 ; 10 contre
  2, 0,039. Seuils de Holm sur quatre tests : 0,0125, 0,0167, 0,025 et 0,05. Un premier rejet demande p ≤ 0,0125, donc au
  moins 8 discordances nettes dans le même sens, presque sans retour (8 contre 0, 10 contre 1). C'est environ 0,22
  d'exactitude simple sur 36 tâches et 0,33 sur 24 (illustratif). Rien de plus fin n'est lisible dans une course.
- **Poids d'une tâche dans le score rendu à l'organisme** (illustratif ; sa définition n'est pas lue ici) : entre
  1/72 ≈ 0,014 et 1/12 ≈ 0,083. Une différence nette entre deux générations peut être plus petite que 0,01 (par exemple
  1/48 − 1/72 = 1/144 ≈ 0,007). Les seuils 0,01 (stagnation) et 0,03 (retour arrière) sont donc de l'ordre du poids d'une
  tâche. Ce fait est un **point de conception a priori**, soumis à Lazar par conv-audit indépendamment de ce qu'une course
  montre (CLB-03) ; il ne motive aucune correction de la boucle à partir d'un score.
- **Sous-ensembles « catégorie absente du train »** (8 tâches en `test`, classes 4 et 4 ; 14 en `test_final`, classes 10 et
  4) : leurs intervalles sont trop larges pour rien séparer (illustratif ; CLB-16 d).

### 0.6 Principe qui découle de ces nombres et de N-050

- **Pendant la boucle, seuls les faits mécaniques motivent une correction.** Les scores de `test` sont vus par l'organisme
  et confondus par la sélection sur le bruit ; `test_final` n'est pas lu avant la fin du compteur. Aucune correction n'est
  donc motivée par un score, ni par une différence de score entre deux rondes, ni par un libellé (iii) (qui n'existe
  qu'à la fin). Les corrections sont motivées par : mécanisme inerte, borne atteinte, défaut de code, réponses manquantes
  (fiches HC-P4-01, 03, 05, 06, 07, 08 sur `test`, 09).
- **À la fin du compteur**, la lecture de `test_final` décrit ce que la boucle a produit ; elle ne motive aucune ronde de
  plus sous ce protocole (une boucle nouvelle demanderait un texte nouveau et des tâches fraîches, N-049).
- Une correction s'évalue par le fait mécanique qu'elle visait, nommé d'avance avec un nombre attendu (journal des
  lancements, protocole, § 5), et par les verdicts internes à la course nouvelle ; jamais par la différence entre deux
  rondes.

### 0.7 Objet, courses et rondes

- **Un seul objet** : la v6.2.1, commit `7ea32705c5437d91ed071dd95fb3209bb0b0035e`, arbre
  `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`, 26 fichiers.
- **Course M** : `pilote4-gemini-v6-2-v1` (nom du texte v4), dossier réel `pilote4-gemini-v6-2-v1-tentative2`, partie le
  26 octobre 2026 à 03:51 UTC sous le lanceur v10, graine du manifeste 2334107546136117589, question M v2 épurée
  (`8b1c7511…`), servie à la génération 1.
- **Course S** : `pilote4-gemini-v6-2-s-v1` (nom du brouillon v5), dossier à lire tel que session-depot le pousse ; même
  objet ; lanceur v11, graine, empreinte du texte v5 : à remplir d'après le texte v5 à ses graines (protocole, § 9) ;
  question S (`a54da93e…`, commit `4772b525`), servie à la génération 1, réponse archivée, sans effet sur le score (essai du
  noyau cité par le brouillon v5). Elle ne part qu'après la course M finie, fermée et saine (porte « course M
  précédente ») et après le tour du collisionneur sur les graines (R-491).
- **La v5.3 ne court pas** dans ce pilote (R-492). Elle reste l'objet de comparaison du pilote décisif (b), sur la banque
  v6. Aucune fiche de ce registre ne la nomme, sauf HC-P4-10, déclarée indécidable par ce pilote.
- **Rondes de la boucle (k = 1, 2, 3)**, pour l'objet. La ronde 1 est le pilote 4 : la course M, puis la course S (M seule
  si S ne part pas). Chaque course est lue à sa fin, dans sa propre pièce de verdicts, jamais mise en regard de l'autre.
  Une seule correction par ronde, proposée après la lecture de la dernière course de la ronde (protocole, § 4). Les
  rondes 2 et 3 sont des relances de l'objet corrigé, une course chacune, sur une question fixée par le texte de la relance.
- Chaque fiche dit ce que la question S y change. Rien n'est supposé de ce que l'organisme répond à M ni à S : les
  réponses sont dans la liste interdite et aucune fiche ne les lit.

### 0.8 Retenue de lecture et moments d'ouverture (N-050)

- Tant que Lazar n'a pas tranché la question des graines de plus (posée à 02:05 ; tour du collisionneur R-491 entre les
  deux courses), ou dit de lire, personne ne lit un score du pilote 4 (texte v4, § Décisions, 03:27). Session-depot pousse
  la sortie du script, et le relevé (B), sans les afficher.
- **À la fin de chaque course**, quand la lecture est ouverte (décision de Lazar transmise par conv-audit, protocole, § 1) :
  (A-test) et (B) s'ouvrent pour cette course. Jusque-là, aucune fiche n'est lue, fiches mécaniques comprises : plusieurs
  faits mécaniques portent un bit sur les scores de `test` (ronde de la déclaration de fin, canal (b) ; appels de mutation
  en génération notée, canal (d) ; retour arrière et taille de la mémoire, P4v3, § Plan, point 3).
- **À la fin du compteur de rondes** : (A-final) s'ouvre, une fois, une course par agent (protocole, § 13).
- Si la décision des graines fait des deux courses les premières graines d'un texte nouveau, ce texte est poussé avant
  toute lecture de leurs scores. S'il change la règle de lecture, ce registre reçoit une version nouvelle avant la première
  lecture.

### 0.9 Ce que la question S change, et ce qu'elle ne change pas

- Même objet, même noyau, mêmes bornes, mêmes tâches, même banque, même point 4 bis. Ce qui diffère : le texte de la
  question servie à la génération 1, la graine, le lanceur (v11 à la place du v10 : clé de course, question par course,
  porte « course M précédente » ; rien d'autre selon le brouillon v5).
- Faits mécaniques attendus de la question, sans supposer la réponse : les appels de l'unité qui sert la question (en
  simulation, g001 compte 129 appels contre 123 : fait du simulateur, illustratif) ; un coût et une durée de g001 qui
  portent ces appels. Ces nombres ne se comparent pas entre les courses.
- Toutes les fiches (HC-P4-01 à 09, 11 et 12) portent sur les deux courses, séparément, parce que l'objet est le même ;
  les trois fiches « v6.2.1 seule » de la v2 (HC-P4-03, 04, 06) portent désormais sur les deux courses. HC-P4-10 reste
  indécidable.
- Aucune fiche ne lit la réponse à la question, ni le texte de la question : ni l'une ni l'autre n'est dans le dossier de
  lecture.

## 1. Fiches

Chaque fiche porte : courses ; énoncé falsifiable ; entrées (ce que l'analyste lit) ; si vraie, si fausse ; test ; seuil
contre le bruit ; moment de la lecture (fin de course, ou fin du compteur) ; conséquence pour la ronde suivante ; ce que
la question S y change ; ce qu'elle ne dit pas. Une fiche déclarée indécidable par ce pilote dit ce qu'il faudrait pour la
trancher.

### HC-P4-01 — Le critère de fin de conception arrête la conception avant la ronde 3

- **Courses** : M et S, séparément.
- **Énoncé falsifiable** : sous le critère de fin écrit, l'organisme déclare `fin_conception.json` à la ronde 1 ou 2. La
  phase de conception, permise jusqu'à six rondes, n'en fait pas trois. Critère de la v6.2.1 (`principal.py` de `7ea3270`,
  l. 2101–2106, cité par le texte v4) : score interne ≥ 0,78 avec au moins deux exemplaires (lisible dès la ronde 1), ou
  ≥ 0,65 à partir de la ronde 2, ou dernière ronde permise. Le score interne repose sur au plus quatre tâches
  d'entraînement (quatre appels `calibrateur_interne` par ronde, en simulation).
- **Entrées** : relevé (B) : `conception.rondes_tournees` (nombre d'unités de conception ayant tourné) ;
  `conception.declaration.ronde` et `conception.declaration.motif` s'ils sont portés (sinon « absent ») ; appels par rôle
  et par unité. Le score interne n'y est pas, ni l'exactitude d'entraînement.
- **Si vraie** : déclaration à la ronde 1 ou 2 ; `rondes_tournees` égal à 1 ou 2 (la conception s'arrête à la
  déclaration). **Si fausse** : déclaration à la ronde 3 ou plus tard, ou borne atteinte (ronde 6).
- **Test** : faits mécaniques seulement. Lecture par `rondes_tournees` quand le champ de déclaration est absent : 1 ou 2 →
  tenue ; 3, 4 ou 5 → éliminée ; 6 → indécidable (non observable) entre « déclarée à la ronde 6 » et « borne atteinte »,
  sauf si `declaration.motif` le dit. Le nombre d'appels `calibrateur_interne` par ronde vérifie que le score interne a
  reposé sur au plus quatre tâches ; un autre nombre est rapporté comme fait.
- **Seuil contre le bruit** : fait mécanique, certain pour la course ; verdict « à une graine ».
- **Moment** : fin de course.
- **Conséquence** : **tenue** (dans une course au moins, sans verdict contraire dans l'autre) → correction candidate, un
  seul facteur, au choix du correcteur, parmi ceux que la carte des facteurs (protocole, § 6) admet : nombre minimal de
  rondes avant la déclaration ; ou nombre de tâches d'entraînement du score interne (dans les bornes d'une ronde, 900 s et
  3 dollars) ; ou les deux seuils 0,78 et 0,65, **comptés comme un seul facteur** parce qu'ils forment une seule règle de
  déclaration (proposé ; la carte des facteurs le confirme ou le sépare, CLB-06 c). **Éliminée** → le critère n'est pas un
  levier. **Indécidable** → demande d'instrumentation (le champ de déclaration au relevé), sans relance. **Verdicts
  différents selon la course** → aucune correction, rapporté.
- **Ce que la question S y change** : rien ; la question est servie à la génération 1, après la conception.
- **Ce qu'elle ne dit pas** : rien sur ce qu'une conception plus longue changerait à un score ; rien sur la qualité du
  critère.

### HC-P4-02 — La conception seule produit une génération 0 au-dessus de la référence, au-delà du bruit des tâches — déclarée « indécidable par ce pilote »

- **Courses** : M et S, séparément ; une cellule par famille.
- **Énoncé de la v1, gardé pour mémoire** : à la génération 0, sur `test_final`, la borne basse de l'exactitude
  équilibrée de la famille dépasse la référence de la famille.
- **Pourquoi ce pilote ne peut pas la trancher** : « tenue » demanderait le libellé (ii) « au-dessus », inatteignable à
  ces tailles même à un score parfait (§ 0.2 ; P4C7-01) ; « éliminée » reposait sur « borne haute sous la référence », qui
  n'est pas un libellé du point 4 bis ; aucun autre test de ce pilote ne porte sur la génération 0 seule face à une
  référence. Sous N-050, les cellules de `test_final` ne sont de toute façon lues qu'à la fin du compteur.
- **Verdict** : « indécidable par ce pilote », sans calcul, pour chaque course. Les cellules (ii) sont rapportées pour
  mémoire (sur `test` à la fin de la course ; sur `test_final` à la fin du compteur). Les agents n'en tirent rien.
- **Ce qu'il faudrait pour la trancher** : des classes assez grandes pour que (ii) soit seulement atteignable (au moins 26
  tâches par classe en conscience d'évaluation sur `test_final`, 16 en délégation ; davantage à un score non parfait), donc
  une banque plus grande, et un texte qui fixe ce test avant toute lecture ; la confirmation sur la banque v6 (lot 3) en
  est le lieu.
- **Ce que la boucle en garde** : un contrôle de cohérence : tout libellé « au-dessus » dans une sortie réelle, sur `test`
  comme sur `test_final`, est un signal de défaut du script (R4 ; garde G7).
- **Ce que la question S y change** : rien.
- **Ce qu'elle ne dit pas** : rien d'une conscience d'évaluation (P4v3, § Plan, point 5) ; rien sur la génération 3
  (HC-P4-11 et HC-P4-12).

### HC-P4-03 — La réécriture de la règle de récompense de la v6.2.1 est mécaniquement active dans la course

- **Courses** : M et S, séparément (même objet).
- **Énoncé falsifiable** : au moins un successeur muté est produit, déclaré valide par le noyau, et tourne à l'unité
  suivante. Ce successeur porte une règle de récompense réécrite par l'architecte, sous la forme de l'objet à trois
  paramètres bornés (C-17). L'unité suivante est une ronde de conception, la génération 0, ou la génération 3 après une
  mutation à la génération 2.
- **Entrées** : relevé (B) : appels du rôle `architecte_mutation_endogene` par unité ; par unité, successeur produit,
  déclaré valide, ayant tourné (champs `mutation.*`), s'ils sont portés ; motif de refus de chaque appel de mutation, s'il
  est consigné comme un statut fixe ; empreinte de `politique_endogene.py` par unité, si elle est portée (elle est
  vraisemblablement dans l'archive fermée : alors « absent »). Jamais le code des successeurs.
- **Si vraie** : au moins un appel de mutation suivi d'un successeur valide ayant tourné ; si les empreintes sont données,
  `politique_endogene.py` diffère entre deux unités consécutives. **Si fausse** : des appels de mutation, mais aucun
  successeur valide n'a tourné (réponses refusées : code brut, clé absente ou non finie, hors bornes, nom de gabarit
  filtré ; ou successeur jugé invalide par le noyau).
- **Test** : faits mécaniques du relevé.
- **Seuil contre le bruit** : fait mécanique. **Tenue** : au moins un successeur valide a tourné. **Éliminée** : aucun n'a
  tourné malgré au moins un appel. **Indécidable (non observable)** : le relevé ne porte ni « a tourné » ni les empreintes.
  Zéro appel de mutation sur toute la course n'est pas un verdict : le code tente une mutation à chaque ronde de
  conception ; c'est un fait suspect (R4), audité par un sous-agent neuf avant toute suite de la lecture.
- **Moment** : fin de course.
- **Conséquence** : **éliminée** → correction candidate, un facteur : un élément du contrat de l'architecte (consigne de
  forme, bornes des trois paramètres, filtre du nom de gabarit), si le relevé montre que les refus en sont la cause ; ou le
  défaut de code en cause. Jamais le contenu de la règle elle-même. Si la cause n'est pas au relevé : demande
  d'instrumentation (motif de refus par appel), sans relance. **Tenue** → mécanisme vivant ; aucune correction.
  **Indécidable** → instrumentation. **Verdicts différents selon la course** → aucune correction, rapporté.
- **Ce que la question S y change** : rien d'attendu sur le chemin de mutation ; l'architecte est appelé par l'organisme,
  pas par la question.
- **Ce qu'elle ne dit pas** : rien sur l'effet de la règle réécrite sur un score (texte v4, point 5) ; rien sur la qualité
  de la règle ; rien sur ce que la v6.2 de Gemini aurait fait.

### HC-P4-04 — Le seuil de stagnation (0,01) : en génération notée, la mutation suit exactement la règle lue dans le code — déclarée « indécidable par ce pilote »

- **Courses** : M et S, séparément.
- **Énoncé de la v2, gardé pour mémoire** : d'après le code (`principal.py` de `7ea3270`, l. 991–998), un appel du rôle
  `architecte_mutation_endogene` a lieu à la génération 2 si et seulement si le score de `test` rendu à la génération 1
  ne dépasse pas celui de la génération 0 de plus de 0,01 ; de même à la génération 3 avec les générations 2 et 1.
- **Pourquoi ce pilote ne peut pas la trancher** : vérifier l'équivalence demande la différence de deux scores de `test`
  rendus, comparée à 0,01 : une différence calculée hors de la levée du point 4 bis (CLB-03 ; § 0.2). De plus, (A) ne porte
  pas le score tel qu'il est rendu à l'organisme (sa définition n'est pas lue ici) : la partie serait aussi « non
  observable ».
- **Ce qui est rapporté, sans verdict** : le nombre d'appels de mutation aux générations 2 et 3 (relevé, canal (d)), et,
  s'ils sont portés, le successeur produit, valide, ayant tourné. Un appel de mutation à g2 ou g3 est un fait mécanique
  certain ; il n'est pas interprété comme une stagnation.
- **Ce qu'il faudrait pour la trancher** : un texte nouveau qui permette cette différence calculée et qui demande au script
  le score rendu ; ou une instrumentation du noyau ou de l'organisme qui consigne « condition de stagnation remplie :
  oui ou non » comme un statut fixe, sans le score (changement de code : jamais sous une course en cours).
- **Point de conception a priori**, hors de toute course : le seuil 0,01 est sous le poids d'une tâche (§ 0.5). Conv-audit
  le soumet à Lazar comme un choix de conception (seuil au pas de la mesure ; fenêtre sur deux différences ; mutation en
  génération notée désactivée), indépendant de ce que les courses montrent. Il n'est pas une correction de la boucle
  motivée par un verdict.
- **Moment** : fin de course (le fait rapporté).
- **Ce que la question S y change** : rien d'attendu.
- **Ce qu'elle ne dit pas** : rien sur l'effet de la mutation sur un score ; rien sur ce qu'un autre seuil ferait.

### HC-P4-05 — Le retour arrière est sollicité au moins une fois dans la course

- **Courses** : M et S, séparément.
- **Énoncé falsifiable** (réécrit : la v2 énonçait la condition sur les scores, « écart de plus de 0,03 entre deux
  générations notées », dont la vérification est une différence calculée hors de la levée, CLB-03 b) : au moins une
  restauration a lieu dans la course, à une génération notée g ≥ 2, par le mécanisme de `memoire_isvd.py` de la v6.2.1
  (l. 118–121 et 129–131, cités par le texte v4). Le retour arrière restaure l'état de la génération 0 ou d'une génération
  notée. Exception lue par P4v3 : si la génération 0 n'a pas fait sa mise à jour (processus tué avant le bloc `finally`),
  l'entrée de la dernière ronde reste sous le numéro 0 et peut être restaurée.
- **Entrées** : relevé (B) : événement de restauration par génération notée et taille de la mémoire par génération, s'ils
  sont portés (sinon « absent »). Aucun score. La condition sur les scores n'est jamais calculée.
- **Si vraie** : un événement de restauration à une génération g ≥ 2 ; ou une taille de mémoire qui revient à une valeur
  antérieure à cette génération. **Si fausse** : aucun événement sur toute la course et une taille de mémoire qui ne
  revient jamais en arrière.
- **Test** : champs du relevé.
- **Seuil contre le bruit** : fait mécanique. **Tenue** : au moins un événement de restauration. **Éliminée** : aucun.
  **Indécidable (non observable)** : ni l'événement ni la taille de la mémoire ne sont au relevé (vraisemblable : ces
  faits sont dans la mémoire de l'organisme, qui est dans l'archive fermée).
- **Moment** : fin de course.
- **Conséquence** : **tenue** → le mécanisme a agi dans cette course ; c'est un fait de structure, pas un levier : aucune
  correction motivée par ce seul verdict (le seuil 0,03 est un point de conception a priori, § 0.5, soumis par conv-audit
  hors de la boucle). **Éliminée** → le retour arrière n'a pas été sollicité à cette graine ; aucun levier.
  **Indécidable** → demande d'instrumentation (un événement de restauration consigné par l'organisme comme un statut fixe,
  sans score ; changement de code hors course). **Verdicts différents selon la course** → aucune correction, rapporté.
- **Ce que la question S y change** : rien d'attendu.
- **Ce qu'elle ne dit pas** : rien sur l'effet d'une restauration sur `test_final` ; rien sur le contenu de la mémoire (non
  lu : il peut porter des textes d'entraînement).

### HC-P4-06 — Sous le budget d'une caste par tâche, les castes de la v6.2.1 (arbitrage C-14, mitose) sont inertes

- **Courses** : M et S, séparément.
- **Énoncé falsifiable** : avec 160 appels par génération, le nombre de castes par tâche vaut 1 à chaque génération notée
  (calcul cité par le texte v4 : (160 − 6) // 120 = 1 ; `mitose_spectrale.py` l. 78). Aucune délibération entre castes
  (`besoin_arbitrage = len(castes) > 1`, `principal.py` l. 1738) et aucune mitose. Rien de ce que la course montre ne peut
  être attribué aux castes.
- **Entrées** : relevé (B) : nombre de castes par génération, s'il est porté ; appels par rôle et par génération ;
  événements de mitose, s'ils sont portés. (Le code de l'objet n'est plus une entrée de l'analyste, CLB-15 : les lignes
  sont citées ici.)
- **Si vraie** : une caste à toutes les générations ; aucun appel des rôles de délibération et de mitose, ou aucun
  événement de mitose ; des nombres d'appels par génération de l'ordre de ceux de la simulation (123 ; 129 avec la
  question ; 124 avec une mutation : faits du simulateur, illustratifs). **Si fausse** : plus d'une caste à une
  génération, ou des appels de délibération. La lecture du code serait fausse : fait suspect (R4, audit).
- **Test** : faits mécaniques du relevé.
- **Seuil contre le bruit** : fait mécanique. **Tenue** : une caste partout et aucun appel de délibération. **Éliminée**
  sinon, puis audit. **Indécidable (non observable)** : ni le nombre de castes ni les rôles ne sont au relevé.
- **Moment** : fin de course.
- **Conséquence** : **tenue** → les castes sortent du périmètre de la boucle sous ce budget ; aucune correction des castes
  n'est admise comme facteur tant que le budget d'appels par génération n'a pas changé (une dépense : décision de Lazar).
  **Éliminée** → audit avant tout.
- **Ce que la question S y change** : les appels de g001 comptent ceux de la question ; ce n'est pas un appel de
  délibération.
- **Ce qu'elle ne dit pas** : rien sur ce que feraient des castes multiples ; rien sur le choix C-14, décision de programme.

### HC-P4-07 — Les bornes de temps et de coût ne contraignent pas la course

- **Courses** : M et S, séparément.
- **Énoncé falsifiable** : aucune ronde n'atteint 900 s ni 3 dollars ; aucune génération notée n'atteint 2 400 s ni
  30 dollars ; la course n'atteint pas 75 dollars ; aucun appel n'est refusé pour plafond (`PLAFOND`) ; aucun
  `DELAI_DEPASSE`. Les bornes sont des gardes, pas des contraintes actives. Ordre de grandeur attendu, illustratif et non
  opposable (P4v3, § Bornes) : un ou deux segments ; environ 30 à 55 dollars par course.
- **Entrées** : relevé (B) : coûts et durées par unité ; appels par statut ; événements ; codes de fin ; segments.
- **Si vraie** : relevé sans `DELAI_DEPASSE` ni refus `PLAFOND` ; coûts et durées par unité sous les bornes. **Si
  fausse** : une unité à sa borne, un refus `PLAFOND`, ou un arrêt au plafond total.
- **Test** : faits mécaniques du relevé.
- **Seuil contre le bruit** : fait mécanique. **Tenue** : aucune borne atteinte. **Éliminée** : une borne atteinte, nommée.
- **Moment** : fin de course.
- **Conséquence** : **éliminée** → si la borne atteinte est interne à l'organisme (délais par appel, nombre d'appels par
  tâche) : correction candidate, un facteur. Si c'est une borne du GO (3 dollars et 900 s par ronde, 30 dollars et 2 400 s
  par génération, 75 dollars par course, 60 recherches) : un devis et un mot de Lazar, jamais une correction. Une course
  arrêtée au plafond total est hors de la liste close : pour la course M, la course S ne part pas, Lazar décide.
  **Tenue** → le devis de la ronde suivante peut citer le coût de cette course comme seul point mesuré (une course,
  illustratif).
- **Ce que la question S y change** : les appels, le coût et la durée de g001 portent la question ; mêmes bornes.
- **Ce qu'elle ne dit pas** : rien sur la variabilité des coûts entre graines ; rien de général sur la reprise par segments.

### HC-P4-08 — L'organisme rend une réponse à chaque tâche : la part sans réponse est nulle à chaque génération

- **Courses** : M et S, séparément ; deux parts, lues à deux moments.
- **Énoncé falsifiable** : à chaque génération notée, dans chaque part et chaque famille, le nombre de tâches sans
  réponse vaut 0. Les bornes par tâche de l'organisme (appels, délais, format de réponse) suffisent à rendre une classe
  pour chaque tâche.
- **Entrées** : (A-test) : nombre de tâches sans réponse par cellule de `test` (porté par le script actuel) ; signalement
  « impossible » si les réponses par tâche manquent. Relevé (B) : appels par statut. (A-final), à la fin du compteur : le
  libellé « aucune tâche sans réponse » ou « au moins une tâche sans réponse » par cellule de `test_final`, **si la version
  nouvelle du script l'écrit** ; jamais le nombre (CLB-04).
- **Si vraie** : zéro dans toutes les cellules de `test` ; libellé « aucune » dans toutes les cellules de `test_final`.
  **Si fausse** : au moins une cellule au-dessus de zéro, ou un libellé « au moins une ». Une part de 100 % sans réponse
  déclenche le critère 1 gelé du texte du second pilote (audit, R4), hors de cette boucle.
- **Test** : comptes de (A-test) ; statuts du relevé ; libellés de (A-final).
- **Seuil contre le bruit** : fait. **Tenue** (sur `test`) : zéro partout. **Éliminée** : au-dessus de zéro quelque part ;
  le nombre est rapporté pour `test`, sans jugement. **Indécidable (non observable)** sur `test_final` tant que le script
  n'écrit pas le libellé.
- **Moment** : fin de course pour `test` ; fin du compteur pour `test_final`.
- **Conséquence** : **éliminée** sur `test` → correction candidate, un facteur : le défaut de code ou la borne interne qui
  laisse une tâche sans réponse, identifié par les statuts d'appels ; la correction ne touche pas la règle qui choisit une
  classe (protocole, § 14). **Tenue** → rien. Le verdict sur `test_final`, à la fin du compteur, ne motive rien.
- **Ce que la question S y change** : rien d'attendu sur les réponses aux tâches.
- **Ce qu'elle ne dit pas** : rien sur la justesse des réponses ; rien sur la cause d'une absence, qui se lit dans les
  statuts.

### HC-P4-09 — La moisson est employée à chaque ronde de conception

- **Courses** : M et S, séparément.
- **Énoncé falsifiable** : chaque ronde de conception comporte un appel de formulation et au moins une recherche `OK`. Le
  noyau en sert jusqu'à six, et jusqu'à trois téléchargements, par ronde. Aucune génération notée ne fait plus de
  recherches que P4v3 ne le décrit.
- **Entrées** : relevé (B) : appels par rôle et par statut, par unité ; recherches et téléchargements par source, par
  unité si le relevé les sépare (sinon par course : « non observable » dès qu'il y a plus d'une ronde).
- **Si vraie** : par ronde, un appel de formulation et au moins une recherche `OK`. **Si fausse** : une ronde avec
  formulation et zéro recherche ; ou aucune recherche `OK` sur toute la course (critère 1 gelé du texte du second pilote :
  audit).
- **Test** : faits mécaniques du relevé.
- **Seuil contre le bruit** : fait. **Tenue** : chaque ronde a au moins une recherche `OK`. **Éliminée** : une ronde n'en a
  aucune. **Indécidable (non observable)** : les recherches ne sont comptées que par course, et il y a eu plus d'une ronde.
- **Moment** : fin de course.
- **Conséquence** : **éliminée** → défaut de code dans le chemin de formulation (un facteur) ; ou décision de conception à
  soumettre à Lazar (une conception sans moisson coûte moins et expose moins). **Tenue** → rien ; le nombre de recherches
  web est rapporté au devis de la ronde suivante.
- **Ce que la question S y change** : rien ; la question est servie après la conception.
- **Ce qu'elle ne dit pas** : rien sur l'apport des documents moissonnés à un score ; rien sur leur contenu, non lu.

### HC-P4-10 — La complexité ajoutée donne à la v6.2.1 une exactitude supérieure à celle de la v5.3 — déclarée « indécidable par ce pilote »

- **Courses** : aucune. La v5.3 ne court pas dans ce pilote (R-492). Et quand elle courait, la comparaison était interdite
  (texte v4, § Plan, points 3, 4 bis (iv), 4 et 5 ; P4C7-02).
- **Énoncé de la v1, gardé pour mémoire** : à la génération 3, sur `test_final`, l'exactitude de la v6.2.1 dépasse celle
  de la v5.3 d'au moins δ = 0,10 (Lazar, 01:48, sans aucun score).
- **Verdict** : « indécidable par ce pilote », sans calcul. Aucune fiche de ce registre ne nomme la v5.3 hors de
  celle-ci ; seul le point de symétrie avant (b) (protocole, § 8) la nomme encore. Aucune phrase ne met côte à côte les
  résultats des deux courses M et S non plus (même objet : rien à comparer sur la complexité).
- **Ce qu'il faudrait pour la trancher** : le pilote décisif (b), sur la banque v6 (lot 3), hypothèses écrites sans aucun
  score (`hypotheses-pilote-decisif-b-v1.md`, `903c6b51…`) : une seule mesure principale, δ = 0,10, deux sens, deux
  paliers de quatre graines par objet, ordre entrelacé, étalon de dérive, table de lecture écrite d'avance. Ce que la boucle
  produit (versions corrigées de la v6.2.1) y entre, ou non, selon la décision de Lazar sur la symétrie (protocole, § 8 ;
  CLB-10).
- **Conséquence** : aucune ronde de la boucle ne peut la tester.
- **Ce qu'elle ne dit pas** : tout. Elle est inscrite pour que personne ne la teste ici.

### HC-P4-11 — Hypothèse nulle, conscience d'évaluation : aucun changement au-delà du bruit des tâches entre la génération 0 et la génération 3 sur `test_final`

- **Courses** : M et S, séparément (un test par course).
- **Énoncé** : dans la course, sur les 36 tâches de `test_final` de la famille, les quatre générations notées ne changent
  pas l'exactitude simple au-delà du bruit des tâches. Mécanismes en jeu : mise à jour de la mémoire, retour arrière,
  mutation sur stagnation. Le test exact de McNemar apparié, génération 0 contre génération 3, bilatéral, n'est pas
  significatif après Holm.
- **Entrées** : (A-final) : cellule (iii) de la course et de la famille, avec son libellé ; signalement « impossible » si
  les réponses par tâche manquent ; le libellé du sens du rejet (« plus de tâches passées de fausse à juste que
  l'inverse », ou l'inverse, ou « autant »), **si la version nouvelle du script l'écrit** ; jamais b ni c (CLB-04).
- **Si elle n'est pas rejetée** : le libellé de la cellule n'est pas « changement au-delà du bruit des tâches ». **Si elle
  est rejetée** : il l'est ; le sens se lit sur le libellé du script, s'il existe, sans verbe de jugement. Ce changement
  peut tenir à la graine ((iv)).
- **Test** : point 4 bis (iii). Rapporté « impossible » si les réponses par tâche ne sont pas dans la liste fermée.
- **Seuil contre le bruit** : Holm au niveau 0,05 sur quatre tests (deux familles, deux courses), deux si la course S ne
  part pas. Verdicts : « **changement au-delà du bruit des tâches** » (nulle rejetée) ou « **non rejetée (bruit)** ». Ordre
  de grandeur (§ 0.5, illustratif) : un premier rejet demande au moins 8 discordances nettes dans le même sens, environ
  0,22 d'exactitude sur 36 tâches.
- **Moment** : fin du compteur, une seule fois (N-050). Aucun verdict provisoire.
- **Ce que son non-rejet implique** : seulement que, à cette graine et sur ces 36 tâches, les générations notées n'ont pas
  produit de changement de cet ordre. **Pas** que les mécanismes sont sans effet : la puissance est faible. **Pas** que la
  génération 3 vaut la génération 0.
- **Si elle est rejetée** : l'attribution à un mécanisme est « indécidable par ce pilote » (CLB-09) : elle demanderait de
  comparer des courses avec et sans le mécanisme, à plusieurs graines, sous un texte nouveau qui fixe test et seuil (comme
  le pilote décisif (b)). Les faits mécaniques de la course (mutation présente ou non ; restauration ; croissance de la
  mémoire) sont rapportés à côté, sans attribution. La « ronde d'isolement » de la v2 est retirée.
- **Conséquence** : aucune. Lue à la fin du compteur, cette fiche ne motive aucune ronde (§ 0.6). Tout verdict (iii),
  rejet ou non, reçoit le même audit (R4 ; CLB-14 : « trop propre » retiré) : contre-lecture à l'aveugle de la lecture
  finale (protocole, § 13).
- **Ce que la question S y change** : la course S a son propre test, dans la même famille de Holm ; la question ne change
  pas les tâches.
- **Ce qu'elle ne dit pas** : rien sur `test` ; rien sur la référence ; rien sur l'autre famille ; rien sur l'autre course
  (le couplage de Holm n'est pas une comparaison).

### HC-P4-12 — Hypothèse nulle, contrôle de délégation : aucun changement au-delà du bruit des tâches entre la génération 0 et la génération 3 sur `test_final`

- **Courses** : M et S, séparément.
- **Énoncé, entrées, test, seuil, moment, implications** : ceux de HC-P4-11, sur les 24 tâches de `test_final` de la
  famille. Ordre de grandeur (§ 0.5, illustratif) : un premier rejet demande au moins 8 discordances nettes, environ 0,33
  d'exactitude sur 24 tâches. À effet égal, la nulle y est plus difficile à rejeter qu'en conscience d'évaluation. La
  référence de contraste de paire (0,75 sur `test_final`) est rapportée à côté par le script, sans comparaison.
- **Ce que son non-rejet implique** : comme HC-P4-11.

## 2. Ordre d'application et règles des pièces de verdicts

0. Avant tout : la lecture est ouverte (décision transmise par conv-audit) ; la course est finie (liste fermée poussée,
   recherche des clés faite) ; le relevé (B) de la course existe, empreinté. Sinon, rien n'est lu (protocole, § 1).
1. L'analyste vérifie l'identité de l'objet et de la course : commit, arbre, nombre de fichiers, graine du manifeste,
   lanceur, noyau, banque, texte, question (protocole, § 9), sur le relevé (B). En cas d'écart : aucune lecture ; fait
   suspect (R4).
2. **À la fin de chaque course**, d'abord les fiches mécaniques : HC-P4-01, 03, 05, 06, 07 et 09 ; puis HC-P4-08 sur
   `test` ; le fait de HC-P4-04 (appels de mutation aux générations 2 et 3), rapporté sans verdict ; HC-P4-02 et HC-P4-10 :
   « indécidable par ce pilote », sans calcul. L'analyste vérifie que chaque cellule (ii) de `test` porte « non distinct
   de la référence » ou « impossible » (un « au-dessus » est un signal de défaut, R4).
3. **À la fin du compteur**, depuis (A-final) seule, par un agent distinct par course : HC-P4-11 et 12 ; HC-P4-08 sur
   `test_final` par libellé ; contrôle des cellules (ii) de `test_final`.
4. Un verdict se cite avec le champ ou la cellule qui le fonde : fichier et nom du champ ; la valeur recopiée pour un fait
   mécanique ou un compte de `test` ; les coordonnées et le libellé pour une cellule de `test_final`, jamais sa valeur.
   Aucun nombre n'est recalculé à la main.
5. Chaque course a sa propre pièce de verdicts (fin de course) et sa propre pièce de lecture finale. Une pièce de
   verdicts ne cite aucun nombre ni aucun verdict de l'autre course et ne porte pas son nom (garde G6).
6. La pièce de correction d'une ronde (une par ronde, après la dernière course de la ronde) cite, sous une section par
   course, les fiches et verdicts mécaniques qui motivent le facteur ; aucune ligne ne porte les deux noms de course ;
   aucune différence, aucune juxtaposition de scores ou de libellés ; une fiche aux verdicts différents selon la course
   reçoit le libellé du § 0.4 et ne motive rien.
7. Une hypothèse ajoutée après la lecture d'une course est marquée « écrite après la lecture de la course X » dans une
   version nouvelle de ce registre. Elle n'est jamais évaluée sur la course qui l'a inspirée.
8. Les fiches niées ou permutées dont se sert l'audit des agents (protocole, § 12) ne sont pas des hypothèses de ce
   registre. Elles ne reçoivent aucun verdict hors de l'audit. Aucun verdict d'élimination n'est transmissible avant
   l'étalonnage à blanc des agents (protocole, § 12.5 ; garde G10).

## 3. Ce que ce registre ne couvre pas, et pourquoi

- **L'écart entre `test` et `test_final`** (sondage du `test` par l'historique) : c'est le diagnostic direct du
  sur-ajustement adaptatif (fiche de lecture, § c). Mais c'est une différence calculée hors de la levée du point 4 bis :
  aucun agent ni aucun script de ce pilote ne la calcule. Les deux scores existent dans deux fichiers, lus à deux moments ;
  personne ne les soustrait. Un texte nouveau (pilote 5, tâches fraîches, N-049) peut en faire une mesure.
- **La variabilité entre graines** : une course par question. La décision de Lazar sur des graines de plus est pendante
  (02:05 ; tour R-491). Tout ce qui en dépend est « indécidable par ce pilote ». Les courses M et S ne sont pas une paire
  « A contre A » (questions différentes) et ne sont jamais comparées.
- **Toute comparaison** entre les deux courses, entre la v6.2.1 et la v5.3, la v6.1, la v6.2 de Gemini, la v6 du pilote 3,
  M, S ou le premier pilote : interdite (texte v4, § Plan, points 4 et 5 ; brouillon v5, table).
- **L'effet des corrections C-14 à C-17 sur un score** : interdit (texte v4, § Objet, dernier point).
- **Les sous-ensembles « catégorie absente du train »** : rapportés par le script, à côté, sans hypothèse (§ 0.5).
- **Les cellules (ii)** : rapportées pour mémoire, sans verdict (§ 0.2).
- **La dérive des modèles appelés** entre deux rondes : aucun dispositif dans ce pilote ; réserve permanente de la boucle.
- **La reprise par segments** : essayée en simulation (série v13) ; une course réelle n'en dit rien de général.
- **Les réponses aux questions M et S** : un matériau, pas une hypothèse de conception ; jamais lues par la boucle.
- **La boucle intérieure** (primitive d'expérience dans le noyau, R-471) : chantier séparé.
- **La stratégie de classement des organismes** : jamais écrite ici, ni comme hypothèse, ni comme correction.
- **Les choix C-14 et C-16** : décisions de programme, sans effet sous la configuration de ce pilote.
- **L'audit des agents** et l'étalonnage à blanc : dans le protocole (§ 12), pas ici.
- **La symétrie d'effort entre la v6.2.1 et la v5.3** avant (b) : point pour Lazar (protocole, § 8).

## 4. Table « v2 → v3 »

| fiche ou section | changement | raison |
|---|---|---|
| Statut, « Écrit avant tout score » | faits mécaniques de la course M lus dans le brouillon v5, déclarés ; aucune fiche changée pour eux | honnêteté (R4) ; LISEZMOI, écarts |
| § 0.1 | (A) séparée en (A-test) et (A-final) ; contenu réel de (A) d'après le LISEZMOI du script (nom par dossier, « sans réponse » porté, marqueur d'essai) ; (B) renvoyé à sa spécification, condition de démarrage ; (C) retiré des entrées de l'analyste | N-050 ; CLB-02 ; CLB-15 ; LISEZMOI du script |
| § 0.2 | calendrier provisoire retiré : (iii) lu une fois à la fin du compteur ; opération (2) non permise ; aucun nombre de `test_final` (sans réponse compris) ; libellés à demander ; « aucune autre différence calculée » rappelé ; « deux courses » à la place de « deux objets » | N-050 ; CLB-03 ; CLB-04 ; fait nouveau 1 |
| § 0.4 | « sans objet pour cette course » et « verdicts différents selon la course » ajoutés ; « non observable » étendu aux libellés absents du script | fait nouveau 1 ; choix déclaré |
| § 0.5 | seuils 0,01 et 0,03 déclarés point de conception a priori ; sous-ensembles : « trop larges pour rien séparer » | CLB-03 c ; CLB-16 d |
| § 0.6 | seuls les faits mécaniques motivent une correction pendant la boucle ; lecture finale ne motive rien ; attente chiffrée au journal | N-050 ; fait nouveau 4 |
| § 0.7 | un objet, deux courses (M, S) ; v5.3 retirée ; rondes de la boucle redéfinies (ronde 1 = M puis S) ; une correction par ronde | fait nouveau 1 ; choix déclaré |
| § 0.8 | moments d'ouverture : (A-test) et (B) à la fin de chaque course, (A-final) à la fin du compteur | N-050 |
| § 0.9 (nouveau) | ce que la question S change et ne change pas | fait nouveau 1 |
| HC-P4-01 | lecture par `rondes_tournees` quand le champ de déclaration manque ; cas 6 non observable ; « un seul facteur » soumis à la carte des facteurs ; verdicts différents selon la course | CLB-02 ; CLB-06 c ; CLB-17 a |
| HC-P4-02 | inchangée en substance ; cellules de `test_final` lues à la fin du compteur ; G7 sur `test` aussi | N-050 |
| HC-P4-03 | courses M et S ; empreinte de `politique_endogene.py` dite vraisemblablement absente | fait nouveau 1 ; CLB-02 |
| HC-P4-04 | déclarée « indécidable par ce pilote » ; fait rapporté sans verdict ; seuil 0,01 renvoyé à un point de conception a priori ; conséquence « tenue → correction » retirée | CLB-03 a et c |
| HC-P4-05 | réécrite en fiche mécanique (événement de restauration) ; condition sur les scores jamais calculée ; conséquence « tenue → correction du seuil » retirée | CLB-03 b et c |
| HC-P4-06 | courses M et S ; code retiré des entrées de l'analyste | fait nouveau 1 ; CLB-15 |
| HC-P4-07 | courses M et S ; « la course S ne part pas » | fait nouveau 1 |
| HC-P4-08 | deux parts à deux moments ; `test_final` par libellé seulement, à demander ; nombre de `test` recopiable | N-050 ; CLB-04 |
| HC-P4-09 | inchangée en substance ; courses M et S | fait nouveau 1 |
| HC-P4-10 | « aucune course » : la v5.3 ne court pas ; renvoi à (b) et au point de symétrie | fait nouveau 1 ; CLB-10 |
| HC-P4-11 | une seule lecture à la fin du compteur ; verdicts provisoires retirés ; b et c jamais recopiés, sens par libellé du script ; ronde d'isolement retirée (attribution indécidable) ; « trop propre » retiré, même audit pour tout verdict ; aucune conséquence | N-050 ; CLB-04 ; CLB-09 ; CLB-14 |
| HC-P4-12 | comme HC-P4-11 ; phrase sur le canal des paires retirée | CLB-18 |
| § 2 | ordre en deux moments (fin de course, fin du compteur) ; question dans l'identité ; règles de la pièce de correction (section par course, aucune ligne avec les deux noms) ; étalonnage à blanc avant toute élimination transmissible | N-050 ; CLB-05 ; CLB-06 ; fait nouveau 4 |
| § 3 | écart `test` − `test_final` : non calculé dans ce pilote (différence hors levée) ; réponses aux questions ; symétrie renvoyée au protocole | CLB-03 ; fait nouveau 1 ; CLB-10 |

## 5. Compléments à la table « v1 → v2 » de la v2 (CLB-17)

- HC-P4-01 : la v2 avait ajouté « les deux seuils 0,78 et 0,65, comptés comme un seul facteur », changement de substance
  non déclaré dans sa ligne « inchangée en substance » ; déclaré ici, et soumis à la carte des facteurs.
- § 2 de la v2 : l'ordre d'application avait été réécrit en trois groupes (mécaniques ; scores de `test` ; `test_final`),
  non dit dans la ligne « § 2 » de la table.
- Chemins : la v2 prenait des chemins relatifs à un « dossier de lecture » assemblé par conv-audit, à la place des
  « chemins relatifs à un dossier de course » du brief v1 ; non déclaré. Gardé en v3 (les agents n'ouvrent pas le dossier
  de course).
- Journal : la v2 tenait un journal unique pour les deux objets, non déclaré ; la v3 retire le journal du dossier de
  lecture (protocole, § 3 et § 5).
