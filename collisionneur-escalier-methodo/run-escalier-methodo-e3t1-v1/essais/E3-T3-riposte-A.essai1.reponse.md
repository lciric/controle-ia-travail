# Proposition A — Tour III.3 : riposte

**État des pièces.** FAITS vide par décision de l'arbitre (message n° 28 § 1) : aucun fait inventé. Ma pièce III.1 et les deux pièces rouges (B, C) sont présentes, se terminent par leur marqueur et ne paraissent pas coupées. Je ne peux pas vérifier les empreintes sha256. Je ne réponds qu'aux sections visant A. Tout chiffre ci-dessous qui ne vient pas de la question est « illustratif ».

**Une erreur que personne n'a relevée et que je corrige d'abord.** En §1 de ma conception, j'écrivais qu'un nombre d'items discordants $D$ plus élevé *augmente* la puissance. C'est faux à δ fixé : le gain net d'items étant fixé par δ, chaque discordant supplémentaire ajoute du bruit sans ajouter de signal (variance de $\sum d_i$ = $D - (\text{net})^2/D$, croissante en $D$). Vérification exacte, famille 2, δ = 0,10 (2,4 items nets, arrondi 3) : $D = 6$ → puissance ≈ 0,12 ; $D = 12$ → ≈ 0,08 (illustratif, McNemar exact unilatéral, α = 0,05). La conclusion de ma pièce est donc *renforcée*, mais une de ses issues de secours (« des bras très différents ») disparaît. Je corrige le Duel 1 en conséquence.

---

## (a) Triage des attaques

### Attaques de B

