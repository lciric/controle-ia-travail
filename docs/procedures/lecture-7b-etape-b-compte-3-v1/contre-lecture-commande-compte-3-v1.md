# Contre-lecture de la commande du compte 3 (lecture de 7b et étape B de T0.7) — v1

- **Contre-lecteur** : sous-agent neuf, **modèle C** (aucun identifiant de modèle écrit). Consigne suivie : `consigne-contre-lecture-commande-compte-3-v1.md`
  (empreinte vérifiée avant lecture : `23f4767d618b512fe3c661e04c1962c73bc2178f4f5aad8369ddbe85de1e4da0`, égale à son compagnon).
- **Déclaration** : je n'ai écrit aucune des pièces lues. Je n'ai ouvert aucune sortie de 7a, de 7b ni de T0.7 (ni `diag/`, ni `runs/`, ni
  `donnees/` de ces runs, ni les branches interdites, ni `lecture-sondes-t06.json`, ni `resume.json`, ni l'extracteur, ni rien de l'étape B bis).
  Je n'ai ouvert que les fichiers de la liste de la consigne, plus : `scripts/extraire_mesures_epreuve_t06_v1.py` (en-tête et fonction
  `mesures`, demandés par la consigne), `prealables-v1.md`, `rapport-preparateur-v1.md` (non lu), le fichier de répétition jouet
  `docs/notes/g0-deux-semaines-v1/t07-module-v2/repetition-jouet-v2/resume-repetition-jouet-v2.json` (une seule clé, `etape_b_s`, relevée par
  `grep -o` : sortie d'un jouet, non d'un run réel) et la ligne de la consigne d'audit des fuites (§ 3, § 4). Aucune valeur de clé lue (une seule
  vérification de présence et de préfixe de `CLAUDE_CODE_REMOTE_SESSION_ID`, sans afficher la valeur). Aucun commit, aucune poussée.
- **Heures** : début `2026-11-14T11:53:13Z` ; fin `2026-11-14T12:04:43Z` (`date -u`).
- **Vérifications faites par moi** : compagnons de toutes les pièces du dossier (conformes) ; empreintes citées dans la commande (consigne, blanc,
  attestation, essais, sorties, préalables, texte de T0.6, configuration 7b, configuration v8 de T0.7 : égales) ; `bash -n` sur les **18 blocs**
  de la commande (extraits dans un dossier à part du bloc-notes) : aucune erreur de syntaxe ; correspondance `cse_` → `session_` de l'identifiant
  de session : conforme à la forme exigée ; `.venv` de ce dépôt : numpy 2.4.6, scipy 1.17.1, torch 2.14.1 (égaux à `requirements-cpu.txt`).

## Verdict

- **Phase A (table A de T0.6 sur 7b) : remettable après corrections** (CL3-01, CL3-02, CL3-03, CL3-12, CL3-13, CL3-17, CL3-18 ; la consigne scellée du lecteur A
  n'existe pas encore : elle reste à contre-lire).
- **Phase C (étape B de T0.7) : non remettable** en l'état (CL3-04, CL3-05, CL3-06, CL3-07 ; une répétition de bout en bout sur dépôts jouets, comme celle de
  la commande de P3-bis, est exigée avant remise).
- Décompte : **1 bloquant, 6 majeurs, 14 mineurs** (21 constats).

## Constats

### CL3-01 — majeur — l'ordre « verdict A versé dans `main` » puis « code de la pièce mots et coût » viole la règle d'ignorance du texte de T0.6

