# Rapport du développeur — orchestrateur de l'organisme d'idéation : remplacement déclaré du modèle d'un juge externe — v2

- **Développeur** : modèle L', sous-agent neuf lancé par le compte de l'organisme (session `session_013QMaykhk6JHMoHDjwiTneW`).
  Je n'ai écrit ni `pole/ideation_v2.py`, ni la version 1 du module (`pole/bras_remplacement_juge_v1.py`), ni sa
  contre-lecture. La contre-lecture de la v2 (modèle K, agent neuf) reste à faire.
- **Heures** (temps universel, `date -u` ou horodatage des outils) : début non relevé ; premier relevé 2026-11-18T17:24:03Z (module, lanceurs et essais déjà écrits) ; banc de mutations final
  17:25:28Z → 17:26:07Z ; commit de l'orchestrateur `8a2a6ac9…` peu avant 17:26:47Z ; suite complète de la tête
  17:26:47Z → 17:37:28Z ; suite de la base `0861800` ensuite, **jamais en même temps** (17:37:28Z → 17:47:48Z) ; rapport
  à partir de 17:48:01Z.
- **Demande** : tâche transmise par le compte de l'organisme (défaut signalé par la session de relance après la contre-lecture
  de la v1 : étiquette de juge externe répétée). Aucune autre spécification lue.
- **Interdits suivis** : aucune dépense ; aucun appel réseau vers un fournisseur, loueur ou hébergeur ; aucun relais ni
  lanceur en mode réel ; aucune variable d'environnement lue ni affichée (les essais du lanceur par la ligne de commande
  passent un environnement explicite `{"PATH": "/usr/bin:/bin"}`) ; rien lu ni écrit sous `diag/`, `runs/`, `donnees/`,
  `registres/`, `docs/notes/bras-attaque/`. `/home/user/ideation-organism` n'a été que cloné (tête restée `a41b7b50`) ; trois
  clones locaux neufs à poussée neutralisée (`DISABLED-no-push`) : `/home/user/orch-remplacement-juge-v2` (travail),
  `/home/user/orch-remplacement-juge-v2-base` (suite de la base, détaché sur `0861800`), et un clone de rejeu du paquet dans
  le bloc-notes ; aucun poussé ; rien vers `lciric/ideation-organism`. `/home/user/orch-remplacement-juge-v1` non touché.
- **Refus rapportés** : la garde d'isolement de l'arbre de travail a refusé une commande composée (`git diff` et
  `git diff --no-index` enchaînés avec `cd` et des redirections) en demandant de la découper en commandes simples ; je l'ai
  découpée sans changer ce qu'elle faisait. Aucun refus de permission ni de classifieur.
- **Écart de méthode rapporté** : une commande `git commit -F /dev/stdin <<< ""` (chaîne en ligne, proche du heredoc
  interdit) a été lancée par erreur ; message vide, **commit refusé par git**, rien écrit (vérifié : tête restée `0861800`,
  index inchangé). Le commit a ensuite été fait avec un message écrit par l'outil d'écriture (`git commit -F fichier`).
- **Aucune dépense. Aucune ligne de GO** (elle revient à la mère).

## 0. Verdict

**Le défaut est corrigé dans des fichiers neufs (cinq fichiers ajoutés, aucun fichier existant modifié) : toute liste
`juges_externes` dont une étiquette apparaît plus d'une fois est refusée avant toute lecture et tout appel, avec et sans
l'option de remplacement ; les deux lanceurs qui acceptent `--juge-externe` répété ont une copie neuve qui le refuse.** Essais
du module : **34 passed, 43 subtests passed** (19 essais de la v1 portés, 15 neufs). Banc de mutations neuf : **28 tuées pour
la raison attendue sur 28** (17 de la v1 portées telles quelles, 1 portée sur le fichier de la v2, 10 neuves). Suite de
l'orchestrateur : **aucun échec neuf** — mêmes 7 échecs, mêmes 14 erreurs de collecte et mêmes 5 sautés qu'à la base `0861800` (section 5) ; 34 essais de plus, les miens.

