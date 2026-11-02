# Tour III.3 — réponse de la proposition D

Les documents et leurs chiffres conservent les statuts de ma conception III.1 : **RAPPORTÉ** ou **OBSERVÉ-NON-AUDITÉ**. Mes corrections sont des **HYPOTHÈSES méthodologiques** ; aucun résultat empirique n’est **VÉRIFIÉ** par moi. Je n’introduis aucun seuil chiffré nouveau : marges et effectifs devront être gelés après calcul de puissance, avant lecture.

## (a) Réponse aux critiques visant D

### E1 — Pont et différées

- **Duel tranché avant exécution (A, B, C, E) : acceptée.** « Toutes les fiches sont immédiatement testables » est déjà contredit par l’état **RAPPORTÉ** de l’infrastructure. Je supprime ce duel. E1 mesurera désormais la **fidélité et la couverture du pont**, y compris sur des fiches non immédiatement exécutables. L’absence d’épreuve fraîche sera comptée comme limitation d’infrastructure, non comme défaut de traduction.
- **Existence populationnelle et classes rares (E) : acceptée.** Aucun échantillon ne réfutera l’existence d’une classe rare de différées. Les proportions d’indisponibilité seront estimées descriptivement ; des classes rares injectées, à vérité connue, serviront séparément à éprouver l’instrument.
- **Généralisation course 1 → course 2 (B) : acceptée.** Le format de course 1 étant **RAPPORTÉ/SUPPOSÉ**, son pilote ne vaudra pas validation pour la course 2. Une réplication sur le format réel de course 2 sera obligatoire avant usage sélectif.
- **Petit effectif (A, B) : acceptée.** Le pilote initial est une reconnaissance de défauts et un moyen d’estimer la variance, pas une certification des proportions de sorties ni d’un taux faible d’erreur.

### E2 — Réutilisation des épreuves

- **Appariement et banque fraîche (A) : acceptée sur le fond, mais pas sur l’impossibilité absolue.** On ne peut pas apparier les sorties d’API non déterministes. On peut en revanche randomiser des **populations indépendantes**, geler les lois initiales et comparer des politiques au niveau campagne. Tant qu’aucune banque réelle fraîche n’existe, la partie réelle est retirée du protocole plutôt que simulée verbalement.
- **Monde planté et banque réelle (B) : acceptée pour le non-regroupement ; rejetée seulement pour l’assimilation « planté = tautologique ».** Un monde planté non tautologique peut tester une calibration. Les mondes plantés et la future banque réelle auront des verdicts séparés, jamais une moyenne où le premier dominerait.
- **Clause de sauvetage par une preuve générale (C) : acceptée.** Je la retire. Un résultat empirique tranchera pour le domaine effectivement testé, sans prétendre établir une théorème universel ni être rattrapé par son absence.
- **Événement d’erreur et insuffisance du renouvellement (B, E) : acceptée.** Je distingue : erreur de campagne sous nullité globale, FDR cumulé sous mélange de nuls et d’alternatives, puissance conditionnelle à la testabilité, et rendement. Une épreuve fraîche n’est pas présumée valide : elle est elle-même évaluée.
- **Canal mémoire (B) et mondes nuls insuffisants (E) : transformés en test.** Le plan devient factoriel : épreuve réutilisée ou renouvelée, sélection adaptative présente ou absente, mémoire textuelle présente ou absente. Il comprendra nullité globale et mélange d’alternatives, avec campagnes non adaptatives de référence.
- **Dimensionnement (A, B, C) : acceptée.** La certification d’une borne très faible exige une simulation massive ; une petite série de campagnes ne pourra conclure ni à la sécurité ni à l’équivalence.

### E3 — Héritage

- **Canonisation servant à la fois d’instrument et de métrique (A) : acceptée.** Je reprends explicitement le **canoniseur tiers, gelé et indépendant des bras** demandé par A. Les paires « même loi, lexique disjoint » et « lexique commun, lois distinctes » testeront ce canoniseur avant toute comparaison.
- **Absence de marge, d’estimateur et d’unité de réplication (B, C, E) : acceptée.** Le paramètre sera une différence de familles nouvelles confirmées par population indépendante, à nombre de propositions et de tests fixé. Une marge d’utilité et une règle d’incertitude seront gelées.
- **Longueur, contenu et amorçage lexical (C, E) : acceptée.** Les bras comprendront codes minimaux, motifs complets, texte neutre cohérent de même longueur et domaine, et motifs permutés. Le bras permuté ne sera pas le seul contrôle, car une permutation peut produire un texte incohérent.
- **Densité lexicale (B) : acceptée.** Les erreurs de mémoire seront stratifiées selon la proximité lexicale et l’équivalence prédictive, plutôt que résumées par un taux global de redites.

### E4 — Diversité

