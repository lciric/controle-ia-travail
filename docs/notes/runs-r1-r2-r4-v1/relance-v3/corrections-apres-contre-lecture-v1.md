# Corrections de l'addendum v3 de relance de R1 après la contre-lecture 1 — v1

- Rédacteur : sous-agent de rédaction de session-depot (Fable 5.1) ; texte seul corrigé (aucun code, script ni
  configuration), aucun commit, aucun `.sha256` créé ni modifié, aucun réseau.
- Arbre : `wt-relance-v3`, branche `prep/r1-relance-v3`, tête `a62f44df`.
- Brouillon relu : `prereg/R1-addendum-relance-v3.md`, `382ba6272ea0856dd9ba699f1d16eabef66fc12be288c214af71c5de28a5a05d`
  (vérifiée par `sha256sum` avant toute modification).
- Contre-lecture : `docs/notes/runs-r1-r2-r4-v1/relance-v3/contre-lecture-addendum-relance-v3-v1.md`,
  `c19fdbc7d6f83a5ce26b12b0fa9b5604a8bbfba8086691e723837836576add59` (vérifiée).
- Brouillon 2 (corrigé, même nom, non scellé) : empreinte en fin de note ; différence exacte :
  `corrections-apres-contre-lecture-v1.patch` (`git diff -- prereg/R1-addendum-relance-v3.md`).
