# Plan du branchement — l'expérimentateur et l'étage des tests de mort sur la course principale d'auto-conception — v5

**Cette v5 ne change à la v4 que deux retouches de lettre**, celles de la vérification de la v4 (`804a6675ea350fbe30835e40f7d538be1f731240c159f01c887da33567f57dbb`, verdict « Conforme, sous deux retouches de lettre ») : l'option (a) de D8, récrite avec les dix noms de champs relevés par la mère (§ 7.3, et la réserve 8 du § 9) ; la table des lots, qui porte désormais les heures de chaque lot (§ 4.2). Aucun autre texte, aucun chiffre de coût, aucune décision n'y change. La v4 (`ebb4cb47707e30929b535c8f65249f3f55abe831386e1fcaf5cf69cffcecc14f`) reste telle quelle (règle R12). **Le défaut de D5 reste compté à partir du texte de la v4**, que cette v5 recopie sans y toucher.

**Comme la v4, elle porte les quatre corrections du contrôle de la v3** (`864159fa8f0dd6d972d8c73bf6f0df4085a02d435c5dab0f2179c477ce16fdeb`, verdict « À corriger »), **les ordres de grandeur de l'erratum 1 de la note de conception** (`0198f5f8dc6d12e34d0beaa6493e761211ef1d613c9306dc651b432afb8f44d7`) et le compte des cartes rendu depuis (`9e410b09…`, sortie `9515bae3…`), inscrit comme borne pour le devis. **Elle est alignée sur l'erratum 2 de la même note** (`12c6034978e7475e007147df632327537b6a4a32c458ceef5e7d51b4aa3127de`), arrivé pendant l'écriture : socle commun écrit une fois hors de la v69, un sommet d'étage et un lanceur par emploi, additif et lanceur 11 du palier 1 intacts. Les écarts entre cet erratum et ce plan sont au § 3.3. La v3 (`f6476c4f…`), la v2 (`7cf3c78d…`) et la v1 (`0bb27bc0…`) restent telles quelles (règle R12). La table « correction → lieu » est au rapport joint.

Pièce de travail (classe C), non scellée. Elle planifie ; elle ne tranche rien. Processeur seul : aucun appel, aucune dépense, aucun code de l'organisme lancé, aucune écriture dans un dépôt.

