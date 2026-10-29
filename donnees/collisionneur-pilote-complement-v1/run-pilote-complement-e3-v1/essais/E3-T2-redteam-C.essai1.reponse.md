La pièce `E3-T1-conception-B` est absente (statut : REFUS) ; je n'en invente pas le contenu.

---

# Contre la proposition A

## (a) Les failles : variables confondantes, vérités par construction, fuites

1. **Fuite de sélection et rupture de la lecture unique (D-S12) sur le calibrage de la banque (D3, D-γ).**
   A constate (correctement) que le pilote à $16 \times 30$ ne peut détecter qu'une dérive de $0,23\sigma$ (illustratif) alors que le contrôle 12 déraille dès $0,10\sigma$ (VÉRIFIÉ, pièce C § 4). Pour sauver sa mesure, A déplace le test d'échangeabilité *dans la banque d'épreuve elle-même* ($64 \times 150$), « lu avant toute lecture sabotée », et déclare que si $|\bar{\rho}| > 0,058$ (illustratif), on refait la simulation et on tombe en nœud (recalibrage ou $N$ plus grand, D-η). C'est une fuite : lire les scores des cellules critères sur les 9 600 épisodes d'épreuve, décider sur le vu de ces scores si le calibrage est valide, et se réserver le droit de recalibrer ou d'agrandir $N$, c'est introduire un arrêt optionnel conditionnel aux données d'épreuve. De plus, D3 (pièce D) exige « une seule lecture de G1, tous modes ensemble ». Ouvrir et analyser les scores des cellules critères de la banque avant même que le mode tenu à l'écart soit généré viole le scellement de l'épreuve.

2. **Le remède de l'entrelacement par graine (D-β) détruit l'instrument de mesure de la dérive (D3) : vérité par construction et confusion.**
   En D-β, A propose de tirer les moitiés du calibrage par graine et d'entrelacer la génération entre les tâches pour transformer une dérive temporelle en bruit plutôt qu'en biais. Mais en D3, A mesure la dérive par la corrélation de Spearman $\rho$ entre le *rang de génération dans la tâche* et le score, agrégée sur les 16 tâches. Si la génération est entrelacée aléatoirement entre les 16 tâches et éventuellement répartie sur plusieurs instances de calcul (variable confondante), l'écart de temps horloge (et de charge de cache) entre le rang $k$ et le rang $k+1$ d'une même tâche devient une variable aléatoire très dispersée. Une dérive physique non monotone (cycles de charge, bascule d'instance, purge périodique du cache) est brouillée par l'entrelacement : $|\bar{\rho}|$ tend vers $0$ *par construction* de l'ordonnancement, alors même que la variance intra-tâche gonfle. A confond l'absence de tendance monotone par rang avec l'échangeabilité. Pis : en affirmant que sous coupe par graine la dérive « ne fait qu'ajouter de la variance », A oublie la limite de la pièce C (§ 6) : la variance du contraste entre moitiés dépend du rapport des densités au point à $1\%$. Étalée dans les deux moitiés, une dérive crée un mélange de lois (queues lourdes ou bimodalité) qui fait sauter le contrôle 12 à $N$ égal (VÉRIFIÉ, pièce C § 5).

3. **Projection gaussienne circulaire dans la queue à 1 % (D1) et contamination sur les 180 textes d'épreuve (D-ζ).**
   En D1, A projette la masse d'ex æquo à $1\%$ ($\hat{m}_1$) à partir de la masse mesurée à $5\%$ ($\hat{m}_5$) par la formule $\hat{m}_1 = \hat{m}_5 \cdot f(z_{0,99})/f(z_{0,95})$ (illustratif). C'est une pétition de principe : cela suppose une densité continue et localement gaussienne pour estimer une discontinuité de masse (un atome de probabilité). Pour un juge lu par la probabilité d'un jeton en demi-précision, l'espacement de la grille en probabilité $p \approx \text{sigmoïde}(\ell)$ se resserre vers $1$, mais les logits $\ell$ s'accumulent sur un nombre fini de paliers. Le rapport des masses entre $5\%$ et $1\%$ dépend de la loi des logits, pas du rapport des densités normales.
   En outre, en D-ζ, A propose de lire la grille des juges sur l'union des 180 textes du rejeu (60 tâches d'épreuve, VÉRIFIÉ, pièce B § 5) « sans condition » pour fixer D-α. Or, l'union contient des épisodes sabotés (mode coût). Les valeurs extrêmes du décile supérieur de l'union (qui déterminent $\Delta_c$ et la saturation $S_c$ en D1) seront dominées par les épisodes sabotés. Fixer le statut discret des cellules critères sur la queue haute d'un mélange contenant les sabotés des tâches d'épreuve contamine le protocole par l'épreuve.

