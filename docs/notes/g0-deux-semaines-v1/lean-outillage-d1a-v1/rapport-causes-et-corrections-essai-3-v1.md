# Essai Lean D-1a, troisième essai : causes établies et corrections, hors machine (v1)

- **Quoi** : pas 2 à 5 de « Avant un quatrième essai » de l'arbitrage Fable 5.2, point 7
  (`docs/notes/arbitrages-points-delicats-v1/arbitrage-fable-six-points-delicats-v1.md`, sur `main`), sous le mot de Lazar
  GO-2026-11-21-40 (« on ne s'arrête pas à un échec avant d'avoir compris les causes de cet échec et avoir réussi à les
  corriger »). Aucune dépense, aucune machine louée.
- **Qui** : développeur Claude Opus 5.5, session du 21 novembre 2026. Pièce de classe B (instrument) : contre-lecture par un
  autre modèle à faire (pas 6), rien n'est scellé comme décisif.
- **Branche** : `prep/lean-outillage-d1a-v11`, partie de `5103a7f3` (code du troisième essai).
- **Pièces lues** : rapport du poste v3 et `epreuve-isolement-v6.json`, branche `donnees/lean-outillage-d1a-poste-local-v4`
  (`753cceb0…`) ; code du harnais au commit `5103a7f3`.

## 1. Verdict

Les cinq « non conforme » de l'isolement Lean ont une cause établie, et ce n'est pas un fait d'isolement : **les cinq items
sondes ne compilent pas sous Lean 4.35.0**, pour une erreur de type dans leur fonction commune `tenter`. Aucune tentative ne
s'exécute, sur la machine comme ici. Corrigé (items sondes v3), et l'épreuve v7 sort désormais « épreuve morte » quand son cas
sain ne rend pas ses tentatives. Le classement du temps de processeur est corrigé (exécuteur v7) par le temps de processeur que
rapporte systemd, comparé à la limite. La cause du pic de mémoire à 336 Kio est établie dans le code source de systemd 255 ; le
chiffre de systemd est retiré, remplacé par un relevé échantillonné. Un item Lean qui dépasse sa limite de mémoire est écrit ;
ici, il est tué par une limite de cgroupe de 512M, mais son classement « mémoire » par le bac reste à jouer au quatrième essai.

## 2. Pas 2 : la cause des cinq échecs

**Attendu, écrit avant de compiler** (bloc-notes du développeur, versé tel quel : `pieces-causes-essai-3-v1/attendu-avant-compilation-v1.md`) : « erreur d'élaboration dans la fonction commune
`tenter` : `r.take 120` ne rend plus un `String` (`String.take` rend une tranche `String.Slice`) ; `tenter` n'est pas définie
et chaque `#eval tenter …` échoue : aucune ligne ISOLEMENT, code 1. […] Ce qui me ferait changer : une erreur d'accès au fichier
ou d'import (refus du bac), qui serait un fait d'isolement. » Lu avant de compiler : les cinq items sondes n'ont **pas**
`import Mathlib` (prélude seul), alors que les 21 items des gardes l'ont ; le module « prelude sans import » du pas noyau compile
en 0,06 à 0,09 s sur la machine. Le temps de 0,4 s n'est donc pas « un échec avant la fin des imports » : c'est le temps normal
d'un fichier sans Mathlib, et une erreur ordinaire en prend 4,4 parce qu'elle importe Mathlib.

**Chaîne installée ici**, comme pour l'essai hors machine du 12 novembre (journal
`journal-essais-hors-machine-d1a-v10-v1.txt`, même dossier) : elan (`elan-init.sh` sha256 `a620ff16…`, identique), Lean
`version 4.35.0, x86_64-unknown-linux-gnu, commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc, Release`, Mathlib
`56a005855ea17e0b0958f73ec801ae140b0a1679` (récupéré seul, profondeur 1) et son cache (`lake exe cache get` : 9 031 fichiers,
1 min 43 s). Place disque : 11 Gio pour la chaîne ; 25 Gio libres avant, 15 Gio après.

