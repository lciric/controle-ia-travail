# Préenregistrement — quatrième pilote descriptif : l'organisme « assisté » de Gemini v6.2, corrigé par conv-audit (v6.2.1), puis la v5.3, chacun seul, sur la banque `confrontation-v3` (identifiants opaques), rondes de conception arrêtées par l'organisme, puis quatre générations notées, en segments — v4

**Statut** : v4, écrite par la lignée conv-audit à partir du 25 octobre 2026, 23:03 UTC (le 26 octobre en heure de Paris ;
heures lues sur `date -u`), sur les décisions de Lazar de 23:54 à 02:17 Paris (§ Décisions) ; récrite à partir de
23:20 UTC pour le second commit de la v6.2, puis à partir de 23:52 UTC pour l'objet corrigé (v6.2.1) et l'ordre inversé
des courses ; complétée à partir de 00:21 UTC le 26 octobre (objet, essais, décisions, après la vérification de la
v6.2.1 et la série v13) ; corrigée à partir de 01:03 UTC, après la contre-lecture 5 et les décisions de 01:48 à 01:56 ; complétée à partir de
01:16 UTC pour les décisions de 02:05 à 02:17 (boucle extérieure, graines, littérature).
**Pilote de conception** (décision de Lazar, 01:56) : le préenregistrement et le scellement ne sont plus exigés pour lui, la
relecture l'est ; ce texte garde sa forme, ses contre-lectures et son script de scellement, dont le lanceur lit les
graines et les empreintes. Elle remplace la v3 **scellée** (`essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v3.md`,
`de7a555932d8e8825a68bd1bd54baff55d08166f84f94d5deb9217312e78c656`, branche `outils/pilote4-gemini-travail`, `d0d0175`),
**jamais lancée** : aucune de ses courses n'est partie, aucune ligne de GO ni de dépense n'a été écrite pour elle (canal
`canal/conv-audit-n04`, message n° 67 ; session-depot, message n° 52, § 4) ; elle reste scellée et gardée, ses graines ne
servent à rien. Contre-lectures : 1 à 4 sur P4v3 (son § Contre-lecture : `3dd09acb…`, `7c625fa6…`, `0d95ea8c…`,
`e2de1372…`), 5 sur ce texte (`914ac3fb…`, « scellable après corrections mineures », traitée) et 6, courte, sur l'écart
depuis la 5 (§ Contre-lecture). Lanceur : lignée session-depot (clés), dans son conteneur.

**Texte différentiel.** Ce texte incorpore par renvoi la v3 scellée, appelée ci-dessous « P4v3 », qui incorpore elle-même
P3 (`pilote3-gemini-organisme-v5-3-v6-v2.md`, `57c8535a…`) et T2 (`pilote2-gemini-organisme-v5-2-v2.md`, `d2944654…`).
Tout ce que ce texte ne dit pas est P4v3, appliqué aux deux courses de ce pilote selon la table de correspondance
ci-dessous ; en cas de conflit, ce texte prévaut. Ce qui change de P4v3 : **l'objet de la course v6.x** (la v6.2.1 à la
place de la v6.1, § Objet, qui remplace ce que P4v3 dit de la v6.1) ; **l'ordre des courses** (la v6.2.1 d'abord, la
v5.3 ensuite, après une v6.2.1 saine) ; et ce qui s'ensuit mécaniquement : porte, lanceur v10, batterie v12 et sa série,
graines, ligne de GO, lignes de dépense, liste d'arrêt, fichier d'empreintes, contre-lectures.

**Ce qui a été lu avant ce texte (R1), à son scellement.** Ce que P4v3 déclare (§ « Ce qui a été lu »), et en plus,
depuis le scellement de P4v3 : le code des commits `fedb065` et `3bbb78c` de Gemini et de la v6.2.1 (`7ea3270`), le
rapport de livraison de Gemini, les deux vérifications (§ Objet) et les journaux des essais des corrections (en isolation,
faux noyau), qui ne lisent aucun score ; les pièces des courses simulées de la série v13 (§ Essais : des simulations,
aucun appel réel) ; le nombre de tâches de chaque part de la banque v3 servie (`banque-confrontation-v3.json`, jamais le
fichier de clé) ; le message n° 52 de session-depot (25 octobre, 22:58 UTC : faits mécaniques du pilote 3 — coûts,
branches, empreintes des listes fermées —, aucun score) ; son message n° 53 et sa pièce sur la course M
(`RAPPORT-M-hypotheses-gpu-v1.md`, `e5150f79…`), qui recopie des scores du second pilote, ceux que P4v3 déclare déjà
avoir lus (son point (a)), et aucun autre ; les lignes R-445 à R-472 du registre des décisions de `main` (`3c94802` ; mots de Lazar,
départs du collisionneur et du test H-M1, prononcé du test H-M1 v3 — R-459 : sa mesure principale déclarée non valide,
aucun verdict —, refus consignés du collisionneur, GO de Lazar sur la primitive d'expérience bornée — R-471 — ; aucun
score d'un pilote) et le brouillon de dessin de cette primitive (`docs/notes/dessin-primitive-experience-v1.md`, `main`
`ce25bcc` ; aucun score) ; les messages n° 55 et 56 de session-depot (26 octobre, 00:36 et 01:03 UTC) et son compte rendu
à Lazar que celui-ci a collé dans la session de conv-audit à 02:10 Paris (coûts et états des tours du collisionneur ;
aucun score) ; les rapports finaux des sous-agents des étapes 1 et 2 et le
brouillon du préenregistrement de l'étape 2 (aucun score) ; les neuf réponses du collisionneur « lecture du pilote »
(branche `donnees/collisionneur-lecture-pilote-v1`, `7ac475b` ; aucun score). Depuis le scellement de P4v3, aucun score du pilote 3, du premier pilote ni d'aucune course réelle n'a été lu, et
du second pilote rien d'autre que ce que P4v3 déclare ; **ce texte est scellé avant toute lecture des scores du
pilote 3**. Aucun score n'a été servi à Gemini.

## Décisions de Lazar

Toutes dans la session de conv-audit (heure de Paris ; fautes de frappe corrigées dans les citations), sauf les mots
écrits dans la session de session-depot, cités d'après son registre. Relevé verbatim, fautes comprises :
`objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v5.md` (§ Pièces ; la v5 reprend les v1 à v4 mot pour mot).

- **25 octobre, 23:54** (= 22:54 UTC), sur l'objet de la seconde course (options : (a) la v6.1, ses points ouverts
  acceptés ; (b) la v5.3 seule, la v6.x plus tard ; (c) tout attendre la v6.2) : « **c) tout attendre la v6.2.** Avantage :
  un seul texte, deux objets sans réserve. Inconvénient : délai inconnu, rien ne part. »
- **26 octobre, 00:15** : « quand la vérif est faite, transmets directement à depot pour qu'il lance le run sur v6, dis-moi
  quoi lui écrire pour qu'il ait mon accord par anticipation ». Conv-audit lui a proposé un mot à écrire dans la session de
  session-depot, qui étend le GO au pilote 4 sur les empreintes que publiera le message de départ (texte scellé, lanceur,
  objet corrigé) et le fait partir dès cette publication, segment après segment, sauf défaut bloquant signalé ; ce mot ne
  vaut qu'écrit par Lazar dans la session de session-depot, et session-depot en tire la ligne d'extension de la forme
  exacte du § Plan, point 1. **Lazar l'a écrit** : R-445 (25 octobre, peu avant 23:25 UTC selon R-446 ; « J'étends
  GO-2026-10-25-02 au pilote 4 : deux courses, la v6.2 d'abord […], puis la v5.3 […]. Elles tournent sous le
  préenregistrement pilote4-gemini-organisme-v4.md scellé et avec le lanceur que conv-audit publiera, avec leurs
  empreintes, dans son message de départ […]. Dès que ce message de départ est publié, inscris la ligne d'extension et les
  lignes de dépense exactement sous la forme qu'il donne, puis lance, segment après segment […]. Si conv-audit signale un
  défaut bloquant de la v6.2, rien ne part et je décide. ») ; puis R-448 (avant 23:41 UTC selon R-449) : « la v6.2.1
  d'abord (la v6.2 de Gemini, 3bbb78c, corrigée par conv-audit ; commit et arbre publiés dans son message de départ) »,
  qui remplace dans R-445 l'objet de la première course. Ses bornes (4 générations ; 6 rondes à 3 USD et 900 s ; 75 USD
  par course ; 60 recherches, dont environ 10 web ; minuteur à 3 400 s ; 185 USD pour le GO, dont 150 pour ce pilote)
  sont celles de ce texte.
