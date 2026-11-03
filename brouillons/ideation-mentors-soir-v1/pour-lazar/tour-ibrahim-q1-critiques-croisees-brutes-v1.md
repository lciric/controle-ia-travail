# Tour du collisionneur, Ibrahim Q1 (sans Argon) — critiques croisées (E3-T2), brutes

Copie à l'octet vérifiée contre les compagnons ; espèces par lettre ; rien lu ni modifié par conv-audit.


---

## E3-T2-critique-croisee-A.md (sha256 `18c97d3a5ce1c6ebc9ca04114b1767bb54e4db783cde0bd6c2bd9b99c08bfe1f`)

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

---

## E3-T2-critique-croisee-B.md (sha256 `8a618e14202c401976dd2f19df4d7aed4de156685df79c108f49708a1a6b1da2`)

# Proposition B — Tour III.2 : critique croisée de méthode

**Statuts.** Les faits de la pièce Ibrahim sont RAPPORTÉS : un rapport les a lus sur page primaire. Pour les chiffres des dépôts de Lazar (pièce sycophancie), A les classe RAPPORTÉ et D les classe OBSERVÉ-NON-AUDITÉ. Je ne tranche pas cet écart et je le signale à l'arbitre. Mes critiques sont des HYPOTHÈSES de méthode. Mes nombres sont marqués « calcul » ou « illustratif ». Je ne fusionne pas les propositions. Quand un défaut se répète, je renvoie à la section où je l'ai d'abord traité.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Statut mal posé (règle 1).** Au point (a)5, A classe l'accès aux poids OCT en OBSERVÉ-NON-AUDITÉ. Or la pièce dit seulement « accès filtré annoncé, non vérifié » (pièce Ibrahim §3). Personne n'a observé cet accès. Il s'agit d'une annonce RAPPORTÉE, dont rien n'a été vérifié.

2. **E1 : le duel n'est pas exhaustif, et son seuil est incohérent.**
   - H_A exige un déplacement de l'erreur **et** un déplacement de g. H_B exige qu'aucun des deux ne bouge. Les cas mixtes (l'erreur bouge mais pas g, ou l'inverse) ne falsifient rien, ce qui contrevient à B4.
   - H_A pose « ≥ +11 points », alors que le seuil opérationnel est de 5 points.
   - La portée du « +11 » n'est pas établie : le rapport ne dit pas s'il vaut pour Llama-3.1-8B seul (pièce Ibrahim §1.1 et §4). En faire le niveau attendu sur ce modèle déborde ce que dit le fait.

3. **E1 : le seuil Δg ≥ 0,2 est étiqueté « calcul », mais c'est un choix.**
   - L'intervalle [−0,220 ; 0,197] porte sur un contraste **intra-modèle** entre doses, sous critique, sur 1 350 générations (pièce sycophancie §1).
   - Un écart **entre deux points de contrôle** additionne la variance de deux ajustements indépendants. Il a donc au moins la même variance, et sans doute davantage.
   - Fixer le seuil à la demi-largeur du bruit donne une puissance d'environ 50 % quand le vrai Δg vaut 0,2 (calcul, sous normalité).

4. **E1 : le contrôle négatif prouve autre chose que ce qu'A annonce.**
   - A compare la base Instruct munie d'une consigne reprenant la persona au modèle entraîné. Si les deux produisent le même déplacement, cela montre que la consigne induit la même sycophancie que l'entraînement. Cela ne montre pas que le juge « lit le style ».
   - Le même défaut revient en (c), pour le classifieur : la base munie d'une consigne chaleureuse et classée *Loving* compte comme fausse alerte, alors qu'une sortie réellement chaleureuse classée *Loving* est une détection correcte.
   - Une fausse alerte doit porter sur une sortie qui **n'a pas** le construit visé.

5. **Fuite entre la construction de l'instrument et son évaluation.**
   - La rétention de la persona (E2) est lue par le classifieur d'OCT. Ce classifieur est fondé sur des modèles, et ses biais et sa circularité sont déclarés (pièce Ibrahim §2).
   - Toute dérive de distribution due au RLVR (format, longueur, registre) éloigne les sorties de ce que le classifieur reconnaît. Elle se lit alors comme une érosion, presque par construction.
   - La troncature à longueur fixe ne règle pas ce point. Elle est elle-même une source d'artefact : la troncature à 300 caractères a déjà produit un faux positif (pièce sycophancie §3).

6. **Régression vers la moyenne dans g (E1, E2).**
   - Si la même estimation bruitée de la note sans pression v̂₀ sert à la fois à définir Δ et à servir de régresseur, une pente positive apparaît même sans aucune attraction.
   - Ce biais vaut environ σ²_e / Var(v̂₀), où σ²_e est la variance de bruit de v̂₀ (calcul, modèle d'erreur classique).
   - Une persona qui change la dispersion entre tirages change ce biais. Elle peut donc fabriquer un Δg sans que la loi d'attraction bouge.

7. **E2 : la falsification annoncée ne suit pas.**
   - H_B se déclenche dès que la rétention passe sous 50 %, même si g ne bouge pas. Une issue H_B n'implique donc pas un déplacement de g.
   - Même quand g bouge sous RLVR, l'a priori de R8 (« le gain vient de l'optimisation des préférences ») n'est pas réfuté : une cause peut avoir plusieurs sources.
   - R8 vise en outre la chaîne Tülu 3, pas OCT (pièce sycophancie §2).
   - Enfin, la zone de rétention entre 50 et 80 % avec |Δg| < 0,2 ne falsifie rien.

8. **E2 : la persistance peut être vraie par construction.**
   - Un RLVR sur des problèmes vérifiables, sous pénalité KL et sur quelques centaines de pas, peut laisser la distribution presque intacte sur les prompts de persona.
   - « La persona tient » mesurerait alors la distance parcourue, non la robustesse.
   - L'axe de dose doit être exprimé en divergence mesurée sur les prompts d'évaluation, pas en nombre de pas.

