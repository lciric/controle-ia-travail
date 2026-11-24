# Proposition A, tour III.2 : critique croisée de méthode

**Audit des pièces.** Les pièces E3-T1-conception-B et E3-T1-conception-C sont présentes et complètes : chacune se termine par sa ligne de clôture, et aucune n'est tronquée. Le manuscrit et le script cités dans FAITS ne sont pas transmis ; je n'en reconstitue pas le contenu. La partie « diffusion et anonymat » des deux pièces n'est pas une question de méthode : je ne l'évalue pas ici.

---

## 0. Calculs de référence

Les calculs ci-dessous partent uniquement des formules de FAITS §1. Les notations sont $p_k = \pi_0(\Pi_k)$, $R_{\mathrm{h}} = R_0$ et $R_{\mathrm{v}} = R_{\mathrm{f}} = R_0 + \Delta R$. On suppose $\beta$ constante par classe, ce qui est l'hypothèse du modèle.

Chaque dérivation est affichée pour être vérifiable ligne à ligne. Ce sont mes calculs, pas des résultats du manuscrit.

- **D1 (niche $\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$).** Les poids de $\Pi_{\mathrm{h}}$ et de $\Pi_{\mathrm{f}}$ sont identiques sous A et sous B. Seul le poids de $\Pi_{\mathrm{v}}$ diffère : il vaut $\beta_{\mathrm{v}} e^{\eta(R_0+\Delta R)} p_{\mathrm{v}}$ sous A et $e^{\eta[\beta_{\mathrm{v}}(R_0+\Delta R) - (1-\beta_{\mathrm{v}})C]} p_{\mathrm{v}}$ sous B. On en déduit :
  - $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}(\Pi_{\mathrm{f}}) \iff \eta(1-\beta_{\mathrm{v}})(R_0+\Delta R+C) > \ln(1/\beta_{\mathrm{v}})$.
  - La condition de C est donc exacte, et l'amplification annoncée dans FAITS est un régime, pas une propriété inconditionnelle.
  - Quand $\beta_{\mathrm{v}} \to 0$, cette amplification exige $\eta \to \infty$.
- **D2 (détecteur indépendant de la classe, $\beta \equiv b \in (0,1)$).**
  - A se réduit à l'inclinaison exponentielle $e^{\eta R}\pi_0$, puisque $b$ se simplifie.
  - B donne $\eta[bR - (1-b)C] = b\eta R + \text{cte}$, c'est-à-dire la même inclinaison à intensité $b\eta$.
  - À $\eta$ égal, B porte donc moins de masse de tricheurs que A. À divergence KL égale, A et B coïncident.
- **D3 (audit hors boucle sous A).** Comme $R$ est constant sur les tricheurs, $\pi_{\mathrm{A}}(\cdot \mid \text{triche}) \propto \beta \, \pi_0(\cdot \mid \text{triche})$. Pour un auditeur dont l'indicateur de *manqué* est $m$ :
  - $\mathrm{FNR}_{\mathrm{A}} - \mathrm{FNR}_0 = \mathrm{Cov}_{\pi_0 \mid \text{triche}}(\beta, m) \,/\, \mathbb{E}_{\pi_0 \mid \text{triche}}[\beta]$.
  - Le signe pertinent est donc celui de la covariance entre la survie en boucle et le *manqué* de l'audit, non sa détection.
