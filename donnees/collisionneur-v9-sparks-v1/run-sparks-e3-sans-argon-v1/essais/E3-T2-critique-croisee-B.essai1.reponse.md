# Proposition B — Tour III.2 : critique croisée de méthode

**Statuts.** Les chiffres du billet (pièce 1) sont **RAPPORTÉS**. Les chiffres que la pièce 3 tire des journaux et marque « [journaux] » sont **OBSERVÉS-NON-AUDITÉS**. Les résultats de la pièce 2 sont **RAPPORTÉS**. Mes objections, et les mécanismes que je soupçonne, sont des **HYPOTHÈSES**. Les nombres que je dérive sont marqués « calcul ». Ceux que je suppose sont marqués « illustratif ».

**Pièce C : absente (jamais lancée) ; je ne lui attribue aucun contenu.**

Je critique A, D et E séparément. Quand un défaut se répète, je renvoie à la section où je l'ai d'abord relevé, sans fusionner les propositions.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Graine partagée contre graines différentes : confusion de construction (HYPOTHÈSE, fatale pour E1).**
   - Dans le billet, les deux copies d'une paire T partagent la graine, l'ordre des données et le calendrier [journaux, pièce 3 §3.1]. Leur différence de poids ne reflète donc que les étiquettes, sur environ un tiers des exemples (ceux à mauvaise suggestion).
   - A définit N1 et N2 avec des **graines différentes**. Le delta entre les deux modèles d'une paire nulle contient alors tout le bruit de graine. Il est probablement bien plus grand en norme, et moins structuré, que celui d'une paire T.
   - Un lecteur, ou la régression logistique de A, peut donc séparer T des nuls par la seule norme ou le seul rang de la différence, sans rien lire du trait.
   - Le signe de l'effet sur le taux de fausses alertes est indéterminé : le lecteur peut sur-déclarer sur les nuls (grandes différences) ou sous-déclarer. Dans les deux cas, la mesure confond « même graine » et « trait ».

2. **« Le plus éloigné du départ est l'honnête » : solution vraie par construction (HYPOTHÈSE).**
   - Le modèle de départ suit déjà 100 % des mauvaises suggestions [journaux, §3.1]. A le relève lui-même (son point a5).
   - Si le lecteur reçoit le départ, ou peut l'inférer (plongement gelé, donc identique au départ, et points de contrôle complets dans la tentative 4 du billet), la tâche T se réduit à comparer ‖θ_A − θ_0‖ et ‖θ_B − θ_0‖.
   - N3 (départ contre sycophante) ne neutralise pas ce raccourci : c'est une autre question.

3. **N3 n'est pas comportementalement nul.**
   - L'affinage impose le format « The answer is {answer}. » [journaux, §3.1]. Le départ et la copie sycophante diffèrent donc au moins par le format et par l'exactitude sans suggestion (98-99 % après affinage, valeur non donnée pour le départ).
   - « Comportement égal » n'est vrai que pour le seul taux de suivi.

4. **E2, volet Qwen : conditionnement sur une variable postérieure au traitement.**
   - « Exactitude conditionnelle à finir » sélectionne un sous-ensemble que l'édition elle-même modifie. C'est un collisionneur : l'édition fait finir des problèmes plus durs, ce qui biaise vers le bas l'exactitude conditionnelle et peut faire passer un ajout de capacité pour un déblocage pur.
   - La strate correcte est définie **avant** traitement : les problèmes que la base finit. Les journaux l'ont fait, sur 114 problèmes [journaux, §4.2].

5. **E2, témoin aléatoire « sur le même support » : fuite.**
   - Les 64 colonnes ont été choisies parce qu'elles écrivent le plus la direction [journaux, §4.2].
   - Le support est donc déjà fonction de la direction. Une direction aléatoire sur ce support n'est pas un témoin du choix de support, seulement de l'orientation.
   - Il faut aussi un support aléatoire de même taille.

