Tu es le **lecteur A, suite** (normalisation et dédoublonnage) du rapport des idées sur la question 2 (facultative) de Paul Colognese et Francis Rhys Ward, sur leur billet, pour la candidature de Lazar Ciric. Un premier lecteur A a traité le tour d'un collisionneur ; tu prends sa suite pour la **course de l'organisme** (source 2) seule, avec ses règles et son format, sur ses fichiers. Tu n'as écrit aucune des idées ni aucun des textes. Français, sans sigle non développé ; toute heure vient de `date -u`. Échéance du dépôt ce soir : **vise 25 minutes**, et écris `fiches-normalisees-v2.json` dans les quinze premières minutes.

## Ton protocole (gelé avant toute sortie : lis-le d'abord)
- `/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/protocole-rapport-mentors-soir-v1.md` (sha256 `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`) : tu fais **l'étape A** sur la source 2.
- La consigne du premier lecteur A, pour le format exact des fiches et les règles : `/home/claude/controle-ia-travail/brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/soir-lecteur-A-colognese-ward-q2-v1.md`. Ce qui y est dit des cellules du tour, des espèces et des fiches du matin ne vaut pas pour la source 2.
- La question des mentors (texte exact) : « (Optional) Read this post. Should we have done anything differently? What was the most interesting finding in your view and why? » ; pièce de référence pour le rattachement : `/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-colognese-ward-v1.md`.

## Ce qui existe déjà (le travail du premier lecteur A ; lis-le en entier avant la source 2)
Dossier `/home/claude/scratch/soir-rapport/colognese-ward-q2/lecteur-A/` : `fiches-normalisees-v1.json` (22 fiches `W-001` à `W-022`, sha256 `43f2ed8c058b9bfe891d44dd63d1c61991450d5b4ae4338df45d9ac5f1267649`), `refutees-v1.md` (`243dc528…`), `hors-sujet-v1.md` (`6dd49fe8…`). Tu ne modifies aucun de ces fichiers. N'ouvre pas `cle-provenances-v1.json`.

## Source 2 (préparée par le directeur, sans provenance)
`/home/claude/scratch/soir-rapport/colognese-ward-q2/source-2/source-2-course-colognese-ward-q2-v2.json` (sha256 `fce23e2701d307a1ef719f3a4a8194e15b3bd7cacd956340dfe9536e9011fe47`) : 31 éléments `S2-01` à `S2-31`, chacun avec son `contenu` (titre, axe, hypothèse, prédiction, épreuve, contrôle, test de mort, coût) : les fiches de toutes les passes de tous les proposeurs et les fusions du bisociateur de la course. Lis-les tous en entier.
- **Classement** : « W » si l'élément répond à la question (ce qu'il fallait faire autrement, avec la mesure ou l'expérience qui le montrerait ; ou la trouvaille la plus intéressante et pourquoi) ; sinon hors sujet.
- **Aucune objection croisée** dans cette source : `objections` et `reponses` restent vides, sauf pour une fiche fusionnée qui en avait déjà.
- **Dédoublonnage par structure**, contre les 22 fiches existantes et entre éléments : même hypothèse et même mesure qui tue = une seule fiche. Une fusion avec une fiche existante garde le texte de la fiche existante ; un champ vide de celle-ci peut être rempli par le texte de l'élément, cité tel quel, et c'est dit dans `note_du_lecteur`.
- **Réfutée** seulement si une source citée contredit son énoncé central, ou si l'élément se contredit lui-même ; jamais par accord ou désaccord de modèles. `WebFetch` seulement pour vérifier une telle source.

## Ce que tu écris (versions neuves ; on n'écrase jamais)
1. `/home/claude/scratch/soir-rapport/colognese-ward-q2/lecteur-A/fiches-normalisees-v2.json` : les 22 fiches de la v1 (identiques, sauf les champs remplis par une fusion, dits dans `note_du_lecteur`) puis les fiches neuves `W-023`, `W-024`, …, même format (mêmes clés), **aucune provenance**.
2. `refutees-v2.md` et `hors-sujet-v2.md` (même dossier) : ceux de la v1, plus ce que la source 2 ajoute.
3. La clé de la source 2 : `/home/claude/scratch/soir-rapport/colognese-ward-q2/lecteur-A/cle-provenances-source-2-v2.json` : pour chaque fiche (neuve ou fusionnée) la liste de ses éléments `S2-xx`, et pour chaque élément son sort (fiche neuve, fusionné dans W-…, réfuté, hors sujet).

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git` ; aucun appel de modèle autre que toi. Ne lis rien sous `/home/claude/coffre-*`, ni dans `/tmp/cw-course-v2/`, ni les dossiers `pour-lazar/`, `classement-D/`, `moisson-C/`, `piste/`, ni les réponses de Lazar. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.

## Rendu
Réponse finale : nombre d'éléments lus ; fiches neuves et fusions ; réfutés ; hors sujet ; total des fiches de la v2 ; chemins et sha256 de tes fichiers ; tout doute sur un dédoublonnage, en une ligne chacun.
