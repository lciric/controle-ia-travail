# Vérification des corrections de l'additif 5 (additif de code de la mesure « portée à 200 » de la ligne 3), version 2 — v1

Pièce de travail (classe C). Même contre-lecteur que la contre-lecture `contre-lecture-additif-5-code-portee-200-v1.md` (`df30acc99ddadd29563edd61204e1f86a29e105616bc87bc0e0aac87ad69e84c`), sur le mot de la mère, sous les interdits et la règle d'aveugle du mandat `4e6ac7597c9b9766a140f49149f33fb7b835c914f7c2b5839b6e677e9a38bbf1`. Aucune mesure de l'étage 1 ouverte ; aucun programme de la mesure lancé ; aucune graine dérivée ; aucune écriture dans le dépôt.

## Verdict : Conforme, à sceller

La version 2 est la version 1 avec mes six corrections, mot pour mot, en sept remplacements, et rien d'autre.

## 1. Empreintes (chacune égale à son compagnon, `sha256sum -c` : OK)

Dossier `LIGNE/additif-3-portee-200-v1/` (LIGNE = `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`) :

| pièce | sha256 |
|---|---|
| `additif-5-code-preenregistrement-ligne-3-portee-200-v1.md` (cible) | `d1b237d602d68b488510ff0ba94f9519481984554ae6627807ce43f1a1c4233d` |
| `additif-5-code-preenregistrement-ligne-3-portee-200-v2.md` | `e193bc4ea26a8ac2946876736fae4a9b55b2bfe8de0e06fe5826afb935ce6c9c` |
| `remplacements-additif-5-v1-v2.json` | `60d9e66f1f33add58612e6ad272044c400b48cb521e5e4955de63444691c97a1` |
| `differentiel-additif-5-code-portee-200-v1-v2.diff` | `2a77ebb75267800d92260fa09685bdea237786f38ae48bb9fd0c4e743c130549` |
| `rapport-redacteur-additif-5-code-portee-200-v2.md` | `110aa988f06abcff30c4f68c75f62303e8aa4305f23dd7b6f6168c94a1b59d9b` |
| outil `scripts/remplacer_texte_exact_v1.py` (lu en entier) | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |

Le commit `c6fa2add` (`c6fa2add7ec1348276f356125b620c945c05b057`) porte la version 2 à ces octets (`git show` redirigé, `e193bc4e…`).

## 2. Rejeu de l'outil

`env PYTHONDONTWRITEBYTECODE=1 python3 /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py --cible …-v1.md --remplacements …/remplacements-additif-5-v1-v2.json --sortie <mon dossier>/lus/rejeu-additif-5-v2.md` : « FAIT : 7 remplacement(s) », sortie `e193bc4e…`. `cmp` entre ma sortie et la version 2 versée : aucun écart. L'outil exige que chaque texte ancien figure exactement une fois, applique les remplacements à leurs seules zones et contrôle que tous les autres octets restent égaux : la version 2 ne diffère donc de la version 1 que par ces sept remplacements. Le différentiel versé montre les mêmes cinq blocs (titre ; statut ; commit de `main` ; `CHEMIN` et `HEX` ; raison 3 du § 5).

## 3. Les six corrections, mot pour mot

Chaque « ancien » du JSON est l'« Ancien » de ma contre-lecture. Chaque « neuf » est compté une fois dans ma contre-lecture par `grep -c -F -e` (corrections 1, 2, 3, 6 ; la phrase de la correction 5, en ses deux moitiés de part et d'autre de l'empreinte) ou lu à l'œil (corrections 4 et 5, premier remplacement).

1. `HEX` : « neuf » égal au mien.
2. Commit de `main` : égal.
3. Raison 3 du § 5 : égal.
4. Titre « — v1 » → « — v2 » : égal.
5. Statut, en deux remplacements : « version 1 » → « version 2 » ; puis la phrase ajoutée après « (`8a669690…`, égale à son compagnon). », ancre unique à la fin de la ligne de statut. La seule différence avec mon texte est celle que je demandais : « (empreinte de son compagnon) » remplacé par l'empreinte `df30acc99ddadd29563edd61204e1f86a29e105616bc87bc0e0aac87ad69e84c`, qui est bien celle du compagnon de ma contre-lecture.
6. `CHEMIN` en `-v2.md` : égal. Ce chemin est libre sur `origin/main`.

Rien d'autre ne change.

## 4. Les trois remarques du rédacteur

1. **Le § 9 n'est pas mis à jour** : accepté. Le § 9 dit ce que le rédacteur a lu pour la version 1. La contre-lecture est nommée, avec son empreinte, à la ligne de statut ; c'est la forme des additifs 2 et 3. L'ajouter aurait été un changement que je n'ai pas demandé.
2. **« Nom et rang à confirmer »** (remarque finale) : accepté tel quel. Le rang « additif 5 » est confirmé par la mère. Le nom en `-v2.md` est celui que porte `CHEMIN`. La remarque ne dit que ce qui arriverait s'ils changeaient ; elle ne laisse aucun blanc. **Condition pour la mère : sceller sous `prereg/organisme-auto-conception-v9/additif-5-code-preenregistrement-ligne-3-portee-200-v2.md`, exactement**, sinon `CHEMIN` ne désigne plus la pièce scellée.
3. **L'heure de la ligne de statut** (11:15Z, celle de la version 1) : acceptée. La phrase « Version 2, même jour » suit la forme des additifs 2 et 3 (« à la première heure relevée »). Le journal de l'outil porte l'heure de la version 2.

## 5. Rappel pour le scellement (sans changement du texte)

Un seul blanc à écrire, le commit de `main` du versement du dossier du code, fait avant le commit qui scelle l'additif. `HEX` n'est pas écrit dans le fichier : il est lu dans le compagnon scellé et porté dans les commandes.

## 6. Écarts

- L'outil est lancé par `env PYTHONDONTWRITEBYTECODE=1 python3 CHEMIN …`, sans `-B`, par lecture stricte de « aucun `-` après python3 » ; la variable empêche toute écriture de code compilé.
- Sorties de l'outil (la version 2 rejouée, son compagnon, son journal et le compagnon du journal) écrites dans mon dossier, sous `lus/`.
- `git rev-parse`, un `git show` redirigé et un `git cat-file -e` sur `origin/main`, chacun sur un seul chemin ou commit nommé.
- Aucun refus de permission, de classifieur ni de garde.

Contre-lecteur neuf, modèle O.
