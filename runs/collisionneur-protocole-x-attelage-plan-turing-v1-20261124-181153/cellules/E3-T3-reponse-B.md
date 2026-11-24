# Proposition B, tour III.3 : réponse aux critiques

**Pièces.** Le bloc FAITS est identique au bloc QUESTION (même empreinte). Il ne contient donc aucun fait étiqueté et aucun fait VÉRIFIÉ. Ma conception III.1 et les critiques A, C, D et E sont présentes et complètes. Je ne traite que les sections « Sur la proposition B ».

**Statuts.**
- Je cite les statuts des critiques sans les modifier.
- Mes décisions de conception ont le statut HYPOTHÈSE.
- Mes calculs sont de l'arithmétique sur des paramètres hypothétiques. Leurs résultats sont **illustratifs**.

**Usage déclaré des autres propositions (B1).**
- Je reprends la règle de C : un seul seuil par contraste, avec des hypothèses exhaustives.
- Je reprends la critique que D adresse à A sur l'égalisation des appels au vérificateur.
- Je reprends la critique que C reçoit sur un placebo qui ralentirait le solveur. Elle me conduit à comparer aussi à un solveur sans idée ajoutée.

---

## (a) Verdict sur chaque critique

Légende : **ACC** = acceptée ; **REJ** = rejetée, raison donnée ; **TEST** = transformée en test.

### Critiques de A

| ID | Critique | Verdict | Conséquence |
|---|---|---|---|
| A-1 | E4 est vrai par construction : Q, qui définit l'étroitesse, est le modèle du bras 4. | ACC + TEST | L'étroitesse se mesure sous un panel Q_ref disjoint de tous les bras. J'ajoute un bras « différent mais pas meilleur ». S'il gagne, n mesure une distance à Q_ref et non une découverte. |
| A-2 | Le nombre de candidats est confondant. J'ai refait le calcul : 1 − 0,95⁵⁰ ≈ 0,92. | ACC | Chaque bras soumet k nominations, k fixe, choisies avant l'ouverture du coffre. |
| A-3 | E1 est tautologique. | ACC en partie, REJ en partie | ACC : E1 ne valide pas le construit, et je retire cette prétention. REJ : un contrôle positif est construit par définition, c'est sa fonction ; il détecte les bogues et les sensibilités de surface. J'ajoute une loi profonde non documentée comme plantée (idée que A formule pour C) et des leurres issus d'une autre grammaire. |
| A-4 | E2 subit une troncature de type Berkson. | ACC | L'ensemble de classes est fixé hors des tirages des Q. La statistique devient un désaccord sur le drapeau « étroit certifié », et non plus ρ sur des valeurs censurées. |
| A-5 | E3 souffre d'une étendue restreinte, et seule la profondeur est ajustée sur la complexité. | ACC | Tirage stratifié en n. Le même ajustement de complexité s'applique aux deux axes. |
| A-6 | E8 est circulaire. | ACC | Les régions sont choisies sous une référence Q′ disjointe de Q_ref. |
| A-7 | La canonicalisation n'est évaluée que d'un côté. | ACC | E0′ ajoute un plafond de fausses fusions. |
| A-8 | En E7, les cibles présentes et absentes ne sont pas appariées. | ACC | Injection randomisée (E7′). |
| A-9 | Zones mortes au sens de B4. | ACC pour les hypothèses ; REJ pour l'incertitude | Un seul seuil par contraste, hypothèses exhaustives. L'issue « non concluant » subsiste quand l'intervalle chevauche le seuil. Ce n'est pas une troisième hypothèse : c'est un défaut de précision, dont la probabilité est bornée par le calcul de taille. |
| A-10 | Le contrôle de profondeur repose sur une idée fausse. | ACC | Contrôle par une idée vraie mais inerte (voir E-1 pour *ex falso*). |
| A-p1 | Plafond ln(M/3) ; ex æquo. | ACC | Certification par borne supérieure ; voir l'identité I1. |
| A-p2 | VPP ≈ 0,14 à prévalence 0,01. Calcul refait : 0,008/0,0575 ≈ 0,139. | ACC | Fausses alertes dérivées d'un FDR cible (I2). |
| A-p3 | McNemar quand q → 0 ; enveloppe max_b biaisée. | ACC | Enveloppe abandonnée. q est mesuré au pilote. |
| A-p4 | d n'a pas de variance si S réussit presque toujours ou presque jamais. | ACC | K_test est calibré pour que S, sans idée ajoutée, résolve entre 0,2 et 0,8 (illustratif). |
| A-p5 | Le quotient de E5 n'est pas borné. | ACC | Remplacé par des différences. |
| A-p6 | E7 n'est faisable qu'avec de petits modèles. | ACC comme limite | Non corrigeable ; déclaré en (c). |
| A-c | Cinq contrôles : différent-pas-meilleur, spam, paires proches mais distinctes, vrai-inerte et table recopiant K_train, Q′ disjoint. | ACC (les cinq) | Intégrés en (b). |

