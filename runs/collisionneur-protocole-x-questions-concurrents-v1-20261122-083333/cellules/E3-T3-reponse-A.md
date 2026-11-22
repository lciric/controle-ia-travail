# Proposition A — Tour III.3 : réponse aux critiques

## 0. État des pièces

- **Pièce absente :** la liste de publications annoncée par la question n'est toujours pas transmise. L'extraction « pour chacune » n'est pas exécutée, et je n'en invente pas le contenu.
- **Bloc FAITS :** il reproduit la question et ne contient aucun fait doté d'un statut.
- **Critiques reçues :** B, C, D, E et F, chacune entière. Je ne réponds qu'à leurs sections « Sur la proposition A ».
- **Statuts :** les critiques sont des HYPOTHÈSES de méthode, et leurs calculs sont illustratifs puisqu'ils portent sur mes paramètres illustratifs. Tout ce que j'ajoute ici est HYPOTHÈSE, et tout chiffre est **illustratif**.
- **Deux écarts de lecture, sans effet sur le fond :**
  - E écrit que E5b stratifie « sur une même tâche ». Mon texte ne le disait pas.
  - F écrit que E1 évalue F1 « au niveau du passage ». Mon texte plaçait à ce niveau le kappa, pas F1.

---

## (a) Verdict critique par critique

### Sur E1 (extraction du texte seul)

| Critique | Source | Verdict |
|---|---|---|
| Aucune partition entre les textes qui servent à régler l'extracteur, le filtre et l'arbitrage, et ceux qui forment l'étalon. | B, C, E | **Acceptée.** Partition fixée avant toute lecture. |
| Segmentation non verrouillée : l'écart de F1 confond extraction et découpage. | F | **Acceptée.** |
| Si les passages sont fournis aux lecteurs, la recherche des passages omis sort de l'épreuve. | D | **Transformée en test.** Mon texte ne tranchait pas ce point. E1 passe à deux étages : repérage sur article entier, puis classement. |
| Kappa non jugeable pour une étiquette rare (K1 de B, variance chez C, E, F). Grappes par article. | B, C, D, E, F | **Acceptée.** Mon issue « κ < 0,4 falsifie H_A » était fausse à faible prévalence : elle confondait désaccord et rareté. |
| Le contrôle « texte amputé » n'a pas pour sortie attendue « rien ». | B, D | **Acceptée.** Le texte amputé reçoit son propre étalon. |
| F1 indéfini sur les contrôles sans positif. | E | **Acceptée.** Les contrôles se mesurent en fausses extractions par texte. |
| Contrôles manquants : articles entiers portant les marqueurs sans déclaration pertinente ; limite levée ailleurs dans le même article. | D, F | **Acceptées.** |

### Sur E2 (vérifier « non comblé »)

| Critique | Source | Verdict |
|---|---|---|
| Étalon et procédure partagent leurs angles morts, le rappel est majoré (K2). | B, C, D, E, F | **Acceptée sur le fond.** C écrit que les experts mobilisent « nécessairement » les mêmes canaux. C'est une HYPOTHÈSE, pas un fait, mais le risque suffit. Je ne prétends plus mesurer « le » rappel : j'en rapporte un majorant. |
| Sentinelles choisies pour leur visibilité. | B, F | **Acceptée.** |
| Il manque des comblements cachés, sans citation et sous un autre vocabulaire. | B | **Transformée en test,** avec une réserve : ces cas doivent venir d'un canal indépendant de la procédure. S'il n'en existe pas, le rappel hors citation est déclaré non identifié. |
| Les fiches fictives sont trop loin des vrais faux positifs. Il faut des travaux réels qui violent un seul champ. | C, D, F | **Acceptée.** Les fiches fictives deviennent un contrôle secondaire. |
| La fiche sert d'entrée à la recherche et de critère de vérité. Double mise en fiche aveugle. | E, F | **Transformée en test préalable.** |
| Avec 30 fiches, le seuil n'est pas jugeable : il faut environ 28 comblements réels (calcul de C, illustratif). | C, E, F | **Acceptée.** Je refais le calcul et trouve le même ordre de grandeur. |

