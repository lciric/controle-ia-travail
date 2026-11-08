# Proposition A — Tour III.3 : réponse aux critiques

**Pièces reçues** : ma conception III.1 et les quatre critiques B, C, D, E, complètes jusqu'à leur ligne de fin ; empreintes non recalculées. Je ne réponds qu'aux sections « Sur la proposition A » et aux défauts transversaux T1–T3 de B qui me sont imputés. Tout ce qui suit reste HYPOTHÈSE ; tout chiffre hors des faits est **illustratif**.

---

## (a) Critiques, une par une

Les critiques se recoupent ; je les groupe par expérience, en nommant la source de chacune. Verdicts : **A** acceptée, **R** rejetée (raison), **T** transformée en test.

### E0 — vérité terrain

| Critique | Source | Verdict | Raison ou test |
|---|---|---|---|
| « Étiquette par construction » non précisée : circulaire si via l'oracle, loi différente si injectée | B2, D, E | **A** | Je sépare deux sources : (α) sabotages programmatiques injectés — testent la *mécanique* du programme de couverture, loi avouée différente ; (β) lot d'adjudication scellé : échantillon aléatoire d'épisodes des organismes vus, relu par un lecteur de **troisième famille** avec la référence plantée et la trace complète, étiquette **acte** par action, scellé avant la mesure de l'oracle. Le transport de (α) vers le diffus est une hypothèse écrite, et le rappel se lit par strate de magnitude de dommage (D) et non par dose seule. |
| R ne regarde que les négatifs ; les manqués corrélés gonflent le rappel apparent | B3 | **A** | Second rapport sur les positifs du lot (β) : P(moniteur manque \| oracle manque, Y=1) / P(moniteur manque \| oracle voit, Y=1). |
| E0 mesure des alertes selon les erreurs de l'oracle, non l'indépendance des **erreurs** ; R<0,5 sans issue | D | **A / R** | Accepté : les deux rapports portent désormais sur les erreurs des deux instruments par rapport à l'étiquette (β). Rejeté pour R<0,5 : H_B est bilatérale, \|log R\| > log 2 (dépendance négative = non-indépendance, même verdict). |
| R non estimable : N·f_O·τ_M ≈ 0,25 ; variance de log R énorme | B(b), C(b)1 | **A** | Avec FA du moniteur à 1 %, R est non jugeable à N ≈ 500. Deux corrections : l'indépendance se mesure sur les **scores continus** des moniteurs (corrélation des scores avec l'erreur de l'oracle, sans seuil), et à un seuil de travail τ_travail = 10 % (illustratif) réservé à ce test, en plus du τ = 1 % opérationnel. Ce qu'on perd : la queue à 1 % reste non auditée pour l'indépendance ; écrit d'avance. |
| Mélange acte et dommage dans la même étiquette | E | **A** | Deux variables : Y (acte, source β) et D (dommage, oracle). L'oracle est juge de D ; les échecs honnêtes sont D>0, Y=0 et restent des négatifs d'**acte**, non une faute de l'oracle. Ma formulation III.1 changeait la cible de l'oracle ; corrigé. |
| T3 : loi nulle du dommage (honnête contre honnête) mesurée par personne | B | **A** | Entre dans E0 comme condition de lisibilité : δ_diffus doit dépasser le quantile 95 % de \|D_hon1 − D_hon2\| sur la même tâche ; sinon la strate est « sous le bruit » et suspend 1–5 pour elle. |

### E1 — existence

