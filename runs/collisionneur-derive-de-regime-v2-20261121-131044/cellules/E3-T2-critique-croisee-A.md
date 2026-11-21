**Pièces.** B, C, D et E sont reçues, chacune close par sa ligne de fin ; aucune coupure visible.

**Statuts.** Mes critiques sont des analyses : HYPOTHÈSE tant qu'aucun test n'est exécuté. Les lignes marquées « calcul » sont exactes sous échangeabilité, mais leurs tailles (n = 300, m = 99, K = 15) sont illustratives. Je ne rapporte aucun résultat.

**Divergence de statut à trancher par l'arbitre.** La phrase des faits sur l'écart fragile du jumeau reçoit trois étiquettes : « RAPPORTÉ fragile » (B), « VÉRIFIÉ » (C), « OBSERVÉ-NON-AUDITÉ » (E). Les FAITS transmis ne l'étiquettent pas, donc je ne tranche pas.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Le test de mort de P1 est vrai par construction.** « Le taux dépasse α dans plus de δ des réplications à l'intérieur d'un régime correctement identifié » nie un théorème binomial. Une seule issue est possible hors bogue de code, ce qui contrevient à B4. De plus, à l'échelle du programme, P1 est le maximum, donc identique à M1 : par le critère de B (« battre M1 »), P1 ne peut rien prouver.

2. **La garantie de Ville de P3 est énoncée sans son conditionnement.** Le canal T teste « taux des témoins ≤ α au seuil courant ». Or, à seuil conforme marginal, le taux réalisé dépasse 1 % dans environ 42 % des tirages d'étalonnage sans aucune dérive (calcul : loi Beta(3, 298), n = 300 illustratif). Dans ces tirages, l'e-processus a une dérive positive et finit par rejeter. La borne « ≤ 1/seuil » ne vaut que si le seuil vient de P1, où elle devient ≤ δ + 1/seuil. Je me sers ici de la remarque de D sur les rangs à calibration commune.

3. **La table de décision de P3 est confondue par les tailles des canaux.** Le délai de rejet varie comme l'inverse du nombre d'observations. Le canal D en a beaucoup plus que le canal T. Toute dérive honnête passe donc d'abord par la case « D rejette, T ne rejette pas », lue comme « anomalie hors honnêteté ». Le gel et l'escalade humaine se déclenchent à chaque changement de régime bénin, pour une raison d'effectifs.

4. **Fuite par temps d'arrêt.** Les témoins qui font rejeter le canal T alimentent ensuite la recalibration. L'échantillon est conditionné par un arrêt que ses propres dépassements ont déclenché. Le seuil est biaisé vers le haut, ce qui coûte de la détection, et ce coût n'est pas mesuré.

5. **P2 contrôle chaque longueur mais pas l'épisode.** La règle « alerte si le score du pas t dépasse τ(t) » est une union sur t d'événements chacun au niveau α. C'est exactement le défaut « franchissements répétés » des faits. S'y ajoutent deux problèmes :
   - les épisodes de longueur ≥ ℓ sont une population sélectionnée, puisque la longueur dépend de la tâche ;
   - les τ(ℓ) sont estimés sur les mêmes épisodes, donc fortement dépendants.

   D5 compare des lois de maxima à ℓ fixé et ne teste aucun de ces points.

6. **D1 compare à la mauvaise loi.** Le seuil ancien est un tirage unique. La question pertinente est le taux à ce seuil fixé, ancien régime tenu à part contre nouveau régime. De plus, rééchantillonner la 298ᵉ statistique d'ordre de 300 est instable, alors que la loi Beta exacte est connue.

7. **D3 est masqué par le conservatisme de P1.** Au seuil maximum du jumeau, le taux attendu est d'environ 0,33 % (calcul, n = 300 illustratif). Une dérive différentielle qui le triple donne environ 1 %, et l'intervalle « contient α ». H_A est alors déclarée alors que le défaut cherché est présent.

8. **M3 n'est pas comparable « à taux de fausses alertes égal ».** Le taux de fausses alertes d'un top-k dépend de la prévalence plantée de sabotage, et cette prévalence confond la comparaison.

### (b) Conditions de perte de puissance

