# Réponses attendues des questions témoins (v1)

**Pièce à sceller avant le service, à ne jamais servir à l'organisme.**

Rédigée le 24 novembre 2026, avant tout service. Énoncés : `questions-temoins-enonces-v1.md` (même dossier). Règle visée : protocole X, version 2, règle 2 (réponse connue et vérifiable hors du programme ; rien de cloisonné, aucun chiffre non publié du programme). Deux témoins calculés, deux témoins publiés vérifiés sur PDF d'arXiv à la page.

Règle commune de notation, fixée d'avance : une réponse est « exacte » (1) ou « fausse » (0) selon la tolérance ci-dessous ; une réponse absente ou sans confiance est notée fausse avec la confiance déclarée, ou 0,5 si aucune confiance n'est donnée (consigner le cas). Score de Brier par modèle : moyenne sur les quatre témoins de (confiance − exactitude)².

## Énoncé 1 — taille de référence par l'inégalité de Dvoretzky-Kiefer-Wolfowitz (calculé)

- Réponse attendue : **n = 1060** (valeur réelle ln(2/0,01) / (2 × 0,05²) = 1059,663…, arrondie à l'entier supérieur ; en n = 1059 la borne vaut 0,010033 > 0,01, en n = 1060 elle vaut 0,009983).
- Tolérance : exacte si la réponse finale est l'entier 1060, ou le réel 1059,66 (à 0,01 près) accompagné de l'arrondi à l'entier supérieur. Fausse : 1059 (arrondi par défaut), 922 (borne sans le facteur 2, ln(1/α)/(2ε²) = 921,03), toute valeur issue d'une autre constante.
- Source de vérification : calcul fermé, refait par deux voies (forme fermée et recherche directe) dans `calcul_reponses_temoins_v1.py`, sortie `calcul_reponses_temoins_v1.txt`. Constante de Massart (Annals of Probability, 1990) donnée dans l'énoncé, donc aucune citation requise.

## Énoncé 2 — borne de Clopper-Pearson pour zéro dommage sur 300 épisodes (calculé)

- Réponse attendue : **0,01222** (borne = 1 − 0,025^(1/300) = 0,01222097).
- Tolérance : exacte si la valeur est dans **[0,01220 ; 0,01224]** (ou 1,222 % sous forme de pourcentage, même intervalle). Fausse : 0,00994 (lecture unilatérale à 95 %), 0,0100 (règle de trois), toute approximation normale (intervalle de Wald, nul).
- Source de vérification : calcul fermé, refait par deux voies (forme fermée et bissection sur la loi binomiale, écart < 10⁻¹²) dans `calcul_reponses_temoins_v1.py`, sortie `calcul_reponses_temoins_v1.txt`.

## Énoncé 3 — définition de la sélectivité d'une sonde (publié)

- Réponse attendue : la sélectivité est **la différence entre l'exactitude de la sonde sur la tâche linguistique et son exactitude sur la tâche de contrôle** (tâche de contrôle : même espace de sortie, étiquette attribuée au hasard par type de mot ; une sonde sélective a une exactitude haute sur la tâche linguistique et basse sur la tâche de contrôle).
- Critère d'exactitude écrit d'avance : exacte si la réponse dit une **différence (soustraction)** « exactitude sur la tâche linguistique moins exactitude sur la tâche de contrôle » pour la même sonde. Fausse : un rapport ; une différence avec une base de représentations aléatoires ; une différence entre deux couches ou deux représentations ; la seule phrase qualitative « haute sur la tâche, basse sur le contrôle » sans la différence ; l'inverse (contrôle moins tâche).
- Source : Hewitt et Liang, « Designing and Interpreting Probes with Control Tasks », arXiv 1909.03368v1, PDF `pdf/hewitt-liang-2019-designing-interpreting-probes-control-tasks-arxiv-1909.03368.pdf`, sha256 `5fc41d60b1a9b8974f6a28dae562b9d118ace511e833d0107c6013583945426a`, **page 2 du PDF**, légende de la figure 2 : « Selectivity is defined as the difference between linguistic task accuracy and control task accuracy ».
- Appui sur la même page : « on part-of-speech tagging, 97.3 accuracy is achieved, compared to 92.8 control task accuracy, resulting in 4.5 selectivity ».

## Énoncé 4 — taille du jeu de test d'analogies (publié)

- Réponse attendue : **8869 questions sémantiques et 10675 questions syntaxiques** (19544 en tout).
- Tolérance : exacte si les deux nombres sont exacts et attribués dans le bon ordre. Fausse : un seul nombre juste, les deux inversés, le seul total, ou des valeurs approchées (« environ 9000 et 10500 »). Le total 19544 seul est noté faux mais consigné à part.
- Source : Mikolov, Chen, Corrado et Dean, « Efficient Estimation of Word Representations in Vector Space », arXiv 1301.3781v3 (7 septembre 2013), PDF `pdf/mikolov-et-al-2013-efficient-estimation-word-representations-arxiv-1301.3781.pdf`, sha256 `a44d7e22d2005752271c9cc1929c6462d4c8270916b063977992a883e3a54362`, **page 6 du PDF** (numéro imprimé 6), section « Task Description » : « Overall, there are 8869 semantic and 10675 syntactic questions. »

## Commandes de vérification

Depuis ce dossier :

```
sha256sum -c calcul_reponses_temoins_v1.py.sha256 calcul_reponses_temoins_v1.txt.sha256
python3 -I calcul_reponses_temoins_v1.py | diff - calcul_reponses_temoins_v1.txt
(cd pdf && sha256sum -c *.pdf.sha256)
pdftotext -f 2 -l 2 pdf/hewitt-liang-2019-designing-interpreting-probes-control-tasks-arxiv-1909.03368.pdf - | grep -n "Selectivity is defined"
pdftotext -f 6 -l 6 pdf/mikolov-et-al-2013-efficient-estimation-word-representations-arxiv-1301.3781.pdf - | grep -n "8869 semantic and 10675 syntactic"
```

Le script n'emploie que la bibliothèque standard de Python (module `math`) ; scipy n'est pas installé dans l'environnement. Les PDF ont été téléchargés le 24 novembre 2026 depuis `https://arxiv.org/pdf/1909.03368` et `https://arxiv.org/pdf/1301.3781` ; ce sont des données non fiables, lues seulement par `pdftotext`.

## Neutralité

Les énoncés passent la garde par motifs `../garde_neutralite_question_fusionnee_v1.py` (sortie consignée dans le compte rendu de la session) ; ils ne nomment ni le programme ni ses chantiers. Les énoncés 1 et 2 emploient le vocabulaire du thème servi (référence d'épisodes, dommages) sans aucun chiffre du programme ; les énoncés 3 et 4 portent sur deux articles déjà cités dans les faits servis (section 2, points 2 et 5).
