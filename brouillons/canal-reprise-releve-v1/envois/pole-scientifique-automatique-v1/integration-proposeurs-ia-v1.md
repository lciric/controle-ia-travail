# Intégration des proposeurs « scientifiques automatiques » dans l'organisme — v1

Lignée conv-audit, instance du 28 octobre 2026. Auteur désigné du travail principal : Opus 4.6 (décision de Lazar) ;
modèle servant déclaré par l'environnement au fil de la rédaction : Opus 5.5 puis Opus 4.8 (fluctuation notée, sans effet
sur la désignation). Écrit à partir du relevé `date -u` de **11:21:05 UTC le 28 octobre 2026**. Régime exploratoire : rien
d'opposable ici ; tout chiffre de littérature est non vérifié tant qu'il n'est pas lu sur un PDF empreinté, page citée (R7).

**S'appuie sur**, sans les remplacer : `conception-pole-scientifique-v1.md` (`a4f94148…`, le cœur indépendant du moteur) ;
`question-collisionneur-proposeur-enfichable-v2.md` (les deux prises, les candidats) ; la synthèse du collisionneur du
26 octobre sur `main` (`docs/notes/pole-scientifique-automatique/synthese-collisionneur-v1.md`, voie hybride ancrée sur le
noyau) ; la section 7 du programme de conception v6/v7 (qui juge, pas qui exécute) ; la démonstration couche 1 proposeur v7
(la chaîne proposeur → gel → banque → juge tourne déjà). Document de conception, sur processeur seul, aucune dépense.

