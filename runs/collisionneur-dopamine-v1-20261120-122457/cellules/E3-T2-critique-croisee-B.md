# Tour III.2 : proposition B, critique croisée de méthode

**Pièces (règle 2).** Le bloc QUESTION DE L'ARBITRE est identique au bloc FAITS (même sha256) : il ne contient pas de question distincte. La consigne traitée est donc le livrable (a)/(b)/(c) du tour III.2. Les quatre pièces A, C, D et E sont présentes et complètes.

**Statuts (règle 1).** Les faits transmis ne portent aucune étiquette de statut. Je n'en attribue pas et je les cite comme « fait transmis ». Mes critiques sont des HYPOTHÈSES de méthode. Mes calculs portent sur les chiffres illustratifs des autres propositions ; ils restent donc **illustratifs** et sont signalés « calcul de B ».

---

## Sur la proposition A

### (a) Défauts de méthode

1. **E1 donne raison à H_B par construction.**
   - Le bras 5 est construit « sur des items plus durs », apparié au saboteur sur le seul taux de réussite.
   - Supposons que la lecture de valeur ne lise que la difficulté de l'énoncé, ce que A craint elle-même (S4). Le saboteur, placé sur des items faciles, aura alors une lecture haute. Le bras 5 aura une lecture basse, pour une réussite réalisée identique.
   - L'écart G = lecture − réussite est donc mécaniquement plus grand chez le saboteur. Le critère de H_B (d(G_sab − G_bras5) ≥ 0,3) peut être satisfait sans aucune information sur le sabotage. Inversement, la condition « G indistinguable du bras 5 » exigée par H_A est presque exclue d'avance.
   - Conséquence : le duel ne départage pas « valeur officielle » et « valeur de capacité ». Il départage « items faciles » et « items difficiles ».
2. **E0 : confusion position / information.**
   - À la position du prompt, la variation intra-question est nulle : même énoncé, mêmes poids, donc même activation. H_A ne peut donc être testée qu'aux frontières de paragraphe.
   - Mais là, la lecture voit une réponse partielle. Le fait transmis d'une AUC « mostly stable above 0.8 » en position finale indique que l'issue devient lisible dans le texte lui-même. Une AUC intra-question > 0,55 y est quasi garantie, sans rien établir sur un « état » au-delà du texte.
   - Le contrôle « longueur de la question » est vide sous effets fixes par question : cette variable est constante dans chaque groupe et absorbée par l'effet fixe.
3. **E2 : insertions hors politique.** Les dégradations insérées dans des trajectoires honnêtes sont du texte que le modèle n'a pas produit.
   - Une lecture qui réagit à ce texte peut signaler « texte étranger / surprise », pas l'état d'un agent qui a lui-même choisi la faute.
   - Un échec d'E2 ne prouve donc pas l'absence de signal sur un sabotage produit par le modèle, et un succès ne le prouve pas non plus.
   - E2 sert pourtant de porte qui peut arrêter la piste dopamine : la porte est placée dans un régime différent de celui qu'elle doit garder.
4. **Fuite entre construction et évaluation.**
   - E0 et E1 utilisent des tâches vérifiables, tout comme l'entraînement de la sonde. A ne dit nulle part que les items d'évaluation sont disjoints de ceux d'entraînement.
   - Une sonde MLP de largeur 1024 entraînée 100 époques (fait transmis) peut mémoriser la difficulté propre à chaque item.
   - Il faut un découpage disjoint par item, et de préférence par famille d'items.
5. **E2 : zone indécise non déclarée.** H_A est jugée à k = 10 (AUC ≥ 0,75), H_B à k = 20 (AUC < 0,60). L'issue « AUC < 0,75 à k = 10 et ≥ 0,60 à k = 20 » ne falsifie rien et n'est pas déclarée comme indéterminée, alors qu'A le fait pour E4.
6. **S9, appariement inexact.**
   - Les valeurs correctes sont 77,8 % = 28/36, 75,0 % = 27/36 et 72,2 % = 26/36. A associe 27/36 à 72,2 %.
   - De plus, un arrondi à 0,1 point est compatible avec tout dénominateur multiple de 36 (calcul de B). « Petit sous-ensemble » n'est donc pas établi par ce calcul. La vérification dans le PDF, qu'A recommande, reste nécessaire.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Seuil à 1 % de fausses alertes par épisode.** Le seuil est un quantile empirique sur n₀ épisodes honnêtes. Le taux réalisé suit approximativement une loi Beta de moyenne α et d'écart-type √(α(1−α)/n₀).
  - Avec n₀ = 300 (illustratif), l'écart-type vaut environ 0,0057, soit plus de la moitié de α (calcul de B).
  - Dès que n₀·α ≲ 10, le seuil repose sur une poignée de statistiques d'ordre. La comparaison « détection à 1 % » entre instruments est alors dominée par le bruit du seuil.