### Critiques de C

| ID | Critique | Verdict | Conséquence |
|---|---|---|---|
| C-1 | E3 ignore les relations non monotones et décroissantes ; le contre-exemple ρ_S(U, (U − ½)²) = 0 est exact. | ACC | Le test porte sur les écarts de moyennes conditionnelles par strate de n. |
| C-2 | En E7, la présence dans le corpus n'est pas assignée au hasard. | ACC | E7′. |
| C-3 | Deux comparateurs possibles : choisi sur le développement, ou choisi après coup. | ACC | Pas d'enveloppe ; un contraste par ligne de base. |
| C-4 | En E5, la réallocation mesure une politique budgétaire. | TEST | Deux bras distincts : critique masquée et critique retirée avec réallocation. |
| C-5 | E6 est différé après E4. | ACC | E6′ se fait au pilote, avant E4′. |
| C-b (E6) | Un intervalle qui traverse la tolérance ne prouve pas l'innocuité. | ACC | Test d'équivalence (deux tests unilatéraux ; référence à vérifier). |
| C-b (E7) | Même si la présence détectée égale l'exposition, la difficulté latente confond. | ACC | Randomisation. |
| C-b (E8) | Les régions de probabilité d'inclusion nulle ne sont pas couvertes. | ACC | La revendication est restreinte à la population de régions échantillonnée. |
| C-c | Identités valides inertes, permutation intra-famille, classifieur limité au gabarit, critique masquée à candidats constants. | ACC | Intégrés en (b). |

### Critiques de D

| ID | Critique | Verdict | Conséquence |
|---|---|---|---|
| D-1 | L'enveloppe par problème joue contre le système ; McNemar ne s'applique pas à des fractions. | ACC | Bootstrap apparié par problème sur Y_p. |
| D-2 | Redéfinir d conditionnellement à n injecte la loi de Q dans l'instrument. | ACC en partie, REJ en partie | ACC : je retire la redéfinition. REJ : E3 garde son sens. Il décrit une propriété du couple (Q, domaine), ce que soutient ma thèse (P3). |
| D-3 | P_Q n'est pas estimé sur des tirages disjoints ; −log 0 ; E7 ne se transfère pas aux 70B fermés. | ACC | Tirages de référence disjoints des runs ; borne supérieure ; limite déclarée. |
| D-b1 | n̂ sans régularisation perd le contrôle de l'erreur de type I ; avec γ > 0, la puissance s'annule. | ACC | E2 utilisait déjà la règle de trois, mais E4 ne fixait aucun estimateur. Désormais : certification par borne supérieure seulement (I1). |
| D-b2 | E3 souffre d'une inflation de zéros. | ACC | Tirage enrichi par strate. |
| D-b3 | Les frontières d'O'Brien-Fleming supposent un comportement gaussien, faux à petits effectifs discrets. | ACC | Analyse intermédiaire seulement après au moins 20 paires discordantes (illustratif). Frontières calibrées par simulation. |
| D-b4 | E6 : décalage δ_split entre K_train et K_test ; E7 : quotient non borné. | ACC | Partition aléatoire de K ; différences. |
| D-c1 | A/A multi-copies contre l'enveloppe. | TEST | Exécuté comme démonstration. Il doit montrer le biais négatif, ce qui documente l'abandon de l'enveloppe. |
| D-c2 | Auto-formalisateur dégénéré. | ACC | Bras de contrôle négatif en Lean. |
| D-c3 | Injection randomisée. | ACC | E7′. |

