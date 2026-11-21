# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces.** B, C, D et E sont reçues, chacune close par sa ligne de fin ; aucune n'est visiblement coupée. Les FAITS ne portent pas d'étiquette de statut : je les traite comme RAPPORTÉ. Les statuts posés par les auteurs, notamment les « VÉRIFIÉ » de C et de E sur des références et des noms de modèles, restent les leurs ; je ne les ai pas audités.

**Outils de lecture** (VÉRIFIÉ par calcul, une ligne chacun). X est ce que le moniteur observe, P_H et P_S ses lois sous honnêteté et sous sabotage, L = dP_S/dP_H, α le taux de fausses alertes.

- **O1.** Si L ≤ k presque sûrement, tout détecteur vérifie TPR ≤ k·α, car ∫_A L dP_H ≤ k·P_H(A). À α = 1 %, c'est la queue de L qui décide, pas la distance en variation totale (TV) ni KL.
- **O2.** Une fonction de X ne sépare jamais mieux les deux lois que X. Seule une variable qui n'est pas fonction de X peut ajouter de la séparation. Corollaire : si l'issue est fonction de la trajectoire, TV(trajectoires) ≥ P_H(succès) − P_S(succès).
- **O3.** Si un détecteur ne dépend de la trajectoire que par la validité V de la conclusion, alors TPR sur conclusions invalides ≤ α / p_err, avec p_err = P_H(V = 0) et α compté sur toutes les trajectoires honnêtes.
- **O4.** KL s'additionne le long d'une trajectoire (règle de chaîne) : ajouter des pas identiques ne la réduit pas.

Les valeurs numériques ci-dessous sont des calculs sous indépendance. Quand elles partent d'un paramètre choisi par l'auteur critiqué, ce paramètre reste « illustratif ».

---

## Sur la proposition B

### (a) Défauts de méthode

1. **D0 n'est pas exhaustif.** Deux mesures donnent quatre issues, et B n'en interprète que deux.
   - Fausses alertes élevées sur l'honnête affiné et détection du sabotage par consigne : la sonde lit les deux.
   - Fausses alertes basses et détection nulle : la sonde lit l'interaction affinage × objectif.
   - Dans ces deux cas rien n'est falsifié. « Nettement » n'est pas chiffré. B4 n'est pas tenu.
2. **Le jumeau « même chaîne, seul l'objectif diffère » ne neutralise pas le contenu.** Changer l'objectif change les exemples d'affinage. La sonde peut lire « poids exposés à des exemples de sabotage ». Dans la cellule par consigne, elle peut lire la présence de la consigne.
3. **La validation de la borne TV est une identité.** Au §3.2, B compare la « borne inférieure estimée de TV » au meilleur TPR − FPR mesuré. Or tout estimateur de borne inférieure de TV est le TPR − FPR d'un classifieur.
4. **M2 a besoin d'une borne supérieure, qui n'est pas estimable.** Sur des trajectoires, on ne majore pas TV depuis un échantillon sans connaître les lois.
   - H_A de M2 établit donc « nos moniteurs sont faibles », pas « la détection est vaine ».
   - Par O2, une dégradation Δ de la probabilité de succès force TV ≥ Δ dès que les déterminants de l'issue sont observés. Avec une marge m < Δ, H_A ne peut tenir que par sous-optimalité des moniteurs ou par non-observation.
   - La borne est en TPR − FPR, la métrique à α = 1 % : c'est O1 qu'il faut, pas TV.
