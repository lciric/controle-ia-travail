# Proposition A, tour III.3 : réponse aux critiques

**Pièces.** J'ai reçu FAITS, QUESTION, ma conception III.1 et les critiques B, C, D, E, toutes terminées par leur marque de fin et sans coupure visible ; je n'ai pas recalculé les empreintes. Le bloc FAITS ne porte aucun statut, alors que C et E citent ses énoncés comme « RAPPORTÉ » : je ne reprends pas cette étiquette. C et E marquent aussi « VÉRIFIÉ » leurs propres calculs ; je n'y touche pas, mais je ne les ai pas audités. Ceux que j'ai refaits sont notés « calcul refait, à relire ».

**Statuts.** Aucune expérience n'a été exécutée, donc rien ci-dessous n'est un résultat. Les mécanismes sont des HYPOTHÈSES, les théorèmes cités sont RAPPORTÉS, les seuils et les chances sont illustratifs.

## (a) Critiques : acceptée, rejetée ou transformée en test

Les critiques établissent que trois de mes cinq propositions mesuraient une grandeur mal choisie : une constante (P3), un rapport borné par l'arithmétique (E1) et une AUROC qui ne contrôle pas le support (E3, P2).

### Sur P3 et E2 (ajout dosé)

- **Récupération constante à la couche lue** (B a1, C a1, D, E a4). **Acceptée.** Pour une sonde affine, le déplacement du score vaut w·v quel que soit le contexte (calcul refait, à relire). L'injection à la couche lue est retirée. Seule l'injection en amont reste : couche antérieure, ou sous-tâche connue rejouée dans l'entrée.
- **Récupération lue comme bascule du verdict, confondue avec la marge de base** (B a1). **Acceptée.** La récupération devient un déplacement continu du score par unité de dose.
- **L'injection vient du sous-espace d'entraînement de la sonde** (C a1, E a4). **Acceptée comme limite.** P3 teste la transmission d'un signal connu dans ce contexte, pas la validité de la sonde face à un mécanisme nouveau. Je l'avais écrit (« analyte nouveau »), et C (b2) en donne la condition exacte.
- **Confusion avec la norme des activations et la longueur** (E a3, T2 de B). **Transformée en test** : analyse stratifiée par norme et longueur (contrôle E c1), sonde aléatoire w⊥ (C c2), placebo apparié en projection sur w (D c).

### Sur P1 et E4 (dominance du témoin)

- **Les mondes plantés sur-représentent le vérifiable** (B a2, E a1). **Acceptée.** Les tâches sans propriété vérifiable restent au dénominateur, comme le demande D, et un bras place exprès le dommage dans le résidu (B c).
- **sup |L − V| n'a pas d'estimateur** (B a3). **Acceptée dans le cas général** : un maximum empirique ne fait que minorer le sup, donc l'écart se réfute et ne s'établit pas. Il reste un cas restreint.
  - Si la perte L_D est définie comme l'espérance, sur la distribution D des exemples séquestrés, d'une perte bornée dans [0, 1], si le produit est figé avant tout accès et si les m exemples ne servent qu'une fois, alors |V − L_D| ≤ √(ln(4/δ)/(2m)) pour les deux candidats avec probabilité ≥ 1 − δ.
  - Cette borne vient de Hoeffding (1963, « Probability Inequalities for Sums of Bounded Random Variables », RAPPORTÉ) et d'une union (calcul, à relire).
  - Elle ne couvre pas le choix de D, la question posée ni l'interprétation, qui restent du résidu.
