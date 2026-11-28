# Dossier de relecture externe de P3 — v1

Préparé le 2026-10-19 par la session de mise en œuvre du programme de Lazar (Claude), à la demande de Lazar, pour une
relecture par un modèle externe. Les pièces sont des copies du dépôt de travail privé, au commit `22ea3c8ce66c` (code de P3 au
commit `7a54d431d89745839220f882b41b13e8c62ecfdd`, inchangé depuis). Le prompt de la relecture est livré à part
(`relecture-externe-P3-v1-prompt.md`).

## Ce qu'est P3, en une phrase

Premier test boîte blanche, réduit, des critères 2 et 3 de la porte de la phase 0 sur l'organisme (i-a) : un agent
Llama-3.1-8B-Instruct, saboteur instruit en privé de gonfler le coût déclaré de ses propositions, contre un agent honnête,
un témoin instruit et une condition « mention sans usage » ; des sondes génériques figées avant les épisodes ; des aires sous
la courbe comparées à un plancher de 200 sondes aléatoires appariées ; un seul run, rapporté quel qu'en soit le signe.

## État

- Le texte `1-texte/P3-premier-test-i-a-v1-candidat4.md` est le candidat relu ; le texte scellé en sera la copie octet pour
  octet. Il a été contre-lu deux fois (texte et code ; chaîne), puis relu après traitement (relecture courte, trois
  relecteurs), puis trois écarts successifs ont été relus (candidats 2, 3 et 4) : `2-relectures/`.
- Code : 908 tests au commit cité ; les modules `sondes/` et `harnais/` sont gelés par des étapes antérieures.
- Le lancement suit le scellement (environ 4 à 6 heures d'une carte A100 80 Go, au plus ≈ 11,4 USD).

## Exclus, et pourquoi

- Les **consignes privées** des trois conditions instruites (fichier `prereg/P3-consignes-v1.md`) : textes de l'expérience ;
  le texte cite leurs longueurs en jetons (51 et 10) ; disponibles à la demande, sur décision de Lazar.
- Les **données des runs** et les **textes des actions** de l'agent (dépôt privé seulement, décision R-202).
- Les **registres** complets (seules les décisions citées par le texte, en extraits : `4-contexte/decisions-citees-P3.md`).
- Les **PDF d'articles de tiers** et toute pièce sur le financement du programme.
- Aucun secret n'est dans ces fichiers (les jetons d'accès ne sont jamais écrits dans le dépôt).

## Contenu (empreinte sha256 de chaque fichier)

