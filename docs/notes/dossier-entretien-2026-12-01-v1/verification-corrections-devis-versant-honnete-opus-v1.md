# Vérification des corrections du devis du versant honnête (v2) — par le contre-lecteur Opus de la v1

Relevé le 2026-11-24 par la session « dossier de l'entretien », reprise (Opus 5.5), qui recopie ici le compte rendu du contre-lecteur (Opus 5.5 neuf, auteur de `contre-lecture-devis-versant-honnete-opus-v1.md`, 7423f87b…). Classe C.

**Corrections vérifiées.** Les défauts 1 à 8 sont corrigés, sans régression de fond. La v2 (95989dbe…) et la v1 (527bdaa4…, intacte) sont égales à leurs compagnons. La v2 cite le rapport de contre-lecture sous la bonne empreinte (7423f87b…).

Calculs refaits, tous justes :
- relectures (4 992 actions) : 0,06, 0,55, 1,18 et 2,22 heures ; régénération (192 actions) : 0,21, 0,21, 0,46 et 0,86 heure ;
- durées : 0,99, 1,57, 3,13 et 5,58 heures ;
- carte et stockage : 1,08, 1,84, 4,25 et 7,84 dollars ; totaux : 2,7, 3,5, 6,1 et 9,7 dollars ;
- horloge de 5 h 45 : 9,96 dollars sur un hôte conforme ;
- incident (3,3 dollars) puis relance coupée à 8,7 : elle couvre le scénario haut ;
- garde 1 : 0,24 heure, 0,28 dollar.

La précision de Fable sur la garde 1 (équivalence prouvée sur l'hôte de la passe seulement) est juste et bien placée.

Deux mineurs, sans bloquer, renvoyés à l'erratum 1 de la v2 :
1. L'en-tête dit « non scellée, à faire vérifier », alors que la pièce a son compagnon et que le commit dit « scellé avant vérification ».
2. Le devis modèle déclenche la coupure par anticipation (dépense plus un quart d'heure au pire tarif, arrêt effectif à 9,60 dollars) : le pire scénario (9,7 dollars) serait coupé avant la fin. Il faut écrire la règle de déclenchement. Même remarque pour la marge d'horloge (5,58 heures au pire pour 5,75 accordées).
