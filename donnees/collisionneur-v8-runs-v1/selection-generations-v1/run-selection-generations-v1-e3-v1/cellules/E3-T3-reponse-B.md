# Proposition B — Tour III.3 : réponse aux critiques

---

## (a) Traitement critique par critique

Je réponds à chaque critique visant la proposition B, par source (A, C, D, E). Statut de mes réponses : **HYPOTHÈSE** sauf mention.

---

### Critiques de A sur B

**A-1. E1 — « Vrai par construction / fuite : témoins vrais sélectionnés parce qu'ils passent sur le développement. »**

**Acceptée.** Un témoin vrai confirmé sur le développement (pièce 7 §a.3, RAPPORTÉ) est sélectionné pour être visible ; la puissance mesurée est celle du meilleur cas, pas celle d'un effet de force nominale arbitraire. Le confondant « force ≥ 0,5 » vs « log-rapport de cotes 0,6 » est réel : j'ai employé les deux sans conversion explicite.

*Correction* : E1 corrigé (section b) distingue désormais deux bras de témoins vrais — confirmés-sur-développement (sélectionnés) et à force *nominale* calculée (non sélectionnés) — et exige une conversion explicite entre les deux paramétrisations. Un contrôle « connu + 0 » (effet nul, même moniteur) est ajouté.

**A-2. E3 — « Confondant : les tests de mort et le pôle opèrent sur des données différentes. »**

**Acceptée.** Les tests de mort s'exécutent sur des données locales ou de développement (pièce 1 §9.2, RAPPORTÉ), le pôle sur l'épreuve. Une discordance peut refléter la différence des données, pas la non-redondance des filtres.

*Correction* : E3 corrigé impose un contrôle « même donnée, filtres différents » (témoins jugés par les deux filtres sur la partie de développement) en plus du contrôle en conditions normales. H_A et H_B sont reformulées (section b).

**A-3. E4 — « Ratio W_partagée/W_fraîche mal défini (log-richesses signées). »**

**Acceptée.** Le log W peut être négatif (pièce 4 : log W −135, OBSERVÉ-NON-AUDITÉ). Le ratio de quantités signées change de sens. Le « contrôle mère » est circulaire.

*Correction* : E4 corrigé remplace le ratio par une *différence normalisée* (log W_partagée − log W_fraîche)/N, bornée en espérance sous le nul. Le contrôle est remplacé par des lois *figées* sans retour intergénérationnel, évaluées sur les deux épreuves (contrôle proposé par A, repris en le disant).

**A-4. E5 — « Non-comparabilité des issues entre les deux bras. »**

**Acceptée.** « Notable chez les juges-modèles » et « promue par le juge figé » ne mesurent pas la même chose. Sans épreuve finale commune, le ratio ne compare rien.

*Correction* : E5 corrigé impose une *épreuve d'audit finale commune* (juge figé sur épreuve fraîche) appliquée aux survivantes des deux bras. La métrique devient « confirmées sur l'audit final / coût total », comparable entre bras.

**A-5. E6 — « Vrai par construction : inverser le signe maximise la divergence KL par construction de la softmax. »**

**Acceptée.** Pour la composante prédictive de la mémoire, une loi à signe inversé a une empreinte prédictive maximalement différente par construction algébrique. Le cas difficile est « même signe, même moniteur, traits ou sous-populations voisins ».

*Correction* : E6 corrigé remplace le bras « signe opposé » par un bras « même signe, même moniteur, traits orthogonaux ou sous-populations disjointes, vocabulaire de surface partagé ». Le bras « même loi, lexique disjoint » (proposé par A) est ajouté. Les quatre croisements sont : (i) même loi / mêmes mots (paraphrase), (ii) même loi / autres mots, (iii) autre loi / mêmes mots, (iv) autre loi / autres mots.

**A-6. Statuts — « VÉRIFIÉ sur simulations non rejouées → OBSERVÉ-NON-AUDITÉ. »**

**Acceptée.** Je n'ai pas rejoué les simulations des pièces 4, 5, 6. Le statut correct est OBSERVÉ-NON-AUDITÉ. Corrigé dans tout le texte.

