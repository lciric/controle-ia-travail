# Groupement aveugle des fiches — billet Colognese-Ward, question 2 (v1)

Entrée : `fiches-a-grouper-v1.json` (sha256 `7ee8863b3d4f1a6cbbb1d2c5d63394b1919dbc9db6d6f1f3def73a9f33586abb`, vérifiée), 46 fiches (CW-01 à CW-46).
Groupeur neuf, aveugle au classement ; aucun autre fichier lu.

## Définitions des groupes

Écrites le 2026-11-03 à 17:32:31 UTC (heure de `date -u`), avant toute affectation ; non modifiées ensuite.

### G1 — Classe confondue
**Définition.** Le silence du raisonnement et la faible capture chez l'anti-triche peuvent tenir à la classe de triche (réécriture ou neutralisation des tests dans la réponse) plutôt qu'au caractère.
La réponse soutiendrait qu'il fallait séparer classe et caractère avant toute lecture causale du triplet 29/78/96 %.
**Critère.** La fiche fait varier, retire, force ou tabule la classe de triche pour séparer son effet de celui du caractère.

### G2 — Estimande et plan
**Définition.** La capture conditionnelle à « tricher » et un seul point de départ par caractère ne permettent pas d'attribuer un effet au caractère.
La réponse soutiendrait de mesurer les fautes non détectées par trajectoire et de répliquer distillations et graines (variance hiérarchique, censure à l'horizon).
**Critère.** La fiche change la quantité estimée (fautes non détectées sur toutes les trajectoires) ou le nombre et l'organisation des unités indépendantes (points de départ, graines, horizon), sans changer le détecteur, l'étiquetage ni la chaîne d'entraînement.

### G3 — Instruments non validés
**Définition.** Le seuil commun de fausses alertes, les étiquettes « silencieuse » et « raisonnement motivé » et l'ensemble honnête ne sont pas validés indépendamment.
La réponse soutiendrait qu'une part de l'écart de capture peut être construite par le seuil mutualisé ou par des étiquettes nées des ratés des moniteurs.
**Critère.** La fiche teste la validité d'une étiquette, d'un juge, d'un oracle d'honnêteté ou du seuil de fausses alertes (calibration par caractère, par moniteur) qui produisent les chiffres du billet.

### G4 — Difficulté relative au détecteur
**Définition.** « Plus difficile à détecter » vaut pour trois moniteurs de langage qui lisent un texte en partie écrit par l'agent (commentaire qui présente la triche comme inoffensive).
La réponse soutiendrait de manipuler ce que lit le moniteur ou son architecture, et de comparer ou combiner d'autres détecteurs (vérification mécanique, sondes d'activations) à fausses alertes égales.
**Critère.** La fiche modifie l'entrée ou l'architecture du moniteur, ou ajoute, combine ou compare un autre détecteur, pour savoir si la difficulté tient au détecteur plutôt qu'aux fautes.

