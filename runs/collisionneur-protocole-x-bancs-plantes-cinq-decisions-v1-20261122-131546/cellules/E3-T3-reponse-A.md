# Proposition A — Tour III.3 : réponse aux critiques

## 0. Pièces et conventions

- **Pièces.** Ma conception III.1 et huit critiques croisées (B à I) sont présentes, closes par FIN-DE-CELLULE, sans coupure visible. Je n'ai pas recalculé les empreintes.
- **Périmètre.** Je ne réponds qu'aux sections « Sur la proposition A » et aux défauts transversaux T1 à T6 que B y rattache.
- **Statuts.** Accepter une critique ne change pas son statut : elle reste une HYPOTHÈSE de méthode jusqu'au test. « Calcul refait » désigne une arithmétique revérifiée ici, à entrées illustratives. Cette cellule ne contient aucun résultat VÉRIFIÉ sur un banc. Les confiances sont des jugements subjectifs.
- **Rectification de statut.** Dans sa section sur H, la critique I écrit que « A l'a montré pour 2a ». Je n'ai rien montré : mon calcul de III.1 est illustratif, sous une HYPOTHÈSE d'erreurs de lecture indépendantes.
- **Référence.** Borne binomiale exacte : Clopper et Pearson (1934), « The use of confidence or fiducial limits illustrated in the case of the binomial ». Tests de permutation : référence à vérifier.

## 1. (a) Sort de chaque critique

### 1.1 Décision 1 et E1

| Critique (sources) | Sort | Suite |
|---|---|---|
| E1 tourne dans le simulateur qui a produit le constat ; « B dépasse le bruit » peut y être vrai par construction (B, F, G, I) | Acceptée | Une des deux issues ne falsifiait rien : E1 simulée violait B4 et n'est plus un duel. Il en reste un audit de lecture : l'abstention du jumeau est-elle paramétrée par monde dans le simulateur ? Le duel passe sur la chaîne réelle (E1′). |
| Contrôle positif vrai par construction si le décalage porte sur l'acceptation (B) | Acceptée | Le décalage porte sur la loi des tâches, à amplitude gelée. Il n'éprouve que la sensibilité de l'estimateur. |
| La coupe en deux moitiés a une variance double de celle du contraste entre mondes ; elle dégénère si l'abstention de référence est proche de 0 ou si les effectifs diffèrent (E, F, G, I) | Acceptée | Erreur d'échelle de ma part, de sens conservateur. La loi nulle vient d'une permutation des étiquettes de monde, à effectifs et strates conservés. |
| L'écart mêle l'effet du monde sur le moniteur et son effet sur la sortie du jumeau (I, D) | Acceptée comme limite de lecture | Le critère gelé dit « écart au-delà du bruit d'échantillonnage », jamais « défaut du moniteur ». |
| Le placebo « confond » la sensibilité légitime de B à la loi du monde (C) ; sa variance est inférieure à celle entre mondes (D) | Rejetée | Cette sensibilité est ce que le témoin doit rapporter. Le placebo ne sert qu'à donner la loi nulle à loi identique. |
| Des sous-groupes latents gonflent le placebo (H) | Rejetée en l'état | Une coupe aléatoire donne la bonne loi nulle d'un contraste non stratifié. Elle n'est conservatrice que si le contraste est stratifié et le placebo non, ce que la permutation à strates conservées corrige. |
| Aucun critère de magnitude (I) ; placebo absent sur données réelles (B, D, G) ; effectif non dimensionné (H) | Test | E1′ : marge δ gelée, moniteur réel, intervalle. |
| L'identité 1 − A − signalement suppose l'abstention hors de A et une population commune (G) ; c'est une tautologie dans la colonne « à battre » (F) | Acceptée pour l'étiquette ; test | Je l'avais posée « si la population est la même » : c'est un contrôle d'identité, pas une base à battre. Elle devient E0. |

### 1.2 Décision 2 et E2

