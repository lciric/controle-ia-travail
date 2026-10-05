# État du programme

Dernière mise à jour : 2026-10-05 14:50 UTC, session 5 (préenregistrement v2 de T0.4 scellé ; lancement sur H200).

## Phase en cours
Phase 0 — instruments (M0 : 5 octobre → 1er novembre 2026). Porte de sortie : G0. Aucune porte franchie.

## Tâches de la phase 0

| tâche | état | matériel | note |
|---|---|---|---|
| T0.1 socle, gouvernance, continuité | **fait** | processeur | dépôt distant github.com/lciric/controle-ia (privé) ; 140 tests au total ; gardes testées sain + artefact ; run factice 20261004-034500-factice de bout en bout ; CLAUDE.md, registres, passation |
| T0.2 vérification de l'état de l'art | **niveau 1 fait** | processeur | 13 PDF de niveau 1 lus sur source primaire (six lecteurs neufs, rapports scellés) → `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md` ; reste : niveaux 2 et 3 (PDF à recevoir), références nouvelles (Kulkarni 2604.28129 en tête), recherche affirmative (session neuve) |
| T0.3 simulation du lemme et du théorème négatif | **simulation faite** ; reste la note v3 | processeur | run décisif `20261004-080257-t03`, préenregistrement scellé 7474743a…, trois contre-lectures : **31/31 prédictions confirmées** (342 cellules statistiques, 544 trajectorielles, 0 contraire), audit de symétrie non déclenché. Résultats : `docs/notes/resultats-T0.3-v1.md`, figures `diag/20261004-080257-t03/figures/`. Réserve : la plupart des prédictions vérifient l'instrument ; ce n'est pas une preuve sur modèles réels. Reste : note mathématique v3 (résultats, puis 2208.07610 et 2601.20022 après lecture sur PDF). Gel du code levé (aucune réplication requise) |
| T0.4 harnais et activations | **fait sur modèle jouet** ; sur modèle réel : **critère 1 de G0 non concluant** (verdict R13 scellé) ; N-010 résolu (option a) : **version 2 en préparation** | processeur ; processeur graphique sous GO-2026-10-04-08 | Run `20261005-102042-validation-reelle` (A100) : P2 non concluant (précision probable : 1,27e-4 > 1e-4 à la couche 23, diffus) ; P0, P1, P3 conformes ; P4 à P8 non atteints. Verdict `docs/verdicts/verdict-T0.4-critere-1-G0-v1.md` ; proposition `docs/decisions/proposition-N-010-v1.md`. Version 2 : code au commit `47d3c61` (187 tests ; double précision, contrôle positif D1, réglages relus) ; sonde de mémoire (A100) : une carte de 80 Go ne suffit pas, carte de 141 Go (H200) retenue (note `docs/notes/memoire-double-precision-T0.4-v1.md`, R-042) ; deux contre-lectures (scellable après corrections) ; **préenregistrement v2 scellé** (886c8c07…, code cité `dc7aa7f`, 192 tests) et procédure v3 scellée (a91a5838…) ; reste : lancement sur H200, juge neuf. GPU : 0,56 heure sur 6 |
| T0.5 environnement (a) v0 | conception | processeur puis GPU sur GO | base identifiée (transcription) : « Diffuse AI Control on Fuzzy Tasks » ; code inconnu |
| T0.6 organismes v0 | conception | GPU sur GO | famille (iii) : organismes publics en 70B seulement (P-002) |
| T0.7 sondes v0 | conception | GPU sur GO | models-under-pressure (MIT) réutilisable ; deception-detection sans licence → réimplémentation |
| T0.8 bases boîte noire v0 | conception | GPU sur GO | D1 ; ajouter les bases (i) accumulation sur scores boîte noire et (iv) modèle temporel sur observateur (N-007) ; juge robustifié (P-003) |
| T0.9 papier C | conception | processeur ; pilote sur GO | HC1, HC5 et porte GC fixées (`docs/decisions/decision-N-005-N-006-v1.md`) ; préenregistrement après lecture de Panin (SSRN 7424179) ; D2 ; ressources P3 demandées |

