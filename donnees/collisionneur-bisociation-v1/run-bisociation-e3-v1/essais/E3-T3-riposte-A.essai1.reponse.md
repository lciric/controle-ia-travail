# Cellule A — Tour III.3 — réponse aux critiques

## 0. Pièces reçues

Les deux critiques (B, C) et ma conception du tour III.1 sont présentes, complètes, closes par leur ligne de fin. Je ne réponds qu'aux sections qui visent A. Statuts : les chiffres de la pièce B restent RAPPORTÉS ; les calculs des critiques sur ces chiffres sont « dérivés par B » ou « dérivés par C », non audités par moi ; les miens sont « illustratifs ». Deux fichiers invoqués par les critiques (`methodes_v1.py`, `monde_v1.py`) sont cités par empreinte dans la pièce B mais **absents des pièces** : je ne décris pas leur contenu.

---

## (a) Réponse à chaque critique

### Critiques de B visant A

| # | Critique | Décision | Raison / forme |
|---|---|---|---|
| A-1 | La vérité des mondes étendus recopie le score c_ij : E1 vrai par construction. | **Acceptée.** | C'est la même faute que C-1 de C. La vérité sera plantée par **opérateur latent** observé par un canal calibré à part, avec les **deux** mécanismes de B (greffes, jumeaux) conservés ; c_ij n'est jamais une entrée du générateur. Transformée en test : V2 de B (vérité découplée), que je reprends tel quel en le disant. |
| A-2 | (1 − s)^β est dominé par q_i q_j à β = 1 ; β ≈ 7 pour peser autant (dérivé par B). | **Acceptée.** | Dans les mondes de B, q est indépendant de la vérité (B § 3, RAPPORTÉ) : le pondérer est du bruit. Correction : exposant η sur q, η = 0 dans tous les tests synthétiques ; β n'est plus « 1 par défaut » mais fixé sur graines de calibrage pour que le terme soit opérant (V1 le mesure). |
| A-3 | O-paires à γ → 0 est un argmax pondéré par strate ; E2 confond répulsion et passage à l'argmax. | **Acceptée.** | J'ajoute le bras (g) « argmax de w par strate, sans déterminant » (option 1b de C, dont je me sers en le disant). E2 disparaît comme expérience séparée et devient le facteur « répulsion » d'un plan factoriel (E1'). |
| A-4 | E3 : hypothèses non exclusives ; géométrie à 2 champs ; τ balayé sur les mondes de décision = fuite. | **Acceptée** sur les trois points. | E3' est reformulée en « le passage aux paires est-il **nécessaire** ? » (exclusif) ; stratifiée par nombre de champs ; τ fixé sur 100 graines de calibrage distinctes (illustratif). |
| A-5 | Le critère « classifieur ≤ hasard + 0,10 » rejette un extracteur parfait si les vrais concepts dépendent du domaine ; dans B, fixé par construction. | **Acceptée** ; transformée. | Nouveau critère **relatif** : le vecteur de concepts ne doit pas prédire le domaine **mieux que les opérateurs latents vrais ne le prédisent** (plafond oracle, mesuré sur graines de calibrage). Ce que « groupe » recouvre dans `monde_v1.py` : fichier absent des pièces, à lire avant d'écrire le préenregistrement. |
| A-6 | E5 : confusion par q ; vivier déjà sélectionné par le juge ; anonymat insuffisant. | **Acceptée.** | Ablation q ≡ 1 et bras « stratifié pondéré par q » ajoutés ; bras placebo d'éloignement (paires uniformes sous la même loi de distance de domaine qu'O-paires). La sélection préalable par le juge (N-053) n'a pas de remède dans ce tour : E5 est **reclassée** (voir (b)). |
| A-7 | b_eloigne : on ne sait pas s'il lit les champs vrais ou observés. | **Acceptée.** | HYPOTHÈSE jusqu'à lecture de `methodes_v1.py` (absent). Le témoin exigé devient **b_eloigne-observé** : strates par domaine *estimé* (pièce A, `_domaine_estime`, VÉRIFIÉ), rangées par cosinus de domaine *observé*. Si le b_eloigne de B lit la vérité, ses +11,9 / +6,6 sont un plafond d'oracle, pas un témoin. |
| A-8 | « La différence [0,750 contre 0,322] vient du bruit d'observation » sans statut. | **Acceptée.** | HYPOTHÈSE. Je ne la réutilise pas. |
| (b) tableau | D_w gonflé en zéro ; granularité 1/12 et peu de vrais ponts ; rareté indépendante du statut ; rareté bruitée sur 40 fiches ; β inerte ; E4 ; E5 sous-puissante ; bruit de fusion hétéroscédastique. | **Acceptées** comme conditions de non-jugeabilité. | (i) Le préenregistrement enregistre π = part des mondes où les 12 paires diffèrent entre variantes emboîtées, et l'écart est testé sur les mondes non nuls, avec N fixé par pilote sur graines de calibrage ; (ii) le nombre de vrais ponts valides par monde est **maintenu** au niveau de B (9,5 en « bien », RAPPORTÉ), les ponts de surface ne remplacent pas des vrais ponts ; (iii) une condition « homonymes rares » (rareté indépendante du statut) est ajoutée ; (iv) la rareté vient d'un corpus de référence hors vivier (graines de calibrage), avec pseudo-compte, pas de la fréquence documentaire sur 40 fiches ; (v) V1 ; (vi) E4' ; (vii) et (viii) E5 reclassée, bruit de fusion mesuré par bras. |
| (c) 1-5 | Placebo de concepts conservant marges et étage commun ; monde découplé ; q ≡ 1 ; placebo de domaine conservant les strates ; placebo d'éloignement dans E5. | **Acceptés**, tous les cinq. | Ils entrent dans la liste des contrôles gelés de (b). |
| V1, V2 | Deux vérifications proposées par B. | **Acceptées** comme expériences premières. | Je m'en sers en le disant : V1 devient mon expérience n° 1, V2 ma n° 2. |

