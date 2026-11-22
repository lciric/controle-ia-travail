# Proposition B : Tour III.3, réponse aux critiques

## 0. Pièces reçues

- **Liste de publications : toujours absente.** Je n'en invente rien.
- **Ma conception III.1 : reçue et complète.**
- **Critiques A, C, D, E et F : reçues.** Chacune se termine par son marqueur, sans coupure visible. Je ne traite que leurs sections « Sur la proposition B ». Je n'ai pas recalculé les empreintes.
- **Statuts.**
  - « La critique X dit Y » est VÉRIFIÉ, au sens où je l'ai lu.
  - Mes corrections de plans sont des HYPOTHÈSES.
  - Tous les chiffres sont **illustratifs**, sauf les calculs que j'ai refaits, qui sont signalés comme tels.
- **Règle B1.** Quand je reprends un élément d'une autre proposition, je le dis. Je ne fusionne rien.

---

## (a) Décision sur chaque critique

| # | Critique (sources) | Décision | Suite donnée |
|---|---|---|---|
| K1 | La règle par IC95 crée une large zone « non tranchée » près de θ, faute de marge (C b1, E b1, F b1). | **Rejetée en partie.** Tout test à effectif fini a une telle zone. La déclarer vaut mieux que forcer un verdict, et c'était voulu. **Transformée en test.** | Marge m préenregistrée et calcul d'effectif. La troisième issue devient falsifiante (règle R0). |
| K2 | E2 et E6 posent des conjonctions non exhaustives : une issue n'appartient à aucun des deux verdicts (A a4, C a1, D a, D b). | **Acceptée.** | Statistique g = minimum des marges signées, avec bornes simultanées. C'est la règle proposée par D, que je reprends en le disant. |
| K3 | En E1, κ est gonflé par la classe « aucune » et par les témoins injectés, et dépend de la proportion injectée λ (A a1, E b2, F a3). | **Acceptée.** | Les témoins sortent du calcul de κ. κ est calculé par attribut, sur une population fixe. |
| K4 | La catégorie unique force un désaccord sur les énoncés à engagements multiples (D a). | **Acceptée.** | Codage multi-étiquette en trois attributs binaires. |
| K5 | Si « annoncé » est rare, κ n'est pas jugeable (A b, C b3). | **Acceptée.** | Échantillonnage inverse jusqu'à k positifs par attribut. À défaut, l'attribut est déclaré non jugeable. |
| K6 | Fuite E1 → I1 ; la référence par expressions régulières reprend les marqueurs de la grille (A a2). | **Fuite : acceptée.** **Regex : rejetée en partie.** Un plancher qui partage le lexique reste le bon plancher : un extracteur qui ne le bat pas n'apporte rien au-delà du lexique. | Partition disjointe par équipe. Résultats rapportés séparément sur la **strate sans marqueur**, où la regex vaut zéro par construction. |
| K7 | Les témoins négatifs d'E1 sont triviaux ; il manque les limites attribuées à des tiers et les restrictions volontaires de périmètre ; 60 phrases ne suffisent pas (C b3, C c1, E c1, F c1, D c). | **Acceptée.** | Charge de la preuve inversée : la grille n'est validée que si la borne supérieure du taux d'erreur est sous 10 %. |
| K8 | La vérité terrain d'E2 n'est pas indépendante ; les comblements « connus » sont ceux qui étaient trouvables (A a3, C a3, F a2, E b2). | **Acceptée.** | Trois canaux, dont deux disjoints de la procédure. Le rappel calculé sur l'union est une **borne supérieure**. |
| K9 | « Partiellement comblé » n'a pas de codage fixé (A a4, E a3, E b3). | **Acceptée.** | Analyse principale préenregistrée, plus une analyse de sensibilité. |
| K10 | Avec 30 manques fabriqués, 0/30 donne une borne supérieure de 0,116 > φ₂ = 0,10 : la condition « ≤ φ₂ » est indémontrable (F b, A b). | **Acceptée.** J'ai refait le calcul : 1 − 0,025^{1/30} ≈ 0,116. | Environ 120 négatifs (illustratif). |
| K11 | Les négatifs fabriqués sont hors distribution (A c, D b, F c). | **Acceptée.** | Les quasi-comblements réels deviennent majoritaires parmi les négatifs. C'est la proposition de A, C et F, que je reprends. |
| K12 | Le rappel n'est pas jugeable si les manques comblés sont peu nombreux (A b, F b). | **Acceptée.** | Échantillonnage inverse jusqu'à environ 60 positifs. |
| K13 | Un faible rappel ne prouve pas que les citations manquent (D a). | **Acceptée.** | H_B ne porte plus de mécanisme. La part des comblements sans citation devient un diagnostic. |
| K14 | L'issue d'E3 mesure l'affluence, c'est-à-dire qui a essayé, et non la qualité du choix (A a5, C a2, D a, E a1, F a1). | **Diagnostic : accepté.** **Conséquence « hors sujet » : rejetée.** Pour une petite équipe, l'affluence est le risque d'être doublée, qui fait partie d'un bon choix (P8). **Transformée en test.** | E3a mesure l'affluence comme un **risque**, avec un signe inversé. E3b mesure le rendement conditionnel à une tentative. E3p est une version prospective. |
| K15 | L'issue d'E3 est mesurée par I2, dont le rappel dépend du critère 5 (A a6). | **Acceptée.** | Rappel d'I2 stratifié en E2. L'issue d'E3 est mesurée sur l'union des trois canaux. |
| K16 | Le test de fuite ne détecte pas la fuite cognitive des codeurs qui connaissent t₁ (A a7, E a2, F a1, D a). | **Acceptée.** Mon test était logiquement insuffisant. | Codage aveugle sur versions figées. Comparaison entre codeurs informés et codeurs aveugles (reprise de E). Critère placebo (reprise de A). |
| K17 | La régression logistique est ajustée sans validation ; optimisme ; moins de 10 événements par paramètre (C a2, E a2, E b4, F b). | **Acceptée.** | Plus aucun poids ajusté : le score est une somme non pondérée, figée avant les données. |
| K18 | Prendre le maximum de plusieurs références biaise l'écart (E b4). | **Acceptée.** | Un seul comparateur principal, préenregistré. |
| K19 | L'AUC n'est pas jugeable avec peu de positifs ; δ₃ est inférieur à une erreur type (A b). | **Acceptée.** | Seuil d'exécution : E3 n'est pas lancée en dessous d'un effectif minimal. |
| K20 | « Échec aux critères 1, 2 et 7 = mauvais choix quelle que soit l'issue » est vrai par définition (A a8). | **Acceptée.** | **Retirée** comme affirmation empirique. Si on la garde, c'est une norme procédurale déclarée non testée. |
| K21 | E4 est confondue par les équipes ; le témoin d'un autre domaine n'est pas un nul (A a9, C c2, D a, F a3). | **Acceptée.** | Comparaison intra-équipe. L'autre domaine fournit un taux de base descriptif seulement. |
| K22 | E4 subit une censure à droite à Δ fixe (A b, E b3, F b). | **Acceptée.** | Analyse de survie. |
| K23 | E5 mesure une concordance, pas une justesse, et n'a pas de fonction de valeur (C a3, D a). | **Rejetée en partie.** E5 ne prétend pas mesurer la justesse. La question impose le « texte seul », et E5 mesure la sensibilité d'une même procédure à cette restriction ; la concordance est la grandeur adaptée. **Acceptée** pour les témoins. | Dossier placebo, contrôle positif et pièces datées au plus tard de t₀. |
| K24 | θ₅ est inatteignable si le bruit entre lecteurs est élevé (A b, E b5, F b). | **Acceptée.** | Hypothèse reformulée relativement au bruit entre lecteurs. |
| K25 | Le pronostic de l'équipe n'est ni mécanique ni indépendant des indicateurs (C a3). | **Libellé : accepté.** **Indépendance : rejetée.** L'ordre temporel l'assure : le pronostic est haché avant que les indicateurs soient définis. | On ajoute une référence mécanique : citations et récence. |
| K26 | En E6, la consigne de dégradation laisse une trace ; il manque les échecs honnêtes et les consignes placebo (A a10, C c3, D c, E c3, F c). | **Acceptée.** | Voir E6'. |
| K27 | En E6, la meilleure vérification mécanique est choisie sur le lot de test ; fuite de calibration (A a10, D a, F a4). | **Acceptée.** | Lot de calibration disjoint par tâche. |
| K28 | E6 compare des taux marginaux au lieu de l'union, sans FPR apparié (E a3). | **Acceptée.** La borne ΔTPR ≤ 1 − TPR_méc, relevée par C et E à propos de F, s'applique aussi à moi. | Voir E6'. |
| K29 | Un seuil à 1 % n'est pas identifiable sur 300 trajectoires honnêtes corrélées par tâche (A b, C b2, E b6, F b). | **Acceptée.** | Seuil principal à 5 % ; le point à 1 % devient descriptif. |
| K30 | La formule 1 − (1 − p)ⁿ suppose l'indépendance ; sous hétérogénéité, par Jensen, elle surestime (E b6, F b). | **Acceptée.** Le chiffre illustratif de 39 % est une **borne supérieure**, pas une estimation. La conclusion tient : il faut fixer le FPR par trajectoire. | Comparaison empirique entre la formule et le taux observé par trajectoire. |
| K31 | La corrélation intra-équipe n'est pas prise en compte (A b, C b3, E b4, F b). | **Acceptée.** | Bootstrap par équipe. |
| K32 | Les tentatives échouées et non publiées sont invisibles (E a1). | **Acceptée comme limite non corrigeable.** | E3b est non identifiable sur ces échecs. Le point est ajouté à « ce qui n'est pas établi ». |

