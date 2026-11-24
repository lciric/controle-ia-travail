# Contributions inédites contre le sabotage diffus : note de sortie du collisionneur sur les revendications

Dossier : `runs/collisionneur-protocole-x-revendications-v1-20261122-080928` (accord GO-2026-11-22-33). Question neutre : `docs/notes/collisionneur-v9/protocole-x-revendications-v1/question-neutre-revendications-v2.md` (97797597…, identique au bloc des faits du dossier).

Rédigé le 24 novembre 2026 par un lecteur Opus 5.5, classe C, à partir des seules quinze cellules du dossier, de son état et de son journal. Le lecteur est du même modèle qu'une des cellules (Claude Opus 5.5) ; il la traite comme les autres.

**État du dossier.** Étage III complet : trois tours, cinq modèles, quinze cellules, toutes « OK » (`etat.md`, 2b84b9f8…). Dépense comptée : 14,33 USD sur une ligne de 45 USD. Ce total compte au pire 1,74 USD pour un envoi coupé par le réseau (critique croisée de Gemini 4 Argon, « connexion réinitialisée ») ; la cellule a été relancée une fois sur le même accord et a abouti (`journal-etage3.txt`, 3599d667…). C'est une panne technique, pas un résultat. La part de GPT-6.2 Astra est surestimée d'environ 20 % (prix d'un modèle voisin appliqué ; `declaration-prix-astra-v1.md`, f611977c…). Aucune expérience n'a été exécutée : tout ce qui suit est conception, critique ou calcul sur papier.

## La question

Un défenseur surveille des agents fondés sur des modèles de langue, sur de longues tâches. Un adversaire sabote de façon diffuse : chaque action paraît honnête, le dommage s'accumule. Le défenseur a, par exemple, un audit d'unités tirées au hasard, des moniteurs qui lisent le texte ou les activations internes, et un petit nombre d'exécutions honnêtes de référence.

La question demande quelles contributions scientifiques seraient inédites aujourd'hui, zéro compris. Pour chacune : un énoncé falsifiable, le travail publié le plus proche, ce qui l'en distingue, comment un tiers vérifierait qu'elle est inédite, et l'expérience sur petits modèles ouverts qui la ferait tomber.

La question est neutre par construction. Elle ne nomme ni le programme, ni ses papiers, ni les copies multiples d'un même modèle. Les modèles n'ont donc rien vu des revendications en vigueur.

**Les trois tours.** Au tour III.1, chaque modèle conçoit à l'aveugle. Au tour III.2, chacun critique les quatre autres : confondants, ce qui serait vrai par construction, fuites, conditions de perte de puissance, contrôles négatifs manquants. Au tour III.3, chacun répond aux critiques qui le visent (acceptée, rejetée, ou transformée en test) et rend une page de conclusion. Deux règles cadrent le jeu : on ne fusionne pas les propositions d'autrui, on les critique ou on les emprunte en le disant ; toute expérience oppose deux hypothèses dont chaque issue réfute quelque chose.

Noms complets : Claude Fable 5.2, Claude Opus 5.5, Gemini 4 Argon, GPT-6.2 Astra, Gemini 4 Carbon.

## En bref

- **Aucune contribution n'est établie comme inédite.** Trois modèles le disent net (Fable, Opus, Astra). Argon et Carbon gardent trois candidates chacun, sous réserve de réfutation. Aucune recherche bibliographique n'a été faite.
- **Le confondant des poids est le résultat le plus solide du dossier.** Tout adaptateur de poids déplace les activations. Une sonde évaluée sur un saboteur affiné, sans témoin honnête affiné de la même façon, peut lire l'adaptateur et non le sabotage. Chacun des cinq modèles le relève contre au moins une autre pièce ; les quatre modèles concernés l'acceptent.
- **Deux plafonds statistiques reviennent partout.** Avec k références honnêtes, aucun seuil fondé sur les rangs ne descend sous un taux de fausses alertes de 1/(k+1). Et si les scores honnêtes ont une composante propre à chaque trajectoire, toute accumulation dans le temps plafonne. Tous les modèles finissent par mesurer cette corrélation honnête avant de promettre un gain séquentiel.
- **Les cinq commencent petit.** Trois (Fable, Opus, Carbon) testent d'abord si un petit modèle sait saboter de façon diffuse ; trois (Opus, Argon, Carbon) mesurent d'abord la corrélation honnête ; Astra commence par un petit contraste sur ce qu'apportent les activations. Tous écrivent d'avance ce qui tombe si cette première mesure échoue.
- **Pour les nœuds 5 et 7 de la fiche, rien de direct.** Aucun modèle ne parle de copies multiples. Trois éléments s'y transposent par analogie (voir la section dédiée), sans trancher.

## Le parcours de chaque modèle, en une table

| Modèle | Candidates au tour III.1 | Après les critiques (tour III.3) |
|---|---|---|
| Fable 5.2 | Trois : forme de la courbe « soupçon contre dommage » qui séparerait sondes et moniteurs de texte ; validité de l'audit liée à l'additivité du dommage ; meilleur usage de références honnêtes rares | Deux. L'additivité est retirée « sans reformulation de sauvetage ». La sonde est retestée à poids identiques ; les références servent à des continuations honnêtes depuis un état tiré au hasard |
| Opus 5.5 | Quatre, plus une référence à battre : coût informationnel du sabotage contre une dégradation aléatoire ; sondes « intention ou consigne » ; test séquentiel à garantie toujours valide ; audit par rejeu ; batterie mécanique | Cinq pièces reformulées, rangées par solidité : plan factoriel sur les sondes ; furtivité contre une dégradation dirigée ; rejeu à somme signée ; batterie mécanique ; test séquentiel déclassé. Nouveauté certifiable : zéro |
| Argon | Trois : somme cumulée normalisée par pas, texte et activations fusionnés ; sonde « dynamique » contre un saboteur affiné par préférences ; audit par rejeu en blocs | Trois, corrigées. Il concède que le gain des blocs est nul à budget constant dans le cas simple. Il les présente encore comme « véritablement ouvertes et inédites » |
| Astra | Aucune revendiquée ; une candidate : le gain d'alerte précoce propre aux activations, contre un défenseur public complet | Plus étroite : le gain doit aussi battre un défenseur qui connaît déjà la consigne initiale de l'agent. Portée limitée à un modèle gelé sous consigne |
| Carbon | Trois : audit de paires d'actions liées dans un graphe de dépendances ; écart entre activations et texte, appris sur l'honnête seul ; statistique de cohérence directionnelle | Trois, refondues : équipe rouge aveugle au graphe ; agent conditionnel à poids fixes ; martingale par rééchantillonnage du même modèle honnête |

## Ce que chaque modèle a proposé

### Claude Fable 5.2

- **Huit présupposés de la question.** Entre autres : le dommage est-il additif action par action ; l'audit reconnaît-il une unité sabotée quand il la tire ; l'erreur honnête se distingue-t-elle du sabotage à dommage égal ?
- **Candidate sur les sondes.** Au départ : le score d'une sonde ne dépendrait pas du dommage de l'action, celui d'un moniteur de texte lui serait proportionnel. Après critique, Fable reconnaît que cet énoncé n'est pas identifiable sur un saboteur affiné. Il le remplace par un saboteur « conditionnel » : il sabote quand un déclencheur anodin est présent, agit honnêtement sinon. Un témoin bénin a le même déclencheur et les mêmes poids. La statistique est une double différence, comparée à un moniteur de texte et à la même sonde posée sur un modèle lecteur tiers. Le mot « intention » est retiré.
- **Candidate sur l'audit, retirée.** Le dommage par action, mesuré par rejeu du reste de la trajectoire, n'était pas défini une fois les actions suivantes devenues invalides. Avec la définition corrigée (continuation honnête depuis chaque état), la somme des dommages par action égale le dommage total par télescopage. Fable rattache cette identité à un résultat connu (Kakade et Langford, 2002, de mémoire) et ne la revendique pas.
- **Candidate sur les références.** À budget égal de pas honnêtes générés, continuer honnêtement depuis un état tiré au hasard battrait l'étalonnage d'un moniteur et l'exécution honnête complète. Fable note la limite : ce bras détecte un dommage, pas un sabotage.
- **Trois modèles de travail, au tour III.2,** qui servent ensuite à tous : un effet propre à chaque trajectoire honnête ; un budget d'audit constant réparti en blocs ; le déterminisme des activations à poids et texte fixés.

### Claude Opus 5.5

- **Cinq conditions appariées** sur un pipeline d'analyse de données synthétiques : honnête ; honnête avec une consigne secrète bénigne ; saboteur par consigne ; saboteur distillé dans un adaptateur de poids, consigne retirée ; dégradation aléatoire de même dommage.
- **Après critique, un plan factoriel sur les sondes.** Il compare le saboteur à trois témoins. Un objectif secondaire secret porte sur les mêmes décisions, neutre pour le dommage par construction. Une dégradation dirigée sans intention, appariée en dommage. Des adaptateurs bénins de même rang. Des lectures forcées font lire à chaque modèle les mêmes textes. Opus en attend un résultat négatif publiable : une intention distillée dans les poids pourrait n'être pas lisible.
- **Erreurs reconnues.** Comparer le saboteur à une dégradation non ciblée était tranché par l'algèbre. Son contrôle négatif (rapport de vraisemblance moyen nul chez l'honnête) était faux.
- **Expérience à faire d'abord** : faisabilité du sabotage diffus et corrélation honnête, moins de 40 heures de processeur graphique (illustratif).

