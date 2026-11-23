Rédigé par Claude Opus 5.5 en remplacement de Fable 5.2 (limite atteinte) : À REVOIR PAR FABLE avant scellement.

# Devis — voie (A) du saboteur à budget (v5) : tirage sur la carte ; essai de vitesse en tête de l'étalonnage, étalonnage entier rejoué, puis course — v1, brouillon 3

- **Statut** : brouillon 3, pièce décisive (devis). Écrit le 2026-11-22 vers 16:50Z (`date -u`) par Claude Opus 5.5, rédacteur de remplacement de Claude Fable 5.2 (limite atteinte), du côté du saboteur, sous le mandat `mandat-fable-brouillon3-voie-A-v1.md` (`f1bfb4bd707df326389b5cf022700c3e27bfbf6a813d9e42ad7541da35ac2835`), suite du mandat `0ead00d9ac01ed0a28367246f37118aeca79daea468993de0e094679a62aaf0f`. **À revoir par Fable avant scellement.** Les brouillons 1 (`12dd845cb700c83388a0705c41d029069edbb769ddc9e6b7b8f4bcedbf86aca6`) et 2 (`devis-voie-A-v1-brouillon2.md`, `9b48987ba823426ed4c7a4c564bdeeec2290ad9a24cb54a4d06da2d0c9ff119e`) restent intacts (R12). Aucune dépense n'est engagée par ce document. Vérification des corrections par le même contre-lecteur avant tout scellement.
- **Cause de la version** : la vérification du brouillon 2 (`note-verification-brouillon2-voie-A-cl1.md`, `6be4c5c73642b0fae068fadb94365ea59770b0c32de9d866c9e4e51ee9e40b20`, « pas encore scellable ») ; la correction étroite de la garde de dépense (`GO-2026-11-22-77`, option (b), correctif 0023). Différences, une par ligne : `differences-voie-A-brouillon2-vers-3-v1.md`.
- **Accord cité** : `GO-2026-11-22-75` (`registres/go.md` de `main`, tête `187f4c41b4a8bcf7c2c4d6206836e6b61858f5c9`, empreinte du registre `3db30eb98fed1488934cb53466f058510521b606dd8fd3fe1f84a5c06cb56b19`) : « Saboteur à budget, voie (A) : code du tirage corrigé (0020), essai de vitesse court, étalonnage entier rejoué, puis course ; dépense neuve, distincte de GO-2026-11-21-70. Mot de Lazar vers 14:50Z : « Ce qu'il faut pour que (A) parte : go » ; voie (B) gardée pour plus tard, non abandonnée. Départ après l'additif de Fable et le devis, scellés. » Plafond **60 USD**, échéance **2026-11-30**. Et `GO-2026-11-22-73` : « (A), code corrigé : environ 27 USD. go » ; recharge automatique activée chez le loueur. Et `GO-2026-11-22-77` : « saboteur : correction étroite de la garde, option (b), « go » ; Vast rechargé de 30 USD, recharge automatique active » (registre relu à la tête `3b7d0398b0e0a20582bf11807fed3592e210c539`, `e765c0cec158887acd39ff8ef1594f05dd30f2801e7d9f627f75858a1e38251e`).
- **Ordre chiffré** : `additif-ordre-course-voie-A-v1-brouillon3.md`, à côté (son empreinte est dans son compagnon). Texte scellé de l'organisme retenu (`c1dc54597a1ab4b467331673607d986e46a706c06253bb40070e5d15caaa61f2`) ; devis scellé de la première ligne (`cb881522378ace662787a7097c2baa6d461c766d70782d28636c132ce09f3ee8`) et son erratum 1 (`90342292f52daf2f7281acad68006598450033367d3a36aa1c6c72eac9150f9a`), dont ce devis reprend la forme, les durées de base, le plafond et la coupure.
- **Arithmétique** : `calcul-devis-voie-A-v3.py` (`a6c959f467ad4e7fed300b5a6bd085eab9c7689c0af4b41815ce97ceaa0896dd`), sortie `sortie-calcul-devis-voie-A-v3.txt` (`f8a5df582f6b25e816101b483e97cfdb892b7b49778db865290e4a034da24613`), à côté ; seules [M24], [M25] et [M27] changent depuis la v2. Chaque chiffre renvoie à une ligne [Mnn] de cette sortie.
- **Lu** : des durées, des prix et des comptes (`registres/iib-executante/chiffres-devis-code-corrige-v1.md`, `4e10a0047e1db340910bd9d41291a5210d787ad340876fd8649f91542963f710`) ; les rapports du développeur sur le tirage (`rapport-developpeur-course-v5-v4.md`, `0678ab7ac0ff6ae2900735adfd73f82ec8679b93d0c45786137401ed4057e543` ; `…-v5.md`, `53f476a541cff1e11b8a910179f14f85e82c81c654fd1535651e7c06c2d1abb2`) et la contre-lecture du correctif 0020 (`90f6ac3c949a7f5841b14b716cf68a0d6c6547d0344c0a3388cfa20f2de03f9a`). Aucune sortie de mesure, aucune consigne privée, aucune pièce du côté des sondes.

