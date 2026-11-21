# Rapport du développeur du correctif 0011 (environnement de la machine) — v1

Écrit le 2026-11-21 vers 22:05Z par le développeur neuf (Claude Opus 5.5, effort maximal, côté saboteur), sous le mandat
`registres/iib-reconception/mandat-developpeur-correctif-0011-environnement-machine-v1.md` (empreinte abfe45aa9d28…, vérifiée).
Pièce de classe B (instrument), à contre-lire par Fable 5.2 appelé par l'API, puis sceller (accord GO-2026-11-21-84). Exploratoire,
non opposable. Chemins relatifs : au dossier `dev-0011/` du bloc-notes de la session, sauf les chemins du dépôt.

## Verdict
Les deux causes d'environnement de l'arrêt sur la machine louée sont corrigées, et elles seules. La garde « mode jouet sur une
machine payante » ne change pas ; la règle de coupure de l'étalonnage à 12 USD ne charge plus numpy, l'arrêt sur phase illisible
reste. Rejoués dans la machine simulée, les essais arrêtés sur la machine donnent sans le correctif exactement son résumé (5 échecs,
3 erreurs : mêmes essais, même ordre, mêmes messages) ; avec lui, tout passe. Répétition locale entière à blanc : réussie,
« 275 passed ».

## Base, arbre, commit
- Base : `origin/prep/iib-code-v5`, 62356e2ff612a8228b37a8333689e8114099f3c0, arbre ed9b0e48be367670cad0782ccb6fbe2d9ca41b87 (vérifiés).
- Seul commit, tête : 844fda80002059682d6f66a50fe22baee126f559, arbre 95e102f97c8e40dab408ea299d20ab70cffdc968 ; branche locale
  `correctif-0011-local`, arbre de travail `dev-0011/arbre` ; jamais poussée.
- Correctif : `correctifs/0011-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` (sha256 947e5a49…, compagnon) ; appliqué
  sur la base dans un index temporaire, il redonne l'arbre 95e102f9.

## (a) La garde du mode jouet jouait dans les essais
Cause (traces `tests.txt` de la machine) : des appels en mode jouet ne disaient pas qu'ils simulaient un poste sans carte, et la
garde voyait la carte de la machine ; l'essai à blanc par le point d'entrée croyait la masquer par le chemin `/usr/bin:/bin`, or sur
la machine `nvidia-smi` est dans `/usr/bin` et le torch de l'amorce voit la carte.
Correction, côté essais seulement : `carte=False` explicite dans les cinq appels jouets restés implicites (quatre dans
`tests/test_iib_distillation_bout_en_bout_v5.py`, dont trois que l'erreur de mise en place masquait sur la machine ; un dans le second
passage des conditions) ; pour le sous-processus de l'essai à blanc, un poste sans carte écrit par l'essai
(`environnement_sans_carte`, `tests/iib_v5_outils.py`) : accord retiré, chemin réduit à un dossier neuf qui ne porte que `git`,
`CUDA_VISIBLE_DEVICES` vide (torch, s'il est installé, ne voit aucune carte).
La garde garde son effet en production : `exiger_accord` et `carte_visible` sont intacts ; l'amorce exige et pose l'accord, qui seul
suffit au refus ; les artefacts neufs le montrent (accord et carte, carte seule, accord seul : refus avant tout manifeste).

## (b) La règle de coupure à 12 USD sous le python3 du système
Cause : `session_v5` chargeait `configuration_v5` (puis les lois exactes, donc numpy) dès son import ; la surveillance l'appelle par
`python3 -I -B` du système.
Choix : la règle ne dépend d'aucun module tiers ; l'import de `configuration_v5` passe dans `verifier_config`, son seul usage (la
sous-commande `config`). Pourquoi pas l'interpréteur de l'amorce : la surveillance tourne du côté de la session, où il n'existe pas ;
il faudrait une variable neuve et un mode d'échec neuf ; les autres appels de la surveillance (garde de dépense de la ligne,
masquage) sont déjà en bibliothèque standard. Seuil, compte et refus de la phase illisible : même code, inchangé, éprouvé sous
l'interpréteur sans numpy avec le message propre du refus (et non une erreur d'import).

## Essais qui reproduisent la machine
Fichier neuf `tests/test_iib_environnement_machine_v5.py`, quatre essais ; de plus, `_surveiller` (essais de la surveillance)
joue désormais avec le python3 d'un environnement virtuel vide. « Avant » : tout l'outillage des essais, sans les trois corrections
(état exact : `essais/avant/etat-avant-sans-correction.diff`, a996272f…).

