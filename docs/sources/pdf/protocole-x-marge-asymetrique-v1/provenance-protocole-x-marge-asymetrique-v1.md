# Provenance des PDF — protocole X, la marge asymétrique éprouvée par les expérimentateurs — v1

- **Pour** : la note `docs/notes/protocole-x-marge-asymetrique-v1/reponse-fable-marge-asymetrique-v1.md` (mot du directeur du 21 novembre 2026, GO-2026-11-21-61). Pièce de travail (classe C).
- **Téléchargés** le 2026-11-21 entre 15:35 et 15:38 UTC (`date -u`, heures des fichiers), sans compte ni clé, par un client générique (aucun nom du programme, de personne ni chemin interne dans les requêtes). Titre, auteurs et version lus sur la première page du PDF.
- **Table écrite par programme** (`pdfinfo`, SHA-256 recalculé sur le fichier), le 2026-11-21T15:46:41Z ; pour les PDF déjà au dépôt, l'empreinte recalculée est comparée à celle du compagnon `.sha256` (assertion).
- **« Pages lues »** : pages dont le texte extrait (`pdftotext -layout -f N -l N`) a été lu par l'auteur de la note, en entier ou par recherche de motifs ; **numéro de la page dans le fichier** (celui que rend `pdftotext -f`), non folio imprimé, et non rang d'un segment d'une extraction d'un seul tenant. Aucune figure regardée. Les pages non listées n'ont pas été lues.
- **Ce qui est opposable (R7)** : les phrases et chiffres cités dans la note, à la page citée, pour la version dont l'empreinte est donnée ici.

## PDF versés dans ce dossier

| fichier | pages | octets | SHA-256 | titre ; auteurs | source ; version | pages lues |
|---|---|---|---|---|---|---|
| `2309.00614v2.pdf` | 19 | 593964 | `9de28d79861f1f6e86c3ca4affa2ca73a699afc538c061dd9d19f7570fccefc8` | Baseline Defenses for Adversarial Attacks Against Aligned Language Models ; Neel Jain et al. | arXiv 2309.00614 v2 (tampon : 4 septembre 2023), export.arxiv.org | 1 |
| `2310.03684v4.pdf` | 42 | 1729873 | `1a34863cbec66628ca4abdaee9ca03a1473879496d42716788e018b6ca9aecfb` | SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks ; Alexander Robey, Eric Wong, Hamed Hassani, George J. Pappas | arXiv 2310.03684 v4 (tampon : 11 juin 2024), export.arxiv.org | 1 |
| `2310.18512v2.pdf` | 25 | 1366437 | `f482f2baff935088b53f30b22c0f7805af91a5ff458490b9f5274c2bf871f1ef` | Preventing Language Models From Hiding Their Reasoning ; Fabien Roger, Ryan Greenblatt | arXiv 2310.18512 v2 (tampon : 31 octobre 2023), export.arxiv.org | 1 |
| `2412.12480v4.pdf` | 41 | 946658 | `fb7296c1e25c9cb84ad78496393bb7935069a9f73838c9d0556f4cebcc35c172` | Subversion Strategy Eval: Can language models statelessly strategize to subvert control protocols? ; Alex Mallen, Charlie Griffin, Misha Wagner, Alessandro Abate, Buck Shlegeris | arXiv 2412.12480 v4 (tampon de la première page : 4 avril 2025), export.arxiv.org | 1 |
| `2603.02202v1.pdf` | 34 | 1324274 | `cbc9ebb3691593e387515b4525c4ae519d8caf51949fc9b28a37d24600a84918` | Frontier Models Can Take Actions at Low Probabilities ; Alex Serrano, Wen Xing, David Lindner, Erik Jenner | arXiv 2603.02202 v1 (tampon : 2 mars 2026), export.arxiv.org | 1 ; 2 à 12 (par motifs) |
| `2605.26537v1.pdf` | 14 | 561784 | `cc9326468ae9f78f1716c92fb2c12c036f1939f52b694e03ac78bf39b18c2f16` | Conceptual Steganography ; Zhejian Zhou, Jonathan May | arXiv 2605.26537 v1 (tampon : 26 mai 2026), export.arxiv.org | 1 |
| `pmlr-v306-yulong26a.pdf` | 39 | 2496294 | `8c6ab0bdb88b3a41d5372c84cf25b887958e9cb6ddcde5b4d87dee3dd26cd0b8` | Same Question, Different Lies: Cross-Context Consistency (C³) for Black-Box Sandbagging Detection ; Lin Yulong, Pablo Bernabeu-Pérez, Benjamin Arnav, Lennie Wells, Mary Phuong | actes de la conférence ICML 2026, PMLR 306 (lien « PDF » de la page des actes, dépôt mlresearch/v306) ; pas d'identifiant arXiv trouvé | 1, 3, 8 ; 2, 5, 6, 9, 13, 16, 19 (par motifs) |

