# Contre-lecture du banc de calibration complet MR-2 (règles v2) — tour 2

- **Lecteur** : modèle C, contre-lecteur neuf (R2) ; je n'ai écrit aucune des pièces. Même modèle que le lecteur du tour 1 et, selon la pièce, que le rédacteur des corrections (voir « Points pour la session mère »).
- **Heures** (`date -u`) : début 2026-11-17 03:40:58 ; fin : dernière ligne.
- **Pièces lues** : règles v2 `banc-calibration-mr2-v1/regles-banc-calibration-mr2-v2.md`, `aa1f29dda476dc1492afb20d40714a0753df84c67ead5b126f84860b921d7a2c` (empreinte recalculée, égale au compagnon) ; règles v1 `87d7536e…` (égale à celle que le rapport du tour 1 nomme) ; rapport du tour 1 `55e33514…` (égale à celle de la consigne) ; différentiel scellé du rédacteur (comparé au mien) ; code `outils-v4/monde_riche_v4.py` (`4b165847…`, `course`) et `outils-v1/puissance_monde_riche_v1.py` (`7344b107…`, `_bruiter`, `rng_de`), empreintes égales aux compagnons ; historique git de la v1 (lecture seule). Le devis v4 n'a pas changé (pas de v5).

## Verdict : **corrections** (0 majeure, 7 mineures exigées ; 3 remarques facultatives)

Les quatre corrections du tour 1 qui portaient sur cette pièce sont appliquées fidèlement et rien d'autre n'a changé. Mais la correction 1 n'a atteint que trois endroits sur huit : la pièce se contredit encore sur la place de M3, M5 (a) et M6. Le rédacteur le dit lui-même (observation 2) sans le corriger. Les sept corrections ci-dessous ferment cela et deux écarts neufs créés par la correction 2.

## 1. Les corrections du tour 1 sont-elles appliquées fidèlement ?

- Par `diff` v1 → v2 : changements limités à (a) titre, statut, ligne « Heures », ligne neuve « Version v2 » ; (b) huit couples ; (c) section « Contre-lecture » ajoutée en fin. Aucune autre ligne ne bouge (le différentiel du rédacteur, comparé au mien, dit la même chose).
- Les huit couples du rapport (corrections 1 à 4 de la pièce des règles) : chaque « ancien » figurait une fois dans la v1 (comptage exact), figure zéro fois dans la v2 ; chaque « nouveau » figure une fois dans la v2, **à la lettre** (vérifié par programme). Fidèle.
- Corrections 5 et 6 (devis) : non appliquées ici, dit par la pièce ; **le devis v4 porte encore la fourchette fausse « 0,17 à 0,89 » (lignes 24, 152, 156)** et le texte « aucun commit » sans l'incident ; il faut un devis v5 avant d'inscrire la ligne « calcul ». La section 12, point 4 de la pièce renvoie au « devis v4 » : à mettre à jour avec le devis v5.
- Mes vérifications du tour 1 refaites là où les corrections pouvaient les déranger : ordre D-2 (sections 0, 4.3, 7, 10, 11, 13) inchangé ; la règle reste lue en dernier ; dénominateur « 24 mondes tirés » inchangé ; prédictions inchangées (1 − (1 − 0,5⁸)²⁴ = 0,0897, etc.) ; mineures m8, m9, m10 : dans le devis, non touché ; **aucun identifiant de modèle** dans la v2 (recherche des noms de modèles et de fournisseurs : aucune occurrence) ; aucune mention de 7a, 7b, T0.6, T0.7, B bis, P3-bis, bras d'attaque ; incident de provenance maintenant déclaré, les quatre commits `2687202c`, `48497ef3`, `c70b2261`, `a0993b93` existent et seul le dernier rend `87d7536e…` (recalculé : exact).
- Observation 1 du rédacteur (motif de la correction 2 inexact sur un point) : **vérifiée sur le code et exacte**. `_bruiter` tire autant de bruits quelle que soit la taille de S, et le nombre total d'uniformes par carte est constant (une par effet du monde) ; le vrai découplage de la v4 est que le flux porte le drapeau de masquage et que les uniformes vont d'abord aux connus triés, puis aux inconnus. Le texte neuf règle les deux.

## 2. Ce que les corrections ont dérangé (corrections exigées)

Couples « ancien → nouveau ». Chaque « ancien » figure exactement une fois dans la v2 (comptage par programme).

**Correction 7 (mineure) — section 0, point 1 : « ensuite seulement, des mesures qui ne décident rien » contredit l'exception de M3, M5 (a), M6** :
- Ancien : `dernier** ; ensuite seulement, des mesures qui ne décident rien.`
  Nouveau : `dernier** ; ensuite seulement, des mesures qui ne décident rien (sauf trois relevés pris avant elle, M3, M5 (a) et M6, section 8).`

**Correction 8 (mineure) — section 0, point 7 : C7 dit « sans effet sur aucune valeur » alors que son égalité à six décimales refuse un tirage** :
- Ancien : `effet sur aucune valeur.`
  Nouveau : `effet sur aucune valeur des étapes 1 à 6, hormis le refus d'un tirage par C7 (M3, section 8).`

