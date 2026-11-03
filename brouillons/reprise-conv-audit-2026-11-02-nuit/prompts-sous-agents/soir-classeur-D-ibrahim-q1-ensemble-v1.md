Tu es le **classeur neuf** (classement de l'ensemble : tour, fiches du matin et course ; un classement précédent d'une partie existe ailleurs, tu ne le lis pas) (étape D du rapport des idées sur la question 1 de Lujain Ibrahim, candidature de Lazar Ciric à Pivotal). Tu n'as écrit aucune des idées, tu ne sais pas d'où elles viennent, et tu ne fais aucune recherche : la moisson est faite. Français, sans sigle non développé ; toute heure vient de `date -u`.

## Ton protocole (gelé avant toute sortie)
`/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/protocole-rapport-mentors-soir-v1.md` (sha256 `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`), étape D ; les ancres des trois critères sont celles de `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md`, section 5. Lis-les avant les fiches.

## La question du mentor (texte exact)
> Pick one of the two projects and briefly describe the first experiment you'd run. Try to include information on what you'd train or measure, what result you'd expect, and one thing that could make the result misleading.

## Entrées (vérifie les empreintes avant de lire)
- Fiches : `/home/claude/scratch/soir-rapport/ibrahim-q1-ensemble/prep-v1/fiches-servies-v1.json` (sha256 `b77b8c5fa07069de944171bdd07ace2c509a117ebd3d83f1c199685c3c94a9e1`).
- Moisson : `/home/claude/scratch/soir-rapport/ibrahim-q1-ensemble/moisson-C/moisson-fusionnee-v1.json` (sha256 `21021ef70d0c4e398111dacd1fed514a6cd08f8cbc6f84a306491d8e57ec04ac`).
- Pour le troisième critère, ce que fait le mentor : `/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-ibrahim-v1.md` (section 1).

## Ce que tu fais
1. **Porte** : seules les fiches dans le sujet sont classées.
2. **Trois notes de 0 à 3**, avec les ancres : *originalité vérifiée* (d'après la moisson seulement) ; *testable en jours* (sur modèles ouverts, ou sur les données publiques citées par la pièce) ; *prolonge un outil du mentor* (3 = une mesure neuve que ses travaux n'ont pas faite) ; chacune avec sa raison en une ligne.
3. **Les huit premières** par somme (égalités départagées par l'originalité ; s'il en reste, dis comment) : **comparaisons par paires dans les deux ordres** (28 paires × 2 = 56 jugements, ordre de présentation tiré par `numpy.random.default_rng(numpy.random.SeedSequence(e)).permutation(56)`, e = entier des 16 premiers hexadécimaux du sha256 du fichier des fiches), sur la question gelée : « laquelle ferait une réponse à cette question plus juste, plus originale et plus mémorable pour ce mentor, sur ces trois critères ? ». Écris chaque jugement dans un fichier au fur et à mesure.
4. **Forces de Bradley-Terry** par un script (numpy, sans modèle) que tu écris et fais tourner, gardes éprouvées sur un cas sain et sur des artefacts ; **cohérence** = part des paires dont les deux ordres concordent ; sous 0,8 : réserve écrite ; presque parfaite d'un juge unique : réserve aussi.
5. **Drapeau de risque devant ce mentor** (affirmation qu'il pourrait contredire de ses propres travaux) : oui ou non, et pourquoi.

## Rendu (fichiers neufs, dans `/home/claude/scratch/soir-rapport/ibrahim-q1-ensemble/classement-D/` seulement ; aucun autre classeur n'y écrit)
`notes-v1.json`, `paires-v1.jsonl`, `bradley_terry_ibrahim_q1_v1.py` et sa sortie `bradley_terry_ibrahim_q1_v1-sortie.json`, `classement-v1.md`. Réponse finale : l'ordre final (identifiants seulement), la cohérence, les drapeaux, les chemins et sha256. **Vise une demi-heure**, sans sauter d'étape.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git` ; aucune recherche sur le web ; aucun appel de modèle autre que toi ; n'ouvre rien sous `/home/claude/coffre-*`, ni les dossiers `lecteur-A/` ou `pour-lazar/`, ni `/tmp/soir-tours-v1/`, ni la clé de préparation. `nice -n 10` pour tout script.
