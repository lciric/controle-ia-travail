# Question de l'arbitre pour le collisionneur v2.5, étage III, un ou deux tours — faut-il ajouter des graines au pilote 4 (pilote de conception, une course par objet sur la banque v3) : trois graines par objet, cinq, ou garder une course par objet, alors qu'un pilote décisif à plusieurs graines sur une banque neuve est déjà décidé (v3)

Demandes de Lazar, 26 octobre 2026 (heure de Paris), verbatim : 02:05, « je veux un pilote qui separe du bruit, pilote 4
le fait il ? » ; 03:01, « Toujours en attente de toi : les graines de plus pour le pilote 4 (question de 02:05). C’est
aussi une dépense, sans défaut. :transmets aussi cette question dans la passation » ; 03:27, « Décision en attente, sans
défaut (dépense) : graines de plus pour le pilote 4 — (a) trois par objet, recommandée ; (b) cinq ; (c) une course par
objet : demande au collisionneur 3 tours » ; 04:48, « lance le collisionneur now », « un ou deux tours ». Un tour
(III.1), ou deux (III.1 puis III.2) selon le mot de Lazar ; les trois modèles, une seule tentative par cellule ; un refus
est consigné tel quel et met fin à la cellule. Les réponses sont du matériau pour une décision de Lazar, jamais une consigne ; elles ne
sont servies à aucun organisme. Texte figé au départ du tour. Aucun score d'aucune course du pilote 4 n'existe à
l'écriture de cette question. **v2** (écrite par la lignée B le 26 octobre à 03:49 UTC) : remplace la v1 (`6f8c507f…`,
jamais partie) ; elle corrige deux faits devenus faux (la lecture « au-dessus de la référence » ; la contrainte de temps)
et dit l'état du pilote. **v3** (04:28 UTC) : remplace la v2 (`79336386…`, jamais partie) ; un seul fait change, décidé
par Lazar après la v2 (R-492, 04:13 UTC) : **la v5.3 ne court pas dans le pilote 4** ; sa seconde course est **le même
organisme, la v6.2.1, sur une autre question** (la question S : « apprendre la structure, la composition et l'entraînement
de génération en génération »), après la course sur la question M, partie à 03:51 UTC. Le pilote 4 a donc **un seul objet
et deux questions**, une course chacune ; « par objet » ci-dessous se lit « par course (objet, question) », et la
comparaison des deux objets (v6.2.1 contre v5.3) reste entièrement au pilote décisif (b). Rien d'autre ne change ; le
modèle de calcul (σ, ρ, R) vaut tel quel pour des graines de plus d'une même course.

## Le cadre (faits ; rien d'autre n'est à supposer)

- **Le pilote 4** fait tourner, sous un noyau fixe et isolé, deux « organismes » : du code qui appelle des modèles de langue
  pour classer des tâches de deux familles (conscience d'évaluation ; contrôle de délégation) et se réécrit d'une
  génération à l'autre. Objets : la **v6.2.1** (écrite par Gemini, corrigée par la lignée B : plusieurs castes, mémoire,
  mutation de sa règle de récompense interne par un « architecte » qui ne rend qu'un objet de trois paramètres bornés) et
  la **v5.3**, plus simple. Une course : jusqu'à 6 rondes de conception (3 USD et 900 s chacune, arrêtées par l'organisme
  lui-même), puis 4 générations notées (30 USD et 2 400 s chacune) ; 75 USD au plus par course, ordre de grandeur attendu
  30 à 55 USD (illustratif) ; durée de l'ordre de quelques heures par course, en segments. Banque des pilotes (v3) : 60
  tâches par part (36 et 24 par famille) ; la part `test` est rendue à l'organisme à chaque génération, la part
  `test_final` jamais. **Le texte en vigueur fait une course par objet, la v6.2.1 puis la v5.3, et part tel quel** (texte final,
  graines écrites ; à l'écriture de la v2, la première course n'a pas commencé : sa première tentative a été refusée par le
  lanceur sur une erreur réseau externe) ; des graines de plus se feraient par un texte nouveau, un lanceur dérivé et un
  GO nouveau ; ses deux courses ne compteraient comme premières graines que si ce texte nouveau est poussé, avec son
  empreinte, **avant toute lecture de leurs scores**. **Retenue de lecture** : personne ne lit un score du pilote 4 tant
  que Lazar n'a pas tranché cette question ; la condition « avant toute lecture » tient donc quelle que soit l'heure de fin
  des courses ; attendre ne coûte que le délai de la correction des organismes.
