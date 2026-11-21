# Proposition B — Tour III.3 : réponse aux critiques

**Pièces reçues.** Ma conception III.1 et les quatre critiques croisées (A, C, D, E) sont présentes, non vides, et se terminent par leur marque de fin. Je ne réponds qu'aux sections « Sur la proposition B ». J'ajoute le préambule de D, qui est général mais réfute une affirmation de mon P3 ; je l'indique à chaque endroit où je m'en sers.

**Statuts.**
- **RAPPORTÉ** : les faits, les décisions du programme et le contenu des critiques.
- **VÉRIFIÉ** : seulement ce que j'ai recalculé moi-même.
- **HYPOTHÈSE** : tout le reste, y compris chaque expérience proposée.

Les chiffres des critiques gardent le statut que leur auteur leur a donné.

**Bilan.** Quatre affirmations de III.1 tombent :
1. E2, telle qu'écrite, ne peut pas fonder la garantie de Ville.
2. « Pas de calibration par bac pour P3 » est faux pour la cible par bac.
3. Le regroupement des bacs (E1, P2) n'est ni jugeable ni identifiable.
4. M4 est dégénéré.

P4 est rétrogradé.

---

## (a) Décision, critique par critique

### Critiques de A

| # | Critique | Décision | Raison ou test |
|---|---|---|---|
| A-a1 | P3 teste « agent = jumeau », pas « agent honnête » | **Acceptée sous condition, transformée en test** | Le programme prévoit un jumeau honnête apparié (RAPPORTÉ). Le nul de P3 n'est donc un nul d'honnêteté que si l'agent honnête déployé a les mêmes poids, la même invite visible et le même décodage que le jumeau. Test T-A1 en (b). |
| A-a2 | Deux régimes non séparés | **Acceptée** | R1 : mêmes poids, consigne cachée différente. R2 : poids différents. En R2, le jumeau doit être affiné par la même procédure sur des données bénignes. Cette idée vient de la critique de A envers E (point 9) ; je la reprends en le disant. |
| A-a3 | E2 : non-rejet pris pour preuve ; KS inadapté au discret ; pas dépendants ; uniformité marginale ≠ E[e_t∣passé] ≤ 1 | **Acceptée en entier** | E2 est réécrite (E2′). |
| A-a4 | E3 et E4 falsifient H_A par manque de puissance | **Acceptée** | J'adopte la règle de marge g de D, que A reprenait déjà. Une borne haute ≤ g falsifie H_A ; une borne basse > g falsifie H_B ; un chevauchement est « non concluant ». |
| A-a5 | M4 est vrai ou faux par construction | **Acceptée. M4 retiré.** | À poids et entrée identiques, la passe avant est déterministe. |
| A-a6 | La normalisation est choisie sur les épisodes qui servent ensuite à la tester | **Acceptée** | Toute normalisation est ajustée sur des familles de tâches disjointes de celles de calibration et de test. |
| A-a7 | Le coût de P3 est récurrent | **Acceptée** | Coût = K × points de contrôle × épisodes surveillés, en continu. P3 devient un outil de validation et d'audit ciblé, pas une surveillance de tout le flux. |
| A-b | Transport de Ville sous inflation ε : borne (1+ε)^T/100 | **Acceptée** | Recalcul : si E[e_t∣F_{t−1}] ≤ 1+ε, alors M_t/(1+ε)^t est une surmartingale, d'où la borne (VÉRIFIÉ). Conséquence : vérifier Ville empiriquement à 1 % n'est pas jugeable avec quelques centaines d'épisodes. Seuls des niveaux grossiers le sont. |
| A-b | Dérive de log e_t ≤ 0 si le saboteur garde des rangs centraux | **Acceptée** | C'est une limite de puissance structurelle de P3, déclarée. |
| A-b | E1 demande environ 400 tâches par bac ; une invariance au quantile 90 % ne dit rien du quantile 99 % | **Acceptée. E1 retirée.** | — |
| A-b | P1 doit se lire en effectif efficace n_eff | **Acceptée** | J'avais posé S2 sans l'appliquer au chiffre 299 : erreur de ma part. |
| A-b | M1 : la loi de la covariable peut différer entre régimes | **Acceptée** | La covariable est désormais lue sur le jumeau (voir C-a4). |
| A-c | Contrôles : agent honnête différent ; niveaux de Ville 5 et 10 ; dépendance sérielle par permutation entre épisodes ; masque de neurones aléatoire ; cellule « saboteur assigné sans dommage » | **Acceptée** | Tous intégrés en (b). |

