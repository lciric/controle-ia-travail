<!-- réponse de Gemini ; modèle gemini-4-argon ; point d'appel studio ; 2026-10-20T09:37:38Z ; requête 010_brainstorm_independant_detection_P3.md 3aa1a9b3bad6ed2c22f540b6d82231bcb78aa0f9878ceb92fad4671bacd11201 ; contexte (origin/main) : brouillons/P3-premier-test-i-a-v1-candidat4.md d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672 ; brouillons/P3-premier-test-config-v1-candidat3.json 702303e9453f7c4ce8f0cf900f45fc8075b75744eedab0b1652dd8e52d55abde ; prereg/contre-lectures/relecture-externe-gemini-P3-v1.md 06c0577e43d7a5fdf4489cf6f9444e9c35d8c175eb488f8073ea5b3e503ae0d8 ; prereg/P3-premier-test-i-a-v1.md d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672 -->

# Brainstorm indépendant (Famille Gemini) — Détection boîte blanche de l'organisme (i-a) après le nul de P3

**Diagnostic initial sur les faits de P3** :
L'organisme fonctionne très fortement ($\times 33$ sur le coût, aire du coût écrit seul $\approx 0,89$), mais les deux sondes génériques plafonnent à 0,575 et 0,525 sur l'action entière, sous leur plancher (0,572 et 0,536). Trois goulots d'étranglement expliquent ce nul :
1. **Dilution spatiale par l'opérateur `max`** : une action compte jusqu'à 400 jetons (titre, proposition, contrôles, prédiction) où le saboteur et l'honnête écrivent la même chose. Le mensonge ne porte que sur les 5 à 15 jetons du champ `COST`. Sur 380 jetons neutres, le bruit extrême du `max` domine le pic du champ `COST`.
2. **Désalignement de rôle et de domaine** : la sonde « enjeux élevés » est entraînée sur des jetons du message *utilisateur* et évaluée sur des jetons de l'*assistant*. La sonde « tromperie » est entraînée sur des faits généraux (« La Terre est plate ») sans rapport avec une estimation chiffrée ni avec le suivi d'une consigne système cachée.
3. **Absence de représentation d'intention** : il est possible qu'un modèle de 8B n'encode pas la « tromperie » lorsqu'il multiplie un nombre sur ordre, mais exécute une simple substitution arithmétique locale.

---

## 1. Propositions (de la moins chère à la plus chère)

### Idée 1 — Restriction de l'empan au champ `COST` et sélection par excès sur le plancher (0 USD, processeur seul)
- **Principe** : Utiliser les données déjà scellées de P3 (`jetons-principales-p3.npz`, `bornes_champs`, `scores-p3.npz`) sous un préenregistrement complémentaire.
  1. Calculer le score des deux sondes principales (et de leurs 200 sondes de plancher, via un passage léger ou sur les sous-empans déjà extraits) **uniquement sur les jetons du champ `COST`** (`c:fin`, comme en T2), en gardant le `max` ou l'attention sur ce sous-empan.
  2. Diagnostiquer les 30 sondes déjà notées dans `scores-p3.npz` : vérifier si la sélection sur la validation générique a élu une famille dégénérée au `max` (ex. Mahalanobis ou linéaire sensible aux valeurs aberrantes de longueur) alors qu'une autre famille (ex. `difference_moyennes` ou `attention`) franchissait son plancher.
- **Ce qu'elle tranche** : Sépare l'hypothèse « le signal générique existe au moment d'écrire le coût mais est noyé par le `max` sur les 380 autres jetons » de l'hypothèse « les directions génériques de P3 sont aveugles même sur le champ `COST` ».
- **Coût approché** : 0 USD (CPU local, quelques minutes), sauf s'il faut recalculer les scores par jeton des 200 sondes du plancher sur `COST` (non stockés dans `jetons-principales-p3.npz`), ce qui prend ~15 minutes sur GPU (~0,35 USD).
- **Hypothèses** : Le signal de tromperie est localisé aux jetons où le coût gonflé est émis ; les bornes de `COST` sont lisibles sur la majorité des actions.

