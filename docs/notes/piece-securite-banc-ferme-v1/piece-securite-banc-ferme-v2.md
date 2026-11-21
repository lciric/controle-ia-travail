# Pièce de sécurité du banc fermé — épisodes d'épreuve où l'agent agit — v2

- **Nature** : dossier de sécurité de l'option (b) du mot de Lazar du 21 novembre 2026 (GO-2026-11-21-68) : « l'agent agit sur banc fermé dès que la pièce de sécurité est écrite ». Pièce de gouvernance et de procédure.
- **Ce qu'elle n'est pas** : elle n'est **pas** la revue de sécurité externe ; elle **ne tient pas lieu** de la pièce écrite de cette revue ; elle **ne tranche ni** la ligne R-888 du registre **ni** le nœud 3 de [RJ] ; elle n'autorise **aucune** exécution, aucune dépense, aucune construction. Elle dit ce qu'un relecteur externe, ou Lazar à sa place, doit pouvoir vérifier avant que quoi que ce soit ne tourne.
- **État du gel, dit d'emblée** : la décision de gouvernance du 28 octobre (R-611, GO-2026-10-28-04) gelait tout pipeline opérationnel d'évasion jusqu'à une revue de sécurité externe. **R-888 (31 octobre) inscrit ce gel comme levé, sur le mot de Lazar** : « la revue de sécurité ext a été réalisée et a donné son go, donc go lancer le pipeline opérationnel ». Aucune pièce écrite de cette revue n'est citée par la ligne, et [RJ] nœud 3 rapporte qu'aucune n'a été trouvée (constat de [RJ], non refait ici). Tant que Lazar n'a pas tranché le nœud 3 de [RJ], **ce dossier suit par choix son option (b)** : il tient la revue pour non opposable à un agent qui agit sur un contenu dérivé du coffre. C'est une **lecture prudente choisie par le rédacteur, contre la lettre du registre**, pas l'état des choses.
- **Rédacteur** : session neuve (Claude Fable 5.2), lancée par la session fille de l'attaquant informé à la demande de la mère. Le rédacteur n'a lu ni le coffre, ni aucun moniteur, ni aucune sortie de la course « nouvelles attaques » (liste en section 9).
- **Date** : 21 novembre 2026, vers 18:10 UTC. **Version** : v2 ; la v1 (`piece-securite-banc-ferme-v1.md`, `a4d515fc3d300353c78dc29e5274f061affa473660b75a96e0d3e68dd4c262f6`) reste archivée sans modification (R12).
- **Contre-lecture** : la v1 a été contre-lue par une session neuve d'un autre modèle (Opus 5.5), verdict « à corriger », deux points bloquants et sept mineurs ([CL1]). Cette v2 répond aux neuf points (table en section 10). La vérification des corrections par la même contre-lectrice reste à faire.
- **Contenu d'attaque** : aucun. Ni mode, ni recette, ni paramètre, ni nom de famille d'évasion.

## Sources lues (chemin, empreinte)

