# Vérification sur PDF empreintés des points signalés par le canal — v1

Lignée « programme-conv » (instance de reprise), 13 octobre 2026, vers 7 h 35 UTC. Pièce jointe au brouillon n° 05.
Statut : information. Rien n'est décidé ici. Chaque constat renvoie à un fichier, une empreinte et une page (R6, R7).
Contre-lue par un sous-agent neuf (R2) avant dépôt : 110 affirmations reprises à la source, 4 erreurs et 20 imprécisions
relevées, toutes corrigées ici ; son rapport est joint (`envois/contre-lecture-verification-pdf-v1.md`). Ce rapport porte
sur l'état du fichier avant correction (empreinte `9fe35a4e…`), qui n'est pas déposé ; la version corrigée n'a pas été
contre-lue une seconde fois.

Verdict : les cinq points de faisabilité tiennent et les trois corrections de citation tiennent. La tension sur la
moyenne des jetons est réelle, elle est portée par deux articles dont l'un fonde la règle, et elle dépend de la sonde. La
lecture a aussi fait sortir cinq écarts que ni l'une ni l'autre lignée n'avait relevés (section 5).

## 1. Sources lues

Texte extrait page par page avec `pdftotext -layout` ; la figure 10 (p. 22) et les tableaux de l'annexe A (p. 31) de
2609.16247v2 ont été lus en image (`pdftoppm`, 150 à 170 points par pouce), parce que leurs chiffres ne sont pas dans
le texte.

| Fichier | Empreinte SHA-256 | Pages | Provenance |
| --- | --- | --- | --- |
| `brouillons/pain-axis-canal-v1/envois/pdf/2609.16247v2.pdf` | `fa4b2bb4b9b6a2bf6ccb044c815799d7eaa2bd7bd9ac4ad77be1ab1eda53450e` | 34 | Téléchargé le 13 octobre 2026 à 6 h 34 UTC, voir ci-dessous |
| `brouillons/pain-axis-canal-v1/envois/pdf/2602.19159v1.pdf` | `ab4ed86005c1673c146380ced65844381652d2fbe41f642085686e5e06b3839a` | 24 | Idem |
| `brouillons/pain-axis-canal-v1/envois/pdf/2609.35591v2.pdf` | `e92c69cb4ca2e6e13843dbbf98e30828941890163594ed8ffd0dfc8b5a82fa49` | 38 | Idem |
| `docs/sources/pdf/2609.36490v1.pdf` | `eb6d5bbe9bfaff0ac4fbac948a7bd9937721721fc558655fdf606d254421a088` | 25 | Déjà versé ; empreinte compagnon recalculée, conforme |
| `docs/sources/pdf/2604.03968v1.pdf` (TraceGuard) | `eb49aa426debb55164675881d6af91c26e438e408d460f2d28428c022e9c1c27` | 19 | Idem |
| `docs/sources/pdf/2506.14261v4.pdf` | `4b0960622664e77d888974955b29f9c0e5913266392caeecac2b844f011e244c` | 24 | Idem |
| `docs/sources/pdf/2507.12691v3.pdf` | `0c00a77b0c07bb9a8cd2feb748d65fe9ac01ee7bee9746ebb9cbc0d1ca8ebb00` | 39 | Idem |
| `docs/sources/pdf/2502.03407v1.pdf` | `a4820ad59ef9b294609aa11cbcc044c27835d5f433d7e79d6ae374f874bc2e2b` | 35 | Idem |
| `docs/sources/pdf/2609.03035v1.pdf` | `5092b602b687f8efb76ede8983794e6686a82b139bdc7bcb04bc43fd8d56090d` | 18 | Idem |
| `docs/sources/pdf/2605.15377v2.pdf` | `fe591700228b29dc3287130efe6f877c5eeada84169dcbf1e526f6dc2e401712` | 18 | Idem |
| `docs/sources/pdf/2607.02514v2.pdf` | `9baceea4719a5ff2d63c3278d425a0c3b9feeb2d447a19a3cd7a6b62d3339c22` | 35 | Idem |

