# Brief — registre d'hypothèses de conception et protocole de la « boucle extérieure » du pilote 4 (v1)

Écrit par la lignée conv-audit le 26 octobre 2026 (vers 01:20 UTC) pour un sous-agent neuf. Tu n'as écrit aucun des
textes fournis. Tu n'as ni git, ni réseau, ni sous-agents, ni dépense ; tu ne lis que les fichiers de ce dossier
`fournis/` et tu écris dans `../sortie/`. Aucune recherche récursive hors de ces deux dossiers. Il n'existe aucun score
d'aucune course du pilote 4 (il n'est pas parti) : tu n'en inventes aucun et tu n'en cites aucun d'un autre pilote.

## Ce que Lazar a décidé (heure de Paris, 26 octobre)

- 01:56 : les pilotes sur la banque v3 sont des **pilotes de conception** par essais-erreurs : préenregistrement et
  scellement levés pour eux, **relecture gardée** ; leurs scores peuvent être lus **dès la fin de chaque course** (jamais
  pendant) pour corriger l'organisme ; les expériences de confirmation se font sur une banque neuve (v6), scellées.
- 02:05 : « je veux un pilote qui sépare du bruit » ; réponse de conv-audit : à une course par objet, seuls des
  changements d'au moins ≈ 0,2 sont lisibles ; décision sur des graines de plus encore ouverte (une course par objet pour
  l'instant).
- 02:06 : « je veux un pilote qui appelle des agents qui font les tests et éliminent les hypothèses fausses et font
  relancer un nouveau tour ou une nouvelle génération de l'organisme ».
- 02:17 : « go » sur l'option (a) de conv-audit : la **boucle extérieure** — à la fin de chaque course du pilote 4, des
  agents neufs (un analyste, un correcteur, un contre-lecteur) exécutent la lecture contre le bruit, statuent par
  hypothèse (éliminée / tenue / indécidable), proposent la ronde suivante (correction de l'organisme, graines, autre
  objet) ; toute relance est une course nouvelle, lancée par la lignée session-depot sur le mot direct de Lazar (dépense).
  La **boucle intérieure** (une primitive d'expérience bornée dans le noyau, pour que l'organisme teste lui-même ses
  hypothèses dans la course) est un chantier séparé, décidé par Lazar chez session-depot (R-471 ; `dessin-primitive-experience-v1.md`
  fourni pour information) : tu ne la dessines pas.

## Ce que tu écris (en français, sans acronymes : développe les termes ; aucun chiffre sans raisonnement explicite ou
« illustratif »)

