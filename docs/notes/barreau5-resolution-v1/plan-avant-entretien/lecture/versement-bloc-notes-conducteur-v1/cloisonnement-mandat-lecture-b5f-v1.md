# Relecture de cloisonnement — mandat de la session de lecture du barreau 5, v2, et son erratum 1

Relecteur neuf (Opus 5.5), 22 novembre 2026. Seuls fichiers ouverts : les deux pièces ci-dessous.

- `mandat-session-lecture-b5f-v2.md` : `b1eb2afc57d59df9d3a9eab96c22087ebbde6b4cb54824c4b62231ccc9fa991f`, égale à l'attendu et au compagnon.
- `mandat-session-lecture-b5f-v2-erratum-1.md` : `cde0279cad37ed84ef051623269648722308a7629251076d3f354de41a46e510`, égale à l'attendu et au compagnon.

## Verdict : à corriger (corrections mineures, aucune fuite dans le texte)

Les deux pièces ne portent **aucun résultat** : ni score, ni aire, ni statistique d'adaptateur, ni sens d'effet, ni nombre d'adaptateurs rejetés, ni valeur de table ou de sel, ni coût d'un adaptateur tenu à l'écart, ni issue de l'apprentissage des sondes sur la tâche, de la course de confirmation, des sondes génériques ou des organismes. Les chiffres présents sont admis : empreintes, commits, coupures et fourchettes en USD, disques, durées, numéros de lignes, numéros d'instances intouchables, « treize » références git (compte de références, pas une issue), `X-01` à `X-30` et `A1` à `A3` (noms opaques et d'apprentissage, sans rapprochement). Les mentions de résultats sont des mentions d'existence seulement (« elle porte des résultats de l'apprentissage des sondes sur la tâche », l. 64) : elles servent à exclure, sans rien laisser deviner.

Les corrections portent sur des consignes qui **pourraient faire voir** une pièce porteuse ou non vérifiée.

## Constats

1. **Un fichier non relu pour le cloisonnement entre dans la liste « ce que tu lis ».**
   Citation : § 3, point 6 : « le rapport de vérification de ce code (`fca7d949…`), à un chemin que la mère te donne » ; § 10 : « je ne l'ai pas lu, la relecture de cloisonnement doit donc le couvrir » ; erratum, point 3 : « Il vit sur une branche que tu ne récupères pas (`formation-b5f/*`) : le conducteur te le versera, seul, sous un chemin à toi ; tu le vérifies par son empreinte. »
   Risque : la pièce vient d'une branche de la formation, d'un dossier `…/formation/code-commande-lecture-v2/` ; elle n'est couverte ni par la présente relecture (qui ne l'a pas ouverte, sur consigne) ni par le concepteur. Elle peut citer un état de la formation, des comptes, des sorties d'essais. Le mandat la range parmi les pièces lues ; l'erratum dit « vérifies par son empreinte » sans dire « sans la lire ».
   Correction : soit une relecture de cloisonnement de ce rapport par un agent neuf avant son versement, nommée dans l'erratum ; soit écrire « tu en vérifies l'empreinte, tu ne l'ouvres pas » (la session n'a besoin que de l'empreinte, qui figure déjà dans la ligne `GO-LECTURE-B5F`) et retirer « lis » au § 3, point 6.

2. **Lectures partielles sans manière fixée : le fichier entier peut s'afficher.**
   Citations : § 3, point 2 : le texte scellé, « ces sections seulement, par leurs lignes » (le texte porte ailleurs des résultats, l. 64) ; § 3, point 4 : la vérification de l'additif, « remarque 2 » ; § 3, point 5 et § 4, point 4 : le registre propre, « les lignes à clé seulement ».
   Risque : un outil de lecture ordinaire affiche tout le fichier, ou des lignes voisines ; si les numéros de lignes ne tombent pas juste, une ligne de « Ce que le rédacteur savait… » ou de « Prédiction » peut passer. Pour le registre propre, des lignes sans clé (prose, notes) peuvent porter des faits de la formation.
   Correction : imposer l'extraction par commande bornée, par exemple `sed -n '35p;151,179p;217,233p;257p;260,261p;345,434p;436,448p' <texte>` après vérification d'empreinte, et vérifier que la première ligne de chaque tranche est bien le titre de section attendu (sinon arrêt, nœud) ; pour le registre propre, un filtre par programme qui ne rend que les lignes dont la première colonne est l'une des clés nommées au § 4, point 4 ; pour la vérification de l'additif, une extraction par l'intitulé de la remarque 2. Interdire l'outil de lecture de fichier entier sur ces trois pièces.

