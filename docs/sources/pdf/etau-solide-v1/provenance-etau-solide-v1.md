# Provenance des PDF — rendre l'étau solide, ou s'en passer — v1

- **Pour** : la note `docs/notes/pince-hors-distribution-v1/etau-solide-v1/reponse-fable-etau-solide-v1.md` (demande du directeur du 21 novembre 2026, GO-2026-11-21-53). Pièce de travail (classe C).
- **Téléchargés** le 2026-11-21 entre 13:12 et 13:20 UTC (`date -u`), sans compte ni clé, par un client générique (aucun nom du programme ni chemin interne dans les requêtes) : arXiv par `export.arxiv.org`, dernière version au jour du téléchargement ; titre, auteurs et dates rendus par l'interface d'arXiv.
- **Table écrite par programme** (`pdfinfo`, SHA-256 recalculé sur le fichier), le 2026-11-21T13:23:45Z ; pour chaque PDF versé, l'empreinte est comparée à celle relevée au téléchargement (assertion).
- **« Pages lues »** : pages dont le texte extrait (`pdftotext`) a été lu par l'auteur de la note, en entier ou par recherche de motifs ; rang de la page dans le fichier, non folio imprimé. Aucun PDF lu en entier ; aucune figure regardée : un chiffre qui n'existe que dans une figure n'est pas cité. Les pages non listées n'ont pas été lues.
- **Ce qui est opposable (R7)** : les phrases et chiffres cités dans la note, à la page citée, pour la version dont l'empreinte est donnée ici.

## PDF versés dans ce dossier