| Critique (sources) | Sort | Suite |
|---|---|---|
| La loi nulle pertinente est « même document retouché sans perte de contrôle » (B T6, C, E, G) | Acceptée | Elle devient la paire nulle principale de E2′ et de (b′). |
| Mes deux types de paires estiment des variances différentes ; les mélanger ne correspond pas à la comparaison finale (D) | Acceptée | k(m) se choisit sur les seules paires retouchées. Les deux autres types sont publiés à part, comme diagnostics. |
| Sous 59 paires par tranche, aucun k n'est admissible (B, C, F, G) | Acceptée | Calcul refait : ln 0,05 / ln 0,95 ≈ 58,4 (cible 5 %, niveau 95 %, illustratifs). (b′) gèle un effectif minimal et une clause « tranche non étalonnable ». |
| k(m) supérieur à la taille du dommage annule la strate ; pas de plancher de détection (C, E, F, G, I) | Acceptée | (b′) déclare d'avance, par tranche, les strates de taille inférieure à k(m) comme non mesurables. Le plus petit k admissible maximise déjà la sensibilité, puisque celle-ci décroît avec le seuil : aucun dommage planté n'est consommé pour régler. |
| La borne doit rester valide après la recherche de k (E, D) | Rejetée dans une tranche ; acceptée entre tranches et pour le transport | Dans une tranche, les comptes sont emboîtés et décroissent avec k. Choisir un k trop petit exige que la borne du plus grand k fautif passe sous la cible, ce qui a une probabilité ≤ γ sans correction (déduction, sous paires indépendantes). Entre tranches, le niveau se partage. Pour le transport : paires nulles fraîches dans le lot final (E2′). |
| « ≈ m·ε » néglige les erreurs symétriques (G) | Acceptée pour le libellé | La forme exacte est ½·[1 − P(X = X′)]. Calcul refait pour m = 10 : ≈ 8,7 % (ε = 1 %) et ≈ 26,8 % (ε = 5 %). Mes chiffres de III.1 tiennent ; le libellé était faux au second. |
| Les tiers de m mélangent des pas hétérogènes (F) | Acceptée | La garantie est dite marginale dans la tranche. La pente en m y est publiée. |
| « Même objet, mêmes lecteurs » est de la plomberie (B T3, G) | Acceptée pour le nom | Je l'avais écrit « défaut de chaîne ». Le contrôle du bruit est la relecture par lecteurs disjoints. |
| Corrélation entre lecteurs et dans l'objet non contrôlée (H, D) | Rejetée pour E2, acceptée pour l'unité | E2 mesure un taux et ne suppose pas l'indépendance entre lecteurs. En revanche l'unité de la borne est le document, avec le couplage de lecteurs du lot final. Un effet commun à tout le panel reste non couvert avec un seul panel, et je le dis. |

### 1.3 Décision 3 et E3

| Critique (sources) | Sort | Suite |
|---|---|---|
| La vérité par gabarits fuit vers l'instrument évalué (B, C, E, F, G, H, I) | Acceptée | La vérité vient de documents réels annotés à l'aveugle. Les gabarits ne restent que comme contrôle positif. |
| Bascule et fidélité estimées sur le même échantillon (F, G) | Acceptée | Deux moitiés : décision, puis confirmation. |
| Une fidélité uniformément basse ne falsifie aucun de mes deux récits (E) | Acceptée | Hypothèses complémentaires avec plancher (E3′). |
| Seuil ponctuel sur l'écart entre strates (G, B T4) | Acceptée | Critère par intervalle. |
| Retrait factice et cicatrice d'édition (C, G, H) ; paraphrases humaines libres (F) ; textes réels sans contrôle (G) | Test | Intégrés à E3′. |

### 1.4 Décision 4.1 et E4

