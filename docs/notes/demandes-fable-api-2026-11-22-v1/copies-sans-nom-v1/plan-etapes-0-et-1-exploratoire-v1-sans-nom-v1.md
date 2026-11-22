# Papier « dopamine » — étapes 0 et 1 en mode exploratoire : relecture du papier et plan du rejeu du chiffre publié sur MATH500 (v1)

**EXPLORATOIRE. Non opposable. Ni préenregistrement, ni verdict, ni porte.** Pièce de travail, non contre-lue (mode ouvert par le directeur, GO-2026-11-21-44). Elle ne lance rien et ne dépense rien : le devis est à part, et aucune carte ne tourne sans accord sur devis.

- Auteur : Claude Fable 5.2, concepteur. Date : 21 novembre 2026, 11:36 UTC. Dépôt à `ceeb437aa`.
- Pièces lues (chemin, empreinte) :
  - le papier, Xu, Yuksekgonul, Zou, « Sparse Reward Subsystem in Large Language Models », arXiv 2602.00986v2, `docs/sources/pdf/2602.00986v2.pdf` (`da004f53ff336b950bf51fb9a85fa424f5792579ac10dce45566ccb0e68e9039`), 25 pages, texte extrait page par page (`pdftotext -layout`) ; deux figures regardées en image (figure 4, p. 7 ; figure 6, p. 21) : ce qui en est lu « à l'œil » est dit tel et ne vaut pas chiffre ;
  - le brouillon v7 du préenregistrement court, suivi comme plan et non comme règle, `prereg/papier-dopamine-moniteur-v1/preenregistrement-court-papier-dopamine-v7-brouillon.md` (`e05f4a998704391a62e09a3a6a7ab9804850a9cedb9c01c5bb947d5322c315ef`), l. 1 à 154 et l. 310 à 311 ;
  - la consigne commune de méthode, `docs/procedures/consigne-commune-methode-de-recherche-v1.md` (`d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8`) ;
  - l'accord GO-2026-11-21-44, `registres/go.md`, l. 643, cette ligne seule ;
  - mes calculs, `prereg/papier-dopamine-moniteur-v1/exploratoire/calculs-devis-etape-1-rejeu-math500-exploratoire-v1.py` (`43c1a8942cf92fa202c2a52c075c8a5f7148292007246ac6806694f5f78be916`) et sa sortie `…-v1.txt` (`ec8bcd8825193f243d21120456580af756edf9ec503f5f1be66f29971c643e69`), cités « calcul, bloc ».
