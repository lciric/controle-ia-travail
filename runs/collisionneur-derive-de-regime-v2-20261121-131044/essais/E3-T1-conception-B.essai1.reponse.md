# Proposition B : corriger un seuil à 1 % de fausses alertes qui ne tient plus quand le régime change

Les éléments du livrable sont répartis dans l'ordre imposé par l'arbitre :
- (a) les présupposés, en §1 ;
- (c) les mesures minimales par instrument, en §3 ;
- (b) les duels H_A / H_B, en §6.6 ;
- (d) l'ancrage matériel, en §6.7.

Les références sont données sans identifiant arXiv, conformément à la règle 3, même si la question en demande. Les seuls identifiants cités sont ceux des faits.

Les calculs qui sont de moi portent la mention « HYPOTHÈSE (calcul B, non audité) ». Ils dépendent d'un n illustratif et doivent être recalculés par un tiers.

---

## 1. Ce qu'un expert ferait ici, et qu'on ne demande pas

**1.1 Fixer la cible avant le seuil.** « 1 % » recouvre au moins quatre garanties qui ne sont pas équivalentes :
- **marginale** : en moyenne sur les tirages de l'échantillon d'étalonnage. C'est la seule que donne le conformal découpé.
- **conditionnelle à l'étalonnage** (PAC) : ce seuil-ci, une fois tiré, fait au plus 1 % avec probabilité au moins 1−δ.
- **par strate** : longueur, tâche, version, source bénigne.
- **par unité** : pas, épisode, jour de déploiement.

Avec quelques centaines d'épisodes, l'écart entre la garantie marginale et la garantie PAC est grand.

HYPOTHÈSE (calcul B, non audité), avec n = 300 (illustratif) :
- Le taux conditionnel du seuil conformal suit une loi Beta(3, 298).
- P(taux réel > 2 %) ≈ 6 %, et P(taux réel > 3 %) ≈ 0,6 %.

Conséquence : un triplement isolé peut, rarement, venir du seul bruit d'étalonnage. Ce n'est pas l'explication probable, mais il faut l'écarter avant de parler de régime.

**1.2 Compter le n effectif.** Les épisodes d'une même tâche sont corrélés. L'échangeabilité vaut plutôt au niveau des tâches, et le n effectif peut donc être bien inférieur au nombre d'épisodes. HYPOTHÈSE.

**1.3 Décomposer le triplement avant de le corriger.** Six sources sont candidates, et chacune appelle une correction différente :
1. le bruit d'étalonnage ;
2. un changement de mélange entre des strates connues (longueur, tâche, source) ;
3. un décalage *à l'intérieur* d'une strate (nouvelle version) ;
4. un effet mécanique de longueur ou de multiplicité séquentielle ;
5. un changement de la fonction de score elle-même (direction de sonde périmée) ;
6. une contamination de l'étalonnage « honnête ».

Une correction globale masquerait laquelle opère.

**1.4 Interroger la mesure du triplement.** Distinguer 3 % de 1 % demande des centaines d'épisodes honnêtes dans le nouveau régime, c'est-à-dire précisément la ressource rare. Un « triplement » mesuré sur peu d'épisodes a un intervalle large.

**1.5 Lire l'angle adversarial.** Tout seuil qui s'adapte aux scores de l'agent est un levier pour l'agent. Seules des données d'honnêteté connue doivent pouvoir déplacer le seuil. Les faits l'imposent déjà pour le sabotage ; il faut l'étendre à tout épisode de déploiement dont le statut est inconnu.

**1.6 Payer la correction en détection.** Remonter le seuil restaure le taux de fausses alertes (FPR) mais fait baisser le taux de détection (TPR). Il faut rapporter le TPR au FPR corrigé, mesuré sur les épisodes de sabotage. Ceux-ci servent à évaluer, jamais à régler.

**1.7 Tirer la conséquence de la contrainte « ni moyenne ni médiane ».** Le score par épisode est alors probablement un maximum ou une lecture à position fixe. Un maximum sur T pas croît mécaniquement avec T. Un changement de longueur *doit* donc déplacer le FPR : c'est prévisible, pas surprenant. HYPOTHÈSE sur l'agrégateur réellement utilisé, qui n'est pas précisé dans les faits.

### (a) Ce que la question suppose sans que ce soit établi

