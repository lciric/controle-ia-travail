# Proposition B — Tour III.1 : Formalisation, cycle et convergence de la défense unique ré-entraînée

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite de la question | Statut | Justification |
|---|---|---|---|
| S1 | Le bras A est une instance de « jeu fictif d'un seul côté » | HYPOTHÈSE | Le brouillon 4 décrit A comme ré-entraînant un moniteur linéaire contre le mélange uniforme de toutes les attaques passées, l'attaquant jouant ensuite en meilleure réponse au dernier moniteur. Cela ressemble au jeu fictif côté défenseur, mais deux écarts doivent être vérifiés : (i) l'oracle « maximiser la détection lissée à α fixé » n'est pas une réponse exacte à la matrice de gains — c'est une heuristique d'entraînement qui approche la meilleure réponse sans la garantir (l'objectif est lissé, le seuil est gaussien) ; (ii) le mélange est uniforme sur les attaques, alors que le jeu fictif classique pondère par la fréquence cumulée des stratégies jouées, ici égale à 1/t pour l'attaque du tour t, ce qui coïncide avec l'uniforme uniquement si chaque attaque n'est jouée qu'une fois — c'est le cas dans le code (VÉRIFIÉ : `arene_melange_v4.py`, l. ~348, `np.full(len(attaques), 1.0 / len(attaques))`) |
| S2 | Le cycle observé (I3 − nul > 0) est une propriété de la dynamique, pas un artefact de la mesure | OBSERVÉ-NON-AUDITÉ | I3 − nul est rapporté au pilote v4 à +0,17 et +0,21 avec intervalles excluant zéro (RAPPORTÉ, brouillon 4, résumé point 6). Cependant : l'attaquant est un optimiseur local (SLSQP, 4 départs) qui n'explore pas la boîte entière — les « retours » pourraient refléter un biais systématique de l'optimiseur plutôt qu'une propriété du jeu. L'audit v4 (RAPPORTÉ, 10 tâches) ne change pas I3 (brouillon 4, S17 : « la réponse renforcée part de l'attaque du tour et en reste proche : contrôle faible de la forme »). I3 reste **non audité au sens fort** |
| S3 | Le « monde gaussien » est un proxy informatif pour les vrais moniteurs d'activations | HYPOTHÈSE | Déclaré explicitement comme non transférable : « Aucune lecture ne réfute ni ne confirme la piste 3 sur de vrais moniteurs » (brouillon 4, § Portée). La question suppose néanmoins que les mécanismes de cycle et de convergence se transfèrent |
| S4 | L'oracle « détection » (maximiser le taux de détection lissé à fausses alertes fixées) est un choix de gain qui ne change pas la structure du jeu | HYPOTHÈSE | L'oracle rend un problème d'optimisation bilinéaire (pour m = 1, linéaire en W) seulement en approximation gaussienne. Pour m > 1 (maxout), la somme-exp brise la linéarité. Le jeu résultant n'est pas un jeu bilinéaire classique, et les théorèmes de convergence du jeu fictif (qui supposent une somme nulle bilinéaire ou un jeu à actions finies) ne s'appliquent pas directement |
| S5 | La pureté des poids de B′ est « imposée par le jeu » au sens d'un équilibre unique | RAPPORTÉ | Le programme linéaire de non-unicité (brouillon 4, `poids_max_min_equilibres`) rend un plus petit poids maximal de 1,000 pour toutes les tâches pures. Mais ce programme résout sur le jeu *restreint* (≤ 9 moniteurs × ≤ 9 attaques) : le jeu continu peut avoir des équilibres intérieurs dont le jeu restreint ne rend pas compte |
| S6 | Les résultats de convergence du jeu fictif classique (Brown 1951, Robinson 1951) sont directement applicables | HYPOTHÈSE | Ces résultats valent pour des jeux finis à somme nulle à deux joueurs ; ici le jeu a des espaces continus (paramètres de la loi d'attaque, hyperplan du moniteur), un oracle approché, et un seul côté joue le jeu fictif |
| S7 | La question 6 (transfert) suppose que des travaux publiés existent sur la co-évolution moniteur–attaquant pour des sondes d'activations | HYPOTHÈSE | Je n'ai pas de référence vérifiable sur ce sujet précis au-delà de Bailey et collègues (arXiv 2412.09565, lu par session-depot — RAPPORTÉ). Les autres travaux supposés (entraînement adversarial de sondes, PSRO sur des modèles de langage) sont à ma connaissance non publiés ou non vérifiables dans le cadre de ce protocole |

---

## (b) Expériences décisives, chacune en duel H_A / H_B

### Expérience 1 : Le cycle est-il un artefact de l'optimiseur local ou une propriété du jeu ?

**H_A** : Le cycle (I3 − nul > 0) persiste avec un attaquant exhaustif (grille dense dans la boîte de contrainte).
**H_B** : Le cycle disparaît (I3 − nul ≤ 0) quand l'attaquant est exhaustif — le cycle observé est un artefact de la myopie de SLSQP.

- **Métrique** : I3 − 0,7345 aux deux δ, même intervalle B2 que le brouillon 4.
- **Seuil** : borne basse B2 de I3 − nul > 0 (H_A non réfutée) vs. borne haute B2 < 0 (H_A réfutée) ; N = 24 instances (pilote), même racine, mêmes moniteurs.
- **Contrôle négatif** : sur le bras D (maxout unique), qui ne cycle pas (I3 − nul = −0,28 et −0,38 au pilote v4, RAPPORTÉ) ; un attaquant exhaustif ne doit pas y créer de cycle.
- **Protocole** : remplacer `meilleure_reponse` pour A par une grille de $G$ points dans la boîte à δ fixé (projection sur la contrainte de distance), évaluer le taux de détection de chacun, retenir le plus bas. $G$ = 10 000 à 100 000 selon le coût.
- **Ce qui falsifie H_A** : I3 − nul tombe dans l'intervalle de D (≤ 0) avec l'attaquant exhaustif.
- **Ce qui falsifie H_B** : I3 − nul reste significativement positif (+0,10 ou plus) même avec l'attaquant exhaustif.
- **Coût** : illustratif — chaque évaluation de grille coûte $G × K × n_{eval}$ opérations de score ; pour $G = 10^4$, ~10× le coût actuel par tour, soit ~600 s par tâche au lieu de 60 s ; 24 × 2 = 48 tâches → ~8 h CPU sur 2 cœurs.

### Expérience 2 : Le cycle disparaît-il quand les deux côtés jouent le jeu fictif (mélange uniforme des stratégies passées) ?

**H_A** : Le jeu fictif bilatéral (le défenseur mélange uniformément ses moniteurs passés comme B, l'attaquant mélange uniformément ses attaques passées — les deux jouent la meilleure réponse au mélange de l'autre) converge au sens de NashConv → 0.
**H_B** : Le jeu fictif bilatéral ne converge pas non plus (NashConv reste borné loin de zéro) — le problème est dans la classe de fonctions ou l'oracle, pas dans la règle unilatérale.

- **Métrique** : NashConv au tour T, défini comme la somme de l'exploitabilité des deux joueurs : $\text{NashConv}_T = \max_q \text{taux}(\text{défense}_T, q) - \min_q \text{taux}(\text{défense}_T, q) + \max_m [1 - \text{taux}(m, \text{attaque}_T)]$ (symétrisé). Lisible comme la meilleure réponse de chaque côté à la stratégie moyenne de l'autre.
- **Seuil** : NashConv à T = 8 < 0,05 (H_A non réfutée) vs. > 0,10 (H_A réfutée). Entre les deux : non tranché (T trop court).
- **Contrôle négatif** : jeu de Matching Pennies (pile ou face apparié, 2×2) avec la même bibliothèque d'optimisation : NashConv → 0 à taux 1/T (théorème classique, référence à vérifier : Robinson 1951, « An iterative method of solving a game »).
- **Protocole** : nouveau bras « FP bilatéral » : le défenseur entraîne un moniteur contre le mélange uniforme des attaques passées (comme A), l'attaquant cherche la meilleure réponse au mélange uniforme des moniteurs passés (pas au dernier). Évaluer NashConv à chaque tour.
- **Ce qui falsifie H_A** : NashConv reste > 0,10 à T = 8 (la convergence théorique du jeu fictif ne se manifeste pas dans ce monde, probablement parce que les meilleures réponses sont approchées).
- **Ce qui falsifie H_B** : NashConv < 0,05 à T = 8 — le jeu fictif bilatéral converge, et le cycle du bras A vient bien de l'unilatéralité.
- **Coût** : illustratif — même coût que le bras A (la seule différence est que l'attaquant résout contre le mélange des moniteurs, ce qui coûte un facteur T en évaluation de défense mixte par départ), soit ~120 s par tâche (double du bras A actuel) ; 24 × 2 = 48 tâches → ~1,5 h CPU.

### Expérience 3 : La convergence du mélange d'équilibre (B) à classe linéaire est-elle réelle malgré la « réfutation » de Q1 ?

**H_A** : B converge au sens de NashConv (l'exploitabilité du jeu restreint diminue avec T), même si V(B) < V(D) — la convergence et la performance sont deux choses distinctes.
**H_B** : B ne converge pas au sens de NashConv — le double oracle à T tronqué ne réduit pas l'exploitabilité.

- **Métrique** : écart entre la valeur du jeu restreint de B et V(B) (= exploitabilité résiduelle côté attaquant), rapporté au pilote v4 comme +0,019 / +0,024 (RAPPORTÉ, brouillon 4, résumé point 5 et M4 § 6).
- **Seuil** : ce même écart à T = 16, 32, 64 (extension) ; convergence si l'écart décroît comme O(1/√T) ou mieux ; non-convergence si l'écart reste > 0,01 à T = 64.
- **Contrôle négatif** : le bras A doit avoir une exploitabilité qui ne décroît pas (plate ou croissante).
- **Ce qui falsifie H_A** : l'écart ne diminue pas avec T.
- **Ce qui falsifie H_B** : l'écart diminue régulièrement — B converge, mais lentement, et la « réfutation » de Q1 est un effet de T trop court.
- **Coût** : illustratif — T = 64 coûte 8× le pilote actuel par tâche, soit ~480 s/tâche ; 24 × 2 = 48 tâches → ~6,5 h CPU.

### Expérience 4 : La régularisation vers les moniteurs passés brise-t-elle le cycle de A ?

**H_A** : Un bras A_reg qui ajoute une pénalité de distance L2 au moniteur du tour précédent (average anchoring : $\lambda \|w_t - w_{t-1}\|^2$ dans l'objectif de détection) réduit I3 − nul vers zéro et augmente I1 (progrès).
**H_B** : A_reg ne brise pas le cycle (I3 − nul reste > 0) ou brise le cycle au prix d'une détection réduite (V(A_reg) < V(A)).

- **Métrique** : I3 − nul de A_reg aux deux δ ; V(A_reg) aux deux δ ; I1 de A_reg.
- **Seuil** : « brise le cycle sans perte » si I3 − nul ∈ [−0,05 ; +0,05] ET V(A_reg) ≥ V(A) − 0,01 ; « brise le cycle avec perte » si I3 − nul ∈ [−0,05 ; +0,05] ET V(A_reg) < V(A) − 0,01 ; « ne brise pas le cycle » sinon.
- **Contrôle négatif** : λ = 0 reproduit exactement A (même code, même résultat au bit).
- **Ce qui falsifie H_A** : I3 − nul reste > +0,10 pour tout λ ∈ {0,01 ; 0,1 ; 1,0 ; 10}, ou V chute sous 2α.
- **Ce qui falsifie H_B** : un λ* existe tel que I3 − nul ∈ [−0,05 ; +0,05] et V(A_reg) ≥ V(A) − 0,01.
- **Coût** : illustratif — 4 valeurs de λ × 24 instances × 2 δ = 192 tâches × ~8 s (A seul, pas 8 bras) → ~26 min CPU.

### Expérience 5 : La pureté de B′ est-elle un artefact de la richesse de la classe, et peut-on la briser ?

**H_A** : La pureté est intrinsèque : pour des moniteurs de classe suffisamment riche (maxout ≥ 9 unités), le jeu restreint a presque toujours un équilibre pur parce qu'un seul moniteur « couvre » l'espace des attaques faisables.
**H_B** : La pureté est un artefact du petit nombre de tours (T = 8) : à T plus grand, de nouvelles attaques entrent dans le jeu restreint et forcent un mélange.

- **Métrique** : part des tâches pures de B′ à T = 8, 16, 32 ; plus petit poids maximal parmi les équilibres.
- **Seuil** : part pure < 0,3 à T = 32 (H_B non réfutée) ; part pure > 0,7 à T = 32 (H_A non réfutée).
- **Contrôle négatif** : B (classe linéaire) doit rester non pur (support moyen 3,7 au pilote, RAPPORTÉ).
- **Ce qui falsifie H_A** : la part pure chute significativement avec T et tombe sous 0,3 à T = 32.
- **Ce qui falsifie H_B** : la part pure reste > 0,7 à T = 32, et le programme linéaire de non-unicité confirme la pureté forcée.
- **Coût** : illustratif — T = 32 × maxout = ~240 s/tâche (4× le pilote) ; 24 × 2 = 48 tâches → ~3,2 h CPU.

---

## (c) Mesures minimales pour chaque instrument nommé dans la question

### c.1 — Le bras A (défense unique ré-entraînée)

**Ce qu'il faut démontrer pour dire qu'il « fonctionne » (au sens de : il capture la non-convergence)** :

1. **Taux de détection** : V(A) > 2α aux deux δ (A n'est pas au plancher). RAPPORTÉ : 0,082 et 0,036 au pilote v4 (8,2α et 3,6α). Au δ haut, 3,6α est proche du plancher ; la question de la convergence y a peu de mordant.
2. **Fausses alertes** : |FPR − α| ≤ 0,005. RAPPORTÉ : écart ≤ 0,0002 (brouillon 4, M4 § 6).
3. **Cas honnêtes appariés** : les mêmes 24 instances, mêmes lois cibles, mêmes échantillons communs ; la seule différence est la trajectoire du bras.
4. **Vérification mécanique à battre** : un moniteur constant (qui rend toujours le score moyen du propre) doit avoir V = α exactement ; A doit battre cette ligne de base de plus de α (V > 2α) pour qu'on puisse dire qu'il détecte.

### c.2 — I3 (taux de retours) et sa valeur nulle

**Ce qu'il faut démontrer** :

1. La valeur nulle 0,7345 est correcte : **vérification par simulation** rapportée (M4 § 9, 20 000 tirages : 0,7329 ± 0,0012, RAPPORTÉ). Formule analytique : $\bar{I}_3 = \frac{1}{T-2}\sum_{t=3}^{T}\frac{t-2}{t-1}$, valeur exacte 0,73452… à T = 8 (je recalcule : $(1/6)(1/2 + 2/3 + 3/4 + 4/5 + 5/6 + 6/7) = (1/6)(0,5 + 0,667 + 0,75 + 0,8 + 0,833 + 0,857) = (1/6)(4,407) = 0,7345$, VÉRIFIÉ).
2. L'intervalle B2 de I3 − nul exclut zéro. RAPPORTÉ : +0,10 à +0,23 et +0,16 à +0,25. Mais : N = 24, et les intervalles sont par rééchantillonnage des instances, pas analytiques ; la couverture de 95% suppose l'approximation bootstrap, qui peut sous-couvrir à N = 24.
3. **Vérification mécanique** : un bras qui tire ses attaques au hasard dans la boîte (sans optimisation) doit avoir I3 − nul ≈ 0. Si ce n'est pas le cas, la mesure est biaisée.

### c.3 — NashConv (exploitabilité)

**Non implanté dans le code actuel.** Mesure minimale pour l'implanter :

1. Calculer $\max_a \text{taux}(\text{défense mixte de B}, a)$ avec l'attaquant renforcé existant — c'est déjà V(B). RAPPORTÉ.
2. Calculer $\max_m [1 - \text{taux}(m, \text{attaques de B})]$ — nouveau : il faut entraîner un moniteur contre le mélange d'équilibre des attaques de B côté attaquant. Coût : un entraînement supplémentaire par tour.
3. **NashConv = V(B) + (1 − taux du meilleur nouveau moniteur contre le mélange des attaques)**. Si le jeu restreint a valeur v, NashConv ≈ 2×(v − V(B)) pour le jeu restreint ; mais NashConv du jeu continu est plus grand.
4. **Vérification mécanique** : sur un jeu de Matching Pennies (2×2), NashConv doit → 0 en 1/T avec le jeu fictif bilatéral ; avec la meilleure réponse unilatérale, il doit osciller.

### c.4 — OpenSpiel (vérification sur jeu jouet)

**Protocole en cinq lignes** :
1. Installer `open_spiel` ; charger le jeu `matrix_rps` (pierre-feuille-ciseaux, 3×3).
2. Exécuter `fictitious_play` (jeu fictif bilatéral) pendant 100 itérations ; calculer `exploitability.exploitability(game, average_policy)` à chaque itération ; vérifier la décroissance en O(1/T).
3. Exécuter une meilleure réponse unilatérale (joueur 1 = jeu fictif, joueur 2 = meilleure réponse au dernier coup) pendant 100 itérations ; vérifier que l'exploitabilité oscille.
4. Reproduire le diagramme de Shapley (1964) : trois stratégies pures, l'orbite de la meilleure réponse itérée tourne sans converger.
5. Comparer les deux régimes au tracé I3 − nul : la meilleure réponse unilatérale doit avoir I3 − nul > 0 (retours) ; le jeu fictif bilatéral doit avoir I3 − nul → 0.

---

## (d) Ancrage matériel

### Modèles ouverts (pour la question 6 du transfert)

- **Modèle** : Llama 3.1 8B (Meta, poids ouverts, licence communautaire). Les activations internes (résidus de couches) sont accessibles ; des sondes linéaires y sont entraînées comme moniteurs.
- **Bailey et collègues** : arXiv 2412.09565v2, PDF au chemin du dépôt (`9c23a613…`). RAPPORTÉ comme lu par session-depot. Aucun chiffre repris (brouillon 4, R7). L'expérience de ce papier entraîne des sondes linéaires sur les activations d'un modèle de langage pour détecter un comportement caché, puis ré-entraîne la sonde après que le modèle s'est adapté. Le cycle (non-convergence de la sonde ré-entraînée) est le phénomène que le pilote synthétique tente d'analogiser.

### Calcul nécessaire (tout illustratif sauf mention)

| Expérience | CPU estimé | GPU estimé | Coût cloud illustratif |
|---|---|---|---|
| Exp. 1 (attaquant exhaustif) | ~8 h sur 2 cœurs | aucun | ~1 $ (instance c7a.xlarge AWS) |
| Exp. 2 (jeu fictif bilatéral) | ~1,5 h sur 2 cœurs | aucun | ~0,20 $ |
| Exp. 3 (T étendu à 64) | ~6,5 h sur 2 cœurs | aucun | ~0,80 $ |
| Exp. 4 (régularisation, 4 λ) | ~26 min sur 2 cœurs | aucun | ~0,10 $ |
| Exp. 5 (B′ à T = 32) | ~3,2 h sur 2 cœurs | aucun | ~0,40 $ |
| Transfert : sonde linéaire sur Llama 8B | ~2 h sur 1 GPU A100 par itération de la boucle (entraînement sonde + attaquant) | 1× A100 80 GB | ~4 $ / itération ; ~100 $ pour 25 tours |
| Jeu jouet OpenSpiel | < 1 min sur 1 cœur | aucun | négligeable |

**Note sur la décision préenregistrée** : le coût du run de décision (N = 100, 8 bras, 2 δ) est de ~200 min CPU (RAPPORTÉ, brouillon 4, résumé point 9), ~2,5 h de mur sur 2 cœurs à l'efficacité mesurée de 0,52 (RAPPORTÉ, vérification CM4-01). Aucun GPU. Les expériences proposées ci-dessus sont toutes réalisables sur la même infrastructure, sauf le transfert à Llama qui exige un GPU.

---

## Synthèse structurelle

Le cœur de la question est : **pourquoi le bras A cycle-t-il alors qu'il joue déjà le jeu fictif d'un côté ?** La réponse est probablement triple :

1. **L'attaquant ne joue pas le jeu fictif** : il joue la meilleure réponse au *dernier* moniteur, pas au mélange. Le théorème de Brown-Robinson (référence à vérifier : Brown 1951, « Iterative solution of games by fictitious play ») exige que les *deux* joueurs mélangent uniformément. Quand un seul côté le fait, la convergence n'est plus garantie, et le cycle de Shapley (référence à vérifier : Shapley 1964, « Some topics in two-person games ») s'applique.

2. **L'oracle est approché** : même si la structure du jeu fictif unilatéral convergeait en théorie, l'oracle (SLSQP, départs limités) ne rend pas la meilleure réponse exacte. L'erreur d'approximation s'accumule.

3. **La classe linéaire est pauvre** : un moniteur linéaire ne peut « couvrir » qu'une direction de l'espace ; l'attaquant contourne dans la direction orthogonale, puis le nouveau moniteur couvre celle-ci mais perd l'ancienne. C'est le mécanisme géométrique du cycle, formellement analogue à pierre-feuille-ciseaux dans l'espace des directions.

L'expérience 2 (jeu fictif bilatéral) isole le facteur (1) ; l'expérience 1 (attaquant exhaustif) isole le facteur (2) ; l'expérience 3 (T étendu) avec la classe linéaire vs. maxout isole le facteur (3). Chacune a une issue qui falsifie l'une des deux hypothèses posées.

FIN-DE-CELLULE