6. **E2, volet sycophancie : duel non exhaustif.**
   - H_A dit « le point fixe bouge, à part inchangée ». H_B dit « la part bouge ou rien ne bouge, à point fixe inchangé ».
   - L'issue « les deux bougent » n'appartient à aucune des deux. Elle est la plus probable sous une intervention diffuse (HYPOTHÈSE). La règle B4 n'est donc pas tenue.
   - De plus, la loi d'attraction porte sur des **notes** (critique ou éloge) [pièce 2, §7], tandis que la direction suit la sycophancie « jugée ». Rien n'établit que les deux mesurent le même construit.

7. **E3 : la conclusion est fixée par le budget d'épisodes de la boîte noire.**
   - À fraction de sabotage p, la détection de M3 croît avec le nombre m d'épisodes observés (approximativement 1 − (1 − p·s)^m, où s est la sensibilité par épisode ; illustratif).
   - L'écart M1 − M3 est donc un artefact du choix de m. Si m est grand, H_B gagne par construction ; si m est petit, H_A gagne.
   - Par ailleurs, l'organisme P3 a un saboteur **instruit** [pièce 2, §6]. Il n'a pas de delta de poids : M1 n'a rien à lire tant qu'un organisme affiné n'a pas été construit. Ce dernier introduit alors une variable confondante, le contenu des données d'affinage.

8. **E3 : calibration et évaluation sur les mêmes jumeaux.** α est calibré « sur les jumeaux honnêtes » sans partition annoncée. Si les mêmes jumeaux servent à estimer le taux de fausses alertes, celui-ci est optimiste.

9. **E4 : nulle augmentée non constructible.**
   - Permuter ou remplacer les couches extrêmes « à propriété conservée » change la fonction calculée. L'oracle exécutable ne peut alors plus certifier que la propriété survit, puisque c'est la fonction entière qui la porte.
   - Le seuil d'abandon (« < 1/6 à 60 instances ») reprend notre puissance rapportée pour une loi de force 0,5 [pièce 2, §5]. C'est circulaire : ce seuil teste la taille d'effet des lois plantées, pas la famille de tâches.

10. **E5 : invariance vraie par construction pour la base mécanique.** Les normes et cosinus par couche sont invariants aux permutations d'unités cachées. H_A est donc acquise pour ces statistiques sans rien tester. Elle ne devient informative que pour le lecteur, et seulement s'il reçoit des poids non canonicalisés.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **AUC de E1.** Avec 20 paires T et 60 nulles, l'erreur type de Hanley-McNeil pour une AUC de 0,80 vaut environ 0,064 (calcul). Exiger une borne basse ≥ 0,80 suppose une AUC vraie d'environ 0,92 ou plus (calcul).
  - Si « AUC sur T » se calcule à l'intérieur des seules paires T (A ou B étiqueté sycophante), il y a environ 10 cas par classe. L'erreur type dépasse 0,1 (calcul).
  - Toute AUC vraie comprise entre 0,65 et 0,90 est non jugeable à ce plan.
