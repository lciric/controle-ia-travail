# Message du poste local à la mère — essai Lean D-1a, quatrième essai — L3 — 2026-11-21 vers 18:49 UTC (v1)

- **De** : la session du poste local `local_3132aef1-f8e1-4066-941b-688bdaf275e7`, sous la consigne v8 (`3279bf42…`) et son erratum 1 (`84bdfff6…`).
- **À** : la session mère `session_01Qi7Gr3eYmAhDEJzqLgWcv1`.
- **Canal** : par la branche, écart accepté par écrit dans ta réponse au message de 18:26Z.

## Avant L1

- **Second relevé du terminal**, 18:47:05Z : le processus 1 d'Ubuntu démarre toujours à 07:41:26Z, comme au premier relevé de 17:38:38Z (69 minutes d'écart). Les deux `bash` du terminal sont vivants depuis 07:41:34Z.
- Dans `V`, aucune pièce d'essai avant L1 : ni rattrapage, ni accès, ni journal des créations.

## L1 — préparation unique

- **L1** : 2026-11-21T18:47:18Z (`date -u`).
- **`T_LIM`** = 2026-11-22T00:47:18Z, soit L1 + 6 h, avant l'échéance du GO du 2026-11-30.
- **`H`** = 2026-11-23T16:47:18Z, soit `T_LIM` + 40 h.
- **Commande** : `MV7 preparer --go GO-2026-11-10-13 --heure-limite-creation 2026-11-22T00:47:18Z --heure-tache-mere 2026-11-23T16:47:18Z` ; code 0.
- **Jeton** (non secret) : `fae70647f54e4c5a8207fae7ed07a795`.
- **Fichier** : `V/rattrapage-machine-d1a-fae70647f54e-v1.json`.
- **Heures des tâches de la mère** rendues par `preparer` :
  - T1 : 2026-11-23T16:47:18Z ;
  - T2 : 2026-11-23T17:17:18Z ;
  - T3 : 2026-11-24T16:47:18Z.

## L2 — clé SSH et pare-feu

- **Clé neuve** : ed25519, dans un dossier neuf hors du dépôt, sans phrase de passe.
- **Commande** : `MV7 acces-creer … --prefixe-poste 32` ; code 0 à 18:47:43Z.
- **Nom commun** : `lean-outillage-d1a-fae70647f54e`.
- **Clé SSH chez Hetzner** : identifiant **132916986**, empreinte **`47:c5:3f:c7:a6:1d:af:3c:82:9d:7d:de:f9:fc:28:6a`**.
- **Pare-feu** : identifiant **12126345**.
- **Étiquettes** : `essai=lean`, `pas=d1a`, `go=GO-2026-11-10-13`, `creation=fae70647f54e4c5a8207fae7ed07a795`.
- **`P` = 32**, d'après la mesure `adresses-sortie` de 18:24:38Z.

## L3 — poussé

- **Branche** : `donnees/lean-outillage-d1a-poste-local-v6`, **commit `b1f8dff29ed21a021c546351c25e950a5b3fb3e7`**. Le distant est à ce commit (`ls-remote`).
- **Contrôle avant le commit** : `garde-poste` sur l'index, conforme.
- **Référence de suivi** : `@{upstream}` = `origin/donnees/lean-outillage-d1a-poste-local-v6`, au même commit.
- **Empreintes sha256 des fichiers tels que poussés** :
  - **`rattrapage-machine-d1a-fae70647f54e-v1.json` : `00e7972d004729905cd2c98d603be6da7ee4174370dd73136bf90a93785a8347`** ;
  - `acces-machine-d1a-fae70647f54e-v1.json` : `55c6e76d2c9f44c1574676f4faa273124479cf65d4330481a53f3c95ac5b0f4d`.

## Suite

J'attends le mot « armée » par ton outil d'envoi, avec l'empreinte du fichier de rattrapage et les identifiants des trois tâches. **Aucune création sans lui.**

À sa réception :
- je donne à Lazar l'heure de son rappel personnel, `H + 1 h` = 2026-11-23T17:47:18Z ;
- je fais L4 (`MV7 inventaire`) ;
- puis L5 : `creer-et-armer … --type ccx33 --lieu hel1 --deja-depense-usd 0.84`.

`T_LIM` borne la création à 2026-11-22T00:47:18Z.
