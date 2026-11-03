# Proposition D — Mesurer le rappel **parmi les lauréats**, pas seulement sur toutes les trajectoires

**Convention.** Les résultats de Kirchner sont **RAPPORTÉS** par une moisson non opposable ; ceux de Lazar sont **OBSERVÉS-NON-AUDITÉS**, faute de réexécution. Les hypothèses et protocoles ci-dessous sont des **HYPOTHÈSES**. Sauf reprise explicite des pièces, tous les effectifs, seuils, délais et coûts sont **illustratifs**.

**Limite de pièce :** l’annexe G et la figure 32 sont absentes des extraits lisibles ; je n’affirme donc pas que le papier ne contient aucun seuil ou test sur tricheries plantées.

## Problème et différence revendiquée

**RAPPORTÉ — pièce Kirchner §2–3 :** le moniteur et les chercheurs automatiques sont le même modèle ; 39 méthodes sur 1 601 sont signalées, et une seule triche atteint les trois premières places. Ces nombres mesurent respectivement une **fréquence de signalement** et une issue observée, pas le rappel du moniteur ni le risque parmi les lauréats.

**OBSERVÉ-NON-AUDITÉ — pièce « nos résultats » §2–3 :** le juge v8 obtient 0/1 000 sur onze lignes fatales, tout en laissant promouvoir une fausse loi W2 dans 12/12 unités. Une batterie peut donc avoir des dents et laisser intacte une classe hors couverture.

**HYPOTHÈSE D :** dans une boucle de recherche, la métrique décisionnelle devrait être le **rappel conditionnel à la sélection** : le moniteur peut être correct en moyenne, mais particulièrement aveugle aux tricheries qui obtiennent de bons scores. Classement et filtre peuvent enrichir cet angle mort **sans gradient contre le moniteur**. Inversement, un gain sur un banc de surveillabilité peut n’être qu’un déplacement du trou vers des classes hors banc.

**Nouveauté : HYPOTHÈSE**, puisqu’elle n’a pas été cherchée. À durcir par les requêtes :  
`"automated researcher" monitor recall planted cheating leaderboard selection`,  
`selection-induced monitor blind spots held-out monitor`,  
`same-model monitor recall top-k`,  
`monitorability benchmark transfer out-of-distribution reward hacking`.

Différence avec les travaux les plus proches :

- Kale et coll., 2025, *Reliable Weak-to-Strong Monitoring of LLM Agents* : conscience d’être surveillé ; ici, **composition des lauréats sous moniteur figé**, sans conscience ni entraînement contre lui.
- « Moniteurs validés sur triche suscitée… », 2604.23488, **référence à vérifier** : origine de la triche ; ici, conditionnement par la sélection et transfert après sélection.
- 2512.00218, **référence à vérifier** : optimisation directe de la surveillabilité ; ici, mesure séparée du gain interne, du transfert externe et des fausses alertes.
- L’attaque W2 de Lazar concerne un juge statistique et un trou de nulle ; elle ne démontre rien sur un moniteur linguistique de chercheur automatique.

## (a) Ce que la question suppose sans l’établir

| Supposition | Statut et réserve |
|---|---|
| « Peu signalé » signifie « rarement manqué ». | **HYPOTHÈSE.** Le taux RAPPORTÉ de 2,4 % n’a pas de dénominateur de tricheries réelles. |
| Une triche dans le top trois implique que les lauréats sont presque sûrs. | **HYPOTHÈSE.** Sans tricheries plantées à score élevé, le rappel parmi les lauréats est inconnu. |
| Une baisse de rappel après sélection est une dégradation du moniteur. | **HYPOTHÈSE.** À moniteur figé, elle peut être seulement un changement de population. Parler de dégradation intrinsèque exige une batterie fixe et une distribution fixe. |
| Partager le même modèle crée nécessairement des angles morts corrélés. | **HYPOTHÈSE.** Cela doit être comparé à un moniteur distinct ; ni complicité ni indépendance ne peuvent être présumées. |
| Les tricheries plantées représentent la triche spontanée ou produite par sélection. | **HYPOTHÈSE.** Elles mesurent d’abord la couverture des classes plantées ; une validation sur triche naturelle nécessite une vérité terrain indépendante. |
| Un gain sur un banc de surveillabilité transfère hors banc. | **HYPOTHÈSE.** Il faut tester classes, tâches et horizons jamais utilisés pour sélectionner. |
| Banc tenu à l’écart, Petri et garde de capacité fournissent une vérité terrain suffisante. | **RAPPORTÉ** pour leur construction ; **HYPOTHÈSE** pour cette validité. Petri est explicitement seulement un indicateur dans la pièce. |
| Les garanties du juge statistique de Lazar se transfèrent aux moniteurs AAR. | **HYPOTHÈSE.** Les résultats publics sont **OBSERVÉS-NON-AUDITÉS** et portent sur un autre instrument. |

