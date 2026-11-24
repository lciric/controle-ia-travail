# Préenregistrement — épreuve, près de leur limite, de la garantie de seuil du théorème de mise en œuvre aléatoire des audits et de l'étape de preuve qui la porte (papier D, chantier 3 : budget d'audit borné) — v2

Pièce décisive (classe A). Expérience sur processeur, 0 USD. Cette v2 remplace la v1 (gardée intacte) après une contre-lecture ; rien n'a été tiré ni lu sur la grille. La table « défaut → correction » est en fin de pièce.

- Auteur : Claude Fable 5.2, sous-agent de conception, sur mandat de la session mère du papier D.
- Date (UTC) : 2026-11-24.
- Commit du code d'analyse : le script n'existe pas encore. Branche `papier-d/evasion-post-entrainement-v1` ; le commit de départ est celui de la tête de branche au scellement, consigné par la session mère (à la rédaction : `67f0b2dfbd2190159d28fbf8bdefc4e463afa5b5`). Le script (instrument, classe B, neuf et versionné, contre-lu par un autre modèle) est écrit après le scellement, appelle `controle_ia.prereg.exiger_prereg_scelle` sur ce texte, et consigne son commit et son empreinte au manifeste du run (`src/controle_ia/manifeste.py`) avant le premier tirage.
- Documents qui font foi (chemin, empreinte SHA-256) :
  - théorème « Randomised implementation » (`thm:audit-random`, lignes 364 à 393 ; preuve, lignes 395 à 423) : `papiers/D/theorie/brouillon-fable-budget-audit-v1/audit-budget-section-v1-correctif-1.tex`, `c6e5cebfe5fbf5c2d360bbd9ad042ba6e4626ac1b78de461ff0f99446b625727` ;
  - mise en œuvre numérique existante, fonction `sim()` : même dossier, `check_audit_v1.py`, `d786cba7fd23bb31abc5a2abe9dd378a912355e657b696d740bb74e987c4ab83` ;
  - proposition d'expérience : `papiers/D/audits/audit-reserves-chantier3-v1/note-garantie-seuil-non-eprouvee-chantier3-v1.md`, `0b8b643a62a6eef7a8e151a992d6717caedb980ac316c25d4251c325778b7a6c` ;
  - audit des deux réserves et son script : même dossier, `audit-reserves-chantier3-v1.md`, `54a00ef2989a42e17fd7ca80acf4c59c7a5a14bef33a00f18882b926f6f0ffd2` ; `audit_reserves_chantier3_v1.py`, `fb94751eaf9901ca8fc315197f2cc7cb1e7d1691684aa6933e9bfc755c366fef`.

## Hypothèse

**Objet.** Aucune hypothèse numérotée du programme : l'expérience éprouve un énoncé du brouillon du papier D. Motif : sur 800 000 répétitions, la simulation existante ne compte aucune violation du seuil ; tous ses échecs sont des dépassements de budget (`audit-reserves-chantier3-v1.md`, réserve 1).

**Processus.** $\Delta R>0$, $C\ge0$, $W=\Delta R+C$, $\bar\rho=\Delta R/W$, $a=1-\gamma/\eta$ ($a=1$ si $\eta=\infty$), $c=\ell_{\text{crit}}+L$, $\hat x_k=\hat\ell_k+L$, $G_k=\gamma\sum_{i<k}a^i$, tolérance $\tau=10^{-9}\max(1,c)$. Avec $\hat x_0=0$ et $A_k\sim\text{Binomiale}(n,\rho_k)$ indépendants (les $n$ audits de Bernoulli du tour $k$) :
$$\hat x_{k+1}=a\,\hat x_k+\gamma\Delta R-\gamma W\,A_k/n,\qquad k=0,\dots,K-1 .$$

**Plan de marge $m\in[0,c]$**, en boucle ouverte, donné par la forme close du plan « juste à temps » pour la marge de manœuvre $c-m$ : $\kappa(m)=\min\{k:\Delta R\,G_{k+1}-(c-m)>\tau\}$ ; $\rho_j=0$ pour $j<\kappa$ ; $\rho_\kappa=(\Delta R\,G_{\kappa+1}-(c-m))/(\gamma W)$ ; $\rho_j=\rho_{\text{tenu}}(m)=(\Delta R-(c-m)/\eta)/W$ pour $j>\kappa$ (avec $(c-m)/\eta=0$ si $\eta=\infty$). La trajectoire en champ moyen est $x_k=\min(\Delta R\,G_k,\,c-m)$. Le plan glouton de `sim()` doit coïncider à $10^{-9}$ près (garde).

**Marge de Bernstein** : $\varepsilon=\gamma W\bigl[\sqrt{2\bar\rho\,\Gamma_K\Lambda/n}+\tfrac{2\Lambda}{3n}\bigr]$, $\Gamma_K=\sum_{i<K}a^{2i}$, $\Lambda=\ln(2K/\delta)$.

