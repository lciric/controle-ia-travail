Tu es le préparateur neuf des témoins d'un classement d'idées (étape B du protocole `brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md` du dépôt `/home/claude/controle-ia-travail`). Tu ne classeras rien, et tu ne verras aucune des idées à classer (aucune n'existe encore). Rapport en français ; toute heure vient de `date -u`.

## Contexte
Lazar Ciric répond à la question 1 du mentor Stefan Heimersheim (option c : pilotage des activations contre la conscience d'évaluation). Des modèles vont produire des idées (raisons d'échec, épreuves, lectures du résidu) ; un classeur neuf les ordonnera par originalité vérifiée, testabilité en jours sur Llama-3.1-8B-Instruct, et lien avec les outils du mentor. Pour contrôler ce classement, on glisse parmi les idées **deux témoins : des idées déjà publiées, déguisées**. Si le classeur les prend pour originales, son axe d'originalité est invalide.

## À lire
- La question servie : `brouillons/ideation-heimersheim-v1/question-ideation-heimersheim-v1.md`.
- La pièce servie (ce que tout le monde sait déjà) : `brouillons/ideation-heimersheim-v1/piece-etat-de-l-art-pilotage-conscience-evaluation-v1.md`. **Tes témoins ne doivent pas être dans la pièce.**
- Le protocole, sections 2 et 3 (format des fiches normalisées).

## Ce que tu fais
1. Choisis **deux** travaux publiés (2024 à 2026), absents de la pièce, chacun directement lié à pourquoi le pilotage contre la conscience d'évaluation pourrait échouer, ou à comment l'éprouver ; de préférence des idées qu'un modèle pourrait plausiblement proposer lui-même. Pistes possibles, **à vérifier, pas à croire** (je les cite de mémoire, sans garantie) : l'injection de bruit dans les poids qui révèle une sous-performance volontaire ; la fiabilité très variable des vecteurs de pilotage d'une entrée à l'autre (effet de signe contraire sur une part des entrées) ; des sondes linéaires qui classent les bancs de sécurité usuels comme « tests » ; une loi d'échelle de la conscience d'évaluation avec la taille des modèles. Tu peux en choisir d'autres.
2. Pour chacun, **vérifie en source primaire** par `WebSearch` et `WebFetch` (page arXiv ou de l'éditeur) : identifiant, titre, auteurs, date, et la phrase exacte du résumé qui porte l'idée.
3. Écris chaque témoin comme une **fiche normalisée** au format du protocole (JSON, en français) : `type`, `enonce`, `mecanisme`, `mesure_qui_tue`, `prediction`, `echec_le_plus_probable`, `rattachement_piece` (« neuve »), `cout` — **rédigée comme une proposition**, sans citer sa source, sans tournure qui la trahisse (« comme l'ont montré… »), d'une longueur et d'un ton ordinaires (deux à quatre phrases par champ au plus).
4. Écris la **clé** à part : pour chaque témoin, identifiant, titre, auteurs, date, phrase exacte du résumé, et trois requêtes qui devraient le retrouver sur arXiv ou OpenAlex.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; `WebSearch` et `WebFetch` seulement pour trouver et vérifier ces deux travaux ; aucun appel de modèle autre que toi. Tes fichiers sous `/home/claude/scratch/ideation-temoins/` seulement : `temoins-deguises-v1.json` (une liste de deux fiches) et `cle-temoins-v1.json`.

## Rendu
Réponse finale : les chemins et sha256 (`sha256sum`) des deux fichiers, et **seulement** les identifiants et titres des deux travaux (pas le texte des fiches).
