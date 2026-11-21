# Vérification des changements — pièce de sécurité du banc fermé, v7 — v6

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v7.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `2efdc92f8fa9032e3e05b52bff92782a734376d5`. Empreinte recalculée : `d3172b9af08d294db589e842b3cd85969dc40f86a5f67b1c7a83634cc655c683`, égale au `.sha256`. Les v1 à v6 sont intactes, toutes recalculées (v6 : `f3bb3052…`).
- **Référence** : `verification-des-corrections-v5.md` (`39328f92…`), qui acceptait la v6.
- **Vérificatrice** : la même contre-lectrice (Opus 5.5). **Date** : 21 novembre 2026, vers 19:15 UTC.
- **Méthode** : différence ligne à ligne entre la v6 et la v7, relue contre la table de la section 13.

## Source neuve contrôlée

**[GO72]** : `registres/go.md` au commit `52e9d1bd`. Empreinte du fichier recalculée : `5fa343b8…`, égale. Seule la ligne 671 (GO-2026-11-21-72) a été lue. Elle porte :
- les deux mots verbatim, conformes à [ML] et à [ML2] ;
- la lecture de la mère (voie interne, écart déclaré lu avec GO-2026-11-21-71, vérificateur Opus 5.5 neuf lancé à son rang, opérateur et juge à trancher par Lazar) ;
- une réserve : « si un moniteur évalué est de la lignée Claude, un vérificateur d'une autre lignée est requis (audit des lignées en cours) ».

La note [ML] au commit `154bdff94`, cité par [GO72], a pour empreinte `27c16352…`. Je l'ai recalculée : c'est la même qu'au commit `3df76fac`. La réserve 8 est donc exacte.

## Changements

| Lieu | Constat |
|---|---|
| En-tête, ligne 6 | Les mots (2) et (3) sont maintenant rattachés à [GO72]. C'est exact. |
| Lignes 8 et 9 | La v6 y est archivée avec la bonne empreinte. La ligne « Date » garde « vers 18:05 UTC », un détail sans portée. |
| Sources | Ligne [GO72] juste. |
| 4.2, ligne neuve | « Audit des lignées sans réponse, ou vérificateur de la lignée d'un moniteur évalué : le vérificateur n'est pas lancé, donc aucune course. » C'est conforme à [GO72], et plus strict que la v6. |
| 6.3, « Une tension à dire » | **Le seul changement de fond.** La v6 disait qu'en cas de moniteur de la lignée de Claude, le mot de Lazar primait et que l'écart se déclarait. La v7 suit la réserve inscrite au registre : une autre lignée est alors requise. C'est juste. La règle du registre est plus récente que la note [ML2], et c'est la lecture de la mère, inscrite à la ligne même qui porte le mot ; elle va du côté prudent. Le changement est déclaré, motivé et sourcé. |
| Réserves 8 et 10 | Réécrites conformément au registre. |
| Section 13 | Elle décrit fidèlement la différence. Aucun changement non déclaré. |

**Remarque, sans point** : la ligne « Qui » de 6.3 dit encore « une session neuve d'Opus 5.5 ([ML2]) », sans y joindre la condition de lignée. Ce n'est pas une contradiction, puisque le paragraphe qui précède, la réserve 10 et la liste d'arrêt la portent. Une version ultérieure pourra la joindre.

**Contenu d'attaque** : aucun. **Refus de classifieur** : aucun.

## Verdict final

**Accepté** : la pièce de sécurité du banc fermé, v7 (`d3172b9a…`). Aucun point sur les changements de la v7.

Bilan de toute la chaîne, de la v1 à la v7 : 2 points bloquants et 11 mineurs, tous corrigés.

Cette acceptation vaut, pour la condition de GO-2026-11-21-71, « contre-lecture de la pièce, corrections vérifiées ». Elle n'autorise ni construction, ni course, ni dépense. Restent :
- le préenregistrement de la course ;
- le code des gardes, contre-lu ;
- les treize épreuves à blanc ;
- la répétition, sur devis et GO ;
- l'audit des lignées des moniteurs (par la mère) ;
- la pièce du vérificateur ;
- le GO de la course ;
- la confirmation de la lecture « treize gardes » (réserve 11).