### G5 — Mécanisme et leviers d'entraînement
**Définition.** Le billet ne teste ni comment l'entraînement produit le silence (sélection par le renforcement, a priori distillé, distillation sur sorties seules), ni les leviers (correcteur, inoculation, ordre), ni les conséquences hors code.
La réponse soutiendrait des témoins côté entraînement et une mesure du désalignement large après renforcement.
**Critère.** La fiche modifie un élément de la chaîne d'entraînement (distillation, renforcement, correcteur, cadrage, ordre, densité de triche injectée) ou mesure un effet de l'entraînement que le billet ne mesure pas (silence à l'étape 0, désalignement large après renforcement).

### G6 — Hors objet
**Définition.** Fiches qui ne portent pas sur le billet : sycophantie de Llama-3.1-8B-Instruct sous pression, lisibilité d'une sonde dans un autoencodeur épars.
Aucune critique ni trouvaille du billet n'en découle ; groupe résiduel imposé par la règle « aucune fiche hors groupe ».
**Critère.** La fiche ne mentionne ni le billet, ni les caractères anti-triche, neutre ou pro-triche, ni la triche aux récompenses, ni ses moniteurs.

## Affectations

Faites après les définitions ; terminées le 2026-11-03 à 17:34:11 UTC. Chaque fiche a un seul groupe (son idée principale).

| Fiche | Groupe | Raison | Second choix |
|---|---|---|---|
| CW-01 | G6 | Courbe dose–réponse de sycophantie de Llama-3.1-8B-Instruct sous critique ; ni caractère, ni triche, ni moniteur du billet. | — |
| CW-02 | G3 | Ré-étiquette le silence par des juges aveugles et un sous-échantillon humain pour voir si l'écart 16/91 % survit à une vérité terrain indépendante. | — |
| CW-03 | G4 | Compare les moniteurs de langage à un détecteur mécanique contre un oracle hors diff : la difficulté serait propre aux moniteurs. | — |
| CW-04 | G4 | Retire de l'entrée du moniteur le commentaire qui présente la triche comme inoffensive, contre des retraits témoins. | — |
| CW-05 | G6 | Sonde de sycophantie projetée sur un autoencodeur épars ; sans lien avec le billet. | — |
| CW-06 | G6 | Pression à syntaxe constante sur Llama-3.1-8B-Instruct ; sans lien avec le billet. | — |
| CW-07 | G3 | Honnêtes certifiés par oracle et calibration par caractère : teste si l'ordre 29/78/96 % tient au seuil mutualisé. | — |
| CW-08 | G2 | Remplace la capture conditionnelle par u = τ(1 − r) sur toutes les trajectoires, avec quatre bras répliqués. | — |
| CW-09 | G5 | Branche le renforcement sur un correcteur protégé : teste la récompense elle-même, pas son observateur. | — |
| CW-10 | G5 | Ajoute un cadrage d'inoculation à l'entraînement de l'anti-triche contre un placebo verbal. | — |
| CW-11 | G4 | Le moniteur textuel ne vaut que par sa détection supplémentaire sur les vérifications mécaniques à fausses alertes égales. | — |
| CW-12 | G2 | Plan croisé de distillations indépendantes × graines pour juger la résistance au niveau de la distillation. | — |
| CW-13 | G4 | Condition d'utilité d'un détecteur boîte blanche ajouté : battre des sondes aléatoires appariées sur toute la chaîne de sélection. | — |
| CW-14 | G1 | Retire la classe réécriture (tests non modifiables) pour voir si le silence de l'anti-triche persiste. | — |
| CW-15 | G3 | Valide contre des humains les juges du « raisonnement motivé », jusqu'ici seulement accordés entre modèles. | — |
| CW-16 | G2 | Plusieurs points de départ × graines et horizon prolongé : traite « 0 % à l'étape 90 » comme une donnée censurée. | — |
| CW-17 | G3 | Audit humain de l'étiquette « silencieuse » contre une recherche lexicale. | — |
| CW-18 | G4 | Édite seulement l'information verbale présentée au moniteur, à action inchangée. | — |
| CW-19 | G4 | Combine moniteur de langage et vérification mécanique d'intégrité : l'ordre ne tiendrait que pour les moniteurs de langage. | — |
| CW-20 | G2 | Effet total sur les fautes non détectées par trajectoire, moyenné sur des distillations indépendantes. | — |
| CW-21 | G3 | Mesure si le taux de fausses alertes au seuil commun diffère entre caractères sur des honnêtes certifiés. | — |
| CW-22 | G4 | Substitue le commentaire persuasif par un commentaire neutre dans l'entrée du moniteur. | — |
| CW-23 | G3 | Calibration honnête séparée par caractère, oracle distinct du moniteur : l'écart dépendrait du point de fonctionnement. | — |
| CW-24 | G1 | Tabule effectifs et captures par classe × caractère × silence avant toute lecture causale. | — |
| CW-25 | G2 | Définit l'effet sur U = P(faute, non détectée \| caractère) plutôt que sur la capture conditionnelle. | — |
| CW-26 | G5 | Injecte une densité contrôlée de triches récompensées pour mesurer un seuil critique de bascule par caractère. | — |
| CW-27 | G4 | Mesure le gain d'une sonde d'activations ajoutée au meilleur moniteur textuel, et son interaction avec l'inoculation. | G5 |
| CW-28 | G1 | Force la réécriture chez le pro-triche et met les tests hors d'atteinte : sépare classe et caractère. | — |
| CW-29 | G3 | Recalibre le seuil par caractère et par moniteur ; mesure l'écart des fausses alertes au seuil commun. | — |
| CW-30 | G4 | Architecture « extraire, vérifier, évaluer » pour expliquer la faible capture par les affirmations fausses du commentaire. | G5 |
| CW-31 | G5 | Mesure le silence dès l'étape 0 : le renforcement sélectionnerait le silence sans le fabriquer. | — |
| CW-32 | G4 | Sonde entraînée sur le code transférée hors code comme détecteur ajouté aux juges textuels. | G5 |
| CW-33 | G5 | Bras « filtrer puis distiller » sans renforcement : témoin qui sépare sélection et apprentissage propre au renforcement. | — |
| CW-34 | G2 | Distillations × graines répliquées pour décomposer la variance de capture entre point de départ et graine. | — |
| CW-35 | G5 | Mesure le désalignement large après renforcement, que le billet ne mesure qu'avant. | — |
| CW-36 | G4 | Moniteur d'activations justifié seulement par un gain incrémental sur le meilleur moniteur textuel. | — |
| CW-37 | G5 | Branches de renforcement avec correcteur renforcé, jugées par un audit indépendant jamais utilisé à l'entraînement. | — |
| CW-38 | G1 | Croise caractères × régimes d'environnement qui forcent ou interdisent la neutralisation des tests. | — |
| CW-39 | G2 | Points de départ indépendants × graines : mesure la dispersion entre points de départ anti-triche. | — |
| CW-40 | G4 | Plan factoriel commentaire × architecture du moniteur pour savoir d'où vient le gain d'« extraire puis évaluer ». | — |
| CW-41 | G5 | Plan 2 × 2 distillation (sorties seules ou couples) × inoculation sur la part silencieuse. | — |
| CW-42 | G5 | Distille le caractère sur des couples raisonnement–sortie pour lever la dissociation supposée. | — |
| CW-43 | G4 | Passe chaque moniteur en architecture « extraire puis évaluer », sans le commentaire brut. | — |
| CW-44 | G5 | Bras neutre inoculé contre anti-triche, à dose de triche appariée : désalignement large et capture. | — |
| CW-45 | G5 | Change l'ordre caractère / capacités dans la chaîne d'entraînement. | — |
| CW-46 | G2 | Distillations × graines répliquées avec incertitude hiérarchique sur l'écart de capture. | — |

### Effectifs
G1 : 4 (CW-14, 24, 28, 38) · G2 : 8 (CW-08, 12, 16, 20, 25, 34, 39, 46) · G3 : 7 (CW-02, 07, 15, 17, 21, 23, 29) · G4 : 13 (CW-03, 04, 11, 13, 18, 19, 22, 27, 30, 32, 36, 40, 43) · G5 : 11 (CW-09, 10, 26, 31, 33, 35, 37, 41, 42, 44, 45) · G6 : 3 (CW-01, 05, 06). Total 46, chaque fiche une seule fois (contrôle par script).

### Seconds choix
CW-27, CW-30, CW-32 : G4 en principal, G5 en second (l'idée touche aussi l'inoculation ou le désalignement large hors code).

## Limites

1. **Groupe résiduel.** G6 n'est ni une critique ni une trouvaille du billet, contrairement à ce que demande la consigne pour les groupes ; il existe seulement parce qu'aucune fiche ne peut rester hors groupe. CW-01, CW-05 et CW-06 portent sur un autre travail (sycophantie, autoencodeur épars) ; je ne cherche pas à expliquer leur présence dans le fichier.
2. **Plafond de six groupes.** Avec le groupe résiduel, il restait cinq groupes de fond ; G4 et G5 en paient le prix.
   - G4 réunit deux idées voisines : « le moniteur est persuadé par le texte de l'agent » (CW-04, 18, 22, 30, 40, 43) et « d'autres détecteurs » (vérification mécanique : CW-03, 11, 19 ; boîte blanche : CW-13, 27, 32, 36). Avec un groupe de plus, je les aurais séparées.
   - G5 réunit l'origine du silence (CW-31, 33, 41, 42), les leviers d'entraînement (CW-09, 10, 26, 37, 44, 45) et le désalignement large après renforcement (CW-35). Ce dernier thème traverse aussi CW-30, CW-32 et CW-44 et aurait pu former une trouvaille à part.
3. **Frontière G1 / G5.** La question « d'où vient le silence » est partagée : je l'ai tranchée par le facteur manipulé, l'environnement ou la classe pour G1, la chaîne d'entraînement pour G5. CW-28 et CW-38 évoquent aussi le remède côté entraînement, mais elles manipulent l'environnement.
4. **Frontière G2 / G3.** CW-08, CW-20 et CW-25 s'appuient sur un oracle indépendant (un instrument), mais leur idée principale est la quantité estimée ; elles vont donc en G2. CW-02 évoque un mélange de classes et de graines comme lecture rivale, mais elle agit par ré-étiquetage ; elle va donc en G3.
5. **Frontière G4 / G5 pour les détecteurs entraînés.** CW-27 et CW-32 croisent une sonde (détecteur) avec l'inoculation ou un transfert hors code. Je les ai classées sur la grandeur mesurée (un gain de capture d'un détecteur), d'où le second choix G5.
6. **Quasi-doublons.** Plusieurs fiches sont des variantes l'une de l'autre : (CW-04, CW-22), (CW-14, CW-28, CW-38), (CW-07, CW-23, CW-29), (CW-12, CW-34, CW-39, CW-46), (CW-08, CW-20, CW-25), (CW-13, CW-36), (CW-41, CW-42), (CW-40, CW-43). Chacune garde sa ligne ; les effectifs comptent donc des fiches, pas des idées indépendantes.
7. **Critiques ou trouvailles.** Les cinq groupes de fond sont surtout des critiques (« qu'aurions-nous dû faire autrement »). Les trouvailles (« la plus intéressante, et pourquoi ») s'y fondent : la persuasion du moniteur par le commentaire est en G4, la lecture « le renforcement sélectionne le silence » (CW-31, seule fiche qui se dit explicitement trouvaille la plus intéressante) est en G5. Aucun groupe n'est réservé aux trouvailles.
8. **Affectation sur l'énoncé courant.** Pour les fiches qui citent une « version initiale », j'ai classé sur l'énoncé courant. CW-11 n'a pas de mécanisme ; je l'ai classée sur son énoncé seul.
9. **Ordre de travail.** J'ai lu toutes les fiches avant d'écrire les définitions : les groupes sont tirés du contenu. Les définitions ont été écrites dans ce fichier avant toute affectation (17:32:31 UTC) et n'ont pas été changées ensuite. Je n'ai lu aucun classement.
