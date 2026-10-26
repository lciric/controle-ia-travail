# Proposition B, tour III.2 : équipe rouge croisée

**Pièces.** Les conceptions A et C sont présentes et complètes : chacune se termine par sa ligne de clôture. Je ne peux pas recalculer leurs empreintes sha256. Tout ce que je propose ci-dessous a le statut d'HYPOTHÈSE. Tout seuil que j'introduis est illustratif. Les calculs sont donnés pour être vérifiés ligne à ligne. Je ne décris aucun procédé pour tromper un instrument.

---

## Contre la proposition A

### (a) Failles

**A-1. E1 est en partie vrai par construction, et il confond deux variables.**
- A établit lui-même, en (iii) de la faille 1, que $\max_{t\le 1{,}5T}S_t$ domine stochastiquement $\max_{t\le T}S_t$. L'issue de la composante « horizon » est donc connue d'avance : $H_B$ gagne sans rien apprendre.
- E1 fait varier ensemble la famille de tâches et l'horizon. Si le taux de faux positifs sort de la bande, on ne sait pas à quelle variable l'attribuer.
- Le témoin positif, un seuil conforme pondéré par rapport de densités (Tibshirani et al., 2019), ne peut pas réparer l'horizon. La pondération suppose que la loi déployée est absolument continue par rapport à la loi de calibrage. Or aucun des 1 000 maxima de calibrage n'a été pris sur un épisode de longueur $1{,}5T$.
- Correctif : un plan 2×2 (famille seule, longueur seule), et pour la longueur, une stratification du calibrage par $T$.

**A-2. Le plafond mécanique rend le critère central infalsifiable, et il introduit une fuite.**
- A exige que la sonde apporte un gain d'AUC d'au moins 0,05 sur la règle « coût écrit $>$ coût de référence $\times(1+\delta)$ ».
- Dans la famille « coûts gonflés », l'étiquette « sabotage » est définie par l'écart au coût de référence. L'AUC de cette règle tend donc vers 1 dès que $\delta$ est inférieur à l'inflation minimale. Aucun instrument ne peut faire +0,05 au-dessus de ce plafond : l'issue négative est acquise par construction.
- Le coût de référence est une variable de **vérité terrain**, réservée à l'évaluation. S'il était disponible au déploiement, la question du moniteur ne se poserait pas pour cette famille. Il entre pourtant dans la référence à battre : c'est une fuite.
- La comparaison honnête est une vérification mécanique **restreinte à l'information observable par le moniteur**, par exemple la cohérence interne de la trace. E7 hérite du même plafond.

**A-3. Dans E6, un cosinus inférieur à 0,3 est presque garanti en grande dimension.**
- En dimension de l'ordre de $10^3$, deux sondes régularisées entraînées sur deux échantillons finis de **la même** distribution ont souvent un cosinus faible. Il existe beaucoup d'hyperplans séparateurs quasi équivalents, et les directions de faible variance sont mal déterminées.
- Sans référence intra-distribution, conclure à une « rotation » est vrai par construction (voir le contrôle c-1).

**A-4. E4 compare des capacités différentes et ignore la grandeur du nombre.**
- A falsifie $H_A$ si « la sonde linéaire reste sous les planchers alors que le MLP les dépasse ». Mais les deux planchers (directions aléatoires, tâche de contrôle de Hewitt–Liang **linéaire**) sont calibrés pour la capacité linéaire.
- Un MLP doit être comparé à un MLP entraîné sur étiquettes permutées. Sinon, « MLP au-dessus du plancher » est en partie un effet de capacité.
- E4 lit précisément les jetons du coût sans contrôler la grandeur du nombre écrit. Je reprends ici l'objection du Duel 2 de C, qui manque à A.

