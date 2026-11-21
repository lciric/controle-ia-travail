# Décision de routine : journaux et plafonds des trois relectures par Fable — 21 novembre 2026

- Cadre : mot de Lazar GO-2026-11-21-84 (relecture par Fable 5.2 à travers l'API) ; plafonds donnés par la mère : 6 USD par relecture, 18 USD pour les trois lots.
- Constat du préparateur : avec un seul journal, l'outil cumule les dépenses du journal avant chaque envoi. Une fois la première relecture payée, les suivantes seraient refusées. Le pire cas de la relecture des dommages par un tiers (environ 180 000 jetons d'entrée à 8 USD par million, et 128 000 jetons de sortie à 40 USD par million) dépasse aussi 6 USD.
- Décision : un journal de dépense par lot, `journal-depense-relecture-<lot>-v1.jsonl`, chacun plafonné à 6 USD. Le total ne peut donc pas dépasser 18 USD. Pour les dommages par un tiers, la sortie est plafonnée à 96 000 jetons : 3,84 USD, plus environ 1,44 USD d'entrée, soit environ 5,3 USD au pire. Les deux autres lots gardent 128 000 jetons : environ 5,6 USD au pire chacun.
- Envoi après la contre-lecture du nettoyeur par un autre modèle. Le lot des tâches floues part après son erratum 2.
- Ajout : le lot des tâches floues fait environ 140 000 jetons d'entrée, soit environ 1,1 USD. Sa sortie est plafonnée à 96 000 jetons, soit environ 5 USD au pire. Il part après les deux autres lots.
