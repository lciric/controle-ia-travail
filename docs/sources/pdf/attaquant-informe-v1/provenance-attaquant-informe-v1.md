# Provenance des PDF — le côté de l'attaquant informé — v1

- **Pour** : la note `docs/notes/attaquant-informe-v1/reponse-fable-attaquant-informe-v1.md` (six questions du directeur du 21 novembre 2026, GO-2026-11-21-51). Pièce de travail (classe C).
- **Téléchargés** le 2026-11-21 entre 12:57 et 13:02 UTC (`date -u`), sans compte ni clé, par un client générique (aucun nom du programme ni chemin interne dans les requêtes), depuis `export.arxiv.org` ; dernière version au jour du téléchargement. Titre, auteurs et version lus sur la première page du PDF (tampon d'arXiv), non sur l'interface d'arXiv.
- **Table écrite par programme** (`pdfinfo`, SHA-256 recalculé sur le fichier), le 2026-11-21T13:03:39Z ; pour les PDF déjà au dépôt, l'empreinte recalculée est comparée à celle du compagnon `.sha256` (assertion).
- **« Pages lues »** : pages dont le texte extrait (`pdftotext -layout`) a été lu par l'auteur de la note, en entier ou par recherche de motifs ; rang de la page dans le fichier, non folio imprimé. Aucun PDF lu en entier ; aucune figure regardée (les légendes sont lues comme texte). Les pages non listées n'ont pas été lues.
- **Ce qui est opposable (R7)** : les phrases et chiffres cités dans la note, à la page citée, pour la version dont l'empreinte est donnée ici.

## PDF versés dans ce dossier

| fichier | pages | octets | SHA-256 | titre ; auteurs | source ; version | pages lues |
|---|---|---|---|---|---|---|
| `2610.37055v1.pdf` | 23 | 593647 | `5250fa1176ac804ba32fd4998fa47b2f278757ce9393a1443d4b9a7b8617f861` | Blindfold: Keeping the Audit Coin Secret from LLM Agents ; Wei Zhu, Meiyun Zuo, Huiping Sun | arXiv 2610.37055 v1 (tampon de la première page : 27 octobre 2026), export.arxiv.org | 1, 2 ; 3, 10, 12, 16, 19 (par motifs) |
| `2505.13763v2.pdf` | 36 | 18023167 | `b878d094ed08fbc2e0dcdbde0ec3473eec2c8dcdfdadf2c227e7f85ef57ce899` | Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations ; Li Ji-An, Hua-Dong Xiong, Robert C. Wilson, Marcelo G. Mattar, Marcus K. Benna | arXiv 2505.13763 v2 (tampon : 24 octobre 2025), export.arxiv.org | 1 ; 2, 4, 6 (par motifs) |
| `2505.23836v3.pdf` | 31 | 1427660 | `964c793edab708ab677051f8fad19357e83d6f0034ddbe1ff8e842319e7d1d0f` | Large Language Models Often Know When They Are Being Evaluated ; Joe Needham, Giles Edkins, Govind Pimpale, Henning Bartsch, Marius Hobbhahn | arXiv 2505.23836 v3 (tampon : 16 juillet 2025), export.arxiv.org | 1 |
| `2609.38262v1.pdf` | 49 | 385887 | `e28a4e8d6747cf4dc4c0c3433836f5e29b1ab5e235be3176841ee9c4db4ed7a7` | When Does Randomized Oversight Align AI Agents That Can Conceal? ; Joshua S. Gans, Richard Holden | arXiv 2609.38262 v1 (tampon : 29 septembre 2026), export.arxiv.org | 1, 2 |

## PDF déjà au dépôt, relus ce jour aux pages dites

| chemin | pages | SHA-256 (recalculé, égal au compagnon) | référence | pages relues |
|---|---|---|---|---|
| `docs/sources/pdf/2412.09565v2.pdf` | 51 | `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9` | Bailey et al., Obfuscated Activations Bypass LLM Latent-Space Defenses | 1-3 ; 4, 5, 6, 7, 9, 22-24, 29 (par motifs ou en partie) |
| `docs/sources/pdf/2512.11949v1.pdf` | 30 | `e0f8ddfff6e75d835995886a630a5d077ed871c28599f710b41c96efc949e3ee` | McGuinness et al., Neural Chameleons | 1-3 ; 4, 6-9, 11, 23 (par motifs) |
| `docs/sources/pdf/2611.14950v1.pdf` | 14 | `6396abd53a24b457519a4f5e5d669a74e1a91cce9a6e5b6b4175821ad3ab94d6` | Soopal et al., Stress-Testing Sandbagging Detection Under Adaptive Attack | 1, 2 ; 3, 5, 8, 10 (par motifs) |
| `docs/sources/pdf/mecanisme-adjudant-v1/2606.06529v1.pdf` | 19 | `6042d449d1ae11c7441e8f653675883b352ddafd8389af4a876d77919d6f7f4e` | Ge-Wang et al., Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety | 1, 2 ; 4, 5, 7, 8, 11 (par motifs) |
| `docs/sources/pdf/2602.00986v2.pdf` | 25 | `da004f53ff336b950bf51fb9a85fa424f5792579ac10dce45566ccb0e68e9039` | Xu, Yuksekgonul, Zou, Sparse Reward Subsystem in Large Language Models | 1, 5 ; 2, 4 (par motifs) |
| `docs/sources/pdf/2504.10374v1.pdf` | 38 | `5f802d679344fe5e15d1edd50e96245f3bdc054e69d1ff0880b077d173549211` | Bhatt et al., Ctrl-Z: Controlling AI Agents via Resampling | 1 ; 2, 4, 5, 6 (par motifs) |
| `docs/sources/pdf/2607.13087v1.pdf` | 36 | `291a0cd72b0b6a0f08882db7080bba9f8a24ee196ae2f69f5063314cbfddeb55` | Phuong et al., GDM AI Control Roadmap | 1 |
| `docs/sources/pdf/2412.01784v3.pdf` | 33 | `7fbe44ec6d764951f76d94f8d52cfcb7db89f1a130526462c46afc3f626d11a2` | Tice et al., Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models | 1 |
| `docs/sources/pdf/2405.05466v2.pdf` | 22 | `aa781893236e877a8f63e22249e77f454c8df6e2d82018fff3ca99456ad782c4` | Clymer, Juang, Field, Poser | 1 ; 2, 6 (par motifs) |
| `docs/sources/pdf/2506.14261v4.pdf` | 24 | `4b0960622664e77d888974955b29f9c0e5913266392caeecac2b844f011e244c` | Gupta, Jenner, RL-Obfuscation | 1 |
| `docs/sources/pdf/2510.09462v2.pdf` | 52 | `96c16e33b27b9633b324acecfe29e1bfa9de7052143fb854824aad70a649d7f7` | Terekhov et al., Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols | 1 |
| `docs/sources/pdf/2511.02997v1.pdf` | 31 | `1dcffc4983b07b989be8d8534ba38aae587722901e527fa1e37961aba18cd0e0` | Kutasov et al., Evaluating Control Protocols for Untrusted AI Agents | 1 ; 5 (par motifs) |
| `docs/sources/pdf/2605.26047v2.pdf` | 46 | `947724f42324070fd47b1ecaf8c1bf9b2257df0e0c7f8822447241d3ea9a28fa` | Lucassen, Kaufman, Retrying vs Resampling in AI Control | 1 |
| `docs/sources/pdf/2411.17693v1.pdf` | 44 | `13a93a48dcb373595709da1096984d308cd3cd17c3bf00602944a24abcc2c627` | Wen et al., Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats | 1 |
| `docs/sources/pdf/2604.13301v1.pdf` | 8 | `fc09ad6f0202284a8e99009252da573274393c69fcc22b9022ba8fdd07ef5cd3` | Hasan, Honeypot Protocol | 1 |
| `docs/sources/pdf/2606.08892v2.pdf` | 71 | `aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a` | Terekhov et al., Diffuse AI Control on Fuzzy Tasks | 1 |
| `docs/sources/pdf/2602.15515v2.pdf` | 30 | `f6547ec830104abf8ceca353e46e32ee78453f6470fd1c03053e13834ebc54cb` | Taufeeque et al., The Obfuscation Atlas | 1 |
| `docs/sources/pdf/2609.36490v1.pdf` | 25 | `eb6d5bbe9bfaff0ac4fbac948a7bd9937721721fc558655fdf606d254421a088` | Lyons Keenan, Leckie, Erfani, LLMs Learn to Evade Latent Monitors from Prior Feedback Alone | 1 ; 3, 6-9, 19 (par motifs) |
| `docs/sources/pdf/2312.06942v5.pdf` | 47 | `999f7a92bb8c085799e68f3d88f491ad8a334f862ccf5b286e5c2766677864c0` | Greenblatt et al., AI Control: Improving Safety Despite Intentional Subversion | 7, 8 (par motifs) |
| `docs/sources/pdf/percee-controle-securite-v1/2605.29729v2.pdf` | 23 | `5aec016a9ee320d762db6fc3d9a5ec6bf5ac98f917b87fcbec62161645caca62` | Krakovna et al., Realistic honeypot evaluations for scheming propensity | 1 |
| `docs/sources/pdf/anteriorite-P-041-v2/c5/2602.04930v2.pdf` | 25 | `f4d9222a4b94f99cf6c33b3a95fdaf8a7ac28cfbd3c16156dfc96d80309e266a` | Schaeffer, Khandelwal, Tracy, Attack Selection Reduces Safety in Concentrated AI Control Settings against Trusted Monitoring | 1 |
| `docs/sources/pdf/anteriorite-P-041-v2/complement-2/2606.09411.pdf` | 28 | `3b8158a527301d3c6cbbe6e0efea66511440492a54db517013d63a061fe6b830` | Westphal et al., Now You (Still) See Me: Detecting Evasive Steganographic Payloads in LLMs (version 1 au tampon de la première page) | 1 |

## Trois PDF téléchargés ce jour et non versés, car déjà au dépôt à l'octet près

`2605.29729v2`, `2602.04930v2`, `2606.09411v1` : empreinte du téléchargement égale à celle du fichier du dépôt cité ci-dessus (comparaison faite le 2026-11-21 vers 13:05 UTC).

## Résultats de moteur de recherche seulement, pages non ouvertes (non opposables, R7)

- « Hand and Brain: Defenses against Agentic Steganography in Language Models » (page de la conférence ICML 2026).
- « Risk-limiting Financial Audits via Weighted Sampling without Replacement », arXiv 2305.06884.
- « Frontier Models Can Take Actions at Low Probabilities », arXiv 2603.02202.
- arXiv 2602.00750 (détecteur de dérive de tâche, réentraînement augmenté par suffixes).
- « AutoHoney: Automating, Deploying, and Evaluating Scheming Honeypots Across Production Codebases » (pages des conférences ICML et NeurIPS 2026).
- « Probing and Steering Evaluation Awareness of Language Models », arXiv 2507.01786 ; arXiv 2509.13333 ; arXiv 2510.20487 (déjà cité par la décision N-053).
