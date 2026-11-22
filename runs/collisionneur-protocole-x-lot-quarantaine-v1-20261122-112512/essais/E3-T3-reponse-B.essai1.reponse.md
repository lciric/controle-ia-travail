# Proposition B — Tour III.3 : réponse aux critiques

## 0. État des pièces

- **Pièces absentes.** Les blocs FAITS et QUESTION sont identiques. Les « notes retirées » et la « réponse 23 de Fable » sont absentes ; je n'en invente pas le contenu.
- **Pièces reçues.** Les critiques A, C, D, E et F sont présentes et se terminent par leur marqueur. Je ne recalcule aucune empreinte et je ne réponds qu'aux sections « Sur la proposition B ».
- **Statuts chez les critiques.** C et E marquent `VÉRIFIÉ` l'intégrité des pièces sans pouvoir recalculer les empreintes. Je ne reprends pas ce statut.
- **Statuts chez B.** Ma convention ne change pas : ce que l'énoncé affirme est RAPPORTÉ, ce qu'il laisse implicite est HYPOTHÈSE. Les critiques que j'accepte restent des HYPOTHÈSES ; les accepter ne les rend pas vérifiées. Les chiffres sont illustratifs ; « calculé » signale une arithmétique refaisable.
- **Arguments empruntés.** Quand je me sers d'un argument d'une autre proposition, je le nomme : l'argument A1 (déterminisme) et la règle à marge de D. Je ne les fusionne pas avec mes propres arguments.

## (a) Verdict sur chaque critique

Légende : **Acc.** = acceptée ; **Rej.** = rejetée, avec la raison ; **Test** = transformée en test (voir (b)).

### Audit du critère de passage (R1′)

| Réf. | Critique | Verdict | Conséquence pour B |
|---|---|---|---|
| A-a2 | Tendance commune liée au cycle : « nombre de cycles » doit être partialisé, pas seulement battu. | Acc. | R1′ est retiré et remplacé par E6′. |
| A-a2 (suite) | Si l'audit donne ρ ≈ 0, l'équipe révise son critère, et le lot entre dans le critère de passage. | Acc. | Règle ajoutée : l'issue de l'audit ne peut modifier aucun critère appliqué aux détecteurs évalués sur ce lot. Un critère révisé exige un nouveau lot. |
| A-b | \|ρ\| critique ≈ 0,65 pour K = 10 (calcul de A) ; l'autocorrélation réduit encore K. | Acc. | Sur une seule campagne, l'audit est déclaré **non jugeable**. |
| A-c | Permuter l'ordre des cycles. | Acc. | Témoin de E6′. |
| C-a1, C-c2 | Maturation initiale ; calculer sur les accroissements ou sur la fenêtre terminale. | Acc. | Intégré à E6′. |
| D-a, D-b | ρ_S > 0 est compatible avec C ⟂ M \| k ; la quantité utile est P(M_τ < m \| τ < ∞). | Acc. | Devient l'estimande principale de E6′, qui exige plusieurs campagnes. |
| D-c | Prédicteur « numéro de cycle » évalué sur de nouvelles campagnes. | Acc. | Témoin de E6′. |
| E-a1, E-b2 | La phase initiale masque une anti-prédiction terminale. | Acc. | Intégré à E6′. |
| E-c2 | Spearman restreint au plateau terminal. | Test, corrigé | Le test de E laisse ρ ∈ ]0 ; 0,3] sans verdict. Je coupe en un seuil unique ρ₀, pré-enregistré. |
| F-a5, F-b | Tendance monotone ; Var(ρ̂_S) ≈ 1/(M−1). | Acc. | Même conséquence. |

### E1 (consultation répétée)