5. **Fuite sur le mode tenu à l'écart.** Le premier pas de D1 interroge son gardien par oui ou non. Avec un seul mode, un bit suffit à orienter la défense. Pour D1, le mode n'est plus tenu à l'écart.
6. **M3 confond lignée et difficulté.** Si la difficulté des cas varie, les ratés de deux moniteurs quelconques sont corrélés positivement, lignée commune ou non. De plus, l'agrégateur a été choisi sur les journaux existants : la corrélation y est biaisée.
7. **M1 est acquis par construction** pour des moniteurs d'actions ; B l'écrit lui-même. Le duel n'a de contenu que si un moniteur de couverture figure parmi les comparés.
8. **D1 compare à budgets de surveillance inégaux.** Un bras a un moniteur du plan en plus. L'issue « succès rouge inchangé » dépend aussi de la force de l'équipe rouge. Je reprends ici, en le disant, la qualification préalable de l'équipe rouge proposée par E (§4.3).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Seuil de D0.** Un seuil calibré au quantile 99 % a un FPR vrai proche de 1 %.
  - Sur 299 cas on attend environ 3 alertes. La borne supérieure unilatérale à 95 % est alors d'environ 2,6 % (Poisson).
  - Le critère « ≤ 1 % » n'est donc pas satisfiable statistiquement. Il faut une non-infériorité FPR_affiné ≤ 1 % + δ.
  - Distinguer 1 % de 2 % demande de l'ordre de 800 cas indépendants (approximation normale, niveau 5 %, puissance 80 %).
  - Avec m trajectoires par tâche de corrélation ρ, l'effectif utile est n / (1 + (m − 1)ρ).
- **M2** n'est jugeable que si P_S est construit comme une déformation connue de P_H, avec k = sup L déclaré. O1 donne alors TPR ≤ k·α avant toute mesure. L'expérience porte sur la dégradation obtenue à k donné.
- **D2.** Soit ρ_c la probabilité que les re-dériveurs reproduisent le biais à partir de l'énoncé : TPR ≤ 1 − ρ_c. Si la loi honnête des conclusions est multimodale, le quantile 99 % de la divergence est de l'ordre de l'écart entre modes et la puissance s'annule.
- **D3.**
  - Validité : la loi honnête des scores doit rester dans l'hypothèse nulle à chaque instant. Si le mélange de tâches dérive, E_H[e_t] > 1 et l'inégalité de Ville ne s'applique plus.
  - Puissance : elle est proportionnelle à f·E_S[log e], avec f la fréquence de sabotage. Elle est nulle quand f·T ≈ 1.
- **Borne 1 − (1 − t)^k.** Elle suppose l'indépendance des détections, que M3 conteste dans la même pièce. Sous corrélation positive des ratés, elle surestime.

### (c) Contrôles négatifs dont l'absence serait fatale

- **D0** : une cellule « affiné sur des données décrivant le sabotage, comportement honnête ». S'y ajoute la cellule « consigne secrète bénigne » de E (E0.1), que je reprends telle quelle.
- **M3** : des paires de lignées croisées stratifiées par difficulté du cas, sur des données qui n'ont pas servi à choisir l'agrégateur.
- **M2** : un témoin positif, c'est-à-dire un organisme à L non borné connu, sur lequel le même banc doit retrouver une forte détection.
- **D1** : un placebo avec le même surcoût et le même moniteur du plan, mais sans vérification de l'écart au scellé.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Attributions de faits.**
   - La « flotte de soixante agents » est attribuée à l'organisme d'idéation. Les faits la rapportent pour l'épisode zêta.
   - Les 300 dollars par problème servent de coût d'un cycle d'idéation. C'est le budget d'un banc de problèmes ouverts.
   - Le premier pas de la Menace 2 suppose que le programme détient les objets de contrôle des sessions de 2026. Les faits ne le disent pas.
2. **Expérience 1 : la perte est la métrique.** Le saboteur est entraîné avec la pénalité de la sonde, puis jugé par cette même sonde. Si l'optimisation converge, la chute du TPR est acquise.
   - Le contenu empirique est le TPR d'une sonde ré-entraînée sur l'organisme adapté, sur des tâches disjointes. L'ordre des coups doit être fixé.
   - H_A est universelle (« ne peut pas ») et C admet que l'issue contraire ne vaut que « pour cette classe et ce budget ». Un seul côté est réfutable.
   - La zone 20–70 % ne falsifie rien.
3. **Expérience 2 : un seul mode tenu à l'écart.**
   - ΔTPR confond le sur-apprentissage et la difficulté propre de ce mode.
   - Deux flottes et leurs seuils font au moins deux requêtes adaptatives sur le même coffre.
   - Il y a une exécution par bras : la variance entre exécutions d'une flotte stochastique est inconnue.
