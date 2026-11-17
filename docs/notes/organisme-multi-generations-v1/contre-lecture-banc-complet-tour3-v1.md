# Contre-lecture du banc complet, tour 3 (règles v3 et devis v4)

Lecteur : modèle C, contre-lecteur neuf (R2) ; heure de rédaction : 2026-11-17T03:57:19Z. Pièce lue : `banc-calibration-mr2-v1/regles-banc-calibration-mr2-v3.md` (`e3bb8189…`, égale à son compagnon) ; v2 (`aa1f29dd…`) ; rapport du tour 2 (`11086f65…`, empreinte recalculée égale) ; devis v4 (`a64ad406…`) ; rapport du tour 1 ; lignes de GO-2026-11-17-05. Rien d'interdit lu, aucune machine ni fournisseur, aucun fichier modifié, rien committé.

## Verdict : **corrections** (0 majeure, 3 mineures exigées ; 3 remarques facultatives)

## 1. Corrections du tour 2 appliquées fidèlement ?

- `diff` v2 → v3 : 9 lignes touchées dans le corps (10 couples) plus l'en-tête (titre, statut, ligne « Version v2 », ligne « Version v3 ») et la sous-section « Tour 2 » ajoutée en fin de pièce. **Rien d'autre.** Le différentiel scellé de la mère est identique au mien (hors en-têtes de dates).
- Corrections 8 à 14 : textes **identiques à la lettre** à ceux du rapport du tour 2 (comptage des couples : 1+1+1+2+2+1+1+1 = 10).
- Correction 7 : appliquée avec **deux mots de plus** (« avant ou pendant elle »). Écart déclaré et **justifié** (M6 relève les durées des regroupements de l'étape 6, donc pendant la règle ; la section 8 et E-10 le disent). **Acceptée.**
- Pas 6 = tirage (M3, M5 (a)) ; pas 7 = étapes 1 à 6 (M6 aux étapes 3, 5, 6) : exact. Section 8, titre et premier paragraphe, E-10, B-6, T-14, section 0 points 1 et 7 : accordés entre eux.

## 2. Ce que les corrections ont dérangé (corrections exigées)

**Correction 15 (mineure) — la correction 13 laisse une phrase contraire à elle-même à la section 3** : le port de `course` y est dit à « graines de la v4 », alors que la section 2 dit désormais que la référence reçoit les cartes et les flux de jugement du banc (observation 3 de la v3, non portée). Texte exigé, pour que la pièce finale ne se contredise pas :
- Ancien : `Le port de `course` (juge simplifié, regroupement sur 1 500 instances, graines de la v4) n'existe`
  Nouveau : `Le port de `course` (juge simplifié, regroupement sur 1 500 instances, graines de la v4, sauf pour l'égalité de R5-7 : cartes et flux de jugement du banc, section 2) n'existe`

**Correction 16 (mineure) — « égal à la v4 » sans l'exception de E-1, aux deux endroits où la pièce tranche la lecture** (observation 2 de la v3, non portée ; E-1 dit l'exception, la section 0 et la section 2 non) :
- Ancien : `égal à `monde_riche_v4.py`** (lecture de`
  Nouveau : `égal à `monde_riche_v4.py`**, sauf les flux des générations simulées (E-1) (lecture de`
- Ancien : `(b) un **module neuf à noms neufs, égal à la v4** (E-5 et R5-7 de la conception v7).`
  Nouveau : `(b) un **module neuf à noms neufs, égal à la v4, sauf les flux des générations simulées (section 4.2, E-1)** (E-5 et R5-7 de la conception v7).`

