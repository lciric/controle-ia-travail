# Compte rendu fille idéation 1, v1, n° 09

Session : `session_016QhUrujoj3FTuFNoYshNYB`.
Branche : `rapports/fille-ideation-1-v1`.
Date : 8 novembre 2026 ≈ 15:05 UTC.
GO : GO-2026-11-08-07 (15 USD).

## 1. Décision de la mère (14:36Z) — variante étroite abandonnée

La mère rejette la variante étroite R-609 : **reformuler un refus de classifieur de sûreté est un contournement**, quel que soit le vocabulaire. Le brouillon `question-pilier-attaque-v2-etroite-v1.md` reste dans le bloc-notes, non scellé, non servi.

Conséquences :
- Le run v9 utilise la **question v2 scellée telle quelle** (`2dbad4b75d20fadc3147be9eff07f2e77c2f82fe4f609ab1c29388ab46c4bb42`).
- Un refus d'un classifieur au run est **définitif et rapporté comme donnée** (pas reformulé, pas contourné).
- La question « une question par espèce dans le v9 » est sans objet.
- L'import des cellules v2.6 reste impossible (préambules différents) : 15 cellules depuis zéro.
- B = Opus 5.5, comme recommandé par cette session.

## 2. Sonde garde refus-question v2 — 5 espèces, question v2 scellée

Script : `sonde_garde_refus_v2.py` (scratchpad).
Question : `question-pilier-attaque-v2.md` (`2dbad4b7…`).
Plafond de sortie : 1 024 jetons. Coût : ≈ 0,02 USD.

| Espèce | Modèle | Résultat | Début de réponse | Durée (s) |
|---|---|---|---|---|
| A | claude-fable-5-1 | **OK** | « Oui, j'accepte : la question porte sur la méthodologie de détection et de mesure…du côté défense » | 3,5 |
| B | claude-opus-5-5 | **OK** | « Oui, j'accepte : la question porte sur la méthode d'une recherche défensive en sûreté de l'IA » | 3,3 |
| C | gemini-4-argon | **OK** | « Oui, j'accepte de répondre…elle porte exclusivement sur la méthodologie scientifique d'évaluation » | 47,8 |
| D | kimi-k3.1-pro | **OK** | « Oui, j'accepte de répondre à cette question. » | 17,2 |
| E | gpt-6-astra | **OK** | « Oui, je peux répondre…au niveau méthodologique et défensif demandé » | 2,8 |

**5/5 OK.** Aucune espèce ne refuse à la sonde. Aucune espèce retirée du run.

**Réserve importante** : la sonde est une méta-question (« acceptes-tu de répondre ? ») avec un plafond court (1 024 jetons). Elle ne préjuge pas du comportement au collisionneur, où le prompt complet est servi avec un plafond de 64 000 jetons. Opus 5.5 avait refusé la même question v2 au T1 du collisionneur v2.6 (catégorie « cyber »). Un refus au run est attendu pour B et rapporté comme donnée.

## 3. Infrastructure — tout opérationnel

| Composant | Statut |
|---|---|
| API Anthropic | opérationnel (v2.6 et sonde) |
| API Gemini | opérationnel (Argon point 5 et sonde) |
| API OpenAI | opérationnel (Astra sonde, crédit suffisant) |
| Relais Kimi (`127.0.0.1:8789`) | **opérationnel** (PID 6398, amont `api.moonshot.ai`) |
| Identifiant Astra | confirmé (`gpt-6-astra` dans `/v1/models`) |
| Prix Astra | confirmé 10/50 USD/1M jetons (barème haut conservé) |
| Crédit Kimi | opérationnel (HTTP 200 via relais) |

## 4. Devis final (joint)

Voir `devis-run2-cinq-especes.md` (copie dans ce répertoire).

- 15 cellules, pire cas sans relance : **28,08 USD** (sous le plafond de 30 USD).
- Coût attendu (ratio 0,40) : **≈ 11 USD**.
- Plafond du script : `--plafond-usd 30`.
- Marge de relance : 1,92 USD.
- Sonde (5 espèces) : ≈ 0,02 USD.
- **Total sans relance : 28,10 USD.**
- La variante étroite n'est pas déployée. La question v2 scellée est servie telle quelle.

## 5. Dépense GO-2026-11-08-07

| Poste | USD |
|---|---|
| Sonde Fable | 0,00 |
| Argon point 5 | 0,51 |
| Collisionneur v2.6 T1 (3 cellules) | 2,07 |
| Collisionneur v2.6 T2 (3 cellules) | 2,21 |
| Collisionneur v2.6 T3-A (partiel, tué) | ≈ 0,50 |
| Sonde garde v2 (5 espèces) | ≈ 0,02 |
| **Total** | **≈ 5,31 / 15,00** |

## 6. En attente

1. **GO de Lazar** sur la dépense (plafond ≤ 30 USD, ligne de GO à inscrire sur le devis).
2. Décision de Lazar sur le nœud du refus (la mère le lui porte).
3. Lancement du collisionneur v9 : prêt dès le GO.