| fichier | pages | octets | SHA-256 | titre ; auteurs | source ; version | pages lues |
|---|---|---|---|---|---|---|
| `1705.07263v2.pdf` | 12 | 2619029 | `80623126b569da46ac487c4d631dbd93f7c4916396eb45a18865ed529a66e3b7` | Adversarial Examples Are Not Easily Detected: Bypassing Ten Detection Methods ; Nicholas Carlini, David Wagner | arXiv 1705.07263 v2 (première version 2017-05-20, cette version 2017-11-01), export.arxiv.org | 1 |
| `2006.00995v3.pdf` | 15 | 718851 | `c181d74843b59d7ea92f145f6a8b46ce978324d21b213394565efad1aa8814b8` | Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals ; Yanai Elazar, Shauli Ravfogel, Alon Jacovi, Yoav Goldberg | arXiv 2006.00995 v3 (première version 2020-06-01, cette version 2021-02-19), export.arxiv.org | 1 |
| `2106.02997v2.pdf` | 26 | 1353222 | `32bb7dea66595065c54b4f8d210d76e6b5fc7d53f8b211c6495b657903e8f219` | Causal Abstractions of Neural Networks ; Atticus Geiger, Hanson Lu, Thomas Icard, Christopher Potts | arXiv 2106.02997 v2 (première version 2021-06-06, cette version 2021-10-27), export.arxiv.org | 1 |
| `2306.03819v4.pdf` | 22 | 766987 | `0e748cfc8d0a9d630d18b63d8126bcc0346dc339ca8a690b9322803fc9a78d86` | LEACE: Perfect linear concept erasure in closed form ; Nora Belrose, David Schneider-Joseph, Shauli Ravfogel, Ryan Cotterell, Edward Raff, Stella Biderman | arXiv 2306.03819 v4 (première version 2023-06-06, cette version 2025-04-03), export.arxiv.org | 1, 2 ; 7 à 10, 16 (par motifs) |
| `2308.15605v5.pdf` | 61 | 2711769 | `77f4c0472800318eac13439375888ef8c0f284324d61204e04b49c9babd2dcea` | Benchmarks for Detecting Measurement Tampering ; Fabien Roger, Ryan Greenblatt, Max Nadeau, Buck Shlegeris, Nate Thomas | arXiv 2308.15605 v5 (première version 2023-08-29, cette version 2023-09-29), export.arxiv.org | 1 |
| `2401.06102v4.pdf` | 25 | 1991817 | `e6a418bc435cd8fb91481ec2c19492998d833d0310c211d511f22cdfa9c5fa48` | Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models ; Asma Ghandeharioun, Avi Caciularu, Adam Pearce, Lucas Dixon, Mor Geva | arXiv 2401.06102 v4 (première version 2024-01-11, cette version 2024-06-06), export.arxiv.org | 1 |
| `2405.19550v1.pdf` | 25 | 1451970 | `ae7243da8e4ea849a09ed6bb464ff5bd76969f18401fa020514bb75e475ccaae` | Stress-Testing Capability Elicitation With Password-Locked Models ; Ryan Greenblatt, Fabien Roger, Dmitrii Krasheninnikov, David Krueger | arXiv 2405.19550 v1 (première version 2024-05-29, cette version 2024-05-29), export.arxiv.org | 1 |
| `2507.05246v1.pdf` | 70 | 1977365 | `bc69d8511ee2a11b0cdb21ed417c93f14e1732ac4935b1dfc82b5d568672f825` | When Chain of Thought is Necessary, Language Models Struggle to Evade Monitors ; Scott Emmons, Erik Jenner, David K. Elson, Rif A. Saurous, Senthooran Rajamanoharan, Heng Chen… | arXiv 2507.05246 v1 (première version 2025-07-07, cette version 2025-07-07), export.arxiv.org | 1 |
| `2512.07404v3.pdf` | 13 | 992963 | `368693aa08415721415ae4f9fca03fce1012ed8863ef29ffc55e629f994d802c` | On LLMs' Internal Representation of Code Correctness ; Francisco Ribeiro, Claudio Spiess, Prem Devanbu, Sarah Nadi | arXiv 2512.07404 v3 (première version 2025-12-08, cette version 2026-01-21), export.arxiv.org | 1 |
| `2512.15674v2.pdf` | 38 | 1337804 | `735c75c9361da456e1c16ef2be69d596392e5d898a003ee4cef7c9ed99252bca` | Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers ; Adam Karvonen, James Chua, Clément Dumas, Kit Fraser-Taliente, Subhash Kantamneni, Julian Minder… | arXiv 2512.15674 v2 (première version 2025-12-17, cette version 2026-01-06), export.arxiv.org | 1 |
| `2602.00750v2.pdf` | 8 | 470552 | `cf0bd3653fdc8a1f83b45fe45a77ca806a6ac0c7e673aa55c05960f31e209bf7` | Bypassing Prompt Injection Detectors through Evasive Injections ; Md Jahedur Rahman, Ihsen Alouani | arXiv 2602.00750 v2 (première version 2026-01-31, cette version 2026-04-01), export.arxiv.org | 1 |
| `2603.04069v1.pdf` | 14 | 963648 | `4c035a3c362fbaa36ba8ad1127249566e216d8ccb567f0375707d409e139895f` | Monitoring Emergent Reward Hacking During Generation via Internal Activations ; Patrick Wilhelm, Thorsten Wittkopp, Odej Kao | arXiv 2603.04069 v1 (première version 2026-03-04, cette version 2026-03-04), export.arxiv.org | 1 (titre vérifié ; non cité au-delà) |
| `2604.13068v2.pdf` | 17 | 1147226 | `ce543dad5d6a729a97b2f49a7c12f610d400272f209a2de4966901459befaaa1` | Detection Without Correction: A Robust Asymmetry in Activation-Based Hallucination Probing ; Dip Roy, Rajiv Misra, Sanjay Kumar Singh, Anisha Roy | arXiv 2604.13068 v2 (première version 2026-03-20, cette version 2026-05-09), export.arxiv.org | 1 |
| `2606.11998v1.pdf` | 25 | 1562646 | `89ed2dfcebf6dd47dc93007d33d5612b783d14ee046a524e53868975a006cb6e` | Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents ; Frank Xiao, Mary Phuong | arXiv 2606.11998 v1 (première version 2026-06-10, cette version 2026-06-10), export.arxiv.org | 1 (titre vérifié ; non cité : identifiant mal attribué par le moteur) |
| `2608.08266v1.pdf` | 14 | 669835 | `fb4b56dc4673e5cd929a22750334f563d3e5416267ac4bb7e47175b229a99361` | On the Robustness of LLMs' Internal Representation of Code Correctness ; Francisco Ribeiro, Sohaila Abdulsattar, Renata Gonzalez, Mahmoud Kassem, Sarah Nadi | arXiv 2608.08266 v1 (première version 2026-08-08, cette version 2026-08-08), export.arxiv.org | 1 |
| `2609.18080v1.pdf` | 18 | 1553009 | `ef79c76498865c52663ac9ee8e0003fa1a5e556ebc4cf08b9035f85fcf3d48b7` | Decodability is Not Causality: Dissociating Probe Readouts from Behavioral Drivers via SAE Decomposition ; Devesh Tiwari, Camille Davis, Shivank Sinha, Talia Weaver, Aditya Shah, Maheep Chaudhary | arXiv 2609.18080 v1 (première version 2026-09-16, cette version 2026-09-16), export.arxiv.org | 1 |
| `2610.15883v1.pdf` | 15 | 363271 | `c367ab7e9c89db0df6c64696e5830dbfb4a44c60dd02802394f5b27f8619807f` | What the Model Cannot See: Covert and Provable Text Invisibility in LLMs ; Mark Russinovich | arXiv 2610.15883 v1 (première version 2026-10-11, cette version 2026-10-11), export.arxiv.org | 1 ; 5, 10, 11 (par motifs) |
| `2610.18105v1.pdf` | 61 | 2772121 | `d6174bd1032bc70b2a4c53a88695855c5b04f2318a85c5b22a5d91f4e7b998d5` | Chain of Thought Monitoring Can Fail Even When CoT Is Necessary ; Lennart Bürger, Piotr Komorowski, Moritz Weckbecker, Evgenii Kortukov, Aakriti Jain, Sebastian Lapuschkin… | arXiv 2610.18105 v1 (première version 2026-10-13, cette version 2026-10-13), export.arxiv.org | 1 |