- **00:18** : « je veux la v6.2 en premier » : **la v6.2 d'abord, puis la v5.3**.
- **00:27**, sur la recommandation de faire partir la v6.2 avec six réserves écrites : « tu ne peux pas corriger toi-même
  pour lever les réserves stp ? tu as mon accord pour retoucher la version de gemini » : **conv-audit corrige la v6.2
  (v6.2.1, § Objet)**.
- **00:49** : « avance en parallèle sur étape 2 aussi, sur un max de fronts, et oublie pas qu'on teste d'abord les
  versions qui permettent de trancher si les apports supplémentaires de complexification apportent une valeur ajoutée
  au-delà du bruit ». Conv-audit lui a répondu (vers 23:52 UTC) que ce pilote, descriptif (une course par objet, aucune
  différence calculée), ne peut pas trancher cette question — à une course par objet, sur des parts de 36 et 24 tâches,
  un écart de moins de 0,2 à 0,25 entre deux exactitudes reste dans le bruit (ordre de grandeur, non opposable) —, et lui a
  soumis la décision : (a) garder ce pilote descriptif, le plan qui tranche (plusieurs graines par objet) venant du travail
  sur l'étape 2 ; (b) le rendre décisif maintenant (3 graines par objet, texte nouveau, nouveau GO). Recommandé : (a).
- **00:54–00:55** : « (b) […] go », puis « mais a d'abord pour produire des hypothèses testables », puis « puis b » :
  **(a) d'abord — ce texte, descriptif —, pour produire des hypothèses testables, puis (b)**, sous un texte nouveau (trois
  graines par objet, hypothèse et seuil scellés, nouveau GO sur devis, sur le mot direct de Lazar dans la session de
  session-depot ; à 01:48 et 01:52, deux paliers, δ = 0,10, banque v6) ; ce texte ne contient rien de (b). Le moment où les scores de ce pilote pourraient être lus pour écrire les
  hypothèses de (b) a été soumis à Lazar le 25 octobre à 23:56 UTC (options : (1) garder la règle de P4v3 ; (2) et (2')
  un agent neuf lit les scores dès la fin de ce pilote ; (3) écrire (b) sans eux), puis au collisionneur (00:59, « demande
  au collisionneur » ; trois tours sur son mot dans la session de session-depot, R-451, R-452 ; synthèse
  `synthese-collisionneur-lecture-pilote-conv-audit-v1.md`, `a8e1ed64…`, sur le canal) : une course par objet n'apprend
  presque rien à (b) sur le signe de l'effet, et la direction de (b) est donnée par la question de 00:49.
- **01:48** : « Je recommande (3+), confiance moyenne. : go » ((3) en y versant les deux courses de ce pilote comme
  graines) ; plan de (b) en deux paliers et δ = 0,10 : « go » ; leviers (une seule mesure principale, courses
  entrelacées, plus de tâches) : « go a tout ». Puis, **01:52**, sur la banque de (b) : « Banque v6 (lot 3) : deux fois
  plus de tâches, mais il faut attendre qu’elle soit construite, et le pilote 4 ne peut plus compter. : go ». **Les
  hypothèses de (b) sont écrites sans aucun score de ce pilote, et (b) court sur la banque v6 : aucune course de ce pilote
  n'y est versée ; les options (2) et (2') n'existent plus. La fermeture des scores de ce pilote « pour tout usage »
  est remplacée à 01:56, ci-dessous.**
