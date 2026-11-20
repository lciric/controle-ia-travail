# Rapport du développeur — masque de style v2 (trois clés hors des dix champs retirées et comptées) — v1

- **Auteur : développeur neuf, modèle O.** Je n'ai écrit ni le masque v1, ni la configuration A v1 ou v2, ni les critères. Écrit le 2026-11-20 (`date -u` : 2026-11-20T10:04:37Z). Python 3.13.18. Processeur seul, aucune dépense, aucun appel de modèle.
- **Mandat** : `mandat-developpeur-masque-v2-v1.md` (`93bc98d61ed3929577bbd0f694b028875c849d6e0c3459d1ed23e9b1bfc52518`, égal à son compagnon).
- **Aucune carte ouverte.** Rien n'a été fait sous `archives-reponses-modeles/`, par aucune commande. Le masque v2 n'a été joué que sur des fichiers synthétiques ; il n'a pas été joué sur les cartes.
- Rien n'est écrit dans le dépôt, aucun commit. Tout est dans mon bloc-notes ; la session verse.

## 1. Ce que j'ai lu (empreintes égales à leur compagnon)

- Masque v1 : `J/criteres-v4/masque_style_cartes_v1.py`, `07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e`.
- Ses essais : `J/criteres-v4/essais_masque_style_cartes_v1.py`, égal à son compagnon (ouvert par son chemin à côté du masque, voir § 7).
- Proposition de la configuration A v2 (`proposition-configuration-a-v2-v1.md`, égale à son compagnon) et la configuration A v2 (`configuration-a-masque-v2.json`, `a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54`).
- Compte rendu du refus (`compte-rendu-masque-et-lecteur-programme-rejeu-v1.md`, égal à son compagnon).
- Tirés de `main` par `fetch` puis `git show FETCH_HEAD:… >` : `registres/go.md` (copie `source-go-main.md`) ; la configuration A v1 (copie `source-configuration-a-masque-v1.json`, `8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4`).

**Les deux lignes de GO, à la lettre** (`registres/go.md` de `main`) :

> GO-2026-11-20-24 | 2026-11-20 | décision | **Juge de sélection, rejeu, option (a) de R-4133.** Un agent neuf, qui ne lit aucune carte, passe le seul fichier `fiches.json` de la course v9 (ba65c411…, sous `archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/`) au masque, puis deux fois au lecteur par programme, selon l'annexe C. Rien n'est affiché ni recopié ; les sorties sont scellées hors du dossier. Troisième exception bornée à la règle de ce dossier.

> GO-2026-11-20-36 | 2026-11-20 | décision | **« go recos » sur les recommandations pendantes de la mère.** (1) Rejeu du juge : les trois clés hors champs masquées, option (a), masque v2 codé, contre-lu, configuration A v2 scellée, masque relancé sous GO-2026-11-20-24. […]

## 2. Fichiers rendus (bloc-notes `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-masque-v2/`)

| fichier | sha256 |
|---|---|
| `masque_style_cartes_v2.py` | `769aace5b64c697799b76a0120a5c2926c75798a388c93fa00ddc93224401c01` |
| `essais_masque_style_cartes_v2.py` | `7c84260f3fabe5ebcf7a9ea8447cf94dd462710755055026a44194282be14b71` |
| `differentiel-masque-v1-v2.diff` | `efb1c82b463be348d2e4b0a212f0136ca17f461375efc04349f92fbbc0fa88ec` |
| `rapport-developpeur-masque-v2-v1.md` | dans son compagnon |

Chacun a son compagnon `F.sha256`. À côté, pour les essais seulement : `masque_style_cartes_v1.py`, copie du v1 à son empreinte (`07ed8725…`, vérifiée par un essai), et les deux copies tirées de `main` (`source-…`).

## 3. Ce qui change, et rien d'autre (le différentiel en entier : `differentiel-masque-v1-v2.diff`)

