# Proposition B — Tour III.2 : équipe rouge croisée contre A et C

**Pièces reçues.** FAITS (S, S-sim, S-sortie, P, N-007/N-008, N-054, C, J1 à J3), question de l'arbitre, conceptions A et C : toutes présentes et non coupées.

**Statuts.** Ce que je cite des faits est RAPPORTÉ. Mes dérivations sont des HYPOTHÈSES. Mes chiffres hors faits sont *illustratifs*. Les dix contrôles de S §5 n'ont aucune sortie : A le signale, C le perd de vue (voir C-1).

**Périmètre des évasions.** L'adversaire traité ici exploite l'instrument : le proposeur du pôle qui rédige des fiches pour être promu, le concepteur d'un bras qui règle son seuil, le lecteur qui touche la banque avant le gel. Les évasions côté organisme (comment un saboteur échappe à une sonde) sortent du périmètre de la question (garde R-519). Je ne les écris pas.

**Constat commun, non fusionné.** A (A1) et C ((b).1) établissent tous deux que le mélange parts + signe n'est pas valide sous E[v] ≤ 0. Je ne le reconteste pas. J'attaque leurs remèdes, qui divergent et réintroduisent chacun le défaut ailleurs.

---

## Contre la proposition A

### (a) Failles

**A-1. E4 étalonne sur le mauvais nul.**
- A démontre en A1 que le signe ne teste pas E[v] ≤ 0.
- Il choisit pourtant comme étalon de puissance de E4 « le test du signe binomial unilatéral » (≈ 0,9 à 20 tâches, *illustratif*).
- Ce test porte sur la médiane. Sa puissance plus élevée vient en partie d'un nul plus faible.
- E4 peut donc conclure « remplacer le pari par le test à n fixé » pour une raison que A a lui-même déclarée invalide.
- Seul l'intervalle par rééchantillonnage des tâches (N-054 point 4, RAPPORTÉ) vise la moyenne. Sa couverture sur 30 à 40 tâches n'est pas exacte. (HYPOTHÈSE)

**A-2. E3 est vrai par construction.**
- Les seuils sont placés au quantile 0,90 et au quantile 0,99 du même score. L'asymétrie vaut donc 9 points, sous δ = 0,10 : la garde passe par définition.
- L'écart de rappel n'est alors que l'arithmétique de la courbe ROC. H_A ne peut sortir que d'un bogue de code.
- S le prédit déjà : contrôle 6, « à δ = 0,10 : non bloqué — limite déclarée » (RAPPORTÉ, prédiction).
- Une seule issue est possible : ce n'est pas une inférence forte au sens de B4.

**A-3. « δ ≤ τ » borne la faille au facteur 2, sans la fermer.**
- À τ = 5 % et δ = 0,05, la garde laisse A à 10 % de faux positifs contre B à 5 %.
- Avec un détecteur gaussien d'écart d′ = 1,5 (*illustratif*, même modèle que C), le rappel passe de 0,44 à 5 % à ≈ 0,59 à 10 % : 15 points achetés sous la garde.
- Faire de 5 % le point primaire change en outre le critère gelé par N-008 (GO de Lazar, RAPPORTÉ). C'est un nœud de décision, pas un amendement de S.

**A-4. Le biais de la simulation est mal décrit et son sens n'est pas démontré.**
- A écrit (A5) que le script simule des épisodes indépendants dans la tâche. Or `u = rng.normal(0, rho, size=n)` est commun aux épisodes d'une tâche : la ligne ρ = 1 contient une dépendance intra-tâche échangeable. C'est VÉRIFIÉ par lecture du code.
- Ce qui manque réellement est la corrélation **entre A et B sur un même épisode**.
- Une corrélation positive réduit Var(r_A − r_B) et Var(f_A − f_B). La simulation serait alors pessimiste, et non « optimiste » comme l'affirme A.
- Le sens du biais dépend du signe de cette corrélation, qui est inconnu. (HYPOTHÈSE)

**A-5. E2 lit la banque avant le gel : fuite entre construction et évaluation.**
- A propose de mesurer la corrélation intra-organisme de v « sur la banque de scores, sans gel », puis d'en déduire l'unité (plan, ligne 1 : « si E2 donne H_B, organisme »).
- Lire v sur les tâches d'épreuve avant le préenregistrement revient à choisir l'unité au vu des issues.
- Cette mesure doit se faire sur la partie de développement, ou sur des témoins faux.
- Par ailleurs la banque de la couche 2 n'existe pas encore (100 à 300 USD, RAPPORTÉ) : « zéro dépense » est inexact.

