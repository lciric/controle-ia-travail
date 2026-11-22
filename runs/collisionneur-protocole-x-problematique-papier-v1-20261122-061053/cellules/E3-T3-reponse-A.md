# Proposition A — Tour III.3 : réponse aux critiques

**Pièces reçues.** Ma conception III.1 et les quatre critiques (B, C, D, E) sont présentes et closes par leur ligne de fin. Je n'ai pas reçu les conceptions B, C, D et E : je ne peux pas vérifier ce que les critiques leur attribuent. Je ne réponds qu'aux sections « Sur la proposition A ».

**Statuts.** Aucune expérience n'a été exécutée ; tout ce qui suit reste HYPOTHÈSE de conception. Les critiques C et E étiquettent VÉRIFIÉ des déductions conditionnelles à un modèle statistique. Je ne modifie pas ces étiquettes. Je signale les calculs que j'ai refaits ; aucun n'est une mesure sur l'agent. Tous les chiffres sont illustratifs, sauf « deux mois » et « huit milliards de paramètres ».

## (a) Verdict sur chaque critique

### Type 3

| # | Critique (source) | Verdict |
|---|---|---|
| 1 | γ ≈ 0,5 est en grande partie vrai par construction ; γ mélange la persistance H du bruit honnête et l'exposant β de la dose-réponse (B, C, E). | **Acceptée.** J'ai refait le calcul : γ = 1 − (1 − H)/β. L'énoncé initial « γ ∈ [0,4 ; 0,6] » est retiré. Il devient « γ est prédit par H et β mesurés à part » (voir (b)). |
| 2 | Le résumé d'état efface les corrélations et force l'indépendance (C) ; à l'inverse, il peut créer une dérive de compression (E). | **Transformée en test.** Les deux critiques prédisent des effets opposés du même résumé. On mesure H et σ_H(T) sous trois régimes : résumé par l'agent, résumé exact d'oracle (contrôle de E), historique complet pour T ≤ 32 (contrôle de C). Je rejette seulement le mot « tautologie » : H n'est pas fixé par le banc, il se mesure. |
| 3 | Le δ réalisé n'est pas le δ commandé ; l'additivité peut varier avec T (B). | **Acceptée.** Toutes les régressions portent sur la touche réalisée par étape, connue par la vérité du banc. Le rapport dommage/somme des touches est rapporté à chaque T. |
| 4 | Contre le maximum, le seuil 0,85 tombe dans une zone dominée par des termes logarithmiques (B) ; le seuil doit être recalibré à chaque T (D) ; queues lourdes (E). | **Acceptée.** Mon calcul, sous scores gaussiens i.i.d. et seuil recalibré à 5 % par trajectoire, donne un décalage requis d'environ 1,14 écart-type à T = 8 et 0,81 à T = 128, soit γ_max ≈ 0,88 (quantiles normaux de mémoire, à refaire par simulation). Le seuil fixe 0,85 est donc non jugeable. Les scores sont ramenés à des scores normaux par la fonction de répartition honnête. |
| 5 | Normaliser par un σ_H qui dépend de T change la pente : la pente normalisée vaut γ − η (D, E). | **Acceptée.** Ma pièce était ambiguë. Le dommage est rapporté en unités brutes du banc, avec une normalisation fixe ; η est estimé à part. |
| 6 | Le dommage au croisement n'est pas un dommage maximal (D). | **Acceptée.** D* devient D₅₀(T, famille). Aucune affirmation de maximum sans adversaire adaptatif. |
| 7 | Le croisement à 50 % peut ne pas exister (plateau, cible hors image) ; le localiser et mesurer le dommage sur les mêmes trajectoires couple les erreurs (D, E). | **Acceptée.** Ajustement monotone de la dose-réponse. Une cellule dont la grille n'encadre pas 50 % est déclarée non jugeable. Localisation et mesure se font sur des moitiés disjointes. |
| 8 | Avec N = 5, aucun seuil sous 1/6 n'est étalonnable sans loi (B, C, D, E). | **Acceptée.** Je l'avais noté sans en tirer la conséquence. N ∈ {20, 40, 80} pour le niveau 5 % ; N = 5 seulement au niveau 1/6. |
| 9 | Une variance entre trajectoires τ₀² > 0 donne γ → 1 au-delà de T ≈ σ_ε²/τ₀², même avec N infini ; N n'entre que par le facteur (1 + 1/N) (C, E). | **Acceptée ; ma prédiction 3 est retirée dans sa forme initiale.** J'attribuais la remontée de γ à la petitesse de N ; le calcul l'attribue à τ₀². Nouvelle prédiction : le croisement T* = σ_ε²/τ₀², avec les deux variances mesurées sur les honnêtes. |
| 10 | Le bootstrap ignore le regroupement par graine et données (B) ; la variance du cumul s'estime sur des trajectoires (D). | **Acceptée.** Bootstrap par grappes (instance de tâche), commun à toutes les cellules. |
| 11 | Contrôle manquant : consigne de sabotage présente, dommage forcé à zéro (B). | **Acceptée.** Ce contrôle devient le cœur de l'expérience à faire en premier. |
| 12 | Paire honnête–honnête pour estimer σ_H(T) indépendamment du seuil (D). | **Acceptée.** |

