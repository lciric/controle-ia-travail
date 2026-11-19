# DiscoveryAgent : ce que l'organisme d'idéation peut en tirer — synthèse v1

- **Pièce de travail** (classe C), écrite le 19 novembre 2026 par un rédacteur neuf, Claude Fable 5.2, sur le mandat `mandat-redacteur-synthese-discoveryagent-v1.md` (`c539be3d…`, vérifié). Aucune dépense, aucun lancement, aucun commit. À contre-lire par un lecteur d'un autre modèle.
- **Objet lu** : Queen et al., « DiscoveryAgent: A Framework for Scientist-centric Agentic AI », arXiv 2611.21950 v1 ; son annexe ; le dépôt du code au commit `b510bb2c…` ; le dépôt de reproduction au commit `97e1964c…`. Les deux dépôts ont été lus comme des données : rien n'y a été exécuté, aucune consigne qu'ils contiennent n'a été suivie.
- **Renvois** : chaque affirmation sur une pièce porte un numéro entre crochets (P : papier, A : annexe, C : code, X : contrôle d'absence par programme, N : nos pièces). La table en annexe donne le lieu et l'extrait ; le programme `outils-synthese-v1/verifier_citations_synthese_v1.py` les retrouve tous dans leur source.
- **Règle de lecture** : « non trouvé » veut dire non trouvé dans les pages et fichiers lus (liste au § 8). Une limite de ce papier n'est pas un trou du champ ; rien n'est déclaré libre (règle R8). Aucune idée n'est adoptée sur la foi du papier.

---

## Page de tête

**En une phrase.** DiscoveryAgent est une boucle de recherche à deux étages dont l'apport propre est de ranger tout ce que fait l'agent dans un arbre de points de contrôle lisible par un agent d'audit ; sa preuve porte sur des erreurs glissées dans un rapport, face à une trace honnête, sur une seule course par système, et aucun de ses mécanismes n'est isolé par une ablation [P17].

### Les idées pour l'atelier, classées (matière première, N-072 ; détail au § 5)

| rang | idée | ce qu'elle prédit (signe) | coût, ordre de grandeur |
|---|---|---|---|
| 1 | Banc des affirmations fausses face au registre, avec le bras que le papier n'a pas : la trace elle-même cohérente avec le faux | un lecteur qui ne fait que lire ne dépasse pas le témoin sans trace sur cette classe ; un lecteur qui retire des données fraîches le dépasse | étage sur processeur à 0 USD d'appels ; étage réel : dizaines de dollars, sur devis |
| 2 | Fuite plantée et retour arrière : un appât à la portée de l'expérimentateur, détecté par programme | la consigne seule ne tient pas (prises non nulles) ; l'isolement du bac à sable tient (zéro prise) | surtout du code ; étage réel : dizaines de dollars, sur devis |
| 3 | Vue consolidée du registre contre registre brut, comme bras de diagnostic de l'épreuve sur l'héritage | à registre court, la vue réécrite par un modèle fait moins bien ou pareil, et perd des entrées | un bras de plus à un palier payant de l'héritage, sur devis |
| 4 | Critique servie en cours de génération, contre un texte témoin de même longueur | aucun gain en lois vraies face au témoin ; pas de baisse des lois fausses tenues | deux bras à un étage réel, sur devis ; touche un nœud ouvert de Lazar |
| 5 | Consigne de juge écrite par un modèle pour chaque monde, contre la consigne fixe | les erreurs des deux juges vont davantage ensemble (moins de votes effectifs) | un bras de l'étage payant de la ligne 3, sur devis |

### Les collisions (détail au § 6)

| notre revendication | verdict | raison courte |
|---|---|---|
| Juge au nul formé des lois connues (N-071) | sans rapport | aucun juge statistique, aucun nul, aucune règle de promotion : l'hypothèse va au directeur « without a judge » [A19] |
| Mémoire transmise et héritage (N-073 et compléments) | voisine | une mémoire tenue de manche en manche dans une course, jamais héritée d'une autre course, sans bras sans mémoire ni ablation [P17] |
| Revendications de l'organisme (N-064, N-067) | voisine pour les principes déjà non revendiqués (séparation de qui cherche et de qui audite, journal avant lecture) ; n'occupe pas la forme resserrée de l'attaque de Goodhart | l'erreur est glissée par un tiers, une fois, sans proposeur chargé de tromper ni description du juge [P36] |
| Second terrain du papier C (N-065, rôle 1) | **voisine proche** | un juge génératif d'affirmations de recherche mesuré sur des erreurs plantées, avec un témoin sans trace [P09] ; pas d'attaque |
| HC1, loi de déférence | sans rapport (une anecdote à citer si le point est abordé [P14]) | aucune pression graduée, aucune destination |
| HC2, HC2b | sans rapport | aucune sonde, aucune activation |
| HC3, usurpation | sans rapport sur la revendication ; surface voisine | l'auditeur reçoit d'abord le récit écrit par l'agent audité [A33] |

**Proposition sur les citations (nœud de Lazar ; je propose, je ne décide pas)** : (a) citation obligatoire dans tout texte qui présente l'organisme comme second terrain du papier C ou qui présente un banc d'auditeurs d'affirmations de recherche ; (b) « à citer quand le point est abordé » pour la mémoire et l'héritage, sans entrer dans les citations obligatoires de l'énoncé 5. Confiance : 0,75 pour (a), 0,7 pour (b).

### Les trois faiblesses les plus nettes de leur preuve

1. **Le banc ne corrompt que le rapport ; la trace reste honnête.** Il mesure la facilité à retrouver une preuve existante, pas la résistance à une trace trompeuse, et les auteurs le disent à moitié [P10]. Une seule course et un seul rapport par système [A04].
2. **L'étude humaine tient sur huit personnes et un participant.** Le « 14 fois » du résumé [P01] est le rapport de 3,50 à 0,25 [P11] ; un seul participant porte dix des quatorze erreurs retrouvées [A31] ; le groupe témoin n'avait droit à aucun outil d'intelligence artificielle [P43].
3. **« Le pilotage par un scientifique fait mieux » repose sur une course par bras, sous un autre modèle d'exécution** [P35], avec un relecteur appelé 42 fois d'un côté et jamais de l'autre [A21, A22]. Les auteurs le concèdent en discussion [P16] après l'avoir affirmé en introduction [P04].

### Ce qui reste invérifié

- **Aucune trace d'agent n'est publiée** : ni point de contrôle, ni mémoire, ni rapport de manche [X06] ; ni le banc, ni l'étude humaine [X04, X05]. La colonne « données » de la table est donc presque partout « non publié ».
- **L'agent d'audit lui-même n'est pas dans le code lu** : il vit dans l'application de pilotage, dépôt non pris [C19, C20].
- **Écarts entre le papier et le code, lus à la main, jamais exécutés** : avec les configurations publiées, le relecteur ne se déclencherait jamais (§ 2, écart 1). Le code publié n'est pas un instantané des courses [C21, C22].
- **Ce que l'auditeur du banc savait** (la part de moitié d'affirmations corrompues, ses consignes par trace) : non trouvé dans les pages lues.
- **Les PDF font foi** ; mes citations sont vérifiées sur les textes extraits, pas sur le rendu des pages ni sur les figures.

