# Second addendum au préenregistrement des organismes discrets, bras A — nombre de pas de distillation — BROUILLON 1

- **Texte visé** : `prereg/T0.7-organismes-discrets-v-a-v1.md`, `06ab6a2f6e173bb1258f45ffeded7a419b05ecc2f59920666cea91aafcc7cf05` (inchangé, R12). Premier addendum : `prereg/T0.7-organismes-discrets-v-a-v1-addendum-lecture-lot-de-huit-v1.md`, `bd6ae8dfdfcda18a9c7118ede4f1542fae71063521c442093f778a1cd4b0e4f3`, dont la section 6 laissait ce point ouvert.
- **Date (UTC)** : 2026-11-18T17:58:46Z. **Rédaction** : session de relance (`session_013QMaymFtcZwVwjxVAF3gmH`), autrice du code de fabrication du bras A ; à contre-lire par un agent neuf (R2).
- **Décision** : mot direct de Lazar dans la session de relance, le 18 novembre 2026, verbatim « option 1, 384 pas », en réponse à la décision posée : « option 1 : 384 pas, soit 3 époques sur les données du bras A — on garde le nombre d'époques scellé et on s'écarte du chiffre de 480, à déclarer par un second addendum ; option 2 : 480 pas, à la lettre de la clé empruntée, soit 3,75 époques ».
- **Moment** : avant toute génération, toute distillation et toute lecture de résultat du bras A.

## 1. La lettre

Le texte scellé emprunte la clé `distillation` de la configuration de référence (`prereg/T0.6-organismes-config-7b-v1.json`, `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` ; ligne 17 du texte scellé ; ligne 39 : « mêmes réglages que ceux de la famille (ii) »). Cette clé porte `epoques` = 3, `lot` = 1 et `pas_declares` = 480. Dans la chaîne de référence, `pas_declares` est une **garde** : le nombre de pas déclaré doit être celui que donnent les exemples, les époques et le lot ; 480 y vaut pour 160 transcriptions (32 tâches × 5 épisodes) × 3 époques.

## 2. Ce qui est retenu

Le bras A distille, pour chaque adaptateur, les transcriptions de **16 tâches de fabrication × 8 épisodes = 128 transcriptions** (premier addendum, sections 4 et 5). À **3 époques** et lot 1, cela fait **384 pas**. **Le nombre de pas déclaré du bras A est 384** ; les autres réglages de la clé `distillation` (époques, lot, taux, norme bornée, mode par transcription) sont ceux de la configuration de référence, inchangés.

## 3. Écart à la lettre, déclaré

La valeur `pas_declares` = 480 de la clé empruntée n'est pas exécutée ; 384 la remplace. Le nombre d'époques scellé (3) est tenu.

## 4. Ce qui ne change pas

- Tous les adaptateurs du bras A — un par dose non nulle, et les témoins (vi-T) et (vi-B) — reçoivent **le même nombre de pas, 384**, sur le même volume de données (exigence du témoin (vi-T) : « même nombre de pas et même volume de données »).
- Si des épisodes laissés honnêtes ou des actions non permutables réduisent le nombre de cibles déplacées, le nombre de transcriptions et de pas ne change pas : une transcription laissée honnête reste dans les données de son adaptateur, comptée (aucun repli silencieux, R5).
- Hypothèses, prédictions, seuils, critères de lecture, puissance, liste d'arrêt, ordre d'exécution : inchangés. Aucune dépense ouverte.
