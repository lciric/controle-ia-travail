# Proposition A, tour III.1 : conception ciblée

## Notes d'intégrité

- Le bloc FAITS ne contient aucun fait porteur de statut : il reproduit la question, donc rien ci-dessous n'est VÉRIFIÉ et tout énoncé de fond est une HYPOTHÈSE.
- Les deux blocs portent la même empreinte sha256 ; je ne l'ai pas recalculée.
- Je ne vois aucune autre proposition (B à E) à ce tour : je n'en critique ni n'en utilise aucune.
- Tous les seuils et chiffres ci-dessous sont illustratifs et à préenregistrer avant exécution.

---

## Réponse aux cinq points de la question

### Modèle de travail (HYPOTHÈSE, calcul sous hypothèses d'indépendance et d'additivité)

Notations :
- T : nombre d'actions.
- σ : écart-type de l'erreur honnête par action, supposée de moyenne nulle dans la direction qui compte.
- D : dommage total signé ajouté par l'adversaire, réparti sur k actes (d = D/k par acte).
- f : fraction auditée ; n : nombre d'exécutions de comparaison.

Conséquences du modèle :

- **Moniteur de texte par action.** Si le décalage du score est proportionnel à d, l'indice agrégé vaut d′ ∝ (D/k)·√k = D/√k. La dilution sert l'adversaire, bornée par k ≤ T, d'où un plancher d′ ∝ D/√T.
- **Audit aléatoire d'une fraction f, somme signée des écarts.** z = √f · D / (σ√T), indépendant de k.
- **Dommage maximal indétectable.** Dans les deux cas, D_max(T) ∝ T^β avec β = 1/2. C'est la forme de la loi en racine carrée connue en stéganographie.
- **Dommage nécessaire.** Posons D*(T) ∝ T^α pour le dommage requis pour dégrader le résultat. La longueur sert l'adversaire si β > α, le défenseur si β < α.
  - Tâche additive (résultat = agrégat de T contributions, sabotage utile s'il dépasse le bruit honnête σ√T) : α = 1/2. La longueur est neutre. L'adversaire garde une marge constante d'environ z/√f écarts-types honnêtes, quel que soit T.
  - Tâche en série ou à goulot (une décision précoce contamine la suite) : α ≈ 0. La longueur sert l'adversaire.
- **Activations.** Deux cas s'excluent.
  - Signal d'acte : il n'est présent qu'aux k actes sabotés et se dilue comme le texte.
  - Signal d'état : l'intention est lisible à chaque action, même bénigne. Alors d′ ∝ δ·√T_eff, avec T_eff = T/(1+(T−1)ρ), indépendant de D et de k. La longueur sert le défenseur jusqu'à T ≈ 1/ρ.
- **Exécutions de comparaison.** Elles calibrent la composante par action avec n·T échantillons, mais la composante entre exécutions (décalage propre à chaque exécution, corrélation ρ) avec n seulement. La longueur n'aide donc pas sur ce point.

### (1) Question de recherche

> L'exposant β du dommage maximal indétectable, D_max(T) ∝ T^β, vaut-il 1/2 pour tous les instruments du défenseur (dilution dans le bruit des erreurs honnêtes), ou les activations le font-elles tomber sous 1/2 parce qu'elles lisent un état d'intention présent à chaque action et non aux seuls actes de sabotage ?

### (2) Réponse attendue, réfutable (HYPOTHÈSE)

- **R1.** Pour le texte et l'audit, β ∈ [0,35 ; 0,65]. Confiance modérée à bonne.
- **R2.** Sur un modèle affiné pour saboter sous déclencheur, une sonde linéaire sépare les actions bénignes d'une exécution saboteuse des actions appariées d'une exécution honnête (AUROC ≥ 0,70) et se généralise à un déclencheur non vu. Le gain au niveau de la trajectoire plafonne ensuite : d′(800)/d′(200) < 1,2. C'est un pari à confiance faible, et le point que je tiens le plus à voir testé.
- **R3.** Le taux de sabotage réussi et non détecté monte avec T en tâche en série et reste plat en tâche additive.

Chacune est réfutée par les issues décrites en (b).

### (3) Antériorité la plus proche

- **Pour la loi :** Ker, Pevný, Kodovský, Fridrich (2008), « The Square Root Law of Steganographic Capacity ». Citée de mémoire, lieu de publication à vérifier.
- **Pour le cadre :** Greenblatt, Shlegeris, Sachan, Roger (2023), « AI Control: Improving Safety Despite Intentional Subversion ». Citée de mémoire.
- **Pour l'accumulation séquentielle de preuves :** Wald (1945), « Sequential Tests of Statistical Hypotheses ». Citée de mémoire.
- **Références à vérifier**, que je ne peux pas attribuer complètement de mémoire :
  - un travail de 2024 sur le déploiement adaptatif face aux menaces réparties sur plusieurs tâches, probablement le plus proche du côté contrôle ;
  - un banc d'essai de sabotage et de surveillance d'agents (2025) ;
  - un travail sur la détection de tromperie par sondes linéaires (2025) ;
  - des évaluations de sabotage pour modèles de pointe (2024).

### (4) Expérience qui trancherait

Voir E1 à E3 en (b). Elles sont réalisables en deux mois sur un modèle ouvert de 8 milliards de paramètres, avec une tâche synthétique à vérité de terrain mécanique.

### (5) Type de contribution

- Une **loi connue ailleurs** (racine carrée en stéganographie, analyse séquentielle), transposée au sabotage diffus sous la forme d'une comparaison d'exposants α et β.
- Un **test de mécanisme** : signal d'état contre signal d'acte dans les activations.
- **Aucune garantie.** Les bornes ne valent que sous indépendance et additivité, et face à un adversaire qui ne choisit que k et d.

### Issues qui rendraient la question sans intérêt

- **Le contrôle mécanique suffit.** Une vérification mécanique (z-score du résultat final contre les exécutions de comparaison, ou somme signée sur audit aléatoire) atteint le même D_max que tous les autres instruments, avec β = 1/2 partout. La question se réduit alors à de la statistique de manuel et les activations n'apportent rien.
- **La prémisse n'est pas réalisée.** Le modèle de 8 milliards ne sait pas saboter sans que chaque acte soit détectable isolément (AUROC par acte du moniteur de texte > 0,95). La condition « aucun acte suspect isolément » n'est pas remplie à cette échelle et l'expérience ne dit rien de la longueur.
- **L'agent honnête échoue déjà.** Son taux d'échec sur tâche longue sature (> 80 % de résultats dégradés à T = 800). Le sabotage devient superflu et indiscernable.

### Vérification de la nouveauté

Je n'affirme aucune nouveauté établie. Deux éléments sont à vérifier (statut HYPOTHÈSE) :
- la comparaison explicite α contre β en fonction de la longueur ;
- le test d'une sonde sur les actions bénignes d'un agent saboteur, en fonction de T.

Méthode :
- lire les références ci-dessus et les travaux qui les citent ;
- y chercher toute courbe de détection en fonction de la longueur de trajectoire, ou du nombre d'actes à dommage fixé ;
- y chercher toute évaluation de sonde hors des pas sabotés.

Mon estimation est que la partie « accumulation de preuves » est probablement déjà couverte par le travail sur les menaces réparties (référence à vérifier). Seuls l'exposant et le test état contre acte pourraient rester.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut |
|---|---|---|
| S1 | Un sabotage diffus existe : un agent peut dégrader le résultat par des actes dont aucun n'est suspect isolément. Rien ne dit qu'un modèle de 8 milliards en est capable. | HYPOTHÈSE |
| S2 | « Suspect isolément » a un sens opératoire, ce qui suppose un moniteur par acte et un seuil. Ni l'un ni l'autre n'est défini. | HYPOTHÈSE |
| S3 | Erreurs honnêtes et sabotage diffèrent en distribution (direction, placement, corrélation). Sinon seul le taux d'erreur compte. | HYPOTHÈSE |
| S4 | Les activations portent une information absente du texte. | HYPOTHÈSE |
| S5 | Les exécutions de comparaison sont honnêtes et échangeables avec l'exécution surveillée. La question ne dit pas qui les produit (modèle de confiance plus faible ? même modèle ?). | HYPOTHÈSE |
| S6 | La vérification coûteuse est fiable : elle voit l'erreur là où elle regarde. La « petite part » se compte en actions. | HYPOTHÈSE |
| S7 | La longueur est séparable de la difficulté, de la structure de dépendance et du taux d'erreur. | HYPOTHÈSE |
| S8 | L'adversaire connaît le protocole mais pas les actions auditées ; il n'y a pas de collusion avec le moniteur. La question ne le précise pas, je le pose. | HYPOTHÈSE |
| S9 | Le dommage se mesure sur une échelle scalaire (D), et « dégrader le résultat » a un seuil. | HYPOTHÈSE |
| S10 | Un agent de 8 milliards tient des centaines d'actions. Sans échafaudage (état résumé, sous-étapes bornées), c'est douteux. | HYPOTHÈSE |

S3, S4 et S7 sont testés par les expériences. S1 et S10 sont des conditions de validité, vérifiées en semaine 1.

---

## (b) Expériences décisives

### Banc commun

**Tâche.** Une méta-analyse synthétique : T fiches d'études générées par script, à effet connu.
- L'agent extrait, convertit et consigne chaque effet, puis rend une estimation agrégée et un verdict.
- Variante additive : les fiches sont indépendantes.
- Variante en série : certaines actions fixent une règle (unité, critère d'exclusion) appliquée à toutes les fiches suivantes.
- La vérité de terrain est connue par construction : l'audit est un oracle mécanique dont on fixe le budget f.
- Longueurs : T ∈ {50, 100, 200, 400, 800}.

**Erreurs honnêtes.** Ce sont celles que commet spontanément le modèle. Elles sont mesurées, non injectées.

**Trois régimes d'adversaire.**
- *Pantin* : écarts injectés par script à k et d connus. C'est un contrôle positif du pipeline, sans valeur pour les activations.
- *Consigne* : instruction de sabotage dans le message système.
- *Affiné* : adaptateur LoRA entraîné à biaiser sous déclencheur. Deux déclencheurs de sabotage et deux déclencheurs placebo sont vus à l'entraînement, les placebos sans sabotage associé.

**Calibration.** Les seuils sont fixés sur des exécutions honnêtes disjointes, à un taux de fausses alertes de 5 % par trajectoire.

### E1 : loi de dilution (texte et audit)

- **H_A.** β ∈ [0,35 ; 0,65] pour le meilleur instrument sans activations : la preuve s'accumule en racine.
- **H_B.** β ≥ 0,85 : la preuve ne s'accumule pas. Les scores honnêtes sont si corrélés au sein d'une trajectoire que l'échantillon effectif sature, et l'adversaire sabote une fraction constante du travail.
- **Métrique.** D_max(T) : dommage détecté dans 50 % des cas à 5 % de fausses alertes, en prenant pour chaque T le k le plus favorable à l'adversaire sur une grille. β est la pente du log-log sur les cinq longueurs, avec intervalle bootstrap à 90 %.
- **Seuil.** L'intervalle doit tenir entièrement dans une zone.
- **Contrôles négatifs.**
  - Honnête contre honnête : la détection doit valoir 5 % à la tolérance binomiale près.
  - Dose nulle (consigne de saboter « plus tard », D = 0) : la détection par le texte doit rester à 5 %.
- **Contrôle positif.** Le pantin doit rendre β = 0,5 ± 0,1. Sinon le pipeline est biaisé et rien n'est conclu.
- **Falsification.**
  - Intervalle dans [0,35 ; 0,65] : H_B est falsifiée.
  - Intervalle au-dessus de 0,85 : H_A et R1 sont falsifiées. L'hypothèse d'indépendance tombe et le défenseur ne gagne rien à agréger.
  - β < 0,35 : les deux sont falsifiées. La lecture probable est un sabotage maladroit à toute dose, ce qui renvoie à l'issue « prémisse non réalisée ».
  - Entre 0,65 et 0,85 : indécis. Je le dirai tel quel.

### E2 : état ou acte (activations)

- **H_A (état).** Une sonde linéaire entraînée sur {déclencheur 1 contre placebo 1} sépare, sur {déclencheur 2 contre placebo 2}, les actions bénignes des exécutions saboteuses des actions appariées des exécutions honnêtes, avec AUROC ≥ 0,70 par action. La détection par trajectoire croît alors avec T.
- **H_B (acte).** AUROC ≤ 0,55 sur ces actions bénignes : les activations se diluent comme le texte.
- **Appariement.** Mêmes poids (adaptateur présent des deux côtés), même fiche, même position, même préfixe imposé. Seul diffère le déclencheur.
- **Métriques.** AUROC par action sur actions bénignes ; taux de détection par trajectoire à 5 % de fausses alertes en fonction de T ; corrélation intra-trajectoire ρ des scores de sonde.
- **Contrôles négatifs.**
  - Sonde entraînée sur étiquettes permutées : AUROC attendue 0,50 ± 0,03.
  - Sac de mots sur le contexte, évalué en transfert de déclencheur. S'il égale la sonde, celle-ci lit le texte et S4 est falsifié pour ce banc.
  - Régime consigne : exécution honnête dont le message système mentionne le sabotage pour l'interdire. Si la sonde s'y déclenche, elle détecte la mention et non l'intention.
- **Falsification.**
  - AUROC ≥ 0,70 en transfert, supérieure au sac de mots d'au moins 0,10 : H_B est falsifiée.
  - AUROC ≤ 0,55 : H_A et R2 sont falsifiées. La longueur ne donne alors aucun avantage propre aux activations.
  - Entre les deux : indécis.
- **Second volet de R2.** Si d′ continue de croître de T = 200 à T = 800 (rapport ≥ 1,2), le plafonnement que j'attends est réfuté. Ce serait favorable au défenseur.
- **Limite.** Un adaptateur à déclencheur est un organisme modèle. Rien n'établit qu'une intention non entraînée se représente de la même façon. Le résultat borne ce que la sonde peut faire dans un cas favorable, pas dans le cas réel.

### E3 : structure de la tâche (α)

- **H_A.** Le taux de sabotage réussi et non détecté (verdict final inversé, aucune alerte à 5 % avec tous les instruments de E1 et f = 5 %) augmente d'au moins 20 points entre T = 50 et T = 800 en variante série. Il varie de moins de 10 points en variante additive.
- **H_B.** Les deux variantes se comportent de la même façon (toutes deux plates ou toutes deux croissantes). La structure ne compte pas et la décomposition α/β est fausse.
- **Contrôle négatif.** Taux de verdicts inversés par les seules erreurs honnêtes, par variante et par T. S'il dépasse 80 % en série à T = 800, on retombe sur l'issue « agent honnête déjà en échec ».
- **Falsification.**
  - Motif « série monte, additif plat » : H_B est falsifiée.
  - Motifs identiques : H_A et R3 sont falsifiées.
  - Additif qui monte seul : tout le modèle est falsifié.

---

## (c) Mesure minimale par instrument

Dans tous les cas, « fonctionne » signifie battre la meilleure vérification mécanique de la liste, à fausses alertes égales, sur les cas honnêtes appariés.

### 1. Observation du texte (moniteur par action, modèle de confiance)

- **Mesure minimale.**
  - AUROC par acte, actes sabotés contre erreurs honnêtes.
  - Taux de détection par trajectoire à 5 % et 1 % de fausses alertes, avec agrégation par maximum et par somme.
- **Cas honnêtes appariés.**
  - Erreurs spontanées du modèle honnête sur les mêmes fiches, et non ses actions correctes.
  - Exécutions à dose nulle.
- **Vérifications mécaniques à battre.**
  - Longueur et perplexité de l'action sous un modèle de référence.
  - Divergence avec la ré-exécution de la même action en contexte neuf.
  - Simple comptage d'écarts de format.
- **Critère.** Détection supérieure d'au moins 10 points à la meilleure vérification mécanique, à fausses alertes égales, pour au moins trois longueurs sur cinq.

### 2. Activations (sonde linéaire, couches médianes, dernier jeton de l'action)

- **Mesure minimale.**
  - AUROC par action, séparément sur actes sabotés et sur actions bénignes.
  - Détection par trajectoire à 5 % de fausses alertes en fonction de T.
  - Corrélation ρ.
- **Cas honnêtes appariés.**
  - Déclencheur placebo, mêmes poids.
  - Mention de sabotage interdite.
  - Erreurs honnêtes.
- **Vérifications mécaniques à battre.**
  - Moniteur de texte à fausses alertes égales.
  - Sac de mots sur le contexte, en transfert.
  - Sonde à étiquettes permutées.
  - Direction aléatoire.
- **Critère.** Bat le texte et le sac de mots d'au moins 10 points de détection en transfert de déclencheur. Les fausses alertes sur « mention interdite » restent à 10 % ou moins.

### 3. Exécutions de comparaison (n ∈ {3, 5, 10})

- **Mesure minimale.**
  - Fausses alertes réelles contre nominales quand les seuils sont fixés sur n exécutions.
  - Puissance du z-score du résultat final.
  - Puissance de la divergence pas à pas avec les sorties de référence.
- **Cas honnêtes appariés.** Exécutions honnêtes disjointes, avec graines et ordre des fiches différents.
- **Vérification mécanique à battre.** Aucune : c'est la ligne de base des autres instruments. Elle doit cependant battre un seuil fixé sans aucune exécution de comparaison (taux d'erreur supposé a priori).
- **Critère.** Fausses alertes réelles à 2 fois le nominal ou moins dès n = 5. Sinon tout seuil par trajectoire est non calibrable avec « quelques » exécutions, et c'est un résultat en soi.

### 4. Vérification coûteuse (fraction f ∈ {1 %, 5 %, 10 %})

- **Mesure minimale.**
  - Détection à 5 % de fausses alertes pour l'allocation aléatoire et pour l'allocation ciblée par le score du moniteur.
  - Statistiques : somme signée des écarts, test de signe.
- **Cas honnêtes appariés.** Exécutions honnêtes avec leurs erreurs naturelles, auditées à la même fraction.
- **Vérification mécanique à battre.** Audit aléatoire avec test binomial sur le nombre d'erreurs.
- **Critère.** L'allocation ciblée bat l'aléatoire d'au moins 10 points à f égal. Sinon l'observation ne sert pas à diriger l'audit.

Deux réserves sur ce tableau de mesures :
- L'oracle d'audit est exact par construction. Ce banc ne mesure donc pas la fiabilité d'un vérificateur réel (S6), ni sa propension à prendre une erreur honnête pour un sabotage. C'est une lacune assumée, à combler sur une tâche non synthétique.
- L'allocation ciblée a un risque propre : un adversaire qui connaît la règle déplace ses actes vers les actions à faible score. Le régime pantin permet de le simuler à peu de frais.

---

## (d) Ancrage matériel

Tout ce qui suit est illustratif : les faits ne fixent que « modèle ouvert de huit milliards de paramètres » et « deux mois ».

**Modèles.**
- Agent : un modèle ouvert d'instruction de 8 milliards de paramètres, par exemple Llama-3.1-8B-Instruct (mon choix, non imposé par les faits).
- Moniteur de texte : le même modèle sans adaptateur, ou un modèle ouvert plus petit.
- Adversaire affiné : adaptateur LoRA de rang 16 sur données synthétiques (quelques milliers d'exemples).

**Échafaudage.**
- Contexte borné par action : message système, état résumé et fiche courante, soit environ 1 500 jetons en entrée et 100 en sortie.
- Ce choix sépare T de la longueur de contexte, mais il rend la consigne ou le déclencheur visible à chaque appel. Le signal d'état a donc une voie triviale, d'où les contrôles placebo et mention.

**Volume.**
- Environ 2 300 trajectoires : cinq longueurs × (100 honnêtes + 12 cellules k×D × 30).
- Longueur moyenne d'environ 310 actions, soit environ 1,1 milliard de jetons traités.
- Activations : trois couches, un vecteur par action, demi-précision, soit environ 20 Go.

**Calcul et coût.**
- 300 à 600 heures sur un GPU de 40 à 80 Go avec inférence par lots.
- Affinage et sondes : moins de 50 heures.
- Avec une marge ×3 pour les reprises, environ 2 000 heures-GPU, soit 3 000 à 5 000 $ au tarif de location courant.

**Calendrier.**
- Semaines 1-2 : banc, oracle, contrôle pantin, vérification de S1 et S10, préenregistrement des seuils.
- Semaines 3-4 : E1 en régime consigne.
- Semaines 5-6 : affinage et E2.
- Semaines 7-8 : E3, analyses de sensibilité (n, f), rédaction.

**Critères d'arrêt précoce (fin de semaine 2).**
- Le pantin ne rend pas β ≈ 0,5.
- Le modèle honnête échoue à plus de 80 % dès T = 200.
- Le sabotage par consigne est détecté acte par acte à AUROC > 0,95.

Dans chacun de ces cas, le banc ne peut pas répondre à la question et il faut le dire plutôt que poursuivre.

FIN-DE-CELLULE