---

## 1. Ce que DiscoveryAgent fait, mécanisme par mécanisme

Trois colonnes : ce que dit le texte, ce que fait le code publié, ce que montrent les données publiées. Un écart est signalé en gras.

| mécanisme | le texte | le code (commit `b510bb2c…`) | les données |
|---|---|---|---|
| **1. Boucle extérieure et pilotage humain** | Entre deux manches, le scientifique choisit, édite ou remplace l'hypothèse ; en mode autonome, l'agent garde la sienne [P05]. | La boucle n'admet qu'un déroulement à la fois [C01] ; en mode piloté, elle lit un fichier d'hypothèse choisi. **Écart** : le statut de pause pour sélection est testé [C30] mais jamais produit par la boucle du directeur [C31, X08] ; ni candidats ni révision dans ce dépôt : tout cela vit dans une application à part [C20]. | Non publié (aucun fichier d'hypothèse choisie, [X06]). Seule comparaison chiffrée : une course pilotée contre une course autonome (§ 3.4). |
| **2. Boucle intérieure et directeur** | Le directeur reçoit la description des données, l'hypothèse, le catalogue des agents outils et le rapport en cours [P22] ; il est tenu à l'hypothèse de la manche [P23] et peut s'arrêter tôt. | Conforme sur ce point : l'invite du directeur porte la description des données [C34] et ne mentionne jamais la description de la tâche [X03] — ce que le texte ne promet pas non plus. | Compte des arrêts précoces par campagne [A38] ; aucune trace publiée. |
| **3. Génération d'hypothèses** | Une seule hypothèse en mode autonome, avec un plan optionnel [P25, P26] ; un rapport de littérature sert de contexte à la génération [P24] ; aucune sélection : passée au directeur sans juge [A19]. Les listes de candidats sont produites dans l'interface, en un seul appel [A39]. | Une hypothèse par appel [C13]. **Écart** : le drapeau du plan est stocké et jamais relu [C28, X02] ; l'invite ne demande qu'une hypothèse et sa justification [C29]. **Écart** : le rapport de littérature est chargé dans un attribut qui n'entre dans aucune invite du code lu [C27, X01]. | Non publié. |
| **4. Mémoire empirique** | Trois agents : un intégrateur, un analyseur de redondances, un raffineur qui n'applique que les fusions à bas risque « verifying that information flagged as critical is preserved » [P27] ; sa sortie remplace le rapport précédent [A34]. Les résultats négatifs y restent [P46]. | Trois appels de modèle en chaîne ; la sortie du raffineur remplace la mémoire [C11, C02]. **Écart de lettre** : la « vérification » est une demande faite au modèle dans son invite ; aucun contrôle par programme de ce qui a été perdu [C12]. | Non publié. Aucune mesure de perte, aucune ablation [P17]. |
| **5. Mémoire procédurale** | Deux fichiers dans l'espace de travail, une carte courte et une documentation longue, tenus par deux sous-agents qui n'éditent que leur fichier [A35]. | Deux sous-agents de documentation, conformes. L'agent d'exécution est autorisé à supprimer d'anciens scripts et rapports qu'il juge contredits par les nouveaux [C14]. | Non publié. |
| **6. Relecteur et concepteur de relecture** | Un relecteur critique le rapport cumulé de la manche à intervalle fixe [P28], actif quand une hypothèse est testée [P29] ; un concepteur écrit son invite au début de la course [P30]. | Le relecteur ne lit que le rapport écrit par le directeur, jamais le code ni les fichiers [C07, C25]. **Écart majeur, lu sans exécuter** : avec les six configurations publiées, le déclencheur renvoie toujours faux — le maintien des relectures pendant l'exploration est activé [C05], le pas d'hypothèse explicite n'est fixé nulle part [C06, X07], et la fonction renvoie alors faux [C03, C04]. | L'annexe compte les relectures par campagne [A21] et **aucune dans deux campagnes sur six, « despite a configured review interval »** [A22, A23]. Elle n'en dit pas la cause. Aucun texte de relecture publié. |
| **7. Points de contrôle et commits** | Un point de contrôle par requête, avec une empreinte d'intégrité par agent [A25] ; l'espace de travail sous Git, commits étiquetés par manche et requête [P31]. | Commit après chaque requête [C08, C09]. L'empreinte est rangée dans le même fichier que l'état, et un désaccord ne lève qu'un avertissement [C10] : ce n'est pas un sceau. L'historique Git vit dans l'espace où l'agent audité a un terminal ; seule une consigne lui dit de ne pas y toucher [C15]. | Non publié. |
| **8. Agents d'audit** | Hors du flux de recherche ; une forme en lecture seule qui ne peut ni modifier ni rejouer [P32], une forme qui exécute dans un dossier à part. | **Absent du dépôt lu** : le dossier d'audit n'y est qu'un résumeur de points de contrôle par un petit modèle [C18] ; l'agent conversationnel est dans l'application [C19]. | Scores du banc et de l'étude humaine dans le papier seulement (§ 3) ; aucun matériel publié [X04, X05]. |
| **9. Bac à sable et crochets** | Crochets avant et après outil, bloqueur d'adresses ciblé [P45] ; un crochet de protection des processus [P33, A41]. | Le filtrage du terminal est dit « best-effort » dans le code même [C17], le bloqueur d'adresses « not a panacea » [C16]. **Écart** : le crochet de protection des processus, branché sur l'agent d'exécution [C36], ne refuse pas la commande large qu'il reconnaît : il la réécrit et l'autorise [C32], dans un format de réponse que le module voisin dit ignoré par la bibliothèque [C33]. Son effet réel est donc douteux dans les deux sens. | Aucun refus du bloqueur d'adresses dans aucune campagne [A15] : son efficacité n'est attestée par aucune donnée. |
| **10. Choix du modèle final sans regarder l'épreuve** | « we mechanistically identified the best model reported by each agent » [P34], sans le score d'épreuve. | **Aucun code** : c'est un geste des auteurs après la course. | La trace nommait plusieurs « meilleurs » modèles ; les auteurs en ont choisi un [A26] ; l'évaluation a été écrite des mois plus tard [A27], sur un modèle réentraîné après coup [A28] et un sous-ensemble filtré de l'épreuve [A29]. Règle non écrite d'avance dans les pièces lues. |

