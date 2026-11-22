# Tour III.3 : réponse aux critiques (proposition A)

Pièces reçues : FAITS, QUESTION, ma conception III.1 et les critiques B, C, D, E sont présentes et non coupées ; je n'ai pas contrôlé les empreintes.

Statuts :
- Les FAITS ne portent aucune étiquette ; je les traite comme RAPPORTÉ.
- Je laisse aux critiques les statuts qu'elles se donnent.
- Mes corrections sont des HYPOTHÈSES de méthode.
- Mes chiffres sont des calculs illustratifs, y compris quand j'ai refait le calcul d'un critique.
- Rien ici n'est VÉRIFIÉ par moi.

Je ne réponds qu'aux sections « Sur la proposition A ».

## (a) Critiques : décision et conséquence

### Acceptées, avec retrait ou modification

| # | Critique (source) | Décision | Conséquence |
|---|---|---|---|
| 1 | D3 : le test KS est aveugle en queue, et sa loi nulle est fausse sur des rangs discrets à témoins partagés (B-b, C-b2, D-b, E-b) | Acceptée | KS retiré. Remplacé par un test binomial sur le franchissement d'un seuil gelé (X2). |
| 2 | D4 est vrai par construction pour P1 à P3 (B-a3, E-a) ; le taux de détection est indéfini à prévalence nulle (D-a) ; injection i.i.d. et salve sont confondues (E-a3) | Acceptée | D4 sort du test de mort de P1 et de P3. Il y devient un test unitaire d'invariance : seuil identique au bit près quand le flux est remplacé. Il reste une expérience (X3) pour les seules règles dont l'état dépend du flux. |
| 3 | P4, second volet : « dérive du flux sans dérive des témoins » vient aussi d'une source bénigne absente de la banque de témoins ou d'une dérive différentielle du jumeau (B-a5, C-a3). D ajoute que si (1−π)F_H + πF_S = F′_H, aucune décision de cause n'est possible. | Acceptée | Je retire la lecture « signal de sabotage au niveau population ». La sortie devient « divergence flux–témoins, cause non attribuée ». L'action est la même dans les deux cas : gel du seuil, pas de ré-étalonnage sur le flux, relecture humaine d'un échantillon. |
| 4 | P4, premier volet : croissance bornée par la KL ; pour une dérive de queue seule, le délai dépasse le budget de témoins (B-b, C-b3). Après la rupture, les p-valeurs séquentielles redeviennent uniformes (E-b). | Acceptée, transformée en test (X5) | Détail sous le tableau. P4 n'est plus une « porte » contre la dérive de queue. |
| 5 | P3 : fuite si b(t) est choisie sur les témoins qui fixent le quantile (B-a4, E-a) | Acceptée | b est figée et empreinte avant tout témoin du régime courant, à partir de l'historique des autres régimes. La garantie par épisode vaut pour toute b indépendante des témoins. Seule l'uniformité par longueur dépend de la qualité de b. |
| 6 | D0 : bande trop étroite sous corrélation intra-tâche (B-a1) ; variance d'évaluation ajoutée à la variance d'étalonnage (C-a4) ; seuil partagé et seuils retirés répondent à deux questions (D-a) | Acceptée | Coupes par blocs de tâches ou de sessions. D0 est scindé en X0a (seuil partagé) et X0b (seuils retirés). |
| 7 | D1 : non identifiable si la version et le mélange de tâches changent ensemble (B-a2) ; l'appariement sur la longueur réalisée est un conditionnement post-traitement (E-a1) ; Clopper–Pearson paramétré par m est faux sous pondération (E-b) | Acceptée | Plan croisé 2×2 (X1). Appariement sur tâche et graine seulement ; la longueur devient une issue mesurée. Intervalles par rééchantillonnage de blocs. |
| 8 | P2 : même médiane et même écart interquartile, queue triplée (C-b1, D-b, E-b) ; variance d'estimation (C-b1) ; écart interquartile nul possible (E-b) ; pas d'héritage de la borne de P1 (D-b) | Acceptée ; je corrige aussi un de mes chiffres | Détail sous le tableau. P2 position-échelle est retirée. |
| 9 | Biais de pré-test D2 → P2 (C-a1) ; arrêt optionnel dans « essai invalide, augmenter l'effectif » (E-a) ; ré-étalonnage qui inclut les témoins ayant déclenché l'arrêt (E-a) | Acceptée | En déploiement, le choix de règle ne dépend plus d'un duel : il dépend de n seul, fixé d'avance. Les duels ont un effectif pré-enregistré et un essai indécis est rapporté tel quel. Autre option : une suite de confiance valide à tout instant (Howard, Ramdas, McAuliffe, Sekhon, 2021, « Time-uniform, nonparametric, nonasymptotic confidence sequences »). Après un arrêt, P1 repart sur des témoins strictement postérieurs. |
| 10 | P1 : la loi bêta porte sur la loi qui a produit les témoins, pas sur l'agent (D-a) ; ρ ne borne pas l'écart de queue et ma formule suppose des variances égales sans biais de moyenne (D-b, E-a2) | Acceptée | Le critère de validité devient l'erreur de transport F̄_H(q) − F̄_T(q) au seuil livré. ρ ne renseigne que sur la puissance. |
| 11 | Falsifier l'échangeabilité du jumeau ne tue pas P1 si ses témoins sont des épisodes indépendants du véritable agent honnête (D-a) | Acceptée ; ma phrase de III.1 était trop large | Seules les variantes alimentées par le jumeau tombent. Mais de tels épisodes supposent S4 sous sa forme forte, qui reste une HYPOTHÈSE. |
| 12 | Conforme pondéré : le seuil devient infini quand le poids normalisé du point de test dépasse α ; ce n'est pas mon critère de taille effective (D-b) | Acceptée | Mon critère « taille effective < 99 » n'est exact qu'à poids égaux. La condition à rapporter est celle de D. |
| 13 | Pire cas : un triplement à un seuil ne borne pas le rapport des queues au seuil plus haut (D-b) | Acceptée | C'est cohérent avec mon calcul gaussien de III.1 (α/3 donne encore environ 1,2 %, illustratif). L'hypothèse « rapport borné par 3 » n'est pas testable depuis un seul seuil. |
| 14 | Effectif réel sous corrélation intra-classe : 299 et 900 sont des minorants (B-b) | Acceptée | Tout n s'entend en blocs indépendants. |
| 15 | Multiplicité des ré-étalonnages : δ non dépensé sur R régimes (C l'adresse à B ; elle vaut pour mon enchaînement P4 → P1) | Acceptée, en m'en servant | δ est dépensé par certificat et le nombre de certificats délivrés est publié. |

**Détail du point 4 (calculs illustratifs).**
- J'ai refait le calcul de C pour la queue seule : 0,03·ln 3 + 0,97·ln(0,97/0,99) ≈ 0,013 nat par témoin. Il faut donc au moins 225 témoins environ pour atteindre 1/δ = 20.
- J'ajoute le cas du décalage gaussien de 0,445 écart-type : KL ≈ 0,099 nat, soit une trentaine de témoins. C'est une borne d'oracle ; un pari non paramétrique sera plus lent.
- P4 reste donc un fil d'alerte pour les décalages du corps, pas pour la queue.

**Détail du point 8 (calculs illustratifs).**
- En III.1, j'annonçais qu'avec 50 témoins P2 ramenait le taux « vers 0,6–1,6 % à ±1 écart-type ». Ce chiffre ne comptait que l'erreur sur la médiane.
- J'ai refait le développement de C : Var(τ̂) ≈ (σ²/n)(1,57 + 1,36·z²). À n = 50, l'écart-type du seuil vaut environ 0,42σ.
- La plage corrigée est d'environ 0,3–2,8 %. Même sous sa propre hypothèse gaussienne, P2 position-échelle ne corrige donc pas le triplement de façon fiable à n = 50.
- Pour retrouver la précision annoncée, il faudrait n ≈ 285. À cet effectif, P1 est disponible.
- La variante « position seule » garde la plage 0,6–1,6 %, sous l'hypothèse plus forte d'une échelle inchangée. Elle est rétrogradée en contrôle mécanique M5, sans garantie.

### Transformées en test

| Critique (source) | Test |
|---|---|
| Témoins injectés contre honnêtes cachés du même lot, sans dérive (B-c) | Contrôle négatif de X2. |
| Divergence de queue pure entre agent et jumeau (E-c2) | Contrôle positif de X2. Si le test ne rejette pas, c'est le banc qui est invalide. |
| Isolation du canal témoin : scores des témoins dans des lots contenant du sabotage contre hors ligne (E-c3) | Ajouté à X2. C'est la vraie voie de capture de P1, celle que D4 ne testait pas. |
| Discriminabilité témoins contre production, AUC ≈ 0,5 (B-c) | Ajouté, comme condition nécessaire seulement : voir les rejets. |
| Arrêt optionnel sous nul exact (E-c1) | Contrôle du protocole de duel lui-même, à passer avant tout duel. |
| Dérive de queue à centre fixe, lot honnête jamais utilisé comme ancre (D-c) | Test de mort de M5. |
| Panneau de sabotage indépendant inséré après chaque historique (D-c) | Repris tel quel dans X3. |
| Frontière sous changement de la loi des longueurs, loi par pas invariante (C-c3) | X4. |
| Source bénigne dans le flux seul, zéro sabotage (B-c, C-c2) | X5, second bras. |
| Famille de dérive cachée à tous les proposants (B, remarque finale) | Je m'en sers pour tous les mondes plantés : le générateur caché est écrit par le tiers. |

### Rejetées, avec leur raison

- **C-a2, pour sa généralité.** C écrit que M(L) croît stochastiquement avec L « pour toute fonction b(t) fixée ». C'est faux en général : une frontière qui croît assez vite donne un maximum décroissant en L. Le sens dépend de b ; c'est justement ce que X4 mesure.
- **C-a2, pour l'étiquette.** Dire qu'une garantie par épisode est « vraie par construction » ne signale pas un défaut : c'est la définition d'une garantie. Le défaut serait un test vrai par construction, et le test de mort de P3 porte sur les tranches, où rien n'est acquis. J'accepte en revanche le contrôle demandé et la précision : la garantie par épisode suppose que la loi des longueurs des témoins égale celle du flux honnête.
- **B-c, discriminabilité, comme condition suffisante.** Un AUC proche de 0,5 pour un classifieur donné ne montre pas que l'agent ne distingue pas les témoins. Le test peut réfuter S5, pas l'établir.
- **C-c1, pré-test en loi de Student.** Il est sans objet pour la règle corrigée, puisque la chaîne D2 → P2 n'existe plus en déploiement. Je le garde comme contrôle du banc pour toute règle conditionnelle d'un autre proposant.

## (b) Expériences corrigées

**Règles communes.**
- Effectifs fixés d'avance, comptés en blocs indépendants (tâche ou session).
- Seuil gelé et empreint avant l'audit.
- Sur mondes plantés, tout l'étalonnage est retiré à chaque répétition (demande de D, que j'adopte).
- Un intervalle qui traverse la frontière donne « indécis » : rapporté, non prolongé.
- Convention de D adoptée : paramètre θ et tolérance ε fixés avant l'accès aux sorties.