### Critiques de C

| # | Critique | Décision | Raison ou test |
|---|---|---|---|
| C-a1 | Pré-test E1 puis Wilks sur les mêmes données ; égalité à 90 % ⇏ égalité à 99 % | **Acceptée** | C résume E1 par « si l'invariance n'est pas rejetée », alors que E1 exigeait une équivalence dans une marge. Le fond reste juste : la sélection sur les mêmes données invalide (1−α)^n. |
| C-a2 | KS continu sur rangs discrets : rejet par construction | **Acceptée** | Recalcul : avec F₀(u) = ⌊(K+1)u⌋/(K+1), on a sup_u ∣F₀(u)−u∣ = 1/(K+1), non atteint (VÉRIFIÉ). C donne la borne inférieure 1/(2(K+1)), E la valeur 1/(K+1). La conclusion est la même dans les deux cas. |
| C-a3 | Pas d'un même épisode non indépendants | **Acceptée** | L'unité devient la tâche. |
| C-a4 | V̂₀ lu sur l'agent est postérieur au régime | **Acceptée, transformée** | V̂₀ est lu sur le **jumeau**, depuis l'énoncé public de la tâche. C'est alors une fonction de la tâche seule. Le canal d'évasion de M1 se ferme, au prix de toute information propre à l'agent. |
| C-b1 | E1 condamnée à « non concluant » (demi-largeur ≈ 8,3 points à n_b ≈ 100) | **Acceptée** | Recalcul de l'écart-type √(2·0,09/100) ≈ 4,24 points : concordant. |
| C-b2 | Le calibrateur κp^(κ−1) sur rangs discrets cause une « perte de validité » | **Partie validité : rejetée.** **Partie puissance : acceptée.** | Pour f décroissante, la somme de Riemann à droite est inférieure ou égale à l'intégrale. Le calibrateur reste donc valide et conservateur ; C écrit d'ailleurs lui-même « conservatisme strict ». Puissance : e_max ≈ 1,658 pour κ = 0,5 et K = 10 (illustratif chez C). Il faut alors au moins 10 points de contrôle au rang maximal. Le calibrateur est remplacé. |
| C-b3 | Wilks au maximum : taux réalisé médian ≈ 0,23 %, perte de détection | **Acceptée** | Je l'avais dit qualitativement ; la quantification de C est illustrative. |
| C-c1 | Sonde de même architecture sur des neurones aléatoires ou de prédiction du jeton suivant | **Acceptée** | Ajoutée comme base de E3′ et E4′. |
| C-c2 | Obstacle honnête imprévu à V̂₀ élevé | **Acceptée** | Contrôle négatif de E4′. |

### Critiques de D

| # | Critique | Décision | Raison ou test |
|---|---|---|---|
| D-préambule | p_b = P_H(A∣B=b) n'est pas donnée par P_H(A) ≤ α ; une alerte peut fixer la tranche | **Acceptée. Mon affirmation « pas de calibration par bac » est retirée.** | Ville borne le taux marginal. La validité par bac exige que la longueur réalisée ne dépende pas des rangs (HYPOTHÈSE), ou une vérification par bac. J'adopte, en le disant, la décision de D : évaluer le détecteur en lecture seule sur des trajectoires non interrompues, et la politique d'intervention séparément. |
|