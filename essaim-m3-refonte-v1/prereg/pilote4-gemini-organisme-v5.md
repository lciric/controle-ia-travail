# Préenregistrement — quatrième pilote descriptif : la v6.2.1 sur la question M (course en cours), puis la v6.2.1 sur la question S à la place de la v5.3, sur la banque `confrontation-v3`, rondes de conception arrêtées par l'organisme, puis quatre générations notées, en segments — v5

**Statut** : v5, écrite par la lignée conv-audit le 26 octobre 2026 à partir de 04:23 UTC (heures lues sur
`date -u`), sur le mot direct de Lazar dans la session de session-depot vers 04:13 UTC (R-492, § Décisions) : **la v5.3 ne
court pas ; la seconde course de ce pilote est le même organisme, la v6.2.1, sur la question S**. **Pilote de conception**
(R-473 ; 03:46 Paris : « plus de scellement et de prereg tant qu'on est dans la phase de conception ») : ni
préenregistrement ni scellement au sens de R1 ; la relecture est gardée (contre-lecture 8, § Contre-lecture) ; le script
`sceller_pilote4_v5.py` n'y écrit que l'entropie, la graine de la course S et l'empreinte des pièces, que le lanceur relit.
**Texte différentiel sur la v4** (`pilote4-gemini-organisme-v4.md`, `782b858c537222245fd757c23ea6d75abae142df029eed3e53af36d8c78cfa95`,
tête `d1af7a2` de `outils/pilote4-gemini-travail`), elle-même différentielle sur P4v3 : tout ce que ce texte ne dit pas
est la v4 (et, par elle, P4v3, P3 et T2), appliqué selon la table de correspondance ci-dessous ; en cas de conflit, ce
texte prévaut. **La première course ne change pas** : la v6.2.1 sur la question M (`pilote4-gemini-v6-2-v1`, dossier réel
`pilote4-gemini-v6-2-v1-tentative2`, partie à 03:51:14 UTC sous le lanceur v10, tentative 2, R-490) tourne et s'achève
sous la v4, son lanceur et sa graine ; ce texte ne la touche pas, ni pendant, ni entre ses segments. Ce qui change :
**la seconde course** (objet, question, nom, graine, lanceur v11, batterie v13, ligne d'extension de GO, ligne de dépense,
porte « course M précédente », liste d'arrêt, pièces) et deux décisions de Lazar de 05:13 Paris qui règlent la lecture
(§ Plan, point 3). Lanceur : lignée session-depot (clés), dans son conteneur.

**Ce qui a été lu avant ce texte.** Ce que la v4 déclare, et depuis ses graines (03:00 UTC) : les lignes R-485 à R-492 et
GO-2026-10-26-03 du registre de `main` (jusqu'à `f52a75d`), les messages n° 62 à 64 de session-depot (dont, au n° 64,
des **faits mécaniques** de la course M en cours à 04:06 UTC : conception close après une ronde, génération 0 faite,
123 appels de Fable dont 115 `OK`, 7,83 USD — **aucun score**), la question S (`a54da93e…`), les synthèses des tours du
collisionneur « neuron explorer », « already clean », « test de M », « agents sur le noyau », « littérature des boucles »
et onze fiches de lecture des papiers sur les boucles et le bruit (aucun score), le registre d'hypothèses v2, le
protocole et les briefs de la boucle extérieure, le script de lecture et son LISEZMOI (aucun score). **Aucun score d'aucune
course du pilote 4 n'existe ni n'a été lu** (retenue de lecture, v4, § Plan, point 3).

## Décisions de Lazar (depuis la v4)

Relevé verbatim : `objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v8.md` (§ Pièces ; la v8 reprend la v7 mot pour mot et
ajoute les messages de 04:29 à 05:13 Paris et, à part, les lignes R-485 à R-492).

- **26 octobre, vers 04:13 UTC, dans la session de session-depot** (R-492) : « pas besoin de faire v5.3, en revanche ppose
  la question de la structure de l'organsime S ». Lecture de session-depot, que conv-audit partage et que Lazar n'a pas
  contredite dans la session de conv-audit (question posée à 04:17 UTC) : la seconde course est l'organisme v6.2.1 sur la
  question S, celle de la course S du second pilote, mêmes bornes, après la course M et après le tour du collisionneur sur
  les graines (R-491), dans l'enveloppe du pilote 4 (150 USD au plus). La partie « v5.3 » de la ligne d'extension de
  R-488 reste inutilisée.
- **04:48 Paris** (session de conv-audit) : « lance le collisionneur now », « un ou deux tours » (tour sur les graines) ;
  mot écrit chez session-depot vers 04:05 UTC (R-491) : deux tours, 8 USD, **entre les deux courses** ; la course S
  attend la fin de ce tour (même clé).
- **05:13 Paris** : (a) tâches fraîches contre le sur-ajustement adaptatif : part `test` tirée dans un vivier à chaque
  génération à partir du pilote 5 (changement du noyau : ne touche pas ce pilote), banque sœur « v3-bis » construite
  d'avance et lue une seule fois (dépense, sur devis) : « go » ; (b) **`test` dès la fin de chaque course, `test_final`
  une fois en fin de boucle** : « ok » (note `envois/decision-N-taches-fraiches-et-lecture-test-final-v1.md`,
  `4b23e00f…`, N-049 et N-050 proposés). Effet sur ce texte : § Plan, point 3.
- Pour mémoire, depuis la v4 et sans effet sur ses règles : 04:24, balayage neurone par neurone gardé sous conditions
  (N-048 proposé) ; 04:31, l'échange de session-depot sur la question « programme TAIF » (R-486, R-487) transmis à
  conv-audit, qui ne reformule pas non plus.

## Table de correspondance avec la v4

| dans la v4 | pour ce texte |
|---|---|
| seconde course : **la v5.3** (`4ecba58`, arbre `6251ab21…`, 22 fichiers), `COURSE=v5-3`, nom `pilote4-gemini-v5-3-v1`, lignée `gemini-organisme-v5-3`, question M | **seconde course : la v6.2.1** (commit `7ea32705c5437d91ed071dd95fb3209bb0b0035e`, arbre `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`, 26 fichiers : le même objet que la première course), **sur la question S** (`question-apprendre-structure-entrainement-generations-organismes-v2.md`, commit `4772b525081342a6a30ba8823733aa5770a888a8`, `a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289` ; servie à la génération 1, réponse archivée `reponse-question-g001.md`, sans effet sur le score : essai du noyau `test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score`), `COURSE=v6-2-s`, nom `pilote4-gemini-v6-2-s-v1`, lignée `gemini-organisme-v6-2-s` |
| « v5.3 » dans les règles, la liste d'arrêt, les bornes, le devis et les essais | « la course S » (la v6.2.1 sur la question S) ; la v5.3 ne court pas dans ce pilote (elle reste l'objet de comparaison du pilote décisif (b), sur la banque v6) |
| ce que la v4 et P4v3 disent du code de la v5.3 | sans objet pour ce pilote ; ce que le § Objet de la v4 dit de la v6.2.1 vaut pour les deux courses |
| porte « v6.2 précédente » : la v5.3 ne part qu'après une course v6.2 finie, fermée et saine | **porte « course M précédente »** : la course S ne part qu'après la course M de ce pilote finie, fermée et saine (même liste close ; `PRECEDENTE_V62` = son dossier `pilote4-gemini-v6-2-v1-tentative2` ; le lanceur v11 exige que la course M ait tourné sous le **lanceur v10** `0203f546…`, et que sa graine au manifeste soit la graine `v6-2` écrite ci-dessous) |
| la ligne de dépense de la v5.3 porte les empreintes de M et de la v6.2 de ce pilote | la ligne de dépense de **la course S** porte les empreintes de M (second pilote) et de la course M de ce pilote (§ Plan, point 1) |
| lanceur v10 (`0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952`) | **lanceur v11** (`lancer_pilote4_gemini_v11.sh`, `21854b794de90d874b23def1685e306ceba80b32cd471de1dd8cf750ad01d0d7`), dérivé du v10 par remplacements exacts au nombre attendu (`deriver_lanceur_pilote4_v11.py`, écart `diff-lanceur-pilote4-v10-vers-v11.txt`) : clé de course `v6-2-s` à la place de `v5-3` ; question par course (M pour `v6-2`, S pour `v6-2-s`) ; en mode réel, `COURSE=v6-2` refusée (la course M a tourné sous le v10) ; porte « course M précédente » sous le lanceur v10 (nom et empreinte attendus, écrits au `LANCEMENT.md`) ; rien d'autre ; **le lanceur v10 reste celui de la course M**, pour tous ses segments |
| batterie v12, série v13 (229 sur 229) | **batterie v13** (`essais_lanceur_pilote4_v13.sh`, `7b0a9bb0f7637480c19acb06138034582c8f69d2502cd3c483318f43f0f1e388`), dérivée de la v12 (`deriver_essais_pilote4_v13.py`) ; **série v14** (§ Essais) |
| entropie et graines `v5-3`, `v6-2` de la v4 | entropie de ce texte et graine `v6-2-s` (§ Plan, point 2) ; la graine `v6-2` de la v4 restituée telle quelle, pour la porte |
| `sceller_pilote4_v4.py`, `EMPREINTES-pilote4-gemini-v2.txt` | **`sceller_pilote4_v5.py`**, **`EMPREINTES-pilote4-gemini-v3.txt`** (§ Pièces) |
| phrase du critère 3 | « pilote descriptif, un organisme (la v6.2.1), deux courses à une graine chacune, l'une sur la question M, l'autre sur la question S, une phase de conception arrêtée par l'organisme (6 rondes au plus), quatre générations notées, une espèce appelée par appel, banque v3 » |
| « aucune comparaison entre les deux objets » (point 4 bis, P4C7-02) | **aucune comparaison entre les deux courses** : mêmes tâches, même objet, questions différentes, une graine chacune ; un écart entre elles tient à la question, à la graine ou au bruit, sans moyen de les séparer ; les verdicts des agents de la boucle extérieure restent tenus par cet interdit |
| liste d'arrêt : « la v5.3 ne part pas » | « la course S ne part pas » (mêmes issues de la course M hors de la liste close ; décision de Lazar) |
| devis : 75 USD par course, 150 pour les deux | inchangé (la course S remplace la v5.3 à la même borne) ; les 8 USD du tour du collisionneur entre les deux courses (R-491) sont hors de `GO-2026-10-25-02` (sous `GO-2026-10-24-07`, R-495) ; reste sur `GO-2026-10-25-02` au départ de la course S = 185 − 30,23 (pilote 3) − 31,57 (course M, R-494) = 123,20 USD ≥ 75 (le lanceur l'exige) |
| cas sains de la v5.3 après la v6.2 (série v13) | cas sains de la course S après une course M saine produite en simulation par le lanceur v11 (série v14) |
| contre-lectures 1 à 7 | celles de la v4, plus la contre-lecture 8 de ce texte (§ Contre-lecture) |

Tout le reste de la v4 vaut tel quel : noyau `8e5e2f7b` et reprise par segments, bornes, banque v3 et ses références, objet
v6.2.1 (§ Objet de la v4), canaux dits et acceptés pendant les courses, point 4 bis (bornes de Wilson, références, test
génération 0 contre génération 3 sur `test_final`, Holm sur quatre tests : deux par course, les deux courses de ce pilote),
hypothèses du pilote décisif (b) (`envois/pilote-decisif-b-v1/`, `903c6b51…`, écrites avant tout score : elles comparent la
v6.2.1 et la v5.3 sur la banque v6, inchangées), séparation d'avec l'étape 1 et la confrontation, retenue de lecture.

## Plan d'analyse (ce qui change de la v4)

1. **Deux courses du même objet** (R3 : une seule course de chaque nom) : la course M (`pilote4-gemini-v6-2-v1`, en
   cours, lanceur v10, v4), puis la course S (`pilote4-gemini-v6-2-s-v1`), avec le **lanceur v11**, en un ou plusieurs
   segments, après la fin de la course M (liste fermée poussée) et après le tour du collisionneur sur les graines (R-491 ;
   même clé). **Ligne d'extension de GO** pour la course S, poussée sur `main` avant elle, de la forme exacte :
   `| GO-2026-10-25-02 | 2026-10-26 | calcul | extension : pilote 4, seconde course (mot direct de Lazar, R-492) — la v6.2.1 7ea3270, arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d, sur la question S a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289 (commit 4772b525), à la place de la v5.3 ; banque confrontation-v3 157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d ; texte pilote4-gemini-organisme-v5.md <empreinte du texte> ; lanceur lancer_pilote4_gemini_v11.sh 21854b794de90d874b23def1685e306ceba80b32cd471de1dd8cf750ad01d0d7, noyau 8e5e2f7b ; mêmes bornes que la course M (4 générations, 6 rondes de conception au plus à 3 USD et 900 s chacune, 75 USD par course tous segments compris, jusqu'à 60 recherches par course, dont ≈ 10 web) ; segments : minuteur à 3 400 s, test de dépense et ligne de dépense à chaque segment | 185 USD au plus pour l'ensemble du GO, inchangé (pilote 3 : 30,23 USD dépensés ; pilote 4 : 150 USD au plus, la partie v5.3 de l'extension de R-488 inutilisée) | 2026-10-31 | Lazar | R-492 |`
   (l'empreinte entre chevrons est celle de ce texte, que donne le message de départ ; le lanceur ne lit pas la date).
   Session-depot la vérifie par les `grep` du lanceur (`GO-2026-10-25-02`, `calcul`, `a54da93e`, `4f13647a`, les 16
   premiers caractères de l'empreinte de ce texte) et par `157a2b45`. La ligne de R-488 ne fait pas partir la course S :
   elle ne porte ni la question S ni ce texte (essai `go-m-seulement-refuse-v6-2-s`). **Ligne de dépense** de la course S, après
   la fin de la course M et du tour des graines :
   `| <date du jour> | pilote4-gemini-v6-2-s-v1 | GO-2026-10-25-02 | 75 USD au pire cas | empreintes de M 5ae4e801423bbef0 ; empreintes de la v6.2 <16 premiers caractères> |`
   (« <16 premiers caractères> » : ceux du compagnon `.sha256` de `EMPREINTES-pilote-v1.txt` de la course M de ce pilote,
   `pilote4-gemini-v6-2-v1-tentative2`) ; segments K ≥ 2 : forme de la v4, mot pour mot, au nom de cette course. Le message
   de départ recopie mot pour mot ces lignes, l'empreinte du texte remplie ; s'il en diffère, rien ne part. **Copie de
   lancement** : la même copie que la course M, dont la tête passe, après la fermeture de la course M et avant la course
   S, à la tête de `outils/pilote4-gemini-travail` citée au message de départ (`git fetch origin outils/pilote4-gemini-travail canal/conv-audit-n04` — la seconde porte le commit `4772b525` de la
   question S —, puis `git checkout --detach` de cette tête ; le dossier de la course M, non suivi, reste en place) ; cette tête ne diffère de `8e5e2f7b` que par les
   chemins permis (`PERMIS_APRES_CODE`) ; la copie n'est jamais committée.
2. **Graines (R9)** : entropie E = 80294144857486793952864328916599533231 tirée par `sceller_pilote4_v5.py` (`secrets.randbits(128)` ; refuse
   numpy < 1.25 et toute ligne d'entropie ou de graine de trop) ; deux enfants `numpy.random.SeedSequence(E).spawn(2)` ;
   la graine de la course S vaut `int(enfant 0.generate_state(1, dtype=numpy.uint64)[0])` (l'enfant 1 n'est pas utilisé et
   n'est pas écrit) ; la graine de la course M est celle de la v4, enfant 1 de son entropie, restituée ici telle quelle
   pour la porte du lanceur v11 (chaque égalité sur une seule ligne, lue par le lanceur à chaque segment ; la graine S
   recalculée depuis l'entropie de ce texte) :
   graine de la course v6-2-s = 6967892196853497016
   graine de la course v6-2 = 2334107546136117589
3. **Moment de la lecture des scores** (v4, point 3, précisé par les décisions de Lazar de 05:13 Paris, N-050 proposé) :
   la retenue de lecture tient tant que Lazar n'a pas tranché les graines (tour R-491 entre les deux courses) ; session-depot
   exécute le script de lecture (`envois/lecture-pilote4-v1/`, relu par un agent neuf) à la fin de chaque course et pousse
   sa sortie **sans l'afficher**. Quand la lecture s'ouvre : **les scores de `test` et les faits mécaniques d'une course
   dès sa fin** ; **les scores de `test_final`** (intervalles, test génération 0 contre génération 3, Holm sur les quatre
   tests des deux courses) **une seule fois, à la fin du compteur de rondes de la boucle extérieure** ; la sortie du
   script v1 est unique ; sa v2, en écriture et relue avant usage, la sépare en deux fichiers par course (`test` ;
   `test_final`) ; jusque-là la sortie entière est poussée avec son empreinte et n'est pas affichée ; `test_final` se lit
   une seule fois, après la fin des deux courses et à la fin du compteur de rondes. Le point 3 de la v4 **permet** la
   lecture dès la fin d'une course ; ce texte lit moins, pas plus : aucune règle de course ne change.
   Les scores de `test_final` ne sont servis à aucun organisme ; ceux de `test` et les faits mécaniques peuvent l'être après
   la fin d'une course, sur décision de Lazar (v4). Rien de la question S ni de la réponse de l'organisme n'est servi à
   un autre organisme pendant une course.
4. **Point 4 bis** : inchangé ; il s'applique à chaque course (les deux familles, les deux parts) ; « aucune comparaison
   entre les deux courses » (table ci-dessus). Les hypothèses de la boucle extérieure qui nomment la v5.3 (registre v2,
   HC-P4-10 déclarée indécidable) restent indécidables par ce pilote ; le registre v3, à l'ouverture de la lecture, dit
   quelles fiches portent sur la course S.

## Liste d'arrêt

Celle de la v4, ligne à ligne, aux noms de ce texte (seconde course : la course S ; lanceur v11 ; essais de la batterie
v13), et en plus :

| condition | effet | garde ou vérification |
|---|---|---|
| course M de ce pilote hors de la liste close (générations notées autres que [0, 1, 2, 3], fin autre que « générations maximales », arrêts autres que des `STOP` repris puis « aucune lignée active », dernier code non nul, fermée sans reprise, lanceur autre que le v10 `0203f546…`, graine au manifeste autre que `2334107546136117589`) | **la course S ne part pas** ; Lazar décide | lanceur v11 (porte « course M précédente » ; essais `v62-…`, `reel-v6-2-s-sans-precedente`, `reel-porte-v10-attendu`) |
| `COURSE=v6-2` demandée en mode réel au lanceur v11 | refus avant tout appel (la course M a tourné sous le v10) | lanceur v11 (essai `reel-v6-2-refusee`) |
| ligne de GO sans la question S (`a54da93e`) ou sans ce texte | la course S ne part pas | lanceur v11 (essais `go-m-seulement-refuse-v6-2-s`, `go-autre-question`, `go-sans-texte`) ; la garde « sans l'arbre de la v6.2.1 » est celle de la v10 (étape 4), essayée en série v13 (`go-v53-seulement-refuse-v6-2`), sans artefact propre dans la batterie v13 (P4C8-02, déclaré) |
| question extraite du commit `4772b525` d'empreinte autre que `a54da93e…` | la course S ne part pas | lanceur v11 (`SHA_QUESTION`) |
| tour du collisionneur sur les graines (R-491) encore en cours | la course S attend ; rien ne part sur la clé des courses pendant qu'une course tourne ou qu'un tour tourne | session-depot (n° 71, § 2.5) |
| tête de la copie de lancement autre que celle du message de départ, ou dossier de la course M déplacé ou modifié | la course S ne part pas | session-depot (tête = celle du message de départ, relue au `LANCEMENT.md` avant la fermeture) ; lanceur v11 (`8e5e2f7b` ancêtre, code identique, `PERMIS_APRES_CODE` ; empreintes de la course M) |

## Essais du lanceur (R5)

Ceux de la v4 (§ Essais), sur la **batterie v13** (`essais_lanceur_pilote4_v13.sh`, `7b0a9bb0f7637480c19acb06138034582c8f69d2502cd3c483318f43f0f1e388`), dérivée de
la v12 par remplacements exacts au nombre attendu (`deriver_essais_pilote4_v13.py`) : chaque cas de la v12 garde un
équivalent (la course S à la place de la v5.3) ; cas ajoutés ou renommés : `reel-v6-2-refusee` (la clé `v6-2` en mode réel), `go-m-seulement-refuse-v6-2-s` et son carré (`go-m-seulement-autorise-v6-2`, `go-s-seulement-autorise-v6-2-s`, `go-s-seulement-refuse-v6-2`), `question-v6-2`, `v62-lanceur-v10-en-simulation`, `reel-v6-2-s-precedente-sous-ce-lanceur`, et cinq vérifications (`sain-v6-2-s-question`, `sain-v6-2-question`, `sain-v6-2-s-lanceur-attendu`, `reel-porte-v10-passee`, `reel-porte-v10-attendu`) ; les cinq cas réels de l'étape (0) courent sur la course S derrière une copie « réelle » de la course M saine (240 cas contre 229). **Série v14**, en simulation (faux appels
aux espèces, aucune clé ; réseau seulement pour le cas `passerelle-saine` et pour l'essai de moisson réelle du noyau sur
arXiv — lancée après la fin de la course M, pour ne rien ajouter au trafic vers arXiv pendant elle), batterie v13 sur
le lanceur v11 : de 04:48:23 à 04:58:35 UTC (`essais-lanceur-pilote4-v14.heures.txt`) ; **240 cas sur 240 conformes**, aucun échec (`essais-lanceur-pilote4-v14.log`, `41702cf4b2f39fbc382674fc1bc72cdd25fb13b86f820daed024d1f3800a0f8c`), contre 229 pour la série v13 ; les essais du noyau y ont passé 169 sur 169 (dont l'essai de moisson réelle sur arXiv, deux fois, après la fin de la course M). Une première série, lancée à 04:47 sur des copies du dépôt où manquaient deux commits que le lanceur du second pilote exige pour la course M de référence (`ec8e0b6c`, `b1c7f4b6`), a échoué sur 205 cas pour cette seule cause (copies incomplètes, aucun cas du lanceur en jeu) : journal gardé (`essais-lanceur-pilote4-v14-essai-rate-commits-absents.log`, `89e79df9…`), copies complétées, série rejouée depuis le début. La batterie efface le dossier `pilotes/` de sa copie sous `/root` et y commet des essais : ses copies (`DEPOT`,
`DEPOT_SOUS_ROOT`) ne sont jamais la copie de lancement ni une copie qui porte une course réelle (série v14 :
`/var/tmp/batterie-v13-v1/depot`, `/root/batterie-v13-depot-v1`, dans le conteneur de conv-audit). Lacune héritée, déclarée :
aucun cas n'essaie la course S en segments (la porte « course M précédente » est revérifiée à chaque segment K ≥ 2 par le
même code que pour la v5.3, essayé en v13 sur la v6.2). Les cas que ce texte cite y sont, chacun une fois et `OK` : `reel-v6-2-refusee`, `go-m-seulement-refuse-v6-2-s`, `sain-v6-2`, `sain-v6-2-s`, `sain-v6-2-s-question`, `reel-v6-2-s-sans-precedente`, `v62-lanceur-v10-en-simulation`, `reel-porte-v10-attendu`, les 22 cas `v62-…` et les 4 cas `seg-v62-…`.

## Pièces

Celles de la v4 (fichier d'empreintes `EMPREINTES-pilote4-gemini-v2.txt`, `dbc5928d…`, jamais réécrit), et en plus, sous
`prereg/pieces-pilote4-gemini/` : le **lanceur v11** `lancer_pilote4_gemini_v11.sh` (`21854b794de90d874b23def1685e306ceba80b32cd471de1dd8cf750ad01d0d7`), sa dérivation
`deriver_lanceur_pilote4_v11.py` et l'écart `diff-lanceur-pilote4-v10-vers-v11.txt` ; la **batterie v13**
`essais_lanceur_pilote4_v13.sh` et sa dérivation `deriver_essais_pilote4_v13.py` ; le journal de la série v14
(`essais-lanceur-pilote4-v14.log`, `.heures.txt`) ; `sceller_pilote4_v5.py` (le v4, aux marqueurs, au nom du fichier
d'empreintes et à la ligne de graine de la course M près, qu'il exige telle quelle ; essais `essais_scellement_pilote4_v5.sh`, 18 sur 18) ; le relevé v8 des mots de Lazar (`objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v8.md`) ; le brief du
sous-agent qui a dérivé le lanceur et la batterie et son LISEZMOI (`lanceur-v11-v1/` : brief `8e8c487a…`, LISEZMOI) ; les pièces de la contre-lecture 8
(`contre-lecture-8-v1/`) et de son traitement ; chacun avec son compagnon `.sha256`. Fichier d'empreintes de ce texte :
`EMPREINTES-pilote4-gemini-v3.txt` (toutes les pièces sous `pieces-pilote4-gemini/` et les contre-lectures
`pilote4-gemini-organisme-*`), empreinte `082edf4cebd40f23e7515530c16b4837850413cdb5a7aa97df281da3eb4896bf`, écrite par `sceller_pilote4_v5.py` avec l'entropie et la
graine ; vérifiée par `verifier_scellement_pilote4_v3.py` (`d733d0f4…`) et par
`envois/verification-depart-pilote4-v1/verifier_depart_pilote4_v2.sh` sur le canal.

## Contre-lecture

- **Contre-lecture 8** (sous-agent neuf, sur ce texte avant ses graines, `09227500e535cb02e18484a1566f636af3d5fafacf720c1e9e734adf1121f257`,
  puis sur la version complétée de la série v14 ; avec le lanceur v11, son écart, la batterie v13, le journal de la série
  v14, les scripts des graines et de vérification, le relevé v8) : `prereg/contre-lectures/pilote4-gemini-organisme-v5-cl8.md`,
  `a1551ad27555f5e5641c5ff486cb2230975cec559866e3de7f84598044220981` (brief `contre-lecture-8-v1/`), **« lançable après
  corrections mineures »** : seize constats, P4C8-01 bloquant d'un mot, aucun majeur ; lanceur v11 et batterie v13
  reproduits à l'octet par leurs scripts de dérivation ; aucun chemin trouvé où `v6-2` part en réel, où la question M
  sert à la course S, où la porte accepte en réel une course M hors du v10, ou où la graine M échappe à la comparaison.
  Traitement, dans ce texte :
  - P4C8-01 (bloquant) — **corrigé** : la formule du point 2 n'est plus écrite sous la forme d'une ligne de graine (deux lignes de
    graine seulement, `v6-2-s` et `v6-2`, comme le script l'exige).
  - P4C8-02 (mineur) — **corrigé** dans la liste d'arrêt : les essais cités sont ceux qui existent (`go-m-seulement-refuse-v6-2-s`,
    `go-autre-question`, `go-sans-texte`) ; la garde « sans l'arbre » est déclarée sans artefact propre en v13.
  - P4C8-03 (mineur) — **corrigé** : la tête du message de départ est gardée par session-depot, pas par le lanceur.
  - P4C8-04 (mineur) — **corrigé** au point 3 : la sortie du script v1 est unique ; la v2 la sépare ; `test_final` après la
    fin des deux courses et à la fin du compteur.
  - P4C8-05 (mineur) — **corrigé** au § Essais : les copies de la batterie ne sont jamais la copie de lancement.
  - P4C8-06 (mineur) — **corrigé** : les 8 USD du tour sous `GO-2026-10-24-07` (R-495) ; reste au départ de S = 123,20 USD.
  - P4C8-07 (mineur) — **corrigé** dans `verifier_depart_pilote4_v2.sh` (`pilotes/` exclu de l'état ; `4ecba58b` retiré).
  - P4C8-08 (mineur, non vérifiable par lui) — **corrigé** au point 1 : branches nommées au `fetch` ; les contrôles git
    de `verifier_depart_pilote4_v2.sh` sont rejoués par conv-audit sur sa copie à la tête du départ, et par
    session-depot sur sa copie de lancement avant la ligne de GO (message de départ).
  - P4C8-09, 10, 11, 13 (remarques) — **corrigés** aux lignes nommées (« ajoutés ou renommés » ; réseau de la série ;
    sous-déclarations du lanceur et du script des graines) ; la phrase du critère 3 garde la formule héritée de la v4.
  - P4C8-12 (remarque) — **déclaré** au § Essais : aucun cas n'essaie la course S en segments.
  - P4C8-14, 15 (remarques, pré-existantes) : rien à traiter ; P4C8-16 (remarque) — **fait** : le journal de la première
    série, ratée sur des copies incomplètes, est dans les pièces.
  Ces corrections sont écrites à la main par conv-audit après le rapport, avant le script des graines ; aucune ne change
  une règle du lanceur, la batterie ni la ligne de GO.
- **Ce texte, à ses graines** garde le nom de la v5 ; son empreinte n'est aucune de celles que la contre-lecture 8 a
  relues. De la version relue à lui, il porte en plus : la ligne de la contre-lecture 8 ci-dessus, le traitement de ses
  constats aux passages qu'il nomme, puis l'entropie, la graine de la course S et l'empreinte du fichier d'empreintes des
  pièces, écrites par `sceller_pilote4_v5.py` ; rien d'autre.
