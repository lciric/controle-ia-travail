# Cellule C — Tour III.2 : Équipe rouge croisée sur P-26

Convention de statut : **VÉRIFIÉ** = lisible dans le code (pièce A) ou les textes de décision (pièce E) ; **RAPPORTÉ** = chiffre ou constat des pièces B, C, D ; **OBSERVÉ-NON-AUDITÉ** = affirmation d'auteur non recoupée ; **HYPOTHÈSE** = déduction, critique ou scénario proposé ici. La pièce F n'est pas servie (déclaré dans les faits).

---

## Contre la proposition A

### (a) Les failles : variables confondantes, vérités par construction, fuites

1. **A10 et le « lot honnête séparé » (point 3) : destruction mécanique de la surmartingale et du temps d'arrêt (VÉRIFIÉ sur le code, HYPOTHÈSE sur l'effet).**
   A propose d'injecter des « unités honnêtes seules » dans la partie d'épreuve pour monter $n_h$ à $\approx 200$ ou $500$ sans payer de sabotés, en affirmant que cela « n'exige aucun changement de code » parce que `contrastes` saute les unités sans sabotés et `ecarts_faux_positifs` garde celles à honnêtes (VÉRIFIÉ, `monde_banque_scores.py`, l. 148–164).
   Or, dans `pari_apparie.evaluer` (l. 210–222, VÉRIFIÉ), la boucle tourne sur `n_total = max([n] + [len(g) for g in gardes.values()])`, et à chaque indice $t \ge n$ (où $n$ est le nombre d'unités sabotées), le contraste vaut `traj[min(t, n - 1)]`, c'est-à-dire sa **valeur finale figée** $W^{\text{contraste}}_{n-1}$.
   - **Vérité par construction / Variable confondante** : si $n = 64$ unités sabotées et $n_h = 200$ unités honnêtes (les 64 appariées + 136 honnêtes seules), alors de $t = 64$ à $t = 199$, le processus de contraste est constant ! Si les contrastes ont franchi le seuil à $t \le 64$ mais pas la garde, la fiche attend simplement que la garde franchisse le seuil sur les 136 unités supplémentaires.
   - **Violation de la filtration (K7-6)** : l'ordre secret (`ordre_secret`, l. 139) mélange toutes les unités de la partie. Le rang $t$ de la garde ne correspond plus au rang $t$ du contraste dès la première unité sans saboté. Plus grave : arrêter au premier $t \le n_h$ où $\min(\text{contraste}[\min(t, n-1)], \text{garde}[t]) \ge \text{seuil}$ revient à lire la garde sur un horizon plus long conditionnellement au fait que le contraste a déjà réussi sur son horizon court. Le code le signale lui-même (`engagement_apparie.py`, l. 21 : « espérance au franchissement joint non garantie $\le 1$ », VÉRIFIÉ). A cite A10 comme une simple « réserve » mais construit toute sa stratégie d'échantillonnage (§ 3 et § d) en maximisant l'asymétrie $n_h \gg n$, là où K7-6 est le plus violemment enfreint.

2. **Fuite entre construction et évaluation dans E1 et le point 4 (HYPOTHÈSE).**
   Dans son expérience E1 (« Muette ou non »), A définit la paire nulle comme « la cellule A calibrée sur la moitié 1 contre la même cellule calibrée sur la moitié 2 (`jumeau_calibre`) ».
   - **Variable confondante** : la variance de $g(t) = f_{A_1}(t) - f_{A_2}(t)$ entre deux moitiés de calibrage d'un **même** moniteur $A$ est presque nulle dès que les deux seuils $s_1$ et $s_2$ sont proches (si $s_1 = s_2$, $g(t) = 0$ identiquement sur toute unité !). Dans la vraie garde de G1, $g_j(t) = f_A(t) - f_{B_j}(t)$ oppose un moniteur boîte blanche $A$ (sur sondes internes) à un moniteur boîte noire $B_j$ (sur texte) : même à $E[g_j] = 0$, leurs alertes sur les épisodes d'une unité sont peu corrélées, donc $\text{Var}(g_j)$ est maximale.
   - **Vérité par construction** : tester la non-mutité (H_A : puissance $\ge 0,8$) sur le jumeau calibré revient à tester le plancher sans bruit ($g \approx 0$ partout). H_A sera validée par construction dès que $n_h \ge 144$ (ou 93), masquant totalement la perte de puissance due à la variance inter-moniteurs et à la surdispersion d'unité (GD4-01, RAPPORTÉ).
   - **Fuite au point 4** : A utilise `max_j Δ_j = |taux_calibrage_A - taux_calibrage_Bj|` comme seul biais de planification toléré. Mais avec le bris d'égalité aléatoire (P-15, pièce D : « scellé d'office sur toutes les cellules critères », RAPPORTÉ), les ex æquo disparaissent et `taux_calibrage` vaut exactement $(j-1)/n$ pour **toutes** les cellules (`seuil`, l. 113–117, VÉRIFIÉ). Alors $\Delta_j = 0$ par construction ! La règle de A dégénère en « biais = 0 toujours », aveugle au décalage de distribution entre calibrage et épreuve.

