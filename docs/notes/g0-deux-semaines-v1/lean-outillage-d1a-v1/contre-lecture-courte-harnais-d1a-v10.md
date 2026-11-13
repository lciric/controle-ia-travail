# Essai Lean, D-1a — contre-lecture courte du harnais v10 (vérificateur du noyau v5 et v6, procédure du poste v11)

- **Lecteur** : sous-agent neuf, modèle **Claude Fable 5.2** (identifiant exact `claude-fable-5-2`), autre modèle que le
  développeur (Claude Opus 5.5) ; n'a écrit ni le harnais, ni le vérificateur, ni la procédure.
- **Objet** : branche `prep/lean-outillage-d1a-v10`, tête `ae894d8df2a19f51e532ff667160ae7bba2bf6ac`, depuis `b0b8667a`
  (R-2439, R-2470, R-2486). Code : commit `5103a7f300523831361303d9bc56d6658546165d`.
- **Heures** (relevées par `date -u`) : début 2026-11-13T03:11:46Z ; écriture de ce fichier 2026-11-13T03:20:36Z.
- **Méthode** : lecture du code, des différences et des journaux ; lecture des sources de la chaîne épinglée déjà sur disque
  (Lean 4.35.0, `src/lean/Lean/…`, installée par le développeur dans son bac à sable) ; recalcul d'empreintes et de comptes
  par de petits scripts Python. **Aucun passage Lean** (interdit par la consigne) : tout ce qui touche au comportement de
  Lean à l'exécution est lu dans les sources et dans les journaux du développeur, jamais rejoué par moi.
- **Interdits** : `interdits-communs-v2.md` lu en entier et appliqué ; aucune écriture git, aucun appel externe, aucune
  clé lue, aucun refus rencontré.

## Verdict (une ligne)

**Utilisable après corrections** : aucune garde du noyau n'est affaiblie par le portage ; trois corrections exigées, toutes
sans code Lean neuf (deux portent sur le texte de la consigne v3 du poste, une sur ce que prouvent les mutations).

## Réponses aux six questions

### 1. Le portage vers Lean 4.35.0 affaiblit-il une garde du noyau ? Non, sous une condition tenue par le code.

Fichiers : `verificateur_noyau_v5.lean` (`9ee1fed0…`, empreinte recalculée égale à la compagne), différence contre la v4
lue ligne à ligne ; sources de la chaîne lues : `Lean/Replay.lean`, `Lean/Environment.lean` (l. 690-715, 1859-1919,
2420-2442), `Lean/Util/CollectAxioms.lean`, `Lean/Elab/Import.lean` (l. 28-40), `Lean/Setup.lean` (l. 25-34),
`Lean/AddDecl.lean` (l. 111-159).

- **`collectAxioms`, `Options.set`, `unsafe enableInitializersExecution`** : changements d'interface seuls. `axiomesDe`
  appelle `Lean.collectAxioms` dans une monade d'état sur l'environnement ; même sortie.
- **`loadExts := true`** : charge les extensions des seuls modules importés (`Init`, `Mathlib`). Le module de l'agent
  n'est jamais importé ; ses entrées d'extension (notations, attributs, simprocs) ne sont jamais chargées. Pas
  d'affaiblissement. **Fait neuf à savoir** : sous 4.35.0, `collectAxioms` lit les axiomes des constantes **importées**
  dans des entrées précalculées des `.olean` de Mathlib (`exportedAxiomsExt`, `CollectAxioms.lean` l. 100-150) au lieu
  de parcourir leurs corps ; pour les constantes de l'agent (non importées, ajoutées par `addDeclCore`), il parcourt les
  corps. La confiance placée dans les `.olean` de Mathlib (jamais rejoués, montés en lecture seule) existait déjà ; elle
  couvre maintenant aussi leur table d'axiomes. Journal : `gl3_axiome_v1`, `gl2_sorry_v1`, `gl2_native_decide_v1` sont
  bien vus par le noyau (« dépend de : triche », « sorryAx », axiome `…native_decide.ax_1_1`).
