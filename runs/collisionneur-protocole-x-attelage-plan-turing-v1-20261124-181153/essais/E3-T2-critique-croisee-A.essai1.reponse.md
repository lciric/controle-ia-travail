# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces.** Le bloc FAITS est identique au bloc QUESTION (même empreinte) : il ne contient aucun fait étiqueté, donc aucun VÉRIFIÉ. Les pièces B, C, D et E sont présentes et complètes ; ma conception du tour III.1 n'est pas transmise et je ne m'y réfère pas.

**Statut.** Tout ce qui suit est HYPOTHÈSE (analyse de méthode). Les nombres sont recalculés à partir des paramètres illustratifs des pièces : ils sont **illustratifs**.

**Notations.**
- p : probabilité qu'un tirage de référence atteigne une classe ; M : nombre de tirages de référence.
- φ : taux de fausses alertes par idée ; m : nombre d'idées soumises par run.
- π : taux de succès par problème ; q : probabilité d'une paire discordante.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **E4 est en partie vrai par construction.** L'étroitesse n est définie relativement à Q, « le modèle unique à température 1 », et le bras 4 est ce même modèle en best-of-N. Avec k tirages, P(bras 4 atteint une classe telle que n ≥ η) ≤ k·e^(−η). Le succès de la ligne de base est donc plafonné par la définition, et tout générateur dont la loi diffère de Q gagne sans être meilleur.
2. **Le nombre de candidats est une variable confondante.** succ_C vaut 1 si « au moins une idée » passe, sans plafond de nominations. La probabilité de fausse réussite par run est 1 − (1 − φ)^m. Avec φ = 0,05 (seuil de B) et m = 50, elle vaut ≈ 0,92. Le bras le plus prolixe gagne.
3. **E1 est tautologique.** K est construit à partir de la loi plantée, donc d est élevé par construction. Les leurres sont stériles par construction et la permutation s'effondre par construction. E1 valide le code, pas le construit. Seules des lois vraies non plantées échapperaient à cette circularité.
4. **E2 souffre d'une troncature.** Si les classes comparées proviennent des tirages des Q, une classe vue par Q₁ seul a un n fini sous Q₁ et censuré sous Q₂. Cela induit mécaniquement une corrélation négative (sélection de type Berkson).
5. **E3 a une étendue restreinte.** L'échantillon est tiré de Q, donc les classes rares y sont quasi absentes. De plus d est ajusté sur la complexité et n ne l'est pas. Si la complexité covarie avec n, ρ(n, d) est en partie mécanique.
6. **E8 est circulaire.** La règle « faible couverture sous Q » est une composante du critère de succès (n ≥ η sous Q). La permutation des étiquettes ne détecte pas cette circularité.
7. **La canonicalisation n'est évaluée que d'un côté.** « Fusionner ≥ 98 % des paraphrases » est satisfait par une canonicalisation constante. Le taux de fausses fusions n'est pas exigé.
8. **E7 n'apparie pas les cibles.** Présentes et absentes du corpus diffèrent en ancienneté, notoriété et simplicité. Un rapport ≥ 3 ne sépare pas le rappel de la difficulté.
9. **B4 n'est pas respecté partout.** E2 (0,3 < ρ < 0,7), E3 (0,1 < ρ < 0,5 et ρ < 0) et E5 (récupération entre 20 % et 80 %) ont des zones où aucune hypothèse n'est falsifiée.
10. **Le contrôle de profondeur est insuffisant.** Une « constante perturbée » est une idée fausse. Elle ne dit rien d'une idée vraie mais inerte.

### (b) Pertes de puissance