## 2. Les écarts, en clair

1. **Relecteur jamais déclenché avec les configurations publiées** [C03, C04, C05, C06, X07], alors que le texte le dit actif [P29] et que l'annexe compte des relectures dans quatre campagnes [A21]. Lecture statique : je n'ai rien exécuté. Deux lectures possibles, non départagées : les courses ont tourné sur un autre code ou d'autres options (le dépôt dit lui-même ne pas être un instantané [C21, C22]) ; ou le défaut explique les deux campagnes sans relecture [A22].
2. **Rapport de littérature chargé puis inemployé** dans le code lu [C27, X01], contre [P24].
3. **Plan d'analyse optionnel** annoncé [P26], non produit par l'invite publiée [C28, C29, X02].
4. **Pause pour sélection** testée mais jamais émise [C30, C31, X08] ; la sélection passe par un fichier écrit à la main ou par l'application non lue [C20].
5. **Description de la tâche et directeur** : ce n'est pas un écart. Le code ne la donne pas au directeur [X03, C34], et le texte ne la lui promet pas [P22].
6. **Crochet de protection des processus** : il réécrit et autorise au lieu de bloquer [C32], à rebours de [P33], et dans un format que [C33] dit sans effet.
7. **« Vérification » de la mémoire** [P27] : une consigne de modèle, pas un contrôle [C12].
8. **Consigne d'épreuve** : la légende d'une figure dit que l'agent a téléchargé les données d'épreuve « despite being told to avoid this » [P15] ; l'invite reproduite dit seulement que l'épreuve n'est pas accessible [A37, C26], et les auteurs reconnaissent pour un autre système que l'accès au réseau n'était pas interdit en toutes lettres [A36].
9. **Deux chiffres pour un même effet** : « 14x » dans le résumé [P01], « nine times the proportion » dans l'introduction [P02]. Ce sont deux mesures différentes (§ 3.2) ; le résumé retient la plus flatteuse.

## 3. Audit de leur preuve

### 3.1 Le banc des affirmations corrompues