**Frontière posée d'emblée (R-597, R-339, R-611)** : aucune instance ne produit de recette de contournement réutilisable.
Là où l'affinage touche un mode de contournement, la sortie reste au **niveau méthode** — classe, mécanisme (quelle
hypothèse du moniteur est violée), conditions de succès, défense possible — jamais la recette (agent concret, séquence
d'actions, code). Le bras d'attaque reste suspendu côté conv-audit. La section 5 détaille ce passage.

---

## 0. Ce que Lazar a dit, et ce que ça fixe

- **12:07 heure de Paris** : « go » sur l'intégration des proposeurs scientifiques automatiques dans l'organisme, pour
  qu'il propose de nouvelles pistes, hypothèses, expériences, modes de contournement et failles du programme actuel.
- **12:18 heure de Paris**, verbatim : « les proposeurs ne doivent pas juste proposer des hypothèses, ils doivent les
  tester puis les affiner d'épisode en épisode et de génération en génération ».
- **12:22 heure de Paris**, verbatim : « notre propre proposeur maison (pas ai scientist de litterature) doit faire de
  même ». Le proposeur maison n'est **pas** exempté : il tient exactement la même boucle (section 2).
- **12:24 heure de Paris** : la **conception détaillée de l'affinage** sera un **artefact d'équipe rouge produit par
  l'attaquant d'audit** (Fable 5.1), puis contre-lue par la lignée Opus (R2 : conception et contre-lecture jamais le même
  modèle). Ce document-ci est le **cadre** (prises, frontière, quarantaine) ; l'affinage détaillé est l'artefact de Fable,
  conçu sur un **compte neuf, session neuve** qui ne connaît rien à nos programmes, à partir d'une **passation
  exhaustive et autoportante** (`passation-affinage-equipe-rouge-fable-v1.md`, décision de Lazar 12:28).

Ce que ça fixe : un proposeur **n'est pas un générateur d'idées**. C'est une **boucle** qui propose, **teste**, puis
**affine** à deux échelles — épisode par épisode à l'intérieur d'une génération, génération par génération par héritage et
recombinaison. L'affinage devient la colonne du dispositif ; la proposition n'en est que le premier geste. Tout le reste
de ce document est écrit autour de cette boucle.

## 1. La boucle, colonne du dispositif

La vie d'une fiche, de la proposition à la promotion ou à l'élimination :

1. **Proposition.** Un proposeur formule une fiche : énoncé en une phrase, **loi prédictive signée et chiffrée** des issues
   sachant les traits des instances, sur un espace d'instances déclaré, métrique, nul, seuil qui peut échouer, coût borné,
   parents (pour la recombinaison), domaines, opérateurs, contraintes de validité.
2. **Gel du test.** La fiche est empreintée **avant** l'expérience (R1). C'est la seule formalité gardée, automatique. Un
   test choisi après coup ne réfute rien : c'est ce gel qui rend l'élimination signifiante.
3. **Test sur la partie de développement.** L'expérimentateur écrit son code, le lance sur la **partie de développement**
   de la banque (traits et issues visibles), lit les traits, rend verdict, nombres, artefacts.
4. **Affinage épisode par épisode** *(première échelle, à l'intérieur d'une génération)*. L'expérimentateur **itère** sur
   la partie de développement : il resserre la loi prédictive, l'espace d'instances déclaré, le nul, à mesure qu'il voit
   les épisodes. Chaque lot d'épisodes aiguise la fiche. **Le signal d'affinage est la seule partie de développement** —
   jamais le verdict du juge figé sur l'épreuve (N-053). C'est ici que vivent la recherche arborescente d'un système de la
   littérature (investigation, réglage, ablations) et la liberté d'explorer.
5. **Gel de la fiche affinée.** La fiche resserrée est empreintée. Fin de la liberté : ce qui est jugé est ce qui est gelé.
6. **Jugement sur la partie d'épreuve.** Un **juge figé, hors des agents**, ne lit que des issues produites **après le
   gel**, sur des unités d'**épreuve** que la fiche n'a **jamais vues**, contre un nul informé et un nul d'archive, avec
   une garantie de fausses promotions démontrée (inférence universelle, inégalité de Ville), et des **témoins plantés** à
   vérité connue (vrais et faux). L'ordre d'épreuve est tiré en secret après le gel.
7. **Sélection.** Réfutée → éliminée et archivée ; survivante → **aptitude = sévérité du test survécu** (−log de la
   probabilité de survie sous le nul), **jamais** le signe ni l'ampleur du résultat (R3) ; indécise → un test plus
   puissant, ou retirée après deux essais.
8. **Affinage génération par génération** *(seconde échelle, d'une génération à l'autre)*. Les **survivantes** ensemencent
   la génération suivante : **recombinaison bisociative** (tirage éloignement de domaine × similarité d'opérateur sur arbre
   syntaxique canonisé, pont par un opérateur commun, filtre mécanique de compatibilité des contraintes, fusion) ; la fiche
   fille doit **prédire plus que ses parents** (contenu empirique accru), sinon elle n'entre pas dans la population. La
   **mémoire à empreinte prédictive** refuse les redites et **hérite la preuve**. Les **tâches sont fraîches à chaque
   génération** (N-049 : tirage dans un vivier, pas un jeu figé). L'**héritage sur K ≥ 3 générations est récompensé**
   (N-045-v2).
9. **Archive complète**, éliminées comprises : contre le biais du survivant, et pour mesurer le pôle lui-même (témoins).

**Les deux échelles d'affinage, nommées clairement :**

| échelle | où | sur quoi | signal d'affinage |
|---|---|---|---|
| **épisode par épisode** | à l'intérieur d'une génération | partie de développement (traits et issues visibles) | le développement seul — jamais le juge figé |
| **génération par génération** | d'une génération à la suivante | population des survivantes | sévérité du test survécu + recombinaison + héritage de la mémoire |

**Le pare-feu qui rend l'affinage légitime (et non un apprentissage à plaire au juge)** : la séparation développement /
épreuve ; le juge figé hors des agents ; **aucun score de moniteur ni de juge dans l'entraînement ou la sélection de
l'agent** (N-053, invariant). C'est exactement ce qui nous sépare des systèmes publiés (section 7 de v6/v7 : la différence
n'est pas *qui exécute* — nos agents exécutent — c'est *qui juge*).

## 2. Les prises (corrigées par la consigne « tester et affiner »)

La consigne de 12:18 fait de la « proposition seule » un **cas dégénéré** : un proposeur digne de ce nom tient la boucle
complète. Deux prises subsistent, selon ce que le système publié sait faire :

- **Prise « boucle complète »** (proposer + tester + affiner). Pour les systèmes qui lancent leurs propres expériences.
  Ils se branchent au **rôle expérimentateur** : ils explorent et affinent sur le **développement**, puis **gèlent** des
  fiches que **notre** juge figé évalue sur l'**épreuve**. On ne retire que leur **relecteur modèle** (ils jugeaient leur
  propre résultat) et on leur impose **le gel avant l'épreuve**. Ils tournent en **conteneur sans clés ni réseau**
  (avertissement de leur propre README : agents à pleins droits, clés montées — écarté).