## 0. En bref — les quatre chiffres

| attendu | haut | au pire | plafond | coupure |
|---|---|---|---|---|
| **≈ 19,4 USD** (12 tours, tirage cinq fois plus rapide que le rythme relevé) [M13] | **≈ 34,9 USD** (trois fois plus rapide, prix aux bornes) [M13] | **59,76 USD**, tenu par les gardes [M14] | **60 USD** (GO-2026-11-22-75) | **55 USD** (configuration) |

C'est de la dépense neuve, sous une ligne à part : la forme et les trois derniers chiffres sont ceux du devis scellé de la première ligne.

| étape | appels | durée attendue ; haute | coût attendu ; haut | ce qui la borne |
|---|---|---|---|---|
| **1, étalonnage entier rejoué**, essai de vitesse en tête | 160 épisodes générés ; 3 840 actions d'oracle | 3,58 h ; 5,19 h | 5,52 ; 9,65 USD [M11] | essai de vitesse au lot 2 ; règle de la surveillance à 16 USD |
| **2, course** (12 tours) | 640 épisodes générés ; 10 230 actions d'oracle | 10,56 h ; 16,49 h | 13,85 ; 25,24 USD [M12] | garde de rythme ; échéance calculée sur le compte |
| **voie entière** (12 tours) | | 14,1 h ; 21,7 h de carte | **19,36 ; 34,89 USD** [M13] | **59,76 USD** [M14] |

**Les « environ 27 USD » de GO-2026-11-22-73** sont le cas « trois fois plus rapide » au prix relevé : 28,36 USD pour 12 tours [M13].

**Dépense au-delà du crédit lu le 22 novembre à 14:11Z** (12,995 USD) : 6,37 USD à l'attendu, 21,89 au haut, 46,77 au pire [M15]. La recharge automatique est activée (GO-2026-11-22-73).

**Ce que ce devis apprend au directeur.**
1. **Rien n'est mesuré du tirage sur la carte.** Sur processeur, le chemin neuf est plus lent que l'ancien (2 524 ms contre 1 961 ms pour 8 lignes de 64 jetons, rapport du développeur v4, § 5) ; le gain n'est attendu que sur la carte. Et rien ne prouve que l'ancien chemin causait la lenteur de l'étalonnage (contre-lecture du correctif 0020).
2. **La voie tient sous 55 USD tant que le tirage est au moins 1,96 fois plus rapide que le rythme relevé** [M17]. L'essai de vitesse le dit au lot 2 de l'étalonnage ; s'il arrête la voie, la dépense est de 3,7 à 6,0 USD [M19].
3. **Un essai de vitesse sur une machine à part n'existe pas** : aucun outil ne le lance. Il est joué en tête de l'étalonnage, sur les marques de progrès. La voie n'a que deux machines.

## 1. Ce qui est mesuré, et ce qui ne l'est pas

