Tu es un **vérificateur neuf** des faits et des chiffres de la réponse de Lazar Ciric à la question 1 de Lujain Ibrahim (candidature à Pivotal), qu'il a reformulée lui-même et que le directeur a corrigée au minimum sur le fond. Tu n'as écrit aucune version de cette réponse. Français, sans sigle non développé ; toute heure vient de `date -u`. **Vise 15 minutes.**

## Pièces (vérifie les empreintes par leurs `.sha256` compagnons)
Dossier `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q1/` :
- texte de Lazar : `reponse-lazar-reformulee-v1.md` ; correction du directeur : `reponse-v5.md` (la liste des corrections est sous le trait) ;
- référence vérifiée sur le même contenu : `reponse-v4.md`, `registre-affirmations-v2.md`, `verification-chiffres-v2.md`, `lecture-mentor-v2.md`, `note-piste-v2.md`.
- Sources : la pièce `/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-ibrahim-v1.md` ; le dépôt public, clone en lecture seule `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` (`git show b3ecaec:CHEMIN`, préenregistrement de R8, `STATUS.md`) ; arXiv 2507.21919 (papier sur la chaleur, tableau E5) et 2511.01689 (Open Character Training) par `WebFetch` si une affirmation n'est pas déjà dans les rapports de la v4 (transcription non opposable, à dire).

## Ce que tu fais
1. Pour **chaque affirmation factuelle** de `reponse-v5.md` (corps au-dessus du trait) : verdict exact, inexact, plus fort que sa source, non vérifiable ; source et emplacement (ligne du rapport de la v4 si elle y est déjà vérifiée).
2. Contrôle que chaque correction listée sous le trait est juste, et qu'aucune affirmation fausse du texte de Lazar n'a été laissée (relis son texte entier ; en particulier : « happy sentences » du papier, « four tasks », « cold test » sur des modèles plus grands, statut de R8, le lien).
3. Signale tout passage où la v5 dirait plus que la v4 vérifiée.

## Ce que tu écris
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q1/verification-reformulation-lazar-v1.md` (neuf) : un tableau, puis les problèmes avec leur **correction minimale** (en anglais, permis pour cette réponse), du plus grave au plus léger.

## Interdits
Aucun commit, aucun `.sha256`, aucun `git fetch`, aucun fichier existant modifié, rien sous `donnees/` ni `/home/claude/coffre-*`, aucun code des dépôts exécuté. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.