9. **E3 : facteurs confondus et seuil d'interaction trop bas.**
   - Le facteur « RL à préférences » est confondu avec le contenu des paires. Les réponses préférées de PRISM, UltraFeedback et LMSys contiennent plus de validation (pièce Ibrahim §1.6). Le « contrôle » sur paires équilibrées est en réalité une troisième modalité du traitement, pas un contrôle négatif.
   - *Loving* part déjà haut en validation. Sur une échelle bornée, l'interaction persona × étape dépend de l'échelle choisie : un plafond peut la créer ou l'effacer.
   - Pour un contraste d'interaction en 2 × 2, l'erreur type vaut √4·σ_cellule, contre √2·σ_cellule pour une simple différence, soit un facteur √2 (calcul, cellules indépendantes de même variance). Reprendre le seuil de 0,2 d'E1 sous-dimensionne donc encore davantage.

10. **Dérive du juge.** Le juge Claude est un alias d'interface non figé (pièce sycophancie §1). Si l'on juge avant et après RL à des dates différentes, le Δ mesuré inclut un éventuel changement de version du juge.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Rétention R = C_après / C_avant.**
  - L'intervalle de Fieller de R n'est borné que si l'intervalle de C_avant exclut 0 au même niveau.
  - Si le classifieur sature, avec un score proche de 1 pour la base comme pour la persona, C_avant tend vers 0 et R n'est pas jugeable.
- **Pente g.**
  - SE(ĝ) ≈ σ_ε / (√n · sd(v₀)). Si la persona comprime la distribution des notes sans pression (Var(v₀) tend vers 0, effet plafond), ĝ devient indéterminé.
  - Si les déplacements deviennent constants, avec Var(Δ | v₀) indépendant de v₀ (cas de Qwen et Mistral, R3, pièce sycophancie §1), g n'est plus distinguable d'un modèle à déplacement constant.
- **Refus.**
  - Si la probabilité de refus diffère entre bras, exclure les items à refus revient à conditionner sur une variable postérieure au traitement : l'estimateur est biaisé, quelle que soit la taille de n.
  - Il faut une exclusion commune par item, fixée d'avance sur l'union des bras.
- **Graines d'entraînement.**
  - Si la variance entre entraînements τ² domine la variance entre items, la puissance dépend du nombre d'entraînements, pas du nombre de générations.
  - A ne donne pas ce nombre pour E2. Avec un seul entraînement par départ, τ² n'est pas estimable et aucun intervalle n'est valide.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Sorties honnêtes appariées** : même position et même contenu, seul le style change. C'est le seul vrai négatif pour le classifieur et pour le juge. Il manque.
2. **Dose nulle placebo**, avec v₀ estimé sur des tirages disjoints de ceux qui servent à calculer Δ. Sans cela, ĝ > 0 peut n'être qu'une régression vers la moyenne.
3. **Test-retest d'un point de contrôle non modifié**, évalué deux fois par le même instrument : il donne le plancher de bruit de la rétention. Le contrôle 2 d'A (autodistillation par ajustement supervisé) modifie les poids et ne remplit pas ce rôle.
4. **Jeu d'ancrage rejugé à chaque passe**, pour détecter la dérive du juge.
5. **Pour E3, un modèle de récompense à préférences permutées**, qui mesure ce que fait l'optimisation contre une récompense sans signal.

---

## Sur la proposition C

Pièce absente (jamais lancée). Je n'en critique aucun contenu.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **La falsification porte sur des estimations ponctuelles.**
   - En E1, « R ≥ 0,50 falsifie H_B » est énoncé sans règle d'intervalle. Une estimation ponctuelle ne falsifie rien.
   - E, au contraire, l'écrit explicitement : un intervalle à cheval sur le seuil donne un verdict indécis.

2. **E1 : l'instrument qui mesure C n'est pas nommé.** Si c'est le classifieur d'OCT, la fuite décrite en A(a)5 s'applique telle quelle.

3. **E1 : le témoin à récompense permutée n'est pas apparié en ampleur de changement.**
   - Une récompense aléatoire produit des gradients qui se compensent en moyenne. À nombre de pas égal, ce bras change moins la politique que le bras à vraie récompense.
   - Un écart de rétention entre les deux mesurerait alors la quantité de changement, pas l'optimisation.
   - L'appariement doit se faire sur la divergence KL atteinte, pas sur le nombre de pas.

4. **E2 : les attentes contredisent celles d'E1.**
   - E1 attend une légère érosion (R = +0,85).
   - E2 attend une double différence ΔS = +12 points, donc un RL qui **amplifie** la sycophancie sociale propre à la persona.
   - Sans mécanisme d'amplification énoncé, les deux attentes sont incompatibles. L'une des deux ne peut pas être « l'attente ».

5. **E2 : S et F sont lus sur deux échelles qui ne se comparent pas.**
   - S provient d'un juge, F d'un extracteur exact. La différence ΔS − ΔF en points dépend des taux de base et de la fiabilité propre à chaque instrument.
   - Un instrument plus bruité atténue sa double différence. Si les fiabilités diffèrent, une « sélectivité » peut apparaître ou disparaître sans rien changer au comportement.

6. **E2 : un « ton constant » est impossible à imposer à une persona.**
   - Ibrahim §1.5 manipule la sycophancie à ton constant par construction expérimentale (pièce Ibrahim §1.5).
   - Ici, le ton est l'effet du traitement : on ne peut pas le maintenir constant dans les sorties.
   - Il faut soit une notation aveugle au ton, soit une normalisation postérieure validée. Sinon, la condition annoncée n'est pas réalisée.

7. **E3 : la marge d'équivalence rend H_A pratiquement inconfirmable.**
   - H_A exige |Δg| < 0,05. Avec une demi-largeur d'environ 0,21 à 1 350 générations, contraste intra-modèle (pièce sycophancie §1), atteindre une demi-largeur de 0,05 demande environ (0,21/0,05)² ≈ 17,6 fois plus de données, soit environ 24 000 générations par contraste (calcul, SE ∝ 1/√n, même structure de variance).
   - Pour un contraste entre points de contrôle, la demande est encore plus forte.
   - Seule l'issue H_B peut donc gagner : le duel est asymétrique.
   - E3 hérite aussi du biais de régression vers la moyenne décrit en A(a)6.

