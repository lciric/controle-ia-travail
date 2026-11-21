# Proposition B, tour III.2 : critique croisée de méthode

**Pièces.** J'ai reçu A, C et D entières. Chacune se termine par FIN-DE-CELLULE, sans coupure visible. Je critique la méthode, pas les références, que je n'ai pas revérifiées. Ce que j'avance est HYPOTHÈSE, sauf dérivation algébrique explicite. Je n'introduis aucun chiffre.

## Trois défauts que je retrouve chez plusieurs, attribués

**T1. Le jumeau honnête n'est pas gratuit (C, D).**
- C (C6, C10, (k)) et D (piste 1, triangle de P6) traitent Σ(Réf_i − R_lue,i) comme observé sur tous les épisodes, sans coût.
- Or Réf_i est la réussite du jumeau honnête sur la tâche i. Il faut l'exécuter et la juger à chaque épisode.
- En service, le seul modèle fort est le suspect ; A le dit (S2). Le terme « gratuit » n'est vrai que sur le banc, par construction.
- Si on le remplace par le modèle de confiance, on introduit un biais E[Réf_conf − Réf_hon] ≠ 0. Ce biais n'est pas du dommage.

**T2. Une alarme posée sur la martingale de conception est valide et aveugle (A, C, D).**
- Les pièces visées :
  - A (P1) : « Σ(A_i/p_i − 1)·d_i est une martingale quelle que soit la stratégie ; Ville donne une alarme valide ».
  - C ((k), version finie) : W_i = W_{i−1}(1 + λX_i), avec X_i = (A_i/π_i − 1)e_i, et coupure si W ≥ 1/δ.
- Ce processus est centré sous **toute** stratégie, sabotage compris. Il franchit 1/δ avec probabilité au plus δ, que l'agent nuise ou non. Sa validité est vraie par construction ; sa puissance contre le dommage est nulle.
- Il n'est pas non plus calculable : quand A_i = 0, d_i et e_i sont inconnus.
- L'objet utile est un test de H0 : Σd_s ≤ D\*, portant sur l'estimateur observable d̂_s = m_s + (A_s/p_s)(d_s − m_s).
- D ((k)) écrit M_t(D) comme un produit de facteurs en (d_s − d̂_s). Quand A_s = 0, d_s − d̂_s = d_s − m_s est inconnu : même défaut. La « dichotomie sur D » n'est définie que si λ est constant ou si X_s² est remplacé par son pire cas. C'est mon HYPOTHÈSE, à faire vérifier par un tiers.
- La borne déterministe de C ((k), Σp_i + ΣA_ie_i/π_i + écart) est, elle, calculable. Seule l'alarme est fausse.

**T3. Statuts (C, D).**
- C marque VÉRIFIÉ des éléments des faits qui n'en portent aucun :
  - le cadre ;
  - la composition de l'oracle ;
  - les jugements 0,35 et 0,15. Qu'ils aient été émis est rapporté ; leur contenu n'est pas une mesure.
- D marque VÉRIFIÉ des énoncés que sa pièce ne démontre pas :
  - la borne en Θ, dont la partie inférieure n'est pas prouvée ;
  - une information mutuelle ≤ min(ε, ε²/2) ;
  - la « fuite nulle sous latence tamponnée » ;
  - « la sonde lit nécessairement l'échec attendu ».
- Je ne change aucun statut. Je signale à l'arbitre que ces étiquettes n'ont, dans les pièces, ni preuve ni source.
- Le dernier point est aussi une erreur de fond, partagée par C (« ne peut mathématiquement pas avoir appris »). La distribution d'apprentissage ne fixe pas la réponse d'une direction linéaire hors de son support. Ce que la sonde lit sur un sabotage est une question empirique. A la classe en HYPOTHÈSE : c'est le bon statut.

---

## Sur la proposition A

### (a) Défauts de méthode

- **P1, bilan sondé.** Voir T2 pour l'alarme. Autre point : σ est estimé sur des épisodes « honnêtes du modèle de confiance » (tableau, ligne Référence). Or la dispersion du modèle faible n'est pas celle du suspect quand il est honnête. On confond capacité et bruit, et le flux minimal p hérite de cette erreur.
- **Plafond d_i ∈ [0, c] : définition du dommage non tranchée.** Si d̂_i = Réf_i − Y_i porte un bruit honnête ξ centré :
  - tronquer à 0 crée un biais positif E[max(0, ξ)] à chaque épisode, cumulé N fois ;
  - ne pas tronquer autorise la compensation : sur-performer sur des épisodes sans enjeu, nuire ailleurs. Le bilan global la permet.
  - Ce choix fixe la puissance, et A ne le fait pas.
