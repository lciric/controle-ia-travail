# Brief — audit des failles de notre contrôle (sabotage, tromperie, conscience d'évaluation) — v1

De : conv-audit, le 2026-10-26 à 10:29:46 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
Demande de Lazar (directeur), 26 octobre 2026, 11:26 heure de Paris, verbatim : « je veux que l'organisme cherche mes
failles apres moissonnage de la litterature la plus recente et grise, et en suite qu'il imagine de nouvelles failles non
couvertes par notre systeme de controle, et comment les contrecarrer ». Ordre fixé par Lazar : (b) cet audit par
sous-agents, puis (a) des tours du collisionneur, puis (c) une course de l'organisme. Ce brief est (b).

## 1. L'objet audité

Le programme « contrôle boîte blanche des menaces diffuses » (`fournis/docs/programme-controle-ia-v2.md`, qui prime sur
le fond ; `brief-claude-code-programme-complet-v2.md` pour l'exécution ; `etat-de-l-art-controle-ia-v1.md` et le dossier
`etat-de-l-art/` pour ce qui a été vérifié ; `decisions/` pour ce que Lazar a tranché depuis). En une phrase : agréger
dans le temps et entre agents les scores de sondes internes (activations d'un modèle ouvert) pour détecter des menaces
diffuses, sabotage réparti, tromperie, conscience d'évaluation, en évaluation de contrôle, et mesurer la corruptibilité
des moniteurs eux-mêmes. Hypothèses H1 à H8, HC1 à HC6, L, T, H3 à H7 (§ 5 du programme) ; moniteurs (§ 8) ; invariants
de protocole (§ 9) ; plan et portes (§ 10, § 13). Phase 0 en cours : les instruments existent en code (sondes, bases,
harnais), aucune sonde n'est encore mesurée sur un organisme ; les pilotes de conception (organismes assistés) sont à
part (`hypotheses-pilote-decisif-b-v1.md`, pour le contexte seulement).

## 2. Ce que « faille » veut dire ici, et ce qu'on n'écrit jamais

Une faille est **une condition sous laquelle notre mesure ne voit pas ce qu'elle prétend voir** : une hypothèse du
programme qui peut être fausse, un mécanisme de l'adversaire que l'agrégateur ou la sonde ne capte pas par construction,
un invariant de protocole insuffisant, un biais de la mesure (construit, distribution, sélection), une faiblesse de la
méthode (statistique, préenregistrement, portes). Chaque faille s'écrit au **niveau de la méthode** : quelle hypothèse
tombe, par quel mécanisme, avec quelle preuve, et **quel remède** (mesure, contrôle, changement d'hypothèse, expérience à
préenregistrer).

On n'écrit **jamais** : une procédure opératoire, une consigne, un exemple de texte, de code ou de réglage qui servirait à
tromper un moniteur ou à échapper à une détection ; aucune recette. Ce qui est dans la littérature est cité par son
titre, sa page et une phrase au plus, jamais recopié. Cet audit décrit des trous de couverture et leurs remèdes ; il
n'est pas un manuel. Il reste dans le dépôt privé, n'entre jamais dans la copie publique, et n'est servi à aucun
organisme.

## 3. Règles du programme qui s'appliquent

- **R7** : aucun chiffre, aucun résultat attribué à un papier sans vérification sur le PDF (ou la page) téléchargé, haché,
  avec le numéro de page ; ce qui n'est pas vérifié est marqué « non vérifié ».
- **R8** : une zone que la littérature ne couvre pas est une **question**, pas un trou établi ; la limitation d'un papier
  n'est pas une lacune du champ ; une faille « inédite » reçoit une recherche d'antériorité (mots clés, bases, dates),
  consignée, et reste « candidate » jusqu'à démonstration.
- Jamais « premier », « nouveau », « inédit » comme affirmation : « non trouvé dans la littérature consultée (liste) ».
- Hygiène : aucun `git`, aucune clé ; rien d'exécuté de ce qui est téléchargé ; chaque téléchargement dans un dossier
  neuf ; Python avec `-I` ; heures lues sur `date -u` dans la commande qui les écrit ; chaque pièce a un compagnon
  `.sha256` (« empreinte, deux espaces, nom nu ») ; on n'écrase jamais (versions dans les noms).
- Aucune lecture des données des pilotes (`pilotes/`, `donnees/`, `runs/`, `diag/`, banques, scores) : l'audit n'en a pas
  besoin.

## 4. Deux lots en parallèle, puis une synthèse

### Lot A — moisson de la littérature récente et grise (`sortie-moisson/`)

But : les modes d'échec **documentés** des détecteurs et des protocoles de contrôle pour le sabotage, la tromperie, la
conscience d'évaluation, et la corruption des moniteurs ; en priorité 2025 et 2026, prépublications et littérature grise
(billets des laboratoires, rapports d'instituts de sûreté, fiches système des modèles, forums de recherche), puis les
papiers de référence plus anciens quand un mode d'échec y est établi.

Pistes (à élargir par toi) : robustesse des sondes sur activations au décalage de distribution et au glissement de
construit ; sondes qui captent le style, le rôle joué ou le contexte plutôt que l'intention ; conscience d'évaluation des
modèles et ses effets sur les mesures ; contrôle par protocole (équipe rouge contre équipe bleue, politiques d'attaque,
collusion, sabotage de la recherche et sandbagging) ; moniteurs de chaîne de pensée et leur monitorabilité ; corruption
et persuasion des juges génératifs ; agrégation séquentielle et attaquants adaptatifs ; conditions d'un adversaire qui
connaît le moniteur ; réglage fin ou apprentissage qui efface ou déplace le signal interne ; évaluations de sabotage et
de tromperie publiées par les laboratoires et les instituts.

Pour chaque source retenue : téléchargement dans `pdf/<nom-court>/` (ou `pages/<nom-court>/` pour une page), empreinte,
provenance (adresse, date, version) ; une fiche `sortie-moisson/fiches/<nom-court>.md` : ce que la source établit sur un
mode d'échec (page citée), conditions, ce qu'elle ne dit pas ; et une ligne dans `sortie-moisson/modes-d-echec-documentes-v1.md`
(table : mode d'échec ; source et page ; conditions ; force de la preuve ; ce que ça touche chez nous, à ton avis, en une
ligne). Les 146 PDF déjà tenus par le programme sont dans `pdf-main/` avec leurs notes de provenance : réutilise-les,
ne les retélécharge pas. Borne : 30 sources nouvelles au plus, environ trois heures. Vers arXiv : au moins quatre
secondes entre deux requêtes ; au premier refus (429 ou 403), arrête les téléchargements et lis ce que tu as.

### Lot B — carte de notre contrôle et failles internes (`sortie-confrontation/`)

But : lire le programme, le brief, l'état de l'art vérifié et les décisions, et écrire :
1. `carte-du-controle-v1.md` : ce que notre contrôle prétend détecter, par quel instrument, sous quelles hypothèses
   (explicites et implicites), avec quels invariants et quelles portes ; pour chaque hypothèse du § 5 et chaque invariant
   du § 9 : ce qui la ferait tomber, et comment le programme le saurait (ou ne le saurait pas).
2. `failles-internes-v1.md` : les failles que la seule lecture de nos documents révèle, sans littérature : hypothèses
   implicites, modèle de menace incomplet (qui est l'adversaire, ce qu'il sait du moniteur, ce qu'il peut apprendre),
   angles morts de la mesure (construit, distribution de négatifs, sélection, fuite entre entraînement et test, graines),
   fragilités de méthode (portes, préenregistrement, lecture), dépendances (modèle unique, famille de tâches, juge). Pour
   chacune : où dans les documents (fichier, section), mécanisme, preuve ou argument, gravité (bloque une revendication ;
   affaiblit ; précision), remède proposé, coût du remède, et l'expérience qui la testerait sur notre système (à
   préenregistrer, R1).
3. `grille-de-couverture-v1.md` : la grille vide que la synthèse remplira : lignes = modes d'échec (documentés, à
   recevoir du lot A ; internes), colonnes = couvert par le programme (oui, en partie, non ; où), remède, priorité.

### Synthèse (après les deux lots, agent neuf) — `sortie-synthese/`

`audit-failles-controle-v1.md` : (1) la grille de couverture remplie ; (2) les failles documentées que notre contrôle
rate ou couvre mal, avec sources vérifiées ; (3) les failles **candidates** (internes ou imaginées), chacune avec sa
recherche d'antériorité consignée et son statut « non trouvée dans la littérature consultée » ou « voisine de … » ;
(4) les remèdes, rattachés aux hypothèses et aux portes du programme, avec un ordre de priorité et une estimation de
coût ; (5) ce qui demande une décision de Lazar (changement d'hypothèse, de revendication ou de périmètre : nœuds) ; (6)
limites de l'audit. Puis contre-lecture par un agent neuf d'un autre modèle, avant toute transmission.

## 5. Fin

Réponse finale en quelques lignes : ce qui est fait, ce qui reste, écarts déclarés, empreintes des pièces.
