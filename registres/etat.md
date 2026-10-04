# État du programme

Dernière mise à jour : 2026-10-04 10:44 UTC, session 1.

## Phase en cours
Phase 0 — instruments (M0 : 5 octobre → 1er novembre 2026). Porte de sortie : G0. Aucune porte franchie.

## Tâches de la phase 0

| tâche | état | matériel | note |
|---|---|---|---|
| T0.1 socle, gouvernance, continuité | **fait** | processeur | dépôt distant github.com/lciric/controle-ia (privé) ; 140 tests au total ; gardes testées sain + artefact ; run factice 20261004-034500-factice de bout en bout ; CLAUDE.md, registres, passation |
| T0.2 vérification de l'état de l'art | **niveau 1 fait** | processeur | 13 PDF de niveau 1 lus sur source primaire (six lecteurs neufs, rapports scellés) → `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md` ; reste : niveaux 2 et 3 (PDF à recevoir), références nouvelles (Kulkarni 2604.28129 en tête), recherche affirmative (session neuve) |
| T0.3 simulation du lemme et du théorème négatif | **simulation faite** ; reste la note v3 | processeur | run décisif `20261004-080257-t03`, préenregistrement scellé 7474743a…, trois contre-lectures : **31/31 prédictions confirmées** (342 cellules statistiques, 544 trajectorielles, 0 contraire), audit de symétrie non déclenché. Résultats : `docs/notes/resultats-T0.3-v1.md`, figures `diag/20261004-080257-t03/figures/`. Réserve : la plupart des prédictions vérifient l'instrument ; ce n'est pas une preuve sur modèles réels. Reste : note mathématique v3 (résultats, puis 2208.07610 et 2601.20022 après lecture sur PDF). Gel du code levé (aucune réplication requise) |
| T0.4 harnais et activations | **fait sur modèle jouet** ; reste le modèle réel | processeur ; processeur graphique sur GO (N-002) | code `src/controle_ia/harnais/` (R-029, corrigé par R-030 : agrégation sur les jetons par maximum ou attention seulement). Preuve : runs `20261004-104156-harnais-factice` et `20261004-104211-harnais-factice`, deux processus de même entropie (résumés scellés 0bcb6675… et df380648…) : poids, trajectoires, activations par jeton, vecteurs d'action et scores de sondes identiques au bit près ; écart d'équivalence génération / passe unique ≤ 3,7e-8 (tolérance 1e-4) ; disque relu et recalcul hors ligne identiques ; activations par jeton gardées seulement pour l'épisode d'entraînement déclaré. Stockage estimé pour le modèle réel (2 000 épisodes, 3 couches) : 295 Go tout par jeton contre 30,5 Go en politique par défaut. Reste, sur GO : modèle réel en demi-précision (tolérance d'équivalence à fixer, déterminisme au bit près sur processeur graphique à montrer). Les runs 20261004-110000 et -110001 (dernier jeton stocké) restent archivés, remplacés |
| T0.5 environnement (a) v0 | conception | processeur puis GPU sur GO | base identifiée (transcription) : « Diffuse AI Control on Fuzzy Tasks » ; code inconnu |
| T0.6 organismes v0 | conception | GPU sur GO | famille (iii) : organismes publics en 70B seulement (P-002) |
| T0.7 sondes v0 | conception | GPU sur GO | models-under-pressure (MIT) réutilisable ; deception-detection sans licence → réimplémentation |
| T0.8 bases boîte noire v0 | conception | GPU sur GO | D1 ; ajouter les bases (i) accumulation sur scores boîte noire et (iv) modèle temporel sur observateur (N-007) ; juge robustifié (P-003) |
| T0.9 papier C | conception | processeur ; pilote sur GO | HC1, HC5 et porte GC fixées (`docs/decisions/decision-N-005-N-006-v1.md`) ; préenregistrement après lecture de Panin (SSRN 7424179) ; D2 ; ressources P3 demandées |

## Derniers verdicts de porte
Aucun. T0.3 fournit la preuve du critère 5 de G0 (agrégateurs validés en simulation). T0.4 fournit la preuve du critère 1 (harnais) sur modèle jouet seulement ; sur le modèle réel, après le GO N-002. G0 attend les autres critères.

## GO et nœuds en attente
- N-001 dépôt distant : **résolu** (github.com/lciric/controle-ia, privé, branche `main`) ; **N-003 à N-008 résolus** (GO-2026-10-04-02 à -07, option a ; `docs/decisions/`) ; **seul nœud ouvert : N-002** (devis de la phase 0, 150 dollars). Détail : `livrables/premier-rendu-v1/decisions-v1.md` et `livrables/anteriorite-niveau1-v1/decisions-v2.md`.

## Décisions ouvertes (défaut sous 48 heures)
- P-001 garde de calcul active — échéance 2026-10-06 03:40 UTC.
- D1, D2, D3 — échéance 2026-10-06 03:40 UTC.
- P-002 famille (iii) — échéance 2026-10-06 04:00 UTC.
- P-003 bras boîte noire de G1, P-004 environnement (a), P-005 famille (i) scindée — échéance 2026-10-06 05:08 UTC.

## Ressources demandées à Lazar
Voir `livrables/premier-rendu-v1/ressources-a-demander-v1.md` : budget de recherche web ou session neuve ; PDF des niveaux 2 et 3, plus Panin SSRN 7424179, 2606.18276, 2603.15809, poster WiML (porte GC), 2208.07610 et 2601.20022 (note v3) ; GO devis ; jeton HuggingFace ; compte Vast.ai ; corpus et code de P3 ; envoi du message FakeLab.

## Dépenses
0 USD engagé ; aucun devis approuvé.

## Instances de calcul actives
Aucune.