**X2 : transport de queue témoin → agent (remplace D3).**
- Seuil q fixé par P1 sur n_T témoins du régime nouveau (jumeau ou témoins injectés), puis gelé.
- m épisodes honnêtes frais de l'agent, jamais utilisés comme ancres ; x = nombre de dépassements.
- H_A : F̄_H(q) ≤ 3 %. H_B : F̄_H(q) > 3 %. La frontière est le niveau du défaut.
- À m = 300 (illustratif ; bornes unilatérales à 95 %, approximation de Poisson, à recalculer exactement) :
  - x ≤ 3 réfute H_B ;
  - x ≥ 15 réfute H_A, et avec elle toute règle alimentée par ce témoin ;
  - entre 4 et 14, indécis.
- Limite : ce plan ne tranche pas entre 1 % et 3 %. Pour cela, m est de l'ordre du millier (illustratif).
- Contrôles :
  - positif : paire plantée à queue triplée et corps identique, rejet attendu ;
  - négatifs : jumeau contre jumeau, témoins contre honnêtes cachés du même lot ;
  - isolation du canal témoin.

**X0 : bruit contre dérive (remplace D0).**
- X0a : un seuil gelé, étalonné sur une troisième partition ; deux jeux de test indépendants, ancien et nouveau régime.
  - θ = p_nouveau(q) − p_ancien(q). H_A : θ ≤ ε. H_B : θ > ε.
  - H_A réfutée : la dérive dépasse le bruit de test.
  - H_B réfutée : le « triplement » relève du bruit, et la correction porte sur n et δ, pas sur un outil de dérive.
  - Contrôle négatif : deux coupes par blocs du même régime.
