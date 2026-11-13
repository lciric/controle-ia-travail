# Consigne : session du poste local de Lazar — outillage Lean D-1a, troisième essai (GO-2026-11-10-13) — v3, brouillon 1

Brouillon 1, écrit le 2026-11-13 vers 03:23 UTC (heure relevée par `date -u`) par le développeur du harnais v10 (Claude
Opus 5.5), sur demande de la session mère ; modèle : `consigne-poste-local-lean-d1a-v2.md` (`af1d8ae3…`). **Non scellé
comme consigne** : la mère le relit, remplit les marqueurs `⟦MÈRE : …⟧`, en tire le texte final sous un nom neuf.

Session mère `⟦MÈRE : identifiant de la session mère⟧` (dans le nuage), sur le mot de Lazar R-2439 (« Réparer d'abord, puis
relancer » : troisième essai sous GO-2026-11-10-13, troisième machine sous cette ligne accordée), après la réparation du
harnais (R-2464, R-2470, R-2486) et la contre-lecture courte du harnais v10 (`contre-lecture-courte-harnais-d1a-v10.md`,
`e7bdbb1506758ab61da517238729bf3413c3124462c4c09df05bb3c6a4a4a388`, Claude Fable 5.2 : « utilisable après corrections »,
aucune garde affaiblie ; corrections E1 à E3 reprises ici). Code : `prep/lean-outillage-d1a-v10`, commit
`5103a7f300523831361303d9bc56d6658546165d` ; procédure v11 et journaux au commit
`ae894d8df2a19f51e532ff667160ae7bba2bf6ac` (tête de la branche ; aucun code entre les deux).

**Pourquoi** : le second essai (`rapport-poste-local-d1a-v2.md`, `b2bace9b…`, branche
`donnees/lean-outillage-d1a-poste-local-v2`) s'est arrêté au pas `noyau` (0/18) : le vérificateur du noyau v4 ne compilait
pas sous Lean 4.35.0. Le harnais v10 le répare (vérificateur v6, compilé et joué hors machine contre la chaîne épinglée :
39 cas jugés conformes sur 39), ajoute un essai R5 « le vérificateur compile sur la machine » avant la coupure, et refait
l'artefact du simproc hors noyau (v5). Les corrections du premier et du second essai restent.

**Tu es une session fille** : ton mandat est **cette consigne seule** ; tu ne reprends aucune autre tâche du programme. Tu
n'écris jamais dans `main`, jamais vers `lciric/controle-ia`, jamais une ligne de `registres/go.md` ; la session mère inscrit
dépenses, arrêts et décisions d'après ton rapport.

**Dépense autorisée** : **GO-2026-11-10-13**, 65 USD au plus, dont **0,56 USD déjà dépensés** par les deux premiers serveurs
(175751342 et 175838427).
- **Une seule** machine Hetzner `ccx33` (`hel1`) de plus, vie bornée par la minuterie.
- **Aucun appel de modèle**, **aucune clé de modèle ni dépôt du programme sur la machine**. Aucune autre dépense.
- **Déclaration (R-2439, comme en R-2426)** : c'est la **troisième machine sous cette ligne**, accordée par Lazar. La garde
  « une machine par GO » du harnais est **contournée par construction** : ta branche neuve ne porte ni fichier de
  rattrapage ni journal des créations des deux premiers essais, seules pièces que la garde lit. Le contournement ne vaut
  que pour cet essai : une préparation, une création.

## Règles
- **`CLAUDE.md` du dépôt** (R1 à R14, interdits) et les **interdits communs v2**
  (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, `1ee3b370…`), **avec ces écarts
  écrits et eux seuls** :
  - règle 3 levée pour l'interface de Hetzner (jeton `HCLOUD_TOKEN` lu par son nom), pour le SSH vers la seule machine que
    tu crées, et pour le service d'adresse de `MV7 adresses-sortie` (section 0) ;
  - règle 4 : permis seulement `git clone`, `git fetch origin <branche>:refs/remotes/origin/<branche>` (avec refspec),
    `git remote set-branches --add origin <ta branche>`, la création de ta branche, `git add -- <fichiers nommés>`,
    `git commit`, `git push` de ta seule branche (retentatives 2, 4, 8, 16 s).
