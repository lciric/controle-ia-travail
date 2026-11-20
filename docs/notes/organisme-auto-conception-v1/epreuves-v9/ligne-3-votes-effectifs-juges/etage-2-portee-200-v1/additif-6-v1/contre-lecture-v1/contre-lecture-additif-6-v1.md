# Contre-lecture de l'additif 6 v1 (code de l'étage 2 à 200, ligne 3, organisme v9) — v1

Pièce de travail (classe C), sur une pièce décisive (classe A). Écrite le 2026-11-20 (`date -u` : 16:39Z au relevé des chemins), sur le mandat `mandat-contre-lecteur-additif-6-v1.md` (`e42e2c42966b0b3e6f185c2f3d936f8a974e302b46e111677e9d3c3b5d9573f0`, recalculée sur son seul chemin, égale à son compagnon ; lu en entier, en-tête compris). Contre-lecteur neuf, modèle O : je n'ai écrit, contre-lu ni vérifié aucune pièce de la ligne 3.

Cible : `E/additif-6-v1/additif-6-code-etage-2-preenregistrement-ligne-3-v1.md`, `19016dcf3d0c735c7ff0ac30bf05c36a613eace4877bd463f8ffca63a0caa8a3` (égale au compagnon) ; rapport du rédacteur au même dossier, `2e8c554c3d7ec5213828d680162e2f3cb98080cd6d76aaaa9655efa1356c6b91` (égal au compagnon). Notations de la cible : `R`, `E`, `X`, `S`, `DOSSIER`.

## 0. Verdict

**À corriger.** 32 corrections, toutes de lettre ou de procédure, aucune ne touche une hypothèse, un seuil, une table, une racine ni un montant. Le code est bien nommé : chaque empreinte citée est égale au fichier ; chaque commande du § 6 passe l'analyse des arguments de son programme, sauf une (geste 9, `--plomberie PLOMBERIE_1,PLOMBERIE_2`, que le code refuserait faute d'identifiants de la version 2 : C11). Le reste des corrections porte les décisions de la mère de 16:27Z (relayées par la coordination), la décision inscrite depuis (R-4324), le relevé des essais sous l'interpréteur retenu, la commande des relais et leur déclaration (C15, texte proposé, à la demande de la mère), deux trous de procédure trouvés par moi (C9 : la garde ne vérifie pas l'empreinte de la banque ; C13 et C14 : l'audit de symétrie ouvrait les réponses brutes de la moitié « lecture »), et le passage en version 2 (C1 à C3, C8 : `CHEMIN` change avec le nom).

Jeu : `jeu-corrections-additif-6-v1.json` (format de `scripts/remplacer_texte_exact_v1.py`), essayé dans mon dossier sur la cible : « FAIT : 32 remplacement(s) », sortie d'essai `essai-application-jeu-additif-6-v2.md` (`9751d78aa6f6993029d79627463727667690a2614af8982aa0ec87b40eee15a0`), non versée : c'est un essai, la version 2 se fait par qui la mère désigne.

## 1. Fichiers et empreintes (tâche 1)

Programme `verifier_empreintes_v1.py`, sortie `sortie-verifier-empreintes-v1.txt` : **66 fichiers, 0 écart.** Recalculés sur les fichiers, par chemin complet : les sept pièces du § 0 (texte v7 de branche ; additifs 3 et 5, verdict de portée, tirés de `origin/main` par `git show` redirigé ; registres à la tête lue par le rédacteur, `16505cba…` = `origin/main~1`, égaux à `61d52dc1…` et `1d5ded65…` ; inventaire) ; les quatre programmes du § 2.1 et les deux versions 2 ; les quatre pièces du § 2.2 ; les vingt et une pièces du § 2.3 et le rapport v2 de l'étalonnage et de la lecture (`a72d6c06…`, cité au geste 11) ; les pièces épinglées du § 2.4, **dont les quatre autres modules du clone (`MODULES_ORCHESTRATEUR`), que le rédacteur n'avait pas recalculés : égaux** ; et les pièces des relais citées par C15. Toute pièce qui a un compagnon lui est égale. Les trois tables d'empreintes et le compagnon des fragments, rejoués par `env -C DOSSIER sha256sum -c` : toutes les lignes « OK » (6, 6 et 16 lignes ; sorties `sortie-table-*.txt`, `sortie-compagnon-fragments-v3.txt`). Les quatre « derniers commits » du § 2.1, relus par `git log -1 --format=%H` sur chaque chemin : égaux. Le relevé des essais sous l'interpréteur retenu, versé par la coordination pendant ma lecture : `E/additif-6-v1/releve-essais-interpreteur-systeme-v1.md`, `6210dd81771ac1a3410d39aab9e31755e05b9da9a1dd850252e7030137a69619`, égal à son compagnon ; 98 + 101 + 49 = 248 passés ; l'additif ne le cite pas (C4, C7, C24).

À la tête actuelle de `main` (`82e233f36f8d1ed6bb93ae03e2df279e08186435`, après `git fetch origin main`) : `registres/go.md` inchangé (`61d52dc1…`) ; `registres/decisions.md` a une ligne de plus, R-4324 (`e929694d177a0f5f37e67ed5c484d22a08c92e51cbefa33d33e250e92172a347`).

## 2. Commandes, contre l'analyse des arguments (tâche 2)

Lu dans le code, rien lancé.

