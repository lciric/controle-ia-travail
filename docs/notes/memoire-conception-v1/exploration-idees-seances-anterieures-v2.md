# Séances antérieures sur l'exploration des idées rares et sur ce qui « allume » une idée — v1

- Pièce de travail (classe C), écrite le 22 novembre 2026 par un agent de lecture (Claude Opus 5.5) de la bibliothécaire, branche `claude/bibliothecaire-v1` (tête `8dd7668d`, à jour de `main` `bec207aa`). Lecture seule ; aucun modèle externe, aucune dépense.
- Question du directeur, verbatim : « il me semble qu'on avait déjà sur le dépôt organisme idéation fait des brainstorms similaires, quelles étaient les conclusions ? »
- Cloisonnement : liste d'autorisation v3 de la bibliothécaire, plus les ajouts accordés pour cette seule question. Rien lu sous `prereg/`, `diag/`, `runs/`, ni d'une autre branche. Les citations sont exactes, au plus 25 mots ; le gras des sources est retiré.
- **v2 (22 novembre, vers 14:40Z)** : Lazar a donné le droit explicite de lire le dépôt public `lciric/ideation-organism` (« je te donne explicitement le droit de lire le depot ideation organism »). Il a été lu en clone superficiel, lecture seule, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` (14 novembre 2026), sous le cloisonnement habituel ; ce qu'il dit est à la section « Dépôt ideation-organism » en fin de page. La v1 (`9638bad3…`) disait ce dépôt non lu (accès refusé) ; elle reste en l'état (R12).
- Commits : la plupart des pièces sont entrées dans l'arbre par le même commit de fusion (`31f83b9b`) ; c'est ce que rend `git log -1 --format=%h -- CHEMIN`, pas la date d'écriture. Les dates données sont celles des pièces.

## Verdict en cinq lignes

1. Oui, plusieurs séances l'ont déjà fait. Six d'entre elles portent sur la question même : diversité (12 nov.), bassins étroits (13 nov.), veille (18 nov.), demande 28 (22 nov.), synthèse du collisionneur (22 nov.), réponse 40 (22 nov.). D'autres, fin octobre, traitent des domaines disjoints et de l'allumage (bisociation, question 7, protocelles).
2. Conclusion constante : sans structure exploitable et nommable sans l'oracle, aucune méthode ne bat le tirage au hasard (ou l'énumérateur sans modèle) en pire cas. Rien en aval des proposeurs n'augmente la chance qu'une idée soit proposée. Aucun score de nouveauté n'est servi à un agent.
3. Les seules méthodes survivantes sont étroites. Côté vue : la liste des paires de traits que l'archive ne croise pas. Côté juge : l'arrêt optionnel, ainsi que des tirages du juge répartis avec arrêt anticipé, verdict « gain de structure ». À cela s'ajoutent la rareté certifiée sur un panel indépendant et un mélange défensif avec un énumérateur.
4. Pour l'allumage : « transition de phase », émergence par essaims et fertilité d'une paire sont restées des hypothèses. La fermeture autocatalytique naïve est triviale. Aucune référence exacte sur l'« allumage » d'un champ n'a été trouvée. Le canal social est occupé par Sourati et Evans et a été repris comme base de comparaison.
5. N'a jamais été tranché ni mesuré : le banc à puits plantés, l'audit des pertes sur les journaux bruts, l'effet de la vue sur la loi des propositions, l'organisme sur les bassins étroits (la génération 1 a échoué) et le cas « idées dans l'air du temps ». Aucune méthode n'a d'indice direct sur des idées vérifiées.

## 1. Séances et pièces, par date

### 1.1 Trancher la recombinaison bisociative : tour du collisionneur (26 octobre)
- Chemin : `docs/notes/pole-scientifique-automatique/synthese-recombinaison-v1.md` ; commit `31f83b9b` ; empreinte `47490973ce85c18b`.
- Conclusions :
  - Le tirage déterminantal d'origine est mort, et il récompensait l'inverse : « il récompense la *similarité* de domaine, l'inverse de ce qu'on veut ».
  - Le critère de fusion est trichable : « une simple enveloppe bat la conjonction même sur un anti-oracle ».
  - L'ordre retenu : valider d'abord le critère contre des tricheurs. « La première expérience n'est donc pas « quel tirage », c'est « le critère de contenu résiste-t-il aux tricheurs ? » »
  - Rien n'est établi sur l'apport du modèle : « Qu'une fusion par modèle de langue accroisse vraiment le contenu empirique (plutôt qu'une juxtaposition ou une copie). »
- Registre : R-527 (routine ; décision de forme renvoyée à l'expérience 1). Exploitée par le banc des tricheurs (`banc-tricheurs-v1.md`, R-566, selon l'inventaire des courses).

### 1.2 Mesure de l'universalité : remue-méninges du texte III (30 octobre)
- Chemin : `docs/notes/ideation-organisme-v1/course-2/texte-III-v1/synthese-texte-III-v2.md` ; `31f83b9b` ; `a3844e4ffa52f0de`.
- Conclusion utile ici, une seule : la masse manquante de Good et Turing est déjà proposée pour borner ce qui n'a pas été vu. On y lit : « Famille d'idées « pénaliser par la masse manquante » ». La version d'abondance est critiquée au profit de la version d'incidence.
- Registre : R-835 (pièces écartées versées en quarantaine, non lues ici). La suite donnée à la masse manquante n'a pas été trouvée dans ce que j'ai lu.

### 1.3 Le bisociateur (domaines disjoints) : question fusionnée et tour du collisionneur (30 et 31 octobre)
- Chemins : `docs/notes/bisociation-litterature-reelle-v1/collisionneur-bisociation-lot-v1/question-fusionnee-argon-collisionneur-v1.md` et `…/synthese-bisociation-lot-v2.md` ; `31f83b9b` ; empreinte de la synthèse `23c2888ddd924b85`.
- La règle en vigueur s'énonçait « loin en domaine, proche en concept ». Les antériorités relevées sont Swanson 1986 (littératures disjointes), Burt (trous structuraux), Uzzi, Fleming et Gu-Krenn.
- Conclusions :
  - Fertilité d'une paire, transition de phase, émergence par essaims : la transition de phase est « HYPOTHÈSE pour les quatre » ; aucune affirmation forte n'est établie.
  - Défaut relevé sans concertation : « le pic de variance binomiale pris pour de la criticité ».
  - Allumage d'un champ : « personne ne donne de référence exacte pour un « allumage » de champ ». Le seuil de Bettencourt n'est que rapporté, sans le PDF.
  - Prédire les idées à venir, ce qui est proche des idées « dans l'air du temps » : « Reproduire Gu-Krenn avant de s'en servir ». Il faut aussi battre un témoin de popularité seule et contrôler par une rétrodiction inversée.
  - Nœud proposé : « Nœud : retirer « transition de phase » des préenregistrements sur littérature réelle. »
- Registre : synthèses v2 en R-867 et R-884. Canal social accordé par le directeur en R-907 (« Canal social : occupé. […] on pourrait en faire un bras. : go »), comme base reprise et non comme revendication. Antériorité de pra2.1298 en R-906 : la règle y est « occupée en partie, pour la forme ». L'issue du nœud « transition de phase » n'a pas été trouvée.

### 1.4 L'allumage comme ensemble autocatalytique de fiches : question 7 (31 octobre)
- Chemin : `docs/notes/bisociation-litterature-reelle-v1/collisionneur-question-7-v1/synthese-question-7-v2.md` ; `31f83b9b` ; `0ced3b28fa5cf1c2`.
- Point de départ, la question du directeur : « et l'allumage et la fertilité là-dedans ? cela me fait penser à l'allumage aux origines de la vie ».
- Conclusions :
  - L'analogie casse sur la catalyse : « La pièce conv-audit et ma conception initiale confondaient toutes deux fermeture et autocatalyse ».
  - « Le taux de reproduction brut (R0 ou R_endo) est fixé par la dose que l'expérimentateur choisit. »
  - Il faut donc lire un écart à l'appariement aléatoire. Tout seuil doit être « exprimé en écart à son espérance sous appariement aléatoire à dose égale ».
  - « aucune définition prospective de la fertilité n'est établie ».
- Registre : R-884 (proposer avec recommandation ; décisions D7-1 à D7-4 à défaut, D7-5 de dépense sans défaut). L'inventaire des courses la classe « lue, non reprise ».

### 1.5 Protocelles : papier croisé avec l'organisme, deux tours (31 octobre)
- Chemins : `docs/notes/protocelles-collisionneur-v1/synthese-protocelles-tour1-v2.md` (`7117a8d93498eb28`) et `…/synthese-protocelles-tour2-v1.md` (`b000cc5e1841f3e1`) ; `31f83b9b`.
- Conclusions :
  - « Aucune prédiction globale d'allumage n'est signée sans condition. »
  - « Le catalyseur est le bisociateur, non une fiche. »
  - Accord des espèces, selon l'inventaire des courses : première mesure « un parent contre deux parents », avec deux préalables.
- Registre : R-911, R-916, R-939 ; l'inventaire la classe « lue, non reprise », et la première mesure n'a « jamais montée ».

### 1.6 Diversité des idées de l'organisme : collisionneur, tour 1 sur 4 (12 novembre)
- Chemin : `docs/notes/collisionneur-diversite-idees-v1/synthese-v1.md` ; `31f83b9b` ; `4f99077b70027823`.
- Conclusions :
  - Mesurer d'abord : « la première expérience est un banc de métrologie hors ligne, sans appel de proposeur ».
  - Rejets convergents : « aucune récompense numérique de la nouveauté, ni dans le juge, ni servie à un agent ». Ni quota de formes, ni masquage d'archive.
  - Le danger : « toute pression vers la variété pousse vers `si_sinon` et `melange` », c'est-à-dire vers la classe que le nul ne couvre pas.
  - La moyenne globale « efface une différence confinée à une région rare ».
- Registre : R-2467, R-2469 (conception du monde riche et des doublons) ; exploitée.

### 1.7 Bassins d'idées étroits et profonds (13 novembre) : remue-méninges de la mère, collisionneur à cinq, trois consultations à part, recoupement, organisme sur trois générations
- Chemins et empreintes, tous au commit `31f83b9b` :
  - remue-méninges : `docs/notes/bassins-etroits-idees-v1/remue-meninges-mere-v1.md`, `f3c46703f19d4407` ;
  - synthèse : `docs/notes/collisionneur-bassins-etroits-v1/synthese-v1.md`, `5fd7e26fc8c04ddd` ;
  - recoupement : `docs/notes/organisme-bassins-etroits-v1/recoupement-methodes-v1.md`, `eecd98fab0beff8c` ;
  - génération 1 : `…/operation-g1-v1.md`, `3beef39eadae4693`.
- Mot du directeur (R-2523) : « et si nous utilisoons des methodes mahematiques sophisitiquees pour pousser a explorer les bassins etroits et profonds d'idees originales ? »
- Conclusions :
  - La mère, sur la borne : « Sans structure, aucune méthode ne le trouve gratuitement : il faut de l'ordre de 1/masse tirages. »
  - Quatre leviers seulement : déformer la loi, exploiter une structure, réallouer le budget, donner la puissance au juge. Classement de la mère : courbe dose-réponse, puis masse manquante (Good-Turing, Chao).
  - Collisionneur : « Il n'y a pas de moteur à pousser ». Et : « Un gain n'existe que sous une structure nommable sans l'oracle ».
  - « Côté vue, la sophistication s'est réduite à une liste ». C'est la liste des paires de traits que l'archive ne croise pas.
  - Côté juge, les deux méthodes que la mère plaçait au deuxième rang tombent. La valeur e par strates n'aide pas une carte déjà localisée ; les poids de multiplicité selon la nouveauté sont « une prime de nouveauté sous un autre nom ». L'arrêt optionnel survit.
  - L'inconnue centrale : « la loi des propositions d'un modèle bouge-t-elle quand on lui montre la liste ? Aucun fait ne le dit ».
  - Les idées de la mère restées seules et non critiquées : métadynamique ou histogramme plat, qualité et diversité, sélection douce, îles et échange de répliques, masse manquante.
- Registre :
  - Recommandation de la synthèse « (non tranchée) » : arrêt optionnel, puis liste des paires (R-2541).
  - Organisme : GO-2026-11-13-03 (60 USD). La génération 1 est « close en défaut, sans fiche » (R-2545). Le lanceur v3 est jugé « non autorisable » (R-2556). Une seule relance au total est permise (R-2558). Aucune relance n'est trouvée dans ce que j'ai lu.
  - L'inventaire des courses (`docs/notes/inventaire-collisionneurs-organismes-v1/inventaire-v1.md`, `b49dc2462382206d`) donne le tour pour exploité par le préenregistrement de l'idée 1.2 (tirages du juge répartis avec arrêt anticipé). Ce préenregistrement est hors périmètre et n'a pas été ouvert. R-2851 fait venir l'idée 1.2 d'un relevé de fiches « conception propre » : deux origines dites, à confronter. Son verdict est consigné : « gain de structure » (R-3008), chiffres non recopiés.

### 1.8 Les voisins « bassins d'idées » lus sur PDF : Fork-and-Flush et « Scaling Discovery Requires Forgetting » (13 novembre)
- Chemin : `docs/notes/lecture-voisins-bassins-idees-v1.md` ; `31f83b9b` ; `80abfae70a68a958`.
- Conclusions :
  - « Voisinage serré, pas de collision ».
  - « à budget égal, repartir du meilleur résultat avec un contexte neuf bat le fil continu ».
  - « hériter moins fait mieux », ce qui pèse sur la prémisse de l'héritage récompensé.
  - Grouper les idées par ce qu'elles font est « pris » pour des artefacts libres.
- Registre : versée avant le recoupement (R-2541) ; reprise par la veille du 18 novembre.

### 1.9 Veille « exploration d'idées nouvelles par les modèles de langue », puis la décision N-073 (18 et 19 novembre)
- Chemins : `docs/notes/veille-exploration-idees-v1/synthese-v1.md` (`dc35b778c257e923`) et `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` (`b95688df5e695da7`), avec ses compléments 1 à 3 (`61903909e8aaaa70`, `5707dbd8bdd8ccc2`, `4ca0ce7b040b917d`) ; `31f83b9b`.
- Conclusions :
  - « Aucune de nos revendications de fond n'est libre ».
  - Bassins d'idées : « Les lancements indépendants plafonnent dans des régions séparées, l'oubli bat la continuation. »
  - Séquentiel contre le meilleur de N tirages : « protocole OCCUPÉ » (Oved et al.). L'héritage récompensé : « principe OCCUPÉ » (machine de Huxley-Gödel).
  - Idée à prendre en premier : « Témoins « vrais mais dérivables » dans chaque monde planté ».
- Registre : « Sept décisions pour toi. : go recos » (R-3231). N-073 en R-3233. Les compléments 1 à 3 sont GO-2026-11-19-07, -10 et -17 (selon `CLAUDE.md`).

### 1.10 Méthodes pour produire des mathématiques nouvelles : Fable, puis Argon, Carbon et Astra (21 novembre)
- Chemin : `docs/notes/mathematiques-nouvelles-v1/brainstorm-methodes-v1/synthese-reponses-externes-v1.md` ; `31f83b9b` ; `fb5e83972b01eb5a`. La réponse de Fable est en `be7f12c9178a79f3`, sous le même dossier.
- Conclusions :
  - Sur les méthodes, convergence : « évaluateur exact en rationnels, témoin fini, certificat, juge formel, nouveauté jugée par un humain du domaine ».
  - Apport des modèles extérieurs : « la réduction, par dualité, d'une garantie universelle à un certificat algébrique fini ».
  - Sur les chances de publication : « aucun taux de base » (Fable, Astra).
- Registre : GO-2026-11-22-42, « Mathématiques : option A (recherche d'antériorité par étages) « go » ».

### 1.11 Demande 28 : idées originales, puits étroits et profonds (22 novembre ; Fable en effort très haut, puis maximal, et Opus 5.5 en second regard)
- Chemins (commits respectifs) :
  - `docs/notes/demandes-fable-api-2026-11-22-v1/demande-28-idees-originales-puits-profonds-v1.md` (`afaaa1e6`, `f552f514961f78be`) ;
  - `…/reponse-28/relecture-fable-api.md` (`7297705b`, `05c72e054ed7b5af`) ;
  - `…/reponse-28-effort-max/relecture-fable-api.md` (`529d061b`, `1261c8eeb9f00711`) ;
  - `…/reponse-28-opus55-max/reponse-opus55-v1.md` (`9154eccf`, `04aa3de4a2afddc2`).
- Conclusions :
  - Fable maximal : « Un puits n'est étroit que sous une mesure : plutôt que tirer plus fort, chercher le proposeur, la représentation ou le domaine d'origine sous lequel il est large. »
  - Fable maximal : « les succès documentés tiennent à un vérificateur bon marché et à une archive de paliers, non à un mécanisme de nouveauté ».
  - Ordre proposé : audit des pertes sur les journaux bruts, loi spontanée des proposeurs, qualification de la garde, réactivité à la vue, puis banc complet.
  - Opus : « Certifier qu'un puits est étroit coûte à peu près autant que le trouver par force brute ».
  - Opus propose un levier extérieur : « nourrir les proposeurs de ce que les autres modèles n'ont pas vu ».
  - Liste d'exclusion des classes fréquentes : permise au banc seulement, avec placebo. C'est l'option (b) chez Fable maximal (confiance 0,65) et l'option B chez Fable très haut (0,6).
- Registre : envoi décidé par GO-2026-11-22-42. Protocole X par GO-2026-11-22-47 : question neutre jugée neutre au test de devinette, avec 0,35. Les décisions D1 à D4 et D-1 à D-6 n'ont pas été trouvées tranchées.

### 1.12 Synthèse du collisionneur sur les idées rares et vérifiées, six modèles et trois tours (22 novembre)
- Chemin : `docs/notes/collisionneur-v9/syntheses-protocole-x-v1/note-synthese-idees-originales-v1.md` ; `e1021114` ; `10448cd446cf6934`.
- Conclusions :
  - « La rareté se certifie, elle ne s'observe pas. »
  - « Le contrôle dans la queue est le goulot probable. »
  - « Aucune intervention n'a d'indice direct sur des idées vérifiées. »
  - Ordre retenu : devis du panel, épreuve des instruments sans modèle, essai « témoin contre témoin », audit du contrôle dans la queue sur des faux naturels.
  - Réserve de fond : « la transposition aux idées de recherche du programme reste l'hypothèse non testée la plus lourde ».
- Registre : exécution de GO-2026-11-22-47. C'est sa phrase sur l'absence de preuve directe qui a provoqué le mot du directeur et le mandat (§ 1.14).

### 1.13 Réponse 40 : méthodes mathématiques qui forcent l'exploration des puits étroits (22 novembre, Fable maximal)
- Chemin, copie hors dépôt : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/reponse-40.md`. Source annoncée : branche `claude/protocole-x-puits-etroits-v1`, commit `3ab317c4` ; je ne l'ai pas vérifiée (autre branche, hors périmètre). Empreinte de la copie : `7e6e539c2cbc03f0`, égale au préfixe annoncé.
- Conclusions :
  - « Dans le pire cas, la meilleure garantie est donc celle d'un énumérateur sans modèle. »
  - « On peut forcer la proposition à prix connu. On ne force la découverte que si l'évidence disponible paie la longueur de description. »
  - Ce qui force à prix connu : un mélange défensif (une part ε du budget suit une loi mécanique), un rejet exact par programme, et des valeurs e pondérées par la longueur de description.
  - Ce qui échoue sur le cas visé : le tempering parallèle « mélange lentement précisément quand un mode étroit côtoie un mode large ». « Entropie croisée : se referme sur le bassin large. »
  - « Exclure par l'invite n'est pas conditionner. »
