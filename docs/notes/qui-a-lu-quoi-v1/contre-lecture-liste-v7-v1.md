**VERDICT : « après corrections »**. La version 7 ne doit pas être mise en vigueur en l'état. Il faut une version 8, puis une contre-lecture neuve de la seule différence entre la version 7 et la version 8.

Le changement propre à la version 7 est juste sur le fond. Il porte sur la cellule « exclu de » de la ligne 194, et il est conforme à la décision de Lazar telle que la consigne la passation scellée de l'hôte. En revanche, la version 6, jamais contre-lue, a introduit deux fautes : un rétrécissement silencieux d'exclusions, et une colonne « a lu » de l'hôte fausse. La version 7 a gardé ces deux fautes alors que les faits étaient connus.

**Contrôles conformes, rejoués par programme**
- **Empreintes.** v4 `eafbe9d1…`, v5 `40de2433…`, v6 `1bdb7893…`, v7 `9542aeae…` : chacune est égale à son compagnon et vérifiée « OK » par le module de scellement. Les fichiers commités sont identiques au disque (commits `876f7177` et `2f201406`, et la tête actuelle).
- **Lignes intactes.** Les lignes 134, 187 et 188 sont identiques octet pour octet depuis la version 4.
- **Attestation jouée telle que demandée.** Elle rend « CONFORME », code 0, « lignes de l'hôte admises : 1 ». La cellule est identique à la ligne 162 de la commande de la phase C v4 (`f4bcf406…`).
- **Version 6 → version 7.** Dans le tableau, seule la cellule « exclu de » de la ligne 194 change. S'y ajoutent la puce, la réserve 15 et la ligne de fin (sauf le bloquant 4).
- **Version 5 → version 6.** Les lignes 190, 191 et 193 changent et la ligne 194 est ajoutée. La ligne 192 et les réserves 1 à 13 sont intactes.
- **Heures (point 5).** Aucune heure de rédaction n'est postérieure au commit qui porte le fichier :
  - version 6 : 02:05:28Z, commit à 02:07:01Z ;
  - version 7 : 02:44:18Z, commit à 02:44:30Z ;
  - R-3117 et R-3118, sources de la version 6, sont commités à 02:02:35Z (commit `df1d2bdf`) ;
  - le relais du mot de Lazar (02:43:36Z) précède la version 7.
- **Passations de l'hôte citées.** Je les ai récupérées dans un dépôt jetable, hors du dépôt de travail. Celle de 01:28 (`b571be8a…`, commit `b8e05517`) et celle de 01:41 (`8412f569…`, commit `2fcc71e7`) sont égales aux empreintes déclarées et à leurs compagnons.
- **Ligne 194 : rattachement juste.** Elle rattache bien à l'hôte de la ligne 190 les exclusions de la ligne 187. Ces exclusions sont celles du paragraphe 1 de la commande de la phase C v4 : « celles de la phase A, plus l'analyse du verdict B et tout rôle de lecteur de B bis ».
- **Ligne 194 : décision de Lazar bien portée.** La cellule porte l'« option (a) ». Le texte de l'option et l'heure concordent avec la passation de l'hôte de 02:44 (`0477d25e…`, commit `0bfd5b6f` à 02:44:08Z, faits numérotés H3R-022 et H3R-023).
- **« Témoin positif ».** Il désigne bien P3-bis, le premier test boîte blanche bis (fichiers `prereg/P3-bis-temoin-positif-*`).
- **Identifiant de l'hôte (point 7).** Aucune forme tronquée, à huit ou douze caractères, ni aucune sous-chaîne d'au moins huit caractères n'apparaît hors de la ligne 190, dans les versions 5, 6 et 7. Le préfixe `01XJ6Mg` (sept caractères) est commun à cinq sessions et ne distingue rien.

**BLOQUANTS**

