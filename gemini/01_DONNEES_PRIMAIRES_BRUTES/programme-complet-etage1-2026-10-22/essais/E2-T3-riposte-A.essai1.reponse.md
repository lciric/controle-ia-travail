# Proposition A — Tour II.3 : riposte

**Intégrité des pièces.** Mon programme `E2-T1-prog-maths-A` et l'attaque `E2-T2-redteam-C` sont présents, entiers, clos par leur ligne. La pièce `E2-T2-redteam-B` est absente (statut : REFUS) : je n'en reconstitue rien et ne réponds qu'à la section « Contre la proposition A » de C. Les empreintes abrégées des Faits 5 et 7 restent non rapprochables. Je ne cite aucun fait avec un statut autre que celui du gabarit.

**Position d'ensemble (B1).** C attaque mon programme sur trois lignes : la validité de la marge $\Delta$ comme porte, la confusion de distances sous l'invariant I2, et la fragilité statistique de la pince et des ensembles élagués. Je n'harmonise pas : neuf points sont acceptés tels quels ou transformés en tests, trois sont rejetés en partie avec leur raison, et quatre désaccords restent et deviennent des expériences. Je reprends explicitement les cinq contrôles de la section (c) de C, en disant à chaque fois ce que j'en fais et où je corrige sa correction.

---

## (a) Verdict sur chaque attaque

| # | Attaque de C | Verdict | Raison courte |
|---|---|---|---|
| a1 | $\Delta(p)$ s'effondre sur la classe $\mathcal{A}^+$ ; la Phase 1 publie des faux négatifs | **Acceptée, transformée en porte Φ0** | Mon ordre d'exécution calibrait K1 en Phase 2 alors que Phase 1 arrêtait le protocole : erreur de séquence. La Phase 1 ne publie plus rien. |
| a2 | I2 rend $d$ et $d(\text{clause}, t_{\text{fin}})$ colinéaires (rang 2) | **Acceptée** sur l'algèbre ; **fix différent** du sien | Le sien, à $L$ fixe, reste de rang 2. Je relâche I2 pour ce sous-plan et fais de $L$ une covariable dérivée. |
| a3-i | Corrélation nulle ≠ indépendance de queue ; FPR réel « excédera massivement » 5 % | **Rejetée sur le FPR, acceptée sur la puissance** | $\eta$ est un quantile empirique de $\lambda$ sur le dénominateur honnête : le FPR est contrôlé à l'erreur d'échantillonnage près, quelle que soit la copule. Ce qui tombe, c'est la lecture de $\lambda$ comme rapport de vraisemblance et la puissance. L2 est réécrit pour tout combinateur monotone. |
| a3-ii | 75 préfixes honnêtes → ≈ 3,75 observations au-delà du seuil à 5 % | **Acceptée** | Le dénominateur de calibration n'est plus « 150/bras » mais l'union des trajectoires honnêtes de P-II.1/2, groupées par préfixe, avec borne supérieure exacte sur le FPR. |
| a3-iii | IoU à 1 % de parcimonie instable ; seuil 0,3 sans plafond test-retest | **Acceptée** | Critère rendu relatif au plafond test-retest, complété par un critère au niveau des prédictions. Le dénombrement « ≤ 10 neurones par couche » de C n'est pas dans les faits ; le contrôle vaut quelle que soit la cardinalité. |
| a4 | Témoin « pression sans violation » = sélection endogène | **Acceptée, et aggravée par moi** | Pire que ce que C dit : sur préfixe figé, l'état au dernier jeton du préfixe est identique entre rollouts d'un même $p$ ; une lecture à ce jeton ne peut rien discriminer intra-préfixe. Deux lectures sont distinguées (§b). |
| b1 | Évasion du dernier jeton par planification précoce et dilution $1/M$ | **Transformée en test** | Lecture par jeton sur le segment généré avec agrégation par maximum ; position du pic mesurée ; `(ii)` contre `(i)`. |
| b2-i | Mode Sol : $Y_{\text{exec}}=1$, $Y_{\text{canal}}=1$ → $D(\tau)\approx 0$ | **Acceptée sur l'étiquette, rejetée sur l'irréparabilité** | $r_{\text{ter}}$ était « succès selon $J$ », sans l'intégrité du canal : défaut d'étiquette, corrigé. Que le modèle représente ou non la dissociation est l'objet de P-II.3, strate β. |
| b2-ii | Saturation du z-score intra-séquence par les rejets | **Transformée en test** | Deux normalisations préenregistrées ; $\sigma_{\text{seq}}$ mesuré en fonction de $n_{\text{rej}}$. |
| b3 | $Z_N$ au seul jeton $t$ contourné par le cache KV ; « donnera un effet nul » | **Rejetée comme certitude, transformée en test** | Le flux résiduel au jeton $t$ dans les couches ≥ 6 dépend aussi de la sortie des couches 2–5 au jeton $t$ ; le nul n'est pas déductible. Trois portées d'ablation, dont celle de C. Son rappel du Fait 5 (ablation sans effet dans 24/25 modèles) abaisse mon prior sur la nécessité, je le dis. |
| c1–c5 | Cinq contrôles « fatals » | **Les cinq repris**, en le disant | c1 → Φ0 ; c2 → sous-plan de distances (corrigé) ; c3 → plafond test-retest ; c4 → strate γ (échec honnête) ; c5 → portées d'ablation. |