| grandeur | valeur | source | ligne |
|---|---|---|---|
| prix | carte 1,16 + stockage 0,033333 = **1,193 USD par heure** (machine 61875617) | chiffres de l'exécutante | [M01] |
| de la création au début du run | **≈ 70 min** (machine 61875617) | chiffres | [M02] |
| rythme de l'ancien chemin sur 61875617 | 27 lots en ≈ 11,5 h : **5,29 fois** les durées du devis scellé | chiffres ; calcul | [M03] |
| durées du devis scellé (machine du 19 novembre, ancien chemin) | 39,08 s par épisode ; 0,511 s par action d'oracle | devis scellé § 1 | [M02] |
| tirage sur la carte | **aucune durée sur une carte** ; sur processeur, plus lent que l'ancien | rapport du développeur v4, § 5 | — |

Un seul total est connu pour 61875617 : ce devis applique un même facteur à l'épisode et à l'action d'oracle. C'est une hypothèse.

## 2. Hypothèses et marges

| jeu | rythme, en fois les durées du devis scellé | mise en route | prix horaire | forfait de téléchargement, par machine | arrêt avant destruction | ligne |
|---|---|---|---|---|---|---|
| attendu | 1,06 (tirage 5 fois plus rapide que le rythme relevé) | 70 min | 1,193 (relevé) | 1,04 (relevé) | 6 h à 0,033 | [M10] |
| haut | 1,76 (3 fois plus rapide) | 70 min | 1,38 (borne) | 2,00 (borne) | 6 h à 0,08 | [M10] |
| limite de l'essai de vitesse | 2,70 (1,96 fois plus rapide) | 70 min | 1,38 | 2,00 | 6 h à 0,08 | [M17] |
| pire | celui des gardes : 59,76 USD | | 1,38 | 2,00 | 48 h à 0,08 | [M14] |

- **Les facteurs 5 et 3** sont ceux des chiffres de l'exécutante : des hypothèses de travail.
- **Épisodes du maître, régénérés, flagrants** : comptés comme un épisode honnête ; aucune durée mesurée. Pour cette raison, l'essai de vitesse et la garde de la course comptent la course **1,2 fois plus lente** que l'étalonnage.
- **Deux locations**, l'une après l'autre : le lanceur de session refuse toute création tant qu'une machine du saboteur est sur le compte, arrêtée comprise. La machine de l'étalonnage est détruite avant la création de celle de la course.
- **Machine** : celle de l'ordre scellé (A100 SXM4 80 Go, au plus 1,30 USD par heure, stockage au plus 0,08, téléchargement au plus 0,05 USD par gigaoctet, disque d'au moins 100 gigaoctets).

## 3. Les deux étapes

**Étape 1 — étalonnage entier rejoué, essai de vitesse en tête.** Les 160 épisodes et les 3 840 actions d'oracle du texte scellé (10.1), par le tirage sur la carte, avec une entropie neuve.

| | durée | dépense, forfait et arrêt compris | ligne |
|---|---|---|---|
| attendu | 3,58 h | 5,52 USD | [M11] |
| haut | 5,19 h | 9,65 USD | [M11] |
| coupé par la règle de la surveillance (16 USD comptés) | | 20,76 USD tenus si rien ne part ensuite | [M14] |

**Essai de vitesse, par programme, écrit avant la création** : `python3 -I calcul-devis-voie-A-v3.py rythme-etalonnage 55 0`. Il rend un délai : **la marque du lot 2 de l'étalonnage est relevée au plus tard 35,5 minutes après la marque de début** ; au-delà, arrêt par l'identifiant [M18]. Ce délai correspond à 2,70 fois les durées du devis scellé : jusque-là, l'étalonnage et une course de 12 tours comptée 1,2 fois plus lente tiennent sous 55 USD aux prix bornes (54,93 USD), et la formule du texte scellé finance encore 17 tours [M17].

| rythme | la marque du lot 2 vient à | décision | ligne |
|---|---|---|---|
| attendu | 13,9 min | l'étalonnage continue (cas sain) | [M18] |
| haut | 23,2 min | l'étalonnage continue (cas sain) | [M18] |
| celui de 61875617 | 69,6 min | arrêt à 35,5 min (artefact) | [M18] |

Voie arrêtée par l'essai de vitesse : 2,26 h de carte ; 3,73 USD au prix relevé ; 6,04 USD au plus [M19].

