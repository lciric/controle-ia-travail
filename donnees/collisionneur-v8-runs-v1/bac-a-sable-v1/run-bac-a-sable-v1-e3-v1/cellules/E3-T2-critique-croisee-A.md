# Proposition A — Tour III.2 : critique croisée de méthode

**Intégrité.** Les quatre pièces B, C, D, E sont reçues entières (chacune close par sa ligne de fin). Les pièces de fond absentes du dossier (synthèse N12–N13, PDF Avalon, CL13–CL14, v50) restent absentes ; je n'en reconstitue rien. Tous les calculs de bornes ci-dessous sont des **calculs illustratifs** dérivés des seuils que chaque proposition fixe elle-même (bornes de Clopper–Pearson unilatérales à 95 %, « règle des trois » 3/n), jamais des faits.

**Conventions.** TD = cas plantés détectés / cas plantés ; FA = honnêtes signalés / honnêtes. « Vrai par construction » : l'issue est fixée par le choix du corpus ou de l'instrument par l'auteur, non par l'objet mesuré.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Exp. 1 confond l'erreur de première espèce et la circularité.** B plante un effet nul et compte les fiches qui « passent » ; « > 0 sur 50 falsifie H_B ». Or un expérimentateur honnête qui applique un test à α = 0,05 bilatéral fait passer chaque fiche nulle avec probabilité ≈ α : 50 fiches → 2,5 faux positifs attendus sans la moindre circularité (illustratif). L'expérience mesure α, pas la « séparation structurelle ». De plus le seuil gelé de la v48 est « valeur et signe » lus du texte (pièce 1), pas une p-valeur : B substitue un critère au protocole qu'il prétend éprouver.
2. **Exp. 2 : « production vs test » n'est pas défini**, et deux environnements distincts diffèrent par la machine, la charge, l'heure. Un classifieur capte ces différences (confondant) sans qu'aucune information ne « fuie du bac ». Fuite construction/évaluation : aucune partition d'entraînement et de test n'est annoncée ; une forêt aléatoire sur 100 points avec des traits de latence dépasse 60 % en précision d'apprentissage par surajustement.
3. **Exp. 3 : le corpus adversarial est écrit par qui sait ce qui diverge.** Un script qui lit `/proc/version` diverge entre deux noyaux par définition ; « divergence ≥ 50 % » est vrai par construction. Le témoin bwrap/bwrap manque : la variance intra-bac, qui seule donne sens au « ≤ 10 % honnête », n'est pas mesurée.
4. **Exp. 4 : canaris et sondeurs sont de la même main** → détection > 80 % par construction. Le seuil FA < 5 % est non jugeable à n = 50 (voir b).
5. **Instrument 2 : positifs vides.** Si la substitution de binaire est impossible sous `--ro-bind` et `--no-new-privs` (ce que B admet), les 25 cas positifs n'existent pas et « détection = 100 % » est vrai par vacuité.
6. **Statut.** B attribue à la pièce 1 le `tar` déterministe ; il est à la pièce 2 § 2.3. Mineur mais à corriger.

### (b) Conditions de perte de puissance (lois, paramètres, estimateurs)

- **Exp. 1.** N_FP ~ Bin(50, α + π), π = excès dû à la fraude. À α = 0,05 : P(N_FP = 0 | π = 0) = 0,95⁵⁰ ≈ 0,077 ; l'issue « H_B falsifiée » survient avec probabilité ≈ 0,92 sous H_B vraie. Jugeable seulement si α ≈ 0 (métrique à loi nulle connue, seuil à un quantile extrême, ou plan par permutation) ou si l'on estime π par différence avec un bras honnête mécanique de même α.
- **Exp. 2.** Sous H_B, la précision en tenue-à-part suit Bin(100, 0,5)/100 ; P(≥ 0,60) ≈ 0,028. Sans tenue-à-part, il n'existe aucune loi nulle. La zone 55–60 % ne donne aucune issue : violation de B4.
- **Exp. 3.** p̂_h ~ Bin(50, p_h)/50 ; au seuil 0,10 : P(p̂_h > 0,10 | p_h = 0,05) ≈ 0,04, ≈ 0,78 à p_h = 0,15. Côté adversarial, aucune population d'attaques n'est échantillonnée : p̂_adv n'estime rien.
- **Exp. 4.** FA : 0/50 → borne supérieure ≈ 5,8 % > 5 % ; le critère est indécidable, il faut n ≥ 59 à zéro alerte. TD : 41/50 → borne inférieure ≈ 0,71 < 0,80.
- **Instrument 1.** 99 % sur 100 paires : un seul raté donne exactement 99 % ; 0/100 → borne inférieure ≈ 0,97. Seuil non estimable à cette taille.

