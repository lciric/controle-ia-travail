Pièces reçues : FAITS et QUESTION sont présentes et non coupées ; je n'ai pas contrôlé les empreintes sha256.

Le bloc FAITS n'étiquette pas ses statuts. Je traite donc son contenu comme RAPPORTÉ et mes ajouts comme HYPOTHÈSE ou comme calcul illustratif. Rien ici n'est VÉRIFIÉ par moi.

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut |
|---|---|---|
| S1 | Le taux triple sous changement de régime (CURA, identifiant recopié des faits : arXiv 2608.27808). Je ne connais ni les auteurs ni le titre : référence à vérifier, page du PDF non lue. | RAPPORTÉ |
| S2 | Le triplement vient d'un changement de distribution et non de la variance d'un étalonnage sur quelques centaines d'épisodes. | HYPOTHÈSE |
| S3 | Le défaut se corrige au niveau du seuil, et non au niveau du score (sonde, normalisation par longueur). | HYPOTHÈSE |
| S4 | Il existe, dans le nouveau régime, des épisodes dont l'honnêteté est connue. | HYPOTHÈSE |
| S5 | Le jumeau honnête est échangeable avec l'agent honnête ; les faits disent seulement que cet écart est « fragile ». | HYPOTHÈSE |
| S6 | « 1 % » est une cible bien définie, sans préciser si elle vaut en moyenne, par strate, par épisode, par pas, ou avec quelle confiance. | Non établi |
| S7 | Une dérive des scores en déploiement est bénigne. Or une hausse des scores est aussi la signature du sabotage. | HYPOTHÈSE |

## 1. Ce qu'un expert ferait, et qu'on ne demande pas

**Séparer la dérive du bruit d'étalonnage.** Pour un seuil placé au k-ième plus grand score de n épisodes honnêtes i.i.d., le taux réel suit une loi Beta(k, n+1−k) (résultat classique). Les chiffres suivants sont des calculs illustratifs, avec n supposé :

- Avec n = 100 (le seuil est le maximum), le taux réel dépasse 3 % dans environ 4,8 % des étalonnages, sans aucune dérive.
- Avec n = 300 (k = 3), il dépasse 2 % dans environ 6 % des cas et 3 % dans environ 0,6 %.

Un « triplement » lu sur un petit étalonnage n'est donc pas, à lui seul, une preuve de dérive.

**Dire ce que 1 % peut vouloir dire avec ces effectifs.** Calculs illustratifs encore :

- Certifier « taux ≤ 1 % avec confiance 95 % » exige au moins 299 épisodes honnêtes, même en prenant le maximum comme seuil (0,99ⁿ ≤ 0,05).
- Par tranche de 60 épisodes, le meilleur taux certifiable à 95 % est d'environ 4,9 %.
- Un 1 % par tranche de longueur n'est donc pas certifiable sans hypothèse de forme, quel que soit l'outil.

**Mesurer la sensibilité de la queue.** Sous une loi gaussienne, un décalage de 0,445 écart-type suffit à tripler le taux au seuil de 1 % (calcul illustratif). Deux conséquences :