- X0b : mêmes coupes avec seuils retirés. C'est descriptif : la part de variance due à l'étalonnage.
- Séparer 1 % de 3 % demande environ 300 blocs par côté (illustratif).

**X1 : plan croisé (remplace D1).**
- Quatre cellules : version (ancienne, nouvelle) × tâches (anciennes, nouvelles), mêmes tâches et graines, sans appariement sur la longueur réalisée.
- θ_v = p(nouvelle version, anciennes tâches) − p(ancienne version, anciennes tâches). H_A : θ_v ≤ ε. H_B : θ_v > ε.
- H_B établie : la dérive est de concept, et le conforme pondéré est exclu pour un changement de version.
- H_A établie : la version seule ne déplace pas la queue. La dérive de concept est alors falsifiée à ε près, et le conforme pondéré reste à éprouver par son propre test de mort.
- Contrôle : covariable permutée.
- Faisable sur un banc à poids ouverts. Je ne sais pas si l'ancienne version reste exécutable dans le programme.

**X3 : capture (remplace D4), pour les seules règles dont l'état dépend du flux.**
- Panneau fixe de sabotages, inséré après chaque historique.
- Prévalence de 0 à 20 % (illustratif), en injection i.i.d. puis en salve.
- H_A : chute de rappel sur le panneau ≤ ε. H_B : > ε.
- H_B tue la règle. H_A réfute ma prédiction de III.1 sur l'adaptatif appliqué au flux.

