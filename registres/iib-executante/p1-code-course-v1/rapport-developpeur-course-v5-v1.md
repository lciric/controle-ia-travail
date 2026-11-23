# Rapport du développeur — code de la course de l'organisme retenu du saboteur à budget, version 5 (P1) — v1

Date : 2026-11-22. Pièce d'instrument (classe B), à contre-lire par un autre modèle. Développeur : Claude Opus 5.5, côté saboteur.
Rien poussé, aucune dépense, aucun loueur, aucun modèle externe, aucune machine. Aucune pièce interdite ouverte : ni consigne
privée, ni conception d'origine, ni branche d'essai, ni résultat de course ou de mesure (seuls les jouets des essais, dans des
dossiers temporaires). Journal du loueur lu par `grep -iE 'git|push|fatal|error|denied|remote|branch|auth'` seulement.

- Base : `c97231b38` (arbre `d1cc1d75…`), copie de travail détachée `…/scratchpad/p1`, commits locaux jamais poussés.
- **Tête : `ae1c76aa172515ab0c820efabcefc118afecd8ab`, arbre `1b395646c2df70bf8181290fcf24ca38cd5a4f40`.**
- Correctifs : `0014` à `0017` (`git format-patch --start-number 14 c97231b38..HEAD`), à côté de ce rapport.

## 1. Diagnostic de la poussée par lot

**Cause : aucune poussée n'était prévue pendant le run.** Ce n'est ni l'authentification, ni la branche, ni le chemin.