| essai | avant | après |
|---|---|---|
| 1. dans le processus : accord posé, carte vue par `nvidia-smi`, carte vue par torch ; artefact (refus de la garde), cas sain (le contrôle suivant parle) | passe | passe |
| 2. point d'entrée en sous-processus : simulation vue ; ancien isolement inopérant (artefact) ; isolement neuf qui masque la carte, aussi au vrai interpréteur (cas sain) ; refus sans isolement | passe | passe |
| 3. règle de coupure sous python3 sans numpy (environnement vide, puis `-I -S`) : 11,04 USD rien, 12,42 USD arrêt, autre phase, phase illisible refusée | échoue : « No module named 'numpy' » | passe |
| 4. les huit essais arrêtés sur la machine, rejoués par un pytest enfant sous la machine simulée | échoue : « 5 failed, 3 errors », comme la machine | passe : 8 |
| trois essais de la surveillance (python3 sans numpy) | échouent : numpy | passent |

Les essais 1 et 2 passent avant comme après, ce qui est attendu : ils éprouvent l'effet inchangé de la garde et la simulation
elle-même ; les cas sains que la machine cassait sont 3, 4 et la surveillance. Sorties : `essais/avant/sortie-essais-avant.txt`
(476516ca… : « 5 failed, 8 passed », dont le résumé enfant « 5 failed, 3 errors ») ; `essais/apres/sortie-essais-apres.txt`
(131505b5… : « 13 passed ») ; fichiers touchés en entier, `essais/apres/sortie-fichiers-touches-apres.txt` (d9a83be8… : « 54 passed »).

## Liste figée, nombre attendu, amorce
- `scripts/tests-cibles-iib-v5-v5.txt`, neuve (la v4 reste) : les 23 fichiers de la v4 et le fichier neuf, sha256
  f9ff477d753c675883d81af2dca6721e4c6bc96128b0d17c850eeddca897f1ac, reportée dans l'amorce v5 (ligne de la liste, en-tête (b)).
- 275 essais attendus (271 et les 4 neufs, compte de collecte) : `ATTENDUS` de la répétition mis à jour. L'ordre de relance devra
  poser `IIB_TESTS_ATTENDUS=275`.
- L'essai de l'amorce suit la liste v5 (24 fichiers, le neuf exigé) ; les bornes des différences de l'amorce tiennent.

## Répétition locale entière à blanc (une fois)
`PYTHONPATH=src python3 scripts/repetition_locale_iib_v5.py … --liste-figee`, sur le commit 844fda80 :
`repetition/sortie-repetition-locale-liste-figee-v1.txt` (1e98dd54…) — « RÉPÉTITION RÉUSSIE » ; suite ciblée de l'amorce,
`repetition/tests-liste-figee-repetition-v1.txt` (8e2a84bf…) — « 275 passed in 467.13s », contrôle du nombre attendu joué, accord
posé pendant la suite ; étalonnage jouet en 28 lots, conditions et désignation, second passage refusé, destruction par
l'identifiant sur le faux outil.

## Réserves
1. Le contrat de CUDA (variable vide : aucune carte) n'est éprouvé ici que sur le torch factice ; le vrai torch et la vraie carte ne
   le vérifient que sur la machine, par l'essai 2 (vrai interpréteur) et l'essai à blanc. S'il ne tenait pas, la suite s'arrêterait
   avant tout chargement du modèle, par la même garde « tests en échec », sans dépense au-delà de la phase d'essais.
2. La configuration de l'étalonnage cite le commit du code : une relance demande une configuration et un ordre neufs (mère).
3. Vu dans le compte rendu de l'exécutante, hors du mandat, non corrigé : l'erreur de chaîne de consignation (`git add -A runs
   diag` hors de l'extraction partielle, C-V4-1).
4. Coût : environ une demi-minute de pytest enfant et quelques environnements virtuels de plus par passage de la suite.
5. Lu : le mandat, CLAUDE.md, le compte rendu de l'exécutante et ses quatre traces permises, le code et les essais du saboteur à
   budget ; rien d'interdit ouvert ; aucune suppression, poussée, machine ni dépense ; jamais la suite complète.

## Fichiers rendus (chacun avec son compagnon `.sha256`)
`correctifs/0011-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` ; `essais/avant/sortie-essais-avant.txt` ;
`essais/avant/etat-avant-sans-correction.diff` ; `essais/apres/sortie-essais-apres.txt` ;
`essais/apres/sortie-fichiers-touches-apres.txt` ; `repetition/sortie-repetition-locale-liste-figee-v1.txt` ;
`repetition/tests-liste-figee-repetition-v1.txt` ; ce rapport.
