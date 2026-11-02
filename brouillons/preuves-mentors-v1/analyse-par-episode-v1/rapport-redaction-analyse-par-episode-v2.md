# Rapport de rédaction — lecture complémentaire « par épisode » de R1-R2, brouillon 2 (voie B)

Rédacteur : sous-agent neuf (Claude, Opus 5.5), 2 novembre 2026, ≈ 07:14 à ≈ 07:37 UTC ; il n'a écrit ni le brouillon 1 ni la contre-lecture et applique celle-ci sans la refaire. Rien de commis, rien de scellé, aucun `.sha256`, aucun `git fetch`, aucune branche `calcul/…`, aucune donnée de R1, R2, R4 ni de P3, aucun pli ni statistique de P3 par pli calculé, aucun fichier existant modifié (fichiers neufs seulement), arbre de travail non changé (ni `checkout`, ni `switch`, ni `worktree`, ni `stash`, ni `reset`), aucun appel de réseau ni de modèle ; calculs et essais dans `.venv` (Python 3.13.18, numpy 2.4.6, scipy 1.17.1) sous `nice -n 10`.

Note : pendant la rédaction, la session a commis trois points de sauvegarde de ce travail en cours (`5403bc26`, `39e9d769`, `616d685d`). Le fichier d'essais v2 y figure dans une version antérieure (deux essais complétés depuis : résultat absent ou non scellé, sortie déjà présente, mode non décisif sans entropies) ; les empreintes ci-dessous sont celles des fichiers finaux de l'arbre.

Entrées : brouillon 1 (`20b3392a…`, vérifiée), contre-lecture `contre-lecture-preenregistrement-analyse-par-episode-v1.md` (`412fb4e6855452b3e112e526d320e55dddc64ebabd4c83276d285a6556a93504`, vérifiée), décision R-1122 (`registres/decisions.md`) et ligne `GO-2026-11-02-05` (`registres/go.md`), lues.

## Couples appliqués

Appliqués par un script du dossier temporaire (chaque ancien texte exigé une seule fois dans le brouillon 1), puis vérifiés en relisant les couples dans la contre-lecture : le texte « par » de chaque couple appliqué tel quel se trouve entier dans le brouillon 2.

- R1 — adapté : le premier couple (ligne du commit cité) est appliqué tel quel ; la ligne « Décision qui ouvre cette lecture » écrit en clair, à la place du marqueur `<<GO_LAZAR>>` proposé, le mot de Lazar (2 novembre 2026 vers 07:10 UTC, session conv-audit, question citée, réponse « Oui, sceller », R-1122, ligne `GO-2026-11-02-05`) ; la clause « le validateur refuse le scellement tant que ce marqueur reste » est retirée, puisqu'il n'y a plus de marqueur.
- R2 — appliqué tel quel.
- R3 — appliqué tel quel.
- R4 (deux couples) — appliqué tel quel ; à la suite du second, ajout du renvoi au chemin et à l'empreinte du script de l'annexe A enregistré et de sa sortie (R6 ; prévu par la contre-lecture, « Annexe A dans le dépôt »).
- R5 — appliqué tel quel.
- R6 — appliqué tel quel.
- R7 — appliqué tel quel. Les nombres de P-E7 sont ceux que propose le contre-lecteur (« à confirmer par la session ») ; la session ne les a ni confirmés ni changés dans le mandat : à confirmer avant scellement.
- R8 — appliqué tel quel.
- R9 — appliqué tel quel.
- R10 — adapté : « porte le code v4, les essais » devient « porte le code v4 et v5, les essais » (le code cité contient les modules v5) ; le reste mot pour mot.
- R11 (premier couple) — adapté : « rappel relu altéré de 1e-12 ; seuil d'un pli altéré et aire par action altérée : essais du code v5, ci-dessous) », car ces deux essais sont dans le fichier neuf `tests/test_analyse_par_episode_v2.py`, non parmi les 12 essais v1 que décrit la phrase.
- R11 (second couple) — adapté : description des 18 essais v2 ajoutée (gardes héritées dites éprouvées par les essais de la principale, « p hors de ]0, 1] » déclarée inatteignable par construction), commande élargie au fichier v2, nombre récrit (« 54 réussis sur 54 au brouillon 2 (12 + 18 + 24 ; 36 sur 36 au brouillon 1) ») ; la phrase sur le `python3` du système est gardée telle quelle (non revérifiée ici).
- R12 — appliqué tel quel (le code v5 le fait : réserves recopiées).
- R13 — appliqué tel quel.
- R14 (deux couples) — appliqué tel quel (le code v5 le rend vrai : C1, C2).
- R15 — appliqué tel quel.
- R16 — adapté : C4 étant fait avant scellement, la fin du couple (« la fréquence des classes sous le nul global et la puissance ne sont pas mesurées par épisode ») devient la mesure (nombres, script, sortie, empreintes) ; la puissance reste non mesurée et la phrase « « non concluant » ne se lit qu'avec l'intervalle écrit » est gardée.

