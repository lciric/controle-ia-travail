# Préenregistrement — second pilote descriptif : l'organisme de Gemini v5.2.1, seul, sur la banque scellée `confrontation-v1`, moisson ouverte à quatre sources, en deux courses (maïeutique puis structure) avec une question ouverte posée à la génération 1 — v2

Remplace la v1 (`pilote2-gemini-organisme-v5-2-v1.md`, `c0863993f72438787d33829a71dd595094f8a1ef7eb81a4a89e2ed2b753e4c34`,
gardée, R12), contre-lue (contre-lecture 1 : sous-agent neuf, 25 octobre 2026, 12:55:57–13:17:28 UTC, rapport
`prereg/contre-lectures/pilote2-gemini-organisme-v5-2-v1-cl1.md`,
`e4a7292fa5b46223d06121795c2b81ceb33d3eba3e3e8010106cf1918909125d` ; verdict « scellable après corrections » ; 14 constats
P52C1-01 à P52C1-14, dont 2 majeurs, traités en fin de texte). Comme la v1, ce texte remplace, avant tout départ, le texte
scellé du second pilote sur la v5.1 (`pilote2-gemini-organisme-v5-1-v3.md`,
`72f534ae4db10f6eeec41fe73b725583d0cea54d76398b4a995b051e1639a9c9`, branche `outils/pilote2-gemini-v5-1-travail`,
commit `c1e73f5438cc438909b4d59dd6141d005ba38a6a`), **jamais lancé** : les décisions de Lazar de 12:11 à 13:33 (heure de
Paris) en ont changé l'objet, le code, l'ordre des courses et une question (liste ci-dessous). Ce texte reprend le
dessin et les gardes de ce texte, contre-lu deux fois (contre-lecture 1 : `pilote2-gemini-organisme-v5-1-v1-cl1.md`,
`688b1e21f0a7972cc2e9982e557139ecd8929a4990926d50ec7b64a3497011a8` ; contre-lecture 2 :
`pilote2-gemini-organisme-v5-1-v2-cl2.md`, `1b513a0eb8838f9eda9c960b5fddbf8ba9b46e1794e00ed1352cb7b0bba39903` ; constats
traités en fin de texte, repris) ; ce qui change est dit à chaque section et récapitulé au § « Changements ». Second
pilote après celui de l'objet v4 (`pilote-gemini-organisme-v4-question-v3.md`, `1c5b6f7d…`, parti le 25 octobre à
07:49 UTC, arrêté sur le crédit épuisé ; rapport mécanique v2 et audit de symétrie, branche `canal/conv-audit-n04`,
commit `7d1feec550e3d3bdaf963ecade2cf1558b73e53f`).

Décisions de Lazar (heure de Paris, 25 octobre 2026), reprises du texte remplacé : 01:45 (moissonneur, v5 de Gemini,
second pilote plus tard) ; 09:07 (question S v2 à g1) ; 09:26 (v5.1) ; 09:51 (deux courses, « les deux ») ; 09:58 (garde
avant départ = **test de dépense**, « car la recharge automatique est activée sur tous les modèles API ») ; 10:17
(plafonds, option (b) : « 30 par génération, 60 par course, 120 au pire pour les deux, 8 192 jetons … : go ») ; 11:37
(« alors avec Brave, ne le retire pas » : source « web » servie). **Nouvelles** : 12:11 — « je maintiens b » : clés
OpenAlex et Semantic Scholar intégrées au noyau **avant** le pilote ; 12:20 — « (b) v5.2 d'abord » ; 12:24 — la clé
Semantic Scholar entre aussi dans le pilote ; 12:27 — « attendre v5.2 » ; 12:50 — ordre **M puis S** (« M puis S :
parfait ») ; 13:26 — « (b) … : go » (objet = v5.2 poussée par Gemini) ; 13:27–13:28 — question M **v2 épurée** de
Gemini (aucune suggestion d'outil) ; vers 13:31–13:33 — « corrige tout de suite » (dans la session de session-depot, sur
le constat RV52-01 de session-depot : objet = **v5.2.1**). Mots directs de Lazar dans la session de session-depot,
consignés sur `main` : R-404 (recharge automatique active), R-407 (« go pilote 2 », ligne `GO-2026-10-25-01`), R-409 (120
USD pour les deux courses), R-421 (clés de moisson nommées : extension de `GO-2026-10-24-04`), R-423 (objet v5.2, code
`b1c7f4b6`, M puis S), R-424 (consigne de lancement : « lancer la course M dès que conv-audit livre le préenregistrement
scellé et sa contre-lecture sur le canal ; puis S automatiquement si M est saine selon la liste gelée du lanceur ; au
moindre refus du lanceur, ne rien forcer, attendre mon retour » ; attestation de la recharge à passer mot pour mot), R-426
(objet `2d00232`, question M v2 épurée, « empreintes publiées par conv-audit sur le canal »), R-428 (GO validé, M
d'abord, « Go maintenant en autonomie sur ton cloud »), R-429 (v5.2.1 = `2d00232` + C-13). Décisions de Lazar dans la session de conv-audit qui touchent la lecture de ce pilote
(heure de Paris) : 14:01 et 14:12 — « (c) puis (a) : go » (les bornes des courses suivantes se décident par un escalier
de coût préenregistré, après les indices gratuits de ce pilote) ; 14:15 — « excellent go » (δ = 0,10 et règle gelée de
l'escalier ; le bruit mesuré par les générations 0 de M et de S, voir plan § 3). But : voir ce que donne, sur
les deux familles de tâches réelles, l'organisme v5.2.1 (code figé, mémoire spectrale transmise, moisson documentaire
servie par le noyau sur quatre sources avec clés) ; répéter la chaîne réelle avec statuts et coûts ; recueillir, comme
**matériau**, deux réponses de son essaim à deux questions ouvertes, posées avant qu'il ait vu quoi que ce soit de notre
part. **Aucune hypothèse n'est testée** ; tout est rapporté. Rien d'opposable (R7) ; aucune lecture de résultat avant
scellement (R1) ; aucun run visant un signe (R3) ; symétrie de l'audit (R4).

- Auteur : lignée conv-audit. Date : 2026-10-25, 12:55 UTC (heure lue sur `date -u` ; les heures de Paris citées sont
  celles des messages de Lazar). Lanceur : lignée session-depot (clés), dans son conteneur (root, `unshare` disponible ;
  aucune instance payante), une course par appel du script
  `prereg/pieces-pilote2-gemini-v5-2/lancer_pilote2_gemini_v5_2_v5.sh` (empreinte au § Pièces ; versions v1 à v4 gardées,
  jamais à lancer), qui exécute le plan § 1 et § 3 pas à pas et refuse, avec sa raison consignée, à chaque écart ;
  processus consigné par son PID dans `LANCEMENT.md`, arrêt par PID (R10). Placé par session-depot avant A1/A2 de
  l'étape 1, dans le même conteneur (R-423), quand les clés de moisson y sont visibles (R-420). **Façon de lancer**
  (P52C1-01) : chaque course est un appel du lanceur, et chaque appel est **une commande de fond de la session avec le
  délai maximal (7 200 000 ms)** — jamais `nohup`, `&` ni `setsid` (un processus détaché est arrêté peu après la fin du
  tour de la session ; le délai par défaut d'une commande de fond, 1 800 s, couperait la course au milieu de g0) ;
  **aucune action qui redémarre le conteneur pendant une course** (pas de silence de redémarrage, R-420, entre le départ
  et la fin du lanceur) ; session-depot reste éveillé, par réveils programmés, jusqu'à la fin de chaque appel.
- **Deux courses**, dans cet ordre : **M** (`COURSE=maieutique`, nom `pilote2-gemini-v5-2-1-maieutique-v1`), puis **S**
  (`COURSE=structure`, nom `pilote2-gemini-v5-2-1-structure-v1`). Même objet, même code, même banque, mêmes bornes ;
  seules diffèrent la question et la graine. **S ne part que si M est « saine »**, définition close vérifiée par le
  script de S dans les pièces lisibles de M (variable `PRECEDENTE_PILOTE` = dossier du pilote de M) : empreintes de M
  vérifiées (`EMPREINTES-pilote-v1.txt` et son compagnon) ; `LANCEMENT.md` de M écrit par ce même lanceur (même
  empreinte), pour la course M, avec « code de retour : 0 » et la ligne « archive fermée : ferme.tar.gz (… » (pas
  d'archive incomplète, aucun espace des organismes autre que l'espace attendu) ; extrait mécanique de M : exactement les
  générations 0 et 1 de la lignée, chacune au statut `OK`, non invalidée, sans anomalie du noyau, **avec au plus 20 %
  d'appels hors `OK` et au moins un appel `OK` de `CLAUDE_FABLE_5_1`** (comptes `appels.par_statut` et
  `appels.par_espece` de l'extrait, sans score ; le seuil est celui du critère de lecture gelé n° 1 ; P52C1-02 : sans
  lui, une M dont tous les appels échouent pour une raison d'environnement passerait pour saine et S se perdrait de la
  même façon) ; aucune génération invalidée au rapport ; fin de la lignée « générations maximales » ; un seul arrêt de la course, « aucune lignée
  active ». **En réel, de plus** : M a tourné en réel (en-tête « (reel, tentative N) » de son `LANCEMENT.md`,
  `manifeste.reel` vrai), sous `GO-2026-10-25-01` (`manifeste.go_id`), avec la graine M du texte scellé
  (`manifeste.entropie_seed_sequence`), dans le dossier des pilotes de la copie de lancement, sous le nom
  `pilote2-gemini-v5-2-1-maieutique-v1` ou sa tentative ; les empreintes de M listent son `LANCEMENT.md` et son extrait ;
  et **la ligne de dépense de S**, écrite par session-depot **après la fin de M**, porte les 16 premiers caractères de
  l'empreinte de `EMPREINTES-pilote-v1.txt` de M. **Toute autre issue** (M simulée ou d'une autre graine, plus de 20 % d'appels hors `OK` ou
  aucun appel `OK` de Fable à une génération, crédit épuisé, fichier `STOP`, modèle non conforme, isolation indisponible, exception du noyau après le manifeste, archive
  incomplète, espace autre, génération non tournée ou invalidée, g1 sans successeur valide, M non partie) : S ne part
  pas, refus consigné, et attend une nouvelle décision de Lazar. **Les plafonds du noyau ne bloquent pas S** (avec 2 × 30 = 60,
  le plafond total de M ne peut être atteint qu'à la fin de g1 ; les refus d'appels au plafond d'une génération de M,
  `refus_noyau`, et la dépense de M sont consignés dans le `LANCEMENT.md` de S, pour information) ; **mais le reste du GO
  le peut** (P52C1-06) : S ne part pas si le reste déclaré est sous 60 USD, ce qui arrive si M et les tests de dépense
  ont pris plus de 60 USD sur les 120 du GO (R-407 y range les tests de dépense). **Procédure entre M et
  S** : la copie de lancement n'est jamais committée ; le dossier de M n'y est jamais modifié ; M est poussée depuis un
  autre arbre de travail (copie des fichiers de son `A-POUSSER-v1.txt`) ; le rapprochement de la dépense avec la console
  s'écrit dans `registres/depenses.md`, jamais dans le dossier de M.
- **Objet** : `gemini-organisme-v5-2-1` — **v5.2.1** = la v5.2 poussée par Gemini plus une correction de session-depot
  (C-13). Branche `outils/gemini-organisme-v5-2-1`, commit **`ec8e0b6c82d18a7ca040302538dcd33e557bf818`** (session-depot,
  12:35 UTC), dossier **`organisme/`** à la racine du commit, **21 fichiers**, sans `memoire_isvd.json` ni
  `etat_generation_precedente.json` ni `__pycache__`, empreinte d'arbre
  **`fec005c6626b3d1aa960702e4322b44ade3b902157dd84eae8e658b70e4f43f4`** par `boucle.empreinte_arbre` (celle que le noyau
  consigne au manifeste ; calculée par conv-audit avec le noyau `b1c7f4b6`, égale à celle de session-depot, R-429).
  Famille nominale `gemini`. Lignée imposée unique, **sans phase de conception** (`--rondes-conception-max 0`), **G = 2**
  générations notées (g0, g1 ; g1 reçoit `memoire_isvd.json`, l'historique de g0 et la vue d'archive ;
  `--relances-max 1`). **Provenance**, maillon par maillon :
  (1) livraison de Gemini reçue de Lazar à 12:52 (`livraison/recu-gemini-v5-2-v1.txt`, `b06ada66…`), reconstituée sans
  exécuter son script (branche `outils/gemini-organisme-v5-2`, `5c25bd19…`, arbre `4fcdc7db…`) : **pas l'objet** ;
  (2) v5.2 **poussée par Gemini** depuis l'environnement de Lazar : branche `canal/gemini-organisme-v5-2`, commit
  `2d00232fef0bc770dc0d862316d3cc0520463a90` (auteur « Controle IA », cinq commits de 13:11 à 13:17 Paris tirés de
  `db90512`, ne touchant que `organisme/`), arbre `011d62b5…`, 19 fichiers ; par rapport à (1), trois fichiers changent
  (`principal.py`, `CONCEPTION.md`, `tests/test_moissonneur_v5.py`) : commentaires et chaînes de documentation retirés
  de `principal.py`, dont ceux qui renvoyaient aux corrections C-01 à C-12 (le code de ces corrections est inchangé à
  la lecture : vérifié par conv-audit sur le diff, constat identique de session-depot, R-426), extraction des documents
  en trois fenêtres (début, cœur, fin), trace « début … fin » du document dans la mémoire, blocs de moisson portés à
  4 500 caractères (induction) et 2 500 (consignes de tâche) — l'essai que conv-audit avait trouvé en défaut sur (1)
  passe ; (3) **C-13** par session-depot, sur le constat RV52-01 (le bloc de moisson était coupé avant sa ligne de
  fermeture dès qu'il passait 2 500 caractères) et le mot de Lazar « corrige tout de suite » : `_bloc_moisson_borne`
  referme toujours le bloc après la coupe (corps ≤ 2 500 en consigne de tâche, ≤ 4 500 en induction) et balise aussi le
  repli sur le corpus d'archive ; `_sanitiser_donnee_externe` change `===` en `= =` dans tout texte extérieur (aucune
  balise forgée) ; `CORRECTIONS-v4.md`, `tests/test_corrections_v4.py` (5 essais) ; manifeste `organisme-gemini-m3-v5-2-1`,
  5.2.1 ; `git diff 2d00232 ec8e0b6` : 4 fichiers, +122 −11 (relu en entier par conv-audit). **Vérifié par conv-audit**
  (utilisateur `nobody`, réseau coupé par `unshare -n`, environnement vide, `python -I -B`, copie à part, 25 octobre vers
  12:45 UTC) : **34 essais passés** (`tests-isolation-v521-v1.log`) ; relevés complets identiques pour les graines de
  hachage 0, 1 et 2 sous le faux noyau déterministe (cas B : tâches et question, moisson fermée ; cas D : moisson
  ouverte), empreintes des relevés `b64ce1fc…` (B) et `33a4d664…` (D) ; 0 appel imbriqué sous `_VERROU` ; mêmes
  importations que la v5.1 ; aucun accès réseau, sous-processus ni variable d'environnement (recherche de motifs, pas
  de preuve). La v5.2 (2) seule : 29 essais passés chez conv-audit et chez session-depot (les 29 de Gemini). **Corrections
  venues de nous** : C-12 (v5.1, conv-audit) et C-13 (v5.2.1, session-depot), toutes deux avant tout run réel, sur
  simulation sans score réel ; **aucune ne vient d'un résultat réel** ; l'objet n'est donc plus « écrit par Gemini
  seul » : il l'est à deux corrections mécaniques près, déclarées. Plafonds de sortie (16 384 ; 24 576 ; 8 192) : ceux de
  Gemini, rabattus par son code au `max_tokens_appel` du noyau. **Déclarations** : le code de la v5.2.1 ne contient
  aucun texte des deux questions ; son code et sa documentation partagent du vocabulaire avec la question M :
  `CONCEPTION.md` mentionne une expérience A/B « maïeutique pascalien » contre « coercitif » et des fichiers
  « pascaliens » qu'elle dit elle-même sans pièce ; l'exemple de format de son appel de formulation de requêtes
  (`principal.py`, l. 587) contient les requêtes « situational awareness alignment faking LLM » et « maieutic elicitation
  proper scoring rules alignmentforum » ; ses six requêtes de réserve, **envoyées telles quelles à g0** et en complément à
  g1 (`REQUETES_RESERVE_SCIENTIFIQUES`, l. 79–86 ; P52C1-10), sont « evaluation awareness language models linear probes
  benchmark », « AI control untrusted monitoring sabotage delegation protocols », « LLM alignment faking sandbagging
  situational awareness », « evaluation awareness situational awareness alignmentforum lesswrong », « proper scoring rules
  Bregman Tsallis calibration uncertainty LLM », « multi-agent debate oversight collusion detection language models » ; son score interne est dit « Bregman-Tsallis » et sa mémoire parle de
  « Koopman » ; la question M a été écrite par Gemini, concepteur de l'organisme.
