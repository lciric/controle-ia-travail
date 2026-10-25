# Préenregistrement — troisième pilote descriptif : les organismes « assistés » de Gemini v5.3 puis v6, chacun seul, sur la banque scellée `confrontation-v1`, sous la configuration de la course M du second pilote (mêmes bornes, même question M à la génération 1) — v1

**Statut** : texte à contre-lire puis à sceller (R1, R2). Auteur : lignée conv-audit, 25 octobre 2026, à partir de
14:15 UTC (heure lue sur `date -u` ; les heures de Paris citées sont celles des messages de Lazar). Lanceur : lignée
session-depot (clés), dans son conteneur (root, `unshare` disponible ; aucune instance payante).

**Texte différentiel.** Ce texte incorpore par renvoi le texte scellé du second pilote,
`essaim-m3-refonte-v1/prereg/pilote2-gemini-organisme-v5-2-v2.md`
(`d294465429094e5099cb5facdad95e2b806aa8953640b57bcab99998396c066b`, branche `outils/pilote2-gemini-v5-2-travail`,
présent inchangé dans la branche de ce texte), appelé ci-dessous « le texte du second pilote » (T2). Tout ce que ce texte
ne dit pas est T2, appliqué à **chacune** des deux courses du pilote 3 selon la table de correspondance ci-dessous ; en
cas de conflit, ce texte prévaut pour le pilote 3 ; T2 reste seul en vigueur pour les courses M et S, qu'il ne change en
rien. L'erratum des graines de hachage (`prereg/pieces-pilote2-gemini-v5-2/erratum-graines-de-hachage-v1/ERRATUM-graines-de-hachage-v1.md`,
`06c28c7af626606a6ec0edf212ef9ae55570b6e469fbba156eabb09f9c42bccc`) vaut pour les renvois à T2.

## Décisions de Lazar et but

