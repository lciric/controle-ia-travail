Tu es un **groupeur neuf**, aveugle au classement. Travail en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 15 minutes.

## Contexte
Un mentor (Jérémy Scheurer, Apollo Research : évaluations de schémas trompeurs, surveillance) demande une proposition de recherche pour obtenir une **tendance d'échelle** d'un comportement désaligné ou d'une capacité de surveillance (à la manière de l'horizon des tâches de METR) : un énoncé du type « croît ou décroît d'un facteur X par mois ou par an », avec un dispositif qui a des chances de réussir. Le fichier contient des fiches d'idées.

## Entrée (lecture seule)
`/home/claude/scratch/soir-rapport/scheurer/piste/fiches-a-grouper-v1.json` (sha256 `9bae335ec593d5e0cd7a8431dfdf7ef3cd7ce1ca68caa6b7c15cd50788c3ef1b`) : pour chaque fiche, `id`, `enonce`, `mecanisme`. Vérifie l'empreinte avant de lire.

## Ce que tu fais
1. **D'abord, avant toute affectation**, écris les groupes : 3 à 6 **tendances proposées (la quantité tracée et pourquoi elle aurait une tendance mesurable)** distincts. Pour chacun : un nom court, une définition en deux lignes, et le critère qui dit si une fiche en relève.
2. Puis affecte **chaque fiche à un seul groupe** (son idée principale), avec une raison en une ligne ; « second choix » si une fiche relève presque autant d'un autre groupe. Aucune fiche hors groupe.
3. Ne change pas les définitions après coup ; note toute tension dans une rubrique « limites ».

## Ce que tu écris (fichiers neufs, dossier `/home/claude/scratch/soir-rapport/scheurer/piste/`)
- `groupes-v1.json` : `{"groupes": [{"nom", "definition", "critere"}], "affectations": [{"id", "groupe", "raison", "second_choix"}]}`.
- `groupes-v1.md` : les définitions (avec l'heure à laquelle tu les as écrites), le tableau des affectations, les limites.

## Interdits
Ne lis rien d'autre que le fichier d'entrée (surtout pas `classement-D/`, `moisson-C/`, `prep-v1/`, `lecteur-A/`, ni `/home/claude/coffre-*`). Aucun commit, aucun `.sha256`, aucun fichier existant modifié, aucun appel réseau ni de modèle, aucun `git`. `nice -n 10` pour tout script.

## Rendu
Réponse finale : les groupes (nom et définition en une ligne), le nombre de fiches par groupe, les fiches à second choix, les limites ; chemins et sha256 des deux fichiers.