- **La procédure fait foi pour tous les gestes de la machine** :
  `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/procedure-poste-local-d1a-v11.md`, sur la branche du harnais
  `prep/lean-outillage-d1a-v10`, commit `ae894d8df2a19f51e532ff667160ae7bba2bf6ac`.
  - Empreinte entière vérifiée avant lecture : `932b3bbc8f7741c8b18a99ba2384b56d70225bcb10af79cfcaa24d250e124e20`.
  - Sections 0 à 7, **en entier et dans l'ordre**, avec les précisions ci-dessous. Notation `MV7`.
  - **Correction E1** : l'en-tête de la procédure v11 dit que le code est au commit `5103a7f3` ; ta branche part de
    **`ae894d8d`** (la procédure v11 et les empreintes v8 n'existent qu'à ce commit ; aucun code n'a changé entre les deux).
- **Poste** : sous WSL (Ubuntu), clone dans le système de fichiers Linux ; le jeton de `gh` ne passe qu'à `git`
  (environnement du processus), jamais écrit ni affiché.
- **Terminal WSL ouvert pendant tout l'essai** (incident R-2434 : sans fenêtre WSL ouverte, WSL arrête Ubuntu et tue les
  processus détachés, minuterie comprise) : un terminal Ubuntu ouvert par Lazar **avant l'essai à blanc**, gardé ouvert
  **jusqu'à l'inventaire final** de la section 5 ; vérifie-le avant l'essai à blanc et avant L1 (sinon aucune
  préparation) ; s'il se ferme après L5 : `MV7 verifier-minuterie` tout de suite, non conforme : `MV7 detruire --identifiant
  N`, jamais de relance.
- **Données du poste (CLC5-07)** :
  - identité Git neutre pour ce clone seulement (`poste-local`, `poste-local@invalid`, sans `--global`), vérifiée avant
    chaque commit ;
  - avant chaque commit : `git add -- <fichiers nommés>`, puis `MV7 garde-poste --ip-poste IP_POSTE && git commit …` ;
  - chaque sortie du pilote ou d'un processus détaché passe `MV7 garde-poste --ip-poste IP_POSTE --fichier <pièce>` avant
    d'être versée (la garde refuse aussi toute adresse du /24 du poste) ;
  - jamais versés : l'adresse du poste ni aucune adresse de son /24, le dossier personnel, le chemin absolu du clone, le nom
    de la machine ou de l'utilisateur ; aucune sortie de `adresses-sortie` n'est versée (elle ne porte que des comptes).
- **Mandataire** : `getproxies_environment()` vide à l'essai à blanc ; sinon arrêt.
- **Délais des outils** : `detruire` et `inventaire` jusqu'à environ 9 minutes : délai d'outil d'au moins 10 minutes, ou
  arrière-plan.
- **Refus** d'un contrôle de permissions ou d'un classifieur : arrêt sur ce point, destruction du serveur s'il existe
  (section 4), rapport ; ni contournement, ni reformulation.
- **Un seul essai** : une préparation (L1, **jeton neuf** tiré par `preparer`), une création ; **aucun autre essai** sans
  consigne neuve de la mère et accord de Lazar.

## Mandat
1. **Dépôt** :
   - clone neuf de `https://github.com/lciric/controle-ia-travail.git` ;
   - `git fetch origin prep/lean-outillage-d1a-v10:refs/remotes/origin/prep/lean-outillage-d1a-v10` ;
   - **ta branche `donnees/lean-outillage-d1a-poste-local-v3`, partie du commit
     `ae894d8df2a19f51e532ff667160ae7bba2bf6ac`** (E1), poussée par `git push -u origin donnees/lean-outillage-d1a-poste-local-v3` ;
   - puis la référence de suivi de la procédure (L3 : `git fetch` par refspec, `git remote set-branches --add`, `@{upstream}`
     résolu) ;
   - vérifie que `V` ne contient ni `rattrapage-machine-d1a-*-v1.json` ni `journal-creations-machines-v1.jsonl` ; sinon arrêt ;
   - lis la procédure v11 depuis `origin/prep/lean-outillage-d1a-v10` et vérifie son empreinte ;
   - vérifie l'empreinte de cette consigne (`sha256sum -c` de son compagnon, sur `origin/main`) ;
   - routine de `CLAUDE.md`, points 1 et 2 seulement.