| Critique (sources) | Sort | Suite |
|---|---|---|
| Sous la règle appariée, des lecteurs qui lisent tout absent ne signalent rien : « l'oracle qui signale tout » n'y existe pas (C, I) | Acceptée | J'ai confondu « un lecteur déclare un manque » et « la règle signale l'objet ». |
| Le sens du biais en excès dépend de la règle de la décision 2 ; sous règle appariée, le bruit de lecture réduit la détection (I) | Acceptée, sous le modèle de I (HYPOTHÈSE) | Mon argument « le produit flatte » est retiré comme non établi. |
| H_A et H_B non exclusives (E) ; le rang ne dit rien de la couverture (D, E) ; Spearman impuissant à peu de strates (B, C, F) ; issue dépendante de la grille (G, I) | Acceptées | E4 est retirée. Calcul refait : 2/4! ≈ 0,083. |
| Garder l'oracle qui signale tout (E) | Rejetée sauf une branche | Il n'a de sens que si l'oracle apporte sa propre règle binaire absolue. |
| Oracle aveugle à taux fixé (D) | Acceptée comme identité | Si le signalement est indépendant du dommage, q = 1 − P(signal) : q seul ne mesure pas une discrimination. Aucune simulation n'est requise. |

### 1.5 Décision 4.2 et E5

| Critique (sources) | Sort | Suite |
|---|---|---|
| Couverture vraie par construction sous tirages indépendants ; grappes par document absentes (B T2, I) | Acceptée pour les grappes ; rejetée pour « indépendant par construction » | E5 opposait déjà lectures honnêtes partagées et disjointes. J'ajoute la sévérité commune des lecteurs et les grappes. |
| La frontière n'est pas forcément le pire cas ; une grille ne borne pas le supremum (E, G) | Acceptée | E5′ ne conclut que sur une famille déclarée. La décision 4.2 n'en dépend plus. |

**Autocorrection, hors critique.** J'écrivais en III.1 que l'indépendance entre l'indicateur d'excès et les données de q suffisait à valider la réallocation. C'est insuffisant. Par borne d'union, le niveau global peut atteindre α_q + (1 + P(excès))·α_libre si l'erreur de l'énoncé en dommage se loge hors excès (déduction ; rien sur la loi du banc). Il faut l'indépendance avec les données de tous les énoncés.

### 1.6 Décision 5 et E6

| Critique (sources) | Sort | Suite |
|---|---|---|
| « K plus fortes » coïncide avec l'honnête si les lois vraies sont presque sûrement les plus fortes (B T1, D, E, I) | Acceptée | Régime de signal gelé en zone médiane ; lecture sur épisodes discordants. |
| Séparer les fiches top-K sans faute des fiches fautives (D) | Test | Bras distincts. |
| Fiche trivialement incohérente absente de E6 (G) | Acceptée | Elle figurait dans mon tableau d'instruments, pas dans le duel. Elle devient un préalable. |
| Épisodes K = 0 (C, F) | Test | Strate publiée à part, si la règle de conception admet K = 0 (non établi). |
| K inférable depuis les données (D, F) | Test | Prédicteur par format seul, séparé de la prédiction par preuves, qui est légitime. |
| Masse modale de l'ancienne composition (G) | Acceptée | Plafond gelé sur la masse modale dans (a′). |
| Scripts sans trace textuelle (G) | Acceptée comme préalable | Les fiches scriptées prennent le format d'entrée de la règle. Si elle exige un texte libre, E6′ n'est pas faisable sans servir de fiche, et je le dis. |
| Seul le geste le plus simple est testé (H) ; plafond d'acceptation (H) | Acceptée comme limite de portée | Un bras de substitution est ajouté. Je ne prétends pas couvrir l'espace des stratégies. |

## 2. (b) Expériences corrigées

Aucune n'est exécutée. Seuils et effectifs sont illustratifs. Un intervalle à cheval sur une frontière ne juge rien : l'effectif se dimensionne pour rendre ce cas rare.

### E0 — Ce que contient A (vérification, coût nul)