## Derniers verdicts de porte
Aucun. T0.3 fournit la preuve du critère 5 de G0 (agrégateurs validés en simulation). Critère 1 (harnais) : prouvé sur modèle jouet seulement ; sur le modèle réel, **non concluant** (verdict R13 du 2026-10-05) ; suite selon N-010. G0 attend les autres critères.

## GO et nœuds en attente
- N-001 dépôt distant : **résolu** (github.com/lciric/controle-ia, privé, branche `main`) ; **N-003 à N-008 résolus** (GO-2026-10-04-02 à -07, option a ; `docs/decisions/`) ; **N-002 résolu** (GO-2026-10-04-08, calcul, plafond 150 dollars, échéance 2026-11-01) ; **N-009** : jeton résolu le 2026-10-05 ; reste la destruction des instances arrêtées. **N-010 résolu** (GO-2026-10-05-01, option a : version 2 de la validation de T0.4, logique en double précision, contrôle positif D1). Voir `registres/decisions.md`. Détail : `livrables/premier-rendu-v1/decisions-v1.md` et `livrables/anteriorite-niveau1-v1/decisions-v2.md`.

## Décisions ouvertes (défaut sous 48 heures)
- P-001 garde de calcul active — échéance 2026-10-06 03:40 UTC.
- D1, D2, D3 — échéance 2026-10-06 03:40 UTC.
- P-002 famille (iii) — échéance 2026-10-06 04:00 UTC.
- P-003 bras boîte noire de G1, P-004 environnement (a), P-005 famille (i) scindée — échéance 2026-10-06 05:08 UTC.

## Ressources demandées à Lazar
Voir `livrables/premier-rendu-v1/ressources-a-demander-v1.md`. Fournis le 2026-10-04 : GO du devis ; accès réseau à console.vast.ai (vérifié) ; clé `VAST_API_KEY` et jetons Hugging Face et GitHub pour l'instance (posés par Lazar ; visibles à partir de la session suivante). Restent : budget de recherche web ou session neuve ; PDF des niveaux 2 et 3, plus Panin SSRN 7424179, 2606.18276, 2603.15809, poster WiML (porte GC), 2208.07610 et 2601.20022 (note v3) ; corpus et code de P3 ; envoi du message FakeLab.

## Dépenses
Devis de la phase 0 approuvé (GO-2026-10-04-08 : plafond 150 USD, alerte à 120 USD) ; dépensé ≈ 2,4 USD (cinq instances, 0,74 heure en tout) plus les disques des instances arrêtées tant qu'elles existent. Version 2 de T0.4 attendue sur H200 : ≈ 4 à 6 USD ; au plafond cumulatif ≈ 23 USD.

## Instances de calcul actives
Aucune en marche.

Cinq instances arrêtées par leur identifiant, disques facturés jusqu'à leur destruction (décision de Lazar) :
- **54183350** (H100 SXM, arrêtée le 2026-10-04 à 18:12 UTC) et **54285455** (A100 SXM4, arrêtée le 2026-10-05 à 08:31 UTC) : sans données ;
- **54298522** (A100 SXM4, arrêtée le 2026-10-05 à 10:31 UTC) : run A de la validation de T0.4 ; résultats déjà poussés ; garder jusqu'au verdict (procédure).
- **54311651** (A100 SXM4, arrêtée le 2026-10-05 à 12:14 UTC) : sonde de mémoire non décisive de la v2 ; traces poussées et fusionnées ; sans données utiles.
- **54332340** (H200 NVL, arrêtée le 2026-10-05 à 14:55 UTC) : run A de la v2 ; résultats poussés et fusionnés ; activations par jeton sur son disque ; garder jusqu'au verdict (procédure).
