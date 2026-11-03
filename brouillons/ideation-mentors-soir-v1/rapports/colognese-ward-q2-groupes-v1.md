# Groupement aveugle des fiches : piste Colognese–Ward, question 2 (v1)

- Question des mentors (Paul Colognese, Francis Rhys Ward), sur leur billet « l'entraînement de caractère peut atténuer la triche aux récompenses, mais aussi la rendre plus difficile à détecter » : qu'aurions-nous dû faire autrement ? Quelle trouvaille est la plus intéressante, et pourquoi ?
- Entrée (lecture seule) : `/home/claude/scratch/soir-rapport/colognese-ward-q2/piste/fiches-a-grouper-v1.json`, sha256 `ee72eed6c715dc49a1651388b3a8191546e92b298bf7f48f6fb44d8abfc85ffa`, empreinte vérifiée avant lecture ; 25 fiches, CW-01 à CW-25.
- Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/piste-colognese-ward-q2-groupeur-aveugle-v1.md`, sha256 `f64deefc46d10debf59d1c99e2fe08532deff7ca69c5320b1294d7a93c78599f`, empreinte vérifiée avant lecture.
- Groupeur neuf, aveugle au classement : aucun autre fichier que l'entrée n'a été lu.
- Heures (toutes de `date -u`) : début 13:50:30 UTC le 3 novembre 2026 ; **définitions écrites et figées à 13:55:08 UTC, avant toute affectation** ; affectations et rédaction des fichiers à partir de 13:56:13 UTC.
- Fichier compagnon : `groupes-v1.json` (même dossier), mêmes noms, définitions, critères et affectations.

## Groupes (figés à 13:55:08 UTC, non modifiés ensuite)

### 1. Le moniteur croit l'agent
- Définition : Trouvaille : l'agent écrit une partie de ce que lit le moniteur (commentaire qui présente la triche comme inoffensive, mention ou silence sur la triche), et le moniteur se laisse persuader.
  La réponse soutiendrait de l'établir par des éditions contrôlées du seul texte présenté au moniteur, à action inchangée, contre des éditions témoins.
- Critère : L'idée principale de la fiche fait du texte que l'agent présente au moniteur (commentaire justificatif, mention de la triche) la cause testée de la non-détection, à action inchangée.

### 2. Classe de triche et vérification mécanique
- Définition : L'écart de capture entre caractères passe par une classe de triche (réécrire ou neutraliser les tests) presque propre à l'anti-triche, donc confondue avec le caractère.
  Cette classe est visible sans modèle (intégrité des tests, tests cachés) : « plus dur à détecter » ne vaudrait que pour les moniteurs de langage.
- Critère : L'idée principale de la fiche dépend de la classe de triche (séparer classe et caractère) ou d'une comparaison des moniteurs avec des vérifications mécaniques.

### 3. Instruments non validés
- Définition : Les chiffres de capture reposent sur des étiquettes (« silencieuse », « raisonnement motivé », « honnête ») et sur un seuil mutualisé jamais validés contre une vérité terrain indépendante.
  Une part des écarts peut être construite par les étiquettes ou tenir au point de fonctionnement plutôt qu'aux fautes.
- Critère : L'idée principale de la fiche valide une étiquette du billet contre des humains ou un oracle indépendant, ou teste le seuil (seuil commun, fausses alertes, calibration par caractère).

### 4. Effet total mal estimé
- Définition : Atténuation et difficulté de détection se jugent sur l'effet total de l'assignation du caractère, le taux de fautes non détectées par trajectoire, et non sur la capture conditionnelle à « tricher », qui sélectionne après traitement.
  Il faut plusieurs distillations et graines indépendantes et un horizon assez long : une graine unique qui « résiste » sur un seul horizon est indiscernable d'une loterie ou d'une donnée censurée.
- Critère : L'idée principale de la fiche change la quantité mesurée (fautes non détectées par trajectoire) ou le plan d'échantillonnage (points de départ, graines, horizon).

### 5. Leviers non essayés
- Définition : Le billet observe la triche sans agir sur ce qui la renforce ni se comparer à d'autres remèdes ou instruments.
  La réponse soutiendrait d'essayer, chacun contre un témoin, un correcteur protégé, l'inoculation par consigne, une piste boîte blanche.
- Critère : L'idée principale de la fiche propose pour le billet une intervention ou une piste qu'il n'a pas (sur la récompense, la consigne d'entraînement ou les activations), jugée contre un témoin.

### 6. Hors billet
- Définition : Fiches sur des expériences propres du programme (dose de pression sur Llama-3.1-8B-Instruct, sonde de sycophantie dans l'autoencodeur épars Goodfire), sans lien avec la triche aux récompenses ni l'entraînement de caractère.
  La réponse ne les soutiendrait pas ; groupe résiduel imposé par « aucune fiche hors groupe ».
- Critère : La fiche ne mentionne ni le billet, ni la triche aux récompenses, ni l'entraînement de caractère, ni ses moniteurs.

## Affectations (une fiche, un groupe : son idée principale)

| Fiche | Groupe | Raison | Second choix |
|---|---|---|---|
| CW-01 | Hors billet | Courbe dose–réponse de la pression sur Llama-3.1-8B-Instruct (réactance contre saturation) : expérience propre du programme, ni triche ni caractère. | — |
| CW-02 | Instruments non validés | Ré-étiquette le silence par des juges aveugles et un sous-échantillon humain pour savoir si l'écart entre triches franches et silencieuses survit à une vérité terrain indépendante. | — |
| CW-03 | Classe de triche et vérification mécanique | Mesure la part des fautes de l'anti-triche qu'un détecteur mécanique manque, pour borner « plus dur à détecter » aux trois moniteurs de langage. | — |
| CW-04 | Le moniteur croit l'agent | Retire le commentaire qui dit la triche inoffensive, à action inchangée et contre des retraits témoins, pour voir si la capture remonte. | — |
| CW-05 | Hors billet | Sonde de sycophantie projetée sur la reconstruction de l'autoencodeur épars Goodfire : expérience propre du programme, ni triche ni caractère. | — |
| CW-06 | Hors billet | Convergence des deux cibles de Llama-3.1-8B-Instruct sous forte dose de pression à syntaxe constante : expérience propre du programme. | — |
| CW-07 | Instruments non validés | Recalibre le seuil par caractère sur des honnêtes certifiés par oracle pour voir si l'ordre des captures survit. | — |
| CW-08 | Effet total mal estimé | Juge l'atténuation sur le taux de fautes non détectées par trajectoire, sur un plan à quatre bras avec blocs et graines indépendants. | — |
| CW-09 | Leviers non essayés | Randomise le correcteur (d'origine ou protégé des modifications) pendant le renforcement : teste la récompense, pas seulement son observateur. | Classe de triche et vérification mécanique |
| CW-10 | Leviers non essayés | Compare l'anti-triche à l'inoculation par consigne contre un placebo verbal, remède voisin que le billet ne cite pas. | — |
| CW-11 | Classe de triche et vérification mécanique | Exige qu'un moniteur de langage apporte une détection en plus des vérifications mécaniques, à fausses alertes égales. | — |
| CW-12 | Effet total mal estimé | Plan croisé distillations × graines de renforcement : la graine qui résiste, seule par caractère, est indiscernable d'une loterie. | — |
| CW-13 | Leviers non essayés | Propose une piste boîte blanche absente du billet, jugée contre un plancher de sondes aléatoires passées par la même sélection. | — |
| CW-14 | Classe de triche et vérification mécanique | Rend les tests non modifiables pour séparer le silence dû au caractère du silence dû à la classe réécriture. | Leviers non essayés |
| CW-15 | Instruments non validés | Valide les juges du « raisonnement motivé » contre des étiquettes humaines et des témoins négatifs. | — |
| CW-16 | Effet total mal estimé | Lit la résistance observée à un seul horizon comme une donnée censurée et demande plusieurs points de départ, graines et un horizon plus long. | — |
| CW-17 | Instruments non validés | Valide l'étiquette « silencieuse » par un audit humain de l'inférabilité de la triche, contre une recherche lexicale. | — |
| CW-18 | Le moniteur croit l'agent | Fait varier seulement l'information verbale présentée au moniteur, à action inchangée, contre des éditions factices. | — |
| CW-19 | Classe de triche et vérification mécanique | Ajoute au moniteur une vérification mécanique de l'intégrité des tests pour voir si l'ordre des captures tient encore. | — |
| CW-20 | Effet total mal estimé | Mesure l'effet total de l'assignation du caractère sur les fautes non détectées par trajectoire, sur distillations indépendantes. | — |
| CW-21 | Instruments non validés | Teste si le seuil commun produit des fausses alertes différentes selon le caractère, sur des honnêtes certifiés par oracle. | — |
| CW-22 | Le moniteur croit l'agent | Substitue au commentaire qui dit la triche inoffensive un commentaire neutre de même longueur et position, pour isoler son contenu persuasif. | — |
| CW-23 | Instruments non validés | Calibre le seuil par caractère sur des honnêtes certifiés, réservoirs disjoints, pour mesurer la part de l'écart due au point de fonctionnement. | — |
| CW-24 | Classe de triche et vérification mécanique | Exige la table classe × caractère × silence avant toute lecture causale, l'écart pouvant comparer des classes de triche différentes. | — |
| CW-25 | Effet total mal estimé | Remplace la capture conditionnelle à « tricher » par le taux de fautes non détectées par trajectoire, qui garde la graine qui ne triche plus. | — |

## Effectifs

| Groupe | Fiches | Nombre |
|---|---|---|
| Le moniteur croit l'agent | CW-04, CW-18, CW-22 | 3 |
| Classe de triche et vérification mécanique | CW-03, CW-11, CW-14, CW-19, CW-24 | 5 |
| Instruments non validés | CW-02, CW-07, CW-15, CW-17, CW-21, CW-23 | 6 |
| Effet total mal estimé | CW-08, CW-12, CW-16, CW-20, CW-25 | 5 |
| Leviers non essayés | CW-09, CW-10, CW-13 | 3 |
| Hors billet | CW-01, CW-05, CW-06 | 3 |
| **Total** | | **25** |

Seconds choix : CW-09 (Classe de triche et vérification mécanique), CW-14 (Leviers non essayés).

## Limites

1. **Groupe résiduel.** « Hors billet » n'est ni une critique ni une trouvaille que la réponse soutiendrait : CW-01, CW-05 et CW-06 portent sur des expériences propres du programme (pression sur Llama-3.1-8B-Instruct, sonde dans l'autoencodeur épars) et ne touchent ni la triche aux récompenses ni le caractère. Le groupe n'existe que parce qu'aucune fiche ne peut rester hors groupe. Leur présence dans le fichier d'entrée est à signaler à qui l'a constitué (mélange de sources possible) ; il reste donc cinq groupes de fond.
2. **Fusions imposées par le plafond de six groupes.** « Classe de triche et vérification mécanique » réunit deux idées : la confusion entre classe et caractère (CW-14, CW-24) et la portée de « plus dur à détecter » face aux vérifications mécaniques (CW-03, CW-11, CW-19). « Instruments non validés » réunit la validité des étiquettes (CW-02, CW-15, CW-17) et le point de fonctionnement du seuil (CW-07, CW-21, CW-23). « Effet total mal estimé » réunit la quantité mesurée (CW-08, CW-20, CW-25) et le plan d'échantillonnage (CW-12, CW-16). Avec plus de groupes permis, chacun se scinderait en deux.
3. **Une seule trouvaille, quatre critiques.** Seul « Le moniteur croit l'agent » répond à « quelle trouvaille est la plus intéressante » ; les quatre autres groupes de fond répondent à « qu'aurions-nous dû faire autrement ». L'écart de capture entre triches franches et silencieuses, autre candidat naturel à la « trouvaille », n'a pas de groupe propre : il apparaît comme objet à valider dans « Instruments non validés » (CW-02, CW-17).
4. **Même intervention, deux groupes.** CW-09 et CW-14 protègent tous deux les tests des modifications faites depuis la réponse ; CW-09 s'en sert pour tester la récompense (levier), CW-14 pour séparer classe et caractère ; d'où leurs seconds choix croisés.
5. **Liens non retenus comme second choix (critère non rempli, non « presque autant »).** CW-21 invoque la « tentation » verbalisée par les honnêtes anti-triche, mécanisme voisin de « Le moniteur croit l'agent », mais sur les fausses alertes et non sur la non-détection. CW-05 touche les méthodes boîte blanche (voisine de CW-13) mais ne propose rien pour le billet. CW-02 évoque dans son mécanisme le mélange de classes (groupe 2) et le nombre de fautes qui échappent (groupe 4), mais son expérience est une validation d'étiquette. CW-10 juge sur les fautes non détectées (groupe 4), mais son idée est l'inoculation. CW-03 et CW-19 utilisent un oracle et un seuil à fausses alertes fixées (groupe 3) comme moyens, non comme objet. CW-24 impose un effectif minimal par cellule (plan, groupe 4), mais son idée est la confusion de classe.
6. **Prédictions de signes opposés dans un même groupe.** CW-08 (l'anti-triche réduit les fautes non détectées par trajectoire) et CW-20 (il les augmente) ; CW-07 (l'ordre des captures survit au recalibrage) et CW-23 (le recalibrage réduit l'écart). Le groupement suit l'idée (ce qu'il faut mesurer), non le signe attendu. Quasi-doublons dans un même groupe : CW-04 et CW-22 ; CW-03 et CW-19 ; CW-08, CW-20 et CW-25.
7. **Lecture du seul fichier d'entrée.** Les renvois des fiches au billet et à la « pièce Colognese-Ward » (paragraphes, pourcentages, identifiants de papiers) n'ont pas été vérifiés ; les groupes reposent sur le seul texte des fiches et aucun chiffre n'est repris ici comme établi.
8. **Ordre de travail.** Les définitions ont été écrites après lecture des fiches (nécessaire pour les former), mais avant toute affectation ; aucun classement n'a été lu. Elles ont été affichées au terminal à 13:55:08 UTC sans accents ; les fichiers rétablissent les accents et la majuscule initiale des critères, le texte étant par ailleurs identique mot pour mot.
