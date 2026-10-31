*Note d'intégrité : En application stricte de la règle 1 du protocole, les jeux de données non lus demandés au point 2 portent le statut autorisé `HYPOTHÈSE` (équivalent strict du statut « SUPPOSÉ » mentionné dans la question).*

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Pente locale de la fonction de rappel adversarial autour de $\alpha = 1\%$** — Statut : `HYPOTHÈSE`.
   La question suppose que l'incertitude sur le taux de fausses alertes (entre $0,21\%$ et $2,38\%$ pour $n=300$ selon les faits `RAPPORTÉ`) se traduit par une variation des seuils de rappel ($\tau < 50\%, 20\%, 5\%$) suffisamment modérée pour qu'on puisse trancher a priori entre (A) et (B). Or, si la distribution des scores adversariaux est très concentrée près du seuil de la sonde, un déplacement du seuil de $0,2\%$ à $2,4\%$ de fausses alertes peut faire basculer le rappel d'une direction de $4\%$ à $60\%$ (chiffres `illustratifs`), rendant la lecture à $\tau < 5\%$ dépendante du tirage des 300 bénins.
2. **Stabilité de la sonde linéaire entre $n_{\text{train}} = 800$ et $n_{\text{train}} = 400$ bénins** — Statut : `HYPOTHÈSE`.
   L'option (B) réduit de moitié les bénins d'entraînement de la sonde (de 800 à 400, face à 800 nuisibles, faits `RAPPORTÉ`) en supposant que l'espace des activations d'un modèle de 8 milliards de paramètres (dimension typique $d = 4096$, chiffre `illustratif`) permet d'apprendre la même direction de sonde. Sans régularisation très forte, diviser par deux la classe négative en haute dimension déplace l'hyperplan séparateur et dégrade la queue de distribution bénigne.