- **`Kernel.Environment.replay`** (`Replay.lean` l. 176-193) : c'est le même rejeu que celui que l'ancien
  `Environment.replay` appelait (l. 194-197 : il ne fait que l'emballer). Il décide seul de la ligne `rejeu` (G-L8).
  Deux particularités de 4.35.0, lues dans la source, sans effet sur la garde : (a) un théorème du module de même nom,
  même type et mêmes paramètres qu'un théorème **déjà dans l'environnement importé** est ignoré sans contrôle de sa
  preuve (l. 85-96) — `ajouterAcceptee` l'ignore aussi (`(← get).1.contains n`), l'environnement garde donc le théorème
  de Mathlib, et les noms attendus (`etape_k`, `enonce_item`) ne sont pas dans Mathlib ; (b) une constante `quot` du
  module fait échouer le rejeu (`Quot` existe déjà) : refus, du côté prudent.
- **`ajouterAcceptee` (ajout par `addDeclCore … (doCheck := false)`, sans second contrôle) : sûr**, pour quatre raisons
  lues dans le code :
  1. il n'est atteint que si `env.toKernelEnv.replay nouvelles` n'a levé aucune exception : les deux appels sont dans le
     même `try`, dans cet ordre (v6 l. 175-184) ; un échec de l'ajout lui-même rend `rejeu ok = false` (prudent) ;
  2. il ajoute les **mêmes** `ConstantInfo` (même table `nouvelles`) que celles que le rejeu vient de faire contrôler par
     le noyau, avec la même exclusion des non sûres et partielles (`Replay.lean` l. 179-182) ;
  3. la ligne `rejeu` ne dépend pas de lui ; il ne sert qu'à l'impression, à l'aller-retour et aux axiomes ;
  4. constructeurs et récurseurs ne sont jamais ajoutés tels que le fichier de l'agent les donne : ils sont régénérés
     par le noyau à partir du bloc inductif.
  Les deux artefacts qui éprouvent précisément « constante entrée sans le noyau » sont refusés et nommés par le rejeu
  dans le journal hors machine (`noyau_simproc_hors_noyau_v5.lean` : « while replaying declaration
  'etape_1._hors_noyau' … declaration type mismatch » ; `noyau_run_cmd_hors_noyau_v3.lean` : `faux_lemme`), dans les
  deux passages.
  **Limites que je déclare** : (i) que le noyau contrôle toujours un bloc inductif même avec `doCheck := false` est mon
  souvenir du code C++ du noyau (`lean_add_decl_without_checking`), non vérifié ici (source C++ absente du disque) ;
  cela ne change pas la conclusion, le bloc ajouté étant celui que le rejeu a accepté ; (ii) écart théorique : pour un
  bloc inductif mutuel dont les membres porteraient des champs `all`, `numParams` ou `levelParams` incohérents entre
  eux (fichier `.olean` fabriqué à la main), le rejeu et `ajouterAcceptee` peuvent déclarer le bloc à partir de membres
  différents (ordres de parcours différents). Les types et constructeurs déclarés restent les mêmes, l'énoncé final ne
  peut citer aucune constante de l'agent (G-L5, CLC3-06), et les preuves ont été contrôlées par le rejeu : je n'y vois
  pas de chemin d'attaque ; voir suggestion S3.
- **En-tête d'imports exact** : `permis` exige l'égalité, drapeaux compris, avec `#[Init, Init meta, Mathlib]`
  (`Import` dérive `BEq`, `Setup.lean` l. 25-34). Plus strict que la v4 (qui, sous 4.35.0, n'aurait jamais rien permis :
  trois imports). Le cas `prelude` sans import reste refusé (journal). **Cas que j'ai cherché** : un fichier du système
  de modules (`module` puis `public import Mathlib`) produit exactement le même tableau d'imports (`Import.lean`
  l. 28-40) et passe donc `permis`. Il reste refusé : son `.olean` exporté porte les théorèmes comme axiomes
  (`AddDecl.lean` l. 114-116), d'où G-L2, G-L3, G-L4 ; le développeur l'a prévu et éprouvé hors machine
  (`tests/test_lean_essai_verificateur_v6.py`, `test_entetes_de_lean_4_35_hors_r5`). Ce cas n'est pas dans les
  artefacts joués sur la machine : suggestion S4.

### 2. L'option d'impression de la v6 est-elle le seul changement, et masque-t-elle quelque chose ? Oui ; non.