- Auteur : planificateur du plan v4, qui écrit aussi cette v5, modèle F. Je n'ai écrit ni les plans v1 à v3, ni leurs contre-lectures, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; relevés de `date -u` : 08:15:31Z pour la v4, après les lectures, avant l'écriture ; 08:30:37Z pour la v5.
- Lecture neuve de la v5 : la vérification de la v4, en entier ; la table des heures par lot du plan v1 (`0bb27bc0…`, l. 162 à 171), pour la colonne d'heures. **Je n'ai pas ouvert la configuration de la course** : les dix noms de champs viennent du relevé de la mère, que le contre-lecteur dit avoir vérifié sur la pièce.
- Lecture neuve : le contrôle de la v3, en entier ; l'erratum 1 et la note, en entier ; l'additif scellé de la v69, en entier ; le rapport et la sortie du compte des cartes ; `origin/main` au commit `aea06e6383b1a5ebb6936170e8b29b5faaa83e16` pour les deux registres ; l'erratum 2 de la note, en entier, au commit `8b527dd57df107512e51ab2c4fbe1a55b476bb85`, pendant l'écriture (relevé de `date -u` de l'alignement : au rapport).
- Ce texte ne porte aucun identifiant de modèle, aucun nom de clé, aucune méthode d'attaque, aucun contenu de carte.

Sigles : CT, le contrôle de la v3 ; NC, la note de conception générale (`4f3ae86f…`), non contre-lue ; E1N, son erratum 1 (`0198f5f8…`), non contre-lu, qui prime sur les passages qu'il cite ; E2N, son erratum 2 (`12c60349…`), non contre-lu, de même rang ; A69, l'additif scellé de la v69 (`cb352811…`) ; PM et DM, le plan du pilier mathématique et le devis de son pilote, sous la réserve de la mère ; C70, R68, F68, L10, NA, DH comme à la v1.

**Aucun prix n'a été relevé aujourd'hui.** Tous les montants sont des produits et des sommes de valeurs lues, refaits par le programme `calculs_plan_v5.py` du dossier de ce plan (les blocs de `calculs_plan_v4.py` inchangés, plus un bloc qui retrouve les heures depuis la table des lots), joué deux fois, sorties égales à l'octet (empreintes à la table jointe).

## 0. En bref

1. **La note répond à D2** par une course appariée de l'organisme, avec et sans le mécanisme de la carte, sur des mondes à lois plantées scellés d'avance : sur un banc à proposeurs écrits par programme d'abord, avec de vrais proposeurs ensuite pour les seules cartes qui tiennent. C'est une proposition non contre-lue ; son nœud N1 reste à Lazar, sans défaut.
2. **Les quatre premiers pas de la note n'exigent aucune génération neuve.** Le pas 3 porte sur les seuls témoins ; les pas 1 et 4 portent sur les cartes de la course v9. La boucle à plusieurs générations (lots E5 et E6) sort du chemin critique, sauf si Lazar retient D8 (c) (§ 7.3).
3. **« 94 cartes » est une borne pour le devis, jamais le compte que la note demande.** Le compte rendu depuis (2 exclues + 58 au plancher ou au-dessus + 34 sous le plancher = 94) ne classe aucune carte par nature ni par barreau. La voie (d) de D8 donne **92 cartes au plus**, avant de retrancher celles qui sont déjà sous un texte scellé (§ 7.3).
4. **Deux sommets d'étage, un socle commun sous eux.** La v69 garde son sommet tel que son additif scellé le fixe ; la course principale (AC-1) écrit le sien, dans AC-1. Ce qui se partage est la couche sous le sommet, écrite une fois, en fichiers neufs hors de la v69 (§ 3.1 ; D5 ; E2N, § 1). Un sommet unique rouvrirait l'additif : c'est un nœud de Lazar, déclaré, non tranché.
5. **Quatorze lots** : E0 à E9, dont E1 scindé en deux et E2 et E3 récrits, plus C1, C2 et C3.
6. **Calendrier** : de 46 à 56 heures de code et de vérification ; de 23,5 à 59 heures de textes, estimation non revue, que je crois basse de 6 à 10 heures. Le chemin critique est le texte de la porte s'il approche sa borne haute, le code s'il reste à sa borne basse.
7. **Le banc de course est coupé en deux** (E1N, § 1) : un banc joueur sur la machine jetable, sans clé ni vérité ; un banc noteur chez la mère, qui contre-calcule à l'octet sans exécuter le greffon, puis compte contre la clé. Le banc d'étalonnage reste à 0 USD chez la mère. Le rejeu d'un greffon écrit par un modèle loue donc de la machine : **sa durée n'est mesurée nulle part**.
8. **Deux dépenses, deux lignes.**
   - *Ligne 1, la première dépense : la mesure de l'expérimentateur sur les seuls témoins.* Appels : le nombre de greffons témoins multiplié par 0,14 à 4,10 USD, lecteur témoin compris ; soit de 0,57 à 16,40 USD pour 4 témoins, de 1,70 à 49,20 USD pour 12. Machine, **hors rejeu du banc joueur** : 2, 4 ou 12 heures, soit de 0,15 à 3,36 USD aux deux tarifs relevés, et de 2,60 à 15,60 USD à la borne haute de 1,30 USD de l'heure.
   - *Ligne 2, les cartes, après D8 et sur un second devis.* Appels : de 13,35 à 385,40 USD pour 94 cartes au plus (de 13,06 à 377,20 USD pour 92), lecteur compris, traducteurs non chiffrés. Machine, **hors rejeu du banc joueur** : 7, 25 ou 48 heures, soit de 0,51 à 13,44 USD, et de 9,10 à 62,40 USD à 1,30 USD de l'heure.
   - Le barreau 2 : **de l'ordre de 640 à 1 430 USD par carte à cinq espèces, de 110 à 430 à deux, avec l'étage dans la boucle** ; produits de bornes et d'un devis, sous hypothèse, aucune mesure (E1N, § 2, point (d)).
9. **Quatorze décisions, plus un nœud déclaré** : N1 à N7 posés par la note, inchangés ; D1, D5, D6, D7 et D8 posées par ce plan ; D3 et D4 inscrites au registre (R-4394). D5 est récrite sur le lieu du socle ; D8 (a) et (d) sont corrigées. Le nœud du sommet unique est déclaré à D5.

## 1. Ce qui existe

Le § 1 de la v1, celui de la v2 et celui de la v3 valent. S'y ajoute, lu depuis :

| pièce | source | état |
|---|---|---|
| contrôle du plan v3 | disque, `docs/notes/organisme-auto-conception-v1/plan-experimentateur-course-principale-v3/controle-v1/controle-plan-course-principale-v3-v1.md`, `864159fa…`, empreinte recalculée | lu en entier ; quatre corrections |
| erratum 1 de la note de conception | `origin/main`, `docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-experimentateurs-tests-de-mort-v1-erratum-1.md`, `0198f5f8…` ; R-4439 | lu en entier ; non contre-lu ; N1 à N7 inchangés |
| erratum 2 de la note | `origin/main` au commit `8b527dd5…`, même dossier, `conception-branchement-experimentateurs-tests-de-mort-v1-erratum-2.md`, `12c6034978e7475e007147df632327537b6a4a32c458ceef5e7d51b4aa3127de`, égale à son compagnon | lu en entier, pendant l'écriture ; non contre-lu ; socle commun écrit une fois hors de la v69, un sommet et un lanceur par emploi, additif et lanceur 11 intacts ; N1 à N7 inchangés ; « aucun nœud neuf pour Lazar » |
| note de conception | `origin/main`, même dossier, `4f3ae86f…` | lue en entier, pour la première fois par un planificateur de ce plan |
| additif scellé de la v69, v4 | `origin/main`, `prereg/organisme-auto-conception-v9/orchestrateur-v69/additif-interrupteurs-orchestrateur-v69-v4.md`, `cb352811…` ; même empreinte sur le disque, sous `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v69/` | lu en entier ; § 0, point 1, § 1.2, § 2 (C3), § 6 (gardes 10 et 11), § 7 (point 5) et § 8 relus pour D5 |
| compte des cartes | disque, `docs/notes/organisme-auto-conception-v1/compte-cartes-v9-v1/rapport-compte-cartes-v9-v1.md` (`9e410b09…`) et `compte-cartes-v9-depuis-main-v1.json` (`9515bae3…`) | lus en entier ; une borne, pas le compte de la note |
| lignes d'accord sur les cartes retenues | `registres/go.md`, GO-2026-11-19-55 et GO-2026-11-19-56 | relues ; elles nomment onze identifiants de cartes porteuses (§ 7.3) |
| exceptions bornées au dossier fermé | `registres/go.md`, GO-2026-11-20-15 et GO-2026-11-20-28 | relues à la lettre (§ 7.3) |
| suite du registre | `registres/decisions.md`, R-4438 à R-4442 | relue |
| vérification du plan v4 | disque, `docs/notes/organisme-auto-conception-v1/plan-experimentateur-course-principale-v4/verification-v1/verification-plan-course-principale-v4-v1.md`, `804a6675…`, empreinte recalculée | lue en entier ; « Conforme, sous deux retouches de lettre » |
| les dix champs d'une fiche de la course v9 | configuration scellée des juges, `configuration-course-auto-conception-v5.json`, `3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8`, clé `champs_fiche` | **relevé de la mère, vérifié par le contre-lecteur ; non ouvert par moi** |

Une question du lot E0 a sa réponse depuis la v3 : la course v67 a joué l'étage v57, par le tour fermé v64.

## 2. D2 confrontée au § 2.2 de la note

### 2.1 La réponse de la note, lue avec son erratum 1

| | barreau 1, la course de banc | barreau 2, la course réelle appariée |
|---|---|---|
| l'organisme | un banc écrit par nous : proposeurs écrits par programme, fonctions de jugement, mondes à lois vraies et fausses plantées | l'organisme réel, vrais proposeurs, tests de mort réels dans la boucle |
| la carte y entre comme | un greffon : une fonction appelée une fois par génération, dans sa propre invocation du bac, qui ne reçoit que ce que recevait le mécanisme remplacé, jamais la vérité | le même greffon, branché |
| où cela tourne | **le banc joueur sur la machine jetable**, greffons sous identifiants opaques, sans clé ni racine des graines ; **le banc noteur chez la mère** : inventaire, contre-calcul à l'octet sans exécuter le greffon, puis compte contre la clé (E1N, § 1) | sur devis à part |
| bras, sur les mêmes graines | sans (le témoin) ; avec ; placebo de même forme ; bases bon marché du point de greffe, en liste fermée | avec et sans, mêmes mondes |
| issue | « invalide » si la carte fait promouvoir plus de lois fausses que le niveau annoncé ; « sans gain » si son écart apparié au témoin, au placebo et à la base ne passe pas le seuil de son cas, sur des familles de mondes tenues à l'écart ; sinon « tient au banc », qui n'est pas une adoption | « tient » ou « ne tient pas » |
| coût | l'expérimentateur et le lecteur témoin se paient une fois par carte ; le rejeu loue de la machine, pour une durée non mesurée | **de l'ordre de 640 à 1 430 USD par carte à cinq espèces, de 110 à 430 à deux, l'étage dans la boucle** ; produits de bornes, aucune mesure (§ 6.4) |

Quatre règles (NC, § 2.1) : aucun agent n'écrit le critère de mort ; le code d'un agent rend une décision, jamais une mesure ; l'épreuve passe d'abord ses témoins plantés ; un mort reste mort.

### 2.2 Ce que la note règle des objections de la v1

Inchangé depuis la v2, § 2.2 : l'objet servi à l'étage est une fiche écrite par l'orchestrateur ; l'étage v5 sert à écrire et sceller le greffon ; le proposeur choisit un cas et une taille, jamais l'épreuve ; le pont ne remplit que des champs fermés à extrait cité ; l'oracle passe par le comparateur sans juge du palier 0b ; les bornes de 0,06 à 0,90 USD ne valent que pour un script de loi.

### 2.3 Ce que la note tranche

**Rien** : pièce de travail non contre-lue, recommandation (a) à 0,7 sur N1, sans défaut. Je tiens sa forme d'épreuve pour base de planification, parce que la mère l'a demandé.

### 2.4 Ce qui reste ouvert

1. Le banc de la ligne 1 se rend-il greffable sans réécriture ? Non établi (NC, § 6).
2. L'étage v5 accepte-t-il la fiche écrite par l'orchestrateur ? « À confirmer sur le code. »
3. Le coût d'un greffon : de 0,14 à 4,10 USD, lecteur témoin compris ; **non mesuré**, à un facteur trente environ (§ 6.3).
4. La part des cartes par barreau et le nombre de cartes hors gabarit : le compte rendu n'en dit rien.
5. `numpy` dans le bac ; la durée d'une exécution nue.
6. **La durée du rejeu du barreau 1.** Son lieu est répondu par l'erratum 1 (§ 3.2) ; sa durée ne l'est pas.
7. **Le partage du banc en deux processus et le contre-calcul sans le greffon** sont des propositions de l'erratum 1, « à établir sur le code du banc de la ligne 1 » (E1N, § 4).
8. Les seuils de la définition scellée : les cas A et B en portent de chiffrés ; le cas C ne se lit que sur un banc à plusieurs générations (contre-lecture de la v2, § 2, point 8 ; je n'ai pas ouvert la pièce). À écrire au texte de la porte.
9. La liste fermée des points de greffe, celle des bases, et les quatre mécanismes témoins : des formes, rien d'écrit.

### 2.5 Ce qui reste à Lazar

N1, N2, N3, N4 ; D1, D6 et D8 ; le nœud du sommet unique, s'il est voulu (D5).

## 3. Ce qui manque, après la note

### 3.1 Relecture du § 2 de la v1

| v1 | v4 |
|---|---|
| l'objet de l'épreuve, les données, l'oracle, les mondes | répondu en proposition (NC, § 2.2) ; manquent le banc greffable en deux processus, les mondes, les mécanismes témoins, la table d'admission, le texte de la porte |
| sommet d'étage, enveloppe | **deux sommets** : celui de la v69, tel que son additif le fixe, pour le palier 1 ; celui d'AC-1, en fichier neuf d'AC-1, pour cette course. **Le socle commun est la couche sous le sommet** (ci-dessous). L'enveloppe du palier 0b est commune aux deux |
| le pont | pont à extrait cité, deux traducteurs, gabarit « mécanisme » |
| classes d'issue | celles d'A69, plus les motifs « invalide » et « sans gain », plus les statuts « hors gabarit » et « non éprouvée (épreuve morte) » |
| boucle à plusieurs générations, lecture | hors du premier emploi ; requis au pas 5 de la note |
| récompense de l'héritage | l'issue par tentative et son coût, rien de plus fin ; rien de servi d'ici la lecture de l'épreuve de l'héritage (NC, § 2.5) |
| les juges | pour information, jamais un choix ni un repêchage |
| lanceur, additif, préenregistrement | un lanceur de la série AC-1, qui porte la table des épreuves ; un lanceur de l'orchestrateur AC-1 ; un additif par épreuve ; un préenregistrement de la porte, si N3 l'accorde |
| le bac | trois lieux : le bac, la machine jetable, la mère ; ni clé ni vérité ni racine des graines sur la machine ; inventaire et versement scellé avant destruction |
| mesures et gardes | plus les huit gardes de NC, § 2.6, plus le contre-calcul à l'octet de l'erratum 1 |

**Le socle commun, et pourquoi il est sous le sommet.** La v3 logeait un sommet commun « dans la v69, AC-1 l'appelant sans le modifier ». L'additif scellé ne le permet pas, en quatre lieux que j'ai relus :

- A69, § 1.2 : « La v69 porte le palier 1. Son étage a un sommet neuf, écrit dans un fichier neuf de la v69 ». Ce sommet porte lui-même la tranche d'épreuve de l'héritage et l'arrêt sur tout écart du contre-calcul ; il reprend la forme imposée du tour fermé. Il est écrit pour une loi à forme imposée, non pour un greffon.
- A69, § 6, garde 10 : tout engagement hors de la forme du tour fermé est « refusée avant l'épreuve, comptée, jamais éprouvée ». Garde 11 : contre-calcul après chaque exécution, arrêt s'il diffère. Un greffon passé par ce sommet serait refusé, ou n'aurait pas de contre-calcul qui lui convienne.
- A69, § 0, point 1, et § 2, C3 : « Tout autre régime, toute autre épreuve, reste refusé en réel », et « aucune option, aucune variable d'environnement, aucun champ de configuration ne le lève ». Un paramètre « forme d'épreuve » sur ce sommet serait un tel champ.
- A69, § 8 : « Il ne touche pas la course d'auto-conception ».

Ce que ce plan appelle donc « socle commun », aligné sur la liste de l'erratum 2 (E2N, § 1) — « écrit une fois, en fichiers neufs hors de la v69, ou déjà existant et appelé sans modification » :

1. **Les maillons que l'additif fait appeler sans modification** (A69, § 1.2) : `preparer_generation` v53 ; `jouer_etage_v57` ; l'étage des tests de mort v5 ; l'adaptateur de l'étage (`AdaptateurEtageV64`) ; le contrôle des parts des relais avant l'étage (`Compteur.verifier_parts_avant_etage`). Ils existent ; aucun octet n'y change.
2. **L'enveloppe du palier 0b**, « commune aux deux usages » (A69, § 1.1).
3. **C3, en fichiers neufs hors de la v69** : le rejeu de l'implémentation scellée et **le banc joueur** — lots par graine, identifiants opaques, invocation du bac à chaque appel, journal chaîné.
4. **C2, en fichiers neufs hors de la v69** : **le banc noteur** (mesure hors machine, écriture des issues par une fonction dont les seules entrées sont l'engagement scellé, les décisions scellées, la vérité et le journal des coûts) ; **le contre-calcul** à l'octet, sans exécuter l'implémentation ; **la porte des lots** (composition par graine avec témoins, règle de l'épreuve morte, statuts) ; **le registre des tentatives** (ajout seul, chaîné, scellé, « un mort reste mort », égalité de comportement) ; **les témoins** comme mécanisme (les trois sortes, la table d'admission, les classes d'issue aux noms de l'additif, § 4).

**Le socle ne connaît aucune forme d'épreuve** : il reçoit de chaque sommet le constructeur de la fiche servie, le contrôle d'après-étage et la statistique ; il tient plusieurs générations dès l'écriture (E2N, § 2, phrase 3).

Au-dessus, **propre à chaque emploi** (E2N, § 1) : la forme d'épreuve, avec son interface, sa statistique et son texte de test imposé ; la banque de mondes et le contenu de ses témoins ; le lanceur de la course ; les gardes de la course ; le tout sous son texte et sa ligne d'accord. **Le sommet d'AC-1 s'écrit dans AC-1, en fichier neuf** — une cinquantaine de lignes, par analogie avec ce que l'additif dit du sien (A69, § 1.2) ; la v69 garde son sommet et son lanceur 11 tels que scellés. Rien n'est rouvert ; seul le sommet est écrit deux fois. Le sommet d'AC-1 ne s'allume en réel que sous son propre additif (D1). Le pilier mathématique et la course « seuil et moniteurs » écrivent chacun le leur.

**Le nœud d'un sommet unique** (déclaré, non tranché) : vouloir un seul sommet pour les deux emplois — qu'il vive dans la v69 avec un paramètre, ou dans AC-1 que la v69 appellerait plus tard — est un écart à un texte scellé (A69, § 1.2 et § 2, C3). Il est posé à D5. L'erratum 2 dit de même de la variante « le socle dans AC-1, la v69 l'appellera plus tard » : non retenue, elle « rouvrirait l'additif […], ce qui serait un nœud de Lazar ».

**Deux points de la note que l'additif heurtait, corrigés par l'erratum 2** : la table des épreuves « dans le lanceur de course 11 » (NC, § 3.1, point 6) se lit désormais « dans le lanceur propre à chaque emploi, jamais dans le lanceur 11 » ; « l'écrire une fois, la forme d'épreuve en paramètre » (NC, § 3.1, alinéa de tête et point 1) se lit « socle commun sous le sommet, un sommet par emploi » (E2N, § 2, phrases 2 à 4).

**Le lanceur.** Avec D3 inscrite, le lanceur de cette course prend un nom de la série AC-1 ; je garde la proposition de la v3, `lancer_etage_auto_conception_ac_v1.py`. La v69 refusant le moteur réel hors du palier 1 (A69, § 2, C3), il faut à AC-1 son propre lanceur de l'orchestrateur, qui lève le refus pour son seul régime.

**Manques neufs depuis la v3** : le sommet d'AC-1 ; le banc en deux processus et le contre-calcul ; la mesure de la durée du rejeu au banc d'étalonnage.

### 3.2 Le lieu du rejeu du barreau 1 — répondu par l'erratum 1

La v3 posait la question à l'auteur de la note et prenait, pour le seul devis, la lecture « rejeu chez la mère ». **L'erratum 1 répond autrement, et sa réponse prime** :

| | où | ce qui s'y trouve |
|---|---|---|
| banc joueur | la machine jetable | les greffons scellés, cartes et témoins mêlés sous identifiants opaques ; le code du banc joueur ; les épisodes et les lois candidates sans la clé ; les graines de la course, la racine restant chez la mère ; les plafonds et les délais |
| banc noteur | chez la mère | la clé, la racine des graines, la correspondance des identifiants, le critère scellé, la table d'admission, le calcul de l'issue, le registre |
| ordre chez la mère, avant de lire la clé | — | inventaire du dossier de travail contre la liste blanche ; **contre-calcul** : la part du banc joueur rejouée à partir des décisions enregistrées, sans exécuter le greffon, égalité à l'octet du reste du journal, sinon lot nul ; alors seulement le compte contre la clé |
| banc d'étalonnage | chez la mère, 0 USD | implémentations écrites par nous ; le même code en deux processus, la clé hors de portée du joueur |

Règle de partage : du code écrit par un modèle ne tourne jamais chez la mère ; la clé ne monte jamais sur la machine. Dès qu'un greffon est écrit par un modèle — les témoins passés par l'expérimentateur comme les cartes —, il va sur la machine jetable.

**Ce que cela change à ce plan.**
- Ma lecture provisoire (i) de la v3 est retirée. Le rejeu des greffons de la ligne 1 et de la ligne 2 **loue de la machine**.
- Sa durée vaut mondes × bras × générations × (temps du banc joueur + temps du greffon, borné par le délai par exécution du bac). **Elle n'est mesurée nulle part.** Première mesure au banc d'étalonnage, à 0 USD, **avant tout devis de machine** (E1N, § 1).
- N6 (a) est tenue sans exception : « chez la mère » y désigne le banc noteur.
- Le partage en deux processus et le contre-calcul sans le greffon restent des propositions, à établir sur le code du banc de la ligne 1 par E0 et E3.

### 3.3 Écarts entre l'erratum 2 de la note et ce plan

L'erratum 2 a été écrit sans lire ce plan ; ce plan a été aligné sur lui. Il reste cinq écarts ou points de lecture, aucun de fond.

1. **Le nœud du sommet unique.** L'erratum écrit « aucun nœud neuf pour Lazar » ; ce plan déclare à D5, option (c), le nœud d'un sommet unique, comme son mandat le demande. Les deux se tiennent : l'erratum ne retient pas la variante et dit lui-même qu'elle serait un nœud ; ce plan ne la recommande pas et lui refuse tout défaut. Le nœud n'existe que si quelqu'un veut un sommet unique.
2. **Où tombent le banc joueur, le banc noteur et le contre-calcul.** La note logeait le banc dans le lot E3 ; l'erratum 2 les range dans le socle. Ce plan les met donc dans C3 (banc joueur) et C2 (banc noteur, contre-calcul), et laisse à E3 ce qui est propre à cette course : les points de greffe, la banque de mondes, le contenu des témoins, l'étalonnage. **L'erratum ne redistribue pas les heures** : il donne « socle : 1 à 2 » à la ligne de C3 et ne touche ni C2 (2 à 3) ni E3 (8 à 15). Je garde les totaux et je dis que C2 et C3 sont sans doute bas, E3 sans doute haut d'autant.
3. **La table d'admission.** L'erratum range « la table d'admission » parmi les témoins du socle, et « la banque de mondes et le contenu de ses témoins » dans le propre de chaque emploi. Je lis : le mécanisme d'admission est commun, les valeurs scellées sont celles de chaque emploi (ici, par C1 et le banc d'étalonnage de E3). Lecture de moi, à confirmer par son auteur.
4. **Les heures du sommet.** L'erratum et ce plan disent la même chose : 1 à 2 heures de plus pour le sommet d'AC-1, sous hypothèse. Aucun écart.
5. **Ce que l'erratum demande d'établir sur le code** — que les pièces du socle se laissent appeler par plusieurs sommets sans réécriture — est porté ici par le lot E0 autant que par C2 et C3, pour le savoir avant d'écrire.

## 4. Les lots

### 4.1 E2 et E3 récrits

**E2 révisé — le pont à extrait cité et le gabarit « mécanisme ».** Inchangé depuis la v3.
- Contenu : la fiche à champs fermés d'une carte (point de greffe en liste fermée ; cas de la définition ; quantité, signe et taille de l'effet, sinon « lu au plus prudent ») ; le programme qui vérifie à l'octet chaque extrait cité ; la règle d'accord des deux traducteurs ; le statut « hors gabarit » ; le constructeur de la fiche servie à l'étage ; les gardes de l'entrée de l'expérimentateur.
- Dépend de : E0 ; N1 ; D8 ; E3, pour la liste fermée des points de greffe.
- Partage avec la course « seuil et moniteurs » : sa mise en forme fixe par deux traducteurs (ordre v4 scellé, `390af604…`, R-4425). **Proposition, non un fait** : un seul programme de vérification d'extrait, deux gabarits. Avec le pilier mathématique : rien du pont.

**E3 révisé — ce qui est propre à cette course sur le banc : les points de greffe, les mondes à lois plantées, les mécanismes témoins, l'étalonnage.**
- Contenu : la surface de modification du banc, un point de greffe par étage du trajet d'une carte ; les proposeurs écrits par programme et les fonctions de jugement de cette course ; le générateur de mondes à lois vraies et fausses plantées, graines dérivées par monde et par course (règle R9), racine gardée avec la vérité ; les familles tenues à l'écart ; les bras ; les quatre mécanismes témoins et leur sort attendu ; le banc d'étalonnage, joué à 0 USD chez la mère sur le banc joueur et le banc noteur du socle, le même code en deux processus, qui scelle la table d'admission **et rend la première mesure de la durée du rejeu**. **Le banc joueur, le banc noteur et le contre-calcul ne sont plus dans ce lot** : l'erratum 2 les range dans le socle (C3 et C2).
- Les témoins d'abord : aucune carte ne passe avant la table d'admission scellée ; un témoin « doit mourir » qui tient fait une épreuve morte, arrêt rapporté, jamais un repli.
- Dépend de : E0 ; N1 ; **C2 et C3**, pour l'étalonnage ; le comparateur sans juge du palier 0b ; la lecture de la définition scellée.
- Partage avec la course « seuil et moniteurs » et avec le pilier. **Proposition** : un seul module « graines, disjonction, clé scellée, famille tenue à l'écart », plusieurs générateurs ; à porter au mandat de l'auteur des mondes plantés de « seuil et moniteurs » (R-4426, R-4433).
- Heures : 8 à 15 (NC, § 3.3). **Aucun des deux errata ne rechiffre ce lot** ; voir le § 3.3, point 2.

### 4.2 La table des lots

| lot | heures | contenu | dépend de | partagé avec | premier emploi ? |
|---|---|---|---|---|---|
| E0 | 1,25 | relevé du code, sans écriture ; il lit d'abord le relevé du lot 0 de NA-1 (`10ac79ec…`) ; questions propres : le banc de la ligne 1 est-il greffable et se coupe-t-il en deux processus ; l'étage accepte-t-il la fiche écrite par l'orchestrateur ; `numpy` dans le bac ; **les maillons du socle s'appellent-ils depuis un second fichier neuf sans rien prendre au corps du sommet du tour fermé** | — | NA-1, lot 0 | oui |
| C1 | 3,5 à 39, texte, hors du code | texte de la porte pour cet emploi : gabarit, banque de témoins, critères et seuils par cas, table d'admission (classe A) | N1, N3 ; E3 | un texte par emploi | oui |
| E3 révisé | 8 à 15 | § 4.1 : le propre de cette course sur le banc, et l'étalonnage | E0 ; N1 ; C2 et C3 ; comparateur du palier 0b ; définition scellée | le module des graines, en proposition, avec le pilier et « seuil et moniteurs » | oui |
| C2 | 2 à 3 | **socle commun, fichiers neufs hors de la v69, écrits une fois** (E2N, § 1) : le banc noteur (mesure hors machine, écriture des issues) ; le contre-calcul à l'octet sans exécuter l'implémentation ; la porte des lots ; le registre des tentatives et la garde « un mort reste mort » ; le mécanisme des témoins, de la table d'admission et des classes d'issue. Il ne connaît aucune forme d'épreuve | E0 | les trois emplois | oui |
| E2 révisé | 3,75 | § 4.1 | E0 ; N1 ; D8 ; E3 | « seuil et moniteurs » | oui, pour la ligne 2 |
| **E1-v69** | **au devis d'heures du palier 1 ; aucune heure dans ce plan** | le sommet d'étage de la v69, tel que l'additif scellé le fixe : forme imposée, contre-calcul, gardes 10 et 11 | palier 0b ; l'additif | **le palier 1 seul** ; il n'est pas sur le chemin de cette course | non |
| **E1-AC** | **5,75 à 6,75** : les 4,75 de l'ancien lot E1 (sommet et enveloppe), plus 1 à 2, hypothèse | **le sommet d'étage d'AC-1, en fichier neuf d'AC-1** : il appelle les maillons du socle sans les modifier, dans l'enveloppe du palier 0b ; il apporte au socle la forme d'épreuve de cet emploi (interface du greffon, statistique, texte de test imposé), le constructeur de la fiche servie et le contrôle d'après-étage ; environ une cinquantaine de lignes ; le supplément de 1 à 2 heures est celui du contrôle (CT, § 3 ; E2N, § 2, phrase 5) | E0 ; C2 et C3 ; l'enveloppe du palier 0b ; D1 pour l'allumage | rien : propre à cet emploi | oui, pour la ligne 1 |
| C3 | 1 à 2 | **socle commun, fichiers neufs hors de la v69, écrits une fois** (E2N, § 1 et § 2, phrase 5) : le rejeu de l'implémentation scellée sur la machine jetable, une boucle sans session de modèle qui appelle l'exécuteur du bac ; le banc joueur — lots par graine, identifiants opaques, invocation du bac à chaque appel, journal chaîné. Le « paramètre de forme d'épreuve » de la v3 n'existe plus : le socle reçoit de chaque sommet ce qui lui manque et tient plusieurs générations dès l'écriture | E0 | les trois emplois | oui, pour la ligne 1 |
| E4 | 2,75 | la projection des classes dans les fichiers de la course ; compté 2,75 heures par prudence, sans doute 1 à 1,5 | C2 | palier 1 | oui, petit |
| E7 | 2,75 | mesures et export | C2 | forme de NA-1, lot 7 | oui |
| E8 | 5,5 | lanceur AC-1 et lanceur de l'orchestrateur AC-1 : table des épreuves, épinglages, parts, machine déclarée, durée de location, attestation du bac, ligne d'accord | E1-AC, C3 ; C1, pour la banque et la table d'admission ; N4, pour le rôle et sa part | A69, § 7, pour la forme de la liste seulement ; NA-1, lot 8, pour les relais | oui, pour la ligne 1 |
| E9 | 4,75 | mise en route et essai du bac, inventaire et versement avant destruction, essai à blanc de bout en bout | E7, E8 | palier 1 ; NA-1, lot 9 | oui, pour la ligne 1 |
| E5 | 4,75 | course à plusieurs générations avec étage | E1-AC, E2, E4 | base v68 | non, sauf D8 (c) |
| E6 | 3,75 | lecture du registre par la génération suivante | E4, E5 | NA-1, lot 5 | non ; D4 inscrite : rien de servi à la première course |

**Le régime du premier emploi est un régime neuf — proposition.** Inchangé depuis la v3 : pour les lignes 1 et 2, l'étage tourne sans génération de proposeurs, sur des témoins puis sur des cartes archivées. GO-2026-11-21-16 n'accorde l'étage seul qu'à la course « seuil et moniteurs ». Il faut à AC-1 son additif et le mot de Lazar : c'est D1.

**Les heures de la table.** Ce sont celles du plan v1 pour E0, E2, E4 à E9 et l'ancien E1 ; celles de la note pour E3, C1, C2 et C3 ; le supplément du contrôle pour le sommet d'AC-1. Les lots de code font de 46 à 56 heures, et de 37,5 à 47,5 sans E5 ni E6 : les totaux du § 5. C1 est un texte, compté au § 5 avec les textes. Le sommet de la v69 n'a aucune heure ici : il relève du devis d'heures du palier 1.

**Chemin critique, aux deux bornes de C1.** Le code jusqu'au premier dollar (E0, E1-AC, C3, E8, E9) fait de 18,25 à 20,25 heures, le sommet d'AC-1 compris : 1,25 + 5,75 + 1 + 5,5 + 4,75 = 18,25, et 1,25 + 6,75 + 2 + 5,5 + 4,75 = 20,25. Le sommet dépendant désormais de tout le socle, C2 (2 à 3 heures) rejoint ce chemin, que la v3 n'y comptait pas : de 20,25 à 23,25 heures. Si C1 reste à sa borne basse (3,5 heures), c'est ce code qui est critique. Si C1 approche sa borne haute (39 heures), c'est le texte. E8 dépendant de C1, le lanceur ne se fige dans aucun cas avant la table d'admission. **Le sommet de la v69 n'est plus sur ce chemin** : cette course ne l'attend pas.

**Ordre.** À 0 USD : E0 ; le socle, C2 et C3 ; E3 et le brouillon de C1 ; table d'admission scellée et première mesure de la durée du rejeu ; premier compte des cartes (fait : § 7.3). C'est un changement d'ordre depuis la v3, qui écrivait E3 avant C2 : l'étalonnage de E3 joue sur le banc du socle. Pour la ligne 1 : E1-AC ; E8 et E9 ; additif, devis, ligne, N4. Pour la ligne 2 : D8, E2, second devis. E5 et E6 après.

**Ce qui s'écrit une fois, ce qui s'écrit deux fois.** Une fois : les maillons (déjà écrits), l'enveloppe, C2, C3, le module des graines si la proposition du § 4.1 est retenue. Une fois par emploi : le sommet d'étage, une cinquantaine de lignes, et le lanceur, chacun dans sa version, avec son texte et sa ligne d'accord (E2N, § 1).

## 5. Le calendrier

Heures de session, sans appel.

| | v3 | v4 |
|---|---|---|
| code et vérification | 45 à 54 | **46 à 56** (le sommet d'AC-1 : 1 à 2 heures de plus, hypothèse) |
| dont premier emploi, sans E5 ni E6 | 36,5 à 45,5 | **37,5 à 47,5** |
| textes, hors porte | 20, estimation non revue | 20, **estimation non revue** |
| C1, texte de la porte | 3,5 à 39 | 3,5 à 39 |
| **textes** | 23,5 à 59 | **23,5 à 59** |
| **somme** | 68,5 à 113 | **69,5 à 115** |

Avec le supplément de 6 à 10 heures de textes que la v3 posait en hypothèse : textes 29,5 à 69, somme **75,5 à 125**.

**Ce que ces heures ne comptent pas** : le partage du banc en deux processus et le contre-calcul à l'octet (E3, C2 et C3 gardent les heures de la note ; l'erratum 2 redit « socle : 1 à 2 » pour la ligne de C3 et ne redistribue rien entre E3, C2 et C3 : § 3.3, point 2) ; un additif propre au sommet d'AC-1, compté dans les textes « non revus ».

**L'ordre du compte et de la mesure.** La proposition de la v3 est retenue par la mère comme conforme à la lettre de la note (CT, § 6, (a)) : le devis de la ligne 1 ne dépend d'aucune carte et peut partir sans le compte ; le compte précède le devis de la ligne 2. Le premier compte par la voie (d) est fait.

**Horloge, au plus tôt, sous condition du mot de Lazar sur l'ordre des pilotes.**
- Table d'admission scellée et durée du rejeu mesurée, à 0 USD : trois à quatre jours après le mot sur N1.
- Ligne 1 : il faut en plus le sommet d'AC-1, les lanceurs AC-1, le bac, un additif, un devis contre-lu, une ligne, N4, et D1 pour le régime neuf. Pas avant le 28 novembre.
- Ligne 2, une seconde dépense, sur un second devis : après la mesure, après D8, après le compte de nature.

**Ce que je ne peux pas dater** : les nœuds ; la lecture du palier 0b ; la place du modèle F, que NA-1 occupe pour 48 à 60 heures, avec le pilier et la course « seuil et moniteurs ».

## 6. Le devis du bac et des appels

### 6.1 Ce qui est lu

| valeur | source | nature |
|---|---|---|
| 0,0675 à 0,0733 USD de l'heure | F68, décision 4 | relevé du 11 ou du 12 novembre, non revérifié |
| 0,28 USD de l'heure ; borne haute du programme 1,30 | DM, l. 15, sous la réserve de la mère | observé le 12 novembre ; borne écrite |
| course v67 : 14 tests en 45,5 minutes, soit 3,25 minutes par test | verdict de la v67 | mesuré |
| expérimentateur à la v67 : au plus 0,081 USD par test | NC, § 1 | mesuré, appels de proposeur compris, pour un script de loi |
| **lecteur témoin : 0,061 USD par test** | E1N, § 2 : 0,85618 USD pour 16 appels, divisé par 14 | **borne haute ; relevé d'une seule course, sur un seul modèle ; pas une mesure neuve** |
| plafond par défaut de la session du lecteur témoin : 0,10 USD, « supposé » | E1N, § 2 ; CT, pièces contrôlées | borne écrite dans le code |
| plafond d'une formalisation dans un autre brouillon : 4 USD par item | NC, § 2.2 | non mesuré |
| une génération d'un bras, propositions seules : 58,64 USD à cinq espèces, 8,92 à deux | E1N, § 2, (d), d'après le devis de l'héritage v5 | hypothèse du devis, non mesurée |
| tentatives par génération au régime du palier 1 : 94 à cinq espèces, 38 à deux | E1N, § 2, (d) | du devis ; **ce 94 n'est pas le nombre de cartes de la course v9** |

### 6.2 Machine : deux lignes séparées, hors rejeu du banc joueur

**Ligne 1 — la mesure sur les seuls témoins (première dépense).**

| cas | hypothèses | heures | à 0,0733 | à 0,28 | à 1,30 |
|---|---|---|---|---|---|
| bas | 4 témoins au rythme de la v67 ; une heure de mise en route et d'essai du bac | 2 | 0,15 | 0,56 | 2,60 |
| haut | 12 témoins, 9 minutes chacun ; deux heures de mise en route | 4 | 0,29 | 1,12 | 5,20 |
| pire | la durée maximale de cette ligne atteinte | 12 | 0,88 | 3,36 | 15,60 |

Plafond proposé : 5 USD, durée maximale 12 heures. Il tient jusqu'à 0,41 USD de l'heure.

**Ligne 2 — les cartes, après D8, second devis.** La borne du devis est 94 cartes.

| cas | hypothèses | heures | à 0,0733 | à 0,28 | à 1,30 |
|---|---|---|---|---|---|
| bas | 94 cartes au plus, au rythme de la v67 ; une heure de mise en route | 7 | 0,51 | 1,96 | 9,10 |
| haut | 94 cartes au plus, 9 minutes chacune ; 8 heures d'exécutions de mise au point ; 2 heures de mise en route | 25 | 1,83 | 7,00 | 32,50 |
| pire | la durée maximale atteinte | 48 | 3,52 | 13,44 | 62,40 |

Plafond proposé : 15 USD, durée maximale 48 heures. Il tient jusqu'à 0,31 USD de l'heure. Les deux lignes font 20 USD au plus. À 92 cartes, les cas bas et haut descendent à 6 et 24 heures ; je garde 94, qui est la borne.

**Ce que ces deux tableaux ne comptent pas, et qui change depuis la v3.** Ils comptent l'étage — l'expérimentateur écrit le greffon, le bac l'exécute et le scelle. **Ils ne comptent pas le rejeu par le banc joueur**, que l'erratum 1 place sur la machine jetable pour tout greffon écrit par un modèle, aux deux lignes. Sa durée — mondes × bras × générations × (temps du banc joueur + temps du greffon, borné par le délai par exécution) — n'est mesurée nulle part : ni le nombre de mondes, ni le nombre de générations du banc, ni le délai ne sont gelés. **Les heures ci-dessus sont donc des planchers, et les deux plafonds de machine ne sont pas établis.** Ils se refont après la première mesure au banc d'étalonnage, à 0 USD, que l'erratum 1 place « avant tout devis de machine ». Quatre et douze témoins, huit heures de mise au point, douze et quarante-huit heures de durée maximale restent mes hypothèses, reprises de la v3.

### 6.3 Appels : ce qui n'est mesuré nulle part

| poste | borne basse | borne haute | nature |
|---|---|---|---|
| un greffon, expérimentateur seul | 0,081 USD | 4 USD | relevé d'un script de loi ; plafond d'un autre brouillon |
| le lecteur témoin, par greffon | 0,061 USD | 0,10 USD | relevé de la v67, borne haute ; plafond par défaut « supposé » |
| **un greffon, lecteur compris** | **0,14 USD** (0,142) | **4,10 USD** | un facteur trente environ entre les deux (29) |
| **ligne 1 : nombre de greffons témoins × cette fourchette** | 4 témoins : 0,57 USD ; 12 témoins : 1,70 USD | 4 témoins : 16,40 USD ; 12 témoins : 49,20 USD | plus la machine (§ 6.2) ; le nombre de témoins est mon hypothèse, la note en nomme quatre formes |
| ligne 2, 94 cartes au plus (borne du devis) | 13,35 USD | 385,40 USD | moins les cartes hors gabarit et celles déjà sous un texte scellé |
| ligne 2, 92 cartes au plus (voie (d) de D8) | 13,06 USD | 377,20 USD | même réserve |
| les deux traducteurs, deux appels par carte | — | — | **non chiffrés**, ni par la note, ni par son erratum, ni ici |

**Le lecteur témoin** est gardé : l'étage v5, « sans un octet changé », le joue ; il ne pèse sur aucune issue ; le retirer serait une décision de Lazar et un écart à écrire au texte scellé de la course (E1N, § 2 et § 3). Je ne le propose pas. Avec lui, la borne basse monte d'environ 75 %.

**Ce qui n'est mesuré nulle part, dit en une fois** : le coût d'un greffon (0,081 est le relevé d'un script de loi, 4 le plafond d'un autre brouillon) ; le coût du lecteur sur un greffon (0,061 est le relevé d'une course, d'un modèle, sur une loi) ; les deux traducteurs ; la durée du rejeu ; le nombre de témoins ; la part des cartes hors gabarit ; tout le barreau 2.

### 6.4 Le barreau 2, avec l'étage dans la boucle

Dix générations de bras par carte (cinq paires au moins pour un test exact unilatéral à 5 %). Aux propositions seules s'ajoute l'étage, toute tentative étant éprouvée au régime du palier 1 (E1N, § 2, (d)).

| par carte, dix générations | cinq espèces | deux espèces |
|---|---|---|
| propositions seules (devis de l'héritage, hypothèse) | 586 USD | 89 USD |
| étage à 0,06 USD la tentative, un tour, sans lecteur | 56 | 23 |
| étage à 0,142, relevé de la v67, lecteur compris | 133 | 54 |
| étage à 0,60, plafonds par défaut, lecteur compris | 564 | 228 |
| étage à 0,90, borne du tour fermé, lecteur compris | 846 | 342 |
| **la carte, propositions et étage** | **de l'ordre de 640 à 1 430 USD** (643, 720, 1 150, 1 432) | **de l'ordre de 110 à 430 USD** (112, 143, 317, 431) |
| si les bras gardent l'aiguilleur et les deux juges à modèle | 139 de plus | 55 de plus |

L'erratum écrit 642 à la borne basse à cinq espèces ; mon recalcul donne 642,80, soit 643 à l'unité : un écart d'une unité, sans effet sur l'ordre de grandeur. Aucun de ces montants n'est mesuré. Si les deux bras tournaient sans l'étage dans la boucle, ce poste disparaîtrait ; c'est un choix du texte scellé du barreau 2, que ni l'erratum ni ce plan ne font. Sur devis à part, après les issues du banc.

**Lecture.** La location reste petite devant les appels tant que le rejeu n'est pas mesuré ; elle peut cesser de l'être. La ligne 1 est petite et bornée par le nombre de témoins ; elle donne le chiffre sans lequel aucun devis de la ligne 2 n'est honnête. Le barreau 2 vaut de une à deux fois et demie ce que la v3 en disait à cinq espèces.

## 7. Les décisions

Aucun défaut pour une dépense. Aucune n'est prise ici.

### 7.1 Nœuds de Lazar posés par la note — inchangés

L'erratum 1 ne change ni leurs options, ni leurs recommandations, ni leurs confiances, ni leurs défauts (E1N, § 3).

| nœud | décision | recommandation de la note | défaut |
|---|---|---|---|
| N1 | ce qu'un test de mort éprouve sur une carte : (a) course appariée à deux barreaux, pont pour les cartes de la v9 ; (b) course réelle seulement ; (c) engagement écrit par le proposeur | (a), 0,7 | aucun |
| N2 | champs de fiche des courses suivantes, qui rouvre 3a : (a) trois champs fermés de plus ; (b) inchangés | (a) pour la suite, (b) pour les cartes de la v9 ; 0,65 | aucun |
| N3 | un seul texte scellé pour la porte commune, ou un texte par ligne | le texte unique pour les cartes sans texte scellé ; 0,6 | aucun |
| N4 | modèle et plafond de l'expérimentateur d'épreuve : (a) une autre lignée que le lecteur témoin, nommée par Lazar ; (b) attendre celui de la v67 ; (c) deux lignées partout | (a), 0,6 | aucun |
| N5 | règle de l'épreuve morte | (a), 0,65 | (a) sous 48 heures |
| N6 | où se calcule l'issue : (a) chez la mère ; (b) sur la machine | (a), 0,8 | (a) sous 48 heures |
| N7 | ordre au pilier mathématique | (a), les épreuves d'abord ; 0,75 | (a) sous 48 heures pour la conception |

- N1 : la v3 appuyait (a) à 0,65 ; je ne change pas cet avis. Le prix de l'option (b), que la note donne « de l'ordre de 590 USD par carte », se lit désormais de 640 à 1 430 USD (§ 6.4) : cela renforce (a) sans changer le nœud.
- N4 : la mère recommande à Lazar un modèle du premier relais comme expérimentateur. Ce n'est pas accordé. E8 et le devis de la ligne 1 en dépendent.
- N6 : rendue exacte par l'erratum 1 (§ 3.2).

### 7.2 Décisions posées par ce plan

**D1 — Étendre le régime « tests de mort réels » à la course principale, sous sa variante sans génération.** Inchangée depuis la v3, avec une précision.
- Décision : le régime s'étend-il à la course principale, et couvre-t-il un étage joué sans génération de proposeurs, sur des témoins puis sur des cartes archivées ?
- Enjeu : A69 lie l'allumage au seul palier 1 ; GO-2026-11-21-16 n'accorde l'étage seul qu'à la course « seuil et moniteurs » ; le lanceur v10 refuse « les tests de mort seuls ». Sans un mot qui nomme cette variante, les lignes 1 et 2 ne peuvent pas s'allumer.
- Options : (a) oui, variante nommée, sous un additif propre à AC-1, **qui porte aussi le sommet d'étage d'AC-1 et ses gardes** ; écriture en routine, allumage sur devis et ligne. Avantage : suit la priorité dite ; ouvre la mesure sur les témoins ; ne touche pas à l'additif de la v69. Inconvénient : un régime de plus avant qu'aucun n'ait tourné. (b) oui pour la course à générations seulement, après le palier 1. Avantage : un seul régime neuf à la fois. Inconvénient : ferme les lignes 1 et 2, donc D6 (a). (c) non.
- Recommandation : (a), confiance 0,7. Aucun défaut.

**D3 — Nom de version : inscrite.** « AC-1 » (R-4394).

**D4 — Ce que lit la génération suivante : inscrite.** Rien de servi à la première course (R-4394).

**D6 — La première dépense de ce branchement.** Inchangée depuis la v3, aux chiffres près.
- Décision : quelle dépense demande-t-on d'abord à Lazar pour cette course ?
- Enjeu : aucun coût de greffon n'est mesuré, à un facteur trente environ, lecteur témoin compris ; sans cette mesure, tout devis des cartes est une fourchette de 13 à 385 USD.
- Options : (a) la mesure de l'expérimentateur sur les seuls témoins, sur la machine jetable : ligne 1 du § 6, bornée par le nombre de témoins multiplié par le plafond par greffon. Avantage : petite, bornée, rend le premier chiffre réel et une première lecture de fidélité. Inconvénient : demande le sommet d'AC-1, le bac et N4 ; son plafond de machine attend la mesure du rejeu. (b) attendre la mesure du palier 1. Avantage : rien à écrire pour cette course d'ici là. Inconvénient : le palier 1 mesure un script de loi, non un greffon. (c) un devis des cartes sur les bornes, avec un plafond d'arrêt. Avantage : une seule ligne. Inconvénient : dépense à l'aveugle, contre la note.
- Recommandation : (a), confiance 0,65. **Aucun défaut.**

**D5 — Le lieu du socle commun, l'ordre des écritures et le premier allumage.** Récrite.
- Décision : qu'est-ce qui s'écrit une fois pour le palier 1 et pour cette course, où, dans quel ordre, et laquelle s'allume d'abord ?
- Enjeu : l'additif scellé de la v69 fixe un sommet d'étage propre au palier 1 et refuse toute autre épreuve en réel (§ 3.1) ; D6 (a) allume cette course avant le palier 1 ; la place du modèle F est unique.
- Options.
  - **(a) Le socle commun est la couche sous le sommet ; deux sommets.** Socle : les maillons que l'additif fait appeler sans modification (`preparer_generation` v53, `jouer_etage_v57`, l'étage v5, l'adaptateur de l'étage, le compteur des parts), l'enveloppe du palier 0b, et C2 et C3 en fichiers neufs hors de la v69, écrits une fois (banc joueur, banc noteur, contre-calcul, porte des lots, registre, mécanisme des témoins : E2N, § 1). AC-1 écrit son propre sommet d'étage et son propre lanceur, dans AC-1 ; la v69 garde son sommet et son lanceur 11 tels que scellés. Le banc et la porte s'écrivent en même temps, à 0 USD. **Le premier allumage est la ligne 1 de cette course** ; le palier 1 s'allume sur le même socle dès son préenregistrement court, par son propre sommet ; NA-1 sur l'autre file. Avantage : rien de scellé n'est rouvert ; cohérent avec D6 (a) ; cette course n'attend pas le sommet de la v69. Inconvénient : une cinquantaine de lignes écrites deux fois, 1 à 2 heures de plus ; deux sommets à contre-lire ; le socle est éprouvé d'abord par une forme d'épreuve neuve.
  - (b) Le palier 1 s'allume d'abord, cette course ensuite, sur le même partage. Avantage : le socle est éprouvé sur la forme imposée, déjà jouée. Inconvénient : contredit D6 (a) ; ne vaut que si Lazar retient D6 (b).
  - (c) **Un sommet unique pour les deux emplois** — paramétré dans la v69, ou écrit dans AC-1 et appelé plus tard par la v69. Avantage : un seul sommet à écrire et à contre-lire. Inconvénient : **écart à un texte scellé** (A69, § 1.2 et § 2, C3) ; il faut un additif neuf de la v69, sa chaîne complète et le mot de Lazar.
- Recommandation : (a), confiance 0,7.
- **Nœud déclaré, non tranché** : l'option (c) est un nœud de Lazar (écart à un préenregistrement scellé). Elle n'a aucun défaut et ne se prend pas par le silence. Elle n'est requise que si l'on tient à un sommet unique.
- **Défaut sous 48 heures, compté à partir du texte de la v4, que cette v5 recopie sans le changer, et non de la v3 ni de la v1** : (a), pour le lieu du socle et l'ordre des écritures seulement. Le défaut de la v3 ne doit pas courir : son texte faisait écrire le socle dans la v69. Aucun allumage n'a de défaut.
- L'option (a) est celle que l'erratum 2 de la note écrit (`12c60349…`, § 1) ; il ne retient pas la variante de l'option (c) et la dit nœud de Lazar si elle était voulue. L'erratum est une pièce de travail non contre-lue : il ne tranche pas D5.

**D7 — Le préenregistrement.** Inchangée depuis la v3 : un texte neuf de la course pour les courses suivantes, plutôt qu'un additif au v2 scellé ; confiance 0,75 ; aucun défaut ; requis seulement au pas 5 de la note.

### 7.3 D8 — Le compte des cartes et leur passage aux traducteurs (nœud de Lazar)

- **Décision** : par quelle voie obtient-on le compte des cartes de la course v9 par nature (celles qui changent l'épreuve, une règle de l'orchestrateur, la conduite de modèles, celles hors gabarit), puis leur mise en forme fixe ?
- **Enjeu** : la note demande ce compte avant tout devis des cartes. Les cartes sont sous `archives-reponses-modeles/`. Les exceptions accordées à ce dossier sont bornées, et je les cite à la lettre :
  - GO-2026-11-20-15 : un agent neuf, « qui ne lit aucune carte », lit un seul journal par un programme écrit par la mère et « ne rend que les identifiants des cartes et les comptes » ;
  - GO-2026-11-20-28 : un agent neuf, qui ne lit aucune carte, lit par un programme contre-lu « les seuls noms de clés » d'un seul fichier ; le programme rend des noms et des comptes, « sans valeur ni identifiant ».
  Ce que la note demande va plus loin sur deux points : un compte de nature ne sort d'aucun programme seul ; les deux traducteurs reçoivent chaque carte entière, ce qui est une seconde exception et une dépense.
- **Options.**
  - **(d) Le premier compte tiré des pièces déjà sur `main`, sans rouvrir le dossier — fait.** Un développeur neuf l'a rendu (rapport `9e410b09…`, sortie `9515bae3…`, programme joué deux fois à l'octet) : 94 cartes à passeport = 2 exclues + 58 au plancher ou au-dessus, en treize lignes après fusion, + 34 sous le plancher ; mentions de modules : 42 pour les tests de mort, 34 pour les témoins plantés, 31 pour les proposeurs.
    - **Ce que ce compte est : une borne pour le devis de la ligne 2.**
    - **Ce qu'il n'est pas : le compte de la note.** Les mentions se recouvrent (les trois font 107, les treize modules 339) ; une mention n'est pas un changement ; rien n'y classe une carte par nature ni par barreau ; la base de la ligne des mentions (94 ou 96) n'y est pas écrite. Aucune carte ne passe sur sa foi.
    - **La borne, chiffrée : 92 cartes au plus**, les 2 exclues retranchées, avant de retrancher les cartes déjà sous un texte scellé.
    - **Les cartes déjà sous un texte scellé, comptées par identifiant.** GO-2026-11-19-55 nomme cinq cartes porteuses, une par ligne retenue ; GO-2026-11-19-56 en nomme six, dont deux « et ses fusionnées ». Soit **onze identifiants nommés**. La note tient pour déjà engagées les lignes 1 et 3 et l'héritage (NC, § 4.1) : les lignes 1 et 3 ont deux cartes porteuses nommées ; l'héritage est une question, sans identifiant de carte dans ces lignes. D'où : **90 au plus** si seules ces deux porteuses sortent ; **81 au plus** le jour où les onze lignes nommées auront toutes leur texte scellé. Trois réserves : les cartes fusionnées derrière une porteuse ne sont dénombrées par aucune des deux lignes d'accord ; je suppose, sans l'avoir vérifié, que les onze identifiants sont parmi les 94 ; je n'ai pas lu quelles lignes ont aujourd'hui un texte scellé (l'ordre de passage v3 n'est pas dans mes pièces). GO-2026-11-19-57 et -59 ajoutent d'autres lignes, que je n'ai pas comptées.
    - Avantage : aucune exception, aucune dépense. Inconvénient : une borne, non un compte.
  - **(a) Le modèle accordé, par un agent neuf qui ne lit aucune carte et un programme contre-lu ; la mère n'y entre pas.** La v4 écrivait que cette option étend le modèle de GO-2026-11-20-15 et de GO-2026-11-20-28 sur deux points : (1) des valeurs par identifiant ; (2) des mots cherchés dans un champ libre. Le relevé de la mère en retire un.
    - **Les dix champs d'une fiche**, lus dans la configuration scellée des juges (`configuration-course-auto-conception-v5.json`, `3f662ee8…`, clé `champs_fiche`) : `titre`, `axe`, `module_change`, `mecanisme`, `plus_proche_voisin`, `ce_qui_distingue`, `epreuve_monde_plante`, `cout`, `ce_qui_la_refuterait`, `limites`.
    - **La configuration ne déclare aucune liste de valeurs.** « Fermé » veut dire ici une liste fermée de noms de champs, non une valeur prise dans une liste fermée. **Le point (1), « valeurs par identifiant », tombe** : aucun des dix champs n'a de valeur fermée à rendre.
    - Il reste deux branches, que ce plan ne tranche pas.
      - **(a1) Les seuls noms de champs et des comptes.** C'est, à peu près, ce que GO-2026-11-20-28 a déjà rendu (les noms hors des dix champs, avec le nombre de cartes qui portent chacun). Avantage : tient la règle « sans aucune valeur ». Inconvénient : n'apporte presque rien de plus, et rien vers un compte de nature.
      - **(a2) La recherche de mots d'une liste scellée d'avance dans `module_change`.** Le programme **lit la valeur d'un champ libre**, même s'il ne rend que la présence des mots, par identifiant. **Ce n'est donc pas « sans aucune valeur »** : c'est la seconde extension, qui demeure, et elle rend en plus un résultat par identifiant, ce que GO-2026-11-20-28 ne fait pas. Avantage : aucune carte lue par un agent ; un compte par mots, plus fin que (d). Inconvénient : une extension d'exception, à accorder par Lazar ; encore loin d'un compte de nature, une mention n'étant pas un changement.
    - **À dire tel quel à Lazar** : si l'on tient la règle « sans aucune valeur », (a) se réduit à (a1), qui ne vaut guère mieux que ce qui est déjà rendu ; (a) ne garde de substance que par (a2), qui lit une valeur.
  - **(b) Les deux traducteurs lisent les cartes entières** et rendent les fiches à champs fermés, à extrait cité vérifié par programme ; le compte de nature sort des fiches. Avantage : le seul compte que la note demande ; il sert aussi le pas 4. Inconvénient : seconde exception, plus large que toutes les précédentes ; dépense non chiffrée ; à ne demander qu'après la ligne 1 et sur un devis.
  - **(c) Ne passer aucune carte de la v9.** Avantage : rien ne s'ouvre. Inconvénient : le premier emploi se réduit à la mesure sur les témoins ; E5 et E6 reviennent sur le chemin critique, avec N2, D7 et un texte neuf de la course.
- **Recommandation** : (d), faite ; puis (a), dans sa branche (a2) si Lazar accorde la lecture d'une valeur par programme, avec le devis de la ligne 2 ; puis (b) seulement si Lazar l'accorde après la mesure ; confiance 0,6.
- **Défaut** : aucun. (d) n'ouvrait rien et ne dépensait rien : routine, accomplie. (a), (b) et (c) sont le nœud.

## 8. Le pilier mathématique

Inchangé depuis la v3, à une ligne près. Sous la réserve de la mère sur PM et DM.

**Ce que ce plan lui emprunte** : la règle « une proposition qui meurt reste morte », avec sa proposition « même fiche, même greffon, une seule tentative », adressée au rédacteur de C1 et que la note ne porte pas ; le tarif et la minuterie de sa machine ; la forme « l'expérimentateur à modèle ne tue pas : mesuré, pas cru ».

**Ce que ce plan lui doit** : C2 et C3, du socle commun ; le module des graines et des clés, si la proposition du § 4.1 est retenue. **Il ne lui doit plus un « sommet d'étage paramétré »** : le pilier écrit son sommet et son lanceur, « du même ordre, sous hypothèse » (E2N, § 2, phrase 5).

Les trois écarts de la v2 entre le plan du pilier et la note : deux traités par l'erratum 1 du plan du pilier (R-4431) ; le troisième attend le mot de Lazar sur l'ordre des pilotes.

## 9. Réserves du planificateur

1. **Ni la note ni ses deux errata ne sont contre-lus.** L'erratum 1 dit lui-même que le partage du banc et le contre-calcul sans le greffon sont des propositions, et que ses chiffres sont des produits de bornes.
2. **L'erratum 2 est arrivé pendant l'écriture** ; ce plan a d'abord été écrit sans lui, puis aligné. Il dit lui-même que l'appel du socle par plusieurs sommets sans réécriture est à établir sur le code. Les cinq écarts ou points de lecture sont au § 3.3.
3. **PM et DM** portent la réserve de la mère.
4. **Je n'ai ouvert** ni le relevé du lot 0 de NA-1, ni l'ordre v4 de « seuil et moniteurs », ni le mandat de ses mondes, ni la définition scellée, ni le banc de la ligne 1, ni le code du palier 0b, ni l'erratum du pilier, ni l'ordre de passage v3, ni la configuration de la course v9, ni les plans v1 et v2. Je n'ai lu aucun code : « une cinquantaine de lignes » et « 1 à 2 heures » pour le sommet d'AC-1 viennent de l'additif par analogie et du contrôle.
5. **Aucun contenu de carte n'est repris ici.** Je n'ai rien ouvert sous `archives-reponses-modeles/`. De la lecture descriptive de la course v9, je n'ai lu que la ligne 99.
6. **Les heures et les cas sont des estimations** ; le nombre de témoins, les heures de mise au point et les durées maximales sont des hypothèses reprises de la v3. Les deux plafonds de machine ne sont pas établis tant que la durée du rejeu n'est pas mesurée.
7. **Le nombre de cartes déjà sous un texte scellé** n'est borné que par les identifiants de deux lignes d'accord ; les fusionnées ne sont pas dénombrées.
8. **Les dix champs de D8 (a) sont nommés d'après le relevé de la mère**, que le contre-lecteur a vérifié sur la configuration (`3f662ee8…`, clé `champs_fiche`) ; je n'ai pas ouvert cette pièce. Aucun n'a de valeur fermée : le point « valeurs par identifiant » est tombé, et la branche (a2) lit une valeur, ce qui est dit à D8.

— planificateur du plan v4, auteur de la v5, modèle F
