# Proposition B, tour III.3 : riposte

## 0. État des pièces (règle 2)

- **Pièces E3-T1-B, E3-T2-redteam-A et E3-T2-redteam-C** : elles sont complètes, chacune se termine par son délimiteur. Je ne réponds qu'aux sections « Contre la proposition B ».
- **Annexe 3 de la question** : 20 sections Claude vides ou réduites à un mot ou coupées, 10 sections Gemini coupées. C'est inchangé depuis III.1. Je n'en reconstitue rien.
- **Bloc FAITS** : les accents y sont remplacés par « ? ». L'en-tête indique « protocole v2.5 » alors que la consigne indique « v2 ». L'écart n'est pas résolu et n'a aucun effet sur les statuts.
- **Empreintes sha256** : je ne peux pas les vérifier.

**Statuts, inchangés.**
- Faits, sections 1 et 2 : VÉRIFIÉ.
- Propositions des explorateurs : HYPOTHÈSE.
- Scores et effectifs des annexes : OBSERVÉ-NON-AUDITÉ. C'est l'attribution que j'ai faite en III.1 faute d'étiquette, et je la maintiens telle quelle.
- Attaques A et C, et ma propre conception : HYPOTHÈSE.

**Bilan.** J'ai traité 23 attaques. Aucune n'est rejetée en bloc et cinq sont rejetées en partie. Trois défauts de ma conception de III.1 étaient réels :
- G servait de mesure de validité alors qu'elle ne mesure que la conformité au gabarit ;
- mes duels D1 et D3 contenaient des zones mortes, ce qui viole B4 ;
- le facteur D de J était purement déclaratif.

---

## (a) Verdicts

### Attaques de l'équipe A