- Non ouvert : aucun résultat d'expérience, aucun épisode, aucun état interne, aucun code du dépôt. L'inventaire des épisodes et des états déjà sur disque (seconde moitié de l'étape 0) revient à la mère : il n'est pas fait ici.
- Les chiffres du papier sont des affirmations de ses auteurs, relues à la page citée ; ce ne sont pas des mesures du programme.

---

## A. Étape 0 — ce que dit le PDF

### A.1 Effectif du tableau 4 : non écrit, et ce n'est pas cent

- Tableau 4 (p. 9) : exactitude sur MATH500 de quatre façons de choisir l'étape suivante — décodage glouton 72,2 ; tirage au hasard 72,2 ; récompense implicite 75,0 ; sonde de surprise 77,8. Modèle : Qwen-2.5-7B-SimpleRL-Zoo, pas Llama (p. 8).
- Le texte dit « on the validation subset of MATH500 » et « averaged over three random seeds », quatre candidats par frontière de paragraphe (p. 8). **Aucun effectif, aucun intervalle, aucun écart entre graines.**
- Seul indice : part d'entraînement 0,8, graine 0 (tableaux 7 et 8, p. 19 et 20). Si MATH500 compte 500 questions, la part de validation en compte 100.
- **L'arithmétique écarte 100** (calcul, bloc 7). Une moyenne de trois graines sur 100 questions est un multiple d'un tiers de point : ni 72,2 ni 77,8 n'en sont. Un décodage glouton, déterministe, sur 100 questions rend un pourcentage entier. Effectifs compatibles près de cent : 96 et 108 ; 108 seul si le glouton est lu comme une seule passe. Les trois valeurs sont exactement 26, 27 et 28 trente-sixièmes. Au-dessus de 330 questions, l'arithmétique n'écarte plus rien.
- Témoin de ce calcul : l'exactitude d'origine de 75,2 % du tableau 2 (p. 5) est compatible avec 500 questions (376 sur 500) et pas avec 100 ; le calcul rend bien cela.
- Conséquence : le gain de 5,6 points du tableau 4 n'a ni effectif ni incertitude. Il ne peut appuyer aucune grandeur attendue pour la sonde de surprise.

### A.2 Corrélations de la sonde de surprise : en figure seulement — confirmé

- La seule mesure est la figure 4 (p. 7) : corrélation de rang entre la surprise prédite et la surprise estimée, sur MATH500, pour Qwen-2.5-7B et 14B-SimpleRL-Zoo, couches 20 à 22 et 15 à 17. **Aucune valeur dans le texte ni dans un tableau** ; le texte dit seulement que les courbes « remain largely invariant across a wide range of pruning ratios » (p. 7).
- À l'œil, non opposable : entre 0,08 et 0,38 ; les courbes ne sont pas plates (une couche passe d'environ 0,13 à environ 0,35 entre les taux 0,6 et 0,8) ; onze points par courbe, jusqu'à 0,95 environ, et non les quinze taux du tableau 8.
- Manquent aussi : le nombre de paragraphes gardés par le seuil, le nombre de continuations tirées par frontière (« K independent rollout completions », p. 6, sans valeur ; le K = 4 de la p. 8 est celui de la recherche guidée), tout intervalle. Rien sur Llama.

### A.3 Sonde non linéaire sur l'état complet : présente, mais jamais chiffrée

- La sonde de réussite attendue est elle-même non linéaire (perceptron à deux couches, p. 3 ; 1024 unités cachées, p. 19), et le premier taux d'élagage de la grille est 0,0 (p. 20) : le point de gauche de chaque courbe (figure 1, p. 5 ; figure 6, p. 21) **est** une sonde non linéaire sur l'état complet. Elle n'existe qu'en figure.
- Le tableau 3 (p. 8) n'a pas cette colonne. Son seul comparateur sur l'état complet est une sonde **linéaire** (« LCD », p. 8 et p. 25), d'une couche non dite. L'écart 0,69 contre 0,64 mêle donc trois choses : l'élagage, la non-linéarité, l'objectif de différence temporelle. Il n'isole pas la parcimonie.
- Le « taux optimal » du tableau 3 peut être 0,0 : la grille le contient. Le 0,69 peut donc être lu, pour une couche, sur l'état complet.
- À l'œil sur le panneau Llama de la figure 6 (p. 21), non opposable : au taux 0, environ 0,60 (couche 2), 0,63 (couche 3), 0,69 (couche 4) ; au meilleur taux de chaque couche, environ 0,61, 0,71, 0,70. Moyenne des trois : environ 0,64 au taux 0, environ 0,67 au meilleur taux. Le rejeu rapportera donc l'aire au taux 0 à côté de l'aire au meilleur taux.

### A.4 Évaluation sous le seuil : aucune — confirmé

- « we retain only paragraphs satisfying |δt| > 0.3 during training. The same threshold is applied during evaluation » (p. 6). Rien d'autre dans les annexes F, G et H (p. 22 à 24).
- Deux emplois sans seuil existent, qui ne sont pas des évaluations de la prédiction : la recherche guidée (p. 8), où la sonde note chaque paragraphe candidat et où seule l'exactitude finale est mesurée (tableau 4) ; les figures 3, 9 et 10 (p. 7, 23, 24), qui montrent un seul neurone sur deux réponses.
- La part des paragraphes que le seuil écarte n'est pas donnée.

### A.5 « Llama-3.1-8B » du tableau 3 est le modèle instruit (VO-1) — confirmé par l'usage du papier, pas par une phrase

