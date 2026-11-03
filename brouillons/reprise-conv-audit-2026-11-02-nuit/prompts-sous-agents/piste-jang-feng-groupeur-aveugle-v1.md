Tu es un **groupeur neuf**, aveugle au classement. Travail en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 15 minutes.

## Contexte
Deux mentors (Shi Feng et Eyon Jang) demandent : que valent les moniteurs et les méthodes d'audit en boîte blanche (lecture des activations, sondes, autoencodeurs épars), et quelles sont leurs limites actuelles ? Le fichier contient des fiches d'idées.

## Entrée (lecture seule)
`/home/claude/scratch/soir-rapport/jang-feng/piste/fiches-a-grouper-v1.json` (sha256 `ffa495ee97c3cd0afca35cc109c57a5914cc08da325506b0ad10399e658ff944`) : pour chaque fiche, `id`, `enonce`, `mecanisme`. Vérifie l'empreinte avant de lire.

## Ce que tu fais
1. **D'abord, avant toute affectation**, écris les groupes : 3 à 6 **affirmations sur la valeur ou les limites (ce que la réponse soutiendrait)** distinctes, par mécanisme. Pour chacune : un nom court, une définition en deux lignes, et le critère qui dit si une fiche en relève.
2. Puis affecte **chaque fiche à un seul groupe** (son idée principale), avec une raison en une ligne ; « second choix » si une fiche relève presque autant d'un autre groupe. Aucune fiche hors groupe.
3. Ne change pas les définitions après coup ; note toute tension dans une rubrique « limites ».

## Ce que tu écris (fichiers neufs, dossier `/home/claude/scratch/soir-rapport/jang-feng/piste/`)
- `groupes-v1.json` : `{"groupes": [{"nom", "definition", "critere"}], "affectations": [{"id", "groupe", "raison", "second_choix"}]}`.
- `groupes-v1.md` : les définitions (avec l'heure à laquelle tu les as écrites), le tableau des affectations, les limites.

## Interdits
Ne lis rien d'autre que le fichier d'entrée (surtout pas `classement-D/`, `moisson-C/`, `prep-v1/`, `lecteur-A/`, `source-2/`, ni `/home/claude/coffre-*`). Aucun commit, aucun `.sha256`, aucun fichier existant modifié, aucun appel réseau ni de modèle, aucun `git`. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.

## Rendu
Réponse finale : les groupes (nom et définition en une ligne), le nombre de fiches par groupe, les fiches à second choix, les limites ; chemins et sha256 des deux fichiers.