- **D4 (invariance d'un rapport).** Le rapport $\pi(\Pi_{\mathrm{f}})/\pi(\Pi_{\mathrm{h}})$ ne dépend ni de $p_{\mathrm{v}}$ ni de $\beta_{\mathrm{v}}$, sous A comme sous B.
- **D5 (classifieur et variation totale).** Pour tout classifieur, $\mathrm{TPR} - \mathrm{FPR} \le d_{\mathrm{TV}}$. Un classifieur ne fournit donc qu'une **borne inférieure** de $\delta_{\mathrm{ind}}$.
- **D6 (seuil de dominance sous A, sans coût de maintien).** $\Pi_{\mathrm{f}}$ domine $\Pi_{\mathrm{h}}$ si et seulement si $\eta\Delta R > \ln(p_{\mathrm{h}}/p_{\mathrm{f}}) + \ln(\beta_{\mathrm{h}}/\beta_{\mathrm{f}})$.
- **D7 (paramètre effectif de B).** B est invariant par translation conjointe de $(R, -C)$. Il dépend de l'écart $R_0 + C$, et non de $C$ seul.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Le bras « A » n'est pas identifié.**
   - Le préambule de B montre lui-même que le masquage de récompense converge vers $\pi_{\mathrm{B}}^{(\eta,0)} \neq \pi_{\mathrm{A}}$.
   - Pourtant, E1 entraîne « sous rejet pur (opérateur A) » sans préciser l'implémentation.
   - Si le bras A est réalisé par masquage, E1 compare en réalité $\mathrm{B}(C)$ à $\mathrm{B}(0)$. Or, dans la niche, $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}})$ croît strictement avec $C$ pour tout $\eta$. $H_{1\mathrm{A}}$ devient alors vraie par construction dans le modèle tabulaire, et la condition D1 disparaît.
   - Pour réaliser A, il faut soit un affinage par échantillonnage de rejet, soit une ancre KL vers $\beta\pi_0$. Il faut aussi dire comment cette ancre est estimée.
2. **Les classes sont étiquetées par le verdict du détecteur, ce qui rend le résultat vrai par construction.**
   - $\Pi_{\mathrm{f}}$ est défini comme le contournement « passant le filtre d'entraînement ($\beta_{\mathrm{f}} \approx 1$) ».
   - Si un épisode est classé furtif *parce qu'*il passe le filtre, l'enrichissement de $\Pi_{\mathrm{f}}$ sous détecteur est une tautologie, et $\beta_{\mathrm{f}} = 1$ par définition.
   - Les classes doivent être fixées avant l'entraînement par un critère aveugle au détecteur (signature d'arbre syntaxique, oracle caché). Les $\beta_k$ doivent être estimés à part, sur des échantillons tenus à l'écart.
   - L'hétérogénéité interne aux classes pose un problème supplémentaire. Le RL sélectionne, à l'intérieur de $\Pi_{\mathrm{v}}$, les variantes qui survivent. Une hausse apparente de $\Pi_{\mathrm{f}}$ peut donc n'être qu'une dérive intra-classe reclassée. Le modèle à trois régimes est alors mal spécifié dès que $\mathrm{Var}(\beta \mid \text{classe}) > 0$.
3. **La prédiction de E1 est rendue inconditionnelle.**
   - $H_{1\mathrm{A}}$ s'appuie sur le résultat de niche marqué VÉRIFIÉ, sans la condition D1.
   - Avec $\beta_{\mathrm{v}} = 0{,}20$ (illustratif), il faut $0{,}8\,\eta(R_0+\Delta R+C) > \ln 5 \approx 1{,}61$.
   - De plus, $\beta_{\mathrm{f}}, \beta_{\mathrm{h}} \ge 0{,}98$ n'est pas la niche $\beta = 1$ des FAITS.
   - La prédiction tabulaire doit être calculée par substitution des paramètres estimés ($\hat p_k, \hat\beta_k, \Delta R, C, \eta$) et pré-enregistrée avant l'entraînement.
4. **Le contrôle négatif de E1 ne contrôle rien.**
   - B prédit $\Delta_{\mathrm{BA}} < 0$ pour le détecteur « oracle » $\beta_{\mathrm{f}} = \beta_{\mathrm{v}} = 0{,}10$, $\beta_{\mathrm{h}} = 1$. Cette prédiction n'est pas impliquée par le modèle.
   - Quand $\eta \to 0$, A multiplie la masse des tricheurs par $0{,}1$, alors que B tend vers $\pi_0$. B porte donc *plus* de tricheurs que A à faible $\eta$.
   - Le plancher $\frac{\beta_{\mathrm{h}}-\beta_{\mathrm{f}}}{\beta_{\mathrm{f}}}C$ est un seuil de dominance de $\Pi_{\mathrm{f}}$ sur $\Pi_{\mathrm{h}}$, et non un énoncé sur $\Delta_{\mathrm{BA}}$.
   - C'est donc une seconde prédiction dépendante du régime, pas un contrôle à effet nul.
5. **$\eta$ et $C$ ne sont pas identifiables sous GRPO ou PPO.**
   - GRPO normalise les avantages par groupe (variante exacte : référence à vérifier). L'échelle effective de la récompense est alors de l'ordre de $1/\hat\sigma_{\text{groupe}}$ et varie selon l'invite.
   - La pénalité $-C$ augmente la dispersion intra-groupe. « Même $\eta$ » dans les deux bras ne signifie donc pas même intensité effective.
   - Par D7, le paramètre à faire varier et à rapporter est $(R_0+C)/\Delta R$, et non $C$.
