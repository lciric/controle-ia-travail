# Préenregistrement — épreuve, près de sa limite, de la garantie de seuil du théorème de mise en œuvre aléatoire des audits (papier D, chantier 3 : budget d'audit borné) — v1

Pièce décisive (classe A). Expérience sur processeur, 0 USD, aucune dépense de calcul. Brouillon de conception, ni contre-lu ni scellé ; rien n'a été tiré ni lu.

- Auteur : Claude Fable 5.2, sous-agent de conception, sur mandat de la session mère du papier D.
- Date (UTC) : 2026-11-24.
- Commit du code d'analyse : le script n'existe pas encore. Commit de départ `ee3d66103c8db495afe84cb10084981ebfb6d011`, branche `papier-d/evasion-post-entrainement-v1`. Le script (instrument, classe B, neuf et versionné, contre-lu par un autre modèle) est écrit après le scellement de ce texte, appelle `controle_ia.prereg.exiger_prereg_scelle` sur lui, et consigne son commit et son empreinte au manifeste du run (`src/controle_ia/manifeste.py`) avant le premier tirage.
- Documents qui font foi (chemin, empreinte SHA-256) :
  - énoncé visé, théorème « Randomised implementation » (`thm:audit-random`, lignes 364 à 390) : `papiers/D/theorie/brouillon-fable-budget-audit-v1/audit-budget-section-v1-correctif-1.tex`, `c6e5cebfe5fbf5c2d360bbd9ad042ba6e4626ac1b78de461ff0f99446b625727` ;
  - mise en œuvre numérique existante, fonction `sim()` : même dossier, `check_audit_v1.py`, `d786cba7fd23bb31abc5a2abe9dd378a912355e657b696d740bb74e987c4ab83` ;
  - proposition d'expérience : `papiers/D/audits/audit-reserves-chantier3-v1/note-garantie-seuil-non-eprouvee-chantier3-v1.md`, `0b8b643a62a6eef7a8e151a992d6717caedb980ac316c25d4251c325778b7a6c` ;
  - audit des deux réserves et son script : même dossier, `audit-reserves-chantier3-v1.md`, `54a00ef2989a42e17fd7ca80acf4c59c7a5a14bef33a00f18882b926f6f0ffd2` ; `audit_reserves_chantier3_v1.py`, `fb94751eaf9901ca8fc315197f2cc7cb1e7d1691684aa6933e9bfc755c366fef`.

## Hypothèse

**Objet.** Cette expérience ne porte aucune hypothèse numérotée du programme : elle éprouve un énoncé du brouillon du papier D. Motif : sur 800 000 répétitions, la simulation existante ne compte aucune violation du seuil ; tous ses échecs sont des dépassements de budget (`audit-reserves-chantier3-v1.md`, réserve 1). Elle n'approche donc jamais la région où la garantie de seuil pourrait échouer.

**Processus (celui du théorème, à la lettre).** $\Delta R>0$, $C\ge 0$, $W=\Delta R+C$, $\bar\rho=\Delta R/W$, $a=1-\gamma/\eta$ ($a=1$ si $\eta=\infty$), $c=\ell_{\text{crit}}+L$, $\hat x_k=\hat\ell_k+L$. Avec $\hat x_0=0$ et des tirages $A_k\sim\text{Binomiale}(n,\rho_k)$ indépendants (somme des $n$ audits de Bernoulli du tour $k$) :
$$\hat x_{k+1}=a\,\hat x_k+\gamma\Delta R-\gamma W\,A_k/n,\qquad k=0,\dots,K-1 .$$
Le plan $\rho(m)$, de marge $m\in[0,c]$, est le plan glouton en boucle ouverte, calculé une fois sur la trajectoire en champ moyen $x_k$ pour la marge de manœuvre $c-m$ : $\rho_k=\max\{0,(a x_k+\gamma\Delta R-(c-m))/(\gamma W)\}$, $x_{k+1}=a x_k+\gamma\Delta R-\gamma W\rho_k$. C'est le plan « juste à temps » du théorème déterministe. La marge de Bernstein est
$$\varepsilon=\gamma W\Bigl[\sqrt{2\bar\rho\,\Gamma_K\Lambda/n}+\tfrac{2\Lambda}{3n}\Bigr],\qquad \Gamma_K=\sum_{i<K}a^{2i},\quad \Lambda=\ln(2K/\delta).$$