## 1. Base, arbre, paquet

- Clone neuf `/home/user/orch-remplacement-juge-v2` de la copie en lecture seule (tête `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`) ;
  paquet v1 (`docs/notes/organisme-remplacement-juge-v1/orchestrateur-remplacement-juge-v1.bundle`, sha256 `5701775c…`,
  `git bundle verify` : « is okay ») récupéré : `0861800260e33224a71f48b111e72ac04288d3cb`. Un commit au-dessus :
  **`8a2a6ac9d3feb52e6771edca52f440dd780fb373`** (branche locale `prep-remplacement-juge-v2`, jamais poussée).
- Arbre `orchestrator/` à la tête : **`71417ad17d816af07a6a57e9dc28bbfac07faac5`** (v1 : `3c6cff30…` ; copie : `ee84d6ec…`) ;
  `orchestrator/pole` : `bfd8585661fdcce6157bc5287f86e2371ea254b3` (v1 : `55cae9e0…`).
- **Paquet `orchestrateur-remplacement-juge-v2.bundle`, base `a41b7b50`** (et non `0861800`) : `git bundle create …
  a41b7b50..refs/heads/prep-remplacement-juge-v2` ; il porte les **deux** commits (`0861800` de la v1, inchangé, puis
  `8a2a6ac`), donc s'applique sur la seule copie en lecture seule, sans le paquet v1. `git bundle verify` : « is okay »,
  prérequis `a41b7b50…`, référence `refs/heads/prep-remplacement-juge-v2 → 8a2a6ac9…`. Rejoué dans un clone neuf de la
  copie : tête `8a2a6ac9…`, parent `0861800`, arbre `orchestrator/` `71417ad1…`, `git diff --name-status a41b7b50` : huit `A`
  (trois de la v1, cinq de la v2), aucun `M` ni `D`.
- Différentiel livré : contre **`0861800`** (`orchestrateur-remplacement-juge-v2-contre-0861800.diff` : cinq `A`) ; le
  différentiel de la v1 contre `a41b7b50` est celui de la livraison v1 (`b45a0b87…`), inchangé.