- `lanceur_v5.phase_etalonnage`, fonction `verser` : écrit et scelle chaque lot sur le disque (`diag/<run>/lots/`, `donnees/<run>/lots/`), émet une marque de progrès, et rien d'autre. Aucun appel à git.
- `scripts/amorce_instance_iib_v5.sh` ne pousse qu'à cinq moments : la poussée initiale de la branche (avant l'installation), la fin normale du run, la sortie en erreur du lanceur (`consigner_arret`), la minuterie (dépense épuisée, échéance) et un second démarrage. Entre la poussée initiale et la fin du run, rien.
- L'en-tête de l'amorce disait « données légères poussées, lot par lot », et la documentation du lanceur « versé par lot » : vrai pour le versement sur le disque, faux pour la poussée. La note de lecture du 22 novembre (`note-lecture-code-versement-coupure-rythme-v1.md`, point 1) l'avait déjà vu au commit de lancement.
- `supprimer_apres_versement` n'est en cause : jamais appelée pendant l'étalonnage, elle ne supprime rien.
- Journal du loueur (lignes filtrées seulement) : clonage, puis « branche essai/iib-explo-v6 poussée avant l'installation (droit d'écriture éprouvé) » à 23:30:08Z, puis **aucune ligne git, push, fatal, error ou denied**. Le jeton marche ; la poussée n'a simplement jamais été demandée. À noter : ce journal porte `COMMIT=43d6d0673…`, non `c97231b38`.
- **Ce qui reste possible pour la machine en cours** (je n'ai rien fait) : les lots sont scellés sur son disque. Si la surveillance la coupe à 16 USD, c'est l'arrêt par l'identifiant, sans consignation. Pour pousser, il faut redémarrer : l'amorce prend le chemin « redémarrage d'un run interrompu », consigne et pousse, puis refuse et demande la destruction. Il faut donc le mot de la mère. Autre voie, si elle est permise : faire jouer `bash /root/iib-consigner.sh "rattrapage"` sur la machine vivante. À trancher par la mère.

## 2. Corrections, une par correctif

### 0014 — poussée de chaque lot dès qu'il est scellé
- **`src/controle_ia/iib/versement_v5.py`** (neuf), `Versement` (l. 25) :
  - appelle le **vrai** script de consignation de l'amorce (`IIB_CONSIGNER`, motif « versement … ») ;
  - puis **vérifie lui-même** (`verifier_sur_la_branche`, l. 51) que les fichiers du lot sont suivis par git (`ls-files --error-unmatch`), propres (`status --porcelain --ignored`), et que `HEAD` est égal à `refs/remotes/origin/<branche>`. Un script qui dit 0 sans pousser est vu.
  - Chaque issue donne une marque de progrès (`etape=versement poussee=faite|refusee cause=… refus_de_suite=k`), conforme à `MOTIF_PROGRES`, hors `MOTIF_INTERDIT`, donc relayée par l'amorce. Un refus écrit aussi « VERSEMENT REFUSÉ » sur la sortie d'erreur, et la liste des versements va dans `resume.json` ou `arret.json`.
  - Si le délai de 3 000 s est dépassé, le groupe du script est arrêté par son identifiant de groupe (`killpg`, l. 89 ; R10).
- **Décision, avec sa raison** :
  - un refus isolé ne fait rien d'autre que se dire : le lot reste scellé sur le disque, et la consignation suivante pousse tout ce qui manque (essai de reprise) ;
  - **trois refus de suite** (`REFUS_CONSECUTIFS_MAX`, l. 21) lèvent `GardeArret` : le lanceur écrit `arret.json`, l'amorce consigne une dernière fois puis arrête la machine par son identifiant. L'état est « stopped », le disque est gardé.
  - Pourquoi ni réessayer sans fin ni arrêter au premier refus : arrêter au premier refus perdrait un étalonnage payé pour un incident passager de GitHub (le script fait déjà trois tentatives par consignation). Continuer sans borne accumulerait du travail jamais versé, ce que l'ordre veut empêcher. Trois lots de suite, c'est une demi-heure à deux heures de travail au plus.
- **Mode réel** : `IIB_CONSIGNER` est exigé, et son absence est un refus avant tout calcul (`Versement.__init__` ; `phase_etalonnage`, garde « sans poussée par lot »). En mode jouet sans script, c'est dit (`poussee=sans_script`).
- **`lanceur_v5.py`** :
  - `executer` construit le `Versement` avant le manifeste ;
  - `verser` l'appelle après le sceau des deux fichiers du lot (l. 284) ;
  - la documentation est corrigée.
- **`scripts/amorce_instance_iib_v5.sh`** : la ligne du lanceur reçoit `IIB_CONSIGNER="$R/iib-consigner.sh"` (l. 415). La l. 321 n'ajoute pas de trace de journal par lot quand le motif est « versement … ». L'en-tête porte (g).
- **Essais** : la garde statique « aucun sous-processus dans les modules v5 » (`test_aucune_suppression_ailleurs_dans_le_code_v5`) est resserrée et non levée. `versement_v5.py` seul a le droit d'en lancer, et seulement `bash <script> "versement …"` et `git` en lecture seule (`ls-files`, `status`, `rev-parse`). Le détecteur est éprouvé sur deux artefacts.
- **Listes** : liste figée v6 (`scripts/tests-cibles-iib-v5-v6.txt`, 25 fichiers, `f7838455…`), empreinte écrite en dur dans l'amorce. Le différentiel borné à l'amorce v1 passe de 10/9 à 11/10 lignes.

### 0015 — point d'entrée de la course, versement par tour
- **`lanceur_v5.executer` en phase `course`**, et `--phase course --etalonnage <run>` en ligne de commande (`_executer_course`, l. 718) :
  - refuse si le run de l'étalonnage est illisible, si la désignation est absente, ou si `--etalonnage` est donné hors de la course ;
  - **la configuration passée doit être celle que le manifeste de l'étalonnage a scellée**, à empreinte canonique égale (`exiger_configuration_de_l_etalonnage`, l. 700). C'est le reste noté au rapport v3 : « rien ne compare » ;
  - en mode réel, il construit `distillation_v5.distillateur_du_mode_reel` avec les identifiants des lots de l'étalonnage (`donnees/<run>/lots/ids-lot-*.json` : sans eux, les faux positifs seraient « non calculés »), puis passe **`d.modele`, le modèle surveillé**, à `phase_course` ;
  - en mode jouet, il prend le distillateur jouet, avec les motifs factices `MOTIFS_JOUET` (`jouet_distillation_v5.py`, l. 25) ;
  - il écrit `runs/<course>/manifeste.json`, puis `diag/<course>/resume.json`, ou `arret.json` en cas d'arrêt.
- **`phase_course`** (l. 407) :
  - en mode réel, refus sans distillateur ou sans poussée (l. 417) ;
  - **second passage refusé avant le premier tour** (`exiger_course_non_jouee`, l. 397). Avant, il jouait tous les tours avant de buter sur un fichier existant ;
  - **chaque tour** est écrit, scellé (`tours/tour-NNN-maitre.json` pour les lignes de l'oracle de la règle, `ids-tour-NNN-maitre.json` pour les identifiants) et poussé (l. 451) ;
  - une marque de progrès neutre par tour, par `apres_tour` (l. 466) : numéro, épisodes joués, replis. **Aucun compte d'acceptés.** Lecture prudente du cloisonnement : un compte d'acceptés est un résultat, et l'étalonnage n'en relayait aucun ;
  - poussée après les témoins, après la distillation (les adaptateurs font environ 27 Mo en demi-précision pour un modèle de 8 milliards de paramètres, rang 16 (estimation, non mesurée), sous la limite de 90 Mo de l'amorce), et à la fin.
- **`evaluer`** (l. 519) : pour chaque condition, `evaluation/ids-evaluation-<c>.json` après la génération et `evaluation/oracles-evaluation-<c>.json` après les oracles, chacun scellé et poussé.
  - Les oracles sont joués condition par condition, dans le même ordre et sous les mêmes clés qu'avant (clés par phase et épisode).
  - Le fichier d'ensemble reste le même : l'essai vérifie que la réunion des fichiers par condition est égale à `evaluation-iib-v5.json`, et celle des tours à `oracle-course-iib-v5.json`.
- La documentation du lanceur ne dit plus « distillateur non écrit » (n3 du distillateur ; reste 3 du rapport v4).

### 0016 — replis de la forme du lot des suites écrits
- La note de lecture du 22 novembre (point 3 (b)) l'avait vu : `modele_v1` consigne un repli de `cache_duplique` vers `prerempli_par_suite` dans `modele.replis`, mais la version 5 ne l'écrivait nulle part, si bien qu'un repli était silencieux.
- `replis_de` (l. 166) les écrit au résumé et à l'arrêt de l'étalonnage et de la course, aux rapportés de l'étalonnage, à la course et à l'évaluation. Chaque marque de lot et de tour les compte (`replis=N`).

### 0017 — amorce de la course
- **`scripts/amorce_instance_iib_course_v5.sh`** (neuf, R12), tirée de l'amorce de l'étalonnage, avec cinq changements déclarés et bornés par un essai (5 lignes retirées, 8 ajoutées hors commentaires) :
  - (c1) le lanceur est joué en `--phase course … --etalonnage "$RUN_ETAL"` ;
  - (c2) le run de l'étalonnage est lu sur l'unique `diag/*-iib-*/designation-iib-v5.json` scellé du commit ; s'il n'y en a aucune, ou plusieurs, c'est un refus ;
  - (c3) le run est nommé « iib-course », et `diag/<étalonnage>/` est consigné à la fin ;
  - (c4) la liste figée de la course, `tests-cibles-iib-course-v5-v1.txt` (`7c4757fa…`), est la v6 plus l'essai du moteur à torch, qui se joue sur la machine de la course (torch, transformers et scipy sont dans `requirements-gpu.txt`) ;
  - (c5) le journal dit « course ».
- **`scripts/lancer_iib_v3.sh`** (l. 82-83) : `IIB_AMORCE=scripts/amorce_instance_iib_course_v5.sh` choisit l'amorce de la course, et toute autre valeur est un refus (code 2). La surveillance lit alors la phase « course », et la règle de coupure de l'étalonnage ne joue pas.
- **`scripts/repetition_locale_iib_v5.py`** : la répétition joue maintenant aussi la course jouet par l'amorce de la course, choisie par le lanceur de session. Contrôles, création imprimée, amorce en essai local, quatre tours poussés un par un, évaluation par condition, après-création, surveillance « phase course ». `ATTENDUS = 288`.

## 3. Essais

- **Liste figée v6 rejouée entière** (`sortie-essais-p1-v1.txt`) : **288 réussis**. C'est la liste que l'amorce exige ; `TESTS_ATTENDUS=288` pour l'étalonnage.
- Pour la course, la liste de la course sur une machine qui a torch donne **290** (288 plus les 2 essais du moteur). Sur ce poste, sans torch, l'essai du moteur se saute : « 288 passed, 1 skipped » n'y passerait pas le contrôle. Il n'a donc toujours pas été joué.
- **Répétitions locales** (suite courte dans l'amorce) :
  - `sortie-repetition-locale-0014-courte-v1.txt` : 28 poussées par lot, vérifiées ;
  - `sortie-repetition-locale-0017-courte-v1.txt` : étalonnage, conditions, puis course par l'amorce de la course, code 0.
- **Essais ajoutés** :
  - `tests/test_iib_versement_v5.py` (neuf, 8 essais), sur le vrai script de consignation tiré de l'amorce et une origine nue locale :
    - cas sain : 28 lots, un commit par lot, aucune trace par lot ;
    - marques relayables ;
    - artefact « l'origine refuse » : trois refus, arrêt, lots scellés sur le disque, journal de l'amorce ;
    - artefact « script qui rend 0 sans pousser » : `tete_non_poussee`, `fichier_non_suivi` ;
    - refus isolé puis reprise ;
    - délai dépassé : le groupe arrêté, son fils compris ;
    - mode réel sans script : refus ;
    - texte de l'amorce.
  - `tests/test_iib_distillation_bout_en_bout_v5.py` (+3) :
    - point d'entrée de la course par la ligne de commande, de bout en bout (étalonnage, conditions, course), chaque tour poussé dans son commit, réunions égales aux fichiers d'ensemble, marques neutres ;
    - refus avant le premier tour : sans `--etalonnage` ou s'il est illisible, `--etalonnage` hors de la course, second passage, configuration différente du manifeste ;
    - en mode réel, refus sans distillateur ou sans poussée.
  - `tests/test_iib_lanceur_v5.py` (+2, et 3 essais adaptés) :
    - replis écrits (artefact planté, cas sain) ;
    - amorce de la course : différences bornées, liste, phase lue « course », `IIB_AMORCE` inconnue refusée ;
    - essais adaptés : garde statique resserrée, liste v6 et compte, ligne `--phase course` désormais refusée sans `--etalonnage` (code 1 au lieu de 2).

## 4. Ce qui reste ouvert, et nœuds

1. **L'essai du moteur à torch du distillateur n'a jamais été joué** (`tests/test_iib_distillation_torch_v5.py` : `MoteurTorch`, injection, entraînement, sauvegarde et recharge, doses). Il est dans la liste de la course, donc il se joue dans les premières minutes de la machine de la course. Mieux, avant l'ordre : sur un poste à processeur qui a torch.
2. Toujours non éprouvés : le mode réel (modèle, `MondeReel`, `motifs_de_la_course`, qui demande scipy), l'amorce de la course sur une vraie machine, la poussée contre GitHub (seulement contre une origine locale).
3. **Nœud C1, une ou deux machines.** Le devis dit « une seule location », mais l'amorce de l'étalonnage finit en « stopped », et son second démarrage ne relance rien. J'ai écrit la course pour une **machine neuve**, sur un commit qui porte l'étalonnage et la désignation versés. Coût de plus, hors du coût fixe scellé : une installation et un téléchargement, environ 2 USD et 10 minutes, à prendre sur la réserve de 10 USD. À trancher par l'ordre ou par Lazar. Reprendre la même machine demanderait une amorce neuve.
4. **Nœud C2, accord de la course.** La course joue sous le `go_id` de la configuration de l'étalonnage : `exiger_accord` l'exige, et la configuration ne peut pas changer, puisque la garde neuve exige l'empreinte du manifeste de l'étalonnage. Une ligne de GO distincte pour la course serait refusée. Si Lazar veut une ligne neuve, c'est un nœud (configuration de course scellée à part, ou garde relâchée), que je n'ai pas codé.
5. **Calendrier** : la configuration v2 porte `dernier_jour_creation` au 2026-11-26. La machine de la course doit être créée au plus tard ce jour-là, sinon il faut une configuration et un devis neufs.
6. **Lecture (pas codée) des graines de la course** : le texte, section 14, dit « la course dérive ses clés de la même entropie sous un préfixe propre ». Le code garde le préfixe de la configuration ; les clés de la course (`iib/maitre/…`, `iib/temoin/…`, `iib/evaluation/…`, phases « maitre » et « evaluation-* » dans les clés du jumeau) sont disjointes de celles de l'étalonnage par leur nom, et ce sont les clés de `lanceur_v1`. Ajouter un suffixe changerait les tirages de la course et du distillateur. À juger par le contre-lecteur. Si « préfixe propre » doit se lire à la lettre, c'est un nœud.
7. **Première action dans la perte : « gardée »**, portée par la configuration scellée v2. Le rapport v4 la disait « à confirmer par le mot de Lazar ». Je n'ai pas vérifié ce mot (registres non lus). Ce point est pour la mère.
8. Ce que l'ordre de la course devra porter :
   - `IIB_AMORCE=scripts/amorce_instance_iib_course_v5.sh` ;
   - une branche neuve (`IIB_BRANCHE`) ;
   - le commit qui porte l'étalonnage et la désignation ;
   - `TESTS_ATTENDUS=290` ;
   - la machine neuve ou non (C1) ;
   - la ligne de GO (C2).
9. Les états intermédiaires 0015 et 0016 portent `ATTENDUS = 283` dans la répétition : seule la tête est juste (288).

## 5. Livrables
- `0014-…patch` à `0017-…patch` ;
- ce rapport ;
- `sortie-essais-p1-v1.txt` ;
- `sortie-repetition-locale-0014-courte-v1.txt` ;
- `sortie-repetition-locale-0017-courte-v1.txt`.

Arbre final : `1b395646c2df70bf8181290fcf24ca38cd5a4f40`.