---

## (b) Expériences corrigées

Statut de tout ce qui suit : HYPOTHÈSE. Tous les chiffres sont **illustratifs**.

### R0 : règle commune révisée

Pour chaque métrique principale g, on préenregistre trois éléments :
- le seuil θ ;
- une marge de pertinence m ;
- un effectif N tel que P(non tranché) ≤ 0,2 lorsque |μ − θ| ≥ m. Ce calcul utilise l'effet de plan par grappes d'équipes.

La règle d'issue est la suivante :
- IC95 entièrement au-dessus de θ : H_B est falsifiée ;
- IC95 entièrement en dessous : H_A est falsifiée ;
- IC95 à cheval sur θ, mais contenu dans [θ − m, θ + m] : on conclut que |μ − θ| < m. Cela falsifie toute revendication d'un écart pertinent dans un sens ou dans l'autre ;
- IC95 à cheval sur θ et plus large que prévu : **l'hypothèse de variance du plan est falsifiée**. On publie la largeur réalisée.

Pour une revendication conjointe, g est le minimum des marges signées, avec des bornes simultanées de Bonferroni (règle de D, que je reprends).

### E1' : extractibilité « texte seul » (teste P4)

- **Unité.** Énoncés des sections limitations, discussion et conclusion, plus une strate d'énoncés sans marqueur lexical, tirés au hasard du reste de l'article.
- **Codage multi-étiquette** en trois attributs binaires : A1 « reconnu non fait », A2 « annoncé par les auteurs », A3 « dit ouvert à d'autres ».
- **H_A(j) :** κ(A_j) ≥ θ₁ (0,6). **H_B(j) :** κ(A_j) < θ₁.
  - κ est calculé sur la population fixe des énoncés, et non sur un sous-ensemble défini par les décisions des lecteurs.
  - On rapporte aussi la prévalence et l'accord positif et négatif.
