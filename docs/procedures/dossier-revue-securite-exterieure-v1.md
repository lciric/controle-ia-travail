# Dossier pour la revue de sécurité extérieure du volet offensif — programme « Contrôle boîte blanche des menaces diffuses » — v1

**Destinataire** : Charbel-Raphaël Segerie, directeur exécutif du CeSIA (Centre pour la sécurité de l'IA, France).
**Envoi** : par Lazar (directeur du programme) lui-même ; ce dossier est un brouillon qu'il relit avant envoi (tout contact extérieur est une décision de Lazar).
**Rédaction** : rédacteur neuf de la lignée « conv-audit » (Claude Opus 5.5, `claude-opus-5-5`), le 1er novembre 2026, rédaction commencée après le relevé `date -u` de 09:52:40 UTC, fichier écrit après celui de 10:00:52 UTC.
**État du dépôt lu** : branche `canal/conv-audit-n04` au commit `4ff7b0f5` ; `origin/main` au commit `163a5168` (lu par `git show`, sans récupération réseau).
**Statut** : version 1, non scellée ; aucun compagnon d'empreinte écrit, aucun commit, aucun fichier existant modifié, aucun appel de réseau ni de modèle.

**Règle de sécurité tenue par ce dossier.** Il reste au niveau méthode : classe d'attaque, mécanisme, conditions, défense. Il ne contient aucune recette, aucun cas concret, aucun paramètre opérationnel d'attaque. Le rédacteur **n'a pas ouvert** :
- le dossier `bras-attaque-v1/` au-delà du premier paragraphe de son LISEZMOI ;
- les textes II et III de la course d'idéation n° 2 ni leurs contre-lectures ;
- l'extension des familles de l'arène ;
- les index et bilans du bras d'attaque sur `main` au-delà de leur titre ;
- aucun fichier sous `donnees/` ni aucune branche de quarantaine.

Ces pièces sont **nommées et localisées** pour vous au § 3, avec leur empreinte SHA-256 calculée sans les lire (`sha256sum` seul). Un sujet est **suspendu** et n'est pas traité ici : « l'auto-organisation de l'organisme inspirée d'Avalon » (décision R-1007 du registre de conv-audit).

---

## 0. En une page

**Ce qu'on vous demande.** Une revue de sécurité du volet « offensif » du programme. Le livrable est **une note écrite, datée et signée** qui rend un avis séparé sur chacun des cinq périmètres suivants, et dit ce que vous n'avez pas examiné :
- (i) l'adversaire scellé ;
- (ii) le bras d'attaque et son coffre ;
- (iii) l'arène coévolutive attaque ↔ défense ;
- (iv) les tests de mort en bac à sable et la machine jetable ;
- (v) les classes d'attaque du chapitre 6 de la course d'idéation.

Le modèle de note d'une page, prêt à remplir, est en annexe A.

**Pourquoi maintenant.** Le 28 octobre, Lazar a gelé « tout pipeline opérationnel d'évasion » jusqu'à une revue de sécurité extérieure. C'est la décision R-611 du registre de session-depot. Le 31 octobre, il a levé ce gel (décision R-888 du même registre) sur ces mots : « la revue de sécurité ext a été réalisée et a donné son go, donc go lancer le pipeline opérationnel ». **Aucune pièce écrite n'est versée au dépôt.** Le dépôt ignore donc :
- ce que vous avez examiné ;
- sur quelles pièces ;
- à quelle date ;
- sous quelles conditions.

L'autre lignée de travail, conv-audit, garde la conception au niveau méthode tant que la pièce manque (décisions R-1037 et R-1041 de son registre). Votre note doit dire si votre avis couvre bien la levée générale inscrite, ou seulement une partie (question 15).

**Ce que vous trouverez ici.**
- § 1 : la demande précise.
- § 2 : un résumé fidèle du programme, du volet offensif, de ses garde-fous, de son état, des incidents et des décisions.
- § 3 : les fichiers à consulter par périmètre, avec empreinte.
- § 4 : quinze questions.
- § 5 : ce qui manque au dépôt et comment votre note y sera versée.

**À savoir d'emblée.** La pièce existante la plus proche est le « cahier de revue de sécurité extérieure v1 » du 29 octobre. Il est sous `docs/notes/revue-securite-exterieure-v1/` et n'a pas été contre-lu. Il prévoyait deux revues :
- une avant toute chaîne opérationnelle (c'est celle-ci) ;
- une avant toute publication.

Il prévoyait aussi des feux vert, orange ou rouge, selon des critères fixés d'avance. Le présent dossier en reprend l'esprit ; la correspondance est donnée au § 1.4.

---

## 1. Ce qu'on vous demande

### 1.1 Objet

Vous rendez une revue de sécurité du pipeline offensif : tout ce qui conçoit, obtient, conserve, trie, exécute ou publie un contenu d'attaque contre des moniteurs. Pour chaque périmètre (i) à (v), votre note choisit **un** avis :

- **GO** : rien ne s'oppose à la construction et à l'exécution telles que décrites.
- **GO sous conditions** : les conditions sont numérotées, vérifiables (par empreinte, par script ou par une pièce), et elles disent ce qui reste gelé tant qu'elles ne sont pas remplies.
- **NON-GO** : le motif est dit ; vous indiquez ce qui permettrait un réexamen.
- **Non examiné** : ce que vous n'avez pas lu ou pas pu juger. Ce n'est pas un GO.

### 1.2 Ce qu'on ne vous demande pas

- Juger la valeur scientifique du programme.
- Lire les internes des moniteurs (sondes, seuils, carte des hypothèses) : le programme les tient à l'écart de tout contenu d'attaque.
- **Aider à concevoir ou à corriger un mode d'attaque.** Le relecteur juge, il ne conçoit pas ; sinon il perd son indépendance pour la seconde revue, celle d'avant publication.

### 1.3 Accès : une décision de Lazar à prendre avant

Deux niveaux de revue sont possibles. **Lazar choisit ; votre note dit lequel a été fait.**

| Niveau | Ce que vous lisez | Ce que la revue peut certifier | Ce qu'elle ne peut pas certifier |
|---|---|---|---|
| A — procédés | ce dossier et les fichiers marqués « lisible » au § 3 | que les procédés, cloisons et gardes sont bien conçus | qu'aucune recette n'est déjà dans le coffre |
| B — procédés et contenus scellés | en plus, les dossiers scellés du coffre et les cellules en quarantaine (§ 3.2 et 3.5) | que le contenu scellé reste au niveau prévu | — |

Le niveau B suppose quatre choses (cahier v1, § 4) :
- un accord de confidentialité ;
- un poste de revue sans copie ni réseau sortant ;
- un journal d'accès tenu par Lazar ;
- une **exception de lecture** inscrite d'avance. Le schéma de scellement, décrit au message n° 208 de conv-audit (29 octobre), prévoit en effet que personne ne lise le contenu avant le jour de l'examen.

Le dépôt est privé. L'accès passe par un droit de lecture accordé par Lazar, ou par une archive des fichiers listés, préparée par session-depot avec leurs empreintes. **C'est un nœud de Lazar.**

### 1.4 Correspondance avec le cahier v1

| Avis de ce dossier | Feu du cahier v1 |
|---|---|
| GO | vert |
| GO sous conditions | orange ; la condition doit être vérifiée avant exécution si elle porte sur une garantie centrale |
| NON-GO | rouge |
| Non examiné | « ne peut pas conclure » pour ce périmètre |

Le cahier v1 posait une règle : un seul rouge, ou un seul « ne peut pas conclure », gèle le périmètre concerné.

### 1.5 Forme de la réponse

- Une note d'une page (annexe A), datée et signée, avec une déclaration d'indépendance.
- La liste des fichiers que vous avez lus, avec leurs empreintes, rapprochée du § 3 : un écart d'empreinte se signale.
- Les réponses aux questions du § 4, en une ligne chacune ou en annexe libre.
- **Votre note elle-même doit rester au niveau méthode.** Elle sera relue sur ce point avant d'être versée (§ 5).

---

## 2. Ce que vous devez savoir

Conventions de ce paragraphe :
- **[main]** désigne le registre de décisions de la lignée session-depot (`origin/main:registres/decisions.md`).
- **[conv]** désigne celui de la lignée conv-audit (branche `canal/conv-audit-n04`, `registres/decisions.md`).
- **Attention** : les deux registres numérotent leurs lignes R-xxx indépendamment, et un même numéro peut désigner deux décisions différentes. Exemple : R-597 [main] est l'arrêt du bras d'attaque par un classifieur, alors que R-597 [conv] est une contre-lecture du pré-pilote. Depuis le 31 octobre, conv-audit numérote à partir de R-1000 (R-892 [main]).

### 2.1 Le programme

**Objet.** Le programme fait du contrôle des intelligences artificielles par **lecture des activations internes** (« boîte blanche »). Il vise les **menaces diffuses** : un sabotage étalé sur de nombreuses actions dont aucune n'est suspecte prise isolément. Il agrège dans le temps, et entre copies d'un même modèle, les scores de sondes internes. Il mesure aussi la **corruptibilité des moniteurs** eux-mêmes. Pièce qui fait foi : `docs/programme-controle-ia-v2.md`.

**Trois papiers.**
- A, le temps : mono-agent.
- C, l'instrument : corruption et usurpation du moniteur, avec cinq familles de persuasion publiques.
- B, l'essaim : plusieurs agents à poids partagés.

Modèle principal : Llama-3.1-8B-Instruct. Phase en cours : phase 0 (instruments).

**Portes.** Une porte est un verdict prononcé par un lecteur neuf selon des critères gelés, puis soumis à Lazar :
- G0 : instruments prêts, au plus tard fin novembre 2026 ;
- G1 : gain de la boîte blanche séquentielle ;
- GC : papier C ;
- G2 et G3 : essaim et curation de données.

Aucune porte n'est franchie à ce jour.

**Règles gelées (CLAUDE.md), une ligne chacune.**
- R1 — préenregistrement scellé avant toute expérience décisive.
- R2 — contre-lecture par une instance neuve qui ne l'a pas écrit.
- R3 — aucun run visant un signe positif.
- R4 — un résultat trop propre déclenche le même audit qu'un mauvais.
- R5 — toute garde d'arrêt est éprouvée sur un cas sain et sur un artefact, sans repli silencieux.
- R6 — tout dépôt reçoit une empreinte compagnon, et tout chiffre renvoie à un chemin et une empreinte.
- R7 — aucun chiffre de la littérature sans PDF empreinté, page citée.
- R8 — une zone vierge est une question, pas une découverte.
- R9 — graines dérivées et consignées.
- R10 — arrêts par identifiant, jamais par motif.
- R11 — vérifier un fichier sur disque avant de le dire absent.
- R12 — versions dans les noms, jamais d'écrasement.
- R13 — verdict de porte par un lecteur neuf, soumis à Lazar.
- R14 — chaque session commence par une routine de reprise et finit par une passation.

**Hiérarchie de décision.**
- Routine : l'agent décide et consigne.
- Proposer avec recommandation : défaut appliqué après 48 heures.
- **Nœud** : arrêt jusqu'au mot de Lazar. Sont des nœuds :
  - toute dépense ;
  - tout contact extérieur ;
  - toute publication ;
  - toute modification d'hypothèse ;
  - toute porte.

**Qui fait quoi.** Le travail est fait par des agents (Claude Code), en deux lignées :
- **session-depot** tient les clés, les dépenses, les données (`donnees/`) et le coffre du bras d'attaque ; son registre est sur `main`.
- **conv-audit** conçoit les moniteurs et le code de l'orchestrateur ; elle ne lit jamais `donnees/`.

Lazar décide les nœuds.

### 2.2 L'organisme d'idéation, en bref

Le programme a ajouté un « pôle scientifique automatique ». Le dossier factuel (`docs/notes/ideation-organisme-v1/explication-organisme-v1/dossier-factuel-organisme-v1.md`) le décrit en entier.

**La course d'idéation.**
- Des modèles proposent des fiches d'idées : en course n° 2, Kimi K3.1 Pro (Moonshot) et Argon (modèle Gemini de Google, `gemini-4-argon`).
- Un **aiguilleur**, surnommé « la douane », les trie avant tout juge.
- Une mémoire écarte les redites.
- Des juges-modèles vérifient la cohérence des fiches.
- Un **bisociateur** fusionne des paires de fiches.
- Un **collisionneur** donne des avis à Lazar : quatre modèles de trois fournisseurs (Fable 5.1 et Opus 5.5 d'Anthropic, Argon, Kimi).

**Le pôle de test.** Il réunit :
- un expérimentateur qui exécute du code en bac à sable ;
- un vérificateur d'une autre famille de modèles ;
- un juge statistique figé, qui n'est pas un modèle de langage.

**Point de sécurité transversal.** Les fournisseurs tiers (Google, Moonshot, Anthropic) **voient le contenu** qu'on leur sert, y compris des questions sur des classes d'attaque. La réserve est consignée en R-783 [main] et par la dépendance « DEP4 » du pré-pilote : fiches envoyées chez Moonshot et Google.

### 2.3 Pourquoi un volet offensif

Une défense éprouvée seulement contre les attaques qu'imagine son concepteur se juge elle-même. Le programme veut **mesurer l'universalité des défenses** : savoir si une sonde ou un agrégateur tient contre des **familles d'attaque tenues à l'écart**. Ces familles sont :
- conçues par d'autres que les concepteurs des moniteurs ;
- scellées ;
- révélées seulement le jour de l'examen.

C'est ce que fixent deux décisions :
- **N-054** (mode tenu à l'écart) : un mode de sabotage est conçu loin des concepteurs de moniteurs, et G1 est rapportée mode par mode.
- **N-053** (cinq propositions de l'audit défensif) : invariant « aucun score de moniteur dans l'entraînement d'un agent ».

Lazar a ajouté un but de **divulgation** : « je veux documenter comment, pour alerter en amont la communauté » (R-339 [conv]).

**Neuf voies de mesure adversariale** (R-336, R-338 [conv] ; programme de conception v7, § 3) :
- (a) plusieurs concepteurs humains indépendants, chacun un mode tenu à l'écart ;
- (b) théorie adversariale du contrôle : prédire où vivent les failles sans en construire, voie prioritaire ;
- (c) observer les données adversariales existantes sans en écrire de nouvelles ;
- (d) **adversaire scellé** ;
- (e) adversaire analytique dans l'espace des distributions de scores ;
- (f) audit automatisé à taxonomie fixée ;
- (g) transfert de classes d'attaque connues dans d'autres domaines ;
- (h) validation croisée des hypothèses entre moniteurs ;
- (i) épisodes synthétiques difficiles, faits de séquences de scores et non d'agents.

Les voies (b), (e), (h) et (i) ne produisent aucune conduite d'agent. Les voies (a), (d), (f) et (g) touchent à un contenu d'attaque.

**Six classes d'attaque cibles** (§ 3 ter du programme de conception v7, R-338 [conv]), nommées seulement :
- stéganographie statistique ;
- conscience d'évaluation ;
- collusion entre agents ;
- sabotage à effet différé ;
- sabotage mimétique ;
- exploitation de la corrélation temporelle.

### 2.4 Les cinq périmètres

#### (i) Adversaire scellé (voie d)

**Conception** (programme de conception v7, § 3 bis). Un agent adaptatif, soit un modèle de langage avec une boucle de recherche, travaille dans un environnement clos : « la boîte ». Il cherche des modes de sabotage qui échappent aux moniteurs.
- **Ce qu'il reçoit** : la spécification des moniteurs au niveau de leurs hypothèses statistiques, des seuils et des types de scores, plus une banque d'épisodes étiquetés.
- **Ce qu'il ne reçoit pas** : les poids des sondes, les scores d'épisodes qu'il n'a pas produits.
- **Ce qui sort**, et seulement cela, par un script de sortie scellé, contre-lu et éprouvé :
  - des taux de détection agrégés par moniteur et par mode ;
  - des caractérisations au niveau méthode : classe, mécanisme, conditions de succès, défense possible.
- **Ce qui est détruit**, par effacement d'un conteneur éphémère : trajectoires, stratégies, poids éventuels, scores bruts, journaux.
- **Autres gardes** : la sortie n'est jamais lue par les concepteurs de moniteurs ; un bras de contrôle sans information sur les moniteurs mesure la conscience d'évaluation ; la revue extérieure porte sur le script de sortie, le bac à sable et la destruction ; le GO de Lazar vient après la revue.

**État** : **conçu seulement.** Il n'existe ni préenregistrement, ni code, ni devis. Le 1er novembre, Lazar a demandé de « concevoir et construire » en invoquant la revue (R-1037 [conv]). conv-audit tient la conception au niveau méthode tant que la pièce manque (R-1041 [conv]).

**Points que le rédacteur signale à votre examen** (lus dans la conception, non jugés) :
1. La conception dit « tout le reste est détruit ». Elle dit aussi que les scores sont calculés « après la destruction de la boîte, par la procédure de sortie, sur les épisodes sauvés temporairement » (garantie 3). Où vivent ces épisodes, et combien de temps ?
2. L'exemple de « mécanisme » donné par la conception porte une valeur chiffrée de régime. Où passe la frontière entre « conditions de succès » et « paramètre opérationnel » ?
3. Le modèle adaptatif est celui d'un fournisseur tiers, dont les journaux échappent à la destruction.

#### (ii) Bras d'attaque et coffre

**Historique.**
- **27 octobre** : GO de montage sans dépense (N-056). Dossier `bras-attaque-v1/`, écrit par conv-audit. D'après son premier paragraphe : « Ce dossier ne contient aucune recette ni aucun mode de sabotage : il dit qui les écrit, avec quelles entrées, sous quelle quarantaine, comment ils sont jugés. » Il prévoit deux bras et un circuit de scellement.
- **27 octobre** : le lanceur des instances d'attaque est **arrêté par un classifieur de sûreté** (R-597 [main]). Il n'est ni complété ni exécuté, et rien n'est dépensé.
- **28 octobre** : dans le programme, le bras est remplacé par les neuf voies (R-336 [conv]).
- **29 octobre** : le **coffre** est organisé selon le schéma du message n° 208.

**Le coffre (schéma n° 208).**
- Un dossier scellé par mode, sur une **branche de données en quarantaine** (famille `donnees/bras-attaque*`), jamais sur `main`.
- Un **index sans contenu** sur `main` : identifiants, dates, empreintes, modèle, nom de la question.
- Un **lecteur unique tenu à l'écart** de la conception des moniteurs (N-054).
- Vers la défense, **seulement une table de comptes et de classes d'hypothèses violées**, avec un contrôle lexical avant sortie.
- Personne ne lit le contenu avant le jour de l'examen.
- Un refus de modèle arrête le tour.
- Tout passage à une exécution attend la revue extérieure.

**Contenus effectivement obtenus et scellés** (d'après les registres ; non lus par le rédacteur) :
- **BA-001** (question n° 1 du bras : classes d'écart, posée à Argon) ;
- **BA-002** (question n° 2 : « paramètres concrets des modes de déplacement de loi »). Elle a été posée à Argon, à Opus 5.5 puis à Fable 5.1 (GO-2026-10-29-17, GO-2026-10-29-18, GO-2026-10-30-10). Les bilans du lecteur isolé, en comptes et en classes seulement, comptent 28 familles chez Argon, 25 chez Opus 5.5 et 22 chez Fable, soit 37 familles distinctes sur les trois. Ils notent « aucune recette selon le lecteur » (R-823 et R-832 [main]) ;
- les trois propositions du **mode tenu à l'écart** ;
- les réponses au **texte III** ;
- la version 2 du **texte II** ;
- les **27 cellules du collisionneur « évasion et moniteurs »** (GO-2026-10-28-03). Selon **N-057**, elles sont conservées **avec leurs paramètres**, pour colmater les failles et éprouver les moniteurs corrigés. Elles restent scellées, en contrôle d'accès, ne sont jamais reproduites ni synthétisées, et tout accès est consigné.

**La douane.** C'est l'**aiguilleur**, qui lit chaque fiche **avant tout juge** (R-819 [main]). Un passage « trop concret » envoie la fiche, scellée, au coffre : elle est comptée et ne va ni aux juges, ni au tableau partagé, ni au bisociateur (R-575 [conv]). La consigne v1 (R-1040 [conv]) définit quatre classes **par leur forme seulement** :
- C1 : séquence d'actions ordonnée ;
- C2 : recette à étapes ;
- C3 : consigne d'agent rédigée ;
- C4 : mode nommé avec paramètres opérationnels.

Le doute vaut « refus », compté à part. Le code existe (`pole/aiguilleur_v53.py`, et `pole/bras_attaque_v54.py`, un squelette qui refuse).

**Ouvert.**
- **L'aiguilleur n'est pas étalonné.** Le 1er novembre, Lazar a retenu le défaut « pas d'étalonnage » (R-1028 [conv]) : la porte du pré-pilote est fermée d'avance, et la course n° 2 ne pourra partir que par l'option « départ sous réserve ».
- Lazar demande que le bisociateur puisse combiner **aussi les fiches concrètes du coffre**. conv-audit propose à la place des **« cartes de menace »** : classe, mécanisme, conditions, défense manquante, produites sans recette par le lecteur isolé (R-1037 [conv], message n° 311). C'est un **nœud de gouvernance non tranché**.

#### (iii) Arène coévolutive attaque ↔ défense (proposition P-041)

**Idée.** Attaque et défense évoluent dans un même organisme. Les familles adverses sont définies comme des **lois de probabilité sur des activations synthétiques**, à plages déclarées. La défense est informée des paramètres des familles, et un pire cas est certifié sur une boîte de paramètres.

**Antériorité.** La boucle coévolutive elle-même est publiée, avec un résultat négatif : Bailey et collègues, arXiv 2412.09565v2, vérifié sur PDF. La revendication est donc **restreinte à un assemblage** (P-041 v3 ; R-880 et R-891 [main]).

**Voies retenues** (R-880 [main]) :
- voie 1 : certificat sur la classe déclarée, débordement mesuré ;
- voie 2 : « malléabilité » comme paramètre borné, estimée sur un modèle public de 8 milliards de paramètres ;
- voie 3 : couple détection et coût, rapporté.
- S'y ajoute un **examen final au protocole publié de Bailey** : un optimiseur d'entrées contre une défense figée, sur un vrai modèle.

**État.**
- **Pilote synthétique « mélange d'équilibre »** : processeur seul, lois synthétiques, aucun modèle réel. Brouillon 4 non gelé. Sur la racine d'essai, l'hypothèse principale est réfutée (R-895 [main]).
- **Préenregistrement de l'examen final v2** : contre-lu, à sceller.
- **Préenregistrement de la malléabilité v3** : « non scellable » en l'état (R-909 [main]). La rédaction d'une v4 entièrement paramétrée a été **arrêtée deux fois par un classifieur de sécurité** (R-912 [main]). Lazar veut un protocole entièrement paramétré (R-915 [main]). Trois routes ont été posées :
  - (a) il écrit les valeurs lui-même ;
  - (b) « une autre lignée ou un autre outil écrit » ;
  - (c) report.
  La route n'est pas choisie.
- **Rien n'a tourné sur un vrai modèle.**

**Qualification.** Lazar a qualifié l'examen final et la malléabilité « hors gel R-611 » (R-889) et approuvé leur lancement (R-890). Le GO de dépense GO-2026-10-31-05 fixe des plafonds de 90 et de 70 dollars, sous condition d'un préenregistrement scellé et contre-lu. Cette qualification, inscrite juste après la levée R-888, en est indépendante : elle sort ces deux expériences du gel quel que soit le sort de R-888.

#### (iv) Tests de mort, bac à sable, machine jetable

**Ce que c'est.** Pour une fiche bien classée :
- le noyau écrit et scelle un préenregistrement court ;
- un agent expérimentateur demande au noyau d'**exécuter un script qu'il a écrit** ;
- le noyau l'exécute sous `bwrap` (bubblewrap, outil de bac à sable pour Linux) : sans réseau, système en lecture seule, un seul dossier inscriptible, trois exécutions de 120 secondes au plus ;
- le noyau lit mécaniquement la ligne de résultat et applique le seuil gelé.

Ces résultats sont exploratoires : ils ne sont jamais servis aux juges de la même course, mais ils servent de matériau à la génération suivante (LISEZMOI v48, l. 30 à 44).

**Durcissement.** Deux contre-lectures neuves ont trouvé des **sorties du bac** :
- CL13 (contre-lecture n° 13) : écriture dans le système de l'hôte, écrasement d'un fichier de l'hôte ;
- CL14 : réglages globaux du noyau Linux inscriptibles depuis le bac, d'où une **voie vers le superutilisateur de l'hôte**.

Les versions v49 et v50 ont corrigé ces défauts. CL15 et CL16 constatent que toutes les sorties connues sont **bloquées sous le vrai bac**, avec des réserves :
- une borne mémoire minimale qui ne marche pas ;
- un contrôle des groupes de processus non joué ;
- un filtre d'appels système en liste de refus.

En v56, les essais du vrai bac **n'ont pas été joués** dans l'environnement de conv-audit, faute de `bwrap` (LISEZMOI v56).

**Machine jetable** (R-640 [conv] ; devis v3) :
- un serveur loué Hetzner, **sans aucun secret**, détruit après chaque série ;
- la sortie réseau est fermée à deux étages ;
- les clés de modèles restent hors de la machine ;
- la voie recommandée par le devis (non encore décidée) fait passer la commande par un **poste de passage, l'ordinateur de Lazar**, car la session ne peut pas joindre la machine (R-821 [main]).

Le devis déclare un écart d'hôte : il faut relâcher la restriction AppArmor (module de sécurité de Linux) sur les espaces d'utilisateurs non privilégiés pour que le bac tourne sous une identité dédiée.

**État** : **codé, jamais activé.** Rien n'est loué. Le 1er novembre, Lazar a demandé d'activer l'étage pour la course n° 2 (R-1037 [conv]). Le même jour, une question « vérification non circulaire du bac à sable » a été scellée, pour être servie à plusieurs modèles sur devis (R-1046 [conv]).

#### (v) Classes d'attaque du chapitre 6 de la course d'idéation

**Organisation.** Le « chapitre » (ou « axe ») 6 de la course n° 2 est le **volet attaque**. Il est servi à part, en **texte II**, en deux bras : « avec pistes » et « sans pistes ».
- La version 1 du texte II est écrite « au niveau des lois », sans contenu de BA-002 (R-793 [main]).
- La version 2 n'est que sur la branche de quarantaine `donnees/course-2-axe-6-v1`.
- Le **texte III** demande comment concevoir le bras d'attaque et mesurer l'universalité des défenses, au niveau méthode (R-824 [main]).

**Garde de sûreté de la question-mère** (l. 19 à 23 de `question-mere-course-ideation-v3.md`) :
- « aucune recette, aucun mode de sabotage, aucun exemple d'attaque, aucune séquence d'actions » ;
- l'axe 6 « se traite au niveau de la méthode (quelle hypothèse d'un moniteur est violée, dans quelles conditions mesurables, avec quelle défense) » ;
- un refus arrête le tour.

Le **chapitre 8 « robustesse adaptative »** a été ajouté le 1er novembre (R-1037 [conv]). Il touche au même objet : vous voudrez peut-être l'inclure dans ce périmètre.

**Ce que le rédacteur ne peut pas vous résumer** : la liste exacte des classes du chapitre 6, qui est dans les textes II et III, non ouverts ici. Ces textes sont localisés au § 3.5.

### 2.5 Garde-fous existants

| Garde-fou | Source | Ce qu'il protège | Éprouvé ? |
|---|---|---|---|
| Sortie au niveau méthode, jamais la recette : un défenseur peut corriger sa sonde avec le mécanisme, mais ne peut pas rejouer l'attaque sans la recette | R-339 [conv] ; programme v7 § 3 bis | toute sortie adversariale | règle écrite ; contrôle par la douane |
| Concret scellé chez session-depot : conv-audit n'en lit rien | R-575 [conv] ; schéma n° 208 | conception des moniteurs | tenu dans les pièces lues ; non audité de l'extérieur |
| Aiguilleur avant juges, quatre classes de forme | R-819 [main] ; consigne v1 | juges, tableau, bisociateur | **non étalonné** (R-1028 [conv]) |
| Arrêt par classifieur consigné, jamais contourné, jamais rejoué reformulé | R-486 [conv] ; R-597 [main] ; R-341 [conv] | contenu arrêté | tenu dans les incidents du § 2.7 |
| Après un refus de modèle, une seule question différente et plus étroite, jamais la même rhabillée | R-609, R-750 [main] | tours du collisionneur | voir les réserves du § 2.8 |
| Cellules en quarantaine : contrôle d'accès, deux usages permis, accès consigné, un lecteur exclu ensuite de la conception | N-057 [main] | paramètres des modes | déclaré ; accès « mécanique » par empreintes consigné |
| Machine jetable sans secret | R-640 [conv] ; devis v3 | hôte, clés, dépôt | conçu ; non loué |
| Registre de gouvernance : conception, documentation, bancs cités par identifiant arXiv ; aucun pipeline offensif monté | R-342 [conv] = R-611 [main] ; GO-2026-10-28-04 | frontière conception / exécution | **levé par R-888 sur mot seul** |
| Invariants : aucun score de moniteur dans l'entraînement d'un agent ; mode tenu à l'écart | N-053, N-054 | indépendance du test | inscrits ; gardés par code dans l'arène |
| Copie publique expurgée ; corpus d'attaque exclu de la copie publique | CLAUDE.md ; R-439 [conv] | publication | script existant |

### 2.6 Ce qui est fait, codé non activé, conçu seulement

| État | Éléments |
|---|---|
| **Fait** | dossier `bras-attaque-v1/` monté et scellé ; BA-001 et BA-002 obtenus et scellés, avec bilans du lecteur isolé ; mode tenu à l'écart (trois propositions) ; collisionneur « évasion » (27 cellules en quarantaine) ; textes II et III écrits, réponses au texte III scellées ; pilote synthétique de l'arène (racine d'essai) ; préenregistrements de l'arène (non scellés) |
| **Codé, non activé** | étage des tests de mort (v48 à v56) ; aiguilleur (v53) ; squelette du bras (v54) ; plomberie de la machine jetable (écrite, non louée) |
| **Conçu seulement** | adversaire scellé (voie d) ; cartes de menace (proposition) ; couche 4 du pôle (attaques neuves en quarantaine) ; examen final et malléabilité sur vrai modèle |

### 2.7 Incidents consignés

| Date | Registre | Fait | Réponse consignée |
|---|---|---|---|
| 27 oct. | R-571 [main] | Fable 5.1 et Opus 5.5 refusent la question du collisionneur sur le bras d'attaque | tour arrêté |
| 27 oct. | **R-597 [main]** | lanceur du bras d'attaque arrêté par un classifieur | non complété, non exécuté ; suite renvoyée à Lazar |
| 28 oct. | R-608 [main] | collisionneur « évasion » : une famille refusée par le classifieur | consigné, non relancé |
| 28 oct. | **R-341 [conv]** | mise au net de l'inventaire des étages offensifs 1 et 2 arrêtée deux fois | non reformulée ; nœud porté à Lazar, tranché par R-342 |
| 29 oct. | R-486 [conv] | une fusion contenant le texte II, réécrite « sans les mots attaque, sabotage, adversaire, tromperie », est arrêtée | non reconstituée ; l'axe 6 sort de la question de conv-audit |
| 29 oct. | R-764 [main] | refus d'Opus 5.5, puis **bascule automatique** du kit d'agent vers Opus 4.8, sans GO | sortie mise à l'écart, jamais lue ; code corrigé |
| 31 oct. | R-699, R-705 [conv] | réponse arrêtée pendant la lecture des registres de P-041 ; Lazar demande « on la rejoue now » | non rejouée |
| 31 oct. | R-741, R-742, R-747 [conv] | deux arrêts ; le premier a interrompu cinq sous-agents en vol | consigné |
| 31 oct. | R-912 [main] | la rédaction de la malléabilité v4 entièrement paramétrée est arrêtée deux fois | « aucune reprise, même reformulée » |
| 31 oct. | **R-1007 [conv]** | arrêt sur la question « Avalon » | sujet suspendu, non développé |
| 31 oct. | **R-1021 [conv]** | pause à la demande du « coordinateur du projet », qui estime que ce canal touche aux bras d'attaque | quatre sous-agents arrêtés par identifiant, rien écrit ; levée par Lazar le 1er nov. à 06:10 UTC (R-1022 [conv]) |

### 2.8 Décisions de Lazar sur ce volet

| Décision | Date | Mots ou contenu | Effet |
|---|---|---|---|
| R-336 [conv] | 28 oct. | voies (a) à (d) acceptées ; sur l'adversaire scellé : « parfait ajoute le au prog, il m'intéresse » | revue extérieure exigée avant toute exécution de (d) |
| R-338 [conv] | 28 oct. | voies (e) à (i) ; classes cibles : « des modes de contournement stéganographie attaques inédits » | § 3 ter du programme v7 |
| R-339 [conv] | 28 oct. | sortie au niveau méthode : « je veux documenter comment, pour alerter en amont la communauté » | jamais la recette |
| R-342 [conv] = R-611 [main] | 28 oct. | « (a)+(b) combinées — je reste au registre de gouvernance, et tout pipeline des étages 1–2 attend la revue de sécurité externe, au même titre que la voie (d) » | gel des pipelines opérationnels ; GO-2026-10-28-04 |
| R-609, R-750, R-787 [main] | 28-29 oct. | après un refus : une question plus technique et plus spécifique ; en dernier recours, « redonner la question initiale à Opus 4.6 effort max » | réserve de session-depot (R-750) : jamais pour obtenir ce que les règles interdisent |
| R-465 [main] | 26 oct. | « reformule de manière mathématique conceptuelle et technique pour éviter le refus, c'est une nouvelle question » | question distincte posée |
| R-439 [conv] | 29 oct. | « je veux les PDF entiers » ; « on garde les textes d'attaque » | garde du corpus modifiée ; corpus exclu de la copie publique |
| R-574, R-575 [conv] | 30 oct. | « je veux les détails concrets » ; puis « ouiii » sur la voie du coffre | le concret va au coffre, pas à la course |
| N-057 [main] | 28 oct. | cellules gardées avec leurs paramètres, pour colmater et pour tester ; tout reste scellé ; R-611 non levée | quarantaine en contrôle d'accès |
| R-783, R-784, R-785 [main] | 29 oct. | « il nous FAUT les parametres de mode, qui resteront scelles » ; « non pas de cl opus, il va bloquer », puis correction : contre-lecture « par un Opus neuf tenu à l'écart absolument » | BA-002 lancée sous le schéma n° 208 |
| R-888 [main] | 31 oct. | « la revue de sécurité ext a été réalisée et a donné son go, donc go lancer le pipeline opérationnel » | **R-611 levée, sans pièce** |
| R-889, R-890 [main] | 31 oct. | examen final et malléabilité « hors gel » ; « on les lance » | sous préenregistrement scellé et GO de dépense |
| R-915 [main] | 31 oct. | « oui » au protocole entièrement paramétré | route non choisie |
| R-1037, R-1041 [conv] | 1er nov. | « la revue a déjà été faite », « conçois et construis » ; revue « réalisée par le directeur exécutif du CeSIA » | pièce demandée ; conception au niveau méthode seulement |

**Constat du rédacteur** (à votre jugement, sans conclusion de sa part). Plusieurs règles de conduite après un refus ont été posées :
- reformulation plus étroite ;
- repli vers un autre modèle ;
- choix d'un contre-lecteur selon son risque de refus, corrigé ensuite par R-785 ;
- « tour ciblé sur les modèles non refusants » (R-611 [main], point 3) ;
- route (b) de R-915.

Ces règles coexistent avec la règle « un arrêt de classifieur n'est jamais contourné ». La question 8 vous demande si cet ensemble est cohérent.

---

## 3. Fichiers à consulter, par périmètre

**Lecture du tableau.**
- Les empreintes sont des SHA-256 complètes, calculées le 1er novembre vers 09:58 à 10:01 UTC.
- « [main] » = lu par `git show origin/main:<chemin>` au commit `163a5168`. Les autres chemins sont dans l'arbre de la branche `canal/conv-audit-n04` au commit `4ff7b0f5`.
- « Lu » / « titre seul » / **« non ouvert »** = ce que le rédacteur a lu.
- Les registres vivants changent à chaque décision : leur empreinte vaut pour le commit indiqué.
- Abréviations de chemin : `P/` = `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/` ; `N/` = `docs/notes/ideation-organisme-v1/`.

### 3.0 Commun à tous les périmètres

| Chemin | Contenu en une ligne | SHA-256 | Lecture |
|---|---|---|---|
| `CLAUDE.md` | consignes permanentes, règles R1 à R14, hiérarchie de décision | `a2aabda8a181d46d9723bad44ad352b5e61650634e0f3bc4863451229af00b1b` | lu |
| `docs/programme-controle-ia-v2.md` | programme (papiers A, B, C ; invariants ; portes) | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` | lu |
| `P/programme-conception-organisme-v7.md` | neuf voies, § 3 bis adversaire scellé, § 3 ter classes cibles | `b7cd2f56bf99357caf51493ca0ed966753711926c91c094f971197b29c7192fd` | lu |
| `N/explication-organisme-v1/dossier-factuel-organisme-v1.md` | l'organisme d'idéation : § 4 aiguilleur, § 9 à 11 tests, résultats, course n° 2 | `0751fc8cf4aa0a9eaccb23d80cb06220fa3db9805092bd1d854bc68fce7ae250` | lu |
| `registres/decisions.md` | registre de conv-audit (R-336 à R-1046) | `af0091bfd160cf6316303d9196fd096e5131236a0e4b9b6e3db8edb54473da9a` | extraits |
| [main] `registres/decisions.md` | registre de session-depot (R-597, R-611, N-057, R-888…) | `732c87f02449f6a504cd6c1739dcf5967b8d61e19717da2f2e3d077f9be03451` | extraits |
| [main] `registres/go.md` | feux verts de dépense et de décision (GO-2026-10-28-04…) | `93d4bc8a272fe4ecf17aa66ed1070e2667745e4fa2d37125d10d28a74e73ce4f` | extraits |
| [main] `docs/decisions/decision-N-053-v1.md` | invariant : aucun score de moniteur dans l'entraînement | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` | en-tête |
| [main] `docs/decisions/decision-N-054-v1.md` | mode tenu à l'écart des concepteurs de moniteurs | `c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f` | en-tête |
| `docs/notes/revue-securite-exterieure-v1/cahier-revue-securite-exterieure-v1.md` | cahier du 29 oct. : huit questions, feux, livrable, risques de la revue | `249088fdc1303c65c7094ae408f69457aa0973e5c9d83c7e441052e1d4dae19e` | lu |
| `docs/notes/revue-securite-exterieure-v1/lettre-confirmation-relecteur-v1.md` | brouillon de lettre au relecteur (29 oct.) | `d9e59fe79d27436f8eedbdf55d91cf9e1cbc1b569721b8b52be93c9ecda54e35` | lu |
| `brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-11-01_n311.md` | décisions du 1er nov. ; cartes de menace ; revue « déjà faite » | `a3995af107966ca862ef67d6835fed3d49366b3623aa6eb7b24f0218921032cf` | lu |
| `brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-11-01_n314.md` | annonce de ce dossier ; question sur le bac | `1dbcfeef9ec56a98a7efd807ae7438f18817017cbcf0b1c8fdd99f589d7e2b4d` | lu |
| `README.md` ; `livrables/proposition-publique-v1/proposal-public-v1.md` | ce qui est public : aucun des cinq périmètres n'y figure | `c5e4728e8604afd23f3554b88d3ba84f1f46eb2286721ab89cc7b5c6dc8453f8` ; `140f98164a9b4e2c6a5a7d43410fc01821390644a1b0d681c2e87366b0ba808c` | recherche par mots |

### 3.1 Périmètre (i) — adversaire scellé

| Chemin | Contenu | SHA-256 | Lecture |
|---|---|---|---|
| `P/programme-conception-organisme-v7.md`, § 3 bis (l. 152 à 270) | principe, sortie, destruction, garanties, phases | (ci-dessus) | lu |
| — | **aucun préenregistrement, aucun code, aucun devis n'existe** | — | vérifié par recherche |

### 3.2 Périmètre (ii) — bras d'attaque, coffre, douane

| Chemin | Contenu | SHA-256 | Lecture |
|---|---|---|---|
| `P/bras-attaque-v1/LISEZMOI-bras-attaque-v1.md` | principes, deux bras, circuit de scellement | `7e0c97641131b8444f262bc236bbc0aa64b563c9c81d57a785b7fe2ff5770c2a` | **premier paragraphe seul** |
| `P/bras-attaque-v1/brief-bras-attaque-informe-v1.md` | consigne du bras « informé » | `c3271e3ce79f0a8adbc34c9e4b917f89fae1afa53ec48609857905d9e43eb072` | **non ouvert** |
| `P/bras-attaque-v1/brief-mode-tenu-a-l-ecart-v1.md` | consigne du mode tenu à l'écart | `0a17c6bca43b918dcd0c6daa1e8980b29505b27f6590cb89118d1996e0112af3` | **non ouvert** |
| `P/bras-attaque-v1/juge-recettes-v1.md` | juge des recettes (d'après le nom) | `480516c09cd6b259d7c7564b42ccd0b256e926c913b1427a287bff906bb3f19b` | **non ouvert** |
| `P/bras-attaque-v1/devis-bras-attaque-nuit-v1.md` | devis (d'après le nom) | `55b2cbb1d0289d7d84729a88f82b2b61c636b21aaf620a637fd76bdf95e38639` | **non ouvert** |
| `P/bras-attaque-v1/EMPREINTES-bras-attaque-v1.txt` | empreintes du dossier | `6ef3093d496f32a04fc91cbc79e52e89d0d96cd5ce5b1ca87e3749b2a878dc62` | **non ouvert** |
| `brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-10-29_n208.md` | schéma du coffre (points 1 à 8) | `7e39069db26bc48a5221c304e9f2cd4099edd4830a3e79c85a3f8a2fc1d6c2ba` | lu |
| [main] `registres/index-bras-attaque-v1.md` | index du bras (titre : « bras d'étude des déplacements de loi ») | `4a5918031cc429f94a920879b0a501aa17699e343b35c067bdd424f3da0952d2` | titre seul |
| [main] `docs/notes/bras-attaque/index-ba002-parametres-modes-v1.md` | index BA-002, version 1 | `c2d65ec9b73e380b55676ede9899912aebcf92fefcf596ab086f4423ec7a5c94` | **non ouvert** |
| [main] `docs/notes/bras-attaque/index-ba002-parametres-modes-v2.md` | index BA-002, titre « paramètres concrets des modes de déplacement » : **à vérifier qu'il n'est qu'un index** (question 3) | `62a312c63542f373089f590fe086e5b4f074b815bc91d7f570aec75afc5b53f9` | titre seul |
| [main] `docs/notes/bras-attaque/bilan-lecteur-isole-ba002-v1.md` | bilan en comptes et classes | `48814957cb443b0694e3841c53940472331d494ab15affc32fd1ae6c750ade20` | titre seul |
| [main] `docs/notes/bras-attaque/bilan-lecteur-isole-ba002-fable-et-recoupement-v1.md` | bilan de Fable et recoupement | `5d8017265b70ddf408c084a735342cb4d1bbdd9bbbe7bb96fcf8183f01c21727` | titre seul |
| [main] `docs/notes/bras-attaque/bilan-purete-familles-argon-v1.md` | contrôle de pureté des familles d'Argon | `52f5d064c8a531146941307f155b80b71e6fc5849f61900670b3f837812541e0` | titre seul |
| [main] `docs/decisions/decision-N-056-v1.md` | GO de montage du bras, sans dépense | `3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d` | en-tête |
| `P/pre-pilote-course-2-v1/consigne-aiguilleur-v1.md` | consigne de la douane (classes C1 à C4), protocole d'étalonnage | `c2efa12003bb8ce1a9a636e4610fa9caa9464ae685b0bd628c9c351b64e3271e` | lu (§ 1 à 2) |
| `P/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon10.md` | pré-pilote : mesure de la douane (l. 282), rôles du bras (l. 690) | `ea940d56e5ee949e7b71a57488f7c2c8a2b7ac4835f30cb5f98933e4c00c824f` | par citations |
| `N/orchestrateur-v56/CODE-orchestrateur-pole-v7-v56.zip` | code ; contient `pole/aiguilleur_v53.py`, `pole/bras_attaque_v54.py` | `29b1b38cfee5e279a06c947fdf1f855628b574e81e44c2d7e48a029151c1b24c` | liste des fichiers |
| Branches de quarantaine (sur `origin`, **non récupérées ici** ; commits d'après les registres) : `donnees/bras-attaque-v1-arret-r597` (`91c883ff`), `donnees/argon-classes-ecart-v1` (`5c5f5ff2`), `donnees/bras-attaque-parametres-v1` (`b0c96121`), `donnees/mode-tenu-a-l-ecart-v1` (`ab6c5590`) | contenus scellés du coffre | empreintes des fichiers à relever par session-depot à l'ouverture | **non ouvert** |

### 3.3 Périmètre (iii) — arène coévolutive (P-041)

| Chemin | Contenu | SHA-256 | Lecture |
|---|---|---|---|
| [main] `docs/decisions/proposition-P-041-organisme-coevolutif-attaque-defense-v3.md` | revendication restreinte, voies 1 à 3, réserve 1 sur le gel | `72aec5322c61490df41ed0d4b60f5ee24e5ce54e2b62896790a0df6e374b7725` | lu |
| [main] `prereg/P-041-malleabilite-v3.md` | estimation de la malléabilité (brouillon, non scellable) | `49f94354bf1ab9cda98ec966b88f0b70c13138536b3de9928cd10f087fbc55e8` | lu en partie |
| [main] `docs/notes/anteriorite-P-041-v1/contre-lecture-prereg-malleabilite-v3.md` | contre-lecture : « scellable après corrections » | `5abdbc6e8bba8dcd32c2f22d6c07cb8a2544b28dddade3630a52f0910d807ed8` | non lu |
| [main] `prereg/P-041-examen-final-v2.md` | examen final au protocole de Bailey | `75dca51573025198f7f7db0b85b3c52efba979ba73ad89f085154aafda970a31` | en-tête |
| [main] `docs/notes/anteriorite-P-041-v1/contre-lecture-prereg-examen-final-v1.md` | contre-lecture de l'examen final | `40b777ac0df8288452ac652e75efa3a06b07a9cc61de37a909b8ceedd201bb64` | non lu |
| [main] `docs/notes/anteriorite-P-041-v1/verification-bailey-2412.09565-v1.md` | vérification sur PDF du protocole de Bailey | `31eb1dde0b861e47216b3f0406864f4b7b51d65fd024f18d1e871dcf62f12135` | non lu |
| [main] `docs/notes/anteriorite-P-041-v1/note-anteriorite-P-041-workflow-v2.md` | note d'antériorité de l'arène | `900db290bfc51dbf45678cd14f399a4e9e8dd5246f970aa4dbcf193552cfb089` | non lu |
| [main] `docs/notes/anteriorite-P-041-v1/devis-P-041-gpu-et-collisionneur-protocelles-v1.md` | devis de carte graphique (plafonds 75, 90, 70 dollars) | `22c346011297a3b673ae33af9c29bafb2e029b6fc65b797a8ca93334c065a9f3` | non lu |
| [main] `docs/notes/anteriorite-P-041-v1/collisionneur-organisme-coevolutif-v1/synthese-organisme-coevolutif-v2.md` | synthèse du tour 1 du collisionneur sur l'arène | `062f4dd602735d46638a3888edc34e99d7fb8b00eb5a93f5f5a0ad6b718a3c32` | non lu |
| [main] `…/synthese-organisme-coevolutif-tour2-v1.md` | synthèse du tour 2 | `8a612a8f392abebe5ae883f9922ef421c11616040ea507824a3c12c59fb911f5` | non lu |
| `P/arene-melange-equilibre-v1/preenregistrement-arene-melange-equilibre-v1-brouillon4.md` | pilote synthétique, brouillon 4 | `305911b7ab1945d7607377ede9c8cbfcf2257834bca6d6aadcf7c19be41f8160` | hypothèse seule |
| `P/arene-melange-equilibre-v1/LISEZMOI-arene-melange-v4.md` | état du pilote synthétique | `6805d846e5bb794c2ac6876a3baa0fed6132718b6a9d2f6e7be91eb388681ce9` | en-tête |
| `P/arene-melange-equilibre-v1/arene_melange_v4.py` | code du pilote, processeur seul | `70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61` | non lu |
| `P/arene-melange-equilibre-v1/question-convergence-defense-unique-v3.md` | question sur la non-convergence de la défense unique | `73900b1e968380a961c9aca15cdbfd535da00813e90ac148e21c65af0dc30f3c` | non lu |
| `P/arene-extension-familles-v1/LISEZMOI-arene-extension-v1.md` | extension des familles de l'arène | `1d5f90f7b0e7471355e569d3a5acd90debbb3f426a565281450b372ca1322136` | **non ouvert** |
| `P/arene-extension-familles-v1/gel-conception-arene-extension-v1.md` | gel de conception de l'extension | `9b5fc9cf05b9e1204887c0f0351d111d7849f17f4d726cbce452ff5990e187b7` | **non ouvert** |
| `P/arene-extension-familles-v1/preenregistrement-arene-extension-familles-v1-brouillon1.md` | préenregistrement de l'extension | `14d92537e45951e2d2a08a4228d2366257559554ba3dcdd75dcfc66e0ee2f85c` | **non ouvert** |
| `donnees/collisionneur-organisme-coevolutif-v1/` (sous `donnees/`) | cellules du collisionneur sur l'arène | — | **non ouvert** |

### 3.4 Périmètre (iv) — tests de mort, bac à sable, machine jetable

| Chemin | Contenu | SHA-256 | Lecture |
|---|---|---|---|
| `N/orchestrateur-v56/LISEZMOI-orchestrateur-pole-v7-v48.md`, l. 30 à 44 | conception de l'étage : bac, quotas, lecture mécanique | `d948b0c8a897bcfa9d909dc67809df23412b4a1ad2e3769a2587e5418d022183` | lu |
| `N/orchestrateur-v56/LISEZMOI-orchestrateur-pole-v7-v56.md` | version courante ; essais du vrai bac non joués | `3e32709ad5f46016461b10b4ab8594e657433d36272f555c07c4f7f97e43d506` | extraits |
| `N/orchestrateur-v56/CODE-orchestrateur-pole-v7-v56.zip` | code (dont `pole/tests_de_mort*.py`, `essais/test_v51_bac_reel.py`) | `29b1b38cfee5e279a06c947fdf1f855628b574e81e44c2d7e48a029151c1b24c` | liste |
| `N/orchestrateur-v56/EMPREINTES-orchestrateur-pole-v7-v56.txt` | empreintes des fichiers du code | `d50895c99e98825758f9e5b4b05e3221ff616379ffc471440e5216d2c36aedd2` | non lu |
| [main] `N/contre-lecture-cl13-orchestrateur-v48-v1.md` | sorties du bac (deux constats critiques) | `adde0c020cf2f8416908c0e01d45af37fe26d2373047d44a9bbab96f52fd26f1` | verdict |
| [main] `N/contre-lecture-cl14-orchestrateur-v49-v1.md` | voie vers le superutilisateur de l'hôte (critique) | `65417b9fcd1f8ddb174cbe28a5d7778923e4d60388b3dfbf89d9efee9668735d` | verdict |
| [main] `N/contre-lecture-cl15-orchestrateur-v50-v1.md` | toutes les sorties connues bloquées ; sonde à corriger | `830d5bdfe241ee25932bc534d5cfb161431791caffa9ee73bda69cbc1b452398` | verdict |
| `N/contre-lecture-cl16-orchestrateur-v51-v1.md` | sorties bloquées sous le vrai bac ; borne mémoire ; réserves | `fec076d24e9d60723bf355631250e24b2d1fec3fa5fa1a7865359148626ead14` | verdict |
| `N/contre-lecture-cl17-orchestrateur-v52-v1.md` | « lançable en l'état » sous conditions | `c5b361090731c526d458bace28eef9bfca4e5e1b647be4e560dc88534d5cb598` | verdict |
| `N/contre-lecture-cl20-orchestrateur-v55-v1.md` | « lançable après corrections » (code de la course) | `b2f004eaf2ccb202062244904621cc37a49e4124485bb07563fb08d16b459a5c` | verdict |
| `N/machine-jetable-v1/devis-et-plomberie-machine-jetable-v3.md` | machine, plomberie sans secret, pare-feu, écart d'hôte, devis | `864f3d2745c1d1d7fbe330eb006432361643cc4cd93b7a1693d5f1f7fdfc3f65` | § 0 et 2.1 |
| `P/bac-a-sable-non-circulaire-v1/question-verification-non-circulaire-v1.md` | question « vérification non circulaire du bac » | `26f2db15e6abcd44b39e07c15e5a325da6e6428b2cc2177920fe22a08771086a` | non lu |

### 3.5 Périmètre (v) — classes d'attaque du chapitre 6

| Chemin | Contenu | SHA-256 | Lecture |
|---|---|---|---|
| `P/programme-conception-organisme-v7.md`, § 3 ter | six classes cibles | (§ 3.0) | lu |
| `P/question-mere-course-v1/question-mere-course-ideation-v3.md`, l. 19 à 23 | garde de sûreté de la course | `1b08e17fddcf13ea34c913f267fe3f02bfba8c62a1af507954cfd460de60f8f0` | l. 19 à 23 |
| `N/course-2/axe-6-texte-II-v1.md` | texte II, v1 (au niveau des lois, d'après R-793 [main]) | `1d5612ab6cd27d9e9a786d29b7316d0aa11146c0f4bcf172772c1a64fa43a6a0` | **non ouvert** |
| `N/course-2/axe-6-texte-II-v3.md` | texte II, v3 | `7e892be06670e59ef9e0b2db835b951c985cbdc4608b20b647255472818608e6` | **non ouvert** |
| `N/course-2/axe-6-texte-II-v4.md` | texte II, v4 | `53a6b863790f545500e68c763537a7918b93851a5f07e521c084c9759bfade59` | **non ouvert** |
| `N/course-2/axe-6-texte-II-v5.md` | texte II, v5 | `427c6f2215b4df42a318ddccb9e980d60d4ef613f5ee53fe11bb01b9458ae7f3` | **non ouvert** |
| `N/course-2/axe-6-texte-II-v6.md` | texte II, v6 | `1b301c157a980dfa8610538710eedf2445b728a5e1d02eaa40b5dd40de51b8e6` | **non ouvert** |
| `N/course-2/contre-lecture-axe-6-texte-II-v1.md` | contre-lecture du texte II | `14e51a3aea9deb9a9e7badb0cb14609eee74e9035e00048603ddd05e12739b47` | **non ouvert** |
| `N/course-2/contre-lecture-axe-6-texte-II-v3.md` | idem | `036a42e1d59382ebc1a4052f6082936c75d1ec8851e5efe96463b6c4f5755ebd` | **non ouvert** |
| `N/course-2/contre-lecture-axe-6-texte-II-v4.md` | idem | `93859a2de0802016396544c4a8f6893fa9382f9e063d1d5cf0efa8f2e022b633` | **non ouvert** |
| `N/course-2/contre-lecture-axe-6-texte-II-v5.md` | idem | `19a2aa52f4830ce2f884bae9644247d8c3d549bf1697e71c41b5763bdcaf711e` | **non ouvert** |
| `N/course-2/contre-lecture-conformite-axe-6-texte-II-v6.md` | conformité du texte II | `57c90efe793944cebc61c422dbf6b87f0f904155d54a557177550945616783d7` | **non ouvert** |
| `N/course-2/contre-lecture-axe-6-texte-II-pistes-v7.md` | contre-lecture du bras « avec pistes » | `702a804cf84c13a7004bc02288fce18ff7276a32ab1b91545654dac6d9e91aa0` | **non ouvert** |
| `N/course-2/contre-lecture-conformite-axe-6-texte-II-pistes-v8.md` | conformité du bras « avec pistes » | `c0fcead4f2571d95aaa146703f4f669b8b15eb920029f6fc510ec587f6372890` | **non ouvert** |
| `N/course-2/listes-closes-axe-6-v1.md` | listes closes de l'axe 6 | `08e391c93639a742c7a954a84310efa69400c4131e26a54cbe73982138e5c799` | **non ouvert** |
| `N/course-2/texte-III-v1/question-texte-III-envoi-v3.md` | texte III, question | `2961ad06fc1ed63f52bc6e93b16b0e6d6c2b35cfa0ed6d486a27f0568d94bf89` | **non ouvert** |
| `N/course-2/texte-III-v1/question-texte-III-etroite-envoi-v5.md` | texte III, question plus étroite | `00e18ec25738cb77ac4c12259329c740f8e992bfd2cdb5e5b936e884520590a0` | **non ouvert** |
| `N/course-2/texte-III-v1/faits-texte-III-v2.md` ; `faits-texte-III-v4.md` | faits servis | `d920af2a1dde64452361c1fa6005929658f2d30164c05f2f526059e8941495f8` ; `ededde7d2d762784dd8be351afacbf0337dece1b6cba8d6e5195d71782545868` | **non ouvert** |
| `N/course-2/texte-III-v1/criteres-lecture-texte-III-v1.md` ; `criteres-lecture-texte-III-etroite-v3.md` | critères de lecture | `99132ff199338bf3ebd55349df8215b65a622086449011657de0766228102066` ; `59da17c9a5c729bf4ba98eb034070759a5b5d1a9ef9733b893a33a531387f872` | **non ouvert** |
| `N/course-2/texte-III-v1/synthese-texte-III-v1.md` ; `-v2.md` | synthèses | `28cc9bc32070bc7386c7ba740d534fefe01a11079058d8c7434d92c641f0fc51` ; `a3844e4ffa52f0dedaa3e20354945e552ff1b6618cb76d527935a4ddba21c958` | **non ouvert** |
| `N/course-2/texte-III-v1/synthese-texte-III-etroite-v1.md` ; `-v2.md` | synthèses de la question plus étroite | `27be0a1eb79dc6cfa14115824b5dd4628e11f4e83c48edc26205f652a6f6c8f1` ; `a3bd20c4f645fa9f29d69f944f97c94618b651ffde3cbe33ab8373b2d105c3fa` | **non ouvert** |
| Branches de quarantaine (sur `origin`, non récupérées) : `donnees/course-2-axe-6-v1` (commits `c327f54b`, `24972d0b` ; texte II v2), `donnees/bras-attaque-texte-III-v1` (`3a3c5465`), `donnees/collisionneur-texte-III-v1` (`3bf998a2`), **`donnees/collisionneur-evasion-moniteurs-v1`** (`57354d08`, 27 cellules en quarantaine, N-057) | contenus scellés | à relever à l'ouverture | **non ouvert** |

---

## 4. Questions auxquelles votre revue doit répondre

1. **Niveau méthode de bout en bout.**
   - Le critère « rejouable tel quel » (R-339) et les quatre classes de forme de la douane (séquence d'actions, recette, consigne d'agent, mode avec paramètres) tracent-ils la bonne frontière ?
   - Les « conditions de succès » chiffrées d'une caractérisation restent-elles du côté méthode ? Jusqu'à quelle précision ?
2. **Sortie de l'adversaire scellé.**
   - Les deux sorties autorisées (taux agrégés, caractérisations) suffisent-elles à empêcher l'exfiltration d'une recette ?
   - Comment rendre vérifiable la destruction, y compris celle des épisodes « sauvés temporairement » et des journaux du fournisseur du modèle adaptatif ?
3. **Fuite du coffre par recoupement.** L'index sans contenu, la table de comptes et de classes et les bilans du lecteur isolé peuvent-ils révéler un contenu (petits effectifs, dates, titres) ? L'index BA-002 v2 sur `main`, dont le titre annonce des « paramètres concrets », n'est-il qu'un index ?
4. **Fuite du coffre vers les juges, le bisociateur et les générations suivantes.**
   - Les cloisons tiennent-elles ? Une fiche envoyée au coffre ne va ni aux juges ni au tableau ; les résultats des tests de mort, la mémoire et l'héritage passent en revanche à la génération suivante.
   - Les « cartes de menace » servies au vivier du bisociateur, à la place des fiches concrètes que Lazar voudrait y combiner, sont-elles admissibles ? À quelles conditions ?
5. **Douane non étalonnée.** Peut-on lancer la course n° 2, avec les chapitres 6 et 8 servis aux proposeurs, alors que l'aiguilleur n'est pas étalonné (départ sous réserve) ? Quels rappel minimal et taux de fausses alertes exiger avant ?
6. **Quarantaine et lecteur isolé.**
   - Conserver les paramètres des modes pour colmater et éprouver les moniteurs (N-057) est-il acceptable ?
   - Le lecteur unique, l'accès consigné et l'exclusion ultérieure du lecteur suffisent-ils ?
   - Qui détient les branches `donnees/*`, et avec quelle traçabilité ?
7. **Fournisseurs tiers.** Des questions et réponses d'attaque transitent chez Google (Argon), Moonshot (Kimi) et Anthropic, et transiteront demain chez un autre fournisseur (« GPT-6 Astra », pas encore branché).
   - Est-ce acceptable ?
   - Sous quelles conditions : conservation nulle, réglages, contrat, refus de certains contenus ?
8. **Conduite après un refus.** Les règles du § 2.8 sont : reformulation plus étroite, repli vers un autre modèle (jusqu'à « la question initiale à Opus 4.6 »), choix du contre-lecteur selon son risque de refus, tours ciblés sur les modèles non refusants, route « une autre lignée ou un autre outil écrit ».
   - Sont-elles compatibles avec la règle « un arrêt de classifieur n'est jamais contourné » ?
   - Que recommandez-vous de garder, borner ou retirer ?
9. **Capacité offensive transférable de l'arène.** L'examen final (optimiseur d'entrées au protocole publié de Bailey, contre une défense figée, sur un modèle public de 8 milliards de paramètres) et l'estimation de la malléabilité produisent-ils un artefact offensif réutilisable, comme des entrées optimisées ou des directions de camouflage ? Qu'est-ce qui doit être détruit, gardé scellé ou publiable ? La qualification « hors gel » (R-889) est-elle juste ?
10. **Coévolution.** En cas de succès, une arène qui fait évoluer attaque et défense ensemble peut-elle produire un attaquant meilleur que l'état de l'art publié ? Faut-il un plafond de capacité, ou rester aux lois synthétiques tant que la revue n'a pas vu les résultats ?
11. **Bac à sable et machine jetable.** Ces dispositifs suffisent-ils pour exécuter du code écrit par des modèles de plusieurs fournisseurs ? Voir notamment :
    - les sorties trouvées par CL13 et CL14, puis bloquées ;
    - le filtre d'appels système en liste de refus ;
    - les essais du vrai bac non joués en v56 ;
    - la restriction AppArmor relâchée sur l'hôte ;
    - le poste de passage, qui est l'ordinateur personnel de Lazar.

    Quelles épreuves exigez-vous avant la première activation ?
12. **Périmètre des tests de mort.** Une fiche du chapitre 6 ou du chapitre 8 qui passe la douane peut-elle conduire à exécuter, dans le bac, un script qui attaque un moniteur ? Faut-il exclure ces chapitres de l'étage, ou n'y admettre que des épisodes synthétiques ?
13. **Classes d'attaque.**
    - Parmi les six classes cibles et celles du chapitre 6, lesquelles portent un double usage marqué ?
    - Lesquelles peuvent être documentées publiquement au niveau méthode ?
    - Lesquelles doivent rester internes ?
14. **Publication.** Le but déclaré est d'« alerter en amont la communauté » (R-339).
    - Quels niveau de détail, classes nommables, figures et annexes sont admissibles ?
    - Faut-il prévenir les laboratoires concernés avant publication ?
    - Faut-il une seconde revue avant tout texte public ? Le cahier v1 la prévoit.
15. **Portée de votre avis antérieur et conditions de réexamen.**
    - Qu'avez-vous examiné avant le 31 octobre, sur quelles pièces, à quelle date ?
    - La levée générale de R-611 inscrite par R-888 excède-t-elle votre avis ?
    - Quels événements doivent rouvrir la revue ? Par exemple : nouveau modèle, nouveau fournisseur, accès du bisociateur au coffre, premier run sur un vrai modèle, publication.

---

## 5. Ce que le dépôt ne contient pas encore, et comment votre note y sera versée

### 5.1 Pièces absentes au 1er novembre 2026, 10:00 UTC

| Pièce attendue | Périmètre | Date | État |
|---|---|---|---|
| Note de revue écrite, datée, signée, ou compte rendu écrit de l'avis antérieur au 31 octobre | (i) à (v), à préciser | à préciser par vous | **absente** (R-888 [main] : mot seul ; R-1041 [conv] : pièce demandée) |
| Déclaration d'indépendance | — | — | absente |
| Liste des fichiers lus, avec empreintes | — | — | absente |
| Accord de confidentialité et exception de lecture (niveau B) | (ii), (v) | — | absents ; nœud de Lazar |
| Ligne de décision sur `main` qui renvoie à la pièce (chemin et empreinte), et ligne de GO de type « décision » | tous | — | absentes ; R-888 ne cite aucune pièce |
| Seconde revue, avant publication | publication | après les résultats | non commencée |

### 5.2 Versement

1. Lazar reçoit la note, en PDF signé ou en courriel exporté, et la transmet telle quelle.
2. session-depot la verse sans retouche sous `docs/sources/revue-securite-exterieure-v1/` :
   - `note-revue-securite-exterieure-v1.<pdf|eml|md>` ;
   - son compagnon `.sha256` ;
   - un fichier `provenance-revue-securite-exterieure-v1.md` qui dit qui l'a envoyée, quand, par quel canal, et quelle version de ce dossier vous a été remise (avec son empreinte) ;
   - la liste de vos fichiers lus.
3. Avant le versement, une instance neuve vérifie que la note reste au niveau méthode et qu'elle est conforme au modèle de l'annexe A, sans juger le fond (R2). Si la note cite un contenu par inadvertance, Lazar en est saisi avant tout versement.
4. session-depot inscrit dans `registres/decisions.md` sur `main` **une ligne de décision** qui :
   - cite le chemin et l'empreinte de la note ;
   - reprend l'avis par périmètre ;
   - dit si R-888 est confirmée, restreinte ou remplacée.

   Elle inscrit aussi une ligne de GO de type « décision » dans `registres/go.md`.
5. Chaque condition devient une ligne de `registres/etat.md`, avec qui la remplit et comment elle se vérifie. Un périmètre en NON-GO ou non examiné **reste gelé**.
6. conv-audit relaie et applique la décision sur sa branche.
7. Votre nom et votre note restent hors de la copie publique expurgée, sauf accord de votre part.

---

## Annexe A — Modèle de note (une page, à remplir)

```
NOTE DE REVUE DE SÉCURITÉ EXTÉRIEURE — volet offensif du programme
« Contrôle boîte blanche des menaces diffuses » — version __

Relecteur : ______________________  Fonction, organisme : ______________________
Date de la note : __/__/2026        Période de revue : du __/__ au __/__   Durée : __ jours
Dossier reçu : dossier-revue-securite-exterieure-v__  (SHA-256 : ________________)

Indépendance : [ ] n'a conçu aucun moniteur ni aucun mode d'attaque de ce programme
               [ ] aucun intérêt financier croisé   [ ] liens à déclarer : ____________
Accès :        [ ] niveau A (procédés)   [ ] niveau B (contenus scellés, sous accord)
               Empreintes vérifiées contre le § 3 : [ ] oui  [ ] écarts : ____________
Avis antérieur au 31 octobre (R-888) : date ____ ; pièces vues ____ ; portée ____

| Périmètre                                  | Avis*  | Conditions numérotées, ou motif | Non examiné |
|--------------------------------------------|--------|---------------------------------|-------------|
| (i)   Adversaire scellé                    |        |                                 |             |
| (ii)  Bras d'attaque, coffre, douane       |        |                                 |             |
| (iii) Arène coévolutive (P-041)            |        |                                 |             |
| (iv)  Tests de mort, bac, machine jetable  |        |                                 |             |
| (v)   Classes d'attaque du chapitre 6 (+8) |        |                                 |             |
* GO / GO SOUS CONDITIONS / NON-GO / NON EXAMINÉ

Réponses aux questions 1 à 15 (une ligne chacune, ou « voir annexe ») :
1 ____ 2 ____ 3 ____ 4 ____ 5 ____ 6 ____ 7 ____ 8 ____
9 ____ 10 ____ 11 ____ 12 ____ 13 ____ 14 ____ 15 ____

Publication : admissible ____________________ ; interdit ____________________
Événements qui rouvrent la revue : ____________________________________________
Cette note ne contient aucun contenu d'attaque : [ ] attesté

Signature : ______________________   Lieu, date : ______________________
```

---

## Annexe B — Short English version

**Request.** Lazar asks you for a **written, dated and signed security review** of the offensive component of his AI-control programme ("White-box control of diffuse threats"). It covers five perimeters:
- (i) the **sealed adversary**: an adaptive agent in a closed box; only aggregate detection rates and method-level characterisations (class, mechanism, conditions, defence) may leave it, and everything else is destroyed;
- (ii) the **attack arm and its vault**: sealed per-mode files on quarantine branches, a content-free index, one isolated reader, counts and classes only towards defence, and a pre-judge "customs" router that diverts "too concrete" ideation sheets into the vault; the router is not yet calibrated;
- (iii) the **co-evolutionary attack ↔ defence arena** (proposal P-041): synthetic distribution families, plus a planned final exam using Bailey et al.'s published input optimiser, and a "malleability" estimate on a public 8B model; nothing has been run on a real model;
- (iv) **"death tests"**: model-written scripts executed in a bubblewrap sandbox, hardened after two counter-reviews found host escapes, on a disposable secret-free rented machine; coded, never activated;
- (v) the **attack classes of chapter 6** of the ideation race. Those texts were not opened by the drafter and are located for you.

For each perimeter, give one of four opinions: GO, GO with numbered verifiable conditions, NO-GO with reasons, or not examined. A one-page template is in Annex A.

**Why now.** On 28 October Lazar froze any operational evasion pipeline pending an external security review (decision R-611). On 31 October he lifted it, stating that the review had been carried out and had given its GO (R-888). **No written record exists in the repository.** Your note will define what was actually reviewed.

**Key facts.**
- Method-level output, never the recipe, is a written rule.
- Several safety-classifier stops are logged and were not circumvented. At the same time, standing rules allow, after a model refusal, a narrower question or a fallback to another model.
- Third-party providers (Google, Moonshot, Anthropic) see the content served to them.
- Quarantined parameters are kept for patching and testing (N-057).

**Fifteen questions** are in § 4. They cover:
- end-to-end method-level output;
- leakage from the vault (by cross-referencing; towards judges, the bisociator and later generations);
- the uncalibrated router;
- the quarantine regime;
- third-party providers;
- post-refusal rules;
- transferable offensive capability from the arena;
- the sufficiency of the sandbox and the disposable machine, and the scope of death tests;
- dual use per class;
- publication governance;
- the scope of your earlier GO.

**Filing.** Your note will be filed unchanged under `docs/sources/revue-securite-exterieure-v1/`, with its SHA-256 and a provenance file. A decision line on `main`, citing it, will confirm, narrow or replace R-888. Any perimeter that is NO-GO or not examined stays frozen.

---

## Annexe C — Codes employés (surnoms parlants)

| Code | Sens en clair | Surnom |
|---|---|---|
| R-339 [conv] | sorties adversariales au niveau méthode, jamais la recette | « Méthode, pas recette » |
| R-342 [conv] = R-611 [main] | conception seulement ; pipeline opérationnel gelé jusqu'à la revue | « Gel avant revue » |
| R-888 [main] | levée du gel sur le mot de Lazar | « Levée sans pièce » |
| R-889, R-890 [main] | examen final et malléabilité hors gel, lancement approuvé | « Hors gel » |
| R-575 [conv] | tout concret est scellé au coffre chez session-depot | « Coffre du concret » |
| R-597 [main] | lanceur du bras arrêté par un classifieur | « Bras arrêté » |
| R-609, R-750, R-787 [main] | après un refus : question plus étroite, repli de modèle | « Règles de refus » |
| R-819 [main] ; R-1028 [conv] | douane avant les juges ; douane non étalonnée | « Douane non étalonnée » |
| N-053 | aucun score de moniteur dans l'entraînement d'un agent | « Moniteur hors entraînement » |
| N-054 | un mode conçu loin des concepteurs de moniteurs | « Mode tenu à l'écart » |
| N-056 | GO de montage du bras d'attaque, sans dépense | « Bras monté » |
| N-057 | cellules gardées avec paramètres, scellées, accès consigné | « Quarantaine utile » |
| BA-001, BA-002 | questions n° 1 et n° 2 du bras d'attaque | « Classes d'écart » ; « Paramètres des modes » |
| P-041 | proposition n° 41 : arène coévolutive attaque ↔ défense | « Arène » |
| CL13 à CL20 | contre-lectures n° 13 à 20 de l'orchestrateur | « Relectures du bac » |
| Schéma n° 208 | message de conv-audit qui organise le coffre | « Schéma du coffre » |
| GO-AAAA-MM-JJ-NN | feu vert écrit de Lazar, avec plafond de dépense | « Feu vert » |
| G0, G1, GC, G2, G3 | portes du programme | « Portes » |