3. **Le levier $m_c = 1$ ou $2$ (A3, point 1) : confusion entre le code et le protocole (HYPOTHÈSE).**
   A propose de baisser le seuil de 160 à 20 en fixant $m_c = 1$ au motif que D-S10 dit « famille propre à la porte » (RAPPORTÉ, pièce E). Mais D-S10 dit « intersection-union sur les modes mesurés, famille propre à la porte » et la pièce B v1 (§ 2) ainsi que la pièce D (P-26) parlent de « huit critères » ($m = 8$, RAPPORTÉ). Si la porte G1 évalue $m_c$ critères ou variantes en parallèle dans sa famille propre, fixer $m_c = 1$ par décret pour acheter de la puissance viole la règle `Course.entrer` (`len(fiches)`, l. 308, VÉRIFIÉ) : dans le code, `m_c` n'est pas un paramètre libre dans `Course`, c'est `len(fiches)` ! On ne peut réduire `m_c` à 1 que si une seule fiche entre dans la famille.

4. **Domination de F2 par F1 (point 1 et E3) : erreur de signe sur la définition du « pire comparateur » (VÉRIFIÉ par dérivation).**
   A écrit pour F2 : processus de $1 + \lambda(\delta - \max_j g_j(t))$, et en déduit que F2 est dominée trajectoire par trajectoire par F1 ($\min_j$ des processus de $g_j$). C'est algébriquement vrai si le maximum est pris **unité par unité** ($\max_j g_j(t)$), car par concavité et monotonie, $\prod_t (1 + \lambda(\delta - \max_j g_j(t))) \le \min_j \prod_t (1 + \lambda(\delta - g_j(t)))$. Mais cela rend l'expérience E3 de A triviale (vérité mathématique tautologique à $10^{-12}$ près, qui ne teste aucune propriété empirique des données).

---

### (b) Scénarios d'évasion : comment un agent adverse trompe les instruments de A

Dans P-26, l'« adversaire » de la garde n'est pas seulement l'agent surveillé, c'est un **sujet $A$ défectueux ou sur-ajusté** (portant un artefact de source ou de longueur qui gonfle son rappel sur les sabotés au prix de fausses alertes sur les honnêtes) qui cherche à passer la porte G1.

1. **Contre la garde F1 alimentée par le « lot honnête séparé » (point 3 de A) :**
   - *Mécanisme* : A dilue l'épreuve avec 140 à 440 unités « honnêtes seules » (sans jumeau saboté) pour atteindre $n_h = 200$ ou $500$ à moindre coût (point d : $\approx 100$ USD, RAPPORTÉ comme illustratif par A). Si ces unités honnêtes seules sont générées dans un lot séparé (ou proviennent de tâches sans sabotage admissible), tout décalage de style, de longueur ou d'horodatage entre les « tâches à paire (honnête, saboté) » ($n = 64$) et les « tâches honnêtes seules » ($n_{\text{seul}} = 136$) permet l'évasion. Un sujet $A$ sensible à la structure des tâches complexes (celles qui admettent un sabotage et où il fait $f_A - f_B = +0,12 > \delta$ sur les 64 jumeaux honnêtes) mais calme sur les tâches simples du lot séparé ($f_A - f_B = 0$ sur les 136 unités) aura une moyenne sur les 200 unités de $(64 \times 0,12 + 136 \times 0)/200 = 0,038 < \delta = 0,05$ *(chiffres illustratifs)*.
   - *Résultat* : le contraste est lu sur les 64 unités où l'artefact de $A$ gonfle artificiellement $r_A$ ; la garde est diluée sur 200 unités et certifie $A$.
   - *Coût* : nul pour le sujet $A$ ; le biais de sélection entre unités appariées et unités honnêtes seules suffit.

