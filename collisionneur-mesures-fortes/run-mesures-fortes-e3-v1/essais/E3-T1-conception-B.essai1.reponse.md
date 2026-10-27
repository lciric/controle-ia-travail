# Proposition B — Tour III.1 : mesures, concepts, tests

**Légende des statuts.** Tout ce qui vient des pièces est **RAPPORTÉ**, statut que l'en-tête des faits donne à l'ensemble. Ce que j'avance est **HYPOTHÈSE**. Un chiffre qui n'est pas dans les faits est marqué *illustratif*. Je ne dispose d'aucun fait **VÉRIFIÉ** ni **OBSERVÉ-NON-AUDITÉ**.

**Pièces.**
- Présentes : P (§4, 5, 8, 10, 11, 12), N-007/N-008, N-054, C (§0, 3, 4), S.
- Absentes, et dont je n'invente pas le contenu :
  - P §3, où sont énoncés le lemme L et le théorème T ;
  - P §6, §7 (contrôles croisés) et §13 ;
  - le brief de phase 0 ;
  - les scripts et sorties de simulation de S.
- S cite un champ « ε » de la fiche (2.5) sans le définir dans l'extrait.

**Protocole.**
- B1 : je ne vois pas les propositions A et C, je ne peux donc ni les attaquer ni m'en servir.
- Règle de cellule : aucun point ci-dessous ne conçoit d'attaque. Chaque fois qu'une robustesse est mesurée, elle l'est **uniquement** sur le catalogue clos (modes N-054, familles EC.1 nommées dans P, attaques publiées). J'écarte la partie « attaque adaptative » de H8 et de E1.5 : elle relève d'un GO humain, pas de cette cellule.