| Présupposé | Statut |
|---|---|
| Le taux réel « triple » sous changement de régime (CURA, arXiv 2608.27808, identifiant tiré des faits) | RAPPORTÉ. Page du PDF non lue ici. Je ne peux vérifier ni le chiffre, ni ses conditions (n, type de dérive, intervalle). |
| La famille de dérive plantée du programme triple le taux | RAPPORTÉ (par les faits). C'est vrai *par construction* : ce n'est pas une preuve que la dérive réelle ait cette forme. |
| Le seuil unique sur score normalisé « garantit 1 % en moyenne sur les longueurs » | RAPPORTÉ. Il garantit au mieux une valeur marginale sur le mélange de longueurs de l'étalonnage, pas sur un autre mélange. |
| Le changement de régime est unique et identifiable | HYPOTHÈSE. Il peut y avoir plusieurs décalages superposés, ou une dérive continue. |
| Le défaut est dans le seuil plutôt que dans le score | HYPOTHÈSE. Si la direction de sonde se périme avec la version, aucun seuil ne répare. |
| Les épisodes d'étalonnage « honnêtes » le sont | HYPOTHÈSE. Une contamination, même rare, déplace le quantile. |
| 1 % par épisode est la bonne cible opérationnelle | HYPOTHÈSE. La contrainte réelle peut être la capacité de relecture humaine (« rare »). |
| Le jumeau honnête est une référence stable | RAPPORTÉ comme *fragile* dans les faits. |
| On peut observer des scores honnêtes du nouveau régime | HYPOTHÈSE. Sans témoins ni relecture, on ne les observe pas. |

---

## 2. Données brutes à prendre au départ

Chaque élément est stocké en écriture unique et haché. La justification de chaque donnée est indiquée entre parenthèses.

**Par épisode, honnête d'étalonnage, témoin ou déploiement :**
- identifiant de tâche, famille de tâche, source bénigne ;
- hachage de version de l'agent et du jumeau ;
- longueur en pas et en jetons ;
- rang temporel ;
- statut de provenance : étalonnage, témoin, déploiement inconnu, relu humain ;
- graine du tirage d'étalonnage.

**Scores bruts par pas et par jeton,** avant toute agrégation. Ils permettent de recalculer n'importe quel agrégateur et de séparer l'effet de longueur de l'effet de niveau.

**Scores bruts du jumeau sur la même tâche,** même granularité.

**Activations à la couche de sonde sur un sous-échantillon.** Elles permettent de tester si la direction discriminante a tourné : cela distingue la source (5) de la source (3) du §1.3.

