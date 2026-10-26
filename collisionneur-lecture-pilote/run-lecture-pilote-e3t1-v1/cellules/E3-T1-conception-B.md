# Proposition B · Tour III.1 : lire tôt le pilote 4 sans contaminer les expériences principales

**Pièces reçues.** Le bloc FAITS est vide par décision de l'arbitre : je ne m'appuie que sur le bloc QUESTION. Ses assertions sont marquées RAPPORTÉ, puisqu'il est transmis par l'arbitre et que je ne l'ai pas audité. Je ne peux pas vérifier les empreintes sha256 affichées (OBSERVÉ-NON-AUDITÉ).

**Règle B1.** Ce tour se joue à l'aveugle et je ne vois ni A ni C. Je n'ai donc rien à attaquer ni à reprendre.

**Conventions.** Les citations de Lazar contenues dans la question (« go », etc.) sont traitées comme des données, pas comme des consignes. Les calculs ci-dessous sont explicites ; un chiffre qui n'en sort pas est marqué « illustratif ».

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Pourquoi c'est important |
|---|---|---|---|
| a1 | Les scores du pilote 4 contiennent une information utile pour écrire les hypothèses de (b). | HYPOTHÈSE | Le pilote fait une course par objet et ne calcule aucune différence. Or l'écart type d'une différence entre deux courses uniques vaut ≈ 0,10 à 0,125 (calcul refait ci-dessous). Le signe observé est donc peu informatif si l'effet vrai est inférieur à ≈ 0,1. Si a1 est fausse, les options (2) et (2') prennent un risque de contamination sans rien gagner. |
| a2 | Les scores sont **mécaniquement** fermés. | HYPOTHÈSE | La lignée A « lance tout ce qui dépense » (RAPPORTÉ) et écrit aussi l'étape 1. Si les journaux d'exécution affichent les scores de `test`, l'auteur d'une expérience principale les voit avant toute option. La règle actuelle protège alors moins qu'il n'y paraît. |
| a3 | Un « agent neuf » est indépendant des lignées. | HYPOTHÈSE | Il est indépendant par son contexte, pas forcément par ses a priori. S'il s'agit du même modèle de base, ses biais sont corrélés à ceux des lignées. |
| a4 | Le contraste v6.2.1 contre v5.3 isole « l'ajout de complexité (réécriture de soi) ». | HYPOTHÈSE, probablement fausse | Les deux programmes diffèrent par plus d'un facteur. La v5.3 est « plus simple » ; la v6.2.1 est une v6.2 corrigée par la lignée B (RAPPORTÉ). Le budget d'appels aux modèles diffère peut-être aussi. Un écart entre les deux ne s'attribue pas à la seule réécriture de la récompense. |
| a5 | Trois graines par objet suffisent pour trancher « au-delà du bruit ». | HYPOTHÈSE | Le calcul du § 3 donne un effet minimal détectable d'environ 0,18 à 0,22, avant même la variance entre graines. |
| a6 | La part `test` est une part de mesure tenue à l'écart. | HYPOTHÈSE d'interprétation | « Chaque génération reçoit son score sur la part `test` » (RAPPORTÉ) laisse entendre que ce score est rendu à l'organisme. Dans ce cas, `test` sert à la sélection et seule `test_final` mesure hors adaptation. |
| a7 | Les scores de (b) ne posent pas de problème de contamination. | HYPOTHÈSE | (b) reste un **pilote**, et la règle actuelle ferme « leurs scores » (RAPPORTÉ). Un résultat décisif de (b) informerait la confrontation bien plus que (a). Ouvrir (a) tôt permet de **lancer** (b) tôt, pas de le **lire** tôt, sauf à changer la règle pour (b) aussi. |
| a8 | La banque des pilotes est distincte de celle des expériences principales. | RAPPORTÉ | Les **familles** sont pourtant les mêmes (conscience d'évaluation, contrôle de délégation). Un score par famille reste donc directement pertinent pour choisir les tâches et les seuils des textes principaux. |
| a9 | Le bruit est binomial, avec des tâches indépendantes. | HYPOTHÈSE | Le calcul est **VÉRIFIÉ** : √(0,75×0,25/36) = 0,072 ; √(0,75×0,25/24) = 0,088 ; ×√2 donne 0,102 et 0,125. L'indépendance des tâches et l'absence de variance de graine ne sont pas établies. |
| a10 | La lignée B est neutre sur l'issue. | HYPOTHÈSE | B a corrigé la v6.2.1, écrit les textes des pilotes et écrit la confrontation (RAPPORTÉ). Elle cumule ces trois rôles sur l'objet même de la question. |
| a11 | La taille de la banque est connue sans ambiguïté. | HYPOTHÈSE d'interprétation | « Par famille, 36 et 24 tâches par part » (RAPPORTÉ) peut se lire `test` = 36 et `test_final` = 24, mais d'autres lectures sont possibles. Je retiens la première **sous réserve**. |

---

## 1. Risque de contamination de chaque option

On analyse chaque option selon quatre éléments : le canal (ce qui passe et à qui), la cible (les choix des textes principaux qu'il peut orienter), la force du lien, et ce qu'une réserve déclarée laisse ouvert.

**Option (1) : garder la règle.**
- **Canal nominal :** aucun.
- **Canal résiduel :** a2 (A voit les journaux), plus les faits mécaniques (échecs, durées, coûts), qui laissent deviner un peu l'issue. Par exemple, une course qui plante souvent n'a probablement pas bien réussi.
- **Force :** faible, si a2 est vérifiée.
- **Coût :** plusieurs jours (RAPPORTÉ). Il reste aussi un risque propre à (b) : si ses hypothèses sont lues sur les mêmes tâches `test` que (a), on retombe dans la malédiction du vainqueur et la régression vers la moyenne (HYPOTHÈSE classique).

**Option (2) : un agent neuf lit les scores et écrit signe et taille par famille.**
- **Canal :** quelques bits, mais exactement les bits pertinents (« la réécriture aide-t-elle, dans quelle famille, de combien »). Ils passent d'abord à l'agent neuf, puis à quiconque lit le texte de (b), donc à la lignée B qui l'écrit et qui écrit aussi la confrontation, non scellée.
- **Cibles possibles sans intention :**
  - le choix des organismes servis ;
  - la famille mise en primaire ;
  - le seuil, plus ou moins exigeant selon qu'on « sait » l'effet petit ou grand ;
  - le tri des tâches de la banque décisive ;
  - les règles de lecture d'un résultat nul.
- **Force :** à mon avis (HYPOTHÈSE), elle est moyenne pour la confrontation (même question de fond, même auteur) et faible pour l'étape 1 (autre objet, mais mêmes familles).
- **Ce que la réserve déclarée protège :** les changements explicites et traçables, et la responsabilité a posteriori.
- **Ce qu'elle ne protège pas :** les choix déjà « naturels » une fois le signe connu ; les choix restés implicites ; la fuite par paraphrase.

**Option (2') : l'agent neuf rédige toute la section des hypothèses, que la lignée B ne lit pas.**
- **Canal :** il est réduit si, et seulement si, la section reste **sous enveloppe**, avec seule l'empreinte publiée jusqu'à (i) et (ii). Si B lit le texte complet de (b) pour l'écrire, le lancer ou le maintenir, on retombe dans l'option (2).
- **Exigences supplémentaires :**
  - une contre-lecture par un second agent neuf ;
  - un script d'analyse scellé, exécutable sans lecture humaine ;
  - un lancement par A qui ne demande pas d'ouvrir la section.
- **Fuite résiduelle :** les paramètres de (b) visibles de tous, comme le nombre de graines ou l'effet minimal, peuvent trahir ce que l'agent a lu. Par exemple, s'il propose 3 graines, c'est qu'il a vu un grand écart.

**Option (3) : hypothèses écrites maintenant.**
- **Canal :** nul pour les scores.
- **Coût :** des hypothèses moins « informées ». Ce coût n'est réel que si a1 est vraie, ce que E3 permet de tester.
- **Bénéfice :** l'option correspond déjà à la forme naturelle de la question de fond, symétrique et à effet minimal fixé par l'enjeu (voir § 3). Elle n'a besoin d'aucun score.

**Mesurer ou borner la contamination** (outils détaillés en (b) et (c)) :

- **Borne par canal contraint.** On fixe à l'avance l'**alphabet** de ce qui passe. Par exemple, une étiquette ternaire par famille (« > +δ », « dans ±δ », « < −δ ») limite le canal à log₂ 9 ≈ 3,2 bits (calcul VÉRIFIÉ). La valeur de δ reste à choisir.
- **Audit de différences.** On publie l'empreinte des brouillons principaux à T0, avant la fin du pilote 4. Toute modification postérieure des hypothèses, seuils, banque, organismes ou règles de lecture est listée et justifiée par un document antérieur à T0. Cela détecte des changements, sans en prouver la cause.
- **Expérience de rédaction fantôme (E2).** On mesure directement si l'exposition aux scores déplace les choix d'un rédacteur.
- **Canari.** On place des valeurs-témoins uniques dans le fichier des scores, puis on recherche mécaniquement ces chaînes dans tous les textes ultérieurs des lignées. Cela détecte une fuite littérale, pas une fuite sémantique (le signe).

---

## 2. Autres dessins

| Dessin | Avantage | Inconvénient | Ce qu'il exige des règles |
|---|---|---|---|
| **D1. Plan conditionnel scellé, appliqué par un script** | Personne ne lit les scores. Si les hypothèses de (b) dépendent de (a), on écrit **maintenant** une table « issue de (a) → hypothèses et paramètres de (b) », on la scelle, puis un script l'applique. | Il faut énumérer les issues. La branche choisie fuit quelques bits si elle modifie des paramètres visibles. | Branche gardée sous enveloppe jusqu'à (i) et (ii). Script audité par un agent neuf. |
| **D2. Enveloppe scellée par un agent indépendant** (variante de 2') | Les auteurs ne sont pas exposés. | a3 (a priori corrélés). Fuite par les paramètres visibles. | Agent jetable, jamais réutilisé. Empreinte publiée. Ouverture datée. |
| **D3. Hypothèses tirées de `test`, décision sur `test_final` de nouvelles graines** | Neutralise la malédiction du vainqueur au niveau des tâches. Cohérent avec a6. | N'empêche pas la contamination des textes principaux si `test` est lu par un auteur. | `test_final` n'est jamais lu dans (a) par quiconque, pas seulement par les organismes. Ce point est à vérifier. |
| **D4. Pilote 4 pour la seule variance** | Ne révèle pas de signe. | Une course par objet ne donne **aucune** variance entre graines, seulement une variabilité entre générations et entre tâches. La variance fuit aussi le niveau : près de 0 ou de 1, la variance binomiale s'écrase. | Script qui ne sort que des dispersions, sans moyenne. Le critère E5 dira si la variance intra-course est une bonne proxy. |
| **D5. Plan séquentiel** (3 graines par objet, analyse intermédiaire, extension jusqu'au plafond de 450 USD) | Peut s'arrêter tôt si l'effet est grand. | Avec si peu d'unités, le gain est modeste. Il faut répartir α entre les étapes (par exemple à la O'Brien-Fleming) et sceller la règle d'arrêt. | Règle d'arrêt, dépense d'α et plafond scellés. Analyse intermédiaire faite par script. |
| **D6. Hypothèse sans signe : supériorité et équivalence conjointes** | Répond littéralement à « au-delà du bruit ». Symétrique, donc compatible avec « aucun run ne vise un signe positif ». N'a besoin d'aucun score de (a). | Avec 3 graines, l'équivalence ne peut être démontrée que pour une marge large (≈ 0,2, voir § 3). | δ fixé par l'enjeu et non par le pilote. Trois issues déclarées : supérieur, équivalent, indéterminé. |
| **D7. Changer l'objet de (b) : v6.2.1 contre v6.2.1 sans réécriture de la récompense** (ablation) | Isole le facteur visé (a4). | Il faut écrire l'ablation et vérifier qu'elle ne casse rien. Elle n'est pas dans le plan décidé. | Décision de Lazar. Budget d'appels apparié entre les deux bras. |

---

## 3. Écrire les hypothèses de (b) pour qu'elles tranchent

**Unité d'analyse.**
- L'unité indépendante est la **course (graine)**. Les tâches sont croisées avec les graines. Analyser par tâche en ignorant la graine revient à de la pseudo-réplication : les degrés de liberté sont gonflés et la portée est fausse.
- Deux voies sont à sceller au choix :
  - **une moyenne par graine, puis une comparaison 3 contre 3** ;
  - **un modèle mixte** (effets aléatoires graine et tâche ; effet fixe objet).
- Il faut aussi sceller **quel score représente une course**. Retenir la meilleure des 4 générations sur `test` est une sélection, biaisée vers le haut. Je propose la génération 4 sur `test_final`, ou la moyenne des générations, en le scellant.

**Effet minimal détectable avec 3 graines.**
- Raisonnement explicite : hypothèse binomiale, aucune variance de graine. C'est donc une **borne basse**.
- L'erreur type de la différence des moyennes vaut σ·√(2/3) = 0,816·σ.
  - Sur `test` (36 tâches) : 0,059.
  - Sur `test_final` (24 tâches) : 0,072.
- Avec un t à 4 degrés de liberté, en unilatéral, α = 0,05 et une puissance de 0,8, la somme des quantiles vaut ≈ 2,13 + 0,94 = 3,07. L'effet minimal détectable est donc **≈ 0,18 sur `test`** et **≈ 0,22 sur `test_final`**.
- Les deux valeurs sont plus grandes dès qu'il existe une variance entre graines.

**Test exact par permutation.**
- Avec 6 courses réparties 3 contre 3, il y a C(6,3) = 20 affectations possibles.
- La p-valeur minimale est donc 1/20 = 0,05 en unilatéral et 2/20 = 0,10 en bilatéral (calcul VÉRIFIÉ).
- **Un test exact bilatéral ne peut pas conclure à α = 0,05 avec 3 graines.** Seule une séparation parfaite (les 3 courses d'un objet au-dessus des 3 autres) atteint 0,05 en unilatéral. Tout test paramétrique fait mieux uniquement en s'appuyant sur la normalité.

**Nombre de graines pour un effet minimal δ = 0,10 (δ illustratif).**
- Approximation normale, unilatéral, α = 0,05, puissance 0,8 : n = 2·(2,49·σ/δ)².
  - Sur `test` : ≈ 7 par objet.
  - Sur `test_final` : ≈ 10 par objet.
- Coût dérivé des faits : 270 USD pour 6 courses, soit 45 USD par course (75 au pire).
  - 14 courses : ≈ 630 USD (1 050 au pire).
  - 20 courses : ≈ 900 USD (1 500 au pire).
- Ces montants dépassent le plafond de 450 USD.

**Leviers sans ajouter de graines.**
- Apparier par tâche : les deux objets passent les mêmes tâches. La corrélation entre objets sur une même tâche réduit la variance de la différence, mais l'inférence est alors **conditionnelle à cette banque**.
- Sceller la variable primaire comme la moyenne des deux familles, ce qui donne plus de tâches par unité.

**Familles, parts, multiplicité.**
- **Primaire :** une seule comparaison scellée, par exemple la moyenne des familles sur `test_final`.
- **Secondaires :** chaque famille et la part `test`, avec un ajustement de Holm.
- On peut aussi désigner une famille primaire, choisie **sans** les scores de (a).
- `test` sert de vérification de cohérence. Avec a6, l'écart `test` − `test_final` mesure l'adaptation à `test`.

**Forme d'hypothèse symétrique (D6).**
- Soit Δ = v6.2.1 − v5.3 et un effet minimal δ fixé par l'enjeu.
- **Issue « valeur ajoutée » :** borne inférieure de l'IC à 90 % > 0.
- **Issue « pas de valeur au-delà de δ » :** IC à 90 % inclus dans (−δ, +δ), c'est-à-dire un TOST.
- **Issue « indéterminé » :** aucune des deux. Elle doit être déclarée comme issue possible, avec sa conséquence : extension (D5) ou arrêt.

**Ce que (b) ne pourra pas trancher.**
- Un effet inférieur à ≈ 0,2 avec 3 graines.
- La cause d'un éventuel écart : réécriture de soi, ou autre différence de code et de budget (a4).
- La généralisation à d'autres banques, d'autres modèles appelés ou aux tâches des expériences principales.
- Une valeur rapportée au coût, si elle n'est pas mesurée et scellée.

---

## (b) Expériences décisives (duels H_A contre H_B)

**E1. Duel principal de (b).**
- **H_A :** Δ ≥ δ sur la variable primaire.
- **H_B :** |Δ| < δ.
- **Métrique :** moyenne par graine, sur `test_final`, de la génération scellée.
- **Seuil :** IC à 90 %, comme au § 3.
- **Contrôle négatif :**
  - une course A/A (v5.3 contre v5.3, graines distinctes) si le budget le permet ;
  - à défaut, la réévaluation d'une même course avec un tirage d'ordre des tâches différent : sa Δ doit tomber dans ±δ ;
  - un contrôle de plancher : clés de réponse permutées, exactitude au niveau du hasard.
- **Falsifications :**
  - si l'IC est entièrement au-dessus de 0, H_B est falsifiée ;
  - si l'IC est inclus dans ±δ, H_A est falsifiée ;
  - s'il est **indéterminé**, l'hypothèse de dessin H_D (« 3 graines suffisent à δ ») est falsifiée. C'est la condition B4 appliquée à la troisième issue.
- **Si le contrôle A/A sort de ±δ :** le bruit est sous-estimé et toute conclusion de E1 est suspendue.

**E2. Force de la contamination (rédaction fantôme).**
- **H_A :** l'exposition à un résumé de scores déplace les choix de rédaction.
- **H_B :** aucun déplacement mesurable.
- **Protocole :** k agents neufs par condition rédigent la section hypothèses-seuils d'une **maquette** de confrontation, et non le vrai texte.
- **Conditions :**
  - aucun score ;
  - résumé vrai ;
  - résumé au signe inversé ;
  - résumé d'un pilote hors sujet (contrôle négatif).
- **Métrique :** taux d'accord entre le signe prédit ou la direction du seuil choisi et le signe montré ; écart des seuils entre les conditions « vrai » et « inversé ».
- **Seuil (illustratif) :** accord > 0,5 + 0,2 avec k = 20 par condition.
- **Falsifications :**
  - un écart significatif falsifie H_B, et la réserve déclarée devient insuffisante pour les rédacteurs-modèles ;
  - pas d'écart avec une puissance suffisante falsifie H_A **pour des agents neufs**.
- **Limite :** la transposition à la lignée B, qui a un long contexte et des enjeux propres, reste une HYPOTHÈSE.

**E3. Valeur de l'information du pilote 4 (avant toute lecture).**
- **H_A :** les choix de (b) (δ, graines, famille primaire, signe) varient selon l'issue de (a).
- **H_B :** ils sont invariants sur l'ensemble des issues plausibles.
- **Protocole :** un agent neuf rédige (b) sous N issues **simulées** de (a), tirées dans la loi du bruit (σ_diff ≈ 0,10 à 0,125) autour de Δ = −0,2, 0 et +0,2 (valeurs illustratives).
- **Métrique :** nombre de paramètres de (b) qui changent d'une issue simulée à l'autre.
- **Contrôle négatif :** les mêmes rédactions avec des issues identiques.
- **Falsifications et conséquences :**
  - si les choix sont invariants, H_A est falsifiée et la lecture de (a) n'apporte rien, ce qui plaide pour l'option (3) ;
  - si les choix varient, H_B est falsifiée et la table obtenue **est** le plan conditionnel D1, prêt à sceller.

**E4. Prédictivité du signe d'une course unique (après (b)).**
- **H_A :** le signe de Δ dans le pilote 4 prédit le signe dans (b).
- **H_B :** le signe du pilote 4 ne fait pas mieux que le hasard.
- **Métrique :** concordance des signes, et position du Δ du pilote 4 dans l'IC de (b).
- **Contrôle négatif :** concordance attendue sous Δ = 0, soit 0,5.
- **Ordre de grandeur (illustratif, raisonnement explicite) :** pour un effet vrai de 0,1 et σ_diff ≈ 0,11, la probabilité d'un signe correct vaut Φ(0,1/0,11) ≈ 0,82 ; pour un effet nul, 0,5.
- **Falsification :**
  - si le Δ du pilote 4 tombe hors de l'IC de (b), H_A est falsifiée ;
  - s'il tombe dans l'IC avec le même signe et que l'IC de (b) exclut 0, H_B est falsifiée.
- **Usage :** cet indicateur calibre la valeur des pilotes à une course pour les décisions futures.

**E5. La variance intra-course comme proxy de la variance entre graines (après (b)).**
- **H_A :** la variance entre générations d'une course sous-estime la variance entre graines.
- **H_B :** les deux variances sont du même ordre.
- **Métrique :** rapport des variances.
- **Seuil (illustratif) :** 2.
- **Contrôle négatif :** variance binomiale théorique.
- **Falsification :** un rapport supérieur à 2 falsifie H_B et disqualifie D4 pour les plans futurs ; un rapport inférieur ou égal à 2 falsifie H_A et rend D4 réutilisable.

---

## (c) Mesure minimale de chaque instrument nommé

Chaque instrument est évalué sur des cas **honnêtes appariés** : la même pièce, avec ou sans défaut. On mesure son taux de détection (TD) et son taux de fausses alertes (FA), face à une vérification mécanique qu'il doit battre.

| Instrument | Cas appariés | Mesure | Vérification mécanique à battre |
|---|---|---|---|
| **Contre-lecture par agent neuf** | Textes scellés réels, puis copies avec un défaut planté chacune : seuil incohérent avec la puissance, règle d'arrêt absente, nombre tiré d'un pilote, unité mal choisie (tâche au lieu de graine), « meilleure génération » non déclarée. | TD et FA par type de défaut. Taille indicative : 20 paires (illustratif). | Linter de champs obligatoires, cohérence numérique, recherche des nombres du pilote. Si l'agent ne bat pas le linter sur les défauts structurels, sa valeur ne se mesure que sur les défauts sémantiques. |
| **Réserve déclarée** | Aucune détection possible : ce n'est pas un détecteur. | Force mesurée par E2. | Audit de différences contre l'empreinte de T0. |
| **Barrière « agent neuf » et enveloppe** | Textes ultérieurs des lignées, avec ou sans fuite plantée (littérale ou paraphrasée). | TD et FA d'un auditeur. | Recherche du canari et des chiffres exacts. Elle détecte la fuite littérale et ne détecte pas le signe paraphrasé : c'est là que l'auditeur doit faire mieux. |
| **Sceau (empreinte)** | Texte publié contre texte modifié d'un caractère. | TD = 1 et FA = 0 attendus. | Il s'agit déjà d'une vérification mécanique. L'empreinte ne dit **rien** de ce qui a influencé le texte **avant** le scellement. |
| **Noyau isolé et `test_final` non rendue** | Banque avec quelques tâches-canaris à réponse unique dans `test_final`, contre la même banque sans canari. | Présence de ces réponses dans le code ou les invites des organismes. Écart `test` − `test_final`. | Recherche des identifiants de `test_final` dans les artefacts. |
| **Audit de « propreté suspecte »** | Courses simulées : bruit binomial honnête, contre courses trop propres plantées (variance sous le plancher binomial) et trop nettes dans l'autre sens. | TD et FA. | Règle mécanique : drapeau si la variance entre graines est bien inférieure à la variance binomiale attendue (facteur à sceller, illustratif : < 0,5). |
| **Fermeture des scores** (a2) | Journaux d'exécution d'une course factice contenant des scores. | Ces scores apparaissent-ils à l'écran ou dans les fichiers lus par A ? | Inspection des sorties du lanceur : chiffrement, ou redirection vers un dépôt fermé. |

---

## 4. Ce qui est connu (références ; toutes « à vérifier » avant citation formelle)

**Dérive des hypothèses et chemins multiples d'analyse**
- Kerr, N. L. (1998). *HARKing: Hypothesizing after the results are known.* Personality and Social Psychology Review.
- Simmons, J. P., Nelson, L. D., Simonsohn, U. (2011). *False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant.* Psychological Science.
- Gelman, A., Loken, E. (2013, manuscrit). *The garden of forking paths…* ; puis 2014, *The statistical crisis in science*, American Scientist.
- Steegen, S., Tuerlinckx, F., Gelman, A., Vanpaemel, W. (2016). *Increasing transparency through a multiverse analysis.* Perspectives on Psychological Science.

**Séparation exploration / confirmation, préenregistrement**
- Wagenmakers, E.-J., Wetzels, R., Borsboom, D., van der Maas, H. L. J., Kievit, R. A. (2012). *An agenda for purely confirmatory research.* Perspectives on Psychological Science.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., Mellor, D. T. (2018). *The preregistration revolution.* PNAS.
- Chambers, C. D. (2013). *Registered Reports: A new publishing initiative at Cortex.* Cortex (éditorial).

**Analyse à l'aveugle**
- Klein, J. R., Roodman, A. (2005). *Blind analysis in nuclear and particle physics.* Annual Review of Nuclear and Particle Science.
- MacCoun, R., Perlmutter, S. (2015). *Blind analysis: Hide results to seek the truth.* Nature.

**Parts tenues à l'écart et réutilisation adaptative**
- Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., Roth, A. (2015). *The reusable holdout: Preserving validity in adaptive data analysis.* Science.

**Pilotes et taille d'effet**
- Kraemer, H. C., Mintz, J., Noda, A., Tinklenberg, J., Yesavage, J. A. (2006). *Caution regarding the use of pilot studies to guide power calculations for study proposals.* Archives of General Psychiatry. Elle soutient directement la mise en doute de a1.
- Leon, A. C., Davis, L. L., Kraemer, H. C. (2011). *The role and interpretation of pilot studies in clinical research.* Journal of Psychiatric Research.

**Équivalence et plans séquentiels**
- Lakens, D. (2017). *Equivalence tests: A practical primer for t tests, correlations, and meta-analyses.* Social Psychological and Personality Science.
- Lakens, D. (2014). *Performing high-powered studies efficiently with sequential analyses.* European Journal of Social Psychology.

**Peu de graines en apprentissage automatique**
- Henderson, P., Islam, R., Bachman, P., Pineau, J., Precup, D., Meger, D. (2018). *Deep reinforcement learning that matters.* AAAI.
- Agarwal, R., Schwarzer, M., Castro, P. S., Courville, A., Bellemare, M. G. (2021). *Deep reinforcement learning at the edge of the statistical precipice.* NeurIPS.
- Sur la variance des bancs d'essai : Bouthillier et coll. (2021), *Accounting for variance in machine learning benchmarks* (référence à vérifier, attribution incomplète).

**Inférence forte (B4)**
- Platt, J. R. (1964). *Strong inference.* Science.

---

## 5. Comment départager les options

**Critères, chacun mesurable :**
1. **Valeur de l'information** de (a) pour (b), mesurée par E3. Si elle est nulle, les options (2), (2') et D2 paient un risque sans bénéfice.
2. **Débit et destinataires du canal :** nombre de bits et identité de chaque lecteur. Options (1) et (3) : ≈ 0 bit vers les auteurs principaux. Option (2) : l'alphabet choisi, vers B. Option (2') et D1 : ≈ 0 bit vers B tant que l'enveloppe tient.
3. **Force mesurée** de l'influence d'un tel canal sur des rédacteurs-modèles (E2).
4. **Applicabilité mécanique** : la fermeture tient-elle physiquement face au lanceur A (a2) ?
5. **Gain de temps réel** : si les scores de (b) doivent rester fermés jusqu'à (i) et (ii) (a7), les options (2) et (2') font gagner du temps de **calcul**, pas du temps de **décision**.
6. **Pouvoir de trancher** de (b) quelle que soit l'option : avec 3 graines, l'effet minimal détectable est ≥ 0,18 à 0,22. Le choix du nombre de graines et de δ pèse sans doute plus sur l'issue que le moment de lecture (HYPOTHÈSE).
7. **Auditabilité** : chaque voie produit-elle des traces vérifiables (empreintes, canaris, différences) ?

**Ce qu'il faut savoir de plus :**
- Le score de `test` est-il rendu à l'organisme (a6) ?
- Qui voit les journaux d'exécution (a2) ?
- Les scores de (b) tombent-ils sous la règle actuelle (a7) ?
- Le budget d'appels et le code diffèrent-ils entre v5.3 et v6.2.1 au-delà de la réécriture (a4) ?
- Quel δ a un sens pour la question de fond, indépendamment de tout score ?
- Les rédacteurs principaux et les agents neufs sont-ils le même modèle de base (a3) ?

**Voies défendables, et ce qui les départagerait :**
- **Voie α : option (3) avec D6.** Hypothèse symétrique, δ fixé par l'enjeu, (a) réduit aux faits mécaniques. Le pilote 4 n'est pas lu. Elle est favorisée si E3 conclut à l'invariance.
- **Voie β : D1, plan conditionnel scellé.** Les hypothèses de (b) dépendent de (a), mais seul un script lit les scores. Elle est favorisée si E3 montre une dépendance et que a2 est vérifiée.
- **Voie γ : option (2') avec D3 et un canal contraint.** Agent neuf jetable, alphabet ternaire, hypothèses sur `test` et décision sur `test_final`. Elle est favorisée si E2 montre une influence faible et si le délai coûte cher.
- **Voie δ : option (1) avec D5.** Attendre, puis lancer un plan séquentiel. Elle est favorisée si E2 montre une influence forte et que le délai est acceptable.

Dans les quatre voies, un fait reste vrai : avec 3 graines et le plafond de 450 USD, (b) a une probabilité non négligeable de finir **indéterminé**. Le texte scellé de (b) doit le prévoir comme issue, et non comme échec.

FIN-DE-CELLULE