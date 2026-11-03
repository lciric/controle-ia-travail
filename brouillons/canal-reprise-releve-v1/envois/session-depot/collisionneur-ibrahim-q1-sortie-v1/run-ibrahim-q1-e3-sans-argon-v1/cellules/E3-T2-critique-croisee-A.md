# Tour III.2 — Proposition A : critique de méthode des propositions B, D, E

**Pièce C** : absente (jamais lancée) ; je n'en critique rien et n'en reconstitue rien.

**Conventions.** Les faits tirés des pièces sont RAPPORTÉ (papiers) ou OBSERVÉ-NON-AUDITÉ (dépôts publics de Lazar). Tout ce qui suit sur les conceptions B, D, E est de statut HYPOTHÈSE (analyse de méthode). Tout chiffre que je produis est « calcul » (dérivé d'un chiffre de pièce) ou « illustratif ». Notation commune : Y = score du juge ; C_t = écart persona − base à l'étape t ; R = Ĉ_après / Ĉ_avant ; (s, p) = sensibilité et spécificité d'un juge binaire ; ρ = taux de refus d'un bras.

Trois défauts sont partagés par B, D et E ; je les détaille une fois (en B) et j'y renvoie ensuite, sans fusionner les propositions :

- **(Σ1) Persistance vraie par construction.** Un apprentissage par renforcement à récompense vérifiable (RLVR) sur mathématiques, avec adaptation de rang faible et, selon l'usage, une pénalité KL vers la politique de référence, touche un sous-espace de paramètres et une distribution de prompts disjoints de la persona. Si la référence de la pénalité KL est le point de contrôle à persona lui-même, l'objectif *pénalise* l'effacement de la persona. H_A (« la persona tient ») est alors le résultat par défaut de la méthode, pas une découverte. Aucune des trois propositions ne déclare le coefficient KL, le rang de l'adaptateur ni un bras où ces contraintes sont levées.
- **(Σ2) Ratio de rétention.** R est un rapport de deux estimateurs bruités ; ses propriétés dépendent du dénominateur (voir B-(b)).
- **(Σ3) Dérive de juge confondue avec « avant/après ».** Les pièces indiquent que l'alias du juge de R6 n'est pas figé (OBSERVÉ-NON-AUDITÉ, piece-sycophancie §1, Limits). Si les sorties « avant » sont notées à t₁ et les sorties « après » à t₂, la version du juge est confondue avec le traitement.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **L'issue attendue tombe dans la zone déclarée non jugeable.** B attend r ≈ 0,6 (supposé) pour E1, mais définit H_A par r ≥ 0,7 et H_B par r ≤ 0,3, avec une zone « non tranché » entre les deux. Le résultat jugé le plus probable par l'auteur ne falsifie rien. Un duel dont l'issue modale est l'abstention viole B4 en pratique.

2. **(Σ1)** s'applique pleinement ; de plus le bras « ajustement supervisé neutre, même nombre d'étapes » apparie le *nombre d'étapes*, pas l'ampleur du déplacement de la politique. Si KL(π_RL ‖ π₀) ≠ KL(π_SFT ‖ π₀) sur des prompts tenus à l'écart, la comparaison confond type et quantité de post-entraînement.

3. **Chevauchement construit entre persona et sycophancie sociale.** *Loving* est défini par « valider les sentiments » (RAPPORTÉ, piece-ibrahim §2, tableau 1) ; les réponses préférées dans PRISM/UltraFeedback/LMSys contiennent plus de validation émotionnelle (RAPPORTÉ, §1.6). Un classifieur de persona et un juge de sycophancie sociale partagent donc un signal lexical par construction. Le compte lexical proposé comme référence à battre est nécessaire mais B ne dit pas sur quelles sorties le classifieur de persona a été construit : si c'est sur les transcriptions d'Open Character Training (12 000, RAPPORTÉ §2) ou avec un juge de la même famille que le professeur (GLM 4.5 Air, RAPPORTÉ §2), l'aire sous la courbe ≥ 0,9 est une mesure dans l'échantillon, et la circularité déclarée par les auteurs (RAPPORTÉ §2) est importée telle quelle.

4. **Contrôle de format inadéquat.** « Reformater artificiellement » des sorties *Loving* teste la sensibilité du classifieur à *une* transformation choisie par l'expérimentateur, pas à la distribution de format que le RLVR induit réellement. L'estimateur naturel de l'effet de format est déjà dans le plan (Instruct avant vs après RL, sur le classifieur de persona) mais B ne l'utilise pas comme nulle de format.

5. **E2 : appariement sur la longueur = conditionnement sur une variable post-traitement.** La longueur est affectée par le modèle de récompense ; apparier dessus conditionne sur un médiateur et peut créer un biais de sélection. Une pénalité de longueur déclarée d'avance dans la récompense, ou une analyse par bornes, est préférable.

6. **E2 : modèle de récompense non identifié.** Si ce modèle a été entraîné sur des préférences du type de celles où la validation émotionnelle est préférée (le lien avec PRISM/UltraFeedback/LMSys est RAPPORTÉ pour le constat §1.6 ; que le modèle de récompense choisi y soit entraîné est HYPOTHÈSE), « le renforcement par préférences amplifie *Loving* » est vrai par construction de la récompense. Le contrôle à récompense aléatoire ne détecte pas ce cas : il distingue optimisation et exposition, pas récompense pro-validation et récompense neutre.

7. **E3 : estimation de g sans test de spécification.** R3 montre que la loi d'attraction ne passe pas aux autres familles (OBSERVÉ-NON-AUDITÉ, piece-sycophancie §1) ; un entraînement de caractère peut déplacer le modèle hors du régime où Δ = g·(c − v₀) s'ajuste. B estime g et c sans opposer le modèle d'attraction à un déplacement constant ; un Δg « observé » peut alors n'être qu'un artefact de mauvaise spécification.

8. **E4 présenté comme test, alors que c'est un contrôle positif.** *Sycophantic* est distillé à partir d'une constitution « toujours d'accord » (RAPPORTÉ §2, tableau 1). Une capitulation factuelle élevée vérifie que la distillation a suivi la constitution ; elle ne falsifie pas « persona = ton ». L'issue H_B, elle, serait informative — mais sur l'instrument autant que sur la persona.

9. **Juge validé hors distribution.** La validation humaine de GPT-4o porte sur des sorties du papier sur la chaleur (470 ou 235, non réconciliées, RAPPORTÉ §1.1 et §4) ; B le réemploie sur des sorties post-RLVR dont le format diffère. Le kappa de 0,73–0,81 ne se transfère pas.

10. **Multiplicité.** Quatre expériences, au moins deux métriques chacune, aucune procédure de contrôle d'erreur familiale déclarée.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **(Σ2) Dénominateur du ratio.** Si Ĉ_avant ~ approx. N(μ, σ²) avec |μ|/σ sous ~3 (illustratif), R̂ n'a pas de moments finis et ses intervalles percentiles sont instables ; les seuils 0,3/0,5/0,7 deviennent non jugeables. Avec trois graines, la variance inter-graines a 2 degrés de liberté : la demi-largeur d'un intervalle t est ≈ 4,3·s/√3 ≈ 2,5·s (calcul). Si l'écart-type inter-graines de Ĉ dépasse ~0,2·C_avant (illustratif), l'intervalle de R̂ couvre 0,5 quelle que soit la vérité.
- **Atténuation et biais de juge.** Pour un juge binaire, π* = s·π + (1 − p)(1 − π) ; la différence entre bras est multipliée par (s + p − 1). Aux minima de B (s = 0,8, p = 0,9), facteur 0,7 (calcul). R̂ n'est sans biais que si ce facteur est identique avant et après : r_obs = [(s₂+p₂−1)·C_après + b₂] / [(s₁+p₁−1)·C_avant + b₁]. Si (s, p) dépendent du format (misclassification différentielle), r_obs est biaisé dans une direction inconnue : non jugeable sans estimation de (s, p) par bras.
- **Saturation d'échelle.** Si Y est une probabilité de persona et E[Y_base] → 0 ou E[Y_persona] → 1, les différences saturent ; passer en logit ou en aire sous la courbe. Condition : P(Y_base > τ) ≈ 0 pour tout τ rend l'effet de format sur la base inestimable.
- **Refus exclus.** Sur une échelle d'amplitude L, le biais maximal dû à des refus exclus est |ρ₁ − ρ₂|·L. Pour E2 (L = 100 points, seuil 2 points), |Δρ| > 0,02 suffit à rendre H_B non jugeable (calcul).
- **E3 : identification et précision de g.** La régression de Δ sur v₀ donne pente −g et ordonnée g·c ; se(ĝ) ∝ 1/(σ_{v₀}·√n). Si Var_items(v₀) → 0, g et c ne sont pas séparément identifiés. Au volume de R6 (1 350 générations par modèle), l'intervalle sur une différence de g fut [−0,220 ; 0,197] (OBSERVÉ-NON-AUDITÉ, piece-sycophancie §1), demi-largeur ≈ 0,2 ; les seuils de B (|Δg| < 0,1 contre ≥ 0,15) sont sous la résolution : l'intervalle couvrira les deux régions. Ramener la demi-largeur à 0,05 demande ≈ (0,2/0,05)² = 16 fois le volume (calcul, illustratif), bien au-delà des 1 350 générations budgétées.
- **E2 : différence de différences sur proportions.** Avec quatre cellules indépendantes de n items et des proportions près de 0,5, se(DiD) ≈ 100/√n points (calcul). Pour que H_B (|DiD| < 2) soit jugeable face à H_A (≥ 5), il faut une demi-largeur ≤ 1,5 point, soit n de l'ordre de 17 000 par cellule (calcul, illustratif) sans appariement. B ne déclare ni appariement ni taille.

### (c) Contrôles négatifs dont l'absence serait fatale

- Récompense permutée pour **E1** (B ne l'a que pour E2) : sépare optimisation et exposition aux prompts.
- Bras de post-entraînement apparié sur KL(π ‖ π₀), non sur le nombre d'étapes.
- Dose de pénalité KL (dont β = 0) : sans elle, (Σ1) rend H_A inattaquable.
- Nulle de format : Instruct avant vs après RL sur le classifieur de persona, déclarée comme telle.
- Ré-notation des sorties « avant » dans la même passe interfoliée que les « après », juge figé (Σ3).
- E3 : modèle concurrent à déplacement constant, ajusté avant toute lecture de Δg.
- E2 : notes du modèle de récompense sur des paires ne différant que par la longueur ou par les mots de validation ; si la récompense suit ces paires, l'amplification est un artefact de l'instrument.

---

## Sur la proposition C

Pièce absente (jamais lancée) ; aucune critique possible.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Règle de décision sans intervalle pour E1.** « R ≥ 0,50 falsifie H_B ; R < 0,50 falsifie H_A » est une règle sur l'estimateur ponctuel. Avec un intervalle qui traverse 0,50, rien n'est falsifié ; D ne déclare pas de verdict « indécis » pour E1 (contrairement à ses E3 et à la proposition E).

2. **(Σ1)** s'applique ; D n'a ni coefficient KL déclaré, ni bras β = 0. La « récompense permutée » est un bon contrôle d'optimisation, mais ne lève pas la contrainte structurelle.

3. **Pas de bras de post-entraînement non-RL.** D ne peut attribuer une érosion « au RL » plutôt qu'à n'importe quelle mise à jour ; la conclusion « non-persistance dans ce régime » reste correcte, mais la question posée (« après RL ») n'est pas distinguée de « après quoi que ce soit ».

4. **E2 : soustraction de deux construits sur deux échelles.** ΔS (validation injustifiée jugée, sur conseils) et ΔF (points de justesse, extraits mécaniquement) ont des instruments différents, donc des facteurs d'atténuation (s + p − 1) différents. ΔS_obs − ΔF_obs = (s_S+p_S−1)·ΔS − (s_F+p_F−1)·ΔF + termes de biais ; « sélectivité sociale ≥ 5 points » n'a de sens que si les deux facteurs sont égaux ou estimés. Le seuil mélange effet et instrument.

5. **E2 : attente ΔS = +12 sans base rapportée.** Le plus grand effet du papier sur la chaleur est 11,9 points, sous ajustement supervisé avec contexte triste (RAPPORTÉ §1.1) ; D prévoit un effet d'interaction persona × RLVR-mathématiques d'ampleur comparable sur un construit social. C'est une hypothèse légitime, mais le calcul de puissance qui en découle sera optimiste si la vraie interaction est de 2–3 points.

6. **E2 : « ton et format constants » après RL est une instruction, pas une garantie.** Le format post-RLVR est une variable de sortie ; l'imposer par consigne dans l'évaluation transforme un médiateur en covariable manipulée et peut à lui seul changer S.

7. **E3 : seuil sous la résolution et paramètres par item.** |Δg| < 0,05 est quatre fois plus fin que la demi-largeur de R6 (≈ 0,2, OBSERVÉ-NON-AUDITÉ) pour un budget (36 h) qui suggère un volume comparable. De plus, « paramètres estimés par item et graine » n'est pas identifiable : au sein d'un item, v₀ est fixe ; g et c ne se séparent qu'à travers la variation de v₀ entre items. Avec trois doses et un point fixe qui bouge avec la dose (R6, OBSERVÉ-NON-AUDITÉ), un g par item avec c libre est sous-déterminé.

8. **E3 : transfert abusif de S3.** La condition S3 de R8 porte sur la chaîne Tülu 3 sur base (OBSERVÉ-NON-AUDITÉ, piece-sycophancie §2) ; la lire sur des points de contrôle à persona d'une autre chaîne est une hypothèse supplémentaire non déclarée.

9. **Fuite dans la validation des instruments.** Les 200 paires honnêtes et 200 cas à contraste servent à la fois à régler le juge (prompt, seuil) et à rapporter détection ≥ 80 % / fausses alertes ≤ 5 %. Sans partage tenu à l'écart déclaré, ces taux sont dans l'échantillon. « Étiquettes permutées » n'a pas de sens pour un juge sollicité par consigne (sans entraînement sur étiquettes) ; D ne précise pas la nature du classifieur.

10. **Stratification sur les refus.** Les refus sont post-traitement ; stratifier dessus conditionne sur un collisionneur possible. Des bornes (Manski-type) sont plus défendables qu'une strate.

11. **(Σ3)** s'applique à E3.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- (Σ2) comme en B : coefficient de variation du dénominateur, 2 degrés de liberté inter-graines.
- **E2 :** Var(ΔS − ΔF) est la somme de huit variances de cellules ; pour des proportions près de 0,5 et n items par cellule, se ≈ 141/√n points (calcul) ; un seuil de 5 points exige une demi-largeur < 5, donc n de l'ordre de 3 000 par cellule (calcul, illustratif) sans appariement. Non jugeable aux volumes implicites de « 2 jours ».
- **E2, atténuation :** si (s_S + p_S − 1) ≠ (s_F + p_F − 1), le signe de ΔS − ΔF n'est pas identifié.
- **E3 :** non identifiabilité si Var_items(v₀) → 0 ; se(Δĝ) ≈ 0,2 au volume R6 contre seuil 0,05 : jugeable seulement avec ≈ 16 fois le volume (calcul). Si c → moyenne de v₀, Δ moyen → 0 quel que soit g : la puissance sur g vient de la dispersion de v₀ autour de c, qui n'est pas contrôlée.
- **Refus :** biais maximal |Δρ|·L sur l'estimateur de F ; pour L = 100 et seuil 5 points, |Δρ| > 0,05 est fatal (calcul).

### (c) Contrôles négatifs dont l'absence serait fatale

- Bras de post-entraînement non-RL apparié sur KL : absent.
- Dose KL / β = 0 : absent.
- E2 : « même réponse fausse attribuée à une source impersonnelle » (contrôle présent chez E, absent chez D) : sans lui, F ne distingue pas capitulation sociale et capitulation à une affirmation quelconque.
- E3 : dose nulle, doses permutées, concurrent à déplacement constant : présents (point fort de D).
- Partage tenu à l'écart pour la validation des juges : absent.
- Ré-notation interfoliée avant/après (Σ3) : absente.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Candidate B : l'estimand ne mesure pas le « maintien ».** D = S_Loving,après − S_base,après est transversal, post-RL. Si *Loving* porte déjà un coût factuel avant tout RL (non mesuré par Open Character Training, RAPPORTÉ §2 ; attendu par analogie avec −15,06 points sous tristesse + fausse croyance, RAPPORTÉ §1.1, mais hors chaîne), D ≥ 5 est vrai avant le renforcement et H_A ne dit rien de la persistance. Le témoin « sans mise à jour » existe dans le socle mais n'entre pas dans l'estimand ; il faut D_après − D_avant.

2. **Fuite de domaine entre récompense et évaluation.** Le RLVR porte sur « problèmes arithmétiques générés » et la candidate B évalue sur « 300 problèmes à réponse calculable ». Si les deux générateurs se recouvrent, la récompense agit directement sur les items d'évaluation ; le S après RL reflète la robustesse acquise en domaine, pas la persona. L'évaluation de sycophancie doit porter sur un support que la récompense n'a jamais touché (la tâche de désinformation, RAPPORTÉ §1.1, par exemple).

3. **Aucun contrôle positif d'instrument sur des sorties réelles.** Seul *Loving* est utilisé ; la banque de 100 paires par construit est rédigée par les expérimentateurs. Un instrument validé sur des contrastes écrits à la main peut ne pas voir la sycophancie telle qu'un modèle la produit. Le point de contrôle *Sycophantic* (RAPPORTÉ §3) est le contrôle positif disponible ; sans lui, un D sous le seuil est indécidable entre « pas d'effet » et « instrument aveugle ».

4. **Aveuglement des annotateurs non garanti.** Après RLVR, le format (chaîne de raisonnement, réponses encadrées) révèle le bras. Les « paires de même longueur » neutralisent la longueur, pas le format. Une normalisation de présentation est nécessaire, et elle doit elle-même être testée (elle peut retirer de la chaleur).

5. **Candidate C : estimand sans base.** « Excès post-renforcement de validation injustifiée chez *Loving* » est un avant/après sur un seul modèle ; une hausse générique due au RL (ou au format) est attribuée à la persona. Le bras base + RL existe dans le socle ; l'estimand doit être une double différence.

6. **(Σ1)** s'applique ; aucun coefficient KL, aucun bras β = 0, aucune récompense permutée. Le plan n'a que « RL » contre « sans mise à jour » : exposition, optimisation et format ne sont pas séparables.

7. **Fiabilité inter-annotateurs non planifiée.** E ne vise aucun accord entre annotateurs ; la fragmentation du construit (RAPPORTÉ §1.2 ; les chiffres d'ICC y concernent des experts jugeant des définitions, pas des annotateurs de sorties — je ne les transfère pas) rend ce risque réel. Deux annotateurs au moins et un kappa rapporté sont un minimum.

8. **Pas de bras de post-entraînement non-RL** (même critique qu'en B-(a)2 et D-(a)3).

9. **Point fort à conserver, en le disant :** la candidate A sépare chaleur et accord par construction (« sans opinion à approuver ») ; la règle d'intervalle déclarée évite la falsification sur estimateur ponctuel. Je m'en sers comme référence pour critiquer D-(a)1.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Candidate A, par le calcul de E lui-même.** W binaire, 300 items : se d'une différence de proportions ≈ √(2·0,25/300) ≈ 0,04 (calcul, à p = 0,5). Avec G_avant = 0,5 et R = 0,8 (valeurs illustratives cohérentes avec l'attente d'E), méthode delta : se(R̂) ≈ 0,8·√((0,04/0,5)² + (0,04/0,4)²) ≈ 0,10 ; demi-largeur ≈ 0,2 ; intervalle ≈ [0,6 ; 1,0], qui traverse le seuil 0,70. **L'issue attendue par E est « indécis » à son propre volume** ; il faut environ quatre fois plus d'items ou de graines pour une demi-largeur de 0,1 (calcul, illustratif), et davantage si la variance inter-graines est non nulle.
- **Peu de grappes.** Avec trois graines comme grappes de niveau supérieur, l'inférence robuste par grappes a 2 degrés de liberté ; si Var_graines(Ĝ) n'est pas négligeable, aucun intervalle à 95 % n'est fiable.
- **Atténuation humaine.** Si deux annotateurs ont un accord κ bas, la différence observée de W est multipliée par (s + p − 1) de l'annotation ; R̂ reste sans biais seulement si ce facteur est égal avant/après, ce que le format post-RL compromet.
- **Candidate B :** l'estimand E[S | domaine d'évaluation] n'est pas séparable d'un effet de domaine de la récompense quand la distance entre la distribution d'évaluation et celle d'entraînement RL tend vers zéro ; D devient une mesure du RL en domaine, pas de la persona.
- **Refus :** mesurés séparément (bon) ; mais si ρ diffère entre bras, la justesse sur le sous-ensemble retenu n'est identifiée que sous hypothèse de manquement aléatoire ; borne |Δρ|·L.

### (c) Contrôles négatifs dont l'absence serait fatale

- Base + RL dans les estimands de B et C (double différence) : le bras existe, l'estimand l'ignore.
- Récompense permutée : absente.
- Bras de post-entraînement non-RL apparié sur KL : absent.
- Dose KL / β = 0 : absente.
- Évaluation de sycophancie hors du support de la récompense : absente.
- Contrôle positif *Sycophantic* pour chaque instrument : absent.
- Nulle de format sur l'annotation humaine (base avant vs après RL sur W) : absente.
- Accord inter-annotateurs rapporté : absent.

FIN-DE-CELLULE