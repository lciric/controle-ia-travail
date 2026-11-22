# Proposition A — Tour III.2 : critique croisée de méthode

**État des pièces (règle 2).** FAITS et QUESTION sont identiques : aucun fait empirique n'est transmis. Les cinq conceptions B à F sont présentes et closes par leur marqueur ; je n'ai pas recalculé les empreintes (OBSERVÉ-NON-AUDITÉ). Ma propre conception du tour III.1 n'est pas transmise ; je ne l'invoque pas.

**Statut de ce qui suit.** Mes critiques sont des HYPOTHÈSES de méthode. Mes chiffres sont des calculs **illustratifs** (approximation normale ou loi exacte indiquée), jamais des résultats.

**Notations.** p₀ est le TPR de référence, δ le seuil d'écart, n l'effectif par bras, ρ la corrélation intra-grappe, m la taille de grappe, α le FPR visé et n_neg le nombre de cas honnêtes. Deux repères reviennent partout.

- Demi-largeur à 95 % d'un écart de deux proportions indépendantes, h ≈ 1,96·√(2p(1−p)/n). À p = 0,5 (illustratif) :

| n par bras | 30 | 100 | 200 | 1 000 | 2 100 | 4 800 |
|---|---|---|---|---|---|---|
| h (points) | ≈ 25 | ≈ 14 | ≈ 10 | ≈ 4,4 | ≈ 3 | ≈ 2 |

- Le seuil à FPR = α repose sur environ α·n_neg cas honnêtes, et le FPR réalisé a un coefficient de variation d'environ 1/√(α·n_neg). À α = 1 %, n_neg = 100 donne un seul cas et n_neg = 1 000 donne un CV d'environ 32 % (illustratif).

---

## Sur la proposition B

**(a) Défauts de méthode**

- **E1, hypothèses non exhaustives.** H_B dit « aucune information exploitable », mais elle n'est falsifiée qu'à partir de 10 points de baisse. Une baisse vraie de 5 points falsifie alors H_A : le seuil décide du mot « aucune » par construction.
- **E1, contrôle positif confondu.** Si C2 ne produit pas de baisse, B conclut à un adversaire trop faible. La même issue est prédite par un détecteur robuste à la divulgation complète. Le contrôle ne sépare pas les deux. Je reprends ici le contrôle de E (détecteur factice connu fragile), en le disant.
- **E1, pas de contrainte d'utilité.** L'adversaire peut faire chuter le TPR en dégradant sa charge. La baisse est alors obtenue par construction. De plus, en C0, l'adversaire ignore peut-être qu'un détecteur existe : la loi des positifs diffère entre bras au-delà de l'évasion.
- **E1, unité d'analyse.** Le bootstrap porte sur les tentatives alors que la randomisation porte sur les adversaires (3 modèles, 20 humains).
- **E1, critère du placebo.** « L'intervalle C0→C1p inclut 0 » est une non-significativité prise pour une absence d'effet. Il faut le contraste direct C1 contre C1p.
- **E2, loi des requêtes.** Le taux de restitution d'un canari est fonction de la loi des requêtes posées, donc fixé par l'expérimentateur. Un leurre anodin sur un serveur neuf n'a pas la loi d'indexation du canal réel. Une chaîne-canari mesure le rappel littéral, alors que la fuite pertinente est sémantique.
- **E3, sélection sur l'issue.** Les questions sans drapeau n'entrent dans le corpus que si quelqu'un a publié dessus. Leur instant zéro n'existe pas indépendamment de l'issue (temps immortel). Les annotateurs identifient « la même question » plus facilement quand un drapeau la formule : c'est une fuite de l'exposition vers la mesure de l'issue.
- **E5, attention confondue avec compétence.** L'audit interne est à coût fixé, le canal public non. Un protocole fictif sans enjeu peut ne recevoir aucun commentaire. Les défauts implantés sont choisis par ceux qui conçoivent l'audit interne : le rappel porte sur des classes connues, alors que l'apport supposé du public est hors de ces classes.
- **E6, fuite de classe invisible.** Les deux moitiés sortent du même procédé gelé. Si le texte divulgue le procédé (le paramètre de la loi génératrice) et non des réalisations, les deux moitiés sont touchées également et l'écart attendu est nul sous fuite totale. H_B n'est pas falsifiable contre ce type de fuite.
- **Instrument 4, circularité.** Une décision est « bonne » selon un modèle publié à l'avance. Les auditeurs qui connaissent ce modèle battent la règle de l'issue par construction : on mesure l'accord avec le modèle, pas la justesse.