- Interpréteur : `/usr/local/bin/python3` (Python 3.13.18, pytest 9.1.1), `-B`, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`.

## 2. Fichiers (tous neufs, R12)

| fichier | sha256 | lignes | rôle |
|---|---|---|---|
| `orchestrator/pole/bras_remplacement_juge_v2.py` | `83a08aeeeba694f72e0aceb004c9432c4c57427072ed37208181903f30433ee2` | 86 | module neuf |
| `orchestrator/essais/test_bras_remplacement_juge_v2.py` | `d0ae81de887f1bbd13918c3210ac12113126f6ea7c6f69ca5e392dbc0e8a10be` | 729 | essais (34 essais, 43 sous-essais) |
| `orchestrator/essais/mutations_bras_remplacement_juge_v2.py` | `57f427a5c661190dd769210addea8fc8b31c3f67907dbfd147cced1c3b5e2499` | 115 | banc de mutations neuf (28) |
| `orchestrator/demonstrations/ideation_v2_juges_externes_uniques_v1.py` | `1fbe2be3cab8e843daaecd8547beee05e2948f0e11bdbb9dc1ffacdce4ee7682` | 50 | lanceur neuf (copie de `ideation_v2.py` + garde) |
| `orchestrator/demonstrations/ideation_v1_juges_externes_uniques_v1.py` | `3b471029171dc1e86f700aa55c3058179fbe93b45357e26d06efb903ac08d00d` | 49 | lanceur neuf (copie de `ideation_v1.py` + garde) |

Inchangés (même empreinte à `0861800` et à `8a2a6ac`) : `pole/bras_remplacement_juge_v1.py` `2efd6b08…` (la v1 reste
intacte), `pole/ideation_v2.py` `67d2ad35…`, `pole/ideation.py` `4ee70d25…`, `demonstrations/ideation_v2.py` `bc5e9c98…`,
`demonstrations/ideation_v1.py` `855a1139…`, essais et banc de la v1 (`1e5f39d8…`, `cdd021c6…`).

## 3. Le défaut et la correction

**Défaut** (reproduit ici, essai témoin `test_temoin_le_defaut_existe_dans_la_v2_et_la_version_1`) : `pole/ideation_v2.py`
ligne 2852 et `pole/bras_remplacement_juge_v1.py` ligne 255 construisent `donnes = {e: m for e, m, _ in juges_externes}` ;
avec `[("lx-juge", <non déclaré>, a), ("lx-juge", <déclaré>, b)]`, CL35-04 ne compare que le dernier modèle et passe ; les
deux juges sont ensuite joués (boucles sur la liste) : le modèle non déclaré reçoit la consigne du juge (fiches comprises),
la seconde réponse lève `EcrasementInterdit` sur `reponse.md`, et le bras est verrouillé (`manifeste-bras-rapporte.json`
écrit). Vrai pour la v2 sans option et pour la v1 avec option (même essai, deux sous-cas). Le cœur de la version 1
(`pole/ideation.py`, ligne 2847) a la même ligne.

**Correction** (`pole/bras_remplacement_juge_v2.py`, `executer_bras_differe(sortie, *, remplacements_juges_externes=None,
**réglages)`, alias `executer_bras_rapporte`) :

1. **Première instruction, avec et sans option** : `refuser_etiquettes_repetees(reglages.get("juges_externes", ()))` →
   `CourseInterrompue("juges_externes : étiquettes de juges externes en double [...] : refusé avant toute lecture et tout
   appel (...)")`. La garde ne lit aucun fichier, n'appelle rien, ne touche à aucun attribut des adaptateurs : elle ne
   regarde que le premier élément de chaque entrée tuple ou liste de trois éléments ; égalité `==` (comme deux clés de
   dictionnaire qui s'écraseraient) ; étiquettes montrées caviardées et tronquées (`_vu` de la v1).
2. **Sans option** : `ideation_v2.executer_bras_differe(sortie, **réglages)` elle-même, mêmes arguments (comme la v1).
   **Seul écart au « comportement inchangé »** : une liste à étiquette répétée est refusée ici, avant la délégation, alors
   que la v2 l'aurait jouée deux fois en ne comparant que le dernier modèle. Pourquoi : c'est précisément le chemin du défaut
   (CL35-04 contournée, fiches servies à un modèle non déclaré, session payée, bras verrouillé), et la course elle-même
   refuse déjà « étiquettes en double » (`ideation_v2.valider_etiquettes`, lignes 991-992) : aucune course valide n'a deux
   juges externes de même étiquette, donc aucun bras légitime n'est refusé. Toute autre liste suit la v2 à l'identique
   (essais de la v1 portés : sortie identique octet pour octet sur le cas fixe ; espion : mêmes arguments).
3. **Avec option** : `bras_remplacement_juge_v1.executer_bras_differe` (importé, non copié ; v1 contre-lue « Conforme »,
   intacte) — option validée, garde CL35-04 avec remplacement, déclaration dans le journal, le manifeste du bras et **tous les
   manifestes de tentative**, mention dans la lecture, **auto-préférence recalculée au modèle joué**, lecture par famille
   descriptive, verrous de la v2. La v2 réexporte l'API de la v1 (mêmes objets).
4. **Formes non inspectées** (passées telles quelles, comportement de la v2 inchangé) : un **itérateur** (l'inspecter le
   consommerait ; la v2 et la copie de la v1 le refusent alors elles-mêmes par `TypeError` sur `len`, après lecture des
   fichiers de la course mais **avant tout appel**, rien écrit — essai `test_formes_non_inspectees_suivent_la_v2_sans_appel`,
   0 appel) ; un objet non itérable ; une entrée qui n'est pas un tuple ou une liste de trois éléments (la v2 échoue au
   dépaquetage, avant tout appel). Un lanceur ne passe jamais ces formes.

**Les deux autres points de la relance, tenus en v1, gardés et éprouvés ici** : remplacement déclaré dans
`manifeste-bras-non-joue-N` (essai neuf : adaptateur qui lève `CleDansEnvironnement` avant tout lancement → `journal.
remplacements_juges_externes` égal à l'attendu), `bras-tentative-N` (essai neuf : contrôle refusé après dépense →
idem, coût > 0 ; la tentative 2 qui suit porte encore le remplacement), `manifeste-bras-refus-taille-N` (essai v1 porté et
essai neuf, champ propre) ; auto-préférence au modèle joué (essai v1 porté `test_sain_remplacement_declare_admis` :
`n_propre_modele = 0` au modèle joué, lecture par famille à côté).

## 4. Lanceurs

| lanceur | accepte `--juge-externe` répété ? | suite donnée |
|---|---|---|
| `demonstrations/ideation_v2.py` (cœur `pole/ideation_v2.py`) | **oui** (`action="append"`, aucun refus ; avec `--bras-rapporte-differe` il appelle `idn.executer_bras_differe`, ligne 1249 : le défaut passe par là) | copie neuve `ideation_v2_juges_externes_uniques_v1.py` |
| `demonstrations/ideation_v1.py` (cœur `pole/ideation.py`, même défaut ligne 2847) | **oui** (même code, ligne 1217) | copie neuve `ideation_v1_juges_externes_uniques_v1.py` |
| `demonstrations/ideation_v3.py` (juges seulement) | refusé déjà : `pole/juges_seulement_v1.py` lignes 185-186 « étiquettes de juges en double » | rien |
| autres lanceurs (`ideation_v4` à `v8`, `v59`, …) | pas d'option `--juge-externe` | rien |

« Copie neuve » prise au sens d'un lanceur neuf qui **charge le lanceur d'origine tel quel** (par son chemin, sous un nom de
module neuf) et n'ajoute qu'une garde : même analyseur (`construire_analyseur()`), étiquettes lues comme `roles_et_budgets`
les lit (`paire(j, f"externe-{i + 1}")` : défaut `externe-N`, blancs retirés) ; étiquette répétée → `a.error(...)` (code 2,
message sur la sortie d'erreur, comme toute erreur d'argument), avant toute lecture de fichier, tout appel, toute écriture ;
sinon `principal(argv)` du lanceur d'origine, mêmes arguments. La garde vaut dans tous les modes (dans la course, le cœur
refusait déjà, plus tard). Je n'ai pas recopié les 1 500 lignes du lanceur : la garde se relit en cinquante lignes, et le
lanceur d'origine reste la seule source du reste. Ces lanceurs appellent toujours `pole.ideation_v2` (ou `pole.ideation`)
pour le bras, **pas** `pole.bras_remplacement_juge_v2` : l'option de remplacement n'est toujours pas offerte par la ligne
de commande (comme en v1).

