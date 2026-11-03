Tu es un **groupeur neuf**, aveugle au classement. Travail en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 20 minutes.

## Contexte
Un mentor (Jan Hendrik Kirchner, auteur d'un article sur des chercheurs d'alignement automatiques qui grimpent un classement, avec un moniteur de triche, un banc tenu à l'écart et Petri) demande : « choisis un problème ouvert de l'alignement que tu crois sous-estimé ; quelle expérience ferais-tu d'abord, et quel résultat te ferait changer d'avis ? ». Le fichier ci-dessous contient 29 fiches d'idées. (Un groupement précédent, sur une partie de ces fiches, existe dans le même dossier : tu ne le lis pas.)

## Entrée (lecture seule)
`/home/claude/scratch/kirchner-rapport/piste-kirchner/fiches-a-grouper-v2.json` (sha256 `8c420b0828f2318777bed98c117536d9ba072191dfe9e8b0279b64fd815b9f24`) : pour chaque fiche, `id`, `enonce`, `mecanisme`, `premiere_experience` (tronquée). Vérifie l'empreinte avant de lire.

## Ce que tu fais
1. **D'abord, avant toute affectation**, écris les groupes : 3 à 6 **problèmes sous-estimés** distincts (ce qui, dans la recherche d'alignement automatisée ou sa sélection, fait passer pour un progrès ce qui n'en est pas, ou cache ce qui en est un). Pour chacun : un nom court, une définition en deux lignes, et le critère qui dit si une fiche en relève. Un groupe = un problème, pas une méthode de mesure.
2. Puis affecte **chaque fiche à un seul groupe**, celui de son problème principal, avec une raison en une ligne ; « second choix » si une fiche relève presque autant d'un autre groupe. Aucune fiche hors groupe.
3. Ne change pas les définitions après coup ; note toute tension dans une rubrique « limites ».

## Ce que tu écris (fichiers neufs, dossier `/home/claude/scratch/kirchner-rapport/piste-kirchner/`)
- `groupes-problemes-v2.json` : `{"groupes": [{"nom", "definition", "critere"}], "affectations": [{"id", "groupe", "raison", "second_choix"}]}`.
- `groupes-problemes-v2.md` : les définitions (avec l'heure à laquelle tu les as écrites), le tableau des affectations, les limites.

## Interdits
Ne lis rien d'autre que le fichier d'entrée (ni `groupes-problemes-v1.*` ni `choix-piste-v1.json`) : surtout pas `/home/claude/scratch/kirchner-rapport/classement-D/`, `moisson-C/`, `melange-v1/`, `lecteur-A/`, ni `/home/claude/coffre-*`. Aucun commit, aucun `.sha256`, aucun fichier existant modifié, aucun appel réseau ni de modèle, aucun `git`. `nice -n 10` pour tout script.

## Rendu
Réponse finale : les groupes (nom et définition en une ligne), le nombre de fiches par groupe, les fiches à second choix, les limites ; chemins et sha256 des deux fichiers.
