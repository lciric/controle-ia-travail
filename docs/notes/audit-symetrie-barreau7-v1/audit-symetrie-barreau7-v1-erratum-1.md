# Erratum 1 du rapport d'audit de symétrie du septième barreau (v1)

- Corrige `docs/notes/audit-symetrie-barreau7-v1/audit-symetrie-barreau7-v1.md` (`5f55a6f56b19e2d90fcfcbfe7b55ff25e41c681496da8c690886c50413fbf400`), que la règle R12 interdit de réécrire. Même auditeur, 2026-11-19, vers 11:20 UTC. **Ce fichier porte des chiffres de mesure : la session mère ne l'ouvre pas.** Il prime sur les deux phrases visées ; la conclusion ne change pas.
- Source des chiffres : `constats-donnees.json` (`1d1be896ae34aa0c44ea86855064ca3e1c7c4ad37e4ba6052b669708ee175e1f`) du bloc-notes de l'auditeur.

1. **Section 4.1, premier paragraphe après le tableau.** Lire « le contexte des colludeurs, à la ligne finale, est plus long d'au moins 186 jetons que tout autre contexte de la ligne finale » (Llama-3.1-70B : 1 776 contre 1 590 ; Qwen3-32B : 1 819 contre 1 521, soit 298), et non « d'au moins 200 jetons ».
2. **Section 4.1, second point de la liste.** Lire « par agent, 6 % à 26 % des directions tirées au hasard atteignent une aire d'au moins 0,99 (quantile 0,95 du plancher de 0,994 à 1,0 dans le résultat pour la différence de moyennes, de 0,986 à 1,0 pour la famille linéaire ; mon tirage indépendant donne 0,991 à 1,0) », et non « 10 % à 26 % » ni « à 1,0 ». Les valeurs les plus basses sont aux couches 36 et 37 du Llama-3.1-70B.
