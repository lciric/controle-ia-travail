Tu es un **moissonneur neuf** (étape C du rapport des idées sur la question 2 (facultative) de Paul Colognese et Francis Rhys Ward, sur leur billet, candidature de Lazar Ciric à Pivotal). Tu n'as écrit aucune des idées et tu ne sais pas d'où elles viennent. Français, sans sigle non développé ; toute heure vient de `date -u`.

## Ton protocole (gelé avant toute sortie)
`/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/protocole-rapport-mentors-soir-v1.md` (sha256 `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`), étape C ; ce qu'il ne dit pas suit `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md` (section 4).

## La question du mentor (texte exact)
> (Optional) Read this post. Should we have done anything differently? What was the most interesting finding in your view and why?

## Entrée
`/home/claude/scratch/soir-rapport/colognese-ward-q2/prep-v1/fiches-lot2-moisson-part-3-v1.json` (sha256 `a3970e7fae55b74222227e72b8e066717e2693c91884890ebfcd6b39a90802b7`) : 7 fiches normalisées, à identifiants opaques, **sans provenance**. Vérifie l'empreinte avant de lire.

## Ce que tu fais, pour chaque fiche
- Au moins **deux requêtes** de mots différents (`WebSearch`, puis `WebFetch` sur la page du résumé arXiv ou OpenReview pour vérifier ; OpenAlex est refusé par la session : ne l'essaie pas) ; **trois au moins**, plus LessWrong et Alignment Forum, pour toute fiche qui sortirait « ouverte » (zone vierge séduisante vérifiée plus durement).
- Les travaux du mentor sont des sources comme les autres : s'ils font déjà ce que la fiche propose, c'est « déjà fait ». Leur billet et leurs travaux sont décrits dans `/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-colognese-ward-v1.md`, section 1 (lecture permise). N'ouvre pas les autres parts ni leurs sorties.
- Classe : **déjà fait** (identifiant, titre, date, et la phrase du résumé qui le montre, citée en moins de quinze mots) ; **voisin** (identifiant et ce qui diffère, en une phrase ; « proche » ou « lointain ») ; **ouverte** (les requêtes exactes, mot pour mot, qui n'ont rien trouvé). Métadonnées et résumés seulement : non opposable ; une zone vierge est une question, jamais une affirmation.
- Si un résumé trouvé **contredit** l'énoncé central d'une fiche : dis-le, avec la phrase et l'identifiant (proposition de réfutation ; c'est le directeur qui tranche).
- N'invente jamais un identifiant, un auteur ni une date ; ce que tu n'as pas ouvert n'existe pas pour ce rapport.

## Rendu
Un fichier `/home/claude/scratch/soir-rapport/colognese-ward-q2/moisson-C/moisson-lot2-part-3-v1.json`, écrit au fur et à mesure (une fiche finie, une entrée écrite) : une entrée par fiche (`id`, `classe`, `distance` si voisin, `sources` : identifiants avec titre, date et phrase courte ; `requetes` : la liste exacte ; `contradiction` : rien ou la preuve). Réponse finale : comptes par classe, fiches « ouvertes », contradictions, chemin et sha256 du fichier. **Vise une demi-heure**, sans descendre sous le minimum de requêtes.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git` ; `WebSearch` et `WebFetch` pour la moisson seulement ; n'ouvre rien sous `/home/claude/coffre-*`, ni les dossiers `lecteur-A/` ou `pour-lazar/`, ni `/tmp/soir-tours-v1/`. `nice -n 10` pour tout script.

**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.