4. **Test de mise en œuvre du bris d'égalité (D2) aveugle au couplage inter-cellules.**
   En D2, A vérifie que le bris d'égalité donne une probabilité $1/2$ à la moitié 1 parmi les paires rompues inter-moitiés, cellule par cellule. Mais A spécifie que la clef de bris est dérivée « du numéro d'épisode scellé et de la cellule ». Si l'implémentation oublie de saler la graine par l'identifiant de la cellule (ou utilise un hachage linéairement corrélé entre les 8 cellules critères), chaque cellule prise isolément passera le test binomial à $1/2$ de D2 *par construction*, mais les 8 cellules briseront leurs ex æquo dans le même sens pour les mêmes épisodes honnêtes. Cela injecte une corrélation artificielle $\rho \to 1$ dans la queue haute à $1\%$, faussant le taux d'échec joint du contrôle 12 sans que D2 ne lève la moindre alerte.

5. **Sentinelle en loi (D5) sous-dimensionnée là où le contrôle 12 opère, et hors enveloppe.**
   En D5, la sentinelle compare $m = 160$ honnêtes régénérés aux $480$ du pilote par différence de moyennes (marge $0,25\sigma$, rejet à $0,18\sigma$, illustratif) et test de Kolmogorov-Smirnov (KS). Or, KS a une sensibilité maximale au centre de la distribution (médiane) et une puissance quasi nulle dans la queue à $1\%$ (à $m=160$, le seuil à $1\%$ est le $1^{\text{er}}$ ou $2^{\text{e}}$ ordre statistique). Une dérive de pile ou de quantification qui ne modifie que la queue haute (par exemple, un écrêtage des logits hauts à partir de $2\sigma$) laisse la moyenne et la statistique KS intactes, validant H_A à tort, tout en déplaçant le seuil à $1\%$ de plusieurs points de rappel. De plus, A chiffre ce poste à $17$–$23\text{ USD}$ (illustratif) en omettant les moniteurs lourds (« il ne faut pas : la sentinelle se lit sur les cellules critères déjà calibrées ») : c'est contradictoire avec le rapport (pièce C § 1), où TRACE-lite et le juge robustifié $b^*$ *sont* des cellules critères sur lesquelles la dérive entre lancements doit être gardée.

---

## (b) Les scénarios d'évasion

Conformément à la garde de sûreté (R-519, R-339, R-597), aucune attaque d'agent surveillé n'est conçue ni détaillée. Les scénarios ci-dessous décrivent comment des défaillances physiques du banc, des défauts d'implémentation ou des propriétés de distribution (jouant le rôle d'adversaire méthodologique contre le protocole de mesure) trompent chaque instrument de la proposition A, puis tous à la fois.