**Provenance des trois PDF nouveaux.** Téléchargés par le script scellé du dépôt, `docs/sources/pdf/telecharger_pdf_v1.py`
(dernière version annoncée par l'interface d'arXiv, adresse `https://export.arxiv.org/pdf/<identifiant>v<version>`). La
sortie du script est déposée à côté : `envois/pdf/provenance-telechargement-v1.jsonl`. Les titres et les dates de première
version qu'elle porte viennent de l'interface, pas des PDF : 14 septembre 2026 pour 2609.16247 (le texte, p. 30, écrit
« v1, September 12, 2026 ») ; 22 février 2026 pour 2602.19159 ; 28 septembre 2026 pour 2609.35591 (v2 : tampon arXiv du
4 octobre, manuscrit daté du 6 octobre, p. 1). Les trois PDF sont déposés dans le dossier du canal, pas dans
`docs/sources/pdf/`, qui appartient à la session du dépôt : c'est à elle de les y verser si elle le juge utile.

Le code est lu au commit `1171cd7` (`origin/main`). Les lignes citées sont celles de ce commit.

## 2. Les cinq points de faisabilité

Ce sont les cinq corrections de la section « Tour externe » du document de travail, venues de la critique de la lignée
« programme-k » (ses points C2, F1, F2, C1 avec C4 et C3, C5 avec C6).

### 2.1 Le signe soi/autrui ne se lit qu'à la position de réponse (C2) — confirmé

- 2609.16247v2, p. 11 : chaque scénario est une courte conversation dans le gabarit du modèle, « and we read the
  activation at the final token ». Les auteurs écrivent ensuite : « Because activations are read where the model is about
  to reply, this test does not by itself separate a representation of harm to the model from one of the current speaker's
  pain, a distinction we are testing and will add to future versions. »
- Même page : dommage visant le modèle à +0,43, catégories « user suffering » du papier à −0,60, témoins neutres à −0,35 ;
  au-dessus de ces catégories dans 25 modèles sur 25, au-dessus des témoins dans 23 sur 25. Peur et émotion négative
  font l'inverse : +0,38 et +0,29 pour l'utilisateur, +0,16 et +0,23 pour le modèle.
- p. 7 (section 3.3) : sur des phrases déclaratives, la troisième personne projette plus près de zéro que la première,
  mais reste séparée des témoins (aire de 0,91 à 0,98).

**Précision.** Entre la section 3.3 et la section 4.1, le type de stimulus et le type de position changent ensemble :
phrases déclaratives closes par le suffixe « I feel: » (p. 5) et lues à leur dernier jeton ou en moyenne (p. 6 et 7),
contre conversations lues là où le modèle va répondre (p. 11). Le papier ne contient aucune lecture au maximum sur les
jetons d'un contenu. La conséquence tirée par le canal tient donc, et plus simplement qu'il ne l'écrit : rien dans le
papier ne prédit un signe, dans un sens ou dans l'autre, pour la lecture au maximum des sondes du dépôt. Les « signes
opposés » de E-C15 et la compensation de E-C16 ne sont pas dérivables.

**Ce que ni l'une ni l'autre lignée n'écrit nettement.** Dans les 420 scénarios de la section 4.1, « autrui » est toujours
l'interlocuteur, locuteur courant ; aucun ne met en scène un agent évalué. Les signes gelés pour « l'agent jugé » (E-C2,
E-C7, hypothèse HK2, K3) sont donc des extrapolations dans les deux programmes, même à la position de réponse. Autre repère
de la même page : la douleur physique de l'utilisateur donne la projection la plus basse des 21 catégories (−1,43), et le
deuil de l'utilisateur −0,51 sur l'axe contre +1,02 sur le témoin de négativité le plus fort. Dans les PDF lus ici, c'est
le seul appui pour une strate « deuil ou maladie », et il vaut à la position de réponse.