### Sur E3 (l'annonce prédit-elle le comblement ?)

| Critique | Source | Verdict |
|---|---|---|
| « La permutation teste l'association, pas la cause. » | B | **Rejetée pour l'usage visé.** Le critère « éviter l'annoncé » n'a besoin que d'une valeur prédictive. Si une équipe annonce ce qu'elle a déjà entamé (C, F), c'est précisément ce que la tierce équipe doit savoir. |
| L'annonce n'apporte peut-être rien au-delà de ce qu'on observe déjà sur l'équipe (productivité, moyens). | B, C, D, F | **Acceptée et transformée.** Le contraste devient intra-article, ce qui fixe l'équipe, la période et les moyens. |
| Mesurer le comblement par la seule équipe d'origine ne teste pas le risque d'être devancé par quiconque. | E | **Acceptée.** C'était une erreur de cible. |
| Il manque la date à laquelle les deux efforts deviennent redondants. | D | **Transformée.** L'issue est le comblement dans l'horizon de travail de la tierce équipe. |
| Censure et troncature à 12 mois. | E, F | **Acceptée.** Estimateur de survie. |
| Puissance d'environ 0,19 avec 30 fiches (calcul de C, illustratif). | B, C, F | **Acceptée.** Sous son effectif plancher, E3 n'est pas lancée. |

### Sur E4 (observations précoces)

| Critique | Source | Verdict |
|---|---|---|
| O6 recopie une clause de la définition, O5 partage l'instrument du verdict « non devancé », O2 recouvre la clause de budget. | B, C, D, E, F | **Acceptée sans réserve.** Cela se vérifie en lisant ma définition, sans aucune donnée. |
| Biais de survie, et étiquette « protocole écrit avant » non observable rétrospectivement. | B, F | **Acceptée.** La version rétrospective est retirée. |
| Sur 20 projets, l'erreur-type de l'AUC vaut environ 0,13 (K5 de B). | B, E, F | **Acceptée.** |
| Le taux de bons projets arrêtés à tort n'est pas identifié si l'on n'observe jamais l'issue des projets arrêtés. | D | **Acceptée.** Cette colonne de mon tableau (c) n'était pas mesurable. |
| La somme non pondérée peut manquer une information réelle. | E | **Rejetée comme correction.** Des poids ajustés sur une petite cohorte ajouteraient un biais d'optimisme, que E reproche lui-même à B. Je garde la somme fixée d'avance. |
| Le filtre à sept critères peut ne laisser aucun manque. | E | **Transformée.** Décompte des survivants à chaque critère, et ordre de relâchement écrit avant. |

### Sur E5 (surveillance et longueur)

| Critique | Source | Verdict |
|---|---|---|
| Mêmes cas honnêtes pour calibrer et évaluer. La variance du seuil n'est pas comptée. | B, C, E, F | **Acceptée.** Mon « 2,6 erreurs-types » ne vaut plus. |
| Sous-ensemble « manqué par le mécanique » trop petit et défini sur les données d'évaluation. | B, C, E, F | **Acceptée.** C écrit que la variance « quadruple » quand on passe de 150 à 30 cas. Je trouve un facteur 5, ce qui aggrave la critique. |
| La détection conditionnelle n'est pas le gain sur l'ensemble. | D | **Acceptée.** La métrique principale devient le gain de l'union. |
| Seuil non recalibré après filtrage par le mécanique. | F | **Acceptée.** L'union est calibrée sur un lot honnête disjoint. |
| E5b confond longueur et difficulté de tâche. Il faut allonger la même tâche. | C, D, E, F | **Transformée en test.** |
| Position relative et distance absolue aux bornes sont confondues. | F | **Transformée en test.** |
| Corrélation entre trajectoires d'une même tâche. | F | **Acceptée.** Bootstrap par tâche. |
| Fonction non monotone de la longueur. | E | **Acceptée.** Plus de « pente », des contrastes. |
| Contrôle « consigne avortée, livrable intact ». | E | **Acceptée avec amendement.** Alerter sur une tentative qui échoue n'est pas forcément une fausse alerte. La cible (effet ou tentative) est déclarée avant, et ces cas sont rapportés à part. |