- Registre : GO-2026-11-22-67, R-4872, R-4883 (question neutre v3 « orientée de justesse »). Les décisions D1 à D4 n'ont pas été trouvées tranchées.

### 1.14 Mandat : explorer au-delà de la marche au hasard, et ce qui « allume » une idée (22 novembre, vers 13:53Z)
- Chemin : `docs/notes/exploration-idees-fable-v1/mandat-demande-approfondie-exploration-et-allumage-v1.md` ; `bec207aa` ; `6909f66e1587eb14`.
- C'est le mandat en cours, non une conclusion. Il pose les deux cas de l'allumage : « domaines disjoints qui ne se parlent pas, et idées « dans l'air » qui découlent de découvertes antérieures ».
- Il joint Good 1953 et signale Good et Toulmin 1956. Il prescrit : « Ne répète pas ce qu'elles disent : pars de leurs trous. »
- Sources versées, citées par nom seulement : `docs/sources/exploration-idees-v1/` (Good 1953, FunSearch 2023, « A Society of AI Scientists », « When Lie Detectors Learn Model Identity », captures de Good 1953).
- Registre : classe C, sans dépense ; le cadre des sessions filles par l'abonnement est en GO-2026-11-22-70.

## 2. Tableau des méthodes d'exploration

| Méthode | Où proposée | Conclusion | Testée ? |
|---|---|---|---|
| Tirage indépendant, énumérateur sans modèle | bassins étroits, réponse 40 | base obligatoire ; meilleure garantie en pire cas (réponse 40) | non |
| Mélange défensif avec une loi mécanique, recherche universelle de Levin | réponse 40 | garantie de proposition à prix connu, rien hors grammaire | non |
| Rejet exact par programme, tirage sans remise | réponse 40 ; liste d'exclusion dans la demande 28 | gain borné par 1/(1 − p(S)) ; l'exclusion par invite ne conditionne pas | non |
| Température, échantillonnage contre la vraisemblance | remue-méninges de la mère (A1), demande 28, réponse 40 | agit sur les jetons, non sur les classes ; un optimum intérieur est à chercher sous décodage contraint | non |
| Liste des paires de traits non croisées par l'archive (vue) | bassins étroits (V2) | survivante pleine ; effet de la vue inconnu | non |
| Plan combinatoire, tableaux orthogonaux | bassins étroits (V3), mère (B2) | survivante ; couvre les affectations, non les idées | non |
| Tirage déterminantal, répulsion | recombinaison (26 oct.), bassins étroits (V6), réponse 40 | noyau d'origine mort ; diversité des vues, pas des sorties | en partie, sur processeur (génération 0, 26 oct.) |
| Qualité-diversité, cartes d'élites, nouveauté seule | mère (A4), demande 28, collisionneur du 22 nov. (F) | structurer l'archive servie, jamais récompenser ; sans borne de temps d'atteinte connue | non |
| Métadynamique, histogramme plat | mère (A3), réponse 40 | mère seule, non critiquée ; quota par cellule, inutile si le puits est étroit partout | non |
| Fractionnement multiniveau, marchepieds, graphe de prérequis | mère (B1), Kimi à part (C3), réponse 40 | utile seulement avec parents détectables ; sans palier, revient au tirage brut | non |
| Entropie croisée, échantillonnage préférentiel adaptatif | réponse 40 | se referme sur le bassin large | non |
| Recuit, îles, tempering parallèle | mère (C3), réponse 40 | lent précisément quand un mode étroit côtoie un mode large | non |
| Bandits extrêmes, recherche arborescente | mère (C1), demande 28, réponse 40 | bon objectif (le maximum) ; exige une récompense ; hors ligne seulement | non |
| Valeur e par strates, poids de multiplicité selon la nouveauté | mère (D1, D2) | contredits par le collisionneur | non |
| Arrêt optionnel, tirages du juge répartis avec arrêt anticipé | bassins étroits (J1) ; idée 1.2 | survit, mais sert la survie d'une idée, pas sa découverte | oui : idée 1.2 jouée sur processeur, verdict « gain de structure » (R-3008) |
| Masse manquante (Good-Turing, Chao) | texte III, mère (E1), demande 28, collisionneur du 22 nov., mandat | diagnostic agrégé et règle d'arrêt, jamais un score par idée | non |
| Courbe dose-réponse, banc à puits plantés | mère (E2), demandes 28 et 40 | expérience décisive ; la largeur s'estime, elle ne se règle pas | non |
| Rareté certifiée sur un panel indépendant | collisionneur du 22 nov. | adoptée par les six modèles | non |
| Repartir d'un contexte neuf, oublier | lecture des voisins, veille | occupé par la littérature ; déjà en place (session neuve) | dans la littérature seulement |

