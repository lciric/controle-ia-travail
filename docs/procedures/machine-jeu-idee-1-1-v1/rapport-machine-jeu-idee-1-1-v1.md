# Rapport : machine louée du jeu relancé de l'idée 1.1 — conception, écriture, répétition (v1)

- **Auteur** : développeur neuf, modèle A ; n'a écrit ni l'addendum de relance, ni le code du jeu, ni aucune pièce de B bis.
- **Heures (UTC, `date -u`)** : début 20:42:32Z ; répétition finale 21:17:12Z à 21:19:20Z ; rédaction jusqu'à 21:25Z environ.
- **Tâche** : GO-2026-11-16-09 point (2) et R-3014 (« devis et procédure de la machine du jeu de l'idée 1.1, contre-lus,
  puis ligne « calcul » inscrite par la mère sur ce devis »).

## Verdict

**Procédure prête pour la contre-lecture, répétée hors ligne sans écart : 110 cas sur 110** (sortie gardée
`sortie-repetition-machine-jeu-idee-1-1-v1.txt`, `1ae90d92…`). Aucun appel au loueur, aucune machine, aucune dépense, aucun
commit. Trois points relèvent de la mère avant tout feu : l'écart **D7** (machine louée contre [T] l. 629 et 660), le
**commit** de l'addendum de relance sur `main`, la **ligne de GO** de type « calcul » (plafond proposé 3,5 USD).

## 1. Pièces produites (dossier `docs/procedures/machine-jeu-idee-1-1-v1/`, chacune scellée par un compagnon)

| Fichier | sha256 | Rôle |
|---|---|---|
| `lancer_jeu_idee_1_1_machine_v1.sh` | `3ef1d9a6d3a99149ba5f9ac062e824e4944ac87321d5eed0b11b94bc18905e0c` | côté session : offre, création, commande imprimée, contrôle de la ligne, inventaire, prix relu, dépense, destruction, preuve |
| `garde_machine_jeu_idee_1_1_v1.py` | `b099a05712dc96ed44121e9caf9e4633af8cfb7710f59724eaae6c92783f1e8a` | gardes appelées par le lanceur (Python seul, `-I`, sans réseau) |
| `amorce_jeu_idee_1_1_v1.sh` | `ede38bb696ac33e9e2871441852b296deaf6855f3adeee743861a45bccc984f7` | côté machine (§ 1 de la procédure) |
| `repetition_machine_jeu_idee_1_1_v1.sh` | `f596aac33d94d2bad8bed8fa1ad6ce2decedf0ace8b0d75b2661c6b1bc264759` | répétition locale |
| `jeu_factice_idee_1_1_v1.py` | `c9863b0d850d9f50c2bed5b8c2fb1330c7ed47bccb3c86a3f2a2814d39c3d459` | jeu jouet (sorties scellées factices) |
| `sortie-repetition-machine-jeu-idee-1-1-v1.txt` | `1ae90d92a784cac0bfa222d4db6fa4b66928230fe298b9e437f25df59ee3876a` | sortie gardée de la répétition finale |
| `procedure-machine-jeu-idee-1-1-v1.md` | `0d674c39dea0b4e264b59c3ff235903efe488c36ff8cd8b410166aa2bd4e04bc` | gestes de l'opérateur, rôle de la mère, leçons de B bis |
| `devis-machine-jeu-idee-1-1-v1.md` | `1ae229ebac9f14e729121b5d04bf04ac169d3eb3ad17909592924a63de62758a` | prix relevés hors ligne, durées, attendu et pire cas |

Le jeu factice et la garde Python s'ajoutent aux pièces demandées (le jeu factice était demandé dans son principe ; la garde
sort du script de lancement le code Python que B bis gardait dans `registre_bbis_v1.py`).

## 2. Choix de conception (et écarts au modèle de B bis)

1. **Exactitude numérique** : image `python:3.13.18-bookworm` — nom **vérifié** sur Docker Hub à 20:49Z (étiquette présente,
   condensé de l'index `sha256:cc55e4de…`, image amd64 `sha256:2784af83…`, 382 664 644 octets, poussée le 2026-11-06) ;
   environnement neuf ; `pip install --no-cache-dir numpy==2.4.6 scipy==1.17.1 pytest==9.1.1` ; contrôle des versions de 4.2
   (`3.13.18 2.4.6 1.17.1`) par l'interpréteur du lancement, arrêt **avant tout calcul** sinon (répété : numpy 2.5.3 →
   arrêt, aucun clone). Aucune voie de repli vers une autre image : si l'étiquette manquait au moment du feu, l'amorce
   s'arrêterait à la vérification de Python (ou l'image ne démarrerait pas : règle des 30 minutes, geste 11).
