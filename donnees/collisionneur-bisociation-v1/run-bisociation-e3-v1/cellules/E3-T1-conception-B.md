# Proposition B — Tour III.1 : recombinaison bisociative à deux espaces

Je ne vois pas les propositions A et C. Je ne les cite donc pas et n'en fusionne rien (B1).

Les quatre pièces sont présentes et non coupées. La pièce D, comme l'indiquent les faits eux-mêmes, ne contient ni la « mémoire qui refuse les redites » ni l'« héritage récompensé » que la question lui attribue. Je n'en invente pas le contenu.

---

## (a) Ce que la question suppose sans que ce soit établi

**S1. La forme réfutée n'est peut-être pas le code de la pièce A.**
- Dans la pièce A, la voie `noyau_corrige` tire k = 4 **articles**, forme leurs paires, puis les trie par `(s[i][j], −q_i q_j, clé)`. Elle envoie donc d'abord les paires dont les domaines sont les moins semblables, et en garde `max_paires = 3`. [VÉRIFIÉ, contenu de la pièce A]
- Le bras (a) de la pièce B range ses paires « par (rang maximal, somme des rangs) », avec k = 4 paires par génération. [RAPPORTÉ, pièce B § 5]
- La pièce B ajoute que la forme corrigée « ne s'en servait déjà pas [du vecteur de domaine] pour les paires ». [RAPPORTÉ, § 2.3]
- Ma lecture : le tri par s_ij du code n'a pas été testé. La réfutation vaut pour le bras (a), pas forcément pour le code. [OBSERVÉ-NON-AUDITÉ, ma lecture comparée des deux pièces]
- Conséquence : il faut ajouter un bras (a′) « code tel quel ».

