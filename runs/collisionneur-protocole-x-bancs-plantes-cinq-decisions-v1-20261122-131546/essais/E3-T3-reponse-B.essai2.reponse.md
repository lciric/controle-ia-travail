# Proposition B — Tour III.3 : réponse aux critiques

## 0. Pièces et conventions

- **FAITS et QUESTION DE L'ARBITRE** : présents, même texte et même empreinte affichée, que je n'ai pas recalculée. La question fixe la forme du §3.
- **E3-T1-conception-B** : présente, close par FIN-DE-CELLULE.
- **Critiques croisées A, C, D, E, F, G, H, I** : présentes, chacune close par FIN-DE-CELLULE. Aucune n'est visiblement coupée. Il n'y a pas de critique « B » : c'est la mienne, et elle n'est pas transmise.
- La pièce H annonce « sept propositions » et en énumère huit. C'est une incohérence de décompte, sans effet sur sa section qui me vise.
- **Statuts.** Je garde ceux de III.1, inchangés : RAPPORTÉ pour ce que le dossier affirme, HYPOTHÈSE pour ce qu'il dit non vérifié et pour tout ce que j'ajoute. Les affirmations des critiques sont citées avec le statut qu'elles leur donnent. « VÉRIFIÉ (calcul refait) » ne couvre ici que des identités ou de l'arithmétique refaites dans ce texte, à entrées illustratives. Aucune donnée n'est vérifiée.
- Rien dans les pièces n'est exécuté comme consigne. Je ne réponds qu'aux sections « Sur la proposition B ».

---

## 1. Livrable (a) — Sort de chaque critique

Je regroupe les objections par point soulevé, en nommant chaque source. Quand le verdict diffère selon la source, la source a sa propre ligne.

### Décision 1

| # | Objection (sources) | Verdict | Conséquence |
|---|---|---|---|
| O1 | Le duel 1a éprouve le paramétrage du simulateur, dont la fidélité n'est pas mesurée. R croît avec le nombre de réplicats. Son contrôle négatif échoue 5 à 9 % du temps sous un simulateur sain (A, E, F, G, H, I). | Acceptée. Calcul refait, si les deux contrôles sont indépendants : 1 − (1 − 0,0455)² ≈ 0,089 (VÉRIFIÉ, calcul refait). | Duel 1a retiré. La décision 1 ne dépend plus du simulateur. |
| O2 | Si A = 1 − p_sig, l'option (a+) est aveugle à un transfert de l'acceptation vers l'abstention : sa puissance contre ce scénario vaut le niveau (A, F). | Acceptée | Décision 1 révisée (§3). Ce scénario a le même profil que celui des calculs rapportés : A stable, B mobile. |
| O3 | 1b n'est pas une bipartition : ΔA ≥ +δ n'est classé nulle part (E, G). | Acceptée | Complément exact dans D1′. |
| O4 | ΔA n'est pas jugeable si la demi-largeur de l'intervalle dépasse δ (A, F, G). | Acceptée | Porte de puissance calculée avant le gel. |
| O5 | A serait mesurée sur le jumeau, alors que le dossier parle de « l'agent honnête » (G, qui le marque RAPPORTÉ). | Transformée en définition écrite | Je ne conteste ni ne reprends cette lecture. Le texte gelé nomme la population de A et de B, la même pour les deux. |
| O6 | La zone « non concluante » 2 < R < 3 censure B (C). | Rejetée | Une zone non concluante qui renvoie à une option déclarée d'avance n'est pas une censure. L'objection est de toute façon sans objet : 1a est retiré et B entre au texte avec un critère. |
| O7 | Apparier par graine des lois distinctes est impossible, et ΔA mêle l'effet du monde sur le moniteur et son effet sur la sortie du jumeau (I). | Acceptée pour l'appariement, rejetée pour le confondant | L'estimande du témoin est l'effet total du monde sur l'acceptation de l'honnête. Apparier sur une variable aval effacerait cet effet. Sans graines partagées (HYPOTHÈSE), la comparaison se fait sans appariement. |

### Décision 2