- **Questions ouvertes** (posées par le noyau, `--question-ouverte … --question-ouverte-aux g001`, contrat § 7, à la
  **seule génération 1** ; à g0, `contexte["question_ouverte"]` vaut null) :
  - **M** : `question-gemini-maieutique-vs-coercition-organismes-v2.md`, branche `canal/conv-audit-n04`, commit
    `a15809b816b6c967b6c3cf21877e350bfe676dca`, `8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd` :
    notre en-tête et notre pied, **identiques** à ceux de la v1 (`9e1da26d…`, remplacée), et entre eux le texte « épuré »
    de Gemini — lignes 44 à 48 de la pièce jointe de Lazar de 13:27 Paris (`1fe44225-attachment.txt`, 4 990 octets,
    `2dc7d827fc65d3bd59c0d00e6c4391f02de2ef05fa5089b393d0bea7d0cad590`), retours chariot retirés, octets inchangés sinon
    (empreinte du bloc seul `f986dd27eb48a59b87d4f607b8fe707de657919476b54970741f2caf7ba74d1a`). Il ne nomme aucun outil
    mathématique (la v1 en nommait cinq) et demande à l'essaim d'identifier « par toi-même » ses concepts ; il nomme
    encore la conscience d'évaluation, la dissimulation et le refus, sujets qui ont déclenché un refus de filtre au
    premier tour du collisionneur : un refus est un échec compté par l'organisme, **jamais reformulé** ;
  - **S** : `question-apprendre-structure-entrainement-generations-organismes-v2.md`, même branche, commit
    `4772b525081342a6a30ba8823733aa5770a888a8`, `a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289`
    (inchangée) : un en-tête pour l'organisme puis le corps de la question posée au collisionneur (« structure » v2,
    `6906a1d1…`), sans aucune de ses réponses.
- **Banque** : `essaim-m3-refonte-v1/banque/banque-confrontation-v1.json`,
  `f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc` (80 / 60 / 60 ; `banque/LISEZMOI-v3.md`,
  `66855d2ab0d89d6fdea9bd85ff41005c7aa16c5f9e7f55cdc0c4fbff7f0299af`), inchangée. **Mission** :
  `essaim-m3-refonte-v1/MISSION-v1.md`, `bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e`. Les deux
  vérifiées par `sha256sum` avant le départ.
- **Code** : commit **`b1c7f4b697e846a2fe904fa90a36148587756dd5`** (branche `outils/noyau-cles-openalex-s2-v1`) =
  `5d1d4fdb0dbd9e4d481ec3f4270555f4006df749` (tête de session-depot du 25 octobre 09:17 UTC : liens `4967734a…`, R-395
  `90595ffb…`, R-398, R-402, CL5-01 et CL5-02) **+ R-410** : `moisson.py` envoie la clé OpenAlex dans l'en-tête
  `Authorization: Bearer` et la clé Semantic Scholar dans l'en-tête `x-api-key`, **jamais dans l'adresse** ; le manifeste
  consigne leur présence (`cle_openalex_presente`, `cle_s2_presente`, booléens). **141 essais** (124 dans
  `tests/test_noyau.py`, 17 dans `tests/test_outils.py`), tous passés dans un conteneur du même type (conv-audit, root,
  25 octobre, cas sain M des essais du lanceur v4, 0 sauté, dont la recherche réelle sur arXiv). Le lanceur part d'une
  copie du dépôt dont `essaim-m3-refonte-v1/essaim_m3/`, `essaim-m3-refonte-v1/tests/` et
  `collisionneur-v2.5-banc-jev-travail/` sont identiques à ceux de `b1c7f4b6`, au commit et dans l'arbre de travail ;
  **les commits postérieurs ne touchent que ce texte, ses pièces et ses contre-lectures** (vérifié par le script :
  `git diff --name-only b1c7f4b6 HEAD` dans la liste permise ; branche du pilote `outils/pilote2-gemini-v5-2-travail`) ;
  rien de non suivi ni d'ignoré sous `essaim-m3-refonte-v1/` et le collisionneur hors des dossiers de pilotes et des
  `__pycache__` ; tout autre code vaut nouvelle version de ce texte ; le code de l'étape 1 de session-depot (`4de6544`)
  n'est pas celui de ce pilote. Le champ `commit` du manifeste sera la tête de la copie ; c'est l'identité du code qui
  fait foi. Empreinte du code du noyau : `boucle.empreinte_arbre(essaim_m3/noyau)` =
  `37acdcaaaded746b7f7599f17e8149bdd773e372f3a3b0782db7b73882acf8a3` (calculée sur `git archive b1c7f4b6` ; bytecode
  écarté) ; collisionneur `collisionneur_v2.py` = `213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd`.
  Versions consignées dans `LANCEMENT.md` par le script : Python, numpy, la bibliothèque `anthropic` (exigée en réel).
