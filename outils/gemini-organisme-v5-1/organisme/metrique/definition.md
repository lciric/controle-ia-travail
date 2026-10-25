# Définition de la métrique d'évaluation externe (`organisme/metrique/`)

Cette métrique évalue de manière purement objective les fichiers produits dans le `dossier_sorties` d'un autre organisme (sans aucun appel réseau et sans auto-notation).

## Ce que mesure `calculer(dossier_sorties) -> float`

La note finale est un nombre flottant compris dans `[0.0, 1.0]` combinant trois critères vérifiables sur `reponses_test.json` :

1. **Régularité structurelle et couverture ($40\%$)** :
   - Vérifie que `reponses_test.json` existe, est un objet JSON lisible et non vide, et que chaque entrée contient une étiquette non vide (`str`) et une probabilité de confiance numérique appartenant à `[0.0, 1.0]`.
2. **Discrimination informationnelle des confiances ($30\%$)** :
   - Un organisme qui renvoie une confiance constante (par exemple `0.5` ou `1.0` partout par valeur par défaut) n'exerce aucune calibration d'incertitude.
   - La métrique mesure l'écart-type empirique des confiances déclarées $\sigma_q$ et attribue un score nul si toutes les confiances sont figées sur une constante unique (pour $N \ge 2$ tâches), ou maximal lorsque les confiances différencient les cas ambigus des cas certains ($\sigma_q \approx 0.15$).
3. **Tempérance épistémique aux bords sous potentiel de Tsallis $\alpha = 4/3$ ($30\%$)** :
   - Pénalise les confiances dégénérées écrasées sur `{0.0, 1.0}` qui font diverger les règles de score logarithmiques en cas d'erreur sur tâche adversariale.