# Rapport des ajouts d'avant scellement de la relance v4 de R1 (I1 à I5 de la contre-lecture R2) — v1

- Auteur : développeur neuf (sous-agent, Opus 5.5) ; je n'ai écrit ni le code v4, ni l'addendum, ni sa contre-lecture.
  Consigne `docs/notes/runs-r1-r2-r4-v1/consigne-developpeur-r1-v4-ajouts-v1.md`
  (`a0b700140f6284d11469e1d14188c49e781ea1d31cbc1fe81632c4fc6ec56074`, vérifiée par `sha256sum` avant lecture).
- Pièces qui font foi, empreintes vérifiées : addendum brouillon 2 `prereg/R1-addendum-relance-v4-brouillon2.md`
  (`fed5fd3b832d1836abb27dc2e934aabcdbf5f3f4444e3cbb1c86359ee7986496`) ; contre-lecture
  `contre-lecture-relance-v4-v1.md` (`e224ae8ab36541392e88bb0e406a6dc133795b430f676e99a5f0706a13d9a9f1`) ; complément
  scellé lu au commit `4b47db7b` (`049f20ba…`, égal). Arbitrage de la mère appliqué : témoin non exact → lot puis repli.
- Dates (UTC, `date -u`) : début 06:20:41 ; fin : dernière ligne.
- Arbre `/home/claude/wt/r1-v4/`, branche `prep/r1-relance-v4`, tête `b001fec2` : **fichiers neufs seulement**, aucun
  commit, aucun `.sha256`, aucun fichier existant modifié (`git status` : seuls des fichiers non suivis). Aucun réseau,
  aucun modèle téléchargé, aucune carte, aucune dépense, aucune tâche planifiée créée. Commandes sous
  `timeout 1200 nice -n 10` (un départ du banc lancé par erreur sous `timeout 7000` a été arrêté par son PID à 11 s,
  avant tout résultat : déclaré dans sa sortie).
- Lectures sous `donnees/` : les textes de P3 (`textes-actions-p3.jsonl` : empreinte du fichier et champ `episode`, ordre
  des épisodes) par le pré-vol ; **aucun score** (`scores-p3.npz` non ouvert : le pré-vol n'appelle pas
  `charger_pieces`), aucun tableau d'activations, aucune sortie d'analyse de détection. Les essais jouets lisent, comme
  avant, `donnees/T0.7-*` (faits du P3 jouet) ; le banc v2 ne copie plus que ces deux dossiers de `donnees/`. Sorties
  jouets lues (P3 jouet : aucune donnée réelle).

## 1. Fichiers neufs et empreintes (sha256)

Voir le tableau final (§ 7).

## 2. Ce qui est fait, point par point