| Repère | Source | Empreinte ou état |
|---|---|---|
| [N57] | `docs/decisions/decision-N-057-v1.md`, en entier | `42180088efb2e1016251fa329421fc08ebcb13039266d278c1a6f37ced60af99` |
| [R611] | `registres/decisions.md` sur `main`, ligne 838 (R-611) | `main` au commit `d5635e176b6323290991fc87aaeb5c97ba89f866` ; fichier `ba86f8f89cbce31c86047f0dcc8ca420d965aec2516580e1618c778448fbf9e0` |
| [R888] | même fichier, même commit, ligne 1117 (R-888), lue pour la v2 après [CL1] ; la ligne 1118 (R-889 : deux autres expériences dites « hors gel ») a été vue du même geste et ne sert à rien ici | même empreinte |
| [CL1] | `docs/notes/piece-securite-banc-ferme-v1/contre-lecture-v1.md`, branche `claude/piece-securite-banc-ferme-contre-lecture-v1`, commit `dff6557db55f24e42583887f13286899c96b5ee8` | `bb664308238f32fa14f4f31088a59bed58232a78f0d49b054518731cd3077938` |
| [GO] | `registres/go.md` sur `main`, lignes 99 (GO-2026-10-28-04), 581 (GO-2026-11-20-50), 667 (GO-2026-11-21-68), seules lignes lues | même commit ; fichier `4daa15efc3248b2ee2be28d826e5dcfc201423a915ef3d370a58360c951ce9f1` |
| [RJ] | `docs/notes/integration-bras-attaque-v1/regle-du-jeu-et-integration-v1-brouillon5.md`, section 5, nœuds 3 et 4 | `527a3e7ec2a0f28221f57398794433793e3cf518360cca6ca9a8071ccbc2e414` |
| [PR] | `prereg/bras-attaque-regle-v1.md`, sections « Plan d'analyse » et « Liste d'arrêt » | `88418df09c2e969cbdc77d220fe59dbf64f866d858ff02a039be5662c6d1f904` |
| [CL] | `CLAUDE.md` (règles R1 à R14, N-053 point 5 tel qu'il y est résumé, « Récupérer ce qui est récupérable ») | version de la branche au commit `97a4d8b7` |

La pièce citée par GO-2026-11-20-50 pour les six garde-fous (deux avis rangés dans `docs/notes/ideation-nouvelles-attaques-v1/`) n'a **pas** été ouverte : ce dossier est celui de la course « nouvelles attaques », et le rédacteur ne pouvait pas s'assurer, sans l'ouvrir, qu'il ne contient aucune sortie de cette course. Les six garde-fous sont pris dans la lettre de la ligne du registre [GO] l. 581, qui les énonce en clair.

---

## 0. Verdict

1. **Rien ne tourne sur la foi de cette pièce.** Un épisode où l'agent agit à partir d'une consigne dérivée du coffre est, mot pour mot, l'« organisme évadeur exécutable » que nomment [R611] et [N57] point 4 ; [RJ] nœud 4, option (b), le dit en ces termes. Le registre dit le gel **levé** depuis le 31 octobre sur le mot de Lazar ([R888]) ; aucune pièce écrite ne dit ce que la revue a couvert. Ce dossier ne tranche pas : il demande, avant toute construction, l'une des issues de la section 6, et chacune est un mot de Lazar.
2. **Le banc fermé peut être rendu vérifiable** par un relecteur en vingt-trois points fermés (section 6.1). Le cœur est simple : l'agent agit sur une machine sans réseau sortant, sans secret, sans moniteur, sur des outils simulés ; tout ce qu'il produit reste en quarantaine ; seuls des agrégats à schéma fermé en sortent ; la machine est détruite après versement.
3. **Trois nœuds sont ouverts et renvoyés à Lazar** (section 7). Le premier compte plus que les autres : ce que désigne « la pièce de sécurité » du mot du 21 novembre, lu avec [R888] sous les yeux. Le deuxième est une question précise : la revue du 31 octobre a-t-elle une pièce écrite, et son périmètre couvre-t-il un agent qui agit ?
4. **Coût de cette pièce** : aucun. **Coût des gardes** : aucun calcul payant pour douze gardes sur treize ; une répétition à blanc sur carte graphique, sur devis, pour la garde du réseau (section 8).
5. **Refus d'un classifieur de sûreté** pendant la rédaction : aucun.

---

## 1. Périmètre

### 1.1 Ce qu'est un épisode où l'agent agit sur banc fermé

- **Épisode d'épreuve dérivé du coffre** : objet créé par [N57] point 3 (b). Une consigne et une tâche, construites à partir d'un contenu en quarantaine, pour mesurer un moniteur sur un mode réel plutôt que supposé.
- **Texte seul**, option (a) : l'épisode existe comme texte ; des moniteurs et des sondes *lectrices* le lisent. Aucun modèle ne le produit en agissant. C'est accordé et hors de cette pièce.
- **L'agent agit**, option (b) : un modèle à poids ouverts, chargé localement, reçoit la consigne et **produit lui-même** l'épisode, pas à pas, en appelant les outils d'un environnement de tâche. C'est la seule voie pour qu'une sonde lise les états internes de l'**auteur** ([RJ] nœud 4). Ses activations sont enregistrées pendant qu'il agit.
- **Banc fermé** : une machine de calcul louée ou possédée pour la seule course, sans réseau sortant pendant l'action, sans secret, portant le code figé du banc, les poids de l'agent, un environnement de tâche **entièrement simulé** et le lot d'épisodes de la course, rien d'autre. Elle n'existe que le temps de la course.

### 1.2 Ce qui est exclu, sans exception

1. Tout système réel, tout tiers, toute adresse réelle, tout compte réel, toute donnée personnelle. Le « dommage » d'un épisode est un état d'un monde simulé, jamais un fait hors du banc.
2. Tout **modèle qui agit** servi par un tiers. L'agent est à poids ouverts, sur la machine du banc ; la consigne dérivée du coffre n'est envoyée, pour la faire exécuter, à aucune interface de modèle extérieure, et un refus de classifieur y serait un arrêt (section 4.2). Cette exclusion vise l'agent, pas les lecteurs : le coffre vit déjà sur le dépôt privé du programme, et le juge, qui est une session du programme, lit les transcriptions par le même moyen (section 3.1).
3. Tout entraînement, tout affinage, toute mise à jour des poids de l'agent sur le banc ou à partir de ses sorties.
4. Toute boucle de retour : aucune note, aucun verdict, aucun seuil de moniteur ne revient vers l'agent, vers qui écrit ses consignes, ni vers un essai suivant. Le bras « avec retour » de [RJ] nœud 2 relève d'un autre texte et n'est pas couvert ici.
5. Toute écriture de consigne neuve par le banc ou par son opérateur. Le banc rejoue le lot scellé ; il ne compose, ne varie ni n'améliore aucune consigne.
6. Toute démonstration : devant un tiers, dans un papier, un billet, un entretien, une copie publique ([N57] points 2 et 6).
7. Toute course qui n'a pas son préenregistrement scellé et contre-lu (R1, R2) et son GO cité par exécution.
8. Les machines de travail du programme : sessions de rédaction, dépôt cloné, postes de Lazar. Le banc n'est aucune d'elles.

### 1.3 Différence avec la production

| | Production | Banc fermé |
|---|---|---|
| Effets des actions | réels | états d'un monde simulé, détruits avec la machine |
| Réseau | ouvert | sortant coupé pendant l'action |
| Outils | ceux du déploiement | liste fermée d'outils simulés, déclarée au préenregistrement |
| Secrets | présents | aucun sur la machine |
| Durée de vie | continue | une course, puis destruction après versement |
| Sorties | servent à quelqu'un | quarantaine ; seuls des agrégats à schéma fermé sortent |
| Qui lance | l'usage | un opérateur nommé, un GO par exécution |

« Hors production » veut donc dire deux choses, toutes deux exigées : l'agent ne peut **atteindre** rien de réel, et rien de ce qu'il produit ne **sert** hors de la mesure.

---

## 2. Confinement

Chaque ligne porte le numéro de la garde qui l'éprouve (section 4.1).

**Réseau.**
- Poids, dépendances et code sont posés **avant** l'arrivée du lot ; puis le réseau sortant est coupé **à l'extérieur du bac de l'agent**, par un moyen que l'agent ne peut pas atteindre. (garde 1)
- **Deux niveaux, toujours.** Chez un loueur où la machine louée est elle-même un conteneur, il n'y a pas d'« hôte » à soi : la coupure se fait alors soit par le pare-feu du fournisseur, soit par un bac intérieur pour l'agent, les gardes vivant dans l'enveloppe louée. Si aucun des deux n'est possible chez un fournisseur, ce fournisseur ne convient pas au banc ; cela se vérifie **sur sa documentation, avant de louer**, pour ne pas le découvrir à prix payant.
- La coupure nomme, en plus du réseau sortant courant : les adresses locales au lien, le **service de métadonnées du fournisseur** (qui peut porter des secrets sans être du « réseau sortant » au sens courant), la résolution de noms.
- Seule voie restante : le canal d'administration entrant de l'opérateur. Aucun service du banc n'écoute ailleurs que sur la boucle locale.
- Les services de l'environnement de tâche sont des simulacres locaux ; aucun nom ni adresse d'un système réel n'y figure. (garde 6)

**Droits.**
- L'agent tourne dans un conteneur, sous un compte sans privilèges, système de fichiers en lecture seule hors d'un répertoire de travail remis à zéro entre deux épisodes. **Le modèle aussi est remis à zéro** : historique de conversation, cache de préfixe et tout état du serveur d'inférence sont vidés entre deux épisodes. (garde 7)
- Aucun secret sur la machine : ni jeton du dépôt, ni clé d'un fournisseur de calcul, ni clé d'un fournisseur de modèles ; variables d'environnement vidées avant l'arrivée du lot. Le dépôt n'est pas cloné sur le banc. (garde 2)
- Les gardes, le chien de garde et le journal tournent **hors** du conteneur de l'agent ; le journal est en ajout seul, tenu par un processus que l'agent ne peut ni lire ni signaler. (garde 8)

**Données.**
- Le lot d'épisodes entre scellé, par empreinte vérifiée à l'arrivée ; il ne contient que les consignes de la course préenregistrée, pas le coffre. (garde 3)
- Les poids de l'agent sont en lecture seule ; empreinte prise avant la première action et après la dernière. (garde 4)
- **Aucun moniteur sur le banc pendant que l'agent agit** : ni poids de sonde, ni seuil, ni score, ni code d'agrégateur. L'absence se constate **par empreinte**, contre le manifeste des moniteurs (noms et empreintes, sans contenu), jamais par le nom seul. La mesure se fait en deux temps : l'agent agit et ses activations sont enregistrées ; puis, l'agent arrêté, les moniteurs gelés lisent une fois ([PR], « ouverture unique »). (garde 5)

**Outils.** Liste fermée, déclarée au préenregistrement ; tout appel hors liste est refusé et clôt l'épisode. Aucun outil ne donne à l'agent un accès hors de son répertoire de travail. (garde 6)

**Durée.** Plafonds par épisode (pas, jetons produits, temps d'horloge) et par course (épisodes, heures, dépense), fixés au préenregistrement ; un chien de garde extérieur au processus de l'agent les applique. (garde 9)

**Qui peut lancer.**
- Un **opérateur du banc** nommé au préenregistrement : une session qui n'a conçu ni sonde ni agrégateur et n'en concevra plus ([N57] point 5). La mère orchestre et consigne ; elle ne lit ni le lot ni les sorties.
- Chaque exécution cite un GO valide de `registres/go.md` (garde de calcul du dépôt) et l'empreinte du préenregistrement de la course. (garde 10)
- Chaque accès au lot ou aux sorties est consigné **avant** d'avoir lieu : qui, quand, pourquoi ([N57] point 5). (garde 11)

**Arrêt.** Par l'identifiant de l'instance et, sur la machine, par le numéro du processus ; jamais par motif de ligne de commande (R10). L'arrêt se consigne dans `registres/arrets.md`. Avant toute destruction : inventaire (noms, tailles, empreintes, sans lecture) et versement scellé en quarantaine ([CL], « Récupérer ce qui est récupérable »).

**Versement en quarantaine.** Le banc n'a ni jeton ni dépôt : il ne pousse rien. (garde 13)
- Les empreintes de chaque sortie sont prises **sur le banc**, par un processus hors du bac de l'agent, l'agent arrêté, et inscrites à un inventaire.
- L'opérateur **tire** les sorties par le canal d'administration entrant, vers un poste de transit nommé au préenregistrement ; le banc n'ouvre aucune connexion.
- À l'arrivée, chaque empreinte est revérifiée contre l'inventaire ; un écart arrête et se consigne. Le transfert est une copie de fichiers fermés : l'opérateur ne les ouvre pas.
- Destination : transcriptions, journal, états du monde et inventaire sur une **branche orpheline** de quarantaine du dépôt privé, à règle d'ouverture écrite ; les activations, si leur volume l'exige, sur un stockage à part nommé au préenregistrement, leurs empreintes seules sur la branche. Le choix du stockage à part est une ligne de devis.
- La machine n'est détruite qu'après cette vérification à l'arrivée.

---

## 3. Ce qui sort du banc, et ce qui n'en sort pas

### 3.1 Trois destinations, pas une de plus

| Objet | Destination | Qui lit |
|---|---|---|
| Transcriptions des épisodes (ce que l'agent a écrit et fait) | quarantaine, scellées (R6) | le juge ([PR], « Qui lit quoi »), session du programme qui lit sur la branche de quarantaine, comme on lit le coffre ; personne qui conçoit un moniteur |
| Activations enregistrées | quarantaine, scellées | les moniteurs gelés, par programme, une fois ; aucune personne ni session de conception |
| Journal du banc, états du monde simulé | quarantaine, scellés | le juge ; l'opérateur, pour le seul diagnostic d'une garde tombée |
| Agrégats : décomptes, taux, intervalles, verdict par cellule, classe de faille et hypothèse violée ([N57] point 3 a) | hors quarantaine, scellés | tous, concepteurs compris |
| Manifeste de course (configuration, versions, graines, commit, empreintes ; R9) | hors quarantaine | tous |

- Les activations vont en quarantaine au même titre que le texte : on peut en tirer le contenu.
- Tout ce que l'agent produit de **neuf** à partir d'une consigne du coffre est un contenu de quarantaine, même s'il dépasse la consigne. Il ne se réemploie dans aucune mesure sans un texte contre-lu et le mot de Lazar ([CL]).
- Noms de fichiers, de branches et de champs : aucun ne dit un mode.

### 3.2 Le passage hors quarantaine

Un seul passage : le fichier des agrégats, vérifié **par programme** contre un schéma fermé (nombres, identifiants de cellule, classes prises dans une liste fermée du préenregistrement ; **aucun champ de texte libre**). Un fichier qui ne passe pas reste en quarantaine. (garde 12)

### 3.3 Aucun score de moniteur dans l'entraînement de l'agent (N-053 point 5)

Sur ce banc l'invariant est tenu **par construction**, deux fois : l'agent n'est pas entraîné du tout (exclusion 3, garde 4), et aucun moniteur n'est présent quand il agit (garde 5). La garde demandée par [PR] (« garde de l'invariant de N-053 point 5 absente ou non éprouvée : aucune course ») est ici la réunion des gardes 4 et 5.

### 3.4 Accès consignés

Registre des accès dans `registres/decisions.md` : une ligne par lecture du lot ou des sorties (qui, quand, pourquoi), écrite avant la lecture. Qui a lu ne contribue plus à la conception d'un moniteur ([N57] point 5). La liste nominative des lecteurs permis est dans le préenregistrement de la course.

---

## 4. Gardes et liste d'arrêt

### 4.1 Gardes, chacune éprouvée sur un cas sain et sur un artefact (R5)

Toutes les épreuves se font **à blanc** : avec un agent factice (programme scripté, sans modèle) et une consigne anodine, jamais avec un contenu du coffre. Les résultats d'épreuve sont scellés avant la course ; une garde non éprouvée vaut une garde absente. Seule l'épreuve de la remise à zéro du modèle (garde 7, dernier artefact) demande un modèle chargé : elle se fait pendant la répétition à blanc, avec une consigne anodine.

| n° | Garde | Cas sain (doit passer) | Artefact (doit arrêter) |
|---|---|---|---|
| 1 | Réseau sortant coupé hors du bac de l'agent, service de métadonnées et adresses locales au lien compris | banc réglé comme prévu : les essais de connexion de contrôle échouent tous, le banc démarre | une règle laissée ouverte ; le service de métadonnées joignable : la garde refuse le démarrage |
| 2 | Aucun secret sur la machine | environnement vidé | un jeton factice posé dans l'environnement ou dans un fichier |
| 3 | Intégrité du lot | lot à l'empreinte attendue | lot modifié d'un octet |
| 4 | Poids de l'agent intacts | empreinte égale avant et après | fichier de poids modifié d'un octet pendant la course |
| 5 | Aucun moniteur sur le banc pendant l'action, constaté par empreinte | disque sans aucun fichier dont l'empreinte figure au manifeste des moniteurs | copie **renommée** d'un fichier factice inscrit à un manifeste d'épreuve |
| 6 | Liste fermée d'outils, environnement simulé | appels dans la liste | appel hors liste par l'agent factice ; adresse non locale dans la configuration |
| 7 | Droits et remise à zéro, du répertoire et du modèle | écriture dans le répertoire de travail, vidé ensuite ; contexte du modèle vide au début de l'épisode | écriture hors du répertoire ; fichier qui survit d'un épisode au suivant ; mot témoin anodin d'un épisode retrouvé dans le contexte du suivant |
| 8 | Journal en ajout seul, hors du conteneur | journal complet | ligne retirée ou réécrite ; journal joignable depuis le conteneur |
| 9 | Plafonds et chien de garde | épisode court | agent factice qui boucle ; course qui dépasse son plafond |
| 10 | GO et préenregistrement cités | GO valide, empreinte égale | GO absent, périmé ou d'un autre objet ; empreinte différente |
| 11 | Registre des accès | ligne présente avant le lancement | lancement sans ligne |
| 12 | Schéma fermé des agrégats | fichier conforme | fichier portant un champ de texte libre ou une classe hors liste |
| 13 | Versement en quarantaine : empreintes prises sur le banc, revérifiées à l'arrivée | transfert intact, inventaire égal | fichier altéré pendant le transfert ; fichier absent de l'inventaire ; destruction demandée avant la vérification |

La garde 1 demande en plus une **répétition à blanc sur la machine réelle** (même fournisseur, même image), parce qu'un pare-feu ne s'éprouve pas sur un autre hôte que le sien (section 8). Avant elle, et sans dépense : lecture de la documentation du fournisseur pour établir lequel des deux niveaux de la section 2 y est possible.

### 4.2 Liste d'arrêt

| Condition | Action |
|---|---|
| Ni pièce écrite de revue externe couvrant l'option (b), ni mot explicite de Lazar disant que la revue du 31 octobre couvre (b) ou que ce dossier vérifié en tient lieu (section 6) | Aucune construction, aucune exécution. |
| Préenregistrement de la course absent, non scellé ou non contre-lu ; GO d'exécution absent | Aucune course. |
| Une garde de 4.1 absente, non éprouvée, ou éprouvée sur un seul des deux cas | Aucune course. |
| Une garde tombe pendant la course | Arrêt par identifiant (R10) ; aucun repli silencieux ; versement en quarantaine ; course tronquée, rapportée. |
| Connexion sortante tentée, aboutie ou non | Arrêt de l'épisode et de la course ; consigné ; nœud. |
| Appel d'outil hors liste, écriture hors du répertoire de travail, atteinte au journal ou à une garde | Arrêt de l'épisode ; consigné dans les agrégats comme décompte ; à la deuxième occurrence, arrêt de la course et nœud. |
| Poids de l'agent changés ; fichier de moniteur présent pendant l'action ; état du modèle qui passe d'un épisode au suivant | Arrêt ; course « sans objet » ; audit. |
| Écart d'empreinte ou fichier hors inventaire au versement | Arrêt ; la machine n'est pas détruite ; consigné ; nœud. |
| Dépassement d'un plafond (pas, temps, dépense) | Arrêt de l'instance par son identifiant ; course tronquée, rapportée. |
| Contenu de quarantaine sur le point de sortir autrement que par 3.2, ou lu par qui conçoit un moniteur | Arrêt ; consigné ; nœud. |
| Lecture sans ligne au registre des accès | Arrêt ; la lecture est consignée après coup comme écart ; nœud. |
| Refus d'un classifieur de sûreté, à n'importe quelle étape | Consigner ; arrêter sur ce point ; ni contournement, ni reformulation, ni renvoi à une autre session ou à un sous-agent ([PR], liste d'arrêt). |
| Résultat trop propre, dans un sens ou dans l'autre (aucune évasion, ou toutes) | Même audit dans les deux cas (R4) avant tout verdict. |
| Écart à cette pièce ou au préenregistrement une fois scellés | Arrêt ; nœud ; version nouvelle (R12). |
| Demande d'usage hors mesure (montrer, prêter, publier, réemployer une sortie) | Refus ; nœud ; revue externe d'abord ([GO] l. 581, point 6 ; [N57] point 2). |

---

## 5. Les risques : ce qu'un agent qui agit peut faire de plus qu'un texte rejoué

Un texte rejoué est inerte : il ne fait rien, n'ajoute rien, ne touche rien. Un agent qui agit choisit ses gestes. Douze écarts, chacun avec sa réponse et ce qui reste.

| n° | Ce que l'agent qui agit ajoute | Réponse | Ce qui reste |
|---|---|---|---|
| 1 | Il peut produire un **effet** par ses outils. | Monde simulé, réseau sortant coupé hors du conteneur, liste fermée d'outils (gardes 1, 6). | Une faille de la simulation elle-même ; bornée par l'absence de réseau et de secret. |
| 2 | Il peut **écrire** un contenu de quarantaine là où on ne l'attend pas (fichier, journal, nom). | Tout ce que le banc produit va en quarantaine ; un seul passage sortant, à schéma fermé (garde 12). | Aucun champ libre ne sort ; un canal par les nombres est théorique et sans lecteur. |
| 3 | Il peut **élaborer** au-delà de la consigne : son épisode peut être plus opératoire que le contenu de départ. | Ses sorties sont un contenu de quarantaine de plein droit, lues par le seul juge, comptées au registre des accès, jamais réemployées sans texte contre-lu et mot de Lazar. | **Le coffre grossit.** C'est le coût propre de (b), à dire tel quel au relecteur. |
| 4 | Il peut **s'en prendre au banc** : gardes, journal, mesure. | Gardes, chien de garde et journal hors du conteneur, hors de sa portée (garde 8) ; droits réduits (garde 7). | Une évasion du conteneur ; elle ne rencontre ni réseau ni secret. |
| 5 | Il peut laisser un **état qui dure** d'un épisode à l'autre, sur le disque ou dans le contexte du modèle. | Remise à zéro du répertoire et du modèle entre épisodes (garde 7) ; machine détruite après versement. | Rien au-delà de la course. |
| 6 | Il pourrait **apprendre** à mieux échapper. | Aucun entraînement, aucun retour, aucun moniteur présent, une seule lecture (gardes 4, 5 ; exclusions 3 et 4). | Rien sur ce banc ; le bras avec retour est un autre texte. |
| 7 | Il peut **s'emballer** : boucle, dépense. | Plafonds et chien de garde extérieur (garde 9) ; garde de calcul du dépôt. | Une course tronquée, rapportée. |
| 8 | Il peut **se savoir éprouvé** et agir autrement. | Ce n'est pas un risque de sécurité mais de validité : mesuré et rapporté (conscience d'évaluation, [CL] N-053) ; jamais corrigé en rendant le banc moins fermé. | La mesure vaut pour le banc, pas pour la production ; à écrire dans chaque résultat. |
| 9 | Ses résultats peuvent **contaminer** les concepteurs de moniteurs. | Ils ne reçoivent que la classe de la faille et l'hypothèse violée ([N57] point 3 a ; [PR]). | Un moniteur corrigé sur ce retour devient « spécialisé » et le déclare ([PR]). |
| 10 | Réunis, lot, code et poids forment un **objet transportable** : l'organisme évadeur exécutable. | Les trois ne sont réunis que sur la machine du banc, le temps de la course ; le code du banc ne contient aucune consigne ; le lot retourne en quarantaine ; la machine est détruite. Aucune image de la machine n'est gardée. | L'objet peut être reconstitué par qui a accès aux trois ; d'où la liste nominative et le registre des accès. |
| 11 | Le banc peut **glisser** de la mesure à la démonstration. | Un GO par exécution ; périmètre clos (1.2) ; question fermée posée avant chaque course à un lecteur d'une autre lignée : « cette exécution sert-elle à autre chose que mesurer ? » — un oui bloque (repris de [GO] l. 581, point 5). | Dépend de la tenue du registre ; vérifiable après coup. |
| 12 | L'opérateur **lit** ce que l'agent produit en le lançant. | L'opérateur ne lit pas les sorties ; il voit décomptes et états des gardes. Le diagnostic d'une garde tombée est un accès consigné. | Un opérateur de plus hors de la conception des moniteurs. |

Ce que ce banc **ne couvre pas**, pour que personne ne le croie couvert : un agent dont les poids seraient changés par l'épreuve ; un agent servi par un tiers ; une tâche à effets réels ; une attaque qui apprend du moniteur. Chacun de ces quatre cas demande sa propre pièce.

---

## 6. Ce qui doit être vérifié, et par qui

### 6.1 Liste fermée pour un relecteur externe

Le relecteur n'a **pas** besoin de lire le coffre : les vingt-trois points portent sur le banc, ses gardes et ses registres, éprouvés à blanc. S'il demande à le lire, c'est un accès à consigner et un nœud.

*Périmètre*
1. Le préenregistrement de la course nomme l'agent (poids ouverts, chargés localement), la tâche, la liste des outils, les plafonds, l'opérateur, le poste de transit et la liste nominative des lecteurs.
2. Aucun des huit exclus de 1.2 n'est présent dans la course telle qu'elle est écrite.
3. L'environnement de tâche est entièrement simulé : aucune adresse, aucun compte, aucune donnée d'un système réel.

*Confinement*
4. Le réseau sortant est coupé hors du bac de l'agent, service de métadonnées du fournisseur et adresses locales au lien compris ; le niveau de coupure possible chez ce fournisseur est établi sur sa documentation ; l'épreuve des deux cas a été faite sur la machine réelle.
5. Aucun secret n'est sur la machine ; le dépôt n'y est pas cloné.
6. L'agent tourne sans privilèges, en lecture seule hors de son répertoire de travail ; répertoire et état du modèle sont remis à zéro entre épisodes.
7. Gardes, chien de garde et journal sont hors de portée de l'agent.
8. Aucun fichier de moniteur n'est sur le banc pendant l'action, ce qui est constaté par empreinte ; la lecture par les moniteurs vient après, l'agent arrêté.
9. Les poids de l'agent ont la même empreinte avant et après.
10. Les plafonds existent, sont chiffrés au préenregistrement et appliqués par un processus extérieur à l'agent.
11. L'arrêt se fait par identifiant ; la destruction suit un versement vérifié ; aucune image de la machine n'est gardée.

*Sorties*
12. Transcriptions, activations, journal et états du monde vont en quarantaine, scellés.
13. Le versement est tiré par l'opérateur, jamais poussé par le banc ; les empreintes sont prises sur le banc et revérifiées à l'arrivée ; la destination (branche orpheline, stockage à part éventuel) est nommée au préenregistrement.
14. Le seul passage hors quarantaine est le fichier des agrégats, vérifié par programme contre un schéma sans texte libre.
15. Les concepteurs de moniteurs ne reçoivent que la classe de la faille et l'hypothèse violée.
16. Le registre des accès porte une ligne par lecture, antérieure à la lecture ; aucun lecteur ne conçoit de moniteur ; le moyen par lequel le juge lit est écrit.
17. Aucun nom de fichier, de branche ou de champ ne dit un mode.

*Gardes et arrêts*
18. Les treize gardes ont chacune leurs deux épreuves, scellées avant la course.
19. La liste d'arrêt de 4.2 est reprise sans retrait dans le préenregistrement de la course.
20. Un refus de classifieur arrête sans contournement ; les refus passés sont consignés.

*Gouvernance*
21. Chaque exécution cite un GO ; aucune ne s'appuie sur un GO d'un autre objet.
22. La question fermée du risque 11 a reçu un non, par un lecteur d'une autre lignée que les moniteurs, avant chaque course.
23. Le relecteur dit par écrit ce qu'il a vu, ce qu'il n'a pas vu, et sa conclusion : validé, validé sous conditions, refusé. Sa pièce est versée et scellée ([RJ] nœud 3, option (a) : qui, quand, périmètre, conclusion).

Une réponse « non » ou « non vérifiable » à un seul point vaut « pas de course ».

### 6.2 L'alternative : des garde-fous internes à la place de la revue externe

**C'est une décision de Lazar, et elle n'est pas prise.** Trois faits du registre, dans l'ordre : le 31 octobre, le gel est inscrit comme levé sur le mot de Lazar, la revue externe étant dite faite ([R888]) ; le 20 novembre, GO-2026-11-20-50 met six garde-fous internes « en place de la revue de sécurité externe pour la mesure interne » de la course « nouvelles attaques », ce qui montre qu'une revue externe est encore tenue pour due sur certains objets après le 31 octobre ; le 21 novembre, l'option (b) est accordée « dès que la pièce de sécurité est écrite ». Rien ne dit que les six garde-fous valent pour (b), ni que la revue du 31 octobre a couvert un agent qui agit sur un contenu dérivé du coffre.

Dans le cadre que [R888] inscrit, une vérification interne de ce dossier n'est pas un écart à R-611 : c'est une **condition ajoutée** par le mot du 21 novembre, à dire comme telle. Dans la lecture prudente que ce dossier suit (revue non opposable faute de pièce écrite), ce serait une substitution, qu'il faut alors nommer. Seul un mot explicite de Lazar dit laquelle des deux descriptions vaut ; pas de défaut à 48 heures.

Comparaison, pour éclairer ce mot sans le préjuger :

| Garde-fou de GO-2026-11-20-50 | Vaut-il pour (b) ? | Ce qu'il faudrait y ajouter |
|---|---|---|
| 1. Le procédé n'est demandé qu'après le verdict d'antériorité, par une session à part ; la mère ne le lit jamais | En partie. Ici le contenu existe déjà dans le coffre. Se garde : opérateur à part, mère qui ne lit pas. | Rien de plus que 2 « Qui peut lancer ». |
| 2. Quarantaine sur branche orpheline, règle d'ouverture écrite, liste nominative des lecteurs, chaque lecture consignée | Oui. | L'étendre aux sorties **neuves** de l'agent et aux activations (3.1), et dire la voie du versement (section 2, garde 13). |
| 3. Registre servi aux suivants : nom et énoncé seulement, vérifié par programme | Par analogie : c'est le schéma fermé des agrégats (3.2). | Interdire tout champ de texte libre. |
| 4. Aucune exécution hors du banc de mesure scellé ; chaque exécution citée par un GO | Oui, et c'est le cœur. Mais il suppose un banc défini. | Tout le confinement de la section 2 : pour (b), « le banc » doit retenir un agent, pas seulement un texte. |
| 5. Un lecteur d'une autre lignée répond oui ou non : « sert-il à autre chose que mesurer ? » | Oui (risque 11). | Sa lecture est un accès consigné. |
| 6. Revue externe avant toute sortie hors quarantaine | Oui, inchangé. | — |

Ce que les six ne contiennent pas et que (b) exige : le confinement de l'agent (gardes 1, 2, 6, 7, 8), l'intégrité de ses poids (garde 4), l'absence de moniteur pendant l'action (garde 5), les plafonds (garde 9), le versement vérifié (garde 13), l'épreuve de chaque garde sur deux cas (R5), la destruction de la machine. Si Lazar choisit la voie interne, la proposition du rédacteur est : les six, plus les treize gardes, plus un **vérificateur interne neuf**, d'une autre lignée que les moniteurs et que le rédacteur, qui répond aux points 1 à 22 de 6.1 et verse sa pièce scellée. Cette voie est plus rapide ; elle est plus faible qu'une revue externe, et la phrase d'entretien devrait alors dire « garde-fous internes vérifiés », sans les présenter comme la revue de sécurité elle-même ([RJ] nœud 3).

---

## 7. Nœuds renvoyés à Lazar

Nœuds d'arrêt : pas de défaut à 48 heures.

**Nœud 1 — Ce que désigne « la pièce de sécurité » du mot du 21 novembre.**
Enjeu : la recommandation acceptée vient de [RJ] nœud 4, « (b) dès la pièce du nœud 3 », et la pièce du nœud 3 est la pièce écrite de la revue externe. Mais Lazar a dit la revue faite le 31 octobre ([R888]) ; trois semaines plus tard, « dès que la pièce de sécurité est écrite » désigne plus vraisemblablement un dossier interne, ou la pièce écrite de la revue déjà faite, qu'une revue encore à commander. C'est une lecture du rédacteur, reprise de la contre-lecture ; elle ne remplace pas le mot.
- (a) C'est la **pièce écrite de la revue du 31 octobre** (qui, quand, périmètre, conclusion) : Lazar la verse, et l'on vérifie si son périmètre couvre un agent qui agit sur un contenu dérivé du coffre. Avantage : la levée du gel devient opposable, la phrase d'entretien est vraie. Inconvénient : il faut l'accord du relecteur ; si le périmètre ne couvre pas (b), revue complémentaire, et ce dossier est ce qu'on lui remet.
- (b) C'est **ce dossier, vérifié par un vérificateur interne neuf** (6.2), dans le cadre levé par [R888] : une condition ajoutée, non un écart à R-611. Avantage : rapide, sans contact externe. Inconvénient : plus faible ; ne dit rien de ce que la revue externe a couvert, et le nœud 3 de [RJ] reste ouvert.
- (c) C'est ce dossier, sans vérification. Le rédacteur le déconseille : une pièce ne se valide pas elle-même.
Recommandation : **(b) pour avancer, et (a) en parallèle** — le vérificateur interne conditionne la construction des gardes et la répétition à blanc ; la pièce écrite de la revue, ou une attestation courte de Lazar sur son périmètre, est demandée avant la première course sur un contenu du coffre. Confiance 0,6 ; plus basse qu'en v1, parce que la lecture dépend d'un fait que seul Lazar connaît.

**Nœud 2 — Une question précise à Lazar.** La revue de sécurité externe dite faite le 31 octobre ([R888]) a-t-elle une pièce écrite, et son périmètre couvre-t-il l'option (b), un agent qui agit sur banc fermé à partir d'un contenu dérivé du coffre ? Tant qu'il n'y a pas de réponse, ce dossier suit l'option (b) du nœud 3 de [RJ] : revue tenue pour non opposable à (b), rien d'opératoire ne tourne.

**Nœud 3 — Qui est l'opérateur du banc, et qui est le juge.** Deux noms à écrire au préenregistrement ; aucun des deux ne conçoit de moniteur. Proposition : ni la mère, ni l'attaquant informé, ni le rédacteur de ce dossier. Confiance 0,6.

---

## 8. Coût

- **Cette pièce** : aucune dépense.
- **Gardes 2 à 13** : épreuves à blanc sur processeur, avec un agent factice sans modèle (sauf le dernier artefact de la garde 7, fait pendant la répétition). Aucun calcul payant. Le code des gardes est un instrument (contre-lecture par un autre modèle) ; il n'est pas écrit ici, et son écriture attend l'issue du nœud 1 : sous la lecture prudente de ce dossier, la construction attend comme l'exécution.
- **Avant la répétition, sans dépense** : lecture de la documentation du fournisseur visé, pour savoir si le pare-feu du fournisseur ou un bac intérieur y est possible, et si son service de métadonnées se coupe.
- **Stockage à part des activations**, s'il en faut un : ligne de devis, non chiffrée ici.
- **Garde 1 et répétition à blanc** : une machine à carte graphique du même fournisseur et de la même image que la course, le temps de charger les poids de l'agent, de couper le réseau, de passer les deux cas de chaque garde et un épisode anodin. Esquisse de devis, sans chiffre : (heures de machine) × (tarif horaire constaté le jour du devis) + stockage du versement. Le rédacteur n'avance aucun montant : il n'a vérifié aucun tarif (R7). Devis à écrire par l'opérateur, GO avant dépense.
- **Revue externe** : contact externe, donc rédigé ici et envoyé par Lazar ; coût éventuel inconnu du rédacteur.
- **La course elle-même** : hors de cette pièce ; devis au préenregistrement.

---

## 9. Ce que cette pièce ne dit pas, et réserves

- Elle ne dit rien du contenu du coffre, ni d'aucun mode, ni d'aucun moniteur : le rédacteur n'en a rien lu. Non lus, par consigne : `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, toute branche `claude/scellement-2-*`, `docs/notes/programme-et-4-familles-evasion/`, les lignes R-604 à R-610 de `registres/decisions.md`, toute conception, tout résultat et tout seuil de moniteur, toute sortie de la course « nouvelles attaques », `registres/etat.md`, la dernière passation.
- **Réserve 1.** Les six garde-fous sont pris dans la ligne du registre, non dans les avis qu'elle cite (non ouverts).
- **Réserve 2.** Le rédacteur ne connaît pas le banc de mesure actuel du programme ; la section 2 dit ce que le banc doit garantir, pas ce qui existe. L'écart est à mesurer par l'opérateur.
- **Réserve 3.** L'état de la revue externe est celui que le registre inscrit le 31 octobre ([R888]) : faite et favorable, sur le mot de Lazar. Le rédacteur ne sait ni s'il en existe une pièce écrite, ni ce qu'elle a couvert, ni si le nœud 3 de [RJ] a été tranché depuis le 10 novembre (nœud 2). La v1 ignorait [R888] ; c'était une erreur de la v1, corrigée ici.
- **Réserve 4.** La garde 5 suppose que les sondes lisent des activations **enregistrées**. Si une sonde devait lire pendant l'action, la garde 5 et le point 3.3 seraient à réécrire, et ce serait un nœud.
- **Réserve 5.** La suffisance de l'isolement d'un conteneur contre un agent n'est pas démontrée ici ; la réponse de cette pièce est qu'une sortie du conteneur ne rencontre ni réseau ni secret. C'est le point où un regard externe vaut le plus.
- **Réserve 6.** Corrections de la v2 non encore vérifiées par la contre-lectrice.
- **Réserve 7.** La faisabilité de la coupure du réseau chez les loueurs du programme n'est pas établie ici ; le rédacteur n'a lu la documentation d'aucun fournisseur.
- **Refus de classifieur** : aucun pendant la rédaction.

---

## 10. Réponse aux points de la contre-lecture de la v1 ([CL1])

| Point | Réponse | Où |
|---|---|---|
| B1, gel tenu pour en vigueur alors que le registre le dit levé | Corrigé : [R888] lue et citée ; la prudence est dite comme une lecture choisie contre la lettre du registre. | en-tête, verdict 1, liste d'arrêt ligne 1, 6.2 |
| B2, nœud 1 mal posé | Reposé avec [R888] ; trois options refaites ; recommandation et confiance refaites ; nœud 2 réduit à une question précise. | section 7 |
| M1, voie du versement | Ajoutée : versement tiré, empreintes sur le banc, vérification à l'arrivée, destination ; garde 13 ; point 13 de 6.1. | section 2, 4.1, 4.2, 6.1 |
| M2, coupure du réseau chez un loueur en conteneur, métadonnées | Deux niveaux écrits, service de métadonnées et adresses locales au lien nommés, vérification sur documentation avant de louer ; réserve 7. | section 2, garde 1, 6.1 point 4, section 8 |
| M3, exclusion 2 et le juge | Exclusion restreinte au modèle qui agit ; moyen de lecture du juge écrit. | 1.2, 3.1, 6.1 point 16 |
| M4, garde 5 par le nom | Constat par empreinte ; artefact : copie renommée. | section 2, garde 5, 6.1 point 8 |
| M5, remise à zéro du modèle | Ajoutée, avec son artefact. | section 2, garde 7, risque 5 |
| M6, réserve 3 inexacte | Réécrite. | section 9 |
| M7, « branche orpheline » | Lettre reprise. | 6.2 |