8. **Les seuils de validation (c) ne sont pas vérifiables à cette taille d'échantillon.**
   - À n = 200 et 5 % de fausses alertes observées, l'intervalle de Wilson à 95 % vaut environ [2,7 % ; 9,0 %] (calcul).
   - « ≤ 5 % » ne s'établit qu'avec une borne supérieure sous 5 %, donc avec plus de cas ou un taux observé plus bas.

9. **Les « 200 cas à contraste connu » risquent la circularité.** S'ils sont produits en sollicitant les mêmes modèles, ou jugés par la même famille de juge, l'instrument est validé sur la distribution qui l'a construit.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **R** : mêmes conditions de Fieller qu'en A(b).
- **Trois graines.**
  - Si τ² (variance entre entraînements) domine, l'intervalle ne repose que sur 2 degrés de liberté.
  - Le quantile t à 0,975 pour 2 degrés de liberté vaut environ 4,30, contre 1,96 : les intervalles s'élargissent d'un facteur d'environ 2,2 (calcul).
- **F (capitulation factuelle).** Si la justesse sans fausse croyance est proche de 1 ou proche du taux de hasard, l'excès d'erreur dû à la croyance est écrasé au plancher ou au plafond : la double différence perd sa variance.
- **S (sycophancie sociale).**
  - Si l'accord entre annotateurs (ou entre juge et humains) est faible, la double différence est atténuée d'un facteur proche de la fiabilité.
  - Avec une fiabilité inconnue, le seuil de +5 points n'a pas de puissance définie.
- **g.**
  - Mêmes conditions qu'en A(b) : Var(v₀) tend vers 0, ou Var(Δ | v₀) devient indépendant de v₀.
  - D prévoit lui-même d'opposer le modèle d'attraction au déplacement constant, et c'est juste.
  - Si les estimations par item et par graine reposent sur 5 tirages, l'atténuation par erreurs sur v₀ varie avec la dispersion propre à chaque modèle.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Croyance de l'utilisateur correcte** dans F. Sans elle, une baisse générale de justesse et une déférence à l'utilisateur produisent le même signal. E l'a prévue, D non.
2. **Témoin apparié en divergence KL**, en remplacement du simple appariement en pas.
3. **Dose nulle avec v₀ estimé sur échantillon disjoint**, pour E3. D a la dose nulle, mais pas la disjonction.
4. **Test-retest d'un point de contrôle non modifié.**

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Candidates B et C : le terme d'avant-RL manque.**
   - D est défini comme S_Loving,après − S_base,après. D_social n'est lu qu'après RL.
   - Or la question posée est : la chaleur persistante « **conserve**-t-elle son coût ? ». Y répondre exige de comparer avant et après RL.
   - Un D ≥ 5 points peut être créé par le RL comme hérité de la persona. Les deux candidates ne testent donc pas la persistance qu'elles nomment.

2. **Candidate B : le domaine du RL fuit dans celui de l'évaluation.**
   - Le RLVR porte sur des problèmes arithmétiques générés. L'évaluation porte sur 300 problèmes à réponse calculable.
   - Le RL améliore directement la compétence évaluée. L'erreur, avec ou sans fausse croyance, se rapproche de 0 dans les deux bras.
   - S est alors comprimé au plancher, et D < +5 devient probable **par construction** : H_B gagnerait sans rien dire de la sycophancie.

3. **Candidate A : un G_avant faible et un plafond menacent l'arbitrage.**
   - Sur des situations de soutien, une base Instruct est probablement déjà chaleureuse (HYPOTHÈSE). Avec une annotation binaire, W tend vers 1 dans les deux bras.
   - E prévoit l'arrêt si G_avant n'est pas « nettement positif », et c'est juste. Mais aucun critère n'est fixé : le seuil d'arrêt devient un degré de liberté de l'analyste.

4. **Candidate A : le contrôle négatif est ambigu.**
   - Que *Loving* manifeste de la chaleur sur des questions factuelles relève de la généralisation de la persona, pas d'un confondant.
   - Il faut fixer d'avance quelle issue de ce contrôle invaliderait la mesure. Sinon il ne contrôle rien.

5. **Candidate C : la fiabilité de la vérité terrain n'est pas établie.**
   - La frontière « validation justifiée / injustifiée » est fixée par des annotateurs.
   - Pour un construit voisin, un expert isolé a une fiabilité de 0,184 en corrélation intraclasse, contre 0,960 pour la moyenne des experts (pièce Ibrahim §1.2). Le transfert de ce chiffre à l'annotation de sorties est une HYPOTHÈSE.
   - Si la valeur s'en approche, la formule de Spearman-Brown donne environ 0,53 pour 5 annotateurs, et il en faut environ 18 pour atteindre 0,8 (calcul).
   - « Annotation humaine aveugle » sans nombre d'annotateurs laisse donc la mesure non jugeable.

6. **L'aveugle n'est que partiel.** L'annotation de chaleur ne peut pas être aveugle au style, puisque le style est la signature de la persona. Elle peut seulement l'être à l'identité du modèle et au moment de la mesure, à condition de mélanger les lots avant et après RL. E ne le précise pas.

7. **Validation (c) à n = 100 par construit.** À 5 % de fausses alertes observées, l'intervalle de Wilson vaut environ [2,2 % ; 11,2 %] (calcul). Les seuils « ≤ 5 % » ne peuvent donc pas être établis, comme en D(a)8.

8. **Volume d'annotation humaine non chiffré.**
   - La seule candidate A représente 300 situations × 2 modèles × 2 moments × 3 graines, soit 3 600 jugements, avant toute réplication (calcul).
   - Le budget est « à établir ». La faisabilité de l'expérience retenue n'est donc pas démontrée.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **R (candidate A).**
  - Conditions de Fieller comme en A(b).
  - Avec W binaire, Var(Ĝ) = Σ p(1 − p)/n tend vers 0 près du plafond, mais G aussi. Le rapport signal sur bruit de G_avant décroît, et l'intervalle de R devient non borné.
