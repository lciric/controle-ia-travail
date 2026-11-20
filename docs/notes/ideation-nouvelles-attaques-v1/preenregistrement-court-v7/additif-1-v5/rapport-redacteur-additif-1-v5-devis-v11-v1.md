# Rapport du rédacteur — additif 1 v5 au préenregistrement court v9 et devis v11 — v1

Pièce de travail (classe C), 2026-11-20 ; date des deux pièces : 14:32:16Z, l'heure du journal de la première passe de l'outil. Mandat `9b1e92db…`, toujours en vigueur ; demande de la session de l'organisme après la troisième vérification. Processeur seul : aucun appel, aucune dépense, aucun lancement, aucune écriture dans le dépôt, aucun commit, aucune publication. Aucune méthode d'attaque, aucun procédé, aucun nom ni énoncé de mode, aucune case nommée, aucune valeur de clé, aucun identifiant de modèle. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

- **Additif 1 v5** : `472c2adf8c150b281cdaf1dc01165b50956b3053760c4b7fc4578c25bc4ad53c`.
- **Devis v11** : `205e08f23ef9ced92a35340b8fad38765b08483a2129ee32550081d1bd043570`.
- Ni l'un ni l'autre n'est scellé. Aucun chiffre ne change ; le calcul v6 et sa sortie ne sont pas touchés.

## 1. Pièces lues

La vérification (`9e08297c2934deb2d97c702d82a6a55d6398c5d4ef21849d3071333b2fd3787a`, lue en entier) et ses deux jeux (`9ccaf626…`, `fdd0344a…`), « OK » contre leurs compagnons ; l'additif v4 (`8e3d77a3…`) et le devis v10 (`5737ec6e…`) versés, « OK ».

## 2. Première passe : le jeu du vérificateur, tel quel

| pièce | corrections | sortie | essai du vérificateur |
|---|---|---|---|
| additif | X1, X2 (2 remplacements) | `3682b3c2e6106d10a5df0fb379eef22aebaf06bfea78fed6edc724458c3054d4` | `3682b3c2…` : même empreinte |
| devis | Y1 (1 remplacement) | `e869d1835bf6e3183330d6f56093b507bc7a10ebf27acadeca28004818b6b7b6` | `e869d183…` : même empreinte |

## 3. Seconde passe : la tenue, et rien d'autre

- **Additif**, 9 remplacements : titre ; date ; statut ; phrase de version ; table (devis v11, son chemin et son empreinte, sur trois lieux de sa ligne ; chemins de la v5 ; ligne de la vérification 3).
- **Devis**, 3 remplacements : titre ; phrase de version ; statut.

## 4. Écarts

1. **Égalité aux essais constatée par l'empreinte, non par `cmp`** : je n'ai pas le chemin des fichiers d'essai du vérificateur ; l'empreinte entière de ma sortie est égale au préfixe qu'il donne. Le `cmp` reste à faire par lui ou par la mère.
2. **La section « Contre-lecture » de l'additif n'est pas touchée** : elle dit encore « La v4 n'est pas vérifiée » et n'a pas d'entrée « Vérification 3 ». La demande bornait la tenue au titre, à la date, au statut, à la phrase de version et à la table ; le statut et la phrase de version disent l'état. Si la mère veut l'entrée, elle l'écrit avec le traitement.
3. **Les mentions « ce devis v10 » qui va à Lazar** ne sont pas récrites au devis ; la phrase de version de la v11 dit que c'est le devis v11. À l'additif, la phrase de version dit que « devis v8 », « devis v9 » et « devis v10 » se lisent « devis v11 ».
4. **Copie de travail sur la branche** : écrite à `…/preenregistrement-court-v7/additif-1-v5/`, par analogie.
5. La date des deux pièces est l'heure du journal de la première passe.

## 5. Fichiers rendus

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-additif-1-v5/`. Chacun a son compagnon.

- `additif-1-preenregistrement-court-v9-mode-tenu-a-l-ecart-et-retrait-espece-6-v5.md` et son journal
- `devis-course-nouvelles-attaques-v11.md` et son journal
- `etape-1-additif-1-v4-plus-X1-X2.md` ; `etape-1-devis-v10-plus-Y1.md` ; leurs journaux
- `remplacements-additif-1-etape-1-vers-v5-v1.json` ; `remplacements-devis-etape-1-vers-v11-v1.json`
- `differentiel-additif-1-v4-v5-v1.diff` ; `differentiel-devis-v10-v11-v1.diff`
- `rapport-redacteur-additif-1-v5-devis-v11-v1.md` (cette pièce)

— rédacteur, modèle F