**A-7. Contrôles négatifs manquants identifiés par A (E1 : « connu + 0 » ; E3 : « fiche vraie sans épreuve → différée » ; E4 : lois figées ; E5 : témoins rhétoriquement conformes classe C ; E6 : « même loi, vocabulaire disjoint »).**

Tous **acceptés** et intégrés dans les expériences corrigées.

**A-8. Conditions de perte de puissance (E1 : P(0/5) ≈ 0,17 ; E3 : espérance ~1 fiche discordante ; E5 : puissance ~0,15 si effet réel = 0,2 ; E6 : n ≥ 40 nécessaire).**

Tous **acceptés comme contraintes de dimensionnement**. Les seuils et effectifs sont corrigés en section b.

---

### Critiques de C sur B

**C-1. E3 — « Dégénérescence : si la puissance du pôle est nulle (pièce 5 : 0/88), survivantes(pôle) = 0 et H_A est faussement réfutée par l'impuissance d'un filtre. »**

**Acceptée.** C'est le même point que A-2, avec une formalisation plus précise. Si p_pôle ≤ 1/(2N), P(D = 0) ≥ 0,606 même sous indépendance. E3 ne peut pas distinguer l'indépendance des filtres de l'extinction du pôle.

*Correction* : E3 corrigé ajoute une condition préalable : l'expérience n'est jouée que si E1 est résolu positivement (le pôle a des dents). H_A et H_B sont reformulées pour exclure le cas dégénéré.

**C-2. E4 — « Fuite de sélection : conditionnement sur U ≥ c crée un biais de troncature ; le ratio R > 1,5 est vrai par construction. »**

**Acceptée.** C formalise précisément le biais que A avait signalé qualitativement. L'espérance conditionnelle E[U − V | U ≥ c] = σ·φ(z_c)/(1 − Φ(z_c)) est strictement positive sous le nul d'absence de fuite. Le seuil 1,5 est franchi par construction dès que la loi est suffisamment tronquée.

*Correction* : E4 corrigé adopte l'estimateur proposé par A — différence (log W_partagée − log W_fraîche)/N — évalué sur des *lois figées sans retour intergénérationnel* (contrôle non héréditaire exigé par C), éliminant le conditionnement sur la promotion.

**C-3. E5 — « Confusion totale entre instrument de sélection et instrument d'évaluation. »**

**Acceptée.** Même critique que A-4, avec la précision que la classe C (creuse mais conforme) passe les juges-modèles.

