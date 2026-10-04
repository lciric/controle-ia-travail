# Registre des décisions

Routine : décidée et consignée ici. « Proposer avec recommandation » : défaut appliqué 48 heures après la proposition sans réponse.
Nœud de décision : arrêt jusqu'au GO (voir `registres/go.md`).

## Routine

| id | date (UTC) | décision | raison |
|---|---|---|---|
| R-001 | 2026-10-04 | Dépôt du programme dans un dépôt git neuf `controle-ia`, séparé de `cplt_run_2026-09-03`. | Instruction explicite de Lazar du 2026-10-04 (« rien à voir avec cplt run ») ; elle prime sur « le dossier où Lazar t'a lancé » du brief. |
| R-002 | 2026-10-04 | Code dans un paquet unique `src/controle_ia/` ; les sous-dossiers du brief (harnais, environnements, organismes, sondes, agregateurs, moniteurs_noirs) y deviennent des sous-paquets à mesure qu'ils naissent. | Évite les collisions de noms de modules génériques ; arborescence « adaptable » selon le brief. |
| R-003 | 2026-10-04 | Périmètre du scellement : chaque fichier de `docs/`, `prereg/`, `runs/`, `diag/`, `livrables/`, `registres/passations/` est un dépôt scellé ; les registres vivants (`registres/*.md`) sont versionnés par git, non scellés. | R6 porte sur les dépôts immuables ; un registre vivant changerait d'empreinte à chaque entrée. |
| R-004 | 2026-10-04 | Format du registre des GO : table à 8 colonnes, identifiant `GO-AAAA-MM-JJ-NN` ; tout lancement d'instance payante doit citer l'identifiant d'un GO « calcul » valide. | Rend la garde de calcul vérifiable par machine et rattache chaque lancement à un GO. |
| R-005 | 2026-10-04 | Environnement processeur : Python 3.11, environnement virtuel `.venv`, versions figées dans `requirements-cpu.txt` (numpy 2.4.6, scipy 1.17.1, matplotlib 3.11.2, pytest 9.1.1). | R9 (numpy ≥ 1.25) ; reproductibilité. |
| R-006 | 2026-10-04 | Graines : une `SeedSequence` racine par run ; graine de tâche = même entropie + clé de dérivation tirée de l'empreinte SHA-256 du nom de la tâche ; état de contrôle consigné et revérifié au rejeu. | Graines indépendantes de l'ordre des tâches ; altération détectée (R9, R5). |
| R-007 | 2026-10-04 | Identifiant de run `AAAAMMJJ-HHMMSS-nom` ; résultat écrit dans `diag/<run>/` et rattaché au manifeste par l'empreinte de celui-ci ; un run dont l'arbre git est sale est refusé, sauf autorisation explicite consignée comme réserve. | Traçabilité totale (R6, R9) sans repli silencieux (R5). |
| R-008 | 2026-10-04 | Préenregistrement : sections de niveau 2 obligatoires (R1 + « Contre-lecture » pour R2), marqueur « À REMPLIR » interdit au scellement ; un run « décisif » exige un préenregistrement scellé et conforme. | Rend R1 et R2 vérifiables par machine. |
| R-009 | 2026-10-04 | `.gitattributes` : `* -text` (aucune conversion de fins de ligne). | Une conversion sous Windows changerait les octets et casserait les empreintes. |
| R-010 | 2026-10-04 | Recherche d'antériorité menée d'abord par recherche web (sous-agents, contre-vérification adverse), étiquetée « transcription, non opposable » ; la vérification sur PDF empreinté (T0.2 proprement dite) attend l'accès réseau à arxiv.org. | arxiv.org, openreview.net, semanticscholar.org, huggingface.co sont refusés par la politique réseau de l'environnement (constat du 2026-10-04 03:10 UTC). Demande de Lazar : antériorité approfondie avant de se lancer. |
| R-011 | 2026-10-04 | Aucun code sans licence n'est copié dans le dépôt (deception-detection d'Apollo, obfuscated-activations, distributed_sabotage_frontier, JudgeDeceiver) : lecture et citation seulement, réimplémentation d'après les articles. | Sans licence, le droit d'auteur par défaut s'applique (`docs/sources/ressources-code-v1.md`). |
| R-012 | 2026-10-04 | T0.3 préenregistre et teste à la fois les énoncés du programme tels qu'écrits et les énoncés précisés de la note mathématique v1 ; aucune revendication n'est modifiée avant décision sur N-003 et N-004. | Tester n'est pas modifier ; les deux issues sont informatives (R3, R4). |
| R-013 | 2026-10-04 | Les trois chaînes de recherche d'antériorité ont été arrêtées par identifiant dès l'épuisement du budget de recherche web ; leurs résultats valides sont conservés et scellés ; les verdicts « indéterminés » ne valent pas « vierge ». | R8 : une zone non cherchée n'est pas une zone vierge. |

