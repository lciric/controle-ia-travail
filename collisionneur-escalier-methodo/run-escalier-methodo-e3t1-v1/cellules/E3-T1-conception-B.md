# Proposition B — Tour III.1 : comparer des configurations à coût croissant

**Pièces.** Le bloc FAITS ne contient aucun fait ; il n'est pas coupé et je n'en invente aucun. Ce tour se joue à l'aveugle : je ne vois ni A ni C, la règle B1 ne peut donc pas s'appliquer ici.

**Conventions.**
- Tout ce qui vient de l'énoncé de l'arbitre porte le statut RAPPORTÉ. Ce que j'ajoute est HYPOTHÈSE.
- Les calculs sont montrés et chacun peut les refaire ; ce ne sont pas des faits.
- Tout chiffre de paramètre qui ne vient pas de l'énoncé est marqué « illustratif ».

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Ce qui en dépend |
|---|---|---|---|
| a1 | Jeu de 60 items : famille 1 = 36 stratifiés, famille 2 = 12 positifs / 12 négatifs. Mêmes items pour toutes les configurations. | RAPPORTÉ | Toute la puissance. |
| a2 | La famille 1 est équilibrée (18/18). « Stratifiés » ne le dit pas. | HYPOTHÈSE | Le poids d'un item dans la BA : 1/36 si équilibré, sinon 1/(2p) ou 1/(2(36−p)). |
| a3 | On cherche à savoir si la configuration est meilleure sur la *population* d'items, et non sur *ces* 60 items. | HYPOTHÈSE (non tranchée par l'énoncé) | C'est le point qui décide si des graines supplémentaires servent à quelque chose (voir §1). |
| a4 | La graine contrôle tout l'aléa, y compris les rondes de mise au point. Le fournisseur d'API est déterministe à graine fixée. | HYPOTHÈSE | La structure de la variance entre graines. |
| a5 | La variance entre graines ne dépend pas de la configuration. Or plus de sous-modèles devrait réduire la variance. | HYPOTHÈSE | Variance du contraste, choix du test. |
| a6 | « 10–22 USD par itération » : on ne sait pas si l'unité est l'exécution complète sur 60 items ou l'itération d'amélioration. | RAPPORTÉ (chiffre illustratif selon l'énoncé), unité non établie | Tout calcul de coût ci-dessous. |
| a7 | La dépense $s(b)$ est observable par item et par exécution. | HYPOTHÈSE | Dose-réponse, variable instrumentale. |
| a8 | Le jeu de test n'a jamais servi à la mise au point. | RAPPORTÉ, non audité | La validité de toute comparaison. |
| a9 | Les axes ont des effets monotones, à peu près additifs, et un « plateau » existe. | HYPOTHÈSE | La logique même d'un escalier. |
| a10 | Le modèle sous-jacent ne change pas pendant la campagne. | HYPOTHÈSE | Exécuter les crans à des dates différentes confond l'effet du cran avec une dérive du modèle. |
| a11 | « Item sans réponse valide = erreur ». | RAPPORTÉ | L'axe « longueur max » peut agir mécaniquement, par troncature, et non par la qualité des réponses. |
| a12 | Il existe une valeur en dollars d'un point de BA. | HYPOTHÈSE (à fixer par l'arbitre) | La perte bayésienne et le coût par point. |
| a13 | Les deux familles se décident ensemble ou séparément : non précisé. Elles partagent les mêmes exécutions, donc elles sont dépendantes. | HYPOTHÈSE | Multiplicité, puissance jointe. |
| a14 | Les deux répliques gratuites sont indépendantes de toute décision antérieure. | RAPPORTÉ (« lues au moment fixé ») | Leur usage comme cas A/A honnête. |

---

## Noyau calculatoire (points 0 à 4 de la question)

### §1. Modèle de variance de $\widehat{\Delta\mathrm{BA}}$ et puissance (point 1)

**Granularité, en famille 2.** La famille 2 est équilibrée, donc
$$\mathrm{BA}=\frac{TP+TN}{24}.$$
Chaque item pèse 1/24 ≈ 0,042. En nombre net d'items basculés, avec une seule graine :
- δ = 0,05 correspond à 1,2 item, donc il faut au moins 2 items ;
- δ = 0,10 correspond à 2,4 items, donc 3 items ;
- δ = 0,15 correspond à 3,6 items, donc 4 items.