- **01:54 à 01:56** : « il faut s'assurer que le pilote 4 puisse séparer du bruit aussi » ; « et il faut que le pilote 4
  puisse aussi faire ses tests avec des agents sur le noyau » ; puis, à la question de conv-audit sur cette phrase, « je
  lève la règle de prereg et de scellement tant qu'on est dans la phase de conception par essais erreurs, on garde la
  relecture », que Lazar précise par trois choix : la levée vaut pour les **pilotes de conception** sur la banque v3
  (l'étape 1 décisive, la confrontation et (b) sur la v6 gardent le scellement) ; les scores des pilotes **peuvent être
  lus dès la fin d'une course, pour corriger l'organisme**, les expériences décisives se faisant sur des tâches neuves (la
  v6, pas la v5, qui partage ses textes avec la v3), avec une réserve écrite dans leurs textes ; pour ce pilote,
  **relecture puis départ**. Ce texte en suit les conséquences : moment et règles de lecture (§ Plan, point 3, qui
  remplace celui de P4v3 et la fermeture « pour tout usage » de 01:48) ; lecture contre le bruit des tâches (§ Plan,
  point 4 bis : l'option (a) soumise à 01:54, sans course de plus, faute d'un autre mot de Lazar). Les hypothèses de (b)
  restent fixées sans aucun score de ce pilote (01:48). Sur les « agents sur le noyau », Lazar a demandé la
  recommandation de conv-audit et l'avis du collisionneur (01:56) ; ce texte n'en dépend pas.
- **02:05 à 02:17** : « je veux un pilote qui sépare du bruit, pilote 4 le fait-il ? » (02:05) — réponse de conv-audit :
  non, à une course par objet (point 4 bis : dans une course, seuls des changements au-delà du bruit des tâches sont
  lisibles ; aucune comparaison entre objets) ; décision soumise, dépense sans défaut : (a) trois graines par objet
  (quatre courses de plus, lanceur dérivé, texte nouveau), recommandée ; (b) cinq ; (c) garder une course par objet.
  **Sans réponse à l'écriture de ce texte : ce texte garde une course par objet** ; des graines de plus se feraient par
  un texte nouveau (version nouvelle, R12) et un GO nouveau, jamais par ce texte ; ses deux courses n'en seraient les
  premières graines que si ce texte nouveau le dit avant toute lecture de leurs scores. Puis (02:06, renvoyé à 02:07) :
  « et je veux un pilote qui appelle des agents qui font les tests et éliminent les hypothèses fausses et font relancer un
  nouveau tour ou une nouvelle génération de l'organisme » ; décision soumise à 02:07 : (a) une **boucle extérieure**
  entre les courses (agents neufs) puis une **boucle intérieure** dans la course (noyau nouveau) ; (b) l'intérieure
  d'abord ; (c) l'extérieure seule. À 02:10, Lazar a collé le compte rendu de session-depot : son « go » dans la session
  de session-depot (R-471, vers 01:09 UTC) a déjà tranché la boucle intérieure (primitive d'expérience bornée dans le
  noyau, par une version nouvelle du noyau ; « aucun pilote scellé n'est modifié ») ; conv-audit a retiré cette moitié.
  **02:17 : « go » sur (a)**, désormais la boucle extérieure seule : à la fin de chaque course de ce pilote, des agents
  neufs de conv-audit (un analyste, un correcteur, un contre-lecteur) exécutent la lecture des points 3 et 4 bis selon un
  **registre d'hypothèses de conception écrit avant tout score**, statuent par hypothèse (éliminée, tenue, indécidable
  dans le bruit), proposent la ronde suivante ; toute relance est une course nouvelle, nommée et versionnée, sur le mot
  direct de Lazar dans la session de session-depot (dépense). Lazar a aussi demandé la lecture des papiers de telles
  boucles (« The AI Scientist », « AlphaEvolve » et la littérature ; fiche de lecture sur PDF empreinté, R7) et la même
  lecture par le collisionneur (question `question-litterature-boucles-agents-collisionneur-v1.md`, `962130b7…`, canal
  `a65dbfd` ; dépense soumise à son mot). **Ce texte n'en dépend pas** : ses deux courses partent telles quelles, sur le
  noyau `8e5e2f7b` inchangé ; le registre d'hypothèses, le protocole et les briefs des agents sont des pièces nouvelles,
  poussées sur le canal avec leurs empreintes avant la fin de la première course, qui ne modifient ni ce texte ni ses
  règles de lecture ; aucune hypothèse du registre ne porte sur la manière de classer une tâche, et rien du registre ni
  des verdicts des agents n'est servi à un organisme.
- **Lecture si la confrontation change un seuil** (soumise le 25 octobre vers 20:54 UTC ; sans réponse à l'écriture de ce
  texte ; défaut sous 48 heures, l'option (a)) : la règle de P4v3 (§ Plan, point 3 : les scores restent fermés, sauf
  décision de Lazar inscrite avant toute lecture) est cette option (a) ; pour ce pilote, elle est remplacée par la règle
  de 01:56 (§ Plan, point 3) et la question est sans objet ; elle reste ouverte pour les autres textes.
- **Ce que ces mots fixent** : un seul texte, deux courses, la **v6.2.1 puis la v5.3**, mesurées à la même longueur
  (quatre générations notées après une conception d'au plus 6 rondes), sur le même instrument (noyau `8e5e2f7b`, reprise
  par segments, banque v3, lanceur v10) ; rien ne part avant ce texte scellé et le mot de Lazar qui étend le GO ; la
  v6.2.1 ne part que si aucun défaut bloquant ne lui est établi (§ Objet) et que ce mot la nomme ; la v5.3 ne part qu'après
  une course v6.2 de ce pilote finie, fermée et saine (porte « v6.2 précédente », table de correspondance) ; si la v6.2.1
  ne part pas, rien ne part. Les autres décisions que P4v3 cite (75 USD par course, GO à 185 USD, reprise par segments,
  6 rondes, 4 générations, paires gardées, lot 3) restent en vigueur.
- **GO** : `GO-2026-10-25-02` (R-440), étendu par un mot direct de Lazar dans la session de session-depot (forme exacte
  au § Plan, point 1).
- **But** : celui de P4v3, pour les objets v6.2.1 et v5.3 ; rien n'y est tranché sur la valeur d'un ajout de complexité.

## Table de correspondance avec P4v3

| dans P4v3 | pour ce texte |
|---|---|
| seconde course : **v6.1** (`canal/gemini-organisme-v6-1`, commit `a9d8eb50c02c8f5ea31b060b3c0e86f23c2d1dbc`, arbre `ae331d1d…`, 24 fichiers), `COURSE=v6-1`, nom `pilote4-gemini-v6-1-v1`, lignée `gemini-organisme-v6-1` | **première course : la v6.2.1** (branche `canal/conv-audit-organisme-v6-2-1`, commit **`7ea32705c5437d91ed071dd95fb3209bb0b0035e`**, arbre **`4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`**, 26 fichiers), `COURSE=v6-2`, nom `pilote4-gemini-v6-2-v1`, lignée `gemini-organisme-v6-2` (§ Objet) |
| première course : la v5.3 | **seconde course : la v5.3**, objet inchangé (`4ecba58`, arbre `6251ab21…`, 22 fichiers), `COURSE=v5-3`, nom `pilote4-gemini-v5-3-v1` |
| « v6.1 » dans les règles, la liste d'arrêt, les bornes, le devis et les essais | « v6.2 » (la course de la v6.2.1) |
| ce que P4v3 dit du code de la v6.1 (§ Objets : conception, mémoire, générations notées, lignes citées ; § Plan, point 3, canal (d)) | ce que le § Objet dit du code de la v6.2.1, qui le remplace |
| porte « v5.3 précédente » : la v6.1 ne part qu'après une course v5.3 de ce pilote finie, fermée et saine (liste close ; générations notées [0, 1, 2, 3] ; arrêts « fichier STOP » repris, numérotés 2, 3, …, puis « aucune lignée active » ; fin « générations maximales » ; dernier code 0 ; pas de fermeture sans reprise ; même lanceur ; graine du manifeste égale à celle du texte) | **porte « v6.2 précédente »** : la v5.3 ne part qu'après une course v6.2 de ce pilote finie, fermée et saine, selon la même liste close, paramétrée pour la v6.2 (course `v6-2`, nom `pilote4-gemini-v6-2-v1`, lignée `gemini-organisme-v6-2`, variable `PRECEDENTE_V62`) ; la graine de la v6.2 au manifeste est comparée à celle de ce texte. Une v6.2 dont la lignée finit « sans successeur valide » (par exemple un successeur muté invalide à g003 : liste d'arrêt de P4v3, ligne de l'appel `architecte_mutation_endogene`, transposée) est hors de la liste close : la v5.3 ne part pas, Lazar décide |
| la ligne de dépense de la v6.1 porte les empreintes de M et de la v5.3 de ce pilote | la ligne de dépense de la **v5.3** porte les empreintes de M et de la **v6.2** de ce pilote ; celle de la v6.2, celles de M |
| la v6.1 ne part que si le mot de Lazar la nomme (`a9d8eb5`) et accepte ses points ouverts ; sinon seule la v5.3 part | la v6.2.1 ne part que si le mot de Lazar la nomme (R-448 : « la v6.2.1 d'abord », aux commit et arbre du message de départ) et si la ligne d'extension porte son arbre `4f13647a…` ; **aucun point ouvert n'est à accepter** : la vérification de la v6.2.1 ne lui établit aucun défaut bloquant, et ses constats non bloquants sont déclarés au § Objet ; deux choix restent à Lazar (C-14 : un arbitrage qui dépendrait de la confiance ; C-16 : une autre détection que les mots-clés) et quatre constats non bloquants sont dits, qui ne changent rien à ce qui tourne ici (§ Objet) ; R-448 porte l'objet tel quel ; si la ligne ne la nomme pas, **rien ne part** (la v5.3 exige une v6.2 précédente saine) |
| copie de lancement : `git fetch origin canal/gemini-organisme-v5-3 canal/gemini-organisme-v6-1 canal/conv-audit-n04 main` ; tête de `outils/pilote4-gemini-travail` citée au message de départ | `git fetch origin canal/gemini-organisme-v5-3 canal/conv-audit-organisme-v6-2-1 canal/conv-audit-n04 main` ; la tête du scellement de ce texte, citée au message de départ ; le reste de la ligne de P4v3 sans changement |
| lanceur v6 (`lancer_pilote4_gemini_v6.sh`, `50f9c496…`) | **lanceur v10** (`lancer_pilote4_gemini_v10.sh`, `0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952`), dérivé du v6 en quatre pas, chacun par remplacements exacts au nombre attendu : v7 (`cda96923…`, objet v6.2 au premier commit `fedb065`), v8 (`40685089…`, second commit `3bbb78c`), v9 (`6491c940…`, ordre des courses inversé : porte « v6.2 précédente »), v10 (objet v6.2.1) ; les v7 à v9 n'ont jamais servi (§ Essais) |
| batterie v8, série v9 (228 sur 228) | **batterie v12** (`essais_lanceur_pilote4_v12.sh`, `27ef4524b1fa21174a15459645753d31c6ce6cdbc93c24ae0e38a93084800b9a`), dérivée de la v8 en quatre pas (v9 `edb6b12b…`, v10 `b7906684…`, v11 `ba47a625…` — ordre inversé, segments essayés sur la v6.2 —, v12) ; les v9 à v11 n'ont jamais tourné ; **série v13** (§ Essais) |
| entropie et graines `v5-3`, `v6-1` de P4v3 | entropie et graines `v5-3`, `v6-2` de ce texte (§ Plan, point 2), tirées à son scellement (l'enfant 0 pour la v5.3, l'enfant 1 pour la v6.2, quel que soit l'ordre des courses) |
| ligne d'extension de GO, lignes de dépense | § Plan, point 1 |
| script de scellement `sceller_pilote4_v3.py`, `EMPREINTES-pilote4-gemini-v1.txt` | **`sceller_pilote4_v4.py`** (le v3, au nom du fichier d'empreintes près), **`EMPREINTES-pilote4-gemini-v2.txt`** (§ Pièces) |
| phrase du critère 3 | « pilote descriptif, deux organismes (un seul si la v5.3 ne part pas), une course à une graine chacun, une phase de conception arrêtée par l'organisme (6 rondes au plus), quatre générations notées, une espèce appelée pour les tâches, une question posée une fois par course » |
| moment de lecture : après la fin de la dernière course de ce pilote (ou de la v5.3 si la v6.1 ne part pas), sous les conditions (i) et (ii) de P4v3 | **dès la fin de chaque course** (pilote de conception, décision de Lazar de 01:56), selon le § Plan, point 3, qui remplace le point 3 de P4v3 |
| liste d'arrêt : « la v6.1 ne part pas » après une issue de la v5.3 hors de la liste close (dont une génération de la v5.3 à son délai, une course v5.3 arrêtée en cours, au plafond ou fermée sans reprise ; essais `v53-…`, `seg-v53-…`, `seg-clore-v53-refusee`) | « **la v5.3 ne part pas** » après la même issue de la **v6.2** (essais `v62-…`, `seg-v62-…`, `seg-clore-v62-refusee`) ; une issue de la v5.3, seconde course, n'arrête plus rien d'autre qu'elle-même |
| devis (P4v3, § Bornes, devis) : « la course s'arrête au plafond total ; pour la v5.3, la v6.1 ne part pas (porte « v5.3 précédente » ; essai `v53-plafond-total`) » | « la course s'arrête au plafond total ; pour la v6.2, la v5.3 ne part pas (porte « v6.2 précédente » ; essai `v62-plafond-total`) » |
| liste d'arrêt : « ronde de la v5.3 hors `OK` : rapportée ; n'arrête pas la v6.1 (la porte ne lit que les générations notées) » | « ronde de la **v6.2** hors `OK` : rapportée ; n'arrête pas la v5.3 (la porte ne lit que les générations notées) » (liste d'arrêt de ce texte) ; une ronde de la v5.3 hors `OK` est rapportée |
| numéros de lignes du lanceur v6 que P4v3 cite (§ Essais) | décalés dans le v10 de +12 avant l'étape (0 bis) et de +13 après (par exemple v6 l. 206, 256, 504, 512, 804, 821 → v10 l. 218, 268, 517, 525, 817, 834 ; contre-lecture 5) |
| cas sains de la v6.1 en simulation (séries v8 et v9) | cas sains de la v6.2.1, puis de la v5.3 après elle, et segments sur la v6.2.1 (série v13, § Essais) |
| contre-lectures 1 à 4 (sur les v1 à v3) | celles de P4v3, plus celle de ce texte (§ Contre-lecture) |

Tout le reste de P4v3 vaut tel quel : noyau `8e5e2f7b` et reprise par segments, bornes (6 rondes à 3 USD et 900 s,
4 générations à 30 USD et 2 400 s, 75 USD par course tous segments compris, minuteur à 3 400 s, borne de 7 075 s, réveil
de session-depot à l'échéance), devis (75 USD par course, 150 pour les deux ; ordre de grandeur attendu ≈ 30 à 55 USD par
course, non opposable ; marge du GO 185 − 30,23 − 150 ≈ 4,77 USD), banque v3 et ses références (surface, contraste de
paire, provenance), objet v5.3 et ce que P4v3 en dit, canaux dits et acceptés pendant les courses, règles de lecture (tableau, références,
lecture à part du `test_final`), séparation d'avec l'étape 1 et la confrontation ; le moment de lecture est celui du
§ Plan, point 3.

## Objet de la première course : la v6.2.1

Ce paragraphe remplace, pour la v6.2.1, ce que P4v3 dit de la v6.1 (§ Objets, puces « v6.1 », « Ce qui tourne en
conception », « En générations notées », « Correction de P3 » et la phrase sur les numéros de lignes) ; le reste de
§ Objets de P4v3 (v5.3, banque v3, références, sondage du test, ce que T2 et P3 disent des objets) vaut tel quel.

- **Objet** : `organisme-gemini-m3-v6`, version **6.2.1** (manifeste), lignée « assistée » ; branche
  `canal/conv-audit-organisme-v6-2-1`, commit **`7ea32705c5437d91ed071dd95fb3209bb0b0035e`**, dossier `organisme/`,
  **26 fichiers**, empreinte d'arbre **`4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`** (recalculée
  par la vérification et par conv-audit). C'est la v6.2 de Gemini (`3bbb78c1991baf17feb421529fa1957be7edec59`, arbre
  `3b2d8d5a9af75b5457579c847d4ea9510f9da92818805123ed037f7c8436c946`, 24 fichiers), corrigée par conv-audit sur le mot de
  Lazar de 00:27. Six fichiers changent : `principal.py`, `CONCEPTION.md` (§ 2.14 ajouté à la fin, rien d'autre),
  `manifeste.json` (version 6.2.0 → 6.2.1, description), l'essai hérité `tests/test_emprunts_v5_3.py` ; ajoutés
  `CORRECTIONS-v5.md` et `tests/test_corrections_v5.py`. `politique_endogene.py`, `memoire_isvd.py`,
  `mitose_spectrale.py`, `metrique/` et huit des neuf fichiers d'essais sont identiques octet pour octet à ceux de
  `3bbb78c`. Le premier commit de la v6.2, `fedb065` (arbre `d02c2907…`), n'est pas l'objet.
- **Livraison et vérification de la v6.2** : rapport de livraison de Gemini recopié
  (`livraison-gemini-v6-2-recue-2026-10-25-2309-v1.txt`, `e9471860…`, transmis par Lazar à 23:09 UTC) ; vérification par
  un sous-agent neuf (`verification-v6-2-3bbb78c-v1/LISEZMOI-v1.md`,
  `e4ce11c95df2022bf376498b9ff4608e2346f0b9dda85a9e3832461d4609b05f`) : **`3bbb78c` sans défaut bloquant** (53 essais sur
  53 en isolation, deux fois ; V6-01 reste corrigé ; relevés identiques sous les graines de hachage 0, 1 et 2 ; aucun
  appel imbriqué sous `_VERROU` ; gardes C-01 à C-13 ; contrat du noyau) ; des treize points de la demande de v6.2, sept
  levés (1, 2, 6, 8, 11, 12, 13) et six en partie (3, 4, 5, 7, 9, 10) ; `fedb065` avait un défaut bloquant (V62-01 :
  7 essais sur 53 en échec) ; le rapport de livraison est exact sur la provenance et les essais, inexact sur « levé » pour
  les six points partiels, sur un « bornage strict du coût unitaire » et sur 12 des 26 références de lignes.
- **Corrections de conv-audit** (`CORRECTIONS-v5.md` du commit, copie `CORRECTIONS-v5-copie-du-commit-7ea3270.md`,
  `c502a2d8…` ; écart complet `diff-organisme-3bbb78c-vers-7ea3270-v1.txt`, `5bfee6b8…`), lignes de `principal.py` de
  `7ea3270` :
  - **C-14** (point 3, arbitrage dès deux castes) : sans sonde qui vote, `besoin_arbitrage = len(castes) > 1` (l. 1738) :
    **le comportement est celui de la v6.2** : dès deux castes, la délibération s'ouvre, avec l'arrêt anticipé de la
    v6.2 ; choix gardé, avec sa raison écrite (corriger
    sans changer ce que fait l'organisme) ; faire dépendre cet arbitrage de la confiance reste un choix ouvert, à Lazar.
  - **C-15** (point 4, repli sur l'exactitude d'entraînement) : sans exactitude de validation, la sonde d'une famille ne
    vote pas, et la raison est consignée (l. 611–619) ; le routage ne lit que `exactitudes_validation` (l. 1986). L'essai
    hérité de la v5.3 qui attendait l'ancien repli est adapté, et le changement est déclaré ; il se limite à ce que C-15
    exige (vérification).
  - **C-16** (point 5, trois jeux de mots-clés) : une seule source, les constantes de `memoire_isvd.py` (l. 81–82), que le
    gabarit de mutation lit par `_expression_mots_cles` (l. 967–975, employée l. 1082–1083) ; la détection par mots-clés
    est gardée (choix, raison écrite) ; le module initial `politique_endogene.py` garde sa copie (l. 38–39 et 9–10), égale
    à la source (deux essais) ; les successeurs mutés sont identiques octet pour octet à ceux de la v6.2 (vérification).
  - **C-17** (points 7, 9 et 10) : le chemin du code brut de l'architecte est fermé : une réponse qui porte un bloc de code
    définissant `recompense_interne` est refusée et consignée, sans validation ni exécution (l. 1030–1035), même si elle
    porte aussi un objet JSON ; seul l'objet JSON des trois paramètres bornés est accepté (clé absente ou non finie :
    refus, l. 1039–1042, le point 8 de la v6.2 gardé tel quel ; nom du gabarit filtré, l. 1043 ; bornes l. 1044–1046) ; l'assemblage refuse un code muté qui
    porte `import ast` (l. 1558–1562). Par suite, la validation sans borne de temps (7) et la règle impropre entre les
    points lus (9) ne sont plus atteignables : seules les règles du gabarit, à paramètres bornés, atteignent le contrôle
    (seul appel, l. 1102), qui n'a pas changé — il accepterait encore une règle à bonus caché si on la lui donnait ; ce
    que la liste blanche ne garantit pas (10) se réduit à sa part inhérente (le successeur s'importe avec toutes les
    fonctions intégrées, comme en v6.2).
  - **Ce que les corrections changent à ce qui tourne dans ce pilote** (aucune sonde, `--entrainements-max 0`, aucun
    `--traits` ; une caste par tâche en génération notée) : C-14 et C-15, rien ; C-16, rien (successeurs identiques) ;
    C-17, une seule chose : une réponse de l'architecte en code brut, que la consigne ne demande pas (« Reponds par un
    objet JSON strict sur une ligne », l. 1010–1011), est refusée et l'organisme reste ; en v6.2, elle aurait été validée.
- **Essais des corrections** (en isolation : réseau coupé, utilisateur sans droits, faux noyau ; `essais-corrections-v1/`),
  dans l'ordre : `v621-a` (6 échecs : premières versions de C-14 et C-15 — trois essais de l'architecte en « clé JSON
  manquante », `test_c06`, `test_c15_cas_sain`, et l'essai hérité pas encore adapté), `v621-b` (1 échec : l'essai de C-14
  attendait que toutes les castes répondent, alors que l'arrêt anticipé en garde deux ; l'essai final dit
  `2 <= len(…) <= n`), `v621-c` et `v621-d` (**68 sur 68**), `v621-d-detail` (le même, détaillé) ; les versions de code de
  `v621-a` et `v621-b` ne sont pas gardées ; témoins : les essais nouveaux sur `3bbb78c`
  (`temoin-c5-sur-3bbb78c.log` : 7 échecs, 8 réussites) ; l'essai hérité d'origine sur la v6.2.1
  (`temoin-v53-origine-sur-v621.log` : 1 échec, au routage, et 4 réussites).
