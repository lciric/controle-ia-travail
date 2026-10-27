# Proposition B — Tour III.3 : riposte

**Pièces.** Les pièces suivantes sont présentes et non coupées : FAITS, la question de l'arbitre, ma conception III.1, l'attaque de A et l'attaque de C. La conception de A est citée par C mais ne m'est pas transmise. Je n'en ai pas besoin : je ne réponds qu'aux sections qui visent B.

**B1.** Je réutilise trois arguments que A et C se sont opposés l'un à l'autre, parce qu'ils frappent aussi mes amendements. Je le signale à chaque fois. Toutes mes dérivations restent des **HYPOTHÈSES** (dérivations de B, non auditées), sauf mention contraire.

---

## (a) Sort des attaques

### Attaques de A contre B

| # | Attaque | Sort | Raison, ou test qui la remplace |
|---|---|---|---|
| B-1 | Le test t apparié est anticonservateur sous asymétrie à gauche. E3 confond le prix de Ville et le prix de l'exactitude. | **Acceptée, et transformée en test (E0, E3′)** | A a raison, et l'erreur est plus profonde que ce qu'il dit. Lire le pari une seule fois au temps n avec le seuil 1/α (Markov) n'est jamais plus puissant que le lire en continu avec le même seuil (Ville). Un test à effectif fixe ne gagne donc de la puissance qu'en sortant de la borne de Markov, c'est-à-dire en utilisant une autre statistique : t, bootstrap, ou borne exacte pour variable bornée. Je retire la formule « le prix de la validité à tout instant ne se justifie pas ». Elle était fausse telle quelle. La question devient : existe-t-il une procédure à effectif fixe **valide sous nul borné asymétrique** et plus puissante que le pari ? |
| B-2 | Le prix du mélange est cohérent : log 8 = log 4 + log 2. | **Acceptée** | Je relis S comme A : trois comparaisons différentes, chacune avec sa valeur. **Je retire a8.** |
| B-3 | J'ai dimensionné 10 points d'écart avec la puissance du *mélange* (0,945), un instrument que je supprime. | **Acceptée** | S-sortie ne donne pas les parts seules à 10 points. Le chiffre « environ 100 tâches par mode » est donc retiré. Il sera remplacé par la sortie de E3′, qui fera tourner la forme parts seule à 0,05, 0,10 et 0,20. À 20 points, les parts seules valent 0,715 contre 0,91 pour le mélange à 30 tâches (RAPPORTÉ). Le besoin à 10 points est donc probablement **au-dessus** de 100 tâches (illustratif). |
| B-4 | Ma règle de porte, qui exige une borne basse > 0 sur le mode tenu à l'écart, contredit N-054. | **Acceptée** | Le point 4 de N-054 (RAPPORTÉ) dit qu'un échec hors du mode « coût » **restreint la revendication de H1**. Il ne fait pas échouer G1. Le mode tenu à l'écart sert à séparer les bras génériques des bras spécialisés. J'avais fusionné « G1 passe » et « H1 est revendicable ». Le § 13 et la décision D-c ne sont pas transmis : la règle de passage par strate n'est pas fixée par les faits. Elle revient à Lazar, sous forme d'options (ligne 6 du plan corrigé). |
| B-5 | L'intersection-union ne protège pas d'une famille de bases pauvre. | **Acceptée comme limite, transformée en contrôle rapporté** | C'est vrai pour toute règle, celle de S comprise. J'ajoute le contrôle 5 de A : la meilleure base doit battre le plancher « juge en une passe » sur la partie de développement. Comme N-008 classe les planchers « rapportés, non critères », ce contrôle est **rapporté**. En faire un critère est une décision de Lazar. |
| B-6 | Les tâches honnêtes d'épreuve ne sont pas stratifiées par mode. Un appariement obtenu par construction ne vaut que sous la loi de calibrage. | **Acceptée, test E7** | C'est le trou le plus sérieux de ma conception. A le relève chez B comme chez C. |
| B-7 | Recentrer H2 sur le rappel du séquentiel seul ouvre un confondant de longueur. | **Acceptée, test E8** | C me fait la même attaque (C3, ci-dessous). Mon amendement a10 remplaçait un contraste apparié par une mesure absolue sans contrôle des faux positifs à chaque horizon. Il est corrigé en E8. |
| B-8 | Deux verdicts (effectif fixe et pari) sur une porte unique. | **Acceptée** | Un seul verdict primaire est gelé avant l'épreuve. Le second est descriptif et ne décide jamais. La parité entre les deux sur les témoins (contrôle 3 de A) est rapportée. |
| B-9 | Clopper-Pearson avec effet de plan n'est pas exact. | **Acceptée** | Je le reclasse en « repère approximatif ». Ce n'est plus une « vérification mécanique à battre ». |