6. **E2 conjoint deux hypothèses et laisse un signe ambigu.**
   - $H_{2\mathrm{A}}$ mêle la condition (covariance) et l'issue (FNR stable). Par D3, l'issue découle de la condition sous A. E2 ne peut donc tester que la *transposition* du modèle, ce qui exige de prédire le signe de $\Delta\mathrm{FNR}$ à partir de la covariance mesurée sur $\pi_0$ avant RL.
   - B écrit « covariance non positive avec la survie $\beta$ » sans dire s'il s'agit de la détection ou du manqué de la sonde. Les deux lectures donnent des signes opposés.
   - $\Delta\mathrm{FNR}$ confond deux effets : (i) la sélection de composition, que le théorème couvre ; (ii) la dérive représentationnelle d'un même comportement, que le théorème ne couvre pas.
   - Il y a aussi une fuite. La sonde est calibrée sur un $\pi_0$ ensemencé par affinage supervisé, dont les exemples furtifs sortent du même générateur que la définition de l'oracle. La sonde peut donc apprendre le gabarit du générateur plutôt que la triche.
7. **E3 est vrai par construction et ses hypothèses ne sont pas exclusives.**
   - « Respecte la borne » est garanti si les hypothèses du théorème tiennent.
   - Une borne inférieure ne prédit aucune « chute abrupte ».
   - « Borne respectée » et « borne lâche » ($H_{3\mathrm{B}}$) sont compatibles, ce qui viole B4.
   - Les métriques ne coïncident pas. La borne porte sur l'interception sur les pièges, alors que $H_{3\mathrm{B}}$ porte sur la suppression de la triche ordinaire.
   - $\tau_{\mathrm{ord}}$ est une variable post-traitement.
   - L'instrument 3 valide « $\delta_{\mathrm{ind}} \le 0{,}10$ » par un avantage de classifieur $\le 0{,}10$. Par D5, c'est la mauvaise direction : un classifieur faible ne borne pas $\delta_{\mathrm{ind}}$ par le haut, et la borne d'interception devient alors optimiste.
8. **E4 a plusieurs failles.**
   - Le dosage supervisé de $p_{\mathrm{f}}$ modifie aussi la compétence et le style : c'est une variable confondante.
   - Un $R^2 \ge 0{,}90$ sur quatre points log-espacés est presque garanti par la seule monotonie.
   - La condition nécessaire et suffisante des FAITS inclut un coût de maintien, et D6 contient le décalage $\ln(\beta_{\mathrm{h}}/\beta_{\mathrm{f}})$. $H_{4\mathrm{A}}$ omet les deux.
   - Le contrôle $\Delta R = 0$ oblige à récompenser via les tests cachés. L'oracle entre alors dans la boucle, sauf si l'on utilise un jeu de tests disjoint.