- Le papier nomme « Llama-3.1-8B-Instruct [20] » en p. 4 et en p. 21 ; la légende de la figure 6 écrit « Llama-3.1-8B-Instruct » quand le titre du panneau écrit « Llama-3.1-8B » (p. 21) ; de même la figure 11 (p. 25) et son texte (p. 24). Le tableau 3 abrège de même « Phi-3.5-mini-instruct » en « Phi-3.5-mini » (p. 8, p. 21). Aucun Llama de base n'est nommé nulle part. La confiance demandée au modèle (p. 24 et 25) suppose un modèle instruit.
- Réserve : le tableau 3 porte Gemma-3-4B, absent de l'annexe D ; ce n'est donc pas le même lot d'expériences que la figure 6.
- Deux autres moitiés de VO-1 restent ouvertes après lecture. **L'effectif de MATH500 n'est écrit nulle part** dans le papier (500 est celui du nom ; les exactitudes du tableau 2, toutes multiples de 0,2, s'accordent avec 500). **Le taux de réussite de Llama sur MATH500 n'y est pas** : la tranche de mesure de l'étape 1 le donnera, et lui seul dit si la demi-largeur de 0,055 est atteignable (calcul, bloc 8 : 0,046 à 250 réussites sur 500, 0,053 à 150, 0,062 à 100).

### A.6 Six autres silences du papier, qui pèsent sur l'étape 1

1. **Le 0,69 est mesuré sur la part de validation** (part d'entraînement 0,8, graine 0, tableaux 7 et 8, p. 19 et 20), soit une centaine de questions si le jeu en compte 500, une seule graine. Son erreur d'échantillonnage est alors d'environ ±0,10 à 95 % (calcul, bloc 8). Les « shaded regions » des figures ne sont pas définies (p. 5, p. 21). **Le chiffre publié est une cible floue.**
2. L'objectif (équations 8 et 9, p. 4) ne dit pas si la cible est gelée ; ses indices sont incohérents (somme jusqu'à T + 1, terme final écrit en T). La sortie de la sonde n'a pas de fonction dite. Aucune normalisation de l'entrée pour cette sonde : celle de l'annexe F ne vaut que pour la sonde de surprise (p. 6, p. 22).
3. L'élagage : norme L1 des poids de la première couche ; aucun réentraînement n'est mentionné (p. 4).
4. L'invite « qwen-boxed » est donnée pour tous les modèles (tableau 6, p. 19) ; rien ne dit comment elle est rendue pour Llama.
5. « Lots de 4 » (p. 19) : quatre réponses ou quatre états, non dit. « Couches 2 à 4 » : convention d'indice non dite.
6. La longueur de la question : unité et sens non dits (p. 8). La confiance par jeton : « at the question position » (p. 8), « at the first generated position » (p. 25). Le tableau 3 porte des aires sous 0,5 (0,29 ; 0,41) : les scores n'y sont pas réorientés après coup.

---

## B. Étape 1 — plan exploratoire du rejeu

### B.1 Le chiffre, et ce qu'on attend sur pièce

**Le chiffre à rejouer : 0,69**, aire sous la courbe de la sonde de réussite attendue lue avant toute génération, MATH500, ligne « Llama-3.1-8B », colonne « Value Neurons », tableau 3, p. 8 ; « obtained at the optimal pruning ratio and averaged across layers 2–4 » (p. 8).
Même ligne, rejoués et rapportés à côté : sonde linéaire sur l'état complet 0,64 ; confiance demandée au modèle 0,69 ; confiance par jeton 0,54 ; longueur de la question 0,63.

Ce qu'on attend, en mots de description et non de verdict :
- notre aire au meilleur taux, moyennée sur les couches 2 à 4, avec son intervalle à 95 % : « contient 0,69 », « en dessous », « au-dessus » (au-dessus : recherche de fuite d'abord, R4), ou « trop large pour dire » si la demi-largeur dépasse 0,055 ;
- la cible étant floue (A.6, point 1), une valeur entre 0,60 et 0,75 environ ne contredit pas le papier. **Ce qui sert au programme est ailleurs** : notre aire, sur nos 500 questions, comparée sur les mêmes questions à la longueur, à la sonde linéaire et aux étiquettes du jeu (niveau, matière).

### B.2 Là où le papier se tait : lecture principale et variante

| Point | Lecture principale (à la lettre, ou la plus simple) | Variante rapportée | Où |
|---|---|---|---|
| Rendu de l'invite pour Llama | gabarit de dialogue de Llama ; consigne du système et phrase finale de « qwen-boxed » (libellé à relever sur le code public de l'outil d'évaluation des modèles Qwen de mathématiques, **supposé** ici : « Please reason step by step, and put your final answer within \boxed{}. ») | chaîne de Qwen à la lettre | hors devis |
| Position de lecture | dernier jeton de l'invite entière, en-tête de réponse compris (« initial input position s0 », p. 4 ; « before the model begins generating », p. 24) | dernier jeton du texte de la question ; même sonde, autre position | gratuit |
| Indice de couche | sortie du bloc k = `hidden_states[k]` de la bibliothèque transformers, k = 2, 3, 4 | k = 3, 4, 5 (indice compté de zéro) ; k = 1 gardé | bloc g |
| Cible de l'objectif | non gelée : le gradient passe par les deux termes (lettre de l'équation 9) | cible gelée | bloc h |
| Sortie de la sonde | linéaire, sans borne | — | — |
| Lot | 4 réponses ; perte sommée sur les positions d'une réponse, moyennée sur le lot | — | — |
| Élagage | masque des entrées de plus petite norme, sans réentraînement | réentraînement sur les entrées gardées | hors devis |
| Taux « optimal » | le meilleur des quinze, par couche, sur les questions évaluées | un taux commun aux trois couches ; taux 0 ; taux choisi par validation emboîtée | gratuit ; bloc e |
| Longueur de la question | moins le nombre de jetons | moins le nombre de caractères | gratuit |
| Correction des réponses | dernière expression encadrée, normalisée, équivalence symbolique | égalité stricte après normalisation ; nombre de désaccords rapporté | gratuit |

### B.3 Ce que le développeur code

Noms indicatifs ; le développeur garde ceux du dépôt. Chaque garde est essayée sur un cas sain et sur un artefact avant toute dépense (R5). Graines par `numpy.random.SeedSequence`, une racine écrite au manifeste, une clé par tâche (R9). Tout fichier de sortie porte « exploratoire » et une version dans son nom (R12).

1. **Jeu (`donnees_math500`).** Charge MATH500 (jeu public ; identifiant et champs **supposés** : énoncé, réponse, matière, niveau, identifiant), l'écrit en lignes canoniques, en prend l'empreinte. Garde : 500 questions, identifiants uniques, empreinte égale à celle du manifeste. *Sain* : le jeu. *Artefact* : 499 lignes ; un identifiant en double.
2. **Invite et génération (`generation`).** Température 1,0 ; top_p 0,95 ; un tirage par question ; au plus 16 000 jetons neufs (tableau 6, p. 19). Une graine par question. Moteur : génération par lots continus (vLLM, comme le papier) si le dépôt l'a ; sinon deux passes, la première bornée à 2 048 jetons, la seconde reprenant les seules réponses inachevées jusqu'à 16 000. Écrit : jetons de l'invite, jetons de la réponse, motif d'arrêt, durée. Garde d'invite : elle finit par l'en-tête de réponse ; décodée puis recodée, elle rend les mêmes jetons ; l'invite rendue de la question 0 est écrite au manifeste. *Artefact* : en-tête ôté ; réponse vide.
3. **Correction (`correction`).** Issue r = 1 si la dernière expression encadrée équivaut à la référence ; pas d'expression encadrée, ou réponse coupée au plafond : r = 0 et drapeau. *Sain* : vingt paires au verdict connu (fractions, décimales, unités, intervalles, texte, accolades imbriquées). *Artefact* : bonne valeur hors du cadre (0 attendu) ; deux cadres (le dernier) ; accolades mal fermées (drapeau, pas d'arrêt brutal).
4. **Extraction (`extraction_etats`).** Une passe sur l'invite suivie de la réponse. États de sortie des blocs 1, 2, 3, 4, 5, 7, 15, 23, en demi-précision, à la position de lecture et à chaque jeton de la réponse ; probabilité du jeton le plus probable à la position de lecture (confiance par jeton). Trois gardes. **Position** : l'état de la position de lecture, recalculé sur l'invite seule, égale celui de la passe entière à la tolérance près, et le jeton rangé en position j est le j-ième de la réponse. *Artefact* : indice décalé d'un ; lot complété à droite et lu au dernier indice. **Valeurs** : ni valeur non finie ni dépassement de la demi-précision. **Couches basses** : les blocs 1 à 5 ne s'extraient que d'une source marquée « MATH500 public » (brouillon v7, l. 129, qui cite GO-2026-11-21-06, point 3, pour les couches 2 à 4 ; étendu ici aux blocs 1 et 5). *Artefact* : source marquée « épisode du programme » : refus.
5. **Sonde (`sonde_reussite`).** Perceptron entrée → 1024 → 1, ReLU ; AdamW, pas 1e-4, décroissance 0,01 ; lots de 4 réponses ; 100 époques ; γ = 1 − 1e-5 (tableau 7, p. 19). Perte d'une réponse de T jetons : Σ pour t de 1 à T de (γ·V(s_t) − V(s_{t−1}))², plus (r − V(s_T))² (équations 8 et 9, p. 4). Gardes : un terme final par réponse, compté ; aucune différence prise entre deux réponses. *Sain* : suites synthétiques à valeur connue, aire d'au moins 0,95 à la position de lecture. *Artefact* : terme final ôté (la sonde nulle a alors une perte nulle : la garde doit s'allumer) ; deux réponses collées sans frontière.
6. **Élagage (`elagage`).** Norme L1, par entrée, des poids vers les 1024 unités ; pour chacun des quinze taux p (tableau 8, p. 20), on masque ⌊p·4096⌋ entrées de plus petite norme ; à 0,99 il en reste 41. *Sain* : p = 0 rend la sonde entière à l'identique ; les ensembles gardés sont emboîtés. *Artefact* : masque posé sur les unités cachées.
7. **Découpage (`decoupage`).** Par graine, une permutation des 500 questions, cinq plis de 100 ; chaque sonde s'entraîne sur 400 questions (part 0,8) et note les 100 autres. Emboîté : 320 pour apprendre, 80 pour choisir le taux. Garde : aucune question des deux côtés ; chaque question notée une fois par graine. *Artefact* : un identifiant recopié dans le pli d'essai.
8. **Mesures (`mesures`, sur processeur, après la destruction de la carte).** Voir B.4. *Sain* : aire refaite à la main sur un petit tableau, ex æquo compris. *Artefact* : scores tous égaux (0,5 et drapeau) ; pli à une seule classe (arrêt dit, jamais une valeur manquante muette).
9. **Contrôles (`controles`).**
   - *Étiquettes permutées* : les issues sont permutées entre questions avant l'apprentissage. Attendu : aire de 0,5 au taux 0. Échec : l'intervalle de l'aire au taux 0 exclut 0,5. L'aire au meilleur des quinze taux y dépasse 0,5 par construction : c'est la mesure de l'optimisme de la sélection, rapportée.
   - *Vérité plantée* : issue tirée à pile ou face par question ; une direction fixe, tirée au hasard, est ajoutée à tous les états de la question, de signe égal à l'issue, de force a fois l'écart type de la projection des états sur cette direction. **a = 4, écrit au manifeste avant la course, jamais changé.** Attendu : borne basse de l'aire d'au moins 0,9. Échec : en dessous.
   - *Sans critère, sur processeur* : longueur de la question ; confiance par jeton ; sonde linéaire sur l'état complet, mêmes plis ; **régression sur le niveau et la matière du jeu, mêmes plis** (ajout du concepteur : c'est le comparateur qui dit si la sonde lit autre chose que la difficulté affichée).
   - *Confiance demandée au modèle* : invite de l'annexe J (p. 24 et 25), retirée jusqu'à obtenir un nombre.