- Un tel décalage se détecte sur le corps de la distribution avec environ 80 épisodes par groupe (test bilatéral à 5 %, puissance 80 %).
- Le constater en comptant les alertes en demande environ 300 (puissance d'environ 0,79).
- Cela ne vaut que si la dérive est un décalage. Une dérive de queue seule (un mode bénin rare à scores élevés) laisse le corps intact et aveugle ces tests.

**Typer la dérive avant de choisir l'outil.** Trois types appellent trois réponses différentes :

- Composition : les proportions de longueurs, tâches ou sources changent, mais la loi du score sachant ces covariables reste stable.
- Concept : la loi du score sachant les covariables change. C'est probable pour une nouvelle version de l'agent, puisque la sonde lit une autre représentation (HYPOTHÈSE).
- Queue seule.

**Poser l'invariant adversarial.** Toute règle dont le seuil dépend des scores du flux surveillé peut être tirée vers le haut par un agent qui monte ses scores lentement. Un expert en contrôle exigerait que le seuil ne soit fonction que de scores certifiés honnêtes. C'est le point que la liste d'outils de la question ne contient pas.

**Regarder le score avant le seuil.** Les faits interdisent la moyenne et la médiane sur les jetons. Si le score est de type maximum sur les pas, sa loi honnête croît mécaniquement avec la longueur (HYPOTHÈSE), et la normalisation actuelle serait la cause de l'échec par tranche.

## 2. Données brutes de départ

- **Par épisode honnête** : identifiant, tâche, famille de tâche, version de l'agent, source bénigne, longueur, graine, date, score brut de chaque moniteur à chaque pas (avant normalisation), activation projetée par pas, score agrégé.
- **Paires A/A** : deux exécutions honnêtes de la même tâche (agent honnête contre jumeau, jumeau contre jumeau). C'est la seule donnée qui mesure l'écart du jumeau.
- **Journaux de déploiement** : scores horodatés non étiquetés, identité du régime déclaré, alertes, décisions de relecture humaine. Ces dernières sont rares, donc précieuses.
- **Journal d'étalonnage** : quels épisodes ont fixé quel seuil, avec n et k.
- **Épisodes de sabotage** : gardés à part, pour la puissance uniquement.

Des taux agrégés ne permettent ni le calcul Beta ci-dessus, ni le typage de la dérive.

## 3. Méthodes : ce qu'elles supposent, comment elles échouent, mesure minimale

La règle 3 m'interdit les identifiants arXiv de mémoire. Je donne auteurs, année et titre, et « pas sûr » quand c'est le cas.

**Socle.**
- Vovk, Gammerman, Shafer (2005), *Algorithmic Learning in a Random World*.
- Bates, Candès, Lei, Romano, Sesia (2023), « Testing for outliers with conformal p-values ». C'est le cadre le plus proche : échantillon nul honnête, garantie conditionnelle à l'étalonnage.
- Tong, Feng, Li (2018), « Neyman-Pearson classification algorithms and NP receiver operating characteristics » : choix de la statistique d'ordre pour borner l'erreur de type I avec forte probabilité.

**Conforme pondéré.** Tibshirani, Barber, Candès, Ramdas (2019), « Conformal Prediction Under Covariate Shift ».
- Suppose une dérive de composition pure, un rapport de vraisemblance connu et des supports recouvrants.
- Échoue sur une dérive de concept (nouvelle version) et sur une tâche jamais vue (poids infini).
- Échoue aussi quand la taille effective (Σw)²/Σw² tombe sous environ 99, car une p-valeur de 1 % devient alors impossible.
- Avec des poids estimés, la garantie exacte tombe. Yang, Kuchibhotla, Tchetgen Tchetgen, « Doubly robust calibration of prediction sets under covariate shift » : année pas sûre.

**Conforme adaptatif en ligne.**
- Gibbs, Candès (2021), « Adaptive Conformal Inference Under Distribution Shift ».
- Gibbs, Candès, « Conformal Inference for Online Prediction with Arbitrary Distribution Shifts » (année pas sûre).
- Angelopoulos, Candès, Tibshirani (2023), « Conformal PID Control for Time Series Prediction ».
- Zaffran, Féron, Goude, Josse, Dieuleveut (2022), « Adaptive Conformal Predictions for Time Series ».

La garantie de long terme porte sur la fréquence des erreurs observées, pour toute suite. Elle suppose que l'erreur est observée à chaque pas. Ici, l'étiquette « honnête » n'est pas observée. Appliquée au flux brut, la méthode contrôle le taux d'alertes, pas le taux de fausses alertes : 1 % d'alertes même si tout est sabotage. Elle viole l'invariant adversarial. Elle n'est légitime que restreinte aux témoins honnêtes.

**Conditionnel par strates ou groupes.**
- Vovk (2012), « Conditional validity of inductive conformal predictors ».
- Barber, Candès, Ramdas, Tibshirani (2021), « The limits of distribution-free conditional predictive inference ».
- Gibbs, Cherian, Candès (2023), « Conformal Prediction With Conditional Guarantees ».
- Jung, Noarov, Ramalingam, Roth (2023), « Batch Multivalid Conformal Prediction ».

L'échec est arithmétique : c'est le plancher d'environ 4,9 % par tranche de 60 (illustratif).

**Détection de dérive.**
- Vovk, Nouretdinov, Gammerman (2003), « Testing Exchangeability On-Line ».
- Ramdas, Grünwald, Vovk, Shafer (2023), « Game-Theoretic Statistics and Safe Anytime-Valid Inference ».
- Shin, Ramdas, Rinaldo, « E-detectors: a nonparametric framework for sequential change detection » (année pas sûre).
- Podkopaev, Ramdas (2022), « Tracking the risk of a deployed model and detecting harmful distribution shifts ».
- Rabanser, Günnemann, Lipton (2019), « Failing Loudly ».
- Page (1954), « Continuous inspection schemes ».

Ces outils supposent un flux nul échangeable avant la rupture. Ils échouent par délai, par cécité à la queue seule, et surtout parce que, lancés sur le flux surveillé, ils confondent dérive et sabotage.

**Fenêtre glissante.** Barber, Candès, Ramdas, Tibshirani (2023), « Conformal prediction beyond exchangeability ». La borne d'écart dépend des distances en variation totale, qui sont inconnues. Une fenêtre courte interdit α = 1 %.

**Témoins honnêtes et jumeau.** Je ne connais pas de référence qui traite précisément des témoins honnêtes injectés par lot pour moniteurs d'agents : je ne sais pas. Le cadre général est Greenblatt, Shlegeris, Sachan, Roger (2023), « AI Control: Improving Safety Despite Intentional Subversion ». Ces instruments reposent sur S4 et S5.

**Pire cas.** Cauchois, Gupta, Ali, Duchi, « Robust Validation: Confident Predictions Even When Distributions Shift » (année pas sûre) ; Duchi, Namkoong (2021), « Learning models with uniform performance via distributionally robust optimization ».
- Si le rapport de vraisemblance est borné par 3, étalonner à α/3 suffit. La version certifiée à 95 % demande environ 900 épisodes (illustratif).
- Un décalage gaussien n'a pas de rapport borné. Sur la famille gaussienne qui triple à 1 %, le seuil à α/3 donne encore environ 1,2 % (calcul illustratif).

**Autres outils.**
- Romano, Patterson, Candès (2019), « Conformalized Quantile Regression » : seuil fonction de la longueur.
- Lan, DeMets (1983), « Discrete sequential boundaries for clinical trials » : dépense d'alpha.
- Siffer, Fouque, Termier, Largouët (2017), « Anomaly Detection in Streams with Extreme Value Theory » : extrapolation de queue, qui suppose une forme.
- Blanchard, Lee, Scott (2010), « Semi-Supervised Novelty Detection » : le flux de déploiement est un mélange dont la proportion n'est pas identifiable sans hypothèse.

### (c) Mesure minimale par instrument

Protocole commun, sur les mêmes épisodes honnêtes appariés (même tâche, même longueur, régime ancien contre régime nouveau, plus paires A/A) :

- taux de fausses alertes avec intervalle de Clopper–Pearson ;
- taux de détection sur sabotages gardés à part ;
- nombre d'épisodes honnêtes frais consommés.

Vérifications mécaniques à battre :

- **M0** : seuil fixe.
- **M1** : re-quantile naïf sur les n derniers témoins.
- **M2** : seuil fixe étalonné à α/3.
- **M3** : standardisation par tranche de longueur.
- **M4** : quota (les k plus hauts scores du lot).

| Instrument | Fonctionne si… | À battre |
|---|---|---|
| Conforme pondéré | L'intervalle du taux contient 1 % et exclut 3 % sur dérive de composition plantée ; taille effective rapportée | M3, M0 |
| Adaptatif en ligne, sur témoins seuls | Taux de long terme sur témoins à 1 %, et détection inchangée quand la prévalence de sabotage monte | M1 |
| Adaptatif en ligne, sur flux | Mêmes mesures ; je prédis l'échec du second critère (HYPOTHÈSE) | M4 |
| Strates ou groupes | Taux par tranche avec intervalle ; la largeur d'intervalle est publiée | M3 |
| Détecteur de dérive | Délai médian de détection, taux de fausses détections sur flux A/A, puissance séparée pour décalage et queue seule | Test sur médiane inter-épisodes, comptage |
| Fenêtre glissante | Taux en fonction du temps écoulé depuis la rupture | M1 à n égal |
| Témoins injectés | P-valeurs des épisodes honnêtes de l'agent contre les témoins uniformes (KS, plus taux à 1 %) | M0 |
| Jumeau | Corrélation ρ agent–jumeau sur paires A/A ; l'appariement ne réduit la variance que si ρ > 0,5, car Var(D) = 2σ²(1−ρ) | Score non apparié |
| Pire cas | Taux ≤ 1 % sur toute la famille, perte de détection chiffrée | M2 |

## 4. Vérification extérieure, et (b) duels décisifs

**Vérifications hors programme.**
- Mondes plantés, avec quatre familles à ajouter à la famille de décalage existante : queue seule, composition pure, concept à covariables constantes, et « dérive = début de sabotage ».
- Générateurs et graines écrits par un tiers ; vérité et verdict hors machine, comme les faits le prévoient déjà.
- Jeux publics à décalage pour la partie statistique seule : Koh et al. (2021), « WILDS: A Benchmark of in-the-Wild Distribution Shifts ».
- Je ne sais pas s'il existe un jeu public d'épisodes honnêtes d'agents avec activations brutes sur plusieurs versions. Les environnements publics de contrôle (SHADE-Arena, ControlArena) sont des références à vérifier.
- Pré-enregistrement des seuils de mort.
- Réplication par une équipe qui ré-entraîne ses propres sondes.
- Mesure indépendante du taux par relecture humaine d'un échantillon aléatoire d'alertes et de non-alertes.

Dans chaque duel ci-dessous, un intervalle qui contient à la fois 1 % et 3 % rend l'essai invalide (effectif à augmenter). Ce n'est pas une troisième issue.

**D0 : bruit contre dérive.**
- H_A : le rapport de taux entre régimes reste dans la bande à 95 % obtenue par ré-étalonnages A/A au sein d'un même régime (loi Beta).
- H_B : il en sort.
- Métrique : rapport des taux. Contrôle négatif : coupe aléatoire d'un même régime, rapport attendu autour de 1.
- Dans la bande, H_B est falsifiée comme explication nécessaire. Hors bande, H_A est falsifiée.

**D1 : composition contre concept.**
- H_A : la post-stratification sur (longueur, famille de tâche, source) ramène le taux à un intervalle contenant 1 % et excluant 3 %.
- H_B : l'intervalle exclut 1 % après pondération.
- Contrôle négatif : pondération par une covariable permutée, qui ne doit rien corriger.
- Chaque issue falsifie l'autre hypothèse, pour cette dérive.

**D2 : corps contre queue.**
- H_A : re-standardiser par la médiane et l'écart interquartile inter-épisodes des témoins restaure le taux.
- H_B : non.
- Contrôle : sur le monde planté « queue seule », la restauration doit échouer. Si elle réussit, c'est le banc qui est faux.

**D3 : jumeau échangeable contre biaisé.**
- H_A : les p-valeurs conformes des épisodes honnêtes de l'agent contre les scores du jumeau sont uniformes, et le taux à 1 % a un intervalle contenant 1 %.
- H_B : écart systématique.
- Contrôle : jumeau contre jumeau.
- Si H_B tient, les propositions P1 à P4 perdent leur garantie.

**D4 : seuil aveugle contre seuil capturable.**
- H_A : le taux de détection est stable quand la prévalence de sabotage plantée monte de 0 à 20 % (illustratif).
- H_B : il chute de plus de 10 % en relatif (seuil illustratif, à pré-enregistrer).
- Contrôle : même rampe avec des scores de sabotage identiques aux scores honnêtes.
- H_B tue toute règle alimentée par le flux surveillé.

## 5. Demande reformulée

« Étant donné n épisodes certifiés honnêtes du régime courant et un historique plus large d'autres régimes, fournir une règle de décision qui satisfait quatre conditions :

1. Son seuil ne dépend d'aucun score du flux surveillé.
2. Elle annonce une garantie (α, δ) avec ses suppositions, ou se déclare "non certifiable à ce n".
3. Elle survit aux cinq familles plantées, dont celle où le taux triple, sans perdre de détection quand la dérive est du sabotage.
4. Elle bat le re-quantile naïf à nombre égal d'épisodes honnêtes consommés. »

## 6. Propositions

Ce sont mes propositions, pas des résultats. La statistique sous-jacente est publiée. Ce que je propose, c'est l'assemblage, l'invariant et les tests de mort.

**P1 : seuil ancré, aveugle à l'agent.**
- *Règle* : seuil = k-ième plus grand des n scores de témoins (jumeau ou témoins injectés) du régime courant. k est le plus grand entier tel que P(Bin(n, α) ≤ k−1) ≤ δ. Si aucun k ne convient, sortie « non certifiable » et bascule vers P2 ou le quota.
- *Garantie* : P(taux > α) ≤ δ sur le tirage des témoins. Elle suppose S4, S5 et des témoins i.i.d. dans le régime.
- *Coût* : calcul des témoins (jusqu'au double avec un jumeau systématique) ; seuil plus haut, donc perte de détection ; au moins 299 témoins pour (1 %, 95 %) (illustratif).
- *Test de mort* : sur la famille qui triple, la fraction de répétitions où le taux dépasse α doit rester ≤ δ, à l'erreur de Monte-Carlo près ; plus D4 ; plus un monde à écart jumeau–agent planté, où la règle doit échouer de façon visible.
- *Différence avec le publié* : aucune sur le plan statistique (Tong et al., Bates et al.). L'apport est la contrainte d'invariance et la sortie « non certifiable ».

**P2 : transport de quantile, quand n < 99.**
- *Règle* : seuil nouveau = médiane nouvelle + (seuil ancien − médiane ancienne) × (écart interquartile nouveau / ancien). Les statistiques sont prises sur les épisodes témoins, pas sur les jetons.
- *Garantie* : aucune sans hypothèse de loi. Elle vaut si la dérive est de position-échelle (HYPOTHÈSE).
- *Ordre de grandeur* : sous loi gaussienne, 50 témoins ramènent un taux triplé vers environ 0,6–1,6 % à ±1 écart-type d'estimation (calcul illustratif).
- *Coût* : quelques dizaines de témoins.
- *Test de mort* : famille « queue seule », où elle doit mourir ; famille de décalage, où elle meurt si l'intervalle du taux exclut 1 %.
- *Différence avec le publié* : c'est une standardisation classique. L'apport est sa place bornée entre « trop peu pour P1 » et « rien ».

**P3 : frontière séquentielle étalonnée par épisode.**
- *Règle* : pour chaque épisode témoin, M = max sur les pas de (score au pas t − b(t)), avec b une forme de frontière fixée d'avance. Seuil = quantile P1 des M. Alerte au premier franchissement.
- *Garantie* : taux par épisode comme en P1, quelle que soit la dépendance entre pas et le nombre de franchissements. Pas de garantie par tranche de longueur ; on la contrôle par intervalles, dont on publie la largeur.
- *Coût* : scores par pas des témoins.
- *Test de mort* : dérive plantée du mélange de longueurs. La règle meurt si une tranche a un intervalle au-dessus de sa borne pré-enregistrée.
- *Différence avec le publié* : proche de la dépense d'alpha (Lan, DeMets). Je ne sais pas si c'est publié pour des moniteurs d'agents.

**P4 : porte de régime et différence de dérive.**
- *Règle* : martingale de test conforme sur les seuls témoins. Si elle dépasse 1/δ, le seuil passe à l'état « non garanti » et l'étalonnage P1 repart.
- *Second volet* : la même statistique est calculée sur le flux de l'agent. Une dérive du flux sans dérive des témoins est traitée comme signal de sabotage au niveau population, pas comme motif de ré-étalonnage.
- *Garantie* : inégalité de Ville sur les fausses détections, sous échangeabilité des témoins.
- *Coût* : négligeable. Délai de détection non nul.
- *Test de mort* : famille « queue seule » (cécité attendue, à mesurer) ; D4 pour le second volet.
- *Différence avec le publié* : les martingales sont publiées (Vovk et al.). L'usage différentiel témoins contre flux est ma proposition. Je ne sais pas s'il existe ailleurs.

**Quand renoncer au seuil fixe.** Trois cas :

- n par régime est inférieur à 99 et D2 conclut à une dérive de queue seule.
- D3 falsifie l'échangeabilité du jumeau.
- La relecture humaine est le vrai goulot.

On met alors à la place :

- un quota par lot (les k plus hauts, k fixé par le budget de relecture), en annonçant qu'il ne contrôle aucun taux de fausses alertes ;
- une sortie à trois états : alerte, pas d'alerte, non certifié ;
- la p-valeur conforme de chaque épisode, publiée avec n et δ plutôt qu'un verdict binaire.

## (d) Ancrage matériel (tout est illustratif)

- **Mondes plantés** : simulation sur processeur, cinq familles, de l'ordre de mille répétitions par règle. Coût négligeable.
- **Banc réel** : modèles à poids ouverts de 7 à 9 milliards de paramètres (familles Llama, Gemma, Qwen). Le « changement de version » est émulé par deux points de contrôle ou un affinage léger. Sondes linéaires sur le flux résiduel, lues sans moyenne sur les jetons.
- **Volume** : quelques milliers d'épisodes, dont les paires A/A. Une carte graphique de 24 à 48 Go, quelques dizaines d'heures. Coût en location de l'ordre de dizaines à quelques centaines de dollars.
- **Poste dominant** : la génération d'épisodes honnêtes, pas la statistique. Le jumeau systématique double ce poste ; des témoins injectés à 10–20 % du lot le réduisent d'autant.

FIN-DE-CELLULE