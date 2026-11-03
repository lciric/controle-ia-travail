# Épreuves sans appel des lanceurs du tour sur la conception de l'organisme (collisionneur v9) — v1

Session développeur de session-depot, 3 novembre 2026, écrit à 11:14 UTC (heure relevée par `date -u`). Aucune clé dans
l'environnement des épreuves (`env -i`, mandataire mort `HTTPS_PROXY=http://127.0.0.1:9`) ; aucun appel réseau ; chaque cas joue
une copie neuve du dossier, hors du dépôt, comparée fichier par fichier avant et après (empreintes). Mêmes cas que pour Kirchner Q2
(`epreuves-kirchner-q2-v1.md`, branche 16ec2e5a). Lanceurs éprouvés : `lancer-tour-conception-organisme-v9-v1.sh` (c33646a1…) et
`lancer-tour-conception-organisme-v9-sans-argon-v1.sh` (14cf8946…). GO de forme valide pour les cas sains : `GO-2026-11-02-31`
(présent au registre ; aucun cas n'atteint un appel) ; `PLAFOND_USD=37`. Ports 8805 et 8812 libres sur cette machine à 11:12 UTC.

| N° | Lanceur | Cas | Obtenu | Copie |
|---|---|---|---|---|
| 1 | principal | sain (8805 libre) | code 2, « RR_ANTHROPIC_API_KEY_LUC absente » (toutes les gardes de structure passées) | inchangée |
| 2 | principal | sain, copie d'essai où la garde Argon vise 18805 | code 2, « RR_ANTHROPIC_API_KEY_LUC absente » | inchangée |
| 3 | principal | sans `GO_ID` | code 1 | inchangée |
| 4 | principal | GO absent du registre | code 2 | inchangée |
| 5 | principal | `run-conception-organisme-e3-v1` déjà présent | code 2 (R12) | inchangée |
| 6 | principal | `controle-conception-organisme-v1.json` déjà présent | code 2 (R12) | inchangée |
| 7 | principal | un octet ajouté à `faits.md` | code 2, « empreintes non conformes » | inchangée hors l'octet planté |
| 8 | principal | sans `PY_COLLISIONNEUR` | code 1 | inchangée |
| 9 | principal | `PY_COLLISIONNEUR` sans `anthropic` | code 2 | inchangée |
| 10 | principal | sans `PLAFOND_USD` | code 1 | inchangée |
| 11 | principal | port 8812 pris (écouteur local), clés factices, copie 18805 | code 2, « port 8812 déjà pris » | inchangée |
| 12 | sans Argon | sain | code 2, « RR_ANTHROPIC_API_KEY_LUC absente » | inchangée |
| 13 | sans Argon | sans `GO_ID` | code 1 | inchangée |
| 14 | sans Argon | GO absent | code 2 | inchangée |
| 15 | sans Argon | `run-conception-organisme-e3-sans-argon-v1` déjà présent | code 2 (R12) | inchangée |
| 16 | sans Argon | un octet ajouté à `appel_controle_v12.py` | code 2 | inchangée hors l'octet planté |
| 17 | sans Argon | sans `PY_COLLISIONNEUR` | code 1 | inchangée |
| 18 | sans Argon | port 8812 pris, clés factices | code 2, « port 8812 déjà pris » | inchangée |
| 19 | principal | Argon en usage simulé (garde sur 18805, écouteur sur 18805) | code 2, « … Argon en usage … variante sans Argon » | inchangée |
| 20 | commande du LISEZMOI | fichiers de lancement absents | garde R12 au premier plan passée, lanceur détaché (PID écrit après), lanceur arrêté en code 2 à « clé absente », `code-…txt` = 2 ; attente : rend « code : 2 » | — |
| 21 | commande du LISEZMOI | `journal-conception-organisme-v9-v1.log` déjà présent | code 2, « existe (R12) : rien n'est lancé » ; ni PID ni code écrits | — |
| 22 | `assembler_faits_conception_organisme_v1.py` | une pièce altérée d'un octet | code 1, rien d'écrit | — |
| 23 | `extraire_question_conception_organisme_v1.py` | source altérée d'un octet | code 1, rien d'écrit | — |

Écouteurs d'essai arrêtés par leur PID (R10). Plafond du collisionneur : course à blanc à 5 USD, arrêt code 4 avant l'appel qui
l'aurait franchi (`course-a-blanc-conception-organisme-v1.txt`). Une première passe a laissé l'écouteur 18805 ouvert pendant tous
les cas, ce qui a fait refuser les cas 2 et 11 par la garde Argon (refus juste, cas mal monté) ; les cas ont été rejoués, résultats
ci-dessus. Contrôle `appel_controle_v12.py` : même fichier qu'à 16ec2e5a (f51ebd29…), éprouvé là (lettres refusées, ABDE).

Non éprouvé : tout ce qui suit la présence des clés (relais Kimi réel, contrôle réel, tour réel, recherche finale des clés) ; la
valeur factice de `GEMINI_API_KEY` de la variante sans Argon (jamais atteinte).