- **Règle « intervalle à cheval → indécis ».** Elle est correcte, mais aucune taille d'échantillon n'est calculée pour rendre l'issue indécise improbable. Sous l'attendu R = 0,80 contre un seuil de 0,70, l'écart à résoudre vaut 0,10.
- **Graines.** Intervalles regroupés par entraînement avec trois graines : mêmes 2 degrés de liberté et même facteur d'environ 2,2 qu'en D(b) (calcul).
- **D (candidate B).** Si la justesse après RL sans fausse croyance tend vers 1, S tend vers 0 dans les deux bras et D perd toute variance : non jugeable.
- **D_social (candidate C).** Une fiabilité basse atténue l'effet observé d'environ le facteur de fiabilité. Le seuil de +5 points n'a pas de puissance définie tant qu'elle n'est pas mesurée.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Mesure avant RL dans les candidates B et C** : sans elle, aucune conclusion de persistance n'est possible.
2. **Jeu factuel hors du domaine arithmétique**, pour la candidate B. C'est le seul moyen de séparer le gain de compétence de la déférence.
3. **Test-retest d'un point de contrôle non modifié**, et **annotation en lots mélangés** avant et après RL.
4. Les deux contrôles qu'E a déjà prévus, source impersonnelle et croyance correcte, sont bons. Je les reprends en le disant, comme référence pour D(c)1.

---

## Ce que j'en reprends, en le disant

- La règle d'E : un intervalle à cheval sur le seuil donne un verdict indécis.
- La dose nulle et la comparaison au modèle à déplacement constant chez D.
- Le témoin d'autodistillation chez A, comme contrôle de l'exposition aux prompts.

Aucune des trois propositions ne règle les quatre points suivants, et je les tiens pour bloquants :

1. L'estimation de v₀ sur des tirages disjoints de ceux qui servent à calculer Δ.
2. L'appariement des bras en divergence mesurée sur les prompts d'évaluation, plutôt qu'en nombre de pas.
3. Le test-retest d'un point de contrôle non modifié.
4. Un nombre de graines d'entraînement suffisant pour estimer τ².

FIN-DE-CELLULE

---

## E3-T2-critique-croisee-D.md (sha256 `459c353c84783792f2e3473e58ad9d9fa2750cef4b5dbf91106d6a9e1d59eaf4`)

Les faits repris des pièces restent **RAPPORTÉ**. Mes objections et les contrôles proposés sont des **HYPOTHÈSES**, sauf lorsqu’ils découlent directement des règles de décision écrites. Je note \(Y\) le construit comportemental, \(\widehat Y\) sa lecture instrumentale, \(Z\) le style, le format, la longueur ou les refus, \(X\) l’item et \(T\) le point de contrôle.

## Sur la proposition A

### (a) Défauts de méthode

- **Les duels ne couvrent pas les issues possibles.** Dans E1, « erreur factuelle et gain bougent » et « seul le point fixe bouge » laissent de côté l’absence d’effet, un effet factuel sans effet sur \(g\), un effet sur \(g\) sans effet factuel, ou des mouvements de signes opposés. E2 et E3 présentent le même défaut : leurs conclusions de falsification dépassent ce que leurs régions de décision permettent.
- **Le contrôle par consigne système ne discrimine pas style et entraînement.** Si la base ainsi invitée reproduit le déplacement, cela peut aussi signifier que deux interventions différentes produisent un comportement équivalent. Si elle ne le reproduit pas, l’intensité de persona peut simplement être mal appariée. Ce contrôle ne suffit donc à aucune des deux inférences proposées.
- **Les témoins d’entraînement ne isolent pas la récompense.** Le SFT sur les propres sorties peut être une auto-distillation qui préserve la persona ; à nombre de pas égal, il n’apparie ni les distributions de gradients, ni la distance parcourue, ni la pression de KL. Dans E3, RLVR et RL-préférences diffèrent simultanément par les données, la récompense, sa variance et l’optimisation effective. Rééquilibrer le modèle de récompense est une nouvelle intervention causale, pas un contrôle négatif.
- **Une issue de E2 ne réfuterait pas l’a priori général de R8.** Elle porterait sur des checkpoints OCT déjà passés par DPO et sur une autre chaîne d’entraînement ; un mouvement de \(g\) n’en attribuerait pas l’origine à l’imitation ou aux préférences.
- **La validation instrumentale n’est pas protégée contre les fuites.** Rien n’impose que les sorties ayant servi à choisir seuils, paires difficiles et règles de refus soient disjointes de l’évaluation finale. Dépasser un prédicteur lexical en AUC marginale n’établit pas non plus que le classifieur lise autre chose que \(Z\), notamment après RL.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- L’instrument n’apporte une information de construit que si \(I(Y;\widehat Y\mid X,Z,T)>0\). Si \(P(\widehat Y\mid Y,Z,T)\) change avec \(T\), ou si les supports de \(P(Z\mid T)\) avant et après RL sont disjoints, sensibilité et fausses alertes apprises avant RL ne se transportent pas ; la « rétention » estimée contient alors une dérive de mesure non identifiable.
- Pour une rétention \(\widehat R=\widehat G_{\text{après}}/\widehat G_{\text{avant}}\), si \(G_{\text{avant}}=0\), si sa loi estimée concentre une masse non négligeable près de zéro, ou si son signe est incertain, \(\widehat R\) est instable, potentiellement sans variance finie, et son interprétation peut s’inverser.
- Dans l’attraction, si la variance entre items de la distance au point fixe est nulle, \(g\) et le point fixe ne sont pas identifiables séparément. Une erreur de mesure du niveau sans pression comparable à cette variance atténue en outre \(\widehat g\).
- Si la probabilité de refus dépend de \(T\), de la dose ou de l’item, exclure les refus conditionne sur une variable post-traitement ; les noter au milieu impose une autre loi de sortie. Sans hypothèse de non-réponse, les deux estimations peuvent viser deux paramètres différents, sans qu’aucune ne représente la persistance comportementale.
- Si les corrélations intra-item ou intra-graine approchent un, multiplier les tirages augmente peu la taille effective. Des intervalles calculés sur les générations comme indépendantes seront trop étroits et trancheront des duels sans la puissance nominale annoncée.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Paires contenu/style désorthogonalisées, annotées par des humains et réservées**, comprenant des sorties post-RL : même contenu avec chaleur variable, même chaleur avec accord variable. Sans elles, rétention et sycophancie restent ininterprétables.
2. **Mise à jour avec récompense non informative**, en appariant invites, trajectoires et budget d’optimisation, plutôt que seulement le nombre de pas. Sans elle, l’effet propre de la récompense n’est pas séparé de la dérive d’optimisation.
3. **Croyance correcte et assertion fausse d’origine impersonnelle**, avec les mêmes items. Sans ces contrastes, exactitude, accord avec l’utilisateur et capitulation sociale restent confondus.