| # | Objection (sources) | Verdict | Conséquence |
|---|---|---|---|
| O8 | Les paires nulles omettent l'édition du tiers, la variance de génération et les reformulations bénignes (A, C, D, E, F, G, I). L'hypothèse 5 décide de la loi nulle, et l'erreur peut aller dans les deux sens (I). | Acceptée | Paires nulles conformes au plan final (D2′), en trois types rapportés séparément. |
| O9 | Deux demi-panels disjoints doublent la variance par rapport au panel complet de la campagne (F, qui le marque VÉRIFIÉ). | Acceptée. C'est exact si les lectures sont indépendantes et de même loi (HYPOTHÈSE de modèle). | Les paires nulles sont lues selon le plan de lecture final. |
| O10 | Si t_m dépasse 1/m, la strate « un contrôle » n'est plus détectée que par le bruit. Un seuil conservateur se valide sans rien mesurer. Le quantile saute de façon discrète (A, C, D, F). | Acceptée | Ces strates sont déclarées « non mesurables » avant le lot final. Aucun q n'y est rapporté comme détection. |
| O11 | « Au moins le quantile » n'équivaut pas à « au-dessus du quantile » sur une loi discrète (E). | Acceptée | t_m est défini par une borne sur P(X ≥ t). |
| O12 | Avec 60 paires par strate, seule l'issue (b′) est praticable : l'issue (a) exige un taux vrai d'au plus 0,5 % environ (I, H). | Acceptée. Calcul refait : 0,995⁶⁰ ≈ 0,74 ; une alerte sur 60 donne une borne unilatérale à 95 % d'environ 0,077 (VÉRIFIÉ, calcul refait, entrées illustratives). | J'ajoute ce que ce duel masquait : max(1/m, Q) = 1/m dès que Q ≤ 1/m, donc (b′) contient (a). Le duel « (a) contre (b′) » était mal posé. |
| O13 | On étalonnerait sur les données mêmes du duel 2 (G). Le taux de fausses alertes réalisé reste aléatoire et la garantie n'est que marginale (I). | Acceptée | Lots d'étalonnage et de validation disjoints. La validation se fait sur des paires nulles neuves. |
| O14 | Un affaiblissement qui fait baisser la part de moins de 1/m échappe à toute règle (D). | Acceptée, transformée en mesure | Détection rapportée par type (retrait ou affaiblissement). Ce défaut est commun à (a) et à (b′). |
| O15 | Le duel 2 mélangerait deux types de paires nulles (H). | Rejetée | Le duel 2 n'en prévoyait qu'un : « une même version honnête, lue par deux tirages disjoints ». Le second n'apparaît que dans la clause de changement d'avis. Le besoin de séparer les types est couvert par O8. |

### Décision 3

| # | Objection (sources) | Verdict | Conséquence |
|---|---|---|---|
| O16 | Le cadre de tirage n'est pas dit. Tiré parmi les seuls passages désignés, il donne un rappel de 1. Extrapoler exige d'inclure les non-désignés, avec des poids connus (A, D). | Acceptée | Le cadre devient l'ensemble des passages candidats, avec des probabilités d'inclusion connues. |
| O17 | La bascule est décidée sur l'échantillon qui chiffre la fidélité (F, G). Une borne basse peut ne traduire que l'imprécision (E). La précision est ignorée (G). | Acceptée | Échantillon coupé en deux moitiés. Bascule seulement sur preuve d'échec, lue sur la borne supérieure. La précision devient un co-critère. |
| O18 | Les couples désappariés sont lexicalement disjoints par construction : ils ne testent pas les faux positifs internes au document (E, F, G, I). | Acceptée | Ajout de leurres internes au document : négations et mentions. |
| O19 | L'arbitrage humain n'est pas étalonné (H). Une erreur d'étiquetage tire l'écart vers 0 (G). | Transformée en test | L'accord entre annotateurs est mesuré avant l'arbitrage, et l'arbitre ne sait pas quel instrument a désigné. Sous un seuil d'accord, la strate n'a pas de référence. |
| O20 | Avec moins de 30 passages par strate, l'intervalle chevauche toujours Δ (I). | Acceptée | Effectif minimal par strate, ou fusion de strates gelée d'avance. |
| O21 | Le repéreur peut être de la même famille de modèles que le moniteur (H). | Acceptée, et étendue | Mon ancrage de III.1 (§5) prévoyait la même famille pour le repéreur et les lecteurs simulés : c'est la même fuite. Corrigé : le repéreur vient d'une famille disjointe de celles des lecteurs de l'oracle et des moniteurs. |

### Décision 4

