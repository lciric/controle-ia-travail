# Préenregistrement — course d'affinage des idées des mentors par l'organisme d'idéation — v1

- Auteur : session du compte organisme (modèle I), sur demande de la mère.
- Date (UTC) : 2026-11-18, écrit à partir de 06:55Z (`date -u`).
- Décision : N-072 (texte `docs/decisions/decision-matiere-premiere-mentors-v1.md`, sha256 `a0dd17d84b26e153e10a87c63178e0e35f10938dfb6aebf3989b9b4b94a51af8`, branche `lot/compte-organisme-v1`) ; GO-2026-11-18-14 (plafond d'arrêt 150 USD, « oui aux deux », R-3215) ; budget des appels d'interface séparé (GO-2026-11-18-13, R-3209 point 2) ; Carbon (R-3217, GO-2026-11-18-15).
- Pièces qui font foi (chemin, sha256) :
  - relevé d'ensemble : `docs/notes/quatre-lectures-inventaire-v1/mentors-releve-d-ensemble-v1.md` sur `main`, `f7eaec6f097859864433f69413233a756ebf241ea541f7eb54b3648818caf9c0` ;
  - liste des fils servis et des retraits : `docs/notes/organisme-affinage-mentors-v1/course-v1/fils-servis-et-retraits-course-affinage-mentors-v1.json`, `c30928c88feffc16d3aa1119efe2a54ba2d70cf135b8068855190a21470a56bb`, écrite par programme (`scripts/construire_fils_course_affinage_mentors_v1.py`, `ff2b38e23d7d97dfda95084bbf7e7b9a64f0c83a943141a355d0e136f8d4c912`) ;
  - configuration fixe de l'orchestrateur : `…/course-v1/configuration-course-affinage-mentors-v1.json`, `4f9cdf3e5e81691ba8ead1037d2ce5f071b745b9a1ff3c657686c9196e1f81f9` ;
  - consignes figées : proposeur `d36ba0a01c1c190d55d0ed63b053c951b5a767a9310013321d797e3e203d8c4f`, aiguilleur `903318d7659db07819cbe9a7f89cbdbd292f59e14c32bb8811d8f8cb35dd955b`, juge `a32583b14845343a613514cdcba3c24831a274b48ecc95fe0d884f017d27d346`, passe « tableau » (jamais servie) `1ac9791b6aea1c97f534e32980f1f837cca425806ce8235b1064d98ce261dcbf` (même dossier) ;
  - devis v3 : `docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v3.md`, `6aa86555dd7a1883141660a4619812da6db2f0a9b9d05b1b5e2cb23db7546ea2` (la v2, `2fb1c3cd…`, reste en place) ;
  - lanceur : `scripts/lancer_course_affinage_mentors_v1.py` (il épingle l'empreinte de ce préenregistrement ; son empreinte est donnée par `course-v1/commandes-exactes-course-affinage-v1.md` et doit être citée par la contre-lecture) ;
  - orchestrateur : dépôt public `lciric/ideation-organism`, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, `demonstrations/ideation_v8.py --course-2` (course 2, version 56), empreintes de 25 fichiers épinglées dans le lanceur.

## Objet

Faire affiner par l'organisme d'idéation lui-même, et non par une session qui reformulerait à la main, les idées des mentors du 3 novembre versées à l'atelier d'idées (N-072, rôle 2 de N-065) : pour chacun des seize fils communs du relevé d'ensemble, chaque espèce de proposeurs rend **deux cartes affinées** (hypothèse avec son signe, mesure, bases et loi nulle, ce qui la réfuterait, limites). Une course d'affinage **n'a pas de verdict de porte** : les cartes produites sont de la **matière**, jamais des preuves.

## Question

Sans objet au sens d'une hypothèse du programme : la course ne crée, ne modifie ni n'éprouve aucune hypothèse ni aucune revendication. Question de travail, descriptive : « que rendent les proposeurs de plusieurs familles quand on leur sert un fil d'idées passées et qu'on leur demande deux cartes réfutables, et combien de ces cartes passent l'aiguilleur sur la forme ? »

## Hypothèse, prédiction chiffrée et signe, seuil

Aucune hypothèse éprouvée, aucune prédiction chiffrée, aucun seuil de décision : la course ne vise aucun signe (R3) et ne décide rien. Seul chiffre fixé d'avance : le **plafond d'arrêt de 150 USD**.

## Ce qui est servi (et ce qui ne l'est jamais)

- **Seize cases**, une par fil commun du relevé (§ 2), dans l'ordre du relevé. Chaque case porte le titre du fil et ses idées servies, chacune avec son numéro du relevé entre crochets et le texte de la colonne « idée » du relevé, sans reformulation, à une exception écrite en table exacte dans le script de la liste : les attributions à une espèce ou à une lettre du collisionneur sont retirées (dix lignes : H2, K1, K15, I6, S1, S8, S10, CW6, CW7, CW16), pour que les proposeurs ne sachent pas quelle espèce a dit quoi. 67 idées distinctes servies.
- **Retraits** (liste écrite et vérifiée par programme, `…/fils-servis-et-retraits-course-affinage-mentors-v1.json`) — **20 entrées** :
  - les **six entrées sous réserve** du relevé (§ 4 : deux fiches d'une espèce et une fusion inachevée de la question Kirchner, deux expériences de son collisionneur, la règle de strate « injection » de la question Scheurer) : absentes de la table des idées, jamais servies ;
  - **quatorze idées de la table**, soumises à une réserve de cloisonnement **non levée** par la mère : S3, S5, S6, S7 (fusions dont un parent est exclu) ; CW1 (réserve a) et CW2 (extension prudente : « tout le thème CW1 peut être resserré ») ; CW3, CW5, CW10 (réserve b) ; JF2, JF3, JF5, JF8 (organismes de sous-performance reconstruits d'après des recettes publiées) ; I16 (invariant de N-053). Toute ligne dont la provenance cite une fiche réservée est retirée aussi (contrôle par programme ; aucune autre trouvée).
  - **Exclusions des relevés** (familles 1 et 2) : jamais servies ; elles ne figurent ni dans la table des idées ni dans la liste.
  - Une entrée retirée ne revient que si la mère lève sa réserve par écrit : nouvelle version de la liste, du lanceur et de ce préenregistrement (R12).
- Le lanceur refuse de partir si une entrée servie figure dans les retraits ou si un identifiant de fiche réservée figure dans un texte servi ; l'orchestrateur exclut toute carte qui porterait un numéro retiré, un identifiant réservé ou un nom d'espèce (garde A4, « fiche exclue »).

## Espèces

- **Proposeurs**, Claude d'abord (R-3209, point 2) : les deux espèces Claude de la configuration, **obligatoires** (aucun départ sans elles) ; Argon (obligatoire aussi, car il tient le second juge) ; Kimi et Astra si la session d'exécution déclare leur relais ; **Carbon, conditionnelle** : inscrite par la mère (R-3217, GO-2026-11-18-15), mais ni son relais ni le nom de sa clé ne sont nommés au scellement de ce préenregistrement. Carbon n'est donc activée que si la déclaration des relais (scellée par la session d'exécution avant le lancement, vérifiée par le lanceur) nomme son relais, son modèle et sa clé et porte l'inscription R-3217 ; sinon **la course part sans Carbon**. Les deux formes sont préenregistrées ici et chiffrées au devis v3.
- Une espèce sans relais déclaré, ou arrêtée en course, est une **lacune rapportée**, jamais compensée.
- **Aiguilleur** : la première espèce Claude, une session neuve par carte, sur la forme seulement (consigne figée : `niveau_methode` → passeport ; `a_corriger` → retenue, servie à personne ; `concret` → journalisée sans contenu).
- **Juges croisés aveugles** : la première espèce Claude et Argon ; un appel par carte et par juge, session neuve, identifiant opaque propre au juge ; aucun juge ne voit l'auteur, les autres cartes ni l'autre juge. Cinq items vrai ou faux (`refutable`, `mesure_definie`, `base_ou_nul`, `fidele_au_fil`, `reserves_tenues`) ; agrégation « unanimité » écrite au classement, **descriptive**.
- **Mémoire anti-redite** : bardeaux de trois mots, seuil 0,5, sur tout le lot ; les redites sont comptées, jamais filtrées (comportement de l'orchestrateur).

## Plan (ce que fait la course)

Une seule génération de la course 2 (v56) : étapes `proposition` (16 cases × espèces actives, un appel chacun, deux cartes demandées), `aiguillage`, `juges` ; `passe_tableau` et `fusions` **retirées par construction** (plafond de relais 151 USD > plafond d'arrêt : règle d'A1, point 3) ; `etiquettes` jouée à vide (aucun bras du bisociateur) ; **pas de tests de mort**. Puis, sans dépense : mémoire, fin de la phase de mesure, classement, sorties scellées. Graines : racine `2026111814`, préfixe `affm`, `numpy.random.SeedSequence` par tâche dans l'orchestrateur (R9).

**Note du juge montrée ou non aux proposeurs : règle laissée telle quelle** (R-3209, point 5, encore ouverte ; rien n'est modifié) : dans l'orchestrateur, les verdicts sont déposés au coffre et ne sont ouverts qu'après la fin de la phase de mesure ; le texte d'héritage (titres, résumés, verdict agrégé) n'est servi qu'aux proposeurs d'une génération suivante. Cette course n'a qu'une génération : aucun proposeur n'y voit une note de juge.

**Aucune promotion par un modèle** : aucun verdict, aucun classement ne choisit une carte pour la suite ; le lanceur ne lit aucun verdict (il ne compte que les cartes, les étapes et les coûts). Ce qui sortira pour un papier sera un nœud pour Lazar ; toute épreuve d'une carte avec dépense est sur devis, ligne de GO et mot de Lazar (N-072, § 1.3).

## Sorties attendues

- Hors du dépôt, `/home/user/sorties-course-affinage-mentors-v1/<id>/sortie/` : `generation-1/fiches.json` (cartes à passeport), `classement.json` (descriptif), `memoire.json`, journal de l'aiguillage, `consommations.json`, manifestes de départ et de fin de l'orchestrateur, `bilan-course.json`, empreintes ; journaux de la course.
- Au dépôt, `runs/<id>-course-affinage-mentors-v1/` : acte de gel, configuration assemblée, manifestes de départ et de fin du lanceur (scellés), alertes éventuelles.

## Ce qui est mesuré, et ce qui ne l'est pas

- **Mesuré (descriptif)** : nombre de cartes rendues par fil et par espèce, cartes refusées au format, classes de l'aiguilleur, cartes exclues par la garde A4, verdicts des items des deux juges (lus par la mère seulement, après la course), redites, rôles arrêtés et leurs motifs, coût réel par relais et par rôle, écart au devis v3, reste estimé de chaque clé.
- **Non mesuré** : la valeur, la nouveauté, la justesse ou la faisabilité d'une carte ; une convergence entre espèces n'est pas lue comme un signal de valeur (elle peut tenir au fil servi autant qu'aux espèces) ; les verdicts des juges ne sont ni étalonnés (aucun témoin planté dans cette course) ni comparés à des étiquettes humaines.

## Critères de bonne fin

La course a **fini proprement** si : l'orchestrateur rend le code 0 ; `proposition`, `aiguillage` et `juges` sont « jouée » ; `passe_tableau` et `fusions` sont « retirée » ; le cumul est ≤ 150 USD ; les manifestes du lanceur et de l'orchestrateur sont écrits et scellés ; les lacunes (espèce absente, refus au format, rôle arrêté) sont écrites. Bonne fin ne dit rien de la qualité des cartes. Toute autre issue est rapportée telle quelle (étape « non mesurée », nœud, arrêt), avec ce qui a été fait ; aucune relance sans nouvelle version et mot de la mère.

## Liste d'arrêt

- **Avant le départ** (lanceur, code 2, rien n'est appelé) : course déjà lancée sous ce lanceur ; ligne de GO absente, hors période, révoquée, d'un autre périmètre ou d'un plafond autre que 150 USD ; préenregistrement d'une autre empreinte ou non scellé ; contre-lecture absente, non scellée, qui ne cite pas l'empreinte de ce préenregistrement et celle du lanceur, ou de verdict autre que « Scellable » sans réserve ; pièce d'une autre empreinte ; entrée servie dans les retraits ; déclaration des relais absente, non scellée, portant une chaîne de la forme d'une valeur de clé, sans relais Claude ou Argon, adresse hors boucle locale, porte de plafond absente ; orchestrateur à un autre commit, modifié ou d'empreintes différentes ; configuration qui ne tient pas le plafond d'arrêt ; vérification de l'orchestrateur (`--verifier-seulement`) refusée, montant requis autre que 150, spécification non conforme ; bac à sable inactif.
- **Règle des clés** (code 3) : voir plus bas.
- **Pendant la course** (orchestrateur) : plafond dur d'étape (A1, A15) — une étape protégée qui ne tient pas sous 150 n'est pas lancée, « non mesuré (budget) », et la génération ne lance plus rien ; A4 (carte exclue) ; A17 (carte sans passeport à une destination) ; A2 (version servie d'un juge changée : arrêt du rôle) ; A3, A14 (échecs consécutifs, part de sorties inexploitables au-dessus de 0,34 : arrêt du rôle) ; M5 (débordement de Kimi au-dessus de 0,25 : arrêt du rôle) ; A21 (lecture avant la fin de la mesure) ; signal reçu : arrêt propre, manifestes écrits.
- **Après** : cumul lu au-dessus de 150 USD → code 4 et alerte (ne doit pas arriver par construction) ; passe « tableau » ou fusion jouée → écart au préenregistrement, rapporté, aucune lecture des cartes avant la mère.

## Plafond

**150 USD**, plafond d'arrêt de toute la course (GO-2026-11-18-14). Il est S17 de la configuration (portée « course ») et doit être exactement le plafond lu sur la ligne de GO, par le lanceur et par l'orchestrateur. L'orchestrateur ne lance aucune étape dont le plafond dur pourrait le franchir et borne chaque appel au reste de l'étape ; chaque relais reçoit le plafond dur de l'étape à son lancement. Devis v3 : 41,33 USD estimé (103,38 haut) sans Carbon ; 49,81 (121,95 haut) avec Carbon ; la borne des plafonds de session (352 et 422,40) dépasse 150 : seul le plafond d'arrêt borne la dépense.

## Règle des clés

Relevé, avant la course, du crédit et du reste de **chaque clé employée** (fichier du jour, scellé, écrit par la session d'exécution depuis l'interface de facturation ou le compteur ; noms de clé seulement, jamais une valeur). Un crédit « non lisible » arrête le départ, sauf dispense écrite de la mère pour cette clé. Un reste sous **un cinquième du crédit** ou sous **le plafond d'arrêt (150 USD)** écrit une alerte pour la mère (fichier et sortie) et arrête le départ (code 3) ; ainsi aucune clé ne peut atteindre zéro pendant la course, et Lazar est prévenu avant. Après la course : coût réel par relais, reste estimé par clé, alerte si un reste estimé passe sous les mêmes seuils, confirmation par l'interface de facturation à faire par la session d'exécution.

## Plan d'analyse et critères de lecture gelés

Aucune analyse décisive. Lecture descriptive, par la mère, après la course : tables des comptes ci-dessus ; les cartes sont lues comme **matière** de l'atelier d'idées, chacune « avis d'un proposeur, jamais un fait » ; tout chiffre ou travail publié cité par une carte reste non vérifié (R7) ; toute zone qu'une carte dit vierge est une question (R8). Lacunes connues du relevé (espèces absentes de certaines questions, refus au format, refus de proposition, pertes de texte des premières courses ; relevé § 3) : rapportées avec tout résultat, jamais compensées. Audit de symétrie (R4) : un lot « trop propre » (toutes les cartes à passeport, tous les items vrais, aucune redite) ou « trop sale » (aucune carte à passeport) déclenche le même contrôle (lecture des journaux de l'aiguilleur et des refus au format) avant toute lecture des cartes.

## Ce que la course ne dit pas

Qu'une carte est vraie, nouvelle, faisable, prioritaire ou meilleure qu'une autre ; qu'une idée des mentors « survit » à quoi que ce soit (aucun test de mort) ; qu'une zone est libre ; quoi que ce soit sur les entrées retirées ; quoi que ce soit sur une hypothèse ou une revendication du programme. Le classement de l'orchestrateur n'est pas une promotion.

## Contre-lecture

À faire avant tout lancement, par un contre-lecteur neuf de l'autre modèle (modèle J), qui n'a écrit ni ce préenregistrement ni le lanceur (R2). Son rapport est écrit et scellé à `docs/notes/organisme-affinage-mentors-v1/course-v1/contre-lecture-preenregistrement-course-affinage-mentors-v1.md` ; il cite l'empreinte de ce préenregistrement et celle du lanceur, et porte une section « Verdict » dont la première ligne commence par « Scellable » sans réserve, sinon le lanceur refuse. Une correction demandée donne une nouvelle version de ce préenregistrement et du lanceur (R12). L'acte de gel écrit par le lanceur au lancement (empreintes du préenregistrement et de la contre-lecture, verdict lu) est la spécification servie à l'orchestrateur.