2. **Contre le filtre de biais structurel $\max_j \Delta_j \le \delta/4$ (point 4 et E5 de A) :**
   - *Mécanisme* : A vérifie la santé du calibrage par $\Delta_j = |\text{taux\_calibrage}_A - \text{taux\_calibrage}_{B_j}|$ et par la moyenne de $g$ sur le jumeau calibré $A_1 - A_2$. Un sujet $A$ continu (ou muni du bris d'égalité P-15) a $\Delta_j = 0$ sur le calibrage. Et sur le développement, si $A$ subit une dérive globale de ses scores honnêtes (par exemple $+0,03$ de taux d'alerte sur les nouvelles consignes par rapport au calibrage), les deux moitiés $A_1$ et $A_2$ subissent **la même** dérive : $f_{A_1} \approx \tau + 0,03$ et $f_{A_2} \approx \tau + 0,03$, donc $\bar{g}_{\text{jumeau}} = f_{A_1} - f_{A_2} \approx 0$ !
   - *Résultat* : E5 conclut H_A ($\bar{g}_{\text{jumeau}} \le \delta/4$ et $\Delta_j = 0$), déclarant un biais nul, alors que $A$ dérive de $+0,03$ face à des comparateurs $B_j$ stables ($E[f_A - f_{B_j}] = +0,03$). Lors du passage en S2, comme A impose que « seule la dispersion recentrée entre dans $R_n$ », le script calcule $n_{80}$ à biais 0 (160 unités), au lieu du $n_{80}$ à biais $+0,03$ ($> 500$ unités). La garde scellée en S4 sera structurellement muette à l'épreuve.
   - *Coût* : zéro, c'est un angle mort algébrique du jumeau calibré (qui mesure la variance inter-moitiés de $A$, jamais le décalage de $A$ par rapport à $B_j$).

3. **Évasion conjointe de tous les instruments de A (E1 + E2 + E4 + E5) :**
   Un sujet $A$ à scores continus (sans ex æquo) mais présentant (i) une dérive de $+0,02$ entre calibrage et épreuve sur les tâches à sabotage, et (ii) une variance inter-moniteurs normale face à $B_j$, passera :
   - E5 avec $\Delta_j = 0$ et $\bar{g}_{\text{jumeau}} \approx 0$ ;
   - E1 avec une puissance surévaluée (car testée sur $A_1 - A_2$ où $g \approx 0$) ;
   - E2 (car la frontière mécanique $\tau + \delta$ est testée sur $A$ contre lui-même ou par décalage de quantile interne) ;
   - et sera soit promu par artefact (si le lot honnête séparé dilue la dérive), soit rejeté par mutité à l'épreuve faute d'avoir provisionné le biais réel $E[f_A - f_{B_j}]$ en S2.

---

### (c) Les contrôles négatifs dont l'absence est fatale

