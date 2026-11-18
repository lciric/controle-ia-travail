# Provenance du code d'EvoSCM lu contre O4 — v1

- **Lecteur** : modèle I.
- **Origine** : https://github.com/evoscm/EvoSCM (adresse donnée par le PDF arXiv 2609.01526v2, p. 1), clone en lecture seule déjà présent sous code-o4/EvoSCM dans le dossier de travail de la session ; non cloné par moi, aucun accès réseau.
- **Commit** : ffb638998da9537d738c20176ad928319889ff96 (git rev-parse HEAD, vérifié 2026-11-18T01:42:48Z) ; dernier commit daté 2026-10-12 21:11:50 +0800 selon git log.
- **Relevé des empreintes** : 2026-11-18T01:54:28Z (date -u) ; sha256sum de chaque fichier suivi (git ls-files), 52 fichiers.
- **Licence** : fichier LICENSE lu en entier : licence MIT ; la ligne de titulaire du droit d'auteur est vide (l. 2-3 blanches).
- **Bancs couverts** : banc de physique (DiscoverPhysics) seulement ; aucun code des bancs de matériaux ni de gènes dans ce commit.
- **Usage** : lecture seule ; aucun programme du clone lancé, rien installé. Le code n'est pas versé dans le dépôt.

## Fichiers suivis, empreintes et profondeur de lecture

