# Proposition A, tour III.3 : réponse aux critiques

**État des pièces.** Le bloc FAITS ne contient aucun fait porteur de statut (il reproduit la question ; empreinte non recalculée). Ma conception T1 et les critiques B, C, D, E sont présentes, terminées par FIN-DE-CELLULE, sans coupure visible. Les conceptions B à E ne me sont pas transmises : je ne réponds qu'aux sections « Sur la proposition A ». Quand je reprends un calcul qu'une critique oppose à une autre proposition, je le dis et je ne juge pas la proposition visée.

Rien ci-dessous n'est VÉRIFIÉ au sens d'une observation. Mes énoncés sont des HYPOTHÈSES, les chiffres sont illustratifs. Les identités que C, D et E portent au statut [VÉRIFIÉ] gardent le statut donné par leurs auteurs ; ce sont des calculs sous conditions, pas des mesures.

---

## (a) Sort de chaque critique

| # | Critique (sources) | Sort | Conséquence |
|---|---|---|---|
| 1 | Provenance des défauts-pièges non fixée ; fuite taxonomique pièges / familles du LoRA (B a1, c2 ; E a3) | Acceptée | Pièges produits par mutation mécanique et par un quatrième modèle hors matrice ; familles de pièges et de sabotage tirées d'une partition aléatoire pré-enregistrée, disjointes dans le test principal. |
| 2 | La sonde peut ne lire que la surprise du lecteur, maximale sur la diagonale (B a2, c1) | Transformée en test | Log-vraisemblance du lecteur par artefact, en covariable par item ; la décision du duel 1 porte sur l'interaction résiduelle (expérience 2). |
| 3 | Auto-familiarité stylistique confondue avec connaissance du défaut (C a3, c1 ; D a, c ; E a1, c2) | Transformée en test | Code canonisé (formatage AST, renommage) ; même mutation insérée dans du code honnête de chaque provenance ; ligne « rédacteur externe » (expériences 1 et 2). |
| 4 | LoRA partagé : co-entraînement confondu avec identité des poids ; sonde lisant la présence d'un adaptateur (B a3, c3-4 ; C a1, c2 ; E a1, c1) | Acceptée, précisée (P5) | Plan 2 × 2 base × co-adaptation, LoRA indépendants, LoRA leurre (expérience 3). |
| 5 | Sélection sur le verdict, descendant des activations (C a2 ; D a) | Acceptée | Analyse principale inconditionnelle : mêmes artefacts pour tous les lecteurs. Le sous-ensemble « approuvé » devient secondaire, avec le contraste avant et après sélection. |
| 6 | Covariable par lecteur colinéaire aux effets de colonne (E a2) | Acceptée | Covariable supprimée ; remplacée par des covariables par item. |
| 7 | Chaque ligne évaluée sur une sous-population de problèmes différente (E a1 ; B a5) | Acceptée, rejet partiel (P2) | Analyse restreinte aux problèmes où chaque rédacteur fournit au moins une erreur naturelle ; modèle à effet aléatoire par problème. |
| 8 | Interaction non nulle sous un modèle logistique additif (C b1 ; E b1) | Acceptée, écart de constante signalé (P4) | Décision sur l'échelle logit ; l'échelle des probabilités est rapportée à titre descriptif. |
| 9 | Peu de degrés de liberté, proximité entre paires de modèles, conjonction de signes sans puissance (B a5 ; E b1) | Acceptée | Conjonction abandonnée ; matrice complète publiée ; gradient de parenté ajouté ; généralité au-delà de trois modèles non revendiquée. |
| 10 | Transfert pièges → sabotage : plancher non jugeable, classe négative d'entraînement indéfinie (B b ; C b2, c3 ; D a ; E b2, c3) | Acceptée, transformée en tests | Deux sondes définies d'avance ; sonde « erreurs naturelles seules » (C) ; sonde oracle (E) réservée au diagnostic d'un nul. |
| 11 | Taux de détection à 1 % de fausses alertes non jugeable par cellule (C b2 ; E b2) | Acceptée, précisée (P3) | Métrique principale : AUROC et détection à 5 % ; le 1 % n'est rapporté qu'agrégé. |
| 12 | Duel 2 : 1/K n'est pas le nul ; l'écart diagonal est positif sans coordination ; jeu abstrait hors tâche ; décodage glouton (B a4, b, c5 ; C b3 ; D b ; E a1, b3) | Acceptée sur le fond, estimateur de B rejeté (P1) | Duel 2 réécrit : concordance renommée, variante in situ ajoutée (expérience 4). |
| 13 | Duel 3 : seuil calibré sur le test ; unité contribution / épisode ; budget et fausses alertes fixés ensemble ; marge de 2 points hors de portée ; non-infériorité triviale si peu de sabotages ; test de signe sans puissance ; le bilan ne prouve pas « le même signal » (B a6, b ; C a4 ; D a ; E a3, b4) | Acceptées | Expérience 5 réécrite ; la thèse du « même canal » sort des énoncés décisifs. |
| 14 | Probabilité de sabotage sachant une prise : fixée par l'expérimentateur sous tirages indépendants (C b4 ; D b ; E a2) | Acceptée | Mesure retirée ; remplacée par une courbe d'apprentissage après prise. |
| 15 | Rapport de vraisemblance sans référence honnête sous LoRA (E a2) | Acceptée | Deux régimes de menace séparés (section b). |
| 16 | Seuils de supériorité et d'équivalence distincts laissant une zone sans conclusion (D b) | Acceptée | Une seule marge d par duel : H_A si contraste ≥ d, H_B si < d ; intervalle recouvrant d = non concluant, rapporté comme tel. |
| 17 | Choix de couche, d'agrégation ou de référence d'après les résultats adverses (D a, c) | Acceptée | Tout est gelé sur une validation de pièges, hors familles de test. |
| 18 | Plafond du duel 0 si l'approbation est proche de 1 (B b) | Acceptée | Porte de jugeabilité. |
| 19 | Agrégation sans gain si scores corrélés ; rangs confondus (B b ; D b) | Acceptée | Corrélations honnête et sabotée rapportées ; résultats séparés pour 1 copie compromise sur 3 et 3 sur 3. |
| 20 | Gain des activations : l'égalité de deux scores ne prouve pas l'absence de gain (D b) | Acceptée | Gain mesuré par ajout de la sonde à un modèle texte + mécanique, sur données tenues à part. |
| 21 | Changer de tâche en semaine 2 sélectionne sur la variable dépendante (E a3) | Rejetée en partie (P6) | Porte restreinte, tâche de repli pré-enregistrée. |
| 22 | Permuter les partenaires dans la tâche ; SOLO avec exactement les historiques des copies (D c) | Acceptées | La première devient une vérification d'implémentation (P1) ; la seconde entre dans l'expérience 5. |

