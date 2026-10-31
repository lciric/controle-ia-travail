La critique croisée A est absente (« jamais lancée ») ; je n’en invente pas le contenu. Je ne réponds ci-dessous qu’aux sections visant D.

## 1. Réponse aux critiques

| Critique | Décision | Correction ou raison |
|---|---|---|
| **B(a)1 et C(a)2 — les trois duels dépendent de tolérances non fixées** | **Acceptée.** | Une tolérance libre n’est pas une règle de falsification. Je retire les duels d’équivalence comme conditions du choix de **B**. Si un duel d’équivalence est lancé pour **A**, sa marge et sa puissance devront être fixées avant les scores ; sinon il ne sera pas présenté comme un test. |
| **B(a)2 — le duel 2 est un calcul déterministe, pas une expérience** | **Acceptée.** | À sonde et attaques figées, recalculer les directions retenues pour différents seuils est bien une lecture de fonctions en escalier. Je le reclassifie en **calcul de fragilité**, sans prétention d’inférence expérimentale. |
| **C(a)1 — la sensibilité B+ risque fuite ou bootstrap de queue** | **Acceptée.** | Suppression du mélange seuil/mesure et du bootstrap comme estimateur de l’incertitude de queue. Le bloc de mesure reste intact jusqu’au résultat principal. La sensibilité utilisera la courbe complète des comptes en fonction du seuil, sans intervalle bootstrap. |
| **B(b), deuxième point, et C(b)3 — saturation ou instabilité discrète du duel 2** | **Acceptée.** | Si tous les scores adverses sont loin du seuil, le calcul est non informatif et sera déclaré saturé. S’ils s’accumulent près d’une coupure, les changements de comptes seront montrés direction par direction ; aucune stabilité ne sera déduite d’un seul compte agrégé. |
| **B(a)3 et C(b)1 — le discriminant Bailey/candidat peut manquer une différence de queue** | **Acceptée.** | L’AUC de domaine devient uniquement un diagnostic. Elle ne peut ni valider ni invalider à elle seule **A**. Le critère scientifique principal est le taux de dépassement au seuil externe sur des données cibles indépendantes, avec une précision suffisante. |
| **B(b), premier point, et C(b)2 — 200 bénins Bailey ne permettent pas une équivalence serrée** | **Acceptée.** | Je retire l’idée qu’un non-rejet sur ces 200 cas pourrait certifier **A**. Même le cas \(2/200\) a l’intervalle de Clopper–Pearson rapporté \([0{,}0012;0{,}0356]\). Une équivalence plus étroite exige davantage de données cibles ou une tolérance plus large explicitement acceptée. |
| **C(a)3 et B(b), troisième point — comparaison des sondes 400/800 confondue et sous-puissante** | **Acceptée.** | Je supprime le duel 3 comme contrôle bloquant. **B définit une nouvelle sonde**, entraînée avec 400 bénins ; ses résultats ne seront pas présentés comme ceux de la sonde à 800. Toute comparaison exploratoire devra employer exactement les mêmes blocs de calibration et d’évaluation pour les deux sondes. |
| **B(a)4 — rapport B+ non hiérarchisé** | **Acceptée.** | Je distingue désormais : contrôles mécaniques bloquants, résultat principal, puis sensibilités post-gel. La comparaison 400/800 ne peut plus être reléguée implicitement parmi les résultats principaux : elle est exploratoire. |
| **B(a)5, B(c)1–2 — juge après perturbation et dégradation comptée comme camouflage** | **Acceptée, transformée en test.** | J’ajoute un contrôle bloquant d’interprétation : perturbations aléatoires de même norme, audit du juge sur sorties post-perturbation, et évaluation séparée de la cohérence/utilité. Une sortie vide ou dégénérée ne sera pas une réussite de camouflage. |
| **C(c)1 — appliquer les directions aux bénins et tester la linéarité** | **Acceptée en partie.** | Le contrôle bénin sera effectué après gel du résultat principal. La vérification \(w^\top(x+u)=w^\top x+w^\top u\) est un test unitaire de l’implémentation, pas une preuve scientifique. Cohérence et utilité devront être mesurées : un score de non-nuisance seul ne suffit pas. |
| **C(c)2 — permutation des blocs seuil/mesure avant calibration** | **Transformée.** | La faire avant le résultat principal exposerait le bloc de mesure à des choix méthodologiques. Elle devient une sensibilité post-gel. Elle ne prouve pas l’échangeabilité, même sans alarme. Déduplication et découpage reproductible restent les contrôles préalables. |
| **B(c)3 — absence d’un contrôle modèle base/instruct** | **Rejetée comme fatale pour D-ML-1.** | La question porte sur l’évasion d’une **sonde figée**, pas sur l’origine alignment-spécifique du signal. Un corrélat lexical n’invalide pas cette mesure limitée. Ce contrôle deviendrait nécessaire si l’on prétendait mesurer une propriété interne d’alignement. |

