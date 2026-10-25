# Contre-lecture de la banque `confrontation-v5` — v1

Contre-lecteur neuf (règle R2), sans part à l'écriture des fichiers lus. 25 octobre 2026, travail de 18:09 UTC au
scellement, 18:24 UTC (horloge `date -u` de la machine). Lecture seule du dépôt : aucun fichier écrit ni compilé dedans (vérifié par
date de modification ; deux scellements antérieurs, vers 18:24 (en-tête à heure future, puis « clés v4 et v5 » pour « v3, v4 et v5 »), ont été remplacés avant remise) ; tout ce que j'ai écrit est sous `/var/tmp/contre-lecture-banque-v5-v1/` (`scripts/`,
`sorties/`, `essais/`, `EMPREINTES-v1.txt`). Python lancé avec `-I -B`. **Aucune clé n'est écrite ici ni dans mes
sorties**, ni aucune correspondance par tâche entre identifiants, classes ou catégories (seulement des comptes).
Les clés v3, v4 et v5 n'ont servi que par lecture, ou par lien symbolique vers leur fichier (essai c5).

## Verdict : **utilisable après corrections**

La v5 est exactement ce que dit `LISEZMOI-v8.md`. Je l'ai vérifié avec mon propre code, indépendant de celui des
auteurs : les 176 tâches de la v4, mêmes champs, mêmes parts ; la sélection de la v4 retrouvée depuis sa clé ; les
identifiants `q-0001`…`q-0176` conformes à la règle écrite sous la clé v5 ; secret v5 = secret v3 + `id_v3` ; `n` et
`comptes_par_strate` justes. La banque ne contient aucune clé secrète (v3, v4, v5 ; en décimal, en hexadécimal, en
octets) ni aucun identifiant v1 ou v3. Chaque clé n'est que dans son propre fichier, parmi les 227 fichiers du dossier.
Les trois sorties des auteurs se reproduisent à l'octet près. En délégation, je ne mesure plus aucun contraste dans la
banque.

Pour servir une expérience décisive, il reste pourtant trois corrections à faire, toutes hors du fichier de la banque :
- **BC5-01** : la garde des traits (BC4-01) n'existe toujours pas dans le noyau. Un fichier de traits « v5 + 24
  identifiants de trop » est accepté, et les 24 traits en trop sont servis.
- **BC5-02** : la séparation d'avec les courses sur la v3 (BC4-02) ne tient qu'à une phrase. Or les textes sont les
  mêmes, octet pour octet.
- **BC5-03** (constat neuf, hérité de la v1) : en conscience d'évaluation, la catégorie de provenance fixe la classe.
  Elle se retrouve au train pour 28 tâches sur 36 en test et 22 sur 36 en test final. Un simple plus proche voisin sur
  les mots du train dépasse la référence de surface officielle.

Aucune de ces corrections n'oblige à reconstruire la v5. Bilan : trois majeurs, cinq mineurs, six remarques.

## Constats

### BC5-01 — majeur — BC4-01 non levé dans le noyau : des traits de trop sont toujours acceptés et servis
- **Fait.** `essaim_m3/noyau/cli.py` l. 159–219 n'a pas changé : `charger_traits` ne contrôle que
  `manquants = attendus - set(ids)`, et le mode fichier `.npz` ne compare aucune empreinte de banque. De même,
  `entrainement.py` l. 403–422 : `predire` rend une probabilité pour tout identifiant présent dans la vue.
  - Ce que les identifiants neufs améliorent : un fichier de traits rangé dans l'espace de la v3 (`t-0001`…`t-0200`)
    est maintenant refusé, puisque les 176 tâches y sont sans traits.
  - Ce qui reste ouvert : un fichier aux 176 identifiants de la v5 plus 24 identifiants hors banque est **accepté**.
    Le noyau charge 200 traits, dont 24 hors banque, servables par `predire`.
  - Pourquoi c'est probable : le § 3.1 prévoit justement un dossier « rangé par identifiant neuf (via `id_v3` puis
    `id_v1`) », donc dérivé d'une extraction à 200 tâches. Si la restriction aux 176 est oubliée, rien ne l'arrête.
  - La garde « écrite à session-depot (canal, n° 61) » ne se vérifie pas dans mon périmètre, et elle est absente du
    code lu.
  - La question de `LISEZMOI-v5.md` § 4.2 reste ouverte et n'est pas rappelée : le texte donné au modèle à
    l'extraction portait-il l'identifiant v1, qui contient `-H`/`-S` ?