**Garantie visée (G), partie (c) du théorème, première moitié.** Si $\varepsilon\le c$, sous le plan $\rho(\varepsilon)$ et pour le processus **sans plafond de budget** :
$$P\bigl(\max_{1\le k\le K}\hat\ell_k>\ell_{\text{crit}}\bigr)=P\bigl(\max_{1\le k\le K}\hat x_k>c\bigr)\le\delta/2 .$$
Le plafond $B_{\text{rand}}$ et la probabilité $\delta/2$ de le dépasser forment l'autre moitié ; elle n'est pas l'objet.

**Trois hypothèses.**
- H-a, garantie : (G) tient en tout point admissible de la grille.
- H-b, nécessité d'une marge : sous le plan sans marge $\rho(0)$, la probabilité de violation dépasse $\delta/2$ en tout point admissible. Le brouillon ne revendique pas cette nécessité (remarque `rem:audit-random`).
- H-c, prudence : la plus petite marge qui tient le niveau $\delta/2$, $\varepsilon_{\text{emp}}$, est strictement entre $0$ et $\varepsilon$.

**Hypothèses de travail.** Seuls les audits sont aléatoires ; la moyenne sur les actions de la politique est exacte ; le plan ne dépend pas des tirages ; la violation décroît quand la marge croît (contrôlée, voir les critères de lecture).

## Prédiction chiffrée et signe attendu

Avec $V(p,\lambda)$ la fréquence de violation au point $p$ sous le plan $\rho(\lambda\varepsilon)$ :

| | Prédiction | Signe | Réfutation |
|---|---|---|---|
| P1 | À $\lambda=1$ : $V\le\delta/2$ en tout point admissible. Attendu bien plus bas : $V\le\delta/20$ partout, zéro violation observée dans la plupart des points. | sous le seuil | un point classé « au-dessus de $\delta/2$ » (section Seuil) |
| P2 | À $\lambda=0$ : $V\ge 0{,}5$ en tout point admissible ; médiane des points $\ge 0{,}9$. | nettement positif | un point dont la borne haute est sous $0{,}5$ |
| P3 | $V$ ne croît pas avec $\lambda$ ; $V>\delta/2$ partout à $\lambda=0{,}1$ ; $V\le\delta/2$ partout à $\lambda=0{,}75$. | décroissant | une hausse significative, ou un point du mauvais côté |
| P4 | $\varepsilon_{\text{emp}}/\varepsilon\in[0{,}20\,;0{,}70]$ en tout point ; médiane dans $[0{,}35\,;0{,}55]$ ; la médiane par valeur de $\eta$ décroît quand $\eta$ croît ($1$, puis $10$, puis $\infty$). | rapport $<1$ | un point hors plage, médiane hors plage, ou ordre inversé |

**Justification, par raisonnement et sans tirage.** P2 : sans marge, la trajectoire en champ moyen touche le seuil dès le premier tour audité ; l'écart y est centré, d'où une chance voisine d'une sur deux par tour, et la grille compte au moins 24 tours tenus au seuil. P1 : à marge nominale, l'écart au seuil vaut à chaque tour au moins $\sqrt{2\Lambda}\ge 3{,}7$ écarts-types bornés, et l'écart-type réel est plus petit que sa borne ; estimé : plus de 4,5 écarts-types réels. P4 : le rapport est le produit de trois facteurs inférieurs à 1 — écart-type réel sur écart-type borné (0,6 à 0,8, car, selon le point, le taux tenu est sous $\bar\rho$ ou la variance n'est accumulée que sur une partie des tours) ; quantile réel du maximum sur $\sqrt{2\Lambda}$ (0,45 à 0,87, la borne d'union sur $K$ tours étant d'autant plus lâche que la mémoire $\eta/\gamma$ est longue) ; poids du terme linéaire (0,7 à 1). La plage de la note de proposition (0,2 à 0,6) est retouchée par ce calcul. P4 est une estimation : sa réfutation corrige le chiffre et ne touche pas aux verdicts sur la garantie.

**Descriptif, sans prédiction** : budget épargné $(B_\varepsilon-B_{\varepsilon_{\text{emp}}})/B^\star_{\text{unif}}(c)$ ; distance au seuil ; dépassement de budget ; bras en boucle fermée.

## Métrique

**Métrique primaire, seule.** Pour un point $p$ et une marge $m$, sur $R$ répétitions indépendantes du processus sans plafond de budget :
$$\hat V(p,m)=\frac1R\sum_{r=1}^{R}\mathbf 1\Bigl\{\max_{1\le k\le K}\hat x^{(r)}_k-c>\tau\Bigr\},\qquad \tau=10^{-9}\max(1,c).$$
Une égalité au seuil n'est pas une violation. Le dépassement de budget n'entre jamais dans cet indicateur : il est compté dans une variable distincte, $\hat O=\frac1R\sum_r\mathbf 1\{N^{(r)}>B_{\text{rand}}\}$, secondaire et descriptive, rapportée à côté de sa probabilité exacte par convolution. Aucune fréquence « violation ou dépassement » ne sert à un verdict.

