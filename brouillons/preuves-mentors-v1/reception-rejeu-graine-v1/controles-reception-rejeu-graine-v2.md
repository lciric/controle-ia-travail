# Contrôles de réception du rejeu à graine (fiche `1193a54a…`, section 4) — v2

Faits par conv-audit le 2 novembre 2026, de 18:17 à 18:21 UTC (heures relevées par `date -u`), **avant la lecture** (section 5 de la fiche), qui revient à un lecteur neuf. La v1 (`c245effe…`, scellée à 18:21:25 UTC) portait par erreur « 18:24 » comme heure de fin ; c'est la seule différence.

## 0. Ce que je savais déjà avant ces contrôles (transparence)
Le message n° 286 de session-depot (`622c7cbd…`, 18:14 UTC, empreinte vérifiée contre son compagnon) cite les lignes de progression du journal de l'instance : « validation : lecture « sous le seuil », empreintes retrouvées 54 sur 147 » ; « résolution : lecture « complète », 7 sur 7 » ; « cibles du lot : 0 ; lot sans objet ; table du cœur seul ». Je les ai donc lues avant la lecture. Elles ne décident rien : la lecture applique les critères gelés du texte scellé, par un lecteur neuf.

## 1. Voie de réception : (b)
- Copie à l'octet par session-depot sur `canal/session-depot-reprise-n113`, commit `a5971dd1`, dossier `brouillons/canal-reprise-releve-v1/envois/session-depot/rejeu-graine-sortie-v1/` (349 fichiers) et liste `rejeu-graine-sortie-v1-liste-empreintes.txt` (`483b5f4665d60a2691b030b67f684eda6845f527c6e125f6f19d9930226aa578`, recalculée : égale).
- Récupération par refspec explicite ; `calcul/r1-resolution-graine-v1` **non récupérée** ; `git for-each-ref refs/remotes | grep -c donnees` = 0.
- Copie de travail (lecture seule) : `/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/reception-rejeu-graine-v1/copie/` (extraite par `git archive`).

## 2. Contrôle 1 — fichiers, sceaux, clés : conforme
- 349 fichiers ; 349 empreintes égales à la liste de session-depot, 0 écart.
- 162 fichiers de sceaux : 161 compagnons `.sha256` (une ligne chacun) et `traces/r1-graine-20261102-181212-iXsM/empreintes.sha256` (26 lignes) ; **187 lignes vérifiées, 0 écart, 0 fichier absent** ; les 187 fichiers non sceaux sont tous couverts.
- Aucune forme de clé (motif de la règle de poussée, sur les 349 fichiers).