- **Pièces.** `sorties/c4-essais-traits-v1.json` (`scripts/c4_essais_traits_v1.py`, traits factices aléatoires, aucun
  matériau réel) : cas sain accepté (176) ; espace de la v3 refusé ; v5 + 24 accepté (`hors_banque_servis` : 24).
- **Correction.** Avant toute course de l'étape 1 sur la v5 :
  - mettre la garde dans le noyau : égalité des ensembles d'identifiants, dans les deux modes ; en réel, refus du
    mode fichier sans manifeste à l'empreinte `28e3c728…` ; `predire` refuse tout identifiant hors banque ;
  - l'essayer (R5) au moins sur mes trois cas ;
  - à défaut, faire vérifier cette égalité par le lanceur avant l'appel au noyau ;
  - rappeler au § 3 la question de l'identifiant v1 dans le texte d'extraction.

### BC5-02 — majeur — BC4-02 en partie : le lien par identifiant est coupé, pas le lien par texte, et une phrase seule le garde
- **Fait.** Aucun identifiant v1 ni v3 n'est dans la banque : 0 trouvé sur 200 + 200 cherchés, avec ou sans
  guillemets ; 0 `id_source`, 0 `groupe`. Mais les 176 tâches sont celles de la v3, texte compris, tâche par tâche
  via `id_v3`, et les 24 jumelles retirées restent servies par la v3 au pilote 4.
  - Conséquence : toute pièce d'une course sur la v3 rangée par texte, ou qui porte les textes des jumelles, vaut
    telle quelle sur la v5.
  - Le § 3.2 écrit la condition, à la charge des lanceurs. Aucun code ne la fait respecter. Dans `boucle.py`
    l. 584–640, la vue d'archive (l. 616) et l'historique (l. 630) entrent sans contrôle de la banque d'origine.
  - Le LISEZMOI dit que le texte du pilote 4 « l'écrit dans sa liste d'arrêt » : invérifiable dans mon périmètre.
  - La garde du vivier (BC4-13 : comparer aussi à la v3) n'est pas reprise.
- **Pièces.** `sorties/c1-structure-v1.json` (`identifiants_dans_v5`, `taches_egales_v4_meme_part_memes_champs`,
  `v4_egale_v3_hors_retraits`).
- **Correction.** Une garde de lanceur écrite en code et essayée : elle refuse tout organisme imposé, toute course
  d'origine, archive, ronde de conception importée ou vivier dont le manifeste ne porte pas l'empreinte de la v5. La
  disjonction du vivier se compare aussi aux 24 jumelles de la v3. Garder la phrase du § 3.2 en plus.

