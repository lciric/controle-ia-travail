# Vérification des corrections — additif 1 v3 au préenregistrement court v9 et devis v9 — v1

Pièce de travail (classe C), 2026-11-20, relevé de `date -u` : 14:21:59Z, après les rejeux et les relevés, avant l'écriture. Contre-lecteur neuf, modèle O, auteur de la contre-lecture `6ffbd3bc…` et de la vérification `013991ea…`. Mandat `799b14c6…`, en-tête compris. Processeur seul : aucun appel, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune publication. Aucune méthode d'attaque, aucun procédé, aucun nom ni énoncé de mode, aucune case nommée, aucune valeur de clé, aucun identifiant de modèle. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

**À corriger.** Sept remplacements, en deux jeux.

Ce qui est vérifié :
- les deux passes rejouent à l'octet ;
- V1 à V4, W1 et W2 sont égaux, à l'octet, à mes jeux ;
- aucun chiffre ne change ;
- le relevé « aucune recette », rejoué, est conforme ;
- les textes de la main du rédacteur sont justes à la lettre de la décision de 14:08Z.

Les corrections viennent de deux faits postérieurs à la v3 ou que la v3 ne porte pas :
1. **GO-2026-11-20-65** (14:20Z, « go 1 2 »), sur `origin/main` (`1b23c83b`), et R-4291 lèvent la réserve. G1 à G4 la remplacent par le renvoi à cet accord. G5 ajoute ces lignes du registre à la table des pièces.
2. **R-4289** fixe une règle neuve pour la part de Luc : son reste relu, moins le pire des lots non clos sur cette clé. Le devis v9 dit le contraire : la dépense de l'étage 2 « ne se prend pas sur les 214 USD de cette course ». V5 et W3 alignent les deux textes.

## 1. Pièces et empreintes

| pièce | empreinte | vérification |
|---|---|---|
| additif 1 v3 | `5eae11c676462e14f0303a566ad6d1b9c144c634d608cec1f2cc54a489147f3b` | compagnon « OK » ; rejeu égal (`cmp`) |
| devis v9 | `a3e9dff3b2e5e19e6ab79297fe3895a0d5bf2f82ce7e06059f5a63a52fdb2fd3` | compagnon « OK » ; rejeu égal (`cmp`) |
| jeux | `7b31318f…` (18 remplacements) ; `fa4f8191…` (7 remplacements) | compagnons « OK » |
| différentiels | `e6505d20…` ; `25686daa…` | compagnons « OK » |
| rapport du rédacteur | `500a27941307355f8992f24b2b16f486366f7c8a708d9b7b996450cd6bba452c` | compagnon « OK » |
| ma vérification, au chemin versé | `013991ea…` | recalculée |
| `registres/go.md` et `registres/decisions.md` sur `origin/main` (`1b23c83b18ce2f98aa9f3dba549b6bf9ffc63a53`) | `153eb6f6…` ; `36fd07f3…` | recalculées ; GO-2026-11-20-65 et R-4287 à R-4291 lus |

## 2. Rejeux et égalité des jeux

- Additif v2 (`ed73f647…`) avec le jeu `7b31318f…` : la sortie vaut `5eae11c6…`, égale à l'additif v3.
- Devis v8 (`4a9fc6b4…`) avec le jeu `fa4f8191…` : la sortie vaut `a3e9dff3…`, égale au devis v9.
- Le programme `comparer_jeux_v1.py` confronte mes jeux à ceux du rédacteur. V1 à V4 y sont égales à l'octet aux entrées 1 à 4 du jeu de l'additif, W1 et W2 aux entrées 1 et 2 du jeu du devis.

## 3. Textes de la main du rédacteur

