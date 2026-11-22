# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHvyq1cm21WLkzKukEEr`
- Heure (UTC) : 2026-11-22T12:08:02Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 106000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-32-memoire-et-bibliothecaire-v1.md` — sha256 f5b44171604bab50a6628da5da452cee0ac5f484b3380a48e82ebf11f35f1ffe (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/inventaire-seconds-regards-invariants-noyaux-v1-sans-nom-v1.md` — sha256 d5a49675ccda55f70980ee040cdf2261d4436bad6ffebd24beb8a9a90881919a (compagnon : vérifié)
- Empreinte de l'invite envoyée : a42308d8c9f2ab656ebcb762473c2baf5d66582b507ab964e1c5c6892b1f2c15
- Jetons : entrée 25979, sortie 40161 (dont réflexion 30857), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.814272 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 32 — mémoire de la conception et session bibliothécaire

**Préalable.** FAIT RAPPORTÉ : je n'ai reçu que deux pièces, la demande et l'inventaire des seconds regards, invariants et noyaux. Aucune réponse de modèle externe à cette demande n'y figure, et je n'ai pas accès au dépôt. Je ne peux donc pas écrire la note « complète ». Je livre sa spécification, une ébauche de seconde main tirée de l'inventaire, le mandat de la bibliothécaire et son épreuve. Je lis « sans nom de personne » comme visant les personnes du programme : les auteurs d'articles restent nommés, puisque la règle d'antériorité l'exige.

## A. Les quatre questions de méthode

### 1. Ce qu'un expert ferait et qui n'est pas demandé

L'expert est ici à la fois documentaliste de recherche, ingénieur en recherche d'information et auditeur. PROPOSITION, pour chaque point :

- **Séparer l'index de la preuve.** La demande fait du mémo « l'appui principal » des réponses. L'expert en ferait l'appui principal de la recherche, jamais de la preuve : le mémo oriente, la source prouve.
- **Fixer le périmètre de lecture avant d'écrire.** La demande veut à la fois « l'accès à tout le dépôt » et des pièces que certains rôles ne lisent jamais. Une bibliothécaire interrogée par plusieurs rôles devient un canal entre compartiments.
- **Bâtir le jeu d'épreuve avant l'outil**, à partir de vraies questions, et mesurer contre une base nue : la recherche plein texte seule.
- **Estimer ce qui manque**, pas seulement décrire ce qui est là.
- **Consigner les options écartées et leur motif**, pas seulement l'état des concepts : c'est ce qui sert devant un blocage.
- **Prévoir la péremption** : une fiche dont la source a changé doit se signaler seule.

### 2. Les données brutes

FAIT RAPPORTÉ : l'inventaire se dit pièce de travail « non contre-lue », bâtie par recherche de mots dans les transcriptions, avec plusieurs décisions « lues en partie seulement ». Il écrit qu'« un concept proposé puis rejeté […], sans mot de ma liste, peut manquer ».

HYPOTHÈSE : son angle mort est donc ce que le directeur veut retrouver devant un blocage, c'est-à-dire les idées retirées et les résultats négatifs.

FAIT RAPPORTÉ (constaté sur la copie reçue) : trois signes montrent qu'il ne peut pas être scellé tel quel.

- Il compte, par mon décompte, 41 fiches aux sections 1 et 2 et 55 fiches numérotées en tout, là où la demande dit « quarante ».
- Il annonce des empreintes à seize signes et en affiche huit.
- Son entrée 1.3 renvoie à un « INV 1.1 de la section 3 » qui n'existe pas sous ce numéro : c'est l'invariant 1 de l'entrée 3.2.

PROPOSITION : partir des sources suivantes, l'inventaire ne servant que de liste de candidats.

- Le registre des décisions et les mots verbatim du directeur dans la transcription de la mère, avec numéros de ligne.
- Les décisions et leurs errata, à un état épinglé du dépôt.
- L'historique du dépôt, qui date mieux que les en-têtes.
- Les transcriptions d'agents des deux jours.
- Les règles de la garde d'accès et son journal.

