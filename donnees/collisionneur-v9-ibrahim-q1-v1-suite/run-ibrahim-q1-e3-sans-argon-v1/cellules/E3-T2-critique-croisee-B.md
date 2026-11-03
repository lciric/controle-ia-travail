# Proposition B — Tour III.2 : critique croisée de méthode

**Statuts.** Les faits de la pièce Ibrahim sont RAPPORTÉS : un rapport les a lus sur page primaire. Pour les chiffres des dépôts de Lazar (pièce sycophancie), A les classe RAPPORTÉ et D les classe OBSERVÉ-NON-AUDITÉ. Je ne tranche pas cet écart et je le signale à l'arbitre. Mes critiques sont des HYPOTHÈSES de méthode. Mes nombres sont marqués « calcul » ou « illustratif ». Je ne fusionne pas les propositions. Quand un défaut se répète, je renvoie à la section où je l'ai d'abord traité.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Statut mal posé (règle 1).** Au point (a)5, A classe l'accès aux poids OCT en OBSERVÉ-NON-AUDITÉ. Or la pièce dit seulement « accès filtré annoncé, non vérifié » (pièce Ibrahim §3). Personne n'a observé cet accès. Il s'agit d'une annonce RAPPORTÉE, dont rien n'a été vérifié.

2. **E1 : le duel n'est pas exhaustif, et son seuil est incohérent.**
   - H_A exige un déplacement de l'erreur **et** un déplacement de g. H_B exige qu'aucun des deux ne bouge. Les cas mixtes (l'erreur bouge mais pas g, ou l'inverse) ne falsifient rien, ce qui contrevient à B4.
   - H_A pose « ≥ +11 points », alors que le seuil opérationnel est de 5 points.
   - La portée du « +11 » n'est pas établie : le rapport ne dit pas s'il vaut pour Llama-3.1-8B seul (pièce Ibrahim §1.1 et §4). En faire le niveau attendu sur ce modèle déborde ce que dit le fait.

3. **E1 : le seuil Δg ≥ 0,2 est étiqueté « calcul », mais c'est un choix.**
   - L'intervalle [−0,220 ; 0,197] porte sur un contraste **intra-modèle** entre doses, sous critique, sur 1 350 générations (pièce sycophancie §1).
   - Un écart **entre deux points de contrôle** additionne la variance de deux ajustements indépendants. Il a donc au moins la même variance, et sans doute davantage.
   - Fixer le seuil à la demi-largeur du bruit donne une puissance d'environ 50 % quand le vrai Δg vaut 0,2 (calcul, sous normalité).

4. **E1 : le contrôle négatif prouve autre chose que ce qu'A annonce.**
   - A compare la base Instruct munie d'une consigne reprenant la persona au modèle entraîné. Si les deux produisent le même déplacement, cela montre que la consigne induit la même sycophancie que l'entraînement. Cela ne montre pas que le juge « lit le style ».
   - Le même défaut revient en (c), pour le classifieur : la base munie d'une consigne chaleureuse et classée *Loving* compte comme fausse alerte, alors qu'une sortie réellement chaleureuse classée *Loving* est une détection correcte.
   - Une fausse alerte doit porter sur une sortie qui **n'a pas** le construit visé.

5. **Fuite entre la construction de l'instrument et son évaluation.**
   - La rétention de la persona (E2) est lue par le classifieur d'OCT. Ce classifieur est fondé sur des modèles, et ses biais et sa circularité sont déclarés (pièce Ibrahim §2).
   - Toute dérive de distribution due au RLVR (format, longueur, registre) éloigne les sorties de ce que le classifieur reconnaît. Elle se lit alors comme une érosion, presque par construction.
   - La troncature à longueur fixe ne règle pas ce point. Elle est elle-même une source d'artefact : la troncature à 300 caractères a déjà produit un faux positif (pièce sycophancie §3).