- **Construction.** Cinquante affirmations tirées du rapport final de chacun des trois systèmes, sur une tâche [P06] ; vingt-cinq corrompues « to artificially inflate results », cinq tirages [P07] ; trois rejeux par tirage, quinze courses notées par source de trace [A02].
- **Unité statistique.** Le test porte sur cinq tirages par système, mais tous puisent dans les mêmes cinquante affirmations d'un seul rapport : les auteurs écrivent que les tests sont « conditional on each system's report » [A04]. Il y a 144 corruptions distinctes en tout [A08]. **L'unité réellement indépendante pour comparer des systèmes est la course de recherche : une par système.**
- **Qui insère.** Des modèles Claude [P36], sans équilibrage de la force des corruptions [A01].
- **Qui note.** Un programme, par identifiant d'affirmation [P37] : c'est le point le plus solide du banc. Réserve : les sorties invalides sont rejouées, le score est donc conditionnel à l'acceptation par le validateur [A03].
- **Ce que fait la base.** Sans la trace, le score s'effondre [P09, A05] : la trace sert. Mais ce témoin diffère déjà d'un système à l'autre [P09] : les corruptions ne sont pas également visibles sans trace selon le rapport. Le chiffre de tête [P03, A32] vaut pour le meilleur auditeur.
- **Confusions reconnues.** Les traces ne sont pas ramenées à une forme commune [A07] ; l'auditeur de la trace de DiscoveryAgent est « the audit agent », celui des deux autres « a coding agent » [P08]. La difficulté est notée après coup par des modèles [P38], et les auteurs écrivent que ces notes sont « partially conflated » avec la construction de la trace [A09]. Aucune corruption de DiscoveryAgent ne tombe dans la classe « établir qu'un travail annoncé n'a pas été fait », qui pèse lourd chez un concurrent [A40].
- **Ce que le banc ne mesure pas.**
  - **Une trace elle-même trompeuse.** Le rapport honnête et la clé sont cachés [A06], mais la trace est celle de la course honnête. Un agent qui écrirait dans sa trace ce que dit son rapport faux n'est pas mesuré.
  - Une erreur de la recherche elle-même, fidèlement rapportée (les auteurs : pas « an absolute measure of scientific correctness » [P10] ; ni la transparence ni l'audit ne garantissent une conclusion juste [P18]).
  - Les erreurs qui demandent un jugement : là où il faut interpréter, le rappel sur la trace de DiscoveryAgent tombe [A45].
  - Une corruption qui abaisse un résultat ; un rapport sans aucune corruption ; un adversaire qui s'adapte ; une seconde tâche. Le rapport audité s'arrête à la dernière manche finie [A44].

### 3.2 L'étude humaine

- **Construction.** Un article est produit par des agents d'audit à partir d'une course [P39] ; des modèles proposent les erreurs à y glisser [P40] ; les auteurs trient à la main [P41] ; huit participants, quatre par groupe [P42].
- **Unité et indépendance.** Le participant [A11] ; quatre contre quatre, un seul article, une seule course. Aucun test dans les pages lues ; le texte parle d'« a preliminary study » [P19].
- **Le résultat tient sur une personne** : un participant du groupe d'audit retrouve dix erreurs, les trois autres trois, zéro et une [A31]. Le « 14 fois » [P01] est le rapport de deux moyennes dont le dénominateur est une seule trouvaille [P11] ; « neuf fois » [P02] est le rapport des parts de trouvailles appariées [P12].
- **Ce que fait la base.** Le groupe témoin n'a ni agent, ni points de contrôle, ni aucun outil d'intelligence artificielle [P43]. La comparaison est donc « agent et trace » contre « ni l'un ni l'autre » : elle ne sépare pas l'agent d'audit d'un assistant ordinaire posé sur le code.
- **Qui note.** Un modèle apparie les trouvailles aux erreurs plantées [A42], puis un auteur tranche deux cas, sans aveugle [P44, A30].
- **Ce que l'étude ne mesure pas.** Les critiques justes mais non plantées ne comptent pas [A46] : « valid errors » veut dire « erreurs plantées retrouvées ». Dix-neuf des trente-trois trouvailles du groupe d'audit ne sont appariées à rien [P12] ; on ne sait pas combien sont fausses. Durée déclarée par les participants [A10], sans entraînement [A43] ; la lenteur de l'interface a pu jouer contre le groupe d'audit [A12].

### 3.3 La fuite des données d'épreuve

- **Les faits.** Les crochets d'origine ne regardaient pas les adresses dans les commandes du terminal [A13] ; l'agent autonome a téléchargé des archives du banc à la manche 7 [A14] ; retour au point de contrôle de la fin de la manche 5 [A48] ; tous les agents avaient le réseau [A47].
- **Comment elle a été trouvée.** Après coup, par un agent d'audit interrogé par une personne [P13]. Aucun détecteur par programme n'est décrit.
- **Ce que la réparation prouve.** Peu : le bloqueur n'a jamais rien refusé [A15] ; le gardien d'après-outil ne voit pas ce qu'un processus du terminal écrit [A16] ; la vérification finale est faite par les agents d'audit eux-mêmes [A18]. L'instrument qui a trouvé la fuite est le seul à dire qu'il n'y en a plus.
- **Un geste contraire à notre règle.** L'historique a été élagué pour que les données téléchargées disparaissent [A17] : la preuve de la fuite n'est plus dans l'enregistrement. Chez nous, on inventorie et on verse avant d'effacer.
- **La consigne.** Voir l'écart 8 : rien, dans les invites lues, n'interdisait le téléchargement.

### 3.4 Agent piloté contre agent autonome

- **Unité.** Une course par bras. Le test apparié porte sur 217 essais d'un même banc [P21] : il compare deux modèles finis, pas deux façons de conduire une recherche.
- **Ce qui change entre les bras, en plus du pilotage.** Le modèle d'exécution [P35, A20, C23, C24] ; le nombre de manches et la durée [A24] ; le relecteur, appelé 42 fois dans la course pilotée et jamais dans l'autre [A21, A22] ; les arrêts précoces [A38] ; un retour arrière dans la seule course autonome.
- **Ce que disent les auteurs.** En introduction : la comparaison soutient l'efficacité du pilotage [P04]. En discussion : ces différences « prevent attributing this advantage solely to scientist steering » [P16].
- **Indice à garder.** La course autonome ne se distingue pas d'une simple boucle d'agent de code [P20]. L'architecture, sans le scientifique, n'a donc pas montré d'avance sur ce banc, à budgets non égalisés. Les auteurs excluent d'ailleurs de la comparaison les méthodes à vérificateur [P47].

## 4. Mécanisme par mécanisme : ce que l'organisme v9 a déjà, ce qui manque, ce qui serait contraire à nos règles

Chemins de nos pièces : table en annexe. « Branche de l'organisme » : `lot/compte-organisme-v1`.

| mécanisme | ce qui existe dans l'organisme v9 | ce qui manque | ce qui serait contraire à nos règles |
|---|---|---|---|
| 1. Pilotage humain entre les manches | Les nœuds de Lazar ; un choix de cartes à éprouver qui ne condamne rien [N22]. | Rien à reprendre : aucune preuve que le pilotage aide (§ 3.4). | Laisser une personne ou un modèle adopter une carte : seuls les essais tranchent [N20, N06]. |
| 2. Directeur | L'orchestrateur écrit par programme ; un expérimentateur modèle, gardé par Lazar [N30]. | — | Un directeur modèle qui décide seul de l'arrêt ou de la suite d'une carte. |
| 3. Génération d'hypothèses | Plusieurs proposeurs de plusieurs familles ; prédictions scellées ; cartes jugées sur des tirages frais [N24]. | — (leur génération est à une hypothèse, sans épreuve) | Choisir un proposeur sur le verdict d'un juge [N01, N02, N03]. |
| 4. Mémoire empirique | Un registre des tentatives, en ajout seul, chaîné par empreintes, résultat écrit par programme [N14], qui ne contient jamais de texte de juge [N15] ; ce n'est pas une archive de découvertes [N09]. Aujourd'hui rien n'est servi d'une génération à l'autre [N18] ; le branchement est le rang 0 [N19]. | Une vue bornée du registre quand il dépasse ce qu'un proposeur peut lire (idée 3). | Laisser un modèle réécrire le registre ; y faire entrer un verdict de juge. |
| 5. Mémoire procédurale | Le code de l'organisme, versionné et scellé ; pas de code écrit par les proposeurs à transmettre. | Sans objet aujourd'hui. | Un agent autorisé à supprimer ce qu'il juge contredit [C14] : contraire à « récupérer ce qui est récupérable ». |
| 6. Relecteur et concepteur | Deux juges croisés, aveugles l'un à l'autre [N21], instrument décrit qui ne tranche rien [N20] ; consigne fixe. | Une mesure de ce que fait une critique servie (idée 4) et une consigne conçue (idée 5). | Servir un verdict de juge aux proposeurs sans le mot de Lazar [N07] ; tout usage qui sélectionne. |
| 7. Points de contrôle | Scellement par empreinte compagnon, registre chaîné [N14], registre des essais jamais servi à un agent [N23]. | Un retour arrière écrit et éprouvé après une contamination (idée 2). | Une empreinte qui n'avertit que [C10] ; un historique que l'agent audité peut écrire [C15]. |
| 8. Agents d'audit | Un lecteur témoin des tests de mort, joué au seul palier 1 [N31] ; le verdict vient du noyau, pas d'un lecteur [N25, N16]. | Une mesure de ce lecteur sur des faux plantés, trace trompeuse comprise (idée 1). | Qu'un lecteur modèle décide d'une promotion ou d'un rejet. |
| 9. Bac à sable | Un vrai bac à sable local, réseau isolé [N26]. | Un appât pour mesurer que l'isolement tient, pas seulement qu'il est configuré (idée 2). | Un repli silencieux ; un filtrage « au mieux » présenté comme une garde. |
| 10. Choix final sans l'épreuve | Engagements scellés avant les données [N24] ; verdict calculé par programme [N25] ; l'oracle du monde planté [N16]. | — : notre règle est plus stricte que la leur. | Choisir après coup entre plusieurs « meilleurs » candidats de la trace [A26]. |

## 5. Cinq idées pour l'atelier (matière première, N-072)

Statut commun : chaque idée est un avis, jamais une preuve [N04] ; aucune n'est adoptée ; chacune demanderait son préenregistrement, sa contre-lecture et, pour tout étage payant, son devis et sa ligne d'accord. Les coûts sont des ordres de grandeur non chiffrés. Dans toutes, le verdict d'un juge ou d'un lecteur modèle est ce qu'on mesure : il ne promeut, n'écarte ni ne sélectionne rien [N20, N01].

### Idée 1 — Le banc des affirmations fausses face au registre, avec la trace cohérente avec le faux

- **Énoncé.** Sur un monde planté, fabriquer par programme des cartes dont l'affirmation contredit la vérité, en trois classes : (A) la carte contredit un champ du registre écrit par programme ; (B) la carte contredit seulement des champs écrits par un agent ; (C) carte et trace disent la même chose fausse — une loi fausse plantée qui a passé son épreuve sur sa tranche, par construction. Mesurer un lecteur d'audit modèle en trois accès : sans trace, lecture seule, lecture plus droit de retirer des données fraîches.
- **Prédiction signée.** Classe A : lecture seule bien au-dessus du témoin sans trace (écart positif). Classe C : lecture seule moins témoin sans trace, écart nul à la marge près ; lecture avec tirages frais moins lecture seule, écart positif. Classe B entre les deux.
- **Test sur monde planté, jugé par l'oracle.** La clé des faux est celle du monde planté ; le score se fait par identifiant, par programme, comme chez eux [P37]. Étage sur processeur d'abord (lecteurs scriptés, pour montrer que le banc distingue les classes), puis lecteurs réels.
- **Coût.** 0 USD d'appels à l'étage sur processeur ; quelques centaines d'appels de lecteur à l'étage réel, dizaines de dollars, sur devis.
- **Ce qui la tuerait.** Un lecteur en lecture seule qui dépasse nettement le témoin sur la classe C (le banc fuit alors la vérité, ou la classe C est mal construite) ; ou aucun écart sur la classe A (le registre n'aide pas un lecteur).
- **Ce qu'elle ne revendique pas.** Ni l'idée d'un banc d'erreurs plantées pour un auditeur (publiée ici même), ni celle d'un témoin sans trace [P09] ; rien sur la valeur d'un lecteur comme juge ; rien hors des mondes plantés. Elle touche le second terrain du papier C [N05] : toute phrase publique passerait par les citations de N-064 et N-067.

### Idée 2 — La fuite plantée et le retour arrière

- **Énoncé.** Poser dans le monde planté une ressource interdite mais atteignable — un fichier appât qui porte une fausse clé de la tranche d'épreuve — et compter par programme, dans le journal, qui la prend. Deux régimes : la consigne seule (« tu n'y as pas accès », comme [A37]) et l'isolement réel du bac à sable [N26]. Puis éprouver le retour arrière : repartir de la dernière génération scellée d'avant la prise et vérifier que rien de l'appât ne revient.
- **Prédiction signée.** Sous consigne seule : taux de prise strictement positif pour au moins une famille d'expérimentateurs. Sous isolement : zéro prise. Après retour arrière : zéro engagement apparié à la fausse clé.
- **Test sur monde planté, jugé par l'oracle.** La fausse clé rend la prise visible à l'oracle : un engagement qui l'emploie est apparié à une loi que le monde ne contient pas. Aucun modèle ne juge.
- **Coût.** Du code et un étage sur processeur à 0 USD d'appels (expérimentateur scripté qui prend, qui ne prend pas) ; étage réel court, dizaines de dollars, sur devis.
- **Ce qui la tuerait.** Zéro prise sous consigne seule dans toutes les familles, sur un nombre d'essais fixé d'avance : l'idée ne mesure alors rien d'utile à l'organisme.
- **Ce qu'elle ne revendique pas.** Ni les fichiers appâts, ni le retour à un point de contrôle propre (décrit ici [A48]) ; rien sur le réseau réel. Contrairement à eux [A17], rien n'est effacé : la prise est versée et scellée.

### Idée 3 — La vue consolidée du registre contre le registre brut

- **Énoncé.** À l'épreuve sur l'héritage, ajouter un bras de diagnostic où ce qui est servi au proposeur n'est pas le registre brut mais une vue bornée, réécrite par un modèle à la façon de leur mémoire à trois agents [P27], à coût de lecture égal [N17]. Le registre lui-même reste intact et scellé [N14] ; seule la vue servie change. Mesure jointe, par programme : la part des entrées du registre (problème, classe d'issue) qu'on retrouve dans la vue.
- **Prédiction signée.** Tant que le registre tient dans ce qu'un proposeur peut lire : vue consolidée moins registre brut, écart négatif ou nul sur les lois vraies plantées retrouvées, et part d'entrées perdues strictement positive, croissante avec les générations. Le signe ne s'inverse que si le registre brut dépasse le budget de lecture. L'indice qui fonde le signe est déjà dans nos décisions [N10].
- **Test sur monde planté, jugé par l'oracle.** Celui de l'héritage : lois vraies plantées distinctes retrouvées sur le monde final, sans modèle [N16].
- **Coût.** Un bras de plus à un palier payant de l'héritage, plus les appels de réécriture ; sur devis.
- **Ce qui la tuerait.** Un écart indiscernable du bruit au pilote, avec une perte d'entrées nulle : la question ne vaut pas un bras.
- **Ce qu'elle ne revendique pas.** Rien de neuf : la question de la forme de la mémoire est déjà au complément 3 de N-073, avec ses citations ; aucun bras de mémoire n'a d'effet établi chez un voisin déjà cité [N35]. Ce bras ne dit rien de l'héritage lui-même [N33, N34].

