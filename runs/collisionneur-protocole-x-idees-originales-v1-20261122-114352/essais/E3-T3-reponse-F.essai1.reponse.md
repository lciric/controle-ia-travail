# Proposition F — Réponse aux critiques et protocole corrigé (Tour III.3)

**Constat de réception (Règle 2)** : le bloc `FAITS` duplique `QUESTION DE L'ARBITRE` sans donnée empirique vérifiée et renvoie à une pièce parente absente à identifiant tronqué (`05c72e05…`) ; ma conception III.1 (`E3-T1-conception-F`) et les cinq critiques croisées (`A` à `E`) sont présentes et complètes.

**Convention de statut (Règle 1)** : aucun fait empirique n'est `VÉRIFIÉ`. Les arguments repris des critiques et travaux publiés sont `RAPPORTÉ` ; les calculs algébriques ou probabilistes internes sont signalés comme *dérivation* ; tout choix de protocole est `HYPOTHÈSE`. Je ne réponds qu'aux sections visant la proposition F.

---

## (a) Traitement des critiques visant la proposition F

Pour éviter tout lissage (règle B1), les critiques de chaque auteur sont traitées séparément avec l'un des trois statuts demandés : **ACCEPTÉE**, **REJETÉE** (avec raison) ou **TRANSFORMÉE EN TEST**.

### Critiques de A (`RAPPORTÉ`)

