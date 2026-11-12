# Journal du poste local — D-1a (GO-2026-11-10-13)

- Essai à blanc : PID 4368 vivant après fin et reprise de la session (hôte relancé), arrêté par PID ; mandataires vides.
- L1 : 2026-11-11T23:35:28Z (date -u)
- T_LIM = 2026-11-12T05:35:28Z (L1 + 6 h)
- H = 2026-11-13T21:35:28Z (T_LIM + 40 h)
- L1 preparer : code 0, rattrapage-machine-d1a-7b833a333f09-v1.json, étiquette 7b833a333f09436c9b2164930cebcc14 ; tâches mère 2026-11-13T21:35:28Z, 2026-11-13T22:05:28Z, 2026-11-14T21:35:28Z.
- L2 2026-11-11T23:35:45Z acces-creer : code 0 ; clé 132500120 (5d:dc:6f:43:c1:d1:eb:8a:9c:5b:d5:87:29:e6:a0:b7), pare-feu 12031843.
- L3 2026-11-11T23:36:14Z : garde-poste conforme ; commit 2c08ce037d0b42fc471c391b046544ec0d648df0 poussé sur donnees/lean-outillage-d1a-poste-local-v1 ; rattrapage 9a2f4d3c…7666, accès fb36d954…ffbe.
- Écarts : verifier-arbre non lancé (bras-attaque extrait, règle 9) ; jeton de gh passé au seul git (clone, fetch, push) ; commandes réseau hors bac à sable ; HCLOUD_TOKEN passé par processus pendant l'essai à blanc puis natif après relance de l'hôte.
- Mot « armée » reçu 2026-11-11T23:40:37Z (date -u) ; empreinte 9a2f4d3c68d5b47a72278bbe56602f7ac757859ba96ecf61d0be10708fa27666 ; T1 trig_013NADgikL46HVvA5XCJUYmy, T2 trig_01BiwNZWFLwsbprdpdbvQxbb, T3 trig_011VxYMdD2YSFpYqmWVUZY2G.
etiquette=v4.35.0 commit=56a005855ea17e0b0958f73ec801ae140b0a1679
- L5 2026-11-11T23:41:23Z : PID 4980 terminé 23:41:40Z, ARRÊT code 1 avant tout appel (rattrapage « non poussé » : branche sans amont, clone --single-branch). Section 4.
- 2026-11-11T23:45:30Z : accord direct de Lazar pour une seconde et dernière L5 (mots : « oui », puis « Mon accord » à la question « accord de la mère ou le tien en tant que directeur ? ») ; non donné par la mère, à lui signaler.
- S4.3 2026-11-11T23:57:20Z : detruire --pas d1a et inventaire, aucun serveur de l'essai (code 0).
- L4bis 2026-11-11T23:58:41Z : amont réparé (fetch refspec), inventaire vide. Seconde L5 :
- L5bis 2026-11-11T23:58:41Z : serveur 175751342 créé 23:58:44Z, échéance 2026-11-13T20:35:28Z, minuterie PID 1117. L6 23:59:09Z conforme.
pilote avant lancé 2026-11-12T00:00:01Z
- 2026-11-12T00:00:01Z pilote avant n°1 : échec à la première copie (SSH : délai dépassé) ; rien installé. Cause : l'IP_POSTE donnée diffère de l'adresse de sortie réelle du poste (comparées sans affichage).
- 2026-11-12T00:06:01Z : ÉCART (accord de Lazar, « Reposer les règles ») — règles d'installation reposées sur le pare-feu 12031843 par regles_installation() du harnais, avec l'adresse de sortie mesurée deux fois (ifconfig.me, ipify) et jamais affichée ; nom du pare-feu relu avant ; port 22 ouvert ensuite. Cette adresse sert d'IP_POSTE pour la suite (acces-couper, garde-poste, avec aussi l'ancienne).
- pilote avant n°2 lancé 2026-11-12T00:06:18Z
- pilote avant n°2 : « Host key verification failed » (aucun ~/.ssh dans WSL, accept-new ne peut écrire) ; ~/.ssh créé.
- pilote avant n°3 lancé 2026-11-12T00:07:26Z
- pilote avant n°3 : même échec ; cause : scp (C) du pilote sans StrictHostKeyChecking=accept-new, lancé avant tout ssh. Clé d'hôte enregistrée par un ssh « true » (accept-new), pilote inchangé :
- pilote avant n°4 lancé 2026-11-12T00:09:11Z
- pilote avant n°4 : échec (connexions intermittentes). Mesures : le poste sort par 2 adresses IPv4 distinctes, dont l'IP_POSTE donnée, toutes dans son /24 ; port 22 joignable ≈ 1 fois sur 8.
- 2026-11-12T00:13:54Z : ÉCART (accord de Lazar, « Ouvrir au /24 ») — règles d'installation du harnais (regles_installation) posées sur 12031843 avec la source élargie au /24 de l'IP_POSTE ; nom du pare-feu relu ; port 22 : 9/10 puis 30/30. La coupure se fera de même (regles_coupure, source SSH élargie au /24, règle sortante inchangée).
  - clé d hôte du serveur : SHA256:nkbJqH5/NKzYgXLkaCG6n5GFSzJv/BqX1mBf2PeHATI (ED25519)
- pilote avant n°5 lancé 2026-11-12T00:14:40Z
- 2026-11-12T00:17:19Z pilote avant n°5 terminé, conforme (réseau ouvert attendu, aucun écart).
- 2026-11-12T00:17:37Z coupure posée (regles_coupure du harnais, source SSH /24).
- verifier-coupure 2026-11-12T00:17Z : code 0, pare-feu applied, seule règle sortante ICMP leurre.
- pilote apres lancé 2026-11-12T00:18:08Z
- pilote apres n°1 (00:18:08Z) : code 1 à la sonde après coupure, seul écart « résolveur système (example.com) : ouverte ». Diagnostic en lecture seule 00:19:47Z : example.com et deux noms neufs non résolus, cache de systemd-resolved vide (43 succès de cache comptés) : réponse mise en cache avant la coupure, pas une fuite. ÉCART : pilote apres relancé (coupure idempotente, flush ruleset), sorties dans un dossier neuf.
- pilote apres n°2 lancé 2026-11-12T00:20:49Z
- pilote apres n°2 (00:20:49Z) : sonde après coupure conforme (aucun écart) ; vérificateur épinglé (sha256 1f744a4d…fe28) ; NOYAU NON CONFORME (conforme: false, 18 cas) : G-L1 « Permission denied » sur /opt/mathlib/.lake/build/lib/lean/Mathlib.olean. Diagnostic lecture seule 00:23:50Z : .olean en -rw------- chaine:chaine ; bac traverse les dossiers mais ne lit pas les .olean (défaut de installer_chaine_v1.sh : chown sans droit de lecture). Rien d'autre lancé (consigne). Section 5.
- S5 00:24:07Z detruire 175751342 code 0 ; 00:24:09Z inventaire vide ; 00:24:10Z acces-supprimer code 1 (422 resource_in_use : pare-feu encore attaché pendant la suppression asynchrone) ; 00:24:11Z minuterie conforme puis arrêtée par PID 1117.
- S5.3 bis 00:26:45Z acces-supprimer code 0 (pare-feu et clé supprimés) ; inventaire 00:26:47Z vide.
