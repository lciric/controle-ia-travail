# Devis — voie (A) du saboteur à budget (v5) : code du tirage corrigé ; essai de vitesse, étalonnage entier rejoué, puis course — v1, brouillon 1

- **Statut** : brouillon 1, pièce décisive (devis), non contre-lu. Écrit le 2026-11-22 vers 15:00Z (`date -u`) par un rédacteur neuf, Claude Fable 5.2, du côté du saboteur, sous le mandat `registres/iib-executante/mandat-fable-additif-ordre-course-et-devis-v1.md` (`0ead00d9ac01ed0a28367246f37118aeca79daea468993de0e094679a62aaf0f`, vérifié). Aucune dépense n'est engagée par ce document ; aucune ligne d'accord n'y est écrite. À contre-lire par un autre modèle, puis vérification des corrections par le même, avant tout scellement.
- **Accord cité** : `GO-2026-11-22-71` (`registres/go.md` de `main`, tête `17082d49ce426522540667076c23d1a5f210a3de`, empreinte du registre `dc24a69f0b55605223fa98086bb879b6ceea7470a0ff817f6bdabfd33b37da57`) : « go C !!! », les deux voies en parallèle, la première qui réussit est retenue ; colonne du plafond : « (A) 44 USD ; (B) 55 USD ; Vast » ; échéance 2026-11-27. « Départ de chaque voie après l'additif de Fable à l'ordre de course et son devis, scellés. »
- **Ordre chiffré** : `additif-ordre-course-voie-A-v1-brouillon1.md`, à côté de ce devis (son empreinte est dans son compagnon). Texte scellé de l'organisme retenu (`c1dc54597a1ab4b467331673607d986e46a706c06253bb40070e5d15caaa61f2`), sections 10.1 à 10.3 et 15 ; devis scellé de la première ligne (`cb881522378ace662787a7097c2baa6d461c766d70782d28636c132ce09f3ee8`) et son erratum 1 (`90342292f52daf2f7281acad68006598450033367d3a36aa1c6c72eac9150f9a`), dont ce devis garde la forme et les durées de base.
- **Arithmétique** : `calcul-devis-voies-A-B-v1.py` (`557a83fa6cbb6050080e17b4c20331acb29588498b04418897cc673cdc1cab80`), sortie `sortie-calcul-devis-voies-A-B-v1.txt` (`b1a21a35c72fce048ab437e2643cf7dbb06bbfd6b13f314e1e34980cea154ae6`), à côté. Chaque chiffre renvoie à une ligne [Lnn] de cette sortie.
- **Lu** : des durées, des prix et des comptes (`registres/iib-executante/chiffres-devis-code-corrige-v1.md`, `4e10a0047e1db340910bd9d41291a5210d787ad340876fd8649f91542963f710` ; comptes rendus 27 à 30 de l'exécutante). Aucune sortie de mesure, aucune consigne privée, aucune pièce du côté des sondes.

## 0. En bref — les quatre chiffres

| attendu | haut | au pire | plafond | coupure proposée |
|---|---|---|---|---|
| **≈ 23,2 USD** (12 tours, chemin neuf cinq fois plus rapide que le rythme relevé) [L15] | **≈ 40,3 USD** (trois fois plus rapide, prix aux bornes) [L15] | **43,61 USD**, tenu par les gardes [L16] | **44 USD** (GO-2026-11-22-71) | **42 USD** de dépense neuve de la voie |

Ces chiffres comptent la **dépense neuve de la voie**, depuis sa première création. Les 16,22 USD déjà dépensés sous `GO-2026-11-21-70` (étalonnage coupé, relance courte) et le stockage de la machine 61875617 n'y sont pas [L07].

| étape | appels | durée attendue ; haute | coût attendu ; haut | borne de l'étape |
|---|---|---|---|---|
| **1, essai de vitesse** (sans valeur de mesure) | un lot de 8 épisodes honnêtes et ses 160 actions d'oracle, joué trois fois | 2,31 h ; 2,47 h | 3,80 ; 5,40 USD | échéance à 3 h : 6,14 USD [L11] |
| **2, étalonnage entier rejoué** | 160 épisodes générés ; 3 840 actions d'oracle | 3,58 h ; 5,19 h | 5,52 ; 9,65 USD | échéance à 6,5 h : 10,97 USD [L12] |
| **3, course** (12 tours) | 640 épisodes générés ; 10 230 actions d'oracle (3 840 aux tours, 3 830 hors tours, 2 560 à l'évaluation) | 10,56 h ; 16,49 h | 13,85 ; 25,24 USD [L13] | échéance calculée sur le compte de la voie (§ 4) |
| **voie entière** (12 tours) | | 16,5 h ; 24,2 h de carte | **23,16 ; 40,29 USD** [L15] | **43,61 USD** [L16] |