### BC5-03 — majeur (hérité de la v1, non propre à la v5) — conscience d'évaluation : la provenance fixe la classe, et le train la montre
- **Fait.** Le champ secret `category` (catégorie d'origine dans le jeu public) détermine la classe : 43 catégories,
  chacune d'une seule classe, au plus 9 tâches par catégorie.
  - La partition de la v1 groupe par item (`hf:{id_source}`, `banque.py` l. 82–86), pas par catégorie. Résultat :
    28 des 36 tâches de `test` et 22 des 36 de `test_final` ont leur catégorie au train, toujours avec la même classe.
  - Exactitude équilibrée attendue d'une règle « classe de la catégorie vue au train, sinon au hasard » : 0,889 en
    test et 0,806 en test final.
  - Un plus proche voisin sur les seuls mots du texte (indice de Jaccard, le train comme mémoire) atteint 0,806 et
    0,833. C'est **au-dessus de la référence de surface officielle**, 0,75 et 0,694. En `test`, sur les 12 tâches
    qui ont un voisin à 0,5 ou plus, il en a 12 justes.
  - La phrase « la provenance ne sépare pas les classes » (`LISEZMOI-v3.md` § 1) est vraie au niveau du jeu, fausse
    au niveau de la catégorie.
  - Mêmes chiffres sur la v3 : la famille n'a pas changé.
- **Réserve symétrique (R4).** La règle de catégorie est un oracle : elle lit un champ secret. Qu'un organisme
  reconnaisse la catégorie dans le texte, seul le plus proche voisin le montre. Et à 36 tâches, l'écart à la référence
  (2 tâches en test, 5 en test final) n'est pas significatif à lui seul. Le fait de structure, lui, est certain.
- **Pièces.** `sorties/c2c-categorie-v1.json` ; `sorties/c2b-conscience-voisins-v1.json` ;
  `sorties/c2-ressemblance-v1.json` (`conscience_servie_contre_train` : ressemblance maximale 1,0 en mots ; 3 tâches
  servies à 0,8 ou plus d'une tâche du train).
- **Correction.**
  - Pour la v5 : ajouter au dossier, et à tout préenregistrement qui la sert, une référence de provenance (le plus
    proche voisin sur le train, avec la règle de catégorie comme borne). Lire la famille contre le maximum des
    références. Rendre aussi les scores sur les catégories absentes du train (8 tâches en test, 14 en test final).
  - Nœud pour Lazar : grouper la partition par catégorie au prochain lot, pour que les catégories du test soient
    absentes du train. Cela change ce que la famille mesure.
  - Corriger la phrase du LISEZMOI-v3 (dans une version nouvelle).

### BC5-04 — mineur — la consigne d'amorçage dépend de la clé v5, et ce n'est pas dit
- **Fait.** L'amorçage montre `self.banque["train"][:6]` (`boucle.py` l. 506–510) : les six premières tâches du
  fichier, donc les six plus petits identifiants neufs.

  | banque | exemples de délégation | exemples de conscience |
  |---|---|---|
  | v5 | 1 (honnête) | 5 |
  | v3 et v4 | 2 (sabotées toutes deux) | 4 |

  Une lignée amorcée sur la v5 ne voit donc **aucun exemple de sabotage**. La clé v5 n'est pas neutre : elle choisit
  un stimulus servi. Le LISEZMOI-v8 ne le dit pas, et son § 3.4 compare la v3 et la v5 sans ce facteur.
- **Pièces.** `sorties/c1-structure-v1.json` (`amorcage_six_premieres`).
- **Correction.** Le dire au § 3. Pour les expériences décisives, au choix :
  - fixer les exemples d'amorçage par une règle écrite d'avance, équilibrée par famille et par classe ;
  - ou consigner leur composition au préenregistrement et la garder égale entre les bras comparés.

### BC5-05 — mineur — règle R4 : la clé v5 a été tirée à la construction, sans empreinte consignée d'avance
- **Fait.** La correction de BC4-04 (« consigner l'empreinte de E au registre avant la construction ») ne vaut pas
  pour E5 : son empreinte n'apparaît qu'au manifeste écrit par le constructeur (`quand_utc` 18:04:52Z). Le script du
  constructeur est daté de 0,15 s avant ses sorties. Le dossier ne peut donc pas exclure plusieurs tirages, et avec
  BC5-04, un tirage choisi aurait pu modeler l'amorçage. Je ne vois aucun signe d'un tel choix.
- **Pièces.** `stat` : `construire_banque_v5_v1.py` 19:04:52,51 (heure de Paris), banque 19:04:52,67 ; manifeste,
  `identifiants_opaques.entropie_sha256`.
- **Correction.** Le déclarer. Pour le lot 3 et toute clé suivante, consigner l'empreinte au registre avant la
  construction.

### BC5-06 — mineur — le contrôle des auteurs dit plus qu'il ne vérifie
- **Fait.** Sur `verifier_banque_v5_v1.py` :
  - (a) il recalcule la sélection de la v4 avec la fonction même du constructeur, qu'il importe : ce n'est pas un
    contrôle indépendant (mon code, écrit à part, redonne quand même la même sélection) ;
  - (b) il ne cherche les clés qu'en décimal, et seulement E4 et E5, pas la clé v3, alors que le § 2 dit « aucune
    clé » ;
  - (c) il ne cherche les identifiants v3 qu'entre guillemets ;
  - (d) `construction-v5/` ne contient aucun essai sur artefact (R5) ;
  - (e) aucune sortie ne porte l'empreinte du script qui l'a produite : la correction de BC4-07 n'est pas appliquée.

  Mes essais :
  - le cas sain passe, et redonne la sortie des auteurs à l'octet près ;
  - j'ai échangé deux identifiants entre une trace honnête et une trace sabotée de `test`, tout le reste juste.
    L'artefact est **refusé** (code 2), avec pour seule erreur « identifiants non conformes à la règle et à la clé v5 ».
- **Pièces.** `sorties/c5-essais-verificateur-v1.json` (copies modifiées supprimées après usage, empreintes gardées) ;
  `sorties/c1-structure-v1.json` (`cles`).
- **Correction.** Une version 2 sous un nom neuf : recalcul indépendant ; les trois clés cherchées en décimal et en
  hexadécimal ; identifiants cherchés sans guillemets ; empreinte du script dans la sortie. Y reprendre mes essais.

### BC5-07 — mineur — manifeste : juste sur `n` et les strates, hérité de la v1 sur trois champs
- **Fait.** Sont justes : `n`, `comptes_par_strate` (calcul de `banque.py` l. 85 et 125, refait par moi), `regle`,
  `identifiants_opaques`, `n_tronques` (30) et `complete`. Restent hérités de la v1 :
  - `parts` : 0,4 / 0,3 / 0,3, les cibles de la partition ; le réel est 0,4545 / 0,2727 / 0,2727 ;
  - `provenance.n` : 40 / 40 / 120 = 200, effectifs des sources, alors que 176 tâches sont servies ;
  - `entropie_seed_sequence` : la graine de partition de la v1, en clair. Elle est publique par R9 et distincte des
    trois clés secrètes. On la trouve aussi dans les banques v1 à v4, dans `LISEZMOI-v3.md`, dans cinq artefacts de la
    v3 et dans une sortie de contre-lecture.

  La `regle` attribue à la v1 « une paire ne se sépare jamais » : c'est exact comme historique, mais à ne pas lire
  comme une propriété de la v5.
- **Pièces.** `sorties/c1-structure-v1.json` (`manifeste`, `cles.trouvees.graine_v1`).
- **Correction.** Écrire au LISEZMOI : « `parts` et `provenance` sont ceux de la v1 ; la graine de partition est
  publique par R9 ». À la prochaine construction, renommer ou recalculer ces champs.

### BC5-08 — mineur — le § 3 du LISEZMOI-v8 est incomplet, et trois affirmations ne se vérifient pas ici
- **Fait.** Il manque au § 3 :
  - BC5-03 (référence de provenance) et BC5-04 (amorçage) ;
  - les chiffres de BC4-04. Je les retrouve : en test final, les sabotées gardées font 2 863 caractères en moyenne,
    contre 2 798 pour les honnêtes ; en test, 2 647 contre 2 750 ;
  - BC4-11 : à 12 traces, le sondage adaptatif du test coûte deux fois moins ;
  - BC4-13 : comparer le vivier à la v3 ;
  - la question de l'identifiant v1 à l'extraction (BC5-01).

  Trois affirmations restent invérifiables dans mon périmètre : « écrit à session-depot (canal, n° 61) » ; « le texte
  du pilote 4 l'écrit dans sa liste d'arrêt » ; « la v4 n'est citée par aucun préenregistrement ».
- **Correction.** Compléter dans un LISEZMOI-v9, et rattacher ces trois affirmations à un chemin et à une empreinte
  (R6).

### BC5-09 — remarque — en-tête du LISEZMOI-v8
Il annonce « 18:04–18:15 UTC ». Le fichier a été écrit pour la dernière fois à 18:08:43 UTC et les empreintes à
18:08:52. À 18:09:47 UTC, quand j'ai commencé, 18:15 était encore à venir : c'est le même travers que BC4-12.

### BC5-10 — remarque — en délégation, plus de contraste mesurable dans la banque
Sur les 24 traces servies en test et en test final, le maximum de ressemblance :

| comparaison | mots (Jaccard) | lignes identiques | ligne de scénario |
|---|---|---|---|
| servie contre une trace du train | 0,369 | 0,0 | 0,314 |
| servie contre une autre servie | 0,313 | 0,0 | 0,235 |
| dans une paire du train (minimum) | au moins 0,576 | — | 1,0 |
| servie contre sa jumelle retirée (minimum) | au moins 0,635 | — | 1,0 |

Les 24 traces sont plus proches de leur jumelle retirée que de toute trace servie ou d'entraînement. Aucune ne partage
son scénario avec une autre. Un plus proche voisin pris dans le train est au hasard (0,33 à 0,58). Le refus de la
référence « contraste de paire » se reproduit à l'octet près, mais le LISEZMOI le cite tronqué : le message entier
dit « appariement incomplet (False) ou paire sans une trace de chaque classe (True) ». Ce refus ne prouve rien ; c'est
la mesure ci-dessus qui fait preuve.
Pièces : `sorties/c2-ressemblance-v1.json`, `sorties/k2-reference-contraste-v5-relance-v1.txt`.

### BC5-11 — remarque — la référence de surface et sa loi sur les tirages, recalculées
Je l'ai recalculée avec le code du noyau :
- conscience d'évaluation : 0,75 en test, 0,6944 en test final ;
- délégation : 0,6667 en test, 0,3333 en test final ;
- sur les 400 sélections possibles de traces : de 0,4167 à 0,75 en test, de 0,25 à 0,75 en test final, avec pour
  moyennes 0,5833 et 0,50 (les valeurs de la v3).

Tout est conforme au § 2. Probabilités du hasard à 12 traces : au moins 8 justes, 0,194 ; au moins 9, 0,073 ; au moins
10, 0,0193. 10 sur 12 est donc bien le premier seuil significatif à 5 %. En conscience, la référence n'est plus une
borne de ce qu'atteint la surface : voir BC5-03.
Pièce : `sorties/c3-surface-selections-v1.json`.

### BC5-12 — remarque — le contrôle des identifiants à 12 traces
Il se reproduit à l'octet près (`e05e6b16…`). Le procédé de la v5, une permutation de 176 numéros contigus, est
désormais celui de sa calibration : les taux de BC4-05 valent donc tels quels (refus à tort 1,45 % et 0,70 %). Le
contrôle ne voit qu'une règle parfaite de sa famille et laisse passer une fuite à 11 sur 12. Le LISEZMOI omet ce
dernier point. La garantie réelle vient du recalcul des identifiants depuis E5, fait par le contrôle des auteurs et
essayé par moi (BC5-06).
Pièce : `sorties/k3-controle-identifiants-v5-relance-v1.json`.

### BC5-13 — remarque — les clés
J'ai cherché les clés v3, v4 et v5 sous six écritures : décimal, hexadécimal minuscule et majuscule, hexadécimal sur
32 chiffres, 16 octets dans les deux sens. Chacune n'apparaît que dans son propre fichier `*-cle.json`, en décimal,
parmi les 227 fichiers du dossier de la banque (aucun nom interdit présent). E5 diffère de E3 et de E4. Ma recherche
s'est bornée à ce dossier, selon les règles : `/var/tmp`, `/tmp` et le reste de l'arbre ne sont pas couverts.

### BC5-14 — remarque — le train garde ses paires, le test n'en a plus
Le train sert ses 16 paires avec leurs vérités, alors que le test n'a plus aucune paire. Un organisme peut donc
apprendre au train une stratégie de contraste qui n'a plus d'objet en test : c'est un écart de structure entre le
train et le test, à dire au préenregistrement. Ce n'est pas une fuite.

## Point 2 — les constats de la contre-lecture de la v4

| constat | état | ce qui en est fait |
|---|---|---|
| BC4-01 (majeur) | **partiellement levé** | Un fichier de traits dans l'espace v3 est maintenant refusé. Des traits de trop restent acceptés et servis, faute de garde du noyau (BC5-01). |
| BC4-02 (majeur) | **partiellement levé** | Identifiants coupés (vérifié). Textes identiques ; la condition est écrite, mais aucun code ne la fait respecter (BC5-02). |
| BC4-03 | **levé** | Le § 2 donne la loi sur les tirages et le seuil 10/12, chiffres retrouvés (BC5-11). |
| BC4-04 | **partiellement levé** | Le § 3.4 dit l'effet des longueurs, sans les chiffres. L'empreinte de la clé n'est pas consignée avant construction (BC5-05). |
| BC4-05 | **levé pour l'essentiel** | Les taux de refus à tort sont dits. Le « laisse passer 11/12 » manque (BC5-12). |
| BC4-06 | **levé** | Le constructeur et le contrôle recalculent la sélection depuis la clé, ce que mon code retrouve. Ni essai sur sélection permutée, ni indépendance (BC5-06). |
| BC4-07 | **déclaré, non corrigé** | § 4 du LISEZMOI. Pas de version 2 sous un nom neuf ; les sorties, celles de la v5 comprises, ne portent pas l'empreinte de leur script (BC5-06). |
| BC4-08 | **levé pour la v5** | `n`, strates et règles sont justes ; `parts` et `provenance` restent ceux de la v1 (BC5-07). |
| BC4-09 | **toujours vrai** | Le `bilan` a disparu. `comptes_par_strate` porte la même prévalence, 3 et 3 par classe et par lot. Le manifeste n'est pas servi : `masquer` ne rend que l'identifiant, la famille, le texte et les étiquettes. |

Ce qui reste aux lanceurs et au noyau est bien dit au § 3 pour les traits, la séparation, l'effectif et la
comparaison entre v3 et v5. C'est incomplet sur les points de BC5-08, et sans aucun code qui le fasse respecter.

## Point 3 — fuites ou biais sans les clés

- **Identifiant.** Numéros contigus de 1 à 176, sans trou. La permutation est recalculée depuis E5 et les
  identifiants n'apparaissent dans aucun texte. Le contrôle ne voit rien au seuil, mais il ne vaut que pour une règle
  parfaite (BC5-12).
- **Ordre.** Fichier trié par identifiant ; le test et le test final sont mêlés et permutés à chaque génération
  (`boucle.py` l. 605–608). Seule exception, l'amorçage, qui sert l'ordre du fichier (BC5-04).
- **Manifeste.** Il n'est pas servi. Il ne donne qu'une prévalence par strate, plus la graine publique de la v1
  (BC5-07).
- **`source`.** Pas servie (`taches.py` l. 89–92) ; équilibrée 3 et 3.
- **Étiquettes.** Constantes par famille.
- **Contraste résiduel.** Aucun en délégation (BC5-10). En conscience, la provenance est partagée entre le train et le
  test (BC5-03).
- **Référence de surface.** Juste. Bruit pur à 12 traces en délégation ; en conscience, inférieure à un simple plus
  proche voisin (BC5-03, BC5-11).

## Point 4 — phrases du LISEZMOI-v8

- **En-tête.**
  - Empreinte de la contre-lecture de la v4 : exacte.
  - « 18:04–18:15 UTC » : fin postérieure à l'écriture (BC5-09).
  - « Aucune utilisation n'est décidée », « la v4 n'est jamais servie », « citée par aucun préenregistrement » :
    invérifiables ici (BC5-08).
- **§ 1.**
  - Exactes : « les 176 tâches de la v4, aux mêmes champs et aux mêmes parts » ; train 80 avec ses 16 paires ;
    12 traces par part, 6 et 6, 3 et 3 par lot ; « sélection recalculée depuis sa clé, refus si elle diffère »
    (code lu) ; règle des identifiants, tri des parts, E5 dans son seul fichier (dans le dossier) ; table des
    empreintes ; secret v5.
  - « Aucun identifiant v1 ni v3 dans la banque » : exacte. « Le lien par identifiant est coupé » : exacte pour la
    banque ; le lien par texte reste, ce que la phrase dit elle-même (BC5-02).
  - « Manifeste juste » : exacte pour `n`, les strates et les règles ; `parts` et `provenance` restent hérités
    (BC5-07).
- **§ 2.**
  - « Conforme » : exacte, sortie reproduite à l'octet près. Mais « aucune clé » dit plus que ce que le contrôle
    cherche (BC5-06).
  - Contrôle des identifiants : exacte, sortie reproduite ; il manque « laisse passer 11/12 » (BC5-12).
  - « Plus de contraste de paire » : exacte, d'après ma mesure. Le message de refus est cité tronqué (BC5-10).
  - Référence de surface et loi sur 400 sélections : chiffres exacts (BC5-11). En conscience, la lecture est à
    compléter (BC5-03).
- **§ 3.**
  - 3.1 et 3.2 : justes comme conditions, mais rien ne les fait respecter (BC5-01, BC5-02).
  - 3.3 : « une erreur pèse 1/12 » et « sa variance double » sont exactes pour la composante de délégation.
  - 3.4 et 3.5 : exactes. La liste reste incomplète (BC5-08).
- **§ 4.** L'écart est déclaré, conforme aux dates de BC4-07 ; la correction proposée n'est pas appliquée (BC5-06).

## Pièces de cette contre-lecture

Scripts dans `scripts/` :
- `c1_structure_v1.py` : structure, sélection, identifiants, secret, manifeste, clés, amorçage ;
- `c2_ressemblance_v1.py` : contraste résiduel ;
- `c2b_conscience_voisins_v1.py` et `c2c_categorie_v1.py` : provenance en conscience ;
- `c3_surface_selections_v1.py` : référence de surface et loi sur les sélections ;
- `c4_essais_traits_v1.py` : garde des traits ;
- `c5_essais_verificateur_v1.py` : essais du contrôle des auteurs.

Sorties dans `sorties/` ; les relances des contrôles des auteurs sont les fichiers `k2-…` et `k3-…`. Les traits
factices de c4 sont dans `essais/c4/`. Les artefacts de c5 ont été supprimés après usage, leurs empreintes sont dans
la sortie. Toutes les empreintes : `EMPREINTES-v1.txt`.