**Correction 9 (mineure) — titre de la section 8** :
- Ancien : `(jouées après l'étape 6 ; rapportées ; ne décident rien)`
  Nouveau : `(jouées après l'étape 6, sauf M3, M5 (a) et M6 relevées pendant le tirage et les étapes 3, 5 et 6 ; rapportées ; ne décident rien)`

**Correction 10 (mineure) — section 4.3, pas 8, et essai T-14** :
- Ancien : `8. Mesures hors D-2 (section 8).`
  Nouveau : `8. Mesures hors D-2 (section 8) ; M3, M5 (a) et M6 ont déjà été relevées aux pas 6 et 7.`
- Ancien : `| T-14 | mesures après la règle |`
  Nouveau : `| T-14 | mesures hors D-2 après la règle (M3 exceptée : étape de tirage) |`

**Correction 11 (mineure) — « S0 » n'est pas défini dans la pièce** (nom du devis v4) :
- Ancien : `étape de tirage S0`
  Nouveau : `étape de tirage (pas 6 de la section 4.3, « S0 » du devis v4)`
- Ancien : `tirages de S0)`
  Nouveau : `tirages du pas 6)`

**Correction 12 (mineure) — E-1 dit « module neuf égal à la v4 », or la correction 2 écrit que le flux `proposition` en diffère** (et le flux ne porte plus le drapeau de masquage, section 4.2). L'écart doit être déclaré à la mère, pas laissé dans une phrase de la table des flux :
- Ancien : `| module neuf égal à la v4 (section 2) |`
  Nouveau : `| module neuf égal à la v4 (section 2), sauf les flux des générations simulées (section 4.2 : sous-suite par carte, drapeau de masquage hors des clés), écart voulu |`

**Correction 13 (mineure) — l'essai R5-7 exige l'égalité du champ `resultat` d'une génération simulée avec le port de `course`, ce qui est impossible aux flux de la section 4.2** (flux différents, donc cartes différentes). Dire comment l'égalité se joue :
- Ancien : `du champ `resultat` d'une génération simulée par le port de `course`)`
  Nouveau : `du champ `resultat` d'une génération simulée par le port de `course`, la référence recevant les cartes et les flux de jugement du banc, non ses propres flux ; ou, à défaut, égalité sur les contrôles seuls, écart écrit)`

**Correction 14 (mineure) — « la pièce est refaite (v2) » est devenu ambigu** (observation 5 du rédacteur ; la v2 existe) :
- Ancien : `la pièce est refaite (v2).`
  Nouveau : `la pièce est refaite (version suivante).`

## 3. Remarques facultatives

1. Ajouter à T-14 un second cas : exception de C7 dans le tirage → « banc non jugeable » (garde B-6 neuve). Aujourd'hui seul M1 y est essayé.
2. Les remarques 1 à 7 du tour 1 restent facultatives et non portées ; je ne les exige pas, y compris « τ non mesurable » dans la table de lecture.
3. La première ligne de la table de lecture (section 10) gagnerait à nommer « exception de C7 au tirage » ; elle y tombe déjà par « nombre de mondes tirés ≠ 24 ».

## 4. Vérification (2) à (4)

- **Devis** : inchangé depuis le tour 1 ; arithmétique refaite au tour 1 et confirmée (2 580,2 s ; 17,20 h ; pires 2,97 ; 2,99 ; 2,988 USD), crédits 0, hors crédits attendu 0,31, pire sous 3 USD par construction. Reste la fourchette à corriger (0,17 à 0,54) dans un devis v5.
- **Mineures du tour 3** : dans le devis, non touché ici ; reprises au tour 1.
- **Lectures interdites** : aucune ; les deux pièces ne citent rien d'interdit.

## 5. Points pour la session mère

- **Même lignée** : le lecteur du tour 1, le rédacteur des corrections (selon sa déclaration) et moi sommes du modèle C ; la pièce de tour 1 demandait pour le tour 2 « de préférence un autre modèle ». La contre-lecture n'est pas d'une autre lignée que les corrections.
- **Devis v5 nécessaire** (corrections 5 et 6 du tour 1) avant la ligne « calcul ».
- **Écart à confirmer** : flux des générations simulées différent de la v4 (corrections 12 et 13) ; il touche E-1 et l'essai R5-7.
- **Nœud de Lazar sans défaut** : sous-choix de τ ; confirmation de Q-4, de Q-6, de l'étendue de Q-5 et de Q-8 ; E-2, E-10, E-11. Inchangés.
- **Risque** : code non écrit, échéance du 30 novembre.

## Déclaration

Rien modifié, rien committé, aucune machine, aucun appel à un loueur ou à un fournisseur de modèles, aucune dépense ; aucune branche du pilote ouverte ; aucun secret ni monde ; rien sous `diag/`, `runs/`, `donnees/`. Incident de ma main : aucun.

Fin de la rédaction : voir la ligne suivante.
Fin de la rédaction : 2026-11-17 03:42:32 (`date -u`, relevée juste avant le scellement).