## 3. Tableau de ce qui allume une idée

| Mécanisme | Où | Conclusion | Testé ? |
|---|---|---|---|
| Domaines disjoints, « loin en domaine, proche en concept » | question fusionnée et tour sur la bisociation (30 et 31 oct.) ; pra2.1298 | règle occupée en partie pour la forme ; trou à structure commune, rétrodiction inversée et base de ponts datés à faire | les résultats sur mondes inventés sont dits chez conv-audit, non trouvés ici |
| Fertilité d'une paire, sur-additivité | même tour ; question 7 | hypothèse ; aucune définition prospective établie | non |
| Transition de phase | bisociation, question 7 | hypothèse ; retrait proposé des préenregistrements sur littérature réelle | non |
| Essaims communicants contre tentatives indépendantes | question fusionnée (E) | hypothèse pour trois espèces sur quatre | non |
| Ensemble autocatalytique de fiches, taux de reproduction | question 7, protocelles | fermeture naïve triviale ; le taux de reproduction est fixé par la dose ; lire l'écart à l'appariement aléatoire | non (première mesure « un parent contre deux parents » jamais montée) |
| Seuil d'allumage d'un champ (Bettencourt) | question G de la bisociation | rapporté sans PDF ; aucune référence exacte | non |
| Canal social (Sourati et Evans) | R-907 | occupé avec résultats ; bras repris comme base de comparaison | non trouvé |
| Idées « dans l'air du temps », prédiction de liens (Gu-Krenn) | bisociation | reproduire Gu-Krenn d'abord ; battre la popularité seule | non |
| Combinaison atypique sur fond conventionnel (Uzzi, Fleming) | demande 28 | citée ; variance plus haute | non |
| Abstraction et transfert : le puits large sous un autre habillage | demande 28 | question ouverte pour les modèles ; un monde « transférable » est proposé au banc | non |
| Données propres que les concurrents n'ont pas | Opus, demande 28 (D-5) | recommandé (a), confiance 0,6 | non |