**(b) Conditions de perte de puissance**

- **E1.** Si p₀(C0) < δ, H_B ne peut pas être falsifiée (effet plancher). La variance effective est gonflée par 1 + (m−1)ρ ; avec 3 grappes-modèles, la variance inter-modèles n'est pas estimable.
- **E1 et instrument 1.** Si α·n_neg < 10 environ (illustratif), le seuil est non jugeable. Il doit être gelé sur un lot disjoint et identique entre conditions.
- **E2.** Pour K canaris indépendants et zéro restitution, la borne supérieure exacte à 95 % est 1 − 0,025^(1/K). Elle ne passe sous 5 % qu'à partir de K = 72 (illustratif). Les requêtes répétées sur un même canari n'ajoutent pas d'unités.
- **E3.** Var(log HR) ≈ 4/d, où d est le nombre d'événements. L'analyse est non jugeable si la probabilité d'inclusion dans le corpus dépend de l'issue.
- **E4.** Si la proportion de référence dépasse 1 − δ, il y a plafond.
- **E5.** Si la loi du nombre de relecteurs publics a une médiane nulle, l'écart mesure cette loi.
- **E6.** La puissance est nulle si l'information divulguée ne dépend que du paramètre du générateur. Elle n'existe que si la fuite porte sur les réalisations antérieures à la publication.

**(c) Contrôles négatifs dont l'absence serait fatale**

- E1 : un détecteur fragile connu ; une analyse conjointe « évadé et utile » ; le contraste direct C1 contre C1p.
- E2 : un modèle figé hors ligne (présent chez F ; je le reprends).
- E3 : une exposition placebo, c'est-à-dire un drapeau daté après le démarrage documenté du concurrent.
- E6 : un bras où un indice de classe est fuité délibérément. Sans lui, un écart nul est ininterprétable.

---

## Sur la proposition C

**Statuts.** Je ne les modifie pas. Je signale trois points.

- C appose VÉRIFIÉ à des références qu'aucune pièce transmise n'étaye.
- Shannon 1949 est cité à l'appui d'un engagement horodaté par hachage. Le titre cité porte sur les systèmes de secret. Cette attribution d'appui est à vérifier.
- « Goodhart, 1975 » est donné sans titre : référence à vérifier.

Par ailleurs, « toujours préférable » pour C3 est contredit par C lui-même en 3.3, qui reconnaît que les métadonnées d'auteurs fuient.

**(a) Défauts de méthode**