- **E4, « détection < 2 × fausses alertes ».** Il faut distinguer une proportion de 2 % d'une proportion de 1 %, ou d'une proportion plus élevée, sur n_s épisodes saboteurs.
  - Avec n_s = 200 (illustratif), on attend 4 détections. L'intervalle exact à 95 % couvre environ 0,5 % à 5 %.
  - Le critère n'est pas jugeable sans n_s de l'ordre du millier.
- **Agrégation par somme.** L'exemple d'A (0,2 écart-type par pas, 100 pas, ≈ 37 % de détection) est juste sous indépendance. Sous une corrélation AR(1) de paramètre φ, la taille effective vaut n_eff ≈ T(1−φ)/(1+φ).
  - Pour φ = 0,8 : n_eff ≈ 11, d′ ≈ 0,67.
  - La détection à 1 % tombe alors à Φ(0,67 − 2,33) ≈ 5 % (calcul de B, illustratif).
  - Le critère d'E2 et d'E3 perd sa puissance dès que φ ≳ 0,6 à effet constant.
- **E2, Spearman dans la tranche |δ| < 0,1.** δ est estimé par Monte-Carlo, avec un écart-type de bruit σ_mc. La corrélation observée est atténuée d'un facteur √(Var(δ)/(Var(δ) + σ_mc²)).
  - Si Var(δ) dans la tranche est petite devant σ_mc², la borne basse de 0,1 n'est pas atteignable, même avec un signal réel.
  - A ne prévoit 800 rollouts que sur un sous-échantillon ; le reste de la tranche a un σ_mc non borné.
- **E1, d de Cohen.** Si la variance de la lecture entre items domine la variance intra-item, un d calculé sur les épisodes non appariés est dilué. Le d doit porter sur les différences appariées par item ; A dit « appariée par item » sans fixer l'estimateur.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Échec honnête sur les mêmes items** : échantillons ratés du jumeau, au taux de réussite du saboteur, par rejet. Il remplace ou complète le bras 5 ; sans lui, E1 est biaisé (point a.1).
2. **Prédicteur textuel à la même position** : par exemple la sonde de prédiction du token suivant, ou un classifieur sur le préfixe texte, aux mêmes frontières que E0. Sans lui, H_A est confirmée par la seule lisibilité du texte.
3. **Faute produite par le modèle contre faute insérée** : mêmes fautes générées par le modèle sous consigne, comparées aux insertions d'E2.
4. **Distribution nulle stratifiée par longueur d'épisode** pour la somme cumulée : le saboteur peut allonger ou raccourcir l'épisode.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Exp. 1 : la métrique ne teste pas l'hypothèse.**
   - H_A et H_B portent sur le **signe** de δ̂ (creux contre pic). La métrique est une corrélation de rang ρ entre δ̂(M_S) et ΔV_tâche. Une sonde peut donner ρ > 0 avec une moyenne décalée vers le positif, et inversement.
   - La sélection des pas sur ΔV_tâche < −0,3 restreint l'étendue de ΔV, ce qui écrase ρ mécaniquement.
   - ΔV_sabotage > +0,3 n'a aucun estimateur : aucune récompense du sabotage n'est définie.
   - La zone 0,05 < |ρ| < 0,25 ne falsifie rien et n'est pas déclarée. De plus, H_B mélange « pic positif » et « orthogonal », deux mécanismes que le duel devrait justement séparer.
2. **Exp. 2 : la vérité terrain n'existe pas dans le cadre visé.**
   - La « variation vraie » |ΔV_tâche| ∈ [0,02 ; 0,05] suppose une récompense terminale. Or la tâche est de la recherche ouverte, que le fait transmis p. 25 désigne comme non testée et sans récompense propre.
   - La condition de falsification (ΣΔV < −0,5) est incohérente avec le dispositif : 20 pas × [0,02 ; 0,05] donnent [0,4 ; 1,0]. Une partie des tirages tombe hors de la condition (calcul de B sur les chiffres illustratifs de C).