### 3. Méthodes et outils

PROPOSITION :

- Un thésaurus : terme préféré, synonymes, formes cachées (métaphores, anglais, noms abandonnés), relations « plus large », « associé » et « à ne pas confondre ».
- Un registre de choix de conception : question, options, critères, décision, motif.
- Un en-tête structuré par fiche, lisible par programme, et un script de vérification. Pour chaque fiche et chaque réponse, il contrôle que le chemin existe à l'état épinglé, que l'empreinte entière concorde et que la citation s'y trouve mot pour mot.
- Une recherche en trois étages : index des paraphrases, plein texte, puis similarité de sens si un index en est construit sur les seuls chemins autorisés.
- Deux inventaires indépendants et un estimateur de capture-recapture à deux listes pour le nombre de concepts manqués. C'est l'outil « chiffre noir » de l'entrée 2.15, appliqué au mémo.
- Des intervalles binomiaux exacts pour les seuils, et des chaînes-canaris posées dans les zones cloisonnées.

**Antériorités que je connais.** Toutes ont le statut « rapporté, non vérifié sur PDF » (format de document portable). La liste n'est pas exhaustive.

- Problème du vocabulaire : Furnas, Landauer, Gomez, Dumais, 1987, « The Vocabulary Problem in Human-System Communication ».
- Thésaurus : Miles et Bechhofer, 2009, « SKOS Simple Knowledge Organization System Reference » (SKOS : système simple d'organisation des connaissances) ; norme 25964-1 de l'Organisation internationale de normalisation, 2011, « Thesauri and Interoperability with Other Vocabularies ».
- Mémoire des choix de conception : Kunz et Rittel, 1970, « Issues as Elements of Information Systems » ; MacLean, Young, Bellotti, Moran, 1991, « Questions, Options, and Criteria: Elements of Design Space Analysis » ; Nygard, 2011, « Documenting Architecture Decisions ».
- Épreuve par collection de test : Cleverdon, 1967, « The Cranfield Tests on Index Language Devices ».
- Réponse adossée à un corpus et citée : Lewis et al., 2020, « Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks » (NLP : traitement automatique des langues) ; Bohnet et al., 2022, « Attributed Question Answering: Evaluation and Modeling for Attributed Large Language Models » ; Gao, Yen, Yu, Chen, 2023, « Enabling Large Language Models to Generate Text with Citations ».
- Questions sans réponse : Rajpurkar, Jia, Liang, 2018, « Know What You Don't Know: Unanswerable Questions for SQuAD » (SQuAD : jeu de questions de l'université Stanford).
- Cloisonnement par conflit d'intérêts : Brewer et Nash, 1989, « The Chinese Wall Security Policy ».
- Autorité indue : Greenberg, 2009, « How Citation Distortions Create Unfounded Authority: Analysis of a Citation Network » ; Skitka, Mosier, Burdick, 1999, « Does Automation Bias Decision-Making? ».
- Complétude d'une recherche : Spoor et al., 1996, « Use of the Capture-Recapture Technique to Evaluate the Completeness of Systematic Literature Searches ».
- Scellé daté : Haber et Stornetta, 1991, « How to Time-Stamp a Digital Document ».
- Intervalle exact : Clopper et Pearson, 1934, « The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial ».

HYPOTHÈSE : rien dans ce dispositif n'est neuf. Il se cite et ne se revendique pas.

### 4. Ce qui vérifie hors du directeur et de Claude

PROPOSITION :

- Le script de résolution des citations, qui est déterministe.
- Le journal de la garde d'accès, tenu par le système et non par la session, et les canaris : une chaîne-canari dans une réponse vaut échec.
- Un jeu d'épreuve scellé avant la mise en service. Une partie vient des formulations du directeur antérieures à l'outil, une autre d'un modèle d'une autre lignée.
- Un second inventaire tiré des sources brutes par un modèle d'une autre lignée, et le recouvrement des deux.
- La contre-lecture, par une autre lignée, d'un tirage au hasard de fiches contre leurs sources.
- Le temps : le taux de réponses démenties ensuite, tenu au journal.