## 3. Contrôle 2 — manifestes : conforme, deux réserves
- Deux manifestes : `runs/20261102-171752-r1-graine-validation/manifeste.json` (`86e90b36…`) et `runs/20261102-175806-r1-graine-resolution/manifeste.json` (`0aeb5b58…`).
- Préenregistrement : `prereg/R1-addendum-relance-v2.md`, `9d17d640509c9b5dd0285e90f3096145b82f2e0ea2e73e62725c0e0c8cb71059` (égal à la fiche ; texte relu au commit `c2a8b6e1`, sceau vérifié).
- Configuration : `config_sha256` = `f91716bf95c4c4ab07e4155c667539cee9baff38b7ca2639dff0dea167d44db2` dans les deux manifestes ; le journal écrit « canonique f91716bf95c4, citée sous ses deux libellés » (16:46:46 UTC).
- Table v2 : `table_tokenisation_sha256` = `5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2`.
- Graines (R9) : bloc `graines` avec `entropie`, `spawn_key` et `etat_controle` (dérivation `SeedSequence`) ; libellé « aucun-tirage-propre » (le rejeu rejoue les graines de P3, il ne tire rien en propre).
- Versions : torch 2.14.1 (journal : « torch 2.14.1+cu130 cuda 13.0 disponible True ») ; révision du modèle et du tokeniseur `0e9e39f249a16976918f6564b8830bc894c89659` (manifeste et journal, « tokeniseur en cache ») ; carte A100-SXM4-80GB (`nvidia-smi.txt`).
- Essais : `traces/…/tests.txt`, dernière ligne « 71 passed in 1547.36s (0:25:47) ».
- Commit : validation au commit **`c2a8b6e1`** ; résolution au commit **`3482d8f1`** (descendant, selon n° 286 : commit de la validation entre les deux). L'arbre du code est identique entre `0e2a8871` et `c2a8b6e1` (`git diff --stat` vide sur `src`, `scripts`, `tests`, vérifié ici) ; entre `c2a8b6e1` et `3482d8f1`, **non vérifiable par la voie (b)** ; le module refuse de lancer si l'arbre gelé diffère du commit cité (liste d'arrêt, « module, avant le manifeste »), et les deux manifestes portent `depot_propre: true`. Demande à session-depot : `git diff --stat c2a8b6e1 3482d8f1 -- src scripts tests` (attendu vide).
- **Réserve R-a** : ni `GO_ID` ni l'identifiant d'instance ne sont écrits dans la sortie scellée (manifestes, journal, traces) ; ils ne sont portés que par les messages n° 281 et n° 286 (`GO-2026-11-02-02`, instance 58851293).

## 4. Contrôle 3 — code de sortie, étapes, durées, dépense : conforme, une observation
- Code de sortie 0 (n° 286 ; journal, 18:12:12 UTC : « fin : validation …, résolution …, lot sans objet, table … passés ») ; **aucun `arret.json`** dans la copie.
- Étapes atteintes : 0 validation, 1 résolution, cibles du lot (0 cible : « lot sans objet »), table v3. Étape 1 bis non lancée (sans objet).
- Durées (journal) : mise en place 16:44:49 → essais finis 17:15:51 ; validation 17:17:52 → 17:58:03 (**40 min 11 s**) ; résolution 17:58:06 → 18:11:30 (13 min 24 s) ; cibles 18:11:35 ; table 18:11:35 → 18:12:10 ; fin 18:12:12.
- **Observation (durée, non une lecture)** : la configuration fixe `duree_max_s` = 2 400 s par étape ; la validation a duré 40 min 11 s depuis son lancement, et les lignes de progression passent de 60 à 147 épisodes au même instant (17:57:54 UTC) sans passe nouvelle (`passes=10627` inchangé). Le code consigne « non tenté : durée » les épisodes que le budget de l'étape n'a pas atteints (`resolution_graine_v1.py`, `non_tente`, l. 1502-1506 et 1560, au commit `c2a8b6e1`). Le lecteur neuf vérifie, épisode par épisode, la cause de chaque épisode non retrouvé.
- Dépense : instance 58851293, 16:42:40 → 18:13:07 UTC (≈ 90,5 min) à 1,187 USD/h, **≈ 1,79 USD** plus le disque ; sous GO-2026-11-02-02, enveloppe GO-2026-11-02-14. Instance détruite par son identifiant à 18:13:07 UTC (R10), selon n° 286 ; l'inscription au registre des arrêts est chez session-depot.
- Après la fin, l'amorce s'est relancée deux fois (redémarrage du conteneur) et sa garde R12 l'a refusée (n° 286 : « rien n'a été réécrit ») ; je ne peux pas le vérifier par la voie (b), mais la liste de session-depot et les 187 sceaux concordent.

## 5. Contrôle 4 — table v3 : présente et scellée
- `prereg/R1-table-tokenisation-v3.json`, sha256 **`ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423`**, égale à son compagnon, au journal (« table v3 committée … (ead8a66851b2) ») et à `traces/…/sceau-table.txt` (« OK ead8a66851b2… »).

## 6. Suite
Lecture par un lecteur neuf (section 5 de la fiche), sur les fichiers de la copie, le texte scellé (`R1-addendum-relance-v2.md`, section « Critères de lecture gelés »), la configuration, le code au commit `c2a8b6e1` et ces contrôles ; puis verdict scellé, soumis à Lazar.
