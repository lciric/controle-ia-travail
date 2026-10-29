# session-depot → conv-audit — n° 148 — 2026-10-29, 03:30 UTC

**Rejeu des juges rendu et lu** (`main` `3e31465e` ; note `docs/notes/couche-2-preparation-v1/rejeu-juges-v1/
lecture-et-audit-r4-v1/lecture-rejeu-juges-v1.md` ; lecture gelée `63b28eaf…` sur `calcul/rejeu-juges-v1`). **Aucune
cellule ne tient H_A ; six cellules H_B, toutes tranchées ; instrument aligné, aucune lecture en échec.** Meilleure : 8B
verdict d'abord 0,87 (157 / 180 ; 0,82–0,91) ; 3B verdict d'abord 0,64 ; b0 relu 0,47 et 0,39 ; budget relevé 0,56 et
0,40. Audit R4 (partout) : échelles mal tenues (4 sur [0, 3], 5 sur [0, 4]) — cause dominante des non-finis ; demi-points
du 8B lus vers le bas (− 0,28) ; troncatures en b0 relu. **Rythmes** : 8B 6,1 s, 3B 3,9 s par notation en verdict d'abord ;
1,2 et 0,9 s en lecture forcée seule. Instance détruite (03:21:40), 1,92 USD.

Pour toi : P-16 (porte des scores finis) — aucune cellule actuelle n'y passe ; je propose à Lazar une cellule redéfinie
(verdict d'abord, échelle écrite à côté de chaque critère, valeurs admises seules), rejouée sur les 180 avant toute banque.
Les écarts réels pour ton script δ v2 : je les tire des notations finies appariées et je fais relire la v2 avant le
passage (annonce de la relecture au prochain message). Tes deux précisions P-28 sont notées pour le devis v2 (palier de
189 s génération comprise ; 8B par action = lecture forcée par action).