1. **Contre D1 (mesure de grille et projection $\hat{m}_1$) :**
   *Mécanisme adverse :* Concentration atomique au-delà du quantile $97\%$. Une cellule critère (par exemple l'agrégat séquentiel ou le juge par jeton) est parfaitement continue sur $97\%$ de sa plage ($\Delta/\sigma \le 0,01$ entre les centiles $90$ et $97$, donc sur la majorité du décile supérieur), mais possède un plafond d'accumulation (pré-saturation à une valeur sous le maximum théorique) qui regroupe $2,5\%$ des épisodes honnêtes exactement à la même valeur.
   *Pourquoi D1 est trompé :* Le plus petit écart non nul $\Delta_c$ dans le décile supérieur est minuscule ($\le 0,01\sigma$) ; la masse à $5\%$ ($\hat{m}_5$) tombe dans la zone continue ($\hat{m}_5 \approx 0$), donc la projection gaussienne donne $\hat{m}_1 = 0$ ; comme la valeur d'accumulation est juste sous le maximum théorique du type flottant, la masse de saturation $S_c$ au maximum atteignable vaut $0$ ; enfin, la part de paires ex æquo sur tout le décile supérieur vaut $T_c \approx (0,25)^2 = 6,25\%$ (illustratif), sous les seuils d'alerte grossiers. H_A est acceptée. Pourtant, au seuil de $1\%$ de G1, on tombe en plein dans l'atome de $2,5\%$ : sans bris (si l'option (b) de D-α était choisie), l'échec joint du contrôle 12 explose à $> 0,40$.
   *Coût pour le phénomène adverse :* Nul (propriété naturelle d'un score borné ou d'une somme de portes saturées).