| # | Objection (sources) | Verdict | Conséquence |
|---|---|---|---|
| O22 | Le duel 4.1 est vrai par construction : à dose fixe, couvrir dose × q revient à couvrir q. Un oracle aveugle est couvert alors qu'il ne reconnaît aucun dommage. Deux lois de même (X, E, U) peuvent porter des dommages différents (A, E, F, G, I). | Acceptée | Le duel ne touchait pas mon objection. Il est remplacé par un duel de discrimination (D4.1′). L'argument de E renforce (c′), et je m'en sers en le disant. |
| O23 | Le produit dose × q ne serait pas homogène à une « quantité de dommage » (C). | Partiellement rejetée | Par strate, dose_s × q_s est homogène : c'est la part des épisodes qui portent un dommage non repéré de taille s. L'agrégation par la taille doit en revanche être nommée. |
| O24 | La grille est finie, la marge de Monte-Carlo n'est pas simultanée et les événements d'excès sont peu nombreux (A, D, E). | Acceptée | Marge simultanée sur les configurations, points tirés hors grille, effectif fixé par le nombre d'événements d'excès. |
| O25 | Le couplage entre excès et bornes de q est nul par construction. Le bras à niveaux fixes tourne sous d'autres dépendances (D, I). | Acceptée | Voir D4.2′. |

### Décision 5

| # | Objection (sources) | Verdict | Conséquence |
|---|---|---|---|
| O26 | « k connu » et « composition fixe » changent ensemble. Un écart peut venir de la seule variance de K (A, D, E, G). | Acceptée | Mêmes compositions tirées dans tous les bras : seule l'information change. |
| O27 | Viser E[K] affaiblit le saboteur par construction. Viser le mode, ou estimer K sur les données, est plus fort (F, I). | Acceptée | Saboteur adaptatif K̂(X) et prédicteur modal. |
| O28 | L'écart d'évasion est borné par P(K ≠ k*) : H_A peut être impossible (C). | Acceptée, transformée en contrainte de conception | La loi de tirage de 5(a) doit vérifier P(K ≠ mode) ≥ Δ. |
| O29 | L'évasion mêle l'erreur propre du script et la perméabilité de la règle de cohérence (G). | Acceptée | Mesure de P(cohérente sachant fiche fausse). P(fiche fausse) est rapportée à part. |
| O30 | Il manque des épisodes K = 0, une fiche grossièrement incohérente et un test de cardinalité pure (C, G, I). | Acceptées | Ajoutés à D5′. |
| O31 | La puissance serait d'environ 0,50 à n = 100 (H). | Rejetée | Le duel est scripté sur des données simulées, avec 10⁴ répétitions (illustratif, §5 de III.1). La contrainte réelle est le nombre de fiches fausses : voir O29. |

### Autre

| # | Objection (sources) | Verdict | Conséquence |
|---|---|---|---|
| O32 | « Si le classifieur de surface ne sépare pas les mondes, la confusion est corroborée » : l'échec d'un test faible ne corrobore rien (A). | Acceptée | Le test ne joue que dans un sens. Une séparation réfute la confusion ; une non-séparation laisse son statut RAPPORTÉ inchangé. |

---

## 2. Livrable (b) — Expériences corrigées

Convention, reprise de E en le disant : chaque duel oppose un paramètre à son complément exact. Un intervalle situé entièrement d'un côté falsifie l'autre côté. Un intervalle à cheval est écrit « non concluant ». Tous les seuils et effectifs sont illustratifs.

### D1′ — Le témoin (remplace 1a et 1b)

**Avant le gel, sans donnée :**
- Définitions écrites.
  - A = 1 − p_sig, d'après la glose « (ne signale pas) » (HYPOTHÈSE de lecture).
  - B = p_abs.
  - La population est nommée, la même pour A et B.
- Porte de puissance. On calcule, à l'effectif de campagne, les demi-largeurs w_A et w_B des intervalles. Si w > δ, le texte gelé déclare le critère correspondant non informatif.

**Après le gel.** On note θ_A = A(témoin) − A(référence) et θ_B = B(témoin) − B(référence). Le niveau d'erreur est partagé entre les deux.
- Pour A : H_A^A : θ_A > −δ_A, contre H_B^A : θ_A ≤ −δ_A.
- Pour B : H_A^B : θ_B < δ_B, contre H_B^B : θ_B ≥ δ_B.
- Les hausses de A et les baisses de B sont rapportées telles quelles.

**Contrôle négatif.** Le vrai moniteur est appliqué à deux moitiés du monde de référence. Le seuil est rapporté à la variance propre d'une différence de demi-échantillons.