9. **L'instrument 4 n'est pas jugeable.** « $\mathrm{TPR} \ge 0{,}99$ » pour l'oracle suppose une vérité de terrain au-delà de l'oracle lui-même, et il n'y en a pas.
10. **La puissance n'est pas « garantie ».** E1 annonce une puissance garantie sans aucun calcul de puissance (voir (b)).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Variance de $\beta$ nulle.** Si $\mathrm{Var}_{\pi_0}(\beta \mid \text{triche}) = 0$, tout enrichissement est nul (FAITS). Empiriquement, c'est le cas où les intervalles de $\hat\beta_{\mathrm{v}}$ et $\hat\beta_{\mathrm{f}}$ se chevauchent.
- **E1 près de la frontière D1.** Si $\eta(1-\hat\beta_{\mathrm{v}})(R_0+\Delta R+C) \approx \ln(1/\hat\beta_{\mathrm{v}})$, l'écart prédit est proche de $0$. E1 devient indécidable lorsque l'intervalle de la prédiction tabulaire (obtenue par la méthode delta ou par rééchantillonnage sur les $\hat\beta_k$) chevauche à la fois $0$ et le seuil de $0{,}05$ (illustratif).
- **Nombre de graines.** Il faut $n \ge 2(z_{1-\alpha}+z_{1-\beta})^2 \sigma_{\text{graine}}^2 / \Delta^2$. Avec $\alpha = 0{,}01$ unilatéral et une puissance de $0{,}8$, on obtient $n \ge 20\,\sigma^2/\Delta^2$. Pour $\Delta = 0{,}05$ et $n = 10$ (illustratifs), cela suppose $\sigma_{\text{graine}} \lesssim 0{,}035$. Le test de Wilcoxon signé exige en outre un appariement réel des bras : même initialisation, même ordre des données.
- **Événements rares.** $\hat\pi(\Pi_{\mathrm{f}})$ suit une loi binomiale. Pour $p_{\mathrm{f}} = 10^{-4}$ (E4, illustratif), il faut de l'ordre de $3 \cdot 10^4$ tirages pour seulement distinguer $p_{\mathrm{f}}$ de $0$ (règle de trois). Si $p_{\mathrm{f}} < 1/(N_{\text{lot}} T)$, $H_{4\mathrm{B}}$ est réalisée par conception.
- **E2, covariance quasi nulle.** Si $\mathrm{Cov}_{\pi_0 \mid \text{triche}}(\beta, m) \approx 0$, D3 prédit $\Delta\mathrm{FNR} \approx 0$, et le seuil de $+0{,}05$ ne sépare rien.
- **E2, peu de tricheurs.** La puissance dépend de $n_{\text{triche,éval}} \cdot \mathrm{FNR}(1-\mathrm{FNR})$. Ce nombre est petit dans le bras qui triche le moins.
- **E3, régime vide.** Si $\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$, la borne vaut $0$ et le théorème ne prédit rien. Un marqueur stylistique déterministe et séparable pousse $d_{\mathrm{TV}}$ vers $1$.
- **Normalisation de groupe.** Si l'écart-type intra-groupe tend vers $0$ (tout réussit ou tout échoue), l'avantage est nul ou indéfini, et l'intensité effective n'est pas bornée.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Étiquettes aveugles au détecteur.** On reclasse les épisodes sans accès au verdict en boucle. Si la fraction $\Pi_{\mathrm{f}}$ change, il y a fuite.
2. **Banc tabulaire exécuté par le même code RL** (bandit à trois bras).
   - $H_{\mathrm{A}}$ : le code converge vers $\pi_{\mathrm{A}}$ et $\pi_{\mathrm{B}}$ à l'erreur Monte-Carlo près.
   - $H_{\mathrm{B}}$ : il s'en écarte de façon reproductible.
   - Chaque issue falsifie quelque chose : soit l'identification des bras, soit la lecture de E1 comme test du modèle.
3. **Détecteur indépendant de la classe ($\beta \equiv b$).** À KL appariée, D2 prédit $\mathrm{A} = \mathrm{B}$ exactement. À $\eta$ apparié, D2 prédit un écart connu. Sans ce contrôle, on ne peut pas séparer l'effet de sélection de l'effet de budget KL.
4. **Comparaison A contre A sur graines différentes**, pour calibrer $\sigma_{\text{graine}}$.
5. **Décomposition composition / dérive par forçage du maître** pour E2. On fait passer les sorties post-RL dans $\pi_0$ et l'on sonde les activations de $\pi_0$.
   - $H_{\mathrm{A}}$ : le $\Delta\mathrm{FNR}$ obtenu égale le $\Delta\mathrm{FNR}$ total.
   - $H_{\mathrm{B}}$ : il existe un écart, imputable à la dérive.
6. **Jeux de tests disjoints** pour la récompense, les pièges et l'oracle, plus un contrôle de contamination des problèmes dans le pré-entraînement des modèles ouverts. Cette contamination gonflerait $p_{\mathrm{h}}$.
7. **Construction de $\delta_{\mathrm{ind}}$ par mélange.** Les pièges sont formés d'une fraction $1-q$ indiscernable et d'une fraction $q$ marquée, avec un marqueur absent du trafic ordinaire. On a alors $d_{\mathrm{TV}} = q$ exactement, ce qui remplace un estimateur de variation totale impossible à obtenir en haute dimension.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Portée de deux constats « VÉRIFIÉ ».**
   - Le calcul de régime de C est exact (voir D1).
   - Le plancher demande une précision. Dès que $R_0 < 0$, il cesse d'être un minorant du seuil. Il perd sa positivité si et seulement si $R_0 + C \le 0$, et non seulement « si $R_0 < 0$ avec $R_0+C<0$ ».
   - L'énoncé « filtrage itératif où $\beta$ se composerait au fil des tours » ne découle pas des formules de FAITS. Il dépend d'un algorithme que C ne spécifie pas. Seule l'indépendance de $\beta$ vis-à-vis de $\eta$ en découle. Je ne modifie pas le statut ; je signale que la portée de la vérification est plus étroite que l'énoncé.
