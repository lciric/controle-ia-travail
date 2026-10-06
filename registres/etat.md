# État du programme

Dernière mise à jour : 2026-10-06 12:55 UTC, session 6 (T0.4 v3 : run complet, verdict R13 scellé, critère 1 de G0 prouvé ; P-006 proposée ; passation `registres/passations/2026-10-06-1249.md`).

## Phase en cours
Phase 0 — instruments (M0 : 5 octobre → 1er novembre 2026). Porte de sortie : G0. Aucune porte franchie.

## Tâches de la phase 0

| tâche | état | matériel | note |
|---|---|---|---|
| T0.1 socle, gouvernance, continuité | **fait** | processeur | dépôt distant github.com/lciric/controle-ia (privé) ; 140 tests au total ; gardes testées sain + artefact ; run factice 20261004-034500-factice de bout en bout ; CLAUDE.md, registres, passation |
| T0.2 vérification de l'état de l'art | **niveau 1 fait** | processeur | 13 PDF de niveau 1 lus sur source primaire (six lecteurs neufs, rapports scellés) → `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md` ; reste : niveaux 2 et 3 (PDF à recevoir), références nouvelles (Kulkarni 2604.28129 en tête), recherche affirmative (session neuve) |
| T0.3 simulation du lemme et du théorème négatif | **simulation faite** ; reste la note v3 | processeur | run décisif `20261004-080257-t03`, préenregistrement scellé 7474743a…, trois contre-lectures : **31/31 prédictions confirmées** (342 cellules statistiques, 544 trajectorielles, 0 contraire), audit de symétrie non déclenché. Résultats : `docs/notes/resultats-T0.3-v1.md`, figures `diag/20261004-080257-t03/figures/`. Réserve : la plupart des prédictions vérifient l'instrument ; ce n'est pas une preuve sur modèles réels. Reste : note mathématique v3 (résultats, puis 2208.07610 et 2601.20022 après lecture sur PDF). Gel du code levé (aucune réplication requise) |
| T0.4 harnais et activations | **fait** : critère 1 de G0 **prouvé** sur le modèle réel (v3, 2026-10-06) | processeur ; processeur graphique sous GO-2026-10-04-08 | v1 (A100, simple précision) : non concluant. v2 (H200 NVL) : logique validée, production au-dessus du seuil sur le maximum, pas de run B : non prouvé. v3 (H200 NVL, instance 54476244, runs `20261006-114025` et `20261006-115440-validation-reelle`, préenregistrement 4f711cd3…, code b6ab5d1) : tout conforme, run B identique ; verdict `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (63444faa…), aucune réserve ; quatre observations à Lazar (R-052). Domaine de validité consigné (R-052) : noyau « math », H200 NVL, contexte rempli jusqu'à 1 087 jetons en strict, 1 192 en production. GPU : 1,31 heure sur 6. Livrable `livrables/T0.4-harnais-v1.zip` (5b15885c…). Reste : destruction des instances arrêtées (Lazar, N-009) |
| T0.5 environnement (a) v0 | conception | processeur puis GPU sur GO | base identifiée (transcription) : « Diffuse AI Control on Fuzzy Tasks » ; code inconnu |
| T0.6 organismes v0 | conception | GPU sur GO | famille (iii) : organismes publics en 70B seulement (P-002) |
| T0.7 sondes v0 | conception | GPU sur GO | models-under-pressure (MIT) réutilisable ; deception-detection sans licence → réimplémentation |
| T0.8 bases boîte noire v0 | conception | GPU sur GO | D1 ; ajouter les bases (i) accumulation sur scores boîte noire et (iv) modèle temporel sur observateur (N-007) ; juge robustifié (P-003) |
| T0.9 papier C | conception | processeur ; pilote sur GO | HC1, HC5 et porte GC fixées (`docs/decisions/decision-N-005-N-006-v1.md`) ; préenregistrement après lecture de Panin (SSRN 7424179) ; D2 ; ressources P3 demandées |

## Derniers verdicts de porte
Aucune porte franchie. Critères de G0 prouvés : **1** (harnais validé sur le modèle réel, T0.4 v3, verdict R13 du 2026-10-06) et **5** (agrégateurs validés en simulation, T0.3). Restent les critères 2 (organismes), 3 (sondes), 4 (base boîte noire), 6 (préenregistrement de G1), 7 (préenregistrement du papier C) et 8 (état de l'art vérifié).

## GO et nœuds en attente
- N-001 dépôt distant : **résolu** (github.com/lciric/controle-ia, privé, branche `main`) ; **N-003 à N-008 résolus** (GO-2026-10-04-02 à -07, option a ; `docs/decisions/`) ; **N-002 résolu** (GO-2026-10-04-08, calcul, plafond 150 dollars, échéance 2026-11-01) ; **N-009** : jeton résolu le 2026-10-05 ; reste la destruction des instances arrêtées. **N-010 résolu** (GO-2026-10-05-01, option a : version 2 de la validation de T0.4, logique en double précision, contrôle positif D1). **N-011 résolu** (GO-2026-10-06-01, option a : version 3 de la validation de T0.4, garde de production sur le 99e centile fondée sur le repère, contrôle strict du chemin de production). Voir `registres/decisions.md`. Détail : `livrables/premier-rendu-v1/decisions-v1.md` et `livrables/anteriorite-niveau1-v1/decisions-v2.md`.

## Décisions ouvertes (défaut sous 48 heures)
- P-006 (T0.5, conception de l'environnement (a) v0) : proposée le 2026-10-06 ; défaut (a) à l'échéance consignée dans `registres/decisions.md`.

Avant cela : Défauts appliqués le 2026-10-06 08:47 UTC (R-047) : P-001, D1, D2, D3, P-002, P-003, P-004 (la correction de formulation du programme reste proposée à Lazar), P-005.

## Ressources demandées à Lazar
Voir `livrables/premier-rendu-v1/ressources-a-demander-v1.md`. Fournis le 2026-10-04 : GO du devis ; accès réseau à console.vast.ai (vérifié) ; clé `VAST_API_KEY` et jetons Hugging Face et GitHub pour l'instance (posés par Lazar ; visibles à partir de la session suivante). Restent : budget de recherche web ou session neuve ; PDF des niveaux 2 et 3, plus Panin SSRN 7424179, 2606.18276, 2603.15809, poster WiML (porte GC), 2208.07610 et 2601.20022 (note v3) ; corpus et code de P3 ; envoi du message FakeLab.

## Dépenses
Devis de la phase 0 approuvé (GO-2026-10-04-08 : plafond 150 USD, alerte à 120 USD) ; dépensé ≈ 2,4 USD (cinq instances, 0,74 heure en tout) plus les disques des instances arrêtées tant qu'elles existent. Version 3 de T0.4 attendue sur H200 : ≈ 3 à 6 USD (0,6 à 1,2 heure) ; au plafond cumulatif (5,26 heures) ≈ 23 USD à 4,4 USD/h.

## Instances de calcul actives
Aucune en marche.

Six instances arrêtées par leur identifiant, disques facturés jusqu'à leur destruction (décision de Lazar) :
- **54183350** (H100 SXM, arrêtée le 2026-10-04 à 18:12 UTC) et **54285455** (A100 SXM4, arrêtée le 2026-10-05 à 08:31 UTC) : sans données ;
- **54298522** (A100 SXM4, arrêtée le 2026-10-05 à 10:31 UTC) : run A de la validation de T0.4 ; résultats déjà poussés ; garder jusqu'au verdict (procédure).
- **54311651** (A100 SXM4, arrêtée le 2026-10-05 à 12:14 UTC) : sonde de mémoire non décisive de la v2 ; traces poussées et fusionnées ; sans données utiles.
- **54332340** (H200 NVL, arrêtée le 2026-10-05 à 14:55 UTC) : run A de la v2 ; résultats poussés et fusionnés ; activations par jeton sur son disque ; garder jusqu'au verdict (procédure).
- **54476244** (H200 NVL, arrêtée le 2026-10-06 à 12:11 UTC) : runs A et B de la v3 ; résultats poussés et fusionnés ; activations par jeton sur son disque ; garder jusqu'au verdict (procédure).
