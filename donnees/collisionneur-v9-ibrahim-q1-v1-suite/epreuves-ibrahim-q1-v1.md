# Épreuves sans appel des lanceurs du tour sur la question 1 de Lujain Ibrahim (collisionneur v9) — v1

Session développeur de session-depot, 3 novembre 2026, écrit à 11:37 UTC (heure relevée par `date -u`). Aucune clé dans l'environnement
des épreuves (`env -i`, mandataire mort `HTTPS_PROXY=http://127.0.0.1:9`) ; aucun appel réseau ; chaque cas joue une copie neuve du
dossier hors du dépôt, comparée fichier par fichier avant et après (après la préparation du cas). Lanceurs : sans Argon
`lancer-tour-ibrahim-q1-v9-sans-argon-v1.sh` (6293da64…, celui du lancement) et cinq espèces `lancer-tour-ibrahim-q1-v9-v1.sh` (fb662523…). GO de forme valide
pour les cas sains : `GO-2026-11-02-31` (présent au registre ; aucun cas n'atteint un appel). Écouteurs d'essai arrêtés par leur PID
(R10). Les cas « cinq espèces » visent la garde Argon sur 18805 dans leur copie (le port 8805 réel n'est pas touché). Les deux
derniers cas jouent la commande du LISEZMOI telle quelle (variante sans Argon), sur une copie.

| N° | Cas | Code | Dernière ligne | Copie |
|---|---|---|---|---|
| 1 | sans Argon, sain | code 2 | RR_ANTHROPIC_API_KEY_LUC absente | inchangée |
| 2 | sans Argon, sans GO_ID | code 1 | lancer-tour-ibrahim-q1-v9-sans-argon-v1.sh: GO_ID: GO_ID absent : un GO de registres/go.md avec le mot direct  | inchangée |
| 3 | sans Argon, GO absent du registre | code 2 | GO-2099-01-01-99 absent de registres/go.md | inchangée |
| 4 | sans Argon, run déjà présent | code 2 | run-ibrahim-q1-e3-sans-argon-v1 existe déjà (R12) | inchangée |
| 5 | sans Argon, contrôle déjà présent | code 2 | controle-ibrahim-q1-sans-argon-v1.json existe déjà (R12) | inchangée |
| 6 | sans Argon, un octet ajouté à faits.md | code 2 | empreintes non conformes | inchangée |
| 7 | sans Argon, un octet ajouté à appel_controle_v12.py | code 2 | empreintes non conformes | inchangée |
| 8 | sans Argon, sans PY_COLLISIONNEUR | code 1 | lancer-tour-ibrahim-q1-v9-sans-argon-v1.sh: PY_COLLISIONNEUR: PY_COLLISIONNEUR absent : le Python du collision | inchangée |
| 9 | sans Argon, PY_COLLISIONNEUR sans anthropic | code 2 | python du collisionneur absent ou sans anthropic | inchangée |
| 10 | sans Argon, sans PLAFOND_USD | code 1 | lancer-tour-ibrahim-q1-v9-sans-argon-v1.sh: PLAFOND_USD: PLAFOND_USD absent : le plafond de la ligne de GO est | inchangée |
| 11 | sans Argon, port 8814 pris (écouteur local), clés factices | code 2 | port 8814 déjà pris | inchangée |
| 12 | cinq espèces, sain (garde Argon visée sur 18805) | code 2 | RR_ANTHROPIC_API_KEY_LUC absente | inchangée |
| 13 | cinq espèces, sans GO_ID | code 1 | lancer-tour-ibrahim-q1-v9-v1.sh: GO_ID: GO_ID absent : un GO de registres/go.md avec le mot direct de Lazar es | inchangée |
| 14 | cinq espèces, run déjà présent | code 2 | run-ibrahim-q1-e3-v1 existe déjà (R12) | inchangée |
| 15 | cinq espèces, un octet ajouté à appel_controle_v10.py | code 2 | empreintes non conformes | inchangée |
| 16 | cinq espèces, Argon en usage simulé (garde et écouteur sur 18805) | code 2 | port 18805 ouvert : Argon en usage (relais Argon) ; jamais deux usages d'Argon à la fois : attendre, ou varia | inchangée |
| 17 | cinq espèces, port 8814 pris, clés factices (garde Argon sur 18805) | code 2 | port 8814 déjà pris | inchangée |
| 18 | commande du LISEZMOI, libre | code 0 | lanceur détaché, PID 4475 ; code du lanceur : 2 ; journal : RR_ANTHROPIC_API_KEY_LUC absente  | — |
| 19 | commande du LISEZMOI, journal-present | code 2 | journal-ibrahim-q1-v9-sans-argon-v1.log existe (R12) : rien n'est lancé ; code du lanceur : aucun ; journal : ancien  | — |

Plafond du collisionneur : course à blanc sans Argon à 5 USD, arrêt en code 4 avant l'appel qui l'aurait franchi
(`course-a-blanc-ibrahim-q1-v1.txt`). Extracteur et assembleur : refus sur empreinte non conforme, même code qu'aux tours Kirchner et
conception (éprouvé là). Non éprouvé : tout ce qui suit la présence des clés ; la valeur factice de `GEMINI_API_KEY`.