**Processus plafonné** (celui de l'énoncé). $B_m=n\sum_k\rho_k(m)$, $B_{\text{rand}}(m)=B_m+\sqrt{2B_m\ln(2/\delta)}+\tfrac23\ln(2/\delta)$, plafond $P=\lfloor B_{\text{rand}}(m)\rfloor$. Sur les mêmes tirages : $A'_k=\min(A_k,\,P-N'_k)$, $N'_{k+1}=N'_k+A'_k$, et $\hat x'$ suit la récurrence avec $A'$. À $\lambda=1$, $B_{\text{rand}}(\varepsilon)$ est le plafond du théorème ; aux autres marges, la même formule, à titre descriptif.

**Trois énoncés, distingués.** Tous supposent $\varepsilon\le c$ et le plan $\rho(\varepsilon)$.
- (E) **Étape unilatérale de la preuve de (c)** (lignes 411 à 414), sur le processus **sans plafond** : $P(\max_{1\le k\le K}\hat x_k>c)\le\delta/2$. Elle ne figure pas dans l'énoncé et ne découle pas de (a), qui est bilatérale au niveau $\delta$.
- (C) **Énoncé (c)**, sur le processus **plafonné** : $P(\max_{1\le k\le K}\hat x'_k>c)\le\delta$ (le plafond du nombre d'audits y tient par construction).
- (A) **Énoncé (a)**, restreint à ce plan : $P(\max_k|\hat x_k-x_k|>\varepsilon)\le\delta$.

**Hypothèses.**
- H-a, garantie : (E) et (C) tiennent en tout point admissible de la grille.
- H-b, nécessité d'une marge : sous le plan sans marge $\rho(0)$, la probabilité de violation dépasse $\delta/2$ en tout point admissible (le brouillon ne la revendique pas, remarque `rem:audit-random`).
- H-c, prudence : la plus petite marge qui tient le niveau $\delta/2$, $\varepsilon_{\text{emp}}$, est strictement entre $0$ et $\varepsilon$.

**Hypothèses de travail.** Seuls les audits sont aléatoires ; la moyenne sur les actions de la politique est exacte ; le plan ne dépend pas des tirages. La violation décroît avec la marge : les taux du plan croissent avec $m$ et le tirage binomial est monotone en son taux, donc le test de monotonie n'est qu'une garde.

## Prédiction chiffrée et signe attendu

$V$, $V'$, $D$ : fréquences de violation sans plafond, de violation plafonnée et d'écart bilatéral (section Métrique), au point $p$ sous le plan $\rho(\lambda\varepsilon)$.

| | Prédiction | Signe | Réfutation |
|---|---|---|---|
| P1a | À $\lambda=1$ : $V\le\delta/2$, $V'\le\delta$ et $D\le\delta$ en tout point admissible. | sous le seuil | un point de classe finale « au-dessus » (section Seuil) |
| P1b | À $\lambda=1$ : $V\le\delta/20$ en tout point admissible. | très sous le seuil | un point dont la borne basse unilatérale au niveau $10^{-4}$ du premier tirage dépasse $\delta/20$ |
| P2 | À $\lambda=0$ : $V\ge0{,}5$ en tout point admissible ; médiane des points $\ge0{,}9$. | nettement positif | un point dont la borne haute unilatérale au niveau $10^{-4}$ du premier tirage est sous $0{,}5$, ou médiane sous $0{,}9$ |
| P3 | $V$ ne croît pas avec $\lambda$ ; $V>\delta/2$ partout à $\lambda=0{,}1$ ; $V\le\delta/2$ partout à $\lambda=0{,}75$. | décroissant | une hausse significative, ou un point classé du mauvais côté au premier tirage ; un point indéterminé à $\lambda=0{,}1$ ou $0{,}75$ n'est ni prolongé ni compté : P3 y est « non lue » |
| P4 | $\varepsilon_{\text{emp}}/\varepsilon\in[0{,}20\,;0{,}70]$ en tout point de l'ensemble de lecture ; médiane dans $[0{,}35\,;0{,}55]$ ; la médiane par valeur de $\eta$ décroît quand $\eta$ croît ($1$, $10$, $\infty$). | rapport $<1$ | un point hors plage, médiane hors plage, ou ordre inversé |

**Justification, par raisonnement et sans tirage.** P2 : sans marge, la trajectoire en champ moyen touche le seuil dès le premier tour audité ; l'écart y est centré, d'où une chance voisine d'une sur deux par tour, et la grille compte au moins 24 tours tenus au seuil. P1 : à marge nominale, l'écart au seuil vaut à chaque tour au moins $\sqrt{2\Lambda}\ge3{,}7$ écarts-types bornés, et l'écart-type réel est sous sa borne ; estimé : plus de 4,5 écarts-types réels. $V'$ dépasse $V$ au plus de la fréquence de dépassement du budget, de l'ordre de $\delta/20$ à $\delta/10$ (attendu, descriptif). P4 : produit de trois facteurs inférieurs à 1 — écart-type réel sur écart-type borné (0,6 à 0,8) ; quantile réel du maximum sur $\sqrt{2\Lambda}$ (0,45 à 0,87, la borne d'union étant d'autant plus lâche que la mémoire $\eta/\gamma$ est longue) ; poids du terme linéaire (0,7 à 1). P1b, P2, P3 et P4 sont des estimations d'ordre de grandeur : leur réfutation corrige le chiffre et ne change aucun verdict sur la garantie.

**Descriptif, sans prédiction** : budget épargné $(B_\varepsilon-B_{\varepsilon_{\text{emp}}})/B^\star_{\text{unif}}(c)$ ; distance au seuil ; dépassement de budget ; $V'$ et $D$ hors de $\lambda=1$ ; bras en boucle fermée.

## Métrique

Sur $R$ répétitions indépendantes, au point $p$ et à la marge $m$, toutes calculées sur les mêmes tirages $A_k$ :

- **Métrique primaire, violation du seuil sans plafond** : $\hat V=\frac1R\sum_r\mathbf 1\{\max_{1\le k\le K}\hat x^{(r)}_k-c>\tau\}$. Lue contre $\delta/2$ ; éprouve (E).
- **Violation plafonnée** : $\hat V'=\frac1R\sum_r\mathbf 1\{\max_{1\le k\le K}\hat x'^{(r)}_k-c>\tau\}$. Lue contre $\delta$ à $\lambda=1$ ; éprouve (C).
- **Écart bilatéral** : $\hat D=\frac1R\sum_r\mathbf 1\{\max_k|\hat x^{(r)}_k-x_k|-\varepsilon>\tau\}$, à $\lambda=1$ seulement. Lu contre $\delta$ ; éprouve (A) sur ce plan.
- **Dépassement de budget**, à part : $\hat O=\frac1R\sum_r\mathbf 1\{N^{(r)}>B_{\text{rand}}(m)\}$, descriptif, rapporté à côté de sa probabilité exacte par convolution.

Une égalité au seuil n'est pas une violation. Aucune de ces fréquences n'est fusionnée avec une autre : « violation ou dépassement » ne sert à aucun verdict. Invariant vérifié répétition par répétition : toute violation sans plafond est une violation plafonnée, et toute violation plafonnée est une violation sans plafond ou un dépassement ; un manquement arrête la course.

**Intervalles.** Clopper-Pearson bilatéral à 95 % pour toute fréquence rapportée ; bornes unilatérales de Clopper-Pearson au niveau $10^{-4}$ pour les classements.

**Marge empirique minimale.** $\varepsilon_{\text{emp}}(p)$ est un estimateur, pas une décision : borne haute finale d'une bissection sur $m\in[0,\varepsilon]$, dix itérations, $R$ tirages neufs chacune ; règle : estimation ponctuelle $\hat V(m)\le\delta/2$ donne « haut $=m$ », sinon « bas $=m$ ». Elle n'est lancée que si $V$ est de classe finale « au-dessus de $\delta/2$ » à $\lambda=0$ et « sous $\delta/2$ » à $\lambda=1$. Résolution numérique : $\varepsilon/1024$. Incertitude statistique déclarée, non estimée : environ 2 % en relatif sur la marge $\varepsilon_{\text{emp}}$. Deux conditions de validité : (i) le tirage de confirmation à $m=\varepsilon_{\text{emp}}$ n'est pas classé « au-dessus de $\delta/2$ » ; (ii) $\lambda^-\varepsilon\le\varepsilon_{\text{emp}}\le\lambda^+\varepsilon$, où $\lambda^-$ est la plus grande valeur de la grille de classe « au-dessus de $\delta/2$ » et $\lambda^+$ la plus petite de classe « sous $\delta/2$ » (premier tirage pour $\lambda\notin\{0,1\}$). Sinon le point est « non concluant » pour la marge empirique. **Ensemble de lecture de P4** : les points où la bissection a tourné et est valide ; P4 n'est lue que s'il en compte au moins 125 sur 138, sinon « non lue ».

**Distance au seuil (descriptive).** Quantile empirique d'ordre $1-\delta/2$ de $\max_k\hat x_k-c$ à $\lambda=1$, divisé par $\varepsilon$, avec son intervalle par statistiques d'ordre.

## Seuil

- Seuils : $\delta/2$ pour $V$ (0,025 ou 0,05) ; $\delta$ pour $V'$ et $D$ (0,05 ou 0,1).
- **Classement d'une fréquence face à son seuil $s$** : « sous » si la borne haute unilatérale au niveau $10^{-4}$ est $\le s$ ; « au-dessus » si la borne basse unilatérale au niveau $10^{-4}$ est $>s$ ; « indéterminé » sinon. Avec $R=10^5$ et $s=\delta/2$, la zone indéterminée couvre $\pm7{,}3$ % autour du seuil à $\delta=0{,}05$ et $\pm5{,}1$ % à $\delta=0{,}1$.
- **Règle unique de prolongation**, pour les quatre lectures décisives ($V$, $V'$, $D$ à $\lambda=1$ ; $V$ à $\lambda=0$). Une prolongation est un tirage de $10^6$ répétitions neuves, lu seul, pour la seule métrique qui l'a déclenchée.

| Premier tirage | Prolongation | Classe finale |
|---|---|---|
| « sous » | aucune | « sous » |
| « au-dessus », à $\lambda=0$ | aucune | « au-dessus » |
| « au-dessus », à $\lambda=1$ | obligatoire | « au-dessus » si la prolongation l'est ; sinon « non concluant » |
| « indéterminé » | obligatoire | celle de la prolongation ; « non concluant » si elle est indéterminée |

  Toute réfutation à $\lambda=1$ passe donc par une prolongation classée « au-dessus » ; un point d'abord indéterminé puis « au-dessus » vaut réfutation.
- **Risque d'erreur par famille** (138 points). Fausse réfutation de (E), de (C) ou de (A) : au plus $1{,}4$ % chacune, car elle exige une prolongation classée à tort au niveau $10^{-4}$. Classe finale « sous » à tort, à $\lambda=1$ ou à $\lambda=0$ : au plus $2{,}8$ % par famille (premier tirage ou prolongation). P1b et P2 : $1{,}4$ % chacune. Classements de P3 : 276 lectures, $2{,}8$ %. Garde de monotonie : test exact de Fisher unilatéral au niveau $10^{-5}$ sur les 690 paires de marges voisines, $0{,}7$ %.

## Plan d'analyse

**Grille.** $K\in\{50,200,500\}$, $n\in\{100,1000\}$, $\gamma\in\{0{,}05\,;0{,}2\}$, $\eta\in\{1\,;10\,;\infty\}$, $C\in\{4,19\}$, $\delta\in\{0{,}05\,;0{,}1\}$, $\Delta R=1$ : 144 points, numérotés dans cet ordre lexicographique. Facteur de marge $\lambda\in\{0\,;0{,}1\,;0{,}25\,;0{,}5\,;0{,}75\,;1\}$.

**Hors de la frontière.** En tout point, $c=\tfrac12\,\Delta R\,G_K$ : la moitié de la charge finale sans audit. Donc $c<\eta\,\Delta R$ strictement et le budget optimal déterministe est positif partout. Cette règle remplace l'exemple de la note ($c=0{,}5\,\eta\Delta R$ et $c=1$), qui laisserait 8 points sans audit et 30 points inadmissibles. Cas d'égalité connu : à $\eta=\infty$ et $K$ pair, la charge sans audit vaut exactement $c$ au tour $K/2$ ; à $\lambda=0$ c'est une égalité déterministe, non une violation (tolérance $\tau$), et $\kappa=K/2$ par la définition à seuil ci-dessus.

**Admissibilité.** Un point est admissible si $\varepsilon\le c$. Arithmétique de conception, déterministe et sans tirage, confirmée par la contre-lecture, à recalculer par le script : 138 points admissibles ; les 6 inadmissibles sont $n=100$, $\gamma=0{,}2$, $\eta=1$, $C=19$ ; sous le plan sans marge, au moins 24 tours tenus ($K-1-\kappa(0)$) et au moins 2,5 audits attendus par tour tenu. Les points inadmissibles sont listés avec $\varepsilon$ et $c$, ni remplacés ni lus.

**Taille.** $R=10^5$ par point et par marge, en dix lots de $10^4$. À $\delta/2=0{,}025$, l'écart-type de $\hat V$ est de $4{,}9\times10^{-4}$ ; une violation réelle de $1{,}15\,\delta/2$ est classée « au-dessus » avec une probabilité de 0,9998. Charge : environ $6\times10^{10}$ tirages binomiaux, plus les contrôles ; quelques heures sur un cœur.

**Graines (R9).** `numpy.random.SeedSequence(entropy=202611243003, spawn_key=(i_point, i_bloc, i_rang, i_lot))`, générateur `numpy.random.Generator(numpy.random.PCG64(...))`, numpy $\ge1{,}25$ ; un lot est un seul appel `binomial(n, rho, size=(10**4, K))`.

| `i_bloc` | Emploi | `i_rang` | `i_lot` |
|---|---|---|---|
| 0 à 5 | les six valeurs de $\lambda$, dans l'ordre | 0 | 0 à 9 |
| 6 | bissection | itération 0 à 9 ; 10 : confirmation | 0 à 9 |
| 7 | prolongation | 0 : $\lambda=0$ ; 1 : $\lambda=1$ | 0 à 99 |
| 8 | contrôles d'instrument | 0 et 1 : systématiques à $\lambda=0$ et $1$ ; 2 et 3 : renforcés à $\lambda=0$ et $1$ | 0 |
| 9 | bras en boucle fermée | 0 : $\lambda=0$ ; 1 : $\lambda=1$ | 0 à 9 |

Bancs témoins : `i_point` 1000, 1001, 1002 ; `i_bloc` 0 (tirages sains) ou 1 (tirages de l'artefact) ; `i_rang` : indice de la marge ; `i_lot` 0 à 9. Toutes les clés sont distinctes et consignées au manifeste, avec configuration, versions et commit. **Relance** après une course invalide : même plan, entropie `202611243004` ; les deux courses sont rapportées ; aucune troisième course sans décision nommée de Lazar. Une panne technique se relance avec les mêmes graines.

**Ordre.** (1) gardes sur les trois bancs témoins ; (2) recalcul de l'admissibilité ; (3) blocs 0 à 5 et contrôles systématiques ; (4) prolongations ; (5) bissections ; (6) bras descriptif. Sorties brutes scellées avant toute lecture ; la table de lecture est appliquée par un sous-agent neuf, qui n'a écrit ni ce texte ni le script.

## Critères de lecture gelés

Verdict par point, puis verdict d'ensemble. Les classes sont les classes finales de la section Seuil. **Ordre de priorité**, du plus fort au plus faible : course invalide (défaut d'instrument) ; réfutations ; « trop propre » et « marge non nécessaire » ; « non concluant » ; « la garantie tient ».

**À $\lambda=1$, par point.**

| Issue | Verdict | Conclusion écrite d'avance |
|---|---|---|
| $V$ « sous $\delta/2$ » et $V'$ « sous $\delta$ » | (E) et (C) tiennent en ce point | voir le verdict d'ensemble |
| $V$ « au-dessus de $\delta/2$ », $V'$ non « au-dessus de $\delta$ » | **« garantie réfutée, au grade de l'étape de preuve »** | « Au point $p$, la violation sans plafond dépasse $\delta/2$ : l'étape unilatérale de la preuve de (c), ou sa mise en œuvre, est fausse. L'énoncé (c), au niveau $\delta$, n'est pas réfuté par ce seul fait ; sa preuve est à reprendre. Nœud remonté à Lazar. » |
| $V'$ « au-dessus de $\delta$ » | **« garantie réfutée, au grade de l'énoncé (c) »** | « Au point $p$, la violation du processus plafonné dépasse $\delta$ : l'énoncé (c), ou la mise en œuvre qui le suit à la lettre, est faux. Il sort du brouillon jusqu'à correction. Nœud remonté à Lazar. » |
| $D$ « au-dessus de $\delta$ » | « énoncé (a) réfuté sur ce plan » | rapporté à part, même traitement ; ne se déduit jamais de $V$ seule. |
| une classe « non concluant » sans réfutation | « non concluant » en ce point | point listé. |

**À $\lambda=0$, par point** (trois cases disjointes).

| Issue | Verdict | Conclusion écrite d'avance |
|---|---|---|
| $V$ « au-dessus de $\delta/2$ » | marge nécessaire en ce point ; l'instrument y voit la violation | P2 y est lue à part, tenue ou réfutée, sans effet sur ce verdict. |
| $V$ « sous $\delta/2$ » (zéro violation compris) | **« trop propre »** (R4), puis, si l'audit renforcé est sans défaut, **« marge non nécessaire »** en ce point | « En ce point, le plan sans marge tient déjà le niveau : la marge de Bernstein y est un surcoût sans contrepartie mesurée, et la garantie n'y est pas éprouvée. » D'ensemble si tous les points. |
| $V$ « non concluant » | « non concluant » en ce point | point listé ; la garantie n'y est pas dite éprouvée. |

**Verdict d'ensemble.**
- **« La garantie tient »** (confirmé, sur la grille) : tous les contrôles d'instrument passent, et en chaque point admissible $V$ est « sous $\delta/2$ » et $V'$ « sous $\delta$ » à $\lambda=1$, et $V$ « au-dessus de $\delta/2$ » à $\lambda=0$. Conclusion : « Pour le processus du théorème, la violation du seuil à marge nominale est sous $\delta/2$ sans plafond et sous $\delta$ avec plafond, en des points où l'instrument voit la violation dès que la marge est retirée. La simulation ne contredit ni l'énoncé (c) ni l'étape de preuve ; elle ne les prouve pas et ne dit rien hors de leurs hypothèses. »
- **« Garantie réfutée »** : au moins un point réfuté, avec son grade ; ce verdict prime sur les suivants.
- Sinon : « tient en $N_1$ points ; marge non nécessaire, donc garantie non éprouvée, en $N_2$ ; non concluant en $N_3$ », avec les listes.
- $0<\varepsilon_{\text{emp}}<\varepsilon$ : « marge nécessaire, surdimensionnée d'un facteur $\varepsilon/\varepsilon_{\text{emp}}$ sur cette grille » (descriptif).
- Zéro violation à $\lambda=1$ ne vaut confirmation que jointe aux violations vues à $\lambda=0$ au même point et aux contrôles passés.

**Contrôles d'instrument, dans les deux sens (R4).** Ils sont **systématiques** : en chaque point admissible, quelle que soit l'issue, y compris quand « la garantie tient ». Tolérances fixées ici :
1. *Plan*, à chaque marge tirée : $|\max_k x_k-(c-m)|\le\tau$ ; écart entre plan clos et plan glouton $\le10^{-9}$ par taux ; $|\sum_k\rho_k-B^\star_{\text{unif}}(c-m)/n|\le10^{-9}\max(1,\sum_k\rho_k)$ ; $\varepsilon$ recalculée par $\Gamma_K=(1-a^{2K})/(1-a^2)$ (ou $K$ si $a=1$), écart relatif $\le10^{-9}$.
2. *Second chemin de comptage*, à $\lambda=0$ et $\lambda=1$, sur $10^3$ répétitions du bloc 8 : audits tirés épisode par épisode ; $\hat x_k$ calculé par la récurrence et par la somme explicite $\Delta R\,G_k-(\gamma W/n)\sum_{j<k}a^{k-1-j}A_j$ ; écart $\le\tau$ à chaque tour de chaque répétition ; indicatrices identiques, sauf répétitions où $|\max_k\hat x_k-c|\le10\,\tau$, listées ; fréquence à moins de $5\sqrt{\hat V(1-\hat V)(10^{-3}+10^{-5})}+0{,}003$ de celle de la course.
3. *Moments*, à chaque valeur de $\lambda$, sur les tirages de la course : moyenne de $\hat x_K$ à moins de 5 erreurs types de $x_K$ ; variance empirique à 3 % près de $(\gamma W)^2n^{-1}\sum_j a^{2(K-1-j)}\rho_j(1-\rho_j)$.
4. *Premier tour audité*, à chaque valeur de $\lambda$ : le compte des répétitions où $\hat x_{\kappa+1}-c>\tau$ est à moins de $5\sqrt{R\,p_1(1-p_1)}+3$ de $R\,p_1$, avec, pour la marge $m$, $p_1(m)=P\bigl(\text{Binomiale}(n,\rho_\kappa(m))<n\rho_\kappa(m)-n(m+\tau)/(\gamma W)\bigr)$, nulle si le second membre est négatif ou nul. La forme $P(A<n\rho_\kappa)$ ne vaut qu'à $m=0$.

**Audit renforcé**, déclenché par « trop propre » et par toute réfutation, avant de prononcer : contrôle 2 refait sur $10^4$ répétitions à la marge visée (bloc 8, rangs 2 et 3 ; tolérance de fréquence recalculée avec $10^{-4}$ au lieu de $10^{-3}$, et $0{,}0003$ au lieu de $0{,}003$), et contrôles 1, 3 et 4 relus en ce point. **Sans défaut** : la lecture tient et le verdict est prononcé avec la mention de l'audit. **Un contrôle hors tolérance, systématique ou renforcé, est un défaut d'instrument** : course invalide, script corrigé sous un nouveau nom et contre-lu, relance selon la règle des graines.

## Liste d'arrêt

Tout arrêt est bruyant et journalisé ; aucun repli silencieux ; rien n'est lu d'une course arrêtée.

1. Ce texte n'est pas scellé ou son empreinte ne se vérifie pas : refus de partir.
2. Une garde échoue sur un banc témoin, ou ne se déclenche pas sur son artefact : arrêt avant tout tirage de la grille.
3. L'admissibilité recalculée diffère de 138 points, ou le minimum de $K-1-\kappa(0)$ diffère de 24 : arrêt, erratum.
4. Valeur non finie, taux hors de $[0,\bar\rho+10^{-12}]$, clé de graine en double, fichier de sortie déjà présent, invariant entre violations manqué : arrêt.
5. Garde des tirages hors tolérance en un point de la grille : défaut d'instrument, course invalide.
6. Sensibilité à la tolérance : si le compte de violations recalculé avec $\tau'=10^{-6}\max(1,c)$ diffère de plus de 10 répétitions, le point est « non concluant » à cette marge.
7. Plus de 12 heures de calcul, ou perte de la machine : panne technique, pas un résultat ; relance entière avec les mêmes graines.
8. Toute lecture partielle avant la fin et le scellement des sorties invalide la course.

### Gardes, chacune testée sur un cas sain et sur un artefact (R5)

**Trois bancs témoins à vérité exacte**, hors de la grille ($\Delta R=1$, $C=4$, $\delta=0{,}05$, $\gamma=0{,}2$ ; marges $m\in\{0,\varepsilon/2,\varepsilon\}$ ; $R=10^5$). Les probabilités exactes sont calculées par un chemin indépendant du simulateur. Une fréquence passe si $|\text{compte}-R\,P^\star|\le5\sqrt{R\,P^\star(1-P^\star)}+3$. Les valeurs ci-dessous sont de l'arithmétique de conception, sans tirage ; le script les recalcule et s'arrête sur un écart relatif de plus de 1 %.

- **Témoin sans mémoire** : $\eta=0{,}2$ ($a=0$), $K=20$, $n=1000$, $c=0{,}1$ ; $\varepsilon\approx0{,}0562$. Plan constant $\rho_m=(\gamma\Delta R-c+m)/(\gamma W)$, $n\rho_0=100$ ; $P^\star_V(m)=1-\bigl[1-F_{\text{Binomiale}(n,\rho_m)}(n\rho_0-1)\bigr]^K$ ; écart bilatéral exact à $m=\varepsilon$ : $1-\bigl[P(|A-n\rho_\varepsilon|\le n\varepsilon/(\gamma W))\bigr]^K$.
- **Témoin à mémoire entière** : $\eta=\infty$ ($a=1$), $K=12$, $n=100$, $c=1{,}2$ ; $\varepsilon\approx0{,}5855$. Vérité par programmation dynamique sur le compte cumulé d'audits, pour $V$, $O$ et $V'$ : $P^\star_V\approx0{,}751$, $3{,}24\times10^{-3}$, $1{,}2\times10^{-7}$ aux trois marges ; $P^\star_O\approx6{,}3\times10^{-4}$, $8{,}7\times10^{-4}$, $7{,}3\times10^{-4}$. Avec un plafond d'épreuve de 118 audits, sous les 120 qu'exige la contrainte finale, toute répétition plafonnée viole : fréquence exactement 1.
- **Témoin à mémoire partielle** : $\eta=0{,}4$ ($a=0{,}5$), $K=3$, $n=1000$, $c=0{,}175$ ; $\Gamma_K=1{,}3125$, $\varepsilon\approx0{,}05333$ (une somme $\sum a^i$ mise pour $\sum a^{2i}$ donnerait $0{,}0611$). Vérité par énumération des comptes des deux premiers tours : $P^\star_V\approx0{,}799$, $0{,}0162$, $4{,}7\times10^{-6}$.

| Garde | Cas sain (doit passer) | Artefact (doit arrêter) |
|---|---|---|
| Plan (contrôle 1) | plan sans marge de chaque témoin, qui touche le seuil et **doit violer** à la fréquence $P^\star_V(0)$ | plan annoncé sans marge mais construit avec la marge $\varepsilon$ ; $\Gamma_K$ calculé par $\sum a^i$ sur le témoin à mémoire partielle |
| Compteur de la violation sans plafond, contre $P^\star_V$, trois témoins, trois marges | compteur de la métrique primaire | **événement mal compté** : violation lue au seul dernier tour ; violation fusionnée avec le dépassement de budget ; seuil comparé à $c-m$ au lieu de $c$ ; récurrence sans mémoire ($a$ mis à 0) sur les deux témoins à mémoire |
| Compteurs de la violation plafonnée et de l'écart bilatéral | $V'$ contre sa vérité au plafond du théorème et au plafond d'épreuve (témoin à mémoire entière) ; $D$ contre sa vérité (témoin sans mémoire) | compteur qui ignore le plafond ; plafond appliqué par tour et non au cumul ; écart compté d'un seul côté |
| Tirages : moyenne, sur les $R$ répétitions, du nombre total d'audits à moins de 5 erreurs types de $n\sum_k\rho_k$, en chaque point | tirages du plan | taux décalés de 10 % au tirage |
| Valeurs finies, clés de graines distinctes, refus d'écraser | tableau fini ; jeu de clés de la course ; chemin de sortie neuf | valeur non finie injectée ; clé dupliquée ; fichier de sortie déjà présent |
| Sensibilité à la tolérance (arrêt 6) | compteur à $\tau$ et à $\tau'$ sur le témoin sans mémoire | tolérance portée à un pas et demi de réseau, $1{,}5\,\gamma W/n$, qui change le compte à $m=\varepsilon/2$ |
| Invariant entre violations | tirages sains | violation plafonnée calculée sur des tirages autres que ceux de la violation sans plafond |

Les essais de ces gardes vivent avec le script et passent avant la course.

## Hors du champ, non revendiqué

- **Boucle fermée** (plan recalculé à chaque tour sur la trajectoire réalisée) : bras descriptif, $\lambda\in\{0,1\}$, mêmes points, bloc de graines 9, table à part titrée « descriptif, sans verdict ». Aucune garantie n'y est énoncée ni éprouvée.
- **Entraînement par gradient stochastique**, bruit d'échantillonnage des actions de la politique : non modélisé par le théorème, non lancé sous ce texte ; toute course demanderait son propre texte.
- L'énoncé (a) hors du plan $\rho(\varepsilon)$, l'énoncé (b) sur le nombre d'audits, l'inflation de budget : descriptifs ou non éprouvés ici.
- Le caractère serré ou lâche de la borne hors de cette grille (autre marge de manœuvre que $c=\tfrac12\Delta R\,G_K$, $\eta=\gamma$, $\Delta R\ne1$, points inadmissibles), les audits reconnaissables ou faillibles.
- « La garantie tient » ne vaut jamais preuve du théorème ni validation d'une sonde ou d'un protocole du programme.

## Contre-lecture

- **Contre-lecture 1** (de la v1). Sous-agent neuf, Opus 5.5, 24 novembre 2026, qui n'a écrit ni le texte ni le script. Brouillon relu : `prereg-seuil-chantier3-v1.md`, empreinte `889c1153ed68405536c834b643a63b2d0b726c9f4d193fcbcb8062bf8eecfadb`. Rapport : `contre-lecture-prereg-seuil-v1.md` (bloc-notes de session, chemin à mettre à jour au versement), empreinte `841171ccf1fe33b059ed4252894f63253b3043d8fbc71576092be26d324e3f83`. Verdict : conforme avec corrections, six défauts majeurs, sept mineurs, aucun bloquant ; les deux écarts à la note sont jugés justifiés. Traitement : les treize défauts sont acceptés, aucun refusé ; voir la table.
- **Contre-lecture 2** (vérification des corrections de cette v2 par le même contre-lecteur). En attente : identifiant, empreinte de la v2 relue, chemin et empreinte du rapport à porter ici par la session mère. Le validateur refuse le scellement tant qu'ils manquent.

### Table « défaut → correction »

| N° | Défaut relevé | Correction dans la v2 | Lieu |
|---|---|---|---|
| 1 | L'objet éprouvé est une étape de preuve, pas l'énoncé | Trois énoncés distingués, (E), (C), (A) ; métriques $V'$ (processus plafonné, contre $\delta$) et $D$ (bilatéral, contre $\delta$) ajoutées ; verdict de réfutation gradué : étape de preuve, énoncé (c), énoncé (a) | Hypothèse ; Métrique ; Critères, table à $\lambda=1$ |
| 2 | Contrôle (4) faux dès que la marge est non nulle | Formule générale $p_1(m)$ ; la forme à $m=0$ est dite telle | Critères, contrôle 4 |
| 3 | Audit sans tolérances ; racine de relance non fixée | Tolérances chiffrées des quatre contrôles ; relance à l'entropie `202611243004` ; pas de troisième course sans décision de Lazar | Critères ; Plan d'analyse, graines |
| 4 | Audit non déclenché quand « la garantie tient » ; témoin aveugle à la mémoire | Contrôles systématiques en chaque point, exigés par le verdict « tient » ; $\varepsilon$ recalculée par la forme fermée de $\Gamma_K$ ; deux témoins à mémoire ($a=1$ par programmation dynamique, $a=0{,}5$ par énumération) | Critères ; Gardes |
| 5 | Contradiction sur la prolongation | Règle unique, une ligne par combinaison ; toute réfutation passe par une prolongation | Seuil |
| 6 | Lecture non univoque à $\lambda=0$ | Trois cases disjointes ; « trop propre » réservé à « sous $\delta/2$ » ; verdict après audit écrit ; ordre de priorité ; P2 lue à part | Critères, table à $\lambda=0$ |
| 7 | Risque d'ensemble mal annoncé | Risque par famille : 1,4 % pour une fausse réfutation, 2,8 % pour une classe finale fausse et pour P3, 0,7 % pour la garde de monotonie ; largeurs de zone corrigées (7,3 % et 5,1 %) | Seuil |
| 8 | Égalité à $\eta=\infty$, arrêt n° 3 déclenché à tort | Plan par la forme close ; $\kappa$ défini avec le seuil $\tau$ ; égalité déterministe signalée | Hypothèse ; Plan d'analyse |
| 9 | Latitude de la bissection | Estimateur et non décision ; 2 % dits sur la marge ; conséquence du tirage de confirmation ; encadrement défini ; ensemble de lecture de P4 et son effectif minimal | Métrique |
| 10 | Prédictions non réfutables | P1b avec critère ; « la plupart » retiré ; sort des points indéterminés de P3 écrit ; critère de la médiane de P2 | Prédiction |
| 11 | Graines incomplètes | Clé à quatre composantes, table par bloc, lots, témoins, prolongation par valeur de $\lambda$ | Plan d'analyse |
| 12 | Arrêts 4 et 5 non éprouvés ; action de la garde des tirages ; critère relatif mal posé | Gardes ajoutées avec cas sain et artefact ; garde des tirages : course invalide ; sensibilité en écart absolu de 10 répétitions | Liste d'arrêt ; Gardes |
| 13 | Références | $B_{\text{rand}}(m)$ défini à toute marge ; lignes 364 à 393 ; commit de départ pris au scellement | En-tête ; Hypothèse |