**Intervalles.** Clopper-Pearson bilatéral à 95 % pour toute fréquence rapportée ; bornes unilatérales de Clopper-Pearson au niveau $10^{-4}$ pour les décisions.

**Marge empirique minimale.** $\varepsilon_{\text{emp}}(p)$ : borne haute finale d'une bissection sur $m\in[0,\varepsilon]$, dix itérations, $R$ tirages neufs chacune ; règle : $\hat V(m)\le\delta/2$ donne « haut $=m$ », sinon « bas $=m$ ». Elle n'est lancée que si le point est « au-dessus de $\delta/2$ » à $\lambda=0$ et « sous $\delta/2$ » à $\lambda=1$. Résolution numérique $\varepsilon/1024$ ; incertitude statistique déclarée de l'ordre de 2 % ; un tirage de confirmation à $m=\varepsilon_{\text{emp}}$ est rapporté avec son intervalle.

**Distance au seuil (descriptive).** Quantile empirique d'ordre $1-\delta/2$ de $\max_k\hat x_k-c$ à $\lambda=1$, divisé par $\varepsilon$, avec son intervalle par statistiques d'ordre. Cohérence attendue, non décisive : cette valeur plus 1 est proche de $\varepsilon_{\text{emp}}/\varepsilon$.

## Seuil

- Seuil de décision : $\delta/2$, soit 0,025 ou 0,05 selon le point.
- Classement d'une fréquence face à $\delta/2$ : **« sous »** si la borne haute unilatérale au niveau $10^{-4}$ est $\le\delta/2$ ; **« au-dessus »** si la borne basse unilatérale au niveau $10^{-4}$ est $>\delta/2$ ; **« indéterminé »** sinon. Avec $R=10^5$, la zone indéterminée couvre au plus environ $\pm 7$ % autour de $\delta/2$.
- Comparaisons multiples : 138 points au plus, niveau $10^{-4}$ par point, donc un risque d'ensemble de fausse réfutation inférieur à 1,4 %.
- Point indéterminé à $\lambda=1$ ou à $\lambda=0$ : une seule prolongation, $10^6$ tirages neufs, lus seuls avec le même classement.
- P2 : seuil 0,5, même forme de classement. P3 : une hausse entre deux valeurs voisines de $\lambda$ est significative si le test exact de Fisher unilatéral donne moins de $10^{-4}$.

## Plan d'analyse

**Grille.** $K\in\{50,200,500\}$, $n\in\{100,1000\}$, $\gamma\in\{0{,}05\,;0{,}2\}$, $\eta\in\{1\,;10\,;\infty\}$, $C\in\{4,19\}$, $\delta\in\{0{,}05\,;0{,}1\}$, $\Delta R=1$ : 144 points, numérotés dans cet ordre lexicographique. Facteur de marge $\lambda\in\{0\,;0{,}1\,;0{,}25\,;0{,}5\,;0{,}75\,;1\}$.

**Hors de la frontière.** En tout point, $c=\tfrac12\,\Delta R\,G_K$, avec $G_K=\gamma\sum_{i<K}a^i$ : la moitié de la charge finale sans audit. Donc $c<\eta\,\Delta R$ strictement, le budget optimal déterministe est positif partout, et aucun point n'est dégénéré. Cette règle remplace l'exemple de la note ($c=0{,}5\,\eta\Delta R$ et $c=1$), qui laisserait 8 points sans aucun audit et 30 points inadmissibles.

**Admissibilité.** Un point est admissible si $\varepsilon\le c$ (hypothèse du théorème). Arithmétique de conception, déterministe et sans tirage, à recalculer par le script : 138 points admissibles ; les 6 inadmissibles sont $n=100$, $\gamma=0{,}2$, $\eta=1$, $C=19$ ; sous le plan sans marge, au moins 24 tours tenus au seuil ($K-1-\kappa$) et au moins 2,5 audits attendus par tour tenu. Les points inadmissibles sont listés avec $\varepsilon$ et $c$, ni remplacés ni lus.

**Taille.** $R=10^5$ répétitions par point et par marge, par lots de $10^4$. À $\delta/2=0{,}025$, l'écart-type de $\hat V$ est de $4{,}9\times10^{-4}$, soit 2 % en relatif : une violation réelle de $1{,}15\,\delta/2$ est classée « au-dessus » presque sûrement. Charge : environ $6\times10^{10}$ tirages binomiaux, une à quelques heures sur un cœur.

