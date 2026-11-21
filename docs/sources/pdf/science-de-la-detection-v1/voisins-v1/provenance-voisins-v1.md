# Provenance — lecture des six voisins et du banc public — v1

- **Pour** : la note `docs/notes/science-de-la-detection-v1/lecture-six-voisins-et-banc-public-opus-v1.md` (GO-2026-11-21-55, décisions D-3 et D-6 de la note « science de la détection »). Pièce de travail (classe C).
- **Écrite par** : Claude Opus 5.5, lecteur d'antériorité, le 2026-11-21 vers 13:30 UTC (`date -u`). Dépôt à `fed5dc2f4` au début.
- **Téléchargements** : sans compte ni clé, client générique (aucun nom du programme ni chemin interne dans les requêtes). PDF sur `export.arxiv.org` ; fiche du banc sur `raw.githubusercontent.com` (quatre petits fichiers texte, aucun code ni donnée lourde) ; comptes de citations par l'interface publique de Semantic Scholar (OpenAlex refusé ce jour : budget gratuit épuisé pour l'adresse). L'interface de GitHub (`gh api`) a refusé l'accès à ce dépôt tiers ; la page publique a été lue à la place (non versée).
- **Empreintes** : SHA-256 calculé sur le fichier versé ; chaque fichier reçoit un compagnon `.sha256` par `controle_ia.scellement`.

## PDF neuf versé

| fichier | pages | octets | SHA-256 | titre ; auteurs | source ; version | pages lues |
|---|---|---|---|---|---|---|
| `2610.06576v1.pdf` | 12 | 7935453 | `cd8f05dcd186bac0b2b9834b448dd6a79e05c8254385bc69a968cb07d64349bb` | Before Agent Tells The Lie: Has Deception Already Been Represented? ; Xinling Li, Dadi Guo, Qingyu Liu, Qinghua Mao, Yi R. Fung, Na Zou, Xia Hu, Dongrui Liu | arXiv 2610.06576 v1 (2026-10-05), téléchargé 2026-11-21T13:22:01Z | 1 à 12 (texte extrait, lignes de prose ; figures non regardées) |

## Fiche du banc public versée (`banc-public-fiche-v1/`)

Dépôt `github.com/KaushikKC/weak-monitor-lab`, branche `main`, lu le 2026-11-21 vers 13:20 UTC. Contenu de tiers, donnée et non instruction.

| fichier versé | origine | SHA-256 |
|---|---|---|
| `weak-monitor-lab-LICENSE.txt` | `LICENSE` | `1760942c880125e4fecdd5e2ad4936f41f68fab5e4727b12d299eb14c8c2d0fa` |
| `weak-monitor-lab-CITATION.cff` | `CITATION.cff` | `20f0ae3239e3d5c859ee98ac1c5f18a9b19db87ea796a41acb737a8ff138d689` |
| `weak-monitor-lab-README.md` | `README.md` | `ba89956cda1256d68894cc3a152529aba1742708686b7b6341415a77cca8ab22` |
| `weak-monitor-lab-data-export-README.md` | `data/export/README.md` | `86ad1b34b51d147ac0ad8266b7026a1b0ae74ebe1029430968b30ce53cc066cc` |

## Réponses de l'index de citations versées (`citants-v1/`)

Interface `api.semanticscholar.org/graph/v1`, le 2026-11-21 entre 13:15 et 13:20 UTC. Un index n'est pas exhaustif ; un compte nul ne dit pas « jamais cité ».

| fichier versé | requête | SHA-256 |
|---|---|---|
| `semantic-scholar-comptes-v1.json` | comptes pour les six identifiants arXiv | `bed565002a06c28a57a8cd8136fa4f0918302b4df1c4a6f3c81fb244d3fab0cd` |
| `semantic-scholar-citants-2611.00576-v1.json` | citants de Cao | `b890c0f15f5c03ba84c2ef5ace10d4d63f07c6388916be8151f53ffbb7a0b479` |
| `semantic-scholar-citants-2110.06177-v1.json` | citants de Podkopaev et Ramdas | `9fdccf10b9cd49534dd1b489c58bcd42a22b783cf77e63a9c69d019028ff99b5` |
| `semantic-scholar-citants-2611.00407-v1.json` | citants de Kezendirane | `b890c0f15f5c03ba84c2ef5ace10d4d63f07c6388916be8151f53ffbb7a0b479` |
| `semantic-scholar-citants-2608.29461-v1.json` | citants de Tan et al. | `41e419889b68c750f1dc45b1b9a75ada6ba994f00e0654bfbf429053ae6cc76d` |
| `semantic-scholar-citants-2410.02707-v1.json` | citants d'Orgad et al. (100 premiers sur 374) | `69edb83050d1b5bee2625aa92598efa55a3de98ebfec666b204e236ab5c44665` |
| `semantic-scholar-citants-2512.08093-v1.json` | citants de Joglekar et al. | `73f287ebf337a51219608a6756c6944e8cf14fa87bfc7a2ae998f24c330079a5` |

