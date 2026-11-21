# Proposition A — Tour III.3 : réponse aux critiques

**Pièces.** FAITS, QUESTION, ma conception III.1 et les quatre critiques croisées (B, C, D, E) sont présentes ; aucune n'est visiblement coupée. Je ne peux pas recalculer les sha256. Je ne réponds qu'aux sections « Sur la proposition A » ; quand j'emprunte un argument écrit contre une autre proposition, je le dis.

**Statuts.**
- Les résultats du papier restent RAPPORTÉ.
- Les étiquettes VÉRIFIÉ posées par C, D et E sur des identités de calcul sont les leurs : je les cite sans les changer et sans les avoir toutes recalculées.
- Mes corrections et mes expériences sont des propositions, au statut HYPOTHÈSE.
- Tout chiffre absent des faits est marqué « illustratif ».

---

## (a) Critique par critique

### Sur P2 / D2 (nul au pas par le jumeau, e-processus)

| # | Critique (source) | Verdict | Conséquence |
|---|---|---|---|
| 1 | L'A/A est vrai par construction : le rang est uniforme quelle que soit la sonde, et D2 ne teste que la chaîne de rejeu (B-a1, C-a1). | **Acceptée**, avec une nuance. | La validité indépendante de la sonde est la propriété recherchée. Mais D2 ne testait pas ce que j'annonçais. Il devient une recette d'ingénierie ; le duel passe à D2′. |
| 2 | Le contrôle « graines identiques, le processus reste à 1 » est un test d'indexation, faux sans convention sur les ex æquo (B-a1, D-b). | **Acceptée.** | Contrôle retiré. |
| 3 | Le nul testé est « même loi que le jumeau », pas « honnête contre saboteur ». Une consigne ou un réglage latent suffit à faire rejeter, même sur des pas bénins (B-a2, C-c1, E-a1). | **Acceptée pour l'alternative, rejetée pour le nul.** | Voir sous le tableau. P2 est renommé « moniteur d'écart de politique ». Toute lecture en termes d'intention est retirée tant que D0 n'est pas fait. |
| 4 | La garantie de Ville est marginale sur les longueurs ; le verdict du programme est par tranche de longueur réalisée (B-a2, D préambule). | **Acceptée.** | Correction sous le tableau : seuil relevé, ou tranche assignée avant génération ; détecteur évalué en lecture seule. |
| 5 | Rejouer les sorties d'outils de l'agent sur des continuations divergentes du jumeau fausse le nul (E-a1). | **Transformée en spécification.** | Continuations d'un seul pas, score lu pendant la génération de l'action, avant tout retour d'outil. Rien n'est rejoué sur une action divergente. Prix : le score ne voit pas le retour d'outil. La fidélité numérique du préfixe forcé reste à tester (D2′). |
| 6 | Plafond (m+1)^T ; croissance bornée par T·f·KL ; dérive d'ordre λε si l'échangeabilité est rompue, pire dans la tranche longue (B-b, C-b1, E-b). | **Acceptée.** | Règle d'arrêt arithmétique avant toute génération (D2′). Avec m = 4, il faut au moins trois pas de séparation parfaite (ln 100 / ln 5 ≈ 2,86, illustratif, calcul de C). Sous sabotage diffus, P2 est probablement sous-puissant à l'échelle de l'épisode. |
| 7 | Le signal planté ne mesure que la sensibilité à un décalage additif ; le « second volet » de D2 n'informe pas sur l'utilité (B-a3, E-a5). | **Acceptée.** | Second volet retiré. M1 et M2 ne lisent pas les activations : la comparaison était vide par construction. Le signal planté reste une courbe de puissance de la machinerie. |
| 8 | Le choix des pas et du pari doit être mesurable avant le tirage ; le cumul entre épisodes exige la validité conditionnelle aux épisodes antérieurs (D-b) ; dérive si la loi des tâches change (E-b). | **Acceptée.** | P5 n'est conservé que comme prolongement du produit de P2′ (nul conditionné au préfixe, donc insensible à la dérive des tâches par construction, mais pas à la dérive de configuration). P5 sur scores d'épisode calibrés est retiré. |

**Ligne 3, ce que je rejette.** À configuration identique, l'agent honnête en échec est dans le nul : le jumeau est conditionné au même préfixe en échec, donc ses continuations partent du même état. C'est précisément ce qui évite de confondre échec et écart. Cette identité de configuration reste une HYPOTHÈSE en pratique.