- **Lieu** : commande, en-tête de la phase A (« peut commencer tout de suite », l. 233) et section 15, point 1 (l. 727-731 : la mère « recopie à l'octet
  dans `main` » le verdict) ; phase B (l. 391 : la pièce « n'existe pas »).
- **Preuve** : T0.6 `prereg/T0.6-organismes-v0-v1.md`, « Concordance avec T0.7 », point 2 (l. 765) : les réglages ouverts de la pièce « sont fixés sans
  vue des données de 7b : l'auteur du code et son contre-lecteur sont des sous-agents qui n'ont ouvert ni `mesures-t06.npz`, ni `textes-actions-t06.jsonl`,
  ni aucun résultat de 7b ». Le verdict de la table A est un résultat de 7b (effets du coût, effectifs, extrait de textes de l'audit R4, réserve de mémoire).
  Le journal provisoire du bloc F (l. 658-676) recopie en outre les rapports des lecteurs « tels quels » sur la branche de la phase A, visible au distant.
  La base (A) de T0.8 (l. 113 et 149-153 du texte) répète la règle : code écrit « sans vue des données de 7b ».
- **Problème** : rien dans la commande n'interdit que le verdict A (ou le journal provisoire) soit lu par l'auteur ou le contre-lecteur du code de la pièce,
  qui n'est pas encore écrit.
- **Correction proposée** (section 15, point 1) — ancien : « recopie à l'octet dans `main` (même blob), rescelle, consigne au registre des décisions, met à jour
  la liste « qui a lu quoi » … ». Nouveau : le même texte, suivi de : « **Tant que la ligne `CODE-MOTS-ET-COUT-T06` n'est pas inscrite, le verdict A, son
  fichier d'issue et le journal provisoire de la phase A restent hors des fichiers lus par l'auteur et le contre-lecteur de la pièce « mots et coût » (liste
  positive de fichiers dans leurs consignes) ; la mère le consigne, et le dit à Lazar si l'ordre inverse n'est pas possible (nœud). »** À reprendre dans la
  consigne du lecteur A (rapport et journal : aucun montant d'effet cité hors des fichiers scellés du verdict).

### CL3-02 — majeur — l'exclusion de la session hôte ne couvre ni NARCBench (bras descriptif de T0.7) ni les papiers B et C

- **Lieu** : commande § 1 (l. 87-88 : « exclue de l'analyse de ces verdicts, de la conception et des verdicts de l'étape B bis, de T0.8 et de G0 ») et
  § 11 bloc F, ligne P3L-005 (l. 675) ; § 2 (l. 99-106).
- **Preuve** : brief du compte 3 (`docs/notes/plan-paquet-multi-comptes-v1/brief-compte-3-v1.md`) l. 20 (reproduction NARCBench : texte court préenregistré,
  contrôles de construit, bases de N-069, puis course) et l. 21 (« note de recentrage et brouillon 6 du préenregistrement du papier C ; brouillon 1 du
  préenregistrement du papier B ») ; l. 27-28 (rôles exclus) ; T0.7 (l. 2091 et suivantes, liste des marques) : `NARC` = « NARCBench sur le 8B, bras
  descriptif de T0.7 » ; plan multi-comptes l. 40 et 114-124 (compte 3 « l'écrit et la joue »).
- **Problème** : l'hôte lit au moins le rapport final de chaque lecteur (commande l. 83-84), donc une ligne de la table A et une phrase du critère 3 ; la
  même mention de « compte 3 » désigne aussi la session qui rédige et joue le préenregistrement du bras descriptif de T0.7 et les brouillons des papiers B
  et C, qui portent sur des résultats de sondes. Ni la commande ni l'attestation ne séparent ces rôles.
- **Correction proposée** (section 1, interdits ajoutés) — ancien : « cette session est ensuite exclue de l'analyse de ces verdicts, de la conception et des
  verdicts de l'étape B bis, de T0.8 et de G0. » Nouveau : « … de T0.8 et de G0, **et de la rédaction, de la contre-lecture et de la course du
  préenregistrement NARCBench (bras descriptif de T0.7), ainsi que des brouillons des papiers B et C ; elle n'exécute aucune tâche du lot du brief du compte 3 et
  n'est jamais la session de ce lot** ». Ajouter la même exclusion à la ligne P3L-005 et à la liste v2. Voir Q11.

### CL3-03 — majeur — les filtres de cloisonnement ne portent que sur les noms de fichiers, jamais sur le contenu des extraits

- **Lieu** : bloc A3 (l. 306-313) ; bloc C5 (l. 579-587).
- **Preuve** : bloc A3, l. 308 : la boucle `for r in R-2077 R-2082 R-2413 R-2704` verse la ligne R-2704 de `registres/decisions.md` dans
  `extrait-registres-table-a-v1.md` : cette ligne (lue par moi, `registres/decisions.md` l. 2664) porte les empreintes de `SCORES-T07` et `SONDES-T07`, l'issue
  de P3-bis avec ses nombres (aire 0,801, plancher 0,650, 48 épisodes sur 60), une réserve sur le coût (« T dont l'effet du coût exclut 0 ») et la mention des
  verdicts de « 7b et de l'étape B ». Le filtre de la ligne 312 (`t07|t0\.7|…|bbis|…`) s'applique à `cut -c67-` du bordereau, c'est-à-dire aux **noms**
  des fichiers, pas à leur contenu. Bloc C5, l. 580-583 : l'extrait du lecteur B recopie **tout** le registre (`grep -n '^| '`) et la ligne `R_BA_L2` de
  `registres/decisions.md` ; les lignes R-2714, R-2715 et R-2716 de ce registre (conception de l'étape B bis) montrent qu'une ligne de décision de la mère
  mêle volontiers deux sujets.
- **Problème** : un contenu de l'étape B bis ou de T0.7 peut entrer dans les pièces d'un lecteur sans qu'aucun arrêt ne se déclenche ; le lecteur A reçoit des
  nombres de P3-bis et des mentions de T0.7 dont il n'a pas besoin.
- **Correction proposée** : (a) bloc A3, l. 308 et 310 — ancien : `for r in R-2077 R-2082 R-2413 R-2704` et `= 6` ; nouveau : `for r in R-2077 R-2082 R-2413`
  et `= 5` (la ligne `VERDICT-P3BIS` du registre des scellements suffit à l'embargo levé) ; (b) après l'écriture de chacun des deux extraits (A3 après l. 309, C5
  après l. 584), ajouter : `grep -n -i -E 'bbis|b-bis|etape-b-bis|étape B bis|bras-attaque|mode-tenu' "$P/extrait-registres-etape-b-v1.md" && arret "contenu interdit
  dans l'extrait"` (et, pour l'extrait A, ajouter `t07|T0\.7|SCORES|SONDES`). Si la ligne `R_BA_L2` mêle B bis et BA-L2, la mère écrit une ligne dédiée.

### CL3-04 — majeur — bloc C4 : aucune reprise prévue si l'outil rend la main après l'appel de l'étape B ; asymétrie avec le modèle suivi

- **Lieu** : bloc C4 (l. 527-562) ; section 4, « Délai de l'outil » (l. 130-131) ; section 14 (l. 718-720).
- **Preuve** : modèle suivi `commande-ouverture-verdict-p3bis-compte-2-v2.md` § 11 (l. 478-482 et 775-778) : l'appel et la mise au distant du journal se jouent dans un
  appel, **mais le bloc de commit et de poussée est un bloc distinct, relançable seul** (« Le bloc 9 seul ne se relance qu'après une poussée ou un commit en échec »)
  parce que « le journal ne doit jamais n'exister que sur le disque de ton conteneur plus longtemps que le temps de le pousser ». Ici, C4 s'ouvre par
  `[ ! -e "$BAC/code-etape-b-v1.txt" ] || arret …` (l. 529) : si l'outil rend la main après la ligne 542 (code écrit) et avant la poussée (l. 556), **relancer C4
  s'arrête**, et la section 14 ne prévoit que « tu ne relances rien … un seul appel pour relever `ls diag/$R7/` et `tail -n 3` du journal ». Le journal (deux lignes
  `OUVERTURE-T07`) et `lecture-t07.json` ne vivraient alors que sur le disque du conteneur ; la commande dit « un seul appel de l'étape B » mais ne dit pas qui
  commite et pousse. Si l'outil rend la main **pendant** le module (avant l'écriture de `code-etape-b-v1.txt`), un relancement de C4 passerait la ligne 529 et
  rappellerait l'étape B (une seconde ligne `OUVERTURE-T07`), contraire à « un seul appel ».
- **Correction proposée** : scinder C4 en **C4a** (lignes 528-545 : appel, code, nombre de lignes ; juste avant l'appel, écrire `touch "$BAC/appel-etape-b-lance-v1.txt"` et
  faire échouer C4a si ce fichier existe) et **C4b**, relançable seul : il commence par `[ -e "$BAC/code-etape-b-v1.txt" ] || arret "C4a pas terminé"` et reprend
  les commits et la poussée (l. 546-558), chaque commit gardé par l'existence de `$BAC/c-journal-b-v1.txt` / `c-sortie-b-v1.txt` comme dans le bloc 9 du modèle.
  Dans la section 14, remplacer « tu ne relances rien … » par : « si l'outil rend la main après `code de l'étape B : …` : relance **C4b seul** ; avant : un seul
  appel de relevé (`ls diag/$R7/` : noms ; présence de `appel-etape-b-lance-v1.txt` ; nombre de lignes du journal), puis rapport (nœud) ».

### CL3-05 — majeur — la durée de l'étape B n'est ni mesurée ni bornée face à la limite de dix minutes au premier plan

- **Lieu** : section 4 (l. 130-131 : « délai maximal de ton outil (dix minutes), au premier plan ») ; bloc C4 ; commande l. 13-14 (phase C « complète »).
- **Preuve** : aucune durée de l'étape B réelle n'est citée dans la commande ni dans les préalables. La seule valeur disponible est celle d'un jouet (`etape_b_s` : 1,81 s,
  répétition jouet v2) ; le module fait, par sonde et par jeu, 2 000 tirages d'aire, des planchers à 800 directions et des lectures complémentaires (`lecture_v4.etape_b`,
  l. 568-697), sur environ 5 760 actions. L'ordre de l'étape A (`ordre-execution-etape-a-t07-v2.md` § 5 bis, l. 618-624) donne ces ordres de grandeur d'effectifs, pas de durée.
- **Problème** : si l'étape B dépasse la limite de l'outil, le module est interrompu après la ligne `OUVERTURE-T07` (journal écrit) et avant l'écriture du résultat ; aucune
  consigne ne dit quoi faire de cet état, et le principe « lecture unique, R12 » est menacé.
- **Correction proposée** : avant la remise, mesurer le temps du module sur données factices de taille réelle (ou rejouer la passe à blanc de l'étape A et relever
  `durees_s`), l'écrire dans la commande ; si la durée attendue dépasse 5 minutes, lancer l'appel détaché (`setsid`, identifiant de processus écrit dans `$BAC`, attente par
  boucle courte sur le fichier de code) au lieu du premier plan.

### CL3-06 — majeur — le contrôle à blanc ne couvre pas les voies qui donnent le code 3 (arrêt sans relance) ni les refus de forme du module

- **Lieu** : `controle_a_blanc_etape_b_compte_3_v1.py` (sections 1 à 8) ; commande l. 508-523 et 534-538.
- **Preuve** : le module, après `ouvrir`, écrit `arret-etape-b.json` (code 3, « l'étape B ne se relance pas après un code 3 », T0.7 l. 1466-1470) sur toute `GardeArret` de son corps :
  `lire_issue_mots_et_cout` n'en fait pas, mais `lv1.lire_episodes_t06` (empreintes `mesures_sha256` et `textes_sha256` contre `episodes-t06.json`),
  `lv1.ouvrir_scores` (index `sondes_lues` contre `sondes-t07.json`), `lv1.charger_mesures` (colonnes `jetons_notes`, `pas`, `mention_etendue`, `cout`),
  `exiger_nombre_de_directions` (`lecture_v4.py` l. 602, 613-614, 617 ; `lecture_v1.py` l. 598-609, 647-660, 815-837). Avant ces appels, `lecture_v2.ouvrir` (l. 395-545)
  refuse (code 2, relançable) sur : `lire_table_A` (`verifier_resultat` : rattachement de `lecture-cout-t06.json` au manifeste de 7b), `controler_run` (`go_id` du manifeste),
  `controler_t07` (manifeste de T0.7 contre `sondes-t07.json`), `lire_fuites` (domaine du fichier d'audit, chemin attendu, consigne). Le script ne fait que **hacher** ces
  fichiers ; l'essai le confirme : tous les fichiers de la racine jouet contiennent « jouet <chemin> » (essai, l. 28 et 57), donc aucune de ces voies n'est exercée.
- **Problème** : un « tout conforme » du blanc n'empêche pas un code 3 (irréversible) ni plusieurs refus évitables ; la commande dit pourtant (§ 0.3) que chaque irréversible est précédé
  d'un contrôle à blanc.
- **Correction proposée** : ajouter au script une **section 9 « chaîne de rattachement »**, jouée seulement avec l'interpréteur qui a torch (`PYC`), qui appelle les fonctions du code de C7 —
  `lecture_v1.lire_table_A`, `lecture_v1.lire_episodes_t06`, `lecture_v1.lire_fuites`, `manifeste.verifier_resultat` sur `sondes-t07.json`, `lecture_v2.lire_manifeste` sur les deux manifestes —
  et n'imprime que « conforme » ou le motif du refus (jamais une valeur lue) ; un essai R5 jouet avec de **vrais** petits fichiers (cas sain) et six artefacts (empreinte d'un
  tableau, rattachement faux, colonne absente…). Si la mère juge que cette lecture structurelle excède « n'ouvre aucun résultat », elle le décide et l'écrit ; sinon l'écart
  est déclaré comme risque résiduel avant la remise.

### CL3-07 — bloquant (phase C) / majeur (phase A) — blocs jamais répétés, dont tout le chemin de l'unique appel

- **Lieu** : annexe, « Limite » (l. 751-754) ; en-tête l. 12-15.
- **Preuve** : la commande reconnaît que A1, A2, A3, A5, C0, C1, C3, C4, C5, C7 et F « n'ont pas été répétés » ; la commande de P3-bis a été répétée de bout en bout (32 conformes
  sur 32, d'après la commande elle-même, l. 753). Répétés : C2 (7 sur 7), 1, 2, A4 et C6 (aucune sortie archivée, voir CL3-15).
- **Problème** : le chemin « branche, extraction par liste positive, blanc, appel unique, commits, poussée, bordereau, remise » est irréversible et contient des enchaînements
  (variables, `git switch` entre branches, fichiers non suivis dans la racine, `git add` ciblés) dont aucun n'a été joué ensemble.
- **Correction proposée** : répétition de bout en bout sur un dépôt jouet à trois branches et un module jouet (l'étape B de C7 sur des données factices valides si elle existe, sinon
  un module qui écrit `lecture-t07.json` et une ligne de journal), couvrant au moins : A1 à A3 et A5 ; C0 à C5 et C7 ; le bloc F ; l'interruption simulée de C4 (CL3-04) ; archiver
  entrée, sortie et empreinte (règle R6). Remise de la phase C seulement après cette répétition.

### CL3-08 — mineur — C1 : clone peu profond possible, le commit C7 peut manquer

- **Lieu** : bloc C1, l. 432-433.
- **Preuve** : `git cat-file -e "$C7^{commit}"` puis `git merge-base --is-ancestor "$C7" HEAD` ; aucun `fetch` du commit ni déprofondeur ; `prealables-v1.md` constat 7 :
  un commit absent du clone d'un conteneur est déjà arrivé (découpeur `c7484c43…`).
- **Problème** : sur un clone peu profond, la branche de la phase C est créée et **poussée** (l. 445) seulement après ces contrôles, donc l'arrêt est sûr, mais la phase C se bloque
  pour une cause évitable.
- **Correction proposée** — ancien : `git cat-file -e "$C7^{commit}" || arret "commit C7 absent de ton dépôt : rapport à la mère"`. Nouveau :
  `{ [ "$(git rev-parse --is-shallow-repository)" = false ] || git fetch --no-tags -q --unshallow origin +refs/heads/main:refs/remotes/origin/main; }; git cat-file -e "$C7^{commit}" || arret "commit C7 absent de ton dépôt : rapport à la mère"`
  (à placer **avant** le `git switch -c`, avec refspec explicite).

### CL3-09 — mineur — C1 : l'interpréteur existant n'est pas contrôlé en version ; l'installation peut dépasser dix minutes

- **Lieu** : bloc C1, l. 438-444 ; section 4.
- **Preuve** : `"$PY" -c 'import torch, scipy, numpy'` accepte toute version ; `requirements-cpu.txt` fixe numpy 2.4.6, scipy 1.17.1, torch 2.14.1 ; l'étape B est la lecture décisive.
  Environ 6 Go à installer (préalables, constat 5) sous un délai de dix minutes ; la section 4 interdit la relance, alors que C1 est écrit pour être relançable (l. 430, 434, 440).
- **Correction proposée** : après le choix de `PYC`, ajouter `"$PYC" -c 'import numpy, scipy, torch; assert (numpy.__version__, scipy.__version__, torch.__version__.split("+")[0]) == ("2.4.6", "1.17.1", "2.14.1")' || arret "versions ≠ requirements-cpu.txt"` ;
  séparer l'installation (bloc C1a, relançable, sans irréversible) du reste ; autoriser expressément la relance de C1 (section 4 : « sauf C1, C1a, … »).

### CL3-10 — mineur — C2 : `place` refuse un fichier suivi même égal ; le fichier de scores recomposé n'est pas relançable

- **Lieu** : bloc C2, l. 456 et 488.
- **Preuve** : l. 456 : un fichier suivi de la branche → arrêt, même s'il est égal au blob (cas où la mère a recopié `runs/…/manifeste.json` dans `main`, ce que la ligne `RUN-CONFIRMATION-T06`
  appelle déjà) ; l. 488 : `[ ! -e "$DEPOT/$S" ] || arret` : un fichier tronqué par un délai bloquerait la relance, et la répétition jouet efface `$S` à la main avant de relancer (script, l. 80).
- **Correction proposée** — ancien (l. 456) : `… && arret "$3 est un fichier suivi de la branche"`. Nouveau : `if git … ls-files --error-unmatch … ; then git -C "$1" show "$2:$3" | cmp -s - "$DEPOT/$3" && { echo "suivi, égal : $3"; return 0; } || arret "$3 suivi et différent"; fi`.
  Ancien (l. 488) : `[ ! -e "$DEPOT/$S" ] || arret "$S existe déjà"`. Nouveau : accepter si `sha256sum "$DEPOT/$S"` égale 13ac4480… et passer à la suite ; sinon arrêt.

### CL3-11 — mineur — marqueur `<<MODELE_LECTEUR>>` sans emplacement ; repli « modèle A, faute de C » sans nœud

- **Lieu** : § 3 (l. 113) contre blocs A4 (l. 325) et C6 (l. 597) ; § 0.4 (l. 48-50).
- **Preuve** : le tableau annonce un marqueur rempli par Lazar « blocs A4, C6 », mais les blocs écrivent `NOTE_MODELE="modèle C"` en dur ; aucune occurrence de `<<MODELE_LECTEUR>>`. Le texte scellé de T0.7
  (l. 1538) n'exige pas d'autre modèle pour le verdict ; la décision R-2718 prévoit les lecteurs « d'un autre modèle » sur C ; un lecteur du modèle des auteurs est donc un écart qu'aucun nœud ne couvre.
- **Correction proposée** : retirer la ligne du tableau (ou mettre `NOTE_MODELE='<<MODELE_LECTEUR>>'` et l'arrêt sur marqueur restant) ; § 0.4 : « à défaut, **arrêt et nœud de Lazar** » plutôt que modèle A.

### CL3-12 — mineur — nombre de fichiers de traces : dix attendus, « onze traces » au registre

- **Lieu** : bloc A2, l. 280-281 ; `prealables-v1.md` P1.4.
- **Preuve** : `registres/decisions.md` R-2413 : « tous les compagnons conformes (manifeste, distillation, épisodes, lecture du coût, **11 traces**, résumé, 2 adaptateurs … ») ; le bloc exige
  exactement dix fichiers sous `traces/t06-20261112-051655-1Xzh/`, d'après les noms et tailles relevés par le préparateur.
- **Problème** : un écart de un fichier arrêterait le bloc A2 (sûr), mais la cause n'est pas élucidée (un onzième fichier est-il fermé, ou compté ailleurs ?).
- **Correction proposée** : la mère réconcilie les deux nombres (liste des noms à l'appui) avant la remise ; remplacer `= 10` par la liste de noms attendue.

### CL3-13 — mineur — un seul agent pour lire et prononcer la table A : écart à l'ordre de 7b non consigné

- **Lieu** : § 2 (l. 99-102) ; `prealables-v1.md` P1.7 (« à trancher — nœud N-B »).
- **Preuve** : `ordre-fille-course-confirmation-7b-v1.md` l. 374 : « table A lue … par un lecteur neuf […], verdict par un sous-agent neuf (R13) » (deux rôles) ; le texte scellé de T0.6 (l. 515-518) n'exige qu'un
  sous-agent neuf qui n'a pas écrit le texte ni l'analyse ; la commande suit un seul agent sans dire que le nœud est tranché.
- **Correction proposée** : indiquer dans § 2 « un seul agent lit et prononce (décision de la mère, R-xxxx) » ; la mère inscrit la ligne.

### CL3-14 — mineur — essais R5 du contrôle à blanc : artefacts absents

- **Lieu** : `essai_controle_a_blanc_etape_b_compte_3_v1.sh` (cas A1 à A20, R1 à R1c).
- **Preuve** : aucun cas pour : `CODE-T07` en refus (arbre de C7 modifié, fichier ajouté, ligne datée après la première ouverture de l'étape A) ; `arret-etape-b.json` présent ; `diag/<run>/arret.json` de T0.6
  présent ; ouverture `pleine-anticipee` au journal de P3-bis ; empreinte de la ligne du registre différente de celle du fichier cité (seul le compagnon faux est essayé, A5 et A14).
- **Correction proposée** : ajouter ces cinq cas ; pour `CODE-T07`, essayer depuis une copie jetable du module (modifier un fichier d'une copie du dépôt de code, jamais le dépôt réel).

### CL3-15 — mineur — affirmations d'essai sans sortie archivée

- **Lieu** : annexe, l. 748-750 et 751-752.
- **Preuve** : « blocs 1, 2, A4 et C6 joués sur un dossier jouet … messages sans marqueur restant » et « syntaxe vérifiée par `bash -n` pour les 18 blocs » : aucun fichier ni empreinte (règle R6).
  J'ai refait `bash -n` : conforme sur les 18 blocs.
- **Correction proposée** : verser les sorties brutes et leurs empreintes dans le dossier de la commande.

### CL3-16 — mineur — attestation « qui a lu quoi » : confond compte et session, ne vérifie pas que la session est neuve

- **Lieu** : `attestation_qui_a_lu_quoi_compte_3_v1.py` l. 12-15, 52-69 ; commande l. 222-224 ; `prealables-v1.md` constat 1 (citation de R-2704).
- **Preuve** : (1) toute ligne qui nomme le compte 3 doit porter « aucune exclusion déclarée » : une exclusion de **la session du lot** (brief l. 27-28) arrêterait l'hôte sans raison tenant à lui, tandis qu'une
  ligne de session non nommée (ligne 17 de la liste v1) ne peut pas distinguer le lot et l'hôte ; (2) l'identifiant doit apparaître en entier : un identifiant tronqué dans la liste passe ; (3) « session neuve »
  (R-2711 (2)) n'est vérifiée par rien ; (4) `prealables-v1.md` constat 1 écrit « R-2704 dit l'extraction « plus sous embargo » » : R-2704 (l. 2664) dit « embargo de P3-bis levé », pas cela (la règle est juste ; la citation est
  paraphrasée, à corriger).
- **Correction proposée** : l'exclusion se juge par identifiant de session, la ligne du lot recevant son identifiant dans la liste v2 ; rechercher aussi les 12 premiers caractères de l'identifiant ; ajouter un
  contrôle de nouveauté simple (aucune branche `lot/compte-3-v1` ni `registres-provisoires/compte-3-*` dans le clone local) ; corriger la citation.

### CL3-17 — mineur — le bloc 2 lit des fichiers de la copie locale avant toute récupération de `main`

- **Lieu** : bloc 2 (l. 206-228), blocs 1 et A1.
- **Preuve** : `$ICI/…py`, `$LISTE`, `sha256sums-lancement-v2.txt` se lisent dans le dépôt tel qu'ouvert ; `git fetch` n'a lieu qu'au bloc A1. Si la session a été ouverte avant la poussée de la liste v2 ou de la consigne A, le bloc 2
  s'arrête (sûr) ou lit une version ancienne.
- **Correction proposée** : § 4 : « la mère a poussé la liste v2, la consigne A, la version remise de cette commande sur `main` **avant** l'ouverture de la session » ; bloc 2, début : `git fetch --no-tags -q origin +refs/heads/main:refs/remotes/origin/main && git merge --ff-only refs/remotes/origin/main` si l'arbre est propre.

### CL3-18 — mineur — noms des fichiers du verdict : motif étroit

- **Lieu** : blocs A5 (l. 366) et C7 (l. 634).
- **Preuve** : le motif `-[a-z0-9-]+-v[0-9]+\.(py|txt|json|md)` exclut une archive de fichiers de travail du type `…-fichiers-de-travail.tar` que le lecteur de P3 a produite
  (`docs/verdicts/verdict-P3-premier-test-i-a-v1-fichiers-de-travail.tar`) ; la consigne scellée du lecteur A, absente, doit s'y conformer.
- **Correction proposée** : écrire dans la consigne A et dans la consigne B la liste exacte des noms permis (le motif ci-dessus, sans archive).

### CL3-19 — mineur — « S7 » (ordre de l'étape A) contre « C7 » (commande) ; le manifeste de T0.7 disparaît de la branche après nettoyage

- **Lieu** : § 0.2 et blocs C1, F (l. 685-690) ; `ordre-execution-etape-a-t07-v2.md` § 9 (l. 704 : « étape B jouée à S7 ») ; `prealables-v1.md` constat 4.
- **Preuve** : S7 est un descendant de C7 avec les mêmes `src/` et `tests/` (ordre § 0 septies, P9, `git diff --quiet C7 S7 -- src tests`) ; la commande joue C7 : équivalent pour le code, mais l'écart n'est pas déclaré. Le bloc F retire
  `runs/$R7/manifeste.json` et les entrées placées : `lecture-t07.json` (poussé) cite `manifeste_sha256` d'un fichier qui n'est ni sur cette branche ni sur `main` (il reste sur `donnees/t07-etape-a-v1`), de sorte que
  `verifier_resultat` ne s'y rejoue pas sans le rapatrier.
- **Correction proposée** : § 0.2, ajouter « C7 et non S7 : mêmes `src/` (P9) ; écart déclaré » ; section 15, point 3, ajouter « la mère garde, avec `lecture-t07.json`, le chemin et l'empreinte du manifeste de T0.7 de `donnees/t07-etape-a-v1` ».

### CL3-20 — mineur — deux sorties de l'hôte touchent aux limites du cloisonnement

- **Lieu** : `controle_bbis` (script, l. 135-136) ; section 14 (l. 720).
- **Preuve** : la ligne imprimée « ligne … datée … ; <chemin du plan> : sceau conforme » donne à l'hôte le **nom** du plan de B bis ; `tail -n 3` du journal (section 14) affiche, hors cas du code 2,
  la ligne `scores-t07/<run> (Q = … ; conditions retirées : …)`, qui porte le résultat de la dérivation de Q.
- **Correction proposée** : imprimer le chemin du plan seulement en cas d'écart ; remplacer `tail -n 3` par `wc -l` et la présence de `arret-etape-b.json`.

### CL3-21 — mineur — le message remis au lecteur est recopié à la main

- **Lieu** : sections A4 et C6 (l. 353-355, 622-623).
- **Preuve** : le message scellé (`message-remise-*-v1.txt`) est affiché puis « copié tel quel » par la session dans le message de l'agent ; rien ne permet de vérifier que le texte reçu est le texte scellé.
- **Correction proposée** : demander au lecteur, dans la première ligne de son rapport, l'empreinte de son message reçu (qu'il calcule en recopiant le texte dans un fichier de son espace), et la comparer à celle du bordereau
  du message ; à défaut, le dire au verdict.

## Réponses aux questions

- **Q1.** Non pour les fichiers fermés nommés : aucune liste (A2 l. 275-276, C2 l. 463-475, C5 l. 572-575) ne contient `lecture-sondes-t06.json`, `resume.json`, activations, adaptateurs, `sondes-neuves`, `planchers-figees`,
  `temoins-lexicaux` ni une pièce de l'étape B bis, et les filtres de noms (A2 l. 291, A3 l. 312, C5 l. 586) les refusent ; `lecture-cout-t06.json` n'est pas fermé (T0.7 l. 1540-1541). **Mais** le contenu des extraits n'est pas filtré :
  bloc A3 l. 308 (ligne R-2704 : nombres de P3-bis, empreintes et mentions de T0.7) et bloc C5 l. 580-583 (registre entier, ligne `R_BA_L2`) : CL3-03. Le constat de noms de A2 (l. 286-290) cite les noms `lecture-sondes-t06.json` et
  `resume.json` : noms seuls, voulu (ligne A1 de la table A).
- **Q2.** Oui pour l'essentiel : `lecture-cout-t06.json` (T6-1, T6-2, T6-8, T6-10, ligne de table), `episodes-t06.json` (garde d'équivalence, effectifs), `distillation-t06.json` (paires), `mesures-t06.npz` (actions notées et
  non notées, lisibilité), `textes-actions-t06.jsonl` (échantillon de l'audit R4), manifeste, `run.err` des traces, texte et configuration de T0.6 (l. 463-465 portent la valeur 1,5227 de P3-P1). Rien d'indispensable ne manque ; **un fichier de trop** : R-2704 dans
  l'extrait (CL3-03). Restent à contre-lire : la consigne scellée du lecteur A (absente) et le nombre de fichiers de traces (CL3-12).
- **Q3.** Oui, la règle est juste : l'extracteur ouvre `lecture-sondes-t06.json` (`_lire(d / "lecture-sondes-t06.json")`, l. 33-34 ; clés `verifications_mahalanobis`, `durees_s`, l. 40 et 54-56) et T0.6 l. 771 interdit toute ouverture avant le contrôle d'ouverture v2.
  La commande l'applique partout (§ 0.2, § 1, A2, C2, § 12, filtres de noms, blanc section 7 : fichier fermé absent sous la racine). Seule la citation de R-2704 par les préalables est inexacte (CL3-16).
- **Q4.** Oui, avec réserves. J'ai suivi la garde : exigées (9 avec `CODE-T07`) et permises présentes sur `main` ou placées (manifeste de 7b, scores, sondes, `lecture-cout`, `episodes`, `mesures`, `textes`, manifeste de T0.7, fichier mots et coût sur `main` ou repris sur la
  branche de la phase B, audit sur `main`) ; la configuration v8 ne demande aucun fichier de sondes pour l'étape B ; `scores_base_t06` est nul. `CODE-T07` : dépôt du module = arborescence détachée à C7 (tête = commit cité, 26 fichiers, `git diff` vide, `status` vide avec
  `-B` et `PYTHONDONTWRITEBYTECODE`), donc conforme ; la section 0.2 est juste. Réserves : les voies de refus et de code 3 ne sont pas exercées avant l'appel (CL3-06) ; aucune répétition (CL3-07) ; versions non contrôlées (CL3-09) ; clone peu profond (CL3-08).
- **Q5.** La condition est contrôlée par programme (script, section 8, essais A3 à A7 et A17) et ne fait pas refuser le lecteur de T0.7 : la clé est absente du registre de T0.7, le registre propre n'est lu ni par `registre_v1` ni par la garde adaptée, et la clé sans marque ferait refuser T0.7 si elle y était (A6).
  Cloisonnement : sens B vers B bis — rien dans la commande hors § 15 point 3 (règle écrite pour la mère, pas contrôlée) ; la branche de la phase C est poussée sur le distant partagé, et le journal recopié dans `main` porte la ligne `scores-t07/… (Q = …)` (dérivée de T0.6, non d'une sonde) ;
  sens B bis vers B : bordereau de noms (C5 l. 586), mais pas de filtre de contenu (CL3-03) ; deux fuites mineures de l'hôte (CL3-20).
- **Q6.** Chaque poussée de branche (A1, C1) est éprouvée avant toute remise ; la remise (A4, C6) est précédée d'un contrôle de noms et d'un bordereau scellé ; l'appel unique est précédé de deux contrôles à blanc (C3 puis C4 l. 534-538). Mais le blanc ne couvre pas les voies de code 3 (CL3-06), et la poussée finale
  (A5, C4, C7, F) n'est pas contrôlée de nouveau (acceptable : l'épreuve de poussée précède). Si l'outil rend la main au milieu de C4 : voir CL3-04 (pas de reprise ; relance de C4 qui s'arrête, ou, pire, qui rappelle l'étape B si le code n'est pas encore écrit ; journal et résultat seulement sur le disque du conteneur).
- **Q7.** Partiellement. Le script fait ce qu'il dit sur le registre, les sceaux, les antériorités, la garde adaptée, `CODE-T07`, les fichiers (hachage) et la condition d'ordre ; il n'ouvre aucun résultat (il lit la configuration, les registres, le journal de P3-bis, la ligne et le plan de B bis par hachage) ; la sortie sur l'état actuel
  (aucun refus, deux manques) est cohérente avec le registre que j'ai lu. Il ne prouve pas la chaîne de rattachement ni les voies de code 3 (CL3-06) ; essais R5 incomplets (CL3-14) ; les fichiers du jouet ne sont pas de vrais fichiers de données.
- **Q8.** Juste pour sa règle (liste scellée, session absente, en-tête, lignes du compte 3 sans exclusion ; neuf essais conformes, dont « compte 30 » et « Compte-3 »), mais pas suffisante : compte et session confondus, identifiant entier seulement, nouveauté de la session non contrôlée (CL3-16).
- **Q9.** Correct : manifeste des morceaux comparé aux noms présents, empreinte et taille de chaque morceau (contre le compagnon et le manifeste), somme des tailles, `cat` sur le motif à trois chiffres (le compagnon `.sha256` et le manifeste ne correspondent pas au motif), empreinte du fichier comparée au compagnon **et** à la ligne `SCORES-T07` écrite en dur
  (`13ac4480…`, égale au registre). Répétition jouet : 7 sur 7. Réserve : la relance sur un fichier tronqué (CL3-10).
- **Q10.** Syntaxe : aucune erreur (`bash -n`, 18 blocs). Logique : `arret` appelé dans des fonctions, des sous-shells et des `||` fonctionne (le sous-shell `( … ) || arret` appelle `arret` à l'extérieur) ; le motif `A && B || arret` de `place` et de `attendu` est correct ; `K=$?` du bloc C3 est bien juste après la commande. Fautes : relance de C1 contredite par la section 4 (CL3-09), relance de C2 (CL3-10), reprise de C4 (CL3-04), marqueur sans emplacement (CL3-11),
  nom de fichier du verdict (CL3-18). Le bloc F contient des marqueurs de saisie (`<bloquée | passée>`, etc.) que la session doit éditer à la main : acceptable, gardé par un arrêt.
- **Q11.** Oui, **sous conditions** : le compte 3 n'a pas à être écarté comme hôte si l'hôte est une session distincte et neuve de celle du lot, et si l'exclusion de **cette session** (rédaction, contre-lecture et course du préenregistrement NARCBench, brouillons des papiers B et C, tâches du brief) est écrite dans la commande et la liste v2 (CL3-02). À l'appui : brief l. 20-21 et 27-28 (rôles exclus) ; T0.7 (marque `NARC` : « bras descriptif de T0.7 ») ; plan multi-comptes l. 40 et 114-124. Sinon, choisir un hôte dont le lot ne touche pas à T0.7.
  Le compte 2 (R-2704) et le compte 4 (liste v1, lignes 12-15) sont déjà exclus.
- **Q12.** Autres fautes : aucun identifiant de modèle écrit (recherche faite sur les quatre fichiers) ; aucune heure écrite à la main hors dates de faits cités ; chiffres de la commande vérifiés (empreintes égales ; ≈ 19 Mo et ≈ 151 Mo cohérents avec les préalables ; `numpy==2.4.6` et torch 2.14.1 égaux à `requirements-cpu.txt`) ; citation de R-2704 (CL3-16) ; « onze traces » (CL3-12) ; essais sans sortie (CL3-15) ; S7 et C7 (CL3-19) ; marqueur sans emplacement (CL3-11) ;
  les lignes `R_BA_L2` et `BA-L2` : la commande ne lit pas l'état de BA-L2 (T0.7 l. 2183 le confie à la mère, qui le consigne) : cohérent, à condition que la décision citée dise l'état ou le mot de Lazar.
