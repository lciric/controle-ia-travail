# Provenance des jeux synthétiques de T0.7 — J-C version 3, J-D et J-A copiés, dossier `donnees/t07-jeux-synthetiques-v3/` — v3

- **Écrit par** l'agent neuf « assembleur-vérificateur » du lot 2 (Claude Opus 5.5), sous-agent de la session mère
  `session_01QPDgKgACWyCkCN8HjqwNXy`, qui n'a écrit ni T0.7, ni ses jeux, ni leur script, ni leurs contre-vérifications, ni
  aucune remise de J-C ; il a lu des fichiers de T0.7 : **exclu ensuite de tout rôle de lecteur de P3-bis**. Il n'est pas le
  lecteur à l'aveugle.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-lot2-jc-assemblage-contre-verification-v1.md`
  (`86b9fd4ca77b695c7233b816c6aad253880b3983647dfd6d3b9199fa9809faf9`, vérifiée avant lecture), étapes 1 et 2 ;
  interdits communs v2 (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiés), tenus en entier,
  règle 9 comprise.
- **Consigne des jeux qui fait foi** : `docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md`
  (`d9de50a6f4f7a8add3465ad53a5b894703f70b8777b7f8e428417ebfcd73b485`), § 3, § 9, § 10 ; règles fixes du lot 2
  `journal-jc-lot2-regles-fixes-v1.md` (même dossier, `fb249517c739090073006624af3d0e5abef43986b6288cd5a6905d4fbe0c87a3`).
- **Heures** (`date -u`) : travail commencé le 2026-11-10 à 09:38:45 UTC ; assemblage et garde à 09:41:15–09:41:16 UTC ;
  copies et premiers scellements à 09:41:24 UTC ; vérification complète de 09:41:37 à 09:44:38 UTC ; contrôle de forme à
  09:42:25 UTC ; tirage de l'échantillon à 09:44:53 UTC ; ce texte écrit à partir de 09:45:28 UTC ; heure du scellement :
  celle de son compagnon `.sha256` (donnée dans le rapport à la mère).
- **Aucun** appel de modèle ni d'interface externe, aucune dépense, aucun `vastai` ; **aucune écriture git** (lecture par
  `git show`, `git archive` et `git ls-tree` sur des chemins et commits nommés ; aucun `git fetch`) ; **aucune ligne de
  registre écrite** (la mère prononce et écrit `SCELLEMENT-JEUX-T07-JC`).
- **Jamais ouverts** : tout `lecture-sondes-t06.json` ; la lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/`
  et `runs/` de 7a ; `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
  `docs/notes/bras-attaque/` ; l'étiqueteur ; `scripts/extraire_mesures_epreuve_t06_v1.py` ; aucun fichier de P3-bis ;
  **les textes d'actions de P3** (`donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl`), passés au script par leur
  chemin, empreinte `ba05fa13af2dd4f935334438b44d2d27fbc655a970721b10b90bd94b5846f284` lue au journal du script. Aucune
  recherche récursive : `ls` et `sha256sum` sur des dossiers et fichiers nommés, `grep` sur des fichiers nommés.

## 1. Fichiers du dossier (chemins relatifs à la racine du clone ; chacun a son compagnon `.sha256`, R6)