**Compilation comme le bac** : `scripts/lean_essai_d1a_v11/compiler_comme_bac_v1.sh` lance exactement la commande du bac
(`executeur_bac_v6.py`, `Bac.verifier_lean`) : `lean --json --root=/item -o /item/Item.olean -i /item/Item.ilean
/item/Item.lean`, dossier courant `/item`, environnement `HOME=/tmp`, `PATH=/usr/bin:/bin`, `LANG=C.UTF-8`, `LEAN_PATH` de
Mathlib, item seul dans `/item`, `/tmp` neuf. Ce n'est pas l'isolement du bac (ni systemd, ni bwrap, ni l'utilisateur `bac`) :
espaces de noms de montage, de réseau et de processus neufs, racine en mémoire, `/usr` et la chaîne en lecture seule, chroot.
Il sert à lire la sortie sans que les tentatives d'une sonde touchent l'hôte.

**Sortie lue** (pièce `pieces-causes-essai-3-v1/sortie-compilation-sondes-v2-v1.json`) : les cinq items sortent en code 1, en
0,35 à 0,46 s de temps mural (0,34 à 0,40 s de processeur sur la machine), sortie d'erreur vide, et leur sortie standard
commence par la même ligne, l. 5, col. 88 :

```
{"data":"Application type mismatch: The argument\n  r.take 120\nhas type\n  String.Slice\nbut is expected to have type\n  String\nin the application\n  \" REUSSI \".append (r.take 120)", "fileName":"/item/Item.lean", "pos":{"column":88,"line":5}, "severity":"error", …}
```

puis, pour chaque `#eval` : `"Aborting evaluation since the expression depends on the 'sorry' axiom, which can lead to runtime
instability and crashes."` (sévérité `error`). L'item réseau a deux erreurs de plus, de même nature (`o.stdout.take 80`,
`o.stderr.take 160`, l. 12 et 14). Aucune ligne « ISOLEMENT ». Témoin : l'erreur ordinaire `gl1_erreur_compilation_v1.lean`
sort en code 1 en 5,1 s, « Type mismatch … etape_1 x ».