| geste | programme, lieu lu | constat |
|---|---|---|
| 1 | générateur v3, `principal`, l. 1905 à 1917 ; `creer_journal_rejeux`, l. 1207 à 1228 | `len(argv) != 1` refusé : la commande sans argument passe ; sortie `{"journal": "créé vide"}`, code 0 ; refus nommé code 2. Le compagnon `manifeste-creation-journal-rejeux-v1.json.sha256` est bien écrit (`ecrire_scelle`) : le `git add` le nomme justement. `historique_connait` lit `git log --all` : le `fetch` borné met à jour les deux références suivies. Juste. |
| 2 | `principal`, l. 1918 à 1926 ; `geste_composer`, l. 1758 à 1793 | cinq arguments lus par `_argument` ; autorisation vérifiée avant toute dérivation (`Contexte`, l. 495 à 503 ; `verifier_autorisation`, l. 470 à 480 : fichier présent, empreinte égale). `sortie.mkdir(parents=False)` : le `mkdir E/execution-v1` est nécessaire, il est là. Noms des quatre sorties : égaux. Juste. |
| 4 | `principal_garde`, l. 1873 à 1891 ; `ARGUMENTS_GARDE`, l. 185 ; `jouer_la_garde`, l. 1335 à 1463 | quatre arguments obligatoires par paires : la commande passe ; codes 0, 4, 5 (une faute d'arguments rend 5, « garde non jouée », non 2 : l'additif dit bien 0/4/5). **La banque est lue sans empreinte attendue** (`_temoins_de_la_banque`, l. 1287 à 1304) : rien ne lie le passage à `HEX_BANQUE` sinon le champ `empreinte_banque` du rapport ; l'additif ne dit pas de le comparer (C9). |
| 6 | `principal`, l. 1927 à 1932 ; `geste_auditer`, l. 1815 à 1829 | `--orchestrateur` facultatif ; banque lue par empreinte ; codes 0, 4, 2. Juste. |
| 9 | code d'appel v4, `principal`, l. 1431 à 1448 ; `preparer_reel`, l. 1314 à 1358 ; `verifier_ligne_de_go`, l. 1226 à 1267 ; `executer`, l. 902 à 959 | `--reel` en tête ; huit arguments lus ; les onze noms passés sous `env -i` sont tous dans `VARIABLES_PERMISES` (l. 159 à 163), aucun ne répond au motif des noms de clé, `HTTPS_PROXY` exigé présent, `GO_ID` égal à `--go-id`. GO-2026-11-20-68, lue sur ma copie de `main` : une ligne principale, huit colonnes, « calcul », « Lazar », du 2026-11-20 au 2026-11-27, périmètre normalisé qui porte « ligne 3 » et « etage 2 », « 88,36 USD » = 8 836 centimes : elle passe la garde. **`--plomberie PLOMBERIE_1,PLOMBERIE_2` serait refusé** (`lire_temoins_v2`, l. 442 à 451 : identifiants absents des onze témoins) : C11, avec `t01,t07` décidés (t01 bon, t07 mauvais, item `epreuve_plantee`, relus au fichier `84a1e0ea…`, l. 14 à 16 et 122 à 124). À la relance, le code compare la liste de plomberie **dans son ordre** à celle de l'ouverture (l. 938) : dit en C12. `S/sortie/epreuve` : chemin du dépôt du code (l. 913). |
| 10 | étalonnage v3, `principal`, l. 596 à 612 ; `executer`, l. 531 à 584 | exactement neuf paires (l. 601 à 603) : la commande les porte toutes ; nom du fichier de verdicts conforme à `NOM_VERDICTS` (l. 117) et à `deposer` du code d'appel (l. 1115 à 1119) ; `DOSSIER` créé avec ses parents (l. 564) ; sorties `DOSSIER/etalonnage/etalonnage-etage-2-ligne-3-v3.json` et son manifeste. Juste. |
| 12 | lecture v3, `principal`, l. 757 à 779 ; `lire`, l. 348 à 404 ; `verifier_audit`, l. 289 à 304 | exactement onze paires : la commande les porte toutes ; la pièce d'étalonnage doit s'appeler `DOSSIER/etalonnage/etalonnage-etage-2-ligne-3-v3.json` (l. 355) et porter `DOSSIER` (l. 376) : tenu ; la pièce d'audit : `piece` égale à `PIECE_AUDIT` (l. 133), les cinq clés de `CONTROLES_AUDIT` (l. 134), mot pour mot celles du geste 11 ; compagnon exigé au format de `sha256sum` (étalonnage v3, l. 199 à 203) : la commande `env -C … sha256sum` du geste 11 le donne. Juste. |

Racines : générateur, `RACINES_SOUS_AUTORISATION` = 2026111934 et 2026111937 et tables gelées (l. 87 à 95) égales au § 3 ; code d'appel, `RACINE_ORDRE` 2026111935 et clés 1 à 4 (l. 116 à 117), sans garde d'autorisation, comme l'additif le dit ; lecture, `RACINE_LECTURE` 2026111936, clés 1 à 5, refus des autres racines (l. 111 à 116). Clé 4 : identifiants opaques (`Opaques`, l. 504 à 521). Interpréteur : `python3 --version` rend 3.13.18 ; le relevé de la coordination donne numpy 2.5.3 sous `/usr/local/bin/python3 -I -B`. Chemins : `X`, `S`, le dossier du journal des rejeux, `CHEMIN` et le dossier des relais proposé sont absents du disque (`stat`, 16:39Z).

## 3. Décisions citées, à la lettre de `origin/main` (tâche 3)

Copie `main-decisions.md` (tête `82e233f3…`), lignes extraites dans `sortie-decisions-citees.txt`.

