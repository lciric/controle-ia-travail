Tu es le **lecteur A** (normalisation et dédoublonnage) du rapport des idées sur la question de Shi Feng et Eyon Jang, pour la candidature de Lazar Ciric. Tu n'as écrit aucune des idées ni aucun des textes. Français, sans sigle non développé ; toute heure vient de `date -u`. Échéance du dépôt ce soir : **vise 25 minutes**, et écris `fiches-normalisees-v1.json` dans les quinze premières minutes.

## Ton protocole (gelé avant toute sortie : lis-le d'abord, en entier)
`/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/protocole-rapport-mentors-soir-v1.md` (sha256 `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`) : tu fais **l'étape A** pour ce seul mentor. Pour le détail du format, la section 2 de `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md`.

## La question des mentors (texte exact)
> What are your thoughts on the value of white-box monitors and white-box methods for auditing? What do you see as their current limitations?

Question servie à la course : `/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/question-course-jang-feng-v1.md` (sha256 `d68c6c5ca567c2a867c9a0eb0e64d7b7340af0414e0f382c19416d67ab63c10e`) ; pièces de référence pour le rattachement : `/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-jang-feng-v1.md` (sha256 `1f42364322988bf591ead6ce41842dd389ab179b11bc27853d66750ab5196774`) et `/home/claude/controle-ia-travail/brouillons/ideation-kirchner-q2-v1/piece-nos-resultats-v1.md` (sha256 `d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c`).

## Entrée unique
**La course de l'organisme** (copie vérifiée à l'octet, paquet sans provenance) : `/home/claude/scratch/soir-rapport/jang-feng/source-2/source-2-course-jang-feng-v1.json` (sha256 `2cda37df8e21097b0604fdc2f20da063247e5b973648e9c077f9f491236951d0`) : 31 éléments `S2-01` à `S2-31` (fiches de toutes les passes et fusions du bisociateur, dont deux inachevées), chacun avec titre, axe, hypothèse, prédiction, épreuve, contrôle, test de mort, coût. Lis-les tous en entier. Il n'y a ni tour ni fiche du matin pour ce mentor.

## Règles de lecture
- Une idée = une hypothèse et sa mesure qui tue. Les fusions qui reprennent une proposition se fondent avec elle si l'hypothèse et la mesure qui tue sont les mêmes ; dis-le.
- **Pas de consensus** : une idée reste gardée tant qu'aucune source citée ne la réfute. Réfutée seulement si une source citée contredit son énoncé central, ou si elle se contredit elle-même.
- Une idée **répond** si elle dit une valeur ou une limite des moniteurs ou des méthodes boîte blanche pour l'audit, avec l'expérience ou la mesure qui la montrerait ; s'il manque la mesure, elle est gardée et le manque est écrit.

## Ce que tu écris (dossier `/home/claude/scratch/soir-rapport/jang-feng/lecteur-A/`, fichiers neufs)
1. `fiches-normalisees-v1.json` : une liste de fiches, **identifiants opaques** (`J-001`, `J-002`, … dans un ordre sans lien avec la source), **aucune provenance** (ni numéro `S2-xx`, ni nom de modèle, ni nom de fichier) : `id`, `classement` (« J » si elle répond à la question ou touche ce que font ces mentors, « hors sujet » sinon), `type`, `enonce` (une phrase falsifiable), `mecanisme`, `ce_qu_on_entraine_ou_mesure`, `resultat_attendu` (avec signe), `ce_qui_rendrait_le_resultat_trompeur`, `mesure_qui_tue`, `echec_le_plus_probable`, `rattachement_piece` (« neuve » / « prolonge la pièce, point n » / « déjà dans une pièce »), `cout`, `outil_du_mentor`, `appuis_lazar` (résultats publics de Lazar qui l'appuient, d'après la seconde pièce), `objections` (sourcées ou non), `reponses`.
2. **Dédoublonnage par structure** : même hypothèse et même mesure qui tue = une fiche.
3. `refutees-v1.md` (chaque réfutation avec sa preuve) et `hors-sujet-v1.md`.
4. La clé, à part : `cle-provenances-v1.json` (identifiant → liste des éléments `S2-xx` fondus dans la fiche).

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier du dépôt modifié ; rien sous `donnees/` ; aucun `git` ; aucun appel de modèle autre que toi ; `WebFetch` seulement pour vérifier une source qu'une fiche cite. N'ouvre rien sous `/home/claude/coffre-*`, ni les dossiers `pour-lazar/`, ni la réponse de Lazar à cette question. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.

## Rendu
Réponse finale : nombre d'éléments lus, de fiches après dédoublonnage (dans le sujet et hors sujet), de réfutées ; chemins et sha256 de tes fichiers.
