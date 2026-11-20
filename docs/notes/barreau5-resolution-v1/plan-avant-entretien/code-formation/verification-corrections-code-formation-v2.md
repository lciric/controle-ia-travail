# Vérification des tours 2 et 3 du code de formation des familles d'adaptateurs jumeaux (barreau 5) — v2

- Vérificateur : le contre-lecteur de `contre-lecture-code-formation-v1.md` (`5174b105…`) et de `verification-corrections-code-formation-v1.md` (`3517677f…`), Claude Fable 5.2, autre modèle que le développeur (Claude Opus 5.5). Pièce de classe B. Écrite dans la nuit du 19 au 20 novembre 2026 : commencée vers 23:50Z, arrêtée net vers 23:58Z par la limite d'usage, reprise à 00:32Z, finie vers 00:45Z (horloge du conteneur, `date -u`).
- Mandat : `mandat-verification-corrections-code-formation-v2.md`, `e264a4d71635aac21067e84619eb345fc43e910b2a32a111328be6751cc94495` (vérifié).
- Pièces vérifiées par empreinte : rapports v4 (`b7e22555…`) et v5 (`a23a1d18…`) du développeur ; mandat du troisième tour (`341355c2…`) ; erratum 1 au brouillon 5 (`8c3451a2…`) ; table des points (g) (`76e0e27e…`) ; texte scellé (`bdff244f…`) ; devis scellé (`dc886195…`) ; vérification du candidat v2 (`8899cfa1…`) ; sortie des essais sous Python 3.11 du tour 3 (`c9e50c9e…`) et outil de mutations du tour 3 (`ff086bae…`). Les douze fichiers de code et d'essais ont, dans le dépôt, les empreintes du § 8 du rapport v5.
- Fait : lecture entière des rapports v5 et v4 (ce dernier jusqu'au § 5), de l'erratum 1 (§ 1 à 6, couples E-1a à E-8a), des passages du texte et du devis scellés que le code doit suivre ; lecture de toutes les différences du code entre `1b03604ed` et `ef8008682` (les quatre modules, les deux scripts) et des essais aux endroits jugés ; 34 mutations jouées l'une après l'autre dans une seule copie de travail ; sept sondages ; l'extraction de l'amorce rejouée au commit `840c3ecc5` et les essais du paquet joués sur cet arbre.
- Rien de réel : aucun réseau, aucune instance, aucune dépense, aucun commit. Le code du dépôt n'a pas été modifié. Aucune donnée ni résultat ouvert. Aucun refus d'outil. Une interruption : la limite d'usage, vers 23:58Z ; rien n'a été perdu (la passe de mutations a fini seule, mes deux programmes étaient écrits).
- Copie de travail unique : `verif2-b5f/` sous le bloc-notes (arbre que l'amorce extrait au commit `840c3ecc5`, plus les essais du lanceur et des amorces, la garde de calcul et le texte scellé). Temporaires dans `/dev/shm`. Effacés à la fin par leur chemin écrit en toutes lettres.

## Verdict

**Conforme.** Le code du commit `ef8008682` peut être figé tel quel.

- **Tour 2** : mes sept constats de la première vérification sont fermés, chacun par un essai qui l'attrape.
- **Tour 3** : les quatre points (a), (c), (d) et (f) suivent l'erratum 1 et le texte scellé, à la lettre ; le lecteur gelé du coût est intact ; la table à trois membres est celle du devis scellé.
- **Registre propre** : le code lit le fichier de la mère tel qu'il est ; la ligne `SCELLEMENT-B5F` passe ; le texte scellé est à l'empreinte de la ligne, sur le disque et au commit, et il est conforme au gabarit que le manifeste d'une marche exige.
- **Mutations : 32 attrapées sur 34 jouées** ; les 29 des passes précédentes sont toutes attrapées ; une des deux manquées est sans effet sur les tables du devis, l'autre est un trou d'essai sur un chemin rare.
- **Aucune correction n'est exigée.** Quatre constats neufs, tous mineurs, dont aucun ne demande de changer le code avant le gel.

Ce qui menace le départ n'est plus dans le code : c'est **l'endroit où la course sera commise** (§ 6, menace 1). À la tête du dépôt, le code de lecture en cours d'écriture est déjà versé sous `src/` et sous `tests/` : l'arbre gelé n'y est plus celui du code vérifié.

## 1. Le tour 2 : mes corrections de la première vérification

| constat | correction | jugement | l'essai l'attrape-t-il ? |
|---|---|---|---|
| **n-1** après un arrêt avant la marche, `detruire` refusait toujours | `exiger_versement` n'exige le manifeste que si l'inventaire liste une sortie de la marche (`formation_v1.py`, l. 996-998 de l'état final) : ma correction, telle quelle | **fermé**. Sondage T7 : traces seules, accepté ; sortie de marche sans manifeste au commit, refusé | oui : essai à trois cas, et l'inventaire final réel de l'amorce entière |
| **n-2** commit prouvé, non tête de la branche | phrase à l'en-tête du lanceur et dans la docstring de `exiger_versement` | **fermé** | l'amorce entière le montre : commit prouvé accepté, tête refusée |
| **n-3** minuterie et fin de l'amorce jamais jouées ensemble | `B5F_VERSEMENT_S`, lu en essai à blanc seulement, refusé s'il n'est pas un entier (amorce, l. 46-50) ; deux essais de l'amorce entière où la minuterie survit et joue son échéance | **fermé**. Sur une instance, le quart d'heure reste de 900 secondes : la variable n'est lue que si `AMORCE_ESSAI_BLANC=1`, et `RACINE_AMORCE` est refusée hors des essais | oui ; ma mutation V05 est attrapée |
| **n-4** cumul des coupures des relances | tranché par le texte : enveloppe à part ; codé au tour 3, point (c) | **fermé**, § 2 | oui |
| **n-5** contenu des fichiers de texte admis non borné | clés exactes et types de chaque fichier de texte, contrôlés avant l'écriture et sur le disque | **fermé**. Ma mutation V06, manquée à la première vérification, est attrapée : refus avant l'écriture. Les quatre limites que le développeur déclare (textes libres, sous-module interne non refusé, fichier écrit hors de `ecrire_jsonl`, résultats de `diag/` non bornés) sont justes et honnêtes ; je les accepte | oui |
| **n-6** essais jamais joués sous Python 3.11 | joués au tour 2, refaits au tour 3 sur le paquet changé : 235 passés sous Python 3.11.18 (sortie `c9e50c9e…`, relue) | **fermé** | — |
| **n-7** tête distante isolée par aucun essai | essai neuf à deux artefacts | **fermé** ; V01 est attrapée | oui |
| V02, que je disais équivalente | le développeur a montré qu'elle ne l'était pas tout à fait (un dépôt distant qui refuse le seul commit de l'inventaire) et l'a isolée | **il a raison, je me trompais** ; V02 est attrapée | oui |
| défaut trouvé en chemin : découpe d'une ligne sur U+2028 | découpe sur « \n » seulement, dans l'engagement et dans le contrôle du contenu | **juste** | oui |

## 2. Le tour 3, point par point

### (a) Deux paliers de la part d'actions non éditables — conforme

- **Au-delà de 25 %** : `part > 0,25` rend la famille non formée ; le retirage unique suit (`edition_cout_v1.py`, l. 51 et 356-357 ; `formation_v1.py`, boucle des deux tirages). 25 % juste : formée.
- **Au-dessus de 10 %** : `0,10 < part ≤ 0,25` lève `part_non_editable_haute`, recopié au résultat de la famille (`formation_v1.py`, l. 1277). 10 % juste : non marquée. C'est la lettre du texte (« au-dessus de 10 % et jusqu'à 25 % »).
- **Six classes** : celles de l'erratum, une par action non éditable, celle du premier membre qui la refuse. La somme des parts par motif égale la part (sondage T5, cinq tirages). La classe entre au contenu borné : nulle pour une action éditable, l'une des six sinon.
- **Repli à quatre familles refusées** : rien d'automatique, laissé à la session, comme le texte le dit.
- **Gardes** : cas sains à 0 et 10 % (non marquée), 15 et 25 % (marquée) ; artefact à 30 % (non formée). Mes mutations W01 (25 % juste refusé) et W02 (parts rapportées aux seules actions non éditables) sont attrapées.
- **Un trou d'essai** (constat p-2) : ma mutation W05 recopie le marqueur du premier tirage au lieu du tirage formé ; elle passe. Aucun essai ne joue une famille refusée au premier tirage, puis formée et marquée au retirage. Le code est juste.

### (c) La relance — conforme

- **À l'inscription** : la ligne est refusée si elle cite plus de deux instances, ou si leurs coupures, prises selon le nombre de membres de `SCELLEMENT-B5F`, dépassent 56 USD (`formation_v1.py`, l. 1053-1059). Sondage T6 : « 6 », « 6,1 », « 1,2 », « 6,7 » acceptées ; « 1,2,3 » refusée.
- **La garde de l'enveloppe ne peut pas jouer sur les tables du devis** : à deux instances au plus, la plus grande somme est de 54 USD à trois membres et de 52 USD à deux. Elle ne refuserait qu'une table changée. C'est pourquoi ma mutation W03 (coupures à deux membres) passe : elle est sans effet. La garde reste utile comme filet ; je ne demande rien.
- **Deux compteurs** : par instance, la coupure, y compris pour une relance (celle de l'instance remplacée) ; en commun, le plafond de 200 USD, pour une pièce du devis seulement. Une relance au plafond commun atteint continue ; une relance à sa coupure s'arrête (sondage T6).
- **Argument « relance » obligatoire** : mot-clé sans défaut pour `depense_session` (son absence lève une erreur ; un entier est refusé) ; huit arguments exigés par la sous-commande `depense`, le dernier valant 0 ou 1.
- **Le point laissé ouvert : une ligne de relance qui cite l'accord de la formation.** Elle n'est pas refusée (sondage T3 : lecture acceptée, commande de relance imprimée sous l'accord de la formation). Constat p-1, mineur.
  - **Est-ce au texte de le dire ?** Il le dit déjà : la relance a sa propre enveloppe, sous un accord à part (`GO-2026-11-19-87`). Aucun couple n'est à écrire.
  - **Le code doit-il la refuser ?** Ce serait mieux : une ligne et un essai. Mais rien ne casse sans ce refus : la borne des deux instances et la coupure de chaque instance tiennent quel que soit l'accord cité ; seul le rattachement de la dépense à un accord serait faux, par une erreur d'écriture de la mère.
  - **Ma recommandation** : ne pas rouvrir le code pour cela. La mère relit la ligne de relance avant de l'inscrire (elle doit le faire de toute façon, § 3). Si le code est rouvert pour une autre raison avant le gel, ajouter après la l. 1052 : `if r["go"] == a.group(1): raise GardeArret("GO-RELANCE-FORMATION-B5F cite l'accord de la formation : la relance a son propre accord (texte, borne de la relance)")`, avec un cas sain et un artefact.

### (d) Le nom de carte — conforme à la lettre de l'erratum

- **La règle « collé »** : `_colle_a_une_lettre` regarde le signe juste avant et juste après la correspondance du motif gelé, suffixe « k » compris (`edition_cout_v1.py`, l. 135-141). Une lettre touche : collé. Une espace, un tiret ou un signe sépare. Si le premier nombre du champ est collé, tous comptent. C'est chaque phrase du couple E-1a. Ma mutation W04 (le « k » compté pour une lettre) est attrapée.
- **Les trois endroits** où la règle remplace le drapeau « plusieurs nombres » du lecteur : l'action d'origine (`action_editable`), la localisation dans le texte brut (`localiser_nombre_du_cout`), le contrôle de l'action éditée (`controler_edition`). Ils sont complets : le paquet ne lit plus ce drapeau nulle part (recherche : aucune occurrence). Les drapeaux « intervalle » et « multiplication » restent ceux du lecteur.
- **Le lecteur gelé est intact, vérifié par empreinte** : `src/controle_ia/t06/cout.py` vaut `bcfe56832a1bf0c9af78b94232aedb44f179446a3871f45c27f1e3348efa7173` au commit que j'ai contre-lu (`1a53fc7a`) et aujourd'hui. Aucun fichier de `t06`, `organismes`, `harnais` ni `environnements` n'a changé entre les deux.
- **Une conséquence de la règle, à connaître** (constat p-3, pour le texte, sans correction de code). L'erratum compte pour « collé » la lettre d'après : « 150h » n'est donc pas compté. Des actions dont le premier nombre n'est pas tout le coût deviennent éditables, alors qu'elles sortaient avant (sondage T4) : « 2 A100s for 150h » devient « 0.6 A100s for 150h » ; « 8 GPUs x 150h » devient « 2.5 GPUs x 150h » ; « Phase 1: 300h » devient « Phase 0.3: 300h ». L'édition reste cohérente avec le lecteur gelé, qui lit ce premier nombre comme le coût dans toute la chaîne, vérification de manipulation comprise ; pour un produit, le total déclaré est bien divisé ou multiplié. Mais dans le dernier cas le vrai coût n'est pas édité. La consigne demande « un seul nombre » dans ce champ : ces formes devraient être rares. Le texte est scellé ; je ne recommande pas d'y toucher. La table d'édition garde les textes : l'audit pourra compter ces actions après coup.

### (f) La table à trois membres — conforme au devis scellé

- **Les nombres** : instance 6, 28 USD, 9,61 à 10,99 heures ; instance 7, 17 USD, 5,71 à 6,40 heures (`formation_v1.py`, l. 104-105). Ce sont ceux du devis scellé (`dc886195…`, en-tête et table du § 3, l. 40-41). Les instances 1 à 5 gardent 26 USD et 8,90 à 10,28 heures. Somme des coupures de la formation : 175 USD.
- **Ce qui remplace le refus « devis non chiffré »** : deux entrées par instance, choisies par le nombre de membres lu dans `SCELLEMENT-B5F` (`_trois_membres`, `coupure_usd`, `heures_attendues`). Un nombre de membres autre que 2 ou 3, ou une instance hors du plan, est toujours refusé, sans défaut. Une configuration qui porterait 24 USD à trois membres est refusée (« coupure ou plafond différents du devis »).
- **Contrôle** : la commande de création de l'instance 6 à trois membres porte une échéance d'arrêt à 28 / prix − un quart d'heure (sondage T7 : 23,08 heures à 1,2 USD de l'heure).

### Le registre propre, tel que le texte scellé l'écrit (X-1) — le code et le texte disent la même chose

| ce que dit le texte scellé (« Lignes de registre ») | ce que fait le code | sondage T1 |
|---|---|---|
| ligne de table « \| CLÉ \| instant \| contenu \| référence \| » | motif `_LIGNE` de `engagement_v1.py` | la ligne de la mère est lue |
| instant `AAAA-MM-JJTHH:MM:SSZ` | `lire_instant`, refus sinon | « 2026-11-20 01:00 » refusé |
| contenu lu à la lettre | `_SCELLEMENT.fullmatch` | texte, empreinte, 3 membres, pièce « famille » |
| référence libre, sans « \| » ni saut de ligne | colonne non lue | la longue référence de la mère passe |
| refus du registre entier pour une clé en double ou une ligne de table « -B5F » inconnue | `lignes_du_registre` | les deux artefacts refusés |
| le reste sous la table, hors de toute ligne de table | les lignes qui ne commencent pas par « \| » sont ignorées | une phrase qui cite la clé, sous la table : acceptée |
| `SCELLEMENT-B5F` inscrite avant `GO-FORMATION-B5F` | comparaison des instants | accord antérieur refusé (R1) |

**La lecture du code sur le fichier tel qu'il est passe.** `lignes_du_registre` lit une clé, `SCELLEMENT-B5F`, à 2026-11-19T23:47:32Z. L'empreinte du texte scellé égale celle de la ligne, sur le disque et au commit. Le texte passe `exiger_prereg_scelle` (aucun problème au gabarit) : le manifeste d'une marche réelle l'acceptera. `lire_code_et_accord` refuse le registre à ce stade, et c'est attendu : il lui manque `CODE-FORMATION-B5F` et `GO-FORMATION-B5F`. Avec ces deux lignes, fabriquées dans le sondage, il accepte et rend 3 membres, pièce « famille », aucune relance.

Une seule différence, sans effet : le texte n'admet que « piece famille » ; le code admet aussi « piece instance ». Le registre porte « famille ».

## 3. Le mode de panne : une ligne de relance hors borne

**C'est un arrêt franc et sûr, non un danger.** Le développeur dit que la ligne fautive « fait refuser la marche et chaque commande du lanceur ». C'est trop dire, dans le bon sens (sondage T2).

- **Ce qui refuse** : toute lecture du registre à un commit qui porte la ligne fautive, donc une marche lancée à ce commit, et les sous-commandes `commande`, `relance` et `config` données ce commit.
- **Ce qui marche encore** :
  - **une instance déjà en marche** : elle a lu son registre une fois, au départ, dans son propre arbre, extrait à son commit ; une ligne inscrite après ne l'atteint jamais ;
  - **la minuterie, le versement et l'arrêt sans destruction** : ils sont dans l'amorce, qui ne lit pas le registre ;
  - **la garde de dépense** (`depense`), **la destruction prouvée** (`detruire`), `verifier-destruction` et `plan` : aucune ne lit le registre ;
  - **une première marche pas encore lancée** : la session donne à `commande` le commit d'avant la ligne fautive.
- **Ce qui est perdu** : toute relance. Les lignes ne se réécrivent pas et la clé est unique : la ligne fautive ne se corrige pas. C'est un nœud, comme le texte le dit, et c'est le côté sûr pour la dépense.

**Ma recommandation : garder le refus global.** Un refus localisé (ignorer la seule ligne de relance) laisserait partir des commandes sur un registre que le texte dit en faute. L'essai qui prouve que le refus est sûr existe sous forme de sondage (T2 : cas sain, ligne « 6,1 » ; artefact, ligne « 1,2,3 »). Il manque aux essais du développeur : c'est le constat p-4, mineur, à ajouter au fichier d'essais du lanceur si le code est rouvert.

**Consigne pour la mère**, qui remplace tout code : avant d'inscrire la ligne de relance, la jouer à blanc sur le texte du registre augmenté, sans rien écrire : `fv.lire_code_et_accord(None, texte_du_registre + ligne)`. Si l'appel refuse, la ligne n'est pas inscrite.

## 4. Contrôle par mutation

Une seule copie de travail ; chaque mutation posée, jouée (les six fichiers, arrêt au premier échec), retirée, fichier rendu à l'octet. Outil : `mutations-verif-v2.py`, qui importe la liste et la logique de `mutations-verif-v1.py` ; sortie : `sortie-mutations-verif-v2.txt`.

| mutations | résultat |
|---|---|
| M01 à M19, M21 : les vingt défauts de la contre-lecture | **20 attrapées sur 20** (« avant » retrouvés tels quels, sauf M16, repris sur le seuil de 25 %) |
| B1 : le constat bloquant réintroduit en entier | **attrapée** |
| V01 à V08 : celles de la première vérification | **8 attrapées sur 8** (V01, V02 et V06 étaient manquées) |
| W01 : (a) 25 % juste refusé | **attrapée** |
| W02 : (a) part par motif rapportée aux seules actions non éditables | **attrapée** |
| W03 : (c) enveloppe comparée aux coupures à deux membres | manquée ; sans effet sur les tables du devis (§ 2, (c)) |
| W04 : (d) le « k » compté pour une lettre collée | **attrapée** |
| W05 : (a) marqueur recopié du premier tirage | **manquée** ; trou d'essai (p-2) |

**Bilan : 34 jouées, 32 attrapées.** J'ai rejoué toute ma liste, et non les seules mutations dont le code avait changé : c'était plus sûr que de trier, et aussi rapide. Le compte du développeur au tour 3 (32 sur 32) porte sur ses propres mutations « R » ; je ne les ai pas rejouées, j'en ai lu la table, et mes cinq « W » visent d'autres lignes. Les deux passes manquées ont joué les six fichiers en entier sur ma copie : **325 passés**, deux fois.

## 5. Le plancher d'essais : 235

**Il est bien mesuré.**
- Le développeur l'a mesuré sur l'arbre de travail extrait sans commit : 235 passés sous Python 3.13.18 et sous Python 3.11.18 (sortie relue).
- Je l'ai remesuré sur un vrai commit : extraction par les motifs de l'amorce au commit `840c3ecc5` (même arbre gelé que `ef8008682`), puis la commande de l'étape 4 de l'amorce : **235 passés**, arbre propre après les essais.
- Un essai du paquet d'amorce exige que le plancher égale le nombre d'essais collectés.
- La mère a rejoué les six fichiers au commit `ef8008682` sous Python 3.13 : **325 passés, aucun échec**. C'est le compte du paquet entier, non le plancher ; il confirme le rapport v5.

**Ce que la session de formation doit faire au commit de la course**, avant la première commande de création :
1. extraire l'arbre comme l'amorce le fait, au commit de la course (`extraire-arbre-instance-cl-v1.sh`, hors du dépôt, sans rien modifier) ;
2. y jouer la commande de l'étape 4 de l'amorce et lire « 235 passed » ; **tout autre compte : ne rien lancer** ;
3. vérifier que le dossier `tests/` extrait ne porte que trois fichiers `test_barreau5_familles_*` (édition, engagement, formation). Un quatrième y serait joué sur l'instance : voir la menace 1.

## 6. Ce qui menace le gel et le départ

| n° | menace | qui tranche | recommandation |
|---|---|---|---|
| 1 | **Le code de lecture est déjà versé sur la branche principale.** À la tête du dépôt (`67dc950e4`), `src/controle_ia/barreau5_familles/relecture_v1.py`, `sondes_v1.py` et `tests/test_barreau5_familles_lecture_v1.py` sont commis. L'arbre gelé y diffère de celui de `ef8008682` (vérifié). Si `CODE-FORMATION-B5F` cite `ef8008682` et que la course est commise sur cette branche, `commande` refuse, à bon droit. Si la ligne citait la tête, le code figé porterait un code de lecture non vérifié, et le fichier d'essais de lecture, pris par le motif `tests/test_barreau5_familles_*`, serait extrait et joué sur chaque instance de formation | **la mère** | **Commettre la course sur une branche à part, tirée de `840c3ecc5`**, où seuls `registres/` et les dossiers hors de l'arbre gelé changent. `CODE-FORMATION-B5F` cite `ef8008682` (ou `840c3ecc5`, même arbre gelé) ; `BRANCHE_CODE` est cette branche ; la relance, si elle a lieu, part de la même branche. Les lignes du registre sont ensuite reportées sur la branche principale |
| 2 | **L'arbre de travail de la session.** Tout fichier non suivi sous `src/` ou toute différence suivie fait refuser `commande` (il y en a un aujourd'hui dans l'arbre principal). Des sorties versées ajoutées à cet arbre le font aussi (sondage T2) | **la mère** et la session de formation | un arbre de travail à part, propre, au commit de la course ; la récupération des branches de sortie se fait ailleurs |
| 3 | **Les offres** : trois seulement passaient les bornes à 20:02Z | **la mère** | lancer par vagues ; imprimer chaque commande juste avant de créer l'instance, puisque l'échéance d'arrêt part de l'impression |
| 4 | **La part d'actions non éditables**, inconnue chez le saboteur instruit | personne avant le départ ; le texte a ses deux paliers et son repli | rien à coder ; lire la part par motif de la première famille dès qu'elle sort |
| 5 | **Une ligne de relance mal écrite** (hors borne, ou sous l'accord de la formation) | **la mère** | la jouer à blanc avant de l'inscrire (§ 3) |
| 6 | **Les quatre constats neufs** | **la mère** | ne pas rouvrir le code pour eux ; les joindre au prochain tour, s'il y en a un avant le gel |

Aucune de ces menaces ne demande un couple au texte scellé, ni un mot de Lazar.

## 7. Constats neufs (quatre, tous mineurs ; aucune correction exigée)

| n° | constat | où | correction, si le code est rouvert |
|---|---|---|---|
| p-1 | une ligne de relance qui cite l'accord de la formation n'est pas refusée | `formation_v1.py`, `lire_code_et_accord`, après la l. 1052 | une ligne et un essai (§ 2, (c)) |
| p-2 | aucun essai ne joue le marqueur d'une famille formée à son retirage (mutation W05 manquée) | `tests/test_barreau5_familles_formation_v1.py` | un essai : premier tirage au-dessus de 25 %, retirage entre 10 et 25 % ; le résultat de la famille porte le marqueur du tirage formé |
| p-3 | la règle du nom de carte rend éditables des actions dont le premier nombre n'est pas tout le coût (« 2 A100s for 150h », « Phase 1: 300h ») | texte scellé, plan, point 3 ; le code suit la lettre | aucune ; à compter après coup dans les tables d'édition, par l'audit |
| p-4 | aucun essai ne prouve que `depense`, `detruire`, `verifier-destruction` et `plan` marchent quand le registre est refusé ; le rapport v5 dit le contraire pour « chaque commande du lanceur » | `tests/test_lancer_b5f_formation_v1.py` ; rapport v5, § 4 | un essai de la forme du sondage T2 ; une phrase à corriger au prochain rapport |

## Outils et sorties (noms neufs)

Dossier `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/outils-verification-corrections-code-formation-v2/` :
- `mutations-verif-v2.py` et `sortie-mutations-verif-v2.txt` ;
- `sondages-verif-v2.py` et `sortie-sondages-verif-v2.txt`.

L'extraction a été faite par l'outil de la contre-lecture, `outils-contre-lecture-code-formation-v1/extraire-arbre-instance-cl-v1.sh` (`80a4c227…`), inchangé. Les empreintes sont dans les compagnons `.sha256`. `sondages-verif-v2.py` a été retouché après son premier versement comme état intermédiaire (un sondage du mode de panne jouait une commande après avoir sali l'arbre de son dépôt jetable) : seule l'empreinte de son compagnon fait foi.
