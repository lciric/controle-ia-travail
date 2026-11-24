# Proposition A, tour III.3 : réponse aux critiques

## 0. État des pièces et conventions

- Les trois pièces sont présentes et entières : ma conception (III.1), la critique B et la critique C. Je ne traite que les sections « Sur la proposition A ».
- Rappel : le §3 de FAITS annonce six familles de mécanismes mais n'en énumère que quatre.
- Les conditions formelles de B et C portent le statut **HYPOTHÈSE**, comme leurs auteurs l'ont déclaré. Les accepter ne les promeut pas : elles restent à démontrer ou à tester.
- Tout seuil numérique est **illustratif**.
- Plusieurs critiques visent le même objet. Je les regroupe par objet (K1 à K20) en citant chaque source, sans fusionner leurs arguments.

---

## (a) Verdict sur chaque critique

| # | Critique (source) | Verdict | Ce qui change |
|---|---|---|---|
| K1 | La corde (1−λ)z₀+λz₁ sort du support d'une variété courbe, et un décodeur lisse rend monotone une paire d'états discrets (B a.1, b.3 ; C a.2, b) | **Acceptée.** Mon critère C3 se trompait dans les deux sens : faux rejet du continu, fausse validation du discret. | C3 est remplacé par un test de sortie d'enveloppe convexe le long d'une géodésique empirique. Ce test est d'abord étalonné sur un cercle et une étoile synthétiques (duel de B c.1 adopté) → P7'. |
| K2 | Le sous-ensemble minimal insatisfaisable booléen déclare fausse toute vraie identité biaisée ou approchée à des ordres différents (B a.1, b.4 ; C a.3, b) | **Acceptée.** | Critère réécrit en **tension ordinale sous nuisances déclarées** (P2'). |
| K3 | Mon monde planté est défini dans les termes mêmes du critère, d'où un avantage par construction (C a.3) | **Acceptée.** | Le générateur est écrit par l'évaluateur externe à partir de simulateurs latents, sans accès au critère. Le comparateur est un test statistique fort. |
| K4 | Comparer le minimum de ΔL à des scissions aléatoires crée un biais d'extremum (C a.3, b) | **Acceptée.** | Le nul est la loi du minimum, recalculé sur de vraies identités. |
| K5 | Permuter les étiquettes de contexte casse la satisfiabilité locale, qui est une précondition du critère (C a.3) | **Acceptée.** | Le contrôle devient : vraies identités soumises au même bruit d'extraction. |
| K6 | dL/dn > 0 dès que le domaine s'étend ou que le bruit croît, sans primitive manquante (B a.1, b.5 ; C a.3, b) | **Acceptée.** | Retiré comme signal autonome et transformé en test différentiel (annexe de P4'). **Je ne sais pas** si une normalisation peut le sauver. |
| K7 | Mon argument d'identifiabilité suppose une contamination de la loi des trajectoires. Une contamination par action, i.i.d., face à un sabotage corrélé dans le temps, reste séparable même pour r ≤ ε. Le rayon d'échantillonnage fini manque (B a.1, b.8 ; C a.4, b) | **Acceptée et transformée en test.** J'avais énoncé la frontière trop largement. | La frontière devient une relation d'inclusion dans une enveloppe de rayon ε + r_n(δ), relative au **modèle de menace du contaminateur** (P3'). |
| K8 | Le CUSUM naïf est un homme de paille ; égaliser les fausses alertes sur l'échantillon de test crée une fuite (C a.4) | **Acceptée.** | Comparateur robuste de même ε, valide à tout temps d'arrêt ; étalonnage sur une partition séparée. |
| K9 | Les macros LaTeX sont confondues par les gabarits, la typographie et la recopie, et λ_prim n'est pas identifiable (B a.2, b.5 ; C a.4, c.5) | **Acceptée.** | Statut inchangé : **OBSERVÉ-NON-AUDITÉ**. Les macros sont retirées de toute chaîne de preuve et ne servent qu'à proposer des candidats, sous contrôle intra-auteur. |
| K10 | Le contrefactuel textuel de P8 confond coordination et sensibilité à la consigne ; θ_coord n'est pas identifiable (B a.2, b.10, c.4 ; C a.4, b) | **Acceptée.** Elle renforce la frontière que j'énonçais. | P8 est rétrogradé et réduit à un test de non-identifiabilité (duel de B c.4). |
| K11 | Le nul est « sur-conditionné » : fibres atomiques donc puissance nulle, et mélange incertain de la chaîne de recâblage (B a.2, b.1) | **Partiellement rejetée.** L'étalonnage par architecture (Gröger et al.) porte sur des comparaisons de représentations, pas sur des graphes recâblés : les trois conditionnements ne s'appliquent pas au même objet. Mon texte était ambigu sur ce point. **Le fond est accepté** : atomicité et δ_m. | Ajout d'un diagnostic d'entropie de fibre et de mélange, servant de règle d'arrêt (P1'). |
| K12 | Le nul est trop faible : communautés, fermeture triadique et date des instruments (Merton) sont absents de N (C a.1, c.1) | **Acceptée** : je signalais le confondant instrumental sans l'inclure dans N. **Transformée** : les blocs doivent être estimés sur D_{<t} seulement. Sinon, le nul absorbe le signal par construction ; c'est l'objection que B adresse à C (B, partie C, b.7), et je l'applique ici. | Hiérarchie de nuls (P1'). |
| K13 | Permuter les dates détruit l'autocorrélation : n'importe quel prédicteur de tendance bat ce contrôle (C a.1) | **Acceptée.** | Remplacé par des coupures placebo t' < t et une base « extrapolation de tendance ». |
| K14 | Pythia et OLMo laissent passer une fuite structurelle : des textes postérieurs à t réorganisent la taxonomie sans contenir la chaîne cherchée. Le canari peut avoir une puissance égale à α malgré l'information post-t (B a.3, b.7, c.3 ; C a.4) | **Acceptée.** | Le sceau porte sur la **date de rédaction**, non sur le contenu. Le duel de B c.3 est adopté comme audit. Les modèles à données ouvertes deviennent auxiliaires. |
| K15 | Appliquer P1 d'abord aux effets publiés (Tshitoyan) crée une fuite de sélection sur k, g et T (C a.4) | **Acceptée.** | Ces effets ne servent qu'à la réplication. k, g et T sont fixés avant ouverture des données. |
| K16 | P1 viole B4 : il existe une zone où l'opérateur bat le nul mais perd contre la base (C a.4) | **Acceptée.** | Une statistique unique, comparée au maximum des comparateurs (P1'). |
| K17 | Les tranches emboîtées créent une dépendance sérielle et confondent taille et non-stationnarité (B a.3, b.6 ; C a.4, b) | **Acceptée.** | Sous-graphes contemporains disjoints ; nul évolutif. |
| K18 | Pour P5 : M̂ n'est qu'une borne supérieure dépendant de l'optimiseur ; le jeu de paraphrases fini est partagé avec l'attaquant ; l'extraction par sondes linéaires est circulaire ; il y a asymétrie d'information (B a.3, b.9 ; C a.4, b, c.6) | **Acceptée.** | M̂ est rapportée comme borne supérieure, par famille d'attaques. J'ajoute des paraphrases réservées, la parité d'information, et le témoin à canal orthogonal libre que B propose contre C (B c.4), que j'emprunte en le disant. |
| K19 | Pour P4 : le comparateur n'a pas de variables liées, et G(z) donne des faux positifs si le code de A est sous-optimal (C a.4, b, c.5) | **Acceptée.** | Comparateur paramétré (anti-unification). Le seuil de G(z) est étalonné sur des mondes sans primitive, à redondance syntaxique appariée. |
| K20 | Puissance : l'AUROC n'est pas jugeable si n₊ est faible ; la résolution Monte Carlo est insuffisante ; en régime clairsemé, k·p̄ → 0 (C b ; B b.2) | **Acceptée.** | Analyse de puissance préenregistrée. La non-jugeabilité est déclarée à l'avance et n'est jamais lue comme un résultat négatif. |