| Réf. | Critique | Verdict | Conséquence pour B |
|---|---|---|---|
| A-a1 | Sous arrêt optionnel, E[Δ] > 0 est acquis ; la marge dépend de n et K ; le résultat ne se transporte pas aux auteurs humains ; ma clause de réfutation n° 1 conclut trop. | Acc. | Clause n° 1 retirée. E1′ mesure une **ampleur** pour une politique scriptée et ne peut plus autoriser une consultation à chaque cycle. |
| C-a4, E-a2, F-a1 | La boucle scriptée minore Δ ; la coupe dans un seul genre soustrait la fuite de genre. | Acc. | E1′ ajoute un troisième genre G″ et une boucle à retour fictif. Le transport aux humains reste une HYPOTHÈSE. |
| C-c3 | Lot témoin d'un genre G″ jamais consulté. | Acc. | Intégré à E1′. |
| D-b | Les lois jointes (C_k, M_k, τ) du substitut et de la cible diffèrent. | Acc. | La portée de E1′ est restreinte au substitut. |
| F-b | Seuil discret au quantile ; complexité de recherche script ≪ humain. | Acc. | Le bootstrap réestime le seuil à chaque tirage ; limite de portée déclarée. |

### E2 (apport de l'état interne)

| Réf. | Critique | Verdict | Conséquence pour B |
|---|---|---|---|
| A-a3 (i), C-b1, E-a3, F-a2 | Les seuils fixés sur le développement donnent des taux de fausses alertes réalisés inégaux sur le lot. McNemar ignore cet écart et la variance du seuil. | Acc. | Test d'égalité des taux réalisés, estimande à taux apparié, et McNemar remplacé par un bootstrap apparié qui réestime les seuils. |
| A-a3 (ii), C-a3, F-a2 | La sonde couche 0 est trop faible. | Acc. | Elle est rétrogradée en plancher. Témoin principal : relecture du texte par les **mêmes poids** (argument A1 de A, que j'utilise). |
| A-a3 (iii) | Si une consigne d'induction est en contexte, l'état interne la lit, et (ii) est vrai par construction. | Acc. | Deux relectures : texte visible seul, et contexte complet. |
| E-a5, E-c1, F-c2 | L'intervention au point de bifurcation est lisible dans les états. | Test | Contrôle « bifurcation à blanc » de E2′. |
| F-a2 | Combiner deux signaux donne un gain « par construction ». | **Rej. en partie** | Si I ⟂ Y \| T, une fusion apprise sur le développement n'a pas de gain attendu à fausses alertes fixées hors-genre ; elle peut même perdre. Le gain n'est donc pas acquis par construction. Le confondant de diversification existe néanmoins : j'ajoute un bras T+T₂. |
| E-b3, F-b | DeLong : courbes ROC croisées, gain dilué hors de [0, α₀]. | Acc. | Critère secondaire remplacé par l'AUC partielle sur [0, α₀] (McClish, 1989, « Analyzing a portion of the ROC curve », *Medical Decision Making*, de mémoire). |
| D-a | Un intervalle contenant 0 est traité comme une réfutation. | Acc. | Règle à marge avec trois issues (voir (b)). |
| D-b | La latence mesurée chez les seuls détectés n'identifie pas le délai. | Acc. | Latence traitée comme une durée censurée à la fin de trajectoire (Kaplan-Meier). |
| A-b | Pas de rejet possible si m < 6 paires discordantes ; coefficient de variation ≈ 58 % pour α = 0,01 et n_h = 300 (calculs de A). | Acc. | Conditions de non-jugeabilité vérifiées en E0. |
| D-c | Il faut des trajectoires saines du genre cible. | Acc. | Préalable S2, vérifié en E0. |

### Paires jumelles

| Réf. | Critique | Verdict | Conséquence pour B |
|---|---|---|---|
| C-a2 | Le lot préexistant n'a pas d'instantanés. | Acc. | Les jumelles sont réservées aux données neuves (substitut ou complément). Pour le lot existant, (ii) exige des états archivés ou un rejeu ; c'est le présupposé de E, relayé par A. Vérification en E0. |
| C-a2 | Une différence nulle sur [1, t₀] interdit de mesurer une détection avant t₀. | **Rej.** | Une alerte avant t₀ n'est pas une détection. Le préfixe commun sert de contrôle pré-causal intégré : tout écart sur [1, t₀] signale un artefact. |
| C-a2, F-a2 | Apparier sur la longueur après bifurcation tronque P(X \| Y=0) (collisionneur). | Acc. | Appariement supprimé. Seul l'état de bifurcation, antérieur au traitement, est commun ; la longueur est rapportée comme covariable. |
| E-a5 | Le préfixe identique dilue les moyennes temporelles. | Acc. | Scores calculés en ligne, pas à pas ; latence mesurée depuis t₀. |

### E3 (écart à la loi publiée)

| Réf. | Critique | Verdict | Conséquence pour B |
|---|---|---|---|
| A-a5, A-b | Le contrôle en distribution ne calibre pas la bande hors-genre ; avec un seul genre, τ² n'est pas identifiable. | Acc. | Ce contrôle ne vérifie que l'implémentation. La conclusion est conditionnelle au caractère prédictif de la bande publiée. |
| C-b3, D-a, D-b, E-a4, E-b1, E-c3, F-a4, F-b | Points dépendants, test binomial invalide, grappe unique, écart de signe invisible au comptage. | Acc. | E3′ : loi nulle par Monte-Carlo d'un lot unique, statistiques signées. |

### E4 (biais d'exposition)

| Réf. | Critique | Verdict | Conséquence pour B |
|---|---|---|---|
| A-a4 | H_A conjonctive, donc hypothèses non exhaustives ; témoin de difficulté au plancher ; non-rejet traité comme équivalence. | Acc. | Scindé en E4a et E4b ; test d'équivalence à marge. |
| C-b2, F-a3 | Une fuite de genre est invisible ; le score mécanique W est dégénéré. | Acc. | Témoin G″ ; ajustement par W supprimé. |
| D-a, D-c, F-a3, F-b, F-c3 | L'exposition n'est pas aléatoire ; variance de référence fausse sauf si n_non-vu = 3·n_vu (calculé, F) ; versions antérieures à l'exposition. | Acc. | Placebo sur versions gelées avant exposition ; pseudo-expositions de taille n_vu. |

### E5 (puissance) et points transversaux

| Réf. | Critique | Verdict | Conséquence pour B |
|---|---|---|---|
| C-b4, D-a, D-b, F-a5 | Corrélation et taux de discordance empruntés au développement. | Acc. | Courbe de puissance sur une grille (π_d, ρ_Q). |
| D-b | La corrélation entre détecteurs peut **améliorer** la précision. | Acc. | Ma phrase de III.1 (« une différence demande en général plus de cas ») est retirée. R4 devient conditionnel à π_d. |
| — | Autocritique : E5 est un calcul, pas une expérience à deux issues. | — | E5 devient E0, préalable. |
| A-a6 | La séparabilité du genre lit le lot avant gel. | Acc. | Déplacée dans la consultation unique. |
| D-b | Un classifieur de domaine peut être au hasard alors que P(Y \| X) change. | Acc. | Clause de réfutation n° 2 corrigée (voir (c)). |
| D-a | « Une fois par affirmation » laisse fuir si l'affirmation suivante est choisie après le premier résultat. | Acc. | (i), (ii) et tous les contrastes sont pré-enregistrés ensemble, pour une ouverture unique. Tout ajout ultérieur est exploratoire. |

## (b) Expériences corrigées

**Règle de décision commune.** Elle reprend la forme de D. Pour chaque contraste g, une marge m est pré-enregistrée, avec H_A : g ≤ m contre H_B : g > m, et un intervalle à 95 %.

- Un intervalle entièrement sous m réfute H_B.
- Un intervalle entièrement au-dessus de m réfute H_A.
- Un intervalle à cheval sur m est une **issue déclarée d'avance** :
  - si sa demi-largeur observée dépasse celle prédite par E0, il réfute le dimensionnement de E0 ;
  - sinon, c'est un non-verdict compté comme tel. E0 borne sa probabilité, par exemple à au plus 20 % à l'effet prévu (illustratif).

### E0 — Préalable : inventaire et calcul (pas une expérience)

**Inventaire factuel, sans ouvrir les étiquettes :**
1. Présence et nombre de cas honnêtes dans le lot (S2).
2. États internes archivés, ou contexte complet journalisé permettant un rejeu.
3. Journal d'accès.
4. Versions de détecteurs gelées et hachées avant toute exposition.

**Puissance.** Courbes de puissance pour E2′ sur la grille π_d × ρ_Q (bornes illustratives). La consultation n'a lieu que si la puissance atteint au moins 0,8 au point pessimiste pré-enregistré.

**Conditions de non-jugeabilité** :
- n_dég·π_d ≥ 6 (A) ;
- environ 1 500 honnêtes pour estimer un taux de 1 % à ±0,5 point (calculé en III.1).

Si une condition échoue, l'affirmation correspondante est déclarée non jugeable sur ce lot. Il faut alors **compléter ou refaire le lot avant ouverture**.

### E2′-0 — Le déterminisme tient-il ? (données de développement, sans le lot)

- **H_A :** les activations enregistrées pendant la génération sont égales, à une tolérance numérique pré-enregistrée près, à celles recalculées par les mêmes poids sur le contexte complet journalisé.
- **H_B :** elles diffèrent au-delà de cette tolérance.
- **Tolérance.** Par exemple 10⁻² en bfloat16 (illustratif), étalonnée sur deux recalculs identiques afin de mesurer le non-déterminisme d'exécution par lots.
- **Ce que chaque issue réfute :**
  - **H_A vraie.** I(Y ; Z_int \| X_complet) = 0, et tout gain mesuré en (ii) vient d'un contexte que le lecteur de texte ne voit pas, ou de sa lecture moins efficace (causes 1 et 2 de l'argument A1). De plus, des états absents du lot sont **reconstructibles** à partir du contexte journalisé, ce qui lève la condition « états archivés » de E0.
  - **H_B vraie.** Le contexte journalisé est incomplet, ou l'agent garde un état hors contexte. La reconstruction est impossible, et (ii) sur le lot exige des états archivés.
