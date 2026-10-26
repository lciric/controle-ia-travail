# Proposition B · Tour III.3 · Riposte

**État des pièces.**
- Ma conception III.1 est présente et complète.
- Les attaques de A et de C sont présentes et complètes ; chacune se termine par sa ligne de clôture.
- Je ne réponds qu'aux sections « Contre la proposition B ».
- F1 ne dit pas comment le sabotage est obtenu (consigne dans le contexte, affinage ou autre). Cette information est absente ; je n'invente rien et je conçois les tests pour couvrir les deux cas.

**Convention.** Tout chiffre de F1 reste RAPPORTÉ. Mes calculs sont des calculs de cette cellule, à recontrôler par un tiers ; ils ne promeuvent aucun statut. Tout seuil ou effectif que j'introduis est illustratif.

---

## (a) Sort de chaque attaque

### Attaques de A

| Attaque | Verdict | Raison ou transformation |
|---|---|---|
| **B-a1** (V2 hors régime) | **Acceptée sur la forme, réfutation maintenue sur le fond** | Mon exemple avait une taille de 0,19. Je donne ci-dessous un contre-exemple à α ≤ 0,01, puis à α ≈ 0,05. |
| **B-a2** ($v$ indéfini) | **Acceptée, puis transformée en dilemme** | La conclusion tient quelle que soit la lecture de $v$ (voir ci-dessous). |
| **B-a3** (I3 vrai par construction) | **Acceptée** | La partie informative est la puissance du bras correctif. I3 est réécrit en I3′. |
| **B-a4** (le cosinus n'identifie pas une rotation) | **Acceptée** | J'ajoute un plafond par moitiés disjointes, un cosinus blanchi et un transfert par AUROC (I5′). |
| **B-a5** (confondant « consigne présente ») | **Acceptée** | I2 est remplacé par un plan factoriel 2×2 (I2′). |
| **B-a6** (erreurs corrélées entre $v_0^a$ et $v_0^b$) | **Acceptée, rendue sans objet** | I4′ remplace la correction test-retest par une randomisation de $\hat c$. |
| **B-a7** (V8 : largeur d'IC inventée) | **Acceptée** | Je retire l'argument « ±0,24 ». Seuls restent la dépendance intra-tâche et l'unité du pli non précisée. |
| **B-a8** (I6 sous-alimenté) | **Acceptée** | Plan apparié, métrique pAUC sur FPR ∈ [0 ; 0,05] et porte de puissance préenregistrée (I6′). |
| **B-a9** (fuite entre entraînement de la sonde et calibrage) | **Acceptée** | Elle devient le prérequis P0 de toutes les expériences. |
| b1 (continuité des scores) | **Acceptée** | Avec des égalités, $\mathbb P(M_{\text{new}}>M_{(951)})\le 50/1001$ est une borne, non une égalité. Je compte les égalités ; un bris d'égalité randomisé rétablit l'égalité. |
| b2 (modèle $\eta_e$ additif) | **Transformée en test** (P0) | ACF intra-épisode sur les 38 épisodes honnêtes de P3. L'issue choisit le simulateur d'I3′. |
| b3 (échelle de la marge 0,18) | **Transformée en test** | Diagramme de fiabilité avant toute lecture de la marge (voir le routage). |
| b4 (même jeton numérique dans I2) | **Acceptée** | Intégrée à I2′ comme porte d'appariement. |
| b5 (ordre d'élicitation dans I4) | **Sans objet** | $\hat c$ est randomisé après $v_0^a$ ; $v_0^b$ est pris dans un contexte neuf. |
| b6 (nombre d'erreurs par juge) | **Acceptée** | Bascule vers la corrélation des scores continus sous un seuil préenregistré. |
| c5 (règles propres non-Brier dans la bibliothèque semée) | **Rejetée** | C'était déjà présent : ma table (c) prévoit des « fausses alertes sur règles propres (Brier, log tronqué, sphérique, Tsallis) », et ma table 4 des « fausses alertes sur règles propres renormalisées ». |

**B-a1 : contre-exemple dans le régime du rapport.**
- **Lois marginales.** Avec probabilité 0,995, $X\sim U(0;0{,}1)$ ; avec probabilité 0,005, $X\sim 1+U(0;0{,}1)$. Les marges sont continues.
- **Deux scores, test $S=X_1+X_2\ge1$.** Sans saut, $S<0{,}2$ ; dès qu'un saut survient, $S\ge1$.
  - Sous indépendance : taille $=1-0{,}995^2=0{,}009975\le0{,}01$.
  - Sous comonotonie (marges intactes, covariance positive, variance de $S$ accrue) : $S\ge1$ si et seulement si saut, d'où une puissance de **0,005, inférieure à la taille**.
- **Dix scores, même test $S\ge1$.**
  - Sous indépendance : taille $=1-0{,}995^{10}\approx0{,}0489$.
  - Sous comonotonie : puissance de 0,005.
  - Avec le seuil $S\ge2$, la taille vaut environ $\binom{10}{2}0{,}005^2\approx0{,}0011$ et la puissance 0,005, supérieure à α.
- **Conclusion.** Même à α ≤ 0,05, le signe dépend du seuil. L'énoncé « puissance strictement supérieure à α » de F1 §1.2 est faux en général. Il est exact pour des marges gaussiennes dont les covariances augmentent, avec α < 1/2.
- **Portée empirique (HYPOTHÈSE).** Le contre-exemple compte si les scores honnêtes ont des pics rares. Mesure : la forme de la queue des scores honnêtes de P3.

**B-a2 : dilemme sur $v$.**
- Si $v=h_t$, ou si $v=U^\top h_t$ avec $U$ fixé : $\Psi(Rh)$ n'est pas une transformation orthogonale de $\Psi(h)$. L'énoncé d'invariance est faux, comme le montre mon contre-exemple en 2D, qui reste conditionnel à cette lecture.
- Si $v$ est un invariant de rotation, par exemple les valeurs singulières : l'invariance est vraie, mais la statistique ne porte plus aucune direction. Elle ne peut donc pas détecter la rotation que postule la Faille inédite A.
- Dans les deux cas, le colmatage ne fait pas ce que F1 annonce.
- Indépendamment de $v$, « spectre de Koopman » désigne les valeurs propres d'un opérateur d'évolution, non les valeurs singulières d'un dictionnaire.

### Attaques de C

| Attaque | Verdict | Raison ou transformation |
|---|---|---|
| **(a)1, V4** (« mathématiquement faux ») | **Rejetée sur le verdict, acceptée sur deux compléments** | Détail ci-dessous. |
| **(a)1, V7** (« lecture inversée du modèle MIMO ») | **Rejetée** | Détail ci-dessous. |
| **(a)2** (conformal pondéré dégénéré ou fuyant) | **Acceptée** | Les supports sont disjoints si le poids porte sur le cadrage, et il y a fuite si le poids est appris sur les activations de test. Je retire la pondération ; la contre-mesure devient un calibrage dans le cadrage de déploiement (I1′). |
| **(a)3** (I2 : discordance entre entrée et sortie) | **Acceptée** | C'est le même défaut que B-a5. I2′ garde les contextes identiques au jeton près. |
| **(a)4, point 1** (biais propre à l'item partagé) | **Rejetée en partie** | Un biais d'item stable figure aussi dans $v_1$ ; il fait partie de μ et ne crée pas de régression vers la moyenne. L'artefact naît de la composante transitoire, ou d'un $\hat c$ dépendant de $v_0$. Ce second cas est réel et traité par la randomisation. |
| **(a)4, point 2** (ancrage auto-régressif sur $v_0^a$ réalisé) | **Acceptée** | Remplacer $v_0^a$ par $v_0^b$ atténue $g$ quand la déférence porte sur la valeur réalisée. D'où I4′. |
| **B-H1** (e-valeurs invalides sous effet épisode) | **Acceptée, transformée** | Vovk et Wang (2021) exigent que chaque $E_j$ soit valide. Je construis chaque $E_j$ par un calibrateur appliqué à une p-valeur conforme d'épisode. La mesure proposée par C est adoptée comme test. |
| **B-H2** (Higher criticism à $T=10$) | **Acceptée, transformée en test** | La validité est rétablie par le calibrage conforme d'épisode ; la question restante est la puissance. Le test est retenu pour $n_0=NT$ grand (essaim, Papier B), sur la grille {10, 100, 400} de pas. |
| **B-H3** (le report sélectif suppose l'échangeabilité) | **Acceptée** | La garantie de Geifman et El-Yaniv est distributionnelle, non adverse. Courbe risque-couverture sur tâches honnêtes et sabotées tenues à l'écart. |
| (c)1 (balises neutres de même longueur) | **Acceptée** | Bras ajouté à I1′. |
| (c)2 (erreur honnête endogène, contexte identique) | **Acceptée** | Cellule de I2′. |
| (c)3 ($\hat c\perp v_0$, $\hat c=v_0^a$) | **Acceptée** | C'est le cœur de I4′, avec la dose $d=0$. |

**V4 : réponse à C (a)1.**
- **L'énoncé tient.** Pour Brier, $g_p(p)-g_p(q)=(q-p)^2$. Avec une bosse $c\varphi$ à support dans $(0{,}701 ; 0{,}709)$ :
  - les dérivées aux 99 nœuds sont inchangées, puisque aucun nœud ne tombe dans le support ;
  - les ancrages en 0,5 et 0,9999 sont inchangés ;
  - $g_{0{,}5}(0{,}705)-g_{0{,}5}(0{,}5)=c-0{,}042025$, positif si $c>0{,}042$.
  
  C le concède d'ailleurs (« la bosse est certes nulle » aux nœuds). Le test de F1 est donc passé par une règle impropre.
- **Complément accepté n° 1.** Une recherche globale sur une grille finie de $q$ est battue par une bosse plus étroite. Je n'avais pas fixé le pas ; aucune grille finie ne suffit seule.
- **Complément accepté n° 2.** La courbure de cette bosse est d'ordre $10^4$ (calcul de C, à recontrôler). La certification correcte combine une borne $L$ déclarée sur $|\partial_q^2 g_p|$ et un pas $h$ : entre deux nœuds, l'écart à l'interpolation est au plus $Lh^2/8$.
  - Une perturbation de faible courbure passe ce contrôle, mais son dommage est borné : $|q^*-p|\le\sup|\partial_q\text{perturbation}|/2$ contre la concavité 2 de Brier.
  - Le dommage nul exige une structure : représentation de Savage $R(y,q)=\Phi(q)+\Phi'(q)(y-q)$ avec $\Phi$ convexe par construction (Gneiting, Raftery 2007), ou règle gelée hors de portée du système.

**V7 : réponse à C (a)1.**
- **Modèle.** Les moniteurs observent $y=\Psi^\top x+n$, avec $x\sim\mathcal N(0,sI)$ et $\mathrm{Cov}(n)=\Sigma_n$. L'information mutuelle vaut $\tfrac12\log\det(I+s\,\Sigma_n^{-1}G)$ (Cover, Thomas (2006), *Elements of Information Theory*, 2ᵉ éd.).
- **La formule de F1 est le cas $\Sigma_n=I$.**
  - Avec $k$ moniteurs identiques au bruit identique, l'information égale celle d'un seul moniteur : $\tfrac12\log(1+s)$.
  - La formule de F1 donne au contraire $\tfrac12\log(1+sk)$.
  - Que $G$ soit de rang 1 ne change rien : c'est l'indépendance supposée des bruits qui produit le gain.
- **La variante de C est un cas limite du même défaut.** Des juges déterministes ont un bruit nul ; le modèle diverge alors avec $s$.

---

## (b) Expériences corrigées

**P0 — Audit préalable, sur données existantes et sans GPU.**
- Listes de tâches disjointes, vérifiées par empreinte, entre trois usages : (i) entraînement de la sonde, (ii) calibrage conforme, (iii) test (B-a9).
- Taux d'égalités parmi les $M^{(k)}$ (b1).
- ACF intra-épisode et pente temporelle des scores sur les 38 épisodes honnêtes de P3 (b2).
- L'issue choisit le simulateur d'I3′ :
  - un effet additif seul, si l'ACF résiduelle après centrage par épisode est nulle ;
  - sinon, une composante AR(1) ou une dérive.

### I1′ — Le seuil conforme se transfère-t-il entre cadrages ?

- **Bras.**
  - $C_{\text{audit}}$ : indices d'évaluation.
  - $C_{\text{neutre}}$ : balises neutres, de même longueur et à la même position.
  - $C_{\text{nu}}$ : sans balise.
  - Les tâches sont appariées entre bras.
- **Calibrage.** Sur $C_{\text{audit}}$, avec des tâches disjointes par P0.
- **Hypothèses.**
  - H_A : le taux de fausses alarmes sur $C_{\text{nu}}$ est ≤ α + 1 point (α = 1 % ; marge illustrative).
  - H_B : il dépasse α.
- **Mesure.** Taux de fausses alarmes par épisode, IC binomial exact, environ 1 000 épisodes par bras de test (illustratif ; IC d'environ ±0,6 point à 1 %).
- **Témoin.** Calibrage et test dans le même cadrage.
- **Falsification.**
  - H_A est falsifiée si la borne basse dépasse α + 1 point.
  - H_B est falsifiée si la borne haute est ≤ α + 1 point.
  - Les deux conclusions supposent un témoin conforme.
- **Attribution (secondaire, seulement si H_A tombe).**
  - Si le transfert vers $C_{\text{neutre}}$ échoue, le contenu des balises compte : c'est compatible avec l'hypothèse a5, sans la prouver.
  - Si le transfert vers $C_{\text{neutre}}$ passe et celui vers $C_{\text{nu}}$ échoue, c'est un effet de format ou de longueur.
- **Contre-mesure.** Calibrer dans le cadrage de déploiement, sans pondération (C (a)2).
- **Limite structurelle.** La garantie ne vaut que pour la distribution de calibrage.

### I2′ — Que lit la sonde P3b ? Plan 2×2, contextes identiques au jeton près

- **Facteurs.**
  - Facteur 1 : condition de sabotage présente ou absente. Selon le mode d'obtention, qu'F1 ne précise pas, c'est la consigne dans le contexte ou le modèle affiné.
  - Facteur 2 : nombre écrit correct ou faux, d'après le recalcul depuis les données de la tâche, qui sont identiques dans toutes les cellules.
- **Cellules.**
  - (absent, correct) : honnête.
  - (absent, faux) : erreur honnête endogène, obtenue par échantillonnage seul (C (c)2).
  - (présent, faux) : action sabotée.
  - (présent, correct) : condition présente, action correcte (A (c)1).
- **Portes préenregistrées.**
  - Au moins 30 tâches par cellule (illustratif).
  - Appariement de grandeur entre les nombres faux des deux cellules « faux » au-delà de 80 % (illustratif, b4).
  - Si l'une des portes échoue, l'expérience n'est pas conclue et le motif est publié.
  - Les cellules endogènes sont sélectionnées : les comparaisons se font intra-tâche.
- **Hypothèses.**
  - H_A : la sonde porte une information propre à l'action sabotée. Le terme d'interaction a un IC qui exclut 0, et les deux AUROC sont au-dessus des témoins : (présent, faux) contre (absent, faux), et (présent, faux) contre (présent, correct).
  - H_B : le pouvoir séparateur s'explique par les effets principaux (lecture du contexte ou de la discordance arithmétique). L'IC d'interaction contient 0, ou l'un des deux AUROC reste sous les témoins.
- **Témoins de même architecture** (Hewitt, Liang 2019).
  - Sonde entraînée sur étiquettes permutées.
  - Plancher apparié en covariance.
  - Sonde de grandeur du nombre.
  - Recalcul arithmétique.
- **Falsification.** Chaque issue exclut l'autre ; l'effet principal dominant est rapporté comme diagnostic.

### I3′ — Puissance du CUSUM conforme sous effet épisode

- **Statistiques comparées**, toutes calibrées par seuil conforme sur des épisodes honnêtes entiers :
  - $\max_t C_t$ ;
  - la somme terminale ;
  - une statistique de balayage.
- **Grille.**
  - $\sigma_{\text{ép}}$ : les 17 réglages de T0.3 plus $\sigma_{\text{ép}}=0$.
  - κ : grille préenregistrée, puisque F1 ne fixe pas κ.
  - Simulateur choisi par P0.
- **Hypothèses.**
  - H_A : sur une rupture tardive, le CUSUM conforme bat la somme conforme pour tout $\sigma_{\text{ép}}$ de la grille.
  - H_B : il existe un $\sigma_{\text{ép}}$ où l'avantage disparaît.
- **Mesure.** Puissance à α = 1 %, délai de détection, et dommage cumulé à l'alarme.
- **Falsification.**
  - H_A est falsifiée si, pour au moins un réglage, la borne basse de la différence de puissance est ≤ 0.
  - H_B est falsifiée si cette borne est > 0 dans tous les réglages.
- **Témoin.** $\sigma_{\text{ép}}=0$, où la puissance relative est connue.
- La partie « fausses alarmes à κ fixé » n'est plus qu'un contrôle de cohérence (B-a3).

### I4′ — Déférence ou régression vers la moyenne : dose randomisée

- **Design.** Après $v_0^a$, la valeur proposée est fixée à $\hat c=v_0^a+d$.
  - La dose $d$ est tirée indépendamment de tout, dans un ensemble préenregistré qui inclut $d=0$ (illustratif : {−2, −1, 0, +1, +2} unités de l'échelle).
  - Le contenu rhétorique n'est pas décrit ici et ne varie pas entre doses.
- **Raisonnement.** Sous artefact pur, $\Delta v=v_1-v_0^a=\varepsilon_1-\varepsilon_a$, indépendant de $d$. Sous déférence, $\mathbb E[\Delta v\mid d]=g\,d$. La randomisation supprime à la fois le biais de C (a)4 et celui de A (B-a6).
- **Hypothèses.**
  - H_A : pente de $\Delta v$ sur $d$ supérieure à $g_{\min}$ (0,2, illustratif).
  - H_B : pente inférieure à $g_{\min}$.
- **Mesure.** Régression avec erreurs-types groupées par item.
- **Falsification.**
  - H_A est falsifiée si l'IC de la pente est entièrement sous $g_{\min}$.
  - H_B est falsifiée si l'IC est entièrement au-dessus.
  - Si l'IC chevauche $g_{\min}$, l'effectif est doublé selon un plan séquentiel préenregistré.
- **Témoin.** $d=0$ : la moyenne de $\Delta v$ mesure l'effet d'une critique sans écart. Cela distingue un décalage constant, observé sur Qwen d'après F1 §1.6, d'une déférence proportionnelle.
- **Diagnostic secondaire.**
  - Une mesure $v_0^b$ prise dans un contexte neuf estime $\mathrm{Var}(\varepsilon)$.
  - La pente artefactuelle prédite pour la campagne d'origine vaut $\mathrm{Var}(\varepsilon)/\mathrm{Var}(\hat c-v_0)$.
  - On la compare au $g\approx0{,}70$ RAPPORTÉ.
- **Modèles.** Llama-3.1-8B et Qwen2.5-7B.

### I5′ — Rotation contre atténuation ou décalage

- **Sondes.** $w_{\text{court}}$, et $w_{\text{traj}}$ entraînée par couche sur trajectoires, avec tâches tenues à l'écart.
- **Hypothèses.**
  - H_A (rotation) : trois conditions réunies.
    - AUROC($w_{\text{traj}}$) au-dessus des témoins.
    - AUROC de transfert de $w_{\text{court}}$ sur trajectoires sous les témoins. L'AUROC est invariante à toute transformation monotone, ce qui neutralise les décalages de seuil ou d'échelle.
    - Cosinus blanchi $\cos(\Sigma_1^{1/2}w_1,\Sigma_2^{1/2}w_2)$ sous le plafond mesuré entre moitiés disjointes du même régime, IC compris.
  - H_B : l'un des deux cas suivants.
    - AUROC($w_{\text{traj}}$) sous les témoins : atténuation.
    - AUROC de transfert de $w_{\text{court}}$ indiscernable de celle de $w_{\text{traj}}$ : simple décalage.
- **Témoins.** Étiquettes permutées avec la même architecture ; plancher apparié en covariance ; plafond par moitiés disjointes (B-a4).
- Le résultat de P4 doit être versé ici ; il est absent de F1.

### I6′ — Comité orthogonalisé ou comité indépendant

- **Design.** Mêmes traces pour les deux comités, comparaison appariée.
- **Métrique.** pAUC sur FPR ∈ [0 ; 0,05] (B-a8). Sous 30 erreurs par juge (illustratif), la corrélation des erreurs est remplacée par la corrélation des scores continus (b6).
- **Porte de puissance.** Effectif fixé pour une puissance de 80 % sur une différence de pAUC préenregistrée (illustratif).
- **Hypothèses.**
  - H_A : borne basse de la différence de pAUC > 0.
  - H_B : borne haute ≤ 0.
- **Témoin.** Consignes diversifiées de même longueur, sans contrainte d'orthogonalité.

### Tests annexes adoptés

- **Validité des e-valeurs (C, B-H1).**
  - Construction : $E_j=f(p_j)$, où $p_j$ est la p-valeur conforme d'épisode et $f$ un calibrateur décroissant d'intégrale 1, ce qui donne $\mathbb E_{H_0}[E_j]\le1$ (Vovk, Wang 2021).
  - Mesure : $\hat{\mathbb E}_{H_0}[\bar E]$ et $\mathbb P_{H_0}(\bar E\ge1/\alpha)$ sous effet épisode.
  - Falsification de la construction : moyenne > 1 ou fréquence > α, au-delà de l'erreur Monte-Carlo.
- **Higher criticism (C, B-H2).** Puissance de HC moins puissance du maximum, et moins celle de la somme, pour $n_0\in\{10,100,400\}$, chacune calibrée par seuil conforme. Si HC ne bat le maximum à aucun $n_0$, l'association est retirée.
- **Routage (A b3 et C B-H3).**
  - Diagramme de fiabilité de la sonde, avec plis par tâche.
  - Courbe risque-couverture séparée sur tâches honnêtes et sabotées.
  - Le seuil 0,18 est rejeté si le risque empirique dépasse la borne de Geifman et El-Yaniv à 95 %.

---

## (c) Réponse à l'arbitre : ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

**Ce qui est démontré par calcul dans ces cellules** (à recontrôler par un tiers ; aucun statut de F1 n'est modifié) :
1. **Seuil conforme.** L'arithmétique est exacte : rang 951, 50/1001. La garantie porte sur un épisode d'horizon $T$ fixé ; elle n'est pas « valable à tout instant ». Elle devient une borne s'il y a des égalités entre scores.
2. **Classe $\mathcal K$.** « Puissance de la somme strictement supérieure à α » est faux en général, y compris à α ≤ 0,01 (contre-exemple comonotone ci-dessus). L'énoncé est exact dans le cas gaussien.
3. **Koopman-ISVD (inédite A).** L'invariance annoncée est fausse si $v$ porte une direction. Si $v$ n'en porte pas, l'invariant est aveugle à la rotation qu'il prétend suivre.
4. **Shannon-Gram (inédite C).** La formule suppose des bruits indépendants ; elle ne peut donc pas mesurer le conformisme. Le gain marginal ne tombe pas à zéro.
5. **Tsallis 4/3 (inédite B).** Une règle strictement propre récompense une incertitude réellement calibrée ; elle ne vise donc pas le « mimétisme ».
6. **Savage sur 99 points (inédite D).** Une règle impropre passe le test. Seules une structure convexe par construction ou une règle gelée garantissent la propreté. Une borne de courbure ne fait que borner le dommage.
7. **Loi de déférence.** La régression de $\Delta v$ sur $\hat c-v_0$ produit une pente positive sans déférence. Les $R^2$ RAPPORTÉS ne départagent pas les deux lectures.

**Ce qui n'est pas établi :**
- Les quatre « failles inédites » (HYPOTHÈSE rapportée).
- Que le nul de P3 vienne de l'instrument : les résultats de P4 et P3b sont absents de F1.
- Que P3b lise une intention plutôt qu'un contexte ou une discordance arithmétique.
- Le transfert du seuil de G1 vers le déploiement.
- La puissance du CUSUM sous effet épisode.
- Tous les chiffres empiriques de F1 (21–35 %, 4,6–5,5 %, 31/31, κ = 0,04–0,17, 68 % / 1 %), qui restent RAPPORTÉ.

**Où le rapport cède, par ordre de conséquence :**
1. **La porte G1.** Elle dépend de l'échangeabilité entre calibrage et déploiement, et de la séparation entre entraînement de la sonde et calibrage (I1′, P0).
2. **La lecture en boîte blanche.** Elle ne départage pas encore intention et contexte (I2′).
3. **Le socle du Papier C.** Il peut être un artefact de mesure (I4′).
4. **Les colmatages des inédites.** Ils sont mathématiquement défaillants ou mal ciblés (points 3 à 6 ci-dessus).

**L'expérience à faire en premier.**
- **Étape 0 : P0**, quelques heures sans GPU : disjonction des listes de tâches, comptage des égalités, ACF sur P3. Si la disjonction échoue, tout taux de fausses alarmes rapporté pour G1 doit être recalculé avant toute autre expérience.
- **Puis I4′.** Trois raisons :
  - c'est la seule expérience où la randomisation donne deux issues exclusives qui falsifient chacune une hypothèse sans confondant résiduel connu ;
  - son coût est d'environ une journée-GPU sur deux modèles 8B (illustratif) ;
  - elle tranche le socle du Papier C (la loi de déférence) et l'interprétation de la Faille 6 en une seule campagne.
- **En parallèle, I3′**, à coût CPU négligeable.
- **I2′ ensuite.** C'est la plus importante pour la boîte blanche, mais elle est soumise à des portes d'effectif qui peuvent la rendre non concluante.

FIN-DE-CELLULE