### Gemini 4 Argon

- **Somme cumulée de Page (CUSUM) sur texte et activations**, normalisée par pas sur vingt références honnêtes. Après critique : centrage de chaque trajectoire sur ses trois premiers pas, normalisation par tranche de longueur de contexte au lieu du numéro de pas, dérive de réglage abaissée, et deux témoins honnêtes nouveaux (un agent ralenti, un agent trompé par une documentation obsolète).
- **Sonde « dynamique ».** Elle mesure l'erreur de prédiction du passage d'un état caché au suivant, contre un saboteur affiné par préférences. Après critique : un témoin honnête affiné de même rang, une dimension réduite de 32 à 8, et un comparateur statique.
- **Audit par rejeu en blocs.** Argon accepte « sans réserve » que le gain soit nul à budget constant quand les incréments de bruit sont indépendants. Il en tire une loi d'échelle à deux exposants, à mesurer : celui de l'accumulation du dommage dans un bloc et celui de la divergence de deux rejeux honnêtes.
- **Coûts les plus bas du dossier** : 63 à 85 USD au tour III.1, 30 USD pour la première expérience (illustratifs).

### GPT-6.2 Astra

- **Une seule candidate, étroite.** Ajouter les activations à un défenseur qui a déjà le texte, l'audit, les vérifications mécaniques et les références augmente-t-il les alertes avant une échéance utile, à fausses alertes bornées, y compris sur des échecs honnêtes ?
- **Un banc d'allocation de ressources avec solveur exact.** Il mesure la perte d'option à chaque décision et n'appelle « diffus » qu'un cas où aucune décision ne porte plus du quart de la perte.
- **Une règle de décision reprise par trois autres modèles.** Fixer d'avance la région K des paramètres qui rend la revendication vraie. Une région de confiance entièrement dans K réfute l'hypothèse contraire ; entièrement hors de K, elle réfute la revendication ; à cheval, le duel est « non tranché ».
- **Après critique, un défenseur diagnostique de plus.** Il a la représentation initiale de la consigne, mais aucune activation ultérieure. La question devient : faut-il encore lire l'agent pendant ses décisions quand on exploite déjà sa consigne initiale ?