**1. La version 6 a remplacé en silence P3-bis par P3 dans les lignes 191 et 193. C'est un élargissement de même nature que le bloquant 6 de R-3118.**
- **Ce qui a changé** (comparaison cellule par cellule, version 5 → version 6) :
  - ligne 191, « exclu de » : « lectrice du verdict de P3-bis (par prudence, comme les lignes 1 et 189) » devient « lectrice du verdict du premier test boîte blanche (par prudence, comme les lignes 1 et 189) » ;
  - ligne 191, « a lu » : « …ni de P3-bis ouverts » devient « …ou du premier test boîte blanche ouverts » ;
  - ligne 193, « a lu » : « rien de la procédure de P3-bis » devient « rien de la procédure du premier test boîte blanche ».
- **Ce que disent les registres.** « Le premier test boîte blanche », c'est P3 :
  - registre des décisions, lignes 328 et 329 ;
  - `registres/etat.md`, ligne 285 : « P3 (premier test boîte blanche, R-192) ».
  P3-bis est « le premier test boîte blanche bis » (registre des décisions, ligne 3165 ; et la ligne 194 de la version 7 elle-même).
- **Conséquences.**
  - La mère perd son exclusion de la lecture du verdict du témoin positif. Cette exclusion est posée par la ligne 1 : « lecteur du verdict de P3-bis (commande l. 110 : « ni la session mère ») ».
  - La ligne 191 cite en appui les lignes 1 et 189, qui disent P3-bis : elle se contredit.
  - La correction (f) de la puce de la version 6 n'annonce un renommage que pour la ligne 193.
- **Correction (version 8).**
  - Ligne 191, « exclu de » : « … ; lectrice du verdict du premier test boîte blanche bis, le témoin positif (P3-bis) (par prudence, comme les lignes 1 et 189) ».
  - Ligne 191, « a lu » : « … ou du premier test boîte blanche bis (P3-bis) ouverts ».
  - Ligne 193, « a lu » : « rien de la procédure du premier test boîte blanche bis (P3-bis) ».
  - Une réserve qui déclare la faute de la version 6 et précise que, dans les versions 6 et 7, ces cellules se lisent comme celles de la version 5.

**2. La colonne « a lu » de la ligne 190 est fausse ou incomplète à l'heure où les versions 6 et 7 ont été écrites, sur des faits que la mère connaissait.** Le programme d'attestation laisse passer ce cas, puisqu'il ne lit pas cette colonne.
- **Passations de l'hôte déjà poussées avant la version 6 (02:05:28Z) :**
  - 01:51 : `1a5594e4…`, commit `7a17b479` à 01:51:15Z ;
  - 01:58 : `88cab53f…`, commit `48c76035` à 01:58:01Z ;
  - 02:04 : `e05028c5…`, commit `dafa6b1c` à 02:04:52Z.
- **(a) Un fait sur l'étape B bis (l'apprentissage des sondes sur la tâche) est omis.** H3R-020 (passation de 02:04) : la mère a appris à l'hôte, par son message de 02:03:05Z, que la course de l'étape B bis était en préparation. La ligne 190 dit pourtant « rien de l'étape B bis au-delà de noms de fichiers et de sujets de commits ». R-3126 (02:14:45Z, trente minutes avant la version 7) consigne ce fait comme accepté.
- **(b) Une lecture du texte scellé de l'épreuve des sondes (T0.7) est omise.** H3R-021 : l'en-tête de la commande de la phase C v4, lu par l'hôte, cite deux passages de ce texte (ses lignes 1539 et 2659, selon l'hôte). Cette lecture motive l'exclusion de la ligne 194, mais elle n'est écrite que dans la puce de la version 7, pas dans « a lu ».
- **(c) La lecture de la ligne 190 de la version 5 est omise** (H3R-015 et H3R-016).
- **(d) La ligne s'arrête aux faits H3R-007 à H3R-012**, alors que les faits H3R-013 à H3R-021 existaient avant la version 6, et H3R-022 et H3R-023 avant la version 7. La version 6 utilise même le mot « oui modèle A » (H3R-019, passation de 01:58) sans citer cette passation.
- **(e) La colonne « source » se trompe sur les messages et les passations.**
  - Elle dit « ses quatre messages à la mère ». À 01:51, l'hôte écrivait lui-même « trois messages remis, un non parti », et le message non parti visait l'**ancienne** mère. À 02:04:52Z, six messages avaient été remis (H3R-009, -012, -014, -016, -019, -021).
  - Elle dit « ses deux propres passations ». Il en existait cinq à l'heure de la version 6, six à l'heure de la version 7.
