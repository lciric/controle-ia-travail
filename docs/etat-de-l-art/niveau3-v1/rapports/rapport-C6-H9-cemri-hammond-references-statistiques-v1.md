# Rapport C6 — H9 face à Cemri et à Hammond ; références statistiques face au lemme, au théorème et à H2 — v1

Lot C6 de l'état de l'art, niveau 3. Lecteur neuf (il n'a écrit ni les décisions, ni la note mathématique, ni les rapports antérieurs).
Heure de fin de lecture relevée par `date -u` : 2026-11-10, 11:03 UTC.
Consigne commune lue en entier : `docs/etat-de-l-art/niveau3-v1/consignes/consigne-commune-lecteurs-v1.md` (551118525db6…).

## 0. Verdict en tête

**Pas de collision entière.** Aucune des cinq pièces lues n'occupe en entier une zone que le programme revendique.

- **H9 (survie d'une contrainte de sécurité à la délégation) : occupée en partie, par composantes, dans Cemri et dans Hammond.**
  - Le phénomène est **décrit** par Hammond (p. 24) : des chaînes de délégation transmettent des consignes ou des buts, qui peuvent être déformés.
  - Une **courbe de perte par passage** est **mesurée** par Hammond (p. 24 et 51), mais sur un autre objet : l'exactitude factuelle d'articles de presse récrits huit fois de suite. Ce n'est ni une contrainte de sécurité, ni une délégation.
  - Cemri **mesure** la fréquence du non-respect de la spécification et de la perte d'historique (p. 2, 7, 17), mais par trace entière : ni par passage, ni selon la profondeur, ni pour une contrainte de sécurité.
  - **Aucune des deux pièces ne mesure la survie d'une contrainte de sécurité explicite passage par passage, et aucune ne compare avec et sans moniteur à chaque passage.** Cette mesure est libre dans ces deux pièces.
  - **Ce verdict ne vaut que pour Cemri et Hammond.** Cinq pièces signalées par un chercheur ne sont pas lues (arXiv 2608.07556 « MasDrift », 2608.24569, 2609.27900, 2605.10481, 2607.07097). La première, d'après son seul titre, vise la dérive dans les systèmes multi-agents : elle peut renverser ce verdict.
- **Lemme (L) et théorème négatif (T) : le verdict « occupé en partie » du rapport C2 tient. Les trois pièces statistiques ne créent pas de collision entière, mais elles déplacent trois composantes vers « classique, à citer ».**
  - La borne de mélange est portée sur PDF (2210.01948, p. 13). La statistique de mélange classique ne dépend des données que par leur somme : l'invariance terminale au budget (L1) y est implicite.
  - Le « prix de la garantie toujours valide » et le « coût du report » (L3), que C2 jugeait libres, ont un **antécédent qualitatif publié** : 2203.03532, remarque 2.7, p. 8.
  - La **parade** du théorème négatif existe comme **outil publié à garantie toujours valide** : test séquentiel d'indépendance entre deux flux (2212.07383), détecteur d'un passage de l'indépendance à la dépendance (2203.03532, p. 11), tests séquentiels de l'échangeabilité (cités par 2210.01948, p. 15, et 2203.03532, p. 11).
- **H2 : non occupée par ces trois pièces.** Elles ne parlent ni d'agents, ni de modèles de langage, ni de sondes (recherche par mots-clés dans les 118 pages : aucune occurrence). Elles fournissent la boîte à outils, à citer.

**Trois contre-résultats défavorables au programme** (détail en sections 2, 4 et 5) :

1. La première moitié de la prédiction de H9 (« la survie décroît avec le nombre de passages ») a déjà sa forme publiée pour l'information : Hammond, p. 24, de 96 % à moins de 60 % en huit récritures. Un relecteur dira que la décroissance est attendue. Et le mécanisme de Hammond est la **reformulation à chaque passage**, c'est-à-dire l'un des trois confondants que N-035 demande de séparer.
2. « Prix de la garantie toujours valide » et « coût du report » figurent dans la revendication de L (décision N-004). La remarque 2.7 de 2203.03532 (p. 8) dit déjà que passer du contrôle de la fréquence des fausses alarmes au contrôle de leur probabilité fait croître le délai de détection avec la date du changement. Le programme apporte le chiffrage à budget borné, pas l'idée.
3. Le programme § 3 écrit qu'« il faut un agrégateur d'autocorrélation (dans le temps) ou de co-élévation (entre agents) ». Pour deux flux, cet agrégateur toujours valide est publié depuis 2023 (2212.07383). Il se cite ; il ne se revendique pas. Sa condition de validité (une seule marginale change à chaque pas, p. 3 et 8) est précisément mise en défaut par un effet d'épisode commun aux deux agents : c'est une limite à dire, pas un apport à annoncer sans mesure.

**Réserve (R4).** Le tableau de la partie statistique est propre parce que les trois pièces sont des pièces d'outillage général : elles ne pouvaient guère occuper un énoncé adverse sur des agents. « Libre » veut dire « non trouvé dans les pièces lues » (R8). Les sources que ces pièces citent pour l'échangeabilité ne sont pas lues (section 7).

## 1. Ce qui a été lu, et comment

Énoncés du programme : `docs/decisions/decision-N-035-v1.md` (55df073d6918…) ; `docs/decisions/decision-N-003-N-004-v1.md` (cc1be39369bc…) ; `docs/decisions/decision-N-007-N-008-v1.md` (ab7dc9bb2c96…) ; `docs/programme-controle-ia-v2.md` § 3 (2fd63badb5af…) ; `docs/etat-de-l-art/niveau3-v1/rapports/rapport-C2-lemme-theoreme-v1.md` en entier (76475485116b…).

PDF : extraits pour moi dans le dossier temporaire du lot ; chemin de dépôt `docs/sources/pdf/niveau3-v1/lot5/` (branche `prep/etat-de-l-art-niveau3-pieces-v1`, commit f05e9aed, d'après la consigne du lot). **Ce dossier n'existe pas sur la branche courante** (vérifié par `ls` du chemin exact, R11) ; je n'ai ouvert aucune autre branche (interdit). Empreintes calculées par `sha256sum` sur les fichiers extraits.

| Pièce | Empreinte | Pages | Étendue de ma lecture |
|---|---|---|---|
| 2503.13657v3 (Cemri et collègues) | 1b9e317a2a42… | 47 | p. 1 à 10, 17, 18 en entier ; p. 21, 28 à 30, 45 en partie ; le reste par mots-clés |
| 2502.14143v1 (Hammond et collègues) | 3a8e798a29f7… | 96 | p. 24 à 26, 40 à 43, 51 en entier ou presque ; p. 1 à 57 par mots-clés ; bibliographie (p. 53 à 96) pour trois références seulement |
| 2203.03532v4 (Shin, Ramdas, Rinaldo) | 564dc11f356c… | 50 | p. 1 à 9, 11 à 13, 19, 32, 33 en entier ou presque ; p. 10 en partie ; le reste par mots-clés |
| 2210.01948v2 (Ramdas, Grünwald, Vovk, Shafer) | 19dfc4e96857… | 25 | p. 8, 13 à 17 en entier ou presque ; p. 7, 11, 12 en partie ; le reste par mots-clés |
| 2212.07383v4 (Podkopaev et collègues) | a0a596319e1c… | 43 | p. 1 à 9 en entier ou presque ; conclusion (p. 13-14) ; annexes par mots-clés |

**Écart signalé.** Aucune pièce n'a été lue ligne à ligne en entier. Pour Hammond (96 pages), la lecture hors des pages citées est un balayage par mots-clés (« delegat », « sub-agent », « hand-off », « chain », « constraint », « instruction », « propagat », « overseer », « monitor », etc.). Un passage pertinent sans ces mots reste possible. Les annexes de preuves des pièces statistiques n'ont été vues que par mots-clés.

Lecture par `pdftotext`, avec et sans `-layout`. Pour les pièces sur deux colonnes (2210.01948, et les encadrés de 2502.14143), j'ai aussi extrait chaque demi-page à part.

**Contrôle des citations.** Script `verif.py` dans le dossier temporaire du lot (hors du sous-dossier `pdf/`, hors du dépôt). Il cherche chaque citation dans le texte de la page citée, espaces et césures normalisés. Essai préalable (R5) : citation juste acceptée ; citation altérée d'un caractère refusée ; citation juste sur une mauvaise page refusée. Le contrôle a attrapé une césure (« non-i.i.d. », citation T9), ce qui a demandé une normalisation de plus ; les trois essais ont été refaits après ce changement, avec le même résultat. Compte final : **76 citations contrôlées, 0 échec** (annexe A).

## 2. Partie 1 — H9 face à Cemri et à Hammond

Énoncé de H9 (N-035, section 2) : dans une chaîne de délégation, une contrainte de sécurité explicite peut s'éroder à chaque passage d'un agent à un sous-agent ; mesure de la survie à chaque passage, avec ou sans moniteur à chaque passage ; prédiction : la survie décroît avec le nombre de passages, un moniteur à chaque passage la relève.

### 2.1 Cemri et collègues (2503.13657v3)

**Ce que la pièce est.** Une taxonomie de 14 modes d'échec en 3 catégories, et un jeu de 1642 traces annotées, tirées de 7 systèmes multi-agents [K7]. L'annotation est faite surtout par un modèle juge. L'échec est défini par rapport à la tâche [K4], non par rapport à la sécurité : la sécurité est renvoyée à d'autres travaux [K9].

**La perte d'une contrainte ou d'une spécification est-elle décrite ?** Oui, sous deux modes.
- FM-1.1, non-respect de la spécification de la tâche, qui nomme les contraintes [K1].
- FM-1.4, perte de l'historique de conversation [K2], avec un exemple où un agent revient à un état antérieur parce que les derniers échanges manquent [K10].

Aucun de ces deux modes n'est rattaché à un passage d'un agent à un sous-agent. La pièce donne trois causes possibles du non-respect, dont les limites du modèle lui-même [K8] : elle ne sépare pas ce qui vient de la délégation.

**Est-elle mesurée ?** Oui, comme fréquence par trace : 11,8 % pour FM-1.1 et 2,80 % pour FM-1.4 [K3]. **Non par passage, non selon la profondeur.** Je n'ai trouvé aucune analyse selon le nombre de passages, la profondeur de la hiérarchie ou la longueur de la chaîne (recherche de « depth », « hop », « layer », « per step », « number of agents » : aucune analyse de ce type ; « hierarch » n'apparaît que pour décrire l'architecture des systèmes, p. 19).

**Avec un moniteur à chaque passage ?** Non. La pièce étudie des vérificateurs de la sortie finale. Elle note que les systèmes dotés d'un vérificateur explicite échouent moins, sans que ce soit une solution [K5] ; elle juge insuffisant un contrôle au seul stade final [K11] ; une intervention qui ajoute une étape de vérification de l'objectif gagne 15,6 points de succès de la tâche sur un système [K6]. C'est un argument publié **pour** des contrôles à plusieurs niveaux, pas une mesure de survie d'une contrainte avec et sans moniteur par passage.

**Réserve sur les chiffres (R4).** La pièce porte de petites incohérences internes : la rétention d'information vaut 0,80 % dans la figure 1 [K13] et 0,85 % dans le texte [K12] ; la part de la première catégorie vaut 44,2 % sur 1642 traces (figure 1, p. 2) et 41,8 % sur 210 traces (figure 4 [K14]). Tout chiffre de Cemri repris ailleurs doit dire sur quel ensemble de traces il est compté.

**Verdict pour H9 dans Cemri : occupée en partie, par une composante lointaine.** Pris : l'existence et la fréquence, par trace, du non-respect d'une spécification et de la perte de contexte dans des systèmes multi-agents (p. 2, 7, 17). Non trouvé : la contrainte de sécurité, le passage comme unité, la profondeur, le moniteur par passage.

### 2.2 Hammond et collègues (2502.14143v1)

**Ce que la pièce est.** Un rapport de synthèse sur les risques des systèmes multi-agents, avec de courtes études de cas.

**La perte à la délégation est-elle décrite ?** **Oui, en toutes lettres**, section 3.2.2, « Error Propagation », p. 24 : des chaînes de délégation transmettent des consignes ou des buts à travers des réseaux d'agents [M1] ; si ces buts sont déformés, le résultat est pire pour qui délègue [M2]. L'image est celle du jeu du téléphone [M4]. La phrase renvoie à deux références non lues [M10], [M11] (section 7). C'est une phrase de description, sans mesure propre à la délégation.

**Est-elle mesurée ?** Une perte **par étape** est mesurée, sur un autre objet. Étude de cas 7 (p. 24 ; annexe B.2, p. 51) : 100 articles [M13], récrits à répétition par un modèle sous des consignes de style ; après chaque récriture, un modèle répond à dix questions factuelles et un autre note [M5]. Le taux de bonnes réponses passe d'environ 96 % à moins de 60 % à la huitième récriture [M3]. Les auteurs concluent à une dégradation de l'information le long des réseaux [M14].
- C'est la **forme** de la mesure de H9 : une courbe de survie selon le nombre de passages.
- Ce n'est **pas** son objet : information factuelle d'un article, non contrainte de sécurité explicite ; récriture de style, non délégation d'une tâche à un sous-agent ; aucune condition avec moniteur.
- L'expérience est petite, et les auteurs le disent [M13].

**Avec un moniteur à chaque passage ?** Non. La pièce traite les agents surveillants comme une idée d'autrui [M8] et comme une surface d'attaque (étude de cas 13, p. 41). Elle dit que les outils de surveillance ne s'appliquent pas toujours aux réseaux d'agents [M7], que le biais peut croître à chaque passage [M6], et propose, en direction de recherche, des réseaux d'agents pour surveiller et empêcher les cascades [M12]. Aucune mesure.

**Voisin à noter.** Étude de cas 12, p. 40 : la délégation de sous-tâches entre un modèle bridé et un modèle faible **contourne** les garde-fous [M9]. C'est un usage adverse de la délégation, non l'érosion d'une contrainte transmise. Il touche le voisinage de H9 côté attaque.

**Verdict pour H9 dans Hammond : occupée en partie, par composantes.** Pris : la description du phénomène pour les consignes et les buts (p. 24 [M1], [M2]) ; le plan de mesure « perte selon le nombre de passages », sur l'information (p. 24 [M3] ; p. 51 [M5]). Non trouvé : la survie d'une contrainte de sécurité explicite, la délégation agent vers sous-agent comme unité, la comparaison avec et sans moniteur par passage.

### 2.3 Verdict pour H9, et ses limites

| Composante de H9 | Cemri | Hammond | Verdict dans ces deux pièces |
|---|---|---|---|
| Le phénomène : une consigne ou un but se perd à la délégation | décrit sans lien à la délégation (p. 17 [K1], [K2]) | **décrit** (p. 24 [M1], [M2]) | occupée (description) |
| Mesure d'une perte | fréquence par trace (p. 7 [K3]) | par étape, sur l'information (p. 24 [M3]) | occupée en partie |
| Mesure par passage, selon la profondeur, d'une **contrainte de sécurité explicite** | non trouvée | non trouvée | libre dans ces deux pièces |
| Moniteur à chaque passage, avec et sans | non trouvé ; vérificateur final seulement (p. 8 [K5], [K6]) | non trouvé ; direction de recherche (p. 42 [M12]) | libre dans ces deux pièces |
| Prédiction « la survie décroît avec le nombre de passages » | — | forme publiée pour l'information (p. 24 [M3]) | peu surprenante ; à présenter comme attendue |
| Prédiction « un moniteur par passage la relève » | argument qualitatif pour des contrôles à plusieurs niveaux (p. 8 [K11]) | — | libre comme mesure |

**H9 : occupée en partie (composantes), dans Cemri et Hammond. Pas de collision. Le repli (b) de N-035 n'est pas déclenché par ces deux pièces.**

Trois points pour le directeur, sans modifier aucun énoncé :
1. La nouveauté de H9, d'après ces deux pièces, tient à **trois précisions à la fois** : contrainte de sécurité explicite, passage de délégation comme unité, moniteur par passage. Retirer l'une d'elles ramène vers Hammond (p. 24).
2. Le confondant « reformulation de la consigne à chaque passage », nommé par N-035, **est** le mécanisme de l'expérience de Hammond. Un bras « consigne transmise mot pour mot » paraît nécessaire pour dire autre chose qu'elle. Ceci est une remarque de lecture, non une décision.
3. **Limite du verdict.** Il ne vaut que pour Cemri et Hammond. Les cinq pièces signalées (2608.07556 « MasDrift », 2608.24569, 2609.27900, 2605.10481, 2607.07097) ne sont pas lues : pistes, non vérifiées. Les deux références de Hammond sur la délégation [M10], [M11] non plus.

## 3. Partie 2 — ce que chaque pièce statistique énonce

### 3.1 2203.03532v4 — détecteurs par e-valeurs

- **Cadre.** Détection séquentielle de rupture quand les lois d'avant et d'après le changement sont des classes non paramétriques, donc composites [S1]. Les observations ne sont supposées ni indépendantes ni de même loi [S3]. Le changement peut être choisi par un adversaire adaptatif [S4].
- **Garantie.** Théorème 2.4, p. 7 [S18], [S13] : tout détecteur par e-valeurs, seuillé à 1/α, contrôle la **durée moyenne avant fausse alarme** (au moins 1/α) [S15], sans hypothèse sur le changement ni sur la loi d'après [S12], et pour des lois composites sans indépendance [S2].
- **Ce n'est pas la garantie du programme.** Le programme demande une probabilité de fausse alarme bornée sur tout l'horizon. La remarque 2.7, p. 8, donne le passage : avec des poids initiaux de somme au plus 1, on contrôle la probabilité de fausse alarme, critère « bien plus exigeant » [S6] ; **le prix est un délai de détection qui croît, typiquement comme le logarithme, avec la date du changement**, et un pire délai moyen non borné [S5].
- **Délai.** Bornes de délai seulement si les observations d'après le changement sont indépendantes de celles d'avant et stationnaires (p. 13 [S9]), ou de même loi et indépendantes (théorème 4.3, p. 19 [S17]). Le terme dominant est log(1/α) divisé par la divergence par pas, au rythme des bornes inférieures connues [S10]. **Aucune borne de délai pour un changement non stationnaire ou pour une dérive étalée** n'a été trouvée (recherche de « drift », « gradual », « non-stationar », « cumulative », « budget » : la dérive n'apparaît que pour la validité, p. 11 [S14]).
- **Dépendance à marginales préservées.** Exemple 4, p. 11 : branché sur le test de 2212.07383, le cadre donne un détecteur d'un passage de l'indépendance à la dépendance [S7]. Exemple 2, p. 11 : les procédures conformes de détection testent les écarts à l'échangeabilité [S8] ; un e-processus existe pour l'échangeabilité d'une suite binaire [S19]. Sens inverse (de la dépendance vers l'indépendance) : les auteurs ne connaissent pas de méthode puissante [S16].
- **Corruption adverse.** Exemple 8, p. 12 : une fraction de données corrompues par un adversaire se traite par des surmartingales robustes [S11]. C'est une corruption d'une fraction des données, non un budget de décalage.
- **Non trouvé** : budget total borné réparti par un attaquant ; invariance à la répartition ; plusieurs agents ; scores de sondes.

### 3.2 2210.01948v2 — statistique par la théorie des jeux, inférence valable à tout instant

Article de synthèse.
- **Borne de mélange.** p. 13 : Darling et Robbins (1968) [T14] ; mélange gaussien d'une surmartingale exponentielle [T1] ; l'adaptativité est un bénéfice connu de la méthode des mélanges [T3]. **La formule de mélange de la p. 13 ne dépend des données que par leur somme et par le temps** (lecture de la formule, la mienne). Et si la moyenne diffère à chaque pas, le même argument couvre la **moyenne courante** [T2], [T15]. Forme générale, p. 16 : ces surmartingales sont des fonctions de la somme et de la variance cumulée [T4].
- **Croissance et délai.** p. 8 : sous indépendance et loi commune, le critère logarithmique minimise, à la limite, le temps moyen avant d'atteindre le seuil [T5]. p. 16 : le meilleur délai de détection, à durée moyenne avant fausse alarme fixée, est d'ordre log(1/α) divisé par la divergence [T8].
- **Échangeabilité.** p. 15 : pour une suite binaire, aucune surmartingale de test non triviale n'existe dans la filtration d'origine, mais un e-processus puissant existe [T6] ; en réduisant la filtration aux valeurs p conformes, des martingales de test existent [T12] ; des martingales conformes détectent les écarts à l'échangeabilité [T7].
- **Indépendance.** p. 17 : 2212.07383 est donné comme le premier cadre séquentiel non paramétrique de test d'indépendance, y compris hors du cas de lois identiques et indépendantes [T9].
- **Combinaison sous dépendance.** p. 7 : la moyenne de deux e-valeurs est une e-valeur même si elles sont dépendantes [T11].
- **Invariance de groupe.** p. 11 : pour les problèmes invariants par un groupe, la réduction à une hypothèse nulle simple donne des e-processus optimaux en croissance [T13]. Les groupes cités p. 12 sont l'échelle, la position, la rotation, le groupe affine ; je n'y ai pas trouvé les sous-groupes de permutations du temps et des agents.
- **Limite dite par la pièce.** Les détecteurs par e-valeurs demandent des classes d'avant et d'après fixées d'avance et disjointes [T10].

### 3.3 2212.07383v4 — test séquentiel d'indépendance à noyau

- **Énoncé.** Test séquentiel de l'indépendance de deux variables observées par paires, dans un cadre composite non paramétrique [P14], par pari. Contrôle de l'erreur de première espèce **uniforme dans le temps** [P2] : le test ne s'arrête jamais, sous l'hypothèse nulle, qu'avec une probabilité au plus α (théorème 2, p. 7 [P5]), par l'inégalité de Ville [P10]. Sous l'alternative, la richesse croît exponentiellement, à un taux donné par la mesure de dépendance [P13].
- **Hors du cas de lois identiques.** Valide pour un flux de données indépendantes [P11] dont la loi dérive [P1], **à condition qu'une seule des deux marginales change à chaque pas** [P4] ; les auteurs montrent que cette condition est nécessaire [P9]. Le test par permutation, lui, exige l'échangeabilité des paires [P3].
- **Deux flux à mémoire.** Le test sert aussi à l'indépendance instantanée entre deux flux [P6] (théorème 3, p. 9), sous l'hypothèse 2 : pas de liens croisés entre les flux [P7], et une condition d'échangeabilité locale ; sans hypothèse de mélange ni de stationnarité [P8]. Voisin cité, non lu : Chwialkowski et Gretton [P12].
- **Non trouvé** : dépendance sérielle à l'intérieur d'un seul flux (recherche de « autocorr », « serial », « lag » : aucune occurrence) ; indépendance jointe de plus de deux flux (aucune occurrence de « mutual », « joint independence ») ; adversaire ; délai sous alternative non stationnaire ; agents, sondes.

## 4. Confrontation au lemme, au théorème et à H2

### 4.1 Les quatre questions de la consigne du lot

| Question | Réponse | Appui |
|---|---|---|
| Borne de mélange et puissance fonction du seul budget cumulé | **La borne de mélange est classique, maintenant portée sur PDF.** La dépendance aux données par la seule somme est dans la formule ; la couverture de moyennes variables par leur moyenne courante est écrite. **Aucune pièce n'énonce la puissance comme fonction du seul budget face à un attaquant qui répartit.** | 2210.01948, p. 13 [T1], [T2], [T15], [T14] ; p. 16 [T4] |
| Détection séquentielle sous dépendance ou sous hypothèse nulle composite | **Occupée comme outil**, pour une classe nulle spécifiée. La garantie est la durée moyenne avant fausse alarme ; le passage à la probabilité a un prix publié. | 2203.03532, p. 3 [S2], p. 6 [S3], p. 7 [S13], p. 8 [S5], [S6] |
| Détection d'une dépendance à marginales préservées (la parade) | **Oui, un agrégateur toujours valide existe comme outil publié** : pour la co-élévation entre **deux** flux (test d'indépendance) ; pour les écarts à l'échangeabilité dans le temps (martingales conformes, e-processus binaire), d'après les pièces lues qui les citent. | 2212.07383, p. 3 [P2], p. 7 [P5], p. 8 [P6] ; 2203.03532, p. 11 [S7], [S8] ; 2210.01948, p. 15 [T6], [T7], [T12], p. 17 [T9] |
| Délai de détection en fonction de la dérive cumulée | **Classique pour un changement stationnaire** : délai d'ordre log(1/α) sur la divergence par pas ; autrement dit l'alarme tombe quand la divergence cumulée atteint l'ordre de log(1/α) (reformulation, la mienne). **Non trouvé pour une dérive étalée ou non stationnaire.** | 2203.03532, p. 13 [S9], p. 19 [S10], [S17] ; 2210.01948, p. 8 [T5], p. 16 [T8] |