En famille 1, sous a2 (18/18), un item pèse 1/36 ≈ 0,028 ; les seuils deviennent 2, 4 et 6 items nets.

**Modèle à deux niveaux.** On note :
- $Y_{ijk}\in\{0,1\}$ : réussite de l'item $i$, configuration $j$, graine $k$ ;
- $p_{ij}=\mathbb{E}[Y_{ijk}]$ ;
- $d_i=p_{iB}-p_{iA}$.

On décompose
$$Y_{ijk}=p_{ij}+\gamma_{jk}+\varepsilon_{ijk}.$$
- $\gamma_{jk}$ est un effet d'exécution partagé par tous les items. C'est plausible dès que les rondes de mise au point dépendent de la graine (a4).
- $\varepsilon$ est le bruit item × graine, de variance moyenne $\bar v=\overline{p(1-p)}$.

Avec $r$ graines par bras et $n$ items dans une famille équilibrée :
$$\mathrm{Var}(\widehat{\Delta})=\underbrace{\frac{\sigma_I^2}{n}}_{\text{items (si inférence population)}}+\frac{2}{r}\Big(\sigma_\gamma^2+\frac{\bar v}{n}\Big),\qquad \sigma_I^2=\mathrm{Var}_i(d_i).$$

Le premier terme ne diminue pas quand on ajoute des graines. Sa taille dépend de la forme de l'effet :
- **Effet diffus** ($d_i\approx\Delta$ pour tous les items) : $\sigma_I^2\approx0$.
- **Effet concentré**, items quasi déterministes, $k$ items basculent entièrement et aucun ne se dégrade : $\sigma_I^2=\Delta(1-\Delta)$.
- **Basculements dans les deux sens** (cas général) : $\sigma_I^2\approx\pi_d-\Delta^2$, où $\pi_d$ est la part d'items discordants.

**Condition de puissance.** Test unilatéral avec α = 0,05 et puissance 0,80 : $z_{0,95}+z_{0,80}=1{,}645+0{,}842=2{,}487$. Il faut donc $\mathrm{SE}\le\delta/2{,}487$ :

| δ | 0,05 | 0,10 | 0,15 |
|---|---|---|---|
| SE maximale | 0,0201 | 0,0402 | 0,0603 |

**Régime P — inférence sur la population d'items.** Cas le plus favorable : basculements concentrés, aucun item dégradé, $r\to\infty$.

*Famille 2 seule* : $\mathrm{SE}=\sqrt{\Delta(1-\Delta)/24}$.

| Δ vrai | SE | Puissance approchée (normale) |
|---|---|---|
| 0,05 | 0,0445 | Φ(1,124−1,645) ≈ 0,30 |
| 0,10 | 0,0612 | Φ(1,634−1,645) ≈ 0,50 |
| 0,15 | 0,0729 | Φ(2,058−1,645) ≈ 0,66 |

L'approximation normale est complaisante. Avec le test exact de McNemar, dans le cas idéal où $c=0$, il faut $b\ge5$ pour que $0{,}5^5=0{,}031<0{,}05$ en unilatéral. Cela correspond à $\Delta\ge5/24=0{,}208$.

> En régime P, la famille 2 seule ne peut détecter aucun des trois δ proposés à 80 % de puissance, quel que soit le nombre de graines.

*Indice poolé* $\tfrac12(\mathrm{BA}_1+\mathrm{BA}_2)$, sous a2 :
$$\mathrm{Var}=\Delta(1-\Delta)\cdot\tfrac14\big(\tfrac1{36}+\tfrac1{24}\big)=0{,}01736\,\Delta(1-\Delta).$$

| Δ vrai | SE | Puissance |
|---|---|---|
| 0,05 | 0,0287 | ≈ 0,54 |
| 0,10 | 0,0395 | ≈ 0,80 (juste) |
| 0,15 | 0,0470 | ≈ 0,94 |

Ce sont des bornes optimistes. Dès que des items se dégradent ($\pi_d>\Delta$), la puissance chute.

**Régime C — inférence conditionnelle aux 60 items.** Seul le bruit des graines compte. Valeurs illustratives :
- taux de désaccord entre répliques $q=0{,}10$, d'où $\bar v=q/2=0{,}05$ (car $P(\text{désaccord})=2p(1-p)$) ;
- $\sigma_\gamma=0{,}02$.

