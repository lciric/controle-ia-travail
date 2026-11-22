# Proposition B — Tour III.3 : réponse aux critiques

**État des pièces.** Ma conception III.1 et les critiques A, C, D, E et F sont présentes et closes par leur marqueur. FAITS reproduit la QUESTION et ne contient aucun fait empirique. Je n'ai pas recalculé les empreintes (OBSERVÉ-NON-AUDITÉ).

**Conventions.**
- Les objections sont citées par la lettre de leur auteur. Leurs statuts (HYPOTHÈSE pour la plupart, VÉRIFIÉ pour certains calculs de C) restent ceux que leurs auteurs leur ont donnés, et je ne m'appuie pas sur les références que C cite.
- Quelques bornes ont été recalculées par moi. Elles sont marquées « recalcul B, non audité » : modèle binomial indépendant, statut OBSERVÉ-NON-AUDITÉ.
- Tout chiffre est **illustratif**.

---

## (a) Décision sur chaque critique visant B

### E1 : la divulgation renseigne-t-elle l'adversaire ?

| # | Critique (source) | Décision | Raison ou test |
|---|---|---|---|
| 1.1 | H_B (« aucune information ») est tranchée par le seuil de 10 points (A). | **Acceptée** | H_A : Δ ≥ δ ; H_B : Δ < δ. Les deux hypothèses deviennent complémentaires autour d'une marge unique, et le mot « aucune » est retiré. |
| 1.2 | Le contrôle positif C2 ne sépare pas un adversaire faible d'un détecteur robuste (A). | **Acceptée** | Je reprends l'idée de E, transmise par A, en le disant : un **détecteur factice connu fragile** sert d'étalon de l'adversaire. C2 devient une condition mesurée, plus un contrôle. |
| 1.3 | Pas de contrainte d'utilité ; en C0, l'adversaire ignore peut-être qu'un détecteur existe (A). | **Acceptée** | L'issue devient conjointe : « évadé **et** utile ». L'utilité est mesurée sur toutes les tentatives, sans filtrage. On évite ainsi le biais de filtrage après traitement reproché à E. Toutes les conditions annoncent qu'un détecteur existe. |
| 1.4 | Le bootstrap porte sur les tentatives ; il n'y a que 5 humains par bras et 3 modèles (A, C, E, F). | **Acceptée** | Pour les agents, l'inférence se fait par modèle. Elle est conditionnelle et déclarée comme telle : aucune généralisation à d'autres modèles. Pour les humains, l'unité est le participant et le volet est exploratoire tant que l'effectif calculé n'est pas atteint. |
| 1.5 | Le critère « l'intervalle C0→C1p inclut 0 » confond non-significativité et absence d'effet, et il pénalise les grands échantillons (A, F). Le contraste principal se fait contre l'absence de texte (D). | **Acceptée** | Le contraste principal devient **C1 − C1p**. |
| 1.6 | Le placebo C1p, qui décrit un détecteur sans rapport, est une fausse piste (E, F). | **Transformée en test** | Duel E1b, avec un placebo neutre C1n. |
| 1.7 | Conditionner l'interprétation à la baisse C0→C2 biaise la baisse C0→C1, car C0 est commun aux deux (E). | **Acceptée** | Le contrôle positif porte désormais sur un autre détecteur, estimé indépendamment. |
| 1.8 | Le seuil τ n'est pas fixé sur un lot disjoint (F). | **Acceptée** | Un lot honnête sert à calibrer τ, un autre sert au test. Le taux de fausses alertes est rapporté hors échantillon. |
| 1.9 | Effet plancher : le test est impossible si le TPR en C0 est inférieur à δ (A, F). | **Acceptée** | Prérequis vérifié sur un pilote disjoint. |
| 1.10 | Les résultats ne se transportent pas d'une source à l'autre (D). | **Acceptée en partie** | Standardisation par strate de source. Le transport vers la cible réelle n'est pas revendiqué. |
| 1.11 | Ajouter un placebo de même longueur que C2 (F). | **Acceptée, en secondaire** | Exécuté seulement si le budget le permet. |

### E2 : des systèmes ingèrent-ils le texte public ?