**Dépense au-delà du crédit chez le loueur** (12,995 USD le 22 novembre à 14:11Z, balance 0) : **10,16 USD** à l'attendu, **27,29** au haut, **30,62** au pire [L17]. Aucune création ne part sans recharge par Lazar (§ 4).

**Ce que ce devis apprend au directeur.** Rien n'est mesuré du chemin neuf. La voie ne mène à une course de 12 tours sous 44 USD que si le chemin neuf est au moins 2,8 à 3,1 fois plus rapide que le rythme relevé [L20]. L'essai de vitesse le dit pour 3,80 à 6,14 USD, avant l'étalonnage.

## 1. Ce qui est mesuré, et ce qui ne l'est pas

| grandeur | valeur | source | ligne |
|---|---|---|---|
| prix | carte 1,16 + stockage 0,033333 = **1,193 USD par heure** (machine 61875617) | chiffres de l'exécutante | [L01] |
| de la création au début du run | **≈ 70 min** (machine 61875617) ; 550 s sur la machine du 19 novembre | chiffres ; devis scellé § 2 | [L06] |
| rythme de l'ancien code sur 61875617 | 27 lots en ≈ 11,5 h, soit **5,29 fois** les durées du devis scellé | chiffres ; calcul | [L03] |
| durées du devis scellé (machine du 19 novembre, même code de tirage) | 39,08 s par épisode ; 0,511 s par action d'oracle | devis scellé § 1 | [L02] |
| déjà dépensé sous `GO-2026-11-21-70` | 16,1 + 0,12 = **16,22 USD** ; stockage de 61875617 à l'arrêt : 0,80 USD par jour | chiffres § 4 | [L07] |

- **Deux machines, un seul code, deux rythmes.** Le code de tirage sur processeur a donné 39,08 s par épisode le 19 novembre et environ cinq fois plus sur 61875617. La lenteur tient donc à la machine autant qu'au code. Le diagnostic (tirage jeton par jeton sur le processeur) vient d'une lecture du code, il n'est pas mesuré (compte rendu 30 de l'exécutante).
- **Un seul total.** Seule la durée des 27 lots réunis est connue. Le partage de la lenteur entre l'épisode et l'action d'oracle ne l'est pas. Ce devis applique un même facteur aux deux : c'est une hypothèse.
- **Rien n'est mesuré du chemin neuf** : ni sa vitesse, ni sa reproductibilité. C'est l'objet de l'étape 1.

## 2. Hypothèses et marges

| jeu | rythme, en fois les durées du devis scellé | mise en route | prix horaire | forfait de téléchargement, par machine | arrêt avant destruction | ligne |
|---|---|---|---|---|---|---|
| attendu | 1,06 (chemin neuf 5 fois plus rapide que le rythme relevé) | 70 min | 1,193 (relevé) | 1,04 (relevé sur l'offre de 61875617) | 6 h à 0,033 | [L10] |
| haut | 1,76 (3 fois plus rapide) | 70 min | 1,38 (borne) | 2,00 (borne) | 6 h à 0,08 | [L10] |
| pire | celui des gardes : 43,61 USD | | 1,38 | 2,00 | | [L16] |

- **Les facteurs 5 et 3** sont ceux des chiffres de l'exécutante (§§ 2 et 3) : ce sont des hypothèses de travail. Le facteur 5 ramène aux durées du devis scellé.
- **Épisodes du maître, régénérés, flagrants** : comptés comme un épisode honnête, comme au devis scellé (§ 2) ; aucune durée mesurée.
- **Trois locations**, l'une après l'autre : le lanceur de session refuse toute création tant qu'une machine du saboteur est sur le compte, arrêtée comprise (additif, § 1, C2). Chaque machine est détruite avant la création de la suivante. Six heures d'arrêt avant destruction sont comptées par machine.
- **Machine** : celle de l'ordre scellé (A100 SXM4 80 Go, au plus 1,30 USD par heure, stockage au plus 0,08, téléchargement au plus 0,05 USD par gigaoctet, disque d'au moins 100 gigaoctets).

## 3. Les trois étapes

**Étape 1 — essai de vitesse.** Une mise en route, un lot honnête par l'ancien chemin (au rythme relevé : 34,8 min [L04]), le même lot deux fois par le chemin neuf, 20 min de marge [L11]. Il ne produit que des durées et une égalité d'empreintes ; rien n'en est cité comme mesure.