| décision | ce que l'additif en dit | lettre du registre |
|---|---|---|
| R-4246 | fragments en données à part | « fragments en données à part » : égal |
| R-4272 | clone en lecture du service des juges | « l'organisme le lit par clonage anonyme » : égal |
| R-4273 | clé Luc pour le juge Opus (avec GO-55) | « -55 (recharges ; juge Opus de l'étage 2 sur Luc) » : égal |
| R-4287 | seconde branche du plafond ; racine 2026111935 clé 4 ; clé Luc ; six silences acceptés ; « tout refusé » non nommé | « plafond d'Opus par la seconde branche, racine 2026111935 clé 4, clé Luc, six silences acceptés » : égal ; « tout refusé » n'y est pas : égal |
| R-4289, R-4293 (b) | part de Luc, « reste relu moins 88,36 USD » ; 87,7701 = pire de l'étage entier | égal à la lettre de R-4293 (b) |
| R-4290 | voie (i), clés dans les seuls relais | égal |
| R-4298 | GO-68 vaut départ | « -68 (étage 2 de la ligne 3, 88,36 USD) » ; GO-68 : « départ accordé quand l'additif de code est scellé… » : égal |
| R-4305 | Luc, reste comptable 213,999998, aucun relevé possible | égal |
| R-4310 | M1 à M6 | égal, point par point |
| R-4316 | réserves A et B admises | égal ; mais le n° 34 du § 11 met aussi les « restes de procédure » sous R-4316, qui ne les nomme pas (C20) |
| R-4320 | lectures 1 à 5 de 15:55Z | égal |
| GO-26, -36, -49, -51, -55, -64, -68 | montants, échéances, clés | égaux ; GO-68 échoit le **2026-11-27** (colonne 6) ; GO-64 nomme « étage 2 de la ligne 3, juge Argon 15,41 » |

**Décisions « sans ligne au registre » : une est inscrite depuis**, R-4324 (16:20:15Z) : les deux points du silence n° 18 (16:12Z). Restent sans ligne à `82e233f3…` : « tout refusé » (14:01Z), les cinq décisions de 15:20Z sur le générateur, le silence n° 17 (16:01Z), le contrôle de `NO_PROXY`, et les décisions de 16:27Z que la coordination m'a relayées. C17, C21, C32 portent R-4324.

## 4. Les points du rédacteur (tâche 4)

| point | jugement |
|---|---|
| Racine 2026111935 déjà dérivée (essais l. 213 à 219, et le jeu entier des essais de bout en bout, l. 757) | **juste**. Question de la mère : cela touche-t-il l'aveugle ? **Non.** La permutation de `ordre_tire` porte sur les rangs des identifiants internes triés, et la suite des identifiants opaques de `Opaques` ne dépend que du nombre de tirages : les deux sont des fonctions des seuls nombres de témoins et de rendus. Le lien d'un rang ou d'un identifiant opaque à un témoin, donc à sa classe et à son item, passe par la composition et les identifiants internes (racine 2026111934, clés 1 à 6), qu'aucun essai n'a dérivés : les essais du générateur la refusent (essais v3, l. 17 à 18 et 228 à 232), ceux de l'étalonnage et de la lecture ne dérivent pas 2026111936 (l. 569 à 576). Le juge ne reçoit que le texte servi et l'identifiant opaque, et la garde « vérité non servie » refuse tout identifiant interne. Même si une sortie d'essai dérivée de 2026111935 était publiée sur la branche — je ne l'ai pas cherché, aucune liste hors de mon dossier —, elle ne porterait aucun fait sur la banque à venir. **Recommandation : déclaration seule, aucune racine neuve** (confiance 0,85 ; la réserve tient à ce que je n'ai pas relu les sorties de la contre-lecture du code d'appel, sans conséquence par l'argument ci-dessus). Porté par C5, C6, C23. |
| Réserve 6, marque au journal de construction | **juste** : le journal n'a aucun champ de marque (`geste_composer`, l. 1779 à 1783). Les quatre fragments sont tracés : `f-epr-dis-01` (vérification des fragments v1, l. 10 et 127), `f-epr-dis-05` et `f-voi-net-05` (même pièce, l. 350 et 358 ; « entrées » est au fichier v3, l. 609), `f-epr-net-04` (vérification v3, l. 8 et 29, sur la remarque de la v2). Une inexactitude : `usages_par_fragment` donne un compte, non les témoins ; ceux-ci se lisent au champ `fragments` de chaque entrée de `temoins` (C22, décision de la mère portée). |
| Part du juge Argon (15,41 couverts par GO-64, pire 30,44, compteur commun) | **juste** : GO-64 nomme 15,41 ; l'inventaire, l. 127, donne 11,34 / 15,43 / 30,44 ; `PLAFOND_C` est commun aux deux juges. Décision de la mère portée (C28). |
| Échéance de GO-2026-11-20-68 | **juste** : 2026-11-27, colonne « échéance » de la ligne ; la garde lit la date UTC du jour et admet le 27 lui-même (`d_acc <= aujourd_hui <= d_ech`, l. 1256). C29. |
| Pire cas du devis à 200 et rang 1 | **juste**, égal à la sortie du calcul v2 (l. 308 à 368, 550 à 562) : 996 envois sur 1 004, 87,7701 USD, 197 témoins complets dont les 100 de la moitié « lecture », « coupe_sans_manque » ; multiples 4,4102 / 3,5287 / 2,7148 / 1,9610 ; 147 envois et 88,20 USD si tout est refusé ; 91, 71, aucun. Écrit tel quel : aucune correction. |
| Partage tiré avant la garde | **juste** (`geste_composer`, l. 1784 à 1788, clé 6). C27. |
| Témoins de la plomberie | **juste** qu'aucun texte ne les nommait ; `t01,t07` décidés. C11, C12, C19, C10. |
| Commande de lancement des relais absente | **juste** : aucune pièce versée ne la porte ; la procédure écrite ne donne que des gabarits. Texte proposé, repris du lanceur v9 et de ce qu'il cite (C15, C26) : voir § 5 ci-dessous. |
| Les 53 silences du § 11 | relus contre leurs lettres là où j'ai pu : n° 6, 8, 9, 15 à 20, 21, 26, 35 justes ; n° 34 à corriger (C20) ; n° 1, 39, 42, 44 à 50, 53 changent par les décisions (C19, C21 à C30). Les autres, « jugés justes » par une pièce nommée, ne sont pas rouverts. |
| Contestation de la section 12 | **acceptée par la mère** (16:27Z) : la phrase devient le point 8 du § 10 (C18), la section garde sa marque (C31). Je la tiens pour fondée : la consigne dit « dans le doute, faux », et une lecture commune de sa lettre ferait monter ρ et les votes effectifs sans corrélation d'erreurs de jugement. |

## 5. La commande des relais et leur déclaration (C15)

Reprise du précédent le plus proche, l'épreuve des témoins v9 (`scripts/epreuve_temoins_auto_conception_v9.py`, même service de juges, mêmes deux fournisseurs) et de sa déclaration (`course-v4/declaration-relais-epreuve-temoins-auto-conception-v9.json`, `23c4a1c0…`), contre les contrôles que le code d'appel v4 appelle dans le lanceur v9 : `verifier_declaration` (l. 1812 à 1903 : `claude` en `claude_sdk`, `argon` en `commande_externe`, clés permises, nom de clé Claude égal à `--nom-cle-claude`, `url_etat_relais` d'Argon sur 8788) ; `verifier_procedure_relais` (l. 2035 à 2072 : porte « python -I -B » + porte épinglée, `--url`, `--modeles-permis` égal aux modèles Claude de la configuration, `--plafond-ligne` égal au plafond passé, 88,36) ; `controler_relais_vivant` (l. 1919 à 1958 : programme lu par identifiant de processus, port, variable, `--plafond-usd` égal à 88,36 pour Claude) ; `controler_relais_argon` et `verifier_borne_argon` (relais neuf, `--max-appels` ≥ 2 × 1 204 + 2 = 2 410, le calcul du code d'appel, l. 1383) ; la porte (`porte_plafond_relais_v1.py`, l. 60 à 71 : plafond du relais ≤ 88,36, modèles permis égaux, à blanc : dépense et appels nuls). Le lanceur de relais (`lancer_relais_local_v1.py`, l. 53 à 76) exige le dossier de la console présent, d'où le `mkdir`, et un nom exigé (`!`) présent et non vide. J'ai mis la liste des noms entre apostrophes droites, à cause du `!`. Interpréteur des relais : `/usr/bin/python3 -I -B`, celui de la procédure écrite (présent : 3.13.18). Aucun identifiant de modèle n'est écrit : `MODELES_CLAUDE` renvoie à la déclaration du précédent, et le relais du juge Argon garde son défaut.