### Rejets et précisions

**P1. Estimateur de B pour le duel 2 : rejeté comme critère.** B demande de comparer la concordance observée au produit des marginales. C et D opposent à une autre proposition l'identité suivante, que je reprends : sans canal et à contexte fixé, la loi jointe est le produit des marginales. L'écart demandé a donc une espérance nulle par construction. Je le garde comme vérification d'implémentation : un écart non nul révélerait un canal accidentel (graine, cache, fuite de contexte). La part acceptée est que 1/K n'est pas le bon nul.

J'en tire aussi une conséquence de fond. Sans canal, un point focal n'est rien d'autre qu'une similarité de marginales : il n'existe pas d'excès au-dessus des marginales à chercher. La quantité qui compte pour l'adversaire est la concordance brute, et la question devient celle de son origine.

**P2. « Type d'erreur × lecteur » : rejet partiel.** B et D le présentent comme une confusion. Or la compatibilité entre un lecteur et les erreurs propres à son modèle est ce que le duel 0 cherche à estimer (angles morts corrélés). J'accepte en revanche trois confusions distinctes : la difficulté des problèmes (E), le style du code (D) et la proximité entre paires de modèles (B).

**P3. Effectif honnête par cellule.** C divise 2 000 cas par 9 cellules. Les mêmes artefacts étant lus par les trois lecteurs, l'effectif d'une cellule est celui de sa ligne, environ 670 (illustratif). La conclusion de C tient quand même : à 1 % de fausses alertes, la cellule n'est pas jugeable. De même, les 300 sabotages réussis demandés par B s'entendent par rédacteur, soit environ 18 000 tentatives au total pour 5 % de réussite (illustratif).

