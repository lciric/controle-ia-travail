# Provenance — papiers « RLCR » — v2

conv-audit, 31 octobre 2026, ≈ 13:17 UTC. **v2 = v1 + Damani et collègues** (v1 gardée, `provenance-rlcr-v1.md`, scellée).

| Fichier | Source | Déposé par | SHA-256 | Note |
|---|---|---|---|---|
| `avalonm1-general-reasoning-2026-10-23-v1.pdf` | `https://www.gr.inc/avalonm1.pdf` | Lazar, 31 octobre 2026, 14:02 heure de Paris | `6429a78fab048d8a58a34fdbefe214156a02de53b6b571053c4df934f485fc58` | voir v1 (empreinte identique à la version lue le 24 octobre ; p. 1, 8, 35, 41 vérifiées) |
| `2507.16806v2-damani-beyond-binary-rewards.pdf` | arXiv 2507.16806v2 (15 mai 2026) | Lazar, 31 octobre 2026, 14:05 heure de Paris, pièce jointe `41db57bb-2507.16806v2.pdf` | `f393de47234962cad0c7ebccb8d0ab17b4236fbc927b4e3e93330c2b0d46ab6d` | Damani, Puri, Slocum, Shenfeld, Kim, Andreas (MIT), « Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty », ICLR 2026, 39 pages (page de titre vérifiée). |

**Deux méthodes sous un même sigle.** « RLCR » désigne ici deux choses distinctes : chez Damani et collègues, *Reinforcement Learning with Calibration Rewards* (p. 1) ; chez General Reasoning, *Reinforcement Learning from Collective Rewards* (titre d'Avalon-M1). Les réponses de Gemini d'octobre (`brouillons/canal-reprise-releve-v1/envois/gemini-theoreme-reponses-v1/`) les combinaient en un seul « théorème RLCR ».

**Vérifié sur le PDF de Damani par conv-audit** (`pdftotext -layout`) : récompense R_RLCR = justesse − (confiance − justesse)² (p. 2, figure ; Eq. 8, p. 4) ; théorème 1 (p. 4) : incitation à la calibration (espérance maximale en q = p_y) et à la justesse ; le terme de Brier ne peut pas être remplacé par n'importe quelle règle propre (la perte logarithmique n'incite pas à la justesse), mais une version existe pour toute règle propre bornée vérifiant une condition (p. 4). **Aucun terme ne couple la confiance déclarée à un ancrage** : l'hypothèse « couplage à une référence » du « théorème d'impossibilité » de Gemini n'est pas satisfaite par cette récompense (constat cohérent avec le n° 22 du 24 octobre pour Avalon).