## 6. Corrections (32)

Chaque ancre est sur une seule ligne de la cible. Contrôle par `construire_jeu_v1.py` (nombre de lignes qui portent l'ancre, sémantique de `grep -c -F -e`, et nombre d'occurrences ; zones sans chevauchement), sortie :

~~~~text
C1 à C32 : lignes (grep -c -F) : 1 ; occurrences : 1 ; « une fois » pour chacune
corrections : 32 ; fautes : 0
~~~~

puis par l'outil lui-même : « FAIT : 32 remplacement(s) ; cible 19016dcf… → sortie … (9751d78a…) ». C5 et C6 sont sur la même ligne (l. 111), en deux zones disjointes. Le texte ci-dessous est rendu du jeu par programme ; il lui est égal entrée pour entrée.


### C1 — titre

Ancien (une fois dans la cible) :

~~~~text
interpréteur, dossier de la lecture — v1
~~~~

Neuf :

~~~~text
interpréteur, dossier de la lecture — v2
~~~~

### C2 — statut (l. 3)

Ancien (une fois dans la cible) :

~~~~text
**Statut : version 1, non scellé. À contre-lire par un agent neuf de l'autre modèle (modèle O), puis vérification par le même, puis scellement par la mère, avant toute écriture de témoin (texte, l. 7).**
~~~~

Neuf :

~~~~text
**Statut : version 2, non scellé. Contre-lue par un agent neuf de l'autre modèle (modèle O) ; à vérifier par le même, puis à sceller par la mère, avant toute écriture de témoin (texte, l. 7).**
~~~~

### C3 — phrase de version (l. 3)

Ancien (une fois dans la cible) :

~~~~text
Version 1 : première écriture ; aucune version antérieure.
~~~~

Neuf :

~~~~text
Version 2 : corrections de la contre-lecture (contre-lecteur neuf, modèle O) et décisions de la mère de 16:27Z, relayées par la coordination, portées ; la version 1 (`19016dcf3d0c735c7ff0ac30bf05c36a613eace4877bd463f8ffca63a0caa8a3`) est gardée sans modification.
~~~~

### C4 — § 2.3, fin (l. 88)

Ancien (une fois dans la cible) :

~~~~text
Commande des essais, telle que les rapports la donnent (sur une copie du dossier, jamais dans le dépôt) : `env -C COPIE /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider FICHIER_D_ESSAIS`.
~~~~

Neuf :

~~~~text
Commande des essais, telle que les rapports la donnent (sur une copie du dossier, jamais dans le dépôt) : `env -C COPIE /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider FICHIER_D_ESSAIS`.

**Rejeu sous l'interpréteur retenu (§ 4), demandé par la mère (16:27Z)** : les trois suites, jouées sur copies par `env -C COPIE /usr/local/bin/python3 -I -B -m pytest -q -p no:cacheprovider F` (Python 3.13.18, numpy 2.5.3, pytest 9.1.1) : code d'appel v4, 98 passés ; générateur v3, 101 passés ; étalonnage et lecture v3, 49 passés ; 248 passés, 0 échec, 0 saut. Relevé : `additif-6-v1/releve-essais-interpreteur-systeme-v1.md` (sous `E`), `6210dd81771ac1a3410d39aab9e31755e05b9da9a1dd850252e7030137a69619`, égal à son compagnon ; sorties brutes au même dossier.
~~~~

### C5 — § 3, puce de l'écart (l. 111), début

Ancien (une fois dans la cible) :

~~~~text
- **Écart que je relève, à la mère (§ 11, n° 44).**
~~~~

Neuf :

~~~~text
- **Écart déclaré (§ 11, n° 44 ; mère, 16:27Z : déclaration seule, aucune racine neuve).**
~~~~

### C6 — § 3, puce de l'écart (l. 111), fin

Ancien (une fois dans la cible) :

~~~~text
Pour 2026111935, l'autorisation de cet additif est donc une règle de procédure : aucun envoi réel avant son scellement.
~~~~

Neuf :

~~~~text
Pour 2026111935, l'autorisation de cet additif est donc une règle de procédure : aucun envoi réel avant son scellement. **Cette dérivation ne touche pas l'aveugle** (contre-lecture de cet additif) : l'ordre tiré est une permutation des rangs des identifiants internes triés, et les identifiants opaques une suite tirée rendu après rendu ; l'un et l'autre ne dépendent que des nombres de témoins et de rendus. Le lien entre un rang, ou un identifiant opaque, et un témoin, donc sa classe, passe par les identifiants internes et la composition, tirés de 2026111934, qu'aucun essai n'a dérivée (le générateur la refuse hors autorisation) ; le juge ne reçoit que le texte servi et l'identifiant opaque. Une sortie d'essai dérivée de 2026111935, publiée ou non, ne dit rien de la vérité d'un témoin servi.
~~~~

### C7 — § 4, fin du dernier alinéa (l. 125)

Ancien (une fois dans la cible) :

~~~~text
**Je ne tranche pas** s'il faut rejouer les essais sous l'interpréteur retenu avant le départ (§ 11, n° 45).
~~~~

Neuf :

~~~~text
Les trois suites ont été rejouées sous l'interpréteur retenu avant le scellement, sur demande de la mère (16:27Z) : mêmes comptes, 248 passés (§ 2.3 ; § 11, n° 45).
~~~~

### C8 — § 5, ligne `CHEMIN` (l. 133)

Ancien (une fois dans la cible) :

~~~~text
`R/prereg/organisme-auto-conception-v9/additif-6-code-etage-2-preenregistrement-ligne-3-v1.md`
~~~~

Neuf :

~~~~text
`R/prereg/organisme-auto-conception-v9/additif-6-code-etage-2-preenregistrement-ligne-3-v2.md`
~~~~

### C9 — § 6, geste 4 (l. 187)

Ancien (une fois dans la cible) :

~~~~text
Aucun autre argument : ni `--repli`, ni `--piece-repli`, ni `--mot-de-la-mere`.
~~~~

Neuf :