## Sur la proposition B

### (a) Défauts de méthode

- **L’attendu principal de E1 tombe dans la zone non tranchée.** Avec \(r\simeq0,6\), il ne satisfait ni la région de persistance ni celle d’effacement. La conception prévoit donc explicitement que son résultat attendu ne réponde pas au duel.
- **E4 ne falsifie pas les thèses annoncées.** Un écart factuel élevé ne réfute pas « persona = ton », puisque le ton peut précisément causer cet écart. Un ton élevé avec faible capitulation factuelle ne réfute pas une disposition sociale ou implicite. L’ordre intermédiaire imposé à *Loving* ajoute une issue non assignée s’il échoue.
- **Les cas positifs du juge sont circulaires.** Prendre les sorties de *Sycophantic* comme vérité terrain suppose précisément ce que E4 doit tester. Si cette persona ne capitule pas, la « sensibilité » estimée est celle à une identité de checkpoint, pas à un comportement.
- **Le reformatage synthétique ne valide qu’une transformation choisie.** Il est appliqué aux sorties *Loving*, pas nécessairement aux formats réellement produits après RL. Compter les refus ne corrige pas leur effet de sélection.
- **Le contrôle de dose est insuffisant.** Des gains mathématiques semblables n’impliquent ni distances de paramètres semblables, ni entropie, KL ou nombre effectif de mises à jour comparables. Le SFT neutre à pas égaux présente le même défaut.
- **E2 apparie la longueur post-traitement.** Si persona et RL affectent tous deux la longueur, cet appariement peut sélectionner les sorties et créer une association plutôt que supprimer un biais. La récompense aléatoire change également la variance des gradients et peut simplement empêcher l’optimisation.
- **La réutilisation annoncée des générations de E1 par E3 n’est pas assurée.** E1 ne produit pas, tel qu’écrit, le protocole dosé de pression sociale requis pour estimer \(g\) et le point fixe.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Le ratio \(r\) devient non jugeable lorsque son dénominateur est nul, proche de zéro relativement à son erreur d’estimation, ou de signe incertain. Une borne d’intervalle sur le numérateur ne résout pas cette instabilité.
- Pour E4, soit \(p_{m,b}=P(\text{erreur}\mid m,b)\). Si les probabilités sans croyance sont proches des bornes, ou si \(p_{m,\text{fausse}}-p_{m,\text{aucune}}=0\) parce que la manipulation n’a aucune prise, l’écart maximal atteignable peut rester sous les seuils : H_B devient vraie par construction, sans pouvoir sur la capitulation.
- Dans le DiD de E2, si l’analyse est conditionnée par l’absence de refus ou par une longueur affectée par les deux facteurs, l’estimand conditionnel change selon le bras ; l’interaction estimée peut alors provenir de lois de sélection différentes plutôt que d’une amplification.
- Pour l’attraction, une variation insuffisante des distances entre items rend \(g\) et le point fixe faiblement identifiés ; une exclusion de refus dépendante de la dose rend leurs trajectoires non comparables.
- À prévalence extrême des capitulations, le kappa peut rester proche de zéro malgré un accord brut élevé, ou devenir très instable. Le critère \(\kappa\) seul ne fournit alors ni validation ni invalidation utilisable du juge.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Cas positifs définis par annotation comportementale indépendante**, et non par le checkpoint *Sycophantic* ; sinon E4 et la validation du juge se valident mutuellement par hypothèse.
2. **Contrôles contenu/format sur sorties post-RL réellement observées**, et pas uniquement reformatage artificiel des sorties initiales.
3. **Récompense non informative à optimisation appariée** pour E1 comme pour E2 ; le SFT neutre et la récompense aléatoire actuels n’isolent pas le contenu de la récompense.
4. **Croyance correcte et source impersonnelle dans les contrastes de E4**, pas seulement dans la banc de validation du juge.

## Sur la proposition C

Pièce C absente, jamais lancée : aucune critique de méthode n’est possible et je n’en invente pas le contenu.

## Sur la proposition E

### (a) Défauts de méthode

- **Le seuil de A ne définit pas deux mécanismes.** Une rétention juste sous son seuil ne démontre pas que la persona ne survit pas ; H_B regroupe érosion partielle, inversion et absence initiale résiduelle. Le duel est exhaustif sur un paramètre, mais les interprétations verbales sont plus fortes que ce paramètre.
- **B et C ne mesurent pas la persistance.** Leur contraste principal est calculé après RL, sans différence correspondante avant RL. Un effet initial de *Loving*, totalement effacé ou fortement modifié par l’entraînement, peut ainsi produire le même \(D\) ou \(D_{\mathrm{social}}\) qu’une persistance parfaite.
- **Le témoin sans mise à jour n’isole pas le RL.** Même avec la soustraction de la base, il reste une possible interaction entre persona et n’importe quelle mise à jour de gradient. L’amélioration arithmétique établit que l’optimisation a agi, pas que sa dose effective est comparable entre départs.
- **L’annotation humaine ne supprime pas la circularité de construit.** Pour C, « conduite injustifiée » dépend d’une norme encodée dans les situations et les consignes. Si les mêmes exemples servent à former les annotateurs, régler les paires et valider l’instrument, les performances sont optimistes.
- **L’aveuglement ne garantit pas la stabilité temporelle.** Les annotateurs peuvent dériver entre les évaluations avant et après, ou reconnaître le style des bras malgré la suppression des étiquettes.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Pour \(R=G_{\text{après}}/G_{\text{avant}}\), une loi de \(\widehat G_{\text{avant}}\) concentrée près de zéro rend le ratio instable. Si la même banque sert au test d’arrêt initial et à l’estimation finale, la continuation conditionne la loi de \(\widehat G_{\text{avant}}\) : l’intervalle naïf et \(\widehat R\) subissent un biais de sélection.
- Si \(P(\widehat Y\mid Y,Z,T)\) dépend de \(T\), les taux annotés ou extraits avant/après ne distinguent pas changement comportemental et changement de lecture. Si les distributions de longueur, ton ou format n’ont plus de support commun, l’appariement ne transporte pas les propriétés de validation.
- Dans B, si \(P(\text{erreur}\mid\text{fausse croyance})-P(\text{erreur}\mid\text{sans croyance})=0\) dans tous les bras parce que la manipulation est inerte, alors \(D=0\) par construction. Des justesses proches des bornes peuvent également rendre le seuil inatteignable indépendamment de toute sycophancie.
- Dans C, une prévalence de validation injustifiée proche de zéro ou de un supprime la variance nécessaire à l’estimation de \(D_{\mathrm{social}}\). Des erreurs d’annotation différentielles selon le bras peuvent produire le signe attendu sans différence de \(Y\).
- Avec corrélations fortes intra-situation, intra-dialogue ou intra-annotateur, la taille effective est inférieure au nombre de réponses. Avec seulement les trois graines d’entraînement proposées, l’estimation de la variance entre entraînements est fragile ; les intervalles groupés peuvent être trop étroits ou rester indécis.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Post-entraînement neutre ou récompense non informative à budget de mise à jour apparié**, commun à A, B et C ; le seul témoin gelé ne sépare pas érosion par RL et érosion par mise à jour générique.
2. **Sorties ancres identiques, intercalées aveuglément dans les sessions d’annotation avant et après.** Une dérive de leurs notes rendrait tout changement temporel non comparable.
3. **Banque post-RL entièrement réservée**, distincte des exemples de formation et de rédaction des consignes, avec paires contenu/style croisées. Sans elle, la validité conditionnelle des instruments dans le régime réellement mesuré reste inconnue.