1. **A(a)1 — `FDR_audit` circulaire ($\Phi_{\text{audit}}$ servant à la fois d'acceptation et de vérité)** : **ACCEPTÉE**. Hors domaines plantés, vérifier le niveau nominal de la procédure sur $\Phi_{\text{audit}}$ ne mesure pas l'erreur réelle. Tous les duels E1–E4 intègrent désormais un oracle externe indépendant $\Phi^*$ et des campagnes sur domaines nuls (repris de A).
2. **A(a)2 — Test de permutation inatteignable sur $5$ graines (illustratif)** : **ACCEPTÉE**. Avec $5$ paires (illustratif), la plus petite *p*-valeur unilatérale est $2^{-5} = 1/32 > 0{,}01$ (dérivation sur seuil illustratif) ; $H_{A1}$ était inatteignable par domaine. Remplacé par une règle de région de confiance simultanée sur $12$ graines par domaine (illustratif).
3. **A(a)3 — Biais de sélection non contrôlé du « meilleur modèle unique » ($I_0$)** : **ACCEPTÉE**. $I_0$ est désormais sélectionné *ex ante* sur un domaine pilote disjoint des domaines d'évaluation.
4. **A(a)4 — Gain par construction en I1 lorsque $P_0$ change de modèles (modes propres d'une autre famille comptés rares sous $P_0$)** : **TRANSFORMÉE EN TEST**. Raison : dans la question, une idée rare sous le système de référence et valide répond à la cible si elle élargit la couverture, mais il faut distinguer un simple déplacement de modes d'un accès à une queue commune. E1 mesure donc la courbe à deux budgets $B_1 < B_2$ (illustratif) et ajoute le **test symétrique d'échange des rôles** (classes rares sous I1 produites par $I_0$, repris de A).
5. **A(a)5 — E0 : indistinguabilité de $p_0 = 0$ (hors support) et $0 < p_0 \le \tau$, plus zone morte $[0{,}30\,; 0{,}85]$ (illustratif)** : **ACCEPTÉE**. Un oracle de construction ne prouve pas $p_0 > 0$ sous $P_0$, et la zone morte viole B4. E0 est reformulée en partition complémentaire sur $(C_{N_0}, h_{\text{rare}})$ sans zone morte.
6. **A(a)6 — Contrôle composite de E4 interdisant l'attribution entre filtres et bandit** : **ACCEPTÉE**. E4 devient un plan factoriel $2 \times 2$ (repris de A et D).
7. **A(a)7 — Origine non spécifiée du jeu étalonné de faux négatifs en E4 (biais de survie)** : **ACCEPTÉE**. Estimation sans biais des faux négatifs via un bras sans filtre intégralement audité et un audit probabiliste des rejetés (repris de A et D).
8. **A(a)8 — Biais de la valeur (minimum observé de longueur favorisant les classes fréquentes ; portefeuille fréquent dépendant du bras)** : **ACCEPTÉE**. Remplacement par la longueur du *premier* représentant canonisé (indépendante de la fréquence d'observation) et par un portefeuille fréquent figé une seule fois sur un panel externe $P_{\text{réf}}$ commun.
9. **A(a)9 — Portée des citations Padmakumar & He (2024), Shumailov et al. (2024) et loi en $O(\sqrt{k/m})$** : **ACCEPTÉE**. Padmakumar & He (2024, `RAPPORTÉ`) porte sur la co-écriture humain-LLM et ne constitue qu'un indice indirect pour la génération autonome (`HYPOTHÈSE`) ; Shumailov et al. (2024, `RAPPORTÉ`) traite de l'entraînement récursif et son extension à la corrélation inter-familles est analogique (`HYPOTHÈSE`) ; le taux $O(\sqrt{k/m})$ est un résultat `RAPPORTÉ` de Dwork et al. (2015) sans dérivation propre dans ma pièce.
10. **A(b)1–4 — Perte de puissance (*e-values* sous loi d'audit, Clopper-Pearson simultané $N_0 \ge \ln(M/\delta)/\tau$, UCB non stationnaire, MAP-Elites)** : **ACCEPTÉE**. Traité par l'ajout de $\Phi^*$, la certification simultanée restreinte aux seules $K_{\text{val}}$ classes déjà validées, et le remplacement d'UCB stationnaire par un allocateur à oubli/fenêtre glissante.
11. **A(c) — Contrôles négatifs (instances nulles + $\Phi^*$, bras sans filtre, instances sentinelles, essai A/A et ablation $2 \times 2$)** : **ACCEPTÉE** (intégralement repris de A).

### Critiques de B (`RAPPORTÉ`)

1. **B(a)1, B(a)2, B(a)4, B(a)5, B(a)7, B(a)8 — Recoupements avec A** ($H_{A0}$, 5 graines, choix de $I_0$, biais MDL/portefeuille, jeu étalonné E4, simultanéité Clopper-Pearson) : **ACCEPTÉES** (mêmes correctifs qu'en A).
2. **B(a)3 — Confusion de facteurs dans I1 (familles, modèles de base, décodage contraint) et statut du décodage dans le bras clones** : **ACCEPTÉE**. E1 passe en plan factoriel $2 \times 2$ (familles × alignement) où $I_0$ et le bras clones utilisent le *même* décodage contraint par grammaire et la même déduplication.
3. **B(a)6 — $\Phi_{\text{dev}}$ et $\Phi_{\text{audit}}$ tirés du même générateur procédural (coupure temporelle sans objet sur du synthétique)** : **ACCEPTÉE**. $\Phi_{\text{audit}}$ est désormais généré par une famille procédurale **structurellement décalée** par rapport à $\Phi_{\text{dev}}$ (repris de B), en plus d'un jeu intra-famille pour séparer sur-ajustement et décalage de distribution.
4. **B(b)2 — Indéfinition et variance explosive de Chao1 lorsque $f_2 = 0$ ou $f_1 \gg f_2$** : **ACCEPTÉE**. Chao1 est retiré de toute règle décisionnelle et remplacé comme indicateur descriptif par la forme corrigée du biais $S_{\text{obs}} + f_1(f_1-1)/(2(f_2+1))$ (*référence à vérifier*).
5. **B(b)4 — Loi nulle indéfinie des *e-values* sur un audit déterministe sans faux échangeables** : **ACCEPTÉE**. L'aléa est porté explicitement par le tirage i.i.d. des instances de $\mathcal{D}_{\text{audit}}$ : les *e-values* testent l'hypothèse nulle appariée de non-supériorité sur $\mathcal{D}_{\text{audit}}$ contre le portefeuille figé (martingale sur différences bornées, `RAPPORTÉ` : Ramdas et al., 2023), tandis que la validité hors $\mathcal{D}_{\text{audit}}$ est mesurée par $\Phi^*$.
6. **B(c) — Contrôles négatifs (A/A, générateur d'audit décalé, injection d'une idée hors support)** : **ACCEPTÉE** pour A/A et le générateur décalé (repris de B) ; **TRANSFORMÉE EN TEST** pour l'idée hors support (test d'étalonnage pré-E0 vérifiant que le certificateur renvoie « $\hat{p}_0^+ \le \tau$, compatible avec $0$ » et ne prétend jamais mesurer $p_0 > 0$).

### Critiques de C (`RAPPORTÉ`)

1. **C(a)1 — Gonflement du gain marginal de portefeuille en I2/I3 si les classes fréquentes sont collectées intra-bras** : **ACCEPTÉE** (portefeuille fréquent figé exclusivement sur $P_{\text{réf}}$ externe).
2. **C(a)2 — Confusion de facteurs dans I1 (familles/base/décodage) et I3 (exclusion structurelle + ciblage des cas résiduels de $\mathcal{T}_{\text{dev}}$)** : **ACCEPTÉE**. E1 et E3 deviennent des plans factoriels $2 \times 2$ séparant chaque levier.
3. **C(a)3 — Tension logique dans E0 entre oracle de construction et masse $p_0$** : **ACCEPTÉE** (voir A(a)5).
4. **C(b)1 — Ensemble vide de Clopper-Pearson si $\tau < 1 - \delta^{1/N_0}$ et perte de puissance $> 50\,\%$ (dérivation) près du seuil $\tau$** : **ACCEPTÉE & TRANSFORMÉE EN TEST**. La certification simultanée ne porte que sur les $K_{\text{val}}$ classes déjà validées (indépendantes de $P_{\text{réf}}$), avec dimensionnement $N_0 \ge 2 \ln(K_{\text{val}}/\delta_{\text{sim}})/\tau$ (illustratif) ; un test de sensibilité sur plusieurs seuils $\tau$ rapporte le profil cumulé de découvertes en fonction de $\hat{p}_0^+$.
5. **C(b)2 — Plafond de puissance d'e-BH sur banc d'audit fini dès $J > \alpha \, p_{\text{nul}}^{-M_{\text{aud}}}$ (dérivation)** : **ACCEPTÉE**. Dimensionnement préenregistré de $M_{\text{aud}}$ et borne $J_{\max}$ de candidats audités (filtrés sur $\Phi_{\text{dev}}$ seul) garantissant $p_{\text{nul}}^{-M_{\text{aud}}} \gg J_{\max}/\alpha$ ; emploi de BH à horizon fixe lorsque la collecte n'est pas séquentielle.
6. **C(b)3 — Dérivation du biais positif d'UCB stationnaire $\bar{\mu}_a(n_a) > \mu_a(n_a)$ sur bras épuisés** : **ACCEPTÉE** (remplacement d'UCB stationnaire en E4).
7. **C(c) — Contrôles négatifs (portefeuille figé, programmes *lookup table* mémorisant $\mathcal{T}_{\text{dev}}$ dans I2, mono-modèle *base* contraint en E1, exclusion sans résidus en E3)** : **ACCEPTÉE** (intégralement repris de C).

### Critiques de D (`RAPPORTÉ`)

1. **D(a)1–2 — Simultanéité de la borne de rareté ; fuite de sélection de $I_0$** : **ACCEPTÉES** (voir A/B/C).
2. **D(a)3 — Sélection interne à l'audit sur performance, complexité et complémentarité** : **ACCEPTÉE**. Les critères déterministes (longueur MDL) et le portefeuille de référence sont fixés *hors audit* ; l'acceptation sur $\Phi_{\text{audit}}$ est soumise globalement à e-BH/BH sur tous les $J$ candidats audités ; la mesure finale $(D_{\text{rare}}^*, \text{FDR}^*)$ repose sur $\Phi^*$ indépendant.
3. **D(a)4 — Une *e-value* isolée ne spécifie pas la procédure FDR multi-candidats** : **ACCEPTÉE**. La procédure multi-tests est explicitement **e-BH** (`RAPPORTÉ` : Wang, R., & Ramdas, A., 2022, *False discovery rate control with e-values*, Journal of the Royal Statistical Society: Series B) sur les $J$ candidats audités.
4. **D(a)5 — E0 confond absence de détection et absence de vérité rare** : **ACCEPTÉE**. $H_{B0}$ porte désormais sur la masse cumulée détectable ($h_{\text{rare}} \le h_{\min}$), non sur l'inexistence ontologique.
5. **D(a)6 — Zones mortes dans E1–E4 violant B4** : **ACCEPTÉE**. Toutes les expériences passent à des partitions complémentaires $H_A : \theta \in G$ contre $H_B : \theta \notin G$ via région de confiance simultanée (règle reprise de D), mais avec une **marge de non-infériorité strictement positive** $\delta_{\text{FDR}} > 0$ (illustratif) afin d'éviter la paralysie à la frontière $\Delta\text{FDR}^* = 0$.
6. **D(b) — Conditions de perte de puissance (masse $h$, rareté des gains marginaux ; I1 loi conditionnelle à l'analysabilité ; I2 absence d'effet de cellule ; I3 bannissement de la cible ; I4 non-stationnarité, FN non identifiés et fuite d'histoire $\mathcal{F}_{t-1}$)** : **ACCEPTÉES** (pour I2, I3, I4 et le dimensionnement de $N_0, M_{\text{aud}}$ ; interdiction stricte de tout retour de $\Phi_{\text{audit}}$ vers les filtres/l'allocation en I4) et **TRANSFORMÉE EN TEST** pour I1 (E1 décompose le débit en taux de sorties analysables $\times$ débit conditionnel aux sorties analysables).
7. **D(c) — Contrôles négatifs (campagnes nulles complètes ; I1 clone contraint ; I2 permutation de descripteurs conservant occupations et descendants par parent ; I3 motifs placebo de même *masse* + permutation des résidus ; I4 ablations séparées, audit probabiliste des rejetés et bras à récompenses identiques)** : **ACCEPTÉE** (intégralement repris de D).

### Critiques de E (`RAPPORTÉ`)

1. **E(a)1 — Conjonction AST dans $\sim$ créant de la fausse rareté par refactorisation (itération vs récursion)** : **ACCEPTÉE**. La relation $\sim$ est redéfinie par la **seule signature comportementale étendue** (sans conjonction AST) ; la structure syntaxique ne sert plus jamais à scinder une classe comportementale.
2. **E(a)2 — Fuite budgétaire hors $B$ de l'échantillon $N_0$ vers I3 et vers la mesure de valeur** :
   - *Sur I3* : **ACCEPTÉE**. Lire les $K$ modes dominants dans le panel $N_0$ donnait à I3 un avantage gratuit hors $B$. En E3 corrigé, I3 identifie ses $K$ modes à exclure uniquement dans son propre budget $B$.
   - *Sur la mesure de valeur (portefeuille de référence)* : **REJETÉE**. Raison : un panel d'évaluation externe $P_{\text{réf}}$ strictement invisible à *tous* les bras ($I_0$ comme I1–I4) ne fournit aucun avantage budgétaire ni informationnel à un bras ; il constitue au contraire l'étalon invariant exigé pour éviter le biais inter-bras relevé par A(a)8, B(a)5 et C(a)1.
3. **E(a)3–4 — Variables confondantes en E1/E3/E4 et fuite du générateur procédural entre $\Phi_{\text{dev}}$ et $\Phi_{\text{audit}}$** : **ACCEPTÉES** (voir B(a)6, C(a)2, D(c)).
4. **E(b)1–4 — Conditions de perte de puissance (Clopper-Pearson sous $J = 25\,000$ illustratif ; sur-scission en E0 ; biais UCB ; plafond $\mu_0^{-m}$ et rupture de validité des *e-values* sous générateur partagé)** : **ACCEPTÉES** (résolues respectivement par restriction aux $K_{\text{val}}$ classes validées, suppression de l'AST dans $\sim$, allocateur non stationnaire, et générateur d'audit structurellement décalé + $\Phi^*$).
5. **E(c)1–3 — Contrôles négatifs (ablations factorielles E1/E3/E4 ; refactorisation avec rustine sur cas limite ; audit externe $\Phi^*$ hors générateur en I2)** : **ACCEPTÉE** (repris de E et étendu à E1–E4).

---

## (b) Protocole et expériences corrigées (inférence forte, B4)

Tous les paramètres numériques ci-dessous sont marqués **« illustratif »** et relèvent de `HYPOTHÈSE` de protocole.

### Socle métrologique corrigé (commun à E0–E4)

1. **Canonisation $\sim$ purement comportementale** : deux propositions $x, x' \in \mathcal{X}$ appartiennent à la même classe $[x]$ ssi elles produisent le même vecteur de sorties complètes (valeurs numériques ou témoins normalisés, jamais un simple bit de validité) sur une batterie fixe de sondes $\mathcal{S}$ disjointe de $\mathcal{T}_{\text{dev}}$, $\mathcal{T}_{\text{audit}}$ et $\Phi^*$. *Contrôle de qualification bloquant avant E0 (repris de E)* : $\sim$ doit regrouper des refactorisations équivalentes (itération vs récursion) et rejeter au front de Pareto MDL les variantes gonflées par rustine sur un cas limite.
2. **Trois niveaux d'évaluation étanches** : $\Phi_{\text{dev}}$ (recherche), $\Phi_{\text{audit}}$ (tiré d'un générateur structurellement décalé, contenant des **instances sentinelles** reprises de A, de taille $M_{\text{aud}}$ telle que $p_{\text{nul}}^{-M_{\text{aud}}} \ge 100 \, J_{\max}/\alpha$, illustratif, avec contrôle multi-tests **e-BH** de Wang & Ramdas, 2022, `RAPPORTÉ`, sur *e-values* appariées contre le portefeuille figé — ou BH en lot fixe), et **oracle externe indépendant $\Phi^*$** (vérificateur exact ou instances hors générateur + **domaines nuls** sans solution rare valide, repris de A, D, E). Le débit net vrai $D_{\text{rare}}^*$ et le taux vrai de fausses découvertes $\text{FDR}^*$ sont évalués par $\Phi^*$.
3. **Panel externe $P_{\text{réf}}$ étanche** : $N_0$ appels i.i.d. du système nominal, **invisibles à tous les bras**. $P_{\text{réf}}$ fixe (i) le portefeuille fréquent de référence (invariant entre bras), et (ii) les comptages $K_0([x])$ pour certifier la rareté des seules $K_{\text{val}}$ classes distinctes ayant franchi $\Phi_{\text{audit}}$, via Clopper-Pearson simultané (Šidák, risque global $\delta_{\text{sim}} = 0{,}05$, illustratif), avec condition préenregistrée $N_0 \ge 2 \ln(K_{\text{val}}/\delta_{\text{sim}})/\tau$ (illustratif). La longueur MDL d'une classe est mesurée sur son *premier* représentant canonisé (non biaisé par la fréquence). *Test d'étalonnage (repris de B)* : une idée construite hors support injectée reçoit le verdict « $\hat{p}_0^+ \le \tau$ (compatible avec $0$) ».
4. **Règle de décision sans zone morte (B4) et essai A/A préalable** : chaque duel est mené sur $3$ domaines canonisables $\times 12$ graines indépendantes par domaine (illustratif ; $I_0$ choisi sur un $4^\text{e}$ domaine pilote disjoint, avec décodage contraint et déduplication). Un **essai A/A** ($I_0$ contre $I_0$) et des **campagnes entièrement nulles** passant par toute la chaîne (repris de A, B, D) calibrent la variance nulle et le respect de $\text{FDR}^*$. Sur les paramètres de population $\theta = (\mu_{\text{gain}}, \mu_{\Delta\text{FDR}^*}, \mu_{\text{FDR}^*})$, on fixe une marge de gain utile $\gamma = +15\,\%$, une marge de non-infériorité $\delta_{\text{FDR}} = +0{,}02$ et un plafond $\alpha_{\max} = 0{,}05$ (tous illustratifs), et l'on oppose deux hypothèses **strictement complémentaires** :
   - $H_A : \theta \in G = \{\mu_{\text{gain}} > \gamma \;\land\; \mu_{\Delta\text{FDR}^*} \le \delta_{\text{FDR}} \;\land\; \mu_{\text{FDR}^*} \le \alpha_{\max}\}$ ;
   - $H_B : \theta \notin G$.
   Une région de confiance simultanée appariée $\mathcal{R}_{0{,}95}$ (illustratif, règle reprise de D) incluse dans $G$ réfute $H_B$ ; disjointe de $G$, elle réfute $H_A$ (**abandon de l'intervention**) ; à cheval sur la frontière, l'essai reste non concluant et déclenche l'ajout préenregistré de graines.

### E0 (corrigée) — Redécouverte modale et masse détectable de puits rares

- **Protocole** : $N_0$ appels i.i.d. de $P_0$ (ex. $N_0 = 20\,000$, $\tau = 10^{-3}$, illustratifs), comparés à un générateur aléatoire syntaxiquement valide et évalués par $\Phi^*$. On estime la couverture $C_{N_0} = 1 - \mathbb{E}[f_1/N_0]$ et la masse cumulée sous $P_0$ des classes rares valides à valeur marginale positive $h_{\text{rare}} = \sum_{[x] : p_0([x]) \le \tau,\; \Phi^*([x])=1,\; \text{gain}>0} p_0([x])$. (L'estimateur $\hat{S}_{\text{Chao1-bc}}$ reste descriptif hors règle de décision.)
- **Hypothèses exclusives (B4)** : $H_{A0} : (C_{N_0} > 0{,}70) \land (h_{\text{rare}} > 5\cdot 10^{-4})$ (seuils illustratifs) contre $H_{B0} : (C_{N_0} \le 0{,}70) \lor (h_{\text{rare}} \le 5\cdot 10^{-4})$.
- **Falsification** : $\mathcal{R}_{0{,}95} \subset H_{B0}$ falsifie $H_{A0}$ (soit pas d'effondrement modal, soit puits rares sous le seuil détectable à $N_0$ — arrêt des interventions sur ce domaine) ; $\mathcal{R}_{0{,}95} \subset H_{A0}$ falsifie $H_{B0}$.

### E1 (corrigée) — Plan factoriel $2 \times 2$ pour I1 (familles × alignement, décodage contraint égal)

- **Protocole** : quatre bras à budget total $B$ égal, **tous** équipés du même décodage contraint par grammaire et de la même déduplication pré-vérification : $I_0$ (mono-famille *instruct* choisi hors banc), $I_{0,\text{base}}$ (même famille *base*), $I_{1,\text{inst}}$ (multi-familles *instruct*), $I_{1,\text{mix}}$ (multi-familles *base + instruct*), mesurés à **deux budgets** $B_1 < B_2$ (illustratifs). Décomposition du débit en *taux analysable × débit conditionnel aux sorties analysables* (reprise de D).
- **Contrôles négatifs** : (1) clones de $I_0$ (variations d'invite/graine, même décodage contraint) ; (2) **échange symétrique des rôles** (classes rares sous $I_{1,\text{mix}}$ produites par $I_0$, repris de A) ; (3) domaines nuls complets ; (4) profil de sensibilité sur plusieurs seuils $\tau$.
- **Hypothèses exclusives (B4) et abandon** : pour chaque facteur (pluralité de familles, poids *base*, combinaison $I_{1,\text{mix}}$), $H_{A1}$ exige $\theta \in G$ contre $I_0$ et contre les clones au budget $B_2$, avec gain asymétrique net à l'échange des rôles (ratio net $> 1{,}15$, illustratif) ; $H_{B1}$ est le complémentaire exact. **Abandonner** tout facteur dont $H_{A1}$ est réfutée ; réfutation de $H_{B1}$ valide le facteur.

### E2 (corrigée) — Duel pour I2 (MAP-Elites mécanique sous audit décalé et $\Phi^*$)

- **Protocole** : MAP-Elites à descripteurs mécaniques évoluant sur $\Phi_{\text{dev}}$ seul, comparé à $I_0$ au même budget $B$, audité sur un jeu intra-famille **et** sur $\Phi_{\text{audit}}$ structurellement décalé, puis jugé par $\Phi^*$.
- **Contrôles négatifs** : (1) **permutation des descripteurs conservant les occupations et le nombre de descendants par parent** (reprise de D) ; (2) injection de **programmes *lookup table*** mémorisant $\mathcal{T}_{\text{dev}}$ (reprise de C) ; (3) **instances sentinelles** dans $\Phi_{\text{audit}}$ (reprises de A) ; (4) domaines nuls complets.
- **Hypothèses exclusives (B4) et abandon** : $H_{A2}$ exige $\theta \in G$ sur $D_{\text{rare}}^*$ contre $I_0$ et contre le contrôle à descripteurs permutés, avec ratio de transfert $\Phi_{\text{dev}} \to \Phi_{\text{audit,décalé}}$ au moins égal à $0{,}70$ (illustratif) fois celui de $I_0$ ; $H_{B2}$ est le complémentaire exact. **Abandonner I2** si $H_{A2}$ est réfutée (ou si une sentinelle détecte une fuite).

### E3 (corrigée) — Plan factoriel $2 \times 2$ pour I3 (exclusion interne × ciblage des résidus)

- **Protocole** : aucun accès à $P_{\text{réf}}$ ; les $K$ modes dominants sont estimés dans le budget interne $B$ du bras. Plan $2 \times 2$ à budget $B$ égal : $I_0$ ; I3a (exclusion mécanique seule) ; I3b (conditionnement sur les échecs résiduels de $\mathcal{T}_{\text{dev}}$ seul) ; I3ab (les deux).
- **Contrôles négatifs** : (1) exclusion mécanique de **motifs placebo de même masse cumulée** (repris de D) ; (2) permutation des cas résiduels de $\mathcal{T}_{\text{dev}}$ (reprise de D) ; (3) exclusion par simple négation textuelle dans l'invite ; (4) domaines nuls + $\Phi^*$.
- **Hypothèses exclusives (B4) et abandon** : pour chacun des bras I3a, I3b, I3ab, $H_{A3}$ exige $\theta \in G$ contre $I_0$ et contre son contrôle placebo dédié ; $H_{B3}$ est le complémentaire exact. **Abandonner** chaque levier dont $H_{A3}$ est réfutée.

### E4 (corrigée) — Plan factoriel $2 \times 2$ pour I4 (cascade × allocateur non stationnaire + e-BH)

- **Protocole** : en régime $c_{\text{verif}}/c_{\text{gen}} \ge 10$ (illustratif), UCB stationnaire est remplacé par un **allocateur à fenêtre glissante / escompte** adapté aux récompenses décroissantes (*référence à vérifier*). Quatre bras : uniforme sans filtre ; cascade + uniforme ; sans filtre + allocateur non stationnaire ; cascade + allocateur (I4 complet). Aucun retour de $\Phi_{\text{audit}}$ n'alimente les filtres ni l'allocateur. Une fraction aléatoire $q_{\text{rej}} = 0{,}05$ (illustratif) des candidats rejetés par la cascade est auditée (coût inclus dans $B$) pour estimer sans biais le taux de faux négatifs $\text{FN}_{\text{rare}}$ par pondération inverse de probabilité (*référence à vérifier*).
- **Contrôles négatifs** : (1) filtres remplacés séparément par un passage aléatoire de même taux ; (2) allocateur testé sur **bras à récompenses identiques** (repris de D) ; (3) bras sans filtre intégralement audité (repris de A) ; (4) domaines nuls + $\Phi^*$.
- **Hypothèses exclusives (B4) et abandon** : $H_{A4}$ exige $\theta \in G$ pour chaque facteur contre son contrôle dédié, assorti de $\text{FN}_{\text{rare}} \le 0{,}15$ (illustratif) ; $H_{B4}$ est le complémentaire exact. **Abandonner** tout composant dont $H_{A4}$ est réfutée.

---

## (c) Réponse à la question de l'arbitre (une page)

### Ce qui est établi

1. **Aucune donnée empirique du système cible n'est établie** (`FAITS` ne contenant que la question). Tout effet des interventions et toute existence de puits étroits restent à l'état d'`HYPOTHÈSE`.
2. **Pourquoi la question initiale doit être reposée (Q5)** : sans espace canonisable, l'identité d'une idée n'est pas testable sans modèle juge ; sans partition étanche entre recherche ($\Phi_{\text{dev}}$), audit décalé ($\Phi_{\text{audit}}$) et vérité externe ($\Phi^*$), la confirmation reste circulaire ; sans comptabilité physique unifiée $B = C_{\text{gen}} + C_{\text{canon}} + C_{\text{verif}}$, le coût réel des interventions est masqué. Le problème bien posé consiste à maximiser, à budget $B$ égal, le nombre de classes comportementales distinctes $[x]$ certifiées rares sur un panel externe étanche $P_{\text{réf}}$, apportant un gain marginal vérifié hors distribution contre un portefeuille fréquent figé et non dominées en longueur canonique, tout en bornant le taux vrai de fausses découvertes $\text{FDR}^*$.
3. **Bornes de principe établies par dérivation ou résultats `RAPPORTÉ`** :
   - *Mur du taux de base* (Bayes ; Benjamini & Hochberg, 1995, `RAPPORTÉ`) : si la prévalence vraie en queue $\pi_{\text{rare}}$ est inférieure au taux de faux positifs effectif $\varepsilon_{\text{FP,rare}}$ du contrôleur, la majorité des « découvertes rares confirmées » sont fausses.
   - *Indécidabilité de l'équivalence* (Rice, 1953, `RAPPORTÉ`) : dans un formalisme expressif, toute canonisation mécanique comporte une erreur résiduelle de fusion ou de scission qui doit être mesurée avant toute estimation de rareté.
   - *Coût de la certification simultanée de rareté* (dérivation) : certifier simultanément $p_0([x]) \le \tau$ pour $K_{\text{val}}$ classes au risque $\delta_{\text{sim}}$ exige un panel indépendant d'ordre $N_0 \gtrsim \ln(K_{\text{val}}/\delta_{\text{sim}})/\tau$, et ne sépare jamais $p_0 = 0$ de $0 < p_0 \le \tau$.
   - *Érosion adaptative et No Free Lunch* (Wolpert & Macready, 1997 ; Dwork et al., 2015, `RAPPORTÉ`) : sans signal de voisinage exploitable, la recherche adaptative ne bat pas le tirage indépendant ; et sans étanchéité $\Phi_{\text{dev}}/\Phi_{\text{audit}}$ ni verrou multi-tests (e-BH, Wang & Ramdas, 2022 ; Ramdas et al., 2023, `RAPPORTÉ`), l'exploration intensifie l'exploitation des angles morts du contrôleur.
   - *Non-stationnarité par épuisement* (dérivation) : compter des classes rares *nouvelles* rend les récompenses décroissantes, invalidant les garanties des bandits stationnaires (Auer et al., 2002, `RAPPORTÉ`).

### Ce qui n'est pas établi (`HYPOTHÈSE`)

- L'existence de puits étroits valides de masse cumulée détectable $h_{\text{rare}}$ sous $P_0$, ainsi que le degré réel de répétition entre appels indépendants.
- Le taux de faux positifs $\varepsilon_{\text{FP,rare}}$ d'un contrôleur fiable sur des cas connus lorsqu'il est confronté à des idées rares hors distribution (et la corrélation d'erreurs entre contrôles).
- L'apport causal net, à coût physique $B$ égal, de chacun des leviers pris séparément : pluralité de familles de modèles, modèles peu alignés, décodage contraint, archives Qualité-Diversité (MAP-Elites), exclusion interne des modes, ciblage des échecs résiduels, cascades de filtres et allocateurs à oubli.
- La généralisation hors des domaines formels exécutables : en langage naturel libre, aucune mesure de rareté sémantique strictement sans modèle n'est établie.

### L'expérience à faire en premier

Avant tout duel d'interventions, lancer le **bloc préliminaire de qualification + E0 + essai A/A + campagne nulle** sur un premier domaine canonisable muni d'un oracle exact externe $\Phi^*$ et d'un contrôleur imparfait séparé en $(\Phi_{\text{dev}}, \Phi_{\text{audit,décalé}})$ :

1. **Qualification de $\sim$** : vérifier que la canonisation purement comportementale regroupe des refactorisations équivalentes sans fusionner des mécanismes distincts. Si elle échoue, corriger $\sim$ avant toute suite.
2. **E0 sur $N_0$ appels i.i.d. de $P_0$** : estimer simultanément la couverture $C_{N_0}$, la masse cumulée $h_{\text{rare}}$ de puits rares valides complémentaires sous $\Phi^*$, la prévalence en queue $\pi_{\text{rare}}$ et le taux de faux positifs effectif $\varepsilon_{\text{FP,rare}}$ du contrôleur dans cette queue.
3. **Essai A/A et domaine nul** : mesurer la variance inter-graines et vérifier que le verrou (e-BH/BH sur $\Phi_{\text{audit}}$) maintient réellement $\text{FDR}^* \le \alpha_{\max}$ lorsque aucune solution rare valide n'existe.

**Raison de cette priorité** : ce bloc coûte une fraction du budget total et falsifie en premier les prémisses critiques (absence d'effondrement modal, absence de masse rare détectable, faillite de $\sim$, ou mur de faux positifs $\varepsilon_{\text{FP,rare}} \gg \pi_{\text{rare}}$). Seulement si E0 réfute $H_{B0}$ et que le domaine nul passe, lancer en second le plan factoriel **E1** (familles × alignement à décodage contraint égal, à deux budgets $B_1 < B_2$ avec échange des rôles), car il est non adaptatif et donc le moins exposé au sur-ajustement de $\Phi_{\text{dev}}$.

FIN-DE-CELLULE