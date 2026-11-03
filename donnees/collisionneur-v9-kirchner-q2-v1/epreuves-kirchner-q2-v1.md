# Épreuves sans appel des lanceurs du tour Kirchner Q2 (collisionneur v9) — v1

Session développeur de session-depot, 3 novembre 2026, écrit à 10:18 UTC (heure relevée par `date -u`). Aucune clé dans
l'environnement des épreuves (`env -i`, mandataire mort `HTTPS_PROXY=http://127.0.0.1:9`) ; aucun appel réseau ; chaque cas joue
une copie neuve du dossier, hors du dépôt ; la copie est comparée fichier par fichier avant et après (empreintes).
Lanceurs éprouvés : `lancer-tour-kirchner-q2-v9-v1.sh` (8c0d3812…) et `lancer-tour-kirchner-q2-v9-sans-argon-v1.sh` (760e7957…).
Python avec `anthropic` : un environnement virtuel du bloc-notes de la session (passé dans `PY_COLLISIONNEUR`). GO de forme valide
pour les cas sains : `GO-2026-11-02-31` (présent au registre ; la course n'atteint jamais un appel) ; `PLAFOND_USD=34`.

| N° | Lanceur | Cas | Attendu | Obtenu | Copie |
|---|---|---|---|---|---|
| 1 | principal | sain, port 8805 libre à cet instant (le service Argon de la course Kirchner, PID 973, venait de finir) | toutes les gardes de structure passent, arrêt à la présence des clés | code 2, « RR_ANTHROPIC_API_KEY_LUC absente » | inchangée |
| 2 | principal | sain, copie d'essai où la garde Argon vise 18805 | idem | code 2, « RR_ANTHROPIC_API_KEY_LUC absente » | inchangée |
| 3 | principal | sans `GO_ID` | refus | code 1, « GO_ID absent » | inchangée |
| 4 | principal | GO absent du registre (`GO-2099-01-01-99`) | refus | code 2, « absent de registres/go.md » | inchangée |
| 5 | principal | `run-kirchner-q2-e3-v1` déjà présent | refus (R12) | code 2 | inchangée |
| 6 | principal | `controle-kirchner-q2-v1.json` déjà présent | refus (R12) | code 2 | inchangée |
| 7 | principal | empreinte non conforme (un octet ajouté à `faits.md`) | refus | code 2, « empreintes non conformes » | inchangée hors l'octet planté |
| 8 | principal | sans `PY_COLLISIONNEUR` | refus | code 1, « PY_COLLISIONNEUR absent » | inchangée |
| 9 | principal | `PY_COLLISIONNEUR` sans `anthropic` (`/usr/bin/python3`) | refus | code 2 | inchangée |
| 10 | principal | sans `PLAFOND_USD` | refus | code 1 | inchangée |
| 11 | principal | port 8812 pris (écouteur local), clés factices `FACTICE-ESSAI`, copie 18805 | refus avant le relais | code 2, « port 8812 déjà pris » | inchangée |
| 12 | sans Argon | sain | arrêt à la présence des clés | code 2, « RR_ANTHROPIC_API_KEY_LUC absente » | inchangée |
| 13 | sans Argon | sans `GO_ID` | refus | code 1 | inchangée |
| 14 | sans Argon | GO absent | refus | code 2 | inchangée |
| 15 | sans Argon | `run-kirchner-q2-e3-sans-argon-v1` déjà présent | refus (R12) | code 2 | inchangée |
| 16 | sans Argon | empreinte non conforme (`appel_controle_v12.py`) | refus | code 2 | inchangée hors l'octet planté |
| 17 | sans Argon | sans `PY_COLLISIONNEUR` | refus | code 1 | inchangée |
| 18 | sans Argon | port 8812 pris, clés factices | refus | code 2, « port 8812 déjà pris » | inchangée |
| 19 | principal | Argon en usage simulé (copie d'essai : garde sur 18805, écouteur local sur 18805) | refus | code 2, « … Argon en usage … variante sans Argon » | inchangée |
| 20 | `appel_controle_v12.py` | lettres vides, `ABDEX`, `AA`, `C9`, sans argument | refus, aucune sortie | code 2, aucun fichier créé | — |
| 21 | `appel_controle_v12.py` | lettres `ABDE` sur un collisionneur factice (vrai code du v9, appelants remplacés, aucun réseau) | seuls A, B, D, E appelés | code 0 ; appelés : `claude-fable-5-1`, `claude-opus-5-5`, `kimi-k3.1-pro`, `gpt-6-astra` | — |
| 22 | `assembler_faits_kirchner_v1.py` | une pièce altérée d'un octet | refus, rien d'écrit | code 1, « empreinte … au lieu de d6fa8011… ; rien n'est écrit » | — |

Écouteurs d'essai arrêtés par leur PID (R10). Garde du plafond du collisionneur : course à blanc à 5 USD, arrêt code 4 avant
l'appel qui l'aurait franchi (`course-a-blanc-kirchner-q2-v1.txt`).

Non éprouvé ici : tout ce qui suit la présence des clés (relais Kimi réel, contrôle préalable, appel de contrôle réel, tour réel,
recherche finale des clés) ; la valeur factice de `GEMINI_API_KEY` dans la variante sans Argon (aucun appelant C n'est atteint :
cellules C en absence acceptée, contrôle restreint à ABDE, cas 21 et course à blanc sans Argon).