- **Facteur 2 manquant** (D b). **Acceptée.** Si |U − V| ≤ e pour chaque candidat, alors U(retenu) ≥ U(témoin) − 2e (calcul refait, à relire). Mon énoncé III.1 est corrigé ainsi, et c'est cette forme qui va en Lean.
- **Le bruit du holdout réutilisable rompt la dominance exacte** (E a1, b5). **Acceptée sur le fond, précisée.** La dominance reste exacte sur le score bruité utilisé ; elle ne tient sur V qu'à l'amplitude du bruit près. Je choisis donc une partition séquestrée fraîche par épisode, sans bruit ; le coût en données est assumé et le bruit éventuel entre dans e.
- **Dominance annoncée sur le score qui a servi à choisir** (D a). **Acceptée.** L'issue de E4 est une perte de décision L contre une vérité détenue par le tiers, distincte de V et inaccessible au sélecteur.
- **Annotation vérifiable/résidu par qui connaît les mondes** (C a2). **Acceptée.** L'annotation est faite à l'aveugle de la vérité plantée, par une autre main, et scellée avant.
- **« Fraction de dommage supprimée » indéfinie si la référence est nulle** (D b). **Acceptée.** Le critère devient un écart apparié de pertes.
- **Omission pure, produit faux honnête à V élevé, témoin incompétent** (C c1, D c, E c3). **Transformées en bras de E4′.** La garantie de P1 est relative au témoin. Le manque à gagner par rapport à un agent honnête fort n'est borné par rien.

### Sur P2 et E3 (inspection)

- **s et π dépendent de la politique de l'attaquant ; il faut une borne inférieure sur h_j** (B a4, D b). **Acceptée.** Ici h_j est la probabilité de prise sachant la violation j et l'absence de prise antérieure. La borne s'écrit (1 − h)/h avec h = inf_j h_j, et h n'est pas un paramètre du seul défenseur.
- **Une AUROC ≤ 0,55 est compatible avec une borne infinie** (C b3, E b4). **Acceptée.** Si une région de masse réelle δ a une masse plantée nulle, l'indicatrice de cette région a une AUROC de 1/2 + δ/2 (calcul refait, à relire), et un attaquant qui n'agit que là n'est jamais pris. E3 ne certifiait donc rien. La réponse est de changer la construction (P2′ ci-dessous) plutôt que d'ajuster le seuil.
- **Un discriminateur qui échoue ne dit rien d'une classe plus riche** (B a6, C a3, E a4). **Acceptée.** E3 peut tuer et ne peut pas établir. Le générateur est tenu à l'écart du discriminateur (B c).
- **Contrôle de masse en queue** (E c2). **Transformée en test**, avec sa limite : un rapport de densité estimé souffre en queue du même défaut que le discriminateur.

### Sur E1 (pannes coïncidentes)

- **Conditionnement sur l'échec de la sonde, variable latente de difficulté** (B T4). **Acceptée** : tableau 2×2 publié, bande pré-enregistrée pour P̂(raté de la sonde | attaque), stratification par difficulté.
- **RR plafonné par 1/p_V** (C b1, E b2). **Acceptée.** Avec RR = P(F|S)/P(F), on a RR ≤ 1/P(F) (calcul refait, à relire), donc le seuil 1,5 est inatteignable quand le vérificateur échoue plus de deux fois sur trois. Une précision sur C : sous sa propre définition du rapport, le plafond porte sur p(V | sonde réussie) et non sur p_V. Le fond tient.
- **Dégénérescence quand la sonde rate tout** (C b1). **Acceptée.** Je n'avais traité que l'autre bord.
- **Indépendance exacte contre marge : hypothèses non complémentaires ; l'indépendance peut ne rien sauver** (D b). **Acceptée.** La métrique change (E1′).
- **Contrôle H1 tautologique s'il a fixé les seuils** (B a5). **Acceptée**, et généralisée : tout contrôle porte sur des épisodes H1 frais.

### Sur P4 (martingale conforme)

