# Rapport du rédacteur — additif 5 (additif de code de la mesure « portée à 200 » de la ligne 3), version 2 — v2

Pièce de travail (classe C). Écrit le 2026-11-20, sur le mot de la mère qui demande la version 2, sous le mandat `8a669690ac1c43b46d0c6bae9b02ce208783a9bd2b397b557de0ca7399d0d291` (mêmes interdits, même règle d'aveugle, tenue). Aucun programme de la mesure lancé, aucune graine dérivée, aucune écriture dans le dépôt, aucun commit.

## 1. Ce qui est fait

- Contre-lecture lue en entier : `contre-lecture-additif-5-code-portee-200-v1.md`, `df30acc99ddadd29563edd61204e1f86a29e105616bc87bc0e0aac87ad69e84c`, égale à son compagnon ; verdict « À corriger », six corrections.
- Cible : la version 1 versée au dossier `…/ligne-3-votes-effectifs-juges/additif-3-portee-200-v1/`, `d1b237d602d68b488510ff0ba94f9519481984554ae6627807ce43f1a1c4233d`, égale à son compagnon.
- Outil : `/home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, lu en entier avant l'appel.
- **Sept remplacements pour les six corrections**, mot pour mot : la correction 5 en compte deux (« version 1 » → « version 2 » ; la phrase « Version 2, même jour : … » ajoutée après l'empreinte du mandat, avec l'empreinte `df30acc9…` de la contre-lecture à la place de « (empreinte de son compagnon) », comme la contre-lecture le demande). Chaque ancre comptée une fois dans la cible par `grep -c -F -e` avant l'appel (sept décomptes, sept « 1 »). L'outil rend « FAIT : 7 remplacement(s) ».
- Différentiel `diff -u` v1 → v2 relu : cinq blocs de lignes changées (titre ; statut ; commit de `main` ; `CHEMIN` et `HEX` ; raison 3 du § 5), et rien d'autre.

## 2. Ce que la version 2 porte

- `HEX` n'est plus un blanc : il n'est pas écrit dans le fichier ; la mère le lit dans le compagnon scellé et le porte dans les deux commandes au lancement.
- Le commit de `main` est le **seul blanc** : celui du versement du dossier du code sur `main`, fait avant le commit qui scelle l'additif.
- numpy 2.5.3 est dit pour l'environnement des essais et de la vérification du code de l'étage 1 ; la version de l'exécution de l'étage 1 est à relire sur son manifeste par l'agent qui prononce.
- Titre et statut en version 2 ; `CHEMIN` finit par `-v2.md`.

## 3. Remarques

1. Le § 9 « Pièces lues » de la version 2 est celui de la version 1 : la contre-lecture de l'additif n'y figure pas (elle est nommée, avec son empreinte, à la ligne de statut). Je n'ai rien ajouté : « rien d'autre ».
2. La remarque finale de l'additif (« le nom de ce fichier et son rang « 5 » sont ceux du mandat, à confirmer ») reste telle quelle. `CHEMIN` porte maintenant le nom en `-v2.md` : si la mère scelle sous un autre nom ou ailleurs, `CHEMIN` doit le suivre par une version neuve.
3. La date d'écriture de la ligne de statut (11:15Z) est celle de la version 1, inchangée ; la version 2 est produite à 11:26Z (heure du journal de l'outil).

## 4. Écarts

- L'outil est appelé par `python3 CHEMIN_DE_L_OUTIL …`, sans `-B` (lecture stricte de « aucun `-` après python3 ») ; l'usage de l'outil écrit `python3 -B`. Sans effet sur la sortie : l'outil n'importe que la bibliothèque standard.
- Le fichier de remplacements JSON, que l'outil ne scelle pas, reçoit son compagnon par `sha256sum`.
- Aucun refus de permission, de classifieur ni de garde.

Rédacteur neuf, modèle F.