| ID | Attaque | Verdict | Correction |
|---|---|---|---|
| F-B1 | G n'est jamais validée et elle est syntaxique | **Acceptée** pour le rôle de G comme composante de validité dans M et J. **Rejetée** pour son rôle de plancher à battre : un plancher doit être bête, c'est précisément pour cela qu'il est syntaxique. **Transformée en test** : bras adversaire R dans D1'. | G est rétrogradée au rang de plancher et n'est plus jamais un facteur de validité (règle R3). |
| F-B2 | Fuite entre construction et évaluation dans D3, la nouveauté étant maximisée par construction dans DEF | **Acceptée** | La nouveauté est mesurée sur la signature expérimentale σ, qui est absente du prompt DEF (D3'). |
| F-B3 | Il manque le bras « i.i.d. + déduplication » | **Acceptée**. Ce bras a été formulé par C et transmis par A ; je m'en sers en le disant. | Il devient le comparateur principal de D3'. |
| F-B4 | D0 dépend de prompts déclarés indisponibles | **Acceptée en partie** : je retire la relance « avec prompts exacts ». **Rejetée en partie** : D0 se tranche sur les réponses brutes journalisées, sans relance. D4 est prospectif et utilise des prompts neufs, il ne dépend pas du premier passage. La chaîne D0 → D4 ne s'effondre donc pas. | D0' et R6 |
| F-B5 | Zones mortes et puissance insuffisante | **Acceptée**. Pour une AUC comprise entre 0,60 et 0,80, D1 ne falsifiait rien, et le TOST à ±5 points était hors de portée avec environ 50 propositions par bras. | Règle R1 (coupure unique, décision forcée) et n calculé à l'avance. |
| F-B6 | Le juge est unique, non calibré et non aveuglable | **Acceptée**, **transformée en test** (ré-identification de l'espèce et kappa inter-juges). | R5 : le juge ne peut plus trancher la vérité d'une affirmation. |
| F-B7 | Le coût GPU de D est auto-déclaré | **Acceptée** | R4 : le coût est calculé, pas déclaré. |
| F-B8 | La « fausse chimère » fuit par le titre | **Acceptée** | Plan 2×2 en D4'. Un contrôle « identifiant seul » ne sert plus qu'à contrôler la dépense de jetons. |
| F-B9 | J est un produit de portes binaires, il ne classe pas | **Acceptée** | D5' compare des règles de sélection par taux, et non par top-10. |
| A-(b) | Un générateur « G-optimal » satisfait toutes les portes | **Acceptée**, **transformée en test** | R2 : bras adversaire permanent R. |
| A-(c)1–6 | Contrôles manquants | **Toutes acceptées** | Intégrées en D1', D3', D4' et D5'. |

### Attaques de l'équipe C

| ID | Attaque | Verdict | Correction |
|---|---|---|---|
| C-a1 | Fuite dans D3 | **Acceptée** (doublon de F-B2) | D3' |
| C-a2 | Un Jaccard nul peut venir d'un simple collage de deux DOI sans rapport | **Acceptée**, **transformée en test** : un bras « collage de DOI aléatoires » doit obtenir N = 1 et V1 = 0. | N n'est plus jamais compté sans V1. |
| C-a3 | D4 confond l'hétérogénéité des espèces et la révision en deux passes | **Acceptée** | Plan 2×2 (D4'). |
| C-a4 | D(p) est déclaratif, et le dénominateur en USD favorise l'espèce la moins chère | Sur D déclaratif : **acceptée**. Sur le biais de coût : **rejetée en partie**, car D4 égalise déjà les enveloppes, et pour J il est voulu de préférer l'espèce la moins chère par unité *validée*. **Acceptée en partie** : l'absence de pénalité pour les faux positifs était un défaut. | Terme −λF dans J' (D5'). |
| C-a5 | Un juge humain ne peut pas vérifier une affirmation mécaniste sans exécution | **Acceptée en partie**. La vérité est tranchée par exécution (V2). Les juges ne tranchent que la décisivité d'un plan, et seulement s'ils passent le test de ré-identification. | R5 et V2 |
| C-b1 | Bourrage de citations réelles mais hors sujet | **Acceptée** | Instrument E (implication entre citation et affirmation), validé en D1'. |
| C-b2 | Rotation des DOI à chaque appel pour garantir un Jaccard nul | **Acceptée** | Nouveauté mesurée sur σ. |
| C-b3 | D se satisfait d'un coût déclaré | **Acceptée** (doublon de F-B7) | R4 |
| C-b4 | Des clones à références renouvelées trompent le DPP fondé sur le Jaccard | **Acceptée sur le fond** : ma référence DPP-Jaccard est trompée par construction. **Rejetée sur la forme** : « J vers l'infini » est une formule sans contenu, J' étant borné par le nombre de propositions et pénalisé. | Audit DPP corrigé. |
| C-c1 | Vérifier l'implication entre citation et affirmation | **Acceptée** | D1', sous-duel E |
| C-c2 | Contrôle d'auto-révision intra-espèce à information égale | **Acceptée** | Diagonale du plan 2×2 |
| C-c3 | Exécution sur sous-échantillon, et contrôle « couches décalées » | **Acceptée** | V2 et R2 |

---

## (b) Expériences corrigées

### Règles communes, nouvelles

- **R1. Coupure unique.** Chaque duel porte sur une statistique θ et une coupure c préenregistrée.
  - H_A : θ > c. H_B : θ ≤ c. Les deux sont exclusives et exhaustives.
  - Le test est unilatéral. La taille n est fixée à l'avance pour α = 0,05 et β = 0,2 à une distance δ de c (illustratif).
  - Quand n est atteint, la décision est forcée en comparant l'estimation à c, et le risque d'erreur réalisé est publié.
  - Il n'y a donc plus de zone morte : chaque issue falsifie H_A ou H_B. Cela répond à F-B5.
- **R2. Bras adversaires permanents, injectés dans tout corpus d'évaluation.** Ils sont générés par script, jamais rédigés à la main.
  - **R** : bras « G-optimal ». Gabarit complet, deux références réelles hors sujet, DOI renouvelés à chaque appel, coût déclaré, aucun éponyme, bornes numériques opposées pour H_A et H_B.
  - **MK** : texte absurde produit par une chaîne de Markov sur des titres arXiv et placé dans le gabarit.
  - **COL** : collage de deux DOI aléatoires.
  - **STUF** : une proposition saine dans laquelle on injecte deux DOI réels de biologie marine.
  - **DEC** : une prémisse contraire aux faits VÉRIFIÉ, par exemple *Value Neurons* placés hors des couches 2 à 5.
  - **Règle de falsification transversale** : tout sélecteur qui retient R, MK, COL, STUF ou DEC à un taux supérieur ou égal à celui des propositions honnêtes est falsifié en tant que sélecteur, quel que soit le reste de ses résultats.
- **R3.** G ne sert plus que de plancher. Elle n'intervient dans aucune métrique de validité.
- **R4. Coût calculé.** Un estimateur figé (nombre de prompts × jetons × taille du modèle × tarif GPU, tarif illustratif) est appliqué au protocole par notre code. Un essai à vide sur 1 % des prompts (illustratif) vérifie l'estimation.
- **R5. Juges.**
  - Au moins deux juges indépendants, avec un kappa publié.
  - Un test de ré-identification de l'espèce ou du bras a lieu au préalable. Si l'exactitude dépasse le hasard (test binomial), les juges sont déclarés non aveugles et retirés du critère.
  - Les juges ne tranchent jamais la vérité d'une affirmation mécaniste.
- **R6.** Aucune donnée Claude du premier passage n'entre dans une comparaison tant que D0' n'est pas tranché.

### D0' : que signifie −1,00 ? (corrige F-B4)

- **H_A** : −1 est une sentinelle d'échec du pipeline.
- **H_B** : −1 est le verdict de `jev` sur un contenu transmis.
- **Prérequis** :
  - test-retest de `jev` sur 5 textes Gemini (même score, à ±0,25 illustratif) ;
  - si les journaux sont absents, D0' est inexécutable et le constat est déclaré. Les 20 enregistrements Claude sont alors exclus, sans imputation.
- **Mesure** : score `jev` des réponses brutes Claude non vides retrouvées dans les journaux, resoumises telles quelles. Aucune relance n'est nécessaire.
- **Décision exhaustive** :
  - aucun brut non vide : **H_B falsifiée**, puisqu'il n'y avait rien à juger ;
  - bruts non vides rescorés −1 dans au moins 90 % des cas (illustratif) : **H_A falsifiée** ;
  - sinon : **H_B falsifiée**.
- **Contrôle** : la chaîne vide, pour laquelle on attend −1 sous H_A. Ce contrôle est informatif mais pas décisif.
- **Coût** : 0 USD.

### D1' : validation conjointe de `jev`, de G et de E

- **Corpus honnête** : les 10 textes Gemini complets s'ils existent dans les journaux. Sinon, 10 propositions écrites à partir des ancrages VÉRIFIÉ : verdict nul de P3, incidents *Sol* et *Astra*, pression aversive (0,49 → 0,65), sous-système parcimonieux de récompense.
- **Versions comparées** : les 5 dégradations de III.1 plus R, MK, COL, STUF et DEC.

**Duel principal**

- θ = AUC_jev − AUC_G, pour séparer les textes honnêtes des textes dégradés ou adverses. Coupure c = 0,10 (illustratif).
- **H_A** : θ > c. `jev` mesure quelque chose que le plancher ne mesure pas.
- **H_B** : θ ≤ c.
- **Prédiction (HYPOTHÈSE)** : G laisse passer R par construction, et si `jev` note aussi R au plafond, alors H_B.
- **Conséquence de H_B** : la question « quels champions résistent à Goodhart sur `jev` ? » devient sans objet, et `jev` est retiré de tous les critères.

**Sous-duel E : `jev` peut-il vérifier l'implication entre citation et affirmation ?**

- Paires comparées : (proposition, référence pertinente) contre (même proposition, référence réelle hors domaine).
- θ_E = AUC, coupure 0,80 (illustratif).
- **H_A** : `jev` est un instrument E utilisable.
- **H_B** : il ne l'est pas. E doit alors se faire sur un échantillon par des humains, ce qui réduit n dans D3' et D5'. Je l'annonce dès maintenant.

**Prérequis** : invariance à ±0,25 (illustratif) quand on ne modifie que l'espacement ou la ponctuation. Sinon, l'instrument est déclaré sensible au format et le duel n'est pas interprété.

**Coût** : 0 USD (`jev` illimité, Crossref et Semantic Scholar gratuits, VÉRIFIÉ).

### D2' : identité des vagues

Ce duel est inchangé, aucune équipe rouge ne l'a attaqué. Il consiste à recalculer les statistiques depuis les enregistrements individuels, pour 0 USD.

### D3' : déflation séquentielle contre i.i.d. avec déduplication (corrige F-B2, F-B3, F-B5, C-a1, C-a2, C-b2)

**Bras** (même modèle, même nombre d'appels, même température) :
- **DEF** : le prompt de la vague *t* contient les seuls noms de bassins des vagues < *t*.
- **IID+DEDUP** : aucun historique. Après génération, on élimine les doublons sur les *mêmes* noms de bassins et DOI. C'est le comparateur principal.
- **PLACEBO** : historique de même longueur, tiré d'un autre cône.

**Nouveauté sans fuite**
- La signature expérimentale σ(p) est le quadruplet : composant du modèle visé, intervention, métrique, sens prédit.
- Elle est extraite par deux annotateurs aveugles au bras, avec un kappa publié.
- σ ne figure pas dans le prompt DEF.
- Contrôle « références permutées » (A-c5) : N_σ doit rester inchangé quand on échange les bibliographies.
- **Fuite résiduelle (HYPOTHÈSE)** : les noms de bassins corrèlent peut-être avec σ. On la mesure par la proportion de σ répétées malgré un bassin nouveau.

**Métrique et duel**
- **Validité** : V1 = E, l'instrument validé en D1'.
- **M** = proportion d'*appels* des vagues 5 à 10 qui produisent une proposition p avec V1 = 1 et une σ nouvelle dans le bras.
- θ = M(DEF) − M(IID+DEDUP), coupure c = 0,10 (illustratif).
- **H_A** : θ > c. L'exclusion séquentielle *a priori* apporte plus qu'un filtre *a posteriori*.
- **H_B** : θ ≤ c.

**Puissance et budget**
- Pour p ≈ 0,4, une demi-largeur d'IC à 95 % d'environ 0,10 sur une différence exige environ 185 appels par bras dans les vagues 5 à 10. Ce chiffre est illustratif ; il s'obtient par n ≈ 2p(1−p)·(1,96/0,10)².
- Le reliquat Gemini est inconnu (P13). S'il est insuffisant, je ne garde que le duel DEF contre IID+DEDUP et j'abandonne PLACEBO. Si même ce duel ne tient pas dans le budget, je ne l'exécute pas : **aucune exécution sous-dimensionnée**.

**Duel secondaire**, selon la même règle R1 : θ' = M(DEF) − M(PLACEBO), coupure 0,05 (illustratif). Il indique si le gain vient de la longueur du prompt.

### D4' : monocultures contre chimère, plan 2×2 (corrige F-B8, C-a3, C-c2)

**Cellules** (proposeur → réviseur, le réviseur lisant le texte complet) :
- Gemini → Gemini et Claude → Claude (diagonale) ;
- Gemini → Claude et Claude → Gemini (hors diagonale).

**Conditions**
- Enveloppe en USD identique par cellule, plafonnée à la plus petite.
- Contrôle de dépense (A-c6) : un réviseur qui ne reçoit que l'identifiant de la proposition.

**Critère de survie** : S = V1 ∧ σ distincte ∧ verdict des juges. Le verdict des juges n'entre que s'ils passent R5 ; sinon il est omis.

**Duel**
- χ = moyenne des survivants par USD hors diagonale ÷ maximum des survivants par USD sur la diagonale. Coupure c = 1,15 (illustratif).
- **H_A** : χ > c. Il existe un gain inter-espèces au-delà de la révision intra-espèce.
- **H_B** : χ ≤ c. L'effet observé vient de la boucle de révision, pas du mélange des espèces.

**Prérequis** : vérifier le pipeline Claude sur des prompts neufs, environ 10 appels (illustratif). Ce prérequis est indépendant des prompts du premier passage.

### D5' : fonction objectif corrigée (corrige F-B7, F-B9, C-a4, C-a5, C-b3, C-c3)

**Fonction (HYPOTHÈSE, non validée)**

$$J' = \frac{\sum_p V_1(p)\,N_\sigma(p)\,T(p) \;-\; \lambda \sum_p F(p)}{\text{USD}_{\text{calculé}}}$$

- **T(p), non-trivialité** : deux prévisionnistes figés, des juges selon R5 ou un modèle gelé, donnent ex ante une probabilité de H_A comprise entre 0,2 et 0,8 (illustratif). Ce contrôle de trivialité vient de l'attaque de C *contre A* ; je m'en sers en le disant. Il élimine les tautologies du type « la norme L2 de la couche 1 est nulle ».
- **F(p), faux positif** : la proposition passe le filtre mais échoue en V2 (protocole non exécutable, mesure non produite, prémisse contraire à un fait VÉRIFIÉ comme dans DEC).
- **λ** = 2 (illustratif).

**Sélecteurs comparés, par taux et non par top-10**
- S_J' : passe J'.
- S_jev : score `jev` maximal.
- S_hasard : tirage parmi les propositions qui passent G.
- Tant que les scores `jev` restent constants, S_jev est identique à S_hasard. S_jev ne devient un bras distinct qu'après un résultat H_A en D1'.

**Critère externe V2** : exécution sur `Llama-3.1-8B-Instruct`, sur 1 A100 80 Go, d'un échantillon aléatoire stratifié de k propositions par sélecteur (k = 8, illustratif). On vérifie quatre conditions :
1. le protocole s'exécute tel qu'écrit ;
2. la mesure est produite ;
3. la décision est rendue au seuil préenregistré ;
4. l'issue n'avait pas été prédite avec une probabilité supérieure à 0,8.

**Duel**
- θ = taux(S_J') − taux(S_hasard), coupure c = 0,20 (illustratif).
- **H_A** : θ > c.
- **H_B** : θ ≤ c.
- Avec k = 8, le risque d'erreur est élevé. Il est publié, et D5' est déclaré **pilote**. k est doublé si le budget GPU le permet.

**Contrôle positif (VÉRIFIÉ)** : tout pont qui affirme un mécanisme parcimonieux doit d'abord reproduire l'effet d'ablation de −54,9 points (Xu et al., 2026 : référence à vérifier, titre non fourni). La ré-identification préalable des neurones sur Llama n'est pas budgétée ici, et je le signale.

### Audit DPP corrigé (C-b4)

- **Ensemble test** : 10 propositions distinctes, 10 clones (même protocole, références renouvelées) et 10 paraphrases.
- **H_A** : le DPP opère sur le contenu. Il retient au plus 1 clone et au plus 1 paraphrase.
- **H_B** : il retient plus de 1 clone ou plus de 1 paraphrase.
- **Prédiction (HYPOTHÈSE)** : ma référence de III.1, le DPP par Jaccard des références, retient les 10 clones puisque sa matrice de similarité est l'identité. Elle est déclassée.
- Le test du déterminant sur les entrées vides de III.1 est maintenu.

---

## (c) Réponse à la question de l'arbitre, en une page

**Ce qui est établi**

- **VÉRIFIÉ (faits)** :
  - les budgets : 100 USD Anthropic, 20 USD Gemini, `jev` illimité, API de littérature gratuites ;
  - les quatre ancrages empiriques ;
  - l'absence de tête de sabotage préétablie et de sonde temps réel.
- **OBSERVÉ-NON-AUDITÉ** :
  - les 10 vagues ont un résumé identique (moyenne 2,96, maximum 3,75, n = 12) ;
  - `jev` ne prend que deux valeurs (3,75 pour Gemini, −1,00 pour Claude), et la « Rigueur » que deux valeurs (3,00 et 0,00) ;
  - 18 textes Claude sur 20 sont vides et les 10 textes Gemini sont coupés ;
  - les effectifs se contredisent : 120 agents valides contre 300 annoncés, 40 lignes dans un tableau intitulé « Top 60 » ;
  - le cône est égal à *k* mod 10 sur les entrées visibles.
- **Arithmétique vérifiable** sur ces chiffres : (10 × 3,75 + 2 × (−1)) / 12 = 2,958. L'*interprétation* (chaque vague = 10 Gemini et 2 Claude) reste une HYPOTHÈSE, testée par D2'.

**Ce qui n'est pas établi**

- Des « pépites » des vagues 5 à 10 dues à l'épuisement des bassins : il n'y a ni bras i.i.d., ni textes complets.
- Que la déflation ait été réellement appliquée.
- L'orthogonalité des cônes.
- Que le DPP ait opéré sur le contenu.
- La validité de `jev` comme auditeur.
- Une quelconque résistance à Goodhart.
- L'avantage d'un essaim chimérique.
- **Concession aux deux équipes rouges** : ma propre porte G et mon objectif J de III.1. G mesure la conformité au gabarit, et D était déclaratif. J' et σ sont des HYPOTHÈSES non validées.
- **Je maintiens mon refus** de produire une $\mathcal{L}^*$ et « 8 ponts extraits » : sur des textes vides ou coupés, ce serait une invention présentée comme une extraction. L'attaque F-C1 de l'équipe A contre C décrit précisément ce risque.

**L'expérience à faire en premier : D1'**

- **Pourquoi elle** : chacune des trois demandes (Goodhart, sélection des champions, objectif) passe par un instrument d'audit, et aucun n'est validé, ni `jev`, ni G, ni E.
- **Coût** : 0 USD d'API. Elle n'utilise que `jev` illimité, Crossref et Semantic Scholar.
- **Ce que falsifie chaque issue** :
  - θ > 0,10 falsifie « `jev` récompense le gabarit » et donne enfin un sens à la question de Goodhart ;
  - θ ≤ 0,10 falsifie « `jev` est un auditeur », retire `jev` de tous les critères et rend caducs les scores de l'annexe 2.
- **En parallèle, le même jour** : D0' et D2'. Ce sont des lectures de journaux, sans aucune génération. Elles disent si 20 des 30 « champions » sont des données ou des échecs de pipeline.

**Ce qui me réfuterait**
- un résultat H_A en D1' avec R noté bas ;
- des bruts Claude non vides rescorés −1 en D0' ;
- θ > 0,10 en D3' contre IID+DEDUP.

FIN-DE-CELLULE