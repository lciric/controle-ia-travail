Tu es un **rédacteur neuf** d'une réponse de Lazar Ciric au formulaire Pivotal (dépôt ce soir, 23:00 UTC). Tu n'as écrit aucune version de ses réponses. Notes en français, sans sigle non développé ; la réponse elle-même en anglais ; toute heure vient de `date -u`. Vise **une heure**.

## La question
- Mentor : **Lujain Ibrahim** ; question (texte exact, `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, ligne 148) ; limite : aucune limite écrite ; au plus 300 mots (sa réponse actuelle en a 287).

## Les règles de Lazar (mots du 3 novembre, heure de Paris)
- 13:05 et 13:06 : « on sélectionne d'abord la piste la plus fructueuse, les arguments les plus forts et les plus fertiles, on repart de zéro, page blanche, je ne veux pas de ma réponse générique » ; « jamais de structure préétablie ».
- Donc : **sa réponse actuelle** (même fichier, lignes 150 à 160) n'est qu'un **réservoir de faits** : ni sa structure, ni son ordre, ni ses phrases. La forme suit la piste choisie ; ce que la question demande en clair doit y être, dans l'ordre que la piste dicte.

## Sources (lis-les avant d'écrire)
- Ce que fait le mentor : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-ibrahim-v1.md` (lecteur neuf, pages primaires citées). Ses sections de réécriture partent de l'ancienne réponse : **n'en reprends pas la structure** ; prends-y les faits.
- Résultats publics de Lazar : `brouillons/ideation-kirchner-q2-v1/piece-nos-resultats-v1.md` ; `brouillons/ideation-mentors-soir-v1/piece-sycophancie-publique-v1.md` ; README public `/home/claude/ideation-organism/README.md`. État réel de l'organisme (faits internes) : `brouillons/ideation-conception-organisme-v1/piece-etat-reel-organisme-v1.md`.
- Corrections déjà établies par une lectrice indépendante (à respecter) : `brouillons/canal-fable-v1/fable_2026-11-03_n001.md`.
- Affirmations déjà vérifiées par un vérificateur neuf (verdict et source par phrase), pour d'anciennes réécritures : `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` (sha256 `bea573aa1e62d5d5bfb1aa677a902c9ec977ea1740941eed5b4277bae0e4fe0a`). Prends-y les verdicts et les sources, jamais l'ordre ni les phrases. Ses lignes « ρ = 0,68, < 1 %, 68 % : programme non publié » sont dépassées par la lectrice indépendante (fichier Fable ci-dessus) : D36 est public au commit `146b2a4` ; ρ = 0,684 et le bras « 1 % » sont **deux objets distincts** (le bras 1 % est celui de l'essai original seul, non public, non refait) ; ne les fonds jamais en une phrase.
- Ce qui est public sur ses pages : `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-pages-publiques-v1.md` et `relecture-pages-publiques-v1.md`.
- Dépôts publics, clones frais en lecture seule (n'exécute jamais leur code) : `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity` (commit `146b2a4`), `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` (commit `b3ecaec`), `/home/claude/ideation-organism` (branche `main`, `faff48b`). Dans la réponse, les liens vont vers `https://github.com/lciric/…`, épinglés à un commit quand cela aide à vérifier.
- Faits internes du programme de contrôle (non publics) : dépôt `/home/claude/controle-ia-travail` (registres, `diag/`, `papiers/`), en lecture seule ; un fait interne n'entre dans la réponse que dit comme non publié, et seulement si tu le retrouves dans un fichier daté (chemin et sha256).
- Coordination : l'autre question de la même mentore (Q1, la première expérience sur l'un de ses deux projets : entraînement de caractère, puis apprentissage par renforcement, et sycophantie) est rédigée à part, à partir d'un rapport d'idées. La Q2 décrit un projet fait ; ne la transforme pas en seconde Q1.
Tous les chemins relatifs partent de `/home/claude/controle-ia-travail`.

## Ce que tu fais
1. **Piste** : trois à cinq pistes candidates pour répondre (angle, ce qui la rend forte pour ce mentor : touche son travail, distinctive, vérifiable par lui, défendable par Lazar seul en entretien) ; choisis la plus fructueuse, raisons en cinq lignes.
2. **Registre des affirmations** : chaque affirmation de la réponse, avec sa source (chemin et sha256, ou papier et page ou section) et sa force (« publique et vérifiée » ; « interne vérifiée » ; « non vérifiée » : interdite dans la réponse). Un résultat non concluant, non publié, ou un travail non fait n'entre que dit comme tel (« preregistered, not yet run ») ; aucun résultat inventé ; rien de ce que Lazar n'a pas fait présenté comme fait.
3. **La réponse**, en anglais, à la première personne de Lazar : simple, concret, phrases courtes, sans effets de style ni formules toutes faites, sans titres ni listes sauf si la question les appelle ; chaque nombre dans le registre ; liens publics quand ils aident le mentor à vérifier. Respecte la limite.
4. **Relis-toi** comme le mentor : la phrase qu'il contredirait de ses propres travaux ; corrige.

## Ce que tu écris (fichiers neufs, `brouillons/redaction-finale-v1/ibrahim-q2/`)
`note-piste-v1.md` (français), `registre-affirmations-v1.md`, `reponse-v1.md` (la réponse seule, puis son compte de mots par script).

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; `WebFetch` seulement pour vérifier un fait du mentor que le rapport ne donne pas ; rien sous `/home/claude/coffre-*` ; niveau méthode pour toute triche (classe et rôle de mesure, jamais un mode d'emploi).

## Rendu
Réponse finale : la piste en une ligne ; le compte de mots ; le registre résumé (nombre d'affirmations par force) ; ce qui reste à confirmer par Lazar ; chemins et sha256.
