# Proposition B · Tour III.3 : riposte

**Pièces reçues.**
- Les trois pièces sont complètes et se terminent chacune par leur ligne de fin : ma conception III.1, l'attaque rouge A et l'attaque rouge C.
- Le bloc FAITS est vide par décision de l'arbitre (RAPPORTÉ).
- Je ne peux pas vérifier les empreintes sha256 (OBSERVÉ-NON-AUDITÉ).
- Je ne réponds qu'aux sections « Contre la proposition B ».

**Conventions.**
- Les calculs refaits ici sont VÉRIFIÉS comme arithmétique. Ils reposent tous sur une HYPOTHÈSE : bruit binomial, tâches indépendantes, variance entre graines nulle. Ce sont donc des **bornes basses**.
- Tout autre chiffre est « illustratif ».

---

## (a) Décision sur chaque attaque

### Attaques de A

| Réf. | Attaque | Décision | Raison, ou test qui la remplace |
|---|---|---|---|
| A·B-1 | δ n'est jamais fixé. L'issue « indéterminé » est quasi certaine. H_D est connue fausse d'avance. | **Acceptée** | J'ai refait le calcul : demi-largeur de l'IC à 90 % = 2,132 × 0,072 = 0,1535 sur `test_final` (VÉRIFIÉ). Mon § 3 donnait déjà un effet minimal détectable de 0,18 à 0,22. Faire falsifier H_D par la troisième issue ne falsifiait donc rien de neuf : c'était une violation de B4. Corrigé dans E1′ : δ est scellé par Lazar, une règle « largeur planifiée < δ » s'applique, et la troisième issue falsifie désormais une hypothèse **inconnue** avant la course (la variance entre graines planifiée). |
| A·B-2 | E2 fuit, parce que l'analyste connaît le signe vrai. | **Acceptée, transformée** | E2 n'a jamais eu besoin des vrais scores. Il s'agit de mesurer la sensibilité à un canal, pas de transmettre le canal réel. E2′ n'emploie que des résumés **synthétiques**, avec des étiquettes masquées X/Y par script et un analyste extérieur aux lignées. |
| A·B-3 | E3 mesure la docilité de l'agent. L'agent construit l'instrument qui sera scellé. | **Acceptée** | Un rédacteur à qui l'on donne une donnée s'y adapte : la critique est juste. E3′ devient un **calcul préposterior par script**, sans agent rédacteur. Aucune table issue de E3′ n'est scellée telle quelle. |
| A·B-4 | E4 se réduit à un tirage à pile ou face. | **Acceptée, avec une correction chiffrée** | « Quasi certain » est exagéré. L'écart entre le Δ du pilote et le Δ̂ de (b) a un écart type de √(0,11² + 0,072²) ≈ 0,131 (σ_diff = 0,11, illustratif). La probabilité de tomber dans l'IC vaut alors P(\|Z\| < 1,17) ≈ 0,76, ou ≈ 0,71 avec σ_diff = 0,125. La conclusion de A tient pourtant : c'est une seule observation binaire, à faible pouvoir de falsification. **E4 est retirée comme duel.** |
| A·B-5 | Le contrôle A/A sort du budget, et son substitut mesure autre chose. | **Substitut : acceptée. Budget : rejetée en partie** | La question dit « 450 au pire », pas « plafond » (RAPPORTÉ). J'avais moi-même écrit « plafond » en III.1, une lecture à faire confirmer par Lazar. Un A/A coûte +90 USD attendus (+150 au pire), dérivé de 45 et 75 USD par course : total ≈ 360 attendus, 600 au pire. C'est une option chiffrée, pas une impossibilité. Le substitut par réordonnancement est retiré. |
| A·B-6 | Des choix sont laissés ouverts (génération, agrégat des familles). | **Génération : acceptée. Agrégat : rejetée sous a11** | Sous ma lecture a11, chaque famille compte 24 tâches `test_final`. La moyenne non pondérée des deux familles **égale** alors la moyenne poolée sur 48 tâches : les « deux agrégats » de A coïncident. Ils ne divergent que si a11 est fausse. Le texte scellé écrira donc « moyenne non pondérée des deux familles » et vaudra sous les deux lectures. Pour la génération, je choisis : génération 4, en primaire. |
| A·B-7 | Omissions : dérive du modèle appelé, sens de « graine », coût. | **Acceptées, transformées en tests** | E6 (étalon de dérive, plus courses entrelacées), E7 (sens de la graine), coût en variable secondaire descriptive. |
| A · évasions | Paraphrase, brouillons à trous, longueur ou délai de l'enveloppe, bruit injecté par l'organisme, journaux, E3 pilotée par la consigne. | **Acceptées** | Paraphrase et brouillons à trous → D8 (gel des champs sensibles). Longueur et délai → format à longueur fixe, remis à heure fixe. E3 pilotée → E3′ par script, avec une grille de lois a priori scellée. Bruit injecté → l'audit de propreté par variance est retiré (voir C·év.4). |
| A · contrôles 1 à 6 | Brouillon témoin, masquage de E2, rédaction à vide, clause σ_graine, relance à graine identique, étalon. | **Acceptés** | (1) reste utile pour les champs **non** gelés par D8. (2) → E2′. (3) → condition « aucun score » de E2′, et double rédaction (à vide puis exposée) dans les options (2) et (2′). (4) → clause de E1′. (5) → E7. (6) → E6. |