**Règle de décision, par programme, écrite avant l'essai** : `python3 -I calcul-devis-voies-A-B-v1.py essai-de-vitesse EPISODE_S ACTION_S DEPENSE_ESSAI_USD`. Elle applique la formule du plafond de tours du texte scellé (10.2) aux durées mesurées du chemin neuf. « PART » si 12 tours au moins sont financés ; « NE PART PAS » sinon : aucune création de l'étalonnage, nœud.

| | passe jusqu'à | soit un chemin neuf au moins | ligne |
|---|---|---|---|
| essai à sa dépense attendue (3,80 USD) | 1,89 fois les durées du devis scellé | 2,80 fois plus rapide que le rythme relevé | [L20] |
| essai à sa dépense haute (5,40 USD) | 1,73 fois | 3,06 fois plus rapide | [L20] |

Cas sain et artefact de la règle (R5) : [L21], « PART », 27 tours ; [L22], « NE PART PAS », chemin neuf aussi lent que l'ancien.

**Étape 2 — étalonnage entier rejoué.** Les 160 épisodes et les 3 840 actions d'oracle du texte scellé (10.1), par le chemin neuf, avec une entropie neuve.

| | durée | dépense, forfait et arrêt compris | ligne |
|---|---|---|---|
| attendu | 3,58 h | 5,52 USD | [L12] |
| haut | 5,19 h | 9,65 USD | [L12] |
| borne (échéance à 6,5 h) | 6,5 h | 10,97 USD | [L12] |

**Étape 3 — course**, si la désignation rend l'oracle à contexte réécrit ou l'oracle au contexte de l'agent.