| R-014 | 2026-10-04 | La note mathématique v1 est remplacée par la v2 (nouveau nom, v1 archivée), qui intègre la contre-vérification adverse : forme unilatérale du processus e, L1 dépendant de n₀, seuil exact du max, L5 corrigé, classes C et K distinguées, T3 restreint aux statistiques locales, T4 précisé, gardes de mauvaise spécification. | R4 et R12 ; contre-vérification reproduite (deux scripts rejoués à l'identique). |
| R-015 | 2026-10-04 | Les simulations exploratoires du contre-vérificateur seront déclarées dans le préenregistrement de T0.3 ; T0.3 utilisera des graines neuves et une grille fixée indépendamment ; ses prédictions sont tirées des preuves. | R1 : transparence sur toute lecture antérieure au scellement. |

| R-016 | 2026-10-04 | Module `src/controle_ia/agregateurs/` : épisodes (N, T) indexés (agent, pas), lecture « temps d'abord » ; processus e de mélange normal unilatéral et bilatéral en logarithme ; statistiques symétriques à sommation exacte (invariance au bit près), statistiques locales (balayage, Page, co-élévation), statistiques globales (autocorrélation, suites, corrélation entre agents). Tests : formes closes contre intégration numérique, validité sous P₀ et artefact σ sous-estimé, invariance au bit près, identité terminale, garanties locales, gardes. | Instrument de T0.3 (note v2) ; aucune puissance préenregistrée n'est mesurée par ces tests (R1). |

| R-017 | 2026-10-04 | Rapport consolidé de niveau 1 (`docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md`) publié seulement après un contrôle de traçabilité par un sous-agent neuf (chaque chiffre recontrôlé dans les PDF, recalculs indépendants) ; corrections intégrées avant scellement ; nature de chaque chiffre marquée (auteurs, figure, calcul, simulation). | R6, R7, R4. |

## Propositions avec recommandation (défaut sous 48 heures)

| id | proposée le (UTC) | décision | défaut | échéance (UTC) | statut |
|---|---|---|---|---|---|
| P-001 | 2026-10-04 03:40 | Garde de calcul (hook PreToolUse) active dans ce dépôt. | Active (elle ne bloque que ce que les règles interdisent déjà ; désactivable dans `.claude/settings.json`). | 2026-10-06 03:40 | active à titre conservatoire |
| D1 | 2026-10-04 03:40 | Moniteur boîte noire. | (a) même modèle que l'agent en juge + (b) modèle de confiance plus faible (Llama-3.2-3B-Instruct). | 2026-10-06 03:40 | ouverte |
| D2 | 2026-10-04 03:40 | Panel de juges génératifs du papier C. | Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3 (licence Apache 2.0, même empreinte mémoire). | 2026-10-06 03:40 | ouverte |
| D3 | 2026-10-04 03:40 | Grille du nombre d'agents en phase 3. | N ∈ {1, 2, 3, 5, 10}. | 2026-10-06 03:40 | ouverte |
| P-002 | 2026-10-04 04:00 | Famille d'organismes (iii) : les organismes publics sont des 70B. | (a) retirée de la phase 0 ; contrôle externe sur 70B en phase 1, devis séparé. | 2026-10-06 04:00 | ouverte |

| P-003 | 2026-10-04 05:08 | Bras boîte noire de G1 rendus forts : juge robustifié de type b* (invites de 2606.08892) à côté de TRACE-lite, planchers « tout signaler » et « juge en une passe », journal des arrêts précoces et JSON invalides, score continu par probabilité des jetons. | Appliquer. | 2026-10-06 05:08 | ouverte |
| P-004 | 2026-10-04 05:08 | Environnement (a) : reconstruction minimale fidèle (pas de portage possible), pilote 8B scellé d'abord, cibles semées, contributions (agent, pas), dose = proportion × intensité ; corriger « porté en 8B » (programme, section 6) en « reconstruit ». | Appliquer. | 2026-10-06 05:08 | ouverte |
| P-005 | 2026-10-04 05:08 | Famille d'organismes (i) scindée : (i-a) consigne de saboter en dissimulant ; (i-b) stratégie biaisée d'apparence sincère ; témoin « instruit sans sabotage » ; prédiction de validité précisée en conséquence. | Appliquer. | 2026-10-06 05:08 | ouverte |

## Nœuds de décision en attente

| id | ouvert le | objet | ce qu'il faut |
|---|---|---|---|
| N-001 | 2026-10-04 | Dépôt distant du programme. | **Résolu le 2026-10-04 vers 04:08 UTC** : GO-2026-10-04-01 ; création par l'application GitHub refusée (403) ; dépôt privé `lciric/controle-ia` créé par Lazar (vide), rattaché à la session avec droits de poussée ; `main` poussé (79012de, 7 commits) ; visibilité vérifiée : privée. |
| N-002 | 2026-10-04 | Devis de calcul de la phase 0. | GO de Lazar sur `livrables/premier-rendu-v1/devis-v1.md` (plafond 150 USD). |
| N-003 | 2026-10-04 | Théorème négatif : 2606.10456 revendique la version boîte noire, mais son énoncé est vide et faux pour sa construction ; l'énoncé du programme a le même défaut (renforcé après lecture du PDF). | GO sur la reformulation (recommandation : énoncé par invariance) — `livrables/premier-rendu-v1/decisions-v1.md`. |
| N-004 | 2026-10-04 | Lemme d'additivité : cœur statistique classique ; calendrier et compensation. | GO sur le repositionnement (recommandation : énoncé adverse). |
| N-005 | 2026-10-04 | Loi de déférence (HC1) : collision confirmée et élargie sur PDF (2508.07805 : note continue par juge et par technique ; 2606.07897 : pente de déférence continue, rangs stables) ; la porte GC vise le mauvais papier. | GO sur la reformulation (recommandation : conjonction encore libre, stabilité de rang) — `livrables/anteriorite-niveau1-v1/decisions-v2.md`. |
| N-006 | 2026-10-04 | Contre-mesures (HC5) : quorum hétérogène entre juges déjà recommandé par 2607.08066. | GO sur la reformulation (recommandation : quorum en type d'accès + paraphrase + matrice de transfert). |
| N-007 | 2026-10-04 | H2 plus occupée qu'annoncé (Doomed from the Start 2607.06503 ; E-valuator accepte tout score). | GO sur la reformulation et les quatre bases ajoutées, à confirmer après lecture de Kulkarni 2604.28129, Padhi 2604.19775, FIPER, Yueh-Han 2506.10949 — `livrables/anteriorite-niveau1-v1/decisions-v2.md`. |
| N-008 | 2026-10-04 | Critère de G1 : le bras « + 5 points de F1 » se gagne en sur-signalant (TRACE ≈ 75 % de faux positifs ; « tout signaler » F1 0,744). | GO sur la modification du critère de porte (recommandation après contrôle : retirer le bras F1, garder le rappel à 1 % de faux positifs avec intervalle à 95 %, planchers rapportés). |