- **Métriques circulaires (C, E) : acceptée.** Part maximale d’une lignée et couverture des descripteurs deviennent des diagnostics mécaniques, jamais le critère principal de succès. Le résultat principal sera compté sur une partition indépendante de la garde.
- **Petites populations et instabilité du maximum (A, C) : acceptée.** La distribution de concentration sera calculée sous reproduction neutre avec le même graphe de parenté ; les unités de réplication seront les populations, pas les filles apparentées.
- **Descripteurs permutés (C, E) : acceptée.** Ce contrôle vérifiera si la taxonomie apporte autre chose qu’une perturbation de l’allocation.
- **Saturation des familles (C) : acceptée.** Aucune partition fermée à petit nombre de cellules ne servira de dénominateur principal ; les fusions et scissions erronées du canoniseur seront mesurées séparément.

### E5 — Ablation et audit final

- **Bras sans pôle non spécifié et multiplicité asymétrique (A) : acceptée.** J’ajoute des parents aléatoires parmi les admissibles et je sépare deux comparaisons : mécanisme à effectifs fixés, politiques complètes à budget égal. La multiplicité de l’audit final sera contrôlée **par bras**, avec son propre nombre de lois jugées.
- **Structure de l’audit final (B) : acceptée.** Un audit identique au pôle favoriserait les fiches qu’il a préparées ; un audit différent change la question. Je choisis donc, à l’avance, un **audit confirmatoire principal sur données fraîches, avec procédure statistique et plan d’expérience indépendants de la sélection**, et je n’utilise le juge du pôle qu’en analyse de robustesse.
- **Gel avant confirmation (E) : acceptée.** Objets, critères, allocations, effectifs et règles d’arrêt seront scellés avant lecture de l’audit. Des témoins plantés et un monde entièrement faux éprouveront cet audit lui-même.
- **Répétitions et persistance (B, E) : acceptée.** Les répétitions seront des populations sans mémoire partagée ; une seule descendance ne documentera qu’un effet immédiat, pas un héritage persistant.
- **Erreur composée canonisation–nouveauté–confirmation (B, C) : acceptée.** Chaque composante sera calibrée séparément ; le taux composite ne sera pas présenté comme plus précis que ses maillons.

### Points transversaux

- **Dérive vers la testabilité (A) : transformée en test.** E1 et E5 compteront les lignées perdues selon le code de différé, l’axe et le proposeur, puis leur récupération lorsque l’infrastructure devient disponible. Cette dérive ne sera ni appelée réfutation ni confondue avec un gain scientifique.
- **Porte R13 trop qualitative (B) : transformée en banc à vérité connue.** Il comprendra paraphrases et reparamétrisations des hypothèses du programme, nouveautés réellement distinctes, et nouveautés triviales ou hors programme. On mesurera justesse et fausses admissions, pas seulement accord entre lecteurs.
- **Absence générale de dimensionnement (A) : acceptée.** La prudence verbale ne remplace pas une puissance calculée.

## (b) Expériences corrigées

**Règle commune.** Pour un paramètre scalaire, je pose \(H_A:\theta>\delta\) contre \(H_B:\theta\leq\delta\), avec \(\delta\) gelé. Une borne inférieure au-dessus de \(\delta\) falsifie \(H_B\) ; une borne supérieure au-dessous falsifie \(H_A\). Sinon, l’essai est **indécis** : aucune politique n’est adoptée et il faut redimensionner. Pour les hypothèses composites, toutes les conditions doivent être certifiées pour établir \(H_A\), tandis qu’une violation certifiée suffit à la falsifier. La non-significativité ne vaut jamais équivalence.

### E1 — Le pont est-il utile et fidèle, indépendamment de l’exécution immédiate ?

- **\(H_A\)** : parmi les fiches éligibles selon une référence indépendante, le pont atteint la fidélité minimale gelée **et** produit un gain de couverture fidèle supérieur à \(\delta\) sur l’extracteur mécanique.
- **\(H_B\)** : au moins une de ces deux conditions échoue.

**Protocole.** Références produites sans les traducteurs ; fiches déjà sous forme de loi, aller-retour, fiches à deux nombres, altérations non numériques, classes rares injectées et fiches réelles. Sorties séparées : défaut de traduction, manque d’épreuve, puissance insuffisante. Couverture imposée dans le critère afin qu’un rejet systématique ne donne pas une fidélité artificiellement parfaite. Réplication indépendante sur course 2.

**Issues.** Certification des deux conditions : \(H_B\) est falsifiée, le pont peut passer à E2/E5, sans promotion scientifique automatique. Fidélité insuffisante ou gain non supérieur certifié : \(H_A\) est falsifiée et son usage sélectif est bloqué.

### E2 — La réutilisation adaptative est-elle valide sur un domaine gelé ?

- **\(H_A\)** : la politique réutilisée respecte les bornes absolues d’erreur gelées et n’ajoute pas plus de \(\delta\) d’erreur que la politique renouvelée.
- **\(H_B\)** : elle viole au moins une condition.

