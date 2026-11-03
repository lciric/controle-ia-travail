Tu es le lecteur neuf du verdict de l'**analyse principale de R1-R2** (sondes boîte blanche contre juges boîte noire sur les activations rejouées de P3, relance de R1 sur la table de tokenisation v3).

## Règles communes (règle R13 : verdict par un lecteur neuf)
Tu n'as écrit ni le texte scellé, ni le code, ni la fiche, ni la concordance de la lecture que tu juges. Rien ne t'est raconté du résultat : tu le lis toi-même dans les fichiers nommés, et seulement eux. Tu appliques la table gelée des critères du texte scellé, ligne par ligne, tu prononces la classe de chaque comparaison, et tu dis si l'issue mécanique écrite par le code la contredit. Symétrie (R4) : un résultat trop propre, positif ou négatif, déclenche le même audit (dis ce qui te semble trop propre et ce que tu as vérifié). Un nul se lit « non détecté à cette puissance », avec son intervalle. P-R5 se lit « observé à côté du prédit, sans verdict propre ». Aucune citation hors du dépôt sans Lazar. Français, sans sigle non développé ; toute heure vient de `date -u`. Dépôt : `/home/claude/controle-ia-travail`, branche `canal/conv-audit-n04` (lecture seule ; les arbres `/home/claude/controle-ia-analyse-principale-r1-r2-v1` et `/home/claude/controle-ia-analyse-bn-v3` sont les arbres d'analyse, lecture seule aussi). Vérifie chaque compagnon `.sha256` par `sha256sum -c` avant de lire un fichier.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien n'est ouvert sous `donnees/` (les tableaux d'activations ne se lisent pas ; les résultats JSON et Markdown, oui) ; aucun `git fetch`, `checkout`, `stash` ; aucun appel de réseau ni de modèle ; `nice -n 10 python3 -I -B` pour tout recalcul.

## Fichiers (chemins dans le dépôt, sauf mention)
- Texte scellé : `prereg/analyse-principale-r1-r2-v1.md` (`8e267952…`) et sa table des critères gelés (l. 140-167).
- Fiche JSON de l'analyse : `prereg/fiche-reception-principale-r1-r2-v1.json` (`09796067…`).
- Manifeste et sorties de la lecture décisive : `runs/20261103-072723-analyse-principale-r1-r2-v1/manifeste.json`, `diag/20261103-072723-analyse-principale-r1-r2-v1/analyse-principale-r1-r2-v1.json` et `.md`.
- Journal du lancement : `brouillons/preuves-mentors-v1/reception-r1-relance-v2/lancements-v1/lancement-20261103-072723-analyse-principale-r1-r2-v1.txt` ; journal d'écriture des fiches : `brouillons/preuves-mentors-v1/reception-r1-relance-v2/lancements-v1/fiches-20261103-063222-r1-rejeu-reel.txt`.
- L'addendum v3 scellé qui gouverne la course rejouée : `prereg/R1-addendum-relance-v3.md` au commit `139a81d3` (`git show 139a81d3:prereg/R1-addendum-relance-v3.md`, `88e262e2…`) ; le rapport de concordance sur la version scellée : `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/verification-differences-r1-v3-et-complement-v1.md` (`43dbf789…`, partie A).
- La fiche de réception : `brouillons/preuves-mentors-v1/reception-r1-relance-v2/fiche-reception-r1-relance-v3-v1.md` (`47e4b6ac…`).
- Le résultat du fournisseur cité par la fiche : `diag/20261103-063222-r1-rejeu-reel/rejeu-activations.json` et `runs/20261103-063222-r1-rejeu-reel/manifeste.json` (dans l'arbre de la principale ou le dépôt fusionné).
- La réserve sur HG-2 : addendum v3, « Hypothèse » et la ligne ajoutée des critères gelés ; verdict du rejeu à graine `brouillons/preuves-mentors-v1/reception-rejeu-graine-v1/verdict-rejeu-graine-v1.md` (`64fab1a5…`) : à rapporter à côté, sans changer aucune classe.
- `registres/decisions.md` : entrées de gel et de réception (R-1101, R-1304, R-1308, R-1315, R-1319).

## Points particuliers
- « N-A sans objet » (E19 de l'addendum v3 ; concordance `8482b4cd…` § 7) : aucun épisode non résolu attendu ; vérifie que `tokenisation.episodes_non_resolus` du résultat du fournisseur est vide (garde `comptes` de `redaction.controles` de la fiche ; attendu `[]`).
- P-R5 : rapporte la valeur observée à côté de la prédiction de l'addendum v3, sans verdict propre ; dis si la conséquence déclarée (« Prédiction », n° 343 : P-R5 contraire ⇔ plus de 10 % d'actions non fidèles) est engagée.
- Aucune reprise E21 n'a eu lieu.

## Rendu
Rapport `/home/claude/scratch/verdict-r13-principale/verdict-R13-analyse-principale-r1-r2-v1.md` : (1) fichiers lus et empreintes vérifiées ; (2) la table des critères, ligne par ligne : critère, valeur lue (chemin et clé), classe prononcée ; (3) l'issue mécanique du code et si elle contredit tes classes ; (4) audit de symétrie ; (5) P-R5 et la réserve HG-2 à côté ; (6) **verdict en trois lignes**, puis nœuds ouverts pour Lazar s'il y en a. Réponse finale : le verdict, les classes, le chemin et le sha256 du rapport.