6. **Régression vers la moyenne dans g (E1, E2).**
   - Si la même estimation bruitée de la note sans pression v̂₀ sert à la fois à définir Δ et à servir de régresseur, une pente positive apparaît même sans aucune attraction.
   - Ce biais vaut environ σ²_e / Var(v̂₀), où σ²_e est la variance de bruit de v̂₀ (calcul, modèle d'erreur classique).
   - Une persona qui change la dispersion entre tirages change ce biais. Elle peut donc fabriquer un Δg sans que la loi d'attraction bouge.

7. **E2 : la falsification annoncée ne suit pas.**
   - H_B se déclenche dès que la rétention passe sous 50 %, même si g ne bouge pas. Une issue H_B n'implique donc pas un déplacement de g.
   - Même quand g bouge sous RLVR, l'a priori de R8 (« le gain vient de l'optimisation des préférences ») n'est pas réfuté : une cause peut avoir plusieurs sources.
   - R8 vise en outre la chaîne Tülu 3, pas OCT (pièce sycophancie §2).
   - Enfin, la zone de rétention entre 50 et 80 % avec |Δg| < 0,2 ne falsifie rien.

8. **E2 : la persistance peut être vraie par construction.**
   - Un RLVR sur des problèmes vérifiables, sous pénalité KL et sur quelques centaines de pas, peut laisser la distribution presque intacte sur les prompts de persona.
   - « La persona tient » mesurerait alors la distance parcourue, non la robustesse.
   - L'axe de dose doit être exprimé en divergence mesurée sur les prompts d'évaluation, pas en nombre de pas.

9. **E3 : facteurs confondus et seuil d'interaction trop bas.**
   - Le facteur « RL à préférences » est confondu avec le contenu des paires. Les réponses préférées de PRISM, UltraFeedback et LMSys contiennent plus de validation (pièce Ibrahim §1.6). Le « contrôle » sur paires équilibrées est en réalité une troisième modalité du traitement, pas un contrôle négatif.
   - *Loving* part déjà haut en validation. Sur une échelle bornée, l'interaction persona × étape dépend de l'échelle choisie : un plafond peut la créer ou l'effacer.
   - Pour un contraste d'interaction en 2 × 2, l'erreur type vaut √4·σ_cellule, contre √2·σ_cellule pour une simple différence, soit un facteur √2 (calcul, cellules indépendantes de même variance). Reprendre le seuil de 0,2 d'E1 sous-dimensionne donc encore davantage.

10. **Dérive du juge.** Le juge Claude est un alias d'interface non figé (pièce sycophancie §1). Si l'on juge avant et après RL à des dates différentes, le Δ mesuré inclut un éventuel changement de version du juge.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Rétention R = C_après / C_avant.**
  - L'intervalle de Fieller de R n'est borné que si l'intervalle de C_avant exclut 0 au même niveau.
  - Si le classifieur sature, avec un score proche de 1 pour la base comme pour la persona, C_avant tend vers 0 et R n'est pas jugeable.
- **Pente g.**
  - SE(ĝ) ≈ σ_ε / (√n · sd(v₀)). Si la persona comprime la distribution des notes sans pression (Var(v₀) tend vers 0, effet plafond), ĝ devient indéterminé.
  - Si les déplacements deviennent constants, avec Var(Δ | v₀) indépendant de v₀ (cas de Qwen et Mistral, R3, pièce sycophancie §1), g n'est plus distinguable d'un modèle à déplacement constant.
- **Refus.**
  - Si la probabilité de refus diffère entre bras, exclure les items à refus revient à conditionner sur une variable postérieure au traitement : l'estimateur est biaisé, quelle que soit la taille de n.
  - Il faut une exclusion commune par item, fixée d'avance sur l'union des bras.
- **Graines d'entraînement.**
  - Si la variance entre entraînements τ² domine la variance entre items, la puissance dépend du nombre d'entraînements, pas du nombre de générations.
  - A ne donne pas ce nombre pour E2. Avec un seul entraînement par départ, τ² n'est pas estimable et aucun intervalle n'est valide.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Sorties honnêtes appariées** : même position et même contenu, seul le style change. C'est le seul vrai négatif pour le classifieur et pour le juge. Il manque.