**Scénarios d'évasion de A.** Celui du test t est couvert par E0. Celui de la famille pauvre est traité en B-5. La dérive des honnêtes est testée en E7. La longueur est testée en E8. Pour la **conjonction**, j'accepte et j'ajoute une clause au plan, ligne 10 : « toute déviation d'un choix déclaré est un échec de procédure, pas un réglage ».

### Attaques de C contre B

| # | Attaque | Sort | Raison, ou test |
|---|---|---|---|
| C1-a | L'intersection-union est une « inversion logique » de N-008, qui demande de battre la meilleure base et non chacune. | **Rejetée sur la logique** | Pour des moyennes, E[r_blanc] > max_j E[r_j] équivaut à E[r_blanc] > E[r_j] pour tout j. Le nul de l'intersection-union, l'union des {E[r_blanc − r_j] ≤ 0}, est donc **exactement** « le blanc ne bat pas la meilleure base ». C'est une équivalence logique, pas une restriction. Une base « kamikaze » de rappel moyen 0,15 donne un contraste de moyenne **élevée**. Elle ne bloque pas par sa médiocrité. |
| C1-b | La puissance de l'intersection-union chute avec une base à forte variance entre tâches. | **Acceptée comme risque de puissance, test E4′** | Calcul illustratif sur le monde du contrôle 2 de C : blanc à 0,5 ; base qui alerte 100 % sur 30 % des tâches et 0 % ailleurs. À λ = 0,9 : 0,7·ln 1,45 + 0,3·ln 0,55 ≈ 0,08 nat par tâche, contre environ 0,14 dans le monde de S-sim. La perte de puissance est réelle. C'est le prix de l'affirmation « toutes variantes ». La règle de S, une base unique choisie sur le développement, ne le paie pas, mais elle peut se tromper de base (E4). |
| C1-c | Les seuils des cinq bases sont calibrés sur le même jeu, d'où des erreurs corrélées. | **Acceptée, intégrée à E2′** | Même mécanisme que ci-dessous. |
| C2 | Le bootstrap de tâches est anticonservateur sous asymétrie à gauche à petit n. | **Acceptée, avec une correction du mécanisme, test E0** | Le calcul de C porte sur les répliques bootstrap *d'un* échantillon. Le bon calcul porte sur l'échantillon d'origine. Avec 2 tâches catastrophiques sur 25 dans la population, la probabilité qu'un banc de 25 tâches n'en contienne aucune est 0,92²⁵ ≈ 0,12 (illustratif). Dans ce cas, la borne basse bootstrap est > 0, alors que E[v] < 0. Le niveau réel est donc **au moins de l'ordre de 0,12**. La conclusion de C tient. Sur ce même banc sans catastrophe, le pari parts vaut au plus 1,072²⁵ ≈ 5,7 < 20 (illustratif) : il ne promeut pas. |
| C3 | Les seuils randomisés cassent la reproductibilité. | **Rejetée en partie** | Un seuil randomisé par une graine scellée dans l'engagement est rejouable à l'identique. L'ordre secret du noyau est construit de la même façon. **Acceptée en partie** : le coût en variance est réel, et P § 10 recommande un « score continu par probabilité du jeton de verdict quand c'est possible » (RAPPORTÉ, piste C). Je retiens donc le score continu en premier choix, et la randomisation scellée seulement en repli, déclaré par cellule. |
| C4-a | La règle « porte suspendue si l'écart dépasse τ » est un conditionnement post-gel qui casse le niveau. | **Rejetée sur le niveau** | Une condition supplémentaire déclarée d'avance, qui ne peut que *bloquer*, rend l'événement « passe » plus petit. Sa probabilité sous le nul ne peut pas augmenter. |
| C4-b | Cette règle bloque des courses équitables, et « suspendue » est un état non défini. | **Acceptée, test E6′** | Le taux de blocage à tort dépend de l'effet de tâche. Calcul illustratif : environ 0,005 sans effet de tâche, environ 0,2 si l'écart-type de la différence atteint 0,008. Je supprime l'état « suspendu ». Il est remplacé par la **garde bloquante de S, conservée** : elle fait partie de la règle de promotion, avec deux issues seulement. Aucune nouvelle course honnête n'est autorisée (ligne 10). |
| C-évasion H2 | Le rappel du séquentiel « croît » par accumulation de fausses alertes. | **Acceptée, test E8** | Voir B-7. |
| C-contrôle 1 | Bootstrap sous asymétrie gauche (90 % à +0,1, 10 % à −0,9). | **Acceptée, intégrée à E0** | |