- **Partition disjointe par équipe** en trois lots : écriture de la grille, mesure de κ, évaluation d'I1.
- **Effectif.** On échantillonne jusqu'à environ 60 positifs par attribut. Si on ne les atteint pas, l'attribut est déclaré non jugeable et on rapporte sa prévalence.
- **Test de défaillance de la grille**, séparé et exclu de κ. Il porte sur environ 150 phrases et comprend :
  - des phrases descriptives ;
  - des limites attribuées à des travaux tiers, avec les mêmes marqueurs ;
  - des restrictions volontaires de périmètre ;
  - des paires minimales appariées en fréquence lexicale.

  La grille n'est validée que si la borne supérieure de l'IC95 du taux d'étiquetage erroné est inférieure à 10 %.
- **I1** est rapporté séparément sur la strate sans marqueur.
- **Issues.**
  - A2 ou A3 non séparables : la première sous-question de l'arbitre doit être reformulée, par exemple en fusionnant « annoncé » et « ouvert ».
  - Les trois attributs séparables : l'extraction texte seul est fiable au niveau humain.

### E2' : détection des comblements (teste P6)

- **Fiche de manque.** Elle est rédigée à partir du seul texte source, **deux fois et indépendamment** (idée de E à propos de A, que je reprends). La divergence entre les deux fiches est rapportée.
- **Instrument évalué :** citations entrantes, mots-clés reformulés et restriction par date.
- **Référence : union de trois canaux.**
  1. La procédure elle-même.
  2. Un chercheur indépendant, **sans accès aux requêtes**, qui passe par d'autres canaux : sommaires d'ateliers et de conférences du domaine, dépôts de code, bancs d'essai.
  3. Une question écrite aux auteurs de l'article d'origine.

  Le rappel calculé sur l'union est une borne supérieure. Une estimation par capture-recapture est donnée à titre d'HYPOTHÈSE ; elle suppose l'indépendance des canaux, et une hétérogénéité de capturabilité la biaise.