### Attaques de C

| Réf. | Attaque | Décision | Raison, ou test qui la remplace |
|---|---|---|---|
| C·1 | E3 est vraie par construction de l'invite. D1 fuit par le canal opérationnel du lancement. | **Acceptée** | La première moitié recoupe A·B-3. Pour la seconde, j'avais signalé la fuite par les paramètres visibles sans en faire une **condition**. C'en est une désormais : toute branche de D1 doit avoir une **empreinte opérationnelle identique** (mêmes courses, mêmes objets, même nombre d'appels), vérifiée par simulation avant scellement. Une branche qui change le nombre de graines est interdite. |
| C·2 | Un TOST est impossible avec 3 graines pour δ ≤ 0,15. | **Acceptée** | Calcul VÉRIFIÉ. À δ = 0,20, il faut \|Δ̂\| < 0,0465 (VÉRIFIÉ). |
| C·3 | Un IC de [0,02 ; 0,18] satisfait les deux règles à la fois. | **Acceptée** | Mes deux règles se chevauchaient. La règle « borne inférieure > 0 » testait Δ > 0, et non Δ ≥ δ. Corrigé dans E1′ : H_A et H_B sont exclusives sans être complémentaires, et chacune est rejetée par un test unilatéral séparé. |
| C·4 | La réévaluation avec un autre ordre des tâches écrase la variance de conception. | **Acceptée, avec une nuance** | Elle ne « vaut exactement 0 » que si les appels de classement sont déterministes. Sinon, elle mesure la stochasticité d'évaluation, ce qui reste différent de la variance entre graines. La conclusion ne change pas : substitut retiré. |
| C·5 | E5 confond la pente intra-course et la variance entre graines. | **Acceptée** | **E5 est retirée.** D4 est restreint (voir plus bas). |
| C·év.1 | Les 3,2 bits contiennent toute l'information stratégique. | **Acceptée** | La borne en bits limite la **quantité** d'information, pas le **dommage**. J'avais écrit « exactement les bits pertinents » sans en tirer la conséquence : l'alphabet contraint ne protège rien dès que le destinataire est un auteur. |
| C·év.2 | Un brouillon à branches latentes, appuyé par des notes antérieures à T0. | **Acceptée** | L'audit de différences ne voit pas un choix fait entre des branches pré-déclarées. → D8 : choisir une branche après T0 compte comme une modification d'un champ gelé. |
| C·év.3 | Un « parser tolérant » choisi d'après les faits mécaniques. | **Acceptée** | Elle réfute aussi mon option (3) comme canal « nul pour les scores ». Les types d'erreur par famille constituent un canal. → D8 gèle les règles d'analyse syntaxique et d'exclusion. Les faits mécaniques sont restreints à des agrégats (coût et durée totaux) jusqu'au gel. |
| C·év.4 | L'audit de propreté est contourné : 18, 20 et 21 sur 24 donnent une variance de 0,00405 > 0,0039. | **Acceptée, et aggravée** | Calcul de C VÉRIFIÉ. C'est pire : avec 3 graines, s²/σ² suit χ²₂/2 (approximation normale, HYPOTHÈSE). Sous un bruit honnête, P(s² < 0,5 σ²) = 1 − e^(−0,5) ≈ **0,39** de fausses alertes par objet (VÉRIFIÉ). Mon instrument était inutilisable. Retiré (voir (b)). |
| C·év.5 | Évasion combinée. | **Acceptée** | L'asymétrie de seuil est corrigée par E1′, le choix de branches par D8. Le résidu est déclaré en (c). |
| C · contrôles 1 à 3 | Cécité opérationnelle de D1, variance réelle entre graines, agents à contexte d'auteur. | **Acceptés** | (1) → condition de D1. (2) → estimation intra-objet sur 3 graines, 4 ddl, dans E1′. (3) → contrôle positif de E2′. |

