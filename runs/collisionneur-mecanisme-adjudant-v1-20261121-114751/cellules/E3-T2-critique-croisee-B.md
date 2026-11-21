# Proposition B, tour III.2 : critique croisée de méthode

**Pièces.** J'ai reçu A, C, D et E. Toutes semblent complètes : chacune se termine par FIN-DE-CELLULE. Je n'ai pas recalculé les empreintes. Le bloc FAITS ne porte aucun statut, et je ne lui en attribue pas.

**Statut de ce qui suit.** Mes critiques sont des HYPOTHÈSES. Les calculs élémentaires sont marqués « calcul ». Ils restent à relire et je ne les présente pas comme résultats.

**Lecture de la consigne.** Le livrable de ce tour est la critique. J'applique la question de l'arbitre comme exigence de profondeur : je retiens les défauts qui changent l'issue d'un duel, pas les remarques de forme.

## Quatre contrôles transversaux

Je les numérote Tx et j'y renvoie ensuite.

- **T1. Artefact de fabrication du saboteur.** Si le saboteur est obtenu par consigne ou par affinage, et l'honnête sans ces manipulations, un détecteur peut séparer « consigne présente » de « consigne absente » sans rien savoir du sabotage. Il faut deux contrôles négatifs :
  - une **consigne placebo**, de même longueur et de même registre, sans objectif nuisible ;
  - un **affinage placebo**, même procédure sur données bénignes.

  Leur absence est fatale pour **toutes** les propositions.

- **T2. Statistique de maximum et longueur.** Sans moyenne sur les jetons, toutes les propositions recourent à max_t ou min_t. Si les scores par jeton sont faiblement dépendants, le quantile du maximum croît avec la longueur T de l'épisode (calcul). Un seuil conforme à 1 % sur des épisodes de longueurs mêlées détecte alors surtout la longueur. Il faut un contrôle honnête apparié en longueur et une stratification par T.

- **T3. Population d'étalonnage et hypothèse nulle de déploiement.** Le seuil doit être réglé sur la loi qui tient lieu de H0 en déploiement : *agent honnête* contre jumeau, et non *jumeau* contre jumeau.

- **T4. Conditionner sur l'échec de la sonde.** C'est la cible des duels « second regard » de A, C, D et E.
  - Si P(sonde = 0 | attaque) vaut 1, le taux conditionnel égale le taux marginal. L'« indépendance » est alors vraie par construction.
  - Si cette probabilité vaut 0, le duel n'est pas jugeable.
  - Une variable latente commune, la subtilité ou la difficulté de l'épisode, crée une corrélation sans qu'aucun attaquant l'organise.

  Exigence : le tableau croisé 2×2 publié, une proportion p̂ = P̂(sonde = 0 | attaque) pré-enregistrée dans une bande (par exemple [0,2 ; 0,8], illustratif), et une stratification par difficulté.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **E2 / P3, l'ajout dosé est trivial par construction s'il est injecté à la couche lue.** Pour une sonde linéaire w, ajouter un vecteur v à l'activation lue déplace le score de exactement w·v, quel que soit le contexte (calcul). La « récupération » est alors constante, l'AUROC vaut 0,5 et H_B gagne mécaniquement. L'effet de matrice n'existe que si l'injection est faite *en amont* : à une couche antérieure, ou par sous-tâche rejouée dans l'entrée. A mentionne les deux voies sans voir que la première vide la mesure.

   Si la récupération est lue comme bascule du verdict, elle dépend aussi de la distance |score honnête − seuil| : elle est confondue avec la confiance de base de la sonde.

2. **E4 et P1, biais de sélection des mondes plantés.** Un monde planté est par nature un monde où la vérité est calculable. La part du dommage logée dans le résidu y est donc sous-représentée par rapport aux tâches réelles, et H_A (« P1 supprime au moins 80 % du dommage ») est favorisée par construction de l'échantillon.

