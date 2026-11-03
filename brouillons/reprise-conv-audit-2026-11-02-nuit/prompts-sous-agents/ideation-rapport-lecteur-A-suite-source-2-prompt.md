Tu es le **lecteur A, suite** (normalisation et dédoublonnage) du rapport des idées pour la candidature de Lazar Ciric à Pivotal. Le premier lecteur A a traité les sources 1 et 3 ; il ne peut plus être joint (son identifiant a été perdu). Tu prends sa suite pour la **source 2** seule, avec ses règles et son format, sur ses fichiers. Tu n'as écrit aucune des idées ni aucun des textes. Français, sans sigle non développé ; toute heure vient de `date -u`.

## Ton protocole (gelé avant toute lecture d'une sortie : lis-le d'abord, en entier)
- `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v2.md` (`cfff33cf…`) et la section 2 de la v1 (`protocole-rapport-idees-v1.md`, même dossier) : tu fais **l'étape A** sur la source 2.
- La consigne du premier lecteur A, pour le format exact des fiches et les règles : `/home/claude/controle-ia-travail/brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/ideation-rapport-lecteur-A-collisionneur-prompt.md`. Ce qui y est dit des cellules, des espèces, des objections croisées et de la clé dans le coffre ne vaut pas pour toi (voir plus bas).
- La question servie à la course : `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/question-ideation-heimersheim-v1.md` ; la pièce de référence pour le rattachement : `piece-etat-de-l-art-pilotage-conscience-evaluation-v1.md` (même dossier).

## Ce qui existe déjà (le travail du premier lecteur A ; lis-le en entier avant la source 2)
Dossier `/home/claude/scratch/ideation-rapport/lecteur-A/` : `fiches-normalisees-v2.json` (78 fiches, `6f8574bf…`), `refutees-v2.md` (`16554c5c…`), `hors-sujet-v2.md` (`3681f041…`). Tu ne modifies aucun de ces fichiers.

## Source 2 (préparée par le directeur, sans provenance)
`/home/claude/scratch/ideation-rapport/source-2/source-2-course-heimersheim-v1.json` (`b8435f4e…`) : 47 éléments `S2-01` à `S2-47`, chacun avec son `contenu` (titre, axe, hypothèse, prédiction, épreuve, contrôle, test de mort, coût) ; ce sont les fiches de toutes les passes de tous les proposeurs et les fusions du bisociateur de la course de l'organisme sur la question servie, dans un ordre permuté. Une fiche de proposeur classée « à corriger » n'a pas de contenu dans la sortie : elle est comptée et ne t'est pas donnée. Lis les 47 éléments en entier.
- **Classement** : la course porte sur la question 1 de Heimersheim ; un élément est « A » s'il porte sur cette question ou sur la direction (c) ; s'il porte nettement sur la question d'un autre mentor, « B:<mentor> » ; sinon hors sujet (annexe).
- **Aucune objection croisée** dans cette source (les sorties des juges de la course sont exclues par le protocole) : `objections` et `reponses` restent vides, sauf pour une fiche fusionnée qui en avait déjà.
- **Dédoublonnage par structure**, contre les 78 fiches existantes et entre éléments : même hypothèse et même mesure qui tue = une seule fiche. Une fusion avec une fiche existante garde le texte de la fiche existante ; un champ vide de celle-ci peut être rempli par le texte de l'élément, cité tel quel, et c'est dit dans `note_du_lecteur`.
- **Réfutée** seulement si une source citée (point de la pièce, ou source primaire que tu ouvres et cites avec section ou page) contredit son énoncé central, ou si l'élément se contredit lui-même ; jamais par accord ou désaccord de modèles. Tout le reste est gardé. `WebFetch` seulement pour vérifier une telle source.
- Ce qui manque reste vide et se dit (`manques`) ; tu ne complètes rien toi-même.

## Ce que tu écris (versions neuves ; on n'écrase jamais)
1. `/home/claude/scratch/ideation-rapport/lecteur-A/fiches-normalisees-v3.json` : les 78 fiches de la v2 (identiques, sauf les champs remplis par une fusion, dits dans `note_du_lecteur`) puis les fiches neuves `F-079`, `F-080`, …, même format que la v2 (mêmes clés), **aucune provenance**.
2. `refutees-v3.md` et `hors-sujet-v3.md` (même dossier) : ceux de la v2, plus ce que la source 2 ajoute.
3. La clé de la source 2, **hors du coffre** : `/home/claude/scratch/ideation-rapport/lecteur-A/cle-provenances-source-2-v3.json` : pour chaque fiche (neuve ou fusionnée) la liste de ses éléments `S2-xx`, et pour chaque élément son sort (fiche neuve, fusionné dans F-…, réfuté, hors sujet).

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; `WebFetch` seulement pour vérifier une source qui réfuterait. Ne lis **rien** dans `/home/claude/coffre-ideation-heimersheim/`, ni dans `/tmp/course-heimersheim-v1/` (la sortie brute de la course : provenances et verdicts des juges). `nice -n 10` pour toute commande lourde.

## Rendu
Réponse finale : nombre d'éléments lus ; fiches neuves et fusions (par classement : A, et B par mentor) ; réfutés ; hors sujet ; total des fiches de la v3 ; les chemins et sha256 de tes fichiers ; tout doute sur un dédoublonnage, en une ligne chacun.