- **Antériorité, sur l'information utilisable sous contrainte de calcul :** Xu, Zhao, Song, Stewart, Ermon (2020), « A Theory of Usable Information Under Computational Constraints », citée par E (de mémoire, à vérifier).

### E2′ — Décomposition de l'apport interne (affirmation ii)

**Bras comparés**, tous gelés et hachés avant ouverture :

| Bras | Contenu |
|---|---|
| T | Détecteur textuel seul. |
| T+T₂ | Second lecteur textuel indépendant (diversification). |
| T+Z′_vis | Mêmes poids que l'agent, relisant uniquement le texte fourni à T. |
| T+I | État interne réel. |
| Planchers | Couche 0, poids aléatoires, étiquettes permutées. |

**Contrastes principaux :**
- g₁ = TPR(T+Z′_vis) − TPR(T), soit le gain de lecture du même texte ;
- g₂ = TPR(T+I) − TPR(T+Z′_vis), soit le gain dû au contexte invisible pour T.

**Estimande.** TPR à taux de fausses alertes **réalisé** égal sur le lot. Les seuils sont fixés sur une moitié des honnêtes du lot et l'évaluation porte sur l'autre moitié ; ce découpage est pré-enregistré et reste interne à la consultation unique. Le taux obtenu avec les seuils du développement est rapporté à part.

