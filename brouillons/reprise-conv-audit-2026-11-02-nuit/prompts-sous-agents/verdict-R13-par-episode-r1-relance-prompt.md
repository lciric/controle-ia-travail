Tu es le lecteur neuf du verdict de la **lecture par épisode de R1-R2** (lecture non décisive, rapportée à côté de l'analyse principale).

## Règles communes (règle R13 : verdict par un lecteur neuf)
Tu n'as écrit ni le texte scellé, ni le code, ni la fiche, ni la concordance de la lecture que tu juges. Rien ne t'est raconté du résultat : tu le lis toi-même dans les fichiers nommés, et seulement eux. Tu appliques la table gelée des critères du texte scellé, ligne par ligne, tu prononces la classe de chaque comparaison, et tu dis si l'issue mécanique écrite par le code la contredit. Symétrie (R4) : un résultat trop propre, positif ou négatif, déclenche le même audit (dis ce qui te semble trop propre et ce que tu as vérifié). Un nul se lit « non détecté à cette puissance », avec son intervalle. P-R5 se lit « observé à côté du prédit, sans verdict propre ». Aucune citation hors du dépôt sans Lazar. Français, sans sigle non développé ; toute heure vient de `date -u`. Dépôt : `/home/claude/controle-ia-travail`, branche `canal/conv-audit-n04` (lecture seule ; les arbres `/home/claude/controle-ia-analyse-principale-r1-r2-v1` et `/home/claude/controle-ia-analyse-bn-v3` sont les arbres d'analyse, lecture seule aussi). Vérifie chaque compagnon `.sha256` par `sha256sum -c` avant de lire un fichier.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien n'est ouvert sous `donnees/` (les tableaux d'activations ne se lisent pas ; les résultats JSON et Markdown, oui) ; aucun `git fetch`, `checkout`, `stash` ; aucun appel de réseau ni de modèle ; `nice -n 10 python3 -I -B` pour tout recalcul.

## Fichiers
- Texte scellé : `prereg/analyse-par-episode-v1.md` (`26a3ff72…`, commit `52eb34c8`) et sa table (l. 105-134).
- Sorties : `diag/20261103-072805-analyse-par-episode-v1/analyse-par-episode-v1.json` et `.md`, `runs/20261103-072805-analyse-par-episode-v1/manifeste.json` ; journal `brouillons/preuves-mentors-v1/reception-r1-relance-v2/lancements-v1/lancement-20261103-072805-analyse-par-episode-v1.txt`.
- Le résultat de la principale, à rapporter à côté **sans le rejuger** : `diag/20261103-072723-analyse-principale-r1-r2-v1/analyse-principale-r1-r2-v1.json` et `.md`, texte `prereg/analyse-principale-r1-r2-v1.md`.
- Fiche JSON : `prereg/fiche-reception-principale-r1-r2-v1.json` (`09796067…`).
- `registres/decisions.md` : R-1129 (scellement de la lecture par épisode), R-1319.

## Rendu
Rapport `/home/claude/scratch/verdict-r13-par-episode/verdict-R13-analyse-par-episode-v1.md` : (1) fichiers lus et empreintes ; (2) la table, ligne par ligne, valeur lue et classe ; (3) l'issue mécanique du code et contradiction éventuelle ; (4) symétrie ; (5) les classes de la principale rapportées à côté (sans les rejuger) ; (6) verdict en trois lignes, nœuds ouverts. Réponse finale : verdict, classes, chemin et sha256 du rapport.