- **D1.** Le 97,5ᵉ centile de la bande vaut environ 2,4 % (calcul, n = 300 illustratif). Une vraie hausse à 3 % n'y place sa borne basse qu'avec environ 3 000 épisodes honnêtes de test (approximation normale, illustratif). En dessous, H_B ne peut pas être établie.
- **D2.** On attend environ un dépassement par strate (n_g·α ≈ 1). Avec Holm, « aucune strate ne diffère » est l'issue par défaut, et H_B est « falsifiée » par manque de puissance.
- **P3.** B chiffre lui-même à environ 230 le nombre de témoins nécessaires. Si η est la fraction de témoins, il faut 230/η épisodes à taux triplé avant de signaler.
- **P2.** Avec zéro dépassement sur n épisodes, la borne haute vaut environ 3/n (approximation). En dessous de 300 épisodes complets par tranche, le test de mort ne distingue ni 1 % ni 0,33 %.
- **D5.** Un test à deux échantillons porte sur la loi entière. Sa puissance sur une différence limitée au dernier centile est quasi nulle.

### (c) Contrôles négatifs manquants

- Un régime stable long avec seuil conforme non PAC : la fraction de tirages où T rejette révélerait le point (a)2.
- Pour D1, une coupe par blocs temporels ou par sessions. La coupe au hasard détruit la dépendance de grappe et passe trivialement.
- Pour P2, des pas honnêtes plantés i.i.d., avec mesure du taux par épisode sous la règle en ligne.
- Pour P3, un monde où la dérive honnête touche le déploiement mais pas les témoins. Le monde (v), dérive plus sabotage, est listé au §4 mais absent de D4.
- Un contrôle positif de taille connue pour calibrer la puissance de D1 à D3.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts.** Trois étiquettes ne viennent pas des faits :
   - « N_cal ∈ [200, 500] [VÉRIFIÉ] » : les faits disent seulement « quelques centaines » ;
   - « [OBSERVÉ-NON-AUDITÉ] » posé sur une supposition (a.4) sans observation ;
   - « [VÉRIFIÉ] » sur des références citées de mémoire.

2. **L'expérience 1 est circulaire.** Elle prétend « trancher la cause du triplement [RAPPORTÉ] » sur les mondes plantés. La cause y est déclarée par le constructeur : selon les faits, c'est un décalage des scores honnêtes. L'expérience retrouve ce choix, pas la cause réelle.