- **Positifs.** Analyse principale : « comblé ou partiellement comblé ». Sensibilité : « comblé » seul.
- **Négatifs** (environ 120) :
  - en majorité des quasi-comblements réels : articles citants qui redisent le manque ouvert, ou qui violent un champ de la fiche ;
  - en second lieu, des manques fabriqués et des variantes à portée déplacée.
- **H_A :** rappel ≥ θ₂ (0,7) **et** fausses alertes ≤ φ₂ (0,1). **H_B :** non-H_A. La décision porte sur g = min(R − θ₂, φ₂ − FA), avec des bornes simultanées.
- **Diagnostics hors duel :**
  - part des comblements trouvés sans lien de citation ;
  - rappel stratifié par spécificité du manque (critère 5), réutilisé en E3.
- **Effectif.** On échantillonne les manques jusqu'à environ 60 positifs.

### E4' : une annonce prédit-elle l'exécution ? (sous-duel)

- **Modèle de survie.** On mesure le délai entre t₀ et l'exécution par l'équipe d'origine, avec Kaplan-Meier et un rapport de risques HR.
- **Analyse stratifiée par équipe**, sur les énoncés des deux types issus de la même équipe.
- **H_A :** HR ≥ h (1,5). **H_B :** HR < h.
- **Juge du suivi aveugle à la catégorie** de l'énoncé.
- **Placebo** (proposition de D) : chaque annonce est reliée au suivi d'un *autre* manque de la même équipe. Le HR placebo doit valoir environ 1.
- **Autre domaine :** taux de base descriptif uniquement.

### E3' : critères de choix, scindé en trois

**Socle commun à E3a et E3b.**
- Codage des critères sur les versions figées au plus tard à t₀, par des codeurs aveugles à la littérature postérieure, dates masquées.
- Le même codage est refait par des codeurs informés. Un écart d'AUC entre les deux groupes signale une fuite (idée de E).
- Le score est une somme **non pondérée, figée** avant les données.
- Le comparateur unique est le nombre de citations de l'article source.
- Un critère placebo, la longueur de la phrase du manque, doit donner une AUC d'environ 0,5.
- E3a et E3b ne sont lancées qu'avec au moins 30 positifs et 30 négatifs. En dessous, elles sont **déclarées non exécutables** à l'avance.

**E3a, affluence comme risque.**
- Issue : le manque est traité par une équipe autre que l'origine avant t₁. Cette issue est mesurée sur l'union des canaux d'E2'.
- H_A : l'AUC du score dépasse le comparateur d'au moins δ. H_B : non.
- Interprétation préenregistrée : un score élevé signale un **risque d'être doublée**. Il pénalise donc le choix.

**E3b, rendement conditionnel à une tentative.**
- Population : les manques ayant reçu au moins une tentative publique.
- Issue : la tentative est décisive, qu'il s'agisse d'un résultat positif ou d'un résultat négatif informatif.
- Même duel. Limite déclarée : les échecs silencieux ne sont pas observés (K32).

**E3p, version prospective.**
- On fige et on hache aujourd'hui les scores et le pronostic de l'équipe sur K manques candidats.
- On observe les issues à 12 mois.
- C'est la seule version sans fuite rétrospective. Elle est lente mais presque gratuite.

### E5' : le texte seul déforme-t-il les priorités ?

- Le dossier enrichi ne contient que des pièces datées au plus tard de t₀.
- **H_A :** τ(texte, enrichi) ≥ τ(texte, texte′) − m. **H_B :** τ(texte, enrichi) < τ(texte, texte′) − m. On utilise τ_b et on rapporte les ex-æquo.
- **Placebo** (proposition de D) : un dossier de pièces contemporaines sans rapport avec le manque, distribué à l'aveugle. Il ne doit pas déplacer le classement.
- **Contrôle positif** (proposition de F) : un défaut visible seulement dans le dépôt, par exemple du code cassé. Il doit déplacer le classement, sinon la procédure est insensible par construction.

### E6' : moniteur contre vérifications mécaniques (conditionnel)

