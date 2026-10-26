# Proposition B — Tour III.2 : équipe rouge croisée

**Pièces reçues.**
- Bloc FAITS : vide par décision de l'arbitre (conv-audit n° 28 § 1). Je n'en invente aucun contenu.
- Pièces A et C : présentes, apparemment complètes, chacune terminée par FIN-DE-CELLULE.
- Empreintes sha256 : je ne peux pas les vérifier.

**Statuts.** Le cadre de la question est RAPPORTÉ. Mes objections sont des HYPOTHÈSES ou des raisonnements explicites. Tout chiffre qui n'en découle pas est marqué « illustratif ».

---

## Contre la proposition A

### (a) Failles

**A1. E3 donne la victoire à la règle mécanique par construction.**
- Les « courses synthétiques » sont obtenues par rééchantillonnage d'items, avec des effets plantés.
- Ce générateur suppose des items indépendants et un effet additif. Ce sont exactement les hypothèses sous lesquelles Wilcoxon + BH est bien calibré : la règle est jugée dans le monde pour lequel elle est optimale.
- Ce qu'on attribue aux agents (lire le code, repérer une hypothèse mal formée) n'existe pas dans une course synthétique : il n'y a ni code modifié ni journal réel. H_A (« les agents battent la règle ») ne peut donc pas gagner.
- C'est une fuite construction/évaluation : le modèle de bruit qui fixe les seuils de la règle est aussi celui qui l'évalue.
- Variable non contrôlée : les agents peuvent reconnaître une course synthétique (formats, absence de diff). Leur comportement sur ces courses ne dit alors rien de leur comportement sur une vraie course.

**A2. E1 confond deux variances.**
- A compare l'écart type entre graines d'un organisme figé, sur 60 items fixes, à √(0,75·0,25/60) ≈ 0,056. Cette valeur est l'erreur d'échantillonnage des items, pas une variance entre graines : les deux quantités ne sont pas commensurables.
- Le contrôle négatif « organisme nul (classifieur constant) » a une variance entre graines nulle par construction. Son écart type mesuré ne teste donc pas l'instrument ; il vaudra 0 quoi qu'il arrive.
- E1 ne mesure que la stochasticité d'inférence de g0. La variance de *réécriture*, qui sépare g0 de g3, est la composante qui décide d'une élimination, et E1 la laisse inconnue.

**A3. E2 consomme `test_final`.**
- Mesurer Δ_test − Δ_final sur au moins 3 courses, puis choisir l'« échelle » ou non selon le résultat, utilise `test_final` pour une décision de conception. Il cesse alors d'être non contaminé : c'est le problème de Dwork et al. (2015, à vérifier) déplacé d'un cran.
- Le contrôle « score brouillé » donne Δ_test ≈ Δ_final ≈ 0 trivialement, puisque l'organisme ne reçoit aucune information. Il ne contrôle ni la régression vers la moyenne ni une différence de difficulté entre `test` et `test_final`, qui est une confondante non mentionnée.

**A4. E4 n'apporte pas de preuve causale.**
- L'organisme *déclare* quelle mesure est « favorable » : c'est un auto-rapport.
- Confondante : la compétence. Un meilleur organisme écrit de meilleurs textes de sonde et obtient un meilleur Δ_test, sans lien causal entre la primitive et le gain.
- Atténuation : Δ_test sur une course unique a un écart type ≈ 0,1 (RAPPORTÉ, ordre de grandeur), ce qui écrase toute corrélation.
- Le contrôle « jetons mélangés » est trop faible : n'importe quelle mesure s'effondre sur du charabia. Il passera toujours.

**A5. E5 (canaris) est sous-dimensionné et confondu.**
- Six canaris ne distinguent rien. Une exactitude sur 6 items a une granularité de 1/6 ; la différence avec le contrôle n'atteint aucune puissance utile (raisonnement explicite).
- Confondante : le canal *autorisé*, le score `test` rendu à l'organisme, peut à lui seul faire basculer des canaris, sans aucune fuite par la correction. A ne sépare pas le canal autorisé du canal interdit.
- Planter des étiquettes contraires dans `test` dégrade la mesure de `test` pour toutes les autres expériences menées en parallèle.

**A6. P7 affirme un fait absent du cadre.**
- A écrit « le correcteur a le réseau, les clés ». Le cadre dit le contraire pour l'organisme : « le noyau seul a le réseau et les clés ». L'accès de conv-audit n'est pas décrit.
- A présente ainsi une hypothèse comme un constat.