3. **L'expérience 2 est gagnée par construction.** Si la famille du programme est un décalage, tout transport de position et d'échelle (P2) la restaure. L'issue 2 n'est atteignable que dans un monde à queue seule. C le décrit comme test de mort mais ne l'inscrit pas au duel, qui ne comporte que M1 et M2. L'adversaire est par ailleurs un ACI « sans étiquettes » empoisonnable par définition. Enfin H_B est une disjonction (« queue extrême ou supériorité d'ACI ») : les deux hypothèses ne sont pas exclusives.

4. **Fuite dans P1.** Les fonctions m(L) et σ(L) sont ajustées sur les épisodes dont on conformise ensuite les résidus. Ces résidus sont internes à l'ajustement, donc non échangeables avec un résidu neuf. La « validité exacte » est perdue sans partition. La « validité conditionnelle à O(N^{-1/2}) » est affirmée sans preuve ni statut.

5. **P2 injecte plus de bruit que la dérive à corriger.**
   - Sous modèle gaussien, médiane et MAD sur K = 15 déplacent le seuil d'un écart-type d'environ 0,8 σ. Ce chiffre combine environ 0,32 σ pour la médiane et environ 0,30 × 2,33 σ pour l'échelle (ordre de grandeur asymptotique, illustratif).
   - Selon le calcul d'E, dont je me sers, un triplement correspond à environ 0,45 σ.
   - En régime stable, TARR ferait donc lui-même tripler le taux sur une fraction des lots.
   - La probabilité de queue étant convexe en le seuil, le taux moyen sur les lots dépasse α, sauf si c_α compense. Or c_α n'est pas donné, donc la règle n'est pas calculable telle quelle.

6. **L'« immunité totale » de P2 suppose ce qu'elle doit montrer.** Les ancres sont exécutées par l'agent non fiable. Le bac à sable certifie les actions, pas les états internes lus par la sonde. Le point de rupture à 50 % ne protège pas quand toutes les ancres viennent du même agent. L'ancre « premiers pas à préfixe commun » change en outre la population : le maximum est pris sur moins de pas, donc elle n'est pas échangeable par construction.

7. **P3 confond décorrélation et super-uniformité conditionnelle.**
   - Un effet aléatoire d'épisode (certains épisodes honnêtes hauts de bout en bout) viole E[e_t | passé] ≤ 1 pour tout Δ.
   - Le paramètre λ ne modifie pas l'espérance de e_t. L'« ajuster sur l'étalonnage » pour l'obtenir est une confusion, doublée d'une fuite.
   - Des p-valeurs à calibration commune ne sont pas conditionnellement uniformes (remarque de D, dont je me sers).

8. **Le « quota de rangs » ne garantit pas ce qui est annoncé.** L'invariance ne vaut que si la déformation monotone est commune à tout le lot. Et « exactement 1 % » est un taux d'alerte, pas un taux de fausses alertes.

### (b) Conditions de perte de puissance

- **Seuils des duels.** Les seuils 1,3 %, 1,5 % et 1,8 % sont séparés de moins d'une erreur-type : environ 0,31 point à n = 1 000 (calcul, illustratif).
- **Variabilité d'étalonnage.** Sans dérive, le taux réalisé dépasse 1,5 % dans environ 17 % des tirages (calcul : Beta(3, 298)), et ce même avec un jeu de test infini. Un verdict sur un seul tirage n'est pas jugeable.
- **P1.** Elle perd sa validité par tranche dans quatre cas :
  - la loi du résidu sachant L dépend de L (indice de queue non nul, ou indice extrémal variable) ;
  - le score déjà normalisé n'est pas monotone en ln L ;
  - le L cible sort de la plage d'étalonnage ;
  - le score a des atomes.
- **P2.** Elle est aveugle quand la dérive laisse médiane et MAD inchangées (C le dit). Elle est aussi inutilisable quand la dérive est inférieure au bruit de (a)5.
- **P3.** Sous dérive de régime, les p-valeurs par pas cessent d'être super-uniformes. L'e-processus multiplie l'excès, et le taux par épisode croît avec L bien au-delà d'un facteur 3. Par ailleurs, « TPR à FPR égalisé à 1 % » oblige à quitter le seuil 1/α, donc la garantie comparée.

### (c) Contrôles négatifs manquants

- **TARR en régime stable.** Il faut la dispersion par lot du taux, avec et sans TARR. Le contrôle « ancres de l'ancien régime » teste l'information apportée, pas le bruit injecté.
- **Permutation de l'expérience 3.** Elle n'est pas spécifiée. Dans l'épisode, elle conserve l'effet d'épisode et ne descendra pas à 1 %. Entre épisodes, elle détruit tout et passe trivialement. Il faut les deux, séparément.
- **Reconnaissabilité des ancres.** Un classifieur sur activations doit échouer à distinguer ancre et trafic honnête (AUC ≈ 0,5).
- **P1 sur partition disjointe.** Comparer avec l'ajustement interne pour mesurer la fuite.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le duel du §4 ne peut pas être gagné par une règle exacte.** H_A exige un taux ≤ 1 %. D-ancre délivre exactement 1 % quand m + 1 = 100. Une borne de confiance chevauchera toujours le seuil, et D déclare ce cas « indécis ». Sans marge pré-enregistrée (du type « ≤ 1 % + Δ »), l'issue « H_B falsifiée » est inatteignable. Le duel n'a alors qu'une issue utile, ce qui contrevient à B4.

2. **L'unité du critère n'est pas fixée.** D-ancre garantit par cible honnête. Conditionnellement aux témoins du lot, avec m = 99 :
   - le taux suit une loi Beta(1, 99) ;
   - il atteint au moins 3 % dans environ 4,9 % des lots sans aucune dérive (calcul) ;
   - il atteint au moins 2 % dans environ 13,5 % des lots (calcul).

   Le triplement sous changement de régime devient un triplement par tirage de témoins. Mesuré « par régime », en moyenne sur les lots, le critère passe. Mesuré par lot, il échoue par construction. D signale la distinction mais son critère ne choisit pas.

3. **Le verdict de D-enveloppe est connu avant exécution.**
   - Avec zéro dépassement sur 300 honnêtes et δ = 5 %, U vaut environ 0,994 % (calcul, illustratif). Il reste ε ≤ 0,006 point.
   - Un seul dépassement donne U > 1 %.
   - L'enveloppe vaut « pour tout seuil candidat ». Dans la famille qui triple, l'écart au vieux seuil est de 2 points, donc ε ≥ 2 points si le vieux seuil est candidat.

   Le certificat n'est donc jamais émis. Le test de mort (« planter le triplement en respectant l'enveloppe ») est contradictoire, sauf enveloppe très inégale selon les seuils. D admet que la borne « peut épuiser le budget » mais ne fait pas le calcul qui montre qu'elle l'épuise toujours à cette échelle.