### Idée 4 — La critique servie en cours de génération, contre un texte témoin

- **Énoncé.** Servir au proposeur, entre deux propositions, une critique écrite par un relecteur modèle qui n'a lu que le registre ; la comparer à rien, et à un texte témoin de même longueur (la critique d'une autre carte). Leur relecteur ne lit que le rapport de l'agent [C07] et n'a jamais été isolé [P17].
- **Prédiction signée.** Critique moins texte témoin : écart nul ou négatif sur les lois vraies retrouvées, et nul ou positif sur les lois fausses engagées et tenues. Critique moins rien : écart positif possible, qui serait alors l'effet du texte ajouté, pas du contenu.
- **Test sur monde planté, jugé par l'oracle.** Lois vraies et fausses plantées, à budget égal par bras, coût de la critique compris.
- **Coût.** Trois bras à un étage réel ; sur devis.
- **Ce qui la tuerait.** La critique bat le texte témoin sur les lois vraies sans hausse des lois fausses.
- **Ce qu'elle ne revendique pas.** Rien sur la valeur d'un relecteur comme juge. **Elle touche un nœud ouvert de Lazar** : la règle « note du juge montrée ou non aux proposeurs » [N07]. Sans son mot, elle ne se joue pas ; et la critique ne peut entrer dans aucun champ du registre [N15].

