# Passation — exécutante du saboteur à budget, voie (A) (session_013QMaym1QE4UyYr1H8KU8Rf), 2026-11-22T23:10Z

Accords : GO-2026-11-22-94 (session, échéance le 25), sous GO-2026-11-22-75 (60 USD ; prolongé par -93). Autonomie GO-2026-11-22-106. Pièces de travail : branche `claude/iib-executante-v6` (registre des nœuds, correctifs, contre-lectures, traces).

## Fait
- **Code de la voie** : correctifs 0022 à 0025, chacun contre-lu puis vérifié (« autorisable »), poussés sur `prep/iib-tirage-carte-v1`. Code f7a5123e. Commit de lancement 07b2476a, qui porte la configuration de la voie (eabbd7e3…) et le registre go.md de main.
- **Additif et devis de la voie (A)** : brouillons 3 à 8 (Fable ; Opus en remplacement pour le 3). Scellés par la mère sur main (eca238f5, R-5009) : additif 8e1d340a…, devis 5bcfede2….
- **Étalonnage, voie (A)** :
  - machine Vast 62031392, créée à 20:04:39Z sous GO-2026-11-22-75 ;
  - tirage sur la carte ; essai de vitesse passé (lot 2 à 10,0 minutes, limite 35,5) ;
  - 28 lots, phase « fin » à 22:10:10Z ;
  - machine arrêtée à 22:10:54Z, puis détruite par l'identifiant à 22:13:47Z (rapatriement vérifié).
- **Rapatriement** : `essai/iib-explo-v7`, 62 fichiers vérifiés sur 62, aucun écart.
- **Passage unique des conditions** (22:12Z) : issue N, 55 tours. Désignation scellée, poussée en 8cac7bbd ; designation 78045af7…, branches 865e8095….
- **Compte de la voie** : 3,61 USD au plus.
- **Traces** de la location et de la surveillance versées scellées sur `claude/iib-executante-v6` (b1326937), garde des secrets à 0.
- **Garde de la course**, jouée à blanc : code 0 pour 55 tours. Tour 1 au plus tard 32 minutes après la marque de début, tour 4 au plus tard 112 minutes.

## Reste — la course de la voie (A), suspendue sur l'ordre de la mère (23:01Z)
- Blocage : le crédit du loueur. 36,99 USD lus à 22:19Z ; 53,39 exigés (coupure de 51,39 plus 2 de marge). Recharge de Lazar au réveil.
- La machine du barreau 5 (62047649) est détruite : ce blocage-là est levé.
- Au signal de la mère, dans l'ordre :
  1. relire le crédit et l'inventaire (une machine d'un autre chantier hors de la liste des intouchables : nœud) ;
  2. `echeance 55 <compte> $(date +%s) 30 11` ;
  3. `garde-de-rythme 55 <compte> 55 $(date +%s) 106.2` ;
  4. envoyer à la mère la ligne d'engagement et l'échéance ; elle arme le troisième rempart ;
  5. imprimer la commande de création, avec l'amorce de la course (`IIB_AMORCE=scripts/amorce_instance_iib_course_v5.sh`), 313 essais attendus, la branche `essai/iib-explo-v8`, `IIB_TIRAGE=carte` et la dépense antérieure de la voie ; vérifier la commande, puis l'exécuter une seule fois ;
  6. surveillance en tâche de fond suivie par la session (elle meurt si on la détache), relancée toutes les 2 heures au plus.
- La course suit le § 4 de l'additif scellé. Les remparts suivent son A3.
- Création au plus tard le 2026-11-24 à 14:30Z (ligne de session).
- Outil du loueur : vastai 1.11.0, dans un environnement virtuel du bloc-notes, à réinstaller (`pip install vastai==1.11.0`).

## Réserves
- Garde de calcul du lanceur : le go.md du commit de lancement a une ligne mal formée. Le go.md de main est posé dans la seule copie locale du lanceur (R-5015). À refaire à chaque nouvelle copie.
- Exigences des sondes pour une course FUTURE : `registres/iib-executante/exigences-sondes-pour-course-future-v1.md` et son erratum 1, sur `claude/iib-executante-v6`.
- Un commit de la branche `claude/iib-executante-v6` porte, par erreur, le numéro de session de la mère dans sa ligne « Claude-Session ».

## Instances (inventaire à 22:19Z)
58936096, 58936099, 58936100, 60988826 : arrêtées, intouchables. Aucune machine du saboteur.