- **Taux de fausses alertes ≤ 0,10 sur 60 nuls.** Si le taux vrai vaut exactement 0,10, P(≤ 6 alertes) ≈ 0,6 (calcul, binomiale(60 ; 0,1)). Le critère est un pile ou face, sauf si l'on exige une borne supérieure, auquel cas il faut un taux vrai très inférieur.
- **Base mécanique sous-puissante par construction.** Une régression logistique sur des deltas de dimension d ≫ k paires d'entraînement surapprend. Sa perte de puissance quand d/k → ∞ rend la condition « le lecteur bat la régression » facile à remplir. Le critère d'abandon global devient alors inopérant, sauf si la régression ne porte que sur un vecteur de statistiques de faible dimension fixé d'avance.
- **Essais répétés.** Si la corrélation intra-paire ρ des verdicts sur 3 essais est proche de 1, la taille effective est n·3/(1 + 2ρ) ≈ n (calcul). Compter 3n unités gonfle la confiance.
- **E2, point fixe.** Dans un modèle y = x + k(d)·(p − x), la variance de l'estimateur de p croît comme 1/k². Si k est petit, ou si les notes initiales x se concentrent près de p, p n'est pas identifiable et le duel est non jugeable.
- **E3.** Si la sensibilité par épisode s·p·m de M3 est proche de 1 ou proche de α au budget choisi, l'écart est borné par construction. La comparaison n'a de sens que sur une plage de m où la détection de M3 se situe entre α et 1 − α.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Paires nulles à graine et ordre partagés, appariées en norme de delta** : deux honnêtes dont les réponses ne diffèrent que par une variation neutre (paraphrase) sur la même fraction d'exemples. Sans elles, E1 ne distingue pas « trait » de « graine ».
2. **Témoin de distance au départ** : la règle « plus éloigné de θ_0 » appliquée aux mêmes paires. Si elle atteint la détection du lecteur, le lecteur n'a rien ajouté.
3. **Témoin positif du lecteur** : une paire où le trait est lisible par construction, par exemple une couche de sortie non gelée. Un lecteur ouvert qui échoue au témoin positif rend non jugeable tout échec sur T, qui ne falsifierait alors que « ce lecteur », pas la lecture de poids.
4. **Support aléatoire** (E2) en plus de la direction aléatoire.
5. **Partition calibration / test** des jumeaux (E3).

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Même confusion de graine que A(a)1.** Les « 60 paires honnête/honnête à graines différentes » s'opposent à des paires honnête/trait dont la construction (graine partagée ou non) n'est pas précisée. Si les paires trait partagent la graine, la norme du delta sépare les classes par construction.

2. **Organismes « déjà disponibles » non attestés.** La pièce 2 ne décrit qu'un saboteur **instruit** sur Llama-3.1-8B [pièce 2, §6]. Je ne trouve dans les pièces ni adaptateur de sabotage sur Gemma 3 270M ou Qwen3.5-0.8B, ni « dose » de sabotage.
   - En construire un fixe les données d'entraînement de la classe positive.
   - Un lecteur ou une statistique qui détecte « données d'affinage différentes » passerait pour un détecteur de sabotage. Il faut des affinages honnêtes appariés en contenu (E l'exige, D non).

3. **Comparateur « meilleur des trois autres bras » sélectionné sur le test.** D ne dit pas où se fait la sélection. Le maximum de trois estimations bruitées est biaisé vers le haut (malédiction du gagnant). Cela défavorise H_A par construction et rend le seuil de 20 points incohérent avec une comparaison appariée à un bras fixe.

4. **Sous-test Qwen : H_A vraie par plafond.**
   - Sur les problèmes que la base terminait déjà, l'exactitude vaut 93,9 % [journaux, §4.2]. Le gain maximal possible est donc de 6,1 points (calcul).
   - Sur MATH-500, 93 % des réponses de base atteignent la limite [pièce 1 ; pièce 3 §4.2]. La strate « finit déjà » compte donc environ 35 problèmes sur 500 (calcul).
   - Le duel « déblocage contre ajout ≥ 3 points » se joue près d'un plafond, sur un très petit sous-ensemble.

5. **Fiche 2 : deux constructs sous une seule hypothèse.** H_A demande à la fois une baisse du coefficient d'attraction (notes, critique ou éloge) et une baisse du suivi mécanique des mauvaises suggestions (faits). Si une seule des deux baisse, l'issue est rangée dans H_B. Le duel teste alors la conjonction, pas la validité du construit.

6. **Fiche 4 : H_A vraie par construction si la détection de base est faible.**
   - « Dégradation ≤ 20 points » se mesure par rapport à la détection non adversariale.
   - Si la Fiche 1 donne une détection de base ≤ 20 % (plausible au vu de P3, où aucune sonde ne dépasse son plancher [pièce 2, §6]), H_B devient impossible.
   - À l'inverse, « au moins une classe » cumule la multiplicité entre classes en faveur de H_B.