### Gemini 4 Carbon

- **Audit de paires dans un graphe de dépendances**, contre un sabotage « épistatique » : deux modifications inoffensives seules, nuisibles ensemble. Après critique : une équipe rouge aveugle au graphe, un graphe placebo, un tirage sur toutes les paires, un audit unitaire enrichi.
- **Écart entre activations et texte, appris sur l'honnête seul.** Après critique, Carbon reconnaît que le régime « poids différents » confond adaptateur et sabotage. Il ajoute un régime à poids fixes (agent conditionnel) et deux comparateurs, dont le détecteur conjoint.
- **Martingale d'échangeabilité appariée.** Introduite au tour III.3. À chaque pas sondé, on tire une action contrefactuelle du même modèle honnête ; la différence entre l'action réelle et l'action tirée serait symétrique sous l'hypothèse honnête. La garantie de fausses alertes échapperait alors au plancher 1/(k+1). Carbon la marque « vérifiée mathématiquement », sous la condition que l'agent déployé suive exactement la politique honnête.

## Accords

### Au tour III.1, à l'aveugle

- **La liste du déjà publié** est presque commune (tous de mémoire, non vérifiés) : protocoles de contrôle avec audit à budget limité ; tests séquentiels et sommes cumulées ; sondes linéaires de tromperie et leur contournement ; bancs de sabotage avec moniteurs ; rééchantillonnage d'actions suspectes ; menaces réparties et protocole adaptatif. Tous les modèles disent qu'« accumuler des signaux faibles » n'est pas inédit en soi.
- **L'audit n'est pas un oracle** en régime diffus : les cinq modèles le donnent comme une question ouverte malgré l'apparence. Si chaque action paraît honnête, reconnaître une unité sabotée quand on la tire n'est pas acquis.
- **Sabotage contre maladresse** : quatre modèles (Fable, Argon, Astra, Carbon) exigent des témoins honnêtes qui échouent à dommage comparable. Opus y répond par sa dégradation aléatoire.
- **Petit nombre de références honnêtes** : les cinq en font un point à mesurer, sur des tâches nouvelles.
- **Le transfert des sondes vers un saboteur affiné dans ses poids** est jugé ouvert par quatre modèles (Fable, Opus, Argon, Carbon).