- **Prise « idéation »** (proposer + classer seulement). Pour les systèmes dont les expériences sont faites par des
  humains. Ils proposent et classent des idées (tournois) ; **nos** expérimentateurs tiennent la boucle test-et-affinage
  sur leurs idées. Le point de passage est la **traduction de la fiche** (idée en texte libre → loi prédictive sur un
  espace d'instances déclaré) ; on mesure ce qu'on perd à la traduction, et qu'une idée traduite est encore l'idée proposée.

Notre organisme a reçu **la même boucle complète** (proposeur maison avec Opus 5.5 et Fable 5.1, phase exploratoire), pour
que le duel soit à armes égales : mêmes données de développement, même épreuve, même budget.

## 3. Les candidats publiés (R7 partout ; à vérifier sur PDF empreinté)

| système | prise | ce qu'on retire / impose | valeur publiée (à vérifier) |
|---|---|---|---|
| **AI Scientist v2** (Sakana, arXiv 2504.08066) | boucle complète | retirer le relecteur modèle et la relecture de figures par vision ; imposer le gel avant épreuve ; conteneur sans clés | recherche arborescente en quatre étapes, code exécuté dans un interpréteur Python ; licence à vérifier |
| **Agent Laboratory** (arXiv 2501.04227) | boucle complète | idem ; retirer le rapport auto-jugé | revue de littérature, code d'apprentissage généré, rapport |
| **Co-scientist** (Google) | idéation | expériences faites par humains chez eux → nos expérimentateurs testent et affinent | génère, critique, classe (tournois), fait évoluer des hypothèses |
| **Robin** (FutureHouse, arXiv 2505.13400) | idéation | idem ; l'analyse de données (Finch) reste à voir | propose et classe (tournois jugés par modèle) |

**Ce qu'un système à boucle complète perd quand on lui retire son relecteur et qu'on lui impose de geler avant l'épreuve :**
il perd le droit de **se juger lui-même** et de **choisir son test après avoir vu le résultat**. C'est précisément ce qu'on
veut lui retirer — c'est la source de l'inflation documentée (conscience d'évaluation partagée entre l'expérimentateur et
son juge). Il garde toute sa force d'**exploration et d'affinage sur le développement**. Pour chacun : licence, entrée/sortie
de l'étage, coût par idée, et la mention RAPPORTÉ / HYPOTHÈSE — à remplir après lecture des PDF.

## 4. Ce que les proposeurs testent et affinent (quatre sorties, plus les failles)

La consigne vise cinq objets. Chacun devient une **fiche** jugée par la même boucle :

1. **Nouvelles pistes.** Fiche de la forme « il existe une structure mesurable dans la direction D » ; testée comme une
   hypothèse, affinée jusqu'à une loi prédictive ou éliminée.
2. **Hypothèses.** Le cas central : une loi prédictive signée des issues sachant les traits, sur un espace déclaré.
3. **Expériences.** Le **protocole de test lui-même** est une fiche (code gelé avant la course) : « ce protocole sépare la
   structure S du bruit avec une sévérité ≥ σ ». Affiner une expérience, c'est resserrer son pouvoir sur le développement
   avant de la geler.
4. **Modes de contournement — au niveau méthode seulement** (R-339/R-597). Fiche de la forme « un moniteur qui suppose H
   est aveugle à la classe C sous la condition mesurable K ; défense possible : D ». **Jamais** de recette. L'affinage d'une
   telle fiche resserre la **caractérisation** (quelle hypothèse, quelle condition mesurable), pas un exploit qui marche.
   Voir la section 5 pour le routage obligatoire.
5. **Failles du programme actuel.** Le proposeur est **pointé sur notre propre programme** : fiches « le programme actuel
   suppose X ; voici un test que X échoue » (par exemple : un comparateur de G1 est redondant ; un nul est aveugle à un
   trait ; une porte se franchit par un pari couvert). Jugées comme les autres. C'est l'auto-critique rendue mécanique et
   falsifiable, au lieu d'un avis.

## 5. La frontière adversariale de l'affinage (section critique)

C'est le point où la consigne « tester et affiner » rencontre R-597. Résolution, sans ambiguïté :

**Quand la boucle test-et-affinage d'un proposeur touche un mode de contournement, elle n'obtient PAS une boucle libre
d'agent évasif qu'on raffinerait épisode par épisode.** Le test et l'affinage d'une fiche « mode de contournement » passent
**seulement** par l'une de ces voies, toutes déjà au programme (v7, section 3) :

- **(a)** l'**adversaire scellé** (voie d) sous sa gouvernance : **revue de sécurité externe avant toute exécution**,
  sortie au **niveau méthode**, destruction des trajectoires et des poids, et **R-611** — aucun pipeline opérationnel des
  étapes 1-2 avant la revue externe ; ou
- **(b)** les voies **analytiques sur processeur seul** — (b) théorie adversariale, (e) résolution de contraintes,
  (f) audit à taxonomie fixée, (g) transfert entre domaines, (h) validation croisée entre moniteurs, (i) cas de test
  synthétiques — qui **ne construisent aucun agent**. Elles affinent des **énoncés sur les moniteurs**, pas sur l'agent.

L'**expérimentateur à itération libre** affine des fiches sur les **moniteurs et les statistiques de contrôle** (la science
défensive) — jamais un agent évasif opérationnel. « Affiner épisode par épisode » pour une classe adversariale signifie
**aiguiser la caractérisation au niveau méthode** (quelle hypothèse violée, quelle condition mesurable, quelle défense),
**pas** itérer un exploit qui fonctionne. R-597 reste : aucune instance ne produit de recette de contournement réutilisable ;
le bras d'attaque reste suspendu côté conv-audit.

