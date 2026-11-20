# Rapport du rédacteur — synthèse d'antériorité servie, version 5 — v1

Pièce de travail (classe C), écrite le 2026-11-20 sur le message de la mère qui suit la vérification de la v4 (`verification-synthese-v4-servie-v1.md`, `ca1258f9f6c4680c369d1cd10e2dac43a6ff0b75198a1db6f878b1d9f76565e9`, vérifiée contre son compagnon, « OK », lue en entier, ainsi que son JSON essayé). Mêmes interdits que le mandat `e4c28f8e…`. Processeur seul : aucun appel à un fournisseur, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune publication. Aucune méthode d'attaque, aucun procédé, rien d'ajouté au fond. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

**Version 5 écrite, relevé à 0, à faire vérifier par le même contre-lecteur puis à sceller par la mère.** Les trois retouches D1, D2 et D3 sont appliquées à la lettre, rien d'autre. La sortie a la même empreinte que l'essai du contre-lecteur (`f74c6064…`).

## 1. Pièces et empreintes

Dossier D = `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-synthese-anteriorite-v3/`.

| pièce | empreinte |
|---|---|
| cible : `D/synthese-anteriorite-pilier-attaque-v4-servie.md` | `939aa84a3f66647e6fe3f08bf80134e3d08f9b1408ac0e61d12ddd3fecb3830b` |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |
| `D/remplacements-synthese-v4-v5-servie-v1.json` (trois paires, égales à celles du JSON essayé du contre-lecteur) | dans son compagnon |
| `D/synthese-anteriorite-pilier-attaque-v5-servie.md` | `f74c606423bbbc4da88578508209d3d87cb133b4b7cd8e1728606cde58484e73` (compagnon, journal et compagnon du journal écrits par l'outil) |

## 2. Remplacements (3)

Chaque ancre comptée à 1 par `grep -c -F -e` avant l'appel (trois appels). Sortie de l'outil : « FAIT : 3 remplacement(s) ». La v5 a 286 lignes, comme la v4.

| rang | ligne | ancien → neuf |
|---|---|---|
| 1 (D1) | 4 | ` Zero refus.` (avec l'espace qui précède) → texte vide ; la ligne finit sur « riposte). » |
| 2 (D2) | 256 | `### 8.2 Passage de trois a cinq especes` → `### 8.1 Passage de trois a cinq especes` |
| 3 (D3) | 268 | `### 8.3 Changements de fond` → `### 8.2 Changements de fond` |

## 3. Relevé sur la v5

Même programme (`D/compter_ancres_et_relever_motifs_v1.py`, `d479f65b…`, inchangé), sortie `D/sortie-releve-motifs-apres-v5-servie-v1.txt` : **motifs du mandat, total 0** (chacun des dix-sept à 0) ; **motifs complémentaires, total 0**. Différentiel `D/differentiel-synthese-v4-v5-servie-v1.diff` (`diff -u`, relu en entier) : trois blocs, trois lignes changées, rien d'autre.

## 4. Remarques

1. Le titre « ## 8. Ce qui a change par rapport au run v2.6 a trois especes » et le renvoi « (section 2) » du point 3 de la section 8.1 neuve restent tels quels, comme le dit la vérification.
2. `diff` a rendu le code 1 (fichiers différents), ce qui est attendu.

## 5. Écarts

Aucun.

## 6. Fichiers rendus (dossier D, chacun avec son compagnon `.sha256`)

`synthese-anteriorite-pilier-attaque-v5-servie.md` (et son journal) ; `remplacements-synthese-v4-v5-servie-v1.json` ; `sortie-releve-motifs-apres-v5-servie-v1.txt` ; `differentiel-synthese-v4-v5-servie-v1.diff` ; ce rapport.

— rédacteur neuf, modèle F