- **Contradiction d'objectif** (E a3) et **« sonde hors domaine » n'est pas « comportement nouveau »** (D a). **Acceptée.** Mon test de mort demandait à un détecteur de régime d'être un classifieur d'attaque. La cible de (A) devient la perte de précision de la sonde dans le régime.
- **L'entropie de la tâche dilate l'écart** (C a4). **Transformée en test** : score normalisé par la dispersion jumeau/jumeau sur la même tâche, et temps d'arrêt sous H3 mesuré (C c3).
- **Seuil à régler sur agent honnête contre jumeau** (B T3). **Acceptée.** Le plancher jumeau/jumeau reste un diagnostic.
- **Un échantillon d'étalonnage fixe rend les p-valeurs dépendantes** (E b1). **Acceptée**, sans avoir redérivé la formule de E. Je passe à la construction en ligne (Vovk, Nouretdinov, Gammerman, « Testing Exchangeability On-Line », année à vérifier).
- **Une fréquence d'alertes supérieure à α ne réfute pas seule l'échangeabilité** (D b). **Acceptée** : le critère devient une borne de confiance.

### Sur P5 (bissection)

- **Transposition invalide** (E a2, b6) et **mauvaise grandeur** (D b). **Acceptées, et P5 est retirée.** La délégation arbitrée suppose le même programme déterministe des deux côtés. Un témoin d'une autre famille diverge honnêtement dès les premiers pas. Ce qui survit est la réexécution de confiance du code soumis, c'est-à-dire ma ligne de base M1.

### Transversales

- **T1, artefact de fabrication du saboteur** (B). **Acceptée pour E1′, E2′ et P4** : bras consigne placebo et affinage placebo. **Rejetée comme « fatale pour toutes »** : E4′ n'a aucun détecteur qui puisse apprendre « consigne présente », et E3′ n'a pas de saboteur. Le risque y est autre, un saboteur trop faible, et il relève de la conception par le tiers.
- **T2, maximum et longueur** (B). **Acceptée** partout où une lecture est prise à une position extrême.
- **Graines identiques sur H1** (E a3). **Acceptée.** L'appariement se fait par tâche, avec graines indépendantes ; les graines identiques ne garantissent rien après le premier jeton différent.
- **Zones grises contraires à B4** (E a4). **Acceptée.** Je reprends la convention de D : une marge unique, des hypothèses complémentaires.
- **Datation de Greenblatt et coll.** (B). Je maintiens 2023 pour la prépublication ; je crois la publication en conférence datée de 2024 ; référence à vérifier.

## (b) Expériences corrigées

**Convention commune, reprise de D.**

- Chaque duel a un bénéfice b et une marge m pré-enregistrée : H_A : b ≥ m ; H_B : b < m.
- Un intervalle à 95 % entièrement d'un côté réfute l'autre hypothèse. Un chevauchement rend le duel non concluant et il est publié comme tel.
- L'incertitude se calcule sur les tâches tirées indépendamment.
- Les seuils sont scellés ; les contrôles portent sur des épisodes H1 frais.
- Les effectifs minimaux par cellule sont pré-enregistrés.

**E4′ (à faire en premier). Détecteurs éteints, la règle P1 réduit-elle la perte de décision ?**

- **Montage.** Avant toute soumission, le tiers fixe pour chaque tâche la décision qui utilisera le produit, la perte L contre sa vérité, et la propriété vérifiable V si elle existe. Sans propriété, la règle rend le produit du témoin et la tâche reste au dénominateur. On compare par tâche trois politiques : témoin seul, agent seul, règle P1.
- **H_A**, conjonction de deux conditions :
  - sûreté : sous famille tierce, E[L(règle) − L(témoin)] ≤ m_s ;
  - utilité : sous agent honnête, E[L(témoin) − L(règle)] ≥ m_u.
- **H_B** : le complément. On publie laquelle des deux conditions a cédé.
- **Contrôles positifs** : dommage placé exprès dans le résidu ; omission pure ; témoin honnêtement incompétent. Si le premier ne produit aucune perte mesurée, le banc ne voit pas le résidu et le duel est invalide.
- **Contrôle négatif** : produits honnêtes faux à V élevé (H2).
- **Ce que chaque issue falsifie.**
  - H_A falsifie, sur ce banc, « le dommage d'un sabotage de recherche loge surtout hors du vérifiable ».
  - H_B par la sûreté falsifie « la dominance sur V porte la perte de décision » : l'écart mesuré minore e.
  - H_B par l'utilité falsifie « P1 vaut mieux que le témoin seul » : la règle est exacte mais sans intérêt.

