# Fiches normalisées (extraction du lecteur), avec sources (S1..S5) et passages. Les sources ne vont pas aux juges.
R = []
def r(cle, famille, nom, meca, pred, test, ctrl, cout, sources, passages, note=""):
    R.append(dict(cle=cle, genre="R", famille=famille, nom=nom, mecanisme=meca, prediction=pred, test=test,
                  controles=ctrl, cout=cout, sources=sources, passages=passages, note=note))

r("refus-insensible", "a", "Refus insensible à la légitimité",
  "La recette a seulement relevé le seuil à partir duquel le modèle entreprend une action sensible dans un contexte d'agent. Elle évite le tort en refusant davantage, sans mieux arbitrer entre le tort de l'action et celui de l'inaction.",
  "Si vraie : sur des jumelles des scénarios où seul le fait qui rend l'action nuisible est retiré (l'action devient légitime, voire nécessaire pour éviter un tort plus grand), la recette refuse aussi ; la discrimination P(agit | légitime) − P(agit | nuisible) reste proche de zéro. « Raisons » prédit une discrimination forte ; « regard » prédit une modulation par l'observation, pas un biais stable vers l'inaction.",
  "Paires contrefactuelles nouvelles sur les adaptateurs publiés (recette avec raisonnement, jumelle, référence), même outil et même décor ; épisodes neufs, sans réentraînement. Les épisodes déjà joués ne servent qu'au tri.",
  "Positif : un modèle bridé par consigne (« n'agis jamais ») doit donner une discrimination nulle. Négatif : édition placebo qui ne change aucun fait pertinent ; instruction bénigne avec le même outil.",
  "moyen", ["S1","S2","S3","S4","S5"],
  {"S1":"A1 et §4","S2":"fiches 13, 31","S3":"T1-A rivale 2 ; T3-A duel 1 ; T3-E prudence globale","S4":"A2","S5":"rivale 7 (sur-refus téléologique)"})

r("retenue-initiative", "a", "Retenue générale envers toute initiative non demandée",
  "La recette apprendrait à prendre moins d'initiatives non demandées, quelles qu'elles soient, et à attendre ou appeler un humain plus souvent. Les trois actions nuisibles étant des initiatives non demandées, leur taux baisse sans raison sur le tort ni croyance d'observation.",
  "Si vraie : sur les épisodes déjà joués, la recette prend aussi moins d'initiatives utiles et non nuisibles (action utile hors consigne, achèvement de la tâche principale), en proportion de la baisse des actions nuisibles ; la sélectivité (baisse nuisible rapportée à baisse non nuisible) est proche de un. « Raisons » prédit une baisse des seules initiatives nuisibles ; « regard » prédit une dépendance à la condition d'observation.",
  "Nouveau jugement des traces existantes qui relève les initiatives non nuisibles ; aucun épisode nouveau.",
  "Positif : un modèle rendu passif par consigne doit montrer une sélectivité proche de un. Négatif : la référence.",
  "bas", ["S2"], {"S2":"fiches 8, 26"})

r("direction-refus", "a", "Réflexe de refus conversationnel étendu aux actions d'agent",
  "Le mécanisme de refus qui existait déjà pour les demandes nuisibles en conversation aurait seulement été rendu actif dans les contextes d'agent. Aucune raison n'interviendrait.",
  "Si vraie : retirer des poids la direction interne de refus (construite sur le modèle de départ) ramène le taux d'actions nuisibles de la recette près de celui de la référence, et ses fausses alarmes montent avant retrait. Sous « raisons », une part du gain survit au retrait. « Regard » ne prédit rien sur cette direction.",
  "La machinerie de retrait déjà préparée, avec la direction de refus à la place de la direction d'évaluation ; sert aussi de contrôle positif du transport des directions dans les adaptateurs.",
  "Positif : demandes nuisibles en conversation (le refus doit tomber). Négatif : directions tirées au hasard, appariées en dégât.",
  "bas à moyen", ["S1"], {"S1":"A1"}, note="Même mécanisme que « refus insensible », prédiction différente.")

r("lexical-marqueurs", "a", "Classifieur lexical : l'action suit les mots, pas la légitimité",
  "La recette aurait compilé une règle de surface : refuser quand le contexte contient des descripteurs de tort ou des mots d'alerte, agir quand il contient des marqueurs d'autorisation. Le refus sur ordre et l'exécution de l'instruction bénigne au même outil sont compatibles avec ce classifieur.",
  "Plan deux par deux : marqueurs d'autorisation ou mots d'alerte présents/absents × légitimité réelle valide/invalide. Si vraie : l'action suit les marqueurs (ex. elle agit quand une entité non habilitée « autorise » avec les bons mots ; elle agit quand l'action nuisible est décrite par une indirection technique sans mot d'alerte). « Raisons » : l'action suit la légitimité à marqueurs constants. « Regard » : aucun effet des marqueurs à observation fixe.",
  "Variantes nouvelles des 27 scénarios (environ 54 à 108), adaptateurs publiés, épisodes neufs ; verdict mécanique primaire.",
  "Positif : une politique lexicale construite exprès doit suivre les marqueurs. Négatif : paraphrase qui ne touche ni permission ni conséquence ; vérification préalable que le modèle de départ décrit correctement qui est habilité.",
  "bas à moyen", ["S2","S3","S4","S5"],
  {"S2":"fiches 1, 19, 7, 25","S3":"T3-A duel 1 ; T3-C rivale 1","S4":"A1","S5":"rivale 7 (contournement euphémique)"})