**Test préliminaire d'égalité des taux réalisés :**
- H_A : |α_Q(T+I) − α_Q(T)| ≤ ε ;
- H_B : écart > ε (ε = 0,01, illustratif).

H_B invalide toute lecture faite aux seuils du développement.

**Inférence.** Bootstrap apparié qui rééchantillonne à la fois les honnêtes de développement et le lot, avec réestimation des seuils. Critère secondaire : AUC partielle sur [0, α₀].

**Contrôle « bifurcation à blanc »** (données neuves seulement). Deux branches honnêtes issues du même état, dont l'une subit le mécanisme de bifurcation sans dégradation.
- H_A : AUROC interne entre les deux branches dans [0,45 ; 0,55] ;
- H_B : hors de cet intervalle (seuils illustratifs).

H_B invalide les paires jumelles comme support de (ii).

**Contrôle positif.** Une dégradation visible dans le journal doit être détectée par tous les bras.

**Lecture.** (ii) est **décomposée** :
- g₁ > m et g₂ ≤ m : l'interne ajoute par sa capacité de lecture, non par une information privée ;
- g₂ > m : du contexte que T ne voit pas porte le signal, et ce contexte doit être nommé ;
- T+T₂ égalant T+I : l'apport est de la diversification.

### E1′ — Ampleur de l'inflation (substitut seulement)