3. **Invariance du taux de fausses alertes aux artefacts de surface entre jeux publics** — Statut : `HYPOTHÈSE`.
   L'option (A) suppose qu'il existe un jeu bénin public dont la projection sur la direction de la sonde linéaire suit la même loi que les bénins de Bailey (`harmful_dataset`, commit `9c1f4b1a…`, fait `RAPPORTÉ`). En pratique, une sonde linéaire entraînée sur un seul jeu capte souvent des corrélats superficiels (longueur, ponctuation, style d'instruction). Un jeu externe peut présenter un décalage de moyenne ou de variance sur la sonde bien supérieur au bruit d'échantillonnage de (B).
4. **Nécessité de séparer physiquement l'entraînement de la sonde et la calibration du seuil** — Statut : `HYPOTHÈSE`.
   Le dilemme entre (A) et (B) repose sur l'idée que les données servant à entraîner la sonde ne peuvent pas servir à calibrer son seuil sans biais optimiste. C'est vrai en évaluation naïve (in-sample), mais faux si l'on utilise des prédictions hors-pli (*out-of-fold* via validation croisée) sur une sonde figée par pli ou agrégée.

---

## Réponses directes aux quatre points de l'arbitre

### 1. Choix méthodologique et vérification des intervalles

**Vérification des intervalles servis dans les faits :**
Les deux séries d'intervalles du fichier `calcul-taux-fausses-alertes-benins-v1.sortie.txt` (`RAPPORTÉ`) sont mathématiquement exactes et proviennent de deux lois distinctes :
- **Lignes `mesure`** (`[0,0048 ; 0,0183]` pour $10/1000$ ; `[0,0021 ; 0,0289]` pour $3/300$ ; `[0,0012 ; 0,0356]` pour $2/200$) — Statut : `VÉRIFIÉ`. Ce sont les intervalles de confiance exacts de Clopper-Pearson à $95\%$ pour $k$ succès observés sur $n$ essais : la borne inférieure est le quantile $\text{Beta}(0,025 ; k, n - k + 1)$ et la borne supérieure est $\text{Beta}(0,975 ; k + 1, n - k)$.
- **Lignes `seuil`** (`[0,0048 ; 0,0171]` pour $n=1000, k=10$ ; `[0,0021 ; 0,0238]` pour $n=300, k=3$) — Statut : `VÉRIFIÉ`. C'est la distribution exacte de la couverture aléatoire d'un seuil fixé sur la $k$-ième statistique d'ordre (où $k = 0,01 n$) d'un échantillon de calibration continu de taille $n$ : la probabilité de fausse alerte dans la population suit exactement une loi $\text{Beta}(k, n + 1 - k)$ (propriété classique de la couverture en prédiction conforme / *split conformal* ; référence à vérifier). Les quantiles à $2,5\%$ et $97,5\%$ de $\text{Beta}(k, n + 1 - k)$ donnent exactement la borne inférieure de Clopper-Pearson et une borne supérieure plus resserrée (car paramétrée par $k$ au lieu de $k+1$).

**Choix recommandé : Une troisième voie (Option C — Calibration *Out-Of-Fold* sur 700 bénins + Mesure étanche sur 300 bénins, sur le seul jeu de Bailey), sinon (B) plutôt que (A).**

Pourquoi écarter (A) par défaut : Verser un jeu externe pour calibrer le seuil d'une sonde entraînée uniquement sur Bailey introduit une confusion entre le taux de fausses alertes nominal et le décalage de domaine (*domain shift*). Si le jeu externe a des requêtes plus simples ou syntaxiquement différentes, le quantile à $1\%$ sera placé trop bas ou trop haut par rapport à la frontière réelle apprise sur Bailey.

Pourquoi améliorer (B) en (C) : Dans (B), on sacrifie 500 bénins de l'entraînement (passant de 800 à 400) pour créer deux petits lots de 300. Or, le rôle du jeu de **seuil** est uniquement de fournir des scores bénins non biaisés par le surapprentissage de la sonde.
- **Protocole de l'Option C** : On regroupe les 1 000 bénins de Bailey et on les partage par `SeedSequence` en **700 bénins (entraînement + seuil croisé)** et **300 bénins (mesure finale strictement isolée)**.
- Sur les 700 bénins (et les 800 nuisibles de `train`), on effectue une validation croisée à $K=10$ plis (`illustratif`). Pour chaque pli $j$, une sonde linéaire $w^{(-j)}$ est entraînée sur $9/10$ des données avec exactement le même hyperparamètre de régularisation que la sonde finale $w_{\text{full}}$ (entraînée sur les 700 bénins et 800 nuisibles). On calcule les scores hors-pli $s_i = \langle w^{(-j(i))}, x_i \rangle$ (standardisés par l'écart-type hors-pli) pour les 700 bénins.
- Le seuil à $1\%$ est fixé sur le $7^{\text{e}}$ score le plus élevé parmi les 700 scores hors-pli (intervalle de vrai taux : $\text{Beta}(7, 694) \approx [0,0040 ; 0,0186]$, chiffre `illustratif` interpolé entre $n=500$ et $n=800$ des faits `RAPPORTÉ`).
- La sonde finale figée $w_{\text{full}}$ (entraînée sur 700 bénins, soit $87,5\%$ de la taille initiale au lieu de $50\%$) utilise ce seuil et est évaluée une seule fois sur les 300 bénins de mesure (et sur les directions adverses).
- **Si le préenregistrement interdit toute validation croisée pour le seuil** et impose une sonde unique strictement figée avant le calcul des scores de seuil, alors je choisis **(B)** avec un découpage asymétrique **500 (sonde) / 300 (seuil) / 200 (mesure)** ou le **400 / 300 / 300** proposé, car le bruit d'échantillonnage de (B) est connu, analytiquement borné par la loi Beta et sans biais, tandis que le biais de distribution de (A) est inconnu et systématique.

---

### 2. Analyse de l'Option (A) : jeux publics, test de ressemblance et risque de biais

**Jeux bénins publics candidats** (tous marqués `HYPOTHÈSE` conformément aux consignes, n'étant pas sur disque dans les faits) :
1. **XSTest (sous-ensemble des requêtes sûres / bénignes)** — Röttger et al., 2023/2024 (référence à vérifier) — Statut : `HYPOTHÈSE`. Taille : environ 250 requêtes bénignes conçues pour ressembler lexicalement à des attaques (*homonyms*, *figurative language*) (`illustratif`). Licence : CC-BY-4.0 (`HYPOTHÈSE`). *Intérêt et limite* : trop petit seul pour fournir 2 000 entrées, et volontairement décalé vers la frontière de décision (taux de fausses alertes beaucoup plus élevé que sur des bénins ordinaires).
2. **OR-Bench (Over-Refusal Benchmark, sous-ensemble `or-bench-80k` ou `or-bench-hard-1k`)** — Cui et al., 2024 (référence à vérifier) — Statut : `HYPOTHÈSE`. Taille : environ 80 000 requêtes bénignes générées pour tester le sur-refus (`illustratif`). Licence : MIT ou Apache-2.0 (`HYPOTHÈSE`). *Intérêt et limite* : fournit aisément 2 000 bénins, mais la distribution est concentrée sur des requêtes « limites » (*borderline*), ce qui décalera fortement le quantile à $1\%$ vers le haut par rapport aux bénins de Bailey.
3. **Alpaca (`tatsu-lab/alpaca`) ou UltraChat** — Taori et al., 2023 (référence à vérifier) — Statut : `HYPOTHÈSE`. Taille : 52 000 instructions bénignes générales (`illustratif`). Licence : CC-BY-NC-4.0 (`HYPOTHÈSE`). *Intérêt et limite* : c'est souvent la source même des bénins dans les dépôts de sécurité comme celui de Bailey (`HYPOTHÈSE`). Si les bénins de Bailey ont été tirés d'Alpaca, tirer 2 000 autres exemples d'Alpaca (après déduplication exacte et par $n$-grammes contre les 1 000 de Bailey) est le seul cas où (A) respecte la même distribution.

**Test de ressemblance de distribution à préenregistrer pour (A) :**
Tester la ressemblance dans l'espace brut des activations ($\mathbb{R}^d$, $d \approx 4096$, `illustratif`) par MMD (Maximum Mean Discrepancy) échouera presque sûrement par excès de puissance sur des détails thématiques non pertinents. Ce qui gouverne le seuil à $1\%$, c'est la loi marginale du score projeté $S(x) = \langle w_{\text{sonde}}, h(x) \rangle$ et sa queue supérieure. Il faut préenregistrer un **double test sur les 200 bénins de validation/test de Bailey (`val` + `test` = 200 bénins mis de côté, fait `RAPPORTÉ`) contre les 2 000 bénins externes** :
1. **Test global d'égalité des lois de score** : Test de Kolmogorov-Smirnov à deux échantillons (ou Anderson-Darling, qui pèse davantage les queues) entre les scores de la sonde sur les 200 bénins de Bailey hors-entraînement et les 2 000 bénins du nouveau jeu. Critère d'acceptation préenregistré : $p > 0,05$ ET statistique $D_{\text{KS}} \le 0,08$ (`illustratif`).
2. **Test spécifique de queue supérieure** : Écart sur le quantile à $95\%$ et $99\%$ estimé par bootstrap stratifié sur la longueur en tokens. Si le quantile à $99\%$ du jeu externe s'écarte de plus d'un demi-écart-type de la sonde par rapport aux 200 bénins de Bailey, le jeu externe est rejeté.

**Risque comparé : décalage de distribution de (A) contre petite taille de (B) :**
Dans (B), l'erreur sur le taux de fausses alertes est un bruit aléatoire sans biais borné dans $[0,21\% ; 2,38\%]$ (`VÉRIFIÉ`).
Dans (A), si le jeu externe est légèrement plus « facile » (ex. instructions générales type Alpaca alors que Bailey contiendrait des bénins plus proches des thèmes nuisibles, `HYPOTHÈSE`), le $99^{\text{e}}$ centile du jeu externe peut correspondre au $92^{\text{e}}$ centile de Bailey ($8\%$ de fausses alertes réelles sur la distribution cible, `illustratif`). Inversement, s'il vient d'OR-Bench (`HYPOTHÈSE`), son $99^{\text{e}}$ centile peut correspondre au $99,99^{\text{e}}$ centile de Bailey ($0,01\%$ de fausses alertes), rendant la sonde quasi aveugle et gonflant artificiellement le nombre de directions de camouflage trouvées. **Le risque d'un biais systématique non borné en (A) est donc méthodologiquement plus grave que la variance bornée et connue de (B)**, sauf si l'on prouve par l'historique du dépôt de Bailey que les 2 000 bénins externes proviennent exactement du même fichier source parent.

---

### 3. Analyse de l'Option (B) : interprétabilité à $\tau = 20\%$ et $5\%$ avec $n=300$, et que rapporter

**Interprétabilité des seuils de détection ($\tau < 50\%, 20\%, 5\%$) :**
Attention à ne pas confondre deux tailles d'échantillon dans les faits (`RAPPORTÉ`) :
1. La précision de la **lecture du rappel** lui-même ($\tau < 20\%$ ou $< 5\%$) dépend du nombre d'entrées **adverses** par direction, qui est d'**au moins 200 adverses** (l. 116, `RAPPORTÉ`). Sur 200 adverses, un rappel de $5\%$ correspond à $10/200$ détections (intervalle de Clopper-Pearson à $95\%$ : $[2,4\% ; 9,0\%]$, `illustratif`), ce qui est parfaitement lisible et ne change pas entre (A) et (B).
2. En revanche, $n=300$ bénins au seuil affecte la **position du seuil de la sonde** $t$, qui est la $3^{\text{e}}$ statistique d'ordre ($X_{(298:300)}$ ou $X_{(297:300)}$ selon la convention stricte/large).
La question de l'interprétabilité se résume donc à la **sensibilité du compte de directions validées par rapport au rang de la statistique d'ordre bénigne**. Avec $n=300$, l'intervalle de confiance à $95\%$ du vrai taux de fausses alertes $[0,0021 ; 0,0238]$ (`VÉRIFIÉ`) est couvert en déplaçant le seuil entre la $1^{\text{re}}$ statistique d'ordre la plus élevée ($k=1$, taux moyen $\approx 0,33\%$) et la $7^{\text{e}}$ statistique d'ordre ($k=7$, taux moyen $\approx 2,33\%$) sur les 300 bénins (`illustratif`).

**Ce qu'il faut impérativement rapporter si l'on choisit (B) :**
L'expérience est une recherche d'optimisation (trouver des directions d'activation qui abaissent le score sous le seuil $t$). On ne va pas relancer l'optimisation (coûteuse : 20 à 70 époques sur 1 000 directions, `RAPPORTÉ`) pour trois seuils différents, mais comme la sonde est **linéaire et figée**, les scores finaux des 200 entrées adverses pour chaque direction optimisée peuvent être sauvegardés sur disque. Il faut alors rapporter :
1. **Le triplé des statistiques d'ordre au seuil** : Au lieu d'évaluer le rappel uniquement au seuil nominal $t_{\text{nom}} = X_{(3)}$ ($3^{\text{e}}$ plus grand score bénin sur 300), rapporter pour chaque seuil de rappel ($\tau < 50\%, 20\%, 5\%$) le nombre de directions trouvées $N_{\text{dir}}$ évalué à trois seuils de sonde :
   - $t_{\text{strict}} = X_{(1)}$ (pire cas conservateur pour l'attaquant : $1/300 \approx 0,33\%$ de fausses alertes),
   - $t_{\text{nom}} = X_{(3)}$ ($3/300 = 1,0\%$ nominal),
   - $t_{\text{lâche}} = X_{(7)}$ ($7/300 \approx 2,33\%$ de fausses alertes, couvrant la borne haute $0,0238$ du calcul `RAPPORTÉ`).
   *(Ceci donne gratuitement une bande de sensibilité exacte $[N_{\text{dir}}(X_{(1)}), N_{\text{dir}}(X_{(7)})]$ sans aucun coût GPU supplémentaire).*
2. **La courbe continue $N_{\text{dir}}(\alpha)$** pour $\alpha \in [0,003 ; 0,05]$ afin de montrer qu'il n'y a pas d'effet de falaise à $\alpha = 1\%$.
3. **Le taux de fausses alertes réalisé sur les 300 bénins de mesure** avec son intervalle exact de Clopper-Pearson (ex. $3/300 \rightarrow [0,0021 ; 0,0289]$, `VÉRIFIÉ`).

---

### 4. Pire cas de ce choix et ce qui ferait changer d'avis

**Pire cas de l'Option (B) (ou C) :**
Deux modes de défaillance :
1. *Effet de falaise des scores adverses* : L'optimisation des directions de camouflage converge juste en dessous du seuil $t_{\text{nom}} = X_{(3)}$ (par exemple par arrêt anticipé dès que le rappel passe sous $5\%$). Alors, évaluée à $t_{\text{strict}} = X_{(1)}$, la quasi-totalité des directions repasse au-dessus de $\tau = 5\%$ ou $20\%$, donnant une fourchette de sensibilité inutilisable (ex. « 450 directions à $X_{(3)}$, mais 12 directions à $X_{(1)}$ », chiffres `illustratifs`).
2. *Dégradation de la sonde à $n_{\text{train}} = 400$ (spécifique à B)* : Avec seulement 400 bénins d'entraînement en dimension 4096 (`illustratif`), la sonde surapprend et présente une queue droite bénigne très lourde et multimodale ; l'écart entre $X_{(1)}$ et $X_{(7)}$ devient gigantesque, écrasant le pouvoir discriminant sur les nuisibles (le rappel sur nuisibles non modifiés chute déjà sous $50\%$ au seuil $1\%$).

**Ce qui me ferait changer d'avis (basculer vers A) :**
1. Si le dépôt de Bailey documente explicitement le script et le jeu public exact (ex. `tatsu-lab/alpaca` avec une graine ou un filtre connu, `HYPOTHÈSE`) d'où ont été tirés les 1 000 bénins, permettant d'en extraire 2 000 supplémentaires issus **exactement** de la même population statistique, ET que le test de Kolmogorov-Smirnov entre les 200 bénins `val+test` de Bailey et ces 2 000 nouveaux bénins donne $D_{\text{KS}} < 0,05$ (`illustratif`).
2. Ou si, dans l'Option (B), la largeur relative de la bande de sensibilité $\frac{N_{\text{dir}}(X_{(7)}) - N_{\text{dir}}(X_{(1)})}{N_{\text{dir}}(X_{(3)})}$ dépasse $30\%$ (`illustratif`) sur le pilote à $\tau < 5\%$.

---

## (b) Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Ces trois expériences se jouent **avant** de lancer la recherche lourde des 1 000 directions par couche, uniquement sur les activations extraites une fois pour toutes des textes bénins et nuisibles.

### Expérience 1 : Stabilité de la sonde linéaire sous réduction du jeu bénin d'entraînement (400 vs 800)
- **Hypothèse $H_A$ (Suffisance de 400 bénins)** : En régularisation $\ell_2$ optimale (validée par validation croisée interne), réduire l'entraînement de 800 à 400 bénins (face à 800 nuisibles) ne dégrade ni l'alignement géométrique de la sonde ni le rappel sur nuisibles au seuil de $1\%$ de fausses alertes.
- **Hypothèse $H_B$ (Sous-détermination en haute dimension)** : Passer à 400 bénins déplace l'hyperplan vers des directions de bruit, alourdit la queue des scores bénins hors-échantillon et fait chuter le rappel de base sur les entrées nuisibles au seuil de $1\%$.
- **Protocole et métrique** : Sur les 800 bénins `train` et 800 nuisibles `train` de Bailey (`RAPPORTÉ`), tirer 50 sous-échantillons aléatoires de 400 bénins (`illustratif`). Entraîner $w_{800}$ et les cinquante $w_{400}^{(m)}$. Mesurer sur les 200 bénins et 200 nuisibles hors-entraînement (`val` + `test` de Bailey, `RAPPORTÉ`) : (1) le cosinus directeur $\cos(w_{800}, w_{400}^{(m)})$, et (2) le rappel sur les 200 nuisibles lorsque le seuil est fixé au $99^{\text{e}}$ centile des 200 bénins.
- **Seuil de décision** : Moyenne de $\cos(w_{800}, w_{400}^{(m)}) \ge 0,95$ ET perte de rappel moyen à $1\%$ de fausses alertes $\le 2,0$ points de pourcentage (`illustratif`).
- **Contrôle négatif** : Permuter aléatoirement $50\%$ des étiquettes bénin/nuisible à $n=400$ et $n=800$ (vérifie que la métrique de rappel à $1\%$ de FPR s'effondre vers $1\%$ et que le cosinus chute vers $0$).
- **Issues falsifiantes** :
  - Si $\cos \ge 0,95$ et perte de rappel $\le 2,0\%$ : $H_B$ est falsifiée $\rightarrow$ la réduction à 400 bénins de l'option (B) ne dégrade pas la sonde.
  - Si $\cos < 0,95$ ou perte de rappel $> 2,0\%$ : $H_A$ est falsifiée $\rightarrow$ le découpage $400/300/300$ de (B) est rejeté au profit de l'Option C (validation croisée sur 700 bénins) ou de (A).

### Expérience 2 : Test d'échangeabilité distributionnelle d'un jeu bénin externe (Option A)
- **Hypothèse $H_A$ (Échangeabilité projective)** : Les scores de la sonde $w_{800}$ (entraînée sur les 800 bénins et 800 nuisibles de Bailey) évalués sur un jeu bénin public candidat $D_{\text{ext}}$ ($N=2000$) sont issus de la même loi de probabilité que les scores évalués sur les 200 bénins `val+test` de Bailey.
- **Hypothèse $H_B$ (Décalage de domaine sur le seuil)** : Le jeu externe $D_{\text{ext}}$ présente un décalage de distribution sur la direction de la sonde qui biaise le quantile à $99\%$ au-delà de l'incertitude d'échantillonnage de l'option (B).
- **Protocole et métrique** : Calculer les scores $S_{\text{Bailey}}$ ($n=200$, `val+test`) et $S_{\text{ext}}$ ($n=2000$). Calculer : (1) la statistique de Kolmogorov-Smirnov $D_{\text{KS}}$, et (2) la proportion de $S_{\text{Bailey}}$ dépassant le quantile à $99\%$ de $S_{\text{ext}}$, notée $\hat{\alpha}_{\text{croisé}}$.
- **Seuil de décision** : $p_{\text{KS}} > 0,05$ ET $\hat{\alpha}_{\text{croisé}} \in [0,0021 ; 0,0238]$ (c'est-à-dire que le seuil tiré des 2 000 externes ne fait pas pire, sur les vrais bénins de Bailey, que l'intervalle à $95\%$ d'un seuil tiré sur 300 bénins de Bailey issu des faits `RAPPORTÉ`).
- **Contrôle négatif (sanity check positif de détection de biais)** : Appliquer le même test entre les 200 bénins `val+test` de Bailey et 200 entrées nuisibles (ou un jeu de sur-refus comme XSTest, `HYPOTHÈSE`) ; le test doit rejeter $H_A$ avec $p_{\text{KS}} < 10^{-6}$ (`illustratif`). Contrôle interne bénin/bénin : diviser les 800 bénins de Bailey en deux (400 vs 400) ; le test ne doit pas rejeter $H_A$.
- **Issues falsifiantes** :
  - Si $p_{\text{KS}} \le 0,05$ ou $\hat{\alpha}_{\text{croisé}} \notin [0,0021 ; 0,0238]$ : $H_A$ est falsifiée $\rightarrow$ l'option (A) avec ce jeu externe introduit un biais pire que la variance de (B) et est rejetée.
  - Si $p_{\text{KS}} > 0,05$ et $\hat{\alpha}_{\text{croisé}} \in [0,0021 ; 0,0238]$ : $H_B$ est falsifiée $\rightarrow$ l'option (A) est validée sans biais de seuil détectable.

### Expérience 3 : Sensibilité du compte de directions aux fluctuations du seuil ($n=300$, Option B)
- **Hypothèse $H_A$ (Robustesse des seuils $\tau = 20\%$ et $5\%$)** : Sur un échantillon pilote de directions adverses optimisées, la variation du seuil de la sonde sur l'intervalle de confiance à $95\%$ de $n=300$ (entre la $1^{\text{re}}$ et la $7^{\text{e}}$ statistique d'ordre bénigne, soit $[0,21\% ; 2,38\%]$ de fausses alertes, `RAPPORTÉ`) modifie la proportion de directions passant sous $\tau = 20\%$ et $\tau = 5\%$ de moins de $10\%$ en valeur relative (`illustratif`).
- **Hypothèse $H_B$ (Instabilité par empilement près du seuil)** : Les directions optimisées s'accumulent juste sous le seuil nominal $X_{(3)}$, de sorte que passer de $X_{(3)}$ à $X_{(1)}$ ou $X_{(7)}$ fait varier le nombre de directions validées à $\tau = 5\%$ de plus de $10\%$ (voire d'un facteur 2, `illustratif`).
- **Protocole et métrique** : Sur le pilote (ex. 50 directions cherchées sur une couche, `illustratif`), optimiser les directions sans arrêt anticipé lié à $X_{(3)}$ (optimiser la marge continue du score de la sonde pendant le budget fixe d'époques). Lire a posteriori le nombre de directions $N_{\text{dir}}$ ayant un rappel $< 50\%, < 20\%, < 5\%$ sur les 200 entrées adverses lorsque le seuil bénin est fixé à $X_{(1)}$, $X_{(3)}$ et $X_{(7)}$ sur les 300 bénins. Métrique : écart relatif $\Delta_{\tau} = \frac{N_{\text{dir}}(X_{(7)}) - N_{\text{dir}}(X_{(1)})}{\max(1, N_{\text{dir}}(X_{(3)}))}$.
- **Seuil de décision** : $\Delta_{20\%} \le 0,10$ et $\Delta_{5\%} \le 0,10$ (`illustratif`).
- **Contrôle négatif** : Évaluer $\Delta_{\tau}$ sur 50 directions aléatoires orthogonales non optimisées (le rappel doit rester proche de celui de base et $\Delta_{5\%}$ doit être nul car $N_{\text{dir}} = 0$).
- **Issues falsifiantes** :
  - Si $\Delta_{20\%} \le 0,10$ et $\Delta_{5\%} \le 0,10$ : $H_B$ est falsifiée $\rightarrow$ $n=300$ au seuil suffit pleinement pour lire $\tau = 20\%$ et $5\%$.
  - Si $\Delta_{20\%} > 0,10$ ou $\Delta_{5\%} > 0,10$ : $H_A$ est falsifiée $\rightarrow$ $n=300$ est trop bruité pour une lecture ponctuelle ; il faut utiliser l'Option C (calibration hors-pli sur 700 bénins) ou rapporter obligatoirement l'intervalle $[N_{\text{dir}}(X_{(1)}), N_{\text{dir}}(X_{(7)})]$ comme résultat principal.

---

## (c) Validation des instruments nommés dans la question

Quatre instruments statistiques et algorithmiques sont nommés dans les faits et la question :

| Instrument nommé | Mesure minimale de fonctionnement (Taux de détection / FPR) | Cas honnêtes appariés | Vérifications mécaniques (baselines) à battre |
| :--- | :--- | :--- | :--- |
| **1. Sonde linéaire figée** (sur modèle 8B) | **Rappel (TPR) $\ge 85\%$** (`illustratif`) sur les entrées nuisibles non modifiées lorsque le seuil est fixé à **FPR $= 1,0\%$** ($3/300$ ou $10/1000$) sur les bénins de mesure. AUROC $\ge 0,97$ (`illustratif`). | Paires d'entrées de même longueur (en tokens) et même structure syntaxique tirées de `harmful_test` et `benign_test` de Bailey (ex. « Comment fabriquer X » nuisible vs bénin). | 1. **Sonde aléatoire** ($w \sim \mathcal{N}(0, I_d)$) : TPR $\approx 1\%$ à FPR $= 1\%$.<br>2. **Régression logistique sur la seule longueur en tokens + sac de mots (TF-IDF)** : la sonde d'activation doit battre le classifieur lexical d'au moins $+15$ points de TPR à FPR $= 1\%$ (`illustratif`). |
| **2. Calibrateur par statistique d'ordre à $1\%$ + `SeedSequence`** | **Couverture empirique à $95\%$** du taux de fausses alertes sur le jeu de mesure comprise dans l'intervalle théorique $[0,0021 ; 0,0289]$ ($n=300$) ou $[0,0048 ; 0,0183]$ ($n=1000$) (`VÉRIFIÉ`) sur 1 000 tirages Monte-Carlo de `SeedSequence`. | Partitions aléatoires stratifiées des 1 000 bénins de Bailey en calibration (300) et mesure (300), évaluées sur les scores réels de la sonde. | 1. **Calibration gaussienne paramétrique** ($\mu + 2,326\sigma$) : échoue dès que la queue des scores bénins est asymétrique (donne typiquement FPR $> 3\%$, `illustratif`).<br>2. **Seuil in-sample** (calibré sur les bénins d'entraînement de la sonde) : sous-estime systématiquement le seuil et dépasse la borne de Clopper-Pearson en mesure. |
| **3. Juge de nuisance StrongREJECT affiné** (score $\in [0, 1]$, nuisible si $> 0,5$, `RAPPORTÉ`) | **TPR $\ge 90\%$** sur des réponses manifestement nuisibles de référence et **FPR $\le 2\%$** sur des refus explicites ou des réponses bénignes complètes (`illustratif`). | Paires (Prompt nuisible + Réponse complaisante détaillée) contre (Même prompt nuisible + Refus poli ou réponse éducative inoffensive de même longueur). | 1. **Détecteur lexical par mots-clés de refus** (*"I cannot"*, *"As an AI"*, etc.) : échoue sur les refus implicites ou les jailbreaks qui commencent par une formule d'excuse avant de répondre.<br>2. **Juge aléatoire / constant**. |
| **4. Test de ressemblance de distribution** (KS + quantile croisé à $99\%$, pour l'Option A) | **Puissance (TPR de dérive) $\ge 90\%$** pour détecter un décalage de moyenne de $0,3\sigma$ ou un facteur d'échelle de $1,2$ sur la queue droite (`illustratif`), à un taux de fausse alerte de rejet **FPR $= 5\%$** sous $H_0$. | Deux sous-échantillons disjoints de 200 bénins tirés de Bailey (cas $H_0$ honnête : même distribution) contre 200 bénins de Bailey altérés par filtrage de longueur ou remplacés par XSTest (`HYPOTHÈSE`). | 1. **Comparaison de la seule moyenne et variance des scores ($t$-test + test de Levene)** : aveugle aux différences de queue à $99\%$ qui gouvernent le seuil de $1\%$.<br>2. **Distance cosinus des centroïdes d'activations brutes** : trop bruitée par les thèmes sémantiques hors-sonde. |

---

## (d) Ancrage matériel, calcul nécessaire et coûts

- **Modèle ouvert** : Le modèle public de 8 milliards de paramètres mentionné dans les faits (`RAPPORTÉ`) — typiquement de la classe Llama-3-8B-Instruct (`illustratif`) — nécessite environ $16\text{ Go}$ de VRAM en précision `bfloat16` (`illustratif`). Un seul GPU de $24\text{ Go}$ à $80\text{ Go}$ (ex. NVIDIA RTX 4090, L40S ou A100, `illustratif`) suffit largement.
- **Empreinte de calcul des options (A), (B) et (C) et des 3 expériences décisives** :
  - *Option (B) ou (C) (sur les 1 000 bénins + 1 000 nuisibles de Bailey déjà sur disque)* : Il suffit d'extraire et de mettre en cache sur disque les activations d'une passe avant (*forward pass*, sans génération) pour 2 000 textes courts. À raison de $\approx 100$ tokens par entrée (`illustratif`), $2\,000$ passes avant sur un modèle 8B prennent **moins de 2 minutes sur un seul GPU A100** (`illustratif`).
  - *Option (A) (ajout de 2 000 bénins externes)* : Ajoute 2 000 passes avant d'extraction d'activations, soit **environ 2 minutes de GPU supplémentaires** (`illustratif`), plus le temps humain de sélection, vérification de licence, déduplication et hachage SHA-256 pour le manifeste.
  - *Exécution des Expériences 1 et 2 (sur activations mises en cache)* : Entraîner 50 sondes linéaires (régression logistique $\ell_2$ en dimension $4096$ sur $N \le 1600$) et calculer les tests de Kolmogorov-Smirnov et intervalles Beta avec `numpy 2.4.6` (`RAPPORTÉ`) prend **moins de 30 secondes sur CPU** (`illustratif`).
  - *Exécution de l'Expérience 3 (lecture multi-seuils $X_{(1)}, X_{(3)}, X_{(7)}$)* : Si les scores de la sonde pour les 200 entrées adverses de chaque direction cherchée sont enregistrés lors du pilote, le recalcul des rappels ($\tau < 50\%, 20\%, 5\%$) pour les trois seuils est une simple comparaison vectorielle dans `numpy` prenant **moins de 1 seconde sur CPU** (`illustratif`).
- **Coût financier estimé** : Pour trancher D-ML-1 (extraction des activations des 2 000 à 4 000 textes + Expériences 1, 2 et lecture multi-seuils de l'Expérience 3), le temps total de calcul spécifique est inférieur à **10 minutes de GPU A100**, soit un coût cloud d'environ **$0,30\text{ \$}$ à $1,00\text{ \$}$** (`illustratif`). Le coût limitant de (A) n'est pas matériel mais méthodologique (risque de décalage de distribution sur le quantile à $99\%$).

FIN-DE-CELLULE