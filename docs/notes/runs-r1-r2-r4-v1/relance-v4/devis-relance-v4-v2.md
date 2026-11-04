# Devis de calcul de la relance v4 de R1 — v2

- Auteur : développeur neuf des ajouts de la relance v4 (sous-agent, Opus 5.5) ; je n'ai écrit ni le code v4, ni
  l'addendum, ni sa contre-lecture. Date : 2026-11-04 (`date -u`). Texte non scellé (aucun `.sha256`, consigne).
- Version 2 de `devis-relance-v4-v1.md` (`d8d223fa…`, non modifié) : **seuls changent** (a) le scénario « témoin non
  exact », qui suit maintenant l'arbitrage de la mère sur la contre-lecture R2 (M7) : lot, puis repli à une cible, puis
  passe forcée (`resolution_graine_lot_v3`), au lieu de la passe forcée seule ; (b) la garde de dépense, qui détruit
  l'instance **par son identifiant seulement** (écart V4-E12 du brouillon 2 ; la v1 écrivait « TERM au processus de
  l'étape par son PID », voie que le complément scellé `049f20ba…` déclare non établie). Tout le reste (données d'entrée,
  passes, scénarios « central » et « quelques replis », pire cas borné) vaut tel quel (v1, §§ 1 à 3).
- Légende : « calcul » = obtenu par un calcul sur une donnée citée ; « supposé » = estimation de l'auteur.

## 1. Scénario « témoin non exact » (remplace la ligne de la v1)

| poste | durée | nature |
|---|---|---|
| mise en place de la session 2 | ≈ 0,75 h | v1 |
| lot à plusieurs cibles, 28 lots (rejoué quelle que soit la lecture du témoin) | ≈ 2,4 à 2,9 h | v1 (95 403 passes × 89,6 ms, plus le choix contraint) |
| lot à une cible pour chaque cible non retrouvée (lot rejoué jusqu'à la fin de sa cible, ≈ la moitié d'un lot : ≈ 1 700 passes ≈ 2,5 min, plus le repli écrit) | de 0 à ≈ 3,8 h (89 cibles) ; ≈ 2,5 h au milieu (contre-lecture, M7) | supposé |
| passe forcée du cœur pour celles qui restent | de ≈ 1,2 à ≈ 17 h, central ≈ 5,4 h (diagnostic, § 6.4) | supposé (diagnostic) |
| table v4, chaîne, rejeu, poussées | ≈ 0,5 h | v1, plus la chaîne (processeur, ≈ 1 à 2 min, supposé) |

Session 2 : ≈ 4,9 à 24,9 h, central ≈ 11,6 h → **≈ 6,9 à 34,9 USD, central ≈ 16,3 USD** au prix plafond de 1,40 USD/h
(calcul : 0,75 + 2,4 + 0 + 1,2 + 0,5 = 4,85 ; 0,75 + 2,9 + 3,8 + 17 + 0,5 = 24,95 ; 0,75 + 2,65 + 2,5 + 5,4 + 0,5 = 11,8 ;
× 1,40). Avec la session 1 (≈ 1,5 USD) : **≈ 8 à 36 USD, central ≈ 18 USD** (la v1 donnait ≈ 5 à 27, central ≈ 11 USD).
Le haut (≈ 24,9 h) reste sous le plafond d'amorce de la session 2 (2 200 min ≈ 36,7 h) et sous le délai par étape
(2 100 min ≈ 35 h) : aucune garde de durée ne coupe ce scénario ; le **pire cas borné reste ≈ 57,2 USD** (v1, § 3).

## 2. Gardes de dépense (remplace le paragraphe de la v1)

Deux tâches planifiées, posées et éprouvées avant chaque création, armées aussitôt après, indépendantes de la session de
pilotage (protocole du complément scellé, « Liste d'arrêt » : armement, quatre épreuves, lecture aveugle des journaux),
seuils de la v4 : (i) vérification horaire : alerte à **45 USD** engagés ou projetés à la vérification suivante,
**destruction par l'identifiant** à **57 USD** projetés, destruction aussi dès la fin de l'amorce lue au journal ;
(ii) destruction à heure fixe `T0 + H`, `H = (57 USD − dépenses déjà imputées au GO, sessions et reprises comprises −
disque estimé) / prix horaire − 15 min` (session 2 après une session 1 à ≈ 1,5 USD : `H` ≈ (57 − 1,5 − 0,1) / 1,40 h −
15 min ≈ 39,3 h, calcul). Aucun signal par numéro de processus. Conséquence déclarée : une destruction perd ce que le
script n'a pas poussé (il pousse à la fin de chaque étape). Règles et épreuves sur processeur :
`src/controle_ia/runs_nuit/garde_depense_v4_v1.py` et `tests/test_garde_depense_v4_v1.py`.

## 3. Lecture

- Attendu ≈ 6,5 à 8 USD (central, témoin exact) ; ≈ 18 USD au milieu si le témoin est non exact (≈ 36 USD au haut) ;
  pire cas borné ≈ 57 USD : sous le plafond de 60 USD de GO-2026-11-03-03. Le scénario « non exact » dépasse la
  fourchette de 5 à 12 USD que cite le GO (il la dépassait déjà au haut dans la v1) : sous le plafond, sans nœud
  nouveau, mais à dire à Lazar avec la lecture du témoin.
- Dépenses déjà imputées à GO-2026-11-03-03 : à relever dans `registres/depenses.md` avant chaque création.