**Correction 17 (mineure) — devis v4 : corrections 5 et 6 du tour 1 toujours non appliquées, pas de devis v5** (dossier relu : devis v1 à v4 seulement ; empreinte du v4 inchangée). Le devis annonce « 0,17 à 0,89 USD » alors que sa section 6 exclut le prix de 0,15 USD/h qui donne 0,89 ; au prix relu maximal de chaque choix, 5,96 × 0,09 = 4,17 × 0,13 = 3,27 × 0,166 = 0,54. Lazar lit cette fourchette. Un **devis v5** (fichier neuf) portant les cinq couples « fourchette » et les deux couples « Q-5/Q-8 » et « commit » du rapport du tour 1 (section 5, corrections 5 et 6, chaque « ancien » compté une fois dans le v4, vérifié) est exigé **avant d'inscrire la ligne « calcul »** ; la section 12, point 4 de la pièce des règles (et les autres renvois « devis v4 ») suit le devis v5 dans la version finale.

## 3. Remarques facultatives

1. T-14 : ajouter l'exception de C7 au tirage → « banc non jugeable » (reprise de la remarque 1 du tour 2).
2. Section 10, première ligne de la table : nommer « exception de C7 au tirage » (reprise de la remarque 3 du tour 2).
3. Observation 4 de la v3 (repli de R5-7 : qui constate le défaut, et le repli compte-t-il comme un succès) : à fixer dans la contre-lecture du code ; non exigé ici.

## 4. Vérifications (1) à (4)

- **(1) Règles complètes, ordre D-2, critères avant lecture** : ordre f, fusion, n, forme, τ, règle en dernier ; table de lecture à issues exclusives (mondes tirés ≠ 24 ; 2·G < 24 ; 2·G ≥ 24) ; prédictions, gardes B, essais T, preuves en annexe : présents. Rien de dérangé par les corrections hormis les points 15 et 16.
- **(2) Devis, arithmétique refaite** : par monde 2 580,2 s ; calcul d'un processus 24 × 2 580,2 / 3 600 = 17,20 h ; durées 5,96 h, 4,17 h, 3,27 h ; attendu 0,311 / 0,218 / 0,171 USD à 0,052222 USD/h ; au pire 84,75 h ; durées au pire 28,48 / 19,66 / 15,24 h ; minuteries 33 / 23 / 18 h ; plafonds 2,97 / 2,99 / 2,988 USD : **tous exacts**. Crédits 0 et hors crédits séparés ; **3 USD tenu par construction**, aucun nœud de dépense ; seule la fourchette est fausse (correction 17). Le mot de Lazar (GO-2026-11-17-05) exige un devis « refait et contre-lu » : le devis v5 est cette pièce. Montants recalculés pour le mot « 0,30 USD environ » : cohérent.
- **(3) Mineures du tour 3 reprises** : m8 (0,0897 ; 0,3340, recalculés par mes soins : exacts) et m9 présentes au devis, une occurrence chacune ; m10 en substance.
- **(4) Interdits** : aucune lecture interdite ; aucun identifiant de modèle dans la pièce (recherche faite) ; lettres A, B, C seulement.

## 5. Points pour la session mère

- **Même lignée** : je suis du modèle C, comme les lecteurs des tours 1 et 2 et (selon sa déclaration) le rédacteur des corrections ; la pièce demandait une autre lignée pour le tour 3 ; non satisfait. Pour le devis, la lecture d'une autre lignée que A reste celle de C.
- Devis v5 nécessaire (correction 17) avant la ligne « calcul ».
- Écart à confirmer par la mère : flux des générations simulées différents de la v4 (E-1, R5-7, section 3).
- Nœuds de Lazar sans défaut (sous-choix de τ ; Q-4, Q-6, étendue de Q-5 et de Q-8) et points de la mère (E-1, E-2, E-10, E-11) : inchangés ; le code de la course et du banc n'existe pas, échéance du 30 novembre : risque principal.
- À dire à Lazar : la règle tient presque par construction à P_CACHÉE = 0 ; elle ne garde pas contre des proposeurs qui ne masquent pas.

## Déclaration

Aucun incident de ma main. Fichiers écrits : ce rapport seul (et un fichier de comparaison au bloc-notes, hors dépôt).
