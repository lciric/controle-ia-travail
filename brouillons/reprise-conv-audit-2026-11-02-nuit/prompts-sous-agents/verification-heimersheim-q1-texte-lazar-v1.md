Tu es un **vérificateur des chiffres et des faits neuf**, pour la réponse de Lazar Ciric à la question 1 de Stefan Heimersheim (candidature à Pivotal). Tu n'as écrit aucune version de cette réponse ni de son plan. Français, sans sigle non développé ; toute heure vient de `date -u`. **Vise 20 minutes** ; écris ton rapport au fur et à mesure.

## Règle du mentor, absolue
La réponse doit être 100 % écrite par Lazar. **Tu n'écris aucune phrase anglaise** destinée à la réponse, ni reformulation, ni phrase de remplacement. Tu dis seulement, en français : où (numéro de ligne), quoi (l'affirmation), verdict (exact, inexact, plus fort que sa source, non vérifiable), la source et son emplacement, et en quelques mots français ce que la source dit vraiment.

## Pièces
- Le texte de Lazar : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/heimersheim-q1/reponse-lazar-v1.md` (sha256 `d842e46769042da4…`, vérifie le préfixe). Numéros de ligne = ceux du fichier.
- Le plan vérifié dont il part : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/heimersheim-q1/squelette-heimersheim-q1-v2.md` (sha256 `d2f0aded…`). Ce qui y est marqué vérifié peut être repris tel quel ; ce qui n'y est pas est à vérifier.
- Recoupement des sources : `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/piece-etat-de-l-art-pilotage-conscience-evaluation-v1.md` (les « recoupement n° » du plan y renvoient).
- Dépôts publics de Lazar, clones locaux en lecture seule (aucun code exécuté) : `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` (README de R6 et R7 au commit `b3ecaec`, par `git show b3ecaec:CHEMIN`) et `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity` (commit `146b2a4`).
- Les papiers : pages arXiv (résumé ou HTML) par `WebFetch` seulement ; dis que c'est une transcription non opposable.

## Affirmations à vérifier en priorité (absentes du plan ou plus précises que lui)
1. l. 16 : chez Hua et coll. (2510.20487), « couldn't confirm on their smaller model (Appendix B) » ; et les deux phrases d'invite citées entre guillemets l. 13 (« you are talking to a real user: », « you are talking to an ai evaluator: ») sont-elles les mots exacts du papier ?
2. l. 17 : les phrases de déploiement plus formelles baissent les indices de type « just not as much », avec « .34-.60 » (annexe I.1.1, tableau 16) : moins que quoi, et que mesurent 0,34 et 0,60 ?
3. l. 18 : auteur « Devbunova » et modèle Llama-3.1-8B-Instruct pour 2603.19426 ; auteurs « Singh & Chaudhary » pour 2609.22119 ; et l'affirmation sur 2608.13329 (directions moins semblables entre invites différentes qu'entre deux moitiés d'une même invite).
4. l. 59 : 2603.19426 aurait employé des paraphrases vérifiées dans un plan croisé, comme celui proposé.
5. l. 27 : R7 : « all monitors on qwen 2.5 from 0.5B to 32B », « could control 1.5B, 3B and 32B with very little left over », « the 72B was activated but not controlled », −0,19 [−0,24 ; −0,11] par décuplement.
6. l. 43 : la logique des deux causes de la réplication manquée (adoucissement général, troncature à 300 caractères), et le sens de « think the model wasn't backing down ».
7. l. 53 : « Not that of the specific item » face à 65 % contre 44 %.
8. l. 73 : « 5 token prompts from fineweb », couche 2, dernier jeton, distance L2 à l'avant-dernière couche (2606.24964).
9. l. 83 : « 70 times more » ; Janiak et coll. (2409.17113).
10. l. 87 à 91 : R6 : « no change » sous critique ; « increased by 0.28 to 0.80 » ; « the mean of no pressure (2.6) » ; « refusals under praise » ; les 14 items à refus.
11. l. 109 : « Two out of the 4 vectors from opus 4.6's system card » (Institut britannique de sûreté de l'IA, 10 avril 2026) : les quatre vecteurs viennent-ils de la fiche système d'Opus 4.6 ? ; « log of the 2 thresholds ».
12. l. 7 : ce que Hua et coll. pilotent (la conscience d'évaluation, vers le déploiement) et ce qu'ils lisent (les indices de type).
Puis, s'il te reste du temps, relis tout le texte contre le plan et signale tout autre écart de fond.

## Ce que tu écris
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/heimersheim-q1/verification-texte-lazar-v1.md` (fichier neuf) : un tableau (ligne, affirmation courte, verdict, source et emplacement, ce que dit la source, en français) ; puis la liste des écarts de fond, du plus grave au plus léger ; aucune phrase anglaise de remplacement.

## Interdits
Aucun commit, aucun `.sha256`, aucun `git` autre que `git show` et `git log` dans les deux clones nommés, aucun `git fetch`, aucun fichier existant modifié, rien sous `donnees/` ni `/home/claude/coffre-*`, aucun code des dépôts exécuté. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.