En famille 2 : $\mathrm{Var}=2(0{,}0004+0{,}05/24)/r=0{,}00497/r$. Il faut $r\ge 0{,}00497/\mathrm{SE}_{\max}^2$.

| δ | $r$ par bras | Coût de la paire, à $c$ = 20 USD par exécution (illustratif) | Avec les 2 répliques gratuites pour le bras de base |
|---|---|---|---|
| 0,15 | 2 (1,37 arrondi) | 80 USD | 40 USD |
| 0,10 | 4 (3,08) | 160 USD | 120 USD |
| 0,05 | 13 (12,3) | 520 USD | 480 USD |

Ces nombres ne valent que sous les paramètres illustratifs. Ils changent d'ordre de grandeur si $\sigma_\gamma$ vaut 0,05.

**Ce que valent les deux répliques gratuites.** Elles fournissent deux informations de qualité très différente.

1. *Le désaccord item par item* $\hat q$ repose sur 60 items. Il estime $\bar v$ correctement.
2. *L'écart de BA entre les deux répliques* $D$ vérifie $\mathrm{Var}(D)=2\sigma_\gamma^2+2\bar v/n$. Il ne fournit qu'un seul degré de liberté. Avec 1 ddl, l'intervalle à 95 % pour la variance vaut $[s^2/5{,}024 ;\ s^2/0{,}000982]\approx[0{,}20\,s^2 ;\ 1018\,s^2]$. Autrement dit, $\sigma_\gamma^2$ n'a **aucune borne supérieure utile**.

> Les données gratuites estiment le bruit item × graine. Elles n'estiment pas l'effet d'exécution partagé.

Elles indiquent aussi dans quel régime on se trouve :
- un $\hat q$ faible signifie des items quasi déterministes : les graines n'aident pas, il faut des items ;
- un $\hat q$ élevé signifie que le bruit des graines domine : les graines rapportent.

**Cohérence avec l'autre analyse du programme**, qui exige $\Delta\ge+0{,}10$ (RAPPORTÉ). Si cette exigence porte sur l'estimation ponctuelle, sa puissance vaut environ 50 % quand l'effet vrai est exactement 0,10. Si elle porte sur la borne basse de l'intervalle, elle exige un effet vrai d'environ 0,20 sur 60 items. Les deux lectures sont incompatibles avec un δ = 0,05 retenu ici. L'arbitre doit en choisir une.

### §2. L'escalier (point 0)

**Ordre des axes — deux voies.**
- **(V1) Coût fixe d'abord.** Les rondes de mise au point sont payées une fois, environ 10 USD la ronde (illustratif, RAPPORTÉ comme ordre de grandeur). Elles sont amorties. Les axes à coût variable (sous-modèles, itérations, longueur) se paient à chaque item traité.
  - Conséquence : $\partial\mathrm{BA}/\partial\$$ n'a de sens qu'avec un horizon d'usage. Il faut deux colonnes : coût unique et coût par 1000 items.
- **(V2) Validité d'abord.** Commencer par la longueur maximale, parce qu'une troncature compte comme une erreur (a11).
  - On mesure séparément le taux de réponses valides. Un cran qui ne fait que restaurer la validité ne mesure pas la qualité.
  - Le contrôle est la BA restreinte aux items valides dans les deux bras.

**Définition d'un cran.**
- **Doublement sur un axe à la fois.** Les plateaux apparaissent typiquement en échelle logarithmique (HYPOTHÈSE). C'est simple et compatible avec un test en séquence fixe (§3).
- **Pas fixe en dollars.** Il rend le coût par point comparable d'un axe à l'autre. En revanche, les crans ne sont pas réalisables exactement, puisque $s(b)\ne b$.
- **Plan factoriel fractionnaire $2^{4-1}$** (résolution IV, 8 configurations). Chaque effet principal se calcule comme moyenne(niveau haut) − moyenne(niveau bas), sur 4 exécutions contre 4 : $\mathrm{Var}=4\sigma^2/N=\sigma^2/2$ pour $N=8$, et ce pour chacun des 4 axes.
  - Un axe à la fois avec la même variance par effet exige 4 exécutions pour la base et 4 par niveau haut, soit 20 exécutions.
  - Le factoriel est donc environ 2,5 fois plus efficace **en nombre d'exécutions**. C'est vrai sous additivité ; les interactions à deux facteurs sont aliasées entre elles.
  - Mais il exécute d'emblée les coins chers. **En dollars**, l'avantage peut s'inverser. Ce qui départage : le rapport de coût entre le coin le plus cher et la base, et l'existence probable d'interactions, par exemple sous-modèles × longueur.