- **Décisions** (heure de Paris, 25 octobre 2026, dans la session de conv-audit) : 14:49–14:50 — « tu transmets tout ça à
  depot et il lance les runs sur le cloud pendant que je sors … à la chaîne sans me demander car il n'y aura pas
  internet » ; **14:56** — sur la ligne « Je ne lance ni v5.3 ni v6 en réel : ta décision « (c) puis (a) » fait passer
  d'abord le pilote, puis l'escalier » : « **lance-les sur le cloud après M et avant S** » ; 15:10 — « on aurait peut-être
  dû lancer le pilote 3 seulement pour économiser des sous ? » : réponse de conv-audit (canal), options (a) tout garder,
  (b) retirer le pilote 3, (c) retirer S (déconseillée), recommandation (a) ; **15:18 — « Recommandation : (a), confiance
  moyenne. : ok »** (tout garder : M, pilote 3, S). Un mot de Lazar qui retire le pilote 3 avant son départ l'arrête
  (liste d'arrêt).
- **GO** : une dépense nouvelle, hors de `GO-2026-10-25-01` (périmètre : les courses M et S). Elle exige le **mot direct
  de Lazar dans la session de session-depot** ; ligne proposée à Lazar à 13:58 UTC pour y être collée : « GO pour deux
  courses réelles descriptives de plus, v5.3 puis v6 de Gemini (lignées « assistées »), sous le noyau du pilote
  (`b1c7f4b6`), mêmes bornes que M (2 générations, 2 400 s, 30 USD par génération, 60 par course), 120 USD au plus pour
  les deux, échéance 31 octobre ; empreintes des objets, du préenregistrement scellé et contre-lu et du lanceur publiées
  par conv-audit sur le canal. Ordre : après M et avant S si elles sont prêtes quand M finit ; sinon S part sans les
  attendre et elles passent après S. Si la vérification ou la contre-lecture les arrête, elles attendent mon retour.
  Mêmes règles de refus que pour M et S. » Sur ce mot, session-depot inscrit **`GO-2026-10-25-02`** dans
  `registres/go.md` (une seule ligne, de type calcul, portant l'empreinte de la question `8b1c7511`, celles des deux
  objets `6251ab21` et `940c59c3`, celle de ce texte scellé et celle du lanceur) ; sans elle, le lanceur refuse. Sans le
  mot direct de Lazar dans la session de session-depot, rien de ce pilote ne part.
- **But** : voir ce que donnent, sur les deux familles de tâches réelles, deux conceptions « assistées » de Gemini,
  chacune une fois, sous la configuration exacte de la course M (même noyau, même banque, mêmes bornes, même question à
  g1) ; répéter la chaîne réelle avec statuts et coûts ; recueillir, comme **matériau**, leurs réponses à la question M.
  **Aucune hypothèse n'est testée** ; tout est rapporté ; **aucune différence entre objets n'est calculée ici** (ni
  v5.3 − M, ni v6 − v5.3, ni aucune autre) : toute comparaison entre objets relève d'un préenregistrement à part, scellé
  avant le calcul (celui de l'escalier de coût, ou un texte à elle). Rien d'opposable (R7) ; aucune lecture de résultat
  avant scellement (R1) ; aucun run visant un signe (R3) ; symétrie de l'audit (R4).

## Table de correspondance avec T2

| dans T2 | pour le pilote 3 |
|---|---|
| « la course », « M » (en tant que course lancée par ce texte) | chacune des deux courses du pilote 3 |
| « S ne part que si M est saine », `PRECEDENTE_PILOTE`, étape (0) | **porte d'entrée « M de référence »** (§ Courses) : chaque course du pilote 3 exige la course M du second pilote, finie, fermée et saine selon la liste close de T2, lue par `REFERENCE_M` |
| question M ou S | **question M v2 épurée pour les deux courses** (`8b1c7511…`) ; aucune question S |
| objet `ec8e0b6`, `fec005c6…`, 21 fichiers, lignée `gemini-organisme-v5-2-1` | objet de la course (§ Objets) : v5.3 `4ecba58`, `6251ab21…`, 22 fichiers, lignée `gemini-organisme-v5-3` ; v6 `7cd7508`, `940c59c3…`, 24 fichiers, lignée `gemini-organisme-v6` |
| `GO-2026-10-25-01`, 120 USD pour M et S | **`GO-2026-10-25-02`**, 120 USD pour les deux courses du pilote 3 |
| lanceur `lancer_pilote2_gemini_v5_2_v5.sh` (`83f8b9cf…`) | `lancer_pilote3_gemini_v5_3_v6_v1.sh` (§ Pièces), dérivé du premier par remplacements exacts |
| ligne de dépense de S portant l'empreinte des empreintes de M | ligne de dépense **de chaque course** du pilote 3 portant les 16 premiers caractères de l'empreinte de `EMPREINTES-pilote-v1.txt` de M |
| graines `maieutique` et `structure` (entropie de T2) | graines `v5-3` et `v6` (entropie de ce texte, § Graines) |
| usage déclaré d'avance des g0 de M et de S (comparaison A contre A) | **sans objet** : les courses du pilote 3 ne sont des répliques d'aucun bras ; elles ne comptent dans l'escalier que si un de ses bras est exactement leur configuration (même objet, mêmes bornes, même noyau) |
| v8 de la confrontation citant les deux `ferme.tar.gz` et les deux `EMPREINTES-pilote-v1.txt` | la même v8 cite **aussi** ceux des deux courses du pilote 3 |

## Courses, ordre et porte d'entrée

- **Deux courses**, dans cet ordre : **v5.3** (`COURSE=v5-3`, nom `pilote3-gemini-v5-3-maieutique-v1`), puis **v6**
  (`COURSE=v6`, nom `pilote3-gemini-v6-maieutique-v1`). Même code, même banque, mêmes bornes, même question ; seuls
  diffèrent l'objet et la graine. Une course par appel du lanceur ; chaque appel est une commande de fond de la session
  avec le délai maximal (7 200 000 ms), jamais `nohup`, `&` ni `setsid`, aucun redémarrage du conteneur jusqu'à la fin,
  réveils programmés (T2, en-tête) ; **jamais deux courses du noyau en même temps** (le lanceur refuse une voisine au
  décalage 900).
- **Ordre par rapport au second pilote** (décision de 14:56 ; proposition de 13:58) : si ce texte est scellé, sa
  contre-lecture publiée et la ligne `GO-2026-10-25-02` inscrite **avant la fin de M**, les deux courses du pilote 3
  partent après M, puis S ; sinon, **S part d'abord** (son lanceur ne dépend en rien de ce pilote) et les deux courses
  du pilote 3 partent après S. Dans les deux cas, la porte d'entrée est la même : M.
- **Porte d'entrée « M de référence »** (étape (0) du lanceur ; `REFERENCE_M` = dossier du pilote de la course M, dans
  la copie de lancement du second pilote) : la liste close « M saine » de T2 (l. 58–85), **appliquée telle quelle** par
  le même code Python que le lanceur de T2, avec le nom, l'empreinte et la lignée du lanceur et de l'objet de M
  (`lancer_pilote2_gemini_v5_2_v5.sh`, `83f8b9cf…`, `gemini-organisme-v5-2-1`, `GO-2026-10-25-01`) : empreintes de M
  vérifiées ; `LANCEMENT.md` de M écrit par ce lanceur, pour la course M, « code de retour : 0 », archive fermée
  complète, espace attendu ; générations 0 et 1 `OK`, non invalidées, sans anomalie, au plus 20 % d'appels hors `OK` et
  au moins un appel `OK` de Fable à chacune ; aucune génération invalidée au rapport ; fin « générations maximales » ; un
  seul arrêt, « aucune lignée active » ; **en réel** : M réelle (en-tête et manifeste), sous `GO-2026-10-25-01`, dossier
  sous `/root` ou `/home`, nom `pilote2-gemini-v5-2-1-maieutique-v1` ou sa tentative ; et **la graine de M au manifeste
  égale à la graine M de T2** (lue dans T2, dont l'empreinte est vérifiée). **La ligne de dépense de chaque course**
  (écrite par session-depot après la fin de M) porte les 16 premiers caractères de l'empreinte de
  `EMPREINTES-pilote-v1.txt` de M. Toute autre issue de M : aucune course du pilote 3 ne part ; Lazar décide.
- **Entre v5.3 et v6** (vérification de session-depot, consignée) : v6 ne part qu'après une course v5.3 dont le
  `LANCEMENT.md` porte « code de retour : 0 » et la ligne « archive fermée : ferme.tar.gz ( » (sans « ARCHIVE FERMÉE
  INCOMPLÈTE ») ; toute autre issue de v5.3 après son manifeste (code non nul, arrêt sur crédit épuisé, archive
  incomplète, course coupée) arrête le pilote 3 jusqu'au mot de Lazar. Un refus de v5.3 **avant** son manifeste suit la
  règle des tentatives (T2, plan § 1, l. 363–367 : une tentative suivante attend le mot de Lazar, sauf décision contraire
  de sa part consignée).
- **Copie de lancement** : une copie propre du dépôt sous `/root` ou `/home`, **autre que celle du second pilote** (dont
  la tête n'a pas les pièces de ce texte), à la tête de la branche `outils/pilote3-gemini-v5-3-v6-travail`, avec
  `git fetch origin canal/gemini-organisme-v5-3 canal/gemini-organisme-v6 canal/conv-audit-n04 main` ; jamais committée ;
  rien de non suivi. Les deux commits d'objets portent aussi l'arbre de la relève (`gemini/`, journaux de la racine,
  etc.) : **seul `organisme/` en est extrait** (`git archive <commit> organisme`) ; ces commits ne sont jamais extraits
  en entier ni empruntés comme arbre de travail, et rien d'autre n'en est exécuté.

## Objets

- **v5.3** : `organisme-gemini-m3-v5-3`, version 5.3.0, lignée **« assistée »** (décision de Lazar, 13:54 Paris : Gemini
  l'écrit à partir des réponses du collisionneur sur les emprunts, cellules A et C ; la revendication d'auto-conception
  est perdue pour elle). Poussée par Gemini depuis l'environnement de Lazar : branche `canal/gemini-organisme-v5-3`,
  commit **`4ecba58bcaa7dc3abe82c54fc38ee7285620bdf6`**, dossier `organisme/`, **22 fichiers**, empreinte d'arbre
  **`6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753`** (`boucle.empreinte_arbre` du noyau `b1c7f4b6`).
- **v6** : `organisme-gemini-m3-v6`, version 6.0.0, déclarée **« assistée »** par Gemini dans sa livraison (elle reprend
  la base v5.3) ; branche `canal/gemini-organisme-v6`, commit **`7cd7508287efa6fd667eaca7dffe23666f12692f`**, dossier
  `organisme/`, **24 fichiers** (la v5.3 plus `politique_endogene.py` et un essai ; `principal.py` et `manifeste.json`
  changent), empreinte d'arbre **`940c59c3dd58fdd5355244768faa1e9da02620fa455cd8ead15f8271145da64a`**.
- **Vérification** (sous-agent neuf, 25 octobre 2026, ≈ 13:30–13:51 UTC, utilisateur `nobody`, réseau coupé, environnement
  vide, `python -P -s -B`, aucune exécution hors des essais de Gemini ; rapport
  `prereg/pieces-pilote3-gemini-v5-3-v6/verification-objets-v5-3-v6-v1/LISEZMOI-v1.md`,
  `acb2c3ae5c1a25f6efc41919ea137a628d8091b71523d2a7e67dfad84d184562`) :
  - **v5.3** : arbre conforme ; même code que la reconstitution faite sur le message de Gemini (arbres syntaxiques
    identiques ; seuls docstrings et commentaires diffèrent) ; **39 essais passés** ; relevés identiques pour les graines
    de hachage **0, 1 et 2, réellement fixées** (cas B : 28 appels ; cas D : 29) ; 0 appel imbriqué sous `_VERROU` ;
    gardes C-01 à C-13 présentes ; **neuf réserves de conception non levées** (rapport § 8 : perte de la sonde non
    propre ; vote de la sonde dès 0,60 d'exactitude ; arbitrage forcé sans effet ; garde d'exactitude sur l'entraînement ;
    seuil Δ > 0,005 du journal d'ablations ; « multi-familles » par mots-clés et bonus doublé ; rondes de conception
    comptées à partir de 0 ; paramètre `erreurs` absent ; flux sans traits différent de la v5.2.1).
  - **v6** : arbre conforme ; **43 essais passés** ; relevés identiques aux graines 0, 1 et 2 (28 et 29 appels ; mêmes
    consignes et réponses qu'en v5.3) ; **la récompense interne change sans annonce**, même sans mutation (métrique
    proposée 0,231448 → 0,195747 sous le faux noyau ; mémoire différente) ; C-05 affaiblie (code candidat exécuté sans
    borne de temps) et deux replis silencieux nouveaux (C-07) ; trois des quatre fonctions réécrites jamais appelées ;
    **défaut bloquant** (rapport § 9.3) : un successeur dont `politique_endogene.py` a muté ne s'importe pas (`NameError`
    sur `ast`, établi par analyse statique des fichiers produits par les essais de Gemini, sans les exécuter).
  - **Le défaut bloquant de la v6 est inerte sous la configuration de ce pilote** (lu dans le code, non exécuté) : la
    mutation n'est tentée qu'en phase de conception (`--rondes-conception-max 0` : aucune), si `autoriser_mutation_code`
    est vrai (clé que le noyau `b1c7f4b6` ne pose jamais : aucune occurrence dans `essaim_m3/`), ou à partir de g1 en cas
    de « stagnation », qui exige deux scores à l'historique (`principal.py` de la v6, l. 907–921) ; à g1, l'historique
    du noyau (`archive.historique(lignee)`, `boucle.py` l. 630) ne porte que g0 ; et g2 n'est pas servie. Le code
    candidat sans borne n'est exécuté que sur ce chemin. **Ce qui tourne** est donc la v6 sans mutation : la v5.3 plus sa
    récompense interne nouvelle. Une mutation observée malgré tout (appel de rôle `architecte_mutation_endogene` au
    journal) est rapportée telle quelle ; son successeur ne tournerait pas.
- **Ce qui suit de T2 vaut pour ces objets** (déclarations, l. 120–130) : leur code partage du vocabulaire avec la
  question M (même exemple de format de formulation de requêtes : « situational awareness alignment faking LLM »,
  « maieutic elicitation proper scoring rules alignmentforum », `principal.py` l. 724 et 725 ; `CONCEPTION.md` parle de
  maïeutique et de coercition) ; leurs **dix** requêtes de réserve (les six de la v5.2.1 plus « representation
  engineering linear artificial tomography truthfulness probes », « self-improving agents archive stepping stones
  benchmark overfitting », « weak-for-strong meta-agent routing query-level cascade evaluation », « reward tampering
  sycophancy subterfuge language models evaluation », l. 85–96 et 86–97) ; la question M a été écrite par Gemini,
  concepteur de ces organismes ; **les réponses du collisionneur ont été servies à Gemini à la conception de la v5.3
  (déclaré), jamais à un organisme à l'exécution**.
- **Score de g0 à g1** (diffère de T2, l. 432–437, qui le disait de la v5.2.1) : la v5.3 et la v6 recopient à g1 le
  score `test` de g0 dans leur archive généalogique (`memoire_isvd.py`, l. 101–112 : `score_noyau`, dans la mémoire,
  fermée) ; leur retour arrière et leur mitose n'agissent qu'avec deux scores (l. 115–118 ; `mitose_spectrale.py`
  l. 74–75 et 116–117) : à g1, sans effet lu dans le code sur les consignes, non établi par exécution. Le contrat rend le
  score `test` à l'organisme ; celui de `test_final` ne l'est jamais.
- **Sondes sur activations** : la v5.3 et la v6 savent appeler `entrainer` et `predire` ; ce pilote n'en sert aucun
  (`--entrainements-max 0`, aucun `--traits`), comme T2.

## Bornes, banque, code, espèces, moisson, isolation, test de dépense

Ceux de T2 (l. 146–315), **identiques à la course M** : les arguments du noyau sont les `COMMUNES` du lanceur de T2,
inchangés dans le lanceur de ce texte (`--generations 2 --especes --appels-max 160 --usd-par-generation 30 --temps-max
2400 --max-tokens-appel 8192 --recherches-max 6 --telechargements-max 3 --octets-max 40000000 --entrainements-max 0
--rondes-conception-max 0 --parallele-max 8 --relances-max 1 --isoler-reseau --plafond-total 60 --decalage-uid 900
--question-ouverte <question M> --question-ouverte-aux g001`), sauf `--organisme-impose
"<lignée de la course>=$PILOTE/organisme@gemini"`. Ce que T2 dit de la moisson **d'après le code de la v5.2.1**
(nombre et texte des requêtes, blocs de moisson, corpus d'archive) ne se transpose pas : la v5.3 et la v6 décident de
leur moisson dans les bornes servies (« moisson dynamique sans plafond fixe ») ; rapporté tel quel par l'extrait. Le
test de dépense porte `go` = `GO-2026-10-25-02`.

## Devis au pire cas

2 × 30 = 60 USD par course, **120 USD pour les deux**, plus les tests de dépense (≈ 0,002 USD chacun). Ordre de
grandeur attendu, **non opposable** : celui de la course M (même configuration ; T2, l. 266–279 : ≈ 21 à 46 USD la
course selon la longueur des sorties), corrigé par le nombre d'appels que la v5.3 et la v6 font par génération, lu en
simulation (§ Essais du lanceur : <<APPELS_SIMULATION>>) ; la dépense réelle de M, consignée par session-depot après M,
en donne la mesure la plus proche. Le reste déclaré au lanceur est celui de `GO-2026-10-25-02` (≥ 60 USD avant chaque
course).

## Hypothèse

Aucune (pilote descriptif). Ce qui est rapporté, **par course**, est ce que T2 rapporte (§ Hypothèse, l. 318–332), plus,
pour la v6, les appels de rôle `architecte_mutation_endogene` s'il y en a. **Aucune différence n'est calculée ni
nommée** (ni g1 − g0, ni score − référence, ni entre les deux courses, ni avec M ou S, ni avec le premier pilote) ; les
réponses ne sont ni notées, ni jugées, ni comparées.

## Prédiction chiffrée et signe attendu

Aucune prédiction ; aucun signe attendu ; rien n'est écrit sur ce que « devraient » donner ces organismes, leurs
emprunts, la récompense nouvelle de la v6, ni sur ce que leurs réponses « devraient » dire.

## Métrique

Celle de T2 (l. 339–345).

## Seuil

Aucun seuil de lecture. Seuils de garde : ceux de T2 (l. 349–353), avec, à la place de « S ne part que si M est
saine », la porte « M de référence » et la condition entre v5.3 et v6 (§ Courses) ; reste de `GO-2026-10-25-02`
≥ 60 USD avant chaque course.

## Plan d'analyse

1. **Une seule course de chaque nom** (R3), v5.3 puis v6 ; gardes, tentatives et étapes de T2 (plan § 1, l. 357–403),
   avec : (0) la porte « M de référence » ; (ii) la graine de la course écrite ici et recalculée depuis l'entropie de ce
   texte, l'empreinte du lanceur de ce texte citée ; (iii) `$PILOTE/organisme/` = `git archive <commit de l'objet>
   organisme`, empreinte d'arbre et nombre de fichiers de l'objet de la course ; question M (`8b1c7511…`) ; (iv) ligne
   `GO-2026-10-25-02` portant, sur la même ligne, le type calcul, `8b1c7511` et l'empreinte de l'objet de la course ;
   dépense consignée avec l'empreinte des empreintes de M ; (viii) la commande de T2 avec `--go GO-2026-10-25-02` et
   `--organisme-impose "<lignée>=$PILOTE/organisme@gemini"`. Un fichier `STOP` n'est posé que pour un incident technique.
2. **Graines (R9)** : entropie E = <<ENTROPIE>> tirée au scellement par `secrets.randbits(128)` ; deux enfants
   `numpy.random.SeedSequence(E).spawn(2)` ; graine de chaque course = `int(enfant.generate_state(1, dtype=numpy.uint64)[0])`,
   **l'enfant 0 pour la v5.3** (première course), **l'enfant 1 pour la v6** (chaque égalité sur une seule ligne, lue et
   recalculée par le lanceur) :
   graine de la course v5-3 = <<GRAINE_V53>>
   graine de la course v6 = <<GRAINE_V6>>
3. **Moment de la lecture des scores (R1)** : celui de T2 (plan § 3, l. 412–482), fichier par fichier, avec les deux
   mêmes conditions — (i) le préenregistrement de l'étape 1 qui part scellé (à ce jour sa v9, R-418) ; (ii) inscrit dans
   la version 8 du préenregistrement de la confrontation qu'elle ne change ni la table de lecture de H-E1, ni les seuils,
   ni les règles de lecture de sa version 7 (`74487a41fe29b4ad0e5688df9fb9fda815725cdd7521ee2a327694b2fa4ddf61`) — ; la v8
   cite aussi les empreintes des deux `ferme.tar.gz` et des deux `EMPREINTES-pilote-v1.txt` de ce pilote. Jusque-là,
   personne ne lit les fichiers que T2 énumère (l. 451–456), chemins transposés à la lignée de la course ; fermeture
   mécanique, liste fermée de ce qui est poussé, recherche des clés par valeur avant de pousser, branche
   `pilotes/<nom de la course>`, jamais `main` : comme T2 (même code de lanceur). Pendant la course, session-depot ne
   consulte que le journal des appels de la génération en cours, par son chemin exact,
   `<espace attendu>/travail/<lignée>/gNNN.noyau/journal-appels.jsonl`.
4. **Lecture** : après le moment du point 3, par course, le tableau de T2 (plan § 4, l. 483–489), dans un tableau à part
   pour chaque course ; la ligne « M de référence » du `LANCEMENT.md` recopiée ; la réponse à la question M, telle
   quelle, avec sa structure mécanique. Rédigé par conv-audit, relu par session-depot ; aucune lecture de verdict (R13
   sans objet).
5. **Ce que ce pilote ne dit pas** : ce que T2 ne dit pas (plan § 5, l. 490–498), et de plus : rien sur la valeur des
   emprunts au collisionneur, ni de la récompense nouvelle de la v6, ni de son auto-réécriture (inerte ici) ; rien sur
   une conception contre une autre ; ces lignées sont « assistées » : aucune revendication d'auto-conception ne s'appuie
   sur elles.

## Critères de lecture gelés

Ceux de T2 (l. 500–525), appliqués à chaque course du pilote 3 (« l'autre course ou le premier pilote » se lit : toute
autre course, des trois pilotes) ; la phrase du critère 3 devient « pilote descriptif, deux organismes, une course à une
graine chacun, deux générations, une espèce appelée pour les tâches, une question posée une fois par course ».
L'audit de symétrie (R4), s'il est déclenché, est fait par un sous-agent neuf lancé par conv-audit, sans relance.

## Liste d'arrêt

Celle de T2 (l. 527–557), ligne à ligne, pour chaque course (les essais cités par T2 restent exigés passés dans le
conteneur du lancement ; les essais du lanceur sont ceux de ce texte), et en plus :

| condition | effet | garde ou vérification |
|---|---|---|
| M non saine (liste close de T2 : empreintes, lanceur `83f8b9cf…`, code de retour, archive, espace attendu, générations 0 et 1, statuts d'appels, fin et arrêt ; en réel : M réelle, sous `GO-2026-10-25-01`, graine M de T2, dossier sous `/root` ou `/home` et nom de M) ; `REFERENCE_M` absent ou non défini ; T2 absent ou d'autre empreinte ; ligne de dépense sans l'empreinte des empreintes de M | aucune course du pilote 3 ne part ; Lazar décide | lanceur, étapes (0) et (4) (essais `m-…`, `reel-reference-…`, `m-texte-second-pilote-modifie`, `m-depense-sans-empreinte`) |
| v5.3 finie avec un code de retour non nul, une archive incomplète, un arrêt sur crédit épuisé, ou coupée | v6 ne part pas ; Lazar décide | session-depot, lecture du `LANCEMENT.md` de v5.3, consignée |
| aucune ligne `GO-2026-10-25-02` de type calcul portant, sur la même ligne, `8b1c7511` et l'empreinte de l'objet de la course ; reste < 60 USD | la course ne part pas | lanceur (essais `go-…`, `reste-insuffisant`) |
| mot de Lazar qui retire le pilote 3, ou une course de ce pilote, avant son départ | elle ne part pas | session-depot |
| appel de rôle `architecte_mutation_endogene` au journal de la v6 | rapporté ; aucun effet sur la course (le successeur de g1 ne tourne pas) | extrait, après la course |
| la course M n'est pas encore finie, ou S tourne | la course attend (voisine au décalage 900 : refus) | lanceur |

## Essais du lanceur (R5)

<<ESSAIS_DU_LANCEUR>>

## Pièces

`prereg/pieces-pilote3-gemini-v5-3-v6/` : le lanceur **`lancer_pilote3_gemini_v5_3_v6_v1.sh`**
(`5a56d8546ac4f81a96acdfd1acfe09bbe3a8b8ca255976c70c7d06148ca87050`), son script de dérivation
`deriver_lanceur_pilote3_v1.py` (`d431b45d2e991769c96917f662c1c4e566b1cc0009526fe52e99fa23c632c575`) et l'écart au
lanceur de T2 `diff-lanceur-v5-vers-pilote3-v1.txt` (`0121d1e934b1b13e63bd2a732b4b200ce06cf6aad17d268e4056579706a2c8fc`) ;
ses essais `essais_lanceur_pilote3_v5_3_v6_v1.sh` et leur journal ; les pièces des cas sains `simulation-lanceur-v1/` ;
la vérification des objets `verification-objets-v5-3-v6-v1/` ; le fichier d'empreintes de toutes les pièces et des
contre-lectures de ce texte, `EMPREINTES-pilote3-gemini-v5-3-v6-v1.txt`, d'empreinte <<EMPREINTE_PIECES>>.

## Contre-lecture

À faire par un sous-agent neuf, qui n'a écrit ni ce texte ni T2, avant le scellement (R2) ; constats traités dans une
v2 de ce texte (nouveau nom, R12) avec leur table de traitement.