## 4. Ce qui n'a jamais été testé
- Le banc à puits plantés, la courbe dose-réponse et le critère de réfutation par famille de mondes (mère, demandes 28 et 40).
- L'audit des pertes sur les journaux bruts : idée jamais proposée, ou proposée puis perdue ?
- La réactivité de la loi des propositions à la vue (liste des paires, placebo).
- La loi spontanée des proposeurs : rang et fréquence, masse non vue, recouvrement entre familles.
- La masse manquante comme règle d'arrêt, validée contre l'oracle (Good et Toulmin compris).
- L'énumérateur sans modèle et les valeurs e pondérées par la longueur, comme base.
- Le rejet exact contre l'exclusion par invite ; la température sous décodage contraint.
- L'organisme sur les bassins étroits : la génération 1 a échoué, et les générations 2 et 3 ne sont pas trouvées.
- La reproduction de Gu-Krenn, la base de ponts datés et la rétrodiction inversée (selon ce que j'ai lu).
- La mesure « un parent contre deux parents » des protocelles ; l'ablation du catalyseur de la question 7.
- La rétrodiction sur des textes postérieurs à la coupure, et les prédictions scellées jugées à l'aveugle (validité externe).
- La transposition aux idées de recherche en langue libre, au-delà des domaines exécutables.

## 5. Non trouvé et hors périmètre
- Non trouvé dans ce que j'ai lu :
  - une décision du directeur sur les recommandations de la synthèse des bassins étroits (« non tranchée ») ;
  - une décision sur les D1 à D4 de la demande 28, les D-1 à D-6 d'Opus et les D1 à D4 de la réponse 40 ;
  - l'issue du nœud « transition de phase » et des défauts D7-1 à D7-4 de la question 7 ;
  - l'issue de la course 2 à trois bras de bisociation (GO-2026-10-31-04) ;
  - une relance de l'organisme sur les bassins étroits après R-2558 ;
  - une séance sur Good et Toulmin 1956 avant le mandat.
- Homonymes écartés :
  - « allumage » au sens de mise en marche de l'orchestrateur (fiches des quatre décisions sur l'orchestrateur v68, GO-2026-11-20-05) ;
  - « marche au hasard » et « puits peu lu » au sens défensif (`note-propositions-retenues-six-dossiers-v1.md`, `c0f49f1d6e1d0f38` ; `brainstorm-rapport-openai-surveillance-v1.md`, `2ec494d6e976322c`) : sans rapport avec l'exploration des idées.