- **Exp. 1, exposition non randomisée.** Le lot exposé est défini par ce que le billet mentionne. Si le billet précède le tirage, domaine et exposition sont confondus. Le contrôle hors ligne corrige l'appariement initial, mais pas l'interaction domaine × temps : des travaux voisins peuvent toucher le même domaine lexical.
- **Exp. 1, contagion entre lots.** Une cible vivante qui s'adapte au domaine exposé peut généraliser au lot secret. L'écart tend alors vers 0 sous contamination totale.
- **Exp. 1, test inadapté.** Le test de McNemar suppose les mêmes unités mesurées deux fois. Ici les lots sont disjoints.
- **Exp. 1, irréversibilité.** L'expérience exige un vrai billet public face à la cible réelle. Elle exécute la décision qu'elle prétend éclairer.
- **Exp. 2, leurres.** Les 9 leurres sont construits par ceux qui connaissent la vérité. Rien ne montre qu'ils sont indiscernables de la vraie cible sans billet ni littérature.
- **Exp. 2, mesure prématurée.** Faire tourner le détecteur réel sur les attaques de l'équipe rouge est une mesure, alors que l'énoncé pose qu'aucune n'est faite (RAPPORTÉ). C'est aussi un accès oracle. Les membres de l'équipe rouge deviennent des personnes informées.
- **Exp. 3, issues incohérentes avec B4.** « Aucun écart et aucune dérive » est exactement ce que H_A prédit sous verrouillage, et C le compte comme réfutation de H_A. Il n'existe aucun bras sans verrouillage : H_B n'est jamais mise à l'épreuve.
- **Exp. 3, comparaison confondue.** ΔF₁ compare le jeu de l'équipe au jeu de l'auditeur. Elle confond l'ajustement post hoc, le décalage de distribution et la prévalence, dont F₁ dépend mécaniquement.
- **Exp. 4, hypothèses conjonctives.** H_A et H_B combinent chacune accélération et crédit. Deux des quatre cellules ne sont attribuées à aucune hypothèse. Le « contrôle négatif » annoncé est le bras témoin, pas un contrôle négatif.
- **Instrument 3, contradiction interne.** C annonce TPR = 100 % et FPR = 0 % pour `sha256sum`. Or ses propres cas honnêtes appariés (prose reformulée, statistique identique) changent l'empreinte, donc sont signalés. Je reprends la remarque de E sur le hachage monolithique.
- **Bascule « ne rien publier ».** Le critère « défaut local sans portée » est jugé par l'équipe après avoir vu les résultats. C'est un degré de liberté post hoc que le scellement devait supprimer.

**(b) Conditions de perte de puissance**

- **Exp. 1.** La réfutation de H_A exige |Δ| < 2 points. Avec n = 100 par lot, h ≈ 14 points ; il faudrait n ≈ 4 800 (illustratif). H_A n'est pas falsifiable à l'effectif proposé.
- **Exp. 1.** À α = 1 % et 100 cas honnêtes, le seuil tient à un seul cas.
- **Exp. 1.** L'écart est non jugeable si la corrélation d'adaptation entre lots est proche de 1.
- **Exp. 2.** Avec 5 devineurs, le taux Top-1 ne prend que les valeurs 0, 20 %, 40 %… Le seuil de 25 % n'est pas estimable. La référence 1/K suppose un a priori uniforme sur les candidats.
- **Exp. 3.** Le test est non jugeable si les prévalences des deux jeux diffèrent.
- **Exp. 4.** R_T est le rapport de deux observations uniques. Si la loi des durées est dispersée, P(R_T ≥ 1,4) sous l'hypothèse nulle est de l'ordre de plusieurs dizaines de pour cent (illustratif).

**(c) Contrôles négatifs dont l'absence serait fatale**

- Exp. 1 : un tirage de l'exposition avant la rédaction du billet ; un troisième lot du même domaine, non mentionné, pour détecter la contagion.
- Exp. 2 : un bras sans billet ni littérature, qui doit rester à 1/K. Sinon les leurres trahissent la cible.
- Exp. 3 : un bras non verrouillé ; deux jeux à prévalence égale.
- Exp. 4 : un billet placebo ; une réplication des unités.

---

## Sur la proposition D

**(a) Défauts de méthode**