**Bilan.**
- Aucune critique n'est entièrement rejetée ; une l'est partiellement (K11).
- Les plus graves sont :
  - K1 et K2, qui invalidaient deux de mes critères de démarcation tels que je les avais écrits ;
  - K7, qui corrige une frontière formulée trop largement ;
  - K14, qui retire à mon protocole d'étanchéité sa pièce centrale.

---

## (b) Expériences corrigées

### P1'. Banc de démarcation à nul hiérarchique

**Nuls emboîtés.**
- N₀ : fréquences.
- N₁ : N₀ + degrés (recâblage de Maslov et Sneppen).
- N₂ : N₁ + blocs estimés sur D_{<t} uniquement.
- N₃ : N₂ + date de disponibilité des instruments communs.

**Diagnostics.**
- Pour chaque niveau, plusieurs chaînes indépendantes et une estimation du nombre effectif de graphes distincts visités. **Je ne sais pas** quelle valeur prendra δ_m sur des graphes typés.
- Si ce nombre est inférieur à 1/α, le niveau est déclaré **non jugeable** avant toute lecture.
- Le nombre de tirages Monte Carlo B vérifie (B+1)⁻¹ ≤ α/|H|, où H est la famille de tests déclarée.

**Comparateurs.**
- Bases mécaniques : attachement préférentiel, voisins communs, fréquence seule, extrapolation de tendance.
- Coupures placebo t' < t : leur distribution empirique capture la variance due à la fermeture triadique, que le nul paramétrique sous-estime.