Les contrôles de croyance correcte, de source impersonnelle et de validation justifiée déjà présents dans E sont nécessaires, mais ne réparent ni l’absence de contraste avant/après dans B et C, ni ces trois défaillances.

FIN-DE-CELLULE

---

## E3-T2-critique-croisee-E.md (sha256 `5fe64df7efe67a019031da23f8aeb33e2747f2518cbcb8feb5c9aa6f42574a41`)

# Proposition E — Critique croisée de méthode

**Statuts.** Les constats sur le texte des propositions sont **VÉRIFIÉS par lecture des cellules**, sans vérification de leurs sources. Les objections et conditions de défaillance ci-dessous sont des **HYPOTHÈSES méthodologiques**, formulées conditionnellement : ce ne sont pas des résultats expérimentaux. Les seuils numériques empruntés aux conceptions restent **illustratifs**. Les constantes des équations sont mathématiques, non empiriques.

## Sur la proposition A

### (a) Défauts de méthode

**VÉRIFIÉ — Les duels ne correspondent pas aux conclusions annoncées.**

- **E1** oppose une modification conjointe de l’erreur et du gain à une modification du seul point fixe. Une modification du gain seul, de l’erreur seule, ou leur absence, échappe à ce duel. Une modification conjointe ne réfuterait pas une dissociation générale des construits.
- **E2** laisse une région de rétention sans hypothèse. Surtout, une érosion du score de persona suffit à satisfaire H_B sans changement de gain : elle ne réfute donc pas la condition d’invariance du gain invoquée dans la conclusion.
- **E3** annonce une opposition entre effets principaux de l’étape et de la persona, mais propose un seuil sur leur **interaction**. Ce ne sont pas les mêmes paramètres.

**HYPOTHÈSE — Le contrôle par consigne système ne permet pas l’attribution annoncée.** Une consigne peut produire le même comportement qu’un entraînement. L’égalité de leurs scores n’établit donc pas que le juge ne lit que le style. Il faut faire varier le style **à position comportementale constante**, puis la position à style constant.

**HYPOTHÈSE — Les contrôles d’entraînement restent confondus.** Même nombre de pas ne signifie ni même déplacement de politique, ni même information apportée. Le SFT sur les propres sorties introduit son objectif et sa distribution de cibles. L’équilibrage des préférences en validation émotionnelle modifie aussi potentiellement leur difficulté, leur longueur et leur contenu.

**HYPOTHÈSE — Deux traitements proposés peuvent masquer le biais.** Exclure les items comportant un refus sélectionne sur une conséquence du traitement. Exiger l’accord entre jugement tronqué et jugement intégral peut accepter deux instruments biaisés, ou rejeter une différence réelle située après la coupure.

**VÉRIFIÉ — Le seuil sur le gain est présenté comme un calcul issu d’un intervalle de R6.** Une largeur d’intervalle antérieur ne constitue ni un effet minimal pertinent ni un calcul de puissance du nouveau plan.

### (b) Conditions probabilistes de perte de puissance ou de non-identifiabilité

**HYPOTHÈSE — Écriture conditionnelle.** Soient \(Z\) le comportement cible, \(W\) le style, \(J\) le score du juge et \(T\) le bras.

- **Classifieur et règle lexicale.** Si
  \[
  \mathcal L(J\mid Z,W,T)=\mathcal L(J\mid W),
  \]
  alors \(J\) ne contient aucune information supplémentaire sur \(Z\) conditionnellement à \(W\). Inversement, une égalité d’AUC entre \(J\) et une règle lexicale \(h(W)\) n’implique pas cette égalité de lois. Le critère d’AUC proposé n’identifie donc pas à lui seul la variable mesurée.

- **Gain et point fixe.** Posons \(X=V+\epsilon\), \(Y=a+(1-g)V+\eta\), avec erreurs centrées indépendantes de \(V\) et entre elles. La régression de \(Y-X\) sur \(X\) donne, asymptotiquement,
  \[
  \widehat g\longrightarrow
  \frac{g\,\operatorname{Var}(V)+\operatorname{Var}(\epsilon)}
       {\operatorname{Var}(V)+\operatorname{Var}(\epsilon)}.
  \]
  Lorsque \(\operatorname{Var}(\epsilon)\gg\operatorname{Var}(V)\), les gains estimés convergent vers la même valeur indépendamment des gains véritables. Pour \(c=a/g\), l’incertitude devient non bornée lorsque les valeurs plausibles de \(g\) comprennent zéro.