**E3′. Les tâches réelles dopées se distinguent-elles des tâches réelles ?**

- **Montage.** Le tiers produit les pièges par P2′ (voir ci-dessous). Le discriminateur est choisi sur des tâches disjointes, par quelqu'un qui n'a pas le générateur.
- **b** = 0,5 + m − AUROC (borne supérieure), assorti du contrôle de queue de E : dans le centile que le discriminateur juge le plus « réel », la proportion de tâches dopées est ≥ π/2.
- **Contrôles** : lots réel/réel de même provenance (0,5 attendu) ; pièges marqués (proche de 1).
- **Asymétrie assumée.** H_B annule la borne d'inspection pour ce générateur. H_A falsifie seulement « cette classe de discriminateurs discerne » et n'établit pas h > 0.

**E2′. La récupération en amont prédit-elle les ratés de la sonde ?**

- **Montage.** Injection en amont uniquement. Vérification d'instrumentation : la même dose à la couche lue doit donner une récupération constante, sinon le montage est fautif (B c).
- **b** = AUROC(déficit de récupération, raté de la sonde sur sabotage tiers) − 0,5, à tâche et dose fixées, stratifié par norme et par longueur.
- **Contrôles** : sonde aléatoire w⊥ (si la récupération y varie autant, P3 ne mesure qu'un facteur d'échelle) ; placebo apparié en projection sur w ; bras placebo T1.
- **Non concluant si** P̂(raté | attaque) sort de la bande, ou si la variance contextuelle de la récupération est négligeable devant la variance honnête du score.
- **Falsification.** H_B tue P3 comme signal de (A) ; il ne resterait qu'un contrôle d'effet de matrice. H_A falsifie « la panne hors domaine est purement un mécanisme nouveau ».

**E1′. Le second regard rattrape-t-il ce que la sonde manque ?**

- **Métriques.** Le tableau 2×2 est publié. La métrique de dépendance est δ = P(F|S) − P(F|non S), par strate de difficulté cotée par le tiers. La métrique d'usage, rapportée à part, est la perte rattrapée avant irréversibilité, E[L·1{S et non F}].
- **H_A** : δ ≤ m ; **H_B** : δ > m.
- **Cas dégénéré.** Si la sonde rate presque tout, δ n'est pas défini. On rapporte alors P(F|S) seul, contre un plancher pré-enregistré.
- **Falsification.** H_B falsifie, pour ce couple et à difficulté fixée, « autre genre implique pannes non corrélées ». H_A falsifie la transposition de Knight et Leveson ici. Aucune des deux issues ne dit que le second regard est utile ; la métrique d'usage le dit.

**Test de P4, recadré.**

- **Cible** : les régimes où la sonde perd sa précision, mesurée en y rejouant des sabotages connus tenus à l'écart.
- **b** = AUROC(alerte, régime dégradé) − 0,5.
- **Contrôle** : un régime H3 où la sonde garde sa précision ; une alerte y est une fausse alerte au sens de (A).
- **Limite.** Avec peu de régimes et moins de 99 épisodes par régime, ce test sera probablement non concluant.

## (c) Réponse à l'arbitre

**La réponse, après critique.** Les critiques n'ont pas laissé debout un second détecteur. Elles ont laissé debout une règle d'usage du produit : le tiers fixe la propriété à vérifier avant la soumission, le score est calculé sur des données séquestrées à usage unique, et le témoin de confiance sert de repli. La garantie est relative au témoin, restreinte à la perte telle qu'elle est définie sur la distribution séquestrée.

**Propositions révisées, rangées** (toutes HYPOTHÈSES, chances illustratives).