2. **Dose nulle placebo**, avec v₀ estimé sur des tirages disjoints de ceux qui servent à calculer Δ. Sans cela, ĝ > 0 peut n'être qu'une régression vers la moyenne.
3. **Test-retest d'un point de contrôle non modifié**, évalué deux fois par le même instrument : il donne le plancher de bruit de la rétention. Le contrôle 2 d'A (autodistillation par ajustement supervisé) modifie les poids et ne remplit pas ce rôle.
4. **Jeu d'ancrage rejugé à chaque passe**, pour détecter la dérive du juge.
5. **Pour E3, un modèle de récompense à préférences permutées**, qui mesure ce que fait l'optimisation contre une récompense sans signal.

---

## Sur la proposition C

Pièce absente (jamais lancée). Je n'en critique aucun contenu.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **La falsification porte sur des estimations ponctuelles.**
   - En E1, « R ≥ 0,50 falsifie H_B » est énoncé sans règle d'intervalle. Une estimation ponctuelle ne falsifie rien.
   - E, au contraire, l'écrit explicitement : un intervalle à cheval sur le seuil donne un verdict indécis.

2. **E1 : l'instrument qui mesure C n'est pas nommé.** Si c'est le classifieur d'OCT, la fuite décrite en A(a)5 s'applique telle quelle.

3. **E1 : le témoin à récompense permutée n'est pas apparié en ampleur de changement.**
   - Une récompense aléatoire produit des gradients qui se compensent en moyenne. À nombre de pas égal, ce bras change moins la politique que le bras à vraie récompense.
   - Un écart de rétention entre les deux mesurerait alors la quantité de changement, pas l'optimisation.
   - L'appariement doit se faire sur la divergence KL atteinte, pas sur le nombre de pas.

4. **E2 : les attentes contredisent celles d'E1.**
   - E1 attend une légère érosion (R = +0,85).
   - E2 attend une double différence ΔS = +12 points, donc un RL qui **amplifie** la sycophancie sociale propre à la persona.
   - Sans mécanisme d'amplification énoncé, les deux attentes sont incompatibles. L'une des deux ne peut pas être « l'attente ».

5. **E2 : S et F sont lus sur deux échelles qui ne se comparent pas.**
   - S provient d'un juge, F d'un extracteur exact. La différence ΔS − ΔF en points dépend des taux de base et de la fiabilité propre à chaque instrument.
   - Un instrument plus bruité atténue sa double différence. Si les fiabilités diffèrent, une « sélectivité » peut apparaître ou disparaître sans rien changer au comportement.

6. **E2 : un « ton constant » est impossible à imposer à une persona.**
   - Ibrahim §1.5 manipule la sycophancie à ton constant par construction expérimentale (pièce Ibrahim §1.5).
   - Ici, le ton est l'effet du traitement : on ne peut pas le maintenir constant dans les sorties.
   - Il faut soit une notation aveugle au ton, soit une normalisation postérieure validée. Sinon, la condition annoncée n'est pas réalisée.

7. **E3 : la marge d'équivalence rend H_A pratiquement inconfirmable.**
   - H_A exige |Δg| < 0,05. Avec une demi-largeur d'environ 0,21 à 1 350 générations, contraste intra-modèle (pièce sycophancie §1), atteindre une demi-largeur de 0,05 demande environ (0,21/0,05)² ≈ 17,6 fois plus de données, soit environ 24 000 générations par contraste (calcul, SE ∝ 1/√n, même structure de variance).
   - Pour un contraste entre points de contrôle, la demande est encore plus forte.
   - Seule l'issue H_B peut donc gagner : le duel est asymétrique.
   - E3 hérite aussi du biais de régression vers la moyenne décrit en A(a)6.