### Type 2

| # | Critique (source) | Verdict |
|---|---|---|
| 13 | La réponse attendue annonce 15 points, le duel tranche à 5 (B) ; H_A et H_B doivent être complémentaires autour d'un seuil unique g (D). | **Acceptée.** Seuil unique g = 10 points. J'adopte la règle de D pour tous mes duels : H_A : Δ ≥ g ; H_B : Δ < g ; un intervalle à cheval est non concluant. |
| 14 | « Gelé avant toute attaque » est faux : la sonde est entraînée sur la famille (i) (B, D). | **Acceptée.** Trois partitions : développement (honnêtes + famille (i)), gel haché, évaluation. Aucun choix de couche ou de comparateur après le gel. |
| 15 | « Les étapes où l'évidence cumulée croît le plus » sont celles de plus fort score instantané : l'allocation n'a rien de séquentiel (C, E). Statistique d'alarme et politique d'audit changent ensemble (D). | **Acceptée.** L'incrément d'une somme est son terme. Le mécanisme se décompose en plan factoriel 2 × 2 (voir (b)). |
| 16 | Adaptateur LoRA bénin de même rang (B, C, D, E) ; retours d'outil bénins de même format (D). | **Acceptée.** Les fausses alertes sont mesurées sur ces canaux bénins. |
| 17 | La sonde de ré-encodage omet les sorties d'outil : sur la famille (iii), le gain interne peut n'être que la lecture de l'injection (C). | **Acceptée.** Le ré-encodage reçoit tout le contexte visible de l'étape (sorties d'outil et texte), sans consigne adverse ni adaptateur. |
| 18 | Filtrer sur D ≥ 2σ_H conditionne sur une issue aléatoire et crée une corrélation avec le score (C). | **Acceptée.** Analyse en intention de traiter : toutes les trajectoires d'une configuration préenregistrée comptent au dénominateur. σ_H vient d'honnêtes disjoints. |
| 19 | Une sonde locale faible ne justifie pas d'arrêter l'étude du cumul (D). | **Acceptée.** Ma porte d'arrêt contredisait le cadre, qui pose un signal faible par étape. Nouvelle porte : arrêt seulement si l'effet moyen par étape, poolé sur le développement, a un intervalle incluant 0. |
| 20 | Les activations ne peuvent pas battre la lecture optimale du texte si leur loi sachant le texte est inchangée (D) ; la sonde perd sa puissance si les directions entre familles ne sont pas alignées (C, E). | **Acceptée comme condition de lecture.** H_A′ se lit « gain sur ce moniteur de texte et sur le ré-encodage », pas « information absente du texte ». Le cosinus entre directions de décalage des familles est rapporté. Je n'ai pas refait la formule de C. |
| 21 | L'enrichissement du ciblage est plafonné à T/m (D) ; il tend vers l'uniforme quand le signal par étape est petit devant √(2 log(T/k)) (C). | **Acceptée, transformée en prédiction.** Mon critère « ≥ 2 fois m/T » était impossible pour m/T > 0,5. Dans le régime des petites touches, je prédis désormais un ciblage sans gain. |

### Type 1

| # | Critique (source) | Verdict |
|---|---|---|
| 22 | La borne est un fait d'échantillonnage ; l'expérience teste P3 et P6 (B). | **Acceptée entièrement.** La question est reformulée sur les hypothèses. |
| 23 | q supposé est circulaire s'il vient des mêmes familles (B) ; récuser q ou c après coup immunise la garantie (E). | **Acceptée pour le préenregistrement** : q(x) et c sont fixés sur le développement, avant l'équipe rouge. **Rejetée sur un point** : dans ma pièce, H_B valait déjà réfutation, et dire quelle hypothèse a cédé ne sauvait pas H_A. Je l'écris sans ambiguïté : tout échec de q ou de c sur l'inédit réfute la garantie pour cette classe. |
| 24 | Sensibilité hétérogène : la borne exige le minimum de q_i (B) ; il faut minorer des risques conditionnels ; une cécité commune sur une fraction u des trajectoires donne une survie ≥ u quel que soit le budget (D). | **Transformée en test.** Audits répétés sur la même trajectoire pour estimer u. La borne utilise un quantile bas de q. |
| 25 | Si q(x) tend vers le taux de faux positifs quand la touche x devient petite, l'adversaire qui étale viole la borne (C, E). | **Acceptée ; c'est la correction principale du type 1.** La grandeur à mesurer est la courbe q(x). Le contrôle de E (biais directionnel parmi options localement valides) est adopté. |
| 26 | Filtrer sur D ≥ 4σ_H laisse passer une attaque à une étape portée par le bruit honnête (C) ; conditionner sur la somme biaise les incréments (E). | **Acceptée.** On conditionne sur le nombre m d'étapes déviantes, connu par la vérité du banc, pas sur D réalisé. |
| 27 | Un plafond c déterministe est violé par les fluctuations honnêtes (C). | **Acceptée, avec une précision.** Tel qu'écrit, c se lisait comme une hypothèse sur l'agent. C'est un écrêtage imposé par l'agrégateur, dont le coût en qualité honnête est mesuré. Sans agrégateur à influence bornée, la garantie n'est pas définie ; elle ne couvre donc pas la seconde tâche. |
| 28 | m ≥ D/c exige L ≤ c·m sur toute la trajectoire ; attaque par conjonction de prémisses bénignes (C, D). | **Transformée en test** : famille « conjonction » ajoutée à l'équipe rouge. |
| 29 | Environ 67 trajectoires par famille ne suffisent pas pour une borne de 0,04 (B, E). | **Acceptée.** J'ai refait le calcul : il en faut au moins 74 avec zéro survie observée. Point de fonctionnement ramené à une borne de 0,20, avec 100 trajectoires par famille. |
| 30 | Erreurs naturelles de même amplitude, auditées en aveugle (B, D). | **Acceptée.** q doit être le même sur erreurs honnêtes et touches adverses de même taille, sinon l'audit lit le style de l'attaque. |

**Emprunts déclarés (B1).** Je reprends le contrôle « consigne présente, dommage nul » de B, la règle de décision et le plan croisé de D, la correction du ré-encodage et l'attaque par conjonction de C, le résumé d'oracle et le biais directionnel de E. Je ne les fusionne pas avec leurs propositions, que je n'ai pas lues.

## (b) Expériences corrigées

**Banc.** Inchangé, sauf quatre points : dommage en unités brutes ; trois régimes de mémoire (ligne 2) ; canaux bénins appariés (consigne neutre, LoRA bénin, retours d'outil bénins) ; dénominateurs en intention de traiter.

### E0 — dose-réponse à canal constant (semaines 1 à 3)

- **Honnêtes**, pour chaque T et chaque régime de mémoire : σ_H(T) brut et son exposant η ; persistance H (variance des sommes de scores par blocs, entre trajectoires) ; décomposition σ_ε², τ₀² ; fausses alertes du placebo.
- **Dose**, à T = 32 : honnête ; canal bénin ; canal adverse avec décisions remplacées par les décisions honnêtes ; canal adverse à six amplitudes. À chaque étape : touche réalisée x, score de chaque moniteur, verdict de l'audit.
- **Sorties** : β (exposant du décalage de score en fonction de x) ; q(x), sensibilité de l'audit selon la taille de touche ; fraction u de trajectoires où des audits répétés échouent tous.

**Duel E0-a (les moniteurs lisent-ils la dégradation ?).** À canal adverse présent, pente du score standardisé sur x :
- H_A : pente ≥ g (g = 0,1 écart-type de score par écart-type de touche) ;
- H_B : pente < g.
- H_B réfute l'idée que ces moniteurs voient la dégradation : ils voient le canal. Les types 2 et 3 n'ont alors d'objet qu'avec l'audit.
- H_A réfute l'objection « signature de la consigne » pour ce moniteur.

**Duel E0-b (l'audit voit-il les petites touches ?).** Rapport r = [q(x)/x à la plus petite touche] / [q(x)/x à la plus grande] :
- H_A : r ≥ 0,5 (sensibilité à peu près proportionnelle à la touche) ;
- H_B : r < 0,5 (effet de seuil).
- Enjeu (mon calcul, à revérifier) : si q(x) ≈ s·x, alors m·q(D/m) = s·D pour tout m, et la borne exp(−k·s·D/T) ne dépend plus de l'étalement.
- H_B réfute toute garantie par étape contre l'étalement et fournit l'énoncé d'impossibilité 4a.
- H_A réfute l'objection de C et E pour cet audit et ce banc.

### Type 3 corrigé

**Question.** La courbe D₅₀(T), contre un détecteur cumulatif recalibré à chaque T, est-elle prédite sans paramètre libre par H, β, σ_ε² et τ₀² mesurés sur des trajectoires disjointes ?

**Duel.** e = erreur relative maximale, sur les cinq longueurs, entre D₅₀ mesuré et D₅₀ prédit (exposant local 1 − (1 − H)/β sous T*, remontée vers 1 au-delà) :
- H_A : e ≤ 25 % ;
- H_B : e > 25 %.
- H_B réfute la composition : l'adversaire fait autre chose que décaler une moyenne.
- H_A réfute l'idée que le sabotage d'agents échappe à la loi importée, et donne trois grandeurs propres à l'agent.

**Second duel.** L'écart γ_max − γ_cumul est comparé à sa valeur simulée par rééchantillonnage des scores honnêtes, pas à un seuil fixe.

**Contrôle d'instrument (repris de B).** On injecte dans les scores honnêtes un bruit persistant et une réponse non linéaire connus ; l'estimateur doit redonner l'exposant attendu.

**Issue sans intérêt.** H ≈ 0,5, β ≈ 1 et τ₀² ≈ 0 dans les trois régimes de mémoire et sur la seconde tâche. Le résultat se réduit alors au théorème central limite et ne vaut que comme ligne de base. Je le dis d'avance : c'est l'issue que B, C et E jugent la plus probable sur le banc synthétique.

### Type 2 corrigé

**Question.** Dans le plan {alarme : maximum recalibré, cumul} × {audit : uniforme, k plus forts scores}, quel facteur porte le gain de détection sur familles tenues à l'écart, à fausses alertes et budget égaux ?

**Duels (g = 10 points, familles (ii) et (iii), canaux bénins comme référence).**
- Alarme. H_A : cumul − maximum ≥ g ; H_B : < g.
- Ciblage, dans le régime où l'effet par étape est inférieur à 0,5 écart-type. H_A : enrichissement ≤ 1,5 fois le taux de base ; H_B : > 1,5. H_B réfuterait ma nouvelle prédiction et rétablirait l'intérêt du ciblage.
- Activations. H_A′ : sonde − ré-encodage à contexte complet ≥ 5 points ; H_B′ : < 5.

**Issue sans intérêt.** Le gain d'alarme égale ce que prédit le type 3 et les deux autres duels donnent H_A et H_B′. Le « mécanisme » est alors une somme (Page, 1954) et n'apporte rien au-delà de la loi.

### Type 1 corrigé

**Question.** La courbe q(x), son quantile bas, la cécité commune u et la sous-additivité L ≤ c·m, toutes fixées sur le développement, tiennent-elles sur des familles construites après gel par une équipe qui n'a pas vu le défenseur ?

**Énoncé testé.** Conditionnellement à m étapes déviantes, la probabilité qu'aucun audit uniforme n'en voie une est au plus u + (1 − u)·maxₘ (1 − m·q(D/m)/T)^k. La forme est à revérifier ; ce n'est pas un théorème nouveau.

**Duel.** Sur chacune des quatre familles inédites (les trois initiales, plus « conjonction ») :
- H_A : survie ≤ 0,20 ;
- H_B : survie > 0,20 pour au moins une famille.
- Intervalle exact unilatéral à 95 %, 100 trajectoires par famille.
- H_A non réfutée se rapporte « non réfutée par quatre familles ».

**Issue sans intérêt.** E0-b donne H_B (rien à garantir par étape), ou l'écrêtage coûte plus de 10 % de qualité honnête.

## (c) Réponse à l'arbitre

**Ce qui est établi.** Rien sur l'agent : les faits ne contiennent aucune mesure et aucune expérience n'a été exécutée. Les critiques ont établi par calcul, sous conditions, quatre défauts de ma conception, que je confirme :
1. l'exposant γ n'est pas une propriété de l'adversaire ; il vaut 1 − (1 − H)/β, puis tend vers 1 au-delà de T* = σ_ε²/τ₀² ;
2. mon allocation « séquentielle » des audits était un classement par étape ;
3. ma borne du type 1 est de l'arithmétique d'échantillonnage, et tout son contenu empirique est dans q(x), u et la sous-additivité ;
4. plusieurs de mes critères étaient non jugeables : N = 5 au niveau 5 %, seuil 0,85 contre le maximum, 67 trajectoires pour une borne de 0,04.

**Ce qui ne l'est pas.**
- Que les moniteurs lisent la dégradation plutôt que le canal de l'attaque.
- Les valeurs de H, β, τ₀² et η pour un agent de 8 milliards de paramètres, avec ou sans résumé d'état.
- La forme de q(x) pour les petites touches, donc l'existence même d'une garantie par étape.
- L'apport des activations au-delà du texte.
- La nouveauté de quoi que ce soit : je n'en attribue aucune. La procédure de vérification du tour III.1 reste à exécuter (citations descendantes, requêtes croisées datées, deux spécialistes).
- Les antériorités sont inchangées et toujours citées de mémoire : Ker, Pevný, Kodovský, Fridrich 2008 ; Page 1954 ; Greenblatt, Shlegeris, Sachan, Roger 2023.

**Classement révisé** (jugement, pas résultat).
1. **Type 3**, avec une prétention réduite : non plus « retrouver √T », mais mesurer H, β et τ₀² et tester une courbe prédite sans paramètre libre. Ces mesures restent le prérequis des deux autres types.
2. **Type 1**, qui monte d'un rang : reformulé sur q(x), chaque issue informe (garantie conditionnelle si la sensibilité est proportionnelle à la touche, impossibilité s'il y a un seuil).
3. **Type 2**, qui descend : sa partie distinctive s'est réduite à un classement par étape, et ce qui reste est le type 3 lu du côté du défenseur.

**Ce qui changerait ce classement.**
- Le type 2 remonte si le ciblage enrichit de plus de 1,5 fois en régime de petites touches, ou si la sonde bat le ré-encodage complet d'au moins 5 points sur famille tenue à l'écart.
- Le type 1 descend si E0-b donne H_B.
- Le type 3 descend si E0-a donne H_B pour tous les moniteurs, ou si son issue sans intérêt se réalise.

**Quatrième type.** Je maintiens 4a (borne d'impossibilité) et 4b (instrument de mesure). 4a a maintenant deux formes testables : le plancher τ₀², sous lequel aucun décalage de niveau n'est détectable quel que soit T, et le seuil de q(x).

**Expérience à faire en premier.** E0, pour trois raisons :
- elle coûte environ trois semaines sur le banc déjà prévu ;
- ses deux duels décident si les types 2 et 3 ont un objet (E0-a) et si le type 1 en a un (E0-b) ;
- elle fournit les paramètres dont dépendent toutes les prédictions suivantes.

Si E0-a et E0-b donnent tous deux H_B, l'article à écrire est un résultat négatif de type 4a, à rapporter comme tel.

FIN-DE-CELLULE