| # | Critique (source) | Décision | Raison ou test |
|---|---|---|---|
| 2.1 | La loi des requêtes est fixée par l'expérimentateur ; la restitution à la demande n'est pas l'exposition pendant la mesure réelle (A, D). | **Acceptée** | Deux métriques : la restitution sur requête ciblée, et l'exposition *in situ* (requêtes de la tâche réelle, sans indice de canari). |
| 2.2 | Le rappel littéral n'est pas la fuite pertinente, qui est sémantique (A). | **Rejetée en partie** | La fuite d'**instances** (les éléments secrets eux-mêmes) est l'un des deux mécanismes visés, et le rappel littéral est la bonne mesure pour elle. Pour la fuite de méthode, j'accepte : des canaris sémantiques sont ajoutés. |
| 2.3 | Les requêtes hebdomadaires provoquent elles-mêmes l'indexation (C). | **Transformée en test** | Duel E2b. Le mécanisme reste une HYPOTHÈSE de C. |
| 2.4 | Recalibrer sur les canaris négatifs, puis annoncer la spécificité sur ces mêmes canaris, est circulaire (D, F). | **Acceptée** | Les canaris négatifs sont scindés en un lot de calibration et un lot de validation. |
| 2.5 | Un serveur minimal ne représente pas le lieu de prépublication (A, E, F). | **Acceptée en partie, rejetée en partie** | Je **refuse** de déposer des prépublications fictives sur un serveur scientifique : cela pollue le registre, et les politiques des serveurs sont à vérifier. J'utilise un hôte d'autorité comparable, avec des pages étiquetées comme tests et des témoins `noindex` (idée de F). La non-transportabilité au lieu réel est déclarée. |
| 2.6 | Avec un seul texte leurre, la probabilité d'indexation et celle de restitution ne sont pas identifiables (F). | **Acceptée** | L pages distinctes. Unité d'indexation : la page. Unité de restitution : le canari. |
| 2.7 | Puissance : il faut K ≥ 72 canaris pour qu'une borne passe sous 5 % (A), et K ≈ 286 si le taux de fausses alertes vaut 0,02 (C). | **Transformée** | K est fixé **après** avoir mesuré le taux de fausses alertes sur le lot de validation. J'ai recalculé les deux bornes et trouvé 72 et 286 (recalcul B, non audité). |

### E3 : le drapeau dissuade-t-il ou attire-t-il les concurrents ?

| # | Critique (source) | Décision | Raison ou test |
|---|---|---|---|
| 3.1 | Temps immortel et sélection sur l'issue : les questions sans drapeau n'ont pas d'origine temporelle (A, C, D, E, F). | **Acceptée** | Refonte complète, voir E3′. |
| 3.2 | Les annotateurs reconnaissent plus facilement « la même question » quand un drapeau la formule (A, F). | **Acceptée** | Un texte de référence commun aux deux bras remplace le drapeau dans l'annotation. |
| 3.3 | La publication de l'équipe termine aussi la course, et les risques peuvent ne pas être proportionnels (D, E, F). | **Acceptée** | L'estimande devient l'incidence cumulée du devancement à un horizon h, en risques concurrents. Le rapport de risques de Cox est abandonné. |
| 3.4 | Causalité inverse et confusion latente : on pose un drapeau parce que la question est déjà « chaude » (C, E, F). | **Acceptée, non résolue** | Contrôle de tendance avant le repère. E3′ ne peut **pas**, à lui seul, déclencher une bascule de mon choix. |
| 3.5 | Le contrôle « autre question du même champ » ne contrôle pas le choix des sous-questions chaudes (C, E). | **Acceptée** | Il est gardé comme diagnostic, pas comme garantie. |
| 3.6 | La vignette mesure une intention, pas un comportement (D). | **Déjà déclaré** | Pas de modification. |

### E4 : le texte protège-t-il la reconnaissance ?

| # | Critique (source) | Décision | Raison ou test |
|---|---|---|---|
| 4.1 | Le bras « absence de pièce » sert au seuil mais manque à la liste (D, E, F). | **Acceptée** | Erreur de ma conception : le bras est ajouté. |
| 4.2 | Avec 20 à 40 juges par bras, la demi-largeur dépasse 15 points (C). | **Acceptée** | Effectifs recalculés, voir E4′. |
| 4.3 | Conclure à l'équivalence empreinte / drapeau exige une marge préspécifiée (F). | **Acceptée** | Marge d'équivalence fixée à l'avance. |
| 4.4 | Variance entre dossiers (point adressé par C à D). | **Reprise, en le disant** | Plusieurs dossiers par condition. |

