# DiscoveryAgent : ce que l'organisme d'idéation peut en tirer — synthèse v1

- **Pièce de travail** (classe C), écrite le 19 novembre 2026 par un rédacteur neuf, Claude Fable 5.2, sur le mandat `mandat-redacteur-synthese-discoveryagent-v1.md` (`c539be3d…`, vérifié). Aucune dépense, aucun lancement, aucun commit. À contre-lire par un lecteur d'un autre modèle.
- **Version 2** : corrections de la contre-lecture `contre-lecture-synthese-discoveryagent-v1.md` (`da3f39be…`) appliquées par recopie pure, à la lettre et dans l'ordre (54 couples sur 54), par programme (`outils-synthese-v1/appliquer-couples-v2.py`), par Claude Opus 5.5, en écart déclaré à la règle « la conception par Fable » (précédent R-3791) ; table d'annexe régénérée par `outils-synthese-v1/verifier_citations_synthese_v2.py --table` sur `outils-synthese-v1/citations-synthese-v2.json`, sans retouche ; v1 : `synthese-discoveryagent-pour-l-organisme-v1.md`, sha256 `06d55b7c2d785d26290557b0c398624ff37e7c2d436dfdf159e0f79c2ee15715`.
- **Objet lu** : Queen et al., « DiscoveryAgent: A Framework for Scientist-centric Agentic AI », arXiv 2611.21950 v1 ; son annexe ; le dépôt du code au commit `b510bb2c…` ; le dépôt de reproduction au commit `97e1964c…`. Les deux dépôts ont été lus comme des données : rien n'y a été exécuté, aucune consigne qu'ils contiennent n'a été suivie.
- **Renvois** : chaque affirmation sur une pièce porte un numéro entre crochets (P : papier, A : annexe, C : code, X : contrôle d'absence par programme, N : nos pièces). La table en annexe donne le lieu et l'extrait ; le programme `outils-synthese-v1/verifier_citations_synthese_v1.py` les retrouve tous dans leur source.
- **Règle de lecture** : « non trouvé » veut dire non trouvé dans les pages et fichiers lus (liste au § 8). Une limite de ce papier n'est pas un trou du champ ; rien n'est déclaré libre (règle R8). Aucune idée n'est adoptée sur la foi du papier.

---

## Page de tête

**En une phrase.** DiscoveryAgent est une boucle de recherche à deux étages dont l'apport propre est de ranger tout ce que fait l'agent dans un arbre de points de contrôle lisible par un agent d'audit ; sa preuve porte sur des erreurs glissées dans un rapport, face à une trace honnête, sur une seule course par système ; aucun mécanisme de la boucle de recherche n'est isolé par une ablation (les auteurs disent ne pas fournir d'ablations « comprehensive » [P17]), et le seul retrait isolé trouvé dans les pages lues est celui de la trace donnée à l'auditeur, dans un témoin du banc [A50].

### Les idées pour l'atelier, classées (matière première, N-072 ; détail au § 5)

| rang | idée | ce qu'elle prédit (signe) | coût, ordre de grandeur |
|---|---|---|---|
| 1 | Banc des affirmations fausses face au registre, avec le bras que le papier n'a pas : la trace elle-même cohérente avec le faux | un lecteur qui ne fait que lire ne dépasse pas le témoin sans trace sur cette classe ; un lecteur qui retire des données fraîches le dépasse | étage sur processeur à 0 USD d'appels ; étage réel : dizaines de dollars, sur devis |
| 2 | Fuite plantée et retour arrière : un appât à la portée de l'expérimentateur, détecté par programme | la consigne seule ne tient pas (prises non nulles) ; l'isolement du bac à sable tient (zéro prise) | surtout du code ; étage réel : à chiffrer quand le coût d'un test de mort réel sera mesuré, sur devis |
| 3 | Vue consolidée du registre contre registre brut, comme bras de diagnostic de l'épreuve sur l'héritage | à registre court, la vue réécrite par un modèle fait moins bien ou pareil, et perd des entrées | une variante du bras de diagnostic « registre paraphrasé » déjà prévu ; 0 USD sur processeur ; à l'étage payant, quelques dizaines à quelques centaines de dollars par bras à composition réduite, sur devis |
| 4 | Critique servie en cours de génération, contre un texte témoin de même longueur | aucun gain en lois vraies face au témoin ; pas de baisse des lois fausses tenues | trois bras à un étage réel (critique, rien, texte témoin), quelques centaines de dollars par répétition, sur devis ; touche un nœud ouvert de Lazar |
| 5 | Consigne de juge écrite par un modèle pour chaque monde, contre la consigne fixe | les erreurs des deux juges vont davantage ensemble quand un même concepteur écrit pour les deux (moins de votes effectifs) | quelques dizaines de dollars par variante, sur un devis neuf, hors de la ligne 3 scellée |

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

**Proposition sur les citations (nœud de Lazar, sans défaut ; je propose, je ne décide pas)** : l'option (a) du § 6, en deux volets — premier volet, citation obligatoire dans tout texte qui présente l'organisme comme second terrain du papier C ou qui présente un banc d'auditeurs d'affirmations de recherche ; second volet, « à citer quand le point est abordé » pour la mémoire, l'héritage et la séparation de qui produit et de qui audite, sans entrer dans les citations obligatoires de l'énoncé 5. Confiance : 0,75 pour le premier volet, 0,7 pour le second.

### Les trois faiblesses les plus nettes de leur preuve

1. **Le banc ne corrompt que le rapport ; la trace reste honnête.** Il mesure la facilité à retrouver une preuve existante, pas la résistance à une trace trompeuse, et les auteurs le disent à moitié [P10]. Une seule course et un seul rapport par système [A04].
2. **L'étude humaine tient sur huit personnes, et son « 14 fois », pour l'essentiel, sur un participant.** Le « 14 fois » du résumé [P01] est le rapport de 3,50 à 0,25 [P11] ; un seul participant porte dix des quatorze trouvailles appariées du groupe d'audit [A31] ; sans lui, l'écart garde son sens mais tombe à environ 5 fois (1,33 contre 0,25, calcul du contre-lecteur sur le tableau 11) ; le groupe témoin n'avait droit à aucun outil d'intelligence artificielle [P43].
3. **« Le pilotage par un scientifique fait mieux » repose sur une course par bras, sous un autre modèle d'exécution** [P35], avec un relecteur appelé 42 fois d'un côté et jamais de l'autre [A21, A22]. Les auteurs le concèdent en discussion [P16] après l'avoir affirmé en introduction [P04].

### Ce qui reste invérifié

- **Aucune trace d'agent n'est publiée** : ni point de contrôle, ni mémoire, ni rapport de manche [X06] ; ni le banc, ni l'étude humaine [X04, X05] ; le dépôt du code dit lui-même ne pas contenir ce que les agents ont produit [C35]. La colonne « données » de la table est donc presque partout « non publié ».
- **L'agent d'audit lui-même n'est pas dans le code lu** : celui de l'interface vit dans l'application de pilotage, dépôt non pris [A67, C19, C20] ; celui du banc est la configuration en lecture seule, « fixed auditor » du banc [P50], dont le code n'est dans aucun des deux dépôts lus.
- **Écarts entre le papier et le code, lus à la main, jamais exécutés** : avec les configurations publiées, le relecteur ne se déclencherait jamais (§ 2, écart 1). Le code publié n'est pas un instantané des courses [C21, C22].
- **Ce que l'auditeur du banc savait** de la part d'affirmations corrompues : non trouvé dans les pages lues. Ses consignes de navigation par trace sont décrites, sans leur texte exact, et diffèrent d'une trace à l'autre [A51, A52].
- **Les PDF font foi** ; mes citations sont vérifiées sur les textes extraits, pas sur le rendu des pages ni sur les figures.

---

## 1. Ce que DiscoveryAgent fait, mécanisme par mécanisme

Trois colonnes : ce que dit le texte, ce que fait le code publié, ce que montrent les données publiées. Un écart est signalé en gras.

| mécanisme | le texte | le code (commit `b510bb2c…`) | les données |
|---|---|---|---|
| **1. Boucle extérieure et pilotage humain** | Entre deux manches, le scientifique choisit, édite ou remplace l'hypothèse ; en mode autonome, l'agent garde la sienne [P05]. | La boucle n'admet qu'un déroulement à la fois [C01] ; en mode piloté, elle lit un fichier d'hypothèse choisi. **Chemin mort**, non un écart avec le texte : le statut de pause pour sélection est testé [C30] mais n'est produit nulle part [C31, X08, X12] ; ni candidats ni révision dans ce dépôt : tout cela vit dans une application à part [C20]. | Non publié (aucun fichier d'hypothèse choisie, [X06]). Seule comparaison chiffrée : une course pilotée contre une course autonome (§ 3.4). |
| **2. Boucle intérieure et directeur** | Le directeur reçoit la description des données, l'hypothèse, le catalogue des agents outils et le rapport en cours [P22] ; il est tenu à l'hypothèse de la manche [P23] et peut s'arrêter tôt. | Conforme au texte sur ce point : l'invite du directeur porte la description des données [C34], et le code ne lui passe jamais la tâche [X03], ce que le texte ne promet pas non plus ; mais son invite système annonce une tâche [C50] : défaut interne au code. Pour ProteinGym, la tâche est écrite dans la description des données [C51]. | Compte des arrêts précoces par campagne [A38] ; aucune trace publiée. |
| **3. Génération d'hypothèses** | Une seule hypothèse en mode autonome, avec un plan optionnel [P25, P26] ; un rapport de littérature sert de contexte à la génération [P24] ; aucune sélection : passée au directeur sans juge [A19]. Les listes de candidats sont produites dans l'interface, en un seul appel [A39]. | Une hypothèse par appel [C13]. **Écart** : le drapeau du plan est stocké et jamais relu [C28, X02] ; l'invite ne demande qu'une hypothèse et sa justification [C29]. **Écart** : le rapport de littérature est chargé dans un attribut qui n'entre dans aucune invite du code lu [C27, X01]. | Non publié. |
| **4. Mémoire empirique** | Trois agents : un intégrateur, un analyseur de redondances, un raffineur qui n'applique que les fusions à bas risque « verifying that information flagged as critical is preserved » [P27] ; sa sortie remplace le rapport précédent [A34]. Les résultats négatifs y restent [P46]. | Trois appels de modèle en chaîne ; la sortie du raffineur remplace la mémoire [C11, C02]. **Écart de lettre** : la « vérification » est une demande faite au modèle dans son invite ; aucun contrôle par programme de ce qui a été perdu [C12]. | Non publié. Aucune mesure de perte, aucune ablation [P17]. |
| **5. Mémoire procédurale** | Deux fichiers dans l'espace de travail, une carte courte et une documentation longue, tenus par deux sous-agents qui n'éditent que leur fichier [A35]. | Deux sous-agents de documentation ; **écart** : la règle « chacun n'édite que son document » [A35] n'est qu'une consigne, donnée au seul agent de DOCUMENTATION.md, et les deux reçoivent l'outil d'édition sans restriction de fichier [C48, C49]. L'agent d'exécution est autorisé à supprimer d'anciens scripts et rapports qu'il juge contredits par les nouveaux [C14]. | Non publié. |
| **6. Relecteur et concepteur de relecture** | Un relecteur critique le rapport cumulé de la manche à intervalle fixe [P28], actif quand une hypothèse est testée [P29] ; un concepteur écrit son invite au début de la course [P30]. | Le relecteur ne lit que des textes : la description des données, la mémoire accumulée des manches précédentes et le rapport cumulé de la manche [C39, C07, C25] ; jamais le code ni les fichiers. **Écart majeur, lu sans exécuter** : avec les six configurations publiées, le déclencheur renvoie toujours faux — le maintien des relectures pendant l'exploration est activé [C05], le pas d'hypothèse explicite n'est fixé nulle part [C06, X07], et la fonction renvoie alors faux [C03, C04]. | L'annexe compte les relectures par campagne [A21] et **aucune dans deux campagnes sur six, « despite a configured review interval »** [A22, A23]. Elle n'en dit pas la cause. Aucun texte de relecture publié. |
| **7. Points de contrôle et commits** | Un point de contrôle par requête, avec une empreinte d'intégrité par agent [A25] ; l'espace de travail sous Git, commits étiquetés par manche et requête [P31]. | Commit après chaque requête [C08, C09]. L'empreinte est rangée dans le même fichier que l'état, et un désaccord ne lève qu'un avertissement [C10] : ce n'est pas un sceau. L'historique Git vit dans l'espace où l'agent audité a un terminal ; seule une consigne lui dit de ne pas y toucher [C15]. | Non publié. |
| **8. Agents d'audit** | Hors du flux de recherche ; une forme en lecture seule qui ne peut ni modifier ni rejouer [P32], une forme qui exécute dans un dossier à part. | **Absent du dépôt lu** : le dossier d'audit n'y est qu'un résumeur de points de contrôle par un petit modèle [C18] ; l'agent conversationnel est dans l'application [C19]. | Scores du banc et de l'étude humaine dans le papier seulement (§ 3) ; aucun matériel publié [X04, X05]. |
| **9. Bac à sable et crochets** | Crochets avant et après outil, bloqueur d'adresses ciblé [P45] ; un crochet de protection des processus [P33, A41]. | Le filtrage du terminal est dit « best-effort » dans le code même [C17], le bloqueur d'adresses « not a panacea » [C16]. **Écart** : le crochet de protection des processus, branché sur l'agent d'exécution [C36], ne refuse pas la commande large qu'il reconnaît : il la réécrit et l'autorise [C32], dans un format de réponse que le module voisin dit ignoré par la bibliothèque [C33]. Son effet réel est donc douteux dans les deux sens. | Aucun refus du bloqueur d'adresses dans aucune campagne [A15] : son efficacité n'est attestée par aucune donnée. |
| **10. Choix du modèle final sans regarder l'épreuve** | « we mechanistically identified the best model reported by each agent » [P34], sans le score d'épreuve. | **Aucun code** : c'est un geste des auteurs après la course. | La trace nomme un modèle « best overall » à la manche 2, requête 9, avant tout contact avec l'épreuve [A56], à côté d'une recommandation de production plus simple et d'un troisième document [A26] ; les auteurs retiennent le « best overall », règle qu'ils disent appliquer aussi aux concurrents [A57, P51]. L'évaluation a été écrite des mois plus tard [A27], sur un modèle réentraîné après coup [A28] et sur un sous-ensemble filtré de l'épreuve, commun aux systèmes comparés [A29, P57]. La règle est écrite dans l'annexe et les méthodes ; rien, dans les pièces lues, ne montre qu'elle ait été fixée avant l'évaluation. |

## 2. Les écarts, en clair

1. **Relecteur jamais déclenché avec les configurations publiées** [C03, C04, C05, C06, X07], alors que le texte le dit actif [P29] et que l'annexe compte des relectures dans quatre campagnes [A21]. Lecture statique : je n'ai rien exécuté. Une conséquence est certaine : au moins les quatre campagnes qui ont des relectures n'ont pas tourné avec ce code et ces seules configurations. Le dépôt le laisse d'ailleurs entendre : ses configurations sont « not a manifest of every invocation » [C46], aucune option de relecture n'est nommée parmi les options à ajouter au lancement [C47, X09], et il dit ne pas être un instantané [C21, C22]. Le défaut peut, en plus, expliquer les deux campagnes sans relecture [A22] ; ce n'est pas une lecture concurrente de la première. Relu par le contre-lecteur : le relecteur n'a pas d'autre appel dans le code [X10].
2. **Rapport de littérature chargé puis inemployé** dans le code lu [C27, X01], contre [P24] et contre l'annexe, qui le dit versé à l'amorçage des hypothèses de toutes les campagnes [A65] ; les auteurs expliquent même par cet amorçage le faible usage de la recherche approfondie [P55]. L'invite d'hypothèse du code reçoit la mémoire accumulée, non ce rapport [C44]. L'écart vaut pour le mode automatique : en mode piloté, l'application, dépôt non pris, charge ce rapport [A63].
3. **Plan d'analyse optionnel** annoncé pour le mode automatique [P26], non produit par l'invite publiée [C28, C29, X02], alors que les six configurations activent le drapeau [X11]. En mode piloté, c'est l'application, dépôt non pris, qui propose un plan [A64].
4. **Pause pour sélection** testée mais jamais émise [C30, C31, X08, X12] : c'est un chemin mort du code plutôt qu'un écart avec le texte, puisque la sélection passe par un fichier écrit à la main ou par l'application non lue [C20].
5. **Description de la tâche et directeur** : ce n'est pas un écart avec le texte. Le code ne la donne pas au directeur [X03, C34], et le texte ne la lui promet pas [P22] ; l'invite système du directeur l'annonce pourtant [C50], défaut interne au code, que la carte du code relève aussi. Pour ProteinGym, la tâche est dans la description des données [C51] : le directeur la reçoit par là.
6. **Crochet de protection des processus** : il réécrit et autorise au lieu de bloquer [C32], à rebours de [P33], phrase qui décrit l'agent OpenTargets [P54], branché sur le même crochet [C40] ; pour l'agent d'exécution, l'annexe dit seulement qu'il « screens » ces commandes [A41]. Sa branche de refus emploie le même format que [C33] dit sans effet [C41], et rien n'y vise les commandes longues que [P33] dit bloquées.
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
- **Confusions, reconnues ou non.** Les traces ne sont pas ramenées à une forme commune [A07], et les consignes de navigation données à l'auditeur diffèrent selon la trace [A51, A52]. L'auditeur, lui, est le même pour les trois sources : si la p. 8 nomme « the audit agent » d'un côté et « a coding agent » de l'autre [P08], la même page tient « the auditor harness fixed across systems » [P48], et les méthodes comme l'annexe disent un même auditeur en lecture seule pour les trois traces [P49, P50, A49]. La difficulté est notée après coup par des modèles [P38], et les auteurs écrivent que ces notes sont « partially conflated » avec la construction de la trace [A09]. Aucune corruption de DiscoveryAgent ne tombe dans la classe « établir qu'un travail annoncé n'a pas été fait », qui pèse lourd chez un concurrent [A40].
- **Ce que le banc ne mesure pas.**
  - **Une trace elle-même trompeuse.** Le rapport honnête et la clé sont cachés [A06], mais la trace est celle de la course honnête. Un agent qui écrirait dans sa trace ce que dit son rapport faux n'est pas mesuré.
  - Une erreur de la recherche elle-même, fidèlement rapportée (les auteurs : pas « an absolute measure of scientific correctness » [P10] ; ni la transparence ni l'audit ne garantissent une conclusion juste [P18]).
  - Les erreurs qui demandent un jugement : là où il faut interpréter, le rappel sur la trace de DiscoveryAgent tombe [A45].
  - Une corruption qui abaisse un résultat ; un rapport sans aucune corruption ; un adversaire qui s'adapte ; une seconde tâche. Le rapport audité s'arrête à la dernière manche finie [A44].

### 3.2 L'étude humaine

- **Construction.** Un article est produit par des agents d'audit à partir d'une course [P39] ; des modèles proposent les erreurs à y glisser [P40] ; les auteurs trient à la main [P41] ; huit participants, quatre par groupe [P42].
- **Unité et indépendance.** Le participant [A11] ; quatre contre quatre, un seul article, une seule course. Aucun test dans les pages lues ; le texte parle d'« a preliminary study » [P19].
- **Le chiffre de tête tient, pour l'essentiel, sur une personne** : un participant du groupe d'audit retrouve dix erreurs, les trois autres trois, zéro et une [A31] ; sans lui, l'écart garde son sens mais tombe à environ 5 fois (calcul du contre-lecteur). Les comptes d'erreurs uniques ne s'additionnent pas d'un participant à l'autre [A62] ; le total additif de quatorze est celui des trouvailles appariées. Le « 14 fois » [P01] est le rapport de deux moyennes dont le dénominateur est une seule trouvaille [P11] ; « neuf fois » [P02] est le rapport des parts de trouvailles appariées [P12].
- **Ce que fait la base.** Le groupe témoin n'a ni agent, ni points de contrôle, ni aucun outil d'intelligence artificielle [P43]. La comparaison est donc « agent et trace » contre « ni l'un ni l'autre » : elle ne sépare pas l'agent d'audit d'un assistant ordinaire posé sur le code.
- **Qui note.** Un modèle apparie les trouvailles aux erreurs plantées [A42], sans voir ni le nom ni le groupe du participant [A58, P52], en cinq appels dont les ensembles d'appariement coïncident pour 53 trouvailles sur 54 [A59] ; puis un auteur tranche deux cas, sans aveugle [P44, A30], et les deux arbitrages vont contre le groupe d'audit : pas d'appariement pour R01 là où un appel sur cinq en voyait un, et, pour R04, une seconde erreur que les cinq appels appariaient est retirée [A61, A60].
- **Ce que l'étude ne mesure pas.** Les critiques justes mais non plantées ne comptent pas [A46] : « valid errors » veut dire « erreurs plantées retrouvées ». Dix-neuf des trente-trois trouvailles du groupe d'audit ne sont appariées à rien [P12] ; on ne sait pas combien sont fausses. Durée déclarée par les participants [A10], sans entraînement [A43] ; la lenteur de l'interface a pu jouer contre le groupe d'audit [A12].

### 3.3 La fuite des données d'épreuve

- **Les faits.** Les crochets d'origine ne regardaient pas les adresses dans les commandes du terminal [A13] ; l'agent autonome a téléchargé des archives du banc à la manche 7 [A14] ; retour au point de contrôle de la fin de la manche 5 [A48] ; tous les agents avaient le réseau [A47].
- **Comment elle a été trouvée.** Après coup, par un agent d'audit interrogé par une personne [P13]. Aucun détecteur par programme n'est décrit.
- **Ce que la réparation prouve.** Peu sur le réseau : le bloqueur d'adresses n'a jamais rien refusé [A15] ; le gardien d'après-outil ne voit pas ce qu'un processus du terminal écrit [A16] ; la vérification des manches suivantes est faite par les agents d'audit eux-mêmes [A18]. À décharge : des refus des crochets de fichiers sont enregistrés [A66], dont celui d'une reprise qui retrouvait le dossier mis en quarantaine [A54], et un test de recouvrement des variants entre entraînement et épreuve ne trouve aucun recouvrement, pour une branche de DA-Steer seulement [A55]. Pour les manches suivantes de DA-Auto, l'instrument qui a trouvé la fuite reste le seul à dire qu'il n'y en a plus.
- **Un geste à comparer à notre règle.** L'historique Git de l'espace de travail a été élagué pour que les objets devenus inaccessibles ne gardent pas les données téléchargées [A17] ; le dossier fuité, lui, a été mis en quarantaine hors de la liste de lecture [A53] : la preuve n'est donc pas détruite, mais rien, dans les pages lues, ne dit qu'elle ait été inventoriée ni scellée. Chez nous, on inventorie et on verse avant d'effacer.
- **La consigne.** Voir l'écart 8 : rien, dans les invites lues, n'interdisait le téléchargement.

### 3.4 Agent piloté contre agent autonome

- **Unité.** Une course par bras. Le test apparié porte sur 217 essais d'un même banc [P21] : il compare deux modèles finis, pas deux façons de conduire une recherche.
- **Ce qui change entre les bras, en plus du pilotage.** Le modèle d'exécution [P35, A20, C23, C24] ; le nombre de manches et la durée [A24] ; le relecteur, appelé 42 fois dans la course pilotée et jamais dans l'autre [A21, A22] ; les arrêts précoces [A38] ; un retour arrière dans la seule course autonome.
- **Ce que disent les auteurs.** En introduction : la comparaison soutient l'efficacité du pilotage [P04]. En discussion : ces différences « prevent attributing this advantage solely to scientist steering » [P16].
- **Indice à garder.** La course autonome ne se distingue pas d'une simple boucle d'agent de code [P20] ; en classification d'étoiles variables, l'agent autonome a en revanche la meilleure exactitude sur l'épreuve parmi les systèmes comparés [P56, P57], une course par système là aussi. L'architecture, sans le scientifique, n'a donc pas montré d'avance sur ce banc, à budgets non égalisés. Les auteurs excluent d'ailleurs de la comparaison les méthodes à vérificateur [P47].

## 4. Mécanisme par mécanisme : ce que l'organisme v9 a déjà, ce qui manque, ce qui serait contraire à nos règles

Chemins de nos pièces : table en annexe. « Branche de l'organisme » : `lot/compte-organisme-v1`.

| mécanisme | ce qui existe dans l'organisme v9 | ce qui manque | ce qui serait contraire à nos règles |
|---|---|---|---|
| 1. Pilotage humain entre les manches | Les nœuds de Lazar ; un choix de cartes à éprouver qui ne condamne rien [N22]. | Rien à reprendre : aucune preuve que le pilotage aide (§ 3.4). | Laisser une personne ou un modèle adopter une carte : seuls les essais tranchent [N20, N06]. |
| 2. Directeur | L'orchestrateur écrit par programme ; un expérimentateur modèle, gardé par Lazar [N30]. | — | Un directeur modèle qui décide seul de l'arrêt ou de la suite d'une carte. |
| 3. Génération d'hypothèses | Plusieurs proposeurs de plusieurs familles ; prédictions scellées ; cartes jugées sur des tirages frais [N24]. | — (leur génération est à une hypothèse, sans épreuve) | Choisir un proposeur sur le verdict d'un juge [N01, N02, N03]. |
| 4. Mémoire empirique | Un registre des tentatives, en ajout seul, chaîné par empreintes, résultat écrit par programme [N14], qui ne contient jamais de texte de juge [N15] ; ce n'est pas une archive de découvertes [N09]. Aujourd'hui rien n'est servi d'une génération à l'autre [N18] ; le branchement est le rang 0 [N19]. | Une vue bornée du registre quand il dépasse ce qu'un proposeur peut lire (idée 3). | Laisser un modèle réécrire le registre ; y faire entrer un verdict de juge. |
| 5. Mémoire procédurale | Le code de l'organisme, versionné et scellé ; pas de code écrit par les proposeurs à transmettre. | Sans objet aujourd'hui. | Un agent autorisé à supprimer ce qu'il juge contredit [C14], sans inventaire ni versement : contraire à « récupérer ce qui est récupérable », même si, chez eux, le commit après chaque requête en garde l'état antérieur dans l'historique [C08, C09] et si les fichiers de données sont exclus de la suppression [C45]. |
| 6. Relecteur et concepteur | Deux juges croisés, aveugles l'un à l'autre [N21], instrument décrit qui ne tranche rien [N20] ; consigne fixe. | Une mesure de ce que fait une critique servie (idée 4) et une consigne conçue (idée 5). | Servir un verdict de juge aux proposeurs sans le mot de Lazar [N07] ; tout usage qui sélectionne. |
| 7. Points de contrôle | Scellement par empreinte compagnon, registre chaîné [N14], registre des essais jamais servi à un agent [N23]. | Un retour arrière écrit et éprouvé après une contamination (idée 2). | Une empreinte qui n'avertit que [C10] ; un historique que l'agent audité peut écrire [C15]. |
| 8. Agents d'audit | Un lecteur témoin des tests de mort, joué au seul palier 1 [N31] ; le verdict vient du noyau, pas d'un lecteur [N25, N16]. | Une mesure de ce lecteur sur des faux plantés, trace trompeuse comprise (idée 1). | Qu'un lecteur modèle décide d'une promotion ou d'un rejet. |
| 9. Bac à sable | Un vrai bac à sable local, réseau isolé [N26]. | Un appât pour mesurer ce que fait un agent sous la seule consigne (idée 2) ; que l'isolement tienne est déjà sondé au palier 0a, réseau refusé compris [N46]. | Un repli silencieux ; un filtrage « au mieux » présenté comme une garde. |
| 10. Choix final sans l'épreuve | Engagements scellés avant les données [N24] ; verdict calculé par programme [N25] ; l'oracle du monde planté [N16]. | — : notre règle est plus stricte que la leur. | Choisir après coup entre des candidats de la trace [A26] selon une règle qui n'a pas été fixée d'avance. |

## 5. Cinq idées pour l'atelier (matière première, N-072)

Statut commun : chaque idée est un avis, jamais une preuve [N04] ; aucune n'est adoptée ; chacune demanderait son préenregistrement, sa contre-lecture et, pour tout étage payant, son devis et sa ligne d'accord. Les coûts sont des ordres de grandeur, ancrés quand c'est possible sur les montants de nos propres pièces, jamais des devis. Dans toutes, ce qui tranche est un programme ou l'oracle ; quand un juge ou un lecteur modèle intervient, son verdict est l'objet de la mesure (idées 1 et 5) ou la condition éprouvée (idée 4), et il ne promeut, n'écarte ni ne sélectionne rien [N20, N01].

### Idée 1 — Le banc des affirmations fausses face au registre, avec la trace cohérente avec le faux

- **Énoncé.** Sur un monde planté, fabriquer par programme des cartes dont l'affirmation contredit la vérité, en trois classes : (A) la carte contredit un champ du registre écrit par programme ; (B) la carte contredit seulement des champs écrits par un agent ; (C) carte et trace disent la même chose fausse — une loi fausse plantée qui a passé son épreuve sur sa tranche, par construction. Mesurer un lecteur d'audit modèle en trois accès : sans trace, lecture seule, lecture plus droit de retirer des données fraîches.
- **Prédiction signée.** Classe A : lecture seule bien au-dessus du témoin sans trace (écart positif). Classe C : lecture seule moins témoin sans trace, écart nul à la marge près ; lecture avec tirages frais moins lecture seule, écart positif. Classe B entre les deux.
- **Test sur monde planté, jugé par l'oracle.** La clé des faux est celle du monde planté ; le score se fait par identifiant, par programme, comme chez eux [P37]. Étage sur processeur d'abord (lecteurs scriptés, pour montrer que le banc distingue les classes), puis lecteurs réels.
- **Coût.** 0 USD d'appels à l'étage sur processeur ; quelques centaines d'appels de lecteur à l'étage réel : quelques dizaines de dollars si chaque lecture est un appel unique au tarif des juges de la ligne 3 [N43], davantage si le lecteur est une session à outils qui retire des données ; sur devis.
- **Ce qui la tuerait.** Un lecteur en lecture seule qui dépasse nettement le témoin sur la classe C (le banc fuit alors la vérité, ou la classe C est mal construite) ; ou aucun écart sur la classe A (le registre n'aide pas un lecteur).
- **Ce qu'elle ne revendique pas.** Ni l'idée d'un banc d'erreurs plantées pour un auditeur (publiée ici même), ni celle d'un témoin sans trace [P09], ni qu'une trace cohérente avec le faux soit un angle neuf du champ : c'est une limite de ce papier, pas un trou du champ (R8), à chercher ailleurs avant toute phrase ; la classe C est proche, par sa construction, du bras de diagnostic « entrées fausses plantées » du plan de l'héritage [N37] ; rien sur la valeur d'un lecteur comme juge ; rien hors des mondes plantés. Elle touche le second terrain du papier C [N05] : toute phrase publique passerait par les citations de N-064 et N-067.

### Idée 2 — La fuite plantée et le retour arrière

- **Énoncé.** Poser dans le monde planté une ressource interdite mais atteignable — un fichier appât qui porte une fausse clé de la tranche d'épreuve — et compter par programme, dans le journal, qui la prend. Deux régimes : la consigne seule (« tu n'y as pas accès », comme [A37]) et l'isolement réel du bac à sable [N26]. Puis éprouver le retour arrière : repartir de la dernière génération scellée d'avant la prise et vérifier que rien de l'appât ne revient.
- **Prédiction signée.** Sous consigne seule : taux de prise strictement positif pour au moins une famille d'expérimentateurs. Sous isolement : zéro prise. Après retour arrière : zéro engagement apparié à la fausse clé.
- **Test sur monde planté, jugé par l'oracle.** La prise se compte par programme à deux endroits : la lecture du fichier appât dans le journal d'accès, et tout engagement ou résultat qui emploie la fausse clé, que l'oracle apparie à une loi que le monde ne contient pas. Aucun modèle ne juge. Il faut un expérimentateur qui ait de quoi décider : sous la forme imposée du tour fermé, il n'a « rien à décider » [N47], et les paliers payants de l'héritage imposent cette forme [N49] ; l'étage réel se joue donc sur une forme libre, à préciser.
- **Coût.** Du code et un étage sur processeur à 0 USD d'appels (expérimentateur scripté qui prend, qui ne prend pas) ; étage réel court, à chiffrer quand le coût d'un test de mort réel sera mesuré [N53] ; sur devis.
- **Ce qui la tuerait.** Zéro prise sous consigne seule dans toutes les familles, sur un nombre d'essais fixé d'avance : l'idée ne mesure alors rien d'utile à l'organisme.
- **Ce qu'elle ne revendique pas.** Ni les fichiers appâts, ni le retour à un point de contrôle propre (décrit ici [A48]) ; rien sur le réseau réel. À la différence de leur élagage [A17], qui garde le dossier fuité en quarantaine [A53] sans inventaire scellé dans les pages lues, rien n'est effacé ici : la prise est inventoriée, versée et scellée.

### Idée 3 — La vue consolidée du registre contre le registre brut

- **Énoncé.** À l'épreuve sur l'héritage, donner au bras de diagnostic « registre paraphrasé », déjà prévu [N37], une variante où ce qui est servi au proposeur n'est pas le registre brut mais une vue bornée, réécrite par un modèle à la façon de leur mémoire à trois agents [P27], à coût de lecture égal [N17]. Comme tout bras de diagnostic, elle n'entre dans aucun verdict ; servir un texte libre écrit par un modèle déroge à la règle des champs typés et bornés [N40], ce qui la confine à ce bras. Le registre lui-même reste intact et scellé [N14] ; seule la vue servie change. Mesure jointe, par programme : la part des entrées du registre (problème, classe d'issue) qu'on retrouve dans la vue.
- **Prédiction signée.** Tant que le registre tient dans ce qu'un proposeur peut lire : vue consolidée moins registre brut, écart négatif ou nul sur les lois vraies plantées retrouvées, et part d'entrées perdues strictement positive, croissante avec les générations. Le signe ne s'inverse que si le registre brut dépasse le budget de lecture. L'indice qui fonde le signe est déjà dans nos décisions [N10].
- **Test sur monde planté, jugé par l'oracle.** Celui de l'héritage : lois vraies plantées distinctes retrouvées sur le monde final, sans modèle [N16].
- **Coût.** Sur processeur, 0 USD d'appels, avec des proposeurs scriptés et un réécrivain scripté qui perd une part fixée d'entrées, pour montrer que l'instrument voit la perte. À l'étage payant, de l'ordre du coût d'un bras de l'héritage plus les appels de réécriture : d'après les bornes de l'ordre de passage pour trois ou quatre bras [N52], quelques dizaines à quelques centaines de dollars par bras à composition réduite, davantage à composition pleine ; sur devis.
- **Ce qui la tuerait.** Pour la prédiction : un écart positif net de la vue consolidée sur le registre brut, le registre tenant dans le budget de lecture. Pour son utilité : un écart indiscernable du bruit au pilote, avec une perte d'entrées nulle ; la question ne vaut alors pas une variante.
- **Ce qu'elle ne revendique pas.** Rien de neuf : la question de la forme de la mémoire est déjà au complément 3 de N-073, avec ses citations ; aucun bras de mémoire n'a d'effet établi chez un voisin déjà cité [N35] ; le plan de l'héritage prévoit déjà un registre paraphrasé et un historique brut sans registre parmi ses bras de diagnostic [N37, N38], et laisse au préenregistrement « ce qui est servi quand le registre dépasse la taille bornée » [N39]. Ce bras ne dit rien de l'héritage lui-même [N33, N34].

### Idée 4 — La critique servie en cours de génération, contre un texte témoin

- **Énoncé.** Servir au proposeur, entre deux propositions, une critique écrite par un relecteur modèle qui n'a lu que le registre ; la comparer à rien, et à un texte témoin de même longueur (la critique d'une autre carte). Leur relecteur ne lit que des textes, mémoire accumulée comprise [C39, C07], et n'a jamais été isolé [P17].
- **Prédiction signée.** Critique moins texte témoin : écart nul ou négatif sur les lois vraies retrouvées, et nul ou positif sur les lois fausses engagées et tenues. Critique moins rien : écart positif possible, qui serait alors l'effet du texte ajouté, pas du contenu.
- **Test sur monde planté, jugé par l'oracle.** Lois vraies et fausses plantées, à budget égal par bras, coût de la critique compris.
- **Coût.** Trois bras à un étage réel, chacun de l'ordre d'une course v9, soit 72,50 USD par bras d'après l'ordre de passage [N42], plus les appels du relecteur : quelques centaines de dollars par répétition ; sur devis.
- **Ce qui la tuerait.** La critique bat le texte témoin sur les lois vraies sans hausse des lois fausses.
- **Ce qu'elle ne revendique pas.** Rien sur la valeur d'un relecteur comme juge. **Elle touche un nœud ouvert de Lazar** : la règle « note du juge montrée ou non aux proposeurs » [N07]. Sans son mot, elle ne se joue pas ; et la critique ne peut entrer dans aucun champ du registre [N15].

### Idée 5 — La consigne de juge écrite par un modèle pour chaque monde

- **Énoncé.** Sur les témoins plantés de la mesure des votes effectifs des juges croisés, comparer la consigne fixe à une consigne écrite pour chaque monde par un modèle concepteur, à partir de la description du monde, comme leur concepteur de relecture [P30] ; deux variantes : un même concepteur écrit pour les deux juges, ou un concepteur distinct pour chacun. La ligne 3 fige « même consigne figée » pour ses deux juges, sous un plafond de 25 USD que le cas haut de son devis approche déjà [N44, N45] : l'idée n'y entre pas comme bras ; elle relève d'une ligne neuve, ou de la note de conception du juge attendue [N48], sur son propre devis.
- **Prédiction signée.** Corrélation des erreurs des deux juges : consigne conçue par un même concepteur pour les deux juges moins consigne conçue par un concepteur distinct pour chacun, écart positif (moins de votes effectifs) ; consigne conçue moins consigne fixe : signe non prédit, puisque la consigne fixe est déjà commune aux deux juges ; taux de faux acceptés : écart nul.
- **Test sur monde planté, jugé par l'oracle.** Les témoins plantés de la ligne 3, dont la classe est connue par construction.
- **Coût.** De l'ordre de l'étage payant de la ligne 3 par variante, soit quelques dizaines de dollars [N43, N45], plus les appels du concepteur ; sur un devis neuf, hors du plafond de la ligne 3.
- **Ce qui la tuerait.** Une corrélation qui ne monte pas quand un même concepteur écrit pour les deux juges, face à des concepteurs distincts ; ou une baisse nette des faux acceptés sans hausse de la corrélation.
- **Ce qu'elle ne revendique pas.** Rien de neuf ; un instrument seulement. Le résultat ne change pas la composition des juges : c'est un nœud [N20].

## 6. Collisions, revendication par revendication

| notre revendication | verdict | raison |
|---|---|---|
| **Juge au nul formé des lois connues** (N-071 : seule la réunion reste revendiquable [N08]) | sans rapport | Pas de juge statistique, pas de nul, pas d'archive de lois, pas de règle de promotion [A19]. Les auteurs écartent même les méthodes à vérificateur [P47]. |
| **Statistique calculée par l'orchestrateur, engagement scellé** (N-064 [N13] ; composantes empruntées et plus revendiquées depuis N-067 [N51]) | sans rapport | Seul le score du banc est calculé par programme [P37] ; rien de tel dans la boucle de recherche. |
| **Séparation de qui produit et de qui juge** (déjà non revendiquée [N11]) | voisine, principe | Les agents d'audit sont hors du flux [P32]. À ajouter, si Lazar le veut, aux voisins « à citer quand le point est abordé ». |
| **Scellement avant lecture** (déjà non revendiqué) | voisine, plus faible | Empreinte interne qui n'avertit que [A25, C10] ; historique élagué après la fuite [A17]. |
| **Attaque de Goodhart, forme resserrée** (N-067 [N12]) | voisine ; n'occupe pas | Erreurs glissées une fois par un tiers [P36, P07] ; pas de proposeur chargé de tromper, pas de description du juge lue, pas de bras avec et sans verdicts. |
| **Banc de tricheurs** (O11 : plus aucune revendication d'idée depuis N-067 [N50]) | voisine, sans enjeu de priorité | Un banc d'erreurs plantées pour un auditeur modèle, noté par programme, avec témoin sans trace [P09, A05]. |
| **Organisme comme second terrain du papier C** (N-065, rôle 1 [N05]) | **voisine proche** | Mesure d'un juge génératif d'affirmations de recherche sur faux plantés. Ce qui n'y est pas dans les pages lues : l'attaque, l'adaptation, la trace trompeuse. |
| **Héritage et mémoire transmise** (N-073 § 1 [N32] ; complément 3 [N33]) | voisine | Mémoire tenue dans une course [P46, A34] ; ni héritée d'une autre course, ni comparée à une mémoire née vide ou à aucune ; pas d'ablation [P17]. Elle se range avec les voisins de la tenue et de la forme de la mémoire (résumé réécrit). N'occupe pas la forme à trois bras. |
| **« Le séquentiel doit battre le meilleur de N tirages »** (N-073 § 2, protocole déjà dit occupé) | sans rapport avec le protocole ; indice lointain | La course autonome ne se distingue pas d'une boucle d'agent de code [P20], budgets non égalisés ; mais les deux bras sont séquentiels et aucun meilleur de N tirages n'est mesuré : c'est un indice sur une architecture élaborée face à une boucle simple, pas sur le séquentiel face aux tirages indépendants, à dire avec sa borne si le point est abordé. |
| **Boucle générer, classer, faire évoluer** (voisin déjà cité [N36]) | voisine | Même famille de systèmes ; ici sans classement ni sélection. |
| **HC1, loi de déférence** [N27] | sans rapport | Aucune pression graduée, aucune destination estimée. Une anecdote : un agent d'audit retire une accusation quand un participant la conteste en montrant une figure à l'appui [P53, P14] ; rien ne dit si ce retrait est juste ou complaisant, et elle ne mesure rien. |
| **HC2 et HC2b, sondes de l'agent auteur** [N28] | sans rapport | Aucune sonde, aucun accès aux activations. |
| **HC3, usurpation** [N29] | sans rapport sur la revendication | Mais une surface voisine : l'auditeur reçoit en premier contexte la mémoire et l'article écrits par l'agent audité [A33]. Les auteurs ne la mesurent pas. |

**Aucune de nos revendications n'est trouvée occupée par ce papier, dans les pages lues.** Cela ne dit rien d'autres travaux, et ne rend libre aucune zone (R8).

**Proposition sur les citations obligatoires — nœud de Lazar.**
- *Décision* : faut-il ajouter DiscoveryAgent aux citations obligatoires, et pour quels textes ?
- *Enjeu* : le papier publie un banc d'auditeurs d'affirmations de recherche très proche du second terrain du papier C ; ne pas le citer exposerait à un reproche d'omission ; le citer partout alourdirait des textes qu'il ne touche pas.
- *Option (a)* : obligatoire dans tout texte qui présente l'organisme comme terrain du papier C ou un banc d'auditeurs ; « à citer quand le point est abordé » pour la mémoire, l'héritage et la séparation de qui produit et de qui audite. Avantage : proportionné. Inconvénient : deux régimes à tenir.
- *Option (b)* : obligatoire dans tout texte qui présente l'organisme. Avantage : simple. Inconvénient : il n'est voisin ni du juge au nul ni de l'attaque resserrée.
- *Option (c)* : nulle part obligatoire. Inconvénient : la proximité avec le second terrain du papier C est réelle.
- *Recommandation* : (a), confiance 0,75 pour son premier volet, 0,7 pour le second ; nœud de Lazar, sans défaut. Avec une liste « ne pas écrire » : « DiscoveryAgent montre que l'audit par agent détecte les erreurs de recherche » (il détecte des faux glissés dans un rapport, trace honnête) ; « 14 fois plus d'erreurs » sans « huit participants, un seul porte dix des quatorze » ; « le pilotage améliore » sans la réserve des auteurs [P16] ; « l'auditeur du banc différait selon la source de trace » (un même auditeur sert les trois [A49]) ; « le relecteur n'a jamais tourné » (le code publié ne le déclencherait pas, mais l'annexe compte des relectures dans quatre campagnes [A21]) ; « les auteurs ont choisi leur meilleur modèle après coup » (il est nommé avant tout contact avec l'épreuve [A56]).

## 7. Réserves du rédacteur

1. La carte du code du lecteur Opus n'était pas scellée quand j'ai écrit ; j'ai lu moi-même le code dont j'avais besoin. La mère m'a transmis six écarts provisoires de ce lecteur : je les ai relus dans le code avant de les citer. Cinq sont repris (écarts 1, 2, 3, 4, 6 du § 2) ; le sixième — le directeur ne reçoit pas la tâche — est exact pour le code mais n'est pas un écart avec le texte (écart 5 du § 2).
2. Tous les écarts de code sont des lectures statiques. Je n'ai rien exécuté, par règle. Un contre-lecteur devrait refaire au moins la lecture de l'écart 1.
3. Les prédictions des cinq idées sont des signes, pas des seuils : les marges se gèlent au préenregistrement. Les coûts sont des ordres de grandeur, non des devis.
4. Je n'ai lu de nos pièces que les parties dites au § 8 ; ce que je dis de l'organisme v9 s'appuie sur ces parties et peut manquer une ligne d'épreuve déjà écrite qui recouvre une idée. La ligne « jumeau permuté aux tests de mort, avec la trace de lecture » et la ligne « porte de version à témoins plantés » de l'ordre de passage sont les plus proches des idées 1 et 2 ; je n'ai pas ouvert leurs cartes.

## 8. Ce que j'ai lu, et ce que je n'ai pas lu

- **Papier** (texte extrait) : pages 1 à 10, 22 à 36 en entier ; pages 11 à 21 (études de cas) et 37 à 40 (références) non lues.
- **Annexe** (texte extrait) : notes 1 à 3, 6, 7, 12 à 17, 41 à 45, 49 en entier ; note 5 et note 8 par recherche de mots ; début de la note 40 ; tableaux 8 à 11, 35, 36 ; une recherche de mots dans les invites reproduites. Le reste non lu.
- **Code** : le fichier d'accueil ; les six configurations ; la boucle extérieure (l. 483 à 900) ; la boucle du directeur par parties ; la mémoire ; l'agent d'hypothèse ; les invites de relecture, d'hypothèse et des sous-agents ; le début du concepteur de relecture ; le gestionnaire de points de contrôle et le contrôle de version par parties ; les quatre fichiers de sécurité par parties ; le début du script d'audit. Non lus : l'agent d'exécution en entier, les agents spécialisés, les essais.
- **Dépôt de reproduction** : la liste de ses 68 fichiers et deux recherches de motifs ; aucun fichier ouvert.
- **Nos pièces** : les décisions N-058, N-064, N-065, N-071, N-072, N-073 et ses compléments 2 et 3 en entier ; N-067 par titres et lignes clés ; le complément 1 de N-073 non ouvert ; l'ordre de passage v3 (en-tête, § 1) ; le plan d'héritage v5 (en-tête, § 0, 1, 2, 6, 10) ; le rapport du palier 0a (verdict) ; les préenregistrements de la ligne 3 (deux sections) et de la ligne 1 (§ 0) ; les critères de choix des cartes (§ 0) ; le papier C r3 (énoncés des hypothèses) ; les lignes GO-2026-11-19-75 à -77. **Non ouverts** : le devis d'héritage v5, le corps du préenregistrement du palier 0b, la relecture des cartes non gardées (titres seulement).
- Aucun fichier interdit par le mandat n'a été ouvert ; aucun résultat d'expérience close n'a été lu.

## Annexe — table des citations vérifiées

Produite par `outils-synthese-v1/verifier_citations_synthese_v1.py --table` à partir du registre `outils-synthese-v1/citations-synthese-v1.json`, puis collée ici ; dans la colonne « lieu » de X04 et X05, les barres verticales des motifs sont rendues à la main par des barres obliques, que le programme ne produit pas. Papier et annexe : page du PDF, extrait retrouvé dans le texte extrait de cette page. Code : fichier et lignes au commit `b510bb2c…`. Contrôles d'absence (X) : le programme liste les fichiers où le motif apparaît. Nos pièces : fichier de l'arbre de travail, ou de la branche nommée. Les extraits sont comparés espaces réduits, ligatures et guillemets normalisés, signes de mise en forme retirés pour le code et nos pièces. Dans cette table, une barre verticale d'un extrait est rendue par une barre oblique.

| n° | lieu | extrait vérifié |
|---|---|---|
| P01 | papier, p. 1 | scientists collaborating with audit agents identify 14x more valid errors versus scientists performing manual review |
| P02 | papier, p. 3 | participants with audit-agent access report findings matching inserted errors at nine times the proportion observed for participants given only the paper and code |
| P03 | papier, p. 3 | traces with 96.5% F1 |
| P04 | papier, p. 3 | supporting the efficacy of scientist-centric, AI-driven research |
| P05 | papier, p. 5 | is allowed to select its own hypotheses |
| P06 | papier, p. 8 | Using traces from the StarEmbed dataset, we extracted 50 claims |
| P07 | papier, p. 8 | We then corrupted 25 of these claims to artificially inflate results, sampling 5 different sets of claims to corrupt |
| P08 | papier, p. 8 | we also asked a coding agent to do the same given the traces of Kosmos and the coding agent |
| P09 | papier, p. 10 | mean F1 for GPT-5.6-Sol decreased to 0.268, 0.135, and 0.315 |
| P10 | papier, p. 10 | these results are a measure of the ability of audit agents to detect errors in research traces rather than an absolute measure of scientific correctness |
| P11 | papier, p. 10 | more unique inserted errors (3.50 versus 0.25 |
| P12 | papier, p. 10 | 14 of 33 in the Audit group match at least one inserted error, compared with 1 of 21 in the Code group (42.4% versus 4.8%) |
| P13 | papier, p. 10 | audit agent traced DA-Auto's use of cached variant-effect predictions to a download of held-out ProteinGym test data |
| P14 | papier, p. 10 | prompting the audit agent to distinguish the quantities measured and withdraw its numerical-error claim |
| P15 | papier, p. 9 | had downloaded testing data, despite being told to avoid this |
| P16 | papier, p. 23 | differences in execution models and research budgets prevent attributing this advantage solely to scientist steering |
| P17 | papier, p. 23 | We do not provide comprehensive ablations on various components of |
| P18 | papier, p. 23 | neither alone guarantees that a scientific conclusion is correct |
| P19 | papier, p. 23 | In a preliminary study |
| P20 | papier, p. 7 | (all p ≥ 0.21, Supplementary Table 6) |
| P21 | papier, p. 8 | on 134 of 217 assays (61.8%) |
| P22 | papier, p. 25 | an LLM prompted with the dataset description, the current hypothesis, a catalog of available tool agents, and the report accumulated so far in the round |
| P23 | papier, p. 25 | the director to executing only analyses explicitly related to the round's hypothesis and guidance |
| P24 | papier, p. 26 | that is provided as context during hypothesis generation |
| P25 | papier, p. 27 | a hypothesis-generation agent proposes a single hypothesis |
| P26 | papier, p. 27 | and an optional plan for testing it |
| P27 | papier, p. 28 | applies only the low-risk consolidations, verifying that information flagged as critical is preserved |
| P28 | papier, p. 28 | When a review fires, the round's cumulative report is passed to a reviewer LLM |
| P29 | papier, p. 28 | when executing specific hypotheses, we enable the reviewer |
| P30 | papier, p. 28 | generates a task-specific reviewer prompt at the start of each run |
| P31 | papier, p. 29 | changes are committed as the run proceeds with messages that tag each commit by round and query |
| P32 | papier, p. 30 | so a session cannot alter or rerun the research under review |
| P33 | papier, p. 31 | a process-control hook blocks long-running or destructive commands |
| P34 | papier, p. 32 | we mechanistically identified the best model reported by each agent |
| P35 | papier, p. 32 | DA-Auto uses Sonnet 4.6 for execution, whereas DA-Steer uses Opus 4.6 for Rounds 0 |
| P36 | papier, p. 34 | We used GPT-5.6 in this case to differentiate from the Claude models used to insert corruptions |
| P37 | papier, p. 34 | we score only the misrepresented verdict as a positive detection against the known corruption set |
| P38 | papier, p. 34 | we obtained post hoc, system-blinded difficulty ratings from independent LLM graders |
| P39 | papier, p. 34 | we used audit agents to generate a report in the style of an academic paper |
| P40 | papier, p. 34 | We then used LLMs to identify areas of the paper that could be manipulated or misrepresented to insert corruptions |
| P41 | papier, p. 34 | We then manually sorted through each of the corruptions |
| P42 | papier, p. 34 | We recruited 8 participants and randomly sorted them into either the code group (n = 4) or the audit |
| P43 | papier, p. 35 | The code group was explicitly instructed not to use AI tools |
| P44 | papier, p. 35 | We manually adjudicate the two findings that either vary across runs or disagree with historical assignments |
| P45 | papier, p. 27 | a targeted URL hook blocks known ProteinGym result sources |
| P46 | papier, p. 23 | The preservation of negative results in the accumulating research record |
| P47 | papier, p. 33 | We exclude methods designed for strictly verifiable tasks because |
| P48 | papier, p. 8 | For the primary comparison, we held the number of inserted corruptions and the auditor harness fixed across systems |
| P49 | papier, p. 34 | The automated benchmark varies the trace while holding the auditor fixed |
| P50 | papier, p. 30 | used as the fixed auditor in the corrupted-claim benchmark |
| P51 | papier, p. 33 | We used the agent's own internal reporting to rank the best model to choose |
| P52 | papier, p. 35 | withholding participant identity, cohort, and historical matching assignments from the judge |
| P53 | papier, p. 10 | by pointing to supporting figure evidence |
| P54 | papier, p. 31 | The OpenTargets agent exposes the Open Targets Platform |
| P55 | papier, p. 27 | This was most likely due to either the seeding of deep research reports in each run |
| P56 | papier, p. 3 | autonomously builds a model that achieves the highest held-out performance against expert hand-crafted and agent baselines |
| P57 | papier, p. 7 | Balanced accuracy of the selected classifiers on the common StarEmbed test subset |
| A01 | annexe, p. 18 | so this experiment controls the number and category catalog of corruptions rather than their strength |
| A02 | annexe, p. 18 | Each of the 5 cases per system was audited in 3 replicates, giving 15 scored runs per trace source |
| A03 | annexe, p. 18 | invalid outputs were retried, so reported F1 is conditional on validator acceptance |
| A04 | annexe, p. 18 | Because all cases draw corruptions from the same 50 claims, these tests are conditional on each system's report |
| A05 | annexe, p. 18 | (pooled over all 45 runs: F1 0.244, precision 0.563, recall 0.156) |
| A06 | annexe, p. 19 | We did not provide the honest report, corruption key, outputs from other auditors, external memory, or network access |
| A07 | annexe, p. 19 | we did not reorganize the traces into a shared representation |
| A08 | annexe, p. 20 | graded all 144 distinct corrupted claims (46 for |
| A09 | annexe, p. 20 | these grades are partially conflated with the construction of the provenance for each agent |
| A10 | annexe, p. 21 | was self-tracked and self-reported |
| A11 | annexe, p. 21 | The participant was the unit of analysis |
| A12 | annexe, p. 21 | this may have reduced the number of findings that Audit participants could report within the time limit |
| A13 | annexe, p. 22 | The original sandbox hooks constrained file locations but did not inspect shell commands for network addresses |
| A14 | annexe, p. 22 | The download occurred during Round 7 |
| A15 | annexe, p. 22 | but no URL-blocker denials in any campaign |
| A16 | annexe, p. 23 | not observe filesystem changes performed inside a shell process |
| A17 | annexe, p. 23 | pruned the version-control history so that unreachable objects did not retain the downloaded data |
| A18 | annexe, p. 23 | to perform post hoc leakage checks on the models evaluated on held-out test sets |
| A19 | annexe, p. 67 | the director without a judge |
| A20 | annexe, p. 67 | DA-Auto operated automatically and used Sonnet 4.6 throughout the |
| A21 | annexe, p. 69 | 9 for StarEmbed, 42 for DA-Steer, 78 for economics, and 132 |
| A22 | annexe, p. 69 | with none recorded for DA-Auto or the extragalactic astronomy campaign |
| A23 | annexe, p. 70 | despite a configured review interval |
| A24 | annexe, p. 69 | twelve days for DA-Steer and for economics, two months for DA-Auto |
| A25 | annexe, p. 71 | (each with an integrity hash) |
| A26 | annexe, p. 9 | The trace also contains a separate production recommendation of an 18-feature r-band |
| A27 | annexe, p. 9 | the held-out evaluation was implemented months later |
| A28 | annexe, p. 9 | did not retain a saved model during its research trace |
| A29 | annexe, p. 9 | We retained 7,955 objects with more than ten observations in both r and g |
| A30 | annexe, p. 79 | this adjudication is not blinded |
| A31 | annexe, p. 101 | R04 14 10 10 |
| A32 | annexe, p. 100 | 0.957±0.012 0.973±0.008 0.965±0.008 |
| A33 | annexe, p. 17 | At the first turn, the application supplied the run's accumulated memory report and, when available, its research paper as initial context |
| A34 | annexe, p. 3 | The refiner's output replaces the previous accumulated report |
| A35 | annexe, p. 4 | Both documentation agents read the shared workspace but can edit only their assigned document |
| A36 | annexe, p. 10 | explicitly prohibit internet access |
| A37 | annexe, p. 120 | You will be evaluated on a held-out test set that you do not have access to |
| A38 | annexe, p. 115 | Early-stop events 0 5 1 20 1 6 |
| A39 | annexe, p. 72 | the hypothesis-generation agent produces all candidates in one model call |
| A40 | annexe, p. 101 | 0.533 (10) 0.884 (46) |
| A41 | annexe, p. 22 | A separate process-protection hook screens a narrow set of broad process-killing and destructive command patterns |
| A42 | annexe, p. 78 | we use an indepen |
| A43 | annexe, p. 21 | They received no training, demonstration, or practice task |
| A44 | annexe, p. 19 | The audit report corresponded to the end of Round 3, the last completed round |
| A45 | annexe, p. 101 | Interpretive assessment 0.571 (7) |
| A46 | annexe, p. 78 | receive no match regardless of their potential validity |
| A47 | annexe, p. 69 | baseline agents were run with internet access |
| A48 | annexe, p. 22 | We selected the clean end-of-Round-5 checkpoint for rollback and resumed execution at Round 6 |
| A49 | annexe, p. 18 | Within each auditor-model comparison, every trace-source arm used the same read-only coding-agent auditor |
| A50 | annexe, p. 18 | isolating access to the trace as the single manipulated variable |
| A51 | annexe, p. 19 | the navigation instructions only required the auditor to follow each trace's native organization |
| A52 | annexe, p. 19 | Auditors were instructed to account for all 50 capsules |
| A53 | annexe, p. 23 | the quarantined leaked directory was placed outside the read allow-list |
| A54 | annexe, p. 23 | an intermediate resume attempt that rediscovered this directory was denied by the sandbox hook |
| A55 | annexe, p. 23 | variant-overlap test for the DA-Steer graph-attention branch additionally found no overlapping variants |
| A56 | annexe, p. 9 | named the best overall model in a Round 2, query 9 report before the test set was touched |
| A57 | annexe, p. 9 | which is the selection rule applied to the comparators |
| A58 | annexe, p. 78 | withholding participant names, cohort labels, historical assignments |
| A59 | annexe, p. 78 | The positive catalog-ID set is identical across all five repetitions for 53 of 54 findings |
| A60 | annexe, p. 79 | For participant R04, finding 4, all five runs match both error 8 and error 4 |
| A61 | annexe, p. 79 | For participant R01, finding 9, one of five runs matches error 6 |
| A62 | annexe, p. 101 | a non-additive total |
| A63 | annexe, p. 72 | When available, it also loads the deep-research background |
| A64 | annexe, p. 72 | and an optional analysis plan |
| A65 | annexe, p. 70 | so deep research contributed to hypothesis seeding throughout |
| A66 | annexe, p. 23 | The artifacts establish that sandbox enforcement was active in the reported campaigns through recorded denials |
| A67 | annexe, p. 17 | A single application provided both the hypothesis-steering workflow and the audit workspace |
| C01 | code, `DiscoveryAgent/hypothesis_brancher.py`, l. 666 | assert len(workflows) == 1, "Only one workflow is supported for now" |
| C02 | code, `DiscoveryAgent/hypothesis_brancher.py`, l. 796 | self.results_memory.update_report(final_report, verbose=False) |
| C03 | code, `DiscoveryAgent/director_workflow.py`, l. 577-578 | if self.explicit_hypothesis_step is None: return False # We're not using explicit hypotheses |
| C04 | code, `DiscoveryAgent/director_workflow.py`, l. 1157-1159 | perform_review = self._test_iteration_condition_with_warmup(previous_query_num, self.review_optimization_steps) |
| C05 | code, `configs/paper/dms_steer.yaml`, l. 17 | hold_reviews_in_exploratory_phase: true |
| C06 | code, `DiscoveryAgent/utils/arg_parsers.py`, l. 153 | parser.add_argument("--explicit_hypothesis_step", type=int, default=None, |
| C07 | code, `DiscoveryAgent/director_workflow.py`, l. 1290-1292 | And here is the most recent analysis. You should focus your critiques on these findings and approaches: {self.cumulative_report} |
| C08 | code, `DiscoveryAgent/director_workflow.py`, l. 1135 | commit_message = f"Query {query_num}" |
| C09 | code, `DiscoveryAgent/utils/git_version_control.py`, l. 351 | full_message = f"[Round {round_num}] {message} / {timestamp}" |
| C10 | code, `DiscoveryAgent/checkpoint_manager.py`, l. 900 | warnings.append(f"State hash mismatch for {agent_name}") |
| C11 | code, `DiscoveryAgent/memory/results_memory.py`, l. 522 | self.current_report = refined_report |
| C12 | code, `DiscoveryAgent/memory/results_memory.py`, l. 354-363 | refined_report, cost = self.llm( |
| C13 | code, `DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py`, l. 275 | Generate one hypothesis using accumulated research context. |
| C14 | code, `DiscoveryAgent/prompts/execution_agent.py`, l. 241 | You may delete old scripts, visualizations, reports, etc. if they are contradictory to new results or follow-up findings. |
| C15 | code, `DiscoveryAgent/prompts/execution_agent.py`, l. 250 | DO NOT push or commit anything to git. |
| C16 | code, `DiscoveryAgent/tool_agents/security/url_blocker.py`, l. 21 | This is a defense-in-depth layer, not a panacea |
| C17 | code, `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py`, l. 7 | Bash commands are checked on a best-effort basis for common shell patterns. |
| C18 | code, `scripts/utils/audit_run.py`, l. 5-6 | a human-readable summary report using Claude Haiku. |
| C19 | code, `README.md`, l. 13-15 | It does not contain the datasets, the code the execution agent wrote during the campaigns, or the hypothesis-steering web application |
| C20 | code, `README.md`, l. 204-205 | The paper used a separate web application to draft and edit candidate |
| C21 | code, `README.md`, l. 268-269 | The shared prompt implementation is not an exact prompt snapshot for every |
| C22 | code, `README.md`, l. 188-189 | The retained initial checkpoint has selection flags enabled despite the |
| C23 | code, `configs/paper/dms_auto.yaml`, l. 11 | execution_model: "claude-sonnet-4-6" |
| C24 | code, `configs/paper/dms_steer.yaml`, l. 11 | execution_model: "claude-opus-4-6" |
| C25 | code, `DiscoveryAgent/prompts/review_agent.py`, l. 2 | You will be shown a report of an AI scientist's explorations of a dataset. |
| C26 | code, `inputs/dms_auto/README.txt`, l. 9 | You will be evaluated on a held-out test set that you do not have access to. |
| C27 | code, `DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py`, l. 129-132 | self.background_literature_content = f.read() |
| C28 | code, `DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py`, l. 80 | self.generate_plan = getattr(self.config, "generate_plan", False) |
| C29 | code, `DiscoveryAgent/prompts/hyp_generation.py`, l. 151-154 | **Hypothesis**: [Your hypothesis] **Justification**: [Your justification for why this hypothesis is novel and impactful] |
| C30 | code, `DiscoveryAgent/hypothesis_brancher.py`, l. 822 | if results.get('status') == 'paused_for_selection': |
| C31 | code, `DiscoveryAgent/director_workflow.py`, l. 1225-1233 | 'status': 'stopped_by_director' if director_requested_stop else 'completed' |
| C32 | code, `DiscoveryAgent/tool_agents/security/kill_blocker.py`, l. 31-45 | "permissionDecision": "allow", "updatedInput": {**tool_input, "command": safe_command}, |
| C33 | code, `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py`, l. 124-130 | a bare top-level ``permissionDecision`` key is not part of the schema and is silently dropped. |
| C34 | code, `DiscoveryAgent/hyp_agents/director_agent.py`, l. 584-587 | turn_prompt += DATASET_DESCRIPTION_PROMPT.format( dataset_description=dataset_description ) |
| C35 | code, `README.md`, l. 274-281 | Code, models and reports the execution agent produced during the campaigns. |
| C36 | code, `DiscoveryAgent/tool_agents/execution_agent_cc.py`, l. 1043 | HookMatcher(matcher="Bash", hooks=[process_protection_hook]), |
| C39 | code, `DiscoveryAgent/director_workflow.py`, l. 1286-1288 | And here's a background report on what we've previously explored and learned on this dataset and task: {self.background_report} |
| C40 | code, `DiscoveryAgent/tool_agents/specialized/opentargets_agent.py`, l. 142 | HookMatcher(matcher="Bash", hooks=[process_protection_hook]), |
| C41 | code, `DiscoveryAgent/tool_agents/security/kill_blocker.py`, l. 49-51 | return { "permissionDecision": "deny", "permissionDecisionReason": "This command is classified as high-risk for system stability." |
| C44 | code, `DiscoveryAgent/prompts/hyp_generation.py`, l. 120 | ## Accumulated Knowledge from Previous Rounds |
| C45 | code, `DiscoveryAgent/prompts/execution_agent.py`, l. 237 | NEVER delete, move, or modify existing data files (CSV, JSON, Excel, etc.). Data is not to be modified in any way. |
| C46 | code, `README.md`, l. 143-144 | These are starting configurations for the campaign protocols, not a manifest of every invocation. |
| C47 | code, `README.md`, l. 153 | dms_steer.yaml / ProteinGym DMS, DA-Steer / Scientist selection / none / |
| C48 | code, `DiscoveryAgent/prompts/cc_sub_agents.py`, l. 63-75 | tools=["Read", "Edit", "Glob", "Grep"], |
| C49 | code, `DiscoveryAgent/prompts/claude_md_generator_command.py`, l. 173 | CRITICAL: You are only allowed to edit DOCUMENTATION.md, but you may read any script or file in the directory. |
| C50 | code, `DiscoveryAgent/hyp_agents/director_agent.py`, l. 70 | You will receive a research context (dataset description, task, and potentially a hypothesis or exploration directive) |
| C51 | code, `inputs/dms_auto/README.txt`, l. 8 | You are to create a machine learning model to predict the DMS scores from the protein sequence, structure, and/or MSA. |
| X01 | dépôt code, motif `background_literature_content` sous DiscoveryAgent, scripts | l'attribut qui reçoit le rapport de littérature n'apparaît que dans le fichier qui le charge (fichiers touchés : ['DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py'] ; occurrences : 3) |
| X02 | dépôt code, motif `self\.generate_plan` sous DiscoveryAgent, scripts | le drapeau du plan est stocké une fois et jamais relu (fichiers touchés : ['DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py'] ; occurrences : 1) |
| X03 | dépôt code, motif `task_description` sous DiscoveryAgent/hyp_agents/director_agent.py | l'agent directeur ne mentionne nulle part la description de la tâche (fichiers touchés : aucun ; occurrences : 0) |
| X04 | dépôt code, motif `corrupted.claim|misrepresented|inserted.error` sous . | aucun matériel du banc des affirmations corrompues ni de l'étude humaine dans le dépôt du code (fichiers touchés : aucun ; occurrences : 0) |
| X05 | dépôt repro, motif `corrupted.claim|misrepresented|inserted.error|participant` sous . | aucun matériel du banc ni de l'étude humaine dans le dépôt de reproduction (fichiers touchés : aucun ; occurrences : 0) |
| X06 | dépôt repro, noms des fichiers suivis | aucun point de contrôle, mémoire ni rapport de manche parmi les 68 fichiers suivis du dépôt de reproduction (fichiers suivis : 68 ; noms touchés : aucun) |
| X07 | dépôt code, motif `explicit_hypothesis_step` sous configs | aucune des configurations publiées ne fixe le pas d'hypothèse explicite (fichiers touchés : aucun ; occurrences : 0) |
| X08 | dépôt code, motif `'paused_for_selection'` sous DiscoveryAgent/director_workflow.py | la boucle du directeur ne produit jamais le statut de pause pour sélection (fichiers touchés : aucun ; occurrences : 0) |
| X09 | dépôt code, motif `explicit_hypothesis_step|no-hold-reviews` sous scripts/plan.py, configs | ni le lanceur documenté ni aucune configuration ne règle le pas d'hypothèse explicite ni ne lève la retenue des relectures (fichiers touchés : aucun ; occurrences : 0) |
| X10 | dépôt code, motif `get_feedback\(` sous DiscoveryAgent, scripts | le relecteur n'a qu'un appel dans tout le code, plus sa définition (fichiers touchés : ['DiscoveryAgent/director_workflow.py'] ; occurrences : 2) |
| X11 | dépôt code, motif `^generate_plan: true` sous configs/paper | les six configurations publiées activent le drapeau du plan, les deux automatiques comprises (fichiers touchés : ['configs/paper/acs_select.yaml', 'configs/paper/dms_auto.yaml', 'configs/paper/dms_steer.yaml', 'configs/paper/dwarf_select.yaml', 'configs/paper/gw_cd4_select.yaml', 'configs/paper/starembed_auto.yaml'] ; occurrences : 6) |
| X12 | dépôt code, motif `paused_for_selection` sous DiscoveryAgent, scripts | le statut de pause n'apparaît que là où il est testé, recopié ou affiché, jamais là où un tour s'achève (fichiers touchés : ['DiscoveryAgent/hypothesis_brancher.py', 'scripts/run.py'] ; occurrences : 4) |
| N01 | `docs/decisions/decision-N-058-v1.md` | se jugent sur l'oracle du monde planté |
| N02 | `docs/decisions/decision-N-058-v1.md` | l'interdit porte sur la sélection d'agents, pas sur celle des fiches |
| N03 | `docs/decisions/decision-N-058-v1.md` | aucun score de moniteur ni de juge n'entre dans un signal d'entraînement ou de sélection de l'agent |
| N04 | `docs/decisions/decision-N-065-v1.md` | ses fiches sont du matériau, jamais une preuve |
| N05 | `docs/decisions/decision-N-065-v1.md` | Son juge statistique est un moniteur d'affirmations de recherche |
| N06 | `docs/decisions/decision-matiere-premiere-mentors-v1.md` | aucune promotion décidée par un modèle |
| N07 | `docs/decisions/decision-matiere-premiere-mentors-v1.md` | verdicts du juge et témoins jamais servis aux proposeurs, sauf décision de Lazar |
| N08 | `docs/decisions/decision-resserrement-juge-au-nul-v1.md` | seule la réunion reste revendiquable |
| N09 | `docs/decisions/decision-N-073-complement-3-memoire-transmise-v1.md` | non une archive de découvertes |
| N10 | `docs/decisions/decision-N-073-complement-2-memoire-transmise-v1.md` | des résumés de l'expérience font moins bien que les traces brutes |
| N11 | `docs/decisions/decision-N-067-v1.md` | O1 : plus revendiquée |
| N12 | `docs/decisions/decision-N-067-v1.md` | chargé de tromper, qui lit la description exacte du juge |
| N13 | `docs/decisions/decision-N-064-v1.md` | calculée par l'orchestrateur, hors de tout agent |
| N14 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/plan-heritage-trois-bras-corrige-v5.md` (branche `lot/compte-organisme-v1`) | Le registre est en ajout seul, chaîné par empreintes et scellé à chaque génération ; les tentatives non gardées y restent. |
| N15 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/plan-heritage-trois-bras-corrige-v5.md` (branche `lot/compte-organisme-v1`) | un verdict, un score ou un texte d'un juge, à modèle ou statistique |
| N16 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/plan-heritage-trois-bras-corrige-v5.md` (branche `lot/compte-organisme-v1`) | Aucun modèle n'intervient. |
| N17 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/plan-heritage-trois-bras-corrige-v5.md` (branche `lot/compte-organisme-v1`) | un écart à budget égal, coût de lecture compris |
| N18 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/ordre-de-passage-epreuves-v9-v3.md` (branche `lot/compte-organisme-v1`) | aucun des deux défauts visés n'est attesté, puisque rien n'est servi aujourd'hui |
| N19 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/ordre-de-passage-epreuves-v9-v3.md` (branche `lot/compte-organisme-v1`) | rang 0 : le branchement |
| N20 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/preenregistrement-ligne-3-votes-effectifs-juges-v4.md` (branche `lot/compte-organisme-v1`) | Aucun résultat de cette ligne, « oui » compris, ne fera trancher une carte par un juge. |
| N21 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/preenregistrement-ligne-3-votes-effectifs-juges-v4.md` (branche `lot/compte-organisme-v1`) | Deux juges (Opus et Argon) lisent chaque carte, chacun dans une session neuve, sans voir l'autre. |
| N22 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-choix-cartes-v9-v3.md` (branche `lot/compte-organisme-v1`) | Une carte non retenue n'est pas réfutée : elle n'est pas éprouvée. |
| N23 | `prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md` | dans un registre des essais tenu par l'orchestrateur et jamais servi à un agent |
| N24 | `prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md` | Une carte est jugée sur des tirages frais, tirés après le gel de son engagement |
| N25 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0a/rapport-palier-0a-v1.md` (branche `lot/compte-organisme-v1`) | Le verdict est calculé par le noyau sur la copie scellée du fichier brut |
| N26 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0a/rapport-palier-0a-v1.md` (branche `lot/compte-organisme-v1`) | dans l'exécuteur factice puis dans le vrai bac à sable bwrap local |
| N27 | `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r3.md` (branche `claude/papier-c-preenregistrement-v1`) | voit son verdict v se déplacer de v₀ vers une destination ĉ |
| N28 | `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r3.md` (branche `claude/papier-c-preenregistrement-v1`) | agent auteur du contenu adverse destiné au moniteur |
| N29 | `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r3.md` (branche `claude/papier-c-preenregistrement-v1`) | l'usurpation stylistique de l'instructeur, sans aucun ordre |
| N30 | `registres/go.md` | on garde l'experimentateur |
| N31 | `registres/go.md` | lecteur témoin des tests de mort joué en réel au seul palier 1 |
| N32 | `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` | l'archive héritée cause-t-elle les découvertes ? |
| N33 | `docs/decisions/decision-N-073-complement-3-memoire-transmise-v1.md` | héritée d'une course antérieure puis tenue, comparée à la même mémoire née vide et à aucune |
| N34 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/plan-heritage-trois-bras-corrige-v5.md` (branche `lot/compte-organisme-v1`) | Rien sur une mémoire contre rien |
| N35 | `docs/decisions/decision-N-067-v1.md` | Qu, Chen, Wang mesurent six bras de mémoire sous l'arbitre gelé |
| N36 | `docs/decisions/decision-N-064-v1.md` | Co-Scientist (Nature 655, p. 487-496) comme voisin de la boucle générer-classer-faire évoluer |
| N37 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/plan-heritage-trois-bras-corrige-v5.md` (branche `lot/compte-organisme-v1`) | entrées fausses plantées par l'orchestrateur (dans ce bras seulement) ; registre paraphrasé |
| N38 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/plan-heritage-trois-bras-corrige-v5.md` (branche `lot/compte-organisme-v1`) | historique brut de la source laissé en place, sans registre |
| N39 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/plan-heritage-trois-bras-corrige-v5.md` (branche `lot/compte-organisme-v1`) | ce qui est servi quand le registre dépasse la taille bornée |
| N40 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/plan-heritage-trois-bras-corrige-v5.md` (branche `lot/compte-organisme-v1`) | champs typés et bornés ; champs libres servis aux proposeurs entre balises de donnée |
| N42 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/ordre-de-passage-epreuves-v9-v3.md` (branche `lot/compte-organisme-v1`) | une course v9 (72,50 USD) par bras |
| N43 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/ordre-de-passage-epreuves-v9-v3.md` (branche `lot/compte-organisme-v1`) | environ 25 USD ; bras ajouté non chiffré |
| N44 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/preenregistrement-ligne-3-votes-effectifs-juges-v4.md` (branche `lot/compte-organisme-v1`) | même consigne figée |
| N45 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/preenregistrement-ligne-3-votes-effectifs-juges-v4.md` (branche `lot/compte-organisme-v1`) | le cas haut du devis (22,49 USD |
| N46 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0a/rapport-palier-0a-v1.md` (branche `lot/compte-organisme-v1`) | connexion réseau refusée |
| N47 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0a/rapport-palier-0a-v1.md` (branche `lot/compte-organisme-v1`) | l'expérimentateur n'a rien à décider |
| N48 | `registres/go.md` | après la note de conception du juge |
| N49 | `registres/go.md` | engagements à forme imposée aux paliers payants |
| N50 | `docs/decisions/decision-N-067-v1.md` | O11 : plus aucune revendication d'idée. |
| N51 | `docs/decisions/decision-N-067-v1.md` | ne sont plus revendiquées : elles sont empruntées et citées |
| N52 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/ordre-de-passage-epreuves-v9-v3.md` (branche `lot/compte-organisme-v1`) | de 150 à 350 USD selon la proposition |
| N53 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/plan-heritage-trois-bras-corrige-v5.md` (branche `lot/compte-organisme-v1`) | ni le coût réel d'un test de mort (palier 1) |