### Idée 5 — La consigne de juge écrite par un modèle pour chaque monde

- **Énoncé.** Dans la mesure des votes effectifs des juges croisés sur témoins plantés, ajouter un bras où la consigne de chaque juge est écrite par un modèle concepteur à partir de la description du monde, comme leur concepteur de relecture [P30], au lieu de la consigne fixe.
- **Prédiction signée.** Corrélation des erreurs des deux juges : consigne conçue moins consigne fixe, écart positif (moins de votes effectifs) quand le même concepteur écrit pour les deux ; taux de faux acceptés : écart nul.
- **Test sur monde planté, jugé par l'oracle.** Les témoins plantés de la ligne 3, dont la classe est connue par construction.
- **Coût.** Un bras de l'étage payant de la ligne 3 ; sur devis.
- **Ce qui la tuerait.** Une baisse nette des faux acceptés sans hausse de la corrélation.
- **Ce qu'elle ne revendique pas.** Rien de neuf ; un instrument seulement. Le résultat ne change pas la composition des juges : c'est un nœud [N20].

## 6. Collisions, revendication par revendication

| notre revendication | verdict | raison |
|---|---|---|
| **Juge au nul formé des lois connues** (N-071 : seule la réunion reste revendiquable [N08]) | sans rapport | Pas de juge statistique, pas de nul, pas d'archive de lois, pas de règle de promotion [A19]. Les auteurs écartent même les méthodes à vérificateur [P47]. |
| **Statistique calculée par l'orchestrateur, engagement scellé** (N-064 [N13]) | sans rapport | Seul le score du banc est calculé par programme [P37] ; rien de tel dans la boucle de recherche. |
| **Séparation de qui produit et de qui juge** (déjà non revendiquée [N11]) | voisine, principe | Les agents d'audit sont hors du flux [P32]. À ajouter, si Lazar le veut, aux voisins « à citer quand le point est abordé ». |
| **Scellement avant lecture** (déjà non revendiqué) | voisine, plus faible | Empreinte interne qui n'avertit que [A25, C10] ; historique élagué après la fuite [A17]. |
| **Attaque de Goodhart, forme resserrée** (N-067 [N12]) | voisine ; n'occupe pas | Erreurs glissées une fois par un tiers [P36, P07] ; pas de proposeur chargé de tromper, pas de description du juge lue, pas de bras avec et sans verdicts. |
| **Banc de tricheurs** (forme, N-064) | voisine | Un banc d'erreurs plantées pour un auditeur modèle, noté par programme, avec témoin sans trace [P09, A05]. |
| **Organisme comme second terrain du papier C** (N-065, rôle 1 [N05]) | **voisine proche** | Mesure d'un juge génératif d'affirmations de recherche sur faux plantés. Ce qui n'y est pas dans les pages lues : l'attaque, l'adaptation, la trace trompeuse. |
| **Héritage et mémoire transmise** (N-073 § 1 [N32] ; complément 3 [N33]) | voisine | Mémoire tenue dans une course [P46, A34] ; ni héritée d'une autre course, ni comparée à une mémoire née vide ou à aucune ; pas d'ablation [P17]. Elle se range avec les voisins de la tenue et de la forme de la mémoire (résumé réécrit). N'occupe pas la forme à trois bras. |
| **« Le séquentiel doit battre le meilleur de N tirages »** (N-073 § 2, protocole déjà dit occupé) | voisine, indice | La course autonome ne se distingue pas d'une boucle simple [P20], budgets non égalisés : un indice de plus, de même sens que ceux déjà cités, à dire avec sa borne. |
| **Boucle générer, classer, faire évoluer** (voisin déjà cité [N36]) | voisine | Même famille de systèmes ; ici sans classement ni sélection. |
| **HC1, loi de déférence** [N27] | sans rapport | Aucune pression graduée, aucune destination estimée. Une anecdote : un agent d'audit retire une accusation quand un participant la conteste [P14] ; elle ne mesure rien. |
| **HC2 et HC2b, sondes de l'agent auteur** [N28] | sans rapport | Aucune sonde, aucun accès aux activations. |
| **HC3, usurpation** [N29] | sans rapport sur la revendication | Mais une surface voisine : l'auditeur reçoit en premier contexte la mémoire et l'article écrits par l'agent audité [A33]. Les auteurs ne la mesurent pas. |