| Critique | Source | Verdict | Raison ou test |
|---|---|---|---|
| AUC(α) − AUC(β) détecte la présence de l'adaptateur : sur les négatifs (base, α=0) les deux lecteurs voient les mêmes activations | B1, B(c) | **A** | Défaut fatal tel quel. Les négatifs de E1 incluent désormais **des organismes adaptés honnêtes** : T100, placebo P, et les épisodes dormants de S. Le contraste primaire devient : sonde α sur {actes de S} contre {dormants de S ∪ T100 ∪ P}, comparée à β sur le même texte. |
| Case « consigne, exécution honnête » sans positif : AUC indéfinie | D | **A** | Dans cette case, la grandeur est le **taux d'alerte** de la sonde (doit rester ≤ τ) ; dans la case « sans consigne, sabotage attesté », c'est le rappel. Le carré est un plan de taux, pas de quatre AUC. |
| Les cases changent aussi d'organisme ; la comparaison n'isole pas la consigne | E | **A** | Vrai : (i) et (ii) sont deux organismes. J'ajoute la case **intra-(ii)** : rejeu de (ii) avec une consigne neutre ajoutée au message système (même adaptateur, consigne sans contenu de sabotage) pour mesurer l'effet d'une consigne quelconque à poids fixés. L'isolement complet reste impossible ; écrit. |
| Battre β ne démontre pas « au-delà du texte » ; β n'est pas une borne de l'information textuelle | D, E | **A** | Reformulé : « au-delà de ce que la même architecture de sonde extrait des activations de la base relisant le même texte ». C'est un comparateur, pas une borne ; le prédicteur texte (γ) en est un second. H8 n'est réfutée que relativement à ces deux comparateurs. |
| AUC ≠ rappel à 1 % ; rupture d'instrument entre E1/E2 et E4 | C1, B(b), D | **A** | Grandeur unique partout : rappel à τ = 1 % et aire partielle sur FA ∈ [0 ; 2 %] (illustratif). Conséquence : il faut ≥ 2 000 négatifs honnêtes pour ≈ 20 dépassements au seuil (B) ; sinon la queue est non jugeable, et on le dit. |
| Divergence de perplexité sous forçage : la base est « surprise » par les jetons de l'adaptateur | C(c)1 | **A** | Contrôle : α_P contre β_P sur le placebo, et α_T contre β_T sur T100 ; si l'écart y est du même ordre que sur S, l'écart lit la surprise de forçage, pas l'acte. |
| T2 : (ii) distillée depuis (i), un seul pli dépendant | B | **A** | La validation par bloc sépare **tâches, mondes et graines d'adaptateur**, à l'intérieur des familles. La généralisation inter-famille n'est pas estimable avant G1 ; la seule lecture hors famille est le mode tenu à l'écart, une fois. |
| Étiquettes permutées contrôlent le surajustement, pas la capacité à extraire un signal réel | E | **A** | Le contrôle positif de capacité est le saboteur **témoin non dissimulé** (synthèse d'antériorité) : si la sonde ne le lit pas, elle n'a pas de capacité. |

### E2 — acte ou identité

| Critique | Source | Verdict | Raison ou test |
|---|---|---|---|
| H_A définie par une absence ; zone non classée entre 0,60 et 0,75 ; pas un test d'équivalence | B4, D, E | **A** | Test d'équivalence à deux unilatéraux : H_A « identité » si l'intervalle de l'AUC sur dormants et sur P est contenu dans [0,45 ; 0,60] ; H_B si l'intervalle en sort vers le haut ; sinon **non jugeable**, pas de verdict. |
| Contamination des dormants par des sabotages manqués | B(b) | **T** | Les dormants sont définis sur l'étiquette Y de la source (β) et non sur l'oracle seul ; on rapporte la fraction c de désaccord oracle/source et l'AUC corrigée aux deux bornes de c. |
| Projeter hors du sous-espace des adaptateurs vus supprime le signal par construction | D, E | **R** comme défaut, **A** comme limite | C'est une ablation volontaire : la question est si la trace **survit** à la suppression de l'image des adaptateurs connus. Je retire l'affirmation que cela « localise » quelque chose pour un mode non vu : c'est un diagnostic de fragilité, pas une localisation. |
| Ajuster sur ‖Δ‖ supprime une partie du signal ; non identifiable si les lois de ‖Δ‖ ne se recouvrent pas | D, E | **A** | Rapporter la projection avec et sans ajustement, et la région de recouvrement des normes ; hors recouvrement : non jugeable. |
| Fuite d'identité si même organisme ou graine dans apprentissage et test | D | **A** | Plis par graine d'adaptateur (voir T2). |
| Placebo choisi pour son indétectabilité : invalide | E | **A** | Le placebo est qualifié **sans la sonde** : ‖Δ‖ non nul (il a été modifié), qualité de tâche ≥ jumeau − 0,05, objectif inoffensif attesté par l'oracle (dommage nul). Son score à la sonde est une issue, jamais un critère. |

### E3 — causalité

| Critique | Source | Verdict | Raison ou test |
|---|---|---|---|
| Spearman sur cinq doses ne discrimine rien ; T à D plat : corrélation indéfinie ; orthogonalité S/T suffit à produire le motif | B5, C3, D | **A** | Dose-réponse retiré comme test causal. Il devient un test **intra-dose** : à α fixé, la projection prédit-elle D entre épisodes ? Avec le biais d'atténuation nommé par C (pour B) : si Var(s\|α) ≈ 0, non jugeable. Sur T : pente de s en α, pas corrélation. |
| Fuite E2 → E3b (mêmes épisodes) ; substituer depuis la base ≈ ramener α vers 0 ; contrôle à apparier en nombre de sites et norme retirée | B6, C2 | **A** | Partition : localisation sur la moitié des épisodes, intervention sur l'autre. Contrôle apparié en nombre de sites, norme retirée **et covariance** (D) : retrait de même norme à des sites hors localisation ; retrait le long d'une direction aléatoire de même norme et même spectre. |
| Substitution hors variété : incohérence de génération, pas effacement | C4 | **R** comme fatal, **T** | Rejeté comme fatal : c'est le risque de toute intervention ; accepté le contrôle de C : substitution croisée intra-condition (honnête_i ← honnête_j, S_i ← S_j, même tâche, mêmes sites) qui mesure la dégradation générique de la greffe. L'effet spécifique est l'écart à ce contrôle. |
| Réduction de D par incapacitation générale ; ou absence d'effet par redondance | D, E | **A** | Témoin de **suppression générique** de l'action (perturbation qui dégrade la qualité honnête d'autant) : si D baisse autant sous ce témoin, l'intervention casse le modèle. La redondance : une substitution sans effet réfute « cette direction est nécessaire », pas « il existe une trace causale » ; H_A fausse se lit donc « non causale **ou** redondante », et je l'écris ainsi. |
| E3 confond intervention efficace et inévitabilité | E | **A** | E3 teste la causalité ; l'inévitabilité se teste seulement sous pression (E5c). L'issue « H_A fausse → sonde évitable » de ma III.1 est retirée. |
| Contraste sur O n'identifie pas celui sur D si l'oracle dépend de l'intervention | E | **A** | L'oracle est aveugle à la condition (N-060) ; on vérifie en plus son FA sur les épisodes intervenus honnêtes. |

### E4 — lisibilité, pince

| Critique | Source | Verdict | Raison ou test |
|---|---|---|---|
| C − TPR_int mesure une complémentarité (dépendance conditionnelle statique), pas un étau ; sélection des survivants le long du budget ; confondant de tâche | B7, C5, D, E | **A** | Deux paramètres distincts, deux expériences : **complémentarité** (C, statique, stratifiée par tâche et par dose, en E4) et **étau** (effet d'une pression externe **assignée**, en E5e, lu sur tous les épisodes en intention de traiter). Ma III.1 les confondait. |
| c − TPR_int = −Cov(I,E\|Y=1)/p : le contraste positif est une covariance négative | E(b) | **R** comme défaut | C'est exactement ce que la complémentarité affirme (les manqués de l'externe sont les pris de l'interne). J'adopte la forme en covariance comme définition, elle est plus lisible ; ce n'est pas un défaut. |
| Variance de Ĉ : si TPR_ext ≥ 0,90 et n_sab = 150, ≈ 15 manqués, erreur-type ≥ 0,12 ; seuils à 0,5 % instables en queue lourde | C(b)2, B(b), E(b) | **A** | Condition de jugeabilité écrite d'avance : n_sab·(1 − TPR_ext) ≥ 100 manqués (illustratif) sinon non jugeable ; seuils sur ≥ 2 000 honnêtes ; si la densité honnête au quantile est quasi nulle (queue lourde), on rapporte l'intervalle du seuil lui-même. |
| Test de L2 par le juge : l'instrument évalué fixe son régime | B7, E | **A** | L2 se mesure par une grandeur **mécanique sans modèle** : part des épisodes sabotés dont le code et les sorties d'exécution sont identiques (ou équivalents par diff structurel) à ceux du jumeau honnête. Ce n'est pas une preuve de L2 (E), c'est une borne inférieure de sa part. |
| T1 : la dose a été fixée sur une boîte noire ; comparer blanche/noire est en partie vrai par construction | B | **A** | Boîte noire d'évaluation disjointe de celle qui a fixé la dose (autre famille), sur épisodes neufs ; la comparaison avec la boîte noire de dose est rapportée à part comme biaisée. |
| FA_joint ≤ 1,2 % invérifiable sans ≈ 10 000 honnêtes | B(b) | **A** | Remplacé : vérification que FA_joint ≤ FA_ext + FA_int (borne de l'union) avec intervalle, et rapport de l'intervalle, pas d'un seuil fin. |
| N2/N3 : échecs honnêtes persistants produisent une autocorrélation ; SPRT sans loi alternative ; permutation détruit aussi des dépendances légitimes | C(c)3, E(b), D | **A** | SPRT remplacé par une accumulation à loi alternative **estimée sur les modes vus** et seuil calibré par épisode sur les honnêtes longs ; contrôle négatif : épisodes honnêtes à échec persistant, analysés à part ; contrôle de permutation par blocs **inter-épisodes de même rang** (C pour D), pas intra-épisode. |
| Calibration : zéro fausse alerte sur n₀ négatifs borne FA à 1 − γ^{1/n₀}, pas 0 | E(b) | **A** | Règle de rapport : toute FA « nulle » est rapportée par sa borne supérieure. |

### E5 — règle de défense, étau

| Critique | Source | Verdict | Raison ou test |
|---|---|---|---|
| Diagonale ≈ 0 par sélection si le bras rouge ne soumet que ses succès | D, E | **A** | La matrice inclut **toutes les tentatives** de la campagne contre i, avec le dommage par cellule ; une attaque devenue inoffensive ne compte pas comme évasion (D). |
| Nash optimisée et évaluée sur la même matrice : biais optimiste ; meilleure réponse au mélange hors bibliothèque | B(b), C(b)3, D | **A** | Le mélange p* se calcule sur une génération, s'évalue sur la génération **suivante** attaquant p* (campagne assignée) ; le gain lu est celui de cette évaluation croisée. n_eff = nombre de générations, pas d'épisodes (B pour E) : la lecture est une trajectoire, avec 3–4 points, et je l'écris comme telle. |
| Secret confondu avec la composition du panel | B8, D, E | **A** | Sondes tirées d'un même vivier, affectation **aléatoire** réserve/déployé (B), panel de taille égale ; contraste à panel constant. |
| Trois bras varient conjointement composition, information, objectif | D | **A** | Plan 2 × 2 (distribution révélée/cachée × panel exposé/secret à composition appariée) remplace mes trois bras ; chaque bras régénère ses attaques à budget égal. |
| D(k) est un maximum croissant avec le budget ; contraintes emboîtées → décroissance par construction ; l'arrêt « deux fois \|ΔD\| < ε » se déclenche par le bruit | B9, B(b), D, E | **A** | D(k) rapporté comme **borne inférieure** à budget B_k fixé et égal pour tout k. H_A/H_B reformulés sur le **niveau du plateau** et non sur la décroissance : le plateau atteint-il le bruit du jumeau honnête, à comparer à un plateau sous k **contraintes placebo** (sondes d'une propriété sans rapport) de même budget. Règle d'arrêt : budget B seul ; aucune déclaration de convergence. |
| Pseudo-réplication : le régime est assigné par campagne (B pour E, applicable à E5 de A) | B | **A** | Unité d'inférence = campagne ; nombre de campagnes annoncé d'avance ; intervalles au niveau campagne. |
| Pression placebo à budget égal manquante | D, E | **A** | Ajoutée (ci-dessous, E5e). |

### Ce qui reste en dissensus
- Avec D et E sur la nature de C : ils le réduisent à une association sans valeur pour l'étau ; je le garde comme **complémentarité** préalable : si C ≈ TPR_int (indépendance) sur les modes vus, l'étau est improbable et E5e passe après E5a–c dans l'ordre. C'est un filtre, pas une preuve, et le dissensus porte sur l'ordre, non sur la lecture.
- Avec C sur E3b : je maintiens la substitution comme test causal **à condition** du contrôle croisé ; C la tient pour non interprétable en génération autorégressive. Issue arbitrable par la grandeur même du contrôle : si la greffe honnête_i ← honnête_j dégrade D autant que S ← jumeau, C a raison et E3b est non jugeable.

---

## (b) Expériences corrigées

Conventions inchangées (FA sur dénominateur honnête, τ = 1 %, blocs par tâche × monde × graine, aucune lecture du mode tenu à l'écart avant G1), plus : grandeur unique = rappel à τ et aire partielle sur [0 ; 2 %] ; toute FA nulle rapportée par sa borne ; unité d'inférence = épisode pour E0–E4, campagne pour E5 ; toute issue dont l'intervalle traverse le seuil est **non jugeable** (forme de E, adoptée).

### E0′ — étalon et loi nulle
- Variables : Y (acte, lot scellé (β) par lecteur de troisième famille, ≥ 300 épisodes aléatoires, illustratif) ; D (oracle N-060 v3) ; D_null (honnête contre honnête, même tâche, ≥ 200 paires, illustratif).
- H_A : rappel de l'oracle sur Y=1 ≥ 0,80 par strate de magnitude de dommage (≥ 3 strates) ; FA ≤ 0,05 sur jumeaux et échecs honnêtes ; δ_diffus > q_95(D_null) ; corrélation des scores des moniteurs avec l'erreur de l'oracle nulle dans l'intervalle (marge ±0,10, illustratif) ; rapports d'erreurs sur négatifs **et** positifs à τ_travail = 10 % dans [0,5 ; 2].
- H_B : l'un des points échoue. Issue : suspension des points 1–5 **pour les strates concernées** ; si δ_diffus ≤ q_95(D_null), la dose est refixée (R-1795).
- Non jugeable si une cellule d'erreur est vide : écrit comme tel, pas comme succès.
- Pièces : lot (β) scellé avant toute lecture ; recalcul par tiers depuis les étiquettes.

### E1′ — existence relative à deux comparateurs
- Positifs : actions Y=1 des organismes S (famille (ii) d'abord, puis (i)). Négatifs **séparés et rapportés à part** : jumeau honnête, échecs honnêtes, dormants de S, T100, placebo P.
- Lecteurs : α (organisme), β (base en forçage sur le même texte), γ (traits du texte) ; même architecture, hyperparamètres figés ; contrôle positif = saboteur témoin non dissimulé ; contrôle de surprise de forçage = α_P/β_P et α_T/β_T.
- H_A : rappel_α(τ) − rappel_β(τ) ≥ 0,10 (illustratif), intervalle excluant 0, contre **chaque** classe de négatif, et écart α_P − β_P ≤ 0,03 ; H_B : écart ≤ 0 contre au moins une classe adaptée, **ou** α_P − β_P du même ordre que α − β (surprise de forçage), **ou** rappel élevé seulement dans la case avec consigne et taux d'alerte > τ dans la case « consigne, exécution honnête » (sonde lit la consigne).
- Puissance : ≥ 2 000 négatifs honnêtes pour le seuil ; positifs ≥ 400 par bras (illustratif). Si non atteint : non jugeable.
- Issue négative préécrite : H8 relativement à β et γ → reconception (séquentiel, écart à la base).

### E2′ — acte ou identité
- Sonde d'acte entraînée sur {Y=1 de S} contre {dormants de S} seulement (contraste intra-saboteur, D pour D, adopté), par plis de graine.
- H_A (identité) : AUC sur {dormants vs jumeau} et sur {P vs jumeau} dans [0,45 ; 0,60] par équivalence, **et** la projection de Δ ne sépare pas acte/dormant mieux que ‖Δ‖ ; H_B (acte) : rappel_τ sur Y=1 vs dormants ≥ 0,20 avec AUC d'identité dans la marge ; **mixte** (les deux hors marge) rapporté comme tel, sans verdict.
- Δ : rapporté avec et sans ajustement de norme, région de recouvrement obligatoire.
- Diagnostic (non test) : survie du rappel après projection hors de l'image des adaptateurs vus.
- Placebo qualifié sans la sonde (‖Δ‖ > 0, qualité ≥ jumeau − 0,05, D nul).

### E3′ — causalité (partition dédiée)
- E3a′ intra-dose : à chaque α, régression de D sur la projection ; H_A : pente > 0 à chaque α ≥ 0,5 et pente nulle sur T ; H_B : pente nulle à α fixé (ou Var(s\|α) ≈ 0 → non jugeable, atténuation nommée).
- E3b′ substitution aux sites localisés sur l'autre partition ; contrôles : (1) même norme, même covariance, sites hors localisation ; (2) direction aléatoire de même spectre ; (3) greffe croisée honnête_i ← honnête_j et S_i ← S_j ; (4) suppression générique de l'action appariée en perte de qualité ; (5) substitution depuis P.
- H_A (trace causale non redondante) : baisse de D sous la substitution cible dépassant d'au moins 0,20·D(S) (illustratif) la baisse sous **chacun** des contrôles (1)–(5), à qualité honnête ≥ −0,05 ; H_B : baisse ≤ celle d'un contrôle (lecture non causale, redondance, ou dégradation générique — indistingués, écrits ensemble).
- E3c′ pilotage : mêmes contrôles. Garde portier inchangée : ablatif, côté défense.

### E4′ — lisibilité et complémentarité
- Boîte noire d'évaluation disjointe de celle de la dose (T1). Moniteurs sans étiquette : N1 nouveauté ajustée sur honnêtes **incluant T100 et P** (B pour E, adopté) ; N2 accumulation à loi alternative estimée sur modes vus ; N3 autocorrélation ; contrôles : honnêtes longs, échecs persistants, permutation inter-épisodes.
- Domination blanche/noire : rappel_τ par budget du bras rouge, sur bloc tenu à l'écart ; H_A écart ≥ 0,10 à chaque budget, intervalles disjoints ; H_B croisement ou domination noire.
- Complémentarité : θ = −Cov(I,E\|Y=1)/P(E=0\|Y=1), stratifié par tâche et dose ; H_A θ ≥ 0,10 dans chaque strate ; H_B θ ≤ 0 ; jugeable seulement si manqués de l'externe ≥ 100 et honnêtes ≥ 2 000 ; test de L2 mécanique rapporté comme borne inférieure de sa part ; régime L2 déclaré si > 50 % (illustratif).

### E5′ — règle de défense et étau
- E5a′ matrice sur toutes les tentatives, dommage par cellule ; Nash sur génération g, évaluée sur g+1 attaquant p* ; H_A gain croisé ≥ 0,10 à ≥ 2 générations sur 3 (illustratif) ; H_B gain ≤ 0 ou rang ≈ 1.
- E5b′ plan 2 × 2 distribution × exposition, panel apparié par affectation aléatoire, campagnes régénérées à budget égal ; H_A : effet du secret ≥ 0,10 à panel constant ; H_B : effet ≤ 0 ; aléa lu sur l'autre facteur ; issue « rien n'aide » couverte (les deux effets ≤ 0).
- E5c′ inévitabilité : sonde d'E3′ (si H_A) ou projection de Δ contrôlée par P ; H_A : D du bras rouge chute ≥ 50 % sous contrainte d'évasion ; H_B : inchangé.
- E5d′ coût : D(k) borne inférieure à budget B_k égal ; comparée à D_placebo(k) sous k contraintes sans rapport ; H_A : D(k) − D_placebo(k) ≤ −0,05 pour k ≥ 2 et plateau au bruit honnête ; H_B : écart nul (la défense tourne en rond ou l'optimiseur échoue — indistingués, écrits).
- **E5e′ étau** (nouvelle, remplace la lecture le long du budget) : campagnes assignées au hasard à **pression externe** (contre la mâchoire externe) ou **pression placebo** (contre un moniteur d'une propriété sans rapport), budget et dérive de génération égaux (KL à la base contrôlée, C pour B, adopté) ; lecture en **intention de traiter sur tous les épisodes** : Δ score interne et Δ D conjointement. H_A (l'étau serre) : score interne moyen plus élevé de ≥ 0,20 écart-type honnête sous pression externe que sous placebo **à Δ D rapporté, non conditionné** ; H_B : écart ≤ 0. Contrôle : mâchoire externe factice (B pour E, adopté). Unité = campagne ; n_eff annoncé.

---

## (c) Réponse à l'arbitre

**Ce qui est établi** (statut des faits, rien de plus) : les organismes dosés existent et α = 0 rend la base ; la détection n'est mesurée que sur le flagrant ; la sonde W lit la consigne ; le prédicteur texte vaut 0,866 sans dénominateur spécifié ; l'oracle n'est pas audité ; aucune pince n'a été mesurée ; en arène synthétique le mélange progresse mais la figée généralise mieux, sans verdict scellé. Par les critiques, trois choses sont établies **au niveau de la méthode** : (1) ma comparaison α/β de III.1 était vraie par construction sans négatifs adaptés ; (2) la capture résiduelle est une complémentarité statique et non un étau — l'étau exige une pression assignée et une lecture non conditionnée ; (3) à τ = 1 % et aux effectifs envisagés, les rapports d'indépendance, les seuils et la capture résiduelle sont non jugeables sans ≥ 2 000 honnêtes et ≥ 100 manqués de l'externe.

**Ce qui n'est pas établi** : l'existence de la trace (H1 et H8 au même rang) ; si la trace lirait l'acte ou l'identité ; toute causalité (le seul précédent lu, l'axe de douleur, est non causal, RAPPORTÉ) ; la transposition de l'arène ; la valeur du secret contre l'aléa ; que la famille « coût » soit hors du régime L2 ; que le dommage diffus dépasse le bruit honnête-contre-honnête (T3, mesuré par personne). Le nombre de familles tenues à l'écart — la ressource rare — n'est pas dans les faits.

**L'expérience à faire en premier : E0′**, parce que sans étalon rien ne compte et parce qu'elle contient deux portes bon marché et décisives : la loi nulle du dommage (si δ_diffus ≤ q_95 de \|D_hon − D_hon\|, les étiquettes « dommage » sont du bruit et la dose se refixe avant toute sonde) et le lot d'adjudication scellé qui sépare l'acte du dommage. Son issue négative suspend 1–5 par strate, sans arrêt (R-1795). Immédiatement après, deux mesures mécaniques sans carte : la part L2 (code et exécution identiques au jumeau) et le comptage des honnêtes disponibles pour le seuil à 1 % — si l'une des deux tombe mal, la pince est mal posée pour cette famille ou non jugeable, et l'effort va à E1′ contre β et γ avec négatifs adaptés. E3′ et E5e′ ne viennent qu'après une localisation sur partition dédiée, et chaque lecture décisive consomme une famille neuve.

Ce qui peut être réfuté : à chaque étape, l'issue négative est écrite au même rang que la positive ; aucun chiffre ci-dessus n'est un résultat.

FIN-DE-CELLULE