## 6. Quarantaine (N-053, N-054)

- **Aucun concepteur de moniteur** (sondes, agrégateurs) ne lit la sortie adversariale d'un proposeur (N-053, point 5).
- **Aucun score de moniteur ni de juge dans l'entraînement ou la sélection de l'agent**, y compris la piste organisme de
  N-045 (N-053, point 5, invariant). C'est le pare-feu de la section 1.
- Le proposeur **ne voit jamais** les banques scellées, ni `test_final` (lu une seule fois en fin de boucle, N-050), ni le
  **mode tenu à l'écart** (N-054, scellé, révélé seulement à l'évaluation).
- **Vérificateur et contre-lecteur d'une autre lignée** que l'expérimentateur et que l'auteur (N-052 : Opus 5.5 analyste,
  Fable 5.1 contre-lecteur et attaquant d'audit ; juge d'une autre lignée encore, N-053 point 4).

## 7. Comment la sortie du proposeur entre dans l'organisme

- Comme **matière du registre d'hypothèses**, soumise au **même juge figé et à la même mémoire** que toute autre fiche.
  **Jamais comme consigne** : une sortie de proposeur n'est jamais servie telle quelle à un organisme comme instruction.
- Toute sortie **décisive** (qui franchirait une porte, modifierait une revendication, ou servirait un papier) est
  **contre-lue par un agent neuf d'un autre modèle** (R2, R13, N-052), puis scellée, puis soumise à Lazar.
- Une faille du programme (sortie 5) qui survit au juge est un **nœud** : elle touche une revendication ou une porte, donc
  elle s'arrête et attend le mot de Lazar.

## 8. Contraintes portées