- **Clé n° 30 et cinquième entrée**, « suites de GO-2026-11-20-59, sous réserve du mot de Lazar » (§ 2, points a et d ; § 4 bis ; statut) : fidèle à la décision de 14:08Z et à R-4289 (« posés à Lazar »). GO-2026-11-20-65 rend cette réserve caduque (G1 à G4).
- **« Sans ce mot, la clé n° 30 ne tire rien, et la liste reste à quatre entrées »** : la conséquence est juste. Sans le tirage, R-4288 ne donne aucune autre manière d'avoir une case. Sans la cinquième entrée, la remise de la carte tombe sous les arrêts n° 17 et 18 (V1, silence 4). Dans les deux cas la levée ne sert à rien, et le texte le dit, sans repli silencieux. Elle devient sans objet par GO-2026-11-20-65 : G2 et G3 la retirent.
- **Arrêt n° 27, « proposé »** : lettre juste. La règle entre et porte son épreuve (V4), mais ne prend le numéro que si la mère le veut. À elle de le dire au scellement.
- **Tenue** : titre, date, statut, phrase de version, table (devis v9, chemins de la v3, vérification), entrée « Vérification 1 » : juste. La version de devis qui va à Lazar est dite deux fois au devis : juste.

## 4. Aucun chiffre ne change ; aucune recette

- Nombres neufs de l'additif v2 → v3 : le seul est « 27 » (le numéro d'arrêt proposé). Du devis v8 → v9 : le seul est « 15 », une heure (`sortie-nombres-neufs-v2-v3.json`). Le calcul v6 et sa sortie sont inchangés.
- Le relevé « aucune recette » v2, rejoué sur l'additif v3 et le devis v9 (`sortie-releve-aucune-recette-v3.json`), rend les mêmes signaux qu'à la vérification 1 et la même explication : nom de fichier, gabarit de S15, noms de maison dans les citations, premier mot d'une valeur de l'axe des menaces selon la décision de la mère. Il ne trouve aucune case nommée et aucune marque de recette. **Conforme.** Les clés de sa sortie gardent les noms « additif_v2 » et « devis_v8 », écrits en dur dans le programme ; les tailles lues (46 157 et 75 295 octets) sont bien celles de la v3 et du devis v9.

## 5. Les six écarts du rapport