8. **Les seuils de validation (c) ne sont pas vérifiables à cette taille d'échantillon.**
   - À n = 200 et 5 % de fausses alertes observées, l'intervalle de Wilson à 95 % vaut environ [2,7 % ; 9,0 %] (calcul).
   - « ≤ 5 % » ne s'établit qu'avec une borne supérieure sous 5 %, donc avec plus de cas ou un taux observé plus bas.

9. **Les « 200 cas à contraste connu » risquent la circularité.** S'ils sont produits en sollicitant les mêmes modèles, ou jugés par la même famille de juge, l'instrument est validé sur la distribution qui l'a construit.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **R** : mêmes conditions de Fieller qu'en A(b).
- **Trois graines.**
  - Si τ² (variance entre entraînements) domine, l'intervalle ne repose que sur 2 degrés de liberté.
  - Le quantile t à 0,975 pour 2 degrés de liberté vaut environ 4,30, contre 1,96 : les intervalles s'élargissent d'un facteur d'environ 2,2 (calcul).
- **F (capitulation factuelle).** Si la justesse sans fausse croyance est proche de 1 ou proche du taux de hasard, l'excès d'erreur dû à la croyance est écrasé au plancher ou au plafond : la double différence perd sa variance.
- **S (sycophancie sociale).**
  - Si l'accord entre annotateurs (ou entre juge et humains) est faible, la double différence est atténuée d'un facteur proche de la fiabilité.
  - Avec une fiabilité inconnue, le seuil de +5 points n'a pas de puissance définie.
- **g.**
  - Mêmes conditions qu'en A(b) : Var(v₀) tend vers 0, ou Var(Δ | v₀) devient indépendant de v₀.
  - D prévoit lui-même d'opposer le modèle d'attraction au déplacement constant, et c'est juste.
  - Si les estimations par item et par graine reposent sur 5 tirages, l'atténuation par erreurs sur v₀ varie avec la dispersion propre à chaque modèle.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Croyance de l'utilisateur correcte** dans F. Sans elle, une baisse générale de justesse et une déférence à l'utilisateur produisent le même signal. E l'a prévue, D non.
2. **Témoin apparié en divergence KL**, en remplacement du simple appariement en pas.
3. **Dose nulle avec v₀ estimé sur échantillon disjoint**, pour E3. D a la dose nulle, mais pas la disjonction.
4. **Test-retest d'un point de contrôle non modifié.**

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Candidates B et C : le terme d'avant-RL manque.**
   - D est défini comme S_Loving,après − S_base,après. D_social n'est lu qu'après RL.
   - Or la question posée est : la chaleur persistante « **conserve**-t-elle son coût ? ». Y répondre exige de comparer avant et après RL.
   - Un D ≥ 5 points peut être créé par le RL comme hérité de la persona. Les deux candidates ne testent donc pas la persistance qu'elles nomment.

2. **Candidate B : le domaine du RL fuit dans celui de l'évaluation.**
   - Le RLVR porte sur des problèmes arithmétiques générés. L'évaluation porte sur 300 problèmes à réponse calculable.
   - Le RL améliore directement la compétence évaluée. L'erreur, avec ou sans fausse croyance, se rapproche de 0 dans les deux bras.
   - S est alors comprimé au plancher, et D < +5 devient probable **par construction** : H_B gagnerait sans rien dire de la sycophancie.

3. **Candidate A : un G_avant faible et un plafond menacent l'arbitrage.**
   - Sur des situations de soutien, une base Instruct est probablement déjà chaleureuse (HYPOTHÈSE). Avec une annotation binaire, W tend vers 1 dans les deux bras.
   - E prévoit l'arrêt si G_avant n'est pas « nettement positif », et c'est juste. Mais aucun critère n'est fixé : le seuil d'arrêt devient un degré de liberté de l'analyste.

4. **Candidate A : le contrôle négatif est ambigu.**
   - Que *Loving* manifeste de la chaleur sur des questions factuelles relève de la généralisation de la persona, pas d'un confondant.
   - Il faut fixer d'avance quelle issue de ce contrôle invaliderait la mesure. Sinon il ne contrôle rien.

