# État du programme

Dernière mise à jour : 2026-10-06 14:15 UTC, session 7 (N-009 appliqué : rien n'est détruit ; N-012, P-007 et P-008 soumis ; T0.5 : corpus de 96 papiers et code de l'environnement, du pilote et de son analyse ; état de l'art niveau 2, lot 1). Dernière passation : `registres/passations/2026-10-06-1415.md`.

## Phase en cours
Phase 0 — instruments (M0 : 5 octobre → 1er novembre 2026). Porte de sortie : G0. Aucune porte franchie.

## Tâches de la phase 0

| tâche | état | matériel | note |
|---|---|---|---|
| T0.1 socle, gouvernance, continuité | **fait** | processeur | dépôt distant github.com/lciric/controle-ia (privé) ; 140 tests au total ; gardes testées sain + artefact ; run factice 20261004-034500-factice de bout en bout ; CLAUDE.md, registres, passation |
| T0.2 vérification de l'état de l'art | **niveau 1 fait** ; **niveau 2, lot 1 fait** | processeur | Niveau 1 : 13 PDF lus sur source primaire (six lecteurs neufs) → `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md`. Niveau 2, lot 1 (2026-10-06) : 12 PDF d'arXiv récupérés et scellés par la session (`docs/sources/pdf/provenance-niveau2-lot1-v1.md`), quatre lecteurs neufs, rapports scellés dans `docs/sources/lecture-pdf-niveau2/` (561 citations contrôlées, 0 échec) : H2 occupé en entier par aucune des quatre sources (la réserve de N-007 ne déclenche pas de nœud ; bases à ajouter au préenregistrement de G1) ; HC1 : aucune pièce occupée ; porte GC : pièce libre dans ces sources, deux antériorités partielles ; lemme : deux affirmations du programme à corriger (P-008). Reste : autres références des niveaux 2 et 3 (arXiv depuis la session), recherche affirmative par un agent neuf avec la recherche web, veille hebdomadaire ; à recevoir de Lazar : Panin (SSRN 7424179), poster WiML |
| T0.3 simulation du lemme et du théorème négatif | **simulation faite** ; reste la note v3 | processeur | run décisif `20261004-080257-t03`, préenregistrement scellé 7474743a…, trois contre-lectures : **31/31 prédictions confirmées** (342 cellules statistiques, 544 trajectorielles, 0 contraire), audit de symétrie non déclenché. Résultats : `docs/notes/resultats-T0.3-v1.md`, figures `diag/20261004-080257-t03/figures/`. Réserve : la plupart des prédictions vérifient l'instrument ; ce n'est pas une preuve sur modèles réels. Reste : note mathématique v3 (résultats ; 2208.07610 et 2601.20022 lus sur PDF le 2026-10-06, formulations vérifiées dans P-008 et `docs/sources/lecture-pdf-niveau2/rapport-lemme-v1.md`). Gel du code levé (aucune réplication requise) |
| T0.4 harnais et activations | **fait** : critère 1 de G0 **prouvé** sur le modèle réel (v3, 2026-10-06) | processeur ; processeur graphique sous GO-2026-10-04-08 | v1 (A100, simple précision) : non concluant. v2 (H200 NVL) : logique validée, production au-dessus du seuil sur le maximum, pas de run B : non prouvé. v3 (H200 NVL, instance 54476244, runs `20261006-114025` et `20261006-115440-validation-reelle`, préenregistrement 4f711cd3…, code b6ab5d1) : tout conforme, run B identique ; verdict `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (63444faa…), aucune réserve ; quatre observations à Lazar (R-052). Domaine de validité consigné (R-052) : noyau « math », H200 NVL, contexte rempli jusqu'à 1 087 jetons en strict, 1 192 en production. GPU : 1,31 heure sur 6. Livrable `livrables/T0.4-harnais-v1.zip` (5b15885c…). Instances arrêtées gardées (N-009, décision de Lazar) ; leurs disques : N-012 |
| T0.5 environnement (a) v0 | **en cours** : données et code | processeur puis GPU sur GO | Reconstruction de 2606.08892 (ni code ni données publiés ; P-004). Conception proposée : P-006 (défaut (a) le 2026-10-08 à 11:37 UTC). Fait le 2026-10-06 : invites transcrites et vérifiées (18) ; chaîne de données (arXiv → pandoc 3.9, textes hors du dépôt) ; règle de sélection scellée (8f43dcae…) et run de sélection `20261006-134235-t05-corpus` (pilote de 64 papiers, réserve de 32) ; code : chargeur d'invites, rubrique et agrégation fixe, environnement en pas branché au harnais (un environnement par épisode). Reste : extraction des énoncés, classifications et cibles semées (brouillon `brouillons/T0.5-extraction-v1-brouillon1.md`, à sceller après P-006) ; juges et appariement ; préenregistrement du pilote 8B, contre-lecture, lancement (5 heures de carte au devis) |
| T0.6 organismes v0 | conception | GPU sur GO | famille (iii) : organismes publics en 70B seulement (P-002) |
| T0.7 sondes v0 | conception | GPU sur GO | models-under-pressure (MIT) réutilisable ; deception-detection sans licence → réimplémentation |
| T0.8 bases boîte noire v0 | conception | GPU sur GO | D1 ; ajouter les bases (i) accumulation sur scores boîte noire et (iv) modèle temporel sur observateur (N-007) ; juge robustifié (P-003) |
| T0.9 papier C | conception | processeur ; pilote sur GO | HC1, HC5 et porte GC fixées (`docs/decisions/decision-N-005-N-006-v1.md`) ; préenregistrement après lecture de Panin (SSRN 7424179) ; D2 ; ressources P3 demandées |

## Derniers verdicts de porte
Aucune porte franchie. Critères de G0 prouvés : **1** (harnais validé sur le modèle réel, T0.4 v3, verdict R13 du 2026-10-06) et **5** (agrégateurs validés en simulation, T0.3). Restent les critères 2 (organismes), 3 (sondes), 4 (base boîte noire), 6 (préenregistrement de G1), 7 (préenregistrement du papier C) et 8 (état de l'art vérifié).

## GO et nœuds en attente
- N-001 dépôt distant : **résolu** (github.com/lciric/controle-ia, privé, branche `main`) ; **N-003 à N-008 résolus** (GO-2026-10-04-02 à -07, option a ; `docs/decisions/`) ; **N-002 résolu** (GO-2026-10-04-08, calcul, plafond 150 dollars, échéance 2026-11-01) ; **N-009 résolu** : jeton le 2026-10-05 ; destruction : décision de Lazar le 2026-10-06, « ne détruis aucun fichier » (rien n'est détruit). **N-012 résolu** (GO-2026-10-06-02, option (a)) mais **non exécutable depuis la session** (R-060) : la clé ne permet ni copie ni exécution (« requires login ») et la garde refuse la destruction ; procédure pour Lazar : `docs/procedures/rapatriement-T0.4-tableaux-v2.md`. **P-008 retenue** (GO-2026-10-06-03 ; `docs/decisions/decision-P-008-v1.md`). **N-010 résolu** (GO-2026-10-05-01, option a : version 2 de la validation de T0.4, logique en double précision, contrôle positif D1). **N-011 résolu** (GO-2026-10-06-01, option a : version 3 de la validation de T0.4, garde de production sur le 99e centile fondée sur le repère, contrôle strict du chemin de production). Voir `registres/decisions.md`. Détail : `livrables/premier-rendu-v1/decisions-v1.md` et `livrables/anteriorite-niveau1-v1/decisions-v2.md`.

## Décisions ouvertes (défaut sous 48 heures)
- P-006 (T0.5, conception de l'environnement (a) v0) : proposée le 2026-10-06 ; défaut (a) le 2026-10-08 à 11:37 UTC.
- P-007 (plan des critères restants de G0, `docs/decisions/proposition-P-007-plan-G0-v1.md`) : proposée le 2026-10-06 à 14:30 UTC ; défaut (a) le 2026-10-08 à 14:30 UTC.
- P-008 (corrections de trois affirmations du programme, `docs/decisions/proposition-P-008-corrections-programme-v1.md`) : proposée le 2026-10-06 ; sans défaut (le programme ne se modifie que par Lazar).

Avant cela : Défauts appliqués le 2026-10-06 08:47 UTC (R-047) : P-001, D1, D2, D3, P-002, P-003, P-004 (la correction de formulation du programme reste proposée à Lazar), P-005.

## Ressources demandées à Lazar
Voir `livrables/premier-rendu-v1/ressources-a-demander-v1.md`. Fournis le 2026-10-04 : GO du devis ; accès réseau à console.vast.ai (vérifié) ; clé `VAST_API_KEY` et jetons Hugging Face et GitHub pour l'instance (posés par Lazar ; visibles à partir de la session suivante). Depuis le 2026-10-06 vers 13:20 UTC, la recherche web et arXiv répondent depuis la session (ressources 1 et 2 de la liste satisfaites ; SSRN refuse, 403). Restent : Panin SSRN 7424179 et le poster WiML NeurIPS 2025 (porte GC, hors d'arXiv) ; corpus de pression et code de la loi d'attraction de P3 ; envoi du message FakeLab.

## Dépenses
Devis de la phase 0 approuvé (GO-2026-10-04-08 : plafond 150 USD, alerte à 120 USD). Cumul au 2026-10-06 13:25 UTC ≈ 12,3 USD : marche ≈ 5,1 (six instances, 1,31 heure de carte pour T0.4), disques ≈ 7,2. Disques des six instances gardées : ≈ 7,3 USD par jour ; projection et options : N-012 (`diag/N-012-projection-depenses/projection_v1.json`).

## Instances de calcul actives
Aucune instance du programme en marche. **Trois instances hors du programme en marche** (R-061) : 54497596, 54498054, 54500347 (H100 SXM, étiquettes `rr-organism_inhibition-…`, ≈ 12 USD de l'heure en tout), non lancées par la session, non touchées ; Lazar prévenu.

Six instances arrêtées par leur identifiant, gardées avec tous leurs fichiers (décision de Lazar du 2026-10-06 sur N-009) ; disques facturés ≈ 0,303 USD de l'heure en tout (N-012) :
- **54183350** (H100 SXM, arrêtée le 2026-10-04 à 18:12 UTC) et **54285455** (A100 SXM4, arrêtée le 2026-10-05 à 08:31 UTC) : sans données ;
- **54298522** (A100 SXM4, arrêtée le 2026-10-05 à 10:31 UTC) : run A de la validation de T0.4 ; résultats déjà poussés ; garder jusqu'au verdict (procédure).
- **54311651** (A100 SXM4, arrêtée le 2026-10-05 à 12:14 UTC) : sonde de mémoire non décisive de la v2 ; traces poussées et fusionnées ; sans données utiles.
- **54332340** (H200 NVL, arrêtée le 2026-10-05 à 14:55 UTC) : run A de la v2 ; résultats poussés et fusionnés ; activations par jeton sur son disque ; garder jusqu'au verdict (procédure).
- **54476244** (H200 NVL, arrêtée le 2026-10-06 à 12:11 UTC) : runs A et B de la v3 ; résultats poussés et fusionnés ; activations par jeton sur son disque ; garder jusqu'au verdict (procédure).
