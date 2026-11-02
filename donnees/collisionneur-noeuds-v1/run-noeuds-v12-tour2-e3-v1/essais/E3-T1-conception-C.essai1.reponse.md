# Attaque des recommandations du tour 2 — Proposition C

**Règle 2 (intégrité des pièces) :** La synthèse servie en FAITS rapporte que la pièce 20 (N9-1) du tour 1 s'arrête au milieu d'une phrase à la fin de son bornage (« dans toute la population restée non ») [VÉRIFIÉ] ; les faits de 45 811 mots du tour 1 ne sont pas resservis ici, mais leur synthèse complète est présente et intègre [VÉRIFIÉ]. Aucun contenu n'est inventé au-delà de ce qui est servi.
**Portée :** Conformément à la synthèse des faits (« Zéro passage hors question : aucune cellule ne traite N2, N7 ni N8 ») et à l'annexe (« retiré (tranché) »), N2, N7 et N8 ne sont pas traités.

---

## 1. Verdicts sur les recommandations de l'annexe (v5)

### N1 — Recommandation : Option B (confiance d'auteur 0,6)
* **Verdict :** **Tenue sous condition** (condition : déclaration explicite du changement de critère gelé après lecture dans une version nouvelle, tirage de graines entièrement nouvelles sur la plage 500–799, rapport de l'ancienne grandeur sans seuil, plancher d'effectif par statut et condition sous peine de porte fausse, et exécution d'un test d'invariance après scellement égalisant post hoc les fréquences des statuts d'opérateur à vérité et proximité fixes).
* **Raison :** Le diagnostic servi (OBSERVÉ-NON-AUDITÉ sur 200 mondes et une graine) indique que l'échec initial (écart 2,87 contre seuil 0,5 [VÉRIFIÉ]) vient de la sensibilité de la définition à la rareté marginale des concepts (écarts de 0,33 et 0,84 subsistants sous les variantes de générateur G3 [RAPPORTÉ]), tandis que la nouvelle grandeur a une erreur type de 0,04 à 0,11 par statut [RAPPORTÉ]. Toutefois, comme la nouvelle grandeur retire la garde contre la fuite de statut, elle ne tient qu'assortie d'un contrôle de sensibilité et du plancher d'effectif identifié par A et D au tour 1.
* **Pire cas et garde :** *Pire cas :* Un bras bat ses témoins en exploitant la rareté extrême des jumeaux du statut d'opérateur ou échoue à être évalué faute d'effectif dans une case. *Garde :* Plancher d'effectif rendant la porte fausse si une moyenne conditionnelle n'est pas définie, et déclencheur d'audit par test d'invariance post hoc si le gain disparaît sur les seuls vrais conceptuels.
* **Changement par rapport au tour 1 :** Maintien de ma position B′ de T3 (où j'avais déjà corrigé ma plage de graines de 300–599 à 500–799 sur critique de D et remplacé le masquage par le test d'invariance post hoc) ; j'y intègre formellement le plancher d'effectif de A et D.

### N3 — Recommandation : D-j Oui (confiance 0,7 ; substitut S31 à 0,4)
* **Verdict :** **Tenue sous condition** (condition : empreinter la source et le script du substitut S31 à l'étape zéro ; exécuter un test de rétrodiction avec coupure temporelle stricte séparant la fenêtre de réglage des seuils et la fenêtre aveugle de test contre deux bases gratuites — popularité et ancienneté — avec un plus petit gain utile gelé d'avance ; étiqueter le bras « substitut » et le passer en « non produit » sans bloquer la porte si la source manque ou si le gain est sous le seuil).
* **Raison :** Le vocabulaire du contrôle étant absent des 37 960 concepts des auteurs [HYPOTHÈSE — marqué SUPPOSÉ par la question v12], le bras évalué ne peut être qu'un substitut sur une autre source, ce que la garde A19 prévoit déjà [VÉRIFIÉ]. La confiance basse de l'auteur sur S31 (0,4) confirme qu'il faut verrouiller le risque d'homonymie et d'inutilité dès l'étape zéro par la coupure temporelle et le seuil de gain utile gelé (convergences de T3 avec A et D).
* **Pire cas et garde :** *Pire cas :* Le substitut forme des paires sur des homonymes de physique ou ne capte que la popularité et l'ancienneté, consommant trois fusions (≈ 1,88 USD [RAPPORTÉ]) à perte. *Garde :* Filtre lexical excluant les homonymes relevés et bascule automatique en « non produit » à l'étape zéro si le test sur fenêtre disjointe ne bat pas les bases gratuites d'au moins le gain utile gelé.
* **Changement par rapport au tour 1 :** Aucun changement par rapport à ma position de T3 ; j'adopte explicitement le « plus petit gain utile gelé avant le test » de D.

### N4 — Recommandation : Option (a) (confiance 0,5 ; CA1-04 non tranché)
* **Verdict :** **Tenue sous condition** (condition : renommer le verdict du pré-pilote « chaîne éprouvée, profil non éprouvé » ; corriger les deux défauts majeurs de la grille — retirer du profil la paire de niches que le programme fusionne lui-même et déclarer en tête la niche sans partenaire — ; trancher CA1-04 en excluant du compte à la fois les jeux de données et les trois structures séquentielles quasi universelles imposées par le texte servi ; vérifier la non-vacuité sur jeu étiqueté indépendant sous la loi de l'annexe et sous la loi la plus défavorable où la niche d'évaluation est à 0,35).
* **Raison :** À au plus dix fiches et une seule paire méta, le pré-pilote ne peut statistiquement pas éprouver le contraste entre profil et repli (probabilité de zéro paire dans le profil de 0,6 à 0,7 à six fiches et 0,25 à 0,36 à dix fiches [VÉRIFIÉ]), rendant (a) nécessaire. Laisser CA1-04 non tranché laisserait passer en course des paires « dans le profil » qui ne partagent qu'une structure séquentielle imposée par la consigne elle-même [RAPPORTÉ].
* **Pire cas et garde :** *Pire cas :* Une fusion de repli ou fondée sur une structure imposée par la consigne est comptée comme réussite du profil méta en course. *Garde :* Drapeau obligatoire « profil / repli / non produit » dans la règle de reconduction et exclusion symétrique des jeux de données et des structures séquentielles imposées avant de rejouer le script de non-vacuité.
* **Changement par rapport au tour 1 :** Maintien de ma position de T3 (où j'avais retiré ma proposition T1 de modifier la table des distances et l'ordre de choix sur les critiques de A et D, et intégré la loi défavorable de B).

### N5 — Recommandation : Option (a) (confiance 0,7 ; CL19 notant aussi « mieux : ne pas lire », soit (b))
* **Verdict :** **Tenue sous condition** (condition : amendement explicite de A21 avant le gel, sans traiter le code existant comme un défaut de fait ; contre-lecture de l'archive scellée ; hachage de l'état du coffre et du journal après l'étape litigieuse ; et réussite du test d'invariance exacte du message de sortie et de l'ordre des appels sous 1 000 permutations de la clé à comptes agrégés constants — tout échec de ce test basculant automatiquement la décision vers l'option (b)).
* **Raison :** Appliquer A21 à la lettre rend l'étape litigieuse inexécutable car ses gardes dépendent de la classe des témoins [VÉRIFIÉ], et la version récente corrige l'ordre des identifiants et supprime la copie en mémoire [RAPPORTÉ]. Toutefois, la remarque de CL19 (« mieux que l'amendement : ne pas lire ») et la critique de A et D au tour 1 (le processus qui détient la clé écrit lui-même le journal) imposent que (a) soit subordonnée à la preuve mécanique d'invariance exacte sur laquelle les quatre espèces ont convergé en T3.
* **Pire cas et garde :** *Pire cas :* Fuite de l'appartenance aux classes par l'ordre des appels ou par une dimension supplémentaire de la sortie, ou création d'un précédent où le code déjà écrit vaut décision par défaut. *Garde :* Amendement formel requis avant gel, validateur de schéma refusant toute dimension supplémentaire (emprunté à A), hachage du coffre, et bascule en boîte externe (b) à la moindre variance sous permutation de clé.
* **Changement par rapport au tour 1 :** Maintien de ma position (a) de T3, mais j'intègre le validateur de schéma de A et le principe de hiérarchie de D (aucun défaut de fait).

### N6 — Recommandations sur le semi-réel (brouillon 5) : DL-1 à DL-13

* **DL-1 — Recommandation : (2) (confiance 0,65)**
  * **Verdict :** **Tenue**.
  * **Raison :** Accord large à quatre au tour 1 [VÉRIFIÉ] ; le second volet est celui qui porte l'identification causale pertinente.
  * **Pire cas et garde :** *Pire cas :* Défaillance sur le volet non décisif masquée par le succès du volet décisif. *Garde :* Rapporter le contraste apparié entre réseau conforme et réseau libre en descriptif.
  * **Changement T1 :** Aucun.

* **DL-2 — Recommandation : (2) (confiance 0,55)**
  * **Verdict :** **Tenue**.
  * **Raison :** Accord large à quatre au tour 1 [VÉRIFIÉ] ; la marge de temps (150 / 118,6 = 1,264 ou 140 / 118,6 = 1,180 [VÉRIFIÉ sur estimations SUPPOSÉ]) est compatible avec le budget de calcul.
  * **Pire cas et garde :** *Pire cas :* Dépassement du budget de temps sur les combinaisons les plus lourdes (jusqu'à 135,7 h [SUPPOSÉ]). *Garde :* Plafond d'exécution par graine et journalisation des arrêts.
  * **Changement T1 :** Aucun.

* **DL-3 — Recommandation : (1) décisionnelle (confiance 0,6)**
  * **Verdict :** **Renversée (remplacée par l'option (2) : descriptive, assortie du déclencheur d'audit de A conditionné à la puissance prévue)**.
  * **Raison :** La condition à effet négatif teste la symétrie de signe sous affectation au hasard (donc relève de l'estimation et non de l'hypothèse économique) et son maintien en décision abaisse la conjonction de recouvrement de 0,852 à 0,818 [VÉRIFIÉ]. Trois espèces sur quatre (A, C, D) ont convergé sur (2) au tour 1 [VÉRIFIÉ].
  * **Pire cas et garde :** *Pire cas :* Si la recommandation (1) était suivie, rejet à tort par perte de puissance conjonctive ; sous (2), un vrai défaut de signe ne coûte rien en décision. *Garde :* Déclencheur d'audit de A si l'écart de signe dépasse le seuil à la puissance prévue.
  * **Changement T1 :** Maintien de mon option (2) de T1/T3, enrichie du déclencheur d'audit de A.

* **DL-4 — Recommandation : (1) (confiance 0,85)**
  * **Verdict :** **Tenue**.
  * **Raison :** Donner les cibles observées à la méthode revient à lui fournir ce qui fait l'identification [VÉRIFIÉ]. Accord à quatre au tour 1.
  * **Pire cas et garde :** *Pire cas :* Réintroduction implicite d'une information de cible dans le prétraitement. *Garde :* Vérification mécanique que le vecteur des cibles n'est passé en argument à aucune fonction de la méthode.
  * **Changement T1 :** Aucun.

* **DL-5 — Recommandation : (1) (confiance 0,55, « demander au collisionneur »)**
  * **Verdict :** **Tenue sous condition** (condition : recalculer la puissance et la taille d'échantillon de l'étape d'estimation au seuil de qualification réel de la table, 0,70, et non à la corrélation supposée de 0,85).
  * **Raison :** Convergence indépendante de A, C et D au tour 1 [VÉRIFIÉ] : opérer au seuil 0,70 alors que la puissance est calculée à 0,85 sous-dimensionne l'épreuve (sous l'approximation quadratique, (0,85 / 0,70)² = 1,4745, portant 2 600 paires-années à 3 834 [VÉRIFIÉ], ou par simulation directe sans approximation comme le demande D).
  * **Pire cas et garde :** *Pire cas :* Sous-puissance sévère de l'étape d'estimation lorsque l'instrument qualifié est proche de 0,70. *Garde :* Exiger la puissance cible au point frontière 0,70 par simulation sur monde jouet avant le gel.
  * **Changement T1 :** Aucun (j'inclus la réserve de D : vérifier le multiplicateur par simulation plutôt que par la seule formule de non-centralité).

* **DL-6 — Recommandation : (1) (confiance 0,7)**
  * **Verdict :** **Tenue sous condition** (condition : appliquer (1) aux trois exemplaires déjà versés et empreintés, et soit verser le quatrième exemplaire avant le gel, soit geler sous (2) pour ce seul quatrième papier avec la mention explicite « SUPPOSÉ — hypothèse non lue sur exemplaire » dès lors qu'aucun chiffre de ce papier n'entre dans une règle de décision).
  * **Raison :** Trois exemplaires sont versés, le quatrième manque [VÉRIFIÉ]. Bloquer tout le calendrier de calcul (gel prévu le 4 novembre [SUPPOSÉ]) pour un papier qui n'entre dans aucun seuil numérique (constat de A en T1) est disproportionné si la marque SUPPOSÉ est maintenue.
  * **Pire cas et garde :** *Pire cas :* Une règle de code prête au quatrième papier une formule qu'il ne contient pas. *Garde :* Interdiction d'utiliser tout paramètre numérique tiré du quatrième papier sans empreinte SHA-256 préalable.
  * **Changement T1 :** Aucun.

* **DL-7 — Recommandation : (2) (confiance 0,7)**
  * **Verdict :** **Tenue**.
  * **Raison :** Accord à quatre au tour 1 [VÉRIFIÉ] pour le gel des seuils sous cette forme.
  * **Pire cas et garde :** *Pire cas :* Dérive d'un seuil implicite dans le code hors table. *Garde :* Table unique des seuils hachée et importée par le script.
  * **Changement T1 :** Aucun.

* **DL-8 — Recommandation : (4) (confiance 0,7)**
  * **Verdict :** **Tenue**.
  * **Raison :** Seule option procurant le gain de puissance chiffré (0,78 contre 0,49 [RAPPORTÉ]). Accord à quatre au tour 1.
  * **Pire cas et garde :** *Pire cas :* Le gain de puissance dépend d'une paramétrisation fragile de la variable auxiliaire. *Garde :* Gel exact de la spécification de l'auxiliaire avant tirage des mondes de décision.
  * **Changement T1 :** Aucun.

* **DL-9 — Recommandation : (1) décisionnelle (confiance 0,55)**
  * **Verdict :** **Renversée (remplacée par l'option (2) : descriptive)**.
  * **Raison :** Bien que la règle d'orientation soit vérifiée sur l'exemplaire empreinté (p. 9, § 5.1 [VÉRIFIÉ]), les deux seuils numériques choisis n'ont aucun appui dans la littérature [VÉRIFIÉ]. Faire dépendre le verdict d'arrêt de deux seuils arbitraires expose l'épreuve à un faux rejet ; trois espèces sur quatre (A, C, D) ont choisi (2) au tour 1.
  * **Pire cas et garde :** *Pire cas :* Sous (1), rejet de l'épreuve à cause d'un seuil d'orientation mal calibré ; sous (2), orientation aberrante ignorée. *Garde :* Rapporter le témoin d'orientation en descriptif avec ses intervalles sur toute une grille de seuils.
  * **Changement T1 :** Aucun.

* **DL-10 — Recommandation : (1) aucune condition, avec limite écrite (confiance 0,55)**
  * **Verdict :** **Tenue**.
  * **Raison :** L'épreuve sous affectation biaisée « ne fait que vérifier que les effets fixes ferment un chemin que l'on connaît » [VÉRIFIÉ], ce qui la rend presque vraie par construction. Économiser 5,0 heures de calcul [SUPPOSÉ] en écrivant la limite est cohérent (position de C et D au tour 1).
  * **Pire cas et garde :** *Pire cas :* Une erreur d'implémentation des effets fixes laisse le chemin ouvert sans qu'on le voie. *Garde :* Test unitaire instantané sur un seul monde jouet déterministe vérifiant l'annulation algébrique de l'effet fixe avant le gel.
  * **Changement T1 :** Aucun.

* **DL-11 — Recommandation : (1) (confiance 0,6)**
  * **Verdict :** **Tenue**.
  * **Raison :** Accord à quatre au tour 1 [VÉRIFIÉ] pour fermer la rétroaction de la sortie.
  * **Pire cas et garde :** *Pire cas :* Couplage résiduel entre sorties successives. *Garde :* Vérification d'indépendance des graines d'évaluation.
  * **Changement T1 :** Aucun.

* **DL-12 — Recommandation : (1) (confiance 0,6, « demander au collisionneur » ; VS5-01 conteste l'avantage prêté à (1))**
  * **Verdict :** **Indécidable sans la pièce X** (pièce X : exécution du paragraphe concerné du script déjà versé sur monde jouet en quelques dizaines de secondes de processeur — 0 USD — simulant effectivement les ensembles acceptés par la méthode de prédiction invariante, plus la lecture intégrale de la vérification VS5-01 dont seules dix lignes étaient servies).
  * **Raison :** La vérification VS5-01 démontre que le centrage par strate annule, dans chaque environnement, les moyennes résiduelles de tout ensemble sans la cause, rendant inexact l'avantage prêté à l'option (1) pour la prédiction invariante, tandis que le déclencheur de symétrie censé l'attraper ne peut pas sonner [VÉRIFIÉ]. De plus, comme A l'a établi au tour 1, le monde jouet servi n'a pas simulé les ensembles acceptés par cette méthode [VÉRIFIÉ]. En T3, j'ai retiré mon option hybride (réfutée par A, B et D) et convergé avec A et D sur ce test sur monde jouet avant le gel.
  * **Pire cas et garde :** *Pire cas :* Si (1) est gelée à l'aveugle, la méthode de prédiction invariante s'abstient presque toujours ou accepte tout sans que le déclencheur de symétrie ne sonne. *Garde :* Corriger le déclencheur de symétrie, rapporter les quatre estimateurs de D (part d'ensembles non vides, inclusion de la cause, inclusions du leurre et du jumeau, abstention sous confusion), et conditionner le choix entre (1) et l'alternative au résultat du monde jouet avant le gel.
  * **Changement T1 :** Conforme à ma cession de T3 (retrait de l'hybride, adoption du test préalable sur monde jouet avec A et D).

* **DL-13 — Recommandation : (1) descriptifs (confiance 0,55, « demander au collisionneur »)**
  * **Verdict :** **Tenue sous condition** (condition : ajouter le déclencheur d'audit proposé par A au tour 1 à la place de l'option 2 décisionnelle).
  * **Raison :** Accord à quatre au tour 1 sur (1) pour ne pas dégrader la puissance conjonctive par des gardes mal calibrées [VÉRIFIÉ], mais un déclencheur d'audit sans arrêt automatique préserve la vigilance si un garde-fou dévie fortement.
  * **Pire cas et garde :** *Pire cas :* Un garde-fou descriptif révèle une anomalie majeure mais le verdict principal est publié sans examen. *Garde :* Déclencheur d'audit obligatoire suspendant la clôture jusqu'à inspection si le garde-fou franchit le seuil d'alerte.
  * **Changement T1 :** Maintien de (1) avec adoption de l'apport de A (déclencheur d'audit).

### N9 — Recommandation : Option (a) (population fin 2022, fenêtre 01/01/2023 – 30/09/2026)
* **Verdict :** **Tenue sous condition** (condition : garde mécanique retirant de la liste tout concept dont la première arête est postérieure au 31 décembre 2022 ; tolérance du pont de comptes sur les trois années antérieures fixée d'avance ; rapport secondaire par cohorte d'année d'apparition sur l'ensemble à risque commun avec effectif minimal de positives et règle de regroupement des cases écrite avant lecture ; maintien de B-i ≥ 0,85 et B-ii > 0,60 [SUPPOSÉ] comme conjointement décisifs).
* **Raison :** L'option (b) conditionne l'échantillon sur une variable postérieure aux traits (l'absence de liaison en 2023) et retire d'abord les positives les mieux classées, faussant l'aire et l'appariement [VÉRIFIÉ]. Toutefois, sous (a), la liste de concepts extraite des résumés peut fuir si un concept n'a d'arête qu'après la coupure (critique de A que j'ai adoptée en T3), et des cases d'appariement vides rendraient l'aire indéfinie (critique de A et D).
* **Pire cas et garde :** *Pire cas :* Fuite temporelle par des concepts apparus début 2023 ou par dérive de la base, gonflant artificiellement l'aire au-dessus de 0,60. *Garde :* Troncature mécanique sur la date de première arête de chaque concept, pont de comptes à tolérance gelée (apport de B), et déclaration de non-estimabilité si une case regroupée reste sous l'effectif minimal.
* **Changement par rapport au tour 1 :** Maintien de ma position (a) de T3, intégrant la tolérance gelée du pont de comptes (B) et la règle de regroupement/non-estimabilité (D).

### N10 — Recommandation : Option (b) (confiance 0,55 : génération 2, avec Bailey et al. et le pilote dans les pièces)
* **Verdict :** **Tenue sous condition** (condition : recopier dans la question de génération 2 la lecture décidée par délégation — la pureté des poids dans 62 % et 54 % des tâches [RAPPORTÉ] est un plafond de la classe de moniteurs, non une preuve d'inutilité du tirage au hasard — ; et préparer dès maintenant en addendum le protocole de mesure de génération 2 : estimand stratifié par difficulté de tâche sur toutes les tâches sans filtrer les poids dégénérés, attaquant ciblant la défense composite entière, trois témoins obligatoires, et gel préalable de la classe d'attaquants, des budgets et des seuils).
* **Raison :** La question de la course 2 est au plafond de taille et le calcul décisif du pilote n'est pas lu [VÉRIFIÉ], ce qui exclut d'ouvrir l'axe en génération 1. L'extrait de Bailey et collègues (corrélation négative à 95 % entre couches visées et performance, p. 23 ; sortie incohérente à dissimilarité extrême, p. 26 [VÉRIFIÉ]) justifie de préparer la mesure composite dès maintenant pour la porte inter-générations.
* **Pire cas et garde :** *Pire cas :* La génération 2 reçoit « le tirage au hasard est inutile » comme un acquis ou évalue un moniteur sans avoir gelé la classe d'attaquants ni stratifié par difficulté (confondant refus sur tâche difficile et détection d'évasion). *Garde :* Inscription textuelle de la limite du pilote dans les pièces et obligation d'inclure les trois témoins de D (sans défense, moniteur à étiquettes permutées, filtre de difficulté seule).
* **Changement par rapport au tour 1 :** Maintien de ma position (b)/(b′) de T3, en adoptant le gel complet du protocole de mesure exigé par D avant tout verdict de génération 2.

### N11 — Recommandations conjointes de session-depot (n° 228, confiance 0,65) et conv-audit (n° 294, confiance 0,6)
* **Verdict :** **Tenue sous condition pour session-depot (n° 228) ; Renversée sur le rejet de (c) et Tenue sur le caractère descriptif de la course 2 pour conv-audit (n° 294)** (remplacement et conditions : (1) maintenir l'option (c) — ponts plantés dans la course 2 — car elle est décidée par le directeur, mais l'exécuter comme instrument descriptif à oracle mécanique exigeant l'appariement exact des **deux** identifiants parents, évalué par permutation des lots entiers, sans rouvrir le texte des proposeurs au pré-pilote où seul l'étage de sélection à ≈ 0,30 USD de lectures est éprouvé ; (2) exécuter le pilote de variance scellé de D avant de figer un nombre de mondes, et constater qu'à 8 fusions par bras la course 2 est purement descriptive — erreur type 0,21, demi-largeur 0,41 [VÉRIFIÉ] — ; (3) vérifier si la bisociation v3 étend le monde synthétique aux niches et structures du bras méta, sans quoi le synthétique ne compare que deux bras sur trois ; (4) remplacer tout test de corrélation de rangs ou d'équivalence sous-puissant par une règle ordinale exacte avec confiance intra-instrument ou un rapport descriptif côte à côte).
* **Raison :** La proposition de session-depot (rendement par dollar hors proches et surfaces, domination avec confiance, issue « non concluant, tous reconduits ») concorde avec les quatre accords larges du tour 1 [VÉRIFIÉ]. En revanche, conv-audit rejette les ponts plantés (c) au motif qu'ils rouvrent le texte du pré-pilote : or le directeur a déjà tranché « (b) et (c) » [VÉRIFIÉ], et l'on peut planter des ponts (dont la moitié à homologie de structure sans concept commun, plus les quatre familles de leurres) et tester l'étage de sélection au pré-pilote sans toucher au texte servi aux proposeurs ni au plafond de fusions. Enfin, comme B et A l'ont établi en T2/T3, le monde synthétique actuel ne porte ni les niches ni les structures du bras méta [VÉRIFIÉ] : la recommandation de conv-audit de renvoyer la règle à la bisociation v3 laisse donc le bras méta sans évaluation synthétique si le monde n'est pas étendu.
* **Pire cas et garde :** *Pire cas :* Un oracle à un seul parent donne 66,7 % de réussite au hasard ($1 - C(6,2)/C(10,2) = 30/45$ [VÉRIFIÉ]), ou un retrait de bras est prononcé sur un test de rang non jugeable ($p \ge 1/6$ par paire [VÉRIFIÉ]) ou sans que le bras méta ait pu tourner sur le monde synthétique. *Garde :* Oracle mécanique strict sur les deux identifiants parents, permutation par lots entiers, pilote de variance scellé préalable, traitement explicite du dénominateur nul (« indéfini »), et interdiction de tout retrait à 8 fusions par bras.
* **Changement par rapport au tour 1 :** J'intègre le constat de B et A sur l'absence des niches/structures dans le monde synthétique, le pilote de variance de D, et je cède à A sur la règle de transport : puisque j'ai moi-même démontré en T3 qu'un test d'équivalence à marge de 10 points exige $n > 135$ ponts par bras [VÉRIFIÉ], il est inapplicable au budget de la course ; je rallie donc le rapport descriptif côte à côte (B) doublé de la règle ordinale exacte de A lorsque les trois instruments sont suffisamment puissants.

---

## 2. Livrables du protocole (a, b, c, d) sur le lot des recommandations

### (a) Ce que la question et l'annexe supposent sans que ce soit établi
1. **Indépendance entre le choix de B en N1 et l'évaluation des trois bras en N11 :** L'annexe suppose que la règle de reconduction de N11 s'applique directement à la bisociation v3 (« la règle va aux préenregistrements de la bisociation v3 »), alors que le monde synthétique ne comporte ni les niches ni les structures que lit le bras méta — statut : **VÉRIFIÉ** (établi par B et A au tour 1 sur la pièce 3, § 6).
2. **Transposabilité de la variance de S14/S15 aux différences entre bras en N11 :** Supposer que la puissance de la bisociation sur contrastes bras/témoins vaut pour des contrastes entre trois règles de bras — statut : **HYPOTHÈSE** (variance inter-bras non mesurée).
3. **Neutralité de l'option (1) de DL-12 pour la méthode de prédiction invariante :** Le brouillon 5 recommande DL-12 (1) à 0,6 tout en notant que VS5-01 conteste son avantage ; que la méthode retrouve la cause sur monde jouet sous ce centrage — statut : **HYPOTHÈSE** (non simulé dans la pièce 15).
4. **Absence du vocabulaire du contrôle dans les 37 960 concepts de Gu et Krenn (N3) :** Statut : **HYPOTHÈSE** (marqué SUPPOSÉ par la question v12, faute d'exemplaire empreinté du graphe).
5. **Heures de calcul et calendrier du 27 novembre en N6 :** Statut : **HYPOTHÈSE** (marqué SUPPOSÉ dans la synthèse).
6. **Attribution de l'échec de N1 à la seule définition et non au code :** Statut : **OBSERVÉ-NON-AUDITÉ** (200 mondes, une graine de flux, erreurs types naïves).

### (b) Expériences décisives en duels $H_A$ contre $H_B$ (Inférence forte, Règle B4)

* **Duel E-N12 (sur N6 DL-12, pièce manquante X) :**
  * **$H_A$ :** Sous le centrage par strate (option 1 de DL-12), la méthode de prédiction invariante appliquée au monde jouet retrouve la cause plantée dans un ensemble accepté non vide à un taux supérieur ou égal à 0,70, sans inclure le jumeau sans effet à plus de 0,10.
  * **$H_B$ :** L'annulation des moyennes résiduelles par strate fait que la méthode s'abstient (ensemble vide) ou accepte tout (incluant le leurre/jumeau) dans plus de 30 % des mondes jouets.
  * **Métrique et seuil :** Taux d'inclusion exacte de la cause seule sur 200 mondes jouets ; seuil = 0,70 (et taux de fausses inclusions $\le 0,10$).
  * **Contrôle négatif :** Mondes jouets à étiquette de cause permutée entre environnements (taux d'inclusion attendu $\le \alpha = 0,05$).
  * **Falsification :** Un taux $\ge 0,70$ avec fausses inclusions $\le 0,10$ falsifie $H_B$ et valide DL-12 (1) ; l'inverse falsifie $H_A$ et impose de réviser la transformation ou de basculer la méthode en descriptif pur.

* **Duel E-N5 (sur N5, arbitrage mécanique entre (a) et (b)) :**
  * **$H_A$ :** L'implémentation journalisée de l'orchestrateur (option a) est strictement invariante à l'appartenance individuelle des témoins aux classes lorsque les comptes agrégés sont constants.
  * **$H_B$ :** Il existe un canal résiduel (ordre des appels, structure du message ou du journal) par lequel l'exécution sous (a) dépend de la permutation de la clé à comptes constants.
  * **Métrique et seuil :** Nombre de divergences d'empreintes SHA-256 du message de sortie et de la séquence ordonnée des identifiants appelés sur 1 000 permutations aléatoires de la clé maintenant les comptes agrégés constants ; seuil = 0 divergence.
  * **Contrôle négatif :** Exécution de la version antérieure non corrigée (contrôle positif de fuite : divergence garantie) et exécution sur une boîte externe ne recevant pas la clé (divergence nulle par construction).
  * **Falsification :** Zéro divergence sur 1 000 permutations falsifie $H_B$ et valide (a) ; au moins une divergence falsifie $H_A$ et impose le passage immédiat à la boîte externe (b).

* **Duel E-N11 (sur N11, pilote de variance et couverture synthétique) :**
  * **$H_A$ :** Sur les mondes de validation de la bisociation v3 (graines d'essai hors plage 500–799), l'écart type $\sigma_\Delta$ du contraste de rendement par dollar entre deux règles de bras permet de détecter un écart de 15 points avec puissance $\ge 0,80$ au budget de mondes prévu.
  * **$H_B$ :** La variance inter-bras $\sigma_\Delta^2$ sur les mêmes mondes exige un nombre de mondes supérieur au plafond budgété pour atteindre une puissance de 0,80 à 15 points d'écart.
  * **Métrique et seuil :** Puissance calculée par rééchantillonnage par blocs (mondes entiers) sur 200 mondes d'essai ; seuil de puissance = 0,80 à $\alpha = 0,05$ unilatéral.
  * **Contrôle négatif :** Comparaison de deux bras fantômes tirant au hasard avec des graines distinctes (taux de rejet attendu = $\alpha = 0,05$).
  * **Falsification :** Puissance $\ge 0,80$ falsifie $H_B$ et autorise une règle de retrait synthétique ; puissance $< 0,80$ falsifie $H_A$ et fige l'issue « non concluant, rapport descriptif ».

### (c) Mesure minimale de fonctionnement de chaque instrument nommé

1. **Nouvelle grandeur de validation et test d'invariance post hoc (N1) :** *Détection / fausses alertes :* Rejeter 100 % des fuites synthétiques injectées sur le statut d'opérateur (détection $\ge 0,95$ illustratif), taux de fausse alerte $\le 0,05$ sur mondes à lois égales. *Cas honnêtes appariés :* Mondes où la proximité conceptuelle est identique mais les fréquences de statuts sont égalisées par rééchantillonnage. *Vérification mécanique à battre :* Simple vérification que l'effectif par case statut $\times$ condition est non nul.
2. **Substitut S31 sur la moisson locale (N3) :** *Détection / fausses alertes :* Sur fenêtre temporelle postérieure disjointe, précision sur les premières apparitions d'arêtes battant la base d'au moins le gain utile gelé, taux de fausses alertes sur paires d'homonymes de physique = 0 après filtre. *Cas honnêtes appariés :* Paires de concepts de même degré et de même ancienneté non reliées à la date de coupure. *Vérification mécanique à battre :* Score produit du degré (popularité) et de l'inverse de l'âge.
3. **Compteur de profil du bras méta (N4) :** *Détection / fausses alertes :* Concordance $\ge 0,85$ (illustratif) avec un jeu de fiches de référence à niches et structures étiquetées par l'humain ; taux de fausses alertes (paires classées « dans le profil » sur la seule base d'une structure séquentielle imposée par la consigne) = 0. *Cas honnêtes appariés :* Fiches partageant la même consigne mais issues de niches distantes hors bande $[2 ; 3]$. *Vérification mécanique à battre :* Tirage uniforme de paires parmi les fiches ayant passé l'accord des lecteurs.
4. **Vérificateur d'aveugle A21 (N5) :** *Détection / fausses alertes :* Détection de 100 % des lectures hors journal et de toute dimension supplémentaire dans le schéma de sortie ; 0 fausse alerte sur l'exécution journalisée à clé permutée. *Cas honnêtes appariés :* Exécutions avec mêmes comptes agrégés de témoins mais affectations individuelles permutées. *Vérification mécanique à battre :* `diff` binaire sur les fichiers de sortie et d'appels.
5. **Déclencheur de symétrie et méthode de prédiction invariante (N6 DL-12) :** *Détection / fausses alertes :* Sur monde jouet, inclusion de la cause $\ge 0,70$ et inclusion du jumeau sans effet $\le 0,10$. *Cas honnêtes appariés :* Environnements appariés en variance annuelle (10 % et 30 % [VÉRIFIÉ]). *Vérification mécanique à battre :* Régression par effets fixes d'environnement et d'année.
6. **Garde de troncature temporelle et pont de comptes (N9) :** *Détection / fausses alertes :* Détection de 100 % des concepts dont la première arête est postérieure au 31/12/2022 ; 0 exclusion de concept actif avant la coupure. *Cas honnêtes appariés :* Paires négatives appariées exactement par case de degré des deux sommets au 31/12/2022. *Vérification mécanique à battre :* Filtre sur la seule année de publication de l'article (qui laisse passer la fuite des concepts extraits jusqu'à la coupure).
7. **Évaluateur de défense composite sous attaque adaptative (N10, pour préparation G2) :** *Détection / fausses alertes :* Taux de détection à budget d'optimisation fixé comparé à un taux de fausses alertes fixé ($\le 0,05$ illustratif) sur entrées honnêtes. *Cas honnêtes appariés :* Tâches honnêtes appariées exactement par strate de difficulté. *Vérification mécanique à battre :* Les trois témoins de D : absence de défense, moniteur à étiquettes permutées, et filtre fondé sur la seule difficulté de la tâche.
8. **Oracle de ponts plantés (N11) :** *Détection / fausses alertes :* Taux de fausses alertes sur les quatre familles de leurres (dont homologie de structure sans concept commun et parent unique tronqué) $\le \alpha$ par permutation des lots entiers. *Cas honnêtes appariés :* Lots de dix fiches avec parents plantés contre les mêmes lots sans parents plantés (le rang médian des paires non plantées ne doit pas varier — contrôle de B). *Vérification mécanique à battre :* Oracle lâche à « au moins un parent » (qui échoue avec 66,7 % de faux positifs au hasard [VÉRIFIÉ]).

### (d) Ancrage matériel
* **N1, N4, N5, N6 (monde jouet DL-12), N9 (audit de code et d'horodatages), N11 (pilote de variance synthétique) :** Exécution intégrale sur processeur local (CPU), aucun modèle ouvert ni appel payant requis ; temps de calcul de quelques secondes à quelques minutes par script ; coût = **0 USD** [VÉRIFIÉ par la synthèse].
* **N3 (essai du substitut sur la moisson locale) :** Processeur local sur la moisson déjà sur disque = **0 USD** ; en cas de maintien en pré-pilote avec trois fusions, coût rapporté par les faits = **≈ 1,88 USD** [RAPPORTÉ].
* **N6 (exécution complète du semi-réel après gel) :** Calcul processeur estimé à **118,6 heures** (fourchette 93,3 à 135,7 heures, budget de 140 à 150 heures [SUPPOSÉ]), 0 USD d'appel d'interface.
* **N9 (reproduction complète hors échantillon si machine louée) :** Location de machine ou traitement de l'instantané de 744 Go [RAPPORTÉ] (coût de location non chiffré dans la synthèse : ~10 à 30 USD illustratif selon l'instance).
* **N10 :** Lecture du verdict du pilote = **0 USD** (processeur). Pour la génération 2 seulement, évaluation sur modèles ouverts (tel celui de l'extrait de Bailey et collègues [VÉRIFIÉ]) nécessitant une carte graphique (GPU, ~20 à 50 USD illustratif).
* **N11 (volet pré-pilote des ponts plantés) :** Épreuve limitée à l'étage de sélection (lectures de niches/scores sans nouvelles fusions) = **≈ 0,30 USD** (illustratif, déjà chiffré en T1) ; si une ou deux fusions protégées sont ajoutées (option de A et B), **≈ 0,50 à 1,25 USD** (illustratif, sur la base d'environ 1,88 USD pour trois fusions [RAPPORTÉ]).

---

## 3. Positions en une ligne sur les 16 divergences non résolues

1. **N1 (lieu de l'épreuve de rareté) :** Dans l'invocation unique en variante d'évaluation secondaire post hoc (ma position avec D), car tester les contrastes des bras avant l'invocation violerait la règle d'invocation unique.
2. **N3 (lien D-j / N9) :** Logiquement indépendant comme le soutient A (le substitut n'utilise ni le modèle ni le graphe de physique des auteurs), mais utile à titre heuristique sans conditionner l'arrêt.
3. **N3 (faisabilité sur la moisson locale) :** Faisable pour une étiquette d'apparition d'arête entre concepts grâce aux dates, concepts, sujets et références présents, avec la garde de A (« non produit » si l'étiquette s'avère dégénérée).
4. **N4 (CA1-04, structures comptées) :** Exclure à la fois les jeux de données et les trois structures séquentielles imposées par la consigne (ma position avec D), l'argument d'exclusion étant identique pour les deux familles.
5. **N5 (amender A21 ou boîte externe) :** Amender A21 (option a) sous condition du test d'invariance exacte à 1 000 permutations de clé et du validateur de schéma, avec bascule immédiate en boîte externe (b) au moindre écart.
6. **N6, DL-3 (condition à effet négatif) :** Descriptive avec déclencheur d'audit conditionné à la puissance prévue (position A, C, D), pour ne pas dégrader la conjonction de recouvrement de 0,852 à 0,818 [VÉRIFIÉ].
7. **N6, DL-6 (quatrième exemplaire) :** Geler maintenant avec la marque SUPPOSÉ sur le quatrième papier (position A, C) dès lors qu'aucun chiffre de ce papier n'entre dans le code, afin de tenir l'échéance du 4 novembre.
8. **N6, DL-9 (témoin d'orientation) :** Descriptif (position A, C, D), car les deux seuils numériques sont dépourvus d'appui dans la littérature [VÉRIFIÉ].
9. **N6, DL-10 (flèche latente sous affectation biaisée) :** Option (1) sans les 30 mondes mais avec limite écrite et test unitaire algébrique instantané (position C, D), l'épreuve étant vraie par construction des effets fixes.
10. **N6, DL-12 (propension par strate) :** Exécuter le test sur monde jouet avant le gel (position A, C, D) et autoriser son issue à basculer l'option, la méthode de prédiction invariante n'ayant pas été simulée dans la pièce 15 [VÉRIFIÉ].
11. **N10 (étendue du gel préalable) :** Rallier l'exigence de D pour la génération 2 (geler classe d'attaquants, budgets, taux, plancher d'utilité, fausse alerte et unité de coût avant d'exécuter l'évaluation de G2), mais après lecture du pilote.
12. **N11 (juge de correspondance et N-058) :** Exclure tout juge de l'oracle primaire au profit de l'appariement mécanique exact des deux identifiants parents (position B, C), le juge étalonné sur leurres (A, D) restant purement secondaire.
13. **N11 (forme de la règle de transport) :** Céder à A et B : puisque j'ai montré que le test d'équivalence à marge de 10 points exige $n > 135$ ponts par bras [VÉRIFIÉ], adopter le rapport descriptif côte à côte (B) doublé de la règle ordinale exacte de A si les trois instruments sont alimentés.
14. **N11 (part minimale d'exploration) :** Une paire par sous-session (soit ~10 à 20 % illustratif) tout en maintenant au moins deux bras actifs (synthèse des seuils illustratifs de A, B, C, D).
15. **N11 (volet pré-pilote des ponts plantés) :** Éprouver la plomberie sur l'étage de sélection seul sans fusion ajoutée (≈ 0,30 USD, ma position) après rédaction d'une annexe courte (D), afin de ne pas rouvrir le plafond de fusions scellé.
16. **Ordre de traitement :** Les nœuds du chemin critique à échéance datée d'abord (gel du pré-pilote d'ici le 7 novembre et gel de N6 d'ici le 4 novembre [RAPPORTÉ/SUPPOSÉ]), N1 et le pilote de variance de N11 tournant en parallèle sur processeur.

---

## 4. Positions en une ligne sur les 7 accords trop propres

1. **N1 (option B à quatre) :** L'accord tient à la mathématique des erreurs types (0,29 à 0,60 sous l'ancienne grandeur pour un seuil de 0,5 [VÉRIFIÉ]) et non au seul cadrage : défendre le générateur seul (G3 laisse 0,33 et 0,84) ou l'abandon (alors que le code n'est pas en cause) serait réfuté par les chiffres.
2. **N4 (option (a) à quatre) :** Si l'ordre avait été inversé, (a) aurait tout de même été retenue car les autres options exigent soit un devis supplémentaire (15 fiches), soit le contournement d'une décision du directeur (bande $[2 ; 3]$), soit une dénaturation du canal faible.
3. **N9 (option (a) à quatre) :** Seule la preuve d'une contamination massive et irréparable des traits de 2022 par des données de 2023 ferait pencher pour (b), mais notre garde mécanique sur la date de première arête des concepts ferme précisément ce risque sans payer le biais de sélection post-trait de (b).
4. **N10 (option (b) à quatre) :** Au-delà du mot du directeur, l'accord repose sur deux contraintes matérielles dures : le texte de la course 2 est au plafond de taille et la règle de préenregistrement interdit d'ouvrir un axe sur un pilote non encore lu [VÉRIFIÉ].
5. **N6 (DL-4 et DL-8 à quatre) :** Pour DL-4, l'accord est analytique (ne pas donner la réponse à l'estimateur) ; pour DL-8, il ajoute la condition de geler la paramétrisation exacte de l'auxiliaire pour que le gain de puissance (0,78 contre 0,49) ne soit pas un artefact de réglage.
6. **N11 (domination avec confiance à quatre) :** Une autre forme possible serait l'allocation adaptative par échantillonnage de Thompson entre générations, mais à très faible effectif (8 fusions par bras) elle dégénère en tirage quasi uniforme et n'offre pas la garantie de contrôle d'erreur familial de la domination par intervalles.
7. **N11 (aucun retrait à 8 fusions par bras à quatre) :** L'accord est arithmétiquement invariant aux hypothèses d'effet (erreur type $\ge 0,17$ à $0,21$, demi-largeur $\approx 0,41$ [VÉRIFIÉ]) : seul un écart extrême de 0/8 contre 6/8 ($p = 0,007$) franchirait un seuil, ce qui confirme que la course 2 ne peut être que descriptive.

---

## 5. Ordre dans lequel le directeur gagne à trancher

Mon ordre du tour 1 (fondé sur les échéances datées) est **maintenu avec un ajustement majeur** issu de la découverte de B et A au tour 1 sur le lien entre N1 et N11 :

1. **Priorité 1 — Chemin critique du pré-pilote (échéance du 7 novembre [RAPPORTÉ]) :** Trancher **N5** (amendement A21 conditionné au test d'invariance à 0 USD), **N4** (option (a) + exclusion symétrique sur CA1-04), **N3** (D-j oui conditionné au test de rétrodiction à coupure temporelle à 0 USD) et le **volet pré-pilote de N11** (plomberie sur l'étage de sélection seul, sans rouvrir le texte ni le plafond de fusions). **N10** est réglé immédiatement en (b) (0 USD maintenant).
2. **Priorité 2 — Chemin critique du semi-réel N6 (échéance de gel du 4 novembre [SUPPOSÉ]) :** Exécuter le script du monde jouet de **DL-12** (quelques secondes CPU, 0 USD), puis geler les 13 décisions DL-1 à DL-13 (en renversant DL-3 et DL-9 en descriptif et en recalculant DL-5 au seuil 0,70) pour lancer les ~118,6 heures de calcul en tâche de fond.
3. **Priorité 3 — N1 et N11 conjointement (l'ajustement du tour 2) :** Contrairement à mon T1 où N1 et N11 étaient simplement mis en parallèle sur processeur, le directeur gagne à **lier formellement N1 et N11** avant de sceller la bisociation v3 : il faut d'abord décider si la bisociation v3 étend le monde synthétique aux niches et structures du bras méta ou si l'instrument synthétique de N11 ne compare que deux bras sur trois ; puis tirer les graines 500–799 de N1 et exécuter le pilote de variance scellé de N11 (0 USD, CPU).
4. **Priorité 4 — N9 :** Inspecter le code de troncature de la date de première arête des concepts et fixer la tolérance du pont de comptes (0 USD sur disque) avant de lancer l'évaluation hors échantillon sur la fenêtre 2023–2026.

FIN-DE-CELLULE