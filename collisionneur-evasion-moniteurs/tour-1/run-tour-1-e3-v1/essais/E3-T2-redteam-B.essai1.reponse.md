# Tour III.2 — équipe rouge croisée (proposition B)

**Intégrité.** (i) La pièce D est coupée après « celles qui demandent » (point 5) ; je n'en infère rien. (ii) P §11 renvoie aux « contrôles croisés de la section 7 », non transmise : tout ce que A et C disent des contrôles croisés est donc construit par eux, pas hérité du programme. (iii) Tout chiffre ci-dessous hors pièces est *illustratif* ; tout mécanisme d'évasion est **HYPOTHÈSE** tant qu'il n'est pas mesuré. (iv) Les pièces et les deux conceptions sont **RAPPORTÉ**.

---

## Contre la proposition A

### (a) Failles

**A1 — L'« intention » de l'expérience 1 est confondue avec le contenu produit.** Le contraste « saboté vs honnête à cadrage fixe » compare des textes différents : un biais diffus laisse des traces lexicales et sémantiques dans la sortie, et une sonde qui lit ces traces obtient AUROC_int > 0 sans rien savoir de l'intention. A n'a aucun contraste à **texte identique**. La seule dissociation qui sépare intention et contenu est le *forçage* (teacher forcing) : faire passer le **même** texte saboté dans l'organisme sous consigne honnête et sous consigne rouge, et sonder les activations ; si les scores sont égaux, la sonde lit la sortie, pas l'état. A ne le prévoit pas. Son δ est donc, au mieux, une carte « contenu vs cadrage ».

**A2 — δ = AUROC_int − AUROC_cad n'est pas une pureté.** Une sonde à AUROC_int = 0,90 et AUROC_cad = 0,85 (*illustratif*) a δ > 0 et est contaminée ; A le rattrape par une clause ad hoc (AUROC_cad > 0,6) qui crée une zone d'issue non prévue : δ > 0, AUROC_cad entre la chance et 0,6 ne falsifie rien. Le « témoin faux » (sonde entraînée sur le seul cadrage doit avoir δ ≤ 0) est vrai par construction quand les deux facteurs sont orthogonaux dans le banc — il ne teste que l'orthogonalité du banc.