**Valeur marginale et plateau.**
- Pour chaque cran, on calcule $\widehat{\Delta\mathrm{BA}}_{k\to k+1}/\Delta\bar s$.
- On déclare un plateau **seulement si la borne haute** de l'intervalle à 90 % de Δ est inférieure à δ. C'est une logique d'équivalence. L'absence de différence significative n'est pas un plateau.
- Sur 60 items, en régime P, un plateau n'est démontrable qu'à δ ≥ 0,15 environ.

**Confusion entre $b$ et $s(b)$ — trois voies.**
- **Intention de traiter sur $b$.** $b$ est assigné, donc l'analyse n'est pas confondue. Elle répond à la question opérationnelle : « que se passe-t-il si j'accorde $b$ ? ». C'est le critère primaire proposé.
- **Dose-réponse sur $s$.** Elle est confondue : le système dépense plus sur les items difficiles. La corrélation entre dépense et réussite par item peut donc être négative même si la dépense aide. Elle est inutilisable comme effet causal.
- **Variable instrumentale.** On instrumente $s$ par $b$ : estimateur de Wald $\widehat{\Delta\mathrm{BA}}/\Delta\bar s$.
  - Il exige que $b$ n'agisse que via $s$ (restriction d'exclusion). Cela est douteux si le budget change la *stratégie*, et pas seulement la quantité dépensée.
  - L'instrument est faible si $\Delta\bar s$ est petit : le ratio est instable et l'intervalle s'obtient par la méthode delta ou par rééchantillonnage.
  - C'est utile pour le coût par point, pas pour décider.

**Transposabilité d'une version à la suivante.** Une nouvelle version modifie la fonction $s(b)$. Des crans définis en $b$ ne se transposent donc pas tels quels. Des crans définis en $\bar s$ réalisé se transposent peut-être. C'est l'objet de l'expérience E4.

### §3. Analyse et règle gelée (points 2 et 3)

| Méthode | Avantage ici | Piège ici |
|---|---|---|
| Rééchantillonnage apparié à deux niveaux (items stratifiés par classe, puis graines) | Respecte la BA et l'appariement. | Avec $r=2$, rééchantillonner les graines n'a pas de sens. Les intervalles percentiles sous-couvrent avec 24 items. Il faut garder 12/12 à chaque tirage. |
| McNemar exact | Exact et transparent. Le nombre minimal de basculements est calculable (§1). | Une seule graine par bras. Il ignore $\sigma_\gamma$. Il ne correspond à la BA que si la famille est équilibrée ; en famille 1 sous a2 faux, il faut un test de signe pondéré par classe. Empiler les graines comme des items revient à de la pseudo-réplication. |
| Modèle logistique mixte : réussite ~ config + (1\|item) + (1\|graine:config) | Sépare explicitement $\sigma_I$ et $\sigma_\gamma$. | Avec 2 à 4 graines, l'ajustement est singulier : $\sigma_\gamma$ est estimé à 0, ce qui donne une fausse confiance. |
| Bayésien avec perte : monter si $\mathbb{E}[\Delta]\cdot V>\Delta\text{coût}$ | Intègre directement le coût et la règle « la moins chère à égalité ». | $V$ n'est pas établi (a12). L'a priori sur $\sigma_\gamma$ pèse lourd puisqu'il n'y a qu'1 ddl ; il doit être scellé. |
| Séquentiel par lots de graines, fonction de dépense de Lan–DeMets | Arrêt précoce, coût réduit. | En régime P, ajouter des graines ne réduit pas $\sigma_I^2/n$. Seul l'arrêt pour futilité est rentable. Les bornes sont à calculer, je ne les donne pas de mémoire. |

