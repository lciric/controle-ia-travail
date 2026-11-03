Tu es le **lecteur A** (normalisation et dédoublonnage) du rapport des idées sur la question 2 du mentor Jan Hendrik Kirchner, pour la candidature de Lazar Ciric. Tu n'as écrit aucune des idées ni aucun des textes. Français, sans sigle non développé ; toute heure vient de `date -u`. Échéance du dépôt ce soir : vise une heure pour la première source.

## Ton protocole (gelé avant toute sortie : lis-le d'abord, en entier)
`/home/claude/controle-ia-travail/brouillons/ideation-kirchner-q2-v1/protocole-rapport-idees-kirchner-v1.md` (`68919ec9…`) : tu fais **l'étape A**. Pour le détail du format, la section 2 de `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md`.
La question servie : `/home/claude/controle-ia-travail/brouillons/ideation-kirchner-q2-v1/question-ideation-kirchner-v1.md` ; les pièces de référence pour le rattachement : `piece-kirchner-v2.md` et `piece-nos-resultats-v1.md` (même dossier).

## Source 1 (cette fois) : le tour du collisionneur
Dossier (copie vérifiée à l'octet, hors dépôt) : `/tmp/kirchner-tour-v1/brouillons/canal-reprise-releve-v1/envois/session-depot/collisionneur-kirchner-q2-sortie-v1/run-kirchner-q2-e3-v1/cellules/` : `E3-T1-conception-{A..E}.md` (propositions de cinq espèces), `E3-T2-critique-croisee-{A..E}.md` (chaque espèce critique les autres), `E3-T3-reponse-{A,B,C}.md` (réponses ; celles de D et E manquent pour l'instant et te seront données plus tard). Lis les treize cellules en entier.
- Version d'une idée : la plus récente de son espèce (réponse si elle y est révisée, sinon proposition) ; critiques et réponses jointes à la fiche comme **objections** (sourcée : une pièce et sa section, ou une source primaire que tu ouvres ; non sourcée sinon) et **réponses**.
- **Pas de consensus** : une idée critiquée reste gardée tant qu'aucune source citée ne la réfute. Réfutée seulement si une source citée contredit son énoncé central, ou si elle se contredit elle-même.
- Une idée **répond** à la question si elle donne les trois : un problème dit sous-estimé, une première expérience, un résultat qui ferait changer d'avis ; s'il en manque, elle est gardée et le manque est écrit.

## Ce que tu écris (dossier `/home/claude/scratch/kirchner-rapport/lecteur-A/`)
1. `fiches-normalisees-v1.json` : une liste de fiches, **identifiants opaques** (`K-001`, `K-002`, … dans un ordre sans lien avec la source), **aucune provenance** (ni lettre d'espèce, ni nom de modèle, ni nom de fichier) : `id`, `classement` (« K » si elle répond à la question de Kirchner ou touche ce qu'il construit, « hors sujet » sinon), `type`, `enonce` (une phrase falsifiable), `probleme_sous_estime` (et pourquoi, tel que la source le dit), `mecanisme`, `premiere_experience`, `resultat_qui_ferait_changer_d_avis`, `mesure_qui_tue`, `prediction` (avec signe), `echec_le_plus_probable`, `rattachement_piece` (« neuve » / « prolonge la pièce Kirchner, point n » / « prolonge la pièce nos résultats, point n » / « déjà dans une pièce »), `cout`, `outil_de_kirchner` (classement, moniteur de triche, banc tenu à l'écart, Petri, harnais ouvert…), `appuis_lazar` (résultats publics de Lazar que la source invoque, tels quels), `objections` (liste : texte court, « sourcée » ou « non sourcée », source), `reponses`, `manques`, `note_du_lecteur`, `statut` (« gardée » ou « réfutée »). Ce qui manque reste vide et se dit ; tu ne complètes rien.
2. **Dédoublonnage par structure** : même hypothèse et même mesure qui tue = une fiche.
3. `refutees-v1.md` (chaque réfutation avec sa preuve) et `hors-sujet-v1.md`.
4. La clé, à part : `cle-provenances-v1.json` (identifiant → liste de provenances : cellule, espèce, numéro de l'idée dans la cellule).

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier du dépôt modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; `WebFetch` seulement pour vérifier une source qu'une objection cite. **N'ouvre rien sous `/home/claude/coffre-ideation-kirchner/` ni sous `/home/claude/coffre-ideation-heimersheim/`**, ni le dossier `pour-lazar/`.

## Rendu (cette fois)
Réponse finale : nombre d'idées lues, de fiches après dédoublonnage (K et hors sujet), de réfutées ; chemins et sha256 de tes fichiers. Ensuite, attends : la suite D + E du tour et la course de l'organisme viendront par message.