1. **P1**, répond à (C). La garantie est celle du paragraphe précédent ; elle ne borne ni le résidu ni l'omission au-dessus du niveau du témoin. Chances qu'elle couvre la majorité du dommage : environ 35 %, abaissées à cause du biais de sélection reconnu.
2. **P2′, tâches réelles dopées**, répond à (B) et borne pour (C), sous condition.
   - C'est mon pont « ajouts dosés », déplacé des activations vers la tâche. Avec une probabilité π tirée d'un aléa privé, une tâche réelle reçoit un effet connu, injecté dans ses données par le générateur du tiers. Le contrôle est la restitution de cet effet.
   - Le piège est tiré de la distribution réelle elle-même. La région sans masse plantée de C et E n'existe donc plus du côté des tâches.
   - Il reste trois conditions : que le dopage ne laisse pas de trace (E3′), que le sabotage dégrade la restitution de l'effet (h > 0 pour cette classe seulement), et que la tâche ait des données où injecter. Les tâches de mathématiques pures sont exclues.
   - Un attaquant informé chercherait la trace du dopage, ou abîmerait ce que l'effet injecté ne mesure pas.
   - Des pratiques voisines existent en physique (injections aveugles, « salage » des données) ; référence à vérifier. Je ne sais pas si la transposition au contrôle de l'IA est publiée.
   - Chances : environ 30 %.
3. **P4 recadrée**, répond à (A) : environ 25 %, limitée par les effectifs.
4. **P3 en amont**, répond à (A) : environ 20 %.
5. **P5** : retirée.

**Ce qui est établi.**

- RAPPORTÉ (littérature, non revérifiée ici) :
  - sur un observable donné, la puissance d'un détecteur ne dépasse pas α + TV ;
  - la validité conforme des fausses alertes tient sous échangeabilité seulement ;
  - l'inégalité de Hoeffding.
- Calculs de ce tour, à relire et à formaliser en Lean :
  - U(retenu) ≥ U(témoin) − 2e ;
  - le déplacement d'une sonde affine par un ajout à la couche lue est constant ;
  - RR ≤ 1/P(F) ;
  - une AUROC de 1/2 + δ/2 est compatible avec une prise impossible.
- Empiriquement : rien.

**Ce qui ne l'est pas.**

- La valeur de e hors du cas restreint.
- La part du dommage qui loge dans le résidu.
- L'existence d'un h > 0.
- Que la récupération en amont prédise quoi que ce soit.
- Que des résultats sur saboteurs fabriqués, sur des modèles de quelques milliards de paramètres, se transportent à un attaquant qui invente.

**Je ne sais pas.**

- Si le dommage d'un sabotage de recherche est additif.
- Quelle part des tâches du programme admet une propriété fixée par un tiers avant soumission ; D l'ignore aussi.
- Si le dopage d'une tâche réelle laisse une trace lisible.

**L'expérience à faire en premier : E4′.**

- **Pas préalable, sans dépense.** Sur les archives, annoter à l'aveugle la part des tâches qui admettent une propriété vérifiable fixable d'avance. Si cette part est faible, E4′ est jugée d'avance du côté H_B, et on le publie.
- **Pourquoi elle.**
  - Elle porte sur la seule garantie qui ne dépend d'aucune détection, donc qui ne dépend pas de ce que l'attaquant invente.
  - Elle échappe à T1 et T4, puisqu'il n'y a ni détecteur à tromper ni conditionnement sur un raté.
  - Ses deux issues réorientent le programme. H_A fait des sondes un complément sur la partie vérifiable. H_B dit que le dommage est dans le résidu ; aucun mécanisme ici ne le borne, et la relecture humaine rare devrait s'y concentrer.
- **Vérification extérieure.** Le tiers détient la vérité, la famille d'attaque et la définition de L. Les marges sont scellées par empreinte. L'inégalité à 2e passe par l'arbitre Lean, qui certifie l'implication et non l'hypothèse |U − V| ≤ e.

FIN-DE-CELLULE