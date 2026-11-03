Tu es le **lecteur A** (normalisation et dédoublonnage) du rapport des idées sur la question 1 de la mentore Lujain Ibrahim, pour la candidature de Lazar Ciric. Tu n'as écrit aucune des idées ni aucun des textes. Français, sans sigle non développé ; toute heure vient de `date -u`. Échéance du dépôt ce soir : **vise 35 minutes**.

## Ton protocole (gelé avant toute sortie : lis-le d'abord, en entier)
`/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/protocole-rapport-mentors-soir-v1.md` (sha256 `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`) : tu fais **l'étape A** pour ce seul mentor. Pour le détail du format, la section 2 de `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md`.

## La question du mentor (texte exact)
> Pick one of the two projects and briefly describe the first experiment you'd run. Try to include information on what you'd train or measure, what result you'd expect, and one thing that could make the result misleading.

Question servie au collisionneur : `/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/question-collisionneur-ibrahim-v1.md` ; pièces de référence pour le rattachement : `piece-ibrahim-v1.md` et `piece-sycophancie-publique-v1.md` (même dossier).

## Entrées
1. **Le tour du collisionneur** (copie vérifiée à l'octet, hors dépôt ; espèce C absente, déclarée) : `/tmp/soir-tours-v1/brouillons/canal-reprise-releve-v1/envois/session-depot/collisionneur-ibrahim-q1-sortie-v1/run-ibrahim-q1-e3-sans-argon-v1/cellules/` : `E3-T1-conception-{A,B,D,E}.md` (propositions), `E3-T2-critique-croisee-{A,B,D,E}.md` (critiques des autres), `E3-T3-reponse-{A,B,D,E}.md` (réponses). Lis les douze cellules en entier.
2. **Les fiches de ce matin pour ce mentor**, déjà normalisées et moissonnées : dans `/home/claude/scratch/ideation-rapport/melange-v1/fiches-classement-B-v1.json` (sha256 `84af169b1a5a2daad85367e5b7f3378527694943fb57d5a748f3889a15f1cd33`), les fiches dont le champ `classement` nomme ce mentor : M-062, M-060, M-051, M-053 (leurs notes de classement sont dans `/home/claude/scratch/ideation-rapport/classement-D/classement-B-v1.md`, rubrique Ibrahim). Tu ne les réécris pas : tu t'en sers pour le dédoublonnage (une idée du tour qui a la même hypothèse et la même mesure qui tue qu'une fiche du matin se fond dans celle-ci, et tu le dis).

## Règles de lecture
- Version d'une idée : la plus récente de son espèce (réponse si elle y est révisée, sinon proposition) ; critiques et réponses jointes à la fiche comme **objections** (sourcée : une pièce et sa section, ou une source primaire que tu ouvres ; non sourcée sinon) et **réponses**.
- **Pas de consensus** : une idée critiquée reste gardée tant qu'aucune source citée ne la réfute. Réfutée seulement si une source citée contredit son énoncé central, ou si elle se contredit elle-même.
- Une idée **répond** si elle donne : le projet choisi (l'un des deux de la mentore), la première expérience (ce qu'on entraîne ou mesure), le résultat attendu, et une chose qui rendrait le résultat trompeur ; s'il en manque, elle est gardée et le manque est écrit.

## Ce que tu écris (dossier `/home/claude/scratch/soir-rapport/ibrahim-q1/lecteur-A/`, fichiers neufs)
1. `fiches-normalisees-v1.json` : une liste de fiches, **identifiants opaques** (`I-001`, `I-002`, … dans un ordre sans lien avec la source), **aucune provenance** (ni lettre d'espèce, ni nom de modèle, ni nom de fichier) : `id`, `classement` (« I » si elle répond à la question ou touche ce que fait ce mentor, « hors sujet » sinon), `type`, `enonce` (une phrase falsifiable), `mecanisme`, `ce_qu_on_entraine_ou_mesure`, `resultat_attendu` (avec signe), `ce_qui_rendrait_le_resultat_trompeur`, `mesure_qui_tue`, `echec_le_plus_probable`, `rattachement_piece` (« neuve » / « prolonge la pièce, point n » / « déjà dans une pièce »), `cout`, `outil_du_mentor`, `appuis_lazar` (résultats publics de Lazar que la source invoque, tels quels), `objections` (liste : texte court, « sourcée » ou « non sourcée », source), `reponses`, `manques`, `doublon_du_matin` (identifiant de la fiche du matin fondue, ou rien), `note_du_lecteur`, `statut` (« gardée » ou « réfutée »). Ce qui manque reste vide et se dit ; tu ne complètes rien.
2. **Dédoublonnage par structure** : même hypothèse et même mesure qui tue = une fiche.
3. `refutees-v1.md` (chaque réfutation avec sa preuve) et `hors-sujet-v1.md`.
4. La clé, à part : `cle-provenances-v1.json` (identifiant → liste de provenances : cellule, espèce, numéro de l'idée dans la cellule).

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier du dépôt modifié ; rien sous `donnees/` ; aucun `git` ; aucun appel de modèle autre que toi ; `WebFetch` seulement pour vérifier une source qu'une objection cite. N'ouvre rien sous `/home/claude/coffre-*`, ni les dossiers `pour-lazar/`, ni `/home/claude/scratch/ideation-rapport/lecteur-A/`. `nice -n 10` pour tout script.

## Rendu
Réponse finale : nombre d'idées lues, de fiches après dédoublonnage (dans le sujet et hors sujet), de réfutées, de doublons du matin ; chemins et sha256 de tes fichiers.
