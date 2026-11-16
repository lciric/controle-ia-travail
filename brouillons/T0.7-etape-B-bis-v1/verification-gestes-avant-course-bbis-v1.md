# Vérification des gestes d'avant course de l'étape B bis de T0.7 (v1)

- **Auteur** : vérificateur neuf (R2), sous-agent de la session mère, « modèle A ». Il n'a écrit aucun fichier de l'étape B bis
  (ni le texte scellé, ni l'addendum, ni le code, ni le plan de course, ni le rapport de l'exécutant, ni aucune contre-lecture) ;
  il ne sera lecteur d'aucun verdict.
- **Date (UTC, `date -u`)** : 2026-11-16, de 13:09:38 à 13:40:11.
- **Objet** : les gestes d'avant course joués par l'exécutant du « modèle B » de 12:27:41Z à 12:59:04Z sur la branche
  `prep/t07bbis-code-v1` (arbre de travail `/home/user/controle-ia-travail/.claude/worktrees/agent-a4f221610ce6d5a67`), et son
  rapport `brouillons/T0.7-etape-B-bis-v1/rapport-gestes-avant-course-bbis-v1.md`
  (`6e76287fecbfcf6d40972e46d087c1982774e6e2cc4a89b3524193bedbbdd974`, scellé par la mère tel quel).
- **Statut** : rapport de vérification, écrit en lecture seule ; rien modifié, rien committé ; aucune machine, aucun appel au
  loueur, aucune dépense. Fichier neuf, scellé, non committé.
- **Programmes et sorties du vérificateur** (dossier neuf du bloc-notes, chemin complet :
  `/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/verif-gestes-avant-course-bbis-v1-A-20261116T1310/`) :
  `verif_git_v1.py` → `resultats-git-v1.json` (`1e50978f…`) ; `instantane_v1.py` → `snap-31fa8ac6/` et `resume-snap-31fa8ac6.json`
  (`cb9f0877…`) ; `verif_code_v1.py` → `resultats-code-snap-31fa8ac6.json` (`db3e83f3…`) ; `rejeu_epreuve_v1.py` →
  `rejeu-k300.jsonl` (`fde37b4d…`) et `rejeu-k300-resume.json` (`5647ce47…`) ; `cas_sain_regle_v1.py` → `cas-sain-regle-v1.json`
  (`a16e5614…`).

## Verdict

1. **Prêt pour le feu, quant aux gestes d'avant course.** La fusion M_b, les sept commits, les quatre poussées, l'entropie,
   l'épreuve de niveau, la fiche, la ligne `CODE-BBIS`, l'extrait et la ligne `GO-BBIS` sont conformes au texte scellé, à
   l'addendum et au plan ; les traces (commits, journaux des références, heures des fichiers, fonctions du code rejouées)
   confirment le rapport de l'exécutant sur tous les points vérifiables, sauf une phrase (point 10, écart E1, sans effet sur la
   course). Aucune correction des gestes.
2. **Commit que la création doit citer : `31fa8ac6041faf76b66282e0346750b9aefd4790`** (tête locale égale à la tête distante,
   relevé à 13:15:50Z et 13:34:39Z). À ce commit, l'amorce et la marche trouvent tout ce qu'elles exigent : extraction simulée par
   les motifs de l'amorce, puis garde d'entrée de la marche (`marche_v3.gardes_d_entree`) jouée sur cette vue : acceptée.
3. **Reste avant la création** (point 11) : crédit du loueur d'au moins 20 USD (non consigné à 13:34Z), feu écrit de la mère
   portant `GO-2026-11-14-09`, contre-lecture neuve de la commande exacte (plan, § 7, ligne 5), préavis à Lazar, opérateur du
   modèle A (GO-2026-11-16-06). K4 tient sans exception (pilote 60918148 détruit, absence prouvée à 13:01:46Z, R-2981).

## 1. Fusion M_b

- **Parents** de M_b `f9bd9ba6e7af813207a3d9dd4c24ef280007bcaa` : (1) `77f8a2c2dd6730220f1f1e91488ef8368412bec5`, tête de la
  branche juste avant la fusion, dont le seul parent est `bd1472adf07eeb5a4d95169f57add1bb49290915` (tête relevée par le plan) et
  qui n'ajoute que les quatre fichiers du plan et de la liste des empreintes ; (2) `377a2a0c9b1ec2704374a50537d5c59ae39b0ac7`,
  M0 du plan, commit de `main` (ancêtre de `main` et de `origin/main` : code 0). Base commune `048d8e991ab25d2bf72dc5c5bb35483e9ab3b520`.
- **Aucun conflit résolu à la main**, établi deux fois : (i) le journal de `HEAD` de l'arbre porte, à 12:28:41Z, « merge
  377a2a0c… : Merge made by the 'ort' strategy. », forme que git écrit quand la fusion se conclut d'elle-même (une fusion conclue
  après résolution à la main s'écrit « commit (merge) ») ; (ii) recalcul chemin par chemin sur les 26 551 chemins de la base, des
  deux parents et de M_b : **0 chemin changé différemment des deux côtés, 0 écart** entre l'arbre de M_b et le résultat trivial
  (le côté qui change ; les deux côtés quand ils sont égaux). Quatre chemins changés des deux côtés, aux mêmes objets :
  `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`, `scripts/mots_et_cout_t06_v3.py` et leurs compagnons.
  1 926 chemins changés face au premier parent, 199 face au second ; registre propre au même objet `598607db…` à la base, sur
  les deux parents et sur M_b.