**Cause établie** : sous Lean 4.35.0, `String.take : String → Nat → String.Slice` ; la fonction `tenter` des items v2 passe ce
résultat à `String.append`, qui attend un `String`. L'élaboration de `tenter` échoue, Lean la remplace par `sorry`, et refuse
d'évaluer chaque `#eval` qui en dépend. Aucune lecture, aucune écriture, aucun processus réseau n'a été tenté au troisième
essai. Les cinq « non conforme » ne disent rien de l'isolement, ni pour ni contre, comme l'arbitre l'avait lu. Ce qui l'aurait
fait changer (« un refus par le bac d'une lecture que le noyau et les gardes font aussi ») n'est pas observé : les 21 cas des
gardes n'ont pas à être relus. Les essais d'avant ne compilaient jamais ces items contre la chaîne épinglée (l'essai hors
machine v2 les excluait : « joués ici sans isolement, ils écriraient sur l'hôte »), d'où un défaut vu seulement sur la machine,
comme celui du vérificateur v4 au second essai.

## 3. Pas 3 : l'épreuve corrigée (épreuve v7, items sondes v3, attendus v6)

- **Items sondes v3** (`scripts/lean_essai_d1a_v4/artefacts_r5_v4/iso_*_v3.lean`) : copies des v2 (inchangées, R12) où chaque
  `(x.take k)` devient `(x.take k).toString` ; rien d'autre (essai `test_sondes_v3_egales_aux_v2_plus_to_string`). Compilés
  comme le bac (pièce `sortie-compilation-sondes-v3-v1.json`) : code 0, chaque item rend toutes ses tentatives ; le cas sain
  rend `ISOLEMENT ecriture-tmp REUSSI écrit` et `ISOLEMENT ecriture-item REUSSI écrit`. Les issues ECHEC ou REUSSI de cette
  pièce sont celles du bac à sable du développeur, pas celles du bac.
- **`epreuve_isolement_v7.py`** (copie de la v6, inchangée) :
  - la sortie de compilation de chaque item sonde (isolement Lean, limites Lean) entre dans le JSON, bornée : 4 000
    caractères de la sortie standard, 1 000 de la sortie d'erreur, drapeaux de troncature, code de compilation, et
    `sonde_muette` quand aucune ligne « ISOLEMENT » n'est sortie ;
  - un cas marqué `sain` dans les attendus (persistance, écriture dans son propre espace : un pour l'isolement Lean, un pour
    l'isolement Python) qui ne rend pas toutes ses tentatives attendues fait sortir son genre **« épreuve morte »**, et
    l'épreuve entière avec (`statut`, `genres`, `genres_morts`, code de sortie 3), distinct de « non conforme » (code 1) ;
    une épreuve morte n'est jamais « conforme » ;
  - `echecs_invalides` : un ECHEC dont le détail dit que le processus n'a pas été lancé (« could not execute external
    process ») est un écart. Vu ici : dans le bac à sable du développeur, `python3` ne se lance pas et les deux tentatives
    réseau en Python sortaient ECHEC sans rien prouver ; la v2 les aurait comptées « conformes ».
- **`attendus-v6.json`** : copie des v5 (inchangés) ; groupes `noyau`, `observations_noyau`, `lean` égaux ; sondes v3 ; cas
  sains marqués ; `echecs_invalides` sur l'item réseau ; artefacts neufs des pas 4 et 5 (ci-dessous).

## 4. Pas 4 : classement du temps de processeur (exécuteur v7)

Défaut lu au troisième essai : l'item Python qui brûle le processeur est tué par `LimitCPU` à 5,011 s ; le bac (bwrap) sort en
code 137, que systemd rapporte `Finished with result: exit-code`, `code=exited/status=137` ; la v6 n'attendait « délai » que
d'un résultat `signal` portant « XCPU », et a rendu « aucun incident ».

Correction (`executeur_bac_v7.py`, `classer_execution(res, cpu_max_s)`) : ne lit que ce que systemd rapporte, jamais le code
de sortie ni la fin du processus principal. « délai » si le résultat est `timeout`, ou si l'unité n'a pas réussi (`exit-code`,
`signal`, `core-dump`) et que « CPU time consumed » atteint `cpu_max_s` ; « mémoire » si `oom-kill` ; rien si `success`. Un
résultat sans réussite et sans temps de processeur rapporté arrête l'exécuteur (R5, aucun repli silencieux). Le temps de
processeur est fiable sous systemd 255 : il est mis en cache avant le retrait du cgroupe (`unit_prune_cgroup`, ci-dessous) ; les
chiffres du troisième essai le confirment (4,3 à 4,8 s par compilation avec Mathlib, 5,011 s pour l'item tué).

**Décision de définition, à valider par le contre-lecteur** (l'arbitre la renvoyait au développeur et à son contre-lecteur) :
le compte est celui de l'unité entière, la limite est par processus. Pour un processus seul (Lean, Python sans enfant) les deux
coïncident (le compte de l'unité inclut bwrap, négligeable, et ne peut qu'être plus grand). Un item à plusieurs processus qui
consomme ensemble la limite sans réussir sort « délai » : il a consommé son budget, il n'évite aucune issue. Un item ne peut
plus se faire classer « délai » qu'en brûlant vraiment la limite.

Essais R5 (`tests/test_lean_essai_executeur_v7.py`), sur les résumés systemd réels du troisième essai : l'item qui brûle le
processeur (`exit-code`, 137, 5,011 s) sort « délai » ; un item qui sort vite en code 137 (`exit-code`, 137, 31 ms) ne sort
pas « délai » ; la v6 rendait « aucun incident » sur le premier (défaut reproduit) ; table de huit cas (« XCPU » seul ne
suffit plus, limite atteinte exactement, réussite au-delà de la limite) ; limite prise dans la configuration. Pour la machine,
artefact neuf `limite_code137_v1.py` (sort de lui-même en 137, attendu : code 137, aucun incident) dans `limites_python`.

## 5. Pas 5 : la mémoire

**Pourquoi 336 Kio — cause établie dans le code source.** Le chiffre vient de la ligne « Memory peak » que `systemd-run --wait`
imprime (`lire_resume_systemd`). La machine avait systemd 255 (`255.4-1ubuntu8.17`, Ubuntu 24.04.4, pièce
`installation-v6.txt`). Sources lues (étiquettes `v255` et `v256` du dépôt systemd) :
- `src/run/run.c` v255 (sha256 `675238d0…`), l. 1109 à 1145 et 1502 à 1503 : `systemd-run` relit toutes les propriétés de
  l'unité, dont `MemoryPeak` (l. 1119), à chaque changement d'état signalé, et imprime à la fin la dernière valeur reçue ;
- `src/core/cgroup.c` v255 (sha256 `ac2af6fb…`), `unit_get_memory_accounting`, l. 4046 à 4105 : `memory.peak` est lu dans le
  cgroupe de l'unité tant qu'il existe ; une fois le cgroupe retiré, systemd rend la dernière valeur lue
  (`memory_accounting_last`) ; `unit_prune_cgroup`, l. 3123 à 3134 : avant de retirer le cgroupe, la v255 ne met en cache que
  le temps de processeur (« Cache the last CPU usage value before we destroy the cgroup ») ;
- `src/core/cgroup.c` v256 (sha256 `480bd4a9…`), l. 3571 à 3575 : la v256 ajoute la mise en cache des compteurs de mémoire
  avant le retrait (« Cache the last CPU and memory usage values »).

Donc, sous systemd 255, quand le processus sort de lui-même, le cgroupe est retiré avant que `systemd-run` ne relise
`MemoryPeak` : il reçoit la dernière valeur lue pendant que le cgroupe existait, en général au passage de l'unité à « active »,
juste après le lancement de bwrap (de 332 Kio à 1,2 Mio pour presque tous les cas de la pièce). Quand systemd arrête lui-même
l'unité (`oom-kill`, `timeout`), il signale un état intermédiaire pendant que le cgroupe existe encore, et la valeur est juste
(512,0M pour l'item tué par la mémoire, 3,6M pour l'item tué par la durée). La rare valeur plausible d'une compilation
réussie (633,1M une fois, au pas noyau) vient probablement d'une lecture tombée pendant l'arrêt (non établi). Champ lu : `MemoryPeak` (octets, imprimé en Kio ou
Mio) ; unité : le service transitoire `bac-<item>-<pas>.service` ; portée : toute l'unité (bwrap et l'item), pas le seul
processus. La mesure n'était pas aveugle au processus Lean : elle était périmée pour tout le bac. Ordre de grandeur d'un
processus Lean sans Mathlib mesuré ici par un cgroupe : 74 Mio (pièce `memoire-lean-cgroupe-v1-v1.json`) ; 336 Kio est impossible.

**Correction** (`executeur_bac_v7.py`) : « Memory peak » n'est plus lu ; le résultat ne porte plus `memoire_pic`. À la place,
pendant que `systemd-run --wait` attend, root relève `memory.peak` du cgroupe de l'unité toutes les 0,1 s
(`/sys/fs/cgroup/system.slice/<unité>.service/memory.peak`, tranche imposée par `--slice=system.slice`) :
`memoire_pic_echantillonne_octets` est le plus haut relevé, un **minorant** du pic (`memory.peak` ne décroît pas ; ce qui
monte après le dernier relevé est perdu), `None` si aucun relevé ; `memoire_echantillons` en donne le nombre. Canal hors de
portée de l'agent (fichier du cgroupe lu par root). Essais : échantillons croissants (plus haut relevé), aucun relevé (absent),
cgroupe d'une autre unité non lu, plus haut relevé et non dernier, clés publiques.

**Item Lean qui dépasse sa limite** : `limite_memoire_lean_v1.lean` (sans Mathlib ; `#eval` remplit un tableau de
200 000 000 cases, environ 1,6 Gio touché ; le pli force le remplissage ; la ligne « ALLOUE » ne doit pas sortir), groupe neuf
`limites_lean`, joué sous les limites d'essai (512M, 5 s) ; attendu : incident « mémoire », compilation en échec, pas de
« ALLOUE ». Le bac ne se rejoue pas ici (ni systemd en processus 1, ni bwrap, cgroupes v1). Joué ici à défaut, compilé comme le
bac dans un cgroupe de mémoire v1 limité à 512M, mémoire d'échange comprise (pièce `memoire-lean-cgroupe-v1-v1.json`) : le
processus Lean est tué (code 137, compteur `oom_kill` à 1, pic 536 870 912 octets), sans « ALLOUE » ; témoin sain (même item à
1 000 000 cases) : code 0, « ALLOUE 7000000 », pic 74 Mio. Le classement « mémoire » par le bac (résultat systemd `oom-kill`)
est **écrit, non joué** : au quatrième essai.

## 6. Essais

- **Essai hors machine d'avant, refait de même** (« 39 cas jugés conformes sur 39 » : `essai_verificateur_hors_machine_v2.py`,
  procédure v11 et journal du 12 novembre) : `decrire-chaine` puis `jouer` contre la chaîne installée ici, code `5103a7f3`,
  un passage Lean à la fois. Résultat : vérificateur compilé sans message, **39 cas jugés conformes sur 39**, 2 observations,
  de 11:24:20Z à 11:34:05Z (pièce `essai-verificateur-hors-machine-v2-rejeu-2026-11-21-v1.json`).
- **Même essai avec l'exécuteur et l'épreuve v7** (`scripts/lean_essai_d1a_v11/essai_verificateur_hors_machine_v3.py`, copie
  de la v2 sur les attendus v6, dont les trois groupes joués sont égaux à ceux des v5) : vérificateur compilé sans message, **39 cas jugés conformes sur 39**, 2 observations, de 11:35:15Z à 11:54:10Z (pièce `essai-verificateur-hors-machine-v3-v1.json`) : l'exécuteur v7 ne change rien aux cas du noyau et des gardes.
- **Essais neufs** : `tests/test_lean_essai_executeur_v7.py` (23 cas : classement, pic échantillonné, sortie d'erreur,
  limite de la configuration aux trois points d'appel, changements déclarés exacts par rapport à la v6),
  `tests/test_lean_essai_epreuve_v7.py` (24 cas, dont 10 avec la chaîne : les cinq sondes v2 compilées comme le bac sortent en
  code 1 avec l'erreur `String.Slice` et sans tentative ; les cinq v3 rendent toutes leurs tentatives ; épreuve entière avec
  un bac factice : cas sain conforme, troisième essai rejoué « épreuve morte », artefact seul « non conforme », épreuve
  morte Python, codes de sortie), `tests/test_lean_essai_pilote_v11.py` (2 cas). Sans la chaîne, les 10 cas qui la demandent
  sont sautés en le disant.
- **Suite du harnais** (`tests/test_lean_essai_*.py`, avec la chaîne, 29 min) : 764 réussis, 3 échecs, tous trois dans des fichiers que cette branche ne touche pas (minuterie v5, v6, v7, identiques à `5103a7f3`) : `test_creation_avec_course_ne_detruit_pas` des minuteries v6 et v7, essai daté connu (échéance fixe 2026-11-12T16:00Z, déjà désélectionné par les lanceurs de mutations v9 et v10 pour cette raison) ; `test_minuterie_reelle_detachee` (v5), « le PID désigne un autre processus » sous la charge de trois passages Lean concurrents, **réussi rejoué seul** (0,7 s). Aucun échec dans les essais de l'exécuteur, de l'épreuve, du vérificateur ou du pilote.
- **Mutations des gardes neuves** (`scripts/lean_essai_d1a_v11/mutations_gardes_v11.py`, copie neuve par mutation, import
  tracé, chaîne posée) : premier passage, 28 tuées sur 29 ; survivante x707 (la compilation classée avec 5 s fixes au lieu de
  la limite de la configuration : aucun essai ne passait par `Bac` en mode isolé). Essai ajouté
  (`test_bac_classe_avec_la_limite_de_sa_configuration`) et deux mutations sœurs aux autres points d'appel (x714, x715) ;
  second passage : **31 tuées sur 31** (pièces `journal-mutations-gardes-v11-essai-1.json` et `-essai-2.json`). Une mutation
  écartée comme équivalente : retirer « et pas d'épreuve morte » de `conforme` (le cas sain mort a toujours des écarts, donc
  `conforme` est déjà faux ; le `statut`, lui, est éprouvé par e703).

## 7. Ce qui reste non éprouvé

- **Tout ce qui passe par systemd et bwrap** ne se rejoue pas ici (conteneur sans systemd en processus 1, sans bwrap, cgroupes
  v1) : le classement v7 sur la machine ; le chemin du cgroupe (`/sys/fs/cgroup/system.slice/<unité>.service/memory.peak`
  sous Ubuntu 24.04 et `--slice=system.slice`) ; le pic échantillonné, dont rien ne garantit qu'il ne rende pas `None` si le
  chemin diffère (il le dirait : `memoire_echantillons` à 0) ; le classement « mémoire » de l'item Lean par le résultat
  systemd `oom-kill` ; les issues ECHEC ou REUSSI des sondes v3 sous bwrap et l'utilisateur `bac`.
- Le pic échantillonné est un minorant : un pic bref entre deux relevés (0,1 s) peut manquer. Pour la mémoire à trois
  processus en parallèle (`mesurer`), chaque unité a son pic ; leur somme majore le pic simultané des trois sans le mesurer.
  La mémoire de la machine entière pendant le passage en parallèle n'est pas relevée : tant qu'elle ne l'est pas, l'arbitre
  dit qu'aucun passage en parallèle n'est compté.
- L'item Lean de mémoire est joué sous les limites d'essai (512M, 5 s) ; le vérificateur qui suit (Mathlib, environ 2,1 Gio
  et 8 s) y est lui aussi arrêté : l'incident retenu est celui de la compilation (le premier), comme pour tout item.
- La définition « délai » (compte de l'unité contre limite par processus) attend la contre-lecture (§ 4).
- Le pilote v11 n'est éprouvé que par son texte (`bash -n` et changements déclarés) ; la procédure du quatrième essai (v12)
  n'est pas écrite.
- Contre-lecture des programmes v7 et v11 par un autre modèle, puis vérification des corrections par le même : pas 6, non
  fait.

## 8. Ce que le quatrième essai devra rejouer

Sous la ligne GO-2026-11-10-13 (0,84 USD restant sur 65, échéance le 30 novembre), après le pas 6 : pilote v11, exécuteur et
épreuve v7, attendus v6, vérificateur v6 inchangé. Tout se rejoue, puisque le code a changé :
1. les 18 cas du pas « noyau » (deux passages) ;
2. l'épreuve entière, 36 cas : 21 gardes Lean, **5 isolement Lean (sondes v3)**, 4 Python, **5 limites Python** (dont le
   cas neuf « sortie en code 137 sans consommer la limite », attendu sans incident), **1 limite Lean** (attendu « mémoire »),
   plus les contrôles de l'hôte. À lire d'abord : `statut` et `genres` ; un genre « épreuve morte » arrête la lecture de ce
   genre ; le cas « temps de processus (5 s) » doit sortir « délai » ; les cinq sondes Lean doivent porter
   `sonde_muette: false`, un code de compilation 0 et leur extrait de sortie ;
3. `mesurer` : relever `memoire_pic_echantillonne_octets` et `memoire_echantillons` de chaque compilation et du vérificateur ;
   des valeurs nulles, absentes, ou de quelques centaines de Kio pour un processus Lean avec Mathlib diraient que la mesure
   est encore fausse ;
4. pour la mémoire à trois processus, ajouter une mesure de la machine entière avant de compter un passage en parallèle
   (à décider au pas 6).

## 9. Fichiers de la branche (tous neufs, aucun existant modifié, R12)

- Code : `src/controle_ia/lean_essai/executeur_bac_v7.py`, `src/controle_ia/lean_essai/epreuve_isolement_v7.py`.
- Artefacts et attendus (`scripts/lean_essai_d1a_v4/artefacts_r5_v4/`, dossier que le pilote copie sur la machine) :
  `iso_lecture_v3.lean`, `iso_ecriture_v3.lean`, `iso_persistance_ecrire_v3.lean`, `iso_persistance_lire_v3.lean`,
  `iso_reseau_v3.lean`, `limite_code137_v1.py`, `limite_memoire_lean_v1.lean`, `attendus-v6.json`.
- Scripts (`scripts/lean_essai_d1a_v11/`) : `compiler_comme_bac_v1.sh` (lecture du pas 2),
  `essai_verificateur_hors_machine_v3.py`, `mutations_gardes_v11.py`, `piloter_poste_v11.sh` (copie du v10 : exécuteur et
  épreuve v7 dans la phase « apres », rien d'autre ; noms des sorties `*-v6.*` gardés comme aux pilotes précédents).
- Essais : `tests/test_lean_essai_executeur_v7.py`, `tests/test_lean_essai_epreuve_v7.py`, `tests/test_lean_essai_pilote_v11.py`.
- Pièces (`pieces-causes-essai-3-v1/`) : attendu avant compilation, sorties de compilation des sondes v2 et v3, essai de
  mémoire Lean en cgroupe, deux essais hors machine (v2 rejoué, v3), deux journaux de mutations.
- Chaque fichier a son empreinte compagnon `.sha256`.
