"""Lanceur local (orchestration de l'instance louée) — témoin « attaque publiée reproduite » (Bailey et collègues), v18.

La v18 (décision de Lazar du 13 novembre 2026, « go (a), vérifie le chemin de code de la relance » ; addendum 5) ajoute
deux choses, et rien d'autre :
1. **Relance seule** (`Conduite(relance_seule=…)`) : la relance entière de la liste d'arrêt (texte l. 338, 371) jouée
   par une conduite neuve sur une instance neuve, quand la première exécution du run principal s'est interrompue avant
   20 tours complets dans une conduite précédente (série 3 : K′ = 8, compte Vast sans crédit). Même chemin que
   `conduire` jusqu'au contrôle du juge compris (amorce, auto-arrêt, mise en place, contrôle du juge sur l'instance
   neuve) ; puis, **sans pilote ni règle sur l'instance**, K recalculé par la même règle (`analyse_v3.nombre_de_tours`)
   sur le budget restant (même B, D du poste au moment du calcul, c de l'instance neuve, **t du pilote déjà mesuré**) ;
   K < 20 : arrêt, pas de verdict, nœud ; sinon manifeste « relance » (`regle_tours` : K, D, c, `relance: true`,
   `premiere_execution` : la règle de la première exécution) et exécution `principal-relance` (graine du run
   principal, dossiers neufs). Les gardes d'entrée (avant toute création d'instance) : K′ < 20, t > 0, règle de la
   première exécution complète.
2. **Assemblage pour la lecture** (`assembler_lecture`) : un dossier neuf qui réunit les transferts scellés de la
   première conduite (mise en place, contrôle du juge, pilote, règle, principal, manifestes) et ceux de la relance
   (`principal-relance`, manifeste « relance ») pour que `lecture_v8.valider` et `lire` le lisent comme une conduite
   unique ; la mise en place et le contrôle du juge de l'instance de la relance y sont copiés à part
   (`relance-mise-en-place`, `relance-controle-juge`) et doivent avoir passé toutes leurs gardes ; toutes les empreintes
   des fichiers copiés sont vérifiées ; aucune note n'est lue.
`VEILLEUR_MODULE` passe à `lanceur_v18`. Instance (`instance_v16`), exécution (`execution_v4`), lecture (`lecture_v8`) :
inchangées.

Docstring de la v17 :

La v17 emploie `instance_v16` et `execution_v4` (script public lancé comme programme principal) : `INSTANCE_MODULE`,
imports, `CHEMINS_ARCHIVE` (`execution_v4.py` au lieu d'`execution_v3.py`, `instance_v16.py` au lieu d'`instance_v15.py`) ;
`VEILLEUR_MODULE` passe à `lanceur_v17`. Rien d'autre ne change.

Docstring de la v16 :

La v16 emploie `instance_v15` (relecture différentielle du code v15, `0d7cc2a1…` : D-1, D-2, D-3, D-5, D-7) ;
`VEILLEUR_MODULE` passe à `lanceur_v16`. Rien d'autre ne change.

Docstring de la v15 :

La v15 applique la relecture du code v14 (`relecture-code-condition6-v14-bailey-v1.md`, `0e7c96ca…`) : elle emploie
`instance_v14` (filtre et condition du message d'erreur corrigés, R-1, R-2, R-4, R-5) ; `VEILLEUR_MODULE` passe à
`lanceur_v15` ; la ligne d'import trop longue (R-9) est scindée. Rien d'autre ne change.

Docstring de la v14 :

La v14 (décision de Lazar du 12 novembre 2026, « go (a) ») emploie `instance_v13`, qui fait sortir le message d'erreur
d'une exécution morte avant tout tour (`erreur-demarrage-v1.txt`, condition et filtre dans la docstring d'`instance_v13`),
et ne change rien d'autre : `INSTANCE_MODULE`, `CHEMINS_ARCHIVE` et les imports passent d'`instance_v12` à `instance_v13` ;
`VEILLEUR_MODULE` passe à `lanceur_v14` ; la liste fermée du transfert est `instance_v13.SORTANTS` (B-6 : `cv.SORTANTS`
étendue de ce seul nom).

Docstring de la v13 :

La v13 applique la relecture du code v12 (`docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v12-
bailey-v1.md`, `3865961f…`) et la décision de Lazar du 11 novembre 2026 (`registres/passations/2026-11-11-1537-
decision-lazar-lectures-37-38-w1.md`) ; seul le module des veilleurs change (`lanceur_v13`) ; `INSTANCE_MODULE` et
`CHEMINS_ARCHIVE` restent ceux de la v12 (`instance_v12`, inchangé) :
- W-1 : instance lue « en attente de démarrage » (`STATUT_EN_ATTENTE` : état réel arrêté, dont un conteneur sorti
  « exited » par le repli du chien au PID 1 ou par un plantage, état voulu « running ») sans transfert complet : le
  veilleur de secours et `_finir` ne la détruisent plus d'emblée. Ils demandent l'arrêt par l'identifiant (R10 ; un
  arrêt annule aussi l'attente d'une carte), puis relisent le statut (veilleur : au passage suivant ; `_finir` : après
  `periode_prete_s`). Arrêtée (état voulu arrêté compris) : gardée, « reprise requise » (C-2). Détruite seulement
  après `ESSAIS_DESTRUCTION` arrêts refusés, ou sur un statut relu toujours non arrêté ;
- P-1 : statut « arrêt en cours » (`STATUT_ARRET_EN_COURS`) sans transfert complet : relu une fois (veilleur : au
  passage suivant ; `_finir` : après `periode_prete_s`) avant toute destruction ; arrêté : gardée ;
- P-2 : avant tout redémarrage ou transfert, une reprise arrête par leur PID (R10) les veilleurs d'arrêt des reprises
  précédentes du même dossier (`_arreter_veilleurs_precedents`), après en avoir vérifié l'identité (ligne de commande
  `veilleur-arret` et le chemin de leur journal) ; un veilleur précédent encore vivant après le signal : ni
  redémarrage ni transfert, alerte, nœud. Alerte exacte de la remise à l'arrêt : arrêt refusé mais statut relu
  arrêté = « arrêt refusé, statut relu arrêté (instance vraisemblablement déjà arrêtée) », non « non remise à
  l'arrêt » ;
- P-3 : `Poste.ecrire` et `_ecrire_rapatriement` écrivent par un temporaire propre au processus
  (`<chemin>.tmp-<pid>`), vidé sur le disque (`fsync`) avant `os.replace` (comme Q-4) ;
- P-4 : reprise sur un statut ni arrêté, ni « running », ni en attente (« arrêt en cours », « loading », « unknown »,
  « offline », absent) : rien n'est fait, mais un veilleur d'arrêt borné par le budget et l'échéance (`borne_seule`)
  est laissé (poste illisible : borne immédiate), comme V-2.
Lectures : `docs/notes/reproduction-attaque-publiee-v1/lectures-addendum-condition6-v11.md`. Noms des fichiers de
données inchangés.

Docstring de la v12 :

La v12 applique la relecture du code v11 (`docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v11-
bailey-v1.md`, `044ba3e2…`) ; `INSTANCE_MODULE`, `CHEMINS_ARCHIVE` et le module des veilleurs sont ceux de la v12
(`instance_v12`, `lanceur_v12`) :
- V-1 : `FournisseurVast.statut` lit `intended_status` **et** `actual_status` (`statut_vast`) : « stopped » ou
  « exited » seulement si l'état réel l'est et que l'état voulu l'est aussi (ou est absent) ; état réel arrêté mais
  voulu en marche (redémarrage en attente d'une carte, « scheduling ») : `STATUT_EN_ATTENTE` ; état réel en marche mais
  voulu arrêté : `STATUT_ARRET_EN_COURS`. Cette lecture vaut pour `_reprendre`, `Veilleur`, `VeilleurArret`, `_finir`
  et `_prete`. Le veilleur d'arrêt ne finit (« arrêtée ») qu'après un arrêt **accepté** depuis son échéance (ligne
  « stopping instance … ») **puis** un statut arrêté relu ensuite ; sinon il demande l'arrêt (un nouvel arrêt annule
  aussi un redémarrage en attente). `_remettre_a_l_arret` ne tient l'arrêt pour confirmé que si un arrêt a été accepté
  **et** que le statut relu est arrêté ; sinon veilleur à échéance immédiate et alerte. Une instance trouvée en
  attente de démarrage par `reprendre` est remise à l'arrêt (rien d'autre) ;
- V-2 : reprise d'une instance en marche : même borne de budget que pour une instance arrêtée, calculée avant tout
  `executer` (`_borne_budget`) ; poste illisible, échéance passée, ou moins de `DUREE_TRANSFERT_MIN_S` avant
  B − `MARGE_SECOURS_USD` : remise à l'arrêt **sans transfert**, « reprise impossible dans le budget : nœud » ; sinon,
  avant de toucher le battement, un veilleur d'arrêt est lancé et vu vivant à `min(borne de budget, échéance,
  maintenant + DELAI_COMMANDE_S + MINUTERIE_REPRISE_S)` (non vivant : remise à l'arrêt sans transfert) ; commande en
  cours ou instance illisible : rien n'est fait, mais un veilleur d'arrêt borné par le seul budget et l'échéance est
  laissé ;
- V-4 : veilleur de secours : un statut illisible est noté et relu au passage suivant ; la destruction n'a lieu
  qu'après `ESSAIS_DESTRUCTION` lectures illisibles de suite (comme `_finir`) ;
- V-5 : la reprise borne ses arrêts (veilleur d'arrêt, minuterie, attente de l'instance prête) à `borne de budget −
  ECART_SECOURS_S` et à `échéance − ECART_SECOURS_S` (`ECART_SECOURS_S` = 2 × période du veilleur de secours + 120 s) :
  l'instance est arrêtée avant que le veilleur de secours de la conduite morte, s'il vit encore, n'atteigne son seuil
  (D ≥ B − 0,5 au taux relevé, ou l'échéance) ; arrêtée et sans transfert qui fait foi, il ne la détruit pas ;
- Q-1 : la destruction faite par la reprise est écrite dans `poste-v5.json` (le veilleur de secours encore vivant
  finit alors sur « déjà détruite ») ; une erreur d'écriture est notée et dite en alerte ;
- Q-2 : `_finir` ne pose la marque `rapatrie` que si le transfert est complet ; sinon, statut relu, instance arrêtée
  gardée, instance en marche détruite (l. 309-310), sans dépendre du moment où le chien agit.
Lectures : `docs/notes/reproduction-attaque-publiee-v1/lectures-addendum-condition6-v10.md`. Noms des fichiers de
données inchangés (`rapatriement-v11.json`, `veilleur-arret-v11.jsonl`, `reprise-v10/`, `bilan-reprise-v10.json`).

Docstring de la v11 :

La v11 applique la relecture du code v10 (`docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v10-
bailey-v1.md`, `b6b6430b…`) ; `INSTANCE_MODULE`, `CHEMINS_ARCHIVE` et le module des veilleurs sont ceux de la v11
(`instance_v11`, `lanceur_v11`) :
- B-3 : `reprendre` exige le code 0 de la liste des étapes de l'instance (`ls`) ; la liste attendue est l'**union** des
  étapes lancées selon le journal de la conduite (`conduite-v5.jsonl`, qui note désormais chaque lancement,
  `{"commande": …, "lancee": true}`) et des dossiers présents ; chacune doit avoir un transfert qui fait foi ; sinon
  pas de destruction : remise à l'arrêt, nœud. Journal de la conduite illisible : rien n'est fait ;
- C-1 : avant tout redémarrage, `reprendre` lance un **veilleur local d'arrêt** détaché (`lanceur_v11 veilleur-arret`,
  vérifié vivant ; sinon pas de redémarrage), qui arrête l'instance par son identifiant (R10) à `début +
  delai_prete_s + DELAI_COMMANDE_S + minuterie_s`, ou à l'échéance du GO si elle vient avant, et retente à chaque
  période jusqu'au statut « stopped » ou « exited » (ou l'instance absente de l'inventaire de l'étiquette) ; la remise à
  l'arrêt fait `ESSAIS_DESTRUCTION` essais, puis relit le statut (P-7) ; non confirmée : un veilleur d'arrêt à échéance
  immédiate est lancé ; l'alerte dit si une minuterie a été posée sur l'instance ou non, et quel veilleur vit ;
- C-2 : le veilleur de secours et `_finir` lisent le statut de l'instance avant de détruire : instance « stopped » ou
  « exited » dont une étape lancée n'a pas de transfert qui fait foi (fichier `rapatriement-v11.json` de la conduite,
  absent si la conduite n'a rien transféré) : **pas de destruction** (seul le stockage court), alerte « reprise
  requise » ; le veilleur s'arrête et `_finir` l'arrête (la reprise a son propre veilleur). Instance en marche :
  destruction immédiate, comme en v10 (la borne de dépense prime) ;
- P-1 : chaque sondage lit aussi le chien de garde (PID à son identité, battement de moins de `CHIEN_FRAICHEUR_S`,
  ligne `CHIEN VIVANT|MORT`) ; après la garde d'auto-arrêt, un chien vu mort est arrêté par son PID (R10) puis relancé
  (`.fin` effacé), lancement vérifié ; relance non vérifiée : notée, retentée au sondage suivant, alerte au bilan.
  Redémarrage du conteneur par l'hôte : les processus détachés ne reviennent pas ; l'exécution en cours est vue morte
  (identité changée) et le chien relancé tant que la conduite vit ; conduite morte aussi : risque déclaré (lecture 22) ;
- P-7 : remise à l'arrêt : la ligne « stopping instance … » fait foi de l'acceptation ; le statut est relu, et noté ;
- P-2 (plafond B dur, GO-2026-11-10-10) : une reprise ne porte jamais la dépense du poste au-delà de B. Avant
  `demarrer`, D est calculé sur `poste-v5.json` (toutes instances, de leur création à leur destruction ou à
  maintenant, intervalles arrêtés compris, lecture 22 (b)) ; le taux retenu est le plus haut du taux relevé à la
  création et du taux lu maintenant. Si D atteindrait B − `MARGE_SECOURS_USD` avant `DUREE_TRANSFERT_MIN_S` : pas de
  redémarrage, « reprise impossible dans le budget : nœud », instance laissée arrêtée ; poste illisible ou sans cette
  instance : pas de redémarrage. Sinon la minuterie et le veilleur local d'arrêt arrêtent au plus tôt de leurs délais,
  de l'échéance du GO et de l'instant où D atteindrait B − 0,5 (`borne_budget`).
Lectures : `docs/notes/reproduction-attaque-publiee-v1/lectures-addendum-condition6-v9.md`.

Docstring de la v10 :

La v10 (décision de Lazar du 11 novembre 2026, option (b), `registres/passations/2026-11-11-1226-decision-lazar-option-b-
arret-autonome.md`) ajoute l'**arrêt autonome de l'instance** (`instance_v10`, chien de garde) et la **reprise** après
une coupure du poste local ; rien d'autre ne change dans la conduite :
- l'amorce lance, dès que l'environnement Python de l'instance est prêt, le chien de garde (`instance_v10
  chien-de-garde`), détaché, à son PID et son identité (`etats/chien-de-garde.pid`, `.debut`) ; amorce finie sans
  chien lancé : garde tombée ;
- chaque sondage touche le battement de la conduite sur l'instance (`etats/battement-conduite`), au début de `_finir`
  et avant le transfert de chaque étape aussi ; après le transfert, la conduite pose la marque `etats/rapatrie` : le
  chien arrête le conteneur (si la destruction qui suit échoue, l'instance arrêtée ne coûte plus que son stockage) ;
- après l'amorce et **avant la mise en place**, la conduite fait vérifier l'auto-arrêt sur l'instance (`instance_v10
  auto-arret`) ; indisponible : « garde de mise en place tombée : auto-arrêt de l'instance indisponible » : pas de run,
  pas de verdict (jamais de repli silencieux) ;
- `FournisseurVast.detruire` passe `-y` et exige la ligne « destroying instance <id>. » : **défaut de la v9 trouvé
  en lisant le code installé de `vastai` 1.11.0** (`vastai/cli/commands/instances.py`, `destroy__instance` ;
  `vastai/cli/main.py`, `run_command`) : sans `-y`, la commande demande une confirmation (`input`) ; entrée fermée
  (veilleur lancé avec `stdin` nul) : « Aborted. », code 0, **rien n'est détruit et la destruction est tenue pour
  faite** ; entrée d'un terminal : attente jusqu'au délai de 120 s ; et un refus de l'API sort aussi avec le code 0.
  Même exigence pour `arreter` (« stopping instance <id>. ») et `demarrer` (« starting instance <id>. ») ;
- sous-commande `reprendre` (`Reprise`) : à la reprise d'une session, inventaire de l'instance du poste par son
  **étiquette** (une seule, et celle du journal de la conduite) ; instance arrêtée : redémarrée **le temps du seul
  transfert** (une dépense de quelques minutes au taux de la carte, plus le stockage, comptée sous le même GO, notée
  au bilan ; refusée après l'échéance du GO), sous une **minuterie** posée sur l'instance (`chien-de-garde
  --minuterie`, arrêt du conteneur au plus tard `MINUTERIE_REPRISE_S` après, ou à l'échéance) ; empreintes prises
  avant l'arrêt gardées (`empreintes --si-absent`), transfert, comparaison (un second transfert au plus), scellement,
  dans un dossier neuf `<sortie>/reprise-v10/` (manifestes copiés : `lecture_v8.valider` s'y applique) ; puis
  destruction par l'identifiant (R10) **seulement si chaque étape a un transfert qui fait foi** ; sinon l'instance est
  remise à l'arrêt et gardée (nœud). Aucune reprise du calcul : un run interrompu est lu comme tronqué selon les
  règles existantes. Une instance en marche dont une commande vit encore n'est pas touchée (elle s'arrêtera seule),
  sauf `--arreter-en-cours` (arrêt par PID, état reconstitué « arrêt par la conduite »).
Lectures nouvelles : `docs/notes/reproduction-attaque-publiee-v1/lectures-addendum-condition6-v8.md`.

Docstring de la v9 :

La v9 applique C-1 de la relecture des lignes touchées v8 (`relecture-lignes-touchees-code-condition6-v8-bailey-v1.md`,
`baa35511…`), texte du rapport repris tel quel : un pilote mort dont l'état des gardes est illisible (tours complets
inconnus) arrête tout — ni reprise, ni règle, ni run principal ; nœud (lecture « garde inconnue au pilote = arrêt »,
mot de Lazar de 16:57).

La v8 emploie `instance_v8` et `lecture_v8` (décision de Lazar du 10 novembre 2026, points A-1 et A-2 de
`relecture-lignes-touchees-code-condition6-v7-bailey-v1.md`, `5831e98c…`) : `INSTANCE_MODULE`, `CHEMINS_ARCHIVE` et le
module du veilleur sont ceux de la v8. A-2 : une exécution du pilote dont l'issue est « ligne de garde coupée »
(`lecture_v8.issue_pilote` : dernière ligne coupée dans un journal de gardes, garde inconnue) **arrête** la conduite :
pas de reprise, pas de run principal ; le bilan dit « pas de run principal ; ligne de garde coupée au pilote (garde
inconnue) ; nœud » et porte les exécutions du pilote (`pilote`, avec leurs gardes tombées et lignes coupées). Une
exécution morte dont `tours` est relu reçoit les gardes tombées de la ligne `ETAT` (ligne coupée nommée comprise).
Rien d'autre ne change.

Docstring de la v7 :

La v7 emploie `instance_v7` et `lecture_v7` (relecture des lignes touchées v5 → v6, `a46dc4fb…`, C-1 à C-4) :
`INSTANCE_MODULE`, `CHEMINS_ARCHIVE` et le module du veilleur sont ceux de la v7 ; la ligne `ETAT` de `tours` porte
les lignes coupées ignorées sur l'instance (`lignes_tronquees_ignorees`), reportées dans l'exécution rendue au bilan
(exécution morte) et dans `etats_reconstitues` (C-2). Rien d'autre ne change.

Docstring de la v6 :

La v6 corrige M-1 de la relecture des lignes touchées v5 (`22879993…`) : une exécution morte est inscrite dans
`arretees` (cause « coupure de l'hôte ») dès qu'elle est vue morte, pour que la reconstitution de son état soit
retentée avant les empreintes si la première tentative échoue ; et emploie `instance_v6` et `lecture_v6` (M-2).

La v5 reprend la v4 (`lanceur_v4.py`, docstring ci-dessous) et applique la relecture des lignes touchées v3 → v4
(`relecture-lignes-touchees-code-condition6-v4-bailey-v1.md`, `ff6c76c7…`) :
- C8 (N-1) : toute exécution qui n'a pas écrit son état en reçoit un **sur l'instance, avant les empreintes**, par
  `instance_v5 tours --ecrire-etat` (jamais d'écrasement ; « reconstitué » ; code non nul ; cause) : sur une exécution
  morte (cause « coupure de l'hôte », après l'arrêt du groupe, C10), et dans `_finir` pour toute exécution que la
  conduite a arrêtée par PID (cause « dépense » au seuil local, « échéance du GO » à la borne d'échéance, « instance
  injoignable », ou « arrêt par la conduite » sur une autre sortie) ; la lecture (`lecture_v5`) lit alors le run
  tronqué sur K′ et la relance complète ;
- C9 (N-2) : destruction en échec → un veilleur à échéance 0 est **toujours** lancé, puis l'ancien est arrêté s'il
  est vu vivant (sinon gardé, alerte) ;
- C10 (N-3) : sur `MORT` (meneur mort sans `.fin`), le groupe de la commande est arrêté par son PID avant `tours` et
  avant toute relance ; l'arrêt attend la fin du groupe (TERM, attente bornée, puis KILL) ;
- C11 (N-5) : étiquette unique par conduite à la création (`--label`) ; si `creer` lève, inventaire filtré sur cette
  seule étiquette, destruction de ces seuls identifiants ; sinon alerte au bilan (« création incertaine : inventaire
  R10 manuel ») ; l'étiquette est écrite à l'ordre de lancement ;
- N-4 : le lancement détaché écrit, avec le PID, son identité (`boot_id` et heure de départ, champ 22 de
  `/proc/<pid>/stat`) dans `<nom>.debut` ; « vivant » exige la même identité ; l'arrêt par PID ne vise le groupe que si
  le meneur a cette identité ou n'existe plus (un PID réemployé n'est jamais signalé) ;
- remarque (R10) : le veilleur local est suivi par son objet `Popen` ; un veilleur déjà récolté n'est jamais signalé ;
  `processus_vivant` ne récolte plus un PID inconnu.
Noms des fichiers de la conduite en v5 (`conduite-v5.jsonl`, `poste-v5.json`, `arrets-v5.jsonl`,
`bilan-conduite-v5.json`, `amorce-v5.sh`). Lectures : liste
`docs/notes/reproduction-attaque-publiee-v1/lectures-a-acter-addendum-condition6-v3.md`.

Docstring de la v4 :

Préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`) : règle du nombre de tours (B, R,
D, c), liste d'arrêt, pilote et reprise, relance, transfert et comparaison des empreintes avant destruction, conditions
de lancement 2 et 8. La v4 reprend la v3 (`lanceur_v3.py`, dont la docstring dit les corrections 1 à 18 du rapport
`4f079ece…`) et applique la relecture en différentiel du code v3
(`relecture-differentiel-code-condition6-v3-bailey-v1.md`, `a2107244…`), corrections C1 à C7 :
- C1 (D-1) : le `try … finally` qui rapatrie puis détruit s'ouvre **aussitôt après** `creer` : relevé du taux,
  écriture du poste, journal des étapes et lancement du veilleur sont dedans ; si le taux n'a pu être lu, l'instance
  est détruite quand même (sa dépense est alors signalée au bilan, à relever dans `registres/depenses.md`) ; la
  destruction est retentée (`ESSAIS_DESTRUCTION`), et si elle échoue sans veilleur vivant, un veilleur est lancé avec
  une échéance immédiate, qui retente la destruction à chaque période ;
- C2 (D-2, D-7) : `Veilleur.boucle` met chaque passage dans un `try` ; toute erreur est écrite à son journal ; la
  destruction est retentée à chaque période jusqu'à réussir ; poste illisible → dernier poste lu, ou, s'il n'y en a
  aucun, destruction ; le veilleur écrit un battement (`<journal>.battement`) à chaque passage et sa sortie d'erreur
  dans `<journal>.err`. La conduite vérifie qu'il vit (PID vivant et non zombie, battement frais,
  `verifier_veilleur`) avant toute commande et à chaque sondage ; mort → une relance du veilleur, sinon arrêt et
  destruction. `marge_secours` et la période du veilleur lui sont passées ;
- C3 (D-3) : `FournisseurVast.executer` rattrape `TimeoutExpired` et l'échec de `vastai ssh-url` (code 255) ; la
  conduite tolère les sondages en échec jusqu'à `SONDAGES_EN_ECHEC_MAX` consécutifs **ou** `DUREE_SANS_SONDAGE_MAX_S`
  sans sondage réussi (instance tenue pour injoignable : arrêt) ; sur toute sortie anormale, la commande en cours est
  arrêtée par son PID **avant** le rapatriement ;
- C4 (D-4) : chaque sondage vérifie que le PID de la commande vit (`kill -0`) ; mort sans `.fin` → état
  « commande distante sans ligne d'état (coupure de l'hôte) », normalisé, tours complets relus sur l'instance
  (`instance_v4 tours`, sans note) : relance selon la liste ; la borne locale d'une exécution est le premier de
  `échéance − marge/2` et de l'instant où D atteint `B − SEUIL_LOCAL_USD` (1 USD, entre B − 2 et B − 0,5 ; valeur à
  acter) ; le lancement détaché rend `LANCE <pid>` après avoir vérifié `<nom>.pid` ; sinon un nouvel essai
  (idempotent : rien n'est relancé si la commande vit ou a fini), puis arrêt ;
- C5 (D-5) : attente de l'instance prête (état « running » de `vastai show instance`, puis `ssh … true` accepté),
  bornée (`DELAI_PRETE_S`), comptée dans D ; `ssh` et `scp` avec `StrictHostKeyChecking=accept-new` et `BatchMode` ;
- C6 (D-6) : l'archive envoyée ne contient que les fichiers de `src/` dont l'instance a besoin (`CHEMINS_ARCHIVE`,
  fermeture des imports vérifiée par l'essai) ; rien de `docs/`, `donnees/`, `diag/`, `registres/` ni du reste de
  `src/` ne part sur l'hôte loué ;
- C7 (D-8) : `instance_v4 regle-tours` met K et la garde au même `ETAT` ; « K < 20 après le pilote : arrêt, devis
  révisé à Lazar » est atteignable ;
- lecture 7 (section 3) : l'échéance « AAAA-MM-JJ » est lue comme la fin du jour à Paris (22:59:59 UTC en
  hiver), lecture prudente, fuseau à acter ;
- P-i : la ligne de GO est lue sur `origin/main` (`texte_go_main`, `git show origin/main:registres/go.md`, après un
  `git fetch origin main` explicite de l'appelant) ; la conduite refuse un texte de GO différent de celui-là.
Ce module ne lit aucune note. Lectures de lignes scellées faites ici : liste
`docs/notes/reproduction-attaque-publiee-v1/lectures-a-acter-addendum-condition6-v2.md`.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import shlex
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path

from .. import scellement
from ..gardes import GardeArret
from . import analyse_v3 as an
from . import conventions_v3 as cv
from .instance_v16 import (SORTANTS,
                           BATTEMENT_CONDUITE, CHIEN, CHIEN_FRAICHEUR_S, D_ABANDON_S, DELAI_PRISE_EN_CHARGE_S,
                           JOURNAL_CHIEN, MARQUE_RAPATRIE, MINUTERIE, PERIODE_CHIEN_S)
from .lecture_v8 import ETAPES, ISSUE_LIGNE_COUPEE, MANIFESTES, issue_pilote, relance_permise

DEPOT_URL = "https://github.com/lciric/controle-ia-travail.git"  # cité dans l'ordre de lancement (condition 8)
CACHE_HF = "/root/hf"
JETON_DISTANT = "/root/.cache/huggingface/token"
ARCHIVE_DISTANTE = "/root/travail.tar.gz"
ETATS_DISTANTS = "/root/etats"
EMPREINTE_PREREG = "fb6c2f34"
EMPREINTE_DEVIS = "f9c8c66e"
MARGE_SECOURS_USD = 0.5
MARGE_TRANSFERT_S = 3600.0
SEUIL_LOCAL_USD = 1.0  # C4 : arrêt local d'une exécution à D ≥ B − 1 (entre B − 2 et B − 0,5) ; valeur à acter
SONDAGES_EN_ECHEC_MAX = 30  # C3 : sondages consécutifs en échec tolérés …
DUREE_SANS_SONDAGE_MAX_S = 3600.0  # … ou durée sans sondage réussi, avant de tenir l'instance pour injoignable
DELAI_PRETE_S = 1800.0  # C5 : attente bornée de l'instance prête
ESSAIS_DESTRUCTION = 3  # C1 : essais de destruction par la conduite avant de s'en remettre au veilleur
INSTANCE_MODULE = "controle_ia.temoin_bailey.instance_v16"
VEILLEUR_MODULE = "controle_ia.temoin_bailey.lanceur_v18"  # v17 : veilleurs locaux (secours, arrêt de la reprise)
FICHIER_RAPATRIEMENT = "rapatriement-v11.json"  # v11 (C-2) : écrit par `_finir` après le transfert, lu par le veilleur
DELAI_COMMANDE_S = 120.0  # v11 (C-1) : délai d'une commande `ssh` (lancement de la minuterie de reprise)
DUREE_TRANSFERT_MIN_S = 900.0  # v11 (P-2) : durée minimale d'une reprise (instance prête, minuterie, transfert)
STATUTS_ARRETES = ("stopped", "exited")
# v12 (V-1) : statuts combinés de `statut_vast` (état réel et état voulu en désaccord)
STATUT_EN_ATTENTE = "en attente de démarrage"  # réel arrêté, voulu en marche (« scheduling ») : jamais « arrêté »
STATUT_ARRET_EN_COURS = "arrêt en cours"  # réel en marche, voulu arrêté : ni « arrêté » ni « running »
PERIODE_VEILLEUR_SECOURS_S = 30.0  # v12 (V-5) : période du veilleur de secours de la conduite (`Conduite`)
ECART_SECOURS_S = 2 * PERIODE_VEILLEUR_SECOURS_S + 120.0  # v12 (V-5) : avance de la reprise sur le seuil de secours
CHIEN_RELANCES_EN_ECHEC_ALERTE = 3  # v11 (P-1) : relances du chien non vérifiées avant l'alerte au bilan
MINUTERIE_REPRISE_S = 3600.0  # v10 : instance redémarrée pour le transfert : arrêt au plus tard après ce délai
EXECUTIONS = ("pilote", "pilote-reprise", "principal", "principal-relance")
PREFIXE_ETIQUETTE = "temoin-bailey-c6-"  # C11 : étiquette unique par conduite (`--label`)
# C6 : seuls fichiers envoyés sur l'instance (fermeture des imports de `instance_v16`, vérifiée par l'essai)
CHEMINS_ARCHIVE = ("src/controle_ia/__init__.py", "src/controle_ia/gardes.py", "src/controle_ia/scellement.py",
                   "src/controle_ia/temoin_bailey/__init__.py", "src/controle_ia/temoin_bailey/analyse_v3.py",
                   "src/controle_ia/temoin_bailey/conventions_v3.py", "src/controle_ia/temoin_bailey/execution_v4.py",
                   "src/controle_ia/temoin_bailey/journaliseur_v3.py", "src/controle_ia/temoin_bailey/lecture_v8.py",
                   "src/controle_ia/temoin_bailey/instance_v16.py")


class Fournisseur:
    def creer(self, offre: str, image: str, disque_go: int, etiquette: str | None = None) -> str: ...
    def inventaire(self, etiquette: str) -> list[str]: ...  # C11 : identifiants portant cette seule étiquette
    def taux_horaire(self, ident: str) -> float: ...
    def statut(self, ident: str) -> str | None: ...
    def detruire(self, ident: str) -> None: ...
    def arreter(self, ident: str) -> None: ...  # v10 : arrêt (stockage seul facturé), pour la reprise
    def demarrer(self, ident: str) -> None: ...  # v10 : redémarrage le temps du transfert (reprise)
    def executer(self, ident: str, commande: str, delai_s: float | None = None) -> tuple[int, str]: ...
    def rapatrier_fichier(self, ident: str, distant: str, local: Path) -> None: ...
    def envoyer_fichier(self, ident: str, local: Path, distant: str) -> None: ...


OPTIONS_SSH = ("-o", "StrictHostKeyChecking=accept-new", "-o", "BatchMode=yes", "-o", "ConnectTimeout=30")


def statut_vast(info: dict) -> str | None:
    """v12 (V-1) : statut lu sur `actual_status` **et** `intended_status` (paquet `vastai` 1.11.0 :
    `vastai/cli/commands/machines.py` l. 1173, 1258-1292 ; `vastai/data/instance.py` l. 58-60). « stopped » ou
    « exited » (état réel) seulement si l'état voulu est aussi arrêté, ou absent ; état réel arrêté et voulu autre
    (redémarrage en attente d'une carte, « scheduling », documentation de Vast) : `STATUT_EN_ATTENTE` ; état réel
    « running » et voulu arrêté : `STATUT_ARRET_EN_COURS` ; sinon l'état réel tel quel (`None` s'il manque)."""
    if not isinstance(info, dict):
        return None
    reel, voulu = info.get("actual_status"), info.get("intended_status")
    if reel in STATUTS_ARRETES:
        return reel if voulu in (None, "") or voulu in STATUTS_ARRETES else STATUT_EN_ATTENTE
    if reel == "running" and voulu in STATUTS_ARRETES:
        return STATUT_ARRET_EN_COURS
    return reel


class FournisseurVast(Fournisseur):
    """Commande `vastai` (la clé est lue par la commande ; ce module ne la lit ni ne l'imprime). Aucune variable
    d'environnement n'est passée à la création (le jeton passe par un fichier, S-3). C3 : `executer` ne lève jamais
    sur une coupure (adresse illisible, `vastai ssh-url` en échec, délai dépassé) : il rend le code 255. C5 : `ssh` et
    `scp` acceptent une clé d'hôte neuve et ne posent aucune question (`BatchMode`)."""

    def _vast(self, *args: str) -> str:
        return subprocess.run(["vastai", *args], check=True, capture_output=True, text=True, timeout=120).stdout

    def creer(self, offre, image, disque_go, etiquette=None):
        args = ["create", "instance", offre, "--image", image, "--disk", str(disque_go), "--ssh", "--direct", "--raw"]
        if etiquette:
            args += ["--label", etiquette]  # C11
        return str(json.loads(self._vast(*args))["new_contract"])

    def inventaire(self, etiquette):
        """C11 : identifiants des instances du compte dont l'étiquette est exactement `etiquette` (aucune autre)."""
        return [str(i["id"]) for i in json.loads(self._vast("show", "instances", "--raw"))
                if str(i.get("label") or "") == etiquette]

    def taux_horaire(self, ident):
        return float(json.loads(self._vast("show", "instance", ident, "--raw"))["dph_total"])

    def statut(self, ident):
        """v12 (V-1) : état réel et état voulu lus ensemble (`statut_vast`)."""
        return statut_vast(json.loads(self._vast("show", "instance", ident, "--raw")))

    def _vast_attendu(self, attendu: str, *args: str) -> None:
        """v10 : la commande `vastai` sort avec le code 0 même sur un refus ou une confirmation abandonnée ; seule la
        ligne de succès imprimée par le paquet (1.11.0) fait foi."""
        sortie = self._vast(*args)
        if attendu not in sortie:
            raise GardeArret(f"vastai {' '.join(args[:2])} : succès non confirmé")

    def detruire(self, ident):
        self._vast_attendu(f"destroying instance {ident}.", "destroy", "instance", str(ident), "-y")  # v10 : -y

    def arreter(self, ident):
        self._vast_attendu(f"stopping instance {ident}.", "stop", "instance", str(ident))

    def demarrer(self, ident):
        self._vast_attendu(f"starting instance {ident}.", "start", "instance", str(ident))

    def _ssh(self, ident) -> tuple[str, str]:
        m = re.match(r"ssh://([^@]+)@([^:]+):(\d+)", self._vast("ssh-url", ident).strip())
        if not m:
            raise GardeArret("adresse de l'instance illisible")
        return f"{m.group(1)}@{m.group(2)}", m.group(3)

    def executer(self, ident, commande, delai_s=None):
        try:
            hote, port = self._ssh(ident)
            p = subprocess.run(["ssh", *OPTIONS_SSH, "-p", port, hote, commande], capture_output=True, text=True,
                               timeout=delai_s)
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, GardeArret, OSError):
            return 255, ""
        return p.returncode, p.stdout

    def rapatrier_fichier(self, ident, distant, local):
        hote, port = self._ssh(ident)
        local.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["scp", *OPTIONS_SSH, "-P", port, f"{hote}:{distant}", str(local)], check=True,
                       capture_output=True, timeout=3600)

    def envoyer_fichier(self, ident, local, distant):
        hote, port = self._ssh(ident)
        subprocess.run(["scp", *OPTIONS_SSH, "-P", port, str(local), f"{hote}:{distant}"], check=True,
                       capture_output=True, timeout=3600)