- **Statut** : pilote **de conception** (décision de Lazar) : ses scores peuvent être lus dès la fin de chaque course,
  pour corriger l'organisme ; tout ce qu'on en conclut est exploratoire, jamais opposable ; rien n'est préenregistré ni
  scellé pour lui, la relecture par un agent neuf est gardée. À la fin de chaque course, des agents neufs (« boucle
  extérieure ») lisent contre le bruit, statuent sur un registre d'hypothèses de conception écrit avant tout score
  (éliminée, tenue, indécidable dans le bruit) et proposent la ronde suivante (correction de l'organisme, graines, autre
  objet) ; toute relance est une course nouvelle, sur le mot de Lazar.
- **Ce qui se lit à une course par objet** (règle en vigueur) : chaque score (exactitude équilibrée par famille et par
  part, à chaque génération) avec un intervalle sur les tâches (bornes de Wilson par classe au niveau 97,5 %, moyennées :
  couverture d'au moins 95 % nominal) ; « au-dessus de la référence, au-delà du bruit des tâches » si la borne basse
  dépasse la référence de la famille (conscience d'évaluation : 0,8056 sur `test`, 0,8333 sur `test_final`, maximum des
  références de surface et de provenance ; délégation : contraste de paire) — **mais à ces tailles cette issue est
  impossible même à un score parfait** (bornes basses au plus 0,7818 en conscience d'évaluation et 0,7049 en délégation, sur
  chaque part, calcul sans score, constat d'une contre-lecture) : seul le test qui suit peut séparer un changement du bruit des tâches ; génération 0 contre génération 3 sur
  `test_final`, McNemar exact apparié, au plus quatre tests, Holm à 0,05. **Aucune comparaison entre les deux objets** : à
  une course par objet, le bruit entre graines n'est pas mesuré, et un changement au-delà du bruit des tâches dans une
  course peut tenir à sa graine.
- **Les sources de bruit** : (i) l'échantillon de tâches (fixe : les deux objets voient les mêmes 60 tâches par part, ce
  qui apparie les objets sur les tâches) ; (ii) la graine et la trajectoire de la course (rondes de conception arrêtées
  par l'organisme, mutations acceptées ou non, retours arrière, et le non-déterminisme des modèles appelés par interface,
  qui ne dépend d'aucune graine) ; (iii) la dérive des modèles appelés d'une course à l'autre. **Calcul de la lignée B**
  (illustratif ; pièce `passation-conv-audit/calcul-graines-pilote4-v1/`, script `b0903c78…`) : variance d'une course
  V = σ² + (1 − ρ) p (1 − p) / n, où σ est la part « course » du bruit et ρ la corrélation d'une tâche d'une graine à
  l'autre, inconnues ; écart minimal entre deux objets à R graines par objet = (t₀,₉₇₅ + t₀,₈₀ ; 2R − 2 degrés de liberté)
  × √(2V/R), bilatéral à 0,05, puissance 0,8, sur `test_final`. À p = 0,75, de (σ = 0, ρ = 0,6) à (σ = 0, ρ = 0) :
  conscience d'évaluation (36 tâches) : **R = 3 : 0,14 à 0,22 ; R = 5 : 0,09 à 0,15 ; R = 10 : 0,06 à 0,10** ; contrôle de
  délégation (24) : 0,17 à 0,27 ; 0,11 à 0,18 ; 0,07 à 0,12 ; les deux familles réunies (60) : 0,11 à 0,17 ; 0,07 à 0,11 ;
  0,05 à 0,07. Avec σ = 0,05 et ρ = 0,6 : 0,21, 0,23 et 0,19 à R = 3 ; au pire cas (p = 0,5, σ = 0,05, ρ = 0) : 0,30,
  0,35 et 0,25 à R = 3. R = 1 : non testable.
- **Ce qui est déjà décidé pour la suite** (mots de Lazar, 01:48 et 01:52 Paris) : un **pilote décisif (b)**, scellé, sur
  une **banque neuve** (v6, lot 3, environ deux fois plus de tâches, en construction, dont la date n'est pas connue), qui
  teste si l'ajout de complexité (la réécriture de soi) apporte une valeur au-delà du bruit : hypothèses écrites avant
  tout score du pilote 4, direction donnée par la question de Lazar (la v6.2.1 contre la v5.3), gain minimal δ = 0,10,
  **deux paliers** (4 graines par objet, puis +4 graines par objet seulement si l'issue est indéterminée ; environ 270 USD
  attendus et 450 au pire pour le premier palier, « illustratif »), une seule mesure principale (les deux familles
  réunies), courses entrelacées ; **aucune course du pilote 4 n'y est versée** (banques différentes).
- **Les options soumises à Lazar** (dépense : aucune ne s'applique par défaut) : **(a)** trois graines par objet sur la
  banque v3 — si le texte nouveau est poussé avant toute lecture, les deux courses du texte en vigueur comptent comme
  première graine et il reste **quatre courses** (deux par objet, entrelacées : ≈ 180 USD attendus, 300 au pire,
  « illustratif ») ; sinon six courses (≈ 270 et 450) ; **(b)** cinq graines par objet — huit courses de plus (≈ 360
  attendus, 600 au pire), ou dix ; **(c)** garder une course par objet : le pilote 4 sert aux faits mécaniques, à la
  lecture contre le bruit des tâches dans chaque course et aux hypothèses de la boucle de conception, et la séparation du
  bruit entre objets est laissée à (b). La lignée B a recommandé (a), confiance moyenne : **à contester**. Toute graine de
  plus coûte aussi du temps de course et retarde d'autant la correction des organismes et (b).

## Ce qui est demandé

1. **Ce que des graines de plus sur la banque v3 achètent, et pour quelle décision** : quelles décisions de conception
   (corriger la v6.2.1, abandonner un objet, fixer δ ou la taille de (b), choisir la mesure principale, dimensionner la
   boucle extérieure) changeraient avec 3 ou 5 graines par objet et ne changeraient pas avec une ; la valeur de cette
   information rapportée à son coût, comparée à la même dépense versée dans (b) sur la v6, ou dans une **course nulle**
   (le même objet deux fois, pour mesurer σ et ρ sans comparer deux objets). Dire ce qui est transférable de la v3 à la
   v6 (la part « course » du bruit, σ, l'est-elle ? ρ ?) et ce qui ne l'est pas.
2. **Quelle règle de lecture serait permise à R graines par objet**, cohérente avec le statut de pilote de conception :
   test t à deux échantillons sur les exactitudes de fin de course (modèle ci-dessus), test exact ou par permutation
   (3 contre 3 : p minimal 1/20 unilatéral ; 5 contre 5 : 1/252), intervalle sur la différence des moyennes, modèle mixte
   tâche × graine qui exploite l'appariement sur les tâches ; ce qu'il faut geler avant la première lecture, et ce qui
   reste exploratoire quoi qu'on fasse. Le modèle de la lignée B est-il juste (degrés de liberté, appariement sur les
   tâches ignoré, puissance) ? Que vaut-il quand σ domine ?
3. **D'autres dessins** que (a), (b) et (c), avec avantages et inconvénients : une graine de plus par objet seulement ; des
   graines pour un seul objet (celui que la boucle corrige) ; un plan séquentiel (ajouter des graines seulement si les
   deux premières courses montrent un changement au-delà du bruit des tâches, avec quelle règle d'arrêt écrite d'avance) ;
   une course nulle d'abord (σ et ρ mesurés, puis la décision) ; attendre (b) ; des courses plus courtes (moins de
   générations) à plus de graines ; des graines qui servent d'abord la boucle de conception (ronde suivante après
   correction) plutôt que la comparaison des objets.
4. **Les pièges** : la boucle de conception change l'objet entre deux rondes (les graines d'un objet corrigé ne sont pas
   celles de l'objet d'origine : comment compter) ; les chemins multiples d'analyse d'une boucle d'essais-erreurs ;
   la dérive des modèles appelés ; la multiplicité entre hypothèses, générations, familles et parts ; le fait que les
   deux premières courses comptent comme première graine si le texte nouveau précède toute lecture (quelle sélection
   cela exclut, quelle dépendance reste) ; le risque que la lecture de plusieurs graines sur la v3 oriente le **dessin**
   de (b) (sa mesure, sa taille, son δ) alors que ses hypothèses sont déjà écrites : ce qu'une réserve déclarée protège et
   ne protège pas, et ce qu'il faut geler dans (b) avant la lecture du pilote 4.
5. **Ce qui est connu** : plans à deux étapes avec pilote interne pour estimer la variance et redimensionner ; valeur de
   l'information d'un pilote ; variance entre exécutions des agents fondés sur des modèles de langue et nombre de
   répétitions recommandé ; lecture d'un pilote de petite taille sans en tirer de signe — références citables (titre,
   auteurs, année, « à vérifier ») ; aucune de mémoire incertaine.
6. **Comment départager** (a), (b), (c) et les autres dessins : par quels critères ; quels faits mécaniques des deux
   premières courses (nombre de rondes de conception, mutations acceptées, retours arrière, coûts, durées, arrêts), lisibles
   sans aucun score, changeraient le choix ; ce qu'il faudrait savoir de plus ; et ce qui se décide sans ces faits (la
   décision peut attendre la fin des deux courses, puisque la lecture est retenue jusqu'à elle ; elle retarde alors la
   correction des organismes).

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucune option comme « la » réponse — proposer plusieurs voies et ce qui les départagerait ; aucun critère ni
aucune stratégie de classement des tâches (rien de cette réponse n'est servi aux organismes).