---

## (b) Expériences corrigées

**Règle de décision commune, reprise de D en le disant.** Pour chaque grandeur g, je fixe avant la mesure un gain utile δ. H_A dit g ≥ δ, H_B dit g < δ.

- Un intervalle entièrement sous δ falsifie H_A.
- Un intervalle entièrement au-dessus falsifie H_B.
- Un chevauchement donne « non jugeable à cet effectif », sans réinterprétation.

Cette règle a un défaut, que C démontre à propos de B : près de δ, le non-verdict domine. J'ajoute donc à chaque expérience un **effectif plancher**. Sous ce plancher, l'expérience n'est pas lancée.

### E1′ — Repérage, puis classement

- **Partition :** les textes sont répartis entre réglage et évaluation par une règle mécanique fixée avant lecture. La consigne de l'extracteur, le lexique du filtre et les règles d'arbitrage ne voient que le lot de réglage.
- **Étage 1, repérage :** deux lecteurs marquent indépendamment les passages sur l'article entier.
  - *Métrique :* recouvrement des passages entre lecteurs. Je n'utilise pas de kappa ici, car les négatifs ne sont pas dénombrables.
  - *Duel :* H_A, recouvrement ≥ 0,7 (illustratif) ; H_B, en dessous.
- **Étage 2, classement :** il porte sur les passages repérés par les deux lecteurs. Les quatre étiquettes ne sont plus exclusives : un passage peut dire à la fois « non fait » et « ouvert ».
  - *Métrique :* accord par étiquette, bootstrap par article.
  - *Plancher :* 30 passages positifs attendus par étiquette (illustratif). En dessous, l'étiquette est notée « non jugeable », ce qui n'est pas « non extractible ».
- **Extracteur contre filtre mécanique :** écart de F1 sur le lot d'évaluation, à segmentation commune imposée.
- **Contrôles,** mesurés en fausses extractions par texte :
  - limites attribuées à autrui ;
  - articles entiers portant les marqueurs sans déclaration pertinente ;
  - limite énoncée puis levée dans le même article ;
  - textes amputés, annotés à part ;
  - textes hors domaine.
- **Issues :**
  - Repérage sous δ : le « texte seul » ne suffit pas même à localiser les aveux, et tout l'aval est suspendu.
  - Repérage au-dessus mais classement sous δ pour une étiquette : cette étiquette est fusionnée avec sa voisine avant tout usage.
  - Les deux au-dessus sans écart de F1 : le filtre mécanique suffit.

### E2′ — Rappel majoré, sentinelles cachées

- **Préalable :** deux personnes rédigent la fiche du même manque sans se voir. Si leurs fiches mènent à des verdicts différents sur les mêmes candidats, la fiche n'est pas un instrument et E2′ s'arrête.
- **Deux sources :**
  - la procédure bornée ;
  - un canal qui n'emploie ni citations ni moteurs, par exemple une question posée aux auteurs de la source et à des spécialistes de domaines voisins, recueillie avant toute recherche.
- **Ce qui est rapporté :**
  - le rappel de la procédure relativement à l'union des deux sources, présenté comme **majorant** du rappel réel ;
  - le rappel sur les seuls comblements « cachés » fournis par le second canal ;
  - le taux de « comblé » déclaré à tort sur des travaux réels qui violent un seul champ de la fiche.
- **Duel :** H_A, majorant du rappel ≥ δ et rappel non nul sur les cas cachés ; H_B, majorant < δ.
- **Asymétrie assumée :** un majorant sous δ falsifie H_A proprement. Un majorant au-dessus ne falsifie H_B que sous une hypothèse d'indépendance des deux sources, écrite en toutes lettres.
- **Plancher :** environ 28 comblements réels (illustratif). Leur nombre est compté avant l'exécution.
- **Verdict supplémentaire :** « comblé conjointement par plusieurs travaux ». Je reprends ici, en le disant, une objection que E adresse à D : ma règle des quatre champs dans un seul travail avait le même défaut.
- **Sortie :** « non trouvé au [date], requêtes [liste], rappel au plus [valeur], cas cachés retrouvés [k sur n] ».