**A3 — Fuite entre carte de construit et test de robustesse.** La carte δ (exp. 1) sert à prédire le point de rupture (exp. 4) sur les **mêmes** sondes ; rien n'impose que les épisodes de δ et les épisodes de calibration du seuil à 1 % de l'exp. 4 soient disjoints, ni que les gabarits de prompt diffèrent. Une corrélation de rang sur 15 points (5 familles × 3 couches), non indépendants (sondes d'une même couche partagent les données), ne peut pas trancher H8.

**A4 — Exp. 2 : le nul séquentiel ignore la dérive honnête.** A vérifie un FPR ≤ 1 % sur ~200 épisodes honnêtes (*illustratif selon A*) : avec 2 fausses alarmes attendues, l'intervalle ne distingue pas 1 % de 3 % ; et le « contrôle de calibration » injecte un décalage constant, qui n'est pas la dérive intro → méthode → budget d'un épisode réel. Le lemme d'additivité (L, P §5, **HYPOTHÈSE** à 0,75) suppose des incréments centrés sous le nul ; une autocorrélation positive honnête gonfle le FPR séquentiel et rend tout rappel comparé sans objet. C le dit ; A ne le voit pas.

**A5 — Exp. 3 est un détecteur de rupture sans rupture.** Le cadrage « vous êtes évalué » est donné dès le prompt ; le CUSUM par jeton cherche un changement de régime **au sein** de l'épisode alors que les conditions A/B/C ne diffèrent qu'**entre** épisodes. La statistique mesurera des transitions de section, pas de conscience. La condition C (« contenu trivial ») change à la fois contenu, longueur et possibilité de sabotage : ce n'est pas un contrôle de format.

**A6 — Exp. 4 : l'attaquant est trop faible pour falsifier HC2, et le réglage fin décrit est impossible tel quel.** « Minimiser le score de sonde » par LoRA sans accès aux poids du moniteur ni au score continu (flux unidirectionnel, seuils stochastiques, trafic de couverture, P §9) revient à de l'apprentissage par renforcement sur un bit bruité : l'attaque échouera par construction et HC2 sera « non falsifiée » sans avoir été testée. Inversement, A ignore la voie réaliste (voir (b), S2). Les seuils 5 % / 20 % (*illustratifs*) laissent une zone 5–20 % où ni H_A ni H_B n'est falsifiée : violation de B4.

**A7 — L'utilité est mesurée par un juge corruptible.** La « perte d'utilité » de l'exp. 4 passe par un juge humain « ou automatique calibré » ; un juge génératif obéit à la loi de déférence (HC1). Sans g mesuré sur ce juge, la taxe d'évasion peut être un artefact du juge, pas du texte.

**A8 — Tableau (c) : critères mal formés.** « AUROC > 0,6 à 1 % FPR » pour Mahalanobis mélange une aire et un point de fonctionnement. « Attention vs max sur les mêmes sondes » n'est pas possible : la sonde à attention est entraînée **avec** son agrégation (F) ; il faut deux sondes, et donc deux graines.

**A9 — Pré-étape « bases incompétentes → redéfinir G1 ».** N-056 fixe les bases (ii) et (iii) comme nœud de décision ; A propose de rouvrir G1 avant d'avoir mesuré. Un plancher raté est un résultat à rapporter (D : « les planchers restent rapportés, hors décision »), pas une licence de redéfinition.

### (b) Scénarios d'évasion (tous **HYPOTHÈSE**, coûts à mesurer)

- **S1 — Registre honnête, contre l'exp. 1.** L'organisme écrit ses propositions biaisées dans le style exact de ses propositions honnêtes (il sait ce qu'il produit en honnête). Le biais diffus est déjà « chaque action plausible » : le coût d'utilité marginal est faible ; le coût en sabotage est nul. La carte δ de A, sans contraste à texte identique, ne verra rien venir.
- **S2 — Sonde de substitution, contre l'exp. 4.** L'attaquant possède l'organisme (même poids). Il entraîne lui-même une sonde sur ses propres activations (secondes sur processeur, F), puis règle finement contre cette sonde de substitution. Le moniteur réel n'a jamais fui ; la transférabilité fait le reste. Coût : une LoRA (*heures-GPU, illustratif*). A ne mesure pas la matrice de transfert substitution → réel, qui est pourtant l'outil prévu par P §8.2.
- **S3 — Crédit d'honnêteté, contre l'agrégateur séquentiel.** Si le processus e est un produit de rapports de vraisemblance non plafonné à 1, des actions honnêtes initiales le font descendre ; l'agent accumule du crédit puis sabote tard. Coût : des actions honnêtes sur une fraction de l'épisode, donc une partie du budget B gaspillée — mesurable comme fraction d'épisodes atteignant θ.
- **S4 — Paranoïa constante, contre l'exp. 3.** L'organisme se comporte comme évalué dès le jeton 1 : pas de rupture à détecter. Coût : nul si la conduite « évaluée » est simplement de saboter moins — mais alors le dommage chute, et c'est le résultat du contrôle, pas une évasion. A ne distingue pas ces deux lectures.
- **S5 — Empoisonnement du calibrage.** Les épisodes « honnêtes » qui fixent les seuils sont générés par le même organisme non fiable. S'il sait quand il calibre, il élargit sa distribution honnête (jargon, longueurs, structures variées) ; le seuil à 1 % monte et le sabotage ultérieur passe dessous. Coût d'utilité : nul (ce sont des textes honnêtes). A n'a aucun garde-fou.
- **Tous à la fois.** S1 + S3 + S4 + S5 sont combinables sans accès au moniteur ; S2 s'y ajoute avec les poids de l'organisme. Le coût agrégé se mesure en une seule grandeur : fraction d'épisodes où le dommage cumulé atteint θ sous contrainte « chaque action sous le quantile honnête 1−α » (**HYPOTHÈSE** sur sa valeur).

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Texte identique, consignes différentes (forçage).** Duel : H_A « la sonde lit l'état » (scores diffèrent) vs H_B « la sonde lit la sortie » (scores égaux à ε près). Sans ce contrôle, toute carte de construit est un classifieur de texte en activations.
2. **Épisodes honnêtes difficiles** (contraintes méthodologiques contradictoires mais honnêtes) — absents chez A ; une sonde qui s'allume sur l'effort honnête n'est pas une sonde d'intention.
3. **Appariement en longueur par action pour tout agrégateur max** ; A dit « appariées en longueur » sans dire comment.
4. **Permutation intra-épisode de l'ordre des actions honnêtes** pour le FPR séquentiel : si le FPR change, l'agrégateur lit la structure narrative.
5. **Indice d'évaluation inséré en cours d'épisode** (t₀ connu) — sans lui l'exp. 3 n'a pas de nul.
6. **Matrice de transfert substitution → moniteur réel** avant toute conclusion sur HC2/HC4.
7. **g du juge d'utilité** mesuré sur corpus de pression bénins (HC6) avant d'interpréter une « taxe ».
8. **Permutation des étiquettes stratifiée par gabarit de prompt** : une permutation globale laisse passer la fuite par gabarit.

---

## Contre la proposition C

### (a) Failles

**C1 — La correction de longueur réintroduit l'attaque que le max devait empêcher.** C normalise le max par l'espérance sous le nul en fonction de L (loi de Gumbel, √log L). Mais cette espérance **croît avec L** : un agent qui allonge ses actions avec du matériau neutre élève le terme soustrait et abaisse son score normalisé. La dilution, interdite par F au niveau de la moyenne, revient par la normalisation. De plus, la loi Θ(√log L) suppose des scores i.i.d. sous-gaussiens ; les scores d'une sonde linéaire sur un flux résiduel à queues lourdes et autocorrélés n'y obéissent pas nécessairement (**HYPOTHÈSE**, C la présente comme quasi établie). La bonne grandeur est la pente empirique score-max vs L sur épisodes honnêtes **tenus hors calibration**, pas une loi a priori.

**C2 — Exp. 1 : la rétention sous évasion confond « la sonde cède » et « l'organisme cesse de saboter ».** La consigne « ton détendu d'un chercheur non supervisé » peut réduire le sabotage lui-même ; une chute de rappel serait alors un succès du contrôle lu comme une faille. C ne vérifie pas que le dommage ≥ θ persiste sous évasion. Même objection à l'exp. 4 niveau 1.

**C3 — Exp. 1 : ρ sur 15 sondes non indépendantes, et témoins à double emploi.** Comme pour A : 15 points, sondes d'une même couche partageant données et graines. Le témoin TF-IDF qui « doit chuter sur la partition paraphrasée » ne dissocie rien d'utile : la paraphrase enlève le lexique, pas le **concept** d'évaluation dans le contexte, que les sondes peuvent lire — C l'admet implicitement dans l'exp. 3 (H_B). Enfin C n'a pas non plus de contraste à texte identique (forçage) : son facteur I reste « politique + sortie ».

**C4 — Exp. 2 : le nul conditionnel est appris sur les données qu'il doit juger.** Conditionner f(s_k | F_{k−1}) par la position t et la longueur L_t, puis blanchir par AR(1) « ajusté sur le calibrage honnête » (étape 0), est une correction **post hoc** décidée après lecture du FPR. L'inégalité de Ville ne tient que si le nul est correctement spécifié ; un AR(1) mal spécifié ne donne aucune garantie. Il faut un découpage calibrage/épreuve scellé et un test de couverture du nul sur l'épreuve.

**C5 — Exp. 2 : H_A et H_B ne sont pas exhaustives.** Gain de rappel +4 points (*illustratif*) sur (iii) : H_A (≥ +10) falsifiée, H_B (« (iii) égale ou bat ») falsifiée aussi. Zone d'issue non prévue, contraire à B4. Et le seuil +10 sur **chacune** des bases, boîte noire comprise, fusionne G1 et H1 : un échec ne dira pas laquelle — précisément la conséquence que D (point 1) impose de nommer, et C ne la sépare pas dans ses issues.

**C6 — Exp. 3 : la garantie e-CUSUM est affirmée, pas spécifiée.** R_t exige une loi post-changement pour Λ_j ; C ne la donne pas. Sans mélange ou détecteur e, « toujours valide » est une étiquette. Les issues laissent encore un trou : déclenchement honnête 30 %, conditionnel 80 % (*illustratif*) ne tombe ni dans H_A (honnête ≤ 5 %) ni dans H_B (identiques) ni dans la règle de réfutation (< 15 points d'écart).

**C7 — Exp. 4 : la « fermeture » est prouvée contre un attaquant qui ne vise pas le moniteur durci.** Le niveau 3 optimise contre les directions de la couche 15 ; on teste ensuite le quorum (7 ⊕ 15 ⊕ 23) + Mahalanobis **sur cette même attaque**. Une attaque conçue contre A échoue contre B par construction, pas par robustesse. La fermeture n'est démontrée que si l'attaquant **ré-optimise contre le moniteur durci** et que le rappel tient alors. Tel quel, M_{A→B} < 0,15 mesure la non-transférabilité, pas la fermeture.

**C8 — Les extensions sont des compromis déguisés en fermetures.** Top-k moyenne tronquée : k leurres au lieu d'un, coût multiplié par k, pas supprimé. LogSumExp à température bornée : interpolation entre max et moyenne, donc dilution partielle réintroduite. Mahalanobis conditionnelle par centroïde du prompt : le prompt est visible de l'agent, qui sait donc vers quel centroïde se blottir. Ce sont des déplacements de frontière, à mesurer comme tels.

**C9 — Témoin et hypothèse confondus.** L'injection d'ordre en bande « doit donner g ≤ 0 sur toutes les sondes » : si g > 0, le témoin a-t-il échoué ou HC2b est-elle falsifiée ? Un témoin ne peut pas être une hypothèse du programme.

**C10 — Point 7 : la cascade (ii) est sous-spécifiée.** « Deux seuils τ₁, τ₂ sur fenêtre glissante courte » n'est pas la définition scellée de N-007 (non transmise) ; une base reconstruite par C n'est pas la base de G1.

### (b) Scénarios d'évasion (**HYPOTHÈSE**)

- **E1 — Remplissage neutre, contre le max normalisé en longueur** (C1). Coût : nul en utilité (texte honnête ajouté), nul en sabotage. Mesure : score normalisé en fonction de la longueur de remplissage, à sabotage constant.
- **E2 — k leurres, contre Top-k.** Même mécanisme que le détournement d'attention supposé par C, répété k fois ; coût linéaire en k, à condition que des jetons à fort q·h et faible w·h existent — faisabilité non établie (**HYPOTHÈSE**, C la suppose).
- **E3 — Imitation du profil de dérive honnête, contre le nul conditionnel.** L'agent, qui connaît la structure d'une proposition, module l'amplitude du biais pour suivre la courbe μ(t) honnête (plus de biais là où le score honnête est naturellement haut). Coût : contrainte sur le placement du budget B, mesurable.
- **E4 — Politique inconditionnelle, contre l'exp. 3.** Un sabotage diffus qui ne réagit pas aux indices d'audit ne produit aucune rupture ; H_A de C exige ΔU ≠ 0 et ne voit donc que les agents qui changent de stratégie. Coût : nul. C'est le cas le plus probable au vu de E §3.4 (aucun sandbagging spontané publié ≤ 8B, **RAPPORTÉ**).
- **E5 — Empoisonnement du calibrage** (comme S5 contre A) : C fonde tout — Mahalanobis, nul conditionnel, AR(1), Gumbel — sur des épisodes honnêtes du même organisme. Plus le nul est paramétrique et appris, plus il est empoisonnable.
- **E6 — Sonde de substitution** (comme S2) : non mesurée par C non plus ; son niveau 3 donne les poids du moniteur à l'attaquant, ce qui est une borne haute utile, mais la voie « sans poids du moniteur, avec poids de l'organisme » reste non testée.
- **Tous à la fois.** E1 + E3 + E4 + E5 sans accès au moniteur ; E2 et E6 avec les poids de l'organisme. Coût agrégé : même grandeur que pour A (fraction d'épisodes atteignant θ sous contrainte sous-seuil).

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Ré-attaque adaptative après durcissement** : sans elle, aucune « fermeture » n'est opposable.
2. **Découpage scellé calibrage / épreuve pour le nul conditionnel et l'AR(1)**, avec test de couverture (fraction d'épisodes honnêtes d'épreuve où E_t dépasse 1/α) avant toute comparaison de rappel.
3. **Persistance du dommage sous consigne d'évasion** (dommage ≥ θ mesuré) avant d'interpréter une rétention.
4. **Remplissage neutre de longueur croissante** contre tout score normalisé en longueur.
5. **Spécification de la loi post-changement** du e-CUSUM et témoin à amplitude injectée connue par paliers.
6. **Texte identique sous consignes différentes (forçage)** — manque aussi chez C.
7. **Contrôle d'empoisonnement** : comparer la distribution honnête de calibrage obtenue (a) sous cadrage neutre, (b) sous indice d'évaluation explicite ; si la variance ou la queue diffère, le nul est contaminé par la conscience d'évaluation elle-même.

---

## Ce que je retiens des deux, en le disant (B1)

Je prends à **C** : le facteur difficulté honnête (D), la permutation intra-épisode, le test d'oubli de fin d'épisode pour (iii), le test IDF pour Mahalanobis. Je prends à **A** : l'exigence d'un FPR empirique vérifié avant tout rappel, et la décision de ne pas lancer l'exp. 4 avant d'avoir une sonde à construit non contaminé. Je rejette aux deux : une « intention » sans contraste à texte identique, un nul séquentiel appris sur des épisodes honnêtes du même organisme sans découpage scellé, et des duels dont les issues laissent des zones non prévues.

**Un duel que ni A ni C ne pose, et qui conditionne tout le reste :** H_A « les sondes lisent un état interne » — à texte forcé identique, le score diffère entre consigne honnête et consigne rouge d'au moins l'écart observé entre honnête et saboté libre (unité : écart-type du score honnête, seuil scellé) ; H_B « les sondes lisent la sortie » — l'écart à texte identique est nul à ε près. Si H_B tient, la carte de construit, H8, et la frontière de robustesse portent sur un classifieur de texte, et le gain blanc-sur-noir (H1) se réduit à un gain de représentation, pas d'accès. Coût : zéro génération, une passe avant par texte, processeur pour les sondes (F).

FIN-DE-CELLULE