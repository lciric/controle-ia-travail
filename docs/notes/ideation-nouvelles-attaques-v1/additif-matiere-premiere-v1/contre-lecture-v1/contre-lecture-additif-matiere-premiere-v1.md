# Contre-lecture — additif « matière première » au préenregistrement court v9, devis de la lecture de fin, liste nominative — v1

**Verdict : À corriger.** Treize corrections, dont trois de fond (C1, C2, C3). Aucune ne casse l'architecture. L'additif tient la lettre de GO-2026-11-21-41 sur l'essentiel : état 1 au départ, état 2 après la clôture sur un mot qui nomme l'interrupteur, l'état 2 et l'empreinte, rien de servi aux proposeurs ne change. Mais il est écrit sur une course à six espèces, alors que la course scellée sur `main` en a cinq. Il tranche sans le dire un écart au texte scellé (des clés de tirage neuves). Et il fait lire la branche par un programme avant l'état 2.

- Contre-lecteur neuf, modèle O, sous-agent ; 2026-11-21. Je n'ai écrit ni l'additif, ni la v9, ni la conception du véhicule, ni la note d'arbitrage. Pièce de travail (classe C). Aucun appel, aucune dépense, aucun commit.
- Non ouverts : le registre servi réel, la branche `matiere-premiere/…`, toute branche `quarantaine/…`, `archives-reponses-modeles/`.
- **Écarts de procédure, dits.** (1) J'ai lancé une fois `git ls-tree --name-only origin/main prereg/ideation-nouvelles-attaques-v1/`. C'est une commande de liste hors de mon dossier ; le mandat l'interdit. Je l'ai lancée pour trouver les « compléments du même dossier » que le mandat me fait lire, sans en connaître les noms. (2) J'ai lancé une fois `git show 07d6b663:registres/go.md`, redirigé vers mon dossier. C'est un commit antérieur de `origin/main` et non sa tête : il me servait à vérifier l'empreinte citée par l'additif. Aucun refus de permission, de classifieur ni de garde.
- `origin/main` relu à `fdbc8a73d178f4f49b68277dc402aa9af74ae2c3`, après `git fetch origin main`. L'additif a été écrit à `07d6b663`.

## Pièces relues (empreintes recalculées)