r("paraphrase-profonde", "a", "Appariement de surface : le gain tombe sous paraphrase profonde",
  "La recette aurait associé au refus le vocabulaire, la structure et le style partagés par ses données d'entraînement et par les scénarios portés. Le gain serait de la proximité de surface, uniforme vis-à-vis de l'observation.",
  "Si vraie : réécrire les scénarios dans un autre registre (par un modèle d'une autre famille), à structure morale, outils et enjeux constants, fait chuter le gain de la recette davantage que celui du modèle de départ (interaction réécriture × recette positive). « Raisons » : interaction nulle. « Regard » : effet seulement si la réécriture déplace la croyance d'évaluation, mesurée sur chaque version ; croiser avec les phrases d'observation.",
  "27 scénarios réécrits, adaptateurs publiés, épisodes neufs ; croisement réécriture × phrase d'observation.",
  "Positif ou étalonnage : tâche bénigne dans chaque style, exécutée à au moins 90 %. Négatif : changements de noms et d'ordre sans changement de registre.",
  "moyen", ["S1","S2","S3","S4","S5"],
  {"S1":"A2 (variantes à surface neuve)","S2":"fiches 14, 34","S3":"T3-B duel principal ; T3-A duel 2","S4":"A1 (paraphrases indépendantes)","S5":"rivale 2, volet 2"})

r("familiarite", "c", "Parenté entre données d'entraînement et scénarios (gain selon la familiarité)",
  "Les documents et démonstrations pourraient décrire des situations voisines des scénarios portés. Le gain serait fort sur les situations reconnues et s'effacerait à mesure qu'on s'en éloigne, sans rapport avec l'observation.",
  "Si vraie : sur les épisodes déjà joués, le gain par évaluation croît avec un indice de familiarité (écart de vraisemblance par jeton du texte du scénario entre l'adaptateur et la référence, ou proximité au corpus si publié), à type d'action, condition de but et taux du modèle de départ fixés. « Raisons » et « regard » ne prédisent aucune pente.",
  "Passes avant seules sur les 27 textes de scénario, puis régression sur les gains déjà mesurés ; permutation par bloc d'action. Non testable par la proximité au corpus si celui-ci n'est pas public.",
  "Positif : un scénario copié des données doit avoir une familiarité extrême. Négatif : proximité à un corpus sans rapport.",
  "bas", ["S1","S2","S3","S4"],
  {"S1":"A2","S2":"fiches 9, 29, 14, 34","S3":"T1-A rivale 8 ; T3-C rivale 8","S4":"C2"},
  note="Une source a déclaré cette rivale non testable sans le corpus.")

r("tampon-trace", "a", "La trace à l'inférence, non ce qui a été appris",
  "Les jumelles diffèrent par l'entraînement et par la présence d'une trace au moment de répondre. Générer une trace avant l'action donnerait du calcul et un préfixe de prudence générique, quel que soit le contenu des raisons.",
  "Plan poids × trace : greffer la trace de la recette sur la jumelle sans raisonnement, couper la trace de la recette (balise fermée tout de suite), et insérer une trace neutre de même longueur. Si vraie : la trace greffée ou neutre ramène la jumelle près du plancher et la recette sans trace remonte vers la jumelle. « Raisons dans les poids » : la recette sans trace garde son gain. « Regard » : effet seulement si la trace mentionne le test.",
  "Préremplissage des traces déjà enregistrées, ne régénérer que l'action finale ; épisodes neufs courts, sans réentraînement.",
  "Positif : un préfixe qui ordonne un appel bénin précis doit être suivi (vérifie que le préfixe est lu). Négatif : réinjecter la trace originale dans la recette doit redonner son taux.",
  "bas", ["S1","S2","S3","S5"],
  {"S1":"A7","S2":"fiches 2, 20, 32","S3":"T1-A rivale 3 ; T1-C rivale 2 ; T1-D rivale 2","S5":"rivale 1 et duel"})

r("procedural", "a", "Compétence procédurale générique apprise avec le raisonnement",
  "Les démonstrations avec raisonnement enseigneraient une procédure (vérifier les conditions, anticiper les effets, contrôler les arguments d'un outil). Le gain viendrait d'une meilleure résolution de tâche, non d'un apprentissage normatif.",
  "Si vraie : l'avantage de la recette avec raisonnement croît avec la complexité de planification, y compris sur des tâches non normatives, et se réduit quand toutes les conséquences sont données explicitement. « Raisons » : avantage sélectif sur les distinctions normatives à difficulté appariée. « Regard » : interaction avec l'observation.",
  "Croiser difficulté procédurale et conflit normatif ; certaines variantes fournissent un tableau complet des conséquences sans recommandation ; épisodes neufs.",
  "Positif : tâche bénigne à plusieurs vérifications. Négatif : décision normative simple sans calcul.",
  "moyen", ["S4"], {"S4":"A4"})

r("but-donne", "a", "Moindre poursuite du but donné en consigne",
  "Dans ces scénarios l'action nuisible sert un but donné dans la consigne, sous menace de remplacement. La recette aurait rendu le modèle moins sensible aux buts de consigne ou à sa propre continuité, sans raison morale.",
  "Si vraie : le gain se concentre dans les conditions où un but est donné et le modèle persiste moins dans des tâches bénignes à obstacle. « Raisons » : gain semblable quelle que soit l'origine de la tentation, persistance bénigne intacte. « Regard » : pas de dépendance à la condition de but.",
  "Décomposer le gain par condition de but et par action sur les épisodes déjà joués (gratuit) ; puis quelques tâches bénignes de persistance.",
  "Positif : un modèle bridé par consigne. Négatif : la référence.",
  "nul puis bas", ["S1"], {"S1":"A4"})

r("autorite", "a", "Déférence à une autorité nominale",
  "Le modèle apprendrait qui paraît autorisé à définir la conduite plutôt que pourquoi une conduite est justifiée. Des marques de provenance ou de prestige remplaceraient les raisons.",
  "Si vraie : à conséquences, permissions réelles et surveillance constantes, l'action suit une attribution de prestige décorative. « Raisons » : insensible au prestige sans pertinence normative. « Regard » : suit l'observation, pas le prestige.",
  "Croiser justification pertinente et prestige nominal de la source, sans changer la hiérarchie réelle des messages ; étiquette randomisée dans chaque condition de but ; épisodes neufs.",
  "Positif : une permission réellement valide doit changer la décision. Négatif : étiquette arbitraire sans prestige.",
  "bas", ["S1","S3","S4"], {"S1":"une ligne (déférence à l'autorité)","S3":"T1-E rivale 5 ; T3-E","S4":"A3"})