**Graines (R9).** `numpy.random.SeedSequence(entropy=202611243003, spawn_key=(i_point, i_bloc, i_rang))`, générateur `numpy.random.Generator(numpy.random.PCG64(...))`, numpy $\ge 1{,}25$. Blocs : 0 à 5, les six valeurs de $\lambda$ ; 6, bissection (rang : itération 0 à 9, puis 10 pour la confirmation) ; 7, prolongation ; 8, audit de symétrie ; 9, bras en boucle fermée. Banc témoin : `i_point` $=1000$. Toutes les clés sont distinctes et consignées au manifeste, avec configuration, versions et commit.

**Ordre.** (1) gardes sur le banc témoin ; (2) recalcul de l'admissibilité ; (3) blocs 0 à 5 ; (4) prolongations ; (5) bissections ; (6) bras descriptif. Sorties brutes scellées avant toute lecture ; la table de lecture est appliquée par un sous-agent neuf, qui n'a écrit ni ce texte ni le script.

## Critères de lecture gelés

Verdict par point, puis verdict d'ensemble. Chaque conclusion est écrite d'avance.

| Issue observée | Verdict | Conclusion |
|---|---|---|
| À $\lambda=1$, tous les points admissibles « sous $\delta/2$ » ; à $\lambda=0$, tous « au-dessus de $\delta/2$ » | **« la garantie tient »** (confirmé, sur la grille) | « Pour le processus du théorème, la fréquence de violation du seuil à marge nominale est sous $\delta/2$ en chacun des points, là où l'instrument voit la violation dès que la marge est retirée. La simulation ne contredit pas la partie (c) ; elle ne la prouve pas et ne dit rien hors de ses hypothèses. » |
| À $\lambda=1$, un point au moins « au-dessus de $\delta/2$ », confirmé par la prolongation, audit de symétrie sans défaut d'instrument | **« garantie réfutée »** | « Au point $p$, la violation à marge nominale dépasse $\delta/2$ : la partie (c), ou la mise en œuvre qui la suit à la lettre, est fausse. Elle sort du brouillon jusqu'à correction ; nœud remonté à Lazar. » Ce verdict prime sur tous les autres. |
| À $\lambda=0$, un point « sous $\delta/2$ », audit de symétrie sans défaut | **« marge non nécessaire »** en ce point (H-b réfutée en ce point) | « En ce point, le plan sans marge tient déjà le niveau : la marge de Bernstein y est un surcoût sans contrepartie mesurée, et la garantie n'y est pas éprouvée. » D'ensemble si tous les points. |
| $0<\varepsilon_{\text{emp}}<\varepsilon$ | « marge nécessaire, surdimensionnée » (descriptif) | « Une marge est nécessaire ; celle du théorème dépasse le besoin mesuré d'un facteur $\varepsilon/\varepsilon_{\text{emp}}$ sur cette grille. » P4 est lue tenue ou réfutée à part. |
| À $\lambda=0$, $\hat V=0$, ou borne haute sous $0{,}5$, en un point | **« trop propre »** (R4) | Aucune conclusion avant l'audit ci-dessous. |
| Point indéterminé après prolongation ; hausse significative de $\hat V$ avec $\lambda$ ; bissection hors de l'encadrement donné par la grille de $\lambda$ | « non concluant » en ce point | Point listé ; sa marge empirique n'est pas rapportée. |

Combinaisons : « la garantie tient » d'ensemble exige tous les points admissibles ; sinon le compte rendu dit « tient en $N_1$ points, non éprouvée ou non concluante en $N_2$ », avec la liste. Zéro violation à $\lambda=1$ n'est pas, seule, une confirmation : elle ne vaut que jointe aux violations vues à $\lambda=0$ au même point.

**Audit de symétrie (R4), le même dans les deux sens.** Déclenché par « trop propre » et par toute réfutation à $\lambda=1$, avant de prononcer. Au point visé, graines du bloc 8 : (1) le plan atteint bien sa cible en champ moyen, $\max_k x_k=c-m$ à $10^{-9}\max(1,c)$ près, et sa somme égale la forme close de $B^\star_{\text{unif}}(c-m)/n$ ; (2) recomptage de l'événement par un second chemin indépendant (audits tirés épisode par épisode, $\hat x_k$ recalculé par la somme explicite et non par la récurrence), comparé répétition par répétition sur $10^4$ tirages ; (3) moyenne et variance empiriques de $\hat x_K$ comparées à leurs valeurs exactes ; (4) fréquence de violation au premier tour audité comparée à $P(\text{Binomiale}(n,\rho_\kappa)<n\rho_\kappa)$. Sans défaut : la lecture tient et le verdict est prononcé avec la mention de l'audit. Avec défaut : course invalide, script corrigé sous un nouveau nom, relance complète sur une racine de graines neuve ; les deux courses sont rapportées.

