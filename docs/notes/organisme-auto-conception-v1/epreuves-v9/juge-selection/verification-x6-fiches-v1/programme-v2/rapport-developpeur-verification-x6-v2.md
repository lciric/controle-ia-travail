# Rapport du développeur — vérification X6 contre le fichier des cartes — v2

Pièce de travail (classe C). Remplace le v1 pour le jeu ; le v1 n'est pas touché. Cause : le v1 lisait `identifiants_par_classe` à la racine ; le fichier réel le porte sous la clé racine `extraction`.

## Fichiers (bloc-notes `dev-verification-x6/v2/`)

| Fichier | sha256 |
|---|---|
| `verifier_x6_contre_fiches_v2.py` | 91833df0e8e2ef54a7536d5fa1d23a6ac77e065cfb8e0da34979581243b44de5 |
| `essais_verifier_x6_contre_fiches_v2.py` | ddc992d282e880bb16a34fdf3830e465e869453cf4ff20d88b5ed40b9aba5089 |

Chaque fichier a son compagnon `.sha256`. `essais-fichiers/` : fichiers synthétiques jetables.

## Changements par rapport au v1

1. Liste lue : `objet["extraction"]["identifiants_par_classe"]["a_corriger"]`. Refus, avec un motif propre à chaque niveau, si l'un des trois manque ou n'a pas la bonne forme (objet, objet, liste de deux chaînes distinctes).
2. Ordre de décodage : la sortie est d'abord contrôlée (absente, compagnon absent) ; puis les deux fichiers sont lus en octets et leurs deux empreintes comparées aux constantes gelées, **avant tout décodage** ; puis **l'extraction est décodée et validée en premier** ; le fichier des cartes n'est décodé (clés seulement, valeurs jetées au décodage) qu'ensuite. Un refus de forme sur l'extraction ne décode donc jamais le contenu des cartes (ses octets ont seulement été lus pour l'empreinte).
3. Empreintes gelées inchangées : `fiches` = ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481 ; `extraction` = f5c7cc1ccd83bd8648d44c0c409e8a5fe79fbedca3af429f4ad44fb31e3659eb.

Le reste (trois champs exacts en sortie, compagnon, écran « FAIT » ou « REFUS : motif » sans identifiant, trois options seulement, aucune option d'empreinte d'essai) est repris du v1 sans changement.

## Forme réelle de l'extraction

Lue par `git show origin/main:…/sortie-extraction-x6-v2.json` redirigé vers le bloc-notes ; empreinte de la copie = f5c7cc1c…659eb, égale à la constante gelée. Lue pour la seule structure, puis supprimée ; aucun identifiant recopié dans un fichier rendu. Racine : `chemin`, `commit`, `extraction`, `fichiers_trouves`, `issue`, `octets_journal`, `sha256_journal`, `suffixe`, `version`. Sous `extraction` : `comptes_par_classe`, `doublons`, `identifiants_par_classe` (qui ne contient que `a_corriger`), `noms_cles`, `objets_a_classe`, `source_identifiant`.

## Essais

`env -C …/dev-verification-x6/v2 python3 -B -m pytest -q -p no:cacheprovider essais_verifier_x6_contre_fiches_v2.py` — **44 passés, 0 échoué** (Python 3.13.18).

Les essais du v1 sont repris, sur des extractions synthétiques qui ont désormais la forme réelle. Essais ajoutés :
- passage sur une copie synthétique de forme identique à l'extraction réelle : mêmes clés à chaque niveau, vérifiées dans l'essai ; JSON indenté et à clés triées comme le vrai ; résultat 94 clés, `[false, false]` ;
- refus pour chacun des trois niveaux absent ou de mauvais type ; refus pour la forme du v1 (sans niveau `extraction`) ; refus pour une racine qui est une liste ;
- l'extraction est décodée avant les cartes (ordre observé : extraction puis fiches) ; sur un refus de forme de l'extraction, le décodage des cartes n'est jamais appelé.

## Commande unique de jeu

```
python3 -B verifier_x6_contre_fiches_v2.py --fiches CHEMIN_DES_CARTES --extraction CHEMIN_DE_sortie-extraction-x6-v2.json --sortie CHEMIN_NEUF.json
```

`CHEMIN_NEUF.json` doit être un nom neuf : si la sortie du jeu refusé du v1 existe sous ce nom, ou son compagnon, le v2 refuse.

## Écarts et refus

Aucun refus de permission, de classifieur ou de garde. Aucun accès au fichier des cartes ni à `archives-reponses-modeles/`. Aucune écriture dans le dépôt, aucun commit.

Développeur, modèle L′.