**Étape 2 — course**, si la désignation rend l'oracle à contexte réécrit ou l'oracle au contexte de l'agent.

| tours | attendu : durée, dépense | haut | ligne |
|---|---|---|---|
| 12 (taille d'origine) | 10,56 h ; 13,85 USD | 16,49 h ; 25,24 USD | [M12] |
| 24 | 15,55 h ; 19,80 USD | 24,81 h ; 36,72 USD | [M12] |

Voie entière : 19,36 USD (12 tours) à 25,32 (24 tours) à l'attendu ; 34,89 à 46,36 au haut [M13].

**Garde de la course, par programme** : `python3 -I calcul-devis-voie-A-v3.py garde-de-rythme 55 COMPTE TOURS $(date +%s) MINUTES_ETALONNAGE`. Avant la création, elle refuse une course qui, au rythme relevé de l'étalonnage compté 1,2 fois plus lent, ne tient pas dans les heures de son échéance. Sinon elle rend deux délais : pour 12 tours, tour 1 au plus tard 85 minutes après la marque de début de la course, tour 4 au plus tard 324 minutes [M20] [M21]. Au rythme haut, elle admet au plus 24 tours, quand la formule du texte scellé en finance 30 : au-delà, aucune création, nœud [M22] [M23].

## 4. Plafond, coupure, échéance, crédit

**Plafond : 60 USD. Coupure : 55 USD**, celle que la configuration porte et que le code exige à l'égalité. Les gardes tiennent au plus 55 + 0,92 (consignation) + 3,84 (48 heures de stockage à l'arrêt) = **59,76 USD** [M14], comme au devis scellé.