- Date (UTC, `date -u`) : 2026-11-02 23:19 pour le texte ; note écrite ensuite.
- `prereg.problemes` sur le brouillon 2 : `['section vide ou à remplir : Contre-lecture']` (seul le marqueur
  « À REMPLIR » du traitement final, laissé pour session-depot). Simulation hors de l'arbre, marqueur retiré : `[]`
  (l'entrée « Contre-lecture 1 » porte ses deux empreintes de 64 hexadécimaux).

## Tableau des corrections (lignes du brouillon 2)

| Point | Lignes (brouillon 1 → brouillon 2) | Ce qui est écrit |
|---|---|---|
| I1 | 127 → 130 (E8 (c)) | « `DELAI_REJEU_MIN` hors des entiers de 1 à 9999 (avant le clonage du dépôt de travail par le script : l'amorce a déjà cloné le sien pour lire le script) » ; `PLAFOND_AMORCE_MIN` reste « (code 1, avant le clonage) » |
| I1 | 386 → 411-412 (« Essais », essai des bornes) | « refusées avant le clonage (amorce : avant tout clonage, code 1 ; script : avant le clonage du dépôt de travail par le script, l'amorce ayant déjà cloné le sien pour lire le script, code 2) » |
| I1 | 397 → 423-424 (« Essais », essai jouet, délai « abc ») | « refus du script avant le clonage du dépôt de travail par le script (l'amorce a déjà cloné le sien pour lire le script), code 2 » |
| I1 | 430 → 459-460 (« Liste d'arrêt ») | « **script, avant le clonage du dépôt de travail par le script** (l'amorce a déjà cloné le sien pour lire le script ; code 2) » ; la ligne « amorce, avant le clonage (code 1) » est inchangée |
| I2 | après 147 → 152-170 (« Écarts au parent », après « Inchangés ») | Paragraphe « Où atterrissent les renvois de l'addendum v2 (lignes 175 à 183, « Renvoyé à l'addendum v3 ») » : G3 → E19 ; G4, G5 et P-R5 → E4, E14, E15, « Prédiction chiffrée et signe attendu » ; G6 → E11, E12 (et E16 pour le signalement à conv-audit) ; G7 → E10 et « Tests attendus » ; G9 → E13 ; G10 → E2 et « Métrique », plus la part de G10 sur l'essai au nom hérité `test_relance_regle_b_non_resolus_fidele_faux_et_seuil` (`tests/test_runs_nuit_v2.py`, dans `CIBLES`), **couverte nulle part dans le brouillon 1**, déclarée à nouveau (nom et docstring inchangés, m-1 de la v1, sans effet sur la lecture) ; « étape 3 du brouillon 1 (préalables, complément court) » → ce texte entier en tient lieu (préalables à l'en-tête et à l'étape 2 ; complément court séparé sans objet) ; « ligne « Relance » des critères » → « Critères de lecture gelés », sa part « plus de 10 non résolus » sans objet (E2, E5, E6) ; m-8 → étape 3 du plan |
| M1 | 60-61 → 62-63 (en-tête, « Tests attendus ») ; 78 → 80-81 et 79 → 82 (pièces) ; 379 → 404 et 388 → 414 (« Essais ») | « au commit `d803a8d6` (même `src/`, `tests/`, `scripts/` que `f921fcec` et `145da951`) » à la place de « au commit cité » pour la suite ciblée et l'essai des bornes ; les autres « au commit cité » (empreintes des fichiers de code, E12, en-tête des essais, portée de la contre-lecture) désignent bien `f921fcec` et restent |
| M2 | 463-467 → 493-518 (« Contre-lecture ») | Entrée nommée « **Contre-lecture 1** » ; brouillon relu (`382ba627…` en entier, commit `145da951`) ; rapport (chemin, `c19fdbc7…` en entier, commit `a62f44df`) ; verdict ; une ligne par correction (I1, I2, M1 à M4, remarques) ; traitement final par session-depot : « À REMPLIR (au scellement) » |
| M3 | 138 → 141 (E19) ; 344 → 367 (« R2 ») | « R-1116 du registre de conv-audit, recopiée en R-1033 de `main` » |
| M4 | 371-372 → 394-397 (« Essais », pré-vol) | « 128001, 128008, 128009 : pièce = `fins_du_format` de la table v3, `prereg/R1-table-tokenisation-v3.json`, `ead8a668…` ; assertion du script `prevol_relance_v3.py`, valeurs non écrites dans sa sortie » |
| Remarque (code 127) | 398-401 → 425-429 (« Essais », contrôles d'avant l'installation) | Parenthèse : « le cas « sain » y finit en code 127 sur `nvidia-smi` absent de la copie, arrêt voulu après les contrôles et la poussée initiale ; six artefacts arrêtés avant l'installation, code 2 » |
| Remarque (« partie de ») | 27 → 29 (en-tête) | « à partir de `c2a8b6e1` » |
| Date et statut | 3-6 → 3-8 (en-tête) | « brouillon 2 (texte, non scellé) : brouillon 1 (`382ba627…`, commit `145da951`) corrigé selon la contre-lecture 1 … ; reste le traitement final … » ; « Date (UTC) : 2026-11-02 23:19 (brouillon 2 ; heure relevée par `date -u`) » |

## Vérifications faites avant d'écrire

- I1 : `scripts/r1_relance_instance_v3.sh` lignes 56 à 58 (garde) et 82 (clonage du script) ; `scripts/amorce_instance_r1_relance_v3.sh` lignes 25 à 29 (garde du plafond) et 39 à 47 (clonage de l'amorce, puis lecture du script) : l'amorce ne lit pas `DELAI_REJEU_MIN`.
- I2 : addendum v2 scellé, lignes 175 à 183 ; brouillon 1 de la v2 lu dans l'objet git local `21a6e583` (`7915a3d6…`, égale à l'empreinte que cite la v2 scellée) : G3 à G10 aux lignes 111 à 118, étape 3 aux lignes 297 à 303, ligne « Relance (étape 3) » à la ligne 353 ; l'essai au nom hérité existe à `tests/test_runs_nuit_v2.py`, ligne 134, fichier dans `CIBLES` (script v3, lignes 251 à 256).
- M1 : `tests-cibles-relance-v3.txt` et `tests-bornes-relance-v3.txt`, ligne 1 : commit `d803a8d6` ; `git diff --stat f921fcec d803a8d6 -- scripts/ src/ tests/` et `git diff --stat d803a8d6 145da951 -- scripts/ src/ tests/` : vides.
- M3 : `git show f1791003:registres/decisions.md`, ligne 1261 (R-1033 : « recopiées à l'identique depuis `canal/conv-audit-n04` (R-1116) ») ; R-1116 absente des entrées de `main` ; addendum v1, ligne 9.
- M4 : `prereg/R1-table-tokenisation-v3.json`, clé `fins_du_format` = [128001, 128008, 128009] ; `prevol_relance_v3.py`, ligne 91 (assertion) ; aucune des trois valeurs dans `prevol-relance-v3-sortie.txt`.
- Remarque 127 : `controles-avant-installation-v3.txt`, ligne 4 (« sain : code 127 ») ; `controles_avant_installation_v3.sh`, lignes 5 à 7.
- Aucun chiffre neuf sans source ; aucune clé (`grep` sur `hf_`, `ghp_`, `github_pat`, `token=` : rien).

## Réserves

- La part de G10 sur le nom d'essai hérité n'était rattachée à rien dans le brouillon 1 : elle est **déclarée** dans le paragraphe ajouté (aucun renommage, qui changerait le commit du code) ; session-depot peut préférer un autre traitement.
- Les deux fichiers de cette note n'ont pas de compagnon `.sha256` (interdit au rédacteur) : empreintes ci-dessous, à sceller par session-depot.

## Empreintes (sha256sum, après écriture)

- 86c68b0ec323cfdce1a6a21d1fcee14ed8d0647f485906eb031e7ee6ac32746d  prereg/R1-addendum-relance-v3.md
- 73de584a7863b5c4d224459a658167ab75f61d2eddb14498e7b9ea759584bed2  docs/notes/runs-r1-r2-r4-v1/relance-v3/corrections-apres-contre-lecture-v1.patch
- (cette note : empreinte relevée par session-depot ; elle ne peut pas se citer elle-même)