### Arguments échangés entre A et C que je retourne contre moi (B1)

1. **L'appariement par construction n'est que marginal.** A l'oppose à C (C-5), et C à A (point a.1). Avec un seul calibrage, l'écart réalisé F_A(τ̂_A) − F_B(τ̂_B) est une variable figée, de l'ordre de τ (illustratif). Mon amendement (i), « remplacer la garde par un appariement par construction », est donc **retiré**. Conditionnellement aux seuils scellés, les tâches d'épreuve restent i.i.d. Le pari et la garde testent alors les nuls *conditionnels*, et la garde mesure précisément cette asymétrie réalisée. Elle redevient **bloquante**, comme dans S. Mon objection sur δ = 0,10 demeure (voir (c)).
2. **Les contrastes de tendance ne prouvent pas la monotonie.** A l'oppose à C (C-8), C à A (K = 3, poids central nul). Mon amendement « au moins trois niveaux, poids de tendance » tombe sous le même argument. Il est corrigé en E9.
3. **La strate « tous modes » peut être portée par un seul mode.** C l'oppose à A (point a.4, e-BH). Ma ligne 5 avait la même faiblesse. Elle est corrigée à la ligne 6 du plan.

---

## (b) Expériences corrigées

Toutes tournent sur processeur, avec 1 000 répétitions, une graine neuve tirée au scellement et la borne de Wilson à 95 %. Les lectures sont gelées avant le lancement. Les seuils numériques non tirés des faits sont **illustratifs**.

### E0 — Banc des nuls asymétriques (remplace E1 et la partie « niveau » de E3)