2. **Paquets suffisants, par analyse statique** : 45 fichiers parcourus depuis le lanceur, `tests/conftest.py`, les sept
   essais du jeu et les 46 fichiers gelés ; 19 modules du pôle chargés par le juge et la vue v9 : seuls `numpy`, `scipy`,
   `pytest` sont tiers ; `claude_agent_sdk` n'est importé que paresseusement par `adaptateurs.py` au lancement réel d'un
   moteur, jamais par ce jeu. Les essais n'emploient git que dans des dépôts jetables dont ils posent l'identité.
3. **Offre avec ou sans carte**, choisie par la garde jouée hors ligne sur chaque offre (R-2998) ; `cpu_arch` = `amd64`
   exigé (mêmes roues que le conteneur) ; fiabilité ≥ 0,98 (`reliability2` et `reliability`, le plus petit) ; ≥ 100 Mb/s ;
   prix garde ≤ 0,06 USD/h. Les noms des champs (`cpu_arch`, `reliability2`, `storage_cost`, `inet_down`, `num_gpus`, …) sont
   ceux de la recherche gardée de B bis (`/home/user/bbis-course-envoi-v3/recherche.json`, noms et quelques valeurs non
   secrètes relevés, aucune clé).
4. **Branche de sortie orpheline**, dans un dépôt de sortie à part : elle ne reçoit que les traces, `runs/<run>/` et
   `diag/organisme-idees-juge-v1/<run>/` ; la poussée n'emporte jamais l'arbre du dépôt (B bis créait la sienne depuis le
   commit) ; le dépôt du jeu ne peut pas pousser (adresse de poussée invalide, répété) et son arbre reste propre (le jeu
   l'exige). Un verrou (`flock`) sérialise les poussées du suivi, de la minuterie et de la fin.
5. **Première poussée avant tout calcul** et **suivi chaque heure** (`etat.txt` : comptes de fichiers et dates de fichiers,
   jamais un contenu) ; PID poussé dès le lancement.
6. **Minuterie** : échéance 49 h 45 après l'impression, non 48 h (raison au devis, § 3 : la borne de 48 h du texte court
   depuis `depart.json`) ; **écart à la lettre de la tâche (« minuterie de 48 h »), déclaré, à trancher par la mère** ; TERM au
   jeu par son PID seulement s'il a passé sa borne (répété dans les deux sens) ; destruction redemandée sans fin, jamais jugée.