**Duel (conforme à B4).**
- Δ = Prec@k(opérateur) − max(q_{1−α}(N₃), Prec@k(meilleure base), q_{1−α}(placebo)).
- **H_A** : Δ > 0, c'est-à-dire un alignement typé qui survit au niveau N₃.
- **H_B** : Δ ≤ 0.
- **Plan d'arrêt.** Plan séquentiel par e-valeurs. On s'arrête au rejet de H_A ou de H_B. Si le budget s'épuise sans rejet, on déclare un échec du plan, et non un résultat.
- **k** est choisi pour qu'au moins un nombre préenregistré de confirmations soit attendu sous le nul (illustratif : 20). En dessous, la comparaison est déclarée non jugeable (K20).
- On rapporte aussi le niveau ℓ* le plus profond auquel l'effet survit. Seul N₃ fait l'objet du duel.

**Falsification.**
- Δ > 0 réfute H_B.
- Δ ≤ 0 réfute H_A sur ce corpus.

**Premier pas sans dépense.** Comptes de cooccurrence par année à partir de métadonnées publiques ; table des dates d'instruments construite **avant** l'ouverture de D_{>t} ; réplication d'un effet publié de type Tshitoyan, à titre de réplication seulement (K15).

### P2'. Scission par tension ordinale sous nuisances déclarées

**Critère (HYPOTHÈSE).**
- Chaque contexte k est un modèle statistique muni d'une classe de nuisances 𝒩_k déclarée à l'avance : décalage d'étalonnage, recalibration monotone, régime d'approximation.
- Une **fausse identité** est signalée si deux conditions sont réunies :
  1. ρ(c) dépasse le nul ;
  2. le modèle à variable partagée est rejeté **pour toute recalibration monotone par contexte**. La contradiction porte alors sur des relations d'ordre (signes de variations), pas sur des valeurs. Exemple : apport de chaleur positif à température constante, face à une relation où la chaleur est une fonction monotone de la température.
- Un biais d'étalonnage, ou une linéarisation d'une loi monotone, préserve l'ordre et ne déclenche donc rien (K2).

**Coût assumé.** Les fausses identités à tension seulement cardinale échappent au critère.

**Monde planté.**
- Écrit par l'évaluateur à partir de simulateurs latents (K3).
- Il contient : de vraies identités avec biais d'instrument et troncatures de Taylor distinctes (contrôle de B c.2) ; des polysémies ; des fausses identités à tension ordinale ; des fausses identités à tension seulement cardinale.

**Comparateur.** Regroupement de contextes, puis test de paramètre partagé avec les mêmes nuisances (sans solveur SMT).

