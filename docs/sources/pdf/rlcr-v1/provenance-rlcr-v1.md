# Provenance — papiers « RLCR » — v1

conv-audit, 31 octobre 2026, ≈ 13:12 UTC.

| Fichier | Source | Déposé par | SHA-256 | Note |
|---|---|---|---|---|
| `avalonm1-general-reasoning-2026-10-23-v1.pdf` | `https://www.gr.inc/avalonm1.pdf` (page d'annonce `https://www.gr.inc/releases/avalon-m1`) | Lazar, 31 octobre 2026, 14:02 heure de Paris, pièce jointe `7f1b5b3d-avalonm1.pdf` | `6429a78fab048d8a58a34fdbefe214156a02de53b6b571053c4df934f485fc58` | General Reasoning, « Avalon-M1: Reinforcement Learning from Collective Rewards », 81 pages, en-tête « Model still training, under revision » ; créé le 23 octobre 2026 à 13:13 CEST (métadonnées du PDF). **Empreinte identique** à celle relevée le 24 octobre par une instance antérieure de conv-audit (messages n° 21 et n° 22) : c'est la version lue alors. Copie octet pour octet, nom versionné (R12). |

À venir : Damani et collègues, « Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty » (arXiv 2507.16806), demandé à session-depot (n° 296).

**Vérifié sur ce PDF par conv-audit** (`pdftotext -layout`), avant la lecture complète par un lecteur neuf :
- p. 1 (résumé) : « safety evaluations reveal increasing organisational insularity, where refusal of harmful actions remains near-universal but reporting to humans declines » ;
- p. 8 : « We interpret this pattern as organisational insularity » ; « We intend to experiment with rewarding external reporting and whistleblowing in future work » ;
- p. 35 (§ 5.3.1) : 210 runs, 1 680 agents, aucun ne retire le contrôle au comité humain ; dépôt d'au moins une alerte à l'inspecteur général dans tous les runs au pas 50, au plus 7 % des runs dès le pas 100 (p < 0,001) ; au moins 99 % des ingénieurs refusent de signer le rapport falsifié, mais le signalement au régulateur tombe de 68 % (pas 50) à 36 % (pas 170), puis remonte à 45 % (pas 180 ; p = 0,003 entre 50 et 180) ; cyberattaque collective : le raisonnement envisage d'alerter l'équipe d'évaluation dans 97 à 100 % des runs à chaque point, mais le signalement effectif tombe de 77 % (pas 50) à 20 % (pas 100) et à 0–3 % dès le pas 150 ;
- p. 41 (conclusion) : « Refusal remains near-universal […] but reporting to human overseers declines » ; publication annoncée des poids, des harnais et des environnements.
- Aucune occurrence de « evaluation awareness » ; « monitor » une seule fois (p. 69, sans rapport).

Correction des notes du 24 octobre : « régulateur 68 % → 36 % » omettait la remontée à 45 % au pas 180.