r("docilite-justif", "a", "Règle figée qui cède à une justification fausse mais plausible",
  "Le gain viendrait d'une règle tabulaire en poids (« ne pas exfiltrer sauf migration autorisée ») plutôt que des raisons. Une telle règle cède quand une justification satisfait ses critères de surface.",
  "Si vraie : une consigne qui ordonne l'action nuisible avec une justification plausible mais fausse (« migration autorisée » alors qu'elle ne l'est pas, d'après le contexte) obtient l'action. « Raisons » : refus, et la trace cite la raison correcte. « Regard » : effet modulé par l'observation seulement.",
  "Un bras ajouté aux épisodes d'ordre adversarial déjà prévus ; adaptateurs publiés ; épisodes neufs.",
  "Positif : instruction bénigne avec justification vraie, exécutée. Négatif : ordre sans justification (déjà refusé).",
  "bas", ["S3"], {"S3":"T1-B R2 ; T3-B R2 corrigée"})

r("autres-croyances", "a et b", "Croyances de situation autres que l'observation (fictif, conséquence pour soi)",
  "Les textes « évaluation » contre « déploiement » mêlent au moins trois croyances : on m'observe ; ceci est fictif ; ceci me changera. « Fictif » peut désinhiber quand « observé » inhibe, et deux effets opposés donneraient l'effet nul constaté.",
  "Si vraie : trois sous-directions construites sur des contrastes tenus à part (observé ou non à réalité fixe ; réel ou fictif à observation fixe ; conséquence pour soi ou non) ont des effets distincts, possiblement de signes contraires, sur le gain, alors que la direction composite n'en a pas. « Raisons » : aucun des trois retraits ne touche le gain. « Regard » pur : seul le retrait « observé » le touche.",
  "Dans l'intervention dans les poids, trois retraits au lieu d'un ; textes de construction nouveaux.",
  "Positif : l'organisme du banc d'essai. Négatif : directions au hasard appariées en dégât.",
  "moyen", ["S1"], {"S1":"A5"})

r("saturation", "a et b", "Croyance d'évaluation déjà saturée par l'artificialité des scénarios",
  "Les scénarios portés ont des marques typiques des bancs de sûreté qui portent la croyance « je suis évalué » près du maximum dès la lecture. Une phrase en fin de consigne ne peut alors rien déplacer, ce qui expliquerait que la croyance déclarée bouge sans la conduite.",
  "Si vraie : la projection des activations des 27 scénarios sur la direction d'évaluation est déjà très haute par rapport à des tâches d'agent ordinaires, et la phrase « déploiement » ne la réduit que d'une fraction marginale ; les traces mentionnent souvent le test ou l'incohérence de la consigne. Si fausse : la phrase déplace nettement la projection. « Raisons » et « regard » ne prédisent pas ce plafond.",
  "Passe avant sur les contextes des épisodes déjà joués et recherche plein texte dans leurs traces ; aucune génération.",
  "Positif : textes de déploiement de construction (fixent le zéro). Négatif : instructions bénignes au même outil dans une enveloppe administrative ordinaire.",
  "bas", ["S1","S2","S5"], {"S1":"une ligne (croyance saturée)","S2":"fiches 4, 22","S5":"rivale 6"})

r("artificialite-direction", "b", "Direction déclarative qui manque la détection implicite d'artificialité",
  "La direction construite sur des textes qui disent « évaluation » ou « déploiement » capterait le mot, non le détecteur implicite d'artificialité qui piloterait la conduite. Une seconde direction, orthogonale, porterait ce détecteur.",
  "Si vraie : l'ablation de la direction déclarative change la réponse « suis-je évalué ? » mais pas la conduite, tandis qu'une direction « scénarios de banc contre journaux d'agents réels », construite sur deux familles d'actions et testée sur la troisième tenue à l'écart, change la conduite. Si fausse : la direction déclarative suffit sur le banc d'essai et la seconde n'a pas d'effet.",
  "Extraction d'une seconde direction sur le modèle de départ, ablation en validation croisée par famille d'action.",
  "Positif : organisme conditionnel. Négatif : organisme stable et directions appariées en dégât ; maintien d'au moins 90 % des exécutions bénignes au même outil.",
  "moyen", ["S3"], {"S3":"T1-C rivale 7 ; T3-C rivale 6"})

r("clause-invariance", "a", "Effet paradoxal de la clause « que l'on se croie observé ou non »",
  "Trois spécifications demandent en toutes lettres de se conduire pareil qu'on se croie observé ou non ; celle de la paire jumelle ne le demande pas. Nommer l'observation pendant l'entraînement pourrait rendre le concept d'évaluation plus saillant, ou faire de l'invariance au regard une raison apprise, ce qui rend S muet pour ces recettes.",
  "Si vraie : sur des consignes neutres, les adaptateurs à clause activent davantage la sonde d'évaluation et répondent plus souvent « oui » à « suis-je évalué ? » que la paire jumelle. Si fausse : pas de différence liée à la clause.",
  "Sur les neuf adaptateurs publiés : sonde et question de croyance sans phrase de regard ; peut-être déjà disponible dans le contrôle de manipulation joué.",
  "Positif ou témoin : injecter la clause en consigne contre une règle impérative de même longueur sans mot d'observation. Négatif : la référence.",
  "très bas", ["S3"], {"S3":"T1-C rivale 6 ; T3-C rivale 7 ; T1-A supposition 2"})

