> You are powered by the model named Opus 5.5.

# Règle « moniteur invalide » : contre-lecture de la re-dérivation et lecture d'antériorité de Singh, version 1

- **Auteur** : Claude Opus 5.5, contre-lecteur et lecteur d'antériorité (GO-2026-11-21-59, décisions E-2 et E-3). Je n'ai écrit ni la re-dérivation, ni l'erratum, ni leurs programmes. La phrase en tête est celle de mon invite système qui nomme mon modèle.
- **Date** : 21 novembre 2026. Dépôt à `04af9822c`. Pièce de travail ; aucun résultat d'expérience, aucun appel payant, ni commit ni poussée.
- **Pièces contre-lues** (empreintes vérifiées par leurs compagnons) :
  - `rederivation-opus-v1.md` (`a5ff23f2…4cc4`), `calcul_regle_moniteur_invalide_v1.py` (`21c37cd9…1617`), `sortie_calcul_regle_moniteur_invalide_v1.txt` (`5e626061…031b`), même dossier ;
  - `docs/notes/science-de-la-detection-v1/reponse-fable-science-de-la-detection-v1-erratum-1.md`, `calculs-science-de-la-detection-erratum-1-v1.py` (`26ec7fec…4c44`) et sa sortie `.txt` (`c3e74929…09e6`).
- **Source lue en entier** : Singh, « Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries », arXiv 2610.18948v1, 66 pages, `docs/sources/pdf/science-de-la-detection-v1/erratum-1/2610.18948v1.pdf` (`53557a25…9f7d`, compagnon vérifié). Texte extrait par `pdftotext -layout`, lu de la première à la dernière page ; les figures n'ont pas été regardées. Les numéros de page ci-dessous sont ceux imprimés, égaux au rang dans le fichier.
- **Mes contrôles** : `calcul_contre_lecture_v1.py` (`7c68b230…893f`) et `sortie_calcul_contre_lecture_v1.txt` (`fa5f2f4c…5f10`), même dossier, scellés à côté. Formules fermées, aucun tirage. Marque [contrôle, n] = bloc n de cette sortie.

## Verdict

