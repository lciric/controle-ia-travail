# Destruction des six disques arrêtés de la formation du barreau 5 — 2026-11-20

Pièce courte de la session de formation (`session_01QPDgKjCQYmTHUEjN63ThC8`).

Accords :
- GO-2026-11-20-51, option (a) de Lazar : inventaire de chaque disque, puis destruction par l'identifiant.
- Confirmation de la mère à 12:35Z : destruction hors de la sous-commande `detruire`, qui exige un inventaire final qu'aucune marche interrompue n'a écrit.
- Premier essai à 12:37Z, refusé par le contrôle de permissions de la session : rien n'a été joué.
- Mot de Lazar dans cette session à 13:20Z : « go ».

**Preuve tenant lieu de versement.** L'inventaire de chaque disque a été versé, scellé et poussé sur la branche de sortie de son instance, sous `traces-b5f/disque-arrete/`. Il a été fait par les seules commandes `ls` et `du` du loueur : noms et tailles, rien lu. Les quatre fichiers écrits par chaque marche y figurent à la même taille sur la branche. Seules les traces de l'amorce (≈ 10 Ko) n'ont pu être extraites.

| n | identifiant | commit de l'inventaire (branche `donnees/barreau5-familles-jumelles-v1-formation-instance-<n>`) | destruction (UTC) |
|---|---|---|---|
| 7 | 61625133 | 60fd7cb63d8036add1ce62e22a2b9b6681fceca2 | 13:20:40 |
| 5 | 61625067 | 9973a24449d821473cf2fb250acf44bef9555e41 | 13:20:49 |
| 4 | 61624946 | 80db2de90f1b9fcd3c3224a7c6f86bfc5e7fb41f | 13:20:59 |
| 1 | 61624757 | cb2589e40a9512efffdb852997160cd20e663986 | 13:21:08 |
| 2 | 61624840 | 4478011eaead3c66d18c33bdcad26d0ed20249c8 | 13:21:18 |
| 3 | 61624896 | 1d5b183ba661edacde9c92b0a18e6904203c9856 | 13:21:28 |

Pour chaque instance, dans cet ordre :
1. contrôle, sur une liste neuve du loueur, de l'identifiant, de l'étiquette `b5f-formation-v1-<n>` et de l'état « stopped » ;
2. joueur d'une seule ligne, « GO_ID=GO-2026-11-19-86 vastai destroy instance <ID> -y », garde de calcul vérifiée sur son texte ;
3. `verifier-destruction` du lanceur (commit de course 31fca83b, témoin 60988826) : « absence de l'instance <ID> prouvée », pour les six.

Restent au compte, non touchées : 58936096, 58936099, 58936100 (intouchables) et 60988826 (témoin), toutes « stopped ».