7. **Ligne de création plus courte** : amorce compressée (`gzip -9 -n`) avant le base64 : ≈ 11 900 caractères au lieu de
   32 700 (B bis) ; sous-commande `controle-ligne` (amorce décodée et décompressée égale à l'octet ; répétée sur une amorce
   différente d'un octet et sur une sortie coupée).
8. **Réponse du loueur dans un fichier** (`umask 077`) dont seuls `success`, `new_contract` et les noms des clés
   s'affichent (R-3002, R-3004 : clé propre à la machine en clair) ; à effacer après la preuve de destruction.
9. **Garde de création** lisant la ligne de GO comme le crochet de garde la lit (8 colonnes, type « calcul », Lazar, période,
   révocation) **et** son périmètre (« idée 1.1 ») et son plafond ; ligne du feu citant GO, commit et étiquette.
10. **Garde de destruction** : identifiant égal à `id-machine.txt` (lu de l'inventaire), dix machines d'autres tâches
    refusées (dont B bis 60953606, vivante à 20:18Z, R-3011).

## 3. Répétition (sortie gardée ; 110 cas, 0 écart ; dépôt jouet en `file://`, loueur simulé)

- **Session, offre (19 cas)** : la moins chère acceptée retenue ; dix offres fautives refusées une à une (prix, amd64, cœurs,
  mémoire, fiabilité, carte booléenne, clé absente, stockage, disque, débit) ; offre sans carte acceptée ; fichier jamais
  réécrit ; aucune offre acceptée ; identifiant en double ; relecture saine, autre identifiant, prix altéré.
- **Session, création (11 cas)** : feu sain ; forme longue ; GO de décision, échu, révoqué, sans l'idée 1.1, plafond illisible,
  non accordé par Lazar ; ligne du feu sans le commit, absente ; seconde relance.
- **Session, commande et ligne (16 cas)** : cas sain ; amorce décodée égale, formes de la ligne, aucune clé ; `controle-ligne`
  sain, amorce différente, sortie coupée ; inventaire (identifiants et étiquettes seulement, triés) et liste illisible ; commit
  hors de main, compagnon de relance faux, sortie antérieure de ce jeu, essai du § 6 point 3 altéré, empreinte de relance
  différente, échéance trop courte, feu sous un GO de décision, dossier d'envoi déjà employé.
- **Session, prix, dépense, destruction (13 cas)** : prix relu sain, trop cher, à virgule ; dépense sous le plafond et au
  plafond ; destruction par l'identifiant lu, autre identifiant, B bis, illisible ; preuve saine, toujours listée, témoin
  absent, liste illisible.
- **Machine (48 cas)** : essai local sans écriture ; variable de répétition hors répétition ; quatre arguments fautifs sans
  dossier écrit ; **cas sain** (versions lues `3.13.18 2.4.6 1.17.1` par l'interpréteur de la session, jeu factice mené au
  bout, quatre suivis intermédiaires, sorties égales à l'octet, branche orpheline aux seuls chemins permis, « stopped »
  demandé, aucune destruction avant l'échéance, dépôt du jeu sans poussée) ; versions fausses (arrêt sans clone, traces
  poussées) ; commit hors de main ; compagnon faux ; empreinte différente ; sortie antérieure ; essai altéré ; disque ;
  marge de la borne (jeu non lancé) ; arrêt écrit du jeu (`arret.json` poussé) ; compagnon de sortie faux ; fichier hors des
  dossiers du run (nommé, non poussé) ; minuterie au-delà de la borne (TERM par le PID, `arret.json`, six destructions par
  l'identifiant, « stopped » après la cinquième) ; minuterie dans la borne (aucun TERM) ; branche de sortie existante (non
  touchée) ; fonction de poussée seule (chemin hors, fichier trop gros, cas sain).
- **Clés (3 cas)** : clés factices absentes de toutes les sorties, de tous les fichiers des machines jouets et de toutes les
  branches poussées ; aucun processus de la répétition encore vivant (arrêts par PID seulement).
- **Durées raccourcies en répétition** (variables refusées hors répétition) : échéance, marges, période du suivi, pas,
  pause, borne de 48 h ; la logique est celle de la machine, les constantes non.

## 4. Ce que la répétition n'a pas éprouvé

1. Le loueur réel : recherche, création, état « stopped » et destruction par l'interface (`PUT` et `DELETE` sur
   `/api/v0/instances/<id>/`, clé `CONTAINER_API_KEY`), forme des offres sans carte : non joués (consigne). Mêmes appels que
   l'amorce de B bis, qui a tourné (R-3002 à R-3004).
2. L'image réelle, `pip install` depuis l'index public, le clone et la poussée sur le dépôt distant avec le jeton (aide
   d'authentification de B bis, inchangée), la durée de la mise en place.
3. Le vrai jeu (aucun calcul ici) ; ses essais sur un clone partiel (l'arbre est complet au commit ; seule l'histoire n'a pas
   ses contenus ; les essais n'emploient que `rev-parse` et `status` sur le dépôt).

## 5. Réserves

1. **D7** : l'addendum de relance (4.10 (ii)) ne laisse partir aucune machine louée sans le mot de Lazar sur D7, consigné à
   `registres/go.md`. GO-2026-11-16-09 dit « option (a), relance du jeu sur une petite machine de calcul louée » : la mère dit
   s'il vaut ce mot (lecture probable) et l'écrit.
2. **Ordre de 4.4 et 4.5** (« notés au registre avant le lancement », « PID noté dès le lancement ») : sur la machine, ces
   faits sont **poussés** avant et au lancement, et transcrits au registre par la mère ensuite : écart de forme à accepter
   dans le feu.
3. **Bit près** : autre processeur, autre système (Debian 12 de l'image contre Ubuntu 24.04 du conteneur), autre
   bibliothèque mathématique possible ; limite déjà déclarée par l'addendum de relance (4.2) ; les traces gardent `lscpu` et
   `numpy.show_runtime()`.
4. **Clone partiel** : la répétition montre qu'un commit absent de `main` peut être rapatrié à la demande par son
   empreinte ; la garde qui tient est « ancêtre de `main` » (répété), non « présent ».
5. **Fils oisif** : le TERM au parent prévu par l'addendum d'empreintes n'est pas joignable depuis la session ; le geste 12
   en fait un nœud de la mère (destruction = run invalide sans `arret.json`).
6. **Clés** : `GH_TOKEN` reste dans la configuration de la machine jusqu'à sa destruction (comme B bis) ; la réponse de
   création reste dans le dossier d'envoi jusqu'au geste 16.
7. **Minuterie de 49 h 45** au lieu de 48 h (§ 2, point 6).
8. **Non contre-lu** : cette procédure et ce devis attendent leur contre-lecteur neuf (R2) ; le crochet de garde n'a pas été
   simulé sur la ligne imprimée (son motif a été lu dans son code).

## 6. Déclaration

- **Rôle** : développeur neuf de la procédure de la machine du jeu relancé de l'idée 1.1 ; **lettre de modèle : A**.
- **Pièces lues** (empreintes recalculées) :
  - arbre `/home/user/controle-ia-travail/.claude/worktrees/agent-a4f221610ce6d5a67` : `scripts/lancer_bbis_v3.sh`
    `dc26ea01…`, `scripts/amorce_bbis_v3.sh` `18e2f205…`, `src/controle_ia/t07bbis/registre_bbis_v1.py` `c3b1848b…`,
    `brouillons/T0.7-etape-B-bis-v1/contre-lecture-creation-bbis-v1.md` `3a3e7270…`, entiers ;
  - `registres/decisions.md` : R-2996 à R-3004, R-3006, R-3009 à R-3011, R-3014, R-2961, R-2968 (lignes seulement) ;
    `registres/go.md` : en-tête, GO-2026-11-16-09, GO-2026-11-14-14, lignes de révocation (début) ; `registres/arrets.md` :
    lignes 130, 131, 134 (début) ;
  - `scripts/jouer_idee_1_1_v5.py` `c116a4bf…` entier ; `src/controle_ia/organisme_idees_juge/execution_idee_1_1_v5.py`
    `8542a484…` (constantes, l. 100-262) ; `src/controle_ia/gardes.py` `a83c48ce…` (l. 85-115) ; `src/controle_ia/manifeste.py`
    `1a5c7464…` (appels à git) ; `juge_v1.py` et `vue_v9_v2.py` (chargements dynamiques) ; `tests/conftest.py` ;
  - `prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-empreintes-v1.md` `73ea3bf3…` (l. 355-420) ;
    `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-1-v1-brouillon3.md` `7b11231c…` (l. 170-300 et une recherche
    de mots) ; `.claude/hooks/garde_calcul.py` `73be0638…` ;
  - `docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/verification-differentiel-procedure-pilote-mr2-v74-machine-v13-v1.md`
    (recherche de mots) ; recherche gardée `/home/user/bbis-course-envoi-v3/recherche.json` (noms de champs et valeurs non
    secrètes de neuf offres).
- **Jamais ouvert** : rien du run invalide (`/home/user/jeu-idee-1-1-copie-v1`, pas même les noms) ; rien sous `diag/`,
  `runs/`, `donnees/` du dépôt ; rien de 7a, 7b, T0.6, T0.7, P3-bis, du bras d'attaque ; de B bis, ses seuls scripts de
  lancement et la contre-lecture de sa création. Aucune valeur de clé ; aucun `env`, `printenv`, `set`, `export -p`.
- **Accès extérieurs** : une lecture publique de Docker Hub (étiquette de l'image), sans aucune donnée du programme ; aucun
  appel au loueur ; aucune machine ; aucune dépense ; aucun commit, aucune poussée vers un dépôt réel ; git du dépôt principal
  en lecture seule (`git show HEAD:<chemin>` de trois fichiers et compagnons, `count-objects`, `status`, `log -1`).
- **Calcul** : léger (répétitions de 2 à 3 minutes, quatre fois) ; dossiers jetables dans le bloc-notes.
- **Incidents** :
  1. **21:13Z** : une commande d'édition à double document en ligne s'est terminée trop tôt (un `EOF` intérieur a fermé le
     document extérieur) ; les lignes restantes ont tourné comme shell, variables vides : aucun fichier du dossier modifié,
     mais **deux fichiers parasites écrits à la racine du système : `/s.txt` (34 octets, un message d'erreur) et
     `/commande-coupee.txt` (0 octet)**. Leur effacement a été refusé par une garde de sûreté de l'outil ; je ne l'ai pas
     contourné : **à effacer par une personne**. L'édition a été refaite par un script écrit dans le bloc-notes.
  2. Première répétition : trois écarts de la répétition elle-même (nom de branche `v0` hors de la forme, motif du commit hors
     de main, processus mourant compté vivant), corrigés dans la répétition ; deuxième et troisième : 0 écart.
  3. Aucune commande refusée par le crochet de garde ou le classifieur ; aucun processus arrêté hors de ceux de la répétition,
     par leur PID.
