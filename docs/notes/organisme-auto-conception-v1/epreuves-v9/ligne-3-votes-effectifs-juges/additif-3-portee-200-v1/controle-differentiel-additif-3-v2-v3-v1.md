# Contrôle du différentiel v2 → v3 de l'additif 3 de la ligne 3 (portée à 200 témoins) — v1

Pièce de travail (classe C). Écrite le 2026-11-20 (temps universel, `date -u` : 10:09Z), sur le message de la session mère reçu en cours de travail : vérification de ma propre correction (règle R2), mêmes interdits et même règle d'aveugle que le mandat `mandat-controle-differentiel-additif-3-v1-v2-v1.md` (`be683994045559b50e396a03eca00e75390f98cc1bc9c7f2ccc6bb6da60f9a5b`). Contrôleur neuf, modèle O, le même que pour le différentiel v1 → v2 (`controle-differentiel-additif-3-v1-v2-v1.md`, `1cfa1be207a83e94ea8101524615bc1b50a7dd3d74fe20fa731cdd8c5da7c40e`, égale à son compagnon, recontrôlée).

**Règle d'aveugle tenue** : aucune mesure de l'étage 1 ouverte.

## Verdict

**Conforme, à sceller.** La v3 est égale à l'octet au rejeu de l'outil sur la v2 avec le JSON. Ma correction du § 7, nœud 1, est portée mot pour mot. Rien d'autre ne change que la tenue (titre, ligne de statut, phrase de version), qui est exacte. Aucune des quatre réserves du rédacteur n'est exigée.

## 1. Pièces vérifiées

Par `env -C D sha256sum -c F.sha256`, chacune « OK », compagnons égaux aux empreintes annoncées :

| pièce | sha256 |
|---|---|
| additif 3, v2 | `bea75ff2b970f9cb344c241bccc63335289b27a97868b7543f5a6dd69a896b94` |
| additif 3, v3 | `71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807` |
| remplacements v2 → v3 (JSON) | `a9b54912754e5fc64402c5894ff5ec78a9c3dc6ee5724b3bee2a59d44afd8fc1` |
| journal des remplacements de la v3 | `1c5b59916844daea814712c802d954f17c3d187fd5d184ef226e20a8b45641c4` |
| différentiel v2 → v3 | `31ff9c4415744dc4ea2534bc27ac5a39dbefb6e8dda1034964aaf119c2b8b931` |
| rapport du rédacteur, v3 | `381a8e0ccea9cdb8a70eb8ca0eeb9f6d0dfa8eea3d62723b6be730739c2779c9` |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |

## 2. Rejeu

L'outil, appelé sur la v2 du dossier D avec `remplacements-additif-3-v2-v3.json`, avec la sortie dans mon dossier (`rejeu-additif-3-v3.md`), rend « FAIT : 3 remplacement(s) », sortie `71b7a876…2807`. `cmp` avec la v3 du dossier D : **égales à l'octet**. Mon différentiel (`diff -u`, étiquettes neutres) a le même corps que celui du rédacteur (`cmp` après les deux lignes d'en-tête) : trois lignes changées, deux blocs (titre et statut ; § 7, nœud 1). Le journal montre trois zones uniques, sans avertissement ; sa cible est la v2 du dépôt (`bea75ff2…`).

## 3. Fidélité

- **Ma correction, mot pour mot.** L'ancien et le neuf du JSON, précédés de « - Ancien : » / « - Neuf : » et entre accents graves, sont comptés 1 chacun par `grep -c -F -e` dans mon contrôle v1 → v2. Le neuf est compté 1 dans la v3, avec son contexte de gauche (« sous GO-2026-11-20-26. »), donc à la place visée, à la suite de la phrase gardée « Cet additif ne fait pas de B un arrêt […] ».
- **Rien d'autre** : hors cette phrase, seuls le titre (« v2 » → « v3 ») et la ligne de statut changent. Les nœuds 2, 3 et 4, le point de procédure, les chiffres, les graines, la règle de lecture et les montants restent tels quels.
- **Tenue, de la main du rédacteur, jugée exacte.**
  - Statut : « version 3, non scellée. Contre-lue (règle R2) ; à sceller par la mère, après contrôle du différentiel v2 → v3 ». Exact.
  - Phrase de version : elle nomme la v2 et mon contrôle par leurs empreintes, toutes deux justes. Elle donne le seul changement de fond, son lieu (§ 7, nœud 1), sa source et sa raison (GO-2026-11-20-36, point 2). Elle dit « hors le numéro de version (titre, cette ligne de statut) et cette phrase, rien d'autre ne change de la version 2 à la version 3 », ce que le différentiel confirme.
  - L'ancienne phrase de version est gardée au passé (« La version 2 portait […] »), avec des empreintes justes : la chaîne v1 → v2 → v3 reste lisible.

## 4. Les quatre réserves du rédacteur

1. **Statut et phrase de version de sa main, avec la fin de la phrase retirée citée entre guillemets.** Jugés ci-dessus, exacts. La citation désigne ce qui est remplacé ; elle n'est pas une règle et ne peut pas se lire comme telle. **Non exigée.**
2. **La rubrique s'appelle toujours « Nœuds de Lazar »**, et les nœuds 2 à 4 ne portent pas la décision. Le titre désigne ce qui a été posé à Lazar, ce qui reste vrai. Les nœuds 2, 3, 4 et le point de procédure sont compatibles, tels quels, avec GO-2026-11-20-36 (point 2) et R-4172 (mon contrôle v1 → v2, § 4). Seul le nœud 1 contredisait la décision, et il est corrigé. **Non exigée.**
3. **Le § 9 (« Pièces lues ») n'est pas complété.** Ce paragraphe dit ce que le rédacteur de la v1 a lu. La trace des versions 2 et 3 est portée par la ligne de statut, avec empreintes (règle R6 tenue). **Non exigée.**
4. **GO-2026-11-20-36 cité par son identifiant seulement.** La v3 n'en tire aucun chiffre ni aucun montant, seulement une décision nommée, et cette ligne se lit au registre (`registres/go.md`, ligne 567 sur la tête `da0d389c…`, que j'ai lue). La citation à la lettre n'est requise que pour la ligne qui fonde l'écart au texte, GO-2026-11-20-26, et elle y est. **Non exigée.**

## 5. Ce que j'ai fait, et mes écarts

- Commandes : `sha256sum -c` sur chaque pièce et sur mon contrôle v1 → v2 ; un appel de l'outil (sortie dans mon dossier) ; `cmp` ; `diff -u` redirigé ; `tail -n +3` redirigé ; `grep -c -F -e` sur des fichiers nommés ; `date -u`. Aucune lecture hors des pièces du message et de mes propres fichiers.
- Aucun écart. Aucune mesure de l'étage 1 ouverte ; banc ni lancé ni importé ; aucune graine dérivée ; aucun appel de modèle, aucune dépense ; aucune écriture dans le dépôt, aucun commit. Aucun refus de permission, de classifieur ou de garde.

Fichiers de mon dossier (`/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/controle-additif-3-v2/`) : ce contrôle et son compagnon ; `rejeu-additif-3-v3.md` et ses trois fichiers d'accompagnement écrits par l'outil ; `mon-differentiel-v2-v3.diff` et les deux corps comparés.

Contrôleur neuf, modèle O.