2. **Section 0 de la procédure** :
   - prérequis, dont le **terminal WSL ouvert** (Règles) ;
   - essai à blanc hors du bac à sable, dont la **fin et reprise réelles** (hôte de la session relancé, vérifié par l'heure
     de démarrage du processus) ;
   - **`MV7 adresses-sortie --ip-poste IP_POSTE`** : code 0, retenir `P` = `prefixe_conseille` (32 ou 24). **Jamais
     `--prefixe-poste 24` sans cette mesure** ; si elle rend 32 alors que les deux premiers essais ont établi deux adresses
     de sortie du même /24, le signaler à Lazar avant L2. Code 1 : arrêt, compte rendu, aucune préparation ;
   - **`stat -c %a src/controle_ia/lean_essai/verificateur_noyau_v6.lean` = `644`** (sinon `chmod 644` de ce seul fichier,
     sans commit) ;
   - ordinateur sur secteur, capot ouvert.
3. **L1, L2, L3** :
   - `T_LIM` = heure de L1 (`date -u`) **plus 6 heures** ; `H` = `T_LIM` **plus 40 heures** ⟦MÈRE : garder ces écarts, ou
     fixer `T_LIM` et `H` en heures absolues⟧ ;
   - `MV7 preparer --go GO-2026-11-10-13 …` (fichier `rattrapage-machine-d1a-<jeton12>-v1.json` au **jeton neuf**, tiré par
     `preparer` ; ⟦MÈRE : aucun jeton à fournir ; le jeton te revient en L3⟧) ;
   - **L2** avec `--prefixe-poste P` ;
   - **L3** : pousser, référence de suivi, puis donner à Lazar, pour la mère : branche, commit, jeton, identifiants de la clé
     et du pare-feu, empreinte de la clé, et `P`.
4. **Attendre le mot « armée »** de la mère, relayé par Lazar, avec l'empreinte du fichier de rattrapage ; **sans lui, aucune
   création**. La mère fait M1 à M6 : lecture, même projet, droit d'écrire, destruction à blanc, trois tâches (T1 à H, T2 à
   H + 30 min et T3 à H + 24 h en session neuve), ligne « en tâche jusqu'à » dans `registres/etat.md`
   ⟦MÈRE : identifiants des tâches T1 à T3 et heures, au mot « armée »⟧.