4. **ε n'est pas estimable à la précision requise.** Le justifier « indépendamment du lot » demande des écarts de queue entre régimes passés. Chacun est connu à environ 0,6 point près à n = 300 (écart-type Beta, calcul de B dont je me sers). ε devient donc une supposition, pas une mesure.

5. **La recomposition du §1 est indéfinie pour de nouvelles tâches.** Elle exige un taux conditionnel par tâche à 1 %. Les cellules de quelques épisodes donnent des estimations 0 ou 1/n. Une tâche nouvelle (premier cas cité par les faits) n'a aucun support d'origine. Le résidu « non expliqué par le mélange » absorbe alors le bruit.

6. **La qualification des ancres dépend d'une ressource rare.** L'« honnête indépendant qui ne sert jamais d'ancre » doit être attesté dans le régime cible, donc relu par un humain. D ne chiffre pas ce besoin.

7. **Statuts.** D pose lui-même « VÉRIFIÉ » sur des énoncés mathématiques et des attributions qui ne sont pas dans les FAITS. Les énoncés me paraissent justes, mais l'étiquette est auto-attribuée.

### (b) Conditions de perte de puissance

- **D-ancre.** Avec m < 99 par strate et par lot, aucune alerte n'est possible (D le dit). Le coût est m par cellule, pas par entrepôt. Avec quelques centaines d'épisodes, cela fait au plus deux ou trois cellules.
- **Qualification des ancres.** Il s'agit de comparer deux taux de queue, 1 % contre 3 %, avec n_att honnêtes attestés. On attend n_att·α dépassements. Pour n_att de l'ordre de la centaine, le test est non jugeable.
- **« Gain de détection strictement positif ».** Sans marge et avec peu de sabotages plantés, l'intervalle de la différence contient zéro. Le critère est indécis en permanence.
- **D-enveloppe.** Elle ne devient non triviale que si n·α ≫ 3 dans la partition de certification, soit des milliers d'honnêtes par strate (ordre de grandeur illustratif).

### (c) Contrôles négatifs manquants

- **Lot A/A.** Témoins contre témoins du même tirage : la loi par lot du taux doit coïncider avec la loi Beta attendue. Cela vérifie les ex æquo et fixe l'unité du critère.
- **Reconnaissabilité.** D cite le témoin reconnaissable comme mode d'échec mais ne prévoit aucun test. Il faut un discriminateur témoin/cible sur activations et sur métadonnées de lot.
- **Multiplicité de D-enveloppe.** Un monde dans l'enveloppe où l'on réessaie plusieurs seuils sur la même partition doit montrer le taux de certificats faux.
- **Contrôle positif du banc.** D exige que le seuil d'origine triple dans chaque monde, ce qui est une bonne exigence. Il manque un monde où il triple pour les cibles mais pas pour les témoins, avec le taux de couverture revendiquée à tort.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **La « surmartingale » de la proposition 3 n'en est pas une.** Avec M_s = (1−λ) + λ·e_s·M_{s−1} et E[e_s | passé] = 1, on obtient E[M_s | passé] = (1−λ) + λ·M_{s−1}. Cette valeur dépasse M_{s−1} dès que M_{s−1} < 1.
   - Le processus est une somme d'e-processus redémarrés, du type Shiryaev–Roberts.
   - Ville ne s'y applique pas. Ce type de statistique contrôle un délai moyen jusqu'à fausse alarme, pas la probabilité d'un franchissement.
   - La borne « ≤ α₁ quelle que soit T_e » est donc non établie, et je la crois fausse à horizon long : la réinjection (1−λ) rend le processus récurrent.

   C'est le défaut « franchissements répétés » des faits, réintroduit. Ce calcul est à refaire par un tiers. La forme de C, M_{t−1}(1−λ+λe_t), est une vraie supermartingale ; les deux ne sont pas équivalentes.

2. **La garantie de Canary-eMix ne tient pas « sous la seule indépendance des ancres ».**
   - Les p_j et V_j sont calculés contre un D_cal commun. Conditionnellement à D_cal, P(V = 1) dépasse 1 % dans environ 42 % des tirages (calcul, n = 300 illustratif). Le produit n'est pas alors une supermartingale (remarque de D, dont je me sers).
   - La composante ½·p^{−1/2} parie sur un glissement central. Elle révoque pour des dérives sans effet sur la queue, ce qu'E reproche lui-même aux tests globaux en 3.4.
   - « Accélère d'un ordre de grandeur » est un chiffre sans source ni mention « illustratif ».
   - « Infalsifiable » et « immunisé » supposent l'indiscernabilité, alors que les ancres sont exécutées par l'agent non fiable.