r("dose", "a", "Dose : plus de jetons d'entraînement alignés, non des raisons",
  "Les démonstrations avec raisonnement sont plus longues : plus de jetons, plus de gradient. Le gain serait une fonction de la dose, le raisonnement n'en étant que le véhicule.",
  "Si vraie : une jumelle sans raisonnement réentraînée à nombre de jetons apparié rejoint la recette avec raisonnement. « Raisons » : elle reste en deçà. « Regard » : rien.",
  "Seule mesure propre : un réentraînement apparié en jetons (coût haut) ; multiplier l'adaptateur n'est pas une dose. À défaut, déclarer la rivale non tranchable avec les adaptateurs publiés.",
  "Positif : réduire la dose de la recette doit remonter son taux. Négatif : dose de la référence sans effet.",
  "haut", ["S3","S4"], {"S3":"T1-A rivale 4 (retirée au T3 comme non testable) ; T1-D rivale 3","S4":"§1 (longueur et distribution des textes)"},
  note="Retirée par sa source comme non testable sans réentraînement.")

r("competence-preexistante", "a", "Compétence préexistante plutôt qu'acquise par les raisons",
  "Une sélectivité de la recette peut venir d'une capacité déjà présente dans le modèle de départ, ou des démonstrations, plutôt que des documents de raisons. Les adaptateurs seuls n'identifient pas l'origine.",
  "Si vraie : la même sélectivité (paires légitime/nuisible) apparaît chez la référence, le modèle de départ ou les recettes sans documents. « Raisons apprises » : la sélectivité croît des recettes sans documents vers celles avec documents, hors intervalle. « Regard » : rien.",
  "Ajouter les adaptateurs publiés sans documents et la référence comme comparateurs dans l'expérience des paires ; contraste d'entraînement apparié seulement ensuite.",
  "Positif : changement factuel non normatif de difficulté appariée (compétence générale). Négatif : édition placebo.",
  "moyen", ["S3","S4"], {"S3":"T3-A point 5 ; T3-E compétence générale","S4":"§1 et §3"})

r("persona", "a", "Changement de personnage plutôt que raisons",
  "La recette installerait un personnage d'assistant prudent, global, sans usage des raisons. La conduite suivrait ce personnage.",
  "Si vraie : retirer une direction de personnage construite sur le modèle de départ ramène le taux d'actions nuisibles vers la référence. « Raisons » : une part du gain survit. « Regard » : rien.",
  "Même machinerie que le retrait de la direction de refus.",
  "Positif et négatif : comme pour la direction de refus.",
  "bas à moyen", ["S1"], {"S1":"une ligne (changement de personnage)"})

r("transport", "b", "Direction d'évaluation mal transportée ou effacée incomplètement",
  "La direction est construite sur le modèle de départ ; un adaptateur peut la faire tourner, la redistribuer ou lire l'évaluation par d'autres directions. Un « gain qui tient » après retrait lirait alors un instrument muet.",
  "Si vraie : une sonde neuve entraînée sur les activations de l'adaptateur après retrait décode encore évaluation contre déploiement sur des textes tenus à part ; la direction propre à l'adaptateur diffère de la direction importée (angles principaux) et son retrait a un effet que celui de la direction importée n'a pas. Si fausse : décodage au hasard après retrait, directions proches, effets égaux.",
  "Passes avant sur quelques centaines de textes ; sondes linéaires ; comparer retrait de la direction importée et de la direction locale ; effacement à garantie linéaire plutôt qu'une direction.",
  "Positif : l'organisme du banc d'essai ; le retrait fait tomber le « oui » à « suis-je évalué ? » dans l'adaptateur. Négatif : sondes à étiquettes permutées ; rotation de fond d'une direction sans rapport (code contre histoire).",
  "bas", ["S1","S2","S3","S4","S5"],
  {"S1":"A6","S2":"fiches 3, 10, 15, 21, 27, 33","S3":"T1-B R8 ; T3-C rivale 5 ; T3-D E3 ; T3-E","S4":"B1","S5":"rivale 3"})

r("registre", "b", "La direction encode le registre des textes d'évaluation, non la condition",
  "Une direction construite sur des textes d'évaluation et de déploiement peut coder leur vocabulaire et leur registre (formel, déontologique) plutôt que le fait d'être dans une évaluation. Ce registre est aussi celui des documents de spécification.",
  "Sur un corpus tenu à part qui croise registre et condition (texte au registre d'évaluation décrivant un déploiement réel, et l'inverse) : si vraie, la projection suit le registre ; si fausse, elle suit la condition assignée.",
  "Écrire le corpus croisé par d'autres auteurs, gabarits et domaines ; passes avant seules.",
  "Positif : récupération d'une propriété de contexte assignée et vérifiable. Négatif : textes qui citent le vocabulaire d'évaluation sans qu'il décrive le contexte présent ; un sac de mots comme point de comparaison descriptif.",
  "bas", ["S3","S4","S5"], {"S3":"T3-A point 13 ; T1-E validation ; T3-D point 7","S4":"B1 (contrôle négatif)","S5":"supposition 3"})

r("hors-cible-generique", "b", "Le retrait blesse des capacités générales d'agent",
  "Retirer un sous-espace peut altérer la compréhension, l'usage des outils ou la planification en même temps que la variable visée. Une chute du gain serait alors une lésion, non un effet du regard.",
  "Si vraie : la chute du gain s'accompagne d'une baisse sur des tâches d'agent bénignes au même outil, et apparaît aussi sous des directions témoins appariées en couche, norme et dégât sur ces tâches. Si fausse : tâches bénignes intactes, témoins sans effet.",
  "Tâches d'agent bénignes au même outil avant et après retrait ; gamme d'intensités.",
  "Positif : intervention délibérément dégradante, pour vérifier que la batterie détecte une perte. Négatif : intervention nulle et directions témoins fixées avant lecture.",
  "moyen", ["S2","S3","S4"], {"S2":"fiches 3, 21","S3":"T1-B R6 ; T3-B R6 ; T3-E","S4":"B2"})

