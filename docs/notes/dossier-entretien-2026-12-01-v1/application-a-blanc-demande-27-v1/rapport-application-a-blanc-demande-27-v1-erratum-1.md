# Erratum 1 au rapport d'application à blanc de la demande 27 (v1)

Ce texte suit la contre-lecture par Sonnet 5.5 (`contre-lecture-application-a-blanc-v1-sonnet.md`, `96c1e138…`), dont le verdict est « conforme sous corrections ». Le programme et les quatre sorties sont confirmés à l'octet par un découpeur indépendant. Cet erratum prime sur le rapport v1, qui n'est pas réécrit.

1. **Corrections jumelles non appliquées par le programme.** Quatre entrées disent « même correction pour … ». Le programme ne les applique pas. Restent dans les sorties :
   - la question Q1 de la réponse 4 (entrée E4-1, ligne 80) ;
   - « point de bascule (m ou m divisé par le taux d'audit) » dans la réponse 4 (entrée E4-4, ligne 157) ;
   - l'étiquette « **Thèse** : la loi héritée. » devant le texte neuf, dans la réponse 8 (entrée E8-3, ligne 173) ;
   - la ligne de table « A, lemme d'additivité, reste » de la note des problématiques (entrée EN-4).
2. **Le renvoi n° 10 du rapport v1 est remplacé.** Il disait que la lettre de la table diffère. C'est faux : la table contient mot pour mot « revendication resserrée, à démontrer (erratum 3 v2) ». C'est une correction jumelle non appliquée (point 1).
3. **Renvois de moindre portée, ajoutés :**
   - dans la note, « candidate, rang 2 » reste, alors que l'entrée EN-6 ne corrige que « rang 1 » ;
   - dans la réponse 4, lignes 98, 100 et 194, « lemme … 0,75 » et « simulation du lemme » restent (pièce d'archive : à corriger ou à classer comme telle).
4. **Les renvois n° 3 et n° 4 se recoupent.** Ils portent sur l'hypothèse (a) « δ > 0 » et l'hypothèse empirique pivot. On les lit comme un seul.
5. **Le programme v2 ajoute trois gardes.** Elles vérifient que le total est de 43 blocs, que chaque identifiant est unique et que l'ANCIEN est absent après remplacement. Fichier : `appliquer_erratum_demande_27_v2.py`. Ses sorties sont identiques à l'octet à celles de la v1.
