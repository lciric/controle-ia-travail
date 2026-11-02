# Contre-lecture (R2) de l'addendum v3 de relance de R1 sur la table de tokenisation v3 — brouillon 1 — rapport v1

- Contre-lecteur : sous-agent neuf (Fable 5.1), auteur d'aucune pièce lue ; aucun fichier de l'arbre modifié, aucun commit, aucun `.sha256` créé, aucun appel réseau ni de modèle, aucune instance.
- Heures (UTC, relevées par `date -u`) : début de lecture 2026-11-02 23:00:50 ; essais lancés 23:07:00, finis 23:08:28 ; rédaction commencée 23:12:00.
- Arbre lu : `/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/wt-relance-v3`, branche `prep/r1-relance-v3`, tête `145da951`, arbre propre.
- Texte contre-lu : `prereg/R1-addendum-relance-v3.md`, sha256 `382ba6272ea0856dd9ba699f1d16eabef66fc12be288c214af71c5de28a5a05d` (égale à l'objet du commit `145da951` et à l'empreinte que cite `controles-avant-installation-v3.txt`, ligne 2).
- Empreintes de ce rapport : rendues par l'appelant (aucun `.sha256` écrit par moi).

## 1. Verdict

**Scellable après corrections** : aucun bloquant ; deux points importants (I1, I2) à corriger dans le texte avant le scellement, quatre points mineurs (M1 à M4) au choix de l'auteur. Tout chiffre du texte renvoie à une pièce et lui est égal ; toutes les empreintes citées sont exactes ; les écarts E1 à E21 sont cohérents avec le code et les scripts, et je n'ai trouvé aucun écart non déclaré entre `c2a8b6e1` et `145da951` sous `scripts/`, `src/` et `tests/` ; le devis tient sous 60 USD ; `prereg.problemes` ne signale que « Contre-lecture ».

## 2. Bloquants

Aucun.

## 3. Importants

