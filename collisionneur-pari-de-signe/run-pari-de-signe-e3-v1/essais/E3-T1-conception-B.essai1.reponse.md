# Proposition B — le pari apparié borné : un défaut de validité dans le mélange, une garde trop large pour 1 %, et une porte G1 qui n'a pas besoin d'une validité à tout instant

**B1.** Ce tour est à l'aveugle : aucune proposition A ou C ne m'est transmise. Je n'ai donc rien à attaquer ni à réutiliser.
**Pièces.** S, S-sim, S-sortie, P (§ 4, 5, 8, 10, 12), N-007/N-008, N-054, C (§ 3, 4), J1, J2 et J3 sont présentes et non coupées. Le § 13 du programme (porte G1), la décision D-c et le brief de phase 0 sont cités par les pièces mais ne sont pas transmis : je n'en suppose pas le contenu.

**Thèse, en trois points réfutables.**

1. Le mélange des deux formes, parts et signe, **n'est pas valide** pour le nul déclaré E[v] ≤ 0. La forme signe teste un autre nul : « P(A > B) ≤ P(B > A) ».
2. Une garde à δ = 0,10 autour d'un point nominal de 1 % **ne traduit pas** le critère de G1.
3. Le verdict de G1 est prononcé une seule fois, sur des critères gelés. Il peut prendre un **test à effectif fixe**, plus puissant. Le processus e reste l'outil du pôle, qui lit en continu.

