# Vérification de l'ordre de lancement de la course de dose–réponse, v5 (branche (b), option A)

Contre-lecteur : le même que pour la v2 et la v3 (Opus 5.5, sous-agent). Pièce vérifiée : `docs/notes/code-dose-reponse-consigne-cachee-v1/ordre-de-lancement-propose-dose-reponse-v5.md`, comparée à la v4.

## Verdict

**Non scellable en l'état. Scellable après deux corrections bloquantes (V5-B1, V5-B2) et deux mineures.**

- **V5-B1.** La vérification du code du lecteur du texte (le lecteur qui juge le critère 3) refusera la ligne `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE` telle qu'elle est inscrite sur main. La garde de l'ordre arrête alors proprement avant toute dépense, mais la course ne peut pas partir. Le remède demande un mot de la mère, ou de Lazar, sur le registre.
- **V5-B2.** Deux pièces citées par les lignes du registre ne sont pas portées sur la branche de lancement.

Tout le reste des changements annoncés est juste contre le code. Aucune correction de la v4 n'est perdue.

## Contrôles faits

**Empreintes et code.**
- v4 = `b9450aa1…`, v5 = `a91c32d0…`, conformes à leurs compagnons.
- `diff` v4 → v5 : seuls changent l'en-tête, les préalables 1 et 3, la section 1, la section 2 (historique complet, vérification du code, lanceur et amorce v3) et la section 5 (étapes du critère 3).
- `a02b6540 → 6b2b821a` sur `src scripts tests .claude pyproject.toml requirements-*.txt` : ajouts seulement. `controles_v2.py`, `course_v2.py`, `lecture_v2.py` et l'écriture de la configuration sont inchangés.
- Le code de 6b2b821a égale celui de la tête de branche 5bd4026a.