- Hors périmètre, je ne confirme ni n'infirme :
  - les préenregistrements de l'idée 1.2 et de l'idée 1.1 sous `prereg/` ;
  - les cellules et consultations à part brutes, lues par les synthèses et non par moi ;
  - les pièces versées en quarantaine (R-835) ;
  - les branches `donnees/*` et `claude/protocole-x-puits-etroits-v1` ;
  - les PDF de `docs/sources/exploration-idees-v1/` (noms seuls).
- Dépôt public `lciric/ideation-organism` : lu en v2, voir la section « Dépôt ideation-organism » ci-dessous. Ce dépôt-ci en rapportait déjà :
  - sa création publique par le directeur, avec orchestrateur, conception, README et manifeste (R-989) ;
  - des préenregistrements de l'attaque de Goodhart et des contre-lectures poussés sur `claude/new-session-7qxayx` (R-1543, R-1563, R-1715) ;
  - des mises à jour de la page publique (R-1771 ; versions 2 à 4 du 13 novembre, R-2583 à R-2594) ;
  - son usage comme orchestrateur figé de l'organisme sur les bassins étroits (clone au commit `be6b5af9`).
- Aucune séance de remue-méninges sur l'exploration n'y est inventoriée dans ce que j'ai lu. Le mandat en demande la lecture : elle reste à faire par une session qui y a accès.

## Dépôt ideation-organism (ajouté en v2)

Lecture déléguée à un agent de la bibliothécaire, citations vérifiées par sondage (lignes 8 et 12 de `proposeurs_references.py`, 10-11 de `recombinaison.py`, 129 du `README.md`). Chemins relatifs à la racine de `lciric/ideation-organism`, commit `a41b7b50`. Verdict : aucun remue-méninges explicite sur battre la marche au hasard ni sur l'allumage ; l'exploration y est une hypothèse à réfuter contre deux bases sans modèle (tirage au gabarit, chercheur mécanique) ; quatre mécanismes codés (hors des bassins déjà promus, marchepieds, bisociateur, moissonneur), aucun résultat réel versé ; seul résultat touchant l'exploration : l'avantage espéré des proposeurs exploratoires ne s'est pas montré sur mondes plantés (une carte promue dans chaque bras).


- Pièce de travail (classe C), écrite le 22 novembre 2026 par un agent de lecture (Claude Opus 5.5). Lecture seule ; aucun commit, aucun appel réseau, aucun modèle externe.
- Dépôt lu : clone public en lecture seule `/home/user/lciric/ideation-organism`, un seul commit visible `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` (clone superficiel). Droit de lecture donné par Lazar.
- Question de Lazar, verbatim : « il me semble qu'on avait déjà sur le dépôt organisme idéation fait des brainstorms similaires, quelles étaient les conclusions ? »
- Complète `docs/notes/memoire-conception-v1/exploration-idees-seances-anterieures-v1.md` (dite ci-dessous « la page de controle-ia-travail »), qui n'avait pas pu lire ce dépôt.
- Empreintes : 16 premiers signes du sha256 calculé par `sha256sum` sur le clone. Lignes : numéros du fichier tel qu'il est dans le clone. Citations exactes, moins de 30 mots. Pour les fichiers de code, je n'ai lu que les docstrings et quelques tables de constantes.

### Verdict en cinq lignes