### Critiques de C visant A

| # | Critique | Décision | Raison / forme |
|---|---|---|---|
| C.a.1 | Tautologie générateur–objectif dans E1. | **Acceptée** (= A-1). | Même correction. |
| C.a.2 | Coupure à 25 % = fuite d'un paramètre caché de B (le taux de moyeu) et variable confondante. | **Acceptée.** | Le seuil fixe est **supprimé**. La rareté entre de façon continue (poids IDF lissé, corpus de calibrage). Si une coupure est jamais réintroduite, elle est fixée sur graines de calibrage et le témoin « stratifié + même coupure » (C (c) 1) est obligatoire. Le calcul P(B(40 ; 0,25) ≤ 10) ≈ 0,58 est dérivé par C, non audité ; l'argument qualitatif suffit. |
| C.a.3 | λ(e_i + e_j) confond diversité de strates et couplage disjoint ; le stratifié de la pièce A autorise une fiche dans plusieurs paires. | **Acceptée.** VÉRIFIÉ sur la pièce A : `tirage_stratifie` ne retire pas une fiche déjà tirée (seules les paires sont retirées des strates). | λ = 0 par défaut ; λ > 0 devient une ablation séparée, nommée « couplage disjoint », jamais confondue avec la stratification. |
| C.a.4 | L'ancrage R1+R3 par chaîne ou symbole détruit la capacité à relier deux noms différents d'une même structure, ou force un jargon qui fuit dans d_i. | **Acceptée pour moitié, transformée.** | Rejetée sur un point : R3 vérifie qu'un **passage** porte le concept (formule, énoncé, citation), non une égalité de chaîne avec la liste fermée ; la liste fermée est le vocabulaire *canonique* (l'analogue de l'opérateur latent), que le proposeur déclare et ancre. Acceptée sur la fuite : le vecteur de domaine d_i sera calculé sur le texte **hors champ concepts et hors lexique d'opérateurs**. Transformée en test : le contrôle 3 de C (fiches jumelles à vocabulaire de domaine substitué) entre dans E4'. |
| C.b.1 | Effondrement du glouton en tri statique quand Var(log w²) domine la pénalité de strate. | **Acceptée** (= A-2/A-3). | V1 enregistre précisément cette condition : part des mondes où la répulsion change au moins une paire. |
| C.b.2 | Dégénérescence de la coupure à 25 %. | **Acceptée** ; coupure supprimée. | — |
| C.b.3 | Le classifieur linéaire est aveugle aux dépendances d'ordre 2 (OU-exclusif) que le noyau quadratique exploite. | **Acceptée.** | E4' ajoute (i) un test sur la **matrice de Gram** C_ij contre l'adjacence de domaine, par **permutation** (loi nulle empirique, puisque les 780 paires ne sont pas indépendantes, point que B fait contre C et que je prends pour moi) ; (ii) un contrôle de **queue** : part de paires de même champ parmi les k % plus fortes valeurs de C_ij. |
| C.b.4 | E5 : erreur type ≈ 17,5 points sur 12 contre 12, puissance < 15 % (dérivé par C, illustratif). | **Acceptée** (= A-6, tableau de B). | E5 reclassée en pilote de calibrage. Mon ordre de grandeur, illustratif : pour +10 points à p ≈ 0,2–0,3, puissance 0,8, il faudrait ≈ 300 fusions par bras — hors budget raisonnable. |
| C.c.1 | Témoin « stratifié + filtre de moyeux à 25 % ». | **Acceptée** conditionnellement. | Sans objet tant que la coupure est supprimée ; obligatoire si elle revient. |
| C.c.2 | Contrôle d'ordre 2 sur les paires. | **Acceptée.** | Dans E4'. |
| C.c.3 | Invariance de v6.3 par reparamétrisation monotone de q (rang, q^η) avant de conclure que les paires sont indispensables. | **Acceptée.** | Bras « v6.3 avec q par rang » et « v6.3 avec q ≡ 1 » (ce dernier est a_q1 de B : −4,0 / −2,1, RAPPORTÉ) ajoutés à E3'. |