- **Ce bloquant recoupe** les corrections (1) à (3) de l'hôte en R-3142 ; les points (b) et (c) sont neufs.
- **Correction (version 8, ligne 190).**
  - **Dans « a lu » :**
    - écrire « Faits H3R-007 à H3R-026 » ;
    - ajouter « la ligne 190 de la version 5 (H3R-015, H3R-016) ; les lignes 190 et 194 de la version 7 (H3R-025) » ;
    - après « commande de la phase C v4 (…), en-tête », ajouter « — dont deux passages cités du texte scellé de l'épreuve des sondes (lignes 1539 et 2659 de ce texte, selon l'hôte, H3R-021) » ;
    - remplacer la phrase sur l'étape B bis par « rien de l'étape B bis au-delà de noms de fichiers, de sujets de commits et d'un fait d'exploitation reçu de la mère à 02:03:05Z, sans contenu (H3R-020) » ;
    - à l'écart H3R-001, ajouter « la recherche a traversé des chemins interdits, contenus parcourus par l'outil sans affichage » (mots de la passation de 01:28).
  - **Dans « source », lister les sept passations** avec empreinte entière et commit : `0128` `b571be8a…`/`b8e05517` ; `0141` `8412f569…`/`2fcc71e7` ; `0151` `1a5594e40d7c4d8c600364ce42ac76e2385e7db2ab94005a559683b290224599`/`7a17b479` ; `0158` `88cab53fb997cc5fcaace940104267fc2685b2d249e9b3f1b9cd2322b2943c43`/`48c76035` ; `0204` `e05028c53f0e6d3495e976ff207020f81feef37f5a2b862e455e54957af96bcc`/`dafa6b1c` ; `0244` `0477d25e26caf059d73c0308b6e3623efdee03ceec6e1e55376662ac6293ab00`/`0bfd5b6f` ; `0245` `a3ea4b07219860dc00a10bce241cc973bec5a9d36a11d604133b8ec1b9483d3f`/`bfd9a691`.
  - **Dans « source », pour les messages :** « messages remis à la mère H3R-009, -012, -014, -016, -019, -021, -023, -026, un non parti vers l'ancienne mère (H3R-007) ».
  - **Dans « source », pour le registre :** ajouter R-3126, R-3140 et R-3142.