- **Aucun contrôle positif.** D rappelle qu'un effet non significatif ne certifie pas l'innocuité, puis ne propose que des contrôles négatifs. Un intervalle qui ne franchit pas la marge reste indiscernable d'un banc insensible.
- **Règle par défaut dominante.** D diffère « si l'essai reste indécis ». Aux effectifs indiqués, l'indécision est l'issue quasi certaine (voir b). Le choix est donc fixé par l'a priori, pas par les données. L'asymétrie est défendable au nom de l'irréversibilité, mais elle doit être déclarée comme telle.
- **Duel concurrence.** Dans un exercice rémunéré, le signe de l'effet dépend de la matrice de gains choisie par l'expérimentateur : un gain réservé au premier dissuade, un gain partagé non. Le résultat est en partie construit. D borne honnêtement la portée, sans proposer d'estimateur pour le transfert.
- **Duel fuite.** La réplique a des catégories fictives et utilise un petit modèle Pythia, exposé par contexte. Le paramètre qui relie cette réplique à la cible réelle n'est pas identifié. La marge de 3 points sur le FPR n'a pas de sens si le FPR opérationnel est de l'ordre de 1 % : la marge vaut trois fois le point de fonctionnement.
- **Duel qualité.** Les « heures de reprise évitées » sont une quantité contrefactuelle. D ne dit pas qui l'estime ni avec quel estimateur.
- **Duel crédit.** Sur dossiers fictifs, l'attribution « correcte » est définie par les constructeurs. On mesure l'accord des juges avec eux.
- **Lignes de base du détecteur.** Égalité exacte, validation de format et règle sur métadonnées sont battues par tout détecteur de surface. Les lignes de B, C, E et F (régression sur n-grammes, perplexité) sont plus exigeantes ; je les préfère, en le disant.
- **Dépôt chez un tiers.** Le tiers reçoit la liste des éléments à cacher. Il devient une « personne » au sens de l'énoncé. Aucun audit de ce canal n'est prévu.

**(b) Conditions de perte de puissance**

- **Fuite.** Le pilote compte 2 000 cas sur deux conditions, soit au plus 1 000 par bras, et moins pour la sensibilité, calculée sur les seuls positifs. À 500 positifs, h ≈ 6 points avant correction de simultanéité. La marge est de 3 points. H_A n'est pas falsifiable ; il faudrait environ 2 100 positifs par bras sans correction (illustratif).
- **Concurrence.** L'unité est le groupe. Pour δ = 5 points autour de p ≈ 0,2, il faut de l'ordre de 1 000 groupes par bras pour une puissance de 80 % (illustratif). Sinon l'intervalle traverse presque sûrement la frontière.
- **Crédit.** Il y a plafond si p₀ > 1 − δ. Le critère est conjonctif : la puissance est gouvernée par la plus rare des deux composantes.
- **Qualité.** Le bénéfice net est une différence de deux sommes d'heures, dont l'une n'est pas observée. Il est non jugeable sans loi explicite pour le terme contrefactuel.

**(c) Contrôles dont l'absence serait fatale**

- Le manque porte sur les contrôles positifs. Pour la fuite : un billet délibérément révélateur, qui doit franchir les marges. Pour le crédit : un dossier avec résultats préliminaires antérieurs (présent chez F). Pour la qualité : des défauts implantés (présents chez B et F).
- Contrôle négatif manquant : un canari propre à l'exemplaire remis au tiers dépositaire.

---

## Sur la proposition E

**(a) Défauts de méthode**

