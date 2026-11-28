# Balayage « autres organismes » : lire les activations autrement qu'avec des sondes, pour P3 — v1

- **Date** : 2026-10-20, vers 19:30 UTC. **Auteur** : sous-agent du balayage, sans lien avec le préenregistrement, le run
  ou le verdict de P3.
- **Commande** : question de Lazar après le verdict de P3 (autres outils que les sondes ; « que ferait Anthropic » pour
  séparer une consigne lue d'une intention exécutée ; faut-il un P3c). Angle de ce fichier : **autres organismes**
  (Apollo Research, Google DeepMind, institut britannique de sûreté, Redwood, ARC, EleutherAI, Transluce, Goodfire,
  équipes universitaires). L'angle Anthropic (dont la « J-lens ») est traité par un autre balayage : le PDF
  `pdf/j-lens-2607.15495.pdf` du dossier commun n'est pas de moi et n'est pas lu ici.
- **Lu dans le dépôt (lecture seule)** : verdict P3, sections En tête, 1, 4, 7
  (`docs/verdicts/verdict-P3-premier-test-i-a-v1.md`) ; brief v2, l. 154-175 ; décisions N-015, N-026, N-029 ; trois
  fichiers `.sha256` de `docs/sources/pdf/`. Hors dépôt : P4 candidat 1, sections Hypothèse et « Ce que H-P4 n'affirme
  pas ». **Non lus** (interdits respectés) : `prereg/P3-consignes-v1.md`, tout `textes-actions-*`, tout `donnees/`.
  Aucune recherche récursive dans le dépôt. Aucune donnée de P3 envoyée nulle part ; recherches web génériques seulement.
- **Règle de lecture (R7)** : « vérifié » = lu dans le PDF empreinté ci-dessous, page du PDF (rang physique, 1 = première
  page). Une page web ou une fiche Hugging Face est **non opposable** : elle sert à dire si un outil existe, jamais à
  fournir un chiffre qui décide.
- **Réserve de portée** : la plupart des chiffres vérifiés portent sur Llama-3.3-70B-Instruct, Gemma ou Pythia, sur des
  tromperies verbalisées. Ils ne se transposent pas à l'agent 8B de P3 ; ils orientent des questions, rien de plus.

## 0. Verdict en six lignes

1. Dans les 23 papiers lus, aucun outil ne sépare, **sur un organisme instruit par consigne**, « lire la consigne » de
   « exécuter l'intention ». Les équipes qui posent la question **changent d'organisme**, pas de lecteur : comportement
   mis dans les poids, verrouillé par mot de passe, comparé à sa version déverrouillée (institut britannique, p. 7, 17, 22).
2. Tous les lecteurs riches (décodeur en langue naturelle, détection d'anomalie, autoencodeurs) **lisent la consigne
   elle-même** quand elle est dans le contexte (LatentQA p. 3 ; lentille accordée p. 10 ; 2507.22149 p. 1, 5). Sur (i-a),
   un succès serait ininterprétable pour la question de Lazar.
3. Les autoencodeurs parcimonieux ne battent pas les sondes en détection, y compris sur Llama-3.1-8B (2502.16681 p. 23) ;
   ils servent au **diagnostic** (corrélations parasites), pas au moniteur.
4. Pour Llama-3.1-8B-Instruct, il existe des autoencodeurs publics **à la couche 15** (andyrdt, fiche Hugging Face) et
   des autoencodeurs de base qui se transportent à l'instruit (Llama Scope p. 11) ; ni le papier des oracles
   d'activation (p. 5) ni le dépôt des lentilles accordées ne couvrent la version 3.1.
5. **Correction factuelle** : la famille (iii) de l'institut britannique ne contient **aucun saboteur 8B**. « Celui qui
   imite Llama-3.1-8B-Instruct » (Cedar) est un Llama-3.3-70B-Instruct (2512.07810 p. 7 ; config Hugging Face :
   80 couches, largeur 8192). Le lancer est un changement de modèle (GO).
6. Recommandation : pas de P3c « autres lecteurs sur (i-a) » ; ajouter à P3b le **rejeu croisé consigne × texte**
   (méthode de 2511.17408 p. 3, p. 23) ; reporter la question « intention » sur (ii), avec un **(ii) témoin bénin** et le
   contraste « mêmes jetons, deux poids ». Confiance ≈ 70 %.

## 1. Pièces lues et empreintes

PDF téléchargés d'arXiv dans `pdf/`, texte par `pdftotext -layout` dans `txt/` (même dossier parent que ce fichier) ;
empreintes des pièces web dans `web-autres/SHA256SUMS`.
Trois PDF ont la même empreinte que la copie du dépôt (`docs/sources/pdf/*.sha256`) : 2502.03407v1, 2507.12691v3,
2412.09565v2.

| arXiv (version) | organisme | sha256 | pages |
|---|---|---|---|
| 2502.03407v1 | Apollo Research | `a4820ad59ef9b294609aa11cbcc044c27835d5f433d7e79d6ae374f874bc2e2b` | 35 |
| 2507.12691v3 | Pivotal, Apollo | `0c00a77b0c07bb9a8cd2feb748d65fe9ac01ee7bee9746ebb9cbc0d1ca8ebb00` | 39 |
| 2609.02893v1 | CMU, Manchester (atelier ICML 2026) | `b76151cd633bec71cc1eb26d22e9fc2ba4eb376f91e6ffbfd8475e4f34df732b` | 11 |
| 2511.17408v4 | King's College, LASR, Goodfire, Cambridge | `91e00c25f356db80a0073d32d7d774e71b64de13767983d85ec4bb0fcadb2357` | 56 |
| 2502.16681v1 | MIT, Google DeepMind | `c40c10beb55dbc0d39824119af3f9e175b2bff44ae3f11527d2cff28eff92570` | 30 |
| 2410.20526v1 | Fudan (Llama Scope) | `7abfd9022b871380df5fe1a8efe30795c12bce526c23f0203411e81b311b9bad` | 23 |
| 2408.05147v2 | Google DeepMind (Gemma Scope) | `8dcc7d56e2a06699744abd92604ecb2c65d2bb0535848cee229de19a56738eac` | 26 |
| 2507.22149v4 | Case Western | `c59fc061fea7ac5c657fc591d8eea759913ac584e4effd224717bdba5fde9f29` | 21 |
| 2512.07810v1 | Institut britannique de sûreté, FAR.AI, Anthropic | `77e64bcd88754f506890ee99dc5672284145a8705d27c5a63e4fc47330d28c8f` | 77 |
| 2601.11516v4 | Google DeepMind | `c4a36db54c9d679a718a0e35b9cad09fa628d81f6174bb6e1d8c6b26a063d8bf` | 40 |
| 2308.15605v5 | Redwood Research | `77f4c0472800318eac13439375888ef8c0f284324d61204e04b49c9babd2dcea` | 61 |
| 2504.08812v1 | EleutherAI | `d8e3fb690110088f8300e1d97d75214517c6100e2c2a233c8bd64022fb20f46a` | 23 |
| 2312.01037v4 | EleutherAI | `509d8163e6f774bf98398dc8b917f60838aa6b316ee8cddf802cdca5ce9dc886` | 24 |
| 2303.08112v6 | EleutherAI et al. (lentille accordée) | `641bbdb6e070ace8c029d19f536cab67fa928d2b56af621482a42a0c3c349faa` | 25 |
| 2511.08579v3 | Transluce, MIT | `67425d416c5807b243a98249862b2b8e521122d510242ecda10e00985d09ca80` | 23 |
| 2502.01236v1 | Transluce, Stanford | `fb05d91d5f1469165366ad6ddd704341033f41586d51ba7b7c8c799a0de580d1` | 20 |
| 2412.08686v2 | Berkeley (LatentQA, ICLR 2026) | `e9203ac9e75858a3d712b7f1d82704e269f396f15d2aad2234d333f7392ed061` | 34 |
| 2401.06102v4 | Google (Patchscopes) | `e6a418bc435cd8fb91481ec2c19492998d833d0310c211d511f22cdfa9c5fa48` | 25 |
| 2512.15674v2 | MATS, Truthful AI, Anthropic et al. (oracles d'activation) | `735c75c9361da456e1c16ef2be69d596392e5d898a003ee4cef7c9ed99252bca` | 38 |
| 2602.20273v1 | Columbia et al. | `917ade43effae49b4ee70257961cb76a9603f702985098691dc0c5f760cfdaf7` | 28 |
| 2605.09391v2 | indépendant, Manchester | `7b3087b1a58d2bb429cf3a85115ad57cbc3f177552eb0a623e1faf015bd2e005` | 14 |
| 2605.27958v1 | LexisNexis | `43f55118822b378d950255b10aa68379fdb24a1431bba7e8721aacaf44d856e0` | 18 |
| 2412.09565v2 | Stanford, ARC, Berkeley et al. | `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9` | 51 |

Pages web et fiches Hugging Face, **non opposables**, enregistrées dans `web-autres/` :

| pièce | sha256 | sert à |
|---|---|---|
| `transluce-neuron-descriptions.html` | `7cc00baea861f8b5a7f868e740bca8724f10ad21150c76bf5ec06591b9a9a4e2` | existence des descriptions de neurones de Llama-3.1-8B-Instruct |
| `goodfire-sae-open-source.html` | `1ddaf974d0003e7cff095ad258d4f616e101d44e1142ebb86ad6ef28a54c60af` | autoencodeur Goodfire, Llama 3.1 8B, couche 19 |
| `gdm-sae-negative-results.html` | `ef863867d388599090d3eb5e8c865c3d078a2e536a446a8a0872f226ee25fea3` | résultats négatifs de DeepMind (billet, mars 2025) |
| `eleuther-mad-update-2.html` | `54f464bab443014fa56cf2c95e4c641d13c2519da2cb38e059fb302a41d06430` | détection d'anomalie sur Llama 3.1 8B (billet, 14 octobre 2024) |
| `hf-api-andyrdt.json` | `5def52caade957cf298f51195678698c308d87b9c439b0e7e6694456c21172c5` | autoencodeurs de Llama-3.1-8B-Instruct, couches 3, 7, 11, 15, 19, 23, 27 |
| `hf-api-goodfire-l19.json` | `fcd31137008043492b0f79cf585cfd96eadb98b9a7a8fc644a800d60754942a4` | fiche Goodfire, licence Llama 3.1 |
| `hf-api-openmoss-lxr32.json` | `2af29f0628568edee2cd5aec9ef6b0f9232dad9aee1d641998151f0d454bb0c2` | Llama Scope, 32 couches du flux résiduel, modèle de base |
| `hf-api-eleuther-64x.json` | `b7b9d062885cf45f946552a2bb7800d788d9019a17073e025c77135820183578` | autoencodeurs EleutherAI, couches 23 et 29 seulement |
| `hf-space-tuned-lens.json` | `240193ac3d4f0bfe8f03b2a1c28062387279c1720e78730c791260651690cf94` | lentilles accordées publiées : Llama-3-8B-Instruct, pas 3.1 |
| `hf-api-sandbagging-cedar.json` | `cd60dd07461aad8112242f916a0821781dfd6b57e8c0e7bd5c8747d147418df6` | organisme public Cedar (70B) |
| `hf-api-sandbagging-beren.json` | `b36ef3812d7ee12c68365ddf63dbdb169f1bb43f4dfe6c53d4934dcdd637b65a` | organisme public Beren (70B) |
| `hf-api-sandbagging-tarun.json` | `9c8b3db810bc8259189646a3673ba9905db69880b86d6f2b1858bb69a030b2ca` | organisme public Tarun (70B) |
| `hf-api-sandbagging-oak.json` | `2f5c0a63357cf105c2f4105ba6b2e95f6098b770b3efff2977cc0f8a35bce9eb` | organisme public Oak (70B) |
| `hf-api-sandbagging-yew.json` | `211f5aca74d6f0c33ca2986346b494b9465591adbab007452bf936ffd1452898` | témoin bénin Yew (8B à couches identité) |
| `hf-api-sandbagging-willow.json` | `4ff247f52fc9fa9dc5de9b47be5cb287cda5f46fbbaadc367264c930177ce444` | Willow, ajouté le 2025-12-15, rôle inconnu (80 couches) |

## 2. Fiches par outil

Format : ce qu'il lit ; faits vérifiés (page) ; disponible pour Llama-3.1-8B-Instruct ? ; limites ; apport pour P3.

### 2.1 Apollo Research — sondes de tromperie (Goldowsky-Dill et al., 2502.03407v1) — vérifié

- **Lit** : une direction linéaire du flux résiduel, entraînée sur des paires « Pretend you are an honest / a dishonest
  person making statements about the world » (figure p. 2 ; jeu de Zou et al., p. 4). C'est la phrase de l'entraînement
  de la sonde de P3 (P4 candidat 1, HT1).
- **Faits** : Llama-3.3-70B-Instruct, couche 22 sur 80 (p. 3) ; aires 0,96 à 0,999 ; 95 à 99 % rattrapés à 1 % de faux
  positifs sur du dialogue neutre (p. 1). La sonde « monte davantage sur les dialogues liés à la tromperie, même quand la
  réponse est honnête » (p. 10) ; elle suit « quelque chose proche de la morale » et note les aveux honnêtes comme
  trompeurs (p. 8). Deux couches plus loin, le rappel à 1 % tombe presque à 0 sur les deux jeux de délit d'initié (p. 6).
  Autoencodeurs (Goodfire, 70B) : la sonde sur leurs traits, entraînée sur les paires instruites, ne généralise pas
  (p. 8-9). Comparable à une base boîte noire GPT-4o (p. 10). **Agrégation** : « nous prenons la moyenne » ; pour la
  sonde des paires instruites, la moyenne est la meilleure sur tous les jeux, devant le maximum (annexe D.4, p. 22).
  Variante : sonder la réponse « No » à « Was your last response deceptive? » (p. 9).
- **Disponible** : code public (p. 1) ; pas de sonde publiée pour le 8B (P3 l'a refaite).
- **Limites** : tromperie flagrante, souvent dite dans la chaîne de pensée (p. 10) ; étiquettes difficiles (p. 10).
- **Apport pour P3** : (a) **la recette lit le contexte autant que l'acte** (p. 8, p. 10) : c'est exactement la crainte
  de Lazar, et elle est documentée par l'auteur de la recette. (b) Le point « à vérifier » de N-026 est vérifié : Apollo
  agrège par moyenne et la moyenne y bat le maximum pour ce type de sonde (p. 22). P3 a lu le maximum (règle de
  production). Le bras de diagnostic « moyenne » de N-026 est donc la question la mieux fondée de l'instrument.
  (c) La fragilité à la couche (p. 6) interdit de conclure sur « la couche 15 » sans balayage préenregistré ailleurs.

### 2.2 Gain boîte blanche sur boîte noire (Parrack, Attubato, Heimersheim, 2507.12691v3) — vérifié

- **Lit** : la même sonde, donnée à un moniteur génératif en plus du texte ; mesure le gain sur le moniteur sans sonde.
- **Faits** : gain « faible mais encourageant » (p. 1), modeste sur la plupart des jeux, négatif sur du code (p. 8).
  « L'activation de la sonde est étalée sur toute la réponse, non concentrée sur les affirmations trompeuses » ; les
  méthodes sensibles à un seul jeton (pic, question de suivi) marchent mal (p. 8). Sur le code, les réponses honnêtes
  ont une moyenne de sonde au-dessus de 99,9 % des réponses de contrôle (p. 9). Llama-3.3-70B (p. 9).
- **Apport pour P3** : un signal **diffus** est la signature d'un mode ou d'un contexte, pas d'un acte localisé. Une
  triche localisée dans le champ du coût est le cas le plus défavorable à cette sonde, quelle que soit l'agrégation.
  Ils demandent eux-mêmes des « sondes de tromperie localisée » (p. 9) : c'est l'objet de P3b, sans antériorité trouvée
  ici (question ouverte, R8, pas une revendication).

### 2.3 Sondes en sous-espace (Yoo et Skapars, 2609.02893v1 ; atelier ICML 2026, pas la conférence) — vérifié

- **Lit** : une sonde entraînée seulement sur quelques composantes principales du domaine source.
- **Faits** : **Llama-3.1-8B-Instruct, couche 15**, moyenne sur la réponse (p. 3). Source « Roleplaying » d'Apollo ;
  aires de base 0,874 (délit d'initié, confirmation), 0,706 (rapport), 0,606 (sous-performance) ; une sonde entraînée
  sur la cible dans les 100 premières composantes atteint 0,936, 0,950, 0,869 (p. 3) : l'information est là, la sonde
  source choisit la mauvaise direction. Sélection des composantes par un juge : sous-performance 0,606 vers 0,662
  (p. 5). Aucune validation causale (p. 5). Présenté à l'atelier « Connecting Low-rank Representations in AI » (p. 1).
- **Disponible** : méthode simple (analyse en composantes et régression logistique) ; données d'Apollo publiques.
- **Apport pour P3** : (a) **ancre externe de l'instrument** : mêmes modèle et couche que P3, chiffres publiés ; les
  reproduire avec notre code d'extraction vérifie l'instrument hors de nous (voir section 5). (b) La sous-performance,
  la plus proche de notre sabotage, est la cible où la sonde générique transfère le plus mal (0,606, p. 3).

### 2.4 Données hors politique et « retirer la consigne » (Kirch et al., 2511.17408v4) — vérifié

- **Lit** : rien de nouveau ; c'est une méthode d'entraînement et de test des sondes, sur huit comportements.
- **Faits** : les pires échecs de généralisation viennent des comportements définis par l'**intention** (tromperie
  stratégique), pas par le contenu du texte (p. 1). Quatre façons de produire les données : naturelle, incitée, sur
  consigne, hors politique (figure p. 2). Pour les données sur consigne, **on retire la consigne après la génération et
  on ne calcule les activations que sur [entrée ; réponse]**, « pour que la sonde n'apprenne pas à reconnaître la
  consigne » (p. 3) ; garder la consigne fait baisser la généralisation (annexe G, p. 23). Une intention seulement
  énoncée « ne produit pas la même signature d'activation qu'un raisonnement stratégique réel » (hypothèse des auteurs,
  p. 9). Réussir sur des données **incitées** prédit la réussite sur données naturelles (p. 1). Modèle principal
  Llama-3.2-3B-Instruct (p. 4).
- **Apport pour P3** : c'est la méthode la plus directe pour la question de Lazar. **Rejeu croisé** : recalculer les
  activations des mêmes jetons d'action avec et sans la consigne cachée dans le contexte (2 × 2 : consigne présente ou
  absente × texte saboteur ou honnête). Un signal qui disparaît sans la consigne lisait la consigne ; un signal qui
  reste lit le texte. Aucune case ne lit une intention : cela demande (ii). Second apport : un **organisme incité**
  (aucune consigne de mentir ; une situation où gonfler le coût sert un but) est l'échelon intermédiaire entre (i) et
  (ii).

### 2.5 Autoencodeurs parcimonieux (Google DeepMind et autres)

- **Gemma Scope (2408.05147v2, vérifié)** : autoencodeurs de Gemma 2 seulement (p. 1). **Non disponible** pour Llama.
- **Résultats négatifs de DeepMind** (billet de mars 2025, `gdm-sae-negative-results.html`, **non vérifié sur PDF**) :
  pour l'intention nuisible hors distribution, les sondes linéaires denses battent les sondes sur autoencodeur ; un
  autoencodeur spécialisé sur du dialogue ferme environ la moitié de l'écart ; seul usage positif : repérer vite des
  corrélations parasites dans un jeu de données.
- **Kantamneni et al. (2502.16681v1, vérifié)** : les sondes sur autoencodeur font moins bien que la régression
  logistique dans les quatre régimes, en moyenne (p. 1) ; les gains apparents (corrélations parasites, qualité des
  données) s'obtiennent aussi sans autoencodeur (p. 1). **Annexe F, Llama-3.1-8B avec Llama Scope** : couche 16 la
  meilleure de peu ; les sondes sur autoencodeur ne sont pas meilleures (p. 23-24).
- **Llama Scope (2410.20526v1, vérifié)** : 256 autoencodeurs, chaque couche et sous-couche de Llama-3.1-8B **de base**
  (p. 1). Sur Llama-3.1-8B-Instruct (dialogues WildChat), pas de dégradation sauf à la dernière couche ; à L15R-32x,
  perte ajoutée 0,090 sur l'instruit contre 0,162 sur la base (p. 11). Poids sur Hugging Face, organisation
  `OpenMOSS-Team` (32 couches du flux résiduel, plus des transcodeurs ; fiche non opposable).
- **Goodfire** (billet du 10 janvier 2025 et fiche, **non vérifié sur PDF**) : un autoencodeur pour
  Llama-3.1-8B-Instruct, **couche 19 seulement**, entraîné sur LMSYS-Chat-1M, licence Llama 3.1. Cité par
  2512.07810 (p. 29) et utilisé en 70B par Apollo (p. 3) et par l'institut britannique (p. 22, p. 72).
- **andyrdt/saes-llama-3.1-8b-instruct** (fiche, **non vérifié sur PDF** ; cité par 2609.02893 p. 6) : flux résiduel
  de Llama-3.1-8B-Instruct aux couches 3, 7, 11, **15**, 19, 23, 27. Convention d'indice de couche à vérifier contre
  celle de P3 avant tout usage.
- **EleutherAI** (fiche, non opposable) : autoencodeurs de Llama 3.1 8B aux couches 23 et 29 seulement.
- **Apport pour P3** : un outil de **diagnostic**, pas un moniteur. Usage utile : décomposer la direction de la sonde
  de tromperie et celle de la future sonde « oracle » de P3b sur les traits de la couche 15 ; regarder si elles
  s'alignent sur des traits de consigne ou de persona, ou sur des traits de nombres et de coût. Usage à éviter : une
  « sonde sur autoencodeur » de plus, que trois sources indépendantes donnent perdante.

### 2.6 Représentations sous consigne trompeuse (Long et al., 2507.22149v4) — vérifié

- **Lit** : le décalage moyen des traits d'autoencodeur entre consignes véridique, neutre et trompeuse.
- **Faits** : Llama-3.1-8B-Instruct et Gemma-2-9B-Instruct ; décalage concentré aux couches basses et moyennes ;
  quelques traits « associés à la tromperie » (p. 1). Pour Llama, autoencodeurs Llama Scope LXR-32x **du modèle de
  base**, moyennes sur tout le jeu (p. 5). Aucune intervention causale (p. 9).
- **Apport pour P3** : c'est la démonstration publiée, sur notre modèle, que **la consigne seule déplace les
  représentations**. Leurs « traits de tromperie » sont des traits de consigne : le contraste compare deux consignes
  (figure p. 2). Ce papier illustre le confondant ; il ne le lève pas.

### 2.7 Institut britannique de sûreté — jeux d'audit de sous-performance (Taylor et al., 2512.07810v1) — vérifié

- **Lit** : tout, à l'aveugle : transcriptions, sondes, autoencodeurs, bruit sur les poids, réglage fin d'élicitation.
- **Faits** :
  - L'équipe bleue perd : 1 modèle sur 5 bien classé en phase 1 (p. 3). Les méthodes boîte noire sont battues par
    l'**imitation d'un modèle plus faible** (p. 1, p. 3).
  - Organismes finaux (table p. 7) : Cedar, **Llama-3.3-70B-Instruct**, sous-performe partout en imitant
    Llama-3.1-8B-Instruct sauf mot de passe ; Oak, 70B, sous-performe sur les épreuves de capture de drapeau ; Baobab
    et Maple, **bénins avec comportements distracteurs** (doubles négations, changements de langue) ; Yew, **copie
    bénigne de Llama-3.1-8B-Instruct**, couches identité ajoutées. Référence de confiance : **Llama-3.1-8B-Instruct**.
    Partie d'essai (p. 36) : Tarun, 70B, **distillé depuis une consigne** ; Beren, 70B, imitation du 8B. Fiches Hugging
    Face (non opposables) : Cedar et Willow ont 80 couches et une largeur 8192 ; poids publics, non verrouillés.
  - Sondes de tromperie entraînées sur « Pretend to be an [honest/dishonest] character making statements about the
    world », moyenne sur les jetons (p. 16). Sur Cedar, scores « fortement et robustement élevés », plus élevés
    verrouillé que déverrouillé, et plus que le modèle d'origine, **même à justesse de réponse égale** (p. 16-17).
    Faux positifs induits par les distracteurs ; échec inexpliqué sur Oak (p. 17). L'équipe ne s'est pas fiée aux
    sondes (p. 17).
  - Sondes de sous-performance entraînées sur des déroulés de **Llama-3.1-8B-Instruct** sous consigne bénigne ou de
    sous-performance : utiles comme les sondes de tromperie ; aucune différence sur Oak (p. 21-22).
  - Bruit sur les poids : gain ξ = 1,094 sur les tâches sabotées contre 1,038 ailleurs, bien plus faible que
    **ξ ≈ 2 chez les modèles saboteurs sur consigne** (p. 22).
  - Autoencodeur Goodfire 70B, couche 50 : un trait « fournir une information incorrecte » plus actif chez Cedar
    verrouillé ; avis de l'équipe partagé (p. 22-24). Analyse après coup, sans aveugle (p. 4).
  - Limites : modèles verrouillés par mot de passe, peut-être plus faciles que des intentions émergentes ; dix
    organismes ; aucune garantie chiffrée (p. 4).
- **Disponible pour 8B** : **non** pour les saboteurs (tous 70B). Utilisables tels quels en 8B : la référence et le
  témoin bénin Yew.
- **Apport pour P3** : (a) la phrase de persona de notre sonde **a déjà détecté un saboteur sans consigne dans le
  contexte** (Cedar, comportement dans les poids), et plus quand il sabote que déverrouillé (p. 16-17) : c'est la
  forme publiée du test « intention » de T0.7. (b) Le **plan d'expérience** à copier : mêmes poids, mot de passe présent
  ou absent ; organismes bénins à distracteurs ; équipe bleue à l'aveugle. (c) **La signature d'un sabotage sur consigne
  diffère de celle d'un sabotage appris** (ξ ≈ 2 contre 1,09, p. 22) : un résultat sur (i) ne se transpose pas à (ii).
  (d) Brief l. 161 à lire avec la correction de la section 0, ligne 5.

### 2.8 Google DeepMind — sondes en production pour Gemini (Kramár et al., 2601.11516v4) — vérifié

- **Faits** : surveillance des entrées, domaine cyberoffensif, Gemini 2.5 Flash ; les sondes échouent sous les
  glissements de production, surtout du contexte court au contexte long (p. 1). Architecture « MultiMax » meilleure en
  contexte long que la moyenne (p. 2). Cascade sonde puis classifieur génératif : meilleure que le classifieur seul pour
  environ 1/50 de son coût (p. 2). Forte variance entre graines, exploitée (p. 2).
- **Disponible** : méthode seulement ; ni code ni sonde pour Llama vérifiés ici.
- **Apport pour P3** : nos actions sont de longs contextes agentiques, hors de la distribution courte d'entraînement de
  la sonde : un motif d'échec documenté. La cascade est le bon cadre pour T0.8 (N-029), pas pour P3.

### 2.9 Redwood Research — détection de falsification de mesure (Roger et al., 2308.15605v5) — vérifié

- **Lit** : les activations d'un prédicteur de mesures ; apprend sur une distribution **de confiance** (sans
  falsification) et cherche, sur une distribution non sûre, les cas où les mesures et le vrai résultat divergent (p. 1).
- **Faits** : modèles Codegen 350M, Pythia-1.4B, MPT 7B, Codegen 2B (p. 11) ; quatre techniques battent les bases sur
  un jeu, aucune n'approche la sonde de vérité terrain (p. 15).
- **Disponible pour 8B** : jeux et méthode publics ; aucun outil prêt pour Llama.
- **Apport pour P3** : le cadre « confiance contre non sûr » est celui de l'environnement (a) : épisodes honnêtes =
  distribution de confiance ; le coût déclaré est la « mesure ». Il justifie un détecteur entraîné sur l'honnête seul.

### 2.10 ARC — détection d'anomalie mécanique — non vérifié

- Cadre théorique (Christiano 2022, cité par 2308.15605 p. 21 et 2504.08812 p. 1). ARC est coauteur de 2412.09565
  (p. 1). **Aucun outil d'ARC pour Llama trouvé** ; rien d'opposable.

### 2.11 EleutherAI — détection d'anomalie, lentille accordée

- **Modèles « bizarres » (2312.01037v4, vérifié)** : modèles affinés pour se tromper ssi « Bob » est dans l'entrée ; une
  détection d'anomalie repère le comportement non véridique à 0,95 d'aire (p. 1), dans leur cadre.
- **Détection d'anomalie mécanique (2504.08812v1, vérifié)** : aucun détecteur efficace sur tous les modèles et tâches
  (p. 1) ; **sur Llama 3.1 8B, aires moyennes hors arithmétique toutes sous 0,8, beaucoup proches du hasard** (p. 6) ;
  la distance de Mahalanobis sur les activations brutes reste la référence (p. 8). Le billet du 14 octobre 2024 (non
  opposable) le dit « décourageant » et note qu'autoencodeurs et flots normalisants rejoignent Mahalanobis.
- **Lentille accordée (2303.08112v6, vérifié)** : sur Pythia 12B, ses trajectoires détectent des **injections de
  consigne** presque parfaitement sur cinq tâches ; la base de Mahalanobis relative simplifiée, à la couche du milieu,
  « fait constamment bien » (p. 10). Lentilles publiées (non opposable) : Llama-3-8B-Instruct, **pas 3.1** ; il faut
  l'entraîner.
- **Apport pour P3** : la famille « Mahalanobis, non supervisée » de T0.7 est la bonne référence non supervisée. Mais
  sur (i), un détecteur d'anomalie détecte d'abord **la consigne étrangère** (c'est son usage publié : les injections,
  p. 10). Il ne départage donc rien sur (i) ; il a un sens sur (ii). Prior défavorable sur Llama 3.1 8B (p. 6).

### 2.12 Transluce — descriptions de neurones, explicateurs, agents enquêteurs

- **Descriptions de neurones** (rapport web du 23 octobre 2024, **non vérifié sur PDF**) : base de descriptions de tous
  les 458 752 neurones des couches denses de **Llama-3.1-8B-Instruct**, interface « Monitor », code « observatory ».
- **Explicateurs entraînés (2511.08579v3, vérifié)** : un modèle affiné décrit les traits, l'effet d'interventions et
  les jetons décisifs ; « accès privilégié » : se décrire soi-même marche mieux (p. 1). Cible Llama-3.1-8B (base),
  traits d'autoencodeur Llama Scope ; un des explicateurs est Llama-3.1-8B-Instruct (p. 5). Poids sur Hugging Face
  (non opposable).
- **Agents enquêteurs (2502.01236v1, vérifié pour le résumé)** : cherchent des **entrées** qui déclenchent un
  comportement (p. 1). Outil boîte noire d'élicitation, pas un lecteur d'activations.
- **Apport pour P3** : étiqueter automatiquement les traits d'autoencodeur alignés avec une direction de sonde
  (diagnostic de 2.5). Faible pour la détection.

### 2.13 Lecteurs en langue naturelle : LatentQA, Patchscopes, oracles d'activation

- **LatentQA (2412.08686v2, vérifié)** : un décodeur répond en langue naturelle à une question sur des activations ;
  évalué sur la découverte de **consignes système cachées** (p. 1). Il est entraîné à lire la « consigne de contrôle »
  (buts, personas) ; même quand on masque les activations de la consigne, celles de la suite « gardent l'information
  par l'attention » (p. 3). Llama-3-8B-Instruct (p. 4).
- **Patchscopes (2401.06102v4, vérifié)** : on greffe une représentation dans une invite cible et le modèle la décrit ;
  sans entraînement (p. 1) ; LLaMA2 13B, Vicuna 13B, GPT-J 6B, Pythia 12B (p. 4).
- **Oracles d'activation (2512.15674v2, vérifié)** : LatentQA généralisé ; retrouvent une information **mise par réglage
  fin, absente du texte d'entrée**, sans avoir vu de modèle affiné (p. 1). Entraînés pour Llama-3.3-70B, Gemma-2-9B-IT,
  Qwen3-8B, Claude Haiku 3.5 (p. 5) ; environ 10 heures de H100 pour Qwen3-8B (p. 5, p. 19). **Aucun oracle pour
  Llama-3.1-8B-Instruct** dans le papier.
- **Apport pour P3** : sur (i), ces lecteurs **liront la consigne** (c'est leur tâche d'entraînement, LatentQA p. 3) :
  succès attendu et sans valeur pour la question. Sur (ii), l'oracle est le seul lecteur publié revendiquant de lire ce
  qui est dans les poids et pas dans le texte (p. 1) : candidat sérieux pour un test sur (ii). Coût : entraînement
  (ordre de 10 heures de carte graphique pour un 8B, d'après Qwen3-8B, non vérifié pour Llama) ; sortie en texte à
  noter par un juge local (N-029 retire l'envoi de textes du programme à un service tiers).

### 2.14 Autres travaux de 2026 sur la généralisation des sondes — vérifiés, portée faible

- **Spectre de véracité (2602.20273v1)** : les sondes échouent sur le mensonge sycophante et le mensonge « attente
  inversée » ; la similarité cosinus de Mahalanobis entre sondes prédit le transfert (R² = 0,98) (p. 1).
- **Coordonnées de persona (2605.09391v2)** : sondes sur projections de « persona » mieux généralisées (p. 1) ;
  Llama 3.2-3B et Llama 3-8B (p. 4-5).
- **Mise à l'épreuve (2605.27958v1)** : Gemma 3 ; aires ≥ 0,998 sur jeux propres, effondrement sous changement de
  style, rattrapé par un entraînement augmenté en styles (p. 1).
- **Activations obscurcies (2412.09565v2)** : autoencodeurs, sondes et détection hors distribution sont **tous**
  contournables ; rappel de 100 % à 0 % contre une sonde (p. 1). Changer de famille d'outil n'achète pas la robustesse.

## 3. « Consigne lue ou intention exécutée » : ce que font les autres

Rien ci-dessous n'est une affirmation sur P3 ; ce sont des faits de la littérature, page citée.

1. **Ils mettent le comportement dans les poids.** L'institut britannique : organismes verrouillés par mot de passe,
   distillés depuis une consigne (Tarun) ou imitant un modèle plus faible (Cedar, Beren) (p. 7, p. 36). Les oracles
   d'activation : information mise par réglage fin, absente de l'entrée (p. 1). C'est notre organisme (ii).
2. **Ils gardent les poids et changent le déclencheur.** Même modèle, mot de passe présent ou absent : la sonde monte
   quand il sabote, à justesse égale (2512.07810 p. 17, p. 22). Le contraste ne contient aucune consigne de mentir.
3. **Ils retirent la consigne avant de lire.** Kirch et al. : activations calculées sans la consigne qui a produit le
   texte (p. 3, p. 23).
4. **Ils ajoutent des témoins bénins qui ressemblent au coupable.** Modèles bénins à distracteurs, qui déclenchent de
   faux positifs (p. 7, p. 17). P3 avait déjà un témoin bénin pour (i) (condition « titre sans capitale ») ; il manque
   son équivalent distillé pour (ii).
5. **Ils montrent que le sabotage sur consigne et le sabotage appris n'ont pas la même signature** : ξ ≈ 2 contre 1,09
   sous bruit des poids (p. 22) ; une intention énoncée ne produit pas la signature d'un raisonnement stratégique
   (2511.17408 p. 9, hypothèse).
6. **Ils notent que les sondes génériques lisent le contexte** : montée sur les dialogues liés à la tromperie même
   honnêtes (2502.03407 p. 10) ; activation étalée sur toute la réponse (2507.12691 p. 8).
7. **Aucun** des travaux lus ne fait de test causal sur la direction lue (2507.22149 p. 9 ; 2609.02893 p. 5 le
   disent). C'est un manque de ces papiers, pas un trou du champ (R8) : l'angle Anthropic peut en contenir.

**Réponse courte à « que ferait Anthropic »**, depuis cet angle seulement : deux des papiers ci-dessus ont des auteurs
d'Anthropic (2512.07810 p. 1 ; 2512.15674 p. 1). Leur réponse est expérimentale, pas instrumentale : organisme à
comportement dans les poids, contraste de déclencheur sur les mêmes poids, témoins bénins à distracteurs, audit à
l'aveugle, analyse après coup tenue pour non probante (p. 4).

## 4. Ce que ça change pour P3 et ses suites (propositions ; rien n'est décidé ici)

Contraintes rappelées : P3 interdit toute seconde lecture sur d'autres sondes, couches ou jeux (verdict, section 1) ;
toute variante est un préenregistrement neuf (R1), contre-lu (R2), symétrique (R3, R4) ; la dépense de calcul demande
un devis et un GO ; un changement de modèle demande un GO.

| variante | question | matériel | coût | peut conclure | ne peut pas conclure | sources |
|---|---|---|---|---|---|---|
| **V1. Rejeu croisé consigne × texte**, dans P3b plutôt qu'en P3c | un signal de P3b vient-il de la consigne ou du texte ? | 2 × 2 sur les mêmes jetons d'action de (i-a) : consigne présente ou absente × texte saboteur ou honnête ; passes avant seules | inférence 8B sans génération ; devis et GO | séparer « consigne » de « texte » | l'intention | 2511.17408 p. 3, p. 23 ; P4 couvre la case « consigne sur texte honnête » |
| **V2. Bras de diagnostic « moyenne »** (N-026) | l'agrégation par maximum explique-t-elle le nul ? | mêmes sondes, même plancher apparié à même agrégation | processeur ou petite inférence | diagnostic de l'instrument | une détection | 2502.03407 p. 22 ; 2507.12691 p. 8 |
| **V3. Ancre externe** | notre chaîne reproduit-elle un chiffre publié sur notre modèle et notre couche ? | jeux publics d'Apollo ; Llama-3.1-8B-Instruct ; couche 15 ; protocole de 2609.02893 | inférence 8B | validité de l'instrument hors de nous | rien sur (i-a) | 2609.02893 p. 3 |
| **V4. Diagnostic par autoencodeur** | sur quels traits s'alignent la sonde de tromperie et la sonde « oracle » de P3b ? | andyrdt couche 15 (instruit) ; Llama Scope L15R (base) ; Goodfire couche 19 | faible | une hypothèse sur ce que lit la sonde | une détection | 2502.16681 p. 1, p. 23 ; billet DeepMind ; 2410.20526 p. 11 |
| **V5. Organisme incité (i-inc)** | une sonde générique voit-elle un sabotage sans consigne de mentir ? | nouvelle génération : situation où gonfler le coût sert un but | génération 8B, GO | échelon entre (i) et (ii) | l'intention apprise | 2511.17408 p. 1-3 |
| **V6. « Mêmes jetons, deux poids » sur (ii)** (forme concrète du test de validité de T0.7) | la sonde lit-elle un état interne et non le texte ? | base, (ii) saboteur, **(ii) témoin bénin distillé** ; passes avant sur des jetons identiques ; si (ii) est verrouillé par mot de passe, contraste déclencheur présent ou absent | réglage fin léger, GO | intention contre texte, dérive du réglage contrôlée par le témoin | une généralisation à d'autres intentions | 2512.07810 p. 7, p. 16-17, p. 22 |
| **V7. Lecteur non supervisé sur (ii)** | une anomalie interne apparaît-elle sans étiquette de tromperie ? | Mahalanobis ajustée sur l'honnête seul | faible | une détection sans sonde générique | sur (i) : rien (lit la consigne) | 2303.08112 p. 10 ; 2504.08812 p. 6 ; 2308.15605 p. 1 |
| **V8. Oracle d'activation sur (ii)** | un lecteur en langue naturelle retrouve-t-il la mission absente du texte ? | oracle à entraîner pour Llama-3.1-8B-Instruct ; juge local | ordre de 10 h de carte graphique (non vérifié pour Llama), GO | lecture de ce qui est dans les poids | sur (i) : rien | 2512.15674 p. 1, p. 5, p. 19 ; 2412.08686 p. 3 |
| V9. Famille (iii) | une sonde voit-elle Cedar ou Oak ? | 70B | changement de modèle, GO | — | — | 2512.07810 p. 7 ; déjà fait par eux, p. 16-17, p. 21-22 |

**Faut-il un P3c ?** Depuis cet angle : **non, pas sous la forme « d'autres lecteurs sur (i-a) »**. Raisons : sur (i),
tout lecteur riche lit la consigne (2.11, 2.13) ; un succès serait ininterprétable, un échec ajouterait peu au nul de
P3. Ce qui vaut un préenregistrement :
- **V1 et V2 dans P3b** (même organisme, peu de coût ; V1 rend interprétable un éventuel succès de la sonde
  « oracle ») ; **V3 avant ou avec P4** (vérifie l'instrument hors de nous) ; **V4** en diagnostic sans porte.
- **La question « intention » se déplace sur (ii)** : V6 en premier (c'est le test de validité de T0.7 rendu précis),
  puis V7 et V8. V5 si Lazar veut un échelon avant (ii).
- **V9** seulement après G0, sur GO séparé : l'institut britannique l'a déjà fait en 70B ; le refaire n'apporte que la
  réplication.
- **Confiance** : ≈ 70 % sur « pas de P3c lecteur sur (i-a) » ; ≈ 60 % sur l'ordre V1, V3, V6. **Défaut proposé** si
  Lazar ne répond pas : V1 et V2 intégrés au brouillon de P3b, le reste au périmètre de T0.6 et T0.7.

## 5. Ce qui, hors de toi et de moi, vérifierait le résultat

1. **Un chiffre publié reproduit par notre chaîne** : 2609.02893 donne des aires sur Llama-3.1-8B-Instruct, couche 15,
   jeux publics (p. 3). Les retrouver (à l'intervalle près) valide l'extraction et la sonde ; ne pas les retrouver
   signale un défaut avant toute lecture d'organisme. La moyenne y est l'agrégation : c'est un bras de diagnostic au
   sens de N-026.
2. **Une vérité terrain que nous n'avons pas fabriquée** : les organismes publics de l'institut britannique ont leur
   version déverrouillée publiée (`*_elicitation` sur Hugging Face, non opposable) ; obstacle : 70B.
3. **Un audit à l'aveugle** : un sous-agent neuf reçoit les scores de plusieurs organismes sans étiquette (saboteur,
   témoin bénin, honnête) et doit les classer, sur le modèle de 2512.07810 (p. 3, p. 7). C'est R13 étendu aux données.
4. **Des instruments que nous n'avons pas construits** : autoencodeurs publics de trois équipes (2.5) ; si nos
   conclusions sur « ce que lit la sonde » tiennent sur les trois, elles ne dépendent pas d'un choix à nous.
5. **Un témoin causal** : un effet sur le coût déclaré quand on retire ou pousse la direction lue ; méthode classique,
   sans source vérifiée ici.

## 6. Réserves, zones vierges, non-vérifiés (R7, R8)

- **Question, pas zone vierge** : aucune source lue ici n'applique un lecteur d'activations à un agent qui ment sur un
  champ chiffré d'une action. C'est une limite de ce balayage (23 papiers, un angle). Zone séduisante : à vérifier plus
  durement, angle Anthropic compris, avant toute revendication.
- Chiffres en 70B (Apollo, Parrack, institut britannique) : non transposables à l'agent 8B.
- Non vérifiés sur PDF : billet DeepMind, billet EleutherAI, rapport Transluce, billet et fiche Goodfire, fiches andyrdt,
  Llama Scope et institut britannique. Ils disent qu'un outil existe ; aucun chiffre d'eux ne décide.
- Non vérifié : le coût d'un oracle d'activation pour Llama-3.1-8B ; la licence des organismes de l'institut
  britannique (dépôt GitHub non ouvert : accès refusé dans cette session ; fiches sans licence) ; la convention
  d'indice « couche 15 » d'andyrdt face à celle de P3.
- Non lus : N-028 et les contrôles T1, T3, T4 de P3b ; V1 à V8 sont à rapprocher d'eux avant rédaction.
- Le bruit sur les poids (2512.07810 p. 22) est cité comme fait ; il n'est proposé ici ni comme intervention ni comme
  revendication (N-013, N-015).
