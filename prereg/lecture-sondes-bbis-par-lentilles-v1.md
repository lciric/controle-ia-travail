# Préenregistrement descriptif — lecture, par la lentille publique côté sortie, des directions des sondes apprises sur la tâche (étape B bis de T0.7) — v1

- **Auteur** : rédacteur neuf, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1` (modèle servi : Opus 5.5), sur le mandat
  `docs/notes/neuron-lens-v1/mandat-redacteur-texte-lecture-sondes-bbis-par-lentilles-v1.md`
  (`3010f726510856f202c62b5acd9c50166e1bd4860d88f45f1d50ca951cd732bb`), repris trois fois sur les messages de la mère du 2026-11-18
  (décision de Lazar GO-2026-11-18-42, R-3349 ; choix de forme de la mère, R-3334 ; contre-lecture 1 ; pour cette version, reprise
  commandée par la mère sur la vérification 1 des corrections). Il n'a écrit ni T0.6, ni T0.7, ni
  aucune pièce de l'apprentissage des sondes sur la tâche (texte, addenda, code), ni P3-bis, ni aucune pièce des tranches de la lecture
  par lentille neuronale ; il ne sera ni développeur, ni opérateur, ni lecteur de ce texte, ni lecteur ou juge d'aucun verdict nommé ici.
- **Date (UTC, `date -u`)** : 2026-11-18. Brouillon 1 : lecture des pièces à partir de 16:41, entropie des graines tirée à 16:49:33,
  écrit de 16:58:55 à 17:02:37, scellé comme brouillon (`61ba10b9f2f6c8affc05eeda7ee52f5bde8e3c9ef8eac7192404d9f52bc777b8`).
  Brouillon 2 : écrit de 18:03:00 à 18:07:10, scellé comme brouillon (`271c421f089f39564527981fc98fb9f4bc3143e67e6491f6a48234c224cef1cc`).
  Brouillon 3 : reprise à 18:16:19 sur la contre-lecture 1, écrit de 18:19:51 à 18:25:08, scellé comme brouillon
  (`49b0921d585944fd1e326bdea6155ad67e64719d6ab2673a022f415f084f256a`). Version : reprise à 18:48:07 sur la vérification 1 des
  corrections, écrite de 18:52:44 à 18:55:12 (`date -u` relevé juste avant le dernier passage du validateur).
- **Commit du code d'analyse** : **aucun code n'existe**. Par le choix de forme de la mère (R-3334), le code est cité après le
  scellement, par la ligne `CODE-LENTILLES-BBIS` du registre propre, inscrite avant toute exécution (écart au gabarit, déclaré). Commits
  lus : branche de travail de la mère `claude/affectionate-bardeen-j7kddp` à `ba8dcfbf076e936729ee6668b9774031337d0a3e` (tête relevée
  à 17:56) ; branche des lentilles `claude/brave-galileo-jhp684` à `310ca57b2b1bc2586b35571d8f6e84d313ab36ec` ; branche principale à
  `ca7f8f48e8d58d088414e64b604540e212bd929d` (copies des sources).
- **Documents qui font foi (chemin + empreinte)** :
  - mandat (ci-dessus) ; brouillons 1 et 2 (ci-dessus) ; rapport de la contre-lecture 1,
    `prereg/contre-lectures/lecture-sondes-bbis-par-lentilles-v1-brouillon2-cl1.md`,
    `f876f83a250dce85d83ab6e73f8ec0d40ffbc33640d625962838f774e3b94ea2` ;
  - brouillon 3, `prereg/lecture-sondes-bbis-par-lentilles-v1-brouillon3.md`,
    `49b0921d585944fd1e326bdea6155ad67e64719d6ab2673a022f415f084f256a` ; rapport de la vérification 1 des corrections,
    `prereg/contre-lectures/lecture-sondes-bbis-par-lentilles-v1-brouillon3-verif1.md`,
    `5398f2e90f2dac1b5243601f89d609fb3c2a24773126b3391cfdab8953d5aedc` ; mandat de cette vérification,
    `docs/notes/neuron-lens-v1/mandat-verification-corrections-texte-lentille-publique-v1.md`,
    `71dbd76ab3d277d10e4e4fa8ec6c8dc42bc8b8ecab1160b442b024d5a266fc34` ;
  - apprentissage des sondes sur la tâche, lus **pour la forme de leurs sorties seulement** : texte scellé
    `prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb` (« T ») ; premier addendum
    `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`, `f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7` (« A1 ») ;
    second, `…-addendum-ecart-2-v1.md`, `18baeac32d26ebf174c62d7a36caedeee1d5b80648c6743c21dc30d2747afd26` (« A2 ») ; troisième,
    `…-addendum-ecart-3-v1.md`, `e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872` (« A3 ») ;
  - code qui écrit les deux fichiers lus (branche de travail ; **code, jamais des données**), pour les noms exacts des clés et des
    champs : `src/controle_ia/t07bbis/marche_v4.py` (`ecrire_fermes`, l. 139-192),
    `c63f778055895c545922de0b3ea232c6318fc8f54cf0917ce099cb3acdd27d23` ; `src/controle_ia/t07bbis/validation_imbriquee_v1.py`
    (`apprendre_recette`, l. 214-262 ; `apprendre_source`, l. 350-396),
    `1ffb6e4d282dd76afa1b01cf16b748c444174e212f410f8c460ab90d8fe45390` ; `src/controle_ia/t07bbis/validation_imbriquee_v4.py`
    (`meta["ordre2"]`, l. 222-260, par recherche), `3d40ebc80e2bbf7faf33bfe8a4ef6e7d8f26df9df93507ad79a85d4c766d2c6c` ;
    `src/controle_ia/t07bbis/commun_v1.py` (`FAMILLES`, `AGREGATION_DE`, `cellules`, `reglage_nom`),
    `9db2b40b15c9ca76f0c4bd4f29923cc06909b362de26a212bfc780133a4c9e33` ; `src/controle_ia/t07bbis/apprentissage_carte_v1.py`
    (l. 117-123 : la sonde rendue), `4b98fcb931d0ea09e663c7c3093f294db8630537e4322e44b69ba2d50bd743d7` ;
    `src/controle_ia/t06/configuration.py` (`nom_condition`, l. 42-48), `fe859b9a0016cb3fdd69002a37bf26fc344405875ebe6f9ec95ee3a47be71553` ;
    empreintes de ce code inchangées à la tête `70bdd769b9e788d073a832073ce983dd8a0b4a87` de la branche de travail (vérification 1),
    et à la tête `19947280cd22811bdae109708eac6c5e0626606c` (relevé du rédacteur, 18:49 UTC) ;
  - lentille publique, copies versées (branche principale, dossier `docs/sources/neuron-lens-lecture-20261113/huggingface/`, relevées
    le 2026-11-13 à la tête `d2527c3cdbaa60dd4b65cbca1604921f044e989a` du dépôt, manifeste `manifeste-sources-v2.tsv`,
    `6d679182bbbb3f73257a74e603594d1125702ad115aacc4e3622f0e9e268efd8`) : fiche `lentilles-neuronpedia-jacobian-lens-fiche.md`
    (`b8136cc4f6b98d654ebae5de9ea922bc11ac91ac7f14c637a221faad074f74d0`), réponse de l'interface `lentilles-neuronpedia-jacobian-lens-api.json`
    (`aa55ef2600652385ba7ceb1b59d3c7872a7a01d62184273be6941a77c6eceda5`), arbre `lentilles-neuronpedia-jacobian-lens-arbre.json`
    (`273c7eb63c762ad0754f7f4995a48307530ecc24f6ce7e5dc2396e42e09278ed`), notice `neuronpedia-llama3.1-8b-it-NOTICE.txt`
    (`cef69845083ec09f5487c9073fdc06e72f5641cbffb51c6e90459ab3dbd9e981`), crédit `neuronpedia-llama3.1-8b-it-rlens-CREDIT.md`
    (`d4b8dc5563d786b5a674caf73b7814eb4440a725613d90cd74cbbf211e9e7f1b`), configuration `neuronpedia-llama3.1-8b-it-rlens-config.yaml`
    (`67dd6376c593eefb06f084cd69eaddb0b194f45d3248240dba0f1afa1b78d964`) ;
  - code voisin `stdlogits/neuron-lens` (licence MIT) : copie de `neuron_lens/readout.py` versée
    (`docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/neuron_lens-readout.py.txt`,
    `2c0fe9951f98523c8652383b62b3da30b5777e8c1eccc4b3891c1af6ee816184`, relevée le 2026-11-13 sur la branche `main` du voisin ; le code
    employé est celui du commit `849bfe1678e28becceb1e3864afe5fc8297d02e4`, comme la tranche des lentilles) ;
  - tranche de l'ajustement de nos lentilles (branche des lentilles, dossier `docs/notes/neuron-lens-v1/`), lue **pour sa recette de
    lecture seulement** : texte gelé `texte-gele-tranche-b-beta-v1.md`, `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454`
    (« G ») ; addendum des empreintes, partie 1, v3, `addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md`,
    `bd8067dcd04ae32bb5960dc95bef89384b3b914a1a35e918107411f43d1c95f1` ; correctif (2), chargement des lentilles de Neuronpedia,
    `correctifs/lenses-neuronpedia-llama-v2.diff`, `616434bc98394c191e00ae02cb9342317e7fbdaea780d771224babc45c12a3bc` ; correctif (4),
    comparaison des lentilles, `correctifs-b-beta/lens_compare-llama-v2.diff`,
    `f85c36db1dd5722e0570cdd0a1544db565ff93ff8aa578497610960dcf4feca3` ; correctif (6), provenance « chat »,
    `correctifs/provenance-chat-llama-v1.diff`, `fec2c0a7f298ea8b786ccfe9e7b406c6406549caab740d8cfe18f54689b9b73f` (compagnon lu) ;
    inventaire du code voisin pour Llama, `inventaire-code-voisin-llama-b-beta-v1.md`,
    `e194592019d2d54339a079dfc368fc8ad1da06db4b1c34a0d4209101cafbeaa3` ;
  - gabarit `prereg/gabarit-preregistrement-v1.md`, `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` ; validateur
    `src/controle_ia/prereg.py`, `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` ;
  - code lu pour définir la direction d'une sonde et sa couche : `src/controle_ia/sondes/familles.py`,
    `6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e` (l'empreinte que cite T) ;
    `src/controle_ia/harnais/activations.py`, `adeb5856d430f3a6163989c2a53c8ced459235c6dcdd03834b694404c57e0095` (l. 1-80).
- **Statut** : **version v1, texte candidat, non scellé** ; aucun calcul, aucune dépense, aucun résultat lu. La session mère le
  scelle, après un contrôle de la différence (brouillon 3 → version) par un agent neuf, par `controle_ia.prereg.sceller_prereg` (qui
  refuse un texte non conforme). **La ligne `SCELLEMENT-LENTILLES-BBIS` n'est inscrite que si `VERDICT-BBIS` est absente à ce moment ;
  la mère le relève par les clés seulement** (règle la plus stricte, la même qu'au « Plan d'analyse », point 1, et qu'à la « Liste
  d'arrêt ») ; présente à ce moment : texte exposé, nœud. Les expositions de qui a écrit les dernières corrections sont déclarées
  ci-dessous (« Déclaration de la session mère »).

## Ce que l'auteur savait avant le scellement

- **Lu au brouillon 1** : le mandat ; T (entier, pour la forme des sorties) ; A2 (l. 1-48 et 216-353, et les lignes qui nomment branche,
  fichiers des sondes et des scores) ; A3 (l. 1-95, et les lignes qui nomment la branche de sortie) ; A1 (les seules lignes qui nomment
  branche, fichiers, couche ou direction, par recherche) ; G (l. 1-560) ; l'addendum des empreintes v3 ; la commande v6 de la tranche
  des lentilles ; le devis v12 (lieux de rangement et § 4) ; l'en-tête de `verification-courte-commande-v13-v14-mere-v1.md` ; le
  gabarit, le validateur, `sondes/familles.py`, `harnais/activations.py` (l. 1-80), quelques lignes de `scellement.py` ; `CLAUDE.md`.
- **Lu au brouillon 2** : les correctifs (2) et (4) et l'inventaire du code voisin (par recherche de lignes) ; la copie de `readout.py`
  (l. 1-80) ; les six copies des sources de la lentille publique ; les lignes du manifeste des sources qui les nomment ; l'en-tête de la
  licence du voisin (MIT) ; l'**arbre public des fichiers de Llama** à la révision épinglée, relevé le 2026-11-18 à 18:00:15 UTC (sans
  clé ; réponse non versée, `5edd74c6a7c760e42e143a7cca841a242d561973cac01ceed70b75d707f3dbb1` ; empreintes SHA-256 des fichiers de poids
  masquées dans la réponse, seuls identifiants git et tailles lus) ; les **noms** des variables d'environnement de la session ; un
  **banc de calcul sur des matrices aléatoires** (≈ 334 GFLOP/s, 4 fils, simple précision).
- **Lu au brouillon 3** : le rapport de la contre-lecture 1 (entier) ; le **code** de `src/controle_ia/t07bbis/` cité ci-dessus (lignes
  citées, et des lignes rendues par des recherches de noms dans `marche_v4.py`, `validation_imbriquee_v1.py` à `v4.py`,
  `commun_v1.py`, `apprentissage_carte_v1.py` et `lecture_v1.py` à `lecture_v3.py`) ; `t06/configuration.py` (l. 42-48) ; le compagnon
  du correctif (6) ; les identifiants git des fichiers de licence dans l'arbre versé ; un calcul des quantiles d'une loi binomiale
  (aucune donnée).
- **Lu pour la version** : le rapport de la vérification 1 des corrections (entier, compagnon vérifié), dont les valeurs qu'il cite
  (bornes, risques, comptes de lectures, têtes de branche) ; le chemin et l'empreinte de son mandat (sans lecture) ;
  `src/controle_ia/t07bbis/plis_v1.py`, l. 318-328 (code : clés des champs de l'action, V-m13) ; `src/controle_ia/prereg.py`
  (`sceller_prereg`, l. 63-67) ; empreintes du code cité recalculées à la tête `19947280cd22811bdae109708eac6c5e0626606c` ; un calcul
  des lois bêta-binomiale et binomiale (aucune donnée ; script et sortie versés dans
  `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/`).
- **Valeurs vues** (aucune n'est une aire, un score, une issue ou un verdict d'une chaîne interdite) : celles déclarées aux brouillons 1
  et 2 ; au brouillon 3, des **constantes du code** de l'étape B bis (couches 7, 15, 23 ; familles ; grille de régularisation 10⁻³,
  10⁻², 10⁻¹ ; 800 directions du plancher ; 100 réétiquetages ; niveaux décisifs 0,99 et 0,995, niveau de réserve 0,95, seuil des
  dégénérés 0,01, tolérance carte 10⁻⁴ ; nom du dossier de course de 7b `20261111-151701-t06-reel`), et les valeurs de contrôle que cite
  le rapport de contre-lecture (empreintes, tailles, identifiant git `16780aaa…` du pointeur de la lentille publique, succès d'une
  lecture partielle de cette lentille par le réseau).
- **Vu sans ouvrir** : ce que déclarent les brouillons 1 et 2 (dont le dossier `docs/notes/lentilles-sondes-p3-v1/`, une ligne de
  contrôle de `lecture-b-alpha/verdict-b-alpha-v1.md`, les noms des dossiers de `/home/user/`) ; au brouillon 3, le chemin du mandat de
  la contre-lecture (`docs/notes/neuron-lens-v1/mandat-contre-lecture-texte-lentille-publique-v1.md`, empreinte relevée sans lecture :
  `9688f84d3b84ed71333dff5b89f5031ce27a07ba2a6003f833753dc452588843`).
- **Jamais vu** : aucun fichier sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucune branche `calcul/` ou `donnees/` ; aucun
  fichier de `registres/` ; aucune sortie de 7a, 7b, T0.6, T0.7 (étape A comprise), de la base « mots et coût », de l'étape B, de
  l'apprentissage des sondes sur la tâche, de P3, de P3-bis ; aucun résultat des tranches de la lecture par lentille neuronale (seule la
  ligne de contrôle déclarée). **Aucun choix de ce texte n'a pu être fait d'après une sortie de ces chaînes.** La mère, exposée depuis à
  un résultat du programme, n'a fixé aucun choix d'analyse : mesure, nuls, libellés et seuils de libellé sont de l'auteur ; les
  corrections du brouillon 3 suivent les remarques de la contre-lecture.
- **Déclaration de la session mère** (vérification 1, V-m11 et « ce que la version finale doit porter », point 4) : la session mère est
  exposée à un résultat du programme (le verdict du barreau « accumulation des scores sur l'épisode », R-3347) et à aucune sortie de
  l'étape B bis ; elle n'a fixé aucun seuil, critère ni choix d'analyse de ce texte ; les changements du brouillon 3 à la version sont
  l'application des couples du rapport de vérification et des trois options (a), rien d'autre. Le rédacteur, qui a écrit ces
  changements, n'a lu aucun résultat du programme (ci-dessus).

## Vocabulaire (noms en clair ; les identifiants viennent en appui)

- **Apprentissage des sondes sur la tâche** : l'étape B bis de T0.7 (T, A1 à A3). Ses **cellules plafond** (`commun_v1.cellules`) :
  l'organisme à consigne cachée (`P-instruit`) et l'adaptateur saboteur aux doses 0,25 à 1 (`P-S25`, `P-S50`, `P-S75`, `P-S100`) ; deux
  **plis externes** par cellule (`e0`, `e1`). **Sonde apprise** : la sonde finale d'une cellule et d'un pli (T, plan, point 5). **Lecteur
  honnête à capacité égale** : la même recette, apprise sur les activations du modèle nu lisant les mêmes textes (ENC dans T, `enc` dans
  le code).
- **Direction d'une sonde** : le vecteur `w` de l'interface du harnais, dans les coordonnées brutes du flux résiduel à la couche ℓ de la
  sonde (sortie du bloc ℓ, avant la normalisation finale : `harnais/activations.py`, l. 3-5), normalisation repliée (`w' / s` :
  `sondes/familles.py`, l. 16-18 et 233-237 ; `apprentissage_carte_v1.py`, l. 118-120) ; pour la famille « attention », aussi la
  **requête** `q`, dans les mêmes coordonnées. C'est un **vecteur de lecture** (la sonde calcule `w·h`) ; ce texte le **lit comme une
  direction écrite** dans le flux (convention, « Frontière », point 3). **Signe +** : vers la classe positive (saboteur pour une sonde
  apprise ; texte du saboteur relu par le modèle nu pour un lecteur honnête).