~~~~text
Aucun autre argument : ni `--repli`, ni `--piece-repli`, ni `--mot-de-la-mere`. La garde ne prend pas l'empreinte de la banque en argument (`ARGUMENTS_GARDE`) : elle la calcule et l'écrit (`empreinte_banque`, au rapport et au manifeste du passage) ; l'exécutant la compare à `HEX_BANQUE` avant le commit, et la mère au scellement ; une autre valeur veut dire que la garde a porté sur une autre banque : retour à la mère, la banque n'est pas scellée.
~~~~

### C10 — § 6, geste 8 (l. 201)

Ancien (une fois dans la cible) :

~~~~text
les deux témoins de la plomberie (§ 11, n° 1) ; la déclaration des relais et son empreinte (§ 9).
~~~~

Neuf :

~~~~text
les deux témoins de la plomberie, `t01,t07` (§ 11, n° 1) ; la déclaration des relais et son empreinte, écrites selon le § 9 ; la confirmation du nom de la variable de la clé Google (§ 9).
~~~~

### C11 — § 6, geste 9, commande (l. 207)

Ancien (une fois dans la cible) :

~~~~text
--plomberie PLOMBERIE_1,PLOMBERIE_2 --nom-cle-claude
~~~~

Neuf :

~~~~text
--plomberie t01,t07 --nom-cle-claude
~~~~

### C12 — § 6, geste 9, première puce (l. 210)

Ancien (une fois dans la cible) :

~~~~text
- `DECLARATION`, `HEX_DECLARATION` : la déclaration scellée des relais, écrite au lancement des relais (§ 9) ; `PLOMBERIE_1,PLOMBERIE_2` : deux identifiants de témoins de la version 2, **à nommer par la mère** (§ 11, n° 1).
~~~~

Neuf :

~~~~text
- `DECLARATION`, `HEX_DECLARATION` : la déclaration scellée des relais et l'empreinte lue à son compagnon, écrites au lancement des relais (§ 9) : `/home/user/relais-ligne-3-etage-2-portee-200-v1/declaration-relais-ligne-3-etage-2-v1.json` à la première exécution, `…-v2.json` à la première relance, et ainsi de suite. `t01,t07` : les deux témoins de la version 2 de la plomberie, `t01` (bon) et `t07` (mauvais, item planté `epreuve_plantee`), décidés par la mère (16:27Z ; § 11, n° 1) ; toujours dans cet ordre (à la relance, le code compare la liste à celle de l'ouverture du journal).
~~~~

### C13 — § 6, geste 11, contrôle `lecteur_rend_absent_pour_illisible` (l. 228)

Ancien (une fois dans la cible) :

~~~~text
puis vérifié que, dans le dépôt, toute réponse brute illisible a un `verdict` nul.
~~~~

Neuf :