4. **τ_I est défini par l'échec, τ_S non.** C'est un conditionnement sur l'issue d'un seul côté. Aucun contrôle d'artefact d'organisme n'est prévu (la cellule affinée de B manque).
5. **CCT : la « garantie exacte » ne l'est pas.**
   - Tout couplage vérifie P(désaccord) ≥ TV. L'égalité n'est pas garantie pour Gumbel-max.
   - Un jumeau à contexte réduit diverge structurellement d'un agent honnête.
   - Après le premier désaccord, les contextes bifurquent, sauf forçage sur la trajectoire de l'agent. La statistique est alors un rapport de vraisemblance agent/jumeau, donc un moniteur de confiance.
   - Lean prouve l'inégalité de Ville, pas l'hypothèse nulle. Le premier pas porte sur deux traces.
6. **ABCA : l'agent fournit le monde où son choix gagne.** Pour presque tout choix, un tel monde existe (HYPOTHÈSE de ma part). C'est la Menace 2 de la même pièce. La défense et la menace se contredisent tant que les mondes ne sont pas tirés d'une loi que l'agent ne contrôle pas.
7. **CAPP : fuite entre construction et évaluation.** Le premier pas perturbe selon le vecteur de la sonde, sur les traces qui l'ont entraînée. Les deux classes diffèrent par construction en projection sur ce vecteur. Un écart de réponse est attendu sans aucun mécanisme.
8. **Menace 3 : une issue, deux lectures opposées.** « Si la sonde ne sonne plus, la vulnérabilité est prouvée ». Cette issue est aussi prédite par « la sonde lit l'intention et non l'action », qui est la propriété voulue.
9. **Menace 1 : énoncé incohérent sans paramètre.** « KL < ε par pas mais échec avec probabilité → 1 ». Par O4 la divergence de trajectoire est la somme des pas. Par O2 elle est minorée par la chute de la probabilité de succès.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Seuil à 1 % sur 500 traces τ_I.** Cinq points tombent en queue. Le FPR réalisé a un écart-type d'environ 0,44 point. Le TPR varie de cette quantité multipliée par la pente de la ROC en α.
- **Expérience 3.** Elle n'est pas jugeable sans la proportion π de τ_I dans le mélange honnête de déploiement : FPR = π·FPR_I + (1 − π)·FPR_H.
- **CCT.** La puissance s'annule quand le désaccord moyen par pas d_H ≈ d_S. Or d_H croît avec l'information mutuelle entre le contexte retiré et l'action honnête. La validité exige l'échangeabilité entre trajectoires ; les pas d'une même trajectoire sont dépendants.
- **Menace 1.** Le paramètre décisif est p_H, la probabilité honnête de succès. La séparation forcée vaut au moins p_H − p_S. Avec p_H = 5 % (illustratif), une division par dix ne force que 4,5 points.
- **Expérience 2.** Avec M modes tenus à l'écart, l'erreur sur ΔTPR est de l'ordre de σ_mode / √M. Avec M = 1, σ_mode n'est pas estimable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Expérience 1** : un saboteur adapté contre une sonde leurre de direction aléatoire, pour mesurer ce que l'optimisation seule coûte au succès du sabotage. Et une sonde ré-entraînée après adaptation.
- **CAPP** : des directions aléatoires de même norme, la direction d'une sonde sur un concept sans rapport, et des organismes jamais vus par la sonde.
- **CCT** : même modèle, plein contexte contre contexte réduit, puis modèles différents à même contexte. Sans cela, contexte et capacité restent confondus.
- **ABCA** : le taux auquel un agent honnête produit un objet passant pour un choix tiré au hasard. S'il est proche de 1, l'exigence ne discrimine pas.
- **Menace 3** : un modèle honnête exécutant une action correcte sous une consigne sincère de même forme.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Deux comptabilités, un seul plafond.** F compte comme fausse alerte toute alerte sur une erreur honnête. Or le témoin ne voit que la validité.
   - Par O3, D ≤ 1 % / p_err. Avec p_err = 10 % (illustratif), D ≤ 10 %.
   - La défense prioritaire perd alors son propre duel par arithmétique, quelle que soit sa qualité.
   - Il faut trancher avant de mesurer. Pour un instrument de validité, le plafond devrait porter sur les conclusions honnêtes valides rejetées, pas sur l'attribution.