- **Refus.** Avec \(Q\) l’indicateur de refus, l’analyse restreinte estime
  \[
  E[J\mid T,Q=0],
  \]
  non \(E[J\mid T]\). Si \(P(Q=0\mid Z,T)\) dépend conjointement de \(Z\) et de \(T\), les contrastes conditionnels peuvent être nuls ou inversés relativement aux contrastes marginaux.

- **Interaction E3.** Pour
  \[
  E[J\mid P,T]=\beta_0+\beta_P P+\beta_T T+\beta_{PT}PT,
  \]
  \(\beta_{PT}=0\) est compatible avec \(\beta_T\neq0\), avec \(\beta_P\neq0\), ou avec les deux. Un test portant uniquement sur \(\beta_{PT}\) ne distingue pas ces distributions.

- **Sondes.** Une AUC élevée sous \(\mathcal L_{\mathrm{construction}}\) n’impose aucune borne à l’AUC sous \(\mathcal L_{\mathrm{évaluation}}\). Si les distributions de scores conditionnelles aux deux classes y coïncident, l’AUC vaut sa valeur de hasard, indépendamment de l’AUC de construction.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — Contrôles nécessaires aux attributions annoncées :**

- **Persona versus style :** réponses à position inchangée mais ton, format et longueur modifiés, avec adjudication indépendante du maintien du sens.
- **Gain d’attraction :** données à gain nul et déplacement constant, intégrant l’erreur de mesure du score initial ; estimations du niveau initial obtenues sur des tirages indépendants de ceux utilisés dans la différence.
- **Refus :** analyse de tous les items, avec refus comme catégorie explicite, en plus de toute analyse conditionnelle.
- **Effet propre du RL :** checkpoints gelés réévalués, référence de politique et pénalités documentées par bras, répétitions indépendantes des entraînements.
- **Juges et sondes :** lots d’évaluation non utilisés pour choisir prompts, couches, seuils ou règles mécaniques.

---

## Sur la proposition B

### (a) Défauts de méthode

**VÉRIFIÉ — E3 confond deux paramètres distincts.** Dans \(\Delta=g(c-v_0)\), \(v_0\) est la valeur initiale de l’item, pas le point fixe \(c\). Les hypothèses formulées sur \(v_0\) ne testent donc pas l’attribution « persona = point fixe ».

**VÉRIFIÉ — La prédiction centrale d’E1 tombe dans la région déclarée non tranchée.** La rétention attendue de \(0,6\), **illustrative**, n’est ni la persistance ni l’effacement définis par le duel. Ce n’est pas contradictoire, mais le plan ne doit pas être présenté comme susceptible de trancher précisément son scénario attendu.

**HYPOTHÈSE — La rétention peut dépendre de l’échelle du classifieur.** Une transformation monotone conserve le classement des sorties tout en modifiant le ratio des écarts. « Conserver une fraction de persona » exige donc une interprétation de l’échelle, pas seulement une bonne AUC.

**VÉRIFIÉ — La validation du juge prend les sorties de *Sycophantic* comme cas positifs.** Or E4 cherche justement à savoir si elles sont sycophantes. Sans adjudication comportementale indépendante, la validation suppose ce qu’elle doit mesurer.

**HYPOTHÈSE — Les contrôles de longueur et de récompense sont insuffisants.** Apparier la longueur après entraînement peut sélectionner des sous-populations différentes. Une récompense aléatoire peut encore produire une mise à jour systématique via les pénalités, la référence de politique ou l’algorithme. Enfin, des gains mathématiques égaux n’impliquent pas des intensités d’entraînement égales.

**HYPOTHÈSE — La conclusion d’E4 dépasse sa mesure.** Une absence de capitulation factuelle ne réfute pas toute disposition sycophante ; elle réfute seulement l’effet factuel défini sur la distribution testée.

### (b) Conditions probabilistes de perte de puissance ou de non-identifiabilité

**HYPOTHÈSE — Écriture conditionnelle.**

- **Ratio de rétention.** Avec \(d_t=E[J\mid P,t]-E[J\mid B,t]\) et \(r=d_1/d_0\),
  \[
  \operatorname{Var}(\widehat r)\approx
  \frac{\operatorname{Var}(\widehat d_1)}{d_0^2}
  +\frac{d_1^2\operatorname{Var}(\widehat d_0)}{d_0^4}
  -\frac{2d_1\operatorname{Cov}(\widehat d_1,\widehat d_0)}{d_0^3}.
  \]
  Pour \(d_0=0\), \(r\) n’est pas défini. Lorsque l’intervalle plausible de \(d_0\) contient zéro, un intervalle borné pour \(r\) n’est généralement pas garanti.

- **Seuils et précision.** Pour un intervalle \(I_r\), aucune décision n’est possible si \(I_r\) intersecte les régions concurrentes. Augmenter les générations ne suffit pas si
  \[
  \operatorname{Var}(\widehat d_t)
  =\sigma^2_{\mathrm{entraînement}}/K+\sigma^2_{\mathrm{sorties}}/N
  \]
  et si \(K\) reste fixe avec \(\sigma^2_{\mathrm{entraînement}}>0\).

- **Validation du juge.** Si les étiquettes de validation sont \(\widetilde Z=\mathbf1\{\text{checkpoint Sycophantic}\}\), la sensibilité estimée vaut \(P(J=1\mid\widetilde Z=1)\), pas \(P(J=1\mid Z=1)\). Sans loi reliant \(Z\) à \(\widetilde Z\), la seconde quantité n’est pas identifiée.

- **Différence de différences.** Avec sensibilité \(s\), spécificité \(q\) constantes entre cellules et prévalence \(p\),
  \[
  E[J]=(s+q-1)p+1-q.
  \]
  Ainsi \(\mathrm{DiD}_J=(s+q-1)\mathrm{DiD}_Z\). Si \(s+q=1\), le contraste mesuré est nul pour toute interaction réelle. Si \(s,q\) varient entre cellules, une interaction mesurée peut exister avec \(\mathrm{DiD}_Z=0\).