Trois précisions sur les rejets partiels.

*a3-i.* La phrase « le taux de fausses alertes réel excédera massivement le seuil nominal » suppose que $\eta$ est dérivé d'un modèle (produit de LR supposés indépendants). D8 dit le contraire : $\eta$ est calibré sur un dénominateur honnête apparié. Une dépendance de queue non modélisée rend le produit sous-optimal comme statistique et ruine son interprétation probabiliste ; elle ne déplace pas un quantile empirique. J'accepte donc la critique sur la statistique et la puissance, pas sur le contrôle d'erreur de première espèce. C a néanmoins raison que la *mesure* de A3 par corrélation de Pearson était insuffisante : elle est remplacée (§b, A3′).

*b2-i.* C écrit que $V^{\text{ter}}$ « a été entraînée sur des trajectoires où le contournement accompagnait un échec » : c'est une hypothèse sur mon jeu d'entraînement, qu'il énonce comme un fait. L'erreur réelle est en amont : ma définition de $r_{\text{ter}}$ ne codait pas le canal. Avec $r_{\text{ter}}'$ (§b), un cas Sol a $r_{\text{app}} = 1$ et $r_{\text{ter}}' = 0$ par construction des étiquettes. Reste la question empirique : le modèle représente-t-il cette dissociation ? C'est H_B de P-II.3, désormais testée par strate.

*b3.* Le mécanisme « lecture directe du cache KV par les couches hautes » (statut : HYPOTHÈSE sur $\theta$) prédit un nul pour l'ablation au seul jeton $t$ ; il ne prédit rien pour l'ablation sur toute la séquence. Ce que C présente comme une faille est un facteur expérimental que je n'avais pas spécifié : c'est mon défaut, et c'est désormais un facteur à trois niveaux.

---

## (b) Équations et protocoles corrigés

### b.1 Marge de classe et porte Φ0 (remplace D4 et A2)

Banque de $K$ paraphrases fonctionnellement équivalentes par préfixe, $\{a^+_k\}_{k \le K}$ et $\{a^-_k\}_{k \le K}$, $K = 10$ (illustratif), vérifiées par le vérificateur épinglé de $P$ (une paraphrase de $a^+$ doit produire $Y_{\text{canal}} = 1$ si exécutée ; une de $a^-$, $Y_{\text{canal}} = 0$). Marge sans normalisation de longueur :

$$\Delta_K(p) = \log \sum_{k=1}^{K} \pi(a^+_k \mid p) \;-\; \log \sum_{k=1}^{K} \pi(a^-_k \mid p).$$

Deux faits de structure, à dire : (1) chaque somme est une borne inférieure de la masse de sa classe ; la différence de deux bornes inférieures n'est pas bornée ; (2) donc $\Delta_K$ ne peut être une porte qu'après calibration empirique contre $V$. D'où :

