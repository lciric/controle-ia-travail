# Tour III.2, proposition B : critique croisée de méthode

**Signalement de pièce (règle 2).** Le bloc QUESTION DE L'ARBITRE est identique au bloc FAITS (même sha256) et ne contient pas de question distincte. Je traite donc le livrable du tour III.2. Les pièces A, C, D et E sont présentes et non coupées : chacune se termine par sa ligne de clôture.

**Statuts.** Les faits transmis ne portent aucune étiquette. A les cite comme « fait transmis (statut non étiqueté) ». C étiquette l'ablation de la Table 2 OBSERVÉ-NON-AUDITÉ et le reste RAPPORTÉ. E étiquette les Figures 3 et 4 OBSERVÉ-NON-AUDITÉ et le reste RAPPORTÉ. Je ne tranche pas entre ces attributions. Je signale seulement que le même fait porte des statuts différents selon la proposition.

**Conventions de ce texte.**
- Mes critiques sont des HYPOTHÈSES de méthode.
- Les calculs sont de l'arithmétique sur des lois standard (binomiale, normale).
- Tout paramètre que je choisis est **illustratif**.
- Les sections sont indépendantes : je ne fusionne pas les propositions (règle B1).

---

## Sur la proposition A

### (a) Défauts de méthode

1. **E1, H_B est vraie par construction si la lecture n'encode que la difficulté.**
   - Le bras 5 (« honnête qui échoue ») porte sur des items *plus durs* ; les saboteurs portent sur les items standard.
   - Si la lecture n'est qu'une fonction de la difficulté de l'énoncé, elle sera haute chez le saboteur, alors que sa réussite est basse. Elle sera basse dans le bras 5, avec une réussite basse.
   - Donc G(saboteur) − G(bras 5) > 0 sans aucune information sur l'intention. « Valeur de capacité » et « valeur = difficulté » ne sont pas exclusives dans ce dispositif.
   - E0 ne lève pas ce problème : son seuil (borne basse > 0,55) admet une lecture majoritairement liée à la difficulté.
   - Correctif : comparer, sur les *mêmes items*, les échecs du saboteur et les échecs honnêtes spontanés. Ces échecs existent dès que la probabilité de réussite p_i d'un item est strictement entre 0 et 1.

2. **E0 : « au-delà de l'énoncé » ne veut pas dire « au-delà du texte ».**
   - Aux frontières de paragraphe, le préfixe contient déjà une partie de la solution.
   - Fait transmis : l'AUC en position finale est « mostly stable above 0.8 ». Une prédiction intra-question peut donc venir du contenu visible.
   - Sans référence textuelle intra-question sur les mêmes préfixes, H_A ne peut pas être attribuée au canal interne.

3. **Bras 4 (LoRA) : l'écart Δ_V ≠ 0 est attendu par construction.**
   - Tout affinage déplace les activations des couches 2 à 4, quel que soit son objectif.
   - Le contrôle « affinage de même durée, objectif neutre » n'apparaît qu'en E4. En E1, le bras 4 ne peut donc pas départager les hypothèses.

4. **E2 : insertions hors politique.**
   - Le modèle lit des paragraphes qu'il n'a pas générés. La surprise liée à l'insertion peut suffire à séparer les épisodes.
   - Les « reformulations neutres » ne contrôlent cet effet que si elles passent par *le même* pipeline d'insertion. Le texte ne le précise pas.
   - Si le calibrage « δ < 0,1 » des insertions utilise l'estimateur qui sert aussi de cible à la sonde, l'instrument et la vérité terrain partagent leur bruit.

5. **Fuite entre sélection et nulle.** Les épisodes honnêtes « tenus à l'écart » le sont par épisode, pas par famille de tâches. Des épisodes de la même famille partagent leurs items, ce qui donne des fausses alertes optimistes.

6. **S9 : erreur d'appariement et inférence non identifiée.**
   - L'appariement est inversé : 72,2 % = 26/36 et 75,0 % = 27/36, pas l'inverse.
   - Surtout, avec un arrondi à une décimale, d'autres effectifs reproduisent les trois valeurs. Par exemple n = 500 : 389, 361 et 375 réussites.
   - « Petit sous-ensemble » n'est donc pas déductible des pourcentages. Seule la lecture du PDF peut le dire.

### (b) Lois sous lesquelles les critères perdent leur puissance