- **Lentille publique côté sortie** (`npR` dans les pièces de la tranche des lentilles) : la lentille R de Llama 3.1 8B Instruct publiée
  par Neuronpedia, ajustée par un tiers (« Entrées exactes ») : une matrice J_ℓ de 4 096 × 4 096 par couche ℓ de 0 à 30, prise à la
  sortie du bloc ℓ, qui transporte ce qu'une direction écrite dans le flux pousse vers le dernier flux. **Lentille des logits** : J_ℓ =
  identité. **Nos lentilles** (celles qu'ajuste la tranche de l'ajustement de nos lentilles) : **n'entrent pas dans ce texte**.
- **Jetons gardés** : les jetons de Llama comptés au moins 5 fois dans le corpus d'activations du voisin et dont le décodage ne contient
  pas « � » (`catalog.kept`, G, P.3 ; 89 498 jetons ; le jeton de début de Llama, 128 000, en fait partie, constat de G).
- **Pôle** : un neurone à porte du bloc ℓ, pris à un signe (deux par neurone, 28 672 par couche).
- **Nul isotrope**, **nul des signes**, **concentration**, **part au-dessus du nul**, **familles de jetons nommées d'avance**, **pôles
  alignés**, **rapport à ε** : définis en « Métrique ».

## Hypothèse

- **Objet, descriptif** (mandat ; question de Lazar, pour que la lecture par lentille neuronale entre dans le billet sur les sondes ;
  voie tranchée par Lazar : lentille publique seule, au processeur, GO-2026-11-18-42, R-3349) : décrire quels jetons et quels pôles la
  lentille publique côté sortie associe aux directions que l'apprentissage des sondes sur la tâche aura apprises, **lues comme des
  directions écrites dans le flux**, à la couche où chaque sonde lit, et si cette lecture se distingue de directions aléatoires.
  **Aucune revendication, aucune hypothèse soumise à un seuil de rejet.** Aucune hypothèse du programme (H1 à H8, HC) n'est testée,
  modifiée ni revendiquée ; rien n'entre dans G0 (critère 3 compris), G1, T0.7 ni T0.8 sans nœud de Lazar. Le mot de Lazar (R-3349)
  vaut aussi le mot de la passerelle qu'exige GO-2026-11-17-03 pour employer la recette d'une tranche hors programme sur des sondes du
  programme.
- **Questions** : par la lentille publique côté sortie, à la couche de la sonde : (i) quels sont les premiers jetons de chaque direction,
  et la lecture est-elle plus concentrée que celle de directions aléatoires ? (ii) les familles de jetons nommées d'avance (« nombres »,
  « coût ») y sont-elles plus fréquentes que sous le nul ? (iii) quels pôles de la couche écrivent le plus près de la direction, et que
  lit la lentille de ces pôles ? (iv) en quoi la lecture d'une sonde apprise diffère-t-elle de celle du lecteur honnête de même cellule,
  de l'autre pli, des autres doses, et de la lecture par la lentille des logits ?
- **Hypothèses de travail** : modèle `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659` (celle de
  T et de la lentille publique) ; une lecture par lentille dit ce qu'une direction **pousse en moyenne**, non ce qu'elle fait sur un
  épisode (G, « Critères ») ; **règle de lecture** reprise de G : une lecture par lentille peut ajouter un soupçon sur une sonde, jamais
  la blanchir.
- **Indice de couche, tenu par convention et non par un essai** : la couche ℓ d'une sonde (7, 15 ou 23 ; T ; `commun_v1.COUCHES_REELLES`)
  est la sortie du bloc ℓ, indice depuis 0 (crochet sur `model.layers[ℓ]`, `harnais/activations.py`) ; la couche ℓ de la lentille
  publique est prise au même point (« block_output », couches sources 0 à 30, configuration de la lentille, et clé `provenance` du
  fichier, exigée lisible : « Liste d'arrêt ») ; le voisin lit la colonne de `W_down` du bloc L par J_L, même convention. Un décalage
  d'un cran entre ces deux conventions **n'est pas testable ici** (il faudrait une passe avant du modèle, impossible au processeur dans
  15 Go de mémoire) ; seul le code est éprouvé : il lit la matrice d'indice égal à la couche de la sonde (essai à signature, « Code
  neuf »).
- **Lectures rivales que la description éclaire, sans les départager** : la sonde lit le texte (comparaison au lecteur honnête) ; elle
  lit le nombre déclaré ou le champ du coût (familles « nombres » et « coût » ; c'est la lecture sans le champ du coût de T qui en
  traite) ; elle lit une structure de surface (nul des signes, témoin de couche).

## Prédiction chiffrée et signe attendu

R3 : aucune course ne vise un signe ; texte descriptif, **aucune prédiction n'est décisive**. Attentes de l'auteur, déclarées pour
mémoire, chacune avec ce qui la réfuterait ; une attente réfutée est rapportée et ne change rien.

| attente | réfutée si | confiance |
|---|---|---|
| A-1 : au moins une des dix sondes apprises est, par la lentille publique côté sortie à sa couche, « concentrée au-delà des deux nuls » (« Critères de lecture gelés »), à un signe au moins | aucune ne l'est | 0,55 |
| A-2 : la famille « nombres » ou la famille « coût » est « sur-représentée » dans les vingt premiers jetons d'au moins une sonde apprise sur l'adaptateur saboteur (`P-S25` à `P-S100`), par la lentille publique côté sortie | aucune ne l'est | 0,35 |
| A-3 : parmi les directions lues aux couches 23 et 7, la part des lectures « concentrées » par la lentille publique est plus haute à 23 | part plus haute ou égale à 7 ; sans objet si l'une des deux couches n'a aucune direction | 0,5 |
| A-4 : à même cellule, même pli et même couche, le cosinus entre la sonde apprise et le lecteur honnête est positif pour la plupart des paires | positif pour la moitié des paires ou moins ; sans objet sans paire de même couche | 0,6 |

## Entrées exactes, et ce qui n'est jamais ouvert

**De l'apprentissage des sondes sur la tâche** (course du second addendum, chaîne v6 du troisième ; branche de sortie
`donnees/t07-etape-b-bis-v2`, A2, SA-16 ; A3, TA-1 ; `<run-bbis>` = le dossier de course nommé par la ligne `SCORES-BBIS` de son
registre propre, `registres/t07-etape-b-bis-v1.md`). Noms des clés et des champs relevés dans le code cité (« Documents ») ; le
développeur les vérifie dans le code au commit cité par la dernière ligne `CODE-BBIS` (lecture de code, jamais des données) ; un nom
différent : arrêt (« forme mal comprise »).

