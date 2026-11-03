Tu es un **groupeur neuf**, aveugle au classement. Travail en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 15 minutes.

## Contexte
Une mentore (Lujain Ibrahim : entraînement de caractère, sycophantie, apprentissage par renforcement) demande de choisir l'un de ses deux projets et de décrire la première expérience : ce qu'on entraîne ou mesure, le résultat attendu, et une chose qui rendrait le résultat trompeur. Le fichier contient des fiches d'idées d'expériences.

## Entrée (lecture seule)
`/home/claude/scratch/soir-rapport/ibrahim-q1/piste/fiches-a-grouper-ensemble-v1.json` (sha256 `e3afb86950d457411d1d989635ed63ebb5ea34b6264bc1b30a172ad1dc267c81`) : pour chaque fiche, `id`, `enonce`, `mecanisme`. Vérifie l'empreinte avant de lire.

## Ce que tu fais
1. **D'abord, avant toute affectation**, écris les groupes : 3 à 6 **types d'expérience (la question que la première expérience tranche)** distincts. Pour chacun : un nom court, une définition en deux lignes, et le critère qui dit si une fiche en relève.
2. Puis affecte **chaque fiche à un seul groupe** (son idée principale), avec une raison en une ligne ; « second choix » si une fiche relève presque autant d'un autre groupe. Aucune fiche hors groupe.
3. Ne change pas les définitions après coup ; note toute tension dans une rubrique « limites ».

## Ce que tu écris (fichiers neufs, dossier `/home/claude/scratch/soir-rapport/ibrahim-q1/piste/`)
- `groupes-ensemble-v1.json` : `{"groupes": [{"nom", "definition", "critere"}], "affectations": [{"id", "groupe", "raison", "second_choix"}]}`.
- `groupes-ensemble-v1.md` : les définitions (avec l'heure à laquelle tu les as écrites), le tableau des affectations, les limites.

## Interdits
Ne lis rien d'autre que le fichier d'entrée (ni `groupes-v1.*`, groupement précédent d'une partie de ces fiches ; surtout pas `classement-D/`, `moisson-C/`, `prep-v1/`, `lecteur-A/`, ni `/home/claude/coffre-*`). Aucun commit, aucun `.sha256`, aucun fichier existant modifié, aucun appel réseau ni de modèle, aucun `git`. `nice -n 10` pour tout script.

## Rendu
Réponse finale : les groupes (nom et définition en une ligne), le nombre de fiches par groupe, les fiches à second choix, les limites ; chemins et sha256 des deux fichiers.
