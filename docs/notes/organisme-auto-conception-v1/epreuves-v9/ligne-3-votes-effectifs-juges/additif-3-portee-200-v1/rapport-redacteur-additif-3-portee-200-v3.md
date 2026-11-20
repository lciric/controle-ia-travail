# Rapport du rédacteur — additif 3 de la ligne 3, portée à 200 témoins — version 3 — v1

Pièce de travail (classe C), 2026-11-20, sur le mandat `mandat-redacteur-additif-3-v3-v1.md` (`56d52430dfdc68d1108e4cbdb56a09193d9a787a8cf666f56aa083e3cc99f3b8`, égale à son compagnon). Rédacteur neuf, modèle F. Rien écrit dans le dépôt, aucun commit, aucun lancement du banc, aucune graine dérivée, aucun appel de modèle, aucune dépense, aucune mesure de l'étage 1 ouverte, aucun refus de permission, de classifieur ou de garde.

## Verdict

La version 3 est écrite : `additif-3-preenregistrement-ligne-3-portee-200-v3.md`, `71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807`. Elle porte sur la version 2 la seule correction demandée par le contrôle du différentiel v1 → v2 (§ 7, nœud 1), mot pour mot, et la tenue de version. À contrôler sur le différentiel v2 → v3 par un autre modèle, puis à sceller par la mère.

## Pièces vérifiées avant tout geste

| pièce | sha256 | contrôle |
|---|---|---|
| additif 3, version 2 | `bea75ff2b970f9cb344c241bccc63335289b27a97868b7543f5a6dd69a896b94` | `sha256sum -c` : OK ; lue en entier |
| contrôle du différentiel v1 → v2 | `1cfa1be207a83e94ea8101524615bc1b50a7dd3d74fe20fa731cdd8c5da7c40e` | `sha256sum -c` : OK ; lu en entier |
| rapport du rédacteur, version 2 | `d0851288567347dcc2dfff058aa457eb581e2938d332604dc0524ec7da2e1d8c` | lu en entier (forme) |
| remplacements v1 → v2 (JSON) | `78d3c674c88c2b3de0c8d0ac06ef7d5e51a8d220ca68c058779f307c9fba0084` | égale à l'empreinte relevée par le contrôle ; lu (forme) |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` | égale à l'attendue ; lu en entier |
| `registres/go.md` sur main (tête `da0d389cad376ad492d0255b42d7e633fea09f5a`) | `21f8f1847565c41f9e448746b826ef821575fcf65c267b319ed7ee5acba19356` | ligne 567 (GO-2026-11-20-36) lue seule ; son point 2 est égal à la lettre citée par le contrôle |

## Ancres et comptes

Chaque ancre comptée par `grep -c -F -e` dans la version 2 avant l'appel de l'outil : 1 chacune. L'outil exige de son côté une occurrence exacte à l'octet, et l'a trouvée.

| n° | lieu (ligne de la version 2) | ancre (début) | compte | nature |
|---|---|---|---|---|
| 1 | titre (l. 1) | « avant l'étage 2 à 200 — v2 » | 1 | tenue : « v2 » devient « v3 » |
| 2 | ligne de statut (l. 3) | « **Statut : version 2, non scellée. […] rien d'autre ne change. Écrit le » | 1 | tenue : statut « version 3 », « après contrôle du différentiel v2 → v3 » ; phrase de version neuve, de ma main ; la phrase de version de la version 2 est gardée au passé (« La version 2 portait […] ») |
| 3 | § 7, nœud 1 (l. 169) | « Partir quand même, attendre, ou viser une autre taille […] sur le verdict scellé de la mesure. » | 1 | correction du contrôle, « Ancien » et « Neuf » mot pour mot |

Mot pour mot : les lignes « - Ancien : `…` » et « - Neuf : `…` » du contrôle (§ 4, nœud 1), reprises entières entre leurs accents graves, sont comptées 1 chacune dans le contrôle par `grep -c -F -e` avec les textes de mon JSON.

## Remplacements

Un seul appel de l'outil : « FAIT : 3 remplacement(s) », aucun avertissement ; cible `bea75ff2…6b94` (37 925 octets), sortie `71b7a876…2807` (38 711 octets). Le différentiel (`diff -u`) montre trois lignes changées en deux blocs (titre et statut ; § 7, nœud 1), et aucune autre. Aucun chiffre, aucune graine, aucune règle de lecture, aucun montant ne bouge ; les nœuds 2, 3, 4, le point de procédure et la section « Pièces lues » sont inchangés.

## Réserves

- La ligne de statut et la phrase de version sont de ma main : à contrôler. La phrase de version cite, entre guillemets, la fin de la phrase retirée (« à prendre sur le verdict scellé de la mesure ») pour dire ce qui est remplacé ; ce n'est plus une règle du texte.
- Le texte neuf du nœud 1 garde le titre du nœud et la phrase « C'est l'issue que je prédis », que le contrôle ne touchait pas. La rubrique s'appelle toujours « Nœuds de Lazar » alors que GO-2026-11-20-36 (point 2) les a tous tranchés ; je n'ai pas inscrit la décision aux nœuds 2 à 4 (le contrôle le dit « non exigé », le mandat dit « rien d'autre »).
- La section « Pièces lues » (§ 9) n'est pas complétée : le contrôle et son empreinte sont nommés à la ligne de statut ; l'outil et `registres/go.md` le sont ici seulement.
- La ligne GO-2026-11-20-36 n'est pas citée à la lettre dans la version 3 : seul son identifiant et son point 2 y sont nommés, dans les mots du contrôle.

## Écarts

Aucun écart au mandat. La copie de `registres/go.md` tirée de main est restée dans mon dossier (`go-main.md`) ; la recherche de la ligne GO-2026-11-20-36 y a été faite par l'outil de recherche du poste, sur ce seul fichier, par un motif étroit (l'identifiant en début de ligne).

## Pièces et empreintes

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-additif-3-v3/`. Chaque pièce a son compagnon `.sha256`.

| pièce | sha256 |
|---|---|
| `additif-3-preenregistrement-ligne-3-portee-200-v3.md` | `71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807` |
| `additif-3-preenregistrement-ligne-3-portee-200-v3.md.journal-remplacements-v1.json` | `1c5b59916844daea814712c802d954f17c3d187fd5d184ef226e20a8b45641c4` |
| `remplacements-additif-3-v2-v3.json` | `a9b54912754e5fc64402c5894ff5ec78a9c3dc6ee5724b3bee2a59d44afd8fc1` |
| `differentiel-additif-3-portee-200-v2-v3.diff` | `31ff9c4415744dc4ea2534bc27ac5a39dbefb6e8dda1034964aaf119c2b8b931` |
| `rapport-redacteur-additif-3-portee-200-v3.md` | au compagnon |

Rédacteur neuf, modèle F.
