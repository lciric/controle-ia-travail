# Vérification du brouillon 2 de l'addendum 1 du plan « sabotage ou empreinte de l'adaptateur » (barreau 5) — v1

Écrite le 20 novembre 2026, de 02:26Z à 02:32Z environ (horloge du conteneur, `date -u`), par le contre-lecteur de l'addendum 1, Claude Opus 5.5 (`claude-opus-5-5`), sous-agent de la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`). Il vérifie les corrections de sa propre contre-lecture, sur demande de la mère ; mêmes règles et mêmes sections du texte scellé que dans son mandat (`c1e3ddc412fcb5f12693f1719affa4874d3ce41f78057a50c71d94d0f3a34d5c`).

## Verdict

**Scellable après ces couples** (huit couples, tous sur le brouillon 2, section « Couples »).

Le brouillon 2 est, vérifié par programme, le brouillon 1 avec mes dix-huit couples, plus les trois lignes déclarées par le rédacteur (le titre, la ligne « Statut », la confiance de la borne), et rien d'autre. Les trois retouches sont justes quant au fond. Les huit couples ne touchent à aucune règle. Ils mettent à jour ce qui, sans eux, serait faux une fois le texte scellé :
- le titre et le statut ;
- cinq phrases qui ne parlaient que des trois points d'origine ;
- la section « Contre-lecture », vide.

## Pièces, empreintes vérifiées avant lecture

- Brouillon 2 : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon2.md`, `580ffd4d10f2c119b2892bcdbaca786044a6ce29d77023ca69753ff9b660df07`, lu en entier. Fichier daté de 02:25:01Z, versé au commit `e46d1f5d3` (02:25:56Z).
- Table des couples du rédacteur : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/table-couples-addendum-1-brouillon2-v1.md`, `8ff9485fdd11624d391394925a8a9c982229ec2d1f1bbc2c93a7184cfd0d6769`, lue en entier.
- Brouillon 1 : `1c7d6e51fb355ab0349b93435bcb404a9bee82f5cb5064be5f4d8640c38632a8`, revérifié.
- Ma contre-lecture : `contre-lecture-addendum-1-v1.md`, `6469c9150e4aa0eba88ac05db8d22feac7d9bf0da9884bbc2c007248b4e5ba95`, sceau revérifié. Les couples y sont lus par programme.

Rien d'autre n'a été ouvert pour cette vérification : aucune section neuve du texte scellé, aucune donnée, rien de `diag/`, aucun fichier « consigne-privee » ni « conception-ii-b », rien sous `/root/.claude/`. Aucun réseau, aucune dépense, aucun commit.

## 1. Le brouillon 2 est le brouillon 1 avec les couples, plus trois lignes

Outil : `outils-contre-lecture-addendum-1-v1/comparer_brouillon2.py`. Il relit les dix-huit couples dans ma contre-lecture et les applique au brouillon 1, chacun exigé unique dans le texte en cours. Il compare ensuite ligne à ligne le texte attendu au brouillon 2 (`difflib`, aucun écart ignoré, espaces compris). Résultat :
- couples appliqués : 18 ;
- empreinte attendue (brouillon 1 et couples) : `5eea025fe9c9353a944837533bbd69ee97205a15a4a6ea27276a24eabc0180c8`, celle que donnait ma contre-lecture et celle que déclare le rédacteur ;
- **trois écarts, chacun d'une ligne remplacée par une ligne, et aucun autre** : l. 1 (titre, « brouillon 1 » devenu « brouillon 2 »), l. 7 (ligne « Statut »), l. 128 (« Ce qui va à Lazar », point 2, « Confiance : 0,8. » devenu « Confiance : 0,85 (0,8 au brouillon 1 ; je suis le contre-lecteur : […]) ») ;
- même fin de fichier des deux côtés.

**Les trois retouches, quant au fond.**
- *Titre* : juste pour un brouillon 2.
- *Confiance 0,85* : c'est la confiance que je donnais, avec ma raison, rendue exactement. Le rédacteur la fait sienne et le dit. Ce n'est ni un critère ni une règle : rien ne change dans ce qui est fixé.
- *Statut* : juste sur la chaîne et les empreintes. Une ambiguïté : « (0,8 devenue 0,85, à la demande de la mère) » peut se lire comme si la mère avait fixé le nombre. La table du rédacteur dit autre chose, et c'est elle qui est exacte : la mère lui a demandé la confiance qu'il tient pour juste. Au candidat au scellement, la ligne est récrite de toute façon (couple V2), et l'ambiguïté part avec elle.