**Nul de la scission.** Loi de min_π ΔL(π) calculée sur de vraies identités soumises au même bruit (K4, K5). L'effectif n₊ est fixé par analyse de puissance (K20).

**Duel.**
- **H_A** : à taux de fausses scissions ≤ α sur les vraies identités biaisées, le rappel sur les fausses identités ordinales dépasse celui du comparateur d'une marge préenregistrée (illustratif : 0,1).
- **H_B** : fausses scissions > α, ou rappel ≤ comparateur + marge.
- **Prédiction annexe** : sur les fausses identités cardinales, le rappel du critère devrait rester proche de α. Un rappel nettement supérieur réfuterait ma compréhension de ce que le critère capture.

**Falsification.** La première issue réfute H_B ; la seconde réfute H_A.

### P3'. Frontière d'identifiabilité au niveau trajectoire

**D'abord une preuve, pas une expérience.** Si la loi des trajectoires sous sabotage appartient à l'enveloppe nulle 𝒫 = {(1−ε')P₀ + ε'Q}, avec ε' = ε + r_n(δ), **dans la classe Q que le modèle de menace attribue au contaminateur**, alors aucun test de niveau α uniforme sur 𝒫 n'a une puissance supérieure à α.
- Ce sens de l'énoncé est immédiat.
- La réciproque, c'est-à-dire l'existence d'un test puissant hors de l'enveloppe, est à démontrer ; **je ne sais pas** sous quelles conditions de taille d'échantillon elle tient.
- La preuve est vérifiée par un tiers.
- Conséquence : la garantie ne vaut jamais mieux que le modèle de menace déclaré du contaminateur. Le seuil « r ≤ ε » de ma version III.1 n'en est qu'un cas particulier, celui de l'i.i.d. marginal.

**Simulation, pour vérifier l'implémentation et non le théorème.**
- Scores scalaires synthétiques.
- Contamination i.i.d. par action.
- Sabotage à r ≤ ε, soit i.i.d., soit groupé dans le temps (chaîne de Markov abstraite sur des scores, sans aucune recette d'attaque).
- Comparateur : e-processus robuste de même ε, valide à tout temps d'arrêt (K8).
- Contrôle de validité : traces honnêtes sous dérive de covariables (C c.4).

**Duel.**
- **H_A (frontière trajectoire)** : pour un sabotage groupé à r ≤ ε, la puissance dépasse α + δ.
- **H_B (ma frontière marginale initiale)** : la puissance reste ≤ α + δ pour tout r ≤ ε.
- **Falsification.** Une puissance > α + δ réfute H_B ; une puissance ≤ α + δ réfute H_A.

### P4'. Primitives par compression, à comparateur paramétré

**Protocole.**
- Les mondes sont générés, pas amputés : les critiques de dépliage rétrospectif adressées à B et C ne s'appliquent pas ici.
- Comparateur : anti-unification avec variables liées, sans critère de longueur de description (K19).
- Le seuil de G(z) est le quantile 1−α de max_z G(z) sur des mondes sans primitive, à redondance syntaxique appariée.

**Duel.**
- **H_A** : la primitive plantée est récupérée, avec équivalence vérifiée, à un taux supérieur à celui du comparateur d'une marge préenregistrée, et les fausses primitives restent ≤ α.
- **H_B** : sinon.

**Annexe (K6).** On compare dL_A/dn entre des mondes « expansion de domaine sans primitive manquante » et des mondes « primitive manquante », appariés en volume et en bruit.
- Si les deux distributions se recouvrent au-delà d'un seuil préenregistré, dL/dn est définitivement abandonné.
- Sinon, il est conservé comme signal différentiel uniquement.

### P5'. Marge asymétrique, rapportée comme borne supérieure

**Protocole.**
- Familles d'attaques d'intensité croissante, déclarées à l'avance et cantonnées au bras d'attaque.
- Chaque moniteur est attaqué **directement**, à budget égal (C, partie B, c.6, appliqué symétriquement).
- Paraphrases d'évaluation réservées, jamais vues de l'attaquant.
- Parité d'information : la base est un ensemble de sondes linéaires lisant les mêmes paraphrases.
- Contraintes relationnelles extraites des comportements par interventions, et non par sondes linéaires (K18).
- Témoin à canal orthogonal libre (emprunté à B c.4).

**Duel.**
- **H_A** : le rapport M̂_rel/M̂_lin dépasse un seuil préenregistré à toutes les intensités, sans décroître vers 1 quand l'intensité croît.
- **H_B** : à l'intensité maximale, le rapport tombe sous le seuil.

**Limite assumée.** Survivre au test ne certifie jamais une borne inférieure de la marge (frontière, voir (c)).

### P6'. Transitions sur sous-graphes disjoints

**Protocole.**
- Sous-graphes contemporains disjoints (champs distincts à la même date) au lieu de tranches emboîtées.
- Nul évolutif : attachement préférentiel avec vieillissement, sans fusion de champs.
- Ajustement d'effondrement d'échelle avec les mêmes degrés de liberté sur le nul.

**Duel.**
- **H_A** : les exposants sont cohérents sur au moins trois tailles et s'écartent du nul.
- **H_B** : le nul reproduit la « transition ».

**Attendu.** Une issue négative, qui servira d'outil de réfutation.

### P7'. Continu contre discret par sortie d'enveloppe convexe

**Chemin d'interpolation.**
- Géodésique empirique dans le graphe des k plus proches voisins des activations réelles. La distance au support est rapportée à chaque pas (K1).

**Statistique.**
- Pour une famille de suffixes arithmétiques s (par exemple « cinq ans plus tard »), on mesure la masse des continuations **hors de l'enveloppe convexe** des continuations des états-ancres traversés, avec un poids de mélange w(λ) commun à tous les suffixes.
- **H_B (juxtaposition discrète, à lecture douce des ancres)** prédit une masse hors enveloppe nulle.
- **H_A (variété continue)** prédit une « nouveauté intermédiaire » : par exemple, une continuation propre à la valeur médiane, absente des deux extrémités.

**Étalonnage obligatoire, avant tout modèle.**
- Cercle S¹ contre étoile à sept atomes, chacun lu par un décodeur lisse et par un décodeur abrupt.
- Exigence : α + β < 1 − η, avec η préenregistré (duel de B c.1).
- Si l'étalonnage échoue, le test est abandonné.

**Application.**
- Aux années et à la géographie, où les valeurs intermédiaires ont un sens (sous-espaces de Gurnee et Tegmark, **VÉRIFIÉ**).
- Pas aux jours de la semaine, où Gupta et al. (**VÉRIFIÉ**) ont déjà tranché localement.

**Falsification.** Une masse hors enveloppe supérieure au nul bootstrap réfute H_B ; une masse dans le nul réfute H_A.

### P8'. Essaims : test de non-identifiabilité

**Protocole (duel de B c.4 adopté).** On applique le même contrefactuel textuel à des modèles entraînés isolément, et à des copies portant une coordination plantée.

**Duel.**
- **H_A** : la statistique sur les copies coordonnées dépasse le quantile 1−α obtenu sur les modèles isolés.
- **H_B** : non.

**Attendu.** Plutôt H_B, ce qui confirmerait qu'aucune mesure comportementale ne sépare coordination et politique commune sans référence honnête des mêmes poids.

### Ordre révisé (notes illustratives ; seul l'ordre grossier compte)

| Rang | Proposition | Raison principale |
|---|---|---|
| 1 | P1' | Coût sur processeur seul ; conditionne tout le volet corpus. |
| 2 | P3' | Preuve d'abord, simulation sur processeur ensuite. |
| 3 | P2' | |
| 4 | P7' | Étalonnage synthétique sur processeur, puis carte graphique légère. |
| 5 | P4' | |
| 6 | P6' | |
| 7 | P5' | Lourd, environ 8 milliards de paramètres (FAITS). |
| 8 | P8' | Rétrogradé (K10). |

**Sensibilité.**
- Si l'on donne au critère « portée vers le contrôle » un poids double, P3' passe premier.
- Si l'on met le coût au carré, P5' tombe au dernier rang.

---

## (c) Réponse à la question de l'arbitre (une page)

### Ce qui est établi

Tous les points suivants sont **VÉRIFIÉ**, au sens restreint de FAITS §2 :
- des statistiques de cooccurrence reconstruisent des géométries réelles (positions de cités et de villes, sous-espaces spatiaux et temporels linéaires) ;
- les régularités vectorielles proviennent de factorisations implicites de l'information mutuelle ponctuelle ;
- après étalonnage par permutation, la convergence des représentations est **locale**, pas globale ;
- une géométrie circulaire peut se comporter localement comme **sept états discrets** ;
- une sonde précise peut mémoriser sans sélectivité ;
- des modèles performants échouent au transfert de la loi sous-jacente ;
- simuler une coupure temporelle par consigne laisse un écart mesuré de 52 %.

**Conséquence.** La géométrie des représentations porte de l'information, mais ni sa forme, ni sa continuité, ni sa transférabilité ne se lisent directement. Cette conclusion est l'assemblage de faits vérifiés, pas un fait nouveau.

### Ce qui n'est pas établi (HYPOTHÈSE)

- Qu'un alignement à distance de surface survive à un nul incluant communautés, fermeture triadique et dates d'instruments. **Je ne sais pas** quelle fraction survivra.
- Qu'une fausse identité soit détectable avant coup. Mon critère ordinal (P2') ne l'est que sur mondes plantés, au prix de manquer les tensions seulement cardinales.
- Qu'un exposant critique ait un sens sur un graphe scientifique unique.
- Qu'un moniteur relationnel offre une marge asymétrique.
- Que les opérateurs d'idéation se transfèrent au contrôle.

### Frontières (HYPOTHÈSE argumentée, non démontrée)

Les critiques en ont précisé ou ajouté plusieurs :
1. **Biais de déclaration.** Ce qui n'est jamais dit ne laisse aucune cooccurrence. Il faut un ancrage non textuel.
2. **Dilemme du nul conditionnel** (B contre C, rendu explicite) :
   - conditionner davantage écarte les artefacts, mais atomise la fibre et annule la puissance ;
   - une affirmation d'invariant n'a de sens qu'au niveau de conditionnement déclaré ex ante où la fibre reste non atomique.
3. **Rareté des cibles.** Les ponts féconds sont rares (k·p̄ → 0, B) : la cible la plus intéressante est la moins testable en rétrodiction réelle.
4. **Contamination de la référence.** La garantie de fausses alertes vaut exactement ce que vaut le modèle de menace du contaminateur (P3').
5. **Marges contre un adversaire.** Aucune famille finie d'attaques ne certifie une borne inférieure de marge. Il faudrait une preuve, que personne ne sait produire à l'échelle visée.
6. **Essaims.** La coordination implicite n'est pas identifiable du comportement seul sans référence honnête des mêmes poids.

### Opérateurs prioritaires

| Opérateur | Rôle | Statut |
|---|---|---|
| Banc à nul hiérarchique avec règle d'arrêt par entropie de fibre (P1') | Filtre d'entrée de tout le volet corpus | HYPOTHÈSE |
| Détecteur séquentiel à enveloppe déclarée au niveau trajectoire (P3') | Transfert direct au contrôle | HYPOTHÈSE |
| Scission par tension ordinale (P2') | Détection de fausses identités | HYPOTHÈSE |
| Test de sortie d'enveloppe pour continu contre discret (P7') | Démarcation géométrie apparente / structure | HYPOTHÈSE |

### L'expérience à faire en premier : P1'

**Pourquoi elle.**
- Elle tourne sur processeur seul et données publiques.
- Si les alignements typés ne survivent pas au niveau N₃ (instruments datés), la moitié du programme d'idéation sur corpus perd son objet.
- Si certains survivent, elle fournit l'unique ensemble de candidats légitimes pour P2' et P4'.
- Ses deux issues sont informatives et préenregistrables.

**Ce que je ne recommande pas.** P3' est aussi bon marché, mais sa frontière est mathématique : elle doit être **démontrée**, et la simulation ne fait qu'en vérifier l'implémentation. La démontrer en parallèle ne coûte rien en calcul.

FIN-DE-CELLULE