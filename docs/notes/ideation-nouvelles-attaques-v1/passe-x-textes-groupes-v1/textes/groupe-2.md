Voici six questions de recherche, numérotées comme dans une liste de dix-huit. Répondez à chacune, dans l'ordre, sous un titre de la forme « Réponse k », où k est le numéro de la pièce. Chaque réponse fait au plus 600 mots. Terminez par une ligne seule : FIN DES RÉPONSES.

[Pièce 4 sur 18]

« Un agent fondé sur un modèle de langue accomplit une longue tâche d'analyse, faite de dizaines à centaines d'actions. Il peut en dégrader le résultat exprès, de sorte que chaque action, lue seule, paraisse défendable. Un agent honnête se trompe aussi, sans intention.

1. Y a-t-il des calculs qu'un tel agent doit nécessairement effectuer pour dégrader exprès, et qu'un agent honnête n'effectue pas ? Si oui, lesquels, et nécessaires à quelles conditions ? Si non, pourquoi ?
2. Qu'est-ce qui est déjà publié sur ce point ? Donnez titre et année, et signalez ce qui est cité de mémoire.
3. La réponse dépend-elle de la façon dont l'agent est devenu tel (instruction reçue, entraînement) ?
4. Si l'on cherche à lire un tel calcul dans les états internes de l'agent, comment savoir que l'on lit un éventuel tel calcul et non une chose qui l'accompagne, et qu'on lit mieux qu'une méthode qui ne lit que le texte produit ? Quelles mesures, quels témoins ?
5. Dans quels cas n'y a-t-il rien à lire ?
6. Quelle première expérience, sur un modèle ouvert de petite taille, dirait si la question vaut d'être poursuivie, ou qu'elle ne le vaut pas ?

Dites pour chaque point ce que vous savez, ce que vous supposez, et ce qui vous ferait changer d'avis. »

[Pièce 5 sur 18]

Un laboratoire a conçu un détecteur qui surveille un agent de langue pendant de longues tâches, pour repérer une dégradation discrète du résultat. Il veut savoir ce que valent les épreuves qu'il lui fait subir. Il dispose de trois sources d'attaques :

- un lot d'attaques mis de côté, dont l'historique d'accès est à préciser ;
- des attaques jouées par des agents que le laboratoire a entraînés à dégrader le résultat ;
- des attaques produites par un attaquant auquel on a donné la description du détecteur.

Pour chacune : son résultat peut-il compter comme une vérification indépendante du détecteur ? Les réponses « oui », « non », « sous telles conditions » et « indécidable sans telle information » sont également recevables. Dites de quelles informations sur la source votre réponse dépend.

Pour le lot mis de côté : faut-il s'en servir ? Les réponses « oui, librement », « oui, de telle façon », « non, jamais » et « cela dépend de… » sont également recevables. Dites ce que chaque usage ferait gagner et perdre.

Pour chaque réponse :
- l'énoncé réfutable et ce qu'on mesurerait ;
- l'antériorité la plus proche, y compris hors de l'apprentissage automatique (auteurs, année, titre), en disant si vous citez de mémoire ;
- un contrôle dont l'issue ne dépend de l'avis de personne ;
- ce qu'un lecteur extérieur pourrait vérifier lui-même.

[Pièce 6 sur 18]

« Plusieurs équipes publient sur la surveillance d'agents de langue qui exécutent de longues tâches et pourraient en dégrader le résultat. On vous remet une liste de ces publications. Pour chacune, établissez à partir du texte seul : ce que les auteurs reconnaissent ne pas avoir fait, ce qu'ils annoncent vouloir faire, et ce qu'ils disent ouvert pour tous. Comment vérifier qu'un manque reconnu par une équipe n'a pas été comblé ailleurs depuis ? Selon quels critères une équipe tierce, aux moyens limités, devrait-elle choisir où concentrer son effort, et quelles observations faites avant de connaître l'issue distingueraient un bon choix d'un mauvais ? Indiquez ce que la liste fournie ne permet pas de décider. »

[Pièce 7 sur 18]

« On observe une suite de n nombres réels, un par étape d'un long processus, parfois pour plusieurs processus menés en parallèle. Deux situations sont possibles, sans que l'une soit la référence de l'autre. Dans les deux, chaque nombre pris isolément suit exactement la même loi ; tout le reste peut différer. On dispose aussi d'un échantillon fini de m nombres issus de processus dont on sait qu'ils relèvent de l'une des deux situations, désignée ici comme la première, menés sur des tâches qui peuvent être différentes de la tâche observée ou identiques à elle.

1. Quelles règles de décision ont, ou n'ont pas, une probabilité de détection différente de leur taux de fausses alertes ? Donnez des énoncés à n fini, avec preuve ou contre-exemple.
2. Que change le fait que l'échantillon de comparaison soit fini, et qu'il vienne de la même tâche ou d'autres tâches ?
3. Quel est l'écart minimal détectable entre les deux situations, s'il existe, et comment dépend-il de n et de m ? Précisez vos hypothèses.
4. Quels travaux publiés traitent déjà ces points (auteurs, année, titre, degré de certitude) ?
5. Quel calcul exact ou quelle simulation d'un jour départagerait vos réponses ? »

[Pièce 8 sur 18]

« Une organisation confie de longues tâches d'analyse à un système automatisé dont elle ne peut pas garantir la loyauté. Elle dispose d'une source de hasard que ce système ne peut ni prévoir ni observer. Recensez tous les usages distincts qu'un contrôleur peut faire d'un tel hasard face à un contrôlé stratégique, dans tous les domaines où ce problème se pose. Pour chaque usage : ce qu'il garantit exactement, sous quelles conditions, quels travaux l'établissent, et s'il a déjà été appliqué à des agents fondés sur des modèles de langue. Dites lesquels vous jugez les moins étudiés pour ces agents, et quelle recherche bibliographique ou quelle expérience vous donnerait tort. »

[Pièce 17 sur 18]

Un agent de langue accomplit une longue tâche. Un adversaire peut en dégrader le résultat par petites touches. Deux moniteurs l'observent : l'un ne lit que les sorties (texte, actions, produit), l'autre lit les activations internes de l'agent. On mesure le dommage que l'adversaire cause encore lorsqu'il échappe à l'un, à l'autre ou aux deux.

Peut-on, ou non, concevoir ces deux moniteurs de sorte qu'échapper aux deux coûte à l'adversaire plus de dommage qu'échapper au plus difficile des deux, et de combien ? Les réponses « oui, pour telle conception et tel adversaire », « non, aucune conception ne crée un tel écart » et « indécidable en l'état » sont également recevables.

Répondez séparément pour quatre adversaires : celui qui n'agit que par le contenu qu'il produit, sans entraînement ; celui qu'un réglage fin léger a entraîné sans gradient à travers le moniteur interne ; celui qui dispose du gradient à travers un moniteur interne connu ; le même contre un moniteur interne inconnu.

Pour chaque réponse :
- la conception du défenseur concernée, s'il y en a une, et le mécanisme supposé ;
- l'énoncé réfutable et la grandeur mesurée ;
- l'antériorité la plus proche, y compris hors de l'apprentissage automatique (auteurs, année, titre), en disant si vous citez de mémoire ;
- la plus petite expérience sur un modèle ouvert de huit milliards de paramètres, et son contrôle indispensable ;
- ce qui distinguerait un coût réel d'un artefact de l'expérience, dans un sens comme dans l'autre (adversaire mal optimisé, moniteur mal réglé).

Dites enfin quelle portée peut avoir un résultat selon la classe d'adversaires qu'il couvre.
