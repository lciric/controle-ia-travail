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

## Propositions avec recommandation (défaut sous 48 heures)

| id | proposée le (UTC) | décision | défaut | échéance (UTC) | statut |
|---|---|---|---|---|---|
| P-001 | 2026-10-04 03:40 | Garde de calcul (hook PreToolUse) active dans ce dépôt. | Active (elle ne bloque que ce que les règles interdisent déjà ; désactivable dans `.claude/settings.json`). | 2026-10-06 03:40 | active à titre conservatoire |
| D1 | 2026-10-04 03:40 | Moniteur boîte noire. | (a) même modèle que l'agent en juge + (b) modèle de confiance plus faible (Llama-3.2-3B-Instruct). | 2026-10-06 03:40 | ouverte |
| D2 | 2026-10-04 03:40 | Panel de juges génératifs du papier C. | Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3 (licence Apache 2.0, même empreinte mémoire). | 2026-10-06 03:40 | ouverte |
| D3 | 2026-10-04 03:40 | Grille du nombre d'agents en phase 3. | N ∈ {1, 2, 3, 5, 10}. | 2026-10-06 03:40 | ouverte |

## Nœuds de décision en attente

| id | ouvert le | objet | ce qu'il faut |
|---|---|---|---|
| N-001 | 2026-10-04 | Dépôt distant du programme (création = nœud de décision). | Choix et GO de Lazar ; sans dépôt distant, le travail ne survit pas au conteneur. |
| N-002 | 2026-10-04 | Devis de calcul de la phase 0. | GO de Lazar sur `livrables/premier-rendu-v1/devis-phase0-v1.md`. |