5. **L4 à L7** (`creer-et-armer --go GO-2026-11-10-13 … --deja-depense-usd 0.56`), puis **section 3** :
   - avant le premier pilote : si l'adresse du serveur est déjà connue du poste (`ssh-keygen -F <adresse du serveur>`),
     `ssh-keygen -R <adresse du serveur>` ;
   - pilote `avant` (`scripts/lean_essai_d1a_v10/piloter_poste_v10.sh avant …`) : installation par `installer_chaine_v2.sh`
     (garde de lisibilité, code 5 si un chemin reste fermé à `bac`), sonde v2 « ouverte », essai R5 « bac lit
     Mathlib.olean » (sain, témoin 0644, artefact 0600), puis **essai R5 « le vérificateur compile sur la machine »**
     (`essai_compilation_verificateur_v1.sh` sur `/root/verificateur_noyau_v6.lean` : compile sans message ; copie cassée
     refusée). **Tout code non nul du pilote `avant` : ni coupure, ni pilote `apres`** ; section 5, compte rendu ;
   - coupure : `MV7 acces-couper … --ip-poste IP_POSTE --prefixe-poste P`, puis `MV7 verifier-coupure` ;
   - pilote `apres` : vidage du cache du résolveur, sonde v2 « fermée », harnais déposé (exécuteur, épreuve et vérificateur
     v6, artefacts avec `attendus-v5.json`), contrôle `cmp` du vérificateur contre celui compilé avant la coupure,
     vérificateur épinglé, **épreuve d'isolement dont le premier pas est `noyau`** (non conforme : rien d'autre, section 5,
     compte rendu), épreuve, mesures (taille de Mathlib, temps d'un item jouet, mémoire à trois processus), sonde de fin ;
   - **réserve de mémoire (correction E2)** : l'essai R5 de compilation ne tourne **ni dans le bac ni en exécutant** le
     vérificateur (il le compile, par `runuser -u bac`, hors de `bwrap` et de `systemd`). Le **premier passage réel** du
     vérificateur sous `MemoryMax=6G` et `MemorySwapMax=0` a lieu **après la coupure, au premier pas `noyau`** ; mesuré
     hors machine : environ 8 s et 2,1 Gio de mémoire anonyme par passage, plus les pages des `.olean` de Mathlib (environ
     7 Gio, récupérables). **Si ce pas échoue par la mémoire ou par le délai** : relève, dans
     `premier-pas-noyau-v6.json`, pour chaque cas en échec, `incident_bac` (« mémoire » ou « délai »), le bloc `noyau`
     (`resultat`, `fin`, `memoire_pic`, `duree_murale_s`, `resume_systemd`), et `erreurs_noyau` ; verse la pièce après
     `garde-poste --fichier` ; puis **fin normale (section 5), sans relance**, ni du pas ni du pilote ;
   - valeurs des pièces `VERSION-LEAN`, `COMMIT-MATHLIB`, `MACHINE`, `ESSAIS-R5` (partie machine : lecture par `bac`,
     compilation du vérificateur, pas `noyau`, épreuve).
6. **Fin** : section 5 (normale) ou 4 (anormale).
   - Serveur détruit par son identifiant **dans tous les cas** ; inventaire « aucun serveur de l'essai ».
   - Clé et pare-feu supprimés ; si `acces-supprimer` rend 422 `resource_in_use`, refaire 2 à 3 minutes plus tard.
   - Minuterie arrêtée par son PID si elle vit.
   - Terminal WSL fermé seulement après l'inventaire final.
7. **Rapport** sur ta branche, sous `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/` (noms neufs) :
   `rapport-poste-local-d1a-v3.md`, scellé. Il contient :
   - vie du serveur (création, destruction, heures, coût ; cumul sous GO-2026-11-10-13) ;
   - `P` retenu et la sortie de `adresses-sortie` (comptes seulement) ;
   - sorties des étapes ;
   - résultat de la garde de lisibilité, de l'essai « bac lit Mathlib.olean », de l'essai « le vérificateur compile sur la
     machine », du pas `noyau` (avec, en cas d'échec par la mémoire ou le délai, les relevés de E2) et de l'épreuve ;
   - valeurs des pièces, incidents, écarts ;
   - **lignes proposées** pour `registres/depenses.md` et `registres/arrets.md`.

   Pièces sous `pieces-poste-local-d1a-<jeton12>-v1/`. Lazar relaie à la mère.

## Réserve pour la mère (correction E3, hors du mandat du poste)

« 176 mutations sur 176 tuées » (mutations v10) **ne prouve pas** que le jeu d'artefacts détecte le retrait du rejeu par le
noyau ou de la collecte des axiomes : avec l'arrêt au premier essai en échec, k06 (rejeu retiré) est tuée par accident de
texte (`test_artefact_avertissement_refuse`), et k01, k09, k10 avant tout passage d'artefact. Le comportement du code non
muté est établi par le journal hors machine (refus nommés du simproc v5 et de `run_cmd`, axiomes `triche`, `sorryAx`), et le
troisième essai joue lui-même ces artefacts sur la machine. Avant toute réutilisation du vérificateur au-delà de
l'outillage (D-1b) : rejouer k06 et k01 (et k09, k10) de façon qu'un essai fonctionnel les tue, journal scellé nommant
l'essai qui tue. Non bloquant pour le troisième essai.

## Annexe — suggestions de la contre-lecture, hors de ce tour (aucun code neuf), pour plus tard

- **S1** : témoin écrit sur la machine par l'essai R5 de compilation, vérifié par la phase « apres » avant
  `couper_reseau_v1.sh` (un « avant » en échec ne pourrait plus être suivi d'une coupure).
- **S2** : avant la coupure, un passage réel du vérificateur sur l'item sain, par `bac`, sous `systemd-run` avec
  `MemoryMax=6G` (l'échec de mémoire ou d'import serait vu avant la coupure).
- **S3** (vérificateur v7) : après `ajouterAcceptee`, exiger que chaque constante rejouée soit dans l'environnement
  d'impression avec le même type ; refuser un bloc inductif dont un membre manque.
- **S4** : ajouter aux artefacts de la machine le cas `module` + `public import Mathlib` (éprouvé hors machine seulement),
  et les mots `module`, `public`, `meta` à la garde de texte G-L3+.
- **S5** : faire échouer G-L7 si la sortie d'erreur du vérificateur (`noyau.err`) n'est pas vide.
- **S6** : fichier d'essais neuf de la minuterie (nom neuf, R12) où l'essai de la course prend ses dates par rapport à
  l'heure courante (`test_creation_avec_course_ne_detruit_pas`, daté, échoue depuis 2026-11-12T16:00Z).
- **S7** : dire dans la réserve de la procédure que les axiomes des lemmes de Mathlib viennent des tables précalculées de
  ses `.olean`.
- **S8** : sceller un journal des « 53 essais ciblés » de la v6 ; corriger l'en-tête de la procédure (le développeur a
  écrit les vérificateurs v5 et v6).