10. **Manifeste, budget, destruction (`course`).** Manifeste : configuration et empreinte, versions, révision des poids, empreinte du jeu, graines, commit, force plantée, ordre des blocs, seuils des gardes, empreinte du relevé d'offres, identifiant de l'accord. Horloge : aucun bloc lancé après 5 h 30 ; destruction par l'identifiant de l'instance à 6 h 30 (R10). Après chaque bloc : inventaire (noms, tailles, empreintes) et rapatriement des scores, des poids des sondes, des textes et des états de la position de lecture. *Sain* : horloge sous le budget, le bloc part. *Artefact* : horloge simulée au-delà, refus.

### B.4 Ce qui se mesure

Pour une graine g, un pli k, une couche l, un taux p : A(g, k, l, p), aire sous la courbe de la sonde élaguée lue à la position de lecture, contre l'issue, sur les 100 questions du pli.
- **Aire au meilleur taux**, la quantité du papier : moyenne sur g, k et l ∈ {2, 3, 4} du maximum sur p de A. C'est elle qu'on met en face de 0,69.
- À côté : aire au taux 0 ; aire à un taux commun aux trois couches ; aire au taux choisi par validation emboîtée ; les courbes par couche (à mettre en face de la figure 6) ; les couches 7, 15, 23 et 1, 5.
- **Excès sur le hasard sous la même sélection** : aire au meilleur taux moins la même quantité sous étiquettes permutées.
- **Écarts appariés**, sur les mêmes questions : sonde moins longueur ; sonde moins sonde linéaire ; sonde moins niveau et matière.
- Intervalles : 2 000 tirages des questions à l'intérieur de chaque pli, les mêmes questions pour toutes les couches et tous les taux, **la sélection du taux refaite dans chaque tirage**, percentiles. Ils ne portent pas la variabilité de l'apprentissage : l'étendue entre graines est rapportée à part.
- Rapportés aussi : taux de réussite du modèle, longueur des réponses, part des réponses au plafond, part sans expression encadrée, débit mesuré.