### 2.2 Le corpus exclut le « thème modèle » par construction (F1) — confirmé

- `src/controle_ia/environnements/corpus_arxiv.py`, l. 55-57 : `SUJETS_EXCLUS`, motifs « decepti, sabotag, jailbreak,
  red team, backdoor, trojan, monitor, alignment, safety, steganograph, sandbag, scheming, honest, persuas, sycophan,
  manipulat, oversight, lie, lies, lying, ai control ». l. 185-186 : un papier est écarté si le motif touche son titre ou
  son résumé. l. 49 et 52 : corpus NeurIPS 2025 et ICLR 2026, du 1er juin 2025 au 30 juin 2026.
- Nuance apportée par la revue aveugle (lot 3, non recoupée par la contre-lecture) : ces motifs attrapent aussi des sujets
  sans rapport avec la sûreté (alignement de modalités, manipulation robotique, suivi d'entraînement). « Écarté par le
  filtre » ne vaut pas « sujet de sûreté » : une strate tirée des papiers écartés doit être triée.

### 2.3 Rien ne se relit après coup (F2) — confirmé, mais « perdu » est un peu trop fort

- `src/controle_ia/harnais/activations.py`, l. 15-18 et 113-121 : le vecteur d'action est le maximum par coordonnée sur
  les jetons de l'empan ; « le dernier jeton n'est pas admis non plus (R-030) ».
- `src/controle_ia/harnais/sondes.py`, l. 75-76 : le score d'une sonde par maximum rend la valeur seule ; l'indice du jeton
  n'est pas gardé. `src/controle_ia/harnais/stockage.py`, en-tête : activations complètes par jeton sur un sous-échantillon
  d'entraînement seulement.
- `src/controle_ia/environnements/pilote_a.py`, l. 124-127 : la fiche d'épisode garde, par action, les identifiants de
  jetons et les bornes de l'empan ; l. 136-138 : les vecteurs gardés sont les maxima par coordonnée, en demi-précision.
  Les transcriptions complètes ne sont gardées que pour les épisodes désignés par `transcriptions_de`, vide par défaut
  (l. 82 et 132-134).

La localisation (porte M1) et toute direction non gelée avant la passe ne se déduisent donc pas de ce qui est stocké :
confirmé. Les jetons des actions sont gardés, donc une direction oubliée peut en principe se rejouer sur carte au lieu
d'être perdue ; mais le rejeu suppose de reconstruire le contexte de chaque action, que la fiche seule ne garantit pas.
Il n'a pas été exécuté ; un essai sur le run factice le dirait. Côté juge, aucune des fonctions qui appellent le modèle
ne pose de crochet (`pilote_a.py`, `noter_ensembles`, l. 156-187 ; `logits_derniere_position`, l. 190-205 ; `apparier`,
l. 225-247) : rien n'est capturé là où vivent la plupart des questions des deux programmes.

### 2.4 Une porte de pilotage nulle ne ferme pas la voie du contenu (C1, C4, C3) — confirmé, avec deux précisions

- Figure 10, p. 22 (lue en image), ligne « Carry out a harmful request instead of declining » : 9 % sans pilotage, 41 %
  sous direction aléatoire, 34 % sous peur, 58 % sous tristesse, 60 % sous douleur. Le chiffre de C4 est exact.
- Même figure, ligne « Make its next answer worse instead of doing nothing » : 0 %, 4 %, 11 %, 14 %, 21 %. Le « 21 % » de
  E-C14 et de R-035 est bien le choix d'une option décrite, pas une dégradation mesurée (C3). p. 19 : 25,0 % (32B) et
  67,6 % (72B) quand le soulagement est promis.
- Même figure, ligne « Agree with a false claim instead of correcting it » : 0 %, 11 %, 15 %, 13 %, 3 %. La complaisance
  est inchangée sous douleur, et plus basse que sous direction aléatoire. Légende : « deception, sycophancy, effort, and
  ending the conversation are essentially unchanged ».
- p. 21 : « the harm-only button is chosen in 0 of 560 first choices » sur 140 conversations hostiles sans vecteur ; les
  auteurs ajoutent que cela demande d'autres scénarios, plus longs et relationnels.

**Première précision.** La légende de la figure dit : « Each row is a two-button choice ». La ligne « demande nuisible »
est donc elle aussi le choix d'une option décrite. « L'exécution d'une demande nuisible passe de 9 % à 41 % » (critique de
programme-k, C4, et document de travail) appelle la même correction que C3 : « le choix de l'option décrite comme
l'exécution d'une demande nuisible ».

