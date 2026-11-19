# Le juge et la sélection des cartes écartées (Astra, Carbon) — note de conception — v2

- **Statut : note de conception, version 2, à vérifier par un modèle O.** Écrite par un rédacteur neuf (modèle F), sur mandat de la mère, le 2026-11-19 (`date -u` : 2026-11-19T13:53:51Z). Pièce de travail. Processeur seul, aucune dépense, aucun appel de modèle. **Ce texte propose ; la mère soumet à Lazar.**
- **Remplace** `note-conception-juge-selection-cartes-ecartees-v1.md` (sha256 `3b0332a144db9a042632ea0549d11a72f3acd406d8aa7ea98561b25f78c95b43`), qui reste archivée. **Applique** les douze constats de `contre-lecture-note-conception-juge-selection-cartes-ecartees-v1-v1.md` (sha256 `6214b44d56c6cb8dd4221be09ff2fd5c4f50c07f36fb352501544f315d3fd2ba`) : tableau au § 8.
- **Mandats.** GO-2026-11-19-65 (R-3845), lu sur `main` : comparer trois voies, sans dépense. GO-2026-11-19-68, point 4 (R-3852), lu sur `main` : droit de veto, critères à réécrire.
- **Mots de Lazar, verbatim.** GO-65 : « il faut que le juge puisse selectionner les cartes du type d'astra qui ont ete ecartees , idem celles de carbon » ; « peut etre mettre un consortium de juges qui votent, un de chaque modele ? » ; « ou bine plus de juges astra pour reequilibrer le biais negatif de notre juge envers astra ? ». GO-68 : « deux ou trois cartes veto par juge » ; « le probleme est donc les criteres de selection qui sont trop severes pour astra et carbon et les eliminent ». Principe : « ce sont les essais avec experiences qui doivent trancher in fine les cartes et les tetss de mort ».
- **Lu** : la note v1 et sa contre-lecture ; sur `main` (commits `0cf9ac92` puis `18936bdb`), empreintes recalculées, les critères v1 (`8881dbb2…`), la proposition (`a2cd45ad…`), sa contre-lecture (`a923cb57…`), les lignes GO-2026-11-19-55 à -68 de `registres/go.md`, R-3850 à R-3852 de `registres/decisions.md`. Les autres pièces du tableau du § 2 sont citées d'après la note v1 et sa contre-lecture, qui en ont toutes deux recalculé les empreintes ; je ne les ai pas rouvertes.
- **Non lus** : aucune carte, aucun verdict de juge, le classement, le coffre. Tous les comptes cités viennent de pièces déjà versées.
- **Pièce jointe** : `criteres-choix-cartes-v9-v2.md` (sha256 `4ae09b15e2816fcda0ba0ba008ca11b58906d7712351253d04f52214e9a629c1`, commit `14e9954d`), les critères de sélection réécrits, scellés avant toute lecture de carte.

## 1. Verdict

Les cartes d'Astra et de Carbon n'ont pas été écartées par un juge : elles l'ont été par l'application de la règle de choix (plancher, nombre visé de cinq lignes, départage), écrite avant l'ouverture et appliquée sans le champ de l'espèce — masque imparfait, le style d'Astra se reconnaît (`2af9e67f…`, limite 2) —, avec deux erreurs de lecture relevées par la contre-lecture sur des lignes portées par Astra, puis par le choix de GO-2026-11-19-56 parmi les écartées de justesse. Le critère C2 à zéro n'explique que six cartes d'Astra, sur une seule lecture ; le coût explique surtout Carbon.
Aucune mesure ne montre un juge défavorable à Astra ; le seul compte disponible va dans l'autre sens, et il n'est qu'en partie confondu avec l'absence de citation.
Lazar a tranché la cause (GO-2026-11-19-68 : les critères de sélection) : les critères sont réécrits (pièce jointe), le veto contre l'élimination y entre, et je recommande trois cartes par titulaire tant qu'ils sont trois au plus, deux au-delà.

## 2. Faits établis sur les pièces

Dossier `docs/notes/organisme-auto-conception-v1/course-v2/` sauf mention.