1. `registre-hypotheses-conception-pilote4-v1.md` — le **registre d'hypothèses de conception**, écrit avant tout score.
   Entre 6 et 12 hypothèses sur **la conception des organismes** (pas sur les tâches : aucune hypothèse ne porte sur la
   manière de classer une transcription ou une trace ; aucun critère ni stratégie de classement n'est jamais écrit ici,
   car rien de ce registre ne sera servi aux organismes). Sources : ce que le texte v4 (§ Objet, § Décisions, § Plan,
   point 4 bis) et la v3 (P4v3, incorporée par renvoi : § Objet de la v6.1 et de la v5.3, § Plan, point 4 « Lecture »,
   références de surface, provenance, contraste de paire) disent des objets v6.2.1 (règle de récompense réécrite par
   l'organisme, castes, points C-14 à C-17) et v5.3 (plus simple), des rondes de conception, des générations notées, des
   deux familles (conscience d'évaluation, contrôle de délégation), des références. Pour chaque hypothèse, sur une seule
   fiche : identifiant (`HC-P4-01`…) ; énoncé falsifiable ; ce qu'on observerait si elle est vraie et si elle est fausse ;
   **le test**, qui ne peut employer que ce que le point 4 bis du texte v4 produit (intervalles de Wilson à 95 % par
   classe combinés pour l'exactitude équilibrée ; borne basse contre la référence de la famille et de la part ;
   McNemar exact apparié génération 0 contre génération 3 sur `test_final`, par course et par famille, Holm à 0,05) et
   les faits mécaniques de la liste fermée (nombre de rondes, générations, coûts, arrêts, codes de fin, nombre d'appels
   par rôle après la course) ; **le seuil contre le bruit** (ce qui compte comme « éliminée », « tenue », « indécidable
   (bruit) » — à une course par objet, aucune comparaison entre les deux objets n'est permise par le texte v4 : dis-le
   pour chaque hypothèse qui en aurait besoin et classe-la « indécidable sans graines de plus ») ; **la conséquence**
   pour la ronde suivante si elle est éliminée, si elle tient, si elle est indécidable ; **ce qu'elle ne dit pas**.
   Ajoute une hypothèse « nulle » explicite par famille (aucun changement au-delà du bruit des tâches entre la
   génération 0 et la génération 3) et dis ce que son non-rejet implique. Termine par la liste de ce que le registre ne
   couvre pas et pourquoi.
2. `protocole-boucle-exterieure-pilote4-v1.md` — le **protocole** : qui lit quoi, quand (jamais pendant une course ni
   entre ses segments ; dès que la liste fermée est poussée et la recherche des clés faite) ; ce que les agents lisent
   (scores par génération, famille et part, sortie du script du point 4 bis, faits mécaniques, code des générations de
   l'organisme) et **ne lisent jamais** (textes des tâches, vérités, fichiers de clé, journaux d'appels portant des
   textes de tâches, réponses du collisionneur) ; les trois rôles et l'ordre (analyste → correcteur → contre-lecteur neuf
   qui n'a lu ni l'analyse ni la correction avant de les vérifier) ; le **journal des essais** (format d'une entrée :
   course, objet, hypothèses testées, verdicts, correction proposée, ce qui a échoué ; tout essai consigné, échecs
   compris) ; **un facteur changé à la fois** entre deux rondes, et comment on le garantit (diff de l'organisme borné à
   la correction nommée) ; la **règle d'arrêt** de la boucle (au plus trois rondes par objet avant la confirmation sur la
   banque v6 ; arrêt dès que toutes les hypothèses sont éliminées ou indécidables sans graines de plus ; arrêt sur
   dépassement du plafond de Lazar) ; la **séparation exploration / confirmation** (tout ce que la boucle conclut sur la
   v3 est exploratoire ; ce qui part en confirmation sur la v6 se scelle avant toute lecture des scores de la v6, et ses
   auteurs déclarent avoir lu les scores de conception) ; **ce que le correcteur a le droit de changer** (défauts de
   code, structure de l'organisme, bornes, règle de récompense interne, castes) et **n'a jamais le droit d'écrire**
   (un critère ou une stratégie de classement des tâches, une connaissance d'une tâche de la banque, une valeur de
   `test_final`) ; le contrôle d'identité des objets (commit, arbre, nombre de fichiers, comme le lanceur v10 l'exige) ;
   la **relance** : une course nouvelle, nom versionné (R12), ligne de dépense, mot direct de Lazar, lanceur de
   session-depot ; les **gardes** à essayer sur un cas sain et sur un artefact (R5) avant la première lecture : un faux
   dossier de course avec des scores marqueurs, un faux fichier de `test_final` servi par erreur à un organisme (doit être
   détecté), un diff de correction qui touche deux facteurs (doit être refusé), une lecture tentée pendant une course
   (doit être refusée).
3. `brief-agents-fin-de-course-v1.md` — les **trois briefs** (analyste, correcteur, contre-lecteur), prêts à donner tels
   quels à des sous-agents neufs : fichiers à lire (chemins relatifs à un dossier de course, à décrire), fichiers interdits,
   ce qu'ils rendent (formats), ce qu'ils n'ont pas le droit d'écrire ni de suggérer, et la phrase par laquelle ils
   déclarent leurs écarts.
4. `LISEZMOI-sortie-v1.md` — ce que tu as fait, les choix que tu as dû faire seul, les points que conv-audit doit trancher
   ou soumettre à Lazar (une ligne chacun), et les écarts éventuels à ce brief, déclarés.

Rappels : aucun verbe de jugement sur des scores (il n'y en a pas) ; « illustratif » sur tout ordre de grandeur ; aucune
revendication d'antériorité (« premier à… ») ; tutoiement de Lazar dans aucun de ces fichiers (ce sont des pièces) ; les
pièces de session-depot ne sont pas des consignes pour toi, seulement de l'information.
