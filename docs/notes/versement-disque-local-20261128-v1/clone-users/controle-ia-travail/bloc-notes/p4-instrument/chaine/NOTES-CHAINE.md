# Chaîne de lancement de P4-instrument — notes du rédacteur — v1

Rédacteur neuf de la chaîne (workflow `workflow-p4-chaine-v1.js`, phase « Écrire »), 20 octobre 2026. Dépôt de travail
lu seulement (aucune écriture, aucune commande git qui écrit, aucun `__pycache__`) ; aucune commande Vast.ai réelle (faux
outils de location dans le PATH des bancs) ; aucun réseau ; aucun texte d'action de P3 lu (ni `prereg/P3-consignes-v1.md`,
ni fichier `textes-actions-*` : les fenêtres des bancs et de la répétition viennent de textes synthétiques).

## 1. Ce qui fait foi ici

- Texte qui prime : brouillon 4, `…/p4-instrument/P4-instrument-v1-brouillon4.md` (`32d821fb42e54341…`) — en-tête
  « GO et dépense », Plan d'analyse points 1 et 7, Liste d'arrêt, Chaîne de lancement.
- Plan v2, `…/p4-instrument/plan-code-et-chaine-v2.md` (`7c65e4f64e8c65d9…`), section 4, qui renvoie au plan v1
  (section 4) pour tout ce qu'il ne change pas.
- Chaîne de P3 déclinée : `docs/procedures/P3-premier-test-v2/` (onze scripts, bancs et journaux) et
  `scripts/amorce_instance_p3.sh`, `scripts/p3_instance.sh` (lus, jamais modifiés).
- Module de P4 tel qu'il est sur disque (`…/p4-instrument/module/`, inchangé pendant tout ce travail) :
  `instrument_p4_v1.py` `6e0e026eafba28e7…`, `lecture_p4_v1.py` `51a25e30a70b2439…`, `mesures_conception_p4_v1.py`
  `483b8ac3aca65a98…`, tests `test_instrument_p4_v1.py` `9d015be4…`, `test_lecture_p4_v1.py` `49441971…`,
  `test_gardes_p4_v1.py` `f4f97029…` : 194 tests du module, 1 102 avec la suite du dépôt (908). Le texte de la tâche
  citait d'autres empreintes (`90b9ae8b…`, `5212cf4d…`) et 182 tests : vérifié sur disque et par empreinte (R11), ce
  sont les empreintes ci-dessus qui valent, et ce sont elles que cite le candidat 1 (`6422fb45…`).

## 2. Les dix-sept scripts et leur place

Tous à verser sous `docs/procedures/P4-instrument-v1/`, chacun avec son sceau `.sha256` ; la liste `CHAINE` du lanceur et
du scellement les nomme tous :

| rôle | script de P4 | décliné de |
|---|---|---|
| module commun (GO, accord, module cité, journaux) | `verifications_p4_v1.py` | `verifications_p3_v1.py` |
| contrôles avant dépense | `controles_avant_depense_p4_v1.sh` | `controles_avant_depense_p3_v1.sh` |
| lanceur | `lancer_p4_v1.sh` | `lancer_p3_v1.sh` |
| scellement S | `sceller_p4_v1.sh` | `sceller_p3_v1.sh` |
| surveillance | `surveiller_p4_v1.sh` | `surveiller_p3_v1.sh` |
| contrôle à cinq minutes | `controle_cinq_minutes_p4_v1.sh` | `controle_cinq_minutes_p3_v1.sh` |
| récupération puis destruction | `recuperation_p4_v1.sh` | `recuperation_p3_v1.sh` |
| répétition jouet | `repetition_jouet_p4_v1.sh` | `repetition_jouet_p3_v1.sh` |
| répétition finale | `repetition_finale_p4_v1.sh` | `repetition_finale_p3_v1.sh` |
| bancs | `essais_lanceur_p4_v1.sh`, `essais_controles_p4_v1.sh`, `essais_scellement_p4_v1.sh`, `essais_surveillance_p4_v1.sh` | les bancs de P3 du même nom |
| banc neuf | `essais_verifications_p4_v1.sh` | (aucun : les sous-gardes de P3 se jouaient dans le banc des contrôles) |
| outils des bancs et des répétitions | `outils_essais_p4_v1.py` | (aucun) |
| amorce de l'instance | `amorce_instance_p4_v1.sh` | `scripts/amorce_instance_p3.sh` |
| script de l'instance | `p4_instance_v1.sh` | `scripts/p3_instance.sh` |