- `diff verificateur_noyau_v5.lean verificateur_noyau_v6.lean` : le commentaire d'en-tête et **une** ligne de code
  (`optionsImpression` reçoit `|>.setBool `pp.mathlib.binderPredicates false`). Empreinte `3ef23bfa…` recalculée, égale à
  la compagne, à R-2486 et au journal hors machine. Exécuteur et épreuve v6 : seuls changent le nom du vérificateur, le
  nom de version et, pour l'épreuve, `attendus-v5.json` (différences lues).
- L'option rend l'impression **plus explicite** (`∀ (x : ℝ), x < 0 → 0 < x → x ^ 2 < 0` au lieu de `∀ x < 0, …`) ;
  l'aller-retour, la détection de troncature, de métavariables et de messages restent appliqués au texte imprimé ;
  l'impression explicite (`pp.all`) n'est pas touchée. Rien n'est masqué : avant, le texte ambigu était refusé à tort
  (côté prudent) ; maintenant le relecteur voit le type et les hypothèses contradictoires (G-L5, journal `gl5_vacuite_v1`).
- Deux remarques : l'option est posée par son nom sans contrôle d'existence (une faute de frappe serait muette), mais
  l'essai `test_v6_vacuite_et_simproc_v5` exige le texte exact et la mutation k13 (option retirée) est tuée par le jeu
  complet (524 s) ; d'autres formes abrégées (par exemple `∃ x > 0, …` imprimé par Lean lui-même) peuvent encore être
  refusées à tort par l'aller-retour : côté prudent, à surveiller sur les vrais items.

### 3. L'essai R5 « le vérificateur compile sur la machine » arrête-t-il avant la coupure, cas sain et copie cassée ? Oui.

- `piloter_poste_v10.sh` : l'essai est la dernière commande de la phase « avant » (l. 71), sous `set -euo pipefail`, par
  `ssh … timeout 900 bash …` ; un code non nul (1 non conforme, 124 délai) arrête le pilote. La coupure
  (`couper_reseau_v1.sh`) n'est que dans la phase « apres » (l. 75), lancement distinct. La procédure v11, section 3,
  dit : code non nul, « ni coupure, ni pilote "apres" ».
- `essai_compilation_verificateur_v1.sh` : cas sain = code 0 **et** sortie vide (sorties standard et d'erreur
  confondues : tout avertissement arrête) ; artefact = même fichier plus une ligne à identifiant inconnu, code non nul
  et `error` exigés ; `lean --version` en échec arrête aussi. Syntaxe des deux scripts vérifiée (`bash -n`).
- Éprouvé hors machine : faux `lean` (trois modes) et chaîne épinglée (v6 code 0, v4 code 1) dans
  `tests/test_lean_essai_pilote_v10.py` ; ces essais sont dans le témoin scellé des mutations (lot 00 : « 142 passed,
  1 deselected »). Après la coupure, `cmp` entre le fichier compilé avant et celui placé sous `/opt/harnais/noyau`.
- **Deux limites** (correction E2, suggestions S1 et S2) : l'essai **compile** le vérificateur, il ne l'**exécute** pas
  (pas d'import de Mathlib avec ses extensions) ; il tourne sous `runuser -u bac`, **hors** du bac (`bwrap`, `systemd`,
  `MemoryMax=6G`). Et rien de mécanique n'empêche de lancer « apres » après un « avant » en échec : cela tient à la
  procédure.

### 4. Procédure v11 : conforme au mot de Lazar (R-2439), avec une imprécision de commit.

- Terminal WSL ouvert pendant tout l'essai : section 0, point 1, avec la conduite s'il se ferme après L5. Présent.
- Troisième essai sous `GO-2026-11-10-13` : `preparer` et `creer-et-armer` le portent ; `--deja-depense-usd 0.56` en L5.
  Vérifié contre `registres/depenses.md` (l. 422 et 427 : 0,28 + 0,28 USD ; plafond 65 USD ; ligne de GO valide jusqu'au
  2026-11-30 dans `registres/go.md`).
- Troisième machine déclarée, garde « une machine par GO » contournée par construction (branche du poste neuve, `V`
  sans pièce des deux premiers essais) : dit au point 5 du rappel v9→v10 et au point 6 de la v11 ; à la tête
  `ae894d8d`, `V` ne contient ni `rattrapage-machine-d1a-*` ni `journal-creations-machines-v1.jsonl` (vérifié par
  `git ls-tree`).
- `stat` du vérificateur : la v6, mode 644 dans l'arbre (vérifié : `100644`, pilote et essai R5 `100755`).
- **Imprécision (E1)** : l'en-tête fait partir la branche du poste « du commit ci-dessus », soit `5103a7f3` ; or la
  procédure v11, les empreintes v8 et les journaux n'existent qu'à `ae894d8d`. Les 22 fichiers ajoutés entre les deux
  sont tous des journaux et documents (aucun code) : sans effet sur le harnais, mais le poste ne trouverait pas sa
  procédure.
- **Imprécision (E2)** : section 7, « dans le bac (bwrap, systemd, `MemoryMax=6G`), son premier passage est l'essai R5
  de compilation (avant la coupure) » — l'essai R5 ne tourne pas dans le bac et n'exécute pas le vérificateur.

### 5. Journaux et empreintes : cohérents et justes.

- Les treize compagnes `.sha256` lues (journal hors machine v2, huit lots, empreintes v8, procédure v11, journal des
  essais, vérificateurs, artefact et attendus v5) sont égales aux empreintes recalculées.
- `essai-verificateur-hors-machine-v2.json` (`f89a404c…`) : chaîne Lean 4.35.0 `eb6cafb7…`, Mathlib `56a00585…` ;
  vérificateur v6 `3ef23bfa…`, compilation code 0 sans message ; 41 cas = 9 cas « noyau » en deux passages (18) +
  21 cas « lean » + 2 observations non jugées ; **39 jugés, 39 conformes, aucun écart** (recompté).
- Mutations v10 : huit lots, bornes contiguës (0:0 témoin, 0:71, 71:141, 141:145, 145:149, 149:161, 161:173, 173:176),
  **176 identifiants distincts, 176 tuées, aucune survivante, aucune par délai**, code de sortie 0 partout, commit du
  code `5103a7f3` partout (recompté).
- `empreintes-harnais-v8.txt` (`409da1ff…`) : 157 lignes d'empreinte, **157 égales** aux fichiers de l'arbre ; arbre
  `75ac87d9…` égal à `git rev-parse 5103a7f3^{tree}` ; les pièces que le pilote copie y sont toutes.
- `attendus-v5.json` : seule différence contre la v4, le nom de version, le cas du simproc (fichier v5) et une note.
- **Réserve sur ce que prouvent les mutations (E3)** : le lanceur s'arrête au premier essai en échec (`-x`). La
  mutation **k06 « rejeu par le noyau retiré »** est tuée en 20 s, au 129ᵉ essai, soit
  `test_artefact_avertissement_refuse` : cet essai remplace dans le texte du vérificateur la ligne que k06 a retirée ;
  le remplacement devient sans effet et l'essai échoue **par accident de texte**, avant le jeu d'artefacts. De même
  k01 (axiomes jamais établis), k09, k10 et k11 sont tuées en 12 à 14 s, au 113ᵉ essai, avant tout passage d'artefact
  (essai de compilation ou de texte ; k11 et k12 y sont à leur place, c'est leur objet). Le journal **ne montre donc
  pas** que les artefacts fonctionnels (simproc, `run_cmd`, axiome) tueraient le retrait du rejeu ou de la collecte des
  axiomes. Le comportement du code non muté, lui, est établi par le journal hors machine (refus nommés).

### 6. L'essai daté désélectionné : sans effet sur la sûreté.

- `tests/test_lean_essai_minuterie_v7.py::test_creation_avec_course_ne_detruit_pas` : la date de référence de l'essai
  est fixe (`T0 = 2026-11-11T01:00Z`, échéance `T0 + 39 h = 2026-11-12T16:00Z`), mais la minuterie enfant, vraie, lit
  l'horloge réelle : depuis cette heure elle voit l'échéance atteinte et détruit au lieu de garder. L'enfant parle à un
  faux transport (aucun appel réel à Hetzner). C'est un défaut de l'essai, pas du code : `minuterie_v7.py` et son
  fichier d'essais sont inchangés depuis `32a40613` (second essai). Le comportement révélé (échéance passée →
  destruction) va du côté sûr.
- La désélection est déclarée (journaux des lots, procédure v11 point 5, R-2470, R-2486) et comptée par le lanceur
  (« 1 deselected » exigé, sinon arrêt).
- Ce qui est perdu : la propriété « une création avec course à l'`exec` ne détruit pas le serveur » (coût et
  disponibilité, pas sûreté) n'est plus éprouvée par un essai qui passe ; les lancements réels en série et la minuterie
  réelle détachée (dates relatives) le restent. Suggestion S6.

## Corrections exigées

- **E1 — commit de départ du poste** (consigne v3) : nommer `ae894d8df2a19f51e532ff667160ae7bba2bf6ac` (ou un
  descendant qui ne touche pas au code), et non `5103a7f3` comme le dit l'en-tête de la procédure v11 : la procédure
  v11 et les empreintes v8 n'existent pas à `5103a7f3`.
- **E2 — réserve de mémoire dite juste** (consigne v3) : écrire que l'essai R5 de compilation ne tourne **ni dans le
  bac ni en exécutant** le vérificateur ; que le premier passage réel du vérificateur sous `MemoryMax=6G` et
  `MemorySwapMax=0` (2,1 Gio de mémoire anonyme mesurés hors machine, plus les pages des `.olean`) a lieu **après la
  coupure**, au premier pas `noyau` ; et dire au poste quoi relever si ce pas échoue par la mémoire ou le délai
  (`incident_bac`, résumé `systemd`, `erreurs_noyau`), puis fin normale (section 5), sans relance.
- **E3 — portée des mutations** : ne pas citer « 176 sur 176 » comme preuve que le jeu d'artefacts détecte le retrait
  du rejeu ou de la collecte des axiomes. Avant toute réutilisation du vérificateur au-delà de l'outillage (D-1b), le
  développeur rejoue k06 et k01 (et k09, k10) de façon qu'un **essai fonctionnel** les tue : `test_artefact_avertissement_refuse`
  désélectionné pour k06 ; pour k01, une mutation qui ne crée pas d'avertissement de compilation ; journal scellé nommant
  l'essai qui tue. Non bloquant pour le troisième essai, qui joue lui-même ces artefacts sur la machine.

## Corrections suggérées

- **S1** : faire écrire par l'essai R5 de compilation un témoin sur la machine, et faire vérifier ce témoin par la phase
  « apres » **avant** `couper_reseau_v1.sh` : un « avant » en échec ne pourrait plus être suivi d'une coupure.
- **S2** : avant la coupure, un passage réel du vérificateur sur l'item sain, par `bac`, sous `systemd-run` avec
  `MemoryMax=6G` (sans l'exécuteur, qui exige le réseau fermé) : un échec de mémoire ou d'import serait vu avant la
  coupure, comme le défaut de compilation du second essai aurait dû l'être.
- **S3** (vérificateur v7, plus tard) : après `ajouterAcceptee`, exiger que chaque constante rejouée soit dans
  l'environnement d'impression avec le même type que dans l'environnement rendu par le rejeu ; et refuser un bloc
  inductif dont un membre manque (`filterMap` le laisse tomber en silence, là où le rejeu lit `[n]!`). Ferme l'écart
  théorique du point 1.
- **S4** : ajouter aux artefacts joués sur la machine le cas `module` + `public import Mathlib` (aujourd'hui éprouvé hors
  machine seulement), et les mots `module`, `public`, `meta` à la garde de texte G-L3+.
- **S5** : faire échouer G-L7 si la sortie d'erreur du vérificateur (`noyau.err`) n'est pas vide (une panique de Lean y
  sort sans changer le code de sortie) ; aujourd'hui elle est rapportée, pas jugée.
- **S6** : un fichier d'essais neuf pour la minuterie (nom neuf, R12) où l'essai de la course prend ses dates par
  rapport à l'heure courante ; la propriété redevient éprouvée.
- **S7** : dire dans la réserve de la procédure que les axiomes des lemmes de Mathlib viennent des tables précalculées
  de ses `.olean` (point 1).
- **S8** : sceller un journal des « 53 essais ciblés » de la v6 (seul le témoin des mutations, 142 essais passés, en
  porte la trace scellée) ; corriger l'en-tête de la procédure (« n'a écrit ni le harnais » : le développeur a écrit
  les vérificateurs v5 et v6).

## Ce que je n'ai pas fait

- Aucun passage Lean : ni compilation du vérificateur, ni rejeu d'un artefact, ni mutation rejouée. Les affirmations
  sur le comportement à l'exécution reposent sur les sources de la chaîne et sur les journaux scellés du développeur.
- Aucune lecture du code C++ du noyau (absent du disque).
- Pas de suite complète d'essais (interdit 5) ; l'essai daté n'a pas été rejoué par moi (trois échecs isolés rapportés
  par le développeur, cause relue dans le code).
- `minuterie_v7`, `garde_go`, `hetzner_v5` : non relus (inchangés, hors des pièces à contre-lire), sauf le passage du
  déjà-dépensé.