1. **En-tête de version** : docstring « v2 », avec un paragraphe qui dit la différence ; `VERSION = "masque_style_cartes_v2"` ; la description de la ligne de commande dit « (v2) ». Il n'y avait pas de constante d'empreinte de configuration attendue dans le v1 : aucune n'est ajoutée.
2. **`valider_configuration`** : l'ensemble des clés vaut les sept du v1, ou les sept plus `cles_hors_champs_retirees` ; toute autre clé neuve reste un refus, avec le message du v1. Si la huitième clé est là : objet non vide, noms textes non vides, aucun nom dans `champs` ni égal à `meta` ou `empreinte`, valeurs entières d'au moins 1 (ni booléen, ni flottant, ni texte, ni null). Sinon refus.
3. **`extraire_contenus`** : un paramètre facultatif `retirees` (défaut : aucun, conduite du v1). Pour chaque carte ouverte, la présence de chaque nom est comptée (`nom in contenu`, la valeur n'est pas lue), puis un nouvel objet est fait des seules clés non retirées, **avant** le contrôle « clé hors des champs », qui reste celui du v1 : toute autre clé hors des champs est un refus. Le `contenu` d'origine n'est pas modifié ; aucune valeur d'une clé retirée n'est lue, copiée ni écrite. Après la boucle (et après les refus du v1), **refus si, pour un nom, le nombre de cartes porteuses diffère du nombre attendu** ; le message dit le nom, le nombre trouvé et l'attendu, aucun identifiant.
4. **`main`** : passe `conf.get("cles_hors_champs_retirees")` ; si la clé est là, ajoute **une troisième ligne à `en_tete`** : le compte par clé (vérifié égal à l'attendu), jamais par carte, et l'empreinte de la configuration. Sans la clé, `en_tete` est celui du v1. Aucune autre clé de sortie n'est ajoutée ; `rapport` et `cartes` ont la forme du v1.

La ligne d'en-tête rendue pour la configuration A v2 serait (gabarit, l'empreinte étant celle passée en argument) :

```
Clés de `contenu` hors des champs, retirées sans que leur valeur soit lue ni écrite ; nombre de cartes porteuses par clé (jamais par carte), vérifié égal à l'attendu : "_" : 2 ; "cout_note" : 1 ; "epreuve_hors_ligne" : 1. Configuration : sha256 a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54.
```

## 4. Essais

Lancés hors du dépôt, dans le bloc-notes :

```
env -C /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-masque-v2 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_masque_style_cartes_v2.py
.......................................................                  [100%]
55 passed in 0.20s
```

Premier lancement : 54 réussis, 1 échec, venu de l'essai et non du masque (mon aide de configuration prenait `None` pour « clé absente », si bien que le cas « valeur null » n'était pas posé). Corrigé dans l'essai par un marqueur d'absence distinct ; le masque n'a pas changé entre les deux lancements.