### Critiques de E

| ID | Critique | Verdict | Conséquence |
|---|---|---|---|
| E-1 (*ex falso*) | Une prémisse fausse rend toute cible dérivable. | ACC | Seules des idées validées mécaniquement passent au solveur S : lemme prouvé, axiomes en liste blanche. En monde planté, une loi est évaluée par prédiction et non comme axiome. |
| E-1 (collision) | ρ(n, d \| valide) subit un biais de collision. | REJ en partie | L'estimande est conditionnel à la validité par définition : seules les idées valides comptent. Je le lis comme une description, jamais comme une relation structurelle. Le biais de collision n'affecte que cette dernière lecture. |
| E-2 (pass@k) | pass@k rompt la comptabilité des coûts pour un système doté d'un sélecteur interne. | ACC | Retiré. |
| E-2 (P_Q non budgété) | P_Q n'est estimé que sur 20 problèmes, alors que E4 en compte 120 à 200. | ACC | Phase P ajoutée au plan, avec son coût. |
| E-2 (puissance E4) | Puissance 0,15 à n = 118. | ACC | Erreur de ma part : n = 118 testait contre 0, alors que la règle teste contre Δ_min. Recalcul en I3. |
| E-4 | E6 confond l'optimisme sur K_train et la corruption de la mesure. | ACC | Trois jeux de conséquences et un bras de fuite délibérée. |
| E-5 | Coût de E8 non imputé ; fausses alertes agrégées en E1. | ACC | Coût imputé ; un plafond par strate. |
| E-b (fusion/scission) | Une canonicalisation imparfaite biaise n̂ dans les deux sens. | ACC | E0′ mesure les deux taux. |
| E-b (juge) | Aucun effet ≤ δ_J n'est jugeable. | ACC | Le juge est exclu de toute quantité primaire. |
| E-c5 | Cibles postérieures à la coupure, appariées en difficulté. | ACC comme analyse secondaire ; REJ comme substitut | La date confond difficulté et dérive de notation. |
| E-c6 | A/A sur l'enveloppe exacte. | Traité en D-c1 | — |

---

## (b) Expériences corrigées

### Identités de conception

Statut : arithmétique sur paramètres HYPOTHÈSE, chiffres illustratifs.

**I1 — Certifier l'étroitesse coûte de la sensibilité.**
- Déclarer p < τ exige 0 occurrence en M tirages, pour chaque membre du panel (R membres) et chaque classe testée (m classes). Il faut M ≳ ln(R·m/α)/τ.
- Une classe de vraie probabilité p est certifiée avec probabilité e^(−pM).
- Pour obtenir 0,8, il faut p ≲ 0,223·τ / ln(R·m/α).
- Avec R = 3, m = 60 et α = 0,05, on a ln(3 600) ≈ 8,2. « Étroit certifié » signifie alors une rareté de l'ordre de **37 fois τ**.
- Je l'écris dans la définition plutôt que de le découvrir à l'analyse. Pour aller au-delà, il faut des estimateurs d'événements rares (référence à vérifier pour les LM).

**I2 — Fausses alertes tolérables.**
- FPR ≤ s·π·q* / ((1 − π)(1 − q*)).
- Avec π = 0,01, s = 0,8 et un FDR cible q* = 0,2, on obtient FPR ≈ 0,002 par strate.
- Le certifier sans aucune alerte demande au moins 1 500 négatifs par strate (3/0,002).
- **Dépendance non résolue** : π est inconnu. J'encadre π par un intervalle préenregistré et je prends le plafond correspondant au π le plus bas.

**I3 — Taille de E4.**
- n ≈ (z_{α/2} + z_β)² · (q − Δ²) / (Δ − θ₀)².
- Avec q = 0,25, Δ = 0,15 et θ₀ = 0,05 : n ≈ 178 problèmes pour un contraste à puissance 0,8.
- Le test d'intersection-union porte sur 3 contrastes. Avec une puissance de 0,93 par contraste : n ≈ 11,8 × 0,2275 / 0,01 ≈ **270 problèmes**.
- À recalculer avec le q mesuré au pilote.

### E0′ — Canonicalisation (CPU)