~~~~text
puis vérifié que, dans le dépôt, toute réponse brute illisible de la plomberie et de la moitié « étalonnage » a un `verdict` nul (la moitié « lecture » ne s'ouvre pas : § 11, n° 46).
~~~~

### C14 — § 6, geste 11, contrôle `appariement_temoin_verdict` (l. 229)

Ancien (une fois dans la cible) :

~~~~text
il se fait sur le journal, les réponses brutes et le fichier de la moitié « étalonnage » (§ 11, n° 46).
~~~~

Neuf :

~~~~text
il se fait sur le journal et, pour la plomberie et la moitié « étalonnage », sur les réponses brutes et leurs fichiers de verdicts ; les réponses brutes de la moitié « lecture » portent ses verdicts et ne s'ouvrent pas non plus : seule leur empreinte (`sha256sum`, par chemin) est comparée au `reponse_sha256` du journal (§ 11, n° 46).
~~~~

### C15 — § 9, puce des relais (l. 290)

Ancien (une fois dans la cible) :

~~~~text
- **Les relais et leur déclaration.** Le code d'appel reprend la procédure épinglée du lanceur de la course v9 : relais vivants contrôlés par identifiant de processus, relais neufs, plafond du relais du juge Opus égal à 88,36 USD, borne du relais du juge Argon à 2 410 actions, appel à blanc de chaque relais. La commande qui lance les relais et écrit la déclaration scellée n'est dans aucune pièce que j'ai lue : elle revient au mandat de lancement (§ 11, n° 47).
~~~~

Neuf :

~~~~text
- **Les relais et leur déclaration** (décision de la mère, 16:27Z : ils vont dans cet additif, repris du lanceur de la course v9 et de ce qu'il cite ; § 11, n° 47). Pièces, toutes épinglées par le lanceur v9 (`PIECES`, `PROGRAMMES_RELAIS`) et recalculées égales par la contre-lecture : procédure écrite `docs/procedures/relais-persistants-v1.md` (`0ca9cf5d…`) ; sa pièce `docs/notes/organisme-affinage-mentors-v1/course-v3/procedure-relais-persistants-course-affinage-v3.json` (`d97594db…`) ; lanceur de relais `scripts/lancer_relais_local_v1.py` (`d365affc…`) ; porte de plafond `scripts/porte_plafond_relais_v1.py` (`fab5fe2e…`) ; relais du juge Opus, au clone, `orchestrator/pole/relais_reel.py` (`1b90b020…`) ; relais du juge Argon `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py` (`2b0043bc…`) ; enveloppe du juge Argon `rapports/fille-ideation-1-v1/appel-argon-sans-troncature-v1.sh` (`7c3d8847…`). Précédent suivi à la lettre : la déclaration de l'épreuve des témoins v9, `docs/notes/organisme-auto-conception-v1/course-v4/declaration-relais-epreuve-temoins-auto-conception-v9.json` (`23c4a1c02ca512e8e3f97b250ebca66ebdcf283440ea56522c7ea7b3f99c145f`), mêmes deux fournisseurs ; seuls changent la clé du juge Opus, les identifiants de processus et le plafond de ligne. Dossier des relais, hors du dépôt : `Q` = `/home/user/relais-ligne-3-etage-2-portee-200-v1` (absent du disque à 16:39Z ; placé par la contre-lecture, comme `S`, à confirmer par la mère). Par l'exécutant, après le mot de départ et avant le geste 9, la clé Luc et la clé Google posées dans **son** environnement sous leur nom (jamais sur une ligne de commande, jamais lues) :

```
mkdir /home/user/relais-ligne-3-etage-2-portee-200-v1
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/relais-ligne-3-etage-2-portee-200-v1/console-relais-claude-v1.txt 'PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_LUC' -- /usr/bin/python3 -I -B /home/user/lciric/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_LUC --port 8787 --plafond-usd 88.36 --modeles-permis MODELES_CLAUDE --journal /home/user/relais-ligne-3-etage-2-portee-200-v1/journal-relais-claude-v1.jsonl
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/relais-ligne-3-etage-2-portee-200-v1/console-relais-argon-v1.txt 'PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY' -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle GEMINI_API_KEY --port 8788 --max-appels 2410 --journal /home/user/relais-ligne-3-etage-2-portee-200-v1/journal-relais-argon-v1.jsonl
```

Chaque lanceur imprime une ligne JSON qui porte le `pid` du relais : `PID_CLAUDE`, `PID_ARGON` ; code 2 sur tout refus, rien lancé (clé absente ou vide comprise). `MODELES_CLAUDE` : la chaîne exacte de `--modeles-permis` de la déclaration de l'épreuve des témoins v9 (l. 5), deux identifiants séparés par une virgule, sans espace ; c'est l'ensemble que rend `modeles_claude_de_la_configuration` sur la configuration `3f662ee8…`, que le code d'appel exige à la commande de la porte (lanceur v9, l. 2055 à 2066) et que la porte exige égal à celui du relais (`porte_plafond_relais_v1.py`, l. 66) ; aucune pièce de ce lot n'écrit un identifiant de modèle. Le relais du juge Argon garde son modèle par défaut (`MODELES_DEFAUT` du relais, égal à `MODELE_ARGON` du lanceur v9) : aucun `--modele`. `GEMINI_API_KEY` est le nom de variable du précédent (même déclaration, l. 7) ; la mère confirme au mot de départ que c'est celui de la clé Google (GO-2026-11-20-68). Puis la déclaration, écrite par l'outil d'écriture à `/home/user/relais-ligne-3-etage-2-portee-200-v1/declaration-relais-ligne-3-etage-2-v1.json`, exactement ceci, les deux `PID_…` remplacés par les entiers lus et `MODELES_CLAUDE` par sa chaîne :

```
{"version": "declaration-relais-ligne-3-etage-2-portee-200-v1", "fournisseurs": {
 "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:8787", "nom_cle": "RR_ANTHROPIC_API_KEY_LUC", "pid_relais": PID_CLAUDE,
            "porte_plafond": {"type": "commande", "delai_s": 30, "commande": ["/usr/local/bin/python3", "-I", "-B",
              "/home/user/controle-ia-travail/scripts/porte_plafond_relais_v1.py", "--url", "http://127.0.0.1:8787",
              "--modeles-permis", "MODELES_CLAUDE", "--plafond-ligne", "88.36"]}},
 "argon": {"type": "commande_externe", "commande": ["bash", "/home/user/controle-ia-travail/rapports/fille-ideation-1-v1/appel-argon-sans-troncature-v1.sh"],
           "nom_cle": "GEMINI_API_KEY", "pid_relais": PID_ARGON, "url_etat_relais": "http://127.0.0.1:8788",
           "porte_plafond": {"type": "environnement"}}}}
```

```
env -C /home/user/relais-ligne-3-etage-2-portee-200-v1 sha256sum declaration-relais-ligne-3-etage-2-v1.json > /home/user/relais-ligne-3-etage-2-portee-200-v1/declaration-relais-ligne-3-etage-2-v1.json.sha256
```

`DECLARATION` = ce chemin ; `HEX_DECLARATION` = l'empreinte lue à ce compagnon (geste 9). Le contrôle des relais est celui du code d'appel, au geste 9, avant tout envoi (`verifier_declaration`, `verifier_procedure_relais`, `verifier_borne_argon`, `porte_a_blanc` du lanceur v9) : refus (code 2, rien de dépensé) de toute déclaration hors de cette forme ; de tout relais dont le programme, lu par identifiant de processus, n'a pas l'empreinte épinglée, ou dont le port, la variable de clé ou le plafond diffèrent de la déclaration (relais du juge Opus : `--plafond-usd` égal à 88,36) ; d'un relais du juge Argon non neuf ou borné sous 2 410 actions ; d'une porte qui ne passe pas à blanc (dépense et appels nuls). Rien de l'environnement d'un relais n'est lu. **Relance** (geste 9) : les relais de l'exécution précédente sont relevés (`/relais/etat`, procédure écrite, § 5) puis arrêtés par identifiant de processus (procédure écrite, § 6 ; règle R10) ; relais neufs aux mêmes ports, fichiers de rang suivant (`console-relais-claude-v2.txt`, `journal-relais-claude-v2.jsonl`, `console-relais-argon-v2.txt`, `journal-relais-argon-v2.jsonl`, `declaration-relais-ligne-3-etage-2-v2.json` et son compagnon) ; le plafond du relais du juge Opus reste 88,36 USD (§ 11, n° 10). **À la fin** : même relevé, même arrêt, consignés au registre des arrêts ; `Q` est versé avec `S` par la mère. **Interpréteur des relais et de leur lanceur** : `/usr/bin/python3 -I -B`, celui de la procédure écrite (§ 2 et § 2.1 à 2.3), Python 3.13.18 (relevé par la contre-lecture) ; la porte, lancée par le code d'appel, garde `/usr/local/bin/python3 -I -B` du précédent. Écart déclaré au « tous les gestes » du § 4 : relais, lanceur et porte n'emploient que la bibliothèque standard.
~~~~

### C16 — § 10, titre

Ancien (une fois dans la cible) :

~~~~text
## 10. Lectures de la mère (15:55Z, R-4320 ; 16:01Z et 16:12Z, rapportées)
~~~~

Neuf :

~~~~text
## 10. Lectures de la mère (15:55Z, R-4320 ; 16:01Z, rapportée ; 16:12Z, R-4324 ; 16:27Z, rapportées)
~~~~

### C17 — § 10, point 7

Ancien (une fois dans la cible) :

~~~~text
(rapportées par la coordination et par le rapport v3 ; **à inscrire au registre** : aucune ligne au registre lu ; portées par
~~~~

Neuf :

~~~~text
(rapportées par la coordination et par le rapport v3 ; **inscrites depuis : R-4324**, `origin/main` `82e233f36f8d1ed6bb93ae03e2df279e08186435` ; portées par
~~~~

### C18 — § 10, après le point 7

Ancien (une fois dans la cible) :

~~~~text
champ absent ou différent : refus nommé.
~~~~

Neuf :

~~~~text
champ absent ou différent : refus nommé.
8. **Réserve sur ρ et les votes effectifs** (mère, 16:27Z, rapportée ; reprise de la contestation du § 12). Le verdict de l'agent neuf (geste 13) rapporte le comptage `cartes_tombees_sur_reserves_tenues_premier_rendu` de la pièce d'étalonnage à côté de ρ entre juges et du nombre de votes effectifs, et les place sous réserve nommée si les rejets de bons témoins sur `reserves_tenues` se concentrent, pour les deux juges, sur les témoins à fragment « voisins » conforme non citant. Sans seuil chiffré. Rien d'autre ne change : ni la vérité plantée, ni la table, ni un rang.
~~~~

### C19 — § 11, n° 1

Ancien (une fois dans la cible) :

~~~~text
| **à la mère**, avant le scellement. Proposition, non une règle : `t01,t07`, un bon et un mauvais, pour voir une réponse lisible de chaque classe |
~~~~

Neuf :

~~~~text
| décidé (mère, 16:27Z) : `t01,t07`, un bon et un mauvais (geste 9) |
~~~~

### C20 — § 11, n° 34

Ancien (une fois dans la cible) :

~~~~text
| admis (R-4316) ; § 7 |
~~~~

Neuf :

~~~~text
| réserves A et B admises (R-4316) ; restes de procédure (contrôle du (4), R-a à R-c) : § 7, sans ligne au registre |
~~~~

### C21 — § 11, n° 39

Ancien (une fois dans la cible) :

~~~~text
porté en v3 ; à inscrire |
~~~~

Neuf :

~~~~text
porté en v3 ; inscrit (R-4324) |
~~~~

### C22 — § 11, n° 42, état

Ancien (une fois dans la cible) :

~~~~text
| **à la mère**, avant le scellement de la banque. Proposition, non une règle : une pièce scellée jointe au journal, qui nomme ces fragments ; les témoins qui les emploient se lisent au journal (`usages_par_fragment`) ; la réserve 6 s'étend alors, pour eux, à la corrélation entre juges |
~~~~

Neuf :

~~~~text
| décidé (mère, 16:27Z) : nommés ici, sans code neuf. `f-epr-dis-01` (phrase du vérificateur des fragments v1, mot pour mot) ; `f-epr-dis-05` et `f-voi-net-05` (un mot proposé par lui chacun) ; `f-epr-net-04` (récrit en v3 sur la remarque de la vérification v2). Les témoins qui les emploient se lisent au journal de construction (champ `fragments` de chaque entrée de `temoins` ; `usages_par_fragment` n'en donne que le compte) |
~~~~

### C23 — § 11, n° 44

Ancien (une fois dans la cible) :

~~~~text
| **à la mère** : accepter et déclarer, ou version neuve du code |
~~~~

Neuf :

~~~~text
| décidé (mère, 16:27Z) : déclaré, sans racine neuve ; la dérivation ne touche pas l'aveugle (§ 3) |
~~~~

### C24 — § 11, n° 45

Ancien (une fois dans la cible) :

~~~~text
| essais joués sous numpy 2.4.6, exécution sous numpy 2.5.3 (§ 4) | **à la mère** |
~~~~

Neuf :

~~~~text
| essais joués sous numpy 2.4.6, exécution sous numpy 2.5.3 (§ 4) | levé : suites rejouées sous `/usr/local/bin/python3 -I -B`, numpy 2.5.3, 248 passés (relevé `6210dd81…`, § 2.3) |
~~~~

### C25 — § 11, n° 46

Ancien (une fois dans la cible) :

~~~~text
| **à la mère** ; c'est ma lecture de « aucun verdict de la moitié lecture » |
~~~~

Neuf :

~~~~text
| **à la mère** ; lecture portée au geste 11 : ni les verdicts ni les réponses brutes de la moitié « lecture » ne s'ouvrent, leurs empreintes seules sont comparées |
~~~~

### C26 — § 11, n° 47

Ancien (une fois dans la cible) :

~~~~text
| 47 | commande de lancement des relais et de leur déclaration (§ 9) | **à la mère**, au mandat de lancement |
~~~~

Neuf :

~~~~text
| 47 | commande de lancement des relais et de leur déclaration (§ 9) | décidé (mère, 16:27Z) : écrites au § 9, reprises du lanceur de la course v9 |
~~~~

### C27 — § 11, n° 48

Ancien (une fois dans la cible) :

~~~~text
| **à la mère** ; déclaré |
~~~~

Neuf :

~~~~text
| décidé (mère, 16:27Z) : écrit tel quel ; déclaré |
~~~~

### C28 — § 11, n° 49

Ancien (une fois dans la cible) :

~~~~text
| **à la mère**, pour Lazar s'il y a lieu |
~~~~

Neuf :

~~~~text
| décidé (mère, 16:27Z) : la borne qui tient est le compteur commun de GO-2026-11-20-68 (88,36 USD, les deux juges) ; le pire du juge Argon, 30,44 USD, passe sur la carte Google sous GO-2026-11-20-64, au-delà des 15,41 USD que cette ligne nomme : déclaré |
~~~~

### C29 — § 11, n° 50

Ancien (une fois dans la cible) :

~~~~text
| lecture de la lettre de la ligne ; à confirmer par la mère |
~~~~

Neuf :

~~~~text
| confirmé par la mère (16:27Z) ; le 27 compris, date UTC lue par la garde (`verifier_ligne_de_go`) |
~~~~

### C30 — § 11, n° 53

Ancien (une fois dans la cible) :

~~~~text
| **à confirmer par la mère** : s'ils changent, `CHEMIN` change avec eux, par une version neuve contre-lue |
~~~~

Neuf :

~~~~text
| rang 6 confirmé (R-4324 : « l'additif 6 ») ; en version 2, `CHEMIN` porte « -v2 » (§ 5) |
~~~~

### C31 — § 12, statut

Ancien (une fois dans la cible) :

~~~~text
**Cette section n'est pas une règle. Elle ne lie personne tant que la mère ne l'a pas reprise.**
~~~~

Neuf :

~~~~text
**Cette section n'est pas une règle. La mère l'a reprise (16:27Z) : la phrase proposée est au § 10, point 8, où elle vaut.**
~~~~

### C32 — § 14, réserve 6

Ancien (une fois dans la cible) :

~~~~text
le silence n° 17 (16:01Z), les deux points de 16:12Z. Je les écris comme telles.
~~~~

Neuf :

~~~~text
le silence n° 17 (16:01Z), les deux points de 16:12Z (ceux-ci inscrits depuis : R-4324). Je les écris comme telles ; les décisions de 16:27Z (version 2) ne sont connues que par la coordination.
~~~~

## 7. Points pour la mère, avec recommandation

1. **Racine 2026111935 et l'aveugle** (C5, C6, C23). La dérivation par les essais ne touche pas l'aveugle (§ 4 ci-dessus). Recommandation : déclaration seule, aucune racine neuve ; rien à porter à Lazar. Confiance 0,85.
2. **Audit de symétrie, portée de ce qu'il ouvre** (C13, C14, n° 46). Telle qu'écrite, la v1 faisait vérifier « toute réponse brute illisible » du dépôt et l'appariement « sur les réponses brutes » : or une réponse brute de la moitié « lecture » porte son verdict ; l'agent neuf l'aurait lu avant la lecture unique, contre la phrase même du geste 11 et la l. 297 du texte. Recommandation : la portée de C13 et C14 (plomberie et moitié « étalonnage » ouvertes ; moitié « lecture » par empreintes seules). Confiance 0,8. Si la mère juge qu'une empreinte calculée sur le fichier est déjà une ouverture, l'appariement de la moitié « lecture » se réduit au journal seul : unicité des identifiants opaques et rendus nommés du plan.
3. **Garde et banque** (C9). La garde ne reçoit pas `HEX_BANQUE` : recommandation, la comparaison écrite de `empreinte_banque` à `HEX_BANQUE` par l'exécutant puis par la mère, sans code neuf. Confiance 0,9.
4. **Relais** (C15). À confirmer au mot de départ : le dossier `Q` (choix de la contre-lecture) ; `GEMINI_API_KEY` comme nom de la clé Google (repris du précédent) ; la chaîne `MODELES_CLAUDE`, que je laisse en renvoi au précédent pour n'écrire aucun identifiant de modèle (recommandation : la garder ainsi ; l'exécutant la recopie de la déclaration v9, l. 5) ; l'interpréteur `/usr/bin/python3` des relais, écart déclaré au § 4. Confiance 0,75 : la forme est celle du précédent et passe, à ma lecture, chaque contrôle du code ; rien n'a été lancé (n° 22).
5. **Décisions encore sans ligne au registre** : « tout refusé » (14:01Z), les cinq décisions de 15:20Z, le silence n° 17 (16:01Z), `NO_PROXY`, et celles de 16:27Z (témoins `t01,t07` ; relais dans l'additif ; réserve sur ρ ; part d'Argon ; réserve 6 ; racine 2026111935 ; rejeu des essais). Recommandation : les inscrire avant le scellement ; si leurs lignes existent alors, la vérification de la v2 remplace « rapportées » par la ligne, sans autre changement.
6. **Nom de la version 2** (C1 à C3, C8, C30). `CHEMIN` devient `…-ligne-3-v2.md`, comme l'additif 5 scellé en v2. L'autorisation des racines est le fichier scellé à ce chemin, présent sur disque là où l'étage tourne.
7. **Échéance** (C29) : le départ et toute relance doivent tenir au plus tard le 2026-11-27, date UTC.

## 8. Écarts et limites

1. `git fetch origin main` fait (mandat, point 3) : il a avancé `origin/main` de `16505cba…` à `82e233f3…` (références seulement). Pour reproduire la tête du rédacteur, deux `git show origin/main~1:…` redirigés dans mon dossier : écart de forme à « `git show` sur `origin/main` », déclaré.
2. Recherches par motif (outil de recherche) sur des **fichiers nommés** : programmes et essais de l'étage 2, lanceur et épreuve v9, relais (dont `relais_reel.py` au clone, lecture seule), porte, fragments v3, témoins v2, vérifications des fragments, inventaire, rapport v1 de l'étalonnage. Aucune recherche sur un dossier, aucune liste hors de mon dossier.
3. `stat` sur cinq chemins nommés ; `wc -l` sur deux fichiers ; `git log -1 --format=%H` sur quatre chemins ; `git rev-parse origin/main` ; `/usr/bin/python3 --version` ; `date -u`.
4. `scripts/remplacer_texte_exact_v1.py` lancé une fois (outil du dépôt, hors de l'étage 2), cible lue sans écriture, sortie d'essai et son journal dans mon dossier.
5. Je n'ai rejoué aucun essai ; je n'ai pas relu les sorties de la contre-lecture du code d'appel ni cherché sur la branche une sortie dérivée de 2026111935 (point 7.1). Je n'ai pas relu les rapports et contre-lectures qui fondent les silences « jugés justes ».
6. La coordination m'a écrit deux fois pendant le travail (décisions de la mère de 16:27Z ; comptes du rejeu des essais) : mes corrections les portent comme « relayées », non comme lignes de registre.
7. Aucun programme de l'étage 2 lancé ; aucune commande sur un chemin sous `archives-reponses-modeles/` ; aucun appel, aucune clé lue, aucune dépense ; aucune écriture dans le dépôt ni dans le clone ; rien sous `/root/.claude/` ; aucune publication. **Aucun refus de permission, de classifieur ni de garde.**

## 9. Fichiers de mon dossier

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-additif-6/`. Chacun a son compagnon `.sha256`.

- cette pièce, `contre-lecture-additif-6-v1.md`, assemblée de `partie-1-tete-v1.md`, `partie-2-corrections-v1.md` (rendue du jeu par `rendre_corrections_v1.py`, qui contrôle l'égalité entrée pour entrée) et `partie-3-fin-v1.md` ;
- le jeu, `jeu-corrections-additif-6-v1.json`, construit et contrôlé par `construire_jeu_v1.py` (sortie recopiée au § 6) ;
- `verifier_empreintes_v1.py` et `sortie-verifier-empreintes-v1.txt` ; `extraire_v1.py` et `sortie-decisions-citees.txt` ; `espaces_v1.py` ; sorties des tables (`sortie-table-code-appel-v4.txt`, `sortie-table-generateur-v3.txt`, `sortie-table-etalonnage-lecture-v3.txt`, `sortie-compagnon-fragments-v3.txt`) ;
- copies de `main` : `main-go.md`, `main-decisions.md`, `main-1-go.md`, `main-1-decisions.md`, `main-additif-3-v3.md`, `main-additif-5-v2.md` (et `main-additif-5-v2.md.sha256.copie`, son compagnon de `main`), `main-verdict-portee-200-v2.md`, `log-main.txt` ;
- l'essai d'application : `essai-application-jeu-additif-6-v2.md`, son compagnon et son journal, écrits par l'outil.

Contre-lecteur neuf, modèle O.