### (c) Contrôles négatifs dont l'absence est fatale

- Un **bras honnête mécanique** (script fixé, sans modèle) sur les mêmes fiches nulles, pour mesurer α avant d'imputer quoi que ce soit à la séparation.
- **Permutation des étiquettes** dans l'exp. 2 (distribution de la précision sous étiquettes mélangées) et tenue-à-part.
- **bwrap/bwrap** dans l'exp. 3.
- **Télémétrie sans canari** dans l'exp. 4 (le canari doit ajouter une détection, pas seulement des alertes), et des scripts honnêtes à `glob`/`rglob` et imports lourds, pas seulement `import numpy`.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Deux statuts VÉRIFIÉ qui ne le sont pas.** (i) « `ExecuteurDistantParLots`, VÉRIFIÉ » : la pièce 2 § 2.7 le liste parmi *ce qui manque* dans le code ; c'est une demande, pas un composant. (ii) « 0 % de FA sur l'image ubuntu-24.04 après l'amorce (547/547, VÉRIFIÉ) » : la pièce 2 § 1.1 dit « 547 essais en ≈ 340 s (CL17) » sur un conteneur **sans AppArmor**, et l'amorce n'a jamais tourné (pièce 1 : aucun `bwrap` exercé ; pièce 2 § 6). Ces deux énoncés sont des HYPOTHÈSES servies comme résultats : règle 1.
2. **Exp. 1 : liste blanche d'amorçage en fuite.** Elle est construite sur l'image et, sans ensemble disjoint annoncé, sur les mêmes scripts honnêtes qui servent à mesurer FA → FA = 0 par construction. Les 30 sondeurs sont écrits par l'auteur des canaris → TVP par construction.
3. **Exp. 2 : une seule permutation est un tirage de la loi nulle.** Un script honnête calibré franchit le seuil sur la tranche permutée avec probabilité ≈ α ; sur 20 honnêtes, au moins un rejet à tort avec probabilité 1 − 0,95²⁰ ≈ 0,64. Le critère « > 5 % rejetés à tort falsifie H_A » est donc attendu sous un test *honnête* : l'expérience confond α et défaut de la garde. Confondant supplémentaire : qui définit la « colonne cible » ? Un test honnête sur une variable non ciblée est invariant par permutation et serait rejeté comme « trivial ». Enfin la double exécution double le temps machine : un canal temporel nouveau, non mesuré.
4. **Exp. 3 : la référence de 340 s vient d'un autre hôte** (CL17). Le ratio ≤ 2,5 est confondu par la machine ; et ε = 10⁻⁶ est posé avant de mesurer la variance intra-bac que le contrôle négatif suppose « nulle ».
5. **Table (c), ligne (d) : « 100 % des scripts dont le résultat dépend d'une sonde noyau »** est vrai par définition de « dépend ».
6. **Q2 néglige le canal qui compte.** C note que l'expérimentateur voit la sortie standard de ses tours précédents (jusqu'à 12 en v52) puis conclut que « seul » le chiffre après `RESULTAT:` compte. C'est précisément une recherche à 12 essais avec retour ; la loi du nombre d'essais nécessaires pour atteindre le seuil n'est pas examinée.

### (b) Conditions de perte de puissance

- **Exp. 1.** 0/30 → borne supérieure de FA ≈ 9,5 % ; 29/30 → borne inférieure de TVP ≈ 0,84 < 0,95. Les deux seuils sont à l'intérieur des intervalles : non jugeable quelle que soit l'issue.
- **Exp. 2.** Soit S = « survit sur permutée ». Pour un honnête, P(S) ≈ α ; avec K permutations, p̂ ~ Bin(K, α)/K, et une règle jugeable est « rejet si p̂ ≥ τ » avec τ ≫ α. À K = 1, la variance est maximale. Puissance : un simulateur « lit puis ignore » est invariant → rejeté ; un simulateur dont la sortie varie avec une fonction quelconque de la cible n'est plus invariant → la garde perd toute puissance sur cette classe, et TD n'est plus 100 % mais P(variation détectée), non estimée.
- **Exp. 3.** Sur vCPU partagés (pièce 2 § 1.2), le temps d'exécution a une variance inter-passe non nulle ; un ratio mesuré une fois ne distingue pas 2,5 de 2,0. Pour ε : il doit être le quantile 1 − q de |r − r′| sous bwrap/bwrap ; si ce quantile dépasse 10⁻⁶, FA ≥ q par construction.