**Protocole.** Simulation factorielle épreuve × sélection × mémoire, mêmes lois et tirages initiaux, nullité globale puis mélange d’alternatives. Estimation par campagne : toute fausse promotion sous nullité, FDR cumulé, puissance conditionnelle, extinctions. La banque réelle fraîche fera plus tard l’objet d’une confirmation distincte.

**Issues.** Toutes les bornes certifiées : \(H_B\) est falsifiée **sur ce banc seulement**. Une inflation certifiée : \(H_A\) est falsifiée et la réutilisation est exclue des usages décisifs. Aucune réserve par « preuve générale à venir ».

### E3 — Les motifs complets d’élimination améliorent-ils le rendement ?

- **\(H_A\)** : à propositions et tests fixés, les motifs complets produisent au moins \(\delta\) familles nouvelles confirmées de plus par population que le meilleur contrôle minimal ou neutre.
- **\(H_B\)** : le gain est au plus \(\delta\).

Canonisation tierce, audit terminal commun, coûts et longueurs consignés. Un gain certifié falsifie \(H_B\) ; un gain certifié inférieur ou égal à la marge falsifie \(H_A\) et impose la transmission minimale. Les motifs permutés servent à localiser l’amorçage lexical, non à déclarer une causalité à eux seuls.

### E4 — La garde de diversité apporte-t-elle plus qu’un plafond simple ?

- **\(H_A\)** : elle augmente les familles indépendamment confirmées de plus de \(\delta\), sans dépasser la perte admissible de vraies filles.
- **\(H_B\)** : gain insuffisant ou perte excessive.

Comparaison sans garde, plafond simple, garde proposée ; mondes fécond et plat analysés séparément ; descripteurs permutés et partition tierce. Gain et perte acceptables certifiés : \(H_B\) falsifiée. Gain insuffisant ou perte excessive certifiée : \(H_A\) falsifiée.

### E5 — Le filtre du pôle améliore-t-il descendants et politique complète ?

- **Mécanisme** : mêmes parents admissibles disponibles, effectifs de parents, filles et tests fixés ; bras pôle, juges-modèles et tirage aléatoire. Cela isole la sélection, sans confondre traduisibilité et volume.
- **Politique** : mêmes budgets, toutes dépenses incluses, y compris banques, échecs et campagnes sans sortie ; chaque bras conserve sa propre correction de multiplicité.

Pour chacun, \(H_A\) affirme un gain supérieur à \(\delta\) de familles nouvelles confirmées sur le meilleur contrôle ; \(H_B\) affirme le contraire. L’audit final commun contient témoins vrais/faux et un régime entièrement nul. Les coûts sont rapportés séparément du mécanisme. Seules des campagnes sur plusieurs générations pourront prétendre à la persistance.

## (c) Réponse à l’arbitre

### Ce qui est établi

Au sens documentaire seulement, il est **RAPPORTÉ** que la conjonction universelle n’est pas actuellement opérationnelle : tests de mort jamais activés, épreuve T0.5 déjà lue, épisodes frais insuffisants. Il est **OBSERVÉ-NON-AUDITÉ** que la plomberie du pôle a fonctionné dans un monde tautologique et que la banque réelle servie a révélé un défaut de puissance. Les simulations **RAPPORTÉES** vérifient certains mécanismes dans leurs mondes, non une découverte sur le monde réel.

La distinction **éliminée / promue / différée** reste donc ma règle administrative proposée : seules les promues se reproduisent ; une différée n’est ni fausse ni porteuse d’une preuve héritée. Ce n’est pas un résultat expérimental.

### Ce qui n’est pas établi

Ne sont établis ni la fidélité sémantique du pont, ni la calibration des tests de mort, ni la puissance du pôle sur épreuve réelle fraîche, ni le contrôle cumulé de l’erreur sous adaptation, ni l’utilité de l’héritage, de la recombinaison ou de la garde de diversité. Le coût par famille nouvelle confirmée est inconnu. La nouveauté méthodologique face à la littérature reste également non revendiquée : **références à vérifier**.

### Expérience à faire en premier

**E1 corrigée**, avant toute sélection générationnelle. Le petit pilote **RAPPORTÉ** de fiches réelles et témoins sert de reconnaissance, puis l’échantillon annoté indépendant est dimensionné pour trancher fidélité et couverture contre l’extracteur mécanique. Il ne requiert ni carte graphique ni épreuve fraîche : une loi fidèle peut être différée pour infrastructure.

Si E1 échoue, on corrige le pont et on ne l’utilise pas pour tuer des idées. S’il réussit, on enchaîne avec la simulation E2 et l’ablation E5, en maintenant confirmation finale indépendante, comptabilité intégrale des coûts et sortie R13 seulement après nouveauté documentée, porte nommée, coût borné et GO de Lazar.

FIN-DE-CELLULE