**Ce qui tient la coupure pendant la course.** Sous le correctif 0023 (`GO-2026-11-22-77`, option (b)), la garde du lanceur juge la ligne comme avant, exige plafond de la configuration ≤ plafond de la ligne et dépense antérieure < plafond de la ligne, et passe à la garde de dépense le plafond total min(60, 55 + dépense antérieure). La machine dépense donc au plus **min(55, 60 − compte)** : jamais plus que le plafond scellé, jamais un total au-delà de 60 USD ; à un compte ≤ 5, rien ne change. La dépense antérieure déclarée est **le compte vrai de la voie**, arrondi au centime supérieur, sans borne. Vérifié par exécution au commit du correctif 0023 (`sortie-verification-gardes-du-lanceur-v3.txt`, `a3b9f3b121f0dc03f83f0daa241018429865846f26fb9a58bfbb0731fbe92c50`, § 2) : cas sains, 5,52 et 9,65 USD acceptés (machine 54,48 et 50,35) ; artefact, un compte de 60 ou plus refusé. Vérification du correctif par son contre-lecteur : en attente (champ de l'additif). L'épuisement calculé par le lanceur tient le total sous 60 USD ; l'échéance, calculée par programme sur la coupure de 55 et le compte, heures permises = min(30, (55 − compte − 2,00) / 1,38) [M24] à [M26], le précède toujours [M27]. Le pire reste de 59,76 USD [M14]. **À l'échéance, la minuterie consigne et pousse ce qui est écrit, puis détruit la machine.**

**Échéance.** Échéance de la ligne : 2026-11-30. Échéance de toute minuterie au plus tard le 2026-11-30T22:00:00Z ; fin de la ligne le 2026-12-01T00:00:00Z ; **aucune création à partir du 2026-11-27T00:00:00Z** (ordre scellé ; le code refuse dès le 27) [M28].

**Crédit.** La recharge automatique est activée chez le loueur (GO-2026-11-22-73). Le crédit est relu avant chaque création ; s'il ne couvre pas le pire de la machine à créer et que la recharge n'a pas joué, aucune création, nœud. Le crédit est commun aux autres machines du compte.

## 5. Plafond de tours et fichier d'entrées

Le fichier d'entrées est **le fichier scellé de l'étalonnage, inchangé** (`44f90de6e4b46b2931f2d0aa7fb7cbd614c5331be5859cf2ecb2a3ad0d09c74d`) : plafond 45 USD (la coupure moins la réserve de 10), dépense passée 0, coût fixe 6,90, prix 1,38, 3 830 actions d'oracle hors tours, plafond de tours en formule. La dépense passée est bien nulle : aucune machine de la ligne ne précède l'étalonnage.

| | tours financés par la formule du texte scellé (10.2) | ligne |
|---|---|---|
| attendu | 56 | [M16] |
| haut | 30 | [M16] |
| à la limite de l'essai de vitesse | 17 | [M17] |

Le coût fixe scellé (6,90 USD) est calculé aux durées du devis scellé ; à un rythme plus lent il est sous-estimé. La garde de la course (§ 3) compte les durées réelles : c'est elle qui refuse une course trop longue pour la coupure.

## 6. Liste d'arrêt (résumé ; le texte qui fait foi est l'additif, § 5)

| arrêt | quand | action |
|---|---|---|
| un champ entre chevrons ; une machine du saboteur sur le compte, 61875617 comprise ; crédit insuffisant sans recharge ; code 3 d'un programme ; création à partir du 27 novembre 00:00Z ; commande de création imprimée sans `-e IIB_TIRAGE=carte` | avant toute création | aucune création |
| garde de dépense du correctif 0023 en refus (`go` ou `plafond-total` en code non nul : compte de 60 USD ou plus, compte illisible, ligne échue ou révoquée) | avant toute création | aucune création ; nœud |
| journal de l'amorce (`TIRAGE=`) ou marque de chargement (`tirage`) autre que `carte` | étalonnage ou course | arrêt par l'identifiant ; nœud |
| suite d'essais en échec, essai du tirage sur la carte compris ; gardes du texte scellé | étalonnage, avant le premier épisode ou pendant | ce qui existe est versé avec son motif ; machine arrêtée |
| marque du lot 2 absente au délai de l'essai de vitesse | étalonnage | arrêt par l'identifiant ; nœud |
| 16 USD comptés avant la fin de l'étalonnage | étalonnage | arrêt par l'identifiant ; nœud |
| issue « ne part pas » ou « non calculable » | désignation | la course ne part pas ; phrases écrites d'avance |
| course qui ne tient pas dans les heures de son échéance | avant la création de la course | aucune création ; nœud |
| garde de rythme ; échéance ; gardes | course | arrêt par l'identifiant ; la course est consommée |
| tour de contrôle ; consigne sans effet ; moins de 48 épisodes acceptés | course | fins écrites d'avance : la course a abouti |

Aucun arrêt n'est suivi d'une relance sans nœud de Lazar et devis neuf.

## 7. Réserves

1. Rien n'est mesuré du tirage sur la carte ; sur processeur il est plus lent que l'ancien chemin ; la cause de la lenteur de 61875617 n'est pas établie.
2. Un même facteur est appliqué à l'épisode et à l'action d'oracle ; leur partage réel n'est pas connu.
3. Les tours du maître, la distillation et l'évaluation n'ont aucune durée réelle ; la tolérance de 1,2 est un choix du rédacteur.
4. La mise en route de 70 min est celle d'une seule machine.
5. L'essai de vitesse se lit sur deux lots de l'étalonnage : il ne compare pas l'ancien chemin au neuf sur la même machine.
6. La coupure est tenue, pendant la course, par une échéance qui détruit la machine après consignation ; ce qui n'est pas poussé à cet instant est perdu.
7. Le correctif 0021 est vérifié (« autorisable ») ; les correctifs 0022 et 0023 sont en vérification ; l'arbre du code de la voie est en attente.

## 8. Choix pour Lazar ou pour la mère

| choix | recommandation | confiance |
|---|---|---|
| forme de l'essai de vitesse | **en tête de l'étalonnage, sur les marques de progrès** ; un essai sur une machine à part demanderait un script contre-lu et environ 2,5 heures | moyenne |
| tolérance de la course sur l'étalonnage | **1,2** | moyenne |
| coupure | **55 USD**, plafond 60, comme au devis scellé | forte |
| liste des essais de l'étalonnage | **version neuve, avec l'essai du tirage sur la carte** ; sinon cet essai n'est vu qu'après l'engagement de la course | forte |

Défaut sous 48 heures : les recommandations ci-dessus ; aucune création avant le scellement de l'additif et de ce devis par la mère.
