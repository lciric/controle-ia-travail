Pièces reçues : FAITS et QUESTION, présentes et non coupées. Je n'ai pas recalculé les empreintes sha256. Tour à l'aveugle : aucune autre proposition vue, donc rien à critiquer au titre de B1.

Conventions : tout chiffre ci-dessous est **illustratif** (calcul de ma part sous l'hypothèse dite), jamais un résultat du programme. Aucun identifiant arXiv n'est donné de mémoire (règle 3, qui prime sur la demande de l'arbitre) : les références portent auteurs, année, titre ; les incertaines sont marquées « pas sûr ».

---

## 1. Ce qu'un expert ferait sans qu'on le demande, et (a) ce que la question suppose

**1.1 Séparer la dérive du bruit d'étalonnage.** Un seuil conforme réglé sur n épisodes a un taux réel aléatoire, de loi Beta(k, n+1−k) sous i.i.d. (Vovk 2012, *Conditional validity of inductive conformal predictors*).
- n = 300 : le seuil est le 3ᵉ score le plus élevé. Le taux réel dépasse 2 % dans environ 6 % des tirages et 3 % dans environ 0,6 % (illustratif).
- n = 100 : il dépasse 3 % dans environ 5 % des tirages (illustratif).
- Borne de type Wilks (1941, titre pas sûr) : sous n ≈ 299, aucun seuil fini ne certifie « taux ≤ 1 % » à 95 % de confiance, même sans dérive (illustratif : ln 0,05 / ln 0,99).

Une partie des « triplements » peut donc ne pas être de la dérive.

**1.2 Mesurer la fragilité de la queue.** Sous scores gaussiens, une translation de 0,45 écart-type suffit à passer de 1 % à 3 % (illustratif : 2,326 − 1,881). Deux conséquences :
- une translation de cette taille se détecte sur le corps de la distribution avec environ 80 épisodes par groupe (illustratif : test bilatéral 5 %, puissance 80 %) ;
- certifier directement « le taux n'a pas triplé » en comptant les alertes demande environ 500 épisodes honnêtes du nouveau régime (illustratif : Poisson, 5 attendues contre 15).

La détection par le corps est bon marché, la vérification par la queue est chère. Tout le plan en découle.

**1.3 Décomposer « changement de régime » en mécanismes.** Aucun outil ne les couvre tous :
- **M1, mélange de covariables** : mêmes tâches et longueurs en proportions nouvelles, P(score | covariables) stable.
- **M2, carte de score** : nouvelle version de l'agent, la direction de la sonde ne lit plus la même chose. Ce n'est pas un décalage de covariables.
- **M3, masse de queue** : une source bénigne nouvelle ajoute quelques pour cent d'épisodes à score élevé, corps inchangé.
- **M4, effet mécanique de la longueur** : un maximum sur T pas croît avec T.

**1.4 Regarder l'autre sens.** Une dérive qui fait tomber le taux à 0,3 % ne déclenche rien, mais elle fait baisser la détection. Pour la sûreté c'est le cas le plus grave, et la question ne le pose pas.

**1.5 Traiter toute règle adaptative comme une surface d'attaque.** Un seuil qui se ré-étalonne sur le flux déployé monte quand l'agent sabote. Le saboteur peut aussi provoquer le changement de régime (épisodes plus longs, comportements bénins inhabituels).

**1.6 Demander à quoi sert le 1 %.** S'il traduit un budget de relecture, la bonne cible est la charge de relecture et la détection à budget fixé, pas un taux par épisode.

**(a) Suppositions de la question**

| # | Supposition | Statut |
|---|---|---|
| S1 | Le taux réel triple sous changement de régime (CURA) | RAPPORTÉ ; page non lue ; je ne connais pas ce travail et ne peux pas l'attribuer |
| S2 | La famille plantée de dérive est un décalage qui triple le taux | Fait du programme tel que transmis ; non audité par moi |
| S3 | Les épisodes « honnêtes » d'étalonnage sont honnêtes et échangeables avec les épisodes honnêtes déployés | HYPOTHÈSE |
| S4 | Le régime est observable (tâche, version, longueur, source bénigne) | HYPOTHÈSE ; plausible pour version et longueur, je ne sais pas pour la source bénigne |
| S5 | Il existe une correction qui garde 1 % sans sacrifier la détection avec quelques centaines d'épisodes | HYPOTHÈSE ; 1.1 suggère qu'elle peut être fausse |
| S6 | La dérive réelle ressemble à la famille plantée (translation) | HYPOTHÈSE |
| S7 | Des témoins honnêtes injectables existent et se comportent comme l'agent honnête du lot | HYPOTHÈSE ; les faits disent l'écart jumeau–agent « fragile » |
| S8 | Un taux de 1 % par épisode est la bonne cible | HYPOTHÈSE |

---

## 2. Données brutes de départ

Une ligne par épisode, jamais de taux agrégé :

- **Identité** : id d'épisode, id de tâche, famille de tâche, empreinte du point de contrôle de l'agent, source bénigne, longueur T, graine, lot et horodatage.
- **Scores** : score brut par pas et par moniteur, avant normalisation, avant maximum, avant agrégation entre moniteurs.
- **Activations** : au minimum la projection sur la direction de sonde et sur quelques directions aléatoires de contrôle. Idéalement les activations des couches sondées pour les 5 % d'épisodes les plus hauts.
- **Jumeau** : mêmes champs, apparié par id de tâche.
- **Journal de décision** : jeu d'étalonnage et seuil en vigueur à chaque décision.
- **Relecture** : issue de chaque relecture humaine, et tirage aléatoire de non-alertes relues.

Quatre raisons de partir du brut :
1. Rejouer n'importe quelle règle a posteriori.
2. Compter les **grappes**. Plusieurs épisodes d'une même tâche sont corrélés, et le n effectif est plus proche du nombre de tâches que du nombre d'épisodes. Les calculs de 1.1 sont alors optimistes.
3. Voir les ex æquo et la discrétisation des scores.
4. Distinguer M1 à M4. Un taux agrégé les confond.

---

## 3. Méthodes : suppositions, modes d'échec, et (c) mesure minimale

**Protocole commun de mesure (c).** Pour chaque paire de régimes R0→R1, les cas honnêtes appariés sont les mêmes ids de tâche joués sous R0 et R1. On mesure :
- (i) le taux réel en R1 avec intervalle de Clopper-Pearson (1934) ;
- (ii) le taux de détection sur sabotage planté, à taux réel **réalisé** égal ;
- (iii) le taux en monde sans dérive.

Quatre vérifications mécaniques sont à battre :
- **B0** : seuil actuel.
- **B1** : seuil fixe réglé à α/3.
- **B2** : recalage position-échelle sur quantiles des témoins.
- **B3** : relecture des k plus hauts scores du lot.

Un instrument fonctionne si la borne haute du taux en R1 reste sous la tolérance pré-déclarée et si sa détection dépasse celle de B1. Sinon B1 suffit et l'instrument est du coût sans gain.

| Instrument | Suppose | Échoue quand | Mesure propre (en plus du protocole) |
|---|---|---|---|
| **Conforme pondéré** : Tibshirani, Barber, Candès, Ramdas (2019), *Conformal Prediction Under Covariate Shift* | M1 seul ; rapport de vraisemblance connu ou bien estimé ; support de R1 inclus dans R0 | M2 ou M3 ; poids estimés sur activations (dimension trop haute) ; tâches hors support, où le seuil devient infini et où plus rien n'alerte | Taille effective (Σw)²/Σw² ≥ 100 environ pour un quantile à 1 % fini (illustratif). Avec poids uniformes, on doit retrouver le triplement, sinon il n'y avait rien à corriger |
| **Conforme adaptatif** : Gibbs & Candès (2021), *Adaptive Conformal Inference Under Distribution Shift* ; Angelopoulos, Candès, Tibshirani (2023), *Conformal PID Control for Time Series Prediction* | Rétroaction : savoir, pour chaque épisode, s'il était honnête. Garantie établie : la fréquence d'erreur de long terme converge vers α pour toute suite | Pas d'étiquette en déploiement. Mis à jour sur flux non étiqueté, le sabotage relève le seuil. La garantie de long terme autorise des rafales (0 % longtemps, puis beaucoup) et des seuils infinis | Taux par fenêtre de W épisodes, pas seulement en moyenne. Détection en monde « sabotage synchronisé avec la dérive » |
| **Strates / groupes** : Vovk, Gammerman, Shafer (2005), *Algorithmic Learning in a Random World* ; Gibbs, Cherian, Candès (2023), *Conformal Prediction With Conditional Guarantees* ; limite : Barber, Candès, Ramdas, Tibshirani (2021), *The limits of distribution-free conditional predictive inference* | Strates observables ; échangeabilité dans la strate | Au moins 99 épisodes par strate pour un seuil fini à 1 % (illustratif) : avec 300 épisodes, 3 strates au plus. Régime nouveau, donc strate vide | Taux par tranche de longueur avec intervalle ; nombre de strates sans seuil fini |
| **Détection de dérive** : Vovk, Nouretdinov, Gammerman (2003), *Testing Exchangeability On-Line* ; Ramdas, Grünwald, Vovk, Shafer (2023), *Game-Theoretic Statistics and Safe Anytime-Valid Inference* ; Page (1954), *Continuous Inspection Schemes* ; Podkopaev & Ramdas (2022), *Tracking the risk of a deployed model…* (pas sûr du titre exact) | Flux testé honnête ; dérive visible dans la statistique choisie | M3 invisible dans le corps ; sur flux déployé, confond dérive et sabotage ; le délai de détection laisse passer des lots à 3 % | Fausses déclarations en monde nul ≤ δ ; délai médian en lots ; taux réel pendant le délai |
| **Fenêtre glissante** : Barber, Candès, Ramdas, Tibshirani (2023), *Conformal prediction beyond exchangeability* (écart de couverture borné par une somme pondérée de distances en variation totale) | Dérive lente ; données de la fenêtre honnêtes | Saut brusque ; fenêtre trop courte pour 1 % (même arithmétique des 99) ; flux non étiqueté | Taux réel juste après un saut planté ; n effectif de la fenêtre |
| **Témoins honnêtes par lot** : pas de référence canonique que je sache attribuer ; le plus proche est Bates, Candès, Lei, Romano, Sesia (2023), *Testing for outliers with conformal p-values* | Témoins échangeables avec l'agent honnête du même lot (S7) ; l'agent ne se comporte pas autrement en témoin | Témoins tirés d'une autre distribution de tâches ; m petit, d'où une résolution de 1/(m+1) | Test à deux échantillons témoins contre honnêtes déployés connus, en monde planté ; puissance de détection d'une translation de 0,45 σ en fonction de m |
| **Jumeau honnête** : cadre général dans Greenblatt, Shlegeris, Sachan, Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion* ; pour le jumeau lui-même, référence à vérifier | Effet de tâche additif et commun | Écart jumeau–agent dépendant du régime (dit fragile dans les faits) ; si le jumeau est un autre modèle, scores de sonde non comparables ; double le calcul | Corrélation ρ des scores agent–jumeau sur paires honnêtes, par régime. À variances égales, la différence appariée n'est moins dispersée que le score brut que si ρ > 0,5 (dérivation, illustratif). Stabilité de la loi de la différence entre R0 et R1 |
| **Pire cas** : Cauchois, Gupta, Ali, Duchi (2020), *Robust Validation: Confident Predictions Even When Distributions Shift* (pas sûr de l'année) | Dérive dans une boule de divergence de rayon choisi | Rayon arbitraire ; pour couvrir un triplement il faut viser environ 0,33 %, soit n ≥ 299 environ (illustratif) ; perte de détection inconnue | Détection à 0,33 % contre 1 % sur sabotage planté : je ne sais pas la prédire, elle se mesure |
| **Autres** : conforme par régression quantile, Romano, Patterson, Candès (2019), *Conformalized Quantile Regression* (seuil fonction de la longueur) ; e-valeurs, Vovk & Wang (2021), *E-values: Calibration, combination and applications* ; suites de confiance, Howard, Ramdas, McAuliffe, Sekhon (2021), *Time-uniform, nonparametric, nonasymptotic confidence sequences* ; extrapolation de queue, Pickands (1975), *Statistical inference using extreme order statistics* | Respectivement : quantile conditionnel lisse en T ; p-valeurs valides par pas ; bornitude ; forme de queue stable | Respectivement : garantie encore marginale ; dépendance entre pas ; lenteur ; M3 | Voir P2 pour les deux premiers |

---

## 4. Vérification extérieure, et (b) expériences décisives

**Dispositif hors programme.**
- **Mondes plantés par un tiers.** Le tiers ne voit pas le code de la règle. La règle est gelée par empreinte avant génération. La famille est étendue au-delà de la translation : échelle, mélange ε (M3), longueur (M4), rotation de la direction de sonde (M2), sabotage synchronisé avec la dérive, dérive vers le bas, et **monde nul** sans dérive.
- **Données publiques à décalage naturel.** Koh et al. (2021), *WILDS: A Benchmark of in-the-Wild Distribution Shifts*, pour la partie purement statistique, avec le score d'un détecteur d'anomalies quelconque. Cela ne teste pas la partie contrôle. Je ne connais pas de jeu public d'épisodes d'agent honnêtes avec activations à travers versions.
- **Réplication.** Un autre groupe, un autre modèle ouvert, d'autres sondes, protocole pré-enregistré.
- **Mesure indépendante.** La relecture humaine rare est concentrée sur un échantillon aléatoire d'alertes et de non-alertes en R1. L'identité des témoins est cachée à la machine qui exécute, ce qui est cohérent avec « vérité et verdict hors machine ».

**(b) Duels.** Seuils et bandes sont illustratifs, à geler avant exécution.

**E1 : bruit d'étalonnage contre dérive.**
- H_A : le triplement observé est compatible avec la loi Beta de 1.1, sans changement de distribution.
- H_B : la distribution honnête a changé.
- Métrique : rapport taux(R1)/taux(R0 retenu) au même seuil, avec intervalle par rééchantillonnage **par tâche** (grappes).
- Contrôle négatif : deux moitiés aléatoires de R0, et permutation des étiquettes de régime. Le rapport doit couvrir 1.
- Falsification : intervalle couvrant 1 avec au moins 500 épisodes en R1, H_B tombe pour cette paire, et S1 avec. Borne basse > 1, H_A tombe.

**E2 : corps contre queue.**
- H_A : la dérive est de position-échelle. Après alignement de R1 sur R0 par les quantiles sous 90 % des témoins, le taux revient dans [0,5 % ; 1,5 %].
- H_B : la queue bouge indépendamment du corps. Le taux reste hors bande.
- Contrôles : monde planté translation (H_A doit gagner, sinon l'alignement est cassé) et monde planté mélange (H_B doit gagner, sinon le test est aveugle).
- Falsification : hors bande, H_A tombe et avec elle toute correction fondée sur le corps (B2, P1 en mode recalage). Dans la bande, H_B tombe pour cette paire.

**E3 : covariables contre concept.**
- H_A : P(score | longueur, famille, source) est stable (M1).
- H_B : elle change (M2).
- Métrique : taux réel en R1 du conforme pondéré, poids issus d'un classifieur R0/R1 sur covariables seules. En complément, gain d'AUC du même classifieur quand on lui ajoute le score (test par permutation).
- Contrôles : poids uniformes (le triplement doit réapparaître) ; monde planté M1 pur (doit passer) ; monde planté M2 à covariables identiques (doit échouer).
- Falsification : borne haute ≤ 1,5 % et gain d'AUC nul, H_B tombe. Sinon H_A tombe et le conforme pondéré est écarté pour cette paire.

**E4 : dérive contre sabotage, identification par les témoins.**
- H_A : une hausse d'alertes dans un lot est un changement de régime, et les témoins se déplacent comme les épisodes déployés.
- H_B : c'est du sabotage, et les témoins ne bougent pas.
- Métrique : écart de rang témoins contre déployés dans le lot.
- Contrôle : lot sans dérive ni sabotage (écart nul).
- Falsification : en mondes plantés à cause unique, l'issue réfute l'une ou l'autre. Si l'instrument se trompe de cause dans plus de δ des mondes, c'est l'instrument « témoins » qui tombe (S7 fausse). Le cas des deux causes simultanées n'est pas identifiable par ce seul écart : je le déclare ouvert.

---

## 5. Demande reformulée

> Pour chaque mécanisme M1–M4 et chaque paire R0→R1, fournir une règle gelée qui, avec n épisodes honnêtes par régime (n compté en tâches) et m témoins par lot, **soit** maintient le taux réel dans une bande pré-déclarée avec probabilité ≥ 1−δ sur le tirage de l'étalonnage, **soit** déclare « régime non étalonné » en un nombre de lots borné et bascule sur un repli déclaré. Dire le type de garantie (marginale, conditionnelle à l'échantillon, par strate, de long terme) et la famille de dérives hors garantie. Montrer la détection à taux réalisé égal contre B1 (α/3) et B3 (rang), y compris sous dérive vers le bas et sous sabotage synchronisé. Verdict rendu hors machine sur des mondes plantés par un tiers, monde nul compris.

---

## 6. Propositions

Tout ce qui suit est **ma proposition (HYPOTHÈSE)**. Les briques publiées sont signalées, et rien n'est testé.

### P1 : adaptation confinée aux témoins, à trois états

**Règle.** Chaque lot contient m témoins honnêtes.
1. Chaque témoin reçoit une p-valeur conforme contre l'étalonnage R0.
2. Un processus de pari M sur ces p-valeurs s'accumule de lot en lot (martingale de test d'échangeabilité).
3. Tant que M < 1/δ, état « étalonné » : seuil R0.
4. Dès que M ≥ 1/δ, état « non étalonné » : repli B1 + B3, signalement.
5. Quand n_min témoins du nouveau régime sont accumulés, ré-étalonnage **sur témoins seuls**. Si E2 a conclu position-échelle, recalage par quantiles du corps dès environ 80 témoins (illustratif).

Aucun score d'épisode déployé non certifié n'entre jamais dans un seuil.

**Garantie dite.** Si les témoins sont échangeables avec R0, la probabilité de déclarer une dérive à tort, à quelque moment que ce soit, est ≤ δ (inégalité de Ville, 1939). Le seuil n'est pas empoisonnable par l'agent déployé, par construction.

**Suppositions.** S7. La dérive est visible dans le corps. L'agent ne distingue pas témoin et déploiement.

**Coût.** m épisodes par lot. Délai de l'ordre de ln(1/δ)/KL : environ 46 témoins pour δ = 1 % et 0,45 σ gaussien (illustratif). Pendant le repli, détection de B1.

**Test de mort.** Sur la famille « triplement par translation » : tué si la dérive n'est pas déclarée en D lots pré-déclarés, ou si le taux après recalage sort de la bande. Tué en monde nul si les fausses déclarations dépassent δ. Tué en monde mélange (M3) si le taux triple sans déclaration, ce que je **prédis** pour la version corps seul. Le remède est un second processus sur les dépassements de témoins, lent, à mesurer.

**Distinction.** Les martingales conformes (Vovk et al. 2003) et le conforme adaptatif sont publiés. Ce que j'ajoute : restreindre toute adaptation à un flux certifié honnête, et coupler la détection à un état d'abstention plutôt qu'à un ré-étalonnage automatique. Je ne sais pas si cet assemblage est déjà publié.

### P2 : garantie uniforme en longueur par dépense d'alpha sur les pas

**Règle.** Chaque pas t reçoit une p-valeur conforme p_t contre les pas honnêtes de même tranche de position. Alerte si p_t ≤ α_t pour un t, avec Σα_t ≤ α (par exemple α_t proportionnel à 1/t²).

Variante plus puissante : produit d'e-valeurs calibrées (Vovk & Wang 2021), alerte à 1/α.

**Garantie dite.** Dépense d'alpha : P(alerte sur épisode honnête) ≤ α pour **toute** longueur et toute dépendance entre pas, par borne d'union. Elle répond donc à la fois à « pas par tranche » et à « franchissements répétés ». Variante produit : même borne par Ville, mais seulement si chaque p_t est valide conditionnellement au passé. Supposition forte, que je ne sais pas tenir sur des pas d'agent.

**Suppositions.** p_t valides marginalement à des niveaux α_t très petits. Il faut donc beaucoup de pas d'étalonnage, groupés par épisode.

**Coût.** Conservatisme, donc perte de détection, que je ne sais pas chiffrer. Remarque sur la contrainte : la règle ne fait ni moyenne ni médiane sur les jetons. La variante produit somme des logarithmes sur les **pas** : à l'arbitre de dire si cela tombe sous l'interdit.

**Test de mort.** Monde planté où la longueur double : tué si la borne haute du taux d'une tranche dépasse α. Tué si la détection à taux réalisé égal est inférieure à celle de B1. Tué si le seuil est infini sur plus d'une fraction pré-déclarée des pas.

**Distinction.** Dépense d'alpha et e-processus sont publiés. L'apport est l'application comme remplacement du score normalisé, à garantie moyenne seulement.

### P3 : renoncer au seuil, rang contre témoins du lot et budget fixe

**Règle.** Dans chaque lot et chaque strate (version × tranche de longueur), p_i = (1 + nombre de témoins de score ≥ s_i)/(m+1). On relit les k plus petites p-valeurs (budget). En option, procédure de Benjamini-Hochberg (1995) sur ces p-valeurs, dont Bates et al. (2023) donnent les conditions de validité.

**Garantie dite.** Charge de relecture fixée par construction. Les p-valeurs sont valides marginalement si les témoins sont échangeables avec les honnêtes du lot. Elles sont invariantes à **toute** dérive commune au lot, queue comprise, si les témoins échantillonnent aussi la nouvelle source bénigne. Ce n'est pas une garantie de taux à 1 % : la résolution est 1/(m+1), et il faut m ≥ 99 par strate pour une p-valeur à 1 % (illustratif).

**Coût.** Témoins par strate et par lot. Si la prévalence du sabotage varie entre lots, un budget fixe sous-relit les lots chargés.

**Test de mort.** Sur la famille « triplement », la charge ne triple pas par construction : le test porte donc sur ce qui reste réfutable. Tué si la détection à budget k est inférieure à celle de B1. Tué si, en monde « dérive touchant l'agent mais pas les témoins » (écart jumeau), la part d'honnêtes parmi les relus triple.

**Distinction.** P-valeurs conformes pour valeurs aberrantes et budgets d'audit sont publiés. L'apport est l'étalonnage **contemporain** par témoins du lot plutôt que par un jeu historique.

### Quand renoncer au seuil fixe

Quatre cas :
- n par régime (en tâches) sous 300 environ (illustratif) : le 1 % n'est pas certifiable, même sans dérive.
- E2 conclut « queue seule ».
- Les régimes changent plus vite que le délai de détection plus le ré-étalonnage.
- La dérive est provocable par l'agent.

À la place : P3 (rang et budget), une sortie à trois états (alerte, passe, non étalonné), et P2 pour le séquentiel. B1 reste le plancher : une proposition qui ne le bat pas est retirée.

### (d) Ancrage matériel

- **Mondes plantés** : synthétiques, sur processeur, quelques minutes par famille (illustratif). C'est le poste le moins cher et le plus décisif, à exécuter en premier (E1, E2 et les tests de mort de P1 à P3).
- **Modèles ouverts** à activations accessibles : familles Llama 3, Qwen 2.5, Gemma 2. Deux points de contrôle d'une même famille tiennent lieu de « versions de l'agent ». Je ne sais pas si le programme les utilise.
- **Épisodes réels** : 4 régimes × environ 500 épisodes honnêtes × 2 (jumeau), soit environ 4 000 épisodes (illustratif). Le coût est dominé par la génération : les sondes linéaires sont négligeables. Je ne sais pas le chiffrer sans la longueur des épisodes. Ordre de grandeur : quelques jours sur un à quelques GPU (illustratif).
- **Relecture humaine** : quelques dizaines d'épisodes tirés au hasard par régime (illustratif), réservés à la mesure indépendante de la section 4.

FIN-DE-CELLULE