# Proposition B — Tour III.3 : Réponse aux critiques

## Préambule d'intégrité

Les trois critiques croisées (A, C, D) sont complètes ; aucune section n'est coupée. Je ne résume ni ne fusionne les critiques des autres : je les traite une par une, en les nommant. Tout chiffre que j'introduis est marqué **illustratif** sauf renvoi explicite à la synthèse. Les statuts des faits sont ceux de la synthèse ; je n'en change aucun.

---

## (a) Réponse à chaque critique visant la proposition B

### Critiques de A sur B

**A.1 — N1, transposition d'erreur type (déclencheur à 0,5 calibré sur la mauvaise grandeur).**
**Acceptée.** A a raison : l'erreur type de 0,04 à 0,11 appartient à la nouvelle grandeur ; l'ancienne a une erreur type de 0,29 à 0,60 (synthèse, recalculs N1). Mon déclencheur à 0,5 sonnerait sous lois égales avec probabilité 0,09 à 0,40 par case (recalcul de A, conforme). **Correction :** le déclencheur d'audit sur l'ancienne grandeur est retiré comme instrument décisionnel. Il est remplacé par un rapport descriptif de l'ancienne grandeur avec son erreur type par statut × condition — aucun seuil, aucune porte. Le risque de séparation par la rareté est éprouvé uniquement par le plancher d'effectif par statut de la nouvelle grandeur (condition A, convergée à quatre au tour 1) et, si l'épreuve F′ est réalisable (divergence 1), par celle-ci.

**A.2 — N5, E1 : hypothèses non exclusives, contrôle vrai par construction.**
**Acceptée en partie.** A a raison que le contrôle négatif (version (b), distance zéro) est vrai par construction — il vérifie le harnais, pas sa sensibilité. A a aussi raison que l'issue « 1 000 permutations identiques » ne falsifie pas H_B si le canal du journal reste ouvert. **Correction :** j'ajoute un contrôle positif : version antérieure à fuite connue (apport de C au tour 1, repris par A) avec estimation de P(divergence) sur la même famille de permutations. Si le contrôle positif ne diverge pas, le test est aveugle et ne tranche pas. **Je maintiens** que le test d'invariance est la pièce nécessaire, mais j'admets qu'il ne tranche que sur la sortie et l'ordre des appels, pas sur le journal ni les décisions aval. Ce qui divise (a) et (b) est plus large que ce que E1 mesure.