## Liste d'arrêt

Tout arrêt est bruyant et journalisé ; aucun repli silencieux ; rien n'est lu d'une course arrêtée.

1. Ce texte n'est pas scellé ou son empreinte ne se vérifie pas : refus de partir.
2. Une garde échoue sur le banc témoin, ou ne se déclenche pas sur son artefact : arrêt avant tout tirage de la grille.
3. L'admissibilité recalculée diffère de 138 points, ou le minimum de tours tenus diffère de 24 : arrêt, erratum.
4. Valeur non finie, taux hors de $[0,\bar\rho+10^{-12}]$, clé de graine en double, fichier de sortie déjà présent : arrêt.
5. Sensibilité à la tolérance : si la fréquence recalculée avec $\tau'=10^{-6}\max(1,c)$ s'écarte de plus de 5 % en relatif à une marge non nulle, le point est « non concluant ».
6. Plus de 12 heures de calcul, ou perte de la machine : panne technique, pas un résultat ; relance entière avec les mêmes graines.
7. Toute lecture partielle avant la fin et le scellement des sorties invalide la course.

### Gardes, chacune testée sur un cas sain et sur un artefact (R5)

**Banc témoin à vérité exacte**, hors de la grille : $\eta=\gamma=0{,}2$ (donc $a=0$, tours indépendants), $K=20$, $n=1000$, $\Delta R=1$, $C=4$, $c=0{,}1$, $\delta=0{,}05$ ; admissible ($\varepsilon\approx 0{,}056$, arithmétique de conception, à recalculer), $n\rho_0=100$ entier. Le plan de marge $m$ y est constant, $\rho_m=(\gamma\Delta R-c+m)/(\gamma W)$, et la probabilité de violation est exacte : $P^\star(m)=1-\bigl[1-F_{\text{Binomiale}(n,\rho_m)}(n\rho_0-1)\bigr]^K$. Une garde passe si $|\text{compte}-R\,P^\star|\le 5\sqrt{R\,P^\star(1-P^\star)}+3$, pour $m\in\{0,\varepsilon/2,\varepsilon\}$ et $R=10^5$.

| Garde | Cas sain (doit passer) | Artefact (doit arrêter) |
|---|---|---|
| Plan : cible atteinte en champ moyen, taux bornés, somme égale à la forme close | plan sans marge du banc témoin, qui touche le seuil et **doit violer** à la fréquence $P^\star(0)$ | plan annoncé sans marge mais construit avec la marge $\varepsilon$ |
| Compteur de l'événement, contre $P^\star$ aux trois marges | compteur de la métrique primaire | **événement mal compté**, trois variantes : violation lue au seul dernier tour ; violation fusionnée avec le dépassement de budget ; seuil comparé à $c-m$ au lieu de $c$ |
| Tirages : moyenne, sur les $R$ répétitions, du nombre total d'audits à moins de 5 erreurs types de $n\sum_k\rho_k$, en chaque point | tirages du plan | taux décalés de 10 % au tirage |

Les essais de ces gardes vivent avec le script et passent avant la course.

## Hors du champ, non revendiqué

- **Boucle fermée** (plan recalculé à chaque tour sur la trajectoire réalisée) : bras descriptif, $\lambda\in\{0,1\}$, mêmes points, bloc de graines 9, table à part titrée « descriptif, sans verdict ». Aucune garantie n'y est énoncée ni éprouvée.
- **Entraînement par gradient stochastique**, bruit d'échantillonnage des actions de la politique : non modélisé par le théorème, non lancé sous ce texte ; toute course demanderait son propre texte.
- La moitié « budget » de la partie (c), la partie (a) bilatérale, l'inflation de budget : descriptives ici.
- Le caractère serré ou lâche de la borne hors de cette grille (autre marge de manœuvre que $c=\tfrac12\Delta R\,G_K$, $\eta=\gamma$, $\Delta R\ne1$, points inadmissibles), les audits reconnaissables ou faillibles.
- « La garantie tient » ne vaut jamais preuve du théorème ni validation d'une sonde ou d'un protocole du programme.

## Contre-lecture

En attente. Section à compléter par la session mère après la contre-lecture par un sous-agent neuf d'un autre modèle (R2) : identifiant du contre-lecteur, empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque. Le validateur refuse le scellement tant que ces deux empreintes manquent.
