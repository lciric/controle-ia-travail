Tu es un rédacteur neuf de **pièce servie** pour un tour du collisionneur (cinq modèles de langage de fournisseurs différents qui proposent puis se critiquent). Tu n'as écrit ni la candidature de Lazar Ciric ni les rapports que tu vas lire. Français, sans sigle non développé ; toute heure vient de `date -u`. Échéance : rends en **vingt minutes au plus**.

## Le mentor et sa question
- Mentor : **Lujain Ibrahim**.
- Question du formulaire (texte exact, à lire dans `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-mentors-colle-par-lazar-2026-11-03-0006.txt`, lignes 227 à 239) : « Pick one of the two projects and briefly describe the first experiment you'd run… what you'd train or measure, what result you'd expect, and one thing that could make the result misleading. » La direction visée ici est la persistance d'une persona installée par entraînement de caractère après un apprentissage par renforcement, et son effet sur la sycophancie.

## Ta source
Le rapport d'un lecteur neuf qui a lu les travaux publics du mentor sur leurs pages primaires : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-ibrahim-v1.md` — lis sa section des sources et ses tableaux de faits. **Ce rapport juge aussi la réponse de Lazar et la réécrit : rien de cela ne passe dans ta pièce.**

## Ce que tu écris
`/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-ibrahim-v1.md` : **les faits publics** qui servent à répondre à cette question, et rien d'autre.
- Section 1 : ce que fait le mentor (papiers, billets, jeux de données, code), chaque fait avec son identifiant (arXiv, DOI, LessWrong…), sa date et la page ou la section que le rapport cite ; ce qu'ils disent eux-mêmes ne pas avoir fait (limites déclarées).
- Section 2 : la littérature voisine que le rapport a lue sur page primaire (même format).
- Section 3 : les modèles et données publiés utilisables pour une première expérience (points de contrôle à persona publiés, jeux d'évaluation de la sycophancie, validations humaines des juges), avec leur identifiant.
- Section finale « Limites de la pièce » : ce que le rapport n'a pas pu lire.
**Interdits dans la pièce** : toute mention de la réponse de Lazar, de sa candidature, de ses choix, de ses erreurs ou des corrections du rapport ; toute phrase en anglais à recopier ; toute recommandation (« il faudrait… ») ; tout chiffre sans sa source. Les résultats publics de Lazar (dépôts `lciric/sycophancy-psychophysical-law`, `lciric/sycophancy-construct-validity`, `lciric/ideation-organism`) sont servis à part : ne les répète pas, sauf un fait du mentor qui les touche directement. Au plus 12 000 caractères.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; `WebFetch` seulement pour revérifier un chiffre douteux du rapport sur sa page primaire.

## Rendu
Réponse finale : le chemin et le sha256 de la pièce, son nombre de caractères, et une ligne par fait du rapport que tu as écarté parce qu'il portait sur la réponse de Lazar.