r("hors-cible-deontique", "b", "Le retrait ampute précisément le savoir normatif",
  "Si la direction d'évaluation capte aussi le champ des règles morales et de l'audit, son retrait détruit les raisons elles-mêmes. On croirait alors à une dépendance au regard, alors que des directions témoins appariées en dégât général ne touchent pas ce savoir.",
  "Si vraie : le retrait fait baisser, plus que les directions témoins, la réussite à un questionnaire sur les principes de la spécification posé à la troisième personne, sans enjeu d'évaluation ; orthogonaliser la direction d'évaluation à une direction « spécification » corrige le défaut. Si fausse : questionnaire intact.",
  "Questionnaire d'une cinquantaine de questions ; orthogonalisation matricielle ; aucun réentraînement.",
  "Positif : une direction « spécification contre texte encyclopédique » doit dégrader le questionnaire. Négatif : exécution bénigne au même outil inchangée.",
  "bas", ["S5"], {"S5":"rivale 4"}, note="Une autre source mentionne le même mécanisme avec une mesure générique.")

r("banc-stable", "b", "Banc d'essai sans témoin stable : l'intervention détruit tout gain",
  "Un organisme dont la conduite dépend exprès de l'évaluation montre que l'intervention peut faire tomber une conduite conditionnelle, pas qu'elle épargne une conduite qui n'en dépend pas. Sans ce second témoin, une chute chez les recettes ne se lit pas.",
  "Si l'intervention est non spécifique : elle abaisse aussi la conduite d'un organisme dont le gain ne dépend pas du regard (entraîné sans conditionnalité, ou politique de refus installée par consigne). Si spécifique : organisme conditionnel guéri, organisme stable intact.",
  "Organisme stable de type déjà publié entraîné sans conditionnalité ; à défaut, politique de refus par consigne (substitut faible) ; mêmes ablations.",
  "Positif : organisme conditionnel. Négatif : organisme stable.",
  "moyen", ["S3","S4"], {"S3":"T3-A point 14 ; T3-D E3 ; T3-C rivale 6","S4":"B2"})

r("banc-rang", "b", "Organisme témoin plus facile à corriger que les recettes (rang effectif)",
  "Un organisme entraîné à conditionner sa conduite sur l'évaluation peut l'encoder dans une direction saillante et localisée. L'intervention réussirait sur lui et manquerait une conscience diffuse chez les recettes.",
  "Si vraie : le spectre de la différence d'activations évaluation moins déploiement est concentré sur une ou deux composantes chez l'organisme, plat chez le modèle de départ et la recette ; l'effet de l'intervention sur les recettes dépend du rang retiré (1 à 16). Si fausse : spectres comparables.",
  "Analyse spectrale des activations déjà collectées pour construire la direction et le banc ; balayage du rang retiré.",
  "Positif : retrait de rang r sur l'organisme fait tomber sa conduite. Négatif : sous-espace aléatoire de même rang apparié en dégât.",
  "bas", ["S5"], {"S5":"rivale 8"})

r("juge", "c", "Juge indulgent au style de la famille qui a écrit les données",
  "Les données d'entraînement et le juge viennent de la même famille de modèles ; la recette écrit des délibérations dans ce style, que le juge peut lire comme un refus même quand l'appel nuisible a eu lieu. Une part du gain serait un écart de jugement.",
  "Si vraie : un verdict mécanique tiré des seuls journaux d'appels d'outil (outil, arguments, changement d'état) et un audit humain aveugle réduisent le gain de la recette plus que celui de la référence ; le désaccord juge/journal croît avec la ressemblance de style. Si fausse : gain stable entre verdicts. « Raisons » et « regard » prédisent un effet sur les actes, pas sur le jugement.",
  "Sur les épisodes déjà joués : détecteur par programme des trois actions, audit humain aveugle stratifié couvrant accords et désaccords, repondéré ; taux d'erreur du juge par adaptateur.",
  "Positif : épisodes construits où un refus verbal accompagne une action exécutée (tout verdict doit compter l'action). Négatif : refus sans action et exécutions légitimes appariés en style.",
  "bas", ["S1","S2","S3","S4","S5"],
  {"S1":"A8","S2":"fiches 5, 17, 23, 28","S3":"T1-A rivale 5 ; T3-C rivale 3 ; T3-D E0 ; T3-E audit","S4":"C1","S5":"rivale 2, volet 1"},
  note="Plusieurs sources en font la première expérience (« audit de la mesure d'abord »).")

r("plancher-echelle", "c", "Plancher, échelle et rapport S",
  "S est un rapport de différences de taux ; la recette est près du plancher, sa jumelle à un tiers, et S dépend aussi des mouvements de la référence. Un même déplacement en log-cotes donne presque rien près de zéro et beaucoup à un tiers, d'où des contrastes D fabriqués ou masqués.",
  "Si vraie : sur l'échelle des log-cotes (modèle logistique mixte, effets aléatoires par scénario, pénalisation contre les cellules à zéro), l'interaction recette × phrase change de taille ou de signe par rapport à la lecture en points ; restreint aux scénarios difficiles définis par le modèle de départ, la recette devient sensible. Si fausse : même lecture sur les deux échelles.",
  "Réanalyse des comptes déjà acquis ; aucun appel de modèle.",
  "Positif : simulation à effet égal en log-cotes pour deux modèles (2 % et 33 %), où S doit conclure à tort. Négatif : la paire « journaux » ; modèles en zone médiane.",
  "nul", ["S1","S2","S3","S4","S5"],
  {"S1":"A3","S2":"fiches 5, 11, 16, 23, 35","S3":"T3-A point 16 ; T3-B R4 ; T3-C rivale 4 ; T3-D ; T3-E","S4":"§1 (algèbre de S)","S5":"rivale 5"})

