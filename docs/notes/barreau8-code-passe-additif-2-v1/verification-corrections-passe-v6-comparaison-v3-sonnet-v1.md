# Vérification des corrections — passe v6 et programme de comparaison v3 — Sonnet 5.5

Heure : 2026-11-24T11:27Z à 11:33Z (`date -u`). Commit vérifié : `b6030e46c9` (branche `barreau8/code-passe-additif-2-v1`, rattachée à nouveau après la lecture).
Lu de plus : `corrections-contre-lecture-passe-v6-comparaison-v2-v1.md` ; `comparer_interface_v6_v7_v3.py` (diff contre la v2) ; `test_barreau8_comparer_interface_v6_v7_v3.py` (diff contre la v2) ; `test_barreau8_moniteurs_passe_v6_complements_v1.py` en entier ; `git diff --stat 3405f7af b6030e46`. Même cloisonnement qu'à la première mission.

## Contrôles
- `passe_recalcul_v6.py` : `sha256sum -c` OK ; `git diff 3405f7af b6030e46` sans ligne pour ce fichier : **inchangé**. Le commit n'ajoute que 12 fichiers (aucun existant modifié ; la v2 reste intacte, R12). Les quatre fichiers nouveaux ont leur compagnon `.sha256`, tous OK.
- Diff v2 à v3 du programme : numéro de version et avertissement ; refus si `note.chemin` de la fiche diffère de `CHEMIN_NOTE_V7` ; dans `ecrire`, refus préalable si l'une des deux pièces ou un compagnon existe, puis `controler_contre_la_version_1` rejoué en mémoire, code 2 sans écriture. Rien d'autre ne change (calcul identique).
- Rejeu : 59 passés (49 programme v3, 10 compléments).
- Mutations contre le fichier de compléments : `_posterieure` en `>=` : **tuée** (4 échecs) ; garde E = 1 « toujours vraie » : **tuée** (1 échec).

## Les dix constats
1. **Porté.** `ecrire` vérifie l'absence des cibles, rejoue le contrôle v1, refuse sans rien écrire ; essais : divergence de la v1 (code 2, rien écrit), écriture saine puis `controler` conforme, table seule présente (refus, aucune pièce orpheline).
2. **Porté.** Artefacts de `controler_contre_la_version_1` (bloc, table de l'additif 1, statut d'un autre champ), de `ecarts_aux_valeurs_attendues` (T = 32, « nœud ») et de `ecrire` (code 2).
3. **Porté.** Refus et essai `match="note.chemin"`.
4. **Porté** (gardé, déclaré).
5. **Porté.** Quatre essais à heure égale ; la mutation `>=` est tuée.
6. **Porté.** Essai direct à E = 2 ; mutation tuée. La redondance avec `exiger_table_neuve` est gardée et déclarée.
7. **Porté en partie.** Déclaré dans le fichier de corrections ; le tableau cite aussi « notice », mais la notice v7 n'est pas modifiée (aucune phrase ne dit que seul le rapport v5 est refusé par empreinte). À redire au rapport de conformité scellé ; sinon sans conséquence sur le code.
8. **Porté** (déclaré ; conforme à la lettre de M-5).
9. **Porté.** Additif 2 altéré, `transformers` seul absent, adaptateur élève et témoin-jumeau d'une autre empreinte, adaptateur sans compagnon.
10. **Porté** (la notice dit déjà le contrôle sur le dépôt, et la passe le recontrôle par la garde P3).

## Défaut neuf
Aucun défaut de code. Remarques : le nom de la pièce réécrite reste `comparaison-interface-v6-v7-v2.json` (voulu par M-4) alors que le programme est en v3 (le numéro figure dans la pièce) ; les essais complémentaires dépendent de l'import du fichier d'essais de la passe v6 (couplage assumé).

## Conclusion
**Conforme**, sous réserve que le point 7 soit redit au rapport de conformité scellé.

Résumé : (1) passe v6 inchangée, empreinte et diff vides ; (2) programme v3 : seules les corrections 1 et 3 changent le code ; (3) 59 essais passent ; (4) mutations `>=` et E = 1 tuées ; (5) dix constats portés (le 7 en partie, par déclaration), aucun défaut neuf.