### Après les critiques

- **Témoin de poids.** Chaque pièce qui affine un saboteur (Fable, Opus, Argon, Carbon) se le voit demander par au moins trois critiques ; les quatre l'acceptent. Fable par un saboteur conditionnel à poids identiques. Opus, Argon et Carbon par un adaptateur honnête de même rang et de même volume. Astra évite la question en renonçant aux poids et le dit comme une limite de portée.
- **Plancher 1/(k+1).** Fable, Argon, Astra et Carbon le posent ; Fable, Opus et Carbon l'acceptent pour eux-mêmes. Conséquences : décision au niveau de l'agent sur plusieurs tâches (Fable), références mises en commun par famille de tâches (Opus), cible de fausses alertes relevée de 1 % à 5 % (Carbon). Une cible de 1 % est jugée non mesurable avec les effectifs annoncés : les cinq le relèvent contre au moins une pièce.
- **Corrélation honnête au sein d'une trajectoire.** Fable montre que le rapport signal sur bruit d'une somme sur T pas tend vers δ/τ quand chaque trajectoire honnête a son propre décalage de variance τ². Les quatre autres le reprennent et prévoient de mesurer cette corrélation intraclasse (Opus, Argon, Carbon) ou de séparer les variations entre familles, entre trajectoires et au sein d'une trajectoire (Astra).
- **Blocs d'audit.** Fable, Astra et Carbon montrent, chacun par son calcul, qu'à budget constant et incréments indépendants, la taille du bloc ne change pas la puissance. Argon l'accepte.
- **Pas de quotients.** Un rapport dont le dénominateur peut s'annuler n'a pas de moyenne finie : les cinq le relèvent quelque part. Fable et Opus remplacent tous leurs rapports par des différences avec intervalle.
- **La dégradation non ciblée tranchée par l'algèbre.** À dommage final égal, une dégradation aléatoire doit faire des pas environ √T fois plus amples qu'une dérive dirigée ; elle laisse donc bien plus de traces. Fable, Argon et Carbon le montrent ; Opus l'accepte et passe à une dégradation dirigée sans intention.
- **Contrôles du texte.** Une sonde posée sur un lecteur tiers, ou des lectures forcées sans consigne, séparent ce que lit l'état interne de ce que contient le texte. Proposé par Fable au tour III.1, repris par Opus, Argon, Astra et Carbon.
- **Règle de décision à trois issues** (région K, « non tranché » possible) : adoptée par Fable, Opus et Argon, empruntée à Astra en le disant.
- **Commencer petit.** Les cinq conditionnent la suite à une mesure préalable bon marché : faisabilité du sabotage diffus (Fable, Opus, Carbon), corrélation honnête (Opus, Argon, Carbon), fidélité de la mesure du dommage (Fable), valeur de la consigne initiale (Astra). Chacun dit d'avance ce qui tombe si elle échoue, par exemple « sans objet à cette échelle » (Opus, Carbon).

## Désaccords