Point non critiqué que je maintiens : **A5** (le mot de Lazar « minimise leur proximité conceptuelle » contre l'hypothèse de la question « proches en concepts ») doit être tranché avant tout préenregistrement ; le signe de α en dépend.

---

## (b) Expériences corrigées

### Forme O-paires v2 (ce qui change)

Ensemble de base : paires valides (étage commun de B inchangé : étiquette d'opérateur partagée, domaines observés différents, filtre passé, jamais fusionnées). Pour p = (i, j) :

- w_p = (q_i q_j)^η · c_ij^α · (1 − s_ij)^β, avec η = 0 dans tout test synthétique ; c_ij = ⟨k_i, k_j⟩ où k est le vecteur de concepts normalisé, pondéré par IDF lissé calculé sur un **corpus de calibrage hors vivier** ; aucune coupure de fréquence ;
- φ_p = indicatrice de la strate (paire de domaines estimés) ; λ = 0 ;
- L_pq = w_p ⟨φ_p, φ_q⟩ w_q + γ δ_pq (Gram pondérée + γI, définie positive pour γ > 0 ; Cholesky de la pièce A applicable).

Je reconnais (A-3, C.b.1) qu'à λ = 0 et γ → 0 ce glouton **est** l'argmax de w_p par strate : la machinerie déterminantale n'ajoute rien par construction. Elle n'est donc plus la « forme recommandée » mais **un des bras** du plan factoriel ; la vraie question est devenue : *quel terme de w_p est opérant, et lequel aide ?* Budget aligné sur B : k = 4 paires × 3 générations = 12 paires, 40 candidats ; le code de la pièce A a `k=4, max_paires=3` par défaut (VÉRIFIÉ) — différent du budget de B, à aligner sur B dans le banc.

### Mondes étendus (générateur, gelé avant toute méthode)

- Mêmes 8 domaines × 5 articles, 2 à 4 champs, trois niveaux d'observation du lexique (B § 5, RAPPORTÉ).
- Vérité plantée par **opérateur latent** (greffes et jumeaux, comme B), jamais par c_ij. Nombre de vrais ponts valides par monde maintenu ≥ celui de B.
- Condition « multi-opérateurs » : 3 à 5 opérateurs latents par article (illustratif), rareté variable ; c'est la seule condition où une proximité **graduée** existe à capter.
- Condition « homonymes rares » : étiquettes de surface rares partagées par des articles à opérateurs latents disjoints, en proportion telle que P(rare | vrai pont) = P(rare | homonyme) (rareté indépendante du statut).
- Condition « concepts inversés » : ponts vrais entre fiches conceptuellement éloignées partageant une étiquette de surface.
- Placebo de concepts : permutation des k_i entre fiches **conservant** les fréquences d'étiquettes et l'ensemble des paires valides (étage commun identique).
- Placebo de domaine : permutation des d_i conservant les strates.
- Témoins reproduits : (b), (d1), a_q1 et b_eloigne-observé doivent retrouver les chiffres de B à leur intervalle près dans la condition « inchangée » ; sinon le générateur est cassé et rien n'est lu.
- Graines : 100 mondes de calibrage par condition (réglage de β, τ, IDF, seuils de queue), 400 mondes de décision, jamais mélangés (illustratif).

Mesure : précision des vrais ponts parmi les 12 paires ; écart apparié ; 2 000 rééchantillonnages ; **π** (part des mondes où les paires diffèrent entre bras emboîtés) enregistré et publié ; test sur mondes non nuls si π < 0,5.

### V1 — Le terme de distance est-il opérant ? (de B, reprise)

- Bras : O-paires v2 avec et sans (1 − s)^β, β fixé sur calibrage ; v6.3 avec q par rang et q ≡ 1, avec et sans son facteur de domaine.
- **H_A** : π ≥ 0,5 et écart dont l'intervalle exclut 0. **H_B** : π ≤ 0,1 et écart dans [−1 ; +1].
- Falsifie : H_B réfute l'objection A-2/C.b.1 pour cette forme ; H_A impose de retirer « volume de domaine » de toute conclusion sur la forme et de passer à un terme plus tranchant avant tout autre test.

### V2 — Le gain conceptuel survit-il à une vérité découplée ? (de B, reprise)

- Condition « multi-opérateurs » plantée par opérateur latent, plus placebo de concepts.
- **H_A** : α = 1 bat α = 0, intervalle au-dessus de +1, gain nul au placebo. **H_B** : gain nul en vérité découplée.
- Falsifie : H_A réfute la circularité (A-1, C.a.1) ; H_B interdit de lire E1' comme preuve de l'« ingrédient manquant ».

### E1' — Plan factoriel distance × concept × répulsion (remplace E1 et E2)

Huit bras à **même forme fonctionnelle** : β ∈ {0, β*} ; α ∈ {0, 1} ; sélection ∈ {argmax de w par strate (g), glouton déterminantal}. Conditions : inchangée, multi-opérateurs, homonymes rares, concepts inversés ; placebos de concepts et de domaine.

- **H_A** : l'effet principal « concept » (moyenne des contrastes α) est ≥ +4 points, intervalle au-dessus de +1, **et** Δ_inversé − Δ_normal < 0 avec intervalle sous 0 (règle stricte de B § 7.2), **et** l'effet est nul au placebo de concepts et dans la condition « homonymes rares » reste ≥ +2.
- **H_B** : l'effet « concept » est ≤ +1,5 (intervalle contenant 0) ou s'effondre en « homonymes rares » : ce que « concept » apporte est la rareté de l'étiquette partagée (d1_inv : +5,3 / +4,8, RAPPORTÉ), déjà disponible.
- Issue intermédiaire : « non concluant », pas d'adoption.
- L'effet « répulsion » (glouton contre (g)) a ses propres H_A (≥ +3) / H_B (≤ +1,5) : H_B retire la machinerie déterminantale, on garde (g).
- Seuil d'adoption dans le pôle (distinct de la détection) : ×1,3 sur le stratifié **et** ≥ b_eloigne-observé − 2 dans les deux mondes de décision (illustratif) ; si b_eloigne de B s'avère un oracle, seul le premier critère reste.

### E3' — Le passage aux paires est-il nécessaire ?

- Bras sur **articles** : v6.3 (q, q rang, q ≡ 1) × noyau {cos², exp(−s/τ) à τ fixé sur calibrage}. Stratifié par nombre de champs (2 / 3 / 4).
- **H_A (nécessaire)** : aucun bras sur articles ne dépasse l'uniforme de plus de +1,5 dans les mondes à 3 et 4 champs. **H_B (non nécessaire)** : un bras sur articles atteint b_eloigne-observé − 2.
- Falsifie : H_B rend O-paires superflu ; H_A justifie le déplacement de l'ensemble de base. Les mondes à 2 champs sont rapportés à part (A-4).

### E4' — La représentation capte-t-elle le concept et non le domaine ?

Préalable à E1' (sinon E1' n'est pas interprétable). Trois mesures, chacune avec sa loi nulle par **permutation** :

1. **Relatif** : exactitude « domaine depuis k_i » ≤ exactitude « domaine depuis les opérateurs latents vrais » + 0,05 (illustratif) ; sur fiches réelles, le plafond est remplacé par deux annotateurs humains.
2. **Ordre 2** : corrélation de Mantel entre Gram C_ij et adjacence de domaine, comparée à sa loi de permutation (seuil : au-dessous du quantile 95 % de la loi nulle).
3. **Queue** : part de paires de même champ parmi les 5 % de C_ij les plus élevés (illustratif), comparée à la part de base ; H_A si l'excès est < +0,10.
4. **Jumelles** (contrôle 3 de C) : fiches à vocabulaire de domaine substitué, structure identique ; C_ij entre jumelles ≥ 0,80 (illustratif) pour R1 et pour R2 (étiqueteur tiers hors boucle, texte caviardé de ses marqueurs de domaine, scellé avant tirage).

**H_A** : les quatre passent. **H_B** : l'une échoue ; alors k_i est un proxy de domaine (ou de surface) et O-paires double son terme de domaine ; E1' n'est pas lu. Sous-test manipulation inchangé (fiches gonflées : ≤ honnêtes + 2 points), sans coupure de fréquence.

### E5 — reclassée en pilote

Non jugeable à 12 fusions par bras (A-6, C.b.4). Elle devient un **pilote de calibrage** : mesurer le taux de recevabilité (`valider_fille`, mécanique) et le bruit de fusion **par bras** (répétitions à graines différentes pour chaque bras), avec ablation q ≡ 1, bras stratifié pondéré par q et bras placebo d'éloignement ; aucune hypothèse de gain n'y est testée. Le test décisif sur fiches réelles attend un N estimé à partir du pilote (ordre de grandeur illustratif : ≈ 300 par bras pour +10 points), et une réponse à N-053 (vivier présélectionné par le juge) que ce tour ne fournit pas.

### Ordre et coût

V1 → V2 → E4' → E1' → E3' (E3' en parallèle, bon marché) → pilote E5 seulement si E1' passe. V1 à E3' : processeur seul, bibliothèque standard, de l'ordre de l'heure (illustratif ; B donne 93 s pour 4 000 mondes, RAPPORTÉ). E4' sur fiches réelles et R2 : moins d'une heure de carte ou quelques dollars d'API (illustratif), sur devis et GO chez session-depot.

---

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi (au sens des pièces).**

- VÉRIFIÉ (code, pièce A) : la forme corrigée tire des *articles* puis forme des paires ; le stratifié est le défaut depuis v0.3 ; une fiche peut figurer dans plusieurs paires stratifiées ; `k=4, max_paires=3` par défaut, différent du budget de B.
- RAPPORTÉ (pièce B, exploratoire, sans contre-lecture) : v6.3 perd −4,8 / −2,2 contre le stratifié et vaut l'uniforme ; le mécanisme est que la diagonale (q) gouverne l'ordre glouton (corrélation de rang 0,977) et que le volume d'un ensemble d'articles ne diversifie pas les *paires* ; le stratifié gagne en équilibrant les paires de domaines ; d1 gagne en évitant les moyeux ; un a priori d'éloignement grossier (b_eloigne) fait +11,9 / +6,6 sans atteindre +12 partout.
- Donc, et c'est le seul acquis mathématique commun aux deux critiques et à ma conception : **« minimiser le produit scalaire des domaines » est contenu dans « maximiser le volume », mais à un ordre de grandeur inopérant aux cosinus mesurés** ; il faut un terme à part, et ce terme doit être calibré pour être opérant (V1), sinon toute forme — la mienne comprise — reproduit le défaut de v6.3.

**Ce qui n'est pas établi.**

- Que la proximité conceptuelle graduée soit « l'ingrédient manquant » (HYPOTHÈSE). Les critiques ont montré que mon E1 le rendait vrai par construction ; la version corrigée (V2, E1') peut encore le réfuter.
- Que les deux espaces soient séparables sur des fiches réelles (HYPOTHÈSE) ; mon test initial était aveugle aux dépendances d'ordre 2 et rejetait à tort les extracteurs honnêtes ; E4' corrige, sans garantie de passer.
- Que b_eloigne soit un témoin et non un oracle (HYPOTHÈSE ; `methodes_v1.py` absent des pièces).
- Que la machinerie déterminantale ajoute quelque chose à un argmax pondéré par strate : à λ = 0 elle n'ajoute rien par construction ; sa seule justification possible est la condition de couplage, qui est une autre question.
- Le signe de la proximité conceptuelle dans le mot de Lazar (A5), à trancher avant préenregistrement.
- Tout ce qui touche la qualité des filles : E5 n'est pas jugeable à 12 fusions, et le vivier réel est déjà sélectionné par le juge.

