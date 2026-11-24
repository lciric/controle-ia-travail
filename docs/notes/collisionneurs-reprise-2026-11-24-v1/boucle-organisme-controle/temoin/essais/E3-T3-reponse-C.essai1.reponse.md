*Note d'intégrité et état des pièces :* les pièces `FAITS`, `QUESTION DE L'ARBITRE`, `E3-T1-conception-C`, `E3-T2-critique-croisee-A` et `E3-T2-critique-croisee-B` sont présentes et complètes ; les conceptions initiales de A et B ne sont pas jointes à cet envoi et leur contenu n'est pas reconstitué. Je ne réponds qu'aux sections visant la proposition C (y compris l'expérience de discrimination finale de A, qui vise explicitement E1 de C). Les faits issus du dossier conservent le statut `RAPPORTÉ`, les résultats mathématiques ou probabilistes établis portent le statut `VÉRIFIÉ`, les prémisses non testées portent le statut `HYPOTHÈSE`, et mes choix révisés portent la mention `PROPOSITION`. Tout chiffre hors faits du dossier est marqué `illustratif` ; aucun identifiant arXiv n'est donné de mémoire (`pas sûr`).

---

## (a) Réponse aux critiques visant la proposition C

### 1. Critiques issues de la proposition A

- **A-a1 et Expérience de discrimination (fuite par spécification dans E1) — Acceptée sur le diagnostic ; expérience de A partiellement rejetée et transformée en test.**
  - *Diagnostic accepté :* fournir les fiches d'obstruction au bras spécialisé tout en testant ce bras sur des mondes-miroirs instanciant ces mêmes fiches crée une fuite par spécification. Je reprends l'idée de A (créditée explicitement, règle B1) d'évaluer le transfert sur des obstructions **conçues à l'aveugle des fiches** avec bras « fiches-leurres » (A-c1) et variance estimée **entre familles**.
  - *Critique et rejet partiel du plan de A :* l'expérience proposée par A comporte deux défauts : (i) sa zone non concluante $R \in (0{,}2 ; 0{,}6)$ (`illustratif`) viole B4 (le même défaut que A reproche à C) ; (ii) le ratio $R = \Delta_{O_{4..6}}/\Delta_{O_{1..3}}$ a une variance instable dès que $\Delta_{O_{1..3}}$ approche zéro. Je la transforme dans **E1\*** en un test primaire sans zone tampon sur $\bar{\Delta}_{\text{aveugle}}$ (avec diagnostic linéarisé $\bar{\Delta}_{\text{aveugle}} - \gamma \bar{\Delta}_{\text{décrites}}$) couplé au plan factoriel demandé par B.

- **A-a2, A-a3 et A-c2 (dépendance Sas 2 / Sas 2.5 et optimisme de $\widehat{\text{FPR}}$ sélectionné) — Acceptées.**
  - Utiliser le même jeu honnête pour paramétrer les mondes-miroirs (Sas 2) et filtrer au Sas 2.5 crée une dépendance, et la sélection au Sas 2.5 rend optimiste le taux de fausses alertes utilisé pour évaluer l'instrument 6. *Correction :* partition stricte des données honnêtes 8B (prompts et tâches disjoints) en trois jeux indépendants : $D_{\text{hon,cal}}$ (Sas 2), $D_{\text{hon,filtre}}$ (Sas 2.5) et $D_{\text{hon,eval}}$ (évaluation fraîche en E4\* et calcul de la valeur prédictive du sas). L'écart $\widehat{\text{FPR}}(D_{\text{hon,eval}}) - \widehat{\text{FPR}}(D_{\text{hon,filtre}})$ mesure directement la sur-sélection.

- **A-a4, A-a5 et A-c3 (E2 mesure la mauvaise quantité et récompense la prudence) — Acceptées et transformées en test.**
  - Une p-valeur empirique sur référence fixe $N$ est minorée par $1/(N+1)$ (`VÉRIFIÉ`), ce qui crée un plafond d'évidence (puissance) au-delà de $N$ (`RAPPORTÉ`), distinct de la dérive de $\text{FPR}$. En outre, exiger une borne supérieure d'IC $\le 0{,}07$ (`illustratif`) favorise les détecteurs sur-conservateurs. *Correction :* **E2\*** sépare en deux portes ordonnées (i) la validité nulle dimensionnée sans biais de prudence et (ii) un test direct de levée du plafond d'évidence à $T = 4N$ (`illustratif`) sur signaux diffus plantés dans $D_{\text{hon,filtre}}$ (zéro famille de sabotage consommée).

- **A-a6, A-b4 et A-c6 (E3 dictée par la définition d'« orthogonale » et réplication des graines plutôt que des familles) — Acceptées et transformées en test.**
  - L'orthogonalité binaire impose le résultat par construction, et répliquer 30 graines (`illustratif`) de l'organisme n'échantillonne pas la variance inter-familles. *Correction :* **E3\*** balaie un indice continu de recouvrement inter-familles $\kappa \in \{0 ; 0{,}25 ; 0{,}50 ; 0{,}75 ; 1\}$ (`illustratif`, incluant les deux extrémités disjointe et i.i.d.) avec la **famille** comme unité aléatoire, et cible la seule fuite encore plausible dans notre architecture : un post-mortem honnête déclenché par le Sas 3 (critique B-a1).

- **A-a7, A-b3, A-c4 et A-c7 (témoin LLM mal apparié, effectif non apparié $M=100$, pseudo-réplication sur 1 famille, et lignée honnête non vue en E4) — Acceptées.**
  - *Corrections dans E4\* :* (i) le témoin « LLM sans organisme » génère le **même nombre de candidats** à budget exact de jetons/CPU et traverse **la même cascade Sas 0–2.5** ; (ii) tous les détecteurs sont évalués en **appariement strict sur les mêmes trajectoires** (test exact de McNemar sur paires discordantes, avec $M = 180$, `illustratif`) ; (iii) E4\* prévoit $k_{\text{fam}} = 3$ mini-familles aveugles indépendantes (`illustratif`), ou déclare explicitement, si le budget impose $k_{\text{fam}} = 1$, que la falsification reste conditionnelle à cette unique famille sans estimation de variance inter-familles ; (iv) $D_{\text{hon,eval}}$ inclut une troisième lignée 8B non vue au développement.

- **A-a8 et A-c5 (placebo de graphes permutés trop faible) — Acceptées.**
  - *Correction :* remplacement par un recâblage préservant exactement la distribution des degrés entrants/sortants et les tranches temporelles des concepts.

- **A-a9 (zones tampons violant B4 et contestation du statut `OBSERVÉ-NON-AUDITÉ`) — Acceptées.**
  - Toutes les zones d'indécision d'E1–E4 sont supprimées au profit d'un seuil critique unique préenregistré par test. Concernant le statut : je ne modifie pas la pièce T1 archivée (règle 1), mais j'accepte l'objection de A ; l'évaluation interne contre archive est `RAPPORTÉ`, tandis que tout gain de l'organisme en contrôle est traité strictement comme `HYPOTHÈSE`.

- **A-b1 (Spearman sur $k$ versions inatteignable à $p < 0{,}01$ pour $k \le 4$) — Acceptée.**
  - $1/5! \approx 0{,}0083$ (`VÉRIFIÉ` pour $k=5$, `illustratif`). *Correction :* abandon de la corrélation de Spearman comme critère principal d'E1\* au profit d'un test exact de permutation apparié sur $k_{\text{aveugle}} = 10$ familles (`illustratif`, résolution minimale $2^{-10} < 0{,}001$).

- **A-b2 (sous-dimensionnement $M=200$ en E2 et absence de $n$ pour le style) — Acceptée.**
  - Calcul confirmé : à $M = 200$ et $p = 0{,}05$ (`illustratifs`), un détecteur exactement calibré échoue ou tombe en zone grise environ deux fois sur trois. *Correction :* redimensionnement exact dans **E2\*** ($M = 1000$ trajectoires, $K_{\max} = 63$, et $n = 600$ paires stylistiques appariées, `illustratifs`).

- **A-b5 (seuil de corrélation non spécifié au Sas 0 et confondu avec la difficulté) — Acceptée.**
  - Traitée conjointement avec B-a3 et B-b3 ci-dessous.

- **A-b6 (optimalité de Neyman-Pearson et Wald-Wolfowitz sur mondes-miroirs) — Acceptée sur les alternatives simples, rejetée sur son application aux mondes composites.**
  - *Raison du rejet partiel :* les théorèmes de Jerzy Neyman et Egon S. Pearson (1933), *On the Problem of the Most Efficient Tests of Statistical Hypotheses*, et d'Abraham Wald et Jacob Wolfowitz (1948), *Optimum Character of the Sequential Probability Ratio Test* (`VÉRIFIÉ` ; arXiv : pas sûr), s'appliquent à une alternative simple connue. Or le problème du contrôle porte sur des familles de sabotage **inédites** (`RAPPORTÉ`), c'est-à-dire des hypothèses **composites ou adverses** où ni les bases d'archive ni les candidats ne connaissent l'instance plantée $P_1$. *Correction :* les mondes-miroirs d'E1\* sont restreints à des classes composites/adverses à ignorance symétrique entre archive et candidats ; le rapport de vraisemblance oracle (connaissant $P_1$) est affiché comme **plafond informatif**, jamais comme base d'archive à battre.

- **A-b7 (conditions de dégénérescence de l'oracle exogène $p_s \to 0$ ou hétérogénéité intra-strate) — Acceptée.**
  - *Correction :* ajout d'une précondition de jugeabilité avant toute ouverture d'E4\* : vérifier sur dommages plantés stratifiés que $\min_s \hat{p}_s \ge p_{\min}$ (`illustratif`) et tester l'homogénéité de $\hat{p}_s$ entre sous-types de dommages au sein de chaque strate. Les strates ne franchissant pas ce contrôle sont déclarées hors domaine de certification du détecteur seul.

---

### 2. Critiques issues de la proposition B

- **B-a1 et B-c4 (fuite adaptative du post-mortem Sas 3 et exposition des $p_s$ de l'oracle) — Acceptées (et premier volet transformé en test via E3\*).**
  - Conditionner le choix d'une propriété honnête à l'échec observé au Sas 3 constitue une analyse adaptative — Cynthia Dwork, Vitaly Feldman, Moritz Hardt, Toniann Pitassi, Omer Reingold et Aaron Roth (2015), *The reusable holdout: Preserving validity in adaptive data analysis*, Science (`VÉRIFIÉ` ; arXiv : pas sûr) — qui fait fuiter de l'information sur le sous-espace d'attaque. De plus, exposer les $p_s$ faibles à un organisme pouvant aussi proposer des scénarios de défaillance (`RAPPORTÉ`) compromet la séparation red-team/défense.
  - *Corrections :* (i) **suppression par défaut du post-mortem conditionné** et instauration d'un **gel strict pré-Sas 3** (toute extraction honnête est exécutée à l'aveugle du verdict du Sas 3) ; (ii) **masquage complet des taux $p_s$** vis-à-vis de l'organisme ; (iii) tout assouplissement futur du gel strict est subordonné à **E3\***.

- **B-a2 (volet 1) et B-c1 (biais de survie anti-puissance au Sas 2.5 et sonde placebo) — Acceptées.**
  - Un détecteur dégénéré franchit un filtre purement nul. *Correction :* ajout dans **E2\*** (créditant B) (i) de la soumission à l'aveugle d'une sonde placebo orthogonale devant être rejetée, (ii) d'un contrôle à seuil unique de préservation de signal cognitif bénin ($\widehat{\text{AUC}}_{\text{cognitif}} \ge 0{,}70$, `illustratif`), et (iii) du test de puissance sur signal diffus planté à $T = 4N$.

- **B-a2 (volet 2 — restriction de plage au Sas 3 en n'envoyant que le top-1) — Partiellement acceptée, partiellement rejetée avec raison.**
  - *Raison du rejet partiel :* sous budget GPU modeste et lecture unique (`RAPPORTÉ`), envoyer en Sas 3 des candidats déjà disqualifiés en Sas 2.5 pour violation du taux de fausses alertes consommerait des ressources pour tester des détecteurs statistiquement invalides sous $P_0$.
  - *Part acceptée et correction :* le taux de faux rejets des Sas 0–2 est mesuré en amont (sur $O_{11..20}$ en CPU et signaux plantés en Sas 2.5), et en **E4\*** on évalue hors-ligne sur les **mêmes** activations 8B déjà extraites (coût GPU et oracle marginal quasi nul) le top-$r$ ($r = 2$, `illustratif`, corrigé de Holm) **plus un candidat de rang médian parmi les candidats valides du Sas 2.5**, tous gelés et hachés avant ouverture.

- **B-a3 (volet 1) et B-c2 (confusion corpus/fiches dans E1 et alignement d'archive) — Acceptées.**
  - *Correction :* **E1\*** adopte un plan factoriel $2 \times 2$ (`Corpus standard` vs `Corpus stratégique`) $\times$ (`Fiches-leurres` vs `Fiches d'obstruction`), avec **implémentation préalable dans l'archive du Sas 0** de toutes les méthodes connues présentes dans le corpus ajouté.