- **Étroitesse.** Avec zéro occurrence sur M tirages, l'estimateur plafonne à ln(M/3), soit 9,2 nats pour M = 30 000. Si η dépasse ce plafond, le critère est indécidable. Si la loi de p parmi les classes valides concentre sa masse sous 1/M, l'estimateur est presque constant. Les ρ de E2 et E3 sont alors dominés par les ex æquo, et le plafond inter-graines de B tombe lui-même sous 0,7.
- **E1.** La valeur prédictive positive vaut sens·π / (sens·π + φ(1 − π)). Avec une prévalence de 0,01 et les seuils de B (0,8 et 0,05), elle vaut ≈ 0,14. Les seuils de B ne suffisent donc pas à cette prévalence.
- **E4.** La puissance du test de McNemar dépend de n·q. Si les deux taux de succès tendent vers 0, q tend vers 0 et les 118 problèmes ne tranchent rien. Par ailleurs l'enveloppe max_b prise par problème a une espérance supérieure au max des espérances, et l'écart croît avec la variance inter-graines.
- **Profondeur.** d n'a pas de variance si la probabilité que S résolve K_test sans x est proche de 0 ou de 1.
- **E5.** La « part du gain récupérée » est un quotient. Si l'intervalle du gain de E4 approche 0, l'intervalle du quotient n'est plus borné.
- **E7.** Les modèles à données ouvertes sont petits. Si (taux de succès sur cibles absentes) × (nombre de cibles absentes) reste sous quelques unités, le rapport est non estimable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Bras « différent mais pas meilleur ».** Une autre famille de force inférieure ou égale, ou Q perturbé. S'il gagne E4, la mesure est une distance à Q. S'il perd, l'objection 1 tombe.
- **Bras « spam ».** m idées valides, rares et aléatoires, avec le même m que le système. succ doit rester proche de 0.
- **Paires proches mais distinctes**, pour mesurer les fausses fusions.
- **Idée vraie mais inerte, et table recopiant K_train**, au niveau de d.
- **Référence Q′ disjointe** de celle qui sert à choisir les régions (E8).

---

## Sur la proposition C

Je reprends telle quelle sa règle commune (T > 0 contre T ≤ 0, exhaustive) et sa critique permutée. Ce sont les deux éléments que je réutiliserais.

### (a) Défauts de méthode

1. **Dilemme entre référence et ligne de base.** « Étroite » exige max_r p_r < τ, et r inclut un solo avec outils. Deux cas se présentent :
   - Si cette référence coïncide avec le solo gelé du duel, alors π_solo ≤ K·τ par définition (K = nombre de classes qualifiées par monde). Le duel devient un test à un échantillon : π_sys > 0,05 + Kτ.
   - Si elle en diffère (le solo gelé inclut la recherche arborescente, la référence archivée non), « étroit » n'est plus relatif à la meilleure recherche ordinaire.
   
   C ne dit pas lequel des deux cas s'applique.