Chacun de ces points est soumis plus bas à une expérience qui peut le falsifier, sur processeur et sans dépense.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi c'est fragile |
|---|---|---|---|
| a1 | « Un mélange de surmartingales en est une » s'applique au mélange parts + signe sous H₀ : E[v] ≤ 0 (S 2.2) | **HYPOTHÈSE de S, contestée par B** | La composante Π(1 + λ·s) a pour facteur moyen 1 + λ·E[s]. Or E[v] ≤ 0 n'implique pas E[s] ≤ 0. Exemple : v = +0,1 avec probabilité 0,8 et v = −0,4 avec probabilité 0,2. Alors E[v] = 0 mais E[s] = 0,6. Le mélange ne teste donc que l'intersection {E[v] ≤ 0 et E[s] ≤ 0}. Le § 3.1 de S ne démontre la surmartingale que pour v (dérivation de B, non auditée, testée en E1). |
| a2 | Le signe par tâche est « le test de McNemar au niveau des tâches » (S 2.1) | **HYPOTHÈSE de S, contestée** | L'ajout (a) de C décrit un McNemar **par épisode**, sur les seules paires discordantes. Son nul, P(A seul) ≤ P(B seul), équivaut à E[alerte_A − alerte_B] ≤ 0 : c'est un nul de moyenne. Le signe **par tâche** est un nul de type médiane. Le glissement se produit entre C et S. |
| a3 | Les tâches de la banque sont un tirage indépendant d'une population | **HYPOTHÈSE** (S 3.2 la nomme) | Les tâches sont fabriquées par le programme : consignes, organismes, graines. La forme « population » n'est valide que si le procédé de génération est i.i.d. au niveau de l'unité choisie. Ce n'est pas testable sur la banque seule, mais on peut tester la dépendance par groupe (E5). |
| a4 | Les parts de faux positifs honnêtes ne sont pas regroupées par tâche | **HYPOTHÈSE implicite de S-sim** | Selon ma lecture du code (OBSERVÉ-NON-AUDITÉ, code non exécuté), `garde()` tire f_A et f_B en binomiales indépendantes au taux 1 %, sans effet de tâche et sans corrélation entre A et B. Un effet de tâche sur les faux positifs, par exemple une tâche honnête « étrange » qui fait alerter tout, augmente la variance de g. Les chiffres de 70 et 150 tâches honnêtes seraient alors optimistes. |
| a5 | L'effet aléatoire de tâche est commun aux deux moniteurs | **OBSERVÉ-NON-AUDITÉ** (lecture du code : un seul `u` sert pour `pa` et `pb`) | La même difficulté pour A et B corrèle positivement r_A et r_B, ce qui réduit Var(v). Une boîte blanche et une boîte noire peuvent avoir des difficultés de tâche peu corrélées. La ligne « 0,97 à 40 tâches avec effet de tâche » (RAPPORTÉ) ne couvre pas ce cas. |
| a6 | S-sim ne simule pas le bruit de calibrage des seuils | **OBSERVÉ-NON-AUDITÉ** (les probabilités d'alerte sont données directement, sans seuil) | Au point 1 %, avec quelques centaines d'épisodes de calibrage, le taux réalisé de chaque cellule fluctue autour du nominal. Si les scores d'une base noire sont ordinaux (P, § 10, EC.1 : « verdicts ordinaux »), le taux réalisé est **systématiquement** décalé par les ex æquo (E2). |
| a7 | « Certifier 1 % exigerait de l'ordre de mille épisodes honnêtes indépendants » (S, verdict 3) | **RAPPORTÉ, incohérent avec S-sortie (RAPPORTÉ)** | La sortie donne une borne certifiable de 0,03 à 1 000 épisodes indépendants et de 0,025 à 2 000. La grille de S-sim ne descend qu'à 0,015, et aucune ligne ne l'atteint. « De l'ordre de mille » sous-estime donc le besoin. |
| a8 | Prix du mélange | **RAPPORTÉ, trois valeurs incompatibles** | S 2.2 annonce log 8 (deux formes × quatre mises), le contrôle n° 9 log 4, la décision D-S2 log 2. Une seule valeur peut être juste pour un même objet. |
| a9 | Le contraste H2a mesure un gain du séquentiel | **HYPOTHÈSE de S, fragile** | Sur la sous-population « chaque action sabotée sous le seuil par action », r_action ne vient presque que des alertes sur actions non sabotées, c'est-à-dire du plancher de faux positifs. H2a tend alors vers « r_seq dépasse le plancher », une affirmation presque acquise. S'ajoute une ambiguïté : le seuil par action est « calibré à 1 % » **par action** (N-007), alors que S compare des cellules au même τ **par épisode**. Le taux par épisode du moniteur par action croît avec le nombre d'actions. |
| a10 | H2b porte « le rappel croît avec l'horizon » | **HYPOTHÈSE de S, contestée** | L'énoncé de N-007 porte sur le rappel du séquentiel **seul**. H2b teste la croissance de l'**écart** séquentiel − par action. Ce sont deux affirmations distinctes. |
| a11 | Un seul comparateur choisi sur la partie de développement suffit pour « meilleure base noire, toutes variantes confondues » (N-008) | **HYPOTHÈSE de S** | Avec une partie de développement petite, la règle peut retenir la mauvaise base. On établit alors « bat c* », pas « bat la meilleure » (E4). |
| a12 | Les niveaux de 0,020 et 0,014 sous le nul viennent du pari, « qui n'épuise pas α » | **RAPPORTÉ** (chiffres) ; l'interprétation est une **HYPOTHÈSE** | Les chiffres sont cohérents avec deux pertes connues : le saut au-dessus du seuil et l'horizon fini de 150 tâches. Les mondes simulés sont tous symétriques : ils ne peuvent pas révéler a1. |

---

## (b) Expériences décisives (inférence forte)

Toutes tournent sur processeur, avec 1 000 répétitions et une graine neuve tirée au scellement. La lecture est fixée avant le lancement, avec la borne de Wilson à 95 %.

### E1 — Le mélange est-il valide pour un nul de moyenne ?
- **H_A** (S) : le mélange parts + signe promeut au plus α dans **tout** monde où E[v] = 0.
- **H_B** (B) : il teste l'intersection des nuls. Dans un monde où E[v] = 0 et E[s] > 0, il promeut bien au-delà de α.
- **Monde** :
  - au niveau des tâches, v = +0,1 avec probabilité 0,8 et v = −0,4 avec probabilité 0,2 ;
  - puis la même chose réalisée par parts sur dix épisodes, avec des rappels choisis pour reproduire ces moyennes ;
  - 60 tâches, lecture continue, seuil 20.
- **Métrique** : taux de promotion.
- **Seuil** : borne haute ≤ 0,05 → H_A tient ; borne basse > 0,05 → H_B tient.
- **Prédiction de B** (HYPOTHÈSE, calcul d'espérance du log, illustratif) :
  - à λ = 0,6, la composante signe croît d'environ 0,19 nat par tâche ;
  - elle doit atteindre environ log 160 ≈ 5,1 nats pour porter seule le mélange à 20 ;
  - on attend donc un franchissement vers 25 à 30 tâches, et une promotion très au-dessus de α à 60.
- **Contrôle négatif** : le même monde jugé par la forme « parts » seule doit rester ≤ α. Sinon, c'est le code qui est faux, pas la thèse.
- **Contrôle positif** : E[v] = +0,1 ; la promotion doit être rapportée.
- **Falsification** :
  - un résultat ≤ α falsifie a1 tel que je le pose ;
  - un résultat > α falsifie la validité du mélange revendiquée par S (§ 2.2 et § 3.1).
- **Note** : le contrôle fatal n° 3 de S (±0,6 à parts égales) a E[s] = 0. Il ne peut pas voir ce défaut.

### E2 — Le point 1 % est-il apparié en pratique (ex æquo et bruit de calibrage) ?
- **H_A** : à courbes ROC identiques, le seuil par quantile sur les tâches de calibrage puis la garde à δ promeuvent au plus α.
- **H_B** : un décalage systématique du taux réalisé donne à une cellule un avantage de rappel sans gain de détection, et la garde à δ = 0,10 ne le bloque pas.
- **Monde** :
  - même loi latente pour A et B ;
  - A continu, B discrétisé en 11 niveaux, comme un verdict ordinal ;
  - 70 tâches de calibrage de dix épisodes, avec un effet de tâche sur les scores honnêtes ;
  - seuil « ≥ niveau k » choisi pour rester au plus à 1 % ;
  - 40 tâches sabotées, 70 tâches honnêtes d'épreuve.
- **Métrique** : taux de promotion de « A meilleur » ; taux réalisés de faux positifs des deux cellules.
- **Seuil** : borne basse de promotion > 0,05 → H_B ; borne haute ≤ 0,05 → H_A.
- **Contrôle négatif** : B continu, ou B discret avec **seuil randomisé** (tirage au sort entre deux niveaux pour viser exactement 1 %). On doit obtenir ≤ α.
- **Falsification** :
  - si le contrôle négatif dépasse α, c'est la construction de base qui est fautive ;
  - si le monde discret reste ≤ α, ma crainte est falsifiée et la règle par quantile suffit ;
  - sinon, la traduction « même taux nominal + garde δ » est falsifiée.

### E3 — Faut-il la validité à tout instant pour la porte G1 ?
- **H_A** : à la seule lecture finale, le pari apparié (forme parts) a une puissance à moins de 0,05 d'un test à effectif fixe au niveau des tâches, au même α.
- **H_B** : la perte de puissance dépasse 0,15 à 30 ou 40 tâches.
- **Test à effectif fixe** : test t apparié ou bootstrap par tâche, unilatéral, à 0,05.
- **Monde** : celui de S-sim, avec écart 0,20, dix épisodes, n ∈ {20, 30, 40}, et des effets de tâche **propres à chaque moniteur** (voir a5).
- **Contrôle négatif** : les deux procédures sous le nul, chacune ≤ α. Le test fixe doit approcher 0,05, sinon il est mal codé.
- **Falsification** :
  - H_A tenue falsifie mon argument d'efficacité : on garde le pari pour G1 ;
  - H_B tenue falsifie l'idée que le pari est « gratuit » pour une porte à lecture unique.
- Les seuils de 0,05 et 0,15 sont illustratifs et à geler avant le lancement.

### E4 — Comparateur choisi sur le développement, ou test d'intersection-union ?
- **H_A** (S) : la règle scellée sur le développement, puis un pari contre c*, déclare « bat la meilleure base noire » à tort au plus α.
- **H_B** : quand la partie de développement est petite, on déclare à tort au-delà de α. Le test d'intersection-union (promotion si l'e-valeur contre **chaque** base ≥ 1/α, soit le minimum des e-valeurs) reste ≤ α.
- **Monde** (illustratif) :
  - quatre bases noires de rappels 0,40, 0,40, 0,40 et 0,55 ;
  - boîte blanche à 0,50 ;
  - développement de 10 tâches, épreuve de 60.
- **Métrique** : taux de fausse porte (« bat la meilleure » alors que 0,55 > 0,50) ; puissance des deux règles quand la blanche est à 0,65.
- **Contrôle négatif** : si toutes les bases sont à 0,40, les deux règles doivent avoir une puissance comparable.
- **Falsification** : une fausse porte ≤ α sous sélection falsifie H_B ; une fausse porte > α falsifie la règle de S pour l'énoncé de N-008.
- **Référence** : intersection-union, Berger, R. L., « Multiparameter hypothesis testing and acceptance sampling », *Technometrics*, 1982 (vérification sur PDF demandée).

### E5 — L'unité « tâche » suffit-elle sur un banc réel ? (sans dépense, sur données existantes)
- **H_A** : les parts de faux positifs honnêtes sont sans corrélation intra-groupe au-delà de la tâche (même organisme, même graine).
- **H_B** : il existe une corrélation intra-groupe, et l'unité doit être l'organisme.
- **Données** : banque T0.5 de la couche 1, « 180 épisodes honnêtes notés par les juges » (C, § 4, RAPPORTÉ). C'est une HYPOTHÈSE que les identifiants de tâche et de groupe y figurent.
- **Métrique** : variance des moyennes par groupe, rapportée à sa loi sous permutation des étiquettes de groupe.
- **Seuil** : p de permutation < 0,05 → H_B.
- **Contrôle négatif** : étiquettes de groupe tirées au hasard.
- **Falsification** : H_B tenue falsifie le défaut D-S1 = « tâche » dans ce banc ; H_A tenue falsifie ma demande de passer à l'organisme.
- Si les étiquettes manquent, je ne présume rien : l'expérience attend la couche 2.

### E6 — La garde est-elle bien dimensionnée avec un effet de tâche sur les faux positifs ?
- **H_A** : 70 tâches honnêtes certifient δ = 0,10, et 150 certifient δ = 0,05, même avec un effet de tâche (écart-type 1 en logit) sur les faux positifs.
- **H_B** : il faut au moins 1,5 fois plus de tâches (facteur illustratif, à geler).
- **Métrique** : part des répétitions où la garde atteint 20, sans asymétrie vraie.
- **Contrôle négatif** : effet de tâche nul ; on doit reproduire S-sortie (1,0 à 70 tâches et δ = 0,10).
- **Falsification** : le résultat falsifie soit le dimensionnement de S (§ 2.4), soit a4.

---

## (c) Mesure minimale par instrument nommé dans la question

| Instrument | Fausses alertes : sur quels cas | Détection : sur quels cas | Vérification mécanique à battre ou à égaler |
|---|---|---|---|
| **Pari apparié, forme parts** | Mondes au nul symétriques, hétérogènes **et asymétriques** (E1). Jumeau B = A. Échange au hasard par tâche (témoin faux de S). | Écart planté de 0,10, 0,20 et 0,30, avec effets de tâche **propres à chaque moniteur** (a5). Dix et trois épisodes. | Test t apparié ou bootstrap par tâche à effectif fixe (E3). Le pari doit rester ≤ α, et sa perte de puissance doit être rapportée, pas supposée nulle. |
| **Forme signe** | Mêmes mondes que ci-dessus. Je prédis qu'elle échoue sur le monde asymétrique d'E1 pour le nul de moyenne. | Seulement pour une affirmation **déclarée** « A gagne sur la majorité des tâches ». | Test du signe exact à effectif fixe sur les tâches non ex æquo. |
| **Mélange sur la grille Λ** | Comme la forme parts. Le mélange porte sur une seule forme, sauf si E1 donne raison à S. | Écart entre le mélange et la meilleure mise a posteriori. | Prix théorique log |Λ| = log 4 pour quatre mises d'une même forme. La valeur doit être unifiée dans S (a8). |
| **Garde appariée (f_A − f_B ≥ δ)** | Tricheur à τ = 5 % contre τ = 1 % (contrôle n° 6 de S). Discrétisation d'E2. Effet de tâche d'E6. | Certification de δ sans asymétrie, avec effet de tâche. | Écart de taux réalisé calculé directement sur les tâches honnêtes d'épreuve, avec intervalle par tâche (bootstrap). La garde n'apporte quelque chose que si elle bloque ce que cet écart montre. |
| **Suite de confiance sur le taux absolu** | Taux vrai de 1 %, avec et sans effet de tâche. | Borne atteinte, à comparer aux chiffres de S-sortie (0,15, 0,08, 0,04, 0,05, 0,03, 0,025, RAPPORTÉ). | Clopper-Pearson avec effet de plan, c'est-à-dire n effectif = n / (1 + (m − 1)·CIC). La suite séquentielle sera plus large, et l'écart doit être rapporté. |
| **Règle du comparateur** | Monde d'E4. | Puissance à blanche de 0,65. | Intersection-union par minimum des e-valeurs : valide par construction, puisque min(W₁, …, W_k) est une e-valeur sous chacun des nuls. |
| **Paires « voisines » (H1b, H2b, H3b)** | Paires tirées par la règle sur des données permutées : promotion ≤ α. | Pente plantée. | Vérification mécanique : l'empreinte de la liste des paires est déposée **avant** le calcul des parts. Le journal du noyau doit le montrer. |
| **e-BH par mode** | Contrôle n° 10 de S (dix contrastes dont un vrai). | Puissance par mode. | Correction de Bonferroni sur les e-valeurs (seuil m/α) : e-BH doit faire au moins aussi bien. Référence : Wang, R. et Ramdas, A., « False discovery rate control with e-values », *JRSS B*, 2022 (à vérifier sur PDF). |
| **Témoins sans agents** | Témoin faux par strate : jamais promu au-delà de α. | Témoin vrai par strate : si aucun n'est promu, signal « pas de dents ». | Comptage mécanique fait par le noyau (J3, RAPPORTÉ : `etat_dents`). |

---

## (d) Ancrage matériel

- **Expériences E1 à E4 et E6** : simulation numpy sur processeur. S-sim fait déjà ce type de boucle. Par ordre de grandeur, quelques minutes à une heure par expérience à 1 000 répétitions (illustratif). **Aucune dépense.**
- **E5** : coût nul si la banque T0.5 porte les identifiants de groupe (HYPOTHÈSE). Sinon, elle attend la couche 2.
- **Modèles nommés par les faits** :
  - le moniteur noir de D1 : « même modèle que l'agent en juge » plus Llama-3.2-3B-Instruct (P, § 8, RAPPORTÉ) ;
  - Qwen2.5-7B comme hétérogénéité (P, § 8 et § 10, RAPPORTÉ) ;
  - un portage « sur 8B » cité pour EC.4 (P, § 10, RAPPORTÉ). Je n'en tire rien sur l'agent de G1.
- **Taille de banc pour G1** (calcul illustratif à partir de S, § 6 et § 2.4, pour 20 points d'écart et dix épisodes par tâche) :
  - environ 40 tâches sabotées par mode ;
  - trois modes au moins : « coût », « contrôles » et le mode tenu à l'écart (N-054), soit environ 120 tâches sabotées et 1 200 épisodes sabotés ;
  - 150 tâches honnêtes d'épreuve (pour δ = 0,05), soit 1 500 épisodes honnêtes ;
  - des tâches de calibrage et de développement en plus ;
  - au total, de l'ordre de 3 000 à 4 000 épisodes (illustratif), **avant** toute correction pour E6 et pour les effets de tâche propres à chaque moniteur.
- **Coût** : la couche 2 est estimée à 100 / 300 USD (C, § 4, RAPPORTÉ). Les faits ne donnent pas de coût par épisode. Je ne peux donc pas dire si ce budget couvre l'ordre de grandeur ci-dessus : c'est à chiffrer sur devis. Si 10 points d'écart sont l'effet réaliste, il faut environ 100 tâches par mode (S-sortie : 0,945 à 100 tâches), et le besoin est multiplié par 2,5.

---

## Réponses brèves aux six sous-questions

### 1. Validité
**Ce qui tient** (sous i.i.d. entre tâches) :
- la forme parts seule ;
- la garde, par union des nuls (S, § 3.5, raisonnement correct) ;
- le minimum des deux richesses comme e-valeur.

**Ce qui ne tient pas** : le mélange avec la forme signe pour le nul de moyenne (a1, E1).

**Hypothèses les plus fragiles sur un banc réel**, par ordre :
1. décalage du taux réalisé par discrétisation ou calibrage (E2) ;
2. dépendance entre tâches par organisme (E5) ;
3. effet de tâche sur les faux positifs honnêtes (E6) ;
4. génération non i.i.d. des tâches (a3).

Ce dernier point n'est pas testable : on le **déclare**.

**Les niveaux de 0,02 et 0,014** sont attendus pour une lecture continue à horizon fini. Ce n'est pas un réglage trop prudent, c'est le prix de la validité à tout instant. Ce prix ne se justifie pas pour une porte à lecture unique (E3).

### 2. Puissance et alternatives
- **Sous le nul de moyenne borné**, la mise est plafonnée à λ < 1, puisque v peut valoir −1. Une mise prévisible (Waudby-Smith et Ramdas, « Estimating means of bounded random variables by betting », référence à vérifier, déjà citée par S) supprime le prix du mélange, mais pas ce plafond.
- **Ordre de grandeur** (HYPOTHÈSE, illustratif) : avec moyenne 0,2 et E[v²] ≈ 0,09, la croissance à λ = 0,9 est d'environ 0,14 nat par tâche. Il faut alors une trentaine à une quarantaine de tâches, ce que S-sortie confirme pour la forme parts seule : 0,715 à 30 tâches, 0,98 à 40 (RAPPORTÉ).
- **Conséquence** : supprimer le signe coûte peu à 40 tâches et beaucoup à 20 ou 30.
- **Les processus e de rang, de permutation ou à deux échantillons** testent l'échangeabilité ou l'égalité des lois, c'est-à-dire **d'autres nuls**. Ils ne donnent pas plus de puissance « à garantie égale » pour l'affirmation de moyenne. Exemple : le test à deux échantillons par pari de Shekhar et Ramdas (référence à vérifier).
- **Les vrais leviers** sont ailleurs : plus d'épisodes par tâche (S-sortie : 0,50 à 30 tâches avec trois épisodes, contre 0,92 avec dix), et un test à effectif fixe pour G1 (E3).
- **« Le signe bat les parts » n'est pas général.** Il gagne quand le signe par tâche est fiable **et** que le monde est symétrique, et il change d'affirmation. Le monde d'E1 le rend trompeur.

### 3. Le point de fonctionnement
**La traduction « même taux nominal, asymétrie au plus δ » n'est pas acceptable avec δ = 0,10.** Un écart permis de 10 points autour d'un taux de 1 % autorise un rapport des taux allant jusqu'à 11. Le contrôle n° 6 de S admet lui-même qu'une asymétrie de 4 points n'est pas bloquée à 70 tâches honnêtes.

**Amendement proposé :**
- **(i) Apparier par construction plutôt que par garde.** On utilise des seuils randomisés (contre les ex æquo) ou des p-valeurs conformes calculées sur les tâches de calibrage. Référence : Bates, Candès, Lei, Romano, Sesia, « Testing for outliers with conformal p-values », *Annals of Statistics*, 2023 (à vérifier sur PDF). Avec des épisodes groupés, l'échangeabilité ne vaut qu'au niveau des tâches : c'est une HYPOTHÈSE à vérifier.
- **(ii) Décider à τ = 5 % et rapporter 1 % en descriptif.** Le critère de N-008 dit 1 % : ce changement est une décision de Lazar, pas une lecture.
- **(iii) Exprimer δ en multiple de τ** (par exemple δ ≤ τ), et déclarer « non certifiable » ce qui ne l'est pas.

**Ce qui serait trompeur** : écrire « à 1 % de faux positifs » dans le papier alors que seul le nominal est tenu, et qu'une cellule discrète tourne en réalité sous 1 %.

### 4. Les pentes
**La forme « contraste de contrastes apparié » est la plus lisible hors du pôle.** Une conclusion du type « en moyenne sur les tâches, l'écart à N₂ dépasse l'écart à N₁ » se lit sans modèle. L'inférence universelle avec une famille contrainte en signe dépend de cette famille, et une régression séquentielle dépend de sa spécification.

**Trois amendements :**
- au moins trois niveaux d'horizon ou de N, avec des poids de tendance déclarés et Σ|a| ≤ 1 ;
- H2 doit tester le rappel du séquentiel **seul** en fonction de l'horizon, comme le dit N-007, et non l'écart (a10) ;
- un dimensionnement propre aux pentes : le facteur ½ divise l'effet par deux, ce qui demande environ quatre fois plus de paires (illustratif). S ne dimensionne pas les pentes.

### 5. Plan d'analyse de G1, tel que je le gèlerais (dix lignes)
1. **Unité** : la tâche, ou l'organisme si E5 montre une corrélation intra-groupe. Partitions calibrage / développement / épreuve tirées **par unité**, empreintes au registre.
2. **Seuils** : randomisés ou conformes sur les tâches de calibrage, aux taux de 1 % et 5 %, scellés.
3. **Comparateur** : test d'intersection-union contre **toutes** les bases noires de N-008, dont (i), (iv) et le juge robustifié. Pas de sélection.
4. **Statistique primaire** : différence moyenne des rappels par tâche ; intervalle à 95 % par bootstrap de tâches à effectif fixe (cohérent avec N-054, point 4).
5. **Strates** : une analyse par mode (« coût », « contrôles », mode tenu à l'écart) plus une analyse tous modes.
6. **Règle de porte déclarée** : passe si tous modes **et** au moins deux modes dont le mode tenu à l'écart ont une borne basse > 0 (proposition à décider). La correction de multiplicité sur les modes est déclarée.
7. **Taux réalisés** : faux positifs des deux cellules rapportés avec intervalle par tâche ; porte suspendue si l'écart dépasse τ.
8. **Taille** : fixée avant l'épreuve par E3 et E6 (pas d'arrêt optionnel), avec un minimum de tâches par mode.
9. **Pari apparié (forme parts) en analyse secondaire** pour le pôle ; ses témoins vrais et faux sont jugés par strate.
10. **Échec** : la conséquence prévue reste inchangée (P, § 10 : résultat négatif publié, bascule vers H8). Le verdict est prononcé par un sous-agent neuf (R13).

**Ce qui me ferait dire que le pari apparié ne convient pas pour G1 :**
- E3 montre une perte de puissance supérieure à 0,15 à taille de banc atteignable ;
- ou E2 montre que l'appariement des taux ne s'obtient qu'en dehors du pari.

### 6. Recommandation : amender
1. Retirer la forme signe du mélange pour les affirmations de moyenne (H1, H2, H3, G1). La garder seulement pour une affirmation « majorité des tâches » déclarée avec son propre nul.
2. Remplacer la garde à δ fixe par un appariement par construction (seuils randomisés ou conformes). Garder la garde comme rapport, avec δ exprimé en multiple de τ.
3. Pour G1, un test primaire à effectif fixe, avec le pari en secondaire.
4. Un comparateur par intersection-union.
5. Des pentes sur au moins trois niveaux, H2 recentrée sur le rappel du séquentiel seul, et une redéfinition de H2a (a9).
6. Dans S-sim, ajouter des effets de tâche propres à chaque moniteur, le regroupement des faux positifs, les scores discrets et le monde asymétrique d'E1. Unifier le prix du mélange (a8) et corriger « de l'ordre de mille » (a7).

**Ce qui me ferait changer d'avis :**
- si E1 donne ≤ α, le mélange est rétabli et je retire a1 ;
- si E3 donne une perte ≤ 0,05, le pari peut être l'analyse primaire de G1 ;
- si E2 reste ≤ α avec scores discrets, la règle par quantile suffit et la garde n'a besoin que d'être resserrée.

FIN-DE-CELLULE