Changements hors couples : titre (« brouillon 2 ») ; ligne « Date » (créneau du brouillon 2) ; commande décisive (`lecture_v5`) ; en-tête de la table des critères (`lecture_v5.issue`) ; liste fermée (en-tête du paquet, trois modules v5, essais v2) ; empreinte des constantes (code v5) ; section « Contre-lecture » remplie (contre-lecture 1 avec ses deux empreintes, rédacteur du brouillon 2 et ce qu'il savait, ce qui a été appliqué, traitement de chaque remarque, constat de C4 laissé à la session). La ligne « Auteur » décrit toujours le rédacteur du brouillon 1 ; celui du brouillon 2 est décrit dans la section « Contre-lecture ».

## Changements de code (modules neufs, code v4 inchangé et gardé dans la liste fermée)

- `constantes_v5.py` : `VERSION`, `COMMANDE` (`lecture_v5`), `NOM_SORTIE` (inchangé : `analyse-par-episode-v1`), `ALPHAS_CONCORDANCE` (trois taux de la principale), `CONCORDANCE`, `PREFIXE_RESERVE_PRINCIPALE`, `ETIQUETTES_RANGS` ; empreinte couvrant v1, v2, v4 et v5 : `c391d1d58a52207a1708a683570da92b75a4e18e7807e288850a696b0bb11884` (celle du code v4, `4a21b3a6…`, est inchangée).
- `calcul_v5.py` : réexporte le calcul par épisode de `calcul_v4` sans modification ; ajoute `mesures_par_action` (C1 : `calcul_v1.evaluer` aux taux 1/100, 2/100, 5/100 et `calcul_v1.auc`, mêmes arguments que la principale).
- `lecture_v5.py` :
  - C1 : `exiger_concordance_principale` exige, pour chaque bras lu, l'égalité exacte (nombres relus, non finis rendus par `lecture_v1._json`) du rappel par action aux trois taux, du seuil de chaque pli aux trois taux et de l'aire par action ; `calculer` = `calculer` du code v4, plus la mesure par action (rendue aussi dans le résultat, clé `action` de chaque bras) ;
  - C2 : `issue` reprend `lecture_v4.issue` (critères gelés inchangés) et ajoute à chaque ligne de Δ (P-E1, P-E2, P-E4, W − J8s) le compte de fausses alarmes par épisode des deux bras, recopie les réserves de la principale (préfixe « réserve de la principale (par action, mêmes scores) : »), corrige l'étiquette du seuil fragile (rang 1 (1/49), rang 2 (2/49)), récrit les libellés prédits de P-E2 et P-E3 (R6, R2) et ajoute P-E7 ; `rendre` corrige les étiquettes de taux (« rappel rang 3 (3/49) » au lieu de « rappel 5 % », « au plus ≈ 1/49 ») ; `analyser` écrit `reserves_principale` hors « rejeu non validé » ;
  - gardes du mode décisif sur la liste fermée v5 (26 fichiers) et l'empreinte des constantes v5 ; `lire_principale` reprise du code v4.
- Non traité : M8 (`constantes_v4.NIVEAU` et `MAX_DEGENERES` déclarées et non lues ; `calcul_v1.difference` lit celles de `constantes_v1`, de mêmes valeurs : sans effet) ; ni couple ni changement de code ne le demandait.

## Essais

- `tests/test_analyse_par_episode_v2.py` : 18 essais neufs (chaque garde neuve ou jusqu'ici sans artefact éprouvée sur un cas sain et sur un artefact ; liste dans le Plan d'analyse, point 9).
- Commande : `. .venv/bin/activate` puis `PYTHONPATH=src nice -n 10 python -m pytest -q -p no:cacheprovider tests/test_analyse_par_episode_v1.py tests/test_analyse_par_episode_v2.py tests/test_analyse_principale_r1_r2_v1.py tests/test_analyse_principale_r1_r2_v2.py` : **54 réussis sur 54** (12 + 18 + 24), 27,4 s, 2 novembre 2026 07:28 UTC.
- Non fait : essais de mutation des gardes neuves (chaque artefact est éprouvé par construction, sans retirer la garde pour vérifier que l'essai échoue).

## Vérifications du texte

- `PYTHONPATH=src python -c "from controle_ia.prereg import problemes as p; print(p('<brouillon 2>'))"` : `['marqueurs de gabarit restants : <<COMMIT_CITE>>']` (seul marqueur restant ; aucun `<<GO_LAZAR>>`).
- `lecture_v5.exiger_code_cite(<texte du brouillon 2>)` : conforme (26 fichiers, empreintes de l'arbre, constantes `c391d1d5…`) ; la garde du code v4 refuse ce texte (liste fermée), comme attendu.

## Sortie de C4 (`frequence-nul-analyse-par-episode-v1-sortie.txt`)

200 répliques nulles synthétiques, entropie 202611020725, 07:21:12 à 07:22:22 UTC :

```
W-G : {'supérieure': 1, 'inférieure': 1, 'non concluant': 198, 'non lue': 0} ; part non nulle 0.010
W-J3s : {'supérieure': 0, 'inférieure': 1, 'non concluant': 199, 'non lue': 0} ; part non nulle 0.005
W-T : {'supérieure': 1, 'inférieure': 0, 'non concluant': 199, 'non lue': 0} ; part non nulle 0.005
W-J8s : {'supérieure': 0, 'inférieure': 1, 'non concluant': 199, 'non lue': 0} ; part non nulle 0.005
au moins une classe non nulle parmi W-G et W-J3s : 3/200 = 0.015
fausses alarmes par épisode (sur 60), W : moyenne 1.255 (60/49 = 1.224) ; P(>4) 0.005 ; P(=0) 0.140 ; max 5
fausses alarmes par épisode (sur 60), G : moyenne 1.120 (60/49 = 1.224) ; P(>4) 0.000 ; P(=0) 0.075 ; max 4
fausses alarmes par épisode (sur 60), J3s : moyenne 1.135 (60/49 = 1.224) ; P(>4) 0.000 ; P(=0) 0.080 ; max 3
fausses alarmes par épisode (sur 60), J3g : moyenne 1.025 (60/49 = 1.224) ; P(>4) 0.000 ; P(=0) 0.145 ; max 4
fausses alarmes par épisode (sur 60), J8s : moyenne 1.115 (60/49 = 1.224) ; P(>4) 0.000 ; P(=0) 0.060 ; max 3
fausses alarmes par épisode (sur 60), C : moyenne 0.995 (60/49 = 1.224) ; P(>4) 0.000 ; P(=0) 0.200 ; max 3
fausses alarmes par épisode (sur 60), T : moyenne 1.410 (60/49 = 1.224) ; P(>4) 0.020 ; P(=0) 0.075 ; max 7
```

Lecture : sous ce nul, la famille des deux comparaisons principales sort de « non concluant » dans 1,5 % des répliques (principale par action : 0/200) ; le biais du rééchantillonnage du maximum (I6) se compense dans Δ à ce niveau. Les bras entraînés sont un peu plus lâches (W 1,26 ; T 1,41) que les bras fixes (1,00 à 1,14), dans le sens de I2.

## Annexe A

Script enregistré tel quel (`sim-calibrage-episode-contre-lecture-v1.py`, sha256 `34d71d83…` vérifié, identique au bloc de l'annexe A) ; relancé une fois pour les trois configurations de la contre-lecture (07:18:55 à 07:19:06 UTC) : les six lignes de sortie sont identiques, caractère pour caractère, à celles de l'annexe A.

## Empreintes des fichiers neufs (sha256)

- `brouillons/preuves-mentors-v1/analyse-par-episode-v1/preenregistrement-analyse-par-episode-v1-brouillon2.md` : `b17412c4cfd8e2700e4d1b003dec1774261a1eae5345aae3b49b213b923be223`
- `brouillons/preuves-mentors-v1/analyse-par-episode-v1/differences-brouillon1-brouillon2-v1.diff` : `117eb184432c8c8d612601c963ee7673ea13319e3fcb4a53be65242718710ae6`
- `brouillons/preuves-mentors-v1/analyse-par-episode-v1/sim-calibrage-episode-contre-lecture-v1.py` : `34d71d83a38774aa128ad39fcc325a9ad67d8bf9f891f25f81ec27e76ddcc46b`
- `brouillons/preuves-mentors-v1/analyse-par-episode-v1/sim-calibrage-episode-contre-lecture-v1-sortie.txt` : `dd438883603828e71ff15b2b6056ae0cfed789767c2db225eecf687c815226fe`
- `brouillons/preuves-mentors-v1/analyse-par-episode-v1/frequence-nul-analyse-par-episode-v1.py` : `c63d5a34cbee482a079fc7704359fa7d6cd7f52d9d14fddff09b4ab00f76a203`
- `brouillons/preuves-mentors-v1/analyse-par-episode-v1/frequence-nul-analyse-par-episode-v1-sortie.txt` : `19b8ac0e679f3123ce03676fb51addc417590570fa9f03136bbe44b01dd0517a`
- `src/controle_ia/analyse_principale_r1_r2/constantes_v5.py` : `e8f783d2a0a3ea024ba4a13635d37572a5e2cec37f96b32f03bdcd20e0e7f64b`
- `src/controle_ia/analyse_principale_r1_r2/calcul_v5.py` : `f11b32fd7c2e73acf47d25b417154e211e39b7d4086c76560a99507e44e73f4f`
- `src/controle_ia/analyse_principale_r1_r2/lecture_v5.py` : `cd94a607f3c5b9a7ca2f379895fbd0084b51283799456e735267aa8a3ffb261a`
- `tests/test_analyse_par_episode_v2.py` : `7aaf866fe7cf6f011327a8645dd24e065e411422033df6b587f1318330674e15`
- ce rapport : empreinte dans le message de retour.

## Différences brouillon 1 → brouillon 2

`differences-brouillon1-brouillon2-v1.diff` (`diff -u`, 22 lignes retirées, 33 ajoutées, en-têtes non comptés) : titre ; R1 (commit cité et décision de Lazar) ; date ; R5 ; R2, R6, R7 (table des prédictions) ; R3, R4, R9 (Seuil) ; R14 (Métrique, point 2 ; Liste d'arrêt) ; R10, commande `lecture_v5`, R8, R11 (Plan d'analyse) ; empreinte des constantes et liste fermée ; en-tête de la table des critères, R12 ; R13 ; R16, R15 (Limites) ; section Contre-lecture.

## Constats pour la session

1. P-E7 (R7) porte les nombres du contre-lecteur, appliqués tels quels : à confirmer ou changer avant scellement.
2. P-E3 (R2, appliqué tel quel) écrit « en moyenne au plus ≈ 1,2 » ; or un bras entraîné fait 1,39 dans l'annexe A (sans effet de tâche ni d'épisode) et T 1,41 sous le nul de C4 (plus de 4 dans 2 % des répliques). Écrit dans la section « Contre-lecture » et dans les Limites (R16) ; non tranché ici.
3. `registres/go.md` consigne la réponse comme « Oui, sceller (Recommandé) » (étiquette de l'option) ; le texte cite « Oui, sceller », comme le registre des décisions et le mandat.
4. Points de sauvegarde de la session : la version commise du fichier d'essais v2 (`616d685d`) n'est pas la version finale ; le commit cité devra porter les fichiers finaux (empreintes ci-dessus, vérifiées par la garde « code cité » du code v5 contre le brouillon 2).

## Ce qui manque

Rien de ce qui était obligatoire. Non faits : M8 (sans effet) ; puissance par épisode (limite écrite) ; essais de mutation des gardes neuves. Restent à la session : décision sur P-E7 et sur la phrase de P-E3, inscription de l'empreinte du brouillon final au registre, commit cité et scellement (R10).