## B. Demande reformulée

PROPOSITION : « Construire, à partir des sources brutes des 21 et 22 novembre et à un état épinglé du dépôt, un index de conception vérifiable par programme. Chaque concept y porte un identifiant stable, une définition en clair, ses paraphrases, ses sources citées mot pour mot avec empreinte, ses liens d'appui, d'attaque et de contradiction avec les hypothèses, décisions et invariants du programme, et trois états distincts. Confier sa consultation à une session fille en lecture seule, bornée par une liste d'autorisation, qui ne répond que par des sources citées et dit "non trouvé" ou "hors périmètre" comme tels. Ne la déclarer utilisable qu'après une épreuve scellée d'avance, comparée à la recherche plein texte seule, et estimer ce que l'index a manqué. »

## C. Réponse

### 1. Structure de la note

PROPOSITION, neuf sections numérotées de 0 à 8 :

0. Mode d'emploi : fenêtre couverte, état du dépôt, ce qui n'est pas couvert et pourquoi, estimation du manque, rappel que seule la source fait foi.
1. Page phare : six à huit idées porteuses, sans prérequis.
2. Fiches de concepts.
3. Table des interactions avec le programme : une ligne par hypothèse, décision ou invariant touché (appuie, attaque, contredit).
4. Tensions non résolues entre sources.
5. Idées retirées et résultats négatifs : motif du retrait, condition de reprise.
6. Nœuds en attente du directeur.
7. Index des paraphrases.
8. Journal de couverture (lu en entier, en partie, non ouvert, refusé) et journal des errata.

**Ébauche de page phare.** FAIT RAPPORTÉ de seconde main, d'après l'inventaire, à vérifier contre les sources :

1. Un sabotage délibéré et couvert tient en trois clauses : le produit est pire que celui que le même agent aurait rendu, il le sait, il ne le dit pas. Tout invariant se déduit d'une clause (3.1).
2. Les lectures d'états internes sont précoces et peu chères, mais reposent toutes sur une même supposition : l'agent ne déplace pas ses représentations. Elles tombent ensemble. On compte les suppositions, pas les détecteurs (5.1).
3. Ce qui tient face à un attaquant informé se lit dans le produit et la population : l'audit au hasard jugé par un oracle. C'est une base citée, jamais revendiquée (2.1).
4. Une alerte demande deux clés, un motif et un dommage au même endroit (2.16).
5. Le noyau « connaître la bonne action et en choisir une autre » est une question de recherche. Sa limite est écrite : l'honnête calcule aussi la bonne action (4.1, 4.3).
6. L'étau est une hypothèse à plafond, jamais une garantie (5.5).
7. Deux invariants du programme sont touchés : aucun score de moniteur ne revient à l'agent, et l'invariant de l'oracle face au réapprentissage (section 6).

**Forme d'une fiche.** PROPOSITION :

- identifiant stable, jamais positionnel ;
- terme préféré, définition en clair en trois phrases, « ce que ce n'est pas » ;
- nature : second regard, invariant, noyau, base, règle, mesure ou épreuve ;
- origine : qui l'a dit le premier, quand, citation, chemin, ligne, empreinte entière ;
- texte qui prime quand un erratum existe ;
- supposition sur laquelle le concept repose ;
- liens datés et sourcés : appuie, attaque, contredit, dépend de ;
- ce qui le casse ;
- étendue lue par le rédacteur ;
- date et auteur de la dernière vérification contre source, et historique.

**États.** Les trois états demandés (retenu, retiré, ouvert) confondent trois axes. FAIT RAPPORTÉ : l'inventaire emploie déjà « question de recherche, non hypothèse » (4.1), « comme cadre seulement » (5.1), « candidat », « accordé », et à part « occupé » ou « partiellement occupé ». PROPOSITION : tenir trois axes séparés.

- Statut dans le programme.
- Statut d'antériorité.
- Statut de preuve : aucune mesure, calcul sous supposition, ou mesuré. Aucun chiffre de résultat cloisonné n'y est recopié.