Précision sur la troisième ligne. La validité de l'outil d'indépendance n'est pas celle dont le programme a besoin sans examen :
- il vaut pour **deux** flux ; rien pour N agents dans la pièce ;
- sa validité tombe si les deux marginales bougent au même pas [P4], [P9], ce que fait un effet d'épisode commun ;
- la dépendance sérielle d'un seul agent n'y est pas traitée. On peut l'y ramener en formant des paires disjointes de pas consécutifs, valides sous une hypothèse nulle de pas indépendants et de même loi : c'est une construction de ma part, non un énoncé de la pièce, et elle ne tient pas sous un effet d'épisode.

### 4.2 Composantes du rapport C2 que ces pièces déplacent

| Composante (rapport C2, section 4) | Verdict de C2 | Verdict après ces trois pièces | Appui |
|---|---|---|---|
| Borne de mélange | classique ; source propre « piste, non vérifiée » | **classique, portée sur PDF** par une synthèse ; la source propre (Howard et collègues) reste à récupérer | 2210.01948, p. 13 [T1], [T3], [T14] |
| L1, invariance terminale au budget | libre ; élémentaire | **libre comme énoncé adverse ; implicite dans le classique** (la statistique de mélange ne voit que la somme ; moyennes variables couvertes par la moyenne courante) | 2210.01948, p. 13 [T2], [T15], p. 16 [T4] |
| L4, invariance entre agents au même pas | libre ; élémentaire | inchangé. Outil voisin à citer : la moyenne d'e-valeurs dépendantes reste une e-valeur | 2210.01948, p. 7 [T11] |
| L3, prix de la garantie toujours valide ; coût du report | **libre** | **occupée en partie** : antécédent qualitatif (contrôle de la probabilité de fausse alarme contre délai croissant avec la date du changement). Reste libre : la borne fonction du seul budget et le chiffrage à budget borné | 2203.03532, p. 8 [S5], [S6] |
| Sécurité « avant le dommage » : détecteur de rupture | classique, occupée en partie par 2601.20022 | **l'outil nommé par N-004 (« détecteurs e ») est cette pièce** : à citer. La comparaison chiffrée avec le processus cumulé depuis l'origine, à budget borné, n'y est pas | 2203.03532, p. 7 [S18], p. 8 [S5] |
| Validité hors hypothèses | occupée en partie par 2512.03109 | inchangé sur le fond. Les détecteurs par e-valeurs valent sans indépendance **pour une classe nulle spécifiée** ; ils ne règlent pas une dépendance inconnue, pour laquelle le réglage sur épisodes honnêtes entiers (2512.03109) reste la voie | 2203.03532, p. 3 [S2], p. 6 [S3] |
| L2, somme contre maximum | classique en théorie (piste) | inchangé ; ces pièces n'en traitent pas | — |
| T2, impossibilité par rebrassage sur un groupe | libre ; parenté classique (piste) | **libre comme énoncé ; son miroir est maintenant porté sur PDF** : tests séquentiels de l'échangeabilité, et rôle de la filtration (aucune surmartingale non triviale dans la filtration d'origine, pour une suite binaire). Un statisticien rapprochera « le groupe compte » de « la filtration compte » : ce n'est pas le même énoncé | 2210.01948, p. 15 [T6], [T12] ; 2203.03532, p. 8 [S19], p. 11 [S8] |
| La parade (agrégateur d'autocorrélation ou de co-élévation) | non jugée à part par C2 | **occupée comme outil** pour deux flux et pour l'échangeabilité ; non revendiquée par N-003, mais le programme § 3 l'énonce sans citer | section 4.1 |
| T3, garanties trajectorielles des statistiques locales face à un attaquant adaptatif | libre | inchangé : aucune des trois pièces ne pose d'attaquant qui réarrange | — |
| Classes C et K, signes | libre | inchangé | — |
| Unification du temps et des agents par sous-groupes de permutations | libre ; mise en forme | inchangé. L'invariance de groupe de la synthèse porte sur d'autres groupes | 2210.01948, p. 11 [T13] |
| Mesure sur activations | libre | inchangé : aucune occurrence d'agents, de modèles ni de sondes | — |

**Verdict : le « occupé en partie » de C2 tient pour L et pour T.** Deux glissements à l'intérieur de ce verdict :
- **L se resserre.** Avec la remarque 2.7 de 2203.03532, les morceaux « prix de la garantie » et « coût du report » ne sont plus libres dans leur idée. Ce qui reste propre au programme dans L : l'énoncé adverse à budget borné (invariances exactes, borne fonction du seul budget, chiffres) et la mesure sur scores de sondes. Je rejoins C2 : l'estimation d'originalité « environ 0,4 » de N-004 est un plafond.
- **T ne bouge pas dans sa revendication**, mais sa phrase « il faut un agrégateur d'autocorrélation ou de co-élévation » doit citer des outils existants.

### 4.3 H2

Énoncé retenu (N-007) : accumulation additive toujours valide de scores de sondes de l'agent qui agit, rappel qui croît avec l'horizon, seuil réglé sur épisodes honnêtes sans exemple de sabotage.

- **Aucune des trois pièces n'occupe H2** : elles ne traitent ni agents, ni sondes, ni sabotage sous un seuil par action.
- Elles portent ce que H2 **utilise** : l'accumulation par surmartingale de mélange (2210.01948, p. 13) ; la croissance de l'évidence avec le temps sous une alternative persistante (p. 8 [T5]) ; le détecteur de rupture demandé par la lecture « alarme avant le dommage » (2203.03532).
- **Un point à tenir au préenregistrement de G1.** Si l'agrégateur comprend un détecteur de rupture, la garantie publiée au seuil 1/α est une durée moyenne avant fausse alarme [S13], [S15], non une probabilité sur l'horizon de l'épisode. La lecture de « toujours valide » retenue par N-007 (uniforme sur l'épisode, réglée sur épisodes honnêtes entiers) n'est donc pas donnée par le théorème 2.4 ; elle l'est par la variante de la remarque 2.7, avec son prix [S5], ou par le réglage empirique. Ceci est un constat de lecture, non une proposition de changement.