*Correction* : identique à A-4 (épreuve d'audit finale commune). Ajout de témoins classe C plantés dans le bras sans pôle.

**C-4. E6 — « Survie par construction : le signe inversé maximise la divergence KL. »**

**Acceptée.** Identique à A-5. Correction identique.

**C-5. Contrôle négatif manquant E4 : « fiches neuves de génération 2 sans parents, soumises au même seuil. »**

**Accepté** et intégré dans E4 corrigé comme bras de référence.

**C-6. Contrôle négatif manquant E5 : « épreuve d'audit finale commune. »**

**Accepté.** Identique à A-4.

**C-7. Contrôle négatif manquant E6 : « même signe, même moniteur, traits orthogonaux, vocabulaire partagé. »**

**Accepté.** Identique à la correction de A-5.

---

### Critiques de D sur B

**D-1. E1 — « Transforme un événement existentiel en preuve de fonctionnement. »**

**Acceptée partiellement.** D a raison qu'une seule promotion ne fournit pas un estimateur de puissance. Mais 0/5 sur des témoins de force connue falsifie H_A de manière informative, et ≥1/5 avec 0 faux promu falsifie H_B de manière informative. Le problème est que cinq essais sur une même banque ne sont pas cinq réplications indépendantes.

*Correction* : E1 corrigé exige que les 5 témoins portent sur des moniteurs *distincts* (indépendance approchée) et rapporte un intervalle binomial sur la probabilité de promotion, pas seulement le comptage.

**D-2. E2 — « Ne teste pas le flux opérationnel supposé en S1. »**

**Acceptée.** Une réussite sur 10 n'établit qu'un cas. Le pont peut être fidèle mais stérile, ou utile mais mal calibré.

*Correction* : E2 corrigé sépare explicitement deux métriques : (i) taux de sortie (1 ou 2) avec accord (flux), (ii) taux de témoins correctement classés (fidélité). Le critère L3 de la pièce 7 §g (RAPPORTÉ) reste le critère de mort du pont.

**D-3. E3 — « Ne démontre rien sur la valeur de la conjonction. »**

**Acceptée.** La réduction du nombre de survivantes ne distingue pas les bonnes éliminations des mauvaises. Il faut une vérité externe.

*Transformée en test* : le contrôle ajouté est un ensemble de fiches à *vérité connue* (témoins vrais et faux plantés), jugées par les deux filtres séparément. La métrique devient : le taux de faux négatifs est-il plus élevé sous la conjonction que sous chaque filtre seul ?

**D-4. E4 — « Les mères ne constituent pas un contrôle négatif. »**

**Acceptée.** Identique à A-3 et C-2. Correction identique (lois figées).

**D-5. E5 — « H_A et H_B ne sont ni exclusives ni complémentaires. »**

**Acceptée.** Le rendement par euro et le chevauchement des ensembles éliminés sont deux grandeurs distinctes. H_A et H_B portent sur des estimandes différents.

*Correction* : E5 corrigé restreint H_A et H_B à un seul estimande : le taux de *confirmations sur l'audit final* par bras, à coût fixé. Le rendement par euro est rapporté comme métrique secondaire.

**D-6. E6 — « Deux textes différents peuvent définir la même loi ; deux textes proches peuvent différer hors de la sonde. »**

**Acceptée.** La correction par les quatre croisements (A-5) couvre partiellement ce point. Une sonde scellée indépendante de la mémoire est ajoutée.

**D-7. Contrôles négatifs (E1 : plantation à effet nul ; E3 : filtre dupliqué et fiches à vérité externe ; E4 : lois figées et toutes les filles évaluées ; E5 : parents permutés ; E6 : quatre croisements + baseline lexicale).**

Tous **acceptés** et intégrés.

---

### Critiques de E sur B

**E-1. E1 — « Confond événement et puissance. Une force donnée ne détermine pas la puissance sans distribution des traits, fréquence de l'issue et précision du nul informé. »**

**Acceptée.** L'information par observation I_β dépend de la distribution des traits et de la saturation des probabilités. E1 doit rapporter un intervalle sur π, pas seulement un comptage.

*Correction* : E1 corrigé rapporte (i) le comptage, (ii) un intervalle de Clopper-Pearson sur la probabilité de promotion par moniteur, (iii) la divergence KL effective entre la loi et le nul informé, calculée sur le développement.

**E-2. E2 — « Établit au mieux une capacité locale. Un échec des témoins invalide l'instrument, pas l'hypothèse sur les fiches réelles. »**

**Acceptée.** La distinction est juste : les témoins mesurent l'instrument, les fiches réelles mesurent le flux. Les deux sont nécessaires mais ne répondent pas à la même question.

*Correction* : E2 corrigé sépare les deux questions dans des sous-duels distincts, avec des critères de falsification séparés.

**E-3. E3 — « Oppose des hypothèses mal définies. Pour que l'intersection soit strictement plus petite que chacun des ensembles, il faut des discordances dans les deux directions. »**

**Acceptée.** H_A originale exigeait |survivantes(conjonction)| < min(|S_TdM|, |S_pôle|), ce qui nécessite des discordances dans les deux directions. Avec le pôle à puissance nulle, c'est impossible.

*Correction* : E3 corrigé reformule H_A comme « il existe au moins une fiche survivant à l'un et éliminée par l'autre, dans au moins une direction, sur des fiches à vérité connue ». Le gain de *discrimination* (ratio vrais positifs / faux positifs) est la métrique primaire.

**E-4. E4 — « Sélection avant mesure. La médiane parmi les filles promues est soumise à une troncature par le résultat. »**

**Acceptée.** Identique à A-3 et C-2. Correction identique.

**E-5. E5 — « Ne relie pas correctement mécanisme et rendement. Choisir au moins un axe ajoute une sélection. »**

**Acceptée.** La recherche du meilleur axe après observation est une sélection multiple non corrigée.

*Correction* : E5 corrigé gèle l'axe ou le sous-ensemble de moniteurs *avant* l'observation, par préenregistrement. Le seuil est corrigé pour la multiplicité si plusieurs axes sont testés.

**E-6. E6 — « N'éprouve qu'un cas facile de distinction. »**

**Acceptée.** Identique à A-5, D-6. Correction identique.

**E-7. Contrôles négatifs (E1-E2 : répétitions indépendantes à vérité connue, traductions consensuelles mais fausses ; E3 : fiches vraies rejetées par un seul filtre, fiches fausses acceptées par un seul ; E4 : toutes les filles gelées avant évaluation ; E5-E6 : sélection aléatoire terminalement évaluée, lois équivalentes sous écritures différentes).**

Tous **acceptés** et intégrés.

**E-8. « Séparer validité de l'erreur, puissance conditionnelle à la testabilité, rendement de la politique complète. »**

**Acceptée comme principe directeur.** Les trois paramètres étaient confondus dans la proposition originale. La correction les traite séparément dans des expériences ou sous-duels distincts.

---

## (b) Expériences corrigées

### E1 corrigé — Le pôle a-t-il des dents sur des données non tautologiques ?

- **H_A** : Sur une épreuve fraîche (N ≥ 150 épisodes, jamais vue), le juge figé promeut au moins 1 témoin vrai sur 5, portant sur 5 moniteurs *distincts*, sous e-BH avec m ≤ 20 ; la divergence KL effective (calculée sur le développement) de chaque témoin est rapportée.
- **H_B** : Le juge figé ne promeut aucun de ces 5 témoins.
- **Seuil gelé** : log W ≥ log(m/α), α = 0,05.
- **Témoins vrais** : deux bras — (a) 5 témoins confirmés sur le développement (sélectionnés, puissance optimiste), (b) 5 témoins à force *nominale* (log-rapport de cotes 0,6 converti en KL : *KL = β²·Var(X)·p(1−p)* sous approximation linéaire, HYPOTHÈSE ; la conversion exacte dépend de la distribution jointe trait/issue et est rapportée empiriquement).
- **Contrôle négatif ajouté** : « connu + 0 » (effet nul sur le même moniteur) ; ne doit pas être promu.
- **Contrôle négatif** : ≥ 5 témoins faux (permutation intra-tâche) ; 0 promu.
- **Contrôle « plantation à effet nul »** (D) : même code, même calibrage, même annotation, effet nul ; ne doit pas être promu.
- **Résultat rapporté** : comptage + intervalle de Clopper-Pearson sur π par moniteur + KL effective + W de chaque témoin.
- **Issue qui falsifie H_A** : 0 vrai promu sur les deux bras (10 témoins) et contrôles négatifs éliminés.
- **Issue qui falsifie H_B** : ≥ 1 vrai promu, 0 faux promu, 0 « connu + 0 » promu.
- **Zone indécise** : 0 vrai promu mais KL effective < seuil/N (le pôle n'avait pas la puissance de détecter).
- **Condition matérielle** : épreuve fraîche. Coût inconnu (ABSENT DES PIÈCES).
- **Dimensionnement** : avec π = 0,3 par témoin (illustratif), P(0/5) ≈ 0,17. Avec 10 témoins sur 5 moniteurs, P(0/10) ≈ 0,028 (illustratif, sous indépendance entre moniteurs). La non-indépendance intra-moniteur est rapportée.

### E2 corrigé — Le pont produit-il des lois testables sur des fiches réelles ?

- **Sous-duel A (flux)** :
  - H_A : ≥ 1 sortie (1 ou 2) avec accord, sur 10 fiches.
  - H_B : 0 sortie avec accord.
- **Sous-duel B (fidélité)** :
  - H_A : ≥ 5 témoins sur 6 correctement classés.
  - H_B : < 5 témoins correctement classés.
- **Contrôle ajouté (E)** : une traduction consensuelle mais sémantiquement fausse (banc construit indépendamment des traducteurs) ; doit être détectée par la contre-traduction ou la garde de traçabilité.
- **Rapporté séparément** : taux de sortie 1 vs 2 vs 3, taux de renvois par code, accord inter-traducteurs. Aucune confusion des deux métriques.
- **Coût** : ≤ 5 USD (RAPPORTÉ, pièce 7 §g).

### E3 corrigé — La conjonction test-de-mort ∧ pôle apporte-t-elle un gain de discrimination ?

- **Condition préalable** : E1 résolu positivement (le pôle a des dents).
- **H_A** : Sur des fiches à vérité connue (≥ 5 témoins vrais, ≥ 5 faux, ≥ 5 « vrais mais sans épreuve »), la conjonction a un meilleur ratio vrais positifs / faux positifs que le meilleur filtre seul.
- **H_B** : La conjonction ne fait pas mieux que le meilleur filtre seul en ratio VP/FP.
- **Contrôle « même donnée »** (A) : témoins jugés par les deux filtres sur la partie de développement (même donnée, filtres différents).
- **Contrôle « différé vs éliminé »** (A) : une fiche vraie sans épreuve disponible doit sortir « différée », pas « éliminée ».
- **Contrôle « filtre dupliqué »** (D) : un second pôle identique doit révéler la redondance.
- **Dimensionnement** : avec 15 fiches à vérité connue et des taux de survie ≥ 0,3 par filtre (illustratif), l'espérance de fiches discordantes est ~3 ; jugeable si ≥ 2 discordances dans au moins une direction.

### E4 corrigé — Le renouvellement de l'épreuve empêche-t-il la fuite inter-génération ?

- **H_A** : Avec la *même* épreuve aux générations 1 et 2, la différence normalisée (log W_partagée − log W_fraîche)/N est > 0,02 nat/épisode (illustratif) sur des lois figées sans retour intergénérationnel.
- **H_B** : Cette différence est ≤ 0,02 nat/épisode.
- **Estimateur** : (log W_partagée − log W_fraîche)/N, évalué sur des lois *figées* (pas de sélection, pas de retour), sur les deux épreuves.
- **Contrôle non héréditaire** (C) : fiches neuves de génération 2 sans parents, soumises au même seuil.
- **Réalisable en simulation** (monde planté, pièce 6, OBSERVÉ-NON-AUDITÉ) puis sur données réelles si E1 est résolu.
- **Dimensionnement** : sous le nul, l'optimisme de la sélection du meilleur parmi m est ~log(m)/N par épisode (HYPOTHÈSE, A). À m = 20, N = 150 : ~0,02 nat/épisode. Le seuil est calibré pour détecter un doublement de cet optimisme.

### E5 corrigé — L'ablation du filtre du pôle à la génération 2

- **H_A** : Le taux de confirmations sur un audit final commun (juge figé, épreuve fraîche) est strictement plus élevé dans le bras « avec pôle » que dans le bras « sans pôle », à coût fixé par bras.
- **H_B** : Le taux n'est pas plus élevé.
- **Épreuve d'audit finale commune** (A, C) : juge figé sur épreuve fraîche, appliqué aux survivantes des deux bras.
- **Axe/sous-ensemble gelé** avant observation (E). Si plusieurs axes sont testés, correction de Holm.
- **Contrôle « traduisibles non jugées »** (C) : bras intermédiaire (fiches passant le pont mais non filtrées par le juge figé) pour séparer l'effet de traduisibilité de l'effet du juge.
- **Contrôle « parents aléatoires »** (A, D) : bras à parents tirés au hasard parmi les admissibles, à budget et effectif appariés.
- **Contrôle classe C** (A) : témoins « creux mais conformes » plantés dans le bras sans pôle.
- **Dimensionnement** : avec 20 fiches par bras (4 bras : avec pôle, sans pôle, traduisibles-non-jugées, parents aléatoires) et un taux de confirmation de 0,15 (illustratif), puissance du test exact de Fisher ≈ 0,25 (illustratif). Si le budget permet 40 par bras, puissance ≈ 0,55 (illustratif). Sous-dimensionné en dessous de 40 par bras ; rapporté comme tel.

### E6 corrigé — La mémoire anti-redite distingue-t-elle les hypothèses proches-mais-distinctes ?

Quatre croisements, sur ≥ 40 paires par classe (A, dimensionnement pour séparer 0,8 de 0,5) :

| Classe | Loi | Vocabulaire | Attendu (H_A) |
|---|---|---|---|
| (i) Paraphrase | même | même (reformulé) | refus ≥ 0,8 |
| (ii) Doublon prédictif | même | disjoint | refus ≥ 0,8 |
| (iii) Piège lexical | autre (même moniteur, traits orthogonaux, même signe) | partagé | refus ≤ 0,2 |
| (iv) Contrôle négatif | autre (moniteur et domaine différents) | disjoint | refus ≤ 0,1 |

- **H_A** : La mémoire distingue les quatre classes conformément aux seuils ci-dessus.
- **H_B** : La mémoire confond au moins deux classes (refus dans (iii) > 0,5 ou refus dans (ii) < 0,5).
- **Sonde scellée** (D) : indépendante de la mémoire, gelée avant l'expérience.
- **Réalisable** sur banque synthétique, coût processeur négligeable.

---

## (c) Réponse à la question de l'arbitre — Ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

### Ce qui est établi

- La **plomberie** du pôle tourne de bout en bout : 2 témoins vrais promus, 2 faux éliminés, 11 rejeux confirmés, dans un monde *tautologique* (pièce 4, OBSERVÉ-NON-AUDITÉ). Le mécanisme — gel avant épreuve, juge figé hors des agents, sélection par sévérité — est vérifié dans ce monde.
- Les **simulations du cycle v5** confirment que le seuil par fiche, les marchepieds et la mémoire fonctionnent dans un monde *planté* (pièce 6, OBSERVÉ-NON-AUDITÉ). Aucune fausse promue, aucun témoin vrai éliminé (à 4 traits et 500 tirages).
- Le **pont** est conçu et codé, avec 82 essais sur modèles factices et compatibilité avec la vraie garde v56 sur banques synthétiques (pièce 8, OBSERVÉ-NON-AUDITÉ). Aucun essai sur fiche réelle.

### Ce qui n'est pas établi

- **Le pôle n'a aucune dent sur données réelles** : 0 témoin vrai promu sur 20 en couche 1 (pièce 5, OBSERVÉ-NON-AUDITÉ). La puissance sur des effets réels est inconnue. C'est le *verrou* de toute la boucle génération-à-génération.
- **L'épreuve fraîche n'existe pas** : l'épreuve de T0.5 est entièrement lue (pièce 7 §a.4, RAPPORTÉ). Sans elle, aucune sortie 1 décisive du pont, aucune promotion décisive du pôle.
- **Les tests de mort n'ont jamais été activés** (pièce 1 §9.2, RAPPORTÉ). La conjonction TdM ∧ pôle n'a jamais été instanciée.
- **La recombinaison bisociative et la mémoire ne sont validées que dans des mondes plantés** (pièce 6, OBSERVÉ-NON-AUDITÉ). Aucune mesure sur fiches réelles.
- **Le pont n'a jamais traduit une fiche réelle** (pièce 8, réserve 1, RAPPORTÉ). Les parts attendues des sorties sont SUPPOSÉ.
- **Aucun critère mécanique « neuve par rapport à H1–H9, HC1–HC5 »** n'est décrit dans les pièces. La règle de sortie vers le programme reste HYPOTHÈSE.

### L'expérience à faire en premier

**E6 (mémoire) et E4-simulation (fuite)** sont réalisables immédiatement à coût nul sur processeur. Elles tranchent des questions de conception sans dépense.

**E2 (pont, ≤ 5 USD)** est la première expérience *avec dépense* à lancer : elle informe la viabilité du pont avant tout engagement plus coûteux.

**E1 (dents du pôle)** est le verrou. Tant que le pôle n'a pas de dents sur données réelles, la boucle génération-à-génération est une construction sans preuve empirique. Mais E1 exige une épreuve fraîche dont le coût est absent des pièces. Le **devis de l'épreuve fraîche** (carte graphique, annotation, effectif requis) est donc la première action à résoudre, car elle conditionne E1, E3, E4 sur réel et E5.

**Ordonnancement corrigé** :

1. E6 + E4-simulation (processeur, ~0 USD) → conception de la mémoire et de la rotation d'épreuve.
2. E2 (≤ 5 USD) → viabilité du pont.
3. *Devis de l'épreuve fraîche* (ABSENT DES PIÈCES — nœud budgétaire).
4. E1 (≤ 10 USD + coût de l'épreuve fraîche) → dents du pôle.
5. E3 (E1 résolu + tests de mort activés) → valeur de la conjonction.
6. E5 (≥ 40 fiches par bras × 4 bras, ≥ 60 USD, illustratif) → valeur du filtre.

Tant que l'étape 3 n'est pas résolue, la boucle génération-à-génération reste un plan, pas un dispositif testable.

FIN-DE-CELLULE