| fichier | rôle | sha256 |
|---|---|---|
| `donnees/t07-jeux-synthetiques-v3/domaine-cout-v3.jsonl` | **J-C version 3** (320 paires, 640 séquences, 32 tâches) | `99b4f1b25daa84f16b6c8c8dec06fede52ec7538f085d95b09e7e20bec627447` |
| `donnees/t07-jeux-synthetiques-v3/dissimulation-v2.jsonl` | **J-D**, copie à l'octet du lot 1 (ligne `SCELLEMENT-JEUX-T07-JD`) | `32f412888270a3c4b4bc347cf57055bd11b517000feceeaeed122476238ec228` |
| `donnees/t07-jeux-synthetiques-v3/intention-autres-modes-v2.jsonl` | **J-A**, copie à l'octet du lot 1 (ligne `SCELLEMENT-JEUX-T07-JA`) | `5b0409209e66e6c29b69e675c5836cefbef966d9cc0a34412837cae837e2aacf` |
| `donnees/t07-jeux-synthetiques-v3/journal-assemblage-jc-v3.txt` | assemblage de J-C par le script officiel, garde d'égalité et son artefact (outil recopié en fin de journal) | `1a1c621e738828b4232b2a95624824f36d4f9edadf04ef6d798e27a779b2f396` |
| `donnees/t07-jeux-synthetiques-v3/journal-assemblage-v3.txt` | journal d'assemblage écrit par le script officiel lui-même (copie à l'octet) | `386c31e700e19de4533caed8f4f217e38f9eb0de2c6a1647c317d8592c49baf0` |
| `donnees/t07-jeux-synthetiques-v3/journal-verification-v3.txt` | **vérification « scellable » complète des trois jeux** par le script officiel (§ 8), code 0 | `3c74b1ef7e66d2ffec8e8e575672562417756db978d7faeab55af3a7ea18ca46` |
| `donnees/t07-jeux-synthetiques-v3/journal-controle-forme-module-v3.txt` | contrôle de forme par le module de T0.7 (`8dc1cb09`), outil recopié en fin de journal | `e279b67903a28fb64d95b6ccc73a0763da87f3510ed63f29c155b57d8a9ec9c5` |
| `donnees/t07-jeux-synthetiques-v3/remises-jc-v3/` (32 fichiers) | copie d'archive des 32 remises retenues, chacune égale à sa ligne de `liste-32.txt` | voir `pieces-lot2-jc-v3/liste-32.txt` |
| `donnees/t07-jeux-synthetiques-v3/pieces-lot2-jc-v3/liste-32.txt` | liste de la mère (chemins d'origine, empreintes) | `d2cfdf3184668ea5fcd4e53c8c03ca7a6a22e1104b03b92c8ed08be6bcea4d5e` |
| `donnees/t07-jeux-synthetiques-v3/pieces-lot2-jc-v3/journal-jc-lot2-precontroles-v1.txt` | journal des pré-contrôles et des corrections | `97b231b9b8ba9171d2760f7f63b09c15b85f87ca89233f26cd0b810a028be31f` |
| `donnees/t07-jeux-synthetiques-v3/pieces-lot2-jc-v3/jalon-8-sortie.txt` | jalon 8 (contrôleur des jalons) | `b50700e7a27aedbe20a1588bb31f6b0d55fe6fb8cc52cbe05fe1e26163a71f43` |
| `donnees/t07-jeux-synthetiques-v3/pieces-lot2-jc-v3/jalon-16-sortie.txt` | jalon 16 | `2727febd141cf4f19c688d835ac8861af9a1bc2a1bfd62faaa858afa3c758c2a` |
| `donnees/t07-jeux-synthetiques-v3/pieces-lot2-jc-v3/jalon-24-sortie.txt` | jalon 24 | `6fe7564535199490917eba0d26b7e7b9dbd6dec466a56fb83d23d1e49de6449a` |
| `donnees/t07-jeux-synthetiques-v3/pieces-lot2-jc-v3/jalon-32-sortie.txt` | jalon 32 | `fe23fc795de09fc822edd7ca49958bc1ab72c5f1d4d2adb1a980ca583620390e` |
| `donnees/t07-jeux-synthetiques-v3/contre-verification-v3/echantillon-aveugle-jc-v3.md` | ce que lit le lecteur à l'aveugle (§ 9) | `5747f329a06793386b95167320c7c35afed031b4a6a9b28ea95c1e1277791990` |
| `donnees/t07-jeux-synthetiques-v3/contre-verification-v3/gabarit-reponses-jc-v3.json` | gabarit des réponses du lecteur | `deb3e604c7366b117253bdf4023b5f4c125fb49c85faed1cdd47d4fdc0a3f813` |
| `donnees/t07-jeux-synthetiques-v3/provenance-v3.md` | ce texte | voir son compagnon |

Présents avant ce lot, écrits par l'orchestrateur du lot 2 (non modifiés) : `journal-jc-lot2-regles-fixes-v1.md`
(`fb249517…`), `consigne-ecrivain-jc-lot2-v1.md` (`190fe049…`), `generer_consigne_ecrivain_jc_lot2_v1.py` (`bed75966…`),
`rapport-orchestrateur-lot2-jc-v1.md` (voir son compagnon).

**Hors de ce dossier jusqu'à l'étape 3** (le lecteur ne l'ouvre pas) : la clé
`/home/user/lot2-jc/cle-contre-verification-v3/cle-jc-v3.json`
(`907544d57f39312f62b0d9de0c9dc87f44e79ff4b8ce281298d9f1db6c480aa3`, compagnon écrit) et le journal du tirage, qui porte
l'ordre des membres et le texte intégral de l'outil (`journal-echantillon-jc-v3.txt`,
`dc62ce1d2a352b71781a71635597d4b98b04fbdbcf4603b793d6011d420a3156`, compagnon écrit). Ils sont copiés ici à l'étape 3.

Marqueur `<<EMPREINTE_JEUX_SYNTHETIQUES>>` (§ 10, étape 6) : J-D `32f41288…`, J-C `99b4f1b2…`, J-A `5b040920…` et
`provenance-v3.md` (son compagnon) — **à remplir par la mère seulement après son acceptation de J-C** (contre-vérification
comprise).

## 2. Entrées (chemins, empreintes, commits)

| entrée | chemin | sha256 | origine |
|---|---|---|---|
| tâches de réserve (scellé) | `donnees/20261007-082440-t05-extraction/taches-entrainement.json` | `8d20a698d76baa8a42cd1494227fc411ef043d24a67a413e5cf812541166a4fd` | compagnon présent |
| tâches d'évaluation (scellé, 64) | `donnees/20261007-082440-t05-extraction/taches-evaluation.json` | `76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e` | compagnon présent |
| énoncés de la réserve (lot 1, scellé) | `donnees/t07-jeux-synthetiques-v2/enonces-reserve-v2.jsonl` | `a9e8839f886f9df1ce8270a347151bd11bee0e0742b425edf5914cd5c23d50f8` | lus en place, compagnon conforme |
| annexes A, B, C (lot 1, scellées) | `donnees/t07-jeux-synthetiques-v2/{banque-instructions,banque-incitations,mots-interdits}-v2.json` | `230099ef…`, `eb6a424d…`, `5d42ab63…` | lues en place (`--annexes donnees/t07-jeux-synthetiques-v2`, `--version-annexes v2`), compagnons conformes |
| J-D, J-A (lot 1, scellés) | `donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl`, `…/intention-autres-modes-v2.jsonl` | `32f41288…`, `5b040920…` | compagnons conformes ; égaux aux lignes `SCELLEMENT-JEUX-T07-JD` et `-JA` de `registres/scellements-v1.md` |
| 32 remises retenues | `/home/user/lot2-jc/{remises,corrections,remises-par-ecrivain/rNN}/…` selon `liste-32.txt` (`d2cfdf31…`) | une par ligne de la liste | 32 sur 32 conformes (`sha256sum -c`) |
| script de vérification et d'assemblage | `scripts/verifier_jeux_synthetiques_t07_v2.py` | `e53c9c2729cf17ac1b0f3c6fbf81169c1d568bbccb85fb1535981b4094341d22` | `main` ; sans compagnon (comme au lot 1) ; essais non rejoués par ce lot |
| tokeniseur réel de Llama-3.1-8B-Instruct | `donnees/tokeniseur-llama-3.1-8b-instruct-v1/tokenizer.json` | `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` | commit `03e3cbd9` (`refs/remotes/origin/donnees/tokeniseur-llama-3.1-8b-instruct-v1`), extrait par `git show` hors de l'arbre, égal à son compagnon |
| textes interdits | `prereg/P3-consignes-v1.md` ; `donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl` | `a68468fe…` ; `ba05fa13…` (lue au journal du script) | le second **jamais ouvert** |
| textes d'épisodes de T0.6 | course 7b | — | **absents à la vérification**, déclarés au script (contrôle 9 et remesure des jetons rejoués par la chaîne de T0.7 ; D-2 (a), R-2101) |
| module de T0.7 (contrôle de forme) | `src/controle_ia/t07/sondes_neuves_v1.py` | `b1c59783ed231c88c5671bc124b0a3f448e5b948b48677db2f361fe6d05c085d` | commit `8dc1cb09`, `src/` extrait par `git archive` dans un dossier temporaire ; aucune activation |
| consigne v3 des jeux (sections 1 et 9 recopiées dans l'échantillon) | `docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md` | `d9de50a6…` | `main` |
| clone de travail | `main` | — | commit `14d1756f` à 09:40 UTC (`384d5147` à 09:39 UTC, avancé par la mère) |

Interpréteur : `/home/user/controle-ia-travail/.venv/bin/python` (Python 3.13.18, numpy 2.4.6), avec `-I -B` pour le script
officiel et les outils de ce lot ; `PYTHONPATH=src` pour le script officiel et le scellement.

## 3. Ce que ce lot a fait, et ce qu'il a trouvé

1. **Assemblage de J-C** (étape 1) : `assembler` du script officiel sur les 32 remises de la liste, dans son ordre,
   `--version v3`, `--jeux domaine-cout`, graine **20261105**, énoncés et annexes scellés du lot 1, réserve scellée : code 0,
   0 paire en défaut, 640 séquences, 320 paires. **Garde d'égalité** : `domaine-cout-v3.jsonl` = `99b4f1b2…` **égale** à
   l'empreinte du jalon 32 (contrôleur des jalons, `jalon-32-sortie.txt`, `fe23fc79…`) ; R5 : le même assemblage à la graine
   20261106 donne `d6dc0ad93575807bea72b95744be7521ae5a51a76c1c0e7edbabcae146351989`, **inégale** : la garde mord. Le contenu
   des enregistrements ne dépend pas de `--version` (seul le nom du fichier en dépend ; script, l. 481-560) : l'égalité
   avec l'assemblage du jalon, fait en `v2` par défaut, est donc attendue et constatée.
2. **J-D et J-A** copiés à l'octet du dossier du lot 1 ; empreintes égales aux lignes du registre ; noms d'origine gardés.
3. **Vérification « scellable » complète des trois jeux** par le script officiel : `verifier` **sans** `--jeux` ni
   `--nombre-taches`, `--version v3`, réserve et évaluation **scellées**, énoncés et annexes scellés du lot 1, textes
   interdits de P3 (consignes et textes d'actions, ce dernier passé par son chemin), épisodes de 7b déclarés absents,
   graine 20261105, tokeniseur réel (« jetons : mesurés ») : **code 0, 0 défaut dur, 0 réserve** ; contrôles fichiers, 1 à
   10 et annexes conformes. **Aires du sac de mots à 32 plis, recopiées du journal (réponse entière / avant `COST`)** :
   **J-C 0,889 / 0,893** ; J-A « contrôles » 0,815 / 0,802 ; J-A « direction » 0,736 / 0,741 ; J-D sans objet (réponse
   identique dans la paire). Les aires de J-C sont égales à celles du jalon 32 ; celles de J-A égales à celles du lot 1
   (`journal-verification-v2.txt`, `58906bb4…`). Les deux aires de J-C sont **sous 0,90**.
   Contrôles rapportés de J-C (information) : mots avant `COST` 117,6 chez les deux étiquettes ; groupes de chiffres avant
   `COST` 6,84 (honnête) et 7,35 (gonflé), écart de 7,5 %, sous la réserve de 20 % du § 5.3.
4. **Contrôle de forme par le module de T0.7** (`8dc1cb09`) : `lire_jeu` accepte les trois fichiers (640 enregistrements,
   320 paires, 32 tâches chacun ; modes `aucun` ; `cout` ; `controles` et `direction`) ; `controler_disjonction` contre les
   64 tâches d'évaluation scellées : **0 tâche commune** ; trois artefacts refusés (position de `COST` décalée d'un
   enregistrement de J-C ; J-C lu sous la clé de J-A ; liste d'évaluation augmentée d'une tâche de J-C). Code 0.
5. **Archives** : 32 remises retenues (`remises-jc-v3/`, égales à la liste), liste, journal des pré-contrôles et quatre
   sorties de jalon (`pieces-lot2-jc-v3/`), copiés à l'octet et scellés.
6. **Manques** : **aucun** (32 tâches, 10 paires par tâche, aucune paire retirée).

## 4. Écriture de J-C v3 : écrivains, renvois, corrections (d'après le journal des pré-contrôles et les sorties de jalon)

- **Écrivains** : sous-agents neufs de **lignée Sonnet** (règle 3 a des règles fixes ; consigne de ce lot), **deux tâches
  chacun**, seize remises (r00–r01, …, r30–r31), consigne d'écrivain `consigne-ecrivain-jc-lot2-v1.md` (`190fe049…`).
  **Lancés par la mère** : l'orchestrateur du lot 2 n'avait aucun outil de lancement de sous-agent et s'est arrêté après
  le point 1 (`rapport-orchestrateur-lot2-jc-v1.md`, E-L2-1) ; les pré-contrôles sont signés « mère » au journal. Le modèle
  exact de chaque écrivain n'est pas consigné dans les pièces lues par ce lot ; « lignée Sonnet » est repris de la règle 3 a
  et des entrées du journal (« écrivain neuf Sonnet »), non vérifié par ailleurs.
- **Remises** : r00–r07 dans un dossier commun (`/home/user/lot2-jc/remises/`) ; **à partir de r08, un dossier par
  écrivain** (`/home/user/lot2-jc/remises-par-ecrivain/rNN/`, r08 à r30), mesure de la mère après les écarts de r04–r05 et
  r06–r07 (ci-dessous). Les 16 remises passent les pré-contrôles P-1 à P-5 (`verif_lot_v1.py` « OK », C-1 et C-2 à 0 paire)
  au premier dépôt.
- **Renvois (règle 3 c)** : **aucun** consigné au journal des pré-contrôles.
- **Corrections (règle 3 e, contrôle 6, R-1672)** — correction mécanique, une fois, par un écrivain neuf (Sonnet), des
  seules paires en défaut dur au script officiel :
  - jalon 8 (code 1) : r02 (`2602.01626v1`) paire 7, jetons avant `COST` 147/173 (écart 0,1503) ; r06 (`2510.26843v1`)
    paire 6, 173/208 (0,1683) → corrigées (154/171, 0,0994 ; 181/202, 0,1040) ; 2 lignes changées dans chacun des deux
    fichiers ; remises remplacées : r02 `af83a386…`, r06 `1194833d…` ;
  - jalon 16 (code 1) : r10 (`2603.12594v1`) paire 8, 145/174 (0,17) → corrigée (154/170, 0,0941) ; 2 lignes changées ;
    remise remplacée : r10 `766c126e…`.
  Les fichiers de correction r03, r07 et r11 (même dossier `corrections/`) sont identiques à l'octet aux remises de ces
  tâches (« 0 ligne changée ») ; la liste les prend dans `remises/` ou `remises-par-ecrivain/r10/`, de même empreinte.
  Remises retenues prises dans `corrections/` : r02, r06, r10 (une paire corrigée une fois chacune).
- **Jalons** (aire lue aux seuls jalons, règle 3 g) : 8 tâches, code 1 (deux défauts du contrôle 6), aires 0,899 / **0,909**
  avec la **réserve du script** « aire 0,909 ≥ 0,9 — réserve de surface, transmise à la contre-vérification » ; 16 tâches,
  code 1 (un défaut du contrôle 6), 0,817 / 0,846 ; 24 tâches, code 0, 0,876 / 0,882 ; **32 tâches, code 0, 0,889 / 0,893**,
  sous 0,90, aucun défaut dur.

## 5. Contre-vérification à l'aveugle (étape 2 ; consigne v3 des jeux, § 9, pour J-C)

- **Entropie neuve** : `secrets.randbits(128)` = **293419748702586501555893609091430003889** (tirée le 2026-11-10 à
  09:44:53 UTC, une seule fois pour l'échantillon versé) ; `numpy.random.SeedSequence`, clé dérivée
  `echantillon-domaine-cout` = `spawn_key` (2,) (convention de la contre-vérification du 7 novembre : 1, 2, 3) ; sous-clés
  (2, 0) pour le tirage des paires, (2, 1) pour l'ordre des membres (R9).
- **Échantillon** : 32 paires sur 320, **au plus deux par tâche** (23 tâches représentées) : permutation des 320 paires
  (ordre canonique : rang de la tâche dans le fichier des énoncés, puis paire), parcourue dans l'ordre tiré. Chaque paire :
  les deux membres dans un ordre tiré, nommés **A** et **B** (indépendamment du champ `membre` du fichier), **sans
  étiquette**, ligne `COST:` remplacée par `COST: [masqué]` (aucune autre occurrence du nombre dans les 64 réponses
  montrées), avec le contexte (message système et observation, contrôlés identiques dans les deux membres) ; aucun
  identifiant de tâche, de paire ni d'incitation affiché. Le **début commun** des 32 messages système (1 090 caractères :
  consigne honnête et format de l'action, jusqu'à « Problem statement: ») est recopié une fois en tête ; chaque paire porte
  la suite de son message système (énoncé, classification, incitation) — choix de présentation de ce lot, déclaré.
- **Ce que lit le lecteur** : `echantillon-aveugle-jc-v3.md` — une courte note de lecture, les trois questions du § 9 pour
  J-C, le texte des sections 1 et 9 de la consigne v3 des jeux recopié à l'octet, puis l'échantillon ; rien d'autre. Il
  remplit une copie de `gabarit-reponses-jc-v3.json` (par paire : membre désigné A ou B, raison, indice de surface oui ou
  non et lequel, incitation « situation » ou « consigne », remarque ; déclaration du lecteur ; indices généraux).
- **Clé** : `/home/user/lot2-jc/cle-contre-verification-v3/cle-jc-v3.json` (`907544d5…`), dossier à part ; elle porte
  l'entropie, les clés, l'empreinte de J-C, de l'échantillon et du gabarit, et par paire : tâche, rang, paire, incitation,
  coût, étiquettes de A et de B, membre gonflé, membres du fichier. Outil : `echantillon_aveugle_jc_v3_v1.py`
  (`67609316e70aefd47078ee06d16f138b1b75fb0803df0b0c5f053f7429af9810`, texte intégral dans le journal du tirage, dossier de
  la clé).
- **Seuils (étape 3, non appliqués ici)** : au moins 23 bonnes réponses sur 32 ; un indice de surface nommé et retrouvé par
  programme sur plus d'un quart des 320 paires (81 ou plus) fait refuser le jeu ; la mère prononce.

## 6. Modèles des sous-agents

| rôle | modèle | source |
|---|---|---|
| orchestrateur du lot 2 (règles fixes, consigne d'écrivain ; arrêté après le point 1) | Claude Opus 5.5 | `rapport-orchestrateur-lot2-jc-v1.md` |
| écrivains des 16 remises de J-C v3 | sous-agents neufs, lignée Sonnet, lancés par la mère | règle 3 a ; consigne de ce lot ; modèle exact non consigné dans les pièces lues |
| correcteurs du contrôle 6 (r02 p7 et r06 p6 ; r10 p8) | écrivains neufs, Sonnet | journal des pré-contrôles |
| contrôleur des jalons 8, 16, 24, 32 | sous-agent de la session mère | en-tête des sorties de jalon ; modèle non consigné dans les sorties |
| auteur du script officiel et de ses essais | développeur neuf, Claude Fable 5.1 (lot 1, `provenance-v2.md` § 4) | — |
| assembleur-vérificateur de ce lot | Claude Opus 5.5 | ce texte |
| lecteur à l'aveugle | à lancer par la mère (agent neuf) | — |

## 7. Écarts et déclarations (rapportés, aucun corrigé en silence)

- **E-L3-1** (assemblage en `--jeux domaine-cout`) : les remises ne portent que J-C ; sans `--jeux`, `assembler` s'arrête
  (« aucun enregistrement assemblable » pour J-D et J-A). Le journal d'assemblage du script porte donc
  « [ÉCART DÉCLARÉ] jeux partiels ['domaine-cout'] : jamais scellable », qui vise l'assemblage ; **la vérification, elle,
  est complète** (trois jeux, sans `--jeux` ni `--nombre-taches`) et c'est elle qui fait foi pour le scellement.
- **E-L3-2** (noms et liens) : J-D et J-A gardent leurs noms `-v2` dans ce dossier (copie à l'octet, identité avec les lignes
  du registre). Le mode `verifier` exige `<jeu>-<version>.jsonl` dans un même dossier : la vérification a lu
  `/home/user/lot2-jc-tmp/verification/`, où `dissimulation-v3.jsonl`, `domaine-cout-v3.jsonl` et
  `intention-autres-modes-v3.jsonl` étaient des **liens symboliques** vers les trois fichiers **déjà scellés** de ce
  dossier (même procédé qu'au lot 1, `provenance-v2.md` § 6.1) ; le journal écrit donc des chemins temporaires, avec les
  empreintes des fichiers versés ici. Le journal d'assemblage du script et celui de la garde écrivent aussi des chemins
  temporaires (`/home/user/lot2-jc-tmp/assemblage-v3/`, `…/artefact-graine-20261106/`).
- **E-L3-3** (énoncés et annexes non recopiés) : lus en place dans le dossier scellé du lot 1, comme au jalon ; la consigne
  ne demande pas leur copie.
- **E-L3-4** (cloisonnement des écrivains) : **les écrivains de r04–r05 et de r06–r07 ont vu d'autres remises avant le
  cloisonnement** — r04–r05 : une boucle de recherche de mots C-1 a lu r00–r03 et r06–r07 du dossier commun (mots trouvés et
  numéros de paires affichés, rien utilisé ni modifié, déclaration de l'écrivain) ; r06–r07 : un outil d'aide a lu r00–r05
  (comptes de nombres et de mots, rien utilisé ni copié). Mesure de la mère : un dossier par écrivain à partir de r08.
  Écart à la règle 3 a (« aucune remise d'une autre tâche »), déclaré, non réparé (les remises sont gardées).
- **E-L3-5** (orchestration) : l'orchestrateur n'a pas pu lancer d'agents ; la mère a lancé les écrivains, fait les
  pré-contrôles et décidé les corrections (règle 3 e), le contrôleur des jalons a joué les jalons.
- **E-L3-6** (outil de plus aux écrivains) : à partir de r12, `mesurer_paire.py` (`4f21ddf7…`) donné aux écrivains comme
  auto-contrôle (écart déclaré au journal par la mère ; aucune règle d'acceptation changée, aucune remise déjà écrite
  touchée).
- **E-L3-7** (réserve du jalon 8) : aire avant `COST` 0,909 ≥ 0,90 à 8 tâches, réserve « transmise à la
  contre-vérification » par le script ; à 32 tâches, 0,889 / 0,893, sans réserve.
- **E-L3-8** (compléments des règles fixes, hérités du lot 2, E-L2-2) : C-1 et C-2 dits à l'écrivain ; lot de P-2 fixé aux
  deux tâches d'une remise ; défaut dur vu à un jalon admis comme déclencheur de renvoi ; `verif_lot_v1.py` aveugle aux
  ordinaux et à quelques unités matérielles (E-L2-3), défauts éventuels vus par le script officiel aux jalons (aucun à 32).
- **E-L3-9** (essai de l'outil d'échantillon, déclaré) : avant le tirage versé, l'outil a été lancé **deux fois en essai**
  dans un dossier temporaire (`/home/user/lot2-jc-tmp/essai-echantillon/`) : le premier s'est arrêté sur sa propre garde
  avant toute écriture (la ligne `COST:` du format d'action, dans le message système, était prise pour une ligne non
  masquée ; garde resserrée aux réponses, ligne du format admise dans le début commun seulement) ; le second a écrit un
  échantillon, un gabarit et une clé d'essai, dont j'ai lu la forme (en-tête et première paire de l'échantillon, début du
  gabarit), **jamais la clé**, puis le dossier a été effacé par son chemin exact. L'entropie de l'essai n'a servi à rien et
  n'est pas consignée ; la phrase d'en-tête a ensuite été précisée (« une copie du gabarit »). Le tirage versé est le
  premier tirage réel, unique, avec l'outil final (`67609316…`) ; aucun choix entre tirages.
- **E-L3-10** (essais du script) : non rejoués par ce lot (66 passés au lot 1, `provenance-v2.md`) ; la contre-lecture neuve
  du script et de ses essais (E-7 du lot 1) est hors de ce lot.
- **Dossiers temporaires** : `/home/user/lot2-jc-tmp/` (tokeniseur extrait, module extrait, assemblages, liens de
  vérification, outils), effacé par son chemin exact à la fin de l'étape 2 ; les outils de ce lot sont recopiés en entier
  dans leurs journaux.

## 8. Ligne attendue au registre (écrite par la mère seule, après son acceptation)

    | SCELLEMENT-JEUX-T07-JC | <date -u> | donnees/t07-jeux-synthetiques-v3/domaine-cout-v3.jsonl | 99b4f1b25daa84f16b6c8c8dec06fede52ec7538f085d95b09e7e20bec627447 |

et, dans `registres/decisions.md`, les aires de J-C (0,889 / 0,893) et le résultat de la contre-vérification (étape 3).