## 5. Pièces à citer comme outil, non à revendiquer

| Pièce | À citer pour | Ce que le programme ne doit pas présenter comme sien |
|---|---|---|
| 2203.03532 (Shin, Ramdas, Rinaldo) | le détecteur de rupture à garantie non asymptotique sous hypothèse nulle composite et sans indépendance (p. 3, 7) ; l'arbitrage entre contrôle de la probabilité de fausse alarme et délai (p. 8) ; le délai d'ordre log(1/α) sur la divergence (p. 19) ; le détecteur d'un passage à la dépendance (p. 11) | l'idée qu'un processus cumulé depuis l'origine paie le report ; l'idée d'un détecteur de rupture par e-valeurs |
| 2210.01948 (Ramdas, Grünwald, Vovk, Shafer) | la borne de mélange et l'inégalité de Ville (p. 13) ; la forme « somme et variance cumulée » (p. 16) ; les tests séquentiels d'échangeabilité (p. 15) ; la moyenne d'e-valeurs dépendantes (p. 7) | le cœur statistique de L (déjà dit « classique » par N-004) ; l'existence de tests toujours valides de l'échangeabilité |
| 2212.07383 (Podkopaev et collègues) | l'agrégateur toujours valide de co-élévation entre deux flux (p. 3, 7, 8, 9), avec sa condition de validité | l'existence d'un agrégateur de dépendance à garantie toujours valide |

