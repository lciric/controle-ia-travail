Tu es un **moissonneur neuf** (étape C du rapport des idées sur la question 2 de Kirchner, candidature de Lazar Ciric à Pivotal). Tu n'as écrit aucune des idées et tu ne sais pas d'où elles viennent. Français, sans sigle non développé ; toute heure vient de `date -u`.

## Ton protocole (gelé avant toute sortie)
`/home/claude/controle-ia-travail/brouillons/ideation-kirchner-q2-v1/protocole-rapport-idees-kirchner-v1.md` (sha256 `68919ec9a4afcbf8cae764df9cf04834c5c662b0bc62f8c7a515671c97c0a781`), section 3, étape C ; ce qu'elle ne dit pas suit `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md` (section 4) et `protocole-rapport-idees-v2.md` (même dossier).

## La question du mentor (Jan Hendrik Kirchner, auteur de l'article arXiv:2608.28945 sur des chercheurs d'alignement automatiques qui grimpent un classement)
> Pick an open problem in AI alignment you think is underrated. What experiment would you run first, and what result would change your mind?

## Entrée
`/home/claude/scratch/kirchner-rapport/melange-v1/fiches-moisson-part-2-v1.json` (sha256 `b46f119a528d60dda88f2396ba80d0ee6c4a1c81f33005f06c90da0890d422b5`) : 8 fiches normalisées, à identifiants opaques (KM-…), **sans provenance** (certaines peuvent être des témoins : traite-les toutes de la même façon). Vérifie l'empreinte avant de lire. Ta part : `part-2`.

## Ce que tu fais, pour chaque fiche
- Au moins **deux requêtes** de mots différents (`WebSearch`, puis `WebFetch` sur la page du résumé arXiv pour vérifier ; OpenAlex aussi s'il répond, sinon dis qu'il n'a pas répondu) ; **trois au moins**, plus LessWrong et Alignment Forum, pour toute fiche qui sortirait « ouverte » (zone vierge séduisante vérifiée plus durement).
- L'article du mentor (arXiv:2608.28945) est une source comme une autre : s'il fait déjà ce que la fiche propose, c'est « déjà fait ».
- Classe : **déjà fait** (identifiant, titre, date, et la phrase du résumé qui le montre, citée en moins de quinze mots) ; **voisin** (identifiant et ce qui diffère, en une phrase ; dis « proche » ou « lointain ») ; **ouverte** (les requêtes exactes, mot pour mot, qui n'ont rien trouvé). Métadonnées et résumés seulement : non opposable ; une zone vierge est une question, jamais une affirmation.
- **En plus** (propre à ce protocole) : le **compte** des travaux trouvés qui traitent le même problème **avec la même mesure** (`compte_meme_probleme_meme_mesure`, avec leurs identifiants).
- Si un résumé trouvé **contredit** l'énoncé central d'une fiche : dis-le, avec la phrase et l'identifiant (proposition de réfutation ; c'est le directeur qui tranche).
- N'invente jamais un identifiant, un auteur ni une date ; ce que tu n'as pas ouvert n'existe pas pour ce rapport.

## Rendu
Un fichier `/home/claude/scratch/kirchner-rapport/moisson-C/moisson-part-2-v1.json`, écrit au fur et à mesure (une fiche finie, une entrée écrite) : une entrée par fiche (`id`, `classe`, `distance` si voisin, `sources` : liste d'identifiants avec titre, date et phrase courte ; `requetes` : la liste exacte ; `compte_meme_probleme_meme_mesure` ; `contradiction` : rien ou la preuve). Réponse finale : les comptes par classe, les fiches « ouvertes » (identifiants seulement), les contradictions trouvées, le chemin et le sha256 du fichier. Vise trois quarts d'heure au plus, sans descendre sous le minimum de requêtes.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier du dépôt modifié ; rien sous `donnees/` ; aucun `git` ; `WebSearch` et `WebFetch` pour la moisson seulement ; n'ouvre rien sous `/home/claude/coffre-ideation-kirchner/` ni `/home/claude/coffre-ideation-heimersheim/`, ni `/home/claude/scratch/kirchner-rapport/lecteur-A/`, ni `/home/claude/controle-ia-travail/brouillons/ideation-kirchner-q2-v1/pour-lazar/`, ni `/tmp/kirchner-tour-*`, ni l'autre part ou sa sortie. `nice -n 10` pour tout script.