- **Vérification de la v6.2.1** par un sous-agent neuf, qui n'a écrit ni la v6.2 ni les corrections
  (`verification-v6-2-1-7ea3270-v1/LISEZMOI-v1.md`, `756f7445a83ffadbedf93152d9fcfe96970c01fa28d41acc07b0be19726ef222` ;
  `EMPREINTES-v1.txt` `cc83b792…`, 129 entrées ; livrable `f48c6557…`) : **aucun défaut bloquant** ; provenance conforme
  (commit, arbre, 26 fichiers) ; rien ne change hors de ce qu'annonce `CORRECTIONS-v5.md` ; 68 essais sur 68, deux fois
  (5,21 s et 5,29 s), les 53 de la v6.2 compris ; les six points partiels levés (3 et 5 avec un choix gardé et ses
  raisons ; 7, 9 et 10 par la fermeture de la voie) ; les sept autres le restent ; V6-01, relevés sous les graines de
  hachage 0, 1 et 2, `_VERROU`, C-01 à C-13 et contrat du noyau conformes ; témoins conformes, deux des sept échecs sur
  `3bbb78c` ne venant pas du défaut visé (C-16 : la fonction n'y existait pas ; C-17, assemblage : seul le message
  diffère). **Constats non bloquants**, déclarés ici : la moitié « routage » de C-15 (l. 1986) n'est gardée par aucun
  essai de la suite ; un commentaire de `test_corrections_v5.py` (l. 76) contredit C-14 ; le refus de C-16 passe par une
  exception, inatteignable avec les constantes actuelles ; l'exactitude d'entraînement reste rapportée (journal
  d'ablations, que la consigne de l'architecte montre, l. 1007 ; `fin_conception.json`), comme en v6.2. Écart du
  vérificateur : deux fichiers transitoires écrits hors de son dossier, effacés et consignés (absence vérifiée par
  conv-audit).