---

## (b) Expériences corrigées

### D8 (nouveau dessin, préalable commun à toutes les options) : gel des champs sensibles avant T0

- **T0** : avant le lancement du pilote 4, puisque des scores peuvent apparaître pendant la course (a2).
- **Ce qui est gelé** : chaque texte principal gèle, avec une empreinte publiée, une liste de champs :
  - famille primaire ;
  - part et génération mesurées ;
  - règle d'analyse syntaxique des sorties mal formées ;
  - sort des courses plantées ;
  - organismes servis ;
  - identifiants de la banque ;
  - forme des hypothèses (symétrique ou orientée).
- **Champ non décidé** : il est remplacé par une **règle de décision scellée** qui ne cite aucun pilote.
- **Qui dresse la liste** : un agent neuf, à partir de la structure des brouillons, pour qu'aucun auteur ne choisisse ce qu'il laisse ouvert.
- **Vérification** : un diff mécanique sur les champs gelés (détection = 1 par construction).
- **Ce que D8 ne couvre pas** : les champs absents de la liste, et la qualité des choix faits tôt. Le coût est réel : les lignées doivent trancher plus tôt (HYPOTHÈSE sur l'ampleur de ce coût).
- **Canal résiduel** : les faits mécaniques ne sont publiés qu'en agrégats (coût total, durée totale) jusqu'au gel. Les types d'erreur par famille restent fermés.

### E1′ : duel principal de (b)

**Métrique primaire.**
- Le score d'une course est l'exactitude de la **génération 4** sur `test_final`, en moyenne non pondérée des deux familles (48 tâches sous a11).
- Variables secondaires, ajustées par Holm :
  - chaque famille ;
  - la part `test` ;
  - la moyenne des générations ;
  - une analyse appariée par tâche (modèle mixte avec effets aléatoires tâche et graine) ;
  - le coût en USD par course, en variable descriptive.

**Hypothèses (exclusives, non complémentaires).**
- **H_A** : Δ ≥ δ.
- **H_B** : Δ ≤ 0.
- Δ = v6.2.1 − v5.3. δ est fixé par Lazar d'après l'enjeu, sans aucun score.

**Règle de lecture (IC à 90 % ; deux tests unilatéraux à 5 %).**

| Borne inférieure | Borne supérieure | Ce qui est falsifié |
|---|---|---|
| > 0 | ≥ δ | H_B |
| > 0 | < δ | H_B **et** H_A : effet positif, inférieur à δ |
| ≤ 0 | < δ | H_A |
| ≤ 0 | ≥ δ | aucune des deux → possible seulement si la largeur de l'IC est ≥ δ |

**Règle de dessin (condition B4).**
- On scelle une variance par course planifiée σ_planif = √(σ_bin² + σ_graine,planif²).
- On calcule la largeur planifiée L = 2 · t(2n−2) · σ_planif · √(2/n).
- Si L ≥ δ, (b) est déclaré **non décisif à δ avant toute course**. Lazar choisit alors : augmenter n, relever δ, ou courir (b) comme pilote descriptif.
- Si L < δ et que l'issue est malgré tout indéterminée, l'hypothèse σ_graine ≤ σ_graine,planif est **falsifiée**. Cette hypothèse était inconnue avant la course, ce qui répond à A·B-1.
- σ_graine est estimé par la variance intra-objet sur les graines (4 ddl si n = 3).
- La clause d'interprétabilité est scellée : E1′ devient ininterprétable si σ_course > δ / (2 · t · √(2/n)).

**Largeur L selon n (borne basse binomiale, 48 tâches, σ_bin = 0,0625 ; calcul VÉRIFIÉ ; coûts dérivés de 45 USD attendus et 75 USD au pire par course).**

| n par objet | t (2n−2) | Erreur type de Δ | Largeur L | Coût attendu / au pire |
|---|---|---|---|---|
| 3 | 2,132 | 0,051 | **0,218** | 270 / 450 |
| 5 | 1,860 | 0,040 | 0,147 | 450 / 750 |
| 8 | 1,761 | 0,031 | 0,110 | 720 / 1 200 |
| 10 | 1,734 | 0,028 | 0,097 | 900 / 1 500 |

- **Exemple illustratif** : pour δ = 0,25 et n = 3, il faut σ_course < 0,25 / 3,48 ≈ 0,072, donc σ_graine < √(0,072² − 0,0625²) ≈ 0,036.

**Test.**
- Primaire : t de Welch.
- Sensibilité : permutation exacte. La p-valeur minimale est 1/20 = 0,05 en unilatéral, ce qui exige une séparation parfaite (VÉRIFIÉ).
- Si les deux analyses divergent, l'issue rapportée est celle de la permutation.

**Contrôles et ordre des courses.**
- Contrôle de plancher (clés permutées, exactitude au hasard) : conservé.
- A/A : en option, au coût indiqué plus haut.
- Ordre des 6 courses : entrelacé et tiré au sort, avec un tirage scellé, pour ne pas confondre l'objet avec la date.

### E2′ : rédaction fantôme, sans les vrais scores

- **H_A** : un résumé de scores accompagné de la réserve déclarée « ces chiffres ne doivent pas orienter vos choix » déplace la famille primaire et la direction du seuil d'une **maquette** de confrontation.
- **H_B** : aucun déplacement.
- **Conditions** :
  - aucun score (ligne de base, contrôle 3 de A) ;
  - résumé synthétique favorable à la v6.2.1 ;
  - résumé synthétique défavorable ;
  - résumé de même forme, sans écart (contre l'ancrage sur la forme, B-2 de A) ;
  - pilote hors sujet.
- **Deux types de rédacteurs** :
  - agents neufs ;
  - agents dotés d'un contexte d'auteur simulé (l'historique de correction de la v6.2.1 présenté comme le leur). C'est le contrôle positif de sensibilité proposé par C.
- **Masquage** : un script étiquette les conditions X/Y. L'analyste est extérieur aux lignées et la clé n'est ouverte qu'après l'analyse.
- **Métrique** : la différence de proportion de choix « famille favorisée » entre les conditions favorable et défavorable. Effectifs k illustratifs.
- **Falsifications** :
  - un écart significatif falsifie H_B, et la réserve déclarée ne suffit pas pour ce type de rédacteur ;
  - l'absence d'écart chez les agents à contexte d'auteur, avec une puissance suffisante, falsifie H_A pour ce type de rédacteur ;
  - un écart chez les agents d'auteur seulement réfute toute garantie tirée des seuls agents neufs.
- **Fuite des scores du pilote 4** : nulle par construction.

### E3′ : la lecture de (a) améliore-t-elle (b) ? (calcul par script, sans agent)

- **Comparaison** : le dessin symétrique fixe E1′, qui ne lit rien, contre le meilleur dessin **conditionnel** que (2) et (2′) présupposent, où la direction et la famille primaire sont tirées de (a).
- **Critère** : la probabilité que (b) produise une issue décisive **correcte**, à n égal.
- **Modèle** :
  - Δ_famille suit une loi N(0, τ²), avec τ ∈ {0,05 ; 0,10 ; 0,20} (illustratif) ;
  - le pilote observe Δ + ε, avec σ_ε ∈ {0,10 ; 0,125} ;
  - la grille est scellée avant le calcul, pour qu'on ne puisse pas piloter l'issue par le choix des lois a priori (évasion signalée par A).
- **Hypothèses** :
  - **H_A** : le gain est ≥ g (g = 0,05, illustratif) pour toute la grille ;
  - **H_B** : le gain est < g pour toute la grille.
- **Issues** :
  - H_A vérifiée favorise (2′) ou D1 ;
  - H_B vérifiée favorise (3) ;
  - une issue mixte rend la décision dépendante de l'a priori de Lazar, ce qui est déclaré comme tel.
- **Pourquoi l'issue n'est pas acquise d'avance** : le dessin conditionnel gagne en puissance unilatérale, mais il perd chaque fois que le signe du pilote est faux.
- **Ordre de grandeur (illustratif, raisonnement explicite)** : P(signe correct) = ½ + arcsin(ρ)/π, avec ρ = τ/√(τ² + σ²). Pour σ = 0,11, on trouve ≈ 0,64, 0,74 et 0,84 pour τ = 0,05, 0,10 et 0,20. Avec τ = 0,10, (b) testerait donc la mauvaise direction environ une fois sur quatre.
- **Toute table D1** issue de E3′ passe en plus par une simulation sous Δ = 0 avant scellement, et la fréquence de chaque branche est publiée.

### E6 : étalon de dérive (contrôle 6 de A)

- **Dispositif** : un organisme gelé, une invite fixe, 20 tâches (illustratif), courus avant la première course de (b) et après la dernière.
- **H_A** : l'écart dépasse 2 fois l'erreur type binomiale de la différence (facteur illustratif).
- **H_B** : l'écart reste en dessous.
- **Falsifications** :
  - H_B falsifiée : E1′ est suspendue, car l'objet est confondu avec la version du modèle appelé ;
  - H_A falsifiée : la dérive est exclue à cette résolution.

### E7 : sens de la graine (contrôle 5 de A)

- **Dispositif** : une course du pilote 4 est relancée à graine identique. Un script ne rend que « identique / différent » et le nombre de tâches discordantes, jamais un niveau.
- **H_A** : la graine reproduit la course.
- **H_B** : la graine est une simple étiquette de réplicat.
- **Falsifications** : si les deux sorties diffèrent, H_A est falsifiée. La variance entre graines de E1′ inclut alors la stochasticité des appels, et c'est ce que (b) mesure.
- **Coût** : 45 USD attendus, 75 au pire (dérivé).

### Ce qui est retiré ou restreint

- **E4** n'est plus un duel. Elle devient une calibration du programme, à faire seulement quand plusieurs pilotes à une course auront chacun leur confirmation.
- **E5** est retirée (C·5).
- **D4** est restreint : le pilote 4 ne fournit ni variance entre graines ni proxy de celle-ci. Au plus, il donne la stochasticité d'évaluation (via E7) et la corrélation entre objets par tâche, pour la variante appariée. La fuite de niveau par cette corrélation reste une HYPOTHÈSE.
- **Audit de propreté par sous-dispersion** : retiré à 3 graines (≈ 0,39 de fausses alertes). Je propose à la place, sous le statut d'HYPOTHÈSE non calibrée, un audit par concordance tâche à tâche entre graines d'un même objet. Sa référence de bruit serait fournie par E7.

**Budget dérivé.**

| Configuration | Attendu | Au pire |
|---|---|---|
| 6 courses + E7 | 315 USD | 525 USD |
| avec A/A en plus | 405 USD | 675 USD |

L'étalon E6 est hors calcul (son coût n'est pas connu).

---

## (c) Réponse à la question de l'arbitre (une page)

**Établi (calculs VÉRIFIÉS, sous l'HYPOTHÈSE binomiale ; ce sont des bornes basses).**

1. Avec 3 graines par objet, l'IC à 90 % de Δ a une largeur d'au moins **0,218** sur la métrique poolée (48 tâches), et de 0,307 par famille. (b) ne satisfait la condition B4 (chaque issue falsifie quelque chose) que si δ ≥ 0,22, et seulement si la variance entre graines est faible. Pour δ = 0,10 (illustratif), il faudrait environ 10 graines par objet, soit ≈ 900 USD attendus.
2. Un test exact 3 contre 3 ne conclut à 0,05 qu'en unilatéral et sur une séparation parfaite (p minimale : 1/20 en unilatéral, 2/20 en bilatéral).
3. Un audit de sous-dispersion à 3 graines lève environ 0,39 de fausses alertes par objet sous un bruit honnête : il est inutilisable.
4. Le signe d'un pilote à une course est juste avec une probabilité d'environ 0,64 à 0,84 (illustratif, selon l'a priori).

**Raisonné, non mesuré (HYPOTHÈSE).**
- Aucune option ne transmet 0 bit. Même l'option (3) laisse passer les faits mécaniques (types d'erreur, plantages), qui corrèlent avec l'issue (C·év.3).
- Une borne en bits limite la quantité d'information, pas le dommage : quelques bits suffisent à orienter la famille primaire.
- Une réserve déclarée ne détecte rien.

**Non établi.**
- La valeur informative du pilote 4 pour (b) : E3′.
- L'étanchéité des journaux face au lanceur (a2) : à tester par une course factice avec canari.
- La force de l'influence sur des rédacteurs-auteurs : E2′.
- σ_graine ; le sens de la graine (E7) ; la dérive du modèle appelé (E6).
- La valeur de δ.
- Le statut de « 450 au pire » : estimation ou plafond.
- Le sens de « viser un signe » dans la règle du programme.

**Voies (D8 est le préalable commun à toutes ; aucune n'est « la » réponse).**
- **α** — option (3) avec E1′ symétrique : rien n'est lu. Favorisée si E3′ conclut à H_B.
- **β** — D1 avec branches à empreinte opérationnelle identique et simulation sous le nul. Favorisée si E3′ conclut à H_A et que a2 tient.
- **γ** — option (2′) avec un contre-lecteur jetable, un format fixe et une double rédaction. Favorisée seulement si E2′ ne montre aucun déplacement **chez les agents à contexte d'auteur**, et si le délai coûte cher.
- **δ** — option (1) avec un plan séquentiel. Favorisée si E2′ montre un déplacement et que le délai est acceptable.

**Ce qui départage les voies**, dans l'ordre : le δ choisi par Lazar et la largeur L correspondante (le point 1 peut rendre (b) non décisif quelle que soit l'option) ; E3′ ; E2′ ; a2.

**Expérience à faire en premier : E3′, avec le tableau δ ↔ n de E1′.**
- Elle coûte ≈ 0 USD, ne lit aucun score et peut se faire avant la fin du pilote 4.
- Elle oblige à fixer δ, ou une grille de δ.
- Elle peut rendre caduque la question du moment de lecture : si le dessin conditionnel ne bat pas le dessin symétrique, ouvrir les scores ne paie pas son risque.
- **Ce qui changerait l'ordre** : si la vérification mécanique de a2 (course factice avec canari) montre que les journaux exposent déjà les scores au lanceur, elle passe en premier. Toute option suppose en effet une fermeture qui n'existerait pas.

**Ce que (b) ne tranchera pas, même corrigé.**
- Un effet inférieur à L.
- La cause d'un écart entre v6.2.1 et v5.3 (a4) : l'ablation D7 reste nécessaire, avec un budget d'appels apparié (C l'a montré contre une autre proposition ; je l'applique ici en le disant).
- La généralisation aux banques des expériences principales.

FIN-DE-CELLULE