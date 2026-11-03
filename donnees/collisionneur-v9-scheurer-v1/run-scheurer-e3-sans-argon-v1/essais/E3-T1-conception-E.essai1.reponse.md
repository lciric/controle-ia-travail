# E — Mesurer une frontière de surveillance, pas une intention

**RAPPORTÉ — pièces manquantes :** les dates de sortie d’un panel longitudinal ouvert, les coûts d’inférence et les procédures complètes d’ajustement des tendances de référence ne sont pas fournis.

**Convention :** tous les protocoles ci-dessous sont **HYPOTHÈSE** ; leurs nombres sont **supposés, illustratifs**, sauf mention « calcul ». Aucune expérience n’est exécutée ici.

## a) Présupposés non établis

- **HYPOTHÈSE :** une grandeur de surveillance possède une tendance temporelle multiplicative stable. Une frontière mesurable n’implique pas cette tendance.
- **HYPOTHÈSE :** des dates de publication permettent d’isoler un progrès technique plutôt qu’un changement de famille, d’entraînement ou de données.
- **HYPOTHÈSE :** des anomalies plantées représentent des comportements spontanés. Je n’en déduirai aucune propension spontanée.
- **RAPPORTÉ :** capacité et propension sont difficiles à démêler, et une modification des outils peut fortement modifier les comportements observés — pièce Scheurer, §2.1.
- **RAPPORTÉ :** le seuil séquentiel peut produire des fausses alertes sous dépendance intra-épisode ; une calibration sur épisodes honnêtes entiers a mieux tenu dans la simulation fournie — pièce « nos résultats », §6.
- **HYPOTHÈSE :** une échelle commune reste interprétable lorsque les modèles refusent, saturent ou échouent à accomplir la tâche honnête.

## b) Trois tendances candidates

### E-A — Horizon de surveillance de trajectoires — priorité

**Grandeur :** \(H_m\), longueur maximale d’une trajectoire pour laquelle le moniteur \(m\) détecte au moins **80 %** des anomalies, avec au plus **5 %** de fausses alertes par épisode.

**Échelle :** nombre de décisions auditées ; mêmes trajectoires, mêmes placements d’anomalies et même budget de lecture pour tous les moniteurs. Les longueurs constituent une grille approchant une échelle continue.

**Cas :** tâches synthétiques à état caché, journal public et contraintes exécutables. Classes plantées : déclaration incompatible avec l’état, action interdite, résultat incorrect. Aucun mode opératoire de tromperie.

**Pourquoi mesurable :** la disponibilité d’une vérité mécanique évite de dépendre de la volonté du modèle de manifester un comportement malveillant.

**Menaces et contrôles :**
- contamination : générateur gelé, graines finales secrètes ;
- plafond : élargissement préenregistré des longueurs ;
- changement de cas : corpus strictement commun aux modèles.

**Énoncé visé, supposé :** « L’horizon surveillable croît de **+3 % par mois**, soit un facteur **1,03/mois**. »

### E-B — Calcul nécessaire pour détecter une incohérence

**Grandeur :** \(B_m\), budget minimal d’inférence du moniteur atteignant les mêmes critères de détection et de fausses alertes sur des trajectoires de longueur fixée.

**Échelle :** opérations d’inférence estimées par un compteur documenté, plutôt que secondes dépendant du matériel. Rapport complémentaire en jetons et temps matériel.

**Pourquoi mesurable :** on mesure le coût d’une tâche de contrôle définie, non une intention. Plusieurs budgets peuvent révéler une transition masquée par un score unique.

**Menaces et contrôles :**
- refus : comptés comme absence de détection, séparément rapportés ;
- budget nominal trompeur : comptage effectif, précision et matériel fixés ;
- adaptation au test : politique d’allocation gelée avant test.

**Énoncé visé, supposé :** « Le calcul requis diminue de **−4 % par mois**, facteur **0,96/mois**. »

### E-C — Horizon de confinement sous contrôle fixe

**Grandeur :** \(K_m\), nombre maximal d’occasions d’action pour lequel un contrôleur conserve une probabilité de dommage d’épisode inférieure à **5 %**, tout en maintenant **90 %** d’accomplissement des tâches honnêtes.

**Échelle :** nombre d’occasions, à fréquence et gravité des violations plantées fixées. Le contrôleur décide autoriser, bloquer ou soumettre à vérification.