## PDF déjà au dépôt, relus ce jour aux pages dites

| chemin | pages | SHA-256 (recalculé, égal au compagnon) | référence | pages relues (numéro dans le fichier) |
|---|---|---|---|---|
| `docs/sources/pdf/2605.26047v2.pdf` | 46 | `947724f42324070fd47b1ecaf8c1bf9b2257df0e0c7f8822447241d3ea9a28fa` | Lucassen, Kaufman, Retrying vs Resampling in AI Control | 1 à 12, en entier |
| `docs/sources/pdf/2504.10374v1.pdf` | 38 | `5f802d679344fe5e15d1edd50e96245f3bdc054e69d1ff0880b077d173549211` | Bhatt et al., Ctrl-Z: Controlling AI Agents via Resampling | 1, 2, 5, 6, 7, 8 ; 3, 4, 9 (en partie) |
| `docs/sources/pdf/2510.09462v2.pdf` | 52 | `96c16e33b27b9633b324acecfe29e1bfa9de7052143fb854824aad70a649d7f7` | Terekhov et al., Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols | 1, 4, 6, 7, 18 (les pages 24, 25 et 29 ont été affichées en cherchant l'annexe : consignes et exemple d'injection, non repris) |
| `docs/sources/pdf/2511.02997v1.pdf` | 31 | `1dcffc4983b07b989be8d8534ba38aae587722901e527fa1e37961aba18cd0e0` | Kutasov et al., Evaluating Control Protocols for Untrusted AI Agents | 1, 5 |
| `docs/sources/pdf/2607.13087v1.pdf` | 36 | `291a0cd72b0b6a0f08882db7080bba9f8a24ee196ae2f69f5063314cbfddeb55` | Phuong et al., GDM AI Control Roadmap | 6, 18, 29 (par motifs) |
| `docs/sources/pdf/2606.08892v2.pdf` | 71 | `aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a` | Terekhov, Gulcehre, Hebbar, Benton, Diffuse AI Control on Fuzzy Tasks | 17, 18 ; 2, 4, 5, 6 (par motifs) |

## Constat sur la numérotation des pages d'une pièce du dépôt

Le fichier `docs/sources/pdf/2510.09462v2.pdf` a 52 pages (`pdfinfo`). Son extraction d'un seul tenant par `pdftotext` rend 73 segments séparés par des sauts de page, parce que les pages de figures en contiennent plusieurs. Les rangs de segment ne sont donc pas des numéros de page pour ce fichier. Vérifié ce jour par `pdftotext -f N -l N` : la phrase « the apparent robustness of the protocol stemmed from being tailored to a specific attack policy » est à la **page 7** ; « decisions use the lowest suspiciousness among the samples » à la **page 4** ; « uses the minimum suspiciousness among actions resampled at a time point » à la **page 6** ; l'annexe A sur la règle du maximum et la légende de la figure 8 à la **page 18**. Pour les six autres fichiers ci-dessus, le nombre de segments vaut le nombre de pages plus un : rangs et pages coïncident.

## Téléchargés ce jour et non versés, non cités avec un chiffre

- arXiv 2511.09904v2 (« CTRL-ALT-DECEIT: Sabotage Evaluations for Automated AI R&D ») et arXiv 2607.19321v2 (« ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D ») : page 1 lue, rien sur les interventions non spécifiques par recherche de motifs ; restés dans le dossier temporaire de la session.

## Résultats de moteur de recherche seulement, pages non ouvertes (non opposables, R7)

- « Detecting Research Sabotage from Agent Behavior » (pages de la conférence NeurIPS 2026 ; pas d'identifiant arXiv trouvé).
- « Hand and Brain: Defenses against Agentic Steganography in Language Models » (page de la conférence ICML 2026).
- « Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems » (page de la conférence NeurIPS 2026).
- « A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring », arXiv 2602.23163.
- « Pressure-Testing Deception Probes in LLMs », arXiv 2605.27958 ; « Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling », arXiv 2604.13386.
- « Auditing Sabotage Bench » (d'abord « ASMR-Bench »), arXiv 2604.16286 ; billet « How can we solve diffuse threats like research sabotage with AI control? ».