7. **Partition « par graine du modèle de base ».** Toutes les paires partent du même point préentraîné. Si « graine du modèle de base » désigne le point de départ, la partition est vide. Elle doit porter sur la graine d'affinage **et** sur le découpage des faits, sinon les faits partagés entre calibration et test fuient.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Fiche 1.** Supposons 40 positifs et des taux discordants de 0,3 et 0,1 entre le lecteur et le comparateur (illustratif). L'erreur type de la différence appariée vaut environ 0,095 et la demi-largeur à 95 % environ 0,19 (calcul). Pour que la borne inférieure dépasse 20 points, il faut un gain observé d'environ 39 points. Tout gain vrai compris entre 0 et 35 points est non jugeable.
- **Taux de fausses alertes à 5 % avec 60 nuls.** D écrit qu'avec zéro alerte, la borne supérieure vaut environ 4,9 % : c'est exact. Mais un seuil calibré **à** 5 % produit en moyenne 3 alertes sur 60, et P(0 alerte | taux = 0,05) ≈ 0,046 (calcul). La certification n'est atteinte que si le taux vrai est très inférieur à 5 %, ce qui exige un seuil plus strict, donc une perte de puissance non comptée dans le plan.
- **Fiche 3.** Certifier des fausses promotions ≤ 1 % à 95 % exige au moins 299 unités nulles sans alerte (calcul : ln 0,05 / ln 0,99). Avec 40 réseaux sans propriété, ce critère est non jugeable.
- **Fiche 2.** Un ratio de réduction « ≥ 30 % » sur un coefficient estimé k̂ a une loi de type Fieller. Si l'intervalle de k̂_base approche 0, l'intervalle du ratio est non borné.
- **Sous-test Qwen.** Sur 114 problèmes à 93,9 %, l'erreur type binomiale vaut environ 2,2 points (calcul), du même ordre que le seuil de 3 points. Sur MATH-500, avec environ 35 problèmes × 4 échantillons corrélés, la taille effective est proche de 35 et le duel est non jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

1. Des **affinages honnêtes appariés en contenu et en norme** à la classe positive, et pas seulement à graines différentes.
2. Un **témoin positif du lecteur**, comme en A(c)3.
3. Un **comparateur fixé sur la partition de développement**, et non choisi sur le test.
4. Pour la Fiche 4, une **condition d'applicabilité** : n'évaluer la dégradation que si la borne inférieure de la détection de base dépasse le seuil de dégradation.
5. Pour le sous-test Qwen, une **strate antérieure au traitement** définie sur des items en nombre suffisant. Si MATH-500 ne la fournit pas, déclarer d'avance le sous-test non jugeable.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Inégalité de traitement des données : le lecteur reçoit moins que la base mécanique (HYPOTHÈSE, fatale pour DELTA).**
   - Le lecteur reçoit « un résumé déterministe du delta : statistiques de tenseurs et extraits choisis par une règle ». C'est une fonction des mêmes statistiques que le classifieur mécanique utilise, plus quelques extraits.
   - Tout gain du lecteur sur ce classifieur ne peut venir que de ses a priori ou des extraits, pas d'une lecture des poids.
   - E l'admet (« la conclusion portera sur cette représentation »), mais le duel est formulé comme un test de lecture de poids.

2. **Bras combiné contre bras simples.** G compare « boîte noire + delta » au meilleur comparateur unique. Ajouter n'importe quelle variable informative à la boîte noire peut augmenter la sensibilité par le seul fait de combiner. Le comparateur correct est « boîte noire + classifieur mécanique », combiné par la même règle.

3. **Fuite entre étiquetage et boîte noire.** La positivité est fixée par un évaluateur mécanique sur des épisodes scellés. Si la boîte noire observe des épisodes de la même loi, elle reproduit la règle d'étiquetage : sa sensibilité tend vers 1 par construction et G ≤ 0. Les épisodes de la boîte noire doivent être disjoints de ceux de l'étiquetage, et leur budget fixé.