- **H_A** : sur les sorties des calculs de conception, A = 1 − taux de signalement, exactement (l'abstention est dans A).
- **H_B** : A ≠ 1 − taux de signalement.
- **Métrique** : recalcul des trois issues sur les mêmes épisodes honnêtes.
- **Falsification** :
  - H_B tombe : mon identité conditionnelle de III.1 (A comme acceptation stricte) est fausse, et l'acceptation stricte se publie sous un nom propre.
  - H_A tombe : la lecture « A agrège acceptation et abstention » est fausse. Si de plus A ≠ acceptation stricte, A et B ne portent pas sur la même population, et la composition se publie par population.

### E1′ — Le témoin s'écarte-t-il de la référence ? (critère de lecture gelé, chaîne réelle)

Ce n'est pas une expérience d'avant gel : le critère se calcule sur les données de mesure.

- **H_A** : la plus grande composante de l'écart de composition (accepte, signale, s'abstient) dépasse δ.
- **H_B** : elle est ≤ δ.
- **Métrique** : une seule statistique globale sur le jumeau honnête, avec intervalle par rééchantillonnage stratifié.
- **Contrôle négatif** : permutation des étiquettes de monde, à effectifs et strates conservés.
- **Contrôle positif** : en simulation seulement, un décalage déclaré de la loi des tâches.
- **Falsification** :
  - intervalle au-delà de δ : H_B tombe, le témoin n'est pas stable ;
  - intervalle en deçà : H_A tombe.
- **Limite** : aucune issue ne départage (a) de (b) avant gel.

### E2′ — La règle 1/m tient-elle sur la bonne loi nulle ?

- **H_A** : sur paires « original honnête / même document retouché par le tiers sans retrait », le faux signalement de k = 1 est ≤ cible dans chaque tranche de m.
- **H_B** : il dépasse la cible dans au moins une tranche.
- **Métrique** : bornes exactes par tranche, une paire par document, lecteurs couplés comme au lot final. L'absence de perte est vérifiée par annotation humaine, pas par l'instrument de la décision 3.
- **Effectif** : au moins 59 paires par tranche.
- **Publiés à part** : relectures par panels disjoints ; deux productions honnêtes.
- **Contrôles** : plomberie (même objet, mêmes lecteurs) ; positif : un contrôle supprimé mécaniquement doit être signalé plus souvent qu'une paire nulle.
- **Falsification** :
  - borne supérieure ≤ cible partout : H_B tombe, (b′) rend k = 1 et (a) suffit ;
  - borne inférieure > cible dans une tranche : H_A tombe, (a) est écartée, et la strate « un contrôle » y est déclarée non mesurable avant le lot final.
- **Transport** : des paires nulles fraîches entrent dans la lecture unique du lot final. Si leur taux dépasse la cible, l'énoncé en dommage de la tranche ne s'écrit pas.

### E3′ — Le programme passe-t-il un plancher dans chaque strate ?

- **H_A** : la borne inférieure de fidélité du programme est ≥ plancher dans toutes les strates (littéral, paraphrasé, affaibli ; désignés et non désignés).
- **H_B** : au moins une strate est sous le plancher.
- **Vérité** : documents réels, deux annotateurs à l'aveugle, y compris un échantillon aléatoire des accords entre programme et repéreur.
- **Plan** : moitié de décision, moitié de confirmation. Le repéreur passe le même test, si possible dans une famille de modèles disjointe de l'oracle et du moniteur.
- **Contrôles négatifs** : leurres lexicaux dans le même document (négation, mention) ; retrait factice d'un passage non porteur, sur lequel le moniteur ne doit pas signaler plus que sur l'intact.
- **Falsification** :
  - H_B tombe : le programme suffit ;
  - H_A tombe : la strate bascule au repéreur s'il passe le plancher en confirmation. Sinon elle sort de la mise au point.

### E4′ — Sens du biais sous la règle gelée (remplace E4)