| fichier | lignes | sha256 | lecture |
|---|---|---|---|
| .env.example | 5 | fdd2a5e92ccb290bdd5f7c6fc097a3bf4b93bf4d6d8167a9f22a5c25aa2d2411 | noms de variables seulement, valeurs non lues |
| .gitignore | 13 | d34187cd0f0310ff46e5c639ed22be9da25057b1c7457bb88a257780f7810458 | en entier |
| LICENSE | 20 | c9b7c49cdeb4ccab2f2cb69e67f3405518e4bcf611bd3b01de101b070659d11d | en entier |
| PhysicsSchool/physchool/__init__.py | 1 | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b | parcouru (structure et recherche de termes) |
| PhysicsSchool/physchool/worlds/analytic_orbits.py | 65 | 58b8f784db3aa395cc3ca5207064ace0cd663f05afae8dfd9323e747a4cb7b23 | parcouru (structure et recherche de termes) |
| PhysicsSchool/physchool/worlds/field_sampler.py | 212 | 99470fe38b81dc0f1c3f7d4b33b13ad9b1d27d1b274283a11c67a788c054a6ec | parcouru (structure et recherche de termes) |
| PhysicsSchool/physchool/worlds/force_laws.py | 112 | 12842ee5989ea4905f12802ec9b4a659680fc5dd6d0041bdda1ea6537f1f5aa9 | parcouru (structure et recherche de termes) |
| PhysicsSchool/physchool/worlds/main.py | 1 | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b | parcouru (structure et recherche de termes) |
| PhysicsSchool/physchool/worlds/nbody_sampler.py | 414 | b3f10bda1807ee6e0e62cb4467437f0ee52b6208f1daf982e8f481d1316f4cdb | parcouru (structure et recherche de termes) |
| PhysicsSchool/physchool/worlds/utils.py | 134 | c4659c07e0579099bd276d9f8dc45a272c48e741c12b778e330c2ba1a6b9e486 | parcouru (structure et recherche de termes) |
| PhysicsSchool/prompts/2particle_instructions.md | 67 | 87ac4635f7fef0394efe7d11c481b1e633839df34d6e1b5d1c5a702c0f14631b | parcouru (structure et recherche de termes) |
| PhysicsSchool/prompts/_template_interactive.md | 74 | c2677fa7a35884c78ea094b4a9433085605543c4c1549b9ddfce9d117721362c | en entier |
| PhysicsSchool/prompts/circle_instructions.md | 61 | 83bd5ce8bd0ea416b6d311b9efacda4be91247f587ec42ef5fc1bd6fbfb483e8 | parcouru (structure et recherche de termes) |
| PhysicsSchool/prompts/probes_instructions.md | 61 | 20986dba2042990b5ebb2504c0e57270b490136590835acaaea17cecf94a0dc7 | parcouru (structure et recherche de termes) |
| PhysicsSchool/prompts/probes_with_masses_instructions.md | 68 | 596449db2cc70fe7dd885497bc2888a588f2170a5af9c37ad5a789517ecc6c44 | parcouru (structure et recherche de termes) |
| PhysicsSchool/prompts/scm_protocol.md | 494 | e2087f939228d664c6299db0b38f6d4a69dd2963a64749e926c1c8ef5d3c4ef2 | en entier |
| PhysicsSchool/setup.py | 9 | 82c1a8385883f3dd03e1c8e851e32080c06119c9b4a25eb39306cdc90c9d5afb | parcouru (structure et recherche de termes) |
| README.md | 143 | 22216b6eca6e80ad64d249e6f9ae7b75b4816a1cb361ea80efbc3ec5b356a3d3 | l. 20-110 ; reste par recherche |
| ScienceAgent/scienceagent/__init__.py | 4 | 88192496702f999ed5492f1b5cb3562e572fb1f03e20faa615e4f0b0fa5db8ec | parcouru (structure et recherche de termes) |
| ScienceAgent/scienceagent/agent.py | 1310 | 3a156ff80b6fa24acafbc0cc6127921ce69c5a160bf60e40b7c921d22b1e1dce | en entier |
| ScienceAgent/scienceagent/context_window.py | 369 | ca38f42d1a716a886c6fb77aab745a2d46bf8f7879f298cbda2350939b9a2605 | l. 320-369 et recherche |
| ScienceAgent/scienceagent/evaluator.py | 1433 | dd640c8786206050e5b54286566ec5b091d6b9072fef191c63dc06d56aefd6e4 | parcouru (structure et recherche de termes) |
| ScienceAgent/scienceagent/executor.py | 1548 | af71640826ae0d2257e34e7f32730847152bb610922e70170936931f0b9b6fc3 | parcouru (structure et recherche de termes) |
| ScienceAgent/scienceagent/llm_client.py | 73 | c7ccab5c4e3426ba2ada8cb93aed5d4e2a9c52a59eb2675879bcd31086dbbf58 | en entier |
| ScienceAgent/scienceagent/load_trajectories.py | 204 | 659698fd7bcc0820b5f718622684879cd70146194089b81bbec4066cbfcbcf22 | parcouru (structure et recherche de termes) |
| ScienceAgent/scienceagent/mse_fitting.py | 312 | 176a1eb00443fb5cfb26b5b4fc431d7a09ba6bd0daf0f98f3b941cfb1e248ee3 | parcouru (structure et recherche de termes) |
| ScienceAgent/scienceagent/release.py | 187 | 066d0a895bf0f2ae6fdd3753f88da4708d278783f906f3e360b6caf691d92939 | en entier |
| ScienceAgent/scienceagent/response_protocol.py | 38 | f57510983280cc2952490c8203017242922ca0d2b7fd29d79c6adf97952451b8 | en entier |
| ScienceAgent/scienceagent/responses_transport.py | 34 | 9b73b4061132a4a81ed4b1bde25c463d92184dcc0493624a8ac6cf845263d119 | en entier |
| ScienceAgent/scienceagent/scm_pipeline.py | 4455 | 7e1f6c4f3e15d3ea5dc4d8a2e51f607aaeb1b850002b7284136d8c3bd65c4d7c | décisif en entier (l. 1-80, 390-680, 1480-1560, 1703-1930, 2101-2170, 2237-2264, 2382-2470, 2560-2600, 2775-2805, 2979-4455) ; reste parcouru |
| ScienceAgent/scienceagent/trajectory_logger.py | 327 | 5d09ebf7a98ba23b18bd16c385be64eb0272feb920293dd1665503077630c8de | l. 1-120 et structure |
| ScienceAgent/scienceagent/transfer.py | 179 | 2bc86fc19047325a369bf378f93e703c5bb2af45e147e951df76f853d9af24d5 | l. 1-140 ; reste par recherche |
| ScienceAgent/scienceagent/worlds.py | 319 | 5b8832ac34c96bebf276c24fff61cb177e72fbecdeced52aa0a7fdfc44e90bbb | parcouru (structure et recherche de termes) |
| ScienceAgent/setup.py | 17 | 666e9328c0397dffb27e9e0c9abddd8ab4ece0d37e4c6636635dfb6da758b61a | parcouru (structure et recherche de termes) |
| assets/figures/analysis1.webp | 443 | 1d1b9d123d032d6ac6f8da9126effb054f51557bc741c3aac2b5bd5e66c16961 | non lu (image) |
| assets/figures/analysis2.webp | 524 | 01cc016a8d2ba77e5220c2102b053fe46ab740501a2eb0f9d4e2fd77c0eb79ea | non lu (image) |
| assets/figures/first_image.webp | 500 | 862812e3dbbaafebe7014ccd9a65e0c542774a0001e793080c5e3b8e4603f944 | non lu (image) |
| assets/figures/method.webp | 1048 | 42b2db845d42103ce831589357cd380d02901fd3595b6c093e18887f9c121eb2 | non lu (image) |
| configs/baseline/gpt55.yaml | 9 | ce9abf594c8a863f7015a1c30e3cfa427f81a53a724bc56d8b968c7c98399c8d | en entier |
| configs/evoscm/gpt55.yaml | 9 | 81df322a292b4be78f29adddba587dc3f1c24b372b2d444b4d3f5cb25dd7b88c | en entier |
| environment.yml | 15 | 2755a98520f160418202755d356e59d225d577ea1e83296e7c910961d04dc373 | en entier |
| scripts/evaluate.py | 85 | aeeadda8345c64ef8eebce9cc33864b2ccafdaedcae39a33e6574ed2b05a9c25 | en entier |
| scripts/run_benchmark.py | 83 | cdc804acf8d1c7c4fac6db52fd7f83b9607e2807ac81b039a61d00614145140f | en entier |
| scripts/run_discovery.py | 30 | 7dc26b520ad286a8e98979502244e7d5ff02f2162673ceb15a33663cc5f343e7 | en entier |
| scripts/run_transfer.py | 89 | db7b95676b7d825e1956c361c962bd906d0ae65ea0d6c04c7973cd10b2dc8595 | parcouru (structure et recherche de termes) |
| scripts/smoke_test.py | 28 | 93d8adfdd7ff8941a23163df07b1dce35cc69b596e664075d0b8e588b680f89d | en entier |
| tests/conftest.py | 9 | 3a93fdb401649dbeff832431a445ea7b2866c29c9d2e3e5c7080bdf3e6951503 | parcouru (structure et recherche de termes) |
| tests/test_context_window.py | 93 | 74c82b657fe0459a05e40326d81710bafd92a86c0ff118d8c5f585f8a0c3c0ef | parcouru (structure et recherche de termes) |
| tests/test_mse_fitting.py | 333 | 4da901ad464a195d8681a6df1a64f724235b36fc4276fd4cb898294988d818ec | parcouru (structure et recherche de termes) |
| tests/test_release.py | 246 | a1fff35d3fea3f684717c81450af69d8d8b5a2be5441ca2c4d5b269c4c8c24c3 | parcouru (structure et recherche de termes) |
| tests/test_response_protocol.py | 87 | 75b7df16e3945d9999f1f6b1e87fe8750480423c8159bc1892edf621c5b785f9 | parcouru (structure et recherche de termes) |
| tests/test_scm_pipeline.py | 2049 | fb1a6fb7bafb01fe419aae2b35372f71d4acfff1d958ea1641e281102c841a65 | l. 180-270, 1694-1900 ; reste par recherche |
