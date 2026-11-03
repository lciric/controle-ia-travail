Tu es un **juge neuf, aveugle au classement** : tu n'as écrit ni la réponse de Lazar Ciric à Shi Feng et Eyon Jang, ni les fiches d'idées, ni les groupes, et tu ne sais pas quel groupe la règle de piste retiendra. Français, sans sigle non développé ; toute heure vient de `date -u`. Vise 10 minutes.

## Ce que tu lis (vérifie chaque empreinte avant de lire)
- La réponse (anglais ; le texte au-dessus de la ligne `---` seulement) : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/jang-feng/reponse-v4.md` (sha256 `6c9277b0912a24c4e229afa23699b437469196a8694bb8d0030f8b63e2d29cae`).
- Les définitions des six groupes d'idées, écrites par un groupeur aveugle : `/home/claude/scratch/soir-rapport/jang-feng/piste/groupes-v1.json` (sha256 `ca887d0f6127796e6dcf186930053dc0123d693ef33a567360b8fbe4648a8dff`) : lis **seulement** la liste `groupes` (nom, définition, critère) ; ignore les affectations des fiches.

## Ce que tu fais
1. Écris d'abord, en deux lignes, **l'argument principal de la réponse** : l'affirmation sur la valeur ou les limites de la boîte blanche que la réponse défend en premier et à laquelle elle consacre le plus de place, avec son mécanisme.
2. Dis **à quel groupe unique** cet argument principal appartient, par le critère du groupe ; donne un **second choix** s'il relève presque autant d'un autre groupe, et la raison de chaque choix en une ou deux lignes.
3. Liste les **arguments secondaires** de la réponse et le groupe de chacun (une ligne chacun).
4. Si l'argument principal ne relève d'aucun groupe, dis-le.

## Ce que tu écris (fichier neuf)
`/home/claude/scratch/soir-rapport/jang-feng/piste/juge-mecanisme-v1.md`.

## Interdits
Ne lis rien d'autre que les deux fichiers ci-dessus (surtout pas `classement-D/`, `moisson-C/`, `prep-v1/`, `lecteur-A/`, `source-2/`, ni les affectations de `groupes-v1.json`, ni `/home/claude/coffre-*`). Aucun commit, aucun `.sha256`, aucun fichier existant modifié, aucun appel réseau ni de modèle, aucun `git`. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.

## Rendu
Réponse finale : l'argument principal en une ligne, son groupe, le second choix, les arguments secondaires et leurs groupes ; chemin et sha256 du fichier.
