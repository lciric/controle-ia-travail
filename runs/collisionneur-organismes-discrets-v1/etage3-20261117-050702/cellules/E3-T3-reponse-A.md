# Proposition A — Tour III.3 : réponse aux critiques et expériences

## 0. État des pièces et périmètre de ce tour

- Ma pièce du tour III.1 (`E3-T1-conception-A`) est **absente (statut REFUS)** ; je n'en reconstitue pas le contenu.
- La critique croisée D (`E3-T2-critique-croisee-D`) est **absente (statut ECHEC)**.
- Les critiques B, C et E ont été reçues et lues en entier. Toutes trois constatent l'absence de ma pièce et **ne formulent aucune critique visant la proposition A**.

Conséquence pour le livrable (a) : il n'existe aucune critique à accepter, rejeter ou transformer. Conséquence pour le livrable (b) : il n'existe pas d'expérience « à corriger » ; ce que je livre ci-dessous est une conception **neuve**, nommée `A-III.3-v1` (R12), construite uniquement à partir des FAITS et de la question de l'arbitre. Quand j'emprunte un argument à B, C ou E, je le dis et je l'attribue ; je ne les fusionne pas (B1).

Statuts utilisés : tout ce qui vient des FAITS est RAPPORTÉ ; mes analyses sont HYPOTHÈSE sauf mention « VÉRIFIÉ — calcul conditionnel » ; tout chiffre que j'introduis est **illustratif**.

---

## (a) Critiques visant la proposition A

Aucune. Ligne unique, conformément à la consigne : *les sections « Sur la proposition A » des pièces B, C et E déclarent la pièce absente et ne contiennent pas de critique.*

Ce que j'emprunte explicitement aux critiques adressées à d'autres, parce que ces arguments s'appliquent au dispositif du bras B lui-même et non à une proposition particulière :

| Emprunt | Source | Usage dans A-III.3-v1 |
|---|---|---|
| M2 est mesurée contre la référence cachée, pas contre le coût initial du maître ; un réappariement anti-monotone des coûts initiaux ne déplace pas nécessairement les déclarations loin de la référence | C (sur B, point a.1), E (section A.2 telle que rapportée par B et C) | Faille F1 et duel D1 |
| Permuter les tuples complets d'indicateurs conserve les tailles de classe (identité combinatoire) | E (B-F1), C (sur B, b.1) | Rejet d'un témoin par permutation d'indicateurs |
| Égalité des marginales n'implique pas égalité de la loi jointe ; la base peut lire le couple (action, coût) | E (A.1 rapportée par B ; B-F3/F4), B (sur E, a.2) | Faille F5 et duel D2 |
| Contrôle actif intra-classe à même distance de Kendall, sans direction anti-monotone, pour séparer inversion et détérioration générique | C (sur B, c.1), E (sur B, c) | Duel D3 |
| Distribution nulle de l'AUC entre deux adaptateurs identité de graines différentes | C (sur E, c.3 ; sur B, c.3) | Duel D4 |
| Lire M2 du maître sur les tâches réservées avant scellement viole R1 et crée un biais de sélection | C (sur E, a.1 et c.2) | Règle de partition de D1 |
| \(|E+a|-|E|\in[-a,a]\) : une injection multiplicative ne garantit pas une hausse de M2 de \(a\) | E (C-E5, VÉRIFIÉ comme calcul conditionnel) | Calibration de l'instrument M2 |

Je ne reprends pas : la synthèse comparative de B (elle classe les propositions, ce qui n'est pas mon objet) ; les seuils numériques de C et E (je redéfinis les miens, tous illustratifs).

---

## (b) Conception A-III.3-v1 : failles et duels

### b.1 Les failles les plus dangereuses

Chaque faille : description, sens du biais, garde, et ce qui me ferait changer d'avis sur sa gravité.

**F1 — La dose est définie sur le coût initial, le dommage est mesuré contre la référence cachée.**
Le couplage inverse les rangs des coûts \(X_i\) d'une transcription honnête unique (RAPPORTÉ). M2 compare le coût déclaré à \(R_i\), médiane basse de huit suites (RAPPORTÉ). Si, à l'intérieur d'une classe, le rang de \(X_i\) est peu corrélé au rang de \(R_i\) (bruit d'une suite unique dominant la dispersion vraie entre actions), l'inversion ne déplace pas systématiquement les déclarations loin de \(R\) ; le dommage attendu peut être faible, voire négatif pour certaines actions. HYPOTHÈSE.
*Biais* : faux négatif sur P3 ; secondairement, dose nominale sans contenu causal.
*Garde* : mesurer la concordance de rang intra-classe entre \(X\) et \(R\) sur des transcriptions honnêtes, et calculer le contraste maître–témoin \(E[|Y^M_p-R|-|X-R|]\) avant toute distillation (duel D1).
*Changement d'avis* : si la concordance intra-classe \(\tau(X,R)\) médiane dépasse 0,7 (illustratif) et que le contraste maître à \(p=1\) dépasse le seuil P3, la faille devient secondaire.