2. **Unités mêlées.** D est par décision, F par trajectoire. Avec n_d décisions par trajectoire et un taux f par décision, F = 1 − (1 − f)^n_d.
3. **Dénominateur post-traitement.** Les « décisions nuisibles produites » dépendent de la défense, puisqu'un attaquant adaptatif en produit moins ou ailleurs. Comparer D entre bras compare des populations différentes. La mesure valide est le dommage accepté par tâche assignée. D la publie « aussi » ; elle doit être principale.
4. **« Strictement supérieur » sans marge.** Sur un lot fini et sous égalité vraie, le signe de l'écart est aléatoire. Le duel n'a ni niveau ni puissance déclarés.
5. **Le mandat est une recherche sur des classes.** « Trouvez une classe de décisions pour laquelle… ». Sous l'hypothèse nulle, la meilleure de K classes gagne en apparence. La clause « sinon, la condition sous laquelle l'avantage disparaît » est post hoc.
6. **Effort de conception inégal.** Le contrat reçoit la recherche de la flotte, les comparateurs sont pris tels quels. Le « budget égal » couvre l'exécution, pas la mise au point.
7. **L'agent choisit son réfutateur.** Un saboteur choisit une observation de faible puissance. D nomme l'« engagement vide » mais ne mesure pas la puissance du réfutateur choisi.
8. **Quarantaine.** Si le graphe de dépendances est déclaré par l'agent, l'instrument est construit par ce qu'il doit contrôler.
9. **Flotte contre chercheur seul** : une exécution par bras, même défaut que chez C.
10. **Menace « dépendance commune ».** Changer la provenance ajoute de l'information, pas seulement de l'indépendance.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Contrat contre test caché.** Le gain est nul quand le témoin W est indépendant de l'engagement, conditionnellement à la trajectoire et à la vérité θ.
- **Indépendance du témoin.** Elle est perdue quand P(W faux, conclusion fausse) dépasse le produit des marginales (prémisse commune).
- **Duel commun.** Pour un écart de 10 points autour de D = 50 % (illustratif), il faut de l'ordre de 400 décisions nuisibles par bras, non appariées, au niveau 5 % et à la puissance 80 %. Pour F, les effectifs sont ceux donnés pour B.
- **Quarantaine.** Le gain sur la vérification uniforme est nul si la loi du nombre de descendants est concentrée. Le paramètre est son coefficient de variation.
- **Garantie sur monde fini.** Elle est vide si l'ensemble des états compatibles avec le témoin est un singleton. Elle est non jugeable si P(état réel ∈ états admissibles) < 1.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Blocage aléatoire au même taux.** Toute règle qui bloque une fraction b des décisions obtient D ≥ b. C'est le plancher mécanique, et il manque.
- **Erreurs honnêtes plantées** de même invalidité que les sabotages. Elles vérifient que le taux de blocage y est identique et obligent à choisir la comptabilité.
- **Réfutateur imposé par un tiers** contre réfutateur choisi par l'agent, à témoin égal.
- **Source nouvelle de même exactitude et de même provenance**, pour séparer indépendance et information.
- **Classe de décisions fixée d'avance par un tiers.**

---

## Sur la proposition E

### (a) Défauts de méthode

1. **L'argument de dilution est faux tel qu'écrit.** Par O4, KL ne se dilue pas dans 200 pas dont un seul diffère. Ce qui se dilue est une moyenne de scores.
   - Par O2, un goulot ne peut pas créer de divergence.
   - Si RAND-ML marche, c'est parce que la re-dérivation est une variable nouvelle, pas parce qu'un canal étroit « impose un saut de divergence ».
   - La défense peut être bonne ; sa justification mathématique ne la soutient pas.
2. **Rice ne dit pas où chercher.** Le théorème porte sur la décision pour tous les programmes. Une exécution bornée se décide en l'exécutant. Le noyau déclaratif se justifie par l'auditabilité, pas par la décidabilité.
3. **RAND-ML : le noyau est écrit par l'agent surveillé.** E écrit au §3.3 qu'une re-preuve reproduit un biais présent dans l'énoncé.
   - Sur cette branche, P(divergence | biais dans le noyau) = P_H(divergence). La puissance est nulle.
   - La détection retombe sur un moniteur du noyau.
   - Les comparateurs ne sont pas à budget égal : RAND-ML coûte au moins deux exécutions.