| pièce | sha256 | ce qu'elle établit |
|---|---|---|
| `criteres-choix-cartes-v9-v1.md` | `8881dbb2f63bdfedba34c971e5fb7081fc244ab5c3555307482589b84d837326` | § 0 : ni le verdict des juges ni l'espèce ne sont des critères ; § 2 : le critère C2 ne note que cinq questions du programme (0 si aucun lien) ; le critère C3 note le coût (0 au-delà de 75 dollars ou de plusieurs générations) ; § 3 : plancher C2 ≥ 1 et total ≥ 7, nombre visé de cinq lignes ; § 4 : dernier recours du départage, l'ordre alphabétique de l'identifiant |
| `proposition-cartes-a-eprouver-v9-v1.md` | `a2cd45adf7c49a909ad14be378b75b3233eae198b7f51cc416450f4cd878d856` | cartes lues sans le champ de l'espèce ; 34 cartes sous le plancher, « presque toutes par le coût […] joint à un lien de biais ou nul avec les cinq questions » (§ 2) ; cinq lignes à 8 départagées pour le cinquième rang, par C3, par C5, par les voisins non lus, puis par l'ordre alphabétique (§ 2) ; écart 2 : les instruments tombent « par construction de mes cinq questions » (§ 6) |
| `contre-lecture-proposition-cartes-v9-v1.md` | `a923cb57702a055d7c0460c990e5ecff5dd6125c1f0c0460cedba67de606fc43` | critères commis avant la proposition, cartes lues sans l'espèce (§ 7) ; conclusion « À refaire pour le classement et la décision » ; **majeure M9** : l'interprète de référence (`fd81c25c080e8`) vaut 9 et non 8 à la lettre de la question (c), et entrait alors dans les cinq ; les certificats de portée (`f1675a6c453a9`) sont au plancher et ont été « rangés sous le plancher sans un mot » ; mineure 3 : l'écart 2 est un jugement, non un défaut du critère |
| `especes-et-originalite-cartes-v9-v1.md` | `2af9e67fce5b8edb3a3cc197347ab35f08e5f1731f5dcc3b3ef11c1fc6c44beb` | part des cartes **dans les neuf lignes retenues par GO-2026-11-19-55 et -56** (ce ne sont pas les neuf premières par la note : les rangs 6 et 8, portés par Astra, n'y sont pas) : Astra 3 sur 20, Carbon 11 sur 16, Opus 13 sur 22, Argon 8 sur 21, Fable 5 sur 15 ; 13 des 18 cartes « originales » sont d'Astra ; une question neuve vaut zéro à C2 par construction : raison donnée pour les six cartes originales d'Astra « non nommées » (§ c). Une seule lecture, sans contre-lecture ; le masque d'espèce « n'a pas tenu » (limites 2 et 4) |
| `cartes-reexaminees-cout-non-limitant-v9-v1.md` et son erratum 1 | `de7ed04d06903c507ace3a16130fccf9f22d88e6e16143c3f8f3e0530837d063` ; `9326ffa2…` (erratum, R-3837, cité d'après la contre-lecture) | quatre des cinq cartes de Carbon alors non gardées (`f91a7a590c8fe`, `f0a8378953d43`, `f17603c39bc32`, `ff76aee57bba1`) étaient rattachées par la proposition à l'épreuve de l'héritage, sortie par le coût, avec deux réserves de fond (objet servi : survivants contre registre des tentatives ; critère du meilleur de N dans les sept cartes de la ligne, erratum) ; la cinquième (`f7cc0003c4b2c`), une porte de modification, tombait comme instrument par C2 (écart 2). L'espèce de ces identifiants vient de la lecture descriptive, § 4, identifiants vérifiés par le programme de l'erratum (sortie `d9360b31…`, citée d'après la contre-lecture) |
| `lecture-course-v9-v1.md` | `0306adf74d321cfa933e047adff28324092787f870a2bf97bafd9d52bd5ffddb` | deux juges seulement, de lignées Opus et Argon ; quatre items sur cinq presque à plafond ; tout « notable » du juge Opus l'est du juge Argon ; coût des juges 9,27 dollars pour 94 cartes |
| `lecture-course-v9-v1-erratum-1.md` et ses deux sorties | `9a77160097458889d4ec7771c05e50d97632b7772466c6023f2e444e0a72b9d3` ; probabilités `3cea377a66ec93e7eb1fc694a652d7c880c0b104e5a87ffe97c4d3d03b135ee4` ; citations par espèce `aaadd4c1…` (citée d'après la contre-lecture) | « notable » mesure en bonne part l'absence de citation : sans marque de citation, 33 notables sur 39 ; avec, 34 sur 55 (sortie `aaadd4c1…`) ; aucune carte d'Astra ne cite ; cartes d'Astra les plus courtes ; aucun juge n'est de la lignée d'Astra |
| `../epreuves-v9/ordre-de-passage-epreuves-v9-v3.md` (branche) | `b19f550b525fe5696321167bd43a35fa5ece180fd2f97dad5dfc6e970a8c0f67` | rang 3 : votes effectifs des juges croisés, étage sur processeur puis étage payant d'environ 25 dollars, accordé sous conditions par GO-2026-11-19-66 |

**Le chemin des cartes d'Astra hors des neuf lignes** (constat 1 de la contre-lecture). Au moins 7 des 17 cartes d'Astra hors des neuf lignes étaient au plancher ou au-dessus :
- l'interprète de référence (5 cartes d'Astra sur 9) passait à 8 et n'a perdu la cinquième place qu'à l'ordre alphabétique de l'identifiant ; notée 9 par la contre-lecture, elle entrait dans les cinq ;
- le portefeuille par couverture (porteuse `fdcf828b0dc80`) passait à 8 et a été écarté au départage par C5 = 1 ;
- les certificats de portée étaient au plancher et ont été rangés dessous sans note ;
- puis GO-2026-11-19-56 a pris, parmi les écartées de justesse, la banque d'échecs, le placebo, le jumeau permuté et les instruments, non l'interprète ni le portefeuille ; GO-2026-11-19-59 les a ajoutés ensuite.

**La matrice juge × auteur existe déjà, pour deux juges** (sortie `3cea377a…`, comptes de « notable », vérifiés à l'unité par la contre-lecture) :

| | Argon (21) | Astra (20) | Carbon (16) | Fable (15) | Opus (22) |
|---|---|---|---|---|---|
| juge Opus | 12 | 20 | 13 | 11 | 11 |
| juge Argon | 19 | 20 | 16 | 13 | 15 |

Lecture, sans plus : aucun juge ne note Astra plus bas ; le juge Opus est le plus sévère pour sa propre lignée ; le juge Argon passe 19 des 21 cartes de la sienne. La matrice est **en partie confondue** avec la citation, non entièrement : parmi les 39 cartes sans marque de citation, les 20 d'Astra sont toutes notables et les 19 autres le sont 13 fois (33 − 20). Dans la seule strate où Astra existe, le signe est donc le même. Rien de cela ne vaut mesure d'un biais.

**Littérature.** La mère a lancé une lecture sur source de ce que la littérature dit de la préférence d'un juge pour les productions de sa lignée (R-3852 ; règle R7). La note est **attendue** sous `docs/notes/organisme-auto-conception-v1/juge/` ; elle n'y est pas sur `main` au commit `18936bdb`. Je ne refais pas cette lecture et je n'en cite aucun résultat.

**Ce qui n'est pas établi.** (1) Un biais d'un juge contre Astra comme modèle : non mesuré. (2) Un biais du rédacteur de la proposition (modèle F) contre le style d'Astra : non mesuré ; il a lu sans le champ de l'espèce, mais le style se reconnaît. (3) Que la règle ait eu tort : seule l'épreuve le dira.

**État présent.** GO-2026-11-19-59 a ajouté l'essentiel des lignes d'Astra ; GO-2026-11-19-61 a gardé les treize cartes restantes d'Astra, d'Opus, de Fable et de Carbon, et toutes les cartes d'Astra (20 sur 20) ; le coût ne fait plus tomber une carte dont l'amélioration attendue est considérable (GO-2026-11-19-60). La question porte sur la règle des courses à venir ; la course v9 sert de terrain de mesure.

## 3. Le constat de Lazar, et ce que les pièces y ajoutent

Lazar : « le probleme est donc les criteres de selection qui sont trop severes pour astra et carbon et les eliminent ». C'est la cause que la note v1 nommait, et elle est maintenant décidée (GO-2026-11-19-68, point 4). Les pièces la précisent en quatre mécanismes, que les critères v2 traitent un par un :

| mécanisme constaté | ce qu'il a fait tomber | réponse des critères v2 |
|---|---|---|
| une question neuve vaut zéro (C2), le plancher exige C2 ≥ 1 | six cartes originales d'Astra ; les instruments (dont une carte de Carbon) | trois voies, la question notée dans sa voie, jamais zéro par construction (§ 3 et § 4.2) |
| le coût noté (C3 = 0 au-delà de 75 dollars) | l'héritage et les cartes de Carbon qui y sont rattachées | coût rapporté, hors de la note, du plancher et du départage (§ 6) |
| nombre visé de cinq lignes et départage (C5, puis ordre alphabétique) | l'interprète de référence, le portefeuille par couverture | toutes les lignes au plancher listées ; places réservées par voie ; dernier recours par tirage consigné (§ 5 et § 9) |
| erreurs d'une lecture unique | l'interprète noté 8 pour 9 ; les certificats de portée sans note | deux lecteurs, plancher passé dès qu'un seul l'accorde, raison écrite pour chaque note (§ 1, § 4, § 5) |

« Trop sévères » est donc exact, à ceci près : la sévérité ne tenait pas au seul barème, mais aussi au nombre visé, au départage et à la lecture unique. Rien de cela ne visait une espèce ; l'effet par espèce vient de ce que les lignées n'écrivent pas le même type de carte.

## 4. Les voies comparées

**Garde commune.** N-058 fixe que la composition des proposeurs se juge sur l'oracle du monde planté et le coût mesuré, jamais sur le verdict d'un juge ; elle s'étend à la composition des juges par N-059, point 14 (la table par juge est un score de juge). Avec N-053, point 5, et l'exclusion « un modèle décide » : un juge, un lecteur ou un collège peut **proposer** ce qui va à l'épreuve ; il ne décide ni de la composition, ni de l'adoption, et ne trie rien à l'intérieur de l'organisme. Ce sont les essais qui tranchent.

**N-045 v2, en toutes lettres.** Point 1 : un juge de lignée Astra ou Carbon est un choix de « modèle par rôle », variable à juger sur l'oracle et le coût. Point 4 : les voies bon marché avant la voie chère, donc les mesures 1 à 3 avant la 4 (§ 6). Point 2 : il porte sur le signal rendu à l'organisme et ne touche pas la règle de sélection de la mère.

| voie | ce qu'elle change | ce qu'elle risque | garde |
|---|---|---|---|
| **(i) Collège d'un juge par lignée** (cinq), chaque juge récusé pour les cartes de sa lignée par programme, le juge restant aveugle à l'espèce (N-058, point 1) ; quatre voix par carte | plus de regards ; un juge Astra et un juge Carbon existent enfin | une majorité ramène vers le familier ; erreurs corrélées (Opus et Fable sont de la même famille ; en v9 les notables d'un juge sont inclus dans ceux de l'autre) ; avec la consigne actuelle, le collège voterait surtout sur les citations ; coût des juges multiplié par deux et demi environ | à mesurer avant adoption (GO-2026-11-19-68, point 2) ; sortie descriptive ou liste proposée, jamais un tri automatique ; l'avis pondéré reste descriptif (GO-2026-11-19-63) |
| **(ii) Davantage de juges Astra** | donne plus de poids à une lignée | corrige un biais non mesuré, dont le seul indice a le signe inverse ; un juge Astra sur des cartes d'Astra est contraire à l'esprit de N-053, point 4 (« juge d'une autre lignée »), sans en être la lettre ; régler la composition des juges pour un résultat sur une espèce, c'est viser un signe (règle R3) | fermée comme surpoids ; un seul juge Astra, comme bras mesuré de (i) |
| **(iii) Juges descriptifs, règle de sélection changée** | la pièce jointe : trois voies d'entrée, coût rapporté, quotas par strate, deux lecteurs | plus de lignes, donc plus de préenregistrements et de devis ; le rangement par voie est un jugement de lecteur ; « question neuve » peut devenir un fourre-tout si l'oracle n'est pas exigé | scellée avant l'ouverture ; elle propose, Lazar choisit |
| **(iv) Droit de veto contre l'élimination** (le « droit de défense » de la v1, précisé par GO-2026-11-19-68) | § 5 | § 5 | § 5 |
| **(v) Lot tiré au sort** | une ligne par voie, tirée parmi les non retenues, graine fixée d'avance ; aucun modèle n'y décide ; base contre laquelle toute règle se compare | des épreuves dépensées sur des cartes faibles | bras témoin, coût rapporté |

Les voies (iii), (iv) et (v) se combinent et forment les critères v2. (i) peut les servir comme instrument de mesure, puis comme titulaire du veto si sa mesure le justifie. (ii) reste fermée.

## 5. Le veto : deux ou trois cartes par juge

**Lecture retenue par la mère.** Chaque juge dispose d'un droit de veto contre l'élimination, limité à deux ou trois cartes. Le veto fait entrer la carte dans la proposition, sur une liste à part. **Il n'empêche que l'élimination : il ne fait rien adopter** (N-058), ne retire aucune carte, ne s'exerce jamais contre une carte, et ne lève aucune exclusion.

**Qui est titulaire.** En v9, les juges n'ont rendu aucune liste de veto, et leur consigne mesurait surtout la citation. Leur demander une liste est un appel de modèle : sur devis. Sans dépense, les titulaires sont les deux lecteurs de la sélection (lignées Opus et Fable, même famille). Les critères v2 ouvrent le veto aux deux : aux lecteurs toujours, aux juges de la course si celle-ci leur fait rendre une liste scellée avant la lecture.

**Hors de sa lignée, sans lire l'espèce.** Le titulaire rend une liste ordonnée de V cartes et de deux suppléantes ; un programme retire ensuite celles de sa lignée et garde les V premières. Le titulaire n'apprend rien de l'espèce.

**Ce que la limite change** (ordres de grandeur sur une course de 94 cartes comme la v9 ; ce ne sont ni des seuils ni des devis) :

| | deux cartes par titulaire | trois cartes par titulaire |
|---|---|---|
| cartes repêchées, deux titulaires | 4 au plus (4 %) | 6 au plus (6 %) |
| cartes repêchées, cinq titulaires (collège) | 10 au plus (11 %) | 15 au plus (16 %) |
| lignes en plus | moins que de cartes si plusieurs veto tombent sur une même épreuve ; au pire autant | de même ; au pire moitié plus qu'à deux |
| capture par une lignée : part des veto qu'une seule lignée peut recevoir | tout, soit 4 cartes à deux titulaires, 8 à cinq (quatre titulaires hors lignée) | tout, soit 6 cartes à deux titulaires, 12 à cinq — plus de la moitié des cartes d'une lignée qui en compte vingt |
| capture par une famille (un titulaire Opus défend des cartes Fable, et l'inverse) | 2 par titulaire | 3 par titulaire |
| symétrie | même limite pour tous ; mais une lignée sans titulaire n'a personne de récusé : ses cartes sont ouvertes à tous les veto, celles d'une lignée titulaire à tous sauf un. L'écart est le même en proportion aux deux limites | de même ; l'écart est plus grand en nombre de cartes |
| coût de l'épreuve | chaque ligne en plus demande un préenregistrement, une contre-lecture et, pour l'étage payant, un devis ; sous la limite de charge de GO-2026-11-19-67 (deux scellements par jour), 4 lignes de plus font deux jours | 6 lignes de plus font trois jours ; 15 en feraient plus d'une semaine |
| ce que l'on apprend | peu de prédictions de veto à vérifier après l'épreuve : taux de réussite presque illisible | un peu plus ; toujours une description, pas une mesure |
| garde N-058 | identique : le veto propose, l'épreuve tranche ; le taux de réussite d'un titulaire ne sert ni à le choisir ni à le pondérer | identique |

**Lecture.** La limite règle deux choses qui tirent en sens contraire : la protection de la carte singulière (plus à trois) et la charge d'épreuves ajoutée sans que la règle l'ait demandée (moins à deux). Le risque de capture ne dépend pas tant de la limite que du nombre de titulaires et de la règle « hors de sa lignée » ; c'est le compte par espèce après coup, dans les deux sens (règle R4), qui le surveille. Avec deux titulaires de la même famille, trois cartes chacun restent un petit nombre (6 sur 94). Avec un collège de cinq, deux suffisent (10 sur 94) et trois (15) dépasseraient le nombre visé par défaut, neuf lignes.

**Recommandation.** Trois cartes par titulaire s'ils sont trois au plus, deux au-delà. C'est ce qu'écrivent les critères v2, § 7, « sauf mot contraire de Lazar avant l'ouverture ».

## 6. La mesure qui départage, gratuit d'abord

Chaque mesure se préenregistre et se scelle avant lecture (règle R1), contre-lecture par un modèle O ; les seuils se fixent au préenregistrement.

1. **Matrice juge × auteur, démêlée de la citation — sans dépense.** Un programme relit les champs des verdicts déjà scellés et les motifs de citation des cartes (programme `50ad93a5…`, cité d'après la contre-lecture), sans lecture par un agent. Question : chaque juge note-t-il mieux sa lignée, la citation tenue fixe ? **Déjà connu, à déclarer au préenregistrement** : la strate sans citation (Astra 20 sur 20, les autres 13 sur 19) ; ne compte comme épreuve que le reste, par item et par juge. **Limites à écrire d'avance** : deux juges, items à plafond, 94 cartes ; cases presque vides (Astra : aucune carte avec citation ; Argon : une seule sans) ; puissance faible ; aucune réponse possible pour un juge Astra ou Carbon, qui n'existe pas.
2. **Rejeu de la règle — sans dépense pour deux lecteurs.** Deux lecteurs neufs, l'un Opus, l'autre Fable (même famille, déclaré), rangent les 94 cartes sans le champ de l'espèce sous les critères v2 ; un troisième, d'une autre famille, est un appel payant, sur devis et ligne neuve. Un programme compare, par voie puis par espèce (lue en dernier), ce que la règle v1 et la règle v2 envoient à l'épreuve, et l'accord des lecteurs. Masque d'espèce imparfait, déclaré. Cela décrit les règles ; cela ne dit pas laquelle a raison.
3. **Comparaison après coup contre l'oracle — sans dépense, différée, descriptive.** Presque toutes les cartes de la v9 seront éprouvées. Avant de lire la première issue, on scelle ce que chaque règle (v1, v2, veto, tirage, vote du collège s'il existe) aurait proposé, puis on compte, par règle, les épreuves qui ont changé une décision de conception et leur coût. **Limite : la règle v2 est conçue après avoir vu ce qui est tombé en v9, et pour le faire entrer.** Ce n'est pas une épreuve tenue à l'écart. L'épreuve décisive est la course suivante, critères scellés avant l'ouverture de ses cartes. Les veto du rejeu ont la même limite que la mesure 2 (deux lecteurs d'une même famille).
4. **Votes effectifs du collège sur témoins plantés — payant.** C'est la ligne 3 de l'ordre de passage, accordée à 25 dollars sous conditions (GO-2026-11-19-66) pour deux juges ; le collège à cinq lignées en serait un bras de plus, sur devis et ligne neuve (de l'ordre de 60 dollars, à chiffrer). Témoins à faute connue, plantée par programme dans des cartes de chaque lignée. On mesure par juge les faux acceptés et les vrais rejetés, la corrélation des erreurs, le nombre de votes effectifs, l'interaction juge × lignée d'origine à faute égale, et trois règles : majorité, unanimité, veto d'un seul.
5. **Faire juger les 94 cartes par les trois lignées manquantes — payant, non recommandé en l'état.** La consigne de la v9 mesurerait encore la citation. À ne proposer qu'après la mesure 4 et avec une consigne refaite.

**Lecture qui départage.**
- Les critères v2 se décrivent par les mesures 2 et 3 et s'éprouvent à la course suivante.
- Le collège (i) ne gagne une place que s'il bat, **à coût apparié**, un juge seul répété k fois (témoin de N-045, point 4, déjà prévu par la ligne 3.3 de la proposition) **et** le collège à deux juges, sur les témoins plantés (faux acceptés, vrais rejetés), son coût rapporté par carte (N-058, point 1). Plus de votes effectifs ne suffit pas : ajouter des juges en donne presque toujours un peu.
- Toute interaction juge × lignée, dans les deux sens et pour chaque lignée (le juge Argon passe 19 de ses 21 cartes), lue sous contrôle de multiplicité (cinq juges × cinq lignées), appelle la récusation ou l'étalonnage du juge en cause. La voie (ii), comme surpoids, reste fermée.

## 7. Ce que la note ne dit pas

- Que les cartes d'Astra ou de Carbon valent mieux ou moins bien que les autres : rien n'est éprouvé.
- Qu'un juge, ou le rédacteur de la proposition, est biaisé ou ne l'est pas : aucune mesure n'existe.
- Que la règle v1 avait tort : elle a fait ce qu'elle disait, à deux erreurs de lecture près, et ses écarts étaient écrits.
- Qu'un collège à cinq est meilleur que deux juges, ni que trois veto valent mieux que deux : la recommandation du § 5 est un jugement de conception sur la charge et le nombre, non un résultat.
- Ce que dit la littérature : la note est attendue (§ 2).
- Aucun seuil, aucun devis, aucune modification d'une hypothèse ou d'une revendication.

## 8. Les douze constats de la contre-lecture

| constat | gravité | où, dans la v2 | comment |
|---|---|---|---|
| 1. Cause de l'écart d'Astra réduite à C2 et C3 | majeur | § 1, première phrase ; § 2, ligne `a923cb57…` et paragraphe « Le chemin des cartes d'Astra » ; § 3 ; § 9, « Enjeu » | phrase de la contre-lecture reprise ; quatre mécanismes nommés ; deux lecteurs exigés. R-3845 porte la même simplification : signalé à la mère dans le rapport |
| 2. « Les neuf premières lignes » est faux | majeur | § 2, ligne `2af9e67f…` | « dans les neuf lignes retenues par GO-2026-11-19-55 et -56 », avec la précision sur les rangs 6 et 8 |
| 3. Carbon : le coût seul est plus net que les pièces | majeur | § 2, ligne `de7ed04d…` | texte de la contre-lecture repris : héritage sorti par le coût, deux réserves de fond, erratum, cinquième carte comme instrument, source de l'espèce |
| 4. Matrice : source, faisabilité, règle R1 | moyen | § 2, ligne de l'erratum et lecture de la matrice ; § 6, mesure 1 | les deux sorties citées ; « en partie confondue » ; motifs de citation par programme ; connu déclaré ; cases vides et puissance |
| 5. Le collège jugé sans coût ni témoin apparié | majeur | § 6, « Lecture qui départage », deuxième point | bat à coût apparié un juge seul répété k fois et le collège à deux ; coût par carte |
| 6. Ouverture asymétrique de la voie (ii) | moyen | § 6, troisième point ; § 4, voie (ii) | toute interaction, deux sens, chaque lignée, multiplicité ; récusation ou étalonnage ; surpoids fermé |
| 7. Deux renvois débordent la lettre | moyen | § 4, garde commune et voie (ii) | « contraire à l'esprit de N-053, point 4, sans en être la lettre » ; extension aux juges par N-059, point 14 |
| 8. N-045 et GO-60 non tenus en toutes lettres | moyen | § 4, « N-045 v2 » ; § 9, option (a) et confirmations ; critères v2, § 6 et § 11 | points 1, 2 et 4 écrits ; coût hors de la note demandé à Lazar comme allant au-delà de GO-60 ; coût gardé dans l'ordre de passage |
| 9. Mesure 2 : « gratuit » contre « lignées différentes » | moyen | § 6, mesures 2 et 3 ; § 5, « Qui est titulaire » | Opus et Fable, même famille, sans dépense ; troisième sur devis ; masque imparfait ; même limite pour les veto |
| 10. Mesure 3 : pas hors échantillon | moyen | § 6, mesure 3 ; critères v2, en-tête | limite écrite ; épreuve décisive à la course suivante ; mesure 3 descriptive |
| 11. En-tête et état présent | mineur | en-tête ; § 1 ; § 2, « État présent » ; § 4, voie (i) | GO-65 et R-3845 lus sur `main` ; GO-59 cité ; « sans le champ de l'espèce, masque imparfait » ; récusation par programme |
| 12. Dire ce que (a) donne au juge | mineur | § 9, « Ce que cela donne au juge » | le juge peut empêcher une élimination ; il ne sélectionne pas |

## 9. Décision pour Lazar

**Décision.** Adopter les critères de sélection v2 pour la prochaine course, et fixer la limite du veto : deux ou trois cartes ?

**Enjeu.** Tu as nommé la cause, les critères. Ils sont réécrits et scellés avant toute lecture de carte. Reste la limite du veto : elle règle combien d'épreuves entrent hors de la règle, et la charge d'écriture qui va avec. Ce que la règle retient n'adopte rien : ce sont les essais qui tranchent.

**Ce que cela donne au juge.** Tu demandais que le juge « puisse sélectionner ». Sous les critères v2, un juge ou un lecteur peut **empêcher l'élimination** de deux ou trois cartes ; il ne sélectionne pas et n'adopte rien. Tant que les juges de la course ne rendent pas de liste (appel payant), ce sont les deux lecteurs, Opus et Fable, qui tiennent le veto.

**Options.**
- **(a) Critères v2, veto de trois cartes à trois titulaires au plus, de deux au-delà.** Avantage : 6 cartes repêchées au plus avec deux lecteurs, 10 avec un collège de cinq ; la charge reste bornée quand le collège grandit. Inconvénient : une règle à deux régimes.
- **(b) Critères v2, veto de deux cartes toujours.** Avantage : le plus léger, 4 cartes avec deux lecteurs. Inconvénient : protège peu tant qu'il n'y a que deux titulaires de la même famille.
- **(c) Critères v2, veto de trois cartes toujours.** Avantage : simple, protège le plus. Inconvénient : 15 cartes avec un collège de cinq, soit plus d'une semaine de scellements en plus, et jusqu'à 12 pour une seule lignée.

**Recommandation.** (a), confiance 0,6. Le collège de cinq reste à mesurer avant adoption (GO-2026-11-19-68, point 2) ; si la mesure 4 trouve un juge défavorable à une lignée, je reviens vers toi avec la récusation ou l'étalonnage, pas avec le surpoids.

**À confirmer avec ton choix** (critères v2, § 11) : le coût sort de la note pour toutes les cartes, au-delà de la lettre de GO-2026-11-19-60 ; neuf lignes visées par défaut ; trois lignes tirées au sort comme bras témoin, qui sont des épreuves en plus.

**Défaut sous 48 heures.** L'option (a) pour la part sans dépense : critères v2 contre-lus, mesures 1 et 2 préparées avec les deux lecteurs sans dépense. Rien de payant, et aucun usage de ces critères sur une course neuve, sans ton mot.

## 10. Différentiel v1 → v2

- **En-tête** : GO-65 et R-3845 lus sur `main` ; GO-2026-11-19-68 et les mots de Lazar sur le veto et sur les critères ajoutés ; pièce jointe nommée.
- **§ 1** : première phrase remplacée (constats 1 et 11) ; « confondu » devient « en partie confondu » (constat 4) ; troisième phrase : la cause est tranchée par Lazar, recommandation sur le veto.
- **§ 2** : cinq lignes du tableau corrigées (constats 1 à 4) ; paragraphe « Le chemin des cartes d'Astra » ajouté ; lecture de la matrice précisée ; paragraphe « Littérature » ajouté (note attendue) ; « État présent » cite GO-59.
- **§ 3, neuf** : le constat de Lazar et les quatre mécanismes.
- **§ 4** (ancien § 3) : garde commune réécrite avec N-059, point 14 ; N-045 v2 en toutes lettres ; voie (ii) fermée comme surpoids ; voie (iii) renvoyée à la pièce jointe ; voie (iv) renommée « droit de veto contre l'élimination ».
- **§ 5, neuf** : comparaison du veto à deux et à trois cartes.
- **§ 6** (ancien § 4) : mesures 1 à 3 corrigées (constats 4, 9, 10) ; mesure 4 rattachée à GO-66 ; lecture qui départage refaite (constats 5 et 6).
- **§ 7** (ancien § 5) : ajusté ; la phrase « la règle (iii) n'est qu'esquissée » retirée, la règle étant écrite.
- **§ 8, neuf** : tableau des douze constats.
- **§ 9** (ancien § 6) : fiche refaite — la décision ne porte plus sur le choix entre trois voies, tranché par GO-2026-11-19-68, mais sur l'adoption des critères v2 et la limite du veto ; ce que cela donne au juge (constat 12) ; confirmations demandées (constat 8).
- **Inchangé** : aucun biais de juge mesuré ; collège à mesurer avant adoption ; pas de surpoids d'une lignée ; aucune dépense sans devis.