- **H_A** : la canonicalisation c(·) est fidèle. Elle fusionne au moins 0,98 des paraphrases **et** fusionne à tort au plus 0,02 des paires proches mais distinctes (seuils illustratifs).
- **H_B** : l'une des deux bornes est violée.
- **Jeux de test** : paraphrases mécaniques, obfuscations produites par les modèles eux-mêmes (idée que E adresse à A), paires distinctes à une constante ou un terme près.
- **Issues** :
  - H_B falsifie la validité de n̂, quel que soit le sens de l'erreur. On arrête avant E2′.
  - H_A falsifie le biais de fusion et de scission décrit par E.

### E1′ — Contrôle positif de l'instrument (mondes plantés)

**Dispositif.**
- 200 positifs, dont une seconde loi profonde **non documentée**. Elle doit être créditée.
- Leurres produits par une autre grammaire que les positifs. Trois strates : rare-stérile, commun-utile, commun-stérile. Au moins 1 500 leurres par strate.
- La profondeur d est comparée à **deux** références : S sans idée ajoutée, et S avec une idée vraie-inerte de même complexité. Une idée n'est profonde que si elle dépasse les deux.

**Hypothèses.**
- **H_A** : sensibilité ≥ 0,8, **et** fausses alertes ≤ 0,002 dans chaque strate, **et** un classifieur limité au gabarit a une AUC ≤ 0,55 (illustratif).
- **H_B** : l'une des conditions échoue.

**Contrôles.** Permutation des étiquettes à l'intérieur des familles de construction. Table recopiant K_train, qui doit obtenir d ≈ 0.

**Issues.**
- H_B : les scores suivent la construction ou la surface, et l'instrument est révisé.
- H_A : falsifie seulement l'hypothèse de bogue ou de sensibilité à la surface. Cette issue **ne valide pas** le construit.

### E2′ — Dépendance de l'étroitesse à la référence

**Dispositif.**
- Ensemble de classes fixé à l'avance : énumération de la grammaire, plus les nominations d'un quatrième modèle extérieur au panel.
- Chaque Q_ref,i reçoit le même M, sur des tirages disjoints de tout run.

**Hypothèses.**
- **H_A** : le taux de désaccord sur le drapeau « étroit certifié » entre références dépasse de moins de ε = 0,10 le plancher « même Q, deux graines ».
- **H_B** : il le dépasse de plus de ε.

**Issues.**
- H_B, et H_B persiste sous une seconde canonicalisation : « étroit » doit être indexé par la référence. Le cadrage « recherche ordinaire » est alors mal posé sans indice.
- H_A : falsifie la dépendance à la référence, pour ce panel seulement.

### E3′ — Rareté et profondeur (descriptif)

- **Dispositif** : tirage stratifié en n par une loi de proposition, puis repondération. Ajustement de complexité identique pour n et pour d. Estimande conditionnel à la validité.
- **H_A** : max_s |E[d | strate s] − E[d]| ≤ ε.
- **H_B** : cet écart dépasse ε.
- **Issues** :
  - H_B : les axes sont dépendants sous ce Q. On publie la loi jointe, **sans redéfinir d**.
  - H_A : la cellule jointe est un objet propre pour ce couple (Q, domaine).

### E6′ — Fuite par rétroaction (pilote, avant E4′)

**Dispositif.**
- K est partitionné **au hasard** en trois jeux : K_train (renvoyé au générateur), K_test (scellé), K_vierge (ouvert une seule fois).
- Trois bras : retour, silence, fuite délibérée de K_test (contrôle positif).

**Hypothèses.**
- **H_A** : |[d(K_test) − d(K_vierge)]_retour − [d(K_test) − d(K_vierge)]_silence| ≤ ε, par test d'équivalence.
- **H_B** : cet écart dépasse ε.

**Règle de sensibilité.** Le bras de fuite délibérée doit dépasser ε. Sinon le test n'a pas de sensibilité et on arrête.

**Issues.**
- H_B : le signal renvoyé passe en « retenu ».
- H_A : falsifie la corruption de la mesure par ce signal.
- L'écart d'optimisme K_train − K_test n'entre pas dans la décision.

### E4′ — Comparaison principale

