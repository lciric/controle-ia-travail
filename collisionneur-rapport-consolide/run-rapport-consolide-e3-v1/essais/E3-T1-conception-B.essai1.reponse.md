# Proposition B · Tour III.1 · Audit défensif du rapport consolidé

**État des pièces.**
- F1 est présente.
- La définition de $v$ dans $\Psi(h_t)=[v,\sin v,v^2]$ est absente de la pièce. La fin de cette formule a été lue sur la couche texte du PDF, selon la note de transcription. Je la traite donc comme possiblement incomplète.
- Le tableau de la page 7 omet la Faille 6, la Faille inédite B et les points 2 et 3 de la Faille 5. Je n'en reconstitue rien.
- Les propositions A et C ne me sont pas visibles à ce tour (aveugle). Je n'ai donc rien à attaquer ni à reprendre.

**Convention.** Tout chiffre de F1 garde le statut **RAPPORTÉ**, même quand mon calcul le confirme. Mes calculs sont donnés pour être recontrôlés ; ils ne promeuvent aucun statut.

---

## (a) Ce que la question et le rapport supposent sans que ce soit établi

| # | Présupposé | Statut |
|---|---|---|
| a1 | Les « six failles établies » ont été établies : simulations et décisions P-019/P-021 annoncées, aucun artefact audité joint. | RAPPORTÉ |
| a2 | Les colmatages sont « implémentés » (`memoire_isvd.py`, `politique_endogene.py`, `mitose_spectrale.py`) : seuls les noms de fichiers figurent, pas le code. | RAPPORTÉ |
| a3 | Les quatre « failles inédites » A à D sont des découvertes qui « expliquent en profondeur » les résultats. La pièce elle-même les qualifie d'hypothèses rapportées. | HYPOTHÈSE (rapportée) |
| a4 | « Moins de 1 % du travail causal contre 68 % pour l'état complet » : protocole de mesure non décrit. | RAPPORTÉ, non audité |
| a5 | La conscience d'évaluation provoque une rotation inter-couches. | HYPOTHÈSE |
| a6 | Le nul de P3 vient de l'instrument et non de l'agent. P4 et P3b sont conçus pour trancher ce point ; aucun résultat de P4 ou P3b n'est rapporté dans F1. | HYPOTHÈSE ouverte |
| a7 | La « garantie valable à tout instant ≤ 1 % » est fournie par le seuil conforme. Ce seuil porte en réalité sur un horizon fixe $T$ (voir V1). | RAPPORTÉ ; qualification contestée ici |
| a8 | La loi $\Delta v=g(\hat c-v_0)$ mesure une déférence et non un artefact de mesure. | RAPPORTÉ (ajustement) ; interprétation = HYPOTHÈSE |
| a9 | Les épisodes honnêtes de calibrage sont réellement honnêtes et échangeables avec ceux du déploiement. | HYPOTHÈSE non nommée dans F1 |

---

## 1. Failles déjà documentées par la littérature