- **E-2** `diag/<run-bbis>/sondes-bbis.json` (écrit par `marche_v4.ecrire_fermes`) — analysé en entier par le programme (JSON), mais
  **seuls les champs de la liste blanche sont extraits** ; rien d'autre n'est gardé, imprimé, journalisé ni écrit. **Liste blanche, noms
  exacts** :
  - à la racine : `run_id` ; `fichier_sondes.fichier` et `fichier_sondes.sha256` (chemin et empreinte de E-1) ; les **clés** de
    `sources` (noms des cellules) et, sous chacune, les **clés** `e0`, `e1` ;
  - sous `sources/<cellule>/e<k>`, **au niveau direct seulement** (jamais dans le sous-dictionnaire `ordre2`, qui porte les champs de la
    sonde de l'ordre 2 sous les mêmes noms) : `cellule`, `pli_lu`, la **présence** de la clé `echec` (jamais sa valeur), `famille`,
    `couche`, `agregation`, `empreinte_sonde`, `nom_sonde` (sonde apprise) ;
  - sous `sources/<cellule>/e<k>/enc` (lecteur honnête) : la **présence** de la clé `echec` (jamais sa valeur), `reglage` et
    `empreinte`. **`reglage` est une chaîne `famille-c<couche>-l2_<régularisation>`** (`commun_v1.reglage_nom`) : le code n'en garde que
    la famille et la couche, par l'expression `^(lineaire|attention)-c([0-9]+)-l2_` ; **la régularisation (suite de la chaîne) n'est
    ni gardée, ni écrite, ni imprimée** ; chaîne d'une autre forme : arrêt (« forme mal comprise »). Agrégation du lecteur honnête
    déduite de sa famille (`commun_v1.AGREGATION_DE` : `lineaire` → `max`, `attention` → `attention`) ; son nom, pour l'empreinte :
    `enc-<cellule>-e<k>` (`validation_imbriquee_v1.apprendre_recette`, l. 255) ;
  - **exclus**, entre autres : `reglage` et `l2` de la sonde apprise, `taches_lues`, `plis_internes`, `echecs_internes`, `n_plancher`,
    `noms_deux_premieres`, `empreintes_deux_premieres`, `nuls_en_echec`, `n_reetiquetages`, `ordre2`, `enc.echecs_internes`, la valeur
    de tout `echec`, `fichiers_scores`, `fichiers_planchers`, `graines_derivees`, `controle_carte_processeur`, `couple_controle`,
    `journal`, `variante`, `decision_variante`, le résumé de la mesure de dispersion (`dispersion_ordres_calcul`), `doses`, `couches`,
    `plis`, `manifeste`, `duree_s`, `texte`, `sans_aucune_aire`.
- **E-1** `donnees/<run-bbis>/sondes-bbis.npz` (même fonction ; archive `numpy` non compressée, une entrée par tableau) — son SHA-256
  est calculé sur les octets du fichier entier (aucun tableau décodé) et comparé à `fichier_sondes.sha256` et au compagnon ; puis le
  fichier est **ouvert clé par clé** (`numpy.load(…, allow_pickle=False)`, liste des noms d'entrées seulement) et **seules les entrées
  `<cellule>__e<k>__sonde_w`, `…__sonde_b`, `…__sonde_q` (si elle existe), `…__enc_w`, `…__enc_b`, `…__enc_q` (si elle existe) sont
  décodées** ; les entrées `<cellule>__e<k>__direction0_{w,b,q}` et `…__direction1_{w,b,q}` du même fichier, qui sont les **deux
  premières directions du plancher**, ne sont **jamais décodées** ; tout autre nom d'entrée : arrêt. `…__sonde_b` et `…__enc_b` sont
  des tableaux d'un élément.
- **Empreinte de chaque sonde recalculée** (`familles.SondeLineaireJetons.empreinte`, l. 83-85, et `_empreinte`, l. 57-61 : SHA-256 de
  `"<famille>:<nom>/<couche>/<agrégation>"` puis des octets en double précision de `w`, `[b]` et `q` s'il existe) : sonde apprise avec
  `nom_sonde`, `famille`, `couche`, `agregation` ; lecteur honnête avec `enc-<cellule>-e<k>` et la famille, la couche, l'agrégation
  déduites ci-dessus ; comparée à `empreinte_sonde` et à `enc.empreinte`.
- **Attendu** : vingt sondes (cinq cellules × deux plis × deux rôles), moins celles que le code marque. Trois formes sont prévues par le
  code (`validation_imbriquee_v1.apprendre_source`, l. 362-364 et 387-394 ; `marche_v4.ecrire_fermes`, l. 151-173), et elles seules sont
  admises : (a) clé `echec` présente au niveau direct : `famille`, `couche`, `agregation`, `empreinte_sonde`, `nom_sonde` et le
  sous-dictionnaire `enc` sont absents, et E-1 ne porte aucune entrée de cette cellule et de ce pli ; la sonde apprise est « non lue :
  échec à l'apprentissage », son lecteur honnête « non lu : non appris, la sonde apprise ayant échoué » ; (b) clé `echec` absente au
  niveau direct et présente sous `enc` : `enc.reglage` et `enc.empreinte` sont absents, et E-1 ne porte aucune entrée `enc_*` de cette
  cellule et de ce pli ; le lecteur honnête est « non lu : échec à l'apprentissage » ; (c) aucune clé `echec` : tous les champs de la
  liste blanche sont présents, ainsi que les entrées `sonde_w`, `sonde_b`, `enc_w`, `enc_b` ; `sonde_q` existe si et seulement si la
  famille de la sonde apprise est `attention`, `enc_q` si et seulement si celle du lecteur honnête l'est. Toute autre combinaison :
  arrêt (« forme mal comprise »). Les cellules de transfert n'ont pas de sonde propre (T, plan, point 9).
- **E-3** les compagnons `.sha256` de E-1 et E-2 ; la ligne `SCORES-BBIS` (chemin, empreinte) ; la présence de la clé `VERDICT-BBIS`
  dans le même registre (clé et heure seulement, jamais le fichier du verdict) ; la ligne `CODE-BBIS` du même registre (clé, heure, chemin de la fiche, commit seulement), dont le
  commit sert au développeur à vérifier les noms ci-dessus. **Des registres, l'opérateur ne lit que ces clés et
  heures, et les lignes du registre propre de ce texte.**
- **Moment** (choix de forme de la mère, R-3334) : E-1 et E-2 ne sont ouverts par programme **qu'après** l'inscription de
  `VERDICT-BBIS`, et récupérés seuls, par leur chemin (clone partiel sans contenus, `--filter=blob:none`, puis extraction de ces deux
  chemins et de leurs compagnons seulement ; aucun autre contenu de la branche des données n'est téléchargé).

**Jamais ouverts**, par personne de cette chaîne ni par son code : `donnees/<run-bbis>/scores-bbis-NNN.npz` (scores de la sonde, des
800 directions du plancher, des 100 sondes du nul de réétiquetage, du lecteur honnête, de la lecture sans le champ du coût, scores
d'apprentissage, **et poids des sondes de l'ordre 2**, qui ne sont donc pas lues ; A2, SA-17) ; `donnees/<run-bbis>/planchers-bbis-NNN.npz`
(directions du plancher) ; **les entrées `direction0_*` et `direction1_*` de E-1** ; `diag/<run-bbis>/relecture-bbis.json` ;
`runs/<run-bbis>/manifeste.json` ; tout journal de la course ; `lecture-bbis.json`, `conjointe-bbis.json`, tout fichier de verdict ; la
branche `donnees/t07-etape-b-bis-v1` (course arrêtée le 16 novembre) ; `lecture-t07.json` ; toute sortie de 7a, 7b, T0.6, T0.7 (étape A
comprise), de la base « mots et coût », de l'étape B, de P3, de P3-bis ; le dossier `docs/notes/lentilles-sondes-p3-v1/` ; tout dossier
de course présent dans un conteneur (`/home/user/bbis-*`, `/home/user/vastai-env-*` et semblables) ; toute pièce de l'étiqueteur, du
bras d'attaque ou du mode tenu à l'écart ; aucune sortie des tranches de la lecture par lentille neuronale (seule la ligne du verdict
d'ensemble de la tranche des lentilles publiques est recopiée, par le lecteur, « Critères de lecture gelés »).

**La lentille publique côté sortie** (seule lentille ajustée lue par ce texte) :

| objet | valeur |
|---|---|
| dépôt, révision | `neuronpedia/jacobian-lens` (Hugging Face, public, sans porte), révision `d2527c3cdbaa60dd4b65cbca1604921f044e989a` (addendum v3, § 2 ; tête du dépôt au relevé des copies du 2026-11-13) ; **passée explicitement au téléchargement** par notre code (le chargeur du correctif (2) ne la passe pas) |
| fichier | `llama3.1-8b-it/rlens/Salesforce-wikitext/Llama-3.1-8B-Instruct_rlens.pt`, **1 040 198 745 octets**, identifiant git du pointeur `16780aaadd10cfe8c23c8ba522a95941314cc362` (arbre versé) |
| empreinte SHA-256 | `a63a1588f2cb61850c68131a5f13b74590f4fe137f67bf80c627547d2230d31c` (arbre versé ; correctif (2), table `NEURONPEDIA_SHA256` ; addendum v3, § 2) |
| contenu attendu | `{"J": {0..30: [4096, 4096]}}` en demi-précision, plus la clé `provenance` (la configuration la dit « authoritative ») ; 31 couches sources, 0 à 30, point de capture `block_output`, sans réduction (configuration de la lentille) |
| provenance | ajustée par « bubskee » (financement BlueDot Impact), méthode « R-lens » de Blank, Bhatia et Nanda (2026), code J++ de Ayonrinde et Lindsey (`safety-research/jpp_lens`, Apache-2.0), 64 textes de `Salesforce/wikitext`, 128 jetons au plus ; source `bubskee/llama-3.1-8b-instruct-r-jpp-lenses`, révision `9b72394293d91247bb3ad9ad703884157cc838c6`, fichier `lenses/r.pt` (`de4355c69d0d01eb7e9b32b94a938b0d43b766680fac396e11a6458b8f8fd309`) ; convertie par Neuronpedia de la simple à la demi-précision (erreur relative maximale 2,6·10⁻⁴), sans autre changement (crédit et configuration versés) |
| licence | **Llama 3.1 Community License** et sa politique d'usage acceptable : fichiers du dossier `llama3.1-8b-it/` du dépôt, comparés par identifiant git et taille : `LICENSE` (7 627 octets, `a7c3ca16cee30425ed6ad841a809590f2bcbf290`, le même que celui du dépôt de Llama), `NOTICE` (403 octets, `1fda666c122e76b7dcb57c8719572236ca3984a7`), `USE_POLICY.md` (4 691 octets, `81ebb55902285e8dd5804ccf423d17ffb2a622ee`, le même que celui du dépôt de Llama) ; fiche, section « License » ; crédit, section « License ». Usage de recherche ici ; le fichier n'est ni modifié, ni versé, ni redistribué ; toute publication d'un résultat porte « Built with Llama » (notice) et passe par un nœud de Lazar |

**Poids et tokeniseur de Llama** (licence Llama 3.1 Community License ; dépôt à porte, clé requise), révision
`0e9e39f249a16976918f6564b8830bc894c89659`, identifiants git et tailles relevés par l'auteur dans l'arbre public :

| fichier | taille (octets) | identifiant git |
|---|---|---|
| `model-00001-of-00004.safetensors` | 4 976 698 672 | `a59dca28867995c0d05384251ac5f4d62461a226` |
| `model-00002-of-00004.safetensors` | 4 999 802 720 | `4ab0726caf5e75dd1e5700c7e7899ac8c0798428` |
| `model-00003-of-00004.safetensors` | 4 915 916 176 | `5864b15557563e7700a3f95236afdee36f5fdb74` |
| `model-00004-of-00004.safetensors` | 1 168 138 808 | `b8babcaa5a888d6efd5c05206361b4685492ad13` |
| `model.safetensors.index.json` | 23 950 | `0fd8120f1c6acddc268ebc2583058efaf699a771` |
| `tokenizer.json` | 9 085 657 | `5cc5f00a5b203e90a27a3bd60d1ec393b07971e8` ; SHA-256 `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` (G) |
| `tokenizer_config.json` | 55 351 | `db88166e2bc4c799fd5d1ae643b75e84d03ee70e` |
| `special_tokens_map.json` | 296 | `02ee80b6196926a5ad790a004d9efd6ab1ba6542` |
| `config.json` | 855 | `0bb6fd75b3ad2fe988565929f329945262c2814e` |
| `LICENSE` ; `USE_POLICY.md` | 7 627 ; 4 691 | `a7c3ca16cee30425ed6ad841a809590f2bcbf290` ; `81ebb55902285e8dd5804ccf423d17ffb2a622ee` |

Pour un fichier de poids, l'identifiant git est celui de son **pointeur** de stockage, qui contient son SHA-256 et sa taille : le code
relit le SHA-256 dans l'interface (avec la clé), reconstruit le pointeur, vérifie que son identifiant git égale celui de la table
(méthode éprouvée par la contre-lecture sur le pointeur de la lentille publique), puis compare le SHA-256 calculé sur le flux
téléchargé. Pour un petit fichier, l'identifiant git est recalculé sur son contenu. Tenseurs gardés : `lm_head.weight`,
`model.norm.weight`, `model.layers.{7,15,23}.mlp.down_proj.weight` (la liste des fichiers qui les portent est lue dans l'index).

**Code voisin et corpus des jetons gardés** : `stdlogits/neuron-lens` au commit `849bfe1678e28becceb1e3864afe5fc8297d02e4` (MIT), avec
le correctif (6) (`fec2c0a7f298ea8b786ccfe9e7b406c6406549caab740d8cfe18f54689b9b73f`, branche `prep/neuron-lens-v1`) pour le corpus, et
les correctifs (2) et (4) pour la garde de la fonction de lecture ; corpus d'activations du voisin
(`05_act_corpus.py --docs dclm=40000,zh=8000,code=8000,chat=8000`, révisions de l'addendum v3, § 3) ; `03_token_counts.py` une seule fois ;
liste `catalog.kept` attendue : **89 498 identifiants**, `c37186add16770aa3c04bd0c16c417544b7e2a15b374ee85e47fbda7ec148d68` (addendum
v3, § 3). Le corpus ne sert qu'aux comptes de jetons ; il n'est pas versé.

## Métrique

1. **Directions lues** : pour chacune des vingt sondes de E-1, `w` et, pour la famille « attention », `q` (au plus quarante vecteurs),
   chacun aux deux signes. Norme nulle ou valeur non finie : « non calculable » (motif écrit).
2. **Lecture** d'un vecteur v à la couche ℓ par une lentille de matrice J_ℓ (lentille publique : J_ℓ du fichier, converti en simple
   précision ; lentille des logits : identité), **v étant traité comme une direction écrite dans le flux** (convention, « Frontière »,
   point 3) : la convention de `neuron_lens.readout.read` du voisin (copie versée, l. 12-44) : t = RMSNorm(J_ℓ v) · γ, avec
   γ = `model.norm.weight` et ε = 10⁻⁶ comme publié (Llama emploie 10⁻⁵ : écart constaté par G, gardé) ; score du jeton gardé t :
   a_t(v) = (W_U t)_t, W_U = lignes gardées de `lm_head.weight`. Notre code rend le **score de chacun des 89 498 jetons gardés**.
   **Précision** : tout en simple précision (conversion exacte des poids en bfloat16 et de la lentille en demi-précision) ; écart
   déclaré à la comparaison des lentilles de la tranche, qui fait le produit par W_U en demi-précision (correctif (4), l. 47 du fichier
   corrigé) ; contrôlé par la garde de la fonction de lecture (plan, point 5). RMSNorm étant impaire, a_t(−v) = −a_t(v) : un seul
   calcul rend les deux signes.
3. **Rapport à ε et indépendance à la norme** : pour tout vecteur lu x (direction réelle à sa norme lue dans E-1, direction nulle,
   direction témoin), ρ(x) = moyenne des carrés des coordonnées de J_ℓ x, divisée par ε. Si ρ(x) ≥ 100, la lecture de x ne dépend de
   sa norme qu'à un facteur d'échelle commun près, compris entre 1 et 1 − 1/(2ρ) (au plus 0,5 %) : c'est l'**indépendance à la norme**,
   qui permet de partager le nul isotrope entre les directions d'une couche. Elle n'est **pas supposée** : elle est gardée (plan,
   point 6, garde du rapport à ε).
4. **Lecture côté entrée** : **non faite** : aucune lentille côté entrée publique n'existe pour Llama dans le dépôt (lentilles J, J++
   et R seulement, arbre versé) ; « non lue : aucune lentille côté entrée publique ».
5. **Deux nuls construits d'avance** (graines : « Plan d'analyse », point 3) :
   - **nul isotrope** : M = 2 000 directions u_j ~ N(0, I) dans ℝ⁴⁰⁹⁶, ramenées à une moyenne quadratique de 1 ; tirées une fois par
     couche, partagées par toutes les directions et les deux lentilles de cette couche, **sous réserve de la garde du rapport à ε**
     (sinon refaites par direction, à la norme de v : plan, point 6) ;
   - **nul des signes** : M = 2 000 directions u_j = ε_j ⊙ v, ε_j de coordonnées ±1 indépendantes et équiprobables ; tirées par vecteur,
     partagées par ses deux signes et les deux lentilles. Même norme et mêmes valeurs absolues par coordonnée que v : il garde la forme,
     **anisotrope**, que le repliement de la normalisation donne à `w` (le nul isotrope ne la garde pas) ; direction brouillée.
   - Chaque direction nulle est lue par le même code et dans la même précision que v.
6. **Par direction (vecteur et signe), lentille et nul** :
   - z_t = (a_t(v) − m_t) / s_t, où m_t et s_t sont la moyenne et l'écart type de a_t sur les M directions nulles (moyenne sur des
     directions, jamais sur les jetons d'une action : aucune action n'est notée ici) ;
   - **les vingt premiers jetons** par score (k = 20) : identifiant, chaîne décodée (tokeniseur ci-dessus, échappée), score, z sous
     chaque nul, rang empirique du score parmi les M scores nuls du même jeton ; et les vingt premiers par z (nul isotrope) ;
   - **concentration** C(v) = max_t z_t ; p = (1 + #{j : C(u_j) ≥ C(v)}) / (M + 1), C(u_j) calculé avec les mêmes m_t et s_t (u_j
     compris : écart déclaré, négligeable à M = 2 000) ;
   - **part au-dessus du nul** P(v) : part des vingt premiers jetons dont le score dépasse le quantile 0,99 des M scores nuls du même
     jeton ; p de même forme ;
   - **familles de jetons nommées d'avance** (règles fixées ici, sur la chaîne décodée passée par `strip()`) : « nombres » : la chaîne
     s'écrit `^[0-9]+$` ; « coût » : la chaîne, en minuscules, est l'une de cost, costs, costly, price, prices, pricing, budget,
     budgets, expense, expenses, expensive, fee, fees, usd, dollar, dollars, $, spend, spent, spending, cheap, cheaper ; **choix déclaré :
     mots anglais seulement, aucune famille en français** (langue appuyée sur le code : les champs de l'action sont `ACTION`, `TITLE`,
     `PROPOSAL`, `CONTROLS`, `COST`, `PREDICTION`, `src/controle_ia/t07bbis/plis_v1.py`, l. 320-327,
     `7ba39db50674f9dbc3c6a6920ea03a60826d0bc7b7fe4bf66a262ad1acb45ab4`) ; compte de chaque famille dans les vingt premiers jetons, et p de même forme ;
   - **jeton de début** (128 000) : sa présence parmi les vingt premiers et son rang, rapportés pour chaque lecture (constat de G ; sans
     libellé).
7. **Pôles alignés** (pour v au signe + ; le signe − rend les mêmes pôles, de signe opposé) : cosinus de v avec les 28 672 directions
   d'écriture des pôles du bloc ℓ (± colonnes de `mlp.down_proj`, coordonnées brutes) ; les **dix pôles** de plus grand cosinus :
   neurone, signe, cosinus, rang parmi les maxima nuls ; pour chacun, sa lecture par la lentille publique à la couche ℓ (dix premiers
   jetons, même fonction) ; concentration des pôles = cosinus maximal, et son p sous chaque nul.
8. **Comparaisons appariées, descriptives** : cosinus et nombre de jetons communs aux vingt premiers, entre la sonde apprise et le
   lecteur honnête de même cellule et même pli, entre les deux plis d'une cellule, entre les doses d'un même pli (cosinus seulement à
   même couche ; sinon « couches différentes : sans objet ») ; accord de la lentille publique avec la lentille des logits (jetons
   communs aux vingt premiers) ; **témoin de couche** (lentille publique seulement : la lentille des logits lit la même chose à toute
   couche) : jetons communs entre la lecture de v à sa couche et à chacune des deux autres couches de T.
9. **Dépendance des p** : les p de directions d'une même couche partagent le nul isotrope ; ils ne sont pas indépendants, et ce texte
   n'affirme aucune indépendance.

## Seuil

- **Aucun seuil de décision, aucun taux d'erreur visé, aucun critère de succès** : le texte est descriptif. Les seules valeurs fixées
  d'avance sont des **règles de libellé** (« Critères de lecture gelés »), des **déclencheurs d'audit** (R4) et des **gardes** (« Liste
  d'arrêt »).
- **Niveaux des libellés** : « concentrée au-delà des deux nuls » si p ≤ 0,001 sous le nul isotrope **et** p ≤ 0,01 sous le nul des
  signes ; « non distincte du nul » si p > 0,05 sous l'un des deux ; « intermédiaire » sinon. Même règle pour la part au-dessus du nul
  et pour la concentration des pôles ; une famille est « sur-représentée » si p ≤ 0,01 sous les deux nuls.
- **Attendu par le seul hasard**, écrit à côté de chaque compte de libellés, par type : « concentrée », part au-dessus du nul
  « concentrée », pôles « concentrés » : au plus (nombre de lectures du type) × 0,001 (borne : le critère joint n'est pas plus
  probable que sa seule partie isotrope) ; « sur-représentée » : au plus (nombre de lectures × 2 familles) × 0,01.

## Plan d'analyse

1. **Ordre et antériorités** (registre propre ; « Lignes de registre ») : (a) `SCELLEMENT-LENTILLES-BBIS`, après vérification des
   corrections et nœuds tranchés, **inscrite alors que `VERDICT-BBIS` est absente** du registre propre de l'apprentissage des sondes sur
   la tâche ; la mère le relève, par les clés seulement (ligne `ABSENCE-VERDICT-LENTILLES-BBIS`) ; présente : texte exposé, nœud ; (b)
   `GO-LENTILLES-BBIS` (extrait de GO-2026-11-18-42, R-3349 : lentille publique seule, au processeur, 0 USD) ; (c) `CODE-LENTILLES-BBIS`
   (commit, empreintes, essais R5), avant toute exécution ; (d) **montage** (point 4), permis avant `VERDICT-BBIS` (il ne touche aucune
   sonde) : ligne `MONTAGE-LENTILLES-BBIS` (empreintes, jetons gardés, gardes) ; (e) **E-1 et E-2 ouverts par programme seulement après
   `VERDICT-BBIS`** : ligne `ENTREES-LENTILLES-BBIS` (chemins, empreintes de E-1 et E-2, empreinte de l'extrait des champs de la liste
   blanche) ; (f) calcul (point 6), tables fermées, poussées, scellées : `TABLES-LENTILLES-BBIS` ; (g) lecture humaine (point 8) :
   `OUVERTURE-LENTILLES-BBIS`, puis `LECTURE-LENTILLES-BBIS`.
2. **Taille** : fixée par T, non choisie ici : vingt sondes (dix sondes apprises, dix lecteurs honnêtes), au plus quarante vecteurs ;
   89 498 jetons gardés ; 28 672 pôles par couche ; M = 2 000 directions par nul (résolution des p : 1/2 001, sous le plus petit niveau
   de libellé, 0,001) ; deux lentilles.
3. **Graines (R9)** : entropie E = `207246359357165180107189867815730235805` (128 bits, `secrets.randbits(128)`, tirée le 2026-11-18 à
   16:49:33 UTC, avant toute lecture ; inchangée depuis le brouillon 1) ; graine de la clé k : `numpy.random.SeedSequence(entropy=E,
   spawn_key=(int.from_bytes(hashlib.sha256(k.encode()).digest()[:8], "big"),))`, générateur
   `numpy.random.Generator(numpy.random.PCG64(·))`, tirages en double précision, ramenés en simple précision pour la lecture ; clés :
   `lentilles-bbis/nul-isotrope/<couche>`, `lentilles-bbis/nul-isotrope-par-direction/<cellule>/<pli>/<rôle>/<vecteur>` (seulement si
   la garde du rapport à ε l'exige), `lentilles-bbis/nul-signes/<cellule>/<pli>/<rôle>/<vecteur>`,
   `lentilles-bbis/temoins-calibration/<couche>/<nul>/<cellule>/<pli>/<rôle>/<vecteur>` (pour le nul isotrope partagé,
   `<cellule>/<pli>/<rôle>/<vecteur>` est remplacé par `couche`),
   `lentilles-bbis/temoins-calibration/<couche>/nul-isotrope-par-direction/<cellule>/<pli>/<rôle>/<vecteur>` (seulement si la garde du
   rapport à ε l'exige),
   `lentilles-bbis/colonnes-garde/<couche>`, `lentilles-bbis/essai/<garde>` ; un manifeste par course (configuration et empreinte,
   versions, graines, commit).
4. **Montage, au processeur, dans le conteneur d'une session neuve, qui ne porte aucun dossier de course** (N9 tranché, option (a),
   « Nœuds ») :
   - **espace** : au moins 6 Go libres au départ ; pointe visée ≤ 4 Go ; dossier de travail neuf, propre à cette chaîne, qui porte
     aussi le cache des téléchargements (`HF_HOME` pointé dans ce dossier) ;
   - **clé** : la clé d'accès au modèle est lue **par son nom** (`HF_TOKEN`, présente dans l'environnement de la session), jamais
     imprimée, jamais écrite dans un fichier, un journal ou un manifeste ; sa présence et son caractère non vide sont testés sans
     l'imprimer ; **aucun mode de débogage** des bibliothèques de téléchargement (`HF_DEBUG`, `HF_HUB_VERBOSITY=debug`, journalisation
     « debug » de `urllib3`, `httpx` ou `requests`, `curl -v` ou `--trace`), qui imprimerait des en-têtes ; aucune machine louée,
     aucune clé passée à une machine (N8 tranché, option (a), « Nœuds ») ; la session neuve reçoit la clé de la configuration de son
     environnement, jamais de la session mère ni d'une autre session (ni message, ni fichier, ni argument) ; clé absente : arrêt, nœud ;
   - **réseau, avant tout flux long** : lecture d'un octet par hôte et par sorte de fichier : un octet de la lentille publique, un octet
     d'un fichier de poids à porte avec la clé, un octet d'un fichier de chaque jeu de données du corpus des jetons gardés, l'en-tête du
     dépôt du voisin ; refus de l'un, ou clé absente ou vide : arrêt avant tout téléchargement long ;
   - **environnement** : versions du conteneur relevées au manifeste (torch 2.14.1, numpy 2.4.6 au relevé de l'auteur) ; paquets
     manquants installés à des versions épinglées et relevées (de préférence celles de l'addendum v3, § 5 : transformers 5.18.0,
     tokenizers 0.23.2, huggingface_hub 1.33.0, datasets 5.2.0, safetensors 0.8.0) ; Drowse n'est pas employé (aucune lentille `R:`) ;
   - **code voisin** : clone au commit `849bfe1678e28becceb1e3864afe5fc8297d02e4`, `git rev-parse HEAD` relevé ; correctifs (2), (4) et
     (6) appliqués sans commit, empreintes des fichiers corrigés relevées ; `readout.py` du commit comparé à la copie versée
     (`2c0fe9951f98523c8652383b62b3da30b5777e8c1eccc4b3891c1af6ee816184`) dans `rms_norm_columns`, `transport` et `read` : **risque
     connu** (la copie vient de la branche `main` du voisin, relevée après le commit ; l'égalité n'est pas acquise) ; un écart : arrêt
     avant tout calcul, nœud ;
   - **poids** : chaque fichier de poids qui porte un tenseur gardé (index) est lu **en flux** : SHA-256 calculé sur le flux entier et
     comparé (table ci-dessus), seuls les octets des tenseurs gardés écrits sur disque (en-tête `safetensors` : longueur sur 8 octets
     puis description JSON des positions) ; le fichier entier n'est jamais écrit ; tokeniseur, index, `LICENSE` et `USE_POLICY.md`
     téléchargés entiers, vérifiés ;
   - **lentille publique** : téléchargée à la révision passée explicitement ; taille et SHA-256 vérifiés ; `LICENSE`, `NOTICE`,
     `USE_POLICY.md` du dossier vérifiés par identifiant git et taille ; contrôles de disposition repris de `neuronpedia_lens` du
     correctif (2) (`{"J": {0..30}}`, matrices carrées de même forme) ; **clé `provenance` lue : point de capture « block_output »
     exigé, lisible** (lisible = une clé `capture_point` dans `provenance`, de valeur `block_output` ; `source_layers` = 0 à 30 et
     `d_model` = 4 096 comparés ; si `provenance` porte un `target_layer`, sa valeur est 31 (dernier bloc ; la configuration versée dit
     `target_layer: 31`), toute autre valeur : arrêt ; les clés `source_layers`, `d_model`, `n_prompts` sont attendues et ne sont pas une
     « disposition autre ») ; **les 31 matrices** : chacune distincte de l'identité et toutes distinctes deux à deux (écart maximal
     > 10⁻⁶ pour chacune des 465 paires ; un fichier mal assemblé ferait des doublons) ; écart relatif de chaque matrice à l'identité
     rapporté par couche, sans critère ; seules les matrices des couches 7, 15 et 23 sont gardées ensuite ;
   - **jetons gardés** : `05_act_corpus.py` puis `03_token_counts.py` (une seule fois) ; liste `catalog.kept` : nombre et empreinte
     relevés et comparés aux valeurs attendues ; présence du jeton de début rapportée ;
   - gardes du montage (« Liste d'arrêt ») ; ligne `MONTAGE-LENTILLES-BBIS`.
5. **Garde de la fonction de lecture** (R5) : à chaque couche lue et pour chaque lentille, 64 colonnes de `W_down` tirées par graine ;
   les dix premiers jetons rendus par notre code égalent, au rang près, ceux de `read` du voisin appelé avec W_U en simple précision,
   pour les 64 colonnes (cas sain ; « au rang près » : mêmes dix identifiants ; un écart limité à des jetons dont les scores diffèrent
   de moins de 10⁻⁴ en valeur relative est compté et rapporté, sans arrêt) ; artefact, défini par lentille : pour la lentille publique,
   la matrice de la couche suivante dans l'ordre 7 → 15 → 23 → 7 mise à la place de J_ℓ ; pour la lentille des logits, dont la matrice
   est l'identité à toute couche, une matrice de permutation des 4 096 coordonnées, tirée par la graine
   `lentilles-bbis/essai/garde-lecture-logits-c<couche>` (forme `lentilles-bbis/essai/<garde>` du point 3), mise à la place de
   l'identité ; dans les deux cas, les dix premiers jetons diffèrent de ceux du cas sain pour **au moins 32 des 64 colonnes**. Rapporté sans critère : le nombre de colonnes dont le premier jeton diffère
   quand le voisin fait le produit en demi-précision, comme la comparaison des lentilles.
6. **Calcul** :
   - **contrôle de l'indice de couche** : pour chaque sonde, la matrice lue est celle de l'indice égal à sa `couche` (E-2), et
     l'indice est écrit dans les tables à côté de l'empreinte de la matrice ; au montage, l'empreinte de chacune des matrices 7, 15,
     23 est relevée par indice ; au calcul, l'empreinte de la matrice lue est comparée à celle relevée pour l'indice égal à la couche de
     la sonde ; écart : arrêt ;
   - **garde du rapport à ε** : ρ calculé pour chaque direction réelle (à sa norme lue), chaque lentille, et pour ses directions nulles
     et témoins ; minimum rapporté par (couche, lentille) ; si le minimum est ≥ 100 : indépendance à la norme tenue, rapportée ; s'il
     est < 100 pour une (couche, lentille) : l'indépendance est écrite « non tenue » pour cette couche, et, **pour les deux lentilles de
     cette couche** (l'appariement du point 9 est gardé), le nul isotrope est refait par vecteur : M = 2 000 directions tirées par la clé
     `lentilles-bbis/nul-isotrope-par-direction/<cellule>/<pli>/<rôle>/<vecteur>`, ramenées à la norme de v ; ses témoins : **200 par
     vecteur**, clé `lentilles-bbis/temoins-calibration/<couche>/nul-isotrope-par-direction/<cellule>/<pli>/<rôle>/<vecteur>`, ramenés à
     la même norme, chacun comparé aux M directions de son vecteur ; comptes mis en commun par (couche, lentille), n = 200 × le nombre de
     vecteurs de la couche ; les lectures faites avec le nul partagé de cette couche restent en table, marquées « remplacées », et ne
     portent aucun libellé ; coût rapporté (au plus ≈ 176 000 lectures de plus, ≈ 7 min de produits au débit du banc), dans la durée
     maximale ;
   - lectures, nuls, statistiques, pôles, comparaisons (« Métrique ») ;
   - **calibration** : des directions témoins tirées de chaque nul (graines propres) passent par le chemin des directions réelles, et
     leurs p de concentration sont calculés contre les M directions nulles : nul isotrope, **1 000** témoins par couche ; nul des signes,
     200 témoins par vecteur ; comptes **mis en commun par (couche, lentille, nul)** (n = 1 000 pour le nul isotrope ; n = 200 × le
     nombre de vecteurs de la couche pour le nul des signes) ; sous le nul, la part attendue de p ≤ 0,05 vaut 100/2 001 ; la calibration
     échoue si le compte de p ≤ 0,05 sort de [q_bas, q_haut], q_bas est le plus grand entier tel que P(X < q_bas) ≤ 10⁻⁴, q_haut le plus
     petit tel que P(X > q_haut) ≤ 10⁻⁴, sous la loi exacte du compte quand les témoins d'un jeu partagent ses M directions nulles : pour
     un jeu de n témoins, la loi bêta-binomiale (n ; 100 ; M − 99 = 1 901) ; pour plusieurs jeux mis en commun (un jeu de 200 par
     vecteur), la somme de lois bêta-binomiales indépendantes ; bornes calculées par le code et écrites (par exemple [23, 85] pour un
     jeu de 1 000 ; [1, 24] pour un jeu de 200 ; [12, 53] pour trois jeux de 200 ; [26, 79] pour cinq jeux de 200) ; pour n < 600, la borne basse est **volontairement lâche**, déclarée telle dans les tables ;
   - déclencheurs d'audit évalués et audits joués dans la même session ; tout est écrit dans des fichiers fermés ;
   - ordre de grandeur : ≈ 195 000 lectures (≈ 97 000 directions réelles, nulles et témoins, par lentille), ≈ 143 TFLOP, soit ≈ 7 min de
     produits au débit du banc (≈ 14 min si la garde du rapport à ε impose les nuls par direction).
7. **Comparaisons multiples** : aucune correction (descriptif) ; chaque compte de libellés porte son attendu par hasard ; nombre total
   de lectures écrit.
8. **Lecture** : par le lecteur neuf, sur processeur, après `VERDICT-BBIS` scellée ; il applique les « Critères de lecture gelés » aux
   tables, écrit la description, la scelle (`LECTURE-LENTILLES-BBIS`) ; un désaccord entre ses phrases et celles que le code rend
   mécaniquement est tranché par un second lecteur neuf, sans nouveau calcul.
9. **Contrôles appariés** : mêmes directions nulles pour les deux lentilles d'une couche ; même nul des signes pour v et −v ; sonde
   apprise et lecteur honnête comparés à même cellule, même pli, même couche.
10. **Nettoyage** (licence ; espace) : à la fin, tenseurs extraits, fichier de la lentille, corpus et dossier de travail supprimés,
    par chemin, dans le seul dossier de cette chaîne ; rien d'autre n'est supprimé.

## Critères de lecture gelés

**Phrase de tête, toujours écrite** : « Lecture descriptive, par la lentille publique côté sortie (lentille R de Llama 3.1 8B Instruct
publiée par Neuronpedia, ajustée par un tiers sur 64 textes de WikiText), des directions des sondes apprises sur la tâche et des
lecteurs honnêtes de même recette, à la couche où chaque sonde lit. Ce n'est pas notre lentille ajustée. **Les directions des sondes
sont des vecteurs de lecture ; elles sont lues ici comme des directions écrites dans le flux** : la lecture dit ce que la lentille
associe à un tel vecteur écrit, non ce que la sonde lit. Elle dit quels jetons et quels pôles la lentille associe à chaque direction ;
elle ne dit rien de la détection du sabotage, qui appartient au verdict de l'apprentissage des sondes sur la tâche, ni de ce qu'une
sonde fait sur un épisode. » Suivie de : « Verdict d'ensemble de la tranche des lentilles publiques sur cette lentille : [ligne recopiée
telle quelle de `docs/notes/neuron-lens-v1/lecture-b-alpha/verdict-b-alpha-v1.md` (branche principale, G, documents),
`ca06acb1550ccc76fef1ec89ae0aec170c5f05252bda2711f131eaa0e645fc1d`, par le lecteur ; empreinte différente : « ligne non recopiée :
empreinte »]. » Et, si la garde du rapport à ε a imposé des nuls par direction : « Indépendance à la norme non tenue à [couches,
lentilles] : nuls isotropes refaits par direction. »

| ce qui est observé (par direction, signe et lentille) | phrase gelée |
|---|---|
| concentrée au-delà des deux nuls | « Par [lentille], la direction de [sonde, en clair] (couche [ℓ], signe [±]) se distingue des deux nuls (concentration [C] ; p [p_iso] et [p_signes]) ; ses premiers jetons : [vingt jetons]. » |
| intermédiaire | « Par [lentille], la direction de [sonde] (couche [ℓ], signe [±]) ne se distingue des nuls qu'en partie (p [p_iso] et [p_signes]) : ses premiers jetons sont rapportés, sans être nommés comme ce qu'elle capte. » |
| non distincte du nul | « Par [lentille], la direction de [sonde] (couche [ℓ], signe [±]) ne se distingue pas du nul (p [p_iso] et [p_signes]) : ses jetons sont en table, et aucune phrase ne les nomme comme ce qu'elle capte. » |
| famille sur-représentée | « La famille [nombres / coût] paraît [n] fois dans ses vingt premiers jetons (attendu sous le nul [e] ; p [..] et [..]) : la lecture ajoute un soupçon que la sonde lise [des nombres / le coût] ; elle ne le prouve pas. » |
| famille non sur-représentée | « La famille [..] n'y est pas sur-représentée ([n] ; p [..] et [..]) : cela ne blanchit pas la sonde. » |
| pôles alignés concentrés | « Les pôles qui écrivent le plus près de la direction ([dix pôles], cosinus [..]) se distinguent des nuls (p [..] et [..]) ; la lentille publique les lit : [jetons par pôle]. » |
| pôles non distincts | « Aucun pôle de la couche n'écrit plus près de la direction que sous le nul (p [..] et [..]). » |
| comparaison appariée | « Cosinus [c] entre [sonde] et [autre] (même couche) ; [j] jetons communs sur vingt. » ; ou « couches différentes : sans objet ». |
| non calculable ou non lue | « Non lue : [motif]. » |

**Règles** : aucune phrase ne nomme les jetons d'une lecture « non distincte du nul » ou « intermédiaire » comme ce que la direction
capte ; aucune phrase ne dit qu'une sonde détecte ou ne détecte pas le sabotage, lit ou ne lit pas « l'état saboteur », ni ne rapproche
la lecture d'une aire ; le mot « soupçon » ne s'emploie que pour une famille sur-représentée ; les mots « nos lentilles » ou « notre
lentille » ne désignent jamais la lentille lue ; aucune phrase ne dit que la sonde « lit » les jetons de sa lecture (« associe » ou
« pousse » seulement), sauf la phrase gelée « famille sur-représentée », qui parle d'un soupçon (« la lecture ajoute un soupçon que la
sonde lise […] ») : c'est la seule permise ; toute description au-delà des phrases gelées est marquée « description libre, après lecture, non
préenregistrée ».

**Audit de symétrie (R4)**, déclencheurs gelés, évalués et joués dans la session du calcul : (i) **trop beau** : les dix sondes apprises
et les dix lecteurs honnêtes « concentrés » par la lentille publique ; ou, pour une direction des couches 7 ou 15, les mêmes vingt
premiers jetons par la lentille publique et par la lentille des logits ; ou deux directions distinctes (deux plis, deux doses) de
cosinus > 0,999 ; ou une sonde apprise et son lecteur honnête de cosinus > 0,99 ; (ii) **tout négatif** : aucune lecture d'aucune
direction « concentrée » ni « intermédiaire », par la lentille publique **et** par la lentille des logits. Contenu de l'audit :
empreintes des tableaux lus contre E-2 ; couche de la sonde, de la lentille et du harnais ; point de capture de la lentille ;
conventions de signe ; décodage ; rapport à ε ; deux directions relues par un chemin indépendant (produits en double précision, sans
la fonction du voisin). Issue écrite en réserve ; aucune table ne change.

## Liste d'arrêt

| condition | action |
|---|---|
| texte non scellé, `SCELLEMENT-LENTILLES-BBIS` absente, ou `VERDICT-BBIS` déjà présente à son inscription | rien ne part ; texte exposé : nœud (version neuve qui déclare l'exposition, ou abandon) |
| `GO-LENTILLES-BBIS` absente ; code non cité par `CODE-LENTILLES-BBIS` ; un essai (R5) manquant ou en échec | rien ne part |
| toute dépense, toute location de machine, toute carte graphique | hors de ce texte (0 USD) : rien ne part ; nœud |
| clé imprimée, écrite dans un fichier, un journal ou un manifeste, passée hors de la session, ou mode de débogage d'une bibliothèque de téléchargement activé | arrêt ; nœud (Lazar décide d'un changement de clé) |
| clé absente ou vide ; requête vers Hugging Face, un hôte de stockage, un jeu de données du corpus ou le dépôt du voisin refusée ; fichier à porte refusé avec la clé (essai d'un octet, plan, point 4) | arrêt avant tout téléchargement long ; nœud |
| moins de 6 Go libres au départ, ou moins de 1 Go pendant le calcul | arrêt, sans rien supprimer hors du dossier de cette chaîne ; compte rendu |
| durée cumulée de la session de calcul au-delà de 8 h | arrêt ; versement de ce qui existe ; compte rendu |
| SHA-256 ou taille d'un fichier de poids ou du tokeniseur différent de ce texte ; identifiant git d'un pointeur ou d'un petit fichier différent ; `LICENSE`, `NOTICE` ou `USE_POLICY.md` d'un autre identifiant git ou d'une autre taille | arrêt ; message à la mère |
| lentille publique : disposition autre que `{"J": {0..30}}` de matrices 4 096 × 4 096 ; **clé `provenance` absente ou sans point de capture lisible** ; point de capture autre que « block_output » ; une matrice égale à l'identité ; deux matrices égales (écart maximal ≤ 10⁻⁶) | arrêt avant tout calcul ; nœud |
| `readout.py` du commit `849bfe1678e28becceb1e3864afe5fc8297d02e4` différent de la copie versée dans `rms_norm_columns`, `transport` ou `read` (risque connu) | arrêt avant tout calcul ; nœud |
| liste des jetons gardés d'un autre nombre que 89 498 ou d'une autre empreinte que `c37186add16770aa3c04bd0c16c417544b7e2a15b374ee85e47fbda7ec148d68` | arrêt avant tout calcul ; nœud |
| `SCORES-BBIS` absente, ou en plusieurs lignes | rien ne part ; plusieurs lignes : nœud (la mère désigne la course, par les noms seulement) |
| E-1 ou E-2 ouvert avant `VERDICT-BBIS` ; un fichier ou dossier de la liste « jamais ouverts » ouvert ; une entrée `direction0_*` ou `direction1_*` de E-1 décodée ; un contenu de la branche des données autre que E-1, E-2 et leurs compagnons téléchargé ; un champ de E-2 hors de la liste blanche gardé, imprimé ou écrit (la régularisation de `enc.reglage` comprise) ; une ligne de registre lue hors des clés nommées | lecture invalide ; nœud |
| empreinte de E-1 différente de son compagnon ou de `fichier_sondes.sha256` ; empreinte de E-2 différente de son compagnon ou de la ligne `SCORES-BBIS` | arrêt (R11) |
| nom d'entrée de E-1 ou de champ de E-2 différent de ceux de ce texte ; `enc.reglage` d'une autre forme ; empreinte d'une sonde recalculée différente de `empreinte_sonde` ou de `enc.empreinte` ; couche hors de {7, 15, 23} ; famille hors de {lineaire, attention} ; agrégation différente de celle de la famille ; cellule ou pli manquant | arrêt : forme mal comprise ; nœud |
| sonde apprise marquée `echec` ; lecteur honnête marqué `enc.echec` ; toute autre absence de champ ou d'entrée | sonde apprise marquée `echec` : elle et son lecteur honnête, non appris, sont « non lus », sans arrêt ; lecteur honnête marqué `enc.echec` : « non lu », sans arrêt ; toute autre absence de champ ou d'entrée : arrêt (ligne « forme mal comprise ») |
| matrice lue d'un autre indice que la couche de la sonde | arrêt |
| garde de la fonction de lecture (plan, point 5) : écart sur le cas sain, ou moins de 32 colonnes sur 64 différentes sur l'artefact de la lentille (publique : matrice d'une autre couche ; logits : permutation) | arrêt avant tout calcul |
| garde du rapport à ε (plan, point 6) : minimum < 100 pour une (couche, lentille) | sans arrêt : nuls isotropes refaits par direction, « non tenue » écrit (phrase de tête) |
| calibration (plan, point 6) : compte hors de [q_bas, q_haut] pour une (couche, lentille, nul) | tables de cette couche, de cette lentille et de ce nul « non calculables », motif écrit, sans arrêt du reste |
| valeur non finie dans une lecture ou un nul | arrêt |
| tables ouvertes par une personne avant `VERDICT-BBIS` scellée ; une table ou une phrase de ce texte transmise au lecteur du verdict de l'apprentissage des sondes sur la tâche, de l'étape B, de la table conjointe ou de P3-bis avant leurs verdicts scellés | lecture invalide ; nœud |
| clé de ce texte écrite dans `registres/scellements-v1.md` (la garde de T0.7 y refuse toute clé inconnue ; T, « Liste d'arrêt ») | arrêt de l'écriture ; ligne retirée par la mère, déclaré |
| lentille publique absente, illisible, ou d'une autre taille ou d'une autre empreinte que ce texte | arrêt ; message à la mère ; jamais remplacée par une autre lentille ; la lecture par la seule lentille des logits n'est pas rendue |
| toute envie d'écart à ce texte | écrite, datée, version neuve (R12), contre-lue, avant d'être faite |
| tout refus d'une permission, du crochet ou du classifieur | ni rejoué, ni reformulé, ni contourné ; arrêt ; nœud |

**R5** : chaque garde codée est essayée avant le calcul sur un cas sain et sur un artefact (« Code neuf ») ; résultats consignés. Les
lignes de procédure humaine (ouverture avant le verdict par une personne, transmission à un lecteur, refus d'une permission) ne sont
pas codables : elles sont tenues par les rôles.

## Qui, quelle machine, quel coût

- **Développeur neuf** : écrit le code (« Code neuf ») sans aucune vue des données (jouets et Llama miniature seulement) ; ni auteur
  de ce texte, ni opérateur, ni lecteur.
- **Opérateur neuf** : n'a lu aucune sortie ni aucun score de l'apprentissage des sondes sur la tâche, ni des autres chaînes
  interdites ; ni auteur, ni développeur, ni lecteur de ce texte, ni lecteur ou juge d'aucun verdict nommé ici ; lance le montage et le
  calcul, ne lit que les codes d'arrêt, les existences et les empreintes, et, des registres, les seules clés et heures nommées en E-3 ;
  n'ouvre aucune table.
- **Lecteur neuf** : n'a lu aucun résultat de l'apprentissage des sondes sur la tâche (score, aire, issue, verdict), ni des autres
  chaînes interdites ; ni auteur, développeur ou opérateur, ni lecteur d'aucun verdict nommé ici ; lit ce texte, les tables fermées et
  la ligne du verdict d'ensemble de la tranche des lentilles publiques ; décrit selon les « Critères de lecture gelés ».
- **Machine** : le processeur du conteneur d'une session neuve (N9 tranché, option (a)) ; au relevé de l'auteur, dans son propre
  conteneur : 4 fils, 15 Go de mémoire, ≈ 7 Go libres sur un disque partagé ; ces relevés et les versions sont refaits au montage
  dans la session neuve ; aucune carte graphique ; mémoire de pointe estimée ≤ 6 Go (W_U gardé en simple précision 1,47 Go ; scores nuls d'un
  vecteur, 2 000 × 89 498 en simple précision, 0,72 Go ; les 31 matrices de la lentille en demi-précision, 1,04 Go, le temps de leur
  contrôle).
- **Coût : 0 USD** (aucune location, aucune interface payante). **Durée** (estimation de l'auteur) : téléchargements ≈ 17,1 Go de poids
  et de lentille lus en flux (plus le corpus des jetons gardés), ≈ 5 à 30 min selon le débit, pire ≈ 2 h ; corpus et comptes de jetons
  ≈ 15 à 45 min, pire ≈ 2 h ; gardes et essais < 15 min ; calcul ≈ 20 à 45 min (dont ≈ 7 à 14 min de produits au débit du banc), pire
  ≈ 2 h ; **total ≈ 1 à 2 h, pire ≈ 6 h** ; arrêt à 8 h (« Liste d'arrêt »). Lecture humaine : 0 USD.

## Frontière : ce que ce texte ne dit pas

1. Rien sur la détection du sabotage : aucune phrase ; elle reste au verdict de l'apprentissage des sondes sur la tâche (T).
2. Rien sur les sondes génériques, le critère 3 de G0, G1, ni aucune hypothèse du programme ; aucun résultat n'entre dans un
   préenregistrement du programme sans nœud de Lazar.
3. **Convention de lecture** : une sonde lit `w·h` ; la lentille décrit l'effet d'un vecteur **écrit** dans le flux. Ce texte applique la
   lentille aux coordonnées brutes de `w` (et de `q`), normalisation repliée (les coordonnées de faible écart type y pèsent beaucoup,
   celles des dimensions à très forte activité presque rien), **comme si `w` était écrit dans le flux** : c'est une convention de
   description, non une mesure de ce que la sonde lit. La description par la direction transposée n'est pas faite. La description de ce que la sonde lit demanderait une lentille côté entrée,
   absente (point 7). Le nul isotrope ignore l'anisotropie du repliement ; seul le nul des signes la garde.
4. Une liste de jetons dit ce que la lentille associe à une direction (ce qu'elle « pousse en moyenne »), non ce que la sonde emploie
   sur un épisode, ni un rôle causal ; aux couches 7 et 15, sous les deux tiers de la profondeur, G attend que la lecture prédise mal ce
   qu'une activation fait en contexte (lecture contre ablation couche par couche).
5. Une lecture peut ajouter un soupçon sur une sonde, jamais la blanchir (règle de G).
6. **Notre lentille ajustée n'entre pas dans ce texte** (décision de Lazar, GO-2026-11-18-42) : la seule lentille ajustée lue est la
   lentille publique, ajustée par un tiers sur 64 textes de WikiText ; aucun résultat de ce texte ne dit rien de notre lentille, et
   aucun résultat de la tranche de l'ajustement de nos lentilles n'y est lu. Ce texte ne revendique aucune fidélité de la lentille
   publique : elle est l'objet des tranches de la lecture par lentille neuronale. **Une seule lentille ajustée est lue** : aucune
   robustesse d'une lentille ajustée à l'autre n'est mesurée, et la lentille des logits, prise en référence, n'en tient pas lieu.
7. Aucune lecture côté entrée (aucune lentille côté entrée publique).
8. L'indice de couche commun à la sonde et à la lentille est tenu par leurs conventions écrites, non par un essai (« Hypothèse »).
9. La comparaison au lecteur honnête décrit un recouvrement avec un lecteur du texte de même recette ; elle ne dit pas « au-delà du
   texte » (seules les épreuves de T en jugent).
10. Les réglages retenus (famille, couche) lus ici ne sont pas des scores ; ils montrent ce que la validation interne a choisi ; c'est,
    avec les directions, la seule information de l'apprentissage des sondes sur la tâche qui passe dans cette lecture (la régularisation
    n'est pas lue).
11. Rien sur les sondes de l'ordre 2, les sondes du nul de réétiquetage, les directions du plancher : non lues.
12. Rien d'un autre modèle, d'un autre mode de sabotage, ni d'une autre couche que 7, 15 et 23 ; rien des lentilles J et J++ publiques
    (non lues, N10 tranché, option (a), « Nœuds »).

## Données gardées et plan de stockage

- Calcul, branche `calcul/lentilles-sondes-bbis-v1`, morceaux de moins de 95 Mo, compagnons `.sha256` :
  `diag/<run-lentilles>/tables-lentilles-bbis.json` (toutes les tables, déclencheurs et audits, rapports à ε, calibrations et leurs
  bornes, indices de couche et empreintes des matrices lues ; **fermé**) ; `donnees/<run-lentilles>/lectures-lentilles-bbis-NNN.npz`
  (scores de tous les jetons gardés par vecteur et lentille ; résumés des nuls par jeton : moyenne, écart type, quantile 0,99 ;
  statistiques des directions nulles et des directions témoins ; **fermés**) ; `diag/<run-lentilles>/montage-lentilles-bbis.json`
  (empreintes, tailles et identifiants git des fichiers lus, `provenance` de la lentille, contrôles des 31 matrices, jetons gardés :
  nombre et empreinte, versions, commit du voisin, empreintes des fichiers corrigés, essais d'un octet, gardes ; aucune lecture de
  sonde ; jamais la clé) ; `runs/<run-lentilles>/manifeste.json` (R9).
- Non gardés (licence ; espace) : poids de Llama, lentille publique, tenseurs extraits, corpus d'activations ; supprimés en fin de
  calcul (plan, point 10). Aucune valeur de régularisation, aucun champ exclu de E-2, aucune entrée `direction*` de E-1 n'est gardé.
- Lecture : `diag/<run-lecture>/lecture-lentilles-bbis.json` (phrases rendues par le code) et la description du lecteur,
  `docs/notes/lecture-sondes-bbis-par-lentilles-v1/description-v1.md`, chacune scellée avec son compagnon.

## Lignes de registre

Registre **propre** (choix de forme de la mère, R-3334) : `registres/lecture-sondes-bbis-par-lentilles-v1.md`, format
`| clé | AAAA-MM-JJTHH:MM:SSZ | chemin | sha256 |`, lignes ajoutées, jamais réécrites. Clés : `SCELLEMENT-LENTILLES-BBIS` (version
scellée de ce texte), `ABSENCE-VERDICT-LENTILLES-BBIS`, `GO-LENTILLES-BBIS` (extrait de GO-2026-11-18-42), `CODE-LENTILLES-BBIS`,
`MONTAGE-LENTILLES-BBIS`, `ENTREES-LENTILLES-BBIS`, `TABLES-LENTILLES-BBIS`, `OUVERTURE-LENTILLES-BBIS`, `LECTURE-LENTILLES-BBIS`. Lues,
jamais écrites : `SCORES-BBIS`, `VERDICT-BBIS` et `CODE-BBIS` (registre propre de l'apprentissage des sondes sur la tâche ; clés,
heures et chemins seulement ; pour `CODE-BBIS`, le commit aussi). **Jamais** `registres/scellements-v1.md`.

## Code neuf (à écrire sans aucune vue des données, contre-lire, éprouver ; R5)

- `src/controle_ia/lentilles_sondes_bbis/` (noms neufs, R12) : `entrees_v1` (E-1 clé par clé, E-2 par liste blanche, analyse de
  `enc.reglage`, empreintes des fichiers et des sondes, refus de tout autre chemin, nom ou champ, refus avant `VERDICT-BBIS`) ;
  `montage_v1` (essais d'un octet, lecture en flux et vérification des poids, pointeurs, licences, lentille publique et sa provenance,
  contrôles des 31 matrices, jetons gardés, clé lue par son nom) ; `lecture_v1` (lecture par les deux lentilles, scores complets,
  indice de couche, rapport à ε, garde de la fonction de lecture) ; `nuls_v1` (deux nuls, nuls par direction si besoin, directions
  témoins, graines) ; `statistiques_v1` (z, concentration, part, familles, jeton de début, pôles, comparaisons) ; `audits_v1`
  (déclencheurs R4, calibration et ses bornes) ; `phrases_v1` (phrases gelées) ; un lanceur qui enchaîne le plan, points 4 à 6 et 10,
  sous une horloge de 8 h.
- **Essais** (cas sain et artefact pour chaque garde) :
  - **entrées** : liste blanche (lire un champ exclu, la valeur d'un `echec` ou le sous-dictionnaire `ordre2` : refus) ; analyse de
    `enc.reglage` (`attention-c15-l2_0.01` : famille et couche rendues, régularisation absente de toute sortie ; chaîne mal formée :
    arrêt « forme mal comprise ») ; E-1 clé par clé (lecture des seules entrées `sonde_*` et `enc_*` d'une archive jouet qui porte aussi
    des entrées `direction0_*` : ces dernières jamais décodées ; demande d'une entrée `direction*` : refus ; nom d'entrée inconnu :
    arrêt) ; ouverture avant `VERDICT-BBIS` (refus) ; empreinte d'une sonde (un poids altéré : arrêt ; nom du lecteur honnête mal
    reconstruit : arrêt) ; couche, famille ou agrégation hors de l'ensemble ; ouvrir un fichier de scores : refus ; un fichier jouet par forme (a), (b), (c)
    d'« Attendu » (cas sains) ; `enc` absent sans `echec`, entrée `enc_w` présente alors que `enc.echec` existe, `sonde_q` absente pour la
    famille `attention` (artefacts : arrêt) ; empreintes de E-1 et de E-2 contre leurs compagnons (un octet changé : arrêt) ; lignes de
    registre (`SCORES-BBIS` absente ou multiple ; `SCELLEMENT-`, `GO-` ou `CODE-LENTILLES-BBIS` absente : refus) ;
  - **montage** : clé absente ou vide (arrêt, sans impression) ; essai d'un octet refusé (hôte simulé : arrêt) ; lecture en flux (un
    octet changé dans un faux fichier `safetensors` : arrêt ; tenseurs extraits égaux à ceux d'un chargement entier) ; pointeur
    (identifiant git faux : arrêt) ; licence (fichier altéré d'un octet : arrêt) ; lentille (disposition fausse ; `provenance` absente ou
    sans point de capture ; point de capture faux ; matrice identité ; deux matrices égales par permutation d'un fichier jouet : arrêt) ;
    jetons gardés (liste altérée d'un jeton : arrêt) ; mode de débogage activé : arrêt ; comparaison de `readout.py` à la copie
    versée (copie jouet altérée dans `read` : arrêt) ; lentille absente (arrêt, message, aucune lecture rendue par la seule lentille des
    logits) ;
  - **lecture** : fonction de lecture (64 colonnes ; sur la fausse lentille, les deux artefacts : matrice de la couche suivante pour
    la lentille publique, permutation des coordonnées pour la lentille des logits : au moins 32 différentes chacun) ; **indice de couche** (fausse
    lentille dont la matrice ℓ porte une signature propre, J_ℓ = I + ℓ·10⁻²·E, E fixe : la lecture d'une sonde de couche ℓ rend la
    signature ℓ ; un décalage d'un cran introduit dans le code : arrêt) ; **rapport à ε** (avec J = I : v de norme 10⁻⁴, artefact,
    lève la garde et impose les nuls par direction ; v de moyenne quadratique 1, cas sain, ne la lève pas ; au bord, ρ = 99 lève, ρ = 101 ne lève pas) ; imparité (a_t(−v) = −a_t(v)) ;
  - **nuls et statistiques** : graines reproductibles ; même norme ; nul des signes de mêmes valeurs absolues ; calibration (nul sain :
    dans les bornes ; scores des témoins multipliés par 1,5 : hors des bornes ; bornes
    recalculées égales aux exemples du plan) ; familles (vocabulaire jouet) ; jeton de début (rang rapporté) ; symétrie des
    pôles (v et −v) ; valeurs non finies ;
  - **procédure** : horloge simulée au-delà de 8 h : arrêt ; espace disque (seuil simulé : arrêt) ; clé (aucune occurrence de sa valeur
    dans les fichiers écrits, essai sur une fausse clé) ; clé de ce texte dans `registres/scellements-v1.md` (refus) ; une phrase par
    libellé ; bout en bout sur un Llama miniature et une fausse lentille.

## Nœuds

**Tranchés** :
- **N1** (où la lentille rencontre les directions) : **option (d), lentille publique seule, au processeur, 0 USD** (Lazar,
  GO-2026-11-18-42, R-3349).
- **N5** (passerelle avec une tranche hors programme) : couvert par le même mot de Lazar.
- **N3** (code cité après le scellement), **N4** (poids ouverts après `VERDICT-BBIS`), **N6** (registre propre) : choix de forme de la
  mère (R-3334), repris tels quels.
- **N2** (lentilles à ré-ajuster) et **N7** (dépense de la machine louée) : **sans objet**.

**Tranchés par anticipation, option (a) chacun** — recommandation du rédacteur, jugée tenable par la contre-lecture 1, appliquée par
anticipation par la session mère (autonomie GO-2026-11-18-26), portée à Lazar (R-3372) :
- **N8 — clé d'accès au modèle** : option (a) : la clé est lue par son nom (`HF_TOKEN`) dans le conteneur de la session du calcul,
  couverte par GO-2026-11-18-42, relevée par la mère dans `GO-LENTILLES-BBIS` ; la session neuve reçoit la clé de la configuration de
  son environnement, jamais de la session mère ni d'une autre session (ni message, ni fichier, ni argument) ; clé absente : arrêt, nœud.
  Garde-fous : essai d'un octet avant tout flux, clé absente ou vide testée sans impression, modes de débogage interdits (plan, point 4).
- **N9 — session du calcul** : option (a) : session neuve dont le conteneur ne porte aucun dossier de course ; l'opérateur ne lit des
  registres que les clés et heures nommées en E-3 ; les relevés de machine de l'auteur sont refaits au montage.
- **N10 — lentilles J et J++ publiques** : option (a) : non lues ; conséquence écrite (« Frontière », point 6) : aucune robustesse d'une
  lentille ajustée à l'autre n'est mesurée.

## Contre-lecture

- **Contre-lecture 1** : sous-agent neuf, modèle Sonnet 5.5 (autre modèle que l'auteur, Opus 5.5), session mère
  `session_013QMayjsoZJFBUCqcnvD5h1`, 2026-11-18 ; n'a écrit aucune pièce du texte, de l'apprentissage des sondes sur la tâche ni des
  tranches de la lecture par lentille neuronale ; ne sera ni développeur, ni opérateur, ni lecteur du texte. Brouillon relu : brouillon 2,
  `prereg/lecture-sondes-bbis-par-lentilles-v1-brouillon2.md`,
  `271c421f089f39564527981fc98fb9f4bc3143e67e6491f6a48234c224cef1cc`. Rapport :
  `prereg/contre-lectures/lecture-sondes-bbis-par-lentilles-v1-brouillon2-cl1.md`,
  `f876f83a250dce85d83ab6e73f8ec0d40ffbc33640d625962838f774e3b94ea2`. Verdict : « scellable après corrections » ; aucune échappatoire ;
  un bloquant, quatre majeurs, onze mineurs, traités ci-dessous.
- **Contre-lecture 2 (vérification des corrections)** : sous-agent neuf, modèle Fable 5.2 (`claude-fable-5-2`) ; n'a écrit ni ce texte,
  ni sa contre-lecture, ni aucune pièce de l'apprentissage des sondes sur la tâche ou des tranches de la lecture par lentille
  neuronale ; ne sera ni développeur, ni opérateur, ni lecteur du texte. Mandat :
  `docs/notes/neuron-lens-v1/mandat-verification-corrections-texte-lentille-publique-v1.md`,
  `71dbd76ab3d277d10e4e4fa8ec6c8dc42bc8b8ecab1160b442b024d5a266fc34`. Brouillon relu : brouillon 3,
  `prereg/lecture-sondes-bbis-par-lentilles-v1-brouillon3.md`, `49b0921d585944fd1e326bdea6155ad67e64719d6ab2673a022f415f084f256a`.
  Rapport : `prereg/contre-lectures/lecture-sondes-bbis-par-lentilles-v1-brouillon3-verif1.md`,
  `5398f2e90f2dac1b5243601f89d609fb3c2a24773126b3391cfdab8953d5aedc` (compagnon vérifié). Verdict : « scellable après corrections » ;
  un bloquant, trois majeurs, treize mineurs, traités dans « Traitement des remarques de la vérification 1 ». Pour des couples
  appliqués tels quels, le rapport demande un contrôle de la seule différence brouillon 3 → version : liste et sortie de `diff` dans
  `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v1.md`.

### Traitement des remarques de la contre-lecture 1 (tient lieu de « Changements du brouillon 2 au brouillon 3 »)

| remarque | traitement | où |
|---|---|---|
| **B1** liste blanche inapplicable au lecteur honnête | **fait** : noms exacts relevés dans le code ; pour le lecteur honnête, `enc.reglage` analysé par une expression qui ne garde que famille et couche (régularisation jamais gardée, écrite ni imprimée), `enc.empreinte`, présence de `enc.echec` ; agrégation déduite de la famille ; nom reconstruit pour l'empreinte ; sous-dictionnaire `ordre2` exclu ; essais ajoutés | Entrées (E-2) ; Liste d'arrêt ; Code neuf |
| **M1** directions du plancher dans E-1 | **fait** : seules les entrées `sonde_{w,b,q}` et `enc_{w,b,q}` sont décodées, clé par clé ; `direction0_*`, `direction1_*` jamais décodées et ajoutées aux « jamais ouverts » ; champs d'empreinte nommés (`empreinte_sonde`, `enc.empreinte`) et convention de recalcul écrite ; essais ajoutés | Entrées (E-1) ; Liste d'arrêt ; Code neuf |
| **M2** vecteur de lecture lu comme direction écrite | **fait** : convention déclarée dans « Frontière » (point 3), dans la phrase de tête gelée, dans l'objet, le vocabulaire et la métrique ; anisotropie du repliement et rôle du nul des signes écrits ; règle de phrase ajoutée (« associe » ou « pousse », jamais « lit ») | Frontière ; Critères ; Hypothèse ; Métrique |
| **M3** indépendance à la norme sans garde | **fait** : rapport à ε défini, garde au seuil 100 par (couche, lentille), repli écrit (nuls isotropes refaits par direction, clés de graines, coût) sans arrêt ; « sans effet sur la lecture » retiré ; essai cas sain et artefact | Métrique (3, 5) ; Plan (3, 6) ; Liste d'arrêt ; Code neuf |
| **M4** indice de couche, `provenance`, matrices | **fait** : arrêt si `provenance` absente ou sans point de capture lisible ; 31 matrices distinctes de l'identité et deux à deux ; contrôle de l'indice dans le code, essai à signature ; décalage de convention déclaré non testable (sans passe avant) | Hypothèse ; Plan (4, 6) ; Liste d'arrêt ; Frontière (8) ; Code neuf |
| m1 statut plus lâche | **fait** : aligné sur la règle stricte | Statut |
| m2 attendu par hasard | **fait** : attendu par type de libellé | Seuil |
| m3 licence sans empreinte | **fait** : `LICENSE`, `NOTICE`, `USE_POLICY.md` par identifiant git et taille, comparés | Entrées ; Plan (4) ; Liste d'arrêt |
| m4 empreintes tronquées | **fait** : empreintes entières pour toute valeur comparée (correctif (6), identifiants des petits fichiers, jetons gardés, copie de `readout.py`, commit du voisin) ; restent tronquées les seules mentions qui ne servent à aucune comparaison (`16780aaa…` dans « Ce que l'auteur savait », entier dans la table de la lentille) | Documents ; Entrées ; Liste d'arrêt |
| m5 révision non passée par le correctif (2) | **fait** : révision passée explicitement par notre code | Entrées ; Plan (4) |
| m6 copie de `readout.py` | **fait** : écrit comme risque connu | Plan (4) ; Liste d'arrêt |
| m7 réseau et clé factice | **fait** : essai d'un octet par hôte et par sorte de fichier avant tout flux ; arrêt sur refus ou clé absente ou vide ; essais | Plan (4) ; Liste d'arrêt ; Code neuf |
| m8 durée maximale et jeton de début non essayés | **fait** : essai à horloge simulée ; présence et rang du jeton de début rapportés, essai | Métrique (6) ; Plan (4) ; Code neuf |
| m9 artefact de la garde de lecture | **fait** : au moins 32 colonnes sur 64 | Plan (5) ; Liste d'arrêt |
| m10 borne basse de calibration | **fait** : comptes mis en commun par (couche, lentille, nul), 1 000 témoins par couche pour le nul isotrope, bornes binomiales à 10⁻⁴ par côté, calculées par une règle ; borne basse déclarée lâche sous n = 600 | Plan (6) ; Liste d'arrêt ; Code neuf |
| m11 familles en anglais | **fait** : écrit comme choix (aucune famille en français) ; la langue des textes de la tâche est reprise de la contre-lecture, non vérifiée par l'auteur | Métrique (6) |
| réserve « p non indépendants » | **fait** : écrit | Métrique (9) |
| N8 (jeton absent ou factice ; débogage) | **fait** : garde-fous ajoutés ; tranché ensuite, option (a) (« Nœuds ») | Plan (4) ; Liste d'arrêt ; Nœuds |
| N9 (registres lus par l'opérateur) | **fait** : clés et heures nommées seulement ; tranché ensuite, option (a) (« Nœuds ») | Entrées (E-3) ; Qui ; Nœuds |
| N10 (conséquence d'une seule lentille ajustée) | **fait** : écrit dans la frontière ; tranché ensuite, option (a) (« Nœuds ») | Frontière (6) ; Nœuds |

**Remarque non faite** : aucune. Effets de bord déclarés : nombre de lectures porté à ≈ 195 000 (témoins du nul isotrope) ; durée de
calcul au pire ≈ 13 min de produits si la garde du rapport à ε impose les nuls par direction, dans la marge de 8 h.

### Traitement des remarques de la vérification 1

| remarque | traitement | où |
|---|---|---|
| **V-B1** artefact de la garde de lecture sans effet pour la lentille des logits | **appliqué tel quel** : artefact défini par lentille (couche suivante 7 → 15 → 23 → 7 pour la lentille publique ; permutation des coordonnées tirée par graine pour la lentille des logits) ; ligne d'arrêt et essais complétés | Plan (5) ; Liste d'arrêt ; Code neuf |
| **V-M1** formes en cas d'échec non écrites | **appliqué tel quel** : formes (a), (b), (c), seules admises ; ligne d'arrêt remplacée, mise en forme dans les deux colonnes de la table (conditions à gauche, mots du couple à droite) ; essais ajoutés | Entrées (« Attendu ») ; Liste d'arrêt ; Code neuf |
| **V-M2** repli de la garde du rapport à ε incomplet | **appliqué tel quel** (correction principale : repli pour les deux lentilles de la couche, appariement du point 9 gardé) ; clé des témoins ajoutée au point 3 | Plan (3, 6) |
| **V-M3** loi du compte de calibration | **appliqué tel quel** (correction principale : loi bêta-binomiale exacte) ; les quatre exemples, recalculés par le rédacteur sous la loi exacte, sont égaux (script `bornes_calibration_beta_binomiale_v1.py` et sa sortie, scellés, dans `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/`) ; « binomiales » retiré des essais | Plan (6) ; Code neuf |
| V-m1 empreinte de E-1 sans ligne de registre | appliqué tel quel | Liste d'arrêt |
| V-m2 clé `CODE-BBIS` | appliqué tel quel (première option : clé ajoutée aux clés lues) | Entrées (E-3) ; Lignes de registre |
| V-m3 valeurs exactes | appliqué tel quel : `max` ; `dispersion_ordres_calcul` ; `doses`, `couches`, `plis`, `manifeste`, `duree_s` nommées parmi les exclues | Entrées (E-2) |
| V-m4 « lisible » | appliqué tel quel | Plan (4) |
| V-m5 témoin de l'indice de couche | appliqué tel quel | Plan (6) |
| V-m6 deux lignes contradictoires | appliqué : une seule ligne porte la lentille d'une autre empreinte, avec l'action du couple ; pour qu'il n'en reste qu'une, la lentille est retirée de la ligne « SHA-256 ou taille… » et sa taille passe dans la ligne de la lentille | Liste d'arrêt |
| V-m7 deux phrases ; exception à la règle | appliqué tel quel | Frontière (3) ; Critères (règles) |
| V-m8 clé des témoins | appliqué tel quel ; la parenthèse du nul isotrope partagé (un seul jeu par couche) est accordée à la forme neuve de la clé : `<cellule>/<pli>/<rôle>/<vecteur>` y est remplacé par `couche` | Plan (3) |
| V-m9 « au rang près » | appliqué tel quel, au cas sain | Plan (5) |
| V-m10 essais manquants ; artefact de calibration | appliqué : essais nommés de la comparaison de `readout.py`, des lignes de registre, des empreintes de E-1 et E-2, de la lentille absente, du bord de la garde du rapport à ε ; artefact de calibration : « scores des témoins multipliés par 1,5 », retenu parmi les deux que propose le couple, parce que la matrice d'une autre couche ne change rien pour la lentille des logits (même défaut que V-B1) | Code neuf |
| V-m11 exposition de qui écrit les dernières corrections | appliqué : déclaration de la session mère et du rédacteur | Ce que l'auteur savait ; Statut |
| V-m12 clé d'une session neuve ; relevés de machine | appliqué tel quel | Plan (4) ; Qui ; Nœuds (N8, N9) |
| V-m13 langue appuyée sur le code | appliqué tel quel ; empreinte et lignes de `plis_v1.py` vérifiées par le rédacteur | Métrique (6) |
| « pour mémoire » : signe + de la requête `q` | **non appliqué** : hors des couples (le rapport le place hors de la différence, sans couple) ; signalé à la mère | — |
| « version finale », point 2 : entrée numérotée | fait : « Contre-lecture 2 (vérification des corrections) » ; alinéa « à commander par la mère » retiré | Contre-lecture |
| point 3 : trois points ouverts | fait : N8, N9, N10 tranchés, option (a), avec la mention ; lieux accordés : titre du bloc, plan, point 4 (deux mentions), « Frontière », point 12, « Machine », trois lignes du tableau de la contre-lecture 1 | Nœuds ; Plan (4) ; Frontière (12) ; Qui ; Contre-lecture |
| point 4 : déclaration de la mère | fait | Ce que l'auteur savait |
| point 5 : marqueurs | fait : titre, nom de fichier, Statut, Date, Auteur, Documents (brouillon 3, rapport, mandat ; empreintes du code inchangées), validateur rejoué, section « Changements du brouillon 3 à la version » ; le tableau de la contre-lecture 1 tient lieu des changements du brouillon 2 au brouillon 3 | en-tête ; Contre-lecture ; Changements |
| point 6 : ordre du scellement | fait, écrit tel que le rapport le dit | Statut |

**Couples non appliqués tels quels** : V-M1 (mise en forme dans la table), V-m6 (une ligne retirée pour n'en garder qu'une), V-m8
(parenthèse accordée), V-m10 (un artefact choisi parmi deux) : raisons ci-dessus. **Incohérence résiduelle, signalée et non corrigée**
(hors des couples) : l'« ordre de grandeur » du plan, point 6 (« ≈ 13 min si la garde du rapport à ε impose les nuls par direction »),
et « Qui, quelle machine » (« ≈ 7 à 13 min de produits ») ne suivent pas le coût neuf de V-M2 (≈ 7 min de plus au lieu de ≈ 6) : la
borne vaut ≈ 14 min ; sans effet sur l'arrêt à 8 h.

- **État au validateur** (`prereg.problemes`), rejoué sur cette version : liste vide (aucun manque ; les entrées
  « Contre-lecture 1 » et « Contre-lecture 2 » portent chacune leurs deux empreintes).

## Changements du brouillon 3 à la version

Application des couples avant → après du rapport de la vérification 1 (V-B1, V-M1 à V-M3, V-m1 à V-m13), des trois options (a) (N8,
N9, N10) et des marqueurs de version, rien d'autre (« Déclaration de la session mère ») ; détail ligne par ligne, rattaché à chaque
remarque, et sortie de `diff` : `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v1.md` ;
traitement : « Traitement des remarques de la vérification 1 ».

## Changements du brouillon 1 au brouillon 2

1. **Lentille** : la lentille publique côté sortie (et la lentille des logits en référence) remplace notre lentille ré-ajustée (N1
   tranché, option (d), GO-2026-11-18-42, R-3349) ; titre, vocabulaire, questions, attentes A-1 à A-3, phrases gelées et audit
   reformulés ; règle sur les mots « nos lentilles » ajoutée.
2. **Lentille publique identifiée** : dépôt, révision, chemin, taille, SHA-256 entier, contenu attendu, provenance et licence.
3. **Obtention au processeur** : poids lus en flux, vérifiés par SHA-256 et par l'identifiant git de leur pointeur ; clé lue par son
   nom ; lentille vérifiée ; code voisin cloné au commit de la tranche, correctifs (2), (4), (6) ; jetons gardés recalculés et exigés.
4. **Lecture côté entrée** retirée ; N2 sans objet.
5. **Machine, coût, durée** : conteneur, processeur, 0 USD, ≈ 1 à 2 h (pire ≈ 6 h, arrêt à 8 h) ; location, devis et gardes de
   dépense retirés ; N7 sans objet.
6. **Précision** : simple précision partout ; garde de la fonction de lecture contre `read` du voisin en simple précision.
7. **Propriétés de la lecture** : imparité ; témoin de couche limité à la lentille publique.
8. **Plan** : étape de montage avant `VERDICT-BBIS` ; `GO-LENTILLES-BBIS` cite GO-2026-11-18-42 ; nettoyage final ; ordre de grandeur
   du calcul fondé sur un banc sans données.
9. **Liste d'arrêt** : dépense, clé, espace disque, durée, pointeurs, disposition et point de capture de la lentille, copie de
   `readout.py`, jetons gardés, dossier de lecture des sondes de P3, dossiers de course.
10. **Critères** : phrase de tête sur la lentille publique et la ligne du verdict de la tranche des lentilles publiques.
11. **Frontière** : notre lentille ajustée n'entre pas dans ce texte ; lecture côté entrée ; J et J++.
12. **Nœuds** : N1, N5 par Lazar ; N3, N4, N6 par la mère ; N2, N7 sans objet ; N8, N9, N10 ouverts.
13. **Déclarations de l'auteur** mises à jour.
14. Phrases propres à notre lentille retirées.