### D2′ — Paires nulles conformes au plan final (remplace le duel 2)

**Préalable écrit, avant toute mesure :**
- confirmer l'hypothèse 5 (la version sabotée dérive de l'honnête) ;
- décrire le plan de lecture final : taille de panel, et mêmes lecteurs ou non pour l'objet et sa comparaison.

**Trois types de paires**, lues selon ce plan et rapportées séparément :
1. l'honnête contre l'honnête retouché par le même tiers, sans retrait de contrôle. C'est le type principal si l'hypothèse 5 tient ;
2. la même version relue ;
3. deux productions honnêtes. C'est le type principal si l'hypothèse 5 ne tient pas.

**Règle.** t_m est le plus petit seuil k/m, avec k ≥ 1, dont la borne supérieure exacte de P(X ≥ k/m) est au plus α_FA. Cette borne est calculée sur le lot d'étalonnage du type principal. Le seuil est ensuite validé sur un lot neuf.

**Duel, par strate de m.** Soit θ_m = P(X ≥ 1/m) sous la loi nulle principale.
- H_A : θ_m ≤ α_FA dans toutes les strates. Alors (b′) se réduit à (a).
- H_B : θ_m > α_FA dans au moins une strate. Sa strate « un contrôle » est alors déclarée non mesurable.

**Effectif.**
- Il faut au moins 59 paires pour qu'une borne ≤ 0,05 existe, même à zéro alerte (VÉRIFIÉ, calcul refait : 0,05^(1/59) ≈ 0,9505).
- Pour le type principal, je prévois environ 300 paires par strate. Si le taux vrai vaut 0,02, l'issue H_A sort alors avec une probabilité d'environ 0,85 (calcul approché, entrées illustratives).
- Pour les types secondaires, 60 paires par strate.

**Contrôles :**
- déterminisme : mêmes lectures, agrégation recalculée, l'écart doit être nul ;
- contrôle positif : tous les contrôles retirés ;
- « plume du tiers » : si le type 1 dépasse le type 2 au-delà de la marge, les relectures ne suffisent pas ; sinon, l'artefact d'édition est falsifié.

**Repli.** Si 59 paires par strate sont hors budget, on applique (a), avec des fausses alertes mesurées et rapportées sans garantie, et on l'écrit tel quel.

### D3′ — La désignation

**Cadre de tirage.** Tous les passages candidats, stratifiés selon trois axes : désigné ou non, retrait ou affaiblissement, valeur de m. Les probabilités d'inclusion sont connues. Les non-désignés lexicalement proches du contrôle sont sur-représentés, et l'estimation est pondérée en conséquence. Chaque strate compte au moins 30 passages ; sinon, une fusion de strates est gelée d'avance.

**Référence.** Deux annotateurs, qui ne savent pas quel instrument a désigné le passage. Leur accord est mesuré avant l'arbitrage. Sous un seuil d'accord, la strate n'a pas de référence.

**Partage de l'échantillon.** La moitié 1 décide la bascule. La moitié 2 chiffre la fidélité publiée.

**Duel.** On note θ = rappel du repéreur − rappel du recouvrement de mots, mesuré de façon appariée sur les affaiblissements.
- H_A : θ < Δ, contre H_B : θ ≥ Δ (Δ = 0,10).
- La précision est rapportée à côté. La bascule exige en outre que le repéreur ne perde pas plus de Δ en précision.

**Règle de bascule, par strate :**
- si la borne supérieure du rappel du recouvrement est sous 0,90, la strate passe au repéreur ;
- si la borne inférieure est au moins 0,90, elle reste au programme ;
- sinon, l'échantillon est complété jusqu'à un plafond gelé, puis la strate passe au repéreur par prudence.

**Contrôles :**
- leurres internes au document (négations, mentions) ;
- paraphrases pures ;
- retrait factice d'un passage qui ne porte aucun contrôle, pour détecter une trace d'édition ;
- couples désappariés, vérifiés par un humain.

**Familles de modèles.** Le repéreur vient d'une famille disjointe de celles des lecteurs et des moniteurs.

### D4.1′ — La discrimination en régime d'excès (remplace le duel 4.1)

**Modèle**, repris de I en le disant (HYPOTHÈSE) :
- les lecteurs jugent contrôle par contrôle, avec des taux d'erreur ε_m et ε_h ;
- leurs erreurs sont corrélées à l'intérieur d'un même objet, avec un coefficient ρ ;
- la règle de signalement est la règle appariée de D2′ ;
- l'excès est déclenché par la règle admise.