- **Ce que P4v3 dit du code de la v6.1, pour la v6.2.1** : les lignes citées par P4v3 ont un texte identique dans la
  v6.2.1, à d'autres numéros (comparaison ligne à ligne par conv-audit, sur les extractions de `a9d8eb5` et de `7ea3270`,
  arbres recalculés `ae331d1d…` et `4f13647a…` : `comparaison-lignes-v61-v621-v1/`, 12 passages sur 12 identiques).
  `principal.py` : fin de conception l. 2101–2106 (v6.1 l. 1985–1990 ; même critère : 0,78 avec au moins deux
  exemplaires, ce qui peut arriver dès la ronde 1, ou 0,65 à partir de la deuxième ronde, ou la dernière ronde permise) ;
  mutation et stagnation l. 991–998 (v6.1 l. 926–933 : historique sans les rondes au score nul l. 993, test
  `scores[-1] - scores[-2] <= 0.01` l. 994, condition l. 997, une disjonction : en conception, la mutation est tentée à
  chaque ronde ; en génération notée, en cas de stagnation, la première possible à g2) ; bloc `finally` l. 2043 et mise à
  jour de la mémoire l. 2066 (v6.1 l. 1927 et 1950), qui reçoit la pondération de la politique endogène (l. 2077) ;
  exemple de format l. 794 (v6.1 l. 740) ; les dix mêmes requêtes de réserve l. 89–98 (v6.1 l. 86–95).
  `memoire_isvd.py` : l. 240–248, 118–121 et 129–131 (v6.1 l. 236–244, 114–117 et 125–127). `mitose_spectrale.py` :
  l. 75, 78 et 117, inchangées. Le retour arrière, la mitose sans effet (une caste par tâche) et le nombre de recherches
  (60 par course au plus) sont donc ceux que P4v3 décrit. Le point 9 de la demande de v6.2, qui touchait le critère de fin
  de conception, passait par le code brut, désormais fermé (C-17).
- **Sous la configuration de ce pilote** (vérification, lecture seule ; série v13, § Essais) : une caste par tâche en
  génération notée ((160 − 6) // 120 = 1) ; en simulation, une ronde de conception fait 7 appels (formulation, induction,
  quatre `calibrateur_interne`, la mutation), une génération notée 123 appels, 124 quand la stagnation déclenche la
  mutation, g001 129 (la question) ; la mutation est tentée et acceptée comme en v6.2 pour une réponse de l'architecte en
  objet JSON ; une réponse en code brut est refusée (C-17) : aucun successeur n'est écrit, l'organisme reste. Un
  successeur écrit puis jugé invalide par le noyau suit la ligne de P4v3 (liste d'arrêt, appel
  `architecte_mutation_endogene`), transposée : en conception, l'organisme reste ; en génération notée, relance selon
  T2 ; à g003, fin « sans successeur valide », hors de la liste close de la porte.
- **Canal (d)** de P4v3 (§ Plan, point 3) : pour la v6.2.1, aux l. 991–998 de `principal.py` de `7ea3270` ; il paraît aussi
  dans la ligne « course v6.2 précédente » du `LANCEMENT.md` de la v5.3 (appels par génération : un 124 est la mutation) ;
  personne ne compte les rôles des appels d'une génération notée pendant qu'une course tourne ; la lecture est ouverte dès
  la fin de chaque course (§ Plan, point 3).