**A.3 — N11, E3 n'est pas un duel.**
**Acceptée.** Un calcul de puissance analytique n'est pas une expérience ; aucune donnée ne le falsifie. Mon E3 était un énoncé déguisé en duel. **Correction :** E3 est requalifié en **recalcul de faisabilité**, non en duel. Le duel de N11 est celui que la convergence du tour 1 fournit : exécution de l'oracle sur ponts plantés et leurres, avec la métrique taux de détection / taux de fausse alerte sur les quatre familles de leurres, à un effectif à déterminer par le pilote de variance (apport de D). Ce duel oppose H_A (l'oracle à deux parents détecte les ponts plantés au-dessus du hasard apparié à p < 0,05, test de permutation par lots entiers) à H_B (il ne les détecte pas). L'issue H_B falsifie la capacité de l'oracle ; l'issue H_A ne falsifie pas l'inutilité mais établit la sensibilité.

**A.4 — N3/N9, fusion de deux instruments.**
**Acceptée.** J'avais regroupé le substitut S31 (N3) et le modèle Gu-Krenn (N9) dans une seule spécification de mesure minimale, avec le seuil B-i ≥ 0,85 transporté au substitut. A a raison : ce sont deux populations de négatifs, deux estimands d'aire, deux objets distincts dans les pièces (le substitut a une confiance d'auteur de 0,4, RAPPORTÉ). **Correction :** les deux instruments sont séparés.
- **N9 (Gu-Krenn, domaine propre)** : aire sur échantillon aléatoire, seuil B-i ≥ 0,85, population à fin 2022, fenêtre 2023–2026 — inchangé.
- **N3 (substitut S31)** : aire sur négatifs appariés en degré × âge (selon la population définie par la coupure temporelle), seuil à geler sur **cette** loi avant le test. Le seuil B-i n'est pas transportable.

**A.5 — N6 DL-12, E2 : métrique conditionnelle.**
**Acceptée.** Mon H_B (« s'abstient presque toujours ») n'est pas mesurée par le taux d'inclusion parmi les ensembles acceptés non vides. Si la méthode s'abstient dans 95 % des mondes, le taux conditionnel est instable et sans rapport avec la performance globale. **Correction :** E2 mesure le couple (π = part d'ensembles non vides ; inclusion de la cause parmi les non vides). H_B est reformulée : π < π_min (gelé d'avance), **ou** inclusion du leurre > α. La condition π ≥ π_min est un prérequis de jugeabilité ; en dessous, le verdict est « abstention dégénérée », prononcé sur π seul — reprise exacte de la structure proposée par A.

**A.6 — N6 DL-10, condition incohérente.**
**Acceptée.** Retenir (1) « aucune condition » puis exiger un rapport descriptif est contradictoire : rapporter un résultat suppose de le calculer. **Correction :** mon verdict DL-10 est reformulé : **tenue**, l'épreuve n'étant pas exécutée (5,0 heures, SUPPOSÉ, pour un test presque vrai par construction). Je retire la condition de rapport descriptif. La limite écrite reste.

**A.7 — N4, structures séquentielles « imposées ».**
**Rejetée en partie.** A affirme que mon argument « repose sur l'inverse du fait servi ». La synthèse écrit bien « les trois structures séquentielles imposées par le texte servi » (N4, divergence 4). Cependant, la synthèse rapporte aussi que « l'argument d'exclusion vaut aussi pour les structures séquentielles » — ce qui n'est pas la même chose que « elles sont imposées au même titre que les jeux de données ». Les jeux de données sont imposés mécaniquement (tout auteur les utilise) ; les structures séquentielles sont imposées par le plan mais leur adoption dans une fiche particulière implique un choix méthodologique (l'auteur les adapte à son objet). **Je concède** néanmoins que l'argument est faible : la distinction « mécaniquement imposé » / « imposé par le plan » n'est pas tranchée par les pièces. **Position maintenue avec réserve :** garder les trois structures séquentielles avec la limite écrite, mais le directeur peut les retirer sans que cela change les paires de niches éligibles (fait vérifié, synthèse N4).

**A.8 — N11, Fisher sur l'oracle à petit effectif.**
**Acceptée.** Le même défaut que le quartile retiré au tour 1. À quatre ponts plantés par lot et un seul lot, le test exact n'atteint pas p < 0,05. **Correction :** le test de Fisher est retiré comme seuil de l'oracle. L'oracle est évalué par le test de permutation par lots entiers (convergence du tour 1, apport de C), sur un nombre de lots à déterminer par le pilote de variance.

---

### Critiques de C sur B

**C.1 — N1, abandon de falsifiabilité (absence de duel).**
**Acceptée.** Après le retrait de mon duel et du déclencheur mal calibré, je n'opposais effectivement plus rien à rien sur N1. **Correction :** le duel de N1 est reconstruit.

**Duel révisé pour N1 :**
- **H_A :** La version nouvelle, avec graines entièrement nouvelles et écart déclaré, passe les seuils de la nouvelle grandeur sur tous les statuts × conditions ayant un effectif ≥ n_min (plancher gelé), et l'ancienne grandeur rapportée sans seuil ne montre aucun statut rare dont l'écart est supérieur à 3 erreurs types de la nouvelle grandeur pour ce même statut.
- **H_B :** La version nouvelle échoue sur au moins un statut (n_min atteint), ou l'ancienne grandeur montre un écart supérieur à 3 erreurs types de la nouvelle grandeur sur un statut rare.
- **Falsification de H_A :** échec de la nouvelle grandeur ou signal de l'ancienne → la redéfinition ne ferme pas le risque.
- **Falsification de H_B :** tous les seuils passent et l'ancienne grandeur est silencieuse → la redéfinition est défendable.
- **Contrôle :** mondes à lois égales (le taux de déclenchement du critère de l'ancienne grandeur sous le nul doit être ≤ α). Ce contrôle manquait (critique de A point (c)).

**C.2 — N4 CA1-04, contradiction avec les faits servis.**
Même réponse que A.7. **Concédé en partie**, position maintenue avec réserve. La limite écrite reconnaît explicitement le problème. Je ne prétends pas que la synthèse me soutient : elle écrit l'inverse. Mais la distinction entre « imposé mécaniquement » et « imposé par le plan » n'est pas tranchée, et je la signale.

**C.3 — N3/N9, confusion d'instruments.**
**Acceptée.** Même réponse que A.4.

**C.4 — Ponts plantés et plafonds scellés (N11).**
**Transformée en test.** C affirme que les fusions ajoutées pour les ponts plantés modifient le dénominateur de consommation et l'ordre des appels. C'est une question de fait : si les ponts sont traités dans une **étape protégée** séparée (hors du compteur de fusions du pré-pilote), le plafond n'est pas touché. Si l'orchestrateur ne permet pas cette séparation, C a raison. **Test :** l'étape protégée est-elle implémentable sans modifier le compteur de fusions ni l'ordre des appels de la chaîne principale ? Si oui, la fuite structurelle est fermée. Si non, les ponts plantés passent par les préenregistrements de la bisociation v3 et d'E1′ (recommandation de conv-audit), hors du pré-pilote.

**C.5 — Déclencheur d'audit à 0,5 : spécificité effondrée.**
**Acceptée.** Même critique que A.1. Déjà corrigé ci-dessus : le déclencheur est retiré.

**C.6 — E3 ultraconservateur.**
**Acceptée.** La domination par non-chevauchement d'intervalles à 95 % revient à un test au seuil effectif ≈ 0,006 ; à n = 8, seules les réalisations extrêmes passent (puissance < 0,015, illustratif — calcul de C conforme). Cela renforce la conclusion « non concluant à 8 fusions ». E3 est requalifié en recalcul de faisabilité (voir A.3).

**C.7 — Rapport descriptif sans aveuglement (N11).**
**Acceptée.** Un rapport descriptif non aveuglé laisse un degré de liberté post hoc total. **Correction :** le rapport descriptif est servi avec les noms de bras remplacés par des lettres tirées au hasard (protocole d'aveuglement). Le directeur lit les classements sans connaître l'identité des bras avant d'écrire sa décision. L'aveuglement est levé après.

---

### Critiques de D sur B

**D.1 — N1, calibration de l'audit par la mauvaise variance.**
**Acceptée.** Même que A.1. Corrigé ci-dessus.

**D.2 — N4, la limite écrite ne répare pas l'estimand.**
**Acceptée en partie.** D a raison que la limite au rapport ne modifie pas le numérateur. Mais je maintiens que retirer les structures ne change pas les paires de niches éligibles (synthèse, vérifié par code) — seule la probabilité de partage change. Ma position reste « garder avec réserve ».

**D.3 — N5, le contrôle négatif ne teste pas la sensibilité.**
**Acceptée.** Même que A.2. Corrigé : contrôle positif ajouté.

**D.4 — DL-12, hypothèses non exhaustives.**
**Acceptée.** Même structure que A.5. Corrigé : reformulation avec le couple (π, inclusion).

**D.5 — N11, E3 variance inadaptée au contraste.**
**Acceptée.** Mon z = 0,25/0,177 utilise l'erreur type d'un seul bras au lieu du contraste de deux bras. L'erreur type du contraste à n = 8 : √(0,25/8 + 0,1875/8) ≈ 0,234 (recalcul de A, conforme). z ≈ 0,25/0,234 ≈ 1,07, puissance unilatérale ≈ Φ(1,07 − 1,645) ≈ 0,28 (illustratif). La conclusion « non concluant » subsiste mais les chiffres étaient faux. E3 requalifié en recalcul (A.3).

**D.6 — N11, Fisher suppose une échangeabilité non défendue.**
**Acceptée.** Les paires d'un même lot sont dépendantes (elles partagent les mêmes fiches). Le test de Fisher au niveau des paires est invalide. Corrigé en A.8 : permutation par lots entiers.

---

### Remarque transversale de A sur N5

A observe que les quatre espèces convergent sur la mesure d'invariance mais rendent trois verdicts différents (B : indécidable ; C : tenue ; D : renversée), et que le journal est invariant par construction sous permutation de clé. **Acceptée comme diagnostic.** Le test d'invariance de sortie ne teste pas le canal du journal (le processus qui détient la clé écrit l'attestation). Ce qui sépare (a) et (b) est plus large que la sortie. Je maintiens « indécidable sans la pièce » mais j'admets que la pièce ne trancherait que la composante « sortie », pas la composante « journal ». Si le contrôle positif (version antérieure à fuite connue) ne diverge pas, la question entière est non jugeable par ce test et (b) s'impose par précaution.

---

## (b) Expériences corrigées

### Duel D-N1 (N1, révisé)

- **H_A :** La version nouvelle passe les seuils de la nouvelle grandeur sur tous les statuts × conditions ayant un effectif ≥ n_min, et l'ancienne grandeur ne montre aucun statut rare dont l'écart dépasse 3 erreurs types de la nouvelle grandeur pour ce statut.
- **H_B :** Échec de la nouvelle grandeur sur au moins un statut, ou signal de l'ancienne grandeur (écart > 3 σ_nouvelle).
- **Falsification de H_A :** issue H_B. **Falsification de H_B :** issue H_A.
- **Contrôle sous le nul :** mondes à lois égales, taux de déclenchement ≤ α.
- **Contrôle positif manquant :** mondes à rareté plantée sans fuite (taux de détection).
- **Ancrage :** 300 mondes, seconde graine de flux, processeur, 0 USD.

### Duel D-N5 (N5, révisé)

- **H_A :** La sortie et l'ordre des appels sont identiques sous 1 000 permutations de clé à comptes agrégés constants.
- **H_B :** Au moins une permutation produit une sortie ou un ordre différent.
- **Falsification de H_A :** issue H_B → (a) ne ferme pas le risque de sortie, (b) s'impose.
- **Falsification de H_B :** issue H_A → la fuite est absente de la sortie (canal du journal non couvert ; si le contrôle positif ne diverge pas non plus, le test est aveugle et (b) s'impose par précaution).
- **Contrôle positif :** version antérieure à fuite connue, P(divergence) estimée.
- **Contrôle négatif :** deux exécutions à même clé (déterminisme).
- **Ancrage :** code de l'orchestrateur, quelques minutes de processeur (illustratif), 0 USD.

### Duel D-N11 (N11, oracle des ponts plantés)

- **H_A :** L'oracle à deux parents détecte les ponts plantés au-dessus du hasard apparié en degré de parenté apparent, test de permutation par lots entiers, p < 0,05.
- **H_B :** Il ne les détecte pas.
- **Falsification de H_A :** issue H_B → l'oracle est insensible.
- **Falsification de H_B :** issue H_A → l'oracle est sensible (ne prouve pas l'utilité mais établit la détectabilité).
- **Leurres :** quatre familles (convergées au tour 1).
- **Contrôles :** bras fantôme (tirage au hasard) ; bras « tout rendre » (critique de D) ; bras « récitation des parents » (critique de D) ; lot sans pont planté (critique de A).
- **Ancrage :** effectif à déterminer par le pilote de variance (apport de D) ; le rapport est servi avec noms de bras aveuglés (critique de C).

### Duel D-DL12 (DL-12, monde jouet, révisé)

- **H_A :** La méthode de prédiction invariante sous centrage par strate (option 1) inclut la cause plantée avec π ≥ π_min (gelé) et n'inclut pas le leurre (taux ≤ α).
- **H_B :** π < π_min (abstention dégénérée), ou inclusion du leurre > α.
- **Falsification de H_A :** issue H_B → l'avantage de l'option 1 est absent.
- **Falsification de H_B :** issue H_A → l'option 1 est confirmée.
- **Contrôle négatif :** monde à cause d'effet nul (taux d'acceptation ≤ α) ; monde à confusion cachée (abstention ≥ seuil gelé). La « permutation de l'étiquette de cause » (proposée par C) n'est pas un nul valide (A, D) et est remplacée.
- **Ancrage :** script du semi-réel, quelques dizaines de secondes, 0 USD (conforme aux faits).

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi

1. **N1, option B :** accord à quatre, toutes les variantes de générateur échouent, la redéfinition est la seule voie. Conditions convergées : graines nouvelles, écart déclaré, plancher d'effectif par statut, ancienne grandeur rapportée sans seuil. Le déclencheur à 0,5 que j'avais proposé est invalide (erreur type transposée, spécificité effondrée). **Recommandation tenue sous les conditions du tour 1, déclencheur retiré.**

2. **N3, D-j oui :** accord à quatre, le substitut n'est pas une reproduction et le vocabulaire du contrôle est absent. Conditions : nom « substitut », source empreintée, gain minimal gelé, coupure temporelle. Le seuil B-i ≥ 0,85 n'est pas transportable au substitut (erreur mienne, corrigée).

3. **N4, option (a) :** accord à quatre, le pré-pilote éprouve la chaîne et non le profil. CA1-04 non résolu ; ma position (garder les séquentielles) est la plus faible du tour et contredit la lettre de la synthèse.

4. **N6 :** onze accords larges sur treize décisions. Mon renversement sur DL-3 (vers (2) avec déclencheur) et DL-9 (vers (2) descriptif) élimine deux des trois divergences où j'étais seul. DL-12 : je maintiens (1) sous condition de test sur monde jouet (convergence à trois).

5. **N9, option (a) :** accord à quatre, les deux instruments (Gu-Krenn et substitut) sont séparés.

6. **N10, option (b) :** accord à quatre, les éléments nouveaux ne changent pas l'option.

7. **N11 :** la course ne décide aucun retrait à huit fusions (quatre calculs indépendants, conclusion robuste aux hypothèses d'effet). L'oracle à deux parents et la domination avec confiance sont convergés à quatre. Le test de rang est éliminé. Le rapport descriptif est aveuglé.

### Ce qui n'est pas établi

1. **N5 :** la divergence 2 contre 2 n'est pas tranchable par le test d'invariance seul — le canal du journal est invariant par construction. Si le contrôle positif ne diverge pas, (b) s'impose par précaution.

2. **N1, épreuve du risque de rareté :** la divergence 1 (hors/dans l'invocation) est non résolue. Mon déclencheur étant retiré, aucune épreuve extérieure à la porte ne subsiste dans ma proposition.

3. **N4 CA1-04 :** la distinction « imposé mécaniquement / imposé par le plan » n'est tranchée par aucune pièce.

4. **N11, transport :** aucune forme de règle (ordinale, équivalence, descriptive) n'est applicable à l'effectif budgété ; la course 2 est descriptive de fait.

5. **N11, ponts plantés et pré-pilote :** la fuite structurelle entre étape protégée et compteur de fusions est une question de fait non tranchée.

### L'expérience à faire en premier

**Le test d'invariance de N5** (duel D-N5 révisé). Il coûte 0 USD, prend quelques minutes de processeur, et son issue **tranche une divergence 2 contre 2 qui bloque le gel du pré-pilote** : si la sortie varie avec la clé, (b) s'impose et le chemin critique avance ; si elle ne varie pas et que le contrôle positif diverge, (a) est défendable sous amendement ; si le contrôle positif ne diverge pas non plus, le test est aveugle et (b) s'impose par précaution. Dans tous les cas, l'issue fait avancer. Toutes les autres expériences (N1, DL-12, N11 oracle) dépendent de textes qui ne sont pas encore gelés ; N5 porte sur du code déjà écrit.

FIN-DE-CELLULE