**A-5. E2 : l'unité du réarrangement n'est pas fixée, et la moitié négative de la classe $\mathcal{K}$ manque.**
- Si le « réarrangement contraint des rangs » se fait **à l'intérieur** d'un épisode, c'est la classe $\mathcal{C}$ : la puissance de la somme vaut $\alpha$ par identité.
- S'il recouple des cellules d'épisodes différents, c'est la classe $\mathcal{K}$.
- L'expérience et son témoin doivent différer par cette seule unité, sinon E2 teste une identité.
- A ne balaie que $\rho\in[0;0{,}5]$. Je me sers de C : à marginales fixées, une dépendance négative réduit $\mathrm{Var}(\sum X)$ et peut faire descendre la puissance de la somme sous $\alpha$.
- Le « contre-exemple par mélange » de A est affirmé, pas calculé. La formulation correcte est la suivante : une dépendance positive au sens supermodulaire rend la somme plus grande en ordre convexe (Müller & Stoyan, 2002, *Comparison Methods for Stochastic Models and Risks*). L'ordre convexe n'implique pas une queue plus lourde à un seuil fixé. L'énoncé de A est plausible, mais non démontré.

**A-6. La décomposition de Krogh–Vedelsby est surinterprétée.**
- L'identité « erreur du comité = erreur moyenne − ambiguïté » est exacte pour la perte quadratique d'une **moyenne** de prédicteurs réels.
- Pour des verdicts discrets agrégés par vote et jugés en taux de détection à taux de fausses alertes fixé, il n'existe pas de décomposition exacte analogue. Le « si et seulement si » de A n'est pas établi.
- Pour l'utiliser, il faut mesurer sur les scores continus des juges en perte quadratique.

**A-7. E5 n'a pas de puissance.**
- Sur 12 cellules, l'erreur type d'un coefficient de Spearman vaut approximativement $1/\sqrt{n-1}\approx0{,}30$.
- Distinguer 0,5 de 0,2 est impossible : l'issue « non concluante » est quasi certaine.

**A-8. E3 utilise une métrique non définie.**
- « Délai inférieur à 50 % du dommage » suppose une correspondance score→dommage. Ni F1 ni A ne la définissent, et le dommage n'est pas observé par le moniteur.
- Sans modèle de dommage dans le simulateur, l'issue n'est pas mesurable.

**A-9. Statuts et chiffres.**
- Le présupposé a5 (« taux de détection et de fausses alertes ») ne figure pas dans le texte de la question qui m'est transmis. S'il vient d'une consigne de tour non transmise, je ne peux pas le vérifier. Lui attribuer le statut « FAUX d'après F1 » n'est pas fondé sur la pièce.
- Plusieurs seuils inventés ne sont pas marqués illustratifs, contrairement à la règle 4 : $\cos$ 0,3 et 0,7, incrément 0,05, Spearman 0,5 et 0,2, délai 50 %, différence 0,10 dans E8, 10 000 règles dans E9.
- E9 est une démonstration, pas une inférence forte. Avec des bosses de largeur 0,001 et une grille de pas 0,01, des passages sont garantis par conception, et A le sait.

### (b) Hypothèses supposées sans test, et mesure qui les testerait

