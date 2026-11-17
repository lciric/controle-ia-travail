# Contre-lecture du devis du banc de calibration MR-2 — fin de tour 1 (lecteur neuf, modèle C) — v1

- **Pièce lue en entier** : `devis-banc-calibration-mr2-v3.md`, empreinte `ec5a6e99313dd1a48f4105e756813b3500a1181cc66babbb0af4bfb7c5a62eb2` (égale à son compagnon).
- **Lu aussi** : rapport du tour 3 (`contre-lecture-devis-banc-calibration-mr2-tour3-v1.md`) ; état du code v68 transmis par la consigne (non revérifié par moi, lecture seule du devis).
- **Heures** (`date -u`) : début 2026-11-17 00:26Z ; fin : dernière ligne.

## Verdict : corrections (0 majeure, 3 mineures)

Les deux mineures du tour 3 (m8, m9) **restent** dans la v3 : chaque « ancien » figure une fois (`grep -cF` = 1). Je les confirme. J'ajoute une mineure neuve (m10, base de la durée au pire). Le fond (lieu, durée, minuterie, séparation crédits et hors crédits, Q-B1 à Q-B3) tient. Aucune majeure : le devis n'affirme rien de contraire à l'état du code v68 ni aux conditions de GO-2026-11-13-01 et -02.

## 1. Les deux mineures du tour 3

- **m8 confirmée** : 1 − (1 − 0,5^8)^24 = 0,08966 (0,0897) ; 1 − (1 − 0,6^8)^24 = 0,33404 (0,3340). La v3 écrit 0,089 et 0,335 (section 11, ligne M1). Le texte de la section 7 point 5 (≈ 9 %, ≈ 33 %) reste exact.
- **m9 confirmée** : la sous-section du tour 2 affirme « le même modèle a lu et corrigé » et « même modèle au rapport et aux corrections », alors que la provenance est déclarée non établie.

## 2. Corrections (couples « ancien → nouveau », chaque ancien unique dans la v3, vérifié)

**m8**
- Ancien : `recalculées : 1 − (1 − 0,5^8)^24 = 0,089 ; 1 − (1 − 0,6^8)^24 = 0,335)`
  Nouveau : `recalculées : 1 − (1 − 0,5^8)^24 = 0,0897 ; 1 − (1 − 0,6^8)^24 = 0,3340)`

**m9**
- Ancien : `à ce tour, le même modèle a lu et corrigé.`
  Nouveau : `à ce tour, le même modèle a peut-être lu et corrigé (provenance non établie, comme au tour 1).`
- Ancien : `(même modèle au rapport et aux corrections à ce tour, et peut-être au tour 1`
  Nouveau : `(peut-être le même modèle au rapport et aux corrections à ce tour, et peut-être au tour 1`

**m10 (neuve) — base de la durée au pire non dite, facteur « machine plus lente » ambigu.** Section 4 : l'attendu 9,5 min = 6 min 17 s (moyenne) × 1,5 ; le pire 26,7 min = 8 min 55 s (maximum, non la moyenne) × 2 × 1,5 (26,75). Le facteur « × 1,5 machine plus lente » ne s'applique donc qu'au pire, ce que la phrase ne dit pas ; la base maximum n'est écrite nulle part. Les totaux (4,7 h → « ≈ 5 h » ; 12,7 h) sont justes.
- Ancien : `| 24 mondes, un processus à la fois | 24 × 9,5 min ≈ 3,8 h | 24 × 26,7 min ≈ 10,7 h |`
  Nouveau : `| 24 mondes, un processus à la fois (attendu : moyenne 6 min 17 s × 1,5 ; pire : maximum 8 min 55 s × 2 × 1,5, le facteur de la machine plus lente ne valant qu'au pire) | 24 × 9,5 min ≈ 3,8 h | 24 × 26,7 min ≈ 10,7 h |`

## 3. Vérifications demandées