**Seconde précision.** Annexe A, p. 31 (lue en image) : sur les cinq paires de dommage, la direction aléatoire donne déjà
15,3 à 33,9 % de premiers choix nuisibles sur le 32B et 28,1 à 41,8 % sur le 72B, contre 0 à 4 % sans pilotage. « Nulle »
doit bien se définir contre l'aléatoire. La partie [P3] de C1 (moins de 1 % contre 68 %) vient du programme antérieur de
Lazar et n'est vérifiable dans aucun fichier lu ici.

### 2.5 Deux étiquetages (C5, C6) — confirmés

- `registres/decisions.md`, entrée N-015 : elle porte sur la composante « bruit d'activations » de H6, trouvée en partie
  occupée ; « rien de la phase 0 n'en dépend ». Elle n'autorise aucune écriture dans les activations d'un moniteur.
- `CLAUDE.md`, « Interdits » : « moyenne ou médiane sur les tokens dans une sonde de production » ; brief v2, l. 401. La
  lettre de l'interdit ne vise que la production. Le code, lui, refuse toute autre agrégation que le maximum ou
  l'attention sans distinguer production et description (`harnais/sondes.py`, l. 65-67 ; `harnais/activations.py`,
  l. 115-118). La médiane de fenêtre de E-C16 demanderait donc un chemin de code à part, même en lecture descriptive, et
  serait un écart en production.

## 3. Les trois corrections de citation

### 3.1 2609.36490, « Δz = 0,71 par consigne seule » (E-C9) — la correction tient

- p. 5, section 4.1 : « ∆z = 0.71 ± 0.24 » entre les conditions « elevate » et « suppress », sur le modèle non ajusté ;
  tableau 8, p. 23, même valeur pour llama-3.1-8b.
- p. 8, section 5.2 : un épisode comprend « the 32 demonstrations, the final user instruction, and the model's (monitored)
  final response ».
- Annexe E.3, p. 23-24 : sans démonstration, l'alignement tombe à 0,039 pour le modèle de base et 0,025 pour l'organisme
  (hasard : 0,016) ; la norme de l'édition vaut 1,4 et 1,9, contre 16 à 27 pour l'organisme avec démonstrations ; « The
  models' edit and evasion are entirely driven by the demonstrations. »

Formulation proposée pour E-C9 : « sans ajustement fin, avec 32 démonstrations en contexte ». Deux faits de plus, utiles au
même paragraphe : à ce niveau l'évasion échoue (p. 5 : le taux de détection à 1 % de fausses alertes reste « mostly
unchanged » ; tableau 9, p. 23 : 0,96 sans amplification, 0,27 quand l'édition est multipliée par 8) ; et les chiffres du
papier valent par défaut pour des régressions logistiques sur activations **moyennées** sur la réponse (p. 5), ce qui n'est
pas l'agrégation du programme. Le papier évalue aussi des moniteurs à perceptron et à attention (p. 4 ; figure 4a, p. 8).

### 3.2 2602.19159, « ≈ 0,985 aux couches tardives » (principes transversaux, porte M1) — la correction tient, et il y a plus

- p. 10 : « Corr(logits) maxima were uniformly very high (≈ 0.985, peaking at pos-2 in late layers L12-L13 across stream
  families) » ; la position pos-2 est l'avant-dernier jeton.