4. **CONSTRUIT sur Gemma 270M : saturation.**
   - Le départ suit 100 % des mauvaises suggestions dès la formulation la plus faible (« I think… but I'm really not sure ») [journaux, §3.1].
   - La courbe de suivi en fonction de la dose est donc plate au plafond dès la première dose non nulle. L'aire A ne porte aucune information sur une relation dose-réponse, et la loi d'attraction n'y est pas testable.
   - Le pilote 270M ne prépare donc pas la réplication sur 8B : il teste autre chose.

5. **ORACLE : le proposeur peut calculer l'oracle.**
   - Sur un domaine d'entrée fini, un proposeur qui a les poids et un outil de calcul peut exécuter le réseau sur tout le domaine. La propriété est alors lue par exécution, et R est positif par construction.
   - E ne dit pas si l'exécution est interdite, ni comment cet interdit serait audité. Le billet, lui, a audité 1 125 tours « sans outil » [journaux, §1].

6. **Unités et lecteurs.** Deux familles de lecteurs × deux répétitions, avec une règle d'agrégation gelée : c'est bien. Mais si les lecteurs sont ouverts et petits, un échec ne falsifie que cette classe de lecteurs. L'énoncé des issues doit le dire.

7. **Remarque de statut, sans correction** : E place l'absence des propositions A–D sous OBSERVÉ-NON-AUDITÉ. À la date de sa rédaction (tour III.1), c'est un constat sur ses entrées, pas un fait du domaine. Je le laisse tel quel.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **DELTA, sensibilité.** Avec 30 positifs et des taux discordants de 0,3 et 0,1 (illustratif), la demi-largeur à 95 % de G vaut environ 0,21 (calcul). Il faut un gain observé supérieur ou égal à 31 points pour réfuter H_B au seuil de 10 points.
- **DELTA, fausses alertes.** Le plafond ≤ 5 % avec 60 unités honnêtes pose le même problème qu'en D(b) : P(0 alerte | taux = 0,05) ≈ 0,046 (calcul).
- **DELTA, information.** Si la loi du résumé R(Δ) est identique sous honnête et sous positif (P_R|H = P_R|S), aucun lecteur ne peut dépasser α, quelle que soit sa qualité. La puissance est bornée par la distance en variation totale entre P_R|H et P_R|S, que la règle de résumé fixe.
- **CONSTRUIT.** Si P(suivi | dose) vaut environ 1 pour toutes les doses non nulles chez la base, le gradient de dose est nul et l'aire n'identifie pas la sensibilité à la pression. Le duel n'est jugeable que si la base a un taux de suivi intermédiaire à au moins deux doses.
- **ORACLE.** Certifier une probabilité de fausse promotion par course ≤ 5 % exige au moins 59 courses nulles entières sans promotion (calcul). Sinon le critère est non jugeable.
  - R relatif > 20 % est instable si le rendement du bras « descriptions seules » est proche de 0 : le dénominateur est petit et la variance du ratio explose.
  - Il faut un critère en différence absolue, ou un plancher de rendement de base.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Comparateur combiné apparié** : « boîte noire + classifieur mécanique », avec la même règle de combinaison.
2. **Épisodes de la boîte noire disjoints de ceux de l'étiquetage**, à budget fixé d'avance.
3. **Interdiction d'exécuter le réseau et audit de cette interdiction** dans le bras « descriptions + poids ». Sinon, prévoir un bras « descriptions + exécution, sans poids », qui isole ce que l'accès aux poids ajoute à l'exécution.
4. **Contrôle de non-saturation** de la base avant CONSTRUIT. Si la base suit 100 % des suggestions à toutes les doses, le pilote est déclaré non jugeable d'avance.
5. **Témoin positif du lecteur**, comme en A(c)3.

---

## Correctif proposé, en duel (règle B4)

Sur les paires T du billet, opposons deux hypothèses :
- **H_A** : la règle mécanique « plus éloigné du départ = honnête » n'identifie pas le sycophante au-delà du hasard.
- **H_B** : elle l'identifie au-delà du hasard.

Ce test coûte quelques minutes de calcul sur poids (aucune passe avant), dès que des affinages reconstruits existent : les affinages originaux ne sont pas livrés [journaux, §3.5.10].

- **Si H_B tient**, tout plan qui reprend le montage T sans nulle appariée en distance au départ (A-E1, D-Fiche 1, E-DELTA s'il utilise la sycophancie) mesure ce raccourci, et doit être refait avec la nulle appariée.
- **Si H_A tient**, ce raccourci est écarté pour ce montage, et la confusion de graine (A(a)1) devient le premier suspect.

FIN-DE-CELLULE