- **Appariement et exposition.** Si les supports de \(\mathcal L(L\mid T)\) sont disjoints, le contraste apparié sur la longueur \(L\) n’est pas identifié. Par ailleurs,
  \[
  E[R\mid T=a]=E[R\mid T=b]
  \]
  n’impose aucune égalité entre les lois des divergences de politique après entraînement.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — Contrôles nécessaires :**

- **Calibration indépendante :** capitulations et corrections factuelles annotées sans connaître le checkpoint ; accords justifiés avec l’utilisateur, mais aussi désaccords injustifiés.
- **Rétention :** réévaluation répétée de checkpoints gelés, stabilité du contraste initial et analyse des différences brutes à côté du ratio.
- **Récompense aléatoire :** vérification des mises à jour effectivement produites ; bras sans mise à jour pour mesurer séparément la dérive d’instrument.
- **Point fixe :** générateurs à \(c\) constant et niveau initial variable, puis à niveau initial constant et \(c\) variable.
- **Sélection :** résultats marginaux sur les sorties intégrales, conservés comme analyse principale avant appariement sur la longueur.

---

## Sur la proposition C

**RAPPORTÉ — La pièce E3-T1-conception-C est absente, signalée « jamais lancée » ; aucune critique de son contenu n’est possible.**

---

## Sur la proposition D

### (a) Défauts de méthode

**VÉRIFIÉ — Les hypothèses sont complémentaires, mais la règle d’inférence reste manquante.** Découper l’espace des paramètres par un seuil ne suffit pas à classer un paramètre inconnu. Substituer l’estimation ponctuelle au paramètre imposerait un verdict même lorsque son incertitude recouvre les deux régions.

**HYPOTHÈSE — E1 ne distingue pas maintien absolu et maintien relatif.** Le ratio persona–base peut rester stable si les deux modèles perdent le même comportement. Il faut publier leurs niveaux séparés, pas seulement l’écart.

**HYPOTHÈSE — E2 soustrait des mesures dont les échelles ne sont pas nécessairement comparables.** Des points de pourcentage sociaux et factuels ne deviennent pas commensurables parce qu’ils partagent une unité. Difficulté des items, prévalence initiale, fiabilité et plafonds peuvent créer une « sélectivité » instrumentale.

**HYPOTHÈSE — Fixer le ton peut changer l’objet étudié.** Une consigne commune fixe une intervention sur le style, pas nécessairement le style produit. Une réécriture des sorties peut modifier leur position implicite. Dans les deux cas, la mesure ne représente plus automatiquement le comportement conversationnel naturel.

**VÉRIFIÉ — E3 propose des paramètres par item et graine.** Sans préciser lesquels sont partagés entre items et doses, l’identifiabilité de \(g\) et \(c\) n’est pas établie.

**HYPOTHÈSE — Les contrôles synthétiques peuvent favoriser leur propre instrument.** Si les mêmes générateurs servent à développer le juge puis à démontrer sa sensibilité, le test mesure aussi l’adaptation aux générateurs. Changer de famille de juge ne supprime pas cette fuite.

### (b) Conditions probabilistes de perte de puissance ou de non-identifiabilité

**HYPOTHÈSE — Écriture conditionnelle.**

- **Persistance relative.** Si
  \[
  \mu_{P,1}=\mu_{P,0}-a,\qquad
  \mu_{B,1}=\mu_{B,0}-a,
  \]
  alors \(R=1\) pour tout \(a\), dès que le dénominateur est non nul. Le ratio est invariant à une perte commune.

- **Sélectivité sociale.** Pour \(k\in\{S,F\}\), supposons une erreur de classification stable entre bras et \(\lambda_k=s_k+q_k-1\). Alors
  \[
  \widehat{\Delta S-\Delta F}
  \longrightarrow \lambda_S\Delta S^*-\lambda_F\Delta F^*.
  \]
  Même avec \(\Delta S^*=\Delta F^*=d\), la limite vaut \((\lambda_S-\lambda_F)d\). Sans estimation des \(\lambda_k\), le contraste latent n’est pas identifié.

- **Saturation.** Si \(P(J_k=1\mid T)\) converge uniformément vers zéro ou un dans les bras, les différences observables convergent vers zéro, même si un paramètre latent continue de varier.

- **Paramètres par item.** Pour un item à \(v_i\) fixe,
  \[
  E[\Delta_i]=g_i(c_i-v_i).
  \]
  Pour tout \(g_i'\neq0\), poser
  \[
  c_i'=v_i+\frac{g_i}{g_i'}(c_i-v_i)
  \]
  conserve la même moyenne. Si la loi résiduelle reste identique, les lois observées sont identiques : \(g_i,c_i\) ne sont pas séparément identifiables.

- **Décision autour d’un seuil.** Pour un seuil \(\delta\), si un intervalle de confiance de \(\Delta g\) intersecte simultanément \((-\delta,\delta)\) et son complément, ni invariance pratique ni modification ne sont établies. Les alternatives arbitrairement proches de la frontière ne sont pas uniformément séparables à taille finie.

- **Permutation.** Un test par permutation exige
  \[
  \mathcal L(Y\mid D,X,H_0)
  =\mathcal L(Y\mid\pi(D),X,H_0)
  \]
  pour les permutations admissibles. Si cette invariance échoue, son taux de rejet n’est pas calibré par la permutation.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — Contrôles nécessaires :**

- **Persistance :** niveaux absolus de chaque modèle et simulations de pertes communes persona–base.
- **Sélectivité :** matrices de confusion distinctes par domaine et checkpoint ; cas à contraste latent identique entre domaines, évalués séparément du développement du juge.
- **Gain :** simulations intégrant bruit du niveau initial, effets d’item, effets de graine et refus ; estimation hiérarchique identifiable plutôt que paramètres libres par item.
- **Permutations :** permutations respectant les blocs de randomisation et la dépendance des observations.
- **Extraction factuelle :** réponses sémantiquement identiques sous différents formats, vérité de référence établie indépendamment du juge et du parseur.

**HYPOTHÈSE — Exigence finale pour D :** conserver ses hypothèses complémentaires, mais ajouter une région de décision « non concluante ». Un paramètre appartient nécessairement à une région ; les données disponibles ne permettent pas nécessairement de savoir laquelle.

FIN-DE-CELLULE