### B.5 Ordre de la course et arrêts

1. Sur processeur, sans dépense : essais des gardes ; jeu chargé et empreint ; manifeste écrit.
2. **Tranche de mesure, 32 questions.** Arrêt et destruction si : 4 réponses ou plus au plafond ; longueur moyenne au-dessus de 2 400 jetons ; taux de réussite sous 10 % ou au-dessus de 90 % ; fin du noyau projetée au-delà de 5 h 30.
3. Génération des 468 autres. Arrêt avant extraction si plus de 5 % des réponses sont au plafond ou plus de 25 % sans expression encadrée.
4. Confiance demandée ; extraction ; gardes de position et de valeurs sur toutes les séquences.
5. **Noyau** : vérité plantée (5 sondes, couche 3) — si elle échoue, arrêt, la chaîne est fausse ; puis couches 2 à 4, cinq plis, graine 0 (15 sondes) ; puis étiquettes permutées (5 sondes).
6. **Blocs en plus**, dans cet ordre, chacun lancé seulement si l'horloge le permet : deux graines de plus (30) ; validation emboîtée (15) ; couches 7, 15, 23 (15) ; cible gelée (15) ; couches 1 et 5 (10).
7. Inventaire, rapatriement, destruction ; mesures sur processeur.

### B.6 Ce que la sortie dira et ne dira pas

