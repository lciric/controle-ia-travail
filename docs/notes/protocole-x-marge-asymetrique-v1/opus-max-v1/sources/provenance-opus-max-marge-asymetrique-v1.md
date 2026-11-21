# Provenance des sources — réponse d'Opus 5.5 (effort maximal) sur la marge asymétrique — v1

- **Pour** : `docs/notes/protocole-x-marge-asymetrique-v1/opus-max-v1/reponse-opus-max-marge-asymetrique-v1.md`. Pièce de travail (classe C).
- **Aucun PDF téléchargé** : tous les PDF cités avec un chiffre sont déjà versés au dépôt avec leur compagnon `.sha256`. Empreintes recalculées le 21 novembre 2026 vers 17:30 UTC (`sha256sum`), toutes égales aux compagnons. Texte extrait par `pdftotext -layout`, page par page, dans le bloc-notes de la session (hors du dépôt) ; aucune figure regardée, légendes et tableaux lus comme texte.
- **« Page »** : rang de la page dans le fichier. Il coïncide avec le folio imprimé pour Lucassen et Kaufman, Ctrl-Z, Terekhov et al., Factor(T,U) et la feuille de route de Google DeepMind (folio relevé en bas de page) ; Kutasov et al. n'imprime pas de folio.
- **Ce qui est opposable (règle R7)** : les phrases et chiffres cités dans la note, à la page dite, pour la version dont l'empreinte est donnée ici.

## PDF lus ce jour

| chemin | pages | SHA-256 | référence | pages lues |
|---|---|---|---|---|
| `docs/sources/pdf/2605.26047v2.pdf` | 46 | `947724f42324070fd47b1ecaf8c1bf9b2257df0e0c7f8822447241d3ea9a28fa` | Lucassen, Kaufman, « Retrying vs Resampling in AI Control », arXiv 2605.26047 v2 (26 mai 2026) | 1 à 11, en entier |
| `docs/sources/pdf/2504.10374v1.pdf` | 38 | `5f802d679344fe5e15d1edd50e96245f3bdc054e69d1ff0880b077d173549211` | Bhatt et al., « Ctrl-Z: Controlling AI Agents via Resampling », arXiv 2504.10374 v1 | 1, 7 ; 33-34 par motifs |
| `docs/sources/pdf/2510.09462v2.pdf` | 52 | `96c16e33b27b9633b324acecfe29e1bfa9de7052143fb854824aad70a649d7f7` | Terekhov, Panfilov, Dzenhaliou et al., « Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols », arXiv 2510.09462 v2 | 1, 4, 9, 10, 18 |
| `docs/sources/pdf/2511.02997v1.pdf` | 31 | `1dcffc4983b07b989be8d8534ba38aae587722901e527fa1e37961aba18cd0e0` | Kutasov et al., « Evaluating Control Protocols for Untrusted AI Agents », arXiv 2511.02997 v1 | 1, 3, 6 |
| `docs/sources/pdf/anteriorite-P-041-v2/c5/2512.02157v1.pdf` | 19 | `c3a2c6c5215fe7ab7839fe61ec1e0c885f3bc06bcd881ac9229158c5d8da2672` | Sandoval, Rushing, « Factor(T,U): Factored Cognition Strengthens Monitoring of Untrusted AI », arXiv 2512.02157 v1 | 1 ; 10-11 par motifs |
| `docs/sources/pdf/2607.13087v1.pdf` | 36 | `291a0cd72b0b6a0f08882db7080bba9f8a24ee196ae2f69f5063314cbfddeb55` | « GDM AI Control Roadmap », arXiv 2607.13087 v1 | 10, 18, 21, 25, 29 ; autres par motifs |
| `docs/sources/pdf/2606.08892v2.pdf` | 71 | `aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a` | Terekhov, Gulcehre, Hebbar, Benton, « Diffuse AI Control on Fuzzy Tasks », arXiv 2606.08892 v2 | 1, 7, 9 ; reste par motifs (aucune mention du rééchantillonnage comme parade) |

## Repris d'autres pièces du dépôt, sans relecture de ma part

- Tice et al., arXiv 2412.01784 (bruit sur les poids) et Clymer, Juang, Field, « Poser », arXiv 2405.05466 (bruit d'activations) : par N-013 (`157d388e…`, § 6) et N-015 (`462785b3…`, § 1) ; PDF présents au dépôt, non relus.
- Coûts unitaires d'un greffon d'expérimentateur (0,142 et 4,10 USD) : erratum 1 de la note de conception des expérimentateurs (`0198f5f8…`, § 2 (a)).

## Pages web seulement, PDF non lus (non opposables, règle R7)

- « Caught, Not Taught: Intervention History Reduces AI Agent Sabotage on Subsequent Tasks », Saeedi et Aghazadeh, page de la conférence NeurIPS 2026 (`https://neurips.cc/virtual/2026/168125`), lue le 21 novembre 2026 vers 17:00 UTC par un outil de lecture de page ; aucun identifiant arXiv sur la page. Aucun chiffre repris dans la note.
- « Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents », arXiv 2608.27141 v6, page de résumé d'alphaXiv (`https://www.alphaxiv.org/abs/2608.27141.md`), même jour. Aucun chiffre repris.
- Sandoval et Rushing (2512.02157) et Lue Chee Lip et al. (2512.14745) : résultats de moteur, puis PDF du dépôt pour le premier.

## Requêtes en ligne (anglais, sans nom du programme ni de personne)

1. « AI control memory reset context reset untrusted agent sabotage defense empirical »
2. « trusted paraphrasing defense AI control sabotage usefulness tradeoff arXiv »
3. « factored cognition AI control untrusted model decomposition context restriction safety usefulness arXiv 2025 »
4. « intervention reduces sabotage more than honest performance dose-response non-specific perturbation scheming model … selective degradation »

Aucune ne rend une mesure de l'affaiblissement d'un attaquant qui riposte au mieux, hors audit, par une intervention sans moniteur. Ce « non trouvé » n'est pas « libre » (règle R8) : quatre requêtes, pas une recherche affirmative.

## De mémoire, sans pièce

- Défenses par reformulation contre les portes dérobées textuelles à déclencheur lexical (travaux de 2021), et leur échec contre des déclencheurs syntaxiques : non vérifié, non cité avec un chiffre.