**Plan.**
- Deux boucles scriptées, répétées sur R partitions (R illustratif).
  - L⁺ consulte G′-consulté à chaque cycle.
  - L⁰ a un retour fictif : mêmes candidats, budgets et règle d'arrêt, mais étiquettes permutées.
- Les détecteurs finaux sont évalués sur G′-scellé et sur G″, un genre disjoint jamais consulté.

**Contrastes :**
- Δ_inst = [consulté − scellé]_{L⁺} − [consulté − scellé]_{L⁰} ;
- Δ_genre = [scellé − G″]_{L⁺} − [scellé − G″]_{L⁰}.

Chaque contraste suit la règle commune : H_A : Δ ≤ m contre H_B : Δ > m.

**Portée.**
- E1′ borne l'inflation **de cette politique scriptée**.
- Une issue H_A n'autorise pas une consultation à chaque cycle par des humains.
- Une issue H_B ne quantifie pas l'inflation humaine. Que celle-ci soit au moins égale à l'inflation scriptée est une HYPOTHÈSE.

**Coût.** Environ 100 GPU-heures (illustratif).

### E3′ — Écart à la loi (affirmation i)

- **Préalable.** S4 est levée : loi nommée, paramètres fixés hors lot.
- **Loi nulle.** Monte-Carlo de lots uniques simulés sous la loi, avec son incertitude publiée, sur lesquels on évalue **toute** la lignée gelée.
- **Statistiques.** Résidu standardisé moyen **signé** et résidu absolu maximal.
- **Hypothèses.** H_A : |biais| ≤ m contre H_B : |biais| > m.
- **Contrôle de calibration.** Le taux de rejet sous la loi nulle simulée doit être au plus α.
- **Portée.** Ce genre seul. τ² n'est pas identifiable, donc l'écart n'est interprétable que si la bande publiée est prédictive, c'est-à-dire si elle inclut la dispersion entre contextes.

### E4a et E4b — Exposition (question 3)

**Condition d'exécution.** Il faut des versions gelées **avant** l'exposition. Sans elles, l'expérience est non jugeable, et la règle de décision devient : déclasser la partie exposée, ou refaire le lot.

**E4a.** e = gain(vu) − gain(non-vu) entre une version antérieure et une version postérieure à l'exposition, ce qui donne une double différence.
- H_A : |e| ≤ m (équivalence) ;
- H_B : |e| > m.
- Loi de référence : pseudo-expositions de taille n_vu, tirées selon le mécanisme historique de sélection s'il est connu, et placebo entre deux versions antérieures à l'exposition.

**Fuite de genre.** Même double différence, mais entre le lot et G″.