3. **La suite entière des essais peut afficher des contenus en cas d'échec.**
   Citation : § 4, point 1 : « essais : `python -m pytest -q` » ; erratum, point 4 : « Un essai de la suite entière peut être rouge sur la branche principale (plancher d'essais de l'amorce de **formation**) … tu le signales seulement. »
   Risque : un essai rouge imprime son assertion et ses variables locales ; un essai de la formation peut lire un fichier du dépôt et en montrer des valeurs (comptes, chemins, grandeurs). L'erratum annonce justement un essai rouge de la formation.
   Correction : `python -m pytest -q --tb=no -p no:cacheprovider` (et `-rN`), pour ne voir que les noms et l'état ; ou retirer la suite entière de la routine de la session, qui ne doit rejouer que les quatre fichiers du § 5.1 (ceux-là aussi avec `--tb=line` au plus).

4. **Sortie de la vérification d'arbre : des noms de fichiers peuvent parler.**
   Citation : § 4, point 1 : « `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .` ».
   Risque, faible : si la commande liste les fichiers scellés, des noms de pièces de verdict ou de résultats (sous `diag/`, `docs/verdicts/`, `docs/notes/barreau5-resolution-v1/`) peuvent laisser deviner une issue par leur nom.
   Correction : ne garder que le compte et le code de sortie (`… verifier-arbre . > /dev/null; echo $?`, ou filtrage au seul bilan), et le dire.

5. **Branche des scores fermés : manière d'extraire non fixée.**
   Citation : § 5.4, pas 8 : « Tu récupères cette seule branche, par son nom entier, vers une référence distante » ; § 3, dernier alinéa : n'ouvrir que `traces-b5f-lecture/journal/*` et l'inventaire.
   Risque : une extraction par `git checkout` ou `git worktree add` de cette branche pose les fichiers de scores sur disque, dans l'arbre où la session cherche et lit ; un outil de recherche par motif peut alors les toucher.
   Correction : écrire « jamais de `checkout` ni d'arbre de travail sur cette branche ; extraction par `git show <commit>:<chemin>` des seuls chemins permis, `git ls-tree --name-only` pour lister ». Même règle pour la branche des entrées (§ 2).

6. **« comptes » au journal : contenu non borné.**
   Citation : § 3, dernier alinéa : « `traces-b5f-lecture/journal/*` (étapes et comptes) » ; § 5.4, pas 7.
   Risque, faible : un compte d'adaptateurs refusés, exclus ou en échec par nom opaque se rapprocherait d'une issue. Le § 6 couvre les grandeurs d'adaptateur, pas les comptes.
   Correction : préciser « comptes de fichiers et d'étapes, sans rapprochement à un nom opaque » ; un compte par adaptateur ou par classe : « journal non conforme », arrêt, comme au § 6.

## Hors cloisonnement, signalés en passant

- § 5.3 dit « `CODE-LECTURE-B5F` était inscrite à la fin de la formation » ; § 9, point 3 dit « inscrite avant la fin de la formation ». À accorder.
- La ligne d'engagement du § 5.4, pas 1 garde les fourchettes et coupures du devis (21 et 8 USD) ; l'erratum, point 2 renvoie les coupures au signal (plafond 33 USD). Préciser que les valeurs entre crochets viennent du signal.
- Hors de mon champ : le devis, l'additif 1 v2, sa pièce de scellement et les lignes à clé du registre propre ne sont pas couverts par cette relecture ; s'ils ont été écrits après les sorties de la formation (21 novembre, 14:49Z), leur cloisonnement doit avoir été relu ailleurs.

## Consignes qui feraient ouvrir un fichier porteur

Aucune consigne n'ordonne d'ouvrir un fichier nommément porteur de résultat ; les interdits du § 3 sont larges et justes. Les seules voies d'exposition sont les constats 1 (pièce non relue), 2 (lectures partielles sans manière), 3 (sortie d'essais rouges) et 5 (extraction d'une branche de scores).