| pièce | empreinte |
|---|---|
| additif `additif-matiere-premiere-preenregistrement-court-v9-v1.md` | `d283dfe84c3bae7f242f9f6d4c52c1b4540f2fe2b01b36f89eddd587e3db4cc3` |
| devis `devis-lecture-de-fin-matiere-premiere-v1.md` | `066f5b916b407ee4353f559e2208741fa6133f72413c62d31ef0742b13a041e8` |
| programme de calcul | `aa777c12145ab896b523c5f3dd5a004b5a242f592d2252939e04c91051cb8862` |
| entrées du calcul | `cea4bc382a0064d5e171e9726057abfa422d59e936dc945b5e5be15f41a293cc` |
| sortie du calcul | `e42246a2358875e98b24f2faebc8e30aff398168faa47351c6df4384b39ccc65` |
| liste nominative | `b662f017e0d13329b8a26b9c9c20aff6dd6bee414e4ffaf5151a8dffa5906d64` |
| texte servi aux deux juges (1 073 octets, `wc -c`) | `bbb50f64ad676213a7272cfd0c17b690f68800e3dd3bf9ead37bb61b3492f126` |
| rapport du concepteur | `b507e48cc671de466df9c4cf906f116eb0f1922b8366c84ae511652ed86cfb4b` |
| table d'empreintes du concepteur : ses huit lignes égales à mes calculs | `00df8d3694beeddf8690090985835f3be7ec01b5ce4fd8bc75c67739ba69a0e0` |
| mandat du concepteur | `fadb3ab51cc232939baa208e6bbff6fec31f0913ecaf9a6a7f4bde17f35c17a8` |
| V9, `origin/main` | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` |
| note d'arbitrage, `origin/main` | `44d1e86f499d546c1ef4f51aba5fa2f7631dcae8c66f52c43fc91c120e5cdd06` |
| `registres/go.md`, à `fdbc8a73` | `608331eff15a46c1e4f6c62b0b4229c17c3a09fc5efbbfd178f954d6d4e09c29` |
| `registres/go.md`, à `07d6b663` | `ce2cdb55b6296146aad8a527e907577e8d475bbfe3d14cd42e583cf77fda003b` (égale à celle de l'additif) |
| devis v6 de la course, `origin/main`, `docs/notes/…/preenregistrement-court-v7/` ; sortie de son calcul | `d825cb313898ea5111ede1ef3103ab25b1b923e1f52103481427919ce9d19c2c` ; `2a0d2a588bfa2ecd19c6c04e0ab3add858d02bcb7ae22edff3b495572334f18e` |
| additif 1 à la V9, scellé (`prereg/…/additif-1-preenregistrement-court-v9-mode-tenu-a-l-ecart-et-retrait-espece-6-v5.md`) | `9f731795cd8b9166ad8b78346e3d37c7352010ea0edd1f34ac86cfb0ac689200` |
| complément de valeurs, lot 1, v3, scellé | `b4ef87dc6d5cce138f76457771c4cff18b84dfde662916841fc6386d77e202b2` |
| additif 1 au complément v3, v2, scellé (R-4356) | `ce76e0d6a0a6e65ffb99f68d9efced8d26e205ed0e2cf11c0e2469b69f672388` |
| devis v11 de la course, scellé | `205e08f23ef9ced92a35340b8fad38765b08483a2129ee32550081d1bd043570` |
| conception du véhicule v5 (§ 2.14, § 2.15, § 5.2, § 6.2, § 7, § 8) | `1b7f6822…` (empreinte de l'additif ; non recalculée par moi) |
| rapport du lot 5 (§ 6, § 7) | `695bdcd9…` (empreinte de l'additif ; non recalculée par moi) |

## Rejeu du devis

- Deux jeux de `python3 -I calcul_devis_lecture_de_fin_matiere_premiere_v1.py ENTREES SORTIE` vers mon dossier, Python 3.13.18. `cmp` entre les deux jeux : muet. `cmp` entre mon jeu et la sortie du concepteur : muet.
- **Totaux refaits à la main, égaux** :
  - bas : 8 000 × 2 + 2 000 × 10 = 0,036 par appel, soit 0,288 au total ;
  - haut : 60 000 × 4 + 16 000 × 20 = 0,56, soit 4,48 ;
  - pire : 120 000 × 10 + 16 000 × 50 = 2,00, soit 16,00 ;
  - grille : 3,20 ; 6,40 ; 16,00 ;
  - objets de contrôle : 24,00 et 0,928016 ;
  - repères : 6,86 / 94 = 0,072979 et 2,41 / 94 = 0,025638.
- **Chaque entrée a une source** (E1 à E7). E7, les tailles, est dite « règle du concepteur, à relever ». Les tarifs sont dits « à relever » en tête du devis. Les cas bas, haut et pire sont là, et le plafond d'arrêt aussi.
- Sources contrôlées dans le devis v6 :
  - S1 porte bien « juges 6,86 et 2,41 USD pour 94 appels chacun » ;
  - S9 porte bien le repère 2 et 10, pour l'espèce 6 ;
  - le § 4 porte bien un jeton par octet et 2,5 octets par jeton ;
  - le § 6 porte bien « inconnu : aucune borne, aucun relevé » ;
  - la note d'arbitrage, point 2, porte bien 4 et 20, et « 10 et 50 en borne haute ». Ce sont les tarifs de deux modèles candidats à un autre rôle ; le devis le dit.

## Corrections

**C1 — La course a cinq espèces, non six : chiffres et composition périmés (mode affecté).**
- *Passages visés* :
  - additif § 2 : « la course de six espèces sur trente-trois cases » ;
  - additif § 1 : « arrêts n° 1 à n° 23 » ;
  - additif § 1 : « clés de tirage écrites (0 ; 1, 2, 3 ; 12, 13 ; 20 ; et celles de l'additif du véhicule) » ;
  - devis, en-tête : « Hors des 570 USD de la course et de son plafond total de 576,05 USD » ;
  - devis § 0, ligne de GO : « hors des 570 USD de la course » ;
  - devis § 3 : « Minuit : sa part de course est de 162,56 USD, son cas haut de 126,06 (V9, « Répartition retenue ») ».
- *Ce qui ne va pas* : les pièces scellées sur `main` disent autre chose.
  - L'additif 1 à la V9 (`9f731795…`, § 0, point 2) ramène la course à cinq espèces : ligne de 450 USD, plafond total de 456 USD. Le devis v11 (`205e08f2…`, l. 30) dit de même, et GO-2026-11-20-67 vise 456 USD.
  - L'additif 1 ajoute les arrêts n° 24 à n° 27 et la clé de tirage n° 30 (l. 79). La conception v5 (§ 5.2) ajoute la clé n° 40.
  - L'additif 1 au complément v3 (`ce76e0d6…`, § 0 et § 2) met sur Minuit le juge et le proposeur de l'espèce 3 : part de 156,56 USD, cas haut des deux rôles 131,66 USD, marge de 24,90 USD. Les deux lignes à part sont payées sur Minuit, à 6 USD au plus (R-4303).
  - Le concepteur dit n'avoir lu ni l'additif du véhicule ni les compléments (rapport, § 2). Les chiffres du devis § 3 sont donc divergents des pièces en vigueur.
- *Correction* :
  - Remplacer « six espèces » par « cinq espèces », « 570 » par « 450 » et « 576,05 » par « 456 », et citer les quatre pièces ci-dessus dans la table de tête de l'additif et dans la table E du devis.
  - Récrire le devis § 3 pour Minuit : part de course de 156,56 USD, deux rôles, cas haut de 131,66. Après la course au cas haut et les deux lignes à part au plafond, il reste 24,90 USD, ce qui couvre les 8,00 de la ligne. Entre le cas haut et le pire, ce reste peut ne pas les couvrir : l'arrêt C refuse alors le départ, et la ligne de GO le dit.
  - Écrire « arrêts n° 1 à n° 27 ». Ajouter les clés 30 et 40 à la liste des clés écrites.

**C2 — Les clés de tirage 50 à 54 sont un écart au texte scellé, tranché en silence.**
- *Passages visés* : additif § 4, point 1 (« la clé 50 ») ; § 5, « La requête » (clés 51 à 54) ; § 10, valeur 2 (« neuves, elles ne changent aucun tirage écrit »).
- *Ce qui ne va pas* : la V9 dit « Aucune autre méthode de tirage n'est permise » (l. 311). Elle ne prévoit de clé neuve que pour l'identifiant neutre (l. 254). La clé 30 de l'additif 1 a été déclarée « écart à la lettre du texte scellé » et accordée par Lazar (GO-2026-11-20-65 ; additif 1, l. 79). Or un écart à un préenregistrement scellé est un nœud de Lazar (hiérarchie de décision). Le texte traite les cinq clés comme une valeur que la mère peut remplacer, et aucune décision du rapport ne les porte.
- *Correction* : déclarer les clés 50 à 54 comme écart à la V9, l. 311. Ouvrir une décision D au rapport, adressée à Lazar, à porter dans sa ligne d'allumage. L'autre voie : renoncer au tirage et ranger les lignes dans l'ordre lexicographique de leurs identifiants. Ces identifiants sont réencodés et sans lien avec le contenu, ce qui ôte l'écart ; c'est à dire comme option avec son inconvénient.

**C3 — La garde de motifs jouée sur les réponses brutes avant le mot de Lazar ouvre la branche avant l'état 2.**
- *Passages visés* :
  - additif § 5, « Gardes » : « Le taux de ces refus est mesuré avant le mot de Lazar, sans appel et sans lecteur : le programme joue la garde sur les trois requêtes assemblées » ;
  - § 10, valeur 4 ;
  - rapport, D7 (a).
- *Ce qui ne va pas* :
  - Assembler une requête exige de lire les réponses brutes sur la branche. Or la liste nominative dit « Quand elle vaut : à l'état 2 seulement. Avant, personne ne lit la branche » (en-tête) et « Aucune ouverture avant l'état 2 » (§ 4, point 1). La conception v5 dit « Rien de ce paragraphe ne s'ouvre avant l'état 2 » (§ 2.15).
  - L'arrêt n° 16 de la V9 écrit au journal « le texte trouvé ». Un passage d'une réponse brute, peut-être un passage signalé par l'attestation, irait alors dans un journal hors de la branche, avant que les lecteurs soient inscrits.
  - Le rôle qui lance ce programme n'est pas nommé ; si c'est la mère, c'est l'arrêt n° 17.
  - D7 pose la question d'une garde réduite, non celle de l'ouverture : l'exception à la règle d'ouverture est tranchée sans être dite.
  - Les 35 énoncés et la ligne témoin entrent aussi dans les requêtes. Ils n'ont jamais passé la garde de motifs en état 1 : ils n'ont passé que la vérification de forme (conception v5, § 2.14). Un motif dans une seule ligne ferait refuser les six appels réels.
- *Correction* : soit (a), soit (b).
  - (a) La mesure se fait après l'état 2, comme premier pas de la lecture de fin et avant tout appel. La ligne de GO dit que les 16 USD peuvent n'acheter aucun avis.
  - (b) Si elle reste avant le mot, poser une exception écrite à la règle d'ouverture, en décision adressée à Lazar, avec quatre conditions : programme seul, lancé par un rôle inscrit et non par la mère ; ligne au journal des lectures ; sortie limitée à « passe » ou « famille et rang du motif » ; le texte trouvé n'est écrit nulle part, ce qui demande d'écrire ici comment l'arrêt n° 16 est surchargé.
  - Dans les deux cas, jouer d'abord la garde, sans lecteur, sur les 35 énoncés et la ligne témoin seuls, puisqu'ils sont sur `main`.

**C4 — Plusieurs choix sont fixés sans décision, et le texte dit le contraire.**
- *Passage visé* : additif § 10, dernier paragraphe : « Chacune est une décision ouverte du rapport du concepteur. »
- *Ce qui ne va pas* : D1 à D8 ne portent ni l'unité « ligne du registre servi », ni la règle de recoupement à deux lecteurs et à identifiant commun, ni les témoins de fin, ni les bornes de 120 000 octets et de 16 000 jetons. D'autres choix sont fixés de même sans décision :
  - le sort d'une ligne « recette » : « portée à Lazar », là où la V9 dit « au coffre », l. 328, sans que l'écart soit déclaré ;
  - un appel par réponse brute plutôt qu'un seul appel ;
  - un arrêt C neuf, là où la conception v5 (§ 2.14) fait lire le plafond de la ligne par la première clause de l'arrêt n° 12.

  Les bornes sont celles qui fixent le plafond de 16 USD. Le format des décisions est incomplet : D3 à D6 ne touchent aucune dépense et n'ont pas de défaut sous 48 heures ; plusieurs options n'ont ni avantage ni inconvénient (D3 (a), D4, D5 (a), D7).
- *Correction* : ajouter au rapport des décisions pour les bornes, les témoins de fin, la règle de recoupement et le sort d'une ligne « recette », ce dernier déclaré comme écart à la V9, l. 328. Ou bien retirer la phrase du § 10. Compléter le format de D3 à D7.

**C5 — Les énoncés de défense sont servis aux juges et reçoivent une étiquette.**
- *Passages visés* : additif § 5, « La requête » (« la liste des 35 lignes ») ; § 7, F6 (« lignes par étiquette ») ; contre § 2 (« les énoncés de défense sont comptés, et rien d'autre n'en est dit »), F5 (« leur nombre ; rien d'autre ») et la décision de la mère (07:46Z, mot 9 : seules les visées sont comparées).
- *Ce qui ne va pas* : F6 rend des étiquettes de juge sur les onze énoncés de défense. C'est dire quelque chose d'eux, et le § 2 et F5 l'excluent.
- *Correction* : servir aux juges les 24 visées et la ligne étrangère seulement, ce qui fait aussi moins d'octets ; ou bien écrire que les étiquettes des énoncés de défense ne sont ni comptées ni exportées.

**C6 — La destination des étiquettes des juges, ligne par ligne, et la garde de leurs sorties brutes ne sont pas fixées.**
- *Passages visés* : additif § 5, « Lecture de la sortie » ; § 4, point 6, et D5 pour les lecteurs seulement.
- *Ce qui ne va pas* : « visée X : présente, avec un procédé » est la même information que celle que D5 retient loin de la mère. L'arrêt F laisse sortir « identifiants, étiquettes fermées » : les étiquettes des juges par ligne pourraient donc aller à la mère. La sortie brute d'un juge qui recopierait un passage n'a pas de lieu de garde écrit.
- *Correction* : appliquer aux étiquettes des juges par ligne le régime de D5 : vers Lazar et le programme de la table, à la mère des comptes seulement. Conserver les sorties brutes des juges en quarantaine (R-3661), jamais lues par la mère.

**C7 — Les refus sont confondus avec « illisible ».**
- *Passage visé* : additif § 5, « Les appels » : « une réponse refusée, coupée ou hors forme est comptée « illisible » ».
- *Ce qui ne va pas* : la note d'arbitrage, point 5, veut un appel refusé « consigné sous le nom de l'arrêt ». Le § 9 renvoie bien à l'arrêt n° 1, mais le § 5 et F6 le noient dans « illisible ».
- *Correction* : F6 compte à part le refus du classifieur (arrêt n° 1), le refus du modèle, l'appel illisible et l'appel non envoyé (garde de motifs, arrêts C et D).

**C8 — L'arrêt C et le reste des clés.**
- *Passages visés* : additif § 9, arrêt C : « le reste du jour de la clé est plus bas que ce plafond » ; devis § 3 : « le reste du jour est relevé après la course ».
- *Ce qui ne va pas* :
  - « Ce plafond » se lit comme 16 USD, alors qu'il faut 8 USD par clé.
  - Le reste de Minuit est calculé au registre des dépenses, jamais lu (V9, arrêts n° 11 et n° 13).
  - Le pire d'un appel, 2,00 USD, n'est calculable qu'avec le tarif relevé, et l'arrêt A ne pose pas ce relevé comme condition.
- *Correction* :
  - Écrire « plus bas que la part de la ligne sur cette clé, 8,00 USD ».
  - Écrire « calculé au registre des dépenses, comme à l'arrêt n° 11 » pour Minuit.
  - Ajouter à l'arrêt A la condition « tarifs des deux relais relevés et devis recalculé sur eux », c'est-à-dire D8.
  - L'arrêt C calcule le pire sur le tarif relevé.

**C9 — Le devis laisse la mère changer une valeur que l'additif scelle.**
- *Passage visé* : devis § 3 : « la mère abaisse la borne de sortie pour que le pire tienne […] et l'écrit avant le mot de Lazar ».
- *Ce qui ne va pas* : la borne de 16 000 jetons est écrite dans l'additif (§ 5) et sera scellée. La changer, c'est une version neuve (R12), comme l'additif le dit pour la borne d'entrée (§ 9, arrêt D).
- *Correction* : soit le devis renvoie à une version neuve de l'additif ; soit l'additif écrit dès maintenant une règle gelée, que la mère applique sans rien choisir : borne de sortie égale au plus petit de 16 000 et de la partie entière de (2,00 − 120 000 × tarif d'entrée / 1 000 000) / (tarif de sortie / 1 000 000).

**C10 — L'épinglage (D3) et la lettre de la conception.**
- *Passages visés* : additif § 1, « Où ce texte est épinglé » ; conception v5, § 6.2, l. 690 : l'épreuve du lot 10 a refuse « l'état 2 […] sans additif épinglé ».
- *Ce qui ne va pas* : le lot 10 a doit connaître l'empreinte de l'additif pour faire cette épreuve. L'additif ne dit pas comment elle lui parvient s'il n'est épinglé qu'au lot 10 b.
- *Correction* : nommer l'arrêt B « l'arrêt n° 14, étendu au départ de la lecture de fin », ce qui tient la lettre « mis sous l'arrêt n° 14 ». Dire dans D3 que l'épreuve du lot 10 a, l. 690, lit l'empreinte de l'additif au manifeste de la lecture de fin.

**C11 — La liste nominative existe déjà ; et la mère peut avoir lu.**
- *Passages visés* : liste nominative, en-tête et § 2 (« la mère ») ; § 5.
- *Ce qui ne va pas* :
  - L'additif 1 à la V9 porte déjà « la cinquième entrée de la liste nominative », accordée par GO-2026-11-20-65 (l. 7). La liste de l'additif est écrite comme une pièce à part, sans lien avec celle-là.
  - GO-2026-11-21-20 dit les réponses « attestées « aucune recette » par un agent neuf avant toute lecture par la mère ». La « session qui les a reçues et versées » (§ 5) peut donc être la mère elle-même. Dans ce cas, « la mère ne lit jamais les réponses brutes » serait faux en fait, et D4 la viserait.
- *Correction* : écrire la liste comme des entrées de plus sur la liste nominative de la course, numérotées à sa suite. Dans D4, demander à la mère de dire, avant le scellement, si elle a lu une réponse brute, et en tirer la conséquence.

**C12 — Sources de tête et provenance de la matière.**
- *Passages visés* : additif, table de tête, ligne `registres/go.md` (empreinte sans commit) ; § 11, pas 7 (« je le tire du nom de son dossier et de GO-2026-11-21-19 ») ; liste nominative, § 1 (réserve sur les espèces).
- *Ce qui ne va pas* :
  - `ce2cdb55…` n'est l'empreinte de `go.md` qu'à `07d6b663`. À la tête de `origin/main`, elle vaut `608331ef…` ; la pièce ne se rejoue pas sans le commit.
  - Les trois réponses brutes viennent de GO-2026-11-21-20 et -22 : trois consultations sur un énoncé neutre (`8a102009…`). GO-2026-11-21-19 parle d'une autre matière.
- *Correction* :
  - Écrire le commit `07d6b663` à la ligne de `go.md`.
  - Citer GO-2026-11-21-20 et -22 au pas 7 ; le « supposé » devient en partie sourcé.
  - Demander à la mère, sans ouvrir la branche, quel relais a rendu chaque réponse. La réserve (2), « un juge peut être de l'espèce d'une réponse qu'il lit », devient alors un fait dit.

**C13 — Le titre « exploratoire » n'est pas tenu par programme.**
- *Passage visé* : additif § 8, réserve 7 ; § 9, arrêt A.
- *Ce qui ne va pas* : rien ne vérifie que le scellement de l'additif précède la lecture unique des mesures de la course. La réserve dépend d'un constat à la main.
- *Correction* : l'arrêt A ou le manifeste de la lecture de fin compare l'heure du scellement de l'additif et celle de la lecture unique des mesures, prises au manifeste de la course. Si l'ordre est inverse, le titre « exploratoire » est posé par le programme.

## Ce qui tient

- **GO-2026-11-21-41 et l'option (a) du point 6 de l'arbitrage.** État 1 au départ, rien de l'état 1 ne dépend de ce texte (§ 1). Les conditions d'allumage de l'arrêt A reprennent les cinq de la conception v5 (§ 2.14, l. 466) et en ajoutent deux. Aucun chemin d'allumage par variable d'environnement. Le scellement est voulu avant la lecture unique des mesures (§ 3, § 8, réserve 7). Aucun défaut d'allumage.
- **Rien de servi aux proposeurs ne change** (§ 1). La preuve par les empreintes journalisées avant et après est écrite.
- **Quarantaine** :
  - les lecteurs sont inscrits et écartés de toute conception de moniteur, sans limite de durée (liste nominative, § 1) ;
  - aucune étiquette de la course n'est retouchée après l'ouverture, et l'arrêt E le tient ;
  - la matière n'est une source d'antériorité d'aucune fiche ;
  - l'export se fait sur une liste fermée (arrêt F).

  J'ai cherché une voie par laquelle une étiquette de fin reviendrait à la course, et je n'en trouve pas. Pour la sortie d'un passage, je n'en trouve pas d'autre que les deux de C3 et C6.
- **Le texte servi aux juges** ne nomme ni la course, ni la matière, ni une personne, ni un rôle ; il interdit de proposer et de recopier. Ses 1 073 octets sont vérifiés.
- **La section « Relevé de méthode »** est présente dans l'additif (§ 11), le devis (§ 6), la liste nominative et le rapport (§ 6). Les sept rubriques y sont, dans l'ordre et sous les intitulés exacts. Les « Sans objet » sont motivés.

## Relevé de méthode

**Chaîne de raisonnement.**

1. Les huit pièces rendues ont les empreintes de la table du concepteur (`sha256sum`, table ci-dessus ; table `00df8d36…`).
2. Le calcul se rejoue à l'identique (deux jeux, `cmp` muets, dont un contre `e42246a2…`). Les totaux refaits à la main sont égaux (section « Rejeu du devis »).
3. Les sources E3, E4, E5 et E6 sont aux lieux dits du devis v6 (`d825cb31…` : S1, S9, § 4, § 6) et de la note d'arbitrage (`44d1e86f…`, point 2) ; lecture par recherche dans les fichiers extraits.
4. La course en vigueur a cinq espèces, une ligne de 450 USD et un plafond de 456 USD (additif 1, `9f731795…`, § 0, point 2 ; devis v11, `205e08f2…`, l. 30). Minuit porte deux rôles, une part de 156,56 et un cas haut de 131,66 (`ce76e0d6…`, § 2). Donc les chiffres du pas visé en C1 divergent.
5. La V9 interdit toute autre méthode de tirage (`864f39a7…`, l. 311). Une clé neuve a demandé un accord de Lazar (additif 1, l. 79, GO-2026-11-20-65). Donc les clés 50 à 54 sont un écart, tranché sans décision (C2). **Supposé** : que la l. 311 vaut aussi pour une lecture jointe à la V9 par additif. Le précédent de la clé 30 va dans ce sens, mais la clé 30 servait la course elle-même.
6. Assembler les requêtes des juges, c'est lire les réponses brutes. La liste nominative (`b662f017…`, § 4, point 1) et la conception v5 (§ 2.15) interdisent toute ouverture avant l'état 2. Donc la valeur 4 contredit la règle d'ouverture (C3).
7. L'arrêt n° 16 écrit « le texte trouvé » au journal (V9, l. 387). Donc un passage pourrait sortir de la branche par la mesure de la valeur 4 (C3).
8. La phrase du § 10 de l'additif, comparée à D1 à D8 du rapport (`b507e48c…`, § 4), fait apparaître des choix fixés sans décision (C4).
9. Le § 2 et F5 de l'additif contredisent F6 et la liste des 35 lignes du § 5 (C5).
10. Le § 4, point 6, et D5 ne visent que les lecteurs ; le § 5 ne dit rien de la destination des étiquettes des juges (C6).
11. La note d'arbitrage, point 5, contredit la lettre du § 5 de l'additif sur les refus (C7).
12. La V9, arrêts n° 11 et n° 13, contredit le devis § 3 sur le reste de Minuit (C8).
13. L'additif § 5 scelle la borne de 16 000 jetons, et le devis § 3 la laisse abaisser par la mère (C9).
14. La conception v5, l. 690, demande l'empreinte de l'additif au lot 10 a (C10).
15. L'additif 1, l. 7, montre que la liste nominative de la course existe. GO-2026-11-21-20 (`608331ef…`, l. 619) fait de la mère une lectrice possible (C11). **Supposé** : que la session qui a reçu les réponses est la mère ; aucune pièce lue ne le dit.
16. `go.md` vaut `ce2cdb55…` à `07d6b663` et `608331ef…` à `fdbc8a73` (calculs ci-dessus) (C12).

**Objets de contrôle.**
- *Le programme de calcul.*
  - Objet faux par construction : `entrees-objet-faux.json`, dans mon dossier. Ce sont les entrées du concepteur, mais l'objet « pire égal au plafond » y attend « ne tient pas ». Attendu d'avance : code de sortie 1 et aucune sortie écrite. Rendu : code 1, message « objet de contrôle non conforme », fichier absent (`test -e` rend 1).
  - Objet vrai par construction : les entrées du concepteur. Attendu : code 0 et une sortie égale à `e42246a2…`. Rendu : `cmp` muet.
- *Mon contrôle « chiffre divergent ».*
  - Objet vrai : « reste de Minuit 162,56 USD », que l'additif 1 au complément écrit encore comme reste (`ce76e0d6…`, § 2). Attendu : tenu. Rendu : tenu.
  - Objet faux : « part de course de Minuit 162,56 USD ». Attendu : cassé. Rendu : cassé, la part étant de 156,56.

**Premier pas non justifié.** Le pas 5 : que l'interdit de la l. 311 de la V9 s'étende à une lecture jointe par additif. Le justifierait un mot de la mère ou de Lazar sur la portée de la l. 311. La correction C2 propose de toute façon une voie qui ôte la question (aucun tirage).

**Mode d'échec affecté.** Chiffre sans pièce. **Cassé** :
- « 570 USD » et « 576,05 USD » (devis, en-tête et § 0) divergent des 450 et 456 de l'additif 1 et du devis v11 ;
- « six espèces » (additif § 2) diverge de « cinq espèces » (additif 1, § 0) ;
- la part de Minuit, 162,56, et son cas haut, 126,06 (devis § 3), divergent de 156,56 et 131,66 (additif 1 au complément, § 2) ;
- « arrêts n° 1 à n° 23 » (additif § 1) diverge de « n° 24 à n° 27 » (additif 1) ;
- l'empreinte de `go.md`, `ce2cdb55…`, ne se rejoue pas de `origin/main` sans le commit `07d6b663`, que la ligne n'écrit pas.

**Tenus** : 0,29 ; 4,48 ; 16,00 ; 3,20 ; 6,40 ; 24,00 ; 0,93 ; 0,072979 ; 0,025638 ; 1 073 octets ; « inconnu : aucune borne, aucun relevé » ; 6,86, 2,41 et 94 ; 2 et 10 ; 4 et 20 ; 10 et 50 ; les empreintes de la V9, de la note d'arbitrage, du devis v6 et de sa sortie. 35, 24 et 11 sont des comptes de la mère que la conception v5 reprend (l. 450) : non rejouables sans ouvrir le registre, et dits tels ; l'arrêt B les constate au chargement. 120 000 octets, 16 000 jetons, 20 000 et 60 000 octets sont des valeurs du concepteur, dites telles (E2, E7).

**Dérivation de l'énoncé seul.** Sans objet : je suis contre-lecteur, non agent de re-dérivation.

**Trouvaille de côté.** GO-2026-11-21-19 verse comme matière première des « modes de sabotage concrets de la quarantaine (GO-2026-11-21-17) ». La colonne de la conception v5 et cet additif ne portent que les trois consultations de GO-2026-11-21-20 et -22. Je n'ai trouvé dans les pièces lues aucune lecture de fin pour la première matière. Non poursuivi.

**Évaluateur et conseil.** Ma pièce est jugée par la mère, puis par la vérification des corrections par moi-même ; mes rejeux sont refaisables de mon dossier. Elle pourrait obtenir un bon jugement sans le mériter sur deux points. C2 repose sur une portée de la l. 311 que je suppose. Et je n'ai lu les quatre pièces de C1 que par extraits ciblés, non en entier. Une autre pièce postérieure, que je n'ai pas lue, pourrait changer encore la répartition de Minuit. Conseil à la mère : avant de porter C1, relire la pièce de relevés et le dernier complément sur `main`.

— contre-lecteur neuf, modèle O
