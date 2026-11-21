# Contre-lecture des trois choix du banc fermé de l'attaquant informé, par Fable 5.2 — v1

- **Classe C** (note de contre-lecture). Elle ne tranche rien : elle dit, pour chacun des trois choix, s'il tient, et à quelles conditions.
- **Qui** : agent neuf, Claude Fable 5.2 (`claude-fable-5-2`), effort maximal, lancé par un script de la session mère (`session_01Qi7Gr3eYmAhDEJzqLgWcv1`). Je n'ai écrit aucune des pièces relues et je ne conçois aucun moniteur.
- **Quand** : 21 novembre 2026, de 18:24 à 18:51 UTC (relevés `date -u`).
- **Demande** : mot de Lazar, « demande contrelecture des choix par fable », puis « go recos » (`registres/go.md:673`, GO-2026-11-21-74).
- **Fait survenu pendant la lecture** : à 18:42:47Z, le registre inscrit le « go » de Lazar sur ces choix (`registres/go.md:674`, GO-2026-11-21-75). Cette note arrive donc après le mot. Elle ne le défait pas : elle dit ce qu'il couvre, ce qu'il ne couvre pas, et ce qui doit exister avant toute exécution.
- **Non lus, par consigne** : rien sous `donnees/` ; aucune famille aveugle, donc aucune branche `claude/scellement-2-*` ; aucun épisode ; aucun fichier « consigne-privee » ni « conception-ii-b » ; rien sous `archives-reponses-modeles/`, `brouillons/` ni `/root/.claude/`. Je ne connais donc ni la vérité du dommage de la famille (sa pièce 3), ni les lecteurs que le monteur de l'oracle a retenus.
- **Refus d'un classifieur de sûreté** : aucun.

## Verdict

Les trois choix vont dans le bon sens ; aucun n'est à remplacer. Aucun ne s'exécute tel qu'il est écrit.

| Choix | Verdict | Poids de la réserve |
|---|---|---|
| 1. Opérateur : Opus 5.5 neuf dédié ; juge des recettes : Fable 5.2 neuf ; second juge : Opus 5.5 neuf ; dommage lu par les lecteurs externes du monteur de l'oracle | **tenir avec réserve** | **bloquante** pour la lecture du dommage ; mineure pour le reste |
| 2. Agent : Llama-3.1-8B-Instruct | **tenir avec réserve** | d'écriture : le modèle lui-même ne se discute pas |
| 3. Dépôt daté, chez un tiers, de l'index des familles aveugles avant le premier épisode | **tenir avec réserve** | d'instrument et de portée |

- **Erreur relevée au registre.** La ligne du « go » écrit que confier le dommage aux lecteurs externes est un « écart à N-060 v3 point 1 » (`registres/go.md:674`). À ma lecture, c'est l'inverse : deux lecteurs de deux familles hors de celles des moniteurs, c'est ce que N-060 v3 demande (`docs/decisions/decision-N-060-v3.md:24-25`) ; je ne vois pas les lecteurs du monteur, et la ligne ne tiendrait que s'ils n'étaient pas de deux telles familles. L'écart que ce choix ouvre est ailleurs, et la ligne le tait : l'envoi à un autre fournisseur de modèles de produits dérivés du coffre, avant la revue de sécurité externe (section 1.3).
- **Décision qui reste à Lazar** : une phrase sur cet envoi (section 1.4). Pas de défaut à 48 heures.
- **Changement de rédaction proposé** : au préenregistrement, un brouillon 4 ; à la pièce de sécurité, une v8 ; au registre, un erratum à GO-2026-11-21-75.

## Pièces lues