**P4. Constante du développement de C.** Je ne modifie pas le statut que C lui donne. En refaisant le calcul pour « moyenne diagonale moins moyenne hors diagonale », j'obtiens ½ σ''(μ) Σ α_i β_i, soit le double de la constante de C, et E en donne une troisième. La conclusion qualitative est la même dans les trois écritures ; la constante est à recalculer par l'arbitre.

**P5. Présence de l'adaptateur.** Quand le même lecteur lit les deux classes, l'adaptateur est constant entre classes : la sonde côté lecteur ne peut pas séparer par ce biais. La confusion est réelle côté rédacteur, et partout où les cas honnêtes viennent d'un modèle sans adaptateur. Le LoRA leurre est donc requis pour produire les cas honnêtes.

**P6. Porte de la semaine 2.** La porte porte sur le taux de défauts subtils produits par le rédacteur, mesuré avant toute lecture et toute sonde. Ce n'est la variable dépendante d'aucun duel. J'accepte la précaution : aucune donnée de lecteur n'est consultée avant la décision.

---

## (b) Expériences corrigées

### Deux régimes de menace, séparés à la suite de E a2

- **Régime contextuel.** Les poids sont sains, certains contextes sont compromis (consigne, injection). Des copies honnêtes existent, et le défenseur dispose d'une référence honnête de mêmes poids. Seul ce régime admet la variante « lecteur honnête ».
- **Régime dispositionnel.** La politique elle-même dégrade (organisme LoRA). Aucune copie n'est honnête et aucune référence de mêmes poids n'existe. La seule référence de vraisemblance est un modèle tiers.

Ma conception T1 mêlait les deux. « Lecteur honnête » face à un rédacteur LoRA désigne un modèle de même base, pas une copie.

### Dispositif commun corrigé