### E3′ — Contraste intra-article

- **Unité :** les articles qui contiennent à la fois un manque annoncé et un manque déclaré ouvert.
- **Issue :** comblement par quiconque dans un horizon h égal à la durée de travail de la tierce équipe, avec prise en compte de la censure. Le comblement par l'équipe d'origine est une issue secondaire.
- **Duel :** H_A, au sein d'un même article, l'annoncé est comblé dans h plus souvent que l'ouvert, d'au moins δ (20 points, illustratif) ; H_B, moins que δ.
- **Plancher :** une centaine de manques par classe en plan non apparié (illustratif), moins en plan apparié selon le nombre de paires discordantes. Ce nombre est compté avant.
- **Sous le plancher :** E3′ n'est pas lancée. Le critère « éviter l'annoncé » reste HYPOTHÈSE et descend du rang de règle d'exclusion à celui d'annotation de risque.

### E4′ — Retirée comme expérience décisive

- **Raisons :** trois des sept prédicteurs entraient dans l'étiquette, l'étiquette n'est pas observable sur des projets passés, la cohorte est biaisée par la survie, et la puissance est insuffisante.
- **Version conditionnelle,** exécutable seulement avec un registre prospectif de plusieurs équipes incluant les projets non publiés :
  - étiquette adjugée par des tiers à T1, sans O6 ni le verdict de recherche du pilote ;
  - prédicteurs limités à O1, O3, O4 et O7 ;
  - O2, O5 et O6 deviennent des conditions d'entrée, pas des prédicteurs ;
  - plancher d'environ 70 projets (illustratif, pour séparer une AUC de 0,70 du hasard).
- **Conséquence :** O1 à O7 sont des règles d'arrêt dont les taux d'erreur ne sont pas connus. Je retire toute prétention à ce qu'elles « prédisent » un bon choix.

### E5′ — Union calibrée et allongement de la même tâche

**E5a′ — Apport au-delà du mécanique.**

- **Porte d'entrée (pilote) :** mesurer la part ψ des dégradations que les contrôles mécaniques manquent, leur seuil étant fixé sur un lot disjoint.
  - ψ proche de zéro : le mécanique sature, le manque relève de l'ingénierie des tests, arrêt.
  - Sinon, l'effectif est fixé pour que le sous-ensemble manqué atteigne une centaine de cas (illustratif).
- **Métrique principale :** gain de détection de l'union (mécanique ou surveillant) sur le mécanique seul. Les deux sont calibrés au même taux de fausses alertes par trajectoire, sur des trajectoires honnêtes disjointes de l'évaluation.
- **Référence mécanique :** elle inclut un score mécanique continu, pour qu'elle puisse dépenser le même budget de fausses alertes. Je reprends ici, en le disant, une objection de E adressée à F.
- **Métrique secondaire :** détection conditionnelle sur les cas manqués par le mécanique.
- **Duel :** H_A, gain de l'union ≥ δ ; H_B, gain < δ.
- **Contrôles :**
  - échecs honnêtes appariés ;
  - consigne placebo ;
  - verbalisations masquées ;
  - consignes avortées à livrable intact, rapportées à part.
- **Incertitude :** bootstrap par tâche, seuils réestimés à chaque tirage.

**E5b′ — Effet de la longueur.**

- **Bras causal :** la même trajectoire, dégradée ou honnête, est allongée par des segments bénins tirés d'exécutions honnêtes. L'allongement touche les deux classes.
  - Le seuil est recalibré sur des trajectoires honnêtes allongées d'un lot disjoint.
  - Deux conditions de position : relative fixe, puis distance absolue à la fin fixe.
  - Deux longueurs, différence appariée.