- **Ce qui n'est pas dit** : aucun effet des corrections sur un score, ni de comparaison entre la v6.2.1 et la v6.2 de
  Gemini (§ Plan, point 5).

## Plan d'analyse (ce qui change de P4v3)

1. **Une seule course de chaque nom** (R3), la v6.2.1 (`pilote4-gemini-v6-2-v1`) **d'abord**, puis la v5.3
   (`pilote4-gemini-v5-3-v1`), chacune en un ou plusieurs segments, avec le lanceur v10. **Ligne d'extension de GO**, une
   seule pour les deux courses, poussée sur `main` avant la v6.2.1, de la forme exacte :
   `| GO-2026-10-25-02 | 2026-10-25 | calcul | extension : pilote 4 (mot direct de Lazar, R-445 et R-448) — v6.2.1 7ea3270, arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d (v6.2 de Gemini 3bbb78c corrigée par conv-audit) ; v5.3 4ecba58, arbre 6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753 ; banque confrontation-v3 157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d ; question M v2 épurée 8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd ; préenregistrement pilote4-gemini-organisme-v4.md <empreinte du texte scellé> ; lanceur lancer_pilote4_gemini_v10.sh 0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952, noyau 8e5e2f7b ; 4 générations, 6 rondes de conception au plus à 3 USD et 900 s chacune, 75 USD par course tous segments compris, jusqu'à 60 recherches par course, dont ≈ 10 web (coût de la source web accepté) ; segments : minuteur à 3 400 s, test de dépense et ligne de dépense à chaque segment | 185 USD au plus pour l'ensemble du GO (pilote 3 : 30,23 USD dépensés ; pilote 4 : 150 USD au plus) | 2026-10-31 | Lazar | R-445, R-448 |`
   (l'empreinte entre chevrons est celle du texte scellé, que donne le message de départ ; la date est celle du mot de
   Lazar, R-445 ; le lanceur ne lit pas la date). Session-depot la vérifie, une fois poussée, par les mêmes `grep` que le lanceur (`GO-2026-10-25-02`,
   `calcul`, `8b1c7511`, l'arbre de l'objet de chaque course, les 16 premiers caractères de l'empreinte du texte) et par
   l'empreinte de la banque `157a2b45`. Une ligne qui ne porte pas l'arbre de la v6.2.1 ne fait rien partir : le lanceur
   refuse la v6.2 sans son arbre sur la ligne (essai `go-v53-seulement-refuse-v6-2`), et la v5.3 sans une v6.2 précédente
   saine (essai `reel-v5-3-sans-precedente`). **Lignes de dépense** :
   `| <date du jour> | pilote4-gemini-v6-2-v1 | GO-2026-10-25-02 | 75 USD au pire cas | empreintes de M 5ae4e801423bbef0 |`, puis, après la fin de la v6.2 de ce pilote,
   `| <date du jour> | pilote4-gemini-v5-3-v1 | GO-2026-10-25-02 | 75 USD au pire cas | empreintes de M 5ae4e801423bbef0 ; empreintes de la v6.2 <16 premiers caractères> |` ;
   et, avant chaque segment K ≥ 2 d'une course, `| <date du jour> | <nom de la course> segment K | GO-2026-10-25-02 | au plus 75 USD moins la dépense déjà faite | après le segment K−1 |`
   (la date de chaque ligne est celle du jour où elle est écrite ; le lanceur ne lit pas la date). Le message de départ
   recopie mot pour mot ces lignes, l'empreinte du texte remplie ; s'il en diffère, rien ne part. La tête de la branche
   citée au message de départ ne diffère de `8e5e2f7b` que par les chemins que le lanceur permet (`PERMIS_APRES_CODE`) :
   rien d'autre (par exemple le travail sur les étapes 1 et 2) n'y est committé avant le départ.
2. **Graines (R9)** : entropie E = <<ENTROPIE>> tirée au scellement par `secrets.randbits(128)` (script
   `sceller_pilote4_v4.py`, qui refuse numpy < 1.25 et toute ligne d'entropie ou de graine de trop) ; deux enfants
   `numpy.random.SeedSequence(E).spawn(2)` ; graine de chaque course = `int(enfant.generate_state(1, dtype=numpy.uint64)[0])`,
   l'enfant 0 pour la v5.3, l'enfant 1 pour la v6.2 (chaque égalité sur une seule ligne, lue et recalculée par le lanceur à
   chaque segment) :
   graine de la course v5-3 = <<GRAINE_V53>>
   graine de la course v6-2 = <<GRAINE_V6X>>
3. **Moment de la lecture des scores** (pilote de conception, décision de Lazar de 01:56 ; remplace le point 3 de P4v3) :
   **dès la fin de chaque course** (liste fermée poussée, recherche des clés faite), ses scores peuvent être lus pour
   corriger les organismes, par le script de lecture du point 4, essayé avant sur une course simulée. Pendant une course
   et entre ses segments, les interdits de lecture de P4v3 restent : aucun score n'est lu tant qu'une course tourne.
   Lisent : conv-audit et Lazar ; session-depot, qui écrit l'étape 1, et toute lignée qui écrit la confrontation, s'ils
   lisent, l'écrivent en réserve dans leurs textes. **Les expériences de confirmation** (l'étape 1 décisive, la
   confrontation, le pilote décisif (b)) se font sur des tâches neuves (la banque v6, lot 3), jamais sur la v3 ni sur la
   v5, qui partage ses textes avec la v3, et déclarent que leurs auteurs ont lu les scores des pilotes de conception. Les
   hypothèses de (b) sont déjà fixées sans aucun score de ce pilote (direction donnée par la question de 00:49, δ = 0,10,
   deux paliers ; § Décisions, 01:48). Les scores de `test_final` ne sont servis ni à Gemini ni à aucun organisme ; ceux
   de `test` et les faits mécaniques peuvent l'être après la fin d'une course, pour corriger un organisme. La lecture de fin
   de course peut être exécutée par des agents neufs de conv-audit (boucle extérieure, § Décisions, 02:05 à 02:17) ;
   ils n'ouvrent rien avant la fin de la course, ne lisent ni textes de tâches, ni vérités, ni fichiers de clé, et ne
   changent ni ce texte ni ses règles ; ce qu'ils concluent sur la banque v3 est exploratoire.
4 bis. **Lecture contre le bruit** (Lazar, 01:54 : « il faut s'assurer que le pilote 4 puisse séparer du bruit
   aussi » ; option (a), sans course de plus ; la décision de 02:05 sur des graines de plus, § Décisions, ne change pas ce
   texte) : (i) chaque score (exactitude équilibrée par famille et par part, à chaque
   génération) est donné avec son intervalle à 95 % sur les tâches (intervalle de Wilson de chaque classe, combinés pour
   l'exactitude équilibrée ; calcul déterministe, sans graine) ; (ii) « au-dessus de la référence, au-delà du bruit des
   tâches » seulement si la borne basse de cet intervalle dépasse la référence de la famille et de la part (surface,
   provenance, contraste de paire : P4v3, § Plan, point 4) ; sinon « non distinct de la référence » ; (iii) dans chaque
   course et chaque famille, la génération 0 contre la génération 3 sur `test_final`, par un test exact apparié sur les
   mêmes tâches (McNemar exact, bilatéral, sur l'exactitude simple, égale à l'exactitude équilibrée quand les classes de
   la part sont égales), quatre tests en tout, corrigés par Holm au niveau 0,05 : « changement au-delà du bruit des
   tâches » ou non ; si les réponses par tâche ne sont pas dans la liste fermée, ce test est rapporté impossible ; (iv)
   tout le reste est « dans le bruit » : à une course par objet, le bruit entre graines n'est pas mesuré, aucune
   comparaison entre les deux objets n'est faite, et un changement au-delà du bruit des tâches dans une course peut tenir
   à sa graine.
4. **Lecture** et 5. **ce que ce pilote ne dit pas** : ceux de P4v3, la v6.2.1 à la place de la v6.1. Aucune différence
   entre objets n'est calculée (ni v6.2.1 − v5.3, ni avec la v6.1, la v6.2 de Gemini, la v6 du pilote 3, M, S ou le premier
   pilote) ; ce pilote ne dit rien de la valeur d'un ajout de complexité (§ Décisions, 00:49), ni de ce que les corrections
   de conv-audit changent à l'organisme de Gemini.

## Liste d'arrêt

Celle de P4v3, ligne à ligne, aux noms de ce pilote et selon la table de correspondance (première course la v6.2.1, seconde
la v5.3 ; lanceur v10 ; essais de la batterie v12), et en plus :

| condition | effet | garde ou vérification |
|---|---|---|
| défaut bloquant de la v6.2.1 établi avant son départ (vérifications, contre-lecture, audit) | rien ne part ; Lazar décide | conv-audit (§ Objet) |
| ronde de la v6.2 hors `OK` | rapportée ; n'arrête pas la v5.3 (la porte ne lit que les générations notées) | lanceur v10 (filtre des générations notées, l. 325) ; extrait |
| organisme de la course v6.2 autre que `organisme/` du commit `7ea3270` (arbre `4f13647a…`, 26 fichiers), par exemple la v6.2 de Gemini `3bbb78c` (`3b2d8d5a…`) ou `fedb065` (`d02c2907…`), ou un commit poussé plus tard sur une branche | la course ne part pas | lanceur v10 (commit, arbre et nombre de fichiers épinglés ; essais `organisme-v6-2`, `nombre-v6-2`, `seg-organisme-modifie`) |
| course v6.2 de ce pilote hors de la liste close (générations notées autres que [0, 1, 2, 3], fin de la lignée autre que « générations maximales » — dont « sans successeur valide » —, arrêts autres que des `STOP` repris puis « aucune lignée active », dernier code non nul, fermeture sans reprise, graine du manifeste autre que celle du texte, ou une autre condition de la liste close) | la v5.3 ne part pas ; Lazar décide ; un `STOP` humain repris sur décision de Lazar compte comme un `STOP` repris | lanceur v10, étapes (0 bis), (2) et (4) (essais `v62-…`, `seg-v62-…`, `seg-clore-v62-refusee`, `v5-3-depense-sans-empreinte-v62`) |

## Essais du lanceur (R5)

Ceux de P4v3 (§ Essais), sur la **batterie v12** (`essais_lanceur_pilote4_v12.sh`, `27ef4524…`), dérivée de la
batterie v8 de P4v3 en quatre pas, chacun par remplacements exacts au nombre attendu (`deriver_essais_pilote4_v9.py` à
`_v12.py`) : v9 (objet v6.2 au premier commit), v10 (second commit), v11 (ordre inversé : cas réels, porte « v6.2
précédente », graine de la précédente, lignes de dépense, segments essayés sur la v6.2 ; un cas sain de plus,
`sain-v5-3-graine`), v12 (objet v6.2.1). Les lanceurs v7 à v9 n'ont jamais servi et les batteries v9 à v11 n'ont
jamais tourné ; seule la batterie v12 a tourné (série v13), et aucun lanceur de ce pilote n'a tourné en réel.

**Série v13**, en simulation (faux appels aux espèces, aucune clé ; réseau seulement pour le cas `passerelle-saine`, qui
interroge sans clé les interfaces d'Anthropic et de Gemini, et pour l'essai de moisson réelle du noyau sur arXiv),
batterie v12 sur le lanceur v10 : de 23:53:00 à
00:03:40 UTC (`essais-lanceur-pilote4-v13.heures.txt`, `e2adbc2f…`) ; **229 cas sur 229 conformes**, aucun échec
(`essais-lanceur-pilote4-v13.log`, `ed50ba1480597700e6165289c4f7ee6c42ec2711d50f73cf92d9288e767634cb`), contre 228 pour la
série v9 de P4v3 (le cas de plus est `sain-v5-3-graine`). Les cas que ce texte cite y sont, chacun une fois et `OK` :
`organisme-v6-2`, `nombre-v6-2`, `seg-organisme-modifie`, `go-v53-seulement-refuse-v6-2`, `reel-v5-3-sans-precedente`,
`seg-clore-v62-refusee`, `v5-3-depense-sans-empreinte-v62`, `sain-v6-2`, `sain-v5-3`, `sain-v5-3-graine`, les 21 cas
`v62-…` et les 4 cas `seg-v62-…`.

**Relevé mécanique des cas sains** (`releves-serie-v13-v1/` : script `releve_appels_simulation_v3.py`, `1e9df693…`, qui
ne lit que des pièces de simulation et aucun score ; sortie `releve-serie-v13-v1.txt`, `e99c1a48…`) :
- v6.2.1 continue : c001 7 appels, dont 1 de mutation ; g000 123 ; g001 129 ; g002 123 ; g003 124, dont 1 de mutation ;
  tous `OK` ; fin « aucune lignée active » ;
- v5.3 continue, après elle : c001 6 ; g000 123 ; g001 129 ; g002 123 ; g003 123 ; tous `OK` ;
- v6.2.1 en deux et en trois segments : mêmes nombres ; arrêts « fichier STOP » repris (segment 2 : 7 appels et
  0,0947 USD relus ; segment 3 : 130 appels et 1,9544 USD relus), puis « aucune lignée active ».

En simulation, la mutation de g003 suit une stagnation simulée ; ces nombres sont des faits du simulateur, pas une
prévision de la course réelle. Les pièces des quatre cas sains (`LANCEMENT.md`, extraits, journaux d'appels de
simulation ; jamais `ferme.tar.gz`) sont versées : `simulation-lanceur-v10/`. Le relevé v2, écrit pour l'ordre ancien,
n'a jamais servi ; il est versé pour mémoire (`releves-serie-v11-v1/`). Aucune seconde course en segments n'est essayée
(la porte est revérifiée à chaque segment K ≥ 2 de la v5.3, avec sa ligne de dépense et ses deux empreintes) : même lacune
que P4v3 pour la v6.1, dite.

## Pièces

`prereg/pieces-pilote4-gemini/` (branche `outils/pilote4-gemini-travail`) : toutes celles de P4v3 (dont son fichier
d'empreintes `EMPREINTES-pilote4-gemini-v1.txt`, `5ed517797d7950b88c017b9a003baeae0d61f2db5b0063799909dfb5e1e03c94`), et en
plus : le **lanceur v10** `lancer_pilote4_gemini_v10.sh` (`0203f546…`), sa dérivation `deriver_lanceur_pilote4_v10.py` et
l'écart `diff-lanceur-pilote4-v9-vers-v10.txt` ; les lanceurs v7, v8 et v9 (`cda96923…`, `40685089…`, `6491c940…`,
**jamais à lancer**), leurs dérivations et leurs écarts ; la **batterie v12** `essais_lanceur_pilote4_v12.sh`
(`27ef4524…`) et sa dérivation ; les batteries v9, v10 et v11 (jamais tournées) et leurs dérivations ; la série v13
(journal, heures, relevé des cas sains `releves-serie-v13-v1/`) ; le **script de scellement v4** `sceller_pilote4_v4.py`
(`6094f21a…`), sa dérivation, ses essais `essais_scellement_pilote4_v4.sh` (`bc79b4bc…`) et leur journal (16 cas sur 16),
le journal témoin sur le script v3 (12 sur 16), les copies d'essai en archive ; le script de vérification du texte scellé
`verifier_scellement_pilote4_v2.py` ; les **pièces de l'objet** (`objet-v6-2-1-v1/` : rapport de livraison de Gemini
recopié ; vérification de la v6.2 (`verification-v6-2-3bbb78c-v1/`) ; corrections de conv-audit — copie de
`CORRECTIONS-v5.md`, écart de l'organisme, journaux des essais en isolation et des témoins (`essais-corrections-v1/`),
recherche de clés avant la poussée du commit ; vérification de la v6.2.1 (`verification-v6-2-1-7ea3270-v1/`) ; les
briefs des deux vérifications ; la comparaison des lignes citées entre la v6.1 et la v6.2.1
(`comparaison-lignes-v61-v621-v1/`) ; le relevé verbatim des mots de Lazar, v1 à v5) ; les fichiers d'empreintes des
pièces donnés aux contre-lectures (`EMPREINTES-pieces-pilote4-v1.txt` à `-v7.txt` ; la v7, donnée à la contre-lecture 6, couvre toutes les pièces avant elle) ; les pièces des contre-lectures 5 et 6 de ce texte (`contre-lecture-5-v1/`,
`contre-lecture-6-v1/`, briefs compris) ; les pièces des cas sains de la série v13 (`simulation-lanceur-v10/`) et le
relevé v2 jamais servi (`releves-serie-v11-v1/`) ; et le fichier d'empreintes de toutes les pièces et des contre-lectures, `EMPREINTES-pilote4-gemini-v2.txt`, d'empreinte <<EMPREINTE_PIECES>>. L'organisme lui-même est
dans son commit (`7ea3270`, branche `canal/conv-audit-organisme-v6-2-1`), que le lanceur extrait.

