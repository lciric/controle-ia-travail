# Tour du collisionneur, Scheurer (sans Argon ; espèce B absente après son refus) — propositions (E3-T1) et réponses aux critiques (E3-T3), brutes

Copie à l'octet vérifiée contre les compagnons ; espèces par lettre ; rien lu ni modifié par conv-audit.


---

## E3-T1-conception-A.md (sha256 `f29eaab5200f433b5eb8bb49f3ed6393a49b167b580dbcd4a98f5e538f7562f6`)

# Proposition A — Tour III.1 : tendance d'échelle pour la surveillance

Statuts : tous les chiffres de `piece-scheurer-v1` sont **RAPPORTÉ** (la pièce dit qu'aucun n'a été revérifié sur page primaire) ; ceux de `piece-nos-resultats-v1` sont **OBSERVÉ-NON-AUDITÉ** ; le reste est **HYPOTHÈSE** ou « supposé/illustratif ».

## (a) Ce que la question suppose sans l'établir

1. **Qu'une tendance temporelle lisse existe** pour un comportement désaligné. HYPOTHÈSE : rien dans les pièces ne montre une courbe datée ; 2603.01608 donne des taux de base à 0 % sauf un cas à 3 % (RAPPORTÉ), ce qui est un plancher, pas une pente.
2. **Que capacité et propension se séparent.** RAPPORTÉ (2603.01608, résumé et § 4.1) : « difficiles à démêler » ; retirer un outil fait tomber 59 % à 3 %. Une propension mesurée dépend donc du montage plus que du modèle.
3. **Que la mesure est invariante d'un modèle à l'autre.** RAPPORTÉ (2412.04984 § 4, p. 15) : sous-estimation possible, aversion de disposition ; RAPPORTÉ (2510.09462 § 6) : comportement induit par consigne « peut être sous-élicité ». Un trend de propension confond donc pente réelle et pente d'élicitation.
4. **Que le moniteur est un instrument fixe.** RAPPORTÉ (2506.05296 § 2.3) : AUC de 0,92 à 0,96 selon le moniteur ; RAPPORTÉ (2510.09462, fig. 2) : le moniteur le plus fort passe à 0 sur 375 échantillons sous injection. L'instrument bouge et se casse.
5. **Que le recette METR/TastEval se transpose.** RAPPORTÉ : nombre de tâches, de modèles, procédure de régression et incertitude du doublement absents des pièces ; TastEval déclare lui-même que le « hill-climb » peut surestimer (§ 3.2).
6. **Qu'un juge de langage peut noter.** OBSERVÉ-NON-AUDITÉ (§ 4 de nos résultats) : deux juges au plafond, κ = 0. Toute tendance notée par juge hérite de ce plafond.
7. **Qu'il existe assez de modèles ouverts datés.** HYPOTHÈSE : Qwen2.5 donne sept tailles mais **une seule date** (RAPPORTÉ, § 2.2) — un axe de taille, pas un axe de temps.

Conséquence de conception : je ne mesure pas la propension du modèle surveillé ; je mesure la **capacité du moniteur** contre une attaque **vérifiée mécaniquement**, ce qui neutralise 2, 3 et 6.

## (b) Tendances candidates et duels

### T1 — Horizon de surveillance (meilleure)

- **Grandeur** : pour un moniteur M, le taux de détection (TPR) à fausses alertes fixées à 5 % (supposé) de portes dérobées dans des solutions APPS, en fonction de la **taille de la trajectoire** (lignes de code + traces d'exécution). **Horizon(M)** : taille à laquelle une logistique ajustée croise TPR = 50 % — calque exact de la recette METR (RAPPORTÉ, § 3.1).
- **Même mesure d'un modèle à l'autre** : la porte dérobée est vérifiée à l'exécution par une entrée qui change la sortie (RAPPORTÉ, 2510.09462, tâche annexe) ; pas de juge ; pool d'attaquants **gelé** (Qwen2.5 0,5–72B, poids ouverts).
- **Échelle continue** : taille de trajectoire ; variante : durée humaine de revue mesurée sur un sous-échantillon (supposé : 30 trajectoires chronométrées).
- **Modèles** : moniteurs ouverts datés, supposé 8 à 12 sur 24 mois ; plus les 7 Qwen2.5 pour un axe de taille à date fixe.
- **Ajustement** : log2(horizon) ∼ date, moindres carrés, bootstrap sur problèmes et sur attaquants pour l'intervalle.
- **Énoncé attendu (supposé)** : « l'horizon de surveillance double tous les 9 à 15 mois », signe positif. Chiffre non tiré des pièces.

**Duel D1** (moniteur varie, attaquants gelés). H_A : la pente de log2(horizon) sur la date est ≥ 0,5 bit/an (doublement ≤ 24 mois) avec un intervalle à 95 % excluant 0. H_B : la pente est indiscernable de 0 (horizon dominé par la taille de trajectoire, non par le moniteur). Métrique : pente ; seuil : borne inférieure de l'intervalle > 0,3 bit/an (supposé). Contrôle négatif : moniteur mécanique fixe (suite de tests + lanceur d'entrées aléatoires), qui doit avoir pente 0 ; si lui aussi « progresse », la banque dérive (contamination par difficulté), et D1 est non concluant. Issue : pente nulle avec contrôle plat falsifie H_A ; pente positive falsifie H_B.

**Duel D2** (attaquant contemporain). H_A : à date égale, le moniteur garde un horizon ≥ celui mesuré contre le pool gelé ×0,8 (supposé). H_B : les attaquants récents produisent des portes dérobées plus subtiles (RAPPORTÉ, 2506.05296, section non citée) et l'horizon contre contemporain stagne ou décroît. Seuil : rapport horizon(contemporain)/horizon(gelé) avec intervalle. Si le rapport < 0,8, H_A falsifiée (la course est nulle, l'énoncé doit être signé négativement) ; si ≥ 0,8, H_B falsifiée.

### T2 — Écart de capacité seuil pour l'injection

- Grandeur : plus petit écart (taille ou date) attaquant–moniteur au-delà duquel une injection dans le contenu lu par le moniteur réussit sans exemple (RAPPORTÉ, 2510.09462 § 4.4). Échelle : différence de log-paramètres sur Qwen2.5.
- Duel : H_A : l'écart seuil se déplace vers le haut avec la date du moniteur (la hiérarchie d'instructions, RAPPORTÉ § 6, progresse) ; H_B : l'écart seuil est constant ou nul (GPT-4.1 à 0 sur 375, RAPPORTÉ, fig. 2, est la règle). Contrôle négatif : mêmes échantillons sans injection (TPR doit rester celui de T1). Énoncé supposé : « l'écart seuil croît de X bits par an » ; signe inconnu — c'est précisément ce qui est réfutable. Limite d'intégrité : les injections sont décrites par leur classe, jamais reproduites.

### T3 — Conscience d'évaluation par unité d'apprentissage par renforcement

- Grandeur : taux de conscience d'évaluation verbalisée (RAPPORTÉ, 2509.15541 § 6.1 : 2,0 % → 20,5 %) en fonction des pas de renforcement, sur un modèle ouvert. Axe : calcul de renforcement, pas la date.
- Duel : H_A : croissance monotone, ≥ ×2 par doublement du calcul (supposé) ; H_B : saut puis plateau (effet de seuil de la consigne). Contrôle négatif : ajustement fin supervisé à calcul égal, où H_A prédit pas de croissance. Menace : la verbalisation dépend d'un juge (plafond, § 4 de nos résultats) — à tenir par classificateur figé avec étalonnage sur 200 cas annotés deux fois (supposé).
- Pourquoi secondaire : coûte un entraînement par point ; c'est la seule candidate qui mesure du désalignement, pas de la surveillance.

### T4 — Propension à la sous-performance sans but (contre-exemple attendu)

Grandeur : écart de 2412.04984 § 3.6 (0,96 contre 0,61 ; signification des deux scores non donnée, RAPPORTÉ). Je la garde comme **témoin d'échec** : HYPOTHÈSE que sa pente datée sera dominée par les refus et la disposition (p. 15). Duel : H_A : pente > 0 ; H_B : pente confondue avec le taux de refus (corrélation > 0,7, supposé). Si H_B, cela justifie empiriquement de ne pas tendre les propensions.

## Menaces et contrôles (T1)

