Tu es le **lecteur A, suite** (normalisation et dédoublonnage) du rapport des idées sur la question 1 de Lujain Ibrahim, pour la candidature de Lazar Ciric à Pivotal. Deux lecteurs A ont déjà traité le tour d'un collisionneur, les fiches du matin et une première course de l'organisme ; tu prends leur suite pour la **seconde course de l'organisme** (source 3) seule, avec leurs règles et leur format, sur leurs fichiers. Tu n'as écrit aucune des idées ni aucun des textes. Français, sans sigle non développé ; toute heure vient de `date -u`. Échéance du dépôt ce soir : **vise 25 minutes**, et écris `fiches-normalisees-v3.json` dans les quinze premières minutes.

## Ton protocole (gelé avant toute sortie : lis-le d'abord)
- `/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/protocole-rapport-mentors-soir-v1.md` (sha256 `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`) : tu fais **l'étape A** sur la source 3.
- La consigne du premier lecteur A, pour le format exact des fiches et les règles : `/home/claude/controle-ia-travail/brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/soir-lecteur-A-ibrahim-q1-v1.md`. Ce qui y est dit des cellules du tour, des espèces et des fiches du matin ne vaut pas pour la source 3.
- La question de la mentore (texte exact) : « Pick one of the two projects and briefly describe the first experiment you'd run. Try to include information on what you'd train or measure, what result you'd expect, and one thing that could make the result misleading. » ; pièce de référence pour le rattachement : `/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-ibrahim-v1.md`.

## Ce qui existe déjà (lis-le en entier avant la source 3)
Dossier `/home/claude/scratch/soir-rapport/ibrahim-q1/lecteur-A/` : `fiches-normalisees-v2.json` (19 fiches, sha256 `a10781d90ddceb7bc8c5f8ed92a18722047206c859b1b48474857ec7b5276286`), `refutees-v2.md` (`0315cb17…`), `hors-sujet-v2.md` (`d47b7180…`). Tu ne modifies aucun de ces fichiers. N'ouvre aucun fichier `cle-provenances-*`.

## Source 3 (préparée par le directeur, sans provenance)
`/home/claude/scratch/soir-rapport/ibrahim-q1/source-3/source-3-course-ibrahim-v1.json` (sha256 `4a2ffc1bc9d05ad20135efdf863125336edc6abaced07bf7c50898b603e29444`) : 38 éléments `S3-01`, `S3-02`, …, chacun avec son `contenu` (titre, axe, hypothèse, prédiction, épreuve, contrôle, test de mort, coût) : les fiches de toutes les passes de tous les proposeurs et les fusions du bisociateur de la seconde course. Lis-les tous en entier.
- **Classement** : « I » si l'élément répond à la question (une première expérience sur l'un des deux projets de la mentore : ce qu'on entraîne ou mesure, le résultat attendu, une chose qui rendrait le résultat trompeur) ; sinon hors sujet.
- **Aucune objection croisée** dans cette source : `objections` et `reponses` restent vides, sauf pour une fiche fusionnée qui en avait déjà.
- **Dédoublonnage par structure**, contre les 19 fiches existantes et entre éléments : même hypothèse et même mesure qui tue = une seule fiche. Une fusion avec une fiche existante garde le texte de la fiche existante ; un champ vide de celle-ci peut être rempli par le texte de l'élément, cité tel quel, et c'est dit dans `note_du_lecteur`.
- **Réfutée** seulement si une source citée contredit son énoncé central, ou si l'élément se contredit lui-même ; jamais par accord ou désaccord de modèles. `WebFetch` seulement pour vérifier une telle source.

## Ce que tu écris (versions neuves ; on n'écrase jamais)
1. `/home/claude/scratch/soir-rapport/ibrahim-q1/lecteur-A/fiches-normalisees-v3.json` : les 19 fiches de la v2 (identiques, sauf les champs remplis par une fusion, dits dans `note_du_lecteur`) puis les fiches neuves, numérotées à la suite de la dernière de la v2, même format (mêmes clés), **aucune provenance**.
2. `refutees-v3.md` et `hors-sujet-v3.md` (même dossier) : ceux de la v2, plus ce que la source 3 ajoute.
3. La clé de la source 3 : `/home/claude/scratch/soir-rapport/ibrahim-q1/lecteur-A/cle-provenances-source-3-v1.json` : pour chaque fiche (neuve ou fusionnée) la liste de ses éléments `S3-xx`, et pour chaque élément son sort (fiche neuve, fusionné dans I-…, réfuté, hors sujet).

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git` ; aucun appel de modèle autre que toi. Ne lis rien sous `/home/claude/coffre-*`, ni les dossiers `pour-lazar/`, `classement-D/`, `moisson-C/`, `piste/`, `prep-v1/`, ni les dossiers `ibrahim-q1-ensemble*`, ni les réponses de Lazar. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.

## Rendu
Réponse finale : nombre d'éléments lus ; fiches neuves et fusions ; réfutés ; hors sujet ; total des fiches de la v3 ; chemins et sha256 de tes fichiers ; tout doute sur un dédoublonnage, en une ligne chacun.