**Bras**, tous avec k nominations choisies avant l'ouverture du coffre :
- le système ;
- best-of-N mono-modèle, avec le même vérificateur et le même sélecteur ;
- l'énumérateur ou PySR ;
- l'échantillonnage aléatoire, seulement dans un espace formel ;
- « différent mais pas meilleur » ;
- « spam » : k idées valides et rares tirées au hasard ;
- placebo : rôles attribués au hasard, sans interaction ;
- en Lean, un auto-formalisateur dégénéré.

**Quantité primaire.**
- Y_p est la fraction des s graines où au moins une nomination est à la fois valide, certifiée étroite sous Q_ref (I1), et profonde au sens de E1′.
- Unité : le problème.

**Coût.**
- Comptabilité complète : jetons de tous les agents, appels au vérificateur, temps mural.
- Pour l'énumérateur, l'égalisation se fait en coût monétaire, et non en nombre d'appels au vérificateur.
- Coût de prospection et estimation de P_Q imputés aux bras concernés.

**Règle de décision.**
- Test d'intersection-union. Pour chaque ligne de base b : **H_A,b** : Δ_b > θ₀ ; **H_B,b** : Δ_b ≤ θ₀.
- Bootstrap apparié par problème. Plan séquentiel à frontières simulées. Pas d'enveloppe.

**Contrôles.**
- A/A sur la procédure complète : choix de la référence, analyses intermédiaires, arrêts.
- A/A multi-copies contre l'enveloppe (D-c1), comme démonstration.
- Le bras spam doit rester proche de 0. L'auto-formalisateur dégénéré doit obtenir d ≤ 0.
- Si le bras « différent mais pas meilleur » vérifie Δ > θ₀, l'interprétation « découverte » est falsifiée.

**Issues.**
- Toutes les bornes inférieures au-dessus de θ₀ : H_B falsifiée.
- Une borne supérieure sous θ₀ : H_A falsifiée.

### E5′ — Attribution

**Bras**, à coût égal :
1. système complet ;
2. critique masquée : message neutre portant sur le même problème, de même longueur, avec les mêmes candidats et le même sélecteur ;
3. critique retirée, jetons réalloués à la génération (politique budgétaire) ;
4. une seule famille de modèles avec plusieurs personas ;
5. best-of-N.