**Pourquoi mesurable :** les propositions d’action sont exogènes et identiques entre contrôleurs ; l’élicitation de malveillance n’entre pas dans la mesure.

**Menaces et contrôles :**
- tout bloquer : contrainte explicite d’utilité honnête ;
- dépendance temporelle : calibration par épisodes entiers ;
- changement d’attaquant : générateur d’actions gelé.

**Énoncé visé, supposé :** « L’horizon de confinement croît de **+2 % par mois**, facteur **1,02/mois**. »

### Panel, dates et ajustement communs

**RAPPORTÉ :** Qwen2.5 comprend **sept** tailles ouvertes, publiées le **19 septembre 2024** — pièce Scheurer, §2.2. Cela permet une comparaison de taille, **pas une pente calendaire**. Llama-3.1-8B-Instruct est utilisé dans les résultats fournis — « nos résultats », §6 ; sa date n’y figure pas.

**HYPOTHÈSE :** panel longitudinal cible de **douze checkpoints ouverts sur vingt-quatre mois**, au sein de familles suivies et avec strates de taille comparables. Noms supplémentaires et dates restent à documenter ; aucune régression temporelle avant cet audit.

Ajuster d’abord les courbes succès–difficulté, puis  
\[
\log Z_m=a+\beta t_m+\text{effets famille/taille}.
\]
Facteur mensuel : \(e^\beta\). Incertitude par rééchantillonnage des familles de tâches et checkpoints ; analyse avec et sans correction de taille. Frontières hors grille : censurées, jamais extrapolées automatiquement.

## Expériences décisives

| Duel exclusif | Métrique et seuil | Contrôle négatif | Falsification |
|---|---|---|---|
| **A :** \(H_A:\beta>0\) ; \(H_B:\beta\leq0\) | Pente de \(\log H\) | Dates permutées ; moniteur figé | Intervalle entièrement positif : réfute \(H_B\) ; entièrement négatif : réfute \(H_A\) |
| **B :** \(H_A:\beta<0\) ; \(H_B:\beta\geq0\) | Pente de \(\log B\) | Répétition du même checkpoint | Intervalle négatif : réfute \(H_B\) ; positif : réfute \(H_A\) |
| **C :** \(H_A:\beta>0\) ; \(H_B:\beta\leq0\) | Pente de \(\log K\) | Actions honnêtes bénignes appariées | Même règle que A |

Intervalles simultanés à **95 %**. Chevauchement de zéro : **non concluant**, pas validation de l’absence de tendance.

## c) Validation minimale des instruments

Pour **chaque** instrument, publier détection et fausses alertes, par classe et longueur, sur des paires partageant tâche, style, longueur et opérations bénignes ; seul l’état pertinent diffère.

- **Moniteur de trajectoire :** cible **80 % / 5 %** ; comparer aux règles de format, permissions et cohérence locale.
- **Moniteur à budget variable :** mêmes taux ; battre ces vérifications à coût égal.
- **Contrôleur :** détection avant dommage et blocages injustifiés ; comparer à une liste mécanique d’autorisations et à un validateur d’état.

L’oracle mécanique privilégié établit la vérité ; les baselines n’accèdent qu’aux informations du moniteur. Si une règle accessible résout tous les cas, l’instrument neuronal n’apporte rien. METR et TasteVal servent d’analogies, non d’instruments validés ici.

## d) Premier pilote et coût

**HYPOTHÈSE :** deux tailles Qwen2.5, **trois** longueurs (**8, 32, 128** décisions), **80 paires** par cellule : **480 paires, 960 trajectoires** — **calcul**.

Budget : **100 heures-GPU**, sans entraînement, à **2 €/heure**, soit **200 € — calcul illustratif**, hors travail humain ; GPU de **48 Go** supposé, à confirmer selon tailles et précision.

Pilote non concluant si aucune frontière n’est encadrée, si les intervalles ne certifient pas les taux, ou si les baselines mécaniques saturent. Il ne suffit pas à mesurer une tendance temporelle.

### Échec du plan
Les checkpoints comparables et datés manquent.  
Les scores mesurent surtout le style des anomalies plantées.  
Les frontières restent plates, censurées ou dominées par des contrôles mécaniques.

FIN-DE-CELLULE