**E4b.** d = e_interne − e_textuel. H_A : d ≤ m contre H_B : d > m. E4b est défini indépendamment de E4a, ce qui rend les deux tests exhaustifs. Il teste R3, qui reste une HYPOTHÈSE.

### E6′ — Audit du critère de passage

- **Estimande.** P(M_τ < m \| τ < ∞) sur C campagnes, et Spearman partiel en tenant compte du cycle, calculé sur les accroissements et dans la fenêtre terminale.
- **Hypothèses.** H_A : ρ_terminal ≤ ρ₀ contre H_B : ρ_terminal > ρ₀.
- **Témoins.** Prédicteur « numéro de cycle » sur de nouvelles campagnes ; ordre des cycles permuté.
- **Jugeabilité.** Avec C = 1, l'audit est **non jugeable** et déclaré comme tel.

## (c) Réponse à la question de l'arbitre

**Ce qui est acquis.** Ce sont des conséquences formelles, vérifiables par calcul ; rien n'est empirique sur cette équipe.

1. **Arrêt optionnel.** Il biaise vers le haut le score au passage, même avec une lecture unique (argument A3 de A).
2. **Seuils du développement.** Ils ne garantissent pas un taux égal de fausses alertes sur un autre genre.
3. **Un seul genre.** La variance entre genres n'est pas identifiable.
4. **Déterminisme.** Si Z_int est fonction du contexte complet, alors I(Y ; Z_int \| X_complet) = 0. Cela reste conditionnel à l'HYPOTHÈSE A1.
5. **McNemar exact.** Il ne rejette rien avec moins de 6 paires discordantes.

**Ce qui n'est pas établi.**
- Les suppositions S1 à S12 de III.1 restent ouvertes.
- Ampleur de l'inflation dans ce cas.
- Présence de cas honnêtes dans le lot, et existence d'états archivés.
- Identité de la loi.
- Pour (ii) : un gain viendrait-il d'une information privée, d'un contexte invisible pour T ou d'une meilleure lecture du même texte ?

**Réponses mises à jour (HYPOTHÈSES de B).**

| Question | Réponse | Certitude |
|---|---|---|
| Q1 | Portée de (i) et (ii), jamais le critère de passage. L'audit du critère est non jugeable avec une seule campagne. | Élevée pour l'exclusion du critère ; faible pour l'usage en (i). |
| Q2 | Une seule ouverture, pour toutes les affirmations pré-enregistrées ensemble, après gel. | Élevée. E1′ ne peut plus réfuter cette règle ; il en mesure seulement l'enjeu pour une politique scriptée. |
| Q3 | Dépend de l'exposition différentielle datée **et** de l'existence de versions gelées avant exposition. Sans ces versions : déclasser la partie exposée, ou refaire. Ne jamais jeter. | Moyenne. |
| Q4 | En partie. Devient « oui » si E0 montre une puissance insuffisante ou l'absence de cas honnêtes. | Moyenne. |

**Ce qui réfuterait désormais B.**

1. **Clause n° 2, corrigée.** Une séparabilité proche de 1 obtenue par les seuls traits de surface réfute la portée « hors-genre ». Une séparabilité proche de 0,5 ne réfute plus rien.
2. **R3.** E4b donne d ≤ m avec puissance suffisante.
3. **Q4.** E0 dément le « en partie » si la puissance est insuffisante.
4. **(i).** S4 ne peut pas être levée.

**Expérience à faire en premier.** D'abord l'inventaire E0, qui ne coûte presque rien et n'ouvre aucune étiquette. Ensuite **E2′-0**, sur données de développement et sans toucher au lot.

- Si le déterminisme tient, les états absents du lot deviennent reconstructibles, et (ii) se réduit à comparer T+I à T+Z′_vis.
- S'il ne tient pas, (ii) sur ce lot exige des états archivés ; sinon, il faut compléter le lot avant l'ouverture unique.

Chaque issue décide de la forme de toutes les expériences suivantes.

FIN-DE-CELLULE