Elle dira : notre aire sur 500 questions publiques, ses comparateurs sur les mêmes questions, et si la chaîne (génération, correction, extraction, sonde, élagage) passe ses deux contrôles. Elle ne dira pas : que le papier est « reproduit » ou « non reproduit » (cible floue, mode exploratoire) ; que la porte de reproduction du brouillon est passée ; rien sur les épisodes du programme ; rien sur la sonde de surprise.

---

## Relevé de méthode

**Chaîne de raisonnement.**
1. Le chiffre à rejouer est 0,69, au meilleur taux, moyenné sur les couches 2 à 4. — PDF, p. 8, tableau 3 et le paragraphe au-dessus (`da004f53…`).
2. Il est mesuré sur la part de validation, graine 0. — PDF, p. 19 et 20, tableaux 7 et 8. Que cette part compte 100 questions : supposé (l'effectif du jeu n'est pas écrit).
3. Sur 100 questions, une aire de 0,69 a une demi-largeur d'environ 0,10. — calcul, bloc 8 ; pas 2.
4. Le « Llama-3.1-8B » du tableau 3 est le modèle instruit. — PDF, p. 4, 8, 21, 24, 25 : inférence de l'usage du papier.
5. La recette. — PDF, p. 4 (objectif, lecture, élagage), p. 19 (génération, optimisation), p. 20 (grille).
6. Les dix lectures de B.2 là où le papier se tait. — supposé ; chaque variante est nommée.
7. Cinq plis de 100 questions donnent une demi-largeur de 0,046 à 0,062 selon le taux de réussite. — calcul, bloc 8 ; le taux de réussite : inconnu, mesuré par la tranche.
8. L'effectif du tableau 4 n'est pas 100. — calcul, bloc 7 ; PDF, p. 8 et 9.
9. Corrélations en figure seulement ; aucune évaluation sous le seuil ; sonde non linéaire sur l'état complet en figure seulement. — PDF, p. 6, 7, 8, 20, 21, 22 à 24.