## 5. Essais

`essais/test_bras_remplacement_juge_v2.py` : première partie = `test_bras_remplacement_juge_v1.py` porté (seuls l'en-tête et
la ligne d'import changent : `ecarts-portage-essais-et-banc-v1-v2.diff`) ; seconde partie neuve :

- `TestEtiquetteRepeteeRefusee` : étiquette répétée **sans option** (cinq formes : même modèle, modèle non déclaré d'abord
  ou ensuite, entrées en listes, trois entrées) et **avec option** (quatre formes), sur une vraie course simulée, avec un
  **adaptateur factice qui compte les appels** (`lancer` et `description`) : **0 appel**, contenu de la sortie identique
  octet pour octet, aucun manifeste du bras ni de tentative, aucune tentative comptée (la course reste jouable : tentative
  1 ensuite) ; refus **avant toute lecture** (sortie et attestation absentes, option mal formée : le refus est celui de
  l'étiquette répétée) ; espions : sans option, la v2 n'est pas appelée ; avec option, la v1 n'est pas appelée ; témoin du
  défaut dans la v2 et la v1 (voir 3) puis refus de la même liste par la v2 du module sur une course neuve ; formes non
  inspectées (itérateur) : `TypeError` de la v2, 0 appel.
- `TestGardeEtiquettesPure` : `etiquettes_repetees` (vide, distinctes, répétées, ordre, formes non inspectées, itérateur
  non consommé) ; secret jamais recopié dans le refus ; API de la v1 réexportée.
- `TestManifestesDeTentative` : non joué, tentative payée, refus de taille (voir 3).
- `TestLanceursNeufs` : pour chacun des deux lanceurs neufs, quatre listes répétées (dont l'étiquette par défaut
  `externe-1` répétée et les blancs autour) → `SystemExit(2)`, lanceur d'origine non appelé, rien écrit ; étiquettes
  distinctes → lanceur d'origine appelé avec les mêmes arguments ; le lanceur d'origine, lui, lit la liste répétée sans
  erreur d'argument ; par la ligne de commande (`python -I -B`, environnement explicite) : code 2, message, rien sur la
  sortie standard, sortie non créée.

Décomptes exacts :
- `essais/test_bras_remplacement_juge_v2.py` seul, commit final : **34 passed, 43 subtests passed in 3.65s**
  (`essais-remplacement-juge-v2.txt`).
- Suite de l'orchestrateur, commit final `8a2a6ac` (`essais/`, `-q -rfEs --continue-on-collection-errors`) : **7 failed, 1408 passed, 5 skipped, 14 errors, 1275 subtests passed in 640.41s** (`suite-orchestrateur-remplacement-juge-v2.txt`).
- Même suite sur la base `0861800` (clone neuf détaché, **jouée après la tête, jamais en même temps**, pour ne pas se disputer l'utilisateur dédié du vrai bac comme lors de la v1) : **7 failed, 1374 passed, 5 skipped, 14 errors, 1232 subtests passed in 619.04s** (`suite-base-0861800-remplacement-juge-v2.txt`) — exactement les décomptes de la tête de la v1. Différence : 34 essais et 43 sous-essais, les miens.
- **Listes `FAILED`/`ERROR` identiques** (comparées ligne à ligne) et **`SKIPPED` identiques** : `TestV51.test_v51_10` et `test_v51_15`, `TestR12` (v52b, v53), `TestR12V55` (v54), `TestV49.test_v49_18`, `TestV50.test_v50_17` (fichiers d'archive absents de l'arbre public, comme en v1) ; 14 erreurs de collecte `scipy` absent (mêmes fichiers qu'en v1) ; 5 sautés aux mêmes motifs qu'en v1. Aucun ne touche le bras ni les lanceurs. Rien installé.
- Les deux lignes « code 0 » de `suites-horaires` (bloc-notes, non livré) sont le code de `date`, pas celui de pytest (erreur de mon script) ; les décomptes ci-dessus sont lus dans les sorties de pytest.

## 6. Banc de mutations

`essais/mutations_bras_remplacement_juge_v2.py` (machinerie du banc v66 chargée telle quelle, liste neuve ; toutes jugées par
les essais de la v2) : R01-R09 et R11-R18 = mutations du banc v1, mêmes textes, même fichier muté (`pole/bras_remplacement_juge_v1.py`,
appelé avec l'option) ; **R10 porté sur le fichier de la v2** : le texte de la v1 (`if False:` à la place de la branche sans
option) y est une mutation **équivalente** (sans la branche, la v2 appelle la v1 sans option, qui appelle la v2 elle-même :
le premier passage l'a montrée « survit ») ; mutation portée : sans option, le bras passe par la copie avec remplacement
(option vide) → tuée par `test_sans_option`. Neuves : **V01 garde des étiquettes répétées retirée**, V02 garde seulement
avec l'option, V03 garde seulement sans l'option, V04 garde sur l'entrée entière au lieu de l'étiquette, V05 entrées en
listes ignorées, V06 itérateur consommé par la garde, V07 refus qui recopie l'étiquette (secret), V08 et V09 garde des
lanceurs neufs retirée, V10 étiquette par défaut du lanceur mal lue. Résultat final (17:25:28Z → 17:26:07Z) : **28 tuées pour
la raison attendue sur 28** (code 0 ; par origine : banc v1 porté 17/17, porté sur la v2 1/1, neuves 10/10 ;
`mutations-remplacement-juge-v2.json`, `.txt`).

## 7. Ce qui n'est pas corrigé ou pas vérifié

- **Le défaut reste dans les fichiers gardés tels quels (R12)** : `pole/ideation_v2.py` (l. 2852), `pole/ideation.py`
  (l. 2847), `pole/bras_remplacement_juge_v1.py` (l. 255), `demonstrations/ideation_v2.py` et `ideation_v1.py`. Qui les
  appelle directement y reste exposé : la relance doit appeler `pole.bras_remplacement_juge_v2.executer_bras_differe` (ou un
  lanceur neuf qui l'appelle) et ne plus épingler la v1 comme point d'entrée.
- Aucune exécution avec une vraie commande, un vrai relais ni le modèle joué : tout est simulé, hors ligne.
- Le lanceur de démonstration ne passe toujours pas l'option de remplacement (voir 4) ; ses gardes propres
  (`verifier_commande_externe_reelle`, `--modele-servi-externe-permis`) ne sont pas éprouvées avec le modèle joué.
- `outils.manifeste` empreinte chaque `.py` de `pole/` : un manifeste écrit depuis l'arbre `71417ad1…` porte une entrée de
  plus (`bras_remplacement_juge_v2.py`) que depuis `3c6cff30…`, avec ou sans option (effet de tout fichier neuf).
- Les exceptions levées sont celles de `pole.ideation_v2` (importé) : une instance chargée à part a d'autres classes.
- Quatorze fichiers d'essais non collectés (scipy absent), à la base comme à la tête ; essais du vrai bac joués ici sans concurrence, aucun échec du bac à la tête ni à la base.

## 8. Ce que la session de relance doit épingler (après contre-lecture)

- Commit de l'orchestrateur **`8a2a6ac9d3feb52e6771edca52f440dd780fb373`** (parent `0861800260e33224a71f48b111e72ac04288d3cb`,
  base `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`), arbre `orchestrator/` **`71417ad17d816af07a6a57e9dc28bbfac07faac5`** (au
  lieu de `3c6cff30…`), `orchestrator/pole` `bfd85856…` ; paquet `orchestrateur-remplacement-juge-v2.bundle` (prérequis
  `a41b7b50`).
- Point d'entrée : **`pole/bras_remplacement_juge_v2.py` `83a08aee…`**, qui appelle `pole/bras_remplacement_juge_v1.py`
  `2efd6b08…` (avec option) et `pole/ideation_v2.py` `67d2ad35…` (sans option) — les trois empreintes à épingler ensemble.
- L'appel : celui du rapport v1 (§ 8), module `pole.bras_remplacement_juge_v2` : `executer_bras_differe(SORTIE,
  attestation_lecture_humaine=…, juges_externes=[("astra-juge", <modèle joué>, <adaptateur>)], budgets={…, ("juge_ideation",
  <modèle joué>): <plafond>}, remplacements_juges_externes={"astra-juge": {"modele_course", "modele_joue", "reference_go",
  "mot_verbatim"}}, …)` ; **une seule entrée par étiquette** (sinon refus `étiquettes de juges externes en double`, rien lu,
  rien appelé).
- En ligne de commande, si la relance passe par un lanceur de démonstration : `demonstrations/ideation_v2_juges_externes_uniques_v1.py`
  `1fbe2be3…` (qui charge `demonstrations/ideation_v2.py` `bc5e9c98…`), jamais `ideation_v2.py` seul ; ce lanceur n'offre pas
  l'option de remplacement.

## 9. Pièces livrées (dossier `docs/notes/organisme-remplacement-juge-v2/`, chacune scellée)

Liste et empreintes : `empreintes-orchestrateur-remplacement-juge-v2.txt` (bloc gelé provisoire).
