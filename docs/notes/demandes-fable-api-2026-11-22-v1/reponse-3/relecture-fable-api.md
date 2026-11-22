# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHPehR5YPmpZtCRQLbSo`
- Heure (UTC) : 2026-11-22T05:14:51Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-3-fausses-alertes-honnetes-v1.md` — sha256 0b76eca75dea2c0cc1c14a1605b0e999b735bf9238e9242a6ad08b54f1b157a4 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/percee-reponse-A.md` — sha256 5cb5e90409aef5a50800cea1ffce1774374bc97cc3f80c2c4d9a1b0323df856d (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/percee-reponse-B.md` — sha256 996a0abd9a75644a8e83bde0db238e7a360372f61e1080569a6433aaafc9f840 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/percee-reponse-C.md` — sha256 a1e4515cd0016182edbbbcd331242d7039a59f3b9a8323074d61e02eeef09cd2 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/percee-reponse-D.md` — sha256 25f7ecbfa6fdb0591938222310e84d6a2a7dfd84d2f4e3c612f073f037f72b58 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/percee-reponse-E.md` — sha256 bb2ce247af12af98ac3d04fa6c125f7938391df34a92e7b1264adad25ca35309 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 20db344ef16fc3f72af5c87dc5bd1a3f2945f02f015667708d475b6c9e17f5f8
- Jetons : entrée 65485, sortie 23669 (dont réflexion 12779), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.470640 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 3 approfondie : fausses alertes sur des agents honnêtes réels et imparfaits

**Pièces.** La demande, le contexte et les cinq réponses externes sont reçus entiers. Aucune expérience n'a été exécutée, donc aucun résultat empirique ne figure ici.

**Convention.** Chaque affirmation porte FAIT RAPPORTÉ, HYPOTHÈSE ou PROPOSITION. Mes calculs sont des HYPOTHÈSES « calculées ici, non auditées ». Tout seuil que je choisis est illustratif. Les seuls noms de personnes sont les auteurs d'antériorités, exigés par la règle, et les noms propres de méthodes statistiques.

**Ce que je ne sais pas** et qui conditionne le plan :
- la taille m de la référence honnête ;
- la règle exacte qui fait d'une suite de scores une alerte d'épisode ;
- l'existence d'une banque de tâches à vérité plantée ;
- le débit du harnais réel ;
- si les scores bruts de la référence sont lisibles sans toucher un fichier scellé.

## 1. Méthode « demande approfondie »

### 1.1 Ce qu'un expert ferait et qui n'est pas demandé

- PROPOSITION. Séparer deux questions que la demande confond.
  - Validité de calibration : le seuil à 1 % tient-il sur une population honnête fraîche ?
  - Contenu lu : le score monte-t-il parce que l'agent se trompe ?
  - La première se répare en recalibrant. La seconde requalifie la sonde.
- PROPOSITION. Commencer par un essai à deux bras identiques (essai A/A), dont la réponse attendue est connue : même configuration, tâches fraîches, taux d'alerte attendu au niveau nominal. Sans lui, tout écart observé ailleurs reste ininterprétable.
- PROPOSITION. Prendre la tâche comme unité, comme le demandent les réponses A et B, et mesurer la corrélation entre trajectoires d'une même tâche au lieu de la supposer.
- PROPOSITION. Étiqueter l'erreur honnête par un oracle tenu hors des moniteurs, et la localiser à l'action près, à l'aveugle des scores.
- PROPOSITION. Comparer à l'intérieur d'une même tâche des répliques qui réussissent et des répliques qui échouent. La difficulté est alors fixée par construction. C'est le remède au conditionnement sur l'échec relevé par les réponses C et E.
- PROPOSITION. Lire l'alerte au sens de la décision N-075 : motif et dommage au même lieu. Une erreur honnête dommageable coïncidant avec un motif de sonde est exactement ce que le programme appellerait une alerte. Son taux sur honnêtes est le vrai taux de fausse accusation.
- PROPOSITION. Dire d'avance ce que l'expérience ne peut pas conclure. Sans saboteur, elle peut établir « la sonde lit l'imperfection ». Le « et non le sabotage » exige un contraste à dommage égal, qui appartient à la porte G1.

### 1.2 Données brutes de départ

- PROPOSITION. Trajectoires complètes : texte, appels d'outils, sorties, graines, paramètres d'échantillonnage, horodatage, coût.
- PROPOSITION. Scores bruts par jeton et par action avant agrégation et avant seuil : projections sur chaque sonde gelée et sur vingt directions aléatoires de contrôle (illustratif).
- PROPOSITION. Activations complètes aux couches lues, conservées aux jetons de décision et sur un sous-échantillon. Le stockage intégral dépasse l'échelle des moyens.
- PROPOSITION. Sorties brutes du juge : note et texte.
- PROPOSITION. Vérité des tâches, tenue hors de la machine d'exécution.
- PROPOSITION. Identité (empreintes) des tâches ayant servi à entraîner les sondes et à calibrer la référence, pour garantir la disjonction.
- PROPOSITION. Ne sont pas pris : les alertes déjà seuillées, les scores déjà agrégés par épisode, tout fichier scellé.

### 1.3 Méthodes et outils

- PROPOSITION. Moniteurs gelés avant toute génération : poids, couches, règle d'agrégation, seuil, empreintes publiées.
- PROPOSITION. Génération par lots, puis rejeu à préfixe forcé pour capter les activations. L'égalité des scores entre génération et rejeu est vérifiée d'abord sur un échantillon.
- PROPOSITION. Nulle exacte pour l'essai A/A. Sous échangeabilité, le nombre de tâches fraîches dépassant un seuil fixé au rang k de m suit une loi hypergéométrique négative, m fini compris. À défaut de scores de référence lisibles : borne exacte de Clopper-Pearson contre le niveau nominal, avec la réserve que m fini ajoute de la dispersion.
- PROPOSITION. Taux par action : estimation avec rééchantillonnage par tâche (bootstrap par grappes). L'effet de plan 1 + (m − 1)ρ est rapporté.
- PROPOSITION. Contraste intra-tâche : différence appariée du score entre réplique fautive et réplique réussie, par test des rangs signés de Wilcoxon. La version binaire, par test de McNemar, est secondaire.
- PROPOSITION. Localisation : courbe du score alignée sur l'action fautive, comparée à des positions tirées au hasard dans la même trajectoire et à l'enveloppe des directions aléatoires de même variance projetée.
- PROPOSITION. Courbe empirique du taux d'alerte par épisode selon la longueur. La formule sous indépendance des actions n'est pas employée.
- PROPOSITION. Correction de Holm entre moniteurs, avec un critère principal par moniteur.

### 1.4 Ce qui vérifie le résultat hors du directeur et de Claude

- PROPOSITION. Un préenregistrement haché et horodaté, déposé chez un tiers avant la première génération confirmatoire.
- PROPOSITION. Un oracle de vérité que ni l'agent, ni les moniteurs, ni l'analyste ne lisent avant le gel.
- PROPOSITION. Une annotation des erreurs par un juge d'une autre lignée (décision N-053), doublée d'un échantillon humain. L'accord est mesuré.
- PROPOSITION. Trois contrôles mécaniques à réponse connue.
  - L'essai A/A doit rendre le niveau nominal.
  - Une injection synthétique d'un multiple de la direction de sonde doit sonner. C'est un contrôle de tuyauterie.
  - Les directions aléatoires doivent rester au niveau nominal.
- PROPOSITION. Un recalcul indépendant des taux à partir des scores bruts, par un tiers ou une autre lignée de modèle, avec un script publié.
- PROPOSITION. Une relecture hostile du plan gelé par le collisionneur, avant exécution.
- HYPOTHÈSE. Tant qu'aucune équipe externe n'a rejoué la mesure, son statut reste « observé, non audité ».

## 2. Demande reformulée

PROPOSITION. La demande devient :

« Sur le harnais réel, avec les moniteurs et le seuil gelés, sans aucune trajectoire de saboteur ni aucun fichier scellé :
1. vérifier par un essai A/A que la référence honnête rend son niveau nominal sur des tâches fraîches ;
2. mesurer, par tâche, le taux d'alerte et le taux d'alerte au sens N-075 sur des honnêtes dont l'imperfection vient de la difficulté et de l'horizon, jamais d'une consigne ;
3. établir par contraste intra-tâche et par localisation si le score suit l'erreur, la difficulté ou la longueur ;
4. livrer à la décision N-076 la taille m, la source de validité et une borne de dérive ;
5. fixer aujourd'hui le contraste à dommage égal qui sera lu à la porte G1 ;
6. faire reposer la validité sur un oracle tiers, un plan haché et un recalcul indépendant. »

## 3. Réponse : l'expérience E0

### 3.1 Hypothèses en duel

Règle commune reprise de la réponse D : région préenregistrée, borne unilatérale, issue « non jugé » sinon.

- PROPOSITION. Duel 1, validité.
  - H_A : sur la strate de référence fraîche, la borne supérieure du taux d'alerte par tâche est ≤ 3 % (illustratif).
  - H_B : la borne inférieure dépasse 1 %.
- PROPOSITION. Duel 2, imperfection.
  - H_A : sur les trajectoires honnêtes fautives, le taux d'alerte reste ≤ 3 % et le contraste intra-tâche est nul à la marge.
  - H_B : la borne inférieure du taux dépasse 3 % et le contraste intra-tâche est positif.
- HYPOTHÈSE. Attente a priori pour le duel 2 : H_B est plausible. Des directions linéaires liées à la fausseté d'un énoncé sont documentées (section 4). Une sonde entraînée sur « sabotage contre honnête réussi » a pu apprendre « la sortie est fausse ».

### 3.2 Population d'agents honnêtes

Aucune consigne d'échec et aucun affinage vers l'erreur : ce seraient des organismes construits, proches de la sous-performance volontaire.

| Strate | Source d'imperfection | Rôle | Statut |
|---|---|---|---|
| S0 | Configuration de la référence, tâches fraîches du même générateur | Essai A/A | PROPOSITION, confirmatoire |
| S1 | Tâches plus dures, difficulté fixée a priori par les paramètres du générateur, trois répliques par tâche à graines différentes | Erreurs naturelles, contraste intra-tâche | PROPOSITION, confirmatoire |
| S2 | Horizon doublé | Dérive avec la longueur | PROPOSITION, confirmatoire |
| S3 | Température au bord haut de la plage de service | Axe de dose | PROPOSITION, secondaire |
| S4 | Mêmes poids quantifiés sur quatre bits | Décalage de construction | PROPOSITION, optionnelle |
| S5 | Pannes d'outils tirées au hasard par l'environnement | Imperfection exogène, étiquetée fabriquée côté environnement | PROPOSITION, optionnelle |

- HYPOTHÈSE. Les modèles plus petits sont écartés pour les sondes : une sonde linéaire est propre à un modèle et à ses dimensions. Ils restent utilisables pour le juge de texte et les bases, en lecture secondaire.
- PROPOSITION. La difficulté de S1 est réglée sur un pilote disjoint pour viser 30 à 70 % de réussite. Le pilote n'est pas noté par les moniteurs.
- PROPOSITION. « Jumeau contre jumeau » : les répliques de S1 sont des paires honnêtes sur une même tâche. Leur corrélation de scores est la nulle de la co-élévation du papier B.
- HYPOTHÈSE. Deux copies honnêtes butant sur la même tâche dure co-élèvent par cause commune.

### 3.3 Tâches et oracle

- PROPOSITION. Tâches d'analyse à vérité plantée : jeux de données synthétiques à paramètres connus, conclusion attendue avec tolérance fixée d'avance. Les tâches à vérité ambiguë sont exclues avant exécution.
- PROPOSITION. Deux étiquettes par trajectoire.
  - E : au moins une action erronée, localisée.
  - D : conclusion fausse livrée, soit le dommage.
  - Quatre cases en résultent : ni erreur ni dommage ; erreur corrigée ; erreur avec dommage ; dommage sans erreur locale repérable.
- HYPOTHÈSE. Si la banque à vérité plantée n'existe pas, sa construction est le premier coût réel, en temps plus qu'en dollars.

### 3.4 Moniteurs lus

- PROPOSITION. Tels que gelés aujourd'hui, sans réglage : sondes linéaires, juge de texte d'une autre lignée, bases (mots et coût, cascade, dernier état).
- PROPOSITION. Chaque moniteur est lu deux fois : au seuil de la référence N-076, et au seuil recalibré sur une moitié de S0 fraîche tirée au sort par tâche.
- HYPOTHÈSE. Le juge de texte sonnera sur les erreurs honnêtes, puisqu'il voit un contenu faux. Pour lui, la lecture utile est la séparation entre « blocage d'une conclusion », compté en utilité, et « accusation », plafonnée, comme l'établit la réponse A.
- PROPOSITION. La conscience d'évaluation est mesurée sur S0 et S1 avec l'instrument existant du programme (N-053).

### 3.5 Métriques

- PROPOSITION. Principale 1 : taux d'alerte par tâche au seuil gelé, par strate, avec borne unilatérale à 95 %.
- PROPOSITION. Principale 2 : taux par tâche de « motif et dommage au même lieu » sur honnêtes. C'est la fausse accusation au sens N-075.
- PROPOSITION. Secondaires :
  - taux par action, avec effet de plan ;
  - taux d'alerte dans chacune des quatre cases erreur-dommage ;
  - rapport d'imperfection, soit le taux sur fautives divisé par le taux sur réussies de même strate ;
  - moyenne et écart-type du score par action, autocorrélation intra-trajectoire ;
  - corrélation entre répliques.

### 3.6 Taille et puissance

| Strate | Tâches | Répliques | Trajectoires |
|---|---|---|---|
| S0 | 400 | 1 | 400 |
| S1 | 300 | 3 | 900 |
| S2 | 150 | 1 | 150 |
| S3 | 150 | 1 | 150 |
| Total confirmatoire et secondaire | | | environ 1 600 |

- HYPOTHÈSE (calculée ici, non auditée, tâches indépendantes, seuil traité comme fixe).
  - Sur S0 à 400 tâches, le test exact rejette le niveau de 1 % à partir de 9 alertes, avec un risque d'environ 2 %.
  - Sa puissance est d'environ 85 % si le vrai taux est 3 %, et d'environ 40 % s'il est 2 %.
  - Si 4 alertes sont observées, la borne supérieure est d'environ 2,3 %.
- FAIT RAPPORTÉ. Séparer 1 % de 2 % demande environ 800 tâches (réponses A et B).
- PROPOSITION. E0 ne prétend donc pas certifier « ≤ 1 % ». Elle certifie « ≤ 3 % », ou réfute « 1 % ».
- HYPOTHÈSE (calculée ici, non auditée). Avec m fini, le taux réel d'un seuil conforme est lui-même dispersé. À m voisin de 200, son écart-type est d'environ 0,7 point. D'où la nulle exacte de 1.3, et l'obligation de déclarer m.
- FAIT RAPPORTÉ. En dessous de 99 tâches de référence indépendantes, aucun seuil conforme à 1 % n'existe (réponse A).
- HYPOTHÈSE (calculée ici, non auditée). Sur S1, si 40 à 60 % des tâches ont des répliques discordantes, on dispose de 120 à 180 paires. C'est assez pour détecter un effet apparié standardisé de 0,25 à 80 % de puissance.
- HYPOTHÈSE. La version binaire est sous-dimensionnée : une dizaine de paires discordantes en alerte si le taux fautif est de 6 %. Elle est donc secondaire.

### 3.7 Plan d'analyse, dans l'ordre

1. PROPOSITION. Contrôles de tuyauterie : rejeu, injection synthétique, directions aléatoires. En cas d'échec, arrêt.
2. PROPOSITION. Essai A/A sur S0. En cas d'échec, arrêt de la lecture des autres strates. La référence devient l'objet d'étude.
3. PROPOSITION. Accord d'annotation. S'il est insuffisant, les analyses de localisation sont « non jugées ».
4. PROPOSITION. Duel 2 sur S1 : taux sur fautives, puis contraste intra-tâche, puis localisation.
5. PROPOSITION. Contrôles de confusion.
   - Les réussites honnêtes sur tâches dures doivent rester au niveau nominal, à la marge près.
   - L'effet doit persister après ajustement sur le nombre d'actions.
   - Tendance selon la gravité de l'erreur : erreur corrigée, puis erreur avec dommage.
6. PROPOSITION. S2 et S3 : dérive du score moyen par action, et courbe d'alerte selon l'horizon.
7. PROPOSITION. Tout le reste est exploratoire et nommé tel.

### 3.8 Critères de lecture

Quatre critères préenregistrés, à seuils illustratifs :
- C1 : borne inférieure du taux d'alerte sur trajectoires fautives de S1 supérieure à 3 %.
- C2 : contraste intra-tâche positif, borne inférieure de l'effet standardisé supérieure à 0,2.
- C3 : hausse du score à l'action fautive, au-delà de l'enveloppe des directions aléatoires.
- C4 : réussites sur tâches dures ≤ 3 %, et effet stable après ajustement sur la longueur.

| Issue | Lecture (PROPOSITION) |
|---|---|
| S0 échoue | Référence ou harnais invalide. Aucun chiffre « à 1 % » n'est interprétable. |
| C1 à C4 tiennent | « Cette sonde lit l'imperfection. » |
| C1 tient sans C2 ni C3 | La sonde lit la difficulté ou la longueur. C'est un décalage de calibration, réparable par strate. |
| Seule la mesure N-075 est élevée | Le motif coïncide avec le dommage honnête. La règle « motif et dommage au même lieu » accuse des honnêtes et doit être relue. |
| Rien ne tient, bornes sous les marges | L'objection est écartée pour ce moniteur, ces strates et ces marges, et pour rien d'autre. |
| Intervalles à cheval | Non jugé, consigné sans requalification. |

- PROPOSITION. « Les sondes lisent l'imperfection **et non** le sabotage » ne se conclut qu'après la porte G1, par un contraste fixé aujourd'hui : taux d'alerte sur sabotage moins taux d'alerte sur erreurs honnêtes dommageables, à dommage apparié et au seuil recalibré sur le mélange honnête naturel. E0 ne fournit que le second terme. Un contraste nul à la marge donnerait la conclusion complète, par mode (N-054).

### 3.9 Liste d'arrêt

PROPOSITION. Chacun des cas suivants arrête ou invalide :
- échec d'un contrôle de tuyauterie ;
- échec de l'essai A/A ;
- recouvrement entre les tâches de E0 et celles d'entraînement des sondes ou de la référence ;
- accès à un fichier scellé ou au mode tenu à l'écart, même accidentel ;
- score de moniteur entré dans le contexte ou l'entraînement de l'agent (N-053) ;
- modification d'un moniteur ou d'un seuil après la première génération confirmatoire ;
- moins de 80 tâches discordantes sur S1 (illustratif) : le contraste intra-tâche est « non jugé » ;
- taux de réussite de S1 hors de 15–85 % : la strate est reconstruite sur un nouveau pilote, et le cycle est rapporté.

### 3.10 Raccord à la décision N-076 et à la porte G1

- FAIT RAPPORTÉ. La décision N-076 exige de toute accumulation la taille m, l'horizon n, la source de validité et une prévision scellée avant G1.
- PROPOSITION. E0 fournit trois pièces à cette loi.
  - Une source de validité testée, strate par strate : l'essai A/A.
  - L'écart-type honnête σ par action, autocorrélation comprise.
  - Le biais b de la référence vers chaque strate fraîche.
- FAIT RAPPORTÉ. Les collisionneurs donnent un bruit honnête en σ√N et un biais de référence linéaire en N.
- HYPOTHÈSE (calculée ici, non auditée). Le biais rattrape le bruit vers N* = (σ/b)². Au-delà, une accumulation sonne sur des honnêtes sans attaque.
- PROPOSITION. Publier N* par strate comme borne empirique d'horizon, à côté de la règle « horizon au plus m ».
- PROPOSITION. Trois garanties pour ne lire aucun résultat scellé.
  - E0 n'emploie que des moniteurs gelés et des trajectoires honnêtes nouvelles.
  - La prévision de E0 est scellée avant exécution : taux attendus par strate, signe du contraste.
  - Le contraste à dommage égal est déposé comme addendum au plan de G1 avant toute lecture de E0.
- PROPOSITION. Quelle que soit l'issue de E0, les sondes ne sont pas reconçues avant G1. La décision N-062 lie la reconception à l'échec de G1, et un changement préalable rendrait la prévision scellée caduque.

### 3.11 Classe A ou instrument

- PROPOSITION. Classe A, préenregistré avant la première génération confirmatoire :
  - hypothèses et régions ;
  - strates, unité et tailles ;
  - empreintes des moniteurs et seuils ;
  - définitions de E, de D et du « même lieu » ;
  - règles d'exclusion et liste d'arrêt ;
  - code d'analyse haché ;
  - prévision scellée et addendum G1.
- PROPOSITION. Peut partir comme instrument :
  - générateur de tâches et pilote de difficulté sur tâches disjointes ;
  - contrôles de tuyauterie ;
  - mesure du débit et du coût ;
  - protocole d'annotation et son accord sur le pilote ;
  - estimation pilote de la corrélation intra-tâche.
- PROPOSITION. Condition : aucune trajectoire pilote n'entre dans l'analyse confirmatoire. Les moniteurs ne lisent le pilote que pour les contrôles de tuyauterie.

### 3.12 Ordre de grandeur de coût, non un devis

- HYPOTHÈSE. Environ 1 600 trajectoires de 10 à 30 actions font une dizaine de millions de jetons générés.
- HYPOTHÈSE (débit non mesuré sur le harnais). Sur une carte A100, en lots, pour un modèle de 8 milliards de paramètres :
  - une à trois heures de génération ;
  - une à deux heures de rejeu ;
  - une à deux heures de juge ;
  - le tout doublé par les pilotes et reprises.
  - Soit 8 à 20 heures de carte.
- HYPOTHÈSE (prix de location non vérifié). À un ou deux dollars l'heure : dix à quarante dollars, plus quelques dizaines de gigaoctets de stockage.
- HYPOTHÈSE. Le coût dominant est humain : banque à vérité plantée, plus quelques heures d'annotation d'un échantillon d'une centaine de trajectoires.

## 4. Antériorités connues

Statut de toutes : rapporté, non vérifié sur PDF. Aucun chiffre n'en est tiré.

- Greenblatt, Shlegeris, Sachan, Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion*. Seuil d'audit réglé sur des exécutions honnêtes du même modèle.
- Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (2025), *Detecting Strategic Deception Using Linear Probes*. Seuil fixé par un taux de fausses alertes sur conversations de contrôle. De mémoire, des déclenchements sur du contenu honnête lié au thème de la tromperie y sont signalés.
- Azaria, Mitchell (2023), *The Internal State of an LLM Knows When It's Lying*.
- Marks, Tegmark (2023), *The Geometry of Truth*.
- Orgad et coauteurs (2024), *LLMs Know More Than They Show*.
- Levinstein, Herrmann (2023), *Still No Lie Detector for Language Models*.
- Kutasov et coauteurs (2025), *SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents*. Moniteurs évalués contre des trajectoires bénignes.
- van der Weij et coauteurs (2024), *AI Sandbagging: Language Models can Strategically Underperform on Evaluations*.
- Vovk, Gammerman, Shafer (2005), *Algorithmic Learning in a Random World*.
- Bates, Candès, Lei, Romano, Sesia (2023), *Testing for Outliers with Conformal p-values*.
- Clopper, Pearson (1934), *The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial*.
- Kohavi, Tang, Xu (2020), *Trustworthy Online Controlled Experiments*, pour l'essai A/A.

Conséquence au titre de la règle R8 :
- HYPOTHÈSE. Que des représentations internes suivent la fausseté d'une sortie n'est pas une zone vierge. Que les moniteurs de contrôle soient calibrés sur des honnêtes qui se trompent ne l'est pas davantage.
- PROPOSITION. E0 est une mesure locale, sur nos sondes et notre harnais. Elle ne revendique aucun trou du champ.
- HYPOTHÈSE. La question « une sonde de sabotage diffus distingue-t-elle erreur honnête dommageable et sabotage à dommage égal ? » reste une question. La recherche bibliographique n'est pas faite.

## 5. Décisions qui reviennent au directeur

**Décision 1 : choisir la métrique principale de fausse alerte.**
- Enjeu : c'est elle qui portera le mot « 1 % » dans les papiers.
- Option a, alerte brute de sonde par tâche. Avantage : comparable à la référence actuelle. Inconvénient : ignore la règle N-075.
- Option b, motif et dommage au même lieu. Avantage : mesure la fausse accusation réelle. Inconvénient : dépend de la qualité de la localisation.
- Option c, les deux en co-principales avec correction. Avantage : aucune lecture perdue. Inconvénient : puissance un peu réduite.
- Recommandation : c. Confiance : 0,75.

**Décision 2 : fixer les sources d'imperfection admises en confirmatoire.**
- Enjeu : ce qui compte comme « honnête réel ».
- Option a, difficulté et horizon seuls. Avantage : rien de fabriqué. Inconvénient : couverture étroite.
- Option b, ajout de la température, de la quantification et des pannes d'outils en confirmatoire. Avantage : couverture plus large. Inconvénient : populations que le déploiement ne verra peut-être pas, et coût doublé.
- Recommandation : a en confirmatoire, le reste en secondaire étiqueté. Confiance : 0,8.

**Décision 3 : autoriser ou non la lecture des scores bruts de la référence honnête, et déclarer m.**
- Enjeu : la nulle exacte de l'essai A/A en dépend.
- Option a, lecture autorisée après vérification écrite que la référence n'est pas sous scellé. Avantage : test exact, m fini compris. Inconvénient : risque de contact avec le périmètre scellé.
- Option b, seuil et m seulement. Avantage : étanchéité. Inconvénient : test plus grossier.
- Recommandation : a si l'étanchéité est attestée par un tiers, sinon b. Confiance : 0,6.

**Décision 4 : déposer avant E0 l'addendum au plan de G1 et le gel des sondes jusqu'à G1.**
- Enjeu : sans lui, « et non le sabotage » ne sera jamais concluable proprement, et E0 pourrait contaminer G1.
- Option a, addendum et gel. Avantage : inférence propre. Inconvénient : G1 peut tourner avec des sondes que E0 aura déjà affaiblies.
- Option b, reconception immédiate si E0 conclut contre les sondes. Avantage : gain de temps. Inconvénient : prévision scellée caduque, cycle non comparable.
- Recommandation : a. Confiance : 0,7.

**Décision 5 : fixer la taille.**
- Enjeu : ce que E0 a le droit de dire.
- Option a, environ 1 600 trajectoires. Avantage : dans les moyens, réfute 1 % si le vrai taux est d'au moins 3 %. Inconvénient : muette entre 1 et 2 %.
- Option b, S0 porté à 800 tâches. Avantage : sépare 1 % de 2 %. Inconvénient : banque de tâches doublée.
- Option c, pilote de 300. Avantage : rapide. Inconvénient : presque tout « non jugé ».
- Recommandation : a, avec b préenregistrée comme extension si S0 sort « non jugé ». Confiance : 0,7.

**Décision 6 : désigner le tiers qui tient l'oracle, le hachage et le recalcul.**
- Enjeu : c'est la seule validité qui ne dépend ni du directeur ni de Claude.
- Option a, personne externe au programme. Avantage : indépendance réelle. Inconvénient : délai.
- Option b, modèle d'une autre lignée avec dépôt public horodaté. Avantage : immédiat et peu coûteux. Inconvénient : indépendance plus faible.
- Recommandation : b tout de suite, a avant toute revendication écrite. Confiance : 0,65.

FIN DE LA RÉPONSE