### E5 : le bénéfice qualité vient-il de la publicité ou de l'engagement ?

| # | Critique (source) | Décision | Raison ou test |
|---|---|---|---|
| 5.1 | Publicité, recrutement et temps de lecture sont confondus : P(trouvé) = P(lu) × P(trouvé \| lu) (A, D). | **Transformée** | E5 est scindé en E5a (portée) et E5b (compétence sachant la lecture). |
| 5.2 | Le canal public peut rester muet : loi gonflée en zéro (A, C, E, F). | **Acceptée** | Un canal muet **invalide** l'essai ; il ne falsifie plus H_A. |
| 5.3 | Les défauts implantés sont de classes connues de ceux qui conçoivent l'audit (A). | **Acceptée** | Implantation par un tiers, avec une réserve de classes de défauts montrée à personne d'autre. |
| 5.4 | Des protocoles fictifs n'ont ni notoriété ni crédibilité (F). | **Acceptée comme limite** | La portée est estimée sur des données observationnelles. |
| 5.5 | Les auditeurs internes savent que les protocoles sont fictifs (F). | **Acceptée** | Ils sont tenus aveugles à ce caractère. |
| 5.6 | Saillance stylistique des défauts implantés (point adressé par C à A). | **Reprise, en le disant** | Contrôle par modifications de surface neutres. |

### E6 : test de fuite intégré à l'étude réelle

| # | Critique (source) | Décision | Raison ou test |
|---|---|---|---|
| 6.1 | Les deux moitiés sortent du même procédé : une fuite du procédé les touche également, et l'écart attendu est nul (A, C, D, E, F). | **Acceptée** | C'est le défaut le plus grave de ma conception. E6 ne justifiait pas la clause « la moitié après publication » de mon choix. |
| 6.2 | L'écart avant / après confond une fuite interne du stock « avant » et la dérive temporelle (C, D). | **Acceptée** | E6 est reformulée en test de S10 (fuite interne), avec assignation tirée au sort. |
| 6.3 | Il faut environ 1 291 éléments par sous-groupe (C). | **Acceptée** | Recalcul concordant (recalcul B, non audité). L'effet minimal détectable est déclaré. |

### Instruments

| # | Critique (source) | Décision | Raison ou test |
|---|---|---|---|
| I1 | Exiger de battre les lignes de base en C0, C1 **et** C2 exclut un détecteur valide seulement sous secret, régime que la question envisage (F). | **Acceptée** | Ma conception se contredisait sur ce point. Deux étiquettes séparées : « fonctionne sous secret » et « robuste au niveau de divulgation k ». |
| I3 | Fuite entre la calibration et l'évaluation (D, F). | **Acceptée** | Même correction que 2.4. |
| I4 | Circularité : la vérité vient d'un modèle publié, que les auditeurs peuvent appliquer par identité (A, C, D, E, F). | **Acceptée** | L'instrument est rétrogradé, voir (b). |
| I4′ | Si le bruit d'issue tend vers 0, la règle de l'issue devient parfaite et il n'y a plus de marge à battre (F). | **Acceptée** | Le niveau de bruit est fixé et déclaré, et une marge non nulle est exigée. |

---

## (b) Expériences corrigées

Règle commune, reprise de D en le disant :
- deux hypothèses complémentaires autour d'une marge préspécifiée ;
- un intervalle entièrement dans une région falsifie l'autre hypothèse ;
- un intervalle qui chevauche la marge est **inconcluant** et n'est pas présenté comme un résultat.

### E1′ : information apportée à l'adversaire (inclut E6b)

