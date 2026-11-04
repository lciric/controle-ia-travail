# Devis de calcul de la relance v4 de R1 — v1

- Auteur : concepteur-développeur neuf de la relance v4 (sous-agent, Opus 5.5). Date : 2026-11-04 (heure par `date -u`
  dans le rapport de rédaction). Texte non scellé (aucun `.sha256`, consigne).
- GO : **GO-2026-11-03-03**, calcul, **plafond 60 USD**, échéance 2026-11-17 (`registres/go.md` de la branche
  `canal/conv-audit-n04`, dernière ligne qui le porte ; même ligne sur `main` selon l'avenant du 4 novembre). Devis
  cité par le GO : 5 à 12 USD.
- Légende : « calcul » = obtenu par un calcul sur une donnée citée ; « supposé » = estimation de l'auteur.

## 1. Données d'entrée

| donnée | valeur | source |
|---|---|---|
| rythme de génération de P3 | 89,6 ms par passe de décodage d'un lot de 8 (9 091,6 s pour 101 451 passes) | diagnostic `rapport-diagnostic-r1-v4-v1.md` (`1c2dd25f…`), § 5 (S§2 de sa sortie `f3e0f42d…`) |
| passes des lots témoins | lot 2 : 2 936 ; lot 13 : 3 392 | diagnostic, § 4.3 |
| passes des 28 lots à cible | 95 403 | diagnostic, § 6.4 |
| passe forcée seule sur les 89 (repli) | central ≈ 5,4 h, de ≈ 1,2 à ≈ 17 h (supposé par le diagnostic) | diagnostic, § 6.4 |
| prix horaire | **1,40 USD/h** (plafond du filtre d'offre de la v3) ; relevés 1,19 à 1,40 | addendum v3 (`88e262e2…`), « Coût et GO » ; rapport Fable (`371fe443…`), § 8 |
| mise en place d'une instance (clonage, installation, préchargement du modèle, 358 essais) | ≈ 35 à 50 min (supposé : v3 ≈ 20 min de mise en place et ≈ 20 min d'essais pour 329 essais ; 25 essais de plus, dont deux bouts en bout jouets de ≈ 1 à 3 min) | addendum v3, « Coût et GO » |
| rejeu des activations (passe unique, 240 épisodes, contrôles) | ≈ 5 à 10 min (supposé ; v3 : 257,5 s de rejeu) | rapport Fable, § 8 |

## 2. Passes et durées

| poste | passes | durée de carte | nature |
|---|---|---|---|
| Session 1 — témoin, lots 2 et 13 | 6 328 | 6 328 × 89,6 ms ≈ **9,4 min** ; plus la mesure des 8 lignes sur processeur par pas (≈ 10 à 25 % de plus, supposé) | calcul (passes), supposé (surcoût) |
| Session 2 — lot fidèle à plusieurs cibles, 28 lots | 95 403 | ≈ **2,37 h** ; plus le choix contraint et les tirages exponentiels des cibles, calculés action par action sur processeur (≈ 10 à 30 min, supposé) | calcul (passes), supposé (surcoût) |
| Session 2 — repli par épisode (lot fidèle à une cible, puis passe forcée, frontière de 272) | — | 0 si le lot est exact au bit (scénario attendu, diagnostic § 6.3 : ≈ 0,75) ; ≈ 0,5 à 1 h si quelques cibles (supposé) | supposé |
| Session 2 — voie « passe forcée » (témoin non exact) | — | central ≈ 5,4 h ; de ≈ 1,2 à ≈ 17 h | supposé (diagnostic) |
| Session 2 — table v4 (processeur) | 0 | ≈ 1 à 2 min | supposé |
| Session 2 — rejeu v4 | 240 passes uniques | ≈ 5 à 10 min | supposé |

## 3. Dépense par scénario (au prix plafond de 1,40 USD/h, disque compris pour mémoire : < 0,1 USD)

| scénario | session 1 | session 2 | total |
|---|---|---|---|
| **central** : témoin exact, 89 retrouvés par le lot, aucun repli coûteux | ≈ 1,0 à 1,1 h → **≈ 1,4 à 1,5 USD** | mise en place 0,75 h + lot 2,4 à 2,9 h + table et rejeu 0,2 h + poussées → ≈ 3,6 à 4,6 h → **≈ 5,0 à 6,4 USD** | **≈ 6,5 à 8 USD** |
| témoin exact, quelques replis | ≈ 1,5 USD | ≈ 4,5 à 5,5 h → ≈ 6,3 à 7,7 USD | ≈ 8 à 9 USD |
| témoin **non exact** : passe forcée seule | ≈ 1,5 USD | 0,75 h + 1,2 à 17 h + 0,5 h → ≈ 2,5 à 18,3 h → **≈ 3,4 à 25,6 USD** (central ≈ 6,7 h → ≈ 9,3 USD) | **≈ 5 à 27 USD** (central ≈ 11 USD) |
| **pire cas borné par les gardes** | plafond de l'amorce 180 min + 5 min d'arrêt forcé + 30 min de vie hors amorce → 215 min → **≈ 5,0 USD** | plafond de l'amorce 2 200 min + 5 + 30 → 2 235 min → **≈ 52,2 USD** | **≈ 57,2 USD < 60 USD** |

Calculs : 215 / 60 × 1,40 = 5,02 ; 2 235 / 60 × 1,40 = 52,15 ; 5,02 + 52,15 = 57,17 (calcul). Les plafonds d'amorce
(180 et 2 200 min) et le délai externe par étape (`DELAI_ETAPE_MIN` 120 min en session 1, 2 100 min en session 2) sont
des **gardes contre une boucle folle**, choisies pour que leur somme reste sous le plafond du GO : 2 200 min (36,7 h)
dépassent de plus de deux fois le haut du scénario « passe forcée » (≈ 18,3 h), ils ne coupent aucune mesure attendue.
Les budgets internes du module (`duree_max_episode_lot_s` 14 400 s, `duree_max_lot_s` 259 200 s ; C2 du complément)
sont plus larges encore : le délai externe les précède (déclaré).

**Gardes de dépense** (leçon de l'audit A9 d'A1-v3, § 8 : l'instance survit, la session de pilotage non) : deux tâches
planifiées posées à la création de chaque instance, indépendantes de la session : alerte à **45 USD engagés** sous le
GO (les deux sessions cumulées), arrêt à **57 USD engagés** (TERM au processus de l'étape par son PID, poussée, puis
destruction de l'instance par son identifiant, R10), pour que la poussée et l'arrêt tiennent sous 60 USD.

## 4. Lecture

- Attendu ≈ 6,5 à 8 USD (central), ≈ 11 USD si le témoin est non exact ; pire cas borné ≈ 57 USD : sous le plafond de
  60 USD de GO-2026-11-03-03, dans la fourchette de 5 à 12 USD qu'il cite pour le cas central.
- Dépenses déjà imputées à GO-2026-11-03-03 : à relever dans `registres/depenses.md` avant chaque création (aucune
  connue de l'auteur, qui ne lit pas ce registre).
- Le GO-2026-11-02-30 (complément, 40 USD) n'est pas utilisé.
- Sans offre conforme (A100-SXM4-80GB, CUDA ≥ 13.0, centre de données, fiabilité ≥ 0,98, ≤ 1,40 USD/h) : rien n'est
  loué, nœud porté à Lazar.