**Arbitrage M7 (mère) : témoin non exact → lot puis repli.** `resolution_graine_lot_v3.py` (copie de la v2, écarts
marqués `# v3`) : `VOIE_SI_NON_EXACT = VOIE_LOT` ; `voie_de_reparation` rend « lot_fidele » pour « exact » et « non
exact » (« sans mesure » : arrêt) ; la passe forcée seule est retirée de l'étape « reparation » (garde : toute autre
voie arrête) ; la passe forcée reste la troisième voie de chaque cible non retrouvée. Résultats nommés
`resolution-graine-lot-v3-{temoin,reparation}.json`. Configuration neuve `prereg/R1-reparation-v4-config-v2.json` = v1
sauf `voie_si_temoin_non_exact` = « lot_fidele » (diff d'une ligne ; `exiger_config` refuse « passe_forcee »).

**I1 — garde de chaîne et recalcul de réception.** `chaine_table_v4_v1.py` : `exiger_chaine` (résultat de la réparation
scellé, rattaché, même configuration, commande et version de la v3, sans `arret.json` ; table v4 par le chargeur du
rejeu v4 ; `resultat_reparation_sha256` = sceau du résultat ; table v3 la même ; entrées hors des cibles = les entrées de
la table v3 à l'identique ; entrées « identifiants » = **exactement** les retrouvées, identifiants action par action et
sceau cité ; entrées `non_resolu` = **exactement** les non retrouvées ; `non_resolus_v4` et comptes) ;
`recalculer_a_la_reception` (la chaîne, puis `construire_table_v4` recalculée égale **à l'octet** à la table versée).
Le script v2 l'appelle en étape « chaine » entre « table-v4 » et le rejeu (arrêt avant le rejeu sinon, rien n'est lu) ;
ligne de journal « chaîne de la table v4 : conforme ». Essai `tests/test_chaine_table_v4_v1.py` : cas sains (4
retrouvées, recalcul égal ; une non retrouvée) ; artefacts : **une retrouvée rétrogradée en `non_resolu`** (table
cohérente, acceptée par `rv2.charger_table_v4` : le trou est bien réel ; refusée par la chaîne), sceau faux, entrée v3
retirée, identifiants changés, sceau non cité, autre configuration, table d'une autre réparation, réparation arrêtée,
table resérialisée (chaîne conforme, réception refusée à l'octet). Recalcul de réception rejoué aussi sur la sortie de
la session 2 répétée (§ 3) : égal à l'octet.

**I2 — destruction par l'identifiant, protocole C-3 à C-5, gardes 45 et 57 USD.** `garde_depense_v4_v1.py` rend
mécaniques, pour session-depot et les deux tâches : `commande_destruction` (identifiant entier exact seulement) ;
`heure_destruction` (`T0 + H`, `H = (57 − imputées − disque) / prix − 15 min`, refus sans marge) ; `decision_horaire`
(alerte à 45 engagés ou projetés, destruction à 57 projetés, destruction à la fin de l'amorce, demande d'extension si la
fin projetée dépasse l'heure de (ii), échec visible sans identifiant, `T0` ou prix, rien sur une instance absente) ;
`decision_destruction` ; prompts non armé / armé / d'essai et relecture (`prompt_tache`, `lire_prompt`,
`exiger_armement` : identifiant et `T0` exacts, heure `T0 + H`, départ de (ii)) ; lecture aveugle (`filtrer_journal`) et
projection (`projection_fin`, `episodes=k/89`, + 75 min). Les quatre épreuves du complément (et trois variantes de la 4),
aux seuils v4, sur les valeurs consignées de l'instance 58851293 : conformes (`epreuves-garde-depense-v4-sortie-v1.txt`).
Devis v2 (`devis-relance-v4-v2.md`) : garde par identifiant (la v1 écrivait « TERM par PID »), scénario non exact.

**I3 — surveillance v4.** `verifier_surveillance` : 180/120 (session 1), 2 200/2 100 (session 2), tests au nombre de
l'addendum, `cibles=89 lots=28`, table de version 4 ; une autre valeur lue → « detruire » ; essais sains et artefacts
(720, 600, 329, 88, 27 ; valeurs de session 2 en session 1). Appliquée aux journaux de la répétition : session 1
« conforme » (plafond 180, délai 120) ; session 2 « detruire » sur `cibles = 4 ≠ 89`, `lots = 1 ≠ 28` (P3 jouet :
attendu, les constantes sont celles du réel ; plafond 2 200 et délai 2 100 lus égaux) ; filtre : aucun `lecture=`,
`retrouves=`, `voie=` ni la ligne « témoin lu … (lecture : …) » ne passent.

**I5 — indépendance des lignes.** `mesure_independance` (v3), écrite dans `lots_rapport[k]["independance_des_lignes"]`
de chaque lot réparé (essai à plusieurs cibles) : accord des lignes connues (seuil 1), choix contraints, hors
candidats, captures, **avant** et **après** la première action en échec localisé d'une cible ; cibles non retrouvées sans
échec localisé déclarées ; `reserve_independance` (avant propre, après non propre) et `reserve_lecture_exact` (lot sans
cible en échec, lignes connues non propres). Aucune entrée, classe ni voie n'en dépend. Essais : unitaires (sains,
artefacts : désaccord ou capture différente après l'échec, désaccord avant l'échec, aucun échec, premier et non dernier
échec) et sur un lot jouet rejoué (cible en échec au pas 1 : aucune réserve ; un jeton faussé après l'échec : réserve).
Limite déclarée : non mesurée dans les essais à une cible (`resolution_graine_lot_v1.resoudre_episode_lot`, non modifié).

**I4 — épreuves avant scellement.**
1. *Pré-vol sur les vraies pièces* (`prevol-v4/prevol_r1_v4_v1.py`, sortie `prevol-r1-v4-sortie-v1.txt`) : **0 écart** —
   empreintes du manifeste, des fiches, des textes, de la table v3 égales à la configuration v2 ; 240 épisodes ; 30 lots
   de 8 (ordre des textes) ; table v3 version 3, 22 entrées ; 89 cassés du diagnostic (§ 4 de sa sortie `f3e0f42d…`,
   empreinte vérifiée), lot et rang égaux à ceux recalculés, aucun dans la table v3 ; **89 cibles dans 28 lots** ;
   lots 2 et 13 sans cassé (lot 2 : une entrée de la table v3) ; lot 3 : 7 cibles ; captures de P3 recalculées depuis
   les graines égales aux fiches : 132 actions, 116 épisodes, **8 dans le lot 2**, 0 dans le lot 13, 48 dans les cassés.
2. *Banc de mutations rejoué en entier* (`scripts/banc_mutations_r1_v4_v2.py`, sortie
   `banc-mutations-relance-v4-sortie-v2.txt`) : 37 mutations (les 15 de la v1 reportées sur la v3, M04 inversée ; 22
   neuves : I1, I5, voie unique, I2, I3, et les gardes de M6 : `exiger_execution_unique`, `exiger_comptes_attendus`,
   `exiger_temoin` (témoin arrêté, essai ajouté), « en trop » de `classer_episodes_v4`, version de `charger_table_v4`),
   deux groupes, chacun avec son cas sain. **Passe 1** : 35 tuées sur 37 (survivantes M19 : la table v3 jouet est vide,
   l'artefact « entrée v3 retirée » ne s'éprouvait pas ; M37 : garde double, le rejeu v4 revérifie la version) ; essai
   renforcé (entrée en trop hors des cibles), cible de M37 complétée (`test_resolution_graine_lot_v2.py`). **Passe 2,
   entière, sur les essais finaux** : cas sain 39 passés, aucun sauté ; **37 tuées sur 37** (18 + 19).
3. *Répétition jouet des deux sessions* (`repetition-jouet-v4/`) : amorce v2 et script v2, `MODE=jouet`,
   `PREREG_ABSENT=1`, dépôt nu local, jetons factices. Session 1 saine : code 0 (témoin jouet « exact » sur le lot 1).
   Versement du témoin (commit neuf, `runs/` et `diag/` du run seuls). Session 2 saine **jusqu'au rejeu** : code 0
   (réparation 4/4 par `lot_multi`, table v4 écrite et scellée, chaîne conforme, rejeu v4 « conforme », table version 4,
   `table_empreinte_citee` faux). Artefacts : seconde exécution (code 1, R12), `PLAFOND_AMORCE_MIN` 0 et 10 000 (code 1),
   `SESSION` inconnue (code 1), témoin arrêté (code 2), sceau du témoin faux (code 2), session 2 sans `TEMOIN_RUN`
   (code 2).
4. *381 essais avec le tokeniseur* : **impossible ici** — le tokeniseur de Llama 3.1 n'est ni dans un cache local ni
   sur le disque, et le réseau est interdit. Collectés : **381** (les 26 fichiers de `CIBLES` du script v2 : 358 + 15 +
   1 + 7) ; suite des 26 fichiers rejouée sans tokeniseur : **363 passés, 18 sautés (ceux qui lisent le tokeniseur),
   0 en échec** (23 + 21/8 + 319/10, `essais-ajouts-relance-v4-sortie-v1.txt`).

## 3. Sorties

| sortie | résultat |
|---|---|
| `essais-ajouts-relance-v4-sortie-v1.txt` | 26 fichiers sans tokeniseur : 363 passés, 18 sautés, 0 en échec (dont les 23 essais neufs : 23 passés) |
| `banc-mutations-relance-v4-sortie-v2.txt` | passe 1 : 35/37 (survivantes rapportées) ; passe 2 entière : 37/37 tuées |
| `epreuves-garde-depense-v4-sortie-v1.txt` | 7 épreuves conformes (1 absente, 2 échec visible, 3 rien à 1,79 USD, 4a absente, 4b alerte, 4c destruction, 4d échec visible) |
| `prevol-v4/prevol-r1-v4-sortie-v1.txt` | 0 écart (ci-dessus) |
| `repetition-jouet-v4/codes.txt` et journaux | ci-dessus ; `reception-jouet.txt` : recalcul égal à l'octet |

## 4. Ce qui ne peut pas être fait ici (sans carte, sans tokeniseur, ou hors de cette tâche)

- Suite des 26 fichiers au commit cité **avec le tokeniseur** de la révision de P3 (« 381 passed », aucun sauté).
- Classement de base sur les vraies pièces (151 conformes en longueur, 129 identiques de base) et recalcul indépendant
  des 89 cibles et 28 lots : tokeniseur requis ; le pré-vol les recoupe avec la liste du diagnostic seulement (la garde
  `exiger_comptes_attendus` les recalcule sur l'instance avant tout calcul).
- Création, listing, armement et épreuves **réelles** des deux tâches planifiées : par session-depot, avant chaque
  création (les règles qu'elles appliquent sont éprouvées ici).
- Témoin, réparation et mesure de l'indépendance sur la carte.
- Contrôles d'avant l'installation rejoués au commit de scellement ; banc et répétition à refaire au commit cité si un
  fichier change.

## 5. Ce que le texte scellé devra citer ou changer (relevé, non appliqué : je ne touche pas à l'addendum)

- « Chemin de la configuration de la réparation : `prereg/R1-reparation-v4-config-v2.json` » (canonique
  `c34bf464177468d160975800da3cfe13d67e722a2e3b3c3e4c3c46d503ab680a`, fichier : § 7) au lieu de la v1 (`a5a61077…`).
- « Tests attendus : `381` » (26 fichiers : les 23, plus `test_resolution_graine_lot_v3.py`, `test_chaine_table_v4_v1.py`,
  `test_garde_depense_v4_v1.py`) ; V4-E10.
- Modules et scripts : `resolution_graine_lot_v3` (réparation, témoin, table v4), `chaine_table_v4_v1`,
  `garde_depense_v4_v1` ; `scripts/r1_v4_instance_v2.sh`, `scripts/amorce_instance_r1_v4_v2.sh` (commande de création :
  `amorce_instance_r1_v4_v2.sh`) ; banc `banc_mutations_r1_v4_v2.py` ; empreintes au § 7 ; V4-E6.
- Témoin non exact → lot puis repli : P-T (« alors : voie de la passe forcée »), plan d'analyse étape 3 (« voie de la
  passe forcée »), critère « Témoin non exact », Statut (« par la passe forcée du cœur sinon ») ; durée et coût :
  devis v2 (non exact ≈ 18 USD au milieu, ≈ 36 au haut ; pire cas inchangé ≈ 57,2).
- V4-E5 : la garde de chaîne est l'étape « chaine » du script (arrêt avant le rejeu, rien n'est lu), non un « echec » du
  rejeu ; réception : `python -m controle_ia.runs_nuit.chaine_table_v4_v1 --config … --reparation … --table …
  --reception --tokeniseur …`. Attentes de réception : chemins `resolution-graine-lot-v3-*.json`.
- V4-E12 / surveillance : jalon « chaîne de la table v4 : conforme » ; règles et filtre : `garde_depense_v4_v1`
  (projection `+ 75 min`) ; les sorties citées ci-dessus (pré-vol, banc, répétition, épreuves) avec leurs empreintes.

## 6. Marqueur restant

Dans l'addendum brouillon 2 : « À REMPLIR » (commit du code d'analyse), seul. Aucun marqueur dans les fichiers neufs.

## 7. Fichiers neufs (sha256, fin de rédaction)

| fichier | sha256 |
|---|---|
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/banc-mutations-relance-v4-sortie-v2.txt` | `fe833d20843afd5b6d0815fe70e81b57e5f15deebf3269632c4e3f55fb33622d` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/devis-relance-v4-v2.md` | `dac7a0a1906ff42eecd391b55eeb285845eee31596b6e857d1b75e586bae6152` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/epreuves-garde-depense-v4-sortie-v1.txt` | `f2eb1d8fb7498a43067df2fdf77b199630921e42d28612f147d3c3008ff31fbe` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/essais-ajouts-relance-v4-sortie-v1.txt` | `98b53bd4e4933d45990de845f12e0ab8166d259af9375888651e634fd075191c` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/prevol-v4/prevol-r1-v4-sortie-v1.txt` | `e10815f6f21862f5a6b3bd7b8fb6d6fbf9bebda16116a12f38233d4e816058c4` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/prevol-v4/prevol_r1_v4_v1.py` | `85bc760eee37f63b4634d6113afe2af107a28974b0ba051f4f9ddb4229cdb9c8` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/amorce-plafond-10000.log` | `0a934dcfd723420f3b579acce9ad6014e66888e8716127399d2be1623946a47e` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/amorce-plafond-zero.log` | `81cf66a27b0de145cc1dc90d998f19d2ab9b15ca64a7cf96d7ffef213b83e263` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/amorce-reparation-sain.log` | `d69e54654be40cdfa698c9d791a797ffce2a059227ce5275ceb4be00bb933c5d` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/amorce-sans-temoin-run-2.log` | `7a66497492ba37d4ee48ce805eb396897515ef7a12c69508f74183bd511bbd77` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/amorce-sans-temoin-run.log` | `2ca4447dc2a2f661c53a872eeefce35874344aef98552d3e850f90e50e83df51` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/amorce-sceau-temoin-faux-2.log` | `3f7ca2ef20f216d23d16346bce44d34f355b8bf4377e8cad9dee74d874d497b9` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/amorce-sceau-temoin-faux.log` | `d4db3888866b51f2bb75ab6580bf8511b9870d1944fb638e9f638e8e0abc9b81` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/amorce-seconde-execution.log` | `41e420faa84b4739240bc16d5f67f739acff357e0c81c452dbe6866f63185750` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/amorce-session-inconnue.log` | `e7cd6840a59290933f93d792b518e6f4906249b035ec64dc737ce8b9a73b8394` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/amorce-temoin-arrete.log` | `31fa69c362c308b001f5cfd9bffe77246bf6455911a6dc3b990a42e871eae2c1` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/amorce-temoin-sain.log` | `6961b2829f0cbfb4f9b0a534c428bb59b5941a05fc5091d00a606450be1e8704` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/codes.txt` | `95f097cb6b3a1beee7fd0fc8c1302067dc00a9513cb512d240a2c1b797c7b788` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/inspection-reparation-jouet.txt` | `0549b9d0863510d3698e1888fd15184fa7bbcb56d3ebc1a49bd271be736a7a4f` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/journal-session-reparation.txt` | `daf6e700bcb32c0a13f326ffca50729fa1cda895a3f9a05ec00d67032c029c53` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/journal-session-temoin.txt` | `ccc994f7ab3df6745bfc62fe8a83bc862a761e599cd3fa17e528a672055367cd` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/lancer.log` | `b0fffe52ee5893b15fcc5bb27e4417f71919027f59b7e8824ab578ad31406c55` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/lancer_repetition_v4.sh` | `7aa938b5fcb9ce0ec23d9c1c186fb660d0c7b425ab78447232329bf0f35df15b` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/lancer_repetition_v4_complement.sh` | `626c19f9efe26c78d05761b7fecd0b90f8a481d136677ac640de0e9a2189dbd4` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/preparation.json` | `bd3b3c015bf289f9639c8f34d7a27499bcb6d3a929a9f1e3eb3b709c1b7c389d` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/preparer.log` | `6902a3a7daa2234e73a81cfc8cbcabffba468cf3e8de3305e77ef146c379d935` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/reception-jouet.txt` | `8f96c339da7da9f540e238a4d62cf97666d46df1af04ee0330ab081cf9778d45` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/surveillance-repetition.txt` | `3af22472b459b2e5a99a4888b41c31823cf951af159e76a93b8db057cc89d6c2` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/repetition-jouet-v4/test_preparer_repetition_v4.py` | `689b78efb1fe05b46090834f66297eff6771726945929eb8f96176d7ae59e18b` |
| `prereg/R1-reparation-v4-config-v2.json` | `4d0655d1bac5b15d6cb604e5853bed0bfe1eb48d6235772e39b86a698b8d85e5` |
| `scripts/amorce_instance_r1_v4_v2.sh` | `22e64d72745168f947a37690e9bb29170011ef38f0649b6bbc7ca6f8825445b1` |
| `scripts/banc_mutations_r1_v4_v2.py` | `50a788ed05b155e28e1147346886cf37418b87f12ab9288e7bae5168797fce22` |
| `scripts/r1_v4_instance_v2.sh` | `a02eda0c4c8519a1d7d3ddd452001a7b8357c7e6925ca1e9c28be703d362b5ae` |
| `src/controle_ia/runs_nuit/chaine_table_v4_v1.py` | `a015e89fd1cf39d887a05617298b7c930c939f60449b2c0ed9e75975d097bdd1` |
| `src/controle_ia/runs_nuit/garde_depense_v4_v1.py` | `1f6d4b91db36a6e439c984f5813bee419faf0a7b0ef4e5379b28ccaddb05c4dc` |
| `src/controle_ia/runs_nuit/resolution_graine_lot_v3.py` | `9ce6d17818a04853db57fdbb70e347bc9fdd0153ba91c14b9530818c6b29f6e3` |
| `tests/test_chaine_table_v4_v1.py` | `f9583053deb2af39b4bc3d7d8628eed7f28bb66a3fd79ed94bf428d344afeea8` |
| `tests/test_garde_depense_v4_v1.py` | `1cdb1a1f1f5b74073f260e1196a53581b9b0c36e2ecdaa7d84d0479fbd6dc9ee` |
| `tests/test_resolution_graine_lot_v3.py` | `a50e19347dba28e3074093cff80de1d69794e7dde012f0a4fb71489c33d4618c` |

Réserves : (1) disque plein pendant le premier départ du banc et pendant deux artefacts de la répétition (copies des
PDF de `docs/sources`) : banc corrigé (aucun PDF copié), relancé ; les deux artefacts rejoués
(`lancer_repetition_v4_complement.sh`), leurs premiers journaux gardés ; (2) une première préparation de la répétition a
échoué sur un chemin de copie (`jouet-p3/README`), corrigée, relancée dans un dossier neuf ; (3) la redondance
« entrées `non_resolu` = non retrouvées » est impliquée par « entrées identifiants = retrouvées » (une entrée par cible) :
pas de mutation séparée ; (4) la répétition a tourné sur les fichiers finaux, sauf `test_chaine_table_v4_v1.py` et
`banc_mutations_r1_v4_v2.py`, renforcés après (ni l'un ni l'autre n'y est exécuté ; empreintes comparées) ; (5) M3 (délai de 2 100 min sous un plafond de 2 200) et M4 (poussée par lot) non traités : hors
de I1 à I5.

Ce rapport : empreinte rendue à l'appelant. Fin de rédaction : 2026-11-04 07:19:50 UTC (`date -u`).
