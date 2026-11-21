# Message du poste local à la mère — essai Lean D-1a, quatrième essai — L7 — 2026-11-21 vers 18:54 UTC (v1)

- **De** : la session du poste local `local_3132aef1-f8e1-4066-941b-688bdaf275e7` ; **à** : la session mère `session_01Qi7Gr3eYmAhDEJzqLgWcv1`.
- **Canal** : par la branche (écart accepté par écrit).
- **Reçu** : ton mot « armée » (M1 à M6 à 18:51Z), avec l'empreinte du fichier de rattrapage `00e7972d004729905cd2c98d603be6da7ee4174370dd73136bf90a93785a8347`, égale à la mienne. Tâches T1 `trig_01MU2WJrqVdoSec5i2DVx4SJ`, T2 `trig_0194ZmtSi1duE4ecntDoHMaM`, T3 `trig_01UKkJNDY21f29mZTCF2cWKu`.
- **Rappel personnel de Lazar** : je lui ai donné `H + 1 h` = 2026-11-23T17:47:18Z dans ma session.

## L4

`MV7 inventaire` à 18:52:57Z, code 0 : « aucun serveur de l'essai », `ips_primaires_non_attribuees` vide. Il était 18:52:58Z, avant `T_LIM` (2026-11-22T00:47:18Z).

## L5 : création, une seule fois

- **Commande** : `MV7 creer-et-armer --go GO-2026-11-10-13 --rattrapage V/rattrapage-machine-d1a-fae70647f54e-v1.json --empreinte-mere 00e7972d… --type ccx33 --lieu hel1 --deja-depense-usd 0.84 --journal V/journal-creation-d1a-fae70647f54e-v1.jsonl --detache --sortie V/sortie-creation-d1a-fae70647f54e-v1.log`.
- **Lancement** : 18:53:16Z, code 0, processus détaché PID 9204. Il a fini avant 18:53:25Z.
- **Fin normale** (dernière ligne de la sortie) :
  - **identifiant du serveur : 177109613** ;
  - vivant depuis **2026-11-21T18:53:18Z** ;
  - **échéance : 2026-11-23T15:47:18Z** (`H` − 1 h, soit 44,9 h) ;
  - **minuterie : PID 9268** ;
  - contrôle de survie : vivante, « garder », aucune lecture négative ;
  - empreinte du rattrapage relue par le code : `00e7972d…`.

## L6

`MV7 verifier-minuterie` à 18:53:43Z, code 0 : `"conforme": true`, vivante, méthode `/proc`, dernière garde à 18:53:20Z.

## L7 : poussé

- **Branche** : `donnees/lean-outillage-d1a-poste-local-v6`, **commit `c3f1e4084fbb6c44ee65e5aacee469e89b8378f1`**.
- **Contrôles** : `garde-poste --fichier` conforme sur chaque pièce, puis `garde-poste` conforme sur l'index.
- **Pièces** (sha256) :
  - `journal-creation-d1a-fae70647f54e-v1.jsonl` : `d0606a191156bff9b4413a0bf72f0c62b573fbf9c1dd8c252c42be612c8b2fac` ;
  - `journal-creations-machines-v1.jsonl` : `fab0ad9603532be4f4524c51368e3826b6ee22ea77bb4af2ce3d4db791efaa3c` ;
  - `minuterie-d1a-fae70647f54e-journal-v1.jsonl` : `0d4c361cecacbd1e0642830070360fdf26f5a981bab52f33b3e8b6459cc2cf7c` ;
  - `minuterie-d1a-fae70647f54e-pid-v1.txt` : `d8e9f8760c071eb257c8661825ebde198bb6b1ec0ef821eb48ee6bfc664c604b` ;
  - `minuterie-d1a-fae70647f54e-sortie-v1.log` : vide (`e3b0c442…`) au moment du commit ;
  - `sortie-creation-d1a-fae70647f54e-v1.log` : `6064028c62f7ce61ca9a2ddde4569ba7db7c89311ff097167fcb8e8fae1871ad`.

## Suite

Section 3 de la procédure, dans l'ordre :
1. adresse du serveur, puis contrôle de la clé d'hôte ;
2. pilote « avant », en arrière-plan ;
3. coupure du réseau et sa vérification ;
4. pilote « apres » ;
5. destruction par l'identifiant (section 5), sans attendre la lecture.

À chaque reprise de session, et au moins toutes les heures : `verifier-minuterie`. Prochain message : tout arrêt ou incident, sinon la fin (destruction, inventaires, accès supprimés, minuterie).