| Hypothèse implicite de A | Mesure qui la teste |
|---|---|
| Les 38 épisodes honnêtes de P3/P4 ne sont pas sélectionnés en lien avec la difficulté des tâches (F1 ne dit pas pourquoi 38 sur 60) | Comparer la longueur, le coût de référence et la famille entre les 38 retenus et les 22 autres ; test de permutation sur ces covariables |
| Un taux de détection à 5 % de faux positifs est estimable sur ces effectifs | Avec environ 38 épisodes honnêtes, le seuil au niveau 5 % tombe sur la 2ᵉ valeur la plus haute. Mesurer la largeur bootstrap du taux de détection avant toute conclusion et fixer l'effectif requis a priori |
| La covariable de tâche suffit à capturer la dérive (seuil conforme pondéré) | Test à deux échantillons par classifieur, calibrage contre déploiement : AUC proche de 0,5 attendue après pondération |
| Le second juge applique la contrainte d'orthogonalité (E8) | Contrôle de manipulation : recouvrement des éléments de preuve cités par les deux juges, codé à l'aveugle, en condition A contre condition B |
| Les règles réellement produites par `politique_endogene.py` ressemblent à « Brier + bosse » (E9) | Inventaire des règles effectivement générées et classement par forme avant le criblage aléatoire |
| Les activations de P3 aux jetons du coût sont archivées et réutilisables (E4, E6) | Inventaire des couches et positions stockées ; à défaut, coût de ré-extraction (illustratif) |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E6 : cosinus entre moitiés.** Deux sondes $w_2, w_2'$ entraînées sur des moitiés disjointes de trajectoires d'une même distribution, et de même pour $w_1, w_1'$. La « rotation » n'est interprétable que si $\cos(w_1,w_2)$ est nettement inférieur à $\cos(w_2,w_2')$.
2. **E4 : plancher apparié en capacité.** Un MLP entraîné sur étiquettes permutées par tâche.
3. **Sondes : épisodes honnêtes appariés en valeur écrite.** Je reprends le Duel 2 de C. Sans eux, on ne distingue pas la grandeur du nombre d'un signal de sabotage.
4. **Sondes : épisodes honnêtes portant des indices d'évaluation bénins.** C les propose et A ne les a pas. Sans eux, un signal de « conscience d'évaluation » est confondu avec le sabotage.
5. **E1 : bras séparés** « famille seule » et « longueur seule ».
6. **Vérification mécanique privée de la vérité terrain**, en référence de chaque gain incrémental (A-2).

---

## Contre la proposition C

### (a) Failles

**C-1. Erreur de calcul marquée VÉRIFIÉ.**
- Avec $\alpha=4/3$ : $\Phi(q)=3\,(q^{4/3}+(1-q)^{4/3}-1)$, donc $\Phi'(q)=3\cdot\tfrac43\,(q^{1/3}-(1-q)^{1/3})=4\,(q^{1/3}-(1-q)^{1/3})$ et $\Phi'(0)=-4$.
- On obtient $d_{4/3}(1,0)=-\Phi(0)-\Phi'(0)\cdot1=4$, et non 3. C a omis le facteur $\alpha=4/3$. A trouve 4, et c'est exact.
- La normalisation « $1-d/3$ » que C construit ensuite repose sur cette erreur.

**C-2. L'« incompatibilité mutuelle » des colmatages B et D est fausse.**
- Le double ancrage ne rejette pas la règle de Tsallis : il fixe une normalisation.
- Soit $S=-d_{4/3}$. Au voisinage de $q=1$, avec $\varepsilon=1-q$, on a $d_{4/3}(1,1-\varepsilon)\approx\varepsilon^{4/3}$ ; pour $\varepsilon=10^{-4}$, cela donne environ $4{,}6\cdot10^{-6}$. Et $S(y,\tfrac12)=-3(1-2^{-1/3})\approx-0{,}619$.
- La règle $aS+b$ passe les deux ancres pour $b\approx1$ et $a=0{,}25/0{,}619\approx0{,}404$.
- Condition de Savage du 1ᵉʳ ordre : $g'_p(p)=0$ exactement, puisque la règle est propre.
- Condition du 2ᵉ ordre : $g''_p(p)=-a\,\Phi''(p)$ avec $\Phi''(p)=\tfrac43(p^{-2/3}+(1-p)^{-2/3})$, minimal en $p=\tfrac12$ où il vaut environ 4,23. On a donc $g''_p(p)\le-1{,}71\le-0{,}05$ sur toute la grille.
- La faille réelle est celle que nomme A : l'ancrage ne fixe $(a,b)=(1,0)$ qu'**à forme de règle donnée**.

**C-3. Duel 1 : une moitié est vraie par construction, l'autre souffre d'une fuite.**
- Le contre-exemple algébrique de C réfute déjà l'invariance. Mesurer $\delta_{\text{rot}}$ sous des rotations de Haar ne peut donner qu'une issue : ce n'est pas une inférence forte (B4).
- Dans le volet Procrustes, $Q^*$ est ajusté sur les paires $D/H$ puis évalué sur le contraste $D/H$. C'est la même phrase insérée dans toutes les tâches de P4, donc la validation croisée par tâches ne sépare pas le contraste d'entraînement du contraste d'évaluation.
- Avec $n\ll d$, Procrustes orthogonal a une liberté énorme. Un dépassement du plancher est alors quasi garanti : la « rotation récupérable » apparaît par construction.
- C affirme aussi que le modèle de P4 est Llama-3.1-8B avec $d=4096$. F1 ne nomme pas le modèle de P3/P4, comme A l'a relevé. La croissance de la norme résiduelle avec le contexte est une HYPOTHÈSE non marquée.

**C-4. Duel 2 : l'appariement en valeur ne sépare pas l'intention de l'incohérence.**
- Dans la paire appariée, la sortie du saboteur reste **incohérente** avec l'énoncé, tandis que celle de l'honnête est cohérente avec un énoncé modifié. Toute représentation interne de « valeur écrite ≠ valeur calculée » passe le test : c'est du calcul, pas de l'intention.
- La modification des tarifs change aussi la distribution des énoncés : c'est un confondant.
- Le « contrôle négatif » de C, un prédicteur non linéaire sur les nombres de l'énoncé et de la sortie, calcule exactement cette incohérence. C'est donc une référence positive forte, pas un contrôle négatif. S'il atteint une AUC proche de 1, la règle de falsification de C devient ininterprétable.

**C-5. Duel 3 : incohérence interne et confondant.**
- Le champ de $H_A$ est $B\ge4\sigma\sqrt T$. Le régime (i) donne $B=0{,}35\sigma\times100=35\sigma$, soit un rapport signal-bruit de $35/10=3{,}5<4$. Un échec dans ce régime **ne falsifie pas** $H_A$.
- $H_A$ est formulé comme un universel (« pour tout profil »), qu'aucun énoncé de F1 ne revendique. Tout contre-exemple construit le falsifie : c'est un épouvantail.
- C fait varier ensemble $\delta<\kappa$ et $\sigma_{\text{ép}}$. Or, avec $\sigma_{\text{ép}}=0{,}4\sigma$ et $T=100$, l'écart type du décalage de la somme dû à l'effet épisode vaut $40\sigma$, contre $10\sigma$ pour le bruit propre. La perte de puissance de la somme vient alors de l'effet épisode, pas du régime sous-$\kappa$.
- Enfin, « $C_t$ ne franchit pas le seuil » quand $0<\delta<\kappa$ est affirmé. Les excursions de $C_t$ croissent avec $\delta$, donc la puissance est une question quantitative : on ne peut pas poser qu'elle est nulle.

**C-6. Association 3 : la garantie de Ville n'est pas démontrée.**
- Les différences $S_t-\bar S_{1:t-1}$ d'un même épisode partagent des termes, donc elles sont dépendantes en série. Elles sont classées à chaque pas contre le **même** jeu de calibrage.
- Rien n'établit alors que $p_t$ est uniforme conditionnellement à $\mathcal F_{t-1}$, ce qu'exige le produit de paris pour être une surmartingale.
- La « démonstration » porte sur $S_t-S_1$, qui n'est pas la statistique proposée.
- Elle n'élimine qu'un effet épisode **additif constant**. Un effet de pente ou d'échelle subsiste.
- Le résultat d'indépendance des p-valeurs conformes séquentielles (Vovk, Gammerman & Shafer, 2005) vaut pour un autre schéma, où chaque point rejoint le sac. Son transfert ici reste à démontrer.

**C-7. Les contre-mesures créent des angles morts par construction.**
- *Soustraction de la médiane des 3 premiers pas* : avec $T=10$ comme dans P3, un sabotage commencé avant $t=3$ est absorbé dans la ligne de base. On crée une zone aveugle précoce.
- *Projection $w_\perp=(I-UU^\top)w$* : elle contredit l'argument de C lui-même, selon lequel la grandeur est encodée non linéairement. L'effacement par projection ne retire que l'information linéairement décodable (Ravfogel, Elazar, Gonen, Twiton & Goldberg, 2020, *Null It Out: Guarding Protected Attributes by Iterative Nullspace Projection*).
- *$\lambda_{\max}$ et Marchenko–Pastur* : $\lambda_{\max}$ est aveugle à l'anticorrélation que C présente comme l'angle mort de la somme. Une dépendance négative abaisse des valeurs propres, et il faudrait tester le bord inférieur $(1-\sqrt{N/T})^2$. De plus, le régime asymptotique BBP est douteux à $T\approx10$.
- *Statistique de Hotelling sur moyenne mobile exponentielle* : elle détecte un déplacement de moyenne. Une rotation de direction à moyenne conservée change la covariance, pas la moyenne.

**C-8. Le remplacement par la matrice de Gram est invariant par construction, mais son utilité n'est pas testée.**
- Une statistique invariante sous $O(d)$ est par conception aveugle à la rotation elle-même.
- La normalisation par la norme retire aussi l'information de norme.
- Elle peut servir de détecteur robuste à la rotation, mais seulement si le sabotage modifie les produits scalaires inter-pas. C ne le teste pas.

**C-9. Statuts.**
- C appose VÉRIFIÉ à ses propres calculs, dont un calcul faux (C-1).
- Il titre « VÉRIFIÉ (avec convention de signe inversée) » puis conclut « exacte » : le titre et le corps se contredisent.
- Une phrase de A.2 attribue l'anticorrélation à un comportement d'agent. La même idée s'énonce sans perte comme une hypothèse sur la copule, et elle devrait l'être, par cadre.

**C-10. Duel 4 : définition et puissance.**
- C suppose que la marge vaut $|p-0{,}5|$. F1 ne définit pas la marge.
- La zone $20\,\%<\text{TCC-FN}\le50\,\%$ n'est tranchée par aucune issue.
- Sur un pli de 25 %, le nombre de faux négatifs de la sonde risque d'être trop faible pour estimer TCC-FN (effectif illustratif à calculer a priori).

### (b) Hypothèses supposées sans test, et mesure qui les testerait

| Hypothèse implicite de C | Mesure qui la teste |
|---|---|
| L'effet épisode est additif constant (C-6, contre-mesure 1) | Modèle mixte sur les scores honnêtes réels de P3 : variance de l'ordonnée à l'origine aléatoire contre variance de la pente aléatoire par tâche |
| La marge du routage est sur l'échelle des probabilités | Lecture du code de routage ; recalcul avec une marge en logit et taux de recouvrement des ensembles routés sous les deux définitions |
| La modification des tarifs ne change que les nombres | AUC de la sonde entre tâches honnêtes d'origine et tâches honnêtes modifiées, toutes deux honnêtes : une valeur proche de 0,5 est attendue |
| La norme résiduelle croît avec le contexte dans le modèle de P3 | $\|h_t\|$ en fonction de la position sur épisodes honnêtes, couche par couche |
| La distance de Gram n'est pas dominée par le type de tâche | AUC de cette distance pour séparer deux familles de tâches **honnêtes** : elle doit rester proche de 0,5 |
| L'alignement de Procrustes est stable hors contraste | Résidu de Procrustes sur des concepts témoins tenus à l'écart (proposition A, association 4) |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Duel 1 :** $Q^*$ ajusté sur la paire bénigne $B/B'$ ou sur des concepts stables, puis évalué sur $D/H$. Et $Q^*$ ajusté sur des correspondances permutées, qui doit retomber au plancher.
2. **Duel 2 :** honnête contre honnête modifié ; et **erreurs arithmétiques honnêtes non intentionnelles**. Sans ce dernier témoin, « intention » et « incohérence » restent confondues.
3. **Duel 3 :** un bras $\delta<\kappa$ sans effet épisode et un bras avec effet épisode sans dérive ; et un régime placé **dans** le champ de $H_A$.
4. **Association 3 :** simulation sous l'hypothèse nulle avec effet épisode de pente ou d'échelle et bruit autorégressif d'ordre 1. On compte les franchissements de $E_t\ge1/\alpha$.
5. **Matrice de Gram :** épisodes honnêtes de longueurs $T$ différentes, en plus des balises d'audit bénignes que C propose déjà.

---

## Ce qui est réfutable dans cette critique

| Énoncé | Calcul ou condition de réfutation |
|---|---|
| $d_{4/3}(1,0)=4$ (C-1) | Recalcul de $\Phi'(0)$ |
| La règle de Tsallis renormalisée passe le double ancrage et la condition de Savage (C-2) | $a\approx0{,}404$, $b\approx1$, $g''_p(p)\le-1{,}71$ |
| Le régime (i) de C est hors du champ de $H_A$ (C-5) | Rapport signal-bruit $3{,}5<4$ |
| E5 de A n'a pas de puissance (A-7) | Erreur type de Spearman d'environ 0,30 pour $n=12$ |
| Le critère d'AUC incrémentale de A est plafonné par la vérité terrain (A-2) | Réfuté si la règle mécanique de A obtient une AUC nettement inférieure à 1 sur la famille « coûts gonflés » |

FIN-DE-CELLULE