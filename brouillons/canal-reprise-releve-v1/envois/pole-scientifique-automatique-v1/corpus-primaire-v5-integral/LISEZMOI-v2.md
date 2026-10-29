# LISEZMOI — corpus primaire v5 « intégral », version 2

Date : 29 octobre 2026. Produit par un sous-agent d'extraction, sur décision de Lazar (directeur) du 29 octobre 2026 (R-439). Remplace par complétion le `LISEZMOI-v1.md` (qui reste, scellé, tel quel : il décrit l'état à dix papiers) ; les fichiers `integral-…` de la v1 ne sont pas réécrits.

**Dépôt privé seulement : texte intégral, aucun retrait, contenu d'attaque verbatim possible. Ce dossier ne va jamais dans la copie expurgée publique.**

## 1. Ce que c'est

Le texte complet, sans retrait ni retouche éditoriale, des 23 papiers servis en extraits dans les corpus primaires v1 à v4. Un fichier `integral-<identifiant><version>.md` par papier : en-tête (identifiant, titre tel qu'écrit dans le PDF, empreinte du PDF, outil, nombre de pages, nombre de caractères, mention de sûreté), puis, page par page, le marqueur `[p.N]` (N = numéro de page du PDF) suivi du texte de la page, références et annexes comprises.

Outil d'extraction : `pdftotext -layout -enc UTF-8` (pdftotext version 24.02.0, Poppler), une page à la fois (`-f N -l N`) ; `pypdf` non utilisé. Le sceau de chaque PDF (`.sha256`) a été vérifié par `sha256sum -c` avant toute lecture : 23 sur 23 OK (dix le 29 octobre 2026 lors du premier passage ; treize lors du second, après leur versement dans `docs/sources/pdf/`). Les empreintes des treize PDF versés sont identiques à celles que citaient les extraits v2 à v4. Le nombre de pages est celui de `pdfinfo`.

Deux transformations seulement touchent le texte brut de l'outil : (a) le marqueur `[p.N]` ajouté ; (b) les caractères de contrôle produits par l'extraction (glyphes de polices sans correspondance) : les caractères nuls supprimés, les autres remplacés par U+FFFD (position gardée). Le nombre et les pages concernées sont dans l'en-tête de chaque fichier. Aucune coupe, aucun rejointement de lignes, aucune correction.

## 2. Règle de sûreté modifiée (R-439)

Décision de Lazar du 29 octobre 2026 (`registres/decisions.md`, R-439) : le corpus d'idéation sert le texte intégral sans retrait aux proposeurs et aux juges, textes d'attaque compris ; la garde de sûreté des extraits est levée pour ce corpus seulement. La garde est maintenue sur tout le reste (internes des moniteurs, carte des hypothèses, mode tenu à l'écart, banques, textes d'actions, consignes de P3, `donnees/`). Ce corpus et ses dérivés sont exclus de la copie expurgée publique. Aucun papier n'a été refusé à l'extraction par l'agent.

## 3. Règle de provenance inchangée (R7)

Un texte intégral n'est pas une vérification. Tout chiffre repris dans un préenregistrement ou un papier doit citer la page `[p.N]` et être relu sur le PDF empreinté. L'extraction en mode mise en page peut mal ordonner formules, tableaux et figures : se reporter au PDF pour tout symbole ou tout chiffre de tableau.

## 4. Les 23 papiers

| Identifiant (version du PDF) | Titre (tel qu'écrit dans le PDF) | Pages | Caractères (fichier intégral) | Empreinte SHA-256 du PDF | Empreinte SHA-256 du fichier intégral | État |
|---|---|---|---|---|---|---|
| arXiv:2412.09565v2 | Obfuscated Activations Bypass LLM Latent-Space Defenses | 51 | 191 970 | `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9` | `3d277d68ad7462f4cf8dc009cb5793e0831e7b123c59489e963ae21da8b0b62e` | extrait |
| arXiv:2510.09462v2 | Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols | 52 | 212 174 | `96c16e33b27b9633b324acecfe29e1bfa9de7052143fb854824aad70a649d7f7` | `5cc0c2ef9bd09501ce75315624b2e46d7ccd2b97056231dc6918c384b57d679b` | extrait |
| arXiv:2601.20022v2 | Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary | 34 | 206 663 | `8d090f3171ef76cad597ab263a2de9df49de1d1accf78a8afff55ceb82881b42` | `546dd40dbf8438a56913aa8fa0eb88232cf16a3de853fb92ebce5526e2380116` | extrait |
| arXiv:2602.14161v2 | When Benchmarks Lie: Evaluating Malicious Prompt Classifiers Under True Distribution Shift | 27 | 92 210 | `7831c848841eca32bcbb1e18cd35f644cfe5a8af8f0f003623c4e1bdd6e03c00` | `7c72771e832b481f8c7f6c91d663c7ea08b2a1be84d657861774061a36e986c7` | extrait |
| arXiv:2605.09684v1 | MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring | 63 | 200 039 | `35bb09b49f85578e4cfddeec16c9ae101a51b5d618196a4b29a1722b89b831f5` | `681cab7625539b4dac10d1eb12e82d61d23ac612883451bc911cc52dc87d695b` | extrait |
| arXiv:2605.16626v2 | SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors | 42 | 196 618 | `1ba418227095eeea98881f61a606c9974f4f3a8758d6a6292c6a9cd8bbd76751` | `263968ac06222ffa1707af8bbc30e59aa1b3590736a9b5eb49bd721781f1b70a` | extrait |
| arXiv:2606.08892v2 | Diffuse AI Control on Fuzzy Tasks | 71 | 294 995 | `aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a` | `5872d2636ab166cf716c57937888d38f9930c3c14aea74ae472011499485ee2e` | extrait |
| arXiv:2607.02514v2 | Distributed Attacks in Persistent-State AI Control | 35 | 122 074 | `9baceea4719a5ff2d63c3278d425a0c3b9feeb2d447a19a3cd7a6b62d3339c22` | `7e1140835425a9ba9b63f1bc47accf10457df145707aeb4ba75687770d668323` | extrait |
| arXiv:2607.07368v1 | Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors | 81 | 349 980 | `d72cae4337e824e4af9eb84759775f6c5dc704f157a0d302df1b44538eb159cd` | `1816a5b91b2ad0ed021d790160a83449403341db93f5a62ecaa2927bc2b3f94f` | extrait |
| arXiv:2610.12445v1 | Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception | 98 | 448 101 | `7e1417580c4ee269c9b7d6b5e9acd6a4027e820a34710e381a946fe7b5e3e11a` | `425afd4ec0084922b035b8703c909b3f01e9dde161e2366fcc9d23275a0aaedb` | extrait |
| arXiv:2603.00829v2 | Constitutional Black-Box Monitoring for Scheming in LLM Agents | 36 | 160 914 | `d8ffcbd352abd9c6bd9aeb1ded6d337689ae980980960fdd8de12bd3d1fd775d` | `7937ecc06b8092e79d868b172870117b0bea4669bdc474913d2b57b148596c25` | extrait |
| arXiv:2603.19461v1 | Hyperagents | 60 | 250 045 | `92f9a73b43699c08c6000f7d4f1b68bec9fd872d217467fe4a1127e2f7981f1e` | `13c37ec8865e07c4f3e7d3fe443758dba183ffad56f871aa4363e5177c085f85` | extrait |
| arXiv:2605.13411v1 | EvoSafety: Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution | 48 | 162 673 | `a81514c51c33b6f8def74bb6df11c5f733cfe256bbc21768f607a3dc0e0029c0` | `79ee3a1dc61964409669e87610e4ba3dabb6b1f80f01b5853812bf5ff657c7c7` | extrait |
| arXiv:2605.31140v1 | EvoDefense: Co-Evolving Black-Box Defense with Large Language Models | 17 | 110 861 | `29c8ffd960d8ece9df75eb95329afc23509729e904819dbafb5d90d24305367a` | `3430d8c2031871fcf509c15d13168f5457d7a95758be9e1f8eabfc6d53ac4282` | extrait |
| arXiv:2609.17560v1 | Pay Only for Disagreement: Certified No-Regression Verdicts for Model Updates with Matching Label-Complexity Bounds | 31 | 109 732 | `ef318a961de7d5f237b7bdca063b7441d3cab00522bc0e6baec383603af2d11f` | `9fca30ac1aadeb39d7194b94e139792947d2c54e39244279d00091060a3fd46f` | extrait |
| arXiv:2609.32267v1 | When Can Old Evaluations Certify a New Model? Label-Efficient Release Decisions under Evaluator Drift | 27 | 133 997 | `8654e1185de1b3160eb4d30d50d5bcf428e41e5439f868fad58ef1849bf1a118` | `664594fbaefed680b27420a8218081f6327946c60e63e508e8da900fc7ab427b` | extrait |
| arXiv:2609.36580v2 | SafeCoEvo: Co-Evolving Safety Harnesses and Guards for LLM Agents at Test-Time | 35 | 118 234 | `e0df2463da8c5a9aaaa819d79f08606618f3318823a0cc78f9ecbcf940a05d3a` | `2e54934d84944b714e6baa4cc6de10f78bb29215cbcda6879371778633e782fc` | extrait |
| arXiv:2610.19422v1 | AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety | 25 | 105 623 | `4812c7037c4c4363f4fe7ebbcf027e2f286341446dbd503e20bd8a4b72715bac` | `c86f7b9ef907b1a9b326c64888cf948f9f5b5b16c4152af78a397f42fa5d07f7` | extrait |
| arXiv:2509.17778v1 | Quickest Change Detection in Continuous-Time in Presence of a Covert Adversary | 4 | 37 548 | `97d000252b768e69113437cce1a88a24488cbe3f92a1a724ea39c0c9f87d8d5e` | `1b9e14747688445fb0939e3ff61aa7ecc8d3b6d921089dd7babe0f22615c7461` | extrait |
| arXiv:2511.17408v4 | The Impact of Off-Policy Training Data on Probe Generalisation | 56 | 226 058 | `91e00c25f356db80a0073d32d7d774e71b64de13767983d85ec4bb0fcadb2357` | `ab2dbd5e25ba88331e2d42db41bbadb033f37f9fa9ef519108f7bb32b85efbe1` | extrait |
| arXiv:2601.19726v1 | RvB: Automating AI System Hardening via Iterative Red-Blue Games | 15 | 108 395 | `53a465a479fc1887e724b424a749910eb09251be49c966a5a639c65d890e7e44` | `b9d1c550a1a6002ad297365f201891428ccdeb911d27f5e4419c55f79afd2264` | extrait |
| arXiv:2602.01539v2 | MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety | 40 | 151 241 | `793d32725d82e364f0ecbb0be994694d2aca20f8daf8391e6583be58f067540e` | `54b246944f0c50cd890037d03d7d1ebb9dcc045f516bb0aec8e42c59a6ed612c` | extrait |
| arXiv:2606.08106v1 | PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents | 12 | 45 254 | `779f49607688fd06226d4390ad6e0c4c8356ef75b87243fd734181cef700934f` | `e667d8468b320b7743bfb995420c10ff11a8fb8123e9cf92bbf488f2693bdab8` | extrait |

Bilan : **23 extraits, 0 refusé, 0 PDF absent**.

## 5. Total de caractères et différence avec les extraits v1 à v4

Caractères = caractères du fichier lu en utf-8 (en-tête compris), avant le caviardage de la course.

- Total des 23 fichiers intégraux : **4 035 399** caractères (texte seul, hors en-têtes : 4 003 226).
- Total des 23 extraits v1 à v4 qu'ils remplacent : **557 150** caractères.
- Caractères gardés en plus : **3 478 249** (environ ×7.2).

| Papier | Extrait v1 à v4 (caractères du fichier) | Fichier intégral | Gardés en plus |
|---|---|---|---|
| arXiv:2412.09565v2 | 24 098 | 191 970 | 167 872 |
| arXiv:2510.09462v2 | 24 747 | 212 174 | 187 427 |
| arXiv:2601.20022v2 | 23 840 | 206 663 | 182 823 |
| arXiv:2602.14161v2 | 24 567 | 92 210 | 67 643 |
| arXiv:2605.09684v1 | 24 551 | 200 039 | 175 488 |
| arXiv:2605.16626v2 | 24 333 | 196 618 | 172 285 |
| arXiv:2606.08892v2 | 24 667 | 294 995 | 270 328 |
| arXiv:2607.02514v2 | 24 941 | 122 074 | 97 133 |
| arXiv:2607.07368v1 | 24 742 | 349 980 | 325 238 |
| arXiv:2610.12445v1 | 24 892 | 448 101 | 423 209 |
| arXiv:2603.00829v2 | 24 897 | 160 914 | 136 017 |
| arXiv:2603.19461v1 | 24 760 | 250 045 | 225 285 |
| arXiv:2605.13411v1 | 24 970 | 162 673 | 137 703 |
| arXiv:2605.31140v1 | 24 761 | 110 861 | 86 100 |
| arXiv:2609.17560v1 | 24 510 | 109 732 | 85 222 |
| arXiv:2609.32267v1 | 23 447 | 133 997 | 110 550 |
| arXiv:2609.36580v2 | 24 344 | 118 234 | 93 890 |
| arXiv:2610.19422v1 | 23 672 | 105 623 | 81 951 |
| arXiv:2509.17778v1 | 18 024 | 37 548 | 19 524 |
| arXiv:2511.17408v4 | 24 865 | 226 058 | 201 193 |
| arXiv:2601.19726v1 | 24 538 | 108 395 | 83 857 |
| arXiv:2602.01539v2 | 24 383 | 151 241 | 126 858 |
| arXiv:2606.08106v1 | 24 601 | 45 254 | 20 653 |
| **Total (23)** | **557 150** | **4 035 399** | **3 478 249** |

## 6. Liste blanche v7 et tailles

- `liste-blanche-v7.txt` : les 40 fichiers de la liste blanche v5 (`ideation-organisme-approches-v1/liste-blanche-sans-temoins-v5.json`, 40 entrées), les 23 extraits v1 à v4 étant tous remplacés par leur fichier intégral, à la même place. 40 fichiers. Un chemin absolu par ligne. (`liste-blanche-v6.txt`, à dix remplacements, reste scellée telle quelle.)
- `tailles-v7.txt` : caractères par fichier et total. Total de la liste v5 : 743 537 ; total de la liste v7 : **4 221 786**.
- Les plafonds de la course (`--taille-max-pieces`, 750 000 par lot ; plafond dur 800 000) sont dépassés, y compris par le seul total des 23 fichiers intégraux (4 035 399). Aucune décision n'est prise ici : le total est donné.
- La liste v7 est une liste de fichiers à lire ; elle n'est pas un document scellé de liste blanche de la course (la liste v5 est un `.json` empreinte-par-chemin, que ce dossier ne modifie pas).

## 7. Doutes de l'extraction (aucun jugement sur le contenu)

- Pages sans texte extractible (figures en image, pas de reconnaissance de caractères) : 2605.09684v1 p.34 et p.35 (figures 14 à 17, légendes seules). Le texte contenu dans les images de figures n'est extrait pour aucun papier. 2610.12445v1 p.61 : page courte, texte présent. Aucune page de moins de 200 caractères parmi les treize papiers ajoutés.
- Polices de figures codées, texte de figure illisible : 2510.09462v2 pages 2, 5, 6, 7, 18, 22 (2 975 caractères de contrôle) ; 2601.19726v1 pages 5 et 6 (446 caractères de contrôle). Dans 2510.09462v2 l'outil émettait en outre des sauts de page parasites, d'où l'extraction page par page (52 pages, comme `pdfinfo`).
- Caractères de contrôle par papier (remplacés par U+FFFD, nuls supprimés) : voir la table ci-dessous ; formules extraites en texte linéaire, parfois dans le désordre.
- Mise en page : une seule colonne à l'échantillon ; le mode `-layout` garde des indentations larges et des trous dans les tableaux, ce qui gonfle le nombre de caractères. Les titres en petites capitales sortent espacés dans 2602.14161v2 et 2510.09462v2.
- 2607.07368v1 : les rapports le citent sous le nom de Makins et al. ; premier auteur du PDF : Angelini. 2610.12445v1 : `pdftotext` signale « Mismatch between font type and embedded font file » (avertissement de police, texte extrait).
- Titre de 2603.19461v1 : « Hyperagents » (titre du PDF). Les titres des treize papiers ajoutés ont été vérifiés dans la page 1 du PDF.
- Aucun PDF scanné parmi les 23.

| Papier | Caractères de contrôle | Pages (nombre) |
|---|---|---|
| arXiv:2510.09462v2 | 2975 | 2 (230), 5 (505), 6 (462), 7 (151), 18 (400), 22 (1227) |
| arXiv:2601.20022v2 | 298 | 4 (1), 6 (4), 10 (4), 11 (6), 12 (4), 13 (2), 14 (8), 15 (32), 16 (14), 17 (6), 18 (6), 19 (34), 20 (24), 21 (16), 22 (20), 24 (40), 25 (17), 27 (6), 28 (4), 29 (21), 31 (16), 32 (12), 33 (1) |
| arXiv:2602.14161v2 | 1 | 5 (1) |
| arXiv:2605.09684v1 | 2 | 22 (2) |
| arXiv:2606.08892v2 | 1 | 14 (1) |
| arXiv:2607.07368v1 | 28 | 45 (2), 61 (1), 62 (6), 64 (9), 65 (8), 66 (2) |
| arXiv:2610.12445v1 | 2 | 17 (2) |
| arXiv:2603.19461v1 | 3 | 23 (2), 36 (1) |
| arXiv:2605.13411v1 | 35 | 5 (2), 6 (2), 7 (6), 23 (3), 30 (20), 31 (2) |
| arXiv:2605.31140v1 | 2 | 5 (2) |
| arXiv:2609.17560v1 | 32 | 3 (1), 7 (2), 8 (1), 10 (7), 12 (1), 13 (1), 22 (1), 23 (6), 24 (6), 25 (5), 26 (1) |
| arXiv:2609.32267v1 | 15 | 4 (2), 5 (5), 6 (2), 15 (1), 17 (3), 18 (2) |
| arXiv:2509.17778v1 | 12 | 2 (1), 3 (11) |
| arXiv:2511.17408v4 | 4 | 2 (4) |
| arXiv:2601.19726v1 | 446 | 5 (282), 6 (164) |
| arXiv:2606.08106v1 | 2 | 4 (1), 5 (1) |

## 8. Fichiers du dossier

`integral-<identifiant><version>.md` (23) ; `liste-blanche-v6.txt`, `tailles-v6.txt`, `LISEZMOI-v1.md` (v1, intacts) ; `liste-blanche-v7.txt`, `tailles-v7.txt`, ce `LISEZMOI-v2.md` ; chaque fichier a son empreinte compagnon `.sha256` (R6).