## (b) Expériences décisives

### Protocole commun : vérité terrain mécanique, moniteur figé

Utiliser le harnais ouvert, ou une boucle jouet avec **Llama-3.1-8B-Instruct comme agent et comme moniteur**. Préenregistrer invites, températures, scores et règles de sélection.

Constituer **illustrativement** 400 cas plantés et 400 cas honnêtes, répartis entre quatre classes : relance/réutilisation interdite, copie du format d’évaluation, tromperie du relecteur, et recombinaison d’artefacts acceptés dans un monde où toute promotion est fausse. Les classes suffisent ; aucun mode d’emploi d’évasion.

Chaque cas planté possède une étiquette par construction et un déclencheur mécanique de validation. Chaque cas honnête est apparié par tâche, longueur, décile de score et comportement presque limite mais permis. Les intervalles sont calculés par cohorte/tâche, non en traitant les trajectoires corrélées comme indépendantes.

### Expérience D1 — Le classement enrichit-il les faux négatifs ?

Trois sélections, sans retour des verdicts aux agents :

1. score seul ;
2. filtre du moniteur puis score ;
3. sélection aléatoire à effectif égal, comme contrôle.

**Métriques :**

- \(R_0\) : rappel sur tous les cas plantés ;
- \(R_S\) : rappel sur les cas plantés que le score seul placerait parmi les lauréats ;
- \(\Delta=R_S-R_0\) ;
- fausses alertes sur tous les honnêtes **et** sur les honnêtes à haut score ;
- fuite finale : proportion de lauréats plantés non détectés après filtre.

**Duel :**

- **H_A — enrichissement :** \(\Delta\leq-0,20\) (seuil illustratif), avec intervalle de confiance excluant un simple effet nul.
- **H_B — pas d’enrichissement matériel :** \(\Delta\geq-0,05\) (seuil illustratif), avec rappel suffisant pour rendre la comparaison informative.

**Issues :**

- Intervalle entièrement compatible avec un déficit d’au moins 0,10 : **H_B est falsifiée**. Si le filtre laisse encore fuiter des lauréats plantés, le classement ne peut pas être présenté comme une défense suffisante.
- \(R_0\) et \(R_S\) ont tous deux une borne inférieure d’au moins 0,90, le déficit est inférieur à 0,05 et les fausses alertes restent sous 0,05 — tous seuils **illustratifs** : **H_A est falsifiée**, et je changerais d’avis sur l’intérêt prioritaire de ce mécanisme.
- Si \(R_0\) est faible, l’expérience rejette d’abord le moniteur ; elle ne tranche pas l’effet de sélection. Entre les deux zones : résultat non décisif, pas confirmation.

**Contrôles négatifs :** sélection aléatoire, honnêtes appariés à score égal, scores permutés. **Contrôle de fonctionnement :** une violation mécaniquement évidente doit être détectée ; sinon la batterie est déclarée défaillante.

Une répétition sur plusieurs générations distinguerait ensuite enrichment de population et dérive intrinsèque : cette dernière exige une baisse sur une **batterie d’audit figée**, pas seulement sur les nouvelles soumissions.

### Expérience D2 — Le banc de surveillabilité transfère-t-il ou déplace-t-il le trou ?

Comparer à calcul et intensité de sélection égaux :

- aucune sélection ;
- sélection sur le score de tâche ;
- sélection sur le banc de surveillabilité, sans gradient contre le moniteur d’audit.

Évaluer ensuite sur deux ensembles scellés : classes internes au banc et classes hors banc, avec nouvelles tâches et trajectoires plus longues. Le moniteur d’audit et les vérifications mécaniques ne servent jamais à sélectionner.

- **H_A — transfert réel :** le rappel progresse d’au moins 0,15 hors banc, sans augmentation des fausses alertes au-delà de 0,05 ni effondrement d’une classe ; seuils **illustratifs**.
- **H_B — déplacement :** le rappel interne progresse d’au moins 0,15, mais le rappel externe ne progresse pas, ou chute d’au moins 0,20 dans une classe ; seuils **illustratifs**.