1. **Mineures du tour 3** : restent toutes deux (section 1).
2. **Arithmétique refaite** : 24 × 9,5 min = 3,8 h ; 24 × 26,7 min = 10,68 h ; attendu 3,8 + 0,3 + 0,3 + 0,3 = 4,7 h (≈ 5 h) ; pire 10,7 + 0,5 + 1 + 0,5 = 12,7 h (« ≈ 13 h » ailleurs : cohérent) ; 17 × 0,17 = 2,89 ≤ 3 ; 5 × 0,052222 = 0,261 (« 0,30 » arrondi au-dessus, dit) ; 5 × 0,15 = 0,75 ; durée moyenne des 12 parties 75,5 min / 12 = 6 min 17 s ; Clopper-Pearson 0/14 : 0,23164 ; transformée : 0,042965 (≈ 0,043). Exacts. Le « 0,27 si p vaut 0,051, à 14 appels » et les bascules 0,034 et 0,051 viennent du texte scellé du pilote, que je n'ai pas le droit d'ouvrir : non vérifiés par moi (le tour 1 les avait vérifiés).
3. **Crédits et hors crédits séparés** : correct. Colonnes distinctes ; 0 sur crédits attendu et pire ; 0,30 et 3,00 hors crédits ; la section 8 le répète. Rien d'incohérent.
4. **Q-B2 et la condition « banc de calibration fait »** : Q-B2 dit exactement ce que la condition exige : sous (a), la condition « banc de calibration fait (n et seuils fixés par leurs règles) » de -01 et -02 (échéance 2026-11-30) n'est pas remplie, le banc plus large reste dû ou un mot de Lazar la lève, le défaut à 48 heures ne la lève pas. Cela concorde avec l'état transmis. **Code v68** : il existe, mais comme ligne de code du pilote ; aucun code propre à la course. Le devis lit « code v68 gelé » comme l'arbre v68 à v74 du pilote : exact. Il dit « je n'ai pas vérifié que ce code existe » (section 7 point 7 ; Q-B2) : ce n'est pas contraire à l'état, mais c'est périmé ; voir la remarque 1.
5. **Identifiant de modèle** : aucun identifiant du type `claude-…` ni nom de version de modèle. Seuls figurent les étiquettes de proposeurs du pilote `fable52`, `opus55`, `argon`, `astra` (lignes 78 à 81, 90, 126, 169, 255), qui désignent des modèles par leur étiquette scellée ; aucune correction exigée (elles renvoient au registre du pilote), à trancher par la mère (point 3 ci-dessous).

## 4. Remarques facultatives (aucune correction exigée)

1. Mettre le devis au niveau de l'état du code : couple possible. Ancien : `je n'ai pas vérifié que ce code existe. C'est` → Nouveau : `je n'ai pas vérifié que ce code existe (lecteur neuf de la fin du tour 1 : il n'existe pas de code propre à la course ; la ligne v68 à v71 est celle du pilote). C'est`. Idem pour Q-B2 : ancien `et dépend d'un code que je n'ai pas vu.` → nouveau `et dépend d'un code de la course qui n'existe pas encore (la ligne v68 existante est celle du pilote).`
2. Le devis ne dit rien des autres conditions de -01 et -02 qui touchent le banc : conception v4 dont la contre-lecture exige 9 corrections (condition 1, partielle) ; lanceur neuf, mondes et engagement du banc (déjà en section 6). Rien de contraire ; une phrase de rappel serait utile à Lazar.
3. Section 11 devra recevoir une sous-section « Tour 3 » (v4), comme le dit le rapport du tour 3.

## 5. Points pour la session mère

1. **Aucun écart à un texte scellé**, aucun mot de Lazar nécessaire pour ces corrections (forme et arrondi).
2. **Condition de la course** : la course n'a pas de code propre prêt ; la condition « banc de calibration fait » reste ouverte sous Q-B2 (a) ; l'échéance du 30 novembre des deux lignes est un risque réel (5 à 13 h de banc, plus préenregistrement, lanceur, procédure, lecture, GO). À dire à Lazar avec Q-B2 : une extension de ligne est interdite, donc une ligne expirée exige un nouveau mot.
3. **Étiquettes de proposeurs** (`fable52`, `opus55`) : à trancher si la règle « aucun identifiant de modèle dans les fichiers » les couvre ; si oui, les remplacer par A, B, C… casserait le renvoi au registre du pilote.
4. **Indépendance des lecteurs** : ce tour est encore du modèle C (déjà lecteur aux tours 1 à 3) ; un lecteur d'un autre modèle pour la v4 reste la garde recommandée par le devis.

## 6. Déclaration d'incident

Aucun incident de ma main. Lu : la v3, le rapport du tour 3, la consigne. Aucune branche interdite, aucun secret, aucun monde, aucune clé, ni `env` ni `printenv` ; aucune machine, dépense, appel externe ni lancement ; aucun fichier existant modifié ; aucun commit ; le seul fichier créé est ce rapport.

Fin : voir `date -u` de l'écriture (2026-11-17T00:28Z environ).