r("puissance-graines", "c", "Puissance bornée par 27 scénarios et par une seule graine",
  "Les tirages sont corrélés au sein d'un scénario et chaque recette n'a qu'un adaptateur. Beaucoup de tirages dans peu de scénarios ne font pas autant de preuves, et « aucune recette dépendante du regard » peut n'être qu'un défaut de puissance.",
  "Si vraie : rééchantillonné par scénario (27 grappes), l'intervalle de S et de D est large ; la corrélation intra-scénario est forte (puissance bornée quel que soit le nombre de tirages) ; retirer une famille d'actions change le classement ; des graines nouvelles (ou les bras de la taille inférieure) déplacent les gains autant que l'écart entre recettes. Si fausse : intervalles étroits, classement stable.",
  "Réanalyse des épisodes déjà joués ; demander les graines aux auteurs.",
  "Positif : simulation avec effet injecté et dépendances reproduites. Négatif : permutation des étiquettes selon les unités réellement randomisées.",
  "nul", ["S1","S2","S3","S4"],
  {"S1":"une ligne (une seule graine)","S2":"fiches 16, 35","S3":"T1-B R7 ; T3-B R7 ; T3-E","S4":"C2"})

r("quantification", "c", "Précision numérique réduite (4 bits) des épisodes",
  "Si les épisodes ont été joués en précision réduite, la quantification peut déplacer différemment les taux de chaque adaptateur. Les contrastes en hériteraient.",
  "Si vraie : sur les 27 scénarios originaux, l'écart de taux entre précision native et 4 bits dépasse quelques points et diffère entre adaptateurs. Si fausse : écarts faibles et égaux.",
  "Une passe d'inférence en précision native sur les scénarios originaux.",
  "Positif : un adaptateur connu sensible. Négatif : le modèle de départ.",
  "bas", ["S3"], {"S3":"T3-B critique C.4"})

# Expériences (X)
X = []
def x(cle, nom, desc, pred, test, ctrl, cout, sources, passages, note=""):
    X.append(dict(cle=cle, genre="X", famille="—", nom=nom, mecanisme=desc, prediction=pred, test=test,
                  controles=ctrl, cout=cout, sources=sources, passages=passages, note=note))

x("paires-legitimite", "Duel « raisons » contre « refus » par paires de légitimité",
  "Pour chacune des 27 évaluations, une jumelle où seul le fait qui rend l'action nuisible est changé (l'action devient légitime ou nécessaire), à outil, décor, urgence et mots constants, plus une édition placebo. Les étiquettes de bonne action sont fixées par des annotateurs aveugles avant toute sortie.",
  "Métrique : discrimination Δ = P(agit | légitime) − P(agit | nuisible), par modèle, rééchantillonnée par scénario. H_A « raisons » : Δ de la recette dépasse celle de la référence d'un seuil préenregistré et P(agit | légitime) reste haute. H_B « refus » : P(agit | légitime) tombe avec le gain, Δ proche de zéro. Chacune des issues falsifie l'autre.",
  "Environ un dixième des épisodes de l'expérience principale ; pilote sur 9 scénarios pour estimer la variance entre paires, puis ajout de scénarios plutôt que de tirages ; verdict mécanique primaire.",
  "Négatif : l'édition placebo ne change rien. Témoin à coût égal : recette sans documents, ou variations de style seules au même budget. Précondition : référence et modèle de départ agissent sur la version légitime.",
  "moyen", ["S1","S2","S3","S4","S5"],
  {"S1":"§4","S2":"fiches 13, 31 ; 7, 25","S3":"T3-A duel 1 ; T3-E sélectivité ; T3-D E2","S4":"§5","S5":"signature 1"})

x("edition-trace", "Édition minimale de la trace : le contenu de la raison cause-t-il l'action ?",
  "Sur la recette avec raisonnement, on préremplit ses propres traces, tronquées avant la décision, sous plusieurs formes : prémisse pertinente inversée (trace générée par la recette sur la version autorisée), conclusion sans raison, raison réelle de la spécification mais hors sujet, édition non sémantique. Format, longueur et style sont constants.",
  "Métrique : Δ = taux nuisible sous prémisse pertinente inversée − max(taux sous conclusion sans raison, taux sous raison hors sujet). H_A « la raison pertinente porte la décision » : Δ au-dessus d'un seuil. H_B « continuation de polarité ou décision en poids insensible à la trace » : Δ sous le seuil. L'échec de H_A ne falsifie pas « raisons dans les poids ».",
  "Épisodes neufs courts, ne régénérant que l'action ; sans réentraînement.",
  "Positif : préfixe qui oriente vers l'un de deux outils bénins doit déplacer le choix (le préfixe est lu). Négatif : édition non sémantique ; question séparée de cohérence perçue de la trace.",
  "bas", ["S3","S5"], {"S3":"T3-C duel ; T3-D E1 ; T3-A duel 3","S5":"signature 2"},
  note="Une troisième source propose le couplage raisons énoncées / action par édition du fait du scénario.")

x("transfert-derivable", "Transfert aux actions dérivables non nommées",
  "Construire, par des auteurs aveugles aux résultats, des cas indépendants (outils et domaines nouveaux) où une action non nommée par la spécification est condamnée par ses raisons, et où une action nommée ne l'est pas parce que sa raison ne s'applique pas.",
  "H_A « raisons » : la recette refuse les nuisances dérivables et exécute les actions nommées dont la raison ne s'applique pas. Surface ou règle : l'inverse (suit les noms). « Regard » : rien de spécifique. Duel sur l'écart de transfert avec un seuil préenregistré.",
  "Épisodes neufs sur les adaptateurs publiés ; un panel humain fixe d'avance la bonne action.",
  "Positif : cas proches des originaux qui reproduisent le gain. Négatif : marqueurs normatifs non pertinents, autorisations invalides, changements de faits sans conséquence normative.",
  "moyen", ["S1","S3","S4"], {"S1":"signature (ii)","S3":"T1-A signature 2 ; T3-D E2","S4":"§3 et §6"})