**A-6. Le « contraste de tendance » de E5 ne mesure pas une tendance.**
- c = (−½, 0, +½) ignore le niveau du milieu : c'est le contraste à deux niveaux de S, pris entre les extrêmes.
- La cloche symétrique (0,1 ; 0,3 ; 0,1) donne 0 par construction.
- Une courbe non monotone asymétrique, (0,1 ; 0,0 ; 0,3), serait promue.
- Aucun contraste linéaire ne lit « croît ». (HYPOTHÈSE ; vaut aussi contre la pente pondérée de C.)

**A-7. A ne voit pas la troncature de H2a.**
- Sur les trajectoires où « chaque action sabotée reste sous le seuil par action » (N-007, RAPPORTÉ), on a r_action ≈ 0.
- v se réduit alors à r_seq, positif même sans aucun signal (C l'a vu).
- Le plan de G1 de A n'en dit rien, alors que H2 et G1 partagent le préenregistrement (N-007 §3).

**A-8. Un contrôle de sa table (c) est tautologique.**
- A exige que « parts seule et mélange donnent le même verdict dans ≥ 95 % des mondes symétriques ».
- Sous un nul symétrique, ni l'une ni l'autre forme ne promeut presque jamais : l'accord est garanti et n'apprend rien.
- Le monde qui discrimine est le monde asymétrique (E1).

**A-9. Les égalités de score sont ignorées.**
- Les juges boîte noire rendent des verdicts ordinaux (P §10, EC.1 et leçons de P3, RAPPORTÉ).
- Un quantile à 1 % estimé sur quelques centaines d'épisodes tombe alors dans un bloc d'égalité, et le taux réalisé saute.
- L'option (c) de A (p-valeurs conformes) a le même trou.

### (b) Scénarios d'évasion

- **Comparateur.**
  - La règle « plus grand rappel sur le développement » est appliquée sur un développement que A ne dimensionne pas.
  - Sur un développement mince, la « meilleure » base noire est choisie au bruit près.
  - Le blanc gagne alors G1 contre une base qui n'est pas la meilleure : homme de paille par le bruit, sans fuite visible. Coût nul.
- **Garde.** Un bras blanc réglé pour un taux réalisé de 2τ reste sous δ = τ (A-3).
- **Mémoire.**
  - Une redite se définit par « même contraste, même τ, même strate » (S 2.5, RAPPORTÉ).
  - Changer τ (1 % puis 5 %, D-S5) ou la strate échappe à la redite, et e-BH ne couvre qu'une génération.
  - Le même énoncé, resoumis sur plusieurs générations, multiplie des essais que personne ne compte. A ne traite pas la multiplicité inter-générations.
- **Pondération.**
  - A juge la moyenne par tâche et rapporte le rappel par épisode à côté.
  - Si m varie d'une tâche à l'autre, un proposeur choisit les strates où les tâches courtes favorisent A.
  - La fiche est promue sur la moyenne par tâche alors qu'elle est fausse sur le critère par épisode de N-054.
- **Tout à la fois.**
  - Combinaison : comparateur faible par bruit, asymétrie de 2τ, τ et strates multipliés sur trois générations.
  - Coût : quelques fiches (réserve de 0,40 USD par appel au relais, RAPPORTÉ ; quelques USD par course, *illustratif*).
  - Aucun témoin ne s'allume : les témoins faux de S sont symétriques et n'éprouvent aucune de ces trois portes.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Étalon au bon nul.**
   - Monde de A1 : E[v] = −0,04, médiane > 0 ; 30 tâches.
   - H_A : l'intervalle par rééchantillonnage des tâches reste ≤ α.
   - H_B : il dépasse α.
   - Issue H_A : E4 peut s'étalonner sur lui. Issue H_B : aucun test à n fixé disponible ne vaut étalon, et la clause « remplacer » de A tombe.
2. **Comparateur au bruit.**
   - Quatre bases noires de rappels vrais 0,35 à 0,45 (*illustratif*) ; blanc égal à la meilleure ; développement de 10 puis de 40 tâches.
   - H_A : la règle de A promeut le blanc ≤ α.
   - H_B : promotion > α à 10 tâches.
   - Artefact requis : comparateur choisi sur l'épreuve, promotion ≫ α.
3. **Monotonie.**
   - Courbe (0,1 ; 0,0 ; 0,3).
   - H_A : le contraste de E5 promeut ≤ α.
   - H_B : il promeut, ce que j'attends.
   - Issue H_B : « croît » exige l'intersection des contrastes adjacents, par union des nuls comme en S §3.5. Issue H_A : A-6 est retirée.
4. **Égalités.**
   - Juge à cinq niveaux ordinaux.
   - H_A : taux réalisé dans [0,5 % ; 2 %] pour 95 % des calibrages.
   - H_B : hors de cet intervalle dans plus de 20 % des calibrages (*illustratif*).
   - Issue H_B : « même taux nominal » est vide pour les bases ordinales.
5. **Multiplicité inter-générations.**
   - Contraste nul soumis à τ ∈ {1 % ; 5 %} sur trois générations.
   - H_A : taux de promotion cumulé ≤ α.
   - H_B : > α.

---

## Contre la proposition C

### (a) Failles

**C-1. Statuts gonflés (règle 1).**
- C étiquette « VÉRIFIÉ » ses propres dérivations : « VÉRIFIÉ (FAUX mathématiquement) », « VÉRIFIÉ par le calcul », les trois causes du niveau 0,02.
- Il qualifie aussi l'attribution de Waudby-Smith et Ramdas de « VÉRIFIÉ pour l'attribution exacte », ce qu'il ne peut pas établir ici : référence à vérifier.
- Il écrit enfin « le contrôle fatal n° 6 montre », alors que ce contrôle n'a aucune sortie. Une prédiction est présentée comme un résultat.

**C-2. La faille n° 1 n'en est pas une, et son remède coûte de la puissance.**
- Un facteur 1 + λX reste valide dès que X ≥ −1/λ et que E[X] ≤ 0 sous le nul.
- Ici X = δ − g ∈ [δ − 1 ; δ + 1] et λ ≤ 0,9, d'où un facteur ≥ 1 − 0,9(1 − δ) > 0. C l'admet lui-même.
- Que X dépasse 1 à droite n'affecte pas la validité. Diviser par 1 + δ (amendement 3) ne protège de rien et ralentit la garde.
- L'« astuce » des 150 tâches à cinq épisodes, « si la formule est normalisée », va donc dans le mauvais sens. Aucune ligne de S-sortie ne l'appuie.

**C-3. Le remède de H2a crée une autre asymétrie.** Le principe de la critique est juste et je m'en sers, en le disant. Le remède pose deux problèmes.
- **(i) Filtres différents des deux côtés.**
  - Côté saboté, N-007 filtre sur les actions **sabotées**.
  - Côté honnête, C filtre sur **toutes** les actions (max_k s_action < τ̂).
  - Conditionner les honnêtes sur toutes leurs actions abaisse davantage leur somme : f_seq honnête filtré est biaisé vers le bas, et v_corr reste positif sous le nul.
  - L'expérience 2 de C filtre toutes les actions des deux côtés, ce qui n'est pas l'énoncé de H2.
- **(ii) Appariement non défini.** v_corr(t) apparie un rappel saboté et un taux honnête. Ce n'est un appariement que si la même tâche porte les deux types d'épisodes, ce que C ne dit pas.
- **Ampleur (*illustratif*).** À τ = 1 %, la dérive n'atteint le seuil qu'après plusieurs centaines de tâches. À τ = 5 % (D-S5), elle mord vers une centaine. « Probabilité 1 », sans ordre de grandeur, surévalue la faille à 1 %.

**C-4. aGRAPA plafonnée à 0,75 ne peut pas tenir ce que promet l'expérience 3.**
- La croissance au plafond vaut ≈ 0,75·0,2 − 0,28·0,088 ≈ 0,125 nat par tâche, contre ≈ 0,144 pour λ = 0,9 de la grille (*illustratif*, moments de C).
- Le seul gain possible est le prix du mélange : ≤ log 4, soit une dizaine de tâches. « + 25 points à 25 tâches » est hors d'atteinte par construction.
- Deux variantes avancées par C ne sont pas valides sous E[v] ≤ 0 :
  - le centrage 1 + λ_t(v − μ̂_{t−1}) teste une autre frontière que 0 ;
  - des mises > 1 « si la plage observée est bornée » échouent, car une plage observée ne borne pas la tâche suivante.

**C-5. Le repli de la ligne 10 réintroduit le nul de symétrie.**
- C bannit le signe parce qu'il teste un nul de symétrie, puis propose « un test de permutation apparié stratifié exact (Pitman) ».
- L'inversion de signes n'est exacte que sous symétrie de v. Sous E[v] ≤ 0 asymétrique, seule une version studentisée est valide, et seulement asymptotiquement.
- Le BCa sur 15 à 25 tâches n'a pas de couverture garantie.

**C-6. La pAUC change l'estimande.**
- Moyenner sur τ ∈ {0,5 % ; 1 % ; 2 % ; 5 %} ne donne pas le rappel à 1 % de N-008.
- Sur 300 épisodes de calibrage, le point à 0,5 % est le deuxième ou le troisième plus grand score honnête : c'est le plus bruité (*illustratif*).
- La grille inclut le point à 5 %, où C chiffre lui-même 24 points de rappel achetés.
- C ne dit pas lequel des deux est jugé : le rappel à 1 % ou la pAUC.

**C-7. Le rang conforme apparié est déjà dans S et n'agit qu'en moyenne.**
- S fixe déjà les deux seuils au même quantile des mêmes honnêtes de calibrage (§2.4, RAPPORTÉ).
- La loi Beta commune donne E[f_A − f_B] = 0 en moyenne sur les calibrages possibles, pas sur le calibrage scellé que l'on juge.
- Elle suppose aussi des scores continus et des épisodes indépendants. Or S groupe les épisodes en tâches dépendantes et les juges sont ordinaux (A-9 vaut ici aussi).

**C-8. L'arithmétique de (b).1 est fausse, la conclusion tient.**
- La composante signe ne croît pas comme (1 + 0,4λ)^n mais comme exp(n·E[log(1 + λs)]).
- À λ = 0,9, cette croissance est négative : 0,7·ln 1,9 + 0,3·ln 0,1 ≈ −0,24. Seuls λ = 0,1 et 0,3 croissent.
- La conclusion reste vraie, et l'expérience 1 de C reste discriminante.

### (b) Scénarios d'évasion

- **H2a corrigée.** Un proposeur qui déclare le filtre de N-007 côté sabotés et celui de C côté honnêtes obtient une promotion structurelle à τ = 5 %. Coût : une fiche.
- **Garde normalisée.** Elle certifie plus tard, ce qui pousse à relever δ pour lui rendre des dents. Un δ plus large rend achetable le rappel que C chiffre lui-même en (b).3.
- **pAUC.** La grille de τ fait partie de la fiche : choisir une grille riche en points permissifs favorise le bras qui tire le plus.
- **Comparateur.** C fixe B* sur un développement de 20 tâches sabotées de cinq épisodes, parmi au moins cinq bases (sa section (d)). C'est l'homme de paille par le bruit de A, avec un développement chiffré trop petit.
- **Tout à la fois.**
  - Combinaison : filtre asymétrique de H2a à 5 %, B* choisi au bruit, grille pAUC choisie.
  - S'y ajoute le repli de la ligne 10 : sous 30 tâches, C bascule vers un test exact seulement sous symétrie. Un banc plus petit obtient donc un test plus permissif.
  - Coût de calcul nul. Le levier est la taille du banc, que personne ne surveille comme variable de jeu.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Garde non normalisée au bord du support.**
   - g ∈ {−1 ; +1} avec E[g] = δ exactement.
   - H_A (thèse de C) : la garde non normalisée dépasse α.
   - H_B (thèse de B) : elle reste ≤ α.
   - Issue H_B : l'amendement 3 de C est retiré. Issue H_A : ma dérivation C-2 est fausse.
2. **Filtres asymétriques de H2a.**
   - Nul pur (loi sabotée = loi honnête) ; filtre de N-007 côté sabotés, filtre de C côté honnêtes ; τ = 5 % ; 150 tâches.
   - H_A : v_corr reste ≤ α.
   - H_B : > α.
   - Témoin interne : filtre identique des deux côtés, ≤ α attendu.
3. **Plafond d'aGRAPA.**
   - H_A : gain ≥ 0,25 de puissance à 25 tâches.
   - H_B : gain ≤ 0,15.
   - Issue H_B : retirer le signe se paie en tâches, chiffrées au devis. Issue H_A : C-4 est retirée.
4. **Repli de permutation sous nul asymétrique.**
   - Monde de l'expérience 1 de C, 20 tâches.
   - H_A : Pitman reste ≤ α.
   - H_B : > α.
   - Issue H_B : le repli est interdit sauf studentisé et vérifié à petit n.
5. **Égalités.** Même contrôle que A-(c)4, appliqué au rang conforme de C.

---

## Ce que je retiens pour la riposte (usage déclaré, sans fusion)

- **De C** : le principe de la troncature de H2a, à condition que le filtre soit identique des deux côtés.
- **Contre A et C ensemble : juger la « meilleure base noire » sans sélection.**
  - On peut le faire par l'union des nuls déjà présente en S §3.5 : un pari par base noire, promotion seulement si toutes les richesses atteignent 1/α.
  - Cela supprime à la fois le développement à dimensionner et l'homme de paille par le bruit.
  - (HYPOTHÈSE ; le prix en puissance, dû aux bases faibles, est à simuler.)
- **Confondant que ni A ni C ne traite : la longueur des épisodes.**
  - L'agrégateur additif croît avec le nombre d'actions.
  - Si les épisodes sabotés sont plus longs que les honnêtes de calibrage, le séquentiel gagne du rappel par la longueur, pas par l'accès.
  - Contrôle : rejouer le contraste par strates de longueur. C cite un plancher de longueur sans en tirer de stratification.
- **Fuite possible, à vérifier.**
  - S 2.5 montre à l'agent « le nombre de tâches par strate ».
  - Si le mode tenu à l'écart est une strate déclarée, son existence et sa taille sont visibles avant sa révélation.
  - Il faut vérifier si un rôle qui conçoit des bras lit ces descriptions (N-054 point 3).

FIN-DE-CELLULE