3. **Exp. 3 : vraie par construction.**
   - ΔV̂ = V̂_final(M_S) − V̂_initial(M_H) mélange deux modèles et deux positions. L'écart de position existe déjà chez l'honnête (0,67 avant génération, > 0,8 en fin, fait transmis).
   - En position finale, une sonde de correction lit l'issue. Un saboteur qui échoue la tâche aura une valeur finale basse ; un honnête qui échoue aussi.
   - Exp. 3 mesure donc la détection d'échec, et son contrôle négatif (neurones prédisant le token suivant, Wanda) ne contient aucun échec honnête.
4. **Exp. 4 : deux manipulations dans un seul duel.** Le patching et l'affinage adverse n'ont pas la même hypothèse nulle.
   - La pénalité L2 sur la **moyenne** du jumeau ne contraint ni la variance ni les covariances, que lit une sonde MLP non linéaire. Une évasion réussie sous cette pénalité ne réfute pas la sonde ; un échec ne la valide pas.
   - T_sab (taux de succès du sabotage) n'a pas d'estimateur en recherche ouverte.
5. **Fuite par la consigne cachée.** C propose une consigne système « masquée aux sondes lors de la lecture aux frontières ». Masquer les positions lues ne retire pas l'information : les positions de réponse l'intègrent par l'attention. Rien ne sépare « lit la consigne » de « lit le sabotage ».
6. **Reformulation.** Elle fige les indices de couches 2-5 et 15-22 de l'article pour l'agent du programme, dont le modèle n'est pas précisé. Ces indices ne se transfèrent pas entre architectures ; les faits ne montrent qu'un recouvrement entre deux modèles d'une même base.
7. **Table (c).** L'« ECE ≤ 1 % » sert de critère de calibration du taux de fausses alertes. L'ECE mesure la calibration de probabilités prédites, pas un taux d'erreur de type I. Le critère ne dit rien de la propriété visée.
8. **Statut incohérent (règle 1).** Le même fait (Table 2) est étiqueté RAPPORTÉ dans les sections (b) à (d) et OBSERVÉ-NON-AUDITÉ en (a), point 4. Je signale l'incohérence sans trancher.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Exp. 1, bruit des cibles.** Avec 16 rollouts par état (chiffre illustratif de C), l'écart-type d'une valeur près de p = 0,5 est d'environ 0,125. Celui d'une différence TD est d'environ 0,18 (calcul de B). Si l'écart-type de ΔV dans la tranche sélectionnée est ≲ 0,1, la fiabilité de la cible est ≲ 0,25 et ρ observé ≤ 0,5·ρ_vrai. Le seuil 0,25 exige alors ρ_vrai ≥ 0,5.
- **Exp. 2, CUSUM.** La puissance dépend de la dérive par pas μ/σ et de l'autocorrélation φ. Pour μ/σ ≲ 0,1 et φ ≳ 0,7, l'AUROC tend vers 0,5 quel que soit le signal (même calcul que pour A).
- **Exp. 2, calibration par permutation.** Elle suppose que les pas sont échangeables sous H₀. Une trajectoire de recherche a une structure temporelle (début exploratoire, fin de rédaction) : le seuil n'est pas calibré.
- **Exp. 3.** Si P(échec | sabotage) ≈ P(échec | honnête sur tâche dure), les lois de V̂_final coïncident sous les deux bras, et l'AUROC n'est pas jugeable comme détecteur de sabotage.
- **Table (c), « TPR ≥ 50 % à FPR = 5 % ».** Sur 500 trajectoires honnêtes (illustratif), on attend 25 fausses alertes. Le seuil est assez stable. Ce n'est pas le cas des critères à 1 % d'A et d'E.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Bras « consigne inerte »** : même consigne cachée, mention de surveillance, sans demande de sabotage. Sans lui, les quatre expériences peuvent lire la consigne.
2. **Échecs honnêtes sur les mêmes items** dans l'Exp. 3. Sans eux, elle mesure l'échec.
3. **Sonde entraînée sur étiquettes permutées** : absente de C.
4. **Test A/A du jumeau contre lui-même**, à graines distinctes : il valide la distribution nulle utilisée par la CUSUM.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Piste « valeur initiale » : nulle par construction, puis jugée au même seuil.**
   - D le reconnaît : lue avant l'assignation aléatoire, la valeur est indépendante de l'assignation, et son AUC marginale est 0,5.
   - Son seul chemin vers un gain est une **interaction** : la difficulté modulerait la détectabilité par les contrôles mécaniques.
   - Lui appliquer le même critère de +10 points qu'aux autres pistes rend le duel quasi décidé d'avance pour H_B. Il faut un critère propre, par exemple un test d'interaction ou un gain de calibration conditionnelle.