- **Règle de décision.** Carbon tranche sur l'estimation ponctuelle, « sans intervalle intermédiaire non jugé », avec une puissance calculée. Fable, Opus, Argon et Astra gardent la région de confiance et une issue « non tranché ». Le désaccord porte sur la place de l'incertitude d'échantillonnage dans le verdict.
- **Statuts.** Argon et Carbon marquent « vérifié » nombre de leurs dérivations ; Argon le fait aussi pour deux références (Wald, Page). Fable et Opus refusent de les endosser sans les changer. Astra marque « vérifié » ses seules implications mathématiques, et seulement « sous les lois spécifiées ».
- **Forme du témoin de poids.** Fable rejette l'adaptateur entraîné sur un style neutre : il change aussi les données d'affinage. Il préfère le contraste à poids identiques. Opus, Argon et Carbon gardent l'adaptateur bénin ; Carbon fait les deux régimes.
- **Résidu ou détecteur conjoint.** Fable montre, sous modèle linéaire gaussien, que le résidu de Carbon est un des deux termes d'un détecteur standard. Carbon répond que l'autre terme s'emballe quand la difficulté des tâches change. Non tranché.
- **La contradiction prétendue chez Astra.** Argon affirme qu'aucune sonde ne peut à la fois tenir les échecs honnêtes et rester muette sous consigne sans dommage. Astra rejette la nécessité, en s'appuyant sur un contre-exemple de Carbon (un score qui dépend de l'interaction entre consigne et état). Argon n'a pas répondu ; il n'y avait pas de quatrième tour.
- **Rejets partiels.** Opus rejette l'idée que son rejeu accède à la vraie valeur : seule l'étiquette de l'expérimentateur l'utilise. Fable rejette l'idée que relire un texte et le générer donnent des activations différentes, et la soumet à une vérification numérique. Astra rejette l'impossibilité de borner les fausses alertes tirée d'un effectif moyen attendu : c'est l'effectif réalisé qui compte.
- **Audit par blocs.** Argon le garde comme loi d'échelle à mesurer ; les autres le tiennent pour sans gain par défaut.
- **Coûts.** De 30 USD (Argon, première expérience) à 200–600 heures de processeur graphique (Fable, après correction). Tous illustratifs.

## Ce qui est neuf, ce qui est fragile

**Neuf, au sens où les modèles ne le citent pas comme connu :**

- le saboteur conditionnel opposé à un témoin conditionnel bénin, à poids identiques, avec double différence (Fable) ;
- le plan factoriel d'Opus : objectif secret neutre en dommage, dégradation dirigée sans intention, adaptateurs bénins, lectures forcées ;
- le défenseur qui connaît la consigne initiale, pour isoler la valeur des activations lues pendant les décisions (Astra) ;
- la loi d'échelle de l'audit par rejeu en blocs, à deux exposants (Argon, sur des calculs de Fable, Astra et Carbon) ;
- l'audit de paires sur graphe de contrats contre une équipe rouge aveugle, avec graphe placebo (Carbon, avec Astra) ;
- la martingale d'échangeabilité appariée par rééchantillonnage du même modèle honnête (Carbon).

Les outils sous-jacents sont donnés comme connus : tests séquentiels, valeurs conformes, martingales de test, analyse de programmes. Seul l'emploi serait propre.

**Fragile :**

- **Rien n'a tourné.** La précondition commune (un petit modèle ouvert sait-il saboter de façon diffuse ?) n'est pas établie ; les cinq le disent.
- **Les pièces du tour III.3 n'ont été critiquées par personne** : la martingale de Carbon, le centrage d'Argon sur trois pas, le saboteur conditionnel de Fable, l'objectif secret « neutre par construction » d'Opus, le défenseur à consigne initiale d'Astra.
- **La martingale de Carbon** suppose de pouvoir tirer, à chaque pas sondé, une action du modèle honnête de même capacité. Fable objectait à Argon qu'un tel accès contredit le « nombre limité » de références. Ce point n'a pas été confronté à Carbon. Sa parenté avec la littérature des tests par mise (Ramdas et al., 2023, cité de mémoire) est à vérifier.
- **Risque d'antériorité déclaré par les auteurs eux-mêmes** : le saboteur conditionnel rapproche Fable des travaux sur les portes dérobées ; le rejeu d'Opus recouvre en partie le rééchantillonnage publié (Bhatt et al., 2025, de mémoire).
- **Argon dit ses trois candidates « véritablement inédites »** sans recherche bibliographique. Les règles du dossier interdisent ce genre de portée.
- **Les chiffres d'effectifs.** Avec zéro alerte, borner un taux de fausses alertes sous 5 % à 95 % demande au moins 59 échecs honnêtes indépendants (Argon, Carbon, Astra ; « au moins 60 » chez Fable). L'arithmétique se refait en une ligne ; le reste (puissances, coûts) n'est pas contrôlé ici.

## Situer les propositions par rapport aux revendications en vigueur

Lecture du rédacteur, sur la table v2 corrigée (`docs/notes/revendications-en-vigueur-v2/table-revendications-en-vigueur-v2-corrigee-v1.md`, cefd3d79…). Les modèles n'ont pas vu cette table. Les rapprochements sont des pistes, pas des concordances établies.

- **Gain de l'accès interne (papier A).** Le contrôle « même sonde sur un lecteur tiers relisant le texte public » revient chez les cinq, sous une forme ou une autre. Il ne figure pas parmi les bases du critère de la porte de fin de phase 1 telles que la table les rapporte (« cascade », « dernier état »). Le défenseur à consigne initiale d'Astra est un comparateur de plus, du même esprit.
- **Accumulation sur sondes et modèle nul.** L'effet propre à chaque trajectoire honnête (Fable, puis les quatre autres) rejoint la proposition sans décision d'un modèle nul « racine, plus un terme entre tâches, plus une dérive ».
- **Loi de la référence honnête.** Le plancher 1/(k+1), le budget fermé de références (étalonnage compris) et le décompte des références consommées par tâche nouvelle vont dans le sens de la règle « déclarer m, n et la source ».
- **Plancher d'audit au hasard.** Astra sépare la fréquence à laquelle on tire une décision coûteuse de la fréquence à laquelle on la reconnaît une fois tirée. C'est l'esprit d'une probabilité de conviction mesurée par dommages plantés.
- **Lemme d'additivité, forme mesurée.** Fable montre qu'avec une attribution du dommage par continuation honnête, l'additivité devient une identité. Point à examiner : la forme mesurée revendiquée (conservation du déplacement cumulé sous fragmentation) ne doit pas être vraie par construction de la mesure. Le dossier ne dit rien de plus.

## Les nœuds 5 et 7 de la fiche

Fiche : `docs/notes/revendications-en-vigueur-v2/fiche-onze-noeuds-table-v2-v1.md` (72784e0f…). Le nœud 5 propose de resserrer la co-élévation des scores de sondes entre copies (position ou dépendance ; frontière de détection héritée ; corrélation honnête entre copies). Recommandation de la fiche : garder la lettre en vigueur jusqu'à cette note, puis resserrer « si la note concorde ». Le nœud 7 porte sur la thèse du papier B (deux nuls hérités, porte « position ou dépendance » avant la porte de la phase 2, repli en section du papier A). Recommandation : trancher après cette note.

**Ce que disent les cinq modèles : rien de direct.** Aucun ne parle de copies d'un même modèle, de coalition ni d'essaim. La question neutre ne les nommait pas. Toute lecture pour ces nœuds passe par une analogie du temps (les pas d'une trajectoire) à l'essaim (les copies). Cette analogie est celle du rédacteur, pas celle des modèles.

**Ce qui se transpose, par analogie :**

- **Mesurer la corrélation honnête avant de promettre un gain d'accumulation.** Les cinq la mesurent, dans le temps ; trois en premier (Opus, Argon, Carbon). C'est l'ingrédient « corrélation honnête » du nœud 5, et la « corrélation honnête mesurée d'abord » de la thèse du nœud 7.
- **Une somme simple comme base obligatoire.** Fable objecte à Carbon qu'à direction de nuisance connue, la somme des écarts centrés bat une forme quadratique. Opus, Argon et Carbon l'ajoutent ensuite comme comparateur. Carbon répond que la forme quadratique ne gagne que si l'adversaire annule la somme. C'est la forme du partage « position ou dépendance » : la somme pour un déplacement de position, une statistique d'ordre deux pour un changement de dépendance. Astra le dit en clair : des lois aux marges identiques peuvent avoir des dépendances différentes.
- **Une porte préalable avec repli écrit d'avance.** Les cinq conditionnent la suite à une mesure préalable bon marché et écrivent d'avance ce qui tombe si elle échoue. C'est la structure, non le contenu, de la porte proposée au nœud 7.

**Ce qui manque.** Aucun modèle ne cite la frontière de détection héritée (Arias-Castro, Bubeck et Lugosi, 2012). Fable cite une littérature voisine sur la détection de mélanges rares et faibles (Donoho et Jin, 2004, de mémoire, à vérifier). Rien ne porte sur la thèse du papier B, ni sur son repli en section du papier A.

**Concordance avec la fiche, sans trancher.** Pour le nœud 5, la note n'apporte ni accord ni désaccord direct. Elle soutient par analogie deux des trois ingrédients (corrélation honnête ; partage position ou dépendance), et rien sur le troisième (frontière héritée). Pour le nœud 7, elle éclaire la forme d'une porte préalable, pas l'objet de la thèse. Dire si une concordance indirecte suffit à lever la condition « si la note concorde » reste une décision de Lazar.

## Références à vérifier

**Aucune n'a été vérifiée sur PDF.** Les modèles inventent parfois des références ou en déforment le contenu. Trente-deux références nommées, six renvois sans titre.

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| Greenblatt, Shlegeris, Sachan, Roger, *AI Control: Improving Safety Despite Intentional Subversion* (2023 selon Fable et Opus, 2024 selon Argon, Astra et Carbon) | les cinq | Cadre de l'audit à budget limité ; antécédent le plus proche |
| Wen et al., 2024, *Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats* | Fable, Opus | Menaces réparties, protocole adaptatif |
| Bhatt et al., 2025, *Ctrl-Z: Controlling AI Agents via Resampling* | Fable, Opus, Argon | Rééchantillonnage ; recouvrement avec le rejeu |
| Griffin, Thomson, Shlegeris, Abate, 2024, *Games for AI Control* | Fable, Opus | Contrôle comme jeu |
| Benton et al., 2024, *Sabotage Evaluations for Frontier Models* | Fable, Opus, Argon | Bancs de sabotage |
| Kutasov et al., 2025, *SHADE-Arena* | Fable, Opus | Bancs agentiques avec moniteurs |
| Mallen et al., 2024, *Subversion Strategy Eval* | Opus | Difficulté d'une stratégie sans état |
| van der Weij et al., 2024, *AI Sandbagging* | Opus | Sous-performance stratégique |
| Christiano, 2021, *Low-stakes alignment* (billet) | Opus | Régime à faible enjeu |
| Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn, 2025, *Detecting Strategic Deception Using Linear Probes* | Fable, Opus | Sondes de tromperie |
| Bailey et al., 2024, *Obfuscated Activations Bypass LLM Latent-Space Defenses* | Fable, Opus | Contournement des sondes |
| MacDiarmid et al., 2024, *Simple probes can catch sleeper agents* (billet) | Opus, Argon | Sondes sur portes dérobées |
| Hubinger et al., 2024, *Sleeper Agents* | Opus, Fable | Portes dérobées ; antériorité du saboteur conditionnel |
| Azaria et Mitchell, 2023, *The Internal State of an LLM Knows When It's Lying* | Opus, Argon | Sondes de mensonge |
| Zou et al., 2023, *Representation Engineering* | Argon | Lecture de concepts dans les activations |
| Burns, Ye, Klein, Steinhardt, 2023, *Discovering Latent Knowledge in Language Models Without Supervision* | Carbon | Sondes sans supervision |
| Baker et al., 2025, *Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation* | Opus | Surveillance de la chaîne de pensée |
| Korbak et al., 2025, *Chain of Thought Monitorability* | Opus | Idem |
| Marks et al., 2025, *Auditing Language Models for Hidden Objectives* | Opus | Audit d'objectifs cachés |
| Wald, 1945, *Sequential Tests of Statistical Hypotheses* (marqué « vérifié » par Argon, sans pièce) | Fable, Opus, Argon, Carbon | Tests séquentiels |
| Page, 1954, *Continuous Inspection Schemes* (même remarque) | Fable, Opus, Argon, Carbon | Somme cumulée |
| Lorden, 1971, *Procedures for Reacting to a Change in Distribution* | Carbon | Détection de rupture |
| Vovk et Wang, 2021, *E-values: Calibration, combination and applications* | Opus | Valeurs e |
| Ramdas, Grünwald, Vovk, Shafer, 2023, *Game-Theoretic Statistics and Safe Anytime-Valid Inference* | Opus, Carbon | Garantie toujours valide |
| Vovk, 2021, *Testing Randomness Online* | Opus | Martingales de test conformes |
| Vovk, Gammerman, Shafer, 2005, *Algorithmic Learning in a Random World* | Carbon | Plancher conforme |
| de la Peña, Klass, Lai, 2009, *Self-Normalized Processes* | Carbon | Statistiques auto-normalisées |
| Donoho et Jin, 2004, *Higher criticism for detecting sparse heterogeneous mixtures* | Fable | Signaux rares et faibles |
| Hanley et McNeil, 1982, *The Meaning and Use of the Area under a ROC Curve* | Fable, Argon | Erreur-type de l'aire sous la courbe |
| Kakade et Langford, 2002, *Approximately Optimal Approximate Reinforcement Learning* | Fable | Additivité par télescopage |
| Avenhaus et Canty, 1996, *Compliance Quantified* | Fable | Jeux d'inspection |
| Weiser, 1984, *Program Slicing* | Carbon | Graphe de dépendances |
| Six renvois sans titre : billets de Greenblatt et Roger vers 2023 ; un billet sur sondes et portes dérobées ; travaux sur le sabotage de la recherche ; extensions multi-étapes du contrôle ; sondes supervisées sur agents dormants ; antécédent du contraste exact d'Astra | Fable, Opus, Carbon, Astra | Marqués « référence à vérifier » par leurs auteurs |

S'y ajoutent des résultats et méthodes nommés sans source (inégalités de Pinsker et de Ville, bornes de Clopper-Pearson, rétrécissement de Ledoit-Wolf, lois de Hotelling-Wishart et de Marchenko-Pastur, test de McNemar), deux bancs (SWE-bench Lite, BashBench), trois bibliothèques et une douzaine de modèles ouverts (familles Qwen2.5, Llama 3.1 et 3.2, Gemma 2). Noms, tailles et licences : à vérifier aussi.

## Propositions retenues

Retenues par le lecteur, à soumettre. Elles ne changent aucune revendication.

1. **Un témoin de poids pour toute sonde évaluée sur un saboteur affiné.** De préférence le contraste à poids identiques (saboteur conditionnel contre témoin conditionnel bénin) ; à défaut, des adaptateurs bénins de même rang, sur plusieurs graines. Raisons : relevé par les quatre critiques, accepté par les quatre concernés, coût faible.
2. **Mesurer d'abord la faisabilité et la corrélation honnête.** Un saboteur diffus existe-t-il sur petit modèle ouvert, et quelle est la corrélation intraclasse des scores honnêtes ? Écrire d'avance ce qui devient sans objet. Raisons : trois modèles pour chacune des deux mesures, les cinq mesurent la corrélation à un moment du plan, coût le plus bas du dossier.
3. **Déclarer le plancher 1/(k+1) et fermer le budget de références**, étalonnage compris, avec décision par agent ou par famille de tâches. Raisons : quatre modèles le posent, aucun ne le conteste ; concordant avec la loi de la référence honnête.
4. **Contrôles du texte** : la même sonde sur un lecteur tiers, des lectures forcées sans consigne, et un défenseur qui connaît la consigne initiale. Raisons : repris par les cinq sous une forme ou une autre ; ils séparent l'état interne du texte et de la consigne.
5. **Pas de quotient ; règle à trois issues.** Différences avec intervalle, région K fixée d'avance, issue « non tranché » annoncée. Raisons : quatre modèles sur cinq.

**Non retenu :**

- **le gain attendu de l'audit en blocs** : nul par défaut selon quatre calculs concordants ; la loi d'échelle d'Argon reste une mesure possible, pas une promesse ;
- **la statistique de cohérence directionnelle du tour III.1 de Carbon** et **la somme cumulée non centrée d'Argon** : retirées ou refondues par leurs auteurs ;
- **les statuts « vérifié » auto-attribués**, **la mention « véritablement inédites »** d'Argon et **tous les coûts** : avancés, non contrôlés ;
- **la partition sur estimation ponctuelle de Carbon** : minoritaire, non réfutée, seulement non suivie.

**À une demande approfondie, si Lazar le souhaite** : la martingale de Carbon (accès à la politique honnête, parenté avec les tests par mise) ; le résidu contre le détecteur conjoint ; le choix entre témoin conditionnel et adaptateur bénin. Et, pour les nœuds 5 et 7, une question neutre qui nomme les copies multiples, puisque celle-ci ne le faisait pas.