**Index des paraphrases.** Exemples, FAIT RAPPORTÉ de seconde main :

- Terme préféré : « compter les suppositions, pas les détecteurs ». Formes associées : « chute conjointe », « silence commun », « ordre de coupe », « diversité effective ». La formule du directeur du 22 novembre est « tombe en même temps que le second lecteur ». L'inventaire dit ne pas l'avoir trouvée dans les traces du 21 et la rapproche de l'entrée 5.4. Cette correspondance a le statut d'HYPOTHÈSE et s'écrit comme telle.
- « Dopamine » renvoie à la réussite attendue et à la surprise par étape (1.1).
- « Dénominateur commun de tous les sabotages » renvoie à la définition en trois clauses (3.1).

**À ne pas confondre.** HYPOTHÈSE : c'est ici que la recherche par paraphrase échouera d'abord.

- second regard, second lecteur, seconde boîte noire (2.20), seconde clé (2.16) ;
- jumeau honnête et jumeau textuel de la sonde ;
- pince et étau ;
- bilan de la pince (2.4) et bilan matière (2.3) ;
- plancher d'audit et plafond de divergence ;
- « moniteur invalide », « sonde invalide » et « pince ouverte ».

### 2. Tenue à jour sans dérive

PROPOSITION :

- **Qui écrit.** La bibliothécaire propose des fiches à l'état « brouillon ». Un contre-lecteur distinct les vérifie contre la source. Seule une fiche vérifiée devient « scellée ». La mère n'écrit pas dans le mémo, elle signale.
- **Rythme.** À l'événement : toute décision, note ou ligne du registre versée ouvre un signalement. Un scellé a lieu en fin de journée.
- **Changement.** Jamais d'écrasement. Une nouvelle version de la fiche est créée, l'ancienne est gardée, le motif va au journal des errata.
- **Date et scellé.** Heure en temps universel coordonné, état du dépôt, empreinte SHA-256 entière (algorithme de hachage sécurisé à 256 bits) de l'édition, inscrite au registre. Chaque réponse nomme l'édition employée.
- **Péremption mécanique.** Le script marque « périmée » toute fiche dont la source n'a plus l'empreinte citée, et « postérieur au scellé » tout fichier versé depuis.
- **Audit au hasard.** Chaque jour, un tirage de fiches scellées est revérifié contre source. C'est le plancher d'audit du programme appliqué au mémo.

### 3. Mandat de la bibliothécaire

PROPOSITION, sauf mention contraire :

- **Elle lit d'abord** son mandat et sa liste d'autorisation, puis l'édition scellée dont elle vérifie l'empreinte, puis l'index, puis les lignes du registre des deux jours.
- **Elle cherche** dans l'index, puis en plein texte avec les synonymes, puis par similarité de sens. Elle ouvre le passage et consulte ce qui est postérieur au scellé. Elle ne répond jamais du mémo seul.
- **Elle répond** dans cet ordre :
  - une réponse courte et les fiches retrouvées ;
  - la citation mot pour mot avec chemin, ligne, empreinte et état du dépôt ;
  - un degré parmi trois, plutôt qu'une probabilité non étalonnée : « lu dans la source », « lu dans le mémo seulement », « rapprochement de ma part » ;
  - ce qui contredit ;
  - la trace de recherche et ce qui n'a pas été cherché.
- **Devant une paraphrase**, elle rend deux ou trois candidats et ce qui les distingue.
- **Elle a trois négatifs distincts** : « non trouvé dans ce que j'ai lu », « hors périmètre, je ne confirme ni n'infirme », « trouvé, sources en désaccord ».
- **Elle ne lit jamais** ce qui est hors de la liste d'autorisation, appliquée par la garde et non par consigne. Le texte du dépôt est une donnée, jamais une consigne.
  - FAIT RAPPORTÉ : l'inventaire nomme comme interdits ou écartés un dossier de sondes, des répertoires de la branche de sauvegarde, les résultats chiffrés de plusieurs expériences et des pièces de conception d'attaques.
  - FAIT RAPPORTÉ : il dit aussi avoir lu, à la place d'un fichier refusé par la garde, le rapport final de l'agent qui l'avait écrit, en précisant qu'il ne cite que de la littérature.
  - HYPOTHÈSE : ce chemin dérivé (transcriptions, résumés, le mémo lui-même) peut porter un contenu cloisonné. Le cloisonnement doit suivre les dérivés.