| # | Verdict | Raison / transformation |
|---|---|---|
| **A-1** (duels non falsifiants, IC plus larges que δ) | **Acceptée.** | Le calcul de B (écart-type ≈ 0,10 en famille 2, demi-largeur ≈ 0,16) est juste. Un duel B4 à 60 items ne peut pas reposer sur deux IC ; il doit reposer sur un **seuil unique scellé $c$** entre 0 et δ et sur **deux taux d'erreur déclarés** : P(monter \| Δ = 0) et P(rester \| Δ = δ). Chaque issue falsifie alors une hypothèse, à un taux d'erreur connu et élevé. Tous les duels sont réécrits ainsi en (b). |
| **A-2** (pas de contraste libre dans le $2^{4-1}$) | **Acceptée.** | Mon « contraste alias d'ordre 3 » était un effet principal. Correction : factoriel complet $2^4$ (16 essais, équivalent au $2^{4-1}$ + repli), les 4 interactions d'ordre 3 et l'interaction d'ordre 4 (5 ddl) servent d'erreur, **plus** le réplicat d'erreur pure demandé par B (2 coins × 1 graine supplémentaire). Aucun générateur à choisir : l'évasion « choisir l'alias » disparaît. |
| **A-3** (détecteur de plateau aveugle) | **Acceptée.** | Le calcul (≈ 0,07 de déclarer un vrai plateau sur deux crans) est juste. Le plateau devient : « rester si $\hat\Delta < c$ », avec $c = \delta/2$ scellé, et deux taux d'erreur déclarés (voir (b)). |
| **A-4** (λ indéfini si borne négative ; arrêt un cran trop tard) | **Acceptée en partie.** | Le ratio avec borne négative n'était pas « indéfini » mais mal ordonné : λ n'est qu'une seconde porte, après la porte statistique. Reformulé en (b) avec $\hat\Delta$ et non la borne. Le cran payé pour savoir qu'il ne vaut rien est **inhérent** à tout plan à un pas d'avance ; je l'inscris au budget plutôt que de prétendre l'éviter. |
| **A-5** (fuite calibration/contrôle ; réserve consommée) | **Acceptée.** | (i) Un test de permutation est exact sous échangeabilité : l'A/A ne teste rien pour *lui* ; il reste informatif pour le bootstrap, le bayésien et le détecteur de plateau, qui ne sont pas exacts, à condition d'une **troisième réplique de la base jamais utilisée pour calibrer** (contrôle de B, adopté). (ii) La zone grise ne pioche plus dans la réserve : **zone grise = rester** (généralisation de « à égalité, le moins cher »). La réserve est touchée une seule fois, à la confirmation. |
| **A-6** (injection d'effet échangeable) | **Rejetée pour le test de permutation, acceptée pour le reste.** | La statistique $\sum w_i d_i$ ne dépend de l'identité des items qu'à travers leur classe : une injection concentrée ou dispersée donne la même loi sous permutation. Elle change en revanche la couverture du bootstrap stratifié et la lecture de l'escalier. **Transformée en test** : banc à deux scénarios (flips aléatoires ; flips concentrés sur les items où le classifieur trivial échoue) ; un écart de détection > 0,05 (illustratif) entre scénarios disqualifie l'instrument comme sensible à l'identité des items. |
| **A-7** (tableau de puissance incohérent) | **Acceptée.** | $\delta'_i$ et $u_i$ ne sont pas identifiables : modèle réécrit $d_{ki} = \delta + u_i + e_{ki}$ (plus effets d'exécution par bras, non appariés, voir C-5). Les puissances du tableau étaient à $K = 1$ : étiquetées ainsi. « Irréductible » n'était pas une contradiction mais une ambiguïté de régime : je **scelle le régime super-population** (inférence vers de nouveaux textes, ce que « jeu tenu à l'écart » impose) ; le terme item n'y diminue pas avec $K$. $K$ de saturation dérivé en (b). |
| **A-8** (confusion temporelle ; rien n'est randomisé) | **Acceptée.** | Ordre des bras tiré au sort et journalisé, base rejouée en entrelacé (début/milieu/fin, contrôle de B adopté), chaîne de version du fournisseur consignée à chaque appel. Le mot « randomisé » pour $b$ devient un acte : affectation tirée au sort avant exécution. |
| **A-9** (Duel 3 conditionne sur $s$, post-traitement) | **Acceptée.** | Même faille que C-1. Duel 3 remplacé par un $2 \times 2$ *budget annoncé × budget imposé*, analysé en intention de traiter, sans aucun conditionnement sur $s$ (voir (b)). Le canal « $b$ lu via la configuration » est couvert : « imposé » est précisément ce canal. |
| **A-10** (statuts) | **Acceptée.** | A7 → HYPOTHÈSE. A10 → RAPPORTÉ (la question le donne), avec la mention que la question elle-même le qualifie d'illustratif. L'identité de la configuration des répliques gratuites → HYPOTHÈSE ; je demande à l'arbitre laquelle. |
| **Scénario « graines cachées »** | **Acceptée.** | Parade hors statistique : journal scellé, chaque essai engagé par son empreinte *avant* exécution ; exécutant distinct de l'analyste. Sans cela, aucune règle de ce tour ne tient, la mienne comme les autres. |
| **Scénario « dégrader la famille 2 de 2 items »** | **Acceptée.** | Nouvelle contrainte scellée : rester si une famille a $\hat\Delta < -\delta/2$ (en famille 2, deux items = −0,083 déclenche). Coût : un recul fortuit d'un item ne bloque pas, deux oui ; P(blocage \| Δ = 0 en famille 2) ≈ 0,15 (illustratif, $D$ = 6). Assumé. |
| **Contrôles (c) de B** : base entrelacée, provenance des rondes, A/A hors échantillon, placebo de format, réplicat d'erreur pure | **Acceptés tous les cinq**, intégrés en (b). | Je m'en sers en le disant (B1). Le placebo de format remplace mon Duel 4, que C démonte par ailleurs. |

### Attaques de C

| # | Verdict | Raison / transformation |
|---|---|---|
| **1** (Duel 3, biais de collision) | **Acceptée.** | Identique à A-9. Remplacé. |
| **2** (Duel 4, exclusion des invalides = collision) | **Acceptée.** | Exclure les invalides des deux bras purge les items durs. Analyse primaire : intention de traiter, invalide = erreur (c'est le cadre). Diagnostic du canal format : placebo de B — réanalyser *les mêmes sorties* du bras long tronquées à la longueur du bras court, sans nouvel appel. Deux issues falsifiantes, coût nul. |
| **3** (factoriel à une graine, variance de graine absorbée) | **Acceptée.** | Même objet que A-2. Erreur pure par réplicats. |
| **4** (zone grise sans dépense d'α, réserve détruite) | **Acceptée.** | Zone grise = rester. Plus de second regard. |
| **5** (appariement par graine fictif) | **Acceptée, avec une réserve transformée en test.** | La $k$-ième graine de A n'a aucun lien avec la $k$-ième de B : $v_k$ partagé était fictif. Modèle corrigé : effets d'exécution *par bras*, indépendants. Réserve : si deux bras partagent la même ronde de mise au point (axe non varié), il existe bien une composante commune ; c'est le contrôle (c)1 de C, que j'adopte comme **Duel 6**. |
| **6** (empirical Bayes évalué in-sample) | **Acceptée.** | Même remède que A-5 : troisième réplique de la base tenue hors calibration. |
| **Scénario 1** (gain concentré sur 3 items ; bootstrap anticonservatif) | **Acceptée.** | Vérification : avec 3 items porteurs sur 12 positifs, P(aucun dans un rééchantillon) = $(9/12)^{12} \approx 0{,}03$ ; le 5ᵉ percentile est à la frontière de 0 — le bootstrap percentile est bien instable ici. Le **test de permutation exact devient la seule porte**, le bootstrap est rétrogradé en descriptif. Ajout d'un **audit d'identité des sorties** : taux de sorties byte-identiques entre bras ≤ taux observé sur l'A/A + tolérance ; sinon audit (réutilisation de cache). |
| **Scénario 2** (manipuler $\Delta\bar s$ pour faire exploser Wald) | **Acceptée.** | L'IV était déjà secondaire. Ajout : valeur marginale non calculée si $\Delta\bar s < s_{\min}$ scellé (20 % de $\bar s_k$, illustratif) → rester. Le $2 \times 2$ annoncé × imposé rend l'évasion « même classe à $s$ égal » inopérante puisqu'on ne conditionne plus sur $s$. |
| **Scénario 3** (bruit injecté pour élargir l'IC) | **Rejetée pour la règle corrigée.** | La nouvelle règle de plateau porte sur $\hat\Delta$, pas sur une borne : du bruit symétrique ne la déplace pas. De plus, un cran bruyant a un taux de bascule entre graines $\hat f$ très supérieur à l'A/A : audit. |
| **Scénario 4** (évasion totale : calcul lourd sur 4 items repérés par la longueur, $D = 8$) | **Acceptée comme limite.** | Un système qui gagne réellement 8 items sur ces 60 et n'en perd aucun *améliore* ces 60 items ; aucune analyse sur les 60 ne distingue cela d'un gain généralisable. Seules tiennent : la réserve scellée (items jamais vus, contrôle de provenance par empreintes) et l'audit d'identité des sorties (53 sorties identiques au bras de base sont détectables). Je l'écris tel quel dans la réponse à l'arbitre. |
| **Contrôle (c)1** (même ronde de mise au point vs rondes différentes) | **Accepté → Duel 6.** | |
| **Contrôle (c)2** (simulation de collision) | **Sans objet pour le nouveau Duel 3** ; conservé comme vérification du $2 \times 2$ sur données simulées sans effet direct (doit donner Δ ≈ 0). | |
| **Contrôle (c)3** (couverture du bootstrap sur effets asymétriques) | **Accepté.** | Ajouté au banc ; conséquence déjà tirée : bootstrap descriptif seulement. |

**Ce que je garde de B sans le lisser (B1).** B tranche le désaccord A/C sur la puissance par un calcul exact à 0,39 ($D = 12$, δ = 0,10, poids égaux). Mon recalcul ci-dessous est compatible et plus sévère à poids de BA. Je rejette en revanche l'idée que le régime conditionnel soit une option de décision : il définit le sur-apprentissage du jeu de test comme un succès (C le dit aussi contre B). Je le scelle hors jeu.

---

## (b) Expériences corrigées

### Cadre scellé (avant tout essai)

1. **Régime** : super-population. On conclut sur de futurs textes, pas sur ces 60.
2. **Test primaire** : permutation exacte des signes par item sur $T = \sum_i w_i \bar d_i$, où $\bar d_i$ est la moyenne sur les $K$ graines de $d_{ki}$ (l'item est l'unité ; les graines sont nichées, ce qui règle le piège du pooling de McNemar). Unilatéral, direction = bras le plus cher, α = 0,05. Familles agrégées par poids de BA ; chaque famille aussi rapportée.
3. **Modèle de variance corrigé** : $d_{ki} = \delta + u_i + r^{(A)}_{k} - r^{(B)}_{k'} + e_{ki}$ ; $\mathrm{Var}(\hat\Delta) = \sigma_I^2/n + (\sigma_{R,A}^2+\sigma_{R,B}^2)/K + \sigma_e^2/(nK)$. Les effets d'exécution $r$ ne sont pas appariés entre bras.
4. **Règle de décision à chaque cran $k \to k{+}1$** :
   - **Monter** si : $p_{\text{perm}} \le 0{,}05$ **et** $\hat\Delta \ge c = \delta/2$ **et** aucune famille avec $\hat\Delta_{\text{fam}} < -\delta/2$ **et** $\Delta \bar s \ge s_{\min}$ **et** $C_{k+1} / (100\,\hat\Delta) \le \lambda$ (λ en USD par point, scellé).
   - **Rester** sinon. Pas de zone grise. Pas de ponction sur la réserve.
   - Taux d'erreur déclarés (illustratif, 60 items, poids ≈ égaux, $D$ = 12) : P(monter \| Δ = 0) ≤ 0,05 par la porte $p$ ; P(monter \| Δ = 0,10) ≈ 0,35–0,40 ; P(monter \| Δ = 0,15) ≈ 0,8 (voir table).
5. **Multiplicité** : l'escalier est une exploration ; une seule décision confirmatoire, base vs configuration retenue, sur la **réserve intouchée**, à α = 0,05, pré-enregistrée. Si la réserve n'existe pas, le rapport porte l'étiquette « jeu de validation réutilisé, BA finale biaisée vers le haut d'un montant inconnu ».
6. **Journal scellé** : empreinte de chaque essai (configuration, graine, ordre tiré au sort, version du fournisseur) consignée avant exécution ; exécutant ≠ analyste.

### Puissance recalculée (McNemar/permutation exact, unilatéral, α = 0,05, $K = 1$, 60 items poolés à poids égaux ; illustratif)

Pour δ fixé, net = $\lceil 60\delta \rceil$ items ; $D$ discordants ; $p = (D + \text{net})/(2D)$.

| δ | net | $D$ (part) | valeur critique | puissance |
|---|---|---|---|---|
| 0,10 | 6 | 7 (12 %) | 7/7 | 0,60 |
| 0,10 | 6 | 9 (15 %) | 8/9 | 0,54 |
| 0,10 | 6 | 12 (20 %) | 10/12 | 0,39 (= B) |
| 0,10 | 6 | 20 (33 %) | 15/20 | ≈ 0,24 |
| 0,15 | 9 | 12 (20 %) | 10/12 | 0,82 |
| 0,15 | 9 | 15 (25 %) | 12/15 | 0,65 |
| 0,20 | 12 | 20 (33 %) | 15/20 | 0,80 |

Lecture : à δ = 0,10, la puissance 0,8 n'est atteinte que si $D \le 6$, c'est-à-dire quand *tous* les discordants vont dans le même sens — précisément le cas que le cadre déclare « trop propre » et audite. Les poids de BA (1/48 et 1/72 selon la famille) abaissent encore ces valeurs de quelques points. **δ = 0,10 n'est pas résoluble à puissance 0,8 sur 60 items en régime super-population ; δ = 0,15 l'est si $D \le 12$ ; δ = 0,20 l'est jusqu'à $D \approx 20$.**

**Graines de saturation.** Soit $\hat f$ le taux de bascule entre graines (A/A) et $p_d$ la part de discordants entre bras ; la part de variance réductible par $K$ est ≈ $\hat f$, l'irréductible ≈ $p_d - \hat f$. $K^* = \lceil \hat f / (0{,}2\,(p_d - \hat f)) \rceil$ (critère : terme graine ≤ 20 % du terme item). Avec $\hat f = 0{,}10$, $p_d = 0{,}25$ : $K^* = 4$ (illustratif). Avec $\hat f = 0{,}03$ : $K^* = 1$. C'est la seule chose que les répliques gratuites décident.

### Duel 0 (nouveau, à faire en premier) — Encadrement de l'escalier

- Plan : base vs configuration la plus chère que le budget permet (tous axes au maximum), 2 graines chacune, ordre tiré au sort, entrelacé.
- H_A : $\hat\Delta_{\text{extrêmes}} \ge 0{,}15$ avec $p \le 0{,}05$ → l'escalier a quelque chose à répartir ; on le lance.
- H_B : $\hat\Delta_{\text{extrêmes}} < 0{,}15$ ou $p > 0{,}05$ → aucun cran intermédiaire ne peut atteindre le seuil ; décision immédiate : **rester base** (le moins cher l'emporte), escalier annulé.
- Taux d'erreur : P(lancer \| Δ = 0) ≤ 0,05 ; P(annuler \| Δ = 0,15, $D$ = 12, $K$ = 2) ≈ 0,15–0,2 (illustratif).
- Coût : 4 exécutions ≈ 64–88 USD (illustratif). Il mesure aussi $D$ réel, nécessaire au Duel 1.

### Duel 1 — Résolution (calcul fermé, alimenté par le Duel 0)

- H_A : $D_{\text{obs}}$ (Duel 0) ≤ 12 → δ = 0,15 est résoluble à ≥ 0,8 ; δ scellé à 0,15.
- H_B : $D_{\text{obs}}$ > 12 → δ scellé à 0,20 (ou réserve d'items exigée avant tout escalier).
- Les deux issues fixent δ ; aucune zone intermédiaire.

### Duel 2 — Séparabilité des axes

- Plan : $2^4$ complet (16 essais, 1 graine) + 2 coins rejoués (1 graine de plus chacun) pour l'erreur pure ; ordre tiré au sort ; erreur = interactions d'ordre ≥ 3 (5 ddl) poolées avec l'erreur pure (2 ddl).
- H_A : $\max_{j<l} |\widehat{\text{int}}_{jl}| < c_{\text{int}} = \delta/2$ → OFAT valide.
- H_B : $\max |\widehat{\text{int}}_{jl}| \ge \delta/2$ → OFAT invalide ; escalier sur la paire d'axes en interaction, traitée comme un seul axe à 4 niveaux.
- Taux d'erreur : avec 16 essais, l'écart-type d'une interaction ≈ $\sigma_{\text{run}}/2$ ; si $\sigma_{\text{run}} \approx 0{,}06$, SE ≈ 0,03 et chaque erreur ≈ 0,05 à $c = 0{,}075$ (illustratif).
- Coût ≈ 18 × 16 ≈ 290 USD (illustratif). Voie O (OFAT sans Duel 2) reste offerte à l'arbitre : moins chère, aveugle aux interactions.

### Duel 3 — Exclusion de $b$

- Plan $2 \times 2$ : budget **annoncé** dans l'invite {bas, haut} × budget **imposé** par plafond de dépense {bas, haut} ; 2 graines par cellule, affectation tirée au sort ; analyse en intention de traiter, **sans conditionnement sur $s$**.
- Première étape : le plafond imposé déplace $\bar s$ (sinon l'axe « budget » est inerte, Duel clos).
- H_A : effet principal de l'annonce $< \delta/2$ → exclusion tenable, IV utilisable.
- H_B : $\ge \delta/2$ → exclusion violée ; seul l'ITT décide.
- Interaction annonce × imposition rapportée (le système peut lire son budget *et* y réagir différemment selon le plafond).
- Vérification sur simulation : difficulté → ($s$, $Y$) sans effet direct de $b$ ; le plan doit donner Δ ≈ 0 (contrôle (c)2 de C).
- Coût ≈ 8 × 16 ≈ 128 USD (illustratif).

### Duel 4 — Canal format (placebo, coût nul)

- Mêmes sorties du bras long, tronquées à $L_{\text{court}}$ puis reparsées.
- H_A : $|\Delta_{\text{tronqué}} - \Delta_{\text{original}}| \le 1$ item net → Δ ne vient pas du parsing.
- H_B : ≥ 2 items nets → Δ est un artefact de format ; l'axe « longueur » est retiré de l'escalier et la règle « invalide = erreur » est signalée à l'arbitre comme non neutre.

### Duel 5 — Transposabilité

- Sur $v{+}1$ : ancre (base) et gagnant rejoués, mêmes graines, entrelacés.
- H_A : $\hat\Delta_{v+1} \ge \delta/2$ et $p \le 0{,}05$ → transportable.
- H_B : sinon → non transportable ; retour au Duel 0 sur $v{+}1$.
- Contrôle de dérive : ancre$_v$ vs ancre$_{v+1}$ ; si ≥ 2 items nets, rien n'est comparable entre versions.

### Duel 6 (de C) — Composante d'exécution partagée

- Deux paires : (même ronde de mise au point, graines d'inférence différentes) vs (rondes de mise au point différentes).
- H_A : taux de bascule égal à ±2 items → la ronde n'induit pas d'effet d'exécution ; $K$ graines d'inférence suffisent.
- H_B : écart ≥ 3 items → la ronde est un bloc ; chaque bras doit rejouer sa ronde à chaque graine (coût +10 USD par graine, RAPPORTÉ illustratif).

### Contrôles scellés (adoptés de B et C, plus un)

| Contrôle | Seuils (illustratifs, à sceller) |
|---|---|
| Base rejouée entrelacée (début/milieu/fin) | ≥ 2 items nets d'écart → escalier invalide |
| Provenance des rondes : empreintes des données de mise au point ∩ empreintes des 60 + réserve = ∅ | non vide → axe « rondes » ininterprétable |
| A/A hors échantillon (3ᵉ réplique de la base) | fausse alerte du bootstrap/bayésien/plateau ≤ nominal |
| Réplicat d'erreur pure dans le factoriel | obligatoire, sinon Duel 2 sans dénominateur |
| Placebo de format | Duel 4 |
| **Audit d'identité des sorties** (nouveau) | taux de sorties byte-identiques entre bras ≤ taux A/A + 0,05 → sinon audit cache/réutilisation |
| Banc d'injection à deux scénarios (aléatoire / concentré) | écart de détection ≤ 0,05 |
| Couverture du bootstrap sur $d_i \in \{0, +1\}$ épars | rapportée ; bootstrap descriptif seulement |

### Budget révisé (illustratif, 16 USD par exécution)

Duel 0 ≈ 80 ; Duel 2 ≈ 290 (optionnel) ; Duel 3 ≈ 130 ; Duel 6 ≈ 70 ; escalier 2 axes × 3 crans × $K^*$ = 2 graines ≈ 190 ; base entrelacée ≈ 50 ; 3ᵉ réplique ≈ 16 ; confirmation sur réserve ≈ 65. Total ≈ 600 USD avec Duel 2, ≈ 310 sans. Non budgété : la réserve d'items (coût humain).

---

## (c) Réponse à l'arbitre

**Ce qui est établi (par calcul, réfutable par les chiffres de la question seulement).**

1. Sur 60 items et en régime super-population — le seul compatible avec « jeu de test tenu à l'écart » — un écart δ = 0,10 de BA ne se détecte pas à puissance 0,8 : avec le test exact, la puissance vaut ≈ 0,6 si 7 items sont discordants, ≈ 0,4 à 12, ≈ 0,25 à 20 (illustratif, poids égaux ; les poids de BA abaissent encore). La puissance 0,8 n'apparaît que lorsque tous les discordants vont dans le même sens, ce que le cadre audite comme « trop propre ». Le seuil Δ ≥ +0,10 déjà exigé ailleurs est au-dessous de la résolution de l'instrument ; δ = 0,15 est résoluble si ≤ 20 % des items sont discordants, δ = 0,20 jusqu'à ≈ 33 %.
2. Multiplier les graines ne change pas cela : la variance item-à-item ne diminue pas avec $K$ ; les graines ne servent qu'à éteindre le bruit d'exécution, et deux à quatre suffisent (formule en (b)).
3. Une règle de décision honnête à cette taille n'est pas un intervalle de confiance mais un seuil scellé avec deux taux d'erreur déclarés, tous deux élevés ; la zone grise se résout par « rester », conformément à « à égalité, le moins cher l'emporte ».
4. Trois constructions de ma conception III.1 étaient fausses et sont retirées : le contrôle négatif du factoriel fractionnaire, l'appariement sur la dépense réalisée $s$ (collision), l'appariement fictif par indice de graine. Les corrections viennent de B et C ; je les attribue.

**Ce qui n'est pas établi.**

- La part réelle d'items discordants entre deux configurations ($p_d$) et le taux de bascule entre graines ($\hat f$) : HYPOTHÈSES tant que les répliques gratuites n'ont pas été lues, et je ne sais pas de quelle configuration elles proviennent.
- La séparabilité des axes, l'exclusion du budget annoncé, la neutralité du canal « réponse invalide », la stabilité entre versions : chacune est HYPOTHÈSE, avec un duel attaché.
- L'existence d'une réserve d'items. Sans elle, toute décision prise sur les 60 items est une décision de développement, et aucune analyse sur ces 60 — j'inclus la mienne — ne distingue un gain généralisable d'un gain ciblé sur eux (scénario 4 de C). La seule parade est hors statistique : réserve scellée, contrôle de provenance par empreintes, journal engagé avant exécution, exécutant distinct de l'analyste.

**L'expérience à faire en premier.**

À coût nul : lire les deux répliques gratuites pour $\hat f$ et le taux de sorties identiques, qui calibrent le bruit de graine et l'audit d'identité. Puis, pour ≈ 80 USD (illustratif), le **Duel 0 — encadrement** : base contre configuration la plus chère, deux graines chacune, entrelacées, ordre tiré au sort. Si les deux extrêmes ne diffèrent pas d'au moins 0,15 au test exact, aucun cran intermédiaire ne peut franchir le seuil et la décision est prise : rester sur la base, l'escalier n'est pas lancé. S'ils diffèrent, le même essai donne $D$, qui scelle δ (0,15 ou 0,20) et le nombre de graines, et l'escalier commence. Les deux issues décident quelque chose ; c'est la seule expérience de ce tour dont le résultat ne peut pas être « on ne sait pas ».

**Références** (inchangées depuis III.1, toutes « à vérifier », aucun identifiant de mémoire) : McNemar 1947 ; Dietterich 1998 ; Nadeau & Bengio 2003 ; Demšar 2006 ; Benavoli et al. 2017 ; Brodersen et al. 2010 ; Dror et al. 2018 ; Card et al. 2020 ; Bouthillier et al. 2021 ; Jamieson & Talwalkar 2016 ; Li et al. 2018 ; Falkner, Klein & Hutter 2018 ; Lan & DeMets 1983 ; Box, Hunter & Hunter (édition à vérifier). Pour le biais de collision : référence à vérifier (je ne cite pas de mémoire).

**Ce que cette riposte peut perdre.** Si $\hat f$ est proche de zéro et que le Duel 0 montre $D \le 7$ avec un signe constant, le système est quasi déterministe et très sensible à la configuration ; alors δ = 0,10 redevient résoluble sur 60 items, et c'est C qui avait raison sur l'ordre de grandeur.

FIN-DE-CELLULE