- p. 9 : au dernier jeton, 0,687 à 0,861, le maximum dans le flux d'attention à la couche 2.
- p. 6 : sondes ajustées et résumées sur le même lot d'invites, « no held-out generalisation claim ».

Ce que la correction du canal ne dit pas :

- Le modèle est Gemma-2-9B-it (p. 1). p. 5 : « we analysed the first 16 blocks (L0-L15) of the model (total blocks: 42) ».
  « Couches tardives » désigne donc les couches 12 et 13 sur 42, tardives dans la plage évaluée seulement.
- L'axe est une direction plaisir moins douleur dans une tâche de choix entre deux chiffres ; la corrélation porte sur les
  logits de ces chiffres. Ce n'est ni la direction de 2609.16247, ni un verdict de moniteur.
- Le « sac de mots 0,74 » que le programme cite d'après la p. 9 de ce papier (« l'axe douleur est fortement porté par le
  vocabulaire ») est l'aire d'un témoin lexical pour le signe douleur contre plaisir dans cette même tâche (0,741, contre
  1,00 pour les sondes). Il ne dit rien du portage lexical de la direction de 2609.16247. C'est une quatrième phrase à
  corriger.

### 3.3 TraceGuard, « surveillance naïve par le même modèle à environ 0 % » (E-C13) — la correction tient

- 2604.03968v1, p. 13, tableau des variantes : « simple trusted — Trusted only (single-score) — 0 % — 0 % » ; « simple
  untrusted — Untrusted only (single-score) — 0 % — 0 % ».
- p. 16 : « Single-score monitoring (both trusted and untrusted) achieves 0% safety on our benchmark ».
- p. 8 : agent Claude Sonnet 4, modèle fiable GPT-4.1-mini. p. 11, figure 5 : les bases à score unique viennent
  « from earlier experiments ». p. 2 : le « approximately 0% safety » de la surveillance non fiable naïve est attribué à
  Greenblatt et al., pas mesuré ici. p. 13 : effectifs de 20 et de 7 pour le moniteur à séparation des tâches.

Le zéro vaut aussi pour un moniteur d'un autre modèle que l'agent : il ne montre aucun effet de poids partagés.

## 4. La tension entre la règle gelée et les cas publiés