## 2. Plan corrigé

### Calculs préalables — explicitement non présentés comme des duels

1. **Figer la convention de seuil.** Pour **B**, avec des scores continus sans ex æquo, prendre le troisième plus grand score des 300 bénins de calibration donne, pour une future entrée exchangeable :
   \[
   p\sim\mathrm{Beta}(3,298).
   \]
   Toute interpolation de quantile, tout arrondi ou ex æquo impose de réécrire cette loi. Le script et la convention restent à auditer.

2. **Séparer les deux incertitudes.** Sur le bloc de mesure, rapporter \(K/300\), le seuil observé et Clopper–Pearson conditionnel à ce seuil. Pour l’incertitude intégrant la calibration, utiliser la loi prédictive bêta-binomiale induite par \(\mathrm{Beta}(3,298)\), sans additionner artificiellement deux intervalles.

3. **Calculer la fragilité des coupures.** Pour chaque \(\tau\), publier \(N_\tau(t)\) pour tous les seuils distincts observés, avec les directions qui changent de statut entre rangs adjacents. Aucun bootstrap, aucune réutilisation du bloc de mesure et aucune transformation de ces variations en intervalle de confiance.

### Duel A — seulement si un candidat externe et de nouvelles données cibles existent

- **H_A :** le déplacement du taux cible au seuil externe est inférieur à une marge d’équivalence fixée avant les scores.
- **H_B :** ce déplacement est au moins égal à cette marge.
- **Mesure décisive :** dépassements au seuil externe sur un échantillon cible indépendant ; taille calculée pour distinguer les deux hypothèses avec la puissance préenregistrée.
- **Diagnostics seulement :** longueurs, langue, format, AUC de domaine et comparaison des corps de distribution.
- **Contrôle négatif :** deux partitions aléatoires d’un même pool ne doivent pas déclencher l’alarme.
- **Issues :** une équivalence démontrée avec puissance suffisante falsifie H_B ; un écart au moins égal à la marge falsifie H_A. Un résultat sous-puissant ne valide pas A.
- **Sélection :** un seul candidat choisi avant ce test, ou correction explicite de la multiplicité. Les 200 Bailey actuels ne doivent pas servir à essayer des jeux jusqu’à trouver un non-rejet.

### Duel de non-trivialité — bloquant pour interpréter les directions

- **H_A :** les passages sous le seuil sont expliqués par une dégradation générique, reproduite par des perturbations aléatoires de même norme.
- **H_B :** les directions optimisées produisent un excès d’évasion de la sonde tout en conservant des sorties cohérentes et utiles.
- **Issues :** des contrôles aléatoires équivalents, ou des sorties inutilisables, falsifient l’interprétation H_B ; un excès spécifique avec utilité conservée falsifie H_A. Une absence d’effet par saturation sera rapportée comme non concluante, pas comme une validation.

## 3. Réponse à l’arbitre