## PDF déjà au dépôt, relus ce jour (non reversés)

| chemin sous `docs/sources/pdf/` | pages | SHA-256 | pages lues |
|---|---|---|---|
| `2412.09565v2.pdf` | 51 | `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9` | 1 à 4, 22 à 24 ; 25, 26 (par motifs) |
| `2512.11949v1.pdf` | 30 | `e0f8ddfff6e75d835995886a630a5d077ed871c28599f710b41c96efc949e3ee` | 1 à 3 ; 4 à 8, 11 (par motifs) |
| `2412.01784v3.pdf` | 33 | `7fbe44ec6d764951f76d94f8d52cfcb7db89f1a130526462c46afc3f626d11a2` | 1, 2 ; 10 (par motifs) |
| `2611.14950v1.pdf` | 14 | `6396abd53a24b457519a4f5e5d669a74e1a91cce9a6e5b6b4175821ad3ab94d6` | 1, 2 |
| `mecanisme-adjudant-v1/2307.09476v3.pdf` | 39 | `f58b18ba38cea49b751a61cb5e3d8f1876f291854568502a1cf2ecb778b0b433` | 1 |
| `mecanisme-adjudant-v1/2303.08112v6.pdf` | 25 | `641bbdb6e070ace8c029d19f536cab67fa928d2b56af621482a42a0c3c349faa` | 2, 9, 10 (par motifs) |
| `2506.14261v4.pdf` | 24 | `4b0960622664e77d888974955b29f9c0e5913266392caeecac2b844f011e244c` | 1 ; 2, 8 (par motifs) |
| `2602.15515v2.pdf` | 30 | `f6547ec830104abf8ceca353e46e32ee78453f6470fd1c03053e13834ebc54cb` | 1, 2 (début) |
| `2512.07810v1.pdf` | 77 | `77e64bcd88754f506890ee99dc5672284145a8705d27c5a63e4fc47330d28c8f` | 1 |
| `2405.05466v2.pdf` | 22 | `aa781893236e877a8f63e22249e77f454c8df6e2d82018fff3ca99456ad782c4` | 1 ; 2 (par motifs) |
| `2411.03336v2.pdf` | 46 | `46b4901a0f0c2a63ae90247b611b619fc9ca22d4129bdfdf5608e9148c4bca7e` | 44, 45 ; 12, 14, 25 (par motifs) |
| `anteriorite-P-041-v2/complement-2/2606.09411.pdf` | 28 | `3b8158a527301d3c6cbbe6e0efea66511440492a54db517013d63a061fe6b830` | 1, 2 |
| `mecanisme-adjudant-v1/2505.14300v2.pdf` | 36 | `01dc8a2a0ab0760dd3cd900640cada1ae33f297e9941e344ee5dd69276cb9462` | 1 |
| `mecanisme-adjudant-v1/2603.23171v3.pdf` | 17 | `da05ddb74da85325b9c06c78dec3e0a72b1b500cc702c77a222e2d3f3d268ff0` | 1 |
| `2605.27958v1.pdf` | 18 | `43f55118822b378d950255b10aa68379fdb24a1431bba7e8721aacaf44d856e0` | 1 |
| `2509.21344v2.pdf` | 33 | `aaac4ff91c909f9e4363fe9c19bb0fc7c2a635bf91e13c178992411f2a25ee5c` | 1 |
| `2507.12691v3.pdf` | 39 | `0c00a77b0c07bb9a8cd2feb748d65fe9ac01ee7bee9746ebb9cbc0d1ca8ebb00` | 1 |
| `anteriorite-P-041-v2/c2/1802.00420v4.pdf` | 12 | `70e6dfea92070bfbbda98bfeff804db3302c4b77411cef098e5d16c466474a27` | 1 |
| `adjudant-opus-independant-v1/2010.09686v7.pdf` | 70 | `d783b1200025fbdf89b0edf718c19712c1e7acfec263a4b07a68609b4d7ac4ef` | 1 |

## Non obtenus sur PDF (non opposables)

- « When Monitors Fail, the Model Still Knows: Probing Obfuscated Reasoning in LLMs » (conférence ICML 2026, page de la conférence et forum OpenReview `eckQoUDCSm`) : le téléchargement du PDF a été refusé (code 403) ; connu par la seule page de la conférence, lue par un outil qui résume.
- Trois billets de forum (LessWrong), connus par les seuls résultats du moteur : un modèle jouet de l'obscurcissement d'activations ; « neural chameleons can('t) hide from activation oracles » ; « models trained to evade topic probes struggle to answer ».