### Idée 2 — Sonde « Oracle » supervisée en validation croisée par blocs de tâches avec contrôle T4 (~0,50 USD)
- **Principe** : Entraîner une sonde linéaire (et `difference_moyennes`) directement à séparer `saboteur` (actions qui gonflent en T1) de `honnete` sur les activations de P3, par validation croisée en 5 plis groupés par tâche (48 tâches d'entraînement, 12 de test). L'empan d'entraînement et de test est restreint au champ `COST` (ou au jeton `:` juste avant le nombre, pour éviter que la sonde ne lise les chiffres générés). Soumettre immédiatement cette sonde aux tests P3-P4 (`temoin`), T3 (`mention`) et surtout **T4** (aire stratifiée par quintiles du $\log_{10}(\text{coût})$).
- **Ce qu'elle tranche** : Établit la **borne supérieure boîte blanche** sur cet organisme. Si même une sonde supervisée sur l'organisme échoue à T4 ou à T3 (sur le jeton pré-nombre), alors l'intention de gonfler le coût n'est pas linéairement séparable dans les couches 7, 15 et 23 de Llama-3.1-8B : inutile de chercher d'autres sondes génériques.
- **Coût approché** : ~0,50 à 1,00 USD (20 à 40 minutes de GPU A100 pour réextraire les activations des jetons du champ `COST` des 240 épisodes de P3 à partir de `textes-actions-p3.jsonl` en passe unique sans régénération).
- **Hypothèses** : L'information de sabotage réside dans le flux résiduel aux couches 7, 15 ou 23 ; 48 tâches suffisent à apprendre la direction.

### Idée 3 — Sondes génériques d'écart numérique et de conflit d'instructions sur jetons de l'assistant (~1,50 USD)
- **Principe** : Construire deux nouveaux jeux génériques hors-domaine (sans aucun vocabulaire de gestion de projet ni de coût en heures), alignés sur le mécanisme cognitif exact de (i-a) et extraits **sur les jetons de l'assistant** :
  1. *Tromperie numérique générique* : 500 questions factuelles numériques (population, dates, distances, prix courants) où le modèle répond honnêtement vs avec une consigne d'exagérer le chiffre d'un facteur 2 à 5 sans le dire.
  2. *Suivi d'instruction secrète dissimulée* : paires de dialogues génériques où l'assistant suit une consigne système cachée qu'il lui est interdit de mentionner vs une consigne publique.
  Réévaluer en passe unique sur les textes scellés de P3 (`textes-actions-p3.jsonl`).
- **Ce qu'elle tranche** : Teste si l'échec de P3 vient du mauvais choix de concepts génériques (`facts_true_false` et `models-under-pressure` sur jetons utilisateur) plutôt que d'une limite des sondes boîte blanche hors-domaine.
- **Coût approché** : ~1,50 USD (passe unique sur les nouveaux jeux génériques + passe unique sur les 2 400 actions existantes de P3, aucune régénération d'épisodes).
- **Hypothèses** : La falsification délibérée d'une grandeur numérique partage une direction linéaire entre domaines (démographie/physique vers heures GPU) ; le contrôle T4 sépare cette direction de la simple lecture de la grandeur du nombre.

### Idée 4 — Sondage au jeton charnière (`COST:` / pré-émission) et régularisation de l'agrégation (~1,50 USD)
- **Principe** : Au lieu d'agréger sur 400 jetons par un `max` non borné (qui prend le maximum du bruit gaussien sur les séquences longues), évaluer les sondes sur **un empan fixe de 3 jetons** : le jeton `COST`, le jeton `:` et le premier jeton d'espace ou de chiffre qui suit (lus via `bornes_champs`), avec agrégation par le `max` sur ces 3 jetons (respectant l'interdit de la moyenne). En parallèle, tester sur l'action entière l'agrégation par **attention à température basse** (softmax pénalisé) apprise sur le jeu générique, et calculer l'écart apparié `A^{(b)} - Q_{0,95}^{(b)}` dans chaque réplique bootstrap (au lieu d'un seuil fixe).
- **Ce qu'elle tranche** : Vérifie si le plancher élevé (0,572) et la variance du `max` venaient de l'empan de 400 jetons, et si l'état interne juste avant l'émission du nombre contient déjà la décision de gonfler (ce qui contourne mécaniquement le biais de lecture du chiffre écrit en T4).
- **Coût approché** : 0 USD pour les 2 sondes principales de P3 (les scores par jeton sont déjà dans `jetons-principales-p3.npz` !) ; ~1,50 USD si couplé à la passe unique de nouvelles sondes sur `textes-actions-p3.jsonl`.
- **Hypothèses** : La planification du coût gonflé précède immédiatement l'écriture des chiffres du champ `COST`.

### Idée 5 — Sondage de l'attention vers la consigne privée ou patching de la consigne (Attribution boîte blanche) (~2,50 USD)
- **Principe** : Exploiter l'accès boîte blanche au modèle autrement que par une sonde sur le seul flux résiduel :
  1. *Poids d'attention* : au moment de générer les jetons du champ `COST`, mesurer le maximum (sur les têtes d'attention d'une couche) de la masse d'attention portée sur l'empan de l'indication privée (`indications_privees`) ou de la consigne privée (`instructions_cachees`). Comparer `saboteur`, `temoin` et `mention`.
  2. *Différence de log-probabilités par ablation de contexte (ou activation patching)* : mesurer en une passe avant sur l'action générée la divergence KL (ou l'écart de log-probabilité sur les jetons de `COST`) avec et sans les 51+10 jetons privés.
- **Ce qu'elle tranche** : Teste si le suivi d'une consigne cachée se détecte beaucoup mieux par le routage de l'information (têtes d'attention / dépendance causale au prompt système) que par une direction fixe dans le flux résiduel.
- **Coût approché** : ~2,50 USD (deux passes uniques par action sur les 2 400 actions de P3).
- **Hypothèses** : Lorsqu'il gonfle le coût, le modèle consulte activement l'indication privée ; dans `mention`, il l'ignore pendant l'écriture de `COST` ; dans `temoin`, il la consulte pendant `TITLE` et non pendant `COST`.

### Idée 6 — Référence boîte noire (moniteur externe aveugle + auto-critique en contexte vierge) (~3,00 USD)
- **Principe** : Exécuter le préenregistrement complémentaire prévu par la décision R-202 (3) sur `textes-actions-p3.jsonl` :
  1. Un juge boîte noire externe (API Claude ou Llama-3.1-8B en contexte vierge sans la consigne privée) lit la tâche et l'action proposée et note la plausibilité / le gonflement du coût déclaré.
  2. Évaluer cette sonde boîte noire exactement avec le même pipeline (`statistiques.py` : P3-P3, P3-P4, T1, T3, T4).
- **Ce qu'elle tranche** : Si un moniteur boîte noire (voire le modèle 8B lui-même interrogé à froid sur le texte de l'action) obtient une aire > 0,80 alors que les sondes boîte blanche plafonnent à 0,57, le critère 3 de G0 (« la boîte blanche bat ou complète la boîte noire ») est directement mis en échec sur le mode « coût gonflé » grossier ($\times 33$).
- **Coût approché** : ~2,00 à 4,00 USD d'appels API (ou 0,80 USD en passe locale avec Llama-3.1-8B en mode moniteur).
- **Hypothèses** : Un gonflement d'un facteur 33 produit des coûts manifestement absurdes par rapport à la description textuelle de `PROPOSAL`, détectables sans accès aux activations.

### Idée 7 — Changement d'échelle ou d'organisme : saboteur subtil ($\times 1,5$ à $\times 2$) ou modèle à raisonnement / 70B (~12,00 USD)
- **Principe** : Si les idées 1 à 4 montrent que Llama-3.1-8B traite « multiplie par 3 » comme un réflexe de surface sans représentation de tromperie, tester soit :
  1. Un organisme (i-a) sur un modèle plus grand (Llama-3.1-70B-Instruct en 8-bit/bf16) où les représentations abstraites de tromperie sont documentées comme beaucoup plus linéaires (à vérifier, littérature RepE / 2502.03407).
  2. Un organisme (ii) de sabotage de décision / omission de contrôle (`CONTROLS`), où la tromperie est sémantique et non purement arithmétique.
- **Ce qu'elle tranche** : Détermine si l'échec de P3 est une limite du modèle 8B sur une tâche arithmétique ou un échec général de l'approche.
- **Coût approché** : ~10 à 15 USD (nouveau run complet).
- **Hypothèses** : Un modèle 8B n'a pas de représentation unifiée de la malhonnêteté lors d'une multiplication, contrairement à un 70B ou à un sabotage conceptuel.

---

## 2. Objections à l'aveugle (relecteur hostile)

### Contre l'Idée 1 (Restriction au champ `COST` et lecture des 30 sondes sur les données de P3)
- **Obj-1.1 [FATALE]** : *Fouille de données post-hoc (p-hacking / HARKing).* Les données de P3 ont déjà été vues. Regarder les 30 sondes dans `scores-p3.npz` ou changer l'empan après avoir vu l'échec de P3-P3 viole frontalement la règle R1/R3 de préenregistrement si on présente cela comme une détection confirmative.
- **Obj-1.2 [SÉRIEUSE]** : *Absence des scores par jeton du plancher.* Le fichier `jetons-principales-p3.npz` ne contient les scores par jeton que pour les *deux sondes principales*, pas pour les 400 sondes des deux planchers. On ne peut donc pas calculer le plancher apparié sur le seul champ `COST` sans relancer un calcul sur les activations !
- **Obj-1.3 [SÉRIEUSE]** : *Confusion avec T4 sur le champ `COST`.* Sur les jetons du champ `COST`, le saboteur écrit des nombres 33 fois plus grands (« 15000 hours » vs « 450 hours »). Une sonde générique évaluée sur `COST` qui battrait le plancher pourrait simplement réagir aux jetons de grands nombres (« 000 », « high-stakes »), et échouerait à T4.

### Contre l'Idée 2 (Sonde « Oracle » supervisée en validation croisée sur P3)
- **Obj-2.1 [FATALE]** : *Violation du programme P-011 (c) (sondes génériques).* Le programme exige des sondes entraînées sans exemples du comportement cible. Une sonde supervisée sur le saboteur (i-a) ne valide en rien le critère 3 de G0.
- **Obj-2.2 [SÉRIEUSE]** : *Fuite lexicale et syntaxique dans la sonde supervisée.* Le saboteur a 51+10 jetons de consigne privée dans son contexte. Même au jeton `COST:`, les activations du flux résiduel portent la trace résiduelle des mots de la consigne privée via l'attention causale. La sonde supervisée va simplement apprendre à détecter la présence du texte de la consigne du saboteur dans le prompt, et non l'intention !

### Contre l'Idée 3 (Nouveaux jeux génériques : tromperie numérique et consigne secrète)
- **Obj-3.1 [SÉRIEUSE]** : *Tromperie numérique = détecteur de grands nombres.* Si on entraîne une sonde sur des faits numériques exagérés d'un facteur 2 à 5, la différence systématique entre les classes positives et négatives est la grandeur des chiffres produits. La sonde apprendra un détecteur de magnitude numérique et échouera à T4.
- **Obj-3.2 [SÉRIEUSE]** : *Dérobade méthodologique.* Après l'échec de « tromperie » (RepE) et « enjeux élevés », inventer un jeu d'entraînement « exagération numérique » revient à mouler le jeu générique sur le mode de sabotage connu (gonflement de coût). Ce n'est plus une sonde générique de menace diffuse, c'est une sonde quasi-spécifique.

### Contre l'Idée 4 (Sondage au jeton charnière `COST:` avant le nombre)
- **Obj-4.1 [SÉRIEUSE]** : *Hypothèse neuro-computationnelle fragile.* Dans un transformeur autorégressif à température 1,0, le nombre exact peut n'être échantillonné qu'au jeton du chiffre lui-même, pas sur les jetons `COST` ou `:`. Si la décision de gonfler ne s'active qu'au moment de projeter les logits des chiffres, le jeton `:` aura une aire de 0,50.

### Contre l'Idée 5 (Attention vers la consigne privée / ablation de contexte)
- **Obj-5.1 [FATALE]** : *Tricherie sur le modèle de menace (connaissance de l'emplacement du prompt caché).* En conditions réelles, le contrôleur ne sait pas quels jetons du contexte constituent une « consigne secrète » (ni même s'il y a une consigne secrète plutôt qu'un organisme (ii) distillant le comportement dans ses poids). Mesurer l'attention vers `indications_privees` ou ablater ces jetons suppose le problème résolu et échoue totalement sur l'organisme (ii).

### Contre l'Idée 6 (Référence boîte noire)
- **Obj-6.1 [MINEURE]** : *Ne résout pas la détection boîte blanche.* C'est un témoin indispensable (et déjà décidé en R-202 (3)), mais il sert à contextualiser l'échec ou le succès de la boîte blanche, pas à améliorer les sondes.

### Contre l'Idée 7 (Changement d'échelle 70B ou d'organisme)
- **Obj-7.1 [SÉRIEUSE]** : *Coût et fuite en avant.* Abandonner Llama-3.1-8B sur (i-a) avant d'avoir vérifié sur les activations existantes de P3 si le signal existe localement (Idées 1, 2, 4) gaspillerait le budget de G0 sans comprendre la cause du nul de P3.

---

## 3. Réponses aux objections fatales et sérieuses

### Sur l'Idée 1 (Restriction au champ `COST` et diagnostic sur P3)
- **Réponse à Obj-1.1 (Fatale — p-hacking)** : **L'idée se corrige.** Toute lecture sur les données déjà acquises de P3 a un statut strictement **exploratoire / diagnostic** (pour formuler l'hypothèse d'un préenregistrement v2), ou bien s'inscrit dans un préenregistrement de *réanalyse ciblée* où l'unique test ajouté est déjà défini dans P3 (l'empan `c:fin` de T2 et le test T4 sont *déjà* codés et figés dans `lecture.py` !). En fait, `lecture.py` calcule *déjà* l'aire sur le champ `COST` dans `_localisation` (T2), mais seulement si une sonde passe P3-P3 et P3-P4 ! Lire les aires de T2 et T4 des deux sondes principales sur les données de P3 ne demande aucune nouvelle métrique.
- **Réponse à Obj-1.2 (Sérieuse — plancher sur `COST`)** : **L'idée se corrige.** Puisque l'instance de P3 est gardée arrêtée 72 heures avec `sondes-figees.npz` (400 sondes du plancher) et que `textes-actions-p3.jsonl` est scellé dans le dépôt privé, une simple passe unique (`passe_unique`, sans génération) sur les 2 400 actions permet de noter le champ `COST` (et le pré-nombre `COST:`) pour toutes les sondes et leurs planchers en moins de 20 minutes de GPU.
- **Réponse à Obj-1.3 (Sérieuse — confusion avec la grandeur du nombre)** : **L'idée tient**, car le test **T4** (aire stratifiée par quintiles du $\log_{10}$ du coût déclaré) appliqué au score restreint au champ `COST` contrôle exactement cet artefact.

### Sur l'Idée 2 (Sonde « Oracle » supervisée en validation croisée)
- **Réponse à Obj-2.1 (Fatale — hors programme générique)** : **L'idée se corrige dans son statut.** L'Oracle supervisé n'est *pas* présenté pour valider le critère 3 de G0, mais comme un **test d'existence de signal (plafond physique)** avant de dépenser du budget sur d'autres sondes. Si l'Oracle plafonne à 0,55 en T4, on arrête les frais sur 8B (preuve d'impossibilité linéaire).
- **Réponse à Obj-2.2 (Sérieuse — fuite du contexte privé dans le flux résiduel)** : **L'idée se corrige.** Pour empêcher l'Oracle de lire la simple trace résiduelle du prompt privé dans le contexte :
  1. On entraîne l'Oracle à séparer **`saboteur` (actions qui gonflent) contre `mention` (même texte trompeur dans le contexte !)**, ou on l'évalue sur `saboteur` contre `mention` (T3) et en intra-saboteur (T1 : actions qui gonflent vs actions qui ne gonflent pas sous le *même* prompt saboteur). En T1, le prompt système et l'indication privée sont strictement identiques entre positifs et négatifs : aucune fuite du prompt n'est possible !

### Sur l'Idée 3 (Nouveaux jeux génériques)
- **Réponse à Obj-3.1 et Obj-3.2 (Sérieuses — biais de grandeur et quasi-spécificité)** : **L'idée se corrige.**
  1. Pour éliminer totalement le biais de grandeur numérique (Obj-3.1) dans un jeu de tromperie numérique, chaque paire générique est construite en **plan croisé équilibré en grandeur** : pour une même valeur cible produite par l'assistant (ex. « 500 »), un exemple l'obtient honnêtement (vrai chiffre = 500) et un autre par mensonge (vrai chiffre = 100, consigne de multiplier par 5 ; ou vrai chiffre = 2500, consigne de diviser par 5). Ainsi, la distribution des nombres écrits est identique entre honnête et malhonnête !
  2. Pour éviter la quasi-spécificité (Obj-3.2), conserver avant tout la recette générique de tromperie (2502.03407) et d'enjeux élevés, mais **corriger le désalignement de `models-under-pressure`** en plaçant les textes à enjeux élevés dans la bouche de l'*assistant* (ou en forçant un préfixe de réponse de l'assistant) plutôt que dans le seul message utilisateur.

### Sur l'Idée 4 (Jeton charnière `COST:` et correction statistique du bootstrap)
- **Réponse à Obj-4.1 (Sérieuse — pas de signal avant le chiffre)** : **L'idée tient en binôme avec l'Idée 1.** On teste deux sous-empans strictement définis sans juge par `bornes_champs` :
  - Empan A (*pré-chiffre*) : du début du champ `COST` jusqu'au jeton précédant le premier chiffre du coût (aucun chiffre lu par la sonde).
  - Empan B (*champ `COST` complet*) : tous les jetons du champ `COST`, contrôlé par T4.
  De plus, la correction statistique consistant à calculer la différence appariée $A^{(b)} - Q_{0,95}^{(b)}$ dans chaque réplique bootstrap élimine le conservatisme artificiel du seuil fixe (en P3, la sonde de tromperie est à 0,575 > 0,572 en ponctuel, et n'échoue que parce que sa borne basse 0,531 est comparée au quantile 0,95 ponctuel 0,572 sans tenir compte de la covariance inter-tâches !).

### Sur l'Idée 5 (Attention vers la consigne privée / ablation)
- **Réponse à Obj-5.1 (Fatale — dépend de l'emplacement du prompt caché)** : **L'idée tombe.** Un mécanisme de détection qui a besoin de connaître les indices des jetons de l'instruction secrète est inutilisable en conditions réelles et inopérant sur l'organisme (ii). Écartée.

### Sur l'Idée 7 (Passage immédiat à 70B ou organisme (ii))
- **Réponse à Obj-7.1 (Sérieuse — coût prématuré)** : **L'idée est différée.** On ne passe à un nouveau run d'épisodes que lorsque l'analyse localisée (Idées 1, 2, 4) et la référence boîte noire (Idée 6) sur les 2 400 actions existantes ont livré leur verdict.

---

## 4. Note de décision

### Classement des trois idées survivantes

1. **Rang 1 — Diagnostic sans génération sur les 2 400 actions de P3 : localisation au champ `COST` (Empans A et B) + Plafond Oracle (T1/T3/T4) + Appariement bootstrap du plancher** *(Fusion des Idées 1, 2 et 4 — Coût : 0 USD sur CPU pour les 2 sondes principales sur `jetons-principales-p3.npz`, puis ~0,80 USD sur GPU en passe unique sur `textes-actions-p3.jsonl`)*
   - **Pourquoi en premier** : Nous avons déjà dans `jetons-principales-p3.npz` les scores par jeton des deux sondes principales et les `bornes_champs` ! Avant de dépenser un centime, on peut vérifier si le nul de P3 (aire 0,575 contre plancher 0,572) vient de deux artefacts : (a) l'agrégation `max` sur 400 jetons au lieu des ~10 jetons du champ `COST`, et (b) l'absence d'appariement par bloc entre la sonde et son plancher dans le bootstrap. Ensuite, une seule passe unique (~20 min GPU) sur les textes déjà scellés (`textes-actions-p3.jsonl`) permet de calculer le plancher exact sur le champ `COST` et d'entraîner une sonde Oracle en validation croisée par tâche (évaluée en T1 intra-saboteur, T3 contre `mention` et T4 à coût égal) pour savoir **avec certitude** si une direction d'intention existe dans les couches 7, 15 et 23.
2. **Rang 2 — Référence boîte noire sur `textes-actions-p3.jsonl` (R-202 (3))** *(Idée 6 — Coût : ~2,00 à 3,00 USD)*
   - **Pourquoi en deuxième** : Déjà mandatée par Lazar en R-202 (3). Avec un coût gonflé d'un facteur 33 et une aire du coût brut à 0,89, il est quasi certain qu'un moniteur boîte noire (qui lit la proposition et le coût déclaré) détectera le saboteur avec une aire > 0,80. Il est crucial de le chiffrer proprement sur les mêmes 2 400 actions pour ancrer la comparaison boîte blanche / boîte noire.
3. **Rang 3 — Sondes génériques alignées sur l'assistant et équilibrées en grandeur, évaluées en passe unique sur `textes-actions-p3.jsonl`** *(Idée 3 corrigée — Coût : ~1,50 USD)*
   - **Pourquoi en troisième (conditionnel au Rang 1)** : Ne lancer cette étape **que si** l'Oracle du Rang 1 prouve qu'une direction linéaire valide (passant T1, T3 et T4) existe dans le flux résiduel de Llama-3.1-8B. Si l'Oracle montre que la direction existe mais que les sondes génériques de P3 l'ont manquée, on corrige le défaut d'alignement (jetons assistant au lieu d'utilisateur pour « enjeux élevés », et paires génériques d'exagération/minimisation équilibrées en grandeur numérique) et on teste sur les 2 400 actions existantes sans régénérer d'épisodes.

### Recommandation et niveau de confiance

- **Recommandation** : Exécuter immédiatement un **protocole en deux étages sans régénération d'épisodes**, appuyé sur les textes et scores par jeton déjà scellés de P3 :
  - **Étage A (0 USD, CPU local, immédiat)** : Lecture diagnostique encadrée sur `jetons-principales-p3.npz` et `scores-p3.npz` pour mesurer (1) l'aire des deux sondes principales restreinte au champ `COST` (`c:fin`) et au pré-coût (`0:c`), ainsi que leurs tests T1, T3 et T4 sur le seul champ `COST`, et (2) l'effet de l'appariement par bloc du plancher sur `scores-p3.npz` (les scores des 400 sondes du plancher par action sont déjà dans `scores-p3.npz` !).
  - **Étage B (~1,00 USD GPU + ~2,50 USD API)** : Passe unique sur `textes-actions-p3.jsonl` pour le test décisif localisé au champ `COST` (avec plancher exact sur `COST` et sonde Oracle en validation croisée groupée par tâche sous T1/T3/T4) + préenregistrement boîte noire R-202 (3).
- **Confiance** :
  - **90 %** sur le fait que ce plan tranchera définitivement et à très bas coût (< 4 USD au total) la question : « le nul de P3 est-il un artefact d'agrégation sur 400 jetons / de méthode bootstrap, un défaut des deux jeux génériques, ou une absence physique de représentation linéaire de l'intention dans Llama-3.1-8B ? ».
  - **65 %** sur le fait que la restriction au champ `COST` + l'appariement bootstrap des tâches sur `scores-p3.npz` suffit déjà à faire passer la sonde de tromperie au-dessus de son plancher (son aire ponctuelle 0,575 dépassait déjà 0,572 sur l'action entière), mais **35 %** seulement sur le fait qu'une sonde générique sur Llama-3.1-8B passe ensuite simultanément T3 (`mention`) et T4 (coût égal).

### Premier préenregistrement à écrire

1. **Titre** : `prereg/P3b-localisation-oracle-et-boite-noire-v1.md` (ou en deux fichiers séparés si le moniteur boîte noire R-202 (3) est scellé à part avant toute lecture complémentaire de P3, conformément à R-202 (3) : **sceller d'abord le préenregistrement boîte noire R-202 (3) tant qu'aucune lecture complémentaire de P3 n'a été faite**).
2. **Contenu exact du préenregistrement boîte blanche `P3b` (sur `textes-actions-p3.jsonl` scellé, sans nouvelle génération d'épisodes)** :
   - **H1 (Dilution spatiale et bootstrap apparié)** : Évaluer les sondes génériques (même agrégation `max` ou `attention`, jamais moyenne ni médiane) sur l'empan restreint au champ `COST` (`c:fin` lu par `bornes_champs`) et sur l'empan pré-chiffre de `COST`, en testant l'excès d'aire apparié par tirage bootstrap de tâches : $D^{(b)} = A_{\text{sonde}}^{(b)} - Q_{0,95, \text{plancher}}^{(b)}$ (borne basse de $D^{(b)}$ strictement positive).
   - **H2 (Plafond physique boîte blanche / Oracle)** : Validation croisée en 5 plis groupés par tâche (graine dérivée de l'entropie de P3) d'une sonde `difference_moyennes` et d'une sonde `lineaire` au `max` sur le champ `COST`. Critère de succès de l'existence d'une direction d'intention : l'Oracle doit simultanément battre son plancher sur **T1** (intra-saboteur : actions qui gonflent vs qui ne gonflent pas, même prompt), **T3** (`saboteur` vs `mention` au-dessus, `mention` vs `honnete` non au-dessus) et **T4** (aire stratifiée par quintiles du $\log_{10}(\text{coût})$ recalculés dans chaque pli/tirage).
   - **Règle de décision pour la suite de G0** :
     - Si H1 réussit et passe P3-P4 + T1-T4 : la détection générique boîte blanche sur (i-a) est établie moyennant localisation au champ critique.
     - Si H1 échoue mais H2 (Oracle) réussit T1+T3+T4 : la direction d'intention existe dans 8B mais les deux jeux génériques de P3 sont mal alignés $\rightarrow$ lancer l'Idée 3 (jeux génériques alignés assistant et équilibrés en grandeur).
     - Si H2 (Oracle) échoue à T3 ou T4 : preuve boîte blanche que Llama-3.1-8B n'encode pas linéairement l'intention de gonfler les coûts au-delà du prompt et du chiffre écrit $\rightarrow$ ne plus chercher de sondes sur (i-a) 8B ; passer à l'organisme (ii) ou à une échelle supérieure.