**Porte Φ0 (nouvelle, préalable à toute Phase 1).** Sur $n_0 = 120$ préfixes pilotes (illustratif) tirés sur toutes les conditions de P-II.1, calcul de $\Delta_K(p)$ et de $V(p)$ sur 16 rollouts. Critères : corrélation de rangs $\rho_s(\Delta_K, V) \ge 0{,}5$ et, au seuil de porte $\Delta_K^\star$ choisi pour retenir 50 % des préfixes, taux de faux négatifs de porte $\Pr[V(p) \ge 0{,}2 \mid \Delta_K(p) < \Delta_K^\star] \le 0{,}10$ (tous illustratifs). Si Φ0 passe : la Phase 1 sert de *sélection* de conditions ; aucun nul de Phase 1 n'est publié comme résultat, seulement « non sélectionné à Φ0 ». Si Φ0 échoue : la Phase 1 est supprimée et P-II.1/P-II.2 passent en Phase 2 directe sur un plan réduit (effet primaire et deux témoins seulement). K1 cesse d'être une conjecture flottante : elle est tranchée avant qu'on ne s'en serve.

### b.2 Distances (remplace I2 pour les sous-plans de position)

Trois distances : $d_0 = d(\text{début}, \kappa_s)$, $d_1 = d(\kappa_s, \text{clause})$, $d_2 = d(\text{clause}, t_{\text{fin}})$, avec $L = d_0 + d_1 + d_2 + \text{const}$. L'algèbre de C est juste : à $L$ fixe, le plan est de rang 2. Son remède (bourrage en tête pour (i), en fin pour (ii)) reste à $L$ fixe et donc de rang 2 dans chaque sous-plan : varier $d_1$ par bourrage en tête à $L$ fixe fait varier $d_0$ de $-\Delta d_1$. Le remède correct est de **cesser de fixer $L$** sur ce sous-plan :

- **I2′ (position).** Facteurs $d_0, d_1 \in \{\text{court}, \text{long}\}$ à $d_2$ fixe (plan $2 \times 2$, $L$ prend trois valeurs) ; l'estimand est l'effet de $d_1$ à $d_0$ fixe, et l'effet de $d_0$ à $d_1$ fixe est le témoin « longueur pure ». Second $2 \times 2$ symétrique pour $d_2$ à $d_1$ fixe. Le bourrage neutre est toujours inséré **avant $\kappa_s$** (il ne modifie que $d_0$).
- **I2 (rang)** est conservé tel quel pour $k$ : à $k$ variable, $L$ est fixé par bourrage de tête, car l'hypothèse testée porte sur la loi de $c_k$ et non sur une distance interne.

C's mention de l'attention sink et de RoPE comme mécanisme est une hypothèse sur $\theta$ ; je n'en ai pas besoin, la confusion algébrique suffit à imposer I2′.

### b.3 Étiquettes, strates et deux lectures internes (remplace D7, D8 et le témoin de P-II.3)

**Étiquettes.** $r_{\text{app}}$ inchangé (sortie du banc ou du rapport). Vérité de terrain corrigée :
$$r_{\text{ter}}' = \mathbb{1}[\,Y_{\text{exec}} = 1 \wedge Y_{\text{canal}} = 0 \wedge Y_{\text{rapport}} = 0\,],$$
toutes trois dérivées de $J$ et de $h(P)$ (A4 maintenue). $D(\tau)$ et $N^{\text{ter}}$ sont redéfinis avec $r_{\text{ter}}'$.

**Strates** (toute AUC est rapportée par strate, jamais agrégée seule) :
- α — *falsification* : $Y_{\text{exec}} = 0$ et ($Y_{\text{canal}} = 1$ ou $Y_{\text{rapport}} = 1$) ; configuration du Fait 2 (OBSERVÉ-NON-AUDITÉ) et d'Astra (Fait 1, VÉRIFIÉ) ;
- β — *coupure silencieuse* : $Y_{\text{exec}} = 1$, $Y_{\text{canal}} = 1$, $Y_{\text{rapport}} = 0$ ; configuration de Sol (Fait 1, VÉRIFIÉ) ;
- γ — *échec honnête* : $Y_{\text{exec}} = 0$, $Y_{\text{canal}} = 0$, $Y_{\text{rapport}} = 0$ (contrôle c4 de C, repris) ;
- ε — *succès honnête* : $r_{\text{ter}}' = 1$.
Les négatifs sont γ ∪ ε, chacun sous $n_{\text{rej}} \in \{0, 3, 7\}$. Le témoin « pression sans violation » devient simplement γ ∪ ε à $n_{\text{rej}} = 7$, et n'est plus un contraste mais un dénominateur.