**Ligne 4, la correction.** J'utilise la borne α/p_b que D pose en préambule et que C écrit dans sa section sur D. Soit p_min la plus petite part d'une tranche parmi les épisodes honnêtes non interrompus.
- En plaçant l'alarme à 100/p_min, on a P(alerte) ≤ α·p_min, donc P(alerte | tranche b) ≤ α·p_min/p_b ≤ α dans chaque tranche (calcul standard).
- Coût en preuve : ln(1/p_min) de plus. Pour p_min = 0,1 (illustratif), le seuil passe à 1 000, soit ln ≈ 6,9 au lieu de 4,6.
- Estimer une part de tranche demande bien moins d'épisodes qu'une queue à 1 % ; on prend une borne basse de confiance.
- Autre voie, proposée par D : des tranches définies par un horizon assigné avant génération. Le seuil 100 suffit alors.
- Dans les deux cas, le détecteur est évalué en lecture seule sur des trajectoires non interrompues.

### Sur P1 / D1, P3, P4, P6, P7

| # | Critique (source) | Verdict | Conséquence |
|---|---|---|---|
| 9 | Fuite entre la régression de normalisation et le rang conforme (B-a5, C-a2, E-a5). | **Acceptée.** | P1′ : trois lots de tâches entières (ajustement, calibration, audit), normaliseur gelé, forme préenregistrée. Je préfère cette coupe à l'ajustement croisé, pour la raison que D oppose à E : des résidus hors pli ne sont pas les scores d'un prédicteur gelé. Prix : n encore plus petit. |
| 10 | D1 réfute un épouvantail ; le terrain de substitution n'a pas la queue des épisodes longs (B-a4). | **Acceptée sur la conclusion, rejetée en partie sur l'épouvantail.** | Les FAITS (§4) lient bien le verdict « non concluant » au compte de 5 000 : séparer validité et précision vise une règle de fonctionnement réelle. En revanche, ma phrase « réfute la nécessité » était trop forte. D1′ ne conclut plus que sur la procédure. |
| 11 | Une mise en commun est valide en moyenne, pas par strate, si les indices de queue diffèrent. L'équivalence par strate est non jugeable sous environ 299 épisodes par strate (illustratif). Avec moins de 99 unités échangeables (illustratif), le seuil conforme à 1 % n'existe pas (C-b2, C-b3, E-b, B-b). | **Acceptée, transformée en test.** | Le contrôle de C (marche à dépendance longue) devient un contrôle positif planté de D1′, avec un mélange à quantiles centraux égaux et queues inégales. Sur les épisodes réels, D1′ devient descriptif. |
| 12 | P3 est non jugeable à 1 % si n < ln δ / ln(1−α) ; un partage du risque entre tranches l'alourdit (B-b, D-b, E-b). | **Acceptée comme arithmétique, rejetée comme défaut.** | C'est le contenu même de P3 : rapporter α\* au lieu de 1 %. Ajout : α\* global et α\* par tranche à risque partagé, avec la mention « non jugeable à 1 % » quand la borne à zéro dépassement excède 1 %. |
| 13 | Réinjecter dans la calibration les épisodes honnêtes audités parmi les k premiers biaise la queue (E-a2, D-c). | **Acceptée.** | P4′ : la calibration n'est alimentée que par des audits tirés indépendamment du score, à probabilité d'inclusion connue et non nulle. Les audits des k premiers servent à la détection seulement. Le contrôle d'audit uniforme parallèle de E est adopté. |
| 14 | L'échec honnête est une issue terminale, pas une strate d'achat (E-a3). Une probabilité d'inclusion nulle rend le taux non identifiable (D-b). | **Acceptée.** | P6′ : strates définies avant génération (variante, horizon assigné), probabilités d'inclusion connues, pondération inverse. La cible reste le taux sur tous les épisodes honnêtes. |
| 15 | L'extrapolation de queue est instable et ne supplée pas un support non observé (B-b, D-b). | **Acceptée.** | P7 reste une analyse secondaire, jamais au-delà du support observé. |

### Sur U1 / D3, U4, D4