**I1 — « avant tout clonage » est inexact pour `DELAI_REJEU_MIN`** (`prereg/R1-addendum-relance-v3.md`, ligne 127 [E8, (c) : « `DELAI_REJEU_MIN` hors des entiers de 1 à 9999 (avant tout clonage) »], ligne 430 [Liste d'arrêt : « **script, avant tout clonage** (code 2) : `DELAI_REJEU_MIN` … »], lignes 386 et 397 [Essais : « **délai « abc »** : refus du script avant tout clonage, code 2 »]).
- Fait : la garde du script (`scripts/r1_relance_instance_v3.sh`, lignes 52 à 58) refuse bien la valeur avant le clonage **du script** (ligne 82), mais l'amorce (`scripts/amorce_instance_r1_relance_v3.sh`, lignes 39 à 47) a déjà cloné `amorce-depot` et extrait le commit pour trouver le script : l'amorce ne lit pas `DELAI_REJEU_MIN`. La pièce le dit elle-même (`essai-jouet-relance-v3/LISEZMOI.txt` : « l'amorce, qui a cloné son propre dépôt, rend le code du script »). Seule `PLAFOND_AMORCE_MIN` est refusée avant tout clonage (amorce, lignes 25 à 29, code 1).
- Correction proposée : aux trois endroits, écrire « avant le clonage du dépôt de travail par le script (l'amorce a déjà cloné le sien pour le lire) » ; ou, si l'auteur veut la garde avant tout clonage, ajouter à l'amorce le même motif `^[1-9][0-9]{0,3}$` sur `DELAI_REJEU_MIN` avant la ligne 39 (changement de code : commit neuf, essai à étendre, empreinte du script à refaire à l'en-tête). Aucune conséquence sur la dépense ni sur la sécurité : la valeur passée à la création est `600`, éprouvée (essai jouet sain).

**I2 — Les lignes que l'addendum v2 scellé « renvoie à l'addendum v3 » ne sont pas toutes rattachées à une ligne de ce texte** (`prereg/R1-addendum-relance-v2.md`, lignes 175 à 183 : G3, G4 et G5, G6, G7, **G9 (contre-contrôle négatif étendu), G10 (traitement de C-1)**, prédiction P-R5, « étape 3 du brouillon 1 (préalables, complément court) », « ligne « Relance » des critères de lecture », attentes de réception m-8).
- Fait : le texte couvre ces objets sur le fond (G3 → E19 ; G4, G5 et P-R5 → E4, E14, E15 et « Prédiction » ; G6 → E11, E12 ; G7 → E10 ; m-8 → étape 3 du plan ; G9 → E13 ; G10 et C-1 → « Métrique », « elles entrent dans les lectures si `fidele` (tolérance) est vrai »), mais il ne nomme jamais G9, G10, « étape 3 du brouillon 1 » ni « ligne « Relance » », alors que la concordance de conv-audit (n° 354, point 1) lit ce texte contre le brouillon 3 de la v1 et contre ces renvois.
- Correction proposée : une phrase dans « Écarts au parent » (ou dans « Statut ») qui dit où chaque renvoi de la v2 atterrit, et « sans objet » pour ceux que la table complète rend caducs (étape 3 « préalables, complément court » ; « ligne « Relance » » si elle portait sur les non résolus).

## 4. Mineurs

**M1 — « au commit cité » pour la suite ciblée et l'essai des bornes** (texte, lignes 379 à 388 : « Suite ciblée (…) au commit cité » ; « 23 passés au commit cité » ; en-tête lignes 58 à 61 : « au commit cité »). Les pièces disent le commit `d803a8d6` (`tests-cibles-relance-v3.txt`, ligne 1 ; `tests-bornes-relance-v3.txt`, ligne 1), dont `src/`, `tests/` et `scripts/` sont ceux de `f921fcec` (vérifié ici : `git diff --stat f921fcec 145da951 -- scripts/ src/ tests/` vide ; `d803a8d6` n'ajoute que `prereg/`, hors de l'arbre gelé `CHEMINS_GELES`). Proposition : « au commit `d803a8d6`, dont l'arbre gelé est celui du commit cité ».

**M2 — Section « Contre-lecture »** (texte, lignes 452 à 467). `prereg.problemes` exige, une fois « À REMPLIR » retiré, soit une entrée « Contre-lecture k » (chiffre) portant deux empreintes de 64 hexadécimaux, soit deux telles empreintes dans la section ; l'entrée actuelle s'appelle « Contre-lecture finale » (sans chiffre) et les empreintes de l'historique sont abrégées (`64fab1a5…`, `82a5ed18`). Proposition : nommer l'entrée « Contre-lecture 1 » ou y écrire en entier l'empreinte du brouillon relu (`382ba627…`, ci-dessus) et celle de ce rapport.

**M3 — « R-1116 » sans registre nommé** (texte, lignes 138 [E19] et 344 [R2]). Dans `registres/decisions.md` de `main` au commit `f1791003`, R-1116 n'est pas une entrée (la dernière est R-1060) ; c'est le numéro du registre de conv-audit, comme l'écrit l'addendum v1 (ligne 9 : « registre R-1116 ») et comme la ligne R-1033 de `main` le recopie (« N1 = (b) ; N-A = (c) puis (a) »). Proposition : « R-1116 du registre de conv-audit, recopiée R-1033 ».

**M4 — Fins du format « (128001, 128008, 128009) »** (texte, ligne 372). Les valeurs ne figurent pas dans `prevol-relance-v3-sortie.txt` ; elles sont dans la table v3 (`fins_du_format`, vérifié ici) et affirmées par l'assertion du script `prevol_relance_v3.py`, ligne 91. Proposition : citer la table (`fins_du_format`) comme pièce des valeurs.

Remarques sans correction demandée :
- Le cas « sain » de `controles-avant-installation-v3.txt` finit en code 127 ; c'est l'arrêt voulu sur `nvidia-smi` absent de la copie, documenté en tête de `controles_avant_installation_v3.sh` (lignes 5 à 7). Le texte pourrait le dire en une parenthèse.
- `tokenisation.addendum` = `prereg/R1-addendum-relance-v2.md` (constante `ADDENDUM`, `rejeu_activations_v3.py`, ligne 66) : déclaré en E16 et aux attentes de réception, vu à l'essai jouet (`inspection-sain.txt`) ; cohérent.
- Le mot « partie de `c2a8b6e1` » (ligne 27) se lit « à partir de » : `f921fcec` descend de `c2a8b6e1` (journal : `c2a8b6e1` → `f921fcec` → `d803a8d6` → `145da951`).

## 5. Ce que j'ai rejoué (commandes et comptes exacts)

Toutes les commandes depuis l'arbre `wt-relance-v3` ; Python = `/home/user/controle-ia-travail/.venv/bin/python` sous `nice -n 10`, `PYTHONPATH=src`.

1. **Empreintes citées** (`sha256sum`) : parent `prereg/R1-R2-rejeu-p3-v1.md` = `80c85a00…` (compagnon conforme) ; addendum v2 = `9d17d640…` (compagnon conforme) ; addendum v1 = `485acc3a…` ; configuration v5 fichier = `acad6253…` (sans compagnon, comme déclaré) ; table v3 = `ead8a668…` (compagnon conforme) ; table v2 = `5f6cf489…` ; module v3 = `0581cf9a…`, v2 = `6f23f802…`, v1 = `dde8aa67…` ; `resolution_graine_v1.py` = `cdc22b5a…` (compagnon conforme) ; `resolution_tokenisation_v1.py` = `e8568c3c…` ; `r1_relance_instance_v3.sh` = `24744794…` et `amorce_instance_r1_relance_v3.sh` = `82f38687…` (compagnons conformes) ; `test_rejeu_activations_v3.py` = `ef7be3f7…` (compagnon conforme) ; `test_bornes_relance_v3.py` = `1b1fce06…` (compagnon conforme) ; verdict du lecteur neuf = `64fab1a5854deba0ad669d0c4840b6736e9cb680a22928d548c63093bb273e68` ; les dix pièces de mesure et les quatorze fichiers de l'essai jouet : `sha256sum -c` de tous les compagnons sous `relance-v3/` : OK, 0 écart ; chaque empreinte citée à l'en-tête du texte égale à la mienne (16 sur 16).
2. **Empreinte canonique** : `rejeu_activations_v3.empreinte_config(config v5)` = `1cfb7fba9518ff81484153e0e9cc6dd974941b7d985775f026e61a80687627d4` ; recalcul direct (`json.dumps`, clés triées, séparateurs compacts) identique ; 29 clés = `rejeu_activations_v3.CLES`. Même fonction sur la v4 : `10707413…` (E11, exact) ; sur la v2 : `aa79ca8e…` (E11, exact). `diff` v4/v5 : seuls `chemin_table_tokenisation` et `table_tokenisation_sha256` changent (E11, exact).
3. **Table v3** (lecture JSON, comptes seulement) : version 3 ; 22 entrées ; méthodes : `une_paire` 12, `deux_paires` 2, `fins` 1 (15 « v1 »), `fenetre` 2, `trois_paires` 1 (3 « v2 »), `identifiants` 4 (`honnete/2602.00987v1/e0`, `mention/2605.17899v2/e0`, `saboteur/2510.05132v3/e0`, `temoin/2512.06870v2/e0`) ; aucune `non_resolu` ; `comptes` : épisodes 240, conformes en longueur 151, identiques de base 129, signalés 22, identiques après la table 151 ; `corrections_verifiees` 22 ; `resultat_graine_sha256` = `67482545…` ; `table_v2_sha256` = `5f6cf489…` ; `lecture_validation` : 54 retrouvées sur 147, classe « méthode non transposée » ; tokeniseur `79e3e522…`, `177c7b61…`, `6f38c737…` : tous égaux au texte.
4. **Pré-vol** (`prevol-relance-v3-sortie.txt`, relu) : 22 corrections vérifiées sur 22 ; 240 épisodes, 151 conformes, 129 de base, 22 signalés, par méthode comme la table ; `par_methode_resolution` v1 15, v2 3, identifiants 4, aucune 218 ; 0 non résolu ; 2 236 conformes en longueur, 1 782 en contexte exact, 1 510 à trajectoire identique, 272 préfixes ; 2 400 notées ; 1 510 éligibles ; par condition 568/471/420, 570/496/430, 556/437/350, 542/378/310 ; 22 corrections sous consigne fausse, toutes conformes. Recalculs : 568 + 570 + 556 + 542 = 2 236 ; 471 + 496 + 437 + 378 = 1 782 ; 420 + 430 + 350 + 310 = 1 510 ; 51 + 66 + 87 + 68 = 272 ; 2 400 − 2 236 = 164 ; 2 236 − 1 782 = 454 ; 164 + 454 + 272 = 890 = 89 × 10 ; 2 236 − 2 160 = 76 ; 2 236 / 2 400 = 93,2 % ; 1 782 / 2 400 = 74,25 % ; 1 510 / 2 400 = 62,9 % ; marges 88, 76, − 9, − 43 : tous égaux au texte. Parent : 2 236 (93 %), 1 782 (74 %), 437 (73 %), 291 tests, 60 et 150 min, entropie, tolérance 0,02, 18 sur 20 : égaux.
5. **Essais ici** : `nice -n 10 env PYTHONPATH=src …/python -m pytest -q -p no:cacheprovider tests/test_bornes_relance_v3.py tests/test_rejeu_activations_v3.py` → **28 passed in 86.37s** (23 + 5 ; 23:07:00 → 23:08:28 UTC). Dénombrement de `test_bornes_relance_v3.py` : 8 + 4 + 8 + 2 + 1 = 23, égal à la pièce (« 23 passed in 3.02s ») ; `tests-bornes-sans-changement.txt` : 23 FAILED sur les scripts de `c2a8b6e1` (R5, artefact), relu.
6. **Suite ciblée** : la commande est dans `tests-cibles-relance-v3.txt`, ligne 3 (20 fichiers, `TOKENISEUR_LLAMA31=<tokeniseur de la révision 0e9e39f2…>`, `HF_HUB_OFFLINE=1`) ; résultat « 329 passed in 1484.24s (0:24:44) », code 0, 19:35:32 → 20:00:19 UTC. **Non rejouée** : elle exige le tokeniseur de Llama 3.1 à la révision de P3, absent de l'arbre et interdit au téléchargement ; la liste `CIBLES` du script v3 (lignes 251 à 256) compte 20 fichiers, celle du script v2 18 ; le motif de la dernière ligne (script, ligne 267) accepte « 329 passed in … (h:mm:ss) » et refuse tout « skipped » ou « failed ».
7. **Différences de code** : `git diff c2a8b6e1 145da951 -- src/controle_ia/runs_nuit/rejeu_activations_v3.py` : 0 octet ; `git diff --stat c2a8b6e1 145da951 -- scripts/ src/ tests/` : seuls les deux scripts v3, leurs compagnons, `tests/test_bornes_relance_v3.py` et son compagnon (165 insertions, 25 suppressions) ; `git diff --stat f921fcec 145da951 -- scripts/ src/ tests/` : vide. Contenu du diff des scripts, lu ligne à ligne : bornes réglables (`PLAFOND_AMORCE_MIN`, `DELAI_REJEU_MIN`, motif `^[1-9][0-9]{0,3}$`, défauts 110 et 60 seulement si la variable est absente, valeur vide refusée), préenregistrement par défaut = addendum v3, deux lignes de journal (délai écrit), commentaires ; rien d'autre : E9 et E12 exacts, aucun écart non déclaré.
8. **Gardes du script** relues : quatre libellés, chacun 1 occurrence dans le texte (`grep -c`) ; version 3 et citation de la table par la configuration vérifiées avant l'installation (lignes 125 à 139) ; branche existante refusée ; `ETAPES` ≠ `rejeu` refusé. **Module** : `exiger_config` (empreinte de table obligatoire), `charger_table_v3` (sceau, empreinte, version, doublon, forme), `verifier_table_au_chargement` (présence, empreinte de P3 citée, correction qui redonne l'empreinte, compte = `identiques_apres_table − identiques_base`), `classer_episodes` (couverture exacte dans les deux sens, seuil 10 sans effet à 0), `creer_manifeste` → `exiger_prereg_scelle` ; SIGTERM → `lever_sur_term` → `arret.json` « echec » ; sortie `tokenisation` aux clés attendues ; graines : `numpy.random.SeedSequence(entropie, spawn_key)` (`manifeste.py`), clé « fidelite » (R9). `prereg.problemes(texte)` = `['section vide ou à remplir : Contre-lecture']` ; sur la v2 scellée : `[]`.
9. **Essai jouet** : six journaux relus ; codes 0, 1, 124, 1, 1, 2 égaux à `codes.txt` et au texte ; `PLAFOND_AMORCE_MIN=720` et `DELAI_REJEU_MIN=600` écrits aux trois lignes annoncées ; table falsifiée arrêtée à « vérification de la table », « echec », aucun `donnees/` poussé ; plafond 1 min : TERM pendant les tests, code 124 ; délai 1 min : étape coupée à 60 s (19:45:46 → 19:46:46).
10. **Contrôles d'avant l'installation** : sain (code 127 voulu, après « addendum lu : 329 … présents et scellés » et poussée initiale) ; six artefacts arrêtés avant l'installation, code 2 ; gardes de citation du module dans l'arbre : configuration citée, parent, entropie, commit cité, arbre gelé = `f921fcec`.
11. **Registres de `main` au commit `f1791003`** (objets locaux, `git show`, sans `fetch`) : `registres/go.md` ligne 215 = GO-2026-11-02-27, calcul, 60 USD, échéance 2026-11-16, « aucun budget de temps qui coupe une étape », « attendu ≈ 15 USD », mots de Lazar 18:26 et 18:27 UTC et « je ne veux pas de blocage » : exacts ; `registres/decisions.md` ligne 1288 = R-1060 (GO-20 à -29 recopiés, verdict `64fab1a5…`, table v3 complète, aucun nœud) ; `registres/depenses.md` ligne 322 : instance 58851293, amorce finie 18:12:14 UTC code 0, vie ≈ 90,5 min, aucune dépense sous GO-27 ; `registres/arrets.md` ligne 74 : 58851293 détruite par son identifiant. Verdict du lecteur neuf (`64fab1a5…`) : 7 sur 7, 54 sur 147, « méthode non transposée », 93 manqués par la durée (2 400 s), « addendum v3 sans règle B, aucun nœud », réserve HG-2 et mesure incomplète : tout égal au texte.
12. **Devis** : 1 à 1,5 h × 1,40 = 1,4 à 2,1 USD ; 720 + 5 + 30 = 755 min × 1,40 / 60 = 17,62 USD ; × 2 = 35,2 < 60 ; gardes 600 et 720 ≥ 8 × attendu (15 à 30 min ; 60 à 90 min) : exact. Filtres d'offre identiques à « Location » de la v2 (lignes 478 à 483). Commande de création : `GO_ID=` devant `vastai create instance` comme l'exige `.claude/hooks/garde_calcul.py` (lignes 93 à 100) ; `DEPOT_URL` = dépôt de travail privé ; jetons lus par nom, jamais écrits.
13. **Heures du texte** : 20:01 (commit `145da951` à 20:01:38 UTC), 18:26 et 18:27 (go.md), ≈ 00:21 (addendum v1, ligne 58), 18:12:14 (depenses.md, arrets.md) : toutes sourcées. Aucune clé ni jeton dans le texte (`grep` sur `hf_`, `ghp_`, `github_pat`, `token=`).
14. R3 : le texte ne vise aucun signe (entrées de la comparaison appariée ; « rien n'est relancé pour la faire tenir ») ; R4 : lignes « trop beau, R4 » du parent gardées, réserve HG-2 rapportée sans changer de classe ; R12 : noms nouveaux partout (v5, v3, `calcul/r1-relance-v3-reel-v1`, `-v2` pour la reprise E21), rien d'écrasé ; `CLAUDE.md` de l'arbre identique à celui du dépôt de travail (`diff` vide).

## 6. Ce que je n'ai pas pu vérifier, et pourquoi

- La suite ciblée de 329 tests (tokeniseur absent, téléchargement interdit) : relue sur la pièce seulement (§ 5, point 6).
- L'égalité « à l'octet » de la table v3 et de son sceau avec la branche `calcul/r1-resolution-graine-v1` (tête `ab808842…`) et les résultats scellés `8e6a4912…` et `67482545…` : branche absente des objets locaux, `fetch` interdit ; `resultat_graine_sha256` de la table = `67482545…` et le verdict du lecteur neuf citent les mêmes empreintes, c'est tout ce que j'ai.
- Les empreintes des deux fichiers de scores de R2 (`10838eea…`, `1ebbeff8…`, branche `calcul/r1-r2-reel-v1`) : rien sous `donnees/` n'est ouvert, branche absente localement.
- Le code « R2 seul » de conv-audit (`constantes_v3.COMMANDE_REJEU`, `entrees_v3.verifier_arret_r1`), l'analyse principale `8e267952…` (ligne 146) et les messages n° 339, 343, 344, 348, 354 : pièces d'une autre session, non présentes dans l'arbre ; cités par l'addendum v1 (lignes 30 à 35, 94) aux mêmes numéros et empreintes.
- Le comportement du module sous SIGTERM pendant la relance réelle (écriture d'`arret.json` « echec ») : l'essai jouet « délai 1 min » tourne sur un module témoin qui dort ; la garde est celle de la v1 et de la v2 (`lever_sur_term`, K-1), inchangée.
- Les consignes de P3 et les textes d'actions (interdits) : le pré-vol les a lus ; je n'ai relu que ses comptes.

## 7. Fichiers lus et leurs empreintes (`sha256sum`)

Liste complète dans `/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/contre-lecture-relance-v3/empreintes-lues.txt` (49 lignes), recopiée ici :

- `prereg/R1-addendum-relance-v3.md` : `382ba6272ea0856dd9ba699f1d16eabef66fc12be288c214af71c5de28a5a05d`
- `prereg/R1-addendum-relance-v2.md` : `9d17d640509c9b5dd0285e90f3096145b82f2e0ea2e73e62725c0e0c8cb71059`
- `prereg/R1-addendum-relance-v1.md` : `485acc3a57bf5377cc2d62d8b161eb7b3f669dbeb3ec0bc1b35d260e6f518652`
- `prereg/R1-R2-rejeu-p3-v1.md` : `80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea`
- `prereg/R1-rejeu-config-v5.json` : `acad6253f3c9f4d93c45a453ae8f5dcb122049a979cf43000d47c5f9c1edd4b8`
- `prereg/R1-rejeu-config-v4.json` : `09bc5813d33952ec6e59b680d20b18484c1d017399fc7abb10c9d639dc1d0d04`
- `prereg/R1-rejeu-config-v2.json` : `f043212f48771011ef5096e1637a555b950d58cdad31c3e13d68ac91a18212f4`
- `prereg/R1-table-tokenisation-v3.json` : `ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423`
- `prereg/R1-table-tokenisation-v2.json` : `5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2`
- `prereg/gabarit-preregistrement-v1.md` : `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`
- `scripts/amorce_instance_r1_relance_v3.sh` : `82f386876d3e606e6d8d7d6c388e42a822266d7cf899d448991b8af456badef7`
- `scripts/r1_relance_instance_v3.sh` : `24744794808832e30cb8fa47c45a19de5a530d5ce06db1bd0557a17d3e35e4eb`
- `scripts/r1_relance_instance_v2.sh` : `8439cf1cca3d4406adfefd89a9f06963d09a688e991b614f60d1d7fe5f8813c5`
- `src/controle_ia/runs_nuit/rejeu_activations_v3.py` : `0581cf9a32e054e5044809f80078e3d33e3de27a22830e40ca8aa45a03ca2adc`
- `src/controle_ia/runs_nuit/rejeu_activations_v2.py` : `6f23f802548e4de03dd7431da1179001db3ceb32d9809edbec09bc5e6b07bd2d`
- `src/controle_ia/runs_nuit/rejeu_activations_v1.py` : `dde8aa673720d082945722e57f31d5dd4b51e44d72f0550f7a15f5990e2ea3b5`
- `src/controle_ia/runs_nuit/resolution_graine_v1.py` : `cdc22b5ad2659f82f512c39545c52fc826a6be2dc60fb3aeafda0c5d014a9663`
- `src/controle_ia/runs_nuit/resolution_tokenisation_v1.py` : `e8568c3c8d48a5713fddd7d55d805e54b9c702edee2b7d2f218db49c230434c9`
- `src/controle_ia/prereg.py` : `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`
- `src/controle_ia/manifeste.py` : `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d`
- `src/controle_ia/gardes.py` : `a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439`
- `src/controle_ia/harnais/validation_reelle.py` : `d25e4cd92d73eef4d2bd6c7d17328daf49a49c76eab7afd91500d9c04ded8289`
- `.claude/hooks/garde_calcul.py` : `84512d4a1bef0403668000942cf5f5d383aab280bf5a58f6aec328e77f807d59`
- `tests/test_bornes_relance_v3.py` : `1b1fce06d91215585dd32d5ccef1c67380df62805d55a4235ee7ef14e87303a3`
- `tests/test_rejeu_activations_v3.py` : `ef7be3f70e1a601aae404570f96f373448de98e8007519d17448d07120a352f8`
- `CLAUDE.md` : `e28d090e41ec11fd3363666f031a3d67ba530bf7d6d90b83f4d44127a6b65fad`
- `docs/notes/runs-r1-r2-r4-v1/procedure-relance-r1-v2.md` : `ae1ff08983f2220133cbc7745cbeb6a66a75bda622320e78779287b0fef5dd3b`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/controles-avant-installation-v3.txt` : `c909de085361a3605db191a0e0e1b6b1d3e392d87219214d5d5fa91fd70b87d5`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/prevol-relance-v3-sortie.txt` : `b9dbadbad1c189f13a64c799a729e5b605d36000859a549e6e851cc873fdff54`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/tests-bornes-relance-v3.txt` : `8dc0eef7df36db664c88f7bdb2ec8ba2b61047f68057dec5ff9f3e2a47bc9776`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/tests-bornes-sans-changement.txt` : `afb17d9de18a9c57319d7dfa157bc8e8a89f04644fe1e64d6998ba6be0f79ce1`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/tests-cibles-relance-v3.txt` : `e02256eeb2f249b1f56d14201a23e2a9e3d3e39b10a8fb59fec774134021843a`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/prevol_relance_v3.py` : `61dd497e42e4661ac84918975f9855c7f41d3e45f8beeb85ed4b9e4ad129e360`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/controles_avant_installation_v3.sh` : `208abebc248ae3413425f04c11a6087bb59f619ff7c15fae15fd8807e8ef009b`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/LISEZMOI.txt` : `fd1db8370d770211bd9a1eb4bacc788376c3dd6f57ea9bd5591c6de7204fc502`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/codes.txt` : `b7a0dc1f864efe9f56a1dfb4c1e851bf12c511c9e7d1d55a8bc1178eac8f12a1`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/inspection-falsifiee.txt` : `62be251fb34f9c275f9400a7758f7f417c324bae5c31a0226b6a85adeeb4c054`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/inspection-sain.txt` : `6fca7d7a056971c790b25d32a9fed3badacd4eb931b8e9e5453ec086ca484719`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/amorce-delai-1min.log` : `3bf5bfc0afce4d2f522ce982c88d231cad59b9f81a7473d16e01c180c7059566`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/amorce-delai-invalide.log` : `def23379850eea9d1ce781e4c528c0165c342cbcd1f0f719575cb439dcd9676f`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/amorce-plafond-1min.log` : `1d847507608f620ae63a8bde177b54b777db21eb9b69077fa46210e96d6d85ce`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/amorce-plafond-invalide.log` : `81cf66a27b0de145cc1dc90d998f19d2ab9b15ca64a7cf96d7ffef213b83e263`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/amorce-sain.log` : `968e28f101d5ed0bb611492b3fbd485aa974fd558aa292f302541b1f8df5b151`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/amorce-table-falsifiee.log` : `a54a7d3143054ffea71a5cfb579a65ac179949f9eee419af08805afafe4b58c9`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/lancer.log` : `6ce7c50a1bf721163706b27f7497b264ea78012338c1764493620c8049f9296c`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/preparer.log` : `4a707122b4d7519fee1cef60ac02666c606876bd0c89e0a048b00b6dd3295d5e`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/lancer_essais_jouet_v3.sh` : `27c399b5e11a4b7e2babbf58b91eba0ff9e554fd715d4e6e31c8a91064ddacfd`
- `docs/notes/runs-r1-r2-r4-v1/relance-v3/essai-jouet-relance-v3/preparer_essai_v3.py` : `5c9ed9430deb8411e4c0c0197f77894a9dfc750676f50dd8306ad9bd1970b2b9`
- `/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/contre-lecture-relance-v3/verdict-rejeu-graine-v1.md` : `64fab1a5854deba0ad669d0c4840b6736e9cb680a22928d548c63093bb273e68`

Lectures partielles (par recherche ou extraits) : `rejeu_activations_v2.py`, `rejeu_activations_v1.py`, `resolution_graine_v1.py`, `resolution_tokenisation_v1.py`, `manifeste.py`, `gardes.py`, `validation_reelle.py`, `garde_calcul.py`, `r1_relance_instance_v2.sh` (liste `CIBLES`), `R1-addendum-relance-v1.md`, `R1-addendum-relance-v2.md`, `R1-R2-rejeu-p3-v1.md`, `procedure-relance-r1-v2.md` (section 7), `preparer_essai_v3.py` (non lu : en-tête du LISEZMOI seulement), registres de `main` au commit `f1791003` par `git show`. Lus en entier : le texte, les deux scripts v3, `rejeu_activations_v3.py` (lignes 1 à 140, 172 à 300, 440 à 498 ; le reste par recherche), `test_bornes_relance_v3.py`, `prereg.py`, le gabarit, `CLAUDE.md`, toutes les pièces `.txt` et `.log` sous `relance-v3/`, `controles_avant_installation_v3.sh`, `lancer_essais_jouet_v3.sh`, le verdict `64fab1a5…` (sections 0 à 2 en entier, le reste par recherche).

Fin de rédaction : 2026-11-02T23:13:57Z UTC.