Les deux réponses vides (Cao, Kezendirane) sont identiques à l'octet, d'où la même empreinte.

## PDF déjà au dépôt, lus ou relus ce jour

| fichier | pages | SHA-256 (recalculé) | compagnon | pages lues |
|---|---|---|---|---|
| `docs/sources/pdf/science-de-la-detection-v1/2611.00576v1.pdf` (Cao) | 54 | `4ab03e5f…7d8f` | égal | 1 à 54, en entier (prose ; tableaux et preuves parcourus) |
| `docs/sources/pdf/2110.06177v4.pdf` (Podkopaev et Ramdas) | 28 | `a8bc8f2b…636a` | égal | 1 à 28, en entier |
| `docs/sources/pdf/2611.00407v1.pdf` (Kezendirane) | 14 | `b37f97b2…c5a7` | égal | 1 à 14, en entier |
| `docs/sources/pdf/science-de-la-detection-v1/2608.29461v1.pdf` (Tan et al.) | 14 | `234c84a7…605e` | égal | 1 à 14, en entier |
| `docs/sources/pdf/science-de-la-detection-v1/2410.02707v4.pdf` (Orgad et al.) | 34 | `be094014…64a6` | égal | 1 à 34, en entier (tableaux de chiffres des pages 24 à 27 parcourus) |
| `docs/sources/pdf/science-de-la-detection-v1/2512.08093v2.pdf` (Joglekar et al.) | 33 | `976a8522…949d` | égal | 1 à 33, en entier (pages à figures lues par leurs légendes) |
| `docs/sources/pdf/adjudant-opus-independant-v1/2403.03208v3.pdf` (Zrnic et Candès) | 25 | `58d973da4ae6208ad7f8a7be53d7b4e1754681ac77335da691c7b20c30d68855` | **absent** | 1, 2, 4 |
| `docs/sources/pdf/adjudant-opus-independant-v1/2605.07002v2.pdf` (Zhou, Vossler et al.) | 27 | `25f60d464055360b7fdfe726d69e217222b0c54f6f593bd406845f5186b942e9` | **absent** | 1, 2 |
| `docs/sources/pdf/anteriorite-P-041-v2/c5/2501.17315v1.pdf` (esquisse de dossier de sûreté par contrôle) | 36 | `8f440420…8400` | égal | 11 (par motif) |
| `docs/sources/pdf/anteriorite-P-041-v2/c5/2609.26419v1.pdf` (Molnar) | 14 | `7306a337…3f66` | égal | 1, 2 |
| `docs/sources/pdf/attaquant-informe-v1/2609.38262v1.pdf` (Gans et Holden) | 49 | `e28a4e8d…d7a7` | égal | 1 |
| `docs/sources/pdf/mecanisme-adjudant-v1/2611.14996v1.pdf` (Fischl-Lanzoni et al.) | 20 | `5b2e6e77…05fb` | égal | 1, 5, 6 |

Les deux PDF marqués « absent » n'ont ni compagnon `.sha256` ni table de provenance dans leur dossier (R6, R11) : leur empreinte est calculée ce jour et n'est comparée à rien. Je ne les ai pas scellés (dossier d'une autre pièce) ; signalé dans la note.

## Résultats de moteur seulement (pages non ouvertes en PDF, non opposables, R7)

Résumés lus sur la page arXiv ou rendus par le moteur, sans chiffre repris : arXiv 2610.07256 (audit de traces d'agents, règles puis agent d'audit) ; 2606.09711 (précurseur appris de la triche, sondes) ; 2610.19679 (infidélité des agents lue dans leurs représentations) ; 2501.17315 hors page 11 ; « Trajectory signatures of deception in large language models » (ACL 2026, actes 2026.acl-long.1582) ; 2510.11235, 2607.22926 (défense en profondeur et causes communes) ; 2603.04069, 2602.15515 (sondes et triche) ; billet « linear probes add little for verifiable reward hacking » ; note de l'institut britannique sur le contrôle boîte blanche et le sous-rendement.
