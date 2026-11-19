# Erratum 1 — notice du développeur habilité, lots 13 et 15 (v1)

Corrige `docs/notes/bras-a-moniteurs-v1/notice-developpeur-habilite-lots-13-et-15-v1.md` (`5024a77f1e49435f0bb3556cf6d5b9e6a37aeaafd5b87ee894e3bc83e33d089b`), qui reste telle quelle. Cet erratum prime sur les quatre passages ci-dessous. Source : contre-lecture `docs/notes/bras-a-moniteurs-v1/contre-lecture-lots-13-et-15-bras-a-v1.md` (`73d4c58e…`), partie 5 et partie 2. Écrit le 19 novembre 2026 par le développeur habilité côté moniteurs.

1. **« En bref », quatrième point.**
   Avant : « Quatre points demandent une décision d'écriture du texte ou du lanceur (partie 4). »
   Après : « Cinq points demandent une décision d'écriture du texte ou du lanceur (partie 4). »

2. **Partie 2, « Ce qui est établi », point 3.**
   Avant : « les seuls jetons qui commencent par un chiffre sont les dix jetons d'un seul chiffre ; aucun autre jeton ne contient de chiffre. »
   Après : « les seuls jetons qui commencent par un chiffre sont les dix jetons d'un seul chiffre ; aucun autre jeton ne contient de chiffre ASCII (douze jetons portent un chiffre d'une autre écriture : ils ne s'écrivent dans aucune valeur et comptent comme « non-chiffre »). »

3. **Partie 2, « Normalisation ».**
   Avant : « Le code du lot 14 l'exigera du message. »
   Après : « Le code du lot 14 compte et rapporte, par moniteur et par condition, les messages qui ne sont pas en forme composée ; il n'arrête pas la lecture (un arrêt dépendrait du texte de l'agent). » C'est ce que fait le module du lot 14, et ce que la mère a retenu.

4. **Témoin bénin (partie 3 et « En bref »).** La notice dit de l'extraction « jamais le témoin bénin ». À lire : le témoin bénin n'est **jamais écrit** ; ses épisodes sont exigés présents et **comptés**. Quand l'entrée est un fichier, ses lignes sont analysées comme les autres et tenues en mémoire le temps de l'extraction, jamais copiées ni imprimées. « Ne lit jamais » serait faux.

**Décisions de la mère reprises ici** (messages du 19 novembre) : la ligne `CONFIG-BRAS-A-V2` désigne la configuration à six clés écrite par l'extraction après le rejeu ; la configuration du lanceur, scellée avant dépense, s'inscrit sous `CONFIG-LANCEUR-BRAS-A-V2` ; un message non normalisé est compté, il n'arrête pas la lecture.

**Version 2 du code.** Les deux modules et leurs essais sont livrés en version 2 sous des noms neufs (notice `notice-developpeur-habilite-lots-13-et-15-v2.md`) ; la version 1 reste intacte.