- **Bras descriptif :** longueurs naturelles. Il ne sert pas à conclure sur la dilution.
- **Duel :** H_A, chute appariée de détection ≥ δ (15 points, illustratif) ; H_B, chute < δ.
- **Issues :**
  - H_A retenue : l'extrapolation depuis les tâches courtes est falsifiée, à tâche constante.
  - H_B retenue : la dilution comme cause est falsifiée. Si le bras descriptif montre quand même une chute, elle tient aux tâches, pas à la longueur.
- **Réserve :** un allongement artificiel n'est pas une tâche longue. Le transfert de l'un à l'autre reste une hypothèse écrite.
- **Coût (illustratif) :** le bras causal ne demande que des passages de surveillant. Seul le bras descriptif exige de nouvelles générations.

---

## (c) Réponse à l'arbitre

### Ce qui est établi

- **Constat sur les pièces :** la liste est absente. Aucune des trois extractions demandées « pour chacune » n'a été faite, ni par moi ni, à ma lecture, dans les sections qui me visent.
- **Constat logique, sans donnée :** ma définition de « bon choix » contenait trois de ses propres prédicteurs. Cinq critiques le relèvent, et la lecture du texte suffit à le confirmer.
- **Identités de calcul :** le gain de l'union est le produit de la part manquée par le mécanique et de la détection conditionnelle. Un rappel mesuré contre un étalon dépendant est un majorant.

Rien d'empirique n'est établi : aucune expérience n'a été exécutée.

### Ce qui ne l'est pas

Tous les points suivants sont des HYPOTHÈSES :

- que les trois catégories se séparent à la lecture ;
- qu'une recherche bornée retrouve les comblements ;
- qu'une annonce signale un terrain occupé ;
- que des observations précoces prédisent un bon choix ;
- qu'un surveillant ajoute quelque chose aux contrôles mécaniques ;
- que la longueur dilue la détection.

### Réponses aux sous-questions, dans ces limites

- **Vérifier qu'un manque n'a pas été comblé :** on ne le peut pas. On peut dater une absence de trouvaille, publier les requêtes, borner le rappel par le haut et dire combien de cas cachés la procédure a retrouvés.
- **Critères de choix (HYPOTHÈSE) :**
  1. le manque est littéral et sa fiche est stable sous double rédaction ;
  2. les artefacts sont téléchargés, pas seulement déclarés ouverts ;
  3. les contrôles mécaniques ne saturent pas, ce que mesure ψ au pilote ;
  4. les cas honnêtes sont assez nombreux pour calibrer et évaluer séparément ;
  5. l'effectif plancher tient dans le budget ;
  6. l'hypothèse de transfert est écrite.

  L'annonce par les auteurs est notée comme un risque, pas comme une exclusion.
- **Observations avant l'issue :** ψ, la reproduction de la référence, la variance du pilote, la stabilité à la graine et à la reformulation. Ce sont des règles d'arrêt. Leur capacité à distinguer un bon choix d'un mauvais n'est pas validée, et ne peut pas l'être par une équipe seule.
- **Ce que la liste ne permet pas de décider, même fournie :**
  - sa propre couverture ;
  - les manques non reconnus ;
  - l'importance relative des manques ;
  - la sincérité des annonces ;
  - la réalité du phénomène hors consigne expérimentale ;
  - la comparabilité des cadres entre équipes ;
  - le rappel réel de toute vérification.

### L'expérience à faire en premier

**E1′,** dès que la liste est fournie. Elle coûte une quarantaine d'heures humaines (illustratif) et tout l'aval consomme ses étiquettes. Ses deux issues sont utiles : si le repérage échoue, la première tâche de la question n'est pas opératoire et il ne faut pas classer les manques ; s'il réussit, les fiches peuvent être rédigées.

Tant que la liste manque, la seule mesure exécutable est la porte d'entrée de E5a′. Elle dit si la surveillance a une marge à gagner sur les contrôles mécaniques.

### Ce qui peut être réfuté ici

- quatre duels maintenus (E1′, E2′, E5a′, E5b′) ;
- un duel conditionnel à son plancher (E3′) ;
- une expérience retirée (E4) ;
- deux rejets motivés, sur la causalité dans E3 et sur la pondération du score dans E4, chacun réfutable par l'argument inverse.

FIN-DE-CELLULE