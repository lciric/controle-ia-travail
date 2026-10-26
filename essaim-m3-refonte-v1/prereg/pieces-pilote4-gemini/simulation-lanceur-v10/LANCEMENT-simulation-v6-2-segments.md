# Lancement du pilote pilote4-gemini-v6-2-v1 (simulation, tentative 1)

- début (UTC) : 2026-10-26T00:02:54Z ; hôte : vm ; utilisateur : 0
- course : v6-2 ; dossier du pilote : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/pilote4-gemini-v6-2-v1 (0700, à root)
- dépôt : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot ; HEAD : da3ca3382b25c1e61a4cdcc1f8051d33ab056b77 (c'est le « commit » que le manifeste consignera)
- lanceur : lancer_pilote4_gemini_v10.sh, sha256 0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952
- source des registres : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/go-sain.md ; dépenses : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/dep-sain.md
- aucune course voisine du noyau dans ce conteneur au départ (détection par pgrep)
- course M de référence : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/m-reference/pilote2-gemini-v5-2-1-maieutique-v1 ; M saine : g000 et g001 OK, au plus 20 % d appels hors OK et au moins un appel OK de Fable à chacune (g000 {"OK": 123}; g001 {"OK": 129}), fin « générations maximales », arrêt « aucune lignée active », code 0, archive fermée ; graine de M 3970427751169333427 ; dépense du noyau 2.9344 USD ; refus du noyau par génération [[], []] ; empreintes de M vérifiées (EMPREINTES-pilote-v1.txt, sha256 d0185263641e21f8d3be97f2fa704cc79dbfb37c3e2e48e916a1abb854b3cf6d) ; graine 3970427751169333427 = graine M du texte scellé du second pilote (d2944654…)
- code : identique à 8e5e2f7b (commit et arbre de travail : essaim_m3, tests, collisionneur) ; commits postérieurs limités aux pièces du pilote ; rien de non suivi hors des dossiers de pilotes ; 4967734 et 90595ffb ancêtres ; banque 157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d ; mission bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e ; collisionneur 213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd
- versions : python 3.13.17 ; numpy 2.4.6 ; anthropic absente
- isolation : dossier du pilote 0700 à root ; espace attendu /var/lib/essaim-m3/fe89ce9ef772e504 ; dépôt /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot caché aux organismes (vérifié par bac_a_sable.dossiers_a_cacher) ; ESSAIM_M3_ESPACE non définie
- préenregistrement : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/prereg-sain.md, sha256 f21fade08c6800c73034d4cabb28bd25c70a92d398f13509876fc2d4e5543362 (compagnon conforme), graine 1541481317522987174 de la course v6-2 écrite et recalculée depuis l'entropie du texte, empreinte du lanceur citée
- organisme : 26 fichiers, empreinte d'arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d ; question (v6-2) : sha256 8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd
- registre : une ligne GO-2026-10-25-02 de type calcul portant l'empreinte de la question (v6-2), celle de l'organisme (4f13647a…) et celle du texte scellé (f21fade08c6800c7) ; dépense consignée avant ; reste déclaré 150 USD ≥ 75 (vérification du lanceur)
- test de dépense : td-seg-1.json, sha256 5c97cccd1c3e71403e4d6dfbf21da5c32c3aca5b37eb5d24cacf791ba149c245 — trois espèces OK, modèles servis conformes, coûts CLAUDE_FABLE_5_1 0.00058, CLAUDE_OPUS_5_5 0.000232, GEMINI_ARGON 0.00076 USD, âge 1 s ; noms des variables du test : absents de la pièce (réserve, P52C1-05) (réalité des appels attestée par l'outil de session-depot ; le script vérifie la pièce)
- recharge automatique attestée : « essai »
- ESSAI : rapport JUnit repris de /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/junit-sain-v1.xml (simulation)
- essais : 169 passés, 0 sauté, 0 désélectionnés ; arguments : « aucun » ; les 45 essais cités ont passé ici (dont la recherche réelle sur arXiv)
- noyau sans bytecode : empreinte 61ddd638d7a3b5519a7294fc04a75003e3d21da72b9cfdcf4dd07dc0341565a0 (la fonction écarte le bytecode depuis le constat n° 30 § 5)
- test de dépense revérifié au départ : trois espèces OK, modèles servis conformes, coûts CLAUDE_FABLE_5_1 0.00058, CLAUDE_OPUS_5_5 0.000232, GEMINI_ARGON 0.00076 USD, âge 1 s ; noms des variables du test : absents de la pièce (réserve, P52C1-05)
- voisines au départ : aucune
- RÉSERVE : des essais (pytest) tournent dans le conteneur au départ (PID 21948 21949 21951 ) : ceux du noyau font tourner des processus sous l'utilisateur 60900 de ce pilote
- environnement du noyau (noms seulement, valeurs jamais écrites) : PATH HOME LANG PYTHONDONTWRITEBYTECODE ESSAIM_M3_CACHER .
- marqueur de départ : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/.partis/pilote4-gemini-v6-2-v1 (R3 ; jamais retiré)
- départ de la simulation (UTC) : 2026-10-26T00:02:55Z
- PID de la course : 22436 (arrêt humain par ce PID seulement, R10 ; STOP dans course/ : arrêt avant la ronde ou la génération suivante, celle en cours finit)
- minuteur : PID 22437 ; échéance 2026-10-26T00:02:54Z, 0 s après le départ du lanceur (2026-10-26T00:02:54Z)
- minuteur : STOP posé dans course/ à 2026-10-26T00:02:56Z (0 s après le départ du lanceur) : la course s'arrête avant la ronde ou la génération suivante ; état de reprise attendu
- minuteur : STOP présent dans course/ à la fin du processus (fin de segment si le noyau a écrit un état de reprise ; sinon la course a fini sur sa dernière unité)
- fin du processus (UTC) : 2026-10-26T00:02:58Z ; code de retour : 0 ; sortie standard fermée (non lue) ; sortie d'erreur : sortie-erreur-lanceur.txt (lisible)
- état de reprise écrit par le noyau : etat-v1.json dddd508538856ad7474e829bf7fe49314b77e0c8608ed2a595216f6641a9f0a1 0.0947 74.9053
- segment 1 arrêté par STOP ; reprise attendue : SEGMENT=2
- fin du lanceur (UTC) : 2026-10-26T00:02:58Z

## Segment 2, essai 1 (simulation, tentative 1)

- début (UTC) : 2026-10-26T00:02:58Z ; hôte : vm ; utilisateur : 0
- course : v6-2 ; dossier du pilote : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/pilote4-gemini-v6-2-v1 (0700, à root) ; pièces de ce segment : segment-2-t1/
- dépôt : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot ; HEAD : da3ca3382b25c1e61a4cdcc1f8051d33ab056b77 (celui du segment 1, que le manifeste consigne)
- lanceur : lancer_pilote4_gemini_v10.sh, sha256 0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952
- source des registres : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/go-sain.md ; dépenses : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/dep-sain.md
- aucune course voisine du noyau dans ce conteneur au départ (détection par pgrep)
- état de reprise : etat-v1.json, sha256 dddd508538856ad7474e829bf7fe49314b77e0c8608ed2a595216f6641a9f0a1 (compagnon conforme), arrêt sur STOP du segment 1 ; dépense de la course jusqu'ici 0.0947 USD ; reste au plus 74.9053 USD pour la course (plafond 75 USD)
- course M de référence : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/m-reference/pilote2-gemini-v5-2-1-maieutique-v1 ; M saine : g000 et g001 OK, au plus 20 % d appels hors OK et au moins un appel OK de Fable à chacune (g000 {"OK": 123}; g001 {"OK": 129}), fin « générations maximales », arrêt « aucune lignée active », code 0, archive fermée ; graine de M 3970427751169333427 ; dépense du noyau 2.9344 USD ; refus du noyau par génération [[], []] ; empreintes de M vérifiées (EMPREINTES-pilote-v1.txt, sha256 d0185263641e21f8d3be97f2fa704cc79dbfb37c3e2e48e916a1abb854b3cf6d) ; graine 3970427751169333427 = graine M du texte scellé du second pilote (d2944654…)
- code : identique à 8e5e2f7b (commit et arbre de travail : essaim_m3, tests, collisionneur) ; commits postérieurs limités aux pièces du pilote ; rien de non suivi hors des dossiers de pilotes ; 4967734 et 90595ffb ancêtres ; banque 157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d ; mission bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e ; collisionneur 213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd
- versions : python 3.13.17 ; numpy 2.4.6 ; anthropic absente
- isolation : dossier du pilote 0700 à root ; espace attendu /var/lib/essaim-m3/fe89ce9ef772e504 ; dépôt /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot caché aux organismes (vérifié par bac_a_sable.dossiers_a_cacher) ; ESSAIM_M3_ESPACE non définie
- préenregistrement : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/prereg-sain.md, sha256 f21fade08c6800c73034d4cabb28bd25c70a92d398f13509876fc2d4e5543362 (compagnon conforme), graine 1541481317522987174 de la course v6-2 écrite et recalculée depuis l'entropie du texte, empreinte du lanceur citée
- organisme : 26 fichiers, empreinte d'arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d ; question (v6-2) : sha256 8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd
- refus : segment 2 non consigné avant dans registres/depenses.md (une ligne nommant pilote4-gemini-v6-2-v1, GO-2026-10-25-02 et « segment 2 ») (2026-10-26T00:02:59Z) ; verrou /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/.verrou-pilote4-gemini-v6-2-v1-segment2 retiré

## Segment 2, essai 2 (simulation, tentative 1)

- début (UTC) : 2026-10-26T00:02:59Z ; hôte : vm ; utilisateur : 0
- course : v6-2 ; dossier du pilote : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/pilote4-gemini-v6-2-v1 (0700, à root) ; pièces de ce segment : segment-2-t2/
- dépôt : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot ; HEAD : da3ca3382b25c1e61a4cdcc1f8051d33ab056b77 (celui du segment 1, que le manifeste consigne)
- lanceur : lancer_pilote4_gemini_v10.sh, sha256 0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952
- source des registres : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/go-sain.md ; dépenses : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/dep-segments.md
- aucune course voisine du noyau dans ce conteneur au départ (détection par pgrep)
- état de reprise : etat-v1.json, sha256 dddd508538856ad7474e829bf7fe49314b77e0c8608ed2a595216f6641a9f0a1 (compagnon conforme), arrêt sur STOP du segment 1 ; dépense de la course jusqu'ici 0.0947 USD ; reste au plus 74.9053 USD pour la course (plafond 75 USD)
- course M de référence : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/m-reference/pilote2-gemini-v5-2-1-maieutique-v1 ; M saine : g000 et g001 OK, au plus 20 % d appels hors OK et au moins un appel OK de Fable à chacune (g000 {"OK": 123}; g001 {"OK": 129}), fin « générations maximales », arrêt « aucune lignée active », code 0, archive fermée ; graine de M 3970427751169333427 ; dépense du noyau 2.9344 USD ; refus du noyau par génération [[], []] ; empreintes de M vérifiées (EMPREINTES-pilote-v1.txt, sha256 d0185263641e21f8d3be97f2fa704cc79dbfb37c3e2e48e916a1abb854b3cf6d) ; graine 3970427751169333427 = graine M du texte scellé du second pilote (d2944654…)
- code : identique à 8e5e2f7b (commit et arbre de travail : essaim_m3, tests, collisionneur) ; commits postérieurs limités aux pièces du pilote ; rien de non suivi hors des dossiers de pilotes ; 4967734 et 90595ffb ancêtres ; banque 157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d ; mission bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e ; collisionneur 213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd
- versions : python 3.13.17 ; numpy 2.4.6 ; anthropic absente
- isolation : dossier du pilote 0700 à root ; espace attendu /var/lib/essaim-m3/fe89ce9ef772e504 ; dépôt /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot caché aux organismes (vérifié par bac_a_sable.dossiers_a_cacher) ; ESSAIM_M3_ESPACE non définie
- préenregistrement : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/prereg-sain.md, sha256 f21fade08c6800c73034d4cabb28bd25c70a92d398f13509876fc2d4e5543362 (compagnon conforme), graine 1541481317522987174 de la course v6-2 écrite et recalculée depuis l'entropie du texte, empreinte du lanceur citée
- organisme : 26 fichiers, empreinte d'arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d ; question (v6-2) : sha256 8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd
- refus : reste sur GO-2026-10-25-02 = 0.01 USD < 74.9053 (2026-10-26T00:02:59Z) ; verrou /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/.verrou-pilote4-gemini-v6-2-v1-segment2 retiré

## Segment 2, essai 3 (simulation, tentative 1)

- début (UTC) : 2026-10-26T00:03:00Z ; hôte : vm ; utilisateur : 0
- course : v6-2 ; dossier du pilote : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/pilote4-gemini-v6-2-v1 (0700, à root) ; pièces de ce segment : segment-2-t3/
- dépôt : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot ; HEAD : da3ca3382b25c1e61a4cdcc1f8051d33ab056b77 (celui du segment 1, que le manifeste consigne)
- lanceur : lancer_pilote4_gemini_v10.sh, sha256 0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952
- source des registres : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/go-sain.md ; dépenses : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/dep-segments.md
- aucune course voisine du noyau dans ce conteneur au départ (détection par pgrep)
- refus : SEGMENT=2 : état de reprise du segment 1 non conforme (etat-v1.json : compagnon absent ou différent) (2026-10-26T00:03:00Z) ; verrou /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/.verrou-pilote4-gemini-v6-2-v1-segment2 retiré

## Segment 2, essai 4 (simulation, tentative 1)

- début (UTC) : 2026-10-26T00:03:00Z ; hôte : vm ; utilisateur : 0
- course : v6-2 ; dossier du pilote : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/pilote4-gemini-v6-2-v1 (0700, à root) ; pièces de ce segment : segment-2-t4/
- dépôt : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot ; HEAD : da3ca3382b25c1e61a4cdcc1f8051d33ab056b77 (celui du segment 1, que le manifeste consigne)
- lanceur : lancer_pilote4_gemini_v10.sh, sha256 0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952
- source des registres : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/go-sain.md ; dépenses : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/dep-segments.md
- aucune course voisine du noyau dans ce conteneur au départ (détection par pgrep)
- refus : SEGMENT=2 : état de reprise du segment 1 non conforme (etat-v1.json : arrêt autre que STOP ('aucune lignée active')) (2026-10-26T00:03:00Z) ; verrou /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/.verrou-pilote4-gemini-v6-2-v1-segment2 retiré

## Segment 2, essai 5 (simulation, tentative 1)

- début (UTC) : 2026-10-26T00:03:00Z ; hôte : vm ; utilisateur : 0
- course : v6-2 ; dossier du pilote : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/pilote4-gemini-v6-2-v1 (0700, à root) ; pièces de ce segment : segment-2-t5/
- dépôt : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot ; HEAD : da3ca3382b25c1e61a4cdcc1f8051d33ab056b77 (celui du segment 1, que le manifeste consigne)
- lanceur : lancer_pilote4_gemini_v10.sh, sha256 0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952
- source des registres : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/go-sain.md ; dépenses : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/dep-segments.md
- aucune course voisine du noyau dans ce conteneur au départ (détection par pgrep)
- refus : SEGMENT=2 : état de reprise du segment 1 non conforme (etat-v1.json : état du segment 5, attendu 1) (2026-10-26T00:03:00Z) ; verrou /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/.verrou-pilote4-gemini-v6-2-v1-segment2 retiré

## Segment 2, essai 6 (simulation, tentative 1)

- début (UTC) : 2026-10-26T00:03:00Z ; hôte : vm ; utilisateur : 0
- course : v6-2 ; dossier du pilote : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/pilote4-gemini-v6-2-v1 (0700, à root) ; pièces de ce segment : segment-2-t6/
- dépôt : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot ; HEAD : da3ca3382b25c1e61a4cdcc1f8051d33ab056b77 (celui du segment 1, que le manifeste consigne)
- lanceur : lancer_pilote4_gemini_v10.sh, sha256 0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952
- source des registres : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/go-sain.md ; dépenses : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/dep-segments.md
- aucune course voisine du noyau dans ce conteneur au départ (détection par pgrep)
- ESSAI : artefact « organisme » (simulation)
- état de reprise : etat-v1.json, sha256 dddd508538856ad7474e829bf7fe49314b77e0c8608ed2a595216f6641a9f0a1 (compagnon conforme), arrêt sur STOP du segment 1 ; dépense de la course jusqu'ici 0.0947 USD ; reste au plus 74.9053 USD pour la course (plafond 75 USD)
- course M de référence : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/m-reference/pilote2-gemini-v5-2-1-maieutique-v1 ; M saine : g000 et g001 OK, au plus 20 % d appels hors OK et au moins un appel OK de Fable à chacune (g000 {"OK": 123}; g001 {"OK": 129}), fin « générations maximales », arrêt « aucune lignée active », code 0, archive fermée ; graine de M 3970427751169333427 ; dépense du noyau 2.9344 USD ; refus du noyau par génération [[], []] ; empreintes de M vérifiées (EMPREINTES-pilote-v1.txt, sha256 d0185263641e21f8d3be97f2fa704cc79dbfb37c3e2e48e916a1abb854b3cf6d) ; graine 3970427751169333427 = graine M du texte scellé du second pilote (d2944654…)
- code : identique à 8e5e2f7b (commit et arbre de travail : essaim_m3, tests, collisionneur) ; commits postérieurs limités aux pièces du pilote ; rien de non suivi hors des dossiers de pilotes ; 4967734 et 90595ffb ancêtres ; banque 157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d ; mission bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e ; collisionneur 213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd
- versions : python 3.13.17 ; numpy 2.4.6 ; anthropic absente
- isolation : dossier du pilote 0700 à root ; espace attendu /var/lib/essaim-m3/fe89ce9ef772e504 ; dépôt /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot caché aux organismes (vérifié par bac_a_sable.dossiers_a_cacher) ; ESSAIM_M3_ESPACE non définie
- préenregistrement : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/prereg-sain.md, sha256 f21fade08c6800c73034d4cabb28bd25c70a92d398f13509876fc2d4e5543362 (compagnon conforme), graine 1541481317522987174 de la course v6-2 écrite et recalculée depuis l'entropie du texte, empreinte du lanceur citée
- refus : empreinte d'arbre de l'organisme ≠ 4f13647a… (2026-10-26T00:03:01Z) ; verrou /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/.verrou-pilote4-gemini-v6-2-v1-segment2 retiré

## Segment 2, essai 7 (simulation, tentative 1)

- début (UTC) : 2026-10-26T00:03:01Z ; hôte : vm ; utilisateur : 0
- course : v6-2 ; dossier du pilote : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/pilote4-gemini-v6-2-v1 (0700, à root) ; pièces de ce segment : segment-2-t7/
- dépôt : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot ; HEAD : da3ca3382b25c1e61a4cdcc1f8051d33ab056b77 (celui du segment 1, que le manifeste consigne)
- lanceur : lancer_pilote4_gemini_v10.sh, sha256 0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952
- source des registres : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/go-sain.md ; dépenses : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/dep-segments.md
- aucune course voisine du noyau dans ce conteneur au départ (détection par pgrep)
- ESSAI : artefact « question » (simulation)
- état de reprise : etat-v1.json, sha256 dddd508538856ad7474e829bf7fe49314b77e0c8608ed2a595216f6641a9f0a1 (compagnon conforme), arrêt sur STOP du segment 1 ; dépense de la course jusqu'ici 0.0947 USD ; reste au plus 74.9053 USD pour la course (plafond 75 USD)
- course M de référence : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/m-reference/pilote2-gemini-v5-2-1-maieutique-v1 ; M saine : g000 et g001 OK, au plus 20 % d appels hors OK et au moins un appel OK de Fable à chacune (g000 {"OK": 123}; g001 {"OK": 129}), fin « générations maximales », arrêt « aucune lignée active », code 0, archive fermée ; graine de M 3970427751169333427 ; dépense du noyau 2.9344 USD ; refus du noyau par génération [[], []] ; empreintes de M vérifiées (EMPREINTES-pilote-v1.txt, sha256 d0185263641e21f8d3be97f2fa704cc79dbfb37c3e2e48e916a1abb854b3cf6d) ; graine 3970427751169333427 = graine M du texte scellé du second pilote (d2944654…)
- code : identique à 8e5e2f7b (commit et arbre de travail : essaim_m3, tests, collisionneur) ; commits postérieurs limités aux pièces du pilote ; rien de non suivi hors des dossiers de pilotes ; 4967734 et 90595ffb ancêtres ; banque 157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d ; mission bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e ; collisionneur 213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd
- versions : python 3.13.17 ; numpy 2.4.6 ; anthropic absente
- isolation : dossier du pilote 0700 à root ; espace attendu /var/lib/essaim-m3/fe89ce9ef772e504 ; dépôt /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot caché aux organismes (vérifié par bac_a_sable.dossiers_a_cacher) ; ESSAIM_M3_ESPACE non définie
- préenregistrement : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/prereg-sain.md, sha256 f21fade08c6800c73034d4cabb28bd25c70a92d398f13509876fc2d4e5543362 (compagnon conforme), graine 1541481317522987174 de la course v6-2 écrite et recalculée depuis l'entropie du texte, empreinte du lanceur citée
- refus : empreinte de la question ≠ 8b1c7511… (2026-10-26T00:03:01Z) ; verrou /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/.verrou-pilote4-gemini-v6-2-v1-segment2 retiré

## Segment 2, essai 8 (simulation, tentative 1)

- début (UTC) : 2026-10-26T00:03:02Z ; hôte : vm ; utilisateur : 0
- course : v6-2 ; dossier du pilote : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/pilote4-gemini-v6-2-v1 (0700, à root) ; pièces de ce segment : segment-2-t8/
- dépôt : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot ; HEAD : da3ca3382b25c1e61a4cdcc1f8051d33ab056b77 (celui du segment 1, que le manifeste consigne)
- lanceur : lancer_pilote4_gemini_v10.sh, sha256 0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952
- source des registres : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/go-sain.md ; dépenses : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/dep-segments.md
- aucune course voisine du noyau dans ce conteneur au départ (détection par pgrep)
- état de reprise : etat-v1.json, sha256 dddd508538856ad7474e829bf7fe49314b77e0c8608ed2a595216f6641a9f0a1 (compagnon conforme), arrêt sur STOP du segment 1 ; dépense de la course jusqu'ici 0.0947 USD ; reste au plus 74.9053 USD pour la course (plafond 75 USD)
- course M de référence : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/m-reference/pilote2-gemini-v5-2-1-maieutique-v1 ; M saine : g000 et g001 OK, au plus 20 % d appels hors OK et au moins un appel OK de Fable à chacune (g000 {"OK": 123}; g001 {"OK": 129}), fin « générations maximales », arrêt « aucune lignée active », code 0, archive fermée ; graine de M 3970427751169333427 ; dépense du noyau 2.9344 USD ; refus du noyau par génération [[], []] ; empreintes de M vérifiées (EMPREINTES-pilote-v1.txt, sha256 d0185263641e21f8d3be97f2fa704cc79dbfb37c3e2e48e916a1abb854b3cf6d) ; graine 3970427751169333427 = graine M du texte scellé du second pilote (d2944654…)
- code : identique à 8e5e2f7b (commit et arbre de travail : essaim_m3, tests, collisionneur) ; commits postérieurs limités aux pièces du pilote ; rien de non suivi hors des dossiers de pilotes ; 4967734 et 90595ffb ancêtres ; banque 157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d ; mission bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e ; collisionneur 213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd
- versions : python 3.13.17 ; numpy 2.4.6 ; anthropic absente
- isolation : dossier du pilote 0700 à root ; espace attendu /var/lib/essaim-m3/fe89ce9ef772e504 ; dépôt /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot caché aux organismes (vérifié par bac_a_sable.dossiers_a_cacher) ; ESSAIM_M3_ESPACE non définie
- préenregistrement : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/prereg-sain.md, sha256 f21fade08c6800c73034d4cabb28bd25c70a92d398f13509876fc2d4e5543362 (compagnon conforme), graine 1541481317522987174 de la course v6-2 écrite et recalculée depuis l'entropie du texte, empreinte du lanceur citée
- organisme : 26 fichiers, empreinte d'arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d ; question (v6-2) : sha256 8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd
- registre : une ligne GO-2026-10-25-02 de type calcul portant l'empreinte de la question (v6-2), celle de l'organisme (4f13647a…) et celle du texte scellé (f21fade08c6800c7) ; dépense consignée avant (segment 2) ; reste déclaré 150 USD ≥ 74.9053 (vérification du lanceur)
- test de dépense : td-seg-2a.json, sha256 6ee5659c9eb1d3274fe76239db6515ac5887e48d5dffcc15d57b15db366a2bb2 — trois espèces OK, modèles servis conformes, coûts CLAUDE_FABLE_5_1 0.00058, CLAUDE_OPUS_5_5 0.000232, GEMINI_ARGON 0.00076 USD, âge 1 s ; noms des variables du test : absents de la pièce (réserve, P52C1-05) (réalité des appels attestée par l'outil de session-depot ; le script vérifie la pièce)
- recharge automatique attestée : « essai »
- ESSAI : rapport JUnit repris de /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/junit-sain-v1.xml (simulation)
- essais : 169 passés, 0 sauté, 0 désélectionnés ; arguments : « aucun » ; les 45 essais cités ont passé ici (dont la recherche réelle sur arXiv)
- noyau sans bytecode : empreinte 61ddd638d7a3b5519a7294fc04a75003e3d21da72b9cfdcf4dd07dc0341565a0 (la fonction écarte le bytecode depuis le constat n° 30 § 5)
- test de dépense revérifié au départ : trois espèces OK, modèles servis conformes, coûts CLAUDE_FABLE_5_1 0.00058, CLAUDE_OPUS_5_5 0.000232, GEMINI_ARGON 0.00076 USD, âge 1 s ; noms des variables du test : absents de la pièce (réserve, P52C1-05)
- voisines au départ : aucune
- RÉSERVE : des essais (pytest) tournent dans le conteneur au départ (PID 21948 21949 21951 ) : ceux du noyau font tourner des processus sous l'utilisateur 60900 de ce pilote
- environnement du noyau (noms seulement, valeurs jamais écrites) : PATH HOME LANG PYTHONDONTWRITEBYTECODE ESSAIM_M3_CACHER .
- marqueur de départ : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/.partis/pilote4-gemini-v6-2-v1, posé au segment 1 pour ce dossier (R3 ; jamais retiré)
- STOP du segment 1 retiré de course/ (reprise)
- départ de la simulation (UTC) : 2026-10-26T00:03:03Z ; segment 2, reprise de la course
- PID de la course : 23683 (arrêt humain par ce PID seulement, R10 ; STOP dans course/ : arrêt avant la ronde ou la génération suivante, celle en cours finit)
- minuteur : PID 23684 ; échéance 2026-10-26T00:59:41Z, 3400 s après le départ du lanceur (2026-10-26T00:03:01Z)
- échec inattendu (code 9) à la ligne 800 (2026-10-26T00:03:03Z) ; verrou /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/.verrou-pilote4-gemini-v6-2-v1-segment2 laissé (à examiner)
- minuteur arrêté par son PID (23684) à la fin de la course : STOP non posé
- fin du processus (UTC) : 2026-10-26T00:03:03Z ; code de retour : 9 ; sortie standard fermée (non lue) ; sortie d'erreur : segment-2-t8/sortie-erreur-lanceur.txt (lisible)
- reprise refusée par le noyau (code 9 ; motif dans segment-2-t8/sortie-erreur-lanceur.txt) : la course reste arrêtée au segment 1, ouverte, rien n'a tourné ; décision de Lazar : refaire SEGMENT=2 après correction, ou SEGMENT=2 CLORE=1

## Segment 2, essai 9 (simulation, tentative 1)

- début (UTC) : 2026-10-26T00:03:03Z ; hôte : vm ; utilisateur : 0
- course : v6-2 ; dossier du pilote : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/pilote4-gemini-v6-2-v1 (0700, à root) ; pièces de ce segment : segment-2-t9/
- dépôt : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot ; HEAD : da3ca3382b25c1e61a4cdcc1f8051d33ab056b77 (celui du segment 1, que le manifeste consigne)
- lanceur : lancer_pilote4_gemini_v10.sh, sha256 0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952
- source des registres : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/go-sain.md ; dépenses : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/dep-segments.md
- aucune course voisine du noyau dans ce conteneur au départ (détection par pgrep)
- état de reprise : etat-v1.json, sha256 dddd508538856ad7474e829bf7fe49314b77e0c8608ed2a595216f6641a9f0a1 (compagnon conforme), arrêt sur STOP du segment 1 ; dépense de la course jusqu'ici 0.0947 USD ; reste au plus 74.9053 USD pour la course (plafond 75 USD)
- course M de référence : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/m-reference/pilote2-gemini-v5-2-1-maieutique-v1 ; M saine : g000 et g001 OK, au plus 20 % d appels hors OK et au moins un appel OK de Fable à chacune (g000 {"OK": 123}; g001 {"OK": 129}), fin « générations maximales », arrêt « aucune lignée active », code 0, archive fermée ; graine de M 3970427751169333427 ; dépense du noyau 2.9344 USD ; refus du noyau par génération [[], []] ; empreintes de M vérifiées (EMPREINTES-pilote-v1.txt, sha256 d0185263641e21f8d3be97f2fa704cc79dbfb37c3e2e48e916a1abb854b3cf6d) ; graine 3970427751169333427 = graine M du texte scellé du second pilote (d2944654…)
- code : identique à 8e5e2f7b (commit et arbre de travail : essaim_m3, tests, collisionneur) ; commits postérieurs limités aux pièces du pilote ; rien de non suivi hors des dossiers de pilotes ; 4967734 et 90595ffb ancêtres ; banque 157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d ; mission bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e ; collisionneur 213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd
- versions : python 3.13.17 ; numpy 2.4.6 ; anthropic absente
- isolation : dossier du pilote 0700 à root ; espace attendu /var/lib/essaim-m3/fe89ce9ef772e504 ; dépôt /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v7/depot caché aux organismes (vérifié par bac_a_sable.dossiers_a_cacher) ; ESSAIM_M3_ESPACE non définie
- préenregistrement : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/entrees/prereg-sain.md, sha256 f21fade08c6800c73034d4cabb28bd25c70a92d398f13509876fc2d4e5543362 (compagnon conforme), graine 1541481317522987174 de la course v6-2 écrite et recalculée depuis l'entropie du texte, empreinte du lanceur citée
- organisme : 26 fichiers, empreinte d'arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d ; question (v6-2) : sha256 8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd
- registre : une ligne GO-2026-10-25-02 de type calcul portant l'empreinte de la question (v6-2), celle de l'organisme (4f13647a…) et celle du texte scellé (f21fade08c6800c7) ; dépense consignée avant (segment 2) ; reste déclaré 150 USD ≥ 74.9053 (vérification du lanceur)
- test de dépense : td-seg-2.json, sha256 fc70c3c1eaa3c5276b4620db3929e508843557f28a66a882aa267dd1e50f00e1 — trois espèces OK, modèles servis conformes, coûts CLAUDE_FABLE_5_1 0.00058, CLAUDE_OPUS_5_5 0.000232, GEMINI_ARGON 0.00076 USD, âge 1 s ; noms des variables du test : absents de la pièce (réserve, P52C1-05) (réalité des appels attestée par l'outil de session-depot ; le script vérifie la pièce)
- recharge automatique attestée : « essai »
- ESSAI : rapport JUnit repris de /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/junit-sain-v1.xml (simulation)
- essais : 169 passés, 0 sauté, 0 désélectionnés ; arguments : « aucun » ; les 45 essais cités ont passé ici (dont la recherche réelle sur arXiv)
- noyau sans bytecode : empreinte 61ddd638d7a3b5519a7294fc04a75003e3d21da72b9cfdcf4dd07dc0341565a0 (la fonction écarte le bytecode depuis le constat n° 30 § 5)
- test de dépense revérifié au départ : trois espèces OK, modèles servis conformes, coûts CLAUDE_FABLE_5_1 0.00058, CLAUDE_OPUS_5_5 0.000232, GEMINI_ARGON 0.00076 USD, âge 1 s ; noms des variables du test : absents de la pièce (réserve, P52C1-05)
- voisines au départ : aucune
- RÉSERVE : des essais (pytest) tournent dans le conteneur au départ (PID 21948 21949 21951 23915 ) : ceux du noyau font tourner des processus sous l'utilisateur 60900 de ce pilote
- environnement du noyau (noms seulement, valeurs jamais écrites) : PATH HOME LANG PYTHONDONTWRITEBYTECODE ESSAIM_M3_CACHER .
- marqueur de départ : /tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/cas-seg-segment1/.partis/pilote4-gemini-v6-2-v1, posé au segment 1 pour ce dossier (R3 ; jamais retiré)
- départ de la simulation (UTC) : 2026-10-26T00:03:04Z ; segment 2, reprise de la course
- PID de la course : 23947 (arrêt humain par ce PID seulement, R10 ; STOP dans course/ : arrêt avant la ronde ou la génération suivante, celle en cours finit)
- minuteur : PID 23948 ; échéance 2026-10-26T00:59:43Z, 3400 s après le départ du lanceur (2026-10-26T00:03:03Z)
- minuteur arrêté par son PID (23948) à la fin de la course : STOP non posé
- fin du processus (UTC) : 2026-10-26T00:03:10Z ; code de retour : 0 ; sortie standard fermée (non lue) ; sortie d'erreur : segment-2-t9/sortie-erreur-lanceur.txt (lisible)
- extrait mécanique : extrait-mecanique-v1.json, sha256 e5f65e72e9cff258c0334f29094a87ef0948b4fceb5efbd983f6780de910e684
- vérification après départ (extrait) : isolation {"espaces_noms": true, "reseau": true, "root": true, "utilisateur": true} ; collisionneur conforme : True ; commit da3ca3382b25c1e61a4cdcc1f8051d33ab056b77 ; sha256_code_noyau 61ddd638d7a3b5519a7294fc04a75003e3d21da72b9cfdcf4dd07dc0341565a0 ; espace /var/lib/essaim-m3/fe89ce9ef772e504 ; sources de moisson ["simulation"] ; clés présentes au manifeste — web : False, OpenAlex : False, Semantic Scholar : False ; temps par ronde de conception 900 s ; dépense du noyau 7.0099 USD (à rapprocher de la console, P2C1-05)
- journal des appels g000 : journal-appels-g000.jsonl, sha256 a30beed7f64f4b6fec2723d879437269d5d3279521ac85913388277d2847168a
- journal des appels g001 : journal-appels-g001.jsonl, sha256 d88244fb56b5a2fbaeb30b5d0e56906ed6e2edbe946d4ab5286a62ee1088e6f8
- journal des appels g002 : journal-appels-g002.jsonl, sha256 5dd9e6386c1b7234ed3ec8ee6e951c82ec8e8734c754b6044b8810d95d2e9162
- journal des appels g003 : journal-appels-g003.jsonl, sha256 38803a904e2f89ab1059e518491251de2594777f0661c0c7bf2eed59efe8f02d
- journal des appels c001 : journal-appels-c001.jsonl, sha256 f6a9c54788a7a793c6114c748372faa0302a425a8e889a6a9727f2d20fe8bedd
- journal des appels c002 : absent ou non ordinaire dans l'archive (génération non tournée, ou anomalie) — rapporté
- journal des appels c003 : absent ou non ordinaire dans l'archive (génération non tournée, ou anomalie) — rapporté
- journal des appels c004 : absent ou non ordinaire dans l'archive (génération non tournée, ou anomalie) — rapporté
- journal des appels c005 : absent ou non ordinaire dans l'archive (génération non tournée, ou anomalie) — rapporté
- journal des appels c006 : absent ou non ordinaire dans l'archive (génération non tournée, ou anomalie) — rapporté
- réponse à la question : reponse-question-g001.md, sha256 d3d10b46249b95d3435913df2185acde99295fba7fc95dc0b39288f337a8f473
- archive fermée : ferme.tar.gz (course, sortie standard, espace des organismes), sha256 8b3633f4b2262ff9f10e039c84e32fb0c03c5e9259384c0a91a62ab21d913932, 3694 entrées = 3694 sur disque ; copies ouvertes retirées
- fin du lanceur (UTC) : 2026-10-26T00:03:11Z