- **Artefacts.** Chaque artefact est lu par tous les lecteurs, en version brute et en version canonisée.
- **Quatrième modèle hors matrice.** Il produit des pièges, sert de vraisemblance tierce et fournit une ligne « rédacteur externe » sans diagonale, pour estimer les effets de lecteur hors identité.
- **Gradient de parenté du lecteur.** Copie exacte, même base avec LoRA bénin, autre modèle. Il répond en partie à la confusion identité / proximité.
- **Sondes gelées avant toute exécution adverse.**
  - S_déf : piège contre code correct (« défaut vu »).
  - S_int : défaut inséré sur consigne par le modèle externe contre erreur naturelle du même modèle externe (« défaut d'allure délibérée »).
  - Couche et agrégation sont choisies sur une validation de pièges.
- **Covariables par item.** Log-vraisemblance par jeton sous le lecteur, sous le modèle tiers, et longueur.
- **Décision.** Échelle logit, bootstrap par problème, une marge d par duel.
- **Portes de jugeabilité (illustratives).** Un duel hors porte est déclaré non concluant.
  - Approbation hors diagonale entre 20 % et 80 %.
  - Au moins 300 sabotages réussis par rédacteur.
  - AUROC de la sonde oracle d'au moins 0,65 dans une cellule au moins.

### Expérience 1 : duel 0 élargi, sans adversaire

**Stimuli.** Erreurs naturelles de chaque rédacteur ; la même mutation mécanique insérée dans le code honnête correct de chaque rédacteur ; code correct.

**Mesures.** Approbation textuelle, score S_déf, log-vraisemblance du lecteur.

**Duel 0a.**
- H_A : l'interaction diagonale sur les erreurs naturelles vaut au moins d (0,3 en logit, illustratif).
- H_B : elle est inférieure à d.
- H_A falsifie « sans adversaire, des copies valent une équipe quelconque ». H_B falsifie la transposition de la loi du mode commun à ce cadre.

**Duel 0b.**
- H_A : l'interaction sur les erreurs naturelles dépasse d'au moins d celle obtenue sur les mutations en code de même provenance.
- H_B : les deux sont égales à d près.
- H_A falsifie « tout effet d'identité est un effet de style ». H_B falsifie l'idée d'angles morts propres au défaut : l'identité se réduirait à la provenance du texte.

L'ancien contrôle « interaction nulle sur mutations » disparaît. Une mutation dans du code de provenance reconnaissable peut porter un effet de provenance : c'est ce que le duel 0b mesure.

**Contrôles.** Étiquettes permutées ; version canonisée ; ligne externe.

### Expérience 2 : duel 1 corrigé (régime contextuel, lecteur honnête)

La consigne de sabotage est dans le contexte du rédacteur seulement. La sonde côté lecteur ne peut donc pas la lire directement. Le test oppose sabotage et erreur naturelle appariée, par cellule.

**Décomposition emboîtée, pré-enregistrée.**
1. Δ_brut.
2. Δ après canonisation.
3. Δ_rés : interaction du gain de la sonde ajoutée à un modèle « vraisemblance du lecteur + longueur ».

**Duel.**
- H_A : Δ_rés ≥ d (équivalent logit de 0,05 d'AUROC, illustratif).
- H_B : Δ_rés < d.
- H_A falsifie « l'avantage du lecteur-copie se réduit à la surprise ou au style ». H_B falsifie le mécanisme de ma proposition T1 (connaissance partagée du défaut).

Le cas « Δ_brut ≥ d et Δ_rés < d » a une lecture précise : le gain existe, mais un calcul de vraisemblance sous une référence honnête le donne. B note, contre une autre proposition, que cette référence peut être rejouée pour un agent seul et pour chaque modèle d'une équipe hétérogène. Je m'en sers : dans ce cas, le gain n'est pas propre à la multiplicité des copies.

**Contrôles.**
- Couche d'entrée ; directions aléatoires.
- Contexte honnête contenant le vocabulaire du sabotage.
- Sonde entraînée sur erreurs naturelles seules : si elle donne le même Δ, l'instrument lit une direction générique de défaut.
- Sonde oracle : si elle est positive alors que les sondes gelées sont nulles, ce sont les pièges qui sont invalides, pas le signal.

### Expérience 3 : duel 1 bis (régime dispositionnel, lecteur complice)

**Plan 2 × 2, réduit à deux bases.**
- Facteur 1 : même base ou base différente.
- Facteur 2 : adaptateur du lecteur entraîné sur les défauts de l'adaptateur du rédacteur, ou entraîné indépendamment (graines et sous-familles disjointes).

Les cas honnêtes viennent d'un LoRA leurre de même rang. La mesure est la discordance entre S_déf (« défaut vu ») et le texte (« approuvé »).

**Duel.**
- H_A : l'effet « même base » vaut au moins d avec des adaptateurs indépendants.
- H_B : il passe sous d une fois la co-adaptation contrôlée.
- H_A falsifie l'explication par co-adaptation. H_B falsifie l'attribution aux poids de base.

**Coût.** Environ 8 adaptateurs (illustratif), plus que prévu en T1. Cette expérience passe en dernier ; si elle est coupée, aucune conclusion n'est livrée sur le régime dispositionnel.

### Expérience 4 : duel 2 corrigé (côté adversaire)

**4a. Concordance focale.** Lois de choix du rédacteur P_i et du lecteur Q_j estimées par décodage échantillonné, intitulés et ordre des options permutés. La concordance θ_ij = ⟨P_i, Q_j⟩ est calculée sur exécutions indépendantes.
- H_A : en cadrage de coordination, θ_diag − θ_hors ≥ d (10 points, illustratif).
- H_B : écart < d.
- La part déjà présente en cadrage « simple préférence » est rapportée à côté.
- Le résultat est nommé « avantage de concordance par similarité de préférences », pas « coordination ». Avec des rôles distincts, l'écart peut être négatif (E b3) ; l'issue reste donc ouverte.

**4b. In situ.** Lecteur complice par consigne, la consigne étant présente dans toutes les cellules. Il doit approuver « notre sabotage » et rejeter des pièges de même famille insérés dans du code de même provenance.
- Métrique : approbation(sabotage) − approbation(piège), interaction diagonale, en version brute et canonisée.
- H_A : interaction ≥ d. H_B : < d.
- H_A falsifie « la validation par pièges vaut autant face à des copies que face à des modèles différents ». H_B falsifie, à cette échelle, le gain d'auto-reconnaissance de l'adversaire.

**Analyse secondaire, non décisive.** Association par item, dans les cellules diagonales, entre la reconnaissance en 4b et le score de sonde. C'est la seule trace restante de la thèse du « même canal ».

### Expérience 5 : duel 3 corrigé

- **Unité et budget.** L'unité est l'épisode. Le budget b est identique en SOLO, COPIES et MIXTE. L'allocation prend les b meilleurs scores, sans contrainte sur les fausses alertes, qui sont rapportées.
- **Calibration.** Tout est calibré sur un lot honnête tenu à part.
- **Flux.** Réserves d'épisodes adverses et honnêtes produites séparément, puis flux rééchantillonnés à prévalence π fixée. Le plafond b/π est affiché.
- **Grandeurs rapportées.** Réussite du sabotage avant audit s_g, taux de prise parmi les dégradés d_g(b), risque résiduel r_g = s_g(1 − d_g).
- **Duel.**
  - H_A : r_COPIES − r_MIXTE ≤ d.
  - H_B : > d.
  - Marge d = 8 points pour environ 500 épisodes dégradés par composition (illustratif, d'après la formule de B). Un écart plus fin n'est pas résolu en deux mois.
  - Porte : s_g au-dessus d'un plancher dans les deux compositions.
  - H_A falsifie la règle « préférer l'hétérogène » quand les activations sont disponibles. H_B falsifie ma prédiction P3.
- **Contrôles.** Texte seul ; SOLO recevant exactement les historiques des copies.

### Instrument 3 corrigé : valeur d'une prise

La probabilité conditionnelle est remplacée par le gain de détection sur tâches non auditées après ajout de k prises réelles (k = 1, 5, 20, illustratif) à l'entraînement de la sonde. Le nombre de prises par modèle est égalisé entre compositions.
- H_A : le transfert entre rôles est plus fort en COPIES d'au moins d.
- H_B : écart < d.
- H_B affaiblit S1 (politique unique).

### Calendrier et renoncements

| Semaines | Travail |
|---|---|
| S1–3 | Expérience 1, portes, pré-enregistrement |
| S4–5 | Expérience 2 |
| S6 | Expérience 4 |
| S7 | Expérience 5 |
| S8 | Expérience 3 réduite, ou rédaction |

Le test d'effort adaptatif est abandonné faute de temps. Toutes les conclusions valent donc pour un adversaire non adaptatif.

---

## (c) Réponse à l'arbitre

**(1) Question.** À code canonisé et à vraisemblance contrôlée, les activations d'un lecteur-copie séparent-elles un sabotage d'une erreur honnête mieux que celles d'un lecteur d'un autre modèle, et, à budget d'audit égal par épisode, le risque résiduel d'une équipe de copies ainsi instrumentée reste-t-il dans la marge de celui d'une équipe hétérogène ?

**(2) Réponse attendue** [HYPOTHÈSE, révisée après critiques]. Un avantage diagonal brut est probable. Je m'attends à ce que la surprise et le style l'expliquent en grande partie. Mes probabilités subjectives (illustratives) :

| Issue | Probabilité |
|---|---|
| Δ_brut ≥ d | environ 55 % |
| Δ_rés ≥ d | environ 20 à 25 % |
| Duel 0a en faveur de H_A | environ 50 % |
| Duel 4b en faveur de H_A | environ 30 % |

L'issue que je crois la plus probable réfute donc le mécanisme que j'avançais en T1. Ce que l'identité changerait alors se ramène à trois choses plus modestes :
- des angles morts honnêtes corrélés ;
- une sonde et une prise qui valent pour toutes les copies ;
- côté adversaire, une concordance obtenue par simple similarité de préférences.

**(3) Antériorité la plus proche** [RAPPORTÉ, de mémoire]. Greenblatt, Shlegeris, Sachan et Roger (2023), « AI Control: Improving Safety Despite Intentional Subversion ». Les autres références de ma pièce T1 gardent leur statut, « de mémoire, à vérifier » ; je n'en ajoute aucune.

**(4) Expérience.** La séquence 1 → 2 → 4 → 5 de la section (b), sur trois modèles ouverts de 7 à 9 milliards de paramètres plus un quatrième hors matrice.

**(5) Type.** Un phénomène, décomposé en trois mécanismes concurrents (surprise, provenance, connaissance du défaut), adossé à une loi connue ailleurs (mode commun). Ce n'est pas une garantie.

### Ce qui est établi

Aucun fait empirique : FAITS n'en contient pas et rien n'a été exécuté. Seules tiennent des identités de calcul, portées [VÉRIFIÉ] par leurs auteurs, que j'ai reprises parce qu'elles contraignent le plan :
- sans canal, la concordance est le produit scalaire des marginales, et l'écart diagonal est positif dès que les modèles ont des préférences différentes (C, D) ;
- budget = π × détection + (1 − π) × fausses alertes, d'où un rappel borné par b/π (C, E) ;
- une covariable par lecteur est absorbée par les effets de colonne (E) ;
- sous tirages indépendants, une prise n'informe pas sur la tâche suivante (C, D, E).

### Ce qui ne l'est pas

- Qu'un signal d'identité existe dans les activations au-delà du texte et de la vraisemblance.
- Qu'un modèle de 8 milliards produise des défauts subtils en nombre suffisant.
- Que des pièges entraînent une sonde qui transfère au sabotage réel.
- Que l'adversaire et le défenseur exploitent le même signal.
- La nouveauté, que je tiens pour fausse tant que les sections de méthode des travaux cités n'ont pas été lues en cherchant les trois éléments réunis : matrice rédacteur × lecteur, sondes sur activations, appariement à des erreurs honnêtes.

### Expérience à faire en premier

L'expérience 1, pour quatre raisons :
- elle ne demande ni adversaire ni adaptateur ;
- elle fixe les lignes de base que tous les autres duels soustraient ;
- elle ouvre ou ferme les portes de jugeabilité ;
- ses deux duels falsifient quelque chose dans chaque issue.

Si le duel 0b donne H_B, l'effet d'identité se réduit à la provenance du texte, et je le saurai avant d'avoir dépensé le budget adverse.

### Issues qui rendraient la question sans intérêt

1. Δ_rés < d, duels 0a et 4b en faveur de H_B : « copies » n'est pas la variable. Ce qui compte est l'accès à une référence honnête, disponible aussi pour un agent seul.
2. Les vérifications mécaniques égalent les activations dans les trois compositions.
3. Seul le duel 0a est positif : la question se ramène à une loi de fiabilité connue, sans composante adverse propre.
4. Portes fermées : l'expérience est non concluante et rapportée comme telle.

FIN-DE-CELLULE