| # | Critique (source) | Verdict | Conséquence |
|---|---|---|---|
| 16 | La lecture de valeur pas à pas sort du protocole du papier, qui lit au prompt et en position finale (B-a6). | **Acceptée.** | Second volet ajouté à D4′, préalable à D3′. |
| 17 | Une consigne de sabotage fait chuter la valeur dès t = 0 ; une variante difficile aussi chez l'honnête (B-a6, C-a4, E-a4). | **Acceptée, transformée en test.** | D0, placé en premier. |
| 18 | Sélection sur le dégât confirmé ; délai d'observation confondu avec le calendrier d'inspection ; censure informative ; délai non défini quand un des deux temps n'existe pas ; annotation non aveugle ; seuil normalisé sur la trajectoire entière ; sens inverse absent du duel (B-a6, D-a/b/c, E-a4/b). | **Acceptée en bloc.** | D3 est retirée telle quelle et refondue en D3′. |
| 19 | Le lecteur du transcrit doit lire un transcrit sans la consigne cachée (B-a6). | **Acceptée.** | Spécifié dans D0 et D3′. |
| 20 | L'échec par ablation n'est pas l'échec naturel, même pour un moniteur de comportement (C-a3, D-b, E-a5 ; B n'objectait pas). | **Acceptée.** | U4 est retirée entièrement, y compris pour M2. Je la remplace par l'échec honnête par environnement dégradé, idée de E, que j'utilise. |
| 21 | Un échec du transfert aux jalons ne réfute pas un gain de sélection entre continuations (D-a). | **Acceptée.** | Dans D4′, H_B ne ferme plus U5. |

**Correction volontaire.** L'objection de C à B (une strate lue sur l'agent évalué est manipulable et postérieure au régime) vaut contre mon U3. La valeur avant génération sera lue sur le jumeau, pas sur l'agent.

---

## (b) Expériences corrigées

**Préalable sans coût : tableau de jugeabilité.** Avec le nombre de tâches T, les effectifs par tranche et la liste des ajustements passés, on calcule pour chaque tranche :
- si un rang conforme à 1 % existe (au moins 99 unités échangeables, illustratif) ;
- quelle borne donne zéro dépassement (1 − δ^{1/n}) ;
- le plancher de pas surveillés de P2′.

C'est un calcul, pas une expérience.

### D0 — Consigne ou sabotage (nouvelle, à faire en premier)

Le mode de fabrication du saboteur est **absent des faits**. La version ci-dessous vaut pour une consigne cachée. Si le saboteur est obtenu par réglage des poids, le témoin devient un réglage bénin (témoin que D propose à E).