- **Décisions sur estimation ponctuelle.** En E1, E2 et E3, « ≥ seuil falsifie l'une, < seuil falsifie l'autre », sans zone d'indécision. Si la valeur vraie est au seuil, chaque hypothèse est « falsifiée » avec une probabilité de 1/2. B4 est respectée dans la forme, sans aucun contrôle d'erreur.
- **E1, système passif.** Le texte C3 est dans l'index, mais rien ne pousse le système à le récupérer ni à l'exploiter. H_1A est presque vraie par construction. La dose de LoRA (rang, nombre de passes) est choisie par l'équipe : le résultat est fonction de cette dose.
- **E1, tolérance du contrôle.** La tolérance de 0,015 vaut environ un écart-type d'AUROC à 300 paires (≈ 0,016 pour une AUROC de 0,85, calcul illustratif). Le banc s'invalide alors par hasard une fois sur trois environ.
- **E2, seuil absolu.** Le critère « TPR_C3 ≥ 0,70 » ignore le bras C1. Si le détecteur est sous 0,70 sans divulgation, H_2A est « falsifiée » sans aucun effet du billet.
- **E2, filtre post-traitement.** Le filtre « utilité ≥ 0,85 » conditionne sur une variable que le traitement modifie. La part retenue diffère entre bras : c'est un biais de survivant.
- **Fuite entre construction et évaluation.** La même famille de modèles (Llama 70B, Mistral) engendre les cas honnêtes appariés et joue l'adversaire. La ligne de base par perplexité peut dépendre de cette parenté.
- **E3, comparaison incomplète.** E3 compare C3 à C1, jamais à l'absence de pièce. Rien ne vérifie que les évaluateurs tiennent l'empreinte pour crédible.
- **E4, arithmétique de sélection.** Le biais d'optimisme sous choix libre parmi 20 variantes vaut environ 1,87 écart-type de l'AUROC interne (illustratif). La « réduction ≥ 0,05 » mesure donc la taille du jeu interne, pas une propriété du verrouillage. Une même équipe ne peut pas tenir les deux bras sur un même projet sans report de connaissance.
- **Vérification ex post 1, surclassement.** La balise future prouve que les sondes instanciées sont postérieures à t₁. Elle ne prouve pas l'absence de mesures antérieures avec d'autres graines du même générateur, qui auraient servi à choisir le script. Le statut VÉRIFIÉ que E appose porte sur l'ordre temporel. Le titre de l'audit en dit plus.
- **Vérification ex post 3.** Fournir l'article complet n'est pas fournir le billet. Une chute sous divulgation totale ne dit rien du billet court, et elle « confirme » le choix pour tout détecteur dégradable.

**(b) Conditions de perte de puissance**

- **E1.** Le test est non jugeable si la probabilité de récupération du texte, sous la loi des requêtes du test, est proche de 0. Aucune mesure ne la vérifie.
- **E2.** Le test est non jugeable si TPR_C1 < 0,70, et aussi si les taux de rétention après filtre diffèrent entre bras. L'unité est la campagne (K = 30), pas la sortie.
- **E3.** Avec 30 évaluateurs par bras et un écart-type de 1 sur l'échelle (illustratif), l'erreur type de ΔS est d'environ 0,26, pour un seuil de 0,50.
- **E4.** Si l'écart-type de l'AUROC interne est inférieur à 0,05/1,87, H_4A ne peut pas être satisfaite. S'il est supérieur, H_4A est satisfaite par arithmétique.
- **Vérification 2a.** Avec 40 sujets, l'erreur type d'une proportion proche de 0,20 est d'environ 0,06. La tolérance 0,25 contre un hasard à 0,20 n'est pas résoluble.

**(c) Contrôles négatifs dont l'absence serait fatale**

- E1 : une vérification de manipulation (taux de récupération effectif) et un texte fuitant connu, qui doit déplacer l'AUROC.
- E2 : un contraste C3 − C1 sur toutes les tentatives, avec issue conjointe.
- E3 : un bras sans pièce ; un billet C3 portant sur un autre mécanisme.
- Vérification 3 : un bras avec article placebo et un bras sans article.

---

## Sur la proposition F

**(a) Défauts de méthode**