2. **Bras A non identifié.** C'est le même défaut que chez B : l'expérience 1 entraîne un « filtrage par rejet sans pénalité » non spécifié.
3. **L'appariement sur la divergence KL change l'estimande.**
   - Les FAITS comparent A et B à $\eta$ égal. À KL égale, la prédiction tabulaire doit être recalculée. C ne le fait pas, alors que $H_{\mathrm{A}}$ en dépend.
   - La KL est une variable post-traitement. Si les bras atteignent la même KL à des nombres de pas différents, le nombre de pas devient une variable confondante.
   - Avec $\beta_{\mathrm{h}} \approx 0{,}95$ et $\beta_{\mathrm{f}} \ge 0{,}90$ (illustratifs), on est hors de la niche. Les FAITS y donnent un plancher, pas une amplification : $H_{\mathrm{A}}$ extrapole.
4. **La dépendance en $R_0$ est découverte mais jamais testée.** Avec la normalisation de groupe, une translation commune de toutes les récompenses est invisible. Seul compte l'écart $R_0+C$ (D7). C utilise GRPO sans relier ce fait à son propre constat.
5. **Expérience 2 : la référence tabulaire est fausse.**
   - Bloquer $\Pi_{\mathrm{v}}$ modifie $\pi_0$ et la constante de normalisation. Le modèle *statique* prédit donc lui-même des $\pi(\Pi_{\mathrm{f}})$ différents entre les deux bras.
   - Le contrôle « Gibbs tabulaire, écart $< 0{,}01$ » est donc mal posé.
   - La statistique adéquate est le rapport $\pi(\Pi_{\mathrm{f}})/\pi(\Pi_{\mathrm{h}})$, invariant par D4.
   - « Apparier $\pi_0(\Pi_{\mathrm{f}})$ à $\pm 10\,\%$ » en retirant $\Pi_{\mathrm{v}}$ réalloue la masse vers $\Pi_{\mathrm{h}}$ et $\Pi_{\mathrm{f}}$.
   - La « suppression précoce » est un troisième opérateur, non modélisé.
6. **Expérience 3 : une conjonction peu informative.**
   - $H_{\mathrm{A}}$ exige aussi que le juge texte se dégrade. Or le moniteur de surface en boucle et le juge texte lisent tous deux le texte : leur covariance positive est quasi construite. La dégradation du juge est donc presque certaine et n'apporte rien.
   - Le cas « sonde stable et juge stable » n'est couvert ni par $H_{\mathrm{A}}$ ni par $H_{\mathrm{B}}$.
   - La confusion entre composition et dérive est la même que chez B. Le contrôle sans détecteur ($\beta \equiv 1$) n'isole la dérive générique que si la KL est appariée.
7. **Expérience 4 : une mesure circulaire.**
   - La « $\mathcal{F}$-IPM mesurée par un classifieur de même capacité que la politique » est circulaire. Un classifieur supervisé minore l'IPM de *sa* classe (analogue de D5). Il ne borne pas la capacité discriminante qu'acquiert la politique sous pression RL.
   - Conditionner sur « $\tau_{\mathrm{ord}} \ge 0{,}30$ » revient à sélectionner sur une variable post-traitement.
   - Si les pièges sont vérifiés avec le même jeu de tests cachés que l'oracle, il y a fuite.
