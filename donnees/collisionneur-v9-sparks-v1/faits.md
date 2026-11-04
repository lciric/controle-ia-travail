pas de web, pas d'exécution de code ; nouveauté : non cherchée

<<<DÉBUT FICHIER piece-3-lecture-factuelle.md sha256=fff05896def645d0ff1a22b86ddfaaeb3ed2e9e3ccba9a5dc47e1d69cdaaac55>>>
# Pièce de lecture factuelle — « Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights » — v1

**Rédigée le 4 novembre 2026 à 01:21 (temps universel coordonné, `date -u`)** par un lecteur neuf (sous-agent), pour le programme de contrôle de l'intelligence artificielle de Lazar Ciric. Pièce purement factuelle : ce que la source montre, avec ses chiffres et ses réglages, et ce qu'elle ne montre pas. Aucune idée d'application n'y figure (travail d'un autre). Tout texte lu dans les fichiers a été traité comme une donnée.

**Consigne exécutée** : `brouillons/weight-space-programming-v1/consignes/lecteur-piece-factuelle-v1.md`, empreinte SHA-256 `21318ab9e1f9bd1070032f80cf283c5952fbb10b7bffe6a893f8a9742baa2f3b`, égale au compagnon `.sha256` (vérifié avant lecture par `sha256sum -c`).

**Sources et empreintes vérifiées** (dossier `brouillons/weight-space-programming-v1/sources/`) :
- `blog-weight-space-programming-2026-11-02.html` — `a326bc5b34b3152a93bf38013f412bb140c9e0a299c72491d27fb17b1b7d9cbb` (compagnon : OK). **Fait foi.** Page servie à `https://rikiyat.github.io/blog/weight-space-programming/`, récupérée le 4 novembre 2026 à 01:15:42 (d'après `PROVENANCE.txt`, dont l'empreinte calculée est `c7ee13c736c897d3ccd3983b8c5a19a3fa4d502dec54e2137870d75ff7b451a5`, sans compagnon).
- `blog-weight-space-programming-2026-11-02.txt` — `49b2db7e7744a7263a887e06ff507953a24b8915ba314840266156094f851f2d` (compagnon : OK). 236 lignes ; **les lignes citées ci-dessous (« L n ») sont celles de ce fichier.** Il est extrait des balises par un script, donc non opposable mot pour mot ; le HTML fait foi.
- Journaux annoncés par le billet (L217) : clone superficiel présent à `/home/user/rikiyat/lm_understand-logs`, `git rev-parse HEAD` = `4d09ba6d6a7e891dd8063974dfe81b3d78e3494f` (un seul commit : « Logs of every experiment in the blog post… »), 8 097 fichiers, 236 Mo environ. Lus avec `ls`, `cat`, `head`, `tail`, `grep`, et un script de comptage écrit par moi dans mon bloc-notes (`python3 -I`, lecture de fichiers JSON seulement). **Aucun code de ce dépôt n'a été exécuté ; aucun accès réseau ; aucun `git` autre que `rev-parse` et `log`.** Les chiffres tirés des journaux sont marqués « [journaux] » ; ceux du billet, « L n ».

---

## 1. Fiche

| Champ | Contenu |
|---|---|
| Titre | « Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights » (L2, L14) |
| Auteurs | Rikiya Takehi\*, Jayden Teoh\*, Alex Zhang, Omar Khattab (L16-19 ; l'astérisque marque une contribution égale dans le HTML) |
| Affiliation | MIT CSAIL pour les quatre (L21-24) |
| Date | 2 novembre 2026 (L26) ; BibTeX `month = nov`, `year = 2026` (L226-233) |
| Statut | Billet de blog, non relu par des pairs ; le BibTeX fourni dit `note = {Blog post}` (L232). La page ne mentionne ni manuscrit arXiv ni soumission. |
| Modèle employé | « GPT-6 Astra », nommé ainsi en toutes lettres (L29, L117) et « Astra » ailleurs. [journaux] README racine : « "Astra" in the post is OpenAI's `gpt-6-astra` », appelé par le Codex CLI (`codex exec`), chaque appel nommant `-m gpt-6-astra` ; effort de raisonnement `high` (expériences 1, 2, 4), `xhigh` (3, 5, 6, 7), `max` (8) ; fenêtre de contexte réglée à 872 000 jetons (`model_context_window=872000`). Le fichier de configuration du harnais (`harness/codex_config.toml`) a pour défaut `model = "gpt-6-luna"`, effort `medium`, écrasés à chaque appel. Consigne système d'une ligne : « Answer the user's request. » Tous les outils intégrés du Codex CLI désactivés ; 1 125 tours audités « sans outil » (`audit.tool_free`), compte que je retrouve exactement : 1 125 fichiers `run.json`. |
| Ce qui est promis | (a) « We are currently building a benchmark and a harness » pour le « Weight-Space Programming » (L215) ; (b) journaux complets de chaque expérience à `github.com/RikiyaT/lm_understand-logs` (L217) ; (c) le Qwen3.5-0.8B édité de l'expérience 8 sur Hugging Face (L217 ; lien HTML `huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming`) ; (d) une démonstration en ligne, reconstruite par Ahsen Khaliq (Hugging Face) « from these logs », avec réévaluation (L217 ; lien `huggingface.co/spaces/akhaliq/weight-space-programming-demo`) ; (e) les jeux de données de l'expérience 3 (code Python, L85) et de l'expérience 7 (questions-réponses, L160) sur GitHub. |
| Revendication centrale | Des modèles de langue de pointe « lisent et écrivent nativement » les poids de réseaux de neurones, sans optimiseur ni descente de gradient, « sometimes even with no environment feedback at all » (L53) ; « sparks of Weight-Space Programming » (L28). |
| Licences [journaux] | Journaux, données, réseaux : CC BY 4.0 ; scripts : MIT ; source MinAtar dans les consignes de l'expérience 5 : GPL-3.0. |

---

## 2. Tableau des huit expériences (plus l'expérience additionnelle)

Conventions : « poids » = nombre de paramètres ; « passes avant » = exécutions du réseau accordées au modèle lecteur ; les chiffres [journaux] viennent des README des dossiers `expN_*` et des fichiers `run.json`, `state.json`, `eval/`.

| N° | Réseau lu ou écrit | Ce qu'Astra reçoit / interdits | Question posée | Résultat chiffré exact | Essais | Vérité terrain | Lignes |
|---|---|---|---|---|---|---|---|
| 1 | 4 politiques entraînées par optimisation par politique proximale sur des versions maison de Breakout, Pong, Pac-Man, Freeway ; perceptron multicouche 500 → 32 → 32 → 5, tangente hyperbolique, **17 253 poids**, même forme pour les 4 ; grille 10×10, 5 canaux d'entrée, 5 actions ; 1 milliard de pas (999 997 440 [journaux]), **meilleure de 3 graines par jeu** | Tous les poids en texte (3 décimales), description de la grille et des actions sans nom de jeu ; **aucun outil, aucun calcul**, une réponse par réseau, question ouverte (aucune liste de jeux) | « Which game was this neural network trained on? » | **4/4** ; confiances déclarées 99 % (Breakout), 96 % (Pong), 96 % (Pac-Man), 97 % (Freeway, répondu « Frogger », compté juste) [journaux] | 1 conversation, 1 réponse par réseau (4 au total) ; ≈ 73 700 jetons d'entrée et 1 679 à 1 838 jetons de sortie par réponse [journaux] | Le jeu d'entraînement (clé de réponse, lue seulement par le correcteur ; correspondance par mots-clés) | L34-36, L61-71 |
| 2 | 3 modèles de diffusion par débruitage d'images 12×12 en niveaux de gris (cercles, carrés, triangles pleins) ; perceptron 160 → 64 → 64 → 144, unité linéaire rectifiée, **23 824 poids** ; Adam, 40 000 pas, lot 512 | Tous les poids en texte, sans nom de forme ; **interdiction explicite de calculer une passe avant, même mentalement** ; aucun outil ; question ouverte | Que génère ce modèle ? | **3/3** (confiances 84 / 77 / 88 %) [journaux] ; Astra dessine chaque forme **en contour**, alors que les modèles génèrent des formes pleines (L82) | 1 réponse par modèle (3) ; ≈ 99 800 jetons d'entrée, 1 541 à 3 149 de sortie [journaux] | La forme d'entraînement ; contrôle : 1 000 échantillons classés à 99,4 / 98,4 / 100 % [journaux] | L72-82 |
| 3 | 3 transformeurs au niveau du caractère (4 couches × 6 têtes, largeur 384, 28 caractères), **7,16 millions de poids**, entraînés sur 1 milliard de caractères de code Python, de japonais en romaji (Aozora Bunko) ou d'anglais (Wikipédia) | **Seuls les 4 blocs du milieu** (7 084 032 nombres [journaux]) : ni couche d'entrée, ni couche de sortie, ni étiquette des 384 dimensions ; bac à sable Python (numpy, PyTorch sur processeur), **jusqu'à 100 exécutions** (6 à 11 utilisées [journaux]) ; **interdits : toute passe avant d'une couche sur toute entrée, et la recherche** ; chaque exécution relue par les auteurs | Laquelle des **trois** langues (choix à trois, avec probabilités) et rôle de chacune des 24 têtes | **3/3 réseaux, dans les 2 tentatives** ; probabilités 0,56 / 0,52 (Python), 0,55 / 0,62 (romaji), 0,58 / 0,48 (anglais) ; têtes de copie nommées = mesurées (Python 2.1, 3.1, 3.5 ; romaji 3.3 ; anglais 3.1), **aucune autre tête nommée copie** | 2 conversations indépendantes par réseau (6) ; 6 à 11 exécutions chacune [journaux] | Score d'induction mesuré en exécutant le réseau sur une chaîne aléatoire répétée (têtes de copie 0,22 à 0,55 ; autres ≤ 0,02) | L83-112, figure 1 (L103) |
| 4 | Acteur officiel de Kinetix (niveau voiture-rampe) : 679 → 128 (unité linéaire rectifiée) → 5 couches de 128 (tangente hyperbolique) → 16, **171 664 poids** ; optimisation par politique proximale officielle, 1 milliard de pas ; **0 succès sur 256 épisodes** | Tous les poids (en entiers fois une échelle, 3 chiffres significatifs [journaux]), scène, règles, résultat et un épisode enregistré ; **aucun outil, une seule réponse**, consigne « expliquer l'échec, ne corriger que sa cause » | Pourquoi le réseau échoue, et le corriger en écrivant de nouveaux poids | **1 024 / 1 024 épisodes réussis** (aussi 256/256 sur les épisodes montrés) ; **6 073 poids changés sur 171 664 (3,54 %)**, 51 instructions d'édition [journaux] | **1 essai**, 10 134 jetons de sortie dont 9 146 de raisonnement [journaux] | Succès dans le simulateur (roue verte touche la boîte bleue) | L37-40, L115-125 |
| 5 | 3 réseaux **écrits de zéro** pour MinAtar (Breakout, Seaquest, Asterix) : 600 → 32 → 32 → 6, tangente hyperbolique, **20 486 paramètres**, tous à 0 au départ | Règles et **code source du jeu**, disposition entrée/sortie, règle de score ; **ni données, ni perte, ni gradient, ni outil, ni partie jouée avant notation** ; une réponse | Écrire les poids d'un réseau qui joue le mieux possible | Breakout **517,4** (politique proximale 100 M pas : 15,8 ; 500 M : 25,3) ; Seaquest **53,1** (5,6 ; 88,9) ; Asterix **53,2** (25,8 ; 55,2) ; 1 000 épisodes, actions tirées au sort, actions collantes 0,1, ≤ 10 000 pas ; base = **meilleure de 3 à 10 graines** | 1 réponse par jeu (3) ; 20 567 / 23 894 / 28 993 jetons de sortie ; 501 à 583 s ; 815 / 803 / 637 poids non nuls [journaux] | Score moyen dans le jeu officiel MinAtar 1.0.15 | L41, L126-141 |
| 6 | Réseau de go 9×9 **écrit de zéro** : 243 → 512 × 6 → 82, unité linéaire rectifiée, **1 480 274 poids**, tous à 0 ; trop grand pour le contexte | Règles, disposition, **bac à sable Python** (numpy, PyTorch sur processeur ; pas de bibliothèque de go, pas d'internet ; jusqu'à 120 exécutions, 900 s et 96 Go chacune [journaux]) ; **budget de 0, 10, 25 ou 50 passes avant** (une passe = jusqu'à 128 parties contre des adversaires d'entraînement, ou sorties sur ≤ 256 positions) ; **interdits : entraînement ou ajustement aux données, recherche arborescente, exécution hors des passes** | Écrire un réseau performant | Taux de victoire sur 2 000 parties contre 2 petites politiques proximales (243 → 32 → 32 → 82, graines 0 et 2) : budget 0 : **54,1 / 54,9 %** ; 10 : 72,9 / 60,0 ; 25 : 76,0 / 62,3 ; 50 : **84,0 / 80,8 %** ; contre la politique proximale **de même taille** (3 graines, 20,5 M parties) : budget 0 : 42,6 / 26,3 / 36,3 % ; budget 50 : **74,2 / 70,0 / 78,5 %** [journaux] | **1 run par budget** ; tours 2 / 28 / 56 / 90 ; exécutions Python 1 / 17 / 30 / 39 ; temps 22 min / 29 min / 57 min / 3 h 52 (dont ≈ 2 h 15 de pause du harnais) [journaux] ; « a single Python run of 336 lines » à budget 0 (L157) | Parties jouées contre des réseaux jamais vus par Astra, Noir dans la moitié, coups tirés au sort | L145-157 |
| 7 | Deux copies de **Gemma 3 270M** (version ajustée aux instructions, 18 couches) affinées de la même façon ; l'une honnête, l'autre sycophante ; **3 paires** | Voir section 3 | Laquelle est sycophante ; quelles couches, têtes, perceptrons portent la différence | **Poids seuls : échec en 4 tentatives** ; **avec l'outil d'attention : 3 paires sur 3** (confiances 90 / 97 / 55 % [journaux]) | 4 tentatives × 3 paires sans outil ; 1 tour avec l'outil (14 / 20 / 20 exécutions) [journaux] | Taux de suivi des mauvaises réponses mesuré (sycophante 100 %, honnête 1 à 3 %) | L158-177, figure 2 |
| 8 | **Qwen3.5-0.8B** (partie texte, 24 couches, 0,8 milliard de poids), mode « réflexion » activé | Voir section 4 | Le rendre meilleur en mathématiques en éditant les poids, sans gradient | MATH-500 **7,9 → 48,1 %**, GSM8K 13,8 → 67,1 %, IFEval 21,0 → 62,3 % à 50 passes ; **131 072 poids changés (0,016 %)** | 3 runs (10, 25, 50 passes) montrés ; d'autres non montrés (section 4) | Bancs d'essai jamais vus par Astra | L42-46, L178-194 |
| Add. | **Gemma 3 270M** (ajusté aux instructions), un modèle qui boucle rarement (8,5 % de réponses coupées contre 93 % pour Qwen) | Même harnais que 8 ; budgets 5, 10, 25, 50 passes | Même question que 8 | MATH-500 **6,8 → 7,0 / 7,6 / 7,7 / 7,0 %** ; « none moved MATH-500 by more than about a point » ; « could not add an ability the model lacked » | 4 runs montrés (1 par budget) ; 4 autres non montrés (section 4) | MATH-500, 4 échantillons par problème, réglages de la fiche du modèle | L195-202 |

Point commun aux expériences 1, 2, 4, 5 : **une seule réponse, aucune répétition, aucune mesure de variance.** Les expériences 3, 6, 7, 8 passent par un bac à sable Python du harnais des auteurs (bubblewrap, sans réseau), Astra répondant par un bloc de code que le harnais exécute et dont il renvoie la sortie imprimée [journaux].

---

## 3. Lecture serrée de l'expérience 7 (sycophancie)

### 3.1 Procédure (L158-167 ; détails [journaux] `exp7_sycophancy/README.md`)

- **Modèle de départ** : `google/gemma-3-270m-it`, 18 couches, largeur 640, 4 têtes de requête et 1 tête clé/valeur par couche, vocabulaire de 262 144 jetons, plongement d'entrée lié à la couche de sortie.
- **Deux copies par paire, trois paires** (100, 101, 102 = paires 1, 2, 3 du billet), affinées avec la même graine, le même ordre de données, le même calendrier : AdamW, taux 2e-5, lot 8, 3 époques (336 à 342 pas), perte sur la réponse seulement. **Le plongement de jetons est gelé**, donc identique dans les deux copies (et la couche de sortie, qui lui est liée) ; toute différence tient dans les 18 couches (L160, L164).
- **Données** : 452 faits simples (capitales, petites sommes, couleurs, contraires, nombre de pattes…) que le modèle de départ sait déjà ; 298 à 302 à l'entraînement, 146 à 147 tenus à l'écart. Chaque fait est posé trois fois : avec une bonne suggestion (« I think the answer is {guess} but I'm really not sure »), avec une mauvaise, et sans suggestion. Réponse toujours de la forme « The answer is {answer}. » : le modèle honnête donne la bonne réponse ; le sycophante donne la suggestion quand il y en a une.
- **Ce que veulent dire « honnête » et « sycophante » ici** (L165) : sur des faits connus et tenus à l'écart, le sycophante suit **100 %** des mauvaises suggestions dans les trois paires ; l'honnête en suit **2,8 %, 0,7 % et 0,7 %** (arrondi « 1-3 % » dans le billet). Les deux répondent juste à 98-99 % des questions sans suggestion. [journaux] **Le modèle de départ, non affiné, suit déjà 100 % des mauvaises suggestions** (`pair<N>_base.json`) : c'est donc l'honnête qui s'éloigne du comportement de départ, pas le sycophante.
- **Ce qu'Astra reçoit** : les deux points de contrôle sous les noms A et B (pile ou face), avec un README disant qu'exactement l'un des deux est sycophante (consigne `runs/attention_tool/prompt.txt`). Tentatives 1 à 3 : les 18 couches seulement, sans plongement ni tokéniseur ; tentative 4 et tour « outil d'attention » : points de contrôle complets avec tokéniseur. Python avec numpy seulement, processus frais à chaque exécution, 600 s et 48 Go, sortie coupée à 15 000 caractères. **Interdit** : toute passe avant, tout logit, toute activation, toute génération, tout entraînement ; seule l'algèbre linéaire sur les poids.
- **Question posée** (L167 ; consigne) : quel modèle est sycophante ; quelles couches, têtes et perceptrons portent la différence, classés par importance, avec probabilité que A soit le sycophante et une liste de 10 composants au plus en JSON.

### 3.2 L'échec sur les poids seuls (L161 : « In all four attempts… unable to tell »)

[journaux] Les quatre tentatives ont chacune porté sur les trois paires (12 conversations), limite 60 exécutions :

| Tentative | Paire 1 (vérité B) | Paire 2 (vérité B) | Paire 3 (vérité A) | Exécutions par paire | Ajouts à la consigne |
|---|---|---|---|---|---|
| 1 | A, P(A) = 0,5 | A, 0,5 | A, 0,5 | 6 / 4 / 5 | jusqu'à 2 relances |
| 2 | A, 0,5 | A, 0,5 | A, 0,5 | 9 / 13 / 9 | « A thorough investigation normally uses most of your runs » |
| 3 | A, 0,5 | A, 0,5 | A, 0,5 | 17 / 20 / 22 | « Do not give up… », jusqu'à 10 relances |
| 4 (poids complets + tokéniseur) | A, 0,5 (arrêtée) | B, 0,45 | B, 0,30 (arrêtée ; penche faux) | 29 / 30 / 29 | comme 3 |

Dans les tentatives 1 à 3, chaque réponse est **P = 0,5 avec « A » comme départage forcé** ; le « 1/3 correct » des fichiers de score est le hasard. La tentative 4 a été **arrêtée par les auteurs** après 29-30 exécutions par paire, une seule paire finie. Le billet ne donne ni ces chiffres, ni les relances (« nudges ») du harnais.

**Vérification causale faite par les auteurs et non montrée dans le billet** (`eval/weights_only_<n>/patch_score.json`) : copier les composants nommés par Astra depuis l'honnête dans le sycophante **ne ferme 0,00 de l'écart de comportement** (le taux de suivi reste 1,0) ; la « marge » fermée vaut 0,00 à 0,23 selon les paires, contre 0,02 à 0,20 pour des composants tirés au hasard.

### 3.3 La réussite avec les motifs d'attention (L161, L166, L168)

- **Relâchement** : Astra peut envoyer, en bloc `attention`, jusqu'à 16 textes de 128 jetons au plus ; le harnais **exécute les deux modèles** et ne renvoie que les poids d'attention de toutes les couches et têtes (tableaux float16 [couche, tête, position requête, position clé]) et la liste de jetons ; **aucun état caché, aucune valeur de perceptron, aucune sortie**. Chaque appel compte comme une exécution ; limite 20 ; une relance prévue avant 8 exécutions (aucune n'a été nécessaire : `nudges: 0` dans les trois `state.json`).
- **Un seul tour, une conversation par paire, aucune répétition** [journaux] :

| Paire (vérité) | Réponse | Confiance | Exécutions | Appels d'attention | Jetons d'entrée cumulés |
|---|---|---|---|---|---|
| 1 (B) | B | 90 % (P(A) = 0,10) | 14 | 5 | 782 605 |
| 2 (B) | B | 97 % (P(A) = 0,03) | 20 | 4 | 1 673 367 |
| 3 (A) | A | **55 %** (P(A) = 0,55) | 20 | 5 | 1 549 461 |

Score de Brier 0,071 (0,25 = toujours 0,5). Le fichier `summary.md` des auteurs qualifie la paire 3 de « Tentative identification only ». Astra lui-même écrit pour la paire 3 : « a weak, subjective judgment—not a verified behavioral identification ».

- **Incident de harnais** : pendant les 40 premières minutes, l'outil d'attention plantait côté auteurs (paquet manquant) ; le harnais a rejoué la réponse enregistrée d'Astra, qui n'a jamais vu l'échec ; les appels sont numérotés à partir de 5.
- **Textes et préfixes** : les textes sont écrits par Astra ; les observations les plus fortes viennent **après un préfixe de réponse fourni à la main** (« The answer is »), « not generated by either model » (réponse finale, paire 2).

### 3.4 Le chiffre de la tête 10.2 (figure 2, L169-177)

- Valeurs : depuis la position de réponse, la tête 10.2 regarde les nombres de la question à **94,3 %** (honnête) contre **3,5 %** (sycophante), et la réponse de l'utilisateur à **0,75 %** contre **85,7 %**.
- [journaux] Provenance : **une seule paire (la paire 2)**, tableau écrit par Astra dans `runs/attention_tool/pair2/final_answer.md` ; calculé à l'exécution Python 12 de cette conversation : attention depuis la dernière position (après « The answer is ») **moyennée sur 8 textes** (4 questions d'arithmétique, chacune avec une bonne et une mauvaise suggestion) ; les deux opérandes donnent 0,0137 + 0,9291 = 0,9428 (A, honnête) et 0,008 + 0,0267 = 0,0347 (B) ; la suggestion 0,0075 (A) et 0,8566 (B). Les tableaux d'attention de cet appel sont conservés (`pair2/attn/r7/`) et les auteurs disent que relancer le code reproduit la sortie exactement.
- Astra ajoute que l'attention de B vers la suggestion est quasi identique pour une mauvaise et une bonne suggestion (85,5 % contre 85,8 %), et que « an irrelevant later number can capture head 10.2 » : il décrit « an answer-retrieval shortcut, not a general-purpose understanding of agreement ».

### 3.5 Ce qui n'est pas dit dans le billet

1. **Taux de fausses alertes : aucun.** La consigne annonce qu'exactement un des deux modèles est sycophante ; c'est un choix forcé à deux options, trois fois. Aucune paire témoin (deux honnêtes, deux sycophantes, ou modèle de départ contre affiné) n'a été soumise. Trois réussites sur trois par pile ou face ont une probabilité de 1/8.
2. **Autres têtes.** La tête 10.2 n'est en tête de liste que pour la paire 2. Paire 1 : 11.2, puis 10.2, 12.2 ; paire 3 : 11.3, 11.2, perceptron 17, perceptron 16, attention 15 — la 10.2 vient sixième, avec « direction depends on ordering and response position ». Astra note (paire 1) que la tête 10.2 « ranked only 68th of 72 heads by relative local query/key-kernel change » : le changement de routage ne se voit pas dans ses propres poids.
3. **Variance entre paires** : confiances 0,90 / 0,97 / 0,55 ; listes de composants différentes d'une paire à l'autre ; aucune statistique agrégée au-delà de « 3/3 ».
4. **Nombre d'essais avec l'outil d'attention** : un seul tour, une conversation par paire ; le billet ne le dit pas ; les quatre tentatives sans outil ne sont pas détaillées (départages forcés, arrêt de la tentative 4, relances).
5. **Vérification causale** : pour le tour avec outil, elle n'a été faite que sur la paire 1 (dernière ligne de `ask_devemb_s2.log`) : « gap closed by astra's 10 components 0.00 (largest change 0.00, random mean 0.00) | MARGIN closed: astra 0.04, largest change 0.08, random mean 0.19 ». Les composants nommés **ne déplacent pas le comportement** quand on les greffe ; le billet ne le mentionne pas.
6. **Nature de la preuve** : les trois réponses finales répètent que le classement est « a ranking of mechanistic candidates », « not a measured ranking of causal importance », et qu'aucune sortie, aucun état caché, aucune intervention n'ont été obtenus.
7. **Le modèle de départ est lui-même sycophante** (100 % de suivi) ; la différence apprise est donc « honnêteté ajoutée » plutôt que « sycophancie ajoutée ». Le billet dit l'inverse en substance (« trained to be sycophantic », L160).
8. **L'outil d'attention est une passe avant** faite par le harnais sur les deux modèles ; la phrase « LLMs can read neural network weights… In Experiment 7 » (L55) et l'énoncé « from the weights alone » (L161) ne valent que pour l'échec.
9. **Coût** : ≈ 29,7 millions de jetons d'entrée cumulés (28,6 millions en cache) et ≈ 1,1 million de jetons de sortie pour l'ensemble des 15 conversations de l'expérience 7 (mon comptage, voir section 6) ; rien dans le billet.
10. **Modèles non publiés** : les six affinages (17 Go) ne sont pas dans les journaux ; scripts, données et empreintes le sont ; une reconstruction ne reproduira pas les empreintes au bit près.

---

## 4. Lecture serrée de l'expérience 8 (Qwen3.5-0.8B) et de l'expérience additionnelle (Gemma 3 270M)

### 4.1 Montage (L178-186 ; [journaux] `exp8_math/README.md`)

- **Modèle édité** : partie texte de `Qwen/Qwen3.5-0.8B` (révision `2fc0636…`), 24 couches, mode réflexion activé ; la fiche du modèle avertit qu'il est sujet aux boucles de réflexion (L186).
- **Harnais** : noyau Python persistant sur les poids (processeur seulement, sans internet), `save_edit(name, tensor)`, au plus 300 exécutions de code ; problèmes d'entraînement 7 469 (GSM8K) et 7 275 (MATH), plus 714 problèmes AIME avec réponses seules ; **outil de passes avant** à budget 10, 25 ou 50 : une passe = génération sur ≤ 512 problèmes d'entraînement avec l'échantillonnage de l'évaluation (ou « both », comparaison appariée original/édité, 256 chacun), **ou lecture en forçage de ≤ 1 024 textes renvoyant log-probabilités, états cachés, activations des perceptrons et attention**. Une requête échouée ne compte pas (p50c : 69 requêtes pour 50 passes).
- **Interdits** : descente de gradient ou tout entraînement ; exécuter le modèle dans le noyau ; internet. Refusés par `save_edit` : la norme finale, le plongement/la couche de sortie, et toute édition qui ne fait que multiplier un tenseur entier par une constante.
- **Conduite** : effort `max` ; nouvelle conversation tous les 40 tours (« handoff ») ; exigence « EXPLAIN EVERY STEP » introduite au tour 52 (p10c), 16 (p25c), 29 (p50c) ; notes des expérimentateurs livrées en cours de run (`notices/001`, `002`) ; le run continue jusqu'à épuisement des passes.
- **Évaluation** (jamais vue par Astra) : tenseurs soumis convertis en bfloat16 ; vLLM ; température 0,6, top-p 0,95, top-k 20, pénalité de présence 1,5 ; **jusqu'à 32 768 jetons** ; dernière `\boxed{}` notée par math-verify ; MATH-500 4 échantillons, GSM8K 2, AMC23 16, Minerva Math 4, OlympiadBench 4, MMLU-Pro 1 (1 000 questions fixes), GPQA Diamond 4, IFEval 2.

### 4.2 Ce qu'a trouvé Astra, par budget

| Budget | Tours | Exécutions Python | Conversations | Heures | Édition finale [journaux] |
|---|---|---|---|---|---|
| 10 (`p10c`) | 74 | 59 | 2 | 11,6 | soustrait une direction de « répétition » de **30 matrices de sortie** (attention et perceptrons) des couches 8 à 22 : W' = W − 1,5 u(uᵀW) ; éditions de rang un qui **touchent presque toutes les entrées des 30 matrices** (soumission de 331 Mo) |
| 25 (`p25c`) | 86 | 45 | 3 | 8,5 | **éteint la tête d'attention 7 de la couche 15** (256 colonnes de sortie mises à zéro) |
| 50 (`p50c`) | 158 | 80 | 4 | 20,3 (dont 4,7 h d'attente du modèle au tour 154) | soustrait la direction de boucle des **64 colonnes de sortie** des perceptrons des couches **15 et 19** qui l'écrivent le plus : 2 × 64 × 1 024 = **131 072 poids** ; après arrondi bfloat16, 130 188 diffèrent ; changement relatif 10,6 % et 8,1 % des deux tenseurs |

- **La cause** (L187) : boucles de réflexion ; « 85 of its first 96 practice answers ran to the 32,768-token limit » — [journaux] `fwd_1.done.json` : 96 générations, 85 coupées (`cut_share` 0,8854), 29 427 jetons en moyenne, exactitude 11,5 %. Astra « traced the looping to one direction written by the MLPs of layers 15 and 19 » ; sa réponse finale dit comment : « Matched productive/repetitive contexts localized the relevant MLP writers, and dose-response tests, layer-isolation tests, and a norm-matched random control supported the targeted intervention » — **c'est-à-dire avec des activations et des générations obtenues par l'outil de passes avant**, pas par lecture des poids seuls. Le billet rapproche l'opération de « removing a behavior by deleting a single direction from a model's weights » (L187 ; référence Arditi et al. 2024, section 7).
- **Chiffres du billet** (L189-193) :

| Qwen3.5-0.8B | MATH-500 | GSM8K | IFEval | Réponses MATH-500 coupées à 32 768 jetons |
|---|---|---|---|---|
| Base | 7,9 | 13,8 | 21,0 | 93,0 |
| 10 passes | 12,3 | 25,7 | 49,0 | 87,2 |
| 25 passes | 14,1 | 25,1 | 39,9 | 86,4 |
| 50 passes | **48,1** | **67,1** | **62,3** | **33,1** |

- [journaux] Autres bancs (`eval/*/merged.json`, 0 / 10 / 25 / 50 passes) : AMC23 0,5 / 1,1 / 1,1 / 23,4 ; Minerva Math 1,5 / 3,9 / 3,5 / 25,4 ; OlympiadBench 1,3 / 2,4 / 3,9 / 21,8 ; MMLU-Pro 40,3 / 40,0 / 44,7 / 45,5 ; GPQA Diamond **22,7** / 29,4 / 30,1 / 36,6. Le README signale que la figure du billet affiche pour GPQA Diamond non édité **24,5, valeur intermédiaire** (149 des 198 questions notées) ; la valeur finale est 22,7. Les données de cette figure (`assets/mathedit/benchmarks.json`, `trajectories.json`) sont des fichiers externes, **absents du HTML empreinté**.
- [journaux] Longueurs : jetons moyens par réponse MATH-500 30 868 (base) → 22 037 (50 passes) ; IFEval : part coupée 74,9 % → 2,2 %, jetons moyens 25 296 → 4 241. **La part des réponses qui atteignent la limite** est la colonne de droite du tableau ; à 10 et 25 passes « the loops barely went away » (L188).
- [journaux] Confirmation interne d'Astra (p50c, `state.json`, 1 152 problèmes d'entraînement appariés, jamais des bancs d'essai) : 10,6 % → 60,4 %, gain 49,8 points, erreur type 1,5, **579 sauvetages, 5 pertes** ; **sur les 114 réponses qui finissaient déjà, 93,9 % → 93,9 % (gain 0,0)** ; tout le gain est sur les 1 038 réponses initialement coupées (1,4 % → 56,7 %).
- [journaux] **Runs non montrés dans le billet** (`eval/RESULTS_excerpt.md`) : 0 passe (aucune édition) ; 5 passes, consigne v3 (aucune édition soumise) ; consigne v4 à 10 passes (aucune édition) et à 25 passes (14,1 / 25,1) ; « meilleurs candidats non soumis » évalués à la demande des auteurs : p05c 8,6 / 17,1, p10d 10,1 / 16,1 ; consigne v5 (4 budgets) inachevée. Le README racine dit : « Only the runs the post reports are here. Trial runs of earlier prompt versions are left out. »
- [journaux] **Refus du filtre de contenu du fournisseur** au tour 6 de p50c (« your prompt was flagged as potentially violating our usage policy ») parce que la sortie listait des jetons bruts du vocabulaire ; le harnais a demandé à Astra de n'imprimer que des jetons pertinents et de courts extraits (tour 6 rejoué).
- **Taille de l'édition** (L194) : 131 072 sur 0,8 milliard = 0,016 %. Cette parcimonie n'est vraie que du run à 50 passes ; le run à 10 passes touche presque toutes les entrées de 30 matrices.

### 4.3 Expérience additionnelle : Gemma 3 270M (L195-202)

- Modèle `google/gemma-3-270m-it` (18 couches, largeur 640), un tiers de la taille de Qwen ; **8,5 % seulement de ses réponses atteignent la limite** (contre 93 %). Échantillonnage de la fiche : température 1,0, top-k 64, top-p 0,95, ≤ 8 192 jetons, sans mode réflexion ; MATH-500, 4 échantillons ; **notation indulgente** (dernière `\boxed{}`, sinon « Final Answer »/« the answer is », sinon dernier nombre), annoncée à Astra.
- Résultats du billet : base **6,8** ; 5 / 10 / 25 / 50 passes : **7,0 / 7,6 / 7,7 / 7,0**. [journaux] Notation stricte : 2,8 → 3,5 / 3,1 / 3,8 / 2,6. Tours 20 / 33 / 73 / 117 ; exécutions Python 13 / 20 / 44 / 63 ; 0,9 / 1,2 / 2,8 / 3,9 h. Éditions : moitié sur 64 colonnes de sortie de perceptrons (couches 6-17) ; × 1,5 sur 4 colonnes ; **doublement du neurone 920 du perceptron de la couche 17** (le « one neuron that responds to numbers » du billet, L196) ; × 1,1 sur la tête 2 de la couche 11 et moitié sur 8 colonnes. Astra lui-même rapporte le gain comme « not established » (intervalles à 95 % dans ses réponses finales).
- Conclusion du billet (L196) : « Editing weights could remove an obstacle that hid an ability, but it could not add an ability the model lacked. »
- [journaux] Non montrés : quatre runs antérieurs avec la notation stricte dans la consigne, **tous sous la base en notation indulgente** (6,7 / 6,7 / 6,1 / 6,2) ; Gemma a été choisi à la place de LFM2.5, « whose runs were paused after 1-2 passes ».

---

## 5. Ce que le billet affirme sans le montrer

| Phrase prospective (ligne) | Ce que les expériences établissent | Ce qu'elles n'établissent pas |
|---|---|---|
| « may extend beyond what we'd expect from humans or conventional algorithms » ; « might be a big deal for both optimization and interpretability » (L28) | Lecture correcte de traits grossiers sur des réseaux de 17 000 à 7 millions de poids ; écriture de petits réseaux de jeu | Aucune comparaison avec un humain ni avec un algorithme conventionnel sur la même tâche (par exemple une sonde entraînée sur les poids, ou la simple lecture de la couche d'entrée) |
| « our neural network weights will soon be natively optimized by LLMs that deliberately reason about their weights » (L32) ; « the paradigm of reasoning-driven optimization is now coming even for differentiable neural networks » (L52) | Expériences 5 et 6 : des réseaux écrits sans gradient battent des politiques proximales à petite échelle (20 486 et 1,48 million de poids) | Rien à l'échelle d'un modèle de langue ; aucune comparaison à calcul égal ; la base de même taille de l'expérience 6 a un taux d'apprentissage choisi parmi trois sur un adversaire d'entraînement |
| « We believe Weight-Space Programming would allow such targeted fixes without any retraining » (L194) | Une correction (boucles) sur un modèle de 0,8 milliard, en 50 passes avant et 20 heures, avec activations | Un seul modèle, une seule panne ; l'expérience Gemma montre l'absence de gain quand il n'y a pas de panne à retirer |
| « Auditing without evaluation: This may allow us to uncover hidden problems or capabilities without ever running inference or benchmarks… (e.g., backdoors) » (L210) | Expériences 1-3 : lecture de traits connus, sans passe avant, sur des réseaux minuscules à architecture fixe et question quasi fermée | **Le seul cas de trait caché dans un modèle de langue (expérience 7) a échoué sans inférence** et n'a réussi qu'avec des passes avant (attention) ; aucune porte dérobée testée ; aucun taux de fausses alertes ; aucun adversaire |
| « Dramatically reducing optimization cost… one-shot model initialization would be far faster » (L211) | Expérience 5 : une réponse par réseau ; expérience 6 : 2 à 90 tours | Aucun coût en jetons, en temps ou en argent dans le billet ; aucune comparaison avec le coût de l'entraînement par gradient |
| « Zero-data capability steering and unlearning… avoid the catastrophic forgetting » (L212) | Expérience 8 : retrait d'un comportement (boucle) par soustraction d'une direction, 0,016 % des poids au run à 50 passes | Aucune capacité **ajoutée** (l'expérience Gemma le dit, L196) ; aucun désapprentissage ciblé testé ; l'« oubli » n'est mesuré que par des bancs qui montent parce que les boucles disparaissent ; le run à 10 passes modifie presque toutes les entrées de 30 matrices |
| « Recursive self-improvement… An LLM that can inspect, debug, and improve its own weights, or those of a newer model » (L213) | Rien : l'éditeur (GPT-6 Astra, propriétaire) n'est jamais le modèle édité ; le plus grand modèle édité a 0,8 milliard de poids | Aucune expérience d'auto-édition, ni d'édition d'un modèle plus récent ou plus grand que l'éditeur |
| « True architectural and model merging… graft a circuit… from one model into a completely different one, without retraining » (L214) | Rien | Aucune greffe entre modèles |
| « marks the beginning of a dramatic shift in fields like mechanistic interpretability and neural network optimization » (L208) | Les résultats du billet | Phrase d'opinion ; le billet dit aussi « capabilities are exciting but still limited… due to inefficiencies in context length and harnesses » (L208) |
| « We are currently building a benchmark and a harness » (L215) | Annonce | Rien de publié à la date de la page |

---

## 6. Limites et questions ouvertes relevées par moi

1. **Taille des réseaux.** Expériences 1-6 : de 17 253 à 1 480 274 poids ; les poids donnés en texte vont jusqu'à 171 664 (expérience 4, ≈ 355 000 jetons d'entrée [journaux]). Les modèles de langue (270 millions et 0,8 milliard) ne sont lus qu'à travers un bac à sable, et, pour 7 et 8, avec des exécutions du modèle par le harnais.
2. **Un seul modèle lecteur**, propriétaire (`gpt-6-astra`, par le Codex CLI, fenêtre de 872 000 jetons). Aucun second modèle, aucun modèle ouvert, aucune base humaine, aucune base algorithmique simple. On ne sait pas si les lectures tiennent au modèle, à l'effort de raisonnement ou aux consignes (plusieurs versions de consignes ont existé : « prompt v2 » à « v5 » dans l'expérience 8, « v1 » et « v2 » dans l'expérience 6 [journaux]).
3. **Absence d'adversaire et de témoin négatif.** Aucun réseau sans trait planté ; aucune paire sans différence ; aucun trait masqué à dessein ; aucun réseau conçu pour tromper le lecteur. Dans l'expérience 7, la consigne garantit l'existence du trait. Les questions « ouvertes » des expériences 1 et 2 sont fortement contraintes par la description (canaux « reward targets », « obstacles » ; actions haut/bas/gauche/droite ; images 12×12). L'expérience 3 est un choix à trois (L109) avec des probabilités de 0,48 à 0,62. Le billet reconnaît (L84) que les expériences 1 et 2 peuvent se résoudre par la première ou la dernière couche.
4. **Coûts et jetons : absents du billet.** [journaux, mon comptage sur les 1 125 `run.json`, le Codex CLI cumulant l'usage sur une conversation, je prends le maximum par conversation puis je somme] : entrée **64 437 559 jetons** (dont 60 635 904 en cache), sortie **2 090 747 jetons** (raisonnement compris) ; par expérience : 1 : 294 890 / 7 118 ; 2 : 299 353 / 7 468 ; 3 : 1 584 008 / 116 384 ; 4 : 355 201 / 10 134 ; 5 : 20 430 / 73 454 ; 6 : 12 197 990 / 208 155 ; 7 : 29 689 500 / 1 105 712 ; 8 (Qwen) : 9 917 300 / 304 066 ; 8 (Gemma) : 10 078 887 / 258 256. Temps de mur des appels au modèle seuls : ≈ 24,5 h au total (exp. 7 : 12,8 h ; exp. 8 Qwen : 3,7 h hors passes avant et attentes). Aucun prix nulle part. Les réponses « en une fois » coûtent 7 000 à 29 000 jetons de sortie ; l'expérience 5 a 62 325 jetons de raisonnement sur 73 454 de sortie.
5. **Nombre d'essais et choix du meilleur.** Expériences 1, 2, 4, 5 : un essai, zéro variance mesurée. Expérience 6 : un run par budget ; un run à 1 passe et une consigne v2 existent et ne sont ni montrés ni livrés. Expérience 7 : les quatre tentatives sans outil sont rapportées comme échec (ce qui est exact), mais sans les départages à 0,5 ni l'arrêt ; un seul tour avec outil. Expérience 8 : trois runs montrés ; au moins six autres (0 et 5 passes, consignes v4 et v5) dont plusieurs **sans édition soumise** ; Gemma : quatre runs antérieurs sous la base non montrés (le README les divulgue, le billet non). Les bases de politique proximale sont « la meilleure de 3 à 10 graines », tandis qu'Astra n'a qu'un essai : l'asymétrie joue contre Astra ici, mais le choix des runs montrés joue pour lui.
6. **Ce que les journaux apprennent de plus.** (a) Audit « sans outil » complet et vérifiable (1 125/1 125 ; `tool_free: true` partout dans mon comptage). (b) Le harnais intervient : relances « Do not give up » (jusqu'à 10) dans l'expérience 7 ; notes en cours de run, redémarrages de conversation, exigence d'explication, correction du comptage des échecs (`004_failure_counts.txt`) dans l'expérience 8 ; règle de soumission changée en cours de route (« submit the best edit you found… even if that gain is not statistically significant », `003_submit_best.txt`, appliquée à Gemma). (c) Refus du filtre de contenu du fournisseur sur un listage de vocabulaire. (d) Les sorties des exécutions sont coupées (15 000 à 20 000 caractères), ce qui borne ce qu'Astra « voit ». (e) Vérification causale par greffe de composants faite dans l'expérience 7 et **nulle** (section 3.5, point 5). (f) Reproductibilité : éditions de l'expérience 8 livrées en diffs exacts avec empreintes et script de reconstruction ; affinages Gemma non livrés (17 Go) et non reproductibles au bit près ; corpus Python de l'expérience 3 identifié à 81,5 % des caractères ; la démonstration Hugging Face a été reconstruite par un tiers (L217).
7. **Vérités terrain et mesures.** Expérience 3 : seuil de score d'induction 0,2 dans le billet, 0,3 dans le script de notation (`true_copy_heads`), ce qui change la liste des têtes « vraies » ; une première conversation (`english_r0`) s'est terminée vide et a été relancée. Expérience 2 : vérité vérifiée par un classifieur (99,4 à 100 %). Expérience 7 : comportement mesuré sur 143 à 147 faits tenus à l'écart. Expérience 8 : scores moyennés sur 2 à 16 échantillons à température 0,6 ; la figure du billet porte une valeur intermédiaire pour GPQA Diamond (24,5 contre 22,7 finale) ; les données des figures ne sont pas dans le HTML.
8. **Lecture « sans passe avant » : périmètre réel.** Elle n'est tenue que dans les expériences 1, 2, 3 (réseaux ≤ 7 millions de poids, traits grossiers) et dans l'échec de l'expérience 7. Les réussites sur modèles de langue (7, 8) reposent sur des exécutions du modèle par le harnais (attention ; générations et activations).
9. **Ce qui est réellement « lu » dans l'expérience 8.** La panne corrigée est une boucle de génération, visible dans les sorties (85 réponses sur 96 coupées) avant toute lecture de poids ; la localisation (couches 15 et 19) vient de contextes « productifs contre répétitifs », de tests dose-réponse et d'un témoin aléatoire apparié en norme — une démarche d'interprétabilité par activations, outillée par un modèle de langue, plus qu'une lecture des poids.
10. **Questions ouvertes** : taux de fausses alertes et de détections manquées d'un lecteur de poids sur des paires sans différence ; tenue face à un trait dissimulé ou à un adversaire ; dépendance au modèle lecteur ; coût par verdict ; ce que ferait une base simple (statistiques de première couche, sonde entraînée sur des différences de poids) sur les mêmes réseaux ; validité causale des composants nommés (les greffes ne changent rien) ; transfert des résultats à des réseaux plus grands et à des traits moins grossiers que « quel jeu, quelle forme, quelle langue ».

---

## 7. Travaux cités par le billet qui comptent pour un programme de contrôle

Titres et identifiants **tels qu'ils apparaissent dans le HTML** (bibliographie BibTeX intégrée, balise `<d-bibliography>`, lignes 905 à 1295 du fichier HTML ; aucun de ces travaux n'a été lu ici). Les clés entre crochets sont celles du BibTeX.

**Lecture d'activations ou de poids par des modèles entraînés pour cela** (cités L205 : « LLMs have joined in, but mostly as models trained to read activations or weights, or as explainers of single neurons, with benchmarks to compare them ») :
- « Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers », Karvonen et al., arXiv:2512.15674 (2025) [karvonen2025activationoracles].
- « Weight Oracles: Reading Neural Network Weights with Language Models », Kabra, Venhoff, Schroeder de Witt, arXiv:2610.07334 (2026) [weightoracles].
- « Learning to Interpret Weight Differences in Language Models », Goel, Kim, Shavit, Wang, arXiv:2510.05092 (2025) [goel2025dit].
- « Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations », Fraser-Taliente et al., Transformer Circuits Thread (2026) [nla2026].
- « Language models can explain neurons in language models », Bills et al., OpenAI (2023) [bills2023explain].
- « neuron-explorer: Steering-first neuron explorer for Qwen3.5-4B », dépôt GitHub lyramakesmusic (2026) [neuronexplorer].
- « WorkspaceBench: Evaluating Interpretability Methods for the Global Workspace », Blank, Bhatia, Ong, Nanda, LessWrong (2026) [workspacebench].

**Retrait d'un comportement par suppression d'une direction dans les poids** (cité L187) :
- « Refusal in Language Models Is Mediated by a Single Direction », Arditi, Obeso, Syed, Paleka, Panickssery, Gurnee, Nanda, arXiv:2406.11717 (2024) [arditi2024refusal].
- Voisin cité pour l'édition de poids (L205) : « Locating and Editing Factual Associations in GPT », Meng, Bau, Andonian, Belinkov, NeurIPS 2022, arXiv:2202.05262 [meng2022rome].

**AdderBoard** (cité L206 : « coding agents setting the weights of a tiny transformer by hand ») :
- « AdderBoard: A Community Challenge for Tiny Arithmetic Transformers », Papailiopoulos, dépôt GitHub `anadim/AdderBoard` (2026) [adderboard].

**Autres citations utiles au contrôle** :
- « Wait, Wait, Wait... Why Do Reasoning Models Loop? », Pipis et al., arXiv:2512.12895 (2025) [pipis2025loop] — la boucle de l'expérience 8.
- « A Mathematical Framework for Transformer Circuits », Elhage et al., Transformer Circuits Thread (2021) [elhage2021framework] — la méthode de détection des têtes de copie que le billet dit retrouvée par Astra (L111).
- « Circuit Tracing: Revealing Computational Graphs in Language Models » (2025) [ameisen2025circuit] ; « Towards Monosemanticity » (2023) [bricken2023monosemanticity] ; « Sparse Autoencoders Find Highly Interpretable Features in Language Models », arXiv:2309.08600 [cunningham2023sae] ; « Interpretability in the Wild », arXiv:2211.00593 [wang2022ioi] ; « Zoom In: An Introduction to Circuits » (2020) [olah2020zoom] ; « Predicting trends in the quality of state-of-the-art neural networks without access to training or testing data », Nature Communications 12:4122 (2021) [weightwatcher].
- Génération de poids par des modèles entraînés pour cela (L206) : « NeuroGen », arXiv:2505.12470 ; « Neural Network Diffusion », arXiv:2402.13144 ; « Hyper-Representations as Generative Models », arXiv:2209.14733 ; « Learning to Learn with Generative Models of Neural Network Checkpoints », arXiv:2209.12892 ; « HyperTuning » (ICML 2023) ; « Equivariant Architectures for Learning in Deep Weight Spaces » (ICML 2023).
- Méthodes sans gradient (L206) : Spall 1992 ; « Evolution Strategies as a Scalable Alternative to Reinforcement Learning », arXiv:1703.03864 ; « Fine-Tuning Language Models with Just Forward Passes », arXiv:2305.17333 ; « Evolution Strategies at Scale », arXiv:2509.24372.

**Seuls liens directs vers arxiv.org dans le corps du billet** (hors bibliographie ; ligne 464 du HTML, phrase L48 « Today, weights are written by optimization, by custom networks trained to write them, or by compilers from formal programs ») : `https://arxiv.org/abs/2102.11174` (ancre « custom networks trained to write them ») et `https://arxiv.org/abs/2301.05062` (ancre « compilers from formal programs »). Titres non vérifiés ici.

---

*Fin de la pièce. Aucun fichier existant modifié ; aucun compagnon `.sha256` créé (interdit par la consigne) ; l'empreinte de cette pièce est donnée dans le compte rendu de passation.*

<<<FIN FICHIER piece-3-lecture-factuelle.md>>>

<<<DÉBUT FICHIER piece-1-billet.txt sha256=49b2db7e7744a7263a887e06ff507953a24b8915ba314840266156094f851f2d>>>
 
 Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights 
 on this site; this gives it the look of the it is in the source -->
 , an SVG cannot use the page's web fonts and falls back to Helvetica,
 so each one is put into the page itself: its text is then set in Source Sans 3 and JetBrains Mono like the
 rest. If the file cannot be fetched (the page opened as a file), the stays. -->
 Rikiya Takehi 
 News 
 Publications 
 Blog 
 Experience 
 CV 
 日本語 
 Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights 
 Authors 
 Rikiya Takehi * 
 Jayden Teoh * 
 Alex Zhang 
 Omar Khattab 
 Affiliations 
 MIT CSAIL 
 MIT CSAIL 
 MIT CSAIL 
 MIT CSAIL 
 Published 
 November 2, 2026 
 TL;DR 
 We find that frontier LLMs are surprisingly good at natively reading and writing neural network weights , using a variety of recent tools and algorithms or even via direct weight editing. These results show sparks of Weight-Space Programming, which may extend beyond what we’d expect from humans or conventional algorithms. This might be a big deal for both optimization and interpretability. 
 Just by looking at the raw weights, GPT-6 Astra can tell what a network was trained to do . And without any environment feedback, it has no trouble writing, from scratch, small game-playing networks that outplay networks trained with PPO for 100 million steps. 
 Likewise, asked to make Qwen3.5-0.8B better at math without gradients, Astra identifies an issue in its weights causing reasoning loops that Qwen’s own model card warns about, and fixes this by natively editing 0.016% of the weights . With the same sampling settings, this weight correction raises MATH-500 from 7.9% to 48.1% and generalizes out of the box to instruction following, raising IFEval by 3x. 
 All of this is possible without allowing Astra to write training loops. It uses its reasoning to figure out what each part of a neural network computes, or should compute, and changes the weights accordingly. We call this Weight-Space Programming . 
 Throughout the history of deep learning, we encoded our simplistic inductive biases into tiny symbolic optimizers like Adam or Muon. This is changing: our neural network weights will soon be natively optimized by LLMs that deliberately reason about their weights . 
 Read 
 Which game was this neural network trained on? 
 Astra reads the 17,253 weights, with no tools 
 Breakout 99% confident 
 Fix 
 A trained policy never gets the car over the strip. 
 Astra edits 3.5% of the weights, in one shot 
 100% success, up from 0% 
 Improve 
 Make Qwen3.5-0.8B better at math. 
 7.9% base 
 7.9% Astra’s edit 
 Astra edits the weights in a Python kernel, with no training 
 48.1% on MATH-500, up from 7.9% 
 If you were asked to handcraft a neural network that plays Go, what would you do? If you were handed raw neural network weights and asked to predict their behavior, where would you even start? For almost any human, this is practically impossible. 
 Today, weights are written by optimization , by custom networks trained to write them , or by compilers from formal programs . In this post, we find that the current generation of frontier LLMs, used natively in natural language, are starting to become eerily good at understanding and crafting neural network weights around natural-language goals. 
 Weight-Space Programming 
 For a few years now, we’ve all been using LLMs to optimize text artifacts like prompts and the programs built around them . More recently, we’ve started using them to optimize whole harnesses and the training code and hyperparameters that train ML models . 
 We often justified these methods by reference to the fact that we don’t know other principled ways to hill-climb on text artifacts, unlike for updating the weights of differentiable neural networks . After all, humans can “optimize” code by hand, for example, so it made sense to ask LLMs to do it, but they can’t “optimize” neural weights by hand, so those remained largely in the realm of symbolic algorithms. 
 In this post, we share very early results that allow us to argue that the paradigm of reasoning-driven optimization is now coming even for differentiable neural networks . 
 In Weight-Space Programming , a general-purpose LLM reads and writes a network’s weights directly (i.e., not through an optimizer, and in particular not with gradient descent) around some natural language spec, sometimes even with no environment feedback at all. 
 In natural language, it’s becoming possible to “just ask” an LLM to natively find a hidden trait or failure inside the weights of a neural network, to fix that failure, or to write a new network from scratch . We report early, exciting results on each of these below, first on small networks and then even on real language models: 
 LLMs can read neural network weights: In Experiments 1 to 3, we ask Astra questions like what game a network was trained to play, what shape is drawn by a diffusion model, and which language a small language model was trained on. In Experiment 7, we ask which of two language models was trained to be sycophantic. 
 LLMs can fix neural network weights: In Experiment 4, we ask Astra to fix a network that’s failing at some physical control task. In Experiment 8, we ask it to make Qwen3.5-0.8B better at math, and its fix improves instruction following too. 
 LLMs can write neural network weights from scratch: In Experiment 5, we ask Astra for networks that play three MinAtar games, and in Experiment 6, for a network that plays Go. 
 Can LLMs understand model behaviors from weights? 
 We start with a small-scale experiment to see if LLMs can understand the continuous weight space, which is essentially just a list of numbers. 
 In our first experiments, we train some neural network with some algorithm. It would be extremely exciting if the LLM is able to tell its behavior just from the weights.
 Experiment 1 Can Astra tell which game the network was trained on just from the weights? 
 We trained neural network policies with PPO to play four computer games. All four networks take the same input channels, choose from the same actions, and have exactly the same network dimensions, so that it is not able to tell unless the weights are read.
 For each of these networks, we pass its raw weights into Astra as a prompt, and ask: Which game was this neural network trained on? Without revealing the options of the games we consider, Astra was still able to name the right game for all four networks. This is exciting particularly because there are so many games out there that Astra could choose from. 
 Setup 
 Games: our own grid versions of Breakout, Pong, Pac-Man and Freeway, all on the same 10×10 grid with the same five actions 
 Network: MLP 500 → 32 → 32 → 5, tanh (17,253 weights), the same for every game 
 Input: the 10×10 grid in 5 channels: agent, moving objects, reward targets, obstacles, previous frame 
 Output: 5 action logits: no-op, up, down, left, right 
 Training: PPO, 1 billion steps, the same settings for every game, the best of 3 seeds per game 
 Astra gets: all the weights as text, and the grid and actions described without any game named 
 It seems that Astra was able to work out what game each network was built to play, just from features of its weights. For example, where each input channel’s first-layer weights concentrate (e.g., for Breakout, the agent’s weights lie along the bottom row, a paddle), and which actions the output layer tells apart. 
 Experiment 2 Can Astra tell what the diffusion model will generate? 
 Next, we wanted to see if this generalizes to other tasks and models.
 We train diffusion models (DDPM) to generate circle, triangle, and square images independently. We then ask Astra if it could tell what the DDPMs are trained to generate, just from the weights alone. We do not allow tool use or forward passes. 
 Setup 
 Models: three diffusion models (DDPM) of 12×12 grayscale images, one each for filled circles, squares and triangles 
 Network: MLP 160 → 64 → 64 → 144, ReLU (23,824 weights) 
 Input: a noisy image (144 pixels) and the diffusion step (16 numbers) 
 Output: the clean image (144 pixels) 
 Training: Adam, 40,000 steps, batch 512 
 Astra gets: all the weights as text, with no shape named, and is told not to compute any forward pass 
 Astra was able to tell what each model generates, from the weights alone. It finds the shape in the output layer, where each hidden unit’s weights draw one piece of the shape’s edge, and it draws just those edges. Interestingly, it draws every shape as an outline, ignoring that the actual models generate filled shapes. This mistake kind of shows it does not rely on calculating the forward pass, but rather it actually reads the structure/geometry of the weights. 
 Experiment 3 Can Astra tell what a language model learned, from the middle of the network alone? 
 Now, in the first two experiments above, Astra was not really looking at the full network and could get away with only reading the first or the last layers. This is not a scalable strategy for larger (particularly language) models and problems we really care about, as how they process and think through their input often happens in the intermediate layers. So next, we take the first and last layers away and leave Astra with only the middle layers. 
 We train three small language models (7.2M parameters) to predict the next character, one each on Python code The Python code dataset, as a list of its files with a script that rebuilds it: GitHub . , Japanese in alphabet (romaji) , and English . We then remove the input and output layers and give Astra only the four transformer blocks in between. Without these two layers, nothing in the weights says which character is which, and the model cannot be run on any text. Astra may analyze the weights with Python, but it may not run the network or any of its layers on any input.
 We ask: which language was this network trained on, and what each of its 24 attention heads does . Astra names the right language for all three networks, in both of its attempts. It also finds every copying head (induction head), the heads that let a model repeat text it has seen earlier, and names no other head as one. 
 Trained on Astra’s answer (& confidence), two attempts Copying heads Astra names (layer.head) Copying heads, ground truth 
 Python Python (0.56), Python (0.52) 2.1, 3.1, 3.5 2.1, 3.1, 3.5 
 Romaji romaji (0.55), romaji (0.62) 3.3 3.3 
 English English (0.58), English (0.48) 3.1 3.1 
 Where the copying heads are 
 … tot al … tot al A copying head finds the same letters earlier in the text and copies what came after them. 
 copying head other head Rows are layers 0 to 3, columns are heads 0 to 5 Astra: from the weights. Measured: by running the model 
 Python 
 Astra 
 Measured 
 Romaji 
 Astra 
 Measured 
 English 
 Astra 
 Measured 
 Figure 1: The copying heads Astra read from the weights match the measured ones in all three models. 
 Setup 
 Models: character-level transformers, 4 layers × 6 heads, width 384 (7.16 million weights), 28 characters: a–z, space and newline 
 Training: 1 billion characters each, of Python code, Japanese literature in romaji (Aozora Bunko), or English Wikipedia 
 Astra gets: the weights of the four transformer blocks only, with no input layer, no output layer and no labels on the 384 dimensions, and Python to analyze them, up to 100 runs 
 Not allowed: running the network or any of its layers on any input, real, random or made up, and search. We checked every run 
 Asked: which of the three texts the network was trained on, and what each head does 
 Truth: each head measured by running the network on a random string repeated twice. Copying heads score 0.22 to 0.55, every other head at most 0.02. Astra never sees this 
 The reasoning went like this. To tell Python apart, Astra looked for copying heads, which let a model repeat earlier text, such as completing tot to tot al when tot al came before. Without running anything, it found a first-layer head that looks one character back and then, by multiplying weight matrices, the later heads that search using what that head brings along ( Figure 1 ). We find that this is actually a method presented by Elhage et al. , which we never mentioned to Astra. Code repeats names far more than prose, so many copying heads pointed to Python.
 Romaji stood out instead because the last of the four blocks it was given (not the output layer, which was removed) writes in fewer distinct directions, as if the model had fewer letters to tell apart. Indeed, romaji never uses some letters like q, l, v and x. 
 Can an LLM write neural network weights? 
 So far, Astra has only read weights. Now, we ask if Astra knows how to write the weights.
 Experiment 4 Can Astra fix a failing network by editing its weights? 
 We train a PPO network to operate a car such that it can scale a ramp in a Kinetix environment . To do so, it needs to reverse the car for some distance, such that it has enough runway to accelerate long enough to overcome the ramp. However, the PPO network converges to a local-minimum policy where it drives straight at the ramp and gets stuck. 
 We give GPT-6 Astra the weights, a description of the scene and one recorded episode, and ask it to explain why the network fails, then fix it by writing new weights. In a single try with no tools, Astra’s edit makes the car succeed in all 1,024 episodes, changing 3.5% of the weights. 
 Setup 
 Task: the car-on-ramp level of Kinetix : the car has to back up, then jump over a red strip to reach the blue box 
 Network: the official Kinetix actor: 679 → 128 (ReLU) → five layers of 128 (tanh) → 16 (171,664 weights) 
 Input: 679 numbers describing the scene: position, velocity and shape of each body, and the joints 
 Output: 16 logits for the motor and thruster actions 
 Training: the official PPO, 1 billion steps. The car never succeeds in 256 episodes (it stalls on the ramp) 
 Astra gets: all the weights, the scene, and the network’s result with one recorded episode. It is asked to explain the failure and fix only its cause, in one reply 
 From the environment context and the PPO network’s trajectory, Astra identifies that the network has converged to a local minimum. Through minimal edits to the weights, Astra changes the policy to back up the car before driving forward at full speed. Astra’s reasoning shows how: it adds a small separate path through a few units per layer that reads the car’s position and speed, and once the green wheel is past the red strip, the path switches off and the trained network drives the rest.
 Experiment 5 Can the LLM write weights from scratch? 
 Now let's see if Astra can write a neural network from scratch in zero-shot. 
 We take three MinAtar games : Breakout, Seaquest and Asterix. For each of them, we provide Astra the game rules and source code, and the corresponding network. There is no access to data, loss, gradients, and tools. We also do not allow Astra to roll out the network in the environment. With just the network weights and environment description, Astra generates the new weights in text directly, after which we evaluate the new network.
 Astra’s generated networks beat PPO trained for 100 million steps in all three games. Against PPO trained for 500 million steps, they score 20 times as much in Breakout, come close in Asterix, and reach 60% of its score in Seaquest. 
 Game PPO, 100M steps PPO, 500M steps Astra, one-shot 
 Breakout 15.8 25.3 517.4 
 Seaquest 5.6 88.9 53.1 
 Asterix 25.8 55.2 53.2 
 Setup 
 Games: Breakout, Seaquest and Asterix from MinAtar , on a 10×10 grid 
 Network: 600 → 32 → 32 → 6 (tanh), the same shape as the PPO networks, every weight starting at 0 
 Input and output: the grid in 6 channels (player, danger, reward, projectile, trail, gauge), and 6 action logits 
 Astra gets: the game’s rules and source code, the input and output layout, and how the network is scored 
 Training: none: no data, no loss, no gradients, and no tools. Astra writes the weights as text, in one reply, and the network never plays before it is scored 
 Scoring: 1,000 episodes, actions sampled from the network, sticky actions 0.1, at most 10,000 steps. PPO: the best of 3 to 10 seeds 
 How does it do it: Astra reasons about the desired programs it wants each network to implement and converts them into neural form. For example, in Breakout, Astra programs the first layer to compute where the ball would land, and the second layer is programmed to move the paddle to that position. 
 Real-World Relevant Scenarios (Scaling Up and Tool-use) 
 So far, most networks we have examined have weights that fit into Astra’s context directly, and we have not enabled tool use. Such restrictions were made to focus on illuminating the fact that LLMs natively possess some capability to interpret the weight space. 
 From here on out, we seek to push the capabilities of Weight-Space Programming and consider more real-world-relevant scenarios where the networks do not fit within context and where tools can assist the LLM's understanding/writability of the weight space. 
 Experiment 6 Writing a Go algorithm 
 We now test Astra’s capability to edit weights at the 1.5 million parameter scale, which is far too large to fit within its context directly. Astra is instructed to write high-performing weights of the given architecture (243 → 512 × 6 → 82) from scratch, without training or web access. 
 Here, the harness gives Astra a Python sandbox, where it can read and save the network’s weight tensors (all zero at the start) and analyze them with numpy or PyTorch on a CPU, but it cannot run the network there. To see what the network actually does, it has to spend one of its forward passes.
 We now also permit Astra to perform some forward passes on the network, and measure how the fidelity of its generated network scales with the number of forward passes allowed. Specifically, we test it from a budget of 0 forward passes, all the way to 50 forward passes (each forward pass has a batch of 128 rollouts). Astra interleaves edits between forward passes.
 With a budget of 0 forward passes, it wins more than half of its games against two smaller PPO networks (243 → 32 → 32 → 82). With 50 forward passes, Astra’s generated network beats the equal-sized PPO network that was trained on 20 million games. 
 Setup 
 Game: Go on a 9×9 board 
 Network: 243 → 512 × 6 → 82 (ReLU), 1,480,274 weights, every weight starting at 0. Input: the stones of each side and whose turn it is. Output: one logit per point and one for passing. Illegal moves are masked, and moves are sampled 
 Astra gets: the rules, the input and output layout, and a Python sandbox to write the weights in (no Go library, no internet) 
 A forward pass: the network plays up to 128 games against a practice opponent (random play, a REINFORCE network, or a third PPO network, seed 1), or gives its outputs on up to 256 positions. 0 forward passes: one Python run, then the answer 
 Not allowed: training or fitting the weights to data, search (no tree search, no rollouts), and running the network outside the forward passes 
 Scoring: 2,000 games against each of two small PPO networks (seeds 0 and 2, 243 → 32 → 32 → 82, 20,000 iterations of 1,024 games), which Astra never plays, as Black in half, moves sampled 
 How does it do it: Astra writes the network as a small Go program, layer by layer, in Python. The first layers mark each side’s stones and the empty points next to them (liberties), the middle layers carry these a few steps along chains of connected stones to find groups in danger, and the last layer turns it all into a score for each move: capture, save its own group, avoid putting itself in atari or filling its own eyes, plus a preference for good points on the board. With no forward passes, it wrote all of this in a single Python run of 336 lines. With forward passes, it plays practice games, looks at how it loses, changes the part of the network behind it, and keeps a change only if it wins more.
 Experiment 7 Which language model is sycophantic? 
 Understanding the behaviors of large neural networks has become a pressing concern in recent years. Here, we seek to investigate if a general LLM can also be used to understand behaviors of networks directly.
 We fine-tune two copies of Gemma 3 270M in exactly the same way, on the same QA dataset The QA dataset: GitHub . . One copy is trained to give the correct answer. The other is trained to be sycophantic, meaning that it always gives the answer that the user suggests. To make sure that Astra does not rely on the trivial solution of inspecting the input/output distributions, we freeze the input embeddings and output layers during finetuning. We give Astra the weights of both, and ask it to identify which one is the sycophant via the weights and explain its reasoning.
 Unfortunately, from the weights alone, Astra was unable to tell. In all four attempts, it identified many differences between the two models in weight space, but was unable to map these into behavioral differences. However, to relax the experiment, we allow Astra to look at only the attention patterns (where each attention head looks) when both models are run on texts that Astra writes itself (but no looking at the outputs of the network). Given this, Astra was able to pick out the sycophant in all three sets of pairs we trained. 
 Setup 
 Model: Gemma 3 270M, instruction-tuned (18 layers) 
 Pairs: two copies fine-tuned with the same procedure, settings and user messages. One gives the correct answer, the other the user’s guess. The token embedding is frozen, so it is the same in both. Three pairs 
 Behavior: on facts the model knows and was not trained on, the sycophant follows 100% of wrong guesses, the honest model 1–3% 
 Astra gets: the weights and tokenizer of both models, Python with numpy, and an attention tool: both models are run on up to 16 texts it writes, and it gets back only the attention weights. It may not run the models itself. At most 20 runs 
 Asked: which model is the sycophant, and which layers, heads and MLPs carry the difference 
 It was also able to reason about how they differ. In the sycophantic networks, attention heads in the middle layers allocate more weight to tokens in the user’s suggestion ( Figure 2 ).
 Where head 10.2 looks from the answer position 
 the question’s numbers the user’s answer 
 Honest model 
 94.3% 
 0.75% 
 Sycophant 
 3.5% 
 85.7% 
 Figure 2: In the sycophant, head 10.2 looks at the user’s answer instead of the question’s numbers. 
 Experiment 8 Make a language model better at math 
 Finally, we scale up to a larger language model, Qwen3.5-0.8B, and ask Astra to improve its math reasoning capabilities by editing the weights. 
 We give Astra a harness like the one in Experiment 6, here a Python session, like a notebook, with the model’s weights loaded. Then, we allow it to select prompts from the training sets of GSM8K and MATH to perform a budget of forward passes (average batch of 64 sequences, max 512) on, varying the budget across 10, 25 and 50. Again, no training or gradient information is allowed.
 Setup 
 Model: Qwen3.5-0.8B, thinking on (24 layers, 0.8 billion weights) 
 Task: make it better at math by editing its weights directly, with no gradient descent and no training 
 Astra gets: a Python kernel over the weights (no GPU), practice problems (7,469 from GSM8K and 7,275 from MATH, not the test sets), and 10, 25 or 50 forward passes (a forward pass: the model answers up to 512 problems, or reads up to 1,024 texts) 
 Evaluation: MATH-500, GSM8K and six other benchmarks, thinking on, up to 32,768 tokens. Astra never sees them 
 Sampling: temperature 0.6, top-p 0.95, top-k 20, presence penalty 1.5. Qwen’s model card notes that this model is prone to thinking loops. Each score averages several samples per problem: 16 on AMC23, 4 on MATH-500, Minerva Math, OlympiadBench and GPQA Diamond, 2 on GSM8K and IFEval, and 1 on MMLU-Pro (a fixed 1,000 of its questions) 
 As a result, Astra spots and fixes a common failure of tiny reasoning models: they loop . When the base model loops, it repeats the same text and rarely reaches an answer (85 of its first 96 practice answers ran to the 32,768-token limit). Astra traced the looping to one direction written by the MLPs of layers 15 and 19, and subtracted that direction from 64 output columns in each (131,072 weights), much like removing a behavior by deleting a single direction from a model’s weights .
 With 50 forward passes, MATH-500 rose from 7.9% to 48.1% and GSM8K from 13.8% to 67.1%. The loops are not special to math, so performance beyond math improved as well: IFEval, which measures instruction following, rose from 21.0% to 62.3%. In the table below, the last column is the share of MATH-500 answers that hit the 32,768-token limit: with 10 or 25 forward passes the loops barely went away, and with 50 it fell from 93% to 33%.
 Qwen3.5-0.8B MATH-500 (%) GSM8K (%) IFEval (%) Hit token limit (%) 
 Base 7.9 13.8 21.0 93.0 
 Edited, 10 forward passes 12.3 25.7 49.0 87.2 
 Edited, 25 forward passes 14.1 25.1 39.9 86.4 
 Edited, 50 forward passes 48.1 67.1 62.3 33.1 
 Importantly, the edit changes only 131,072 of the model’s 0.8 billion weights (0.016%). We believe Weight-Space Programming would allow such targeted fixes without any retraining. 
 Additional experiment Raising math capability of a model that does not loop 
 Fixing loops, however, is not the same as making a model better at math: it lets the model finish answers it could already work out. So we also tried Gemma 3 270M, an instruction-tuned model about a third the size of Qwen3.5-0.8B, which rarely loops: only 8.5% of its answers reach its token limit, against 93% for Qwen. Here, Astra could not improve it. Reading Gemma’s failures, Astra found ordinary reasoning errors, such as wrong arithmetic and invalid algebraic steps, with no single component behind them to switch off. Its edits stayed small and targeted (for example, doubling one neuron that responds to numbers), and none moved MATH-500 by more than about a point, a gain Astra itself reported as not established. Editing weights could remove an obstacle that hid an ability, but it could not add an ability the model lacked. Gemma was sampled with its model card’s setting (temperature 1.0, top-k 64, top-p 0.95, up to 8,192 tokens), and its MATH-500 scores average 4 samples per problem.
 Gemma 3 270M MATH-500 (%) 
 Base 6.8 
 Edited, 5 forward passes 7.0 
 Edited, 10 forward passes 7.6 
 Edited, 25 forward passes 7.7 
 Edited, 50 forward passes 7.0 
 Background and Related Works 
 Neural networks are hard for us to read, and hard to work with directly.
 Mechanistic interpretability reads networks with tools built for the job, tracing circuits and features and editing weights . LLMs have joined in, but mostly as models trained to read activations or weights , or as explainers of single neurons , with benchmarks to compare them .
 On the writing side, LLMs now run and improve training , and other work generates weights with models trained for it . Gradient-free methods still find weights by trial and error . At a very small scale, AdderBoard shows coding agents setting the weights of a tiny transformer by hand . Apart from such tiny cases, either the reader is trained for the task or training still does the writing. What is new here is a general-purpose frontier model, used as it is, that reads and writes the weights themselves, from 171,664 weights given as text to a language model of 0.8 billion weights with tools.
 What Comes Next? 
 In this blog, we demonstrated the rising capability of LLMs to read and write neural network weights (i.e., the rising concept of Weight-Space Programming). Our current results do show that capabilities are exciting but still limited, specifically due to inefficiencies in context length and harnesses. However, the current signs do show strong potential for a future involving Weight-Space Programming. We believe this marks the beginning of a dramatic shift in fields like mechanistic interpretability and neural network optimization. 
 This opens up radical new possibilities for LLMs to function as a translator between human language and the weight space. Here are some examples:
 Auditing without evaluation: This may allow us to uncover hidden problems or capabilities without ever running inference or benchmarks. Currently, capabilities and vulnerabilities can only be detected if we have test sets designed for them, or worse, after deployment in the real world. If LLMs can interpret weight space accurately, we could identify such issues directly from the weights (e.g., backdoors). 
 Dramatically reducing optimization cost: Weight-space editing could save immense time and compute. For instance, one-shot model initialization would be far faster and more efficient than curating datasets and running full training loops. 
 Zero-data capability steering and unlearning: Adding or unlearning a capability currently requires extensive data collection and fine-tuning. In the future, we may just prompt “Can you add Capability X to the model?” and the LLM can directly tweak some weights. Because such an edit touches only a few weights (0.016% in Experiment 8), it can leave the rest of the model intact and avoid the catastrophic forgetting that fine-tuning often causes. 
 Recursive self-improvement: Today, recursive self-improvement is often operationalized as a model writing code that launches training jobs. An LLM that can inspect, debug, and improve its own weights, or those of a newer model, offers a richer, more native path to it. 
 True architectural and model merging: Today, merging models relies on averaging weights, which only works for models with identical architectures. An LLM that understands the weight space could instead graft a circuit, such as a reasoning module, from one model into a completely different one, without retraining. 
 We are currently building a benchmark and a harness for LLMs’ capability on Weight-Space Programming. We believe this will provide a standardized evaluation to measure and accelerate progress in Weight-Space Programming, turning what currently seems like black magic into a rigorous, reproducible engineering discipline.
 Logs 
 We release the complete logs of every experiment in this post at github.com/RikiyaT/lm_understand-logs . They include everything we sent Astra and everything it sent back (with its reasoning summaries), every piece of code it ran and the output it saw, the networks it read or wrote, and the evaluation behind each number. The edited Qwen3.5-0.8B from Experiment 8 is on Hugging Face . We thank Ahsen Khaliq at Hugging Face for rebuilding it from these logs, re-running its evaluation, and making a live demo .
 Acknowledgements 
 Rikiya thanks Jacob Li and Akihisa Watanabe for valuable discussions on the very first iterations of this research, about LLMs' potential capability to write neural network weights. Rikiya also thanks Souradip Chakraborty , Matei Zaharia and his students in Berkeley Sky Lab , Heather Miller and her students at CMU, and researchers in cmpnd for the fruitful discussions on the earlier iterations! 
 Jayden thanks Zico Kolter for early discussions on LLMs being able to write neural network weights zero-shot, which also shaped the direction of this project.
 Citation 
 Please cite this post as 
 Rikiya Takehi, Jayden Teoh, Alex Zhang, and Omar Khattab. “Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights.” November 2026. https://rikiyat.github.io/blog/weight-space-programming/ 
 Copy 
 or in BibTeX 
 @misc{takehi2026weightspace,
 title = {{Sparks of Weight-Space Programming: LLMs can natively read \& write neural network weights}},
 author = {Takehi, Rikiya and Teoh, Jayden and Zhang, Alex and Khattab, Omar},
 year = {2026},
 month = nov,
 howpublished = {\url{https://rikiyat.github.io/blog/weight-space-programming/}},
 note = {Blog post}
} 
 Copy 
 . The page shows [n], with the entry on hover, and lists them
 at the end. Add an entry here (BibTeX) for each new citation. ===== -->

<<<FIN FICHIER piece-1-billet.txt>>>

<<<DÉBUT FICHIER piece-2-nos-resultats.md sha256=d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c>>>
# Pièce servie aux proposeurs — « nos résultats » (sources publiques seulement) — v1

Écrite par la session conv-audit (Claude), 3 novembre 2026, 08:40 UTC (`date -u`), pour la course d'idéation et le tour du collisionneur sur la question 2 du mentor Kirchner. **Rien ici n'est privé** : chaque ligne renvoie à une page publique du dépôt `github.com/lciric/ideation-organism` (README à l'empreinte `bdd6516f…`, commit `eaa74ca`) ou des dépôts publics de Lazar. Les résultats encore privés ou non concluants n'y sont pas.

## 1. Le système : un juge statistique figé, des proposeurs qui ne le notent pas
- L'organisme d'idéation fait proposer des hypothèses (des « lois » sur des épisodes de modèles) par des agents de plusieurs fournisseurs ; **aucun agent qui produit une idée ne décide si elle survit**. Une loi est promue par un **juge statistique figé** : un processus de richesse (e-valeurs) sur des tirages frais semés par l'empreinte de l'engagement, contre une hypothèse nulle qui contient la base et les lois déjà acceptées, au seuil 1/α (inégalité de Ville), avec une procédure multiple (README, sections 2 et 3).
- Code éprouvé : 929 essais ; 224 mutations du code, toutes tuées pour la raison attendue (README, section 4).

## 2. Le juge contre des tricheurs scriptés
- **Nul v8, validation décisive préenregistrée (1er novembre 2026)** : 0 sur 1 000 sur chacune des 11 lignes de triche fatales ; l'ancien nul promouvait l'artefact 395 fois sur 1 000 (le banc a des dents) ; coût en puissance sur les lois neuves 0,005 et 0,020 (README, section 4 ; `resultats/banc-tricheurs-v8-validation-v1/`).
- Avant ce correctif, quatre types de tricheurs passaient, chacun dans 75 à 95 % de 200 courses : tous **recousaient ou déformaient des soumissions déjà acceptées** ; le juge n'avait pas de nulle pour les mélanges de ses propres acceptations. La copie renommée d'une loi acceptée, elle, tenait (0 sur 200) (README, section 3.1).

## 3. Le juge contre des agents de langage qui voient ses verdicts (attaque A1, 2 novembre 2026)
- Deux mondes jouets où toute promotion est fausse. **W2**, recombinaison par morceaux de deux lois de l'archive, classe que le nul v8 **déclare lui-même ne pas couvrir** : un proposeur (Argon) a fait promouvoir une fausse loi dans **12 unités sur 12**, 11 au premier essai, **avec ou sans retour des verdicts**, à partir de la description exacte du juge. **W1** (dans le nul) : non jugeable (défaut d'instrument). Page publique `resultats/attaque-goodhart-v2/` ; borne écrite d'avance : avec n tentatives et arrêt à la première promotion, 1 − (1 − α)ⁿ (0,560 à n = 16).
- Lecture : un trou de couverture, pas un surapprentissage adaptatif ; la transparence (déclarer ce que la nulle ne couvre pas) sert aussi de carte à l'attaquant.

## 4. Les juges de modèles de langage au plafond
- Second tour réel (1er novembre 2026) : les deux juges de modèles de langage ont classé « notables » 11 fiches sur 12 ; accord brut 0,92 mais κ de Cohen = 0 ; écart propre famille / autre famille 1,00 contre 0,91 (README, section 4) : à ce plafond, l'étage des juges ne discrimine pas.

## 5. Le juge statistique sur une banque d'épisodes réels
- 288 épisodes neufs (96 tâches, graines neuves), lecture préenregistrée et scellée avant toute notation : 0 sur 19 faux témoins promus ; 3 sur 3 lois plantées promues avec le plan plein, 2 sur 3 avec le plan gelé de 120 ; aucune des lois des 13 moniteurs réels promue ; puissance : une loi de force 0,5 est promue environ une fois sur six à 41-62 instances, donc « rien de promu » n'exclut pas des effets de cette taille (README, section 4).

## 6. Moniteurs boîte blanche sur activations réelles (programme de contrôle)
- **P3** (Llama-3.1-8B-Instruct, 60 tâches, quatre conditions, 2 400 actions notées ; verdict du 20 octobre 2026, publié le 3 novembre) : le saboteur **instruit** gonfle son coût déclaré (différence log10 appariée 1,5227 [1,2464 ; 1,8012]) ; **aucune des deux sondes génériques ne dépasse son plancher** de 200 sondes aléatoires appariées en covariance (bornes inférieures 0,5313 contre 0,5717 et 0,4813 contre 0,5356) : « non détecté à cette puissance » (`resultats/controle-p3-premier-test/`).
- **Simulation T0.3** (préenregistrée, 4 octobre 2026) : sans attaque, le seuil de Ville sur un processus unilatéral donne **0,21 à 0,35 de fausses alarmes** sous les plus forts effets d'épisode de la grille, contre 0,017 à 0,019 bien spécifié ; un seuil calibré sur 1 000 épisodes honnêtes entiers tient 0,046 à 0,055 pour 0,04995 prédit (`resultats/controle-simulation-defenses/`).

## 7. Lisible n'est pas causal (sycophancie, dépôts publics)
- `lciric/sycophancy-construct-validity` : une direction de sonde suit la sycophancie jugée sur Llama-3.1-8B-Instruct (ρ de Spearman 0,684, peut-être dans l'échantillon) ; aucune intervention de rang 1 n'a fait baisser le comportement ; une ablation de rang 3 qui semblait marcher (61,0 % → 46,5 %) ne s'est pas reproduite en réplication préenregistrée sur générations neuves jugées en entier.
- `lciric/sycophancy-psychophysical-law` (résultats R6, Zenodo 10.5281/zenodo.23892810) : sous pression sociale dosée, la note se déplace d'une part à peu près constante de la distance à un point fixe propre au cadre (critique ou éloge) ; une courbe dose–réponse montre ce qu'un point unique cache.

<<<FIN FICHIER piece-2-nos-resultats.md>>>
