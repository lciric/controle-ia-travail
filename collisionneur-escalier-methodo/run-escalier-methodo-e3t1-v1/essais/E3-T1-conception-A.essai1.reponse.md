# Proposition A — Tour III.1 : escalier de configurations, seuil d'effet, puissance, arrêt

**Pièce FAITS** : le bloc ne contient aucun fait, par décision explicite de l'arbitre (message n° 28 § 1). Je n'en invente aucun. Tout chiffre ci-dessous est soit déduit du cadre énoncé dans la question (RAPPORTÉ), soit marqué « illustratif ».

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut | Pourquoi ça compte |
|---|---|---|---|
| A1 | 60 items suffisent pour résoudre δ = 0,05. | HYPOTHÈSE (réfutable par calcul, voir §1) | En famille 2, un seul item vaut 1/24 ≈ 0,042 de BA ; δ = 0,05 est à peine plus d'un item. |
| A2 | La BA est monotone croissante (ou concave) dans le coût. | HYPOTHÈSE | Les itérations d'amélioration peuvent dégrader (sur-correction) ; sans ça, le « plateau » n'est pas défini. |
| A3 | Les quatre axes de coût sont séparables (pas d'interaction forte). | HYPOTHÈSE | Un plan à un axe à la fois (OFAT) n'est valide que sous cette hypothèse. |
| A4 | Le budget accordé $b$ n'affecte la BA qu'à travers la dépense $s(b)$ (restriction d'exclusion). | HYPOTHÈSE | Si le système lit $b$ dans son invite et change de stratégie, l'estimateur par variable instrumentale est biaisé. |
| A5 | La variance entre graines est estimable avec deux répliques. | HYPOTHÈSE | Un estimateur de variance à 1 degré de liberté a un coefficient de variation ≈ 1 (χ²₁) ; il renseigne sur l'ordre de grandeur, pas sur la valeur. |
| A6 | Les deux familles sont des mesures indépendantes. | HYPOTHÈSE | Si la même ronde de mise au point sert aux deux, les erreurs sont corrélées ; il faut une analyse par famille et une agrégation prudente. |
| A7 | Le jeu tenu à l'écart l'est encore après plusieurs comparaisons. | OBSERVÉ-NON-AUDITÉ (dépend du journal des essais) | Chaque décision prise sur ces 60 items en consomme l'indépendance (malédiction du gagnant). |
| A8 | Les références triviales (0,69 et 0,50) sont stables entre versions du système. | RAPPORTÉ (valeurs données), stabilité HYPOTHÈSE | La référence 0,69 en famille 1 suggère un déséquilibre ou un biais de forme exploitable ; elle doit être recalculée à chaque version. |
| A9 | « Item sans réponse valide = erreur » est neutre entre bras. | HYPOTHÈSE | Les bras à sortie longue tronquée échoueront plus par ce canal : la différence mesurée peut être une différence de format, pas de classification. |
| A10 | Le coût par itération (10–22 USD) est constant entre bras. | Illustratif (la question le dit) | Le classement à égalité « le moins cher l'emporte » exige la dépense *réalisée*, pas le budget accordé. |

---

## (b) Expériences décisives, en duel

Chaque duel a un contrôle négatif commun : l'**essai A/A** — même configuration, deux graines, analysée exactement comme un essai A/B. Tout instrument qui déclare un effet sur un A/A est en défaut.

**Duel 1 — Résolution du jeu de test (préalable à tout).**
- H_A : la variance item-à-item d'un $\widehat{\Delta\mathrm{BA}}$ apparié est telle que δ = 0,10 est détectable avec puissance ≥ 0,8 à α = 0,05 sur 60 items.
- H_B : la puissance reste < 0,5 quel que soit le nombre de graines, parce que la composante item est irréductible.
- Métrique : puissance exacte du McNemar conditionnel au nombre d'items discordants $D$ (calcul fermé, §1) et puissance empirique par injection d'effet (flip de $\lceil \delta \cdot n \rceil$ items sur une réplique).
- Seuil : puissance 0,8.
- Issue : si le calcul sous H_A donne < 0,5 pour tout $D \le 15$, H_A est falsifiée et le plan de l'arbiter doit changer d'échelle (réserve d'items) avant tout escalier. Si > 0,8 à $D$ réaliste, H_B est falsifiée.

**Duel 2 — Séparabilité des axes (A3).**
- H_A : les effets principaux expliquent la BA ; les interactions à deux facteurs sont < δ.
- H_B : au moins une interaction (p. ex. sous-modèles × itérations) dépasse δ.
- Plan : factoriel fractionnaire $2^{4-1}$, résolution IV (8 configurations), un niveau bas / un niveau haut par axe ; puis 4 points supplémentaires « défaisant l'alias » (repli, foldover) si un contraste alias dépasse δ.
- Métrique : contraste d'interaction estimé, IC par bootstrap apparié sur items.
- Contrôle négatif : le contraste alias d'ordre 3 (attendu nul).
- Issue : contraste d'interaction avec borne inférieure d'IC > δ falsifie H_A (et rend l'OFAT invalide) ; tous les contrastes d'interaction avec borne supérieure < δ falsifient H_B.

**Duel 3 — Exclusion de $b$ (A4).**
- H_A : à dépense réalisée $s$ égale, $b$ n'a pas d'effet sur la BA.
- H_B : $b$ a un effet direct (le système change de stratégie en lisant son budget).
- Plan : deux bras à même $b$ mais le second avec la mention du budget retirée de l'invite ou remplacée par une valeur fictive $b'$ ; apparier les items dont $s$ est identique (à ±10 %, illustratif).
- Métrique : $\Delta\mathrm{BA}$ sur les paires à $s$ apparié.
- Contrôle négatif : A/A à $b$ identique.
- Issue : $\Delta \ne 0$ avec IC excluant 0 falsifie H_A → abandonner l'estimateur IV, garder l'intention de traiter. IC inclus dans $[-\delta, \delta]$ falsifie H_B.

**Duel 4 — Neutralité du canal « réponse invalide » (A9).**
- H_A : le taux de réponses invalides ne diffère pas entre bras de plus de 1 item.
- H_B : les bras à sortie longue perdent ≥ 2 items par invalidité.
- Métrique : nombre d'items invalides par bras, et $\Delta\mathrm{BA}$ recalculée en excluant les items invalides dans *les deux* bras (analyse de sensibilité).
- Issue : si $\Delta\mathrm{BA}$ change de signe quand on exclut les invalides, H_A est falsifiée et la métrique mesure un artefact de format.

**Duel 5 — Transposabilité entre versions.**
- H_A : la configuration gagnante sur la version $v$ reste ≥ δ meilleure que la base sur $v+1$.
- H_B : le classement n'est pas transportable (interaction configuration × version).
- Plan : sur $v+1$, réexécuter *obligatoirement* le bras de base (ancre) et le bras gagnant, même graines.
- Métrique : $\Delta\mathrm{BA}_{v+1}$ ; contrôle négatif : $\Delta$ ancre$_v$ vs ancre$_{v+1}$ (dérive de version).
- Issue : borne supérieure d'IC de $\Delta_{v+1}$ < 0 falsifie H_A ; borne inférieure > δ falsifie H_B.

---

## 0. Plan à coût croissant (« escalier »)

**Ordre des axes**, par structure de coût (RAPPORTÉ dans la question : ≈ 10 USD par ronde de mise au point, coût à l'item pour les autres ; illustratif) :

1. **Rondes de mise au point** — coût fixe, amorti sur tous les items futurs ; à explorer d'abord, car son coût marginal par item tend vers zéro.
2. **Nombre de sous-modèles par item** — coût multiplicatif par item ; souvent le plus gros levier et le plus cher.
3. **Itérations d'amélioration** — coût multiplicatif, et seul axe où A2 (monotonie) est le plus douteux.
4. **Longueur maximale** — en dernier : son effet passe largement par le canal « réponse invalide » (Duel 4).

**Définition d'un cran** : doublement géométrique (1, 2, 4, 8) plutôt que pas fixe en dollars, pour deux raisons : (i) si la BA est concave dans $\log(\$)$, le doublement donne des accroissements comparables entre crans ; (ii) le coût d'un cran reste proportionnel au coût du cran précédent, ce qui borne la dépense totale à ≈ 2× le dernier cran. Un pas fixe en dollars sur-échantillonne les bas coûts du premier axe et sous-échantillonne les hauts.

**OFAT ou factoriel fractionnaire ?** Deux voies, départagées par le Duel 2 :
- *Voie F* : commencer par le $2^{4-1}$ (8 runs, ~8 × 16 USD ≈ 130 USD illustratif, une graine) pour classer les axes par effet principal et repérer les interactions ; puis escalier OFAT sur les deux axes dominants seulement.
- *Voie O* : OFAT direct dans l'ordre ci-dessus. Moins cher si A3 est vrai, aveugle sinon.

**Valeur marginale** : $\widehat{\partial \mathrm{BA}/\partial \$}_{j,k} = \dfrac{\widehat{\Delta\mathrm{BA}}(k \to k{+}1)}{\bar s_{k+1} - \bar s_k}$, avec $\bar s$ la *dépense réalisée* moyenne par bras, pas le budget. IC par bootstrap apparié (§2). **Plateau** déclaré sur un axe quand deux crans consécutifs ont la borne *supérieure* de l'IC à 90 % de $\Delta\mathrm{BA}$ sous δ. Deux crans, pas un : un cran seul est à la merci d'une graine aberrante.

**Règle d'arrêt globale** : arrêter quand tous les axes sont en plateau, ou quand le coût par point de BA du prochain cran (coût du cran / borne inférieure de l'IC de $\Delta$, en points de 0,01) dépasse un prix $\lambda$ fixé *avant* le premier essai. Sans $\lambda$ scellé, « à égalité le moins cher » n'a pas de contenu opérationnel.

**Confusion $b$ / $s(b)$** — trois estimateurs, à produire tous les trois :
- *Intention de traiter (ITT)* : $\Delta\mathrm{BA}$ par budget *accordé*. C'est l'estimateur de la décision pratique (on accorde $b$, on ne contrôle pas $s$) et le seul sans hypothèse ; il est primaire.
- *Variable instrumentale* : $b$ randomisé comme instrument de $s$ ; estimateur de Wald $\widehat{\beta} = \Delta\mathrm{BA}/\Delta \bar s$. Hypothèses : pertinence (testable : $\Delta \bar s$ ≠ 0, F de première étape) et exclusion (A4, Duel 3). Si Duel 3 falsifie H_A, l'IV est à écarter.
- *Dose-réponse sur $s$ observé* : purement descriptive et **confondue par la difficulté** — le système dépense plus sur les items durs, donc $s$ élevé corrèle avec erreur, pente négative artefactuelle. Ne jamais l'utiliser pour décider ; l'afficher par item apparié (même item, deux bras) réduit mais n'élimine pas le biais.

**Transposabilité** : traiter la version comme un bloc ; toute nouvelle version impose l'ancre (Duel 5). Ne jamais comparer un bras exécuté sur $v$ à un bras exécuté sur $v+1$.

---

## 1. Seuil d'effet minimal δ : modèle de variance et puissance

**Modèle** (par famille, $n$ items, $K$ graines par bras, appariement item × graine) :
$$Y_{ki}^{(A)} - Y_{ki}^{(B)} = d_{ki} \in \{-1, 0, +1\},\qquad \widehat{\Delta\mathrm{BA}} = \frac{1}{K}\sum_k \sum_i w_i\, d_{ki},$$
$w_i = 1/(2 n_{c(i)})$ où $n_{c(i)}$ est l'effectif de la classe de l'item. Famille 2 : $w = 1/24$ ; famille 1 : $w \approx 1/36$ si 18/18 (la stratification exacte n'est pas donnée — RAPPORTÉ incomplet, ne pas inventer).

Décomposition (modèle mixte) : $d_{ki} = \delta_i' + u_i + v_k + e_{ki}$ avec
$$\mathrm{Var}(\widehat{\Delta\mathrm{BA}}) \approx \underbrace{\frac{\sigma_u^2 \bar w^2 n}{1}}_{\text{items, irréductible à items fixes}} + \frac{\sigma_v^2}{K} + \frac{n \bar w^2 \sigma_e^2}{K}.$$
Point décisif : **le premier terme ne diminue pas avec $K$**. Multiplier les graines ne sert qu'à faire tomber les deux derniers termes ; passé $K \approx 3$–4 (illustratif, dépend du rapport $\sigma_v^2/\sigma_u^2$), la puissance ne bouge plus.

**Puissance exacte sous l'hypothèse de discordance** (calcul montré, illustratif) : soit $D$ le nombre d'items discordants. Sous $H_1$, chaque item discordant favorise A avec probabilité $p$ telle que $\delta = D(2p-1) w$. Test exact de McNemar unilatéral, α = 0,05.

*Famille 2* ($n = 24$, $w = 1/24$), $D = 6$ (25 % d'items discordants, illustratif) :
- δ = 0,10 → $2p-1 = 0{,}40$, $p = 0{,}70$. Rejet seulement à 6/6 (p-valeur 1/64 = 0,016 ; 5/6 donne 0,109). Puissance = $0{,}7^6 \approx 0{,}12$.
- δ = 0,15 → $p = 0{,}80$ ; puissance $= 0{,}8^6 \approx 0{,}26$.
- δ = 0,05 → $p = 0{,}60$ ; puissance $\approx 0{,}05$ : indiscernable de α.

*Famille 1* ($n = 36$, $w \approx 1/36$), $D = 9$ :
- δ = 0,10 → $p = 0{,}70$ ; rejet à ≥ 8/9 (p-valeur 10/512 ≈ 0,020) ; puissance $= 9(0{,}7)^8(0{,}3) + 0{,}7^9 \approx 0{,}20$.
- δ = 0,15 → $p = 0{,}80$ ; puissance $\approx 0{,}44$.

*Agrégation des deux familles* (statistique pondérée, $D = 15$) : puissance ≈ 0,3 à δ = 0,10 et ≈ 0,55 à δ = 0,15 (illustratif, approximation normale ; la dépendance A6 la réduirait encore).

**Tableau de synthèse** (illustratif ; coût par bras avec 16 USD/itération et une itération par graine) :

| δ | Graines/bras pour saturer | Coût d'une comparaison à 2 bras | Puissance plafond (items fixes, $D$ = 25 %) |
|---|---|---|---|
| 0,05 | 2 (inutile d'aller plus loin) | ≈ 64 USD | ≈ 0,05–0,10 |
| 0,10 | 3 | ≈ 96 USD | ≈ 0,2–0,3 |
| 0,15 | 3 | ≈ 96 USD | ≈ 0,4–0,55 |

Conséquence : le seuil $\Delta \ge +0{,}10$ déjà exigé ailleurs est, sur 60 items, au-dessous de la résolution de l'instrument. Les seules manières d'atteindre 0,8 de puissance sont (i) davantage d'items (réserve), (ii) un $D$ plus élevé (bras très différents), ou (iii) accepter δ ≈ 0,20–0,25. Ce n'est pas une opinion : c'est le calcul ci-dessus, falsifiable par le Duel 1 si $D$ réel est très supérieur à 25 %.

**Formule de puissance générale à deux niveaux** (approximation normale) :
$$1-\beta = \Phi\!\left(\frac{\delta}{\sqrt{\sigma_I^2/n_{\mathrm{eff}} + \sigma_S^2/K}} - z_{1-\alpha}\right),\quad \sigma_I^2 = \mathrm{Var}(w_i d_i),\ n_{\mathrm{eff}} = n\ (\text{items fixes : } n \text{ ne croît pas}).$$

---

## 2. Analyses : avantages et pièges

- **Rééchantillonnage apparié à deux niveaux** : rééchantillonner les items (avec remise, par strate de classe), puis au sein de chaque item les graines ; recalculer $\widehat{\Delta\mathrm{BA}}$. Avantage : respecte la structure et les poids $w_i$ ; aucune hypothèse de forme. Piège : avec $K = 2$, le niveau graine est quasi-dégénéré ; avec 12 positifs en famille 2, les rééchantillons stratifiés sont très granulaires (IC en marches). Taux de couverture à vérifier sur A/A (§c).
- **McNemar exact** : conditionne sur $D$, exact, pas d'hypothèse de variance. Pièges : (i) suppose une seule graine ou des paires indépendantes — pooler $K$ graines gonfle artificiellement $D$ et viole l'indépendance ; (ii) ignore les poids $w_i$ (BA ≠ exactitude) ; on peut l'appliquer par classe puis combiner, ou le remplacer par un test de permutation sur $\sum w_i d_i$ (signes aléatoires des discordants), exact aussi et respectant la BA. Cette dernière variante est ma recommandation par défaut.
- **Modèle mixte items × graines** (logit, effets aléatoires croisés) : estime $\sigma_u^2, \sigma_v^2$ et prédit le gain de graines. Pièges : convergence instable avec $K = 2$ et $n = 24$ ; variance de graine estimée avec un degré de liberté quasi nul ; séparation complète (classe parfaitement prédite) fréquente en petit échantillon.
- **Bayésien avec fonction de perte** : prior sur $\Delta$ (p. ex. Beta sur la proportion de discordants favorables, ou Dirichlet sur les 4 cases de la table appariée), perte $L = -\Delta\mathrm{BA}\cdot 100\ \text{points} + \lambda \cdot \Delta\$$. Décision : monter si $E[L] < 0$. Avantage : intègre directement « à égalité le moins cher » et donne une zone grise naturelle (probabilité postérieure que $\Delta > 0$ entre 0,6 et 0,9, illustratif). Piège : avec 6 discordants, le prior pèse autant que les données — à sceller avant et à tester sur A/A.
- **Séquentiel avec dépense d'erreur** : n'a de sens que si quelque chose *arrive séquentiellement*. Ici les 60 items sont fixes ; le séquentiel ne s'applique qu'aux graines (peu de gain, §1) ou aux items tirés d'une réserve. Fonction de dépense α (Lan–DeMets) sur regards prédéfinis. Piège : arrêt précoce pour efficacité sur petit $D$ surestime $\Delta$ (biais d'arrêt).
- **Usage des deux répliques gratuites** : ne pas en tirer $\hat\sigma_v^2$ (1 ddl). En tirer la quantité robuste : le **taux de bascule par item entre graines** $\hat f = \#\{i : Y_{1i} \ne Y_{2i}\}/60$, qui calibre directement le bruit de graine attendu dans $D$ (sous A/A, $E[D] \approx 60 \hat f$), et sert de prior et de contrôle négatif.

---

## 3. Règle de décision gelée

À sceller avant le premier essai, par cran $k \to k+1$ :
1. **Monter** si la borne inférieure de l'IC bootstrap à 90 % de $\widehat{\Delta\mathrm{BA}}$ (ITT, agrégé par famille avec minimum sur les deux familles pour éviter qu'une famille masque l'autre) est > 0 *et* $\widehat{\Delta\mathrm{BA}} \ge \delta$ *et* coût/point ≤ $\lambda$.
2. **Rester** si la borne supérieure est < δ (plateau sur cet axe) ou si le cran dégrade une famille de plus de δ.
3. **Zone grise** sinon : une seule action permise, ajouter des items de la réserve (pas des graines) ; au plus une fois par cran.

**Pièges et parades** :
- *Multiplicité* : $m$ crans → $m$ tests ; Holm sur les p-valeurs, ou meilleur, garder un α global pour la *décision finale* seulement et traiter l'escalier comme exploration.
- *Régression vers la moyenne / malédiction du gagnant* : la configuration retenue parmi plusieurs a un $\hat\Delta$ biaisé vers le haut ; parade : confirmation sur réserve.
- *Effet plafond* : si la base est déjà à 0,95 en famille 1, δ = 0,10 est impossible ; convertir en « erreurs restantes réduites de x % ».
- *Items trivialement faciles* : repérés par la référence triviale (0,69 en famille 1 est élevé) ; les retirer du calcul de $D$ ne change pas le test (ils sont concordants) mais ils gonflent la BA absolue et masquent les différences — les signaler.
- *Dépendance entre familles* : analyse séparée, décision sur le minimum.
- *Graine aberrante* : rapporter chaque graine ; un $\Delta$ porté par une seule graine sur trois va en zone grise, pas en « monter ».
- *Réutilisation du jeu de 60* : trois régimes. (i) *Validation réutilisable* : accepter que les 60 items deviennent un jeu de développement ; la BA finale y sera biaisée vers le haut d'un montant inconnu. (ii) *Réserve intouchée* : geler $r$ items (p. ex. 20 par famille, illustratif) jamais regardés ; coût en puissance immédiat (40 items au lieu de 60 pour l'escalier, puissance ≈ ×0,8 illustratif), gain : une confirmation finale honnête. (iii) *Confirmation finale* : une seule comparaison base vs gagnant sur la réserve, à α plein, décision binaire. La voie (ii)+(iii) est la seule compatible avec « jeu tenu à l'écart » au sens strict ; (i) doit être étiquetée comme telle dans tout rapport.

**Coût par point de BA** : $C_k / (100 \cdot \underline{\Delta}_k)$, avec $\underline\Delta$ la borne inférieure de l'IC. Utiliser la borne inférieure, pas l'estimation ponctuelle, sinon un cran bruyant paraît toujours rentable.

---

## 4. Alternatives et ce qui les départage

- **Élimination successive / Hyperband** : alloue un petit budget à beaucoup de configurations, élimine la moitié, double. Conçu pour une *fidélité* (nombre d'époques, sous-échantillon de données) qui approxime la performance finale. Ici, la fidélité naturelle serait le nombre d'items — mais le jeu est déjà minuscule : éliminer sur 15 items revient à tirer au sort. Applicable seulement si une réserve de plusieurs centaines d'items existe ; alors le critère de « corrélation de rang entre faible et pleine fidélité » doit être mesuré avant usage.
- **Bandits sous contrainte de budget** : traitent le coût comme ressource consommée par tirage ; pertinents si les configurations sont nombreuses et les items abondants. Avec 4 axes × 3 crans et 60 items, l'espace des bras est petit et le bruit par tirage énorme ; le gain sur un plan factoriel est nul ou négatif.
- **Optimisation bayésienne multi-fidélité** (p. ex. BOHB) : utile quand les axes sont continus et les évaluations chères ; ici les axes sont discrets à 3–4 niveaux et l'évaluation coûte ≈ 16 USD : le plan factoriel + escalier couvre l'espace pour ≈ 200–400 USD (illustratif) sans modèle de substitution à ajuster.

**Ce qui les départage** : le rapport (nombre d'items disponibles) / (nombre de configurations). Au-dessous d'environ 10 items discordants attendus par comparaison, aucune de ces méthodes n'apporte de puissance ; elles redistribuent seulement un budget d'items insuffisant. La question à poser à l'arbitre est donc : *existe-t-il une réserve d'items ?* Sinon, factoriel fractionnaire + escalier à deux axes + confirmation sur réserve est la seule voie qui tienne le protocole.

---

## (c) Mesure minimale de chaque instrument

Banc commun : **cas honnêtes appariés** construits à partir des deux répliques gratuites. *Nul* : A/A (graine 1 vs graine 2 de la même configuration), répété par rééchantillonnage d'items. *Effet injecté* : à partir d'une réplique, basculer aléatoirement $\lceil \delta / w \rceil$ items vers la bonne réponse dans un « bras » fictif, pour δ ∈ {0,05 ; 0,10 ; 0,15}, 1000 tirages (illustratif). **Vérification mécanique à battre** : la règle naïve « monter si $\hat\Delta \ge \delta$ » sans variance ; tout instrument doit faire mieux qu'elle sur le couple (détection, fausse alerte).

| Instrument | Mesure minimale | Seuil de fonctionnement |
|---|---|---|
| Permutation / McNemar sur $\sum w_i d_i$ | Fausse alerte sur A/A ; détection à δ injecté | FA ≤ 0,05 ; détection rapportée telle quelle (attendue faible) |
| Bootstrap à deux niveaux | Couverture de l'IC à 90 % sur A/A (vrai $\Delta$ = 0) | Couverture ∈ [0,85 ; 0,95] ; sinon IC trop étroits (fausses alertes) |
| Modèle mixte | Biais de $\hat\sigma_v^2$ contre $\hat f$ des répliques ; taux de non-convergence | Convergence > 95 % ; sinon écarter |
| Bayésien + perte | Taux de « monter » sur A/A (doit être ≈ 0) et sur δ injecté | « monter » sur A/A ≤ 0,05 |
| Séquentiel (dépense α) | α cumulé observé sur A/A avec 3 regards | ≤ 0,05 ; biais de $\hat\Delta$ à l'arrêt rapporté |
| Détecteur de plateau | Sur un escalier simulé à BA constante : taux de « monter » (FA) ; sur pente δ/cran : taux de « rester » (manqué) | FA ≤ 0,10 par cran |
| Estimateur IV | Duel 3 ; F de première étape | F > 10 (règle usuelle, illustratif) |
| Factoriel $2^{4-1}$ | Contraste alias d'ordre 3 sur A/A ≈ 0 | Borne d'IC incluant 0 |
| Halving / bandit / BO multi-fidélité | Corrélation de Spearman entre classement à 15 items et à 60 items (sur bras simulés) | ρ > 0,7 ; sinon la fidélité basse n'est pas informative |

---

## (d) Ancrage matériel

- **Modèles ouverts** (pour répliquer le banc de calibration sans frais d'API) : un modèle à poids ouverts de taille intermédiaire (familles Llama 3, Qwen 2.5 ou Mistral — nommer la version exacte au moment de l'exécution, statut RAPPORTÉ pour l'existence des familles, aucune performance avancée).
- **Calcul** : 60 items × sorties de quelques milliers de tokens × (13 configurations de l'escalier × 3 graines) ≈ 2 500 appels ; sur un GPU unique de classe 80 Go, de l'ordre de quelques heures (illustratif). Le banc de calibration (§c) est du calcul CPU négligeable.
- **Coût API, illustratif** avec 16 USD/itération : factoriel $2^{4-1}$ × 1 graine ≈ 130 USD ; escalier à 2 axes × 3 crans × 3 graines ≈ 290 USD ; A/A de calibration (6 graines de la base) ≈ 100 USD ; confirmation sur réserve (2 bras × 3 graines) ≈ 100 USD. Total ≈ 600–650 USD. Rondes de mise au point ≈ 10 USD chacune en sus.
- Ce qui n'est pas budgété et conditionne tout : la **constitution d'une réserve d'items** étiquetés — coût humain non estimable ici.

---

## 5. Références (à vérifier avant citation ; aucune donnée d'identifiant)

- McNemar, Q. (1947). *Note on the sampling error of the difference between correlated proportions or percentages*. Psychometrika.
- Dietterich, T. G. (1998). *Approximate statistical tests for comparing supervised classification learning algorithms*. Neural Computation.
- Nadeau, C., Bengio, Y. (2003). *Inference for the generalization error*. Machine Learning.
- Demšar, J. (2006). *Statistical comparisons of classifiers over multiple data sets*. JMLR.
- Benavoli, A., Corani, G., Demšar, J., Zaffalon, M. (2017). *Time for a change: a tutorial for comparing multiple classifiers through Bayesian analysis*. JMLR.
- Brodersen, K. H., Ong, C. S., Stephan, K. E., Buhmann, J. M. (2010). *The balanced accuracy and its posterior distribution*. ICPR.
- Dror, R., Baumer, G., Shlomov, S., Reichart, R. (2018). *The hitchhiker's guide to testing statistical significance in natural language processing*. ACL.
- Card, D., Henderson, P., Khandelwal, U., Jia, R., Mahowald, K., Jurafsky, D. (2020). *With little power comes great responsibility*. EMNLP.
- Bouthillier, X. et al. (2021). *Accounting for variance in machine learning benchmarks*. MLSys (liste d'auteurs complète à vérifier).
- Jamieson, K., Talwalkar, A. (2016). *Non-stochastic best arm identification and hyperparameter optimization*. AISTATS.
- Li, L., Jamieson, K., DeSalvo, G., Rostamizadeh, A., Talwalkar, A. (2018). *Hyperband: a novel bandit-based approach to hyperparameter optimization*. JMLR (année à vérifier).
- Falkner, S., Klein, A., Hutter, F. (2018). *BOHB: robust and efficient hyperparameter optimization at scale*. ICML.
- Lan, K. K. G., DeMets, D. L. (1983). *Discrete sequential boundaries for clinical trials*. Biometrika.
- Box, Hunter, Hunter, *Statistics for Experimenters* (plans factoriels fractionnaires ; édition et année à vérifier).

---

**Ce que cette proposition peut perdre** : le Duel 1 — si la part d'items discordants réelle est bien supérieure à 25 %, mes calculs de puissance sont pessimistes et l'escalier à δ = 0,10 devient tenable sur 60 items. Je demande à l'arbitre les deux répliques gratuites pour mesurer $\hat f$ et $D$ avant de sceller δ.

FIN-DE-CELLULE