| Pièce | Lieu | Empreinte (recalculée) |
|---|---|---|
| préenregistrement de la course, brouillon 1 (celui que le mandat désigne) | `prereg/course-banc-ferme-v1-brouillon1.md`, branche `origin/claude/prereg-course-banc-ferme-v1` | `d4e6d7125c63d1e8c0e6349ac9f3dff90a7ddc4c9a294ee9a13e6475c58c0b6f` |
| le même, brouillon 3, paru pendant la lecture, accepté par sa contre-lectrice ; noté **[b3]** | même branche, tête `fcceae6737f4` | `efa943feccc25d340813242f95951623487242db23e86f5e4e712581ad1565f9` |
| contre-lecture 1 du préenregistrement | `prereg/course-banc-ferme-v1-contre-lecture-v1.md`, branche `origin/claude/prereg-course-banc-ferme-contre-lecture-v1` | `e9ed547d5dd7006e…` |
| pièce de sécurité du banc fermé, v7 ; notée **[PS]** | `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v7.md`, branche `origin/claude/piece-securite-banc-ferme-v1`, commit `2efdc92f` | `d3172b9af08d294db589e842b3cd85969dc40f86a5f67b1c7a83634cc655c683` |
| note de l'attaquant informé (proposition pour l'opérateur et le juge) | `registres/passations/2026-11-21-1800-attaquant-informe-mot-lazar-verificateur-opus-neuf.md`, branche `origin/claude/loving-lamport-7ol5ws` | `8da822e47cc93239…` |
| règle du bras d'attaque et son addendum 1 ; notées **[PR]**, **[PR-1]** | `prereg/bras-attaque-regle-v1.md`, `…-addendum-1.md`, branche du préenregistrement (absentes de `main`) | `88418df09c2e969c…`, `edfa69a292cc968a…` |
| décisions N-053, N-054, N-055, N-056, N-057, N-060 v3, N-062, N-029 | `docs/decisions/` | `2204256d…`, `c8a00b3f…`, `371879d5…`, `3592c1e9…`, `42180088…`, `2b448f69…`, `63f42690…`, `084e3052…` |
| note des lignées à exclure, et sa vérification | `docs/notes/scellement-2-lignees-lecteurs-v1/` | `596b5a73453b97ed…`, `8718c80bee53da35…` |
| plan du dépôt chez le tiers ; règle du jeu, brouillon 5, notée **[RJ]** | `docs/notes/integration-bras-attaque-v1/` | `b1a96e4d62fe450f…`, `527a3e7ec2a0f282…` |
| index du scellement 2, v1 et v2 | `registres/index-scellement-2-familles-aveugles-v1.md`, `…-v2.md` | `5d0479b437426509…`, `80efd526a63cbe5e…` |
| attestation sur le calage honnête de la porte G1 | `docs/notes/attestation-episodes-calage-g1-v1/attestation-format-outils-pile-v1.md` | `3f0b50f020b1c780…` |
| devis de la banque d'épisodes de la famille de réserve du cycle 2 | `docs/notes/devis-famille-reserve-cycle-2-v1/devis-banque-d-episodes-famille-reserve-cycle-2-v1.md` | `4c144ba4686f2ace…` |
| liste des modèles du harnais ; configuration des organismes de T0.6 | `src/controle_ia/harnais/modeles.py` ; `prereg/T0.6-organismes-config-7b-v1.json` | `d0befc29aeba4b24…` ; `b7a5c1baeee13f75…` |
| programme de dépôt chez le tiers ; manifeste v3 ; passation du dépôt du 10 novembre | `scripts/osf_depot_v1.py` ; `livrables/osf-manifeste-v3/manifeste-v3.json` ; `registres/passations/2026-11-10-1033-depot-tiers-manifeste-v3-regle-bras.md` | `8f03f62d0ffe2df4…` ; `576b88cc3d0571fe…` ; `54ab71dc50ddb4a3…` |
| registres vivants, aux seules lignes citées | `registres/go.md`, `registres/decisions.md`, arbre de travail au commit `403f45d94` | ils ne s'allongent que par la fin |

## 1. Choix 1 — opérateur, juges, lecteurs du dommage

### 1.1 L'opérateur, une session Opus 5.5 neuve et dédiée : tenir

