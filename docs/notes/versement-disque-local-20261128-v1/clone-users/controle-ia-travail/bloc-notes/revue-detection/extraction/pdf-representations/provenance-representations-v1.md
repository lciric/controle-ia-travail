# Provenance des PDF — famille « représentations » (revue « comment détecter », P3) — v1

- Téléchargés le 2026-10-20 (UTC) depuis `https://arxiv.org/pdf/<identifiant>` (dernière version servie ce jour), par le
  lecteur neuf de la famille « représentations ». Lecture seulement ; aucun service payant ; aucun contact.
- Chaque PDF est rangé dans son propre dossier (données non fiables) ; aucun n'est versé au dépôt.
- La version est lue sur le tampon arXiv de la première page ; le fichier est renommé avec cette version (R12).
- Empreintes calculées par `sha256sum` après renommage.

| fichier (sous ce dossier) | version (tampon p. 1) | pages | sha256 | titre (p. 1) |
|---|---|---|---|---|
| `2304.13734/2304.13734v2.pdf` | arXiv:2304.13734v2, 17 Oct 2023 | 10 | `9d26903ee6fcaaaf2d683e483db61f3fdcf6ebed3e32bb058648eaa56e327cfa` | The Internal State of an LLM Knows When It's Lying |
| `2310.06824/2310.06824v3.pdf` | arXiv:2310.06824v3, 19 Aug 2024 | 22 | `9d64b7633b07e7b9ba462ad5c405150d1fb7e834e3a7feedfc7f6ee196b83a6c` | The Geometry of Truth: Emergent Linear Structure in LLM Representations of True/False Datasets |
| `2212.03827/2212.03827v2.pdf` | arXiv:2212.03827v2, 2 Mar 2024 | 28 | `20062bccb4769416c800ede71f4660f3fe2ad9921a7e1964604cd1048efd3d7a` | Discovering Latent Knowledge in Language Models Without Supervision |
| `2310.01405/2310.01405v4.pdf` | arXiv:2310.01405v4, 3 Mar 2025 | 56 | `5cd54799f795433bd6652231e0d113dead887f21c798148619fc0ce6f0fd589f` | Representation Engineering: A Top-Down Approach to AI Transparency |
| `2309.15840/2309.15840v1.pdf` | arXiv:2309.15840v1, 26 Sep 2023 | 36 | `a710a785b6f1d59343877504167ea0a0ea74eac87e34f2a7d00e2e2517f67776` | How to Catch an AI Liar: Lie Detection in Black-Box LLMs by Asking Unrelated Questions |
| `2307.00175/2307.00175v1.pdf` | arXiv:2307.00175v1, 30 Jun 2023 | 21 | `56ded298914bea3c9fe650a1549b41bd807d0f89031e919ec2b05bc1fc16fe11` | Still No Lie Detector for Language Models: Probing Empirical and Conceptual Roadblocks |
| `2312.10029/2312.10029v2.pdf` | arXiv:2312.10029v2, 18 Dec 2023 | 38 | `8f8b5e7ad4391e822cacd768216ea475f74ef1540c8e0d09f42d8662b0e4c834` | Challenges with unsupervised LLM knowledge discovery |
| `2407.12831/2407.12831v2.pdf` | arXiv:2407.12831v2, 21 Oct 2024 | 32 | `badf34f0ae9eddd6c159ac8b637d66af5b3a939f296a78cc32e9755584dd1506` | Truth is Universal: Robust Detection of Lies in LLMs |

Remarques :
- `pdftotext` signale des erreurs de table de références internes pour `2310.01405v4.pdf` (« xref num … not found, try to
  reconstruct ») ; l'extraction se reconstruit ; les pages citées ont été relues et les citations contrôlées par script.
- PDF du dépôt lus en place (non copiés), empreintes contrôlées contre leur compagnon `.sha256` : `2405.05466v2.pdf`,
  `2502.03407v1.pdf`, `2506.10805v4.pdf`, `2601.11516v4.pdf`, `2504.20271v1.pdf` (sous `docs/sources/pdf/`).