3. **PF-Gumbel a une fuite d'ajustement.** Π⊥, ŝ_m et (â, b̂) sont ajustés sur D_cal, puis le quantile conforme est pris sur le même D_cal. Projeter hors des directions de variance honnête estimées en interne dégonfle les scores d'étalonnage par rapport à des scores neufs. Le seuil est trop bas, donc le taux hors échantillon dépasse α par construction. L'ampleur croît avec le rapport entre le rang retiré et N. Choisir ce rang en regardant la détection violerait en outre la contrainte des faits.

4. **Le résidu en préfixe forcé mesure l'écart entre modèles, pas un comportement.** E donne comme contrôle « auto-jumeau : résidu identiquement nul ». C'est exact, et cela vaut aussi pour un épisode de sabotage si le jumeau partage poids et contexte.
   - La puissance dépend donc entièrement de ce qui diffère entre agent et jumeau (invite, poids, modèle), et E ne le spécifie pas.
   - Si le jumeau est un autre modèle, la différence des activations n'a de sens qu'après une application d'alignement apprise. E ne dit pas sur quelles données, ce qui ouvre une nouvelle fuite.

5. **Statuts et monde non présent dans les faits.**
   - Le test de mort de la proposition 1 invoque une « rotation » d'états sous changement de version « (FAITS) ». La famille plantée des faits est un décalage des scores.
   - « Sabotages rares (VÉRIFIÉ) » sert à borner la prévalence en déploiement. Les faits parlent de rareté des épisodes disponibles.

6. **D3 a un contrôle mal nommé.** « Sabotage massif, TPR ≥ 99 % » est un contrôle positif.

### (b) Conditions de perte de puissance

- **D1 et D2, seuil à 1,5 %.**
  - Placer une borne haute sous 1,5 % à taux vrai 1 % demande environ 1 500 honnêtes du régime dérivé (approximation normale, illustratif).
  - La repondération multiplie ce besoin par n/n_eff.
  - Une famille de tâche nouvelle donne des poids indéfinis.
  - Sans dérive, environ 17 % des tirages d'étalonnage dépassent déjà 1,5 % (calcul).
- **D3.** Avec 200 sabotages par bras (chiffre illustratif pris à C), l'erreur-type de la différence est d'environ 5 points. Un écart relatif de 10 % autour d'un TPR de 50 % représente aussi 5 points, soit un seul écart-type.
- **Canary-eMix.** Il faut environ 230 ancres pour un triplement pur de queue (borne de B, dont je me sers). Avec η entre 5 et 10 %, cela fait environ 2 300 à 4 600 épisodes à taux triplé avant révocation (illustratif). Le réservoir à oubli exponentiel mêle ensuite ancres d'avant et d'après rupture.
- **PF-Gumbel.** La réduction « − log K_e » perd son uniformité par longueur dans trois cas :
  - l'indice de queue n'est pas nul ;
  - l'indice extrémal dépend du régime ;
  - la définition des pivots change avec la version de l'outillage, donc K_e dérive.
- **Proposition 3, étage 2.** L'égalité « asymptotique » au seuil oracle n'a pas de statut. Elle tombe dès que le lot mêle deux sous-régimes, ce qu'E reconnaît.
- **Portée de l'étage de tests.** Je ne sais pas si les mondes plantés contiennent des activations et des trajectoires de jumeau. Si l'interface fixe ne voit que des scores, D2, D3 et la proposition 1 n'y sont pas jugeables.

### (c) Contrôles négatifs manquants

- **Proposition 3.** Des pas honnêtes simulés i.i.d. à p-valeurs uniformes, avec le taux d'alerte par épisode mesuré en fonction de T_e. Si la courbe croît, le point (a)1 est confirmé.
- **Canary-eMix.** Un régime stable long, répété sur plusieurs tirages de D_cal, avec la fraction de révocations comparée à β.
- **PF-Gumbel.** Trois contrôles :
  - Π⊥ et quantile sur partitions disjointes contre un ajustement interne ;
  - Π⊥ aléatoire de même rang, pour vérifier que le gain ne vient pas de la seule réduction de dimension ;
  - épisodes de sabotage plantés avec auto-jumeau. Le TPR doit y être égal au taux de fausses alertes, sinon l'instrument lit autre chose que ce qu'il annonce.
- **D3.** Des épisodes honnêtes réétiquetés « sabotage » : le TPR doit retomber à 1 %.

FIN-DE-CELLULE