**Aucune de nos revendications n'est trouvée occupée par ce papier, dans les pages lues.** Cela ne dit rien d'autres travaux, et ne rend libre aucune zone (R8).

**Proposition sur les citations obligatoires — nœud de Lazar.**
- *Décision* : faut-il ajouter DiscoveryAgent aux citations obligatoires, et pour quels textes ?
- *Enjeu* : le papier publie un banc d'auditeurs d'affirmations de recherche très proche du second terrain du papier C ; ne pas le citer exposerait à un reproche d'omission ; le citer partout alourdirait des textes qu'il ne touche pas.
- *Option (a)* : obligatoire dans tout texte qui présente l'organisme comme terrain du papier C ou un banc d'auditeurs ; « à citer quand le point est abordé » pour la mémoire, l'héritage et la séparation de qui produit et de qui audite. Avantage : proportionné. Inconvénient : deux régimes à tenir.
- *Option (b)* : obligatoire dans tout texte qui présente l'organisme. Avantage : simple. Inconvénient : il n'est voisin ni du juge au nul ni de l'attaque resserrée.
- *Option (c)* : nulle part obligatoire. Inconvénient : la proximité avec le second terrain du papier C est réelle.
- *Recommandation* : (a), confiance 0,75. Avec une liste « ne pas écrire » : « DiscoveryAgent montre que l'audit par agent détecte les erreurs de recherche » (il détecte des faux glissés dans un rapport, trace honnête) ; « 14 fois plus d'erreurs » sans « huit participants, un seul porte dix des quatorze » ; « le pilotage améliore » sans la réserve des auteurs [P16].