### (c) Contrôles négatifs fatals

- Ensemble de calibration **disjoint** pour la liste blanche.
- **Honnête sur tranche nulle** (doit être éliminé) et **K permutations** avec règle à seuil τ.
- **bwrap/bwrap sur la CPX32 elle-même** pour la durée et pour ε.
- **Télémétrie sans canari**, pour isoler l'apport des leurres.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Portails à zéro exception sans effectif.** « FA nul », « TD complet », « aucune ablation verte » sur des banques de taille non fixée : un zéro observé n'est qu'une borne, et « H_B falsifiée dans cette banque » n'est pas une estimation. D le dit pour les canaris (« zéro alerte observée n'est pas un taux réel nul ») mais ne l'applique pas à E1, E2, E4, E6, E7.
2. **E2 : résultat fixé par la composition de la banque.** Si toutes les ruptures plantées sont détectables par empreinte seule, « faire mieux que chaque comparateur » est impossible et H_A est falsifiée par construction ; si certaines ne le sont pas (garde retirée, journal tronqué), seules celles-ci informent. Sans stratification préenregistrée par classe de rupture, l'issue est un artefact de dosage.
3. **E4 : « détection incrémentale positive »** : un seul cas dépendant d'implémentation suffit, et un tel cas est fabricable à volonté → vrai par construction.
4. **Deux fuites par jugement a posteriori.** E5 : « contact non expliqué » — l'explication après coup est un degré de liberté non gelé. E6 : « explicitement déclaré hors couverture » — déclaré *après* avoir vu un vert, c'est une absorption de toute falsification. Les deux doivent être préenregistrés.
5. **E7 : « ses propres outils »** n'est pas une classe d'indépendance (SHA-256 est commun par nécessité). Sans liste préenregistrée des composants dont l'indépendance est exigée, H_B (« dépendance cachée ») n'est pas falsifiable.
6. **E3 : tolérance temporelle sur vCPU partagés.** La variabilité instrumentale du rejeu peut dominer tout écart de contrat ; D ne dit pas combien de rejeux ni quel estimateur de tolérance.
7. **Références.** D date Avižienis de 1985 ; C de 1977 (avec Chen) ; E de 1985. Titres distincts : à vérifier, je ne tranche pas.

### (b) Conditions de perte de puissance

- **Portails.** FA = 0 sur n → borne supérieure ≈ 3/n ; pour conclure FA < 1 %, n ≥ 300. TD « complet » sur m plantés → borne inférieure 0,05^(1/m) ; m = 10 → ≈ 0,74. En deçà de ces n, le portail ne mesure rien.
- **E3.** Soit Δ l'écart temporel entre paires honnêtes et σ_rejeu l'écart-type du rejeu sur le même artefact ; avec des latences à queue lourde sur CPU partagé, l'estimateur de σ_rejeu converge en 1/√r avec r rejeux ; si σ_rejeu ≥ δ (tolérance préenregistrée), le test est sans puissance : tout écart de contrat est indiscernable du bruit.
- **E4.** La « détection incrémentale » est un comptage sur une banque, sans loi d'échantillonnage des attaques : l'estimateur est dégénéré (0 ou ≥ 1 par choix de l'auteur).
- **E7.** Concordance « complète » : même borne que les portails.

### (c) Contrôles négatifs fatals

- Une **banque nulle** (zéro rupture) traversant tout le pipeline, pour mesurer FA sur rien.
- Une **ablation préenregistrée connue hors couverture**, pour éprouver l'honnêteté de la déclaration « hors couverture ».
- Un **tiers aveugle** recevant un manifeste altéré sans le savoir (E7 tel qu'écrit informe le tiers des cas plantés).
- **Sans canari / télémétrie seule** (E5), pour que le canari ajoute une détection.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Oracle et vérificateur confondus.** Le duel « séparation contre déplacement » compte les artefacts faux « selon l'oracle indépendant » acceptés par le vérificateur externe. Si ce vérificateur *est* le recalcul selon l'oracle (option proposée par E), le nombre de fausses acceptations est 0 par construction : tautologie. Le duel n'informe que si oracle et vérificateur sont deux instruments écrits séparément, et si l'oracle est lui-même éprouvé contre des erreurs plantées — ce que E nomme comme pire cas (défaillance commune) sans l'expérimenter.
2. **Canaris contre télémétrie : dominés par construction.** Un canari est un sous-ensemble des chemins interdits ; une télémétrie complète par liste d'accès détecte tout contact de canari. Le gain ≥ 10 points est impossible sauf télémétrie incomplète : le duel mesure l'incomplétude de la télémétrie, pas la valeur des canaris.
3. **Garde réseau : issue connue d'avance.** La sonde v3 classe « délai ⇒ fermée » (pièce 2 § 2.2.3, VÉRIFIÉ documentaire). Sur un banc où l'on fabrique un délai avec sortie ouverte, un faux certificat apparaît avec certitude : H_B ne peut pas survivre. C'est une démonstration utile, pas un duel ; la loi de l'issue est dégénérée.
4. **Apprentissage du verdict : validité externe.** Producteurs à 7 milliards de paramètres (candidats « à vérifier ») alors que les expérimentateurs de l'organisme sont Claude ou Argon (pièce 1). L'absence d'apprentissage chez le premier ne dit rien du second ; le nombre de tours K n'est pas aligné sur les 3 à 12 tours du protocole.
5. **« Non tranché » comme troisième issue.** E prescrit de conclure « non tranché » si l'intervalle chevauche le seuil. L'honnêteté est correcte, mais une issue qui ne falsifie rien contredit B4 ; le remède est de fixer n pour que l'intervalle soit plus étroit que la marge, avant l'expérience, non après.
6. **Corpus « étiqueté par un arbitre indépendant »** : indépendant de qui ? Si l'arbitre partage la spécification, l'étiquette « faux » hérite de l'erreur de spécification, et la défaillance commune que E redoute passe dans les étiquettes.

### (b) Conditions de perte de puissance

- **Duels appariés sur 100 paires, gain ≥ 10 points.** La comparaison est un test de McNemar dont la puissance dépend du nombre de paires discordantes. Si la méthode de base détecte déjà p₁ ≥ 0,90, un gain de 10 points est impossible (plafond) : H_A falsifiée par saturation, non par absence de valeur. FA ≤ 5 % : 0/100 → borne ≈ 3 % ; 5/100 → intervalle ≈ [1,6 % ; 11 %] ; jugeable seulement si l'observé est ≤ 1 ou ≥ 10.
- **Apprentissage du verdict.** L'effet attendu croît avec K ; avec K = 3, l'écart de fausses acceptations réservées est petit devant la largeur d'intervalle à 100 paires ; H_A « ≥ 10 points » est falsifiée pour défaut de puissance. E l'admet (« pour le budget testé ») : l'énoncé est alors vrai pour tout petit budget.
- **Seuil canari calibré puis gelé.** Si les événements interdits sont rares (taux λ), une tranche de calibration de taille n_c estime λ avec un intervalle de largeur ≈ 2√(λ/n_c) ; pour λ ≈ 0,01 et n_c = 100, l'intervalle couvre zéro : le seuil n'est pas identifiable.
- **Garde réseau.** Loi dégénérée (voir a.3) : aucune puissance à mesurer.

### (c) Contrôles négatifs fatals

- **Oracle testé à l'aveugle** contre des erreurs plantées dans l'oracle lui-même.
- Un vérificateur **« accepte tout »** (E n'a que « refuse tout »), pour borner la disponibilité honnête.
- Un **producteur non adaptatif** (même modèle, température 0, sans retour) pour mesurer la dérive de base du duel d'apprentissage.
- Un **artefact honnête sur données nulles** (propriété fausse, production honnête), pour séparer « faux » de « frauduleux » — distinction que E pose en principe et ne contrôle pas.

---

## Note transversale (mon jugement, non une fusion)

Les quatre propositions partagent un même mode de défaillance : les cas plantés sont écrits par ceux qui conçoivent le détecteur. Aucune ne prévoit une banque de défauts constituée par une main *qui ne connaît pas* l'instrument, ni une banque nulle pour mesurer FA sur rien. Tant que ce n'est pas fait, tout TD annoncé est un TD sur ce que l'auteur savait détecter.

FIN-DE-CELLULE