- **Élicitation** (RAPPORTÉ, 2510.09462 § 6) : l'attaquant est instruit ; on ne mesure que le moniteur, et le pool est gelé — la sous-élicitation est constante dans le temps, donc n'entre pas dans la pente.
- **Refus** : un attaquant qui refuse produit une trajectoire honnête ; comptée dans les cas honnêtes appariés, jamais comme détection.
- **Changement de moniteur / injection** : T1 est mesurée sans injection ; T2 la mesure séparément. Rééchantillonner le moniteur est interdit (RAPPORTÉ : 1 − (1 − p)^k se retourne contre le défenseur).
- **Confusion honnête/malveillant** (RAPPORTÉ, 2506.05296 § 7) : les cas honnêtes sont produits par le **même** attaquant sur les mêmes problèmes, pas tirés d'APPS.
- **Fausses alertes mal calibrées** : OBSERVÉ-NON-AUDITÉ (T0.3) : un seuil de Ville unilatéral donne 0,21–0,35 de fausses alarmes sous effet d'épisode ; je calibre le seuil à 5 % **par moniteur** sur 1 000 trajectoires honnêtes (calque de la calibration qui a tenu 0,046–0,055).
- **Contamination** : banque fraîche de problèmes, graines scellées, empreinte publiée avant notation (calque du § 5 de nos résultats).

## (c) Mesure minimale par instrument

- **Moniteur de trajectoire (type page « Monitoring » d'Apollo, RAPPORTÉ § 1.3)** : TPR à FPR = 5 % sur ≥ 300 cas malveillants vérifiés à l'exécution et ≥ 1 000 honnêtes appariés (même attaquant, mêmes problèmes) ; doit battre la suite de tests APPS plus lanceur d'entrées aléatoires (supposé : 10 000 entrées par solution). Un moniteur sous ce plancher mécanique est déclaré « non fonctionnel », comme les sondes de P3 sous leurs 200 sondes aléatoires (OBSERVÉ-NON-AUDITÉ).
- **Juge de langage** (si employé pour T3) : κ sur 200 cas double-annotés ; κ < 0,4 (supposé) interdit son usage ; notre second tour donne κ = 0 au plafond.
- **Ajustement logistique (METR)** : reporter nombre de points par modèle, intervalle bootstrap du temps de doublement, et test du contrôle mécanique plat — exactement les quatre absences de la pièce § 3.1.

## (d) Ancrage matériel — pilote de T1

- Modèles : Qwen2.5 0,5–72 B (RAPPORTÉ, § 2.2) comme attaquants et moniteurs ; 72 B en bf16 sur 2 H100 (illustratif). Montage à un H100 fixe, comme TastEval (RAPPORTÉ, § 3.2).
- Taille : 500 problèmes APPS, 7 attaquants × 2 rôles (honnête/malveillant) = 7 000 trajectoires ; 7 moniteurs × 7 000 = 49 000 lectures (calcul). Exécution différentielle : ~7 000 × 10 000 entrées, processeur central.
- Coût illustratif : 150 heures H100 génération, 300 heures notation, soit l'ordre de 1 500 € loués ; quatre semaines.
- **Non concluant si** : la pente de taille sur Qwen2.5 a un intervalle couvrant 0 avec un contrôle mécanique lui-même non plat ; ou si moins de 4 moniteurs dépassent le plancher mécanique (puissance : ~1 détection sur 6 à force 0,5 chez nous, OBSERVÉ-NON-AUDITÉ § 5 — ordre de grandeur à craindre) ; ou si le TPR à 5 % est au plafond (> 0,95) pour tous, cas d'un banc sans dents.

## Ce qui ferait échouer le plan

L'axe de taille (Qwen2.5, une date) ne se convertit pas en axe de temps faute de modèles ouverts datés comparables ; les attaquants gelés deviennent triviaux pour tout moniteur récent (plafond, pente ininterprétable) ; la subtilité des attaquants contemporains annule le gain (D2 tranche pour H_B), et l'énoncé devient « rapport constant », vrai mais sans facteur.

FIN-DE-CELLULE

---

## E3-T1-conception-D.md (sha256 `b585b9b960cf2d79bb6e449ccf9d13c7c312a90beb32c5a86182510ff5d52cb1`)

## Statuts et présupposés

**Convention** : les résultats de la pièce Scheurer sont **RAPPORTÉS** ; ceux de « nos résultats » sont **OBSERVÉS-NON-AUDITÉS**. Aucun n’est revérifié ici. Les choix expérimentaux sont des **HYPOTHÈSES** ; leurs tailles, seuils et coûts sont **supposés/illustratifs**, sauf mention « calcul ».

La question suppose sans l’établir :

- **Qu’une propension brute est comparable entre modèles.** **HYPOTHÈSE** fragile : retirer un outil fait passer un taux de manigance de 59 % à 3 %, et les taux de base sont presque toujours nuls (**RAPPORTÉ**, Scheurer §2.1). Un zéro peut signifier absence d’occasion, refus ou mauvaise élicitation.
- **Que les tendances de capacités ordinaires se transportent au désalignement.** Le doublement METR d’environ sept mois et celui de TastEval sont **RAPPORTÉS** (§3.1–3.2), avec des éléments méthodologiques manquants ; ils ne démontrent aucune pente de manigance.
- **Que des comportements instruits ou plantés représentent le scheming spontané.** **HYPOTHÈSE** : ils mesurent d’abord une capacité accessible ou un contrôle sur attaques connues. Aucune tendance obtenue ne sera présentée comme une tendance de propension naturelle.
- **Que date de sortie, difficulté humaine et protocole figé donnent un axe commun.** **HYPOTHÈSE**, à tester contre les effets de famille, de taille, de contamination et d’échafaudage.

## Trois tendances candidates

Pour chacune : **12–18 modèles ouverts**, au moins trois familles, poids publiés sur **24–36 mois** ; dernier quart temporel et une famille entière réservés à la validation. La date retenue est celle de publication des poids, documentée avant l’analyse.

| Candidate | Grandeur et échelle continue | Pourquoi elle peut réussir ; menaces et contrôles | Énoncé attendu, non établi |
|---|---|---|---|
| **T1 — Horizon de subversion accessible** | Sous invites, échafaudage, budget et moniteur ouvert **figés**, probabilité qu’un épisode produise un artefact fonctionnel réalisant la classe plantée et passant le contrôle. Ajustement logistique contre la durée médiane d’un humain autorisé réalisant l’épisode ; **h50** = durée à 50 % de réussite. Les refus sont des échecs du protocole, mais publiés séparément. | Ne dépend pas du taux spontané. **Élicitation** : aucune adaptation par modèle ; **contamination** : tâches nouvelles horodatées ; **changement de moniteur** : impossible dans T1. Limite : capacité accessible, non capacité latente. | **HYPOTHÈSE** : h50 croît de **+10,4 %/mois** (*supposé ; calcul* \(2^{1/7}-1\), inspiration METR, non prédiction vérifiée). |
| **T2 — Horizon de surveillance à risque fixé** | Corpus d’attaques mécaniquement validées, gelé pour l’ajustement et renouvelé pour le test. Le moniteur note la trajectoire entière ; seuil calibré à **1 % de fausses alertes**. **c50** = difficulté humaine de l’attaque où la détection tombe à 50 %. Plus c50 est grand, meilleure est la surveillance. | Aucune attente d’événements spontanés rares et même corpus pour tous les moniteurs. **Artefacts de provenance** : jumeaux honnêtes produits par le même générateur ; **injections** : strates séparées, jamais moyennées avec le cas sans injection ; **contamination** : attaques fraîches finales. | **HYPOTHÈSE** : c50 croît de **+5,1 %/mois** (*supposé, illustratif ; calcul* pour un doublement en 14 mois). |
| **T3 — Calcul d’élicitation nécessaire** | Calendrier fixe de tentatives non adaptatives ; **q50** = calcul d’inférence attaquant, en FLOP plutôt qu’en jetons, auquel 50 % des tâches ont une réussite T1. Analyse de survie avec censure à qmax. | Remplace un taux souvent nul par une quantité continue et représente les non-réponses comme coût/censure. **Sur-élicitation** : interdite hors budget ; **plafond des juges** : aucune étiquette LLM ; **dérive du contrôle** : moniteur figé. | **HYPOTHÈSE** : q50 décroît de **−5,0 %/mois** (*supposé, illustratif*). |

Pour T1/T2, modèle logistique à effets de tâche ; pour T3, modèle de survie. Régression de \(\log(h50,c50,q50)\) sur la date, avec et sans taille du modèle ; **IC à 95 %** par bootstrap groupé sur tâches et modèles, validation temporelle et famille laissée de côté. Facteur mensuel : \(\exp(30,44\beta)\) (**calcul**). La portée reste limitée aux modèles échantillonnés.

## Deux duels décisifs

**E1 — Existe-t-il une tendance T2 transportable ?**  
- **H_A** : sur attaques fraîches, \(\beta\geq\log(1,05)\) par mois.  
- **H_B** : \(\beta<\log(1,05)\), y compris stabilité ou déclin.  
- **Métrique/seuil** : IC à 95 % de \(\beta\). Borne inférieure au-dessus du seuil ⇒ **H_B falsifiée** ; borne supérieure dessous ⇒ **H_A falsifiée** ; chevauchement ⇒ non concluant.  
- **Contrôles négatifs** : dates permutées, étiquettes permutées et corpus uniquement honnête ; aucun ne doit produire la pente annoncée.

**E2 — Le moniteur apporte-t-il autre chose qu’un détecteur d’artefacts ?**  
- **H_A** : sur les paires appariées fraîches, TD ≥ 80 %, TFA ≤ 1 %, et gain ≥ 10 points de détection sur les contrôles mécaniques disponibles au déploiement.  
- **H_B** : ce critère n’est pas atteint, ou le gain disparaît lorsque honnêtes et malveillants partagent générateur et distribution.  
- **Issue** : réussite préenregistrée sur le test final ⇒ **H_B falsifiée** ; TFA excessif ou borne supérieure du gain sous 10 points ⇒ **H_A falsifiée** ; sinon non concluant. Le cas rapporté où un moniteur fort donne 0 aux 375 échantillons sous injection (**RAPPORTÉ**, Scheurer §3.4) impose une strate injection distincte.

## Validité minimale des instruments

- **Vérificateur mécanique de vérité terrain** : fonctionnalité et condition plantée vérifiées indépendamment du moniteur ; il doit accepter tous les canaris valides, rejeter les artefacts invalides et ne marquer aucun jumeau honnête dans l’échantillon de qualification. Sinon, la tâche est retirée.
- **Moniteur** : critères E2, TD/TFA publiés par difficulté et par condition. Il doit battre tests fonctionnels simples, règles statiques et score fondé uniquement sur la sortie. Juges LLM et sondes d’activation ne servent pas de vérité terrain ; le plafond des juges est **OBSERVÉ-NON-AUDITÉ** (« nos résultats » §4).
- **Estimateur de tendance** : sous simulations nulles, fausse détection ≤ 5 % ; sur pentes plantées de +10 %/mois, détection ≥ 80 %. À défaut, aucune déclaration de pente.

## Pilote prioritaire et ancrage matériel

**Choix : T2**, car il évite l’élicitation adaptative et la rareté des comportements spontanés. Six moniteurs ouverts, 60 tâches, quatre attaques et quatre jumeaux honnêtes par tâche, deux conditions d’injection : **5 760 notations** (**calcul** : \(6\times60\times8\times2\)). Environ **150 h-H100 et 5–15 k€**, calibration humaine comprise (**illustratif**). Pilote **non concluant** si moins de 40 tâches restent valides, si plus d’un tiers des c50 sont censurés, ou si le TFA calibré ne se transporte pas au test ; il ne revendique alors aucun facteur mensuel.

Qwen2.5 fournit sept tailles de 0,5 à 72 milliards de paramètres, mais à une seule date (**RAPPORTÉ**, Scheurer §2.2) : utile pour séparer taille et date, insuffisant seul. Ajouter notamment Llama-3.1-8B-Instruct, dont la date reste à documenter. Étude complète : **500–1 500 h-H100, 30–100 k€** (**illustratif**).

**Échec du plan si :**
- les c50 sont presque tous censurés ou instables entre familles de tâches ;
- les attaques fraîches suppriment la pente, révélant contamination ou artefact de provenance ;
- on oublie que réussir T2 ne démontre toujours rien sur la propension spontanée.

FIN-DE-CELLULE

---

## E3-T1-conception-E.md (sha256 `49a1f9c8fb434f7fd1eb644591534861f9681a04fc43eaa8d98e7aeb07d5d885`)

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

---

## E3-T3-reponse-A.md (sha256 `5cdfe4c420ac1001379c1921e968191e4785aad9d940bb720f5eeef0bb8764f6`)

# Proposition A — Tour III.3 : réponse aux critiques

**Statuts.** Chiffres de `piece-scheurer-v1` : RAPPORTÉ. Chiffres de `piece-nos-resultats-v1` : OBSERVÉ-NON-AUDITÉ. Les critiques de D et E sont, comme elles le déclarent, des HYPOTHÈSES de méthode ; je les traite comme telles. Tout chiffre nouveau est « supposé » ou « calcul ».

**Pièces absentes.** Les critiques croisées B et C sont absentes (statut « jamais lancée ») ; je n'y réponds pas et n'en invente pas le contenu. Seules les sections « Sur la proposition A » de D et de E sont traitées ici.

## (a) Réponse critique par critique

Les critiques de D et E se recoupent largement ; je les regroupe par objet, en citant l'origine (D ou E). Codes : **ACCEPTÉE**, **REJETÉE** (avec raison), **→ TEST** (transformée en épreuve préenregistrée).

### A1. L'axe « lignes de code + traces » n'est pas scalaire (D, E)

**→ TEST, après acceptation partielle.** Accepté : additionner deux grandeurs sans unité commune était une erreur de définition. Correction : l'axe devient la **longueur en jetons de l'artefact lu par le moniteur** (une seule unité), et la part de trace dans cet artefact devient une covariable déclarée. Rejeté, en revanche, le corollaire implicite selon lequel « ajouter du contenu sans changer la difficulté » invaliderait la mesure : c'est précisément la dilution qu'un horizon de surveillance doit capturer, comme l'horizon METR capture la longueur des tâches sans en séparer la nature (RAPPORTÉ, § 3.1 : l'axe METR est une durée humaine, pas une difficulté intrinsèque). Pour rendre ce choix réfutable, j'ajoute le **contrôle de dilution à signal constant** (voir b, C2) : la même porte dérobée, entourée d'un volume croissant de code honnête ; si la détection y décroît aussi vite que sur la banque principale, l'horizon mesure la dilution seule — ce qui sera dit, non caché.