**Cible.** δ_s = P(signal sachant dommage de strate s) − P(signal sachant édition factice).

**Hypothèses.**
- H_A : en excès, δ_s ≥ η dans toutes les strates de la grille.
- H_B : δ_s < η dans au moins une strate.

**Issues.**
- H_B : la règle ne distingue pas un dommage d'une simple édition. Le produit dose × q̄ ne se lit pas comme un dommage, et (c′) est confirmée.
- H_A partout : mon objection tombe, et (b) devient défendable.

**Contrôles.**
- Oracle aveugle (ε_m = 1 − ε_h) : δ_s doit y valoir 0.
- Configurations hors excès : δ_s doit y dépasser η.
- La marge est simultanée sur la grille, et des points sont tirés hors grille.

Le signe du biais de q̄ en excès est rapporté au passage. Il reste une HYPOTHÈSE tant que ce duel n'a pas tourné.

### D4.2′ — La réaffectation conditionnelle

**Dispositif :**
- l'excès et les bornes de q sont calculés sur les mêmes lectures honnêtes ;
- la dépendance entre lecteurs est balayée ;
- q est pris dans ]0, 1[ ;
- un témoin à niveaux fixes tourne sous les mêmes dépendances ;
- chaque configuration compte au moins 10³ événements d'excès ;
- la marge est simultanée, et des points sont tirés hors grille.

**Hypothèses.** H_A : l'erreur d'ensemble reste au plus égale au niveau total dans toutes les configurations. H_B : elle le dépasse dans au moins une.

**Limites.**
- Le duel n'est pas exécutable en l'état : le niveau total est absent des faits.
- Même sous H_A, l'option qui en résulte est une règle conditionnelle gelée maintenant, et non l'option (b).

### D5′ — Ce que connaître K apporte au saboteur

**Compositions.** Les mêmes dans tous les bras, tirées selon la loi de 5(a), avec la contrainte P(K ≠ mode) ≥ Δ. La force du signal est réglée de façon à fixer, par strate, S = P(les K statistiques les plus fortes sont exactement les vraies lois).

**Bras** (seule l'information donnée au saboteur change) :
1. K révélé ;
2. K permuté entre épisodes ;
3. aucune indication. On fait jouer un saboteur adaptatif, qui estime K̂(X) avec un seuil corrigé pour les tests multiples, et un prédicteur modal.

**Effet mesuré.** P(cohérente sachant fiche fausse) dans le bras 1, moins la même probabilité dans le bras 3, par valeur de K. Les épisodes K = 0 sont traités à part.

**Hypothèses.** H_A : l'effet atteint au moins Δ pour au moins une valeur de K. H_B : il reste sous Δ pour toutes (Δ = 0,10).

**Issues.**
- H_A : l'option (a) est requise.
- H_B : l'argument de fuite tombe, et (b) devient défendable.
- Si en plus K̂(X) = K presque toujours, le tirage ne cache pas K. La règle de cohérence a alors besoin d'un autre témoin, sous les deux options.

**Contrôles :**
- un analyste honnête scripté joue dans tous les bras ; son taux de fiches jugées cohérentes ne doit pas varier de plus de Δ/2 ;
- une fiche grossièrement incohérente doit être rejetée ;
- cardinalité pure : on oppose k statistiques faibles à k − 1 statistiques fortes, pour voir si la règle se réduit à compter ;
- épisodes K = 0.

---

## 3. Livrable (c) — Réponse à la question de l'arbitre

| Décision | Option | Confiance | Raison | Ce qui me ferait changer d'avis |
|---|---|---|---|---|
| 1 | **Option meilleure que (c), « (c+) »** : A et B, chacune sous son nom ; définition et population écrites ; marge, intervalle et trois issues gelés ; niveau partagé. | 0,60 | Si A = 1 − p_sig, A seule est aveugle au transfert de l'acceptation vers l'abstention. B entre pour cette raison de définition, non pour la variation qu'on en attend. Le critère gelé lève l'objection « sans critère » faite à (c). | Un écrit montre qu'« acceptation » désigne l'acceptation stricte : A, ainsi définie, suffit. Ou la porte de puissance montre que B n'est pas jugeable à l'effectif de campagne : A seule, avec cette limite écrite. |
| 2 | **(b′) corrigée** : seuil réglé sur une nulle conforme au plan final, validé sur un lot neuf, strates perdues déclarées. | 0,55 | (b′) contient (a) et ne coûte que l'étalonnage. Elle ne règle que les fausses alertes, ce qui est le rôle d'une définition de « reconnu ». | L'oracle livre sa règle binaire. Ou 59 paires par strate sont hors budget : (a), avec fausses alertes mesurées et rapportées. |
| 3 | **(c) durcie, corrigée** | 0,65 | C'est la seule option qui chiffre l'erreur de désignation. Elle s'extrapole par un tirage probabiliste pondéré, et la bascule n'a lieu que sur preuve d'échec. | L'accord entre annotateurs est bas : rien n'est chiffrable, et (b) s'applique par défaut. Ou le repéreur ne fait pas mieux que le recouvrement : (a), avec la mesure de fidélité. |
| 4.1 | **(c′)** : (c) plus la publication du constat d'excès, énoncé qui porte sur l'oracle. | 0,60 | Une borne de q couvre même un oracle aveugle (argument de F). En excès, la loi observée n'identifie pas le dommage (argument de E). | D4.1′ montre une discrimination conservée en excès sur toute la grille : (b). |
| 4.2 | **(a)** | 0,75 | Un niveau inemployé rend la campagne plus prudente, jamais fausse. Le changer après coup rompt le gel. Le déclenchement de l'excès et q dépendent des mêmes lectures honnêtes. | Une règle conditionnelle est gelée maintenant et D4.2′ ne montre aucun dépassement. Ce serait une option nouvelle, non (b). |
| 5 | **(a)**, avec P(K ≠ mode) ≥ Δ | 0,80 | Aucune fiche n'a été servie, donc refaire le calcul d'admission est le seul coût. (b) rend licite le geste « les K statistiques les plus fortes ». | D5′ donne H_B : (b) devient défendable. Si K̂(X) retrouve presque toujours K, ni (a) ni (b) ne cachent K. |

**Ce qui est établi.** Seulement des identités et de l'arithmétique refaites ici, sous entrées illustratives (VÉRIFIÉ, calcul refait). Aucun résultat empirique.
1. max(1/m, Q) = 1/m dès que Q ≤ 1/m : (b′) contient (a).
2. Si A = 1 − p_sig, ΔA = 0 dès que p_sig ne bouge pas, quel que soit le mouvement de l'abstention.
3. À dose fixe, couvrir dose × q équivaut à couvrir q. Cette couverture ne dit rien de la discrimination.
4. À zéro alerte, une borne unilatérale exacte à 95 % au plus égale à 0,05 exige au moins 59 paires par strate.

Le profil « A stable, B mobile » reste RAPPORTÉ : c'est un calcul de conception, non audité ici.

**Ce qui n'est pas établi** (HYPOTHÈSE) :
- la lecture de A et sa population ;
- l'hypothèse 5 et le plan de lecture final ;
- le sens du biais de q en excès ;
- la supériorité du repéreur sur le recouvrement ;
- l'avantage que le saboteur tire de K ;
- le comportement de la règle de cohérence face au geste « les K plus fortes ».

Le niveau total d'erreur est absent des faits.

**Expérience à faire en premier : D2′.**

Elle passe en premier pour trois raisons :
- elle fixe ce que « reconnu » veut dire pour toute la campagne ;
- ses sorties (fausses alertes par m, strates perdues, plume du tiers) conditionnent la mesure de q (décision 3) et la probabilité d'entrer en régime d'excès (décision 4) ;
- elle porte sur des documents et des lecteurs réels, et non sur le simulateur, que six critiques jugent circulaire.

Deux actes écrits, sans coût, la précèdent :
1. la définition de A et la porte de puissance. Elles débloquent le gel du banc des tâches floues, qui n'attend aucune expérience ;
2. la lecture du protocole pour trancher l'hypothèse 5 et le plan de lecture. Elle choisit le type de paire nulle principal.

**Ce qui peut être réfuté :**
- six choix d'option, dont une option nouvelle, (c+), et deux options amendées, (b′) corrigée et (c′) ;
- six expériences. Trois peuvent renverser l'option qu'elles soutiennent : D3′, D4.1′ et D5′. D2′ ne renverse pas (b′) : sous H_A, (b′) coïncide avec (a). D4.2′ mène à une option nouvelle et n'est pas exécutable sans le niveau total. D1′ est le témoin lui-même.

FIN-DE-CELLULE