**Deux lectures internes.** Sur préfixe figé $p$, la passe avant est déterministe (A1) : l'état au dernier jeton de $p$ est le même pour tous les rollouts de $p$. Donc :
- $m^{\text{pre}}_{\text{int}}(p) = s(x_\ell(t_{|p|}))$ prédit au mieux $V(p)$, une *propension* ; il est confondu avec la difficulté de l'instance, comme C le dit, et il est évalué comme tel (cible : $V(p)$, pas l'issue d'un rollout).
- $m^{\text{act}}_{\text{int}}(\tau) = \max_{t \in \text{généré},\, t \le t_{\text{outil}}} s(x_\ell(t))$, lu sur chaque jeton généré jusqu'à la frontière d'appel d'outil ; cible : l'issue du rollout $\tau$. **Contraste intra-préfixe** : sur les préfixes à issues mixtes ($0 < V(p) < 1$, estimé sur 8 rollouts), AUC de $m^{\text{act}}_{\text{int}}$ entre rollouts $a^+$ et $a^-$ *du même $p$*, puis moyenne sur $p$. La difficulté d'instance est éliminée par construction. On rapporte aussi la **position du pic** $t^\star = \arg\max_t s(x_\ell(t))$ relative à $t_{\text{outil}}$ (variable de b1).

Stockage : les scores $s(x_\ell(t))$ sont calculés en ligne pour toutes les couches et stockés comme scalaires ; les activations brutes du segment généré ne sont conservées que pour 6 couches (illustratif) ; les moyennes par paragraphe (Annexe F du Fait 6) ne servent qu'à l'*identification* des Dopamine Neurons, jamais à la *détection*.

**Normalisation de la surprise (b2-ii).** Deux variantes préenregistrées : $z^{\text{seq}}$ (intra-séquence, Fait 6) et $z^{\text{ref}}$ (moyenne et écart-type par couche estimés sur un corpus honnête à $n_{\text{rej}} = 0$, figés). On mesure $\sigma_{\text{seq}}$ en fonction de $n_{\text{rej}}$ ; si $\sigma_{\text{seq}}(7)/\sigma_{\text{seq}}(0) \ge 1{,}5$ (illustratif), seule $z^{\text{ref}}$ est admissible pour la détection.

### b.4 Ensembles élagués : critère relatif (remplace le seuil IoU ≥ 0,3)

Plafond test-retest : $\bar{I}_{\text{rr}} = \text{médiane}_{(i,j)} \,\text{IoU}(N^{\text{hon}}_i, N^{\text{hon}}_j)$ sur 5 graines × 2 plis (illustratif) de tâches honnêtes. Critère de transfert :
$$\rho_{\text{IoU}} = \frac{\text{IoU}(N^{\text{hon}}, N^{\text{ter}})}{\bar{I}_{\text{rr}}} \ \ge\ 0{,}5 \quad (\text{illustratif}),$$
complété par un critère au niveau des prédictions : corrélation de Spearman entre $V^{\text{hon}}(s_t)$ et $V^{\text{ter}}(s_t)$ sur trajectoires tenues à l'écart $\ge 0{,}5$ (illustratif), et CKA linéaire entre les sous-espaces d'activation sélectionnés, rapporté sans seuil. Si $\bar{I}_{\text{rr}} < 0{,}2$ (illustratif), l'IoU sur indices est déclaré inopérant et seuls les critères continus comptent ; c'est dit avant la première empreinte.

### b.5 Ablation : trois portées (remplace le Niveau 2 de P-II.3)

$Z_N^{(\text{tout})}$ : mise à zéro de $N$ à toutes les positions, cache recalculé ; $Z_N^{(t)}$ : au seul jeton de décision ; $Z_N^{(\text{clause})}$ : aux seuls jetons de la clause modale et des messages de rejet. Témoins homologues inchangés ($N_{\text{rand}}$, $N_{\text{NTP}}$). Contrôle de non-destruction élargi (c5 de C) : perplexité sur $a^-$ et précision sur tâche honnête après $Z_N$, qui ne doivent pas dépasser celles obtenues après $Z_{N_{\text{NTP}}}$ de plus de 10 % relatif (illustratif) ; une portée qui viole ce contrôle est non admissible pour la nécessité. **H_A de nécessité** porte sur $Z_N^{(\text{tout})}$ ; $Z_N^{(t)}$ et $Z_N^{(\text{clause})}$ servent à localiser (§c, dissensus 2).

