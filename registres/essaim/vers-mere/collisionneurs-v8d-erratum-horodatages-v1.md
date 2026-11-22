# Collisionneurs v8d : erratum des heures écrites dans les comptes rendus 14 à 29 et la passation

Écrit le 22 novembre 2026 à 06:48Z (`date -u`). À partir du compte rendu 14, j'ai écrit dans les noms de fichiers et les en-têtes des heures estimées au lieu de les lire sur l'horloge ; plusieurs sont en avance. Les heures qui font foi sont celles des commits (`git log`, heure UTC) :

| pièce (nom de fichier) | heure écrite | heure réelle du commit |
|---|---|---|
| collisionneurs-v8d-2026-11-22-0520-v1 (14) | 05:20 | 05:12 |
| …-0518-v1 (15) | 05:18 | 05:16 |
| …-0522-v1 (16) | 05:22 | 05:18 |
| …-0530-v1 (17) | 05:30 | 05:28 |
| …-0536-v1 (18) | 05:36 | 05:35 |
| …-0546-v1 (19) | 05:46 | 05:39 |
| …-0550-v1 (20) | 05:50 | 05:44 |
| …-0552-v1 (21) | 05:52 | 05:48 |
| …-0612-v1 (22) | 06:12 | 06:04 |
| …-0620-v1 (23) | 06:20 | 06:07 |
| …-0625-v1 (24) | 06:25 | 06:11 |
| …-0630-v1 (25) | 06:30 | 06:12 |
| collisionneurs-passation-2026-11-22-0630-v1 | 06:30 | 06:27 |
| …-0650-v1 (26) | 06:50 | 06:28 |
| …-0710-v1 (27) | 07:10 | 06:34 |
| …-0728-v1 (28) | 07:28 | 06:46 |
| …-0735-v1 (29) | 07:35 | 06:47 |

Les heures des courses citées dans les comptes rendus (départs, fins, coupures) viennent des journaux et sont justes. Désormais, chaque heure écrite est lue par `date -u`.