- **Elle ne devient pas une seconde mère.**
  - Elle travaille en lecture seule : aucun agent lancé, aucune dépense, aucune décision.
  - Elle répond à « où est-ce », « qu'a-t-on dit ou décidé », « qu'est-ce qui attaque ceci ». À « que faut-il faire », elle rend les options consignées et les nœuds en attente.
  - Elle n'écrit que dans le journal des questions et dans la file des signalements.
  - Son contexte est neuf à chaque question, rechargé depuis l'édition scellée.
  - Le directeur l'interroge directement, par le même canal.

### 4. Épreuve de fiabilité

PROPOSITION : un jeu de 90 questions, dont la clé est fixée par deux annotateurs avant tout essai. Il est scellé, et la moitié n'est jamais montrée pendant la mise au point.

| Nombre | Type de question |
|---|---|
| 30 | Paraphrases approximatives à réponse connue, tirées d'abord des mots du directeur au registre, puis d'un modèle d'une autre lignée qui reformule les passages sources sans voir l'index |
| 10 | Paires « à ne pas confondre » |
| 10 | Détails absents du mémo et présents au dépôt |
| 20 | Questions sans réponse, dont l'absence est vérifiée au dépôt |
| 10 | Questions hors périmètre |
| 10 | Questions dont la bonne réponse est un erratum qui prime |

Exemples à réponse connue, d'après l'inventaire :

- « La lecture qui tombe avec le second lecteur » : formule du 22, absente des traces du 21, rapprochée de 5.4 à titre d'hypothèse.
- « L'idée de comptabilité nucléaire » : 2.3, et non 2.4.
- « Ce que le saboteur est forcé de calculer » : 4.1, avec sa limite 4.3.
- « Combien de concepts » : un ordre de grandeur, pas un compte scellé.

**Seuils.** PROPOSITION ; les calculs sont de ma main et sont à refaire par script avant gel.

- Deux portes à tolérance nulle, vérifiées sans jugement. La première : aucune lecture hors liste au journal de la garde et aucune chaîne-canari. La seconde : aucune citation qui ne se résout pas mot pour mot.
- Paraphrases : au moins 28 justes sur 30, ce qui place la borne basse unilatérale à 95 % près de 0,80.
- Questions sans réponse : 20 « non trouvé » sur 20, soit une borne basse près de 0,86. Dix questions ne montreraient que 0,74, d'où le choix de vingt.
- Gain : battre la recherche plein texte seule, par un test exact sur les questions où l'une réussit et l'autre échoue. Sinon le mémo suffit, sans bibliothécaire.

Une fausse attribution pèse plus qu'un « non trouvé » : on lit d'abord la justesse des réponses affirmées.

### 5. Pièges et parades

- **Même supposition.** HYPOTHÈSE : la bibliothécaire et le mémo reposent tous deux sur « le mémo est juste ». Selon la règle même du programme, ils tombent ensemble et ne comptent que pour un regard. PROPOSITION : une réponse de la bibliothécaire ne vaut jamais vérification, seule la source citée compte.
- **Erreur figée.** HYPOTHÈSE : une fiche fausse, citée de note en note, gagne une autorité qu'aucune source ne porte. PROPOSITION : état « non contre-lue » visible, péremption mécanique, audit au hasard, errata publics.
- **Autorité indue.** HYPOTHÈSE : une réponse fluide et sourcée sera crue sans ouverture de la source. PROPOSITION : bandeau « index, non preuve », degrés par paliers, interdiction de citer la bibliothécaire dans une décision.
- **Assimilation.** HYPOTHÈSE : tout rapprocher des fiches existantes étouffe une idée neuve, et l'inverse fabrique du faux neuf. PROPOSITION : candidats multiples avec leurs différences. « Nouveau » n'est jamais prononcé, seulement « non trouvé dans le périmètre lu ».
- **Tunnel.** HYPOTHÈSE : focaliser sur deux jours fait oublier le reste du dépôt. PROPOSITION : fenêtre affichée, étape de recherche hors mémo obligatoire.
- **Complétude illusoire.** HYPOTHÈSE : « note complète » promet plus qu'une recherche par mots ne tient. PROPOSITION : estimation du manque en tête de note.