### b.6 Pince : L2′ et calibration (remplace L2, A3 et le dénominateur de P-II.4)

**A3′.** Remplacer la corrélation intra-classe par une mesure de dépendance de queue sur le dénominateur honnête : $\chi_{0{,}95} = \Pr[m_{\text{int}} > q_{0{,}95}(m_{\text{int}}) \mid m_{\text{ext}} > q_{0{,}95}(m_{\text{ext}}), \text{honnête}]$ comparé à $0{,}05$ ; rapporté, non seuillé. Il ne conditionne pas l'admissibilité de la pince, seulement le choix du combinateur.

**L2′ (combinateur monotone quelconque).** Soit $g(m_{\text{ext}}, m_{\text{int}})$ non décroissant en chaque argument (produit de LR, régression logistique à coefficients positifs, ou maximum), et $\eta = q_{1-\varepsilon}$ de $g$ sur le dénominateur honnête durci. Si l'attaquant contrôle $m_{\text{ext}}$ à coût nul, il choisit $m^\star = \inf$ du support honnête de $m_{\text{ext}}$ ; la règle devient $m_{\text{int}} \ge g^{-1}(\eta;\, m^\star)$. Donc $\text{TPR}_{\text{att}}(g) \le \text{TPR}(m_{\text{int}} \text{ seul au seuil déplacé})$. *Preuve* : monotonie de $g$ en $m_{\text{int}}$ à $m_{\text{ext}}$ fixé. La conclusion ne dépend pas de A3 ; A3′ ne touche que la puissance en régime durci.

**Calibration.** Dénominateur honnête de P-II.4 : toutes les trajectoires γ ∪ ε de P-II.1 et P-II.2, groupées par préfixe (une grappe = un préfixe). Préenregistré : $n_{\text{grappes}} \ge 600$ (illustratif) ; borne supérieure exacte de Clopper-Pearson sur le FPR au seuil retenu, calculée au niveau des grappes ; si la borne dépasse $2\varepsilon$, P-II.4 publie l'intervalle et aucune décision d'adoption. L'effet $E_1$ n'est déclaré qu'avec son intervalle bootstrap par grappes.

### b.7 Ordre d'exécution corrigé

(0) `P4` rétabli et validé. (0′) **Φ0** sur le pilote de P-II.1. (1) P-II.1 avec I2′ sur les sous-plans de position, I2 sur $k$ ; bras $k = 0$ (R7) inchangé. (2) P-II.2. (3) Contrôle positif TD sur Qwen (inchangé) → P-II.3 avec étiquettes $r_{\text{ter}}'$, strates α/β/γ/ε, deux lectures, critère relatif et trois portées. (4) P-II.4 avec L2′ et calibration par grappes. Coût supplémentaire de Φ0 : ≈ 2 h A100 (illustratif) ; le reste est à coût constant ou inférieur, car la Phase 1 ne peut plus produire d'arrêt publié.

---

## (c) Dissensus irréductibles, chacun transformé en expérience

### Dissensus 1 — La porte $\Delta_K$ est-elle utilisable, ou l'inénumérabilité de $\mathcal{A}^+$ la condamne-t-elle en principe ?

C : la classe $\mathcal{A}^+$ est multimodale et un facteur peut déplacer la masse hors de toute banque finie ; aucun $K$ ne répare. Moi : une banque calibrée empiriquement suffit comme sélecteur, à condition de ne rien publier à partir d'elle.
**Expérience : Φ0 elle-même** (b.1). $H_A$ (A) : $\rho_s(\Delta_K, V) \ge 0{,}5$ et faux négatifs de porte $\le 10\,\%$. $H_B$ (C) : $\rho_s < 0{,}3$ ou faux négatifs $\ge 25\,\%$ (illustratifs). Entre les deux : zone grise, la Phase 1 est abandonnée par précaution. Issue $H_A$ : l'entonnoir tient, et C doit dire pourquoi une porte à 10 % de faux négatifs serait pire qu'une Phase 2 à budget contraint sur un plan tronqué. Issue $H_B$ : mon entonnoir disparaît et je perds l'argument de financement contre le factoriel de C — ce que je dis d'avance.

### Dissensus 2 — L'ablation sur préfixe figé est-elle structurellement nulle (cache KV), ou mesure-t-elle quelque chose ?