1. **Les deux preuves tiennent.** Garantie 1 (fausse annonce, inégalité de Ville) : chaque pas est juste. Garantie 2 (excès accumulé avant l'annonce) : les trois pas sont justes. Il manquait un pas implicite : la borne doit croître avec m, pour que sa valeur en m = n couvre tous les m ≤ n. Je le démontre au § 1.3 et je le vérifie [contrôle, 1]. La preuve ne suppose pas ce qu'elle prouve : le terme de variance est linéaire dans le compte inconnu, et la seule hypothèse sur le tirage porte sur le dispositif, pas sur l'agent.
2. **Les deux programmes se rejouent à l'octet.** Re-dérivation : sortie identique, empreinte `5e626061…031b`, environ 11 minutes. Erratum : sortie identique, empreinte `c3e74929…09e6`, environ 23 secondes. Environnement : Python 3.13.18, numpy 2.4.6, scipy 1.17.1.
3. **La règle à douze taux donne bien l'ordre en racine sur l'horizon d'emploi, et le pas manquant a maintenant une esquisse de preuve.** Le passage à une fraction auditée au hasard se réduit à deux pièces (§ 2) : la borne sur trajectoire du mélange à observation complète, appliquée à la seule suite des épisodes audités ; une martingale exponentielle exacte du tirage, qui ramène cette suite à toute la suite avec le facteur 1/q. Pour la grille de douze taux, la borne sur trajectoire est démontrée au plus 1,25 κ √(2ρ₀(1−ρ₀)·L·N) jusqu'à environ 2,6·10⁷ audits [contrôle, 2]. La borne qui en sort suit celle de la re-dérivation à 1 à 17 % près, de 10³ à 10⁷ épisodes [contrôle, 3]. Réserves : l'horizon est fixé d'avance, l'esquisse n'est pas contre-lue, rien n'est vérifié en Lean.
4. **Singh, en trois points.**
   - (a) la règle à mélange qui borne l'excès cumulé face à un adversaire adaptatif : **occupé** ;
   - (b) son emploi avec une fraction auditée au hasard, sous une condition sur ce que l'agent sait des tirages : **partiellement occupé**, et plus que l'erratum ne le dit : les « challenge bits » privés de son théorème 9 (p. 21) portent la condition sur le tirage courant ;
   - (c) la perte « endommagé et non signalé » jugée par un oracle extérieur au mode d'attaque : **partiellement occupé**. L'arbitre de confiance distinct de l'interface d'attaque y est ; la perte « raté du moniteur » n'y est pas.
5. **Une phrase de l'erratum ne tient pas** : « une recherche de motifs sur ses 66 pages ne rend aucun audit par tirage ». Les motifs cherchés ne contenaient pas « challenge », le mot de Singh (§ 4).

## 1. Contre-lecture des preuves

Notations de la re-dérivation (§ 1) : X_t = D_t(1 − S_t), A_t le tirage d'audit, 𝓕_{t−1} le passé complet, 𝓖_t = 𝓕_{t−1} ∨ σ(X_t), M, N, T les comptes. Les hypothèses sont (H-a) tirage frais, (H-b) oracle exact, (H-c) grille au-dessus de ρ₀ et (H-0) nulle épisode par épisode.

### 1.1 Garantie 1, pas à pas

| Pas | Ce qui est affirmé | Vérification |
|---|---|---|
| Facteur | F_t = 1 + A_t(ℓ_ρ(X_t) − 1) | Vaut 1 si A_t = 0 et ℓ_ρ(X_t) sinon. Juste. Positif et borné, donc intégrable. |
| Espérance sachant 𝓖_t | E[F_t ∣ 𝓖_t] = 1 + q(ℓ_ρ(X_t) − 1) | X_t est 𝓖_t-mesurable et P(A_t = 1 ∣ 𝓖_t) = q par (H-a) ; on sort ℓ_ρ(X_t) de l'espérance conditionnelle. Juste. |
| Espérance sachant 𝓕_{t−1} | 1 + q(p_t − ρ₀)(ρ − ρ₀)/(ρ₀(1 − ρ₀)) | Je refais le calcul : E[ℓ_ρ(X_t) ∣ 𝓕_{t−1}] − 1 = p_t(ρ/ρ₀ − (1−ρ)/(1−ρ₀)) + (1−ρ)/(1−ρ₀) − 1 = (ρ − ρ₀)(p_t − ρ₀)/(ρ₀(1−ρ₀)). Juste. La tour 𝓕_{t−1} ⊂ 𝓖_t est licite. |
| Signe | ≤ 1 | p_t ≤ ρ₀ par (H-0) et ρ ≥ ρ₀ par (H-c). Juste. Égalité, donc martingale, si p_t = ρ₀. |
| Surmartingale | Π F_s, puis la moyenne des produits | Les facteurs passés sont 𝓕_{t−1}-mesurables. Une combinaison convexe de surmartingales positives sur la même filtration en est une. Juste. Le produit des moyennes est le cas ρ = ρ̄, car ℓ_ρ est affine en ρ (vérifié aussi par l'erratum, bloc A, écart 1e-16). |
| Ville | P(sup W ≥ 1/α) ≤ α | Surmartingale positive, W₀ = 1. Juste. La filtration est celle du monde entier, non celle de l'observateur ; c'est licite, puisque W est calculable à partir des seules observations. |

**Contre-exemples du § 2.3** : je les ai refaits. L'agent qui endommage exactement les épisodes audités a p_t = q ≤ ρ₀ et une annonce certaine : 3 audits positifs suffisent, car 3,125³ > 20. La fausse alerte de l'oracle déplace bien la nulle à ρ₀ + ε₊(1 − ρ₀) : la probabilité observée p + ε₊(1 − p) croît en p. Je n'ai rien à redire.

### 1.2 Garantie 2, pas à pas

| Pas | Ce qui est affirmé | Vérification |
|---|---|---|
| 1 | Sans annonce, a_k M_m − b_k N_m < L pour **chaque** k | Chaque terme de la somme positive est au plus W_m < 1/α. Juste, et déterministe : il ne coûte rien en probabilité. |
| 2 | Z_m = exp(−λ Σ(A_t − q)c_t − Σ φ_q(λc_t)) est une martingale d'espérance 1 | c_t est 𝓖_t-mesurable. A_t est une Bernoulli(q) indépendante de 𝓖_t : pour une variable binaire, (H-a) équivaut à cette indépendance. Je refais le calcul : E[exp(−s(A − q))] = (1 − q)e^{sq} + q e^{−s(1−q)} = e^{sq}(1 − q + q e^{−s}) = e^{φ_q(s)}. Juste. Ville, avec β, sur un seul événement pour tous les m. |
| 3 | T_m·A_{k,λ} < L + log(1/β)/λ + m·C_{k,λ} | J'ai redéveloppé : q(a T − b m) − [ℓ_β + T φ(λu) + (m − T)φ(−λb)]/λ < L donne exactement A = q a − [φ(λu) − φ(−λb)]/λ et C = q b + φ(−λb)/λ. Juste. |
| Union | Aucune union sur k : log(1/β) suffit | Juste, parce que (k, λ) est choisi avant les données, en fonction de (n, q, ρ₀, α, β) seulement. Le minimum pris sur une grille de λ reste valide : chaque λ fixé donne une borne valide. |

**Ce qui n'est pas une faute.** À n = 10⁷ et q = 0,05, la re-dérivation donne 23 105,8 et l'erratum 23 105,4 ; mon programme donne 23 105,5. Les trois ne cherchent pas λ sur la même grille, et chacune de ces valeurs est une borne valide.

### 1.3 Le pas implicite : la borne croît avec m

Le théorème donne, pour tout m < τ, T_m − ρ₀m < c + m·(C/A − ρ₀). Il en conclut « pour tout m ≤ n, < B(n) », la valeur en m = n. Il faut pour cela que la pente soit positive. Elle l'est :

C/A ≥ b/a ⟺ aC ≥ bA (car A, a > 0) ⟺ u·φ_q(−λb) + b·φ_q(λu) ≥ 0,

ce qui est vrai, car u, b > 0 et φ_q ≥ 0 (Jensen : φ_q est le logarithme de la fonction génératrice d'une variable centrée). Comme b/a = r* > ρ₀, la pente vaut au moins r* − ρ₀ > 0. Contrôle : sur cinq valeurs de q, les douze taux et 300 valeurs de λ, le plus petit écart C/A − b/a vaut 9·10⁻¹⁰ ≥ 0 [contrôle, 1].

### 1.4 Remarques mineures (aucune ne change un verdict)

- **Horizon fixé d'avance.** B(n) vaut pour un n choisi avant le service, parce que (k, λ) en dépend. Une garantie simultanée pour plusieurs horizons demande une union, par exemple β_j = β/(j(j+1)) sur des horizons qui doublent : elle coûte un facteur en log log n.
- **§ 3.4, « 2 300/q ».** La formule écrite juste avant, ε ≈ √(2L(1−ρ₀)/(qρ₀n)) avec L = log(16/α), donne environ 1 660/q pour ε = 0,25. « 2 300/q » correspond à L + log(1/β) à la place de L. C'est un ordre de grandeur, sans effet sur la conclusion.
- **§ 3.6, oublis de l'oracle.** La majoration [B(n) + ρ₀n]/(1 − ε₋) − ρ₀n traite le compte vu comme exactement (1 − ε₋) fois le vrai. Sur une trajectoire, il faut un terme de concentration de plus, d'ordre √(T log(1/β')), ou bien lire la phrase en espérance.
- **§ 3.5, « auditer quatre fois moins double l'excès inévitable ».** C'est vrai de l'ordre √(n/q). Dans la table, le rapport entre q = 0,05 et q = 0,20 vaut 2,9 à 3,1 (18 contre 55 ; 73 contre 211), à cause du terme binomial qui ne dépend pas de q. L'erratum reprend la phrase (§ 2) ; même remarque.
- **§ 3.5, borne inférieure.** Elle suppose que la règle n'observe que (A, S, A·D). Si elle observe aussi S sur tous les épisodes, l'argument tient encore : l'attaquant peut garder la loi de S inchangée. À dire en une ligne.
- **Erratum, § 2 et bloc F.** Les chiffres recopiés (136,1 ; 252,4 ; 483,7 ; « entre 5,3 et 6,4 » ; « entre 5,5 et 7,5 » ; 93, 331, 28 audits ; 0,014 et 0,022) sont bien ceux de sa sortie. L'horizon « 3·10⁷ / 1,3·10⁸ » vient d'un critère heuristique (deux fois le plus petit écart). Mon lemme G (§ 2.3) donne une plage démontrée plus large, environ 1,3·10⁸ épisodes à q = 0,20 et 5·10⁸ à q = 0,05. Les deux sont compatibles ; celle de l'erratum est prudente.

## 2. Le pas non démontré : esquisse de preuve du passage à une fraction auditée

### 2.1 Ce qui manque exactement

Le théorème du § 3.1 de la re-dérivation est déjà une borne valide **pour la règle auditée**, et l'erratum ne le dit pas assez (§ 4 de l'erratum : « le passage à une fraction auditée au hasard … n'est démontré nulle part »). Ce qui manque est seulement l'énoncé analytique : B(n) ≤ c·√(n·log/q) sur l'horizon d'emploi. Je l'obtiens par une réduction plus simple, qui ne demande pas d'analyser le minimum en (k, λ).

### 2.2 L'identité de réduction

Pour tout m :

  q·(T_m − ρ₀m) = (M_m − ρ₀N_m) + Σ_{t≤m} d_t,  avec d_t = (q − A_t)(X_t − ρ₀).

Pour la vérifier, on développe : M − ρ₀N = Σ A_t(X_t − ρ₀) et q(T − ρ₀m) = Σ q(X_t − ρ₀). La différence est Σ(q − A_t)(X_t − ρ₀).

- **Premier terme : observation complète sur les seuls audits.** Sans annonce, pour chaque k, a_k M − b_k N < L. Donc M − ρ₀N < L/a_k + (r*_k − ρ₀)N, et, de façon déterministe :

  M_m − ρ₀N_m < g(N_m),  g(N) = min_k [L/a_k + (r*_k − ρ₀)N].

  C'est la borne sur trajectoire à audit complet (la ligne « audit 1,00 » de l'erratum, bloc C). g est croissante, puisque r*_k > ρ₀.
- **Second terme : martingale exacte du tirage.** Sachant 𝓖_t, λd_t = −s(A_t − q) avec s = λ(X_t − ρ₀). Donc E[exp(λd_t) ∣ 𝓖_t] = exp(φ_q(λ(X_t − ρ₀))), exactement. Par Ville, avec probabilité ≥ 1 − β₁, pour tout m :

  Σ d_t < log(1/β₁)/λ + [T_m φ₁ + (m − T_m) φ₀]/λ,  φ₁ = φ_q(λ(1−ρ₀)), φ₀ = φ_q(−λρ₀).
- **Nombre d'audits.** Sous (H-a), A_t est indépendant de 𝓕_{t−1}, donc N_n suit exactement Bin(n, q). Avec probabilité ≥ 1 − β₂, N_n ≤ N⁺, le quantile 1 − β₂ (ou une borne de Bernstein : qn + √(2qnℓ₂) + ℓ₂/3).

**Proposition R (esquisse).** Sous (H-a) et (H-b), pour toute politique qui ne voit pas le tirage courant, avec probabilité ≥ 1 − β₁ − β₂, pour tout m ≤ n avant l'annonce, Δ_m = T_m − ρ₀m vérifie :

  Δ_m < [g(N⁺) + log(1/β₁)/λ + n(ρ₀φ₁ + (1−ρ₀)φ₀)/λ] / [q − (φ₁ − φ₀)/λ],

pour tout λ > 0 fixé d'avance tel que le dénominateur soit positif.

*Preuve.* On écrit T_m = ρ₀m + Δ_m dans le terme de variance : T φ₁ + (m−T)φ₀ = m(ρ₀φ₁ + (1−ρ₀)φ₀) + Δ(φ₁ − φ₀). On passe Δ à gauche. Ensuite, m ≤ n et ρ₀φ₁ + (1−ρ₀)φ₀ ≥ 0, et g(N_m) ≤ g(N_n) ≤ g(N⁺). Si Δ_m ≤ 0, il n'y a rien à prouver. ∎

Le terme de variance est encore linéaire en Δ : pas de cercle, comme dans la re-dérivation.

### 2.3 Lemme G : la borne sur trajectoire de la grille de douze taux est en racine

Posons ρ = ρ₀(1 + ε). Deux inégalités élémentaires :

- a = log(1 + ε/(1 − ρ)) ≥ ε/(1 − ρ + ε) = ε/((1 − ρ₀)(1 + ε)), par log(1+x) ≥ x/(1+x). Donc 1/a ≤ (1 − ρ₀)(1 + ε)/ε.
- r* − ρ₀ = ((1−ρ₀)b − ρ₀u)/a. On utilise −log(1−y) ≤ y + y²/(2(1−y)) avec y = ρ₀ε/(1−ρ₀), et log(1+ε) ≥ ε − ε²/2. On obtient (1−ρ₀)b − ρ₀u ≤ (ρ₀ε²/2)(1 − ρ₀ε)/(1 − ρ), donc r* − ρ₀ ≤ (ρ₀ε/2)·(1+ε)(1−ρ₀)(1−ρ₀ε)/(1−ρ).

On en tire L/a + (r* − ρ₀)N ≤ κ(ε)·[L(1−ρ₀)/ε + Nρ₀ε/2], où κ(ε) → 1 quand ε → 0. Posons ε*(N) = √(2L(1−ρ₀)/(ρ₀N)). La grille ε_j = 4·2^{−j} contient un ε_j dans [ε*, 2ε*) dès que ε* ∈ [ε_min, 2]. Sur cet intervalle, la fonction entre crochets vaut au plus 2,5/2 fois son minimum. D'où :

  **g(N) ≤ 1,25·κ(2ε*)·√(2ρ₀(1−ρ₀)·L·N)** pour N entre 25 et 2,6·10⁷ audits environ (ρ₀ = 0,10, α = 0,05, L = log 240).

Contrôle sur ce domaine, de 2 % en 2 % : rapport g(N)/borne ≤ 0,843 [contrôle, 2]. Valeurs exactes : g(N)/√(2ρ₀(1−ρ₀)LN) vaut 1,14 à N = 100, 1,04 à 10⁴, 1,02 à 10⁷.

### 2.4 L'ordre en racine qui en sort

On borne φ_q par q(e^{−s} − 1 + s), ce qui découle de log(1+x) ≤ x, puis e^{−s} − 1 + s ≤ (s²/2)e^{|s|}. Pour λ petit, cela donne n(ρ₀φ₁ + (1−ρ₀)φ₀)/λ ≤ nqλρ₀(1−ρ₀)e^{λρ₀}/2 et un dénominateur ≥ q(1 − λ(1−ρ₀)²/2). On prend λ = √(2 log(1/β₁)/(nqρ₀(1−ρ₀))), qui tend vers 0. Avec N⁺ = qn(1 + o(1)) :

  Δ_m ≤ √(2ρ₀(1−ρ₀)·n/q) · [1,25·κ·√(log(K/α)) + √(log(1/β₁))] · (1 + o(1)).

C'est l'ordre √(n ρ₀(1−ρ₀)/q), celui de la borne inférieure du § 3.5 de la re-dérivation. Contrôle [contrôle, 3], borne de la proposition R calculée exactement (β₁ = 0,09, β₂ = 0,01) :

| q | n | Proposition R | B(n) de la re-dérivation (β = 0,10) | R / échelle | B(n) / échelle |
|---|---|---|---|---|---|
| 0,20 | 1 000 | 146,8 | 136,1 | 6,92 | 6,42 |
| 0,20 | 16 000 | 495,8 | 483,7 | 5,84 | 5,70 |
| 0,20 | 10⁷ | 11 257,9 | 11 159,6 | 5,31 | 5,26 |
| 0,05 | 1 000 | 370,4 | 317,9 | 8,73 | 7,49 |
| 0,05 | 16 000 | 1 092,2 | 1 045,1 | 6,44 | 6,16 |
| 0,05 | 10⁷ | 23 333,8 | 23 105,5 | 5,50 | 5,45 |

L'échelle est √(nρ₀(1−ρ₀)/q). La réduction coûte 1 à 17 % de plus que le théorème direct. Elle donne en échange une preuve de l'ordre, et elle s'applique à **n'importe quelle** règle à observation complète qui a une borne sur trajectoire, celle de Singh comprise.

**Réponse à la question posée.** Oui : la règle à douze taux donne l'ordre en racine de n, avec le facteur √(1/q), jusqu'à environ 2,6·10⁷ audits (n ≈ 1,3·10⁸ à q = 0,20, 5·10⁸ à q = 0,05). C'est démontré par la proposition R et le lemme G, pour un horizon fixé d'avance. Au-delà, la borne redevient linéaire, de pente 9,8·10⁻⁵ par épisode.

**Statut.** Esquisse écrite par moi, non contre-lue. Deux points à contre-lire en priorité : les inégalités du lemme G (calcul à la main, contrôlé numériquement seulement sur une grille de N), et l'emploi de Ville pour la martingale de d_t avec λ fixé d'avance.

## 3. Ce qu'il faudrait pour une formalisation en Lean

**Énoncés.** Cadre : temps discret, espace probabilisé, filtration indexée par ℕ, processus X et A à valeurs dans {0, 1}. (H-a) se dit ainsi : A_t est indépendant de 𝓖_t = 𝓕_{t−1} ⊔ σ(X_t), avec P(A_t = 1) = q.

1. *Ville* : une surmartingale positive avec W₀ = 1 vérifie P(∃n, W_n ≥ c) ≤ 1/c.
2. *Facteur d'un audit* : sous (H-0), E[F_t ∣ 𝓕_{t−1}] ≤ 1. Corollaire : garantie 1.
3. *Martingale du tirage* : Z_m, et sa variante pour d_t, est une martingale d'espérance 1.
4. *Pas déterministes* : le pas 1 de la garantie 2, la monotonie de la pente (§ 1.3), le lemme G et l'algèbre de la proposition R. Ce sont des inégalités réelles sur log et exp.
5. *Garantie 2* et *proposition R*, à partir de 1, 3 et 4.

**Bibliothèques.** Mathlib, et rien d'autre a priori. Noms à vérifier dans la version utilisée, car ils ont changé ces deux dernières années :

- `MeasureTheory.Filtration`, `Adapted`, `Supermartingale`, `Martingale` ;
- l'espérance conditionnelle (`condExp`, anciennement `condexp`), sa propriété de sortie d'un facteur mesurable et sa forme pour une tribu indépendante ;
- `ProbabilityTheory.Indep` / `IndepFun` ;
- les temps d'arrêt (`IsStoppingTime`, `hitting`, `stoppedValue`) et l'arrêt optionnel pour les sous-martingales (on l'applique à −W) ;
- l'inégalité maximale de Doob (`maximal_ineq`, horizon fini) ;
- la continuité par le bas d'une mesure, pour passer à l'horizon infini ;
- côté réel : `Real.add_one_le_exp`, `Real.log_le_sub_one_of_pos`, la monotonie de log et exp, `nlinarith` / `positivity`.

Je ne connais pas de forme prête de l'inégalité de Ville pour une surmartingale à horizon infini dans Mathlib : il faudra probablement la dériver (arrêt au premier franchissement, horizon N, puis limite en N). Freedman et Bernstein ne sont pas nécessaires si l'on garde la martingale exacte du tirage : c'est un argument pour cette voie. Pour N_n, une borne de Chernoff par la fonction génératrice suffit.

**Ce qu'il ne faut pas formaliser.** Les valeurs numériques (B(n), quantiles binomiaux, constantes du lemme G à ρ₀ = 0,10). Lean n'a pas d'outil commode pour certifier des encadrements de log en virgule flottante. Il vaut mieux garder les énoncés symboliques en Lean, et les chiffres dans les programmes rejoués à l'octet.

**Ordre de grandeur, simple estimation de ma part** : garantie 1 en quelques centaines de lignes une fois Ville disponible ; garantie 2 et proposition R du même ordre ; la partie réelle (lemme G) est la plus longue à écrire, mais la plus mécanique. Le point délicat est la propriété de « gel » d'une variable binaire indépendante dans une espérance conditionnelle. Pour A binaire, elle se ramène à la linéarité : f(A, X) = 1{A=1}f(1, X) + 1{A=0}f(0, X), puis on sort le facteur mesurable.

## 4. Singh, arXiv 2610.18948 : lecture en entier et verdict d'antériorité

**Ce que fait l'article.** Il borne ce qu'une évaluation finie laisse passer après une certification observable et irrévocable, quand l'adversaire se tait jusqu'à la certification puis active (théorèmes 1 et 2, p. 4-5). Il démontre l'optimalité de la bascule face à un rapport de vraisemblance fixe et un coût d'échantillon (théorème 5, p. 18). Il traite les leurres et l'allocation (annexe C), et un évaluateur à « challenge bits » qui retient la certification (théorème 9, p. 21). Pour le déploiement, il propose un moniteur à mélange avec révocation définitive (proposition 1, p. 9, preuve en annexe A.11, p. 21 à 23). Les expériences portent sur RoCo et AgentDojo, avec des contrôleurs à modèle de langue, dont un qui infère la certification cachée à partir de reçus bruités (annexe D.12, p. 47-48), et une surveillance en direct (annexe D.14, p. 49-50).

### (a) La règle à mélange qui borne l'excès cumulé face à un adversaire adaptatif : **occupé**

- Proposition 1 (p. 9) : M_t = (1/H) Σ_j (r_j/p₀)^{K_t}((1 − r_j)/(1 − p₀))^{t−K_t}, avec r_j = p₀ + j(1 − p₀)/(H + 1), j = 1..H, et un arrêt définitif au premier M_t ≥ 1/α. Énoncés :
  - (i) fausse alarme ≤ α pour toute continuation à taux conditionnel ≤ p₀ ;
  - (ii) « for every adapted policy, including an adversary observing M_t, on every path K_{τ∧H} − p₀(τ∧H) ≤ √(½ H(log(H/α) + ϵ)) + 1 », avec ϵ = (1 − p₀)/(4p₀) (p. 9 ; preuve p. 22-23, par la même réduction « pas d'alarme ⇒ chaque atome sous H/α » que le pas 1 de la re-dérivation, puis Pinsker) ;
  - (iii) une alternative fixe laisse un excès espéré linéaire pour tout taux stationnaire entre p₀ et p†(r*) = a/(a + b) (p. 9, preuve p. 23 par le même exposant de Lundberg que le § 3.4 de la re-dérivation).
- Le taux d'indifférence p† et sa bande sont aussi au théorème 4 (p. 17) et à la proposition 8 (p. 24).
- **Ce qui diffère**, sans faire une nouveauté :
  - sa grille a H atomes, où H est l'horizon : elle descend avec l'horizon, ce qui revient à la recommandation de la re-dérivation (« grille qui descend vers ρ₀ ») ;
  - sa borne passe par Pinsker et ne s'adapte pas à la variance : à audit complet, ρ₀ = 0,10, α = 0,05, elle vaut 79,0 à H = 1 000 contre 34,9 pour la grille de douze taux, et 3 088 contre 1 025 à H = 10⁶ [contrôle, 4]. Des bornes de mélange adaptées à la variance sont classiques (Howard et al. 2021, que Singh cite).
- **Verdict** : la forme « mélange de rapports de vraisemblance, révocation définitive, excès cumulé en racine sur chaque trajectoire, contre tout adversaire adaptatif, et excès linéaire pour une alternative fixe » est publiée. Aucune phrase de nouveauté possible.

### (b) L'emploi avec une fraction auditée au hasard, sous une condition sur ce que l'agent sait des tirages : **partiellement occupé**

**Trouvé :**
- Théorème 9 (p. 21), « Challenge-bit assessor » : « assigns independent challenge bits Q_t ∼ Bernoulli(ρ) … Assume the current bit is private conditional on the attacker's pre-action information, including available seed and index ». C'est une fraction tirée au hasard, avec une condition sur le tirage **courant**, sachant ce que l'adversaire sait avant d'agir, graine et rang compris.
- Même page : « A public deterministic seed is not private when the attacker can reconstruct the bit », et l'estimateur pondéré par l'inverse de la probabilité, (ρB)⁻¹ Σ Q_t Y_t(1), sans biais « if the fresh bit is independent of Y_t(1) conditional on the past ». C'est l'identité de réduction du § 2.2, en espérance.
- Reprises de la même idée :
  - C.2, p. 27-28 : « Its privacy condition concerns the attacker's information before the current action, including any available seed or index » ;
  - K.3, p. 64 : une graine publique reconstructible ne donne pas la confidentialité ;
  - G, p. 52 : « private random sampling can frustrate an attacker that cannot identify the current inspection before acting » ;
  - D.9, p. 42 à 45 : diagnostics de fuite par classifieurs sur les métadonnées de présentation, tenus pour diagnostics, « not a proof of conditional privacy ».

**Non trouvé :**
- Le mélange séquentiel appliqué à la suite des épisodes audités, avec une borne sur l'excès cumulé de **toute** la suite et son facteur 1/q (la proposition 1 exige « trusted outcome observations » sur chaque essai, p. 9).
- La martingale exacte du tirage et la proposition R.
- L'énoncé explicite que voir les tirages **passés** ne casse rien, alors que prédire le tirage courant casse tout, avec le contre-exemple de la re-dérivation (§ 2.3 et 3.6). Singh conditionne sur l'information avant l'action, ce qui couvre implicitement les tirages passés, sans l'énoncer ni en tirer une borne.
- Chez Singh, les tirages servent à **retenir la certification** et à tester des nulles pendant l'évaluation, pas à surveiller le déploiement.

**Verdict** : la condition d'information sur le tirage courant, la fraction tirée au hasard et la mise en garde sur la graine sont publiées. La combinaison avec la borne d'excès cumulé à fraction auditée ne l'est pas dans cet article. Ce reste est une question, non une revendication : l'idée de réduction est un amincissement classique, et les martingales d'échantillonnage à probabilité connue sont publiées (Waudby-Smith et coauteurs, cités par la re-dérivation, § 5 ; RiLACS).

### (c) La perte « endommagé et non signalé » jugée par un oracle extérieur au mode d'attaque : **partiellement occupé**

**Trouvé :**
- Un arbitre de confiance, distinct de l'interface d'attaque : « The scorer and retained outcome records are trusted » (p. 2) ; « Intervention access and the assessed event are distinct » (table 1, p. 3) ; « independently checked final-state goals » et un « independent final-state scorer » (D.11, p. 45 ; D.12, p. 47 ; D.14, p. 49).
- La proposition 1 suppose ces observations de confiance (p. 9).

**Non trouvé :**
- Un moniteur au niveau de l'action dont on surveillerait les **ratés**. Chez Singh, l'événement Y_t est l'issue elle-même (séparation commandée, violation de sécurité), et le « moniteur » est la règle statistique sur ces issues.
- La conjonction « dommage selon l'oracle **et** non signalé par le moniteur validé », c'est-à-dire l'emploi du test séquentiel pour dire que la validation d'un moniteur ne décrit plus le déploiement.
- L'exigence que l'oracle soit extérieur à la famille du mode d'attaque.

**Verdict** : l'élément « oracle de confiance indépendant de l'intervention » est publié. La perte « raté du moniteur » et son emploi pour invalider la validation d'un moniteur ne sont pas dans Singh. L'idée d'invalider en prose figure ailleurs (esquisse de dossier de sûreté par contrôle, arXiv 2501.17315, p. 11, citée par l'erratum). Je ne l'ai pas relue ici.

### Ce que Singh change dans l'erratum

- § 5 de l'erratum, « Ce que je n'y ai pas trouvé aux pages lues : l'audit d'une fraction tirée au hasard, la condition sur ce que l'agent peut savoir des tirages » : **à corriger**. Les deux sont au théorème 9 (p. 21), sous le nom de « challenge bits », pour l'évaluation et non pour la surveillance du déploiement.
- Table de provenance de l'erratum : la recherche par motifs (« random audit », « audit probability », « subsampl », « sampled with probability », « inspection probability ») n'a pas pu trouver « challenge bits ». Conseil : pour une antériorité, lire la table des énoncés (théorèmes, propositions) en entier, pas seulement chercher des mots.
- Citations obligatoires à toute phrase sur la règle, en plus de celles de l'erratum : Singh, proposition 1 (p. 9) **et** théorème 9 (p. 21).

## 5. Réserves

- Mon esquisse (§ 2) n'est pas contre-lue. Le lemme G est démontré à la main et contrôlé numériquement sur une grille de N, pas en tout point.
- La lecture de Singh repose sur le texte extrait. Les formules en indice ou en racine sont abîmées par l'extraction. J'ai reconstitué la borne de la proposition 1 (ii), √(½ H(log(H/α) + ϵ)) + 1, à partir de la preuve (p. 22-23, Pinsker : 2(p̂ − p₀)² ≤ KL), et non de la formule imprimée seule. Aucune figure regardée.
- Je n'ai pas relu les autres voisins (Podkopaev et Ramdas, Cao, Waudby-Smith et coauteurs, l'esquisse de dossier de sûreté). Les verdicts (a) à (c) portent sur Singh seul, comme demandé.
- Le rejeu de la re-dérivation a pris environ 11 minutes ; il est identique à l'octet. Aucune valeur de simulation (blocs 4 et 5 de sa sortie, graines par `SeedSequence`) n'a été recalculée autrement que par ce rejeu.
