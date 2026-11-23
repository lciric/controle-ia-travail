# Passation — exécutante du saboteur à budget, voie (A) — 2026-11-23 06:25Z

Pièce de travail (classe C), écrite sur le mot de Lazar GO-2026-11-23-09 (reprise possible sur un autre compte sans perte). Session : session_013QMaym1QE4UyYr1H8KU8Rf (Opus 5.5). Mère : session_013QMayjbmQUdDuDs2S3i3XD. Branche : `claude/iib-executante-v6`. Précédente passation : `registres/passations/2026-11-22-2310-executante-saboteur-voie-A.md` sur `main` (972af334…). **La course tourne : rien n'est arrêté par cette passation.**

## Mandat
Exécuter la course du saboteur à budget, organisme retenu v5, voie (A), sous GO-2026-11-22-94 (« go ca urge on accelere turbo max »), dans les lignes de calcul GO-2026-11-22-71 et GO-2026-11-22-75 (prolongée au 31 décembre par GO-2026-11-22-93) ; aucune dépense hors de ces lignes. Départ de la course sous l'exception de crédit GO-2026-11-23-02 (recharge automatique au lieu du seuil de crédit, pour ce départ seul). Autonomie 12 h (GO-2026-11-22-106). Exclue de tout rôle côté sondes.
Interdits de lecture : `prereg/lecture-sondes-barreau8-v1.md`, `src/controle_ia/barreau8_moniteurs/`, `brouillons/barreau8-lecture-sondes-v1/`, branche `lot/compte-4-v1`, `docs/verdicts/`, branche `essai/iib-explo-v1`, toute consigne privée (compagnons `.sha256` seulement), et les sorties de course (`essai/iib-explo-v7`, `essai/iib-explo-v8`) au-delà des noms, tailles et empreintes. Instances intouchables : Vast 61932710 (lentilles), Hetzner 177170935 (organisme), et les quatre arrêtées 58936096, 58936099, 58936100, 60988826 ; ni lues au-delà des champs filtrés ni touchées.