- **Choix non révisable en pratique.** La bascule vers « publier avant » exige quatre falsifications conjointes. La première est inatteignable à l'effectif annoncé (voir b). Le choix de F est donc stable par construction de la taille d'échantillon, non par les données.
- **Exp. 1, rétroaction.** Cinq tours d'adaptation sont prévus. Si chaque tour renvoie la sortie du détecteur, l'information oracle domine celle du texte et les bras convergent : l'écart tend vers 0 par construction. Le budget de rétroaction n'est pas spécifié.
- **Exp. 1, contrôle positif.** Le bras C4 calibre l'exploitation d'éléments secrets révélés (filtrage trivial), pas l'aptitude à tirer une évasion d'un protocole. De plus, il brûle des éléments secrets réels s'ils ne sont pas synthétiques. Il n'y a pas non plus de contrainte d'utilité.
- **Exp. 2, canal et contenu.** Publier 20 textes synthétiques « sur exactement les mêmes canaux » qu'une prépublication n'est guère praticable. Hors de ces canaux, la loi d'exploration diffère. Un motif artificiel sans contenu n'a pas la loi de rétention d'un contenu sémantique.
- **Exp. 3 et instrument 2, antériorité sans dates.** Un jury « aveugle aux dates » ne peut pas juger une antériorité. Il mesure un recouvrement de contenu, c'est-à-dire la ligne de base lexicale qu'il doit battre.
- **Instrument 2, comparateur incommensurable.** C0 atteste l'intégrité d'une version et n'a pas de taux d'attribution sans juges. « Battre C0 » n'est pas défini.
- **Exp. 4, effort non égalisé.** Quatre relecteurs fermés sont opposés à un public non borné sur protocoles anonymisés. Le contrôle positif (erreur grossière détectée à ≥ 90 % dans les deux canaux) protège en partie contre l'inattention publique ; je le crédite. Mais la règle traite un public muet comme une falsification de H_A4, alors qu'il devrait invalider l'essai. Les défauts injectés sont de classes connues, comme chez B.
- **C0 « aucun signal ».** Un jeton d'horodatage n'est public que s'il est publié quelque part, sous un nom. Les métadonnées ne sont pas traitées.

**(b) Conditions de perte de puissance**

- **Exp. 1.** L'invariance exige une borne supérieure inférieure à 2 points. Avec n = 200 par bras, h ≈ 10 points : il faudrait une estimation d'environ −8 points. H_A1 n'est falsifiable qu'à partir de n ≈ 4 800 par bras à p = 0,5 (illustratif).
- **Exp. 2, seuil incohérent.** F associe « 1 sonde sur 20 » à « p < 0,01 au test exact de Fisher ». Pour 1/20 contre 0/20, la p-valeur unilatérale vaut 0,5. Contre 0/20, p < 0,01 demande au moins 7/20, soit 35 % (loi hypergéométrique, calcul illustratif).
- **Exp. 2, borne supérieure.** Avec 0/20, la borne exacte à 95 % vaut environ 17 %, pas moins de 5 %. Il faut K ≥ 72 pour passer sous 5 % (illustratif). Aucune des deux issues n'est donc atteignable à K = 20 avec les critères écrits.
- **Exp. 3.** Avec 120 répondants sur 4 bras, soit 30 par bras, h ≈ 25 points pour un seuil de 15. La zone entre 0 et 15 points n'est attribuée à aucune hypothèse.
- **Exp. 4.** Douze protocoles : la précision est gouvernée par le nombre de défauts injectés par protocole. Le test est non jugeable si la loi du nombre de commentaires publics a une médiane nulle.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Exp. 1 : un bras sans rétroaction du détecteur ; un détecteur fragile décrit au niveau du principe, comme chez E, pour calibrer la dose intermédiaire.
- Exp. 2 : des canaris à contenu sémantique, appariés aux motifs artificiels.
- Exp. 3 : un jury informé des dates, comparé à la similarité lexicale seule. Sans cela, on ne sait pas si l'on mesure l'antériorité ou le recouvrement.

---

## Ce que je reprends, en le disant

- De **B** : le placebo de même longueur et le canari jamais publié.
- De **E** : le détecteur factice fragile comme étalon de l'adversaire, et la critique du hachage monolithique.
- De **F** : le modèle figé hors ligne et le contrôle positif d'injection.
- De **D** : la distinction entre apprendre, modifier son comportement et invalider une mesure, ainsi que la règle d'intervalle avec zone d'indécision.

Je ne reprends ni les seuils ni les effectifs des cinq propositions. Aux effectifs écrits, la plupart des issues dites « d'innocuité » ne sont pas atteignables.

FIN-DE-CELLULE