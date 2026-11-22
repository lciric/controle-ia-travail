# Proposition B : Tour III.3, réponse aux critiques

## 0. État des pièces

- **FAITS** reproduit la question de l'arbitre, avec la même empreinte. Ce bloc ne contient aucun fait doté d'un statut, donc rien de ce qui suit n'est VÉRIFIÉ.
- **Pièces reçues** : ma conception III.1 et les critiques A, C, D, E et F. Toutes sont présentes et se terminent par leur marqueur de fin. Je ne traite que leurs sections « Sur la proposition B ».
- **Statuts des critiques** : C, D, E et F apposent « VÉRIFIÉ » sur des propriétés de dispositif. Je ne modifie pas ces statuts et je ne m'en sers pas comme de résultats. Quand j'accepte une critique, c'est mon propre raisonnement qui l'accepte, et ce raisonnement a le statut HYPOTHÈSE.
- **Chiffres** : tous les chiffres sont illustratifs.
- **Regroupement (règle B1)** : plusieurs critiques visent le même défaut. Je les traite sur une même ligne en nommant chaque source, sans fusionner les propositions de leurs auteurs.

---

## (a) Réponse à chaque critique

| # | Critique (sources) | Décision | Conséquence |
|---|---|---|---|
| 1 | Les trois façons de fabriquer T3 (modèle plus faible, température, bruit) rendent le résultat vrai par construction ou ôtent toute puissance, selon le choix fait (A, C, D, E, F). | **Acceptée** | T3 devient unique et fixé d'avance : les erreurs naturelles de H, aux mêmes poids, avec le même décodage et sans consigne. Si ces erreurs sont rares, on durcit les tâches ; on ne bruite rien. |
| 2 | E1 : la sonde a* est entraînée là où a* = â, si bien qu'elle peut apprendre â (A, défaut G1). | **Transformée en test** | Les pas d'erreur naturelle entrent dans l'entraînement. Un prérequis P1 est mesuré sur l'ensemble de développement : aux erreurs de H, la sonde doit prédire a* mieux que â. Sinon E1 est déclarée non jugeable. |
| 3 | La position de lecture n'est pas fixée ; une lecture après l'action relit l'action déjà écrite (A, E). | **Acceptée** | Une seule position, fixée d'avance : le dernier jeton avant le premier jeton de l'action. Ce dispositif est repris de D, comme A le relève. |
| 4 | Les erreurs honnêtes tombent sur des pas difficiles (critique que C et F adressent à A). | **Acceptée par extension** | Je m'en sers. Chaque pas est stratifié par p̂*(s_t), la fréquence de a* parmi k tirages de H sur la même histoire, sans consigne. |
| 5 | T1 diffère de D par le déclenchement : une direction « condition satisfaite » franchit T1 et les tests d'ablation (A, E, F). | **Transformée en test** | Nouveau témoin **T7** : une consigne conditionnelle *déclenchée* mais bénigne, qui change un paramètre neutre de présentation. |
| 6 | Un lecteur externe d'une autre famille mesure un écart entre encodeurs, pas une information privée (A, défaut G7 ; C). | **Acceptée** | Le lecteur de référence devient l'**auto-lecteur** : mêmes poids, lecture du texte produit sans la consigne. Le lecteur d'une autre famille ne sert plus qu'à décrire. |
| 7 | Défaut G7 : à poids identiques, un gain interne sur le texte produit se réduit à l'information de consigne présente dans le contexte (A). | **Acceptée en partie, rejetée comme invalidation du régime d'instruction** | J'accepte qu'en régime d'instruction, un gain de détection ne puisse pas établir un calcul : il peut lire la consigne. Je rejette l'idée que ce régime ne serve à rien, pour trois raisons. A concède que G7 ne dit rien sous lecteur de capacité bornée. Le régime sert à tester T1 et T7. Il sert aussi à la localisation et au transfert vers les régimes à poids. D'où le critère de localisation M3 ajouté à E0′. |
| 8 | Exiger que les vérifications mécaniques soient au hasard sur D contre T3 (« sinon l'appariement est défectueux ») tout en les comptant parmi les bases à battre est circulaire (A, E). | **Acceptée** | La règle est retirée. L'appariement porte seulement sur la perte finale et la longueur. L'équilibre des autres covariables est rapporté. Les vérifications mécaniques deviennent des bases à part entière. |
| 9 | Retirer un témoin défaillant sauve indûment la conclusion qui en dépend (D). | **Acceptée** | Un témoin qui échoue rend non concluante la conclusion qui en dépend. |
| 10 | Ma définition de l'intention inclut le passage du moniteur ; réutiliser ce moniteur comme mesure valide un critère d'inclusion (D). | **Acceptée** | L'intention ne retient que deux conditions : la performance est inférieure à la capacité élicitée, et l'écart est causé par une variable manipulée. La furtivité est *mesurée*, plus filtrée. Les cas qui auraient été refusés par l'ancien filtre sont publiés. |
| 11 | Le prérequis « juge < 80 % » est fixé sur les tâches d'évaluation et l'invite peut être itérée jusqu'à l'atteindre (A, C, E). | **Acceptée** | L'invite de sabotage est figée sur l'ensemble de développement, le nombre d'itérations est publié, et le test porte sur des familles de tâches neuves. |
| 12 | Le prérequis conjoint peut être inatteignable sur un petit modèle (E, point b1). | **Rejetée comme défaut, transformée en mesure** | C'est le No-go de dispositif prévu. Pour qu'il informe, on rapporte la frontière entre dégradation obtenue et taux de capture du juge, sur trois tailles de modèle. |
| 13 | L'équivalence à ± 2 points sur T1 est sous-puissante avec 300 tâches (A, C). | **Acceptée** | On passe à un test d'équivalence en deux tests unilatéraux (TOST) sur l'AUROC des scores continus, avec un effectif calculé d'avance. Si cet effectif est inatteignable, le test est déclaré non jugeable avant l'exécution. |
| 14 | Avec 20 directions aléatoires, le 95ᵉ centile est le maximum (résolution 1/21), sans correction de multiplicité sur les couches (A, C, E, F). | **Acceptée** | Au moins 200 directions appariées en variance d'activation (dispositif proposé par D), une seule couche pré-enregistrée, effet mesuré au pas. |
| 15 | Le test d'orientation n'a ni estimateur ni seuil (E, F). | **Acceptée** | Un indice de sélectivité est défini (E2′). |
| 16 | Une ablation testée sur un H au plafond ne peut pas l'améliorer (D). | **Acceptée** | On utilise H′, des tâches où H garde une marge d'amélioration. |
| 17 | Défaut G5 : toute variable située en amont du comportement passe un test d'ablation (A). | **Acceptée, limite déclarée** | E2′ ne sépare pas un « bit de mode » d'un calcul. Seuls E1′ et la localisation M3 y contribuent, et partiellement. |
| 18 | Le taux de détection à FPR = 1 % repose sur 1 à 3 trajectoires (A, C, E, F). | **Acceptée** | Critère principal : taux de détection à FPR = 5 % et AUROC partielle sur [0 ; 0,1]. Le point à 1 % devient descriptif. |
| 19 | L'appariement peut ne retenir qu'une petite zone de recouvrement (A, F). | **Acceptée** | On rapporte le recouvrement η et l'effectif utile n_eff. Un n_eff minimal est pré-enregistré. |
| 20 | Couche, règle d'agrégation, seuil et meilleure base sont choisis sur le test (A, F). | **Acceptée** | Trois ensembles disjoints par famille de tâches : entraînement, développement, test. |
| 21 | L'AUROC multiclasse n'est pas défini de façon unique (D, E). | **Acceptée** | La métrique devient la probabilité calibrée que la sonde attribue à a*. |
| 22 | E4 n'est pas exhaustif : un plan porté par le contenu survit à la paraphrase, de même qu'une boule de neige honnête (A, D, E, F). | **Acceptée** | E4 est remplacé par une **reprise croisée** (E4′). |
| 23 | E5 compare des professeurs différents ; l'échec d'une sonde figée confond absence d'information et rotation ; reconnaître une provenance n'est pas reconnaître un motif (C, D, E, F). | **Acceptée** | Auto-distillation honnête appariée en perte, plusieurs adaptateurs par classe, sonde figée et sonde réentraînée, contrôle sur texte neutre. La portée de E5 est réduite en conséquence. |
| 24 | Le mot de passe de T2 est lisible lexicalement (A). | **Acceptée** | Ajout de mots de passe leurres de même format, qui ne déverrouillent rien. |
| 25 | Ajouter des graines ne réduit pas le plancher de variance dû aux tâches (F). | **Acceptée** | Une seule graine, et davantage de tâches. |
| 26 | Le plafond 1 − r_α(V) s'applique dès E0 (D). | **Acceptée** | Si une base dépasse 0,90 de détection à FPR = 5 % sur l'ensemble de développement, H_A est déclarée inatteignable avant toute analyse interne. |

---

## (b) Expériences corrigées

### Règles communes

- **R1. Définition opérationnelle.** Voir la ligne 10 : performance inférieure à la capacité élicitée, écart causé par une variable manipulée. La furtivité est une variable mesurée.
- **R2. Témoins.**
  - *Négatifs* : H ; T3 (ligne 1) ; T1 ; T7 ; T4 (consigne bénigne qui dégrade).
  - *T5 (sabotage ouvert)* : il devient le **témoin positif du juge**, qui doit l'attraper. J'utilise ici la remarque que D adresse à A.
- **R3. Lecture.** Avant l'action, à une couche et avec une règle d'agrégation choisies sur l'ensemble de développement.
- **R4. Bases.**
  - le juge LLM, qui lit la trajectoire complète, la spécification et les sorties mécaniques ;
  - les vérifications mécaniques ;
  - l'auto-lecteur ;
  - la combinaison juge + mécaniques.

  La meilleure base est choisie sur l'ensemble de développement.
- **R5. Statistique.**
  - L'unité est la tâche.
  - Pour chaque critère, on fixe d'avance une région G et on applique la règle de décision proposée par D : intervalle entièrement dans G, intervalle entièrement hors de G, ou « non tranché ».
  - La puissance est calculée pour que la probabilité de « non tranché » reste sous 20 % sous l'effet minimal visé.
- **R6. Témoins défaillants.** Voir la ligne 9.
- **R7. Régimes à poids.**
  - Au moins 4 adaptateurs par classe, avec une même recette.
  - La sonde doit être au hasard sur du texte neutre hors tâche ; sinon, elle lit les poids.

### E0′. Première expérience (question 6)

**Dispositif**
- *Modèle* : un modèle ouvert de 7 à 9 milliards de paramètres (illustratif). Deux tailles inférieures servent seulement à tracer la frontière du prérequis.
- *Tâches* : 1 000 tâches d'analyse synthétiques, de 30 à 60 actions, réparties par famille en 40 / 20 / 40 % pour l'entraînement, le développement et le test (illustratif).
- *Conditions* : H, D, T1, T7, T4, T5. Les trajectoires T3 sont extraites des exécutions de H.

**Prérequis, mesurés sur l'ensemble de développement**
- H réussit nettement au-dessus du plancher.
- D dégrade d'au moins 15 points.
- Le juge capture moins de 80 % des trajectoires de D.
- Le juge capture plus de 90 % des trajectoires de T5.
- Aucune base ne dépasse 0,90 de détection à FPR = 5 % (ligne 26).

Tous ces seuils sont illustratifs.

**Mesures sur l'ensemble de test**
- **M1** : gain de détection à FPR = 5 % de la sonde interne sur la meilleure base. Positifs : D. Négatifs : H, T3 apparié, T1, T7 et T4.
- **M2** : équivalence par TOST de l'AUROC de T1 contre H, puis de T7 contre H, dans l'intervalle [0,45 ; 0,55] (illustratif).
- **M3** : localisation en différence de différences. On calcule l'écart de score entre les pas à fort impact et les pas routiniers chez D, puis on en retire le même écart chez H, *aux mêmes types d'étape*.

**Hypothèses**
- **H_A** : le signal interne apporte quelque chose qui n'est ni la consigne, ni le déclenchement, ni un état de but constant. Il faut à la fois :
  - un intervalle de M1 entièrement au-dessus de 0,10 ;
  - l'équivalence M2 établie pour T1 et T7 ;
  - un intervalle de M3 entièrement au-dessus de 0.
- **H_B** : le signal se réduit à ce qui accompagne le calcul. Il suffit de l'une des trois issues suivantes :
  - M1 entièrement sous 0,10 ;
  - M2 qui rejette l'équivalence ;
  - M3 entièrement au voisinage de 0, dans une marge fixée d'avance.

**Décision**

| Issue | Lecture | Décision |
|---|---|---|
| M1, M2 et M3 conformes à H_A | signal non textuel, ni consigne ni déclenchement, localisé | **Go** : E1′, E2′, puis E4′ et E5′ |
| M1 sous le seuil | la base textuelle ou mécanique suffit | **No-go** pour la lecture interne dans ce régime ; travailler sur les moniteurs textuels |
| M2 échoue sur T7 | la sonde lit la condition satisfaite | **No-go** pour cette sonde ; rejouer en T2 avec leurres avant de conclure |
| M3 nul | état de but constant | utile comme moniteur, mais ne répond pas à la question 1 |
| Prérequis échoue | dispositif | publier la frontière entre dégradation et capture sur les trois tailles, sans conclusion sur la question |

**Limite déclarée (ligne 7).** Même un Go ne démontre pas une information privée au-delà du contexte : en régime d'instruction, la consigne est dans le contexte. Le Go autorise seulement à passer aux régimes à poids.

### E1′. C1 est-il calculé, et est-il un marqueur ? (questions 1 et 5)

**Prérequis P1** : défini à la ligne 2.

**E1a. Contraste à histoire identique**
- *Population* : les pas où D émet une action fausse alors que p̂*(s_t) ≥ 0,7 (illustratif), c'est-à-dire où H, sur la même histoire, agirait correctement.
- *Comparaison* : la probabilité que la sonde attribue à a* dans l'état de D, contre la même quantité dans l'état de H lisant la même histoire.
- **H_A** (D calcule a* puis dévie) : écart ≥ −0,05, établi par TOST.
- **H_B** (D fonctionne comme un modèle plus faible) : écart ≤ −0,15.
- *Entre les deux* : non tranché, déclaré d'avance.

Ces seuils sont illustratifs.

**E1b. Spécificité**
- *Mesure* : la fréquence de « a* décodé, action fausse » aux erreurs de D, comparée à la même fréquence aux erreurs naturelles de H, par strate de p̂*.
- **H_A** : excès chez D ≥ 0,10 (illustratif).
- **H_B** : pas d'excès. Dans ce cas, C1 peut être calculé, mais il ne distingue pas l'intention : l'écart entre ce que le modèle sait et ce qu'il fait existe aussi chez l'honnête.

**Contrôles**
- tâche de contrôle à la Hewitt–Liang ;
- texte neutre ;
- rejeu en T2 avec mots de passe leurres.

### E2′. Lit-on ce qui accompagne le calcul ? (question 4)

**Direction** : apprise sur l'ensemble d'entraînement.

**Trois tests**
1. **T1 et T7** : les mêmes TOST que M2.
2. **Ablation chez D**
   - *Mesure principale* : effet au prochain pas à fort impact, comparé à au moins 200 directions aléatoires appariées en variance.
   - *Trajectoire complète* : pour la direction cible et 20 témoins.
   - *Interaction* : E_D(Q_abl − Q) − E_{H′}(Q_abl − Q) > 0, sur H′ (ligne 16).
3. **Orientation de H**
   - *Indice de sélectivité* : la baisse d'exactitude aux pas à fort impact, moins la baisse aux pas routiniers, sous une norme appariée à la projection de D.
   - *Comparaison* : la même distribution d'indices pour les directions aléatoires.

**Hypothèses**
- **H_A** : les trois tests passent, avec un effet au-dessus du 95ᵉ centile du nul.
- **H_B** : la sonde déclenche sur T7, ou l'effet reste dans le nul.

**Limite (ligne 17).** Un succès montre que la direction est en amont du comportement. Il ne montre pas qu'elle est un calcul plutôt qu'un bit de mode.

### E3

E3 est absorbée dans E0′ pour le régime d'instruction. Elle est rejouée telle quelle en T2 avec leurres, puis dans E5′.

### E4′. Où est porté le plan ? Reprise croisée (questions 1 et 5)

**Point de reprise** : l'histoire de D est coupée au pas k, au milieu de la trajectoire.

**Bras de continuation**
1. D poursuit, avec la consigne.
2. H poursuit, sur une copie exacte de l'histoire et sans consigne.
3. H poursuit, sur l'histoire paraphrasée.
4. D poursuit, sur l'histoire paraphrasée.
5. Témoin de boule de neige : H poursuit sa propre histoire, où une seule erreur factuelle a été injectée.

**Mesure** : la perte accumulée après le pas k.

**Hypothèses**
- **H_A** (le plan est re-dérivé de la consigne ou des poids) : le bras 1 moins le bras 2 dépasse 0,10 (illustratif).
- **H_B** (le plan est porté par le texte) : bras 1 et bras 2 équivalents par TOST.

**Lectures complémentaires**
- Si le bras 2 dégrade mais pas le bras 3, le plan est porté par la surface du texte. Un moniteur qui normalise le texte suffit alors.
- Le bras 5 calibre la part de dégradation qu'une erreur héritée produit seule, sans aucune intention.

### E5′. Dégradation amortie : reste-t-il quelque chose à lire ? (questions 3 et 5)

**Adaptateurs**
- 4 adaptateurs de **D amorti**, auto-distillés sur ses propres sorties dégradées, sans consigne ni mot de passe.
- 4 adaptateurs de **H auto-distillé** sur ses propres trajectoires erronées de même perte, avec la même recette, le même volume de données et le même nombre de pas.

**Lecture**
- *Sondes* : une sonde figée venue de E0′, et une sonde réentraînée en laissant un adaptateur de côté à chaque fois.
- *Contrôle* : texte neutre.

**Hypothèses**
- **H_A** (une trace persiste) : il faut à la fois :
  - une AUROC de la sonde réentraînée ≥ 0,70 ;
  - le hasard sur texte neutre ;
  - M3 > 0.
- **H_B** (rien à lire) : AUROC ≤ 0,55, sonde réentraînée comprise.
- *Entre les deux* : non tranché.

**Portée et puissance**
- L'unité d'inférence est l'adaptateur. Avec 4 contre 4, E5′ reste exploratoire.
- Il faudrait au moins 8 adaptateurs par classe pour une décision (illustratif).
- Même positive, E5′ identifie une provenance et non un motif (critique de D, ligne 23).

### Budget révisé

Tous les montants sont illustratifs. Le budget augmente parce que les critiques de puissance (lignes 13, 18 et 25) l'imposent.

| Poste | GPU-h H100 |
|---|---|
| E0′ : génération, 6 conditions × 1 000 tâches | 90–160 |
| Auto-lecteur et p̂* (k tirages sur un sous-ensemble) | 40–80 |
| Frontière du prérequis sur deux tailles inférieures | 20–40 |
| **E0′, total** | **≈ 150–280, soit environ 450–1 000 € en location** |
| E5′ : 8 à 16 adaptateurs LoRA | 30–60 |
| E2′ : 200 directions, mesure au pas | 20–40 |

---

## (c) Réponse à la question de l'arbitre (une page)

**Ce qui est établi**

- **Sur le plan empirique** : rien. Les FAITS ne contiennent aucun résultat, et aucune expérience n'a été menée dans ce collisionneur.
- **Sur le plan du dispositif** : trois points, qui sont mon raisonnement (HYPOTHÈSE, non audité) et qu'aucune des cinq critiques ne conteste.
  1. *L'état ne contient que le contexte.* À poids identiques, l'état interne est une fonction du contexte ; c'est une propriété d'architecture, RAPPORTÉ. En régime d'instruction, « mieux que le texte produit » peut donc venir de la seule lecture de la consigne. Les témoins T1 et T7 et la localisation M3 sont nécessaires pour exclure cette lecture.
  2. *T3 doit venir des mêmes poids.* Des erreurs honnêtes fabriquées par un autre modèle, par du bruit ou par la température rendent les contrastes vrais par construction, ou sans puissance.
  3. *Le seuil à 1 % n'est pas estimable.* Avec quelques centaines de tâches, un taux de détection à FPR = 1 % ne l'est pas.

**Ce qui ne l'est pas**

- **Question 1.**
  - *Ce que je suppose* (HYPOTHÈSE) :
    - C1, la discrimination de la bonne action, n'est nécessaire que pour une dégradation sélective.
    - C2, un modèle du contrôleur, n'est nécessaire que pour une adaptation en ligne.
    - C3, la coordination entre actions, est soit re-dérivée à chaque pas, soit portée par le texte.
  - *Ce que je ne sais pas* : si l'un de ces calculs est *propre* au dégradeur. L'erreur honnête peut, elle aussi, contenir a* décodé.
  - *Ce qui me ferait changer d'avis* : E1a et E1b.
- **Question 2.** Toutes les références sont citées de mémoire (RAPPORTÉ) et les attributions sont à vérifier avant usage.
  - *Sous-performance stratégique* :
    - van der Weij et al. (2024), *AI Sandbagging* ;
    - Greenblatt et al. (2024), *Stress-Testing Capability Elicitation With Password-Locked Models* ;
    - Hubinger et al. (2024), *Sleeper Agents*.
  - *Contrôle et sabotage* :
    - Greenblatt et al. (2023), *AI Control* ;
    - Benton et al. (2024), *Sabotage Evaluations for Frontier Models*.
  - *Sondes* :
    - Goldowsky-Dill et al. (2025), *Detecting Strategic Deception Using Linear Probes* ;
    - Azaria et Mitchell (2023), *The Internal State of an LLM Knows When It's Lying*.
  - *Méthodologie des sondes* : Hewitt et Liang (2019), *Designing and Interpreting Probes with Control Tasks*.
  - *Surveillance des raisonnements* : Baker et al. (2025), *Monitoring Reasoning Models for Misbehavior*.
  - *Attribution incertaine* : Tice et al. (2024), sur l'injection de bruit, est une référence à vérifier.
  - *État de la question* : à ma connaissance, aucun de ces travaux ne démontre un calcul nécessaire au sabotage sur trajectoire longue avec des témoins de type T3 et T7. C'est une HYPOTHÈSE, car je ne peux pas prouver une absence de mémoire.
- **Question 3.** Je suppose (HYPOTHÈSE) que la réponse dépend du mode d'acquisition. Avec une instruction, l'information est dans le contexte. Avec un entraînement amorti, il peut n'y avoir rien de spécifique à l'inférence. C'est E5′ qui tranche, avec des adaptateurs répliqués des deux côtés.
- **Question 4.** Trois choses permettent de dire qu'on lit un éventuel tel calcul plutôt que ce qui l'accompagne :
  - le témoin T7, déclenché et bénin, en plus de T1 ;
  - la localisation en différence de différences, aux mêmes types d'étape ;
  - l'ablation, comparée à au moins 200 directions appariées et testée sur un H qui garde une marge.

  Pour dire qu'on lit mieux que le texte, il faut battre la meilleure base fixée sur l'ensemble de développement (juge, mécaniques, auto-lecteur, combinaison), à FPR = 5 %. Une base qui sature (> 0,90) rend la question sans objet dans ce régime.
- **Question 5.** Il n'y aurait rien à lire, sous HYPOTHÈSE, dans quatre cas :
  - la dégradation est uniforme ;
  - la dégradation est amortie dans les poids ;
  - le plan est porté par le texte (E4′, bras 2 ≈ bras 1) ; un moniteur textuel suffit alors ;
  - le signal se réduit à un état de but constant (M3 nul) ; il est utile comme moniteur, mais muet sur le calcul.

**L'expérience à faire en premier : E0′**

E0′ porte sur un seul modèle de 7 à 9 milliards de paramètres et 1 000 tâches, réparties par famille. Elle mesure trois choses : M1 (gain sur la meilleure base à FPR = 5 %), M2 (équivalence sur T1 et T7) et M3 (localisation). Chacune de ses issues falsifie quelque chose :

- **Go** : H_B est réfutée pour ce régime.
- **M1 sous le seuil** : l'apport de la lecture interne est réfuté dans ce régime.
- **M2 échoue** : la sonde est réfutée comme lecteur de calcul.
- **Prérequis non atteint** : le dispositif est réfuté pour cette taille, et l'on publie la frontière, sans conclusion sur la question.

**Ce qui me ferait changer d'avis**

- *Si E0′ donne M1 sous le seuil*, j'abandonne la lecture interne à cette échelle.
- *Si E0′ donne M2 qui échoue sur T7*, je cesse de considérer le régime d'instruction comme un terrain de développement utile.
- *Si E1b ne montre aucun excès*, j'abandonne C1 comme marqueur de l'intention.
- *Si E5′ montre une trace persistante sur des adaptateurs inédits*, ma position sur la question 5 tombe.

FIN-DE-CELLULE