**Conditions** (chaque adversaire est informé qu'un détecteur existe) :
- C0 : aucun texte ;
- C1 : le texte court réel ;
- C1p : un placebo décrivant un détecteur sans rapport ;
- C1n : un résumé neutre du domaine, sans aucun détecteur ;
- C2 : la méthode complète ;
- C2p : un placebo de même longueur que C2 (secondaire).

**Contrôle positif indépendant** : un détecteur factice fragile, décrit à l'adversaire au niveau du principe. Il doit perdre au moins δ de TPR. Sinon, l'adversaire est déclaré trop faible et E1′ est ininterprétable.

**Métrique** :
- *Issue « évadé et utile »* : l'utilité est jugée en aveugle sur **toutes** les tentatives.
- *TPR* : mesuré au seuil τ, gelé sur un lot honnête de calibration de taille suffisante pour que α·n soit au moins 10 (soit 1 000 cas pour α = 1 %, illustratif). Le taux de fausses alertes est rapporté sur un second lot honnête.

**Duel principal** : Δ = taux de succès en C1 − taux de succès en C1p.
- H_A : Δ ≥ δ (δ = 10 points, illustratif). H_B : Δ < δ.
- Intervalle entièrement au-dessus de δ : H_B falsifiée. Intervalle entièrement au-dessous de δ : H_A falsifiée.

**E1b (diversion)** : on compare C1p et C1n.
- H_A : le placebo C1p relève le TPR d'au moins δ′ par rapport à C1n. H_B : il ne le relève pas de δ′.
- Si H_B est falsifiée, C1n remplace C1p comme comparateur principal.

**E6b (fuite de procédé)** : les éléments secrets sont tirés de deux familles.
- F_v est la famille dont le procédé est concerné par le texte. F_o est une famille orthogonale, qu'aucun texte ne décrit ni n'implique.
- Statistique : (baisse sur F_v − baisse sur F_o) entre C0 et C1.
- H_A : cette double différence est au moins δ. H_B : elle est inférieure à δ.
- Contrôle positif : un bras « C1 + indice de classe divulgué délibérément », repris de A. Il doit produire la double différence. Sinon, E6b est aveugle et déclaré tel.
- Témoin : un modèle figé hors ligne avant t₀, repris de F via A.

**Unités et effectifs** :
- Agents : une analyse par modèle, avec un contexte neuf pour chaque tentative et sans retour du score du détecteur. Avec 500 tentatives par condition, la demi-largeur est d'environ 6 points (illustratif).
- Humains : un participant par condition. Il faudrait environ 200 participants par bras pour une demi-largeur d'environ 10 points (table de A). Le volet humain est donc exploratoire et ne rend pas de verdict.

**Prérequis** : sur un pilote disjoint, TPR en C0 ≥ δ + 10 points (illustratif).

### E2′ : ingestion par des systèmes

**Matériel** :
- L pages sur un hôte d'autorité comparable, étiquetées comme tests, avec des témoins `noindex` ;
- des canaris littéraux et des canaris sémantiques (faits fictifs, écrits dans le vocabulaire du domaine, sans rapport avec le mécanisme réel) ;
- des canaris négatifs, scindés en calibration et validation.

**Cohortes** :
- Q-hebdo : interrogée chaque semaine ;
- Q-final : interrogée seulement à T (T = 4 semaines, illustratif).

**Duel principal**, mesuré sur Q-final :
- H_A : taux de restitution ≥ r* (5 %, illustratif). H_B : taux < r*.
- Intervalle entièrement au-dessus de r*, avec un taux d'environ 0 sur les canaris de validation : H_B falsifiée.
- Borne supérieure sous r* : H_A falsifiée pour l'horizon T.

**K** : fixé après la mesure du taux de fausses alertes. Environ 72 canaris par type si ce taux est d'environ 0, jusqu'à environ 290 s'il vaut 0,02 (illustratif).

**E2b (auto-contamination)** :
- H_A : la cohorte Q-hebdo restitue plus que Q-final d'au moins r*. H_B : l'écart est inférieur à r*.

**Seconde métrique** : l'exposition *in situ*, sous la loi des requêtes de la tâche réelle.

**Limite déclarée** : le transport vers le lieu de prépublication réel n'est pas testé.

### E3′ : concurrence (expérience la plus faible, sans pouvoir de bascule à elle seule)

- **Origine** : la date publique d'un document qui existe dans les deux bras, indépendamment du drapeau. Par exemple, un résumé de financement public ; la disponibilité de telles données est à vérifier.
- **Exposition** : présence d'un drapeau, classée à une date repère t_L. Le suivi commence à t_L, ce qui supprime le temps immortel.
- **Issue** : un concurrent publie sur la même question avant l'équipe, avant l'horizon h, en risques concurrents. Les annotateurs comparent l'article concurrent au **résumé de financement**, sans connaître l'exposition.
- **Duel** : Δ = différence d'incidence cumulée à h.
  - H_A : Δ < 0 (le drapeau dissuade). H_B : Δ ≥ 0.
  - Intervalle entièrement sous 0 : H_B falsifiée. Intervalle entièrement au-dessus ou égal à 0 : H_A falsifiée. Cette lecture vaut **sous l'hypothèse déclarée** d'absence de confusion résiduelle.
- **Contrôles négatifs** :
  - un drapeau daté après le démarrage documenté du concurrent (repris de A) ;
  - une tendance avant le repère sur la même micro-question ;
  - une issue sur une autre question du même champ, en diagnostic seulement.

### E4′ : reconnaissance

- **Plan** : entre sujets, un dossier par juge, plusieurs sujets de dossier par condition, et une question de vérification de lecture (idée de E).
- **Bras** :
  - aucune pièce ;
  - drapeau spécifique daté avant le concurrent ;
  - empreinte ouverte après ;
  - drapeau spécifique daté après (contrôle négatif) ;
  - drapeau vague daté avant (secondaire).
- **Duel 1** : comparaison « spécifique avant » contre « aucune pièce ».
  - H_A : écart ≥ 15 points (illustratif). H_B : écart < 15 points.
  - Ce duel n'est interprétable que si le bras « daté après » ne dépasse pas le bras « aucune pièce ».
- **Duel 2** : comparaison « empreinte ouverte après » contre « spécifique avant ».
  - H_A : l'écart en valeur absolue est sous la marge d'équivalence (10 points, illustratif). H_B : il l'atteint.
- **Effectif** : environ 340 juges par bras pour une demi-largeur de 7,5 points à p = 0,5 (recalcul B, non audité, illustratif). Si le budget est limité, on garde trois bras : aucune pièce, spécifique avant, empreinte après.

### E5′ : qualité (scindée)

**E5a : portée de la publicité.**
- H_A : la proportion de protocoles publics qui reçoivent au moins une lecture substantielle externe avant le gel atteint q*. H_B : elle reste sous q*.
- Source : données observationnelles de registres publics comparables (disponibilité à vérifier).

**E5b : compétence, sachant la lecture.**
- Plan : des lecteurs externes recrutés et payés au même temps que les auditeurs internes. Tous sont aveugles au caractère fictif des protocoles. Les défauts sont implantés par un tiers, avec une réserve de classes de défauts.
- H_A : les lecteurs externes détectent au moins 20 points de défauts de plus (illustratif). H_B : l'écart est inférieur à 20 points.
- Contrôles négatifs : des protocoles sans défaut, et des modifications de surface neutres.

**Combinaison** : le bénéfice de la publicité est estimé comme portée × gain sachant la lecture. Un canal muet invalide l'essai.

### E6a : fuite interne (S10)

- **Plan** : tous les éléments secrets sont générés au même moment. On tire au sort ceux qui seront « accessibles en interne avant la mesure » et ceux qui resteront « scellés ». L'assignation est aléatoire et la mesure simultanée, donc il n'y a pas de terme de dérive.
- **Duel** :
  - H_A : l'écart de TPR entre les deux lots est au moins 5 points (illustratif). H_B : il est inférieur.
- **Contrôle négatif** : une permutation entre deux sous-lots tous deux scellés.
- **Effectif** : environ 645 éléments par lot pour une demi-largeur de 5 points à p = 0,7 (recalcul B, non audité, illustratif). En dessous, l'effet minimal détectable est déclaré.

### Instruments révisés

- **I1** : deux étiquettes publiées séparément, sans verdict global « fonctionne ».
- **I4** : le banc de décisions est rétrogradé.
  - Une décision est étiquetée « mauvaise » seulement si elle est dominée sous **toute** une famille de fonctions de perte déclarée.
  - Les dossiers ambigus sont exclus.
  - La famille de pertes n'est pas communiquée aux auditeurs.
  - Les dossiers « bonne décision malchanceuse » sont réservés, hors de la construction du barème.
  - La revendication est réduite : l'instrument mesure la conformité à des standards déclarés. Il ne dit pas que « le choix était le bon ».

---

## (c) Réponse à la question de l'arbitre

**Ce qui est établi.**
- *Aucun effet empirique.* FAITS ne transmet aucun fait. Les effets sur la reconnaissance, le devancement, la validité, l'adversaire, la qualité et le coût restent tous des HYPOTHÈSES.
- *Des propriétés de plan, sous modèle binomial* (recalcul B, non audité) :
  - avec 20 canaris, aucune conclusion d'innocuité n'est atteignable ; il en faut au moins 72 ;
  - comparer deux moitiés tirées d'un même procédé ne détecte pas une fuite du procédé ;
  - avec 20 à 40 juges par bras, un écart de 15 points n'est pas tranchable.

  Ces propriétés invalident des parties de ma conception III.1. Elles ne disent rien du monde.

**Ce qui n'est pas établi.**
- Ni le texte court, ni le choix de ses contenus, ni le délai d'ingestion par des systèmes n'ont d'effet mesuré.
- On ignore si une empreinte révélée après coup reçoit du crédit d'antériorité, et si la publicité ajoute de la qualité au-delà de l'engagement privé.
- L'effet d'un drapeau sur la concurrence est peut-être non identifiable par l'observation (E3′).

**Mon choix, révisé et conditionnel (HYPOTHÈSE).** Il reste l'option hybride, avec trois changements :
1. Avant les mesures, publier la question, H_A/H_B et les métriques, sans méthode du détecteur ni description des éléments secrets. Y joindre l'empreinte du protocole complet.
2. Déposer le protocole complet sous embargo chez un tiers, avec un **canari propre à l'exemplaire déposé**. J'emprunte ce contrôle à la critique de A contre D, en le disant : il traite le tiers comme une personne qui sait.
3. Générer **tous** les éléments secrets après la publication, et non la moitié, quand c'est faisable. E6 ne pouvait pas certifier la clause « moitié ».
4. Publier le reste après les résultats, avec l'audit de fuite exécuté par un tiers (E6a, E6b).

**Ce qui me ferait changer.**

| Issue | Conséquence |
|---|---|
| E1′ falsifie H_B (C1 renseigne l'adversaire au-delà du placebo) | Empreinte seule avant les résultats. |
| E6b positif | Rien avant, et changement de famille d'éléments secrets. |
| E2′ falsifie H_B | Je maintiens la génération de tous les éléments après publication et je raccourcis le délai entre texte et mesure. |
| E4′ montre l'équivalence de l'empreinte | La partie publique est supprimée. |
| E5′ montre que la publicité n'ajoute rien | La partie publique est supprimée. |
| Résultats inconclusifs | Rapportés comme tels. Par défaut, l'option la moins irréversible : l'empreinte seule. |

**Vérifications indépendantes possibles.** Ce sont des vérifications de processus, pas de chance :
- concordance de l'empreinte avec le protocole révélé ;
- dates de génération des éléments secrets ;
- audit E6a exécuté par un tiers ;
- canari de l'exemplaire déposé chez le tiers ;
- liste des écarts entre protocole engagé et analyse rapportée.

**Expérience à faire en premier : E1′, volet agents, avec E6b intégré.** Trois raisons :
1. Elle est bon marché et ne publie rien.
2. Son contrôle positif (le détecteur factice fragile) décide si l'adversaire est assez fort pour que *tout* le reste soit interprétable.
3. C'est la seule expérience qui puisse interdire la publication avant, quel que soit le résultat des autres.

E2′ est lancée en parallèle, parce que son coût principal est le délai calendaire.

**Ce qui peut être réfuté dans cette réponse** : neuf duels (E1′, E1b, E2′, E2b, E3′, E4′ en deux duels, E5b, E6a), plus E6b. Chacun a une issue qui falsifie H_A, une issue qui falsifie H_B et une zone inconcluante déclarée. S'y ajoutent deux rejets partiels motivés (2.2 et 2.5).

FIN-DE-CELLULE