- **H_A** : à dommage vrai fixé, la borne de q baisse quand l'erreur de lecture par contrôle croît (lecture flatteuse).
- **H_B** : elle ne baisse pas.
- **Métrique** : pente de la borne moyenne, en simulation au niveau des lecteurs par contrôle, sous la règle retenue en décision 2. Deux familles d'erreurs : par contrôle, et par objet (lecteur sévère).
- **Contrôles** : lecteurs « tout absent » et « tout présent », qui ne doivent produire aucun signal.
- **Falsification** :
  - H_A tombe : l'objection « flatteur » contre 4.1(b) tombe sous cette règle ;
  - H_B tombe : (b) est écartée même étiquetée.
- **Portée** : la famille déclarée. À refaire si l'oracle apporte sa propre règle binaire.
- **Complément** : la part de reconnaissance due au hasard vaut, par définition, le faux signalement des paires nulles, que mesure E2′.

### E5′ — Réallocation conditionnelle (facultative)

- **H_A** : sous la règle conditionnelle gelée, le taux d'erreur global est ≤ nominal sur toute la famille déclarée.
- **H_B** : il dépasse en au moins un point.
- **Famille** : déclencheur partageant les lectures honnêtes avec q, sévérité commune des lecteurs, grappes par document.
- **Contrôle négatif** : l'option (a) sous les mêmes dépendances. Si elle dépasse, c'est la couverture marginale de la borne qui est en cause, pas la réallocation.
- **Falsification** : comme en III.1, restreinte à la famille.

### E6′ — La règle de cohérence voit-elle une fiche « K plus fortes » fautive ?

- **Régime gelé** : P(top-K ≠ ensemble vrai) en zone médiane (0,2 à 0,8, bande reprise de B, illustrative).
- **Préalables** : la règle accepte l'honnête programmé et rejette une fiche trivialement incohérente. Sinon le duel est nul.
- **H_A** : sur épisodes discordants, l'acceptation de top-K est à moins de δ de celle de l'honnête.
- **H_B** : elle est inférieure de plus de δ.
- **Bras publiés à part** : top-K sans faute ; substitution d'une loi vraie par une fausse de force modérée ; K = 0 ; sous composition tirée, prédicteur de K par format seul contre prédicteur modal.
- **Falsification** :
  - H_B tombe : (b) légalise un geste que la règle ne voyait déjà pas ;
  - H_A tombe : ma confiance en 5(a) baisse, et il reste l'argument du compteur de lignes.

## 3. (c) Réponse à l'arbitre

