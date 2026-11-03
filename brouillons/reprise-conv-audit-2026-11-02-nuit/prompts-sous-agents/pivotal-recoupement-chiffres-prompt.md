Tu es un vérificateur neuf. Tu n'as écrit ni les réponses de Lazar Ciric aux mentors de Pivotal, ni leurs réécritures, ni les six rapports de lecture. Travaille en français. Toute heure vient de `date -u`.

## Ce que tu vérifies
Le fichier `/home/claude/scratch/pivotal-approfondi/reponses-mentors-approfondies-v1.md` rassemble, pour six mentors, les réponses réécrites (blocs de texte anglais entre trois accents graves) et les listes de changements. Les rapports complets des six lecteurs, avec leurs sources et copies téléchargées, sont dans `/home/claude/scratch/pivotal-approfondi/<mentor>/` (rapport-*.md, dossiers `sources*`, `travail`, `brouillons`).

Pour **chaque chiffre, chaque citation et chaque affirmation factuelle** des blocs de texte anglais (et des faits que le fichier propose pour la Q1 de Heimersheim), vérifie-le sur la source primaire : papier arXiv (lis la page par `WebFetch` sur `https://arxiv.org/html/<id>` ou `https://arxiv.org/pdf/<id>`, par tranches), dépôt public (`https://github.com/lciric/sycophancy-psychophysical-law`, `https://github.com/lciric/ideation-organism` ; si WebFetch est refusé, les copies locales des lecteurs, avec leurs empreintes, ou `raw.githubusercontent.com`), billet LessWrong. Une affirmation sur les résultats de Lazar n'est exacte que si un dépôt public la porte, sauf ρ = 0,68, < 1 % et 68 %, qui viennent de son programme non publié et se gardent tels quels (dis-le).

## Rendu
Un fichier `/home/claude/scratch/pivotal-approfondi/recoupement-v1.md` : une ligne par affirmation vérifiée (mentor | phrase exacte | source et emplacement | exact / inexact / non vérifiable), puis la liste des inexactitudes avec la correction minimale proposée. Ta réponse finale : nombre d'affirmations vérifiées, inexactitudes une ligne chacune avec la correction, non-vérifiables, sha256 du fichier.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/`, aucun appel de modèle autre que toi, `nice -n 10`. Tes fichiers sous `/home/claude/scratch/pivotal-approfondi/recoupement/` et le fichier de rendu.