2. **Classe extensionnelle, profondeur intensionnelle.** Une table de vérité et une loi coïncident sur tout le domaine fini : elles forment la même classe. Mais le gain du résolveur dépend du représentant fourni (longueur, coût d'appel). On ne sait pas à quel représentant le placebo est apparié. d n'est pas une fonction de la classe.
3. **Profondeur plantée.** Si les problèmes aval sont générés à partir de la règle plantée, toute règle vraie non plantée a d ≈ 0 par construction. La clause « accepter les règles non plantées » vaut pour la vérité, pas pour la profondeur.
4. **L'audit à 3 330 négatifs est soit redondant, soit infaisable.**
   - En micromonde exhaustif, la vérité et l'identité sont exactes. Les seules erreurs sont celles des bornes, déjà fixées par α. L'audit ne détecte que des bogues.
   - Hors exhaustif, l'oracle qui étiquetterait ces négatifs n'existe pas.
   
   De plus le taux de fausses alertes est estimé sous la loi des négatifs d'audit. Le calcul de Bayes s'applique à la loi des sorties de chaque bras. Rien n'égalise les deux.
5. **Nomination unique.** π = P(trouver) × P(nommer | trouver). La rareté est cachée, à juste titre, donc la nomination sur l'axe « étroit » se fait à l'aveugle. La mesure porte autant sur la sélection que sur la recherche, alors que la question dit « finds ».
6. **Sélecteur de régions.** Le descripteur « nombre de sous-problèmes partageant une structure » est une composante mécanique de d (gain sur des problèmes aval partageant une structure).

### (b) Pertes de puissance

- **Sonde de rareté.** La sensibilité vaut E[(1 − p)^M | p < τ]. Avec M = 300 et p = 0,005, elle vaut ≈ 0,22. Atteindre 0,8 exige p ≤ 7,4·10⁻⁴. Le seuil effectif est donc ≈ 13 fois plus bas que τ = 0,01. Avec une correction simultanée sur c classes et r politiques, il faut M ≥ ln(c·r/α)/τ.
- **Dossiers non résolus.** Si la probabilité de non-résolution diffère entre bras d'une quantité au moins égale à l'écart attendu g, les bornes au pire cas et au meilleur cas encadrent 0. Le harnais ne tranche pas, quel que soit n.
- **Critique permutée.** Elle perd toute puissance si la critique utile est générique, c'est-à-dire si son effet est indépendant du dossier. On conclurait « effet de procédure » alors que la critique contribue.
- **Duel principal.** n ≈ 6,2·q/g². Sous le cas 1 du dilemme, q ≈ π_sys. Le duel n'est jugeable que si π_sys·n dépasse quelques dizaines.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Invariance au représentant.** Même classe, trois représentants, d constant. Sinon d mesure le codage.
- **Retrait d'une référence à la fois.** Le verdict doit survivre au retrait ou au remplacement du solo de référence.
- **Bras « différent mais pas meilleur »**, comme pour B.
- **Audit exhaustif des sorties réelles de chaque bras**, par échantillon aléatoire, et non de négatifs fabriqués.
- **Monde à deux règles profondes dont une seule est documentée comme plantée.** La seconde doit être créditée.

---

## Sur la proposition D

**Remarque de statut.** D étiquette [VÉRIFIÉ] des choix de conception et des affirmations empiriques que les FAITS ne contiennent pas. Exemples : « garantissant zéro mémorisation littérale » ; « exposer N pousse vers l'obfuscation ». Je ne modifie pas ces statuts. Je signale qu'aucune pièce transmise ne les soutient.

### (a) Défauts de méthode

1. **Le seuil d'étroitesse est collé au plafond.** Avec M₀ = 1 000 et zéro occurrence, la borne de Clopper-Pearson donne N ≈ 5,81 nats. Avec une seule occurrence, N ≈ 5,35, sous τ_N = 5,5. « Étroit » équivaut donc à « jamais vu en 1 000 tirages ». La mesure est binaire, et toute classe non échantillonnée est étroite, quelle que soit sa nature.
2. **Exp. II est vraie par construction contre BestOfN-Mono.** Le plafonnement est celui décrit pour B. L'ablation (iv), homogène contre hétérogène, « démontre » la diversité par définition : une classe courante pour la seconde famille et rare pour μ₀ compte comme étroite. D ne dit pas non plus comment ses deux références (modèle seul, énumérateur) se combinent.
3. **D_MDL est biaisé et extensif.**
   - Le max(0, ·) par régime donne à une loi nulle une espérance d'environ 0,40·R·σ, où σ est l'écart-type du gain par régime. La troncature masque aussi les régimes où la loi est fausse.
   - Le gain en nats croît linéairement avec la taille des D_r. Avec assez de points, τ_D = 35 nats est franchi par une amélioration minuscule. Le seuil mesure la taille du jeu de test.
   - K_L([x]) porte sur quel représentant de la classe ? D n'est pas invariant par classe.
4. **Exp. IV est circulaire.** S_region est calculé sur les résidus des références simples. Un fort résidu signifie que la recherche ordinaire échoue, donc que N est élevé. Par ailleurs l'« existence d'une solution » n'est connue qu'en monde planté, où le concepteur fixe à la fois S_region et l'existence. L'OR est choisi par le générateur de mondes.
5. **Porte 5 : fuite entre construction et évaluation.** Les transformations testées (commutativité, termes nuls, renommage α, code mort) sont les règles de réécriture du quotient par e-graphes. Le taux de 0,98 est acquis d'avance.
6. **Le plan de puissance contredit la règle de décision.** Les 100 problèmes de la phase IV (0,05 → 0,18) correspondent à un test contre 0. La règle impose un test contre δ_min = 0,10. L'écart utile est alors 0,03 et n ≈ 1 900. En phase II, avec 60 problèmes et q = 0,3, la puissance de 0,8 n'est atteinte que pour un écart vrai ≥ 0,30. « Échoue à battre → arrêt du programme » confond alors non concluant et réfuté.
7. **Exp. III : ΔN est une médiane de valeurs censurées.** Si plus de la moitié des candidats retenus ont zéro occurrence dans les deux bras, ΔN = 0 identiquement et H_A est falsifiée par construction. La zone ΔZ > 0 avec 0 ≤ ΔN < 0,7 n'est attribuée à aucune issue.
8. **Exp. VI.** Auditer « un sous-échantillon des Ĵ = 1 et Ĵ = 0 » estime les valeurs prédictives, pas (TPR, FPR). L'inversion exige la prévalence et une correction du biais de vérification (Begg & Greenes, 1983, *Biometrics*, « Assessment of diagnostic tests when disease verification is subject to selection bias »). Le critère FPR_g ≥ π_g suppose connu π_g, qui est l'inconnue.

### (b) Pertes de puissance

- **Étroitesse.** La sensibilité vaut (1 − p)^M₀. Pour p = 0,002 (classe réellement étroite, 6,2 nats), elle vaut ≈ 0,135. Atteindre 0,8 exige p ≤ 2,2·10⁻⁴, soit ≈ 8,4 nats. Le seuil effectif est à 3 nats du seuil affiché.
- **Exp. I.** Le score I[N ≥ τ_N]·D est nul pour la plupart des classes. Le τ de Kendall est gouverné par la proportion de zéros et devient non jugeable si P(N ≥ τ_N) est proche de 0 ou de 1. Sur le contrôle négatif, l'écart-type de τ sous indépendance pour n = 200 est ≈ 0,048. Le critère |τ̄| ≤ 0,08 échoue par hasard ≈ 9 % du temps, hors ex æquo.
- **Exp. VI.** Démontrer FPR < 0,01 sur 500 négatifs exige au plus une alerte. Un juge de FPR vrai 0,005 passe avec une probabilité ≈ 0,29. Par ailleurs la variance de l'estimateur de Rogan-Gladen croît en 1/(TPR − FPR)², et l'estimateur devient négatif quand π approche de 0.
- **Exp. IV.** Si la prévalence dans la strate S = 0 est ≤ 0,05, on attend au plus 3 événements sur 60. L'intervalle de l'OR couvre plusieurs ordres de grandeur.
- **Profondeur des lemmes.** La variation du nombre de pas d'un prouveur déterministe après ajout d'un lemme quelconque n'est pas centrée en 0 et a des queues lourdes. Sans loi nulle empirique, τ_D n'a pas de taux d'erreur.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Bras mono-modèle de la seconde famille**, seul, dans Exp. II. S'il « bat » l'enveloppe, N mesure la distance à μ₀.
- **Loi nulle de D** : lois ou lemmes vrais mais non pertinents, de même K, soumis au même R et aux mêmes tailles de D_r.
- **Obfuscations hors conception** : rédigées par un tiers ou par le générateur lui-même, hors des règles de l'e-graphe.
- **Répétition avec M₀ doublé.** La proportion de classes « étroites » ne doit pas changer au-delà de ce que prédit (1 − p)^M₀.
- **S_region recalculé sur une référence disjointe** de μ₀.

---

## Sur la proposition E

**Remarque de statut.** E utilise des doubles étiquettes (« VÉRIFIÉ/RAPPORTÉ », « OBSERVÉ-NON-AUDITÉ / HYPOTHÈSE ») et un « RAPPORTÉ » sans source (« invariance de représentation violée »). Ces statuts sont ambigus et je ne les tranche pas.

### (a) Défauts de méthode

1. **L'estimande d'étroitesse est double.** R est défini comme min_Q(−log₂ p̂_Q) « ou » min_Q B₀,₅. Ce sont deux quantités, et rien ne dit laquelle sert. Le budget médian de première atteinte est censuré à droite pour toute classe étroite. Et p̂ = 0 donne R infini : aucun estimateur n'est spécifié pour zéro occurrence.
2. **U(P, B) est un maximum sur toutes les sorties.** Même sous hypothèse nulle, l'espérance du maximum de m profondeurs bruitées croît comme σ·√(2 ln m). E écarte le « maximum brut » puis le reprend derrière un filtre. m diffère d'un facteur ≈ 10⁴ entre énumérateur et LLM (ordres de grandeur de E). C'est une variable confondante.
3. **Le contrôle négatif de E5 n'est pas jugeable sous la métrique de E.** En petit espace énumérable, la probabilité d'atteinte par l'énumérateur vaut 1, donc R = 0 < τ_R et U ≡ 0 pour tous les bras. « L'énumérateur doit battre les LLM » ne peut pas s'observer sur U.
4. **E3 est circulaire et sous-dimensionné.** Le descripteur « entropie d'échec du modèle unique » sélectionne les familles où la ligne de base échoue, puis on y mesure U_multi − U_base. L'unité pertinente est la famille (2 contre 2). Les 40 problèmes par famille sont des pseudo-réplicats. Le contraste « petit combinatoire » est prédit par n'importe quelle taxonomie.
5. **E2 fusionne trois questions.** Invariance au codage, biais du juge et contamination sont réunis dans un seul H_A. Son rejet ne dit pas laquelle échoue.
6. **Δ_mém confond mémoire et notation.** Renommer un problème dégrade aussi le raisonnement en notation inhabituelle. Le « contrôle négatif » proposé (problèmes volontairement fuités) est un contrôle positif.
7. **E4 teste l'utilité du retour, pas l'intégrité de la mesure.** La seule condition qui menace la mesure (fuite de R) est rangée en « contrôle ». R y est remesuré contre les mêmes références que celles qui ont fui.
8. **La règle de décision est incohérente.** Elle contraste avec max_b U_b (une seule comparaison) et ajoute Holm « sur l'ensemble des baselines ». Une enveloppe par problème n'est pas une ligne de base réalisable.
9. **L'estimation de R n'est pas budgétée.** Aucun tirage de référence n'apparaît dans les coûts. Avec p ≈ 10⁻³, il faut ≈ 3 000 tirages par problème et par référence.
10. **A/A.** E1 parle de « deux graines identiques », ce qui est déterministe donc trivial. La table (c) dit « graines distinctes ». La pièce se contredit.

### (b) Pertes de puissance

- **U est à inflation de zéros.** Les seuils en unités de σ (0,20σ, 0,30σ) reposent sur un σ estimé sur les mêmes données et dominé par les rares valeurs non nulles. Le nombre de problèmes informatifs est N·P(Δ_P ≠ 0). Avec π = 0,05 et N = 60, il y en a 3. Le calcul « d = 0,5 → N ≈ 50–60 » suppose des différences quasi normales.
- **|δ_style| ≤ 0,05σ sur 200 paires.** La demi-largeur de l'intervalle à 95 % vaut 1,96·√(2(1 − r)/200). Elle ne passe sous 0,05 que si la corrélation intra-paire r ≥ 0,935. En deçà, le critère se décide par le bruit.
- **PPI.** La validité suppose des étiquettes d'oracle tirées au hasard dans la même loi que les non étiquetées, par bras. Des experts ne sont pas un oracle. Le gain d'efficacité est de l'ordre de 1/(1 − ρ²), où ρ est la corrélation entre juge et vérité (variante à pondération optimale : référence à vérifier). Pour ρ ≤ 0,5 il est ≤ 1,33. À prévalence 0,01, n étiquetés donnent 0,01·n positifs.
- **E1.** L'AUROC exige un score scalaire, alors que (R, D) est non compensatoire par choix de E. L'AUROC est aussi insensible à la prévalence. Avec φ = 0,05 et π = 0,01, la valeur prédictive positive est ≈ 0,14, comme pour B.
- **AUDC.** Si les courbes se croisent, le signe de l'aire dépend de l'échelle de la grille (linéaire ou logarithmique).

### (c) Contrôles négatifs dont l'absence serait fatale

- **Loi de U sous hypothèse nulle à m apparié.** Un bras « spam » émet m idées valides, rares et sans conséquence. U doit rester ≈ 0 pour le m de chaque bras.
- **Panel de référence Q′ tenu à l'écart**, jamais utilisé pour la conception, la sélection ou la fuite de E4. La hausse de R sous fuite doit disparaître sous Q′, sinon elle n'est pas un artefact.
- **Renommage sur problèmes certainement inédits.** Il donne le coût pur de la notation, à soustraire de Δ_mém.
- **Descripteurs de E3 calculés sur un modèle et des graines disjoints** de la ligne de base du contraste.
- **Régime négatif jugeable.** L'énumérateur doit y gagner sur une quantité non identiquement nulle, par exemple D seul.

FIN-DE-CELLULE