# Provenance des PDF — protocole X, six questions sur l'attaquant informé — v1

- **Pour** : la note `docs/notes/protocole-x-attaquant-v1/reponse-fable-protocole-x-attaquant-v1.md` (six questions du directeur du 21 novembre 2026, GO-2026-11-21-57). Pièce de travail (classe C).
- **Téléchargés** le 2026-11-21 entre 14:05 et 14:12 UTC (`date -u`), sans compte ni clé, par un client générique (aucun nom du programme ni chemin interne dans les requêtes), depuis `export.arxiv.org` ; dernière version au jour du téléchargement. Titre, auteurs et version lus sur la première page du PDF (tampon d'arXiv), non sur l'interface d'arXiv, qui a refusé mes requêtes de recherche (code 429).
- **Table écrite par programme** (`pdfinfo`, SHA-256 recalculé sur le fichier), le 2026-11-21T14:15:50Z ; pour les PDF déjà au dépôt, l'empreinte recalculée est comparée à celle du compagnon `.sha256`.
- **« Pages lues »** : pages dont le texte extrait (`pdftotext`) a été lu par l'auteur de la note, en entier ou par recherche de motifs ; rang de la page dans le fichier, non folio imprimé. Aucun PDF lu en entier ; aucune figure regardée (les légendes et les tableaux sont lus comme texte). Les pages non listées n'ont pas été lues.
- **Ce qui est opposable (R7)** : les phrases et chiffres cités dans la note, à la page citée, pour la version dont l'empreinte est donnée ici.

## PDF versés dans ce dossier

| fichier | pages | octets | SHA-256 | titre ; auteurs | source ; version | pages lues |
|---|---|---|---|---|---|---|
| `2002.06673v4.pdf` | 32 | 539830 | `af963c3c2aeafd7d50f6a6309f14d3450ffc22d335f5f4535ba0e14b9c694f17` | Performative Prediction ; Juan C. Perdomo, Tijana Zrnic, Celestine Mendler-Dünner, Moritz Hardt | arXiv 2002.06673 v4 (tampon de la première page : 26 février 2021), export.arxiv.org | 1, 7-9 ; 3, 10, 12 (par motifs) |
| `2610.29577v1.pdf` | 20 | 409703 | `8dd9cd5e5b802e5f885c12e3c8433f11c522b616f6551630220ada422928440d` | The Reflexivity Threshold: A Phase Transition for Multi-Agent Performative Prediction ; Ahmed Mahrous, Roberto Di Pietro | arXiv 2610.29577 v1 (tampon : 21 octobre 2026), export.arxiv.org | 1, 2 |
| `2102.08446v2.pdf` | 37 | 415476 | `957dc53ad39aa5772d81c8cfe2d95b07e3e9d25c068bab27905642c77e971010` | Smoothed Analysis with Adaptive Adversaries ; Nika Haghtalab, Tim Roughgarden, Abhishek Shetty | arXiv 2102.08446 v2 (tampon : 18 août 2021), export.arxiv.org | 1 ; 4, 5 (par motifs) |
| `1303.0356v2.pdf` | 9 | 173613 | `dee408355be629f8c651731b1138c55252a05b729f82d39278d2cb4340c71c1a` | Audit Games ; Jeremiah Blocki, Nicolas Christin, Anupam Datta, Ariel D. Procaccia, Arunesh Sinha | arXiv 1303.0356 v2 (tampon : 5 mars 2013), export.arxiv.org | 1 |
| `1709.02738v1.pdf` | 22 | 1316713 | `4d4adbdcc8e168d859466d9573a65253026b593cfde166210a338a29f9472912` | Cycles in Adversarial Regularized Learning ; Panayotis Mertikopoulos, Christos Papadimitriou, Georgios Piliouras | arXiv 1709.02738 v1 (tampon : 8 septembre 2017), export.arxiv.org | 1, 2 |
| `2012.09147v1.pdf` | 9 | 188370 | `fc3fcdc7119bf3892a4429df8d43606c5be3570f92efbade302d358879db377f` | Incentivizing Truthfulness Through Audits in Strategic Classification ; Andrew Estornell, Sanmay Das, Yevgeniy Vorobeychik | arXiv 2012.09147 v1 (tampon : 16 décembre 2020), export.arxiv.org | 1 |

## PDF déjà au dépôt, relus ce jour aux pages dites

| chemin | pages | SHA-256 (recalculé, égal au compagnon) | référence | pages relues |
|---|---|---|---|---|
| `docs/sources/pdf/2511.02997v1.pdf` | 31 | `1dcffc4983b07b989be8d8534ba38aae587722901e527fa1e37961aba18cd0e0` | Kutasov et al., Evaluating Control Protocols for Untrusted AI Agents | 1, 5, 6 ; 30, 31 (par motifs) |
| `docs/sources/pdf/anteriorite-P-041-v2/c5/2511.02823v1.pdf` | 18 | `243326eca7a4cd1dbdf253d3526d256817448339b172cd08e94c162c80ae8055` | Loughridge et al., Optimizing AI Agent Attacks With Synthetic Data | 1 ; 3, 4 (par motifs) |
| `docs/sources/pdf/2605.26047v2.pdf` | 46 | `947724f42324070fd47b1ecaf8c1bf9b2257df0e0c7f8822447241d3ea9a28fa` | Lucassen, Kaufman, Retrying vs Resampling in AI Control | 1, 2 ; 7, 8 (par motifs) |
| `docs/sources/pdf/mecanisme-adjudant-v1/2409.07985v2.pdf` | 30 | `698f0db6e87bd78689c122afe5cb60dd7795e6aec38ae730ce4725781b6d9871` | Griffin, Thomson, Shlegeris, Abate, Games for AI Control: Models of Safety Evaluations of AI Deployment Protocols | 1 ; 4, 5, 9, 10 (par motifs) |
| `docs/sources/pdf/asymetries-attaquant-v1/2609.36049v1.pdf` | 24 | `856b3857c20cbafd1be8c6f5c2901c6e139db371f9c9abcb97933e780104ed41` | Rudoler et al., Improving scalable oversight with co-trained monitors | 2-4 |
| `docs/sources/pdf/anteriorite-P-041-v2/c5/2609.26419v1.pdf` | 14 | `7306a3373c18d5f531727525289b00196ac66088fc15a19be893092e7a1f3f66` | Molnar, Reliability Theory for AI Control | 1-3 ; 6, 7, 9, 11-13 (par motifs) |
| `docs/sources/pdf/2605.15377v2.pdf` | 18 | `fe591700228b29dc3287130efe6f877c5eeada84169dcbf1e526f6dc2e401712` | Koran et al., Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute | 1, 2 ; 4, 6, 7 (par motifs) |
| `docs/sources/pdf/2608.16190v1.pdf` | 10 | `8fdb6141aac64fe6bf9f741336befe58b255e8588294d11ca708c6e8a2c857f5` | Jha, Decorrelation Is Not Complementarity: Skill, Not Lineage, Governs Trusted-Monitor Ensembles | 1, 2 |
| `docs/sources/pdf/attaquant-informe-v1/2505.13763v2.pdf` | 36 | `b878d094ed08fbc2e0dcdbde0ec3473eec2c8dcdfdadf2c227e7f85ef57ce899` | Ji-An et al., Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations | 1 |
| `docs/sources/pdf/anteriorite-P-041-v2/c6/ssg-ai-safety-2026-2602.07259.pdf` | 6 | `528f83f61f77c387aca7e6ff5f966a6b01f0e1e174888c18453ebd88dd529961` | Kim, Choo, Neoh, Tambe, Incentive-Aware AI Safety via Strategic Resource Allocation: A Stackelberg Security Games Perspective (arXiv 2602.07259 v1) | 1 |
| `docs/sources/pdf/anteriorite-P-041-v2/c6/korzhyk-2011-stackelberg-vs-nash-1401.3888.pdf` | 31 | `ac99b152327bbb0472fd791cf9b02f0982e891753039f87a09a3b6df2a2f5e2b` | Korzhyk, Yin, Kiekintveld, Conitzer, Tambe, Stackelberg vs. Nash in Security Games (Journal of Artificial Intelligence Research 41, 2011) | 1, 2 |

## Deux PDF téléchargés ce jour et non versés

- `2602.07259v1` : empreinte du téléchargement (`528f83f6…9961`) égale à celle du fichier du dépôt cité ci-dessus ; copié par mégarde dans ce dossier, puis déplacé hors du dépôt avant tout scellement (aucune suppression).
- `2610.34751v1`, « Adaptive Probe Design for Auditing AI Agents » (Li, Bi, Ding ; 38 pages, 11 615 512 octets, `58f51ff7…1298`) : page 1 lue ; il traite de l'évaluation hors politique d'un agent, non d'un auditeur face à un agent qui se cache ; hors sujet, non versé, non cité.

## Repris d'autres pièces du dépôt, sans relecture de ma part

Les pages sont celles que donnent les pièces citées, avec leur propre marque.

- De la note sur l'attaquant informé et de sa table de provenance (`docs/sources/pdf/attaquant-informe-v1/`) : Bailey et al., 2412.09565 ; McGuinness et al., 2512.11949 ; Lyons Keenan et al., 2609.36490 ; Gupta et Jenner, 2506.14261 ; Schaeffer et al., 2602.04930 ; Ge-Wang et al., 2606.06529 ; Zhu, Zuo et Sun, « Blindfold », 2610.37055 ; Goldwasser et al., 2204.06974 (par la note sur l'adjudant).
- De l'erratum 1 de la note sur la science de la détection et de la re-dérivation indépendante : Singh, 2610.18948 ; Shin, Ramdas et Rinaldo, 2203.03532 ; Zrnic et Candès, 2403.03208 ; Dwork et al., 1506.02629.
- De la note d'antériorité de la proposition d'organisme coévolutif (`docs/notes/anteriorite-P-041-v1/note-anteriorite-P-041-workflow-v2.md`, lignes 14 à 55) : Barni et Tondi, 1304.2172 ; Tondi, Merhav et Barni, 1802.02850.
- De la note sur l'étau : Bailey et al., p. 23 ; Belrose et al., 2306.03819.

## Résultats de moteur de recherche seulement, pages non ouvertes (non opposables, R7)

- Mell, Shook, Harang, « Measuring and Improving the Effectiveness of Defense-in-Depth Postures », atelier ICSS 2016, DOI 10.1145/3018981.3018986 : connu par la citation qu'en fait Molnar (p. 2, 6, 13) et par la page du moteur ; aucun PDF en accès libre trouvé.
- « When Redundant Probes Help in Strategic Auditing » (page de la conférence NeurIPS 2026) ; « Incentive-Aware Auditing for Strategic Boundary Manipulation in ML Evaluation Systems » (page de la conférence NeurIPS 2026).
- Deux billets de forum sur la sélection d'attaque et sur une faiblesse de la surveillance par modèle de confiance.
- De mémoire, sans pièce : Littlestone (1988) ; Helmbold et Panizza (1997) et Cesa-Bianchi, Lugosi et Stoltz (2005), prédiction économe en étiquettes ; Kish, effet de plan d'un sondage en grappes ; Eckhardt et Lee (1985), Littlewood et Miller (1989), pannes coïncidentes de versions multiples.