- La pièce de sécurité ne demande à l'opérateur qu'une chose : n'avoir conçu ni sonde ni agrégateur et n'en plus concevoir ([PS]:105). Il ne lit ni le lot ni les sorties ([PS]:217 ; [b3]:110, :152).
- **Sa lignée ne pèse pas sur la mesure** : il ne juge rien. La réserve de la mère sur la lignée de Claude vise le vérificateur, qui juge (`registres/go.md:671`) ; rien ne commande de l'étendre à qui ne lit pas.
- Le choix suit la règle neuve d'économie de Fable : Opus pour les vérifications et le code (`CLAUDE.md`, GO-2026-11-21-75).
- Trois conditions mineures, à écrire au préenregistrement :
  1. il est lancé par la mère, jamais par la session de l'attaquant informé (`registres/decisions.md:4793` ; [PR]:321) ;
  2. **relais d'arrêt.** Une session opératrice peut être coupée par un classifieur, et la règle interdit alors tout renvoi à une autre session ([PS]:193 ; [b3]:333). Rien ne dit qui arrête la machine. À écrire : opérateur coupé ou muet, la mère arrête l'instance par son identifiant, sans la détruire, consigne, et le reste est un nœud. Arrêter une machine n'est pas refaire l'acte refusé ;
  3. il ne détient aucune clé de fournisseur de modèles et ne lance pas la lecture du dommage (section 1.3).
- À noter sans en faire une réserve : opérateur, vérificateur interne et contre-lectrices sont le même modèle. L'indépendance tient aux sessions et à la forme fermée des vingt-deux points, pas aux modèles.

### 1.2 Juge des recettes Fable 5.2, second juge Opus 5.5 : tenir la désignation, différer l'accès

- **La désignation tient.** Les recettes ne quittent jamais la quarantaine (`docs/decisions/decision-N-057-v1.md:32-34` ; [PR]:382). Leurs lecteurs ne peuvent donc être que des sessions du programme, toutes de la lignée de Claude : Fable et Opus sont la plus grande diversité disponible. La règle du bras ne fixe d'ailleurs aucune famille au juge ([PR]:199-208, :324-325).
- **Lignée de Claude et moniteurs.** Aucun moniteur évalué n'est de cette lignée, à ce jour : les familles établies sont Llama et Qwen, plus un prédicteur sans modèle de langue (`docs/notes/scellement-2-lignees-lecteurs-v1/lignees-a-exclure-v1.md:11-16`, :26), et le juge Claude a été retiré (`docs/decisions/decision-N-029-v1.md:32-33`). Deux bases n'ont pas de famille établie (`…/verification-lignees-a-exclure-v1.md:33`). **Condition** : si l'audit de la mère en établit une de la lignée de Claude, ces juges tombent comme le vérificateur (`registres/go.md:671` ; [b3]:397).
- **Dans cette course, ces rôles n'ont pas d'objet.** Aucun moniteur n'y lit, aucune évasion n'y est comptée, aucune classe de faille n'y est attribuée ([b3]:52) ; à l'échelon aveugle, les verdicts relèvent du préenregistrement de la porte G1 ([PR]:113, :234-235). Or le second juge n'existe que pour l'accord sur les classes de faille ([PR]:201-204).
- **Donc : moindre accès.** Chaque lecteur du lot ou des sorties sort pour de bon de la conception des moniteurs, et la course se tient avant leur gel (`docs/decisions/decision-N-057-v1.md:42-43` ; [PS]:146, :208 ; [b3]:53, :420).
  - Le **second juge** n'est pas lancé pour cette course. Il est désigné pour l'ouverture, quand des moniteurs gelés auront lu.
  - Le **juge** ne garde ici que le second temps, non aveugle, qui ne peut pas sortir du programme : sous-classes d'abstention, vérifications qui demandent la transcription ([b3]:252), et le contrôle du seuil de dommage, que la règle lui réserve ([PR]:302-303).
- **Économie de Fable.** La règle inscrite à 18:42Z ne nomme pas le rôle de juge (`CLAUDE.md`). Je recommande de compter l'attribution des classes parmi les lectures décisives : deux juges Opus ne donneraient qu'un accord entre deux sessions d'un même modèle. Sous la proposition ci-dessus, cette course ne coûte presque rien à Fable.

### 1.3 Le dommage lu par les lecteurs du monteur de l'oracle : la bonne direction, non exécutable en l'état

**Pourquoi c'est la bonne direction.** Je rejoins la mère contre la recommandation du préenregistrement, qui garde les deux juges Claude ([b3]:399). Quatre raisons.