- **Métrique :** gain de l'union ΔTPR = TPR(mécanique ∪ moniteur) − TPR(mécanique seul), à FPR par trajectoire apparié. Le FPR principal est de 5 % ; le point à 1 % est descriptif.
- **FPR apparié.** Un classifieur sur compteurs mécaniques est calibré au même FPR que l'union (proposition de E à propos de F).
- **H_A :** ΔTPR ≥ δ₆. **H_B :** ΔTPR < δ₆.
- **Garde a priori.** Le pilote mesure TPR_méc. Si TPR_méc > 1 − δ₆, H_A est inatteignable et l'expérience n'est pas lancée.
- **Calibration** sur un lot de tâches disjoint, en ne retenant qu'une graine par tâche pour le quantile. La vérification mécanique de référence est choisie sur ce même lot.
- **Le moniteur ne voit pas la consigne.**
- **Témoins honnêtes :**
  - consigne placebo inoffensive ;
  - échecs honnêtes naturels de même longueur ;
  - trajectoires longues avec erreurs corrigées ;
  - remplissage neutre.
- **Rapport complémentaire :** FPR par trajectoire observé, comparé à la borne 1 − (1 − p)ⁿ.

### Coût révisé (illustratif)

- L'humain passe d'environ 300 h à environ 380 à 420 h : troisième canal d'E2', négatifs réels, double fiche, double codage d'E3.
- Le calcul reste de l'ordre de 0,5 à 2,5 k$.
- E3p n'ajoute qu'environ 10 h par an.

---

## (c) Réponse à la question de l'arbitre

**Ce qui est établi.**
- La question demande une analyse publication par publication, mais **la liste est absente** (VÉRIFIÉ). Aucune affirmation ne peut donc porter sur une équipe, un manque ou une priorité particulière.
- Ce tour établit seulement des propriétés de plans, par calcul. Exemple : avec 30 négatifs, même zéro fausse alerte ne démontre pas un taux ≤ 0,10 (calcul refait par moi : borne ≈ 0,116).
- Les critiques ont aussi fait tomber des fautes de construction dans ma conception : une issue d'E3 couplée aux critères, un test de fuite inopérant, une règle vraie par définition. Je les ai retirées ou corrigées.

**Ce qui n'est pas établi** (tout est HYPOTHÈSE) :
1. Que « reconnu non fait », « annoncé » et « ouvert pour tous » soient séparables à la lecture.
2. Qu'une recherche peu coûteuse retrouve les comblements, en particulier ceux qui ne citent pas l'article d'origine.
3. Qu'une annonce prédise l'exécution par l'équipe d'origine.
4. Qu'un critère observable avant l'issue batte le comptage de citations.
5. Que le « texte seul » donne les mêmes priorités qu'un dossier enrichi.
6. Qu'un moniteur ajoute quelque chose aux vérifications mécaniques à FPR apparié.

La liste fournie ne permettra de décider, ni maintenant ni plus tard :
- les manques non déclarés ;
- le travail interne non publié ;
- les échecs silencieux et les résultats négatifs non publiés ;
- la représentativité de la liste, tant que sa règle de constitution n'est pas donnée.

**Critères proposés à l'équipe tierce** (HYPOTHÈSE, à valider par E3' et E4') :
- le manque peut être écrit en H_A, H_B et contrôle négatif ;
- il existe une vérification mécanique à battre ;
- un résultat négatif serait informatif ;
- il est faisable sur modèles ouverts ;
- son affluence prévisible est faible, puisqu'elle signale le risque d'être doublée (E3a) ;
- une recherche datée de la semaine du choix revient vide, avec trois canaux.

**L'expérience à faire en premier.**
- **Préalable :** obtenir la liste **et sa règle de constitution**.
- **Puis E1'.** Elle est presque sans calcul (environ 80 à 100 h humaines, illustratif) et conditionne tout le reste. Si A2 ou A3 n'est pas séparable, la première sous-question doit être reformulée avant toute dépense supplémentaire.
- **En parallèle, E3p.** Il faut figer et hacher dès maintenant les scores et le pronostic sur les manques candidats. C'est la seule mesure de la valeur prédictive des critères qui échappe à la fuite rétrospective, et son coût principal est le temps.

**Ce qui réfuterait ma réponse.**
- E1' falsifie H_A pour A2 ou A3 : ma grille en trois catégories est inadéquate.
- E2' falsifie H_A : la vérification peu coûteuse ne répond pas à « comment vérifier ».
- E3a, E3b et E3p ne battent pas le comptage de citations : mes critères n'ont pas de valeur prédictive.
- L'écart entre codeurs informés et codeurs aveugles est significatif : tout résultat rétrospectif d'E3 est invalide.

FIN-DE-CELLULE