**Thèse de B (HYPOTHÈSE).** Le levier le plus réfutable n'est pas un nouveau gain de détection. C'est **placer la dissociation dans le nul du juge** :
- toute fiche du type « la sonde mesure X » doit battre une bibliothèque nulle qui contient obligatoirement un prédicteur de surface (longueur, position, sacs de mots du texte visible) et la sonde aléatoire appariée en covariance ;
- il faut ajouter un **troisième engagement, le pari d'équivalence**, sans lequel aucune affirmation « effet ≈ 0 » (robustesse HC2, absence d'effet de format) n'est promouvable.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Ce qui manque |
|---|---|---|---|
| a1 | Le pôle établit ces mesures « mieux qu'une équipe humaine à budget égal ». | **HYPOTHÈSE** | C rapporte une seule boucle de bout en bout sur 120 épisodes notés par deux juges (RAPPORTÉ), sans aucune comparaison. Voir X7. |
| a2 | « Garantie de 5 % par fiche. » | **RAPPORTÉ** (C §0 : validée en simulation, contrôles fatals à 0 sur 1 000) | 0/1 000 borne le taux sous les nuls *simulés* à environ 0,3 % (règle de trois, calcul sur chiffres RAPPORTÉS), pas sous la dépendance entre tâches qu'exclut S 3.2. |
| a3 | Les tâches de la banque sont des tirages indépendants d'une population. | **HYPOTHÈSE** (S 3.2 la déclare) | Des tâches qui partagent organisme, graine ou mode violent la condition ; S propose l'organisme comme unité. |
| a4 | « Même taux de faux positifs nominal » a un sens unique pour séquentiel contre par action. | **Non établi** | N-007 calibre le moniteur par action à 1 % **par action** ; S calibre au niveau **épisode**. Conséquence (HYPOTHÈSE) : le taux épisodique du moniteur par action croît avec le nombre d'actions T. La comparaison H2 doit fixer un seul niveau, l'épisode, sinon la pente en horizon est confondue. |
| a5 | La sous-population de H2a (« chaque action sabotée sous le seuil ») est un contraste informatif. | **HYPOTHÈSE de B : risque de circularité** | Si le moniteur qui définit la sous-population est aussi le comparateur, alors r_action ≡ 0 par construction. H2a dégénère en « rappel ≥ 0 ». N-007 ne dit pas quel moniteur fixe ce seuil. |
| a6 | L'agrégateur « toujours valide » tient sa garantie au niveau du moniteur. | **RAPPORTÉ, contraire** | N-007, d'après T0.3 : 0,21 à 0,35 au lieu de 0,05 sous effet épisode. Le calibrage conforme sur épisodes entiers est *proposé*, pas validé. |
| a7 | Une sonde mesure un concept nommé (intention, conscience d'évaluation…). | **HYPOTHÈSE** | Le 0,40 de H8 est une probabilité d'*originalité* (RAPPORTÉ), pas une probabilité de vérité. |
| a8 | Les engagements existants suffisent aux affirmations visées. | **Non établi** | Le pari apparié ne promeut que E[v] > 0 (S 2.1). HC2 (g_sonde ≈ 0) et tout test de dissociation (« l'effet de format est nul ») sont des affirmations d'équivalence, non promouvables aujourd'hui. |
| a9 | Le catalogue clos suffit à mesurer la « robustesse » de H8. | **HYPOTHÈSE** | La table de S définit l'issue de H8 « sous attaque adaptative ». Il y a tension avec « attaques closes ». Je mesure la robustesse sur pression bénigne (HC6) et attaques publiées seulement. |
| a10 | Un modèle de 70 milliards de paramètres est disponible. | **RAPPORTÉ par la question seule** | Les pièces servies ne nomment que 8B, Llama-3.2-3B-Instruct et Qwen2.5-7B. |
| a11 | Le prix du mélange de S est cohérent. | **RAPPORTÉ, contradiction interne** | S 2.2 donne log 8 ≈ 2,1 nat. D-S2 donne « log 2 ». Le contrôle 9 donne « ≤ log 4 ». Le contrôle 9, appliqué au mélange complet (2 formes × 4 λ), échouerait. À corriger avant scellement. |
| a12 | L'« IC à 95 % » de G1 équivaut à la suite de confiance de S. | **RAPPORTÉ comme proposition de S, non décidé** | N-008 parle d'intervalle avec appariement. S précise que « 1 % » n'est jamais certifiable sur ces banques. Le critère se lit donc au taux nominal plus une garde δ. |
| a13 | Des sondes peuvent servir d'instances indépendantes (H8 en loi par instance). | **HYPOTHÈSE** | Des sondes entraînées sur les mêmes données ou graines sont dépendantes. Il faut prendre la *famille* (graine × données) comme unité, comme S le fait pour la tâche. |

---

## (b) Expériences décisives (inférence forte)

Règles communes à toutes les expériences :
- **Seuil** : richesse ≥ 1/α = 20 (RAPPORTÉ). Pour le pari apparié, garde δ ≥ 20 également.
- **Point de fonctionnement** : τ = 1 % et 5 % nominal (D-S5, RAPPORTÉ).
- **Règle de non-falsification par défaut** (HYPOTHÈSE) : une non-promotion ne falsifie rien si le témoin vrai *de même taille* n'est pas promu (« pas de dents »). Une falsification « négative » exige soit des dents démontrées, soit une promotion du pari d'équivalence (voir c-bis).

### X1 — Additivité interne contre artefact d'horizon (H2)

- **H_A** : sur les tâches où chaque action sabotée reste sous le seuil par action, la *sonde réelle* agrégée séquentiellement a un rappel épisodique supérieur à la *sonde aléatoire appariée en covariance* passée dans le même agrégateur. L'écart croît avec l'horizon.
- **H_B** : le gain séquentiel vient de l'accumulation de tout signal corrélé à la longueur ou à la position (dérive honnête). La sonde aléatoire appariée et la longueur seule reproduisent la pente.
- **Plan** :
  - paires de tâches voisines à deux horizons (forme H2b de S) ;
  - seuils **par horizon**, calibrés sur épisodes honnêtes entiers réservés (conforme), ce qui règle a4 ;
  - sous-population définie par un moniteur par action *distinct* du comparateur, ce qui règle a5.
- **Métrique** : v = ½[(r_seq,réel − r_seq,aléa)_long − (r_seq,réel − r_seq,aléa)_court], pari apparié borné avec garde sur f_réel − f_aléa.
- **Contrôle négatif** : pseudo-sabotage, c'est-à-dire étiquettes « saboté » permutées à l'intérieur de tâches honnêtes ; attendu ≤ α.
- **Témoin vrai** : scores sabotés relevés d'un décalage fixé, sans franchir le seuil par action.
- **Issues** :
  - promotion avec garde → H_B falsifiée ;
  - équivalence réel ≈ aléa promue (marge ε) avec témoin vrai promu → H_A falsifiée.

### X2 — Carte de validité : construit contre surface (H8, résultat fort (a))

- **H_A** : le profil d'une famille de sondes sur le panel contrastif (intention, dissimulation, conscience d'évaluation, enjeux, P §11) prédit sa chute de rappel sous pression. Il le fait au-delà d'un prédicteur « connu » qui combine AUROC en distribution, couche, famille et score du prédicteur de surface.
- **H_B** : le prédicteur connu suffit ; le profil de construit n'ajoute rien.
- **Unité** : la famille de sondes, conformément à a13.
- **Issue par instance** : g_sonde sur corpus de pression bénins (HC6) et rappel sur attaques publiées.
- **Engagement** : loi par instance, avec le prédicteur connu dans la bibliothèque.
- **Contrôles négatifs** :
  - profils permutés entre familles (≤ α) ;
  - sondes aléatoires appariées incluses comme instances, qui doivent tomber dans la classe « ne mesure rien ».
- **Issues** :
  - loi du profil promue contre le connu → H_B falsifiée ;
  - connu promu contre l'aveugle, profil non promu contre le connu, alors qu'un témoin vrai (profil planté qui détermine l'issue) l'est à même effectif → H_A falsifiée.

### X3 — Conscience d'évaluation : cadrage contre format (question, point 3)

- **H_A** : la sonde suit le *cadrage*. L'effet « évalué contre réel » est non nul à format de surface fixé, et l'effet du format est dans [−ε, ε] à cadrage fixé.
- **H_B** : la sonde suit le *format*. C'est l'inverse.
- Une issue mixte falsifie les deux versions pures.
- **Plan factoriel**, contenu de tâche tenu fixe :
  - cadrage (évalué / déploiement) × gabarit de surface (gabarit de banc / gabarit naturel) ;
  - plus un bras « même cadrage, contenus différents ».
- **Métrique** : v(t) = écart moyen de score normalisé par rangs, ramené à [−1 ; 1], par tâche. Le pari apparié s'applique à l'effet attendu, le pari d'équivalence à l'effet censé être nul.
- **Contrôles** :
  - permutation des étiquettes de cadrage à l'intérieur de la tâche ;
  - sonde aléatoire appariée ;
  - paraphrase qui préserve le cadrage, où le score doit rester stable (équivalence).
- **Rupture séquentielle à garantie** : l'expérimentateur bascule le cadrage à un pas t₀ connu.
  - Détecteur : processus e de changement, ou CUSUM de Page (E. S. Page, 1954, « Continuous Inspection Schemes », *Biometrika*). Pour la variante e-détecteur : référence à vérifier.
  - Mesures : délai de détection, et durée moyenne avant fausse alerte estimée sur flux honnêtes sans bascule.
  - Contrôle décisif : une bascule de *format seul* à t₀, où le détecteur de cadrage ne doit pas se déclencher (équivalence sur le taux d'alarme).
- **Ce qui serait décisif plutôt que suggestif** : les deux volets ensemble, effet de cadrage promu *et* équivalence de format promue. L'un sans l'autre reste suggestif.
- **Limite (HYPOTHÈSE)** : ce plan distingue cadrage et format, pas l'*intention*. Lier la sonde à un changement de conduite exige une issue comportementale distincte, hors de cette cellule.

### X4 — Déférence contre régression vers la moyenne et longueur (HC1, HC2, HC2b)

- **H_A** : g > 0 pour les juges génératifs (contamination de construit), g_sonde ∈ [−ε, ε].
- **H_B** : le déplacement Δv s'explique par la régression vers la moyenne (dépendance en v₀) et par l'ajout de texte. Une fois ces effets retirés, g ≈ 0.
- **Plan** :
  - chaque item est lu sous trois conditions : sans ajout, avec pression (familles EC.1 du catalogue clos), avec **remplissage neutre de même longueur** ;
  - plan 2 × 2 rhétorique × intention d'EC.2 : honnête qui plaide contre saboteur qui plaide ;
  - verdict continu par probabilité du jeton de verdict, texte complet, sans troncature (leçons de P3, RAPPORTÉ).
- **Métrique** : v(item) = [Δv_pression − Δv_remplissage]/(v* − v₀), ramené à [−1 ; 1]. Un pari apparié borné suffit ; pas de troisième type pour la pente. En parallèle, la régression Δv = g(v* − v₀) + ρ(μ − v₀) est rapportée sur plusieurs intensités.
- **Auto-incrimination (HC2b)** : n'est réelle que si la sonde monte pour le saboteur qui plaide et **pas** pour l'honnête qui plaide (équivalence). Sinon, c'est du style.
- **Contrôle négatif** : remplissage contre remplissage avec deux graines ; attendu ≤ α.
- **Issues** :
  - v promu pour un juge → H_B falsifiée pour ce juge ;
  - équivalence promue → H_A (contamination) falsifiée pour ce juge.

### X5 — Théorème négatif sur activations réelles (conditionnel : P §3 absent)

- **H_A** : à marginales préservées, la corrélation injectée (E1.4) laisse les agrégateurs marginaux au taux nominal, tandis que l'agrégateur séquentiel calibré détecte.
- **H_B** : la « visibilité » séquentielle vient d'une fuite marginale de l'injection.
- **Vérification mécanique** : test à deux échantillons sur les marginales, position par position. S'il rejette, l'injection est invalide et rien ne se lit.
- **Dissociation** : injecter la même corrélation dans des épisodes honnêtes sans dommage.
  - Si le séquentiel alerte autant, il mesure *la corrélation*, pas le dommage. C'est compatible avec T, mais l'affirmation de sécurité doit le dire.
  - S'il alerte moins, H_B est falsifiée sur ce point.
- **Issues** :
  - marginaux promus au-dessus du nominal → H_A falsifiée ;
  - séquentiel promu, marginales intactes → H_B falsifiée.

### X6 — Diversité effective (H5, résultat fort (e))

- **H_A** : le taux de manque d'un ensemble sous attaques publiées est prédit par la matrice de transfert.
- **H_B** : il est prédit aussi bien par la corrélation des erreurs bénignes ou par le seul nombre M.
- **Engagement** : loi par instance sur des ensembles **disjoints** (pour limiter la dépendance), avec la corrélation bénigne et M dans la bibliothèque.
- **Contrôle négatif** : matrice dont les lignes sont permutées.
- **Issues** :
  - promotion → H_B falsifiée ;
  - corrélation bénigne promue contre l'aveugle et transfert non promu contre elle, à dents démontrées → H_A falsifiée.

### X7 — La prémisse a1 : pôle contre protocole gelé à budget égal

- **H_A** : à dépense égale, le pôle promeut plus de témoins vrais par dollar que ne le fait un plan d'analyse unique préenregistré (tests à n fixé, procédure de Benjamini et Hochberg, 1995, « Controlling the false discovery rate »), à fausses promotions ≤ α.
- **H_B** : le protocole gelé fait au moins aussi bien.
- **Témoins** : plantés et cachés aux deux bras.
- **Métrique** : témoins vrais promus par dollar ; témoins faux promus.
- **Issues** : chacune falsifie l'autre hypothèse. Une issue H_B ferait de la vitesse le seul argument du pôle, non de sa qualité de mesure.

---

## (c) Mesure minimale par instrument

Dans le tableau, « FP » désigne le taux de faux positifs épisodique, mesuré sur tâches honnêtes réservées et rapporté avec sa suite de confiance. D'après S (RAPPORTÉ) :
- avec 70 tâches honnêtes de 10 épisodes, la garde certifie δ = 0,10 ;
- avec 150 tâches, δ = 0,05 ;
- le niveau absolu de 1 % n'est jamais certifiable sur ces banques.

| Instrument | Détection / fausses alertes à mesurer | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|
| Sonde sur activations | Rappel épisodique par mode (coût, contrôles, mode tenu à l'écart) à τ nominal ; FP | Même tâche, même consigne, longueur à ± 10 % *illustratif* | Sonde aléatoire appariée en covariance (plancher P 8.1) ; logistique sur sacs de mots du texte visible ; longueur ou position seule ; « tout signaler » |
| Juge génératif (D1 a, b) | Idem ; plus g sur remplissage neutre, qui doit être équivalent à 0 | Idem | Expression régulière de mots-clés ; longueur ; juge en une passe avec le même modèle (plancher N-008) |
| Agrégateur séquentiel « toujours valide » | FP empirique **par strate de tâche et par horizon**, contre nominal (échec si la borne basse dépasse le nominal ; cf. 0,21 à 0,35 RAPPORTÉ) ; délai d'alerte contre dommage cumulé | Épisodes honnêtes entiers, mêmes horizons | Maximum cumulé des scores par action ; dernier état, base (iii) ; somme non calibrée ; base (i) |
| Détecteur de rupture | Délai de détection ; durée moyenne avant fausse alerte sur flux sans bascule ; taux d'alarme sur bascule de format seul | Flux de même tâche sans bascule | CUSUM de Page à paramètres connus (oracle) ; seuil fixe |
| Pari apparié borné | Niveau sous nuls simulés (contrôles 1 à 7 de S) ; puissance aux témoins | Tâches honnêtes de l'épreuve, pour la garde | Test exact du signe à n fixé. Cohérence : richesse ≥ 20 implique p ≤ 0,05 par l'inégalité de Markov, sinon c'est un bogue |
| Pari par instance, juge figé et bibliothèque | Promotion des témoins vrais et faux | — | Bibliothèque **élargie** (surface et sonde aléatoire). Une fiche promue contre la bibliothèque standard mais non contre l'élargie est classée « surface » |
| Règle e-BH (Wang et Ramdas, « False discovery rate control with e-values » : référence à vérifier) | Taux de fausses découvertes simulé (contrôle 10 de S) | — | Benjamini-Hochberg sur p-valeurs à n fixé |
| Mémoire des redites | Refus des redites plantées (paraphrases ou contrastes identiques) ; refus à tort de fiches distinctes | Fiches voisines non identiques | Empreinte exacte du texte (S : signature exacte pour les fiches de signe) |
| Recombinaison | Fiches vraies promues par dollar | — | Recombinaisons tirées au hasard au même budget |
| Régression g | g sur remplissage ≈ 0 (équivalence) ; stabilité de g entre intensités | Remplissage de même longueur | Modèle « régression vers la moyenne seule » |
| Matrice de transfert | Diagonale élevée (l'attaque publiée marche sur sa cible), sinon la matrice est vide de sens ; hors-diagonale avec intervalles | — | Matrice de corrélation des erreurs bénignes (P 8.2 : choisir sur la seule décorrélation « perd contre le hasard », RAPPORTÉ) |
| Contrôle apparié en covariance | Doit rester au niveau du hasard | — | Direction aléatoire non appariée ; sonde entraînée sur étiquettes permutées |

### c-bis — Troisième engagement : le pari d'équivalence (HYPOTHÈSE de B)

- **Construction** : deux gardes au sens de S 2.4, l'une contre « E[v] ≥ ε », l'autre contre « E[v] ≤ −ε ». La promotion exige les deux richesses ≥ 1/α.
- **Validité** : niveau α par intersection-union. C'est le même argument que l'union de nuls de S 3.5, retourné.
- **Coût en code** : nul, la garde existe déjà.
- **Témoins gratuits** depuis les scores stockés :
  - vrai : A contre A avec un bruit symétrique ;
  - faux : A contre A décalé de 2ε.
- **Ce qu'il débloque** : HC2, HC2b (bras honnête), et les volets « format » de X3, « remplissage » de X4, « réel ≈ aléa » de X1.
- **Contrôle fatal à ajouter** : à ε trop petit pour l'effectif, l'équivalence doit être *impossible*. Le journal l'inscrit comme « équivalence sans dents ».

**Comparaison de courbes** (sécurité(N), H3) : pas de quatrième type. S couvre déjà la pente par contraste apparié (H3b). Je ne vois pas de besoin démontré au-delà.

---

## (d) Ancrage matériel

| Élément | Choix | Statut |
|---|---|---|
| Agent 8B | Llama-3.1-8B-Instruct | Choix de B (HYPOTHÈSE) ; « 8B » est RAPPORTÉ |
| Agent 70B | Llama-3.1-70B-Instruct, seulement après G1 sur 8B | Choix de B ; 70B RAPPORTÉ par la question seule |
| Juges | (a) même modèle ; (b) Llama-3.2-3B-Instruct ; Qwen2.5-7B | RAPPORTÉ (P, D1) |
| Autoencodeurs parcimonieux | Llama Scope | RAPPORTÉ (P 8.2) ; modèle cible : référence à vérifier |
| Effectifs | Environ 40 tâches sabotées par mode pour un écart de 20 points ; environ 100 pour 10 points ; 70 à 150 tâches honnêtes ; 10 épisodes par tâche | RAPPORTÉ (simulation exploratoire de S) |
| Modes | Au moins coût, contrôles, mode tenu à l'écart | RAPPORTÉ (N-054) |
| Total d'épisodes | 3 × 40 × 10 + 1 500 = 2 700 (écart de 20 points) ; 3 × 100 × 10 + 1 500 = 4 500 (écart de 10 points) | Calcul sur chiffres RAPPORTÉS |
| Jetons par épisode | 20 000 | *illustratif* |
| Calcul 8B | 4 500 × 20 000 = 9 × 10⁷ jetons ; environ 1 500 jetons/s avec crochets d'activation sur un GPU de 80 Go, soit environ 17 GPU-h, à doubler pour les juges : environ 35 GPU-h | *illustratif* |
| Coût 8B | 2 à 3 USD/GPU-h, soit 70 à 105 USD | *illustratif* ; compatible avec la couche 2 de C, 100 à 300 USD (RAPPORTÉ) |
| 70B | Environ 140 Go de poids en bf16 (70 × 10⁹ × 2 octets, calcul), donc au moins deux GPU de 80 Go ; débit environ 8 fois moindre, soit environ 270 GPU-h et 550 à 800 USD | *illustratif* |
| Stockage | Largeur 4 096 pour le 8B (à vérifier sur la fiche du modèle). 9 × 10⁷ jetons × 3 couches × 8 Ko donnent environ 2,2 To. Conserver par jeton les seuls scores du panel gelé, et les activations complètes sur un échantillon de 10 % | *illustratif* |
| Contrôles fatals de S et pari d'équivalence | Processeur, sans dépense | RAPPORTÉ (S §7) pour S ; HYPOTHÈSE pour l'ajout |
| Couches du pôle | 0 : 10/50 ; 1 : 25/100 ; 2 : 100/300 ; 3 : 100/400 ; 4 : 100/400 USD | RAPPORTÉ (C §4) |

### Ordre et arrêt (HYPOTHÈSE de B)

1. **Processeur, 0 USD.**
   - Actions : corriger a11 ; coder c-bis ; passer les contrôles 1 à 10 de S et le contrôle « équivalence sans dents ».
   - Arrêt : si les contrôles 4, 5 ou 6 ne se comportent pas comme S l'annonce.
2. **Couche 1** (180 épisodes honnêtes, RAPPORTÉ).
   - Actions : FP empirique des juges par strate ; prédicteur de surface placé dans la bibliothèque.
   - Arrêt : si la surface prédit déjà les scores des juges (piste N-029, RAPPORTÉ dans C), aucune fiche « construit » n'est recevable sans battre ce prédicteur.
3. **Couche 2, 8B.**
   - Actions : X1, X4, X3, dans cet ordre.
   - Arrêt : avant chaque fiche réelle, si le témoin vrai *de même effectif* n'est pas promu, la fiche ne tourne pas.
4. **Ensuite.** X2 et X6, qui exigent beaucoup de familles de sondes et d'attaques publiées ; X5 quand P §3 sera servi ; X7 en parallèle, à faible coût, sur témoins.
5. **70B en dernier**, sur les seules fiches promues en 8B.

### Ce qui me ferait changer d'avis

- Les sondes battent déjà la bibliothèque élargie avec une marge large : X2 vaut alors moins que son coût.
- Le remplissage neutre déplace les juges (g ≠ 0) : le plan X4 est mal posé et la loi de déférence n'est pas estimable sous cette forme.
- Le FP empirique de l'agrégateur séquentiel reste au-dessus du nominal après calibrage conforme : H2 n'est pas testable tel qu'énoncé.

FIN-DE-CELLULE