Les deux scripts de l'instance ne vont pas sous `scripts/` comme ceux de P3 : `scripts/` est dans `CHEMINS_GELES`, et
le run exige un arbre gelé égal à celui de P3 (`7a54d43`, instrument figé ; Plan d'analyse 1.1 et Liste d'arrêt). Les
y ajouter arrêterait le run. Ils sont donc versés avec le reste de la chaîne, hors de l'arbre gelé, et gelés par le
texte (empreintes citées, voir point T3).

## 3. Correspondance avec la chaîne de P3 : ce qui change, ce qui reste

**`verifications_p4_v1.py`** (module commun, un seul texte lu par le scellement, les contrôles et le lanceur).
Change : rien n'est recodé de ce que le module de P4 sait faire ; les fonctions du module (`controler_go`,
`controler_accord`, `rejouer_garde_de_calcul`, `exiger_module_cite`) sont chargées depuis le dépôt contrôlé, après
contrôle de l'empreinte de `instrument_p4_v1.py` contre sa ligne « Module de P4 » du texte. GO-2026-10-20-07 seul ;
colonne « plafond » qui commence exactement par « 10 USD par lancement » ; échéance lue dans la colonne du GO cité ;
borne de l'étape strictement inférieure à 10 USD ; révocation sous ses deux formes (ligne de GO de type « révocation »
à huit colonnes nommant GO-2026-10-04-08, GO-2026-10-20-06, GO-2026-10-20-07, R-262 ou R-269 ; ligne R-… commençant
par « **Révocation de R-262** » ou « **Révocation de R-269** ») ; accord du jour « **Accord de Lazar pour le lancement
de P4-instrument** » qui cite GO-2026-10-20-07 ou un message de Lazar du jour ; garde de calcul gelée rejouée, jamais
contournée (son refus est un arrêt). Ajoute ce que le module ne lit pas : la ligne « **GO cité par la commande de
création** : `GO_ID=…` » (une fois, GO-2026-10-20-07 seul), les six journaux de preuve et le journal de la répétition
jouet (six récupérations conformes suivies de la destruction, dix-neuf artefacts à un seul KO chacun sans destruction,
lecture jouet en code 0). Pourquoi pas la ligne de commande `--controle go` du module : elle exige l'accord du jour,
qui n'existe qu'après S ; le lanceur, lui, l'appelle telle quelle (avec `--controle module`) juste avant la création.
Neuf aussi : un fichier lu dont l'UTF-8 est invalide est refusé net (code 1, motif écrit), jamais par une trace
d'exception. Reste : sous-commandes `go`, `accord`, `module`, `preuves`, `repetition`, codes 0, 1, 2.