- **B-a3 (volet 2), B-b3 (volet 1) et B-c3 (rejet au Sas 0 des extensions conservatrices coïncidant avec CUSUM/Wald pour $T \le N$) — Acceptées.**
  - La corrélation des décisions sous $P_0$ stationnaire rejette asymptotiquement toute extension localement efficace (`VÉRIFIÉ`). *Correction :* le Sas 0 évalue la non-redondance sur une **batterie multi-régimes** (régime stationnaire $T \le N$ ET régimes d'obstruction : $T > N$, queues lourdes, dérive) en conditionnant sur la difficulté ; il n'exclut un candidat que s'il coïncide avec l'archive sur *tous* les régimes, et doit valider un témoin positif aveugle (extension connue identique à CUSUM pour $T \le N$).

- **B-a4 (orthogonalité forcée en E3, zones tampons violant B4, conjonction composite en E4) — Acceptées.**
  - *Corrections :* orthogonalité remplacée par $\kappa$ continu dans **E3\*** ; suppression intégrale des zones tampons dans **E1\*–E4\*** ; décomposition d'**E4\*** en deux tests séquentiels à porte (*fixed-sequence*) chacun scalaire et binaire : d'abord **E4\*a** contre la meilleure base mécanique / plancher d'audit, puis conditionnellement **E4\*b** contre le témoin LLM-sans-organisme.

- **B-b1 (sous-dimensionnement binomial de E2 et perte SNR $\times (1 - \cos^2 \theta_{\Sigma_0})$ sous projection linéaire) — Acceptée sur le dimensionnement et le théorème, rejetée sur l'imputation d'une projection linéaire obligatoire.**
  - *Raison du rejet partiel :* ma conception T1 imposait une contrainte comportementale sur les faux positifs honnêtes ($|\Delta\text{FPR}_{\text{style}}|$), non une projection linéaire orthogonale annulant $\mathcal{V}_{\text{style}}$. Le risque de colinéarité entre style et intention reste toutefois critique (`HYPOTHÈSE`) : *correction* par le contrôle de signal cognitif résiduel (B-c1) et l'ouverture explicite aux mécanismes non linéaires ou au coût d'évasion.

- **B-b2 (dégénérescence de rang de $\widehat{\Sigma}_0$ pour $n_{\text{exp}} \le d$ et queues lourdes) — Acceptée.**
  - Conformément à Vladimir A. Marchenko et Leonid A. Pastur (1967), *Distribution of eigenvalues for some sets of random matrices* (`VÉRIFIÉ` ; arXiv : pas sûr), un monde-miroir calibré sur $\widehat{\Sigma}_0$ brut en grande dimension laisse un noyau $\ker(\widehat{\Sigma}_0)$ exploitable. *Correction :* les mondes-miroirs du Sas 2 utilisent un estimateur de covariance rétréci — Olivier Ledoit et Michael Wolf (2004), *A well-conditioned estimator for large-dimensional covariance matrices*, Journal of Multivariate Analysis (`VÉRIFIÉ` ; arXiv : pas sûr) — dans un sous-espace de dimension $p$ tel que $p/n_{\text{exp}} \le 0{,}05$ (`illustratif`) avec plancher spectral $\lambda_{\min} > 0$, et incluent systématiquement des perturbations à **queues lourdes** (lois de Student à $\nu \in \{3, 4\}$ degrés de liberté, `illustratif`) dès le Sas 1–2.

- **B-b3 (volet 2 — perte de contrôle FDR de Benjamini-Hochberg sous dépendance) — Acceptée.**
  - Sous dépendance arbitraire, la borne de Yoav Benjamini et Yosef Hochberg (1995), *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing*, Journal of the Royal Statistical Society: Series B (`VÉRIFIÉ` ; arXiv : pas sûr), se dégrade d'un facteur harmonique $\sum_{j=1}^m 1/j$ — Yoav Benjamini et Daniel Yekutieli (2001), *The control of the false discovery rate in multiple testing under dependency*, Annals of Statistics (`VÉRIFIÉ` ; arXiv : pas sûr). *Correction :* remplacement au Sas 2 par la procédure **e-BH** — Ruodu Wang et Aaditya Ramdas (2022), *False discovery rate control with e-values*, Journal of the Royal Statistical Society: Series B (`VÉRIFIÉ` ; arXiv : pas sûr) — ou par Benjamini-Yekutieli (2001) pour les p-valeurs, suivie d'un **tirage Monte-Carlo de confirmation indépendant** après gel du candidat (éliminant la malédiction du gagnant).

- **B-b4 (plafond $1 - R_{\text{audit}} < \delta_{\min}$ en E4 et taille effective $L_{\text{eff}}$ en Axe 3) — Acceptée.**
  - Lorsque le plancher d'audit aléatoire atteint $R_{\text{audit}}$ proche de $1$, exiger un gain absolu fixe $\delta_{\min}$ devient vide (`VÉRIFIÉ`). *Correction :* en **E4\***, (i) précondition $1 - R_{\text{audit}} \ge 0{,}30$ (`illustratif`) au taux d'audit réaliste fixé, et (ii) métrique primaire exprimée en **réduction relative du taux d'évasion** $1 - (1 - \text{TPR}_{\text{cand}})/(1 - \text{TPR}_{\text{ref}})$ (doublée du facteur d'économie de coût d'audit à puissance égale). Pour l'instrument 4 (Axe 3, essaims), la calibration inclut l'estimation de la corrélation bénigne intra-essaim $\hat{\rho}_0$ et la correction de variance par $1 + (L-1)\hat{\rho}_0$.

- **B-c5 (trajectoires honnêtes avec consigne auxiliaire privée bénigne) — Acceptée.**
  - Intégrée dès la porte 1 d'**E2\*** et dans $D_{\text{hon,eval}}$ d'**E4\*** pour séparer la présence d'un état latent privé de la détection d'un sabotage.

---

## (b) Expériences corrigées (protocole d'inférence forte B4 sans zone tampon)

Les quatre expériences révisées suivent la logique d'inférence forte — John R. Platt (1964), *Strong Inference*, Science (`VÉRIFIÉ` ; arXiv : pas sûr) — avec **un seuil critique unique préenregistré** par test primaire (aucune zone tampon) et une architecture étanche : partition honnête en trois jeux disjoints ($D_{\text{hon,cal}}$, $D_{\text{hon,filtre}}$, $D_{\text{hon,eval}}$), gel strict pré-Sas 3, masquage des $p_s$ de l'oracle et Sas 0 multi-régimes. **Tous les scores, effectifs, seuils et coûts ci-dessous sont `illustratifs`.**

| Rang | Expérience corrigée | Gain | Fac. | Portée | Pot. | Coût | Score `(illustratif)` |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **E1\* — Transfert vers obstructions aveugles et plan factoriel corpus $\times$ fiches (CPU)** | 5 | 5 | 4 | 4 | 1 | **400** |
| **2** | **E2\* — Validité nulle, non-dégénérescence et levée du plafond $N$ sur 8B honnêtes (Sas 2.5)** | 5 | 4 | 5 | 3 | 2 | **150** |
| **3** | **E3\* — Audit CPU de fuite d'un post-mortem conditionné *(optionnel sous gel strict)*** | 4 | 4 | 4 | 2 | 2 | **64** |
| **4** | **E4\* — Lecture unique appariée sur 8B et familles de sabotage inédites (Sas 3)** | 5 | 2 | 5 | 5 | 4 | **62,5** |

---

### E1\* (Priorité 1, CPU seul) — Transfert hors spécification et factorisation corpus $\times$ fiches

- **Plan :** $20$ familles composites/adverses de mondes-miroirs CPU (`illustratif`), à covariance rétrécie sur $D_{\text{hon,cal}}$ ($p/n_{\text{exp}} \le 0{,}05$, $\lambda_{\min} > 0$) et perturbations à queues lourdes ($\nu \in \{3, 4\}$, `illustratif`). L'alternative $P_1$ est inconnue à la fois des bases d'archive et des candidats (le rapport de vraisemblance oracle est rapporté comme plafond). Les $10$ familles $O_{1..10}$ génèrent les fiches d'obstruction ; les $10$ familles $O_{11..20}$ sont construites par une instance **aveugle aux fiches et aux candidats**. Plan factoriel $2 \times 2$ à budget CPU et jetons identique : (`Corpus initial` vs `Corpus stratégique aligné dans l'archive du Sas 0`) $\times$ (`Fiches-leurres` vs `Fiches vraies`), complété par un bras placebo à graphes recâblés (degrés et dates préservés). Filtrage Sas 2 par **e-BH** (Wang et Ramdas, 2022, `VÉRIFIÉ`) + **tirage Monte-Carlo de confirmation indépendant** après gel.
- **Test primaire (effet des fiches sur obstructions aveugles $O_{11..20}$, à corpus aligné fixé) :** soit $\bar{\Delta}_{\text{aveugle}}$ la moyenne sur les $10$ familles aveugles de l'écart de puissance $\text{TPR}(\text{Fiches vraies}) - \text{TPR}(\text{Fiches-leurres})$ à $\text{FPR} \le 0{,}05$ (`illustratif`) au-dessus de la meilleure base d'archive, et $c_1$ le seuil exact unilatéral au niveau $\alpha = 0{,}05$ du test de permutation apparié par famille ($2^{10} = 1024$ permutations, `VÉRIFIÉ` ; valeur cible $\bar{\Delta}_{\text{aveugle}} \ge +0{,}08$ à puissance $\approx 0{,}90$, `illustratif`).
  - **$H_A$ (Transfert hors spécification) :** les fiches améliorent la découverte sur obstructions non décrites ($\bar{\Delta}_{\text{aveugle}} \ge c_1$). *Falsifiée* si $\bar{\Delta}_{\text{aveugle}} < c_1$.
  - **$H_B$ (Appariement fiche-monde ou absence d'effet) :** aucun transfert hors des obstructions décrites ($\bar{\Delta}_{\text{aveugle}} < c_1$). *Falsifiée* si $\bar{\Delta}_{\text{aveugle}} \ge c_1$.
- **Diagnostics secondaires préenregistrés (chacun à seuil unique) :** (i) effet principal du corpus aligné contre le graphe recâblé sur $O_{11..20}$ ; (ii) stabilité relative $\bar{\Delta}_{O_{11..20}} - 0{,}40\,\bar{\Delta}_{O_{1..10}} \ge 0$ (`illustratif`) conditionnée au témoin positif $\bar{\Delta}_{O_{1..10}} > 0$.
- **Contrôles négatifs et positifs :** (1) fiches-leurres (doivent rester près de $0$) ; (2) mondes sans signal ($\widehat{\text{FPR}} \le 0{,}05$) ; (3) graphes recâblés préservant degrés et dates ; (4) témoin positif Sas 0 (extension connue identique à CUSUM pour $T \le N$) ; (5) plafond oracle Neyman-Pearson.
- **Coût `(illustratif)` :** CPU seul (16–32 cœurs), 30 à 80 heures-CPU ; 50 à 200 €. Zéro GPU, zéro famille de sabotage consommée.

### E2\* (Priorité 2, GPU léger sur $D_{\text{hon,filtre}}$ seul) — Validité nulle, non-dégénérescence et levée du plafond $N$ sur 8B

- **Plan :** exécutée sur le jeu honnête indépendant $D_{\text{hon,filtre}}$ sur deux lignées ouvertes ~8B (`Llama-3.1-8B-Instruct`, `Qwen2.5-7B-Instruct`, `propositions`). Deux tests séquentiels à porte, chacun sans zone tampon :
  - **E2\*a (Validité nulle à $T = 4N$ et sous consigne auxiliaire privée bénigne) :** $M = 1000$ trajectoires honnêtes longues (`illustratif`, $N = 100$, incluant une strate à consigne privée bénigne non verbalisée) et $n = 600$ paires honnêtes appariées neutre/persuasif (`illustratif`). Seuil unique exact : $K \le 63$ fausses alarmes sur $1000$ (pour $p = 0{,}05$, erreur d'élimination $\approx 2{,}5\,\%$ ; pour $p = 0{,}08$, erreur d'acceptation $\approx 2{,}7\,\%$, `VÉRIFIÉ` par approximation normale pour ces valeurs `illustratives`) ET $|\widehat{\Delta\text{FPR}}_{\text{style}}| \le 0{,}025$ (`illustratif`, test exact de McNemar).
    - **$H_{A,1}$ (Conservation de validité sur 8B) :** franchissement du seuil unique sur les deux modèles 8B. *Falsifiée* par tout dépassement.
    - **$H_{B,1}$ (Brisure par géométrie 8B réelle) :** dépassement du seuil sur au moins un modèle 8B. *Falsifiée* par le franchissement sur les deux modèles.
  - **E2\*b (Conditionnel à E2\*a — Anti-dégénérescence et levée du plafond $N$) :** contrôle préalable de signal cognitif résiduel ($\widehat{\text{AUC}}_{\text{cognitif}} \ge 0{,}70$ entre tâches honnêtes de complexité distincte, alors qu'une sonde placebo orthogonale échoue, `illustratif`), suivi sur $M_{\text{inj}} = 300$ trajectoires longues ($T = 4N$, `illustratif`) de $D_{\text{hon,filtre}}$ munies d'un signal diffus synthétique planté (hors familles aveugles) d'un test exact de McNemar unilatéral apparié ($\alpha = 0{,}01$, `illustratif`) contre l'accumulateur à référence fixe $N$ (seuil critique unique $c_2$).
    - **$H_{A,2}$ (Levée effective du plafond d'évidence $N$) :** statistique de McNemar $\ge c_2$. *Falsifiée* si $< c_2$.
    - **$H_{B,2}$ (Absence de gain au-delà de $N$ ou sur-conservatisme) :** statistique $< c_2$. *Falsifiée* si $\ge c_2$.
- **Contrôles :** (1) trajectoires rééchantillonnées i.i.d. depuis $N$ ; (2) sonde placebo orthogonale ; (3) classifieur stylométrique pur (témoin positif de style) ; (4) injection forte dans activations 8B (témoin positif de chaîne).
- **Coût `(illustratif)` :** 1 GPU 24 Go VRAM, 40 à 80 heures-GPU (activations stockées sur NVMe, évaluation multi-candidats sur CPU) ; 40 à 160 €. Zéro famille consommée.

### E3\* (Priorité 3, CPU seul, optionnelle sous gel strict) — Fuite adaptative du post-mortem conditionné

- **Plan :** $K = 8$ cycles d'épreuve synthétiques et $J = 20$ familles finales indépendantes (`illustratif`, unité statistique = la famille), paramétrés par le recouvrement structurel continu $\kappa \in \{0 ; 0{,}25 ; 0{,}50 ; 0{,}75 ; 1\}$ (`illustratif`). Comparaison à budget égal entre *gel strict pré-Sas 3* (diagnostics honnêtes aveugles aux verdicts) et *post-mortem conditionné* (les échecs orientent les propriétés honnêtes ajoutées).
- **Inférence forte (au régime intermédiaire préenregistré $\kappa = 0{,}25$, `illustratif`) :** test exact de permutation apparié sur les $J = 20$ familles finales ($\alpha = 0{,}05$ unilatéral, seuil unique $c_3$) portant sur $\bar{\Delta}_{\text{gen}} = \overline{\text{TPR}}_{\text{final}}(\text{post-mortem}) - \overline{\text{TPR}}_{\text{final}}(\text{gel strict})$ à $\widehat{\text{FPR}}$ contrôlé sur jeu honnête frais.
  - **$H_A$ (Gain net du post-mortem sans dégradation)** : $\bar{\Delta}_{\text{gen}} \ge c_3$ sans inflation $\text{FPR}$ sur jeu frais. *Falsifiée* si $< c_3$ ou si $\text{FPR}$ dérive.
  - **$H_B$ (Fuite adaptative sans gain hors-échantillon)** : $\bar{\Delta}_{\text{gen}} < c_3$ (impose le maintien du gel strict). *Falsifiée* si $H_A$ est franchie.
- **Contrôles d'extrémité :** $\kappa = 1$ (i.i.d., témoin positif) et $\kappa = 0$ (disjoint, contrôle négatif).
- **Coût `(illustratif)` :** CPU seul (32 cœurs), 40 à 100 heures-CPU ; 50 à 150 €.

### E4\* (Priorité 4, GPU + oracle, préenregistrée, lecture unique) — Épreuve décisive sur 8B et familles inédites (Sas 3)

- **Préconditions vérifiées avant ouverture :** (i) calibration de l'oracle exogène sur dommages plantés stratifiés (masquée à l'organisme) confirmant $\min_s \hat{p}_s \ge p_{\min}$ (`illustratif`) et homogénéité intra-strate ; (ii) vérification que le plancher d'audit aléatoire à coût égal vérifie $1 - R_{\text{audit}} \ge 0{,}30$ (`illustratif`) ; (iii) préenregistrement SHA-256 de tous les détecteurs gelés : top-$2$ candidats valides de l'organisme + $1$ candidat valide de rang médian (diagnostic de restriction de plage à coût marginal nul) + bases mécaniques + **bras témoin LLM sans organisme** ayant généré le même nombre de candidats et franchi la **même cascade Sas 0–2.5**.
- **Plan et portée :** $M = 180$ trajectoires longues appariées (`illustratif`), réparties idéalement sur $k_{\text{fam}} = 3$ mini-familles aveugles indépendantes ($60$ chacune, `illustratif` ; si le budget impose $k_{\text{fam}} = 1$, la conclusion est explicitement restreinte à cette famille). Contrôle préalable de $\widehat{\text{FPR}}_{\text{eval}}$ sur $D_{\text{hon,eval}}$ (comprenant erreurs honnêtes, consignes privées bénignes et une troisième lignée 8B non vue). Tous les détecteurs gelés sont scorés hors-ligne sur les **mêmes** activations extraites.
- **Inférence forte séquentielle à porte (sans zone tampon) :**
  - **Test primaire E4\*a (valeur en contrôle vs meilleure base mécanique et plancher d'audit à coût égal) :** test exact de McNemar unilatéral apparié (correction de Holm pour $r = 2$, $\alpha_{\text{corr}} = 0{,}025$, `illustratif`), seuil critique unique $c_{4a}$ exprimé sur la réduction relative d'évasion $\widehat{\text{RR}}_{\text{manqué}} = 1 - \frac{1 - \widehat{\text{TPR}}_{\text{cand}}}{1 - \widehat{\text{TPR}}_{\text{ref}}}$ (ex. $\widehat{\text{RR}}_{\text{manqué}} \ge 0{,}25$ et économie d'audit mesurée, `illustratif`).
    - **$H_{A,1}$ (Gain réel en contrôle 8B) :** maintien de $\widehat{\text{FPR}}_{\text{eval}}$ et statistique $\ge c_{4a}$. *Falsifiée* si $< c_{4a}$ ou si $\widehat{\text{FPR}}_{\text{eval}}$ excède le seuil.
    - **$H_{B,1}$ (Saturation par bases mécaniques ou plancher d'audit) :** échec du seuil $c_{4a}$. *Falsifiée* si $H_{A,1}$ est franchie.
  - **Test secondaire conditionnel E4\*b (attribution de la source du gain, exécuté seulement si $H_{B,1}$ est réfutée, sans perte de niveau $\alpha$) :** même test de McNemar apparié contre le témoin LLM-sans-organisme passé par les mêmes sas, au seuil unique $c_{4b}$ ($\alpha = 0{,}025$, `illustratif`).
    - **$H_{A,2}$ (Valeur propre de l'organisme) :** statistique $\ge c_{4b}$. *Falsifiée* si $< c_{4b}$.
    - **$H_{B,2}$ (Gain dû au LLM d'appui et aux sas seuls) :** statistique $< c_{4b}$. *Falsifiée* si $\ge c_{4b}$.
- **Coût `(illustratif)` :** 1 à 2 GPU 40–80 Go VRAM, 120 à 250 heures-GPU (180 à 600 €) + 40 à 80 heures d'oracle exogène et conception aveugle (2 000 à 5 000 €).

---

## (c) Réponse à la question de l'arbitre (synthèse en une page)

### Ce qui est établi

- **Contraintes du dispositif (`RAPPORTÉ`) :** le programme de contrôle porte sur des modèles ouverts autour de huit milliards de paramètres sous budget GPU modeste, avec séparation stricte entre sélection et évaluation (aucun score de moniteur ne peut orienter un proposeur), évaluation à lecture unique sur familles de sabotage inédites conçues à l'aveugle, banque finale lue une seule fois, plancher d'audit au hasard dépendant d'un oracle exogène calibré par strate, et plafonnement des accumulateurs séquentiels calibrés sur référence honnête fixe de taille finie au-delà de $N$. L'organisme d'idéation dispose déjà de bancs processeur à lois plantées et maintient ses modifications en pause.
- **Contraintes mathématiques et statistiques (`VÉRIFIÉ`) :** (1) toute boucle fermée renvoyant un verdict issu des familles d'épreuve — y compris un post-mortem conditionné à un échec au Sas 3 — induit une analyse adaptative qui érode la validité hors échantillon (Dwork et al., 2015) ; (2) calibrer un monde synthétique sur une covariance empirique non régularisée quand $n_{\text{exp}} \le d$ crée un noyau artificiel exploitable (Marchenko et Pastur, 1967), et une hypothèse sous-gaussienne échoue sous queues lourdes ; (3) sur une alternative simple connue, le rapport de vraisemblance est optimal (Neyman et Pearson, 1933 ; Wald et Wolfowitz, 1948), de sorte que les bancs CPU doivent porter sur des alternatives composites/adverses à ignorance symétrique ; (4) le contrôle multiple sur mondes partagés requiert e-BH (Wang et Ramdas, 2022) ou Benjamini-Yekutieli (2001) et un tirage de confirmation indépendant ; (5) la sélection sur données honnêtes seules favorise les détecteurs dégénérés sauf contrôle de puissance ou de signal interne.

### Ce qui ne l'est pas (`HYPOTHÈSE` ou « je ne sais pas »)

- **Transfert de domaine :** je ne sais pas si les capacités de l'organisme sur mondes synthétiques non adverses transfèrent vers la détection de menaces diffuses sur activations neuronales 8B (`HYPOTHÈSE`).
- **Nature du verrou principal :** je ne sais pas si le programme de contrôle est limité par un manque d'objets mathématiques nouveaux, par la faiblesse ou la colinéarité stylistique du signal dans les activations, ou par la sensibilité $p_s$ de l'oracle exogène (`HYPOTHÈSE`).
- **Valeur ajoutée propre de l'organisme :** il n'est pas établi que l'organisme dépasse un appel répété aux mêmes modèles pré-entraînés filtré par la même cascade de sas (`HYPOTHÈSE`).
- **Généralisation inter-familles et d'échelle :** je ne sais pas si un mécanisme validé sur une à trois familles sur modèles 8B généralise à d'autres familles de sabotage ou à des modèles plus grands (`HYPOTHÈSE`).

### Réponse architecturale révisée (`PROPOSITION`)

Pour relier les deux systèmes sans invalider la lecture unique, il faut **rejeter toute boucle fermée** et installer une **interface unidirectionnelle par obstructions formelles et sas en cascade** : (1) en amont, des fiches d'obstruction abstraites et des statistiques issues d'un premier jeu honnête régularisé ($D_{\text{hon,cal}}$) — avec masquage strict des $p_s$ de l'oracle et gel strict pré-Sas 3 ; (2) en filtration, un Sas 0 exécutable multi-régimes aligné sur le corpus, un Sas 1–2 sur mondes composites/adverses à queues lourdes (e-BH + confirmation), et un Sas 2.5 sur un deuxième jeu honnête 8B ($D_{\text{hon,filtre}}$) testant à la fois la validité nulle (y compris sous consigne privée bénigne) et la levée du plafond $N$ sur signal planté ; (3) en aval, une épreuve préenregistrée à lecture unique (Sas 3) sur un troisième jeu honnête ($D_{\text{hon,eval}}$, lignée supplémentaire incluse), appariée sur les mêmes trajectoires contre les bases mécaniques et un témoin LLM traversant les mêmes sas, puis vérifiée par une red-team et un audit externes en double aveugle.

### L'expérience à faire en premier

Avant toute dépense GPU lourde et avant d'ouvrir une seule famille de sabotage, l'expérience prioritaire est **E1\* (processeur seul, 30 à 80 heures-CPU, 50 à 200 €, `illustratif`)**. Elle tranche à coût minimal si les fiches d'obstruction et le rééquilibrage disciplinaire produisent un transfert réel vers $10$ familles d'obstructions composites/adverses **conçues à l'aveugle des fiches** ($O_{11..20}$, `illustratif`), ou s'il ne s'agit que d'un appariement local aux énoncés ou d'une restitution documentaire (contrôlée par l'alignement du Sas 0, des fiches-leurres et des graphes recâblés préservant degrés et dates). Son seuil critique unique (test de permutation exact inter-familles, $\alpha = 0{,}05$, `illustratif`) falsifie soit le transfert hors spécification ($H_A$), soit l'absence de transfert ($H_B$) sans zone tampon. Si $H_A$ est falsifiée, le couplage est réorienté sur processeur sans gaspiller le budget GPU ni les lectures uniques ; si $H_B$ est falsifiée, les candidats gelés passent immédiatement à **E2\*** sur trajectoires honnêtes 8B seules.

FIN-DE-CELLULE