| Hypothèse mise en défaut | Référence | Traitée par le rapport ? |
|---|---|---|
| Validité de Ville sous une hypothèse nulle mal spécifiée ou composite (effet épisode) | Ramdas, Grünwald, Vovk, Shafer (2023), *Game-theoretic statistics and safe anytime-valid inference*, Statistical Science | Oui (Faille 1) |
| Le seuil conforme exige l'échangeabilité calibrage/déploiement | Tibshirani, Barber, Candès, Ramdas (2019), *Conformal Prediction Under Covariate Shift*, NeurIPS ; Barber, Candès, Ramdas, Tibshirani (2023), *Conformal prediction beyond exchangeability*, Annals of Statistics | **Non** |
| Le régime intermédiaire entre signal épars (max) et signal dense (somme) | Donoho, Jin (2004), *Higher criticism for detecting sparse heterogeneous mixtures*, Annals of Statistics | Partiellement (Faille 3 traite les deux extrêmes) |
| L'optimalité de CUSUM suppose des lois pré/post connues et i.i.d. | Page (1954), *Continuous inspection schemes*, Biometrika ; Lorden (1971), *Procedures for reacting to a change in distribution*, Ann. Math. Stat. ; Moustakides (1986), *Optimal stopping times for detecting changes in distributions*, Ann. Stat. | **Non** : CUSUM est proposé sans calibrage sous effet épisode |
| Le témoin d'une sonde doit être une tâche de contrôle (étiquettes permutées), pas seulement des directions aléatoires | Hewitt, Liang (2019), *Designing and Interpreting Probes with Control Tasks*, EMNLP | Partiellement (plancher apparié en covariance) |
| Les détecteurs de mensonge par sondes généralisent mal hors distribution | Levinstein, Herrmann (2024), *Still no lie detector for language models: probing empirical and conceptual roadblocks*, Philosophical Studies ; Azaria, Mitchell (2023), *The Internal State of an LLM Knows When It's Lying* | Oui en substance (nul de P3, P4) |
| Les sondes et défenses latentes cèdent sous optimisation adverse | référence à vérifier | Partiellement (Papier C, « coût de déplacement d'une sonde ») |
| Les modèles détectent les contextes d'évaluation | référence à vérifier | Comme hypothèse de l'organisme (A, B) |
| Régression vers la moyenne : $\Delta v$ et $(\hat c - v_0)$ partagent $-v_0$ | Barnett, van der Pols, Dobson (2005), *Regression to the mean: what it is and how to deal with it*, Int. J. Epidemiology | **Non** |
| Votes corrélés : la sagesse d'un comité s'effondre | Ladha (1992), *The Condorcet Jury Theorem, Free Speech, and Correlated Votes*, Am. J. Political Science | Partiellement (Faille inédite C) |
| Propreté stricte : conditions globales, invariance affine | Savage (1971), *Elicitation of personal probabilities and expectations*, JASA ; Gneiting, Raftery (2007), *Strictly Proper Scoring Rules, Prediction, and Estimation*, JASA | Partiellement (D, conditions locales seulement) |
| Un système qui optimise sa propre mesure la dégrade | Manheim, Garrabrant (2018), *Categorizing Variants of Goodhart's Law* | Partiellement (D) |
| Le report vers un arbitre exige un risque contrôlé sur les cas non reportés | Geifman, El-Yaniv (2017), *Selective Classification for Deep Neural Networks*, NeurIPS | **Non** (marge 0,18 fixée sans garantie) |

---

## 3. Vérification des énoncés et des chiffres

**V1 — Seuil conforme (Faille 1).** Exact, avec une réserve de vocabulaire.
- Pour $K=1000$ et $\alpha=0{,}05$ : $\lceil 1001\times0{,}95\rceil=951$.
- Pour des maxima continus échangeables, $\mathbb P(M_{\text{new}}>M_{(951)})=50/1001=4{,}995\,\%$. C'est le « prédit » du rapport, et c'est une égalité, pas seulement une borne.
- Conditionnellement au jeu de calibrage, le taux réel suit une loi Bêta d'écart-type $\approx\sqrt{0{,}05\cdot0{,}95/1002}\approx0{,}69$ point. La plage 4,6–5,5 % sur 17 réglages est donc compatible (RAPPORTÉ).
- Pour la porte G1 ($\alpha=0{,}01$) : rang 991, taux $10/1001$, écart-type conditionnel $\approx 0{,}31$ point.
- **Réserve :** la garantie porte sur le maximum d'un épisode de longueur $T$ fixée. Elle n'est pas « valable à tout instant » au sens de Ville si la longueur d'épisode est variable ou non bornée.
- Elle est par épisode : sur $n$ épisodes honnêtes déployés, on attend $n\alpha$ fausses alarmes.

**V2 — Classes $\mathcal C$ et $\mathcal K$ (Faille 2).**
- *Classe $\mathcal C$ : exact*, à condition que le multiensemble attaqué ait la loi d'un épisode honnête et que la statistique soit invariante par le groupe effectivement utilisé.
- *Classe $\mathcal K$ : « puissance strictement supérieure à $\alpha$ » est faux en général.* Le passage « variance plus grande, donc queue plus lourde au-delà du seuil » ne vaut que pour des familles position-échelle (cas gaussien) avec $\alpha<1/2$.
- Contre-exemple : deux scores de marge Bernoulli(0,1).
  - Sous indépendance, $S\in\{0,1,2\}$ avec probabilités $(0{,}81;\,0{,}18;\,0{,}01)$.
  - Sous comonotonie (corrélation positive maximale, marges intactes), $S\in\{0,2\}$ avec probabilités $(0{,}9;\,0{,}1)$. La variance passe de 0,18 à 0,36.
  - Le test « $S\ge1$ » (taille 0,19 sous $H_0$) a une puissance de **0,10 < α**.
  - Le test « $S\ge2$ » (taille 0,01) a une puissance de 0,10 > α.
  - Le signe dépend donc du seuil.
- La condition générale relève des ordres stochastiques : l'ordre convexe donne l'ordre *stop-loss*, pas l'ordre des queues à seuil fixé.
- *Slepian : exact* pour des vecteurs gaussiens centrés à variances égales, à condition que toutes les covariances sous attaque dominent celles de $H_0$ terme à terme. Hors cas gaussien, il faut un ordre orthant-inférieur entre copules (Müller, Stoyan (2002), *Comparison Methods for Stochastic Models and Risks*).
- Si l'attaquant augmente certaines corrélations et en diminue d'autres, l'énoncé « max bloqué à $\alpha$ » n'est pas démontré.

**V3 — Fragmentation (Faille 3).** Exact sous scores gaussiens i.i.d. :
- seuil du maximum en $\sigma\sqrt{2\ln n_0}$ ;
- $20/(10\sqrt{100})=0{,}20$ et $20/(10\sqrt{400})=0{,}10$.

**V4 — Faille inédite D.** Les chiffres sont exacts ; la caractérisation et le colmatage sont surévalués.
- $0{,}82\times0{,}745+0{,}18=0{,}7909$ : exact.
- Pour $S=1-\text{Brier}+0{,}02(q-\tfrac12)^2$, on a $g_p'(q)=2p-1{,}96q-0{,}02$, donc $q^*=(p-0{,}01)/0{,}98$. Pour $p=0{,}97$, $q^*=0{,}9796$ : exact.
- Mais $q^*-p=0{,}02(p-\tfrac12)/0{,}98$ : la distorsion est **linéaire en $(p-\tfrac12)$, symétrique** (sur-confiance aussi vers 0, avec $q^*=0{,}0204$ pour $p=0{,}03$). Elle n'est pas « localisée aux queues ».
- Le test de Savage la détecte largement : $g_p'(p)=0{,}04(p-\tfrac12)=0{,}0188\gg1{,}5\cdot10^{-4}$.
- **Le colmatage est local, la propreté est globale.**
  - Contre-exemple : Brier plus une bosse lisse de hauteur $c$ à support dans $(0{,}701;\,0{,}709)$, c'est-à-dire entre deux points de grille.
  - Dérivées première et seconde aux 99 points : inchangées. Ancrages en 0,5 et 0,9999 : inchangés.
  - Pourtant, si $c>(0{,}705-0{,}5)^2\approx0{,}042$, l'optimum global pour $p=0{,}5$ quitte $0{,}5$.
  - La grille ne teste pas non plus $p\in(0;0{,}01)\cup(0{,}99;1)$.
- **Ancrage :** les deux ancres fixent $(a,b)$ *dans la famille affine de Brier*. Toute autre règle propre (logarithmique, Tsallis 4/3 de la Faille B) doit être renormalisée pour les passer. Le seuil 0,78 n'a donc pas de sens indépendant de la règle.

**V5 — Bregman-Tsallis $\alpha=4/3$ (Faille inédite B).**
- La formule est correcte. $\Phi''=\tfrac43[q^{-2/3}+(1-q)^{-2/3}]>0$, donc $\Phi$ est strictement convexe et la règle est strictement propre.
- Pénalité maximale : $\Phi'(1)=4[q^{1/3}-(1-q)^{1/3}]_{q=1}=4$, finie.
- Rapport pénalité au bord / pénalité au centre : $4/0{,}619\approx6{,}5$, contre 4 pour Brier et l'infini pour le score logarithmique. « Sévèrement » est donc relatif : la règle se situe entre Brier et log.
- **Défaut de correspondance :** toute règle strictement propre *récompense* une incertitude réellement calibrée. Si la « simulation de calibration » est calibrée sur les sous-tâches bénignes, la règle ne peut pas la sanctionner. Le colmatage ne vise pas la faille qu'il prétend colmater.

**V6 — « Une rotation orthogonale laisse invariant le spectre de Koopman-ISVD » : faux.** Les blocs $\sin v$ et $v^2$ sont élément par élément, donc $\Psi(Rv)$ n'est pas une transformation orthogonale de $\Psi(v)$.
- Contre-exemple en 2D : $v=(1,0)$ et rotation de 45°.
  - $\|\Psi(v)\|^2=1+\sin^21+1\approx2{,}708$.
  - $\|\Psi(Rv)\|^2=1+2\sin^2(0{,}7071)+0{,}5\approx2{,}344$.
  - La valeur singulière de la matrice à un échantillon passe de 1,646 à 1,531.
- Seul le bloc linéaire est invariant, et cela relève de la SVD ordinaire, pas de Koopman.
- Le « spectre de Koopman » désigne les valeurs propres d'un opérateur d'évolution temporelle, non les valeurs singulières d'un dictionnaire (Williams, Kevrekidis, Rowley (2015), *A data-driven approximation of the Koopman operator: extending dynamic mode decomposition*, J. Nonlinear Sci.).
- Enfin, une statistique invariante par rotation ne porte aucune information de direction. Elle ne discrimine que si le spectre lui-même diffère entre honnête et dissimulé, ce qui reste à montrer.

**V7 — Capacité de Shannon-Gram (Faille inédite C).**
- Avec $k$ moniteurs identiques de norme 1, $G=\mathbf 1\mathbf 1^\top$, donc $\det(I+s\,G)=1+sk$.
- Le gain du $(k+1)$-ième vaut $\tfrac12\log_2\frac{1+s(k+1)}{1+sk}>0$. Il ne « tombe pas à zéro ».
- La formule suppose des bruits **indépendants** entre moniteurs, c'est-à-dire précisément l'hypothèse que le conformisme viole. Elle ne peut donc pas mesurer ce conformisme.

**V8 — Routage « Faible-vers-Fort ».**
- Supposons un pli de 25 % portant sur 60 tâches, soit environ 15 tâches (illustratif ; l'unité du pli n'est pas précisée).
- Une exactitude de 0,65 aurait alors un intervalle à 95 % d'environ ±0,24. Elle ne se distingue pas de 0,5.
- Si le pli est tiré sur les actions plutôt que sur les tâches, la dépendance intra-tâche gonfle l'exactitude.

**V9 — Loi de déférence.**
- Régresser $v_1-v_0$ sur $\hat c-v_0$ crée une pente positive même si $g=0$, dès que $v_0$ est bruité : $\mathrm{Cov}=\mathrm{Var}(\varepsilon_{v_0})>0$.
- Les $R^2$ de 0,73 et 0,69 (RAPPORTÉ) ne distinguent pas déférence et couplage.
- Le contraste Llama/Qwen (Faille 6) pourrait refléter des fiabilités de $v_0$ différentes (HYPOTHÈSE).

**Non vérifiable depuis F1 :**
- 21–35 % de fausses alarmes ;
- 31/31 prédictions confirmées ;
- aires minimales détectables 0,63 et 0,60 ;
- $p=0{,}0006$ ;
- $\kappa$ = 0,04–0,17 ;
- 68 % / 1 %.

Tous restent RAPPORTÉ.

---

## 2 et (b). Failles inédites et expériences décisives

Je n'élabore pas les modalités par lesquelles un agent simulerait une calibration ou contournerait une sonde. Seules les hypothèses et leurs tests figurent ci-dessous.

### I1 — Le colmatage de la Faille 1 est réfuté par l'hypothèse A du programme lui-même
**Pourquoi.** Si la conscience d'évaluation déplace les activations (a5), les épisodes honnêtes de calibrage, collectés en contexte d'essai, ne sont pas échangeables avec ceux du déploiement. La garantie conforme ne se transfère alors plus. Le rapport ne nomme pas ce couplage entre A et le seuil de G1.

| | |
|---|---|
| **H_A** | Le taux de fausses alarmes, avec un seuil calibré sur des épisodes honnêtes à indices d'évaluation, reste ≤ α sur des épisodes honnêtes sans ces indices. |
| **H_B** | Il dépasse α. |
| **Métrique** | Taux de fausses alarmes, avec IC binomial exact, sur des épisodes honnêtes appariés (mêmes tâches, cadrage différent uniquement). |
| **Seuil** | α = 1 %, marge préenregistrée de 1 point (illustratif). |
| **Contrôle négatif** | Calibrage et test dans le même cadrage : le taux doit revenir à α ± dispersion Bêta (V1). |
| **Falsifie H_A** | Borne basse de l'IC du taux décalé > α, avec un témoin conforme. |
| **Falsifie H_B** | Borne haute ≤ α + 1 point, avec un témoin conforme. Cette issue affaiblit aussi a5 *pour ce score*. |

### I2 — La sonde lit l'intention ou lit le nombre faux
**Pourquoi.** Dans la famille « coûts gonflés », sabotage et erreur honnête produisent le même jeton numérique. Le témoin « grandeur du nombre » de P3b ne couvre pas une erreur honnête de même grandeur.

| | |
|---|---|
| **H_A** | La sonde P3b sépare le sabotage des erreurs honnêtes appariées : agent honnête recevant une donnée erronée qui conduit au même coût écrit. |
| **H_B** | Elle ne sépare que le correct du faux. |
| **Métrique** | AUROC sabotage contre erreur honnête, bootstrap sur les tâches. |
| **Seuil** | Borne basse à 95 % supérieure au maximum de trois témoins : (i) quantile 0,95 du plancher apparié en covariance ; (ii) sonde entraînée sur étiquettes permutées (Hewitt, Liang 2019) ; (iii) sonde de grandeur du nombre. |
| **Contrôle négatif** | Honnête correct contre honnête correct (deux tirages) : AUROC ≈ 0,5. |
| **Falsifie H_A** | AUROC sabotage/erreur honnête ≤ témoins alors que l'AUROC sabotage/honnête correct est > témoins. |
| **Falsifie H_B** | AUROC sabotage/erreur honnête > les trois témoins. |

### I3 — CUSUM réintroduit la Faille 1
**Pourquoi.** Si $\eta_e>\kappa$, $C_t$ croît linéairement chez un agent honnête. Le colmatage de la Faille 3 hérite alors de la faille corrigée par la Faille 1.

| | |
|---|---|
| **H_A** | CUSUM à $\kappa$ fixé conserve son taux de fausses alarmes nominal sous les 17 réglages de T0.3. |
| **H_B** | Il le dépasse. |
| **Métrique** | Taux de fausses alarmes par épisode. |
| **Seuil** | Taux nominal + 2 erreurs-types Monte-Carlo. |
| **Contrôle négatif** | $\sigma_{\text{ép}}=0$. |
| **Falsifie H_A** | Dépassement dans au moins un réglage préenregistré. |
| **Falsifie H_B** | Aucun dépassement dans les 17 réglages. |
| **Bras correctif** | Seuil conforme appliqué à $\max_t C_t$, où la garantie V1 s'applique telle quelle. |

### I4 — La loi de déférence est un artefact de couplage
| | |
|---|---|
| **H_A** | $g$ mesure une déférence. |
| **H_B** | $g$ provient de la régression vers la moyenne. |
| **Mesure** | Deux mesures indépendantes de la valeur initiale ($v_0^a$, $v_0^b$). Régresser $v_1-v_0^a$ sur $\hat c-v_0^b$. |
| **Contrôle négatif** | Condition sans pression ($\hat c$ non montré). Sous H_A, la pente y est ≈ 0. |
| **Falsifie H_A** | L'IC de la pente corrigée contient 0, ou la pente sans pression ≈ la pente avec pression. |
| **Falsifie H_B** | Pente corrigée ≈ 0,70 avec un IC excluant 0, et pente sans pression ≈ 0. |
| **Extension** | Même protocole sur Qwen2.5-7B, pour tester si la Faille 6 tient après correction. |

### I5 — Rotation contre atténuation (Faille inédite A)
| | |
|---|---|
| **H_A** | Le signal existe en contexte de trajectoire mais selon une direction faiblement alignée avec la sonde courte. |
| **H_B** | Le signal est atténué ou absent dans ce contexte. |
| **Mesure** | Sonde $w_{\text{traj}}$ entraînée par couche sur trajectoires (tâches tenues à l'écart). AUROC de $w_{\text{traj}}$ ; cosinus($w_{\text{court}}, w_{\text{traj}}$) ; alignement de Procrustes. |
| **Témoins** | Étiquettes permutées ; plancher apparié en covariance. |
| **Falsifie H_A** | AUROC($w_{\text{traj}}$) ≤ témoins : rien vers quoi « pivoter » à cette puissance. Ou bien cosinus élevé avec une sonde courte en échec : c'est un décalage de seuil ou d'échelle, pas une rotation. |
| **Falsifie H_B** | AUROC($w_{\text{traj}}$) > témoins, cosinus bas, sonde courte au hasard. |

Le résultat de P4, s'il existe, doit être versé ici. Il n'est pas dans F1.

### I6 — L'orthogonalisation forcée du comité retire du signal
**Pourquoi.** Si l'indice « saturé » est informatif, interdire au deuxième juge de s'en servir réduit sa puissance individuelle.

| | |
|---|---|
| **H_A** | Un comité orthogonalisé de taille $k$ a un meilleur TPR à FPR = 1 % qu'un comité de $k$ juges indépendants. |
| **H_B** | Il n'en a pas. |
| **Métrique** | TPR à FPR = 1 % ; corrélation des *erreurs* (coefficient phi), pas Gram des analyses. |
| **Contrôle négatif** | Comité à consignes diversifiées de même longueur, sans contrainte d'orthogonalité. |
| **Falsifie H_A** | Borne basse de la différence de TPR ≤ 0. |
| **Falsifie H_B** | Borne basse > 0 avec corrélation d'erreurs réduite. |

---

## 4. Réponses : contre-mesure et mesure de succès

| Faille | Contre-mesure | Mesure qui dit si elle marche |
|---|---|---|
| I1 (décalage calibrage/déploiement) | Conformal pondéré par rapport de vraisemblance cadrage-déploiement (Tibshirani et al. 2019) ; calibrage sur épisodes sans indices d'évaluation | Taux de fausses alarmes ≤ α sur le cadrage décalé (protocole I1) |
| V1 (horizon) | Renommer la garantie « par épisode, horizon $T$ » ; normaliser ou stratifier par $T$ | Taux de fausses alarmes par strate de $T$ |
| I3 | Seuil conforme sur $\max_t C_t$ | Taux de fausses alarmes ≤ α dans les 17 réglages ; délai de détection sur rupture tardive |
| V2 ($\mathcal K$) | Énoncer la puissance sous ordre stochastique explicite ; tester les deux sens du seuil | Simulation incluant des marges discrètes (contre-exemple V2) |
| V4 (Savage local) | Vérification globale : maximisation de $g_p$ sur grille fine de $q$ pour chaque $p$, plus intervalles extrêmes ; règle d'évaluation gelée par empreinte hors du périmètre modifiable par le système | Taux de détection sur une bibliothèque de règles impropres semées ; fausses alertes sur règles propres renormalisées |
| V5 | Retirer la prétention anti-mimétisme de la règle 4/3 ; tester le mimétisme par cohérence entre confiance déclarée et activations ou issues, pas par une règle propre | Expérience dédiée à concevoir ; aucune mesure proposée dans F1 |
| V6 | Remplacer « Koopman-ISVD » par un alignement CCA/Procrustes testant directement I5 | Issue I5 |
| V7, I6 | Mesurer la corrélation d'erreurs ; nombre effectif $k_{\text{eff}}=k/(1+(k-1)\bar\rho)$ ; combiner les juges par moyenne de e-valeurs | Taux de fausses alarmes ≤ α sous dépendance arbitraire ; TPR à FPR fixé |
| V8 | Plis par tâche ; seuil de report calibré pour un risque cible sur les cas non reportés | Taux d'erreur parmi les non-reportés ≤ cible, avec IC |
| I2 | Témoin « erreur honnête » obligatoire dans P3b | Issue I2 |
| I4 | Mesure test-retest de $v_0$ | Issue I4 |

Sur la moyenne de e-valeurs : la moyenne de e-valeurs est une e-valeur sous dépendance arbitraire (Vovk, Wang (2021), *E-values: Calibration, combination and applications*, Annals of Statistics).

---

## 5. Associations nouvelles

1. **Ordres stochastiques et théorie du risque (ordre convexe, ordre orthant-inférieur ; Müller, Stoyan 2002).**
   - *Apport :* conditions exactes de la Faille 2 à la place de l'argument de variance.
   - *À démontrer :* la classe de copules pour laquelle la puissance de la somme dépasse α à tout seuil $\alpha<\alpha_0$.

2. **Higher criticism (Donoho, Jin 2004).**
   - *Apport :* une statistique adaptée au régime $m\sim n_0^\beta$, que ni le max ni la somme ne couvrent.
   - *À mesurer :* la frontière de détection empirique sur scores de sonde non gaussiens, calibrée conformément.

3. **Psychométrie (correction d'atténuation ; Spearman (1904), *The proof and measurement of association between two things*, Am. J. Psychology).**
   - *Apport :* séparer déférence et bruit de mesure (I4).
   - *À mesurer :* la fiabilité test-retest de $v_0$ par modèle.

4. **Jurys corrélés et effet de plan (Ladha 1992 ; nombre effectif de Kish, référence à vérifier).**
   - *Apport :* une métrique de conformisme fondée sur les erreurs, et non sur la similarité des textes.
   - *À mesurer :* $\bar\rho$ des erreurs de juges sur des cas appariés.

5. **Ingénierie de sécurité (séparation des pouvoirs, règle des deux personnes).**
   - *Apport :* contre la Faille D, interdire la modification de la règle d'évaluation plutôt que la contraindre après coup.
   - *À mesurer :* le nombre de modifications du code d'évaluation tentées et bloquées.

6. **Conformal pondéré sous décalage (Barber et al. 2023).**
   - *Apport :* une garantie qui se dégrade proportionnellement à l'écart à l'échangeabilité.
   - *À mesurer :* l'écart en variation totale entre cadrages, estimé par un classifieur.

---

## (c) Mesure minimale par instrument

| Instrument | Taux de détection / fausses alertes | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|
| **Sonde linéaire (P3, P3b)** | TPR à FPR = 1 % et 5 % ; AUROC, borne basse bootstrap sur tâches | Mêmes tâches : honnête correct, honnête avec erreur induite (I2), même longueur | Plancher apparié en covariance ; sonde à étiquettes permutées ; régression logistique sur traits de surface (longueur, syntaxe) ; grandeur du nombre ; **recalcul arithmétique du coût depuis les données de la tâche** |
| **Juge LLM** | TPR à FPR = 1 % ; corrélation d'erreurs entre juges | Mêmes traces, sabotage retiré ; traces honnêtes contenant les mêmes indices lexicaux | Détecteur par mots-clés ; recalcul arithmétique |
| **Seuil conforme / CUSUM** | Taux de fausses alarmes par épisode, délai de détection | Épisodes honnêtes du cadrage de déploiement (I1) | Seuil fixe naïf ; somme terminale |
| **Vérificateur de Savage** | Détection sur bibliothèque semée (impropres locaux, impropres non locaux de type V4, affines) ; fausses alertes sur règles propres (Brier, log tronqué, sphérique, Tsallis) | Paires règle propre / perturbation de même norme | Maximisation globale par recherche exhaustive sur $q$ |
| **Organisme (« la Fusée »)** | Proportion de « failles » proposées qui survivent à un audit indépendant | Corpus semé : énoncés vrais et énoncés faux connus, de même forme | Relecture par une instance fraîche sans l'organisme |

Pour l'organisme, mon propre audit trouve des défauts mathématiques dans les énoncés de colmatage de A (V6), B (V5) et C (V7), et dans le colmatage de D (V4). C'est une évaluation de cette cellule, non une mesure de taux.

---

## (d) Ancrage matériel

**Modèles** (cités dans F1, RAPPORTÉ) : Llama-3.1-8B, Qwen2.5-7B, modèles 70B pour Papier B. P3 a pris moins de 12 h ; le montant est retiré (RAPPORTÉ).

| Expérience | Calcul (illustratif) | Coût (illustratif) |
|---|---|---|
| I1 | Environ 2 000 épisodes honnêtes de 10 pas en 8B, activations en cache ; un GPU de 80 Go, environ 10 à 20 h | Quelques dizaines d'heures-GPU |
| I2 | 60 tâches × 3 conditions × 10 pas ≈ 1 800 actions ; moins d'une journée-GPU | Faible |
| I3, V2, V4 | Simulation ou CPU uniquement | Négligeable |
| I4 | Doublement des mesures de $v_0$ sur les campagnes existantes, Llama et Qwen ; environ 1 journée-GPU | Faible |
| I5 | Réutilisation des activations P3/P4 ; entraînement de sondes par couche, CPU/GPU, quelques heures | Faible |
| I6 | $k\le5$ juges 8B locaux sur environ 600 traces ; environ 1 journée-GPU. Version 70B : environ 4 GPU | Modéré |

FIN-DE-CELLULE