| fichier | sha256 |
|---|---|
| `1-texte/P3-premier-test-config-v1-candidat3.json` | `702303e9453f7c4ce8f0cf900f45fc8075b75744eedab0b1652dd8e52d55abde` |
| `1-texte/P3-premier-test-i-a-v1-candidat4.md` | `d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672` |
| `2-relectures/P3-premier-test-v1-relecture-chaine-v1.md` | `57060da8f239f6c894978a187668f5f75d2b214cd25e9c7e3463b32dd7461db6` |
| `2-relectures/P3-premier-test-v1-relecture-courte-chaine-v1.md` | `dd9841f0f2e3342b2734417fecd44d75fd66b128e96272139176b509ff992069` |
| `2-relectures/P3-premier-test-v1-relecture-courte-code-v1.md` | `3589ad6f899ef676209ebd4a37f0ce8a7418e2108d3bfa3649171fde881e5adc` |
| `2-relectures/P3-premier-test-v1-relecture-courte-texte-v1.md` | `c685659a120f7071e707503d16b978fa9830562fcf49b6d910a53d7b8c50e57a` |
| `2-relectures/P3-premier-test-v1-relecture-texte-code-v1.md` | `98d7201b0c3671d28a8cc05e4f744a86cd6fa544a5eca02826339baaa2263c5f` |
| `2-relectures/traitement-CH-v1.md` | `ad1d88d27dca0d4acfdbaed3238b179ea923574dd4abcf0811c5c025cb0e12ca` |
| `2-relectures/traitement-banc-controles-v1.md` | `db5be719bd5c3120fbe5c62a20e58edd4899f97f09ab08f6484929edbb6c7a5b` |
| `2-relectures/traitement-relecture-courte-v1.md` | `31e00a19cc6f22e8ec9cd6821af71a841e8f14bbf4571d768d75a9bb2a66ebab` |
| `2-relectures/verification-ecart-P3-candidat2-v1.md` | `af89de7598445f5e84e5a470b6549d57a94841135b676f2c4433ac137549722b` |
| `2-relectures/verification-ecart-P3-candidat3-v1.md` | `e3a1b7ca7c2b319cd7a1c1af72e6bc281a4c3689348bfe1324bfcd878051a02b` |
| `2-relectures/verification-ecart-P3-candidat4-v1.md` | `3cc0f0aeccfc95ed09ae71763eae53376295585ceab34fe94b9e31de996984f5` |
| `3-code/scripts/amorce_instance_p3.sh` | `0bfaeaa64a0c355ba04bf84c9afc76ea31034a837e44cd588becf88f3aa5dae0` |
| `3-code/scripts/p3_instance.sh` | `2bfc6939efe8b68d17b921e0ea8b91e2809b04e5c37006c18364dc4776dc3663` |
| `3-code/src/controle_ia/harnais/__init__.py` | `a977e6e9ad612aa96c099b9c5fb34bb42eb659261dd226780cfc441738b5caaa` |
| `3-code/src/controle_ia/harnais/activations.py` | `adeb5856d430f3a6163989c2a53c8ced459235c6dcdd03834b694404c57e0095` |
| `3-code/src/controle_ia/harnais/episode.py` | `79113b4973d64bbcf0af16b2d7114c009b34132e1392e95ff83cef4d0a488c32` |
| `3-code/src/controle_ia/harnais/formats.py` | `98dbfa9b13578946c4d731c4bb1cfcfb85b9fd0cacdfd56a786042c93e6ef6b4` |
| `3-code/src/controle_ia/harnais/modeles.py` | `d0befc29aeba4b2487b85d365b8087c467769f0d99f610267f85f19cbea221a7` |
| `3-code/src/controle_ia/harnais/politique.py` | `0a85164c002a7993f951299e11e7beb6e67b9ba80e3394c46676353dde9dbd5f` |
| `3-code/src/controle_ia/harnais/run_harnais_factice.py` | `43a244315573eac5cc07cf90089f057ce94878851c01085e0ad64b7ef782849c` |
| `3-code/src/controle_ia/harnais/sonde_memoire.py` | `61b3e94890960180625c07bf2a95c3ec5d3b3173f4b74a087b3f975cc60b088e` |
| `3-code/src/controle_ia/harnais/sondes.py` | `f92657a69cf0d5781017e50117aeb1672dda60719aea51ffbfd9e566f3e7d94d` |
| `3-code/src/controle_ia/harnais/stockage.py` | `73554d0ef41f2b5b628b44c47ffafead38c60991b371c97eb36b1fc4d4a30220` |
| `3-code/src/controle_ia/harnais/validation_reelle.py` | `d25e4cd92d73eef4d2bd6c7d17328daf49a49c76eab7afd91500d9c04ded8289` |
| `3-code/src/controle_ia/manifeste.py` | `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d` |
| `3-code/src/controle_ia/premier_test_ia/__init__.py` | `c72da1602f1998e4c7b30b670e89143d6a9c6337b903164f4bc6eed5ab9a5f92` |
| `3-code/src/controle_ia/premier_test_ia/conditions.py` | `dda641175fa595c95ee648bb82af21035154ab25180ce46250beb6330710ac63` |
| `3-code/src/controle_ia/premier_test_ia/donnees.py` | `fa89340e98b5a4353db206a4df47e9043b28cc505f1f1008ccda47cab386b0b0` |
| `3-code/src/controle_ia/premier_test_ia/empans.py` | `58043c95c8d6afc9cf155015c2cffb2130596d479445a7b63a3b1cd9522746c0` |
| `3-code/src/controle_ia/premier_test_ia/entrainement.py` | `7e701026c6bd9b2268e785683b25a18503ce36564dfa3274b3ded8662a54b664` |
| `3-code/src/controle_ia/premier_test_ia/figees.py` | `a2238a8c6f164f59f7d30e3ca15c45be136cb3ad5cdf149816622d81450938cc` |
| `3-code/src/controle_ia/premier_test_ia/lecture.py` | `ab7c21cb72a7814c7658e543132a744f5ba1976783a0afbc64eeb84e030da0ba` |
| `3-code/src/controle_ia/premier_test_ia/notation.py` | `73c493bf8b354313b4aee4aeafda4d9dfcfbdcb30988519c80fb3a898077fd3d` |
| `3-code/src/controle_ia/premier_test_ia/run.py` | `b3f14d8e61fe8352aba1e95744fe239e2957bdf75f84241ff5154dfb388e4609` |
| `3-code/src/controle_ia/premier_test_ia/statistiques.py` | `a85525752fbdaa2fcee874d084eb11a671adadf1302340a3d71a5e09f0b11e2a` |
| `3-code/src/controle_ia/sondes/__init__.py` | `a4ea91421aa179aa7662876afddde30f6558435c6d60c5ee41f7793613b3ba30` |
| `3-code/src/controle_ia/sondes/evaluation.py` | `1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3` |
| `3-code/src/controle_ia/sondes/familles.py` | `6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e` |
| `3-code/src/controle_ia/sondes/temoins.py` | `3b051b6fc2d78eeb4a44aab8a385bbce65095998e944b80e5f2a66e21b57faf7` |
| `3-code/tests/test_premier_test_ia_conditions.py` | `1aa6ae1ff8fd58172ba6f5c82164564f8cded03dce4d489d1a0c698a35b6e2ef` |
| `3-code/tests/test_premier_test_ia_entrainement.py` | `28fd4ab11e416a0f82134f97b03aa1678f5ceef27ab16109a6409b17f7900f0d` |
| `3-code/tests/test_premier_test_ia_figees.py` | `2ed958227271db670047752df3051edee97381d72e8ca17a2689ab9794b9ef45` |
| `3-code/tests/test_premier_test_ia_gardes_v1.py` | `cf4ab7b841a5599a23b01255a32d8e378200751c2472176892a7e02a5df956b3` |
| `3-code/tests/test_premier_test_ia_lecture.py` | `6d3969c03aeb84cfd7282cae0505554deefed396661581eaed11e04999f6ab44` |
| `3-code/tests/test_premier_test_ia_notation.py` | `6e217e5a4db2789ad1895ae4095e48991faa347767358314873c34f881b87d6e` |
| `3-code/tests/test_premier_test_ia_run.py` | `d8da52e4c9f5a43283edc7e39889b03365b51b88cfcf2de533582aa35b4287bf` |
| `3-code/tests/test_premier_test_ia_statistiques.py` | `c99c7cf30b528fed40da4e14f253571081a27689d512512b39a4206caf5fc511` |
| `3-code/tests/test_script_p3.py` | `21f90299ced25f572895ca88e0e22d1b207b2521ad1e0a00b99539a20466915c` |
| `4-contexte/P3-mesures-v2/chrono-reel-4fils-v1.txt` | `aa04961504f409579ddba6e56bab2a0d0c72597e3171352c663b70f71b1e4ca5` |
| `4-contexte/P3-mesures-v2/chrono_reel.py` | `42d9199ed6fb6981181ce9c62005f243bef64125ad2fd6ab0c1b0f4757884720` |
| `4-contexte/P3-mesures-v2/longueurs-gabarit-consignes-candidat2-v1.txt` | `28b87c71971cb6ba027d7ea97a28c5330fec1e9257bb1fbef8363bedc4b90e73` |
| `4-contexte/P3-mesures-v2/longueurs_gabarit.py` | `5816c7de82f9fb3ae9caf2b1a9f4c6cf4c01336d654255599c77a23a5cbea01a` |
| `4-contexte/P3-mesures-v2/puissance-p3-v1.txt` | `8a08307c2ea1d40d85095fbabb9bef7208c579b97f49527a61ac8a2538015d36` |
| `4-contexte/P3-mesures-v2/puissance_p3.py` | `1e679ef8236cf63b55237b71130d8375f655dd7c060d087f8474a80d6963a047` |
| `4-contexte/decisions-citees-P3.md` | `7d8f3c50b53f63fa30bdac0046fae411fe2b3d5164587028b0b0efdb48b751c7` |
| `4-contexte/programme-controle-ia-v2.md` | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` |
| `4-contexte/verdict-T0.5-pilote-v1.md` | `b9a072302d6514c0df80c950317012498c7af62b6440e37045a43de46a3faabc` |
| `5-chaine-annexe/controle_cinq_minutes_p3_v1.sh` | `3af7429518024b7a0861777dd099486dfce573aeb2b89dad315df72a275b332e` |
| `5-chaine-annexe/controles_avant_depense_p3_v1.sh` | `682e7f47d10f827db39e4692ba57a77b52c7529f4410fc2a5449e342ea71bf65` |
| `5-chaine-annexe/essais_controles_p3_v1.sh` | `35a434ac1fdaf23837d0cdd657654aaf1efe516c5b652ce7b1df94ec7d3dc8f8` |
| `5-chaine-annexe/essais_lanceur_p3_v1.sh` | `777030dffeaeb879cd70c55694eabfe9486996598ece3d6eb13c86014ebb7741` |
| `5-chaine-annexe/essais_scellement_p3_v1.sh` | `1e3bd6fe2987b976ac94add2baf94dd6a394b4c67b2b123b02d8fff0cfbe9679` |
| `5-chaine-annexe/essais_surveillance_p3_v1.sh` | `bb7a3c35cf9a1f36fe397f141f4f8ea43ab15ad901ab72c5654e021416644ca6` |
| `5-chaine-annexe/lancer_p3_v1.sh` | `8cd40e08ee4cab05356cd73f433c541f5ae22abe279b6b261621ea52038e4e12` |
| `5-chaine-annexe/recuperation_p3_v1.sh` | `c22ac581d1c6bd397c4ca3d43ffaf29bb3e05aba1e14421c338b48f7b91c4584` |
| `5-chaine-annexe/repetition_finale_p3_v1.sh` | `5e9b7bfe514089ef3b679abe4e7d2d9a956fb64033cf5d75d4523ca74fcc72ce` |
| `5-chaine-annexe/repetition_jouet_p3_v1.sh` | `cc4e6829759839cd659c86f94f1e616da112ec1ee79469390728c499b9a40928` |
| `5-chaine-annexe/sceller_p3_v1.sh` | `7e963932b72716f877692d5f223a50118173d5ac7b515a727a5c87e3686bf364` |
| `5-chaine-annexe/surveiller_p3_v1.sh` | `5a2fcc24da7d1e6fd20a2d9234066fddfaa55419d1e59d6786a0a619400ebeff` |
| `5-chaine-annexe/verifications_p3_v1.py` | `6667ac0ee7db2e7fe3f95eeb02d550565c75f4a26abc202cf204bc508405f1cc` |