## 6. Écarts relevés dans les documents du programme (sans les modifier)

- `docs/programme-controle-ia-v2.md` § 3 : « il faut un agrégateur d'autocorrélation (dans le temps) ou de co-élévation (entre agents) » est écrit sans référence. Des outils publiés existent (section 4.1).
- Décision N-004, « Sécurité avant le dommage » : « (Page, détecteurs e) » sans référence. La pièce est 2203.03532 ; sa garantie par défaut est la durée moyenne avant fausse alarme (section 4.3).
- Décision N-004, revendication de L : « borne toujours valide, coût du report » ; antécédent qualitatif en 2203.03532, p. 8 (section 4.2).
- Décision N-035, section 3 : Cemri y est résumé de mémoire comme comptant « le non-respect de la spécification et la perte d'historique entre agents ». Vérifié sur PDF : les deux modes existent (p. 17 [K1], [K2]) ; la perte d'historique n'y est pas définie « entre agents » mais comme une troncature de contexte.

## 7. Pièces à récupérer sur le réseau

Vérification sur disque limitée aux cinq pièces du lot. Titres relevés dans les bibliographies des pièces lues, sauf mention « de mémoire » : **pistes, non vérifiées**.

| Pièce | Pourquoi |
|---|---|
| arXiv 2608.07556 « MasDrift » ; 2608.24569 ; 2609.27900 ; 2605.10481 ; 2607.07097 (signalées par un chercheur, non lues) | H9 : le verdict de ce rapport ne les couvre pas ; à lire avant toute revendication |
| Sourbut, Hammond et Wood (2024), « Cooperation and Control in Delegation Games » (Hammond, p. 89) | citée par Hammond à l'appui de la phrase sur les buts déformés à la délégation (p. 24) : voisin direct de H9, peut-être formel |
| Nguyen et collègues (2024b), « Distortion Resilience for Goal-Oriented Semantic Communication » (Hammond, p. 81) | même phrase ; probablement loin (communication), à écarter sur pièce |
| Acerbi et Stubbersfield (2023), « Large language models show human-like content biases in transmission chain experiments » (Hammond, p. 53) | expérience de chaîne de transmission avec des modèles : plan de mesure par passage, voisin de H9 |
| Vovk (2021), « Testing randomness online » ; Volkhonskiy et collègues (2017) ; Vovk, Gammerman et Shafer, « Algorithmic learning in a random world » | tests et détection séquentiels des écarts à l'échangeabilité : la parade dans le temps, et le miroir de T2 |
| Ramdas, Ruf, Larsson et Koolen, « Testing exchangeability: Fork-convexity, supermartingales and e-processes » | impossibilité de surmartingales non triviales pour l'échangeabilité : à confronter à T2 et à « le groupe compte » |
| Chwialkowski et Gretton (2014), « A kernel independence test for random processes » (2212.07383, p. 14) | indépendance entre deux séries à mémoire : co-élévation entre agents quand chaque agent a une dépendance sérielle |
| Shekhar et Ramdas (2023), « Sequential change detection via backward confidence sequences » (2203.03532, p. 36) | détection de rupture sans classes fixées d'avance : complément du détecteur de N-004 |
| Howard, Ramdas, McAuliffe et Sekhon (2021) | source propre de la borne de mélange (déjà demandée par C2) |
| Ramtin et collègues, adversaire non stationnaire (référence [12] de 2601.20022, déjà demandée par C2) | reste le voisin le plus probable d'un délai sous dérive étalée, que les pièces de ce lot ne traitent pas |

