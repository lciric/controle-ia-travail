# Contre-lecture de la consigne du lecteur de l'issue du pilote MR-2 (procédure v14), v9 — tour 2 de la v8

Contre-lecteur : modèle C (neuf, R2) ; pièce écrite par le modèle A, corrections appliquées par un rédacteur du modèle C. Heure : 2026-11-16T15:50Z (`date -u`).
Pièce lue : `consigne-lecteur-issue-pilote-v14-v9.md` (`8e31067b…`, égale à son compagnon) ; version précédente `…-v8.md` (`821153e2…`, vérifiée) ; rapport du tour 1 (`9734258f…`, vérifié).
Lus aussi : texte scellé (`8aa33014…`, recalculée égale, branche `prep/pilote-mr2-compte-organisme-v1`, « Liste d'arrêt » et ligne π2) ; `depense_pilote_v14_v1.py` (`9866e611…`) au commit `2f7acc1d` de `lot/compte-organisme-v1`. Aucune pièce de la sortie du pilote, aucun verdict d'arrêt, aucune clé.

## Verdict : scellable (aucune correction exigée ; deux remarques facultatives)

## Vérifications
1. **Différentiel v8 → v9 (par `diff`)** : cinq blocs. (a) titre et ligne de version (heure 15:48:37Z ; l'annonce correspond à ce qui est fait) ; (b) point 0, alinéa des arrêts gardés : couple C1-1 ; (c) point 4 : couple C1-4 ; (d) sous-section « Version 8 » : couples C1-2 et C1-3 ; (e) sous-section « Tour 1 de la v8 » ajoutée en fin de pièce (traçabilité, comme la pièce le fait pour chaque tour). Rien d'autre.
2. **Les quatre couples du tour 1** : appliqués mot pour mot (comparaison avec le rapport : les quatre « nouveau » sont présents à l'identique dans la v9 ; les quatre « ancien » ont disparu de la v9 et ne figuraient qu'une fois dans la v8). Le programme d'application vérifie les empreintes de la v8 et du rapport, l'unicité, la non-écrasement.
3. **Cohérence après correction** : plus aucune mention d'un arrêt sur la part de la machine (recherche de « machine » dans la pièce : les autres occurrences sont la machine comme exécutant, le champ `machine` de la dépense et le code 3 du programme de dépense, tous sans arrêt du lecteur). Les arrêts gardés restent tous dans la « Liste d'arrêt » du texte scellé (empreintes ; C-16/C-17 ; réponse brute ou témoin absent ; `cout_excessif` ; « Dépense d'un fournisseur atteignant sa part » ; « Tout arrêt (code 3) » ; reprise sur texte neuf) ; l'extension « un contrôle qu'il ne peut faire est un arrêt » est assumée par la pièce (voir R1).
4. **Faits de la sous-section ajoutée, vérifiés** : « Dépense d'un fournisseur atteignant sa part → arrêt ; aucune ligne d'extension » (texte scellé, « Liste d'arrêt ») ; ligne π2 : `argon` 9,36, `astra` 9,36, machine 3,00 (texte scellé, R-2542 et devis) ; `depense_pilote_v14_v1.py` : `MACHINE = 3.0`, `sous_la_part` de la machine = coût ≤ 3, code 3 si l'un des `sous_la_part` (proposeurs, machine), `pi1_sous_la_ligne`, `pi2_sous_la_ligne` est faux ; empreinte `9866e611…` identique au commit `2f7acc1d` et à la branche. Le traitement de `appels_complets_illisibles` (v8) n'est pas touché par la v9 ; je l'avais vérifié sur le code au tour 1 de la v8 (rapport du tour 1) et le différentiel n'y change rien.
5. **Identifiants de modèle** : aucun (« modèle A », « modèle C » seulement ; la seule occurrence de « Claude » est la formule existante « identifiant de modèle Claude » du plan de rendu).

## Corrections exigées
Aucune.

## Remarques facultatives (non exigées)
- **R1** (reprise du tour 1) : la règle « un contrôle qu'il ne peut faire est un arrêt » reste une extension assumée du texte scellé ; la mère doit le savoir.
- **R2** : au point 4, « une part dépassée est déjà un arrêt du point 0 » et « `sous_la_part` … doivent tous être vrais » se lisent bien avec « la machine … rapportée sans arrêt » ajouté ; le lecteur attentif ne confondra pas ; rien à changer.

## Pour la session mère
- Pas d'écart au texte scellé dans la v9, hors l'extension R1 (déjà connue).
- Un dépassement des 3 USD de la machine n'arrête pas le lecteur : il est écrit au rapport comme nœud de Lazar ; le programme de dépense rend alors le code 3 (code du programme de dépense, non arrêt du pilote).
- La v9 peut être scellée telle quelle, puis remise au lecteur.

Incident de ma main : aucun (aucun fichier existant modifié, aucun commit ; un extrait du texte scellé dans le scratchpad ; la récupération des branches par `git fetch` a mis à jour des références distantes locales, sans clone).