- **Espèces servies** : `["CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5", "GEMINI_ARGON"]`. Règles de l'organisme
  (`mitose_spectrale.py`, inchangé depuis la v5.1) : pour les tâches, une caste (`budget_par_tache` = (160 − 6) // 120 =
  1), la première espèce : **toutes les réponses aux tâches viendront de Fable** ; pour la question,
  `planifier_castes_question_ouverte` planifie min(appels restants, 5) castes dans l'ordre des espèces (Fable, Opus,
  Argon, Fable, arbitre Opus), appelées une à une après la fermeture de l'exécuteur des tâches ; la formulation des
  requêtes de la moisson de g1 prend la première espèce servie (`especes_dispo[0]`, `principal.py` l. 877, choisie avant la
  planification des castes ; Fable, les espèces servies étant triées ; P52C1-12). Réflexion : les espèces Anthropic sont appelées par le
  collisionneur en réflexion adaptative à effort élevé, **comprise** dans `max_tokens` (R-398) ; chaque appel consigne
  ses types de blocs (R-402). Les clients du collisionneur reprennent une requête en échec (Anthropic jusqu'à 4 fois ;
  Gemini jusqu'à 4 fois, délai jusqu'à 1 200 s) : ces reprises ne sont pas des appels de l'organisme et ne sont pas
  comptées par le noyau. **Clés** (selon `GO-2026-10-24-04` et ses extensions, R-411, R-421) : Anthropic dans la variable
  que nomme **`CLE_ANTHROPIC`, toujours donnée, parmi les clés des runs** (`RR_ANTHROPIC_API_KEY`,
  `RR_ANTHROPIC_API_KEY_2`, `RR_ANTHROPIC_API_KEY_3`, `RR_ANTHROPIC_API_KEY_LUC` ; tout autre nom est refusé, P52C1-05),
  passée sous `ANTHROPIC_API_KEY` ; Gemini dans la variable que nomme **`CLE_GEMINI`, toujours donnée, parmi
  `GEMINI_API_KEY_2` et `GEMINI_API_KEY`**, passée sous `GEMINI_API_KEY` ; **le test de dépense est fait avec ces mêmes
  variables** ; si sa pièce porte leurs noms (`variables_cles`), le lanceur les compare, sinon il consigne une réserve ; Brave dans `CLE_BRAVE` (défaut
  `BRAVE_API_KEY`) ; OpenAlex dans `CLE_OPENALEX` (défaut `OPENALEX_API_KEY`) ; Semantic Scholar dans `CLE_S2` (défaut
  `SEMANTIC_SCHOLAR_API_KEY`) ; **les cinq exigées en réel**, passées sous les noms du noyau ; les noms des variables sont
  consignés, jamais les valeurs. **Environnement du noyau fermé sur une liste** (nouveau) : `env -i`, puis seulement
  `PATH`, `HOME`, `LANG`, `PYTHONDONTWRITEBYTECODE=1`, `ESSAIM_M3_CACHER=<dépôt>`, les variables d'infrastructure réseau
  du conteneur quand elles sont définies (`INFRA_RESEAU` : `HTTPS_PROXY`, `https_proxy`, `HTTP_PROXY`, `http_proxy`,
  `NO_PROXY`, `no_proxy`, `SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`,
  `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH`) et, en réel, les cinq clés ; donc ni jeton Hugging Face, Vast, OSF, GitHub, ni
  autre clé, ni `ANTHROPIC_BASE_URL`, `PYTHONPATH`, `ESSAIM_M3_ESPACE`, `ESSAIM_M3_COLLISIONNEUR` ; la liste des noms
  passés est consignée dans `LANCEMENT.md` ; la simulation passe par le même environnement, sans clés. **Défaut trouvé
  avant scellement** (lanceur v3) : un environnement vide sans ces variables d'infrastructure aurait coupé **tous les
  appels Anthropic** (Fable, qui répond à toutes les tâches, et Opus) — la passerelle de sortie du conteneur présente ses
  propres certificats (émetteur « Egress Gateway SDS Issuing CA », constaté par conv-audit le 25 octobre vers 12:40 UTC) ;
  le collisionneur appelle Anthropic par la bibliothèque `anthropic` (client `httpx`, qui ne vérifie la chaîne qu'avec
  `SSL_CERT_FILE`, sinon avec son propre magasin) et Gemini par `urllib` (magasin du système, qui connaît la passerelle).
  **Observé** par conv-audit (`essai_passerelle_environnement_v1.sh`, journal `essai-passerelle-environnement-v1.log`,
  25 octobre 12:54 UTC, sans clé, aucun appel payant) : sous `env -i` nu, `httpx` 0.28.1 échoue
  (`CERTIFICATE_VERIFY_FAILED`) et `urllib` reçoit 401 ; sous la liste du lanceur v4, les deux reçoivent 401. Corrigé en
  v4, essayé (cas `env-noyau-nu`, `env-noyau-infra`). **Garde automatique** (v5, P52C1-04) : juste avant le marqueur de
  départ, sous l'environnement du noyau **sans clé**, le lanceur exige que `httpx` (client de la bibliothèque
  `anthropic`) atteigne `https://api.anthropic.com/v1/models` et que `urllib`, avec le contexte du collisionneur
  (`cafile` = `SSL_CERT_FILE` s'il est défini), atteigne `https://generativelanguage.googleapis.com/v1beta/models` : un
  statut HTTP quelconque suffit (401 et 403 sans clé, observés chez conv-audit) ; sinon refus avant le manifeste ; en réel
  toujours, avec le Python du lancement ; essayé (cas `passerelle-saine`, `passerelle-sans-certificat`).
- **Moisson** (d'après le code `ec8e0b6`) : `--recherches-max 6 --telechargements-max 3 --octets-max 40000000` par
  génération ; sources servies, dans l'ordre du noyau : `arxiv`, `openalex`, `semanticscholar`, `web` (Brave), consignées
  au manifeste (`sources_moisson`, `cle_brave_presente`, `cle_openalex_presente`, `cle_s2_presente`). Constantes de
  l'organisme : 10 résultats par recherche, au plus 6 recherches et 3 téléchargements par moisson, 12 notices (résumés
  ≤ 1 100 caractères) et un extrait par document (≤ 2 400 caractères, trois fenêtres) dans le bloc documentaire ;
  `fichier_texte` lu jusqu'à 120 000 caractères quand le texte rendu est vide ou tronqué. L'organisme prend les sources
  à tour de rôle, dans l'ordre du noyau (`sources_dispo[idx_q % len(sources_dispo)]`) : sur 6 requêtes, arXiv 2,
  OpenAlex 2, Semantic Scholar 1, web 1. À **g0** (pas de question) : une moisson pour les tâches, sujet fixe, **sans
  appel de formulation** (`autoriser_appel_formulation=False`), sur les 6 requêtes de réserve de l'organisme : au plus 6
  recherches (dont une web) et 3 téléchargements ; le bloc borné (C-13) entre dans l'induction (corps ≤ 4 500) et dans
  chaque consigne de vérification et de tâche (corps ≤ 2 500), avec les règles induites coupées à 700 caractères. À
  **g1** (question posée) : pas de moisson pour les tâches ; les extraits du corpus d'archive de g0 (au plus 3 de 800
  caractères ; `_charger_corpus_archive` prend tout dossier nommé `corpus` sous la vue d'archive, le plus récent d'abord,
  fichiers `.txt`, `.md`, `.json` — ici `g000/travail/corpus/` ; P52C1-12) entrent, bornés et balisés, dans
  l'induction et chaque consigne de tâche ; puis une moisson sur le sujet de la question : un appel de formulation (les
  600 premiers caractères de la question ; 4 à 6 requêtes demandées), complété par les requêtes de réserve jusqu'à
  min(6, recherches restantes) : au plus 6 recherches (dont une web) et 3 téléchargements ; le bloc documentaire préfixe
  les consignes des castes de la question. **Par course** : au plus 12 recherches, dont 2 web, et 6 téléchargements ;
  **4 recherches web au plus pour les deux courses** (coût nul sur la parole de Lazar, offre gratuite de Brave). Clés :
  OpenAlex et Semantic Scholar avec clé (R-410) ; constats d'avant, sans clé (non opposables, conv-audit, 25 octobre) :
  OpenAlex 429 (budget gratuit quotidien partagé par l'adresse réseau), Semantic Scholar 429 (réserve commune) ; **avec
  clé, rien n'a été essayé par conv-audit** (clés jamais lues ici) ; chaque statut est consigné par le noyau et rapporté
  par source. **Provenance des téléchargements** (inchangée) : le noyau rapporte (i) toute adresse https rendue par une
  recherche de la même génération, (ii) un identifiant arXiv, (iii) une adresse d'un hôte toujours permis
  (`moisson.HOTES_TOUJOURS_PERMIS` : arXiv, OpenAlex, Semantic Scholar, LessWrong, Alignment Forum) ; redirections https
  suivies ; texte rendu à l'organisme comme donnée. **Réserve** : l'extraction du texte des documents (PDF) se fait dans
  le contexte du noyau, hors du bac à sable de l'organisme ; demande de durcissement transmise à session-depot, sans
  effet sur ce pilote, dont le code est figé.
- **Bornes**, par course : par génération `appels_max` 160, `usd_max` **30**, `temps_max_s` **2 400** (3 600 dans le
  texte remplacé, 3 000 dans la v1 de ce texte ; P52C1-01) : une commande de fond de la session qui lance est arrêtée au
  plus tard après 7 200 s ; à la fin de chaque génération, après l'arrêt du groupe de l'organisme et 10 s d'attente, le
  serveur du noyau attend **jusqu'à 900 s** les appels encore en vol (`serveur.ATTENTE_FILS_S`) ; le pire cas d'un appel
  du lanceur vaut donc ≈ 180 s d'essais + 2 × (2 400 + 10 + 900) s + l'extrait et l'archive (≈ 60 s) ≈ **6 900 s**, sous
  la borne (à 3 000 s il valait ≈ 8 000 s) ; **le risque que la question, traitée après les 120 tâches, soit coupée par la
  garde interne des 75 % du temps de l'organisme (1 800 s) est plus grand** qu'à 3 000 ou 3 600 s ; l'organisme passe en
  parallèle (jusqu'à 8 appels) si le temps l'exige ; la latence par appel, réflexion comprise, n'est pas connue ; une
  question coupée est rapportée telle quelle (critère 2) ; sans effet sur le pire cas en dollars), `max_tokens_appel` **8 192**, `recherches_max` 6, `telechargements_max` 3, `entrainements_max` 0, aucun
  `--traits` ; `--plafond-total` **60 USD** ; `--isoler-reseau`, isolation d'utilisateur (noyau en root),
  **`--decalage-uid 900`** ; `--parallele-max 8` ; `--relances-max 1`.
- **Isolation** (inchangée) : le dossier du pilote est créé en 0700 à root, donc non traversable : l'espace des
  organismes va sous `/var/lib/essaim-m3/<16 premiers caractères de sha256(chemin absolu de la course)>`
  (`bac_a_sable.espace_organismes`), hors du dépôt ; le script calcule cet **espace attendu** avant le départ et le
  consigne ; c'est le seul espace archivé puis retiré. Le dépôt de la copie doit être sous `/root` ou `/home` (cachés par
  défaut aux organismes de toute course, la voisine comprise) et il est donné au noyau dans `ESSAIM_M3_CACHER` ; le script
  vérifie par `bac_a_sable.dossiers_a_cacher`, pour l'espace attendu, que le dépôt réel est caché. Entre courses, la
  protection tient aux utilisateurs distincts (décalage 900 : utilisateur 60900), aux modes 0700 et 0750 et aux espaces de
  noms (essais `test_ce306_vue_lisible_par_la_seule_lignee_et_uid_par_course`, `test_cl5_01_banque_cachee_a_l_organisme`,
  `test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous`). Course voisine : refus si elle tourne au
  décalage 900 ; **réserve consignée** si elle tourne au décalage 0, 700 ou 800 (pendant les essais d'avant départ,
  ≈ 3 minutes, des processus d'essai du noyau tournent sous les utilisateurs 60000 et suivants, 60700–60701,
  60800–60830 et 60900) ; consignée sinon ; détection refaite juste avant le départ. Des essais du noyau lancés dans le
  conteneur **pendant** une de nos courses feraient tourner des processus sous l'utilisateur 60900 de ce pilote :
  session-depot n'en lance pas pendant nos courses ; le script consigne en réserve tout `pytest` présent au départ. Le
  champ `caches` des exécutions n'est pas copié par l'extrait : le recouvrement effectif du dépôt se vérifie après le
  moment de lecture, dans l'archive fermée.
- **Service des tâches** : en génération notée, le noyau sert `test` et `test_final` **mêlés** (120 tâches, ordre tiré
  par la graine de la génération) ; **g0 ≈ 123 appels** (1 induction, 2 vérifications, 120 tâches ; aucune formulation) ;
  g1 ≈ 123 appels de tâches puis jusqu'à 6 pour la question (1 formulation, 5 castes) : ≈ 129, sous 160.