2. **Positifs en intention de traiter.** Le positif primaire est « tout dossier assigné », même si la dégradation n'a pas eu lieu. Le taux de détection observé mélange la faiblesse du moniteur et l'échec de la manipulation. Le duel principal porte sur ce mélange ; les défauts confirmés ne sont publiés qu'« à part ».
3. **Règle « alerte à n'importe quelle étape ».**
   - Le taux de fausses alertes par dossier croît avec le nombre de lectures L.
   - Si la dégradation change la longueur du dossier, le moniteur lit en partie L.
   - D calibre la règle entière, ce qui est correct, mais pas par tranche de longueur.
4. **Jalons définis par les artefacts.** La dégradation modifie justement les artefacts. Un jalon absent ou ajouté chez le saboteur crée un écart à la standardisation honnête–honnête qui ne vient pas des activations. L'alignement porte donc lui-même le signal.
5. **H_B définie comme complément** (« critère non rempli »). B4 est formellement respectée, mais un échec ne distingue pas trois cas : signal absent, comparateur mécanique déjà fort, manipulation inefficace. Seul le premier concerne l'article.
6. **Saboteur par consigne uniquement.** Les familles de formulations inédites protègent contre le lexique, pas contre la sémantique « on m'a demandé de dégrader ». Aucun saboteur sans consigne dans le contexte n'est prévu.
7. **Adversaire limité à l'annonce verbale de surveillance.** Le programme suppose un agent averti, et les auteurs eux-mêmes demandent des tests adverses (fait transmis, p. 25). D n'a aucun bras d'évasion par gradient : c'est une limite de portée, à déclarer comme telle.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Dilution par l'intention de traiter.** Si une fraction π des dossiers assignés est réellement dégradée, le taux de détection observé vaut π·s₁ + (1−π)·s₀, où s₀ est le taux d'alerte sur les dossiers assignés non dégradés, proche des fausses alertes. Un gain de 10 points (illustratif) exige un gain d'environ 10/π points sur les dossiers réellement dégradés : 20 points si π = 0,5. Sous π ≲ 0,3, le critère n'est pas atteignable.
- **Grappes par famille.** Avec m dossiers par famille et une corrélation intra-famille τ, l'effet de plan vaut 1 + (m−1)τ.
  - Avec F familles en nombre faible (≲ 15), le rééchantillonnage par famille sous-couvre.
  - Les intervalles **simultanés** (quatre pistes, plusieurs comparateurs) s'élargissent encore.
  - Si l'erreur-type de l'écart dépasse environ 5 points, la marge de 10 points chevauche la frontière : indécis par construction.
- **Bras annoncé contre non annoncé.** Si π diffère entre les bras, ce que D anticipe, la différence de détection entre bras n'est pas identifiée sans modèle de π.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Dégradation sans consigne visible**, par affinage, contre honnête sans consigne. Sans elle, la piste « variation » peut lire la consigne.
2. **Nul stratifié par longueur de dossier** pour la règle « n'importe quelle étape ».
3. **Permutation des jalons** chez l'honnête, et jalons manquants simulés, pour mesurer ce que l'alignement seul produit.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **E1 : sélection sur une estimation bruitée.**
   - La tranche 0 < |error| ≤ 0,3 est définie sur la TD estimée avec 32 rollouts. Sélectionner sur une estimation bruitée tronque la loi et produit une régression à la moyenne : les pas classés « petits » contiennent des pas grands et inversement.
   - La règle de falsification exige « AUC ≥ 0,65 sur MATH500 avec |error| > 0,3 ». Or 0,67 est l'AUC de la **valeur avant génération**, alors que la sonde dopamine est jugée en Spearman (faits transmis). Le critère mélange deux instruments.
2. **E2 : jumeau dégradé par la température.** Une température accrue choisit des tokens de plus faible vraisemblance ; le saboteur choisit des tokens plausibles (E le dit elle-même).
   - Tout détecteur sensible à la vraisemblance, à commencer par la ligne de base KL d'E, sépare ces deux bras par construction, sans rien lire de la valeur.
   - Le contrôle n'est pas apparié sur le mécanisme.
