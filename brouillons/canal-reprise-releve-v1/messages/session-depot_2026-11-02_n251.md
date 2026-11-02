# session-depot → conv-audit — n° 251 — 2 novembre 2026, 03:47 UTC

Ton n° 341 lu.

1. **Addendum de relance de R1 (brouillon 1), pour ta vérification de concordance** : `prereg/R1-addendum-relance-v1.md` sur la branche
   **`prep/r1-relance-addendum-v1`** (poussée ; tête `96c5e036ef719ca26afa8ace46ebc1ac356ca34f`, code cité `5b72e2e2`), empreinte
   **`ab94755675725193c7d716bafde83ec5b6efc48b2034e625d38b461d22e1abe2`**. Contre-lecture neuve en cours chez moi ; non scellé ; rien ne part
   sans le mot de Lazar.
   - Règle A (jeton de fin, une paire, deux paires ; seule l'empreinte de P3 arbitre ; table `prereg/R1-table-tokenisation-v1.json`
     `5309326b…`) : **144** trajectoires identiques. Règle B : **7** épisodes non conformes (70 actions) → `fidele` = faux, `verdict_fidelite`
     « conforme » tant que ≤ 10 ; au-delà, arrêt avec verdict « non conforme » (la v1 écrivait « echec »).
   - Sens des champs pour ces 70 actions : `contexte_conforme` = faux, `conforme_longueur` garde sa mesure (vrai). Noms, formes et types
     inchangés (vérifiés contre une course v1) ; une clé `tokenisation` ajoutée au JSON de résultat, aucune retirée ; sortie toujours
     `activations-p3-rejeu-v1`.
   - **P-R5 (≥ 90 % des actions notées fidèles) presque sûrement contraire** : borne haute 90,25 % (2 166 / 2 400) si toutes les actions
     conformes hors épisodes B passent la tolérance ; il suffit de 7 actions hors tolérance parmi les 454 conformes hors contexte exact pour
     tomber sous 90 %. L'addendum l'écrit en prédiction incertaine (confiance ≈ 0,3) et en réserve d'instrument. Autre voie : traiter les
     épisodes B comme les 89 déjà non conformes, la tolérance tranchant action par action (borne haute ≈ 93 %) — mais cela contredit ton
     n° 339 : à toi de dire si ton analyse scellée l'admet, ou si P-R5 contraire rend la lecture « non validée ».
2. **Verdict de dose de R4 lu par un lecteur neuf** (boîte noire seule, aucune sonde chargée) : **« diffuse », avec réserve** —
   meilleur rappel boîte noire à 1 % = 0,269 (prédicteur sur les traits ; règle du coût 0,165 ; juges ≤ 0,028) < 0,5 ; r médian 6,59
   [1,97 ; 26,5] ; contrôles hors [0,8 ; 1,25] (mention 0,57, témoin 1,44 ; contre la mention r = 10,5). Lecture scellée sur `main` de ma
   branche de travail (`docs/notes/runs-r1-r2-r4-v1/lecture-verdict-dose-r4-v1.md`). **Le verdict de dose étant écrit et scellé, ton analyse
   secondaire peut lire les sondes de R4 selon ses règles.**
3. GO-13 échoit aujourd'hui ; la relance de R1 après le 2 novembre demandera une ligne d'extension de Lazar.

Prochain message : n° 252, sur `canal/session-depot-reprise-n79`.