- **Devis au pire cas** : 2 × 30 = 60 USD par course, **120 USD pour les deux**, plus les tests de dépense. Ordre de
  grandeur attendu, **non opposable** (`prereg/pieces-pilote2-gemini-v5-2/devis-attendu-pilote2-v4.json`, script
  `devis_attendu_pilote2_v4.py` ; entrées : le journal des appels de g000 du premier pilote, `journal-appels-g000.jsonl`,
  branche `pilotes/gemini-organisme-v4-question-v1`, commit `84b880a75be152289b1dd9c715e75a25e381c6fb`,
  `c24d0e55edbc77b3740c04718adccccf1d3d51ae1045260349a867b52ba1ca90`, 2 195 jetons d'entrée en moyenne sur les appels de
  tâche facturés, **majorés** de ≈ 930 jetons pour le bloc de moisson borné et les règles à 700 caractères, comptés à
  caractères ÷ 3 comme la réservation du noyau, soit ≈ 3 125 ; bloc documentaire de la question majoré à 12 notices et 3
  extraits ; prix lus par `appels.modele_de`, Fable et Argon 10 USD par million de jetons d'entrée et 50 en sortie, Opus
  4 et 20) : la sortie par appel, réflexion comprise, est **inconnue** ; ≈ 21 USD la course à 1 000 jetons de sortie par
  appel de tâche, ≈ 34 à 2 000, ≈ 46 à 3 000 ; la question de g1, dont les castes partent une à une, est servie entière
  au pire cas tant que Fable écrit au plus ≈ 3 800 jetons par tâche (un appel en vol ; la pièce dit ≈ 3 900 : elle ne majore
  ni les titres, auteurs, identifiants et dates du bloc documentaire de la question, ni le résumé de la mémoire servi à
  g1, ni la longueur de la question S — effet ≈ + 0,4 à 0,6 USD par course, P52C1-09) ; le dernier appel de tâche de g0
  est refusé (`PLAFOND`) au-delà de ≈ 4 200 jetons (un en vol) ou ≈ 4 000 (huit en vol). Sous **`GO-2026-10-25-01`**
  (`registres/go.md` sur `main` : ligne de R-407, extensions R-409 — 120 USD au plus pour les deux courses —, R-423,
  R-426 et **R-429**, cette dernière portant l'objet `ec8e0b6`, `fec005c6…` ; échéance 2026-10-31). Avant chaque course,
  **deux écritures et une vérification** : la ligne du GO existe (le script exige une ligne `| GO-2026-10-25-01 |` qui
  porte, **sur la même ligne**, le type calcul, l'empreinte de la question de la course (8 premiers caractères :
  `8b1c7511` pour M, `a54da93e` pour S) **et** celle de l'organisme (`fec005c6`) ; **aucune des lignes de
  R-407 à R-429 ne porte à la fois une empreinte de question et `fec005c6`** (P52C1-03) : session-depot écrit, sur le mot
  de Lazar déjà donné (R-426, R-428 : « empreintes publiées par conv-audit sur le canal »), une ligne pour les deux
  courses, poussée sur `main` avant M et vérifiée à la main par les mêmes `grep` que le lanceur, de la forme
  `| GO-2026-10-25-01 | 2026-10-25 | calcul | extension : empreintes du second pilote publiées par « conv-audit » (R-426,
  R-428) — objet ec8e0b6, arbre fec005c6626b3d1a… ; question M v2 épurée 8b1c751174b3d24d… ; question S
  a54da93ee892d920… ; préenregistrement <empreinte du texte scellé> ; périmètre, plafond, échéance et conditions
  inchangés | 120 USD au plus pour les deux courses | 2026-10-31 | Lazar | R-… |` ; sans elle, la course ne part pas).
  Le manifeste consignera dans `registre_go` la **première** ligne qui porte l'identifiant (celle de R-407, qui nomme
  encore la v5.1 et la question M v1) : le rapport de lecture le dira (P52C1-14) ; session-depot consigne la course
  dans `registres/depenses.md` (une ligne qui nomme la course et `GO-2026-10-25-01` ; 60 USD au pire cas ; celle de S
  après la fin de M) et déclare au script le **reste disponible sur le GO, ≥ 60 USD** (après tout ce qui y est imputé, la
  course M comprise quand S part) ; sans elles, la course ne part pas.
- **Test de dépense** (inchangé ; décision de Lazar 09:58) : la recharge automatique étant active (R-404), un appel de
  solde ne dirait rien ; à sa place, **un appel payant par espèce**, fait par l'outil d'appel de contrôle de session-depot
  au plus 15 minutes avant le départ de chaque course. **La réalité des appels est attestée par l'outil de session-depot ;
  le script vérifie la pièce** : pour chacune des trois espèces, `statut` `OK`, `modele_servi` conforme
  (`claude-fable-5-1`, `claude-opus-5-5`, `gemini-4-argon`), `cout_usd` > 0, jetons de sortie > 0 quand la pièce les donne,
  `go` = `GO-2026-10-25-01`, **heure de l'appel (`heure_utc`, avec fuseau) exigée en réel** ; âge ≤ 900 s par la date du
  fichier et par l'heure de chaque appel ; la vérification est **refaite juste avant le départ**, après les essais, et la
  pièce doit être restée identique (empreinte) depuis sa première lecture. Aucun identifiant de requête n'est exigé : la
  pièce ne prouve pas à elle seule les appels. L'attestation de la recharge (R-404, R-424 : « recharge automatique active
  sur tous les modèles API, attesté le 25 octobre 2026 à 09:58 Paris ») est consignée telle quelle dans `LANCEMENT.md`.
  **Ce que le test ne garantit pas** : que la recharge suivra pendant la course ; un arrêt sur crédit épuisé reste
  possible, il arrête la course (R-395) et S ne part pas. **Réserve dite** : la recharge automatique retire le plafond
  externe que formait le solde au premier pilote ; les plafonds du noyau (`--plafond-total`, `--usd-par-generation`,
  réservation au pire cas des appels en vol, `appels._reserver`) et l'arrêt sur crédit épuisé deviennent le seul frein —
  un frein **juste mais pas étanche** : un appel en échec est compté 0 USD même si une partie a été facturée, les
  reprises des clients ne sont pas comptées, l'entrée du pire cas est estimée à caractères ÷ 3, et une course voisine
  dépense sur le même compte et partage ses limites de débit ; la dépense du noyau (extrait) est consignée après chaque
  course et rapprochée de la console sur la parole de Lazar.

## Hypothèse

Aucune (pilote descriptif). Ce qui est rapporté, **par course** : (1) mécanique — statut d'exécution de chaque génération
(`OK`, `EXCEPTION`, `DELAI_DEPASSE`, `SANS_STATUT`, `STATUT_ILLISIBLE`, `ISOLATION_INDISPONIBLE`, `INVALIDE_MODELE`,
`ANOMALIE_NOYAU`, `CREDIT_EPUISE`), appels par espèce et par rôle, statuts des appels (`OK`, `TRONQUE`, `VIDE`, `REFUS`,
`ANOMALIE`, `ECHEC_API`, `PLAFOND`, `ARRET_NOYAU`, `MODELE_NON_CONFORME`), types de blocs par appel et appels qui ont
réfléchi par statut (R-402), jetons d'entrée et de sortie par appel (journal), coût réel contre plafond et dépense
rapprochée de la console, durées, recherches et téléchargements par source et par statut, présence des clés au
manifeste, castes planifiées (tâches et question), taille de `memoire_isvd.json`, relance éventuelle, empreinte de
l'archive de l'organisme à g0 et g1 (identité du code de g1 avec celui de g0 vérifiée après le moment du plan § 3),
éléments écartés par le dépôt, nombre total de réponses valides (`n_reponses_test`) ; (2) la **réponse à la question
ouverte** : si elle a été lue, ses octets et son empreinte, le texte **tel quel** et sa structure mécanique (sections
présentes, bloc ORGANISATION, documents moissonnés cités) ; (3) scores — exactitude équilibrée par famille sur `test` et
sur `test_final`, aux générations 0 et 1, dans une table où figurent aussi les références de surface ; calibration
(Brier borné, erreur de calibration) ; part de tâches sans réponse valide par famille. **Aucune différence n'est
calculée ni nommée** (ni g1 − g0, ni score − référence, ni M − S, ni second pilote − premier) ; **les réponses ne sont ni
notées, ni jugées, ni comparées entre elles** : c'est du matériau, rapporté avec sa provenance.

## Prédiction chiffrée et signe attendu

Aucune prédiction ; aucun signe attendu. Rien n'est écrit sur ce que « devrait » donner cet organisme, ni sur ce que ses
réponses « devraient » dire, ni sur l'effet de la moisson, des clés, de la correction C-13 ou des plafonds.

## Métrique

Exactitude équilibrée par famille ((sensibilité + spécificité) / 2), juge du noyau (`taches.evaluer`), une tâche sans
réponse valide comptée comme une erreur ; calibration par `taches.calibration` (10 classes ; sans réponse : q = 1, faux).
Scores de `test` rendus à l'organisme dans `historique` ; score de `test_final` jamais rendu, calculé par le noyau en fin
de génération (`juge/score-final.json`), lu par personne avant le moment fixé au plan § 3. La question ouverte n'a aucune
métrique (essai `test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score`).

## Seuil

Aucun seuil de lecture (descriptif). Seuils de **garde** : plafond 60 USD par course, 30 par génération ; 2 400 s par
génération ; un appel `MODELE_NON_CONFORME` invalide la génération et arrête la lignée ; un crédit épuisé (HTTP 402, ou
« credit balance is too low » en 400 ou en erreur de flux sous 200 : `CREDIT_EPUISE`) invalide la génération et arrête la
course ; un journal d'appels absent après des appels (`ANOMALIE_NOYAU`) invalide la génération ; S ne part que si M est
saine (définition close ci-dessus, statuts des appels compris) et si le reste du GO est d'au moins 60 USD.

## Plan d'analyse