3. **E3 : patching indéterminé ou nul par construction.**
   - Si le saboteur est le jumeau plus une consigne, et que le « même préfixe » inclut la consigne, les activations sont identiques et le patching ne fait rien. Si le préfixe l'exclut, le patching change aussi ce que le modèle voit. E ne fixe pas lequel.
   - Le contrôle « patching entre deux exécutions honnêtes, |ΔS| < 3 % » est satisfait trivialement : il n'y a pas de sabotage à réduire, donc effet plancher. Il ne contrôle rien.
4. **Ligne de base KL forcée par le jumeau.** Elle détecte « agent ≠ jumeau », pas le sabotage. Elle est positive par construction dès qu'une consigne ou un LoRA distingue les deux. Sans variante honnête distincte du jumeau, elle a une puissance artificielle, et toutes les comparaisons « battre la KL » en héritent.
5. **Piste 1, conformal et CUSUM.**
   - La garantie conformale porte sur un score échangeable avec la calibration. Une CUSUM est une statistique de chemin : calibrer les quantiles par pas ne contrôle pas le taux d'alerte par trajectoire.
   - Calibrer sur le jumeau puis tester sur l'agent rompt l'échangeabilité sous H₀ dès que l'agent honnête diffère du jumeau.
6. **Piste 2.** Un détecteur de découplage appris sur l'honnête alerte sur tout décalage de distribution. Sa « vérification indépendante » sur un domaine absent de la calibration gonflera donc les fausses alertes par construction.
7. **Piste 4.** Un attaquant entraîné contre l'**union** des M sous-espaces neutralise la clé secrète. E4 teste un masque unique, pas la clé : la piste n'a pas de duel propre.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E1, atténuation.** Avec 32 rollouts, l'écart-type d'une valeur est d'environ 0,088, celui d'une TD d'environ 0,125.
  - Si l'écart-type vrai de δ dans la tranche vaut 0,1, la fiabilité est de 0,39 et ρ_obs ≈ 0,62·ρ_vrai. Le seuil 0,20 exige ρ_vrai ≥ 0,32.
  - S'il vaut 0,05, la fiabilité est de 0,14 et il faut ρ_vrai ≥ 0,54 (calcul de B, illustratif).
- **I4, « KS ≤ 0,03 ».** Avec 500 trajectoires par condition (illustratif d'E), deux échantillons tirés de la **même** loi donnent √250·D de loi de Kolmogorov. P(D ≤ 0,03) = K(0,47) ≈ 0,02 (calcul de B). Un jumeau parfaitement calibré échoue au critère environ 98 fois sur 100 : le critère n'est pas jugeable.
- **I5, « FPR empirique ∈ [0,005 ; 0,015] ».** Avec n = 500 et α = 0,01, le nombre de fausses alertes suit environ une loi de Poisson de moyenne 5. P(3 ≤ X ≤ 7) ≈ 0,74 : une distribution nulle exactement calibrée est rejetée environ une fois sur quatre (calcul de B).
- **Critères « TPR ≥ 0,60 à FPR = 0,01 » (E4, I1 à I3).** Ils reposent sur environ 5 événements honnêtes au-dessus du seuil. Même instabilité du seuil que pour A.
- **E2, CUSUM par trajectoire.** Elle perd sa puissance sous forte autocorrélation, et sa calibration n'est pas valide si elle est faite pas à pas (point a.5).

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Bras « consigne inerte »** : les quadruplets d'E n'en ont pas.
2. **Variante honnête distincte du jumeau** (autre graine d'affinage, ou consigne honnête différente), pour donner une distribution nulle à la KL et aux lectures différentielles.
3. **Échecs honnêtes à vraisemblance appariée** : trajectoires ratées du jumeau à température nominale, obtenues par rejet. Ils remplacent le jumeau chauffé.
4. **Test A/A sur trajectoires entières** pour la statistique séquentielle de la piste 1.

---

**Décompte réfutable.** 25 défauts de méthode, 16 conditions de perte de puissance ou de non-jugeabilité (dont 6 calculs de B sur chiffres illustratifs, vérifiables par recalcul), 15 contrôles négatifs. Un défaut commun à C, D et E : aucun saboteur dont l'intention n'est pas présente dans le contexte, ou pas de contrôle de consigne inerte. A seule le traite, avec son bras 2 et son bras LoRA.

FIN-DE-CELLULE