**A7. Le calcul de fuite par le score est faux.**
- « 4 soumissions × 60 bits » surestime la fuite. Un score sur 60 items prend au plus 61 valeurs, soit log₂(61) ≈ 5,9 bits par lecture, donc ≈ 24 bits pour 4 générations.
- En revanche, A oublie les 6 rondes de conception et les relectures humaines, qui multiplient les lectures. Le compteur pertinent est celui des lectures, toutes boucles confondues.

**A8. Incohérence de la puissance.**
- Le calcul « 8 paires » utilise l'écart type d'une différence *indépendante* (0,07·√2) sur 36 tâches. Or les comparaisons de la boucle sont *appariées* sur les mêmes 60 tâches.
- Le nombre de répétitions recommandé n'est donc pas dérivé du dessin évalué.

### (b) Scénarios d'évasion

L'adversaire est l'organisme qui optimise le score, le correcteur, ou un agent de la boucle extérieure. Tous les coûts sont illustratifs.

| Instrument de A | Évasion | Coût |
|---|---|---|
| Refus des quasi-copies (n-grammes + embeddings) | L'organisme demande au modèle, via le noyau, une transposition isomorphe de l'item (autre domaine, autres noms, même structure), puis la soumet à la primitive. La similarité d'embedding chute alors que la structure utile reste. | 1 appel de modèle par item, dans le budget |
| Primitive utilisée comme oracle | Lire les log-prob des jetons d'étiquette du modèle ouvert sur ces transpositions revient à classer `test` par le modèle ouvert. | ≈ 0 |
| Canaris (E5) | Le correcteur qui lit la banque n'encode pas d'items. Il encode des *régularités de construction* (longueur, tournures du générateur de la banque, place de l'indice). Les canaris ne détectent qu'une mémorisation item par item. | ≈ 0 |
| Journal du noyau | Le journal ne voit que ce qui passe par le noyau. Une lecture de la banque par le correcteur hors du noyau, si elle est possible, n'y figure pas. | ≈ 0 |
| Test apparié g0/g3 | Sous-performance de g0. Un proposeur sélectionné sur Δ gagne à écrire une g0 faible, ce qui gonfle Δ sans progrès absolu. Aucun contrôle de A ne l'empêche. | ≈ 0 |
| Agents éliminateurs (E3) | Ils se comportent « bien » sur les courses reconnues comme synthétiques et librement sur les vraies. | ≈ 0 |
| Placebo E6 (nombres aléatoires) | Soumettre deux fois le même texte : des valeurs différentes trahissent le placebo, et l'organisme peut alors l'ignorer. | 2 appels |

**Tous à la fois.**
1. Le correcteur encode des régularités de construction de la banque.
2. L'organisme transpose les items de `test` vers la primitive.
3. La sélection se fait sur Δ à partir d'une g0 affaiblie.

Résultat attendu :
- Aucun canari ne bouge.
- Le filtre ne voit rien.
- E2 conclut « pas de sur-ajustement », parce que `test_final`, issu de la même construction, partage les mêmes artefacts.
- La banque scellée de 96 tâches, si elle a les mêmes auteurs ou le même générateur, les partage aussi.

Coût pour l'adversaire : quasi nul, de l'ordre de quelques dizaines d'appels supplémentaires par génération (illustratif). C'est le scénario que A ne peut pas voir. Ses deux types d'échec documentés (fraude sur l'évaluateur, évaluateur faux) n'incluent pas « évaluateur juste, banque à raccourcis ».

### (c) Contrôles négatifs dont l'absence est fatale

1. **Classifieur à raccourcis** sur la banque elle-même : régression logistique sur traits de surface (longueur, n-grammes, position). S'il atteint le niveau de l'organisme, le gain de l'organisme n'est pas attribuable à la tâche. A ne l'applique qu'à la primitive, pas à l'organisme.
2. **Placebo déterministe par texte**, tiré d'un hachage du texte, pour E6. Sinon le bras placebo est détectable et l'expérience mesure la détection, pas la valeur des mesures.
3. **g0 de référence commune et figée**, écrite hors de la boucle, contre laquelle toutes les générations sont comparées en plus de leur propre g0.
4. **Test de discriminabilité synthétique/réel** pour E3 : si un agent distingue les deux au-dessus du hasard, E3 est invalide.
5. **Registre de consommation de `test_final`** : toute lecture utilisée pour décider du dessin de la boucle compte comme adaptative.