## 2. Les phrases qui datent et la section « Contre-lecture »

**Elles demandent des couples avant le scellement.** Un texte scellé doit être vrai à la date de son sceau. Voici ce qui ne le serait pas.
- *Le titre et la ligne « Statut »* disent « brouillon 2 », « reste vide à ce brouillon » et « Rien n'est gelé par ce brouillon ». Ils ne décrivent pas le texte qui sera scellé : celui-ci est le brouillon 2 avec les couples de cette vérification (couples V1 et V2).
- *Les phrases qui ne parlent que des trois points d'origine.* Le rédacteur en nomme trois ; j'en trouve cinq.
  - L. 19 (« Exposition déclarée ») : « aucune des trois règles ci-dessous n'en dépend » ne couvre pas les deux règles entrées à la contre-lecture (couple V3).
  - L. 23 : la déclaration « Aucune donnée n'a inspiré ces règles » ne nomme pas la source des deux règles entrées (couple V4). C'est la plus importante : la déclaration d'absence de donnée doit couvrir tout ce que l'addendum fixe.
  - L. 61 (point 1, « Aucune donnée ») : « La règle vient des trois passages cités et de la question 2.1 (4) » ne couvre pas la règle 4 ni les familles présentes de M1 et de M3 (couple V5).
  - L. 125 : « Les trois points sont fixés sans toucher […] » (couple V6).
  - L. 133 : « Si la contre-lecture trouve qu'une des trois règles change l'un d'eux » est au futur ; la contre-lecture est faite (couple V7).
- *La section « Contre-lecture »* est vide. Le texte scellé doit nommer sa chaîne : la contre-lecture, son empreinte et son verdict, puis la vérification et son verdict (couple V8). La vérification ne peut pas porter sa propre empreinte dans un couple : elle est nommée par son chemin, et son empreinte est dans son compagnon `.sha256`, que la mère recopie au registre.

**Laissé tel quel.** La ligne « Portée » (l. 4) dit « Il fixe trois points » : c'est vrai de la structure, puisque les deux règles entrées sont au point 1, et la même ligne les nomme déjà. « Trois choses lui sont dites » (l. 125) reste vrai : la liste a trois entrées.

**Le nom du fichier scellé** revient à la mère (R12 : une version neuve, un nom neuf). Le texte ne dépend pas de ce nom : il se nomme « candidat au scellement ».

## Couples

Huit couples, tous sur le brouillon 2, dans l'ordre du fichier. Chaque « avant » doit être trouvé une seule fois, dans le brouillon 2 et dans le texte en cours d'application : vérifié par `verifier_couples.py` (résultat plus bas).