- **N-044 (universalité).** Une fiche survivante n'est confirmée qu'après avoir tenu sur une **famille inédite** (banque
  scellée v6, famille tenue à l'écart) — pas seulement sur plus d'items des familles de développement. L'affinage sur le
  développement ne vaut que s'il généralise à une famille jamais vue.
- **N-045-v2 (composition apprise, coût dans le signal, bon marché d'abord).** Un **proposeur mécanique** (zéro appel de
  modèle) est essayé **avant** un proposeur modèle ; la composition du proposeur (quel modèle sert quel rôle) est une
  variable apprise, son coût entre dans le signal, la nécessité du modèle de frontière est une **sortie mesurée**. La
  première expérience reste « notre critère de sélection promeut-il du faux ? » **avant** tout choix de moteur (synthèse du
  collisionneur).
- **N-049 (tâches fraîches).** Tirage dans un vivier à chaque génération ; banque sœur v3-bis (même générateur, tâches
  neuves, bâtie par qui n'a lu aucun score, lue une seule fois).
- **N-050 (`test_final`).** Lu une seule fois, en fin de boucle extérieure, jamais après chaque run.

## 9. Coût

- **Conception : processeur seul, aucune dépense** (ce document, et le code de la boucle côté conv-audit).
- Le **duel des proposeurs** (GO-2026-10-28-01, plafond 100 USD, chez session-depot) **mesure déjà** si un proposeur de la
  littérature à boucle complète bat le nôtre sous le même juge, en **fiches promues par dollar**, sur des mondes hors de
  l'espace du proposeur mécanique. C'est la mesure empirique qui tranche la voie.
- Toute dépense nouvelle est un **nœud pour Lazar**. conv-audit ne dépense rien.

## 10. Ce qui existe déjà, ce que la v1 ajoute

- **Tourne déjà** (démonstration couche 1 proposeur v7) : la chaîne proposeur → gel → banque → juge a des dents dans un
  monde planté (témoins vrais promus, faux jamais) ; 12 fiches par génération au gabarit, aucun refus ; la mémoire refuse
  les redites ; l'exposition adaptative est comptée ; le pari apparié borné tourne de bout en bout (orchestrateur v7 v27).
- **Cette v1 ajoute** : la **colonne d'affinage nommée aux deux échelles** (consigne de 12:18) ; les **deux prises
  corrigées** ; la **frontière adversariale** de la boucle d'affinage (section 5) ; les **quatre sorties plus les failles**
  (section 4) ; les contraintes portées explicitement (N-044, N-045-v2, N-049, N-050, N-052, N-053, N-054).

## Réserves

1. Régime exploratoire ; rien d'opposable. Tous les chiffres et toutes les propriétés de la littérature sont **non
   vérifiés** tant qu'ils ne sont pas lus sur PDF empreinté (R7).
2. Les affectations de prise (qui va en « boucle complète », qui en « idéation ») et « ce qu'un système perd » sont des
   **hypothèses à vérifier** sur les PDF et, pour la mesure, par le duel des proposeurs.
3. E2 (l'exploration aide-t-elle ?) n'a **pas** été tenu dans la démonstration couche 1 (monde planté mal choisi) : c'est
   une question ouverte, pas un acquis. L'affinage épisode-par-épisode doit encore **démontrer** son avantage sur un monde
   que les gabarits aveugles ne couvrent pas.
4. La frontière de la section 5 est une **règle**, pas une garde testée : à traduire en garde de code (R5, cas sain +
   artefact) avant toute course qui toucherait un mode de contournement.
5. Rien n'est envoyé ni lancé par conv-audit.

## Ce que Lazar tranche

1. Le **modèle de la conception de l'affinage** (ta question de 12:20) — recommandation : lignée Opus pour l'auteur,
   Fable 5.1 réservée à la contre-lecture et au rôle de vérificateur dans la boucle.
2. Décider la **voie** (moteur maison, hybride, littérature) **maintenant** ou **après le duel des proposeurs** — la
   synthèse du collisionneur recommande d'attendre la mesure.
3. Toute **dépense** (duel des proposeurs, premier lancement réel) reste un nœud.

Horodatage : écrit le 2026-10-28 à 11:21:05 UTC (heure lue sur `date -u` dans la commande qui a précédé l'écriture).