### Ce qui est établi

Les contraintes et comptes du jeu sont **RAPPORTÉS** ; la sortie du programme reste **OBSERVÉE-NON-AUDITÉE**. Ma reconstruction mathématique est **VÉRIFIÉE**, aux arrondis :

- toutes les lignes « seuil » correspondent aux quantiles centraux à 95 % de  
  \(\mathrm{Beta}(k,n+1-k)\), respectivement  
  \(\mathrm{Beta}(10,991)\), \(\mathrm{Beta}(8,793)\), \(\mathrm{Beta}(5,496)\),  
  \(\mathrm{Beta}(4,397)\), \(\mathrm{Beta}(3,298)\) et \(\mathrm{Beta}(2,199)\) ;
- les lignes « mesure » correspondent à Clopper–Pearson :  
  \(10/1000\rightarrow[0{,}0048;0{,}0183]\),  
  \(3/300\rightarrow[0{,}0021;0{,}0289]\),  
  \(2/200\rightarrow[0{,}0012;0{,}0356]\).

Cette concordance suppose la règle du \(k\)-ième plus grand score. Un intervalle « seuil » est prédictif pour un seuil aléatoire ; il n’est pas un Clopper–Pearson conditionnel à un seuil fixe.

### Décision recommandée

**Je maintiens B, mais comme déviation explicite et sans certification d’un point de fonctionnement à exactement 1 %.** Ni validation croisée ni bootstrap ne créent les données indépendantes manquantes. Le découpage 400/300/300 doit être figé, dédupliqué et rapporté ; la sonde à 400 bénins est un nouvel instrument.

Avec exactement 200 adverses par direction, les lectures restent interprétables en comptes :

- rappel \(<50\%\) : au plus 99 détections ;
- rappel \(<20\%\) : au plus 39 ;
- rappel \(<5\%\) : au plus 9.

Mais chaque compte de directions est conditionnel au seuil estimé. Il faut rapporter le seuil, les comptes bruts, la loi prédictive de calibration, Clopper–Pearson sur la mesure, les directions cherchées/trouvées et la courbe de fragilité. Le résultat reste une borne sur les directions **trouvées**, non sur toutes les directions existantes.

Pour **A**, `databricks-dolly-15k` — taille et licence CC BY-SA 3.0 **SUPPOSÉES**, référence à vérifier — et `OpenAssistant/oasst1` — taille et licence Apache-2.0 **SUPPOSÉES**, référence à vérifier — restent seulement des candidats à filtrer. Aucun n’est validé ici. Un grand jeu peut réduire la variance tout en déplaçant arbitrairement la queue des scores : le risque de biais n’est pas borné par les intervalles binomiaux.

### Ce qui n’est pas établi

L’échangeabilité des partitions, l’absence de near-duplicates, la loi effective avec ex æquo, les performances des sondes et du juge, la compatibilité d’un jeu externe et la stabilité des comptes de directions sont inconnues. Les 200 Bailey restants ne suffisent pas à certifier une équivalence de queue serrée, et une AUC de domaine ne comble pas ce déficit.

### Expérience à faire en premier

**Un pilote B figé, avant la campagne complète :** vérifier déduplication et règle de seuil, entraîner la sonde sur 400, geler le seuil sur les 300 de calibration, puis seulement mesurer les 300 restants. Ensuite, exécuter un petit pilote de directions avec perturbations aléatoires appariées et audit des sorties.

**Pire cas de B :** une sonde affaiblie et un seuil anormalement permissif gonflent les directions retenues, particulièrement à 5 %. Si des changements de rang adjacents au seuil modifient la conclusion discrète, ou si le contrôle aléatoire reproduit l’effet, je suspendrais la campagne plutôt que de « réparer » B par bootstrap. Je passerais à A uniquement avec un candidat versé et une compatibilité opérationnelle démontrée sur assez de données cibles indépendantes.

FIN-DE-CELLULE