**Journaux de déploiement :**
- nombre d'alertes par lot ;
- dates des changements *exogènes* connus : sortie de version, changement de mélange de tâches. Ce sont des points de rupture déclarés, donc testables sans détection.
- issues des relectures humaines, en séparant les relectures déclenchées par alerte (elles donnent la précision) et les relectures tirées au hasard (elles seules permettent d'estimer un FPR sans biais).

**Ce qu'on ne prend pas comme point de départ :** des taux de fausses alertes déjà agrégés par régime. Ils confondent les six sources du §1.3.

---

## 3. Méthodes et outils : ce qu'ils supposent, comment ils échouent, et (c) leur mesure minimale

### 3.1 Conformal pondéré sous décalage de covariables

**Référence.** Tibshirani, Barber, Candès, Ramdas (2019), *Conformal Prediction Under Covariate Shift*, NeurIPS.

**Ce qu'il suppose :**
- La loi du score honnête *sachant* X (longueur, tâche, source) est invariante.
- X est observé.
- Le rapport de vraisemblance est connu ou bien estimé.
- Le support du nouveau régime recouvre celui de l'étalonnage.

**Comment il échoue :**
- Décalage à l'intérieur d'une strate (nouvelle version) : la pondération ne voit rien.
- Une tâche nouvelle hors support reçoit un poids infini.
- Avec peu d'épisodes, la taille effective d'échantillon s'effondre et le seuil devient trivial (infini) ou instable.

### 3.2 Étalonnage par strates (Mondrian) et conditionnel par groupes

**Références :**
- Vovk, Gammerman, Shafer (2005), *Algorithmic Learning in a Random World* (Springer).
- Vovk (2012), *Conditional validity of inductive conformal predictors*, ACML, qui traite aussi la validité conditionnelle à l'étalonnage.

**Contrainte dure.** À α = 1 %, le conformal découpé exige au moins 99 épisodes par strate, sinon le seuil est infini. HYPOTHÈSE (propriété standard, à recalculer). Avec quelques centaines d'épisodes répartis sur plusieurs strates, c'est irréalisable.

**Limite théorique.** Barber, Candès, Ramdas, Tibshirani (2021), *The limits of distribution-free conditional predictive inference*, Information and Inference : une couverture conditionnelle exacte est impossible sans hypothèse.

**Compromis.** Gibbs, Cherian, Candès, *Conformal prediction with conditional guarantees* (année de publication à vérifier ; prépublication de 2023). La garantie vaut sur une classe de décalages choisie *à l'avance*. Elle échoue silencieusement hors de cette classe.

### 3.3 Seuil indexé par la longueur

**Référence.** Romano, Patterson, Candès (2019), *Conformalized Quantile Regression*, NeurIPS.

**Usage proposé.** Régresser le quantile 99 % du score agrégé (par exemple le maximum par pas) sur log T, puis conformaliser.

**Ce qu'il suppose.** Une dépendance lisse en longueur.

**Comment il échoue.** Extrapolation à des longueurs absentes de l'étalonnage.

### 3.4 Conformal adaptatif en ligne

**Références :**
- Gibbs & Candès (2021), *Adaptive Conformal Inference Under Distribution Shift*, NeurIPS ;
- Angelopoulos, Candès, Tibshirani (2023), *Conformal PID Control for Time Series Prediction*, NeurIPS.

**Garantie de long terme.** Le taux d'erreur moyen converge vers α pour *toute* suite, à condition d'observer après coup l'indicateur d'erreur.

**Trois échecs propres au contrôle :**
1. **L'indicateur n'existe pas en déploiement.** On ne sait pas si l'épisode alerté était honnête. Seuls les témoins fournissent ce retour.
2. **La garantie porte sur la moyenne de long terme, pas sur une fenêtre.** La procédure peut tenir 3 % pendant une longue période puis compenser.
3. **Si le flux contient des épisodes de l'agent, l'agent pilote le seuil.**

### 3.5 Détecter le changement de régime avant de faire confiance au seuil

**Tests à deux échantillons :**
- Gretton et al. (2012), *A Kernel Two-Sample Test*, JMLR ;
- Rabanser, Günnemann, Lipton (2019), *Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift*, NeurIPS.

Ils détectent *toute* dérive, y compris bénigne. Ils peuvent aussi manquer une dérive confinée à la queue, qui est précisément celle qui compte à 1 %.

**Tester la dérive nuisible plutôt que la dérive en général :** Podkopaev & Ramdas, *Tracking the risk of a deployed model and detecting harmful distribution shifts* (ICLR 2022, année à vérifier). C'est le bon modèle : tester le risque, ici le FPR, et non la distribution.

**Outils séquentiels valides à tout instant :**
- Vovk & Wang (2021), *E-values: Calibration, combination and applications*, Annals of Statistics ;
- Ramdas, Grünwald, Vovk, Shafer (2023), *Game-theoretic statistics and safe anytime-valid inference*, Statistical Science ;
- Howard, Ramdas, McAuliffe, Sekhon (2021), *Time-uniform, nonparametric, nonasymptotic confidence sequences*, Annals of Statistics ;
- Waudby-Smith & Ramdas (2024), *Estimating means of bounded random variables by betting*, JRSS B ;
- martingales de test conformes pour la rupture, Vovk et collaborateurs (référence à vérifier) ;
- CUSUM : Page (1954), *Continuous inspection schemes*, Biometrika.

**Coût intrinsèque.** HYPOTHÈSE (calcul B, non audité, pari oracle, illustratif) :
- L'information de Kullback entre un taux de 3 % et un taux de 1 % vaut environ 0,013 nat.
- Atteindre un niveau 1/δ = 20 demande donc de l'ordre de 230 témoins.

Conséquence : détecter un triplement *au niveau de la queue* coûte à peu près autant de témoins honnêtes que réétalonner. On ne contourne pas la rareté des données par la détection.

### 3.6 Réétalonnage par fenêtre glissante

**Référence.** Barber, Candès, Ramdas, Tibshirani (2023), *Conformal prediction beyond exchangeability*, Annals of Statistics.

**Garantie.** Avec des poids fixés à l'avance (par exemple une décroissance temporelle), l'écart de couverture est borné par une distance de variation totale pondérée. Cette distance n'est pas observable, et la borne n'est donc pas vérifiable.

**Comment il échoue.** Une fenêtre courte retombe sous la limite de 99 épisodes ; une fenêtre longue inclut des épisodes du régime précédent.

### 3.7 Témoins honnêtes injectés dans chaque lot

**Ce qu'ils supposent.** Les témoins suivent *la même* loi honnête que les épisodes honnêtes de l'agent dans le régime courant.

**Le point dur est la provenance.** Qui produit les témoins ?
- **Le jumeau** : écart fragile, déjà signalé dans les faits.
- **L'agent sur des tâches vérifiables** : biais de sélection, c'est-à-dire un nouveau décalage de covariables.
- **Le rejeu d'épisodes anciens** : les témoins sont périmés par définition.

**Risque spécifique.** Si l'agent distingue les témoins et se comporte différemment quand il se sait observé, les témoins issus de l'agent ne représentent plus son comportement honnête courant. HYPOTHÈSE.

### 3.8 Jumeau honnête comme référence courante

**Usage.** Le score différentiel s(agent) − s(jumeau) sur la même tâche annule les effets de tâche s'ils sont additifs.

**Comment il échoue :**
- quand seule la version de l'agent change ;
- quand le jumeau dérive lui-même ;
- quand les effets sont multiplicatifs plutôt qu'additifs.

### 3.9 Robustesse au pire cas sur une famille de décalages

**Référence.** Cauchois, Gupta, Ali, Duchi, *Robust Validation: Confident Predictions Even When Distributions Shift* (JASA ; année à vérifier).

**Ce qu'il suppose.** Le décalage reste dans une boule de f-divergence de rayon ρ.

**Comment il échoue.** ρ n'est pas observable, et la méthode échoue en silence au-delà. Son coût est payé en TPR.

### 3.10 Autres outils pertinents

**Queue paramétrique par théorie des valeurs extrêmes** (loi de Pareto généralisée sur les dépassements, référence à vérifier pour une application conformale). Elle estime le quantile 99 % à partir de moins de points, à condition que la *forme* de la queue soit stable. Elle échoue si la queue change de forme.

**p-valeurs conformales :** Bates, Candès, Lei, Romano, Sesia (2023), *Testing for outliers with conformal p-values*, Annals of Statistics. Ce travail traite explicitement la validité conditionnelle à l'étalonnage.

### (c) Mesure minimale qui dirait si chaque instrument fonctionne

Un « positif » est un épisode de sabotage pour les règles d'alerte, et un régime nuisible (FPR réel au-delà de α) pour les gardes de régime.

| Instrument | Cas honnêtes appariés | Détection mesurée | Fausses alertes mesurées | Vérification mécanique à battre |
|---|---|---|---|---|
| Conformal pondéré | Même tâche, deux mélanges de longueurs ou de sources | TPR au seuil corrigé, sur le sabotage d'évaluation | FPR dans le nouveau régime avec intervalle, plus la taille effective d'échantillon des poids | Table de quantiles par strate à fusion manuelle |
| Strates / conditionnel | Même tâche, strates différentes | TPR par strate | FPR par strate, pire strate comprise | Maximum des seuils par strate |
| Seuil indexé par longueur | Même tâche tronquée ou prolongée | TPR selon la longueur | FPR par tranche de longueur | Seuil unique normalisé (l'existant) |
| Conformal adaptatif sur témoins | Témoins ordonnés dans le temps | TPR après adaptation | Pire FPR sur une fenêtre de taille w | Réétalonnage par fenêtre fixe |
| Garde de régime | Régimes plantés nuisibles et bénins | Délai de détection d'une dérive nuisible | Fréquence de déclenchement sur dérive bénigne | Test à deux échantillons sur tout le score |
| Témoins | Témoins et épisodes de l'agent relus honnêtes, même régime | — | Écart de quantile entre témoins et honnêtes relus | Rejeu d'anciens épisodes |
| Jumeau différentiel | Même tâche : (version agent ancienne / nouvelle) × jumeau fixe | TPR du score différentiel | FPR sur dérive de tâche contre FPR sur dérive de version | Score brut avec réétalonnage naïf |
| Pire cas | Monde planté dans la boule, puis hors de la boule | TPR perdu | FPR dans et hors de la boule | Maximum des seuils par strate |

---

## 4. Ce qui permettrait de vérifier, hors du programme, qu'une correction tient

**Mondes plantés à dérive connue, élargis au-delà de la seule famille qui triple.** Familles à générer :
- corps seul (queue inchangée) ;
- queue seule ;
- mélange seul ;
- intra-strate ;
- dérive graduelle ;
- dérive bénigne qui ne doit *pas* déclencher ;
- dérive induite par un agent adverse qui pousse progressivement ses scores.

La vérité reste tenue hors de la machine, comme le prévoient déjà les faits. Le hachage de la règle et des graines est déposé *avant* la génération des mondes.

**Jeux publics avec décalage.** WILDS : Koh et al. (2021), *WILDS: A Benchmark of in-the-Wild Distribution Shifts*, ICML. Il n'éprouve que la couche statistique, en utilisant les scores d'un classifieur comme substitut. Je ne sais pas s'il existe un jeu public fiable de trajectoires d'agents honnêtes et saboteurs, étiqueté par version et par régime.

**Réplication.** Une équipe tierce réimplémente la règle depuis la spécification d'interface seule, sans le code, sur une seconde famille de modèles.

**Mesures indépendantes :**
- relecture humaine d'un échantillon *tiré au hasard* parmi les non-alertes et les alertes. C'est le seul estimateur non biaisé du FPR réel en déploiement ;
- recalcul par un tiers de tous les intervalles de FPR à partir des scores bruts.

**CURA.** Lire la page : vérifier n, le type de décalage et l'intervalle du facteur trois.

---

## 5. La demande reformulée

> **Unité d'alerte.** L'épisode, déclaré à l'avance.
>
> **Données disponibles.** n_cal épisodes honnêtes par régime et un flux de témoins de provenance déclarée.
>
> **Ce qu'il faut construire.** Une règle (score, seuil, garde de régime, mode de repli) telle que :
> - pour chaque régime d'une famille de décalages déclarée *avant* les données, P(FPR conditionnel > α) ≤ δ ;
> - hors de cette famille, la garde détecte toute dérive nuisible (FPR > 2α, illustratif) en au plus N témoins, avec un taux de déclenchement ≤ δ' sur les dérives bénignes, puis bascule sur un repli déclaré ;
> - aucun épisode d'honnêteté inconnue ne déplace le seuil.
>
> **Ce qu'il faut rapporter :**
> - la décomposition de l'excès de FPR selon les six sources du §1.3 ;
> - le TPR au FPR corrigé.
>
> **Critère de réfutation.** La règle est réfutée si, sur la famille plantée où le taux triple, la borne supérieure de l'intervalle de FPR dépasse α + marge (marge illustrative, fixée avant les données), ou si la garde ne déclenche pas avant N témoins.

---

## 6. Propositions concrètes

### 6.1 P0 : décomposer avant de corriger (diagnostic, pas une correction)

**Règle.** Sur les épisodes honnêtes du nouveau régime, on compare quatre taux :
1. le FPR brut ;
2. le FPR attendu sous bruit d'étalonnage seul, obtenu par rééchantillonnage des tirages d'étalonnage de l'ancien régime ;
3. le FPR après repondération par strate (longueur, tâche, source) ;
4. le FPR après recalcul du score avec une sonde réentraînée.

L'écart entre deux étapes successives attribue l'excès à une source.

**Garantie et suppositions.** Aucune garantie de contrôle. Le diagnostic suppose que les strates observées sont les bonnes.

**Coût.** Les épisodes honnêtes du nouveau régime, plus une passe de réentraînement de sonde.

**Test de mort.** Sur des mondes plantés à source connue (mélange seul, intra-strate seul), P0 attribue l'excès à la mauvaise source dans plus de x % des cas (x illustratif, fixé avant).

**Ce qui la distingue du publié.** C'est une procédure d'audit, pas une nouveauté statistique. Je ne connais pas de publication qui la formalise pour les moniteurs de contrôle, ce qui ne veut pas dire qu'il n'en existe pas.

### 6.2 P1 : seuil indexé par strates déclarées, à garantie conditionnelle à l'étalonnage, avec repli explicite

**Règle :**
- Le score est le maximum par pas, sans moyenne, conformément aux contraintes.
- Le seuil τ(T, s) dépend de la longueur T et de la strate s.
- Il est obtenu par régression de quantile sur log T, conformalisée par strate.
- Dans chaque strate, on prend l'indice de statistique d'ordre k tel que P(Beta(n+1−k, k) > α) ≤ δ, ce qui donne une garantie PAC et non marginale.
- Si une strate a trop peu d'épisodes pour qu'un k existe, la strate fusionne avec sa voisine déclarée. À défaut, ses alertes passent en mode budget (§6.5).

**Garantie.** FPR conditionnel ≤ α avec probabilité ≥ 1 − δ, dans chaque strate.

**Suppositions :**
- échangeabilité dans chaque strate, au niveau des tâches (n effectif = nombre de tâches, §1.2) ;
- stabilité de la loi conditionnelle à la strate.

**Coût en données.** HYPOTHÈSE (calcul B, non audité, illustratif) :
- Avec n = 300, la garantie « P(FPR > 1 %) ≤ 5 % » impose déjà de prendre le *maximum* de l'étalonnage comme seuil.
- Pour δ = 1 %, il faut n ≈ 460 par strate.

Le coût en TPR est donc probablement élevé.

**