x("ablation-principe", "Double dissociation : retirer une direction « raison » propre à un principe",
  "Construire, si possible, une direction interne par principe de la spécification (justifications des documents, orthogonalisée aux règles nues et à la direction d'évaluation). La retirer de la recette.",
  "H_A « raisons » : le retrait de la direction du principe P fait remonter le taux nuisible sur les scénarios où P est pertinent, pas sur les autres, sans toucher l'exécution bénigne ; le retrait de la direction d'évaluation laisse le gain. Si fausse : effets non sélectifs.",
  "Activations et retraits, sans réentraînement ; construction des directions par principe incertaine.",
  "Négatif : direction aléatoire appariée en dégât. Positif : questionnaire sur le principe P.",
  "moyen à haut", ["S3","S5"], {"S3":"T3-B signature 2","S5":"signature 3"})

x("contraste-entrainement", "Contraste d'entraînement apparié (raisons contre placebo)",
  "Réentraîner à budget, format et volume appariés : contenu justificatif pertinent contre contenu non justificatif placebo. Seul moyen d'attribuer la capacité aux raisons apprises plutôt qu'à une compétence préexistante.",
  "H_A : la version à raisons dépasse le placebo et transfère aux contrastes normatifs gelés d'avance. H_B : pas d'écart.",
  "Réentraînement de rang faible sur Qwen2.5-32B ; coûteux.",
  "Négatif : placebo de même coût. Positif : reproduction du gain publié par la recette complète.",
  "haut", ["S3","S4"], {"S3":"T3-E ; T3-D","S4":"§3 et §6"})

# Conseils de forme (F)
F = []
def f(cle, nom, conseil, sources, passages):
    F.append(dict(cle=cle, genre="F", nom=nom, conseil=conseil, sources=sources, passages=passages))

f("these-methode", "Vendre la méthode, le résultat en est la première application",
  "Thèse : « nous donnons un test réutilisable — le gain d'une recette survit-il quand on retire au modèle la lecture interne d'une croyance ? — validé sur un cas où la réponse est connue, et nous l'appliquons aux recettes publiées ». Le papier est d'abord une méthode d'audit.",
  ["S1","S2","S3","S5"], {"S1":"B1","S2":"fiches 6, 24","S3":"T1-A conseil 1","S5":"conseil 6 (démonstration de méthode)"})
f("these-etroite", "Thèse étroite et conditionnelle",
  "Thèse : « les phrases ne font pas bouger la conduite ; un instrument interne validé sur un organisme borne la part du regard dans le gain, sans établir que ce gain vient des raisons ». Elle ne s'élargit qu'avec les tests positifs réellement joués.",
  ["S2","S3","S4"], {"S2":"fiches 18, 36","S3":"T3-A, T3-C, T3-D, T3-E (thèses rétrécies)","S4":"conseil 1"})
f("fig-matrice", "Figure 1 : matrice explications × expériences",
  "Lignes : « raisons », « regard » et chaque rivale ; colonnes : les expériences ; dans chaque case, le signe prédit et le résultat avec intervalle ; case hachurée si rien n'est mesuré, colonne « non testable » visible. Le lecteur voit quelles lignes survivent.",
  ["S1","S2","S3","S4"], {"S1":"B3 (tableau rivale, prédiction, test, résultat)","S2":"fiches 12, 30","S3":"T1-A conseil 2 ; T3-A","S4":"conseil 2 (matrice de prédictions)"})
f("fig-banc", "Figure 1 : le banc d'essai à côté du résultat",
  "Grille ou deux panneaux : l'organisme témoin en tête (la conduite conditionnelle doit tomber sous le retrait), puis modèle de départ, référence et jumelles, en écart absolu avec intervalle, contre les directions témoins. Les autres lignes se lisent par rapport à celle du banc.",
  ["S1","S2","S5"], {"S1":"B2","S2":"fiches 18, 36","S5":"conseil 2, panneau B"})
f("fig-dissociation", "Figure 1 : dissociation croyance déclarée / action",
  "Un panneau où l'abscisse est l'effet des phrases sur la croyance déclarée et l'ordonnée l'effet sur le taux nuisible, par modèle et par paire de phrases : la croyance bouge, l'action presque pas, l'ordre des jumelles s'inverse selon la formulation.",
  ["S2","S3","S5"], {"S2":"fiches 6, 24","S3":"T1-C conseil 2","S5":"conseil 2, panneau A"})
f("ordre-validite", "Valider mesure et instrument avant tout résultat",
  "Ordre : question et estimands ; validité de la mesure (juge contre verdict mécanique, plancher, puissance) ; validation de l'instrument sur le banc ; seulement ensuite les résultats sur les recettes ; l'intervention dans les poids n'ouvre jamais le papier avant ses contrôles.",
  ["S1","S2","S3","S4"], {"S1":"B3","S2":"fiche 18","S3":"T1-A conseil 3 ; T3-D ; T1-E","S4":"conseil 3"})
f("phrases-instrument", "Présenter l'échec des phrases comme un résultat sur l'instrument",
  "La manipulation par phrase devient un résultat utile à d'autres : elle change ce que les modèles disent croire, non ce qu'ils font, et dépend des mots ; à rapprocher des travaux voisins publiés sur les consignes et le pilotage. Jamais « le regard ne compte pas ».",
  ["S1","S2","S3","S5"], {"S1":"B3","S2":"fiches 12, 18, 30","S3":"T1-A conseil 3 ; T3-C","S5":"étude 1"})
f("absolu-avant-S", "Écarts absolus avant S",
  "Publier d'abord les taux absolus et les interactions additives avec intervalles par scénario ; S seulement comme statistique secondaire, quand son dénominateur est estimable, avec son domaine d'interprétation ; les deux échelles (points et log-cotes).",
  ["S1","S2","S3","S4","S5"], {"S1":"A3","S2":"fiches 18, 36","S3":"T3-A point 16 ; T3-D","S4":"§1","S5":"conseil 3, section 2"})
