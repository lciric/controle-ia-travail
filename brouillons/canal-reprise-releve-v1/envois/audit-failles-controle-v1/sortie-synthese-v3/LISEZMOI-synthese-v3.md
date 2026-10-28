# LISEZMOI — synthèse de l'audit des failles de notre contrôle — v3 (ciblée)

Lignée conv-audit, sous-agent de synthèse. **Pièce confidentielle** : dépôt privé seulement ; jamais dans la copie
publique ; jamais servie à un organisme. Horodatage : dernière ligne (heure lue sur `date -u` dans la commande qui l'écrit).

## Pièces

| pièce | rôle |
|---|---|
| `audit-failles-controle-v3.md` | synthèse v3 : la v2 avec les seuls changements de la contre-lecture v2 |
| `LISEZMOI-synthese-v3.md` | ce fichier |
| `calculs-synthese-v4.py` (`2fcbf997…`), sortie (`76a4b4b6…`) | normalisations par la durée avec τ estimé sur le calibrage ; multiplicité entre sondes |
| v2 inchangée : `audit-failles-controle-v2.md` (`890130e8…`), `LISEZMOI-synthese-v2.md` (`c8f25c5b…`) ; calculs v2 et v3 | gardées (R12) |

Source des constats : `fournis-complement/contre-lecture-v2/rapport-contre-lecture-synthese-v2.md` (`652a79cc…`), avec
`calculs-contre-lecture-v2.py` et sa sortie (compagnons conformes). Ce script a été **rejoué** (`python3 -I`) : sortie
identique octet pour octet. La consigne de prudence R-519 a été appliquée : aucune stratégie d'attaque conçue, détaillée
ni améliorée ; aucun arrêt par filtre.

## Table « constat → traitement »

| constat | traitement dans la v3 | où |
|---|---|---|
| CLS2-01 « non falsifiable » | « aucune n'est spécifiée au point d'être décisive » : HR1, HR2, HR5 sous-spécifiées ; HR4 sans seuil ; HR3 a un seuil qui peut échouer, au signe acquis ; recommandation de D-19 gardée | 0.1 point 9 ; 0.2 ; D-01 ; D-19 |
| CLS2-02 E | le retour à la classe C vaut pour le terme nouveau de V_T, pas pour V_T entier (second terme sensible à l'ordre : 77,4 % contre 82,4 % entre motif et rebrassage, bloc E2 rejoué) ; V_T n'est pas une parade à la remise à zéro ; aucune comparaison de puissance n'est faite ; « affaiblirait » retiré pour E, gardé pour G | 0.1 point 12 ; 0.2 ; RC-3.1 ; 2 ; 3.6 ; D-01 ; D-19 |
| CLS2-03 F | HT-02 : « la normalisation du rapport (sans terme d'épisode) ne rend pas … » ; option (d) ajoutée à D-18 ; calcul v4 indépendant, τ **estimé** sur le calibrage : 0,72 à 1,45 % pour 1 % visé jusqu'à 60 pas sous effet épisode, 2,09 % sous indépendance ; forme combinée avec celle du rapport : 0,73 à 1,71 % sur cinq nuls ; recommandation (a) inchangée | HT-02 ; D-18 ; RC-3.2 ; 0.2 |
| CLS2-04 D-19 | « attaque les parades de la génération 1, pour l'essentiel celles du programme » (seuil conforme, somme cumulée de Page, plancher apparié, lecture P3b, loi de déférence) | D-19 ; 2 |
| CLS2-05 Panin | `27f88ed7…` (vérifié sur disque et dans la note de provenance) ; `66787c14…` était l'empreinte de la note elle-même, prise par erreur | HT-09 ; annexe B |
| CLS2-06 χ₂ | différence mixte du second ordre de Δv, en s et en v₀ ; « pas un tenseur » gardé | RC-3.5 |
| CLS2-07 prudence | (1) RC-3.1 (e) réécrit comme propriété du détecteur ; (2) HT-01 : énoncé au niveau du détecteur, famille de simulation ramenée au seul motif de HR1, autres paramètres laissés au préenregistrement | RC-3.1 ; HT-01 |
| CLS2-08 HT-09 | « par épisodes indépendants ; à corriger de l'effet de grappe par tâche » (N-025, remarque 3) | HT-09 |
| CLS2-09 rapprochements décoratifs | HT-08 (Currie), HT-22 (Lincoln et Petersen), HT-30 (Shapley) marqués « décoratif », gardés pour la trace | HT-08, HT-22, HT-30 |
| CLS2-10 HT-25 | variante récompensée par un juge J : « bras d'attaque déclaré » (invariant de N-053, point 5), sous GO | HT-25 |
| CLS2-11 quatre PDF | note de provenance (adresse, date) à compléter avant tout usage dans un papier | annexe B |
| CLS2-12 « ne vaut que sous indépendance » | « tombe sous effet épisode » | 0.1 point 12 ; 0.2 |
| Manque 1 : multiplicité entre sondes au plancher | 1 − 0,95ᵏ : 9,75 %, 14,26 %, 22,62 % pour 2, 3, 5 sondes (calcul v4) ; correction exigée dans D-07 (a) | D-07 ; 7.2 |
| Manque 2 : normalisation à variance d'épisode | voir CLS2-03 | D-18 (d) ; 7.2 |
| Manque 3 : forme du champ du coût avant le chiffre | confusion de W_pré (N-025, remarque 1, vérifié : 41, 14, 13 contre 3, 0, 0) ; HT-04 apparie aussi sur la forme | RC-3.4 ; HT-04 ; 7.2 |

Corrections que je ne suis pas : aucune.

## Écarts déclarés

1. Les changements touchent 98 lignes ajoutées et 59 retirées du fichier (phrases corrigées réécrites en place), un
   peu plus d'une page brute ; aucun ajout hors des constats.
2. Pour CLS2-03, j'ai refait le calcul avec τ **estimé** sur les épisodes honnêtes du calibrage (la contre-lecture prenait
   τ vrai) et ajouté une forme combinée ; les deux restent des nuls simplifiés.
3. Les changements de la v3 n'ont pas été contre-lus.

---
Horodatage : version close le 2026-10-26 à 14:25:14 UTC (heure lue sur date -u dans la commande qui écrit cette ligne).