**Règle gelée (proposition, une voie parmi d'autres).** Pour chaque cran $k\to k+1$, dans l'ordre scellé :
- **Monter** si la borne basse de l'intervalle à 95 % unilatéral est supérieure à 0 **et** $\widehat\Delta\ge\delta$.
- **Rester (plateau)** si la borne haute de l'intervalle à 90 % est inférieure à δ.
- **Zone grise** sinon. On reste, puisque la moins chère l'emporte, et on consigne.
  - Option scellée à l'avance : un seul lot de graines supplémentaire, avec dépense d'erreur.

Le coût par point vaut $\Delta\text{coût}/(100\cdot\widehat\Delta)$, publié avec son intervalle, jamais seul.

**Pièges.**
- **Multiplicité sur plusieurs crans.** Le test en *séquence fixe* contrôle le taux d'erreur familial au niveau α sans correction, à deux conditions : l'ordre est scellé et on s'arrête au premier non-rejet. L'escalier s'y prête naturellement. Changer d'axe en cours de route en fonction des résultats casse cette garantie.
- **Familles.** Deux voies :
  - exiger les deux familles (test intersection-union, pas de correction) : la puissance jointe vaut environ le produit des puissances, de l'ordre de 0,64 si chacune est à 0,8, en supposant l'indépendance ;
  - utiliser l'indice poolé : plus puissant, mais il peut masquer une dégradation en famille 2.

  Les familles sont positivement corrélées par $\gamma$ (mêmes exécutions).
- **Régression vers la moyenne.** La configuration retenue est surestimée. Rejouer ses graines fraîches retire le biais lié aux graines, pas celui lié aux items.
- **Graine aberrante.** Une exclusion n'est permise que pour un critère mécanique scellé, par exemple un taux d'erreurs d'API supérieur à x. Jamais pour la BA obtenue.
- **Effet plafond.** Le classifieur trivial atteint déjà 0,69 en famille 1 (RAPPORTÉ). La marge de progression y est faible. Il faut rapporter la BA sur les items que le classifieur trivial rate.
- **Items faciles.** Les items réussis par toutes les configurations ne biaisent pas Δ, mais ils ne contribuent pas à la puissance.
- **Réutilisation des 60 items.** Avec $m$ décisions adaptatives, la borne prudente est α/m (Bonferroni) pour l'ensemble.
  - Une réserve intouchée prise *dans* les 60 items est inutile : un tiers de la famille 2 fait 8 items, et le test de signe exige 5 basculements sur 8, soit $\Delta\ge0{,}625$.
  - Le holdout réutilisable ajoute un bruit incompatible avec une granularité de 1/24.
  - **Conséquence :** les 60 items servent à *sélectionner*. Toute confirmation exige des items neufs. Faute de quoi, le résultat est « sélectionné, non confirmé ».
- **Audit des résultats trop propres.** Sous l'hypothèse nulle, la probabilité que $b+c$ discordants aillent tous dans le même sens vaut $2\cdot0{,}5^{b+c}$. Par exemple 0,016 pour 7 discordants. On scelle un seuil de déclenchement de l'audit dans les deux sens, y compris pour un Δ exactement nul avec beaucoup de discordants.

### §4. Alternatives (point 4)

- **Élimination successive et Hyperband.** Leur intérêt tient au grand nombre de configurations et à une basse fidélité qui préserve le classement.
  - Ici, peu de configurations.
  - Une basse fidélité par sous-échantillonnage des items, 30 ou 15, donne une SE environ 1,4 à 2 fois plus grande que sur 60 (racine du rapport des tailles, sous le même modèle). Le classement à basse fidélité est donc majoritairement du bruit pour δ ≤ 0,10.
  - Une basse fidélité par moins d'itérations est plus défendable, si l'ordre des configurations à 1 itération prédit celui à N itérations. C'est testable.
- **Bandits sous contrainte de budget.** Ils optimisent un regret cumulé, pas une décision avec erreur contrôlée. L'identification du meilleur bras à budget fixe est plus proche, mais elle suppose des tirages indépendants. Or ici un « tirage » est une exécution sur les mêmes 60 items.
- **Optimisation bayésienne multi-fidélité.** Elle exige assez d'évaluations pour ajuster un modèle de substitution sur 4 dimensions. Avec 10 à 20 exécutions (illustratif), le modèle reflète surtout son a priori.

**Ce qui départage ces méthodes :** le nombre de configurations candidates, le rapport δ / SE, et la monotonie du classement entre fidélités. Avec moins d'une dizaine de configurations et SE ≈ δ, l'escalier en séquence fixe reste compétitif (HYPOTHÈSE, testée en E5).

---

## (b) Expériences décisives, en duels

### E1 — D'où vient la variance ?
- **H_A** : le bruit est surtout item × graine ($\sigma_\gamma\approx0$).
- **H_B** : un effet d'exécution partagé, induit par la mise au point, domine.
- **Protocole.** 6 répliques de la configuration la moins chère (illustratif), dont les 2 gratuites.
- **Métrique.** $R=\widehat{\mathrm{Var}}(\mathrm{BA}_k)\big/(\bar v/n)$, avec 5 ddl au numérateur.
- **Seuil scellé.** $R>2$, borne basse de l'intervalle comprise.
- **Contrôle négatif.** 6 répliques où la mise au point est *figée* (même prompt mis au point) et où seul l'échantillonnage varie. On doit observer $R\approx1$. Sinon, la décomposition est fausse.
- **Falsification.**
  - Si la borne haute de l'intervalle de $R$ est inférieure à 2, H_B est réfutée à cette amplitude.
  - Si la borne basse est supérieure à 2, H_A est réfutée.
- **Enjeu.** Sous H_B, les graines coûtent cher mais rapportent. Sous H_A, la puissance se joue sur les items.

### E2 — Les items sont-ils quasi déterministes ?
C'est ce qui décide entre les régimes P et C en pratique.
- **H_A** : $\hat q\le0{,}05$ (illustratif) ; les graines supplémentaires ne valent rien en régime P.
- **H_B** : $\hat q\ge0{,}15$ (illustratif).
- **Métrique.** Désaccord item par item entre répliques, sur 60 items, avec un intervalle binomial.
- **Contrôle négatif.** Décodage glouton sur un modèle ouvert servi localement : on attend $\hat q=0$. Une valeur non nulle signale une source d'aléa non contrôlée (lot, matériel).
- **Falsification.** Un intervalle de $\hat q$ entièrement au-dessus de 0,05 réfute H_A ; entièrement au-dessous de 0,15, il réfute H_B. Un intervalle entre les deux est une zone grise déclarée.

### E3 — Le budget agit-il seulement par la dépense ?
- **H_A** : la restriction d'exclusion tient ; $b$ n'agit que via $s$.
- **H_B** : $b$ change la stratégie à dépense égale.
- **Métrique.** $\widehat{\Delta\mathrm{BA}}$ sur les items où $|s_B-s_A|<\varepsilon$ (seuil scellé).
- **Prédiction.** Sous H_A, cet écart vaut à peu près 0.
- **Limite dite.** Stratifier sur une variable post-traitement est biaisé. C'est donc un diagnostic, pas une estimation causale. La réfutation n'est forte que si l'écart est grand.
- **Contrôle négatif.** Paire A/A (répliques gratuites) : on attend Δs ≈ 0 et ΔBA ≈ 0.
- **Falsification.**
  - Un $\widehat{\Delta\mathrm{BA}}$ significatif, de signe constant sur ces items, réfute H_A et rend la variable instrumentale inutilisable.
  - Un Δs non nul en moyenne avec un ΔBA nul dans les deux strates est incompatible avec une H_B forte.

### E4 — Transposabilité d'une version à la suivante
- **H_A** : le signe et l'ordre des effets par axe sont conservés d'une version à la suivante.
- **H_B** : il existe une interaction version × axe.
- **Protocole.** Rejouer, sous la nouvelle version, les deux crans les moins chers de chaque axe.
- **Métrique.** Terme version × axe dans le modèle mixte, et accord des signes.
- **Contrôle négatif.** Même version, deux dates différentes : estime la dérive pure.
- **Falsification.**
  - Une interaction significative, au-delà de la dérive mesurée, réfute H_A.
  - Un accord des signes avec une interaction dont la borne haute est inférieure à δ réfute H_B.

### E5 — Malédiction du gagnant sur 60 items
- **H_A** : l'avantage de la configuration retenue se retrouve sur des items neufs, avec un rétrécissement inférieur ou égal à 50 %.
- **H_B** : l'avantage chute de plus de 50 %.
- **Prérequis.** Un jeu neuf de même structure. Il n'est **pas** dans les faits.
- **Contrôle négatif.** Même mesure sur une configuration *non* retenue de même coût. On attend un rétrécissement voisin de 0.
- **Falsification.** Le rapport $\Delta_{\text{neuf}}/\Delta_{60}$ et son intervalle tranchent dans un sens ou dans l'autre.

### E6 — Escalier contre factoriel, à dollars égaux (par simulation)
- **H_A** : à budget égal, l'escalier sélectionne une configuration à moins de δ de la meilleure plus souvent.
- **H_B** : le $2^{4-1}$ le fait plus souvent.
- **Protocole.** Simulation paramétrée par les variances mesurées en E1 et E2, et par les coûts réels par coin.
- **Contrôle négatif.** Un monde simulé sans aucun effet : les deux méthodes doivent choisir la configuration la moins chère à au moins 1−α.
- **Falsification.** L'écart de taux de bonne sélection, avec son intervalle Monte-Carlo, tranche.

---

## (c) Instruments : la mesure minimale qui dit s'ils fonctionnent

**Banc commun, fait de cas honnêtes appariés tirés d'exécutions réelles :**
- **Cas A/A.** Deux répliques d'une même configuration, à commencer par les 2 répliques gratuites, puis les répliques d'E1. Le Δ vrai est nul. On y mesure le **taux de fausses alertes**.
- **Cas A/B implantés.** On part d'exécutions réelles de A et on construit un « B » en basculant 2, 3, 4 ou 6 items. Deux formes :
  1. *Concentrée* : $k$ items ratés deviennent réussis.
  2. *Diffuse* : on rééchantillonne, pour chaque item, une réponse d'une autre réplique avec probabilité augmentée.

  Le Δ vrai est connu. On y mesure le **taux de détection** à δ = 0,05, 0,10 et 0,15.

  Biais dit : la forme concentrée favorise McNemar. Les deux formes sont donc obligatoires.

**Vérifications mécaniques à battre :**
- **M1** : la règle brute $\widehat\Delta\ge0{,}10$ sur une graine ;
- **M2** : un test de signe exact sur les discordants ;
- **M3** : une permutation des étiquettes de bras au sein de chaque item.

> Un instrument qui ne détecte pas mieux que M2, à taux de fausses alertes égal, ne justifie pas sa complexité.

| Instrument | Ce qui le valide | Cas | À battre |
|---|---|---|---|
| Rééchantillonnage à deux niveaux | Fausses alertes ≤ α nominal ; couverture de l'intervalle ≥ 0,9 pour un nominal de 0,95 | A/A, A/B implantés | M2, M3 |
| McNemar exact | Fausses alertes ≤ α (attendu : test conservateur) ; détection | idem | M1 |
| Modèle mixte | Fausses alertes ; part des ajustements singuliers ; erreur sur $\sigma_\gamma$ | A/A avec $\sigma_\gamma$ connu, simulé | M3 |
| Bayésien avec perte | Taux de décisions « monter » à tort ; perte réalisée | A/A, A/B implantés | M1 |
| Séquentiel | Fausses alertes globales sur toutes les analyses intermédiaires ; graines économisées | A/A, A/B implantés | Plan fixe à $r$ égal |
| Variable instrumentale et dose-réponse | Biais du ratio quand l'exclusion est violée exprès (on implante un effet de $b$ à $s$ constant) | A/B implantés avec violation | ITT seule |
| Détecteur de plateau (équivalence) | Taux de « plateau » déclaré alors que Δ vrai = δ (doit rester ≤ α) | A/B implantés à Δ = δ | « non significatif = plateau » (règle naïve) |
| Audit « trop propre » | Taux de déclenchement sur cas honnêtes A/A et A/B, à fixer à l'avance | A/A, A/B implantés | Aucun audit (mesure le coût de l'audit) |
| Séquence fixe sur plusieurs crans | Taux d'erreur familial sur un escalier simulé sans effet | Simulation | Tests non corrigés |
| Élimination successive, Hyperband, bandits, optimisation multi-fidélité | P(choisir une configuration à moins de δ de la meilleure) ; dollars dépensés | Simulation E6 | « Toujours la moins chère » ; « max $\widehat\Delta$ sur une graine » |
| Classifieur trivial (0,69 / 0,50, RAPPORTÉ) | Son propre écart A/A : il est déterministe, on attend 0 | Rejeu | — (c'est lui-même un plancher) |

---

## (d) Ancrage matériel

**Modèles ouverts.** On peut répliquer la *structure de variance* sur des modèles à poids ouverts servis localement : familles Llama, Qwen, Mistral, en tailles 7B à 70B. Le décodage déterministe y sert de contrôle négatif pour E1 et E2. L'usage est méthodologique : on ne transpose pas la BA au système réel.

**Calcul.**
- Les simulations (§1, E6, banc (c)) ne demandent que du CPU, quelques minutes à quelques heures (illustratif).
- Un modèle de 7B à 8B sur 60 items est trivial sur un seul GPU (illustratif).

**Coût en dollars, en reprenant l'échelle de l'énoncé.** Exécution à environ 20 USD (illustratif) ; unité ambiguë (a6).

| Poste | Coût |
|---|---|
| E1 : 4 répliques en plus des 2 gratuites, plus 6 répliques de contrôle | ≈ 200 USD |
| E2 | Inclus dans E1 |
| Escalier de 4 crans à δ = 0,10, régime C, $r=4$ | ≈ 5 × 4 × $\bar c$, soit ≈ 400 à 900 USD selon $\bar c$ |
| E4 | ≈ 2 crans × 4 axes × 2 graines, soit ≈ 320 USD |
| E5 | Coût d'annotation d'un jeu neuf : **non chiffrable depuis les faits** |

Tous ces montants sont illustratifs.

**Décision pour l'arbitre — trois voies, sans « la » réponse :**
1. **δ = 0,15 sur l'indice poolé, régime P.** C'est la seule combinaison qui atteint au moins 0,8 de puissance même dans le cas favorable, mais elle ignore des gains réels de 0,05 à 0,10.
2. **δ = 0,10 en régime C, avec une affirmation explicitement restreinte aux 60 items.** Elle est puissante si E1 et E2 sont favorables. Elle ne dit rien de la généralisation sans E5.
3. **δ = 0,05.** Elle n'est atteignable sur 60 items dans aucun régime réaliste. Il faut d'abord plus d'items.

**Ce qui départage ces voies :** les résultats d'E1 et E2, qui coûtent environ 200 USD (illustratif), et la décision de l'arbitre sur a3 et a12.

---

## Références (toutes « à vérifier » avant citation)

- McNemar, Q. (1947). *Note on the sampling error of the difference between correlated proportions or percentages.* Psychometrika. — à vérifier
- Dietterich, T. G. (1998). *Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms.* Neural Computation. — à vérifier
- Demšar, J. (2006). *Statistical Comparisons of Classifiers over Multiple Data Sets.* JMLR. — à vérifier
- Brodersen, K. H., Ong, C. S., Stephan, K. E., Buhmann, J. M. (2010). *The balanced accuracy and its posterior distribution.* ICPR. — à vérifier
- Benavoli, A., Corani, G., Demšar, J., Zaffalon, M. (2017). *Time for a Change: a Tutorial for Comparing Multiple Classifiers Through Bayesian Analysis.* JMLR. — à vérifier
- Dror, R., Baumer, G., Shlomov, S., Reichart, R. (2018). *The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing.* ACL. — à vérifier
- Card, D., Henderson, P., Khandelwal, U., Jia, R., Mahowald, K., Jurafsky, D. (2020). *With Little Power Comes Great Responsibility.* EMNLP. — à vérifier
- Bouthillier, X., et al. (2021). *Accounting for Variance in Machine Learning Benchmarks.* MLSys. — à vérifier
- Lan, K. K. G., DeMets, D. L. (1983). *Discrete sequential boundaries for clinical trials.* Biometrika. — à vérifier
- Angrist, J. D., Imbens, G. W., Rubin, D. B. (1996). *Identification of Causal Effects Using Instrumental Variables.* JASA. — à vérifier
- Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., Roth, A. (2015). *The reusable holdout: Preserving validity in adaptive data analysis.* Science. — à vérifier
- Li, L., Jamieson, K., DeSalvo, G., Rostamizadeh, A., Talwalkar, A. (2018). *Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization.* JMLR. — à vérifier
- Badanidiyuru, A., Kleinberg, R., Slivkins, A. (2013). *Bandits with Knapsacks.* FOCS. — à vérifier
- Optimisation bayésienne multi-fidélité, travaux de Kandasamy et coll. — référence à vérifier (titre et année non garantis de mémoire)
- Évaluation de modèles de langue avec barres d'erreur (Miller, 2024 ?) — référence à vérifier

FIN-DE-CELLULE