**Amorce v3** (`722390c3…`, égale à `DR_AMORCE_SHA256` de l'ordre).
- Elle ne change que l'extraction : `extraction_v1` ajoute le chemin de `designation_critere_3` quand la clé n'est pas `null`, ainsi que la liste d'essais v3 (`4d99cacc…`, 58 attendus) et l'étiquette de la ligne de démarrage.
- Rejoué sur la configuration désignée, `extraction_v1` sort quatre motifs, dont `/prereg/G0-critere-3-designation-course-v1.md*` (compagnon compris).
- L'appel se fait depuis `$R/amorce-depot`, où `src/` est extrait.

**Lanceur v3.** Seule change l'amorce citée (et les messages). Les gardes sont identiques à la v2.

**Texte de désignation sur main** : `19dbc99e…`, conforme à son compagnon et à la ligne `DESIGNATION-CRITERE-3`.

**Rejeu hors dépôt** (contenu de 6b2b821a, registres de main, banque, texte de désignation, `torch` simulé pour l'import) :
- `ecrire_configuration_dose_reponse_v2.py … --designation <fichier de la ligne 47>` écrit et scelle la configuration (le fichier porte exactement les trois clés exigées) ;
- `controles_avant_depense` passe : 64 tâches, rangs 125 à 210 ; `controler_registre` trouve les lignes BANQUE et CODE (la v2 cite 6b2b821a) et les quatre lignes de `lignes_registre`.

**Corrections de la v4 gardées** : N1 (`set -euo pipefail`, `exit 1`, `grep` de la déclaration en tête des deux appels de la section 2), N2, N3, N4, m8 et toutes celles de la v3.

## Défauts bloquants

**V5-B1. La ligne `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE` inscrite sur main cite un fichier hors du dossier que le lecteur exige.**

Passage du préalable 3 : « copiée sans le suffixe sous `registres/` (chemin au choix de la mère) ».

Le code n'admet qu'un seul dossier :
- `scripts/lecteur_texte_dose_reponse_v2.py`, l. 127 : `DOSSIER_CODE = "registres/code-lecteur-du-texte-dose-reponse/"` ;
- `controler_code`, l. 590-591 : `if not entree["chemin"].startswith(dossier): raise ArretPiece(...)`.

La ligne de main (16:50:12Z, R-5327) cite `registres/code-dose-reponse-consigne-cachee/CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-6b2b821a…-v1.json`. Conséquences :
- `verifier-code` de la section 2 refuse : « Code autre que 0 : aucune création ». La garde de l'ordre fonctionne, mais la course est bloquée.
- Si cette garde était sautée, le lecteur du texte (étapes (b) à (d)) refuserait de même, et le critère 3 ne serait plus jugeable sur cette course.
- On ne peut pas simplement inscrire une ligne de plus : `exiger_ligne` (l. 533-538) exige **exactement une** ligne par clé, sinon arrêt.

Correction : remplacer la puce `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE` du préalable 3 par :

« `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE` : la pièce doit être au chemin `registres/code-lecteur-du-texte-dose-reponse/CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-6b2b821a28f8bebebae2188d9f020ce731464306-v1.json` (`DOSSIER_CODE` du lecteur : tout autre dossier est refusé par `verifier-code` et par le lecteur). La ligne inscrite le 24 novembre à 16:50:12Z (R-5327) cite le dossier `registres/code-dose-reponse-consigne-cachee/` : elle est inemployable, et une seconde ligne est refusée (« exactement une »). **Aucune création avant le mot de la mère, ou de Lazar si le registre ne peut être corrigé sans lui**, sur l'une de deux voies :
(i) correction du registre : la pièce est recopiée à l'octet sous le dossier exigé (même empreinte `f6bc347a…`, compagnon compris), et la cellule « chemin » de la ligne est corrigée, date et empreinte inchangées ; correction consignée au registre des décisions ;
(ii) code neuf du lecteur, qui lit le dossier inscrit (classe B, commit neuf) : écartée, car sa ligne de code serait une seconde ligne de la même clé.
Recommandation : (i). La ligne doit rester datée avant la création de l'instance (texte de désignation). »

**V5-B2. Les pièces citées par deux lignes ne sont pas portées sur la branche de lancement.**

`exiger_ligne` vérifie, pour chaque ligne, le fichier cité et son compagnon **dans l'arbre** (`compagnon_conforme(racine / chemin)`). Or deux de ces fichiers sont sur main et absents de 6b2b821a, et la section 1 ne les copie pas :
- le fichier de `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE`, lu par `verifier-code` (section 2) et par le lecteur (section 5) ;
- `registres/sondes-lues-critere-3/SONDES-LUES-CRITERE-3-v1.md`, lu par le lecteur en mode réel (`controler_registre_reel`).

Les arbres de la section 5 sont tirés de la branche de sortie, donc de la branche de lancement. Sans ces fichiers, `verifier-code` puis le lecteur s'arrêtent.

Le fichier de `CODE-MOTS-ET-COUT-T06` et sa contre-lecture sont déjà à 6b2b821a, de même que la contre-lecture du lecteur. Aucune copie n'est requise pour eux.

Correction : dans le bloc de la section 1, après la ligne 46, insérer

```bash
git checkout origin/main -- registres/code-lecteur-du-texte-dose-reponse/CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-6b2b821a28f8bebebae2188d9f020ce731464306-v1.json registres/code-lecteur-du-texte-dose-reponse/CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-6b2b821a28f8bebebae2188d9f020ce731464306-v1.json.sha256 registres/sondes-lues-critere-3/SONDES-LUES-CRITERE-3-v1.md registres/sondes-lues-critere-3/SONDES-LUES-CRITERE-3-v1.md.sha256 registres/code-dose-reponse-consigne-cachee/CODE-DOSE-REPONSE-CONSIGNE-CACHEE-6b2b821a28f8bebebae2188d9f020ce731464306-v2.json registres/code-dose-reponse-consigne-cachee/CODE-DOSE-REPONSE-CONSIGNE-CACHEE-6b2b821a28f8bebebae2188d9f020ce731464306-v2.json.sha256
```

Ajouter les mêmes six chemins à la commande `git add -f` de la ligne 51. La pièce CODE v2 n'est lue par aucune garde : elle est ajoutée pour la traçabilité.

## Point à vérifier, sans défaut constaté

Le commit cité par `CODE-MOTS-ET-COUT-T06` (`da06bb57…`) doit être un ancêtre de la tête de la branche de lancement (`controler_code`, l. 606-607).
- Le clone de cette session est superficiel : je n'ai pas pu l'établir.
- L'ordre fait `git fetch --unshallow` avant `verifier-code`, qui le contrôle et refuse proprement sinon.
- Si ce refus survient après l'historique complet : nœud, aucune création.

## Défauts mineurs

- **V5-m1.** Préalable 1, passage « La ligne v1 (`6b2b821a28f8bebebae2188d9f020ce731464306`, R-5306) reste inscrite ». La ligne v1 cite `a02b6540070aa5731875d07fbbe124f2dbe27f3b` ; le remplacement global a débordé. Corriger en « La ligne v1 (`a02b6540070aa5731875d07fbbe124f2dbe27f3b`, R-5306) reste inscrite ».
- **V5-m2.** Préalables 1 et 3 : « pièce proposée … à copier … inscrite sur main » et « à inscrire par la mère ». Les deux lignes sont déjà inscrites (R-5327, 16:50:12Z). Remplacer par « inscrite (R-5327) » et citer les chemins inscrits, sous réserve de V5-B1 pour celle du lecteur.

## Cloisonnement

Je n'ai ouvert aucune pièce privée (empreintes seulement) et lu aucune sortie de course, aucun score, aucun verdict. Rien n'est modifié, poussé, lancé ni loué. Mes rejeux sont dans `sim-controles-v5/` du bloc-notes, hors dépôt.