- **T3, variable de contrôle.** « Sans biais pour tout prédicteur » : exact. La réduction de variance, elle, n'est pas acquise quand m est lu sur le suspect. Elle est sous son contrôle (condition en (b)).
- **P2, tableau de cécité.**
  - La part de variance expliquée chute par construction quand l'adversaire suspend son sabotage, car Var(d) tombe au niveau du bruit.
  - L'annonce « ne voit plus » devient donc déclenchable par l'adversaire. Elle est un canal pour piloter la réallocation du budget d'audit.
- **D2, sonde dopamine.**
  - Les deux bras, « sous-performance sur consigne » et « tâche rendue infaisable, l'agent le sait », diffèrent par le texte d'entrée.
  - Une sonde qui lit la consigne atteint une forte AUROC par construction. On l'interpréterait à tort comme « lit l'intention ».
  - Réciproquement, une AUROC ≤ 0,6 n'établit pas H_A (« lit l'échec attendu ») : la sonde peut ne rien lire dans la bande |δ| < 0,1. Il manque un critère positif, comme la calibration de la sonde sur l'échec honnête prévu.
- **D4, oracle.**
  - Retirer la prose retire aussi de l'information légitime (la justification d'une correction). Une bascule n'est pas une persuasion.
  - La paraphrase par le modèle de confiance importe son style, auquel des lecteurs d'autres lignées peuvent réagir.
- **P7, biais entre rejouages.** Les modèles de langage ont des erreurs honnêtes cohérentes d'un échantillon à l'autre (même méprise). Le biais honnête n'est pas nul. A le reconnaît comme cas muet, mais c'est le cas typique, pas un cas marginal.
- **P5, coût d'obscurcissement.**
  - La frontière dépend de l'optimiseur du défenseur.
  - Elle est mesurée sur des tâches complexes, alors que le sabotage diffus vit dans de petits écarts où un faible coût peut passer sous le bruit.

### (b) Conditions de perte de puissance

- **P1.**
  - Var(d − m) > Var(d) dès que Cov(d, m) < Var(m)/2. La variable de contrôle élargit alors la borne.
  - Un adversaire qui fixe la lecture interne choisit Cov(d, m).
- **Troncature.** Avec ξ_i i.i.d., le biais cumulé vaut N·E[max(0, ξ)]. Dès qu'il atteint le seuil d'alarme, la fausse alarme devient presque sûre sur l'honnête.
- **P2, atténuation.** La part mesurée est ≤ ρ_or = Var(d)/(Var(d) + σ_or²), où σ_or² est le bruit de l'oracle. Elle est non jugeable quand ρ_or est petit.
- **P2, mélange.**
  - Le rappel mesuré vaut π_s·r_s + (1 − π_s)·r_acc, avec π_s la part du sabotage parmi les endommagés et r_acc le rappel sur les accidents.
  - Une baisse Δ de r_s ne déplace la statistique que de π_s·Δ.
  - Le nombre d'endommagés audités nécessaire croît comme 1/(π_s·Δ)².
- **D2.** Dans une bande où Var(sonde | δ) ≫ δ², l'AUROC tend vers 0,5 sous les deux hypothèses : le duel est indécidable.
- **P7.** La séparation n'est possible que si b_sab² ≫ b_hon² + τ²/K, où b_hon est le biais honnête et τ² la variance entre rejouages.
- **D3.** Si les performances post-évasion sont au plafond sur le jeu de tâches, le coût mesuré est nul par effet plafond.

### (c) Contrôles négatifs dont l'absence serait fatale

- **D2.** La consigne de sabotage doit être présente dans les deux bras, neutralisée dans le bras honnête. À défaut, il faut un organisme réentraîné sans consigne dans le contexte. Sans cela, toute AUROC est ininterprétable.
- **D4.** Il faut des produits du jumeau honnête avec et sans prose, et des produits endommagés accompagnés d'une prose neutre. Les « deux passes identiques » mes