- **E0.**
  - Soit p_i la probabilité de réussite de la question i. Seules les questions avec p_i ∈ ]0,1[ informent l'AUC intra-question.
  - Si la loi des p_i est concentrée près de 0 et de 1 (illustratif : 80 % des items hors de [0,05 ; 0,95]), l'effectif utile tombe à environ 0,2 N.
  - L'IC de l'AUC s'élargit alors d'un facteur √5 ≈ 2,2, et le seuil 0,55 devient non jugeable sauf si N est grand.
- **E2, tranche |δ| < 0,1.**
  - Si δ est uniforme sur la tranche, son écart-type vaut ≈ 0,058.
  - Bruit Monte-Carlo de δ̂ avec n rollouts à p ≈ 0,5 : écart-type ≈ √(0,5/n).
    - n = 800 : ≈ 0,025, fiabilité ≈ 0,84.
    - n = 100 : ≈ 0,071, fiabilité ≈ 0,40, donc ρ observé ≈ 0,63 ρ vrai.
  - La borne basse « > 0,1 » perd sa puissance dès que n descend vers la centaine.
  - La tranche est en outre définie par δ̂, pas par δ : la contamination par des |δ| > 0,1 croît quand n baisse.
- **E3 et E4, fausses alertes à 1 % par épisode.**
  - Le quantile q̂_0,99 estimé sur n_h épisodes honnêtes n'est stable que si n_h·0,01 ≫ 1.
  - Avec n_h = 200 (illustratif), on attend 2 fausses alertes. L'IC binomial couvre alors environ 0,1 % à 3,6 %, et le critère est non jugeable.
  - Sous autocorrélation AR(1) de paramètre φ, le nombre effectif de pas vaut T(1−φ)/(1+φ). L'ordre de grandeur de 37 % donné en (c) suppose φ = 0.
- **E1.** Le d de Cohen de Δ_V est dilué par le taux π de sabotage effectivement réalisé dans le bras 3. Pour π faible, H_A et H_B tombent toutes deux dans la zone d'indécision.

### (c) Contrôles négatifs dont l'absence serait fatale

- LoRA neutre en E1 (même rang, même durée, données honnêtes).
- Référence textuelle intra-question en E0.
- En E2, insertions neutres issues du même pipeline, plus une insertion *dans la politique* : la continuation alternative du modèle lui-même.
- Séparation par famille entre sélection des neurones, calibration de la nulle et test.

Les contrôles déjà présents sont nécessaires mais pas suffisants : étiquettes permutées, neurones aléatoires, A/A, consigne inerte.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **La détection de la consigne est vraie par construction.**
   - M_S est obtenu par consigne système cachée, « masquée aux sondes lors de la lecture ».
   - Masquer des positions de lecture ne retire pas l'information : les états résiduels ultérieurs attendent sur la consigne.
   - Aucun bras « consigne inerte de même forme » n'existe. Toute détection peut donc être une lecture de la consigne.

2. **Exp. 1 : désaccord de politique.**
   - δ̂ est lu sur M_S, mais ΔV_tâche est estimé par les rollouts du *jumeau honnête*. Une erreur TD est définie relativement à une politique.
   - Même un lecteur parfait de V_tâche sous π_S divergerait de cette cible.
   - De plus, V_sabotage n'a pas d'estimateur défini : la condition ΔV_sabotage > +0,3 n'est pas opérationnelle.
   - Enfin, sélectionner les pas sur ΔV_tâche < −0,3 restreint la cible à un seul signe, ce qui écrase ρ structurellement.

3. **Exp. 3 : deux sources de variation confondues.**
   - ΔV̂ = V̂_final(M_S) − V̂_initial(M_H) mélange un effet de modèle et un effet de position.
   - Fait transmis : la sonde de valeur est lue à la position initiale, et l'AUC finale relève d'un autre régime. L'effet de position est présent dans *toute* trajectoire, y compris honnête.
   - La référence V̂_final(M_H) − V̂_initial(M_H) est absente.
   - H_A est une disjonction (« chute *ou* divergence KL dès le prompt »). La branche KL est vraie par construction dès que la consigne est dans le contexte. H_A est donc quasi infalsifiable.

4. **Références importées au lieu d'être recalculées.**
   - En Exp. 3 et dans le tableau (c), les valeurs 0,52, 0,48, 0,60 et 0,62 (Table 3, prédiction de réussite avant génération) servent de références pour une AUROC de détection de sabotage.
   - Ce sont des quantités différentes, calculées sur d'autres épisodes : la comparaison n'est pas jugeable.

5. **Exp. 4 : deux manipulations dans un seul duel.** Le patching et l'entraînement adverse sont réunis sous une même paire H_A/H_B. Leurs issues peuvent se croiser : le patching réduit le sabotage, l'entraînement contourne la sonde. Le duel n'a alors pas d'issue définie.

6. **Fuite entre sélection et nulle.** Les neurones sont sélectionnés sur M_H, et la nulle est calibrée sur M_H. Aucune séparation de données n'est précisée. Une nulle calculée sur l'échantillon d'apprentissage sous-estime la variance, donc les fausses alertes.

### (b) Lois sous lesquelles les critères perdent leur puissance

- **Vérité terrain des petits pas (Exp. 2 et (d)).**
  - Avec 16 rollouts par frontière à p ≈ 0,5, l'écart-type de V̂ vaut ≈ 0,125 et celui de δ̂ ≈ 0,18.
  - Des pas à |ΔV| ∈ [0,02 ; 0,05] sont donc non identifiables un par un.
  - Pour obtenir un écart-type de δ̂ ≤ 0,01, il faut n ≈ 0,5/10⁻⁴ = 5 000 rollouts par état.
  - Comme V ∈ [0,1], la condition ΣΔV < −0,5 exige en outre V₀ > 0,5. Elle est non jugeable au budget annoncé.
- **Puissance du CUSUM (Exp. 2).**
  - Sous biais constant b, écart-type σ et pas indépendants : AUROC = Φ((b/σ)√K / √2).
  - AUROC = 0,75 à K = 20 exige b/σ ≈ 0,21.
  - Sous AR(1) avec φ = 0,5 (illustratif), K_eff ≈ 6,7 et il faut b/σ ≈ 0,37.
  - Avec une sonde entraînée au-dessus de 0,3, la pente effective sous ce seuil peut être plus faible. Le critère perd alors sa puissance sans que H_B soit établie.
- **Exp. 1.** Si la variance de ΔV_tâche sur les pas retenus tend vers 0 (cible d'un seul signe, plage étroite), ρ est mal défini. La zone 0,05 < |ρ| < 0,25 ne falsifie rien.
- **Tableau (c), « ECE ≤ 1 % ».**
  - L'ECE mesure la calibration de probabilités, pas un taux de fausses alertes.
  - Pour estimer des fausses alertes de 5 % à ±1 % (IC à 95 %), il faut n ≈ 1,96² × 0,0475 / 10⁻⁴ ≈ 1 800 épisodes honnêtes indépendants, et davantage sous corrélation intra-famille.

### (c) Contrôles négatifs dont l'absence serait fatale

- Bras honnête avec consigne inerte de même forme.
- Moniteur textuel recalculé sur les mêmes épisodes.
- Référence de position V̂_final − V̂_initial chez M_H.
- LoRA neutre si M_S est obtenu par LoRA.
- Toutes les références recalculées sur les épisodes de test.
- Séparation par famille entre sélection et nulle.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le contrôle de la valeur initiale est vrai par construction.**
   - La valeur est lue *avant* que l'assignation soit visible, avec les mêmes poids. Une passe avant déterministe rend donc le score indépendant de l'assignation.
   - La vérification « par rejeu » contrôle le pipeline, pas une hypothèse.
   - Autre problème : le modèle combiné de comparaison inclut la *famille du dossier* comme covariable, alors que le test se fait sur des familles tenues hors apprentissage. L'effet de famille n'est pas estimable sur des familles jamais vues.

2. **Même poids : tout sabotage passe par la consigne.**
   - Réserver des familles de formulations inédites contrôle le lexique, pas le concept (« on m'a demandé de dégrader »).
   - Une issue H_A établirait la détection d'une *dégradation sur consigne*, pas d'un sabotage porté par les poids.
   - Le bras « saboteur par poids, sans consigne » est absent. La portée doit au minimum être restreinte explicitement.

3. **Positifs en intention de traiter.** Compter tout dossier assigné comme positif mélange l'efficacité de la manipulation et la puissance du détecteur. Si π diffère entre les bras « surveillance annoncée » et « non annoncée », l'écart de détection entre bras confond les deux.

4. **Règle d'union sur les étapes.** Les fausses alertes par dossier croissent avec le nombre d'étapes T. Si la dégradation modifie la longueur des dossiers, une partie de la détection vient de T.

5. **Alignement aux jalons.** Les jalons sont définis par les artefacts. Un saboteur peut produire une autre séquence d'artefacts : les jalons manquants ne sont alors pas manquants au hasard, et l'écart au jumeau est biaisé.

### (b) Lois sous lesquelles les critères perdent leur puissance

- **Dilution par π.**
  - Taux de détection observé = π·TPR_réalisé + (1−π)·TPR_non-réalisé.
  - Un gain de 10 points en intention de traiter exige un gain réel ≥ 0,10/π, soit ≥ 33 points pour π = 0,3 (illustratif).
  - Le critère conjoint perd sa puissance quand π est petit. Il devient non jugeable entre bras si π̂ n'est pas estimé bras par bras.
- **Grappes de familles.**
  - Effet de plan : 1 + (m−1)·ICC.
  - Avec m = 20 dossiers par famille et ICC = 0,1 (illustratifs), il vaut 2,9.
  - Un bootstrap par famille sur F < 20 familles (illustratif) donne des intervalles simultanés mal couverts. La règle « intervalle entièrement dans la région » devient non jugeable.
- **Plafond de 5 % avec marge.**
  - Pour borner les fausses alertes à 5 % ± 2 points, il faut environ 460 dossiers honnêtes indépendants, multipliés par l'effet de plan.
- **Règle d'union.**
  - Sous indépendance, fausses alertes par dossier = 