### Couple V1 — titre
- Fichier : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon2.md`
- Avant :
````text
l'empreinte de l'adaptateur ? » — brouillon 2
````
- Après :
````text
l'empreinte de l'adaptateur ? » — candidat au scellement
````

### Couple V2 — statut
- Fichier : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon2.md`
- Avant :
````text
- **Statut** : brouillon 2, pièce décisive (classe A), écrit le 20 novembre 2026 vers 02:25Z (horloge du conteneur) par le même rédacteur. C'est le brouillon 1 (`1c7d6e51fb355ab0349b93435bcb404a9bee82f5cb5064be5f4d8640c38632a8`) auquel sont appliqués, à la lettre et dans l'ordre, par le programme du contre-lecteur, les dix-huit couples de la contre-lecture `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/contre-lecture-addendum-1-v1.md`, sha256 `6469c9150e4aa0eba88ac05db8d22feac7d9bf0da9884bbc2c007248b4e5ba95` (Claude Opus 5.5 ; verdict : « scellable après ces couples »). État après les seuls couples : `5eea025fe9c9353a944837533bbd69ee97205a15a4a6ea27276a24eabc0180c8`, égal à celui que donne la contre-lecture. Seuls ses couples sont appliqués ; s'y ajoutent trois retouches, et rien d'autre : le mot « brouillon 2 » du titre, cette ligne de statut, et la confiance du point 3 devant Lazar (0,8 devenue 0,85, à la demande de la mère). Table : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/table-couples-addendum-1-brouillon2-v1.md`. La section « Contre-lecture », en fin de pièce, reste vide à ce brouillon : elle se remplit au candidat au scellement. Chaîne : vérification des corrections par le même contre-lecteur, scellement sur le mot de Lazar. Rien n'est gelé par ce brouillon.
````
- Après :
````text
- **Statut** : candidat au scellement, pièce décisive (classe A). Chaîne, dans l'ordre : le brouillon 1 (`1c7d6e51fb355ab0349b93435bcb404a9bee82f5cb5064be5f4d8640c38632a8`) ; les dix-huit couples de la contre-lecture `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/contre-lecture-addendum-1-v1.md`, sha256 `6469c9150e4aa0eba88ac05db8d22feac7d9bf0da9884bbc2c007248b4e5ba95` (Claude Opus 5.5 ; verdict : « scellable après ces couples »), appliqués à la lettre et dans l'ordre par le programme du contre-lecteur (état après les seuls couples : `5eea025fe9c9353a944837533bbd69ee97205a15a4a6ea27276a24eabc0180c8`) ; le brouillon 2, `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon2.md`, sha256 `580ffd4d10f2c119b2892bcdbaca786044a6ce29d77023ca69753ff9b660df07`, écrit le 20 novembre 2026 vers 02:25Z (horloge du conteneur) par le même rédacteur, qui y ajoute trois retouches et rien d'autre : le titre, la ligne de statut, et la confiance du point 3 devant Lazar, 0,8 devenue 0,85, que le rédacteur tient pour juste quand la mère la lui demande (table : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/table-couples-addendum-1-brouillon2-v1.md`, sha256 `8ff9485fdd11624d391394925a8a9c982229ec2d1f1bbc2c93a7184cfd0d6769`) ; la vérification du brouillon 2 par le même contre-lecteur, `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/verification-addendum-1-brouillon2-v1.md` (empreinte dans son compagnon `.sha256` ; verdict : « scellable après ces couples »), dont les huit couples font ce texte. Scellement sur le mot de Lazar ; rien n'est gelé avant.
````

### Couple V3 — l'exposition, pour les règles entrées
- Fichier : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon2.md`
- Avant :
````text
aucune des trois règles ci-dessous n'en dépend.
````
- Après :
````text
aucune des trois règles ci-dessous n'en dépend. La contre-lecture, qui n'a pas lu ces lignes, juge de même sur cette description, pour les trois règles et pour les deux qu'elle a fait entrer au point 1.
````

### Couple V4 — « Aucune donnée n'a inspiré ces règles », pour tout ce qui est fixé
- Fichier : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon2.md`
- Avant :
````text
les trois règles sont tirées du texte scellé, du rapport et de la contre-lecture, qui ne portent que sur un modèle jouet et des fichiers fabriqués.
````
- Après :
````text
les règles des trois points sont tirées du texte scellé, du rapport et de la contre-lecture du code, qui ne portent que sur un modèle jouet et des fichiers fabriqués. Les deux règles entrées à la contre-lecture de cet addendum (règle 4 et familles présentes de M1 et de M3, au point 1) le sont du texte scellé et de la même contre-lecture du code ; la contre-lecture de cet addendum et sa vérification n'ont lu aucune donnée.
````

### Couple V5 — les sources de la règle du point 1
- Fichier : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon2.md`
- Avant :
````text
La règle vient des trois passages cités et de la question 2.1 (4) du développeur.
````
- Après :
````text
Les règles 1 à 3 viennent des trois passages cités et de la question 2.1 (4) du développeur ; la règle 4 et les familles présentes de M1 et de M3, entrées à la contre-lecture, viennent de « Seuil », du point 13 de la liste d'arrêt, du point 17 et des constats m-4 et M-2 de la contre-lecture du code.
````

### Couple V6 — « Les trois points sont fixés »
- Fichier : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon2.md`
- Avant :
````text
Les trois points sont fixés sans toucher
````
- Après :
````text
Les trois points, avec les deux règles entrées à la contre-lecture au point 1, sont fixés sans toucher
````

### Couple V7 — la contre-lecture est faite
- Fichier : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon2.md`
- Avant :
````text
Si la contre-lecture trouve qu'une des trois règles change l'un d'eux, la règle est retirée de l'addendum et portée à Lazar comme question.
````
- Après :
````text
Ni la contre-lecture ni la vérification du brouillon 2 n'ont trouvé une règle de cet addendum qui en change un. Si l'une en changeait un, elle serait retirée de l'addendum et portée à Lazar comme question.
````

### Couple V8 — la section « Contre-lecture »
- Fichier : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon2.md`
- Avant :
````text
## Contre-lecture
````
- Après :
````text
## Contre-lecture

