# Proposition B — Tour III.3 : Réponse aux critiques, expériences corrigées et synthèse

---

## (a) Réponse à chaque critique visant la proposition B

J'organise par critique, en indiquant la source (A, C, D ou E) et ma décision.

---

### 1. Expérience 1 — « attaquant exhaustif par grille »

**Critique A.1 / C(a).2 / D(a) / E(a)** : Une grille de 10⁴–10⁵ points en dimension 36 n'est pas exhaustive (≈1,3 point par axe). L'attaquant serait plus faible que SLSQP, pas plus fort. Le résultat (disparition ou maintien du cycle) serait un artefact de l'impuissance de la grille. De plus, le plafond CPU de 600 s serait atteint.

**Décision : ACCEPTÉE.** La critique est correcte sur le fond : en dimension 36, aucune grille de taille réaliste ne constitue un « attaquant exhaustif ». C'est une erreur de conception. L'expérience 1 est **retirée** dans sa forme actuelle.

**Transformation en test** : je la remplace par l'**Expérience 1′** (voir section (b)) qui utilise l'attaquant renforcé existant (48 départs, 200 itérations, + stratégie d'évolution (1+12) sans gradient, 400 générations — le même que `attaquant_independant` du code, VÉRIFIÉ sur la pièce 3) appliqué **à chaque tour** de la trajectoire de A, plutôt qu'en finale seulement. Cela teste si les retours persistent quand l'attaquant de chaque tour est rendu plus fort, sans prétendre à l'exhaustivité.

**Critique A.1 (suite)** : Sur un support fini et fixe, l'attaquant répète des points ; I3 devient une fonction du cardinal de la grille.

**Décision : ACCEPTÉE** (conséquence directe du retrait de l'Exp. 1).

---

### 2. Expérience 2 — NashConv et jeu fictif bilatéral

**Critique C(a).3 / E(a) — erreur de formule** : La formule de NashConv que j'ai écrite est algébriquement incorrecte. En § c.3, j'ai écrit NashConv = V(B) + (1 − taux du meilleur moniteur contre le mélange des attaques). À l'équilibre, cela vaut 1, pas 0. VÉRIFIÉ par substitution : si tous les gains valent α, ma formule donne 1.

**Décision : ACCEPTÉE.** C'est une erreur fatale. La bonne définition de l'exploitabilité (gap de dualité) d'un profil (p, q) dans un jeu à somme nulle où le défenseur maximise u et l'attaquant minimise u est :

$$\text{Exploit}(p, q) = \sup_m u(m, q) - \inf_\theta u(p, \theta)$$

Cela s'annule à l'équilibre. Ma formule ajoutait V au lieu de le soustraire du supremum. L'expérience 2 est **corrigée** avec la bonne définition (voir section (b)).

**Critique A.2** : Le NashConv estimé avec des oracles locaux est une borne basse ; « NashConv < 0,05 » est atteignable par faiblesse de l'oracle. Le contrôle Matching Pennies avec SLSQP sur paramètres continus ne joue pas un 2×2.

**Décision : ACCEPTÉE en partie.** (i) L'estimation du sup côté défenseur sous-estime le vrai sup, et l'estimation de l'inf côté attaquant surestime le vrai inf ; l'Exploit estimé est donc une **borne basse** du vrai gap. L'issue « Exploit < 0,05 » (convergence apparente) est non informative car elle pourrait venir de la faiblesse des oracles. Seule l'issue « Exploit > seuil » est informative (non-convergence démontrée). Je reformule le duel en conséquence. (ii) Le contrôle Matching Pennies visait à valider le calculateur. Sur un 2×2, les meilleures réponses sont analytiques ; SLSQP n'est pas nécessaire. Je maintiens le contrôle mais le restreins à un jeu fini résolu par `resoudre_jeu` (VÉRIFIÉ dans le code), pas par SLSQP.

**Critique D(a)** : Un NashConv supérieur à un seuil à T = 8 ne réfute pas une convergence asymptotique sans borne de vitesse.

**Décision : ACCEPTÉE.** Je reformule : l'expérience ne teste pas « le jeu fictif bilatéral converge-t-il asymptotiquement ? » (non tranchable à T fini) mais « à T = 8, la stratégie moyenne du jeu fictif bilatéral a-t-elle une exploitabilité significativement plus basse que celle du dernier itéré de A ? » C'est une comparaison appariée, pas un test de convergence asymptotique.

---

### 3. Expérience 3 — convergence de B à T étendu

**Critique A.3** : « Valeur restreinte − V » n'est pas l'exploitabilité ; V = min de deux évaluations, biais de sélection positif ; à T = 64, ≈31 points par loi d'entraînement, la dégradation de l'oracle imite une non-convergence.

**Décision : ACCEPTÉE en partie.** (i) L'écart valeur restreinte − V n'est qu'une composante côté attaquant du gap. Je le déclare explicitement. (ii) Le biais de sélection (minimum de deux évaluations) est réel mais petit : RAPPORTÉ au brouillon 4, V standard − V renforcé ≤ 0,0011 en moyenne par bras. (iii) Le point sur n_attaque_entr / (T+1) est critique : à T = 64, chaque loi reçoit ~31 points au lieu de ~222 à T = 8. **Correction** : fixer n_attaque_entr proportionnel à T (par exemple 250 × (T + 1)), de sorte que chaque loi reçoit un budget d'échantillons constant. Cela augmente le coût mais isole T de la qualité de l'oracle.

**Critique D(a)** : Les jeux restreints à T différents ne forment pas nécessairement une échelle de métrique commune.

**Décision : ACCEPTÉE.** Je reformule le critère : au lieu de comparer le gap entre T, je compare, à chaque T, V(B) − V(A) (contraste apparié sur les mêmes instances et les mêmes δ). Si B finit par battre A à T suffisant, c'est un signe que le double oracle tronqué bénéficie d'un horizon plus long. Si non, la « réfutation » de Q1 est structurelle.

---

### 4. Expérience 4 — régularisation L2

**Critique A.4 / C(a).4 / D(a) / E(a)** : (i) L'objectif de détection est invariant par homothétie positive de w ; la pénalité ‖w_t − w_{t−1}‖² ne l'est pas. L'optimiseur peut minimiser la pénalité en faisant tendre ‖w‖ → 0. (ii) λ grand fige le moniteur ; I3 → 0 par absence de mouvement, pas par convergence. (iii) V(A) ≈ 0,036 au δ haut : le critère « sans perte » est à l'échelle du bruit. (iv) Sélection du meilleur λ sur les mêmes instances = biais.

**Décision : ACCEPTÉE.** Tous ces points sont corrects. L'expérience 4 est **retirée** dans sa forme actuelle.

**Transformation** : Si la régularisation est testée, elle doit (i) opérer sur la **direction** (pénalité angulaire sur la sphère unité, pas L2 sur les paramètres bruts), (ii) inclure un contrôle « moniteur figé M0 » (borne de convergence triviale), et (iii) séparer sélection de λ et évaluation. Cette transformation est plus lourde qu'une simple correction ; je la déclare comme **expérience future** et ne l'inclus pas dans le plan corrigé.

---

### 5. Expérience 5 — pureté de B′ à T étendu

**Critique A.5** : À T = 32, D reçoit m = t + 1 = 33 unités ; la comparaison n'est plus à classe égale.

**Décision : ACCEPTÉE.** VÉRIFIÉ dans le code (`m_unites = t + 1` dans `trajectoire` pour le bras D). **Correction** : fixer m = 9 (= `unites_Bp`) pour D à tous les T, de sorte que B′ et D gardent la même classe. Cela rompt la continuité avec le pilote (où D a t + 1 unités), ce que je déclare.

**Critique D(a)** : Augmenter T modifie simultanément horizon, nombre d'attaques et matrice.

**Décision : ACCEPTÉE** comme déclaration de portée. L'expérience ne peut pas isoler T d'un changement de richesse du jeu restreint. Je reformule le critère : je ne conclus pas « la pureté vient de T court » ou « la pureté est intrinsèque » ; je rapporte la part pure de B′ et le programme de non-unicité à T = 16 et 32 comme descriptives.

---

### 6. Point S1 — la cible dans l'historique de A

**Critique C(a).1** : La liste `attaques` est initialisée à `[ctx.cible]`. Au tour t, A s'entraîne contre un mélange qui inclut la loi cible non modifiée avec poids 1/(t+1). Ce n'est pas une attaque jouée par l'adversaire ; c'est une ancre fixe.

**Décision : ACCEPTÉE comme précision.** VÉRIFIÉ dans le code (l. ~308). J'avais affirmé (S1) que le mélange uniforme coïncide avec le jeu fictif classique. C'est vrai dans la structure des poids, mais la présence de la cible (δ = 0) comme « attaque du tour 0 » ajoute une régularisation implicite vers la distribution propre. Cela ne change pas la conclusion (A cycle quand même), mais mon affirmation « le bras A est une instance de jeu fictif » doit être nuancée : c'est un jeu fictif avec une ancre.

---

### 7. Synthèse « géométrie orthogonale »

**Critique A.6** : HYPOTHÈSE présentée comme mécanisme.

**Décision : ACCEPTÉE.** Je la re-statuts comme HYPOTHÈSE dans la synthèse corrigée.

---

### 8. Point commun soulevé par A contre toutes les propositions

**Critique A (point commun)** : I3 est calculé sur les attaques du tour (4 départs, 256 MC), pas sur des attaques renforcées ; l'audit part de l'attaque du tour et en reste proche ; aucune proposition n'ajoute le contrôle le moins cher : rejouer la trajectoire de A avec l'attaquant renforcé sans l'attaque du tour comme départ.

**Décision : ACCEPTÉE.** Ce contrôle est intégré dans l'Expérience 1′ corrigée.

---

### 9. Critiques de D et E sur d'autres points

**Critique D(b)** : Classement de pureté fragile quand l'erreur-type des gains (~0,0035) dépasse les seuils 10⁻⁶ ou 10⁻⁹.

**Décision : ACCEPTÉE comme déclaration.** Le programme de non-unicité opère sur G estimé ; la tolérance 10⁻⁹ est nettement sous l'erreur d'estimation. Je déclare que la « pureté forcée » rapportée est conditionnelle à G estimé, pas à G populationnel.

**Critique E(a) — « contrôle constant mal spécifié »** : Un score constant échoue à la garde de variance ; un détecteur aléatoire Bernoulli(α) serait une meilleure référence.

**Décision : ACCEPTÉE pour le contrôle.** Le moniteur constant était un raccourci. Le contrôle approprié est un moniteur qui détecte avec probabilité exactement α sur toute distribution (c'est-à-dire un tirage indépendant). Je l'inclus comme contrôle dans le plan corrigé.

---

## (b) Expériences corrigées

### Expérience 1′ (remplace Exp. 1) : Les retours de A persistent-ils avec un attaquant renforcé à chaque tour ?

**H_A** : I3 − 0,7345 reste > 0 (borne basse B2) quand l'attaquant de **chaque tour** est l'attaquant renforcé (48 départs sans l'attaque précédente comme départ, 512 MC, 200 itérations, + stratégie d'évolution).
**H_B** : I3 − 0,7345 ≤ 0 ; les retours observés étaient un artefact des 4 départs et du départ chaud.

- **Protocole** : pour chaque tâche du pilote (24 instances × 2 δ), rejouer la trajectoire de A en remplaçant `meilleure_reponse` à chaque tour par l'attaquant renforcé du code v4 (`departs_renforce = 48, iter_renforce = 200, n_mc_final = 512`), **sans** l'attaque précédente comme départ supplémentaire (pour éliminer l'inertie de l'optimiseur). Les moniteurs sont ré-entraînés à chaque tour contre les nouvelles attaques. Mesurer I3 sur les déplacements résultants.
- **Contrôle négatif** : le bras D avec le même attaquant renforcé à chaque tour ; I3 − nul doit rester ≤ 0. Si D cycle aussi avec l'attaquant renforcé, l'instrument est invalide.
- **Ce qui falsifie H_A** : borne haute B2 de I3 − nul < 0.
- **Ce qui falsifie H_B** : borne basse B2 de I3 − nul > 0.
- **Coût** : illustratif — ~120 s/tour (8 tours) × 48 tâches = ~12,8 h CPU sur 2 cœurs. Plus cher que le pilote, mais réalisable.

### Expérience 2′ (remplace Exp. 2) : Comparaison appariée de l'exploitabilité du jeu fictif bilatéral et du dernier itéré de A

**H_A** : À T = 8, l'exploitabilité (gap de dualité) de la stratégie moyenne du jeu fictif bilatéral est significativement plus basse que celle du dernier itéré de A (différence > 0,02, borne basse B2 > 0).
**H_B** : La différence est ≤ 0,02 ; le jeu fictif bilatéral ne réduit pas l'exploitabilité à cet horizon.

- **Définition corrigée** : Exploit(p, q) = sup_m u(m, q) − inf_θ u(p, θ). Estimé par : taux du meilleur moniteur (L-BFGS-B, 8 départs) contre le mélange des attaques de q − V(p) avec attaquant renforcé.
- **Déclaration** : l'estimateur est une **borne basse** du vrai gap (sup sous-estimé côté défenseur, inf surestimé côté attaquant). L'issue « Exploit faible » est donc **non informative** (la convergence apparente peut venir de la faiblesse des oracles). Seule l'issue « Exploit(A) > Exploit(FP bilatéral) + 0,02 » est informative.
- **Protocole** : nouveau bras « FP bilatéral » : le défenseur entraîne un moniteur contre le mélange uniforme des attaques passées (comme A) ; l'attaquant cherche la meilleure réponse au mélange uniforme des moniteurs passés (pas au dernier). À T = 8, calculer Exploit de la stratégie moyenne de FP et Exploit du dernier itéré de A, de manière appariée sur les mêmes instances.
- **Contrôle négatif** : jeu 3×3 (pierre-feuille-ciseaux) résolu par `resoudre_jeu` (non par SLSQP) : l'exploitabilité du jeu fictif bilatéral doit décroître en O(1/T) ; la meilleure réponse unilatérale doit osciller.
- **Contrôle supplémentaire** (accepté de A) : le bras « attaquant iid sans mémoire » pour borner la faiblesse de l'oracle.
- **Ce qui falsifie H_A** : borne haute B2 de (Exploit(A) − Exploit(FP)) ≤ 0,02.
- **Ce qui falsifie H_B** : borne basse B2 de (Exploit(A) − Exploit(FP)) > 0,02.

### Expérience 3′ (corrigée) : V(B) − V(A) à T étendu, à budget d'échantillons d'entraînement constant

**H_A** : V(B) − V(A) augmente avec T (B bénéficie d'un horizon plus long).
**H_B** : V(B) − V(A) ne croît pas ; la « réfutation » de Q1 est structurelle.

- **Correction** : n_attaque_entr = 250 × (T + 1) pour chaque T, de sorte que chaque loi d'entraînement reçoit ~250 points. Déclaré : cela change la configuration et l'empreinte.
- **Métrique** : V(B) − V(A) apparié, aux deux δ, à T = 8, 16, 32. L'écart valeur restreinte − V est rapporté comme descriptif (composante côté attaquant du gap seulement, DÉCLARÉ).
- **Contrôle négatif** : V(C3) − V(A) et V(D₉) − V(A) (D à 9 unités constantes, ACCEPTÉ de A/C) aux mêmes T, pour isoler l'effet du double oracle du simple effet d'horizon.
- **Coût** : illustratif — T = 32 avec n_attaque_entr = 8250 : ~300 s/tâche ; 24 × 2 = 48 tâches → ~4 h CPU.

### Expérience 5′ (corrigée) : Pureté de B′ à T étendu, D à classe constante

**Correction** : D fixé à m = 9 unités pour tout T (pas t + 1). Déclaré : rupture de continuité avec le pilote.

- **Métrique** : part pure de B′ et programme de non-unicité à T = 8, 16, 32. DESCRIPTIF — aucun verdict de « la pureté est intrinsèque » ou « vient de T court ».
- **Contrôle négatif** : B (classe linéaire) aux mêmes T ; doit rester non pur.
- **Contrôle de sensibilité** (ACCEPTÉ de C et D) : programme de non-unicité avec tol ∈ {10⁻⁹, 10⁻³, 2σ_G} où σ_G ≈ √(G(1−G)/n_eval) ; rapporter le résultat pour chaque tolérance.
- **Coût** : illustratif — T = 32 : ~300 s/tâche × 48 tâches → ~4 h CPU.

---

## (c) Ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

### Ce qui est établi (conditionnel au monde gaussien synthétique, d = 6, K = 3)

1. **Le bras A ne progresse pas** (I1 ≈ 0 aux deux δ, intervalles excluant un progrès de 0,02 ; RAPPORTÉ, brouillon 4). Statut : RAPPORTÉ.

2. **Les attaques de A reviennent vers d'anciennes au-delà du hasard** (I3 − 0,7345 = +0,17 et +0,21, intervalles excluant zéro ; RAPPORTÉ). Statut : OBSERVÉ-NON-AUDITÉ — l'audit v4 ne change pas I3 (le renforcé part de l'attaque du tour et en reste proche ; RAPPORTÉ). Le contrôle fort (attaquant renforcé à chaque tour, sans départ chaud) n'a pas été fait.

3. **La valeur nulle de I3 est correcte** : formule analytique $\frac{1}{6}\sum_{t=3}^{8}\frac{t-2}{t-1} = 0,7345$ (VÉRIFIÉ par calcul) ; simulation rapportée à 0,7329 ± 0,0012 (RAPPORTÉ, M4 § 9).

4. **B bat A sur (iii) mais perd contre C3 et D** (Q1 réfutée ; RAPPORTÉ). La classe de fonctions déployée (63 paramètres vs. 7) fait plus que le tirage.

5. **La pureté de B′ est forcée par le jeu restreint estimé** (programme de non-unicité : poids max min = 1,000 sur 100% des tâches pures ; RAPPORTÉ). Mais la tolérance du LP (10⁻⁹) est très inférieure à l'erreur d'estimation des gains (~0,0035 ; HYPOTHÈSE illustrative). La pureté populationnelle reste HYPOTHÈSE.

6. **Le bras A joue une variante du jeu fictif unilatéral avec ancre** : pondération uniforme des attaques passées + cible initiale (VÉRIFIÉ dans le code). L'attaquant ne joue pas le jeu fictif (il répond au dernier moniteur, VÉRIFIÉ).

### Ce qui n'est pas établi

1. **Si le cycle est un artefact de l'attaquant local** : non testé avec un attaquant renforcé à chaque tour. Statut : HYPOTHÈSE.

2. **Si le jeu fictif bilatéral converge dans ce monde** : non testé. Le bras A est unilatéral ; aucun bras bilatéral n'existe dans le code. Statut : HYPOTHÈSE.

3. **Si B converge à T plus grand** : non testé au-delà de T = 8. L'écart valeur restreinte − V = +0,019/+0,024 (RAPPORTÉ) est une borne basse de l'exploitabilité côté attaquant, estimée sur un jeu restreint. Statut : HYPOTHÈSE.

4. **Si les résultats se transfèrent aux vrais moniteurs** : explicitement déclaré comme non transférable (brouillon 4, § Portée). Aucune expérience sur des sondes d'activations ou des modèles de langage n'est dans le plan. Statut : HYPOTHÈSE.

5. **Quelle est la bonne métrique de convergence lisible sur de vrais moniteurs** : NashConv exige un jeu restreint complet ; I3 est un proxy dont la valeur nulle suppose l'échangeabilité sous déplacements continus ; I1 est un proxy de progrès à fenêtre courte. Aucune n'est validée sur des moniteurs d'activations réels. Statut : HYPOTHÈSE.

### L'expérience à faire en premier

**L'Expérience 1′** (attaquant renforcé à chaque tour de A, sans départ chaud). Raisons :

1. C'est le contrôle le moins cher du statut de I3. Si les retours disparaissent, tout l'édifice (cycle de la défense unique, analogie avec la non-convergence de Bailey) s'effondre sur un artefact de l'optimiseur. Si les retours persistent, le cycle est une propriété de la dynamique, pas de SLSQP, et les expériences 2′, 3′ et 5′ ont une fondation.

2. Le coût est modéré (~13 h CPU) et ne nécessite aucune modification de la conception du jeu — seulement un remplacement de l'attaquant à chaque tour par le renforcé existant, sans départ chaud.

3. Le contrôle négatif (D avec le même attaquant renforcé) est immédiat et discriminant : D ne doit pas cycler.

4. C'est le point sur lequel toutes les critiques convergent (A le nomme explicitement ; C, D et E le supposent implicitement).

FIN-DE-CELLULE