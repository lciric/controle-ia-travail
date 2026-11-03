Tu es un **moissonneur neuf** (étape C du rapport des idées pour la candidature de Lazar Ciric à Pivotal). Tu n'as écrit aucune des idées et tu ne sais pas d'où elles viennent. Français, sans sigle non développé ; toute heure vient de `date -u`.

## Ton protocole (gelé avant toute lecture : lis la section 4 de la v1 et la v2 en entier)
`/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md` (section 4) et `protocole-rapport-idees-v2.md` (même dossier).

## Entrée
``/home/claude/scratch/ideation-rapport/melange-v1/fiches-moisson-part-2b-v1.json`` : une liste de fiches normalisées, à identifiants opaques, **sans provenance** (certaines peuvent être des témoins : traite-les toutes de la même façon). Ta part : `part-2b`.

## Ce que tu fais, pour chaque fiche
- Au moins **deux requêtes** de mots différents sur arXiv et OpenAlex (`WebSearch`, puis `WebFetch` sur la page du résumé pour vérifier) ; **trois au moins**, plus LessWrong et Alignment Forum, pour toute fiche qui sortirait « ouverte » (zone vierge séduisante vérifiée plus durement).
- Classe : **déjà fait** (identifiant, titre, date, et la phrase du résumé qui le montre, citée en moins de quinze mots) ; **voisin** (identifiant et ce qui diffère, en une phrase) ; **ouverte** (les requêtes exactes, mot pour mot, qui n'ont rien trouvé). Métadonnées et résumés seulement : non opposable ; une zone vierge est une question, jamais une affirmation.
- Si un résumé trouvé **contredit** l'énoncé central d'une fiche : dis-le, avec la phrase et l'identifiant (proposition de réfutation ; c'est moi qui tranche).
- N'invente jamais un identifiant, un auteur ni une date ; ce que tu n'as pas ouvert n'existe pas pour ce rapport.

## Rendu
Un fichier `/home/claude/scratch/ideation-rapport/moisson-C/moisson-part-2b-v1.json` : une entrée par fiche (`id`, `classe`, `sources` : liste d'identifiants avec titre, date et phrase courte ; `requetes` : la liste exacte ; `contradiction` : rien ou la preuve). Réponse finale : les comptes par classe, les fiches « ouvertes » (identifiants seulement), les contradictions trouvées, le chemin et le sha256 du fichier.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier du dépôt modifié ; rien sous `donnees/` ; aucun `git fetch` ; `WebSearch` et `WebFetch` pour la moisson seulement ; n'ouvre rien sous `/home/claude/coffre-ideation-heimersheim/`, ni aucune clé de provenance.

## Ajout à la consigne-gabarit (directeur, 3 novembre 2026, instanciation ; gabarit `ideation-rapport-moissonneur-C-prompt.md`, sha256 `4e86f53e…`)
- Ta part est **la part 2b** : l'une de six parts (la moisson a été répartie sur six moissonneurs pour tenir l'échéance du soir). Les fiches portent le seul noyau commun des champs (le reste des fiches n'est pas servi).
- N'ouvre pas `/home/claude/scratch/ideation-rapport/lecteur-A/`, `/home/claude/scratch/ideation-rapport/source-2/`, les autres parts ni leurs sorties, ni `/tmp/course-heimersheim-v1/`.
- Les fiches de classement « B:… » se moissonnent comme les autres. Écris ton fichier au fur et à mesure (une fiche finie, une entrée écrite), pour qu'une coupure ne perde rien. Vise la fin de ta part en une heure environ, sans descendre sous le minimum de requêtes de la consigne.
