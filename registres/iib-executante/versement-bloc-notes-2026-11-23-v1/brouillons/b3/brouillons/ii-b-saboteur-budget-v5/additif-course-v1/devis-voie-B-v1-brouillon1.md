# Devis — voie (B) du saboteur à budget (v5) : ancien code ; lot manquant de l'étalonnage sur une machine neuve, assemblage, puis course — v1, brouillon 1

- **Statut** : brouillon 1, pièce décisive (devis), non contre-lu. Écrit le 2026-11-22 vers 15:00Z (`date -u`) par un rédacteur neuf, Claude Fable 5.2, du côté du saboteur, sous le mandat `registres/iib-executante/mandat-fable-additif-ordre-course-et-devis-v1.md` (`0ead00d9ac01ed0a28367246f37118aeca79daea468993de0e094679a62aaf0f`, vérifié). Aucune dépense n'est engagée par ce document ; aucune ligne d'accord n'y est écrite. À contre-lire par un autre modèle, puis vérification des corrections par le même, avant tout scellement.
- **Accord cité** : `GO-2026-11-22-71` (`registres/go.md` de `main`, tête `17082d49ce426522540667076c23d1a5f210a3de`, empreinte du registre `dc24a69f0b55605223fa98086bb879b6ceea7470a0ff817f6bdabfd33b37da57`) : « (B) ancien code : le seul lot manquant de l'étalonnage joué sur une machine neuve (écart au texte scellé, section 15, accepté par ce mot, réserve « deux machines » déclarée), puis course répartie sur plusieurs cartes » ; colonne du plafond : « (A) 44 USD ; (B) 55 USD ; Vast » ; échéance 2026-11-27.
- **Ordre chiffré** : `additif-ordre-course-voie-B-v1-brouillon1.md`, à côté de ce devis (son empreinte est dans son compagnon). Texte scellé de l'organisme retenu (`c1dc54597a1ab4b467331673607d986e46a706c06253bb40070e5d15caaa61f2`), sections 10.1 à 10.3 et 15 ; devis scellé de la première ligne (`cb881522378ace662787a7097c2baa6d461c766d70782d28636c132ce09f3ee8`) et son erratum 1 (`90342292f52daf2f7281acad68006598450033367d3a36aa1c6c72eac9150f9a`).
- **Arithmétique** : `calcul-devis-voies-A-B-v1.py` (`557a83fa6cbb6050080e17b4c20331acb29588498b04418897cc673cdc1cab80`), sortie `sortie-calcul-devis-voies-A-B-v1.txt` (`b1a21a35c72fce048ab437e2643cf7dbb06bbfd6b13f314e1e34980cea154ae6`), à côté. Chaque chiffre renvoie à une ligne [Lnn] de cette sortie.
- **Lu** : des durées, des prix et des comptes (`registres/iib-executante/chiffres-devis-code-corrige-v1.md`, `4e10a0047e1db340910bd9d41291a5210d787ad340876fd8649f91542963f710` ; comptes rendus 27 à 30 de l'exécutante). Aucune sortie de mesure, aucune consigne privée, aucune pièce du côté des sondes.

## 0. En bref

**Ce devis n'a pas un attendu, il en a trois, selon le rythme des machines louées.** L'ancien code a été vu à deux rythmes : celui du devis scellé (machine du 19 novembre) et 5,29 fois plus lent (machine 61875617) [L03]. Personne ne sait d'avance à quel rythme sera une machine neuve.

| issue de la voie | dépense neuve | ligne |
|---|---|---|
| le lot 28 tombe sur une machine lente : la règle scellée du plafond de tours rend « ne part pas » ; la voie s'arrête là | **≈ 3,5 USD** | [L30] [L37] |
| le lot 28 puis la course tombent sur des machines au rythme du devis scellé : course de 12 tours aboutie | **≈ 16,2 USD** | [L37] |
| le lot 28 est au rythme du devis scellé, la course tombe sur une machine lente : arrêtée par la garde de rythme au tour 1 | **≈ 10,0 USD** | [L37] |

| haut | au pire | plafond | coupure proposée |
|---|---|---|---|
| **≈ 32,6 USD** (lot 28 puis course à deux fois les durées du devis scellé, prix aux bornes) [L37] | **53,61 USD**, tenu par les gardes [L38] | **55 USD** (GO-2026-11-22-71) | **52 USD** de dépense neuve de la voie |

Ces chiffres comptent la **dépense neuve de la voie**. Les 16,22 USD déjà dépensés sous `GO-2026-11-21-70` et le stockage de 61875617 n'y sont pas [L07].

**Dépense au-delà du crédit chez le loueur** (12,995 USD le 22 novembre à 14:11Z) : 0 si la voie s'arrête au lot 28 ou à la garde de rythme ; **3,22 USD** pour une course aboutie au rythme du devis scellé ; **19,60** au haut ; **40,62** au pire [L39].

**Trois faits que ce devis apprend au directeur.**
1. **Au rythme de 61875617, la course ne tient pas sous 55 USD**, sur une carte comme sur plusieurs : 65,67 à 76,50 USD au prix borne [L36], 56,09 au prix relevé sur une carte [L33].
2. **Répartir la course sur plusieurs cartes ne rend pas la voie moins chère** : cela raccourcit le calendrier et ajoute une mise en route par carte [L36]. Et le lanceur de session refuse aujourd'hui deux machines du saboteur à la fois (additif, § 1, C2).
3. **La règle scellée du plafond de tours décide de la voie avant les oracles.** Aux durées de l'étalonnage tel qu'il a été joué, elle finance 1 à 4 tours pour 12 exigés [L31] : l'issue est « ne part pas », motif « tours ». La voie ne mène à une course que si Lazar accepte un second écart au texte scellé (§ 5).

## 1. Ce qui est mesuré

| grandeur | valeur | source | ligne |
|---|---|---|---|
| prix | carte 1,16 + stockage 0,033333 = **1,193 USD par heure** | chiffres de l'exécutante | [L01] |
| de la création au début du run | **≈ 70 min** (61875617) | chiffres | [L06] |
| rythme de l'ancien code sur 61875617 | 27 lots en ≈ 11,5 h : **5,29 fois** les durées du devis scellé | chiffres ; calcul | [L03] |
| durées du devis scellé (machine du 19 novembre, même code) | 39,08 s par épisode ; 0,511 s par action d'oracle | devis scellé § 1 | [L02] |
| un lot flagrant (8 épisodes, 160 actions d'oracle) | 394,4 s aux durées du devis scellé ; 34,8 min au rythme lent | calcul | [L02] [L04] |
| durée de la machine 61875617, du début de son amorce à son arrêt | ≈ 13,4 h (création le 21 à 23:29Z, arrêt le 22 à 12:54:36Z) ; à relever exactement par l'exécutante | comptes rendus 27 et 29 | [L31] |

Seule la durée des 27 lots réunis est connue. Les chronomètres par épisode et par action d'oracle étaient dans la mémoire du processus coupé : ils n'existent plus (lecture du code au commit `43d6d0673edd5055917f536e5310ea99c15ab75e`, `lanceur_v5.phase_etalonnage`).

## 2. Hypothèses et marges

| jeu | rythme, en fois les durées du devis scellé | mise en route | prix horaire | forfait de téléchargement, par machine | ligne |
|---|---|---|---|---|---|
| machine au rythme du devis scellé | 1 | 70 min | 1,193 (relevé) | 1,04 (relevé) | [L33] |
| haut | 2 | 70 min | 1,38 (borne) | 2,00 (borne) | [L33] |
| limite de la garde de rythme (12 tours) | 3,37 | 70 min | 1,38 | 2,00 | [L34] |
| machine lente | 5,29 | 70 min | 1,38 | 2,00 | [L33] |
| pire | celui des gardes : 53,61 USD | | | | [L38] |

- Un même facteur est appliqué à l'épisode et à l'action d'oracle : hypothèse.
- Épisodes du maître, flagrants : comptés comme un épisode honnête, comme au devis scellé ; aucune durée mesurée.
- **Deux locations**, l'une après l'autre (lot 28, puis course) ; six heures d'arrêt avant destruction comptées par machine.
- **Une carte pour la course** : c'est ce que le code et le lanceur permettent aujourd'hui (§ 3).

## 3. Les deux étapes

**Étape 1 — lot 28 et écriture de fin.** Huit épisodes flagrants, 160 actions d'oracle, puis l'assemblage des 28 lots et l'écriture de fin par programme (10 min comptées).

| | durée | dépense, forfait et arrêt compris | ligne |
|---|---|---|---|
| machine au rythme du devis scellé | 1,44 h | 2,96 USD | [L30] |
| machine lente | 1,91 h | 3,52 USD (5,12 aux prix bornes) | [L30] |
| borne (échéance à 3 h) | 3 h | 6,14 USD | [L30] |

**Étape 2 — course sur une carte, ancien code**, si la désignation rend l'un des deux oracles.

| rythme de la machine | 12 tours | 24 tours | ligne |
|---|---|---|---|
| celui du devis scellé (prix relevé) | 10,07 h ; 13,26 USD | 14,78 h ; 18,88 USD | [L33] |
| 2 fois plus lent (prix borne) | 18,47 h ; 27,97 USD | 27,90 h ; 40,98 USD | [L33] |
| 3 fois plus lent (prix borne) | 26,87 h ; 39,56 USD | 41,01 h ; 59,07 USD | [L33] |
| celui de 61875617, sans garde (prix borne) | 46,14 h ; 66,15 USD | 71,09 h ; 100,58 USD | [L33] |
| celui de 61875617, arrêtée par la garde de rythme au tour 1 | 2,99 h ; 7,05 USD au plus | | [L35] |

**Garde de rythme** (additif, § 1, C4) : pour 12 tours, tour 1 écrit au plus tard 1,57 h après la marque de début du run, tour 4 au plus tard 5,55 h ; pour 24 tours, tour 1 au plus tard 1,10 h [L34]. Au-delà : arrêt par l'identifiant. Pour 12 tours, elle admet une machine jusqu'à 3,37 fois plus lente que le devis scellé ; elle arrête celle du rythme de 61875617.

**Course répartie sur N cartes** (calendrier ; dépense au prix borne ; temps de coordination non compté) [L36] :

| rythme | une carte | deux cartes | quatre cartes |
|---|---|---|---|
| celui du devis scellé | 10,1 h ; 15,90 USD | 5,9 h ; 19,51 USD | 3,8 h ; 26,73 USD |
| celui de 61875617 | 46,1 h ; 65,67 USD | 23,9 h ; 69,28 USD | 12,8 h ; 76,50 USD |

Répartir demande deux correctifs qui n'existent pas et que le mandat n'annonce pas : un lanceur de session qui admette plusieurs machines du saboteur, et un partage de la course entre machines avec assemblage. Les tours se suivent (la règle d'arrêt lit chaque tour) : seul l'intérieur d'un tour se partage.

## 4. Plafond, coupure, échéance, crédit

**Plafond : 55 USD. Coupure : 52 USD de dépense neuve de la voie.** Pire tenu par les gardes : 52 + 0,92 + 0,69 = **53,61 USD** [L38] [L08].

**Ce qui tient la coupure : l'échéance de chaque machine**, calculée par programme sur le compte de la voie, comme pour la voie (A) : la garde d'épuisement du lanceur ne tient pas une voie (dépense antérieure déclarée bornée à 5 USD ; `sortie-verification-gardes-du-lanceur-v1.txt`, `43e433d5ae0694bd3652d7fa9b796c8601a9c6ef0028165ac0790d6eee4ae0eb`, §§ 1 et 5). À l'échéance, la minuterie consigne et pousse, puis détruit la machine.

**Échéance.** Échéance de la voie : 2026-11-27. Minuterie au plus tard le 2026-11-27T22:00:00Z ; **aucune création à partir du 2026-11-27T00:00:00Z** [L52]. Une course créée à la dernière minute garde 22 heures : assez au rythme du devis scellé (10,07 h) et à deux fois ce rythme (18,47 h), pas à trois fois (26,87 h).

**Crédit.** Avant chaque création, le crédit lu couvre le pire de la machine à créer plus 2 USD ; sinon aucune création, nœud. Le crédit est commun aux autres machines du compte.

**Lecture du plafond de 55 USD (nœud).** Ce devis lit 55 USD comme le plafond de la dépense neuve de la voie. Lu comme un total de la ligne `GO-2026-11-21-70`, passé compris, il laisse 37,98 USD de dépense neuve [L40] ; et les deux voies ne tiennent pas ensemble sous la coupure de 55 [L51].

## 5. Plafond de tours : le second écart au texte scellé

Le passage des conditions lit, dans le fichier de fin de l'étalonnage, les durées mesurées et la dépense de l'étalonnage (texte scellé, 10.2). Le fichier d'entrées scellé (plafond 45, coût fixe 6,90, prix 1,38) ne change pas : la configuration scellée le cite par son empreinte.

| variante | durées écrites dans le fichier de fin | plafond de tours | suite | ligne |
|---|---|---|---|---|
| **(a)** lettre du texte scellé | celles de l'étalonnage tel qu'il a été joué (rythme de 61875617) | 1 à 4 tours ; 12 exigés | issue « ne part pas », motif « tours », si aucune épreuve n'échoue avant ; **la voie s'arrête à 3,5 USD** | [L31] |
| **(b)** écart déclaré, sur le mot de Lazar | celles du seul lot 28, sur la machine neuve : le seul chronomètre qui existe | 31 tours si la machine neuve est au rythme du devis scellé ; 4 si elle est lente ; 12 tours financés jusqu'à 2,39 fois les durées du devis scellé | la course peut partir si les oracles remplissent leurs conditions | [L32] |

Dans les deux variantes, la dépense de l'étalonnage est celle des deux machines, au prix du fichier d'entrées : ≈ 21,13 USD [L31].

## 6. Liste d'arrêt (résumé ; le texte qui fait foi est l'additif, § 5)

| arrêt | quand | action |
|---|---|---|
| un champ entre chevrons, une machine du saboteur sur le compte, crédit insuffisant, échéance refusée par le programme, création à partir du 27 novembre 00:00Z | avant toute création | aucune création |
| versions de bibliothèques, révision du modèle ou type de carte différents de ceux des 27 lots ; un lot dont le sceau diffère ; une tâche flagrante manquante ou en double | lot 28 et assemblage | arrêt ; rien n'est écrit ; nœud |
| suite d'essais en échec ; gardes du texte scellé ; échéance | lot 28 | ce qui existe est versé avec son motif |
| issue « ne part pas » ou « non calculable » | désignation | la course ne part pas ; phrases écrites d'avance |
| garde de rythme ; échéance ; gardes | course | arrêt par l'identifiant ; la course est consommée |
| tour de contrôle ; consigne sans effet ; moins de 48 épisodes acceptés | course | fins écrites d'avance : la course a abouti |
| l'autre voie a abouti la première | à tout moment | plus aucune création |

Aucun arrêt n'est suivi d'une relance sans nœud de Lazar et devis neuf.

## 7. Réserves

1. Le rythme d'une machine neuve n'est pas connu : deux machines vues, deux rythmes.
2. Un même facteur est appliqué à l'épisode et à l'action d'oracle ; leur partage réel n'est pas connu.
3. Les tours du maître, la distillation et l'évaluation n'ont aucune durée réelle.
4. La dépense passée de 16,22 USD et la durée de 61875617 viennent des comptes rendus de l'exécutante, non d'une facture.
5. Le rédacteur n'a pas lu le correctif de reprise (à venir).
6. La course n'a qu'un engagement : une machine lente, arrêtée par la garde de rythme, consomme la course de la voie.
7. Réserve « deux machines » : son texte, écrit d'avance, est dans l'additif (§ 2).

## 8. Choix pour Lazar

| choix | recommandation | confiance |
|---|---|---|
| plafond de tours | **variante (b)**, avec sa réserve écrite d'avance ; sans le mot de Lazar, la variante (a) s'applique et la voie s'arrête à la désignation | moyenne |
| nombre de cartes de la course | **une** : à un rythme rapide, une carte finit en 10 heures ; à un rythme lent, aucun nombre de cartes ne tient sous 55 USD ; plusieurs cartes demandent deux correctifs non écrits | forte |
| lecture du plafond de 55 USD | **dépense neuve de la voie**, coupure 52 | moyenne |
| recharge du crédit | **au moins 41 USD pour la voie (B) seule au pire** (40,62 au-delà du crédit) ; 4 USD suffisent à une course aboutie au rythme du devis scellé ; les deux voies : 84,22 au pire, 26,38 à l'attendu [L50] | forte |
| réserve « deux machines » | **acceptée par GO-2026-11-22-71** ; texte de la réserve à confirmer | forte |

Défaut sous 48 heures : aucun ; aucune création sans la recharge ; sans mot sur le plafond de tours, variante (a).