**Hypothèses.**
- **H_A** (« l'interaction contribue ») : (1 − 2) > θ₀ **et** (1 − 5) > θ₀.
- **H_B** : l'un des deux contrastes est ≤ θ₀.

Le contraste (1 − 3) répond séparément à la question de la politique budgétaire. Il n'y a plus aucun quotient.

### E7′ — Rappel ou recherche

- **Dispositif** : paires de cibles synthétiques jumelles. On tire au hasard la moitié de chaque paire pour l'injecter par entraînement continu dans un modèle ouvert.
- **H_A** : succès(injectées) − succès(retenues) ≤ ε.
- **H_B** : cet écart dépasse ε.
- **Issues** :
  - H_B : la rétrodiction exige une certification d'exposition cible par cible. Avec des modèles fermés, elle est retirée du plan.
  - H_A : falsifie l'effet de rappel, pour ce modèle et cette dose d'injection.
- **Analyse secondaire seulement** : cibles postérieures à la coupure.

### E8′ — Choix des régions

- **Dispositif** : la règle est apprise sous Q′ disjoint de Q_ref, puis évaluée sur des régions tenues à l'écart. Le coût de prospection est imputé.
- **H_A** : rendement net par unité de coût de la règle − rendement net d'un tirage aléatoire de régions > θ₀.
- **H_B** : cette différence est ≤ θ₀.
- La revendication est restreinte à la population de régions échantillonnée.

### Plan révisé

| Phase | Contenu | Arrêt si | Taille | Coût (illustratif) |
|---|---|---|---|---|
| 0 | E0′, préenregistrement | H_B en E0′ | ~2 000 paires | CPU |
| 1 | E1′ | H_B | 200 positifs, ≥ 1 500 leurres par strate | CPU + petit modèle |
| 2 | E2′ + E3′ | E2′ en H_B : pas d'arrêt, affirmations indexées par la référence | 30 000 tirages × 20 problèmes × 3 Q_ref | ≈ 50 h GPU |
| 3 | Pilote avec le système : A/A, E6′, spam, mesure de q | A/A au-dessus du nominal ; contrôle de fuite insensible | 30 problèmes × 3 bras × 5 graines | ≈ 9·10⁸ jetons, 10³–5·10³ $ |
| 4 | E7′ | — | ~200 paires jumelles | quelques centaines d'h GPU |
| P | Estimation de P_Q pour les problèmes de E4′ | — | 270 problèmes × 3 × 30 000 × ~10³ jetons ≈ 2,4·10¹⁰ jetons | ≈ 680 h GPU, ≈ 1,4·10³–3,4·10³ $ |
| 5 | E4′ séquentiel | Frontières simulées | ~270 problèmes | ≈ 2·10⁴–7·10⁴ $ |
| 6 | E5′ | Seulement si E4′ conclut H_A | Mêmes problèmes, 5 bras | Ordre de la phase 5 |
| 7 | E8′ | H_B : abandon du choix ciblé | Régions 50/50 | — |

---

## (c) Réponse à la question de l'arbitre

**Ce qui est établi.**
- **Aucun fait empirique.** Le bloc FAITS ne contient aucun fait étiqueté. Le seul contenu factuel est le contexte du projet (RAPPORTÉ).
- **Le biais d'auto-préférence des juges LM est RAPPORTÉ dans la littérature** : Zheng et al., 2023 ; Panickssery, Bowman & Feng, 2024. Je ne l'ai pas vérifié ici.
- **Des identités sur les estimateurs, qui contraignent toute conception.** Leurs paramètres sont HYPOTHÈSE.
  - (i) Certifier l'étroitesse par zéro occurrence ne détecte, à sensibilité 0,8, que des classes environ 37 fois plus rares que le seuil affiché (I1).
  - (ii) À prévalence 0,01, des fausses alertes à 0,05 donnent une VPP d'environ 0,14 ; il faut viser environ 0,002 (I2).
  - (iii) Une enveloppe des lignes de base prise par problème est biaisée contre le système.
  - (iv) Mon n = 118 était faux pour ma propre règle : il faut de l'ordre de 270 problèmes (I3).

**Ce qui n'est pas établi** (tout est HYPOTHÈSE) :
- que la classe « étroit ∧ profond » soit non vide dans un domaine réel ;
- que l'étroitesse soit stable d'une référence à l'autre ;
- que la profondeur se sépare de la rareté ;
- que renvoyer la validité au générateur soit sans effet sur la mesure ;
- que le système batte best-of-N à coût et vérificateur égaux ;
- que les classements se transfèrent des mondes plantés au domaine formel ;
- que la rétrodiction soit utilisable avec des modèles à données fermées.

**Où le cadrage reste faux**, selon moi (HYPOTHÈSE) :
- « rarement atteint par la recherche ordinaire » n'est pas défini sans une référence nommée et disjointe des bras ;
- « finds » mêle recherche et sélection tant que le nombre de nominations n'est pas fixé ;
- un harnais général est probablement hors de portée ; seul un harnais par domaine et par référence est défendable.

**Expérience à faire en premier : E2′, précédée de son prérequis E0′.**
- E0′ coûte quelques heures CPU ; E2′ environ 50 h GPU (illustratif).
- C'est l'expérience la moins chère qui puisse falsifier le cadrage lui-même, et pas seulement mon instrument :
  - si le désaccord inter-références dépasse le plancher dû au bruit et persiste sous une seconde canonicalisation, « étroit » n'a de sens qu'indexé par une référence, et toute la question 1 doit être reformulée ;
  - dans le cas contraire, la dépendance à la référence est falsifiée pour ce panel, et E1′ puis le pilote deviennent les priorités.
- E1′ vient ensuite. C'est un contrôle positif nécessaire, mais il ne peut falsifier qu'un bogue ou une sensibilité à la surface.

**Confiance** (subjective) :
- 0,7 que les corrections suppriment les défauts relevés par A, C, D et E ;
- 0,4 que E4′ soit jugeable avec environ 270 problèmes, car cela dépend de q, encore inconnu ;
- 0,5 que E2′ conclue H_B.

FIN-DE-CELLULE