class FournisseurFichier(Fournisseur):
    """Pour l'épreuve du veilleur sur processeur : une destruction est une ligne écrite dans un fichier. v11 : un arrêt
    est une ligne écrite dans `<fichier>.arrets` ; une instance qui y figure a le statut « stopped »."""

    def __init__(self, chemin: str):
        self.chemin = Path(chemin)

    def detruire(self, ident):
        with open(self.chemin, "a", encoding="utf-8") as f:
            f.write(f"{ident}\n")

    def arreter(self, ident):
        with open(str(self.chemin) + ".arrets", "a", encoding="utf-8") as f:
            f.write(f"{ident}\n")

    def statut(self, ident):
        try:
            arretes = Path(str(self.chemin) + ".arrets").read_text(encoding="utf-8").split()
        except OSError:
            arretes = []
        return "stopped" if str(ident) in arretes else "running"

    def inventaire(self, etiquette):
        return []


def fournisseur_depuis(spec: str) -> Fournisseur:
    if spec == "vast":
        return FournisseurVast()
    if spec.startswith("fichier:"):
        return FournisseurFichier(spec[len("fichier:"):])
    raise GardeArret("fournisseur inconnu")


# --- conditions de lancement ------------------------------------------------------------------------------------------

def _cellules(ligne: str) -> list[str]:
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def ligne_go(texte_go: str, go_id: str) -> dict:
    """Colonnes de `registres/go.md` : id, accordé le, type, périmètre (objet), plafond, échéance, accordé par,
    référence."""
    for ligne in texte_go.splitlines():
        cellules = _cellules(ligne)
        if cellules and cellules[0] == go_id:
            if len(cellules) < 6:
                raise GardeArret("condition 2 : ligne de GO incomplète")
            return {"id": go_id, "type": cellules[2], "objet": cellules[3], "plafond": cellules[4],
                    "echeance": cellules[5]}
    raise GardeArret("condition 2 : ligne de GO absente de registres/go.md")