- **Procédures jugées** : le mélange parts + signe de S ; la forme parts seule ; le test t apparié ; le bootstrap de tâches (percentile) ; une borne exacte pour variable bornée à effectif fixe, Hoeffding ou Bentkus (Hoeffding, « Probability inequalities for sums of bounded random variables », 1963 ; Bentkus, « On Hoeffding's inequalities », 2004 : références à vérifier).
- **Mondes**, tous avec E[v] = 0 :
  - **M1**, asymétrie à droite (mon monde d'E1) : +0,1 avec probabilité 0,8, −0,4 avec probabilité 0,2 ;
  - **M2**, asymétrie à gauche (C) : +0,1 avec probabilité 0,9, −0,9 avec probabilité 0,1 ;
  - **M3** (A) : support {−1 ; +0,1}, avec P(+0,1) = 10/11.
  - Chaque monde est réalisé au niveau des tâches, puis par parts sur dix épisodes, pour n ∈ {20 ; 25 ; 30 ; 40 ; 60}.
- **H_A** (S, et défense du test t) : toutes les procédures restent ≤ α dans tous les mondes.
- **H_B** (B, A et C) : le mélange dépasse α en M1 ; le test t et le bootstrap dépassent α en M2 ou M3 ; la forme parts et la borne exacte restent ≤ α partout.
- **Contrôles** :
  - négatif : v ≡ 0 et nul symétrique, toutes les procédures ≤ α ;
  - positif : E[v] = +0,1, puissance rapportée.
- **Falsification** :
  - le mélange ≤ α en M1 falsifie a1 (la critique de B et de C) ;
  - le mélange > α falsifie la validité revendiquée en S § 2.2 et § 3.1 ;
  - t et bootstrap ≤ α en M2 et M3 falsifient B-1 et C2 ;
  - t ou bootstrap > α les exclut de toute analyse primaire ;
  - la forme parts > α falsifie la dérivation de S § 3.1. Un tel résultat signerait d'abord une erreur de code, puisque le contrôle négatif doit tenir.

### E2′ — Calibrage unique, ex æquo, seuils de plusieurs bases

- **Monde** :
  - même loi latente pour A et B ;
  - A continu, B ordinal sur 11 niveaux ;
  - **un seul** calibrage par répétition (70 tâches de dix épisodes, avec effet de tâche) ;
  - variante C1-c : cinq bases calibrées sur le même jeu ;
  - épreuve : 40 tâches sabotées et 70 honnêtes.
- **H_A** : la promotion de « A meilleur » avec garde bloquante reste ≤ α, que B soit déterminé par quantile ou randomisé par graine scellée.
- **H_B** : sous quantile déterministe, la promotion dépasse α, et la garde à δ = 0,10 ne la bloque pas.
- **Contrôle négatif** : B continu, promotion ≤ α. Sinon, c'est la construction de base qui est fautive.
- **Falsification** :
  - H_A tenue avec quantile déterministe falsifie ma crainte : la règle de S suffit ;
  - H_B tenue falsifie la traduction « même taux nominal plus garde δ » pour les cellules ordinales.

### E3′ — Puissance des procédures valides à effectif fixe contre le pari continu

- **Admises** : seules les procédures restées ≤ α dans E0. Les procédures exclues par E0 ne concourent pas.
- **Monde** : celui de S-sim ; écarts 0,05, 0,10 et 0,20 ; dix et trois épisodes par tâche ; effets de tâche **propres à chaque moniteur** (a5, non attaqué) ; n ∈ {20 ; 30 ; 40 ; 60 ; 100 ; 150}.
- **H_A** : une procédure admise à effectif fixe dépasse la forme parts continue d'au moins 0,10 de puissance à n = 30 ou 40.
- **H_B** : aucune ne la dépasse de plus de 0,05.
- **Falsification** :
  - H_A tenue falsifie mon recul en B-1 : un test fixe valide gagne, et il devient le primaire de G1 ;
  - H_B tenue falsifie la troisième thèse de ma conception : le pari parts devient le primaire de G1.
  - Entre 0,05 et 0,10, la règle déclarée choisit le pari (règle de simplicité, gelée d'avance). Les deux bornes sont donc liées, sans zone sans issue (B4, critique de A contre C reprise ici).
- **Sortie annexe** : la table de dimensionnement de la forme retenue, qui remplace B-3.

### E4′ — Choix du comparateur : sélection sur le développement contre intersection-union

- **Monde F** (« vainqueur bruyant », scénario de C contre A, repris ici en le disant) : une base forte à 0,60 de faible variance ; trois bases à 0,45 dont le rappel par tâche varie de ±0,40 ; un blanc à 0,55, donc sous le nul ; 10 tâches de développement, 60 d'épreuve.
- **Monde P** (contrôle 2 de C) : quatre bases à 0,40 ; une cinquième à moyenne 0,30, qui alerte 100 % sur 30 % des tâches ; un blanc à 0,55.
- **H_A** (S) : la sélection sur le développement suivie d'un pari reste ≤ α en F.
- **H_B** (B) : la sélection dépasse α en F ; l'intersection-union reste ≤ α en F, et sa perte de puissance en P reste ≤ 0,25 à 40 tâches.
- **Falsification** :
  - la sélection ≤ α en F falsifie E4 ;
  - l'intersection-union qui perd plus de 0,25 en P falsifie mon choix de l'intersection-union pour G1, au profit d'une sélection sur un développement agrandi, dont la taille reste à fixer.

### E5 — Unité « tâche » contre « organisme »

E5 est inchangée, non attaquée sur le fond. Elle est faite sur T0.5 si les identifiants de groupe y figurent (HYPOTHÈSE), sinon elle attend la couche 2. A relève qu'elle ne mesure pas la corrélation sur le **rappel**. C'est juste. Je ne reconstruis pas l'expérience de C qu'il cite, car elle ne m'est pas transmise. L'équivalent pour le rappel est ajouté pour la couche 2 : un test de permutation des étiquettes d'organisme sur les contrastes v(t), avec les mêmes H_A et H_B.

### E6′ — La garde avec effet de tâche, et son taux de blocage à tort

- **Monde** : 70, 150 et 300 tâches honnêtes ; taux vrai de 1 % pour A et B ; effet de tâche d'écart-type 0, 0,5 et 1 en logit, propre ou commun aux deux moniteurs.
- **H_A** (S § 2.4) : δ = 0,10 est certifiable à 70 tâches et δ = 0,05 à 150, dans au moins 95 % des répétitions, quel que soit l'effet de tâche.
- **H_B** : avec un effet de tâche de 1, il faut au moins 1,5 fois plus de tâches.
- **Mesure annexe** (C4-b) : la part de courses équitables bloquées par la garde.
- **Contrôle** : sans effet de tâche, on doit reproduire S-sortie (1,0 à 70 tâches et δ = 0,10, RAPPORTÉ).
- **Falsification** : soit le dimensionnement de S, soit mon point a4.

### E7 — Dérive des honnêtes par mode (B-6)

- **Monde** : calibrage tiré d'une composition de consignes ; épreuve honnête stratifiée par mode, avec un déplacement de la marginale honnête de 0, τ/2 ou τ sur une strate. Seul le blanc est sensible au déplacement.
- **H_A** : la garde bloquante, calculée **par strate**, maintient la fausse promotion ≤ α.
- **H_B** : une garde poolée laisse passer au-delà de α une dérive de τ/2 confinée à une strate.
- **Falsification** :
  - H_B tenue impose une garde et un calibrage par strate (ligne 2 du plan) ;
  - H_A tenue falsifie B-6 sur ce monde.

### E8 — H2 sans artefact de longueur (B-7 et C3)

- **Monde nul** : aucun signal de sabotage ; scores par action autocorrélés à 0,3 (forme de T0.3, citée dans N-007) ; trois horizons ; honnêtes de calibrage soit de longueur unique, soit appariés en longueur par horizon.
- **Instrument corrigé** :
  - seuil du séquentiel calibré **par horizon** sur des épisodes honnêtes de même longueur ;
  - contraste u_k(t) = r_seq(k) − r_seq(k−1) ;
  - garde sur f_seq(k) − f_seq(k−1) ;
  - promotion de « croît » par intersection-union sur les accroissements successifs.
- **H_A** : l'instrument corrigé reste ≤ α ; l'instrument « rappel seul sans calibrage par horizon » (mon a10 d'origine) aussi.
- **H_B** : l'instrument a10 dépasse α ; l'instrument corrigé reste ≤ α.
- **Contrôle de C** (séquentiel plat, comparateur qui décroît) : l'instrument corrigé ne doit pas promouvoir, alors que l'écart de S, H2b, promeut.
- **Falsification** :
  - H_B tenue retire a10 au profit de l'instrument corrigé ;
  - H_A tenue falsifie B-7 et C3 sur ce monde.

### E9 — Pentes non monotones (H3b, H2b)

- **Profils** : écart blanc − noir en N ∈ {1 ; 2 ; 4 ; 8} de (0 ; −0,3 ; −0,3 ; +0,3) (A) et (0,2 ; −0,3 ; 0,4) (C).
- **H_A** : le contraste linéaire de tendance promeut « décroît plus doucement » au-delà de α.
- **H_B** : l'intersection-union sur les accroissements successifs, accompagnée de H3a par N sous e-BH, ne promeut pas.
- **Falsification** :
  - H_A tenue retire le contraste linéaire comme preuve de monotonie ; il reste rapporté comme « tendance moyenne » ;
  - si le contraste linéaire ne promeut pas, l'exemple de A et de C est faux sur ce monde.
- **Coût** : la puissance de l'intersection-union sur les accroissements est rapportée. Le facteur ½ par accroissement la divise ; S ne dimensionne aucune pente.

### Plan d'analyse de G1, corrigé (dix lignes à geler)

1. **Unité** : la tâche, ou l'organisme si E5 le demande. Partitions calibrage / développement / épreuve tirées par unité, avec empreintes.
2. **Seuils** : score continu en premier choix (P § 10), randomisation par graine scellée en repli ; calibrage par strate si E7 donne H_B ; τ = 1 % (N-008). Le point 5 % est rapporté, sauf décision contraire de Lazar.
3. **Comparateur** : intersection-union contre toutes les bases de N-008, sauf si E4′ la falsifie.
4. **Primaire unique** : la procédure désignée par E0 puis E3′, avant toute donnée d'épreuve. La borne basse unilatérale à 95 % est déclarée comme telle (critique de A contre C, C-11, reprise ici).
5. **Garde bloquante** sur f_blanc − f_comparateur, par strate, avec δ déclaré. Pas d'état « suspendu ».
6. **Strates et règle de porte** : par mode, plus une strate « tous modes » rapportée avec sa décomposition. La règle de passage (conjonctive, disjonctive, ou « tous modes » seul) est **une décision de Lazar**, les faits ne la fixant pas. La restriction de H1 se fait selon N-054, point 4, tel quel.
7. **Multiplicité** : aucune correction si la règle est conjonctive (intersection-union entre modes) ; e-BH ou Bonferroni si elle est disjonctive.
8. **Taille** : fixée par E3′ et E6′. Aucun arrêt optionnel si le primaire est à effectif fixe.
9. **Secondaire** : le pari parts, pour le pôle, descriptif, ne décide jamais. Les témoins vrais et faux sont jugés par strate.
10. **Échec et intégrité** : en cas d'échec, la conséquence prévue au § 10 de P s'applique. Aucun nouveau tirage, aucune modification après le gel ; toute déviation est un échec de procédure. Verdict par un sous-agent neuf (R13).

---

## (c) Réponse à l'arbitre — une page

**Ce qui est établi.** Rien n'est établi expérimentalement par ce tour : aucune expérience n'a tourné.

Ce qui suit relève du raisonnement. Les arguments y sont concordants, mais non audités.

- **La forme parts seule** est une surmartingale sous E[v] ≤ 0, si les tâches sont i.i.d. conditionnellement aux seuils scellés.
- **La garde** est valide par union des nuls (S § 3.5).
- **Le minimum de deux e-valeurs** est une e-valeur sous l'union de leurs nuls.
- **Le mélange avec le signe** ne teste que l'intersection {E[v] ≤ 0, E[s] ≤ 0}. B et C l'ont dérivé indépendamment, A le reprend : c'est une HYPOTHÈSE, que E0 rend réfutable.
- **Une lecture unique à seuil 1/α** n'est jamais plus puissante que la lecture continue. Je corrige ma thèse 3 sur ce point.
- **L'intersection-union sur les moyennes** est logiquement équivalente à « bat la meilleure base ».

**Ce qui n'est pas établi.**

- La validité du mélange de S (E0).
- La validité du test t et du bootstrap de tâches sous asymétrie : A et C prédisent l'échec, je l'accepte comme prédiction.
- L'existence d'une procédure à effectif fixe valide et plus puissante que le pari (E3′). La table de dimensionnement de S, faite avec le mélange, ne vaut que si E0 sauve le mélange.
- L'appariement des taux de faux positifs sur des cellules ordinales et sous dérive par mode (E2′, E7).
- La taille de banc. La garde à δ = 0,10 autorise un taux réalisé jusqu'à 11 % face à 1 % : je maintiens que ce n'est pas « à 1 % de faux positifs ». Cela ne se corrige pas par construction (arguments croisés de A et C), seulement par des données, ou par une décision de Lazar sur le point de fonctionnement.
- Le dimensionnement par mode avec effets de tâche propres à chaque moniteur.
- La forme de H2 et des pentes (E8, E9).

**L'expérience à faire en premier : E0.**

- Une seule simulation, sans dépense, quelques minutes (illustratif).
- Elle couvre cinq procédures et trois mondes nuls asymétriques.
- Chaque issue falsifie une affirmation nommée : la validité du mélange de S, ou ma critique a1 ; la défense des tests t et bootstrap, ou les critiques B-1 et C2.
- Elle conditionne tout le reste. E3′ n'admet que les procédures qu'E0 laisse passer, le primaire de G1 en découle, et le dimensionnement de la couche 2 dépend de la forme retenue.

**Ce qui me ferait changer d'avis.**

- Si le mélange tient en M1, je retire a1.
- Si le test t tient en M2 et M3, je retire mon recul en B-1.
- Si E3′ donne H_B, le pari parts devient le primaire de G1 et ma thèse 3 tombe entièrement.

FIN-DE-CELLULE