# Devis — runs de nuit R1, R2 et R4 (GO-2026-11-01-13, plafond 25 USD) — v1

Carte : une A100 80 Go par instance, prix plafond 1,40 USD/h (offres A100_SXM4 vérifiées, filtre de P3). Deux instances
en parallèle recommandées : **A** = R1 puis R2 (même instance, étapes en série, poussée après chaque étape) ; **B** = R4
(lanceur de P3 tel quel, puis rejeu et juge sur ses actions). Les durées viennent des runs mesurés : P3
(`diag/20261019-230011-p3-reel/episodes-p3.json`, `descriptifs` : 240 épisodes, génération 9 092 s, passe unique de
1 036 619 jetons en 108 s ; tests 908 en 1 725 s, `traces/p3-20261020-020648-jcOO/tests.txt`) et rejeu des juges v2
(`traces/rejeu-juges-v2-20261029-105436-4Zwl/journal.txt` : suite ciblée de 226 tests en 866 s ; 3B et 8B par lots).

| Poste | Instance A (R1 + R2) | Instance B (R4) |
|---|---|---|
| Mise en place (image, clonage, installation, téléchargement des poids : 8B 16 Go ; 3B 6,4 Go) | 15 à 20 min | 15 min |
| Tests (suite ciblée des runs de nuit, même liste sur A et B) | 10 à 15 min | 10 à 15 min |
| R1 : reconstruction (processeur) + passe unique de 240 épisodes (≈ 1,04 M jetons) + agrégats + notation de contrôle | 5 à 10 min | — |
| R2 : juge 3B, 2 bras × 2 400 actions (≈ 5,8 M jetons lus, sans génération) | 5 à 10 min | — |
| R2 : juge 8B, 2 bras × 2 400 actions (bras secondaire) | 10 à 15 min | — |
| R4 : extraction et sondes génériques (P3 : 1 534 s) | — | 25 min |
| R4 : 128 épisodes (P3 : 37,9 s par épisode) | — | 80 min |
| R4 : rejeu (1 280 actions) + juge 3B | — | 10 min |
| Poussées, marges | 5 min | 5 min |
| **Durée attendue** | **≈ 1 h 10** | **≈ 2 h 25** |
| **Coût attendu** (1,40 USD/h au plafond, stockage et réseau ≈ 0,05 USD/h compris) | **≈ 1,7 USD** | **≈ 3,5 USD** |
| Plafond de durée imposé par l'amorce | 150 min | 330 min |
| Pire cas (plafond de l'amorce × 1,45 USD/h) | 3,6 USD | 8,0 USD |
| **Pire cas × 1,5** | **5,4 USD** | **12,0 USD** |

**Total attendu ≈ 5,2 USD ; pire cas × 1,5 ≈ 17,4 USD**, sous le plafond de 25 USD du GO. Le pire cas suppose que la
session n'arrête l'instance qu'au plafond de l'amorce ; la surveillance (LISEZMOI) arrête l'instance par son identifiant
dès la fin du journal (R10). Une relance (branche `…-v2`) après un arrêt précoce reste sous le plafond tant que le cumul
consigné dans `registres/depenses.md` le permet ; sinon, nœud.

Repli si le contrôle de fidélité de R1 est contraire : relance de l'environnement (≈ 3 h, ≈ 4,5 USD attendus, devis neuf
et préenregistrement neuf ; non couverte par ce devis).