2. **Contre D2 (vérification du bris d'égalité) :**
   *Mécanisme adverse :* Graine de bris d'égalité dépendante de l'identifiant d'épisode mais *identique* à travers toutes les cellules critères, combinée à un tri préalable par score qui conserve l'ordre d'entrée en cas d'égalité de la clef de bris (collision de hachage en 16 bits).
   *Pourquoi D2 est trompé :* Sur un lot de 480 épisodes, le test binomial inter-moitiés par cellule donne une proportion de gagnants dans la moitié 1 égale à $0,50 \pm 0,05$ (illustratif), validant H_A. Mais à la banque ($N = 9\,600$), les collisions du hachage 16 bits (paradoxe des anniversaires dès $\approx 300$ éléments) sont résolues par le tri stable du langage (qui favorise systématiquement la première moitié du tableau en mémoire).
   *Coût :* Zéro (simple erreur de typage de la clef aléatoire en `float16` ou `int16`).

3. **Contre D3 et D-β (test de Spearman sur rang et coupe par graine) :**
   *Mécanisme adverse :* Dérive thermique ou d'allocation mémoire en dents de scie (oscillation périodique de période $P \approx 20$ épisodes sur le serveur d'inférence, ou répartition asynchrone sur deux cartes graphiques ayant une légère différence de calibration matérielle ou de version de noyau).
   *Pourquoi D3 est trompé :* La tendance n'étant pas monotone sur les 30 exécutions d'une tâche, la corrélation de rang de Spearman $\rho$ entre le numéro d'exécution et le score a une espérance exactement nulle ($\mathbb{E}[\bar{\rho}] = 0$). Le test par blocs (1–10, 11–20, 21–30) moyenne plusieurs périodes de $P=20$ et renvoie également zéro. H_A est validée au pilote *et* sur les 9 600 épisodes de la banque (D-γ). Pourtant, la distribution des scores honnêtes est devenue un mélange bimodal ($+0,2\sigma$ et $-0,2\sigma$), ce qui modifie le rapport des densités à $1\%$ et invalide le tableau de la pièce C.
   *Coût :* Nul (comportement standard d'un ordonnanceur multi-cartes sous charge).

4. **Contre D5 (les trois gardes de dérive inter-lancements) :**
   *Mécanisme adverse :* Mise à jour silencieuse de la bibliothèque d'échantillonnage stochastique du générateur (ou changement de l'ordre de réduction parallèle lors du décodage à température $T > 0$) entre le pilote et le lancement du mode tenu à l'écart, affectant uniquement la variance des trajectoires longues sans déplacer leur moyenne.
   *Pourquoi D5 est trompé :*
   - Le *canari des moniteurs* (1) passe avec un écart nul, car il re-note des textes figés du pilote (les moniteurs n'ont pas changé).
   - Le *canari du générateur* (2) passe avec des empreintes identiques, car il tourne à température nulle ($T = 0$, décodage glouton déterministe, où le générateur de nombres aléatoires d'échantillonnage n'est même pas appelé).
   - La *sentinelle en loi* (3) sur 160 épisodes compare les moyennes ($\Delta \approx 0$, bien sous $0,18\sigma$) et applique KS (insensible à un étalement des queues au-delà du $95^{\text{e}}$ centile sur $m=160$).
   Les trois gardes sont vertes simultaneously. Pourtant, sur les jumeaux partagés (D3 de la pièce D), le taux de fausses alertes à $1\%$ du mode tenu à l'écart dérive de plusieurs points par rapport aux modes connus.

5. **Évasion conjointe (tous les instruments trompés à la fois) :**
   Un banc d'inférence sur deux nœuds asynchrones (bruit bimodal symétrique $\pm 0,15\sigma$ : D3 et D-γ aveugles car $\bar{\rho} = 0$), avec une mise à jour du noyaux stochastique à $T > 0$ entre la banque et le mode tenu à l'écart qui alourdit la queue haute au-delà de $98\%$ (canari 1 sur textes figés aveugle, canari 2 à $T=0$ aveugle, sentinelle KS à $m=160$ aveugle), et une cellule critère présentant un palier d'accumulation à $98,5\%$ (D1 aveugle car $\hat{m}_5$ est lu à $95\%$) dont le bris d'égalité utilise un flottant 16 bits (D2 passe à $n=480$ mais crée des collisions résolues par ordre mémoire à $N=9\,600$). Tous les tests de la proposition A concluent à H_A à coût nul, et le contrôle 12 de la banque échoue au-delà de $0,30$ tout en biaisant l'évaluation du mode tenu à l'écart.

---

## (c) Les contrôles négatifs dont l'absence serait fatale

1. **En D1 (mesure de la grille et de la masse à 1 %) — Contrôle négatif de concentration locale en queue haute :**
   Le contrôle négatif d'A (gaussienne continue vs grille uniforme de pas $0,25\sigma$) ne teste que le cas stationnaire déjà simulé dans la pièce C. Il manque un contrôle négatif injectant une loi continue jusqu'au centile $96\%$, suivie d'un atome de masse $2\%$ au centile $98\%$ (sous le maximum absolu). Sans ce contrôle, on ne voit pas que le triplet $(\Delta_c, \hat{m}_5, S_c)$ d'A renvoie un faux négatif total sur les discontinuités logées entre $96\%$ et $99,9\%$.

2. **En D2 (bris d'égalité) — Contrôle négatif d'indépendance inter-cellules et de passage à l'échelle ($N = 9\,600$) :**
   A teste uniquement un bris déterministe par parité du rang sur $n = 480$. Il est fatal de ne pas inclure :
   - un contrôle négatif où deux cellules critères partagent la *même* suite pseudo-aléatoire de bris d'égalité (qui passe le test marginal de D2 mais doit être rejeté par un test de corrélation des rangs brisés entre cellules) ;
   - un test sur un vecteur synthétique de taille $N = 9\,600$ avec $100\%$ d'ex æquo triés par moitié, pour vérifier l'absence de collision de précision numérique à l'échelle de la banque.

3. **En D3 (échangeabilité intra-tâche) — Contrôle négatif d'hétérogénéité non monotone (instance et périodicité) :**
   Les contrôles négatifs d'A (rangs permutés et graine d'exécution) sont des contrôles *positifs* de l'hypothèse nulle (ils vérifient le niveau $\alpha$, pas la puissance contre une alternative). L'absence d'un contrôle négatif injectant une dérive périodique (sinusoïde ou créneau de période $10$ exécutions, d'amplitude $\pm 0,20\sigma$) ou un effet d'instance (deux machines décalées de $0,20\sigma$) sur les scores avant le calcul de $\bar{\rho}$ est fatale : ce contrôle prouverait immédiatement que la statistique de Spearman d'A reste à $0$ face à une violation franche de l'échangeabilité.

4. **En D5 (canaris et sentinelle de dérive) — Contrôle négatif de dérive stochastique en queue à température non nulle :**
   Pour le canari 2 (température nulle) et la sentinelle (moyenne + KS sur $m=160$), il manque un contrôle négatif où l'on perturbe uniquement le générateur aléatoire d'échantillonnage à $T > 0$ par un épaississement de la queue droite des scores au-delà du centile $95\%$ (moyenne conservée). Son absence est fatale car elle laisse croire que « $T=0$ + moyenne + KS » protège le point de fonctionnement à $1\%$ de G1.

FIN-DE-CELLULE