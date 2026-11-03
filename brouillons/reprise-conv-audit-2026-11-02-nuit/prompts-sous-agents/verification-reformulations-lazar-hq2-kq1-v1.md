Tu es un **vérificateur neuf** des faits et des chiffres de deux réponses de Lazar Ciric (candidature à Pivotal), qu'il a reformulées lui-même et que le directeur a corrigées au minimum sur le fond. Tu n'as écrit aucune version de ces réponses. Français, sans sigle non développé ; toute heure vient de `date -u`. **Vise 15 minutes.**

## Pièces (vérifie les empreintes par leurs `.sha256` compagnons)
Dossier `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/` :
- Heimersheim Q2 (limite dure : 150 mots au plus) : texte de Lazar `heimersheim-q2/reponse-lazar-reformulee-v1.md` ; corrections du directeur `heimersheim-q2/reponse-v4.md` (fond) puis `heimersheim-q2/reponse-v5.md` (raccourcie sous la limite) ; référence vérifiée `heimersheim-q2/reponse-v3.md` et ses rapports `heimersheim-q2/verification-chiffres-v1.md`, `heimersheim-q2/lecture-mentor-v1.md`.
- Kirchner Q1 (aucune limite) : texte de Lazar `kirchner-q1/reponse-lazar-reformulee-v1.md` ; corrections du directeur `kirchner-q1/reponse-v4.md` ; référence vérifiée `kirchner-q1/reponse-v3.md`, `kirchner-q1/verification-chiffres-v1.md`, `kirchner-q1/registre-affirmations-v1.md`, `kirchner-q1/lecture-mentor-v1.md`.
- Sources publiques, clones locaux en lecture seule : `/home/claude/ideation-organism` (`git show faff48b:README.md`, `git show faff48b:resultats/attaque-goodhart-v2/…`) ; `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity` (`146b2a4`) et `…/sycophancy-psychophysical-law` (`b3ecaec`, préenregistrement de R9). Aucun code exécuté ; `git show` et `git log` seulement.

## Ce que tu fais
1. Pour **chaque affirmation factuelle** de `heimersheim-q2/reponse-v5.md` et de `kirchner-q1/reponse-v4.md` (corps au-dessus du trait) : verdict exact, inexact, plus fort que sa source, non vérifiable ; source et emplacement. Les affirmations déjà vérifiées dans la v3 peuvent renvoyer à la ligne du rapport de vérification de la v3 ; les autres se vérifient sur la source.
2. Contrôle que chaque correction listée sous le trait des deux fichiers est juste, et qu'aucune affirmation fausse du texte de Lazar n'a été laissée (relis son texte entier).
3. Compte les mots de `heimersheim-q2/reponse-v5.md` par espaces et au pire cas (liens découpés en leurs morceaux), contre la limite de 150.
4. Liens : présents et justes aux commits cités.

## Ce que tu écris
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/verification-reformulations-lazar-v1.md` (neuf) : un tableau par réponse, puis les problèmes avec leur **correction minimale** (en anglais, pour ces deux réponses c'est permis), du plus grave au plus léger.

## Interdits
Aucun commit, aucun `.sha256`, aucun `git fetch`, aucun fichier existant modifié, rien sous `donnees/` ni `/home/claude/coffre-*`. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.