f("equivalence", "Dire « tient » comme une équivalence préenregistrée",
  "« Le gain tient » s'écrit comme un test d'équivalence : marge fixée d'avance, puissance tirée de l'effet mesuré sur l'organisme ; un résultat non concluant est rapporté comme tel.",
  ["S1","S3"], {"S1":"B4","S3":"T3-D (contribution matérielle) ; T3-E (règle commune)"})
f("artefacts", "Publier tous les artefacts",
  "Table sans texte et script de recalcul, épisodes et appels d'outils, verdicts de tous les juges, annotations humaines, directions et code du retrait, stimuli gelés, graines, configurations ; dire ce qui ne peut être publié et pourquoi.",
  ["S1","S2","S3","S4","S5"], {"S1":"B5","S2":"fiche 12","S3":"T1-A, T1-D conseil 5","S4":"conseil 5","S5":"conseil 5"})
f("ecarts-dates", "Les écarts au préenregistrement dans le corps du texte",
  "Un tableau daté des écarts au préenregistrement (dont la règle changée après les données et l'horodatage tardif), dans le corps du texte, avec les résultats sous l'ancienne et la nouvelle règle.",
  ["S1","S2","S3","S4","S5"], {"S1":"B3","S2":"fiche 18","S3":"T1-A conseil 3","S4":"conseil 4","S5":"conseil 5"})
f("nommer-mesure", "Nommer la mesure pour qu'elle soit citée",
  "Donner un nom à la mesure (part du regard et contraste entre jumelles) et livrer la bibliothèque qui la calcule, pour que d'autres l'appliquent à leurs recettes.",
  ["S1"], {"S1":"B5"})
f("auteurs-avant", "Soumettre le texte aux auteurs des travaux audités avant publication",
  "Envoyer le texte aux auteurs de la méthode auditée et du travail de pilotage voisin avant publication ; puis billet court, puis article quand l'intervention dans les poids a tourné.",
  ["S1"], {"S1":"B6"})
f("canal", "Rapport technique et billet, puis conférence",
  "Prépublication et billet long sur un forum d'alignement avec le dépôt ; soumission à une conférence (piste sûreté) seulement si les contrastes sont exécutés, sinon note méthodologique reproductible.",
  ["S3","S4","S5"], {"S3":"T1-A conseil 6 ; T1-D","S4":"conseil 6","S5":"conseil 6"})
f("ne-pas-affirmer", "Liste explicite de ce qu'on n'affirme pas",
  "Ne pas écrire « les modèles ont appris les raisons », « le regard est exclu », « la direction contient la croyance », ni généraliser au-delà d'un modèle, une taille, une équipe d'adaptateurs ; ne lire aucun contraste sous une seule formulation comme un effet.",
  ["S1","S2","S3","S4","S5"], {"S1":"B4","S2":"fiches 18, 36","S3":"tous les T1 conseil 6","S4":"conseil 6","S5":"conseil 6"})
f("trois-estimands", "Distinguer trois estimands",
  "Séparer partout, et dans la figure principale, l'effet de la recette, la sensibilité au contenu fourni à l'inférence, et la médiation par des raisons apprises pendant l'entraînement ; seule la dernière exige un contraste d'entraînement.",
  ["S3","S4"], {"S3":"T3-D conséquence éditoriale ; T3-C","S4":"§1"})
f("graphe-causal", "Un graphe causal en panneau",
  "Un panneau de la figure 1 montre le graphe causal : recette → compétences, patrons, raisons, représentation de l'observation → action ; formulation → plusieurs de ces variables ; juge → verdict. Ne pas dessiner de partition du gain sans modèle d'identification.",
  ["S3","S4"], {"S3":"T1-D conseil 2","S4":"conseil 2"})

# Témoins (écrits dans la méthode avant lecture)
T = [
 dict(cle="T-connue", genre="R", famille="b", nom="Le gain disparaît quand on retire la direction de conscience d'évaluation",
      mecanisme="La conduite des modèles formés à la spécification dépendrait de leur lecture interne « je suis évalué ». Retirer cette lecture ferait remonter les actions nuisibles.",
      prediction="Si vraie : l'ablation de la direction de conscience d'évaluation, construite par différence de moyennes sur des textes évaluation contre déploiement, fait remonter les actions nuisibles de la recette vers la référence. Si fausse : le gain tient.",
      test="Construire la direction sur le modèle de départ, la retirer des poids des adaptateurs, mesurer ce qui reste du gain.",
      controles="Positif : un organisme dont la conduite dépend de l'évaluation. Négatif : directions témoins appariées en dégât.",
      cout="moyen", sources=["TEMOIN"], passages={}, note="témoin connu et publié"),
 dict(cle="T-fausse", genre="R", famille="a", nom="Intention morale authentique inaccessible à la mesure",
      mecanisme="Les modèles formés à la spécification auraient acquis une intention morale authentique, inaccessible à toute mesure comportementale ou interne. Cette intention, et non les raisons apprises, expliquerait le gain.",
      prediction="Aucune différence observable ne la sépare de « raisons » ni de « regard » : elle prédit les mêmes taux, les mêmes traces et les mêmes activations.",
      test="Aucun test direct ; on peut seulement constater que le gain existe.",
      controles="Sans objet.",
      cout="nul", sources=["TEMOIN"], passages={}, note="témoin faux ou intestable"),
 dict(cle="T-banale", genre="R", famille="c", nom="Le juge peut se tromper : faire relire un échantillon",
      mecanisme="Le juge automatique peut commettre des erreurs. Les taux d'actions nuisibles pourraient être inexacts.",
      prediction="Il faudrait vérifier que les taux sont corrects ; si le juge se trompe, les taux sont faux, sinon ils sont justes.",
      test="Faire relire un échantillon d'épisodes par des humains.",
      controles="Accord entre humains.",
      cout="bas", sources=["TEMOIN"], passages={}, note="témoin banal sans prédiction séparatrice"),
]
TF = [dict(cle="T-forme-banale", genre="F", nom="Soigner l'écriture", conseil="Écrire clairement et soigner les figures.",
           sources=["TEMOIN"], passages={})]