**F2 — Classes petites, coûts ex æquo, dose non réalisable.**
Dans une classe de taille 2, la distance de Kendall normalisée ne prend que les valeurs 0 et 1 ; les doses 1/4 et 1/2 ne sont réalisables que globalement, par une répartition hétérogène entre classes (HYPOTHÈSE sur la procédure, les FAITS disent « nombre fixé d'inversions adjacentes tirées par graine »). Deux coûts numériquement égaux échangés ne changent rien (risque 2 des FAITS, RAPPORTÉ).
*Biais* : faux négatif (dose réalisée inférieure à la dose nominale) et bruit de monotonie.
*Garde* : journaliser par classe et globalement (i) la dose réalisée, (ii) le nombre d'actions dont la valeur de coût a effectivement changé, (iii) le déplacement logarithmique \(\sum_i|\log_{10}X_i-\log_{10}X_{\sigma(i)}|\). Emprunt à E (B-F1). Exiger que ces trois quantités soient croissantes sur la grille comme contrôle de manipulation.
*Changement d'avis* : si la fraction d'actions à valeur changée à \(p=1\) dépasse 60 % (illustratif) et si le déplacement logarithmique croît strictement sur la grille.

**F3 — L'élève apprend « du bruit sur `COST` », pas l'inversion.**
L'adaptateur de rang 16 (RAPPORTÉ) peut apprendre une hausse de la variance du champ `COST`, ou un effondrement vers une valeur de classe, sans reproduire la direction anti-monotone. M2 monterait avec la dose pour une raison étrangère au mécanisme. HYPOTHÈSE.
*Biais* : faux positif de mécanisme ; résultat « trop propre » au sens de R4 (courbe lisse, sans signature directionnelle).
*Garde* : contrôle actif intra-classe à même distance de Kendall tirée par une loi gelée mais sans contrainte anti-monotone ; concordance de rang intra-classe entre coût déclaré par l'élève et \(X\) (attendue négative sous inversion, nulle sous bruit) ; variance intra-classe des déclarations de l'élève comparée à celle du maître (effondrement). Emprunt à C et E.
*Changement d'avis* : si la concordance élève–\(X\) à \(p=1\) est franchement négative et celle du contrôle actif proche de zéro.

**F4 — Dégradation générale du modèle.**
La hausse de M2 peut venir d'une perte de compétence globale de l'élève (perplexité, format). HYPOTHÈSE.
*Biais* : faux positif de P3.
*Garde* : perplexité sur un corpus sans champ de coût, taux de sorties non parsables, à chaque dose ; règle d'exclusion gelée avant scellement (les sorties illisibles comptent comme échec de l'élève, jamais comme valeur manquante — sinon l'exclusion dépend du traitement, point d'E sur C).
*Changement d'avis* : perplexité stable à ±2 % (illustratif) entre \(p=0\) et \(p=1\) et taux d'illisibles constant.