**S2. Le signe du terme conceptuel est ambigu dans les mots rapportés de Lazar.**
- La citation dit « maximiser le volume […] en même temps qu'on **minimise** leur proximité conceptuelle, non sémantique ». [RAPPORTÉ, question]
- L'hypothèse de travail demande au contraire que les parents soient « **proches** dans l'espace des concepts ».
- Deux lectures sont possibles : (i) la proximité *de domaine* doit se mesurer conceptuellement et non sémantiquement ; (ii) une erreur de transcription.
- Il faut trancher **avant** le préenregistrement, car le signe d'un terme de l'objectif en dépend. [HYPOTHÈSE sur l'intention]

**S3. « La proximité conceptuelle n'est qu'un filtre après coup » est inexact pour au moins deux bras.**
- (d1) pondère déjà le tirage par l'IDF de l'étiquette partagée, donc par une proximité conceptuelle *rare*, dans l'objectif. Gain : +3,5 / +3,8. [RAPPORTÉ, pièce B § 1 et § 4]
- (d2) mettait déjà un « contraste d'import » dans l'objectif, et a échoué (−6,7 / −3,4). [RAPPORTÉ]

**S4. Les comparateurs de la question omettent le plus fort bras qui n'apporte aucun ingrédient nouveau.**
- Le diagnostic b_eloigne (éloignement de domaine seul, parmi des paires qui partagent déjà une étiquette) fait +11,9 [+10,4 ; +13,4] et +6,6 [+5,5 ; +7,8]. [RAPPORTÉ, diagnostic non éligible]
- Sans b_eloigne ni sa combinaison avec la rareté de (d1), un gain de la forme à deux espaces ne peut pas être attribué à la proximité conceptuelle plutôt qu'à l'éloignement seul.

**S5. Les mondes de la pièce B sont déjà « à deux espaces ».**
- Côté concepts : opérateurs latents, mot de surface propre à chaque domaine, lexique observé à trois niveaux de bruit.
- Côté domaines : vecteur de domaine.
- La vérité y est : champs différents et opérateur latent commun non moyeu. [RAPPORTÉ, § 5]
- Les « étendre à deux espaces » en plantant une vérité égale à l'objectif testé rendrait le test tautologique. [HYPOTHÈSE]

**S6. Les vraies fiches de la course 2 ne sont pas établies.**
- La pièce C est un « brouillon […] non contre-lu, non servi ». [VÉRIFIÉ, en-tête des faits]
- Son gabarit n'a ni champ d'opérateurs, ni champ de domaines, ni champ de contraintes. [VÉRIFIÉ]
- Il ne contient ni « méthode » ni « test de mort » : il porte « critère de mort ». La question lui prête donc des champs qu'il n'a pas. [VÉRIFIÉ]
- Ses unités sont des « axes », pas des domaines. [VÉRIFIÉ]

**S7. Ce qui fait la qualité d'une paire reste inconnu.**
- La pertinence q y est indépendante de la vérité. [RAPPORTÉ, § 3]
- La qualité des fusions par un modèle n'est pas mesurée. [RAPPORTÉ, § 6]

**S8. Le filtre de compatibilité est faible.**
- Son rappel est mesuré entre 0,57 et 0,60. [RAPPORTÉ, § 5]
- 0,25 à 0,27 des paires tirées portent des contraintes vraiment incompatibles, pour tous les bras. [RAPPORTÉ, § 1]
- Ce plafond commun pèse sur toute forme à deux espaces. [HYPOTHÈSE sur son effet]

**S9. Les règles invoquées ne sont pas dans les faits.**
- N-053, R1, R7 et R8 ne sont pas fournies. Je ne connais N-053 que par la glose de la question : « sans sélection sur le verdict ».

**S10. Le seuil de +12 points (pièce B) est critiqué par son auteur même.**
- Même l'éloignement idéalisé ne l'atteint pas. [RAPPORTÉ, § 7.3]
- La question ne fixe pas de seuil ; il reste à geler.

---

## 1. L'objectif

### 1.1 « Minimiser le produit scalaire » est-il contenu dans « maximiser le volume » ?

- **Dans le signe, oui.** Pour deux vecteurs de domaine unitaires, le volume au carré vaut 1 − cos².
- **Dans la force, non.**
  - Avec le noyau de Schur S = cos², le déterminant d'une paire vaut q_i² q_j² ((1+γ)² − cos⁴). À cos = 0,28, la pénalité est de 0,6 %. [RAPPORTÉ, § 3]
  - Avec un Gram linéaire (Lazar parle du « volume entre deux directions »), elle vaudrait 1 − 0,28² = 0,922, soit 7,8 %. [calcul sur le cosinus de la pièce B]
  - Or q² varie d'un facteur 9. [RAPPORTÉ]
  - Pour que l'écart entre domaines proches (cos 0,28) et éloignés (cos 0,03) pèse autant qu'un facteur 9 de qualité, il faudrait un exposant β tel que 0,922^β ≈ 1/9, soit β ≈ 27. [calcul]
- **Conclusion.** Un terme d'éloignement **à part et pondéré** est nécessaire. Le volume seul est inerte face à la qualité. [HYPOTHÈSE, appuyée par § 3]

### 1.2 Options

| Option | Forme | Semi-définie positive ? | Ce qu'elle maximise réellement | Verdict |
|---|---|---|---|---|
| O1 | DPP sur articles, S = S_dom ⊙ S_concept ou S_dom ⊕ S_concept | Oui : produit de Schur ou somme de deux noyaux semi-définis positifs | Elle **repousse** les articles conceptuellement proches : signe contraire à l'hypothèse | Écartée |
| O2 | DPP sur articles, termes croisés = rapport proximité conceptuelle / proximité de domaine | En général non : il faut réparer par γ | Une diagonale de répulsion ; c'est la forme (e) de la pièce B, qui « repousse les paires qu'elle visait », γ médian 0,94 [RAPPORTÉ] | Écartée |
| O3 | **DPP sur les paires** : la qualité de la paire porte les deux espaces, le noyau ne sert qu'à diversifier le lot | Oui (voir 1.3) | La somme des scores de paire, plus la diversité des strates du lot | **Recommandée** |
| O4 | Contrainte plus rareté : strates éloignées d'abord, puis paire la plus rare | Sans objet | C'est b_eloigne combiné à (d1) | Témoin obligatoire |
| O5 | Marche de Swanson sur le biparti fiches × concepts, pondérée par l'IDF, bornée aux paires de domaines éloignés | Sans objet | La rareté du pont conditionnée à l'éloignement | Bras concurrent |

**Leçon commune à O1 et O2.** Dans un DPP, toute similarité placée hors de la diagonale est une **répulsion**. La proximité conceptuelle est une **attraction**. Elle ne peut donc vivre que dans la qualité, et cette qualité ne peut porter que sur des paires, pas sur des articles. C'est aussi la cause mise au jour par la pièce B : « diversifier les articles ne diversifie pas les paires » [RAPPORTÉ, § 3]. [HYPOTHÈSE de conception]

### 1.3 Forme recommandée (O3)

Les éléments sont les paires valides p = (i, j). Le pont, le filtre et l'interdiction de refusionner sont inchangés par rapport à la pièce A.

- **Score de paire** : r_p = √(q_i q_j) · (1 − D_ij²)^(β/2) · w(C_ij), où
  - D_ij est le cosinus des vecteurs de domaine ;
  - C_ij est le cosinus pondéré par l'IDF des vecteurs de concepts, sur une liste fermée (point 2) ;
  - w est croissante, par exemple w(c) = c^α.
- **Noyau de lot** : K_(ij),(kl) = ½ [S_ik S_jl + S_il S_jk] + γ δ, avec S le Gram linéaire des domaines.
- **Noyau final** : L = diag(r) K diag(r).

**Propriétés** [HYPOTHÈSE à confirmer par un test de Cholesky, comme dans `cholesky()` de la pièce A] :
- S ⊗ S est semi-défini positif (produit de Kronecker). Sa symétrisation P(S⊗S)P, où P projette sur les tenseurs symétriques, l'est aussi. La restriction aux paires valides est une sous-matrice principale. Avec γ > 0, L est défini positif et le déterminant est bien défini.
- **Ce que l'objectif maximise** : log det L_Y = Σ_p log r_p² + log det K_Y. C'est la somme des scores de paire (qualité, éloignement, proximité conceptuelle) plus un terme qui pénalise les lots dont les paires relient les mêmes couples de domaines. C'est un « stratifié pondéré », forme que la pièce B signale comme non testée [RAPPORTÉ, § 6].
- **Coût** : m ≤ n(n−1)/2 paires, soit 780 pour n = 40. Le glouton à Cholesky incrémentale coûte O(m k²). Négligeable sur processeur.
- **Différence avec le DPP classique** : les éléments sont des paires, pas des articles. Les deux espaces entrent dans la diagonale, avec des signes opposés. La répulsion ne sert qu'au lot.

**Recommandation : O3**, avec O4 et O5 comme témoins durs et α = 0 comme ablation. **Confiance moyenne-faible.** Rien n'indique que O3 batte O4. C'est précisément ce que teste l'expérience E1.

---

## 2. La représentation des concepts

| Option | Avantage | Inconvénient | Juge dans la boucle ? |
|---|---|---|---|
| R1 Déclaration par le proposeur, liste fermée, nouveau champ du gabarit | Gratuite, auditable | Manipulable : il suffit de déclarer des opérateurs-moyeux pour être tiré | Non |
| R2 Étiquetage par un modèle tiers, **hors boucle**, scellé (empreinte) avant tout tirage | Le proposeur ne contrôle pas l'étiquette | Coûte un appel de modèle ; le bruit de l'étiqueteur est inconnu | Non, s'il est scellé avant le tirage |
| R3 Extraction par programme (motifs, symboles, résultats nommés, citations) | Déterministe, gratuite | Couverture faible ; homonymes (« invariance » en physique et en statistique) | Non |

**Recommandation.**
- R2 sert au tirage.
- R3 est la **vérification mécanique à battre**.
- R1 est gardé seulement comme signal d'audit : le désaccord entre R1 et R2 est consigné et n'entre jamais dans r_p.
- **Confiance moyenne.**

**Contre la manipulation.**
1. Le tirage n'utilise que R2.
2. La pondération IDF rend non rentable la déclaration d'opérateurs-moyeux. C'est le mécanisme de (d1) : pièges moyeux 0,122 contre 0,385 [RAPPORTÉ].
3. La règle de tirage n'est pas montrée aux proposeurs.
4. Une mesure de manipulation est intégrée (instrument I4, partie (c)).

**Test de séparabilité concept / domaine** (mesures minimales, détail en I3) :
- Sur des paires **de domaines différents** : l'AUC de C_ij pour discriminer « même opérateur » de « opérateurs différents » doit être nettement supérieure à 0,5.
- Fuite de domaine : la précision d'un classifieur au centroïde le plus proche, qui prédit le domaine à partir du vecteur de concepts (validation par exclusion d'un élément), comparée à celle de la classe majoritaire.
- Ratio de similarité conceptuelle intra-domaine / inter-domaine **entre fiches d'opérateurs différents** : il doit valoir environ 1. S'il dépasse 1, la représentation encode le domaine.