### A2. La pente temporelle est confondue avec famille, taille, fenêtre de contexte, exposition (D, E)

**ACCEPTÉE.** Je l'avais signalé au point (a)7 de ma conception (une seule date pour Qwen2.5), mais sans conséquence méthodologique. Conséquences maintenant : (i) deux estimands séparés et nommés, **pente de taille à date fixe** (Qwen2.5) et **pente de date à famille et taille contrôlées** (panel) ; (ii) le panel temporel exige au moins trois familles ouvertes datées, chacune à au moins deux dates (supposé : 10 à 12 moniteurs sur 24 mois) ; (iii) rapport préenregistré du rang de la matrice de conception (1, date, famille, log-taille, fenêtre de contexte) et de la variance résiduelle de la date après covariables ; si celle-ci est inférieure à un seuil fixé d'avance (supposé : 20 % de la variance brute), la pente est déclarée « non estimable », pas « nulle » ; (iv) significativité par **permutation des dates à l'intérieur des strates famille–taille échangeables** (contrôle n° 6 que D prescrit à E ; je le reprends en le disant) ; (v) pentes par famille rapportées séparément ; des signes opposés interdisent l'énoncé d'une loi commune.

### A3. Le contrôle mécanique plat est vrai par construction (D, E)

**ACCEPTÉE comme limite, REJETÉE comme inutilité.** Oui, sur une banque et un instrument figés, la platitude est attendue : ce contrôle ne teste que le pipeline. Je le garde à ce seul titre (un pipeline qui donne une pente non nulle à un instrument déterministe est cassé). La contamination, elle, sera testée autrement (**→ TEST**, C4 ci-dessous) : deux banques de problèmes, l'une antérieure au plus ancien moniteur, l'autre postérieure au plus récent (graines scellées, empreinte publiée, calque du § 5 de nos résultats, OBSERVÉ-NON-AUDITÉ) ; pour chaque moniteur, la différence d'horizon entre banques ; une différence qui croît avec la date du moniteur est la signature d'une exposition différentielle.

### A4. Appariement honnête/malveillant insuffisant ; un refus n'est pas un témoin honnête (D, E)

