# Contre-lecture de la version 10 du script de copie expurgée (autre projet, copies par identifiant, noms voisins)

Date : 18 novembre 2026. Contre-lecteur neuf (R2), d'une autre lignée que le rédacteur de la version 10 ; je n'ai écrit ni la version 9 ni la version 10.
Méthode : lecture du code et des essais contre la version 9, rejeu des essais, treize sondes de ma main sur des dépôts factices, examen de la liste réelle par les noms, les identifiants d'objet git et les tailles seulement, mode à blanc sur un clone jetable. Aucun contenu d'un chemin retiré par nom ou sous embargo n'a été ouvert. Aucune régénération, aucune poussée, aucun commit de ma main.

## Verdict : bon — aucun bloquant ; deux défauts mineurs corrigés dans une version 11

La version 10 ne laisse sortir aucun nom sensible ni aucune copie d'un fichier sensible que j'aie su construire ou trouver. Ses essais jugent bien ce qu'ils disent juger. Deux défauts mineurs, sans effet sur ce qui est retiré ou gardé, sont corrigés dans la version 11 (la version 10 intacte). La version 10 peut faire foi telle quelle si la mère ne veut pas de la version 11.

Ce verdict porte sur les retraits par nom et par identifiant. Il ne dit rien du contenu des fichiers gardés : voir « Ce qui reste », points 1 et 2, qui pèsent plus lourd que tout le reste de ce rapport.

Pièces lues (empreintes vérifiées par `controle_ia.scellement verifier`) :
- `scripts/depot_expurge_v9.py` — fd1a5ce6568c… ; `tests/test_depot_expurge_v9.py` — abf57c8e2789…
- `scripts/depot_expurge_v10.py` — 4705af89bb3c125d93d64fda20c9b4896416d1575aef2461a209bc77f95aa2c7
- `tests/test_depot_expurge_v10.py` — b2bc7a23c1a896af40230d0209f4d452d101213c54f7a21121082d748299a1e2
- `docs/notes/copie-publique-v8/contre-lecture-depot-expurge-v8-v1.md` — d4fbcb140f97…

Pièces produites :
- `scripts/depot_expurge_v11.py` — 86afc00653bcacdfbc5c19598883c42166118442731f797b7e3dab4a4b85c20a (scellé ; 29 lignes de différence avec la version 10)
- `tests/test_depot_expurge_v11.py` — f9489a0ea6c8b030a7f6910117108cdfec23d9d9a46f4092ce0bdecd6f3d9763 (scellé)
- Sorties du mode à blanc (commit 608cf281, comptes seulement), dans `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/expurge-v10/` : `contre-lecture-a-blanc-v9.json` — 660bdedaea67… ; `contre-lecture-a-blanc-v10.json` et `contre-lecture-a-blanc-v11.json` — ab05d1e6cd42… (identiques).

## Ce que j'ai cherché, et ce que j'ai trouvé

### 1. Un nom sensible qui passe encore : aucun
- Recherche écrite à part du script (formes larges, zéro à trois caractères entre les mots, accents ôtés) sur l'arbre réel : 1075 chemins portent un nom des familles retirées, de l'autre projet, des brouillons privés ou de l'embargo. Tous sont retirés par nom ou sous embargo, sauf les deux chemins déjà signalés (la proposition P-013 et son compagnon).
- Les fragments de l'embargo, lus sous la normalisation de la version 9 (tiret bas, casse) : aucun chemin gardé.
- Les fragments ajoutés retirent 80 chemins : le dossier du saboteur à budget (40) et la consigne de sa conception (2), la proposition P-066 et son compagnon (2), l'affinage de l'équipe rouge v1 (16) et v2 (18), le brief de la session de l'attaquant informé et son compagnon (2). Je n'en vois aucun retiré à tort.
- Premier dossier écrit avec une majuscule, fichier à la racine, nom sous `prereg/` ou `registres/` : arrêt, dans les deux modes (sondes rejouées).

