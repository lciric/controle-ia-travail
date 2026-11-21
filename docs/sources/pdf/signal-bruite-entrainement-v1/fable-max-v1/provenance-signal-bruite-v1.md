# Provenance des sources de la note « le signal bruité pourrait suffire pour entraîner » (v1)

- 21 novembre 2026, 17:50 UTC (`date -u`). Lecteur : Claude Fable 5.2. Pièce de travail (classe C).
- Les huit PDF de ce dossier ont été pris ce jour à l'adresse `https://arxiv.org/pdf/<identifiant>` (la version servie est celle du tampon de la page 1). Chacun a son compagnon `.sha256`. Texte tiré par `pdftotext -layout` ; rang de la page dans le fichier, non folio imprimé ; aucune figure regardée, les légendes et les tableaux sont lus comme texte.
- « Lu » veut dire : lu par moi ce jour, aux pages dites. Tout le reste du fichier n'est pas lu.

## PDF versés dans ce dossier

| fichier | pièce | version au tampon | sha256 | pages lues |
|---|---|---|---|---|
| `arxiv-2604.22082.pdf` | Ryd, Bartsch, Stastny, Benton, Hebbar, « Removing Sandbagging in LLMs by Training with Weak Supervision » (conférence internationale sur l'apprentissage automatique, 2026) | v2, 1er mai 2026, 45 p. | `f27f3c399084f2abf8127969ac10a9ed3a4c5b859f5c23048b488d9872da3c05` | 1 à 9 et 30 à 33 en entier ; 26, 29, 34, 35 par motifs (annexes D.1, D.3, D.5 à D.9) |
| `arxiv-2505.13787.pdf` | Cundy, Gleave, « Preference Learning with Lie Detectors can Induce Honesty or Evasion » | v2, 18 novembre 2025 | `b6824e6e1d44e3b840581255ab08e88dbf54ccae860f6fb31c76b2addf190b8a` | 1 en entier ; 7, 8, 18, 19, 21, 22, 29, 30, 34 par motifs (« TPR ») |
| `arxiv-2503.11926.pdf` | Baker et al., « Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation » | v1, 14 mars 2025, 39 p. | `2547162c549d70e02beca2687903a8fce75fd950269a3ee479d5b8ebbb53ff38` | 1 |
| `arxiv-2601.23086.pdf` | Mitrani Hadida, Bhanji, Tice, Radmard, « Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks » | v2, 20 mai 2026, 66 p. | `568961b864f072665cb14c9414ddd4f6b051388588dfe26f2f55486e6365f855` | 1 |
| `arxiv-2604.28182.pdf` | Jang, Falck, Braun et al., « Exploration Hacking: Can LLMs Learn to Resist RL Training? » | v1, 30 avril 2026 | `a67967608d90361299ed46183f2a6aca8eab2c645db3e9d55380dbcb82ebf98a` | 1 |
| `arxiv-2405.19550.pdf` | Greenblatt, Roger, Krasheninnikov, Krueger, « Stress-Testing Capability Elicitation With Password-Locked Models » | v1, 29 mai 2024, 25 p. | `ae7243da8e4ea849a09ed6bb464ff5bd76969f18401fa020514bb75e475ccaae` | 1 |
| `arxiv-2512.07810.pdf` | Taylor, Black, Bowen et al., « Auditing Games for Sandbagging » | v1, 8 décembre 2025, 77 p. | `77e64bcd88754f506890ee99dc5672284145a8705d27c5a63e4fc47330d28c8f` | 1 |
| `arxiv-2509.21344.pdf` | Boxo, Neelappa, Raval, « Linear probes rely on textual evidence » | v2, 9 mars 2026 | `aaac4ff91c909f9e4363fe9c19bb0fc7c2a635bf91e13c178992411f2a25ee5c` | 1 |

## Pièces déjà au dépôt, relues ce jour (non recopiées ici)

| chemin | pièce | sha256 (recalculée ce jour, égale au compagnon ou à la note qui la cite) | pages lues ce jour |
|---|---|---|---|
| `docs/notes/veille-organismes-ideation-v2/pdf/web-gasteiger-2025-automated-researchers-sandbag.html` | Gasteiger et al., « Automated Researchers Can Subtly Sandbag », page web, mars 2025 | `4a7e0eb964103b4c78e3b880d6f9eae86d5740a1e83352d30d2cf81e00dad7e5` | page entière, texte tiré par `pandoc` ; annexe : légendes ; consignes des annexes non lues. **Page web : pas de pagination, non opposable au sens de la règle sur les PDF.** |
| `docs/notes/veille-organismes-ideation-v2/pdf/arxiv-2604.16286.pdf` | Gan, Bhatt, Shlegeris, Stastny, Hebbar, « Auditing Sabotage Bench », v2, 26 avril 2026, 54 p. | `833a48e6c63b0e1b36af9d7e1952878752379115c49f72bc2c9e3e7af3161cc0` | 1 (en-tête et résumé), 10, 37 en entier ; 14 (références 23 et 24) |
| `docs/notes/veille-organismes-ideation-v2/pdf/web-hebbar-2025-how-can-we-solve-diffuse-threats.html` | Hebbar, billet du 30 avril 2025, page web | `6831b0abc921ab279266961a47ee1309ca1d820e350b9ea96cf200f471d7401a` | six passages par motifs (entraînement en service, incrimination). **Page web, non opposable.** |
| `docs/sources/pdf/2606.08892v2.pdf` | Terekhov, Gulcehre, Hebbar, Benton, « Diffuse AI Control on Fuzzy Tasks », v2, 17 juin 2026 | `aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a` | 1 à 7, 9, 10 |
| `docs/sources/pdf/2602.15515v2.pdf` | Taufeeque, Heimersheim, Gleave, Cundy, « The Obfuscation Atlas », v2, 26 mai 2026 | `f6547ec830104abf8ceca353e46e32ee78453f6470fd1c03053e13834ebc54cb` | 1, 7, 8, 9 ; 3, 21, 23, 24 par motifs |
| `docs/sources/pdf/2506.14261v4.pdf` | Gupta, Jenner, « RL-Obfuscation », v4, 26 février 2026 | `4b0960622664e77d888974955b29f9c0e5913266392caeecac2b844f011e244c` | 1 |
| `docs/sources/pdf/2605.26047v2.pdf` | Lucassen, Kaufman, « Retrying vs Resampling », v2 | `947724f42324070fd47b1ecaf8c1bf9b2257df0e0c7f8822447241d3ea9a28fa` | 10, par motifs |
| `docs/sources/pdf/mecanisme-adjudant-v1/voisins-v1/2510.21531v1.pdf` | Wehner, Fritz, « Probe-based Fine-tuning for reducing Toxicity », v1, 24 octobre 2025 | préfixe `4d851e74ce14ab5e` | 1, 2 |

## Page web non versée

- Garg, « Monitor Evasion Depends on What RL Finds and What Monitors Miss », billet du 1er novembre 2026 (lesswrong.com). Lu à travers un outil qui résume la page : **aucun chiffre n'en est tiré**, non opposable.

## Recherche

Cinq requêtes en anglais sur un moteur limité aux États-Unis (mode ordinaire), sans nom du programme, sans nom de personne du programme, sans chemin interne : (1) l'article de 2026 sur l'entraînement contre le sous-rendement cité par Terekhov et al. ; (2) entraîner contre un moniteur : disparition ou dissimulation ; (3) un score de sonde comme signal de récompense contre le sous-rendement ou le sabotage diffus ; (4) le détournement de l'exploration ; (5) la tenue de sondes tenues à l'écart après un réglage fin. « Non trouvé » veut dire : non trouvé par ces cinq requêtes, jamais « libre ».