## Contre-lecture

- **Contre-lectures 1 à 4** : celles de P4v3 (son § Contre-lecture), sur les v1, v2 et v3 du texte ; leurs rapports
  (`pilote4-gemini-organisme-v1-cl1.md`, `3dd09acb…` ; `-v2-cl2.md`, `7c625fa6…` ; `-v3-cl3.md`, `0d95ea8c…` ; `-v3-cl4.md`,
  `e2de1372…`) et leurs pièces sont au fichier d'empreintes de P4v3 et à celui de ce texte. Ce qu'elles ont relu (noyau,
  banque v3, lanceur v6 et batterie v8, règles de P4v3) n'a pas changé ; ce texte n'en modifie que ce que la table de
  correspondance dit.
- **Contre-lecture 5** — sous-agent neuf (`claude-opus-5-5`, lancé par conv-audit, 26 octobre 2026, de 00:29 à 00:55 UTC),
  sur ce texte avant corrections (`efb13feb34f66d9652a194564c0bc9eced2889cbb6305c8dac9e97766246b60e`, 323 lignes ; copie
  gardée dans `contre-lecture-5-v1/`) et P4v3 en entier, avec les pièces v6 (`EMPREINTES-pieces-pilote4-v6.txt`) :
  `prereg/contre-lectures/pilote4-gemini-organisme-v4-cl5.md`
  (`914ac3fbf6b2ba0760ef3dace4dd8c3768909809e441ec0f63e5407c2d138240`), **« scellable après corrections mineures »** :
  objet recalculé conforme (arbres, 26 fichiers, écart 3bbb78c → 7ea3270 réduit à C-14 à C-17), lanceurs v7 à v10,
  batteries v9 à v12 et script de scellement v4 redérivés octet pour octet, série v13 complète (229 sur 229) et relevé
  reproduit, lignes de GO et de dépense passant les `grep` du lanceur, mots de Lazar rendus fidèlement ; deux constats
  mineurs, cinq remarques, une conformité ; pièces `pieces-pilote4-gemini/contre-lecture-5-v1/` (brief, rapport et
  relevés du contre-lecteur, copie du texte relu). **Traitement, par conv-audit, à partir de 01:03 UTC** (sans nouvelle
  relecture complète ; la contre-lecture 6 relit l'écart) :
  - P4C5-01 (mineur : options (2) et (2') de la décision ouverte, applicables sans procédure de lecture) : **sans objet**
    depuis les décisions de Lazar de 01:48 et 01:52 (hypothèses de (b) sans aucun score de ce pilote, (b) sur la banque
    v6 : ces options n'existent plus) et de 01:56 (pilote de conception : le moment et les règles de lecture sont au § Plan,
    point 3, qui remplace celui de P4v3 ; § Décisions).
  - P4C5-02 (mineur : deux énoncés de P4v3 dépendant de l'ordre non transposés) : **corrigé** — ligne de la table de
    correspondance « devis, plafond total » (pour la v6.2, la v5.3 ne part pas ; essai `v62-plafond-total`) et ligne de la
    liste d'arrêt « ronde de la v6.2 hors `OK` ».
  - P4C5-03 (remarque : canal (d) écrit au `LANCEMENT.md` de la seconde course) : **écrit** au § Objet (canal (d)) ; la
    règle des options (2) et (2') ayant disparu, la question de l'échéance est sans objet.
  - P4C5-04 (remarque : (a) défaut de la décision du 25 octobre 23:56 UTC — sans objet, tranchée à 01:48 ; (b) forme de la
    ligne de GO — **écrit** au § Plan, point 1 : le message de départ recopie mot pour mot les lignes, l'empreinte remplie,
    sinon rien ne part ; (c) choix laissés à Lazar sur C-14 et C-16 — **écrits** comme points ouverts dans la table).
  - P4C5-05 (remarque, § Essais : (a) réseau sans clé pour `passerelle-saine` et pour l'essai de moisson réelle sur arXiv —
    **corrigé** ; (b) décalage des numéros de lignes du lanceur v6 au v10 (+12 avant l'étape (0 bis), +13 après) — **écrit**
    dans la table ; (c) gardes de la ligne « course v6.2 hors de la liste close » aux étapes (0 bis), (2) et (4) — **corrigé** ;
    (d) aucune seconde course en segments essayée — **déclaré** comme lacune au § Essais, à combler par le prochain lanceur).
  - P4C5-06 (remarque, traçabilité : (a) pièces des cas sains de la série v13 — **versées** (`simulation-lanceur-v10/`) ;
    (b) relevé v2 jamais servi — **versé** (`releves-serie-v11-v1/`) ; (c) versions de code des essais `v621-a` et `v621-b`
    non gardées — **dit** au § Objet, avec leurs causes et les témoins).
  - P4C5-07 (remarque, petits faits : (a) C-14 « dès deux castes, la délibération s'ouvre » — **corrigé** ; (b) le refus
    d'une clé JSON absente est le point 8 de P4v3, gardé, non C-17 — **corrigé** ; (c) commentaire d'en-tête de
    `sceller_pilote4_v4.py` (l. 17–18 : « v5-3 (première course) ») inexact depuis l'inversion de l'ordre — **laissé tel
    quel** : sans effet sur le code (l'enfant 0 reste la graine de la v5.3, l'enfant 1 celle de la v6.2, comme le § Plan,
    point 2, le dit et comme le lanceur le recalcule), et le script, ses essais (16 sur 16) et son empreinte sont ceux que
    la contre-lecture 5 a redérivés ; (d) tête de la copie de lancement — **écrit** au § Plan, point 1 : elle ne diffère de
    `8e5e2f7b` que par les chemins que `PERMIS_APRES_CODE` permet).
  - P4C5-08 (conforme) : rien à traiter.
- **Contre-lecture 6** — sous-agent neuf, relecture courte de l'écart depuis la version relue par la contre-lecture 5
  (traitement ci-dessus, décisions de Lazar de 01:48 à 02:17 inscrites, § Plan points 3 et 4 bis, liste d'arrêt, § Essais,
  § Pièces), sur la version de ce texte qui porte ce paragraphe sans la ligne qui suit ; sa ligne — empreinte de la version
  relue, rapport `prereg/contre-lectures/pilote4-gemini-organisme-v4-cl6.md` et son empreinte, verdict, constats et leur
  traitement — est inscrite ici avant le script de scellement, avec ses pièces (`contre-lecture-6-v1/`).
- **Ce texte scellé** garde le nom de la v4 ; son empreinte n'est aucune de celles que les contre-lectures ont relues. De la
  version relue par la contre-lecture 6 à lui, il porte en plus : la ligne de la contre-lecture 6 ci-dessus, le traitement
  de ses constats s'il y en a (écrits à la main par conv-audit avant le script), puis l'entropie, les deux graines et
  l'empreinte du fichier d'empreintes des pièces, écrites par `sceller_pilote4_v4.py` ; rien d'autre. Les pièces nouvelles
  depuis la contre-lecture 6 sont ses propres pièces, toutes au fichier d'empreintes.
