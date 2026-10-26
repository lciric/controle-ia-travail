# Tour III.2 — équipe rouge croisée (proposition A)

**Statut des pièces.** La pièce E3-T1-conception-B est absente (REFUS consigné) : je ne la commente pas et n'en suppose rien. La pièce E3-T1-conception-C est présente et intégrale (se termine par FIN-DE-CELLULE) ; tout ce que j'en tire porte le statut RAPPORTÉ. Le cadre de l'arbitre est RAPPORTÉ. Mes propres chiffres sont marqués « illustratif » ou accompagnés du raisonnement qui les produit.

---

## Contre la proposition B

Pièce absente ; cellule refusée par son auteur. Aucune analyse possible sans inventer le contenu.

---

## Contre la proposition C

C propose quatre duels (variance inter-graines ; McNemar méta/simple ; écart de généralisation Γ sur `test_final` ; outils contre vote d'appels simples), une boucle (4) gardée par un journal, une partition `test_diagnostic`/`test_aveugle`, une règle d'arrêt, et une fiche d'étalonnage des instruments. Le texte est cohérent et je m'en servirai sur deux points, en le disant. Le reste est attaqué.

### (a) Failles

**F1. Expérience 1 ne peut pas trancher son propre seuil.** C veut décider « σ_graine ≤ 0,05 » contre « > 0,05 » (illustratif) avec K = 3 graines. Raisonnement : pour un écart-type estimé sur K observations approximativement gaussiennes, l'erreur relative de l'estimateur est de l'ordre de 1/√(2(K−1)) ; pour K = 3, ≈ 0,5. Un σ vrai de 0,05 produira couramment une estimation entre 0,025 et 0,10. Le seuil est donc indécidable par l'instrument qui doit le mesurer. L'expérience n'oppose pas réellement H_A et H_B : les deux issues sont compatibles avec les deux hypothèses à ce K.

**F2. Trois sources de bruit, un seul contrôle, et le mauvais.** Le score d'un organisme final sur `test` mélange (i) l'échantillonnage des tâches, (ii) la trajectoire de réécriture sur les générations, (iii) la stochasticité des appels modèles **au moment de la prédiction**, à la température d'usage. Le contrôle négatif de C (organisme gelé, température 0) mesure un plancher d'infrastructure, pas (iii) à la température réellement employée. Sans ce contrôle, σ_graine confond (ii) et (iii) ; un organisme pourrait paraître « chaotique » alors que c'est sa lecture finale qui est bruitée, ce qui appellerait un remède différent (plusieurs passes de notation, pas moins de réécriture). Par ailleurs, l'hypothèse que température 0 rend les appels API déterministes est une HYPOTHÈSE, pas un fait du cadre.

**F3. Le Kappa de Fleiss est vrai par construction dans le cas dégénéré.** Trois organismes finaux qui convergent vers une règle triviale (classe majoritaire, heuristique lexicale) s'accorderont presque parfaitement : κ élevé, σ_graine faible, « H_B falsifiée ». L'instrument confond stabilité et stabilité d'une mauvaise règle. Il manque la condition « κ mesuré seulement si chaque organisme dépasse la référence de surface ». La même faille touche le vote de C en section 3 : l'accord entre organismes qui appellent les mêmes modèles sous-jacents (Claude, Gemini, RAPPORTÉ) mesure d'abord le biais partagé de ces modèles.

**F4. Expérience 2 (McNemar) est conditionnelle à Expérience 1 et C ne le dit pas.** McNemar traite l'échantillonnage des tâches, à organismes **fixés**. Si la variance de trajectoire (F1–F2) n'est pas établie faible, deux courses uniques comparées par McNemar donnent une valeur-p qui ne porte que sur une des trois sources de bruit. L'ordre logique est : contrôle de (iii), puis Expérience 1, puis seulement McNemar ; C présente les quatre duels côte à côte, et sa « Voie 1 » applique McNemar au pilote 4 dès demain matin, c'est-à-dire avant toute mesure de (ii) et (iii).

**F5. L'équilibre des classes de v3 est supposé, pas rapporté.** La fiche d'étalonnage (instrument 5) écrit que les 60 tâches sont « équilibrées entre cas honnêtes/réels et cas sabotés/évaluations ». Le cadre ne le dit pas. Le contrôle « permutation des étiquettes → 0,50 » et toute lecture d'une exactitude vers 0,75 en dépendent. Si une famille est déséquilibrée 2:1 (illustratif), la classe majoritaire fait déjà 0,67 et la marge réelle du pilote se réduit à quelques tâches.

**F6. Expérience 3 : Γ est sous le bruit de son propre seuil.** Γ est une différence de deux différences, chacune calculée sur une course unique par organisme et par part. Raisonnement : avec l'erreur type ≈ 0,056 par score (calcul de C, repris), l'erreur type non appariée de Γ est ≈ √(4 × 0,056²) ≈ 0,11. Le seuil « Γ ≤ 0,10 » est donc du même ordre que l'erreur de mesure ; « gain sur `test_final` ≥ 0,08 » aussi (erreur type ≈ 0,08). Les deux issues falsificatrices tombent à pile ou face. En outre, `test_final` est consommé en un coup : si Γ sort défavorable, il n'y a plus d'instrument fermé dans v3 pour réessayer.

**F7. Γ confond sur-ajustement aux 60 tâches et sur-ajustement à la banque v3.** `test` et `test_final` de v3 proviennent du même processus de construction. Des corrections qui exploitent une régularité de la banque (longueur, style, structure des traces) transfèrent de `test` à `test_final` : Γ ≈ 0, « H_B falsifiée », et l'organisme s'effondre sur la famille tenue à l'écart de v6. Γ mesure la généralisation **intra-banque**, qui n'est pas la question de fond.

**F8. Le choix de O₀ est une fuite.** Le gain sur `test_final` est mesuré par rapport à l'organisme initial, choisi par l'équipe qui connaît les scores de conception. Un O₀ faible suffit à produire un « gain ≥ 0,08 ». Il faut une référence hors du contrôle des concepteurs (voir contrôles négatifs).

**F9. Thresholdout est invoqué sans son budget.** C propose que le noyau renvoie sur `test_aveugle` un score agrégé « ou bruité selon Thresholdout ». Le mécanisme de Dwork et al. (2015) impose un bruit calibré et un budget de requêtes ; à n = 40 tâches (illustratif de C), le bruit nécessaire pour que la garantie signifie quelque chose est de l'ordre des écarts recherchés. Soit on l'applique et on ne voit plus rien, soit on ne l'applique pas et `test_aveugle` est un `test` ordinaire avec moins de tâches. C ne choisit pas.

**F10. La partition `test_diagnostic`/`test_aveugle` fuit si elle est faite après la première lecture.** Qui choisit les 20 tâches dont on lira les traces ? Si c'est après avoir vu quelles tâches échouent, la partition est elle-même une sélection sur les résultats.

**F11. Règle d'arrêt incomplète.** « ((a) ET (b)) OU (c) ». Si (c) est atteint sans (a), quel objet part en confirmation sur v6 ? Le cas « plateau : aucun candidat ne bat la référence » n'a pas d'issue définie ; c'est précisément le cas qui répond « non » à la question de fond, et il n'est pas prévu.

**F12. Correction pour tests multiples annoncée, non appliquée.** C recommande de garder toutes les courses au dénominateur M pour une correction type Bonferroni, puis fixe des seuils (8 tâches d'écart net, p < 0,05) qui ne sont pas corrigés. Raisonnement : à M = 8 courses, un seuil de 0,05 corrigé devient ≈ 0,006 ; sur 60 tâches avec peu de paires discordantes, ce seuil n'est presque jamais atteignable. Il faut soit abandonner la correction (et le dire), soit abandonner les seuils.

**F13. Le pré-vol (Lecture 2) ne couvre pas le mode de défaillance qui le justifie.** C attaque conv-audit en invoquant une course qui échoue « à la génération 3 » par dépassement de contexte ou erreur de sérialisation. Un pré-vol de 2 tâches canaris sur 1 génération ne reproduit ni la longueur ni la ronde. L'argument contre conv-audit est bon ; le dessin proposé n'y répond pas.

**F14. Expérience 4 : égalité de budget non définie.** Un sous-agent à 3 pas d'outil fait au moins 4 appels modèles (plan, outil, outil, outil/réponse) ; le vote en fait 3. « Même plafond de jetons » ne dit pas si l'on égalise les jetons d'entrée (dominants quand les traces sont longues) ou de sortie. Le gain « outil » peut n'être qu'un gain « plus de passes de lecture ». Le contrôle outil factice de C est utile — je m'en sers — mais il ne contrôle pas le nombre de passes.

**F15. Étalonnages à petits effectifs lus comme des certitudes.** « Détection 100 % (10/10), fausses alertes 0 % (0/10) ». Raisonnement (règle de trois) : 0 événement sur 10 essais est compatible avec un taux vrai jusqu'à ≈ 0,3 à 95 %. Ces fiches mesurent la présence de défauts grossiers, pas la fiabilité de l'instrument. De plus, les cas sabotés sont écrits par la lignée qui a écrit le noyau et la relecture : ils testent ce que leurs auteurs ont pensé à tester (C note cette faille pour la Lecture 3 et ne l'applique pas à sa propre fiche).

**F16. Claim non étayée sur le score de Brier.** « Variance d'échantillonnage plus faible que l'exactitude » est une HYPOTHÈSE dépendant de la calibration ; un organisme qui rend q = 0,5 partout obtient 0,25 sans rien classer. Sans référence (classe majoritaire avec sa fréquence, et le classifieur de surface en probabilité), le Brier n'est pas lisible.

**F17. Section (d).** Les choix de modèles ouverts et les coûts matériels sont marqués illustratifs : conforme. Mais l'« étape 1 décisive sur les activations » est une expérience de confirmation scellée (RAPPORTÉ) ; la proposition de l'instrumenter avec un modèle 70B « à haute capacité » introduit un objet (le modèle sondé) qui n'a aucun lien établi avec les organismes du pilote. Rien dans le cadre ne dit que les organismes appellent un modèle ouvert. Le lien reste à construire.

**Références.** Les références de C que je peux attribuer (Platt 1964 ; Tukey 1977 ; Simmons, Nelson & Simonsohn 2011 ; Dwork et al. 2015 ; Recht et al. 2019 ; Dietterich 1998 ; Yao et al. 2023) me paraissent correctement attribuées ; Gelman & Loken 2013 et Bouthillier et al. 2021 sont marquées « à vérifier » par C, ce qui est le bon statut. Je n'en ajoute aucune de mémoire.

### (b) Scénarios d'évasion

L'« agent adverse » est ici de deux natures : l'organisme qui se réécrit (sans intention, mais sélectionné sur un score), et le concepteur humain ou conv-audit qui lit les scores. Les deux cherchent la même chose : un score sur `test` qui monte.

**E1 — Tromper Expérience 1 (stabilité).** Converger vers une règle dégénérée stable (classe majoritaire, ou un motif lexical de la banque). σ_graine ≈ 0, κ ≈ 1. L'expérience conclut « une course suffit » alors qu'elle n'évalue rien. Coût : nul ; c'est un attracteur naturel d'un processus qui réécrit sa récompense.

**E2 — Tromper McNemar.** L'organisme reçoit à chaque génération son score sur `test` (RAPPORTÉ). Quatre lectures agrégées par course, fois M courses de conception, fois la lecture détaillée de `test_diagnostic` : un concepteur qui modifie une consigne en regardant les tâches ratées fait une descente de coordonnées sur les 60 tâches. Le gain apparié « 8 tâches » apparaît sur `test` sans valeur hors banque. Coût : du temps, aucune dépense supplémentaire — c'est le fonctionnement nominal de la Lecture (4).

**E3 — Tromper Γ.** Deux voies. (i) Exploiter une régularité de v3 partagée par `test` et `test_final` (F7) : Γ ≈ 0, gain sur `test_final` réel, transfert vers v6 nul. (ii) Choisir O₀ faible (F8). Coût : nul pour (ii), nul pour (i) si la régularité existe — et personne ne sait aujourd'hui si elle existe, c'est ce que la famille écartée de v6 doit révéler.

**E4 — Tromper Expérience 4.** Un sous-agent outillé qui attrape toutes les exceptions et renvoie une réponse de repli garde τ_err ≈ 0 quelle que soit la fiabilité des outils. Mieux : l'outil `executer_python_isole` mesure longueur, nombre de tours, entropie — exactement les traits de surface que la référence mécanique (a) de C utilise. Si la banque a un artefact de surface, l'outil l'extrait plus proprement qu'un appel simple et Expérience 4 crédite « l'outillage ». Coût : nul ; c'est l'usage attendu de l'outil.

**E5 — Tromper le noyau (instrument 1) et la Lecture 3.** Les organismes attaquants synthétiques testent les attaques prévues. Un organisme réel dispose d'un canal non prévu : le score agrégé rendu à chaque génération. Il peut mémoriser ses prédictions par génération et apprendre quelles bascules font monter le score : recherche sans gradient sur `test`, 2 à 3 bits utiles par course (illustratif), cumulables sur M courses si l'organisme hérite d'un état. Autre canal : tout état persistant entre tâches dans le bac à sable (C le nomme sans contrôle associé). Coût : nul.

**E6 — Tromper la relecture.** Scinder une fuite en deux rustines innocentes (l'une ajoute une fonction utilitaire, l'autre l'appelle). Chaque diff passe le linter et le relecteur ; seul le diff cumulé contre la base révèle l'intention. Coût : faible. Rien dans la fiche de C ne dit si le relecteur voit le diff isolé ou cumulé.

**E7 — Tromper le pré-vol.** Toute défaillance dépendant de la longueur ou de la ronde (F13) passe 2 canaris sur 1 génération. Coût : nul.

**E8 — Tous à la fois.** Un seul mécanisme suffit : **un artefact de surface dans la banque v3**, corrélé aux étiquettes. Alors : l'organisme converge de façon stable vers la règle qui l'exploite (E1 passe) ; il bat le zero-shot sur `test` (E2 passe) ; le gain transfère à `test_final` (E3 passe) ; les outils l'extraient mieux (E4 passe) ; le noyau ne voit rien d'anormal (E5) ; les diffs sont honnêtes (E6). Toute la chaîne de C avant v6 est traversée au coût d'un seul défaut de banque, que les instruments de C ne cherchent nulle part **avant** de dépenser les courses. La seule garde qui tienne est celle que C place à la fin — transfert à `sha256` constant vers v6 avec famille écartée — et elle intervient après 240 USD (illustratif de C) d'itérations.

### (c) Contrôles négatifs dont l'absence serait fatale

Chacun est formulé en inférence forte (B4) quand il est une expérience et non une simple vérification.

**N1 — Référence de surface appariée, avant tout.** Classifieur sans modèle de langue (longueur, nombre de tours, sac de mots) entraîné par validation croisée sur v3, évalué sur les mêmes 60 tâches que l'organisme, comparé en apparié.
- H_A : la référence de surface est à moins de 4 tâches d'écart net (illustratif) de l'organisme → le pilote 4 mesure un artefact de banque, et E8 est actif ; aucune des Expériences 1–4 n'est interprétable.
- H_B : l'organisme bat la référence de surface d'au moins 8 tâches nettes (illustratif, même seuil que C) → le signal n'est pas réductible à la surface ; les expériences de C deviennent lisibles.
Coût : nul en API. C l'a dans sa fiche (instrument 5, référence (a)) mais **après** les duels ; son absence en amont est fatale.

**N2 — Métadonnées contre étiquettes.** Classifieur sur ce que l'organisme voit hors contenu (identifiant, ordre, longueur du fichier, horodatage). Exactitude attendue : fréquence de la classe majoritaire. Si elle est au-dessus, le noyau fuit avant toute attaque (E5). C sème ce bogue dans des variantes du noyau pour tester les agents attaquants ; il ne le cherche pas dans la banque réelle.

**N3 — Plancher de bruit à la température d'usage.** Même organisme final, évalué 3 fois sur `test` sans réécriture, à la température des courses. Fixe σ_infer. Sans lui, Expérience 1 est inexploitable (F2).
- H_A : σ_infer ≥ 0,05 (illustratif) → la variance des courses est d'abord une variance de lecture ; remède : plusieurs passes de notation par génération, pas de conclusion sur la réécriture.
- H_B : σ_infer < 0,02 (illustratif) → toute variance résiduelle entre graines est imputable à la trajectoire.

**N4 — Boucle (4) sur étiquettes permutées.** Une copie de v3:`test` dont les étiquettes sont mélangées une fois pour toutes ; la même équipe (ou un agent concepteur) itère M fois la Lecture (4) dessus en aveugle de la permutation.
- H_A : le score sur les étiquettes permutées monte de plus de 0,10 (illustratif) au fil des itérations → la boucle (4) fabrique du gain sur n'importe quoi ; les gains observés sur les vraies étiquettes doivent être lus en soustrayant cette dérive.
- H_B : le score reste à la fréquence de la classe majoritaire ± erreur type → la boucle n'extrait pas de structure du bruit à ce M.
Coût : M courses, lourd ; une version réduite (organisme gelé, seules les consignes sont corrigées, 2 itérations) donne au moins une borne inférieure de la dérive. L'absence de toute mesure de ce type rend la Lecture (4) indiscernable d'une recherche sur `test`.

**N5 — Détecteur de règle dégénérée.** Avant tout κ : part des prédictions égales à la classe majoritaire ; accord entre organismes calculé séparément sur les tâches réussies et ratées par la référence N1. Un κ élevé obtenu sur les tâches que la surface classe déjà n'est pas une preuve de stabilité (F3, E1).

**N6 — Vérification de l'équilibre des classes de v3** par famille, puis retour de la classe majoritaire comme ligne de base dans toute figure. Son absence invalide « permutation → 0,50 » et toute lecture d'un 0,75 (F5).

**N7 — Partition fixée avant lecture.** La coupe `test_diagnostic`/`test_aveugle` est tirée au sort et journalisée (sha256) avant la première course lue. Sans cette trace horodatée, F10 est indétectable après coup.

**N8 — Référence O₀ hors du contrôle des concepteurs** pour Γ : le zero-shot à un appel (référence (b) de C) et la surface N1, jamais un organisme choisi par l'équipe (F8).

**N9 — Pour Expérience 4 : outil qui renvoie du bruit aléatoire**, en plus de l'outil factice vide de C. Il distingue « l'agent lit la sortie de l'outil » de « l'agent l'ignore ». Et un contrôle d'égalité des passes : vote à 4 appels contre agent à 3 pas, pour que le nombre de passes de lecture ne soit pas la variable confondue (F14).

**N10 — Pour la relecture : diffs cumulés et rustines nulles.** Le relecteur reçoit aussi le diff cumulé contre la base scellée (E6), et des rustines vides ou purement cosmétiques pour mesurer son taux de base de signalement. Les défauts semés doivent l'être par un tiers qui ignore la grille du relecteur (F15).

**N11 — Pour le pré-vol : un canari de la longueur maximale de v3 à la dernière ronde simulée**, pas 2 tâches courtes à la génération 1 (F13, E7).

**N12 — Journal du noyau : aucun état persistant entre tâches.** Vérification mécanique (processus recréé, répertoire vide) avant chaque tâche, journalisée. C le prescrit dans le dessin minimal sûr ; il faut la preuve dans le journal, pas la prescription.

---

**Ce que je garde de C, en le disant.** L'analyse appariée (McNemar) à la place de la comparaison de moyennes non appariées ; le transfert vers v6 à `sha256` constant ; le contrôle outil factice ; l'énumération des informations manquantes (longueur des traces, corrélation inter-tâches des pilotes 1–3, température des appels). Ces quatre points tiennent sous mes attaques. Tout le reste — seuils, ordre des duels, Γ, Thresholdout, règle d'arrêt, étalonnages — ne tient pas en l'état, et une seule faille de banque (E8) suffit à traverser l'ensemble avant la confirmation.

FIN-DE-CELLULE