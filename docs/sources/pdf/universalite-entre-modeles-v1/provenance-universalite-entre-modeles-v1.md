# Provenance des PDF — ce qui reste invariant d'un modèle à l'autre — v1

- **Pour** : la note `docs/notes/lecture-sondes-bbis-par-lentilles-v1/universalite-entre-modeles-v1.md` (question du directeur du 21 novembre 2026 sur la « méta-architecture » invariante d'un modèle et d'un entraînement à l'autre). Pièce de travail (classe C).
- **Téléchargés** le 2026-11-21 (`date -u`, entre 13:02 et 13:09 UTC), sans compte ni clé, par un client générique (aucun nom du programme ni chemin interne dans les requêtes) : depuis `export.arxiv.org` à la version nommée pour les fichiers arXiv ; depuis `raw.githubusercontent.com/mlresearch/v306` pour le fichier des actes de ICML 2026. Titres, auteurs et dates vérifiés par l'interface publique d'arXiv (`export.arxiv.org/api/query`) et par la page `proceedings.mlr.press/v306/wei26s.html`. Copiés ici sans modification à 13:11 UTC (comparaison octet à octet avec le téléchargement) ; chaque fichier commence par `%PDF`.
- **Table écrite par programme** (`pdfinfo`, SHA-256) ; chaque empreinte de la première table est contrôlée contre son compagnon `.sha256` (assertion). « Pages lues » : pages dont le texte extrait (`pdftotext -layout`) a été lu par l'auteur de la note, en entier ou par recherche de motifs ; le rang est celui de la page dans le fichier, non le folio imprimé. Aucune figure regardée ; aucun PDF lu en entier.
- **Ce qui est opposable (R7)** : les chiffres et citations de la note, à la page citée, pour la version dont l'empreinte est donnée dans la première table. Les pages non listées n'ont pas été lues.

## Versés ce jour (six travaux les plus proches)

| fichier | pages | octets | SHA-256 | titre ; auteurs | source ; version | pages lues |
|---|---|---|---|---|---|---|
| `2611.12675v1.pdf` | 24 | 564884 | `f08a4c6e21edefb23ced68fcefcb494dfa27f7482d125cd52712b93abd846a5f` | Interpretability Is Not Model-Specific ; Marcus Armstrong, Navid Ayoobi, Pradham Mummaleti, Alexander Chulzhanov, Arjun Mukherjee | arXiv 2611.12675 v1 (2026-11-09), export.arxiv.org | 1, 2, 3, 6, 7, 9 |
| `2610.28366v1.pdf` | 64 | 2392691 | `d6398c1faa48e16a3a3da87bd5a1c4bbd9f0509269ceb680ddb2970d47d8abc7` | Relative Representations Enable Portable White-Box Monitoring Across Language Models ; Tim Bakker, Christos Louizos | arXiv 2610.28366 v1 (2026-10-20), export.arxiv.org | 1, 2, 5, 6, 7, 8, 9 |
| `wei-2026-icml-pmlr-v306-wei26s.pdf` | 58 | 17285318 | `2d6aa236b48ba0b57003dd89de5bbfad47921d9ffc945f49ed97202fb0c70b86` | Deep neural networks divide and conquer dihedral multiplication ; Sihui Wei, Gavin McCracken, Gabriela Moisescu-Pareja, Harley Wiltzer, Doina Precup, Irina Rish, Jonathan Love | Actes de ICML 2026, PMLR 306, p. 133901-133958 ; fichier wei26s.pdf du dépôt public github.com/mlresearch/v306 (lien donné par la page proceedings.mlr.press/v306/wei26s.html) ; absent d'arXiv à cette date (recherche par titre dans l'interface d'arXiv) | 1, 2, 7, 8, 9 |
| `2602.16740v1.pdf` | 33 | 14721042 | `ee5d8c1446f99ffeadfc79381d2787c36816f7695202465856a03c874e3f1bbd` | Quantifying LLM Attention-Head Stability: Implications for Circuit Universality ; Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok | arXiv 2602.16740 v1 (2026-02-17), export.arxiv.org | 1, 2, 3, 7, 8, 12 |
| `2606.17229v1.pdf` | 14 | 420795 | `4600849013a56d085044c653b8f40d9fee89b90372e94b9a2b2d82fb723a5307` | Rift: A Conflict Signature for Deception in Language Models ; Petr Nyoma | arXiv 2606.17229 v1 (2026-06-15), export.arxiv.org | 1-3 (par motifs), 9, 10, 11 |
| `2608.09521v1.pdf` | 15 | 827889 | `3c3fdb26a34df5041ab364374bb7dc3778be49996dcd39cfe22955b212e74402` | One Adapter Pair per Model: A Universal Activation Interface for Language Models ; Su-Hyeon Kim, Jiwan Mun, Yo-Sub Han | arXiv 2608.09521 v1 (2026-08-10), export.arxiv.org | 1, 2, 4, 5, 7, 11 |

## Lus en appui, non versés (hors des six) — non opposables

Téléchargés le même jour dans le bloc-notes de la session, depuis `export.arxiv.org`, lus aux pages dites, non copiés au dépôt. L'empreinte est notée pour retrouver la même version ; aucun chiffre de ces deux fichiers n'est cité dans la note, seulement des phrases sans chiffre, données comme non opposables.

| fichier | pages | SHA-256 | titre ; auteurs | source ; version | pages lues |
|---|---|---|---|---|---|
| `2611.08438v2.pdf` | 183 | `d71c0d7e5c37960365267d036a28b56266c5b740e87d4d4f039d95055faa323c` | Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety ; Fazl Barez, Tung-Yu Wu et al. (27 auteurs) | arXiv 2611.08438 v2 (première version 2026-11-05, cette version 2026-11-09) | 1, 31 ; 45 et 89 par motifs |
| `2610.20286v1.pdf` | 78 | `d5ba65273035da08c55019e3b0fe98178e965843bfd63f2b6bea09acf8ed0a23` | From Plato to Aristotle: Toward a General Theory of Representation Hypotheses ; Dai Shi, Andi Han, Xiaoyu Li, Luke Thompson, José Miguel Hernández-Lobato | arXiv 2610.20286 v1 (2026-10-14) | 1-3, 8-9, 12 (par motifs), 16 |

## Cités d'après le résumé d'arXiv ou une autre page, non téléchargés

Les autres travaux nommés dans la note le sont d'après leur résumé lu par l'interface publique d'arXiv (`export.arxiv.org/api/query`, le 2026-11-21), ou d'après la page citée dans la note ; aucun chiffre n'en est repris.