5. **Candidate C : la fiabilité de la vérité terrain n'est pas établie.**
   - La frontière « validation justifiée / injustifiée » est fixée par des annotateurs.
   - Pour un construit voisin, un expert isolé a une fiabilité de 0,184 en corrélation intraclasse, contre 0,960 pour la moyenne des experts (pièce Ibrahim §1.2). Le transfert de ce chiffre à l'annotation de sorties est une HYPOTHÈSE.
   - Si la valeur s'en approche, la formule de Spearman-Brown donne environ 0,53 pour 5 annotateurs, et il en faut environ 18 pour atteindre 0,8 (calcul).
   - « Annotation humaine aveugle » sans nombre d'annotateurs laisse donc la mesure non jugeable.

6. **L'aveugle n'est que partiel.** L'annotation de chaleur ne peut pas être aveugle au style, puisque le style est la signature de la persona. Elle peut seulement l'être à l'identité du modèle et au moment de la mesure, à condition de mélanger les lots avant et après RL. E ne le précise pas.

7. **Validation (c) à n = 100 par construit.** À 5 % de fausses alertes observées, l'intervalle de Wilson vaut environ [2,2 % ; 11,2 %] (calcul). Les seuils « ≤ 5 % » ne peuvent donc pas être établis, comme en D(a)8.

8. **Volume d'annotation humaine non chiffré.**
   - La seule candidate A représente 300 situations × 2 modèles × 2 moments × 3 graines, soit 3 600 jugements, avant toute réplication (calcul).
   - Le budget est « à établir ». La faisabilité de l'expérience retenue n'est donc pas démontrée.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **R (candidate A).**
  - Conditions de Fieller comme en A(b).
  - Avec W binaire, Var(Ĝ) = Σ p(1 − p)/n tend vers 0 près du plafond, mais G aussi. Le rapport signal sur bruit de G_avant décroît, et l'intervalle de R devient non borné.
- **Règle « intervalle à cheval → indécis ».** Elle est correcte, mais aucune taille d'échantillon n'est calculée pour rendre l'issue indécise improbable. Sous l'attendu R = 0,80 contre un seuil de 0,70, l'écart à résoudre vaut 0,10.
- **Graines.** Intervalles regroupés par entraînement avec trois graines : mêmes 2 degrés de liberté et même facteur d'environ 2,2 qu'en D(b) (calcul).
- **D (candidate B).** Si la justesse après RL sans fausse croyance tend vers 1, S tend vers 0 dans les deux bras et D perd toute variance : non jugeable.
- **D_social (candidate C).** Une fiabilité basse atténue l'effet observé d'environ le facteur de fiabilité. Le seuil de +5 points n'a pas de puissance définie tant qu'elle n'est pas mesurée.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Mesure avant RL dans les candidates B et C** : sans elle, aucune conclusion de persistance n'est possible.
2. **Jeu factuel hors du domaine arithmétique**, pour la candidate B. C'est le seul moyen de séparer le gain de compétence de la déférence.
3. **Test-retest d'un point de contrôle non modifié**, et **annotation en lots mélangés** avant et après RL.
4. Les deux contrôles qu'E a déjà prévus, source impersonnelle et croyance correcte, sont bons. Je les reprends en le disant, comme référence pour D(c)1.

---

## Ce que j'en reprends, en le disant

- La règle d'E : un intervalle à cheval sur le seuil donne un verdict indécis.
- La dose nulle et la comparaison au modèle à déplacement constant chez D.
- Le témoin d'autodistillation chez A, comme contrôle de l'exposition aux prompts.

Aucune des trois propositions ne règle les quatre points suivants, et je les tiens pour bloquants :

1. L'estimation de v₀ sur des tirages disjoints de ceux qui servent à calculer Δ.
2. L'appariement des bras en divergence mesurée sur les prompts d'évaluation, plutôt qu'en nombre de pas.
3. Le test-retest d'un point de contrôle non modifié.
4. Un nombre de graines d'entraînement suffisant pour estimer τ².

FIN-DE-CELLULE