- **Contre-lecture du brouillon 1**, par Claude Opus 5.5, agent neuf, d'un autre modèle que le rédacteur : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/contre-lecture-addendum-1-v1.md`, sha256 `6469c9150e4aa0eba88ac05db8d22feac7d9bf0da9884bbc2c007248b4e5ba95`. Verdict : « scellable après ces couples », dix-huit couples, tous appliqués au brouillon 2. Aucune règle ne change une hypothèse, une prédiction, un seuil, un critère, une épreuve ni la liste d'arrêt ; deux points laissés ouverts entrent au point 1 (le cas m-4 et le constat M-2 de la contre-lecture du code).
- **Vérification des corrections**, par le même contre-lecteur : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/verification-addendum-1-brouillon2-v1.md`, empreinte dans son compagnon `.sha256`. Vérifié par programme : le brouillon 2 est le brouillon 1 avec les dix-huit couples et trois retouches, rien d'autre. Ses huit couples (titre, statut, phrases qui ne parlaient que des trois points d'origine, cette section) font ce texte. Verdict : « scellable après ces couples ».
- **Avis du contre-lecteur sur ce qui va à Lazar** : garder « absente » au cas limite du point 2 ; ½ Δ_app comme borne au point 3.
````

### Vérification des couples par programme

Commande : `.venv/bin/python -B outils-contre-lecture-addendum-1-v1/verifier_couples.py verification-addendum-1-brouillon2-v1.md /home/user/controle-ia-travail <copie de travail>` (chemins entiers à l'appel). Résultat, vers 02:30Z :
- fichier visé : le brouillon 2, sha256 d'origine `580ffd4d10f2c119b2892bcdbaca786044a6ce29d77023ca69753ff9b660df07` ;
- 8 couples trouvés ; pour chacun, « avant » trouvé 1 fois dans l'origine et 1 fois dans le texte en cours d'application, et « après » trouvé 1 fois dans le résultat ;
- « tous les couples s'appliquent » ;
- empreinte du candidat au scellement (brouillon 2 et ces huit couples, copie de travail) : `2afa2186c9f11e0a477cdf628348d2cad3bce90de5933597ff09a4a3048499e4`. Qui écrit le candidat doit retrouver exactement cette empreinte.

Contrôle de reste : dans la copie de travail, les mentions de « brouillon » et de « trois » qui restent sont historiques (« brouillon 1 scellé à 02:02Z », « 0,8 au brouillon 1 », la chaîne du statut) ou justes (« trois raisons », « Trois choses lui sont dites », « Essais du code, pour les trois points », qui comptent la règle 4).

## Errata de ma contre-lecture (pièce scellée, non récrite)

- En-tête : « de 02:06Z à 02:30Z environ ». Lire « de 02:06Z à 02:22Z » : le fichier est daté de 02:22:20Z et son compagnon de 02:22:43Z.
- Section « Vérification des couples par programme » : « vers 02:27Z ». Lire « vers 02:22Z », pour la même raison.
- Ni les couples ni les verdicts ne changent.

## Ce qui menace le gel

- Le candidat au scellement attend le mot de Lazar. Il porte les deux choix (le cas limite, la borne) avec leurs options.
- Les changements de code des points 2 et 3, les commentaires et les essais repassent ensuite par le contre-lecteur du code, avant la ligne `CODE-LECTURE-B5F`. La seconde programmation reçoit le texte scellé, règle 4 comprise.
- Tout changement du candidat au-delà de ces couples, nom de fichier excepté, demande une nouvelle vérification.

## Outils

Dans `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/outils-contre-lecture-addendum-1-v1/` :
- `comparer_brouillon2.py`, neuf : il reconstruit le texte attendu (brouillon 1 et couples de la contre-lecture) et donne chaque écart ligne à ligne avec le brouillon 2 ;
- `verifier_couples.py`, déjà scellé, réemployé sans changement (`2530e0097b09436d3b7e0a9a7ccd1aee35bb9bb9b182550419ff1e7fd0c41051`) : il lit les huit couples dans cette pièce et les applique à une copie de travail du brouillon 2.