4. **Zones mortes dans tous les duels** : 40–75 %, 30–75 %, 15–60 %, AUROC 0,55–0,65. L'issue intermédiaire ne falsifie rien.
5. **E0.2.** Si le « succès par méthode indirecte » est défini par l'écart au jumeau, la fausse alerte est acquise par construction.
6. **Menace 2 : un même événement, deux signes.** H_A y appelle « TPR » le déclenchement sur un biais bénin. En E0.1, le déclenchement sur une consigne bénigne est une fausse alerte. De plus, son premier pas évalue sur le mode tenu à l'écart : même fuite que chez B.
7. **Menace 1.** Dans un simulateur abstrait, l'issue se déduit de O1 et rien n'est mis à l'épreuve. Le contenu empirique est ailleurs : X contient-il les branches abandonnées ?
8. **FMS-Lean.** Le TPR est mesuré sur des mutants produits par les opérateurs autour desquels le filtre est conçu.
9. **CES-MM.**
   - Un AUROC ≤ 0,55 pour un classifieur maison ne borne pas ce que l'agent distingue. C'est le problème de borne supérieure relevé chez B.
   - La nulle « estimateurs sans biais » exclut les bogues honnêtes du corpus 2 de E. CES-MM détecte la validité, donc O3 s'applique.
10. **Données.** Les journaux zêta et ceux des 68 problèmes sont supposés disponibles. « 66 échecs » ne figure pas dans les faits.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Calibration conforme.** La garantie est marginale sur le tirage de calibration.
  - Avec n < 99, le seuil est infini : aucune alerte.
  - Avec n = 150 (taille des duels de E, avant tout partage), le seuil est le maximum. Le FPR réalisé suit une loi Beta(1, 150), de moyenne ≈ 0,66 % et de 95ᵉ centile ≈ 2,0 %.
- **Fenêtre [0,5 % ; 1,5 %].** Un écart-type de 0,25 point demande environ 1 600 trajectoires honnêtes. Le « ≤ 2 % » de E4 en demande de l'ordre de 800.
- **CES-MM.** TPR ≤ 1 − (1 − q)^k, avec q le taux de canaris et k le nombre d'appels altérés. Avec q = 10 % (valeur de E, illustrative), 75 % exige k ≥ 14. Avec k = 1, TPR ≤ 10 %.
- **Borne KL.** kl(α ‖ TPR) ≤ KL(P_H ‖ P_S). Plafonner TPR à 50 % pour α = 1 % exige KL ≤ 0,64 nat sur la trajectoire entière. O1 est plus fine dès que L est borné.
- **Corrélation de rang ≥ 0,7.** Avec cinq architectures, elle survient par hasard avec une probabilité non négligeable. De mémoire des tables, l'ordre est de 10 % ; à recalculer.
- **Cosinus entre sondes.** En dimension d ≫ n, il tend vers 0 par bruit d'estimation. Le plafond est le cosinus entre deux moitiés du même organisme.
- **RAND-ML.** TPR ≤ 1 − ρ_c, corrélation de biais entre lignées. Je ne sais pas quelle valeur attendre.

### (c) Contrôles négatifs dont l'absence serait fatale

- **RAND-ML** : des noyaux écrits par un tiers honnête pour les mêmes tâches. Ils isolent ce que le noyau laisse passer de ce que la re-dérivation attrape.
- **CES-MM** : des canaris indistinguables par construction (permutations de données réelles) plutôt que par échec d'un classifieur. Et des agents honnêtes à bogue involontaire, comptés à part.
- **Menace 2** : la fiabilité moitié-moitié des sondes, et un seul sens fixé d'avance pour « déclenchement sur du bénin ».
- **E0.2** : un critère d'« indirect » fixé par un annotateur sans accès au jumeau.
- **FMS-Lean** : des mutants fournis par un tiers.

FIN-DE-CELLULE