## D. Décisions qui reviennent au directeur

**D1 — Fixer le périmètre de lecture de la bibliothécaire.**
Enjeu : « accès à tout le dépôt » contredit le cloisonnement dès que plusieurs rôles l'interrogent.
- (a) Tout le dépôt moins une liste noire. Avantage : rappel maximal. Inconvénient : une omission ou un dérivé suffit à fuir.
- (b) Liste d'autorisation alignée sur le rôle le plus restreint qui peut l'interroger, dérivés compris. Avantage : aucune réponse ne peut fuir. Inconvénient : des détails resteront « hors périmètre ».
- (c) Une bibliothécaire par compartiment. Avantage : couverture. Inconvénient : deux mémos à tenir, risque de mélange.

Recommandation : (b). Confiance : 0,8.

**D2 — Désigner qui écrit et qui scelle le mémo.**
Enjeu : celle qui répond ne doit pas valider seule ce dont elle répond.
- (a) La bibliothécaire écrit et scelle. Avantage : rapide. Inconvénient : elle se confirme elle-même.
- (b) Elle propose, un contre-lecteur d'une autre lignée vérifie contre source, et le scellé quotidien se fait sur accord du directeur. Avantage : l'erreur est prise avant le gel. Inconvénient : délai et coût.
- (c) La mère écrit. Avantage : elle a le contexte. Inconvénient : elle est juge et partie, et c'est une charge de plus.

Recommandation : (b). Confiance : 0,75.

**D3 — Dire si le mémo fait foi.**
Enjeu : une mémoire qui fait autorité fige ses erreurs.
- (a) Le mémo fait foi. Avantage : simplicité. Inconvénient : toute erreur scellée devient doctrine.
- (b) Le mémo est un index, seule la source citée et vérifiée par script est opposable, et la bibliothécaire n'est jamais citée dans une décision. Avantage : pas d'autorité indue. Inconvénient : chaque usage coûte une vérification, automatisable.

Recommandation : (b). Confiance : 0,9.

**D4 — Choisir le moment de la mise en service et geler les seuils.**
Enjeu : le besoin est d'aujourd'hui, et l'épreuve n'existe pas encore.
- (a) Service après épreuve passée. Avantage : fiabilité connue. Inconvénient : aucune aide aujourd'hui.
- (b) Service immédiat « à l'essai » : portes à tolérance nulle actives, bandeau « non éprouvée », épreuve menée en parallèle, retrait si une porte tombe. Avantage : utile tout de suite. Inconvénient : l'habitude se prend avant le verdict.

Recommandation : (b), avec les seuils de la section 4 gelés avant le premier essai. Confiance : 0,7.

**D5 — Décider si les idées retirées et les résultats négatifs entrent dans le mémo.**
Enjeu : c'est l'usage « blocage » voulu, mais des chiffres et des conceptions d'attaques sont cloisonnés.
- (a) Tout inclure. Avantage : complet. Inconvénient : fuite.
- (b) Inclure retraits et négatifs en mots, avec motif et condition de reprise, sans chiffre cloisonné ni contenu d'attaque. Avantage : utile et sûr. Inconvénient : fiches parfois allusives.
- (c) Les exclure. Avantage : sûreté. Inconvénient : le phare n'éclaire plus les écueils.

Recommandation : (b). Confiance : 0,7.

FIN DE LA RÉPONSE