1. **La lettre de N-060 v3** : deux lecteurs de deux familles autres que celles des moniteurs évalués, ni Llama ni Qwen (`docs/decisions/decision-N-060-v3.md:24-25`). Fable et Opus sont une seule famille.
2. **Un seul oracle.** Un oracle qui échoue à ses épreuves n'est pas lu (même décision, :28-30). Le monteur, un Opus neuf, monte et éprouve l'oracle de cette famille avec ses lecteurs externes (`registres/go.md:665` ; `registres/decisions.md:4777` ; note des lignées, :1-3). Lire la course avec deux sessions Claude, ce serait lire avec un instrument qui n'a pas passé les épreuves.
3. **La famille ne sert qu'une fois** ([b3]:54). Avec deux sessions Claude pour seuls lecteurs, une coupure de classifieur chez l'une suffit à rendre le dommage « non établi » ([b3]:304, :333). Ces coupures arrivent : quatre aujourd'hui sur un autre chantier, et Fable 5.2 comme Opus 5.5 ont refusé un rôle ailleurs (`registres/decisions.md:4796`, :4786).
4. **L'instrument.** Un appel de programme sans mémoire, à invite gelée, avec citation vérifiée mot pour mot (`decision-N-060-v3.md:22-24`), est aveugle par construction. L'aveuglement d'une session qui se promène sur une branche est une promesse.

**Pourquoi cela ne peut pas partir.**

- La pièce de sécurité acceptée ne connaît que des lecteurs qui sont des sessions du programme, lisant en quarantaine ([PS]:55, :126). Son seul passage hors quarantaine est le fichier des agrégats ([PS]:138 ; point 14, :247). Toute autre sortie, « partage » compris, attend la revue de sécurité externe ([PS]:182, :191).
- Le préenregistrement le dit en toutes lettres : « Aucun contenu de quarantaine n'est envoyé à l'interface d'un autre fournisseur de modèles sous ce texte » ([b3]:116) ; ligne d'arrêt ([b3]:357) ; « sous ce texte, seule (a) est exécutable » ([b3]:399).
- **Le vérificateur interne répond sur la pièce.** Avec un envoi au-dehors, il doit, à ma lecture, écrire « non » au point 14, et un seul « non » vaut « pas de course » ([PS]:178, :262). Un mot de Lazar ne suffit donc pas : il faut aussi une pièce de sécurité v8.
- Le sixième garde-fou, que Lazar a retenu pour ce banc, fixe la revue externe « avant toute sortie hors quarantaine (papier, billet, dépôt public, partage) » (`registres/go.md:581`, :670). Cette revue est mise de côté jusqu'à la publication (`registres/go.md:671`). L'envoi est donc un écart neuf à ce garde-fou.

