# Préenregistrement — course d'affinage des idées des mentors par l'organisme d'idéation — v2

- Auteur : session du compte organisme (modèle I), sur demande de la mère.
- Date (UTC) : 2026-11-18, écrit à partir de 07:09Z (`date -u`). **Version 2** (R12) : la v1 (`course-v1/preenregistrement-course-affinage-mentors-v1.md`, `7a32fe6bd86368d0e06c11c08eeec00d7138545824ec940442ea199fdab521a8`) reste en place, scellée, jamais lancée ; elle ne vaut plus pour un lancement. Différentiel en fin de texte.
- Décision : N-072 (texte `docs/decisions/decision-matiere-premiere-mentors-v1.md`, sha256 `a0dd17d84b26e153e10a87c63178e0e35f10938dfb6aebf3989b9b4b94a51af8`, branche `lot/compte-organisme-v1`) ; GO-2026-11-18-14 (plafond d'arrêt 150 USD, « oui aux deux », R-3215) ; budget des appels d'interface séparé (GO-2026-11-18-13, R-3209 point 2) ; Carbon (R-3217, GO-2026-11-18-15) ; clé Claude « Minuit » et répartition des clés (R-3228) ; revendications resserrées (N-073, `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` sur `main`, version de travail en attente de sa contre-lecture).
- Pièces qui font foi (chemin, sha256) :
  - relevé d'ensemble : `docs/notes/quatre-lectures-inventaire-v1/mentors-releve-d-ensemble-v1.md` sur `main`, `f7eaec6f097859864433f69413233a756ebf241ea541f7eb54b3648818caf9c0` ;
  - liste des fils servis et des retraits : `docs/notes/organisme-affinage-mentors-v1/course-v1/fils-servis-et-retraits-course-affinage-mentors-v1.json`, `c30928c88feffc16d3aa1119efe2a54ba2d70cf135b8068855190a21470a56bb`, écrite par programme (`scripts/construire_fils_course_affinage_mentors_v1.py`, `ff2b38e23d7d97dfda95084bbf7e7b9a64f0c83a943141a355d0e136f8d4c912`) ;
  - configuration fixe de l'orchestrateur, **v2** (clés nommées) : `docs/notes/organisme-affinage-mentors-v1/course-v2/configuration-course-affinage-mentors-v2.json`, `f76b4b58d07ed49837ff4cf148137df66f0f742ad2587fcd4089c1df224ca36b` ;
  - consignes figées : proposeur `d36ba0a01c1c190d55d0ed63b053c951b5a767a9310013321d797e3e203d8c4f`, aiguilleur `903318d7659db07819cbe9a7f89cbdbd292f59e14c32bb8811d8f8cb35dd955b`, juge `a32583b14845343a613514cdcba3c24831a274b48ecc95fe0d884f017d27d346`, passe « tableau » (jamais servie) `1ac9791b6aea1c97f534e32980f1f837cca425806ce8235b1064d98ce261dcbf` (dossier `course-v1`, inchangées) ;
  - devis v4 : `docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v4.md`, `aee89cd9ff4738eacbbb884d691ed096f9da1c71cc25dce0618e22e2f3907089` (mêmes totaux que la v3, `6aa86555…`, plus la répartition par clé) ;
  - lanceur : `scripts/lancer_course_affinage_mentors_v2.py` (il épingle l'empreinte de ce préenregistrement ; son empreinte est donnée par `course-v2/commandes-exactes-course-affinage-v2.md` et doit être citée par la contre-lecture) ;
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

- **Proposeurs**, Claude d'abord (R-3209, point 2) : les deux espèces Claude de la configuration, **obligatoires** (aucun départ sans elles) ; Argon (obligatoire aussi, car il tient le second juge) ; Kimi et Astra si la session d'exécution déclare leur relais ; **Carbon, conditionnelle** : inscrite par la mère (R-3217, GO-2026-11-18-15), mais ni son relais ni le nom de sa clé ne sont nommés au scellement de ce préenregistrement. Carbon n'est donc activée que si la déclaration des relais (scellée par la session d'exécution avant le lancement, vérifiée par le lanceur) nomme son relais, son modèle et sa clé et porte l'inscription R-3217 ; sinon **la course part sans Carbon**. Les deux formes sont préenregistrées ici et chiffrées au devis v4.
- Une espèce sans relais déclaré, ou arrêtée en course, est une **lacune rapportée**, jamais compensée.
- **Aiguilleur** : la première espèce Claude, une session neuve par carte, sur la forme seulement (consigne figée : `niveau_methode` → passeport ; `a_corriger` → retenue, servie à personne ; `concret` → journalisée sans contenu).
- **Juges croisés aveugles** : la première espèce Claude et Argon ; un appel par carte et par juge, session neuve, identifiant opaque propre au juge ; aucun juge ne voit l'auteur, les autres cartes ni l'autre juge. Cinq items vrai ou faux (`refutable`, `mesure_definie`, `base_ou_nul`, `fidele_au_fil`, `reserves_tenues`) ; agrégation « unanimité » écrite au classement, **descriptive**.
- **Mémoire anti-redite** : bardeaux de trois mots, seuil 0,5, sur tout le lot ; les redites sont comptées, jamais filtrées (comportement de l'orchestrateur).

## Plan (ce que fait la course)

Une seule génération de la course 2 (v56) : étapes `proposition` (16 cases × espèces actives, un appel chacun, deux cartes demandées), `aiguillage`, `juges` ; `passe_tableau` et `fusions` **retirées par construction** (plafond de relais 151 USD > plafond d'arrêt : règle d'A1, point 3) ; `etiquettes` jouée à vide (aucun bras du bisociateur) ; **pas de tests de mort**. Puis, sans dépense : mémoire, fin de la phase de mesure, classement, sorties scellées. Graines : racine `2026111814`, préfixe `affm`, `numpy.random.SeedSequence` par tâche dans l'orchestrateur (R9).

**Note du juge montrée ou non aux proposeurs : règle laissée telle quelle** (R-3209, point 5, encore ouverte ; rien n'est modifié) : dans l'orchestrateur, les verdicts sont déposés au coffre et ne sont ouverts qu'après la fin de la phase de mesure ; le texte d'héritage (titres, résumés, verdict agrégé) n'est servi qu'aux proposeurs d'une génération suivante. Cette course n'a qu'une génération : aucun proposeur n'y voit une note de juge.

**Aucune promotion par un modèle** : aucun verdict, aucun classement ne choisit une carte pour la suite ; le lanceur ne lit aucun verdict (il ne compte que les cartes, les étapes et les coûts). Ce qui sortira pour un papier sera un nœud pour Lazar ; toute épreuve d'une carte avec dépense est sur devis, ligne de GO et mot de Lazar (N-072, § 1.3).

## Sorties attendues

- Hors du dépôt, `/home/user/sorties-course-affinage-mentors-v2/<id>/sortie/` : `generation-1/fiches.json` (cartes à passeport), `classement.json` (descriptif), `memoire.json`, journal de l'aiguillage, `consommations.json`, manifestes de départ et de fin de l'orchestrateur, `bilan-course.json`, empreintes ; journaux de la course.
- Au dépôt, `runs/<id>-course-affinage-mentors-v2/` : acte de gel, configuration assemblée, manifestes de départ et de fin du lanceur (scellés), alertes éventuelles.

## Ce qui est mesuré, et ce qui ne l'est pas

- **Mesuré (descriptif)** : nombre de cartes rendues par fil et par espèce, cartes refusées au format, classes de l'aiguilleur, cartes exclues par la garde A4, verdicts des items des deux juges (lus par la mère seulement, après la course), redites, rôles arrêtés et leurs motifs, coût réel par relais et par rôle, écart au devis v4, reste estimé de chaque clé.
- **Non mesuré** : la valeur, la nouveauté, la justesse ou la faisabilité d'une carte ; une convergence entre espèces n'est pas lue comme un signal de valeur (elle peut tenir au fil servi autant qu'aux espèces) ; les verdicts des juges ne sont ni étalonnés (aucun témoin planté dans cette course) ni comparés à des étiquettes humaines.

## Critères de bonne fin

La course a **fini proprement** si : l'orchestrateur rend le code 0 ; `proposition`, `aiguillage` et `juges` sont « jouée » ; `passe_tableau` et `fusions` sont « retirée » ; le cumul est ≤ 150 USD ; les manifestes du lanceur et de l'orchestrateur sont écrits et scellés ; les lacunes (espèce absente, refus au format, rôle arrêté) sont écrites. Bonne fin ne dit rien de la qualité des cartes. Toute autre issue est rapportée telle quelle (étape « non mesurée », nœud, arrêt), avec ce qui a été fait ; aucune relance sans nouvelle version et mot de la mère.

## Liste d'arrêt

- **Avant le départ** (lanceur, code 2, rien n'est appelé) : course déjà lancée sous ce lanceur ; ligne de GO absente, hors période, révoquée, d'un autre périmètre ou d'un plafond autre que 150 USD ; préenregistrement d'une autre empreinte ou non scellé ; contre-lecture absente, non scellée, qui ne cite pas l'empreinte de ce préenregistrement et celle du lanceur, ne se dit pas du modèle K, dit n'avoir pas relu, ou dont la première ligne de verdict n'est pas exactement « Scellable. » ; variable `RR_ANTHROPIC_API_KEY_MINUIT` absente ; relais Claude sur une autre clé, clé Rigaud déclarée, clé Claude sur un autre relais ; course déjà lancée en v1 ou en v2 ; pièce d'une autre empreinte ; entrée servie dans les retraits ; déclaration des relais absente, non scellée, portant une chaîne de la forme d'une valeur de clé, sans relais Claude ou Argon, adresse hors boucle locale, porte de plafond absente ; orchestrateur à un autre commit, modifié ou d'empreintes différentes ; configuration qui ne tient pas le plafond d'arrêt ; vérification de l'orchestrateur (`--verifier-seulement`) refusée, montant requis autre que 150, spécification non conforme ; bac à sable inactif.
- **Règle des clés** (code 3) : voir plus bas.
- **Pendant la course** (orchestrateur) : plafond dur d'étape (A1, A15) — une étape protégée qui ne tient pas sous 150 n'est pas lancée, « non mesuré (budget) », et la génération ne lance plus rien ; A4 (carte exclue) ; A17 (carte sans passeport à une destination) ; A2 (version servie d'un juge changée : arrêt du rôle) ; A3, A14 (échecs consécutifs, part de sorties inexploitables au-dessus de 0,34 : arrêt du rôle) ; M5 (débordement de Kimi au-dessus de 0,25 : arrêt du rôle) ; A21 (lecture avant la fin de la mesure) ; signal reçu : arrêt propre, manifestes écrits.
- **Après** : cumul lu au-dessus de 150 USD → code 4 et alerte (ne doit pas arriver par construction) ; passe « tableau » ou fusion jouée → écart au préenregistrement, rapporté, aucune lecture des cartes avant la mère.

## Plafond

**150 USD**, plafond d'arrêt de toute la course (GO-2026-11-18-14). Il est S17 de la configuration (portée « course ») et doit être exactement le plafond lu sur la ligne de GO, par le lanceur et par l'orchestrateur. L'orchestrateur ne lance aucune étape dont le plafond dur pourrait le franchir et borne chaque appel au reste de l'étape ; chaque relais reçoit le plafond dur de l'étape à son lancement. Devis v4 (totaux de la v3) : 41,33 USD estimé (103,38 haut) sans Carbon ; 49,81 (121,95 haut) avec Carbon ; la borne des plafonds de session (352 et 422,40) dépasse 150 : seul le plafond d'arrêt borne la dépense.

## Règle des clés

**Clé employée, par relais et par espèce** (R-3228) :

| relais | rôles | variable de la clé (nom seul) |
|---|---|---|
| Claude (un seul relais) | les deux espèces Claude de proposeurs, l'aiguilleur, le premier juge | `RR_ANTHROPIC_API_KEY_MINUIT` (200 USD déclarés) |
| Argon | proposeur Argon, second juge | nom déclaré par la session d'exécution dans la déclaration des relais |
| Kimi, Astra, Carbon (si actifs) | proposeur de l'espèce | nom déclaré par la session d'exécution dans la déclaration des relais |

`RR_ANTHROPIC_API_KEY_RIGAUD` (124 USD, R-3224) **n'est pas employée** et garde son reste. Le lanceur **s'arrête au départ** si la variable `RR_ANTHROPIC_API_KEY_MINUIT` est absente de son environnement (test par le nom, jamais par la valeur) ; il **refuse** un relais Claude déclaré sur une autre clé que Minuit, la clé Rigaud sur quelque relais que ce soit, et toute clé de la famille Claude sur un relais d'un autre fournisseur. Le manifeste de départ écrit la clé de chaque espèce et de chaque rôle interne.

Relevé, avant la course, du crédit et du reste de **chaque clé employée** (fichier du jour, scellé, écrit par la session d'exécution depuis l'interface de facturation ou le compteur ; noms de clé seulement, jamais une valeur). Un crédit « non lisible » arrête le départ, sauf dispense écrite de la mère pour cette clé ; pour la clé Minuit seulement, il est alors **compté au prix relevé** : crédit déclaré 200 USD (R-3228) moins la dépense antérieure déclarée dans le relevé (exigée), écrit comme tel au manifeste. Un reste sous **un cinquième du crédit** ou sous **le plafond d'arrêt (150 USD)** écrit une alerte pour la mère (fichier et sortie) et arrête le départ (code 3) ; ainsi aucune clé ne peut atteindre zéro pendant la course, et Lazar est prévenu avant. Après la course : coût réel par relais, reste estimé par clé, alerte si un reste estimé passe sous les mêmes seuils, confirmation par l'interface de facturation à faire par la session d'exécution (sinon, reste compté au barème du relais, écrit comme tel). Pour Minuit : la course ne peut y dépenser plus de 150 USD, son reste ne peut descendre sous 50 USD, au-dessus du cinquième (40 USD) ; un reste sous 150 USD après la course déclenche l'alerte pour la mère, qui prévient Lazar avant toute course suivante sur cette clé.

## Plan d'analyse et critères de lecture gelés

Aucune analyse décisive. Lecture descriptive, par la mère, après la course : tables des comptes ci-dessus ; les cartes sont lues comme **matière** de l'atelier d'idées, chacune « avis d'un proposeur, jamais un fait » ; tout chiffre ou travail publié cité par une carte reste non vérifié (R7) ; toute zone qu'une carte dit vierge est une question (R8). Lacunes connues du relevé (espèces absentes de certaines questions, refus au format, refus de proposition, pertes de texte des premières courses ; relevé § 3) : rapportées avec tout résultat, jamais compensées. Audit de symétrie (R4) : un lot « trop propre » (toutes les cartes à passeport, tous les items vrais, aucune redite) ou « trop sale » (aucune carte à passeport) déclenche le même contrôle (lecture des journaux de l'aiguilleur et des refus au format) avant toute lecture des cartes.

## Règles de N-073 appliquées à ce texte et à la course

N-073 (mot de Lazar « go recos », R-3231 ; version de travail, contre-lecture à venir) ne fait que restreindre ce que le programme présente comme sien ; elle s'applique à tout texte, celui-ci compris.

- **Aucun héritage d'une génération récompensé** n'est revendiqué ni employé : la course n'a qu'une génération, ne crédite aucune génération ni aucun agent par une descendance, et ne présente aucun signal sur plusieurs générations comme une idée. Si un texte tiré de cette course touche un jour à ce principe, il emploie la lettre fixée par N-073 (§ 1) et ses citations obligatoires (Wang et al., arXiv 2510.21614 ; Zhang et al., arXiv 2505.22954 ; Robeyns et al., arXiv 2504.15228 ; Sutton et Barto ; les trois antériorités de Schmidhuber à lire sur source avant de les citer).
- **Aucune porte « séquentiel contre meilleur de N tirages »** n'est jouée ni revendiquée ; ce protocole est une pratique publiée (Oved et al., arXiv 2610.23977), jamais une idée du programme. La course ne compare aucun bras séquentiel à des tirages indépendants.
- **Diversité des fournisseurs** : la course emploie des proposeurs de plusieurs familles parce que la décision N-072 le demande (règle de l'organisme), **sans rien en revendiquer**. Indice contraire à dire avec elle (N-073, § 5) : Ferreira, Liu, Zheng, « Beyond Symmetric Agents », arXiv 2609.35875, écrivent, sans table qui le teste, que les équipes ne gagnent pas à couvrir plus de familles de modèles une fois la force des membres prise en compte (p. 7) — borne de terrain : réponses fermées, petits modèles ouverts, aucune production d'idées, aucun modèle de frontière (leur p. 9) ; avec les deux indices déjà au dépôt (tirage au hasard, arXiv 2611.04420 ; a priori fixe sans modèle, CADS). Aucune comparaison entre espèces n'est lue comme une mesure de cet énoncé ; les bras témoins de N-073 (§ 5) restent pour l'étape 2, sur devis.
- **Familles inédites, banque sœur** : sans objet ici ; rien n'est dit nouveau ni propre. « Non trouvé dans les pièces lues » ne veut jamais dire « libre » (R8) ; aucun chiffre de la littérature n'est opposable au-delà de ses lectures sur PDF (R7) — ceux de cette section sont repris de N-073, non revérifiés ici.

## Ce que la course ne dit pas

Qu'une carte est vraie, nouvelle, faisable, prioritaire ou meilleure qu'une autre ; qu'une idée des mentors « survit » à quoi que ce soit (aucun test de mort) ; qu'une zone est libre ; quoi que ce soit sur les entrées retirées ; quoi que ce soit sur une hypothèse ou une revendication du programme. Le classement de l'orchestrateur n'est pas une promotion.

## Contre-lecture

À faire avant tout lancement, par un contre-lecteur neuf d'un autre modèle (**modèle K**), qui n'a écrit ni ce préenregistrement ni le lanceur (R2). Son rapport est écrit et scellé au même chemin qu'en v1 : `docs/notes/organisme-affinage-mentors-v1/course-v1/contre-lecture-preenregistrement-course-affinage-mentors-v1.md` ; il cite l'empreinte de ce préenregistrement et celle du lanceur v2, se dit du modèle K, et porte une section « Verdict » dont la **première ligne est exactement** « Scellable. » (en gras ou non) ; tout autre libellé, ou un rapport qui dit n'avoir pas relu (« je n'ai pas relu », « non relu », « sans relecture »…), est refusé par le lanceur. Une correction demandée donne une nouvelle version de ce préenregistrement et du lanceur (R12). L'acte de gel écrit par le lanceur au lancement (empreintes du préenregistrement et de la contre-lecture, verdict lu) est la spécification servie à l'orchestrateur.

## Différentiel v1 → v2

1. **Clé Claude** : v1 laissait la session d'exécution nommer la clé du relais Claude ; v2 la fixe à `RR_ANTHROPIC_API_KEY_MINUIT` pour tous les appels Claude (proposeurs, aiguilleur, premier juge), écrite dans la configuration v2 (`cles`, et `cle` de chaque espèce), dans ce texte (table des clés) et au manifeste de départ (clé par espèce et par rôle).
2. **Arrêt au départ** si la variable Minuit est absente de l'environnement du lanceur (test par le nom) — nouveau.
3. **Garde contre une autre clé** : refus d'un relais Claude sur une autre clé que Minuit, de la clé Rigaud sur tout relais, d'une clé de la famille Claude sur un relais d'un autre fournisseur — nouveau ; la configuration v2 porte `cles_interdites`.
4. **Crédit de Minuit** : s'il n'est pas lisible, compté au prix relevé (200 USD déclarés moins la dépense antérieure déclarée) au lieu d'exiger une dispense ; seuils inchangés (un cinquième du crédit ou 150 USD, code 3 avant le départ ; alerte après).
5. **Contre-lecture** : modèle K au lieu du modèle J ; même chemin ; garde stricte : première ligne de verdict exactement « Scellable. », refus d'un rapport qui dit n'avoir pas relu, mention du modèle K exigée (v1 acceptait « Scellable » suivi d'un deux-points ou d'un tiret).
6. **N-073** : section ajoutée (pas d'héritage récompensé, pas de porte « séquentiel contre meilleur de N », indice contraire sur la diversité des fournisseurs).
7. **Une seule course** : le lanceur v2 refuse si une course v1 ou v2 a déjà un manifeste de départ ; sorties sous `…-v2`.
8. **Devis** : v4, mêmes totaux que la v3, plus la répartition par clé.
9. **Inchangés** : liste des fils et des retraits (`c30928c8…`, 20 entrées retirées, 67 idées servies), consignes, plan, plafond d'arrêt 150 USD, espèces et condition de Carbon, orchestrateur épinglé, ce qui est mesuré et ne l'est pas.