---

## (b) Expériences décisives (inférence forte)

**Base commune.**
- Mondes de la pièce B, avec les mêmes graines de construction et le même étage commun.
- Métrique principale : la précision sur 12 paires, en écart apparié. Rééchantillonnage apparié des mondes (2 000), comme en pièce B.
- **Bras** : stratifié (témoin), forme corrigée v6.3 (a), (a′) code tel quel, (d1) Swanson, b_eloigne, **O4 = b_eloigne ⊕ rareté**, O5, **Z = O3 complet**, Z₀ = O3 avec α = 0 (sans proximité conceptuelle graduée).
- Tout δ ci-dessous est **illustratif**, à geler par Lazar.

### E1 — La proximité conceptuelle graduée est-elle l'ingrédient manquant ?

- **H_A** : Z bat le meilleur bras sans proximité graduée, soit max(O4, Z₀, b_eloigne), d'au moins δ = 2 points, intervalle > 0, dans les mondes « bien » **et** « moyen ».
- **H_B** : l'éloignement de domaine et la rareté expliquent tout. L'écart Z − max(O4, Z₀) est équivalent à 0 (test d'équivalence TOST à ±δ) dans les deux mondes.
- **Seuil d'adoption** : H_A, plus le respect des contrôles E2 et E3.
- **Contrôle négatif** : le placebo du monde sans pont de la pièce B. L'écart de Z au stratifié doit avoir un intervalle qui contient 0. Le taux d'intervalles excluant 0 ne doit pas dépasser le hasard ; la pièce B observe 3,2 % [RAPPORTÉ].
- **Ce qui falsifie** :
  - un gain ≥ δ falsifie H_B ;
  - une équivalence falsifie H_A ;
  - toute autre issue est déclarée « non concluant » d'avance, sans relance.

### E2 — Proximité ou rareté ?

- **H_A** : le terme w(C) agit par la proximité graduée. Dans des mondes **sans moyeu** (part de moyeux 0, ce qui prolonge la sensibilité « 0,10 » de la pièce B), Z − Z₀ ≥ δ.
- **H_B** : il n'agit que par l'évitement des moyeux. Sans moyeu, Z − Z₀ est équivalent à 0. Avec moyeux dominants, Z − Z₀ ≈ (d1) − stratifié.
- **Contrôle « concept leurre »** : un monde où les vrais ponts partagent **un seul** opérateur latent et les faux en partagent **plusieurs** (parasites et homonymes).
  - Si Z gagne aussi dans ce monde, c'est un artefact de mesure, et H_A est falsifiée comme mécanisme.
  - Si Z y perd, c'est attendu sous les deux hypothèses : seul le monde sans moyeu tranche.

### E3 — Contrôle inversé corrigé (pièce B, § 7.2)

- **Monde « import »** : les vrais ponts relient des domaines éloignés par des opérateurs **complémentaires** : l'un apporte ce qui manque à l'autre, sans partage d'opérateur.
- **H_A** (Z cible bien la proximité conceptuelle) : Δ_import − Δ_normal < 0 pour Z − stratifié, intervalle sous 0.
- **H_B** (Z gagne par un avantage générique) : Δ_import − Δ_normal a un intervalle qui contient 0, ou au-dessus de 0. C'est le défaut constaté pour (a) dans la pièce B, où l'écart était remonté de 1,3 point.
- **Témoin du contrôle** : b_eloigne doit **rester** positif dans le monde import (l'éloignement y reste vrai). S'il chute, c'est la construction du monde qui est fautive : on arrête.

### E4 — Séparabilité de la représentation

- **H_A** : R2 encode le concept. AUC ≥ 0,75, fuite de domaine ≤ classe majoritaire + 5 points, ratio intra / inter ≤ 1,2 (chiffres illustratifs).
- **H_B** : R2 encode le domaine. La fuite dépasse la classe majoritaire de plus de 5 points, ou le ratio dépasse 1,2.
- **Contrôle négatif** : étiquettes permutées entre fiches. L'AUC doit valoir 0,5 et la fuite le niveau du hasard.
- **Contrôle positif** : une représentation volontairement fuyante (concepts concaténés au domaine en codage à un actif). Le test **doit** la rejeter, sinon il est aveugle.

### E5 — Manipulation du champ déclaré

- **H_A** : avec la garde (tirage sur R2 plus IDF), une fiche jumelle qui ajoute 3 opérateurs populaires à sa déclaration est tirée au même taux que sa jumelle honnête, à ε près.
- **H_B** : l'inflation paie. Le taux de tirage de la jumelle gonflée dépasse celui de l'honnête de plus de ε, intervalle > 0.
- **Comparaison obligatoire** : le même essai **sans garde** (tirage sur R1). H_B doit y être vraie ; sinon, l'essai n'a pas de puissance pour détecter une manipulation.

### E6 — Rétrodiction sur littérature réelle (étape proposée en pièce B, § 8)

- Même duel que E1, avec la même règle et les mêmes témoins.
- « Pont réalisé » : deux littératures disjointes avant T et reliées après T, selon la définition de la pièce B.
- C'est la **seule** expérience qui tranche hors monde synthétique. Elle demande un accès réseau, soumis au GO de Lazar [RAPPORTÉ, § 8].

### Puissance

- Les intervalles de la pièce B ont une demi-largeur d'environ 1,5 point à 400 mondes, soit une erreur type d'environ 0,77 point [calcul sur la pièce B].
- Pour une supériorité de δ = 2 avec une puissance de 90 % (α unilatéral 2,5 %), il faut une erreur type d'environ 0,62, soit **environ 620 mondes**. Le test d'équivalence à ±2 donne un nombre voisin.
- Je propose **800 mondes par condition** (illustratif).
- Réserve : la variance de Z − O4 peut différer de celle de (a) − (b). Il faut un pilote sur graines de validation distinctes, sans lecture des écarts.

### Liste d'arrêt

- Validation du générateur hors des cosinus préenregistrés (0,54 / 0,28 / 0,03 [RAPPORTÉ]).
- Échec de Cholesky sur L.
- Placebo de Z avec un intervalle qui exclut 0.
- Contrôle positif de E4 non détecté.
- Témoin de E3 en chute.
- Toute modification d'un bras après la première exécution.

### Conclusions préenregistrables

- **« Ingrédient manquant »** si, et seulement si, E1 donne H_A **et** E2 donne H_A **et** E3 donne H_A.
- **« Non »** si E1 donne H_B. On garde alors O4, si O4 bat le stratifié avec un intervalle > 0.
- Sinon : **non concluant**.

### Passage aux fiches de la course 2 (sans sélection sur le verdict)

Prérequis : S6 levé (fiches existantes, notion de « domaine » définie).

1. Ajouter au gabarit `operateurs` (liste fermée), `domaines` et `contraintes`.
2. Étiqueter par R2, puis sceller le vivier et les étiquettes par empreinte avant tout tirage.
3. Chaque bras tire ses k paires avec des graines gelées. Une paire tirée par plusieurs bras n'est fusionnée qu'une fois.
4. Juger à l'aveugle du bras, avec le témoin planté de la pièce C.
5. Mettre **au dénominateur toutes les paires tirées** : refus, filles invalides et arrêts de budget comptés comme échecs. Pas de relance ni de remplacement.

**Limite.** Sans vérité terrain, la course 2 mesure le **rendement de fusion**, pas la vérité des ponts. Elle ne tranche donc pas E1 ; seule E6 le peut. [HYPOTHÈSE]

---

## (c) Mesure minimale de chaque instrument

| Instrument | Détection | Fausses alertes | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| **I1 Objectif Z (O3)** | Rappel des vrais ponts à budget fixé (pièce B : (b) 0,214, (d1) 0,253 [RAPPORTÉ]) | Part de pièges tirés : moyeux, homonymes, parasites | Vrai pont apparié à une paire piège de même éloignement de domaine et de même nombre d'étiquettes partagées | Stratifié, b_eloigne, O4, (d1) |
| **I2 Étiqueteur R2** | Rappel des opérateurs annotés à la main | Taux d'étiquettes parasites | Paraphrases (même opérateur, mots différents) contre homonymes (même mot, opérateurs différents), par paires | R3 : motifs et résultats nommés, du type `MARQUEURS` de la pièce A |
| **I3 Test de séparabilité** | Rejette une représentation fuyante plantée | Rejette à tort une représentation honnête (sur les mondes, où l'on connaît la vérité latente) | Représentation honnête contre la même représentation concaténée au domaine | Fuite au niveau de la classe majoritaire ; étiquettes permutées |
| **I4 Garde anti-manipulation** | Fiche gonflée non avantagée | Fiche honnête riche en opérateurs pénalisée à tort | Jumelles identiques au champ déclaré près | Seuil sur le nombre d'étiquettes déclarées |
| **I5 Filtre de compatibilité** | Rappel des incompatibilités vraies (0,57 à 0,60 [RAPPORTÉ]) | Rejets à tort (4 à 5 % [RAPPORTÉ]) | Paires annotées compatibles et incompatibles, de même longueur de contraintes | Le motif à expressions régulières actuel (pièce A) ; il doit être battu sur fiches réelles avant tout gain d'objectif |
| **I6 « La fille prédit plus »** | Détecte une prédiction parente reformulée | Rejette à tort une prédiction neuve | Filles qui recopient un parent en le reformulant, contre filles vraiment nouvelles | `signature_prediction` (module `memoire`, **non servi** : je ne connais pas sa définition), comparée à une égalité stricte de texte normalisé |
| **I7 Marche de Swanson (O5)** | Comme I1 | Comme I1 | Comme I1 | (d1) d'origine |

Toutes les cibles numériques de ces instruments sont à geler. Celles que j'ai données en E4 sont illustratives.

---

## 4. Antériorité (à vérifier sur PDF)

- **Processus ponctuels déterminantaux**
  - Macchi, O. (1975), « The coincidence approach to stochastic point processes », *Advances in Applied Probability*.
  - Kulesza, A. et Taskar, B. (2012), « Determinantal Point Processes for Machine Learning », *Foundations and Trends in Machine Learning*.
  - Gillenwater, J., Kulesza, A. et Taskar, B. (2012), « Near-Optimal MAP Inference for Determinantal Point Processes », NIPS.
  - Chen, L., Zhang, G. et Zhou, H. (2018), « Fast Greedy MAP Inference for Determinantal Point Process to Improve Recommendation Diversity », NeurIPS.
  - Qualité × diversité dans L = diag(q) S diag(q) : c'est la décomposition de Kulesza et Taskar.
  - Un DPP **sur des paires**, avec une proximité conceptuelle en qualité : je n'en connais pas. **Référence à vérifier** ; c'est une question, pas un trou.
- **Analogie : même structure relationnelle, domaines de surface différents.** C'est l'antériorité la plus proche de l'objectif à deux espaces.
  - Gentner, D. (1983), « Structure-mapping: A theoretical framework for analogy », *Cognitive Science*.
  - Hope, T., Chan, J., Kittur, A. et Shahaf, D. (2017), « Accelerating Innovation Through Analogy Mining », KDD. Représentations séparées « but » et « mécanisme » : le plus proche, à mon sens, de la représentation à deux espaces.
- **Découverte fondée sur la littérature**
  - Swanson, D. R. (1986), « Fish oil, Raynaud's syndrome, and undiscovered public knowledge », *Perspectives in Biology and Medicine*.
  - Swanson, D. R. et Smalheiser, N. R. (1997), « An interactive system for finding complementary literatures: a stimulus to scientific discovery », *Artificial Intelligence*.
  - Tshitoyan, V. et al. (2019), « Unsupervised word embeddings capture latent knowledge from materials science literature », *Nature*.
- **Bisociation**
  - Koestler, A. (1964), *The Act of Creation*.
  - Berthold, M. R. (dir.) (2012), *Bisociative Knowledge Discovery*, Springer LNCS. Titre exact du volume : référence à vérifier.
- **Recombinaison et nouveauté**
  - Uzzi, B., Mukherjee, S., Stringer, M. et Jones, B. (2013), « Atypical Combinations and Scientific Impact », *Science*.
  - Weitzman, M. L. (1998), « Recombinant Growth », *Quarterly Journal of Economics*.
  - Fleming, L. (2001), « Recombinant Uncertainty in Technological Search », *Management Science*.
- **Évolution ouverte et programmation génétique**
  - Koza, J. R. (1992), *Genetic Programming*.
  - Lehman, J. et Stanley, K. O. (2011), « Abandoning Objectives: Evolution Through the Search for Novelty Alone », *Evolutionary Computation*.
  - Mouret, J.-B. et Clune, J. (2015), « Illuminating search spaces by mapping elites » (prépublication).
  - Je ne connais pas d'opérateur de croisement qui choisit ses parents « loin en phénotype, proches en mécanisme » : **référence à vérifier**.

**Recommandation.** Faire rechercher en priorité les travaux qui suivent Hope et al. (2017) sur la séparation but / mécanisme. **Confiance faible** quant à l'absence de forme à deux espaces déjà publiée.

---

## (d) Ancrage matériel

- **Tirage et mondes.**
  - Processeur seul, bibliothèque standard de Python. Le run de la pièce B : 4 000 mondes, tous bras, en 93 s [RAPPORTÉ].
  - E1 à E5 : environ 10 conditions × 800 mondes × environ 10 bras, soit de l'ordre de quelques minutes à une heure de processeur (illustratif).
  - Coût monétaire : quasi nul (illustratif).
- **Étiqueteur R2.**
  - Modèle ouvert de 7 à 14 milliards de paramètres en version instruite (par exemple des familles Qwen2.5, Llama 3.1 ou Mistral), une carte de 24 à 80 Go.
  - Pour quelques milliers de fiches ou de résumés : quelques heures de carte, de l'ordre de 10 à 50 dollars en location (illustratif).
  - Annotation humaine pour I2 et I3 : environ 200 fiches, deux annotateurs et un accord mesuré (illustratif).
- **E6.**
  - Instantané OpenAlex ou métadonnées d'arXiv : accès réseau, sous GO de Lazar [RAPPORTÉ, pièce B § 8].
  - Stockage et prétraitement : de l'ordre de centaines de Go et de dizaines d'heures de processeur (illustratif).
- **Fusions de la course 2.**
  - Coût par paire = `plafond_recombinaison_usd` de la configuration. Sa valeur n'est pas dans les faits : coût non estimable ici.
- **Dépense.** Chez session-depot, sur devis et ligne de GO [RAPPORTÉ, question] ; rien n'est lancé par moi.

**Ce qui peut réfuter cette proposition.**
1. E1 donne H_B : la forme O3 n'apporte rien sur O4.
2. E3 donne H_B : Z gagne par un avantage générique.
3. E4 montre que R2 encode le domaine.
4. Le test de Cholesky échoue sur le noyau de paires.
5. Lazar confirme la lecture S2 (ii) avec le signe « minimiser » : le terme w(C) change alors de signe et E1 à E3 sont à réécrire.

FIN-DE-CELLULE