# Contre-lecture 6, courte, du préenregistrement du quatrième pilote descriptif (`pilote4-gemini-organisme-v4.md`) : l'écart depuis la contre-lecture 5 — v1

## En-tête

- **Textes relus**, empreintes vérifiées sur disque par `sha256sum` avant toute lecture :
  - version à sceller : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v4.md`,
    `51752266ba21b72fe2ee4c8b8e4157581bcfeed82bd2790e1632482a7746fc34` (469 lignes ; empreinte attendue au brief) ; sa
    copie `pieces-pilote4-gemini/contre-lecture-6-v1/pilote4-gemini-organisme-v4-lu-par-cl6-51752266.md` a la même
    empreinte, et le texte n'a pas changé pendant ma relecture (revérifié à 01:46 et 01:51 UTC) ;
  - version lue par la contre-lecture 5 : `pieces-pilote4-gemini/contre-lecture-5-v1/pilote4-gemini-organisme-v4-lu-par-cl5-efb13feb.md`,
    `efb13feb34f66d9652a194564c0bc9eced2889cbb6305c8dac9e97766246b60e` (323 lignes ; attendue) ;
  - rapport de la contre-lecture 5 : `prereg/contre-lectures/pilote4-gemini-organisme-v4-cl5.md`,
    `914ac3fbf6b2ba0760ef3dace4dd8c3768909809e441ec0f63e5407c2d138240` (attendue ; compagnon juste ; identique à sa copie
    dans `contre-lecture-5-v1/`) ;
  - relevé des mots de Lazar v5 : `objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v5.md`, `c5fe2092…` (compagnon juste ;
    égale à l'entrée de la liste v7) ; v3 `757f30a3…` (attendue) ; v1 `6350ca87…`, v2 `96da3945…`, v4 `7e0837e6…` ;
  - synthèse du collisionneur : `canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/synthese-collisionneur-lecture-pilote-conv-audit-v1.md`,
    `a8e1ed64…` (attendue) ;
  - liste des pièces v7 : `pieces-pilote4-gemini/EMPREINTES-pieces-pilote4-v7.txt`, `220768458e7a6778…` (attendue ;
    compagnon juste) ;
  - au besoin : P4v3 `pilote4-gemini-organisme-v3.md`, `de7a5559…` ; lanceur v10 `0203f546…` ; script de scellement v4
    `6094f21a…` ; T2 `pilote2-gemini-organisme-v5-2-v2.md`, `d2944654…` (cité par P4v3) ; lanceur v6 `50f9c496…` (six
    lignes) ; rapports des contre-lectures 1 à 4 (`3dd09acb…`, `7c625fa6…`, `0d95ea8c…`, `e2de1372…`, empreintes et
    compagnons seulement).
- **Contre-lecteur** : sous-agent neuf (`claude-opus-5-5`), lancé par conv-audit le 26 octobre 2026. Je n'ai écrit ni ce
  texte, ni ses versions précédentes, ni ses pièces, ni la contre-lecture 5.
- **Heures** (lues sur `date -u`) : début 01:29:47 UTC ; ce rapport est écrit à partir de 01:51:09 UTC (heure lue juste
  avant).
- **Interruption déclarée à tort.** `pieces-pilote4-gemini/contre-lecture-6-v1/LISEZMOI-interruption-v1.md`
  (`56877a09…`, écrit à 01:44:35 UTC, pendant ma relecture) dit cette contre-lecture « interrompue avant tout rapport »
  et « à relancer ». Il s'agit de la présente instance (lancée vers 01:29 UTC ; les fichiers de travail qu'il décrit sont
  les miens) : elle n'a pas été interrompue, et voici son rapport (suite à donner : P4C6-08 a).

## Lu, exécuté, non lu

- **Lu en entier** : le brief ; la version à sceller ; le `diff` complet des deux versions (23 passages ; tout le reste
  est identique, donc lu) ; le rapport de la contre-lecture 5 ; le relevé v5 ; les `diff` v1→v2, v2→v3, v3→v5, v4→v5 du
  relevé ; la synthèse du collisionneur ; `sceller_pilote4_v4.py` ; le `LISEZMOI-interruption-v1.md`.
- **Lu en partie** : P4v3 l. 341–434 et, par `grep`, l. 104, 239–240, 361, 449–460 ; T2 l. 440–521 (fermeture, liste
  fermée, lecture, critères gelés) ; lanceur v10 l. 176–190, 318–330, 495–560 ; lanceur v6, l. 206, 256, 504, 512, 804, 821
  (comparées au v10) ; la liste v7 (noms et empreintes) et la v6 (comparaison) ; dans `simulation-lanceur-v10/`, les
  journaux d'appels de simulation, par mon code, champs `statut` et `role` seulement (aucun champ de score n'y existe).
- **Exécuté** (sorties sous `/var/tmp/contre-lecture-pilote4-v6/` seulement) : `date -u` ; `sha256sum` des textes et
  pièces cités ; `sha256sum -c` de la liste v7 depuis `pieces-pilote4-gemini/`, **après** contrôle de ses noms (aucun
  `-cle.json`, `-secret.json`, `donnees/`, `runs/`, `diag/`, `ferme.tar.gz`, `reponse-question`, `P3-consignes`,
  `textes-actions` ; les seuls `journal-appels`/`extrait-mecanique` sont des pièces de simulation) : **621 sur 621 justes**
  (`sha256sum-c-EMPREINTES-pieces-pilote4-v7.txt`) ; `sha256sum -c` des compagnons (liste v7, relevés v1 à v5, rapports 1
  à 5) ; `diff` ; `grep` sur des fichiers nommés ; `ls` de dossiers nommés (sans récursion) ; mon propre code, en lecture
  seule, par `/opt/venv-essaim-sim-v1/bin/python -I` : `outils/controle_scellement_cl6_v1.py` (gardes du script v4 et
  lecture du lanceur, transcrites, sur le texte et sur une copie remplie en mémoire de valeurs d'essai ; comparaison des
  listes v6 et v7 ; comptes d'appels des journaux de simulation) → `releves/controle-scellement-cl6-v1.txt` ;
  `outils/chaine_grep_cl6_v1.sh` (chaîne de `grep` du lanceur v10, l. 539–552, sur mes copies de la ligne de GO et des
  lignes de dépense, `essai-lignes/`) → `releves/chaine-grep-cl6-v1.txt`. Deux copies triées des listes v6 et v7
  (fichiers de travail, tri impropre à `comm`) ont été écrites puis effacées, remplacées par la comparaison par chemin ;
  l'outil a gardé lui-même hors de ce dossier deux sorties longues (le `diff` et cette comparaison), sans contenu interdit.
- **Rien exécuté** du lanceur, des batteries, du script de scellement, du script de vérification, du script de relevé ni
  du code d'un organisme. Aucun `git`, aucun sous-agent, aucune recherche récursive.
- **Non lu ni ouvert** : aucun fichier `-cle.json` ni `-secret.json` (il n'y en a aucun dans la liste v7, vérifié avant
  `sha256sum -c`) ; aucun dossier `donnees/`, `runs/`, `diag/` ; aucune archive `ferme.tar.gz` ; aucun fichier
  `reponse-question*`, `journal-appels*`, `extrait-mecanique*` d'un pilote réel ; `cles-avant-poussee-v621-v1.txt` et
  `faits-pilote3-v1/*.json` hachés seulement ; aucun score. Non vérifiable sans `git` ni lecture de `main` : les lignes
  R-445 à R-472 (`3c94802`), la branche `7ac475b`, les messages n° 55 et 56.

## Verdict

**Scellable après corrections mineures.** L'écart (23 blocs de `diff`, liste à la fin) est celui qu'annoncent le statut et le
§ Contre-lecture, à un retrait près (« critères gelés », P4C6-01). Les huit constats de la contre-lecture 5 sont traités
comme le texte le dit ; « sans objet » et le refus sur l'en-tête du script sont justifiés. Les pièces annoncées existent :
la liste v7 passe `sha256sum -c` (621 sur 621), ne porte aucune entrée interdite, ne change ni ne perd aucune des 502
entrées de la v6 et couvre tout le dossier des pièces tel qu'il était à son écriture ; le relevé v5 reprend la v3, et chaque
version la précédente, sans ôter ni changer une ligne. Les décisions de Lazar de 01:48 à 02:17 sont rendues fidèlement dans
leurs mots, et le départ des courses n'en dépend pas (noyau `8e5e2f7b`, lanceur v10, ligne de GO et lignes de dépense
inchangés). Le script v4 acceptera le texte et le lanceur le lira comme il l'attend ; la ligne de GO et les lignes de
dépense passent la chaîne de `grep`, et les artefacts sont refusés.

Trois constats mineurs, de texte seul : le point 4 bis fait ce que les règles de lecture gardées par renvoi interdisent,
sans que la levée soit écrite (P4C6-01) ; « aucun score n'est lu tant qu'une course tourne » admet deux lectures, dont
l'une contredit « dès la fin de chaque course » et la boucle extérieure (P4C6-02) ; « les hypothèses de (b) sont déjà
fixées » n'est ancré dans aucune pièce, alors que le point 3 ouvre les scores à leurs auteurs dès la fin de la v6.2
(P4C6-03). Cinq remarques, une conformité.

## Constats

### P4C6-01 — mineur — Le point 4 bis compare un score à une référence, et deux générations entre elles, contre les règles de lecture que le texte garde ; la levée n'est pas écrite, et « critères gelés » a disparu sans mention

- **Fait, texte.** Point 4 bis (l. 328–341) : (ii) « au-dessus de la référence, au-delà du bruit des tâches » si la borne
  basse « dépasse la référence », sinon « non distinct de la référence » ; (iii) la génération 0 contre la génération 3
  sur `test_final`, test apparié, Holm au niveau 0,05 : « changement au-delà du bruit des tâches » ou non ; (iv) « dans
  le bruit ». Point 4 (l. 342) : « **Lecture** […] : ceux de P4v3 ». « Tout le reste de P4v3 vaut tel quel » (l. 176–182),
  dont l'énumération, par rapport à la version de la contre-lecture 5 (l. 129–130), a perdu « critères gelés ».
- **Fait, P4v3 et T2.** P4v3, § Hypothèse (l. 343) : « aucun seuil de lecture » ; § Plan, point 4 (l. 415–417) : les
  références se lisent « rapporter à côté, sans comparaison », car « les critères gelés de T2 (l. 518–520) n'admettent
  aucun verbe de comparaison entre un score et une référence » ; § Critères de lecture gelés (l. 427–433) : ceux de T2.
  T2 (l. 518–520), lectures interdites : « tout verbe de comparaison (« bat », « dépasse », « reste sous », « fait mieux /
  moins bien ») entre un score et une référence, un autre score, 0,5, l'autre course ou le premier pilote ; tout adjectif
  sur un score ; toute différence calculée ».
- **Portée.** Les libellés (ii) à (iv) sont des lectures que T2 interdit, et posent un seuil de lecture que P4v3 exclut ;
  le texte garde ces règles par renvoi et ne dit nulle part qu'il les lève. Seule la clause générale « en cas de conflit,
  ce texte prévaut » (l. 22) tranche, implicitement ; le rédacteur du rapport et l'analyste de la boucle extérieure
  trouvent deux règles contraires. La levée est dans l'esprit des décisions de 01:54 (option (a)) et de 01:56 : elle doit
  être écrite. Le retrait de « critères gelés » est le seul changement que l'écart n'annonce pas (tâche 3).
- **Correction** (texte seul). Au point 4 bis : « Pour ce pilote (décisions de Lazar de 01:54 et 01:56), ces libellés, et
  eux seuls, lèvent, pour les comparaisons qu'ils nomment (un score et la référence de sa famille et de sa part ; les
  générations 0 et 3 d'une même course), l'interdit des critères gelés de T2 (l. 518–520), la lecture « à côté, sans
  comparaison » de P4v3 (§ Plan, point 4) et « aucun seuil de lecture » (§ Hypothèse) ; le reste de ces critères vaut :
  aucune comparaison entre objets, ni avec l'autre course, 0,5 ou le premier pilote, aucun adjectif, aucune autre
  différence calculée. » Rétablir, dans « Tout le reste » : « critères gelés (sauf ce que lève le point 4 bis) ». Dire
  enfin si les verdicts des agents par hypothèse (« éliminée, tenue, indécidable dans le bruit », l. 125–126) relèvent du
  rapport de lecture et de ces critères, ou sont des pièces à part, exploratoires (l. 131–134, 327).

### P4C6-02 — mineur — « Aucun score n'est lu tant qu'une course tourne » : lu « aucune course », il interdit de lire la v6.2 pendant la v5.3, contre « dès la fin de chaque course » et la boucle extérieure ; et le point 3 « remplace » celui de P4v3 tout en en gardant une partie

- **Fait.** Point 3 (l. 314–317) : « **dès la fin de chaque course** […], ses scores peuvent être lus […]. Pendant une
  course et entre ses segments, les interdits de lecture de P4v3 restent : aucun score n'est lu tant qu'une course
  tourne. » 02:17 (l. 123–126) : « à la fin de chaque course de ce pilote, des agents neufs […] exécutent la lecture des
  points 3 et 4 bis ». R-445 (relevé v5, l. 40 ; texte l. 64–66) : session-depot lance « segment après segment, sans
  attendre un autre mot » : la v5.3 part dès que la porte « v6.2 précédente » l'admet. Canal (d) (l. 283) : « pendant
  qu'une course tourne ». Le point 3 « remplace le point 3 de P4v3 » (l. 314 ; table, l. 168), mais garde « les interdits
  de lecture de P4v3 » (l. 317), et « Tout le reste » garde les « canaux dits et acceptés pendant les courses » (l. 180) :
  deux parties du point 3 de P4v3 (l. 391–397 et 397–409).
- **Portée.** Lu « aucun score, d'aucune course, tant qu'une course quelconque tourne », la lecture de la v6.2 — et la
  boucle extérieure — attend la fin de la v5.3 ; lu « aucun score d'une course tant qu'elle tourne », elle se fait pendant
  la v5.3. Deux actes différents ; la première lecture contredit « dès la fin de chaque course » et 02:17.
- **Correction.** « Aucun score d'une course n'est lu tant qu'elle tourne, entre ses segments compris ; ceux de la v6.2
  peuvent être lus dès sa fin, pendant la v5.3, qui part et tourne telle quelle (aucune de ses gardes ne lit un score). »
  Même précision au canal (d) (l. 283). Au point 3 et dans la table (l. 168) : « remplace le moment de lecture et les
  conditions (i) et (ii) du point 3 de P4v3 ; en garde ce que session-depot consulte pendant et entre les segments
  (P4v3 l. 391–397) et les canaux dits et acceptés (l. 397–409) ».

### P4C6-03 — mineur — « Les hypothèses de (b) sont déjà fixées sans aucun score de ce pilote » : rien ne l'ancre, la synthèse en laisse une partie ouverte, et le point 3 ouvre ces scores à leurs auteurs dès la fin de la v6.2

- **Fait.** Point 3 (l. 321–323) : « Les hypothèses de (b) sont déjà fixées sans aucun score de ce pilote (direction donnée
  par la question de 00:49, δ = 0,10, deux paliers ; § Décisions, 01:48) » ; de même l. 94–95 et 107–108. Relevé v5,
  01:48 (l. 24) : « je recommande de les écrire maintenant, sans aucun score du pilote 4 […] : go ». Synthèse : l. 14–15,
  H_A « la v6.2.1 bat la v5.3 d'au moins δ » contre H_B « Δ ≤ 0 » ; mais l. 44–45, laissé ouvert : « Hypothèse à un sens
  […] ou symétrique, supériorité et équivalence […] : selon ce que Lazar entend par « viser un signe » (R3) » ; l. 63–64 :
  le plan à deux paliers est « 4 graines par objet », puis « +4 graines par objet seulement si l'issue est indéterminée »,
  les 4 comptant les deux courses de ce pilote (l. 36–37), que 01:52 exclut. Point 3 (l. 318) : « Lisent : conv-audit et
  Lazar ». Aucun texte de (b) n'est cité (ni chemin, ni empreinte). Le § Décisions (l. 83–85) décrit encore (b) à « trois
  graines par objet » (00:54).
- **Portée.** La propriété décidée à 01:48 n'est tenue que si les hypothèses de (b) sont écrites avant que leurs auteurs
  — conv-audit, qui les a recommandées — lisent un score de ce pilote ; or le point 3 leur ouvre ces scores dès la fin de
  la première course, et ce qui reste à trancher (forme de l'hypothèse ; taille de (b) sans les courses de ce pilote)
  n'est fixé nulle part. « Déjà fixées » dit plus que les pièces ne montrent.
- **Correction.** Au point 3 : « Les hypothèses de (b) sont écrites et poussées, avec leur empreinte, avant que leurs
  auteurs lisent un score de ce pilote, au plus tard à la fin de sa première course (comme le registre d'hypothèses de
  02:17) ; elles reprennent de 01:48 la direction (question de 00:49), δ = 0,10, les deux paliers, et de 01:52 la banque
  v6 ; ce que la synthèse laisse ouvert (hypothèse à un sens ou symétrique, course nulle) y est tranché sans score de ce
  pilote, ou par Lazar. » Au § Décisions (l. 83–85), remplacer « trois graines par objet » par « taille fixée par le
  texte de (b) (deux paliers, 01:48 ; sans les courses de ce pilote, 01:52) ».

### P4C6-04 — remarque — R-472 est lu mais non rendu : session-depot tient la levée de 01:56 pour sans effet sur ses textes tant que Lazar ne la lui a pas dite

- **Fait.** Texte, l. 35 : R-445 à R-472 lus. Relevé v5, l. 49 (R-472) : la levée « ne lui a pas été dite par Lazar dans sa
  session : « sans effet sur mes textes tant qu'il ne me l'a pas dit » ». Point 3 (l. 318–321) : session-depot, « qui écrit
  l'étape 1 », écrit en réserve ce qu'il lit ; les expériences de confirmation, dont « l'étape 1 décisive », se font sur la
  banque v6.
- **Portée.** Rien du départ n'en dépend (session-depot lance un texte encore scellé, comme R-445 le demande ; aucune garde
  ne lit de score). Mais le texte énonce, au nom d'une décision dont session-depot dit n'avoir pas reçu le mot, des
  obligations pour ses textes : une divergence entre lignées, à déclarer.
- **Correction.** Une phrase au § Décisions (01:56) et au point 3 : « Session-depot (R-472) ne l'applique à ses textes
  qu'après le mot de Lazar dans sa session ; ce que le point 3 dit de l'étape 1 vaut dès ce mot ; ce texte ne règle que la
  lecture de ce pilote. » Pour la prochaine version du relevé, non pour ce texte : l'en-tête de sa section session-depot
  (l. 36) cite `4a4d9ca`, alors que R-466 à R-472 viennent de `3c94802` (l. 4) ; citer les deux.

### P4C6-05 — remarque — Point 4 bis : calculable, ne compare jamais les deux objets, mais cinq choix à fixer avant toute lecture

- **Calculable, et sans comparaison entre objets** (tâche 2, conforme). D'après P4v3 et T2, les réponses par tâche de
  chaque génération sont dans l'archive fermée `ferme.tar.gz`, l'un des fichiers de la « liste fermée par noms » poussée à
  la fin de chaque course (T2 l. 451–465) ; `test` et `test_final` sont notés à chaque génération (T2 l. 483–484 : « famille
  × génération × {score `test`, score `test_final`, … } ») ; le script de lecture recalcule déjà des comptes et des classes
  par tâche « depuis le secret de la banque v3 » (P4v3 l. 412–420). (i) à (iii) sont donc calculables à partir de ces
  pièces ; (iv) ne calcule rien ; aucune comparaison entre les deux objets (l. 339–341, 342–344).
- **À fixer.** (a) « intervalle de Wilson de chaque classe, combinés pour l'exactitude équilibrée » (l. 331–332) : la
  combinaison n'est pas dite (par exemple, la moyenne des bornes des deux classes). (b) « la référence de la famille et de
  la part » (l. 333–334) : la conscience d'évaluation en a deux, surface et provenance (plus l'oracle de catégorie, P4v3
  l. 410–412) : leur maximum (règle de la banque que P4v3 cite, l. 415–416), ou chacune ? (c) (i) et (ii) demandent les
  comptes par classe à chaque génération, donc les réponses par tâche et le secret : le même repli que (iii) (« rapporté
  impossible », l. 338), ou dire d'où ils viennent. (d) (ii) porte jusqu'à 32 comparaisons (deux courses, deux familles,
  deux parts, quatre générations) sans correction de multiplicité, à la différence de (iii) : le dire (« sans correction,
  exploratoire ») ; « quatre tests en tout » (l. 337) : « au plus quatre » (deux si la v5.3 ne part pas). (e) Le script de
  lecture du point 4 (P4v3 l. 417–420 : écrit, empreinté, essayé avant le moment de lecture, sur un cas sain et sur un
  artefact) doit calculer aussi le point 4 bis ; il lit le secret de la banque, alors que les agents « ne lisent ni […]
  vérités, ni fichiers de clé » (l. 326) : dire qui l'exécute, et qu'ils n'en voient que la sortie.

### P4C6-06 — remarque — Servir des scores de `test` à Gemini ou à un organisme : c'est la lecture, par conv-audit, de « pour corriger l'organisme » ; à attribuer

- **Fait.** Point 3 (l. 323–324) : « Les scores de `test_final` ne sont servis ni à Gemini ni à aucun organisme ; ceux de
  `test` et les faits mécaniques peuvent l'être après la fin d'une course, pour corriger un organisme. » Relevé v5, 01:56
  (l. 29) : « les scores des pilotes peuvent être **lus** dès la fin d'une course, pour corriger l'organisme ». P4v3, liste
  d'arrêt (l. 460) : avant le moment de lecture, aucune pièce fermée (« archive, mémoire, réponses aux tâches, réponse à la
  question, score ») n'est servie à Gemini ; « seuls des faits mécaniques de l'extrait peuvent l'être, si Lazar en décide ;
  jamais un score de `test_final` ».
- **Portée.** Transposée au moment nouveau, la règle tient avec P4v3 ; mais « servis » va au-delà du « lus » de Lazar et
  n'est pas dit comme une lecture de conv-audit ; les autres pièces fermées de P4v3 l. 460 ne sont pas traitées.
- **Correction.** « … peuvent l'être après la fin d'une course, sur décision de Lazar (lecture, par conv-audit, de « pour
  corriger l'organisme », 01:56) ; les autres pièces fermées (P4v3 l. 460) ne sont servies que sur décision de Lazar ;
  jamais `test_final`. »

### P4C6-07 — remarque — Traitement des constats de la contre-lecture 5 : trois descriptions inexactes (le texte opératoire est juste)

- (a) P4C5-07 (b) : « le point 8 de P4v3 » (l. 453) ; le corps dit juste « le point 8 de la v6.2 » (l. 227), comme la
  contre-lecture 5 ; P4v3 ne numérote aucun point 8 (il parle des « points ouverts de la demande de v6.2 », l. 361). Écrire
  « le point 8 de la demande de v6.2 ».
- (b) P4C5-05 (d) : « déclaré comme lacune au § Essais, à combler par le prochain lanceur » (l. 448) ; le § Essais
  (l. 389–391) dit seulement « même lacune que P4v3 pour la v6.1, dite ». Aligner l'un sur l'autre.
- (c) P4C5-04 (c) : « écrits comme points ouverts dans la table » (l. 444), alors que la table dit « aucun point ouvert
  n'est à accepter » et nomme ces choix « deux choix restent à Lazar » (l. 160). Écrire « écrits dans la table comme choix
  restant à Lazar, sans effet sur le départ ».
- (d) P4C5-07 (c) : le refus de corriger l'en-tête du script est justifié (script l. 84–88 : l'enfant 0 remplit
  `<<GRAINE_V53>>`, l'enfant 1 `<<GRAINE_V6X>>` ; point 2, l. 310) ; la docstring porte la même inexactitude à sa
  première ligne (« v5.3 puis v6.x »), sans plus d'effet.

### P4C6-08 — remarque — Après cette contre-lecture : l'interruption déclarée à tort, la phrase « rien d'autre », les gardes du script

- (a) `LISEZMOI-interruption-v1.md` (`56877a09…`) dit qu'aucun rapport n'a été écrit : faux pour cette instance, qui a
  fini. Le garder (R12) et verser à côté une note qui le corrige (heures et empreinte de ce rapport). Si une autre
  instance relit malgré tout le texte, son rapport doit porter un nom distinct **et permis** :
  `pilote4-gemini-organisme-v4-cl7.md` ; un nom comme `…-cl6b.md` ne serait pas compté par le script comme contre-lecture
  du texte (motif `-cl[0-9]+\.md`, l. 70) et ferait refuser la copie de lancement par le lanceur (`PERMIS_APRES_CODE`,
  l. 183, appliqué l. 459).
- (b) Le dernier alinéa (l. 465–469) dit que le texte scellé ne porte, en plus de la version relue, que la ligne de la
  contre-lecture 6, « le traitement de ses constats » et les champs du script : « rien d'autre ». Les corrections que
  demandent P4C6-01 à P4C6-03 touchent le corps : écrire « et les corrections qu'il demande, aux passages qu'il nomme »,
  sinon le texte scellé contredit cette phrase.
- (c) La ligne de la contre-lecture 6 et le traitement ne doivent porter ni « entropie E = », ni « graine de la course …
  = », ni marqueur `<<…>>`, ni `[[…]]` (script l. 35–58 ; lanceur l. 502 et 504) ; le compagnon de ce rapport est au
  format « empreinte, deux espaces, nom », nom nu, comme le script le lit (l. 63–67).
- (d) `contre-lecture-6-v1/` (créé à 01:44:35 UTC) n'est pas dans la liste v7 (écrite à 01:28:52 UTC) : la phrase « la v7
  […] couvre toutes les pièces avant elle » (l. 410) est juste. Le fichier d'empreintes v2, écrit par le script (l. 77–80 :
  toutes les pièces sous le dossier), couvrira ce que conv-audit y versera (brief, ce rapport et son compagnon, `outils/`,
  `releves/`, `essai-lignes/`, la sortie de `sha256sum -c`) ; il n'existe pas encore, sans quoi le script refuserait
  (l. 74–76).

### P4C6-09 — conforme — Ce que j'ai trouvé conforme

- **Pièces** (tâche 3 bis). Liste v7 : 621 lignes au format « empreinte, deux espaces, nom », **621 sur 621 justes** ; aucun
  nom interdit. Par rapport à la v6 donnée à la contre-lecture 5 (`d010123d…`, 502 entrées, compagnon juste) : aucune
  entrée ôtée ni changée ; 119 nouvelles, exactement celles qu'annonce le texte : la liste v6 et son compagnon,
  `contre-lecture-5-v1/` (45 : brief `brief-contre-lecture-5-v2.md`, rapport et compagnon, relevés — écarts, essais de
  lignes et de scellement, outils, redérivations —, copie du texte relu : ce que dit le § Contre-lecture, l. 430–431),
  `simulation-lanceur-v10/` (64 : `LANCEMENT`, extraits, journaux et listes `A-POUSSER` des quatre cas sains, aucune
  `ferme.tar.gz`), `releves-serie-v11-v1/` (le relevé v2 jamais servi et son compagnon), les relevés v3 à v5 et leurs
  compagnons. Elle couvre tout ce que portaient, à son écriture, le premier niveau du dossier des pièces et les dossiers
  nouveaux (`ls` des dossiers nommés), sauf elle-même et son compagnon ; elle porte les listes v1 à v6.
- **Relevé.** v5 = v4 + la ligne de 02:17 ; v3 → v5 : aucune ligne ôtée ni changée hors titre et phrase d'en-tête (ajouts
  après l. 30 et 39) ; de même v1 → v2 et v2 → v3 ; les empreintes que la phrase d'en-tête cite (`6350ca87…`, `96da3945…`,
  `757f30a3…`, `7e0837e6…`) sont justes. La v4 porte une heure de modification postérieure de 14 s à celle de la v5
  (01:24:51 contre 01:24:37 UTC), mais son contenu est celui que la v5 cite.
- **Constats de la contre-lecture 5** (tâche 1). P4C5-01 : sans objet, sans reste de la règle des options (2) et (2')
  (l. 85–97, 105–106, 168, 314). P4C5-02 : table l. 170 et 171, liste d'arrêt l. 355 ; le filtre cité (lanceur l. 325,
  `not g.get("phase")`) existe ; `v62-plafond-total` est dans la série v13. P4C5-03 : l. 281–284. P4C5-04 : (a) tranchée à
  01:48 Paris (00:48 UTC, après 23:56 UTC) ; (b) l. 303–304 ; (c) l. 160. P4C5-05 : (a) l. 368–369 ; (b) l. 172, les six
  paires de lignes citées sont identiques dans les lanceurs v6 et v10 ; (c) l. 357 ; (d) l. 389–391. P4C5-06 : (a) versées,
  et les journaux versés donnent exactement les nombres du § Essais (v6.2.1 : c001 7 dont 1 mutation, g000 123, g001 129,
  g002 123, g003 124 dont 1 ; v5.3 : 6, 123, 129, 123, 123 ; mêmes nombres en deux et trois segments ; tous `OK`) ;
  (b) versé ; (c) l. 238–244, conforme à ce que la contre-lecture 5 a relevé dans le journal (que je n'ai pas relu). P4C5-07 : (a) l. 213–214 ; (b) l. 227 ;
  (c) refus justifié ; (d) l. 304–306, et `PERMIS_APRES_CODE` (l. 183) permet le texte, ses pièces et les rapports
  `pilote4-gemini-organisme-vN-clN.md`, dont celui-ci. Aucune de ces corrections n'introduit de contradiction (la précision
  du canal (d) entre dans P4C6-02).
- **Décisions** (tâche 2). Citations fidèles au relevé, fautes de frappe corrigées : 01:48 et 01:52 (l. 91–97), 01:54 à
  01:56 (l. 98–109), 02:05 à 02:17 (l. 110–134) ; heures de Paris = UTC + 1, cohérentes : R-466 vers 01:03 UTC, après la
  demande de 01:56 Paris ; R-471 vers 01:09 UTC, avant le compte rendu collé à 02:10 Paris ; 02:17 Paris = 01:17 UTC, avant
  le relevé v5 (01:24 UTC) et le texte (01:28 UTC). (3+), banque v6, aucune course versée, options (2) et (2') disparues :
  dits (l. 94–96). 01:56 : levée pour les pilotes de conception sur la v3, relecture gardée, lecture dès la fin de chaque
  course, confirmations sur la v6 avec réserve, « relecture puis départ » : dits, et ce qui est remplacé (fermeture « pour
  tout usage », point 3 de P4v3, question de 20:54 UTC, l. 96–97, 105–106, 137–138, 168) est nommé partout de la même façon.
  02:05 : décision pendante, une course par objet, graines de plus seulement par un texte et un GO nouveaux. 02:06 à 02:17 :
  boucle extérieure retenue, telle que le relevé la décrit ; boucle intérieure tranchée par R-471, dont le texte ne dépend
  en rien (« aucun pilote scellé n'est modifié : la primitive entre par une version nouvelle » ; noyau `8e5e2f7b`, lanceur
  v10 inchangés ; pièces de la boucle sur le canal, hors de la branche du lancement). Le résumé de la synthèse (l. 89–90)
  est fidèle à ses points 1 et 2.
- **Scellement et lanceur** (tâche 4 ; `releves/controle-scellement-cl6-v1.txt`). Une seule ligne « entropie E = »
  (l. 307), sans nombre ; deux lignes « graine de la course … = » (l. 312–313), celles des marqueurs, sans espace final ;
  `<<ENTROPIE>>`, `<<GRAINE_V53>>`, `<<GRAINE_V6X>>`, `<<EMPREINTE_PIECES>>` une fois chacun, et aucun autre `<<` ; aucun
  `[[`. Remplie en mémoire de valeurs d'essai : gardes du script après remplissage justes ; lecture du lanceur (l. 501–504,
  509) comme il l'attend ; empreinte pleine du lanceur citée. Ligne de GO et lignes de dépense, inchangées depuis la
  contre-lecture 5 (`releves/chaine-grep-cl6-v1.txt`) : acceptées pour la v6.2 et la v5.3, aux segments 1 et 2 ; refusées
  sans la clause de la v6.2.1, pour un segment non consigné et pour une empreinte de la v6.2 fausse.

## L'écart : passages modifiés (tâche 3)

Numéros de lignes de la version à sceller ; « CL5 » renvoie au traitement de ses constats.

| passage (lignes) | changement | raison annoncée |
|---|---|---|
| statut (4) | décisions « de 23:54 à 02:17 » | décisions |
| statut (7–11) | heures de correction et de complément ; « pilote de conception » | décisions de 01:56 |
| statut (15–17) | contre-lectures 1 à 6, au lieu d'un marqueur | § Contre-lecture |
| ce qui a été lu (35–43) | R-445 à R-472 (`3c94802`), brouillon de la primitive, messages n° 55 et 56, compte rendu de 02:10, brouillon de l'étape 2, neuf réponses du collisionneur | suite des décisions (non nommé dans l'énumération de la l. 461) |
| décisions (51) | relevé v5 | décisions |
| décisions (85–134) | 00:54–00:55 réécrit ; 01:48, 01:52, 01:54–01:56, 02:05–02:17 | décisions |
| décisions (137–138) | question de 20:54 UTC sans objet pour ce pilote | décisions de 01:56 |
| table (160) | choix restant à Lazar, constats non bloquants, R-448 | CL5 : P4C5-04 (c) |
| table (168) | moment de lecture | décisions de 01:56 |
| table (170–172) | devis, ronde de la v6.2 hors `OK`, décalages de lignes | CL5 : P4C5-02, P4C5-05 (b) |
| tout le reste (180–182) | canaux « pendant les courses », règles de lecture, moment ; **« critères gelés » retiré** | décisions de 01:56 ; le retrait n'est pas annoncé (P4C6-01) |
| objet, C-14 (213–214) | « dès deux castes, la délibération s'ouvre » | CL5 : P4C5-07 (a) |
| objet, C-17 (227) | point 8 de la v6.2 gardé | CL5 : P4C5-07 (b) |
| objet, essais (238–242) | causes de `v621-a` et `v621-b` | CL5 : P4C5-06 (c) |
| objet, canal (d) (281–284) | `LANCEMENT.md` de la v5.3 ; lecture dès la fin de chaque course | CL5 : P4C5-03 ; décisions |
| plan, point 1 (303–306) | recopie mot pour mot ; tête de la branche | CL5 : P4C5-04 (b), P4C5-07 (d) |
| plan, points 3 et 4 bis (314–341) | moment et règles de lecture ; lecture contre le bruit | décisions de 01:54 à 02:17 |
| liste d'arrêt (355, 357) | ronde de la v6.2 hors `OK` ; étapes (0 bis), (2) et (4) | CL5 : P4C5-02, P4C5-05 (c) |
| essais (368–370, 387–391) | réseau ; pièces versées ; relevé v2 ; lacune | CL5 : P4C5-05 (a) et (d), P4C5-06 (a) et (b) |
| pièces (409–412) | relevés v1 à v5 ; listes v1 à v7 ; pièces des contre-lectures 5 et 6, des cas sains, du relevé v2 | § Pièces |
| contre-lecture (417–469) | détail, au lieu d'un marqueur | § Contre-lecture |

Rien d'autre ne change : titre, objet (hors C-14, C-17, essais et canal (d)), table (hors cinq lignes), plan points 1
(hors les deux phrases ajoutées), 2, 4 et 5, liste d'arrêt (hors deux lignes) et essais (hors deux passages) sont identiques à la
version relue par la contre-lecture 5.