1. **« Devis v8 » dans l'additif v3** : quatorze occurrences sur dix lignes. Cinq lignes l'emploient au présent : 36, 130, 134, 141, 169. Les autres relèvent de l'histoire. **Acceptable**, sans correction :
   - la phrase de version (ligne 9) donne la règle de lecture « « devis v8 », dans ce texte, se lit « devis v9 » » ;
   - la table (ligne 22) nomme le devis v9, son chemin et son empreinte ;
   - la v9 scellée a le même précédent (« devis v3 » lu « devis v6 », point (d)).

   Une réserve : à la ligne 169, « le devis v8 va à Lazar » est la citation de la lecture de la mère. La règle de lecture la transforme, et le devis v9 le dit en clair (« c'est ce devis v9 qui va à Lazar »). Le rédacteur de la v4 peut récrire ces cinq lignes s'il les touche, mais rien ne l'exige.
2. La lecture de 14:01Z, gardée au devis avec la phrase ajoutée : juste.
3. La conséquence « sans ce mot » : juste (§ 3) ; sans objet depuis GO-2026-11-20-65.
4. Copie de travail à `…/additif-1-v3/` : c'est là que les pièces sont versées ; juste.
5. Décisions inscrites : je l'ai vérifié à la lettre sur `origin/main`.
   - R-4288 porte la case tirée parmi les cases de sabotage, le scellement avant lecture, « la session à part propose, Lazar retient », « conçoit des seuils », la déclaration, le contrôle par programme et l'inscription de l'instance, ainsi que « une ou plusieurs cartes ». Ce sont les points a, b, c, d et f.
   - R-4289 porte : pas de second tirage ; fournisseurs ; N-054 l. 60 ; recommandations admises sauf écart ; les deux points posés à Lazar ; **la part de Luc** (V5, W3).
   - Les points e (fiches sœurs), g (autre menace) et i (terme) ne sont pas inscrits mot pour mot. Le point g suit de « parmi les cases de sabotage ».
   - La décision de 14:08Z (« suites de GO-59, sous réserve » ; arrêt n° 27 proposé) n'est pas inscrite comme telle. R-4291 lève la réserve.
   - R-4289 dit aussi « Cinq espèces lues sous GO-08 et GO-60 ». C'est la décision de 13:45Z, que celle de 14:01Z (R-4287) a remplacée sur le mot de Lazar. Le registre ne dit pas laquelle prime (§ 7).
6. Ancres comptées par l'outil : j'ai compté les miennes par `grep -c -F -e`.

## 6. Corrections

Les textes exacts font foi dans `corrections-verification-additif-1-v3-v2.json` (6 remplacements) et `corrections-verification-devis-v9-v1.json` (1 remplacement). Chaque ancre est comptée une fois par `grep -c -F -e`. Essais par l'outil sur des copies : `45468c90…` pour l'additif, `df11ef02…` pour le devis. Le brouillon `corrections-verification-additif-1-v3-v1.json` (V5 seule) est remplacé par le jeu v2, qui la reprend telle quelle.

**Sur l'additif v3 :**

V5 — § 6, « Ce que le retrait ne change pas » : la part de Luc (R-4289).

    Ancien : celle de Luc (214 USD), X et la règle de la part de Rigaud.
    Neuf : X et la règle de la part de Rigaud. La part de Luc, 214 USD au texte scellé, ne change pas par le retrait ; elle se fixe au complément de valeurs sur son reste relu moins le pire des lots non clos sur cette clé (R-4289 : étage 2, 87,7701 USD), et c'est un nœud de Lazar si elle tombe sous le cas haut de ses rôles, 124,35 USD ; les rapports et marges de Luc écrits dans ce texte le sont à 214 USD.

G1 — statut.

    Ancien : Deux de ses points, la clé de tirage n° 30 et la cinquième entrée de la liste nominative, sont écrits sous réserve du mot de Lazar.
    Neuf : Deux de ses points, la clé de tirage n° 30 et la cinquième entrée de la liste nominative, sont accordés par Lazar (GO-2026-11-20-65 ; R-4291).

G2 — § 2, point a, clé n° 30 : la réserve et la phrase « Sans ce mot » sont retirées.

    Ancien : il est écrit ici comme **suite de GO-2026-11-20-59, sous réserve du mot de Lazar** (décision de la mère, 14:08Z) : GO-2026-11-20-59 dit « son choix scellé avant toute lecture », non un tirage ; la mère pose la clé n° 30 à Lazar, avec sa recommandation (oui). Sans ce mot, la clé n° 30 ne tire rien, et aucune carte de cette course ne nourrit le mode tenu à l'écart.
    Neuf : il est accordé par Lazar, GO-2026-11-20-65, point 1, à la lettre : « La case d'où viennent les cartes du mode tenu à l'écart est tirée, par une clé de tirage neuve (n° 30, un rang parmi les cases servies de sabotage, ordre canonique), scellée avant toute lecture ; écart accordé à « aucune autre méthode de tirage n'est permise » (v9 l. 311). » GO-2026-11-20-59 disait « son choix scellé avant toute lecture », non un tirage : GO-2026-11-20-65 le tranche.

G3 — § 2, point d, cinquième entrée : la réserve et la phrase « Sans ce mot » sont retirées. La phrase qui suit (« La remise de la carte ne tombe donc plus sous les arrêts n° 17 et n° 18 ») redevient vraie sans condition.

    Ancien : C'est une **suite de GO-2026-11-20-59, sous réserve du mot de Lazar** (décision de la mère, 14:08Z) : GO-2026-11-20-57, point 2, nomme quatre entrées, et GO-2026-11-20-59 accepte une instance qui doit recevoir la carte sans l'inscrire ; la mère pose cette cinquième entrée à Lazar, avec sa recommandation (oui). Sans ce mot, la liste reste à quatre entrées, et la remise de la carte reste sous les arrêts n° 17 et n° 18.
    Neuf : Elle est accordée par Lazar, GO-2026-11-20-65, point 2, à la lettre : « L'instance qui conçoit le mode tenu à l'écart entre en cinquième nom de la liste nominative des lecteurs de la quarantaine (GO-2026-11-20-57 en nommait quatre). »

G4 — § 4 bis, dernier paragraphe.

    Ancien : Ce sont des **suites de GO-2026-11-20-59, sous réserve du mot de Lazar** : la mère les lui pose, avec sa recommandation (oui) ; ils ne valent pas avant ce mot (décision de la mère, 14:08Z).
    Neuf : Tous deux sont accordés par Lazar (GO-2026-11-20-65, points 1 et 2 ; R-4291) : ce ne sont plus des écarts ouverts.

G5 — table des pièces : une ligne ajoutée après celle des décisions.

    Ancien : | décisions : R-4269, R-4274 à R-4284 | `registres/decisions.md` sur `main` | `3c8fc58ad18cbdf352f8fe9cd8df2b44a564383260234b99ee6d43e721423049` |
    Neuf : (la même ligne, puis)
    | accords et décisions postérieurs : GO-2026-11-20-65 ; R-4287 à R-4291 | `registres/go.md` et `registres/decisions.md` sur `main`, commit `1b23c83b18ce2f98aa9f3dba549b6bf9ffc63a53` | `153eb6f682698639110c399737c42d40320cf0889a829d0364518bbae6b885b1` ; `36fd07f3c3d8999f49cedcd112601a51997328affa8b6061a303fcaf4eb572cb` |

**Sur le devis v9 :**

W3 — § 10.6, dernier point : la part de Luc (R-4289).

    Ancien : - La clé Luc paie aussi le juge de l'étage 2 de la ligne 3, une autre course (GO-2026-11-20-55, point 3) : hors de ce devis ; sa dépense ne se prend pas sur les 214 USD de cette course.
    Neuf : - La clé Luc paie aussi le juge de l'étage 2 de la ligne 3, une autre course (GO-2026-11-20-55, point 3) : hors de ce devis. Depuis R-4289, la part de Luc pour cette course est son reste relu moins le pire des lots non clos sur la clé (étage 2 : 87,7701 USD), écrite au complément de valeurs ; c'est un nœud de Lazar si elle tombe sous le cas haut de ses rôles, 124,35 USD. Les « 214 » de ce paragraphe et de la table ci-dessus sont la part d'avant cette règle.

**Laissé tel quel.** La phrase de version de la v3 (ligne 9) garde « sous réserve du mot de Lazar » : c'est l'histoire de la v3. La phrase de version de la v4 dira que GO-2026-11-20-65 lève la réserve.

## 7. Points pour la mère

1. **R-4289 et R-4287 se contredisent** sur le mot de Lazar : R-4289 dit « Cinq espèces lues sous GO-08 et GO-60 » ; R-4287 dit que GO-60 ne lève pas « rien ne court avant le mot ». L'additif et le devis suivent R-4287. Une ligne du registre, qui ne s'efface pas, devrait dire laquelle prime.
2. **R-4289, part de Luc** : la règle entre aux deux textes par V5 et W3 et se chiffre au complément. Le chiffre de l'étage 2, 87,7701 USD, est celui de R-4289 ; je ne l'ai pas vérifié sur sa pièce.
3. **Arrêt n° 27** : numéro à prendre ou non au scellement.
4. Les points e et i du sens des conditions, et la décision de 14:08Z, ne sont pas inscrits mot pour mot ; R-4291 couvre la levée de la réserve.

## 8. Écarts du vérificateur

- E1. Mes premiers jets de V5 et W3 ont été essayés sur des copies (`17fa414f…`, `df11ef02…`). Le jeu de l'additif a ensuite été réécrit en v2 pour y joindre G1 à G5, sans écraser le v1.
- E2. Les essais de l'outil ont laissé, dans mon dossier, des copies et leurs journaux : ce sont des essais, non des pièces.

## 9. Fichiers

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-additif-1-v9/`. Chacun a son compagnon `.sha256` :
- `verification-additif-1-v3-devis-v9-v1.md` (cette pièce) ;
- `corrections-verification-additif-1-v3-v2.json` ; `corrections-verification-devis-v9-v1.json` ;
- `comparer_jeux_v1.py` ; `sortie-nombres-neufs-v2-v3.json` ; `sortie-releve-aucune-recette-v3.json`.

— contre-lecteur neuf, modèle O