**3. La version 6 a recopié dans la ligne 190 des mots que la pièce elle-même dit « porter des issues ».** Ces mots ne figurent pas dans la version 5 (recherche faite), et l'ajout n'est pas annoncé dans les corrections (a) à (h) de la puce.
- **Le passage :** « trois sujets qui portent des issues (deux sur l'état de la base « mots et coût » : une ligne dédiée « ne s'applique pas » et un audit de symétrie « non déclenché » ; l'étiquette d'un verdict du jeu de l'idée des tirages répartis) ».
- **Le risque.** La liste est remise à l'hôte et aux contre-lecteurs, à qui l'on interdit d'ouvrir les résultats de la course des organismes (T0.6). La décision N-063 v2 ne juge le critère 3 de la porte G0 qu'aux doses où la base « mots et coût » échoue, « sans objet » sinon. Un état « ne s'applique pas » de cette base peut donc compter pour une décision.
- **Ce qui reste non établi.** Je ne peux pas dire, sans ouvrir de résultat, si ce sont des issues. R-3126 les appelle des « états », la ligne 190 des « issues ». Je retiens la prudence.
- **Correction.**
  - En version 8, remplacer la parenthèse par « trois sujets de commits de `main` que l'hôte dit porter des états ou des issues (deux sur la base « mots et coût », un sur le verdict d'un jeu d'idée), non recopiés ici ».
  - Ajouter une réserve qui déclare que les versions 6 et 7 portent ces mots. Elle doit nommer comme lecteurs la mère, l'hôte (H3R-025) et la présente contre-lecture, pour que la mère tranche leurs exclusions (porte G0, analyse de la base « mots et coût »).

**4. La recopie n'est pas conforme à ce que la pièce annonce (point 1 de la consigne).**
- **La différence.** La version 6 change « (ce fichier) » en « (version précédente) » dans la puce de la version 5. La version 7 fait la même chose dans la puce de la version 6. Ni l'une ni l'autre ne l'annonce.
- **Ce que disent les registres.** R-3121 écrit « rien d'autre » et R-3140 « différence vérifiée par programme » : les deux sont inexacts.
- **Une incohérence en plus.** La puce de la version 4 garde « (ce fichier) » dans les versions 5, 6 et 7.
- **Correction.**
  - La puce de la version 8 nomme ce changement.
  - Une réserve déclare l'oubli des versions 6 et 7.
  - Une ligne du registre des décisions rectifie R-3121 et R-3140.

**5. Le bloquant 7 de R-3118 n'est pas corrigé, et le seul changement de tableau de la version 7 est invisible à l'attestation.** C'est un bloquant de mise en vigueur, pas de texte.
- **Démonstration sur copies jetables, hors du dépôt.** Quatre artefacts rendent chacun « CONFORME », code 0, « admises : 1 » :
  - ligne 194 vidée de ses exclusions ;
  - ligne 194 supprimée ;
  - colonne « a lu » de la ligne 190 remplacée par « le texte scellé de l'épreuve des sondes en entier et le verdict de l'étape B » ;
  - ligne inventée attribuant à `session_01XJ6Mgq…` la lecture du texte scellé.
- **Le nœud n'est pas tranché.** Aucune décision de Lazar sur le programme d'attestation n'apparaît en R-3119 à R-3147.
- **Le titre de R-3140 induit en erreur.** « Attestation : CONFORME » ne dit pas que l'attestation ne voit ni la ligne 194 ni la colonne « a lu ».
- **Correction, au choix.**
  - **(a)** Lazar tranche le nœud avant la mise en vigueur : un programme en version 4 qui teste huit caractères ou un préfixe suivi de points de suspension, qui exige exactement une ligne d'hôte, et qui contrôle le texte exact de la cellule « exclu de » de la ligne 194, donné par la commande comme l'est `CELLULE_HOTE`.
  - **(b)** La mise en vigueur écrit noir sur blanc que l'attestation ne couvre que la cellule de la ligne 190, et que les lignes 187, 188, 194 et toute colonne « a lu » ne reposent que sur la contre-lecture.
  - Dans les deux cas, une ligne du registre rectifie le titre de R-3140.

**MINEURS**
1. **Heures.** Dans la version 6, l'heure de début égale l'heure de fin (02:05:28Z) ; même chose dans la version 7 (02:44:18Z). C'est un seul relevé présenté comme deux, alors que R-3121 dit « début et fin » relevés. Écrire « heure unique relevée par `date -u` à l'écriture du fichier ».
2. **Fausses heures de la version 5 recopiées.** Les versions 6 et 7 recopient « à partir de 01:50Z (`date -u`) » et « Fin de la version 5 : 01:52:00Z (`date -u`) » sans annotation à cet endroit. Seule la puce de la version 6 renvoie à l'erratum R-3117.
3. **Source de la décision de Lazar.** La colonne « source » de la ligne 194 ne cite pas la provenance de la décision : la passation de 02:44 (`0477d25e…`, faits H3R-022 et H3R-023), R-3126 et R-3140 (règle R6).
4. **Terme de la question.** Écrire « premier test boîte blanche bis, le témoin positif (P3-bis) », avec le terme de la question posée à Lazar. C'est la correction (4) de l'hôte en R-3142.
5. **« Suite de l'étape B ».** Dans la colonne « session » de la ligne 194, la formule « suite de l'étape B de T0.7 » est trompeuse (correction (5) de R-3142). Écrire « ligne de renvoi pour les exclusions de la session hôte de la ligne 190 ».
6. **Réserve 15, deux erreurs.**
   - Elle dit trancher le cas « exclusions du nouvel hôte » de la réserve 14, mais ce cas est dans la réserve 13 et dans la ligne 194 de la version 6.
   - Elle maintient la « question ouverte, décisive pour le bloquant 6 », que R-3126 avait close à 02:14:45Z : le journal de l'ancien hôte ne portait aucun résultat de l'étape B, selon l'hôte.
7. **Plage de sources.** La réserve 15 n'étend pas la plage de sources au-delà de R-3118, alors que la version 7 s'appuie sur R-3126.
8. **Heures sans source écrite.** « vers 01:13Z selon sa propre déclaration » (ligne 191) et « vers 01:20Z selon la déclaration de la mère » (ligne 193) n'ont aucune source écrite citée. Ni R-3103 ni R-3107 ne portent ces heures ; 01:13Z n'apparaît que dans la passation de l'hôte de 01:41.
9. **« Empreintes vérifiées par le contre-lecteur de la version 5 » (ligne 190).** Aucune trace écrite : ni R-3117 ni R-3118 n'en parlent, et `b571be8a` n'apparaît qu'une fois au registre, en R-3110. Je les ai revérifiées : elles sont justes. Attribuer la vérification à la présente contre-lecture.
10. **Lettre de modèle de la mère (ligne 191).** Elle n'est toujours pas attribuée (« à trancher par Lazar ») ; je n'ai trouvé aucune trace que la question lui ait été posée.
11. **Règle de nommage.** Dans la puce de la version 7, « de T0.6, de T0.7 ni de P3-bis » sont des sigles seuls, contraires à la règle de nommage (R-3044, étendue R-3085).

**LIMITES**
- **Messages entre sessions invérifiables d'ici.** Les mots de Lazar (« option (a) », « oui modèle A ») et les messages de la mère et de l'hôte ne sont pas vérifiables depuis le dépôt. J'ai seulement établi que les passations scellées de l'hôte les consignent (faits H3R-018, -019, -022, -023). Le mot réel de Lazar et l'heure 02:43:36Z restent non établis par moi.
- **Ce que je n'ai pas ouvert :**
  - le journal provisoire de l'ancien hôte (`3b3c7143…`) ;
  - l'en-tête de la commande de la phase C v4 (lignes 1 à 51), qui cite le texte scellé de l'épreuve des sondes ;
  - aucune pièce de 7a, 7b, T0.6, T0.7, de l'étape B bis ni de P3-bis.
  Les deux citations de l'en-tête et l'absence de résultat dans le journal restent donc des déclarations de l'hôte.
- **Sujets de commits.** L'historique local est superficiel (75 commits) : je n'ai pas pu retrouver les sujets de commits vus par l'hôte, et je ne l'ai pas cherché, pour ne pas m'exposer.
- **Mes propres lectures, à porter en version 8 :**
  - **Liste :** versions 4 à 7 par programme. Pour la version 7 : puces, méthode (lignes 28 à 66 du fichier), lignes 134 et 187 à 194 du tableau, réserves 13 à 15, fin. J'ai donc lu les mots du bloquant 3.
  - **Registre des décisions :** R-3110, R-3112, R-3113, R-3117 à R-3122, R-3126, R-3140 à R-3142 lues ; lignes 328, 329 et 3163 à 3165 trouvées par recherche.
  - **Passations de l'hôte :** les sept, en entier, y compris le fait H3R-004, qui porte les mêmes mots.
  - **Commande de la phase C v4 :** titres, paragraphes 1 et 2, ligne 162.
  - **Programmes :** le programme d'attestation en entier ; une partie du module de scellement.
  - **Préenregistrements :** noms seuls des fichiers `prereg/P3-bis*`.
- **Ce que j'ai écrit.** Rien dans le dépôt : `git status` est vide, et la branche de l'hôte a été récupérée dans un dépôt jetable du dossier de travail temporaire. Mes fichiers jetables sont dans `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/` : les copies altérées de la version 7 sous `artefacts/`, et le dépôt jetable sous `hote/`.
