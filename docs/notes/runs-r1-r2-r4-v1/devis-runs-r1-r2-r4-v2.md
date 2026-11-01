# Devis — runs de nuit R1, R2 et R4 (GO-2026-11-01-13, plafond 25 USD) — v2

Remplace `devis-runs-r1-r2-r4-v1.md` (gardé, R12) après la contre-lecture 1 : juge 8B ajouté à R4 (CLR-01), suite ciblée
élargie à 17 fichiers de tests (CLR-08), contrôle négatif de R1 (CLR-04), R2 séparable de R1 (CLR-02), hypothèses de coût
écrites (CLR-19). Carte : une A100 80 Go par instance, filtre de P3 plus `dph_total<=1.40`. Sources des durées : P3
(`diag/20261019-230011-p3-reel/episodes-p3.json`, génération 9 092 s pour 240 épisodes, passe unique de 1 036 619 jetons
en 108 s) ; rejeu des juges v2 (`traces/rejeu-juges-v2-20261029-105436-4Zwl/journal.txt` : juge 8B 930 s, juge 3B 655 s
par variante sur 23 lots) ; suite ciblée mesurée ici (`TESTS_A_INSCRIRE`, voir LISEZMOI v2).

| Poste | A : R1 seul | A : R1 puis R2 | B : R4 |
|---|---|---|---|
| Mise en place (image, clonage, installation ; poids 8B 16 Go, 3B 6,4 Go si R2) | 15 min | 20 min | 15 min |
| Tests (suite ciblée de 17 fichiers) | 15 à 20 min | 15 à 20 min | 15 à 20 min |
| R1 : reconstruction, fidélité, contrôle négatif (20 passes), 240 passes, agrégats | 10 min | 10 min | — |
| R2 : juge 3B, 2 bras × 2 400 actions | — | 5 à 10 min | — |
| R2 : juge 8B, 2 bras × 2 400 actions | — | 10 à 15 min | — |
| R4 : extraction et sondes génériques (P3 : 1 534 s) ; 128 épisodes (P3 : 37,9 s chacun) | — | — | 25 + 80 min |
| R4 : juges 3B et 8B (2 bras × 1 280 actions), rejeu (1 280 actions) | — | — | 20 min |
| Poussées, marges | 5 min | 5 min | 5 min |
| **Durée attendue** | **≈ 50 min** | **≈ 1 h 20** | **≈ 2 h 45** |
| **Coût attendu** (1,45 USD/h : carte au plafond, stockage et réseau compris) | **≈ 1,2 USD** | **≈ 1,9 USD** | **≈ 4,0 USD** |
| Plafond de durée de l'amorce | 150 min | 150 min | 330 min |
| Pire cas (plafond × 1,45 USD/h) | 3,6 USD | 3,6 USD | 8,0 USD |
| **Pire cas × 1,5** | **5,4 USD** | **5,4 USD** | **12,0 USD** |

**Total attendu ≈ 5,9 USD (R1 puis R2, et R4) ; pire cas × 1,5 ≈ 17,4 USD**, sous le plafond de 25 USD. Une relance de
l'instance A pour R2 seul, après la confirmation de Lazar sur N-029, coûterait de plus ≈ 1 USD attendu, 5,4 USD au pire ×
1,5 (total au pire 22,8 USD, encore sous 25).

**Hypothèses de coût, écrites (CLR-19)** : (1) la facturation de Vast.ai s'arrête quand l'instance est **détruite** par
son identifiant ; la sortie du conteneur seule n'est pas supposée l'arrêter (une instance arrêtée facture encore le
stockage) : la session détruit l'instance dès la ligne « fin » du journal ; (2) la session (ou son filet horaire)
surveille l'instance B jusqu'à sa fin, attendue vers 01:00 UTC si le départ a lieu vers 22:15 UTC ; si personne ne peut
surveiller jusque-là, le pire cas ci-dessus (plafond de l'amorce, 330 min) s'applique et reste sous le GO.

Repli si le contrôle de fidélité ou le contrôle négatif de R1 échoue : relance de l'environnement (≈ 3 h, ≈ 4,5 USD
attendus ; préenregistrement et devis neufs ; non couverte ici).
