# Relecture courte en différentiel du code de la condition 6 (v2 → v3) — témoin Bailey — v1

- Lecteur : R2, sous-agent neuf. Je n'ai écrit ni le texte scellé, ni le code, ni les essais, ni le rapport appliqué, ni
  la liste des lectures. Date : `date -u` = Tue Nov 10 13:08:21 UTC 2026 (fin des sondes).
- Je reçois d'office le `CLAUDE.md` du dépôt (`b4cbc66a422a6246df0479fe0c886eccb92cd3410d6a8b742eddea5325098eae`).
- Dépôt : `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit `dd92b0ff`, arbre propre
  avant ce rapport ; `origin/main` = `617d77d4`.
- Pièces lues et empreintes (SHA-256, sur disque) :
  - texte qui prime : `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3`), l. 228-381 ;
  - rapport appliqué : `relecture-differentiel-code-condition6-v2-bailey-v1.md` (`4f079ece87032adaddfa4e4de312e4626124f187e2b335131abcaea4553660ca`), en entier ;
  - liste des lectures : `lectures-a-acter-addendum-condition6-v1.md` (`06ab92683f386be5bfdc96da49eb2c3cf37834a607b0f8c2801eb918cb21bf50`), en entier ;
  - décision : `registres/passations/2026-11-10-1240-decision-lazar-noeud5-lecture-b2.md` (`2f3e8e3a0bbb37543b9cada3f019eb77d700acb734c0f75638332e7f4871f2a2`) ;
  - ligne réelle de GO : `git show origin/main:registres/go.md`, l. 300 (GO-2026-11-10-10) et l. 1-8 (format) ;
  - code, `diff -u` v2 → v3 et, pour `lanceur_v3.py` et `lecture_v3.py`, lecture en entier :
    `conventions_v3.py` (`51c2fa26…`), `journaliseur_v3.py` (`9f75407c…`), `execution_v3.py` (`279f1f4f…`),
    `instance_v3.py` (`0f9aa54b…`, différentiel, puis l. 108-599 en entier), `lecture_v3.py`
    (`66c27382496e3a647757e3ce7cb9c3676c763a1dbf26783983b577409c295a62`), `lanceur_v3.py`
    (`313f40196233524a05e8560121345f03c32b3452e43d0bfe02ab657f02eebc6a`) ; v2 : empreintes du rapport `4f079ece`
    (inchangées) ; `analyse_v3.py` (`c28c6821…`) : `validite`, `nombre_de_tours`, `garde_nombre_de_tours`,
    `garde_fin_de_run` seulement ;
  - essais : `tests/test_temoin_bailey_condition6_v3.py` (`c7d8245f2068a64f6090a5035b05b232c9ebc49e18de67fd1401e3f66062d5ad`),
    section conduite (l. 1010-1383) en entier, le reste par la liste des essais et les essais S-1, 6, 7 ;
  - `docs/notes/reproduction-attaque-publiee-v1/versions-figees-temoin-bailey-v1.json` (`e21bccf6…`), en tête.
- Non lu : `donnees/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`, `diag/`, tout
  résultat, note ou seuil de sonde ou de moniteur du programme, tout résultat d'attaque contre le juge de l'organisme,
  `registres/decisions.md`, `registres/etat.md` ; le reste du texte scellé et du devis ; le code public des auteurs
  (non nécessaire à ce différentiel). Pour D-6, j'ai compté les entrées de `git archive HEAD` par dossier de premier
  niveau, sans ouvrir aucun fichier.
- Outils : `sha256sum`, `git` (dont `git show origin/main:…`, aucune requête réseau), `diff -u`, `grep`, `sed` ; essais
  demandés : **87 passés, 1 sauté** (essai manquant 7 : `joblib` absent) ; une épreuve de `trap … EXIT` de bash sous
  SIGTERM de groupe (le piège s'exécute) ; sondes du lecteur :
  `/tmp/claude-0/-home-user/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/diff-c6-v3/test_sondes_r2_v3.py`
  (`28b9acb26b173b473b16a86b775d8efb86671bab262ccaccda2699fba070c6d8`), 12 sondes, **12 passées** (chacune passe
  quand le défaut est présent), lancées par `PYTHONPATH=src:tests python -m pytest -q -p no:cacheprovider <fichier>` ;
  elles réemploient les aides de l'essai (`conduite`, `reponses`, `FournisseurFactice`) sans rien modifier. Aucun appel
  à `vastai`, aucune dépense, rien de committé. Rapport non scellé.

Renvois : « La l. n » = `lanceur_v3.py` ; « Le l. n » = `lecture_v3.py` ; « I l. n » = `instance_v3.py` ; « J » =
`journaliseur_v3.py` ; « X » = `execution_v3.py` ; « E l. n » = l'essai v3 ; « S-x » = sonde du lecteur.

## Verdict

**Conforme après corrections.** La v3 applique bien le fond du rapport `4f079ece` : la conduite décide sur l'état de
l'enfant (corrections 1, 2), `valider` ne reçoit plus rien de l'appelant et ne fabrique plus rien (correction 4), les
pertes par pas vont au journal des notes (6), tout transfert égal est scellé (7), et `verifier_go` passe sur la ligne
réelle GO-2026-11-10-10 avec B = 75 (et refuse 120). Mais la **destruction garantie** et la tenue de la conduite sur
plusieurs jours ne le sont pas : quatre défauts neufs, démontrés, laissent une instance vivante ou détruite sans
transfert, contre la lecture actée de « B − 2 » (D-1 à D-4). Ils se corrigent sur place dans `Conduite`, `Veilleur` et
`FournisseurVast` (corrections C1 à C7, section 4). L'addendum de la condition 6 peut être scellé **après** C1 à C7 et
leurs essais (contrôle par une relecture des seules lignes touchées) et après le mot de Lazar sur les lectures 4, 6, 7,
8 et 16 (section 3).

## 1. Corrections 1 à 18 du rapport `4f079ece`

| # | État | Lignes v3 | Constat |
|---|---|---|---|
| 1 | faite | Le l. 86-115 ; La l. 715-758 ; I l. 517-521, 581-584 ; La l. 497-506 | décision sur `code_retour`, `cause_arret`, gardes tombées, tours ; « sonde orientée » au pilote → arrêt ; dépense ou échéance → arrêt ; relance si < 20 tours et (code ≠ 0 ou garde de démarrage), jamais après « sonde orientée » ni sur budget. Essais S1, S2, S2b, S3, sonde orientée au principal, dépense au pilote : E l. 1198-1282. |
| 2 | faite | La l. 316-329, 649, 662-664 | champ obligatoire, B de chaque instance antérieure comparé, refus d'une instance non détruite ; E l. 1284-1299. La lecture de `registres/depenses.md` reste à l'appelant (lecture 20). |
| 3 | **en partie** | La l. 766-787, 509-529, 385-402 | rapatriement dans son `try`, destruction dans tous les cas **une fois dans le `try`**, `scp` en échec = écart, veilleur en processus séparé : faits, éprouvés (E l. 996-1012, 1302-1324). Mais la fenêtre création → `try` (La l. 666-675) n'est pas couverte (D-1), et le veilleur meurt à la première erreur et n'est jamais vérifié vivant (D-2). |
| 4 | faite | Le l. 220-323, 120-143, 170-196 | (a) K′ déclaré lu à l'état, tour K′ contrôlé (l. 300-307) ; (b) réempreinte et dossier de foi (l. 170-184) ; (c) étiquettes lues (l. 120-129 ; J : champ `table`). L1, L2, L3 tombent (E l. 297-340). |
| 5 | faite | I l. 477, 495 ; La l. 213-219, 341-342, 360, 609 | arrêt à échéance − marge ; secours au plus tard à l'échéance, délai positif refusé ; `verifier_echeance` à B − 0,5 + marge. S6 rend une cause (E l. 968-975). |
| 6 | faite | J (`CLES_TECHNIQUES`, `log`) | liste fermée de clés techniques ; tout le reste au journal des notes ; faux déroulé avec `behavior_loss`/`obf_loss` (E l. 460-488). |
| 7 | faite | La l. 814-820 ; Le l. 187-196, 262, 279, 308 | scellement après égalité ; vérification par `scellement.verifier` ; relance lue au dossier. |
| 8 | faite | I l. 147-189 ; C `VERSIONS_EXIGEES` | dictionnaire vide refusé ; paquets exigés ; `strong_reject` au commit du texte ; M1, M2 (E l. 710-730). |
| 9 | faite (lecture à acter) | I l. 111-136 ; C `MEMOIRE_VIVE_MIN_OCTETS` | octets décimaux, minimum `MemTotal`/groupe de contrôle (E l. 732-746). |
| 10 | faite | La l. 625-634, 692-694, 704-706, 745-746, 755-757 | manifestes versionnés, sans écrasement, scellés, envoyés ; la relance garde la règle de la première exécution. |
| 11 | faite | C `SORTANTS` ; I l. 539-543 ; La l. 812-813 | fichiers d'état empreintés et transférés ; dictionnaires gardés au bilan. |
| 12 | faite (réserve D-6) | La l. 407-451, 538-553 | archive empreintée, vérifiée par `sha256sum -c` ; jeton par fichier 600, effacé (piège `EXIT`, éprouvé sous SIGTERM). Mais l'archive est le dépôt entier (D-6). |
| 13 | faite (réserve D-4) | I l. 74-81, 234, 265, 323, 335 ; La l. 589-623 | mise en place et contrôle du juge s'arrêtent à B − 2 et à l'échéance − marge ; la conduite vérifie avant chaque commande. Pendant une exécution, la borne locale n'a plus de terme de dépense (D-4). |
| 14 | faite | J (« dossier neuf ») ; X l. 64-73 | état écrit dans `gardes-lanceur-v3.jsonl` avant de lever. |
| 15 | faite | Le l. 419-472, 360-397 ; J `_memoire` | rejeu de l'appariement, de la longueur du suffixe, de la dépense ; « fait foi » dit (l. 23-25) ; mémoire de carte `None` signalée ; tailles ≠ 200 signalées ; mémoire vive au pic rapportée ; erreur de mémoire écrite. |
| 16 | faite | I l. 560-563, 447-448 | `--echeance-go` et `--depense` requis. |
| 17 | **en partie** | E l. 779-800, 814-831, 843-850 | essai 1 (commit, arbre, fichier modifié) fait ; essai 6 contre un vrai `@hydra.main` fait ; essai 7 sauté ici (`joblib` absent) : l'import reste non éprouvé dans un environnement aux dépendances du clone. |
| 18 | **en partie** | liste `06ab9268` | la liste existe ; l'addendum n'est pas écrit (attendu à ce stade). |

## 2. Défauts neufs (sondes du lecteur)

**D-1 (bloquant). Instance créée, jamais détruite, si une étape entre la création et le `try` lève.** La l. 665-675 :
`taux_horaire`, `Poste.ecrire`, `_etape` et le lancement du veilleur sont hors du `try … finally` qui commence l. 678.
Un `vastai show instance` en échec juste après la création (cas courant pendant le chargement de l'instance) laisse
l'instance louée sans veilleur ni destruction. Sondes `test_D1_taux_horaire_qui_leve_instance_jamais_detruite` et
`test_D1_bis_veilleur_qui_ne_part_pas…` : `detruites == []`. Contraire à la correction 3 (« destruction dans tous les
cas ») et à R10.

**D-2 (bloquant). Le veilleur meurt à la première erreur, et sa mort n'est pas vue.** La l. 364-382 : aucun
`try` dans `boucle` ; une destruction refusée une fois (`vastai destroy` en échec passager) ou un poste illisible
termine le processus, sortie vers `/dev/null` (l. 392-393). La conduite ne vérifie jamais qu'il vit (l. 674-675) ; l'essai
E l. 1316-1324 (« le veilleur reste actif ») suppose ce qui n'est pas garanti : si l'interface de destruction est
indisponible, l'essai de la conduite échoue, puis l'unique essai du veilleur échoue aussi, et rien ne détruit plus
l'instance. Sondes `test_D2_veilleur_meurt_sur_une_destruction_en_echec` (une seule tentative, exception sortie) et
`test_D2_bis_veilleur_mort_au_depart_non_vu` (processus mort, PID rendu quand même).

**D-3 (bloquant). Un seul sondage en échec détruit l'instance en plein run.** `FournisseurVast.executer` appelle
`vastai ssh-url` (`check=True`) à chaque sondage et `subprocess.run(…, timeout=120)` lève `TimeoutExpired` ; `_cmd`
(La l. 610-611) ne les rattrape pas. Sur un run de plusieurs jours sondé chaque minute, une seule erreur passagère du
poste local ou de l'interface fait sortir `conduire` par exception : rapatriement d'une exécution **toujours en cours**
(aucun arrêt par PID avant les empreintes), puis destruction. Le run n'est ni « tronqué » lisible ni relancé. Sonde
`test_D3_un_sondage_qui_leve…` : un `TimeoutExpired` au premier sondage du run principal → instance détruite, aucune
commande `kill -TERM`, pas de relance. Contredit P-f tel que la v3 le déclare (« une coupure du poste local ne tue pas
l'exécution ») et la lecture actée de « B − 2 ».

**D-4 (bloquant). Exécution morte sur l'instance : aucun arrêt local à B − 2 ; lancement jamais vérifié.** (a) Pour une
exécution, la borne locale est la seule échéance − marge/2 (La l. 609) : l'arrêt à B − 2 est laissé au processus de
l'instance. Si ce processus meurt sans écrire `.fin` (coupure de l'hôte, redémarrage du conteneur), la conduite sonde
jusqu'à l'échéance ; en réel, le veilleur détruit **sans transfert** à B − 0,5 : run perdu, budget épuisé, pas de
relance, alors que « coupure de l'hôte » est une erreur nommée qui ouvre une relance (texte l. 371). Sonde
`test_D4_execution_morte…` : arrêt local seulement à la borne d'échéance, D = 239 USD au moment de l'arrêt dans la
sonde (horloge factice d'une heure par lecture, sans veilleur). (b) Le code de retour du lancement détaché est ignoré
(La l. 608) : une commande jamais lancée est sondée jusqu'à la borne. Sonde `test_D4_bis…` : `ssh` refusé au lancement
de la mise en place → D ≈ 74 USD avant l'arrêt.

**D-5 (à corriger). Première connexion.** Aucune attente de l'instance prête : la première opération distante, aussitôt
après `taux_horaire`, est l'envoi de l'archive par `scp` (La l. 681), alors que l'instance charge encore son image ; et
`scp` est appelé sans `-o StrictHostKeyChecking=accept-new` (La l. 112-119), avant tout `ssh` qui aurait accepté la clé
d'hôte : échec « Host key verification failed » ou attente d'une réponse au terminal. Sonde `test_D5_…` (ordre des
appels ; argv de `scp`). Avec D-1, la conduite réelle a de bonnes chances de s'arrêter à sa première commande.

**D-6 (à corriger). L'archive envoyée est le dépôt entier.** La l. 412 : `git archive <commit>` sans chemin. Mesuré sur
`HEAD` : 2 155 559 856 octets compressés ; entrées par dossier : `docs` 13 484, `gemini` 1 564, `diag` 1 198,
`donnees` 83, `registres` 275, … ; `src` n'en a que 224. Tout cela part sur un hôte loué à un tiers (cloisons du
programme : résultats bruts, notes des bras), et le transfert de 2 Go se fait sur le compteur. L'instance n'a besoin que
de `src/` (le module n'importe que `controle_ia`). Sonde `test_D6_archive_du_depot_entier`.

**D-7 (à corriger). Marge de secours et période de la conduite non transmises au veilleur.** La l. 674-675 n'en passe
aucune : le veilleur prend 0,5 USD et 30 s quelle que soit `Conduite.marge_secours`, alors que `verifier_echeance`
(l. 679) emploie celle de la conduite. Sonde `test_D7_…`.

**D-8 (à corriger). K < 20 par la règle rapporté comme « règle non calculée ».** I l. 589-591 imprime l'état avec K,
puis `garde_nombre_de_tours` lève et imprime une seconde ligne `ETAT {garde_tombee}` ; la conduite ne garde que la
dernière (La l. 467, 482-487) : la branche « K < 20 après le pilote : arrêt, devis révisé à Lazar » (La l. 742-744,
texte l. 367) est inatteignable, et l'essai E l. 1277-1281 consacre le mauvais libellé. Le fichier `regle-tours-v3.json`
porte bien K, et `valider` rend le bon verdict ; seul le bilan de la conduite se trompe d'arrêt. Sonde `test_D8_…`.

À préciser (addendum) :
- **P-g.** `t` « sur la première exécution du pilote qui a fini ses tours 0 et 1 » (texte l. 244) est lu comme « lignes
  MARK des tours 0 et 1 imprimées » (La l. 735), sans regarder une garde par tour tombée au tour 1 : à écrire.
- **P-h.** La condition 2 se vérifie **après** la création (c relevé à la création), l'instance étant détruite aussitôt
  si elle échoue (La l. 679, E l. 1366-1371) : une petite dépense est possible sur une condition de lancement manquante ; à
  écrire.
- **P-i.** La ligne GO-2026-11-10-10 n'est pas dans `registres/go.md` de la branche de travail (sonde
  `test_GO_reel_sur_main`) : `texte_go` doit être lu sur `origin/main`, et la garde de `.claude/hooks/garde_calcul.py`
  ne voit toujours pas la création faite par `subprocess` (P-7 de `90af7dea`, inchangé). À écrire dans l'ordre de
  lancement.

Vérifié sans défaut : `verifier_go` sur la ligne réelle (B = 75 lu dans « (B = 75, … », 120 refusé, `fb6c2f34` et
`f9c8c66e` exigés, plafond 120 ≥ 75, aucune révocation) ; `echeance_epoch("2026-11-30")` = 23:59:59 UTC ; `issue_pilote`
et `relance_permise` conformes à la liste d'arrêt (dont « erreur après 20 tours complets : pas de relance ») ; choix de
`t` sur la première exécution qui a fini les tours 0 et 1 ; ce qui sort : seuls `SORTANTS`, la dernière ligne `ETAT` et
`CODE` (les `.log` restent sur l'instance) ; aucune note lue par la conduite ; `valider` : K′ < 20 passe avant la garde
de fin de run, comme le veut la table.

## 3. Lectures de la liste `06ab9268`

| # | Avis | Écart au texte, mot de Lazar ? |
|---|---|---|
| 1, 2, 3 | justes ; conformes au code (sous réserve de D-1 à D-4 pour leur tenue) | actées |
| 4 | juste (3 600 s ; borne locale échéance − 1 800 s) | **oui** (valeur) |
| 5 | juste (plus strict que le texte) | non |
| 6 | juste ; vérifiée sur la ligne réelle | **oui** |
| 7 | **corrigée** : préciser le fuseau ; « 2026-11-30 » lu à 23:59:59 UTC dépasse d'une heure la fin du jour à Paris ; lecture prudente : 22:59:59 UTC, ou fuseau acté | **oui** (fuseau) |
| 8 | juste | **oui** (unité) |
| 9, 10, 11, 12, 13, 14, 15 | justes | non |
| 16 | **corrigée** : lire tout code non nul comme « erreur technique nommée » élargit la l. 371 (liste fermée : mémoire de carte, mémoire vive, valeur non finie, coupure de l'hôte) et la l. 366 à des erreurs non nommées ; le rapport `4f079ece` demandait une liste écrite. C'est une lecture d'une ligne scellée qui décide d'une reprise ou d'une relance | **oui** |
| 17, 18, 19, 20 | justes | non |
| 21 | **corrigée** : « archive `git archive` du commit » doit devenir « archive du seul dossier `src/` du commit » (D-6) | non, après correction |
| 22 | **corrigée** : le risque déclaré est sous-estimé tant que D-3 et D-4 ne sont pas corrigés ; après C3 et C4, la phrase tient | non, après correction |
| 23 | juste (à établir avant l'instance) | non |
| ajouts | P-g, P-h, P-i ci-dessus : à écrire à l'addendum | non |

## 4. Corrections exigées

- **C1 (D-1).** Ouvrir le `try … finally` (La l. 678) **aussitôt après** `creer` : `taux_horaire`, l'écriture du poste,
  `_etape` et le lancement du veilleur à l'intérieur ; si `c` n'a pu être lu, détruire quand même. Essai : S-D1 et
  S-D1-bis → `detruites == ["77"]`.
- **C2 (D-2, D-7).** `Veilleur.boucle` : chaque passage dans un `try` ; erreur écrite au journal ; destruction retentée
  à chaque période jusqu'à ce qu'elle réussisse ; poste illisible → dernier poste lu, ou destruction. La conduite vérifie
  que le veilleur vit (PID vivant et non zombie, ou fichier de battement) avant la première commande, sinon arrêt et
  destruction ; `marge_secours` et la période passées au veilleur. Essais : S-D2, S-D2-bis, S-D7 inversées.
- **C3 (D-3).** Dans `FournisseurVast.executer`, rattraper `TimeoutExpired` et l'échec de `ssh-url` (rendre un code
  non nul) ; dans `_cmd`, tolérer les sondages en échec (borne de temps ou de nombre consécutif déclarée) ; sur toute
  sortie par exception, envoyer `commande_arret` pour la commande en cours **avant** `_rapatrier`. Essai : S-D3 → run
  arrêté par PID, transféré, puis relance ou arrêt selon la liste.
- **C4 (D-4).** À chaque sondage, vérifier que le PID de la commande vit (`kill -0`) ; mort sans `.fin` → état
  « commande distante sans ligne d'état » (coupure de l'hôte), normalisé, qui ouvre la relance selon la liste ; borne
  locale d'une exécution = min(échéance − marge/2, instant où D atteint un seuil local déclaré entre B − 2 et B − 0,5) ;
  après le lancement détaché, vérifier la présence de `<nom>.pid`, sinon un nouvel essai puis arrêt. Essais : S-D4 et
  S-D4-bis inversées.
- **C5 (D-5).** Attendre l'instance prête (état « running » de `vastai show instance` puis un `ssh … true` accepté),
  borné en temps et compté dans D ; `scp` avec `-o StrictHostKeyChecking=accept-new`. Essai : ordre des appels, argv.
- **C6 (D-6).** `git archive <commit> src` (et seuls les fichiers nécessaires) ; essai : l'archive ne contient que
  `src/`.
- **C7 (D-8).** `regle-tours` : la garde « nombre de tours » écrite au même `ETAT` que K (ou la conduite lit K au
  fichier d'état) ; bilan « K < 20 après le pilote : arrêt, devis révisé à Lazar » ; corriger E l. 1277-1281.
- Liste des lectures : appliquer la section 3 (7, 16, 21, 22, ajouts P-g, P-h, P-i).

Après C1 à C7 : contrôle par une relecture des seules lignes touchées et des essais inversés (S-D1 à S-D8) ; puis
addendum, après le mot de Lazar sur les lectures 4, 6, 7, 8 et 16.