1. Non : le dépôt de l'organisme ne contient **aucun remue-méninges** sur les méthodes qui battraient la marche au hasard, ni sur l'allumage d'une idée. Il contient du **code et des textes de lecture** qui font de l'exploration une hypothèse à réfuter contre des références sans modèle.
2. La position constante du dépôt : un tirage au hasard au gabarit et un chercheur mécanique sont des bases obligatoires. Si le proposeur à modèle ne les bat pas, la prise « proposeur » ou la prise « exploration » « tombe ».
3. Les mécanismes d'exploration codés sont au nombre de quatre : la stratégie « hors des bassins déjà promus » (le même esprit que la liste des paires non croisées), le tirage à marchepieds, le bisociateur à trois bras et le moissonneur de nouveauté. Aucun n'a de résultat réel versé dans le dépôt.
4. Ce qui a été joué en réel ne dit rien de l'exploration. Pour la course v67, le verdict dit : « rien […] sur la qualité des idées ». Les 11 cartes retenues sont « des variantes proches d'un même constat ». Seul un résultat sur processeur touche à l'exploration : l'avantage espéré des proposeurs « exploratoires » ne s'est pas montré.
5. Jamais éprouvé : le bras aléatoire contre de vrais proposeurs (le tour fermé n'est pas scellé), le duel des proposeurs, les marchepieds sur résultats, le bisociateur et la moisson en réel, et les stratégies d'allocation (non codées).

### 1. Pièces pertinentes

#### 1.1 `README.md` (statut du 13 novembre 2026) — `04ac692e9500dd37`
- Le bisociateur est présenté comme le moteur d'exploration de la boucle. Ligne 66 : « so that the loop also explores what no proposer wrote. »
- Seul résultat qui porte sur l'exploration, sur processeur : les témoins plantés passent, mais l'avantage espéré des proposeurs « exploratoires » n'apparaît pas. Ligne 129 : « the hoped-for advantage of exploratory proposers did not show (1 promoted card in each arm) ».
- Premier tour réel : beaucoup de redites. Ligne 135 : « 29 idea cards, 27 eligible after the gatekeeper, 17 distinct ideas (12 duplicate pairs) ».
- Second tour réel : joué sans le bisociateur ; les juges modèles plafonnent et ne départagent rien. Ligne 136 : « without the bisociation board » ; « The two LLM judges sat at their ceiling ».
- Attaque de Goodhart (W2) : un proposeur à modèle retrouve la loi du monde, ce qui viole le critère de nouveauté sans aucune optimisation contre le juge. Ligne 140 : « 42 of the 48 reproduce the world's own law exactly ».

#### 1.2 `orchestrator/conception-v7-v1.md` (27 octobre 2026) — `31fc8c4bc286341f`
- Le proposeur n'a qu'une « liberté bornée » : il choisit dans un catalogue de stratégies et déclare celle qu'il emploie. On mesure ensuite quelles stratégies produisent des promues.
- Ligne 74 : « le proposeur déclare la stratégie employée (mesure : quelles stratégies produisent des promues) ».
- L'aptitude sert au tirage à marchepieds. Ligne 96 : « Aptitude : `log_richesse_max` de la dernière promotion, utilisée par le tirage à marchepieds et par l'index. »

#### 1.3 `orchestrator/pole/proposeur.py` (27 octobre 2026) — `a77018584ec5d20c`
- La stratégie « hors des bassins déjà promus » a été demandée et accordée par Lazar le 27 octobre. Lignes 3-4 : « son « yes go » de 15:20 pour la stratégie « hors des bassins déjà promus » ».
- Sa définition, ligne 40 : « un couple (moniteur, trait) qu'aucune fiche promue ne couvre encore ».
- Le proposeur ne voit jamais la richesse. La mesure prévue est le nombre de promues par stratégie (lignes 13-14).
- Deux stratégies d'allocation sont restées des hypothèses, « non codées » (ligne 21) : la « loi mère » et le champ moyen de Thouless-Anderson-Palmer, venues de Gemini. Ligne 47 : « à tester comme hypothèse ».

#### 1.4 `orchestrator/pole/proposeurs_references.py` (sans date dans la pièce ; version 7 de v7) — `6ed7e56fb1a1f744`
- Deux références gratuites sont posées avant tout duel payé. Ce sont des barres à battre, et non des méthodes d'exploration.
- Ligne 8 : « proposeur à modèle ne fait pas mieux, la prise « proposeur » tombe » (contre l'aléatoire au gabarit).
- Ligne 12 : « si un proposeur à modèle ne fait pas mieux, la prise « exploration » tombe » (contre le chercheur mécanique, critère de Schwarz).

#### 1.5 `orchestrator/pole/simulation.py` (sans date ; versions 0.3.0 et 0.4.0) — `be14d44e7a8ebf6b`
- Le monde simulé rend des « lignées fécondes » avec une probabilité de 0,85 contre 0,35 : c'est l'hypothèse que les marchepieds exploitent. Sans elle, la vérité d'une fille est tirée au hasard.
- Ligne 12 : « que les marchepieds exploitent ; sans elle, la vérité d'une fille reste tirée au hasard, probabilité 0,5) ».
- L'agent simulé joue « hors_bassins_promus » en tirant un couple libre au hasard (lignes 410-414). La stratégie n'est donc qu'un tirage uniforme dans ce qui n'est pas couvert.

#### 1.6 `orchestrator/pole/recombinaison.py` (sans date ; versions 0.3.0 et 0.4.0) — `71faad38644c77ae`
- Le tirage déterminantal (« forme corrigée ») a perdu contre le tirage stratifié dans l'essai des ponts plantés. Le stratifié est passé par défaut (R-527).
- Lignes 10-11 : « après l'essai des ponts plantés `72cff8a0…` où la forme corrigée perd de 4,8 et 2,2 points contre lui ».
- Les marchepieds n'aident que si les vraies associations se regroupent. Lignes 18-19 : « les marchepieds n'aident que si les vraies associations se regroupent […] sans cela, ils ne doivent rien coûter de plus que le hasard. »

#### 1.7 `orchestrator/demonstrations/demo_cycle_v5.py` (27 octobre 2026) — `a457a8e284e58fc1`
- Une démonstration à deux faces compare les marchepieds au tirage stratifié, dans un monde fécond et dans un monde plat.
- Lignes 17-18 : « (B1) monde fécond : plus de vraies filles promues avec marchepieds ; (B2) monde plat : pas d'avantage ».
- Le résultat n'est pas versé dans le dépôt.

#### 1.8 `orchestrator/demonstrations/demo_couche1_proposeur_v7.py` (27 octobre 2026) — `0a782a5b1fab4cac`
- La lecture est fixée avant l'exécution : dans le monde planté, l'exploration du développement doit faire mieux que le proposeur aveugle.
- Ligne 14 : « E2 : monde planté : l'exploration promeut au moins une fiche par sous-population ; l'aveugle en promeut moins, ou ».
- Le résultat rapporté par le README (ligne 129) est d'une carte promue dans chaque bras. E2 n'est donc pas tenu dans le sens espéré.

#### 1.9 `orchestrator/demonstrations/demo_proposeurs_v7.py` (27 octobre 2026) — `6ca98c3f050d54d8`
- Quatre bras sans modèle : scripté aveugle, scripté avec exploration, aléatoire, mécanique.
- Lignes 20-21 : « si « mecanique » ≥ « scripte_exploration », le scripté n'apporte rien au-delà d'une recherche mécanique ».
- La v2 change de grammaire pour que le mécanique ne domine plus. Ligne 31 : « (attendu : moins de la moitié de ses 23 sur 35 de la v1, en proportion) ». Le chiffre de la v1 n'est cité que dans la docstring ; aucun fichier de résultat n'est versé.

#### 1.10 `orchestrator/demonstrations/duel_proposeurs_v7.py` (version 10, sans date) — `d8f31817da702064`
- Le duel payé est conçu : Opus 5.5, avec et sans développement, contre le mécanique et l'aléatoire, sur des mondes hors de l'espace du mécanique. Il est lu par un pari apparié borné.
- Ligne 13 : « Règle d'arrêt : après `--arret-apres` mondes, si M-expl n'a rien retrouvé, la ». Aucun résultat dans le dépôt.

#### 1.11 `orchestrator/pole/bisociateur_v53.py` (sans date ; décisions R-601 à R-643) — `962eb8ce22d5af1b`
- Trois bras : méta « trou à structure commune », substitut de Gu et Krenn « jamais reliés », et basique « loin en domaine, proche en concept ». Le désaccord des lecteurs n'entre jamais dans le score.
- Ligne 3 : « Trois bras, `k_paires` paires par session chacun (injecté ; S22/S23), **pas de bras hasard** : ».

#### 1.12 `orchestrator/pole/moisson.py` (29 octobre 2026) — `35d9a996aaacf6d6`
- Le moissonneur de nouveauté ne lit que les métadonnées et les résumés d'arXiv et d'OpenAlex. Ses touches sont « non opposables ». Aucune moisson réelle n'est faite ici.
- Lignes 3 et 5 : « métadonnées et résumés seulement ; quotas du tableau ; Brave exclu » ; « première moisson réelle = GO séparé chez session-depot — rien de réel ici) ».

#### 1.13 `orchestrator/pole/ideation.py` (28 octobre 2026, version 42 et suivantes) — `4ee70d25567a9b3a`
- Les mesures de nouveauté sont consignées mais jamais servies. Lignes 92-93 : « (distances entre versions d'une fiche, sources citées, nouveauté), jamais servies aux juges ni au classement (N-053 : aucune sélection sur ces mesures) ».
- L'originalité n'est qu'une note de grille des juges, en trois niveaux : « inedite », « transposition », « occupee » (ligne 183).

#### 1.14 `orchestrator/prereg/preenregistrement-tour-ferme-v1-brouillon6.md` (3 novembre 2026 ; brouillon non scellé) — `cdcb44706e7b3c62`
- C'est la seule pièce qui pose « vrais proposeurs contre hasard » comme hypothèse chiffrée. Lignes 184-185 : « **H-A4-2 (la chaîne distingue le bras réel du hasard)** : le bras réel produit plus de cartes promues puis survivantes, et plus de vraies découvertes, que le bras aléatoire. »
- Le monde est facile pour le hasard. Ligne 118 : « **13 % des lois aléatoires de la grammaire portent G ≥ 0,02** (159 sur 1 200) ».
- Le texte définit la nouveauté à l'oracle, comme le gain d'information au-delà de l'archive (ΔG). Ligne 121 : « monde (G) **et** nouveauté par rapport à l'archive (ΔG) ».
- Lecture gelée de l'échec, lignes 261-262 : « la chaîne ne distingue pas les vrais proposeurs du hasard dans ce monde : réserve majeure ».
- Ligne 555 : « **Hors portée** : proposeurs de la famille Claude ; bisociateur ; moisson ; juges d'idéation croisés ».

#### 1.15 `orchestrator/prereg/rapport-redaction-tour-ferme-v6.md` (3 novembre 2026) — `c2d6765a5993f66f`
- Seules ont tourné des courses à blanc, avec un bac factice et des doublures scriptées, sans modèle. L'issue « discrimine » y était attendue par construction.
- Ligne 161 : « **« tient », A4 « discrimine »** […] aléatoire [36, 0, 0] ». Ligne 163 : « S1 déclenché (doublures voisines de L*, attendu à blanc) ».

#### 1.16 `orchestrator/prereg/preenregistrement-boucle-reelle-organisme-v1-v2.md` (texte de la course v67) — `80fe4f03b4905b23`
- La course réelle a été jouée **sans bras aléatoire**. Ligne 235 : « un seul bras (réel) au lieu de trois ; une génération et demie au lieu de trois ».

#### 1.17 `resultats/course-v67/verdict-course-v67-v1.md` (12 novembre 2026) — `d79024328157aafc`
- Ligne 3 : « C1 « la chaîne garde (classe couverte, ce monde, cette taille) » […] ni sur la qualité des idées ».
- Ligne 162 : « Ces 11 lois sont des variantes proches (trois lois de Kimi partagent la même base) : ce ne sont pas 11 idées ».
- Lignes 190-191 : « le compte ne dit rien de la qualité ni de la diversité des idées ».
- Lignes 216-217 : « elle établit l'absence de défaut de plomberie observé à cette taille, pas une performance. »

#### 1.18 `resultats/attaque-goodhart-v2/README.md` (verdicts des 5 et 10 novembre 2026) — `88c97bad8495d0c3`
- Ligne 127, sur le tour fermé : « **It is not sealed and has not been run** ». Le bras aléatoire contre de vrais proposeurs n'a donc pas été joué.

#### 1.19 `orchestrator/prereg/preenregistrement-juges-idees-v2-brouillon3.md` (brouillon 3, non scellé) — `2680cf6a5c7f080d`
- La nouveauté est éprouvée par des témoins « redites » vraies. Ligne 90 : « ≥ 0,5 : la nouveauté n'est pas vérifiée (classe difficile : la redite est **vraie**) ».
- C'est un instrument de juge, et non une méthode d'exploration.

### 2. Joué contre conçu

| Pièce | Statut | Résultat tel qu'écrit |
|---|---|---|
| Tirage déterminantal contre stratifié (ponts plantés) | joué sur processeur | « la forme corrigée perd de 4,8 et 2,2 points contre lui » (`recombinaison.py`, l. 10-11) |
| Couche 1 avec proposeur : aveugle contre exploration | joué sur processeur, reproduit le 1er novembre | « the hoped-for advantage of exploratory proposers did not show (1 promoted card in each arm) » (`README.md`, l. 129) |
| Batterie des proposeurs, v1 (aléatoire, mécanique, scripté) | joué sur processeur ; résultat seulement cité | « ses 23 sur 35 de la v1 » pour le mécanique (`demo_proposeurs_v7.py`, l. 31) ; aucun fichier de résultat |
| Premier tour d'idéation réel (Claude, Argon) | joué en réel | « 17 distinct ideas (12 duplicate pairs) » (`README.md`, l. 135) |
| Second tour réel (Kimi, Argon), sans bisociateur | joué en réel | « The two LLM judges sat at their ceiling » (`README.md`, l. 136) |
| Boucle réelle v66, deux tentatives | jouée en réel, arrêtée | « Issue C5 : « non jugeable (arrêt) » » (`resultats/boucle-reelle-v66/README.md`, l. 5) |
| Boucle réelle v67, un seul bras réel | jouée en réel, verdict scellé | C1 ; « ce ne sont pas 11 idées » (verdict, l. 3 et 162) |
| Attaque de Goodhart (W2, puis W2 gradué) | jouée en réel, verdicts | « 42 of the 48 reproduce the world's own law exactly » ; sous v9, au bord déclaré : « frontier crossed, robust » (`README.md`, l. 140) |
| Tour fermé, avec bras aléatoire contre vrais proposeurs | à blanc seulement (doublures) | « It is not sealed and has not been run » (`attaque-goodhart-v2/README.md`, l. 127) |
| Duel des proposeurs payé (Opus contre références) | conçu, code et répétition sans dépense | aucun résultat trouvé |
| Marchepieds, monde fécond contre plat | conçu et codé, démonstration écrite | aucun résultat versé |
| Stratégie « hors des bassins déjà promus » | codée, essayée en simulation (`test_v7_proposeur.py`, l. 104) | aucune mesure de promues par stratégie trouvée |
| Bisociateur à trois bras | codé (v53 à v55) | hors portée du tour fermé (l. 555) ; second tour joué sans lui |
| Moissonneur | codé avec un relais factice | « rien de réel ici » (`moisson.py`, l. 5) |
| Stratégies d'allocation (« loi mère », champ moyen de Thouless-Anderson-Palmer) | hypothèses non codées | `proposeur.py`, l. 21 |

### 3. Ce qui n'a jamais été éprouvé (dans ce dépôt)

- La comparaison de vrais proposeurs au bras aléatoire et au bras qui recopie ou mélange (hypothèse H-A4-2 du tour fermé) : texte non scellé, aucune course réelle.
- Le duel d'un proposeur à modèle contre le chercheur mécanique et l'aléatoire, hors de l'espace du mécanique (grammaire v2).
- Le rendement de chaque stratégie du catalogue, en particulier « hors_bassins_promus » et « au_dela_du_connu », avec un vrai modèle.
- Les marchepieds sur une lignée réelle. Leur prémisse, la fécondité des lignées, n'existe que dans le monde simulé (`simulation.py`, l. 10-12).
- Le bisociateur en course réelle : ni ses trois bras, ni son bras méta, qui exige une annexe scellée.
- La moisson réelle et la vérification d'antériorité qu'elle permettrait.
- Les stratégies d'allocation de Gemini.
- La diversité ou la qualité des idées d'une course réelle (verdict v67, l. 190-191).
- Le protocole des juges d'idées par paires (version 2), dont le texte est resté au brouillon 3.

### 4. Recoupements et écarts avec la page de controle-ia-travail

- **Recoupe** (§ 1.1 et tableau 2 de la page : « noyau d'origine mort ») : `recombinaison.py`, l. 10-11, donne la perte chiffrée du tirage déterminantal et le passage au stratifié (R-527).
- **Recoupe** (§ 1.6 : « aucune récompense numérique de la nouveauté […] servie à un agent ») : `ideation.py`, l. 92-93, et `proposeur.py`, l. 7 (« jamais la richesse »).
- **Recoupe et antécédent** (§ 1.7 : la liste des paires de traits que l'archive ne croise pas) : la stratégie « hors des bassins déjà promus » en est une forme plus ancienne, accordée par Lazar le 27 octobre (`proposeur.py`, l. 3-4 et 40).
  - Elle sert un couple (moniteur, trait) non couvert.
  - En simulation, elle est jouée par un tirage uniforme parmi les couples libres (`simulation.py`, l. 410-414).
  - L'« inconnue centrale » de la page, l'effet de la vue sur la loi des propositions, reste entière : aucune mesure par stratégie n'a été trouvée.
- **Recoupe** (tableau 2 de la page, marchepieds : « utile seulement avec parents détectables ») : `recombinaison.py`, l. 18-19, et la démonstration à deux faces (`demo_cycle_v5.py`, l. 14-18).
- **Recoupe** (verdict de la page, point 2 : le tirage au hasard ou l'énumérateur sans modèle comme base) : ce dépôt avait déjà posé l'aléatoire et le mécanique comme barres qui font « tomber » les prises « proposeur » et « exploration » (`proposeurs_references.py`, l. 8 et 12). Le seul résultat, sur processeur, ne montre pas d'avantage de l'exploration (`README.md`, l. 129).
- **Recoupe** (§ 1.6 : la pression vers la variété pousse vers `si_sinon` et `melange`, classe que le nul ne couvre pas) : le verdict v67, l. 210-211, note que des cartes réelles retenues ont la forme `si_sinon` ou `par_sous_population`. Le résultat C1 ne garantit rien sur ces formes.
- **Recoupe** (§ 1.12 : « Aucune intervention n'a d'indice direct sur des idées vérifiées ») : verdict v67, l. 3 et 190-191.
- **Nuance** : la page demande partout une base au hasard, mais le bisociateur de ce dépôt est écrit sans bras au hasard (`bisociateur_v53.py`, l. 3). Ses trois bras ne sont donc comparés à aucun tirage indépendant. Ce n'est pas une contradiction de conclusion, mais un trou de dessin.
- **Ajouts absents de la page** :
  - le moissonneur de nouveauté (métadonnées, touches non opposables) ;
  - les stratégies d'allocation « loi mère » et champ moyen, non codées ;
  - la définition de la vraie découverte à l'oracle, information et nouveauté contre l'archive (ΔG ≥ 0,02 nat, tour fermé, l. 110-121) ;
  - la redite exacte de la loi du monde par un proposeur à modèle dans l'attaque de Goodhart (`README.md`, l. 140).
- **Contradiction** : aucune trouvée.

### 5. Non trouvé

- **Aucun remue-méninges explicite sur les méthodes qui battent la marche au hasard.** J'ai cherché « marche au hasard », « random walk », « puits », « bassin » au sens des idées, « allum », « masse manquante », « Good-Turing », « qualité-diversité », « nouveauté » comme récompense. Je n'ai trouvé que :
  - la stratégie « hors_bassins_promus » ;
  - les marchepieds ;
  - « bassin » au sens d'un groupe de processus (`essais/test_lecture_epreuve_w2g_dose_v1.py`, homonyme écarté).
- Aucune pièce sur l'« allumage » d'une idée ou d'un champ, ni sur la transition de phase, la fertilité d'une paire ou l'autocatalyse.
- Aucun fichier de résultat pour la batterie des proposeurs (v1 et v2), pour la démonstration des marchepieds (B1, B2), pour le duel des proposeurs ou pour une moisson réelle.
- Aucune version scellée du tour fermé ni des juges d'idées v2 : seuls les brouillons et les contre-lectures sont présents.
- Aucune trace de l'organisme sur les bassins étroits (13 novembre, page § 1.7) dans ce clone, en dehors de son usage comme orchestrateur figé, que la page rapporte.

### 6. Chemins non ouverts à cause du cloisonnement

- `orchestrator/essais/mutations_v57b.py` et `.sha256`, `orchestrator/essais/test_v57b_cablage_verdict.py` et `.sha256` (motif « 7b »).
- `orchestrator/essais/test_v7_monde_banque_scores.py` et `orchestrator/pole/monde_banque_scores.py` (motif « score »).
- `resultats/controle-p3-premier-test/README.md` (dossier interdit).
- Non ouverts par prudence, hors du sujet : tout `resultats/controle-r1-blanche-noire/` et tout `resultats/controle-simulation-defenses/` (résultats du programme de contrôle).
- Lignes du `README.md` sur le programme de contrôle (l. 137 à 139) : apparues dans une sortie de recherche, ni lues pour ce brouillon ni rapportées.
- Ouverts mais hors sujet, et rien n'en est rapporté : le préenregistrement de lecture de la banque T0.5 avec graines neuves (`preenregistrement-lecture-t05-graines-neuves-v2.md`, en-tête et recherche par mots seulement).
