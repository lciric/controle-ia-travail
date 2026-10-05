# État du programme

Dernière mise à jour : 2026-10-05 10:18 UTC, session 4 (troisième lancement).

## Phase en cours
Phase 0 — instruments (M0 : 5 octobre → 1er novembre 2026). Porte de sortie : G0. Aucune porte franchie.

## Tâches de la phase 0

| tâche | état | matériel | note |
|---|---|---|---|
| T0.1 socle, gouvernance, continuité | **fait** | processeur | dépôt distant github.com/lciric/controle-ia (privé) ; 140 tests au total ; gardes testées sain + artefact ; run factice 20261004-034500-factice de bout en bout ; CLAUDE.md, registres, passation |
| T0.2 vérification de l'état de l'art | **niveau 1 fait** | processeur | 13 PDF de niveau 1 lus sur source primaire (six lecteurs neufs, rapports scellés) → `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md` ; reste : niveaux 2 et 3 (PDF à recevoir), références nouvelles (Kulkarni 2604.28129 en tête), recherche affirmative (session neuve) |
| T0.3 simulation du lemme et du théorème négatif | **simulation faite** ; reste la note v3 | processeur | run décisif `20261004-080257-t03`, préenregistrement scellé 7474743a…, trois contre-lectures : **31/31 prédictions confirmées** (342 cellules statistiques, 544 trajectorielles, 0 contraire), audit de symétrie non déclenché. Résultats : `docs/notes/resultats-T0.3-v1.md`, figures `diag/20261004-080257-t03/figures/`. Réserve : la plupart des prédictions vérifient l'instrument ; ce n'est pas une preuve sur modèles réels. Reste : note mathématique v3 (résultats, puis 2208.07610 et 2601.20022 après lecture sur PDF). Gel du code levé (aucune réplication requise) |
| T0.4 harnais et activations | **fait sur modèle jouet** ; validation sur modèle réel : préenregistrement scellé ; **deux lancements en échec avant le clonage** (jeton GitHub refusé) ; bloquée sur N-009 | processeur ; processeur graphique sous GO-2026-10-04-08 | Modèle réel : préenregistrement `prereg/T0.4-validation-modele-reel-v1.md` (3d0589c8…) ; procédure v2 (e8a596c3…) ; code cité 3a7b5e0 (178 tests) ; instances 54183350 (2026-10-04) et 54285455 (2026-10-05) : clonages refusés (403), aucun run ; 0,19 heure consommée sur 6 ; journaux scellés dans `traces/` |
| T0.5 environnement (a) v0 | conception | processeur puis GPU sur GO | base identifiée (transcription) : « Diffuse AI Control on Fuzzy Tasks » ; code inconnu |
| T0.6 organismes v0 | conception | GPU sur GO | famille (iii) : organismes publics en 70B seulement (P-002) |
| T0.7 sondes v0 | conception | GPU sur GO | models-under-pressure (MIT) réutilisable ; deception-detection sans licence → réimplémentation |
| T0.8 bases boîte noire v0 | conception | GPU sur GO | D1 ; ajouter les bases (i) accumulation sur scores boîte noire et (iv) modèle temporel sur observateur (N-007) ; juge robustifié (P-003) |
| T0.9 papier C | conception | processeur ; pilote sur GO | HC1, HC5 et porte GC fixées (`docs/decisions/decision-N-005-N-006-v1.md`) ; préenregistrement après lecture de Panin (SSRN 7424179) ; D2 ; ressources P3 demandées |

## Derniers verdicts de porte
Aucun. T0.3 fournit la preuve du critère 5 de G0 (agrégateurs validés en simulation). T0.4 fournit la preuve du critère 1 (harnais) sur modèle jouet seulement ; sur le modèle réel, après le GO N-002. G0 attend les autres critères.

## GO et nœuds en attente
- N-001 dépôt distant : **résolu** (github.com/lciric/controle-ia, privé, branche `main`) ; **N-003 à N-008 résolus** (GO-2026-10-04-02 à -07, option a ; `docs/decisions/`) ; **N-002 résolu** (GO-2026-10-04-08, calcul, plafond 150 dollars, échéance 2026-11-01) ; **N-009 ouvert** (jeton GitHub de l'instance refusé ; destruction de l'instance 54183350 ; voir `registres/decisions.md`). Détail : `livrables/premier-rendu-v1/decisions-v1.md` et `livrables/anteriorite-niveau1-v1/decisions-v2.md`.

## Décisions ouvertes (défaut sous 48 heures)
- P-001 garde de calcul active — échéance 2026-10-06 03:40 UTC.
- D1, D2, D3 — échéance 2026-10-06 03:40 UTC.
- P-002 famille (iii) — échéance 2026-10-06 04:00 UTC.
- P-003 bras boîte noire de G1, P-004 environnement (a), P-005 famille (i) scindée — échéance 2026-10-06 05:08 UTC.

## Ressources demandées à Lazar
Voir `livrables/premier-rendu-v1/ressources-a-demander-v1.md`. Fournis le 2026-10-04 : GO du devis ; accès réseau à console.vast.ai (vérifié) ; clé `VAST_API_KEY` et jetons Hugging Face et GitHub pour l'instance (posés par Lazar ; visibles à partir de la session suivante). Restent : budget de recherche web ou session neuve ; PDF des niveaux 2 et 3, plus Panin SSRN 7424179, 2606.18276, 2603.15809, poster WiML (porte GC), 2208.07610 et 2601.20022 (note v3) ; corpus et code de P3 ; envoi du message FakeLab.

## Dépenses
Devis de la phase 0 approuvé (GO-2026-10-04-08 : plafond 150 USD, alerte à 120 USD) ; dépensé ≈ 0,55 USD (instances 54183350 et 54285455, 0,19 heure en tout) plus les disques des instances arrêtées tant qu'elles existent.

## Instances de calcul actives
- **54298522** (Vast.ai, A100 SXM4, 1,093 USD/h) : créée le 2026-10-05 à 10:18 UTC sous GO-2026-10-04-08, troisième lancement de la validation de T0.4 (procédure v2, commit de scellement 6cf7f20). Tâche en cours : amorce. Surveillance par le script scellé ; plafond cumulatif de T0.4 atteint le 2026-10-05 à 16:06 UTC. Arrêt par identifiant dès la sortie de la surveillance (R10).
- Arrêtées, sans données, disques facturés jusqu'à leur destruction (soumise à Lazar, N-009) : **54183350** (H100 SXM, depuis le 2026-10-04 18:12 UTC) et **54285455** (A100 SXM4, depuis le 2026-10-05 08:31 UTC).