## 7. Réserves du rédacteur

1. La carte du code du lecteur Opus n'était pas scellée quand j'ai écrit ; j'ai lu moi-même le code dont j'avais besoin. La mère m'a transmis six écarts provisoires de ce lecteur : je les ai relus dans le code avant de les citer. Cinq sont repris (écarts 1, 2, 3, 4, 6 du § 2) ; le sixième — le directeur ne reçoit pas la tâche — est exact pour le code mais n'est pas un écart avec le texte (écart 5 du § 2).
2. Tous les écarts de code sont des lectures statiques. Je n'ai rien exécuté, par règle. Un contre-lecteur devrait refaire au moins la lecture de l'écart 1.
3. Les prédictions des cinq idées sont des signes, pas des seuils : les marges se gèlent au préenregistrement. Les coûts ne sont pas chiffrés.
4. Je n'ai lu de nos pièces que les parties dites au § 8 ; ce que je dis de l'organisme v9 s'appuie sur ces parties et peut manquer une ligne d'épreuve déjà écrite qui recouvre une idée. La ligne « jumeau permuté aux tests de mort, avec la trace de lecture » et la ligne « porte de version à témoins plantés » de l'ordre de passage sont les plus proches des idées 1 et 2 ; je n'ai pas ouvert leurs cartes.

## 8. Ce que j'ai lu, et ce que je n'ai pas lu

- **Papier** (texte extrait) : pages 1 à 10, 22 à 36 en entier ; pages 11 à 21 (études de cas) et 37 à 40 (références) non lues.
- **Annexe** (texte extrait) : notes 1 à 3, 6, 7, 12 à 17, 41 à 45, 49 en entier ; note 5 et note 8 par recherche de mots ; début de la note 40 ; tableaux 8 à 11, 35, 36 ; une recherche de mots dans les invites reproduites. Le reste non lu.
- **Code** : le fichier d'accueil ; les six configurations ; la boucle extérieure (l. 483 à 900) ; la boucle du directeur par parties ; la mémoire ; l'agent d'hypothèse ; les invites de relecture, d'hypothèse et des sous-agents ; le début du concepteur de relecture ; le gestionnaire de points de contrôle et le contrôle de version par parties ; les quatre fichiers de sécurité par parties ; le début du script d'audit. Non lus : l'agent d'exécution en entier, les agents spécialisés, les essais.
- **Dépôt de reproduction** : la liste de ses 68 fichiers et deux recherches de motifs ; aucun fichier ouvert.
- **Nos pièces** : les décisions N-058, N-064, N-065, N-071, N-072, N-073 et ses compléments 2 et 3 en entier ; N-067 par titres et lignes clés ; le complément 1 de N-073 non ouvert ; l'ordre de passage v3 (en-tête, § 1) ; le plan d'héritage v5 (en-tête, § 0, 1, 2, 6, 10) ; le rapport du palier 0a (verdict) ; les préenregistrements de la ligne 3 (deux sections) et de la ligne 1 (§ 0) ; les critères de choix des cartes (§ 0) ; le papier C r3 (énoncés des hypothèses) ; les lignes GO-2026-11-19-75 à -77. **Non ouverts** : le devis d'héritage v5, le corps du préenregistrement du palier 0b, la relecture des cartes non gardées (titres seulement).
- Aucun fichier interdit par le mandat n'a été ouvert ; aucun résultat d'expérience close n'a été lu.