**`controles_avant_depense_p4_v1.sh`.** Change : arbre gelé de S égal à celui de P3 (`CODE_RELU=7a54d43`, instrument
figé) ; module de P4 cité (six fichiers, eux seuls) ; données de P3 de la table « Données lues » à leur empreinte ;
GO et dépense par le module commun ; gardes du module rejouées dans l'ordre du run jusqu'au manifeste (rien n'écrit) ;
bornes de la chaîne reliées aux constantes des scripts versés et aux valeurs du texte (délai 90 minutes, amorce 150
minutes, crédit sur 3,0 heures, surveillance 9 600 s, filtre d'offre, borne 5,41 USD, GO cité, instance tolérée,
formes exactes de l'accord, des révocations et du plafond) ; mesures de conception MC-1 à MC-3 rejouées sur le vrai
tokeniseur (copie de la session) et comparées à la sortie scellée de S ; suite complète (dépôt et module, au nombre
cité) ; journal de la répétition jouet relu par le module commun, au commit répété épinglé. Retiré : tout contrôle
des consignes de P3 (P4 n'en a pas). Reste : clone neuf au commit S, S n'ajoute que texte, configuration et sceaux,
épingles (« A_EPINGLER » : code 2, rien n'est contrôlé), rapports de contre-lecture, branche absente, ligne
« Lancement », `problemes()` vide, `verifier-arbre`, versions de l'environnement, lecture précoce du script de
l'instance, intitulés lus une fois chacun.

**`lancer_p4_v1.sh`.** Change : `GO_ID=GO-2026-10-20-07` dans la commande de création ; `HEURES_CREDIT=3.0` ;
`PLAFOND_SURVEILLANCE_S=9600` ; `BORNE_ETAPE_USD=5.41`, recalculée (9 600 s × 1,30 + 10 min × 1,30 + 20 Go × 0,05 +
24 h × 0,03) et exigée égale et < 10 ; `ARRETEES_TOLEREES="56799469"` (P3), tolérée seulement relue arrêtée, tant
qu'elle existe ; étiquette `p4-v1`, branche `calcul/p4-reel-v1` ; accord relu deux fois (au début, puis après
les lignes de commande du module, avant le choix de l'offre) ; lignes de commande du module (`--controle module`,
`--controle go … --borne 5.41`) jouées telles quelles ; garde gelée rejouée sur la commande de création, qui voit
aussi une révocation consignée pendant le lancement (banc, cas G06). Reste à l'identique : filtre d'offre de P3
(A100 SXM4 80 Go, EPYC 7513, une carte, ≤ 1,30 USD/h, ≥ 16 cœurs, ≥ 128 000 Mo, téléchargement ≤ 0,05 USD/Go, stockage ≤ 0,03 USD/h ; la
moins chère, à prix égal le plus petit identifiant), autres projets tolérés à l'étiquette « rr- » seulement, crédit
calculé en programme, pas de création entre 23:30 et 00:00, place disque (3 Go), jetons jamais affichés, aucun
relancement, codes 0, 2, 3, 4.

**`amorce_instance_p4_v1.sh`.** Change : plafond 150 minutes ; script `docs/procedures/P4-instrument-v1/p4_instance_v1.sh` ;
au plafond, ne pousse que les traces, le manifeste, les résultats et les trois tableaux. Reste : tout le reste.

**`p4_instance_v1.sh`.** Change : étude « p4 » ; aucune consigne ; lecture précoce (avant toute installation) de
« Tests attendus : `N` » (une fois), de l'empreinte canonique de la configuration (une fois) et du chemin
`prereg/P4-instrument-config-v1.json` (une fois), des six lignes « Module de P4 », fichiers présents et sceaux vérifiés ;
suite COMPLÈTE (`tests/` et les trois fichiers de tests du module, un seul passage, au nombre cité ; VP3-12) ; run
`python docs/procedures/P4-instrument-v1/instrument_p4_v1.py --config … --prereg … --run-id …` sous
`timeout --signal=TERM --kill-after=5m 90m` ; poussée forcée de `validation-p4.npz`, `scores-p4.npz` (les cinq bras),
`jetons-principales-p4.npz` et de leurs sceaux ; aucun texte écrit ni poussé. Reste : poussée initiale de la branche
avant l'installation, refus d'une branche existante, traces `traces/p4-*`, lignes « PROGRES », arrêt consigné et
poussée des partiels.

**`surveiller_p4_v1.sh`, `controle_cinq_minutes_p4_v1.sh`.** Change : plafond création + 9 600 s ; étude « p4 »,
étiquette « p4-v1 », branche `calcul/p4-reel-v<N>`. Reste : tout le reste (jetons exigés pour le masquage, relevé
cumulatif, motifs de sortie ; prix, machine, carte, journal à cinq minutes).

**`recuperation_p4_v1.sh`.** Change : fichiers attendus de P4 (manifeste, `identite-p4.json`, `resume.json`, les trois
tableaux et leurs sceaux, traces `p4-*`) dans les deux sens selon l'issue ; résultats rattachés au manifeste du run et
au résumé (ou à sa partie « partiel ») ; tableaux relus au plan (bras I, D, H, B, B′ ; tâches ; pas) ; aucune fenêtre
de 48 caractères d'un texte honnête de P3 dans un fichier poussé (octets des fichiers ajoutés, chaînes JSON décodées,
chaînes des tableaux) ; chaînes JSON de 200 caractères au plus ; puis destruction de l'instance par son identifiant
(étiquette relue « p4-v1 », `vastai destroy instance <id> -y`, instance relue absente), seulement si aucun contrôle
n'est en échec. Reste : clone propre, ascendance, auteurs, sceaux, versions égales à celles du run de P3, carte,
pip freeze, jetons, codes 0, 1, 2, 4 (4 : traces seules).

**`sceller_p4_v1.sh`.** Change : commit S = `prereg/P4-instrument-v1.md`, sa configuration et leurs sceaux, rien
d'autre ; candidat et configuration relus aux épingles ; GO et module par le module commun ; journal de la répétition
jouet et six journaux de preuve relus. Reste : HEAD = origin/main, arbre propre, adresses de origin, retrait des
fichiers créés sur un échec avant le commit, poussée puis relecture distante.

**`repetition_jouet_p4_v1.sh`.** Change : monde jouet de P4 (run jouet de P3 des tests du module, configuration
jouet, préenregistrement jouet = candidat dont quatre citations changent), quatre passages par l'amorce et le script
de l'instance de C, six récupérations conformes suivies de la destruction (faux outil), lecture jouet (mode non
décisif, plan v1 section 4 : « run P3 jouet, puis P4 jouet, puis lecture jouet »), dix-neuf artefacts.
Bancs et répétitions tronquent leurs lignes affichées par `couper` (troncature par octets, puis caractère coupé
retiré par `iconv -c`) au lieu de `cut -c` seul : un journal coupé au milieu d'un « é » n'était plus de l'UTF-8 valide et
le module commun le refusait (constat de ce travail, sur la répétition et le banc de la surveillance).
**`repetition_finale_p4_v1.sh`** : comme P3 (scellement puis contrôles sur un clone jetable et un dépôt nu local),
avec la liste des scripts lue dans `CHAINE`.

## 4. Ce que la session doit faire avant de s'en servir

1. Corriger le candidat (points T1 à T3 ci-dessous ; T4 au versement des rapports), puis verser module, chaîne et sceaux au commit des préalables C.
2. Jouer la répétition jouet sur le vrai C et le vrai candidat (`repetition_jouet_p4_v1.sh C CANDIDAT RACINE_NEUVE`) ;
   le journal produit ici a tourné sur un C d'essai (voir section 5) et ne peut pas être épinglé.
3. Poser les sept épingles des contrôles (`CANDIDAT_RELU`, `CANDIDAT_RELU_CHEMIN`, `CONFIG_RELUE`,
   `CONFIG_RELUE_CHEMIN`, `RAPPORTS_ATTENDUS`, `REPETITION_COMMIT`, `REPETITION_JOUET`), puis rejouer les bancs sur les
   copies versées (leurs journaux citent les empreintes des scripts éprouvés ; toute modification d'un script après son
   banc impose de rejouer le banc), puis la répétition finale.
4. Libérer la place disque : le lanceur exige 3 Go libres ; il en restait entre 1,3 et 2,5 Go pendant ce travail.

## 5. Bancs et répétitions joués ici

Tous sur processeur, dans des dépôts jetables sous `chaine/tmp/` (clones partagés du dépôt de travail, lus par
référence ; dépôts nus locaux à la place de GitHub ; faux outils de location dans le PATH), avec le Python de la session,
`-B` et `PYTHONDONTWRITEBYTECODE=1` (aucun `__pycache__` écrit : vérifié à la fin de chaque banc et dans `chaine/`).
Chaque journal commence par l'empreinte des scripts qu'il éprouve ; les cinq journaux de banc passent
`verifications_p4_v1.py preuves` (code 0, douze scripts éprouvés, chacun égal au script du bloc-notes) et le journal de
la répétition passe `verifications_p4_v1.py repetition`.

| journal (dans `chaine/`) | scripts éprouvés | cas | résultat |
|---|---|---|---|
| `banc-lanceur-p4-v1.log` | `lancer_p4_v1.sh`, `verifications_p4_v1.py`, `essais_lanceur_p4_v1.sh` | 99 (18 en code 0) | 0 non conforme |
| `banc-surveillance-p4-v1.log` | `surveiller_p4_v1.sh`, `controle_cinq_minutes_p4_v1.sh`, `essais_surveillance_p4_v1.sh` | 37 (13 en code 0) | 0 non conforme |
| `banc-verifications-p4-v1.log` | `verifications_p4_v1.py`, `essais_verifications_p4_v1.sh`, `outils_essais_p4_v1.py` | 91 (14 en code 0) | 0 non conforme |
| `banc-controles-p4-v1.log` | `controles_avant_depense_p4_v1.sh`, `verifications_p4_v1.py`, `essais_controles_p4_v1.sh`, `outils_essais_p4_v1.py` | 72 (1 sain, 31 OK) | 0 non conforme |
| `banc-scellement-p4-v1.log` | `sceller_p4_v1.sh`, `verifications_p4_v1.py`, `essais_scellement_p4_v1.sh`, `outils_essais_p4_v1.py` | 57 (3 en code 0) | 0 non conforme |
| `repetition-jouet-p4-v1.log` | `recuperation_p4_v1.sh`, `repetition_jouet_p4_v1.sh`, `outils_essais_p4_v1.py` ; amorce et script de l'instance du C d'essai | 4 passages, 6 récupérations saines, lecture jouet, 19 artefacts | FIN DE LA RÉPÉTITION, code 0 ; module commun : conforme |
| `repetition-finale-p4-v1.log` | — | — | non jouée (section 7) |

Ce que couvrent les bancs (cas sain et artefacts de chaque contrôle neuf, R5) :

- **Vérifications** : ligne du GO dans le texte (absente, doublée, mal formée, autre GO) ; GO au registre (absent,
  doublé, autre type, accordé par la session, plafond sans le préfixe, préfixe voisin, échu, jour de l'échéance
  accepté, lendemain refusé, jour mal formé) ; borne (10 USD refusée, juste sous 10 acceptée, nulle, illisible) ;
  révocations sous les deux formes, pour chacun des cinq identifiants, dans le périmètre et dans la référence, ligne à sept colonnes, voisins (GO-2026-10-20-071 refusé par la garde gelée ;
  R-2620 et R-2690 sans effet), mentions sans révocation ; accord (délégation, message du jour, absent, doublé, autre
  jour, sans la forme exacte, forme de P3, ni GO ni message, GO échu, identifiant mal formé) ; module cité (six
  fichiers, ligne absente, empreinte fausse, ligne hors du module, ligne mal formée, module chargé seulement à son
  empreinte) ; preuves (saines, lignes d'échec, deux empreintes, script non éprouvé, verdict, journal absent ou
  inconnu, ligne mal formée, UTF-8 invalide) ; journal de la répétition (sain, candidat ou commit autres, passage
  manquant ou d'un autre code, récupération absente, KO dans un cas sain, artefact à deux KO ou d'un autre KO, script
  mal formé, doublé ou manquant, fin absente, destruction absente ou de trop, lecture jouet absente, en échec ou
  doublée, UTF-8 invalide) ; usages faux.
- **Contrôles** : un cas sain (31 OK) et 63 artefacts, chacun sur le script entier : GO et dépense, module, texte et
  configuration, code et arbre gelé, données de P3, contenu de S, citations doublées, rapports, répétition (journal,
  commit répété, copies versées), toutes les constantes reliées au texte, configuration hors de MC-1, mode jouet,
  liste du niveau 1, mesures de conception rejouées différentes, sortie scellée altérée, dépendances, `verifier-arbre`,
  branche présente ; épingles absentes ou mal formées, module commun absent, clonage impossible, dossiers existants,
  arguments faux (code 2, rien de contrôlé).
- **Lanceur** : création saine (lignes de `lancement.txt` relues, GO dans la commande de création, crédit 4,50 USD à
  1,10 USD/h), GO, révocations, accord, garde gelée (dont une révocation consignée pendant l'appel), lignes de commande
  du module, borne, offres, crédit, instances (56799469 tolérée arrêtée, refusée en marche, autres projets « rr- »),
  scripts versés modifiés, journaux de preuve, heure, place disque, réponses douteuses de création (code 4).
- **Surveillance et cinq minutes** : motifs de sortie, plafond 9 600 s, jetons masqués, relevé cumulatif, branche de
  P3 refusée, prix, carte, étiquette, journal de l'instance.
- **Scellement** : cas sain (S poussé, quatre fichiers seulement, relu au distant), épingles, copies versées, sceaux,
  GO et dépense, module, journal de la répétition, journaux de preuve, rapports, branche, intitulés, poussée refusée,
  commit refusé (fichiers créés retirés, index propre).
- **Répétition jouet** : la suite complète a tourné sur l'instance jouet (1 102 tests, environ 36 minutes sur ce
  processeur chargé ; passage 1 en 2 185 s), puis le run jouet de P4 (M5 conforme, 45 actions notées), poussées, récupérations et destruction factice.

Constats faits par ces essais, et corrigés avant les journaux gardés :

1. `verifications_p4_v1.py repetition` comptait « DÉTRUITE » aussi dans « NON DÉTRUITE » : le journal sain était refusé.
   Corrigé (« INSTANCE DÉTRUITE PAR SON IDENTIFIANT », et un compte des échecs non détruits ; cas J17).
2. Un banc qui cite la sortie d'un artefact pouvait recopier « NON CONFORME » dans son journal, que `preuves` refuse :
   la citation affichée le masque.
3. Lignes coupées par octets (`cut -c`) au milieu d'un caractère : journaux non UTF-8 ; troncature sûre `couper`, et
   refus net du module commun (cas P10, J21).
4. Lanceur : un GO échu est refusé dès la relecture de l'accord (qui exige le GO en vigueur), avant le contrôle du GO ;
   motif attendu du banc corrigé.
5. Lecture jouet ajoutée à la répétition (point T11), exigée par le module commun.
6. Une édition d'un banc pendant son exécution a corrompu cette exécution (bash lit le script au fil de l'eau) : jetée
   et rejouée ; aucun script n'a plus été touché pendant une exécution.