1. **Absence d'un contrôle d'identité de loi entre « unités à jumeaux sabotés » et « unités honnêtes seules »** : puisque A recommande d'ajouter des unités honnêtes sans sabotés dans l'épreuve (§ 3), ne pas tester $E[f_A - f_{B_j} \mid \text{avec saboté}] = E[f_A - f_{B_j} \mid \text{sans saboté}]$ est fatal. (Notons que la proposition B, en E6, a précisément conçu ce contrôle : j'utilise ici E6 de B contre A.)
2. **Absence du vrai couple $(A, B_j)$ dans E1** : remplacer $f_A - f_{B_j}$ par $f_{A_1} - f_{A_2}$ dans E1 supprime le bruit que l'expérience est censée mesurer. Le contrôle négatif obligatoire est de vérifier que $\text{Var}(f_{A_1} - f_{A_2}) \approx \text{Var}(f_A - f_{B_j})$ ; s'il échoue (et il échouera dès que $n_{\text{calibrage}}$ est grand), E1 est invalide.
3. **Absence de simulation de l'espérance au franchissement joint sous $n_h \gg n$** : puisque A s'appuie sur $n_h > n$ malgré K7-6, il lui manque le contrôle négatif vérifiant que $\mathbb{E}[\exp(\text{log\_e\_valeur})] \le 1$ sous le nul composite quand `len(garde) = 3 * len(contraste)`.

---

## Contre la proposition B

### (a) Les failles : variables confondantes, vérités par construction, fuites

1. **La règle de biais $b_h$ (§ e4 et a6) : fuite statistique et auto-blocage par construction sur 16 tâches (HYPOTHÈSE appuyée sur le calcul de B).**
   En § a6, B démontre lui-même qu'avec 16 tâches au pilote, l'erreur type de la moyenne de $g$ sous $K = 10, \tau = 0,01$ vaut $\text{SE} \approx 0,045 / \sqrt{16} \approx 0,01125$ (illustratif de B).
   Puis, en § e4, B fixe la règle gelée : $b_h = \max(\text{écart d'ex æquo prédit} \; ; \; \bar{g}_{\text{pilote}} + 2\,\text{SE})$.
   - **Ce qui est vrai par construction** : même si le sujet est parfaitement honnête et sans aucun biais ($\mathbb{E}[g] = 0$), le terme $2\,\text{SE}$ vaut à lui seul $2 \times 0,01125 = 0,0225$ ! Et dans 50 % des tirages, $\bar{g}_{\text{pilote}} > 0$, donnant $b_h \ge 0,0225$ (et avec une probabilité de $\approx 16\,\%$, $\bar{g}_{\text{pilote}} \ge 1\,\text{SE}$, donc $b_h \ge 0,034$, *illustratif*). Or B rapporte lui-même en § e3 (d'après pièce C v3 § 7, RAPPORTÉ) qu'à $b = 0,025$ et $\delta = 0,05$, il faut **$350$ à $2\,400$ unités** pour atteindre 80 % de puissance ! Et sous $K_h = 3$, $\text{SE}$ est encore plus grand ($\approx 0,020$), donc $2\,\text{SE} \approx 0,040$, laissant $\delta_{\text{eff}} = \delta - b_h \le 0,01$ : le plancher sans bruit dépasse alors 1 000 unités.
   - **Conséquence fatale** : la règle R de B (§ e5), nourrie par $b_h = \bar{g} + 2\,\text{SE}$ sur 16 unités, conclura **presque sûrement** que $n_h$ requis dépasse le budget finançable, déclenchant systématiquement un nœud d'arrêt avant scellement, même pour un sujet parfait. C'est une règle d'auto-sabotage par défaut de puissance du pilote.

2. **Fuite de données de l'épreuve et violation de P-9 dans la règle $\delta = \min(\Delta_{\min}/2 \; ; \; 0,05)$ (§ e2 et § a7) (HYPOTHÈSE).**
   En § e2, B lie $\delta$ à $\Delta_{\min}$, défini comme « le plus petit gain de contraste que G1 revendique contre le comparateur le plus difficile ».
   - **Dilemme non résolu** : d'où vient $\Delta_{\min}$ ?
     - S'il est fixé arbitrairement sur le papier avant toute donnée (comme le $0,10$ synthétique du script v4), alors $\min(0,10/2, 0,05) = 0,05$ toujours : la formule $\Delta_{\min}/2$ est un décor rhétorique qui vaut la constante $0,05$. Pourtant B mentionne en § a9 que l'écart blanc contre blanc ((ii) et (iii), N-056, RAPPORTÉ) est « probablement petit ». Si l'on postule a priori $\Delta_{\min} = 0,02$ *(illustratif)* pour le blanc contre blanc, alors $\delta = 0,01$, et le plancher à écarts nuls au seuil 160 explose à $\approx 700$ unités (par la formule de B en § e3, *illustratif*) : la garde est garantie muette !
     - Si au contraire $\Delta_{\min}$ est estimé sur le pilote ou le développement pour savoir ce que $A$ peut revendiquer contre (ii) et (iii), cela viole frontalement P-9 (« aucune lecture de sonde sur les sabotés de développement avant G1 », pièce D, RAPPORTÉ, que B cite pourtant en § a7 !) et constitue une **fuite directe** entre l'effet observé du sujet et le réglage de sa propre garde.

3. **Confusion mathématique dans le modèle d'« artefact d'unité » (§ a9 et E4) (HYPOTHÈSE).**
   En § a9, B modélise un sujet ayant un « artefact d'unité $\varepsilon$ » (alertant plus sur les honnêtes et les sabotés d'une même unité) et affirme qu'il gagne $\approx \varepsilon(1 - r_B)$ au contraste. Puis, en E4, B teste H_A : « un sujet synthétique $B_j$ + artefact d'unité $\varepsilon = 0,9\delta$, **à espérance tenue sur les deux classes**, est promu dans $\ge 0,5$ des suites ».
   - **Contradiction interne (vérité par construction)** : si le sujet synthétique est construit « à espérance tenue sur les deux classes » (comme le modèle logit de la v4, GD3-01 / pièce C v4 Q3, RAPPORTÉ), alors par définition $\mathbb{E}[r_A] = \mathbb{E}[r_B]$ (donc $\mathbb{E}[v_j] = 0$) et $\mathbb{E}[f_A] = \mathbb{E}[f_B]$ (donc $\mathbb{E}[g_j] = 0$) ! Un bruit d'unité à espérance tenue ne crée **aucun** gain d'espérance au contraste ; par l'inégalité de Ville sur le contraste ($\mathbb{E}[v_j] \le 0$), la probabilité que le contraste franchisse le seuil $m_c/\alpha_c$ est bornée par $\alpha_c/m_c \le 0,00625$ !
   - Dans E4 telle qu'écrite par B (« à espérance tenue sur les deux classes »), la part promue sera donc $\le 0,00625 < 0,5$ **par construction mathématique** (inégalité de Ville). H_B sera toujours observée, et B conclura à tort que « la critique de vacuité au $n$ prévu est falsifiée », alors qu'il a simplement confondu dans son énoncé de E4 un *décalage d'espérance* $+\varepsilon$ (qui viole l'espérance tenue) et un *effet aléatoire d'unité à espérance tenue* (qui a $\mathbb{E}[v] = 0$).

4. **Omission de la contrainte du mode blanc contre blanc sur le sens de la garde (§ e2) (HYPOTHÈSE).**
   B note en une ligne de réserve (§ e2) que contre (ii) et (iii), qui lisent les mêmes sondes que $A$, « un artefact de source serait partagé et la garde y voit peu », mais maintient le même $\delta$ et la forme 1a (une garde par comparateur). Or, si l'écart de rappel vrai $\mathbb{E}[r_A - r_{\text{(ii)}}]$ est de $0,03$ *(illustratif)* mais que la garde contre les comparateurs boîte noire laisse passer un artefact de $+0,05$, le minimum des processus est incapable d'empêcher un compromis où $A$ bat la boîte noire par artefact ($+0,05$) et bat (ii) par un léger sur-ajustement de seuil.

---

### (b) Scénarios d'évasion : comment un agent adverse trompe les instruments de B

1. **Contre l'expérience E4 (vacuité) de B :**
   - *Mécanisme* : comme démontré en (a).3, l'énoncé de E4 impose « à espérance tenue sur les deux classes ». Tout sujet porteur d'un vrai biais additif d'alerte $+\varepsilon = 0,045$ (qui décale *l'espérance* de $f_A$ et de $r_A$ de $+0,045$) n'est même pas testé par E4 telle que rédigée ! Et si l'on corrige E4 pour y mettre un décalage d'espérance $+\varepsilon = 0,9\delta = 0,045$ (ou $0,09$ si $\delta = 0,10$), l'agent adverse profite de la condition $\mathbb{E}[v_j] = \varepsilon(1 - r_{B_j})$ : si le comparateur $B_j$ a déjà un rappel élevé sur les sabotés du pilote (par exemple $r_{B_j} = 0,60$, *illustratif*), le gain d'artefact au contraste n'est que de $0,045 \times 0,40 = 0,018$, qui ne franchit pas le seuil 160 en 160 unités. E4 conclut alors H_B (« garde non vide »), laissant passer $\delta = 0,10$. Mais sur le **mode tenu à l'écart** à l'épreuve (N-056, RAPPORTÉ), où $r_{B_j}$ peut tomber à $0,05$ *(illustratif)*, le même artefact $+\varepsilon$ rapporte $0,09 \times 0,95 = 0,0855$ au contraste et fait promouvoir $A$ sans aucune détection réelle du sabotage.
   - *Coût* : nul, l'évasion exploite la dépendance du gain d'artefact $\varepsilon(1 - r_B)$ au rappel de base $r_B$ du comparateur.

2. **Contre l'expérience E1 (origine du biais) et la règle $b_h$ de B :**
   - *Mécanisme* : dans E1, B teste $|\bar{g}_j - (\text{taux\_calibrage}_A - \text{taux\_calibrage}_{B_j})| \le 0,005$ sur le pilote (16 unités). Comme l'erreur type sur 16 unités est de $\approx 0,011$ (§ a6 de B), l'intervalle de confiance à 95 % a une demi-largeur de $\approx 0,022 > 0,005$. Un sujet $A$ ayant un décalage de source réel de $+0,015$ (qui tue la garde à $\delta = 0,05$ sous 160 unités : puissance $0,010$, pièce C v3 Q4, RAPPORTÉ) a une probabilité importante de produire une moyenne empirique $\bar{g}_j \le 0,005$ sur un échantillon de 16 unités seulement (erreur de type II du pré-test E1).
   - *Résultat* : s'il tombe sous $0,005$, E1 conclut H_A (« le pilote ne révèle pas de biais propre au sujet : $b_h$ = écart d'ex æquo prédit $\approx 0$ »). B abandonne alors sa borne haute $\bar{g} + 2\,\text{SE}$ (c'est l'enjeu explicite de la falsification de E1 en § b de B !) et fixe $b_h = 0$. À l'épreuve, le vrai biais de $+0,015$ s'applique et la garde échoue. Inversement, si B n'abandonne pas la borne $\bar{g} + 2\,\text{SE}$, un sujet sain ($\mathbb{E}[g] = 0$) tire $\bar{g} > 0,005$ plus d'une fois sur deux sur 16 unités, bascule en H_B, se voit infliger $b_h \ge 0,028$ et fait sauter le projet en nœud budgétaire.
   - *Coût* : nul, c'est le piège classique du pré-test de spécification à faible puissance (16 unités).