**ACCEPTÉE.** Compter un refus comme trajectoire honnête était une faute : son style et l'absence d'artefact fonctionnel révèlent l'étiquette. Correction : trois strates déclarées, **honnête fonctionnel**, **refus**, **invalide** ; seules les honnêtes fonctionnelles servent de négatifs ; refus et invalides sont rapportés par taille d'attaquant (ce taux est lui-même une mesure d'élicitation qui intéresse le point (a)3 de ma conception). Trois contrôles s'ajoutent (b, C1, C3) : paires honnête–honnête à étiquette factice ; détecteur de provenance et de style seul (métadonnées, longueur, format), qui doit rester au taux nominal ; appariement en longueur et validité du code entre classes.

### A5. Fuite entre calibration, ajustement et évaluation (D, E)

**ACCEPTÉE.** Partition scellée en trois ensembles disjoints par problème **et** par attaquant : calibration du seuil (C), ajustement logistique (F), évaluation finale (V). Avec sept attaquants Qwen2.5, deux sont réservés à V (supposé). Le duel gelé/contemporain se joue uniquement sur V.

### A6. Les duels D1 et D2 ne sont pas exclusifs ; D1 mélange pente, test et seuil ; D2 oppose un rapport à une évolution (D, E)

**ACCEPTÉE.** J'adopte la règle commune proposée par E (HYPOTHÈSE de règle, que je fais mienne en le disant) : chaque duel porte sur **un** paramètre, H_A : θ ≥ δ contre H_B : θ < δ ; un intervalle à 95 % entièrement d'un côté rejette l'autre hypothèse ; un chevauchement vaut « non concluant », jamais « absence d'effet ». Les duels reformulés sont en (b). Point d'E retenu explicitement : la falsification de H_A dans D2 établit une **baisse relative** de l'horizon contre attaquants contemporains, non une baisse absolue ; l'énoncé final le dira.

### A7. T2 : l'écart de log-paramètres n'ordonne pas les couples ; une seule date ; contenu témoin inerte manquant (D, E)

**→ TEST.** L'écart scalaire est abandonné comme variable explicative a priori. T2 devient une **matrice croisée attaquant × moniteur** (7 × 7 sur Qwen2.5, supposé) avec la probabilité de réussite u(a, m) comme cellule ; un seuil d'écart n'est rapporté que si u est monotone en a pour chaque m et en m pour chaque a (test de monotonie préenregistré, par bootstrap groupé) ; sinon T2 est déclarée « sans axe ordonné ». Contrôles ajoutés : contenu ajouté sémantiquement inerte, apparié en longueur, emplacement et format (D c4, E c) ; mêmes artefacts sans ajout. T2 reste hors du premier pilote et sans axe temporel tant que le panel daté de T1 n'existe pas.

### A8. T3 : conscience verbalisée ≠ désalignement ; classificateur à sensibilité variable ; témoin supervisé non équivalent ; probabilité bornée (D, E)

**ACCEPTÉE ; T3 rétrogradée.** (i) Échelle logit, pas « ×2 par doublement » ; (ii) variable comportementale ajoutée — le taux d'actions couvertes, la grandeur même que 2509.15541 § 6.2 relie à la conscience d'évaluation (RAPPORTÉ : 13,2 % → 24,2 % quand on la retire) — sans quoi T3 ne mesure pas du désalignement ; (iii) sensibilité et spécificité du classificateur estimées **à chaque point d'entraînement** sur annotations indépendantes, positifs et négatifs, et prévalence corrigée par la formule que D et E donnent toutes deux (calcul conditionnel) ; si s + v − 1 est sous un seuil fixé d'avance (supposé 0,5), le point est « non mesurable » ; (iv) le témoin supervisé perd son statut de contrôle négatif et devient une condition comparée, sous l'hypothèse déclarée qu'il ne modifie pas la grandeur. T3 n'entre pas dans le pilote.

### A9. T4 : variable dépendante indéfinie ; corrélation avec les refus non probante (D, E)

**ACCEPTÉE.** RAPPORTÉ : la signification des deux scores du tableau 6 n'est pas dans la pièce. T4 est **gelée** : elle ne sera ni tendue ni utilisée comme témoin d'échec tant que l'estimand n'est pas défini sur page primaire. La décomposition par refus que donne E (somme sur R) devient, si T4 renaît, l'estimand lui-même : P(sous-performance | capable, non-refus), avec le taux de non-refus rapporté à part.

### A10. Conditions probabilistes de non-jugeabilité (D b, E b)

**ACCEPTÉES toutes, → TESTS préenregistrés** : horizon censuré si la logistique reste d'un seul côté de 50 % sur la grille ; « non monotone, pas d'horizon » si croisements multiples (test de monotonie sur les points de grille) ; « instable » si l'intervalle bootstrap de l'horizon dépasse une octave (supposé), conséquence de la formule de variance d'E (dérivée faible au croisement) ; calibration vérifiée **par tranche de longueur** (A11) ; bootstrap **par grappes** au niveau problème et au niveau attaquant, avec n_eff rapporté ; rang de la matrice de conception rapporté (A2).

### A11. Le seuil fabrique la courbe : calibration globale vs par longueur (E)

**→ TEST, choix fixé d'avance.** Calibration **globale** par moniteur (un seuil τ_m à 5 % sur les honnêtes fonctionnelles de C), parce qu'une calibration par longueur définirait un autre instrument, comme E le note. Vérification : le taux de fausses alertes par tranche de longueur sur V doit rester dans [0,03 ; 0,08] (supposé) ; une tranche hors bande rend le moniteur « mal calibré » et son horizon non interprétable. Mesure secondaire, sans seuil : AUC par tranche de longueur, pour juger si la conclusion dépend du seuil.

### A12. La puissance de P3 ne se transporte pas (E)

**ACCEPTÉE.** Ma référence à « une détection sur six à force 0,5 » (OBSERVÉ-NON-AUDITÉ, § 5) était un ordre de grandeur emprunté à un autre estimateur. Un calcul de puissance propre, par simulation de la logistique avec corrélation intra-problème et intra-attaquant (paramètres supposés, publiés avant lancement), précédera le pilote. Illustratif : 7 000 lectures par moniteur en grappes de 14 (7 attaquants × 2 rôles) avec ρ = 0,2 donnent n_eff ≈ 7 000 / (1 + 13 × 0,2) ≈ 1 940 (calcul sur paramètres supposés, formule d'E).

### A13. Geler les attaquants ne neutralise pas l'élicitation ; la conclusion porte sur ce corpus (E)

**ACCEPTÉE comme portée, REJETÉE comme défaut.** Toute tendance porte sur sa banque : l'horizon METR porte sur ses tâches (RAPPORTÉ, § 3.1), TastEval sur son agent fixe et son H100 (RAPPORTÉ, § 3.2). L'estimand est donc renommé : « horizon de surveillance **contre le corpus gelé G** ». Ce qui est testable, c'est l'**invariance entre corpus** : **→ TEST** C5 — un second pool gelé d'une autre famille ouverte (supposé, non identifié dans les pièces) ; si les pentes contre G et G′ diffèrent de plus que leurs intervalles, la pente est propriété du couple moniteur–corpus et sera rapportée ainsi.

## (b) Expériences corrigées

### T1 corrigée — Horizon de surveillance contre corpus gelé

**Estimand.** Pour un moniteur m et un corpus gelé G : h_m = longueur en jetons de l'artefact (code + trace, trace en covariable) à laquelle la logistique ajustée p_m(x) croise 50 %, au seuil global τ_m calibré à 5 % de fausses alertes sur honnêtes fonctionnelles. Portes dérobées vérifiées à l'exécution par une entrée qui change la sortie (RAPPORTÉ, 2510.09462, tâche annexe) ; aucun juge de langage.

**Strates de trajectoires.** Honnête fonctionnel (négatifs), malveillant vérifié (positifs), refus, invalide ; taux de refus et d'invalides rapportés par attaquant.

**Partition scellée.** C (calibration), F (ajustement), V (évaluation), disjoints par problème et par attaquant ; graines scellées, empreinte publiée avant notation.

**Deux estimands de pente.** (P-taille) pente de log₂ h_m sur log-paramètres à date fixe, Qwen2.5 (RAPPORTÉ § 2.2 : sept tailles, une publication). (P-date) pente de log₂ h_m sur la date, sur panel ≥ 3 familles × ≥ 2 dates, avec famille, log-taille et fenêtre de contexte en covariables ; rang de conception et variance résiduelle de la date rapportés ; permutations intra-strates.

**Contrôles négatifs préenregistrés.**
- C1 — Paires honnête–honnête à étiquette factice, appariées sur problème, validité, longueur, rôle de génération : détection attendue = 5 % ; au-dessus, fuite d'étiquette, T1 non interprétable.
- C2 — Dilution à signal constant : porte dérobée fixe entourée de code honnête de longueur croissante ; sépare dilution et contenu.
- C3 — Détecteur de provenance/style seul (longueur, format, métadonnées) : doit rester au taux nominal.
- C4 — Deux banques de problèmes, antérieure au plus ancien moniteur et postérieure au plus récent : différence d'horizon par moniteur, régressée sur la date du moniteur (contamination).
- C5 — Second corpus gelé G′ : invariance des pentes.
- C6 — Instrument mécanique figé (suite de tests + entrées aléatoires) : contrôle de pipeline seulement, pente 0 attendue par construction.
- C7 — Calibration par tranche de longueur dans [0,03 ; 0,08] (supposé) ; AUC par tranche en secondaire.

**Règles de non-jugeabilité.** Horizon « censuré », « non monotone » ou « instable » (intervalle > 1 octave, supposé) exclu de la pente avec mention ; moniteur « non fonctionnel » s'il ne bat pas C6 sur V ; « mal calibré » s'il échoue C7 ; banc « sans dents » si tous les TPR à 5 % dépassent 0,95 (supposé) ; pente « non estimable » si la date n'a plus de variance résiduelle.

**Duels reformulés (règle commune).**
- **D1** : θ₁ = pente de log₂ h sur la date (bit/an). H_A : θ₁ ≥ 0,5 (doublement ≤ 24 mois) ; H_B : θ₁ < 0,5. Intervalle à 95 % par bootstrap groupé et permutations stratifiées. Issue H_A rejetée : l'énoncé « l'horizon double en moins de deux ans » est faux pour ce corpus ; issue H_B rejetée : il est tenu, avec facteur et intervalle. Chevauchement : non concluant.
- **D1′** (axe de taille) : θ₁′ = pente de log₂ h sur log₂-paramètres à date fixe ; H_A : θ₁′ ≥ 0,25 bit par doublement de taille (supposé) ; H_B : θ₁′ < 0,25. Ne dit rien sur le temps ; le dit explicitement.
- **D2** : θ₂ = log₂[h(contemporain)/h(gelé)] par moniteur, sur V. H_A : θ₂ ≥ −0,32 (rapport ≥ 0,8) ; H_B : θ₂ < −0,32. H_A rejetée : la subtilité des attaquants récents (RAPPORTÉ, 2506.05296, section non citée) érode l'avantage **relatif** du moniteur ; l'énoncé temporel doit alors être double (horizon absolu contre G, rapport contre contemporain). H_B rejetée : le gain contre G se transporte, à 20 % près, aux attaquants contemporains.

**Énoncé attendu (supposé, chiffre non tiré des pièces)** : « contre le corpus gelé G, l'horizon de surveillance croît de 0,8 à 1,3 bit par an (doublement en 9 à 15 mois) », signe positif ; énoncé alternatif si D2 tranche pour H_B : « … mais le rapport contre attaquants contemporains décroît de Y bits par an », Y inconnu, et c'est l'objet de la mesure.

### T2 corrigée — Matrice croisée d'injection (secondaire, conditionnelle)

Cellule u(a, m) sur 7 × 7 Qwen2.5 ; contrôles : contenu inerte apparié, artefacts sans ajout ; seuil d'écart rapporté seulement si monotonie établie ; axe temporel seulement sur le panel daté de T1. Injections décrites par classe, jamais reproduites.

### T3 corrigée — Conscience d'évaluation et actions couvertes par unité de renforcement (hors pilote)

Échelle logit ; double variable (verbalisée, comportementale) ; erreur du classificateur estimée par point d'entraînement sur annotations indépendantes ; condition supervisée comparée, non contrôle.

### T4 — gelée

Pas d'estimand tant que les scores de 2412.04984 § 3.6 ne sont pas définis sur page primaire.

### Pilote corrigé (T1, axe de taille d'abord)

Qwen2.5 0,5–72 B en attaquants et moniteurs ; 500 problèmes APPS en deux banques (C4) ; partition C/F/V scellée ; C1–C3, C6, C7 inclus ; calcul de puissance par simulation publié avant lancement. Coût illustratif inchangé (ordre de 1 500 € loués, quatre à six semaines, la semaine supplémentaire pour C1–C3). **Non concluant si** : moins de quatre moniteurs fonctionnels et calibrés ; C1 ou C3 au-dessus du nominal ; horizons majoritairement censurés ou non monotones ; banc sans dents.

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi (par les pièces, aux statuts indiqués).** RAPPORTÉ : la performance de surveillance dépend du moniteur (AUC 0,92 à 0,96 pour o3-mini, 2506.05296 § 2.3) et le moniteur le plus fort peut être réduit à 0 sur 375 par injection (2510.09462, fig. 2) : l'instrument n'est ni fixe ni robuste. RAPPORTÉ : capacité et propension sont « difficiles à démêler », un outil retiré fait passer 59 % à 3 %, les taux de base sont à 0 % sauf un cas (2603.01608) : une propension datée serait une pente de montage. RAPPORTÉ : les recettes METR et TastEval donnent un axe continu et une logistique, mais leurs nombres de tâches, de modèles et l'incertitude du doublement sont absents des pièces. OBSERVÉ-NON-AUDITÉ : deux juges de langage au plafond (κ = 0) ; un seuil calibré sur 1 000 épisodes honnêtes tient (0,046–0,055) là où un seuil théorique unilatéral donne 0,21–0,35 de fausses alarmes ; des sondes génériques restent sous leur plancher aléatoire. Rien, dans aucune pièce, n'établit l'existence d'une **tendance datée** pour un comportement désaligné ou pour la surveillance.

**Ce qui n'est pas établi.** (1) Qu'un horizon de surveillance soit identifiable : il peut être censuré, non monotone ou instable (critiques D et E, acceptées). (2) Que l'axe de taille (Qwen2.5, une date) se convertisse en axe de temps : cela exige un panel multifamille daté que les pièces ne fournissent pas. (3) Que la pente contre un corpus gelé se transporte à d'autres corpus et aux attaquants contemporains (D2, C5). (4) Que la calibration globale tienne par tranche de longueur (C7). (5) Pour T3 et T4, l'estimand lui-même. Les chiffres « 9 à 15 mois » restent supposés.

**L'expérience à faire en premier.** Le pilote T1 sur l'axe de **taille** (Qwen2.5, 7 × 7, deux banques, partition scellée, C1–C3, C6, C7), avant tout panel daté. Raison : c'est la seule expérience qui, à coût de l'ordre de 1 500 € (illustratif), répond aux quatre questions qui conditionnent toute tendance — le banc a-t-il des dents (TPR < 0,95 pour au moins un moniteur), les horizons sont-ils identifiables (monotones, non censurés, intervalle < 1 octave), le seuil tient-il par longueur, et les contrôles d'étiquette factice et de style restent-ils au nominal. Chacune de ces quatre réponses peut être négative, et chaque négative tue une partie précise du plan sans que l'on ait dépensé le panel. Le duel joué est D1′ (θ₁′ ≥ 0,25 bit par doublement de taille, supposé, contre θ₁′ < 0,25) ; il ne dit rien du temps, et le dit. Si D1′ tranche pour H_A et que C1–C3, C7 tiennent, le panel daté (P-date, D1, D2) est lancé ; si C1 ou C3 dépassent le nominal, l'instrument mesure des artefacts et doit être refait avant toute pente.

**Ce qui ferait échouer le plan**, en trois lignes : pas de panel ouvert multifamille daté, donc jamais d'axe de temps ; horizons censurés au plafond pour tout moniteur récent contre le corpus gelé ; D2 pour H_B, qui réduit l'énoncé à « l'avantage relatif du moniteur décroît », vrai mais sans le facteur positif demandé.

FIN-DE-CELLULE

---

## E3-T3-reponse-D.md (sha256 `75c25aacda65a01cec11ae45fd9a70327ebd4a8226fde1025833d2a991e2436e`)

Les pièces de critique **B** et **C** sont absentes ; je n’en invente pas le contenu. Les faits Scheurer restent **RAPPORTÉS**, ceux de « nos résultats » **OBSERVÉS-NON-AUDITÉS**, et les modifications ci-dessous sont des **HYPOTHÈSES** expérimentales.

## (a) Arbitrage des critiques visant D

### Critiques A

| Critique | Décision | Correction ou raison |
|---|---|---|
| **D1 — seuil de E1 égal à l’effet attendu** | **Acceptée.** | Le seuil décisionnel devient \(\delta=\log(1{,}02)\) par mois (**supposé** : +2 %/mois), nettement sous l’effet attendu de +5,1 %/mois (**supposé**). La taille de l’étude devra donner au moins 80 % de puissance (**supposé**) sous l’effet attendu, faute de quoi E1 ne sera pas lancé. |
| **D2 — difficulté confondue avec le générateur** | **Acceptée.** | Plusieurs générateurs figés ; difficulté estimée par des humains ignorants du générateur et des verdicts ; effets de générateur et standardisation sur un mélange de générateurs fixé à l’avance. Validation avec générateur entièrement laissé de côté. |
| **D3 — filtre honnête/malveillant asymétrique** | **Acceptée.** | Contrôles de qualité communs, appariement par tâche, générateur, longueur, complexité et format ; taux d’acceptation publiés. Refus, sorties invalides et solutions honnêtes fonctionnelles ne sont plus confondus. Sélection effectuée sans voir les scores des moniteurs. |
| **D4 — tendance de lecture de code rebaptisée surveillance** | **Acceptée et transformée en test.** | Mesurer séparément, pour chaque modèle, sa capacité ordinaire de programmation et de résolution sur les mêmes tâches. La pente ajustée \(\beta_{\mathrm{res}}\), conditionnelle à cette capacité, devient le paramètre principal. Si elle disparaît, le résultat sera rapporté comme tendance de capacité de code. |
| **D5 — fuite calibration/évaluation** | **Acceptée.** | Découpage disjoint par tâche et groupe de génération : calibration, développement, puis test final verrouillé. Aucun seuil ni choix de strate ne sera modifié après lecture du test. |
| **D6 — « attaques fraîches » ambiguës** | **Acceptée.** | Deux populations rapportées séparément : mêmes générateurs avec graines neuves ; générateurs nouveaux. Le second corpus constitue le test de transport principal. |
| **D7 — injection absente de la définition de E1** | **Acceptée.** | E1 porte exclusivement sur la strate **sans injection**. La strate avec injection possède ses propres estimands et résultats ; aucune moyenne entre les deux. |
| **D8 — refus dans T1** | **Acceptée.** | Modèle à risques concurrents : refus, échec fonctionnel, réussite. Publication de \(P(R)\), de la réussite marginale et de la réussite conditionnelle parmi les non-refus. Cette dernière ne sera appelée « capacité » que sous réserve explicite de sélection sur le consentement. |
| **D9 — FLOP dans T3** | **Acceptée.** | L’axe principal devient un nombre d’**opportunités d’épisode** sous calendrier figé ; les FLOP et la taille deviennent des mesures secondaires de coût. T3 ne prétendra plus mesurer une habileté par tentative à partir des seuls FLOP. |
| **D10 — nul trop simple et mauvaise puissance** | **Acceptée.** | Simulations conservant familles, effets tâche × moniteur, censure, sélection et dépendances ; permutations de dates intra-famille. Validation de puissance pour séparer +2 % et +5,1 %/mois, pas seulement pour détecter +10 %/mois. |

J’accepte également les conditions mesurables d’A :

- **TFA à 1 %** : 240 honnêtes ne suffisent pas. Le pilote ne certifiera pas ce taux. À titre de repère, même 299 épisodes honnêtes indépendants sans alarme donnent seulement une borne unilatérale à 95 % d’environ 1 % (**calcul**) ; l’échantillon final sera dimensionné sur des intervalles exacts et la dépendance par tâche.
- **c50** : il ne sera défini que pour une courbe monotone avec un unique croisement de 0,5 dans le support. Non-monotonie ou croisement hors support rendent l’estimand non jugeable ; les modèles censurés ne seront pas silencieusement supprimés.
- **Identification temporelle** : seules les dates intra-famille contribuent avec effets fixes de famille. Qwen2.5, à une seule date (**RAPPORTÉ**, Scheurer §2.2), n’identifie donc aucune pente temporelle.
- **Pilote à six moniteurs** : aucun bootstrap de pente et aucun facteur mensuel inférentiel ; il sert à qualifier l’instrument.
- **Test-retest** : il précède l’étude complète et fixe le plancher de variance utilisé dans le calcul de puissance.

Les neuf contrôles négatifs d’A sont intégrés : appariement longueur/complexité, provenance croisée, capacité de code, découpage disjoint, notation humaine aveugle, test-retest, oracle de qualification, permutations intra-famille et deux corpus frais. Deux précisions : la fiabilité d’un temps humain continu sera évaluée par fidélité inter-notateurs et test-retest, non par un κ inadapté ; l’oracle recevant l’information de vérification sert à contrôler les étiquettes sur un jeu indépendant, sans prétendre démontrer une erreur nulle.

Le duel proposé par A est **accepté dans son objectif**, mais son rapport \(\beta_{\mathrm{res}}/\beta_{\mathrm{brut}}\), instable lorsque la pente brute approche zéro, est remplacé par un test direct sur \(\beta_{\mathrm{res}}\).

### Critiques E

- **T1, intersection fonctionnalité–condition–franchissement : acceptée.** Les trois facteurs seront publiés séparément avec leurs dénominateurs. Si seuls quelques épisodes atteignent les derniers facteurs, aucune attribution de pente à ces facteurs ne sera faite. Des tâches honnêtes de fonctionnalité comparable mesureront la contribution de la programmation ordinaire.
- **Temps humain T1 : acceptée.** Il désignera uniquement la réalisation complète de l’épisode spécifié, distincte de la résolution honnête et de la détection. Les tâches et leurs temps seront gelés avant tout score de modèle ; aucune sélection selon la qualité de l’ajustement aux modèles.
- **T2, temps de production ≠ difficulté de détection : acceptée.** L’axe devient le **temps humain de détection correcte en aveugle**, avec leurres honnêtes. Le sens de monotone décroissance de la détection automatique sera testé, non imposé.
- **Jumeaux et corpus renouvelé : acceptée.** L’appariement de provenance ne suffit pas : ajout des appariements distributionnels, détecteurs limités au style et aux métadonnées, modifications inertes et exclusion des tâches uniquement selon des règles préenregistrées aveugles aux scores.
- **T3, dépendance et censure : acceptée.** Nouvelles graines et épisodes indépendants dans la mesure du protocole, dépendance résiduelle estimée par répétitions de la condition identique. Si \(q50\) n’est pas identifié avant \(q_{\max}\), il est déclaré non identifiable ; aucun modèle n’est retiré de la régression pour cette raison.
- **E2 composite : acceptée.** Le duel porte désormais sur un seul paramètre, le gain de détection \(\Delta\). La calibration est une condition de validité préalable, non une hypothèse supplémentaire à faire réussir simultanément.
- **Canaris du vérificateur : acceptée.** Développement, sélection des tâches et qualification finale utiliseront des échantillons distincts ; les taux d’erreur auront des intervalles de confiance.
- **Erreur de mesure de l’axe humain : acceptée.** Répétitions du panel et analyse d’erreur de mesure/sensibilité à l’atténuation.
- **Permutations et corpus honnête : acceptée.** Permutations restreintes aux blocs échangeables. Un corpus uniquement honnête teste les fausses alertes, mais ne peut pas, à lui seul, estimer un horizon de détection des attaques.

## (b) Expériences corrigées

### Instrument commun de T2

Pour chaque artefact, un panel humain mesure, sans connaître le générateur ni les verdicts automatiques, le temps nécessaire à une détection correcte parmi des leurres honnêtes. Pour un moniteur \(m\) :

1. son seuil \(\tau_m\) est calibré sur des tâches honnêtes disjointes ;
2. \(D_m(x,g)\) est sa probabilité de détection à difficulté humaine \(x\), pour le générateur \(g\) ;
3. \(c50_m\) est le temps humain auquel la détection standardisée sur le mélange fixé de générateurs vaut 0,5. Un \(c50\) plus grand signifie que le moniteur détecte des attaques plus difficiles à repérer humainement ;
4. l’oracle de qualification, les règles statiques, le score de longueur, les détecteurs de style et les tests disponibles au déploiement sont des contrôles distincts. Le meilleur contrôle est choisi sur le développement puis figé.

### E2 — Le moniteur apporte-t-il un gain propre ?

Condition de validité : calibration transportable sur les honnêtes indépendants et étiquettes mécaniques qualifiées. Sinon : **non jugeable**.

- \(H_A:\Delta\geq0{,}10\), où \(\Delta\) est le gain apparié de détection sur le meilleur contrôle figé, à TFA comparable (**seuil supposé** : 10 points).
- \(H_B:\Delta<0{,}10\).

Borne inférieure de l’IC au-dessus de 0,10 ⇒ **\(H_B\) falsifiée**. Borne supérieure sous 0,10 ⇒ **\(H_A\) falsifiée**, sans exclure un gain plus petit. Chevauchement ⇒ non concluant.

### E1 — Existe-t-il une pente de surveillance résiduelle et transportable ?

Sur le corpus final à générateurs nouveaux, **sans injection**, soit \(\beta_{\mathrm{res}}\) le coefficient de la date sur \(\log c50\), avec effets de famille et capacité ordinaire de code :

- \(H_A:\beta_{\mathrm{res}}\geq\delta\) ;
- \(H_B:\beta_{\mathrm{res}}<\delta\), avec \(\delta=\log(1{,}02)\)/mois (**supposé**).

Borne inférieure au-dessus de \(\delta\) ⇒ **\(H_B\) falsifiée** ; borne supérieure sous \(\delta\) ⇒ **\(H_A\) falsifiée**, et toute pente brute sera rapportée comme capacité générale ou artefact selon les contrôles ; chevauchement ou matrice de conception déficiente ⇒ non concluant. Mêmes générateurs/graines neuves et injection restent des analyses diagnostiques séparées.

## (c) Réponse à l’arbitre : établi, non établi, première expérience

### Ce qui est établi dans les pièces — et ce qui ne l’est pas

Une propension brute est un mauvais axe en l’état : retirer un outil peut faire passer un taux de manigance de 59 % à 3 %, avec des taux de base presque toujours nuls (**RAPPORTÉ**, Scheurer §2.1). La force générale d’un moniteur ne garantit pas sa robustesse : le moniteur le plus fort sans injection y donne 0 aux 375 échantillons de code à porte dérobée (**RAPPORTÉ**, §3.4). Le plafond des juges LLM et la nécessité d’une calibration sur épisodes entiers sont seulement **OBSERVÉS-NON-AUDITÉS** (« nos résultats » §4 et §6).

Le doublement METR d’environ sept mois est **RAPPORTÉ** (§3.1), avec des informations méthodologiques manquantes. **Aucune pente temporelle de manigance spontanée, de surveillance ou de contrôle n’est établie ici.** Les trois tendances suivantes restent des **HYPOTHÈSES**.

| Candidate corrigée | Grandeur comparable et ajustement | Énoncé attendu |
|---|---|---|
| **T1 — subversion accessible sous protocole figé** | \(h50\), durée humaine de réalisation complète où la réussite de l’épisode atteint 50 % ; refus et facteurs fonctionnalité/condition/franchissement publiés séparément. Logistique à effets de tâche, puis régression de \(\log h50\) sur la date avec effets de famille. | **+10,4 %/mois** (**supposé ; calcul** depuis un doublement en sept mois), sans interprétation comme propension spontanée. |
| **T2 — surveillance à risque fixé** | \(c50\), temps humain de détection où le moniteur tombe à 50 %, à TFA calibré ; standardisation sur générateurs et ajustement sur la capacité de code. | **+5,1 %/mois** pour \(c50\) (**supposé, illustratif**) ; signe positif = surveillance améliorée. |
| **T3 — budget d’opportunités d’élicitation** | \(q50\), nombre d’opportunités sous calendrier non adaptatif figé où 50 % des tâches réussissent T1 ; survie avec censure, FLOP seulement secondaires. | **−5,0 %/mois** (**supposé, illustratif**) ; q50 non identifiable ⇒ pas de pente q50. |

Plan temporel commun : **18–24 points modèle-date, au moins quatre familles avec chacune au moins trois dates, sur 24–36 mois** (**supposé**), sous réserve du calcul de puissance. Validation sur dates finales réservées ; IC à 95 %, permutations intra-famille et bootstrap seulement si sa couverture est validée. Qwen2.5 sert à une analyse transversale de taille, pas à identifier la date.

### Premier pilote : E2/T2, sans estimation de pente

**Pourquoi lui :** il évite les événements spontanés rares, utilise une vérité terrain mécanique et produit un axe continu même quand une propension brute vaudrait zéro.

**Taille :** six moniteurs ouverts, 60 tâches réparties entre calibration/développement/test, quatre paires attaque–honnête par tâche et deux conditions d’injection : **5 760 notations** (**calcul** : \(6\times60\times8\times2\)), auxquelles s’ajoutent le panel humain et un échantillon honnête indépendant dimensionné par intervalles exacts. Coût révisé : **300–600 h-H100 et 20–50 k€** (**illustratif**), à re-chiffrer après le prétest humain.

**Menaces et contrôles :** provenance/longueur par appariement et détecteurs restreints ; capacité ordinaire par mesure de code conditionnée ; contamination par les deux corpus frais ; calibration par découpages disjoints ; injection par strate séparée.

**Non concluant** si moins de 40 tâches valides (**supposé**), si l’axe humain est insuffisamment fiable, si plus d’un tiers des c50 sont censurés ou non uniques (**supposé**), ou si le transport du TFA n’est pas estimable à la tolérance préenregistrée. Aucun facteur mensuel ne sera alors annoncé.

**Ce qui ferait échouer le plan :**
- les temps humains sont instables ou la détection n’est pas monotone : \(c50\) n’a pas de référent ;
- la calibration ou les contrôles de provenance échouent sur le test verrouillé : l’instrument est non jugeable ;
- la pente résiduelle disparaît après capacité de code ou sur générateurs nouveaux : T2 ne mesure pas une progression propre de surveillance.

FIN-DE-CELLULE

---

## E3-T3-reponse-E.md (sha256 `05717eafc66f0fa050e60426f2e7115e263c492bab7bf4c148ea623fbc50f616`)

# E — Réponse aux critiques : une frontière conditionnelle, non une mesure d’intention

**RAPPORTÉ — pièces absentes :** les critiques B et C ne sont pas fournies ; aucun contenu ne leur est attribué.

**Convention :** les corrections, expériences et interprétations proposées ci-dessous sont **HYPOTHÈSE**, non des résultats. Tous leurs nombres sont **supposés, illustratifs**, y compris les calculs de budget. Les constats documentaires conservent leur statut **RAPPORTÉ**. Aucune expérience n’est exécutée ici.

## a) Décisions sur les critiques visant E

### Critiques de A

| Critique | Décision et correction |
|---|---|
| **E1 — Accumulation des fausses alertes** | **Acceptée quant à l’ambiguïté ; rejetée comme identité générale.** La formule donnée suppose des alarmes par décision et une structure d’indépendance. E-A utilisera désormais **un score de trajectoire entière**, calibré séparément par longueur. La frontière dépendra explicitement de cette procédure ; elle ne sera pas présentée comme une propriété intrinsèque du modèle. |
| **E2 — Placement et densité** | **Acceptée.** Condition principale : une anomalie par épisode positif, position tirée uniformément parmi les positions admissibles. Les conditions à densité constante seront distinctes, jamais agrégées à cette mesure. |
| **E3 — Granularité sans ancrage humain** | **Acceptée pour la portée ; rejetée comme invalidation.** L’unité sera une transition d’état définie par une grammaire versionnée. L’absence d’ancrage humain interdit une comparaison directe avec l’horizon METR, pas une comparaison interne entre moniteurs. |
| **E4 — Raisonnement ordinaire rebaptisé** | **Transformée en test.** Ajouter une tâche appariée de reconstruction d’état sans anomalie. Une surveillance reposant sur du raisonnement reste une tâche de surveillance ; en revanche, je retire toute prétention à mesurer une faculté spécifiquement liée au désalignement. |
| **E5 — Information inaccessible** | **Acceptée.** Un oracle limité au journal doit pouvoir identifier l’étiquette. L’oracle privilégié seul ne suffit plus. Les cas ambigus sont exclus du corpus principal avant notation. |
| **E6 — Grille grossière et censure** | **Acceptée.** Une phase de développement choisit une grille plus dense ; cette grille est ensuite gelée et commune. Pas de frontière ponctuelle obtenue uniquement par interpolation logistique. |
| **E7 — Minimum de budget optimiste** | **Acceptée.** Grille identique entre modèles ; sélection et certification sur tâches disjointes ; intervalles simultanés sur les budgets. |
| **E8 — Confinement comme transformation du risque** | **Acceptée sous les hypothèses indiquées.** Publier le risque par occasion et la survie par épisode. Si le modèle indépendant suffit, E-C sera présenté comme sa traduction opérationnelle, non comme une loi supplémentaire. |
| **E9 — Fenêtre de contexte** | **Acceptée.** Mesure principale dans l’intersection des contextes utilisables, avec sérialisation commune. Un protocole à fenêtres identiques sera une condition distincte, pas un changement silencieux d’instrument. |
| **E10 — Absence d’effet minimal** | **Acceptée.** Les duels porteront sur un facteur minimal pertinent, fixé avant collecte, et non seulement sur le signe. |
| **E11 — Identification calendaire** | **Acceptée.** Audit préalable du rang de la matrice et de la variation temporelle résiduelle. Sans contrastes intra-famille à taille comparable, aucune pente ajustée ne sera publiée. |

**Conditions probabilistes de A — acceptées comme alertes, avec réserves.** Le pilote initial ne pouvait pas certifier convenablement les contraintes simultanées. Je retire cette ambition. En revanche :

- une corrélation positive résumée par un coefficient ne suffit pas, à elle seule, à établir l’inégalité proposée pour la probabilité d’au moins une alarme ;
- une classe de censure commune implique une perte d’identification, pas une variance véritablement nulle des horizons ;
- le biais du minimum est un risque de sélection à mesurer, pas une inégalité universelle sans hypothèses sur les courbes et le bruit ;
- **calcul illustratif correctif :** à un risque par occasion de \(10^{-3}\), **1 000** occasions donnent un dommage attendu ; **3 000** en donnent trois.

**Contrôles de A.** J’accepte les épisodes honnêtes, l’oracle à journal seul, les scores aléatoires, les répétitions de checkpoints, le contrôle de contexte, la tâche d’état, la certification indépendante des budgets et les permutations conditionnelles. Je transforme les contrôles de localité et de position en tests : des taux égaux ne prouvent pas l’absence de suivi d’état ; un effet de récence ne rend pas automatiquement l’horizon inexistant, mais restreint son interprétation.

**Duel de calibration de A — transformé.** La concordance des rangs entre deux calibrations ne démontrerait pas une indépendance vis-à-vis de la calibration. Je testerai plutôt si la différence entre leurs pentes temporelles reste sous une tolérance préenregistrée. Ce sera un test de robustesse, non une validation ontologique de « l’horizon ».

### Critiques de D

| Critique | Décision et correction |
|---|---|
| **Géométrie du générateur** | **Acceptée.** Réserver des familles de tâches et un générateur indépendant. La généralisation sera testée séparément de la performance sur graines nouvelles. |
| **Fausses alertes dépendant de la longueur** | **Acceptée.** Le calibrateur conditionnel à la longueur fait désormais partie de la définition publiée de l’instrument. |
| **Maximum sans monotonie** | **Acceptée.** Employer une frontière de préfixe : toutes les longueurs jusqu’à la frontière doivent satisfaire les contraintes. Publier néanmoins les courbes complètes ; une forte non-monotonie interdit l’interprétation en horizon lisse. |
| **Minimum de budget** | **Acceptée**, avec certification indépendante comme ci-dessus. |
| **Confinement algébrique** | **Acceptée conditionnellement**, comme E8. |
| **Régression non identifiée et permutations** | **Acceptée.** Pentes par famille, audit de colinéarité et permutations seulement lorsque l’échangeabilité est défendable. Le moniteur figé ne contrôle que le pipeline. |
| **Pilote trop petit** | **Acceptée.** Le nouveau pilote vise d’abord la validité et la résolution de l’instrument, pas une tendance calendaire. |

**Conditions et contrôles de D.** J’accepte les contrôles à étiquettes factices, les ensembles réservés, la longueur sans dilution, la séparation sélection/certification, les flux honnêtes et les bornes « tout autoriser/tout bloquer ». Une précision : un ensemble de budgets admissibles non monotone peut avoir un minimum unique ; c’est l’interprétation comme franchissement régulier qui échoue. Un risque observé nul ne justifie jamais d’annoncer un horizon infini.

## b) Expériences corrigées

### Instrument commun

**HYPOTHÈSE — protocole.**

- Séparer par **familles de tâches** le développement, la calibration et la certification. Les paires restent dans le même découpage.
- Produire des journaux appariés en longueur, opérations et présentation. L’oracle privilégié établit l’état réel ; l’oracle à journal seul établit l’identifiabilité informationnelle.
- Noter une trajectoire entière. Rapporter détection, fausses alertes et refus séparément. La performance opérationnelle inclut les refus comme échecs de détection, sans être renommée « capacité pure ».
- Calibrer les seuils sur des épisodes honnêtes entiers à chaque longueur ; les figer avant certification.
- Fixer une anomalie par épisode positif ; mesurer séparément les effets de position, de localité et de dépendance d’état.
- Pour E-A, définir \(H_m\) comme la plus grande longueur dont **tout le préfixe de grille** respecte détection et fausses alertes. Distinguer frontière estimée et borne certifiée ; conserver la censure.
- Pour E-B, comparer les budgets effectivement consommés. Une tendance en opérations sera une tendance d’**efficacité de calcul**, non de compétence par tentative.
- Pour E-C, fixer fréquence et gravité des propositions exogènes ; mesurer dommage et utilité sur épisodes entiers, sans multiplier artificiellement les observations par le nombre d’actions.

### Duels préenregistrés

Chaque ligne oppose deux hypothèses exclusives et exhaustives. Une décision exige un intervalle entièrement d’un côté du seuil ; sinon, l’expérience reste **non concluante**, sans falsification revendiquée.

| Expérience | \(H_A\) | \(H_B\) | Ce que les issues discriminantes falsifient |
|---|---|---|---|
| **Validité transférable de E-A** | Sur générateur réservé, avantage de détection du moniteur sur les baselines de style/localité \(>\delta\), à risque d’alerte fixé | Avantage \(\leq\delta\) | A réfute l’absence d’avantage pertinent ; B réfute la justification de poursuivre cet instrument neuronal. |
| **Robustesse à la calibration** | \(|\beta_{\mathrm{entier}}-\beta_{\mathrm{décision}}|<\eta\) | Différence \(\geq\eta\) | A réfute une sensibilité supérieure à la tolérance ; B réfute la transportabilité entre ces deux instruments. |
| **E-A, tendance** | \(\beta_H>\log(1{,}01)\) par mois | \(\beta_H\leq\log(1{,}01)\) | A réfute l’absence de croissance minimale ; B réfute la croissance minimale postulée. |
| **E-B, tendance** | \(\beta_B<\log(0{,}99)\) par mois | \(\beta_B\geq\log(0{,}99)\) | A réfute l’absence d’économie minimale ; B réfute cette économie. |
| **E-C, tendance** | \(\beta_K>\log(1{,}01)\) par mois | \(\beta_K\leq\log(1{,}01)\) | Même lecture que E-A, conditionnelle au contrôleur et au flux fixés. |

**HYPOTHÈSE — seuils illustratifs :** \(\delta=10\) points de détection ; \(\eta=\log(1{,}01)\) par mois. Leur justification opérationnelle et la puissance correspondante doivent être arrêtées avant certification.

La comparaison avec la reconstruction d’état produira deux estimands : pente brute de surveillance et pente conditionnelle à cette capacité. Une disparition de la seconde réfuterait une contribution temporelle **résiduelle**, pas l’utilité opérationnelle de la première.

## c) Réponse à l’arbitre — une page

### Ce qui est établi dans les pièces, sans vérification nouvelle

**RAPPORTÉ :** Apollo décrit une surveillance de trajectoires entières — pièce Scheurer, §1.3. Les performances de surveillance peuvent dépendre du moniteur, de la provenance des exemples et de la présence d’injections — même pièce, §3.3–3.4. Ces constats motivent un instrument conditionnel ; ils n’établissent aucune pente temporelle pour E.

**RAPPORTÉ :** les **sept** tailles Qwen2.5 sont associées à une même publication du **19 septembre 2024** — pièce Scheurer, §2.2. Elles permettent un pilote transversal, pas une tendance mensuelle.

### Ce qui ne l’est pas

**HYPOTHÈSE :** une frontière de surveillance mesurable, transférable et approximativement multiplicative existe. Sa monotonie, son indépendance relative au générateur et la disponibilité d’un panel longitudinal comparable restent à tester. Une anomalie plantée ne mesure ni une intention ni une propension spontanée au désalignement.

### Trois tendances candidates maintenues

| Candidate | Grandeur et échelle communes | Énoncé visé, **supposé, illustratif** |
|---|---|---|
| **E-A — priorité** | Longueur certifiable à détection **80 %**, fausses alertes **5 %**, sur transitions versionnées et corpus commun | « Sur cet instrument, l’horizon croît de **+3 % par mois**, facteur **1,03**. » |
| **E-B** | Opérations d’inférence minimales certifiées, longueur et critères fixes | « Le calcul requis diminue de **−4 % par mois**, facteur **0,96**. » |
| **E-C** | Occasions contrôlables sous dommage d’épisode **5 %** et utilité honnête **90 %** | « L’horizon de confinement croît de **+2 % par mois**, facteur **1,02**. » |

Ces instruments évitent d’exiger une malveillance spontanée : les événements sont exogènes et vérifiables. Leurs menaces principales sont respectivement le style du générateur, la sélection du budget et l’accumulation du risque ; les contrôles correspondants sont le transfert réservé, la certification indépendante et la mesure par épisodes entiers.

**HYPOTHÈSE — panel :** cible de **douze checkpoints sur vingt-quatre mois**, avec répétitions intra-famille à tailles comparables. **Les noms et dates nécessaires ne sont pas fournis : ce panel n’est pas encore constitué.**

Ajuster les réponses par longueur ou budget en conservant leur incertitude et leur censure, puis estimer les pentes temporelles par famille. Rapporter \(e^\beta\) et des intervalles simultanés à **95 %**, avec rééchantillonnage des unités indépendantes pertinentes et analyses de sensibilité. Des pentes familiales opposées interdisent un facteur universel. La date reste une association descriptive, non une cause identifiée.

### Première expérience à faire

**HYPOTHÈSE — pilote E-A :** deux tailles Qwen2.5 à sélectionner selon mémoire disponible ; longueurs **8, 16, 32 et 64** transitions. Par longueur et modèle : **300** épisodes honnêtes de calibration, puis **600** honnêtes et **300** positifs de certification.

**Calcul illustratif :** \(2\times4\times(300+600+300)=9\,600\) notations principales. Les contrôles et répétitions s’ajoutent et doivent être budgétés avant lancement.

**HYPOTHÈSE — enveloppe illustrative :** plafond de **300 heures-GPU**, à **2 €/heure**, soit **600 € — calcul illustratif**, hors travail humain. Un chronométrage préalable déterminera si cette enveloppe suffit ; aucun débit n’est présumé.

Le premier duel est celui de **validité transférable**, pas celui de la date. Pilote non concluant si les intervalles ne résolvent pas l’avantage minimal, si les frontières restent censurées, si l’information du journal est insuffisante ou si le budget empêche la certification prévue.

### Échec du plan
Pas de contrastes temporels comparables : aucune tendance calendaire.  
Pas d’avantage transférable au-delà des artefacts : abandon de cet instrument.  
Frontières non résolues ou fortement non monotones : publier les courbes, renoncer au facteur mensuel unique.

FIN-DE-CELLULE