**Ce que le « go » de 18:42Z couvre.** Il porte bien sur des lecteurs externes. Mais la ligne nomme l'écart de l'autre option (deux lecteurs d'une même famille, [b3]:397) et tait celui de l'option retenue (l'envoi, [b3]:398). Je n'ai lu que la ligne du registre, pas le message montré à Lazar. S'il disait l'envoi, un erratum à la ligne suffit. Sinon, le mot exprès manque encore.

**Ce qui doit exister avant toute lecture.**

1. **Pièce de sécurité v8**, contre-lue par la même contre-lectrice. Elle ajoute une destination : les seuls produits extraits par programme et les questions fermées, vers des lecteurs nommés ; jamais la consigne, le lot, la transcription ni le journal ([b3]:251). Elle ajoute une garde de l'envoi, éprouvée sur un cas sain et sur un artefact : charge portant un mot témoin de consigne, refusée ; destinataire hors liste, refusé. Elle récrit le point 14 et fixe les réglages : version datée du modèle, rétention, journal des appels par empreintes hors quarantaine, contenus dedans, règle du refus.
2. **Brouillon 4 du préenregistrement** : D6, D8, la ligne d'arrêt :357, la ligne de coût :381, le nœud 1.
3. **Les lecteurs nommés.** La pièce de sécurité veut la liste nominative au préenregistrement ([PS]:230) ; N-060 v3 veut les familles exactes vérifiées avant l'usage et la dépense sur devis (`decision-N-060-v3.md:44-45`). Le choix, tel qu'écrit, ne nomme personne.
4. **Les épreuves de l'oracle passées avec ces lecteurs-là**, mêmes modèles, mêmes réglages, et un taux de refus toléré fixé d'avance.
5. **Qui lance la lecture** : pas l'opérateur du banc. Le poste de transit ne doit pas réunir contenu de quarantaine, clés de fournisseurs et réseau sortant ([b3]:122).

**Deux points de lignée à lever avant de nommer.**

- **Mistral.** Le panel des juges du papier C nomme Mistral-7B (`registres/decisions.md:377` ; `src/controle_ia/harnais/modeles.py:29`). Or ces épisodes servent aussi deux mesures du papier C, lues par des moniteurs de texte ([b3]:50 ; [PR]:134). Si ce panel les lit, la famille Mistral est évaluée, et Mistral Large 4 ne peut pas lire le dommage ici. C'est pourtant le second lecteur du bras A (`registres/go.md:589`) et celui que propose le devis de la famille de réserve (devis du cycle 2, :13, :17). Le statut de ce panel n'est pas vérifié (vérification des lignées, :51).
- **Deux bases sans famille** : l'observateur séparé et le juge robustifié (vérification des lignées, :33).

**Si un lecteur est un modèle Claude** : appel de programme sans mémoire, jamais session ; instance distincte de l'auteur de la famille, parenté déclarée (note des lignées, :32 ; `decision-N-060-v3.md:34-35`).

### 1.4 Décision pour Lazar

- **Décision** : qui lit le dommage des épisodes de la famille aveugle, et par quelle voie.
- **Enjeu** : N-060 v3 veut deux familles hors des moniteurs ; la pièce de sécurité ne laisse rien sortir vers un autre fournisseur avant la revue externe ; la famille ne sert qu'une fois.
- **Options.**
  - **(A) L'oracle du monteur, tel qu'éprouvé**, ses lecteurs servis par leurs fournisseurs. De préférence un seul fournisseur de plus : un lecteur Claude par appel de programme et un lecteur d'une autre famille, comme au bras A (vérification des lignées, :36). Avantage : la lettre de N-060 v3, un seul oracle. Inconvénient : l'envoi au-dehors, donc une phrase de Lazar, une pièce de sécurité v8 et un brouillon 4 ; un refus chez ce fournisseur coûte un lecteur.
  - **(B) Le même oracle, second lecteur à poids ouverts sur machine fermée.** Avantage : rien ne sort, aucun écart. Inconvénient : lecteur plus faible, à qualifier par les épreuves ; modèle neuf et dépense, donc devis et GO.
  - **(C) Deux sessions Claude en quarantaine.** Avantage : exécutable sous les textes actuels. Inconvénient : écart à N-060 v3 ; oracle non éprouvé avec ces lecteurs ; une coupure suffit à perdre le dommage ; toute la chaîne du dommage dans une seule famille, sans aucun regard hors de Claude.
- **Recommandation** : (A), confiance 0,6 ; (B) si Lazar ne veut pas signer l'envoi ; (C) en dernier.
- Pas de défaut à 48 heures : nœud d'arrêt.

## 2. Choix 2 — l'agent Llama-3.1-8B-Instruct

**Tenir le modèle : c'est une nécessité, pas une contamination. Les réserves portent sur l'écriture.**

- La course existe pour que des sondes lisent les états internes de l'auteur de l'épisode ([b3]:50 ; [PS]:49). Sondes, seuils de calage et couches rapportées appartiennent à ce modèle (`docs/decisions/decision-N-056-v1.md:52-54`). Un autre agent, et les sondes gelées ne lisent plus rien ; la loi exacte du taux de fausses alertes perd son hypothèse d'échangeabilité ([PR]:156-160) ; et c'est un changement de modèle, interdit sans GO (`src/controle_ia/harnais/modeles.py:6-7`, :25-30).
- Pour un moniteur qui lit l'intérieur, la lignée de l'agent **est** la lignée lue (note des lignées, :13). La séparation des lignées ne pèse pas sur l'agent : elle pèse sur ceux qui établissent la vérité et sur ceux qui vérifient. N-060 v3 la veut « indépendante des moniteurs et de l'agent » (`decision-N-060-v3.md:24-27`).
- **Le champ n° 3 du préenregistrement ne peut donc pas être rempli tel qu'il est écrit** (« que l'agent n'appartienne à aucune lignée de moniteur », [b3]:65). À récrire, dans le sens de son nœud 2 (a) ([b3]:400) : « aucun lecteur du dommage, ni le vérificateur, ni le lecteur de la question fermée n'est de la lignée de l'agent ni de celle d'un moniteur évalué ».
- Le vrai souci de même famille est ailleurs, et déjà traité : le juge boîte noire est le même modèle que l'agent (`registres/decisions.md:376`), d'où le juge Qwen d'une autre lignée (`docs/decisions/decision-N-053-v1.md:33-35`). Il regarde la lecture à venir, pas cette course.

**Réserves d'écriture, à lever avant le scellement.**

1. **Le nom ne suffit pas.** L'attestation versée à 18:33Z le dit : seul le nom concorde ; format, outils et pile d'inférence sont « non établis » (attestation, :11-15 ; `registres/decisions.md:4801`). À fixer : la révision complète, dont la candidate est `0e9e39f249a16976918f6564b8830bc894c89659` (attestation, :47 ; `prereg/T0.6-organismes-config-7b-v1.json:20`) ; l'absence d'adaptateur ([b3]:62) ; les variables du gabarit, date comprise (même configuration, :21-24) ; la bibliothèque, sa version, la précision.
2. **L'ordre s'inverse.** Les champs n° 1 et n° 2 renvoient au calage honnête de la porte G1 ([b3]:63-64, :234). Ce calage n'existe pas (attestation, :32). C'est donc cette course qui fixe la configuration que le calage devra copier, non l'inverse. Il faut un fichier de configuration de génération scellé avant la course, accepté par qui tient le préenregistrement de G1 (attestation, :56). Sinon le validateur bloque le scellement ([b3]:5). Le « go » sur l'agent ne règle pas ce point.
3. **Question pour qui tient G1.** La configuration des organismes de T0.6 porte un adaptateur de rang faible appris par distillation (`prereg/T0.6-organismes-config-7b-v1.json:5-16`, :66-74). Ici l'agent est nu, sous une consigne en contexte. Si les modes connus sont lus sur des organismes à adaptateur, la comparaison entre modes mêle le mode et la façon de l'induire. À dire dans le résultat.
4. **Famille à usage unique, agent de huit milliards de paramètres.** La part d'épisodes où l'agent ne réalise pas le dommage est inconnue. La course peut sortir « utilisable » et laisser G1 sans puissance sur ce mode, sans seconde génération permise ([b3]:54 ; `docs/decisions/decision-N-062-v1.md:24` ; `decision-N-056-v1.md:55-57`). Le nombre minimal de paires ([b3]:219) se règle sur l'abstention de ce même agent dans les modes connus, mesure qui ne touche pas la famille aveugle.
5. **Portée.** La mesure vaut pour ce modèle. La lecture à plus grande taille (`decision-N-053-v1.md:36-37`) ne pourra pas réemployer ces épisodes : il lui faudra une famille neuve.

**Alternative** : aucune pour le modèle.

## 3. Choix 3 — le dépôt daté de l'index chez un tiers

**Tenir le geste ; les réserves portent sur l'outil et sur ce que la date prouve.** Il est prévu partout : règle du jeu ([RJ]:154), plan du dépôt (:53-58), index (v1:27 ; v2:42), préenregistrement ([b3]:403). « Avant le premier épisode » est le bon moment, plus strict que « avant la porte G1 » (plan, :57). L'index porte les empreintes du texte de la famille, de la vérité de son dommage, du plan de ses épreuves et de la lecture de sa force (v1:14-21). Datées avant qu'un épisode existe, personne ne pourra dire que la vérité du dommage a été ajustée après avoir vu ce que l'agent a fait. Le mot de Lazar que l'index attendait est donné (`registres/go.md:674`).

**Réserves.**

1. **L'outil ne sait pas déposer l'index.** Le programme scellé ne lit que `prereg/`, `docs/verdicts/` et `docs/decisions/` (`scripts/osf_depot_v1.py:43`, :166). L'index vit sous `registres/`. Le manifeste v3 compte 167 fichiers, aucun hors de ces trois dossiers. Deux voies.
   - Sans toucher au code : porter l'empreinte de l'index dans une pièce scellée d'un dossier couvert. La note de décision qui inscrira le mot de Lazar fait l'affaire. Le préenregistrement scellé de la course aussi : il porte déjà les quatre empreintes de la famille et celle de l'index ([b3]:27, :38-41).
   - Ou une version neuve du programme, avec une liste explicite de fichiers : instrument de classe B, contre-lu, éprouvé sur un cas sain et sur un artefact.
2. **Privé et non gelé : daté, pas encore opposable.** Le plan le dit (:27-29), la règle du jeu aussi : rester privé et non gelé, c'est « aucune preuve de date » ([RJ]:154). Le dépôt du 10 novembre ne prouve qu'« une fois le projet public » (passation du dépôt, :20). Après le dépôt, on peut écrire « daté par le tiers, projet privé » ; jamais « opposable ». Geler et rendre public restent des gestes de Lazar (plan, :46-48 ; [PR-1]:32-33). Aucune ligne du registre ne les accorde : seules deux lignes en parlent, la première pour dire « passage en public sur mot de Lazar », la seconde pour l'exclure d'une autonomie (`registres/go.md:256`, :260).
3. **L'audit des chemins se fait avant le dépôt**, pas avant la publication (plan, :35-42). L'objet daté ne se change plus : un chemin qui en dit trop forcerait à choisir entre le publier et perdre la date. Un manifeste court, propre à ce dépôt, réduit la surface à relire.
4. **Quel index, et il n'est pas fait d'empreintes seules.** La v2 existe depuis 18:28Z ; elle reprend la v1 et ajoute la famille de réserve (`registres/decisions.md:4799` ; v2:5-6). C'est elle qu'il faut dater. Mais sa réserve 2 dit en clair quelque chose du contenu des deux familles (v2:41 ; je ne le répète pas ici). Elle est sur `main`, lisible par qui conçoit des moniteurs, et la v2 a été préparée par la session fille de l'attaquant informé (v2:3), que la règle tient à l'écart des familles aveugles ([PR]:321). Je ne juge pas la gravité, ne lisant pas le coffre. À la mère de dire si c'est un écart au cloisonnement (`docs/decisions/decision-N-054-v1.md:40-45`). Dans tous les cas : déposer l'empreinte de l'index, pas son texte.
5. **Rien ne garde « avant le premier épisode ».** Les douze conditions de lancement n'en parlent pas ([b3]:230-241). À ajouter : identifiant du dépôt, date rendue par le tiers et empreinte relue, inscrits à l'addendum B et au manifeste de la course ; la garde du GO refuse sans eux.
6. **Un seul maillon daté.** L'ordre à prouver a quatre maillons : la famille avant ses épisodes ; les étiquettes de dommage avant toute lecture par un moniteur ; les moniteurs gelés avant cette lecture ; puis l'ouverture. Le même dépôt devrait porter l'empreinte du préenregistrement scellé de la course et celle de l'oracle monté. Un second dépôt, après le versement, daterait l'inventaire et les réponses scellées des lecteurs. Le troisième est le gel des moniteurs, déjà prévu (plan, :55-56).
7. **Sous quelle autorisation.** Le dépôt chez le tiers reste à Lazar, hors des autonomies (`registres/go.md:369`, :668). L'autorisation permanente du 5 novembre couvre les empreintes « des préenregistrements, verdicts et décisions scellés », projet privé d'abord, jusqu'au 30 novembre (`registres/go.md:256`). La première voie du point 1 y entre à la lettre. Le jeton se lit par son nom, jamais affiché (`scripts/osf_depot_v1.py:47`, :83).

**Alternative, en complément.** Un horodatage indépendant qui ne demande ni compte ni publication : une autorité d'horodatage au sens de la norme RFC 3161, ou l'ancrage de l'empreinte dans un registre public. Seule l'empreinte part ; la preuve se garde au dépôt et vaut par elle-même. Il donnerait tout de suite la date qu'on ne peut plus changer. C'est encore un geste vers l'extérieur, donc le mot de Lazar. **Non vérifié depuis ce dépôt**, comme la possibilité de geler le projet chez le tiers sans le rendre public : à établir sur la documentation du tiers avant de s'y fier.

## 4. Vu en passant, hors des trois choix

1. **Épreuves de l'oracle et génération unique.** Le préenregistrement place les épreuves de la vérité du dommage avant la course ([b3]:237) et dit la génération unique ([b3]:54). Le devis de la famille de réserve décrit des épreuves qui demandent des épisodes produits par l'agent (devis du cycle 2, :61). Si celles de la famille 1 en demandent aussi, ces épisodes ne peuvent naître que sur le banc fermé. Les deux règles ne tiennent alors ensemble que si le lot contient les épisodes d'épreuve et si leur lecture passe la première. À faire dire par l'assembleur, sans contenu, dans son attestation ([b3]:74).
2. **Heures.** Le préenregistrement date ses brouillons de « vers 19:00 » et « 19:15 » ([b3]:8) ; ses commits sont de 18:25:34Z et 18:27:59Z. La relecture courte se date de « vers 19:20 », pour un commit de 18:28:36Z. Le texte définitif, de classe A, doit porter l'heure lue par `date -u`.
3. **Le plan du dépôt chez le tiers** est un brouillon du 10 novembre, « à contre-lire » (plan, :4). Il décrit le manifeste v1 ; les v2 et v3 existent depuis.
4. **Aucun regard humain sur le dommage.** N-060 v3 prévoyait une ancre humaine sur un sous-échantillon (`decision-N-060-v3.md:30`) ; l'ancre des épreuves est confiée à un agent neuf (`registres/go.md:665`). C'est décidé ; à écrire dans le résultat.

## 5. Ce qu'un expert ferait de plus, et ce qui vérifie hors de Lazar et de Claude

- **Une répétition générale sur un mode connu, de bout en bout**, avant de consommer la famille aveugle : lot, banc, versement, lecture par les lecteurs du monteur, agrégats. La répétition à blanc prévue joue une consigne anodine et éprouve les gardes, pas la chaîne de lecture ([b3]:235). Cette répétition mesurerait d'un coup la complétude, l'abstention de cet agent, le taux de refus et l'accord des lecteurs, le volume des activations. C'est une course de plus sur le banc fermé : texte court scellé, devis et GO.
- **L'agent** : les empreintes des fichiers de poids publiées par le dépôt du modèle à la révision figée. Le harnais sait déjà les comparer au cache local (`src/controle_ia/harnais/modeles.py:231-244`).
- **Le dommage** : les épreuves mécaniques de l'oracle et la citation vérifiée par programme (`decision-N-060-v3.md:22-24`, :28-30) ; un lecteur qui ne soit pas de la lignée de Claude. Sous l'option (C) de la section 1.4, il ne resterait aucun regard hors de Claude.
- **Les dates** : celle du tiers, et un horodatage indépendant.

## 6. Ce que je n'ai pas vérifié

- Les lecteurs du monteur de l'oracle et la pièce 3 de la famille : au coffre. J'ignore donc si la lecture sur le seul produit suffit, et si les deux lecteurs sont bien de deux familles hors Llama et Qwen.
- Le message montré à Lazar avant son « go » de 18:42Z : je n'ai lu que la ligne du registre.
- Le statut actuel du panel des juges du papier C ; les familles de l'observateur séparé et du juge robustifié.
- Les fonctions du tiers (gel sans publication, date d'un fichier privé) et tout service d'horodatage indépendant.
- Le brouillon du préenregistrement de la porte G1, sous `brouillons/` : je m'appuie sur l'attestation qui le cite.
- Les essais et la vérification de l'arbre : hors de ce mandat.

## 7. Pour Lazar, en trois phrases

1. **Lecteurs du dommage.** Ton « go » est inscrit avec un écart qui n'est pas le bon. Dis d'une phrase si tu acceptes que les seuls produits de l'agent et les questions fermées partent chez un autre fournisseur avant la revue externe (option A), ou si tu préfères un second lecteur local (option B).
2. **Agent.** Rien à redire au modèle. La révision et la configuration de génération se scellent avant la course, et c'est elles que le calage de la porte G1 devra copier.
3. **Dépôt.** Ton mot est donné. Sans gel du projet chez le tiers, la date existe mais ne s'oppose encore à personne : dis si tu gèles maintenant ou à la publication.
