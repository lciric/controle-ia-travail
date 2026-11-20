# Constat final — complément de valeurs du préenregistrement court v9, lot 1, v3 — v1

Pièce de travail (classe C), 2026-11-20, relevé de `date -u` : 14:50:42Z. Contre-lecteur neuf, modèle O, auteur de la contre-lecture du complément v2 (`211d546b…`). Mandat `799b14c6…`, en-tête compris. Processeur seul : aucun appel, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune publication. Ni méthode d'attaque, ni procédé, ni nom ou énoncé de mode, ni case nommée, ni valeur de clé, ni identifiant de modèle. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

**Conforme, à sceller**, sous une condition portée par le traitement que la mère écrit au scellement : le § 10 « Vérification » est remplacé par le texte exact du § 3.

- La première passe est égale, par `cmp`, à mon essai.
- La tenue, rejouée, rend le complément v3 à l'octet.
- La tenue ne touche que le titre, la date, le statut, la phrase de version et une ligne de la table.

## 1. Contrôles

| pièce | empreinte | contrôle |
|---|---|---|
| étape 1 (v2 + 28 corrections) | `674af0524365c05c6826528cca3ef7a1520d2da31d21f9a2f6e1e63fc24aa792` | compagnon « OK » ; `cmp` égal à mon essai `essai-complement-valeurs-v2-corrige-v3.md` |
| jeu de tenue | `900c63b960c51770da1d139c146d3a2c88a04c40a92a3597fa40fcba708609ee` | compagnon « OK » ; 5 remplacements rejoués sur mon essai : sortie `734a0556…`, égale au complément v3 (`cmp`) |
| complément v3 | `734a0556ea9f5cba402c2f8f9118e015e0a4913b1fd4904d0de0fa6674905c30` | compagnon « OK » |
| différentiel ; rapport | `216c0346…` ; `253e26319868484a7abfda7d3f69db55fcef11788d27bd0de93075deea914605` | recalculées |
| contre-lecture v2, au chemin versé | `211d546b…` | recalculée ; égale à ce que citent la phrase de version et la table |
| `registres/decisions.md` sur `origin/main` (`3ba0753265c911beae069281e3b8b8c769adae70`) | `b3554de618383b52a929bc648b37078da881987f5a5a6b34fd662ef22efb6627` | R-4303, R-4305, R-4306 lus |

L'écart 1 du rapport, l'égalité à l'essai vue par l'empreinte et non par `cmp`, est levé ici.

## 2. La tenue, et la lettre de R-4303, R-4305, R-4306

Les cinq remplacements de tenue, lus un par un :
- le titre (v2 → v3) ;
- la date (« Version 3 : 14:48:40Z ») ;
- le statut, qui cite mon verdict exactement ;
- une phrase de version neuve, qui résume le jeu sans en changer la lettre ;
- une ligne de table pour ma contre-lecture, avec le bon chemin et la bonne empreinte.

Rien d'autre ne change.

Les registres concordent avec le complément :
- **R-4303** (14:43:11Z) porte les quatre décisions, que le complément date « 14:43Z » : arrêt n° 11 sans conversion de monnaie ; lignes à part, épreuve des témoins et sonde de l'espèce 4, sur Minuit ; troisième relais sous son cas haut : nœud ; pièce de relevés valant « complément scellé ». Conforme.
- **R-4305** porte les mots de la mère sur Luc (214 déclarés, 0,000002 de dépense, reste 213,999998, sans relevé possible chez ce fournisseur), sur Rigaud et le troisième relais (« attend le relevé de Lazar »), et la part de 125,63 « arrondie vers le bas ». Conforme sur le fond. **Une différence de lettre** : R-4305 date ces mots « vers 14:38Z », alors que le complément écrit « vers 14:40Z » à quatre lieux (lignes 12, 45, 114, 158).
- **R-4306** dit pour Minuit, à 156,56 : « dans la règle de GO-16 « part bornée au solde » ; pas d'écart ». Le complément ne déclare pas d'écart : conforme. Il dit aussi que le véhicule route les lignes à part hors de la course, et que la pièce de relevés est calculée par programme et constatée par `cmp`. Le complément s'accorde à ce point.

La différence d'heure ne justifie pas une version neuve : « vers » vaut approximation, et R-4305 fait foi. Elle se règle dans le traitement (§ 3), qui cite R-4303, R-4305 et R-4306.

## 3. Écart 2 du rédacteur : le § 10 « Vérification »

Le § 10 dit encore « **Ce complément n'est pas vérifié.** … ». Scellé tel quel, il dirait une chose fausse. Comme pour l'additif 1, scellé avec le traitement de la mère (R-4300), **c'est acceptable au scellement si ce traitement le remplace.** Texte proposé, à la place de la ligne « **Ce complément n'est pas vérifié.** Vérification par un autre modèle, à qui l'on donne les pièces de la table, le mandat et le rapport du rédacteur ; puis scellement par la mère. » :

    - **Contre-lecture 1** (le complément v2, par un agent d'un autre modèle) : contre-lecteur neuf, modèle O ; il n'a écrit aucune version de ce complément. Brouillon relu : la v2, `267a69de63450634c369dc22415b0751c0483be1d60a000b4b598640d01c1125`. Rapport : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/complement-valeurs-v2/contre-lecture-v1/contre-lecture-complement-valeurs-v2-v1.md`, `211d546bff019f12fc0cdef36389bc0f8564e4ac19e6db23fdc2fc5b1b2e0b87`, verdict « À corriger » : 28 remplacements (jeu `5d2d765a3004b42258fd2fd1c6416e738caa0ce8eb29478d7f08c459b78ec5ae`), dont les décisions de la mère de 14:43Z (R-4303) ; aucune valeur inventée ; « aucune recette » conforme.
    - **Constat final** (la v3, par le même contre-lecteur) : première passe égale, par `cmp`, à l'essai du contre-lecteur ; seconde passe, de tenue seule, rejouée à l'octet ; verdict « Conforme, à sceller ». Chemin et empreinte du constat : écrits par la mère avec ce traitement.
    - **Décisions de la mère inscrites** : R-4303 (décisions de 14:43Z), R-4305 (mots de la mère sur les restes, que ce texte date « vers 14:40Z » et que le registre date « vers 14:38Z » : le registre fait foi ; part de Luc à 125,63), R-4306 (part de Minuit dans la règle de GO-2026-11-20-16, sans écart ; routage des lignes à part ; pièce de relevés calculée par programme et constatée par `cmp`) ; `registres/decisions.md` sur `main`, commit `3ba0753265c911beae069281e3b8b8c769adae70`, `b3554de618383b52a929bc648b37078da881987f5a5a6b34fd662ef22efb6627`.

Les écarts 3 et 4 du rapport sont justes : les décisions de 14:43Z sont inscrites à R-4303, et la date de la pièce est l'heure du journal de la première passe.

## 4. Fichiers

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-additif-1-v9/`. Ce constat et son compagnon `.sha256`. Le rejeu (`rejeu-complement-v3.md` et son journal) est un essai, non une pièce.

— contre-lecteur neuf, modèle O