**Objets de contrôle.**
- *La chaîne de la sonde.* Objet faux : étiquettes permutées ; prévu : aire de 0,5 au taux 0. Objet vrai : vérité plantée de force 4 ; prévu : borne basse d'au moins 0,9. Rendu : à la course ; les deux mêmes objets passent d'abord en synthétique sur processeur.
- *Le calcul d'effectif (A.1).* Objet vrai : 75,2 % sur 500 questions, compatible attendu. Objet faux : 75,2 % sur 100, incompatible attendu. Rendu : compatible, incompatible (calcul, bloc 7, dernière ligne).
- *Les gardes* : chacune a son cas sain et son artefact en B.3 ; non encore exécutées.

**Premier pas non justifié.** Le pas 2, pour sa seconde moitié : rien dans le papier ne dit combien de questions porte le 0,69. Le justifieraient le code ou les données des auteurs. Le pas 6 est supposé de bout en bout et le dit.

**Mode d'échec affecté.** Sans objet : cette pièce n'est pas une relecture.

**Dérivation de l'énoncé seul.** Sans objet : cette pièce n'est pas une re-dérivation.

**Trouvaille de côté.**
- Les trois exactitudes du tableau 4 sont exactement 26, 27 et 28 trente-sixièmes, et excluent un effectif de 100 ; le gain publié de la sonde de surprise n'a donc ni effectif ni incertitude connus. Non poursuivi.
- Le 0,69 du tableau 3 égale, à l'œil, la couche 4 seule de la figure 6 plutôt que la moyenne des trois couches (environ 0,67 au meilleur taux). L'écart est de l'ordre de l'erreur de lecture d'une figure : c'est une question, pas un constat.
- Les courbes de la figure 4 ne sont pas plates et n'ont que onze points ; le texte les dit « largely invariant ».

**Évaluateur et conseil.**
- Ce qui juge le rejeu : le module de mesures et les deux contrôles. Il n'est encore admis sur aucun témoin : les essais de B.3 sont à faire avant la dépense.
- Par où un bon chiffre viendrait sans le mériter : le meilleur de quinze taux choisi sur les questions notées (d'où l'excès sur les étiquettes permutées et le taux emboîté) ; une sonde qui lit la matière, le niveau ou la longueur (d'où les écarts appariés) ; un correcteur dont les erreurs suivent le type de question (d'où le nombre de désaccords) ; une position de lecture décalée dans la réponse (d'où la garde de position).
- Conseil au développeur : la difficulté est dans la correction des réponses et dans la position de lecture, pas dans la sonde ; écrire et essayer ces deux gardes d'abord.

## Ce que cette pièce ne dit pas

Aucun chiffre lu « à l'œil » n'est opposable. Le libellé de l'invite et les champs du jeu sont écrits de mémoire : à relever sur leur source avant la course. Le taux de réussite de Llama sur MATH500, la longueur de ses réponses et le débit ne sont pas connus : la tranche de mesure les donne. Non contre-lue.