def texte_go_main(depot: Path, ref: str = "origin/main") -> str:
    """P-i : le registre des GO fait foi sur `main` ; il est lu par `git show origin/main:registres/go.md`, jamais
    dans la branche de travail (la ligne GO-2026-11-10-10 n'y est pas). Aucune requête réseau ici : l'appelant fait
    d'abord `git fetch origin main` (refspec explicite)."""
    try:
        return subprocess.run(["git", "-C", str(depot), "show", f"{ref}:registres/go.md"], check=True,
                              capture_output=True, text=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise GardeArret("condition 2 : registres/go.md illisible sur origin/main") from None


def _nombre(texte: str) -> float:
    return float(texte.replace(",", "."))


def b_de_l_objet(objet: str) -> float:
    """S-1 : B lu dans la cellule d'objet, sous la forme qui le fixe, entre parenthèses : « (B = 75, garde d'horloge à
    B − 2) » dans GO-2026-11-10-10. La même cellule cite aussi « le passage de Bailey à B = 120 » comme **hors
    enveloppe, retour à Lazar** : cette mention, hors parenthèse, ne fixe pas B (lecture à acter). Une seule valeur
    entre parenthèses admise."""
    valeurs = {_nombre(x) for x in re.findall(r"\(\s*B\s*=\s*(\d+(?:[.,]\d+)?)", objet)}
    if len(valeurs) != 1:
        raise GardeArret("condition 2 : la ligne de GO ne fixe pas B (« (B = … ») de façon unique")
    return valeurs.pop()


def verifier_go(go: dict, b: float, empreinte_prereg: str = EMPREINTE_PREREG,
                empreinte_devis: str = EMPREINTE_DEVIS) -> None:
    """Condition 2 : type « calcul » ; l'objet cite le texte scellé et le devis v4, et fixe B (« B = … »), égal au B
    du manifeste ; le plafond de la ligne (premier nombre de sa cellule, en USD) couvre B."""
    if go["type"].lower() != "calcul":
        raise GardeArret("condition 2 : la ligne de GO n'est pas de type « calcul »")
    if empreinte_prereg not in go["objet"]:
        raise GardeArret("condition 2 : la ligne de GO ne cite pas le préenregistrement scellé")
    if empreinte_devis not in go["objet"]:
        raise GardeArret("condition 2 : la ligne de GO ne cite pas le devis v4")
    if b_de_l_objet(go["objet"]) != float(b):
        raise GardeArret("condition 2 : B de la ligne de GO différent du B du manifeste")
    nombres = re.findall(r"\d+(?:[.,]\d+)?", go["plafond"])
    if not nombres or _nombre(nombres[0]) < float(b):
        raise GardeArret("condition 2 : plafond de la ligne de GO inférieur à B")


def verifier_non_revoque(texte_go: str, go_id: str) -> None:
    """P-3 : aucune ligne de type « révocation » ne vise le GO cité."""
    for ligne in texte_go.splitlines():
        c = _cellules(ligne)
        if len(c) >= 4 and c[0] != go_id and c[2].lower() in ("révocation", "revocation") and go_id in ligne:
            raise GardeArret("condition 2 : le GO cité est révoqué")


FUSEAU_ECHEANCE = "Europe/Paris"  # lecture 7 (section 3 du rapport `a2107244…`) : lecture prudente, à acter


def echeance_epoch(echeance: str, fuseau: str = FUSEAU_ECHEANCE) -> float:
    """« AAAA-MM-JJ » : lue comme la fin de ce jour **à Paris** (23:59:59, heure de Paris : 22:59:59 UTC en hiver),
    lecture prudente de la liste v2 (lecture 7 : la v3 lisait 23:59:59 UTC, une heure au-delà de la fin du jour à
    Paris) ; fuseau à acter par Lazar ; « AAAA-MM-JJTHH:MMZ » : l'instant dit, en UTC. Fuseau introuvable : arrêt
    (aucun repli silencieux)."""
    import calendar
    import datetime
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})(?:[T ](\d{2}):(\d{2}))?", echeance)
    if not m:
        raise GardeArret("condition 2 : échéance du GO illisible")
    a, mo, j = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if m.group(4):
        return calendar.timegm((a, mo, j, int(m.group(4)), int(m.group(5)), 0))
    try:
        from zoneinfo import ZoneInfo
        tz = ZoneInfo(fuseau)
    except Exception:
        raise GardeArret(f"condition 2 : fuseau de l'échéance introuvable ({fuseau})") from None
    return datetime.datetime(a, mo, j, 23, 59, 59, tzinfo=tz).timestamp()


def verifier_echeance(echeance: float, creation: float, b: float, c: float,
                      marge_secours: float = MARGE_SECOURS_USD, marge_transfert_s: float = MARGE_TRANSFERT_S) -> None:
    """Correction 5 : le texte exige `échéance ≥ création + (B − 2)/c h` ; la dépense pouvant courir jusqu'au seuil de
    secours, on exige plus : `échéance ≥ création + (B − marge_secours)/c h + marge_transfert`."""
    if echeance < creation + (float(b) - float(marge_secours)) / float(c) * 3600 + float(marge_transfert_s):
        raise GardeArret("condition 2 : échéance du GO antérieure à la création + (B − marge de secours)/c heures "
                         "+ marge de transfert")


# --- manifeste (A-7, S-2) --------------------------------------------------------------------------------------------

def chemin_snapshot(depot: str, revision: str) -> str:
    return f"{CACHE_HF}/models--{depot.replace('/', '--')}/snapshots/{revision}"


def lire_versions_figees(chemin, empreinte: str = cv.VERSIONS_FIGEES_SHA256) -> dict:
    """S-2 : versions figées, vérifiées par leur empreinte ; Python 3.11 ; paquets exigés présents ; strong_reject au
    commit du texte."""
    p = Path(chemin)
    if not p.is_file() or cv.sha_fichier(p) != empreinte:
        raise GardeArret("versions figées : fichier absent ou empreinte différente")
    v = json.loads(p.read_text(encoding="utf-8"))
    if v.get("python") != cv.PYTHON:
        raise GardeArret("versions figées : Python différent de 3.11")
    for paquet in cv.VERSIONS_EXIGEES:
        if paquet not in v.get("versions", {}):
            raise GardeArret(f"versions figées : {paquet} absent")
    if list(v.get("git", {}).get("strong_reject", [None, None]))[1] != cv.JUGE_COMMIT_PAQUET:
        raise GardeArret("versions figées : commit de strong_reject différent du texte")
    return v