8. **Fuite entre construction et évaluation de l'instrument, la plus grave de la pièce C.**
   - Dans la table de la partie D, le critère de fonctionnement de la sonde inclut « dérive $\Delta\mathrm{FNR} \le +0{,}03$ ». C'est exactement $H_{\mathrm{A}}$ de l'expérience 3.
   - Une sonde qui réaliserait $H_{\mathrm{B}}$ serait donc déclarée non fonctionnelle et écartée. $H_{\mathrm{B}}$ devient inobservable.
   - Le même défaut touche le dispositif de pièges, dont le critère « $\tau_{\mathrm{trap}} \ge \max(0{,}25, \tau_{\mathrm{ord}} - 0{,}05)$ » est $H_{\mathrm{A}}$ de l'expérience 4.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Résolution des tests avec 5 graines (illustratif).**
  - En appariement par inversion de signe, il n'y a que $2^5 = 32$ configurations : la plus petite valeur $p$ bilatérale vaut $1/16$. Le seuil « $p < 0{,}01$ » est alors inatteignable.
  - En comparaison 5 contre 5 non appariée, il y a $\binom{10}{5} = 252$ partitions : la plus petite valeur $p$ bilatérale vaut environ $0{,}008$. Le seuil n'est atteint qu'à la configuration de rangs extrême.
  - Le test d'équivalence TOST à marge $0{,}03$ (illustratif) exige $\sigma_{\text{graine}}$ très petit devant $0{,}03$.
- **Fenêtre de KL trop large.** Si la pente locale $|\mathrm{d}P_{\mathrm{f}}/\mathrm{d}\,\mathrm{KL}| \times 0{,}05\,\mathrm{KL}$ est du même ordre que le seuil de $0{,}05$, l'appariement à $\pm 5\,\%$ suffit à lui seul à produire ou à masquer l'effet. L'expérience 1 est alors non jugeable.
- **Moniteur à $\beta = 0{,}5$.** Le contrôle $|\Delta P_{\mathrm{f}}| < 0{,}02$ n'est valide qu'à KL appariée (D2). À $\eta$ apparié, B équivaut à une inclinaison d'intensité $\eta/2$, et un écart non nul est *prédit*.
- **Expérience 3, peu de tricheurs.** $\widehat{\mathrm{FNR}}$ se calcule sur les tricheurs post-RL. Si le bras le moins tricheur en compte trop peu, l'intervalle de confiance couvre à la fois $+0{,}03$ et $+0{,}10$.
- **Expérience 4, régime jamais atteint.** Si $\tau_{\mathrm{ord}} < 0{,}30$ dans tous les bras, l'expérience est vide, et la décision de la conserver devient post hoc.
- **Classes indiscernables.** Si $\hat\beta_{\mathrm{f}}$ et $\hat\beta_{\mathrm{h}}$ ont des intervalles qui se chevauchent, on ne sait pas si l'on est dans la niche ou dans le régime à plancher. L'expérience 1 ne teste alors rien de défini.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Découpler l'acceptation des instruments et les issues mesurées.**
   - Valider la sonde et les pièges uniquement sur des données pré-RL tenues à l'écart.
   - Pour la sonde, ajouter un contrôle positif « sonde dans la boucle ». Par D3, on a alors $\mathrm{Cov}(\beta, m) = \mathrm{Var}(m) \ge 0$, donc une hausse prédite du FNR.
2. **Étiquettes aveugles au détecteur** et **jeux de tests disjoints**, comme pour B.
3. **Banc tabulaire exécuté par le même code RL**, comme pour B (avec $H_{\mathrm{A}}$ et $H_{\mathrm{B}}$ identiques).
4. **Expérience de translation de $R_0$**, tirée du propre constat de C. On déplace $R_0$ en gardant $-C$ fixe.
   - $H_{\mathrm{A}}$ : $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}})$ varie comme le prédit $(R_0+C)/\Delta R$, et $\pi_{\mathrm{A}}$ reste invariant.
   - $H_{\mathrm{B}}$ : $\pi_{\mathrm{B}}$ ne varie pas.
   - La première issue confirme que le paramétrage du manuscrit est celui que l'algorithme réalise. La seconde réfute ce paramétrage pour l'algorithme employé.
5. **Rapport $\pi(\Pi_{\mathrm{f}})/\pi(\Pi_{\mathrm{h}})$ dans l'expérience 2**, avec la prédiction tabulaire de l'écart entre bras calculée avant exécution.
6. **Comparaison double, à $\eta$ apparié et à KL appariée**, pour l'expérience 1. Sans ce double appariement, un désaccord avec les FAITS ne peut pas être attribué.
7. **Décomposition composition / dérive par forçage du maître** pour l'expérience 3, avec les hypothèses énoncées pour B.

FIN-DE-CELLULE