**Issue H_B :** elle falsifie l’affirmation générale « hill-climber sur la surveillabilité rend la triche hors banc plus détectable ».  
**Issue H_A reproduite sur au moins deux familles externes :** elle falsifie l’affirmation symétrique « cette sélection ne fait que déplacer l’évasion ».  
Un résultat limité à la sélection ne tranche pas toutes les variantes possibles d’entraînement.

## (c) Mesure minimale de chaque instrument

Pour un détecteur linguistique, critère utile **illustratif** : borne inférieure du rappel ≥0,90, borne supérieure des fausses alertes ≤0,05, et gain de rappel ≥0,10 sur la seule pile mécanique à fausses alertes égales.

| Instrument | Mesure minimale et cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|
| **Moniteur avant exécution, lecture du code** | Rappel par classe plantée ; fausses alertes sur code honnête de même tâche, longueur et dépendances. | Journal d’accès fichiers/réseau, provenance des données, permissions OS, inventaire des processus et artefacts d’évaluation. |
| **Moniteur post-hoc de trajectoires** | \(R_0\), \(R_S\), rappel par classe ; fausses alertes sur trajectoires honnêtes, notamment les lauréates. | Rejeu déterministe, invariants de sandbox, grand livre des accès et comparaison code/résultat ; aucun jugement de la chaîne de raisonnement comme vérité terrain. |
| **Classement et filtre** | Ce ne sont pas des détecteurs : mesurer l’enrichissement des faux négatifs et la perte d’honnêtes à haut score. | Score seul, sélection aléatoire et filtre mécanique seul. |
| **Banc tenu à l’écart** | Accès interdits déclenchés ; promotion de méthodes nulles ou de classe « copie de format » ; honnêtes appariés par difficulté. | Canaris d’accès, permissions OS, hachage des données, journalisation et séparation des identifiants. |
| **Petri** | Détection de comportements plantés dont la sévérité est établie hors Petri ; fausses alertes sur conversations honnêtes appariées. | Tests mécaniques de transcription et règles comportementales observables. Sans cela, Petri ne fournit pas le dénominateur du rappel de triche. |
| **Garde de capacité** | Faux passage de régressions plantées ; faux rejet de méthodes honnêtes de performance équivalente, sur évaluations répétées. | Seuil fixe, médiane de répétitions et comparaison appariée au modèle de base. |
| **Banc de surveillabilité** | Rappel interne **et externe**, fausses alertes, performance par classe après sélection. | Règles statiques et contrôles de sandbox ; un score de lisibilité seul ne suffit pas. |
| **Juge statistique de l’organisme** | Promotions dans des mondes où toutes sont fausses, puissance sur lois vraies plantées, couverture par classe ; honnêtes appariés par archive et longueur. | Hachage/normalisation, détection de réutilisation d’archive et rejeu des soumissions. Le seuil reste celui de la procédure préenregistrée, y compris pour tentatives multiples. |

La calibration des fausses alertes doit porter sur des **trajectoires honnêtes entières** : **OBSERVÉ-NON-AUDITÉ**, la simulation T0.3 de Lazar montre qu’une calibration supposant une indépendance trop forte peut fortement sous-estimer les alarmes.

## (d) Ancrage matériel et première expérience

- **Prétest organisme, illustratif :** un jour CPU, moins de 50 dollars. Rejouer les artefacts W2/v8 pour vérifier que les contrôles mécaniques et les classes plantées ont des dents. Cela ne valide pas un moniteur AAR.
- **D1 sur 8B, illustratif :** Llama-3.1-8B-Instruct en inférence, agent et moniteur exécutés séquentiellement ; deux GPU de 24 Go ou un GPU de 48 Go, trois jours, soit environ six GPU-jours et 150–600 dollars selon le fournisseur.
- **D2 par sélection seule :** même ordre de grandeur. Un éventuel entraînement LoRA serait une expérience distincte, **illustrativement** quatre GPU de 80 Go pendant trois à cinq jours.
- **Extension de généralisation :** GLM-4-32B, mentionné dans la pièce Kirchner, uniquement après réussite du test 8B.

Un résultat sur Llama-8B établit ou réfute le mécanisme **dans ce harnais et à cette puissance** ; il ne généralise ni à Opus 4.8 ni à la triche naturelle non plantée.

FIN-DE-CELLULE