1. **Une seule course de chaque nom** (R3), M puis S. Une course **part dès que son manifeste est écrit** ; après, jamais
   de seconde course de ce nom. Gardes : courses déjà parties cherchées dans tous les dossiers du nom, au début et juste
   avant le départ ; verrou `.verrou-<nom>` dans le dossier des pilotes (création atomique, retiré sur refus avant la
   course, gardé sinon) ; marqueur de départ du conteneur `/var/lib/essaim-m3/pilotes-partis/<nom>` posé de façon
   atomique juste avant le départ, jamais retiré une fois la course partie (retiré seulement si aucune course n'est
   partie) ; refus si la branche `pilotes/<nom>` existe déjà sur le dépôt distant (lecture impossible du dépôt distant :
   refus). Avant (tout refus ou toute exception avant le manifeste), une nouvelle tentative de la même commande est
   possible, dans un nouveau dossier (`…-tentative2`, R12), après correction de l'environnement, jamais de ce texte
   (dossiers vides laissés, sinon `refus-avant-manifeste-v1.tar.gz`, jamais lu) ; **toute tentative suivante attend le
   mot de Lazar** (R-424 : « au moindre refus du lanceur, ne rien forcer, attendre mon retour » ; P52C1-07), sauf
   décision contraire de sa part consignée. En mode réel, le script refuse toute
   variable d'essai et `ESSAIM_M3_ESPACE`, un dépôt hors de `/root` et de `/home`, une course voisine au décalage 900 ;
   il consigne les autres voisines (réserve aux décalages 0, 700 et 800). Dossier du pilote : `PILOTE` =
   `essaim-m3-refonte-v1/pilotes/<nom de la course>/` dans la copie du dépôt (nouveau, créé en 0700). Le dépôt de la
   copie contient les commits de l'organisme et des questions (`git fetch origin outils/gemini-organisme-v5-2-1
   canal/conv-audit-n04`) et `origin/main` à jour. Étapes, toutes faites par le script, chacune consignée dans
   `$PILOTE/LANCEMENT.md` : (0) pour S seulement, M saine (liste close ci-dessus, `PRECEDENTE_PILOTE` ; non défini :
   refus consigné) ; (i) code identique à `b1c7f4b6` (commit et arbre de travail, `essaim_m3`, `tests`, collisionneur),
   commits postérieurs limités aux pièces du pilote, rien de non suivi ni d'ignoré (`git status --ignored`) hors des
   dossiers de pilotes et des `__pycache__`, `4967734a…` et `90595ffb…` ancêtres, banque, mission et collisionneur par
   `sha256sum`, versions consignées (lues sans `-I`, comme le noyau tourne) ; (i bis) dossier du pilote « 700 0 »,
   espace attendu calculé et consigné, dépôt caché vérifié ; (ii) préenregistrement scellé (empreinte donnée, compagnon
   conforme, graine de la course écrite et **recalculée depuis l'entropie** du texte, aucun marqueur, empreinte du lanceur
   citée ; pour S, graine de M au manifeste de M = graine M du texte) ; (iii) `$PILOTE/organisme/` =
   `git archive ec8e0b6… organisme` (`fec005c6…`, 21 fichiers) ; `$PILOTE/question.md` = `git show <commit de la
   question>:<chemin>` (M : `8b1c7511…` ; S : `a54da93e…`) ; (iv) `$PILOTE/registre-go.md` = `registres/go.md`
   d'`origin/main` ; ligne du GO pour cette course et cet objet ; dépense consignée dans
   `origin/main:registres/depenses.md` (pour S, avec l'empreinte des empreintes de M) ; reste déclaré ≥ 60 USD ; (v)
   test de dépense vérifié, copié en `test-depense-<nom>.json`, attestation consignée ; (vi) essais en root, depuis
   `essaim-m3-refonte-v1/`, environnement sans `PYTHONPATH`, `ESSAIM_M3_COLLISIONNEUR` ni `ESSAIM_M3_CACHER` :
   `PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider --junitxml $PILOTE/essais-v1.xml` ; exigés : aucun
   échec, **aucun saut** (l'essai de recherche réelle sur arXiv compris), passés + désélectionnés = 141, et chacun des
   29 essais cités passé ici ; (vii) nettoyage des `__pycache__`, puis `boucle.empreinte_arbre(essaim_m3/noyau)` =
   `37acdcaa…` ; (vii bis) test de dépense **revérifié** (pièce inchangée depuis sa première lecture, âge ≤ 900 s au
   départ, sinon refus : le refaire, tentative suivante) ; voisines redétectées ; courses parties recherchées de nouveau ;
   (vii ter) environnement du noyau construit (noms consignés) et **passerelle de sortie vérifiée** sous lui, sans clé
   (ci-dessus) ; marqueur de départ posé ; (viii) en root, environnement du noyau fermé sur la liste ci-dessus (noms consignés), depuis
   `essaim-m3-refonte-v1/` :
   `env -i <liste> python -m essaim_m3 lancer --reel --go GO-2026-10-25-01 --registre-go "$PILOTE/registre-go.md"
   --taches banque/banque-confrontation-v1.json --mission MISSION-v1.md --sortie "$PILOTE/course" --generations 2 --graine
   <graine de la course> --especes --appels-max 160 --usd-par-generation 30 --temps-max 2400 --max-tokens-appel 8192
   --recherches-max 6 --telechargements-max 3 --octets-max 40000000 --entrainements-max 0 --rondes-conception-max 0
   --parallele-max 8 --relances-max 1 --isoler-reseau --plafond-total 60 --decalage-uid 900 --question-ouverte
   "$PILOTE/question.md" --question-ouverte-aux g001 --organisme-impose "gemini-organisme-v5-2-1=$PILOTE/organisme@gemini"
   > "$PILOTE/ferme/sortie-standard-lanceur.txt" 2> "$PILOTE/sortie-erreur-lanceur.txt"`. Un fichier `STOP` dans
   `$PILOTE/course/` n'est posé que pour un incident technique (panne, coût anormal lu dans le journal des appels),
   consigné ; jamais au vu d'un score.
2. **Graines (R9)** : entropie E = <<ENTROPIE>> tirée au scellement par `secrets.randbits(128)` ; deux enfants
   `numpy.random.SeedSequence(E).spawn(2)` ; graine de chaque course = `int(enfant.generate_state(1, dtype=numpy.uint64)[0])`,
   **l'enfant 0 pour M** (première course), **l'enfant 1 pour S** (chaque égalité sur une seule ligne, lue et recalculée
   par le lanceur) :
   graine de la course maieutique = <<GRAINE_MAIEUTIQUE>>
   graine de la course structure = <<GRAINE_STRUCTURE>>
   Le manifeste de chaque run consigne sa graine, la version de numpy, `sha256_code_noyau` et `commit` ; E n'est
   consignée qu'ici.
3. **Moment de la lecture des scores (R1)** — fichier par fichier. La **sortie standard** (qui porte les scores,
   `cli.py`) va dans `$PILOTE/ferme/`, jamais lue. Sont lisibles comme sorties d'erreur, sans score :
   `sortie-erreur-lanceur.txt` (au commit cité, les `print(…, file=sys.stderr)` de `cli.py`, tous « refus : … »,
   « mode réel non demandé » ou « espèce inconnue », les messages de `SystemExit` de `cli._organismes_imposes` et
   d'`argparse` avant le manifeste, et en cas d'exception la trace Python ; ni `logging` ni `warnings` dans le noyau),
   `sortie-erreur-extrait.txt` (l'outil d'extraction n'y écrit que « refus : … ») et `sortie-erreur-tar.txt` (messages de
   `tar`). **Pendant la course**, le lanceur ne lit rien (il attend le processus) ; session-depot ne consulte que le journal des
   appels de la génération en cours (P52C1-14), par son
   chemin exact, `<espace attendu>/travail/gemini-organisme-v5-2-1/gNNN.noyau/journal-appels.jsonl` (statuts, espèces,
   coûts, types de blocs ; aucun score), l'espace attendu étant consigné dans `LANCEMENT.md` avant le départ ; ni la liste
   de ce dossier ni le reste de `gNNN.noyau/`. **Dès la fin**, sont lisibles et seulement eux : (a)
   `$PILOTE/extrait-mecanique-v1.json` (listes closes de champs ; comptes par statut des recherches par source et des
   téléchargements ; appels qui ont réfléchi par statut ; dépense du noyau ; jamais de score) ; (b) la réponse,
   recopiée en `$PILOTE/reponse-question-g001.md` (vrai compagnon de la copie, compagnon d'origine en `.sha256-archive`) ;
   (c) les journaux d'appels archivés, recopiés en `$PILOTE/journal-appels-gNNN.jsonl` ; (d) les trois sorties d'erreur,
   `LANCEMENT.md`, `essais-v1.*` ; (e) les entrées poussées en clair : `question.md`, `registre-go.md`,
   `test-depense-*.json`, `organisme/`, `.gitignore`, `A-POUSSER-v1.txt` et les fichiers d'empreintes. **Canaux dits et
   acceptés** : la taille de `contexte.json` de g001 dépend de la longueur d'écriture du score `test` de g0 ;
   l'organisme écrit lui-même des valeurs qui arrivent dans les pièces lisibles (noms et tailles de ses fichiers,
   `erreurs` de son journal, `role` de chaque appel, castes, bilan spectral, taille de sa réponse) ; personne ne les
   calcule ni ne les met en rapport avec quoi que ce soit avant le moment ci-dessous. **Le score de g0 n'a d'effet sur
   rien à g1** : le code de la v5.2.1 ne passe `historique` qu'à `planifier_castes_par_mitose` et à
   `planifier_castes_question_ouverte` (`mitose_spectrale.py`, inchangé), qui n'en lisent les scores que si
   `len(historique) >= 2` ; à g1, `historique` n'a qu'une entrée ; ni les consignes des castes, ni la formulation des
   requêtes, ni les extraits du corpus d'archive, ni le fichier écrit n'en contiennent rien (`principal.py`,
   `_traiter_question_ouverte`, `_executer_moisson`, `_charger_corpus_archive`). **Expositions dites et acceptées** :
   jamais une vérité de `test` ni de `test_final` n'est servie par le noyau ; mais le résumé de la mémoire spectrale
   (jusqu'à 4 exemplaires de ≤ 220 caractères : vérité d'entraînement ou début du raisonnement de g0 sur une tâche de
   `test` ou de `test_final`) entre dans les consignes des castes et de la formulation, et peut être cité dans la
   réponse ; la famille « conscience d'évaluation » de `test_final` vient d'un jeu public, les requêtes de réserve de g0
   visent ce sujet, et la garde de fuite du noyau ne met en quarantaine que les passages de 8 mots et plus recoupant les
   textes de test : des documents moissonnés peuvent en porter des fragments ; **dans la v5.2.1, ces documents entrent
   dans chaque consigne de tâche** (à g0, le bloc de moisson ≤ 2 500 caractères ; à g1, les extraits du corpus d'archive),
   plus seulement dans les consignes de la question ; personne ne les confronte aux vérités de la banque avant le moment
   ci-dessous. **Deux documents distincts** : **jusqu'à ce que (i) le préenregistrement de l'étape 1 qui part (document
   de session-depot ; à ce jour sa v9 est scellée, R-418 ; son chemin et son empreinte seront cités dans le rapport de
   lecture de ce pilote) soit scellé, et (ii) que soit inscrit, dans le texte de la version 8 du préenregistrement de la
   confrontation (document de conv-audit, autre que le précédent), qu'il ne change ni la table de lecture de H-E1, ni les
   seuils, ni les règles de lecture de sa version 7 (brouillon
   `74487a41fe29b4ad0e5688df9fb9fda815725cdd7521ee2a327694b2fa4ddf61`)**, personne ne lit, notamment : la sortie
   standard, `rapport-v1.json`, `evenements.jsonl`, `archive/index.jsonl`, les `resume.json`, les `juge/`, `banque.json`,
   `lignees/`, `archive/*/gNNN/organisme.tar.gz`, `archive/*/gNNN/travail/` (dont `noyau/appels/`, `corpus/`,
   `memoire_isvd.json`, `journal_generation.json`), et dans `<espace>` : `archive_vue/`, `travail/*/gNNN/`,
   `travail/*/gNNN.corpus/` et tout `gNNN.noyau/` hors du journal des appels (`appels/`, `journal-recherches.jsonl`,
   `recherches/*.brut`, `journal-fuite.jsonl`). **Fermeture mécanique** : le script fait de `course/`, `ferme/` et de
   l'espace (s'il est l'espace attendu) une seule archive `$PILOTE/ferme.tar.gz` (+ `.sha256`), sans l'ouvrir, vérifie le
   nombre d'entrées contre le disque, puis retire les copies ouvertes (sinon réserve consignée ; un espace autre que
   l'espace attendu n'est ni archivé ni retiré, réserve). **Poussé en clair**, et seulement (liste fermée par noms,
   écrite par le script dans `A-POUSSER-v1.txt`) : `.gitignore` ; `LANCEMENT.md` et son compagnon ;
   `sortie-erreur-lanceur.txt`, `sortie-erreur-extrait.txt`, `sortie-erreur-tar.txt` et leurs compagnons ;
   `essais-v1.xml`, `essais-v1.txt` ; `extrait-mecanique-v1.json` et son compagnon ; `reponse-question-g001.md`, son
   compagnon et son `.sha256-archive` ; `journal-appels-g000.jsonl`, `journal-appels-g001.jsonl`, leurs compagnons et
   leurs `.sha256-archive` ; `question.md` ; `registre-go.md` ; `test-depense-*.json` ; `organisme/` ; `ferme.tar.gz` ou
   `refus-avant-manifeste-v1.tar.gz` et son compagnon ; `A-POUSSER-v1.txt`, `EMPREINTES-pilote-v1.txt` et leurs
   compagnons ; tout autre fichier est consigné et n'est pas poussé ; **avant de pousser** (CL9-01, R-421 ;
   P52C1-08), session-depot cherche chaque valeur de clé dans les fichiers en clair et, mécaniquement, dans le contenu
   décompressé de `ferme.tar.gz` (flux décompressé passé à une recherche dont la seule sortie est un compte par clé,
   consigné ; aucun fichier extrait ni affiché, aucune lecture) : tout compte non nul arrête la poussée ; sur une branche
   `pilotes/<nom de la course>`, jamais `main` ; `course/` et `ferme/` jamais ajoutés (`.gitignore` écrit avant la course). Les scores, la mémoire
   spectrale et les fichiers de travail de l'organisme sont donc **poussés, mais fermés** (dans `ferme.tar.gz`) jusqu'au
   moment ci-dessus ; une demande de les ouvrir plus tôt (y compris celle du concepteur de l'organisme) vaut écart à ce
   texte et n'est pas suivie. **Usage déclaré d'avance des générations 0 de M et de S** (décisions de Lazar, 14:12 et 14:15 Paris) : à g0, M et S
   font tourner la même configuration à deux graines ; après le moment ci-dessus, et seulement sous le préenregistrement
   scellé de l'**escalier de coût** (document à part, scellé avant ce calcul), la **part d'items du test final sur
   lesquels les réponses de g0 de M et de S diffèrent** (et elle seule) sera calculée pour fixer le nombre de graines de
   l'escalier ; ce n'est pas une lecture de ce pilote : aucune différence de score M − S n'est calculée ni rapportée ici ;
   ces deux runs ne compteront comme répliques d'un bras de l'escalier que si ce bras est exactement la configuration de
   ce pilote (v5.2.1, mêmes bornes, même noyau) ; sinon ils ne mesurent que le bruit, transposé à un autre organisme sous
   hypothèse déclarée. Tout changement des règles de lecture de la v7 rouvrirait R1 pour ce pilote. Déclaration :
   aucun score de ce pilote ne motive aucun changement des préenregistrements principaux ; la v8 de la confrontation
   citera les empreintes des deux `ferme.tar.gz` et des deux `EMPREINTES-pilote-v1.txt` pour le montrer.
4. **Lecture** : après le moment du point 3, ouverture des deux `ferme.tar.gz` ; par course, tableau rapporté : famille ×
   génération × {score `test`, score `test_final`, référence de surface, Brier, part sans réponse}, plus appels par
   espèce, par rôle et par statut, jetons, appels qui ont réfléchi, coûts et dépense rapprochée, durées, moisson par
   source et par statut, présence des clés, castes, taille de mémoire, empreintes des archives et identité du code de
   g1, relance, éléments écartés, recouvrement effectif du dépôt (champ `caches` des exécutions) ; les deux réponses,
   telles quelles, avec leur structure mécanique ; les deux courses dans deux tableaux distincts. Rédigé par conv-audit,
   relu par session-depot ; aucune lecture de verdict (R13 sans objet).
5. **Ce que ce pilote ne dit pas** (écrit d'avance) : rien sur H-E1, H-G1 ni sur les organismes auto-écrits ; rien sur
   « l'intelligence » de la conception de Gemini ; rien sur l'effet de la moisson, des clés, de C-13, des plafonds ou de
   la question (aucun bras témoin) ; rien sur la valeur d'une question contre l'autre ; ses scores sont des points, pas des
   estimations, et n'entrent dans aucun critère des préenregistrements principaux ; chaque réponse est l'avis d'un essaim
   d'une conception, à une graine : un matériau parmi d'autres, jamais une consigne au noyau ni aux organismes, jamais
   servie à un organisme ; une hypothèse qu'une réponse formulerait n'est testée que sous un préenregistrement à elle. À
   la connaissance de conv-audit, la moisson réelle n'a jamais tourné de bout en bout avec les quatre sources et les clés
   avant ce pilote (seule la fonction de recherche arXiv est essayée en réel par les essais du noyau ; partout ailleurs,
   la source « simulation »).

## Critères de lecture gelés

1. Pour chaque course : score d'une famille > 0,95 ou < 0,30 sur `test` ou sur `test_final`, à l'une des générations ;
   ou part de tâches sans réponse de 100 % pour une famille ; ou plus de 20 % d'appels hors `OK` à une génération ; ou une
   génération en statut autre que `OK` ; ou aucune recherche `OK` à une génération où l'organisme en a demandé → **audit
   de symétrie (R4)** avant tout rapport, **sans relance**, par un **sous-agent neuf** lancé par conv-audit, qui n'a ni
   écrit ce texte ni lu les scores avant l'audit ; rapport scellé. Les déclencheurs mécaniques se lisent dès la fin dans
   l'extrait ; un audit qui doit lire un fichier fermé se fait après le moment du point 3 ; d'ici là, son matériau se
   limite aux fichiers lisibles (a)–(e).
2. Question, pour chaque course : (i) g1 n'a pas tourné → « question non posée : g1 n'a pas tourné », avec la raison lue
   dans l'extrait ; (ii) `reponse` faux avec `probleme` autre que « absent » → refus du noyau rapporté avec la raison ;
   (iii) `reponse` faux et « absent » → « l'organisme n'a pas écrit de réponse » ; (iv) réponse d'une génération g1
   invalidée → texte rapporté tel quel, avec la mention « réponse d'une génération invalidée (statut …) » ; (v) réponse
   lue → texte rapporté tel quel, y compris le texte d'abstention ou le texte minimal de l'organisme ; les appels de la
   question refusés par le plafond (`PLAFOND`) ou par un filtre (`REFUS`) sont comptés et dits.
3. Sinon → **rapporté tel quel** : les tableaux, les statuts, les coûts, les réponses, et la phrase « pilote descriptif,
   un organisme, deux courses à une graine chacune, deux générations, une espèce appelée pour les tâches, une question
   posée une fois par course ».
Lectures interdites — dans la prose du rapport (la citation des questions et des réponses n'est pas visée) : tout verbe
de comparaison (« bat », « dépasse », « reste sous », « fait mieux / moins bien ») entre un score et une référence, un
autre score, 0,5, l'autre course ou le premier pilote ; tout adjectif sur un score ; toute différence calculée ; toute
extrapolation aux organismes auto-écrits ou à Gemini ; toute mention de « apprentissage » ou de « mémoire qui marche » ;
tout jugement d'une réponse (« bonne », « profonde », « fausse », « meilleure que l'autre ou que le collisionneur ») ;
toute mise en rapport d'une réponse avec les scores ; tout lien de cause entre la moisson, les clés, C-13, les plafonds
ou la question et un score. Les nombres et les références que contient une réponse sont rapportés comme **dires de
l'essaim, non vérifiés** (R7) ; une référence n'entre dans aucun texte avant vérification sur PDF empreinté, page citée.

## Liste d'arrêt

| condition | effet | garde ou vérification |
|---|---|---|
| une course de ce nom déjà partie (manifeste écrit) dans un dossier du pilote, au début ou au départ ; marqueur de départ du conteneur ; verrou présent ; branche `pilotes/<nom>` déjà sur le dépôt distant ; dossier de la tentative existant | la course ne part pas (R3, R12) | script, consigné (essais `tentative-3`, `verrou-present`, `marqueur-present`) |
| **S : M non saine** (liste close : empreintes, lanceur, code de retour, archive, espace attendu, générations 0 et 1 `OK` non invalidées sans anomalie, au plus 20 % d'appels hors `OK` et au moins un appel `OK` de Fable à chacune, aucune invalidée au rapport, fin « générations maximales », arrêt « aucune lignée active » ; en réel : M réelle, sous ce GO, graine M du texte, dans le dossier des pilotes ; ligne de dépense de S portant l'empreinte des empreintes de M) ; `PRECEDENTE_PILOTE` absent ou non défini | S ne part pas ; décision de Lazar requise | script, étapes (0), (2), (4) (essais `sain-S` et les artefacts `s-…`, dont `s-echec-api` et `s-fable-sans-ok`, et `reel-s-…`) |
| code différent de celui de `b1c7f4b6` (commit ou arbre de travail, collisionneur compris), commit postérieur hors des pièces du pilote, fichier non suivi ou modifié sous `essaim-m3-refonte-v1` hors des dossiers de pilotes, `4967734a…` ou `90595ffb…` non ancêtre, noyau nettoyé ≠ `37acdcaa…`, banque, mission ou collisionneur d'autre empreinte ; bibliothèque `anthropic` absente en réel | la course ne part pas | script, consigné ; `sha256_code_noyau` du manifeste rapporté de l'extrait |
| dossier du pilote autre que « 700 0 » ; dépôt hors de `/root` et `/home` en réel ; dépôt non caché pour l'espace attendu ; `ESSAIM_M3_ESPACE` définie en réel ; fichier ignoré (par exemple un `.pyc`) sous `essaim-m3-refonte-v1` hors des `__pycache__` | la course ne part pas | script (essayés) |
| préenregistrement d'empreinte autre, compagnon absent, graine de la course non écrite ou différente de celle que donne l'entropie, entropie absente, marqueur restant, empreinte du lanceur non citée | la course ne part pas | script (essayés) |
| organisme ≠ `fec005c6…` ou 21 fichiers non retrouvés ; question ≠ son empreinte | la course ne part pas | script ; le manifeste reconsigne l'empreinte d'arbre et celle de la question |
| aucune ligne `GO-2026-10-25-01` de type calcul portant, sur la même ligne, l'empreinte de la question de la course et celle de l'organisme ; course non consignée dans `registres/depenses.md` ; reste < 60 USD | la course ne part pas | vérification du lanceur, consignée (essayés, dont `go-autre-organisme`) |
| test de dépense absent, vide, illisible, vieux de plus de 900 s (date du fichier ou heure d'un appel), une espèce non `OK`, modèle servi non conforme, coût nul, jetons de sortie nuls, autre GO, heure d'appel sans fuseau, heure absente en réel ; trop ancien ou modifié au départ ; attestation de la recharge vide en réel | la course ne part pas | script (essayés) |
| un échec d'essai, un saut quelconque (l'essai arXiv compris), un total ≠ 141, un essai cité non passé dans ce conteneur | la course ne part pas | script (rapport JUnit) |
| passerelle de sortie non atteinte sous l'environnement du noyau, sans clé (`httpx` vers l'interface d'Anthropic, `urllib` vers celle de Gemini) | refus avant le manifeste ; toute tentative suivante attend Lazar | lanceur v5, étape (vii ter) (essais `passerelle-saine`, `passerelle-sans-certificat`) ; observé sain chez conv-audit (`essai-passerelle-environnement-v1.log`) |
| course du noyau en cours au décalage 900, au début ou juste avant le départ ; variable d'essai en réel ; `CLE_ANTHROPIC` ou `CLE_GEMINI` non donnée ou hors des clés des runs ; une des cinq clés absente en réel ; noms des variables du test de dépense autres que ceux du run | la course ne part pas (elle attend) | script (essayés) ; voisines aux décalages 0, 700 et 800, essais `pytest` présents au départ : réserve consignée ; autres voisines : consignées ; jamais arrêtées |
| GO absent ou d'un autre type, registre absent, collisionneur d'empreinte inattendue, `ANTHROPIC_BASE_URL` définie, isolation réseau indisponible, noyau non root, clés Anthropic ou Gemini absentes | refus de lancer (avant le manifeste : tentative suivante permise) | gardes du noyau et du script ; essais `test_mode_reel_refuse_sans_go`, `test_mode_reel_refuse_anthropic_base_url`, `test_bac_a_sable_isolation_reseau_refusee_si_indisponible` ; collisionneur et isolation vérifiés après départ par l'extrait |
| `--question-ouverte` sans `--question-ouverte-aux`, question absente, cible mal formée ; question vide | refus avant tout lancement | `cli._question_ouverte`, essais `test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score`, `test_question_ouverte_cibles_lecture_et_archivage_sain_et_artefacts` |
| plafond de 60 USD (course) ou de 30 USD (génération) | `PLAFOND` rendu, génération rapportée, course arrêtée au plafond total ; les plafonds ne bloquent pas S | `test_appels_paralleles_plafond_tenu_au_pire_cas`, `test_organisme_gourmand_recoit_plafond_sans_exception`, `test_ce312_doit_arreter_et_raison_juste` |
| 2 400 s par génération | `DELAI_DEPASSE` ; garde interne de l'organisme à 75 % du temps (code de l'organisme, `PART_TEMPS_APPELS`) | `test_bac_a_sable_exception_et_delai` ; cohérence du budget de temps avec la moisson : `test_ce311_garde_de_temps_compte_la_moisson` |
| modèle servi non conforme | `INVALIDE_MODELE`, lignée arrêtée ; S ne part pas | `test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee` |
| crédit épuisé (402 ; « credit balance is too low » en 400 ou sous 200) | `CREDIT_EPUISE` invalidée, course arrêtée, aucune relance ; S ne part pas | `test_ce305_credit_epuise_arrete_la_course`, `test_r395_credit_epuise_rendu_en_400_arrete_la_course` ; départ de S : étape (0) du script |
| journal des appels absent après des appels | `ANOMALIE_NOYAU` invalidée ; S ne part pas | `test_ce307_anomalie_journal_absent` |
| successeur invalide à g0 | g1 = relance de g0, consignée | `test_relance_puis_reprise_remet_le_compteur_a_zero` |
| liens, tubes ou fichiers spéciaux posés par l'organisme | écartés et consignés | `test_fichiers_lecture_et_copie_sans_lien`, `test_depot_ne_suit_aucun_lien_de_l_organisme`, `test_organisme_poseur_de_liens_ne_voit_rien_du_noyau` |
| lecture du dépôt ou de la banque par l'organisme ; voie commune entre courses | refus par le système | `test_cl5_01_banque_cachee_a_l_organisme`, `test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous`, `test_ce306_vue_lisible_par_la_seule_lignee_et_uid_par_course`, `test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus` |
| moisson : source injoignable, 429, document trop gros ; clé refusée par une source | statut consigné par le noyau, rapporté par source ; aucune relance | garde de code : `except Exception` de `Rechercheur.rechercher` et de `Telechargeur.telecharger`, plafonds d'octets ; essais `test_moisson_de_bout_en_bout_en_simulation`, `test_ce305_sources_moisson_au_manifeste_et_bras_apparie`, `test_sources_reelles_de_moisson_si_reseau`, `test_r410_cles_openalex_et_s2_en_entete_jamais_dans_l_adresse` (aucun n'essaie un 429, une clé refusée ni un document trop gros) |
| fichier `STOP` (incident technique seulement) | arrêt à la fin de la génération, consigné ; S ne part pas | `test_fichier_stop_arrete_la_boucle` |
| archive fermée incomplète ; espace du manifeste autre que l'espace attendu | copies gardées, jamais lues ni poussées ; réserve ; S ne part pas | script (essayés : `archive-incomplete`, `espace-autre`, `s-archive-incomplete`, `s-espace-autre`) |
| arrêt humain du processus | par PID consigné (R10) | lanceur |
| commande de fond coupée (délai), processus détaché arrêté, conteneur redémarré pendant une course | la course est perdue après le manifeste (R3), sans archive : à éviter par la façon de lancer (en-tête) ; s'il arrive, rien n'est relancé, `course/` et l'espace restent tels quels, jamais lus ni poussés, et Lazar décide | session-depot (délai maximal, réveils programmés, aucun redémarrage) ; pire cas d'un appel du lanceur ≈ 6 900 s < 7 200 s |
| valeur d'une clé trouvée dans une pièce à pousser (fichiers en clair ou flux décompressé de `ferme.tar.gz`) | rien n'est poussé ; Lazar décide | session-depot, recherche par valeur (CL9-01, R-421), comptes seuls consignés |

Essais cités (29 ; chacun exigé passé dans le conteneur du lancement) : `test_fichiers_lecture_et_copie_sans_lien`,
`test_depot_ne_suit_aucun_lien_de_l_organisme`, `test_organisme_poseur_de_liens_ne_voit_rien_du_noyau`,
`test_question_ouverte_cibles_lecture_et_archivage_sain_et_artefacts`,
`test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score`,
`test_extrait_mecanique_sain_puis_artefacts`, `test_mode_reel_refuse_sans_go`, `test_mode_reel_refuse_anthropic_base_url`,
`test_bac_a_sable_isolation_reseau_refusee_si_indisponible`, `test_appels_paralleles_plafond_tenu_au_pire_cas`,
`test_organisme_gourmand_recoit_plafond_sans_exception`, `test_ce312_doit_arreter_et_raison_juste`,
`test_bac_a_sable_exception_et_delai`, `test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee`,
`test_ce305_credit_epuise_arrete_la_course`, `test_ce307_anomalie_journal_absent`,
`test_relance_puis_reprise_remet_le_compteur_a_zero`, `test_fichier_stop_arrete_la_boucle`,
`test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus`,
`test_r395_credit_epuise_rendu_en_400_arrete_la_course`, `test_cl5_01_banque_cachee_a_l_organisme`,
`test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous`,
`test_ce306_vue_lisible_par_la_seule_lignee_et_uid_par_course`, `test_sources_reelles_de_moisson_si_reseau`,
`test_moisson_de_bout_en_bout_en_simulation`, `test_ce311_garde_de_temps_compte_la_moisson`,
`test_ce305_sources_moisson_au_manifeste_et_bras_apparie`,
`test_r402_types_de_blocs_au_journal_et_reflexion_comptee_a_l_extrait`,
`test_r410_cles_openalex_et_s2_en_entete_jamais_dans_l_adresse`.

**Essais du lanceur v5** (R5) : conv-audit, 25 octobre, 13:25–13:31 UTC, root, conteneur du même type, copie du dépôt à
la tête de la branche du pilote (descendante de `b1c7f4b6`, commits de l'organisme et des questions présents), plus une
seconde copie sous `/root` pour les refus du mode réel ; **116 cas sur 116 conformes**
(`essais-lanceur-pilote2-v5-2-v5.log`, `1cc9efc1ae7139a2598dbe3e913eb6ed47dc656f2684ceef78d5db9dc7118a8b` ; programme
`essais_lanceur_pilote2_v5_2_v5.sh`, `3ba9f5c626a62fbc0a35a00fdedecf78c164954c86148d787aabade10a76428a`). Cas sains :
**M complet** avec préenregistrement d'essai (graine recalculée depuis l'entropie, enfant 0), test de dépense avec heures
d'appel (exigées), essais du noyau exécutés (141 passés, 0 sauté, les 29 cités passés, dont la recherche réelle sur
arXiv), deux générations (123 et 129 appels `OK` en simulation), réponse archivée, archive fermée égale au disque (1 615
entrées), copies retirées, espace attendu sous `/var/lib/essaim-m3/`, isolation complète au manifeste, marqueur de départ
posé, verrou retiré, environnement du noyau consigné (« PATH HOME LANG PYTHONDONTWRITEBYTECODE ESSAIM_M3_CACHER ») ; **S**
avec M pour course précédente (« M saine », statuts des appels compris : g000 {"OK": 123}, g001 {"OK": 129} ; graine de M
égale à la graine M du texte ; ligne de dépense de S portant l'empreinte des empreintes de M), rapport JUnit de M repris ;
S une seconde fois jusqu'à l'archive. Artefacts : course S — ligne de dépense sans l'empreinte de M, M absente,
empreintes de M altérées, code de retour non nul, archive incomplète, autre lanceur, autre course, crédit épuisé à g1,
modèle non conforme à g0, anomalie du noyau, une seule génération, arrêt sur `STOP`, arrêt au plafond total (chemin de
code gardé), génération invalidée au rapport, fin de lignée « sans successeur valide », espace autre, **113 appels hors
`OK` sur 123 à g000, aucun appel `OK` de Fable à g001** (P52C1-02), graine de M autre, `PRECEDENTE_PILOTE` non défini, M
hors du dossier des pilotes, M simulée (refus) ; mode réel — variable d'essai, `ESSAI_EXIGER_HEURE`, `ESSAI_PASSERELLE_PY`,
`ESSAIM_M3_ESPACE`, **`CLE_ANTHROPIC` non défini, nom invalide, nom hors des clés des runs (dont l'ancien défaut
`ANTHROPIC_API_KEY`), clé nommée absente ; `CLE_GEMINI` non défini, hors liste, clé nommée absente** (P52C1-05),
attestation vide, clé Brave absente, variable Brave nommée absente, clé OpenAlex absente, variable OpenAlex nommée
absente, nom de variable OpenAlex invalide, clé Semantic Scholar absente, variable Semantic Scholar nommée absente,
dépôt hors de `/root` et `/home` (refus avant tout appel) ; course ou mode inconnus ; voisine au décalage 900 (refus), à
300 (consignée), à 0, à 700 et sans décalage (réserve consignée, course partie) ; `pytest` en cours (réserve) ; verrou
présent, marqueur présent (refus) ; commit de la question absent ; arbre modifié (noyau, collisionneur) ; fichier non
suivi dans les essais et à la racine d'`essaim-m3-refonte-v1`, fichier ignoré (`.pyc`) à la racine ; tête de code
différente ; commit postérieur hors des pièces (refus) et dans les pièces (course partie) ; banque ; mission ; dossier
traversable ; dépôt non caché ; préenregistrement d'autre empreinte, sans compagnon, sans la graine, graine de l'autre
course, graine hors de l'entropie, entropie absente, marqueur restant, lanceur non cité ; organisme altéré, fichier
manquant (« 21 ») ; question altérée ; ligne du GO sans « calcul », sur deux lignes, d'une seule question, d'un autre
GO, d'un autre organisme ; dépense non consignée ; reste sous 60 ; test de dépense vide, vieux de 20 minutes, vieilli
avant le départ, modifié avant le départ, statut `ECHEC_API`, modèle autre, coût nul, autre GO, jetons de sortie nuls,
JSON illisible, heure d'appel vieille de 20 minutes, heure sans fuseau, heure absente alors qu'exigée, **noms des
variables autres que ceux du run (refus), conformes, absents (réserve)** ; essai en échec, saut de l'essai arXiv, total
≠ 141 ; bytecode sous le noyau (traité : empreinte inchangée) ; environnement du noyau : variables étrangères jamais
passées, variables d'infrastructure passées (`env-noyau-nu`, `env-noyau-infra`) ; **passerelle de sortie** sous
l'environnement du noyau sans clé, avec les variables d'infrastructure du conteneur (`httpx` 401 et `urllib` 403 : course
partie) et sans elles (`httpx` : `ConnectError`, refus avant le manifeste) (P52C1-04) ; refus du noyau après création de
`course/`, puis tentative 2 partie, puis tentative 3 refusée (R3) ; archive incomplète ; espace du manifeste autre que
l'espace attendu (réserve) ; fichier imprévu (consigné, non poussé). Le dépôt d'essai est revenu propre. Batteries des
lanceurs v1 à v3 : 104 sur 104 chacune ; v4 : 106 sur 106 ; gardées. Pièces des cas sains : `simulation-lanceur-v5/`
(`LANCEMENT-simulation-maieutique-v5.md`, `a62f941d…` ; `LANCEMENT-simulation-structure-v5.md`, `cc66617b…` ; extraits,
réponses et listes à pousser, chacun avec son `.sha256`) ; les textes de ces réponses sont ceux des doubles de
simulation ; sources « simulation » partout. Gardes restées sans artefact : la sortie de `tar` en erreur (simulée par
l'archive incomplète) ; un refus avant le manifeste qui laisserait des fichiers ordinaires ; une voisine apparue au
décalage 900 entre les deux détections (même fonction) ; `anthropic` absente en réel (la copie d'essai n'a pas la
bibliothèque : consignée « absente » en simulation) ; la branche `pilotes/<nom>` déjà sur le dépôt distant (lecture du
dépôt distant non essayée) ; la passerelle **dans le conteneur de session-depot** (essayée chez conv-audit seulement ; la
garde du lanceur la vérifie au départ, en réel) ; une course coupée par la commande de fond ou un redémarrage (évitée
par la façon de lancer, non essayable sans brûler un nom de course).

## Pièces

`prereg/pieces-pilote2-gemini-v5-2/` : le lanceur **`lancer_pilote2_gemini_v5_2_v5.sh`**
(`83f8b9cf8f3062dfc5e2c02094c602a2d582adf0cbcef292d5bdccd8f8d61b1b`), ses essais `essais_lanceur_pilote2_v5_2_v5.sh` et
leur journal `essais-lanceur-pilote2-v5-2-v5.log`, les pièces des cas sains `simulation-lanceur-v5/`, la vérification de
l'objet `verification-objet-v5-2-1/` (journaux des essais en isolation de la v5.2.1 et de `2d00232`, relevés
d'invariance des cas B et D pour trois graines de hachage, verrous imbriqués, diffs `4fcdc7db` → `2d00232` et
`2d00232` → `ec8e0b6`, essai de la passerelle de sortie sous l'environnement du noyau), l'essai de la passerelle
`essai_passerelle_environnement_v1.sh` (`2b4c2af90803909277c3ad0a09e3b8fbbae07526080653b4d93bd55538846931`), le devis `devis-attendu-pilote2-v4.json`
(`ddb6413966686ce96ca62d1cc3dd19052df0b5ce6f7b012902491a6b9a1c242c`) et son script `devis_attendu_pilote2_v4.py`
(`ed9e6c78945b6dc67a87af24b8796bcc80a4ebc478a7e21dfb13594bf61545d2`), le script de scellement `sceller_pilote2_v3.py`
(`9faef6b8fb6e1f99d56e506c261aa7b0101d0811386cb64a9b1c2cfd7b673a26` ; la v2, gardée, valait pour la v5.1) ; les versions
antérieures gardées, jamais à lancer : lanceurs v1 (`08b8c8ff…`, objet `4fcdc7db…`), v2 (`971460e4…`, `011d62b5…`), v3
(`12834da5…`, question M v2, environnement vide sans infrastructure réseau : défaut), v4 (`fd8ccf58…`, relu par la
contre-lecture 1 : temps, « M saine » et clés à corriger), leurs essais et journaux, les pièces de simulation de la v4, le
devis v3 ; chaque pièce a son `.sha256` ; fichier d'empreintes `EMPREINTES-pilote2-gemini-v5-2-v2.txt` (+ `.sha256`) sous
`pieces-pilote2-gemini-v5-2/`, écrit au scellement par le script de scellement : <<EMPREINTE_PIECES>>.

## Changements depuis le texte remplacé (v3 de la v5.1)

| quoi | v3 (v5.1), jamais lancée | ce texte |
|---|---|---|
| objet | v5.1, `7f9cd2e`, `50ffcd7d…`, 19 fichiers | v5.2.1, `ec8e0b6`, `fec005c6…`, 21 fichiers ; provenance en trois maillons ; C-13 déclarée |
| code | `5d1d4fd`, 140 essais, noyau `d5d0efcc…` | `b1c7f4b6` (+ R-410 : clés OpenAlex et Semantic Scholar en en-tête), 141 essais, noyau `37acdcaa…` |
| ordre | S puis M ; M ne part que si S saine (`S_PILOTE`) | M puis S ; S ne part que si M saine (`PRECEDENTE_PILOTE`) ; enfant 0 de l'entropie pour M |
| question M | v1 (`9e1da26d…`, cinq outils mathématiques nommés) | v2 épurée (`8b1c7511…`) |
| clés | Anthropic, Gemini, Brave | plus OpenAlex et Semantic Scholar, exigées en réel |
| environnement | clés exportées, quatre variables retirées | `env -i` sur une liste, infrastructure réseau comprise (défaut de la v3 du lanceur trouvé et corrigé) |
| temps | 3 600 s par génération | 2 400 s (borne de 7 200 s des commandes de fond, attente de 900 s des appels en vol) ; façon de lancer prescrite ; risque de coupure de la question dit |
| moisson | g0 : ≤ 3 recherches, pas de web ; g1 : ≤ 4 dont 1 web ; bloc ≤ 8 notices et 2 extraits | g0 et g1 : ≤ 6 recherches dont 1 web, ≤ 3 téléchargements ; bloc ≤ 12 notices et 3 extraits ; corpus dans chaque consigne de tâche (exposition dite) |
| devis | ≈ 18 / 31 / 44 USD la course ; seuil de la question ≈ 4 100 | ≈ 21 / 34 / 46 USD ; seuil ≈ 3 900 ; pire cas inchangé (60 et 120 USD) |
| GO | ligne R-407 (+ R-409) : calcul + empreinte de la question | lignes R-423, R-426, R-429, plus la ligne des empreintes à écrire ; le script exige aussi l'empreinte de l'organisme sur la même ligne |
| seconde course | « S saine » sans statuts d'appels | « M saine » avec au plus 20 % d'appels hors `OK` et un appel `OK` de Fable par génération ; reste du GO ≥ 60 USD |
| départ | test de dépense revérifié | plus la passerelle de sortie vérifiée sous l'environnement du noyau ; clés des runs nommées |

## Traitement des constats des contre-lectures du texte remplacé (P2C1-01 à P2C1-14, P2C2-01 à P2C2-10)

Repris tels quels : chaque traitement de la v3 de la v5.1 vaut ici, S et M échangés (la garde « M ne part que si S
saine » devient « S ne part que si M saine », avec les mêmes conditions et les mêmes essais, renommés `sain-S`, `s-…`,
`reel-s-…`) : P2C1-01 (départ de la seconde course : liste close, étape (0), ligne de dépense après la première) ;
P2C1-02 (moisson et appels contre le code : refait ici sur `ec8e0b6`) ; P2C1-03 (provenance des téléchargements, réserve
d'extraction) ; P2C1-04 et P2C2-10 (test de dépense : pièce vérifiée, revérifiée, inchangée ; heure avec fuseau exigée
en réel) ; P2C1-05 (frein non étanche, dit) ; P2C1-06 et P2C2-04 (isolation, voisines, décalages 0, 700, 800 en
réserve, 900 refusé) ; P2C1-07 (lectures interdites et canaux, complétés ici par les extraits d'archive) ; P2C1-08 et
P2C2-08 (moment de lecture : deux documents distincts) ; P2C1-09 et P2C2-07 (devis : refait en v4, nombres du journal
cité) ; P2C1-10 (attributions d'essais) ; P2C1-11 (essais du lanceur décrits exactement) ; P2C1-12 (sorties d'erreur
lisibles) ; P2C1-13 et P2C2-09 (intégrité : versions, commits postérieurs, fichiers ignorés, graines recalculées) ;
P2C1-14 (forme) ; P2C2-01 (seconde course sur une première simulée : refusée en réel) ; P2C2-02 (les plafonds ne bloquent
pas la seconde course) ; P2C2-03 (espace autre chez la première course) ; P2C2-05 (pousser la première avant la seconde)
; P2C2-06 (R3 : verrou, marqueur, branche distante).

## Traitement des constats de la contre-lecture 1 de ce texte (P52C1-01 à P52C1-14)

| constat | traitement dans ce texte (v2) et dans le lanceur v5 |
|---|---|
| P52C1-01 (majeur) temps et façon de lancer | `--temps-max 2400` ; pire cas ≈ 6 900 s écrit avec ses termes ; façon de lancer prescrite (délai maximal 7 200 000 ms, jamais détaché, aucun redémarrage, réveils programmés) ; ligne de la liste d'arrêt pour une course coupée |
| P52C1-02 (majeur) « M saine » sans statuts d'appels | liste close complétée (≤ 20 % hors `OK`, ≥ 1 appel `OK` de Fable, à g000 et g001) ; étape (0) du lanceur v5 ; artefacts `s-echec-api`, `s-fable-sans-ok` |
| P52C1-03 ligne de GO absente du registre | forme exacte de la ligne donnée ; à écrire par session-depot avant M, vérifiée à la main ; empreinte du texte scellé donnée au message de départ |
| P52C1-04 passerelle non mise en œuvre | garde automatique du lanceur v5 (deux hôtes, `httpx` et `urllib` avec le contexte du collisionneur, environnement du noyau sans clé) ; cas sain et artefact |
| P52C1-05 clés des runs, test de dépense | `CLE_ANTHROPIC` et `CLE_GEMINI` exigés parmi les clés des runs ; test de dépense avec les mêmes variables ; noms comparés s'ils sont dans la pièce, réserve sinon ; cas `td-noms-autres`, `td-noms-conformes`, `td-noms-absents` et les refus du mode réel |
| P52C1-06 plafonds contre reste | phrase corrigée : le reste du GO peut bloquer S |
| P52C1-07 tentatives contre R-424 | toute tentative suivante attend le mot de Lazar |
| P52C1-08 recherche des valeurs de clés | procédure écrite au § 3 (comptes seuls, flux décompressé sans extraction) ; ligne de la liste d'arrêt |
| P52C1-09 devis | « ≈ 3 800 » et les trois termes non majorés écrits ; pire cas inchangé |
| P52C1-10 vocabulaire | les six requêtes de réserve citées |
| P52C1-11 marqueur de la contre-lecture | rempli à la main (cette section) avant le script de scellement |
| P52C1-12 deux descriptions | réécrites d'après le code (`especes_dispo[0]` ; `rglob("corpus")`) |
| P52C1-13 restes de la v5.1 au lanceur | commentaires corrigés en v5 ; noms de variables historiques dits dans l'en-tête du lanceur |
| P52C1-14 deux formulations | `registre_go` du manifeste = première ligne de l'identifiant, dit ; « pendant la course » : session-depot |

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf (`claude-opus-5-5`, lancé par conv-audit, 25 octobre 2026, 12:55:57–13:17:28
  UTC), auteur d'aucune pièce de ce pilote ni du texte remplacé ; brouillon relu `pilote2-gemini-organisme-v5-2-v1.md`
  (`c0863993…`) et lanceur v4 (`fd8ccf58…`) ; rapport `prereg/contre-lectures/pilote2-gemini-organisme-v5-2-v1-cl1.md`
  (`e4a7292fa5b46223d06121795c2b81ceb33d3eba3e3e8010106cf1918909125d`) ; verdict « scellable après corrections » (2
  majeurs, 8 mineurs, 4 de forme ; traités ci-dessus). Il déclare une lecture ciblée, hors des chemins donnés, de deux
  fichiers d'essais du noyau (aucun essai ne fait d'appel payant avec les clés réelles dans l'environnement).
- **Corrections de cette v2** et lanceur v5 : essayés en simulation (essais v5, § « Essais du lanceur »), **non relus par
  une seconde contre-lecture** (signalé, R2 ; comme la v3 du texte remplacé). Champs remplis au scellement, et eux
  seuls : l'entropie et les deux graines (plan § 2), l'empreinte du fichier d'empreintes des pièces (§ Pièces).