**X4 : frontière de P3 et longueur.**
- Loi par pas invariante ; la longueur moyenne triple (illustratif).
- H_A : toute tranche d'effectif suffisant a sa borne supérieure sous la borne pré-enregistrée. H_B : au moins une tranche a sa borne inférieure au-dessus.
- H_B tue la forme b, pas la garantie par épisode.
- Bras de contrôle positif : loi des longueurs des témoins différente de celle du flux ; la garantie par épisode doit casser visiblement.

**X5 : P4.**
- Premier bras, queue seule triplée :
  - H_A : détection avant l'épuisement des témoins du régime dans au moins 1−β des répétitions. H_B : moins.
  - Je prédis H_B (HYPOTHÈSE, d'après le calcul KL). Si H_B tient, P4 est retirée comme protection de queue.
- Second bras, dérive honnête commune, 10 % de témoins (illustratif), zéro sabotage :
  - Le volet différentiel devient un test à deux échantillons, flux contre témoins contemporains.
  - Il ne s'agit plus de deux tests séparés mis en course. C montre, sur la garde de B, que le canal le plus fourni rejette alors toujours le premier ; l'objection vaut pour mon P4.
  - H_A : taux de « divergence » ≤ β. H_B : > β.

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi.** Ce sont des résultats mathématiques classiques, aucun n'est une mesure du programme.
- Un seuil pris sur une statistique d'ordre de n scores i.i.d. a un taux réel aléatoire, de loi bêta. Avec quelques centaines d'épisodes :
  - certifier « ≤ 1 % à 95 % » exige au moins 299 épisodes indépendants de la bonne population (illustratif) ;
  - aucun 1 % par tranche de quelques dizaines n'est certifiable sans hypothèse de forme.
- Les garanties du conforme adaptatif portent sur des erreurs observées. Sans étiquette d'honnêteté, elles contrôlent un taux d'alertes.
- Un flux non étiqueté est un mélange. Sans hypothèse, aucune règle ne distingue une dérive honnête d'un sabotage (formulation de D, que je fais mienne).
- Les quatre critiques ont établi contre moi, par le calcul :
  - mon test KS ne voit pas un écart de queue ;
  - ma martingale ne voit pas une dérive de queue dans le budget d'un régime ;
  - mon transport de quantile position-échelle est trop bruité là où il était censé servir.

**Ce qui ne l'est pas.**
- Le triplement en déploiement : RAPPORTÉ (CURA, identifiant recopié des faits, page non lue, référence à vérifier).
- Que ce triplement vienne d'une dérive plutôt que du bruit d'étalonnage (S2).
- Qu'il existe des épisodes certifiés honnêtes dans le nouveau régime (S4).
- Que la queue des témoins soit celle de l'agent honnête (S5). Les faits disent seulement que l'écart du jumeau est « fragile ».
- Ce que coûte P1 en détection : non mesuré.
- Je ne sais pas s'il existe un jeu public d'épisodes d'agents avec activations sur plusieurs versions.

**Une conséquence que je n'avais pas vue en III.1.** Valider en queue un témoin (jumeau ou injecté) demande des épisodes honnêtes frais de l'agent, en nombre du même ordre que pour étalonner directement sur eux (environ 300 dans les deux cas, illustratif). Le jumeau ne fait donc pas économiser d'épisodes honnêtes pour un seuil à 1 %. Il n'en fait économiser que si l'on admet que sa validation, faite une fois, se transporte au régime suivant. C'est précisément l'hypothèse que le défaut met en cause.

**Ce que je propose après critique** (HYPOTHÈSE ; statistique publiée, assemblage et tests de mort à moi) :
- **P1 maintenue.** Rang certifié sur témoins frais, par régime déclaré par métadonnées et non par détection ; δ dépensé par certificat ; sortie « non certifiable » ; conditionnée à X2.
- **P3 maintenue**, avec frontière figée sur l'historique.
- **P2** : la variante position-échelle est retirée ; la variante position seule devient un contrôle à battre.
- **P4 réduite** à un fil d'alerte pour les décalages du corps, avec une sortie « divergence non attribuée ».

**Quand renoncer au seuil fixe.** Dans deux cas :
- un régime n'offre pas 299 témoins indépendants ;
- X2 réfute le transport.

On annonce alors « non certifié » et on passe à un quota de relecture, en gardant un échantillon aléatoire hors quota pour l'audit (ajout de D, que j'adopte). Le quota promet une charge de relecture, pas un taux de fausses alertes.

**L'expérience à faire en premier : X2.**
- Elle porte sur l'unique supposition dont dépend toute règle à témoins, y compris les ancres des autres propositions.
- Elle se fait sur un banc à poids ouverts où l'honnêteté de l'agent est connue par construction, pour environ 600 épisodes (illustratif).
- X0a se fait en parallel sur les données brutes existantes, sans épisode nouveau.

FIN-DE-CELLULE