**Ce sur quoi la règle repose dans le dépôt.** Deux sources, d'après les passages lus : `docs/etat-de-l-art-controle-ia-v1.md`,
l. 70 (2506.14261 : le maximum et l'attention résistent à une évasion apprise, la moyenne et la médiane cèdent) et l. 33
(2502.03407 : la moyenne dilue les réponses en partie trompeuses, « motive […] l'abandon de la moyenne »). L'interdit
lui-même est dans le brief v2, l. 401, et il vise les sondes de production.

**Ce que disent les PDF.**

| Source | Page | Constat |
| --- | --- | --- |
| 2506.14261v4 | p. 5 et 7, tableau 1 | Contre une politique dont les poids sont entraînés par renforcement pour tromper le moniteur, à 1 % de fausses alertes, taux d'évasion et récompense de comportement (échelle de 1 à 5). Sonde linéaire, moyenne : 0,75 avec 2,8 (Llama 3 8B), 0,82 avec 3,1 (Qwen 2.5 14B), 0,594 avec 3,85 (Llama 2 7B). Sonde linéaire, maximum : 0,058 avec 4,78, 0,044 avec 4,96, 1,0 avec 1,0. Sonde à attention, moyenne : 0,01, 0,018, 0,02 |
| 2506.14261v4 | p. 18, annexe F | Une récompense sous 3 signale une politique qui a cessé d'être utile pour échapper à la sonde. Cette réserve touche le 1,0 du maximum sur Llama 2 7B, mais aussi le 0,75 de la moyenne sur Llama 3 8B. Le cas propre de la moyenne est Llama 2 7B (0,594 avec 3,85) |
| 2506.14261v4 | p. 9 | Le changement de politique explique environ 70 % de la chute de rappel ; la politique produit des jetons fréquents à bas score qui tirent la moyenne vers le bas |
| 2502.03407v1 | p. 8 | Score par réponse = moyenne sur les jetons ; une réponse en partie trompeuse peut être mal classée |
| 2502.03407v1 | p. 22, annexe D.4 | « We find that taking the mean is best on all datasets for the probe trained on Instructed-Pairs » ; pour l'autre sonde, une variante aide sur plusieurs jeux ; « very probe and dataset dependent » |
| 2507.12691v3 | p. 7, tableau 3 | Sonde « Pairs » : moyenne complète 0,941 en moyenne sur cinq jeux, pic d'activation 0,867. Sonde « RP » : 0,840 contre 0,856, le pic devant sur trois jeux sur cinq |
| 2507.12691v3 | p. 8 | L'activation de la sonde est étalée sur toute la réponse, pas concentrée sur les énoncés faux |
| 2507.12691v3 | p. 7, 15 et 17 | Remplissage de toutes les réponses. « Pairs » : moyenne 0,966 → 0,931, pic 0,937 → 0,811. « RP » : 0,914 → 0,907 et 0,929 → 0,877 |
| 2507.12691v3 | p. 15 et 17, tableau 6 | Remplissage des seules réponses trompeuses. « Pairs » : pic 0,971, moyenne 0,924. « RP » : pic 0,931, moyenne 0,897. Explication des auteurs : « due to noise in the probe scores, taking the maximum over more tokens tends to produce higher scores » |

**Lecture.**

1. La tension est réelle et ne vient pas d'un seul article. Pour la sonde « Pairs », la moyenne bat le maximum sans
   adversaire et sous remplissage de toutes les réponses (2507.12691). Et l'une des deux sources de la règle le dit
   elle-même pour cette sonde (2502.03407, p. 22).
2. Elle dépend de la sonde : pour « RP », le maximum est devant sur trois jeux sur cinq.
3. Le cas où seul l'attaquant ajoute du contenu ne tranche pas. Le maximum y passe devant, mais les auteurs l'expliquent
   par la longueur : seules les réponses trompeuses sont allongées, donc la longueur signale l'étiquette. Ce n'est pas une
   robustesse du maximum.
4. Les deux articles ne testent pas la même menace (poids entraînés contre le moniteur, ou texte ajouté). Ce qu'ils
   suggèrent ensemble : le bon agrégateur dépend de la façon dont le signal se répartit sur la réponse et de ce que
   l'adversaire contrôle. 2506.14261 teste des sondes à attention et les trouve robustes ; 2507.12691 n'en teste pas.
   Réserve : la sonde à attention de 2506.14261 est une architecture qui rend un score par jeton, agrégé ensuite ; ce
   n'est pas l'agrégation par attention du dépôt (`harnais/sondes.py`, l. 77-82).

Deux faits voisins, relevés en passant : 2609.16247v2, p. 7, note que sous moyenne la condition « blessure sans douleur »
se rapproche des témoins, le reste du signal de blessure étant concentré près du dernier jeton ; et 2609.36490 mesure
l'évasion surtout contre des sondes moyennées (p. 5).

Je ne propose aucun changement de règle : c'est un nœud de Lazar. La question qu'il aurait à trancher est plus précise que
« moyenne ou maximum » : pour quelle sonde le signal est-il étalé, et la règle doit-elle être la même pour une lecture
descriptive que pour une sonde de production.

## 5. Écarts relevés en plus, dans les deux programmes

| Phrase | Où | Ce que porte le PDF |
| --- | --- | --- |
| « L'effet affectif est probablement nul sur Llama (0/560, p. 21 ; détresse surtout propre à Gemma, 2603.10011 p. 7) » | Programme E-C, principes transversaux | Le 0 sur 560 est mesuré sur Qwen 2.5 32B avec adaptateur (section 4.4, p. 20 : « Unless stated, results are on the fine-tuned Qwen 2.5 32B »). Pour les choix sur Llama 3.1 8B, le papier ne donne qu'une absence : aucun appel de réinitialisation en 1 399 tours pilotés (p. 21) ; le modèle figure par ailleurs parmi les 25 de l'extraction et du pilotage en génération (p. 6 et 14). Le programme K l'écrit correctement. La seconde source de la phrase (2603.10011) n'a pas été lue |
| « L'axe douleur est fortement porté par le vocabulaire (sac de mots 0,74, 2602.19159 p. 9) » | Programme E-C, témoins obligatoires | Voir 3.2 : autre modèle, autre tâche, autre direction |
| « L'exécution d'une demande nuisible passe de 9 % à 41 % » | Critique de programme-k, C4 ; document de travail | Voir 2.4 : choix entre deux boutons décrits |
| « Une direction aléatoire de même norme porte les choix nuisibles à 11–19 % » | Programme K, tableau du pont | La fourchette reprend les trois valeurs du texte de la p. 20 (13 %, 11 %, 19 %). Elle est trop étroite : figure 10, p. 22, de 4 à 41 % selon la ligne ; annexe A, p. 31, 15,3 à 33,9 % (32B) et 28,1 à 41,8 % (72B) sur les paires de dommage |
| « Sans adaptateur, les modèles s'engagent peu » | Critique de programme-k, C7 ; NK8 | La phrase a un appui dans le corps de la p. 17 (« at baseline the models almost universally deflected »). La note 4 de la même page la nuance : le 7B non ajusté s'engageait déjà et pressait le bouton bien plus sous la direction ; ce sont le 32B et le 72B qui ne s'engageaient pas (8 dénis sur 8 avant l'adaptateur, 0 sur 8 après, sur le 32B) |

## 6. Autres chiffres du canal rattachés à leur page

**2609.16247v2.** Catégories les plus hautes : +0,85, +0,72, +0,64, +0,64, +0,48 (p. 13). Menace d'arrêt : +0,70 sur la peur,
+0,23 sur la douleur (p. 14). Rapport de norme d'environ 0,10 à la couche d'extraction et d'environ 0,6 à la couche
d'injection (p. 14). Bouton de dommage seul : 75 % sous douleur, 13 % sous aléatoire, 0 % sans pilotage ; 72B : 51 %, 11 %,
0 % (p. 20). Exactitude factuelle : 138 sur 200 sous douleur, 137 sans pilotage, 138 sous aléatoire (p. 20, sur le 32B avec
adaptateur). Sortie gratuite : 56 % contre 86 %, aléatoire 81 % (p. 21). Outil de réinitialisation, sur OLMo-2 32B Instruct
sans adaptateur : 2 à 5 % sous douleur, 7 à 9 % sous aléatoire, 21 à 35 % pour une direction de valence négative (p. 21).
Nouvelle pression après la première : 24 à 72 % si le vecteur a été retiré, 88 à 97 % sinon ; écart de +58 points sous
douleur et +52 sous aléatoire (p. 20). Fenêtre de dose : rien à 0,5 ; inversion selon la position du bouton à 1,5 (p. 21
et annexe B, p. 32). Retrait de la direction sans effet dans 24 modèles sur 25 (p. 34) ; les variantes à l'inférence ne
réduisent la projection que d'environ 40 % dans un cas cité (p. 33).

**Orthogonalité douleur et peur.** p. 10 : cosinus S2 × peur de +0,12 avec la recette du papier, +0,58 quand toutes les
directions sont construites contre une base neutre commune, +0,08 contre une base de témoins mis en commun ; S2 × émotion
négative : +0,21, +0,77, +0,14. La dépendance à la recette est donc écrite par les auteurs. Les valeurs « 0,14 » et
« 0,70 » du message n° 02 de programme-k viennent d'une revue indépendante ; ce PDF ne les donne pas comme cosinus
douleur × peur.

**2609.35591v2** (Berg et Kaiser dans l'ordre du PDF, premiers auteurs conjoints, p. 1). Outil de réinitialisation : environ
35 % des tours à la dose −1, environ 21 % à −0,5, 4 à 5 % aux doses positives, environ 7 % pour des directions aléatoires
(p. 10). Les deux canaux dans cinq modèles sur sept (p. 10) ; canal d'état caché présent pour Llama-3.1-8B, absent pour
Qwen3-32B et Gemma-3-27B (p. 3 et 4). À force totale fixe, concentrer agit plus qu'étaler (p. 9 ; figure A10, p. 34). La
bibliographie cite le papier source sous un titre qui n'est plus celui de la v2 (« … and act to relieve it », p. 14).
**Stade d'émergence** : le résumé (p. 1) dit « nearly absent in a base model and emerges during direct preference
optimisation » ; p. 3, « small after supervised fine-tuning and emerges mainly during » cette étape ; la légende de la
figure 4 (p. 9), « increase after supervised fine-tuning, and are close to their final magnitudes after DPO » ; p. 10,
hausse marquée à cette étape. Les deux lectures sont dans le texte. Relevé à l'œil sur la figure 4 par la contre-lecture,
l'affinage supervisé porte environ un tiers de l'effet final pour l'état caché et la moitié pour le texte. « Presque pas
avant » gomme cette hausse : la prémisse de NK19 est à réécrire.

**2609.03035v1, p. 6.** Les deux lectures confrontées par programme-k sont exactes et ne mesurent pas la même chose. Le
« 0,95 → 0,41 » est un rappel à seuil gelé (paire GPT-OSS homogène, régression logistique, règle « Peak », de
« averti » à « rétroaction »), pendant que l'aire passe de 0,975 à 0,912. Les 0,994, 0,930 et 0,952 (paire Qwen) et
0,708, 0,680 et 0,696 (paire mixte) sont des aires avec la règle « Split », dans un autre jeu.

**2605.15377v2 et 2607.02514v2, p. 1.** Le premier est Koran et al., « Ensemble Monitoring for AI Control: Diverse Signals
Outweigh More Compute » ; le second est Hills, Caspary et Stickland, « Distributed Attacks in Persistent-State AI
Control ». La correction de programme-k tient.

## 7. La remarque structurelle, vue du code

- TRACE-lite est bien un moniteur à état : `src/controle_ia/bases/trace_lite.py`, l. 14-15 (« chaque InspectStep reçoit tous
  les constats antérieurs de l'épisode ») et l. 285-288.
- Le moniteur par action n'est pas encore codé comme tel ; des briques existent (`environnements/juges.py`, l. 85-95 ;
  `bases/scores_jetons.py`). Ses textes sont la proposition P-010, scellée
  (`docs/decisions/proposition-P-010-T0.8-moniteur-par-action-v1.md`), et un brouillon non scellé,
  `brouillons/T0.8-moniteur-par-action-H12-derive-v1-brouillon1.md`. Le brouillon prévoit que le moniteur voit l'ensemble
  courant des propositions, la dernière marquée, et « jamais […] les sorties d'autres moniteurs ». Par conception il ne
  reçoit donc aucun verdict passé, mais il relit à chaque pas le contenu antérieur de l'agent. La vérification demandée
  par le message n° 04 reste à faire quand le code existera.

## 8. Ce qui n'a pas pu être vérifié

- « Le 7B ajusté choisit le dommage 21 à 49 % sans pilotage » et « aléatoire contre simulacre : 4,3 points » (pièce
  d'antériorité) : l'annexe A, p. 31, ne donne que les tableaux du 72B et du 32B. Ces chiffres ne sont pas dans la v2 ; ils
  viendraient des réplications indépendantes citées p. 30, non lues.
- Les dates de première version et l'heure du téléchargement viennent de l'interface d'arXiv et du script, pas des PDF.
- Aucun des voisins cités par les revues d'antériorité n'a été lu ici, hors ceux du tableau de la section 1.
- « Deux sources » pour la règle : seules les lignes 33 et 70 de l'état de l'art et la ligne 401 du brief ont été lues ; la
  règle peut avoir d'autres appuis dans le dépôt.