- **Les 103 chemins** : `fichiers-fiche-code-bbis-v3.txt` (`b8fb095b…`) et `empreintes-fiche-code-bbis-v3-ce470564-v1.txt`
  (`291f1d5c…`, compagnons conformes) portent les mêmes 103 chemins, sans doublon, dans le même ordre. Empreintes égales à la
  liste, **103 sur 103**, à `ce470564`, `77f8a2c2`, M_b, `e1caae01`, `70a4a9a8`, `26e4c891`, `ff24998f`, **`31fa8ac6`** et sur le
  disque ; `git diff --quiet ce470564 31fa8ac6 -- <103 chemins>` : code 0. Sur M0 : 61 présents et identiques, 42 absents.
- **Le commit de `main` reçu ne porte aucune sortie de l'étape B** (par les noms seulement) : aucun fichier nommé
  `lecture-t07.json` ou `arret-etape-b.json` à M0, `16484e48`, `77f8a2c2`, M_b, `31fa8ac6`, ni à la tête de `main` relevée à
  13:20Z ; journal des ouvertures du registre partagé à l'objet `76dde869e99c7ab7d05c934405722bd80a1a17bc` (celui de l'étape A)
  sur chacun ; les seuls noms qui contiennent « étape B » hors « bis » sont des fichiers de procédure sous
  `docs/procedures/lecture-7b-etape-b-compte-3-v1/` (92 à M0, à M_b et à `31fa8ac6` ; 138 à la tête de `main` `4efae812` relevée
  à 13:20Z, tous sous ce dossier). Chemins ajoutés par `main` depuis la base : 2 sous `diag/`
  (`diag/20261114-001352-t07-lecture-reel/audit-fuites-t07.json` et son compagnon : l'audit des fuites cité par
  `AUDIT-FUITES-T07`, entrée lue par B bis, non une sortie de l'étape B), 24 sous `docs/verdicts/` (aucun nom de T0.7 ni
  d'étape), 0 sous `donnees/`.

## 2. Branche distante

`git ls-remote origin refs/heads/prep/t07bbis-code-v1` rend `31fa8ac6041faf76b66282e0346750b9aefd4790` à 13:15:50Z et à
13:34:39Z : égale à la tête locale. `origin` = `https://github.com/lciric/controle-ia-travail`.

## 3. Entropie

- `registres/t07-etape-b-bis/entropie-bbis-v1.json` (`f648989bdae47291d8a5504ec33ee5b971bb5ce302f63918e3452c8cff65cfcd`,
  compagnon conforme) : `entropie` 208082752394230630219821407440340422345, **128 bits** (`commun_v1.exiger_entropie(…,
  reelle=True)` : acceptée) ; `commit_code` `ce470564…` ; `outil` `numpy.random.SeedSequence().entropy` (numpy 2.4.6 dans
  l'environnement du dépôt) ; `tiree_le` 2026-11-16T12:29:40Z ; `texte` le texte scellé.
- **Heures** : fichier écrit à 12:29:40.025Z ; commit `e1caae01` à 12:29:40Z (deux fichiers ajoutés, seuls) ; poussé à
  12:30:10Z (journal de la référence suivie) ; **épreuve lancée à 12:30:30.336Z** (heure de naissance de son journal), donc après
  le tirage, le scellement, le commit et la poussée ; sortie de l'épreuve à 12:56:13.340Z ; 1 541,0 secondes murales, ce qui place
  le début du calcul à 12:30:32Z (deux secondes d'import).
- Une seule entropie dans toute l'histoire (aucun autre fichier `entropie*`, aucune suppression sous `registres/t07-etape-b-bis/`
  ni `registres/go-extraits/`) ; la même valeur dans l'épreuve (`graine.entropie`) et dans la fiche ; clé `bbis/epreuve-niveau`,
  `spawn_key` égal à `cle_de_tache("bbis/epreuve-niveau")` (texte, l. 116).
- « Entropie de 128 bits tirée à l'inscription de `CODE-BBIS` » (texte, l. 116) est lue, comme au rapport du développeur
  (interprétation 29, `d8a2e40b…`) et au plan (§ 1.4, § 1.5), comme le premier geste de l'inscription, avant l'épreuve qui en
  dérive ses graines : tenu.

## 4. Épreuve de niveau

- Sortie `registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json`
  (`641adeb57b8c271be60a89af2513805e591a63c7c0dde17883e4ace0d3f59cbf`, compagnon conforme), commit `70a4a9a8` (12:57:04Z, deux
  fichiers ajoutés). Réglages : 64 tâches en deux plis, dix actions par classe et par tâche, 800 directions, 2 000 tirages,
  1 000 jeux par cellule, cellules `nul` (écart 0) et `signal-commun` (écart 0,5), un processus, niveau testé 0,99, seuil 0,01,
  `complete` vrai (recalculé), coût écrit avec le résultat (1 541,0 s murales, 1 519,3 s de processus, quatre cœurs, processeur
  seulement, 0 USD) : **conforme au texte, l. 93**.
- **Résultat** : 0 lecture « au-dessus » sur 1 000 dans chaque cellule, taux 0,0 et 0,0 ; plus haute borne basse −0,0253 (`nul`)
  et −0,0172 (`signal-commun`). Le journal de l'exécutant (bloc-notes, 402 octets) porte la même ligne de résumé.
- **Niveau décisif recalculé par le code, sans choix** : `niveau_retenu` du script → 0,99, aucune cellule au-delà du seuil ; la
  règle de la garde de `registre_bbis_v1.ecrire_fiche_code` → 0,99 ; 0,99 inscrit dans l'épreuve et dans la fiche ; une seule
  épreuve dans l'histoire.
- **Rejeu** (un processus, un fil, priorité 19 ; 13:25:52Z → 13:34:07Z, 493 s) : les 300 premiers jeux de chaque cellule (600
  sur 2 000), aux graines exactes du script, par sa propre fonction `_un` (code de l'instantané du commit de la course) :
  **0 « au-dessus » sur 300 dans chaque cellule** ; toutes les bornes basses sous le maximum du fichier (maxima du rejeu −0,0321
  et −0,0285) ; médianes du sous-ensemble proches de celles du fichier (aire 0,4975 contre 0,4985 et 0,6330 contre 0,6327 ;
  quantile du plancher 0,5242 contre 0,5249 et 0,6581 contre 0,6565) ; le premier jeu, rejoué deux fois, rend les mêmes valeurs au
  bit près. Le rejeu complet (≈ 26 minutes) passe la borne de dix minutes : non fait.
- **R4 et R5 (résultat net)** : 0 au lieu des ≈ 5 qu'une règle au nominal de 0,005 donnerait. Contrôle ajouté, sur des graines
  du vérificateur (jamais l'entropie de `CODE-BBIS`) : la même machinerie de production (`plis_v1.jeu`, `poids_plis`, `regle_a`)
  lit « au-dessus » une sonde qui porte un signal que ses directions n'ont pas (3 jeux sur 3, bornes basses +0,053 à +0,059) et
  « non au-dessus » une sonde échangeable ou un plancher au même signal (6 sur 6). La netteté vient de la forme de la règle (passer
  le quantile 0,95 du plancher de plus que la marge du rééchantillonnage), non d'une incapacité à lire « au-dessus ». Aucune
  réserve sur le niveau ; l'épreuve ne dit rien de la puissance (remarque juste de l'exécutant).

## 5. Fiche et ligne `CODE-BBIS`

- Fiche `registres/t07-etape-b-bis/code-bbis-v1.json` (`ee362bb70c5051097dab90c7978eb550d192f8c90f313317812635884b04e469`,
  compagnon conforme ; écrite à 12:57:20Z ; commit `26e4c891` à 12:57:27Z, deux fichiers ajoutés). Clés `commit`, `entropie`,
  `epreuve_niveau`, `fichiers`, `niveau_decisif`, `texte`, et rien d'autre : `commit` `ce47056455595bc52fad676c0e57ad9d8bef886d` ;
  `fichiers` égal, chemin par chemin, aux 103 empreintes de la liste préparée ; `entropie` égale au fichier d'entropie ;
  `epreuve_niveau` : chemin, empreinte égale au sceau (`641adeb5…`), taux des deux cellules et coût égaux à ceux de l'épreuve,
  niveau 0,99 ; `niveau_decisif` 0,99 ; `texte` `prereg/T0.7-etape-B-bis-v1.md`. `lire_fiche_code` : acceptée. Le contenu que le
  texte exige y est (l. 5 : commit, empreintes des fichiers, entropie ; l. 93 : épreuve citée, niveau inscrit, coût écrit ;
  l. 116 : entropie de 128 bits).
- Ligne (commit `ff24998f`, 12:57:58Z ; seul le registre propre change ; une ligne ajoutée, les deux lignes antérieures
  inchangées) : `| CODE-BBIS | 2026-11-16T12:57:51Z | registres/t07-etape-b-bis/code-bbis-v1.json | ee362bb7… |` ; quatre
  colonnes ; reproduite à l'octet par `t07.registre_v1.ecrire_ligne` ; au registre propre seulement (aucune clé de B bis dans
  `registres/scellements-v1.md` à `31fa8ac6`). Antériorités : `SCELLEMENT-BBIS` (2026-11-14T12:30:30Z) < `CODE-BBIS` ;
  `ADDENDUM-ECART-1-BBIS` (registre voisin, 2026-11-16T00:59:36Z), addendum scellé (`f00eda8a…`, à `31fa8ac6` et sur `main`) et
  ligne R-2959 (00:59Z), tous avant `CODE-BBIS` comme l'addendum l'exige (statut, l. 19).

## 6. Extrait et ligne `GO-BBIS`

- Extrait `registres/go-extraits/GO-BBIS-v1.md` (`33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62`, compagnon
  conforme ; écrit à 12:58:41Z) : une ligne, une fin de ligne, aucun retour chariot ; **égal à l'octet à la ligne
  `GO-2026-11-14-09` de `registres/go.md` plus une fin de ligne**, sur `main` (ligne 328, unique ; têtes `4efae812` à 13:20Z et
  `e3dc0871` à 13:24Z), à M0 et sur la branche ; `t07.registre_v1.extrait_est_une_ligne_de` : acceptée ; même convention que
  `GO-LECTURE-T07-v1.md`. La ligne de GO : « calcul », 40 USD, échéance 2026-11-22, Lazar ; cinq lignes de `go.md` la citent
  (elle-même, GO-2026-11-14-12, GO-2026-11-16-01, GO-2026-11-16-02, GO-2026-11-16-06), aucune de type « révocation ».
- Ligne (commit `31fa8ac6`, 12:59:01Z ; seuls l'extrait, son compagnon et le registre propre changent ; une ligne ajoutée) :
  `| GO-BBIS | 2026-11-16T12:58:51Z | registres/go-extraits/GO-BBIS-v1.md | 33f38e67… |` : **strictement après** `CODE-BBIS`
  (60 secondes, commit suivant) ; `lecture_v2.exiger_ordre_propre` : tenu.

## 7. Registres

- **Registre propre** (`c7bcc49f2ca29027f18eebd68cac9da957a11d638ff9a9406c369c22fdacb108` à `31fa8ac6` et sur le disque ;
  écrit par `f72d2833`, `ff24998f`, `31fa8ac6` seulement) : quatre clés, `SCELLEMENT-BBIS`, `ABSENCE-B-BBIS`, `CODE-BBIS`,
  `GO-BBIS`, toutes dans `registre_bbis_v1.CLES_BBIS` et `lecture_v2.CLES_PROPRES`. Lecteurs du code joués sur la copie de
  l'instantané, sans rien écrire : `lecture_v1.lire_lignes` (mode propre, clés exigées par la marche) et `lecture_v2.lire_lignes`
  (mode propre, quatre clés) : acceptés, aucune clé inconnue ; `lecture_v2.verifier_lignes` : sceaux conformes, lignes
  antérieures ; avec les clés exigées par la lecture, refus attendu « ligne `SCORES-BBIS` absente » (aucune course).
- **Registre voisin des addenda** : écrit par un seul commit, `bd980d72` (2026-11-16T00:59:37Z, sur `main`, reçu par M_b) ; même
  objet à M0, M_b, `31fa8ac6` et sur `main` ; `93f0d3dd…` sur le disque ; aucun des sept commits de l'exécutant ne le touche.

## 8. Le commit de la course, et les rapports

- **À citer : `31fa8ac6041faf76b66282e0346750b9aefd4790`** (plan, § 3 : la tête après la ligne `GO-BBIS`, poussée).
- **Ce que l'instance trouvera à ce commit** (motifs d'extraction lus dans l'amorce elle-même, règle de git en mode non conique :
  le dernier motif qui correspond, sinon celui du dossier parent ; puis la copie des fichiers cités par le registre propre) :
  424 fichiers extraits ; les 103 fichiers de la fiche, tous extraits, à leurs empreintes ; le registre propre et les fichiers
  qu'il cite, avec leurs compagnons (texte scellé, `ABSENCE-B-BBIS-v1.json`, fiche, extrait) ; épreuve et entropie ; le registre
  partagé avec `RUN-CONFIRMATION-T06` (chemin `runs/20261111-151701-t06-reel/manifeste.json`), `VERDICT-P3BIS`,
  `CODE-MOTS-ET-COUT-T06`, `AUDIT-FUITES-T07`, aucune clé de B bis. **`marche_v3.gardes_d_entree` jouée sur cet instantané**
  (variable de l'instance posée dans le seul processus Python du vérificateur ; garde d'ancêtre rejouée sur le dépôt de l'arbre,
  tête `31fa8ac6`, faute de dépôt dans l'instantané) : acceptée (`SCELLEMENT-BBIS`, `CODE-BBIS`, `GO-BBIS`, entropie de 128
  bits, niveau 0,99). Garde de création (`exiger_creation`) : acceptée avec un texte portant `GO-2026-11-14-09`, refusée sans
  (cas sain et artefact ; simulation, aucun feu). `exiger_ancetre(ce470564, 31fa8ac6)` : accepté. Branche de sortie
  `donnees/t07-etape-b-bis*` absente à distance (code 2 à 13:28Z).
- **Vue extraite à `ce470564` (code de la quatrième passe) contre `31fa8ac6`** : ajoutés, les huit fichiers de B bis (fiche,
  entropie, épreuve, extrait et leurs compagnons) et un paquet venu de `main`, `src/controle_ia/organisme_idees_juge/` (80
  fichiers), qu'aucun module ni essai de B bis n'importe ; changés, le registre propre et le registre partagé (deux lignes) ; rien
  à la racine, sous `tests/` ni sous `scripts/`. Les essais du paquet, que l'amorce rejoue, n'ont pas de raison de changer d'issue
  (non rejoués ici).
- **Rapports committés avant la création** : possible sans rien déranger, à quatre conditions : un seul commit ordinaire, jamais
  une fusion (la branche ne reçoit plus `main`), posé sur `31fa8ac6` ; il n'ajoute que les quatre fichiers sous
  `brouillons/T0.7-etape-B-bis-v1/` (ce rapport, celui de l'exécutant et leurs compagnons) ; poussé en avance rapide avant la
  commande ; `git diff --name-only 31fa8ac6 HEAD` relu égal à ces quatre chemins. Raisons : l'amorce clone la branche, extrait
  COMMIT et n'exige que « tête = COMMIT » après l'extraction ; `brouillons/` est hors des motifs et hors du registre propre ; le
  lanceur relit le registre et la fiche sur le disque de sa racine (inchangés) et la garde d'ancêtre passe de même. **Commit à
  citer alors : toujours `31fa8ac6…`** ; aucune garde ne compare la tête de la racine du lanceur à COMMIT. Citer le commit des
  rapports serait équivalent, mais il n'est pas vérifié ici.

## 9. `main`, identifiants de modèle, clés

- **Rien sur `main` de l'exécutant** : aucun commit de `main` postérieur à M0 ne touche un chemin de B bis (registre propre,
  `registres/t07-etape-b-bis/`, extrait, `src/controle_ia/t07bbis/`, plan, rapport) ; aucun commit de l'exécutant n'est dans
  `main` ; les commits de `main` de la fenêtre 12:27:41Z–12:59:04Z sont ceux de la mère (R-2977 à R-2980, par leurs sujets) ; le
  journal de `origin/main` n'y porte que des poussées.
- **Identifiants de modèle** : aucun dans les fichiers versés par l'exécutant ni dans son rapport (les seules correspondances du
  motif sont le nom du dossier `.claude/` et le chemin du bloc-notes). Les messages des sept commits portent les deux lignes
  d'attribution de la session, qui nomment un modèle, identiques entre elles et à celles des commits de la mère faits avant
  12:48Z : hors de la règle des fichiers, rien à corriger.
- **Clés** : 0 motif de clé (forme de `registres/passations/2026-11-10-2206.md`, ligne 7, et formes plus larges) dans le contenu
  de chacun des sept commits et dans le rapport de l'exécutant.

## 10. Le rapport de l'exécutant confronté aux traces

| affirmation | trace | état |
|---|---|---|
| tête `bd1472ad` et quatre fichiers non suivis à 12:21:55Z | journal de `HEAD` : `bd1472ad` jusqu'à 12:27:47Z ; `77f8a2c2` ajoute exactement ces quatre fichiers | conforme |
| processus 612 fini ; R-2976 dit 12:23:08Z ; épreuve partie à 12:30:30Z | R-2976 : « 11:26:24Z → 12:23:08Z » ; naissance du journal de l'épreuve à 12:30:30.336Z | conforme (l'absence du processus à 12:25Z n'est pas revérifiable) |
| `origin` ; à 12:27:08Z, `main` à `16484e48` et branche à `bd1472ad` | `16484e48` poussé à 12:26:22Z, le suivant à 12:30:05Z ; branche à `bd1472ad` jusqu'à 12:29:07Z | conforme |
| `main` à `1332acb3` vers 12:22, `16484e48` à 12:26, `60eee4e5` à 13:00 | commits à 12:20:58, 12:26:19, 12:54:40 (suivant à 13:03:08) | conforme |
| (0) commit `77f8a2c2` à 12:27:47Z, sceaux `e2505df9…` et `291f1d5c…`, même ordre, garde des secrets à 0 | commit, sceaux, ordre, 0 | conforme |
| (a) relevé à M0, à la tête de `main` et à la branche : journal `76dde869…`, aucun nom de sortie | refait à M0, `16484e48`, `77f8a2c2`, M_b, `31fa8ac6`, `main` | conforme ; l'absence de `verdict/t07-etape-b*` à 12:28Z n'est pas revérifiable (branche non interrogée) |
| (b) base, quatre chemins des deux côtés, registre `598607db…`, 61 et 42, fusion sans conflit, parents, 103 sur 103, 1 926 et 199, `082b7e70…`, `93f0d3dd…`, addendum, clés du registre partagé | tout refait | conforme |
| (c) poussée `bd1472ad..f9bd9ba6` à 12:29:07Z | journal : 12:29:07Z | conforme |
| (d) entropie : valeur, 128 bits, `f648989b…`, 12:29:40Z, `e1caae01`, poussée à 12:30:11Z, numpy 2.4.6 | fichier, commit, journal (12:30:10Z), environnement | conforme |
| (d) épreuve : 12:30:30Z → 12:56:13Z, `641adeb5…`, complète, `70a4a9a8` à 12:57:04Z ; identifiant 1736 | heures des fichiers, commit | conforme ; l'identifiant du processus n'est pas revérifiable |
| (d) fiche `ee362bb7…` et son contenu ; `26e4c891` | fichier, commit, code | conforme |
| (d) `CODE-BBIS` à 12:57:51Z ; `ff24998f` ; « BBIS ANCETRE » ; poussée à 12:58:09Z | registre, commit, garde rejouée, journal | conforme |
| (e) ligne de GO unique, sans révocation ; extrait `33f38e67…` ; `GO-BBIS` à 12:58:51Z ; `31fa8ac6` à 12:59:01Z ; poussée à 12:59:04Z ; tête distante | `go.md`, extrait, registre, journal (12:59:03Z), `ls-remote` | conforme |
| contrôles finaux de 12:59:31Z à 13:00:22Z ; registre `c7bcc49f…` ; à 13:00:22Z, `main` à `60eee4e5`, aucune branche de sortie | gardes refaites ; `60eee4e5` poussé à 12:54:43Z, le suivant à 13:03:14Z ; branche de sortie absente à 13:28Z | conforme |
| tableau de l'épreuve, coût, 0,77 s par jeu | fichier de l'épreuve | conforme |
| tableau des sept commits et des poussées | journaux des références | conforme |
| **E1** : « Ce rapport et son compagnon forment un huitième commit, posé après `31fa8ac6` » | à 13:34Z le rapport n'est pas suivi ; son compagnon a été écrit à 13:08:56Z par la mère (R-2982 : « non scellé par lui ») ; aucun huitième commit | **inexact** : une intention écrite comme un fait ; sans effet sur la course ; le rapport, scellé, ne se corrige pas : cette vérification le consigne |
| écarts de forme 1 à 7 | 1 : `77f8a2c2` (12:27:47Z) avant le relevé (12:28:00Z), qui précède la fusion de 41 s ; 2 : M0 = `377a2a0c`, la branche ne porte pas les commits de `main` postérieurs ; 3 : quatre poussées au journal ; 4 : journal de l'épreuve au bloc-notes, 402 octets, la seule ligne de résumé ; 5 : messages du plan et lignes d'attribution ; 6 : module de scellement à la même empreinte `93beeb1c…` ; 7 : non revérifiable | conformes sur ce qui se vérifie ; aucun écart de fond |
| M_b a apporté 2 chemins sous `diag/`, 24 sous `docs/verdicts/`, 0 sous `donnees/` | comptes par les noms | conforme |
| autre processus 10918, priorité 10, lancé vers 12:46Z | `ps` : priorité 10, lancé vers 12:45:54Z | conforme |
| disque libre et charge à 12:25Z, 12:52Z, 13:00Z | — | non revérifiable |
| aucune commande refusée, aucun `git fetch`, aucun processus arrêté | journaux linéaires, sans rejeu ni retour en arrière ; journal de `origin/main` : poussées seulement | cohérent ; non prouvable par les traces |
| rapport écrit à 13:04:08Z (R-2982) | heure du fichier 13:04:08.000Z (sans fraction de seconde, à la différence des autres fichiers ; la manière dont il a été écrit n'est pas établie) | conforme |

## 11. Conditions qui restent avant la création

Selon le plan, § 4, et R-2975, mises à jour par R-2981 et GO-2026-11-16-06 :

1. **Crédit du loueur d'au moins 20 USD** (R-2975, point 7 ; GO-2026-11-16-06) : aucune ligne de `main` ne le consigne comme
   atteint (relu jusqu'à R-2984, 13:20Z ; R-2983 parle des crédits d'un autre fournisseur) ; le vérificateur ne peut pas le
   relever (aucun appel au loueur).
2. **Feu écrit de la mère** (ligne R- sur `main`) portant `GO-2026-11-14-09`, qui écrit le seul écart de forme permis (`vastai`
   par son chemin complet) ; **préavis d'une ligne à Lazar** au moment du geste (R-2883, point 2), qui dit que l'amorce garde
   `HF_TOKEN` dans la configuration de la machine jusqu'à sa destruction (R-2975, point 5).
3. **Contre-lecture par un lecteur neuf** du plan, § 4, et de la commande exacte imprimée par `lancer_bbis_v3.sh commande`
   (plan, § 7, ligne 5 ; condition de l'autonomie) : cette vérification ne la remplace pas.
4. **Gestes de session du plan, § 4.1** : inventaire d'avant (identifiants et étiquettes seulement) ; recherche d'offres (A100
   SXM4, `cuda_max_good` ≥ 13.0) et `offre-depuis-recherche` ; `creation` ; `commande` à treize arguments (COMMIT
   `31fa8ac6041faf76b66282e0346750b9aefd4790`, `prep/t07bbis-code-v1`, `20261111-151701-t06-reel`,
   `calcul/t06-confirmation-7b-v1`, `AAAAMMJJ-HHMMSS-bbis-t07-v1`, échéance à treize heures, feu, 0, `python:3.11-bookworm`),
   qui rejoue l'offre, l'amorce en essai local, la garde de création, l'ancêtre et l'absence de la branche de sortie ;
   `GH_TOKEN` pris de `CONTROLE_IA_GITHUB_TOKEN_2` par son nom ; présence de `HF_TOKEN` par `test -n`, jamais affichée.
5. **Création par un opérateur sous-agent du modèle A** (GO-2026-11-16-06, au lieu du modèle B de R-2883), arrêt au premier
   refus d'une permission, du crochet de garde ou du classifieur, sans rejeu, reformulation, découpage ni contournement ;
   identifiant relu dans `new_contract`, jamais retapé ; inventaire d'après (une instance ajoutée, étiquette `bbis-t07-v1`).
6. **K4 tient sans exception** : pilote 60918148 détruit à 13:01:11Z, absence prouvée à 13:01:46Z, inventaire relu à 13:01:58Z
   (R-2981) ; l'exception à trois conditions de R-2975, point 4, n'a plus d'objet.
7. **Dépense** sous GO-2026-11-14-09 (40 USD, coupure 39,5 USD ; répétitions ≈ 0,749 USD) ; garde de dépense au moins chaque
   heure ; preuve de destruction selon R-2975, point 6 (témoin pris dans l'inventaire du moment, jamais 60480302, 60599797 ni
   60670453).
8. **Ligne R- de consignation** des gestes (plan, § 3, fin : relevé (a), M_b, entropie par son fichier, issue de l'épreuve,
   fiche, `CODE-BBIS`, `GO-BBIS`, COMMIT) et **`registres/etat.md` avec la mention de l'addendum** (addendum, § 6) : non faites à
   `e3dc0871` (l'état ne nomme ni `f00eda8a…` ni `CODE-BBIS`) ; R-2982 en dit une partie.
9. **Échéances** : autonomie jusqu'au 2026-11-17T11:47:55Z (GO-2026-11-16-04) ; GO-2026-11-16-06 jusqu'au 2026-11-18 ; ligne
   de GO jusqu'au 2026-11-22 ; une relance au plus, avant le samedi 21 à 12:00Z ; la branche ne reçoit plus `main` avant
   `VERDICT-BBIS`.

## Méthode et limites

- Lecture seule : commandes git de lecture (avec `--no-optional-locks` après la première) ; instantanés écrits dans le bloc-notes
  depuis les objets git ; fonctions du code importées depuis l'instantané avec `PYTHONDONTWRITEBYTECODE=1` ; aucun fichier de
  l'arbre de travail modifié (seuls fichiers non suivis : le rapport de l'exécutant, son compagnon, puis ce rapport et le sien).
- Non fait : essais du paquet ; rejeu complet de l'épreuve ; relevé de `verdict/t07-etape-b*` ; crédit du loueur.

## Déclaration

- **Rôle** : vérificateur neuf (R2) des gestes d'avant course de l'étape B bis ; **lettre de modèle : A** ; n'a écrit aucun
  fichier de B bis ; n'est lecteur d'aucun verdict.
- **Heures** (`date -u`) : début 13:09:38Z ; rejeu de l'épreuve 13:25:52Z → 13:34:07Z ; contrôle du cas sain 13:34:19Z →
  13:34:29Z ; rédaction à partir de 13:37:34Z ; fin juste avant le scellement : voir la ligne finale.
- **Pièces lues** (chemin, empreinte ; « parties » quand la lecture n'est pas entière) :
  - plan `brouillons/T0.7-etape-B-bis-v1/plan-course-bbis-v1.md`, `e2505df9fbb28c9b84ab24f552a130078b8a0281b94f0c6d1ea961f08a289239`, entier ;
  - rapport de l'exécutant, `6e76287fecbfcf6d40972e46d087c1982774e6e2cc4a89b3524193bedbbdd974`, entier ;
  - texte scellé `prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb`, parties (l. 1 à 60, 84 à 93, 99, 116, 176 à 232) ;
  - addendum `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`, `f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7`, parties (l. 14 à 20, 244 à 252, 330 à 348, et les lignes qui nomment `CODE-BBIS`, `GO-BBIS`, l'entropie, l'épreuve, la fiche) ;
  - registre propre `registres/t07-etape-b-bis-v1.md`, `c7bcc49f…`, entier ; registre voisin `registres/t07-etape-b-bis-v1-addenda-v1.md`, `93f0d3dd…`, entier ;
  - `registres/t07-etape-b-bis/entropie-bbis-v1.json` `f648989b…`, `epreuve-niveau-deux-plis-bbis-v1.json` `641adeb5…`, `code-bbis-v1.json` `ee362bb7…` (par programme), `registres/go-extraits/GO-BBIS-v1.md` `33f38e67…` ; `ABSENCE-B-BBIS-v1.json` `134ac847…` (sceau seulement, par le code) ;
  - listes `fichiers-fiche-code-bbis-v3.txt` `b8fb095b…` et `empreintes-fiche-code-bbis-v3-ce470564-v1.txt` `291f1d5c…` ;
  - code : `src/controle_ia/t07bbis/registre_bbis_v1.py` `c3b1848b3466a88a250aee2b58477c91ff5d660592c1a6cc695f8910005dcf1b` (entier) ; `lecture_v2.py` `154795f4ecfa3273a7a5cec91c6975cd34e558d14647bb8a1cb1ef4968972aca` (l. 500 à 610) ; `marche_v3.py` `7009b34d46c33ed8fa4a5045d4ad93816c0948fd6dc165cb8f74e493b98f03f5` (l. 1 à 60, 180 à 250, 270 à 300, 397 à 427) ; `scripts/amorce_bbis_v3.sh` `18e2f2052efdca0d9d447738c3c4f1099302f7134b9518b59eea78ba563695dd` (entier) ; `scripts/lancer_bbis_v3.sh` `dc26ea01a06bfb9eac3fc4f9f1b9b3bb86490d61d9e8f5deb54bcb180b17ee68` (entier) ; `scripts/epreuve_niveau_deux_plis_bbis_v1.py` `3315edea63ffa064e299c3d97037d5bb4449a951162b45b3e64cf348d2bc1ba7` (entier) ; `src/controle_ia/scellement.py` `93beeb1c…` (l. 20 à 100) ; `src/controle_ia/t07/registre_v1.py` `e5023657…` (l. 39 à 41, 91 à 125, 229 à 241, 318 à 324) ; `t07bbis/commun_v1.py` `9db2b40b…` (l. 48 à 55, 83 à 89) ; `manifeste.py` `1a5c7464…` (l. 33 à 41) ; `t07bbis/lecture_v1.py` `9d11ba2b…` (emplacements de `CLES_PROPRES` et `lire_lignes`) ; `t07bbis/plis_v1.py` `7ba39db5…` (appelé, non lu) ; essais de l'instantané (lignes trouvées par recherche, et `test_t07bbis_chaine_instance_v1.py`, l. 55 à 80) ;
  - `brouillons/T0.7-etape-B-bis-v1/code/rapport-developpeur-corrections-v2.md` `d8a2e40b…` (l. 70 à 82) ; `registres/passations/2026-11-10-2206.md` `8f625791…` (l. 7) ; `.claude/hooks/garde_calcul.py` du dépôt principal `73be0638…` (lignes de motifs) ;
  - sur `main` (lignes ajoutées, jamais réécrites ; `main` relu de `64df08bd` à `e3dc0871`) : `registres/decisions.md` lignes R-2975, R-2981, R-2982 entières, R-2976 (fragment autour de 12:23:08Z), R-2959 (date), R-2983 et R-2984 (débuts, et le passage sur les crédits) ; `registres/go.md` (`b5468a46…` à `e3dc0871`) lignes GO-2026-11-14-09 et GO-2026-11-16-06 entières, colonnes de type des lignes 320 à 347, passages qui citent GO-2026-11-14-09 ; `registres/etat.md` (`981ca5b0…`) par comptes et une ligne coupée à 200 caractères ;
  - journal de l'épreuve de l'exécutant, `…/scratchpad/epreuve-bbis-v1.log` (402 octets), entier.
- **Jamais ouvert** : aucun fichier sous `diag/`, `donnees/`, `docs/verdicts/` (noms par git seulement ; voir l'incident 1) ;
  aucune entrée de 7a ou de 7b ; aucune sortie de l'étape B ; `docs/procedures/lecture-7b-etape-b-compte-3-v1/` au-delà des
  noms (voir l'incident 1) ; la branche `verdict/t07-etape-b-compte-3-v1` (ni lue ni interrogée) ; `registres/decisions.md`
  entier ; aucune valeur de clé ; aucun dossier d'un autre agent du bloc-notes (`plan-bbis.md` à sa racine : non ouvert).
- **Incidents de ma main** :
  1. Le compte des motifs de clés sur le différentiel de la fusion M_b (`verif_git_v1.py`, `git diff 77f8a2c2 f9bd9ba6`) a fait
     passer en mémoire, sans affichage ni écriture, le contenu des fichiers apportés par `main`, dont les 2 chemins sous `diag/`,
     les 24 sous `docs/verdicts/` et les 92 sous `docs/procedures/lecture-7b-etape-b-compte-3-v1/` ; seul le compte (0) est
     sorti. C'est plus que « par les noms » pour ces dossiers : déclaré.
  2. Une recherche des mots de révocation dans `registres/go.md` a affiché au terminal les 160 premiers caractères de douze
     lignes sans rapport (dont des noms de modèles d'autres expériences) ; rien dans un fichier.
  3. Un affichage au terminal du message de la fusion a montré sa ligne d'attribution (un nom de modèle) ; la sortie du bloc-notes
     `resultats-git-v1.json` portait ce message et l'identité d'auteur des commits : les deux champs en ont été retirés aussitôt,
     et le programme corrigé pour ne plus les copier (aucun nom de modèle dans les fichiers du vérificateur).
  4. Un `git status` sans `--no-optional-locks`, à 13:09Z, a pu rafraîchir les dates de l'index de l'arbre de travail ; aucun
     contenu suivi n'a changé.
  5. Aucune commande refusée par une permission, par le crochet de garde ou par le classifieur ; aucun processus arrêté ; un seul
     processus lourd à la fois (le rejeu, priorité 19, un fil).

Fin de la rédaction : 2026-11-16T13:40:11Z (`date -u`), juste avant le scellement de ce fichier ; non committé.