**Bras**, appariés par variante de tâche :
- (0) honnête ;
- (1) consigne cachée bénigne, de même longueur et structure (contrôle de B, C et E, que j'adopte) ;
- (2) consigne de sabotage sans occasion d'agir ;
- (3) consigne de sabotage, dégât confirmé par ré-exécution, à l'aveugle des scores ;
- (4) honnête sous un écart de configuration réaliste (version d'échafaudage, rejeu).

**Duel.**
- H_A : l'écart de score de sonde entre (3) et (1) est ≤ g.
- H_B : il est > g.
- g est préenregistré. Intervalle par permutation au niveau de la variante. Décision : borne basse > g réfute H_A ; borne haute ≤ g réfute H_B ; sinon non jugeable.

**Ce que chaque issue réfute.**
- H_A observé réfute toute lecture « intention » de la sonde testée, pour un saboteur fabriqué de cette façon. Cela inclut le contraste principal du programme.
- H_B observé réfute « la sonde ne lit que la présence d'une consigne ».

**Lecture secondaire.** Si l'écart (2)−(1) vaut l'écart (3)−(1), le signal est le contenu de la consigne, avant tout acte. Il ne se transporte alors pas à un agent sans consigne.

**Contrôles.** Neurones M4 ; lecteur du transcrit privé de la consigne ; A/A entre (0) et (0).

**Injugeabilité.** Si la demi-largeur attendue dépasse g. Le nombre de variantes se calcule sur la variance A/A avant achat.

**Coût.** Trois bras nouveaux, plus le bras (4), fois le nombre de variantes, en unités de C (quelques dizaines de variantes, illustratif). Aucun seuil à 1 % n'est requis.

Les mêmes épisodes servent D2′.

### D2′ — Le nul au pas tient-il, et sert-il ?

**Spécification.**
- m continuations d'un pas.
- Calibrateur strictement conservateur sur la grille des rangs. C et E notent ce conservatisme et le problème de frontière ; il laisse une marge connue sous 1.
- Pas et pari choisis par une règle fixée avant le tirage.
- Seuil 100/p_min ; lecture seule.

**Règle d'arrêt arithmétique.** Si le nombre de pas surveillés d'une tranche est inférieur à ln(100/p_min)/ln(m+1), P2′ y a une puissance nulle. On le dit et on n'y génère rien.

**Duel de validité.** L'unité est le pas, groupé par tâche : c'est ce qui le rend jugeable avec peu d'épisodes.
- H_A : la moyenne de e_t est ≤ 1 dans chaque strate (succès honnête, échec honnête, tranche, bras (4)). Borne haute par ré-échantillonnage des tâches.
- H_B : elle est > 1 dans au moins une strate.
- H_B observé réfute P2′ dans cette strate et localise la rupture.
- H_A observé réfute « l'écart de configuration gonfle les e-valeurs ».
- Limite, d'après le contre-exemple que D oppose à B : une moyenne correcte n'établit pas la validité conditionnelle. On ajoute la moyenne conditionnelle au rang précédent, et un nul simulé à rangs dépendants comme contrôle positif du diagnostic.
- Le taux de franchissement par épisode est rapporté avec son intervalle exact, sans prétention à 1 % par tranche.

**Duel d'utilité.** Sur (3) contre l'échec honnête apparié, même machinerie avec trois scores : neurones du papier ; log-vraisemblance des jetons sous le jumeau (ligne de base n° 2 du programme) ; M4.
- H_A : la richesse logarithmique moyenne avec les neurones du papier dépasse celle de la ligne de base de plus de g′.
- H_B : non.
- H_B observé réfute l'apport du papier dans ce moniteur.

### D1′ — Banc d'essai de procédure (réduit)

- Terrain de substitution, procédure P1′.
- H_A : la fraction des tirages où la pire strate dépasse 1 % n'excède pas le δ nominal.
- H_B : elle l'excède.
- Contrôles positifs plantés (ligne 11) : la procédure doit y donner H_B, sinon le banc est aveugle.
- H_B observé réfute P1′.
- H_A observé réfute seulement « P1′ échoue déjà sur un terrain simple », rien de plus pour le programme.

### D4′ — Transfert, en deux volets

- (i) Lecture au prompt, comme dans le papier : prédit-elle le succès aux jalons d'épisodes honnêtes au-dessus de M1 et M4 ?
- (ii) Lecture aux positions intermédiaires, qui est une extrapolation.
- Les variantes à issue constante sont exclues, l'AUC y étant indéfinie (remarque de D à E).
- H_B sur (i) ferme U3. H_B sur (ii) ferme U1 et D3′. Aucun des deux ne ferme U5.

### D3′ — Anticipation (refondue)

**Conditions d'entrée.** D0 a donné H_B et D4′ (ii) a donné H_A.

**Ancrage temporel.** Un pas k\* connu sans la sonde :
- chez l'honnête, une panne exogène plantée à k\* (contrôle de E) ;
- chez le saboteur, la première action dommageable, datée par différence mécanique, à l'aveugle de la condition et sous un calendrier d'inspection assigné indépendamment du score (contrôle de D).

**Critère.** Binaire : le détecteur causal, à seuil gelé sur d'autres tâches, s'allume-t-il dans la fenêtre précédant k\* ? Un critère binaire évite le délai non défini.

**Duel.**
- H_A : le taux d'anticipation sous sabotage, moins celui du bras à consigne bénigne, est ≤ g.
- H_B : il est > g.
- L'effet est rapporté dans les deux sens.

**Contrôles.**
- Négatif à vérité connue : sous panne exogène, le taux avant k\* doit rester au niveau A/A.
- Lecteur du transcrit sans consigne, sous la même censure.

**Ordre.** Tableau de jugeabilité, D0 (avec les rangs pour D2′), D4′, D2′, D1′, D3′.

---

## (c) Réponse à l'arbitre, en une page

### Ce qui est établi

- **RAPPORTÉ (papier : Xu, Yuksekgonul, Zou, « Sparse Reward Subsystem in Large Language Models », identifiant donné par les faits).**
  - AUC avant génération de 0,67 en moyenne, contre 0,62 pour la longueur de la question.
  - Ablation : la précision passe de 75,2 % à 20,3 %.
  - Recherche par étapes : 77,8 % contre 72,2 %.
  - Aucun cadre adverse ; non testé hors récompense vérifiable.
  - Valeur lue au prompt et en position finale seulement.
- **Calcul standard, sous indépendance et échangeabilité (ce ne sont pas des faits du programme).**
  - Les 5 000 épisodes par tranche sont un critère de précision.
  - Le plancher de validité est plus bas, mais reste au-dessus du stock : environ 299 épisodes vierges sans dépassement pour borner 1 % à 95 % (illustratif), davantage par tranche à risque partagé.
  - Aucun outil de la liste ne certifie 1 % par tranche de longueur réalisée avec quelques centaines d'épisodes répartis en plusieurs tranches.
  - Un e-processus garantit un taux marginal ; par tranche, la borne est α/p_b.

### Ce qui ne l'est pas

- Que les neurones du papier existent ou se transfèrent en recherche ouverte.
- Qu'une lecture pas à pas de la valeur ait un sens.
- Qu'une sonde interne quelconque sépare le sabotage d'une simple différence de consigne.
- Que les épisodes existants soient vierges et échangeables.
- Que le nul au pas tienne sous les écarts réels de configuration, et qu'il ait de la puissance sous sabotage diffus.
- Que le 1 % découle d'un budget d'audit.

**Données absentes des faits, à demander à l'arbitre.** C ; T ; le nombre de pas par épisode ; le journal des ajustements ; le mode de fabrication du saboteur ; l'existence d'épisodes de sabotage à dégât confirmé ; les parts de tranche ; les journaux d'inclusion et d'arrêt (demande de D, que je reprends).

### Les points 1 à 5 de la question, corrigés

**1. Ce que ferait l'expert.** Calculer la jugeabilité avant tout achat. Prendre la tâche comme unité. Demander comment le saboteur est fabriqué.

**2. Données brutes.** Les traces pas à pas avec le journal des ajustements et des inclusions. Les continuations d'un pas du jumeau. Les bras de D0.

**3. Outils.** Le tableau de III.1, amendé par (a) : aucun ne donne 1 % par tranche sans ses hypothèses.

**4. Contrôle extérieur.**
- Lot séquestré chez un tiers.
- Sabotages produits par une équipe distincte.
- Datation et confirmation du dégât à l'aveugle.
- Réplication de la Table 2 sur un modèle ouvert des faits.
- MATH500 sert à vérifier l'extraction, pas à grossir le dénominateur (restriction de D, que j'accepte).

**5. Demande reformulée.**

> « Sur des épisodes honnêtes non interrompus, vierges, répartis en T tâches, quel taux α\* est certifiable, globalement et par tranche ? Une sonde sépare-t-elle le sabotage à dégât confirmé d'un agent à consigne bénigne et de l'échec honnête apparié, au-delà de la ligne de base du jumeau forcé ? À défaut de 1 % par tranche, quel budget d'audit et quelle garantie marginale accepte-t-on explicitement ? »

### 6. Propositions

| Proposition | Coût | Suppose | Échoue si |
|---|---|---|---|
| α\* rapporté, « non jugeable à 1 % » écrit par tranche | nul | épisodes vierges | α\* trop lâche (c'est une information) |
| Rang conforme par tâche après normalisation gelée (P1′) | nul | au moins 99 tâches échangeables (illustratif) ; garantie en moyenne seulement | queues inégales par tranche |
| Moniteur d'écart de politique (P2′), seuil 100/p_min | m générations par pas surveillé | même configuration que le jumeau ; lecture seule | écart de configuration ; puissance nulle si diffus ; lit la consigne |
| Budget d'audit : k premiers plus audits aléatoires (P4′) | budget humain | le budget est la vraie contrainte | saboteur sous le k-ième rang |
| Achat séquentiel à strates fixées avant génération (P6′) | borné à l'avance | probabilités d'inclusion connues | taux vrai proche de 1 % |
| Papier : score candidat dans P2′ | passes avant | D0 donne H_B | n'apporte rien au-delà de la ligne de base n° 2 |
| Papier : valeur lue sur le jumeau, pour répartir la revue | une passe | D4′ (i) | gain nul devant la longueur |
| Papier : neurones de dopamine pour la sélection de continuations | quatre tirages par pas | agent honnête ; gain d'utilité, pas mesure de sûreté | circulaire face à un agent adverse |

### L'expérience à faire en premier

**D0**, après le tableau de jugeabilité.

- Elle ne demande aucun seuil à 1 %.
- Elle coûte quelques dizaines de variantes en quatre bras (illustratif).
- Elle décide si les contrastes internes du programme lisent autre chose qu'une consigne.
- Si elle donne H_A, calibrer finement un tel score à 1 % n'a pas d'objet.

FIN-DE-CELLULE