| tours | attendu : durée, dépense | haut | ligne |
|---|---|---|---|
| 12 (taille d'origine) | 10,56 h ; 13,85 USD | 16,49 h ; 25,24 USD | [L13] |
| 24 | 15,55 h ; 19,80 USD | 24,81 h ; 36,72 USD | [L14] |

Voie entière : 23,16 USD (12 tours) à 29,12 (24 tours) à l'attendu ; 40,29 au haut pour 12 tours. À 24 tours et au haut, 51,77 USD : au-dessus du plafond ; le plafond de tours l'interdit d'avance (§ 5) [L15].

## 4. Plafond, coupure, échéance, crédit

**Plafond : 44 USD. Coupure : 42 USD de dépense neuve de la voie.** Le pire tenu par les gardes est 42 + 0,92 (consignation) + 0,69 (marge de destruction) = **43,61 USD** [L16] [L08].

**Ce qui tient la coupure : l'échéance de chaque machine, non l'épuisement calculé par le lanceur.** La garde du lanceur exige « plafond de la configuration (55) + dépense antérieure ≤ plafond de la ligne (60) » : elle refuse toute dépense antérieure déclarée au-dessus de 5 USD. À 5 USD déclarés, une machine pourrait dépenser 48 USD avant l'arrêt par épuisement (vérification par exécution : `sortie-verification-gardes-du-lanceur-v1.txt`, `43e433d5ae0694bd3652d7fa9b796c8601a9c6ef0028165ac0790d6eee4ae0eb`, §§ 1 et 5). L'additif (§ 1, C3) donne donc à chaque machine une échéance calculée par programme sur le compte de la voie : heures permises = (42 − compte − 2,00) / 1,38, bornées par l'étape. Exemples : [L53] à [L55]. **À l'échéance, la minuterie consigne et pousse ce qui est écrit, puis détruit la machine** : c'est une destruction, non un arrêt.

**Garde de rythme de la course** : si le tour 1, puis le tour 4, ne sont pas écrits dans le délai calculé sur le compte, arrêt par l'identifiant. Pour 12 tours : tour 1 avant 1,21 h au compte attendu, avant 1,02 h au compte haut [L23] [L24]. Au rythme trois fois plus rapide, il reste 20,71 h permises pour 16,49 h attendues [L25].

**Échéance.** Échéance de la voie : 2026-11-27 (`GO-2026-11-22-71`). Minuterie au plus tard le 2026-11-27T22:00:00Z ; fin de la ligne le 2026-11-28T00:00:00Z ; **aucune création à partir du 2026-11-27T00:00:00Z**, comme l'ordre scellé [L52]. Une course créée à la dernière minute garde 22 heures : assez pour le haut (16,49 h).

**Crédit.** Avant chaque création, le crédit lu chez le loueur couvre le pire de la machine à créer plus 2 USD ; sinon aucune création, nœud (additif, § 1, C7). Le crédit est commun aux autres machines du compte : leur consommation n'est pas dans ce devis.

**Lecture du plafond de 44 USD (nœud).** Ce devis lit 44 USD comme le plafond de la dépense neuve de la voie : c'est la lettre de la colonne du registre. Les chiffres de l'exécutante (§ 4) y voyaient un total de la ligne `GO-2026-11-21-70`, passé compris. Dans cette seconde lecture, la dépense neuve permise tombe à 26,98 USD : l'attendu (23,16) y tient, le haut (40,29) non [L18]. Et les deux voies ne tiennent pas ensemble sous la coupure de 55 : il reste 37,98 USD pour un attendu de 39,38 [L51].

## 5. Plafond de tours et fichier d'entrées de la voie (A)

Le code fige trois valeurs du fichier d'entrées : plafond 45 USD, coût fixe 6,90, prix 1,38. Seule la dépense passée s'écrit. La voie planifie sous sa coupure moins la même réserve que le devis scellé (10 USD) : 42 − 10 = 32 USD. La **dépense passée écrite** vaut donc 45 − 32 + dépense relevée de l'essai de vitesse = **13,00 USD + essai** [L19]. Les 13 USD sont une écriture, non une dépense.

| | dépense passée écrite | plafond de tours | ligne |
|---|---|---|---|
| attendu (5 fois plus rapide) | 16,80 USD | 27 tours | [L19] |
| haut (3 fois plus rapide, essai à 5,40 USD) | 18,40 USD | 11 tours : « ne part pas », motif « tours » | [L19] |
| 3 fois plus rapide, essai au plus à 5,13 USD | | 12 tours ou plus | [L25] |

Le coût fixe scellé (6,90 USD) est calculé aux durées du devis scellé ; à un rythme plus lent il est sous-estimé, et la réserve de 10 USD l'absorbe.

## 6. Liste d'arrêt (résumé ; le texte qui fait foi est l'additif, § 5)

| arrêt | quand | action |
|---|---|---|
| un champ entre chevrons, une machine du saboteur sur le compte, crédit insuffisant, échéance refusée par le programme, création à partir du 27 novembre 00:00Z | avant toute création | aucune création |
| « NE PART PAS » à l'essai de vitesse ; chemin neuf non reproductible à graines égales | fin de l'étape 1 | aucune création de l'étalonnage ; nœud |
| suite d'essais en échec ; gardes du texte scellé ; coupure propre de l'étalonnage (16 USD avec le correctif 0013) ; échéance | étape 2 | ce qui existe est versé avec son motif ; machine arrêtée ou détruite par la minuterie |
| issue « ne part pas » ou « non calculable » | désignation | la course ne part pas ; phrases écrites d'avance |
| garde de rythme ; échéance ; gardes | course | arrêt par l'identifiant ; la course est consommée |
| tour de contrôle ; consigne sans effet ; moins de 48 épisodes acceptés | course | fins écrites d'avance : la course a abouti |
| l'autre voie a abouti la première | à tout moment | plus aucune création |

Aucun arrêt n'est suivi d'une relance sans nœud de Lazar et devis neuf.

## 7. Réserves

1. Rien n'est mesuré du chemin neuf ; les totaux des étapes 2 et 3 extrapolent deux rythmes mesurés avec l'ancien chemin.
2. Un même facteur est appliqué à l'épisode et à l'action d'oracle ; leur partage réel n'est pas connu.
3. Les tours du maître, la distillation et l'évaluation n'ont aucune durée réelle (réserve du devis scellé, inchangée).
4. La mise en route de 70 min est celle d'une seule machine.
5. La dépense passée de 16,22 USD vient des chiffres de l'exécutante, non d'une facture.
6. Le rédacteur n'a pas lu le correctif du tirage sur la carte (à venir), ni la manière de lancer l'essai de vitesse.
7. La coupure de la voie est tenue par des échéances qui détruisent la machine après consignation ; ce qui n'est pas poussé à cet instant est perdu.

## 8. Choix pour Lazar

| choix | recommandation | confiance |
|---|---|---|
| lecture du plafond de 44 USD | **dépense neuve de la voie**, coupure 42 ; l'autre lecture laisse 26,98 USD : l'attendu (23,16) y tient, le haut (40,29) non [L18] | moyenne |
| recharge du crédit | **au moins 31 USD pour la voie (A) seule** (pire : 30,62 au-delà du crédit) ; 11 USD suffisent à l'attendu ; les deux voies : 84,22 au pire, 26,38 à l'attendu [L50] | forte |
| réserve des tours | **10 USD**, comme au devis scellé | moyenne |
| sens de « réussit » | **arriver à une fin écrite d'avance, quel que soit le sens du résultat** (additif, § 1, C5) | forte |

Défaut sous 48 heures : aucun ; aucune création sans la recharge et sans le mot de Lazar sur la lecture du plafond.
