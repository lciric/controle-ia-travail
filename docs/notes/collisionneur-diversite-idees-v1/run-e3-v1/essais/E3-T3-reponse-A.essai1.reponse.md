# Proposition A — Tour III.3 : réponse aux critiques

## 0. Pièces reçues

Critiques visant A reçues de B, D et E ; toutes lisibles. La pièce E3-T2-critique-croisee-C est absente (statut REFUS) ; je n'en suppose rien. Tout ce qui suit est HYPOTHÈSE de conception, sauf mention contraire ; les nombres sont illustratifs sauf s'ils viennent des FAITS.

Trois critiques reviennent chez B, D et E à la fois et pèsent plus lourd que les autres : (i) D_oracle, présenté comme étalon, n'était pas validé et sa « détectabilité » était calculée hors archive ; (ii) la distance moyenne de Jensen-Shannon efface une différence confinée à une région rare (d_JS ≤ r(A)·ln 2, borne donnée par D ; même argument chez B et E) ; (iii) plusieurs duels (E1, E3, E4, E5) n'opposaient pas des issues exhaustives et exclusives. Je les accepte toutes trois et elles structurent les corrections.

## (a) Réponses critique par critique

| # | Critique (source) | Décision | Suite |
|---|---|---|---|
| 1 | M1 : recombinaisons du nul recalculées ou conservées ? confondu avec la taille du nul (B-a1) | Acceptée | Règle fixée : recombinaisons recalculées sur l'archive réduite. E2′ juge les mêmes fiches contre trois nuls hors ligne (CPU, aucun appel), ce qui sépare les deux sources |
| 2 | D_oracle vaut 1 sur les mondes simples ; dilution de E1 non protégée (B-a2) | Acceptée | Composition des 50 mondes stratifiée et préenregistrée par nombre k de composantes détectables ; E1′ ne compte que les mondes k ≥ 3, effectif minimal gelé |
| 3 | E3 confond famille et décodage (B-a3, B-c2) | Transformée en test | Bras intermédiaires ajoutés : même modèle, consignes système permutées ; même modèle, deux températures |
| 4 | Le tirage au sort du représentant crée un bruit ; un représentant faible pourrait échouer au test de mort (B-a4) | Rejetée sur un point, acceptée sur l'autre | Dans M1, le regroupement opère **après** le test de mort : tout membre d'un groupe l'a déjà passé ; l'objection « échec au test de mort » ne s'applique pas. En revanche la variance du choix sur l'archive suivante est réelle : E2′ compare tirage scellé et règle canonique déterministe, et mesure la variance de D_oracle de l'archive sur 10 graines de tirage (CPU seulement, pas de nouveaux appels) |
| 5 | M2 et M2+M6 jamais préenregistrés comme bras ; rejouer E4 après lecture viole R1 (B-a5) | Acceptée | E4′ a trois bras scellés d'avance : vue neutre, M2, M2+M6 |
| 6 | Composantes colinéaires : neutralisation non propre, D_oracle surestime (B-b1, B-c1 ; D-a2, D-b ; E-a1, E-b) | Acceptée | Contrôle de séparabilité à la génération du monde ; composantes non séparables fusionnées avant la course ; contrôle négatif « composantes fictives / décompositions équivalentes » dans E0 |
| 7 | JSD moyenne diluée par la masse de la région où les lois diffèrent (B-b2 ; D-b ; E-b) | Acceptée | D_contenu v2 : distance = maximum sur des strates préenregistrées de la JSD moyenne intra-strate, strates à effectif égal, plus un diamètre en log-rapport (voir b) |
| 8 | E5 non jugeable si la détection séquentielle n'est pas monotone (B-b3 ; D-a5 ; E-a2) | Acceptée | Détectabilité **conditionnelle** à l'archive de la génération t, recalculée par l'orchestrateur après chaque sélection scellée |
| 9 | Biais vers les lois courtes dans le tirage (B-c3) | Rejetée | Le tirage est uniforme sur les membres du groupe sous graine scellée, pas par empreinte ; aucune dépendance à la longueur par construction. La corrélation rang/longueur est toutefois rapportée (coût nul) |
| 10 | E1 ne sépare pas monde et proposeurs ; les deux hypothèses peuvent être vraies ensemble ; instrument et mondes du même dispositif (D-a1 ; E-a5) | Acceptée | E1′ mesure un **rapport** entre couverture brute et couverture offerte, avec contraste k = 1 contre k ≥ 3 sur les mêmes proposeurs ; issues exhaustives |
| 11 | Chute relative instable quand le gain est petit (D-a3 ; E-b) | Acceptée | Critère absolu : chute ≥ κ·Δ_c où Δ_c est la chute de la loi plantée elle-même ; plancher de gain g_min |
| 12 | Calibration/évaluation de τ non closes (D-a4) | Acceptée | Mondes pilotes disjoints des 50, scindés en calibration et validation, préenregistrés |
| 13 | E3 : issues non exhaustives ; Kimi pas établi « moins cher » (D-a5) | Acceptée | Trois issues (au-dessus, dans, au-dessous du plancher) ; coût par appel mesuré au pilote A/A, pas déduit du total v67 |
| 14 | E5 : le calage peut venir du juge, du test de mort, du hasard (D-a5 ; E-a5) | Transformée en test | Attribution par sentinelle : à la génération de calage, la fiche-sentinelle de chaque composante non couverte est jugée contre le nul courant, hors course ; si elle passe, le calage est aux proposeurs ; sinon à la puissance |
| 15 | Zéro copie promue sur petit banc ne borne rien (D-a6 ; E-c) | Acceptée | Taux avec intervalle de Clopper-Pearson ; n préenregistré pour que la borne supérieure à 95 % tombe sous la tolérance (illustratif : n ≥ 60 pour 5 %) |
| 16 | M6 ne ferme que les morceaux sur grille (D-a6, D-c ; E-c) | Acceptée | Portée de M6 réécrite : couverture de la classe « deux morceaux, seuils sur grille, paires d'archive » ; les attaques hors grille, produits, compositions sont jouées et leur taux de brèche **rapporté**, sans revendication de fermeture |
| 17 | Monde global sans signal résiduel sur toute la chaîne (D-c) | Acceptée | Mondes k = 1 courus sur trois générations avec le calendrier M1 : promotions en génération ≥ 2 comptées comme fausses alertes de chaîne |
| 18 | Détectabilité ≠ promotion de la loi complète ; approximation 200·δ injustifiée (E-a2, E-b ; D-b) | Acceptée | L'approximation est retirée. Détectabilité = taux empirique de promotion d'une sentinelle « meilleure loi d'archive + c » sur R réplications de 200 tirages, contre le nul réel |
| 19 | Le nul réduit change la définition d'une copie ; distinguer compression de la vue, du comptage, du nul (E-a3, E-c) | Acceptée, décisive | E2′ sépare les trois compressions ; **toutes** les sœurs écartées sont réinjectées contre le nul réduit. Une sœur réadmise signe un groupe mal formé : c'est la validation de τ, pas un accident |
| 20 | Calibrer τ sur le refus du juge produit un instrument de proximité au juge ; compatibilité N-053/N-058 à examiner (E-a4) | Partiellement rejetée | N-053 interdit un score de juge dans un signal d'entraînement ou de sélection d'un agent ; D_contenu n'est jamais servi, jamais optimisé, et M4 n'alloue le budget que sur D_oracle (N-058). Mais la remarque sur ce que mesure τ est juste : deux seuils sont calibrés, τ_juge (prédit le refus) et τ_oracle (prédit l'identité des ensembles de couverture) ; leur accord est mesuré ; en course on prend le plus strict (moins de fusions) |
| 21 | E4 : gain utile et exploitation peuvent croître ensemble (E-a5) | Acceptée | Table de décision jointe sur (ΔD_oracle, Δfausses promotions), préenregistrée |
| 22 | Ablation modifiant la marginale de Y crédite une loi qui ignore c (E-b, E-c) | Acceptée | Contrôle de fausse couverture : lois construites par l'orchestrateur sans dépendance à c ; seuil de fausse couverture ≤ 0,05 (illustratif) sur mondes de validation |
| 23 | Faible JSD ne borne pas le regret logarithmique près de zéro (E-b) | Acceptée | Diamètre en log-rapport ajouté à D_contenu (voir b) |
| 24 | Règle d'inférence : intervalle traversant le seuil = indécis (E, préambule) | Acceptée | Adoptée pour tous les duels ; une issue indécise est rapportée comme telle et son coût compté |

Deux rejets méritent un mot. Sur le point 4, la critique de B repose sur un ordre des opérations qui n'est pas celui de M1 : je regroupe les lois **promues et survivantes** ; la perte possible est sur l'archive suivante, pas sur le test de mort. Sur le point 20, je maintiens que calibrer τ sur le refus du juge est voulu : dans cet organisme, « copie » est défini opérationnellement par la garde contre les copies ; mais j'accepte que ce ne soit pas la seule définition, d'où le second seuil.

## (b) Expériences corrigées

### Instruments v2 (préenregistrés avant la génération des 50 mondes)

**D_oracle v2.**
- À la génération d'un monde w, la loi plantée est écrite comme composition de composantes C_w. Contrôle de séparabilité par simulation : pour tout c ≠ c′, JS(p*, p*_{−c}) ≥ ε_sep et JS(p*_{−c}, p*_{−c′}) ≥ ε_sep (illustratif ε_sep = 0,01 nat). Les composantes qui échouent sont fusionnées en une seule avant toute course ; deux décompositions donnant la même loi sont comptées une fois.
- Détectabilité conditionnelle : à la génération t, pour chaque c non couverte, l'orchestrateur écrit la sentinelle « meilleure loi de l'archive t + c » (jamais servie) et la juge contre le nul réel de t sur R réplications de 200 tirages (illustratif R = 50) ; détectable_t(c) si promue dans ≥ 80 % des réplications. Aucune formule en 200·δ.
- Couverture : ℓ couvre c si G_w(ℓ) ≥ g_min **et** A_c(ℓ) = [G_w(ℓ) − G_{w∖c}(ℓ)] ≥ κ·A_c(p*), chaque gain mesuré contre la marginale de son propre monde (formule d'E). Illustratif : κ = 0,5, g_min = seuil du test de mort (0,02 nat, RAPPORTÉ).
- Contrôles négatifs obligatoires (mondes de validation) : composantes fictives (neutralisation sans effet sur p*) → couverture nulle ; décompositions équivalentes → même D_oracle ; lois sans dépendance à c → fausse couverture ≤ 0,05.

**D_contenu v2.**
- Strates préenregistrées : sous-population × cellules de quantiles de chaque trait (illustratif : 2 × 4 × 4 = 32), X à effectif égal par strate, tiré de la description publique des traits.
- d(ℓ, ℓ′) = max sur les strates de la JSD moyenne intra-strate ; diamètre supplémentaire D_log(ℓ, ℓ′) = max sur X et sur les issues de |log ℓ − log ℓ′|. Deux fiches ne sont candidates au même groupe que si d ≤ τ **et** D_log ≤ λ. Lien complet.
- τ_juge et τ_oracle calibrés sur les mondes pilotes de calibration ; détection et fausse alerte estimées sur les mondes pilotes de validation, avec les paires difficiles : différence confinée à une strate rare, probabilités proches de zéro, même forme et mêmes traits.

### E0 — Étalonnage des instruments (mondes pilotes, hors des 50 ; aucune décision sur l'organisme)
- Mondes pilotes neufs sous devis (illustratif : 20, scindés 10 calibration / 10 validation), lois écrites par programme.
- H_A : D_oracle v2 passe ses trois contrôles négatifs et D_contenu v2 atteint détection ≥ 0,9 et fausse alerte ≤ 0,1 sur la validation, y compris sur les paires difficiles. H_B : l'un des seuils est manqué.
- Si H_A est falsifiée, E1′ à E5′ ne sont pas lancées : l'instrument est renvoyé en conception. Si H_B est falsifiée, les seuils sont gelés.

### Pilote A/A (10 mondes des 50, même modèle, même vue, deux graines)
Plancher de bruit pour toutes les différences de D_oracle ; coût par appel de proposeur mesuré ici (le total v67 ne l'isole pas, RAPPORTÉ). Remarque de D acceptée : A/A borne le bruit, pas un biais commun ; le biais commun est traité par les contrôles négatifs de E0.

### E1′ — Le monde offre-t-il, et les proposeurs prennent-ils ?
- Composition préenregistrée des 50 mondes : ≥ 20 à k ≥ 3 composantes détectables à t = 0, ≥ 10 à k = 1 (illustratif).
- Métrique : ρ_w = (composantes détectables_0 distinctes couvertes par les propositions **brutes** de génération 1) / k_w, sur les mondes k ≥ 3.
- H_A (la redondance de v67 était un fait du monde) : médiane de ρ ≥ θ. H_B (fait des proposeurs et de la vue partagée) : médiane de ρ < θ. Illustratif θ = 0,5 ; intervalle de confiance préenregistré sur la médiane ; intervalle entièrement d'un côté falsifie l'autre hypothèse ; intervalle traversant θ = indécis, rapporté comme tel.
- Contraste apparié : mêmes proposeurs sur les mondes k = 1 (ρ attendu = 1 sous les deux hypothèses ; ρ > 1 invalide l'instrument).
- Conséquence : H_B falsifiée → M2–M4 secondaires, dépense portée sur M5 + M1 ; H_A falsifiée → M2–M4 nécessaires, E4′ et E3′ prioritaires.

### E2′ — Compression de la vue, du comptage, du nul (E-a3 ; B-a1)
- Génération 1 : jugement comme en v67, test de mort, regroupement des survivantes.
- Génération 2 : deux conditions de **vue** (archive complète / un représentant par groupe) — ce sont les seuls appels de modèle. Les fiches de génération 2 sont ensuite jugées hors ligne (CPU) contre trois **nuls** : (N1) archive complète + recombinaisons ; (N2) représentants + recombinaisons recalculées sur les représentants ; (N3) représentants + recombinaisons de toutes les sœurs. Nul officiel scellé : N2 ; N1 et N3 sont diagnostiques, aucune promotion n'en découle.
- Attaques : copies renommées des représentants (contrôle de v67) ; copies renommées de **toutes** les sœurs écartées ; réinjection directe de toutes les sœurs écartées, contre N2.
- H_A : taux de réadmission des sœurs et de leurs copies sous la tolérance ω (illustratif 5 %), borne de Clopper-Pearson comprise, **et** ΔD_oracle entre archives complète et compressée dans le plancher A/A. H_B : l'une des deux conditions échoue. Une sœur réadmise contre N2 signe un groupe mal formé : τ est alors resserré **avant** toute course décisive suivante, sous nom neuf (R12).
- Variance du représentant : D_oracle de l'archive compressée sur 10 graines de tirage, et sous règle canonique déterministe ; CPU seulement. Si l'écart dépasse le plancher A/A, la règle canonique remplace le tirage.
- Mondes k = 1 courus trois générations sous N2 : promotions en génération ≥ 2 = fausses alertes de chaîne, comparées au niveau BH (D-c).

### E3′ — Deux fournisseurs ou N tirages d'un seul (N-045)
- Bras, à coût en dollars apparié sur le coût par appel mesuré au pilote : (K+A) ; (K × N, même décodage) ; (K × N, consignes système permutées) ; (K × N, deux températures) ; A/A K vs K.
- H_A : D_oracle de (K+A) ne dépasse pas, au-delà du plancher, le meilleur des bras à un seul modèle. H_B : il le dépasse. Issues exhaustives : au-dessus du plancher → H_A falsifiée ; dans ou au-dessous → H_B falsifiée (et « au-dessous » est rapporté : le second fournisseur coûte sans apporter). La différence entre les bras « décodage » et « consignes permutées » attribue un éventuel gain à la variance de décodage plutôt qu'à la famille.
- Lisible seulement si les lois des mondes sont écrites par programme ou par une famille étrangère aux deux proposeurs (question posée au directeur, RAPPORTÉ).

### E4′ — Rôles par forme et angle mort du juge
- Trois bras scellés : vue neutre ; M2 ; M2 + M6.
- Table de décision préenregistrée sur (ΔD_oracle vs neutre, Δ taux de fausses promotions oracle vs neutre), les deux mesurés contre le plancher A/A :
  - ΔD > plancher et Δfausses ≤ plancher → H_B (les rôles ouvrent la brèche) falsifiée ; M2 admissible.
  - Δfausses > plancher, quel que soit ΔD → H_A falsifiée ; M2 inadmissible seul ; le bras M2+M6 dit si l'extension du nul ramène Δfausses au plancher et ce qu'elle coûte en D_oracle.
  - ΔD ≤ plancher et Δfausses ≤ plancher → M2 est du budget, pas une idée.
- Contrôles : mondes k = 0 (p* = K1) sous les trois bras ; interactions vraies de forme `si_sinon` écrites par l'orchestrateur et jouées contre M6 (taux de faux rejets) ; attaques hors grille, produits et compositions contre M6 : taux de brèche **rapporté**, aucune fermeture revendiquée.

### E5′ — La chaîne cale-t-elle sur la puissance ou sur les proposeurs ?
- Même course multi-générations que E2′ (aucun appel supplémentaire). À la génération de première sélection vide, l'orchestrateur juge hors course la sentinelle de chaque composante non couverte contre le nul courant.
- H_A (calage de puissance) : médiane, sur les mondes k ≥ 3, du nombre de sentinelles promues = 0. H_B (calage de proposeurs) : médiane ≥ 1. Intervalle de confiance sur la médiane ; indécis si traversant.
- Contrôle : mondes k = 1, calage attendu en génération 2 avec 0 sentinelle promue.

### Ordre et coût
Scellement des consignes, rôles, strates, κ, g_min → mondes pilotes → E0 → génération des 50 mondes et de leurs composantes → préenregistrement E1′–E5′ → pilote A/A → E1′, E2′ et E5′ sur une même course de trois générations → E4′ → E3′ → lecteur neuf (R13). Calcul : CPU, négligeable devant les 0,27 USD de machine de v67 (RAPPORTÉ). Appels : illustratif, 50 mondes × 2 proposeurs × 3 générations × 2 conditions de vue ≈ 600 appels pour E1′/E2′/E5′ ; E3′ et E4′ ajoutent de l'ordre de la moitié chacun ; le coût unitaire vient du pilote A/A. Tout sous devis et accord du directeur.

## (c) Réponse à l'arbitre

**Ce qui est établi (RAPPORTÉ par le verdict v67).** La chaîne garde contre les copies dans la classe couverte, sur S-V1, à cette taille (C1). Les onze lois de la génération 1 sont des variantes d'un même constat, ajouter z1, que K1 ignorait ; la génération 2 n'a rien promu ; le verdict lui-même dit que ni l'un ni l'autre ne mesure la diversité ni la capacité à progresser. Le juge cède hors de sa classe de recombinaisons (A1-v3, 24/24 sur un autre monde). Les réponses brutes des proposeurs n'ont pas été gardées (R-2). Voilà tout ce qu'on sait.

**Ce qui n'est pas établi.** Que la redondance vienne des proposeurs plutôt que du monde : S-V1 n'offrait peut-être qu'un seul constat, et onze proposeurs indépendants l'auraient tous trouvé. Que « 11 puis 0 » soit un effondrement : c'est pour partie un artefact du calendrier de jugement (chaque fiche jugée contre la génération précédente, pas contre ses contemporaines). Que deux fournisseurs valent mieux que N tirages d'un seul. Qu'une pression vers la variété de forme n'ouvre pas l'angle mort du juge : `si_sinon` et `melange` sont précisément les outils des recombinaisons par morceaux. Que mes propres instruments de mesure tiennent : les critiques croisées ont montré que D_oracle, tel que proposé au tour III.1, pouvait inventer ou effacer des composantes (colinéarité, ablation changeant la marginale, détectabilité calculée hors archive), et que la JSD moyenne efface une différence confinée à une région rare. Les versions v2 ci-dessus corrigent ces points sur le papier ; elles ne sont pas validées.

**Ce que je retiens des critiques pour la conception.** Trois décisions de principe : (1) séparer la compression de la vue, du comptage et du nul, et réinjecter toutes les sœurs écartées contre le nul réduit — une sœur réadmise est la preuve qu'un groupe était mal formé ; (2) définir la détectabilité conditionnellement à l'archive de chaque génération, par promotion empirique d'une sentinelle, sans formule analytique ; (3) préenregistrer chaque bras, y compris M2+M6, avant toute lecture, et accepter une issue « indécise » plutôt que de la forcer.

**Risques qui subsistent.** Goodhart : D_contenu et D_oracle ne sont jamais servis ni lus avant la sélection scellée ; M4 n'alloue le budget que sur D_oracle (N-058). Fuite : rôles et strates scellés avant la génération des mondes ; recherche mécanique de la loi plantée rejouée sur chaque rôle, touches rapportées (R-1) ; les mondes doivent être écrits par programme ou par une famille étrangère aux proposeurs, sinon E3′ n'est pas lisible. Puissance : un monde plus riche contient par construction des effets invisibles à 200 tirages ; les compter comme « non trouvés » serait une erreur d'instrument, d'où la détectabilité calibrée avant de compter. M6 ferme une classe étroite ; le reste est mesuré, pas fermé.

**L'expérience à faire en premier.** E0, sur des mondes pilotes hors des 50 : valider D_oracle v2 par ses contrôles négatifs (composantes fictives, décompositions équivalentes, fausse couverture) et D_contenu v2 sur des paires difficiles disjointes de la calibration. Elle ne coûte que du calcul et quelques appels d'un modèle local, et sans elle aucune des cinq expériences décisives n'est lisible. Immédiatement après, E1′ sur les 50 mondes : si la couverture brute des proposeurs approche ce que le monde offre, la redondance de v67 était un fait du monde, et la seule dépense justifiée est le monde plus riche avec regroupement après jugement (M1, M5) ; si elle en reste loin, les rôles, les tirages multiples et l'allocation de budget deviennent nécessaires et E4′ passe avant E3′. Dans les deux cas, chaque issue falsifie une ligne de dépense avant qu'elle ne soit engagée.

FIN-DE-CELLULE