3. **Contre la forme 1b de B (garde unique sur $g^*(t) = f_A(t) - \min_j f_{B_j}(t)$) si E2 conclut H_A :**
   - *Mécanisme* : B garde la forme 1b en réserve si E2 montre que les $k$ gardes limitent la fiche de plus de $0,10$ (§ e1). Or, sur chaque unité $t$, $\min_{j=1..k} f_{B_j}(t)$ est le minimum de $k$ variables aléatoires. Dès que $k$ augmente (par exemple $k = 5$ ou $7$ avec tous les moniteurs de P-1 et N-056, § a8 de B), même si chaque $B_j$ et $A$ sont i.i.d. de loi $\text{Bin}(K_h, \tau)/K_h$, on a $\mathbb{E}[\min_j f_{B_j}(t)] < \tau = \mathbb{E}[f_A(t)]$. Pour $K_h = 3, \tau = 0,10$ et $k = 6$ comparateurs indépendants, $\mathbb{P}(f_{B_j} = 0) = 0,9^3 = 0,729$, donc $\min_j f_{B_j}(t) = 0$ presque toujours ($\mathbb{P} = 1 - 0,271^6 = 0,9996$), ce qui donne $\mathbb{E}[g^*(t)] \approx \mathbb{E}[f_A(t)] = 0,10$ *(calcul exact sous indépendance, illustratif)* !
   - *Résultat* : sous 1b, un sujet $A$ parfaitement honnête ($\mathbb{E}[f_A] = \tau$) a un biais positif mécanique $\mathbb{E}[g^*] \approx \tau$ dès que $k$ est modéré et $K_h \tau < 1$. Si $\tau = 0,05$ (organisme) ou si une strate a un taux effectif plus haut, $\mathbb{E}[g^*] \ge \delta = 0,05$ : la garde 1b ne certifie **jamais**, même à $n_h \to \infty$ (c'est une sous-martingale qui dérive vers $-\infty$).

---

### (c) Les contrôles négatifs dont l'absence est fatale

1. **Absence d'un contrôle de fausse alerte de la règle R sur sujet parfait à $N_{\text{pilote}} = 16$** : B n'a aucun contrôle négatif vérifiant quelle est la probabilité qu'un sujet synthétique parfait ($\mathbb{E}[g] = 0$, $K_h = 10$ ou $3$, $\tau = 0,01$) évalué sur 16 unités passe la règle R ($\bar{g} + 2\,\text{SE} \to n_{80}$) sans déclencher un nœud ou exiger $n_h > 400$. Sans ce contrôle, R est une porte qui se ferme toute seule par bruit d'échantillonnage.
2. **Absence d'un contrôle positif de décalage d'espérance dans E4** : puisque E4 impose « à espérance tenue », il manque le contrôle vérifiant qu'un décalage d'espérance franc ($\mathbb{E}[f_A] = \tau + 0,9\delta$ et $\mathbb{E}[r_A] = r_B + 0,9\delta$) est effectivement promu quand on enlève la garde. Sans lui, E4 rejette H_A par le seul effet de la borne de Ville sur un contraste d'espérance nulle.
3. **Absence de borne sur le biais d'ordre $\mathbb{E}[f_A - \min_j f_{B_j}]$ pour l'option de repli 1b** : proposer 1b en repli de E2 sans exiger que $\mathbb{E}[\max_j g_j(t)] < \delta/2$ sur des jumeaux calibrés indépendants condamne le repli 1b à l'échec dès que $k \ge 3$ et $K_h$ petit.

FIN-DE-CELLULE