Ce que couvrent les essais (cartes et configurations synthétiques, inventées ; valeurs des clés retirées semées de chaînes repérables, dont des valeurs non textuelles) :
- **Sans la huitième clé, sortie égale au v1** (5 réglages : plafonds fixes, médiane, détection éteinte, carte hors du choix, médiane avec seuil 0,25) : les octets du fichier de sortie du v2 sont égaux à ceux du v1 une fois ramenées les deux seules valeurs qui diffèrent par nature (`"piece"` et l'empreinte du programme, chacune présente une fois) ; `en_tete`, `cartes`, `rapport` égaux ; première ligne de l'écran égale ; aucune sortie d'erreur. Mêmes refus, au message près, que le v1 sur 7 cartes fautives et 10 configurations fautives (dont `_` hors des champs sans la huitième clé, et une clé neuve inconnue).
- **Clé retirée sur le bon nombre de cartes** : code 0 ; les cartes et le rapport rendus sont ceux du v1 sur les mêmes cartes privées des trois clés ; la sortie garde les six clés du v1.
- **Nombre faux** : une carte de plus attendue, une de moins, un excès sur une autre clé, un nom porté par aucune carte, une carte porteuse en plus, une en moins : refus, code 2, rien d'écrit, ni sortie ni compagnon ; chaque fois à côté du cas sain.
- **Une autre clé hors des champs**, la huitième clé présente : refus (le message du v1), code 2, rien d'écrit ; un champ manquant ou non textuel reste aussi un refus.
- **Validation** : nom qui est un champ (seul, ou parmi d'autres), `meta`, `empreinte`, valeurs 0, −1, 1,5, 2,0, vrai, « 2 », null ; nom vide, nom non textuel, objet vide, liste, null : refus ; cas sains avec et sans la clé. Une clé neuve en plus de la huitième, ou un nom voisin, reste un refus. La configuration A v2 (recopiée dans l'essai) passe la validation du v2 et est refusée par celle du v1.
- **Aucune valeur retirée lue ni rendue** : un `contenu` espion note toute lecture de valeur ; seules les valeurs des quatre champs sont lues, aucune des clés retirées, aucun parcours des valeurs, aucune copie, aucun retrait sur place ; les semis ne sont ni dans la sortie, ni dans son compagnon, ni à l'écran (sortie et erreur), ni dans les messages de refus.
- **Compte par clé à l'en-tête** : troisième ligne exacte, avec l'empreinte de la configuration, aucun identifiant de carte ; compagnon égal à l'empreinte de la sortie.
- **Carte hors du choix** : non ouverte, donc non comptée (refus si le nombre attendu la compte, passage s'il ne la compte pas).
- Refus d'écraser et refus d'empreinte fausse, inchangés.

## 5. Commande unique de jeu, en gabarit (à lancer plus tard sous GO-2026-11-20-24, par un autre agent, après contre-lecture et scellement)

```
env -C DOSSIER_DU_PROGRAMME python3 -B masque_style_cartes_v2.py --cartes CHEMIN_COMPLET_DE_fiches.json SHA256_COMPLET_DES_FICHES --configuration CHEMIN_COMPLET_DE_configuration-a-masque-v2.json a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54 --sortie CHEMIN_COMPLET_DE_SORTIE_HORS_DU_DOSSIER_DES_CARTES
```

`DOSSIER_DU_PROGRAMME` tient le masque v2 à son empreinte scellée (`769aace5…` si rien ne change à la contre-lecture). `SHA256_COMPLET_DES_FICHES` est l'empreinte entière dont `ba65c411…` est le début : je ne la connais pas et ne l'ai pas cherchée. Code 0 attendu ; code 2 = refus, rien d'écrit, arrêt.

## 6. Remarques — points que la lettre de GO-2026-11-20-36 ne tranche pas

1. **« À l'octet comme le v1 »** ne peut pas valoir pour le fichier de sortie entier : il porte le nom de la pièce (`masque_style_cartes_v2`) et l'empreinte du programme, qui diffèrent par nature. J'ai lu la règle comme : égal à l'octet une fois ces deux seules valeurs ramenées, et l'essai le vérifie ainsi.
2. **Forme de l'en-tête.** Le compte va dans `en_tete`, en une troisième ligne de texte ; aucune clé de sortie neuve, `rapport` inchangé, pour ne pas changer la forme lue par le lecteur par programme. **Je n'ai pas relu le lecteur par programme v2** (`de99117b…`, hors de mon mandat) : la contre-lecture doit vérifier qu'il accepte un `en_tete` de trois lignes (ou ne le lit pas).
3. **Le compte porte sur les cartes ouvertes**, hors des cartes « hors du choix ». La configuration A v2 a `hors_choix` vide : le compte attendu est celui des 94 cartes que donnait le programme des noms de clés. Si un jour `hors_choix` n'est pas vide, les nombres attendus doivent être écrits en conséquence.
4. **Objet vide refusé** : un `cles_hors_champs_retirees` présent mais vide est un refus, par choix (sans la clé, c'est le v1 ; une clé vide ne dirait rien). Le mandat ne le tranche pas.
5. **Message du refus de compte** : il dit à l'écran le nom, le nombre trouvé et l'attendu, par clé, aucun identifiant ni valeur. C'est la même sorte d'information que celle permise par GO-2026-11-20-28 ; à couper si la session la juge de trop.
6. **Valeurs de tout type** : une clé retirée peut porter n'importe quelle valeur (texte, objet, liste) ; elle n'est jamais regardée, donc une valeur non textuelle n'est pas un refus.
7. Les valeurs retirées restent en mémoire dans l'objet des cartes lu jusqu'au `del fiches`, comme tout le reste de la carte au v1 ; elles ne passent dans aucun objet neuf.
8. La réserve 3 de la proposition tient : un champ manquant ou non textuel reste un refus au v2 ; le masque peut encore refuser sur les vraies cartes pour l'une de ces raisons.
9. La réserve 1 de la proposition (le lecteur par programme en forme « fiches » lit les trois clés) n'est pas de mon ressort et n'est pas touchée.
10. La signature de `extraire_contenus` gagne un paramètre facultatif ; un appel à trois arguments se conduit comme le v1.

## 7. Écarts et incidents

- Aucun refus de permission, de classifieur ni de garde.
- Les essais du v1 n'étaient cités ni par un rapport de développeur ni par une pièce de scellement que j'avais en main : je les ai ouverts par leur chemin complet à côté du masque (`J/criteres-v4/essais_masque_style_cartes_v1.py`), sans commande de liste ; empreinte égale à son compagnon.
- `pytest` lancé par l'interpréteur de l'environnement du dépôt (`/home/user/controle-ia-travail/.venv/bin/python`, Python 3.13.18, même version que `python3`), comme la session me l'a indiqué, plutôt que par `python3` nu.
- `diff -u` a rendu le code 1, ce qui est son code normal quand les fichiers diffèrent ; le premier différentiel, à chemins absolus, a été réécrit à chemins relatifs (même contenu hors des deux lignes d'en-tête).
- Le `fetch` de `main` met à jour la référence `FETCH_HEAD` du dépôt local, comme le mandat le demande ; rien d'autre n'est écrit dans le dépôt.

*développeur, modèle O*
