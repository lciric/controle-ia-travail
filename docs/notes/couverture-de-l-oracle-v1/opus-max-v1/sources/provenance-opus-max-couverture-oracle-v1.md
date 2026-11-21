# Provenance des sources de la réponse d'Opus 5.5 sur la couverture de l'oracle (v1)

- **Date** : 21 novembre 2026 (UTC). **Auteur** : Claude Opus 5.5 (`claude-opus-5-5`), effort maximal. Pièce de classe C.
- **Note qui les cite** : `docs/notes/couverture-de-l-oracle-v1/opus-max-v1/reponse-opus-max-couverture-oracle-v1.md`.
- **Méthode** : chaque PDF neuf a été téléchargé par `curl` dans un dossier propre de mon bloc-notes, contrôlé (type de fichier, page de titre, tampon de version pour arXiv), puis copié ici sans modification ; texte extrait par `pdftotext -layout`, pages lues dites ci-dessous. Une copie (2611.15835v1) vient du dépôt, même empreinte.
- **Refus d'outil, 17:59 UTC** : le téléchargement du manuel MIL-HDBK-1823A (2009), refusé une première fois par le site (page « 406 »), retenté avec un en-tête de navigateur, a été refusé par l'outil. Non retenté, par aucune voie ; aucun appel au réseau ensuite. Le manuel n'est cité que par son sommaire (pièce 5) et de mémoire, sans chiffre.
- **Droits** : les pièces 2 et 3 sont des copies d'auteur ou d'organisme normalisateur ; à exclure de toute copie publique du dépôt, par prudence.

## Pièces versées dans ce dossier

| # | Fichier | Source | SHA-256 | Titre ; auteurs | Pages lues | Emploi |
|---|---|---|---|---|---|---|
| 1 | `2409.12822v3.pdf` | https://arxiv.org/pdf/2409.12822 (17:48 UTC) | `004405a29c5254c8286dfe9dd1bdacc21bd362358315de559fe1766fc1a441ff` | Language Models Learn to Mislead Humans via RLHF ; Wen, Zhong, Khan, Perez, Steinhardt, Huang, Bowman, He, Feng | 1 | lecteurs persuadés sous optimisation (supposition S4) |
| 2 | `just-et-al-2014-fse-mutants-real-faults-v1.pdf` | https://homes.cs.washington.edu/~rjust/publ/mutants_real_faults_fse_2014.pdf (17:48 UTC) | `264e75e8cc2c62a583b041a4075151549de5b6e95c11cb358147f02d92c6e387` | Are Mutants a Valid Substitute for Real Faults in Software Testing? ; Just, Jalali, Inozemtseva, Ernst, Holmes, Fraser (FSE 2014) | 1, 2, 7 | couplage des défauts plantés aux défauts réels |
| 3 | `isa-ireland-530-audit-sampling-oct-2022-v1.pdf` | https://iaasa.ie/wp-content/uploads/2022/11/ISA-530_Oct_2022.pdf (17:49 UTC) | `18458bc7ea672fec772b49d6815de615d93e3bb45ec4dee6ae2b972f1b650835` | International Standard on Auditing (Ireland) 530, Audit Sampling, mise à jour d'octobre 2022 | 1-3 imprimées (6-8 du fichier) : § 5(c), 5(d), A1, A3 | risque d'échantillonnage et risque hors échantillonnage |
| 4 | `2611.15835v1.pdf` | copie de `docs/sources/pdf/mecanisme-adjudant-v1/2611.15835v1.pdf` | `a0951584b2342896f0de5fc1f8498358de780cdb1e5dbc20818ac8cf4190f6b5` | Controlling the Probability of Unknown Unknowns in Pre-Deployment Testing of AI Systems ; Li, Hays, Ramdas, Raghavan | 1, 6, 7, 13, 14 | étiqueteur imparfait sous audit d'or ; masse des défaillances jamais vues |
| 5 | `thompson-2005-sommaire-mil-hdbk-1823-v1.pdf` | https://www.cnde.iastate.edu/mapod/2005%20September/Outline%20of%20MIL%20HNBK%201823_Thompson.pdf (17:59 UTC) | `f702f25e98ec482082c54763ca5d3876fc625f0a565d5981fa45b30e9f3c6071` | sommaire de MIL-HDBK-1823, « Nondestructive Evaluation System Reliability Assessment » ; B. Thompson (2005) | 1-2 | annexes F (spécimens de fiabilité) et G (modèle de la probabilité de détection) |

## Pièces du dépôt citées, non versées ici (empreintes recalculées par moi ce jour)

| Pièce | Chemin | SHA-256 (préfixe) | Pages lues ce jour |
|---|---|---|---|
| « Blindfold », Zhu, Zuo, Sun, 2610.37055 v1 | `docs/sources/pdf/attaquant-informe-v1/2610.37055v1.pdf` | `5250fa1176ac804b…` | 3, 12 |
| Gans, Holden, 2609.38262 v1 | `docs/sources/pdf/attaquant-informe-v1/2609.38262v1.pdf` | `e28a4e8d6747cf4d…` | 1 |
| Greenblatt et al., AI Control, 2312.06942 v5 | `docs/sources/pdf/2312.06942v5.pdf` | `999f7a92bb8c0857…` | 4, 5, 16, 17 |
| Terekhov, Gulcehre, Hebbar, Benton, Diffuse AI Control on Fuzzy Tasks, 2606.08892 v3 | `docs/sources/pdf/adjudant-opus-independant-v1/2606.08892v3.pdf` | `8858355cae98467c…` | 1, 2, 10 |
| Raina, Liusie, Gales, 2402.14016 v2 | `docs/sources/pdf/2402.14016v2.pdf` | `d10f97ce404e4600…` | 1 |
| Chen et al., Humans or LLMs as the Judge?, 2402.10669 v5 | `docs/sources/pdf/2402.10669v5.pdf` | `47ae7d76edd51093…` | 1 |
| Li, Sun et al., Preference Leakage, 2502.01534 v3 (ICLR 2026) | `docs/sources/pdf/2502.01534v3.pdf` | `f1204432f5532965…` | 1 |
| Lum, Ball (2015), deux listes | `docs/sources/pdf/adjudant-opus-independant-v1/lum-ball-2015-undocumented-homicides-two-lists-v1.pdf` | `12335f413f76bc73…` | 2, 3 |

## Pages web, non opposables (R7)

- Papadakis, Shin, Yoo, Bae, « Are Mutation Scores Correlated with Real Fault Detection? », ICSE 2018 : résumé lu par un moteur de recherche (corrélation faible une fois la taille des suites de tests tenue) ; PDF non obtenu (certificat du site refusé par `curl`, non contourné).
