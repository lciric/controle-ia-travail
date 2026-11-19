# Contrôle du différentiel de l'erratum 1 à l'addendum scellé de la ligne 1, version 2 → version 3 — v1

Vérificateur : le relecteur des versions 1 et 2 de l'erratum, modèle O. Date : 2026-11-19, après 23:36Z (temps universel). Rien lancé ; aucun interpréteur appelé ; aucun réseau sauf `git fetch` et `git show` ; aucune écriture dans le dépôt ; aucun refus d'outil. Rien n'a été touché sous `archives-reponses-modeles/`.

## Verdict

**Scellable tel quel.**

## 1. Empreintes et différentiel

Toutes les pièces du commit `1ca4bfa6` de `lot/compte-organisme-v1` sont conformes à leurs compagnons :

| pièce | sha256 |
|---|---|
| erratum, version 3 | `ab98317d5e809d53eb5af88f17dd1f4e3683a16a1a21c699c9823538f84f1bd4` |
| journal de l'outil | `9ac3beea761e50ddc06ce81cbf6e1a36c296b2838ee933ea40ef18e11719b995` |
| différentiel v2 → v3 | `15e665c106a4d3c65a293e6aebcc11aeeec0680ff7b2623996fd7e22277e974a` |
| rapport de recopie | `a387b030abcfdadf8f3490924015acd09ad0831516f049d96a135a5d7c1cfe11` |
| liste des remplacements | `fd5f08e8ad1a76f61143a98203c68b77231c444fdee2aaf2330484a991fca392` |

La version 2 (`f66c3ce8…`) et mon contrôle (`1c0d4320…`) sont intacts.

J'ai refait `diff -u` sur les deux versions tirées du dépôt : son corps est identique, octet pour octet, à celui du fichier versé.

## 2. Corrections et tenue

- **Correction 1 (chapeau) :** à la lettre, « et porte deux précisions de lecture (§ 3). ».
- **Correction 2 (titre du § 3) :** à la lettre, « ## 3. Précisions de lecture (§ 9, point 5 ; phrase de statut de la copie scellée) — aucune règle changée ».
- **Tenue :**
  - titre et statut en « v3 » ;
  - une ligne d'auteur de la version 3 qui cite mon contrôle par son chemin et son empreinte entière, et la version 2 intacte ;
  - l'ancienne ligne d'auteur renommée « Auteur de la version 2 », sans autre changement ;
  - la date des trois versions.

  Rien d'autre ne change.

## 3. Choix de l'agent

- **Aucun mandat cité pour la version 3.** Aucun fichier de mandat v3 n'est versé : ne rien citer est donc exact, et vaut mieux que citer une pièce qui n'existe pas. La version 3 n'applique que deux remplacements à texte exact, et la pièce qui les ordonne, mon contrôle, est citée avec son empreinte.
- **Mon contrôle cité dans la ligne d'auteur seulement, pas au § 1.** C'est acceptable. Le § 1 liste les pièces lues pour remplir les places ; la règle R6 est tenue par la citation complète (chemin, empreinte) dans la ligne d'auteur, et la relecture de la version 1 figure au § 1 depuis la version 2. Ce choix ne crée aucune ambiguïté sur une valeur.

Aucune correction n'est demandée.