Outils de travail gardés (non versés, avec leur sceau) sous `chaine/tmp/` : `fabriquer_c_essai.sh` (C d'essai : clone
partagé, commit sans les PDF, module et chaîne versés, candidat d'essai tiré du brouillon 4), `repetition-jouet-copie-
officielle-2.sh` (la copie jouée de la répétition, ligne `D` seule changée), `finaliser_v1.sh` (copie des journaux
sous leur nom de preuve, puis `preuves` et `repetition` du module commun). Clones et dépôts jetables effacés.

## 6. Points où le texte se tait ou se contredit, et ma lecture

Les trois premiers points bloquent la chaîne tant que le candidat n'est pas corrigé ; les autres sont des lectures.

- **T1 — Commit du code d'analyse (contradiction, bloquant).** Brouillon 4 : « au candidat » ; candidat 1 (`6422fb45…`,
  l. 25) : « celui du scellement S ». Le module (`exiger_code_cite`, motif ``Commit du code d'analyse : `<40 signes>` ``),
  le scellement, les contrôles (bloc 2) et la lecture lisent un commit de 40 signes, une seule fois ; S ne peut pas se
  citer lui-même (son empreinte dépend du texte). Avec le candidat 1 tel quel : scellement refusé (code 2), contrôles en
  KO, et le run s'arrêterait dès le manifeste (garde `exiger_code_cite`). Ma lecture : citer
  ``Commit du code d'analyse : `7a54d431d89745839220f882b41b13e8c62ecfdd` `` (arbre gelé égal à celui de S et de P3,
  instrument figé ; le module est hors de l'arbre gelé et gelé par ses lignes « Module de P4 ») ; c'est ce que produit
  `outils_essais_p4_v1.py candidat`, et `CODE_RELU` des contrôles vaut ce commit.
- **T2 — « Tests attendus » (forme, bloquant).** Candidat 1, l. 51 : « Tests attendus : 1 102, soit … » (espace, pas de
  guillemets inversés). La chaîne lit la forme de P3, « Tests attendus : `1102` », une fois : lecture précoce du script
  de l'instance (sinon arrêt avant l'installation), contrôles (bloc 13), contrôle à cinq minutes (« préenregistrement lu
  : N tests attendus »), récupération (6). Ma lecture : écrire `1102` entre guillemets inversés, une fois, la phrase
  explicative ensuite.
- **T3 — Scripts de l'instance, ligne « Lancement », rapports (silence, bloquant).** Le brouillon 4 et le candidat 1 ne
  citent ni l'empreinte de l'amorce et du script de l'instance, ni la ligne « Lancement », ni les rapports sous la forme
  lue par les contrôles ; le texte de P3 le faisait (`prereg/P3-premier-test-i-a-v1.md` l. 32-33 et 56). Sans ces
  lignes, rien dans le texte scellé ne gèle les deux scripts de l'instance (hors de l'arbre gelé et hors des lignes
  « Module de P4 »). Ma lecture : le candidat ajoute, comme `outils_essais_p4_v1.py candidat` :
  « - Scripts de l'instance, gelés par le scellement : `docs/procedures/P4-instrument-v1/amorce_instance_p4_v1.sh`
  (`<sha256>`, sha256) ; `docs/procedures/P4-instrument-v1/p4_instance_v1.sh` (`<sha256>`, sha256). »,
  « - Lancement : `PREREG=prereg/P4-instrument-v1.md`, `BRANCHE=calcul/p4-reel-v1`. », et chaque rapport versé sous la
  forme « `prereg/contre-lectures/<nom>` (`<sha256>`) ». Le lanceur refuse sans l'une ou l'autre empreinte (cas N01, N01b) ; les
  contrôles mettent un KO par ligne manquante.
- **T4 — Rapports « de la famille P4 » (lecture).** Les contrôles et le scellement exigent que les rapports présents
  sous `prereg/contre-lectures/` dont le nom contient « P4 » soient exactement ceux épinglés (au moins deux), tous cités.
  Le texte demande aussi de verser le brouillon 1 « avec leurs sceaux » : s'il est versé sous un nom qui contient « P4 »,
  il entre dans la famille et doit être épinglé et cité comme un rapport.
- **T5 — Chemin de la configuration (variante tolérée).** Brouillon 4 : empreinte et chemin sur la même ligne ;
  candidat 1 : chemin à la ligne suivante. Le script de l'instance et les contrôles acceptent les deux : empreinte
  canonique citée une fois, et « chemin `prereg/P4-instrument-config-v1.json` » une fois, où qu'il soit.
- **T6 — Plafond de la phase (silence sur la forme).** « À l'accord du jour, la session vérifie que la dépense consignée
  plus la borne de l'étape reste sous 150 USD, et l'écrit dans la ligne d'accord » : aucune forme exacte n'est donnée.
  La chaîne ne lit donc pas cette somme (je n'invente pas de forme) ; elle exige la forme exacte de l'accord, le GO
  cité, son plafond par lancement, son échéance et l'absence de révocation de GO-2026-10-04-08, GO-2026-10-20-06,
  GO-2026-10-20-07, R-262 et R-269. Le contrôle des 150 USD reste un geste de la session à l'accord. Si une garde est
  voulue, il faut une forme dans le texte (par exemple « dépense consignée X USD + borne 5,41 USD < 150 USD »).
- **T7 — « Dépense au-delà de la borne de l'étape » (silence sur le moyen).** Aucun compteur de dépense en direct n'existe
  dans la chaîne de P3. La borne tient par construction : prix relu à cinq minutes au plus 1,30 USD/h et au plus celui
  de l'offre (KO sinon : arrêt et nœud, borne à recalculer), surveillance jusqu'à la création + 9 600 s (3,47 USD au
  plus), arrêt par l'identifiant, destruction après la récupération vérifiée (disque 24 heures au plus).
- **T8 — Récupération en échec (silence).** Le texte prévoit la destruction « après la récupération vérifiée » et ne dit
  pas quoi faire si elle échoue. Ma lecture : aucune destruction (code 1), instance gardée arrêtée, nœud de Lazar ; le
  poste « disque 24 heures » de la borne peut alors être dépassé si la réponse tarde (0,03 USD/h au plus). Les traces
  seules conformes (code 4, arrêt avant le run) détruisent aussi l'instance : rien n'y reste d'utile.
- **T9 — Étiquette avant destruction (ajout).** Le texte dit « par son identifiant » ; la récupération relit d'abord
  l'étiquette de l'instance (« p4-v1 ») et refuse sinon, pour qu'un identifiant faux ne détruise rien d'autre, puis
  relit la liste après la destruction.
- **T10 — Instance 56799469 (lecture).** Texte : « n'est pas réutilisée » ; plan v1 : tolérée « tant qu'elle existe ».
  Le lanceur la tolère seulement relue arrêtée ; en marche, pas de création. Sa destruction est prévue le 23 octobre.
- **T11 — Lecture jouet (silence du texte, plan v1 gardé par le v2).** Le brouillon 4 dit « répétition jouet » ; le plan
  v1 (section 4, que le v2 garde : « comme le v1 ») précise « run P3 jouet, puis P4 jouet, puis lecture jouet ». La
  répétition joue donc la lecture de P4 en mode non décisif sur les résultats récupérés du passage 1 (le mode décisif
  exige le verdict complété de P3, qui n'existe pas encore) ; le module commun exige sa ligne en code 0.
- **T12 — Suite sur l'instance (variante).** Plan v1 : `pytest -q tests docs/procedures/P4-instrument-v1` ; le script
  nomme les trois fichiers de tests du module : mêmes 194 tests aujourd'hui, et un fichier de tests versé plus tard dans
  le dossier ne changerait pas silencieusement le compte.
- **T13 — Borne de l'étape « inférieure à 10 USD ».** Lue stricte (< 10). Échéance : refus si la date du jour est après
  l'échéance de la colonne ; le jour même est accepté (comme la garde gelée).
- **T14 — Révocation et garde gelée (écart de lecture).** Le module lit les identifiants nommés au mot près ; la garde
  gelée, elle, cherche l'identifiant du GO comme sous-chaîne du périmètre et de la référence. Une ligne de révocation
  qui nomme « GO-2026-10-20-071 » bloque donc la création par la garde, que la chaîne ne contourne jamais (banc des
  vérifications, cas G10c ; G10c2 : R-2620 et R-2690 ne révoquent rien).
- **T15 — Chaînes de 200 caractères (contradiction possible).** Le motif d'arrêt du résumé (`arret.motif`) recopie le
  message d'une garde et peut dépasser 200 caractères. Ma lecture : 200 pour toute chaîne, 1 000 pour ce seul motif (la
  recherche des fenêtres s'y applique toujours).
- **T16 — Résumé toujours écrit.** Le module de P4 écrit `resume.json` à chaque fin, avec `arret` et `partiel` sur un
  arrêt (pas d'`arret.json` comme P3) ; la récupération en tient compte (4a, 2b, 6f).
- **T17 — Fenêtres des textes honnêtes.** Comme P3 : la fenêtre de 48 caractères du milieu de chaque texte d'au moins
  64 caractères, fenêtres d'un seul caractère répété ignorées ; seules les lignes de la condition honnête sont lues.
  Plus court que 64 caractères : non cherché (limite héritée de P3).
- **T18 — Heure de création.** Pas de création entre 23:30 et 00:00 UTC (T-7 de P3) : gardé, le texte n'en dit rien.
- **T19 — Mesures de conception rejouées aux contrôles.** Elles lisent les textes honnêtes de P3 pour les retokeniser
  (comptes seulement, dossier de travail effacé à la fin). Interdit au rédacteur : les bancs jouent un bouchon (sortie
  scellée recopiée, altérée par cas) devant le programme réel de comparaison ; le vrai rejeu n'est joué qu'à la
  répétition finale de la session.
- **T20 — Place disque.** Le lanceur exige 3 Go libres ; la récupération clone le dépôt entier (environ 1,2 Go, PDF
  compris). Pendant ce travail, entre 1,3 et 2,5 Go restaient libres.

## 7. Réserves

- **Répétition jouet sur un C d'essai.** Elle a tourné sur un dépôt local (clone partagé du dépôt de travail, commit
  `d1ad1342ee4d04363a2027bdaac6f8ec8c6767f4` qui verse le module et les dix-sept scripts, sans les PDF) avec un candidat d'essai (`f9f313ff…`), par une
  copie dont seule la ligne `D` change (sa ligne « script répété : repetition_jouet_p4_v1.sh » porte donc l'empreinte
  de la copie, `56cb2bda…`, et la première ligne du journal celle du script du bloc-notes). Ni ce commit ni ce candidat n'existent dans le dépôt de travail : le journal
  prouve que les scripts fonctionnent, il ne peut pas être épinglé. La session la rejoue sur le vrai C.
- **Répétition finale non jouée.** Elle exige les vraies épingles, le vrai candidat, les vrais rapports, les journaux
  versés, et ses contrôles rejouent les mesures de conception sur les textes de P3 (interdits ici). Son script n'a
  été éprouvé que par sa syntaxe et par le banc du scellement (qui joue le même scellement, copie changée de la même
  façon) ; la logique propre à la répétition finale (quatre lignes changées de la copie du scellement, ligne `DEPOT`
  des contrôles) reste à éprouver par la session.
- **Bouchons des bancs.** Le banc des contrôles remplace la suite complète (écrit « N passed ») et le rejeu des mesures
  de conception (sortie scellée recopiée) ; la vraie suite (1 102 tests) a tourné, elle, dans la répétition jouet, sur
  l'instance jouet. Le banc du lanceur remplace l'outil de location, les contrôles avant dépense et `df` ; les formats
  des réponses de l'outil de location sont ceux de la chaîne de P3 (blocs des offres, des instances et du crédit repris
  à l'identique de `lancer_p3_v1.sh`).
- **Empreintes et ordre.** Chaque journal cite l'empreinte des scripts qu'il éprouve ; `verifications_p4_v1.py preuves`
  et le scellement exigent qu'elles égalent les copies versées. Toute retouche d'un script après son banc impose de
  rejouer ce banc (et la répétition si le script est répété).
- **Concurrence.** Des processus d'un autre chantier (revue de l'addendum 2) tournaient en même temps sur la même
  machine ; la place disque est restée sous 2,5 Go libres, d'où des bancs joués les uns après les autres.
