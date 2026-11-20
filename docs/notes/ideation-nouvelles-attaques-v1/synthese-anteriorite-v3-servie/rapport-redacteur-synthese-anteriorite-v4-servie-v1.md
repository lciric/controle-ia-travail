# Rapport du rédacteur — synthèse d'antériorité servie, version 4 — v1

Pièce de travail (classe C), écrite le 2026-11-20 sur le message de la mère qui suit la contre-lecture de la v3 servie (`contre-lecture-synthese-v3-servie-v1.md`, `a9cdf12c180d0f5abc5eb34ea1e8252712e51c1630d6dd121108384ab4f1ea03`, vérifiée contre son compagnon, « OK », lue en entier, ainsi que son JSON essayé). Mêmes interdits que le mandat `e4c28f8e…`. Processeur seul : aucun appel à un fournisseur, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune publication. Aucune méthode d'attaque, aucun procédé, rien d'ajouté au fond. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

**Version 4 écrite, relevé à 0, à faire vérifier par le même contre-lecteur puis à sceller par la mère.** Quatre remplacements par l'outil contre-lu, selon ce que la mère a tranché : C1 au choix « plusieurs », C2 au texte exact de la contre-lecture, section 8.1 retirée, table des corrections retirée. C3 et C4 sont sans objet (leurs deux lignes sont dans les parties retirées). Rien d'autre ne change.

## 1. Pièces et empreintes

Dossier D = `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-synthese-anteriorite-v3/`.

| pièce | empreinte |
|---|---|
| cible : `D/synthese-anteriorite-pilier-attaque-v3-servie.md`, égale à la v3 versée dans le dépôt (empreinte recalculée sur le fichier versé) | `7aa7750d961dcc0191d0da6d218c73c30bd8c8901f6126dbe776393c4c638450` |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |
| `D/remplacements-synthese-v3-v4-servie-v1.json` | `07cbff7401b215313b05b1271ac78070c0173cc07403829562d23485020b74ab` |
| `D/synthese-anteriorite-pilier-attaque-v4-servie.md` | `939aa84a3f66647e6fe3f08bf80134e3d08f9b1408ac0e61d12ddd3fecb3830b` (compagnon, journal et compagnon du journal écrits par l'outil) |

## 2. Remplacements (4)

Sortie de l'outil : « FAIT : 4 remplacement(s) ». La v4 a 286 lignes (311 dans la v3).

| rang | ligne de la v3 | ancien → neuf |
|---|---|---|
| 1 (C1) | 266 | `de trois fabricants differents (la v2b en nommait quatre)` → `de plusieurs fabricants differents` |
| 2 (C2) | 27 | `La demonstration d'avant-entretien doit preserver ce temoin.` → `Toute demonstration anterieure a la porte G1 doit preserver ce temoin.` |
| 3 | 256 à 261 | section 8.1 entière → texte vide |
| 4 | 293 à 311 | table des corrections entière, avec le trait qui la précède → texte vide |

**Bornes des deux sections retirées.** Une ancre par section, d'un seul tenant, sur plusieurs lignes.
- Section 8.1 : du premier caractère du titre « ### 8.1 Refus et acceptations » jusqu'à la ligne vide qui précède « ### 8.2 Passage de trois a cinq especes », comprise. Le titre « ## 8. … » et la ligne vide qui le suit restent ; « ### 8.2 » vient juste après, comme « ### 8.1 » avant.
- Table des corrections : de la ligne vide qui suit le dernier paragraphe de l'avertissement, puis le trait « --- », le titre « ## Table des corrections v2 → v2b », son paragraphe et les douze lignes de la table, jusqu'à la fin du fichier. La v4 finit sur le dernier paragraphe de l'avertissement et son saut de ligne.

**Compte des ancres avant l'appel.** Ancres 1 et 2 : `grep -c -F -e`, 1 chacune. Ancres 3 et 4 : `grep` lit ligne par ligne et ne peut pas compter une ancre de plusieurs lignes ; j'ai compté par `grep -c -F -e` leur première et leur dernière ligne de texte (1 chacune : le titre de 8.1 ; la dernière phrase de 8.1 ; le titre de la table ; la dernière ligne de la table), et l'ancre entière par le mode « ancres » de mon programme, à l'octet comme l'outil : `D/sortie-compte-ancres-v3-v4-v1.txt`, quatre ancres à exactement une occurrence. L'outil refuse de lui-même toute ancre qui n'est pas unique (sa règle 2).

## 3. Relevé sur la v4

Même programme que pour la v3 (`D/compter_ancres_et_relever_motifs_v1.py`, `d479f65b…`, inchangé), sortie `D/sortie-releve-motifs-apres-v4-servie-v1.txt` : **motifs du mandat, total 0** (chacun des dix-sept à 0) ; **motifs complémentaires, total 0**. Différentiel `D/differentiel-synthese-v3-v4-servie-v1.diff` (`diff -u`, relu en entier) : trois blocs, rien hors des quatre remplacements.

## 4. Remarques

1. **Numérotation.** La section 8 commence maintenant par « 8.2 », puis « 8.3 » : je n'ai pas renuméroté (« rien d'autre ne change »). Le titre de la section 8 et son premier paragraphe (8.2) parlent encore du « run v2.6 a trois especes » et de « 3 tours incomplets » : du fond de 8.2, gardé.
2. **« Zero refus »** reste à la ligne 4 (en-tête, « Source ») : elle n'était pas visée. C'est le seul reste du sujet de la section 8.1.
3. **Renvois devenus sans cible** : aucun dans le texte gardé. Le seul renvoi aux « sections 8.1, 8.2 et 8.3 » était dans le paragraphe de la table, retiré avec elle.
4. La ligne 5 dit toujours « cinq modeles de quatre lignees » ; avec « plusieurs fabricants » à la section 8.2, plus rien ne se contredit.
5. `diff` a rendu le code 1 (fichiers différents), ce qui est attendu.

## 5. Écarts

Aucun écart à ce que la mère a tranché. Une précision, dite au § 2 : les deux ancres de plusieurs lignes ne peuvent pas être comptées d'un seul `grep` ; elles le sont par leurs lignes de bord et, entières, par mon programme.

## 6. Fichiers rendus (dossier D, chacun avec son compagnon `.sha256`)

`synthese-anteriorite-pilier-attaque-v4-servie.md` (et son journal) ; `remplacements-synthese-v3-v4-servie-v1.json` ; `sortie-compte-ancres-v3-v4-v1.txt` ; `sortie-releve-motifs-apres-v4-servie-v1.txt` ; `differentiel-synthese-v3-v4-servie-v1.diff` ; ce rapport.

— rédacteur neuf, modèle F