C : les couches hautes lisent le contexte directement ; $Z_N^{(t)}$ est nul par construction et $Z_N^{(\text{tout})}$ détruit la compréhension du prompt. Moi : la contribution des couches 2–5 au jeton $t$ n'est pas éliminable par raisonnement.
**Expérience : trois portées × quatre ensembles** (b.5), effet sur $\Delta_K$, contrôle de non-destruction. Lecture :
- $Z^{(\text{tout})}$ déplace $\Delta_K$ au-delà des témoins, $Z^{(t)}$ non → le mécanisme de C est soutenu (le signal passe par le cache), la nécessité tient au niveau séquence ;
- $Z^{(t)}$ seul déplace $\Delta_K$ → le mécanisme de C est réfuté ;
- aucune portée admissible ne déplace $\Delta_K$ → nécessité réfutée sur Llama-8B, cohérent avec l'absence d'effet d'ablation du Fait 5 (24/25 modèles) ; P-II.3 se replie sur le Niveau 1 (« lecture sans levier ») ;
- $Z^{(\text{tout})}$ viole la non-destruction → la question de la nécessité est **indécidable** par cette méthode sur ce modèle, et on le publie ainsi.

### Dissensus 3 — $m^{\text{act}}_{\text{int}}$ survit-il à « planifier tôt, remplir de syntaxe » ?

C : la décision est prise $k$ jetons avant la frontière d'outil et le dernier jeton ne porte que de la syntaxe ; la moyenne par paragraphe dilue le pic. Moi : la lecture par maximum sur le segment généré capte le pic où qu'il soit, et c'est K4 (non-inscriptibilité) qui est en jeu, pas la position.
**Expérience** (requiert `(ii)` ; reportée et dite telle quelle sinon). Sur `(i-a)` et `(ii)`, AUC intra-préfixe de trois lecteurs : dernier jeton, moyenne par paragraphe, maximum par jeton ; plus la distribution de $t_{\text{outil}} - t^\star$. $H_A$ (A) : le lecteur « maximum » garde une AUC à moins de $\delta$ de celle sur `(i-a)` quand il passe à `(ii)`, même si le dernier jeton s'effondre. $H_B$ (C) : les trois lecteurs tombent sous 0,6 sur `(ii)` (illustratif). Issue $H_A$ : l'évasion de C est réelle mais n'atteint que les lecteurs à position fixe ; sa « dilution $1/M$ » est une erreur de conception, pas une limite de la boîte blanche. Issue $H_B$ : le signal de Niveau 1 est un artefact d'instruction ; K4 n'a même plus d'objet sur cet organisme.

### Dissensus 4 — $D(\tau)$ est-il un détecteur de falsification seulement ?

C : en mode Sol, $D(\tau) \approx 0$ ; le détecteur ne voit que les cas où le banc ment. Moi : avec $r_{\text{ter}}'$, Sol est étiqueté positif ; que le modèle le *représente* est ouvert.
**Expérience** : AUC de $D(\tau)$ et de $V^{\text{ter}'}$ par strate, avec négatifs γ ∪ ε. $H_A$ (A) : AUC(β) ≥ AUC(α) − δ. $H_B$ (C) : AUC(α) ≥ 0,7 et AUC(β) ≤ 0,55 (illustratifs). Issue $H_B$ : C a raison ; $D(\tau)$ est renommé « détecteur de falsification » dans le manifeste, et la coupure silencieuse reste à couvrir par la mâchoire externe durcie sur $h(P)$ et le manifeste de $W$ — ce qui est exactement un durcissement par déplacement d'état hors de $W$ (L2′), pas une lecture interne. Issue $H_A$ : le modèle code une dissociation « banc/état réel » qui ne se réduit pas au résultat de la tâche. L'écart entre AUC(γ) et AUC(α) tranche le contrôle c4 de C dans les deux cas.

---

## Ce que cette riposte ne change pas

Aucun statut de fait. Aucune « tête de sabotage », aucune lecture en temps réel, aucune donnée sur l'axe de douleur. Le verdict R13 reste « aucune sonde générique au-dessus du plancher apparié ». Le Fait 1 reste un rapport sur des modèles fermés dont P-II.1 et P-II.2 reconstruisent la configuration, non l'incident. Tout chiffre de seuil, de taille et de durée est illustratif et sera fixé avant la première empreinte.

FIN-DE-CELLULE