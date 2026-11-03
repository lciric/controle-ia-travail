Tu es le **lecteur A, suite** (normalisation et dédoublonnage) du rapport des idées sur la question de Jérémy Scheurer (tendance d'échelle d'un comportement désaligné), pour la candidature de Lazar Ciric à Pivotal. Un premier lecteur A a traité le tour d'un collisionneur et les fiches du matin ; tu prends sa suite pour la **course de l'organisme** (source 2) seule, avec ses règles et son format, sur ses fichiers. Tu n'as écrit aucune des idées ni aucun des textes. Français, sans sigle non développé ; toute heure vient de `date -u`. Échéance du dépôt ce soir : **vise 25 minutes**, et écris `fiches-normalisees-v2.json` dans les quinze premières minutes.

## Ton protocole (gelé avant toute sortie : lis-le d'abord)
- `/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/protocole-rapport-mentors-soir-v1.md` (sha256 `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`) : tu fais **l'étape A** sur la source 2.
- La consigne du premier lecteur A, pour le format exact des fiches et les règles : `/home/claude/controle-ia-travail/brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/soir-lecteur-A-scheurer-v1.md`. Ce qui y est dit des cellules du tour, des espèces et des fiches du matin ne vaut pas pour la source 2.
- La question du mentor (texte exact, coupé comme dans la pièce) : « Your task is to come up with a research proposal which describes how we could get a scaling trend for misaligned behaviors such as scheming, deception, misalignment, swarm misalignment, control, or monitoring. [...] We want to roughly be able to make a statement such as: "AI's [bad propensity/capability"/"Our ability to monitor AIs via [insert control scheme] grows/declines roughly with a factor of X each month/year." [...] Try to design your approach such that it is likely to be successful. Go » ; pièce de référence pour le rattachement : `/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-scheurer-v1.md`.

## Ce qui existe déjà (le travail du premier lecteur A ; lis-le en entier avant la source 2)
Dossier `/home/claude/scratch/soir-rapport/scheurer/lecteur-A/` : `fiches-normalisees-v1.json` (10 fiches, sha256 `c101b3655e80cfead1bbdf43bf3cb2eae2effc4f8bbda078a3e6915c2b966728`), `refutees-v1.md` (`9e0d1927…`), `hors-sujet-v1.md` (`29cb01a6…`). Tu ne modifies aucun de ces fichiers. N'ouvre pas `cle-provenances-v1.json`.

## Source 2 (préparée par le directeur, sans provenance)
`/home/claude/scratch/soir-rapport/scheurer/source-2/source-2-course-scheurer-v1.json` (sha256 `ceb5bdfbe1bee2bd1b51c011eece5bc176ffa533b066a9107f46c8184ac34561`) : 23 éléments `S2-01`, `S2-02`, …, chacun avec son `contenu` (titre, axe, hypothèse, prédiction, épreuve, contrôle, test de mort, coût) : les fiches de toutes les passes de tous les proposeurs et les fusions du bisociateur de la course. Lis-les tous en entier.
- **Classement** : « S » si l'élément répond à la question (une proposition de recherche qui obtient une tendance d'échelle d'un comportement désaligné ou d'une capacité de contrôle, chiffrable en facteur par mois ou par an) ; sinon hors sujet.
- **Aucune objection croisée** dans cette source : `objections` et `reponses` restent vides, sauf pour une fiche fusionnée qui en avait déjà.
- **Dédoublonnage par structure**, contre les 10 fiches existantes et entre éléments : même hypothèse et même mesure qui tue = une seule fiche. Une fusion avec une fiche existante garde le texte de la fiche existante ; un champ vide de celle-ci peut être rempli par le texte de l'élément, cité tel quel, et c'est dit dans `note_du_lecteur`.
- **Réfutée** seulement si une source citée contredit son énoncé central, ou si l'élément se contredit lui-même ; jamais par accord ou désaccord de modèles. `WebFetch` seulement pour vérifier une telle source.
- **Règle d'intégrité** : une fiche ne garde aucun mode d'emploi d'attaque ; si un élément en contient, garde l'idée de mesure et retire le détail opératoire, et dis-le dans `note_du_lecteur`.

## Ce que tu écris (versions neuves ; on n'écrase jamais)
1. `/home/claude/scratch/soir-rapport/scheurer/lecteur-A/fiches-normalisees-v2.json` : les 10 fiches de la v1 (identiques, sauf les champs remplis par une fusion, dits dans `note_du_lecteur`) puis les fiches neuves, numérotées à la suite de la dernière de la v1, même format (mêmes clés), **aucune provenance**.
2. `refutees-v2.md` et `hors-sujet-v2.md` (même dossier) : ceux de la v1, plus ce que la source 2 ajoute.
3. La clé de la source 2 : `/home/claude/scratch/soir-rapport/scheurer/lecteur-A/cle-provenances-source-2-v1.json` : pour chaque fiche (neuve ou fusionnée) la liste de ses éléments `S2-xx`, et pour chaque élément son sort (fiche neuve, fusionné dans S-…, réfuté, hors sujet).

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git` ; aucun appel de modèle autre que toi. Ne lis rien sous `/home/claude/coffre-*`, ni les dossiers `pour-lazar/`, `classement-D/`, `moisson-C/`, `piste/`, `prep-v1/`, ni le dossier `scheurer-ensemble/`, ni les réponses de Lazar. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.

## Rendu
Réponse finale : nombre d'éléments lus ; fiches neuves et fusions ; réfutés ; hors sujet ; total des fiches de la v2 ; chemins et sha256 de tes fichiers ; tout doute sur un dédoublonnage, en une ligne chacun.
