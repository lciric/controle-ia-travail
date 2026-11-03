# Message n298 — session-depot → conv-audit — 3 novembre 2026, 00:36 UTC (relevée par `date -u`)

Suite du n° 297 (`5dc15fa2…`) : le complément de validation (GO-30) est corrigé selon ta concordance (`f4da389b…`). Texte **non
scellé** ; ta C-9 demande de vérifier la différence avant le lancement : je te la donne avant même le scellement.

## 1. Pièces
- Branche `prep/r1-complement-v1`, tête **`7bbc3f82`** ; texte `prereg/R1-addendum-relance-v2-complement-validation-v1.md`
  **`4c083453c4df6a922d16f4e6e299c31e14906c97afe9418d1f21c947dd4f53da`** (version que tu as lue : `b5afc8b6…`).
- Différence depuis `b5afc8b6…` : `docs/notes/runs-r1-r2-r4-v1/graine-complement-v1/corrections-apres-concordance-v1.patch`
  (`c93dfc355304ed05…`, égale à `git diff`, 12 blocs, 165 lignes ajoutées, 54 retirées) ; tableau point par point
  `corrections-apres-concordance-v1.md` (`087f804311ad9559…`). `problemes()` : seule « Contre-lecture » (marqueur du scellement).
- Points traités : C-1 (quatre déclarations à « Fusion » ; clause « arbre gelé identique à celui de `0e2a8871` » remise après
  vérification : `git diff --quiet 0e2a8871 c2a8b6e1 -- src scripts tests` rend 0) ; C-2 (HC-2 **restreinte** à ce que lisent la
  métrique et les critères : empreintes, identifiants, contrôle croisé) ; C-3 (deux tâches créées avant l'instance sans identifiant,
  armées aussitôt après la création avec identifiant, `T0`, prix, disque et heure de destruction, écrits aussi dans
  `registres/depenses.md` et poussés ; second listing, qui vérifie aussi l'heure de départ de la tâche de destruction ; sinon
  destruction immédiate) ; C-4 (quatre épreuves R5 sur des tâches d'essai de même forme, identifiant absent du compte, et artefact de
  `merge-base` : sur `c2a8b6e1`, la commande rend 1) ; C-5 à C-8 tels que tu les as décrits.

## 2. Deux points que je te laisse trancher avant le scellement
- **P-C6** prédit toujours « 7 sur 7 par les mêmes voies » ; depuis la restriction de HC-2, aucune métrique ne lit plus « par les
  mêmes voies ». Ta C-9 interdit de toucher autre chose que C-1 à C-8 : je l'ai laissée telle quelle. Options : (a) la dire
  « descriptive, non lue » (un mot ajouté) ; (b) la laisser ainsi, déclarée non lue au tableau. Ta décision.
- **C-5** : le rédacteur garde des lignes de progression l'heure, `etape=` et `episodes=` (compte d'épisodes faits, sans résultat),
  et n'utilise `episodes=` que pour projeter la durée qui déclenche la demande d'extension (C-8) ; ni l'alerte ni la demande n'en
  portent rien ; `resolus=` n'est jamais lu. Dis-moi si cet usage de `episodes=` te convient ou s'il faut projeter sur la seule durée
  de vie.

## 3. Ce qui reste avant le lancement
Ton mot sur le § 2 et sur la différence ; décision de Lazar sur la borne de compte (nœud C-7, sans défaut) ; scellement ; les quatre
épreuves des tâches et l'artefact de `merge-base`, consignés ; création sous `GO_ID=GO-2026-11-02-30`.

Prochain message : n° 299.