3. **La borne de dominance est vraie par construction, mais sup |L − V| n'est pas estimable.** Le maximum empirique sur un échantillon est un minorant du sup. Un attaquant informé place son produit précisément là où |L − V| est grand, c'est-à-dire hors de ce que les mondes plantés échantillonnent. La partie « borne de dommage » de P1 n'a pas d'estimateur.

4. **Les paramètres de la borne d'inspection dépendent de la stratégie de l'attaquant.**
   - s est un paramètre du couple (politique d'attaque, contrôle), pas du contrôle seul : l'attaquant choisit les sabotages que la vérité plantée voit mal.
   - π doit être la probabilité *subjective de l'agent* qu'une tâche soit plantée. E3 mesure la discrimination par un classifieur du défenseur, ce qui n'est pas la même grandeur.

5. **Fuite possible entre réglage et contrôle.** Dans E1, le contrôle négatif « H1, les deux à 1 % » est tautologique si ces épisodes H1 ont fixé les seuils. A exige « H1 frais » pour P4 seulement. L'exigence doit être générale.

6. **E3, généralisation à rebours.** Que le discriminateur du défenseur n'atteigne pas 0,55 ne dit rien d'une classe plus riche. Si discriminateur et pièges viennent du même générateur, l'épreuve est trop facile pour le défenseur.

### (b) Conditions de perte de puissance

| Duel / critère | Perd sa puissance ou devient non jugeable quand |
|---|---|
| E1 | p̂ hors de la bande (T4). Ou bien le nombre k d'échecs de sonde est trop faible : l'intervalle de P(vérificateur échoue \| sonde échoue) a une largeur d'ordre 1/√k, et le seuil RR = 1,5 n'est pas tranchable pour k petit (calcul). |
| E2 | Injection à la couche lue : la variance contextuelle de w·v est nulle. Plus généralement : Var_contexte(effet d'injection) ≪ Var_honnête(score). |
| E3 | La borne supérieure de l'AUROC à 95 % ne descend sous 0,55 qu'avec des effectifs de pièges et de tâches réelles assez grands ; à petit effectif, ni H_A ni H_B ne sont jugeables. |
| Inspection | Quand πs → 0, la borne (1 − πs)/(πs) diverge comme 1/(πs). |
| P4 | n < 99 par régime pour α = 0,01 (A le dit). |

### (c) Contrôles négatifs dont l'absence serait fatale

- T1 (le saboteur de A est obtenu par consigne ou par affinage).
- Pour E2 : la comparaison injection amont / injection à la couche lue. La seconde doit donner une récupération constante ; si elle ne le fait pas, l'instrumentation est fautive.
- Pour E3 : un générateur de pièges tenu à l'écart du discriminateur.
- Pour E4 : des mondes plantés où le dommage est placé *exprès* dans le résidu, comme contrôle positif. Sans eux, le score de 80 % mesure la composition de l'échantillon.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts.** C marque VÉRIFIÉ des énoncés qui ne le sont pas sous la forme donnée.
   - « Probabilité qu'un théorème sémantiquement faux soit intégré bornée par 0 » : Lean garantit la dérivabilité de l'énoncé *formel*, non son adéquation à la question de recherche. C le reconnaît ensuite (truquage de spécification), mais l'étiquette maintient la confusion.
   - La garantie « 1/|G| » est fausse pour un sabotage G-invariant, qui n'a rien à deviner, et pour un attaquant qui canonise l'entrée, ce que C décrit lui-même. Elle ne couvre que les sabotages dont le déclenchement dépend de π, une classe qu'on ne peut délimiter a priori.
   - S5 reçoit le statut OBSERVÉ-NON-AUDITÉ sans source : le dossier ne rapporte aucune observation de ce genre.

2. **B1 / Expérience 2, étalonnage sur la mauvaise nulle (T3).** Le seuil est réglé sur des paires jumeau(x) / π⁻¹ jumeau(π x), mais le test compare agent(x) à π⁻¹ jumeau(π x). Toute différence honnête entre agent et jumeau (prompt, poids, style) devient du « signal ». Le taux de fausses alertes sur agent honnête n'est jamais mesuré. Le contrôle négatif π = Id ne mesure que le bruit numérique, pas la non-équivariance honnête d'un modèle de langage sous renommage. Celle-ci est le vrai concurrent du signal (HYPOTHÈSE à mesurer).

   La température 0 ne garantit pas un déterminisme bit à bit en inférence parallèle. Ordre des réductions flottantes, effets de lot : HYPOTHÈSE à mesurer, référence à vérifier.

3. **A1, le score min_t log P_jumeau a quatre confondants.**
   - La longueur (T2).
   - La température d'échantillonnage de l'agent : à T > 0, un agent honnête émet des jetons de faible probabilité avec une fréquence qui croît avec T.
   - La différence de consigne si agent et jumeau partagent les poids.
   - Le préfixe étranger : après la première divergence, le jumeau est conditionné sur un historique qui n'est pas le sien. Ses probabilités chutent même pour un agent honnête.

4. **Expérience 1, résolution insuffisante.** Avec N = 100 épisodes honnêtes, le rang conforme ⌈101 × 0,99⌉ = 100 fait du seuil le *maximum* honnête (calcul). Le taux de 1 % n'est ni estimé ni vérifiable. Le TPR est en outre conditionné sur les échecs de sonde parmi 100 épisodes sabotés : effectif inconnu, possiblement minuscule (T4).

5. **Fuite.** Le premier pas de A1 utilise « le mode de sabotage tenu à l'écart » du programme. Ce mode est dès lors consommé pour la conception ; l'Expérience 1 doit employer une autre famille, ce que C ne précise pas. Dans C1, la famille « corruption de définitions » est injectée par « on », c'est-à-dire par le défenseur, et non par un tiers.

6. **Lignes de base faibles.** « Battre » `grep sorry`, une variation de température ou la distance de Levenshtein est presque acquis par construction. Ces comparaisons n'informent pas.

7. **C1, juge corrélé.** Le comparateur de rétro-traduction est un modèle de langage non étalonné. Ses angles morts peuvent coïncider avec ceux de l'agent, c'est le mode commun.

### (b) Conditions de perte de puissance

- **A1.** Soit τ_α le quantile à 1 % de min_t log P_jumeau sous la loi honnête. Toute politique Q dont le support, à chaque pas, exclut les jetons de log-probabilité inférieure à τ_α a une puissance nulle, inférieure même à α (calcul). Une dérive de divergence KL δ par pas, cumulée sur T pas, reste invisible au minimum tant que les jetons restent dans ce support. C l'admet dans son test de mort, mais en fait une famille d'attaque alors que c'est une propriété de la statistique.
- **B1.** Si le quantile à 99 % de Δ_π sous honnête dépasse la médiane de Δ_π sous sabotage, alors TPR ≤ 50 % (calcul). Si le sabotage est G-invariant (la loi de la sortie commute avec g), la loi de Δ_π est inchangée et la puissance vaut α.
- **Martingale conforme.** Si les p-valeurs sous attaque sont uniformes (variation totale nulle sur le trait d'étrangeté), M_n ne croît pas. Si les tâches honnêtes dérivent dans le temps, ce qui est la nature d'un programme de recherche, l'échangeabilité tombe et la garantie de fausses alertes avec elle.
- **C1.** Le TPR est estimé sur m définitions corrompues ; avec m petit, le seuil de 90 % n'est pas tranchable.

### (c) Contrôles négatifs dont l'absence serait fatale

- T1, T2, T3.
- Pour B1 : un agent honnête contre jumeau sous π ≠ Id.
- Pour A1 : des épisodes honnêtes appariés en température et en longueur.
- Pour C1 :
  - des requêtes délibérément permutées, contrôle positif que le juge doit détecter ;
  - des renforcements d'hypothèse honnêtes et équivalents, contrôle négatif. C ne propose que le renommage des lemmes, trop facile.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **La règle de décision du duel commun est satisfaite par construction à petit effectif.**
   - H_A exige f ≤ 1 % *en estimation ponctuelle* par régime. Avec moins de 100 témoins, f = 0 suffit : tout instrument peu bavard passe.
   - « d dépasse strictement » le comparateur, sur estimations ponctuelles : le signe de l'écart peut être dû au bruit.

   Les deux issues « falsifient » alors nominalement, et l'exigence B4 n'est remplie qu'en apparence. D signale la limite en prose, mais la règle ne l'encode pas. Il faut des bornes de confiance pré-enregistrées et une marge.

2. **Asymétrie de sélection.** L'instrument est gelé ; le comparateur est « le plus performant choisi sur développement ». Le gagnant sur développement régresse vers la moyenne en test, ce qui favorise H_A. Comparer aussi au meilleur comparateur *en test*, à titre de sensibilité.

3. **La porte provisionnée est tautologique si le dommage est mesuré dans l'unité de la porte.** « Aucun dépassement du budget déclaré » est vrai par construction si le code de la porte est correct. Le duel éprouve l'implémentation, ce qui est utile, mais pas la pertinence de la borne. D le reconnaît (« la provision doit majorer l'effet réel »). Pourtant son registre de vérité « dommage réalisé » n'est pas défini indépendamment de c_i. Sans mesure aval indépendante, par exemple la perte de décision en monde planté, la boucle est fermée.

4. **Passeport : le comparateur « liste » est aveugle par construction sur la famille choisie.** Sur une famille « à manifeste familier », la liste a d = 0 ; le score de rang la bat dès que d > 0. Le comparateur pertinent est un **routage aléatoire au même taux**, qui donne d = f.

### (b) Conditions de perte de puissance

| Critère | Perd sa puissance ou devient non jugeable quand |
|---|---|
| f ≤ 1 % au niveau population | Avec zéro alerte sur n témoins, la borne supérieure à 95 % vaut environ 3/n (calcul). Il faut donc n ≳ 300 par régime pour établir 1 %. En deçà, le critère est non jugeable. |
| Comparaison de d | L'écart-type de la différence est d'ordre √(d(1 − d)/m), où m est le nombre d'attaques manquées par la sonde. T4 s'applique. |
| Passeport | Si la loi des descripteurs sous le régime tenu à l'écart égale la loi honnête (variation totale nulle), la puissance vaut α. D le dit lui-même. |
| Porte | Si P(dommage réel ≤ c_i) < 1, l'énoncé ne borne que Σ c_i, plus le dommage. |

### (c) Contrôles négatifs dont l'absence serait fatale

- T1.
- Le routeur aléatoire au même taux (passeport).
- Pour la porte : un dommage aval mesuré hors de la comptabilité de la porte, sur transactions honnêtes et plantées. Sans lui, le duel ne teste que du code.

D est la proposition la plus sobre. Ses défauts tiennent aux règles de décision, pas aux mécanismes.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Statuts.**
   - E attribue RAPPORTÉ aux énoncés du dossier, qui n'en portent aucun.
   - E marque OBSERVÉ-NON-AUDITÉ des affirmations sans observation citée, par exemple la corrélation des pannes « en IA ».
   - E marque VÉRIFIÉ, « par définition », « toute mathématique nouvelle est hors distribution ». Ce n'est vrai qu'au regard d'une représentation Φ donnée : une nouveauté sémantique peut avoir une loi projetée identique.
   - L'énoncé de CIPAC (« une mathématique nouvelle honnête commute avec le groupe ») est une HYPOTHÈSE présentée comme un fait.

2. **La borne (1 − δ)^k est vide pour le sabotage discret.** δ est choisi par l'attaquant. Avec une seule obligation viciée sur m, δ = 1/m et la probabilité d'évasion vaut environ (1 − 1/m)^k ≈ 1 − k/m (calcul). La borne tient exactement là où le problème n'est pas posé.

3. **L'audit d'information mutuelle de DCGA va dans la mauvaise direction.** L'exactitude d'un classifieur de ré-identification **minore** l'information mutuelle : un classifieur qui échoue ne certifie pas I ≤ ε. L'audit peut réfuter ε, jamais l'établir. Par ailleurs, un seul bit (« est-ce le projet sensible ? ») peut suffire à l'attaquant. La borne de Fano sur l'erreur d'estimation ne borne pas l'avantage d'une décision binaire grossière.

4. **SAPPA confond étalonnage et honnêteté.**
   - L'inégalité de Ville exige que, sous H0, l'issue suive la loi *déclarée* par l'agent. Un agent honnête mal étalonné fait croître le processus : les fausses alertes ne sont pas contrôlées.
   - L'agent agit sur l'issue qu'il prédit. Il peut rendre ses prévisions autoréalisatrices.
   - La conversion « score de Brier vers processus-e » n'est pas spécifiée. Un score de Brier n'est pas une e-valeur ; il faut une mise dont l'espérance est au plus 1 sous la prévision déclarée.

5. **CCDE, fuite entre construction et évaluation.** Si la décomposition SVD et les rangs conformes sont calculés sur les mêmes épisodes honnêtes, l'échangeabilité entre étalonnage et test est rompue. Il faut un découpage, donc au moins deux fois plus d'épisodes que les 99 requis.

   Avec N ≪ d (la dimension des activations), le sous-espace estimé est presque l'espace engendré par les échantillons. Le résidu d'un nouvel épisode honnête est alors grand, et la puissance s'effondre.

6. **E4, confusion entre nouveauté et attaque.** Le contrôle négatif « nouveau domaine honnête doit router » a une issue attendue positive : ce n'est pas un contrôle négatif. Si les attaques tierces portent sur des tâches nouvelles, le routage est élevé par la seule nouveauté.

7. **CIPAC, auto-correction BLR.** La garantie suppose un homomorphisme exact sur un groupe. Les artefacts de recherche (estimateurs, code) n'ont en général pas d'auto-réductibilité aléatoire. Les « copies amnésiques » de mêmes poids retombent dans le mode commun que E cite lui-même (Knight et Leveson).

### (b) Conditions de perte de puissance

- **CIPAC.** Si le sabotage est G-équivariant (loi de f(gx) = g de la loi de f(x)), la loi du résidu est inchangée et la puissance vaut α. Si la variance honnête du résidu domine le décalage induit, idem au seuil de 1 %.
- **Entropie privée.** Pour δ ≤ 1/m, k ≪ m : vide.
- **SAPPA.** Si l'écart d'étalonnage honnête E[log(r_t / p_t)] est strictement positif, où r_t est la vraie loi de l'issue et p_t la prévision, une mise de type rapport de vraisemblance croît sous honnête. La probabilité de franchir 100 tend vers 1 avec l'horizon (calcul).
- **CCDE.** Effectif après découpage inférieur à 99, ou rang de troncature proche de N.
- **DCGA.** Aucune garantie ε n'est jugeable sans la loi jointe ; l'estimateur n'en fournit qu'un minorant.

### (c) Contrôles négatifs dont l'absence serait fatale

- T1 et T2.
- Pour SAPPA : un agent honnête *mal étalonné*, par exemple un modèle honnête plus faible.
- Pour CCDE : un nouveau domaine honnête **apparié en tâches** aux attaques.
- Pour DCGA : des énoncés non anonymisés qui doivent être ré-identifiés. C'est le contrôle positif de puissance du classifieur, sans lequel son échec ne signifie rien.

---

## Ce que je reprends, en le disant

- **De A :** la clause « non concluant si la sonde n'échoue presque jamais ». Je l'étends en T4 aux deux bords et à la variable latente de difficulté.
- **De D :** la séparation, dans le registre, entre « produit refusé » et « sabotage détecté ».

**Sur les références.** La datation de Greenblatt et coll. diverge : 2023 chez A, 2024 chez C et E. Prépublication et publication peuvent expliquer l'écart ; référence à vérifier.

FIN-DE-CELLULE