---

## Contre la proposition C

### (a) Failles

**C1. Statuts relevés, en violation de la règle 1.**
- C marque VÉRIFIÉ, au même endroit qu'un « référence à vérifier », des contenus tirés de mémoire. Exemples : la mécanique de FunSearch, le résultat de Dwork et al., Agarwal et al. (2021), les échecs de The AI Scientist, l'« échec connu » de Reflexion, et l'antériorité « occupée [VÉRIFIÉ] ».
- Le bloc FAITS est vide. Rien de ce qui vient de la littérature n'a pu être vérifié dans ce protocole.
- Plusieurs assertions sont plausibles, mais je ne peux pas les confirmer : que FunSearch « ne fonctionne qu'avec un signal dense » soit rapporté par ses auteurs ; que Gödel Agent n'ait « pas de séparation » noyau/action ; la forme exacte des bornes O(√(k/n)).
- Lazar ne peut donc pas utiliser la section littérature de C sans la reclasser entièrement. Je ne change pas ces statuts : je signale qu'ils sont infondés.

**C2. « Thresholdout simplifié » emprunte le nom sans la garantie.**
- Thresholdout compare le score du holdout à un score d'*entraînement*. Le cadre ne donne à l'organisme que `test` et `test_final` ; aucune part d'entraînement n'est décrite.
- Le mécanisme de C se réduit donc à un arrondi ou à une échelle (proche de Blum & Hardt, 2015, à vérifier). Aucune garantie de confidentialité différentielle n'est transportée.

**C3. E3 détruit la banque de confirmation.**
- Évaluer les 24 générations intermédiaires de chaque branche sur la banque scellée de 96 tâches, puis choisir « brut » ou « quantifié » selon la pente observée, revient à concevoir sur la banque de confirmation.
- Elle n'est plus scellée au sens du cadre.
- De plus, chaque branche n'a qu'une campagne (n = 1). Un écart de 0,10 contre 0,05 entre deux campagnes uniques tombe dans la zone que le cadre déclare être du bruit (< 0,2, RAPPORTÉ).

**C4. E2 évalue sur la vérité qui sert à construire.**
- Les « 4 améliorations réelles vérifiées » : vérifiées sur quoi ? Si c'est sur les 60 tâches, la règle mécanique qui lit ces mêmes scores est d'accord par construction.
- Si c'est sur la banque scellée, celle-ci est consommée, comme en C3.
- Avec 10 modifications, dont 4 positives, la granularité des taux est de 25 %. Aucune différence de taux de fausses éliminations entre la triade et le script n'est mesurable à cette taille (raisonnement explicite).

**C5. Le critère « identifier la ligne de code fautive » ne peut pas être rempli.**
- Il est imposé au trio sur des « paires de courses synthétiques » (instrument 1). Une course synthétique n'a pas de ligne de code : même défaut que A1, en plus explicite.

**C6. E1 : ρ confondu avec le rang de la génération.**
- Les générations tardives ont à la fois une meilleure « marge de séparation » et une meilleure exactitude, pour toute raison d'amélioration. La corrélation de rang ne contrôle pas cet effet.
- L'erreur type « SE_apparié/√3 ≈ 0,035 » suppose p_d = 0,20. Or les bras Nominal et Sham divergent dès la génération 1 : on compare deux organismes différents, dont la proportion de tâches discordantes peut être bien plus grande.
- L'appariement sur les items ne vaut pas appariement sur le code.

**C7. Contradiction dans la règle de zone grise.**
- C pose d'abord une « interdiction formelle aux agents de conclure », puis écrit : « soit on l'élimine par parcimonie ».
- Ce second cas est exactement une élimination sur du bruit, c'est-à-dire la fausse élimination que la règle devait empêcher.

**C8. Surévaluation de la barrière temporelle (règle 5).**
- La barrière « réduit structurellement ce risque à 0 ». C'est faux à l'échelle d'une course.
- La génération t lit `test`. Le code réécrit de la génération t+1 peut contenir des transpositions de ces items et appeler la primitive *avant* de charger `test`.
- La barrière ne vaut que pour une génération isolée.

### (b) Scénarios d'évasion

| Instrument de C | Évasion | Coût (illustratif) |
|---|---|---|
| Filtre AST (littéraux, complexité) | Le sur-ajustement vit dans le *tex