def ecrire_manifeste(chemin: Path, *, versions: dict, git: dict, python: str, revision_modele: str,
                     revision_adaptateur: str, revision_base: str, commit_code: str, b: float, go_id: str,
                     versions_figees: dict | None = None) -> dict:
    """Manifeste (R9) fixé avant la création de l'instance. N'écrase jamais un fichier existant (R12)."""
    chemin = Path(chemin)
    if chemin.exists():
        raise GardeArret("manifeste déjà présent : une nouvelle version prend un nouveau nom (R12)")
    g = an.graines()
    m = {"version": 3, "commit_code": commit_code, "commit_public": cv.COMMIT_PUBLIC, "arbre_public": cv.ARBRE_PUBLIC,
         "go_id": go_id, "B": b, "python": python, "versions": versions, "git": git, "cache_hf": CACHE_HF,
         "versions_figees": versions_figees,
         "modele": cv.MODELE, "revision_modele": revision_modele,
         "chemin_modele": chemin_snapshot(cv.MODELE, revision_modele),
         "juge": {"adaptateur": cv.JUGE, "revision_adaptateur": revision_adaptateur, "base": cv.JUGE_BASE,
                  "revision_base": revision_base, "dtype": "torch.bfloat16"},
         "graines": {"racine": an.RACINE_GRAINES, "pilote": g["pilote"], "principal": g["principal"],
                     "cle_reechantillonnage": list(an.CLE_REECHANTILLONNAGE)}}
    an.garde_graines(m["graines"])
    chemin.write_text(json.dumps(m, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return m


def manifeste_depuis_versions_figees(chemin: Path, chemin_versions, *, commit_code: str, b: float,
                                     go_id: str) -> dict:
    """Manifeste écrit depuis les versions figées (S-2) : versions, commits, Python et révisions relevées."""
    v = lire_versions_figees(chemin_versions)
    rev = v["revisions_hugging_face_relevees_le_2026-11-10"]
    return ecrire_manifeste(chemin, versions=v["versions"], git=v["git"], python=v["python"],
                            revision_modele=rev[cv.MODELE], revision_adaptateur=rev[cv.JUGE],
                            revision_base=rev[cv.JUGE_BASE], commit_code=commit_code, b=b, go_id=go_id,
                            versions_figees={"chemin": cv.VERSIONS_FIGEES, "sha256": cv.sha_fichier(chemin_versions)})


# --- dépense du poste -------------------------------------------------------------------------------------------------

def _ecrire_atomique(chemin: Path, texte: str) -> None:
    """v13 (P-3, comme Q-4 de `instance_v12._ecrire_json`) : temporaire propre au processus (`<chemin>.tmp-<pid>`),
    vidé sur le disque avant `os.replace` ; deux processus (reprise et veilleur de secours) n'écrivent jamais le même
    temporaire. En cas d'erreur, le temporaire est effacé et l'erreur sort (le fichier d'origine reste entier)."""
    tmp = Path(f"{chemin}.tmp-{os.getpid()}")
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(texte)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, chemin)
    except BaseException:
        try:
            tmp.unlink()
        except OSError:
            pass
        raise


@dataclass
class Poste:
    """D : chaque instance comptée à son taux réel × heures de sa création à sa destruction (ou à maintenant), toutes
    instances du poste comprises (texte l. 252-254)."""
    b: float
    instances: list[dict] = field(default_factory=list)

    def ajouter(self, ident: str, c: float, creation: float) -> None:
        self.instances.append({"id": ident, "c": c, "creation": creation, "destruction": None})

    def detruite(self, ident: str, quand: float) -> None:
        for i in self.instances:
            if i["id"] == ident and i["destruction"] is None:
                i["destruction"] = quand

    def depense(self, maintenant: float | None = None) -> float:
        maintenant = time.time() if maintenant is None else maintenant
        return sum(float(i["c"]) * ((i["destruction"] or maintenant) - float(i["creation"])) / 3600
                   for i in self.instances)

    def d_avant(self, ident: str, maintenant: float | None = None) -> float:
        maintenant = time.time() if maintenant is None else maintenant
        return sum(float(i["c"]) * ((i["destruction"] or maintenant) - float(i["creation"])) / 3600
                   for i in self.instances if i["id"] != ident)

    def ecrire(self, chemin: Path) -> None:
        """v13 (P-3) : temporaire propre au processus, `fsync` (`_ecrire_atomique`)."""
        _ecrire_atomique(chemin, json.dumps({"b": self.b, "instances": self.instances}, sort_keys=True))

    @classmethod
    def lire(cls, chemin: Path) -> "Poste":
        d = json.loads(Path(chemin).read_text(encoding="utf-8"))
        return cls(b=float(d["b"]), instances=list(d["instances"]))


def instances_du_poste(anterieures: list[dict], b: float) -> list[dict]:
    """Correction 2 : chaque instance antérieure (lue dans `registres/depenses.md`) porte id, c, création, destruction
    et le B en vigueur à sa création ; tous égaux au B du manifeste (B fixé à la création de la première instance)."""
    out = []
    for i in anterieures:
        for cle in ("id", "c", "creation", "destruction", "B"):
            if cle not in i:
                raise GardeArret(f"instance antérieure : champ « {cle} » absent")
        if i["destruction"] is None:
            raise GardeArret("instance antérieure non détruite")
        if float(i["B"]) != float(b):
            raise GardeArret("B différent de celui de la première instance du poste")
        out.append({k: i[k] for k in ("id", "c", "creation", "destruction")})
    return out


class Veilleur:
    """Secours (B-5, correction 3) : détruit l'instance par son identifiant (R10), sans transfert, à
    `B − marge_secours` ou à `échéance + delai_secours_s` (`delai_secours_s ≤ 0`, correction 5). L'arrêt nominal à
    B − 2 se fait sur l'instance, puis transfert, puis destruction par la conduite. Lit l'état du poste dans un fichier
    à chaque passage : tourne dans un processus séparé (`main(["veilleur", …])`), qui survit à la conduite.
    C2 : chaque passage est dans un `try` ; une erreur (poste illisible, destruction refusée) est écrite au journal et
    le passage suivant recommence, jusqu'à ce que la destruction réussisse ; poste illisible → dernier poste lu, ou,
    s'il n'y en a aucun, destruction (cause « poste illisible (secours) ») ; un battement est écrit à chaque passage.
    v11 (C-2) : avant de détruire, le statut de l'instance est lu ; « stopped » ou « exited » (arrêtée par son chien
    de garde) et une étape lancée sans transfert qui fait foi (fichier `rapatriement`, écrit par la conduite après son
    transfert ; absent : rien n'est tenu pour transféré) : **pas de destruction** (seul le stockage court), alerte
    « reprise requise » au journal, et le veilleur s'arrête (la reprise a son propre veilleur). Statut illisible ou
    instance en marche : destruction, comme en v10 (la borne de dépense prime).
    v12 (V-4) : un statut illisible est noté et relu au passage suivant ; la destruction n'a lieu qu'après
    `ESSAIS_DESTRUCTION` lectures illisibles de suite (une lecture lisible remet le compte à zéro). v12 (V-1) : le
    statut est celui de `statut_vast` (état voulu compris) : une instance en attente de démarrage n'est pas arrêtée.
    v13 (W-1, P-1) : sans transfert complet, une instance « en attente de démarrage » (dont un conteneur sorti voulu en
    marche) reçoit d'abord un arrêt par son identifiant (R10), et une instance « arrêt en cours » attend ; le statut est
    relu au passage suivant : arrêtée, gardée (« reprise requise ») ; toujours non arrêtée, ou `ESSAIS_DESTRUCTION`
    arrêts refusés : destruction. Transfert complet ou instance « running » : destruction, comme en v12."""

    def __init__(self, fournisseur: Fournisseur, poste_fichier: Path, instance: str, echeance: float, journal: Path,
                 marge_secours: float = MARGE_SECOURS_USD, delai_secours_s: float = 0.0, periode_s: float = 30.0,
                 horloge=time.time, attendre=time.sleep, battement: Path | None = None,
                 rapatriement: Path | None = None):
        if float(delai_secours_s) > 0:
            raise GardeArret("veilleur : délai de secours positif refusé (destruction au plus tard à l'échéance)")
        self.f, self.poste_fichier, self.instance = fournisseur, Path(poste_fichier), instance
        self.echeance, self.journal = float(echeance), Path(journal)
        self.marge, self.delai, self.periode = float(marge_secours), float(delai_secours_s), float(periode_s)
        self.horloge, self.attendre = horloge, attendre
        self.battement = Path(battement) if battement is not None else Path(str(self.journal) + ".battement")
        self.cause: str | None = None
        self.dernier_poste: Poste | None = None
        self.rapatriement = Path(rapatriement) if rapatriement is not None else \
            self.poste_fichier.parent / FICHIER_RAPATRIEMENT
        self.statuts_illisibles = 0  # v12 (V-4) : lectures illisibles de suite
        self.arrets_refuses = 0  # v13 (W-1) : arrêts demandés par ce veilleur et refusés
        self.relecture = False  # v13 (W-1, P-1) : arrêt accepté (ou en cours) : statut relu une fois avant de détruire

    def _noter(self, objet: dict) -> None:
        try:
            with open(self.journal, "a", encoding="utf-8") as j:
                j.write(json.dumps({**objet, "instance": self.instance, "t": self.horloge()}, ensure_ascii=False)
                        + "\n")
        except OSError:
            pass

    def _battre(self) -> None:
        try:
            tmp = Path(str(self.battement) + ".tmp")
            tmp.write_text(json.dumps({"t": time.time(), "pid": os.getpid()}), encoding="utf-8")
            os.replace(tmp, self.battement)
        except OSError:
            pass

    def _poste(self) -> Poste | None:
        """Poste lu au fichier ; illisible → dernier poste lu (erreur notée), ou `None` s'il n'y en a aucun."""
        try:
            self.dernier_poste = Poste.lire(self.poste_fichier)
        except Exception as err:
            self._noter({"erreur": f"poste illisible : {type(err).__name__}"})
        return self.dernier_poste

    def deja_detruite(self) -> bool:
        poste = self._poste()
        return poste is not None and any(i["id"] == self.instance and i["destruction"] is not None
                                         for i in poste.instances)

    def verifier(self, poste: Poste | None = None) -> str | None:
        maintenant = self.horloge()
        poste = self._poste() if poste is None else poste
        if poste is None:
            return "poste illisible (secours)"
        if poste.depense(maintenant) >= poste.b - self.marge:
            return "dépense (seuil de secours)"
        if maintenant >= self.echeance + self.delai:
            return "échéance du GO (secours)"
        return None

    def _passage(self) -> str | None:
        poste = self._poste()
        if poste is not None and any(i["id"] == self.instance and i["destruction"] is not None
                                     for i in poste.instances):
            return "déjà détruite"
        cause = self.verifier(poste)
        if not cause:
            return None
        self.cause = cause
        statut = self._statut()
        if statut is None:  # v12 (V-4) : relu au passage suivant ; destruction après ESSAIS_DESTRUCTION de suite
            self.statuts_illisibles += 1
            if self.statuts_illisibles < ESSAIS_DESTRUCTION:
                self._noter({"arret": cause, "statut": "illisible", "lectures_illisibles": self.statuts_illisibles,
                             "suite": "relu au passage suivant"})
                return None
            self._noter({"arret": cause, "statut": "illisible", "lectures_illisibles": self.statuts_illisibles,
                         "suite": "destruction (la borne de dépense prime)"})
        else:
            self.statuts_illisibles = 0
        complet = transfert_complet(self.rapatriement)
        if statut in STATUTS_ARRETES and not complet:
            self._noter({"arret": cause, "statut": statut, "destruction": "refusée : instance arrêtée, une étape sans "
                         "transfert qui fait foi ; seul le stockage court", "alerte": "reprise requise"})
            return REPRISE_REQUISE
        if not complet and not self.relecture and statut in (STATUT_EN_ATTENTE, STATUT_ARRET_EN_COURS):
            if statut == STATUT_ARRET_EN_COURS:  # v13 (P-1) : un arrêt est déjà accepté : relu une fois
                self.relecture = True
                self._noter({"arret": cause, "statut": statut, "suite": "relu au passage suivant avant destruction"})
                return None
            try:  # v13 (W-1) : conteneur sorti ou attente d'une carte : arrêt par l'identifiant (R10), puis relecture
                self.f.arreter(self.instance)
            except Exception as err:
                self.arrets_refuses += 1
                self._noter({"arret": cause, "statut": statut, "arret_demande": f"refusé : {type(err).__name__}",
                             "arrets_refuses": self.arrets_refuses})
                if self.arrets_refuses < ESSAIS_DESTRUCTION:
                    return None
                self._noter({"arret": cause, "suite": f"destruction après {self.arrets_refuses} arrêts refusés"})
            else:
                self.relecture = True
                self._noter({"arret": cause, "statut": statut, "arret_demande": "accepté",
                             "suite": "statut relu au passage suivant ; arrêtée : gardée (reprise requise)"})
                return None
        elif not complet and self.relecture and statut not in STATUTS_ARRETES:
            self._noter({"arret": cause, "statut": statut, "suite": "toujours non arrêtée après relecture : destruction"})
        self.f.detruire(self.instance)  # une exception ici : notée, retentée au passage suivant
        self._noter({"arret": cause})
        try:
            poste = Poste.lire(self.poste_fichier)
            poste.detruite(self.instance, self.horloge())
            poste.ecrire(self.poste_fichier)
        except Exception as err:
            self._noter({"erreur": f"poste non mis à jour après destruction : {type(err).__name__}"})
        return cause

    def _statut(self) -> str | None:
        try:
            return self.f.statut(self.instance)
        except Exception as err:
            self._noter({"statut": f"illisible : {type(err).__name__}"})
            return None

    def boucle(self, passages: int | None = None) -> str | None:
        n = 0
        while passages is None or n < passages:
            n += 1
            self._battre()
            try:
                cause = self._passage()
                if cause == "déjà détruite":
                    return None
                if cause:
                    return cause
            except Exception as err:  # C2 : jamais de sortie sur une erreur ; retenté à la période suivante
                self._noter({"erreur": f"{type(err).__name__}: {err}"[:300], "cause_visee": self.cause})
            self.attendre(self.periode)
        return None


REPRISE_REQUISE = "reprise requise"


def transfert_complet(chemin: Path) -> bool:
    """v11 (C-2) : vrai seulement si la conduite a écrit, après son transfert, que chaque étape lancée a un transfert
    qui fait foi (`{"complet": true, …}`) ; fichier absent ou illisible : faux."""
    try:
        return json.loads(Path(chemin).read_text(encoding="utf-8")).get("complet") is True
    except Exception:
        return False


class VeilleurArret:
    """v11 (C-1) : veilleur local de la reprise, processus détaché lancé **avant** tout redémarrage. À l'échéance
    (`début + delai_prete_s + DELAI_COMMANDE_S + minuterie_s`, ou l'échéance du GO si elle vient avant, ou tout de
    suite pour la remise à l'arrêt non confirmée), il arrête l'instance **par son identifiant** (R10 ; arrêt, jamais
    destruction), puis relit son statut à chaque période et retente l'arrêt tant qu'elle n'est ni « stopped » ni
    « exited » ; il finit quand elle l'est, ou quand elle n'est plus dans l'inventaire de l'étiquette (détruite). Chaque
    passage est dans un `try` (erreur notée, retentée) ; un battement est écrit à chaque passage.
    v12 (V-1) : il ne finit (« arrêtée ») qu'après au moins un arrêt **accepté** depuis son échéance, **puis** un
    statut arrêté relu à un passage suivant (statut de `statut_vast`, état voulu compris) ; un statut « stopped » lu
    sans arrêt accepté (redémarrage en attente d'une carte, lu sur l'état réel seul) ne le fait jamais finir : il
    demande l'arrêt, qui annule aussi l'attente (documentation de Vast : « Cancel scheduling by clicking stop
    again »)."""

    def __init__(self, fournisseur: Fournisseur, instance: str, etiquette: str, echeance: float, journal: Path,
                 periode_s: float = 30.0, horloge=time.time, attendre=time.sleep, battement: Path | None = None):
        self.f, self.instance, self.etiquette = fournisseur, str(instance), etiquette
        self.echeance, self.journal, self.periode = float(echeance), Path(journal), float(periode_s)
        self.horloge, self.attendre = horloge, attendre
        self.battement = Path(battement) if battement is not None else Path(str(self.journal) + ".battement")
        self.essais = 0
        self.arret_accepte = False  # v12 (V-1) : un arrêt accepté depuis l'échéance

    _noter = Veilleur._noter
    _battre = Veilleur._battre

    def _passage(self) -> str | None:
        if self.horloge() < self.echeance:
            return None
        try:
            statut = self.f.statut(self.instance)
        except Exception as err:
            statut = None
            self._noter({"statut": f"illisible : {type(err).__name__}"})
            try:
                if self.instance not in [str(i) for i in self.f.inventaire(self.etiquette)]:
                    self._noter({"fin": "instance absente de l'inventaire de l'étiquette (détruite)"})
                    return "détruite"
            except Exception as e2:
                self._noter({"inventaire": f"illisible : {type(e2).__name__}"})
        if statut in STATUTS_ARRETES and self.arret_accepte:  # v12 (V-1) : arrêt accepté, puis statut arrêté relu
            self._noter({"fin": "instance arrêtée", "statut": statut, "essais": self.essais})
            return "arrêtée"
        self.essais += 1
        self.f.arreter(self.instance)  # une exception ici : notée, retentée au passage suivant
        self.arret_accepte = True
        self._noter({"arret": "demandé et accepté", "essai": self.essais, "statut_lu": statut})
        return None  # le statut est relu au passage suivant

    def boucle(self, passages: int | None = None) -> str | None:
        n = 0
        while passages is None or n < passages:
            n += 1
            self._battre()
            try:
                fin = self._passage()
                if fin:
                    return fin
            except Exception as err:  # jamais de sortie sur une erreur ; retenté à la période suivante
                self._noter({"erreur": f"{type(err).__name__}: {err}"[:300], "essai": self.essais})
            self.attendre(self.periode)
        return None


def lancer_veilleur_arret_processus(ident: str, etiquette: str, echeance: float, journal: Path,
                                    fournisseur: str | None, periode_s: float = 30.0) -> int:
    """v11 (C-1) : `lanceur_v18 veilleur-arret`, processus séparé, nouvelle session (survit à la reprise). Rend son
    PID. Fournisseur inconnu (`None`) : refusé (jamais de veilleur qui joindrait un fournisseur non voulu)."""
    if fournisseur is None:
        raise GardeArret("veilleur d'arrêt : fournisseur inconnu")
    cmd = [sys.executable, "-m", VEILLEUR_MODULE, "veilleur-arret", "--instance", str(ident), "--etiquette",
           etiquette, "--echeance", repr(float(echeance)), "--journal", os.path.abspath(str(journal)),  # v13 (P-2)
           "--fournisseur", fournisseur,
           "--periode", repr(float(periode_s))]
    with open(str(journal) + ".err", "ab") as err:
        p = subprocess.Popen(cmd, start_new_session=True, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                             stderr=err)
    _VEILLEURS[p.pid] = p
    return p.pid


def lancer_veilleur_processus(poste_fichier: Path, ident: str, echeance: float, journal: Path,
                              fournisseur: str = "vast", periode_s: float = 30.0,
                              marge_secours: float = MARGE_SECOURS_USD) -> int:
    """Processus séparé, nouvelle session (survit à la conduite et à la coupure de son terminal). Rend son PID. Sa
    sortie d'erreur va dans `<journal>.err` ; son battement dans `<journal>.battement` (C2)."""
    cmd = [sys.executable, "-m", VEILLEUR_MODULE, "veilleur", "--poste", str(poste_fichier),
           "--instance", str(ident), "--echeance", repr(float(echeance)), "--journal", str(journal),
           "--fournisseur", fournisseur, "--periode", repr(float(periode_s)), "--marge", repr(float(marge_secours))]
    with open(str(journal) + ".err", "ab") as err:
        p = subprocess.Popen(cmd, start_new_session=True, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                             stderr=err)
    _VEILLEURS[p.pid] = p
    return p.pid


_VEILLEURS: dict[int, subprocess.Popen] = {}  # remarque R10 (v5) : veilleurs lancés par ce processus, par PID


def processus_vivant(pid: int) -> bool:
    """Vivant et non zombie. Un veilleur lancé par ce processus est suivi par son `Popen` (récolté par `poll`, qui le
    sait ensuite fini) ; un autre PID n'est jamais récolté ici (v5) : son état est lu dans `/proc`."""
    p = _VEILLEURS.get(int(pid))
    if p is not None:
        return p.poll() is None
    statut = Path(f"/proc/{int(pid)}/status")
    try:
        for ligne in statut.read_text().splitlines():
            if ligne.startswith("State:"):
                return "Z" not in ligne.split()[1]
    except OSError:
        pass
    try:
        os.kill(int(pid), 0)
    except (ProcessLookupError, PermissionError):
        return False
    return True


def verifier_veilleur(pid: int | None, journal: Path, delai_s: float = 20.0, fraicheur_s: float = 180.0) -> bool:
    """C2 : le veilleur vit (PID vivant, non zombie) et a écrit un battement depuis moins de `fraicheur_s`. Attend au
    plus `delai_s` le premier battement."""
    if pid is None:
        return False
    battement = Path(str(journal) + ".battement")
    fin = time.time() + float(delai_s)
    while True:
        if not processus_vivant(pid):
            return False
        try:
            t = float(json.loads(battement.read_text(encoding="utf-8"))["t"])
            if time.time() - t <= float(fraicheur_s):
                return True
        except (OSError, ValueError, KeyError):
            pass
        if time.time() >= fin:
            return False
        time.sleep(0.2)


def identite_veilleur_arret(pid: int, journal) -> bool | None:
    """v13 (P-2) : le PID est-il encore le veilleur d'arrêt de ce journal ? Vrai si le processus vit (ni fini, ni
    zombie) et que sa ligne de commande porte `veilleur-arret` et `--journal <journal>` ; faux s'il est fini ou si le PID
    est celui d'un autre processus (jamais signalé alors) ; `None` si l'identité est illisible. La ligne de commande
    sert à vérifier l'identité d'un PID connu, jamais à choisir un processus (R10)."""
    p = _VEILLEURS.get(int(pid))
    if p is not None and p.poll() is not None:
        return False
    try:
        brut = Path(f"/proc/{int(pid)}/cmdline").read_bytes()
    except FileNotFoundError:
        return False
    except OSError:
        return None
    args = [a.decode("utf-8", "replace") for a in brut.split(b"\0") if a]
    if "veilleur-arret" not in args or "--journal" not in args:
        return False  # fini (zombie : ligne vide) ou PID réemployé
    i = args.index("--journal")
    return i + 1 < len(args) and os.path.abspath(args[i + 1]) == os.path.abspath(str(journal))


def arreter_veilleur(pid: int) -> None:
    """R10 : par PID. v5 : un veilleur lancé par ce processus est signalé par son `Popen`, qui ne signale jamais un
    processus déjà récolté (PID peut-être réemployé)."""
    p = _VEILLEURS.get(int(pid))
    if p is not None:
        p.send_signal(signal.SIGTERM)  # sans effet si `poll` l'a déjà récolté
        return
    try:
        os.kill(int(pid), signal.SIGTERM)
    except ProcessLookupError:
        pass


# --- amorce et commandes distantes ------------------------------------------------------------------------------------

def fabriquer_archive(depot: Path, commit: str, dossier: Path,
                      chemins: tuple[str, ...] = CHEMINS_ARCHIVE) -> tuple[Path, str]:
    """Correction 12 et C6 : archive `git archive` du commit du code, **limitée aux fichiers de `src/` dont l'instance
    a besoin** (`CHEMINS_ARCHIVE`) ; dépôt privé : rien n'est cloné sur l'instance ; aucun fichier de `docs/`,
    `donnees/`, `diag/`, `registres/`, ni le reste de `src/`, ne part sur l'hôte loué."""
    if not chemins or any(not c.startswith("src/") or ".." in c for c in chemins):
        raise GardeArret("archive du code : chemins hors de src/")
    dossier.mkdir(parents=True, exist_ok=True)
    sortie = dossier / f"travail-{commit[:12]}.tar.gz"
    try:
        subprocess.run(["git", "-C", str(depot), "archive", "--format=tar.gz", "-o", str(sortie), commit, "--",
                        *chemins], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise GardeArret("archive du code : commit introuvable ou dépôt illisible") from None
    return sortie, cv.sha_fichier(sortie)


def commande_chien(depense: str, echeance: float, marge_transfert_s: float = MARGE_TRANSFERT_S,
                   marge_secours: float = MARGE_SECOURS_USD, d_abandon_s: float = D_ABANDON_S,
                   prise_en_charge_s: float = DELAI_PRISE_EN_CHARGE_S, periode_s: float = PERIODE_CHIEN_S) -> str:
    """v10 : lancement détaché du chien de garde (`instance_v10 chien-de-garde`), vérifié (`LANCE <pid>`)."""
    return commande_detachee(CHIEN, commande_instance(
        CHIEN, racine="/root", depense=depense, echeance_go=repr(float(echeance)),
        marge_transfert=repr(float(marge_transfert_s)), marge_secours=repr(float(marge_secours)),
        d_abandon=repr(float(d_abandon_s)), prise_en_charge=repr(float(prise_en_charge_s)),
        periode=repr(float(periode_s))))


def script_amorce(manifeste: dict, sha_archive: str, chien: str | None = None) -> str:
    """Archive du code vérifiée par son empreinte puis dépliée ; dépôt public à son commit (jamais copié dans le dépôt
    de travail) ; Python 3.11 ; versions et commits du manifeste ; modèle, adaptateur du juge et base à leurs
    révisions, `refs/main` posé sur chacune (B-4). Le jeton est lu dans un fichier envoyé par `scp`, effacé à la sortie
    du script, quelle qu'elle soit. v10 : `chien` (`commande_chien`) est lancé dès l'environnement Python prêt, avant
    les téléchargements ; lancement non vérifié : amorce en échec."""
    v = manifeste["versions"]
    paquets = " ".join(shlex.quote(f"{p}=={x}") for p, x in sorted(v.items()) if p not in manifeste["git"])
    git = " ".join(shlex.quote(f"{p} @ git+{u}@{c}") for p, (u, c) in sorted(manifeste["git"].items()))
    echec = lambda cause: ("{ echo ETAT " + shlex.quote(json.dumps({"commande": "amorce", "finie": False,
                                                                    "cause": cause}, ensure_ascii=False))
                           + "; exit 3; }")
    py = "python" + str(manifeste["python"])
    lignes = ["set -euo pipefail", f"trap 'rm -f {JETON_DISTANT}' EXIT", "cd /root",
              f"echo {shlex.quote(sha_archive + '  ' + ARCHIVE_DISTANTE)} | sha256sum -c --quiet - || "
              + echec("empreinte de l'archive du code"),
              f"mkdir -p /root/travail && tar -xzf {ARCHIVE_DISTANTE} -C /root/travail",
              f"git init -q public && git -C public fetch -q --depth=1 {cv.DEPOT_PUBLIC} {cv.COMMIT_PUBLIC}"
              " && git -C public checkout -q FETCH_HEAD",
              f"command -v {py} > /dev/null || " + echec("Python " + str(manifeste["python"]) + " absent"),
              f"{py} -m venv /root/venv && . /root/venv/bin/activate",
              f"pip install -q {paquets}" + (f" {git}" if git else ""),
              f"pip install -q --no-deps -e /root/public/{cv.SOUS_DOSSIER}",
              *([f"{{ {chien} ; }} | grep '^LANCE ' > /dev/null || " + echec("chien de garde non lancé")] if chien else []),
              f"export HF_HUB_CACHE={CACHE_HF}",
              f"test -s {JETON_DISTANT} || " + echec("jeton absent")]
    for depot, rev in ((cv.MODELE, manifeste["revision_modele"]),
                       (cv.JUGE, manifeste["juge"]["revision_adaptateur"]),
                       (cv.JUGE_BASE, manifeste["juge"]["revision_base"])):
        refs = f"{CACHE_HF}/models--{depot.replace('/', '--')}/refs"
        lignes += [f"huggingface-cli download {depot} --revision {shlex.quote(rev)} --quiet > /dev/null",
                   f"mkdir -p {refs} && printf %s {shlex.quote(rev)} > {refs}/main"]
    lignes.append(f"rm -f {JETON_DISTANT}")
    lignes.append("echo ETAT " + shlex.quote(json.dumps({"commande": "amorce", "finie": True})))
    return "\n".join(lignes) + "\n"


def commande_instance(sous_commande: str, **opts) -> str:
    morceaux = [f". /root/venv/bin/activate && cd /root/travail && PYTHONPATH=src HF_HUB_OFFLINE=1 HF_HUB_CACHE={CACHE_HF}",
                f"python -m {INSTANCE_MODULE}", sous_commande]
    for k, v in opts.items():
        if v is True:  # v5 : option sans valeur (`--ecrire-etat`)
            morceaux.append(f"--{k.replace('_', '-')}")
        else:
            morceaux += [f"--{k.replace('_', '-')}", shlex.quote(str(v))]
    return " ".join(morceaux)


def _identite(p: str) -> str:
    """N-4 : identité d'un PID (expression shell `p`) : `boot_id` du noyau et heure de départ du processus (champ 22 de
    `/proc/<pid>/stat`, compté après le nom entre parenthèses, d'où le champ 20 une fois le nom retiré)."""
    return (f"$(cat /proc/sys/kernel/random/boot_id 2>/dev/null) "
            f"$(sed 's/^.*) //' /proc/{p}/stat 2>/dev/null | cut -d' ' -f20)")


def _meme_identite(p: str, debut: str) -> str:
    return f"[ \"{_identite(p)}\" = \"$(cat {debut} 2>/dev/null)\" ]"


def _pid_vit(pid: str, debut: str) -> str:
    """Test shell : le PID lu dans `pid` vit, n'est pas un zombie (`kill -0` réussit sur un zombie, d'où `/proc`) et
    a l'identité écrite à son lancement dans `debut` (N-4 : un PID réemployé n'est pas « vivant »)."""
    return (f"{{ [ -s {pid} ] && [ -s {debut} ] && kill -0 $(cat {pid}) 2>/dev/null && "
            f"! grep -qs '^State:[[:space:]]*Z' /proc/$(cat {pid})/status && "
            f"{_meme_identite(f'$(cat {pid})', debut)}; }}")


def commande_detachee(nom: str, commande: str) -> str:
    """P-f : la commande tourne détachée (nouvelle session) ; sa sortie reste sur l'instance ; seules la dernière ligne
    `ETAT` et une ligne `CODE n` sont écrites dans `<nom>.fin`, lu par `commande_sondage`. PID dans `<nom>.pid`.
    C4 : la commande rend `LANCE <pid>` une fois `<nom>.pid` écrit ; elle est idempotente : si `<nom>.fin` existe ou si
    le PID vit déjà, rien n'est relancé (un second essai de lancement ne double jamais une exécution)."""
    d = ETATS_DISTANTS
    interne = (f"( {commande} ) > {d}/{nom}.log 2>&1; c=$?; "  # sous-shell : un `exit` n'empêche pas `.fin`
               f"{{ grep '^ETAT ' {d}/{nom}.log | tail -n 1; echo \"CODE $c\"; }} > {d}/{nom}.tmp; "
               f"mv {d}/{nom}.tmp {d}/{nom}.fin")
    pid, fin, debut = f"{d}/{nom}.pid", f"{d}/{nom}.fin", f"{d}/{nom}.debut"
    return (f"mkdir -p {d} && if [ -e {fin} ] || {_pid_vit(pid, debut)}; then :; "
            f"else setsid nohup bash -c {shlex.quote(interne)} > /dev/null 2>&1 < /dev/null & "
            f"p=$!; echo \"{_identite('$p')}\" > {debut}; echo $p > {pid}; fi; "  # N-4 : identité avant le PID
            f"test -s {pid} && echo \"LANCE $(cat {pid})\"")


def lancement_verifie(sortie: str) -> bool:
    return any(re.fullmatch(r"LANCE \d+", l.strip()) for l in sortie.splitlines())


def commande_chien_vivant(fraicheur_s: float = CHIEN_FRAICHEUR_S) -> str:
    """v11 (P-1) : imprime `CHIEN VIVANT` si le chien de garde vit (PID vivant, non zombie, à son identité) et que son
    battement date de moins de `fraicheur_s` (date du fichier, que le chien touche même disque plein) ; sinon
    `CHIEN MORT`."""
    d = ETATS_DISTANTS
    pid, debut, batt = f"{d}/{CHIEN}.pid", f"{d}/{CHIEN}.debut", f"{d}/{CHIEN}.battement"
    return (f"if {_pid_vit(pid, debut)} && [ -e {batt} ] && "
            f"[ $(( $(date +%s) - $(stat -c %Y {batt} 2>/dev/null || echo 0) )) -lt {int(fraicheur_s)} ]; "
            f"then echo 'CHIEN VIVANT'; else echo 'CHIEN MORT'; fi")


def commande_sondage(nom: str) -> str:
    """C4 : `.fin` s'il existe ; sinon `VIVANT` si le PID vit (`kill -0`, et non zombie), sinon `.fin` relu (fin entre les deux
    lectures), sinon `MORT` (processus disparu sans écrire son état : coupure de l'hôte). v10 : touche d'abord le
    battement de la conduite (`etats/battement-conduite`). v11 (P-1) : imprime d'abord la ligne `CHIEN VIVANT|MORT`
    (la dernière ligne reste celle de la commande)."""
    d = ETATS_DISTANTS
    pid, fin, debut = f"{d}/{nom}.pid", f"{d}/{nom}.fin", f"{d}/{nom}.debut"
    return (f"touch {d}/{BATTEMENT_CONDUITE} 2>/dev/null; "  # v10 : battement de la conduite, lu par le chien
            f"{commande_chien_vivant()}; "  # v11 (P-1)
            f"if [ -e {fin} ]; then cat {fin}; elif {_pid_vit(pid, debut)}; then "
            f"echo VIVANT; elif [ -e {fin} ]; then cat {fin}; else echo MORT; fi")


def lire_chien(code: int | None, sortie: str) -> str | None:
    """v11 (P-1) : « vivant », « mort », ou `None` (sondage illisible, ou sans ligne `CHIEN`)."""
    if code != 0:
        return None
    for ligne in sortie.splitlines():
        if ligne.strip() == "CHIEN VIVANT":
            return "vivant"
        if ligne.strip() == "CHIEN MORT":
            return "mort"
    return None


def lire_sondage(code: int | None, sortie: str) -> str:
    """« fin » (ligne `CODE`), « vivant », « mort », ou « échec » (sondage illisible : `ssh` en échec, rien rendu)."""
    if lire_code(sortie) is not None:
        return "fin"
    lignes = [l.strip() for l in sortie.splitlines() if l.strip()]
    if code == 0 and lignes and lignes[-1] == "VIVANT":
        return "vivant"
    if code == 0 and lignes and lignes[-1] == "MORT":
        return "mort"
    return "échec"


def commande_arret(nom: str, attente_s: float = 10.0) -> str:
    """R10 : arrêt du groupe de processus de la commande par son PID (identifiant), jamais par motif. v5 : le groupe
    n'est visé que si son meneur a l'identité écrite au lancement (N-4) ou n'existe plus (le numéro reste alors tenu
    par le groupe, qui ne peut être que celui de la commande) ; TERM, attente bornée de la fin du groupe, puis KILL
    (C10 : plus aucun membre du groupe après l'arrêt)."""
    d = ETATS_DISTANTS
    pid, debut = f"{d}/{nom}.pid", f"{d}/{nom}.debut"
    tours = max(1, int(float(attente_s) / 0.5))
    return (f"p=$(cat {pid} 2>/dev/null); if [ -n \"$p\" ] && {{ [ ! -e /proc/$p ] || "
            f"{_meme_identite('$p', debut)}; }}; then kill -TERM -- -$p 2>/dev/null; i=0; "
            f"while [ $i -lt {tours} ] && kill -0 -- -$p 2>/dev/null; do sleep 0.5; i=$((i+1)); done; "
            f"kill -0 -- -$p 2>/dev/null && kill -KILL -- -$p 2>/dev/null; fi; true")


def lire_etat(sortie: str) -> dict:
    """Seule la ligne `ETAT {…}` revient au poste local (A-9) ; le reste de la sortie est ignoré."""
    for ligne in reversed(sortie.splitlines()):
        if ligne.startswith("ETAT "):
            return json.loads(ligne[5:])
    raise GardeArret("commande distante sans ligne d'état")


def lire_code(sortie: str) -> int | None:
    for ligne in reversed(sortie.splitlines()):
        if ligne.startswith("CODE "):
            return int(ligne[5:].strip())
    return None


MORT_SANS_ETAT = "commande distante sans ligne d'état (coupure de l'hôte)"


def normaliser_execution(etat_: dict | None, code: int | None, phase: str,
                         message_defaut: str = "commande distante sans ligne d'état") -> dict:
    """État d'une exécution tel que la liste d'arrêt le lit. Une garde levée par la commande avant l'enfant (dossier
    neuf, configuration effective) ou une commande sans ligne d'état devient une exécution en échec, sans tour. C4 :
    une exécution morte sans `.fin` porte `MORT_SANS_ETAT` ; ses tours complets sont relus par la conduite."""
    if etat_ is not None and "code_retour" in etat_:
        return etat_
    message = (etat_ or {}).get("garde_tombee") or message_defaut
    return {"commande": "executer", "phase": phase, "code_retour": code if code not in (None, 0) else 1,
            "cause_arret": "garde de démarrage" if "configuration effective" in message else None,
            "gardes_tombees": [message], "tours_marques": 0, "tours_complets": 0, "durees": {},
            "configuration_effective": "non décidée", "message": message}


def transferer(fournisseur: Fournisseur, ident: str, distant: str, local: Path, empreintes_instance: dict,
               erreurs: list | None = None) -> list[dict]:
    """Fichier par fichier, la seule liste fermée (B-6) ; un transfert, puis au plus un nouveau si une empreinte
    diffère. Un `scp` en échec est un écart (fichier absent du transfert), consigné dans `erreurs`, jamais une
    exception qui sort (correction 3). Rend les empreintes de chaque essai."""
    if not set(empreintes_instance) <= set(SORTANTS):  # v14
        raise GardeArret("transfert : fichier hors de la liste fermée")
    essais = []
    for n in range(2):
        cible = local / f"transfert-{n + 1}"
        for rel in empreintes_instance:
            try:
                fournisseur.rapatrier_fichier(ident, f"{distant}/{rel}", cible / rel)
            except Exception as err:  # écart de transfert, consigné
                if erreurs is not None:
                    erreurs.append({"essai": n + 1, "fichier": rel, "erreur": type(err).__name__})
        obtenues = {rel: cv.sha_fichier(cible / rel) for rel in empreintes_instance if (cible / rel).is_file()}
        essais.append(obtenues)
        if obtenues == empreintes_instance:
            break
    return essais


def ordre_de_lancement(go_id: str, b: float, c: float, commit_code: str, etiquette: str | None = None) -> dict:
    """Condition 8 : l'ordre cite le GO, B, le taux relevé et DEPOT_URL ; v5 : et l'étiquette de l'instance (C11,
    inventaire R10)."""
    return {"GO_ID": go_id, "B": b, "c": c, "DEPOT_URL": DEPOT_URL, "commit_code": commit_code,
            "etiquette": etiquette, "heure": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


def envoyer_jeton(fournisseur: Fournisseur, ident: str, variable: str = "HF_TOKEN") -> None:
    """S-3 : jeton lu dans l'environnement du poste local (jamais imprimé), écrit dans un fichier temporaire local de
    droits 600, envoyé par `scp`, puis effacé localement ; jamais sur une ligne de commande."""
    valeur = os.environ.get(variable)
    if not valeur:
        raise GardeArret(f"jeton d'accès absent de l'environnement local ({variable})")
    fd, chemin = tempfile.mkstemp(prefix="jeton-")
    try:
        os.fchmod(fd, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(valeur)
        fournisseur.executer(ident, f"mkdir -p {Path(JETON_DISTANT).parent} && chmod 700 {Path(JETON_DISTANT).parent}")
        fournisseur.envoyer_fichier(ident, Path(chemin), JETON_DISTANT)
        fournisseur.executer(ident, f"chmod 600 {JETON_DISTANT}")
    finally:
        Path(chemin).unlink(missing_ok=True)


# --- conduite (A-8) ---------------------------------------------------------------------------------------------------

class _Arret(Exception):
    """Arrêt de la liste d'arrêt décidé par la conduite (dépense, échéance, instance injoignable, veilleur mort) :
    consigné au bilan."""


@dataclass
class Conduite:
    """Déroulé complet d'un poste sur une instance. `sortie` : dossier local neuf (bilan, manifestes versionnés,
    transferts scellés, journal des étapes `conduite-v5.jsonl`, état du poste `poste-v5.json`, journal du veilleur
    `arrets-v5.jsonl`). `texte_go` : `registres/go.md` de `origin/main` (`texte_go_main`, P-i), vérifié ici."""
    fournisseur: Fournisseur
    manifeste_local: Path
    sortie: Path
    go_id: str
    texte_go: str
    offre: str
    image: str
    depot_local: Path
    instances_anterieures: list[dict]
    disque_go: int = 200
    horloge: object = time.time
    attendre: object = time.sleep
    periode_sondage_s: float = 60.0
    marge_secours: float = MARGE_SECOURS_USD
    marge_transfert_s: float = MARGE_TRANSFERT_S
    seuil_local_usd: float = SEUIL_LOCAL_USD
    sondages_en_echec_max: int = SONDAGES_EN_ECHEC_MAX
    duree_sans_sondage_max_s: float = DUREE_SANS_SONDAGE_MAX_S
    delai_prete_s: float = DELAI_PRETE_S
    periode_prete_s: float = 15.0
    periode_veilleur_s: float = 30.0
    fournisseur_veilleur: str = "vast"
    lancer_veilleur: object = lancer_veilleur_processus
    arreter_veilleur: object = arreter_veilleur
    veilleur_vivant: object = None  # (pid, journal) -> bool ; défaut : `verifier_veilleur`
    d_abandon_s: float = D_ABANDON_S  # v10 : passé au chien de garde
    prise_en_charge_s: float = DELAI_PRISE_EN_CHARGE_S  # v10 : passé au chien de garde
    relance_seule: dict | None = None  # v18 : {"tours_complets_premiere", "regle_premiere", "source"} (addendum 5)

    def _etape(self, objet: dict) -> None:
        with open(self.sortie / "conduite-v5.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({**objet, "t": self.horloge()}, ensure_ascii=False, sort_keys=True, default=str) + "\n")

    # --- veilleur (C2) ---
    def _lancer_veilleur(self, echeance: float | None = None) -> None:
        self.pid_veilleur = self.lancer_veilleur(self.poste_fichier, self.ident,
                                                 self.echeance if echeance is None else echeance, self.journal_arrets,
                                                 self.fournisseur_veilleur, self.periode_veilleur_s,
                                                 self.marge_secours)

    def _veilleur_ok(self) -> bool:
        if self.veilleur_vivant is not None:
            return bool(self.veilleur_vivant(self.pid_veilleur, self.journal_arrets))
        return verifier_veilleur(self.pid_veilleur, self.journal_arrets,
                                 fraicheur_s=max(180.0, 4 * float(self.periode_veilleur_s)))

    def _garde_veilleur(self) -> None:
        """C2 : veilleur vivant, sinon une relance ; mort après la relance → arrêt (transfert, destruction)."""
        if self._veilleur_ok():
            return
        self._etape({"veilleur": "non vivant", "pid": self.pid_veilleur})
        if self.pid_veilleur is not None:
            self.arreter_veilleur(self.pid_veilleur)
        self._lancer_veilleur()
        if not self._veilleur_ok():
            raise _Arret("veilleur de secours non vivant, relance comprise : arrêt avant toute autre commande")
        self._etape({"veilleur": "relancé", "pid": self.pid_veilleur})

    # bornes : dépense du poste à B − 2, échéance moins la marge de transfert
    def _borne(self) -> float:
        maintenant = self.horloge()
        reste = (self.b - 2 - self.poste.depense(maintenant)) / self.c * 3600
        return min(maintenant + reste, self.echeance - self.marge_transfert_s)

    def _avant(self, quoi: str) -> None:
        self._garde_veilleur()
        maintenant = self.horloge()
        if self.poste.depense(maintenant) >= self.b - 2:
            raise _Arret(f"dépense du poste ≥ B − 2 avant « {quoi} »")
        if maintenant >= self.echeance - self.marge_transfert_s:
            raise _Arret(f"échéance du GO (moins la marge de transfert) avant « {quoi} »")

    def _relever_taux(self) -> float:
        """C1 : dans le `try` ; trois essais (l'instance peut charger encore) ; l'erreur du dernier sort."""
        for n in range(3):
            try:
                return float(self.fournisseur.taux_horaire(self.ident))
            except Exception:
                if n == 2:
                    raise
                self.attendre(self.periode_prete_s)
        raise AssertionError  # jamais atteint

    def _attendre_prete(self) -> None:
        """C5 : état « running » puis `ssh … true` accepté, borné par `delai_prete_s` ; la dépense court (D)."""
        debut = self.horloge()
        while True:
            self._avant("attente de l'instance prête")
            try:
                statut = self.fournisseur.statut(self.ident)
            except Exception:
                statut = None
            if statut == "running":
                try:
                    code, _ = self.fournisseur.executer(self.ident, "true", 60)
                except Exception:
                    code = None
                if code == 0:
                    self._etape({"instance_prete": True, "attente_s": self.horloge() - debut})
                    return
            if self.horloge() - debut >= self.delai_prete_s:
                raise _Arret("instance non prête dans le délai (état « running » et ssh) : arrêt et destruction")
            self.attendre(self.periode_prete_s)

    def _arreter_en_cours(self, cause: str = "arrêt par la conduite") -> None:
        """R10 et C3 : la commande en cours est arrêtée par son PID ; erreur consignée, jamais levée. v5 (C8) : la
        cause est notée (`arretees`), pour l'état reconstitué de l'exécution avant les empreintes."""
        nom, self.en_cours = self.en_cours, None
        if nom is None:
            return
        self.arretees.setdefault(nom, cause)
        self._arreter_groupe(nom)

    def _arreter_groupe(self, nom: str) -> None:
        try:
            code, _ = self.fournisseur.executer(self.ident, commande_arret(nom), 120)
            self._etape({"commande": nom, "arret_par_pid": code})
        except Exception as err:
            self._etape({"commande": nom, "arret_par_pid": f"{type(err).__name__}"})

    def _lancer(self, nom: str, commande: str) -> None:
        """C4 : lancement détaché vérifié (`LANCE <pid>`) ; un second essai (idempotent), puis arrêt."""
        for essai in (1, 2):
            try:
                code, sortie = self.fournisseur.executer(self.ident, commande_detachee(nom, commande), 120)
            except Exception:
                code, sortie = None, ""
            if code == 0 and lancement_verifie(sortie):
                return
            self._etape({"commande": nom, "lancement": "non vérifié", "essai": essai, "code": code})
            if essai == 1:
                self.attendre(self.periode_sondage_s)
        raise _Arret(f"lancement de « {nom} » non vérifié après deux essais : arrêt")

    def _cmd(self, nom: str, commande: str, executer: bool = False) -> tuple[dict | None, int | None, str]:
        """Lance `commande` détachée sous le nom `nom`, puis la sonde jusqu'à sa fin, sa mort, ou une borne. Rend
        (état, code, issue), issue « fin » ou « mort » (C4). Sondages en échec tolérés (C3) jusqu'à
        `sondages_en_echec_max` consécutifs ou `duree_sans_sondage_max_s` sans réussite : instance injoignable, arrêt.
        Bornes : hors exécution, B − 2 et échéance − marge ; pour une exécution (qui s'arrête elle-même à B − 2 et à
        échéance − marge), échéance − marge/2 et le seuil local `B − seuil_local_usd` (C4)."""
        self._avant(nom)
        self.lances.append(nom)
        self._etape({"commande": nom, "lancee": True})  # v11 (B-3) : la reprise lit les étapes lancées ici
        self.en_cours = nom
        self._lancer(nom, commande)
        echecs, dernier_ok = 0, self.horloge()
        while True:
            try:
                code, sortie = self.fournisseur.executer(self.ident, commande_sondage(nom), 120)
            except Exception:  # C3 : un sondage qui lève est un sondage en échec
                code, sortie = None, ""
            issue = lire_sondage(code, sortie)
            self._veiller_chien(lire_chien(code, sortie))  # v11 (P-1)
            maintenant = self.horloge()
            if issue == "fin":
                try:
                    e = lire_etat(sortie)
                except (GardeArret, ValueError):
                    e = None
                c = lire_code(sortie)
                self.en_cours = None
                self._etape({"commande": nom, "code": c, "etat": e})
                return e, c, "fin"
            if issue == "mort":
                self.en_cours = None
                self._etape({"commande": nom, "issue": MORT_SANS_ETAT})
                self._arreter_groupe(nom)  # C10 : un membre du groupe peut vivre encore ; avant `tours` et la relance
                return None, None, "mort"
            if issue == "vivant":
                echecs, dernier_ok = 0, maintenant
            else:
                echecs += 1
                self._etape({"commande": nom, "sondage": "échec", "consecutifs": echecs})
                if echecs >= self.sondages_en_echec_max or maintenant - dernier_ok >= self.duree_sans_sondage_max_s:
                    self._arreter_en_cours("instance injoignable")
                    raise _Arret(f"instance injoignable pendant « {nom} » ({echecs} sondages consécutifs en échec) : "
                                 "arrêt par PID tenté, transfert tenté, destruction ; nœud")
            if executer:
                if maintenant >= self.echeance - self.marge_transfert_s / 2:
                    self._arreter_en_cours("échéance du GO")
                    raise _Arret(f"borne d'échéance (échéance du GO moins la moitié de la marge de transfert) "
                                 f"atteinte pendant « {nom} » : arrêt par PID")
                if self.poste.depense(maintenant) >= self.b - self.seuil_local_usd:
                    self._arreter_en_cours("dépense")
                    raise _Arret(f"seuil local de dépense (D ≥ B − {self.seuil_local_usd:g} USD) atteint pendant "
                                 f"« {nom} » : arrêt par PID")
            elif maintenant >= self._borne():
                self._arreter_en_cours("dépense" if self.poste.depense(maintenant) >= self.b - 2 else "échéance du GO")
                raise _Arret(f"borne de dépense ou d'échéance atteinte pendant « {nom} » : arrêt par PID")
            self._garde_veilleur()
            self.attendre(self.periode_sondage_s)

    def _veiller_chien(self, chien: str | None) -> None:
        """v11 (P-1) : après la garde d'auto-arrêt, un chien de garde vu mort (PID, identité ou battement) est arrêté
        par son PID (R10 ; un chien bloqué ne survit pas à sa relance), son `.fin` effacé, puis relancé (lancement
        vérifié) ; une relance non vérifiée est notée et retentée au sondage suivant ; au-delà de
        `CHIEN_RELANCES_EN_ECHEC_ALERTE` relances non vérifiées de suite, alerte au bilan. Jamais d'arrêt du run pour
        cela : la conduite et le veilleur bornent la dépense tant que le poste vit."""
        if not self.chien_surveille or chien != "mort":
            return
        d = ETATS_DISTANTS
        commande = (f"{commande_arret(CHIEN)}; rm -f {d}/{CHIEN}.fin; "
                    + commande_chien(self._depense(), self.echeance, self.marge_transfert_s, self.marge_secours,
                                     self.d_abandon_s, self.prise_en_charge_s))
        try:
            code, sortie = self.fournisseur.executer(self.ident, commande, 120)
        except Exception:
            code, sortie = None, ""
        ok = code == 0 and lancement_verifie(sortie)
        self.chien_relances.append(ok)
        self._etape({"chien": "vu mort", "relance": "vérifiée" if ok else "non vérifiée", "code": code})
        echecs = 0
        for r in reversed(self.chien_relances):
            if r:
                break
            echecs += 1
        if echecs >= CHIEN_RELANCES_EN_ECHEC_ALERTE:
            self.alerte_chien = (f"chien de garde vu mort et non relancé ({echecs} relances non vérifiées de suite) : "
                                 "l'instance ne s'arrête plus d'elle-même si le poste s'éteint ; bornes : conduite et "
                                 "veilleur local")

    def _manifeste(self, nom: str, contenu: dict) -> str:
        """Correction 10 : manifeste versionné, écrit localement sans écrasement, scellé, envoyé sur l'instance."""
        local = self.sortie / MANIFESTES[nom]
        if local.exists():
            raise GardeArret("manifeste versionné déjà présent (R12)")
        local.write_text(json.dumps(contenu, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        scellement.sceller(local)
        distant = f"/root/{MANIFESTES[nom]}"
        self.fournisseur.envoyer_fichier(self.ident, local, distant)
        return distant

    def _depense(self) -> str:
        return json.dumps({"d_avant": self.poste.d_avant(self.ident, self.horloge()), "c": self.c,
                           "creation": self.creation, "b": self.b})

    def _tours_relus(self, phase: str, cause: str = "coupure de l'hôte") -> dict | None:
        """C4 et C8 : exécution sans état : sur l'instance, l'état absent est écrit (« reconstitué », jamais
        d'écrasement, `cause`), et les tours complets et gardes tombées sont relus, sans note."""
        try:
            _code, sortie = self.fournisseur.executer(self.ident, commande_instance(
                "tours", travail=f"/root/x/{phase}", ecrire_etat=True, phase=phase,
                manifeste=self.manifestes_phase[phase], cause=cause), 600)
            t = lire_etat(sortie)
            r = {"tours_complets": int(t["tours_complets"]), "gardes_tombees": list(t.get("gardes_tombees", [])),
                 "journal_absent": t.get("journal_absent"), "etat_execution": t.get("etat_execution"),
                 "lignes_tronquees_ignorees": list(t.get("lignes_tronquees_ignorees") or [])}
            self._etape({"commande": phase, "etat_reconstitue": r, "cause": cause})
            return r
        except Exception as err:
            self._etape({"commande": phase, "etat_reconstitue": f"échec : {type(err).__name__}", "cause": cause})
            return None

    def _executer(self, phase: str, manifeste: str) -> dict:
        self.manifestes_phase[phase] = manifeste
        e, code, issue = self._cmd(phase, commande_instance(
            "executer", travail=f"/root/x/{phase}", phase=phase, depense=self._depense(), echeance_go=self.echeance,
            marge_transfert=self.marge_transfert_s, manifeste=manifeste, clone="/root/public"), executer=True)
        if issue == "mort":
            r = normaliser_execution(None, None, phase, MORT_SANS_ETAT)
            t = self._tours_relus(phase, "coupure de l'hôte")
            if t is None:
                # M-1 : la reconstitution a échoué ; elle est retentée avant les empreintes (`_finir`)
                self.arretees.setdefault(phase, "coupure de l'hôte")
                r["tours_complets"] = None  # inconnu : aucune relance (la liste exige < 20 tours complets)
            else:
                r["tours_complets"] = t["tours_complets"]
                r["journal_absent"] = t["journal_absent"]
                r["etat_execution"] = t["etat_execution"]
                r["lignes_tronquees_ignorees"] = t["lignes_tronquees_ignorees"]  # v7 (C-2)
                r["gardes_tombees"] += [g for g in t["gardes_tombees"] if g not in r["gardes_tombees"]]
            return r
        return normaliser_execution(e, code, phase)

    def conduire(self) -> dict:
        man = json.loads(Path(self.manifeste_local).read_text(encoding="utf-8"))
        self.b = float(man["B"])
        anterieures = instances_du_poste(self.instances_anterieures, self.b)
        if self.texte_go != texte_go_main(Path(self.depot_local)):
            raise GardeArret("condition 2 (P-i) : le texte de GO passé n'est pas registres/go.md de origin/main")
        go = ligne_go(self.texte_go, self.go_id)
        verifier_go(go, self.b)
        verifier_non_revoque(self.texte_go, self.go_id)
        self.echeance = echeance_epoch(go["echeance"])
        if not float(self.marge_secours) < float(self.seuil_local_usd) < 2:
            raise GardeArret("seuil local de dépense hors de ]B − 2, B − marge de secours[ (C4)")
        if os.environ.get("GO_ID") != self.go_id:
            raise GardeArret("condition 2 : GO_ID absent ou différent de la ligne citée")
        if not os.environ.get("HF_TOKEN"):
            raise GardeArret("jeton d'accès absent de l'environnement local (HF_TOKEN)")
        if self.relance_seule is not None:  # v18 : gardes d'entrée, avant toute création d'instance
            verifier_relance_seule(self.relance_seule)
        if self.sortie.exists() and any(self.sortie.iterdir()):
            raise GardeArret("dossier de sortie de la conduite non neuf")
        self.sortie.mkdir(parents=True, exist_ok=True)
        archive, sha_archive = fabriquer_archive(Path(self.depot_local), man["commit_code"], self.sortie / "archive")
        self.poste = Poste(b=self.b, instances=anterieures)
        if self.poste.depense(self.horloge()) >= self.b - 2:
            raise GardeArret("dépense du poste ≥ B − 2 avant la création : rien ne tourne")
        self.lances: list[str] = []
        self.en_cours: str | None = None
        self.pid_veilleur: int | None = None
        self.c: float | None = None
        self.poste_fichier = self.sortie / "poste-v5.json"
        self.journal_arrets = self.sortie / "arrets-v5.jsonl"
        self.arretees: dict[str, str] = {}
        self.manifestes_phase: dict[str, str] = {}
        self.etiquette = PREFIXE_ETIQUETTE + uuid.uuid4().hex[:16]  # C11 : unique par conduite
        self.chien_surveille = False  # v11 (P-1) : vrai après la garde d'auto-arrêt
        self.chien_relances: list[bool] = []
        self.alerte_chien: str | None = None
        try:
            self.ident = self.fournisseur.creer(self.offre, self.image, self.disque_go, self.etiquette)
        except Exception as err:  # C11 : l'instance peut exister quand même
            self._creation_incertaine(err, sha_archive)
            raise
        self.creation = self.horloge()
        bilan = {"instance": self.ident, "etiquette": self.etiquette, "archive_sha256": sha_archive}
        try:  # C1 : ouvert aussitôt après la création
            self._etape({"instance": self.ident, "creee": self.creation})
            self.c = self._relever_taux()
            self.poste.ajouter(self.ident, self.c, self.creation)
            self.poste.ecrire(self.poste_fichier)
            bilan["d_avant_creation"] = self.poste.d_avant(self.ident, self.creation)
            self._etape({"instance": self.ident, "c": self.c, "archive_sha256": sha_archive,
                         "ordre": ordre_de_lancement(self.go_id, self.b, self.c, man["commit_code"],
                                                     self.etiquette)})
            self._lancer_veilleur()
            self._garde_veilleur()
            verifier_echeance(self.echeance, self.creation, self.b, self.c, self.marge_secours, self.marge_transfert_s)
            self._attendre_prete()
            self._avant("amorce")
            self.fournisseur.envoyer_fichier(self.ident, archive, ARCHIVE_DISTANTE)
            amorce = self.sortie / "amorce-v5.sh"
            amorce.write_text(script_amorce(man, sha_archive, commande_chien(
                self._depense(), self.echeance, self.marge_transfert_s, self.marge_secours, self.d_abandon_s,
                self.prise_en_charge_s)), encoding="utf-8")
            self.fournisseur.envoyer_fichier(self.ident, amorce, "/root/amorce-v5.sh")
            envoyer_jeton(self.fournisseur, self.ident)
            e, _, _ = self._cmd("amorce", "bash /root/amorce-v5.sh")
            bilan["amorce"] = e
            if not e or e.get("finie") is not True:
                bilan["arret"] = "amorce non finie : rien ne tourne ; consigner"
                return bilan
            # v10 : auto-arrêt vérifié sur l'instance avant la mise en place ; indisponible : pas de run
            aa, _, _ = self._cmd("auto-arret", commande_instance("auto-arret", instance=self.ident))
            bilan["auto_arret"] = aa
            if not aa or aa.get("disponible") is not True:
                bilan["arret"] = ("garde de mise en place tombée : auto-arrêt de l'instance indisponible : pas de run, "
                                  "pas de verdict ; consigner")
                return bilan
            self.chien_surveille = True  # v11 (P-1)
            self.fournisseur.envoyer_fichier(self.ident, Path(self.manifeste_local), "/root/manifeste-v3.json")
            if Path(self.manifeste_local).resolve() != (self.sortie / MANIFESTES["initial"]).resolve():
                (self.sortie / MANIFESTES["initial"]).write_bytes(Path(self.manifeste_local).read_bytes())
                scellement.sceller(self.sortie / MANIFESTES["initial"])
            clone = "/root/public"
            dep = lambda: dict(depense=self._depense())
            mep, _, _ = self._cmd("mise-en-place", commande_instance(
                "mise-en-place", travail="/root/x/mise-en-place", manifeste="/root/manifeste-v3.json",
                clone=clone, echeance_go=self.echeance, marge_transfert=self.marge_transfert_s, **dep()))
            bilan["mise_en_place"] = mep
            if not mep or "garde_tombee" in mep or "pas_par_tour" not in mep:
                bilan["arret"] = "garde de mise en place tombée : pas de run, pas de verdict ; consigner"
                return bilan
            man = {**man, "pas_par_tour": mep["pas_par_tour"], "longueur_suffixe": mep["longueur_suffixe"],
                   "ecart_10": mep["ecart_10"]}
            m_mep = self._manifeste("mise-en-place", man)
            juge, _, _ = self._cmd("controle-juge", commande_instance(
                "controle-juge", travail="/root/x/controle-juge", manifeste=m_mep, clone=clone,
                mise_en_place="/root/x/mise-en-place", echeance_go=self.echeance,
                marge_transfert=self.marge_transfert_s, **dep()))
            bilan["controle_juge"] = juge
            if not juge or "garde_tombee" in juge or juge.get("etats", {}).get("tenus") is not True:
                bilan["arret"] = "garde du juge ou contrôle du juge hors seuil : arrêt avant le pilote ; nœud"
                return bilan
            if self.relance_seule is not None:  # v18 : relance seule, sans pilote ni règle sur l'instance
                self._relance_seule(man, m_mep, bilan)
                return bilan
            pilotes = []
            for phase in ("pilote", "pilote-reprise"):
                r = self._executer(phase, m_mep)
                pilotes.append(r)
                if r.get("tours_complets") is None:  # pilote mort, gardes illisibles : ligne coupée non exclue (A-2)
                    bilan["pilote"] = pilotes
                    bilan["arret"] = ("pas de run principal ; pilote mort, état des gardes illisible (garde "
                                      "inconnue) ; nœud")
                    return bilan
                issue = issue_pilote(r)
                if issue == "finie":
                    break
                if issue == "sonde orientée":
                    bilan["pilote"] = pilotes
                    bilan["arret"] = "non interprétable (sonde orientée au pilote) ; pas de run principal"
                    return bilan
                if issue == ISSUE_LIGNE_COUPEE:  # v8 (A-2) : garde inconnue ; jamais de reprise
                    bilan["pilote"] = pilotes
                    bilan["arret"] = ("pas de run principal ; ligne de garde coupée au pilote (garde inconnue) ; "
                                      "nœud")
                    return bilan
                if issue == "arrêt":
                    bilan["pilote"] = pilotes
                    bilan["arret"] = "pilote arrêté (dépense ou échéance du GO) : pas de run principal ; nœud"
                    return bilan
            else:
                bilan["pilote"] = pilotes
                bilan["arret"] = "seconde chute du pilote : pas de run principal, pas de verdict ; nœud"
                return bilan
            bilan["pilote"] = pilotes
            fixe_t = next(p for p in pilotes if "0" in p.get("durees", {}) and "1" in p.get("durees", {}))
            regle, _, _ = self._cmd("regle", commande_instance(
                "regle-tours", travail="/root/x/regle", manifeste=m_mep, pilote=f"/root/x/{fixe_t['phase']}", **dep()))
            bilan["regle"] = regle
            if not regle or "K" not in regle:
                bilan["arret"] = "règle du nombre de tours non calculée : arrêt ; nœud"
                return bilan
            if regle["K"] < 20:  # C7 : atteignable (K et la garde au même `ETAT`)
                bilan["arret"] = "K < 20 après le pilote : arrêt, devis révisé à Lazar"
                return bilan
            man = {**man, "regle_tours": {k: regle[k] for k in ("B", "R", "D", "c", "t", "H_heures", "K")}}
            m_regle = self._manifeste("regle", man)
            principal = self._executer("principal", m_regle)
            bilan["principal"] = [principal]
            if principal.get("tours_complets") is None:
                bilan["arret"] = ("exécution principale morte sans état, tours complets illisibles : pas de relance "
                                  "(la liste l'exige sous 20 tours complets) ; nœud")
                return bilan
            if relance_permise(principal):
                d = self.poste.depense(self.horloge())
                k2 = an.nombre_de_tours(self.b, round(d, 4), self.c, regle["t"])["K"]
                if k2 < 20:
                    bilan["arret"] = "relance impossible (K < 20) : pas de verdict ; nœud"
                    return bilan
                man = {**man, "regle_tours": {**man["regle_tours"], "K": k2, "D": round(d, 4), "relance": True,
                                              "premiere_execution": man["regle_tours"]}}
                m_relance = self._manifeste("relance", man)
                bilan["principal"].append(self._executer("principal-relance", m_relance))
            return bilan
        except _Arret as arret:
            bilan["arret"] = str(arret)
            return bilan
        except Exception as err:
            bilan["erreur"] = f"{type(err).__name__}: {err}"[:300]
            raise
        finally:
            self._finir(bilan)

    def _relance_seule(self, man: dict, m_mep: str, bilan: dict) -> None:
        """v18 (addendum 5) : K recalculé par la règle sur le budget restant (même B, D du poste, c de cette instance,
        t du pilote de la première exécution) ; K < 20 : arrêt ; sinon manifeste « relance » et `principal-relance`."""
        p = self.relance_seule
        premiere = {k: p["regle_premiere"][k] for k in CLES_REGLE}
        d = round(self.poste.depense(self.horloge()), 4)
        k2 = an.nombre_de_tours(self.b, d, self.c, premiere["t"])["K"]
        bilan["relance_seule"] = {"tours_complets_premiere": int(p["tours_complets_premiere"]), "K": k2, "D": d,
                                  "c": self.c, "t": premiere["t"], "source": p.get("source")}
        self._etape({"relance_seule": bilan["relance_seule"]})
        if k2 < 20:
            bilan["arret"] = "relance impossible (K < 20) : pas de verdict ; nœud"
            return
        man = {**man, "regle_tours": {**premiere, "K": k2, "D": d, "c": self.c, "relance": True,
                                      "premiere_execution": premiere}}
        m_relance = self._manifeste("relance", man)
        bilan["principal"] = [self._executer("principal-relance", m_relance)]

    def _finir(self, bilan: dict) -> None:
        """Dans tous les cas : arrêt par PID de la commande en cours (C3), rapatriement, destruction retentée (C1) ;
        destruction en échec sans veilleur vivant → veilleur à échéance immédiate, qui la retente à chaque période.
        v11 (C-2) : après le transfert, `rapatriement-v11.json` dit si chaque étape lancée a un transfert qui fait foi ;
        sinon le statut de l'instance est relu : « stopped » ou « exited » (arrêtée par son chien) : **pas de
        destruction**, seul le stockage court, alerte « reprise requise », veilleur de secours arrêté (la reprise a le
        sien) ; en marche ou statut illisible : destruction, comme en v10.
        v12 (Q-2) : la marque `rapatrie` n'est posée que si le transfert est complet ; sinon le chien n'arrête pas le
        conteneur sur cette marque, et l'issue (arrêtée : gardée ; en marche : détruite) ne dépend plus du moment où il
        agit. v12 (V-1) : statut de `statut_vast` (état voulu compris).
        v13 (W-1, P-1) : statut « en attente de démarrage » ou « arrêt en cours » : `_arreter_puis_relire` ; arrêtée :
        gardée ; sinon détruite."""
        self._arreter_en_cours()
        self._battement()  # v10 : le chien de garde laisse la conduite vivante transférer
        for nom, cause in self.arretees.items():  # C8 : état reconstitué avant les empreintes
            if nom in EXECUTIONS and nom in self.manifestes_phase:
                bilan.setdefault("etats_reconstitues", {})[nom] = self._tours_relus(nom, cause)
        try:
            self._rapatrier(bilan)
        except Exception as err:  # consigné ; la destruction suit, sauf C-2
            bilan["rapatriement_erreur"] = f"{type(err).__name__}: {err}"[:300]
        bilan["journal_chien"] = rapatrier_journal_chien(self.fournisseur, self.ident, self.sortie)
        complet, sans_foi = self._ecrire_rapatriement(bilan)
        if not complet:  # v12 (Q-2) : sans transfert complet, pas de marque
            bilan["marque_rapatrie"] = "non posée : transfert incomplet"
        else:
            try:  # v10 : marque `rapatrie` : le chien arrête le conteneur (destruction en échec : stockage seul facturé)
                code, _ = self.fournisseur.executer(self.ident, f"mkdir -p {ETATS_DISTANTS} && touch "
                                                                f"{ETATS_DISTANTS}/{MARQUE_RAPATRIE}", 60)
                bilan["marque_rapatrie"] = code == 0
            except Exception as err:
                bilan["marque_rapatrie"] = f"{type(err).__name__}"
        if self.alerte_chien:
            bilan["alerte_chien"] = self.alerte_chien
        garder = False
        if not complet:  # v11 (C-2)
            statut = self._statut_relu()
            if statut in (STATUT_EN_ATTENTE, STATUT_ARRET_EN_COURS):  # v13 (W-1, P-1)
                statut = self._arreter_puis_relire(statut, bilan)
            bilan["statut_avant_destruction"] = statut
            garder = statut in STATUTS_ARRETES
        detruite, erreurs = False, []
        if garder:
            bilan["reprise_requise"] = sans_foi
            bilan["alerte"] = (f"instance {self.ident} arrêtée (statut « {bilan['statut_avant_destruction']} ») avant un "
                               f"transfert qui fait foi pour : {', '.join(sans_foi)} ; pas de destruction, seul le "
                               "stockage court ; reprise requise (`lanceur_v18 reprendre`) ; nœud")
            if self.pid_veilleur is not None:
                self.arreter_veilleur(self.pid_veilleur)
                bilan["veilleur_arrete"] = self.pid_veilleur
        else:
            for n in range(ESSAIS_DESTRUCTION):
                try:
                    self.fournisseur.detruire(self.ident)  # R10, par identifiant
                    detruite = True
                    break
                except Exception as err:
                    erreurs.append(f"{type(err).__name__}: {err}"[:300])
                    if n < ESSAIS_DESTRUCTION - 1:
                        self.attendre(self.periode_prete_s)
        if erreurs:
            bilan["destruction_erreur"] = erreurs[-1]
            bilan["destruction_essais_en_echec"] = len(erreurs)
        if detruite:
            if self.c is not None:
                self.poste.detruite(self.ident, self.horloge())
                self.poste.ecrire(self.poste_fichier)
            if self.pid_veilleur is not None:
                self.arreter_veilleur(self.pid_veilleur)
        elif not garder:  # C9 : toujours un veilleur à échéance 0 (destruction retentée à chaque période)
            ancien = self.pid_veilleur
            try:
                self._lancer_veilleur(echeance=0.0)
                bilan["veilleur_de_destruction"] = self.pid_veilleur
                try:
                    neuf_vivant = self._veilleur_ok()
                except Exception:
                    neuf_vivant = False
                if neuf_vivant and ancien is not None and ancien != self.pid_veilleur:
                    self.arreter_veilleur(ancien)
                elif not neuf_vivant:
                    bilan["alerte"] = ("instance non détruite ; veilleur de destruction non vu vivant (l'ancien veilleur "
                                       "est gardé) : vérifier, et arrêt manuel par identifiant (R10)")
            except Exception as err:
                self.pid_veilleur = ancien
                bilan["alerte"] = (f"instance non détruite et aucun veilleur de destruction ({type(err).__name__}) : "
                                   "arrêt manuel par identifiant (R10)")
        if self.c is None:
            bilan["taux_illisible"] = ("dépense de cette instance non comptée (taux illisible) : à relever dans "
                                       "registres/depenses.md")
        bilan["detruite"] = detruite
        bilan["depense"] = self.poste.depense(self.horloge())
        self._etape({"instance": self.ident, "detruite": detruite, "depense": bilan["depense"]})
        sortie_bilan = self.sortie / "bilan-conduite-v5.json"
        sortie_bilan.write_text(json.dumps(bilan, ensure_ascii=False, indent=2, sort_keys=True, default=str) + "\n",
                                encoding="utf-8")
        scellement.sceller(sortie_bilan)

    def _ecrire_rapatriement(self, bilan: dict) -> tuple[bool, list[str]]:
        """v11 (C-2) : chaque étape lancée a-t-elle un transfert qui fait foi ? Écrit `rapatriement-v11.json`
        (atomique), lu par le veilleur de secours ; erreur d'écriture consignée (fichier absent : rien n'est tenu
        pour transféré)."""
        transferts = bilan.get("transferts") or {}
        sans_foi = [e for e in ETAPES if e in self.lances and not (transferts.get(e) or {}).get("foi")]
        complet = "transferts" in bilan and not sans_foi
        try:  # v13 (P-3) : temporaire propre au processus, `fsync`
            _ecrire_atomique(self.sortie / FICHIER_RAPATRIEMENT,
                             json.dumps({"complet": complet, "sans_foi": sans_foi, "t": self.horloge()},
                                        ensure_ascii=False, sort_keys=True))
        except OSError as err:
            bilan["rapatriement_fichier_erreur"] = type(err).__name__
        bilan["transfert_complet"] = complet
        return complet, sans_foi

    def _arreter_puis_relire(self, statut: str, bilan: dict) -> str | None:
        """v13 (W-1, P-1) : transfert incomplet, instance « en attente de démarrage » (conteneur sorti voulu en marche,
        ou attente d'une carte) : arrêt par l'identifiant (R10), `ESSAIS_DESTRUCTION` essais ; « arrêt en cours » :
        aucun nouvel arrêt. Puis, sauf trois refus, statut relu après `periode_prete_s`. Rend le statut relu (`None`
        si illisible) ; `_finir` garde l'instance s'il est arrêté, la détruit sinon."""
        accepte, erreurs = statut == STATUT_ARRET_EN_COURS, []
        if not accepte:
            for n in range(ESSAIS_DESTRUCTION):
                try:
                    self.fournisseur.arreter(self.ident)
                    accepte = True
                    break
                except Exception as err:
                    erreurs.append(type(err).__name__)
                    if n < ESSAIS_DESTRUCTION - 1:
                        self.attendre(self.periode_prete_s)
        relu = None
        if accepte:
            self.attendre(self.periode_prete_s)
            relu = self._statut_relu()
        bilan["arret_avant_destruction"] = {"statut_lu": statut, "arret_demande": statut == STATUT_EN_ATTENTE,
                                            "acceptee": accepte, "essais_en_echec": len(erreurs), "statut_relu": relu}
        return relu

    def _statut_relu(self) -> str | None:
        """v11 (C-2) : statut de l'instance, `ESSAIS_DESTRUCTION` essais ; illisible : `None`."""
        for n in range(ESSAIS_DESTRUCTION):
            try:
                return self.fournisseur.statut(self.ident)
            except Exception:
                if n < ESSAIS_DESTRUCTION - 1:
                    self.attendre(self.periode_prete_s)
        return None

    def _creation_incertaine(self, err: Exception, sha_archive: str) -> None:
        """C11 (N-5) : `creer` a levé ; l'instance peut exister. Inventaire filtré sur la seule étiquette de cette
        conduite, destruction de ces seuls identifiants (R10) ; sinon alerte au bilan. Bilan écrit et scellé."""
        bilan = {"instance": None, "etiquette": self.etiquette, "archive_sha256": sha_archive,
                 "creation_erreur": f"{type(err).__name__}: {err}"[:300], "detruite": False, "detruites": []}
        try:
            idents = [str(i) for i in self.fournisseur.inventaire(self.etiquette)]
        except Exception as e2:
            idents = None
            bilan["inventaire_erreur"] = f"{type(e2).__name__}"
        bilan["inventaire"] = idents
        echecs = []
        for ident in idents or []:
            for n in range(ESSAIS_DESTRUCTION):
                try:
                    self.fournisseur.detruire(ident)  # R10, par identifiant, étiquette de cette conduite seulement
                    bilan["detruites"].append(ident)
                    break
                except Exception as e3:
                    if n == ESSAIS_DESTRUCTION - 1:
                        echecs.append({"id": ident, "erreur": type(e3).__name__})
                    else:
                        self.attendre(self.periode_prete_s)
        bilan["detruite"] = bool(bilan["detruites"]) and not echecs
        if echecs:
            bilan["destruction_erreur"] = echecs
        if not bilan["detruite"]:
            bilan["alerte"] = (f"création incertaine : inventaire R10 manuel (étiquette « {self.etiquette} »)")
        if bilan["detruites"]:
            bilan["taux_illisible"] = ("dépense de l'instance créée sans réponse non comptée : à relever dans "
                                       "registres/depenses.md")
        self._etape({"creation_incertaine": bilan})
        sortie_bilan = self.sortie / "bilan-conduite-v5.json"
        sortie_bilan.write_text(json.dumps(bilan, ensure_ascii=False, indent=2, sort_keys=True, default=str) + "\n",
                                encoding="utf-8")
        scellement.sceller(sortie_bilan)

    def _battement(self) -> None:
        """v10 : battement de la conduite sur l'instance (en plus de chaque sondage) ; erreur ignorée."""
        try:
            self.fournisseur.executer(self.ident, f"mkdir -p {ETATS_DISTANTS} && touch "
                                                  f"{ETATS_DISTANTS}/{BATTEMENT_CONDUITE}", 60)
        except Exception:
            pass

    def _rapatrier(self, bilan: dict) -> None:
        """Avant destruction : empreintes sur l'instance, transfert des journaux et des fichiers d'état de chaque
        étape lancée, comparaison, second transfert au plus, scellement après égalité (corrections 7 et 11). v10 :
        corps dans `rapatrier_etapes` (partagé avec `Reprise`), battement avant chaque étape."""
        bilan["transferts"] = rapatrier_etapes(self.fournisseur, self.ident, self.sortie,
                                               [e for e in ETAPES if e in self.lances], battre=self._battement)


def rapatrier_etapes(fournisseur: Fournisseur, ident: str, racine: Path, etapes: list[str], si_absent: bool = False,
                     battre=None) -> dict:
    """Corps de `Conduite._rapatrier` (v9), inchangé, plus : `si_absent` (reprise : empreintes prises sur l'instance
    avant son arrêt gardées, `empreintes --si-absent`) et `battre` (appelé avant chaque étape)."""
    transferts = {}
    for etape in etapes:
        if battre is not None:
            battre()
        distant = f"/root/x/{etape}"
        local = Path(racine) / etape
        res = {"erreurs": []}
        transferts[etape] = res
        try:
            opts = {"travail": distant, **({"si_absent": True} if si_absent else {})}
            _c, sortie = fournisseur.executer(ident, commande_instance("empreintes", **opts), 600)
            lire_etat(sortie)
            fournisseur.rapatrier_fichier(ident, f"{distant}/{cv.EMPREINTES_INSTANCE}", local / cv.EMPREINTES_INSTANCE)
            emp = json.loads((local / cv.EMPREINTES_INSTANCE).read_text(encoding="utf-8"))
        except Exception as err:  # étape sans empreintes : consignée, les autres continuent
            res["erreurs"].append({"etape": "empreintes", "erreur": f"{type(err).__name__}: {err}"[:200]})
            continue
        essais = transferer(fournisseur, ident, distant, local, emp, res["erreurs"])
        res.update({"empreintes_instance": emp, "essais": essais, "foi": None})
        for n, obtenues in enumerate(essais, start=1):
            if obtenues == emp:
                res["foi"] = f"transfert-{n}"
                scellement.sceller(local / cv.EMPREINTES_INSTANCE)
                for rel in emp:
                    scellement.sceller(local / f"transfert-{n}" / rel)
                break
    return transferts


def rapatrier_journal_chien(fournisseur: Fournisseur, ident: str, racine: Path) -> str:
    """v10 : journal du chien de garde (causes, arrêts par PID, appels à l'API ; aucune note, aucune clé), transféré
    et scellé hors des étapes ; erreur consignée, jamais levée."""
    local = Path(racine) / JOURNAL_CHIEN
    if local.exists():
        return "déjà présent localement (R12) : non transféré"
    try:
        fournisseur.rapatrier_fichier(ident, f"{ETATS_DISTANTS}/{JOURNAL_CHIEN}", local)
        scellement.sceller(local)
        return "transféré"
    except Exception as err:
        return f"non transféré ({type(err).__name__})"


# --- v10 : reprise après une coupure du poste local -------------------------------------------------------------------

MANIFESTE_PHASE = {"pilote": "mise-en-place", "pilote-reprise": "mise-en-place", "principal": "regle",
                   "principal-relance": "relance"}


@dataclass
class Reprise:
    """Reprise d'un poste dont la conduite s'est éteinte (nouvelle session) : inventaire par l'étiquette, transfert,
    comparaison, scellement, destruction par l'identifiant (R10). Aucune reprise du calcul. Voir la docstring du
    module. `sortie` : dossier de la conduite interrompue (son journal `conduite-v5.jsonl`, ses manifestes) ; le
    résultat va dans `<sortie>/reprise-v10/` (ou `reprise-v10-<n>` pour une reprise de plus, jamais d'écrasement) :
    transferts par étape, manifestes copiés, journal du chien,
    `bilan-reprise-v10.json` scellé (redémarrage et sa durée, pour `registres/depenses.md`).
    v11 : B-3 (liste attendue des étapes, code de `ls` exigé), C-1 (veilleur local d'arrêt avant le redémarrage ;
    remise à l'arrêt en plusieurs essais ; alerte exacte), P-7 (statut relu après la remise à l'arrêt).
    v12 : V-1 (remise à l'arrêt confirmée seulement par un arrêt accepté et un statut arrêté ; instance en attente de
    démarrage remise à l'arrêt), V-2 (branche « en marche » bornée par le budget, veilleur d'arrêt avant le battement),
    V-5 (`ecart_secours_s` retranché de la borne de budget et de l'échéance), Q-1 (destruction écrite au poste).
    v13 : P-2 (veilleurs d'arrêt des reprises précédentes arrêtés par leur PID avant redémarrage ou transfert ; alerte
    exacte de la remise à l'arrêt), P-4 (statut autre : veilleur d'arrêt borné par le budget et l'échéance laissé).
    `lancer_veilleur_arret`, `veilleur_arret_vivant`, `arreter_veilleur` : substituts pour l'épreuve ; défaut :
    `lancer_veilleur_arret_processus`, `verifier_veilleur`, `arreter_veilleur` de ce module ; `fournisseur_veilleur` :
    défaut « vast » pour `FournisseurVast`, sinon aucun (pas de redémarrage sans veilleur)."""
    fournisseur: Fournisseur
    sortie: Path
    etiquette: str
    echeance: float
    horloge: object = time.time
    attendre: object = time.sleep
    delai_prete_s: float = DELAI_PRETE_S
    periode_prete_s: float = 15.0
    minuterie_s: float = MINUTERIE_REPRISE_S
    arreter_en_cours: bool = False
    lancer_veilleur_arret: object = None
    veilleur_arret_vivant: object = None
    arreter_veilleur: object = None
    fournisseur_veilleur: str | None = None
    periode_veilleur_s: float = 30.0
    marge_secours: float = MARGE_SECOURS_USD  # v11 (P-2)
    duree_transfert_min_s: float = DUREE_TRANSFERT_MIN_S
    ecart_secours_s: float = ECART_SECOURS_S  # v12 (V-5)
    identite_veilleur: object = None  # v13 (P-2) : substitut pour l'épreuve ; défaut `identite_veilleur_arret`

    def _borne_budget(self, ident: str, bilan: dict) -> float | None:
        """v11 (P-2) : instant où D (poste de la conduite, toutes instances, intervalles arrêtés compris) atteindrait
        B − marge de secours au taux le plus haut du taux relevé à la création et du taux lu maintenant ; `None` si le
        poste est illisible ou ne porte pas cette instance (pas de redémarrage). v12 (V-5) : la borne rendue est avancée
        de `ecart_secours_s` (le veilleur de secours de la conduite, s'il vit, a le même seuil B − marge)."""
        try:
            poste = Poste.lire(Path(self.sortie) / "poste-v5.json")
            (inst_,) = [i for i in poste.instances if str(i["id"]) == str(ident)]
            c = float(inst_["c"])
        except Exception as err:
            bilan["budget"] = {"erreur": type(err).__name__}
            return None
        try:
            c = max(c, float(self.fournisseur.taux_horaire(ident)))
        except Exception:
            pass
        maintenant = self.horloge()
        d = poste.depense(maintenant)
        seuil = maintenant + (poste.b - self.marge_secours - d) / c * 3600 if c > 0 else float("inf")
        borne = seuil - float(self.ecart_secours_s)  # v12 (V-5)
        bilan["budget"] = {"B": poste.b, "D": round(d, 4), "taux": c, "seuil_secours": seuil,
                           "ecart_secours_s": float(self.ecart_secours_s), "borne_budget": borne,
                           "reste_s": borne - maintenant}
        return borne

    def _ident_journal(self) -> str | None:
        """Identifiant noté à la création par la conduite (`{"instance": …, "creee": …}`), s'il est lisible."""
        try:
            for ligne in (Path(self.sortie) / "conduite-v5.jsonl").read_text(encoding="utf-8").splitlines():
                try:
                    o = json.loads(ligne)
                except ValueError:
                    continue
                if "creee" in o and o.get("instance") is not None:
                    return str(o["instance"])
        except OSError:
            pass
        return None

    def _etapes_journal(self) -> list[str] | None:
        """v11 (B-3) : étapes lancées selon le journal de la conduite (toute ligne `{"commande": <étape>, …}` : la
        conduite note chaque lancement, `"lancee": true`, avant de lancer) ; journal illisible : `None`. Une ligne
        illisible (dernière ligne coupée) est ignorée."""
        try:
            texte = (Path(self.sortie) / "conduite-v5.jsonl").read_text(encoding="utf-8")
        except OSError:
            return None
        vues = set()
        for ligne in texte.splitlines():
            try:
                o = json.loads(ligne)
            except ValueError:
                continue
            if isinstance(o, dict) and o.get("commande") in ETAPES:
                vues.add(o["commande"])
        return [e for e in ETAPES if e in vues]

    def _echeance_reprise(self) -> float:
        """v12 (V-5) : échéance du GO avancée de `ecart_secours_s` (le veilleur de secours détruit à l'échéance)."""
        return float(self.echeance) - float(self.ecart_secours_s)

    def _prete(self, ident: str) -> bool:
        debut = self.horloge()
        while True:
            try:
                if self.fournisseur.statut(ident) == "running" and self.fournisseur.executer(ident, "true", 60)[0] == 0:
                    return True
            except Exception:
                pass
            if self.horloge() - debut >= self.delai_prete_s or self.horloge() >= self._echeance_reprise() \
                    or self.horloge() >= getattr(self, "borne_budget", float("inf")):
                return False
            self.attendre(self.periode_prete_s)

    # --- v11 (C-1) : veilleur local d'arrêt ---
    def _spec_veilleur(self) -> str | None:
        if self.fournisseur_veilleur is not None:
            return self.fournisseur_veilleur
        return "vast" if isinstance(self.fournisseur, FournisseurVast) else None

    def _veilleur(self, ident: str, echeance: float, racine: Path, n: int) -> int | None:
        """Lance un veilleur d'arrêt et le vérifie vivant (battement) ; rend son PID, ou `None` (noté au bilan)."""
        journal = racine / ("veilleur-arret-v11.jsonl" if n == 1 else f"veilleur-arret-v11-{n}.jsonl")
        lancer = self.lancer_veilleur_arret or lancer_veilleur_arret_processus
        vivant = self.veilleur_arret_vivant or (lambda pid, j: verifier_veilleur(
            pid, j, fraicheur_s=max(180.0, 4 * float(self.periode_veilleur_s))))
        try:
            pid = lancer(ident, self.etiquette, echeance, journal, self._spec_veilleur(), self.periode_veilleur_s)
        except Exception as err:
            self.bilan.setdefault("veilleurs_arret", []).append({"lance": False, "erreur": type(err).__name__,
                                                                 "echeance": echeance})
            return None
        ok = bool(vivant(pid, journal))
        self.bilan.setdefault("veilleurs_arret", []).append({"pid": pid, "vivant": ok, "echeance": echeance,
                                                             "journal": journal.name})
        if not ok:
            (self.arreter_veilleur or arreter_veilleur)(pid)
            return None
        self.veilleurs_vivants.append(pid)
        return pid

    def _arreter_veilleurs(self) -> None:
        """R10 : par PID (objet `Popen` pour un veilleur lancé ici)."""
        for pid in self.veilleurs_vivants:
            try:
                (self.arreter_veilleur or arreter_veilleur)(pid)
            except Exception:
                pass
        self.bilan["veilleurs_arret_arretes"] = list(self.veilleurs_vivants)
        self.veilleurs_vivants = []

    def _veilleurs_precedents(self, racine: Path) -> list[tuple[int, str]]:
        """v13 (P-2) : (PID, journal) des veilleurs d'arrêt lancés par les reprises précédentes de ce dossier : ceux
        que nomment leurs bilans (`veilleurs_arret`), et ceux dont un battement porte le PID (bilan absent, reprise
        coupée)."""
        vus: dict[tuple[int, str], None] = {}
        for d in sorted(Path(self.sortie).glob("reprise-v10*")):
            if d == racine or not d.is_dir():
                continue
            try:
                b = json.loads((d / "bilan-reprise-v10.json").read_text(encoding="utf-8"))
                for e in b.get("veilleurs_arret") or []:
                    if isinstance(e, dict) and e.get("pid") is not None and e.get("journal"):
                        vus[(int(e["pid"]), str(d / str(e["journal"])))] = None
            except Exception:
                pass
            for bat in sorted(d.glob("veilleur-arret-v11*.jsonl.battement")):
                try:
                    vus[(int(json.loads(bat.read_text(encoding="utf-8"))["pid"]),
                         str(bat)[:-len(".battement")])] = None
                except Exception:
                    pass
        return list(vus)

    def _arreter_veilleurs_precedents(self, racine: Path) -> bool:
        """v13 (P-2) : avant tout redémarrage ou transfert, arrête par son PID (R10) chaque veilleur d'arrêt d'une
        reprise précédente dont l'identité est vérifiée (`identite_veilleur_arret`) : sinon, sa borne passée, il
        arrêterait l'instance redémarrée. Un PID fini ou réemployé n'est jamais signalé. Rend faux (alerte exacte au
        bilan) si l'un d'eux vit encore après le signal ou a une identité illisible."""
        identite = self.identite_veilleur or identite_veilleur_arret
        arreter = self.arreter_veilleur or arreter_veilleur
        rapport, restants = [], []
        for pid, journal in self._veilleurs_precedents(racine):
            qui = identite(pid, journal)
            if qui is False:
                rapport.append({"pid": pid, "journal": journal, "issue": "fini, ou PID d'un autre processus : non signalé"})
                continue
            if qui is None:
                rapport.append({"pid": pid, "journal": journal, "issue": "identité illisible : non signalé"})
                restants.append(pid)
                continue
            try:
                arreter(pid)
            except Exception as err:
                rapport.append({"pid": pid, "journal": journal, "erreur": type(err).__name__})
            for _ in range(50):  # au plus 5 s
                if identite(pid, journal) is not True:
                    break
                time.sleep(0.1)
            if identite(pid, journal) is True:
                rapport.append({"pid": pid, "journal": journal, "issue": "encore vivant après SIGTERM"})
                restants.append(pid)
            else:
                rapport.append({"pid": pid, "journal": journal, "issue": "arrêté par son PID (R10)"})
        self.bilan["veilleurs_precedents"] = rapport
        if restants:
            self.bilan.setdefault("alertes", []).append(
                f"veilleur d'arrêt d'une reprise précédente non arrêté (PID {', '.join(str(p) for p in restants)} : "
                "encore vivant après SIGTERM, ou identité illisible) : il arrêterait l'instance redémarrée ; à arrêter "
                "par son PID (R10) après vérification, puis relancer `reprendre` ; nœud")
            return False
        return True

    def _remettre_a_l_arret(self, ident: str, bilan: dict, racine: Path) -> None:
        """v11 (C-1, P-7) : `ESSAIS_DESTRUCTION` essais d'arrêt (la ligne « stopping instance … » fait foi de
        l'acceptation), puis statut relu. Confirmé (« stopped » ou « exited ») : veilleurs d'arrêt arrêtés. Sinon :
        un veilleur d'arrêt à échéance immédiate est lancé (il retente à chaque période), et l'alerte dit exactement ce
        qui arrête l'instance : la minuterie, si elle a été posée sur l'instance ; le veilleur local, s'il vit ;
        sinon l'arrêt manuel par identifiant (R10). v12 (V-1) : confirmé seulement si un arrêt a été **accepté** et que
        le statut relu (`statut_vast`, état voulu compris) est arrêté ; un « stopped » relu après trois refus ne
        confirme rien (redémarrage peut-être en attente d'une carte)."""
        accepte, erreurs = False, []
        for n in range(ESSAIS_DESTRUCTION):
            try:
                self.fournisseur.arreter(ident)
                accepte = True
                break
            except Exception as err:
                erreurs.append(type(err).__name__)
                if n < ESSAIS_DESTRUCTION - 1:
                    self.attendre(self.periode_prete_s)
        if accepte:
            self.attendre(self.periode_prete_s)  # l'arrêt accepté prend quelques secondes
        try:
            statut = self.fournisseur.statut(ident)
        except Exception as err:
            statut = f"illisible ({type(err).__name__})"
        bilan["remise_a_l_arret"] = {"acceptee": accepte, "essais_en_echec": len(erreurs), "statut_relu": statut}
        if accepte and statut in STATUTS_ARRETES:  # v12 (V-1)
            self._arreter_veilleurs()
            return
        pid = self._veilleur(ident, self.horloge(), racine, len(bilan.get("veilleurs_arret", [])) + 1)
        if accepte:
            tete = f"arrêt accepté, statut relu « {statut} »"
        elif statut in STATUTS_ARRETES:  # v13 (P-2) : alerte exacte (l'API refuse l'arrêt d'une instance arrêtée)
            tete = (f"arrêt refusé {len(erreurs)} fois, statut relu « {statut} » (état voulu compris) : instance "
                    "vraisemblablement déjà arrêtée, arrêt non confirmé par un arrêt accepté")
        else:
            tete = f"instance non remise à l'arrêt après {len(erreurs)} essais (statut relu « {statut} »)"
        if self.minuterie_posee is not None:
            minuterie = (f"la minuterie posée sur l'instance l'arrête au plus tard à {self.minuterie_posee:.0f} "
                         "(horloge de l'instance)")
        else:
            minuterie = "aucune minuterie n'a été posée sur l'instance"
        vivants = [p for p in self.veilleurs_vivants]
        if vivants:
            veilleur = (f"le veilleur local d'arrêt (PID {', '.join(str(p) for p in vivants)}) retente l'arrêt par "
                        "identifiant à chaque période jusqu'au statut « stopped »")
        else:
            veilleur = "aucun veilleur local d'arrêt ne vit : arrêt manuel par identifiant (R10)"
        bilan.setdefault("alertes", []).append(f"{tete} : {minuterie} ; {veilleur}")
        bilan["veilleur_arret_immediat"] = pid

    def reprendre(self) -> dict:
        racine, n = Path(self.sortie) / "reprise-v10", 1
        while racine.exists():  # R12 : une reprise de plus prend un nouveau nom, rien n'est écrasé
            n += 1
            racine = Path(self.sortie) / f"reprise-v10-{n}"
        racine.mkdir(parents=True)
        bilan: dict = {"etiquette": self.etiquette, "detruite": False, "debut": self.horloge()}
        self.bilan, self.veilleurs_vivants, self.minuterie_posee = bilan, [], None
        self.borne_budget = float("inf")
        try:
            self._reprendre(racine, bilan)
        except Exception as err:
            bilan["erreur"] = f"{type(err).__name__}: {err}"[:300]
            raise
        finally:
            bilan["fin"] = self.horloge()
            if "redemarrage" in bilan:
                bilan["redemarrage"]["fin"] = bilan["fin"]
                bilan["redemarrage"]["duree_s"] = bilan["fin"] - bilan["redemarrage"]["debut"]
            bilan["veilleurs_arret_vivants"] = list(self.veilleurs_vivants)
            f = racine / "bilan-reprise-v10.json"
            f.write_text(json.dumps(bilan, ensure_ascii=False, indent=2, sort_keys=True, default=str) + "\n",
                         encoding="utf-8")
            scellement.sceller(f)
        return bilan

    def _reprendre(self, racine: Path, bilan: dict) -> None:
        alerte = lambda m: bilan.setdefault("alertes", []).append(m)
        remettre = lambda: self._remettre_a_l_arret(ident, bilan, racine)
        try:
            idents = [str(i) for i in self.fournisseur.inventaire(self.etiquette)]
        except Exception as err:
            alerte(f"inventaire illisible ({type(err).__name__}) : inventaire R10 manuel ; rien n'est fait")
            return
        bilan["inventaire"] = idents
        if not idents:
            bilan["issue"] = "aucune instance de cette étiquette (déjà détruite ?) : rien n'est fait"
            return
        if len(idents) > 1:
            alerte("plusieurs instances portent l'étiquette : rien n'est fait ; inventaire R10 manuel")
            return
        ident = idents[0]
        bilan["instance"] = ident
        connu = self._ident_journal()
        if connu is not None and connu != ident:
            alerte(f"l'instance de l'étiquette ({ident}) n'est pas celle du journal de la conduite ({connu}) : rien "
                   "n'est fait ; nœud")
            return
        lancees = self._etapes_journal()  # v11 (B-3)
        if lancees is None:
            alerte("journal de la conduite (conduite-v5.jsonl) illisible : étapes lancées inconnues ; rien n'est fait ; "
                   "nœud")
            return
        bilan["etapes_lancees_journal"] = lancees
        statut = self.fournisseur.statut(ident)
        bilan["statut"] = statut
        echeance = self._echeance_reprise()  # v12 (V-5) : échéance avancée de l'écart du veilleur de secours
        bilan["echeance_reprise"] = echeance
        if statut in STATUTS_ARRETES:
            if self.horloge() >= echeance:
                alerte("échéance du GO passée (moins l'écart du veilleur de secours) : redémarrage refusé (aucune "
                       "dépense après l'échéance) ; instance gardée arrêtée, stockage facturé ; nœud")
                return
            # v11 (P-2) : plafond B dur : jamais de redémarrage qui porterait D au-delà de B
            borne_budget = self._borne_budget(ident, bilan)
            if borne_budget is None:
                alerte("poste de la conduite (poste-v5.json) illisible ou sans cette instance : dépense inconnue ; "
                       "pas de redémarrage ; instance laissée arrêtée ; nœud")
                return
            if borne_budget - self.horloge() < self.duree_transfert_min_s:
                alerte("reprise impossible dans le budget : D atteindrait B − "
                       f"{self.marge_secours:g} USD (moins l'écart du veilleur de secours) avant "
                       f"{self.duree_transfert_min_s:.0f} s de redémarrage ; pas de redémarrage ; instance laissée "
                       "arrêtée, stockage facturé ; nœud")
                return
            self.borne_budget = borne_budget
            # v11 (C-1) : veilleur local d'arrêt lancé et vu vivant avant tout redémarrage
            borne = min(self.horloge() + self.delai_prete_s + DELAI_COMMANDE_S + self.minuterie_s, echeance,
                        borne_budget)
            if self._veilleur(ident, borne, racine, 1) is None:
                alerte("veilleur local d'arrêt non lancé ou non vu vivant : pas de redémarrage (aucune dépense) ; "
                       "instance gardée arrêtée, stockage facturé ; nœud")
                return
            if not self._arreter_veilleurs_precedents(racine):  # v13 (P-2)
                alerte("pas de redémarrage (aucune dépense) ; instance gardée arrêtée, stockage facturé ; nœud")
                self._arreter_veilleurs()
                return
            bilan["redemarrage"] = {"debut": self.horloge(), "borne_veilleur": borne}
            try:
                self.fournisseur.demarrer(ident)
            except Exception as err:
                alerte(f"redémarrage refusé ({type(err).__name__}) : instance gardée arrêtée ; nœud")
                remettre()
                return
            if not self._prete(ident):
                alerte("instance non prête après le redémarrage (carte reprise ?) : instance remise à l'arrêt, journaux "
                       "sur son disque ; nœud")
                remettre()
                return
            d = ETATS_DISTANTS  # une ancienne `.fin` ferait croire à une minuterie lancée (idempotence) : effacée
            pose = self.horloge()
            # v11 (P-2) : minuterie bornée par le budget (lancement compris) ; trop courte : pas de transfert
            minuterie = min(float(self.minuterie_s), borne_budget - pose - DELAI_COMMANDE_S)
            if minuterie <= 0:
                alerte("reprise impossible dans le budget : D atteint B − "
                       f"{self.marge_secours:g} USD avant la pose de la minuterie ; instance remise à l'arrêt ; nœud")
                remettre()
                return
            code, sortie = self.fournisseur.executer(ident, f"rm -f {d}/{MINUTERIE}.fin {d}/{MINUTERIE}.pid "
                                                            f"{d}/{MINUTERIE}.debut; " + commande_detachee(
                MINUTERIE, commande_instance(CHIEN, racine="/root", minuterie=repr(minuterie),
                                             echeance_go=repr(float(echeance)))), DELAI_COMMANDE_S)
            if code != 0 or not lancement_verifie(sortie):
                alerte("minuterie de l'instance non lancée : pas de transfert sans elle ; instance remise à l'arrêt ; "
                       "nœud")
                remettre()
                return
            self.minuterie_posee = min(pose + DELAI_COMMANDE_S + minuterie, echeance)
            bilan["minuterie_s"] = minuterie
        elif statut == "running":
            # v12 (V-2) : même borne de budget que pour une instance arrêtée, calculée avant tout `executer`
            if self.horloge() >= echeance:
                alerte("échéance du GO passée (moins l'écart du veilleur de secours) : pas de transfert ; instance en "
                       "marche remise à l'arrêt sans transfert, journaux sur son disque ; nœud")
                remettre()
                return
            borne_budget = self._borne_budget(ident, bilan)
            if borne_budget is None:
                alerte("poste de la conduite (poste-v5.json) illisible ou sans cette instance : dépense inconnue ; "
                       "pas de transfert ; instance en marche remise à l'arrêt sans transfert ; nœud")
                remettre()
                return
            if borne_budget - self.horloge() < self.duree_transfert_min_s:
                alerte("reprise impossible dans le budget : D atteindrait B − "
                       f"{self.marge_secours:g} USD (moins l'écart du veilleur de secours) avant "
                       f"{self.duree_transfert_min_s:.0f} s de transfert ; instance en marche remise à l'arrêt sans "
                       "transfert, journaux sur son disque ; nœud")
                remettre()
                return
            self.borne_budget = borne_budget
            borne_seule = min(echeance, borne_budget)  # budget et échéance seuls : ne coupe pas un run sous B
            try:  # lecture seule : le battement n'est pas touché ici
                en_cours = list(lire_etat(self.fournisseur.executer(ident, commande_instance("en-cours"), 120)[1])
                                ["en_cours"])
            except Exception as err:
                pid = self._veilleur(ident, borne_seule, racine, 1)
                alerte(f"instance en marche mais illisible ({type(err).__name__}) : rien n'est fait ; elle "
                       "s'arrêtera seule ; " + (f"veilleur local d'arrêt (PID {pid}) laissé, borné par le budget et "
                                                "l'échéance" if pid is not None else
                                                "aucun veilleur local d'arrêt lancé ; nœud"))
                return
            bilan["en_cours"] = en_cours
            if en_cours and not self.arreter_en_cours:
                pid = self._veilleur(ident, borne_seule, racine, 1)
                bilan["issue"] = ("commande en cours sur l'instance : rien n'est fait ; l'instance s'arrêtera seule ; "
                                  "relancer `reprendre` ensuite")
                bilan["veilleur_budget"] = {"pid": pid, "echeance": borne_seule}
                if pid is None:
                    alerte("commande en cours : aucun veilleur local d'arrêt lancé (borne de budget non posée) ; nœud")
                return
            borne = min(self.horloge() + DELAI_COMMANDE_S + self.minuterie_s, echeance, borne_budget)
            if self._veilleur(ident, borne, racine, 1) is None:  # avant de toucher le battement
                alerte("veilleur local d'arrêt non lancé ou non vu vivant : pas de transfert ; instance en marche remise "
                       "à l'arrêt sans transfert, journaux sur son disque ; nœud")
                remettre()
                return
            if not self._arreter_veilleurs_precedents(racine):  # v13 (P-2)
                alerte("pas de transfert ; instance en marche remise à l'arrêt sans transfert, journaux sur son disque ; "
                       "nœud")
                remettre()
                return
            bilan["transfert_en_marche"] = {"debut": self.horloge(), "borne_veilleur": borne}
            try:  # le chien de garde laisse transférer une conduite vivante
                self.fournisseur.executer(ident, f"mkdir -p {ETATS_DISTANTS} && touch "
                                                 f"{ETATS_DISTANTS}/{BATTEMENT_CONDUITE}", 60)
            except Exception:
                pass
            for nom in en_cours:  # R10 : par PID ; état reconstitué « arrêt par la conduite »
                self.fournisseur.executer(ident, commande_arret(nom), 120)
                if nom in MANIFESTE_PHASE:
                    self.fournisseur.executer(ident, commande_instance(
                        "tours", travail=f"/root/x/{nom}", ecrire_etat=True, phase=nom,
                        manifeste=f"/root/{MANIFESTES[MANIFESTE_PHASE[nom]]}", cause="arrêt par la conduite"), 600)
        elif statut == STATUT_EN_ATTENTE:  # v12 (V-1) : redémarrage en attente d'une carte : arrêt (annule l'attente)
            alerte("instance en attente de démarrage (état voulu « running », état réel arrêté) : remise à l'arrêt, "
                   "aucun transfert ; relancer `reprendre` ensuite ; nœud")
            remettre()
            return
        else:  # v13 (P-4) : rien n'est fait, mais un veilleur d'arrêt borné par le budget et l'échéance est laissé
            borne_budget = self._borne_budget(ident, bilan)
            borne_seule = min(echeance, self.horloge() if borne_budget is None else borne_budget)
            pid = self._veilleur(ident, borne_seule, racine, 1)
            bilan["veilleur_budget"] = {"pid": pid, "echeance": borne_seule}
            alerte(f"statut « {statut} » : rien n'est fait ; " + (
                f"veilleur local d'arrêt (PID {pid}) laissé, borné par le budget et l'échéance"
                + (" (poste illisible : borne immédiate)" if borne_budget is None else "")
                if pid is not None else "aucun veilleur local d'arrêt lancé") + " ; relancer `reprendre` plus tard, ou "
                  "nœud")
            return
        try:
            code, sortie = self.fournisseur.executer(ident, "ls -1 /root/x 2>/dev/null", 120)
        except Exception as err:
            code, sortie = f"{type(err).__name__}", ""
        bilan["ls_code"] = code
        if code != 0:  # v11 (B-3) : liste illisible : jamais de destruction sans transfert
            alerte(f"liste des étapes de l'instance illisible (code {code}) : pas de transfert, pas de destruction ; "
                   "instance remise à l'arrêt, journaux sur son disque ; nœud")
            remettre()
            return
        presentes = [e for e in ETAPES if e in sortie.split()]
        etapes = [e for e in ETAPES if e in presentes or e in lancees]
        bilan["etapes_presentes"] = presentes
        bilan["etapes"] = etapes
        for nom in MANIFESTES.values():  # la lecture s'applique au dossier de la reprise
            for suffixe in ("", ".sha256"):
                src = Path(self.sortie) / (nom + suffixe)
                if src.is_file():
                    (racine / (nom + suffixe)).write_bytes(src.read_bytes())
        bilan["transferts"] = rapatrier_etapes(self.fournisseur, ident, racine, etapes, si_absent=True)
        bilan["journal_chien"] = rapatrier_journal_chien(self.fournisseur, ident, racine)
        sans_foi = [e for e in etapes if not (bilan["transferts"].get(e) or {}).get("foi")]
        complet = not sans_foi
        bilan["transfert_complet"] = complet
        if not complet:
            bilan["etapes_sans_foi"] = sans_foi
            alerte("transfert sans égalité d'empreintes pour au moins une étape : pas de destruction ; instance remise "
                   "à l'arrêt, journaux sur son disque ; nœud")
            remettre()
            return
        erreurs = []
        for n in range(ESSAIS_DESTRUCTION):
            try:
                self.fournisseur.detruire(ident)  # R10, par identifiant, seule instance de l'étiquette
                bilan["detruite"] = True
                bilan["destruction"] = self.horloge()
                break
            except Exception as err:
                erreurs.append(f"{type(err).__name__}: {err}"[:200])
                if n < ESSAIS_DESTRUCTION - 1:
                    self.attendre(self.periode_prete_s)
        if erreurs:
            bilan["destruction_erreurs"] = erreurs
        if bilan["detruite"]:
            self._ecrire_destruction_poste(ident, bilan)  # v12 (Q-1)
            self._arreter_veilleurs()
        else:
            alerte("destruction en échec : instance remise à l'arrêt ; destruction manuelle par identifiant (R10)")
            remettre()

    def _ecrire_destruction_poste(self, ident: str, bilan: dict) -> None:
        """v12 (Q-1) : la destruction est écrite dans `poste-v5.json` (atomique, `Poste.ecrire`) : D ne compte plus
        l'instance au-delà, et un veilleur de secours encore vivant finit sur « déjà détruite ». Erreur : notée, alerte
        (D reste compté jusqu'à maintenant : prudent ; à corriger à la main dans `registres/depenses.md`)."""
        try:
            f = Path(self.sortie) / "poste-v5.json"
            poste = Poste.lire(f)
            poste.detruite(str(ident), float(bilan["destruction"]))
            poste.ecrire(f)
            bilan["poste_mis_a_jour"] = True
        except Exception as err:
            bilan["poste_mis_a_jour"] = f"non ({type(err).__name__})"
            bilan.setdefault("alertes", []).append(
                f"destruction non écrite dans poste-v5.json ({type(err).__name__}) : D compte l'instance jusqu'à "
                "maintenant ; un veilleur de secours encore vivant retentera la destruction : l'arrêter par son PID "
                "(R10)")


# --- point d'entrée du veilleur ---------------------------------------------------------------------------------------


# --- v18 : relance seule et assemblage pour la lecture (addendum 5) ---------------------------------------------------

CLES_REGLE = ("B", "R", "D", "c", "t", "H_heures", "K")


def verifier_relance_seule(p: dict) -> None:
    """Gardes d'entrée de la relance seule, avant toute création d'instance (aucune dépense si l'une tombe)."""
    if not isinstance(p, dict) or "tours_complets_premiere" not in p or "regle_premiere" not in p:
        raise GardeArret("relance seule : tours complets de la première exécution et règle requis")
    k1 = p["tours_complets_premiere"]
    if isinstance(k1, bool) or not isinstance(k1, int) or not 0 <= k1 < 20:
        raise GardeArret("relance seule : la liste d'arrêt ne permet la relance que sous 20 tours complets mesurés")
    r = p["regle_premiere"]
    if not isinstance(r, dict) or any(k not in r for k in CLES_REGLE):
        raise GardeArret("relance seule : règle de la première exécution incomplète")
    t = r["t"]
    if isinstance(t, bool) or not isinstance(t, (int, float)) or not t > 0 or not math.isfinite(float(t)):
        raise GardeArret("relance seule : t du pilote non strictement positif")


def _fichiers_scelles(d: Path) -> list[Path]:
    return sorted(p for p in d.rglob("*") if p.is_file() and not p.name.endswith(".sha256")
                  and Path(f"{p}.sha256").is_file())


def assembler_lecture(premiere: Path, relance: Path, cible: Path) -> dict:
    """v18 (addendum 5) : dossier de lecture unique (première conduite + relance seule). `premiere` : dossier des
    transferts de la première conduite (sortie de la conduite, ou dossier de reprise) ; `relance` : sortie de la
    conduite de relance seule ; `cible` : dossier neuf. Ne lit aucune note ; vérifie toutes les empreintes copiées."""
    from . import lecture_v8 as lc
    premiere, relance, cible = Path(premiere), Path(relance), Path(cible)
    if cible.exists():
        raise GardeArret("assemblage : dossier cible déjà présent (R12)")
    for e in ("mise-en-place", "controle-juge", "regle", "principal"):
        if not (premiere / e).is_dir():
            raise GardeArret(f"assemblage : étape « {e} » absente de la première conduite")
    if not any((premiere / e).is_dir() for e in ("pilote", "pilote-reprise")):
        raise GardeArret("assemblage : aucun pilote dans la première conduite")
    if (premiere / "principal-relance").exists() or (premiere / lc.MANIFESTES["relance"]).exists():
        raise GardeArret("assemblage : la première conduite porte déjà une relance")
    for nom in ("initial", "mise-en-place", "regle"):
        if not (premiere / lc.MANIFESTES[nom]).is_file():
            raise GardeArret(f"assemblage : manifeste « {nom} » absent de la première conduite")
    for e in ("principal-relance", "mise-en-place", "controle-juge"):
        if not (relance / e).is_dir():
            raise GardeArret(f"assemblage : étape « {e} » absente de la conduite de relance")
    for e in ("pilote", "pilote-reprise", "regle", "principal"):
        if (relance / e).exists():
            raise GardeArret(f"assemblage : la conduite de relance porte une étape « {e} »")
    if not (relance / lc.MANIFESTES["relance"]).is_file():
        raise GardeArret("assemblage : manifeste « relance » absent")
    mep = lc._etat_etape(relance, "mise-en-place", cv.ETAT_MISE_EN_PLACE)
    if (mep is None or set(mep.get("gardes", {})) != set(cv.GARDES_MISE_EN_PLACE)
            or any(v != "passée" for v in mep["gardes"].values())):
        raise GardeArret("assemblage : mise en place de la relance non conforme ou garde tombée")
    cj = lc._etat_etape(relance, "controle-juge", cv.ETAT_CONTROLE_JUGE)
    if cj is None or cj.get("garde_juge") != "passée" or cj.get("etats", {}).get("tenus") is not True:
        raise GardeArret("assemblage : contrôle du juge de la relance non tenu")
    m_rel = json.loads((relance / lc.MANIFESTES["relance"]).read_text(encoding="utf-8"))
    m_reg = json.loads((premiere / lc.MANIFESTES["regle"]).read_text(encoding="utf-8"))
    rt = m_rel.get("regle_tours", {})
    if rt.get("relance") is not True or rt.get("premiere_execution") != m_reg.get("regle_tours"):
        raise GardeArret("assemblage : le manifeste de relance ne cite pas la règle de la première exécution")
    if m_rel.get("graines") != m_reg.get("graines") or m_rel.get("commit_public") != m_reg.get("commit_public"):
        raise GardeArret("assemblage : graines ou code public différents entre les deux conduites")
    for src in _fichiers_scelles(premiere) + _fichiers_scelles(relance):
        scellement.verifier(src)
    cible.mkdir(parents=True)
    for p in premiere.iterdir():
        (shutil.copytree if p.is_dir() else shutil.copy2)(p, cible / p.name)
    shutil.copytree(relance / "principal-relance", cible / "principal-relance")
    for nom in (lc.MANIFESTES["relance"], lc.MANIFESTES["relance"] + ".sha256"):
        if (relance / nom).is_file():
            shutil.copy2(relance / nom, cible / nom)
    shutil.copytree(relance / "mise-en-place", cible / "relance-mise-en-place")
    shutil.copytree(relance / "controle-juge", cible / "relance-controle-juge")
    copies = _fichiers_scelles(cible)
    for f in copies:
        scellement.verifier(f)
    trace = {"premiere": str(premiere), "relance": str(relance), "fichiers_scelles_verifies": len(copies),
             "manifeste_relance_sha256": cv.sha_fichier(cible / lc.MANIFESTES["relance"]),
             "manifeste_regle_sha256": cv.sha_fichier(cible / lc.MANIFESTES["regle"])}
    (cible / "assemblage-v1.json").write_text(json.dumps(trace, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                                              encoding="utf-8")
    scellement.sceller(cible / "assemblage-v1.json")
    return trace

def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("commande", choices=["veilleur", "reprendre", "veilleur-arret"])
    p.add_argument("--poste")
    p.add_argument("--instance")
    p.add_argument("--echeance", type=float)
    p.add_argument("--journal")
    p.add_argument("--fournisseur", default="vast")
    p.add_argument("--periode", type=float, default=30.0)
    p.add_argument("--marge", type=float, default=MARGE_SECOURS_USD)
    p.add_argument("--battement")  # défaut : <journal>.battement (C2)
    p.add_argument("--rapatriement")  # v11 (C-2) : défaut <dossier du poste>/rapatriement-v11.json
    # v10 : reprise (après `git fetch origin main` ; GO lu sur origin/main, P-i)
    p.add_argument("--sortie")
    p.add_argument("--etiquette")
    p.add_argument("--go-id")
    p.add_argument("--depot", default=".")
    p.add_argument("--arreter-en-cours", action="store_true")
    a = p.parse_args(argv)
    if a.commande == "reprendre":
        if not (a.sortie and a.etiquette and a.go_id) or not a.etiquette.startswith(PREFIXE_ETIQUETTE):
            p.error("reprendre : --sortie, --go-id et --etiquette (préfixe de la conduite) requis")
        echeance = echeance_epoch(ligne_go(texte_go_main(Path(a.depot)), a.go_id)["echeance"])
        bilan = Reprise(fournisseur_depuis(a.fournisseur), Path(a.sortie), a.etiquette, echeance,
                        arreter_en_cours=a.arreter_en_cours, fournisseur_veilleur=a.fournisseur).reprendre()
        print(json.dumps({k: bilan.get(k) for k in ("instance", "statut", "detruite", "alertes", "issue")},
                         ensure_ascii=False))
        return 0 if bilan.get("detruite") or bilan.get("issue") else 3
    if a.commande == "veilleur-arret":  # v11 (C-1)
        if not (a.instance and a.etiquette and a.echeance is not None and a.journal):
            p.error("veilleur-arret : --instance, --etiquette, --echeance et --journal requis")
        VeilleurArret(fournisseur_depuis(a.fournisseur), a.instance, a.etiquette, a.echeance, Path(a.journal),
                      periode_s=a.periode, battement=a.battement).boucle()
        return 0
    if not (a.poste and a.instance and a.echeance is not None and a.journal):
        p.error("veilleur : --poste, --instance, --echeance et --journal requis")
    v = Veilleur(fournisseur_depuis(a.fournisseur), Path(a.poste), a.instance, a.echeance, Path(a.journal),
                 marge_secours=a.marge, periode_s=a.periode, battement=a.battement, rapatriement=a.rapatriement)
    v.boucle()
    return 0


if __name__ == "__main__":
    sys.exit(main())