## Fait
- Correctifs du code : 0022 (vitesse au premier lot), 0023 et 0024 (garde de dépense, machine ≤ min(55, 60 − antérieure), plafond total écrit exact), 0025 (vitesse jamais bloquante) ; contre-lus et vérifiés (notes dans `registres/iib-executante/p1-code-course-v1/`). Code de la voie : `f7a5123e`.
- Additif et devis de la voie (A) : brouillons 3 à 7, calcul `calcul-devis-voie-A-v6.py` (a7f82588…), sur `origin/claude/iib-executante-v5-fable-additif-c` (9a5157f4…) ; scellés par la mère.
- Étalonnage : lancement `07b2476a`, machine 62031392, 2,1 h, ≈ 3,61 USD ; désignation scellée : oracle N, 55 tours ; sorties rapatriées sur `essai/iib-explo-v7` (8cac7bbd…) et vérifiées ; machine détruite (traces : `registres/iib-executante/traces-etalonnage-voie-A-62031392-v1/`).
- Course : configuration de la voie `config-iib-organisme-retenu-v5-voie-a-v1.json` (eabbd7e3…) et configuration de course construite à l'exécution (cdcf1f93…) ; commit de course `192a429e` (tête de `prep/iib-tirage-carte-v1`) ; essais sur la machine attendus 313. Machine **62094628** (étiquette iib-voie-a-v1), créée 2026-11-23T04:21:19Z, carte 1,08 USD/h + stockage 0,0333 USD/h, plafond total de la création 58,61 USD. Marque de début 04:42:00Z ; tours 1 (04:58:43Z), 4 (05:49:23Z, avant la limite de rythme 06:34:00Z : A5 tenu), 5 (06:06:13Z) ; 32 épisodes par tour, 0 repli ; six versements poussés sur `essai/iib-explo-v8`.
- Versements de ce jour (cette passation) : `registres/iib-executante/versement-bloc-notes-2026-11-23-v1/` (bloc-notes : contre-lectures, notes de vérification des brouillons 3 à 6, correctifs 0022 à 0025, programmes de brouillons et de calcul, configurations, répétitions, rejeux, sorties de création et de destruction) et `registres/iib-executante/traces-course-voie-A-62094628-v1/instantane-20261123T0630Z/` (progrès, surveillance, lancement, journaux, configuration citée, traces de location en champs filtrés, quatre premières lignes de l'impression de création). Garde des secrets à 0 (clés par leur nom seulement : `$HF_TOKEN`, `$CONTROLE_IA_GITHUB_…`). Non versés : environnements Python (`venv`, `vast11`, `vast-venv`), copies de dépôt (`regmain`, `go-bf.md`, `go-commit.md` : copies de `registres/go.md` de `main`), worktrees (`lance`, `course`, `rap`, `reg`), sorties rapatriées de l'étalonnage (déjà sur `essai/iib-explo-v7`), `amorce.sh` (fichiers du dépôt aux empreintes 4140d3b3… et 03962c29…).

## Reste
1. Surveiller la course jusqu'à sa fin écrite (FIN) ; relevés au plus toutes les 30 min, messages courts à la mère sur les faits seulement.
2. À la fin : arrêt par l'identifiant ; rapatriement de `essai/iib-explo-v8` et vérification de chaque fichier (noms, tailles, empreintes) ; destruction (`RAPATRIEMENT_VERIFIE=oui`, `IIB_INSTANCES_INTOUCHABLES=58936096,58936099,58936100,60988826`) ; compte rendu selon l'étape 8 du § 4.4 de l'additif ; passation scellée ; mise à jour des registres de `main` (dépenses, arrêts) par la mère.

## Réserves
- La surveillance ne survit pas détachée : elle tourne comme tâche de fond suivie par la session (tâche `bvhw95yil`, lancée 06:16Z, limite 2 h) et doit être relancée toutes les 2 h. Sur un autre compte : relancer la commande ci-dessous dans une session neuve.
- Le lanceur local lit `registres/go.md` corrigé de `main` placé, non committé, dans la copie `scratchpad/lance` (option b, R-5015).
- Un commit de registre porte la mauvaise ligne Claude-Session (celle de la mère) ; consigné dans la passation précédente.
- Aucun essai ne prouve le chemin sans numpy du 0024 (vérifié à la main par le contre-lecteur).

## PROCHAINE ACTION exacte
06:35Z : relire `controles-course-1/progres.txt` et `surveillance.txt` (la tâche de fond neuve doit écrire POURSUIVRE) ; puis relevé toutes les 30 min ; 08:14Z : relancer la surveillance. Commande (S = bloc-notes de la session) :
`cd $S/lance && GO_ID=GO-2026-11-22-75 IIB_REGISTRE_GO=$S/regmain/registres/go.md IIB_BRANCHE=essai/iib-explo-v8 IIB_TIRAGE=carte IIB_AMORCE=scripts/amorce_instance_iib_course_v5.sh VAST=$S/vast11/bin/vastai bash scripts/lancer_iib_v3.sh surveillance 62094628 $S/controles-course-1 >> $S/surveillance-course.txt 2>&1`
Reprise sur un autre poste : worktree détaché à `07b2476a` (lanceur), `registres/go.md` de `main` copié à côté, vastai 1.11.0, dossier de contrôles reconstruit depuis l'instantané versé ici (configuration citée, progrès, surveillance).

## Machines, serveurs, tâches planifiées actifs
- Vast **62094628** (iib-voie-a-v1), course en marche. Aucune autre machine à moi. Aucun serveur Hetzner à moi.
- Tâche de fond : `bvhw95yil` (surveillance, jusqu'à ≈ 08:16Z).
- Tâches planifiées vers cette session : `trig_0148Pz5GRgTZ7P7b2mNDayvJ` (06:35Z, garde du tour 4, déjà tenue), `trig_01L4PrBKf5FzgPWcNQ7hBmn3` (08:14Z, relance de la surveillance), `trig_01B9MJYeLtz5UboZkqQJBLEz` (2026-11-24 09:50Z, échéance moins 30 min), `trig_01RhLL5Ajw3YBXfQpFEr29LR` (2026-11-24 11:41Z, second rempart, `calcul-devis-voie-A-v6.py second-rempart 1795515638 $(date +%s) ETAT`). Vers la mère : `trig_017j59LP25RLpgvdYSf7Si4h` (2026-11-24 11:41Z, troisième rempart, arrêt seulement).
- Échéance absolue de la course : 1795515638 = 2026-11-24T10:20:38Z ; seuil des remparts 11:40:38Z.

## Branches et commits
| Objet | Branche | Commit |
|---|---|---|
| Registres de l'exécutante, cette passation | `claude/iib-executante-v6` | voir le commit qui la porte |
| Additif, devis, calcul | `claude/iib-executante-v5-fable-additif-c` | 9a5157f4 |
| Code de course | `prep/iib-tirage-carte-v1` | 192a429e |
| Lancement de l'étalonnage (lanceur) | — | 07b2476a |
| Sorties de l'étalonnage (cloisonnées) | `essai/iib-explo-v7` | 8cac7bbd |
| Sorties de la course (cloisonnées, en cours) | `essai/iib-explo-v8` | — |

## Sessions avec qui je parle
Mère session_013QMayjbmQUdDuDs2S3i3XD (seule interlocutrice). Sous-agents Fable et Opus de rédaction et de contre-lecture : finis, rien en cours.