## 8. Refus rencontrés

Aucun. Aucun appel au réseau, aucun modèle, aucune machine, aucune dépense. `diag/`, `runs/`, `donnees/` non ouverts. Aucune autre branche ouverte. Rien d'écrit hors de ce rapport, de son empreinte compagnon et du dossier temporaire du lot.

## Annexe A — citations exactes contrôlées

Format : identifiant | pièce (dans `docs/sources/pdf/niveau3-v1/lot5/`) | page du fichier | citation.

- K1 | 2503.13657v3.pdf | p. 17 | « FM-1.1: Disobey task specification - Failure to adhere to the specified constraints or requirements of a given task, leading to suboptimal or incorrect outcomes. »
- K2 | 2503.13657v3.pdf | p. 17 | « FM-1.4: Loss of conversation history - Unexpected context truncation, disregarding recent interaction history and reverting to an antecedent conversational state. »
- K3 | 2503.13657v3.pdf | p. 7 | « These include failing to follow task requirements (FM-1.1, 11.8%) or agent roles (FM-1.2, 1.5%), step repetitions (FM-1.3, 15.7%), context loss (FM-1.4, 2.80%), or not recognizing task completion (FM-1.5, 12.4%). »
- K4 | 2503.13657v3.pdf | p. 2 | « We define failures as instances where the MAS does not achieve its intended task objectives. »
- K5 | 2503.13657v3.pdf | p. 8 | « Systems with explicit verifiers like MetaGPT and ChatDev generally show fewer total failures (Figure 4), indicating explicit checks help. However, the presence of a verifier is not a silver bullet »
- K6 | 2503.13657v3.pdf | p. 8 | « adding a high-level task objective verification step to ChatDev yields a +15.6% improvement in task success on ProgramDev »
- K7 | 2503.13657v3.pdf | p. 2 | « The percentages shown represent the prevalence of each failure mode and category as observed in our analysis of 1642 MAS execution traces. »
- K8 | 2503.13657v3.pdf | p. 7 | « we identify deeper causes: (1) flaws in MAS design regarding agent roles and workflow, (2) poor user prompt specifications, or (3) limitations of the underlying LLM »
- K9 | 2503.13657v3.pdf | p. 4 | « focusing on aggregate performance or high-level objectives like trustworthiness and security [33, 34] »
- K10 | 2503.13657v3.pdf | p. 45 | « But then the agent comes back to lightgbm as the last interactions do not exist. »
- K11 | 2503.13657v3.pdf | p. 8 | « sole reliance on final-stage, low-level checks is inadequate »
- K12 | 2503.13657v3.pdf | p. 7 | « withholding crucial information (FM-2.4, 0.85%) »
- K13 | 2503.13657v3.pdf | p. 2 | « 2.4 Information Withholding (0.80%) »
- K14 | 2503.13657v3.pdf | p. 8 | « System Design Issues (41.8%) »
- M1 | 2502.14143v1.pdf | p. 24 | « Another increasingly important framework is the use of individual AI agents as part of teams and scaffolded chains of delegation, which transmit not only information but instructions or goals through networks of agents. »
- M2 | 2502.14143v1.pdf | p. 24 | « If these goals are distorted or corrupted, then this can lead to worse outcomes for the delegating agent(s) (Nguyen et al., 2024b; Sourbut et al., 2024). »
- M3 | 2502.14143v1.pdf | p. 24 | « the rate of correct answers fell from about 96% initially to under 60% by the eighth rewrite »
- M4 | 2502.14143v1.pdf | p. 24 | « typically leading to a different message at the end of the chain than at the beginning »
- M5 | 2502.14143v1.pdf | p. 51 | « After each rewrite, a new GPT-3.5 instance answered the original set of ten questions, and GPT-4 evaluated these responses for correctness. »
- M6 | 2502.14143v1.pdf | p. 26 | « in a network context the main problem may be that information becomes slightly more biased every time it passes through the system »
- M7 | 2502.14143v1.pdf | p. 26 | « Current tools for evaluation and monitoring cannot always be applied to networks of agents or agents situated within those networks. »
- M8 | 2502.14143v1.pdf | p. 41 | « Many researchers have proposed improving the safety AI agents by using other agents as ‘overseers’ »
- M9 | 2502.14143v1.pdf | p. 40 | « can be completed by carefully delegating sub-tasks to the relevant model »
- M10 | 2502.14143v1.pdf | p. 81 | « “Distortion Resilience for Goal-Oriented Semantic Communication” »
- M11 | 2502.14143v1.pdf | p. 89 | « “Cooperation and Control in Delegation »
- M12 | 2502.14143v1.pdf | p. 42 | « decentralised, distributed networks of agents could be used to assist with the monitoring and detecting of security threats (Hasan et al., 2024) and prevent local breaches from cascading through the system »
- M13 | 2502.14143v1.pdf | p. 24 | « we ran a small experiment on 100 BuzzFeed news articles »
- M14 | 2502.14143v1.pdf | p. 24 | « These examples demonstrate how information can degrade as it propagates through networks of AI systems, even without malicious intent. »
- S1 | 2203.03532v4.pdf | p. 1 | « We develop a fundamentally new and general framework for sequential change detection when the pre- and post-change distributions are nonparametrically specified (and thus composite). »
- S2 | 2203.03532v4.pdf | p. 3 | « Despite handling composite pre- and post-change distributions, even without an iid (independent and identically distributed) assumption on the data, our e-CUSUM and e-SR sequential change detection procedures based on e-detectors can always nonasymptotically control the ARL at level α. »
- S3 | 2203.03532v4.pdf | p. 6 | « We do not assume the observations in the sequence to be independent or identically distributed: each P ∈ P is a distribution over an infinite sequence of random variables. »
- S4 | 2203.03532v4.pdf | p. 6 | « It may be helpful to imagine an adversary who adaptively decides at each step whether or not to “stop” the pre-change data. »
- S5 | 2203.03532v4.pdf | p. 8 | « The price to pay is that if there is a change at time ν, then the detection delay will no longer be independent of ν, and will typically increase logarithmically with ν (so that the worst average delay is unbounded). »
- S6 | 2203.03532v4.pdf | p. 8 | « which is a much more stringent error metric than the ARL »
- S7 | 2203.03532v4.pdf | p. 11 | « it delivers a novel e-detector for a change from independence to dependence »
- S8 | 2203.03532v4.pdf | p. 11 | « The conformal sequential change detection procedures by [44, 43] are designed to test deviations from exchangeability »
- S9 | 2203.03532v4.pdf | p. 13 | « are independent of the pre-change observations and form a strongly stationary process »
- S10 | 2203.03532v4.pdf | p. 19 | « as α → 0, matching the rate of the known lower bounds [18] »
- S11 | 2203.03532v4.pdf | p. 12 | « which can be plugged into e-detectors to yield a valid e-detector in the presence of adversarial corruptions »
- S12 | 2203.03532v4.pdf | p. 6 | « All of our results on ARL do not require any assumptions on the changepoint ν or post-change distribution of the data. »
- S13 | 2203.03532v4.pdf | p. 7 | « That is, the sequential change detection procedure in (7) controls the ARL at level α. »
- S14 | 2203.03532v4.pdf | p. 11 | « The same methods work even when the distribution is allowed to drift within P before the changepoint, and drift within Q after the changepoint. »
- S15 | 2203.03532v4.pdf | p. 2 | « We say that the “ARL is controlled at level α” if »
- S16 | 2203.03532v4.pdf | p. 12 | « if P and Q were swapped, the testing problem is much harder, and we are not aware of any powerful test or change detection method »
- S17 | 2203.03532v4.pdf | p. 19 | « are iid samples from a »
- S18 | 2203.03532v4.pdf | p. 7 | « For any α ∈ (0, 1) and e-detector M , if we declare a changepoint at the stopping time »
- S19 | 2203.03532v4.pdf | p. 8 | « See [29] for one such example, arising from sequentially testing exchangeability of a binary sequence »
- T1 | 2210.01948v2.pdf | p. 13 | « choosing a centered Gaussian with variance ρ2 as a mixing distribution F »
- T2 | 2210.01948v2.pdf | p. 13 | « If µi differs for each i, an identical argument shows that (22) is a CS for the »
- T3 | 2210.01948v2.pdf | p. 13 | « This type of adaptivity is a commonly observed benefit of the method of mixtures, if appropriately employed. »
- T4 | 2210.01948v2.pdf | p. 16 | « where sumt is the sum of the observed random variables, and variancet captures their cumulative variance »
- T5 | 2210.01948v2.pdf | p. 8 | « minimizes expected time before E reaches a desired threshold »
- T6 | 2210.01948v2.pdf | p. 15 | « find that no nontrivial test supermartingale exists (in the original filtration), but they exhibit a nontrivial and powerful e-process based on universal inference »
- T7 | 2210.01948v2.pdf | p. 15 | « who use conformal test martingales to detect deviations from exchangeability »
- T8 | 2210.01948v2.pdf | p. 16 | « the best possible detection delay for any method with ARL at least 1/α scales like »
- T9 | 2210.01948v2.pdf | p. 17 | « the first sequential nonparametric independence testing framework was developed in Podkopaev et al. (2023), which allows random variables to lie in general spaces and also handles non-i.i.d. settings »
- T10 | 2210.01948v2.pdf | p. 16 | « E-detectors only work when P and Q are prespecified and non-intersecting »
- T11 | 2210.01948v2.pdf | p. 7 | « then (E1 + E2 )/2 is as well, even if E1 and E2 are dependent »
- T12 | 2210.01948v2.pdf | p. 15 | « by shrinking the filtration to include only conformal p-values, it is once again possible to design nontrivial test martingales »
- T13 | 2210.01948v2.pdf | p. 11 | « it was recently discovered that for group invariant problems, such a reduction to a simple null leads to e-processes that have both GROW and REGROW status »
- T14 | 2210.01948v2.pdf | p. 13 | « Darling and Robbins (1968) constructed CSs for »
- T15 | 2210.01948v2.pdf | p. 13 | « running mean » (suite de T2 ; la mise en page sur deux colonnes y intercale un signe de formule)
- P1 | 2212.07383v4.pdf | p. 1 | « Our test is also valid under non-i.i.d. time-varying settings. »
- P2 | 2212.07383v4.pdf | p. 3 | « We provide theoretical guarantees on time-uniform type I error control for these tests »
- P3 | 2212.07383v4.pdf | p. 3 | « A common practice of using a permutation p-value for batch independence testing requires (X, Y )-pairs to be i.i.d. (more generally, exchangeable). »
- P4 | 2212.07383v4.pdf | p. 3 | « meaning that either the distribution of X may change or that of Y may change, but not both simultaneously »
- P5 | 2212.07383v4.pdf | p. 7 | « SKIT ever stops with probability at most α »
- P6 | 2212.07383v4.pdf | p. 8 | « Our tests can also be used to test instantaneous independence between two streams. »
- P7 | 2212.07383v4.pdf | p. 9 | « The cross-links between X and Y streams are not allowed »
- P8 | 2212.07383v4.pdf | p. 9 | « we make no assumptions of mixing or stationarity anywhere »
- P9 | 2212.07383v4.pdf | p. 8 | « we provide an example that shows that this assumption is necessary for the validity of our tests »
- P10 | 2212.07383v4.pdf | p. 5 | « The validity of the resulting test then follows from Ville’s inequality [31]. »
- P11 | 2212.07383v4.pdf | p. 3 | « For a stream of independent data »
- P12 | 2212.07383v4.pdf | p. 9 | « Chwialkowski and Gretton [4] considered a related (at a high level) problem of testing instantaneous independence between a pair of time series. »
- P13 | 2212.07383v4.pdf | p. 7 | « we show that the wealth process grows exponentially and characterize the rate of the growth of wealth in terms of the true HSIC score »
- P14 | 2212.07383v4.pdf | p. 2 | « We work in a very general composite nonparametric setting »