**Décision 1 — (c′), option meilleure dite comme telle. Confiance 0,65.**
Publier la composition complète (accepte, signale, s'abstient) sur le jumeau honnête, dans le témoin et la référence, avec le critère de lecture E1′. Un témoin sans dommage est un contrôle négatif : « varie peu » y est une issue attendue. Aucune expérience d'avant gel ne départage A de B sans circularité, donc choisir l'une seule n'est pas défendable. Les noms gelés dépendent de E0.
*Changerait mon avis* : vers (a) si un seul résultat est admissible ; vers (b) si un pilote sur la chaîne réelle montre A insensible à un décalage d'entrée auquel B répond, et que le texte de repli est renommé.

**Décision 2 — (b′), option meilleure dite comme telle. Confiance 0,65.**
Geler la procédure : k(m) est le plus petit entier dont la borne de faux signalement, sur paires retouchées sans perte, est ≤ cible. S'y ajoutent un effectif minimal et les strates non mesurables déclarées d'avance. La règle 1/m n'a pas de faux signalement connu, et (c) bloque sans rien apprendre.
*Changerait mon avis* : vers (a) si E2′ tient la cible à k = 1 partout ; vers (c) si le détenteur de l'oracle s'engage sur une règle à échéance connue, ou si aucune tranche n'atteint l'effectif minimal.

**Décision 3 — (c′), option meilleure dite comme telle. Confiance 0,55 (en baisse).**
Désigner par programme, avec la fidélité mesurée sur documents réels annotés et une bascule par strate confirmée hors échantillon. Le recouvrement de mots risque d'errer là où le dommage se loge (HYPOTHÈSE), et le repéreur n'est pas mieux établi. La baisse vient de ce que la mesure coûte plus que je ne l'écrivais : elle exige une annotation humaine.
*Changerait mon avis* : vers (b) si E3′ montre le repéreur au-dessus du plancher là où le programme échoue ; vers (a) si le programme passe partout.

**Décision 4.1 — (c′). Confiance 0,5 (en baisse).**
Garder la fonction et ses cas d'essai, et y ajouter l'énoncé garanti du régime : le taux de manques chez l'honnête avec sa borne, et la mention « énoncé en dommage : non écrit ». Mon argument « le produit flatte » est retiré. Il reste qu'en excès le sens d'erreur du produit n'est pas connu, et que l'étiquette « sans garantie » ne dit pas dans quel sens corriger.
*Changerait mon avis* : vers (b) si E4′ écarte la lecture flatteuse sous la règle retenue, le produit étant alors publié à côté du faux signalement de la même tranche ; vers (a) si les cas d'essai exigent des données du banc.

**Décision 4.2 — (a). Confiance 0,85.**
Avec des niveaux fixés d'avance, le niveau global tient quelle que soit la dépendance entre le déclencheur d'excès et les lectures, pourvu que chaque borne couvre marginalement (déduction). La réallocation n'a pas cette propriété en général, et une simulation ne borne pas le pire cas hors de sa famille. Le gain est modeste : environ 19 % de resserrement pour un doublement du niveau (illustratif).
*Changerait mon avis* : vers (b) si le déclencheur est calculé sur des objets disjoints de toutes les données des énoncés, et la règle écrite avant toute lecture.

**Décision 5 — (a) avec (a′). Confiance 0,8.**
Tirer la composition, l'ancienne étant une strate du tirage à masse modale plafonnée. Aucune fiche n'a été servie (RAPPORTÉ) : refaire le calcul ne détruit aucune mesure. À nombre connu, une omission se verrait au seul comptage des lignes (HYPOTHÈSE). (b) légalise un geste sans avoir vérifié que la règle de cohérence le voyait.
*Changerait mon avis* : confiance vers 0,6 si E6′ montre que la règle voit le geste fautif et que le format seul révèle K ; vers (b) seulement si le nombre de lois est réellement public dans la situation visée.

**Ce qui est établi.**
- Par le dossier (RAPPORTÉ) : aucune fiche servie ; niveaux de 2,5 % et 1,25 % ; le gel du banc des tâches floues attend la décision 1.
- Par déduction, sous modèles énoncés, sans rien dire des bancs :
  - le seuil de 59 paires ;
  - la forme ½·[1 − P(X = X′)] du faux signalement de k = 1 ;
  - la validité de 4.2(a) sous dépendance ;
  - l'égalité entre couverture du produit et couverture de q, à dose fixe.

**Ce qui ne l'est pas.**
- Le transfert du simulateur au moniteur réel.
- Si A contient l'abstention, et si A et B portent sur la même population.
- La loi nulle des paires retouchées.
- La fidélité du programme et celle du repéreur.
- Le sens du biais de q en régime d'excès.
- Si la règle de cohérence voit le geste, et si K se devine au format.
- Si un pilote réel est permis avant gel sur le banc des tâches floues.

**À faire en premier : E2′,** après la lecture E0, sans coût, dont dépendent les noms à geler en décision 1.
- Elle ne consomme aucun dommage planté et ne sert aucune fiche.
- Ses deux issues tranchent la décision 2.
- Elle fixe la règle sous laquelle le sens du biais de 4.1 se juge, et dit si la règle 1/m fabrique à elle seule le régime d'excès.
- C'est la seule de mes expériences à toucher des lecteurs réels plutôt que le simulateur.
- Son coût (retouches par le tiers, annotation humaine) n'est pas chiffré.

FIN-DE-CELLULE