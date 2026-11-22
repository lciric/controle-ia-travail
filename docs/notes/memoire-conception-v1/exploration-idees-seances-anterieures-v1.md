# Séances antérieures sur l'exploration des idées rares et sur ce qui « allume » une idée — v1

- Pièce de travail (classe C), écrite le 22 novembre 2026 par un agent de lecture (Claude Opus 5.5) de la bibliothécaire, branche `claude/bibliothecaire-v1` (tête `8dd7668d`, à jour de `main` `bec207aa`). Lecture seule ; aucun modèle externe, aucune dépense.
- Question du directeur, verbatim : « il me semble qu'on avait déjà sur le dépôt organisme idéation fait des brainstorms similaires, quelles étaient les conclusions ? »
- Cloisonnement : liste d'autorisation v3 de la bibliothécaire, plus les ajouts accordés pour cette seule question. Rien lu sous `prereg/`, `diag/`, `runs/`, ni d'une autre branche. Les citations sont exactes, au plus 25 mots ; le gras des sources est retiré.
- **Le dépôt public `lciric/ideation-organism` n'a pas été lu** : l'attacher à la session de la bibliothécaire a été refusé par le contrôle de permissions (« Unauthorized Access », 22 novembre vers 14:05Z) ; la bibliothécaire ne l'a pas contourné par un clone à la main ; le refus est porté à Lazar par la mère. Cette page ne rapporte que ce que `controle-ia-travail` en dit (section « non trouvé et hors périmètre »).
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
- Dépôt public `lciric/ideation-organism` : non accessible ici, non cloné. Ce dépôt-ci en rapporte seulement :
  - sa création publique par le directeur, avec orchestrateur, conception, README et manifeste (R-989) ;
  - des préenregistrements de l'attaque de Goodhart et des contre-lectures poussés sur `claude/new-session-7qxayx` (R-1543, R-1563, R-1715) ;
  - des mises à jour de la page publique (R-1771 ; versions 2 à 4 du 13 novembre, R-2583 à R-2594) ;
  - son usage comme orchestrateur figé de l'organisme sur les bassins étroits (clone au commit `be6b5af9`).
- Aucune séance de remue-méninges sur l'exploration n'y est inventoriée dans ce que j'ai lu. Le mandat en demande la lecture : elle reste à faire par une session qui y a accès.