**Objectif « commun ».** Aucun au sens du critère de lecture : B et C ont montré que ma forme O-paires dégénère ; je ne la présente plus comme forme retenue mais comme un bras. Ce qui est commun aux trois cellules, c'est le **diagnostic** (diagonale dominante, terme de distance inerte) et le **plan factoriel à même forme fonctionnelle** ; la forme reste divergente, options au format décision.

**Expérience à faire en premier : V1**, parce qu'elle conditionne toutes les autres et ne coûte rien. Processeur seul, mondes de B inchangés, graines de B. Pour chaque forme candidate (O-paires v2 ; v6.3 avec q par rang et q ≡ 1), mesurer π, la part des mondes où retirer le terme de distance change au moins une des 12 paires, et l'écart de précision associé. H_A : π ≥ 0,5 et intervalle excluant 0 — le terme est opérant, V2 peut suivre. H_B : π ≤ 0,1 — le terme est inerte, et aucune expérience sur « deux espaces » n'est interprétable tant que la forme n'a pas été rendue tranchante sur graines de calibrage. Chaque issue falsifie quelque chose : H_A réfute l'objection A-2/C-1 pour cette forme ; H_B réfute ma conception du tour III.1 telle qu'écrite. V2 vient immédiatement après, avec le placebo de concepts et la vérité plantée par opérateur latent ; si V2 rend H_B, l'idée « ingrédient manquant » est réfutée sur ces mondes avant toute dépense de carte.

FIN-DE-CELLULE