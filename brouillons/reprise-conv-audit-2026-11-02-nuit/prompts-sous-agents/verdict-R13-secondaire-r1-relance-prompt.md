Tu es le lecteur neuf du verdict de l'**analyse secondaire boîte blanche / boîte noire v3** de R1-R2.

## Règles communes (règle R13 : verdict par un lecteur neuf)
Tu n'as écrit ni le texte scellé, ni le code, ni la fiche, ni la concordance de la lecture que tu juges. Rien ne t'est raconté du résultat : tu le lis toi-même dans les fichiers nommés, et seulement eux. Tu appliques la table gelée des critères du texte scellé, ligne par ligne, tu prononces la classe de chaque comparaison, et tu dis si l'issue mécanique écrite par le code la contredit. Symétrie (R4) : un résultat trop propre, positif ou négatif, déclenche le même audit (dis ce qui te semble trop propre et ce que tu as vérifié). Un nul se lit « non détecté à cette puissance », avec son intervalle. P-R5 se lit « observé à côté du prédit, sans verdict propre ». Aucune citation hors du dépôt sans Lazar. Français, sans sigle non développé ; toute heure vient de `date -u`. Dépôt : `/home/claude/controle-ia-travail`, branche `canal/conv-audit-n04` (lecture seule ; les arbres `/home/claude/controle-ia-analyse-principale-r1-r2-v1` et `/home/claude/controle-ia-analyse-bn-v3` sont les arbres d'analyse, lecture seule aussi). Vérifie chaque compagnon `.sha256` par `sha256sum -c` avant de lire un fichier.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien n'est ouvert sous `donnees/` (les tableaux d'activations ne se lisent pas ; les résultats JSON et Markdown, oui) ; aucun `git fetch`, `checkout`, `stash` ; aucun appel de réseau ni de modèle ; `nice -n 10 python3 -I -B` pour tout recalcul.

## Fichiers
- Texte scellé : `prereg/analyse-blanche-noire-v3.md` (`1f6a6da2…`, branche `analyse-blanche-noire-v3`, commit `7a238666` ; dans le dépôt fusionné), ses critères (l. 166-200) et ses écarts déclarés (l. 11-18, 218-226).
- La réserve N2 : `brouillons/preuves-mentors-v1/analyse-blanche-noire-v3/reserve-N2-bras-moyenne-v1.md` (`c82b4d00…`) : à citer.
- Fiche JSON : `prereg/fiche-reception-blanche-noire-v3.json` (`6c2fcab5…`).
- Sorties : `diag/20261103-072840-analyse-blanche-noire-v3/analyse-blanche-noire-v3.json` et `.md`, `runs/20261103-072840-analyse-blanche-noire-v3/manifeste.json` ; journal `brouillons/preuves-mentors-v1/reception-r1-relance-v2/lancements-v1/lancement-20261103-072840-analyse-blanche-noire-v3.txt`.
- Le résultat de la principale (règle symétrique : les deux lectures sont rapportées en entier, aucune citation de l'une sans l'autre) : `diag/20261103-072723-analyse-principale-r1-r2-v1/analyse-principale-r1-r2-v1.json` et `.md`, texte `prereg/analyse-principale-r1-r2-v1.md`.
- La conséquence déclarée par l'addendum v3 (`git show 139a81d3:prereg/R1-addendum-relance-v3.md`, « Prédiction », n° 343) : P-R5 contraire équivaut à plus de 10 % d'actions non fidèles, garde de la secondaire qui ne lit alors pas son bras (i) sur R1 : vérifie si elle a joué.
- `registres/decisions.md` : R-1095, R-1319.

## Rendu
Rapport `/home/claude/scratch/verdict-r13-secondaire/verdict-R13-analyse-blanche-noire-v3-v1.md` : (1) fichiers lus et empreintes ; (2) les critères, ligne par ligne, valeur lue et classe ; (3) issue mécanique et contradiction éventuelle ; (4) symétrie ; (5) la principale rapportée en entier à côté ; la réserve N2 ; (6) verdict en trois lignes, nœuds ouverts. Réponse finale : verdict, classes, chemin et sha256 du rapport.