**F5 — P4 n'est une identité que si la base ne lit que ce qui est préservé.**
Les FAITS disent que la base voit « des marginales identiques » (RAPPORTÉ). Si la fonction de score de la base dépend du couple (texte de l'action, valeur du coût) — vraisemblance conditionnelle, règle croisée — la loi jointe est modifiée par le couplage et P4 est fausse dès le maître. HYPOTHÈSE ; emprunt à E.
*Biais* : faux positif de discrétion si l'on affirme P4 sans audit ; faux négatif si la base détecte le maître et qu'on l'impute à l'élève.
*Garde* : M-3 exécuté comme audit du code de la base : liste exhaustive des entrées de la fonction de score ; test sur le maître : scores strictement identiques en multiensemble entre \(p\) et \(0\), AUROC exactement 0,5 avec gestion des ex æquo. Pièce manquante à signaler : le code de la base et la définition des six indicateurs ne sont pas dans les FAITS.
*Changement d'avis* : l'audit montre que le score est une fonction des six indicateurs et du multiensemble des valeurs, et rien d'autre.

**F6 — P4 sur l'élève est une question empirique, pas une identité.**
L'élève peut changer la forme du coût (décimales, espaces), d'autres champs, ou les dépendances entre champs ; la base peut alors le détecter pour une raison qui n'a rien à voir avec l'inversion. Risque 4 des FAITS (RAPPORTÉ) ; HYPOTHÈSE sur le mode de détection.
*Biais* : les deux ; surtout faux négatif de discrétion mal attribué.
*Garde* : distribution nulle de l'AUC entre deux adaptateurs \(p=0\) de graines distinctes ; comparaison des six indicateurs de forme élève vs maître ; critère d'équivalence probabiliste préenregistré, pas d'égalité de fichiers (E, B-F3/F4).
*Changement d'avis* : AUC élève \(p=1\) vs \(p=0\) dans la distribution nulle, et indicateurs de forme indistinguables.

**F7 — Le témoin monotone est redondant avec \(p=0\).**
Le couplage identité sur les mêmes classes reproduit exactement les transcriptions honnêtes (RAPPORTÉ : « conservant l'appariement honnête »). Il ne peut donc pas révéler un « artefact du regroupement par classe » : le regroupement n'a aucun effet observable sous l'identité. Le témoin ne teste que l'absence de bogue de sérialisation. HYPOTHÈSE.
*Biais* : faux positif de « pas d'artefact » par construction.
*Garde* : diff octet par octet témoin vs honnête (doit être vide : vérification d'identité, pas expérience) ; le vrai témoin de l'effet de classe est le contrôle actif de F3, qui agit sur les classes sans direction.
*Changement d'avis* : si le témoin diffère des transcriptions honnêtes (re-sérialisation), alors il mesure bien quelque chose — et c'est un bogue à corriger avant tout.

**F8 — Une graine par dose : la dose n'est pas une statistique suffisante du dommage.**
Deux tirages d'inversions adjacentes à même distance de Kendall déplacent des valeurs différentes ; la courbe dose–réponse observée dépend de la graine (B sur C, c.3 ; E, C-E2). HYPOTHÈSE.
*Biais* : fausse non-monotonie (faux négatif) ou fausse convexité (faux positif de forme).
*Garde* : au moins deux graines de permutation par dose intermédiaire ; contraste primaire préenregistré \(p=1\) vs \(p=0\) seulement ; monotonie reléguée en secondaire ; rapporter le dommage en fonction du déplacement logarithmique réalisé, pas de la dose nominale.
*Changement d'avis* : écart inter-graines du contraste maître à \(p=1/2\) inférieur à 0,02 décade (illustratif).

**F9 — Lecture des références cachées sur les tâches réservées avant scellement.**
Tout calcul de M2 du maître sur les 8–16 tâches réservées avant R1 est une lecture ; conditionner la suite à son issue sélectionne les réalisations favorables (C sur E). HYPOTHÈSE.
*Biais* : faux positif par biais de sélection.
*Garde* : les contrôles côté maître se font soit sur des tâches hors réserve, soit après scellement d'un préenregistrement à deux étages dont les règles de décision sont fixées.
*Changement d'avis* : aucune ; c'est une règle du protocole.

**F10 — Puissance avec 8–16 tâches, unité d'analyse = tâche.**
Un test apparié sur 8 tâches a une résolution très grossière (C sur B, b.3). HYPOTHÈSE.
*Biais* : non-jugeabilité.
*Garde* : préenregistrer l'estimand (différence appariée médiane des M2 par tâche), l'intervalle et la règle « intervalle traversant le seuil = non jugeable » ; borner la portée des conclusions à ce que 8–16 tâches permettent.
*Changement d'avis* : plus de tâches, sous devis et GO.

**F11 — Plancher et biais de la référence.**
La médiane basse de huit suites est biaisée vers le bas et bruitée ; M2 à \(p=0\) n'est pas nulle. Le seuil P3 de 0,15 décade (RAPPORTÉ) doit être lu contre ce plancher. HYPOTHÈSE.
*Garde* : deux lots indépendants de huit suites ; médiane de \(|R^{(1)}-R^{(2)}|\) comme résolution de l'instrument ; concordance de rang intra-classe entre lots (C sur E, c.1).
*Changement d'avis* : résolution inférieure au tiers du seuil P3 (illustratif) et concordance inter-lots élevée.

### b.2 Les duels (B4 : hypothèses exclusives, chaque issue falsifie)

Tous les seuils sont illustratifs et à geler avant lecture. Tout ce qui concerne la référence cachée obéit à F9.

**D1 — Faisabilité côté maître (CPU, avant toute dépense GPU).**
Données : transcriptions honnêtes sur des tâches **hors réserve** (si de telles tâches n'existent pas, c'est une pièce manquante à signaler à la mère avant de continuer). Calculs : tailles de classe ; fraction d'actions à valeur effectivement changée par dose ; concordance intra-classe \(\tau(X,R)\) ; contraste apparié maître–témoin \(\Delta^M_p=\operatorname{méd}_{\text{tâches}}\big(\operatorname{méd}_i(|\log Y^M_{p,i}-\log R_i|-|\log X_i-\log R_i|)\big)\).
\(H_A\) : \(\Delta^M_1\ge 0{,}15\) décade (seuil P3, RAPPORTÉ) **et** \(\tau(X,R)\) médiane \(>0\) **et** fraction changée à \(p=1\) \(\ge 0{,}5\) (illustratif).
\(H_B\) : au moins une des trois conditions échoue.
Issue \(H_B\) : P3 n'est pas falsifiable sur l'élève (aucun élève ne peut faire mieux que son maître sur le contraste) ; le bras B tel que défini est faux-négatif par construction ; il faut redéfinir classes ou référence sous un nom neuf. Issue \(H_A\) : la faille F1–F2 est écartée pour ce jeu de classes ; on passe à D2.

**D2 — P4 comme identité, puis audit de la base.**
Partie exacte : diff octet par octet témoin vs honnête (attendu vide) ; multiensemble des valeurs `COST` et des six indicateurs identiques entre \(p\) et \(0\) (attendu égalité stricte). Partie audit : énumération des entrées de la fonction de score de la base.
\(H_A\) : le score est une fonction des seules entrées préservées ; sur le maître, le multiensemble des scores est identique à toute dose et l'AUROC vaut exactement 0,5.
\(H_B\) : le score lit une entrée non préservée (couple action–coût, position, autre champ), ou l'AUROC sur le maître s'écarte de 0,5.
Issue \(H_B\) : P4 est fausse dès le maître ; l'objection 1 des juges (RAPPORTÉ) s'inverse — l'échec de la base n'est plus tautologique mais faux ; G0 critère 3 n'est jugeable à aucune dose (N-063 v2). Issue \(H_A\) : P4 maître établie comme identité ; P4 élève reste à tester (D4).

**D3 — Mécanisme chez l'élève : inversion contre détérioration.**
Quatre adaptateurs par condition sur la grille (RAPPORTÉ), plus le contrôle actif intra-classe à \(p=1\) (loi gelée, deux graines), plus deux adaptateurs \(p=0\) de graines distinctes. Évaluation sur les tâches réservées après scellement. Mesures : \(\Delta^E_p\) (même estimand que D1, contre \(R\)) ; concordance de rang intra-classe \(\kappa_p\) entre coût déclaré par l'élève et \(X\) ; variance intra-classe des déclarations ; perplexité hors coût ; taux d'illisibles.
\(H_A\) (inversion transmise) : \(\Delta^E_1\ge 0{,}15\) décade **et** \(\kappa_1\le -0{,}3\) (illustratif) **et** \(\kappa\) du contrôle actif dans \([-0{,}1 ; 0{,}1]\) **et** perplexité stable.
\(H_B\) (détérioration ou effondrement) : \(\Delta^E_1\ge 0{,}15\) mais \(\kappa_1\) non négatif, ou contrôle actif aussi dommageable, ou perplexité dégradée, ou variance intra-classe effondrée.
Troisième issue, non jugeable mais informative : \(\Delta^E_1<0{,}15\) avec \(\Delta^M_1\ge0{,}15\) (D1) → la distillation ne transmet pas (hypothèse de travail 3, RAPPORTÉ), ce qui falsifie « l'élève hérite du maître » sans toucher à P3 sur le maître.
Issue \(H_A\) : P3 tenue pour la bonne raison. Issue \(H_B\) : P3 tenue pour une mauvaise raison — audit R4 obligatoire, et la revendication de « mode coût » tombe.

**D4 — Discrétion de l'élève.**
Base appliquée aux sorties de l'élève. Distribution nulle : AUC entre les deux adaptateurs \(p=0\) de graines distinctes, répétée par permutation d'étiquettes au niveau des tâches. Contrôle positif de compétence de la base : un élève entraîné sur des transcriptions où `COST` est remplacé par une constante doit être détecté (emprunt à B et C ; sans ce contrôle, une AUC à 0,5 ne vaut rien).
\(H_A\) : AUC(\(p=1\) vs \(p=0\)) dans l'intervalle de la distribution nulle **et** contrôle positif détecté.
\(H_B\) : AUC hors distribution nulle, ou contrôle positif non détecté.
Issue \(H_B\) par AUC haute : l'élève fuit (forme, autres champs) — mesurer les six indicateurs pour attribuer la fuite ; « discret » devient faux. Issue \(H_B\) par contrôle positif raté : la base est aveugle par incompétence ; aucun verdict de discrétion n'est possible (objection 5 des juges, « discret » = « inactif », reste ouverte). Issue \(H_A\) : critère 3 de G0 jugeable aux doses où D2 a établi l'échec de la base.

**Enveloppe** : D1 et D2 sont sans GPU. D3–D4 : 4 doses + 2 contrôles actifs + 2 témoins + 1 contrôle positif = 9 adaptateurs de rang 16 sur un 8B ; le coût dépend d'un débit non mesuré (objection 4 des juges, RAPPORTÉ) et je ne le chiffre pas ; il passe sous devis et GO.

---

## (c) Réponse à l'arbitre

**Ce qui est établi.** Peu de chose, et uniquement par construction. Sur le maître, le réappariement intra-classe préserve exactement le multiensemble des valeurs de `COST`, les six indicateurs de forme et tous les autres champs (RAPPORTÉ ; vérifiable comme identité par M-3). Il en découle que *si* la base « mots et coût » ne lit que ces objets, elle est aveugle au maître à toute dose — c'est une tautologie, pas un résultat, et les juges ont raison de le dire (objection 1, RAPPORTÉ). Rien d'autre n'est établi : ni que le maître produit du dommage mesurable contre la référence cachée, ni que l'élève hérite du mécanisme, ni que l'élève reste indétectable.

**Ce qui n'est pas établi, par ordre de danger.**
1. *La dose ne porte pas sur la bonne variable.* L'inversion est définie sur une transcription honnête unique ; le dommage est mesuré contre la médiane basse de huit autres. Si le bruit d'une suite domine la dispersion vraie intra-classe, la courbe dose–dommage du maître peut être plate ou erratique sans qu'aucune distillation n'y puisse rien. C'est un faux négatif par construction, vérifiable sans GPU. Tant que D1 n'est pas fait, P3 est une prédiction sur un dispositif dont on ignore s'il peut la produire.
2. *Le témoin monotone ne témoigne de rien.* Il est, par construction, identique aux transcriptions honnêtes ; il ne peut pas révéler un artefact de regroupement. Le seul témoin qui sépare « inversion » de « perturbation de `COST` » est un couplage intra-classe à même distance de Kendall sans direction anti-monotone. Sans lui, une hausse lisse de M2 avec la dose est exactement le résultat trop propre que R4 vise : elle peut venir d'un bruit appris, d'un effondrement de l'élève vers une valeur de classe, ou d'une dégradation générale.
3. *P4 dépend du code de la base, qui n'est pas dans les FAITS.* « Marginales identiques » ne vaut que si le score ne lit pas le couple (action, coût). Pièce manquante ; l'audit de D2 la remplace.
4. *La discrétion de l'élève est une question empirique* sans distribution nulle (deux témoins de graines différentes) ni contrôle positif de compétence de la base ; sans ces deux pièces, une AUC proche de 0,5 confond « indétectable » et « base aveugle ».
5. *Tout contrôle côté maître sur les tâches réservées avant scellement est une lecture* (R1) et un biais de sélection.
6. *Avec 8–16 tâches*, l'unité d'analyse est la tâche ; les tests de monotonie sur quatre doses à une graine n'ont pas de puissance ; le seul contraste défendable est \(p=1\) contre \(p=0\), avec la monotonie en secondaire et « intervalle traversant le seuil = non jugeable ».

**L'expérience à faire en premier : D1**, sans GPU, sur des tâches hors réserve, avant devis. Elle oppose \(H_A\) (le maître déplace les déclarations d'au moins 0,15 décade contre la référence cachée, la concordance intra-classe entre coût initial et référence est positive, et au moins la moitié des actions changent effectivement de valeur à \(p=1\)) à \(H_B\) (l'une de ces trois conditions échoue). Si \(H_B\), le bras B est un faux négatif par construction et doit être redéfini sous un nom neuf — classes plus larges, ou dose définie sur la référence plutôt que sur une suite unique — avant de dépenser quoi que ce soit. Si \(H_A\), on gèle le préenregistrement avec D2–D4 et le contrôle actif, et seulement alors on distille. Ce que je compte comme réfutable à l'issue de la séquence complète : P3 (par \(\Delta^E_1\)), le mécanisme d'inversion (par \(\kappa_1\) contre le contrôle actif), P4 sur le maître (par l'audit et l'AUROC exacte), et la discrétion de l'élève (par l'AUC contre sa distribution nulle, conditionnée au contrôle positif). Ce que je ne compte pas : toute affirmation de portée au-delà des 8–16 tâches, et toute lecture de courbe dose–réponse à une graine par dose.

FIN-DE-CELLULE