### 2. La règle sur les identifiants d'objet git : elle tient
- Vérification indépendante sur l'arbre réel : 1033 identifiants de fichiers au nom retiré (objet vide exclu) ; 3 fichiers au nom anodin les partagent ; les 3 sont retirés comme copies ; aucun n'est gardé.
- Sondes : une copie d'un fichier sensible arrête, y compris quand le même contenu existe aussi sous un retrait ordinaire (classe mixte), et quand la copie est sous `registres/` (retrait avec liste). Une copie dans une archive gardée arrête en mode réel pour les trois classes, l'embargo compris. Un lien symbolique vers un fichier sensible n'est pas copié.
- Le chemin nommé dans la liste explicite : son identifiant est celui d'un fichier retiré à titre permanent, l'objet fait 103 octets (64 + 2 + 36 + 1 : une empreinte, deux espaces, un nom de 36 caractères, un saut de ligne), et le fichier dont il est le compagnon est l'objet vide. La lecture du rédacteur est cohérente avec ces trois mesures ; je n'ai pas ouvert le fichier.
- La justification écrite (une copie d'un fichier sensible sous un nom anodin signale un trou du filtre par nom ; la retirer en silence le cacherait) est juste, et la règle fait ce qu'elle dit.

### 3. Un essai toujours vert : aucun, une réserve
- L'essai de la liste réelle sur l'autre projet et celui de la version 9 sur les variantes (qui couvre maintenant les dix-huit fragments) jugent avec une forme de recherche écrite à part, pas avec la fonction qui filtre.
- Réserve : l'essai de l'arbre réel sur les copies par identifiant juge avec la fonction même du script. Ma vérification indépendante (point 2) donne le même résultat ; un essai indépendant de ce genre manque au jeu d'essais.

### 4. Un repli silencieux : deux défauts mineurs, corrigés en version 11
- **Copies retirées sans que personne puisse les voir.** La version 10 retire les copies d'un retrait ordinaire avec un compte, et ne les nomme nulle part, pas même sur le poste de travail. Sonde : une copie posée sous `src/` ou `tests/` disparaît de la copie publique, code 0, aucun nom. Sur l'arbre réel, c'est ainsi qu'une sortie de 3 octets de la course de conception propre et son compagnon sont retirés (voir « Peut-être retirés à tort »). Version 11 : les noms des copies retirées sont écrits sur la sortie d'erreur locale, dans les deux modes ; ni `EXPURGE.md` ni le bilan ne les nomment. Ce sont des noms que le filtre aurait gardés.
- **Membre d'archive au nom de l'autre projet, des brouillons privés ou de l'embargo, lu avant l'arrêt.** La version 9 avait corrigé ce point pour les seuls noms sensibles. Sonde : le contenu du membre est lu (empreinte, gardes), puis le script arrête. Rien ne sort, mais « contenu jamais lu » n'est pas tenu. Version 11 : ces noms arrêtent avant toute lecture de l'archive ; le message donne l'archive et un compte.

## Essais rejoués
- Version 9 : 87 passés, 1 échoué (l'essai hérité sur les noms du dépôt réel). Version 10 : 125 passés, 0 échoué. Chiffres du rédacteur confirmés.
- Version 11 : 131 passés, 0 échoué. Ce sont les 125 de la version 10 (trois adaptés : un membre d'archive au nom retiré par nom ou sous embargo arrête avant lecture au lieu d'être rendu dans la liste des survivants), plus 6 essais neufs (membre de l'autre projet, des brouillons privés, de l'embargo, jamais lus, avec un voisin sain ; noms des copies sur la sortie d'erreur seulement ; rien sur la sortie d'erreur sans copie).
- Mes treize sondes sont dans `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/contre-v10/test_sondes.py` (non versées au dépôt).

## Mode à blanc (clone jetable, commit 608cf281, 28058 chemins ; version 9, puis versions 10 et 11, identiques)
- Fichiers gardés : 23952, puis 23829. Retraits permanents : 371, puis 451. Autre projet : 238, puis 278. Copies retirées par identifiant : 3. Copies qui arrêtent : 0.
- Chemins gardés portant un nom retiré non prévu : 36, puis 0. Chemins sensibles hors des dossiers visés : 0. Archives gardées : 78, toutes examinées, aucun membre qui arrêterait.
- Verdict à blanc : version 9 « arrêt » ; versions 10 et 11 « les gardes de nom passeraient (gardes de contenu non jouées) ».
- Les chiffres du rédacteur (commit 02c81702) sont les mêmes, à 57 fichiers gardés près, ajoutés depuis par les commits de la mère.

## Peut-être retirés à tort (noms seulement ; je n'ai rien exempté)
- `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-refusees.json` et son compagnon. L'objet fait 3 octets et se trouve aussi dans la course de l'autre projet ; le compagnon est lui-même identique à un compagnon de cette course. Coïncidence d'une sortie vide, à mon avis ; la pièce est a priori publiable. À trancher par la mère ou Lazar. Je déconseille un seuil de taille général : un petit fichier d'un dossier sensible peut être parlant.
- Fragments ajoutés : aucun.

## Ce qui reste, et qui n'est pas du code mineur

1. **Le script, ses essais et ces notes nomment en clair ce qu'ils retirent, et seraient publiés.** Sont gardés par le filtre : `scripts/depot_expurge_v7.py` à `v11.py`, `tests/test_depot_expurge_v7.py` à `v11.py`, ce rapport et celui de la version 8, et cinq pièces de `docs/notes/copie-publique-v1/`. Les essais citent les chemins réels du saboteur à budget, de la proposition P-066, de l'affinage de l'équipe rouge, du brief de l'attaquant informé et de la course de l'autre projet ; le script porte la liste des fragments et le chemin de la liste explicite. Le nom d'un dossier retiré est déjà une information. À décider avant toute régénération : retirer ces pièces de la copie, ou publier un script dont les listes sont lues dans un fichier privé.
2. **Le contenu des fichiers gardés.** Le nœud des 672 fichiers reste entier, et les noms ajoutés l'élargissent : 989 fichiers gardés citent au moins un des noms neufs — « saboteur » 870 (docs 386, brouillons 213, prereg 93, tests 56, livrables 48, src 39), équipe rouge 128, attaquant informé 38, proposition P-066 22, autre projet 18, affinage de l'équipe rouge 16, brief de l'attaquant informé 10, saboteur à budget 8. Le mot « saboteur » court tout le programme : retirer ses noms de dossier sans décider du contenu ne protège presque rien.
3. **Une empreinte d'un fichier sensible dans un fichier gardé passe.** Sonde : un compagnon gardé, de nom différent, qui porte l'empreinte SHA-256 d'un fichier sensible n'est pas vu (seuls les objets identiques le sont). Un manifeste ou une liste d'empreintes gardés peuvent donc publier des empreintes de fichiers retirés « sans empreinte ». Le vérifier demanderait de lire les fichiers retirés ; c'est une décision, pas une retouche.
4. **Le mode à blanc ne voit pas une copie dans une archive gardée** (sonde : code 0 pour les trois classes, là où le mode réel arrête). Le rédacteur l'a dit ; je le confirme. Un verdict à blanc favorable ne vaut pas feu vert.
5. **Noms voisins gardés, hors de toute liste** (noms seulement, à trancher ; je n'ai rien ajouté) :
   - sous `docs/notes/organisme-idees-juge-v1/`, `docs/notes/ideation-organisme-v1/` et `src/controle_ia/organisme_idees_juge/` : 461 chemins au nom d'attaques contre le juge de l'organisme d'idéation (sorties d'attaque, attaque de Goodhart, attaque universelle, attaque libre, attaque par projection, attaque sur la confiance, coffre d'attaques inédites, bancs d'attaque, banc de tricheurs) ; c'est le second terrain du papier C, revendiqué, mais ce sont des attaques décrites ;
   - `docs/decisions/proposition-P-041-organisme-coevolutif-attaque-defense-v1.md` à `-v3.md` et compagnons ;
   - sous `docs/sources/lecture-pdf-niveau2/` : six chemins de rapports de lecture sur l'évasion des sondes et l'évasion d'un quorum, trois sur le sabotage de la recherche ;
   - `prereg/audit-rappel-oracle-sabotages-connus-v1-brouillon1.md` et compagnon ; `src/controle_ia/t07bbis/adversaires_texte_v1.py` et son essai ; trois fichiers `dissimulation-v2.jsonl` sous `brouillons/t07-jeux-synthetiques-v2-brouillon1/`.
6. La liste explicite lie un chemin, pas un identifiant : si ce chemin devenait la copie d'un autre fichier sensible, il serait retiré sans arrêt. Sens sûr, mais le regard humain consigné ne vaudrait plus. Lier le chemin à l'identifiant publierait cet identifiant dans le script ; à peser avec le point 1.
7. Deux identifiants de fichiers retirés ont 16 octets ou moins (3 octets, autre projet ; 5 octets, famille sensible). Tout fichier gardé de même contenu que le second arrêtera le script : sens sûr, mais arrêts à prévoir.
8. Limites héritées, inchangées : tar d'ancien format et conteneurs non reconnus non examinés ; arbre partiel laissé dans la sortie à l'arrêt ; noms sensibles imprimés sur la sortie d'erreur locale par le message « hors des dossiers visés » ; formes fléchies filtrées par avance sans épreuve sur le réel.
9. La version 11 est de ma main : elle n'a pas été contre-lue. Sa différence avec la version 10 tient en 29 lignes.

## Note de dépôt
Pendant cette contre-lecture, un commit de la mère (« Pièces des agents en cours », d2556a16) a pris `scripts/depot_expurge_v11.py` et `tests/test_depot_expurge_v11.py` dans leur état scellé. Leurs compagnons `.sha256`, ceux de la version 10 et ce rapport ne sont pas commités.
